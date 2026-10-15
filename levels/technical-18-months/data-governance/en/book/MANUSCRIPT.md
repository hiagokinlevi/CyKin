# Data Governance: Technical Course

- Language: English (`en`); course 049, Technical course (18 months).
- Editorial state: **published**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical students preparing to work as data technicians who enter, check, fix and protect data under agreed rules.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs compare a synthetic timetable with passenger count records to find trips without counts by route, and normalise synthetic bus stop names to find how many real stops lie behind the variations. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one technical student from forms, spreadsheets and simple Python checks through quality, completeness, names and codes, personal data, security, sharing and retention to issue logs, documentation, stewardship, a placement and a practical assessment. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Marta Kowalski** | Technical student | Invented |
| **Mr. Daniel Osei** | Trainer | Invented |
| **Southport Technical College** | Fictional college | Invented |
| **Linkway Buses** | Fictional bus operator, sixty buses on twelve routes | Invented |

### Core sources

Wang and Strong (1996); GDPR. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Starting at Southport

### Learning outcomes

You will (1) describe the technical course and its case; (2) explain what data governance means for a technician; (3) prepare to learn through practice.

### 1.1 The student

Marta Kowalski begins an eighteen-month technical course in data administration at the fictional Southport Technical College. Her trainer, Mr. Daniel Osei, explains that technicians handle data every day: entering it, checking it, fixing it and keeping it safe. The course follows a fictional partner company, Linkway Buses, which runs sixty buses on twelve routes in a mid-sized town and records tickets, passenger counts, timetables and staff hours. All data in exercises and labs are synthetic, created for teaching only. Marta is ready.

### 1.2 Governance for technicians

Mr. Osei explains data governance simply: agreeing who is responsible for each kind of data, what rules it must follow and how it is kept safe. Technicians do not usually make those decisions, but they apply the rules and notice when something goes wrong. Marta learns that her role is to follow procedures carefully, check data, report problems to the right person and suggest improvements based on what she sees in daily work. Marta writes this description of her role on the first page of her workbook.

### 1.3 Learning by doing

Most lessons involve practical tasks: checking a spreadsheet, writing a short Python script, filling in an issue form or reading a procedure. Mr. Osei asks Marta to keep a workbook recording each task, what went well and what was difficult. He explains that employers value technicians who can show evidence of their work, and that the workbook will help her prepare for the practical assessment at the end of the course. Marta starts the workbook on the first day, recording her first task and a question about it.

### 1.4 Linkway's needs

Linkway's data officer, a fictional figure named Mr. Hughes, visits the class. He explains that the company reports passenger numbers to the local transport authority, which part-funds some routes. Missing or wrong counts can reduce funding. He also mentions complaints about wrong stop names on the website and worries about protecting staff and passenger personal data. He asks students to help with practical checks during the course. Marta notes each need in her workbook, and the class agrees to start with passenger counts because funding depends on them.

### Worked example

Marta starts the technical course, learns that technicians apply rules and report problems, keeps a workbook of practical tasks and hears Linkway's needs around passenger counts, stop names and personal data.

> **Synthetic case.** Southport, Linkway and all people are synthetic.

### Errors and limits

Assuming governance belongs only to managers overlooks the technician's daily role.

### Exercises

- **EX001 — Linkway fleet.** How many buses does Linkway run? *Rubric:* 3 = sixty;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX002 — Technician duties.** What do technicians do in governance? *Rubric:* 3 = apply rules, check data and report problems;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX003 — Workbook purpose.** Why keep a workbook? *Rubric:* 3 = evidence of work for employers and assessment;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX004 — Funding risk.** Why do passenger counts matter for funding? *Rubric:* 3 = the authority part-funds routes based on them;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue studying — lesson 01 (chapter 01 of 18)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Data at a bus company

### Learning outcomes

You will (1) list the main data a bus company holds; (2) trace how passenger counts are collected; (3) identify who uses them.

### 2.1 Main data

Marta lists Linkway's data: timetables with routes, stops and departure times; ticket sales from machines on each bus; passenger counts from sensors at bus doors; driver rosters and hours; vehicle maintenance records; and customer complaints. Each is held in a different system or spreadsheet. She notes that timetables connect many data sets, because tickets, counts and rosters all refer to a scheduled trip identified by route and departure time. Marta draws a simple diagram showing each data set as a box, with lines to the timetable box in the centre.

### 2.2 How counts are collected

Sensors above each door count people getting on and off. At the end of each trip, the bus's onboard computer stores the totals with the trip identifier. When the bus returns to the depot at night, data upload over the depot wireless network. Marta notes that if a bus does not connect at the depot, its counts wait until the next night, and if the sensor fails, no counts are recorded for that trip at all. Mr. Hughes confirms both problems happen every month.

### 2.3 Who uses counts

Counts are used by planners deciding timetables, by managers reporting to the transport authority and by finance estimating revenue on funded routes. The transport authority uses them to decide funding. Marta realises that a missing count can lead planners to cut a busy trip or the authority to reduce funding for a route that people rely on. She writes in her workbook that data errors can affect bus services for passengers. She adds each user to her diagram with a short note about what they decide using counts.

### 2.4 Where errors enter

Marta marks points where errors can enter: faulty sensors, uploads that fail, timetable changes not loaded into onboard computers and manual corrections in spreadsheets. Mr. Osei asks her to rank them by how often she thinks they happen and how much harm they cause. She ranks faulty sensors and failed uploads highest. He explains that this kind of simple ranking helps decide where checks are most needed before investing time. Marta notes that her ranking is a first guess, which she will test with real checks later in the course.

### Worked example

Marta lists Linkway's data with timetables as the link, traces counts from door sensors through depot uploads, identifies planners, managers, finance and the authority as users and ranks error points.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

Ignoring how data are collected hides where errors begin.

### Exercises

- **EX005 — Linking data.** Which data set connects many others? *Rubric:* 3 = timetables;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX006 — Upload timing.** When do counts upload? *Rubric:* 3 = at night at the depot;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX007 — Missing count harm.** What harm could a missing count cause? *Rubric:* 3 = a busy trip cut or funding reduced;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX008 — Top error points.** Which error points did Marta rank highest? *Rubric:* 3 = faulty sensors and failed uploads;; 2 = both;; 1 = one;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue studying — lesson 02 (chapter 02 of 18)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Records and forms

### Learning outcomes

You will (1) design forms that collect good data; (2) use required fields and lists; (3) check forms with users.

### 3.1 Paper and screen forms

Linkway collects some data through forms: complaints from passengers, incident reports from drivers and lost property records. Marta reviews the complaint form and finds free text for the route, date and stop, so staff write routes in many ways, such as route 7, number 7 and the hospital bus. She notes that free text makes later analysis hard, because the same route appears under different names. She counts eleven different ways of writing route numbers in a single month of synthetic complaints, which shows how large the problem is for anyone analysing them.

### 3.2 Better design

Marta redesigns the complaint form for the website: route chosen from a list, date from a calendar, stop from a list filtered by route and a free text box for the description. Required fields are marked clearly. She keeps the form short, asking only for information needed to handle the complaint. She explains that good forms prevent errors at the start, which is easier than fixing them later in spreadsheets. Mr. Hughes approves the design for testing before it goes on the website.

### 3.3 Contact details

The old form asked for the passenger's full address, date of birth and phone number. Marta asks Mr. Hughes why. He says only an email or phone number is needed to reply. She removes the address and date of birth. Mr. Osei explains that collecting only what is needed is a data protection principle and also makes forms quicker to complete, so more passengers finish them. Mr. Hughes agrees, and the next version of the form asks only for an email address or a phone number, with a choice of which to use.

### 3.4 Testing with users

Marta asks three classmates and two Linkway staff to complete the new form. One staff member points out that some stops share names on different routes, so the stop list must show the route. Another finds the date calendar hard on a phone. Marta adjusts both. She learns that testing forms with real users finds problems designers miss, and records the changes in her workbook with reasons. The final form goes live on the website, and Mr. Hughes reports that complaints now arrive with the route and stop recorded correctly in nearly every case.

### Worked example

Marta finds free-text routes on the complaint form, redesigns it with lists and a calendar, removes unneeded address and date of birth fields and fixes problems found in user testing.

> **Synthetic case.** Forms are synthetic.

### Errors and limits

Free text for structured information makes analysis unreliable.

### Exercises

- **EX009 — Route variations.** Give one way staff wrote route 7. *Rubric:* 3 = number 7 or the hospital bus;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX010 — Removed contact fields.** Which fields did Marta remove? *Rubric:* 3 = full address and date of birth;; 2 = both;; 1 = one;; 0 = none.
- **EX011 — Stop list problem.** What problem did staff find with the stop list? *Rubric:* 3 = stops share names on different routes;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX012 — Calendar issue.** What was hard about the calendar? *Rubric:* 3 = using it on a phone;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue studying — lesson 03 (chapter 03 of 18)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Spreadsheets done safely

### Learning outcomes

You will (1) organise spreadsheets clearly; (2) protect formulas and add checks; (3) keep versions under control.

### 4.1 A messy spreadsheet

Linkway's monthly passenger report is built in a spreadsheet. Marta opens it and finds data pasted from the count system, formulas mixed with typed numbers, colours with no explanation and three hidden tabs. She cannot tell which figures are calculated and which were typed. Mr. Osei explains that spreadsheets like this are common and risky, because nobody can check them easily and one mistake can change every total. The person who built it has left the company, and the current preparer copies the steps without knowing why some of them exist.

### 4.2 Organising

Marta reorganises a copy: one tab for raw data pasted unchanged, one for calculations, one for the report and one explaining sources and steps. Calculated cells are shaded consistently, with a key. Typed adjustments go in a separate column with a reason. She removes hidden tabs after checking with the report owner that they are not needed. The new layout lets anyone see where each figure comes from. The report owner reviews the copy and agrees to use the new layout from the next month onwards.

### 4.3 Checks

Marta adds check cells: total passengers in the report must equal the total in the raw data, and the number of trips must match the timetable for the month. If a check fails, the cell turns red. She also protects formula cells so they cannot be overwritten by accident. Mr. Osei notes that simple checks catch most spreadsheet errors, and that protection prevents the most common mistake of typing over a formula. The first month's checks pass, which gives the owner confidence in the new layout.

### 4.4 Versions

The old report was saved as passenger report final, final2 and final latest. Marta sets up a naming convention with the year and month, saves each month's report in a dated folder and keeps the template separate. She writes the convention on the explanation tab. She notes that clear versions mean the authority can be sent exactly the version that was approved, and earlier versions can be found if questions arise. The report owner adopts the convention and asks other teams to use it too.

### Worked example

Marta reorganises a messy passenger report into raw, calculation, report and explanation tabs, adds red check cells and formula protection and replaces final-final names with dated versions.

> **Synthetic case.** Spreadsheets are synthetic.

### Errors and limits

Mixing typed numbers with formulas hides manual changes.

### Exercises

- **EX013 — Hidden tabs.** How many hidden tabs did Marta find? *Rubric:* 3 = three;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX014 — Adjustment column.** Where do typed adjustments go? *Rubric:* 3 = a separate column with a reason;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX015 — Trip check.** What must the trip count match? *Rubric:* 3 = the timetable for the month;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX016 — Version benefit.** What do clear versions allow? *Rubric:* 3 = sending exactly the approved version;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue studying — lesson 04 (chapter 04 of 18)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Checking data with Python

### Learning outcomes

You will (1) read a CSV file in Python; (2) write simple checks; (3) print a clear summary.

### 5.1 Reading a file

Mr. Osei introduces Python for repetitive checks. Marta writes a short script using the csv module to read a synthetic export of passenger counts. Each row has the date, route, trip time, boardings and alightings. She prints the number of rows and the first few rows to confirm the file was read correctly. She learns that checking the file reads properly is the first step before trusting any results from it. She also checks that the number of rows printed matches the number shown by the system export screen.

### 5.2 Simple checks

Marta writes checks: boardings and alightings must be whole numbers, not negative and not above one hundred and twenty, the bus capacity. The route must be one of Linkway's twelve routes. She counts rows failing each check. She notes that each check is a single clear rule, which makes it easy to explain to Mr. Hughes and to change if Linkway buys larger buses. She puts the capacity value at the top of the script as a named setting, so it can be changed in one place if Linkway ever buys larger buses.

### 5.3 Summaries

Marta prints a summary: rows read, rows failing each check and the share failing. She finds a few rows with negative alightings, which Mr. Hughes says come from a sensor fault on one bus. She adds the bus number to the output so the fault can be traced. She learns that a good summary helps someone act, not just know that something is wrong. Mr. Hughes passes the bus number to the maintenance team, who replace the faulty sensor that week, and the negative values stop appearing in later files.

### 5.4 Saving and sharing

Marta saves the script with comments explaining each step and the date. Mr. Osei shows her how to keep scripts in a shared folder with a short readme. When a classmate runs the script on a new month's file, it works without changes. Marta notes in her workbook that a script she can rerun saves hours compared with checking a spreadsheet by eye each month. Mr. Hughes asks for a copy of the script for Linkway's data team, and Marta adds a short note on how to run it.

### Worked example

Marta reads a counts file with csv, checks boardings against capacity and valid routes, adds bus numbers to trace a sensor fault and saves a commented script others can rerun.

> **Synthetic case.** Exports are synthetic.

### Errors and limits

Trusting results before confirming the file read correctly risks wrong conclusions.

### Exercises

- **EX017 — Capacity limit.** What upper limit did the check use? *Rubric:* 3 = one hundred and twenty;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX018 — Negative cause.** What caused negative alightings? *Rubric:* 3 = a sensor fault on one bus;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX019 — Traceability addition.** What did Marta add to trace faults? *Rubric:* 3 = the bus number;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX020 — Script sharing.** How are scripts shared? *Rubric:* 3 = a shared folder with a readme;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue studying — lesson 05 (chapter 05 of 18)

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Data quality basics

### Learning outcomes

You will (1) name common data quality dimensions; (2) apply them to passenger data; (3) pick the right check for each.

### 6.1 Dimensions

Mr. Osei introduces quality dimensions in plain words, based on Wang and Strong's research with data users. Completeness asks whether all expected data are present. Validity asks whether values follow the rules. Accuracy asks whether data match reality. Timeliness asks whether data arrive when needed. Consistency asks whether different systems agree. Marta writes an example from Linkway for each dimension in her workbook to help her remember them. Mr. Osei checks her examples and suggests one change for timeliness, which she makes so that it matches how Linkway actually uses counts.

### 6.2 Applying to counts

For passenger counts, completeness means every scheduled trip has a count. Validity means counts are whole, non-negative and below capacity. Accuracy means counts match the real number of passengers, which can be checked by a person counting on a sample of trips. Timeliness means counts upload by the next morning. Consistency means count totals roughly agree with ticket sales on the same trips. Marta writes these definitions in a table in her workbook, with one row per dimension and a column for the check that tests it at Linkway.

### 6.3 Choosing checks

Marta matches checks to dimensions. Her Python script covers validity. A comparison with the timetable covers completeness. A morning check of upload times covers timeliness. A monthly comparison with ticket sales covers consistency. Accuracy needs manual counts, which Mr. Hughes arranges on ten trips each month. She notes that no single check covers everything, so several simple checks together give a fuller picture. Mr. Hughes agrees to run the checks on a regular schedule, with the results shared each month with the operations manager and planners.

### 6.4 Quality for a purpose

Mr. Hughes explains that the authority cares most about completeness and accuracy, because funding depends on total passengers. Planners care more about timeliness, because they review busy trips weekly. Marta learns that quality depends on what the data are used for, so checks should focus on what matters most to each user. She adds a column to her table showing which users care about each dimension. Mr. Hughes uses the table to explain to the operations manager why manual counts are worth the time they take each month.

### Worked example

Marta learns five quality dimensions, applies them to passenger counts, matches checks to each including monthly manual counts for accuracy and notes which users care most about each.

> **Synthetic case.** Examples are synthetic; Wang and Strong (1996) is real.

### Errors and limits

Checking only validity misses missing or late data.

### Exercises

- **EX021 — Accuracy check.** How is count accuracy checked? *Rubric:* 3 = manual counts on sample trips;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX022 — Consistency comparison.** What are counts compared with for consistency? *Rubric:* 3 = ticket sales;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX023 — Authority priority.** Which dimensions matter most to the authority? *Rubric:* 3 = completeness and accuracy;; 2 = both;; 1 = one;; 0 = none.
- **EX024 — Planner priority.** Which dimension matters most to planners? *Rubric:* 3 = timeliness;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue studying — lesson 06 (chapter 06 of 18)

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Missing trip counts

### Learning outcomes

You will (1) compare counts with the timetable; (2) find routes with missing counts; (3) report the problem to the right person.

### 7.1 The check

Marta writes a check that compares the timetable with the count records. Every scheduled trip should have one count record. Trips without a record are listed by route. She explains that this completeness check matters most for funding, because the transport authority pays for funded routes based on reported passengers, and a missing count records zero passengers for that trip. She runs the check on one month of synthetic data covering three routes. She saves the check in the shared folder with her other scripts.

### Lab — Scheduled trips without passenger count records, by route

```python
"""Find scheduled bus trips with no passenger count record, by route (stdlib only)."""
import random
random.seed(12)
miss = {"Route 1": 0.01, "Route 4": 0.02, "Route 7": 0.09}
tot = 0
for r, p in miss.items():
    m = sum(random.random() < p for _ in range(1200))
    tot += m
    print(f"{r}: 1200 trips scheduled, {m} without counts ({100*m/1200:.1f}%)")
print(f"all routes: {tot} of 3600 missing ({100*tot/3600:.1f}%)")
```

Run with `python3 lab_trips.py`. Verified output:

```text
Route 1: 1200 trips scheduled, 12 without counts (1.0%)
Route 4: 1200 trips scheduled, 10 without counts (0.8%)
Route 7: 1200 trips scheduled, 122 without counts (10.2%)
all routes: 144 of 3600 missing (4.0%)
```

### 7.2 Results

The lab checks twelve hundred scheduled trips on each of three routes. Route 1 has 12 trips without counts, 1.0 percent. Route 4 has 10, 0.8 percent. Route 7 has 122, 10.2 percent. Across all three routes, 144 of 3,600 trips are missing, 4.0 percent. Marta notes that the overall figure hides the real problem: most missing counts are on Route 7, which is far worse than the other two routes. Marta writes the results in a small table with one row per route, so that the difference between Route 7 and the other routes is obvious to anyone who reads it, including managers who are not used to data.

### 7.3 Finding the cause

Marta shares the result with Mr. Hughes. He checks which buses run Route 7 and finds that two older buses on that route have sensors that often fail to save data. Route 7 is the hospital route, which the authority part-funds. Missing counts there could reduce funding for a route many patients and staff depend on. Mr. Hughes asks maintenance to repair the sensors and to move newer buses onto Route 7 meanwhile. Marta records the cause and the actions in her workbook, and plans to check Route 7 again after the repairs.

### 7.4 Reporting

Marta writes a short report: what she checked, the results by route, the likely cause, the action taken and a plan to rerun the check next month. She sends it to Mr. Hughes, who forwards it to the operations manager. Mr. Osei notes that reporting by route rather than as one overall figure made the problem visible, and that technicians should always look for where problems concentrate rather than only at totals. The operations manager thanks Marta and asks for the same check every month.

### Worked example

Marta compares timetable and counts, finds 144 of 3,600 trips missing (4.0 percent) with Route 7 at 10.2 percent, sees older buses' sensors as the cause and reports by route with a rerun plan.

> **Synthetic case.** Trips are synthetic; outputs come from lab_trips.py.

### Errors and limits

Overall percentages hide routes where problems concentrate.

### Exercises

- **EX025 — Route 7 share.** What share of Route 7 trips lacked counts? *Rubric:* 3 = 10.2%;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX026 — Overall missing.** How many trips were missing across all routes? *Rubric:* 3 = 144 of 3,600;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX027 — Route 7 cause.** What caused missing Route 7 counts? *Rubric:* 3 = sensors on two older buses;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX028 — Interim action.** What was done while sensors were repaired? *Rubric:* 3 = newer buses moved onto Route 7;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue studying — lesson 07 (chapter 07 of 18)

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Names, codes and standards

### Learning outcomes

You will (1) spot inconsistent names; (2) normalise text with simple rules; (3) agree a standard list with an owner.

### 8.1 Inconsistent stop names

Passengers complain that the website shows different names for the same stop. Marta collects stop names from the timetable, the website and the complaints system and finds variations such as High St, High Street and high street with a trailing space. Each system was set up separately, and staff typed names in their own way. She explains that inconsistent names confuse passengers and split reports, because one stop appears as several in counts. Marta counts the variations for each stop in a short table.

### Lab — Normalising synthetic bus stop names

```python
"""Normalise synthetic bus stop names and count distinct stops before and after (stdlib only)."""
import re
raw = ["High St", "High Street", "high street ", "Station Rd", "Station Road", "STATION ROAD",
       "Market Sq", "Market Square", "Park Ave", "Park Avenue", "Church Lane", "Church Ln"]
abbr = {"st": "street", "rd": "road", "sq": "square", "ave": "avenue", "ln": "lane"}
def norm(s):
    w = re.sub(r"\s+", " ", s.strip().lower()).split(" ")
    return " ".join(abbr.get(x, x) for x in w)
print(f"names {len(raw)}; distinct raw {len(set(raw))}; distinct after normalising {len({norm(s) for s in raw})}")
print(sorted({norm(s) for s in raw}))
```

Run with `python3 lab_stops.py`. Verified output:

```text
names 12; distinct raw 12; distinct after normalising 5
['church lane', 'high street', 'market square', 'park avenue', 'station road']
```

### 8.2 Normalising

The lab normalises twelve synthetic stop names. It removes extra spaces, converts to lowercase and expands common abbreviations such as st to street and rd to road. All twelve raw names are distinct as written, but after normalising only five distinct stops remain: church lane, high street, market square, park avenue and station road. Marta notes that simple rules can reveal how many real stops lie behind many different spellings. She runs the script on the full list of stop names from all three systems, and shares the results with Mr. Hughes.

### 8.3 Limits of rules

Marta warns that automatic rules can make mistakes. St can mean street or saint, as in St Mary's Church. She checks the normalised list with Mr. Hughes before using it. He confirms the five stops and adds that one stop near the church should keep the word saint. Marta adds an exception list to her script. She learns that normalising is a helpful first step, but a person who knows the data must check the result. The exception list is kept beside the script.

### 8.4 A standard list

Mr. Hughes becomes owner of an official stop list with a code for each stop, an official name and its location. All systems should use the code and official name. Marta helps update the website and complaints system from the list. Mr. Osei explains that a single owned list prevents names drifting apart again, and that new stops must be added to the list before they appear anywhere else. Marta checks the website a month later and finds that every stop now shows its official name, and passenger complaints about names stop.

### Worked example

Marta finds stop name variations across systems, normalises twelve names to five stops, adds an exception for saint after checking with Mr. Hughes and helps adopt an owned official stop list.

> **Synthetic case.** Names are synthetic; outputs come from lab_stops.py.

### Errors and limits

Automatic normalising without review can merge different things.

### Exercises

- **EX029 — Distinct after.** How many distinct stops remained after normalising? *Rubric:* 3 = five;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX030 — Abbreviation risk.** What can St mean besides street? *Rubric:* 3 = saint;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX031 — List owner.** Who owns the official stop list? *Rubric:* 3 = Mr. Hughes;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX032 — New stop rule.** What must happen before a new stop appears? *Rubric:* 3 = it is added to the official list;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue studying — lesson 08 (chapter 08 of 18)

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Personal data at work

### Learning outcomes

You will (1) recognise personal data; (2) apply basic data protection principles; (3) handle personal data carefully in daily tasks.

### 9.1 What counts

Mr. Osei explains that personal data are any information about an identifiable person. At Linkway this includes driver names, rosters and hours, passenger complaint contact details, lost property owners and smartcard holders. Passenger counts from sensors are not personal data, because they count people without identifying them. Marta lists Linkway's data sets and marks which contain personal data, finding that most staff data and some passenger data do. She shares the marked list with Mr. Hughes, who confirms it and adds smartcard top-up records, which she had missed because they sit in a supplier's system.

### 9.2 Principles

Marta learns the main principles of the GDPR in plain words: use personal data fairly and openly, only for clear purposes, collect only what is needed, keep it accurate, keep it no longer than needed and keep it secure. She writes a Linkway example for each, such as collecting only email or phone on the complaint form, as she did in chapter 3, and deleting complaint details after a set time. Mr. Osei checks her examples, and she keeps them as a quick reference card in her workbook.

### 9.3 Daily care

Marta lists daily habits: lock the screen when leaving the desk, do not leave printouts on printers, send personal data only through approved systems, check the recipient before sending emails and do not discuss passengers or staff in public. Mr. Hughes says most data incidents at bus companies come from simple mistakes, such as emailing a roster to the wrong person. Careful habits prevent many of them. Marta writes the habits on a card for her desk and follows them on her work placement days, where she finds that a printed roster has been left on a shared printer.

### 9.4 When unsure

Marta is asked by a driver to share another driver's phone number to swap a shift. She is unsure whether this is allowed. She asks Mr. Hughes, who explains that Linkway has a shift swap system that passes messages without sharing numbers. Marta directs the driver there. Mr. Osei notes that asking when unsure is the right response, and that technicians should know who to ask before a question arises. Marta adds Mr. Hughes's contact details to her workbook as the person to ask about personal data.

### Worked example

Marta marks which Linkway data sets contain personal data, writes examples for each GDPR principle, lists daily care habits and asks before sharing a driver's phone number.

> **Synthetic case.** Examples are synthetic; the GDPR is real. This is not legal advice.

### Errors and limits

Assuming staff data are less sensitive than customer data leads to careless sharing.

### Exercises

- **EX033 — Counts status.** Are sensor passenger counts personal data? *Rubric:* 3 = no;; 2 = partly correct;; 1 = yes;; 0 = none.
- **EX034 — Common incident.** What causes most incidents at bus companies? *Rubric:* 3 = simple mistakes such as wrong email recipients;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX035 — Shift swap answer.** How should drivers swap shifts? *Rubric:* 3 = through the shift swap system;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX036 — Complaint deletion.** Which principle does deleting old complaint details apply? *Rubric:* 3 = keep data no longer than needed;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue studying — lesson 09 (chapter 09 of 18)

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Keeping data secure

### Learning outcomes

You will (1) use passwords and access controls properly; (2) recognise phishing; (3) protect data on devices.

### 10.1 Accounts and passwords

Marta learns that each person should have their own account, never shared, so that actions can be traced. Passwords should be long and unique, ideally managed with a password manager, and multi-factor authentication should be used where available. At Linkway, depot staff shared one login for the roster system. Mr. Hughes replaces it with individual accounts. Marta notes that shared accounts make it impossible to know who changed a roster. Depot staff receive their accounts within a week, and the old shared login is switched off.

### 10.2 Access by need

Staff should see only data they need. Marta reviews who can open the roster spreadsheet and finds that all office staff can, including people in marketing. Mr. Hughes restricts it to depot managers and payroll. Marta learns that access should be checked regularly, especially when people change jobs, and that the data owner, not the technician, decides who needs access. Mr. Hughes asks Marta to check the roster access list again every quarter, and to report any names that have been added since the previous check, so that he can decide whether each one still needs it.

### 10.3 Phishing

Mr. Osei shows examples of phishing emails pretending to be from IT asking staff to confirm passwords. Marta learns to check the sender address, look for urgent threats and never enter passwords through email links. During the course, Linkway runs a practice phishing email; Marta reports it instead of clicking. Mr. Hughes notes that reporting suspicious emails helps protect everyone, because one click can expose the whole company's data. Marta records the exercise in her workbook as an example of good practice.

### 10.4 Devices

Laptops and phones holding Linkway data must be encrypted and locked with a PIN. Data should not be copied to personal memory sticks. Marta notices a memory stick labelled rosters left in a depot office and hands it to Mr. Hughes, who checks it, finds old rosters and destroys it. Mr. Osei explains that small portable devices are easily lost, and that encrypted, approved storage prevents loss turning into a breach. Linkway reminds all staff that only encrypted company storage may be used for data.

### Worked example

Marta learns individual accounts, strong passwords and MFA, sees roster access restricted to depot managers and payroll, reports a practice phishing email and hands in an unlabelled roster memory stick.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Shared logins make it impossible to trace who changed data.

### Exercises

- **EX037 — Shared login fix.** What replaced the shared roster login? *Rubric:* 3 = individual accounts;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX038 — Roster access.** Who can now open the roster spreadsheet? *Rubric:* 3 = depot managers and payroll;; 2 = both;; 1 = one;; 0 = none.
- **EX039 — Phishing response.** What did Marta do with the practice phishing email? *Rubric:* 3 = reported it;; 2 = partly correct;; 1 = clicked;; 0 = none.
- **EX040 — Memory stick.** What was on the found memory stick? *Rubric:* 3 = old rosters;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue studying — lesson 10 (chapter 10 of 18)

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Sharing and requests

### Learning outcomes

You will (1) share data through approved routes; (2) support requests from individuals; (3) prepare data for partners.

### 11.1 Approved routes

Linkway shares data with the transport authority, a ticketing supplier and a payroll company. Marta learns the approved route for each: a secure upload portal for the authority, an encrypted transfer for the supplier and the payroll system's own connection. Email attachments are not approved for personal data. She notes that approved routes have been checked for security, while improvised routes such as personal email are not. Marta writes the approved route for each partner on a one-page guide, which Mr. Hughes shares with office staff.

### 11.2 Requests from individuals

A driver asks for a copy of his roster and hours data. Mr. Hughes explains that people have a right to access their personal data, and that Linkway must respond within a month. Marta helps by finding the driver's records in the roster system and payroll exports, using his staff number. Mr. Hughes checks the results, removes other drivers' details and sends the response. Marta records the request in the log. The driver receives his data within three weeks and thanks the office.

### 11.3 Preparing data for partners

The authority asks for monthly passenger counts by route. Marta prepares the file from the count system, removing internal notes and checking totals against the monthly report. She follows the authority's template exactly, with route codes from the official list. She explains that preparing partner files carefully avoids rejected submissions and questions that delay funding. Before sending, Marta compares this month's totals with last month's and looks into any route where the change is unusually large, because a sudden jump might mean a data problem rather than real growth in passengers. One route's rise is explained by a school holiday ending.

### 11.4 Sharing aggregates

The local newspaper asks how many people use each stop. Mr. Hughes agrees to share yearly totals by stop. Marta checks whether any total is so small it might identify a regular passenger, such as a rural stop used by one person each day. She removes stops with very low use from the published list. Mr. Osei explains that even counts can reveal individuals when numbers are tiny. Mr. Hughes approves the final list, and the newspaper publishes it with a note that very low-use stops were left out.

### Worked example

Marta learns approved sharing routes, helps answer a driver's access request within a month, prepares the authority's monthly file using official codes and removes very low-use stops from newspaper totals.

> **Synthetic case.** Requests are synthetic.

### Errors and limits

Small published counts can still identify individuals.

### Exercises

- **EX041 — Email attachments.** Are email attachments approved for personal data? *Rubric:* 3 = no;; 2 = partly correct;; 1 = yes;; 0 = none.
- **EX042 — Response deadline.** How long does Linkway have to answer an access request? *Rubric:* 3 = a month;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX043 — Authority template.** What codes does the authority file use? *Rubric:* 3 = route codes from the official list;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX044 — Low-use stops.** What happened to very low-use stops in the newspaper list? *Rubric:* 3 = removed;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue studying — lesson 11 (chapter 11 of 18)

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Keeping and deleting records

### Learning outcomes

You will (1) read a retention schedule; (2) find records past their retention date; (3) delete records safely with approval.

### 12.1 The schedule

Linkway's retention schedule lists how long to keep each type of record. Complaints are kept for two years after closing. Driver hours are kept for the period employment and transport law require. Lost property records are kept for six months. Count data without personal details are kept for ten years for planning. Marta learns that keeping data too long increases risk, while deleting too early can break legal duties. Marta keeps a copy of the schedule in her workbook with notes on which records she handles most often.

### 12.2 Finding old records

Marta writes a script that reads the complaints export and lists complaints closed more than two years ago. She finds many old complaints still held, including contact details of passengers who complained years earlier. She also checks the lost property spreadsheet and finds records from three years ago. She reports both to Mr. Hughes with counts, keeping the details inside the secure system rather than copying them into her report. Mr. Hughes thanks her for keeping the details out of the report itself.

### 12.3 Deleting with approval

Mr. Hughes, as owner, approves deletion. Marta deletes old complaint contact details but keeps the complaint category, route and date, which help planners understand problems. For lost property, she deletes old records completely. She records the date, the number deleted and Mr. Hughes's approval in a deletion log. Mr. Osei notes that recording deletions shows that the schedule is followed, which matters if anyone asks. Mr. Hughes checks the log entry and signs it, and planners confirm that the kept complaint fields still meet their needs.

### 12.4 Making it routine

Marta suggests running the deletion check every month. Mr. Hughes agrees and adds it to the monthly task list, with Marta's script and a short procedure. He also asks IT whether the complaints system can delete old contact details automatically. Marta learns that retention works best when deletion is routine and automatic, rather than a big clean-up done once and then forgotten. IT confirms that automatic deletion is possible, and it is planned for the next system update, with Marta's monthly check continuing until then as a safeguard.

### Worked example

Marta reads Linkway's retention schedule, finds old complaints and lost property records past their dates, deletes them with approval while keeping useful complaint categories and makes the check monthly.

> **Synthetic case.** The schedule is synthetic.

### Errors and limits

Copying personal details into reports about deletion creates new copies to delete.

### Exercises

- **EX045 — Complaint period.** How long are complaints kept after closing? *Rubric:* 3 = two years;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX046 — Kept complaint fields.** What complaint details are kept after deletion? *Rubric:* 3 = category, route and date;; 2 = all;; 1 = some;; 0 = none.
- **EX047 — Lost property.** How long are lost property records kept? *Rubric:* 3 = six months;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX048 — Deletion record.** What is recorded in the deletion log? *Rubric:* 3 = date, number deleted and approval;; 2 = all;; 1 = some;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue studying — lesson 12 (chapter 12 of 18)

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — Reporting problems

### Learning outcomes

You will (1) report data problems clearly; (2) use an issue log; (3) follow problems through to a fix.

### 13.1 What makes a good report

Marta learns that a good problem report says what was seen, where, when, how many records are affected, why it matters and who has been told. Mr. Osei shows two reports about the same problem. One says the counts look wrong. The other says Route 7 has 122 trips without counts in March, about ten percent, which could reduce funding. Marta sees that the second report lets someone act straight away, while the first only causes worry. Marta uses the second style from then on.

### 13.2 The issue log

Linkway starts a simple issue log in a shared spreadsheet, with columns for date, reporter, description, data affected, impact, owner, status and fix. Marta enters the Route 7 counts problem, the stop names problem and the old complaints problem from earlier chapters. Mr. Hughes reviews the log each week and assigns owners. Marta notes that a log stops problems being forgotten when people are busy with other work. Each entry has an owner and a status, and Mr. Hughes moves entries along as they progress, so the log always shows where each problem stands.

### 13.3 Following through

An issue is closed only when the fix is checked. After the Route 7 sensors are repaired, Marta reruns her missing counts check and finds Route 7 now has very few missing trips. She records the result and closes the issue. For stop names, she checks the website and complaints system for old names before closing. Mr. Osei explains that closing issues without checking often means problems come back unnoticed. Both issues stay closed in the following months, which Marta checks by rerunning the same checks once a month and noting the results in the log.

### 13.4 Spotting patterns

After three months, Marta looks at the log and sees that several issues come from equipment on older buses. She mentions this to Mr. Hughes, who raises it with the fleet manager as a wider problem rather than separate faults. The fleet manager plans sensor upgrades for all older buses. Marta learns that a log can reveal patterns that individual reports hide, which helps managers fix bigger causes. Mr. Hughes adds a column to the log for the cause type, so that patterns like this one can be seen more easily in future reviews.

### Worked example

Marta writes specific problem reports, keeps a shared issue log reviewed weekly, closes issues only after checking fixes and spots a pattern of older-bus equipment faults that leads to planned upgrades.

> **Synthetic case.** Issues are synthetic.

### Errors and limits

Vague problem reports cause worry without action.

### Exercises

- **EX049 — Good report contents.** What should a problem report include? *Rubric:* 3 = what, where, when, how many, why it matters, who was told;; 2 = most;; 1 = few;; 0 = none.
- **EX050 — Log reviewer.** Who reviews the issue log each week? *Rubric:* 3 = Mr. Hughes;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX051 — Closing evidence.** How did Marta close the Route 7 issue? *Rubric:* 3 = reran the check and found few missing trips;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX052 — Pattern found.** What pattern did the log show? *Rubric:* 3 = issues from older buses' equipment;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue studying — lesson 13 (chapter 13 of 18)

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — Simple documentation

### Learning outcomes

You will (1) write a data dictionary entry; (2) write a short procedure; (3) keep documents easy to find.

### 14.1 Dictionary entries

Marta writes dictionary entries for the passenger counts file. For each field she records the name, what it means in plain words, the format, allowed values and where it comes from. For boardings she writes: number of passengers getting on during the trip, whole number from zero to one hundred and twenty, recorded by door sensors. She checks each entry with Mr. Hughes. She notes that clear definitions stop people guessing what fields mean when they build reports. He suggests two small corrections.

### 14.2 A short procedure

Marta writes a procedure for the monthly authority file: run the missing counts check, fix or note problems, prepare the file from the template, check totals against the monthly report, get Mr. Hughes's approval and upload through the portal. Each step is numbered and names who does it. She keeps the language plain and adds what to do if the portal is unavailable, which happened once during the course. Mr. Hughes approves the procedure and asks that it be used every month by whoever prepares the file.

### 14.3 Testing documents

Marta asks a classmate to prepare a practice authority file using only her procedure. The classmate gets stuck at the totals check, because the procedure does not say which report to compare with. Marta adds the report name and location. The classmate then finishes without help. Mr. Osei explains that testing documents with someone new shows where steps that seem obvious to the writer are missing. Marta records the change and the reason in the procedure's history section, so that later readers can see how the document improved over time.

### 14.4 Finding documents

Marta stores the dictionary, procedures and scripts in one shared folder with a contents page listing each document, its owner and the date it was last checked. Mr. Hughes asks staff to use the contents page rather than searching through emails. Marta learns that documents only help if people can find them quickly, and that dates show whether a document is still likely to be correct. Marta checks the contents page every quarter during her placement and updates the dates of documents she has reviewed, flagging any she cannot confirm.

### Worked example

Marta writes dictionary entries checked with Mr. Hughes, a numbered authority file procedure with a portal fallback, tests it with a classmate who finds a missing report name and stores documents with a dated contents page.

> **Synthetic case.** Documents are synthetic.

### Errors and limits

Procedures tested only by their writers miss obvious-seeming steps.

### Exercises

- **EX053 — Boardings definition.** How is boardings defined? *Rubric:* 3 = passengers getting on, whole number 0–120 from door sensors;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX054 — Procedure gap.** Where did the classmate get stuck? *Rubric:* 3 = the totals check;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX055 — Contents page.** What does the contents page list? *Rubric:* 3 = each document, owner and last checked date;; 2 = all;; 1 = some;; 0 = none.
- **EX056 — Portal fallback.** What extra case did the procedure cover? *Rubric:* 3 = the portal being unavailable;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue studying — lesson 14 (chapter 14 of 18)

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — Working with a steward

### Learning outcomes

You will (1) understand the steward role; (2) support a steward with regular tasks; (3) escalate decisions correctly.

### 15.1 The steward's role

Linkway appoints a data steward for passenger data, a planner named Ms. Price, while Mr. Hughes remains the data officer overseeing all data. Mr. Osei explains that stewards look after the meaning, quality and rules of a data area day to day, and decide many practical questions. Technicians like Marta support stewards by running checks, preparing information and making approved changes. Marta notes that knowing who the steward is tells her where to take questions about passenger data. Ms. Price welcomes her support.

### 15.2 Regular support

Marta prepares a weekly summary for Ms. Price: missing counts by route, invalid values, upload delays and open issues. Ms. Price reviews it and decides what to follow up. When she asks for a new check on counts much higher than usual, Marta writes it and adds it to the summary. Marta learns that regular, short summaries help stewards stay on top of quality without spending long hours on data themselves. The summary takes Marta about an hour to prepare each week, and Ms. Price reads it in a few minutes before her Monday meeting.

### 15.3 Escalating decisions

A planner asks Marta to change last month's counts on Route 4 because a school trip used a regular bus and inflated numbers. Marta knows this would change figures reported to the authority. She tells the planner that Ms. Price must decide, and passes on the request with details. Ms. Price decides to keep the counts but add a note explaining the school trip, which the authority accepts. Marta records the request and the decision in the issue log, and the planner thanks her for passing it to the right person rather than making the change.

### 15.4 Keeping records

Marta records each decision Ms. Price makes in the issue log or a decision list, with the date and reason. When the authority later asks about the Route 4 note, Mr. Hughes finds the decision quickly. Mr. Osei notes that recorded decisions protect everyone: the steward can show her reasoning, the technician can show she followed instructions and the company can explain its figures. Marta keeps the decision list next to the issue log, and Ms. Price reviews it each month to make sure the reasons are clear enough for someone reading them a year later.

### Worked example

Marta supports steward Ms. Price with weekly summaries and a new high-count check, passes a request to change Route 4 counts to her, records the decision to add a note and sees the record answer a later authority question.

> **Synthetic case.** Roles are synthetic.

### Errors and limits

Technicians changing reported figures without the steward bypass accountability.

### Exercises

- **EX057 — Steward name.** Who is the passenger data steward? *Rubric:* 3 = Ms. Price;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX058 — New check.** What new check did Ms. Price request? *Rubric:* 3 = counts much higher than usual;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX059 — Route 4 decision.** What did Ms. Price decide about Route 4? *Rubric:* 3 = keep counts and add an explanatory note;; 2 = partly correct;; 1 = change;; 0 = none.
- **EX060 — Decision record use.** How did the decision record help later? *Rubric:* 3 = Mr. Hughes found it quickly when the authority asked;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue studying — lesson 15 (chapter 15 of 18)

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — Workplace practice

### Learning outcomes

You will (1) apply course skills in a workplace; (2) handle real work pressures; (3) reflect on professional behaviour.

### 16.1 The placement

Marta spends six weeks on placement in Linkway's office. All examples here remain synthetic. She runs the weekly checks, prepares the authority file, updates the stop list and helps answer data requests. She finds that work arrives unpredictably, with urgent requests interrupting planned tasks. She learns to keep a short task list each day, agreeing priorities with Mr. Hughes when two urgent requests arrive at once. Mr. Hughes notes in her placement report that she handled interruptions calmly and kept him informed about which tasks were waiting and why.

### 16.2 Pressure and shortcuts

On the day the authority file is due, the totals check fails by a small amount. A colleague suggests adjusting a figure to make it match and sending the file on time. Marta refuses, finds that one late upload from the previous night was missing, waits for it to arrive and sends the file an hour late with a note. Mr. Hughes supports her. She learns that small shortcuts under pressure can create bigger problems later. The authority accepts the explanation without question.

### 16.3 Communication

Marta explains her checks to drivers and depot staff, who sometimes see data work as criticism. When she reports that a bus's sensor is failing, she explains that it is not the driver's fault and that fixing it protects funding for their route. Drivers become more willing to mention equipment problems. She learns that explaining why data matter helps people cooperate rather than feel blamed. Two drivers later report sensor faults on their own buses before Marta's checks find them, which helps maintenance fix problems faster and keeps counts complete.

### 16.4 Reflection

Marta writes a placement reflection in her workbook. She notes that the most useful skills were careful checking, clear reporting and knowing when to ask. She was surprised how much of her work involved talking to people. She lists two things she would improve: estimating how long tasks take and writing shorter emails. Mr. Osei and Mr. Hughes add comments, which she will use to prepare for her practical assessment. She plans small exercises for each improvement, such as timing her tasks for a week.

### Worked example

Marta runs checks and requests on placement, refuses to adjust a figure under deadline pressure and finds a late upload instead, explains sensor faults to drivers without blame and reflects on her skills.

> **Synthetic case.** The placement is synthetic.

### Errors and limits

Adjusting figures to pass checks hides real problems.

### Exercises

- **EX061 — Placement length.** How long is the placement? *Rubric:* 3 = six weeks;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX062 — Totals failure cause.** Why did the totals check fail? *Rubric:* 3 = a late upload was missing;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX063 — Driver approach.** How did Marta explain sensor faults to drivers? *Rubric:* 3 = not their fault and fixing protects route funding;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX064 — Improvement areas.** What two things will Marta improve? *Rubric:* 3 = estimating task time and shorter emails;; 2 = both;; 1 = one;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue studying — lesson 16 (chapter 16 of 18)

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — Practical assessment

### Learning outcomes

You will (1) complete a practical data task under assessment; (2) document your work; (3) explain your choices to an assessor.

### 17.1 The task

For her practical assessment, Marta receives a synthetic month of Linkway data with hidden problems. She must check the data, find and report problems, prepare the authority file, update the issue log and explain her work to an assessor. She has one working day. She plans her time: an hour reading the data and documents, three hours on checks, two hours on the file and log and an hour preparing her explanation. She writes the plan at the top of her working notes so that the assessor can see how she used her time.

### 17.2 Doing the checks

Marta runs her scripts for validity and missing counts, compares counts with ticket sales and checks stop names against the official list. She finds four problems: a route with many missing counts, a bus with impossible values, two stops with old names and a day where uploads were late. She records each in the issue log with counts, likely causes and who should be told, following the format she practised. She also notes which problems would affect funding, so that the most important ones can be handled first.

### 17.3 Preparing the file

Marta prepares the authority file, leaving out trips with impossible values and noting them in the covering note rather than guessing replacements. She checks totals against the monthly report, adjusting for the excluded trips, and lists the route with missing counts so the authority understands the gap. She saves her work with clear names in a dated folder. She notes that being open about gaps is better than hiding them. The assessor later notes that her file and covering note would be ready to send to the authority.

### 17.4 Explaining to the assessor

The assessor asks why Marta did not fill in missing counts with averages. She explains that guessing would make the file look complete but could be wrong, and that the steward and authority should decide how to treat gaps. The assessor also asks how she would stop the stop name problem recurring. She explains the official list and the rule that new stops are added there first. The assessor marks her work as competent with merit. Marta records the assessor's comments in her workbook.

### Worked example

Marta plans a one-day assessment, finds four hidden problems with her checks and logs them, prepares the authority file with exclusions noted openly and explains why she did not guess missing values.

> **Synthetic case.** The assessment is synthetic.

### Errors and limits

Filling gaps with guesses makes files look complete but less trustworthy.

### Exercises

- **EX065 — Problems found.** How many problems did Marta find? *Rubric:* 3 = four;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX066 — Impossible values.** How did Marta treat trips with impossible values? *Rubric:* 3 = left them out and noted them;; 2 = partly correct;; 1 = guessed;; 0 = none.
- **EX067 — Averages answer.** Why not fill missing counts with averages? *Rubric:* 3 = guesses could be wrong; steward and authority should decide;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX068 — Assessment result.** What result did Marta receive? *Rubric:* 3 = competent with merit;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue studying — lesson 17 (chapter 17 of 18)

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — Review and next steps

### Learning outcomes

You will (1) review skills gained in the course; (2) plan further learning; (3) understand how data governance continues at work.

### 18.1 Skills gained

Marta reviews her workbook. She can design forms, organise spreadsheets, write Python checks, apply quality dimensions, normalise names, handle personal data carefully, follow retention rules, report and log problems, write documentation and support a steward. She notes that each skill connects to a governance idea: rules, responsibility, quality and protection. She feels confident handling data tasks at work and knowing when to ask for decisions. She lists each skill with the chapter where she practised it and an example from her placement, which she plans to use when describing her experience to future employers.

### 18.2 Feedback

Mr. Osei and Mr. Hughes give final feedback. They praise her careful checks and her refusal to adjust figures under pressure. They suggest she continue learning Python and consider the technologist course later. Mr. Hughes offers her a job as a data technician at Linkway. Marta accepts, pleased that her placement work on counts and stop names will continue in her new role. Marta records the feedback in her workbook and thanks both of them for their support during the course, especially during the busy weeks of her placement at Linkway.

### 18.3 Governance at work

Mr. Osei explains that governance does not end with the course. At Linkway, Marta will run checks, keep logs and documents current and support stewards as the company changes, such as when new buses or routes arrive. She should keep asking who owns each decision, whether data are good enough for their use and whether personal data are handled properly. These questions remain useful in any data job. Marta writes these questions on the last page of her workbook, where she can find them quickly when she meets new data tasks.

### 18.4 Next steps

Marta plans to keep her workbook going at Linkway and to join a professional community for data technicians. She also plans to learn more about privacy, since much of her work touches personal data. The next course in this area turns to privacy and data protection, where governed data meet the rights of the people they describe. Mr. Osei wishes her well and reminds her that careful, honest work is what makes data trustworthy. Marta thanks Mr. Osei for his teaching and starts at Linkway the following month.

### Worked example

Marta reviews her skills from forms to stewardship, receives praise and a job offer at Linkway, learns that governance continues through daily questions at work and plans further learning in privacy.

> **Synthetic case.** The review is synthetic.

### Errors and limits

Treating course completion as the end of learning leaves skills to fade.

### Exercises

- **EX069 — Job offer.** What job does Mr. Hughes offer? *Rubric:* 3 = data technician at Linkway;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX070 — Praised behaviour.** What behaviour was praised? *Rubric:* 3 = careful checks and refusing to adjust figures;; 2 = both;; 1 = one;; 0 = none.
- **EX071 — Ongoing questions.** Name one question Marta should keep asking. *Rubric:* 3 = who owns each decision;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX072 — Further study.** Which course might Marta take later? *Rubric:* 3 = the technologist course;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue studying — lesson 18 (chapter 18 of 18)

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Marta Kowalski, Mr. Daniel Osei, Southport Technical College, Linkway Buses and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Sixty buses.

**EX002.** Apply rules, check data and report problems.

**EX003.** It provides evidence of work for employers and the final assessment.

**EX004.** The transport authority part-funds routes using them.

**EX005.** Timetables, through the scheduled trip.

**EX006.** At night over the depot wireless network.

**EX007.** Planners might cut a busy trip or funding might fall.

**EX008.** Faulty sensors and failed uploads.

**EX009.** The hospital bus.

**EX010.** The full address and date of birth.

**EX011.** Some stops share names on different routes.

**EX012.** It was hard to use on a phone.

**EX013.** Three.

**EX014.** In a separate column with a reason.

**EX015.** The timetable for the month.

**EX016.** Sending the authority exactly the approved version.

**EX017.** One hundred and twenty, the bus capacity.

**EX018.** A sensor fault on one bus.

**EX019.** The bus number.

**EX020.** In a shared folder with a short readme.

**EX021.** By a person counting passengers on a sample of trips.

**EX022.** Ticket sales on the same trips.

**EX023.** Completeness and accuracy.

**EX024.** Timeliness.

**EX025.** 10.2 percent.

**EX026.** 144 of 3,600, 4.0 percent.

**EX027.** Failing sensors on two older buses.

**EX028.** Newer buses were moved onto Route 7.

**EX029.** Five.

**EX030.** Saint.

**EX031.** Mr. Hughes, the data officer.

**EX032.** It must be added to the official list first.

**EX033.** No, they do not identify people.

**EX034.** Simple mistakes like emailing a roster to the wrong person.

**EX035.** Through the shift swap system, which does not share numbers.

**EX036.** Keeping data no longer than needed.

**EX037.** Individual accounts.

**EX038.** Depot managers and payroll.

**EX039.** She reported it.

**EX040.** Old rosters.

**EX041.** No.

**EX042.** Within a month.

**EX043.** Route codes from the official list.

**EX044.** They were removed from the published list.

**EX045.** Two years.

**EX046.** The category, route and date.

**EX047.** Six months.

**EX048.** The date, number deleted and owner's approval.

**EX049.** What was seen, where, when, how many, why it matters and who was told.

**EX050.** Mr. Hughes.

**EX051.** She reran the check and confirmed few missing trips.

**EX052.** Several issues came from equipment on older buses.

**EX053.** Passengers getting on, a whole number from zero to 120 from door sensors.

**EX054.** At the totals check.

**EX055.** Each document, its owner and its last checked date.

**EX056.** What to do if the portal is unavailable.

**EX057.** Ms. Price, a planner.

**EX058.** A check for counts much higher than usual.

**EX059.** Keep the counts and add a note about the school trip.

**EX060.** It let Mr. Hughes answer the authority's question quickly.

**EX061.** Six weeks.

**EX062.** A late upload from the previous night was missing.

**EX063.** That faults were not their fault and fixing them protects funding.

**EX064.** Estimating how long tasks take and writing shorter emails.

**EX065.** Four.

**EX066.** She left them out and noted them in the covering note.

**EX067.** Guesses could be wrong, and the steward and authority should decide.

**EX068.** Competent with merit.

**EX069.** Data technician at Linkway.

**EX070.** Careful checks and refusing to adjust figures under pressure.

**EX071.** Who owns each decision.

**EX072.** The technologist course.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and standards were checked against their publisher pages. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
