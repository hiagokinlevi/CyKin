# Security Governance, Risk and Compliance: Engineering Course

- Language: English (`en`); course 120, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; eight offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students designing, verifying and operating a security governance, risk and compliance programme as an engineered system.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs compute expected loss, register validation, residual risk, control pass rates, layered failure, attribute-sampling bounds, budget optimisation and evidence digests on synthetic data. Risk figures are illustrations, standards are cited by edition and paraphrased, and nothing here is a real audit, attestation or legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one engineering student through a five-year course centred on an electricity cooperative's GRC programme: foundations, risk quantities and data, requirements and models, control design and implementation, measurement, verification and validation, operations and optimisation, the capstone, the evidence dossier, the thesis and the defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Nadia Okafor** | Engineering student | Invented |
| **Prof. Tomas Brenner** | Supervisor | Invented |
| **Kestrel Polytechnic** | Fictional university | Invented |
| **Ardwell Power Cooperative** | Fictional electricity distributor, 900 staff | Invented |

### Core sources

ISO 31000:2018; ISO/IEC 27001:2022, 27002:2022 and 27005:2022; NIST [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1), [SP 800-37 Rev. 2](https://doi.org/10.6028/NIST.SP.800-37r2), [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); COBIT 2019; PCI DSS v4.0; Cox (2008), [doi:10.1111/j.1539-6924.2008.01030.x](https://doi.org/10.1111/j.1539-6924.2008.01030.x); Gordon and Loeb (2002), [doi:10.1145/581271.581274](https://doi.org/10.1145/581271.581274). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) describe risk that changes over time with rates; (2) read when exposure is growing or shrinking; (3) use accumulation to total exposure across a period.

### 1.1 Rates in governance

Nadia Okafor is an engineering student at the fictional Kestrel Polytechnic. Her supervisor, Prof. Tomas Brenner, links every foundation course to one running case: the fictional Ardwell Power Cooperative, an electricity distributor with nine hundred staff, a customer payment portal and remote access for the vendors who maintain its control systems. In calculus Nadia learns that a derivative measures how fast something changes. At Ardwell, the number of open audit findings changes each month. Its rate of change shows whether the backlog is shrinking, holding steady or growing, which the board needs more than a single monthly count.

### 1.2 Reading the curve

Nadia plots open findings after the last external audit. The count jumps when the report arrives and then declines as teams close items, quickly at first and then slowly, because the hardest findings remain. The derivative is steeply negative early and flattens later. Where the curve flattens, management attention usually fades, and old findings linger. Nadia learns that a straight-line forecast would wrongly promise that every finding closes by a fixed date. Choosing a realistic shape for how organisations actually respond is the first modelling decision in governance analysis.

### 1.3 Accumulating exposure

Integration adds a rate over time. Nadia uses it to define exposure from a known weakness: each day an unpatched internet-facing server remains open adds to the window in which an attacker could use it. The area under the curve of open weaknesses over time is the accumulated exposure. Closing findings faster shrinks that area even if the final count is the same. This gives Ardwell a better governance measure than the number of findings closed, because it rewards speed on the weaknesses that matter.

### Worked example

Nadia describes the audit-finding backlog as a curve, reads its rate of change and defines accumulated exposure as an area.

> **Synthetic case.** Kestrel, Ardwell and all figures are synthetic.

### Errors and limits

Smooth curves hide lumpy monthly data. Exposure areas ignore how severe each weakness is.

### Exercises

- **EX001 — Backlog trend.** What does the rate of change of open findings tell the board? *Rubric:* 3 = whether the backlog is shrinking, steady or growing;; 2 = trend;; 1 = none;; 0 = none.
- **EX002 — Flattening meaning.** Why does the flattening of the curve matter? *Rubric:* 3 = attention fades and hard findings linger;; 2 = lingering;; 1 = none;; 0 = none.
- **EX003 — Exposure integral.** How does Nadia define accumulated exposure? *Rubric:* 3 = area under open weaknesses over time;; 2 = area;; 1 = count;; 0 = none.

### Synthesis

Rates and accumulation describe how governance backlogs and exposure change over time.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) write policy rules in logic; (2) find conflicts between rules; (3) use sets to compare who holds access with who should.

### 2.1 Policies as logic

Nadia translates two Ardwell policies into logic. One says every remote session to the control system must use multi-factor authentication. Another says vendors may connect during emergencies without delay. Written as statements, the two clash when a vendor's token fails during an outage. Precise logic exposes the conflict before an engineer must decide under pressure which rule to break. Nadia proposes an explicit emergency rule with a pre-approved fallback and after-the-fact review, so the exception becomes part of the policy instead of an undocumented workaround.

### 2.2 Sets of access

Using sets, Nadia compares people with control system access against people whose role requires it. The set difference reveals seven accounts belonging to staff who moved to other jobs. The intersection of vendors and accounts without multi-factor authentication shows two vendor accounts at risk. Sets turn vague concerns into exact lists that owners can act on. They also make it easy to test whether a proposed change widens or narrows access, which is the basic question in every access governance decision Ardwell makes.

### 2.3 Counting combinations

Nadia counts segregation of duties conflicts in Ardwell's finance system. Five sensitive permissions exist, and policy forbids any person from holding both create supplier and approve payment, or both approve payment and reconcile bank. She counts pairs of permissions and lists which are forbidden, then checks staff permission sets against the list. Counting makes the rule testable by a simple script. It also shows how quickly checks grow as permissions are added, a reason to keep role design simple and to automate conflict detection.

### Worked example

Nadia exposes a policy conflict in logic, finds seven stale accounts by set difference and counts forbidden permission pairs.

> **Synthetic case.** Policies, accounts and counts are synthetic.

### Errors and limits

Logic captures written rules, not actual practice. Set lists go stale quickly.

### Exercises

- **EX004 — Emergency clash.** Which two policies clash during an outage? *Rubric:* 3 = mandatory MFA and immediate vendor emergency access;; 2 = conflict;; 1 = none;; 0 = none.
- **EX005 — Stale accounts.** How many stale control-system accounts did the set difference reveal? *Rubric:* 3 = seven;; 2 = 7;; 1 = none;; 0 = none.
- **EX006 — Forbidden pairs.** Name one forbidden permission pair. *Rubric:* 3 = create supplier with approve payment;; 2 = SoD pair;; 1 = none;; 0 = none.

### Synthesis

Logic, sets and counting turn governance rules into precise, testable statements.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical infrastructure to governance scope; (2) reason about energy, heat and failure in data rooms; (3) include physical controls in risk analysis.

### 3.1 Physical scope

Ardwell's information systems run in physical places: a data room at headquarters, substations with control equipment and a backup site. Nadia learns that governance scope must include these places, because ISO/IEC 27002:2022 groups physical controls such as secure areas, equipment protection and supporting utilities alongside organisational and technological ones. Physics helps her reason about why. Electrical power, heat and vibration all affect whether equipment works, and a security programme that ignores them leaves availability risks unmanaged. Nadia adds each site to the scope statement with a named owner.

### 3.2 Heat and power

Every watt drawn by servers becomes heat that cooling must remove. Nadia calculates that if cooling fails in the data room, temperature rises steadily until equipment shuts itself down. The time to shutdown depends on the room's heat load and thermal mass. She shows that Ardwell's monitoring should alert well before that time, and that a risk register entry for cooling failure needs an owner in facilities, not only in IT. Physics thus links an engineering calculation to a governance decision about ownership and response.

### 3.3 Substations

At substations, equipment sits in harsh environments with limited physical security. Nadia notes that a locked cabinet resists casual tampering but not a determined attacker with tools. Physical controls therefore need detection, such as door sensors, as well as delay. She records substation access as a separate risk because it combines physical and digital paths into the control system. Her lecturer stresses that physical risk is easy to miss in desk-based assessments, so site visits remain part of good governance practice.

### Worked example

Nadia includes data rooms and substations in scope, links cooling physics to a risk owner and pairs physical delay with detection.

> **Synthetic case.** Ardwell's sites are synthetic; ISO/IEC 27002:2022 is real.

### Errors and limits

Simple heat models ignore airflow. Physical controls degrade without inspection.

### Exercises

- **EX007 — Control groups.** Which control group in ISO/IEC 27002:2022 covers secure areas? *Rubric:* 3 = physical controls;; 2 = physical;; 1 = none;; 0 = none.
- **EX008 — Cooling owner.** Who should own the cooling-failure risk entry? *Rubric:* 3 = facilities, not only IT;; 2 = facilities;; 1 = none;; 0 = none.
- **EX009 — Delay and detection.** Why do substations need door sensors as well as locks? *Rubric:* 3 = locks delay but do not detect a determined attacker;; 2 = detection;; 1 = none;; 0 = none.

### Synthesis

Physical infrastructure is part of governance scope and its risks need owners and controls.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) represent governance records in code; (2) write simple checks over them; (3) keep scripts readable for auditors.

### 4.1 Records as data

Nadia's first program reads Ardwell's list of policies as structured records: title, owner, approval date and next review date. Representing policies as data rather than prose lets a program check them. She stores the list as a CSV file and reads it with Python's standard library. Her lecturer insists on clear field names and one record per line, because governance data will be read by people who are not programmers, including internal auditors who need to understand what the script checks and why.

### 4.2 Simple checks

Nadia writes functions that flag policies with no owner and policies past their review date. She tests each function on a small hand-made list where she knows the right answer, including edge cases like a review due today. When a check fails, it prints the policy title and the reason, not just a count. She learns that the value of a governance script lies in actionable output: an owner can fix a specific policy, but cannot do anything with an unexplained number.

### 4.3 Readable code

Prof. Brenner reviews Nadia's code with an auditor's eye. Each function has a short docstring explaining the rule it enforces and where the rule comes from, such as Ardwell's policy on policies. Constants like the review interval are named, not buried as numbers. He explains that when scripts produce compliance evidence, the script itself becomes part of the evidence, so it must be understandable and version controlled. Nadia commits her code to a repository with a short history of each change.

### Worked example

Nadia reads policies from CSV, flags missing owners and overdue reviews with reasons and documents rules for auditors.

> **Synthetic case.** Policy records are synthetic.

### Errors and limits

Scripts check only what is recorded. Wrong data produce confident wrong output.

### Exercises

- **EX010 — Policy fields.** Which fields does each policy record hold? *Rubric:* 3 = title, owner, approval date, next review date;; 2 = four fields;; 1 = none;; 0 = none.
- **EX011 — Actionable output.** Why print the policy title and reason, not just a count? *Rubric:* 3 = owners can act on specific items;; 2 = actionable;; 1 = none;; 0 = none.
- **EX012 — Script as evidence.** Why must compliance scripts be readable and versioned? *Rubric:* 3 = the script becomes part of the evidence;; 2 = evidence;; 1 = none;; 0 = none.

### Synthesis

Simple, readable scripts make governance records checkable and their output actionable.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write for boards, auditors and engineers; (2) present risk with uncertainty; (3) structure a short governance memo.

### 5.1 Three audiences

Nadia learns that governance messages reach three audiences with different needs. Boards need decisions, options and consequences in plain language. Auditors need precise statements linked to evidence. Engineers need specific actions and deadlines. A single document rarely serves all three, so she practises writing a one-page board summary, an evidence table for auditors and a task list for engineers from the same analysis. Each version is accurate, but each emphasises different details for its readers. She checks that the three versions never contradict one another.

### 5.2 Stating uncertainty

Her first board summary says that ransomware will cost Ardwell ninety thousand a year. Prof. Brenner asks how she knows. She revises it to say that, under stated assumptions, expected annual loss is about ninety thousand, with a wide range because the frequency estimate is uncertain. He explains that boards make better decisions when they see uncertainty honestly, and that false precision erodes trust when reality differs. Hubbard and Seiersen (2016) make this argument at length for cybersecurity risk. She keeps the range in every later version.

### 5.3 Memo structure

Nadia adopts a memo structure for governance decisions: the decision needed, the recommendation, the options considered, the risk and cost of each, the assumptions and the evidence. She keeps it to two pages, moving detail to appendices. She also adds a line stating who was consulted, because governance decisions affect many teams. Her lecturer notes that clear memos create a record of why a decision was made, which later supports audits and helps successors understand past choices. She files each memo with its evidence.

### Worked example

Nadia writes one analysis for three audiences, states uncertainty around expected loss and uses a decision memo structure.

> **Synthetic case.** Figures are synthetic; Hubbard and Seiersen (2016) is real.

### Errors and limits

Plain language can lose nuance. Long appendices go unread.

### Exercises

- **EX013 — Board needs.** What do boards need from governance messages? *Rubric:* 3 = decisions, options and consequences in plain language;; 2 = decisions;; 1 = none;; 0 = none.
- **EX014 — Revised claim.** How did Nadia revise her ransomware statement? *Rubric:* 3 = expected loss under stated assumptions with a wide range;; 2 = uncertainty;; 1 = certainty;; 0 = none.
- **EX015 — Consulted line.** Why add who was consulted to a memo? *Rubric:* 3 = governance decisions affect many teams;; 2 = record;; 1 = none;; 0 = none.

### Synthesis

Clear, audience-specific writing with honest uncertainty makes governance decisions sound and traceable.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use exponential models for growth and decay; (2) model how control effectiveness decays without maintenance; (3) compare discounting of future losses.

### 6.1 Exponential decay

In Calculus II, Nadia studies exponential functions. She models how the share of accounts with correct access decays after a review: each month some staff change roles without their access being updated, so correctness falls by a roughly constant fraction. The model predicts that correctness halves over a fixed period if nothing is done. Periodic reviews reset the curve. This gives a mathematical reason why review frequency matters and links calculus to a question Ardwell's auditors already raise. Nadia plots both curves to compare them.

### 6.2 Choosing intervals

Using the decay model, Nadia asks how often reviews must happen to keep correctness above a target. If correctness falls by a few percent a month, a quarterly review keeps it above the target, while an annual review lets it fall far below by year end. She notes that the decay rate depends on staff movement, so departments with high turnover need more frequent review. The model supports risk-based scheduling rather than one interval for everyone, which ISO/IEC 27002:2022 permits. She shares this result.

### 6.3 Discounting losses

Nadia also learns to discount future amounts. A control that prevents losses in future years is worth less in today's terms than the same loss avoided now, because money has a time value. She applies a simple discount factor to a three-year investment in backups. The adjustment is modest but changes which of two options looks better. She notes that discounting is standard in investment appraisal and that security investments should be compared on the same basis as others. She states the rate used.

### Worked example

Nadia models access correctness as exponential decay, derives risk-based review intervals and discounts future avoided losses.

> **Synthetic case.** Decay rates and investment figures are synthetic.

### Errors and limits

Real decay is uneven. Discount rates are policy choices.

### Exercises

- **EX016 — Decay driver.** What makes access correctness decay after a review? *Rubric:* 3 = staff changing roles without access updates;; 2 = role changes;; 1 = none;; 0 = none.
- **EX017 — High turnover.** Which departments need more frequent review? *Rubric:* 3 = those with high staff turnover;; 2 = turnover;; 1 = none;; 0 = none.
- **EX018 — Time value.** Why is a future avoided loss worth less today? *Rubric:* 3 = money has a time value;; 2 = discounting;; 1 = none;; 0 = none.

### Synthesis

Exponential models explain why controls decay and how review intervals and investments should be set.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) compute expected annual loss from frequency and impact; (2) rank risks by expected loss; (3) recognise the limits of single-number estimates.

### 7.1 Frequency and impact

Nadia learns the classic annualised loss expectancy: the annual rate of occurrence times the single loss expectancy. For Ardwell she estimates five risks with workshop input: a billing outage expected every two years costing one hundred and twenty thousand; ransomware once a decade at nine hundred thousand; four lost laptops a year at six thousand each; a card breach once in twenty years at one and a half million; and misuse of vendor control-system access once in five years at four hundred thousand.

### 7.2 Ranking the risks

The lab multiplies each pair and sorts the results. Ransomware ranks first at ninety thousand a year, followed by vendor access misuse at eighty thousand, card breach at seventy-five thousand, billing outage at sixty thousand and lost laptops at twenty-four thousand. The total is three hundred and twenty-nine thousand. Nadia notices that the top four are close, so small changes in estimates could reorder them. She concludes that the ranking supports attention to all four rather than a single top priority.

### Lab — Expected annual loss for five Ardwell risks

```python
"""Annualised loss expectancy (ALE = ARO x SLE) for synthetic Ardwell risks."""
risks = [("billing outage", 0.5, 120_000), ("ransomware", 0.1, 900_000),
         ("lost laptop", 4.0, 6_000), ("payment card breach", 0.05, 1_500_000),
         ("SCADA vendor access misuse", 0.2, 400_000)]
tot = 0
for name, aro, sle in sorted(risks, key=lambda r: -r[1]*r[2]):
    ale = aro*sle; tot += ale
    print(f"{name}: ARO {aro} x SLE {sle:,} = ALE {ale:,.0f}")
print(f"total ALE {tot:,.0f}")
```

Run with `python3 lab_ale.py`. Verified output:

```text
ransomware: ARO 0.1 x SLE 900,000 = ALE 90,000
SCADA vendor access misuse: ARO 0.2 x SLE 400,000 = ALE 80,000
payment card breach: ARO 0.05 x SLE 1,500,000 = ALE 75,000
billing outage: ARO 0.5 x SLE 120,000 = ALE 60,000
lost laptop: ARO 4.0 x SLE 6,000 = ALE 24,000
total ALE 329,000
```

### 7.3 Limits of averages

Prof. Brenner warns that expected loss hides the shape of outcomes. The card breach has a low expected value but a catastrophic single outcome that could threaten the cooperative, while lost laptops are frequent but small. A board that only sees averages might underweight rare severe events. Nadia learns to report ranges and worst plausible cases next to averages, and she reads how Freund and Jones (2015) decompose frequency and magnitude in the FAIR model to make such estimates more structured and defensible.

### Worked example

Nadia computes ALE for five risks, ranks ransomware first at ninety thousand, totals three hundred and twenty-nine thousand and notes close rankings.

> **Synthetic case.** All estimates are synthetic; Freund and Jones (2015) is real.

### Errors and limits

Single estimates hide uncertainty. Averages underweight rare catastrophes.

### Exercises

- **EX019 — ALE formula.** How is annualised loss expectancy computed? *Rubric:* 3 = rate of occurrence times single loss expectancy;; 2 = ARO x SLE;; 1 = none;; 0 = none.
- **EX020 — Top two.** Which two risks ranked highest by ALE in the lab? *Rubric:* 3 = ransomware 90k and vendor misuse 80k;; 2 = ransomware first;; 1 = laptops;; 0 = none.
- **EX021 — Hidden shape.** Why might the card breach deserve more attention than its ALE suggests? *Rubric:* 3 = rare but catastrophic single outcome;; 2 = tail;; 1 = none;; 0 = none.

### Synthesis

Expected loss gives a useful first ranking, but ranges and tails must accompany it.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) map system components to governance assets; (2) understand where controls act in hardware and firmware; (3) include supply chain in risk scope.

### 8.1 Assets from architecture

Nadia studies how computers are built from processors, memory, storage and input-output devices, all controlled by firmware and operating systems. For governance, she learns to treat these layers as assets with owners. An asset inventory, required by ISO/IEC 27001:2022 through its Annex A controls, must list not only servers and laptops but also the control-system devices at substations. Without knowing what exists, Ardwell cannot assess risk or demonstrate that controls apply to everything in scope. She lists each layer with its owner and records which team updates the record when equipment changes.

### 8.2 Firmware and trust

Firmware runs before the operating system and is rarely updated. Nadia learns that if firmware is compromised, operating system controls can be bypassed. She adds firmware version tracking to Ardwell's asset records and proposes that procurement require vendors to provide signed updates. Prof. Brenner notes that governance often stops at the operating system because firmware is invisible, yet NIST SP 800-53 Rev. 5 includes controls on system and firmware integrity, which give a basis for asking vendors the right questions. She drafts the clause.

### 8.3 Supply chain

Every hardware component arrives through a supply chain. Nadia lists Ardwell's suppliers for control-system devices and notes which provide security updates and for how long. Two older devices are past their vendor's support period, so new vulnerabilities will not be fixed. She records this as a risk with options: replace, isolate or accept with compensating monitoring. She learns that supply chain risk management is part of the Govern function in NIST CSF 2.0, linking architecture knowledge to board-level oversight. She adds it to the register.

### Worked example

Nadia adds control-system devices and firmware to the inventory, requires signed updates and records unsupported devices as a risk.

> **Synthetic case.** Devices and suppliers are synthetic; standards cited are real.

### Errors and limits

Inventories go stale. Vendor support dates change.

### Exercises

- **EX022 — Inventory scope.** What must Ardwell's asset inventory include beyond servers and laptops? *Rubric:* 3 = control-system devices at substations;; 2 = OT devices;; 1 = none;; 0 = none.
- **EX023 — Firmware risk.** Why does compromised firmware matter? *Rubric:* 3 = it can bypass operating system controls;; 2 = bypass;; 1 = none;; 0 = none.
- **EX024 — Unsupported options.** Which options exist for the two unsupported devices? *Rubric:* 3 = replace, isolate or accept with monitoring;; 2 = three options;; 1 = none;; 0 = none.

### Synthesis

Architecture knowledge extends governance to firmware, devices and the supply chain.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure governance tools as tested modules; (2) handle bad input safely; (3) produce repeatable reports from code.

### 9.1 Modules and tests

In Programming II, Nadia restructures her policy checker into modules: one reads data, one applies rules and one writes reports. Each module has unit tests built with the standard library's test framework. She writes a test for every rule, including tricky cases such as a policy with two owners or a review date written in the wrong format. Separating reading from checking lets her reuse the same rules on other registers later, such as the list of suppliers, which also need owners and review dates at Ardwell.

### 9.2 Handling bad input

Real governance data are messy. Dates arrive in several formats, owners are written as names in some rows and as email addresses in others, and some rows are blank. Nadia learns to validate input explicitly and to report problems rather than silently skipping rows. A skipped row could hide a risk that nobody owns. Her program now lists every row it could not read, with the line number and reason, so data owners can correct the source. Prof. Brenner calls this failing loudly, which is a vital habit for compliance tooling.

### 9.3 Repeatable reports

Nadia makes her reports repeatable: the same input always produces the same output, with the date of the run, the version of the script and a summary of the input file printed at the top. If an auditor asks how a figure was produced, she can rerun the exact version against the archived input. She learns that repeatability turns a script from a personal convenience into organisational evidence, and that a report without its inputs and version cannot be checked by anyone else later.

### Worked example

Nadia splits her checker into tested modules, reports unreadable rows loudly and stamps reports with run date, version and input summary.

> **Synthetic case.** Registers and data are synthetic.

### Errors and limits

Tests cover only cases someone imagined. Archived inputs need retention rules.

### Exercises

- **EX025 — Module split.** Into which three modules did Nadia split her tool? *Rubric:* 3 = reading, rule checking and reporting;; 2 = three;; 1 = none;; 0 = none.
- **EX026 — Skipped rows.** Why is silently skipping unreadable rows dangerous? *Rubric:* 3 = it could hide an unowned risk;; 2 = hidden risk;; 1 = none;; 0 = none.
- **EX027 — Report header.** What does each report print at the top? *Rubric:* 3 = run date, script version and input summary;; 2 = header;; 1 = none;; 0 = none.

### Synthesis

Tested modules, loud failures and repeatable reports make governance tools trustworthy.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering ethics to governance decisions; (2) weigh safety against security and compliance; (3) handle pressure to misreport.

### 10.1 Duties of an engineer

Nadia studies professional codes that place public safety first. At Ardwell, governance decisions affect electricity supply to homes, hospitals and businesses, so they carry safety consequences. She learns that an engineer who signs off a control or a risk assessment takes responsibility for its accuracy. Ethics also means competence: not claiming expertise in an area where one has none, and asking for help when a judgement exceeds one's knowledge. These duties apply equally to compliance work, which can seem administrative but shapes real decisions about public infrastructure.

### 10.2 Safety versus security

Some security controls can harm safety. Locking an operator out after failed sign-ins could prevent them from responding to a grid emergency. Nadia learns that in industrial settings, availability and safety often take priority, so controls must be designed with operators. She proposes monitoring and alerting for repeated failures at control consoles instead of lockout, with a physical access restriction to the control room. The decision is documented with its reasoning, so auditors understand why a standard control was adapted rather than applied unchanged.

### 10.3 Pressure to misreport

In a case study, a manager asks an analyst to mark a failed control test as passed so a certification audit goes smoothly. Nadia discusses the options: refuse, record the true result, escalate through the proper channel and protect the evidence. She learns that misreporting control results undermines the whole management system and may break laws or contracts. Prof. Brenner adds that organisations should make honest reporting safe, because a culture that punishes bad news drives problems out of sight until they cause harm.

### Worked example

Nadia applies safety-first ethics, adapts lockout to monitoring at control consoles and plans an honest response to pressure to misreport.

> **Synthetic case.** The case study and decisions are synthetic.

### Errors and limits

Codes give principles, not answers. Escalation can carry personal risk.

### Exercises

- **EX028 — Sign-off duty.** What does signing off a risk assessment mean for an engineer? *Rubric:* 3 = taking responsibility for its accuracy;; 2 = responsibility;; 1 = none;; 0 = none.
- **EX029 — Console alternative.** What did Nadia propose instead of lockout at control consoles? *Rubric:* 3 = monitoring and alerting with physical access restriction;; 2 = monitoring;; 1 = lockout;; 0 = none.
- **EX030 — Honest culture.** Why should organisations make honest reporting safe? *Rubric:* 3 = punishing bad news hides problems until they cause harm;; 2 = culture;; 1 = none;; 0 = none.

### Synthesis

Engineering ethics put safety and honest reporting at the heart of governance work.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) map network zones to governance scope; (2) assess remote access paths; (3) relate segmentation to compliance requirements.

### 11.1 Zones and boundaries

Nadia maps Ardwell's network into zones: the corporate office network, the customer payment environment, the control-system network and a zone for vendor remote access. Each boundary between zones is a place where traffic can be controlled and logged. Governance needs this map because scope decisions depend on it. For example, PCI DSS v4.0 applies to the cardholder data environment and connected systems, so good segmentation keeps the payment zone small and reduces the number of systems subject to its requirements. Nadia records this point in her course notebook so that later chapters can build on it.

### 11.2 Remote access paths

Vendors maintain control-system equipment over remote connections. Nadia traces each path: from the vendor's site through the internet to Ardwell's remote access gateway, then to a jump host and finally to the equipment. She notes which hops require multi-factor authentication, which are logged and who approves each session. One vendor uses a direct connection that bypasses the jump host. She records it as a finding, because a path without logging or approval breaks the governance assumptions behind the control design. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 11.3 Segmentation evidence

Claiming segmentation is not enough; it must be demonstrated. Nadia learns that assessors expect evidence such as firewall rule reviews and tests showing that traffic cannot cross boundaries it should not. She writes a test plan to verify that the corporate network cannot reach the control-system network directly. She also notes that segmentation must be retested after changes, because one new firewall rule can quietly connect zones. The test plan becomes evidence for both internal governance and external assessments. Nadia records this point in her course notebook so that later chapters can build on it.

### Worked example

Nadia maps four network zones, traces vendor paths, finds a bypass and plans segmentation tests as evidence.

> **Synthetic case.** Ardwell's network is synthetic; PCI DSS v4.0 is real.

### Errors and limits

Network diagrams drift from reality. Tests show only what was tested.

### Exercises

- **EX031 — Four zones.** Which four zones did Nadia map? *Rubric:* 3 = corporate, payment, control-system and vendor access;; 2 = four;; 1 = none;; 0 = none.
- **EX032 — Bypass finding.** Why was the direct vendor connection a finding? *Rubric:* 3 = it bypassed logging and approval;; 2 = bypass;; 1 = none;; 0 = none.
- **EX033 — Retesting.** When must segmentation be retested? *Rubric:* 3 = after changes such as new firewall rules;; 2 = after change;; 1 = never;; 0 = none.

### Synthesis

Network maps define scope, and segmentation must be demonstrated with evidence.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) relate operating system mechanisms to control objectives; (2) define secure configuration baselines; (3) measure configuration drift.

### 12.1 Mechanisms and objectives

Nadia studies how operating systems manage users, permissions, processes and logs. She links each mechanism to a control objective. User accounts and permissions support least privilege. Audit logs support accountability and investigation. Update mechanisms support vulnerability management. Understanding the mechanism helps her judge whether a control claim is credible. A policy saying administrators are restricted means little unless the operating system actually enforces separate administrator accounts and records their use in logs that ordinary users cannot change. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 12.2 Configuration baselines

Ardwell needs a secure configuration baseline for its office computers and servers: which services are disabled, which settings are enforced and how updates are applied. Nadia drafts a baseline based on vendor guidance and adapts it for Ardwell's needs, recording each deviation with its reason. A baseline turns a vague requirement for secure configuration into specific, testable settings. She learns that baselines need owners and review dates like policies, because operating system versions change and old settings can become irrelevant or harmful. She notes the assumption behind it so that a reviewer can challenge it later.

### 12.3 Measuring drift

Systems drift from their baseline as administrators make changes. Nadia writes a script that compares actual settings with the baseline and reports differences. In a synthetic test of forty servers, a quarter show at least one deviation, mostly an unneeded service enabled for troubleshooting and never turned off. She learns that drift is normal and that the governance question is how quickly it is detected and corrected. Regular measurement turns the baseline from a document into a living control with an observable outcome. The same reasoning will return when Ardwell's auditors visit next year.

### Worked example

Nadia links OS mechanisms to objectives, drafts a baseline with recorded deviations and measures drift across servers.

> **Synthetic case.** Baseline and drift figures are synthetic.

### Errors and limits

Baselines lag new versions. Drift scripts miss settings they do not check.

### Exercises

- **EX034 — Admin claim.** What makes a policy restricting administrators credible? *Rubric:* 3 = separate admin accounts enforced and logged;; 2 = enforcement;; 1 = none;; 0 = none.
- **EX035 — Baseline deviations.** How should deviations from the baseline be handled? *Rubric:* 3 = recorded with reasons;; 2 = documented;; 1 = ignored;; 0 = none.
- **EX036 — Drift question.** What is the real governance question about drift? *Rubric:* 3 = how quickly it is detected and corrected;; 2 = speed;; 1 = none;; 0 = none.

### Synthesis

Operating system knowledge makes control claims testable through baselines and drift measurement.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) model a risk register as structured data; (2) validate register quality automatically; (3) protect governance data integrity.

### 13.1 Register as data

Ardwell's risk register lives in a spreadsheet edited by many people. Nadia models it as a table with defined fields: identifier, owner, last review date and a score from one to twenty-five on the cooperative's five-by-five scale. Defined fields allow automatic checks. She learns from database design that each field should have a type and allowed values, so that a score of thirty or a blank owner can be caught. Treating the register as data rather than a document is the first step towards reliable risk reporting.

### 13.2 Validating quality

Nadia's lab checks six synthetic register rows against three rules: every risk must have an owner, reviews must be no older than one hundred and eighty days, and scores must lie between one and twenty-five. The lab finds six issues affecting four rows. Two risks have no owner. Three reviews are overdue, one by over a year. One score of twenty-six is outside the scale. Only two rows are clean. Nadia sends each owner a specific list of fixes rather than a general reminder.

### Lab — Validating a synthetic risk register

```python
"""Validate a synthetic risk register: missing owners, overdue reviews, scores out of range."""
from datetime import date
today = date(2026, 10, 1)
reg = [("R01", "IT ops", date(2026, 6, 1), 12), ("R02", "", date(2026, 9, 1), 8),
       ("R03", "Finance", date(2025, 8, 15), 20), ("R04", "OT eng", date(2026, 3, 20), 26),
       ("R05", "HR", date(2026, 8, 30), 6), ("R06", "", date(2025, 11, 2), 15)]
issues = []
for rid, owner, last, score in reg:
    if not owner: issues.append((rid, "no owner"))
    if (today - last).days > 180: issues.append((rid, f"review overdue {(today-last).days} days"))
    if not 1 <= score <= 25: issues.append((rid, f"score {score} outside 1-25"))
for i in issues: print(*i)
print(f"rows {len(reg)}; issues {len(issues)}; clean rows {len(reg) - len({r for r, _ in issues})}")
```

Run with `python3 lab_register.py`. Verified output:

```text
R02 no owner
R03 review overdue 412 days
R04 review overdue 195 days
R04 score 26 outside 1-25
R06 no owner
R06 review overdue 333 days
rows 6; issues 6; clean rows 2
```

### 13.3 Integrity of governance data

A register that anyone can edit without a trace cannot serve as evidence. Nadia recommends moving it into a system that records who changed each entry and when, with approvals for score changes. She notes that falsified or careless edits could make risks look smaller before a board meeting. Version history makes such changes visible. Prof. Brenner adds that the same principles of integrity, access control and audit trails that protect business data apply to the governance data that describe risk. She adds a short note to the shared course wiki for other students.

### Worked example

Nadia defines typed register fields, finds six issues in four of six rows and recommends an audited register system.

> **Synthetic case.** The register rows are synthetic.

### Errors and limits

Validation checks form, not whether risks are correct. Audit trails need review.

### Exercises

- **EX037 — Validation rules.** Which three rules did the lab apply? *Rubric:* 3 = owner present, review within 180 days, score 1-25;; 2 = three rules;; 1 = none;; 0 = none.
- **EX038 — Clean rows.** How many of six rows were clean? *Rubric:* 3 = two;; 2 = 2;; 1 = six;; 0 = none.
- **EX039 — Integrity risk.** What could happen without change history? *Rubric:* 3 = risks made to look smaller before board meetings;; 2 = manipulation;; 1 = none;; 0 = none.

### Synthesis

Treating governance records as validated, audited data makes risk reporting reliable.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) apply secure development practices as governance controls; (2) manage change with approval and traceability; (3) include third-party code in risk.

### 14.1 Development as a control

Ardwell builds and maintains its customer payment portal. Nadia learns that secure development practices, such as code review, security testing and dependency management, are governance controls as well as engineering habits. ISO/IEC 27002:2022 includes controls for secure development life cycles and secure coding, and PCI DSS v4.0 requires that bespoke software for payment systems is developed securely. She maps each practice in the portal team's workflow to these requirements and notes where evidence already exists in the team's tools. This makes the governance consequence visible to people outside the engineering team.

### 14.2 Change management

Every change to the portal passes through a ticket, a code review and an approval before deployment. Nadia checks a synthetic month of changes and finds that most are traceable from ticket to deployment, but some emergency fixes skipped review. She recommends a documented emergency path with review after the fact within two working days. Traceable change management lets auditors confirm that what runs in production was approved, and lets engineers find which change introduced a problem when something breaks. She notes the assumption behind it so that a reviewer can challenge it later.

### 14.3 Third-party code

The portal depends on dozens of open-source libraries. Nadia learns that each is a supplier whose vulnerabilities become Ardwell's risk. She proposes a software bill of materials listing each component and its version, with automatic alerts when a known vulnerability is published. She also notes licensing obligations, which are a compliance issue in their own right. Prof. Brenner remarks that modern applications are mostly other people's code, so governance must extend to the components a team never wrote. Nadia keeps a dated copy of her working so that the result can be traced.

### Worked example

Nadia maps development practices to standards, finds untraceable emergency fixes and proposes a software bill of materials.

> **Synthetic case.** Change records are synthetic; standards cited are real.

### Errors and limits

Reviews vary in depth. Component lists miss transitive dependencies.

### Exercises

- **EX040 — Standards for development.** Which two standards did Nadia map secure development to? *Rubric:* 3 = ISO/IEC 27002:2022 and PCI DSS v4.0;; 2 = two;; 1 = none;; 0 = none.
- **EX041 — Emergency path.** What did Nadia recommend for emergency fixes? *Rubric:* 3 = a documented path with review within two working days;; 2 = after-the-fact review;; 1 = none;; 0 = none.
- **EX042 — Library risk.** Why are open-source libraries a governance concern? *Rubric:* 3 = their vulnerabilities and licences become Ardwell's risk;; 2 = supplier;; 1 = none;; 0 = none.

### Synthesis

Secure development, traceable change and component inventories are governance controls in software.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) define confidentiality, integrity and availability for Ardwell's assets; (2) link threats, vulnerabilities and impact to risk; (3) distinguish control types.

### 15.1 Security objectives

Nadia defines what security means for Ardwell's main assets. For customer payment data, confidentiality matters most. For meter readings that drive bills, integrity matters most. For control systems that keep power flowing, availability and safety matter most. She learns that ranking objectives per asset guides control choices, because a control that strengthens confidentiality, such as strict lockout, might weaken availability. Making these priorities explicit helps the board understand why controls differ across the organisation. The same reasoning will return when Ardwell's auditors visit next year.

### 15.2 Building blocks of risk

Nadia learns the building blocks used in NIST SP 800-30 Rev. 1: threat sources and events, vulnerabilities and predisposing conditions, likelihood and impact. Risk arises when a threat can exploit a vulnerability to cause an impact. She applies this to vendor remote access: the threat is misuse of a vendor account, the vulnerability is a shared password, and the impact is an unplanned outage. Separating the parts helps her see where a control can act, such as replacing the shared password with named accounts. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 15.3 Control types

Controls can prevent, detect or correct, and they can be administrative, technical or physical. Nadia classifies Ardwell's controls for vendor access: named accounts and approval are preventive; session logging is detective; a tested procedure to revoke access during an incident is corrective. She learns that relying on only one type is fragile, because prevention eventually fails. A balanced set allows Ardwell to stop most problems, notice the rest and recover, which is the basis of defence in depth. She adds a short note to the shared course wiki for other students.

### Worked example

Nadia ranks security objectives per asset, decomposes vendor access risk using SP 800-30 terms and balances preventive, detective and corrective controls.

> **Synthetic case.** Assets and controls are synthetic; SP 800-30 Rev. 1 is real.

### Errors and limits

Objective rankings can be contested. Classifications blur in practice.

### Exercises

- **EX043 — Meter priority.** Which objective matters most for meter readings? *Rubric:* 3 = integrity;; 2 = integrity;; 1 = confidentiality;; 0 = none.
- **EX044 — Risk parts.** What vulnerability did Nadia identify for vendor access? *Rubric:* 3 = a shared password;; 2 = shared password;; 1 = none;; 0 = none.
- **EX045 — Corrective example.** Give the corrective control for vendor access. *Rubric:* 3 = tested procedure to revoke access during incidents;; 2 = revoke;; 1 = none;; 0 = none.

### Synthesis

Clear objectives, risk components and balanced control types form the basis of security governance.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) treat the governance programme as a system with requirements and interfaces; (2) trace requirements to controls and tests; (3) manage the system's life cycle.

### 16.1 Programme as a system

Systems engineering treats complex efforts as systems with purposes, components, interfaces and life cycles. Nadia applies this view to Ardwell's governance programme. Its purpose is to keep risk within the board's appetite and demonstrate compliance. Its components include policies, the risk register, control owners, monitoring and audits. Interfaces connect it to finance, operations and regulators. Viewing governance as a system helps her ask engineering questions, such as what happens when one component fails or an interface changes. This makes the governance consequence visible to people outside the engineering team.

### 16.2 Traceability

A core systems engineering tool is the traceability matrix. Nadia links each governance requirement, from law, contract or standard, to the controls that satisfy it and to the tests that show they work. Gaps appear as requirements with no control or controls with no test. She recognises this as the same coverage problem studied in compliance mapping. Traceability lets Ardwell answer an auditor's question about any requirement quickly and shows managers which controls exist only to satisfy obligations that may have lapsed. She checks the idea against a second example before relying on it.

### 16.3 Life cycle

Systems have life cycles: concept, development, operation, maintenance and retirement. Governance components do too. Policies are drafted, approved, used, reviewed and withdrawn. Controls are designed, implemented, tested and eventually replaced. Nadia notes that retirement is often neglected; old controls and policies remain on paper long after they stop working. NIST SP 800-37 Rev. 2 frames risk management as continuous across the life cycle, and she adopts its emphasis on monitoring as the step that keeps the system honest. Nadia keeps a dated copy of her working so that the result can be traced.

### Worked example

Nadia models governance as a system, builds a requirement-to-control-to-test trace and plans life-cycle management including retirement.

> **Synthetic case.** Ardwell's programme is synthetic; SP 800-37 Rev. 2 is real.

### Errors and limits

System views can become bureaucratic. Traceability needs upkeep.

### Exercises

- **EX046 — Programme purpose.** What is the purpose of Ardwell's governance programme as a system? *Rubric:* 3 = keep risk within appetite and demonstrate compliance;; 2 = purpose;; 1 = none;; 0 = none.
- **EX047 — Trace gaps.** What gaps does a traceability matrix reveal? *Rubric:* 3 = requirements without controls and controls without tests;; 2 = gaps;; 1 = none;; 0 = none.
- **EX048 — Neglected stage.** Which life-cycle stage is often neglected for controls and policies? *Rubric:* 3 = retirement;; 2 = retirement;; 1 = design;; 0 = none.

### Synthesis

Systems engineering brings traceability and life-cycle thinking to governance programmes.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) describe governance as a feedback loop; (2) identify sensors, set points and actuators in a management system; (3) recognise delays and oscillation in governance responses.

### 17.1 Governance as feedback

In control engineering, a system measures its output, compares it with a set point and adjusts its input to reduce the difference. Nadia sees the same loop in governance. Ardwell's board sets risk appetite as the set point. Monitoring and key risk indicators act as sensors. Decisions about budgets, controls and priorities act as actuators. ISO/IEC 27001:2022 builds this loop into its requirements for monitoring, internal audit, management review and continual improvement, so the management system corrects itself over time. Nadia records this point in her course notebook so that later chapters can build on it.

### 17.2 Delays

Feedback loops with long delays behave badly. If Ardwell measures control performance once a year, problems grow for months before anyone responds, and corrective actions arrive late. Nadia models a simple loop in which a backlog of findings is reviewed quarterly versus annually and sees that the annual loop lets the backlog swing much further from target. She learns that faster measurement does not guarantee better control, but slow measurement almost guarantees poor control, especially when risks change quickly. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 17.3 Overreaction

Too strong a response can also cause trouble. After a bad audit, management might impose strict controls everywhere, causing workarounds and complaints, then relax them, then tighten again. Engineers call this oscillation. Nadia suggests proportionate responses tied to the size of the gap and the importance of the asset. Prof. Brenner notes that good governance aims for steady improvement rather than dramatic swings, and that documented decision rules help managers respond consistently instead of reacting to the latest headline or audit report. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Nadia maps appetite, indicators and decisions onto a feedback loop and shows how delays and overreaction degrade governance.

> **Synthetic case.** The models are illustrative; ISO/IEC 27001:2022 is real.

### Errors and limits

Organisations are not linear systems. Indicators can be gamed.

### Exercises

- **EX049 — Set point.** What acts as the set point in Ardwell's governance loop? *Rubric:* 3 = the board's risk appetite;; 2 = appetite;; 1 = none;; 0 = none.
- **EX050 — Annual loop.** What happened to the backlog when reviewed annually instead of quarterly? *Rubric:* 3 = it swung further from target;; 2 = larger swings;; 1 = none;; 0 = none.
- **EX051 — Oscillation cure.** What helps managers avoid oscillating responses? *Rubric:* 3 = proportionate, documented decision rules;; 2 = rules;; 1 = none;; 0 = none.

### Synthesis

Governance works as a feedback loop that needs timely sensing and proportionate correction.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) translate governance requirements into architecture principles; (2) review an architecture against them; (3) record architecture decisions for audit.

### 18.1 Principles from requirements

Nadia learns that architecture turns requirements into structure. Ardwell's governance requirements include keeping payment data in a small segment, separating control systems from office systems and controlling vendor access. She writes architecture principles from them: minimise the scope of sensitive data, separate zones by trust level, broker all external access through monitored points and design for recovery. Principles give architects a basis for choices and give auditors a way to check that designs follow policy. The same reasoning will return when Ardwell's auditors visit next year.

### 18.2 Architecture review

Nadia joins a review of a proposed new meter data platform. She checks it against each principle. The design stores customer names with meter readings in a cloud service reachable from office laptops, which widens the scope of personal data and creates a new path into a sensitive store. She recommends pseudonymising readings and restricting access to an analytics zone. The review records each concern, the architect's response and the final decision, so the outcome can be traced later. She adds a short note to the shared course wiki for other students.

### 18.3 Decision records

Ardwell adopts short architecture decision records: the context, the decision, the alternatives considered and the consequences, including risks accepted. Nadia writes one for the meter platform. She learns that decision records help auditors see that risks were considered rather than overlooked, and help future engineers understand why something looks the way it does. Without them, organisations repeat old debates or undo good decisions because nobody remembers the reasons behind them. This makes the governance consequence visible to people outside the engineering team. Nadia keeps a dated copy of her working so that the result can be traced.

### Worked example

Nadia derives four architecture principles, reviews a meter platform design against them and records the decision with alternatives.

> **Synthetic case.** The platform and decisions are synthetic.

### Errors and limits

Principles can conflict. Decision records go unread if too long.

### Exercises

- **EX052 — Principle list.** Name two of Nadia's architecture principles. *Rubric:* 3 = minimise sensitive data scope; broker external access;; 2 = principles;; 1 = none;; 0 = none.
- **EX053 — Platform concern.** What was wrong with the meter platform design? *Rubric:* 3 = names stored with readings reachable from office laptops;; 2 = scope;; 1 = none;; 0 = none.
- **EX054 — Record contents.** What does an architecture decision record contain? *Rubric:* 3 = context, decision, alternatives and consequences;; 2 = four parts;; 1 = none;; 0 = none.

### Synthesis

Architecture principles and decision records connect governance requirements to system design.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) govern identities across their life cycle; (2) relate cryptographic controls to policy; (3) manage keys as governed assets.

### 19.1 Identity life cycle

Identities at Ardwell are created when staff join, change when they move and must end when they leave. Nadia maps this joiner, mover and leaver process and finds that movers are the weak point: new access is granted quickly but old access is rarely removed. She proposes that the human resources system trigger access changes automatically and that managers confirm access for movers within two weeks. Governance of identity is mainly governance of these transitions, where most excess access begins. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 19.2 Cryptography and policy

Nadia studies how encryption protects data at rest and in transit, and how digital signatures protect integrity. She links them to policy: Ardwell's data classification requires encryption for customer payment data and personal data on laptops. ISO/IEC 27002:2022 includes a control on the use of cryptography that expects rules for its use and for key management. She learns that cryptography is only as strong as the policy decisions about where to use it and how to manage it. She checks the idea against a second example before relying on it.

### 19.3 Keys as assets

Keys must be generated, stored, rotated and destroyed under control. Nadia lists Ardwell's important keys, including the payment portal's certificates, and finds one certificate managed by a single engineer with no backup or expiry tracking. If it expired unnoticed, the portal would fail. She records owners, expiry dates and backup arrangements for each key in an inventory. She learns that key management failures are usually governance failures, such as missing ownership, rather than weaknesses in the cryptography itself. The point seems small, but it changes how owners act on the result.

### Worked example

Nadia fixes the mover gap with automated triggers, links encryption to classification and inventories keys with owners and expiry dates.

> **Synthetic case.** Identities, keys and processes are synthetic; ISO/IEC 27002:2022 is real.

### Errors and limits

Automation fails when HR data are wrong. Key inventories go stale.

### Exercises

- **EX055 — Weak transition.** Which identity transition is Ardwell's weak point? *Rubric:* 3 = movers;; 2 = movers;; 1 = leavers;; 0 = none.
- **EX056 — Encryption rule.** Which data does Ardwell's classification require to be encrypted? *Rubric:* 3 = payment data and personal data on laptops;; 2 = classification;; 1 = none;; 0 = none.
- **EX057 — Certificate risk.** Why was the single-engineer certificate a risk? *Rubric:* 3 = no backup or expiry tracking, so it could expire unnoticed;; 2 = ownership;; 1 = none;; 0 = none.

### Synthesis

Identity and cryptographic controls succeed or fail through governance of transitions and keys.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Security governance, risk and compliance: engineering context

### Learning outcomes

You will (1) define governance, risk management and compliance and how they relate; (2) place them in Ardwell's organisation; (3) identify the obligations that shape the programme.

### 20.1 Three related disciplines

Nadia now begins the core GRC courses. Governance sets direction, accountability and oversight: who decides, what the appetite for risk is and how performance is monitored. Risk management identifies, analyses, evaluates and treats risks, following a process like the one described in ISO 31000:2018. Compliance ensures the organisation meets obligations from law, regulation, contracts and adopted standards. They overlap but differ. COBIT 2019 separates governance, which evaluates, directs and monitors, from management, which plans, builds, runs and monitors. Ardwell's security manager later asks for a copy of this analysis.

### 20.2 Place in the organisation

At Ardwell, the board approves risk appetite and receives quarterly reports. An information security manager runs the risk process and reports through the chief operating officer. Compliance obligations sit with a legal and compliance officer, while internal audit provides independent assurance to the board's audit committee. Nadia draws these relationships and notes that clear reporting lines prevent conflicts of interest, such as the person running controls also judging whether they work, which would weaken assurance. She marks the open questions in red so that they are not forgotten.

### 20.3 Obligations

Nadia lists Ardwell's obligations. Card payments bring PCI DSS v4.0 through contracts with its bank. Personal data of customers bring data protection law. As an energy distributor, Ardwell faces sector rules on resilience and incident reporting. The board has also chosen to align with ISO/IEC 27001:2022 and to use NIST CSF 2.0 for reporting. She separates mandatory obligations from voluntary choices, because penalties and flexibility differ, and records the source and owner of each in an obligations register. Writing the reasoning down also helps her spot a weak step in her argument.

### Worked example

Nadia defines governance, risk management and compliance, maps Ardwell's reporting lines and builds an obligations register.

> **Synthetic case.** Ardwell's structure is synthetic; ISO 31000:2018, COBIT 2019, PCI DSS v4.0 and CSF 2.0 are real.

### Errors and limits

Legal obligations need legal review. Roles differ between organisations.

### Exercises

- **EX058 — Governance role.** What does governance set? *Rubric:* 3 = direction, accountability and oversight;; 2 = direction;; 1 = none;; 0 = none.
- **EX059 — Independence.** Why should the person running controls not judge whether they work? *Rubric:* 3 = it creates a conflict of interest that weakens assurance;; 2 = independence;; 1 = none;; 0 = none.
- **EX060 — Mandatory or voluntary.** Is Ardwell's alignment with ISO/IEC 27001:2022 mandatory? *Rubric:* 3 = no, a board choice;; 2 = voluntary;; 1 = mandatory;; 0 = none.

### Synthesis

Governance, risk management and compliance are distinct disciplines joined by clear roles and obligations.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Security governance, risk and compliance: requirements

### Learning outcomes

You will (1) derive programme requirements from obligations and appetite; (2) write requirements that can be tested; (3) prioritise them.

### 21.1 From obligations to requirements

Obligations are often broad. Nadia turns them into specific requirements for Ardwell's programme. For example, a contractual obligation to protect card data becomes requirements to keep a current inventory of cardholder data systems, to restrict access to them by business need and to review that access regularly. The board's appetite statement that no single incident should interrupt supply for more than four hours becomes a recovery requirement for control-system backups and spare equipment. Nadia discusses the trade-off with a classmate who works in finance.

### 21.2 Testable requirements

Nadia learns to write requirements so they can be tested. A vague requirement such as access should be appropriate cannot be checked. A testable version says that access to cardholder data systems is reviewed every quarter and that excess access found is removed within ten working days. Each testable requirement names an owner, a frequency, a measurable condition and evidence. She rewrites twelve of Ardwell's requirements this way and finds that three had no clear owner at all. The class compares answers and finds that most differences come from unstated assumptions.

### 21.3 Prioritising

Not every requirement is equally urgent. Nadia ranks them by the consequence of failure and by whether they are mandatory. Requirements tied to safety of the electricity supply and to contractual card obligations rank highest. Requirements that support voluntary certification rank next. Improvements for efficiency come last. She presents the ranking to the information security manager with reasons, so that limited staff time goes first to the requirements whose failure would harm customers or breach obligations. Nadia records this point in her course notebook so that later chapters can build on it.

### Worked example

Nadia derives requirements from obligations and appetite, rewrites twelve as testable statements and ranks them by consequence.

> **Synthetic case.** Requirements are synthetic.

### Errors and limits

Testable wording can miss intent. Priorities shift with incidents.

### Exercises

- **EX061 — Appetite to requirement.** Which requirement followed from the four-hour appetite statement? *Rubric:* 3 = a recovery requirement for control-system backups and spares;; 2 = recovery;; 1 = none;; 0 = none.
- **EX062 — Testable parts.** What does each testable requirement name? *Rubric:* 3 = owner, frequency, measurable condition and evidence;; 2 = four parts;; 1 = none;; 0 = none.
- **EX063 — Top priority.** Which requirements ranked highest? *Rubric:* 3 = safety of supply and contractual card obligations;; 2 = safety;; 1 = efficiency;; 0 = none.

### Synthesis

Specific, testable and prioritised requirements turn obligations into an executable programme.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Security governance, risk and compliance: system and data models

### Learning outcomes

You will (1) model the entities of a GRC programme; (2) define relationships between risks, controls, obligations and evidence; (3) use the model to answer governance questions.

### 22.1 Core entities

Nadia designs a data model for Ardwell's programme. Its core entities are assets, risks, controls, obligations, tests, findings and owners. Each entity has defined attributes, such as a control's type, frequency and owner, or a finding's severity and due date. Defining entities clearly prevents the confusion common in spreadsheets, where one column might hold a risk in one row and a control in another. A clear model is the foundation for any governance tool, whether bought or built. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 22.2 Relationships

The value lies in relationships. A risk affects assets and is treated by controls. A control satisfies obligations and is checked by tests. A test produces evidence and may raise findings, each owned by a person. Nadia draws these as a diagram and notes that many-to-many links are common: one control can treat several risks and satisfy several obligations. This explains why a single failed control can create findings across several audits, a pattern Ardwell's managers had noticed but not understood. She notes the assumption behind it so that a reviewer can challenge it later.

### 22.3 Answering questions

With the model, Nadia shows how to answer questions that used to take days. Which obligations depend on the backup control? Which risks are treated only by controls that failed their last test? Which owners hold overdue findings? She writes example queries in plain language and in pseudocode. Prof. Brenner notes that good models make governance questions cheap to answer, which encourages managers to ask them more often, strengthening oversight across the organisation. The same reasoning will return when Ardwell's auditors visit next year.

### Worked example

Nadia defines seven core entities, maps many-to-many relationships and shows queries that answer governance questions.

> **Synthetic case.** The model is a teaching design; Ardwell's data are synthetic.

### Errors and limits

Models simplify messy reality. Data quality limits query value.

### Exercises

- **EX064 — Entity list.** Name four core entities in the model. *Rubric:* 3 = assets, risks, controls, obligations;; 2 = entities;; 1 = none;; 0 = none.
- **EX065 — Cascading findings.** Why can one failed control create findings in several audits? *Rubric:* 3 = it satisfies several obligations;; 2 = many-to-many;; 1 = none;; 0 = none.
- **EX066 — Example query.** Give one governance question the model answers quickly. *Rubric:* 3 = which risks rely only on controls that failed testing;; 2 = query;; 1 = none;; 0 = none.

### Synthesis

A clear data model of risks, controls, obligations and evidence makes governance questions answerable.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Security governance, risk and compliance: threat and failure analysis

### Learning outcomes

You will (1) identify threat scenarios for Ardwell; (2) analyse failure modes of governance controls; (3) combine threat and failure views in risk identification.

### 23.1 Threat scenarios

Nadia builds threat scenarios following the structure of NIST SP 800-30 Rev. 1. A criminal group encrypts office systems and demands payment. An insider in billing alters customer accounts. A vendor's compromised laptop connects to control systems. A card skimming script is injected into the payment portal. Each scenario names a threat source, an event, the vulnerabilities exploited and the impact. Scenarios make risk concrete for owners, who find it easier to judge likelihood and impact for a story than for an abstract category. She adds a short note to the shared course wiki for other students.

### 23.2 Failure modes

Controls themselves can fail. Nadia applies failure mode thinking to Ardwell's access review: reviewers may approve everything without checking, the list of accounts may be incomplete, or removals may be approved but never carried out. For each failure mode she asks how it would be detected and what its effect would be. This analysis reveals that nobody checks whether approved removals happen. She proposes a follow-up test comparing approved removals with actual account changes after each review. This makes the governance consequence visible to people outside the engineering team.

### 23.3 Combining views

Threat analysis asks what could attack Ardwell; failure analysis asks how its defences could quietly stop working. Nadia combines them in the risk register by linking scenarios to the controls they depend on and to those controls' failure modes. A scenario relying on a control with an undetected failure mode is riskier than it looks. Prof. Brenner notes that many real incidents combine an external threat with an internal control failure nobody noticed, so both views are needed. Nadia keeps a dated copy of her working so that the result can be traced.

### Worked example

Nadia writes four threat scenarios, analyses failure modes of access review and links both views in the register.

> **Synthetic case.** Scenarios are synthetic; SP 800-30 Rev. 1 is real.

### Errors and limits

Scenario lists are never complete. Failure analysis takes time.

### Exercises

- **EX067 — Scenario parts.** Which parts does each scenario name? *Rubric:* 3 = threat source, event, vulnerabilities and impact;; 2 = four;; 1 = none;; 0 = none.
- **EX068 — Hidden failure.** Which failure mode of access review went unchecked? *Rubric:* 3 = approved removals never carried out;; 2 = follow-up;; 1 = none;; 0 = none.
- **EX069 — Combined risk.** Why is a scenario relying on a control with an undetected failure mode riskier? *Rubric:* 3 = the defence may have quietly stopped working;; 2 = hidden failure;; 1 = none;; 0 = none.

### Synthesis

Combining threat scenarios with control failure modes reveals risks that either view alone would miss.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Security governance, risk and compliance: methods I

### Learning outcomes

You will (1) distinguish inherent and residual risk; (2) estimate residual risk from control effectiveness; (3) recognise risks with no treatment.

### 24.1 Inherent and residual

Inherent risk is the risk before considering controls; residual risk is what remains after them. Nadia learns that the distinction helps boards see what controls achieve and where risk remains above appetite. ISO/IEC 27005:2022 describes risk analysis and evaluation within the management system and expects organisations to decide on treatment and accept residual risks formally. For Ardwell she estimates inherent expected loss for four risks in thousands and the effectiveness of each control as the fraction of loss it removes. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 24.2 Calculating residual

The lab multiplies inherent loss by one minus each control's effectiveness, assuming controls act independently. Ransomware falls from ninety thousand to about twenty-two thousand, a reduction of seventy-six percent, through backups and endpoint detection. Billing outage halves from sixty to thirty thousand through failover. Card breach falls from seventy-five to about eleven thousand, an eighty-six percent reduction, through tokenisation and segmentation. Vendor misuse stays at eighty thousand because no control treats it, making it the largest residual risk. She checks the idea against a second example before relying on it.

### Lab — Inherent and residual risk with control effectiveness

```python
"""Inherent vs residual risk with control effectiveness (synthetic, ALE in thousands)."""
risks = {"ransomware": (90, [("offline backups", 0.6), ("EDR", 0.4)]),
         "billing outage": (60, [("failover", 0.5)]),
         "card breach": (75, [("tokenisation", 0.8), ("segmentation", 0.3)]),
         "vendor misuse": (80, [])}
for r, (inh, ctl) in risks.items():
    res = inh
    for _, e in ctl: res *= (1 - e)
    print(f"{r}: inherent {inh}k residual {res:.1f}k reduction {1-res/inh:.0%}")
```

Run with `python3 lab_residual.py`. Verified output:

```text
ransomware: inherent 90k residual 21.6k reduction 76%
billing outage: inherent 60k residual 30.0k reduction 50%
card breach: inherent 75k residual 10.5k reduction 86%
vendor misuse: inherent 80k residual 80.0k reduction 0%
```

### 24.3 Interpreting residuals

The lab changes the order of risks. Ransomware ranked first inherently, but vendor access misuse ranks first in residual terms because it is untreated. Nadia recommends that treatment of vendor access becomes a priority. She also notes the independence assumption may overstate combined effectiveness, since backups and detection might fail together in a well-planned attack. Effectiveness figures are estimates from workshops and should be checked with testing evidence over time, as later chapters on measurement will show. The point seems small, but it changes how owners act on the result.

### Worked example

Nadia computes residual losses, finds vendor misuse untreated at eighty thousand and recommends treating it first.

> **Synthetic case.** Losses and effectiveness values are synthetic; ISO/IEC 27005:2022 is real.

### Errors and limits

Independence overstates combined effect. Effectiveness estimates are subjective.

### Exercises

- **EX070 — Residual definition.** How does residual risk differ from inherent risk? *Rubric:* 3 = it remains after controls;; 2 = after controls;; 1 = before;; 0 = none.
- **EX071 — Ransomware residual.** By how much did controls reduce ransomware loss in the lab? *Rubric:* 3 = 76%, to 21.6k;; 2 = 76%;; 1 = none;; 0 = none.
- **EX072 — Largest residual.** Which risk had the largest residual loss and why? *Rubric:* 3 = vendor misuse at 80k, untreated;; 2 = vendor;; 1 = ransomware;; 0 = none.

### Synthesis

Residual risk shows what controls achieve and exposes untreated risks for priority action.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) design a governance solution for a defined problem; (2) present it for critique; (3) revise it based on feedback from users.

### 25.1 The brief

In the first design studio, Nadia's team receives a brief from Ardwell: design a way to manage vendor remote access that satisfies security, keeps outage response fast and produces evidence for audits. The team interviews a control engineer, a vendor technician and the information security manager. Each wants something different. The engineer wants vendors connected within minutes during outages. The technician wants one sign-in, not five. The manager wants every session approved, logged and reviewed. Nadia records this point in her course notebook so that later chapters can build on it.

### 25.2 The design

The team proposes an access broker: vendors sign in with named accounts and multi-factor authentication, request a session for a specific device, receive approval from an on-call engineer through a phone app and work through a recorded jump host. Pre-approved emergency sessions are allowed during declared outages, with review the next day. Sessions end automatically after four hours. The design meets each stakeholder's main concern while removing the shared password and direct connection found earlier. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 25.3 Critique and revision

At the studio review, a lecturer asks what happens if the phone app fails during a storm. Another asks who reviews recordings and how often. The team adds a backup approval by phone call with a logged reference and proposes sampling ten percent of recordings each month, focusing on emergency sessions. Nadia learns that critique is most useful when it tests the design against realistic failure, and that a design is not finished until its operation, including review, is planned. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Nadia's team designs a vendor access broker balancing speed, usability and evidence, then adds fallback approval and recording review after critique.

> **Synthetic case.** The brief and design are synthetic.

### Errors and limits

Studio designs skip cost detail. Stakeholder interviews are small samples.

### Exercises

- **EX073 — Stakeholder wants.** What did the control engineer want? *Rubric:* 3 = vendors connected within minutes during outages;; 2 = speed;; 1 = none;; 0 = none.
- **EX074 — Session limit.** How long can a vendor session last before ending automatically? *Rubric:* 3 = four hours;; 2 = 4h;; 1 = none;; 0 = none.
- **EX075 — Recording review.** How will recordings be reviewed? *Rubric:* 3 = sample ten percent monthly, focusing on emergencies;; 2 = sampling;; 1 = none;; 0 = none.

### Synthesis

Good governance designs balance stakeholder needs and plan for failure and review.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Security governance, risk and compliance: architecture alternatives

### Learning outcomes

You will (1) compare alternative architectures for a GRC capability; (2) weigh criteria transparently; (3) document the choice and its risks.

### 26.1 Alternatives

Ardwell must decide how to run its GRC programme day to day. Nadia compares three alternatives. The first keeps spreadsheets and shared folders, improved with validation scripts. The second buys a commercial governance platform that holds risks, controls and evidence in one place. The third builds light tooling on Ardwell's existing ticketing system, where controls become recurring tasks and evidence attaches to tickets. Each has different costs, skills needs and risks of failure. The same reasoning will return when Ardwell's auditors visit next year.

### 26.2 Criteria and weights

Nadia agrees criteria with the security manager: data integrity and audit trail, effort for control owners, reporting to the board, cost over three years and dependence on scarce skills. She weights integrity and owner effort highest. Spreadsheets score poorly on integrity. The commercial platform scores well on reporting but needs a specialist administrator. The ticketing option scores well on owner effort because staff already use the system. She publishes the scores and weights so reviewers can challenge them. She adds a short note to the shared course wiki for other students.

### 26.3 The choice

The ticketing option wins narrowly over the platform. Nadia documents the decision with its alternatives and accepted risks: reporting will need extra work, and the ticketing vendor's roadmap could change. She recommends reviewing the choice after a year using measures such as overdue control tasks and time to prepare audit evidence. She notes that the close result means the weights matter, and records that a different weighting favouring board reporting would have chosen the platform instead. This makes the governance consequence visible to people outside the engineering team.

### Worked example

Nadia compares three GRC tooling options on weighted criteria, chooses the ticketing approach narrowly and records the sensitivity to weights.

> **Synthetic case.** Options, scores and costs are synthetic.

### Errors and limits

Weights reflect opinion. Vendor claims need verification.

### Exercises

- **EX076 — Three options.** What are the three alternatives? *Rubric:* 3 = spreadsheets with scripts, commercial platform, ticketing-based tooling;; 2 = three;; 1 = none;; 0 = none.
- **EX077 — Heaviest criteria.** Which criteria received the highest weights? *Rubric:* 3 = data integrity and owner effort;; 2 = integrity;; 1 = cost;; 0 = none.
- **EX078 — Sensitivity note.** What would a weighting favouring board reporting have chosen? *Rubric:* 3 = the commercial platform;; 2 = platform;; 1 = spreadsheets;; 0 = none.

### Synthesis

Transparent criteria and sensitivity notes make architecture choices defensible.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Security governance, risk and compliance: control design

### Learning outcomes

You will (1) design controls with clear objectives and attributes; (2) select controls from a reference catalogue; (3) document controls so they can be tested.

### 27.1 Control objectives

Nadia learns that a well-designed control starts with an objective: what risk it reduces and how. For vendor access, the objective is that only approved, identified vendors reach control systems, only for approved tasks, with a record of what they did. From the objective she derives attributes: type, frequency, owner, automation level and the evidence produced. Without a clear objective, controls drift into rituals that are performed but no longer linked to the risk they were meant to reduce. Nadia keeps a dated copy of her working so that the result can be traced.

### 27.2 Using a catalogue

Rather than inventing controls, Nadia consults ISO/IEC 27002:2022 and NIST SP 800-53 Rev. 5. The catalogues offer tested ideas: account management, remote access, session audit and supplier relationship controls. She selects and tailors them to Ardwell, recording which catalogue controls are applied, adapted or excluded, and why. This record resembles the statement of applicability that ISO/IEC 27001:2022 requires, and it lets auditors see that the selection followed from risk rather than habit or convenience. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 27.3 Documenting for testing

Each control description answers who does what, when, using what, and what evidence results. For the monthly recording review, the description names the security analyst, the ten percent sample, the criteria for concern and the report filed in the ticketing system. Nadia checks that an independent tester could verify the control from the description alone. Prof. Brenner notes that ambiguous control descriptions are a common audit problem, because testers and owners then disagree about what the control was supposed to do. She checks the idea against a second example before relying on it.

### Worked example

Nadia states a control objective, selects and tailors catalogue controls with recorded reasons and writes testable control descriptions.

> **Synthetic case.** Control designs are synthetic; ISO/IEC 27002:2022, 27001:2022 and SP 800-53 Rev. 5 are real.

### Errors and limits

Catalogues are generic. Descriptions can describe intent rather than practice.

### Exercises

- **EX079 — Objective role.** Why should every control start with an objective? *Rubric:* 3 = so it stays linked to the risk it reduces;; 2 = objective;; 1 = none;; 0 = none.
- **EX080 — Selection record.** Which ISO/IEC 27001:2022 document does the selection record resemble? *Rubric:* 3 = the statement of applicability;; 2 = SoA;; 1 = none;; 0 = none.
- **EX081 — Description test.** How does Nadia check a control description? *Rubric:* 3 = an independent tester could verify it from the description alone;; 2 = testability;; 1 = none;; 0 = none.

### Synthesis

Objectives, catalogues and testable descriptions produce controls that can be operated and verified.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Security governance, risk and compliance: implementation I

### Learning outcomes

You will (1) plan control implementation with owners and milestones; (2) manage change for people affected; (3) track implementation status honestly.

### 28.1 Planning

Ardwell approves the vendor access broker and the ticketing-based GRC tooling. Nadia helps write the implementation plan: phases, owners, milestones, dependencies and acceptance criteria. Phase one moves the two highest-risk vendors to the broker. Phase two moves the rest. Phase three retires the direct connection and shared passwords. Each phase has a test that must pass before the next starts. She learns that phased plans reduce risk, because problems appear while the scope is still small. The point seems small, but it changes how owners act on the result.

### 28.2 People and change

New controls change people's work. Vendor technicians must learn new sign-ins, and on-call engineers must approve sessions at night. Nadia helps prepare short guides, a test session for each vendor and a contact for problems. She records concerns, such as approval fatigue at night, and the responses, such as allowing pre-approved maintenance windows. She learns that adoption problems are often treated as user resistance when they are really design issues that the implementation team can fix. Ardwell's security manager later asks for a copy of this analysis.

### 28.3 Honest status

Nadia builds a status report showing each milestone as complete, on track, at risk or late, with reasons. When one vendor's equipment cannot support the broker, she marks the milestone late and records a temporary compensating control: supervised sessions with an Ardwell engineer present. Prof. Brenner praises the honest status. He notes that reporting everything as green until the deadline is a common failure, and that boards can only help with problems they are told about in time. She marks the open questions in red so that they are not forgotten.

### Worked example

Nadia plans phased implementation, addresses approval fatigue with maintenance windows and reports a late milestone honestly with a compensating control.

> **Synthetic case.** Plans and vendors are synthetic.

### Errors and limits

Plans meet surprises. Compensating controls can become permanent.

### Exercises

- **EX082 — Phase one.** What does phase one cover? *Rubric:* 3 = moving the two highest-risk vendors to the broker;; 2 = two vendors;; 1 = none;; 0 = none.
- **EX083 — Night approvals.** How was approval fatigue at night addressed? *Rubric:* 3 = pre-approved maintenance windows;; 2 = windows;; 1 = none;; 0 = none.
- **EX084 — Compensating control.** What compensating control covered the vendor whose equipment could not use the broker? *Rubric:* 3 = supervised sessions with an Ardwell engineer;; 2 = supervision;; 1 = none;; 0 = none.

### Synthesis

Phased plans, attention to people and honest status reporting make implementation succeed.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Security governance, risk and compliance: measurement

### Learning outcomes

You will (1) measure control performance through test results; (2) set thresholds for key risk indicators; (3) report measures without hiding weak areas.

### 29.1 What to measure

Nadia learns to separate measures of activity, such as the number of reviews held, from measures of performance, such as the share of control tests passed, and measures of outcome, such as excess access found. NIST CSF 2.0 encourages organisations to monitor and improve their cybersecurity outcomes, and ISO/IEC 27001:2022 requires the organisation to determine what is measured and how results are evaluated. She proposes that Ardwell report mainly performance and outcome measures to the board. Writing the reasoning down also helps her spot a weak step in her argument.

### 29.2 Pass rates and thresholds

For one quarter, Ardwell tests five control families. The lab computes pass rates and applies thresholds agreed with management: green at ninety-five percent or more, amber from eighty percent, red below that. Access passes forty-five of forty-eight tests, ninety-four percent, just amber. Patching passes thirty-one of forty, seventy-eight percent, red. Backup passes all twelve. Logging is amber at eighty-seven percent and change management is red at seventy-two percent. Overall, one hundred and thirty-two of one hundred and fifty-five pass. Nadia discusses the trade-off with a classmate who works in finance.

### Lab — Control pass rates against thresholds

```python
"""Control test pass rates and key risk indicator thresholds (synthetic quarter)."""
tests = {"access": (48, 45), "patching": (40, 31), "backup": (12, 12), "logging": (30, 26), "change": (25, 18)}
for fam, (n, ok) in tests.items():
    r = ok/n
    status = "green" if r >= 0.95 else "amber" if r >= 0.80 else "red"
    print(f"{fam}: {ok}/{n} = {r:.0%} {status}")
n = sum(v[0] for v in tests.values()); ok = sum(v[1] for v in tests.values())
print(f"overall {ok}/{n} = {ok/n:.0%}")
```

Run with `python3 lab_kri.py`. Verified output:

```text
access: 45/48 = 94% amber
patching: 31/40 = 78% red
backup: 12/12 = 100% green
logging: 26/30 = 87% amber
change: 18/25 = 72% red
overall 132/155 = 85%
```

### 29.3 Not hiding weak areas

The overall figure of eighty-five percent looks reasonable, but it hides two red families. Nadia reports each family separately, leading with the reds and their causes: patching delays on substation equipment and emergency changes without review. She warns that thresholds influence behaviour; if teams are judged only on pass rates, they may test easy cases. She recommends rotating test samples and reviewing how tests are chosen, so the measure stays honest over time. The class compares answers and finds that most differences come from unstated assumptions.

### Worked example

Nadia distinguishes activity, performance and outcome measures, computes five pass rates with thresholds and reports red families first.

> **Synthetic case.** Test results and thresholds are synthetic; CSF 2.0 and ISO/IEC 27001:2022 are real.

### Errors and limits

Aggregates hide weak areas. Measures invite gaming.

### Exercises

- **EX085 — Measure kinds.** Which three kinds of measure did Nadia separate? *Rubric:* 3 = activity, performance and outcome;; 2 = three;; 1 = none;; 0 = none.
- **EX086 — Red families.** Which two control families were red? *Rubric:* 3 = patching 78% and change 72%;; 2 = two reds;; 1 = backup;; 0 = none.
- **EX087 — Aggregate risk.** Why is the overall 85% misleading? *Rubric:* 3 = it hides two red families;; 2 = hides;; 1 = none;; 0 = none.

### Synthesis

Measures should show performance by family, lead with weaknesses and resist gaming.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify that controls operate as described; (2) collect and record evidence properly; (3) report verification findings.

### 30.1 Planning verification

In the verification laboratory, Nadia tests the vendor access broker against its control descriptions. For each control she writes a test step, the expected result and the evidence to keep. She checks that a vendor without multi-factor authentication cannot sign in, that a session without approval cannot start, that sessions end after four hours and that recordings appear in the archive. She uses a test vendor account in a laboratory copy of the broker, so production is not disturbed. Nadia records this point in her course notebook so that later chapters can build on it.

### 30.2 Evidence

For each test Nadia records the date, the tester, the steps, the result and supporting artefacts such as screenshots and log extracts. She names files consistently and stores them where they cannot be edited after filing. She learns that evidence must allow another person to understand and repeat the test. An auditor will not accept a statement that a test passed without seeing what was done and what was observed, and a future engineer will need the same detail. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 30.3 Findings

Most tests pass, but one fails: a session approved for one device can reach a second device on the same network segment. Nadia records the finding with its severity, the evidence and a recommended fix: restricting the jump host's routes per session. She reports it to the implementation team, who fix it and ask her to retest. The retest passes and is recorded. She learns that verification is valuable precisely because it finds what designers assumed would not happen. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Nadia verifies four broker controls in a lab copy, records repeatable evidence and finds and retests a route restriction failure.

> **Synthetic case.** The broker and tests are synthetic.

### Errors and limits

Lab copies differ from production. Tests cover planned cases only.

### Exercises

- **EX088 — Lab copy.** Why test in a laboratory copy? *Rubric:* 3 = so production is not disturbed;; 2 = safety;; 1 = none;; 0 = none.
- **EX089 — Evidence fields.** What does Nadia record for each test? *Rubric:* 3 = date, tester, steps, result and artefacts;; 2 = evidence;; 1 = none;; 0 = none.
- **EX090 — Failed test.** Which test failed? *Rubric:* 3 = an approved session could reach a second device;; 2 = routing;; 1 = none;; 0 = none.

### Synthesis

Verification with repeatable evidence finds failures that designers assumed away.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Security governance, risk and compliance: implementation II

### Learning outcomes

You will (1) roll out a GRC capability across the organisation; (2) integrate controls into routine work; (3) manage exceptions formally.

### 31.1 Rolling out the tooling

With the broker running, Ardwell rolls out its ticketing-based GRC tooling. Each control becomes a recurring task assigned to its owner, with the control description, test steps and an evidence field. Nadia helps migrate eighty controls from spreadsheets, checking each for an owner and a frequency. Twelve controls have no clear owner, and three describe practices that no longer exist. Migration thus becomes a cleanup exercise, removing obsolete controls and assigning owners before the first cycle begins. The same reasoning will return when Ardwell's auditors visit next year.

### 31.2 Routine integration

Controls work best when they fit existing routines. Nadia links the quarterly access review to the human resources reporting cycle, so reviewers receive current role lists. She schedules patch evidence collection to follow the monthly maintenance window. Owners receive reminders a week before tasks are due, and overdue tasks escalate to managers after five days. She learns that integration into routine work reduces the effort of compliance and makes evidence a by-product of operations rather than a separate burden. She adds a short note to the shared course wiki for other students.

### 31.3 Exceptions

Some controls cannot be applied everywhere. An old substation device cannot support current authentication. Nadia helps design an exception process: the owner requests an exception, states the risk and compensating controls, a manager approves it for a limited time and the exception appears in the risk register. Exceptions expire and must be renewed with fresh reasoning. She learns that unmanaged exceptions become hidden permanent gaps, while managed ones keep risk visible and decisions accountable. This makes the governance consequence visible to people outside the engineering team.

### Worked example

Nadia migrates eighty controls, finds twelve unowned and three obsolete, integrates tasks into routines and designs time-limited exceptions.

> **Synthetic case.** Control counts and processes are synthetic.

### Errors and limits

Reminders cause fatigue. Exceptions are often renewed by habit.

### Exercises

- **EX091 — Migration findings.** What did the migration reveal? *Rubric:* 3 = twelve controls without owners and three obsolete;; 2 = cleanup;; 1 = none;; 0 = none.
- **EX092 — Escalation rule.** When do overdue tasks escalate to managers? *Rubric:* 3 = after five days;; 2 = five days;; 1 = none;; 0 = none.
- **EX093 — Exception expiry.** Why must exceptions expire? *Rubric:* 3 = to force fresh reasoning and keep risk visible;; 2 = renewal;; 1 = none;; 0 = none.

### Synthesis

Rollout succeeds when controls fit routines and exceptions remain visible and time-limited.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Security governance, risk and compliance: reliability

### Learning outcomes

You will (1) compute the probability that layered controls both fail; (2) account for common-cause failure; (3) design for independence.

### 32.1 Layered controls

Ardwell protects vendor access with two layers: the broker's approval check and network rules that block unapproved routes. Nadia asks how likely it is that both fail at once. If the approval check fails five percent of the time and the network rules ten percent, and failures are independent, both fail only half a percent of the time. Layering seems to give strong protection. Reliability engineering, however, warns that independence is an assumption that must be justified before it is trusted. Nadia keeps a dated copy of her working so that the result can be traced.

### 32.2 Common cause

The lab adds a two percent chance of a common cause that defeats both layers at once, such as an administrator account able to change both the broker and the network rules. The joint failure probability rises from one half of a percent to about two and a half percent, five times higher. Nadia sees that the common cause dominates the result. Improving either layer alone barely helps; removing the shared dependency matters far more. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### Lab — Joint failure of two controls with and without common cause

```python
"""Failure probability of two controls: independent vs with a common cause (synthetic)."""
p1, p2, beta = 0.05, 0.10, 0.02
ind = p1*p2
cc = beta + (1-beta)*p1*p2
print(f"single control A fails {p1:.2%}; B fails {p2:.2%}")
print(f"both fail if independent {ind:.2%}")
print(f"both fail with 2% common cause {cc:.2%}")
```

Run with `python3 lab_layers.py`. Verified output:

```text
single control A fails 5.00%; B fails 10.00%
both fail if independent 0.50%
both fail with 2% common cause 2.49%
```

### 32.3 Designing for independence

Nadia recommends separating administration of the broker and network rules between different teams with different accounts, logging changes to both in a system neither team controls and testing them separately. She notes that common causes also include shared training, shared suppliers and shared assumptions. Prof. Brenner adds that governance reports often count layers as if each were independent, so stating dependencies explicitly is a sign of mature risk analysis and a frequent gap in audit evidence. She checks the idea against a second example before relying on it.

### Worked example

Nadia computes 0.50% joint failure for independent layers and 2.49% with a 2% common cause, then separates administration to reduce it.

> **Synthetic case.** Failure rates are synthetic.

### Errors and limits

Common-cause rates are hard to estimate. Separation adds cost.

### Exercises

- **EX094 — Independent joint.** What is the joint failure probability for independent layers? *Rubric:* 3 = 0.50%;; 2 = 0.005;; 1 = none;; 0 = none.
- **EX095 — Common-cause joint.** How large is the joint failure probability with a 2% common cause? *Rubric:* 3 = 2.49%;; 2 = about five times;; 1 = none;; 0 = none.
- **EX096 — Best fix.** What reduces joint failure most? *Rubric:* 3 = removing the shared dependency;; 2 = independence;; 1 = stronger single layer;; 0 = none.

### Synthesis

Layered controls are only as strong as their independence; common causes dominate joint failure.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Security governance, risk and compliance: safety and resilience

### Learning outcomes

You will (1) integrate safety and resilience into governance; (2) plan for continued operation under attack; (3) test recovery objectives.

### 33.1 Resilience as a governance goal

For an electricity distributor, preventing every incident is impossible, so the board's real goal is resilience: keeping power flowing and restoring services quickly when things go wrong. Nadia learns that NIST CSF 2.0 includes Respond and Recover functions alongside protection and detection, and that ISO/IEC 27002:2022 covers information security during disruption and ICT readiness for business continuity. She helps Ardwell define recovery time objectives for billing, the payment portal and control systems, agreed with the board. Nadia records this point in her course notebook so that later chapters can build on it.

### 33.2 Operating under attack

Nadia joins a workshop on operating while office systems are encrypted by ransomware. Control rooms must keep running on isolated systems with paper procedures for switching. Billing can pause for days without harming customers if communication is clear. The payment portal can redirect customers to pay later. Each decision is recorded in a continuity plan. She learns that resilience planning forces governance to decide in advance which services matter most, rather than improvising priorities during a crisis. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 33.3 Testing recovery

Plans must be tested. Ardwell restores billing from backup in a test environment and measures the time: nine hours against a target of eight. Nadia records the gap, its causes and fixes, such as pre-staging restore scripts. A control-room exercise shows that paper procedures are out of date. She learns that recovery tests often fail first time, which is their purpose, and that recording and closing gaps is what turns a plan on paper into real resilience the board can rely on. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Nadia helps set recovery objectives, plans operation under ransomware and records a nine-hour restore against an eight-hour target.

> **Synthetic case.** Objectives and test results are synthetic; CSF 2.0 and ISO/IEC 27002:2022 are real.

### Errors and limits

Tests are rehearsed scenarios. Real crises bring surprises.

### Exercises

- **EX097 — Board goal.** What is Ardwell's real resilience goal? *Rubric:* 3 = keep power flowing and restore services quickly;; 2 = resilience;; 1 = none;; 0 = none.
- **EX098 — Restore gap.** How did the billing restore test compare with its target? *Rubric:* 3 = nine hours versus eight;; 2 = over by one hour;; 1 = none;; 0 = none.
- **EX099 — Test purpose.** Why are failed first recovery tests valuable? *Rubric:* 3 = they reveal gaps to close;; 2 = learning;; 1 = none;; 0 = none.

### Synthesis

Resilience governance sets priorities in advance and proves recovery through testing.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Security governance, risk and compliance: integration

### Learning outcomes

You will (1) integrate GRC with enterprise risk management; (2) connect security risk to financial and operational reporting; (3) align processes across departments.

### 34.1 Enterprise risk

Ardwell already has an enterprise risk register covering financial, operational, regulatory and safety risks. Security risks lived in a separate register, so the board saw them in isolation. Nadia helps integrate them, mapping security risks to enterprise categories and using common scales for likelihood and impact. ISO 31000:2018 promotes integrating risk management into all organisational activities, and COBIT 2019 links IT goals to enterprise goals. Integration lets the board compare cyber risk with other risks on equal terms. The same reasoning will return when Ardwell's auditors visit next year.

### 34.2 Common language

Integration requires a shared language. Security teams spoke of vulnerabilities and threats; finance spoke of losses and provisions. Nadia drafts a glossary and translation table. A ransomware scenario becomes an operational disruption risk with a financial impact range and a regulatory reporting obligation. She learns that translation is not simplification but connection: each audience keeps its precision while seeing how the risk relates to things it already manages, such as insurance cover and reserves. She adds a short note to the shared course wiki for other students.

### 34.3 Aligned processes

Nadia aligns calendars so security risk reviews feed the quarterly enterprise risk report, internal audit plans consider security findings and procurement checks supplier security before contracts. Each department keeps its own process, but handoffs are defined. She learns that integration fails when it means one team taking over another's work, and succeeds when interfaces are clear. Prof. Brenner notes that this is an application of systems engineering's emphasis on interfaces, which she studied earlier. This makes the governance consequence visible to people outside the engineering team.

### Worked example

Nadia maps security risks into enterprise categories, builds a translation glossary and aligns review calendars across departments.

> **Synthetic case.** Registers and processes are synthetic; ISO 31000:2018 and COBIT 2019 are real.

### Errors and limits

Common scales can blur distinctions. Integration takes political effort.

### Exercises

- **EX100 — Integration benefit.** What does integrating registers let the board do? *Rubric:* 3 = compare cyber risk with other risks equally;; 2 = comparison;; 1 = none;; 0 = none.
- **EX101 — Translation example.** How was a ransomware scenario translated for finance? *Rubric:* 3 = operational disruption with financial impact range and reporting obligation;; 2 = translation;; 1 = none;; 0 = none.
- **EX102 — Integration failure.** When does integration fail? *Rubric:* 3 = when one team takes over another's work;; 2 = takeover;; 1 = none;; 0 = none.

### Synthesis

Integrating GRC with enterprise risk needs common scales, translation and clear handoffs.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design a board reporting pack for security risk; (2) test it with real readers; (3) revise for clarity and decision value.

### 35.1 The brief

In the second studio, Nadia's team designs a quarterly board pack on security risk for Ardwell. The brief asks for no more than four pages, a focus on decisions and honest uncertainty. The team interviews two board members. One wants to know whether risk is rising or falling. The other wants to know what the board is being asked to decide. Neither wants technical detail, but both want to trust the numbers and know where they came from. Nadia keeps a dated copy of her working so that the result can be traced.

### 35.2 The design

The pack opens with decisions requested. Page two shows the top five residual risks with expected loss ranges and trend arrows. Page three shows control performance by family with red items first. Page four lists major findings, exceptions and incidents with owners and dates. An appendix explains methods and assumptions. The team avoids heat maps without numbers, after reading Cox (2008) on how risk matrices can mislead, and uses ranges and plain sentences instead. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 35.3 Testing and revision

The team tests the pack with three volunteers acting as board members. One misreads a trend arrow as good news when risk was rising. Another cannot find who owns a red control. The team adds labelled arrows with words and puts owner names beside each red item. A volunteer asks why ransomware residual risk fell; the team adds a sentence linking the drop to tested backups. Nadia learns that readers reveal confusion that designers cannot see. She checks the idea against a second example before relying on it.

### Worked example

Nadia's team designs a four-page board pack with decisions first, tests it with volunteers and clarifies trends and ownership.

> **Synthetic case.** The pack and testers are synthetic; Cox (2008) is real.

### Errors and limits

Volunteers are not real directors. Short packs omit detail.

### Exercises

- **EX103 — Board wishes.** What did the two interviewed board members want? *Rubric:* 3 = trend direction and decisions asked;; 2 = trend and decisions;; 1 = none;; 0 = none.
- **EX104 — Matrix avoidance.** Why did the team avoid numberless heat maps? *Rubric:* 3 = Cox (2008) shows risk matrices can mislead;; 2 = Cox;; 1 = none;; 0 = none.
- **EX105 — Arrow fix.** How was the misread trend arrow fixed? *Rubric:* 3 = labelled arrows with words;; 2 = labels;; 1 = none;; 0 = none.

### Synthesis

Board reports work when they lead with decisions, show honest ranges and are tested with readers.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Security governance, risk and compliance: performance and scale

### Learning outcomes

You will (1) estimate the workload of a GRC programme; (2) find bottlenecks as it scales; (3) reduce effort through automation and sampling.

### 36.1 Workload

Nadia estimates the yearly workload of Ardwell's programme: eighty controls with tests at various frequencies, quarterly access reviews across ten systems, monthly recording sampling and annual audits. She counts hours per activity using owners' estimates and finds the total close to two full-time staff, spread thinly across many people. She learns that GRC programmes often fail not from bad design but from underestimated effort, which leads to skipped tests and stale evidence. The point seems small, but it changes how owners act on the result.

### 36.2 Bottlenecks

As Ardwell plans to add a second control centre and more vendors, Nadia models growth. Access reviews and evidence collection scale with systems and vendors, but the security analyst who checks evidence is a single person. At current growth, her queue would double within a year. Nadia identifies her as the bottleneck and recommends spreading review across trained control owners, with the analyst sampling their work. Finding the narrowest point lets Ardwell invest where it matters most. Ardwell's security manager later asks for a copy of this analysis.

### 36.3 Automation and sampling

Nadia lists tasks that could be automated: collecting patch levels, exporting account lists and checking configuration baselines. Automation reduces effort and improves consistency, though scripts need their own testing and ownership. For tasks requiring judgement, such as reviewing recordings, sampling reduces effort while keeping assurance. She learns that scale in governance comes from designing evidence to flow from systems automatically, reserving human attention for decisions, exceptions and the things automation cannot judge. She marks the open questions in red so that they are not forgotten.

### Worked example

Nadia estimates about two full-time staff of effort, finds the evidence analyst as the bottleneck and proposes automation and sampling.

> **Synthetic case.** Workload estimates are synthetic.

### Errors and limits

Hour estimates are rough. Automation can fail silently.

### Exercises

- **EX106 — Total effort.** Roughly how much effort does the programme require? *Rubric:* 3 = about two full-time staff;; 2 = two FTE;; 1 = none;; 0 = none.
- **EX107 — Bottleneck person.** Who is the bottleneck as Ardwell grows? *Rubric:* 3 = the single security analyst checking evidence;; 2 = analyst;; 1 = none;; 0 = none.
- **EX108 — Human focus.** Where should human attention go once evidence is automated? *Rubric:* 3 = decisions, exceptions and judgement tasks;; 2 = judgement;; 1 = none;; 0 = none.

### Synthesis

Scalable governance automates evidence and reserves human attention for judgement.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Security governance, risk and compliance: operations

### Learning outcomes

You will (1) run the GRC programme as an operational service; (2) manage findings and incidents through closure; (3) review operations regularly.

### 37.1 Running the service

Nadia shadows Ardwell's security manager for a month. Each week begins with a review of overdue control tasks, new findings and exceptions nearing expiry. Mid-week brings meetings with owners whose controls failed. Month-end brings evidence checks and preparation of indicators. She learns that governance is not an annual project but a continuous service with a rhythm, and that the rhythm itself is a control: when weekly reviews lapse, problems accumulate unseen. Writing the reasoning down also helps her spot a weak step in her argument.

### 37.2 Findings to closure

Every finding follows a path: recorded with severity and owner, agreed remediation plan, due date, evidence of fix and verification by someone other than the owner. Nadia tracks twenty open findings and notices that several were marked fixed without evidence. She introduces a rule that only the security analyst can close findings, after checking evidence. Closure rates dip briefly, then recover with real fixes. She learns that closure without verification produces comforting numbers but not reduced risk. Nadia discusses the trade-off with a classmate who works in finance.

### 37.3 Operational review

Each quarter, the security manager reviews the programme itself: Are tasks on time? Are findings ageing? Are exceptions growing? Which controls fail repeatedly? Nadia helps prepare the review and notes that patch failures have repeated for three quarters on substation devices. The review escalates this to a design problem rather than an owner problem, leading to a project to replace the devices. She learns that operations data reveal where design, not effort, is the real issue. The class compares answers and finds that most differences come from unstated assumptions.

### Worked example

Nadia observes the weekly rhythm, requires verified closure of findings and helps a quarterly review escalate repeated patch failures to a design problem.

> **Synthetic case.** Findings and reviews are synthetic.

### Errors and limits

Verified closure slows reporting. Reviews can become routine.

### Exercises

- **EX109 — Rhythm as control.** Why is the weekly rhythm itself a control? *Rubric:* 3 = when it lapses problems accumulate unseen;; 2 = rhythm;; 1 = none;; 0 = none.
- **EX110 — Closure rule.** Who may close findings under Nadia's rule? *Rubric:* 3 = only the security analyst after checking evidence;; 2 = analyst;; 1 = owner;; 0 = none.
- **EX111 — Repeated failures.** What did repeated substation patch failures turn out to be? *Rubric:* 3 = a design problem leading to device replacement;; 2 = design;; 1 = owner;; 0 = none.

### Synthesis

GRC operations need rhythm, verified closure and reviews that find design problems.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Security governance, risk and compliance: validation

### Learning outcomes

You will (1) distinguish verification from validation; (2) use attribute sampling to validate control operation; (3) choose sample sizes that support conclusions.

### 38.1 Verification and validation

Verification asks whether a control was built as specified; validation asks whether it achieves its purpose in real operation over time. Nadia verified the broker in the laboratory earlier. Now she must validate that the control operated effectively through a year, in the way internal auditors and service auditors examine operating effectiveness. AICPA's trust services criteria, used in SOC 2 reports, distinguish design from operating effectiveness in the same spirit, though her work is internal and not an attestation. Nadia records this point in her course notebook so that later chapters can build on it.

### 38.2 Sample sizes

Checking every vendor session is impractical, so Nadia samples session records and counts deviations, such as a session without approval. The lab computes exact upper ninety-five percent bounds. Twenty-five clean records give a bound of about eleven percent. Forty clean records give about seven percent. Forty records with one deviation give about eleven percent. Fifty-nine clean records give exactly five percent. If Ardwell's tolerable deviation rate is five percent, she needs at least fifty-nine records with no deviations. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### Lab — Exact upper bounds for session-record samples

```python
"""Exact upper 95% bound on deviation rate for attribute samples (stdlib)."""
from math import comb
def cdf(k, n, p): return sum(comb(n, i)*p**i*(1-p)**(n-i) for i in range(k+1))
def upper(k, n):
    lo, hi = 0.0, 1.0
    for _ in range(60):
        m = (lo+hi)/2
        lo, hi = (m, hi) if cdf(k, n, m) > 0.05 else (lo, m)
    return hi
for n, k in [(25, 0), (40, 0), (40, 1), (59, 0)]:
    print(f"n={n} deviations={k}: upper bound {upper(k, n):.3f}")
```

Run with `python3 lab_sample.py`. Verified output:

```text
n=25 deviations=0: upper bound 0.113
n=40 deviations=0: upper bound 0.072
n=40 deviations=1: upper bound 0.113
n=59 deviations=0: upper bound 0.050
```

### 38.3 Conclusions

Nadia samples fifty-nine sessions at random across the year and finds no deviations, so she concludes with ninety-five percent confidence that the deviation rate is at most five percent. She notes the conclusion covers approval only, not whether vendors did the right work. She also checks emergency sessions separately, because they follow a different path and could hide problems in an overall sample. Prof. Brenner reminds the class that sampling supports bounded statements, never certainty. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Nadia separates verification from validation, finds fifty-nine clean records needed for a five percent bound and validates approvals.

> **Synthetic case.** Session data are synthetic; AICPA TSC is real; this is not an attestation.

### Errors and limits

Random samples miss rare patterns. Validation covers only tested attributes.

### Exercises

- **EX112 — Validation meaning.** What does validation ask that verification does not? *Rubric:* 3 = whether the control achieves its purpose in operation over time;; 2 = operation;; 1 = none;; 0 = none.
- **EX113 — Minimum sample.** How many clean records give a 5% upper bound? *Rubric:* 3 = fifty-nine;; 2 = 59;; 1 = 25;; 0 = none.
- **EX114 — Separate stratum.** Why check emergency sessions separately? *Rubric:* 3 = they follow a different path and could hide problems;; 2 = strata;; 1 = none;; 0 = none.

### Synthesis

Validation uses sized samples to make bounded claims about controls in real operation.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Security governance, risk and compliance: maintainability

### Learning outcomes

You will (1) keep policies, controls and registers current; (2) manage framework edition changes; (3) prevent knowledge loss.

### 39.1 Keeping things current

A GRC programme decays unless maintained. Policies reference retired systems, controls describe abandoned practices and register entries describe risks that have changed. Nadia sets review dates for every document and control and links them to triggers, such as a major system change or an incident, that force earlier review. She learns that maintainability means designing governance artefacts to be easy to update: short, owned, versioned and linked to the things they describe. The same reasoning will return when Ardwell's auditors visit next year. She adds a short note to the shared course wiki for other students.

### 39.2 Framework changes

Standards change editions. ISO/IEC 27001 was revised in 2022, reorganising its reference controls into four themes, and NIST CSF moved to version 2.0 in 2024, adding the Govern function. Nadia learns that each change requires a transition plan: compare old and new requirements, update mappings, adjust controls and train staff. Keeping mappings in structured data rather than prose makes transitions much easier, because changes can be traced item by item instead of rewritten from scratch. This makes the governance consequence visible to people outside the engineering team.

### 39.3 Knowledge loss

When the security manager announces retirement, Nadia realises much of the programme lives in her head. Together they write short notes on why key decisions were made, which owners need support and where evidence lives. They pair the manager with her successor for two months. Nadia learns that governance knowledge, especially the reasons behind decisions, is easily lost, and that decision records, runbooks and overlapping handovers are maintainability controls in their own right. Nadia keeps a dated copy of her working so that the result can be traced.

### Worked example

Nadia links reviews to triggers, plans transitions for framework editions and captures knowledge before a key retirement.

> **Synthetic case.** Ardwell's documents are synthetic; edition facts for ISO/IEC 27001 and CSF are real.

### Errors and limits

Triggers are missed. Handover notes are incomplete.

### Exercises

- **EX115 — Review triggers.** What triggers early review of governance documents? *Rubric:* 3 = major system changes or incidents;; 2 = triggers;; 1 = none;; 0 = none.
- **EX116 — CSF change.** What did NIST CSF 2.0 add? *Rubric:* 3 = the Govern function;; 2 = Govern;; 1 = none;; 0 = none.
- **EX117 — Handover measure.** Which measure protects against loss of the retiring manager's knowledge? *Rubric:* 3 = decision notes and a two-month paired handover;; 2 = handover;; 1 = none;; 0 = none.

### Synthesis

Maintainable governance is short, owned, versioned and resilient to edition changes and staff turnover.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) re-verify controls after changes; (2) test GRC tooling itself; (3) report regression findings.

### 40.1 Regression testing

After Ardwell upgrades its ticketing system, Nadia re-runs the verification tests for the GRC tooling and the broker. She learns that changes can break controls in unexpected ways. The upgrade changes how recurring tasks are scheduled, so several quarterly control tasks are now due annually. Without regression tests, the change would have silently reduced control frequency for a year. She adds a check that compares scheduled frequencies with the control register after every upgrade, closing that gap. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 40.2 Testing the tooling

The GRC tooling itself must be verified. Nadia tests that evidence attachments cannot be altered after closure, that only authorised staff can close findings and that reports count tasks correctly. One report counts reopened findings twice, inflating the open count. She fixes the query and adds a test case. She learns that tools that produce governance evidence deserve the same rigour as the controls they track, since errors in the tool become errors in the board's view of risk. She checks the idea against a second example before relying on it.

### 40.3 Reporting regressions

Nadia reports both regressions with severity, cause and fix, and recommends that upgrades to GRC systems follow change management with verification before release. She also proposes keeping a small library of test cases that run after any change. Prof. Brenner notes that the laboratory work shows a key principle: verification is not a one-time event but must be repeated whenever the system changes, because the conditions that made a control work can disappear quietly. The point seems small, but it changes how owners act on the result.

### Worked example

Nadia finds a schedule regression and a double-counting report error after an upgrade and builds regression tests for both.

> **Synthetic case.** Tooling and defects are synthetic.

### Errors and limits

Regression suites age. Not every change triggers tests.

### Exercises

- **EX118 — Schedule regression.** What did the upgrade break? *Rubric:* 3 = quarterly tasks became annual;; 2 = frequency;; 1 = none;; 0 = none.
- **EX119 — Report defect.** Which reporting error did Nadia find? *Rubric:* 3 = reopened findings counted twice;; 2 = double count;; 1 = none;; 0 = none.
- **EX120 — Verification principle.** What principle does the laboratory illustrate? *Rubric:* 3 = verification must repeat whenever the system changes;; 2 = repeat;; 1 = one-time;; 0 = none.

### Synthesis

Re-verification after change protects controls and the tools that report on them.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Security governance, risk and compliance: system optimization

### Learning outcomes

You will (1) choose control investments under a budget; (2) compare optimal and intuitive choices; (3) recognise the limits of optimisation.

### 41.1 The budget problem

Ardwell's board approves two hundred thousand for new security controls next year. Nadia lists six options with costs and estimated reductions in expected annual loss: multi-factor authentication for remote access, offline backups, a vendor access broker extension, card tokenisation, an awareness refresh and log monitoring. Total costs exceed the budget, so choices must be made. She frames this as an optimisation problem: maximise total estimated loss reduction while keeping cost within the budget. Ardwell's security manager later asks for a copy of this analysis.

### 41.2 Finding the best set

With only six options, the lab checks every combination. The best set within budget costs one hundred and ninety thousand and reduces estimated loss by six hundred and thirty thousand: multi-factor authentication, offline backups and card tokenisation. Nadia compares this with an intuitive choice that management had suggested, the broker extension and log monitoring, which uses most of the budget for a much smaller reduction. Exhaustive search shows clearly how much value intuition can leave behind. She marks the open questions in red so that they are not forgotten.

### Lab — Best control set within a budget

```python
"""Choose controls under a budget to maximise expected loss reduction (exhaustive search)."""
from itertools import combinations
opts = [("MFA for remote access", 40, 150), ("offline backups", 60, 220), ("vendor access broker", 80, 190),
        ("card tokenisation", 90, 260), ("awareness refresh", 20, 40), ("log monitoring", 70, 120)]
B = 200; best = (0, 0, ())
for r in range(len(opts)+1):
    for s in combinations(opts, r):
        c = sum(o[1] for o in s); g = sum(o[2] for o in s)
        if c <= B and g > best[0]: best = (g, c, s)
print(f"budget {B}k; best reduction {best[0]}k at cost {best[1]}k")
for o in best[2]: print(" -", o[0])
```

Run with `python3 lab_budget.py`. Verified output:

```text
budget 200k; best reduction 630k at cost 190k
 - MFA for remote access
 - offline backups
 - card tokenisation
```

### 41.3 Limits

Nadia reports the result with caveats. Reduction estimates come from workshops and are uncertain. Options may interact; backups and tokenisation address different risks, but other pairs might overlap. Some benefits, such as better evidence for audits, are not captured. Gordon and Loeb (2002) remind her that the value of investment depends on vulnerability and potential loss, not cost alone. She recommends using the optimal set as a starting point for discussion, with sensitivity checks on the most uncertain estimates. Writing the reasoning down also helps her spot a weak step in her argument.

### Worked example

Nadia finds the best set within two hundred thousand, saving six hundred and thirty thousand at a cost of one hundred and ninety thousand, and states its limits.

> **Synthetic case.** Costs and reductions are synthetic; Gordon and Loeb (2002) is real.

### Errors and limits

Estimates are uncertain. Interactions between controls are ignored.

### Exercises

- **EX121 — Best set.** Which controls form the best set? *Rubric:* 3 = MFA, offline backups and card tokenisation;; 2 = three;; 1 = broker;; 0 = none.
- **EX122 — Best cost.** At what cost does the best set deliver its 630k reduction? *Rubric:* 3 = 190k;; 2 = 190;; 1 = 200;; 0 = none.
- **EX123 — Investment value.** According to Gordon and Loeb, what drives the value of security investment? *Rubric:* 3 = vulnerability and potential loss;; 2 = not cost alone;; 1 = none;; 0 = none.

### Synthesis

Optimisation reveals better choices than intuition but must be read with its uncertainties.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Security governance, risk and compliance: applied research

### Learning outcomes

You will (1) frame an applied research question in GRC; (2) choose a method suited to an operating organisation; (3) review evidence critically.

### 42.1 An applied question

Nadia chooses an applied research question for her final year: does Ardwell's new practice of reporting expected loss ranges to the board change the decisions it makes compared with the old heat map? She narrows it to measurable terms: the number of risk treatment decisions per quarter, the time from proposal to decision and whether decisions follow the largest residual risks. She records that the study can describe changes but cannot fully separate the effect of reporting from other changes. Nadia records this point in her course notebook so that later chapters can build on it.

### 42.2 Method

She uses a before-and-after comparison of board minutes for four quarters before and four after the change, coding each decision with a codebook she pilots with a classmate. She also interviews two directors. Wohlin and colleagues (2012) describe threats to validity that she adapts: changes in board membership, a major incident that might prompt action and her own bias as someone who helped design the new pack. She records how each could affect results. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 42.3 Critical reading

Nadia reviews published evidence. Hubbard and Seiersen (2016) argue for quantitative methods, while Cox (2008) analyses weaknesses of risk matrices. Spears and Barki (2010) show that involving business users improves security risk management. She notes most sources are analytical or based on other settings, and few measure board decisions directly. Her study can add a small, honest piece of evidence from one cooperative, provided she reports its limits and avoids treating it as general proof. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Nadia frames a before-and-after study of board decisions, lists validity threats including her own bias and positions it against published evidence.

> **Synthetic case.** The study is synthetic; cited works are real.

### Errors and limits

Before-after designs confound timing. Minutes are incomplete records.

### Exercises

- **EX124 — Measured outcomes.** Which outcomes does Nadia measure? *Rubric:* 3 = decisions per quarter, time to decision and alignment with largest risks;; 2 = three;; 1 = none;; 0 = none.
- **EX125 — Own bias.** Why is Nadia's own role a validity threat? *Rubric:* 3 = she helped design the new pack;; 2 = bias;; 1 = none;; 0 = none.
- **EX126 — Evidence gap.** What is missing from the published evidence? *Rubric:* 3 = direct measurement of board decisions;; 2 = gap;; 1 = none;; 0 = none.

### Synthesis

Applied GRC research needs measurable questions, explicit validity threats and modest claims.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a real governance function; (2) observe audits and regulator interactions; (3) reflect on practice versus theory.

### 43.1 Placement

Nadia spends a semester on placement in Ardwell's governance team. She supports preparation for the cooperative's first certification audit against ISO/IEC 27001:2022, helping owners assemble evidence and checking the statement of applicability against actual practice. She finds that some controls work well but are poorly documented, while others are documented well but rarely performed. She learns that audits test the link between documents and practice, and that the link is often weaker than managers think. The same reasoning will return when Ardwell's auditors visit next year.

### 43.2 Audit and regulator

She observes the stage one audit, in which the certification body reviews documentation and readiness. Auditors ask how risk acceptance decisions are made and who approves them. Ardwell's answer is clear because of the earlier work on decision records. Later, she sits in on a meeting with the energy regulator about incident reporting expectations. She notes how regulators focus on outcomes such as restoration times and communication, while certification focuses on management system processes. She adds a short note to the shared course wiki for other students.

### 43.3 Reflection

Nadia writes a reflection comparing practice with her coursework. Theory presented controls as neatly designed and tested; practice involved negotiation, competing deadlines and incomplete data. Yet the theory helped: data models, testable requirements and sampling gave her tools to bring order to messy situations. She also learns the value of relationships, since owners cooperated more readily once they understood the reasons behind requests. Prof. Brenner notes that reflective practice turns experience into transferable knowledge. This makes the governance consequence visible to people outside the engineering team.

### Worked example

Nadia supports certification readiness, observes stage one audit and regulator meetings and reflects on theory versus practice.

> **Synthetic case.** The placement, audit and meetings are synthetic; ISO/IEC 27001:2022 is real.

### Errors and limits

One placement is one context. Observations can be selective.

### Exercises

- **EX127 — Document gap.** What gap did Nadia find between documents and practice? *Rubric:* 3 = some controls work but are undocumented, others documented but rarely done;; 2 = mismatch;; 1 = none;; 0 = none.
- **EX128 — Stage one focus.** What did auditors ask about in stage one? *Rubric:* 3 = how risk acceptance decisions are made and approved;; 2 = acceptance;; 1 = none;; 0 = none.
- **EX129 — Regulator focus.** How did the regulator's focus differ from certification? *Rubric:* 3 = outcomes like restoration and communication versus processes;; 2 = outcomes;; 1 = none;; 0 = none.

### Synthesis

Placement shows how theory helps bring order to messy practice and how relationships enable governance.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) scope a capstone governance engineering project; (2) define success criteria with a client; (3) plan risk and quality for the project itself.

### 44.1 Scoping

For her capstone, Nadia works with Ardwell's new security manager on a continuous control monitoring service: automated collection of evidence for twenty high-value controls, with alerts when a control fails and a dashboard for owners. The scope excludes controls requiring human judgement. She writes a scope statement, lists stakeholders and agrees on constraints: only the standard library and existing systems, no access to production data beyond what owners already share and delivery within two terms. Nadia keeps a dated copy of her working so that the result can be traced.

### 44.2 Success criteria

With the client, Nadia defines success criteria: evidence for at least eighteen of twenty controls collected automatically; alerts within one day of a control failure in tests; owners spending less time on evidence than before, measured by a short survey; and no false closure of findings. Each criterion has a measurement method. She learns that agreeing criteria early prevents disputes later and keeps the project focused on outcomes the client values rather than features that are merely interesting. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 44.3 Project risk

Nadia applies risk management to her own project. Risks include data access delays, changes in systems during the project, her own limited time and the chance that owners ignore alerts. For each she records a response: early access requests, interface checks, a schedule buffer and involving owners in alert design. She learns that a GRC engineer who does not manage the risks of her own project undermines her credibility, and that the habits she teaches others apply to her work too. She checks the idea against a second example before relying on it.

### Worked example

Nadia scopes a continuous monitoring service for twenty controls, agrees four measurable success criteria and manages her own project risks.

> **Synthetic case.** The capstone is synthetic.

### Errors and limits

Scopes creep. Surveys measure perception, not time.

### Exercises

- **EX130 — Excluded controls.** Which controls are excluded from scope? *Rubric:* 3 = those requiring human judgement;; 2 = judgement;; 1 = none;; 0 = none.
- **EX131 — Coverage criterion.** What is the evidence coverage success criterion? *Rubric:* 3 = at least eighteen of twenty controls automated;; 2 = 18/20;; 1 = none;; 0 = none.
- **EX132 — Alert risk.** How does Nadia respond to the risk that owners ignore alerts? *Rubric:* 3 = involve owners in alert design;; 2 = involvement;; 1 = none;; 0 = none.

### Synthesis

A capstone starts with clear scope, measurable success criteria and managed project risk.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) respond to reviewers' concerns; (3) record review outcomes.

### 45.1 Preparing

Before building, Nadia submits her monitoring design for independent review by an engineer from another utility and Ardwell's internal auditor. She prepares a short design document: purpose, scope, architecture, data flows, controls covered, failure modes and how evidence integrity is protected. She includes her assumptions explicitly, such as that source systems report accurate timestamps. Independent review works best when reviewers can see what the designer assumed, because hidden assumptions are where reviewers add most value. The point seems small, but it changes how owners act on the result.

### 45.2 Concerns raised

The auditor asks whether automated evidence could be manipulated by the people whose controls it monitors. The engineer asks what happens when a source system is unavailable: is a missing report treated as a pass or a failure? Nadia realises her design treated silence as success. She changes it so missing evidence raises an alert and counts as a failed collection. She also adds hashing of evidence files and storage in a location the monitored teams cannot alter. Ardwell's security manager later asks for a copy of this analysis.

### 45.3 Recording outcomes

Nadia records each concern, her response and whether reviewers accepted it. Two minor concerns about dashboard wording are deferred to a later release with reasons. The record goes into the project archive and later into her evidence dossier. She learns that review records show auditors and examiners not only the final design but how it improved, and that a design able to absorb criticism is stronger than one that never faced any. She marks the open questions in red so that they are not forgotten.

### Worked example

Nadia prepares a review pack with assumptions, fixes silence-as-success and evidence integrity issues and records outcomes.

> **Synthetic case.** Reviewers and design are synthetic.

### Errors and limits

Reviewers have limited time. Deferred items can be forgotten.

### Exercises

- **EX133 — Assumption example.** Which assumption did Nadia state explicitly? *Rubric:* 3 = source systems report accurate timestamps;; 2 = timestamps;; 1 = none;; 0 = none.
- **EX134 — Silence fix.** How was the silence-as-success flaw fixed? *Rubric:* 3 = missing evidence raises an alert and counts as a failed collection;; 2 = fail closed;; 1 = pass;; 0 = none.
- **EX135 — Integrity measures.** What protects evidence from manipulation? *Rubric:* 3 = hashing and storage the monitored teams cannot alter;; 2 = hashing;; 1 = none;; 0 = none.

### Synthesis

Independent review exposes hidden assumptions and strengthens designs when outcomes are recorded.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) build and deploy the monitoring service; (2) measure it against success criteria; (3) hand it over for operation.

### 46.1 Building

Nadia builds the service in stages, starting with the five controls whose evidence is easiest to collect. Each collector is a small script with tests, logging and a clear owner. The scheduler runs collectors daily, stores hashed evidence and raises alerts for failures or missing data. She deploys to a test environment first, then to production with the security manager's approval through change management. She keeps a log of every decision and problem for her thesis. Writing the reasoning down also helps her spot a weak step in her argument.

### 46.2 Measuring

After two months, Nadia measures against the criteria. Nineteen of twenty controls have automated evidence; one depends on a vendor system without an export, so it remains manual. In tests, alerts arrive within a few hours of a simulated failure. The owner survey shows most owners spending less time on evidence, though two find alerts too frequent. No findings were closed falsely. She reports the results honestly, including the manual control and the alert complaints. Nadia discusses the trade-off with a classmate who works in finance.

### 46.3 Handover

Nadia hands the service to Ardwell's operations team with a runbook, an owner for each collector, test cases and a list of known issues. She trains two staff to add new collectors. She tunes alert thresholds with the two unhappy owners before leaving. She learns that a capstone is only successful if the client can run it without her, and that handover documentation is as much a deliverable as the code itself. The class compares answers and finds that most differences come from unstated assumptions.

### Worked example

Nadia builds the service in stages, meets three criteria fully and one partly with nineteen of twenty controls automated, and hands it over with a runbook.

> **Synthetic case.** The service and measurements are synthetic.

### Errors and limits

Two months is short. Survey responses are self-reported.

### Exercises

- **EX136 — Coverage result.** How many controls had automated evidence? *Rubric:* 3 = nineteen of twenty;; 2 = 19;; 1 = 20;; 0 = none.
- **EX137 — Manual control.** Why did one control remain manual? *Rubric:* 3 = its vendor system has no export;; 2 = no export;; 1 = none;; 0 = none.
- **EX138 — Handover items.** Which items did Nadia hand over? *Rubric:* 3 = runbook, collector owners, test cases and known issues;; 2 = handover;; 1 = none;; 0 = none.

### Synthesis

A capstone succeeds when measured honestly against criteria and handed over so others can run it.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) design a failure trial for a GRC service; (2) observe detection and recovery; (3) improve the service from the results.

### 47.1 Designing the trial

With the security manager, Nadia plans a trial of how the monitoring service behaves under failure. Three failures are injected in a controlled window, with owners informed in advance: a collector script crashes, a source system becomes unavailable and an evidence file is altered after storage. The trial tests whether each failure is detected, how quickly and whether recovery restores correct evidence. The rules exclude any action on production control systems or customer data. Nadia records this point in her course notebook so that later chapters can build on it.

### 47.2 Observations

The crashed collector is detected at the next scheduled run and alerts the owner within a day. The unavailable source raises a missing-evidence alert as designed. The altered file is detected by a hash mismatch at the weekly integrity check, but not sooner. Recovery from the crash takes two hours because the runbook omits one step. Nadia records each observation with timestamps and compares it with expectations, noting that detection of tampering is slower than the team assumed. Prof. Brenner asks her to explain the idea aloud to a classmate before moving on.

### 47.3 Improvements

The team adds the missing runbook step and moves integrity checks from weekly to daily. They also add an alert when integrity checks themselves fail to run. Nadia notes that the trial revealed weaknesses that would have remained hidden in normal operation. She learns that planned failure trials are the governance equivalent of fire drills: they prove whether detection and recovery work, and they are only safe and useful when carefully scoped and announced. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Nadia runs three announced failure injections, finds slow tamper detection and a runbook gap and fixes both.

> **Synthetic case.** The trial is synthetic and excluded production control systems.

### Errors and limits

Announced trials differ from real failures. Daily checks add load.

### Exercises

- **EX139 — Injected failures.** Which three failures were injected? *Rubric:* 3 = collector crash, source unavailable, altered evidence file;; 2 = three;; 1 = none;; 0 = none.
- **EX140 — Slow detection.** Which failure was detected slowly? *Rubric:* 3 = the altered evidence file, at the weekly check;; 2 = tampering;; 1 = none;; 0 = none.
- **EX141 — Check change.** How often do integrity checks run after the trial? *Rubric:* 3 = daily;; 2 = daily;; 1 = weekly;; 0 = none.

### Synthesis

Announced failure trials prove detection and recovery and reveal hidden weaknesses.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble an evidence dossier for a governance programme; (2) protect it with a digest manifest; (3) detect and explain changes.

### 48.1 Assembling

For her thesis and for Ardwell's auditors, Nadia assembles an evidence dossier: the risk register extract, quarterly control test results, the statement of applicability and board minutes approving risk appetite. Each item has a source, date and owner. She writes a short index explaining what each item proves and how it links to requirements. She learns that a dossier is an argument, not a pile of files: it should let a reader follow the claim that controls work back to evidence. The same reasoning will return when Ardwell's auditors visit next year.

### 48.2 Manifest and mismatch

Nadia computes a digest for each file and stores the manifest separately. Weeks later, she rechecks. Three files match, but the control test results do not: the lab shows a mismatch for that file. Investigation reveals that a test owner had edited the file to change forty-five passed tests to forty-seven after rerunning two tests. The change might be legitimate, but editing evidence in place destroys the record of the original result. She adds a short note to the shared course wiki for other students.

### Lab — Detecting a changed evidence file

```python
"""Evidence dossier manifest: detect a changed file by SHA-256 (synthetic contents)."""
import hashlib
files = {"risk_register.csv": "R01,IT ops,12\nR02,Finance,8\n", "control_tests.csv": "access,48,45\n",
         "soa.md": "Statement of applicability v3\n", "board_minutes.md": "Risk appetite approved\n"}
man = {f: hashlib.sha256(c.encode()).hexdigest()[:12] for f, c in files.items()}
files["control_tests.csv"] = "access,48,47\n"
for f in sorted(files):
    now = hashlib.sha256(files[f].encode()).hexdigest()[:12]
    print(f, man[f], "OK" if now == man[f] else "MISMATCH")
```

Run with `python3 lab_dossier.py`. Verified output:

```text
board_minutes.md a112873ae77e OK
control_tests.csv 33fdcc0a788f MISMATCH
risk_register.csv 5e0ebfd61225 OK
soa.md ac050567962d OK
```

### 48.3 Handling changes

Nadia restores the original file from the archive and asks the owner to file the retest as new evidence with its own date, so both results remain visible. She updates the procedure to forbid editing filed evidence. She notes that digests detect change but cannot say whether a change was honest. Prof. Brenner explains that integrity of evidence underpins every assurance claim, and that mature programmes treat evidence as append-only, recording corrections as new entries. This makes the governance consequence visible to people outside the engineering team.

### Worked example

Nadia builds an indexed dossier, detects a changed test file through its digest and restores append-only handling.

> **Synthetic case.** Dossier contents are synthetic.

### Errors and limits

Digests prove change, not intent. Manifests must be protected too.

### Exercises

- **EX142 — Dossier as argument.** Why is a dossier an argument rather than a pile of files? *Rubric:* 3 = it lets readers trace claims back to evidence;; 2 = traceability;; 1 = none;; 0 = none.
- **EX143 — Mismatch file.** Which file showed a mismatch? *Rubric:* 3 = control_tests.csv;; 2 = test results;; 1 = none;; 0 = none.
- **EX144 — Correct handling.** How should a retest be recorded? *Rubric:* 3 = as new evidence with its own date;; 2 = append;; 1 = edit in place;; 0 = none.

### Synthesis

Evidence dossiers need indexes, digest manifests and append-only handling.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis on a GRC system; (2) combine design, measurement and research; (3) state contributions and limits.

### 49.1 Structure

Nadia's thesis combines her capstone and applied research. Chapters cover the problem, background and standards, requirements, design and reviews, implementation, verification and failure trials, measurement against criteria, the board-reporting study and conclusions. Each chapter links to dossier evidence. She keeps the main text focused on decisions and results, moving code and detailed test records to appendices. She writes for engineers who might build a similar service and for examiners judging her reasoning. Nadia keeps a dated copy of her working so that the result can be traced.

### 49.2 Findings

The thesis reports that automated evidence covered nineteen of twenty controls, alerts arrived within hours, owners reported less evidence effort and a failure trial revealed slow tamper detection that was fixed. The board study found more treatment decisions per quarter after ranges replaced the heat map, but a major incident during the period also prompted action, so she cannot separate the effects. She states both findings plainly, with the uncertainty attached to each. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 49.3 Contributions and limits

Nadia claims three contributions: a tested design for low-cost continuous control monitoring, evidence that failure trials reveal hidden weaknesses in GRC tooling and a small observational study of board reporting. Limits include one organisation, a short operating period, self-reported effort and a confounded before-and-after comparison. She recommends future work across several utilities. Prof. Brenner notes that stating limits clearly makes contributions more credible, not less. She checks the idea against a second example before relying on it. The point seems small, but it changes how owners act on the result.

### Worked example

Nadia structures her thesis around decisions and results, reports findings with uncertainty and states three contributions with limits.

> **Synthetic case.** The thesis is synthetic.

### Errors and limits

One-organisation studies limit generality. Confounding remains.

### Exercises

- **EX145 — Board finding.** What did the board study find and why is it uncertain? *Rubric:* 3 = more decisions, but a major incident also prompted action;; 2 = confounded;; 1 = none;; 0 = none.
- **EX146 — Contribution list.** Name one of Nadia's three contributions. *Rubric:* 3 = tested low-cost continuous monitoring design;; 2 = contribution;; 1 = none;; 0 = none.
- **EX147 — Thesis limits.** List two limits of the thesis. *Rubric:* 3 = one organisation and short operating period;; 2 = limits;; 1 = none;; 0 = none.

### Synthesis

An engineering thesis links design, measurement and research with clearly stated limits.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend an engineering thesis in GRC; (2) answer questions on design, evidence and ethics; (3) reflect on professional development.

### 50.1 Presentation

Nadia presents her thesis in twenty minutes: the problem at Ardwell, the design, how reviews and trials improved it, results against criteria and the board study with its limits. She shows a short demonstration of an alert for a failed control and of the integrity check detecting a changed file. She closes with lessons for other organisations. Examiners include Prof. Brenner, an external engineer from a utility and an internal auditor from another sector. Ardwell's security manager later asks for a copy of this analysis.

### 50.2 Questions

The external engineer asks whether automation might make owners complacent. Nadia answers that the service collects evidence but owners still review exceptions, and that sampling by the analyst continues. The auditor asks whether the evidence would satisfy an external audit. She answers that it supports one but does not replace the auditor's own testing. Prof. Brenner asks about ethics. She explains how she handled access to staff data and why the failure trial was announced and excluded production control systems. She marks the open questions in red so that they are not forgotten.

### 50.3 Reflection

The examiners pass the thesis and praise the honest treatment of the board study. In her reflection, Nadia notes that the course taught her to see governance as engineering: requirements, design, verification, operation and improvement. She also learned that governance depends on people, trust and clear communication. She plans to join Ardwell's governance team and to keep her habits of testing assumptions, recording decisions and reporting uncertainty honestly in every role she takes on. Writing the reasoning down also helps her spot a weak step in her argument.

### Worked example

Nadia presents and demonstrates her service, answers on complacency, audit reliance and ethics and passes her defense.

> **Synthetic case.** The defense is synthetic.

### Errors and limits

Defenses sample knowledge. Reflections can be idealised.

### Exercises

- **EX148 — Complacency answer.** How did Nadia answer the concern about owner complacency? *Rubric:* 3 = owners still review exceptions and the analyst samples;; 2 = oversight;; 1 = none;; 0 = none.
- **EX149 — Audit reliance.** Does the service replace external audit testing? *Rubric:* 3 = no, it supports but does not replace it;; 2 = no;; 1 = yes;; 0 = none.
- **EX150 — Career plan.** What does Nadia plan after graduating? *Rubric:* 3 = join Ardwell's governance team;; 2 = Ardwell;; 1 = none;; 0 = none.

### Synthesis

The defense confirms that governance engineering joins technical rigour with honest communication.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Nadia Okafor, Prof. Tomas Brenner, Kestrel Polytechnic, Ardwell Power Cooperative and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Whether the backlog of open findings is shrinking, holding steady or growing.

**EX002.** Because management attention fades there and the hardest findings linger.

**EX003.** As the area under the curve of open weaknesses over time.

**EX004.** Mandatory multi-factor authentication for remote sessions and immediate vendor access during emergencies.

**EX005.** Seven, belonging to staff who had moved roles.

**EX006.** Create supplier together with approve payment (or approve payment with reconcile bank).

**EX007.** Physical controls, alongside organisational, people and technological ones.

**EX008.** Facilities, working with IT.

**EX009.** Because locks only delay, and detection is needed against a determined attacker.

**EX010.** Title, owner, approval date and next review date.

**EX011.** Because an owner can fix a named policy but cannot act on an unexplained number.

**EX012.** Because when scripts produce compliance evidence, the script itself is evidence that auditors must understand.

**EX013.** Decisions, options and consequences in plain language.

**EX014.** To say expected annual loss is about ninety thousand under stated assumptions, with a wide range.

**EX015.** Because governance decisions affect many teams and the memo records how the decision was made.

**EX016.** Staff changing roles without their access being updated.

**EX017.** Departments with high staff turnover, where decay is faster.

**EX018.** Because money has a time value, so future amounts are discounted.

**EX019.** The annual rate of occurrence multiplied by the single loss expectancy.

**EX020.** Ransomware at 90,000 and vendor access misuse at 80,000.

**EX021.** Because it is rare but a single occurrence could be catastrophic, which an average hides.

**EX022.** Control-system devices at substations, along with their firmware.

**EX023.** Because it runs first and can bypass operating system controls.

**EX024.** Replace them, isolate them, or accept the risk with compensating monitoring.

**EX025.** One to read data, one to apply rules and one to write reports.

**EX026.** Because a skipped row could hide a risk that nobody owns.

**EX027.** The run date, the script version and a summary of the input file.

**EX028.** Taking responsibility for its accuracy.

**EX029.** Monitoring and alerting on repeated failures, with physical restriction of control room access.

**EX030.** Because punishing bad news drives problems out of sight until they cause harm.

**EX031.** Corporate office, customer payment, control-system and vendor remote access zones.

**EX032.** Because it bypassed the jump host, so sessions lacked logging and approval.

**EX033.** After changes, because a single new firewall rule can connect zones.

**EX034.** That the operating system enforces separate administrator accounts and logs their use where users cannot alter the logs.

**EX035.** Each deviation is recorded with its reason.

**EX036.** How quickly drift is detected and corrected.

**EX037.** Every risk has an owner, reviews are no older than 180 days and scores lie between 1 and 25.

**EX038.** Two.

**EX039.** Careless or falsified edits could make risks look smaller without anyone noticing.

**EX040.** ISO/IEC 27002:2022 and PCI DSS v4.0.

**EX041.** A documented emergency path with review after the fact within two working days.

**EX042.** Because each is a supplier whose vulnerabilities and licence obligations become Ardwell's risk.

**EX043.** Integrity, because readings drive bills.

**EX044.** A shared vendor password.

**EX045.** A tested procedure to revoke vendor access during an incident.

**EX046.** To keep risk within the board's appetite and demonstrate compliance.

**EX047.** Requirements with no control and controls with no test.

**EX048.** Retirement.

**EX049.** The board's risk appetite.

**EX050.** It swung much further from target because of the longer delay.

**EX051.** Proportionate responses guided by documented decision rules.

**EX052.** For example, minimise the scope of sensitive data and broker all external access through monitored points.

**EX053.** It stored customer names with readings in a service reachable from office laptops, widening sensitive data scope.

**EX054.** The context, the decision, the alternatives considered and the consequences including accepted risks.

**EX055.** Movers, because old access is rarely removed.

**EX056.** Customer payment data and personal data on laptops.

**EX057.** Because it had no backup or expiry tracking and could expire unnoticed, breaking the portal.

**EX058.** Direction, accountability and oversight, including risk appetite.

**EX059.** Because it creates a conflict of interest and weakens assurance.

**EX060.** No; it is a voluntary choice by the board, unlike contractual PCI DSS obligations.

**EX061.** A recovery requirement for control-system backups and spare equipment.

**EX062.** An owner, a frequency, a measurable condition and evidence.

**EX063.** Those tied to supply safety and contractual card obligations.

**EX064.** For example assets, risks, controls and obligations (also tests, findings and owners).

**EX065.** Because one control satisfies several obligations and treats several risks.

**EX066.** For example, which risks are treated only by controls that failed their last test.

**EX067.** A threat source, an event, the vulnerabilities exploited and the impact.

**EX068.** Approved removals that were never actually carried out.

**EX069.** Because the control it depends on may have stopped working without anyone noticing.

**EX070.** Residual risk is what remains after controls; inherent risk is before them.

**EX071.** By 76%, from 90 thousand to 21.6 thousand.

**EX072.** Vendor misuse at 80 thousand, because no control treats it.

**EX073.** Vendors connected within minutes during outages.

**EX074.** Four hours.

**EX075.** By sampling ten percent of recordings each month, focusing on emergency sessions.

**EX076.** Improved spreadsheets, a commercial platform and tooling built on the ticketing system.

**EX077.** Data integrity with audit trail, and effort for control owners.

**EX078.** The commercial platform.

**EX079.** So it stays linked to the risk it is meant to reduce rather than becoming a ritual.

**EX080.** The statement of applicability.

**EX081.** By confirming that an independent tester could verify the control from the description alone.

**EX082.** Moving the two highest-risk vendors to the broker.

**EX083.** By allowing pre-approved maintenance windows.

**EX084.** Supervised sessions with an Ardwell engineer present.

**EX085.** Activity, performance and outcome measures.

**EX086.** Patching at 78% and change management at 72%.

**EX087.** Because it hides two control families below the red threshold.

**EX088.** So production systems are not disturbed by testing.

**EX089.** The date, tester, steps, result and supporting artefacts.

**EX090.** A session approved for one device could reach a second device on the same segment.

**EX091.** Twelve controls with no clear owner and three describing practices that no longer exist.

**EX092.** After five days overdue.

**EX093.** So they are renewed with fresh reasoning rather than becoming hidden permanent gaps.

**EX094.** 0.50%.

**EX095.** 2.49%, about five times higher.

**EX096.** Removing the shared dependency, such as one administrator controlling both layers.

**EX097.** Keeping power flowing and restoring services quickly after incidents.

**EX098.** Nine hours against an eight-hour target.

**EX099.** Because they reveal gaps that can be recorded and closed.

**EX100.** Compare cyber risk with other enterprise risks on equal terms.

**EX101.** As an operational disruption risk with a financial impact range and a regulatory reporting obligation.

**EX102.** When it means one team taking over another's work instead of defining interfaces.

**EX103.** Whether risk is rising or falling, and what the board must decide.

**EX104.** Because Cox (2008) shows risk matrices can mislead.

**EX105.** By adding labelled arrows with words.

**EX106.** Close to two full-time staff, spread across many people.

**EX107.** The single security analyst who checks evidence.

**EX108.** To decisions, exceptions and tasks requiring judgement.

**EX109.** Because when weekly reviews lapse, problems accumulate unseen.

**EX110.** Only the security analyst, after checking evidence.

**EX111.** A design problem, leading to a project to replace the devices.

**EX112.** Whether the control achieves its purpose in real operation over time.

**EX113.** Fifty-nine.

**EX114.** Because they follow a different path and problems there could be hidden in an overall sample.

**EX115.** Major system changes or incidents.

**EX116.** The Govern function.

**EX117.** Written notes on decisions and a two-month overlapping handover with her successor.

**EX118.** Several quarterly control tasks were rescheduled as annual.

**EX119.** A report counted reopened findings twice, inflating the open count.

**EX120.** That verification must be repeated whenever the system changes.

**EX121.** Multi-factor authentication for remote access, offline backups and card tokenisation.

**EX122.** 190 thousand.

**EX123.** Vulnerability and potential loss, not cost alone.

**EX124.** Treatment decisions per quarter, time from proposal to decision and whether decisions follow the largest residual risks.

**EX125.** Because she helped design the new board pack and may favour it.

**EX126.** Direct measurement of how reporting affects board decisions.

**EX127.** Some controls worked but were poorly documented, while others were documented but rarely performed.

**EX128.** How risk acceptance decisions are made and who approves them.

**EX129.** The regulator focused on outcomes such as restoration times and communication, while certification focused on management system processes.

**EX130.** Controls requiring human judgement.

**EX131.** Automated evidence for at least eighteen of twenty controls.

**EX132.** By involving owners in designing the alerts.

**EX133.** That source systems report accurate timestamps.

**EX134.** Missing evidence now raises an alert and counts as a failed collection.

**EX135.** Hashing evidence files and storing them where monitored teams cannot alter them.

**EX136.** Nineteen of twenty.

**EX137.** Because it depends on a vendor system with no export.

**EX138.** A runbook, an owner for each collector, test cases and a list of known issues.

**EX139.** A collector crash, an unavailable source system and an altered evidence file.

**EX140.** The altered evidence file, detected only at the weekly integrity check.

**EX141.** Daily.

**EX142.** Because it lets a reader follow the claim that controls work back to evidence.

**EX143.** The control test results file, control_tests.csv.

**EX144.** As new evidence with its own date, keeping the original result.

**EX145.** More treatment decisions per quarter, but a major incident in the period may explain the change.

**EX146.** For example, a tested design for low-cost continuous control monitoring.

**EX147.** For example, one organisation and a short operating period (also self-reported effort and confounding).

**EX148.** Owners still review exceptions and the analyst continues sampling.

**EX149.** No; it supports an external audit but does not replace the auditor's own testing.

**EX150.** To join Ardwell's governance team.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Cox, L. A., Jr. (2008). What's wrong with risk matrices? *Risk Analysis*, 28(2), 497–512. <https://doi.org/10.1111/j.1539-6924.2008.01030.x>
- Freund, J., & Jones, J. (2015). *Measuring and managing information risk: A FAIR approach*. Butterworth-Heinemann. <https://doi.org/10.1016/C2013-0-09966-5>
- Gordon, L. A., & Loeb, M. P. (2002). The economics of information security investment. *ACM Transactions on Information and System Security*, 5(4), 438–457. <https://doi.org/10.1145/581271.581274>
- Hubbard, D. W., & Seiersen, R. (2016). *How to measure anything in cybersecurity risk*. Wiley. <https://doi.org/10.1002/9781119162315>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022b). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- International Organization for Standardization. (2022c). *ISO/IEC 27005:2022 Information security, cybersecurity and privacy protection — Guidance on managing information security risks*. <https://www.iso.org/standard/80585.html>
- ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. ISACA. <https://www.isaca.org/resources/cobit>
- Joint Task Force. (2018). *Risk management framework for information systems and organizations: A system life cycle approach for security and privacy* (NIST SP 800-37 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-37r2>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
- Spears, J. L., & Barki, H. (2010). User participation in information systems security risk management. *MIS Quarterly*, 34(3), 503–522. <https://doi.org/10.2307/25750689>
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
