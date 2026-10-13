# Data Governance: Engineering Course

- Language: English (`en`); course 118, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students learning to build, verify and operate data governance for utility meter and sensor data.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs trace upstream lineage and ownership gaps in a synthetic pipeline graph, compute pass rates for three meter reading rules, measure feed timeliness against a 06:00 service level and reconcile synthetic field reads with billing. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one engineering student from mathematics, measurement, programming and systems foundations through governance requirements, models, controls, implementation, verification, operations and validation to a capstone, a recovery trial, an evidence dossier, a thesis and a final defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Kofi Mensah** | Engineering student | Invented |
| **Prof. Elena Varga** | Supervisor | Invented |
| **Northfield Polytechnic** | Fictional polytechnic | Invented |
| **Tidewater Water** | Fictional utility, about 400,000 customers and 90,000 smart meters | Invented |

### Core sources

DAMA-DMBOK2 (2017); ISO/IEC 38505-1:2017; ISO 8000-8:2015; Khatri and Brown (2010), [doi:10.1145/1629175.1629210](https://doi.org/10.1145/1629175.1629210); Wang and Strong (1996); Batini et al. (2009); NIST SP 800-188; NIST SP 800-30r1. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) use rates of change to describe data flows; (2) relate derivatives to monitoring of data volumes; (3) read a growth curve for storage planning.

### 1.1 The student and the utility

Kofi Mensah begins a five-year engineering course at the fictional Northfield Polytechnic, supervised by Prof. Elena Varga. His placement partner is the fictional Tidewater Water, which supplies about 400,000 customers, reads 90,000 smart meters every hour and monitors its pipe network with flow sensors. Data governance at Tidewater means deciding who owns meter, sensor and customer data, what quality rules apply and how long records are kept. Prof. Varga explains that every mathematics course will be connected to those decisions through Tidewater's data. Readings arrive continuously.

### 1.2 Rates of change

Calculus begins with rates of change. If the volume of stored meter readings is a function of time, its derivative tells Tidewater how fast storage grows. Kofi models stored readings as hourly reads multiplied by meters and hours elapsed, giving a constant rate of about 2.16 million readings per day. When Tidewater adds 10,000 meters each quarter, the rate itself increases, and the second derivative becomes positive. He learns that a governance plan for retention must use the rate, not just the current total.

### 1.3 Monitoring with derivatives

Kofi applies the idea to monitoring. A sudden drop in the rate of incoming readings, which is a large negative change in the derivative, may mean that a data feed has failed rather than that customers stopped using water. Tidewater's data team currently watches only daily totals, which hide hour-by-hour problems. Kofi proposes computing the hourly rate and flagging changes larger than a set fraction. He notes that this mathematical view becomes a governance control, because a missing feed affects billing and leakage reports downstream.

### 1.4 Planning storage

Using an integral, Kofi estimates total storage over seven years, the period Tidewater's retention schedule sets for billing evidence. With the meter count rising linearly, total readings grow quadratically with time, so storage in year seven far exceeds a simple multiple of year one. Prof. Varga asks him to compare this with a policy that aggregates hourly readings to daily totals after two years. The integral shows a large reduction, which illustrates how retention decisions are also engineering decisions about cost and risk.

### Worked example

Kofi models storage growth as a rate, uses changes in the rate to detect failed feeds and integrates over seven years to compare full retention with aggregation after two years.

> **Synthetic case.** Northfield, Tidewater and all people are synthetic.

### Errors and limits

Linear growth is an assumption; revisit it when meter roll-out plans change.

### Exercises

- **EX001 — Daily rate.** About how many readings arrive per day? *Rubric:* 3 = about 2.16 million;; 2 = close;; 1 = wrong;; 0 = none.
- **EX002 — Feed failure.** What might a sudden drop in the reading rate mean? *Rubric:* 3 = a failed data feed;; 2 = correct;; 1 = none;; 0 = none.
- **EX003 — Aggregation effect.** What does aggregating to daily totals after two years do? *Rubric:* 3 = greatly reduces storage;; 2 = mentions reduction;; 1 = none;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) use sets and relations to describe data ownership; (2) model dependencies as graphs; (3) reason about keys and functions.

### 2.1 Sets of data

Kofi describes Tidewater's data as sets: customers, premises, meters and readings. The intersection of customers with a priority services list identifies vulnerable households needing extra support during supply interruptions. Set operations make governance questions precise. For example, the set of meters with readings but no linked premise should be empty; if it is not, some readings cannot be billed or explained. He writes such conditions as rules that can later be checked automatically against the real data. Each rule names the sets it compares and the result expected.

### 2.2 Relations and keys

A relation links elements of two sets, such as meters to premises. Kofi checks whether it is a function: each meter should map to exactly one premise at a time. In the synthetic replica, twelve meters map to two premises because of an old data migration. He explains that a key is an attribute that identifies each element uniquely, and that broken keys create ambiguity about who owns which reading. Defining keys and checking them is one of the first tasks of data governance.

### 2.3 Graphs of dependencies

Kofi models Tidewater's systems as a directed graph, with an edge from each system to the systems that use its data. The billing system depends on meter readings and tariffs; the leakage report depends on billing volumes and sensor flows. Following edges backwards from a report shows every source it relies on. He notes that graph reachability will be the basis for lineage analysis later in the course, when he traces exactly which sources feed a figure presented to Tidewater's board. Cycles are flagged.

### 2.4 Logic for rules

Governance rules can be expressed in logic. Kofi writes: for every reading, if the meter is active then the reading has a premise. He also writes the contrapositive and checks it on examples. Prof. Varga shows how precise logical rules prevent disagreements between teams, because ambiguous phrases such as all readings should be valid hide different meanings. He learns that writing rules formally first makes their later implementation in code and their explanation to managers more consistent. Formal rules also make test cases easier to derive later on.

### Worked example

Kofi uses sets to define rule conditions, finds twelve meters mapped to two premises, models systems as a dependency graph and writes quality rules in logical form.

> **Synthetic case.** The replica is synthetic.

### Errors and limits

Formal rules can still encode the wrong requirement; validate them with data owners.

### Exercises

- **EX004 — Empty set rule.** Which set should be empty? *Rubric:* 3 = meters with readings but no linked premise;; 2 = correct;; 1 = none;; 0 = none.
- **EX005 — Function check.** How many meters mapped to two premises? *Rubric:* 3 = twelve;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX006 — Graph use.** What does following edges backwards from a report show? *Rubric:* 3 = every source it relies on;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical measurement to data quality; (2) explain sensor error and drift; (3) record measurement metadata.

### 3.1 Measurement and data

Tidewater's flow sensors convert physical quantities into numbers. Kofi learns that every measurement has uncertainty from the instrument, the installation and the environment. A flow sensor near a bend in the pipe reads differently from one on a straight run. Data governance must therefore record how each value was measured, because a number without its measurement context can be misused. He notes that ISO 8000's emphasis on requirements includes knowing whether data are precise enough for their intended use. Context travels with values.

### 3.2 Error and drift

Sensor accuracy changes over time. Deposits inside pipes and ageing electronics cause drift, a slow systematic change in readings. Kofi studies synthetic data for a sensor that reads two percent high after three years. If the drift is not detected, leakage estimates fall because supplied volume appears higher than reality. He proposes comparing sensors against calibrated reference meters annually and recording calibration dates as metadata, so analysts can exclude or correct readings outside their calibration period. Drift is invisible without an independent reference measurement.

### 3.3 Units and conversions

A common data error in water utilities is unit confusion: cubic metres versus litres, or hourly versus daily flows. Kofi finds a synthetic case where one district's readings were stored in litres while others used cubic metres, inflating that district's demand a thousandfold in a report. He recommends storing units explicitly with each value and validating that units match the expected ones at ingestion. The physics lesson becomes a governance rule: never store a measured value without its unit. Units are mandatory fields.

### 3.4 Metadata for measurements

Kofi designs a metadata record for each sensor: identifier, location, type, unit, accuracy class, installation date, last calibration date and owner. The record lets analysts judge whether readings meet their needs and lets engineers schedule maintenance. Prof. Varga points out that metadata are data too and need their own quality rules, such as calibration dates not lying in the future. Kofi adds the record to his governance notes as the first example of metadata management. Each field has a defined format and an owner responsible for keeping it current.

### Worked example

Kofi explains measurement uncertainty, models a two-percent drift's effect on leakage, finds a litres-versus-cubic-metres error and designs sensor metadata with calibration dates.

> **Synthetic case.** Sensor data are synthetic; ISO 8000-1:2022 is real.

### Errors and limits

Calibration reduces but does not remove uncertainty; report it.

### Exercises

- **EX007 — Drift effect.** How does upward sensor drift affect leakage estimates? *Rubric:* 3 = leakage appears lower;; 2 = correct;; 1 = none;; 0 = none.
- **EX008 — Unit error.** What did the unit confusion do to one district? *Rubric:* 3 = inflated demand a thousandfold;; 2 = correct;; 1 = none;; 0 = none.
- **EX009 — Metadata fields.** Name three sensor metadata fields. *Rubric:* 3 = identifier, location, type, unit, accuracy, installation, calibration, owner;; 2 = three;; 1 = one;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write scripts that read and validate data files; (2) handle errors explicitly; (3) keep code readable for reviewers.

### 4.1 Reading data files

Kofi writes his first Python scripts using the standard library's csv module to read synthetic meter readings. Each row has a meter identifier, a timestamp, a reading and a unit. He learns to read files line by line, convert strings to numbers carefully and keep the original values for traceability. Prof. Varga requires synthetic data in every exercise, because student scripts often print data while debugging and should never expose real customer information. Each script also prints a count of rows read, rows accepted and rows rejected at the end.

### 4.2 Validation in code

Kofi adds checks: the meter identifier must match a pattern, the timestamp must parse, the reading must be a non-negative number and the unit must be cubic metres. Rows that fail are written to a rejects file with the reason, not silently dropped. He explains that silent dropping hides quality problems from data owners, while a rejects file gives them evidence to fix the source. Counting rejects by reason also shows which problems are most common. The commonest reason in the first run is a missing unit.

### 4.3 Handling errors

When a file is missing a column, Kofi's script stops with a clear message instead of guessing. When a single row is malformed, it records the problem and continues. He distinguishes errors that make the whole result untrustworthy from errors that affect only one record. Prof. Varga calls this fail loudly for structure, fail softly for content, and notes that governance depends on scripts that make problems visible rather than producing confident outputs from broken inputs. Both behaviours are tested with deliberately broken files.

### 4.4 Readable code

Kofi names variables clearly, writes a docstring explaining what each script reads and produces, and keeps functions short. A classmate reviews his code and finds an off-by-one error in timestamp handling, which Kofi fixes and covers with a test. He learns that code review is a quality control for the code that enforces data quality, and that readable code is easier to review, maintain and trust when other people depend on its output. The test now runs automatically whenever anyone changes the timestamp function in the script.

### Worked example

Kofi reads meter files with csv, validates four fields, writes rejects with reasons, stops on structural errors and fixes a reviewer-found timestamp bug with a test.

> **Synthetic case.** Files are synthetic.

### Errors and limits

Validation rules in code drift from written rules; review both together.

### Exercises

- **EX010 — Rejects file.** Why write a rejects file instead of dropping rows? *Rubric:* 3 = gives owners evidence to fix sources;; 2 = mentions evidence;; 1 = none;; 0 = none.
- **EX011 — Error policy.** What does fail loudly for structure, softly for content mean? *Rubric:* 3 = stop on missing columns, record bad rows and continue;; 2 = both;; 1 = one;; 0 = none.
- **EX012 — Review find.** What did the code review find? *Rubric:* 3 = an off-by-one timestamp error;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write clear technical notes about data; (2) present data quality findings to non-specialists; (3) document decisions.

### 5.1 Writing for engineers

Kofi writes a technical note on the unit error from Chapter 3. Prof. Varga asks for a fixed structure: summary, background, method, findings, impact and recommendations. The summary states the problem and its consequence in two sentences: one district's readings were stored in litres, inflating its demand in the monthly report. Engineers reading the note can then decide quickly whether to read further. Clear structure makes notes easier to find and reuse when a similar problem appears years later. Notes are stored in a shared index.

### 5.2 Writing for managers

For Tidewater's operations manager, Kofi writes a one-page version without code or formulas. It explains what went wrong, which reports were affected, what has been fixed and what decision is needed: approval to add unit validation to every data feed. He includes one chart comparing reported and corrected demand. The manager approves the change the same day. Kofi learns that managers need the decision and its consequences, not the full technical journey that led to them. The chart uses plain axis labels.

### 5.3 Presenting uncertainty

When Kofi presents leakage estimates affected by sensor drift, he shows ranges rather than single numbers and explains in plain words why the range exists. Some managers prefer a single figure, so he gives a central estimate while keeping the range visible. Prof. Varga notes that hiding uncertainty can lead to poor decisions, while overwhelming people with technical detail can lead to no decision at all. The skill is to show enough uncertainty to be honest and useful. The range appears on every slide.

### 5.4 Decision records

Kofi starts a decision record for data governance decisions at Tidewater: the date, the decision, who made it, the options considered and the evidence. The first entry records the approval of unit validation. He explains that DAMA-DMBOK2 stresses documented policies and decisions, because organisations forget why rules exist. Months later, when someone asks why a feed is rejected for wrong units, the record answers the question without depending on anyone's memory. The record lives in the same repository as the validation code, so code and reasons stay together.

### Worked example

Kofi writes a structured technical note, a one-page manager version that wins approval for unit validation, presents leakage as a range and starts a decision record.

> **Synthetic case.** Notes are synthetic; DAMA-DMBOK2 is real.

### Errors and limits

Short summaries can lose caveats; keep the main limitation visible.

### Exercises

- **EX013 — Note structure.** What structure did Prof. Varga require? *Rubric:* 3 = summary, background, method, findings, impact, recommendations;; 2 = most;; 1 = few;; 0 = none.
- **EX014 — Manager decision.** What decision did the manager make? *Rubric:* 3 = approve unit validation for every feed;; 2 = correct;; 1 = none;; 0 = none.
- **EX015 — Record contents.** What does a decision record contain? *Rubric:* 3 = date, decision, maker, options, evidence;; 2 = most;; 1 = one;; 0 = none.

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use integrals to compute volumes from flow rates; (2) estimate numerical errors; (3) relate accumulation to reconciliation.

### 6.1 From flow to volume

Tidewater's sensors record flow rates every fifteen minutes. Volume supplied over a day is the integral of flow over time. Kofi approximates it with the trapezoidal rule on synthetic data and compares it with the volume calculated from the district's bulk meter. The two agree within half a percent. He explains that this calculation feeds the leakage estimate, so the method used to integrate flow is itself a data processing decision that should be documented and applied consistently. The method is written into the reporting standard.

### 6.2 Numerical error

Kofi tests how sampling interval affects error. With hourly samples instead of fifteen-minute samples, the trapezoidal estimate misses short peaks in demand and differs from the bulk meter by two percent. He shows that halving the interval roughly quarters the error for smooth flows, as theory predicts, but not for sudden spikes. The finding informs a governance question: what sampling interval is required for the data to be fit for leakage reporting, and who sets that requirement? Leakage reporting needs fifteen-minute data.

### 6.3 Accumulation and reconciliation

Integrals accumulate. Small errors in flow add up over a month into large differences in volume. Kofi computes a monthly reconciliation between supplied volume from sensors and billed volume from meters. The difference represents leakage plus measurement error plus timing differences in meter reading. He learns that reconciliation is a central data governance control in utilities, because it connects two independent data sources and reveals when either has a problem. Each month's difference is tracked over time, and a sudden jump prompts a check of both feeds before anyone concludes that leakage has increased.

### 6.4 Series for forecasting

Kofi uses a simple series expansion to approximate a demand curve that rises in the morning. The first terms capture most of the shape, while later terms add little. Prof. Varga explains that the same idea appears in data governance: a small number of well-chosen quality measures often captures most of the risk, while many extra measures add cost and confusion. Kofi records this as a design principle for the measurement work he will do in later chapters. Fewer, better measures win.

### Worked example

Kofi integrates flow with the trapezoidal rule within half a percent of the bulk meter, shows hourly sampling raises error to two percent and links accumulation to monthly reconciliation.

> **Synthetic case.** Flow data are synthetic.

### Errors and limits

The trapezoidal rule assumes smooth flow between samples; spikes break it.

### Exercises

- **EX016 — Integration agreement.** How closely did the trapezoidal estimate match the bulk meter? *Rubric:* 3 = within half a percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX017 — Hourly error.** What error did hourly sampling produce? *Rubric:* 3 = about two percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX018 — Reconciliation components.** What does the supplied-minus-billed difference contain? *Rubric:* 3 = leakage, measurement error, timing differences;; 2 = all;; 1 = one;; 0 = none.

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) estimate error rates from samples; (2) build confidence intervals; (3) use control limits for quality monitoring.

### 7.1 Sampling for quality

Tidewater cannot inspect every reading by hand, so Kofi samples. He draws 400 synthetic readings at random and checks each against the meter photograph taken by field staff. Eight disagree. The estimated error rate is 2 percent. He explains that a random sample allows a valid estimate of the whole population's error rate, while samples chosen for convenience, such as only easy-to-reach meters, may be biased and mislead decisions about data quality. The sample is drawn by a script with a fixed seed, so anyone can draw the same meters and repeat the checks.

### 7.2 Confidence intervals

Kofi computes a 95 percent confidence interval for the error rate using the Wilson method, which behaves well for small proportions. The interval runs from about 1.0 to 3.9 percent. He reports the interval rather than only the point estimate, because Tidewater's quality target is 3 percent and the interval includes values above it. The data owner therefore cannot claim with confidence that the target is met, and Kofi recommends a larger sample next quarter. With 400 readings and eight errors, the interval is wide; a sample of 1,600 would narrow it considerably.

### 7.3 Control charts

For ongoing monitoring, Kofi plots the daily proportion of rejected readings with control limits three standard deviations from the long-run mean. Points outside the limits signal a change worth investigating. In the synthetic data, one day exceeds the upper limit, which turns out to be a firmware update on a batch of meters. He learns that control charts separate normal variation from real problems and stop teams chasing random noise or ignoring real changes. The firmware batch is rolled back, and the next day returns within the limits.

### 7.4 Statistics and governance

Prof. Varga connects statistics to governance. Quality targets mean little unless measured properly. A target of 3 percent errors needs a sampling plan, an interval method and an owner who acts when limits are crossed. Kofi writes these elements into a measurement standard for Tidewater's meter data. He notes that Batini and colleagues describe assessment as a stage in quality methodologies, and that statistics turns assessment from opinion into evidence that managers and auditors can check. The standard names the owner of each step and the action required.

### Worked example

Kofi estimates a 2 percent error rate from 400 sampled readings, reports a Wilson interval of about 1.0 to 3.9 percent, detects a firmware change with a control chart and writes a measurement standard.

> **Synthetic case.** Readings are synthetic; Batini et al. (2009) is real.

### Errors and limits

Control limits assume stable processes; recalculate after known changes.

### Exercises

- **EX019 — Error estimate.** What error rate did the sample give? *Rubric:* 3 = 2 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX020 — Target judgement.** Why can the owner not claim the 3 percent target is met? *Rubric:* 3 = interval includes values above 3 percent;; 2 = mentions interval;; 1 = none;; 0 = none.
- **EX021 — Control signal.** What caused the out-of-limit day? *Rubric:* 3 = a firmware update on a batch of meters;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) relate hardware limits to data handling; (2) understand edge devices in metering; (3) consider integrity during transmission and storage.

### 8.1 Edge devices

Each smart meter contains a small processor, memory and a radio. Kofi learns that meters store readings locally and transmit them in batches, so a radio outage causes delayed rather than lost data, up to the memory limit. A meter with seven days of storage loses readings if it cannot transmit for longer. Governance needs to know these limits, because a rule that marks late readings as invalid would wrongly reject legitimate delayed data after an outage. The late-data rule is changed accordingly.

### 8.2 Data representation

Kofi studies how readings are represented. Meters store integer counts of litres to avoid floating-point rounding, and the head-end system converts to cubic metres. A bug that converts twice divides values by a thousand. He also sees that timestamps are stored in UTC on meters but displayed in local time, and daylight saving changes create apparent duplicate or missing hours. Representation choices are low-level engineering details with direct effects on billing data quality. Timestamps are now stored in UTC everywhere, and local time is used only for display to customers.

### 8.3 Integrity checks

Meters attach a checksum to each batch so the receiver can detect corruption in transmission. Kofi explains that a checksum detects accidental errors but does not prove who sent the data. Tidewater also uses message authentication to show that readings came from genuine meters. He maps where each check happens and finds that readings pass through a vendor platform where checks are not logged, creating a gap in evidence about integrity between the meter and Tidewater's systems. The vendor agrees to log checks.

### 8.4 Storage tiers

Tidewater stores recent readings on fast storage for billing and older readings on cheaper archive storage. Kofi notes that moving data between tiers is a point where data can be lost or changed. He recommends comparing record counts and checksums before and after each migration. Prof. Varga explains that architecture decisions such as tiering are governance decisions too, because they determine how quickly data can be retrieved for customer queries, audits or legal requests. The first migration test finds that three days of readings are missing from the archive copy.

### Worked example

Kofi links meter memory limits to late-data rules, finds double-conversion and daylight-saving risks, maps integrity checks with a vendor gap and recommends counts and checksums for tier migrations.

> **Synthetic case.** Devices are synthetic.

### Errors and limits

Checksums detect accidents, not tampering; use authentication for origin.

### Exercises

- **EX022 — Seven-day limit.** When does a meter lose readings? *Rubric:* 3 = outage longer than its storage period;; 2 = correct;; 1 = none;; 0 = none.
- **EX023 — Daylight saving.** What problem does daylight saving create? *Rubric:* 3 = apparent duplicate or missing hours;; 2 = correct;; 1 = none;; 0 = none.
- **EX024 — Checksum limit.** What does a checksum not prove? *Rubric:* 3 = who sent the data;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure data processing code into tested modules; (2) write unit tests for quality rules; (3) use version control for rule changes.

### 9.1 Modules

Kofi reorganises his scripts into modules: one for reading files, one for validation rules, one for reporting. Each module has a clear interface. The validation module exposes a list of rules, each with a name, a description and a function. This structure lets data owners read the rule descriptions without reading code, and lets engineers add or change rules without touching the reader or reporter. He notes that clear separation reduces the chance of accidental changes affecting unrelated behaviour. Rule descriptions form a catalogue.

### 9.2 Unit tests for rules

For each rule, Kofi writes unit tests with synthetic cases that should pass and cases that should fail. The test for readings not below the previous value includes a meter replacement, where readings legitimately reset to zero. The first version of the rule wrongly rejects replacements, and the test reveals it. He adds a meter replacement flag to the rule. Prof. Varga emphasises that tests document the intended behaviour of rules as clearly as any written policy. The flag comes from the work order system.

### 9.3 Version control

All rule changes are made through version control with a message explaining why. When the meter replacement exception is added, the commit message links to the decision record. Kofi can show exactly when a rule changed and compare quality reports before and after. He explains that version history is evidence for auditors and for data owners who notice a sudden change in reject rates and want to know whether data or rules changed. Every change to the rule list is reviewed by a second engineer before it is merged into the main branch.

### 9.4 Code review for data rules

Kofi asks a metering engineer to review the rules, not just a programmer. The engineer points out that some older meters report readings only daily, so an hourly completeness rule would fail them unfairly. Kofi adds meter type as a parameter. He learns that domain experts catch errors that code reviewers miss, and that governance rules need both technical correctness and business correctness to be useful rather than just enforceable. Daily meters are now judged against a daily completeness rule, and their reject rate falls to the same level as hourly meters.

### Worked example

Kofi structures code into modules with named rules, writes tests that catch a meter replacement error, links rule changes to decisions in version control and gains domain review that adds meter type.

> **Synthetic case.** Code and data are synthetic.

### Errors and limits

Tests cover only cases someone thought of; add cases from real incidents.

### Exercises

- **EX025 — Rule structure.** What does each rule expose? *Rubric:* 3 = name, description and function;; 2 = all;; 1 = one;; 0 = none.
- **EX026 — Test catch.** What did the unit test reveal? *Rubric:* 3 = rule wrongly rejected meter replacements;; 2 = correct;; 1 = none;; 0 = none.
- **EX027 — Domain review.** What did the metering engineer point out? *Rubric:* 3 = older meters report only daily;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering ethics to data decisions; (2) consider safety impacts of poor data; (3) handle conflicts of interest.

### 10.1 Ethics in data work

Engineering codes ask engineers to hold public safety and welfare paramount and to act honestly within their competence. Kofi applies these duties to data. A wrong pressure sensor reading could cause operators to reduce pressure and leave a hospital without water, while a wrong water quality reading could hide contamination. Data governance therefore has safety consequences, and engineers who manage data share responsibility for those consequences even when they never touch a pipe. Kofi writes these duties at the top of his course notebook as a reminder of why his data work matters.

### 10.2 Vulnerable customers

Tidewater keeps a priority services register of customers who depend on water for medical equipment or need help during interruptions. Kofi recognises that this register includes health information and must be accurate, secure and used only for its purpose. An out-of-date register could mean a customer on home dialysis is not contacted during an outage. He recommends a yearly confirmation with each registered customer and strict access limits, balancing safety with privacy. Only the incident team and customer support can open the register, and every access is logged.

### 10.3 Honest reporting

Kofi's supervisor at Tidewater asks him to present only the leakage estimate within the regulatory target, omitting the higher estimate that accounts for sensor drift. Kofi recognises a conflict between pressure to look good and his duty to report honestly. He presents both estimates, explains the drift and recommends calibration. Prof. Varga supports him and notes that regulators rely on utilities' data, so selective reporting can mislead public decisions. The supervisor later thanks him, because the regulator's audit asks about sensor calibration that very year.

### 10.4 Competence and limits

Kofi is asked to approve a change to water quality data processing. He recognises that he lacks the chemistry knowledge to judge whether the change could mask contamination, and he refers the decision to a qualified water quality scientist. He records the referral in the decision log. Prof. Varga explains that knowing the limits of one's competence is an ethical duty, especially when data decisions can affect public health and safety. The scientist approves a revised change after adding a check that flags readings above the safety threshold.

### Worked example

Kofi connects data errors to safety, protects the priority services register, reports both leakage estimates despite pressure and refers a water quality decision beyond his competence.

> **Synthetic case.** Cases are synthetic.

### Errors and limits

Ethical pressure is often subtle; record decisions and reasons.

### Exercises

- **EX028 — Safety example.** Give a safety consequence of bad data. *Rubric:* 3 = wrong pressure reading leaves a hospital without water;; 2 = mentions harm;; 1 = none;; 0 = none.
- **EX029 — Register care.** What did Kofi recommend for the priority register? *Rubric:* 3 = yearly confirmation and strict access;; 2 = both;; 1 = one;; 0 = none.
- **EX030 — Competence.** Why did Kofi refer the water quality change? *Rubric:* 3 = lacked chemistry competence;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) trace how meter and sensor data cross networks; (2) assess protocol choices for integrity and availability; (3) document network data flows for governance.

### 11.1 Paths through the network

Meter readings travel by radio to collectors on street poles, then over a mobile network to a vendor's head-end platform, then over the internet to Tidewater's data centre. Sensor readings follow a separate path over a private industrial network to the control system. Kofi draws both paths and labels each hop with the protocol, the operator and whether data are encrypted. He finds that the governance owner changes at each boundary, which explains why nobody could answer questions about end-to-end delays or losses.

### 11.2 Protocols and integrity

The meter path uses an encrypted, authenticated protocol from collector to head-end, so readings are protected against tampering in transit. The industrial network uses an older protocol without authentication, which relies on the network being isolated. Kofi notes that this does not make sensor data wrong, but it means Tidewater cannot prove from the protocol alone that a reading came from a genuine sensor. He records the gap and recommends monitoring for unexpected devices on the industrial network. An alert now fires for unknown devices.

### 11.3 Availability and buffering

Network outages delay data. Collectors buffer readings for up to two days; the mobile network occasionally drops for hours. Kofi measures, on synthetic logs, how often readings arrive more than six hours late and finds that most late arrivals cluster around storms. He argues that data consumers such as billing must be told how late data can legitimately arrive, so that they do not treat late readings as missing or estimate bills unnecessarily before the real readings land. The billing team now waits forty-eight hours.

### 11.4 Documenting flows

Kofi produces a network data flow document with each hop, owner, protocol, encryption, buffering and typical latency. The document is reviewed by the network team and the data governance lead. It becomes the reference when Tidewater negotiates a service level with the metering vendor. Prof. Varga notes that a governance owner cannot be accountable for data they cannot see, and that documenting flows across organisational boundaries is how accountability becomes possible in practice. The vendor service level now includes a maximum delay for buffered readings after an outage.

### Worked example

Kofi traces meter and sensor paths, finds an unauthenticated industrial protocol, measures storm-related delays and documents every hop with owners and latencies.

> **Synthetic case.** Networks are synthetic.

### Errors and limits

Flow documents age quickly; review them after network changes.

### Exercises

- **EX031 — Owner changes.** Why could nobody answer end-to-end questions? *Rubric:* 3 = the governance owner changes at each boundary;; 2 = mentions boundaries;; 1 = none;; 0 = none.
- **EX032 — Industrial gap.** What gap did Kofi find on the industrial network? *Rubric:* 3 = no protocol authentication;; 2 = correct;; 1 = none;; 0 = none.
- **EX033 — Late data.** When do late arrivals cluster? *Rubric:* 3 = around storms;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) relate operating system controls to data protection; (2) manage scheduled data jobs reliably; (3) keep audit logs useful.

### 12.1 Files and permissions

Tidewater's data processing runs on Linux servers. Kofi reviews file permissions on directories holding customer extracts and finds that one directory is readable by every user on the server. He explains that operating system permissions are the last line of defence when application controls fail. He changes the directory to be readable only by the processing account and the data team group, and documents the expected permissions so that later checks can compare actual settings with the intended ones. A weekly script compares them.

### 12.2 Scheduled jobs

Nightly jobs load meter readings, run quality rules and publish reports. Kofi finds that if a job fails, the next job runs anyway on incomplete data and publishes misleading results. He changes the schedule so each job checks that its predecessor finished successfully and produced the expected row counts. Jobs that cannot run send an alert. He notes that dependencies between jobs are data lineage in practice, and making them explicit prevents silent propagation of failures. The alert goes to the on-call data engineer.

### 12.3 Audit logs

The operating system records logins and commands. Kofi checks that logs from data servers are sent to a central log store, where administrators cannot alter them, and that they are kept for one year. He finds one server whose logs stayed local and were overwritten after a week. Without logs, Tidewater could not show who accessed a customer extract during an investigation. He adds the server to central logging and a weekly check that all data servers are reporting. The check emails missing servers.

### 12.4 Patching and change

Kofi joins the monthly patch cycle. Before patching data servers, the team runs a test job on a staging server to confirm that the new libraries do not change outputs. In one cycle, an updated date library changes how ambiguous timestamps are parsed. The test catches the difference before production. He learns that system maintenance can alter data processing silently, so governance needs regression tests for data outputs as well as for application features. The comparison script is kept and run on every patch cycle from then on.

### Worked example

Kofi restricts a world-readable extract directory, chains jobs on successful predecessors, centralises a server's logs and catches a timestamp-parsing change in staging before patching.

> **Synthetic case.** Servers are synthetic.

### Errors and limits

Permissions drift after emergency fixes; check them regularly.

### Exercises

- **EX034 — Permission fix.** What did Kofi change about the extract directory? *Rubric:* 3 = readable only by the processing account and data team;; 2 = correct;; 1 = none;; 0 = none.
- **EX035 — Job chaining.** How are jobs now protected from bad inputs? *Rubric:* 3 = each checks its predecessor succeeded with expected counts;; 2 = mentions predecessor;; 1 = none;; 0 = none.
- **EX036 — Patch catch.** What did the staging test catch? *Rubric:* 3 = a change in timestamp parsing;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) design schemas that encode governance rules; (2) use constraints and reference data; (3) manage master data for customers and premises.

### 13.1 Schemas as rules

Kofi designs a relational schema for customers, premises, meters and readings. Primary keys make each entity unique, and foreign keys ensure that a reading refers to a real meter and a meter to a real premise. Not-null constraints enforce required fields. He explains that putting rules into the schema means the database itself refuses invalid data, rather than relying on every application to check. The schema becomes a precise, enforceable statement of part of Tidewater's data standard. Rejected inserts are logged with reasons.

### 13.2 Reference data

Tariff codes, meter types and district codes are reference data: small, controlled lists used across systems. Kofi finds three versions of the district list in different systems, with one district renamed in only two. He proposes a single reference table owned by the network planning team, with each change dated and approved. DAMA-DMBOK2 treats reference and master data as a distinct management area because inconsistencies in shared lists ripple into every report that uses them. Other systems now copy the table nightly.

### 13.3 Master data

Customer and premise records are master data, shared by billing, customer service and field operations. Kofi finds duplicate premises created when field staff register new connections without searching first. He designs a matching step that compares normalised addresses and coordinates before a new premise is created, and a steward role in customer operations who resolves possible duplicates. He notes that master data quality depends as much on process and ownership as on database design. The steward clears the possible duplicates queue every week.

### 13.4 History and change

Customers move, tariffs change and meters are replaced. Kofi designs tables that keep history with valid-from and valid-to dates, so past bills can be explained using the facts that applied at the time. Without history, a customer querying an old bill would see today's tariff and become confused. He tests the design with synthetic examples, including a meter replaced mid-month, and confirms that billing calculations match the period-by-period facts. Customer service staff confirm that the history view answers queries they previously escalated to billing.

### Worked example

Kofi encodes keys and constraints in a schema, consolidates three district lists into owned reference data, adds duplicate-premise matching with a steward and keeps dated history.

> **Synthetic case.** Schemas are synthetic; DAMA-DMBOK2 is real.

### Errors and limits

Constraints can block urgent fixes; define a controlled override process.

### Exercises

- **EX037 — Foreign key purpose.** What do foreign keys ensure here? *Rubric:* 3 = readings refer to real meters, meters to real premises;; 2 = correct;; 1 = none;; 0 = none.
- **EX038 — District lists.** How many versions of the district list existed? *Rubric:* 3 = three;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX039 — History purpose.** Why keep valid-from and valid-to dates? *Rubric:* 3 = to explain past bills with facts at the time;; 2 = mentions past;; 1 = none;; 0 = none.

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) apply requirements and testing practice to data pipelines; (2) manage releases of data logic; (3) design for maintainability.

### 14.1 Requirements for pipelines

Kofi writes requirements for the meter data pipeline as testable statements: every accepted reading has a valid meter and unit; rejected readings are reported with reasons within one hour; daily totals for each district reconcile with the sum of readings. Each requirement has an owner and an acceptance test. He explains that vague requirements such as data should be accurate cannot be tested, so they cannot be shown to be met or traced when they fail. Owners sign off each acceptance test.

### 14.2 Testing pipelines

Kofi builds three layers of tests. Unit tests check individual rules. Integration tests run a small synthetic dataset through the whole pipeline and compare outputs with expected results. Data tests run on production outputs and check properties such as row counts within expected ranges and no negative consumption. The data tests catch a problem unit tests could not: a vendor file arrives with a new column order, and readings land in the wrong fields until the reader is updated. A column-name check now runs first.

### 14.3 Release management

Changes to pipeline logic follow a release process: code review, tests, a staging run on the previous month's synthetic replica and a comparison of outputs. Differences above agreed tolerances must be explained before release. Kofi argues that pipeline releases deserve the same care as customer-facing software, because a small change to a rule can change thousands of bills. Each release note links to the decision record that justified the rule change. Two releases were held back last quarter because unexplained differences exceeded the tolerances.

### 14.4 Maintainability

Kofi documents the pipeline with a diagram, a rule catalogue and an operations guide. He removes unused code and replaces hard-coded thresholds with configuration values that data owners can review. Prof. Varga explains that maintainability is a governance concern: when the person who built a pipeline leaves, the organisation must still be able to explain and change it. Unmaintainable pipelines become black boxes whose outputs nobody can justify. A new team member uses the operations guide to rerun a failed load in her first week without help.

### Worked example

Kofi writes testable pipeline requirements, builds unit, integration and data tests that catch a column-order change, adds release comparisons and documents the pipeline for maintainability.

> **Synthetic case.** The pipeline is synthetic.

### Errors and limits

Tolerances set too wide hide real changes; review them with owners.

### Exercises

- **EX040 — Testable requirement.** Give one testable pipeline requirement. *Rubric:* 3 = accepted readings have valid meter and unit; rejects reported within an hour; totals reconcile;; 2 = one;; 1 = none;; 0 = none.
- **EX041 — Data test catch.** What did data tests catch? *Rubric:* 3 = a vendor file with a new column order;; 2 = correct;; 1 = none;; 0 = none.
- **EX042 — Hard-coded values.** What replaced hard-coded thresholds? *Rubric:* 3 = configuration values reviewed by owners;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to utility data; (2) choose access controls for data sets; (3) relate security incidents to data governance.

### 15.1 Three properties

Kofi applies the classic security properties to Tidewater's data. Confidentiality protects customer details and the priority services register. Integrity protects meter readings and sensor values from unauthorised change, which matters for billing and safety. Availability ensures operators see sensor data during incidents. Different data sets need different emphasis: control system data need availability and integrity first, while customer data need confidentiality. Governance assigns these priorities so engineers know which trade-offs are acceptable. The priorities are written into each data set's catalogue entry so engineers see them when building systems.

### 15.2 Access by role

Kofi designs role-based access for data sets. Billing analysts see readings and tariffs but not the priority register. Field staff see premise and meter details for jobs assigned to them. Data scientists work on pseudonymised extracts with customer identifiers replaced. Each role is approved by the data owner. He finds that analysts currently share one account for the data warehouse, which prevents accountability, and replaces it with named accounts linked to roles. Access is reviewed by each owner every quarter, and unused roles are removed.

### 15.3 Incidents and data

When a contractor's laptop with a customer extract is stolen, Kofi helps analyse the incident. The extract contained names and addresses for one district and was not encrypted. Because it was personal data, the data protection officer assesses notification under Article 33 of the GDPR. Kofi traces why the extract existed: a one-off request approved informally. He recommends that extracts follow a request process with an owner's approval, minimal fields, encryption and an expiry date. The district's customers receive a letter explaining what happened.

### 15.4 Security and governance together

Kofi notes that security controls protect data, while governance decides what data should exist, who owns them and for what purposes. The stolen extract would have been harmless if governance had refused unnecessary fields or required pseudonymisation. Prof. Varga explains that the two disciplines share tools such as access control and logging, but answer different questions, and that effective organisations connect them through shared ownership and policies. At Tidewater, the security manager and the data governance lead now meet monthly and share one register of data risks.

### Worked example

Kofi assigns security priorities by data set, designs role-based access with named warehouse accounts, analyses a stolen extract and recommends a governed extract process.

> **Synthetic case.** The incident is synthetic; GDPR Article 33 is real.

### Errors and limits

Pseudonymised data remain personal data; protect them accordingly.

### Exercises

- **EX043 — Control data priority.** Which properties come first for control system data? *Rubric:* 3 = availability and integrity;; 2 = both;; 1 = one;; 0 = none.
- **EX044 — Shared account.** What warehouse problem did Kofi fix? *Rubric:* 3 = shared analyst account replaced by named accounts;; 2 = correct;; 1 = none;; 0 = none.
- **EX045 — Extract rules.** Name two rules for future extracts. *Rubric:* 3 = owner approval, minimal fields, encryption, expiry;; 2 = two;; 1 = one;; 0 = none.

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) view data governance as part of a system of systems; (2) manage interfaces and requirements across teams; (3) use life cycle thinking for data.

### 16.1 A system of systems

Tidewater's data environment includes meters, the vendor head-end, billing, customer service, the control system, the warehouse and regulatory reporting. Each is owned by a different team or company. Kofi uses systems engineering to view them as one system whose behaviour emerges from interactions. A quality problem often appears far from its cause, as when a meter firmware issue shows up as a billing complaint. Systems thinking helps him trace effects across boundaries rather than fixing symptoms locally. Kofi traces three recent complaints this way.

### 16.2 Interface control

Kofi writes interface control documents for key data exchanges: the meter readings file from the vendor and the daily volume feed from the control system. Each document defines fields, units, formats, timing, error handling and who to contact. When the vendor changes a field, the document requires notice and testing. He explains that interface documents turn informal assumptions into agreed requirements, which are the basis for holding partners accountable when data do not arrive as expected. Both partners sign the documents formally.

### 16.3 Life cycle of data

Kofi maps the life cycle of meter data: creation in the meter, transmission, validation, use in billing, analysis, archiving and deletion. At each stage he notes the owner, quality rules, security controls and retention. ISO/IEC 38505-1 encourages governing bodies to consider data value, risk and constraints across the life cycle. Kofi finds that deletion is the least defined stage; nobody had decided when hourly readings should be deleted or aggregated after billing evidence periods end. The board is asked to make that decision.

### 16.4 Requirements traceability

Kofi builds a traceability matrix linking governance requirements, such as accurate billing and retention limits, to system requirements, tests and evidence. Each regulatory obligation traces to at least one control and one test. Gaps appear where obligations have no test, such as deleting hourly data after seven years. He adds requirements and tests for the gaps. Prof. Varga notes that traceability lets engineers answer auditors' questions with evidence rather than reassurance. The matrix is updated whenever a regulation or system changes, and reviewed every quarter.

### Worked example

Kofi treats Tidewater's data as a system of systems, writes interface control documents, maps the data life cycle and finds deletion undefined, and builds a traceability matrix.

> **Synthetic case.** Systems are synthetic; ISO/IEC 38505-1:2017 is real.

### Errors and limits

Interface documents fail if partners are not bound by them; reference them in contracts.

### Exercises

- **EX046 — Distant symptom.** How can a meter firmware issue appear? *Rubric:* 3 = as a billing complaint;; 2 = correct;; 1 = none;; 0 = none.
- **EX047 — Interface fields.** What does an interface control document define? *Rubric:* 3 = fields, units, formats, timing, error handling, contacts;; 2 = most;; 1 = few;; 0 = none.
- **EX048 — Weakest stage.** Which life cycle stage was least defined? *Rubric:* 3 = deletion;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) apply feedback concepts to data quality processes; (2) design measurement and correction loops; (3) avoid unstable or slow loops.

### 17.1 Feedback loops

A control system measures an output, compares it with a target and acts to reduce the difference. Kofi sees data quality management the same way: measure reject rates, compare with targets and correct causes. Tidewater already measures rejects but has no reliable action step, so the loop is open. He proposes a weekly review where data owners receive their reject figures and must record a corrective action for any figure above target, closing the loop. The review takes thirty minutes on Mondays.

### 17.2 Delay and stability

Feedback loops with long delays can oscillate. Kofi notices that Tidewater changes meter validation thresholds after each month's complaints, but complaints arrive weeks after bills, so thresholds swing back and forth. He recommends basing changes on weekly reject data, which arrives quickly, and limiting threshold changes to small steps. He explains that the same principles that stabilise pumps and valves also stabilise organisational processes that respond to data quality measurements. Threshold changes now need a written reason and a check one week after the change.

### 17.3 Root causes

A good loop corrects causes rather than symptoms. When readings from one district fail validation repeatedly, staff manually override them each week. Kofi traces the failures to a batch of meters with a firmware bug and asks the vendor to fix it. Manual overrides stop. He notes that correcting individual records forever is like a controller that compensates for a broken sensor without anyone repairing it, and that root cause analysis belongs in every quality loop. The vendor ships a firmware fix within a month.

### 17.4 Measuring the loop

Kofi measures the loop itself: time from a figure exceeding target to a recorded action, and time from action to improvement. Initially, actions take three weeks to record. After assigning named owners, they take one week. He presents loop performance to the data governance group as evidence that the process works. Prof. Varga notes that governance processes, like control systems, should be measured on how well they respond, not just on whether they exist. Improvement then follows within about two further weeks on average.

### Worked example

Kofi closes an open quality loop with weekly owner actions, stabilises oscillating thresholds with faster data and small steps, fixes a firmware cause and measures loop response time.

> **Synthetic case.** Processes are synthetic.

### Errors and limits

Too many targets overwhelm owners; keep loops focused.

### Exercises

- **EX049 — Open loop.** Why was Tidewater's quality loop open? *Rubric:* 3 = no reliable corrective action step;; 2 = correct;; 1 = none;; 0 = none.
- **EX050 — Oscillation fix.** How did Kofi stop thresholds swinging? *Rubric:* 3 = weekly reject data and small steps;; 2 = both;; 1 = one;; 0 = none.
- **EX051 — Loop speed.** How fast were actions recorded after naming owners? *Rubric:* 3 = one week instead of three;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) design layered protection for data platforms; (2) separate environments; (3) place governance controls in the architecture.

### 18.1 Layers

Kofi designs a security architecture for Tidewater's data platform with layers: network segmentation separating the control system from business systems, identity and access management, encryption at rest and in transit, logging and monitoring, and data-level controls such as masking of customer identifiers. He explains that layers mean a failure in one control does not expose everything. The architecture is reviewed by the security team and data governance lead together, since each layer affects both. Each layer has a named owner and a test schedule.

### 18.2 Environments

Development, test and production environments are separated. Kofi finds that developers have been copying production customer data into test environments to reproduce bugs. He proposes a synthetic data generator that produces realistic customers, premises and readings with the same statistical properties, plus a strict rule that production personal data never enter test. NIST SP 800-188 discusses synthetic data and de-identification approaches, which he uses to judge what properties the generator must preserve. The generator is itself tested to make sure no real records can be reproduced from its output.

### 18.3 Governance controls in architecture

Kofi places governance controls at specific points: quality rules at ingestion, classification tags on each data set in the catalogue, access policies enforced by the warehouse based on those tags and retention jobs that read tags to decide deletion. He argues that controls tied to metadata scale better than controls written into each application. When a new data set is tagged as containing personal data, protections apply automatically rather than depending on someone remembering. Tag changes are logged and reviewed by the owner.

### 18.4 Review

The architecture review raises concerns about performance of masking on large queries and about who maintains classification tags. Kofi runs a test showing masking adds acceptable delay, and proposes that data owners approve tags when data sets are registered. Prof. Varga notes that architecture is a set of decisions with trade-offs, and that recording rejected alternatives, such as encrypting every column individually, helps future engineers understand the chosen design. The decision record lists that alternative, its cost and the reason it was not chosen by the review panel.

### Worked example

Kofi designs layered data platform security, replaces production data in test with synthetic data, ties access and retention to classification tags and records trade-offs from review.

> **Synthetic case.** The architecture is synthetic; NIST SP 800-188 is real.

### Errors and limits

Tags are only as good as their maintenance; audit them.

### Exercises

- **EX052 — Test data rule.** What rule did Kofi propose for test environments? *Rubric:* 3 = production personal data never enter test;; 2 = correct;; 1 = none;; 0 = none.
- **EX053 — Tag-driven controls.** Why tie controls to metadata tags? *Rubric:* 3 = protections apply automatically and scale;; 2 = mentions automatic;; 1 = none;; 0 = none.
- **EX054 — Tag owner.** Who approves classification tags? *Rubric:* 3 = data owners at registration;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) manage identities of people and devices; (2) use hashing for pseudonymisation; (3) govern cryptographic keys.

### 19.1 People and devices

Tidewater manages identities for staff, contractors and 90,000 meters. Each meter has a cryptographic identity used to authenticate its readings. Kofi learns that device identities must be governed like staff accounts: issued, recorded, rotated and revoked when a meter is removed. He finds 230 meters removed from service whose identities remained valid in the head-end platform. A stolen meter could therefore still send readings that would be accepted, so he recommends linking revocation to the meter removal work order. The revocation step is now automatic.

### 19.2 Pseudonymisation with keyed hashes

For analysis, data scientists need to link a customer's readings over time without seeing names or account numbers. Kofi replaces account numbers with keyed hashes using Python's hmac module and a secret key held by the data team. The same account always produces the same pseudonym, enabling linkage, while the key prevents others from recomputing it. He notes that the result is pseudonymised, not anonymous, so it remains personal data under the GDPR and needs protection. Only two named staff can read the key.

### 19.3 Key management

Keys protect meter data, warehouse encryption and pseudonyms. Kofi drafts key governance: each key has an owner, purpose, storage location, rotation schedule and recovery procedure. Keys for pseudonyms are rotated yearly, with old keys kept only as long as needed to link historical analyses. He finds a pseudonymisation key stored in a script file, which he moves to the key management service with access limited to two people. Recovery procedures are tested once a year by restoring a key from backup in a controlled exercise.

### 19.4 Cryptography and trust

Kofi reflects that cryptography provides strong technical guarantees but shifts trust to keys and the people who manage them. If key holders leave without handover, data may become unusable; if keys leak, protections disappear. Prof. Varga explains that this is why key management is a governance topic, not only a technical one, and why decisions about who may hold keys should be recorded and reviewed like any other data decision. Tidewater's key holders are now listed in the data governance register and reviewed yearly.

### Worked example

Kofi finds 230 removed meters with valid identities, links revocation to work orders, pseudonymises accounts with keyed hashes, drafts key governance and moves a key out of a script.

> **Synthetic case.** Identities and keys are synthetic.

### Errors and limits

Keyed hashes resist outsiders but not anyone holding the key.

### Exercises

- **EX055 — Stale identities.** How many removed meters still had valid identities? *Rubric:* 3 = 230;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX056 — Pseudonym status.** Are keyed-hash pseudonyms anonymous? *Rubric:* 3 = no, they remain personal data;; 2 = correct;; 1 = yes;; 0 = none.
- **EX057 — Key location fix.** Where was a key wrongly stored? *Rubric:* 3 = in a script file;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-20"></a>

## Chapter 20 — Data governance: engineering context

### Learning outcomes

You will (1) define data governance for an engineering organisation; (2) map decision rights; (3) set the scope of the specialist chapters.

### 20.1 What governance means here

Kofi defines data governance at Tidewater as the system of decision rights, policies, roles and controls that ensures meter, sensor, customer and asset data are fit for their uses and handled lawfully. DAMA-DMBOK2 describes governance as authority and control over data assets, while ISO/IEC 38505-1 asks the governing body to direct, evaluate and monitor data use. He notes that the previous nineteen chapters supplied the engineering foundations that governance now relies on. Kofi presents this definition to the head of data, who adopts it for Tidewater's governance charter.

### 20.2 Decision rights

Kofi uses Khatri and Brown's domains to map decision rights at Tidewater: data principles, quality, metadata, access and life cycle. For each, he records who decides, who provides input and who is informed. The map shows that quality rules for meter data are decided by whoever writes the pipeline code, while retention decisions are made by nobody. He presents these gaps to the head of data, who agrees to assign owners for each domain. Each assignment is dated and recorded in the charter.

### 20.3 Roles

Kofi proposes roles: a data governance board chaired by the operations director, data owners for each major data domain, stewards who maintain rules and definitions day to day, and custodians in IT who operate systems. He writes a short description of each role's decisions and duties. He stresses that owners must have authority over the processes that create their data; otherwise they become accountable for problems they cannot fix, which leads to frustration rather than improvement. The board approves the role descriptions.

### 20.4 Scope of the specialist work

Kofi sets the scope for the remaining chapters: requirements, models, threats, methods, architecture, controls, implementation, measurement, reliability, safety, integration, performance, operations, validation and maintainability, all applied to Tidewater's meter-to-board-report data chain. Prof. Varga approves a focus on the leakage indicator reported to the regulator, because it depends on many systems and teams, making it a good test of governance across engineering boundaries. The leakage indicator combines meter readings, sensor flows, network asset records and estimates, so every specialist chapter that follows tests a different part of the same chain from meter to regulator.

### Worked example

Kofi defines governance for Tidewater, maps decision rights finding quality decided by code authors and retention by nobody, proposes board, owner, steward and custodian roles and scopes later work on the leakage indicator.

> **Synthetic case.** Tidewater is synthetic; DAMA-DMBOK2, ISO/IEC 38505-1:2017 and Khatri and Brown (2010) are real.

### Errors and limits

Role charts do not create authority; confirm it in job descriptions.

### Exercises

- **EX058 — Retention rights.** Who decided retention before the map? *Rubric:* 3 = nobody;; 2 = correct;; 1 = someone;; 0 = none.
- **EX059 — Steward duty.** What do stewards do? *Rubric:* 3 = maintain rules and definitions day to day;; 2 = correct;; 1 = none;; 0 = none.
- **EX060 — Focus indicator.** Which indicator do later chapters follow? *Rubric:* 3 = the leakage indicator reported to the regulator;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-21"></a>

## Chapter 21 — Data governance: requirements

### Learning outcomes

You will (1) derive governance requirements from regulation and business need; (2) write them as testable statements; (3) agree priorities with owners.

### 21.1 Sources of requirements

Kofi gathers requirements for the leakage indicator from four sources: the regulator's reporting guidance, Tidewater's own leakage reduction targets, data protection law for customer data used in billing volumes, and the needs of network engineers who use leakage by district to plan repairs. He lists each source with the clause or meeting where the need was stated. He explains that requirements without a recorded source are hard to defend when budgets are cut or priorities change. The source list is stored with the requirements.

### 21.2 Testable statements

He rewrites vague needs as testable statements. Leakage should be reliable becomes: the monthly leakage figure is calculated from volumes that reconcile within one percent with independent totals, and every input has a named owner. Data should be timely becomes: the daily volume feed arrives by 06:00 on at least 95 percent of days. Each statement names a measure, a threshold and an owner who answers for it. These statements later become the tests in the verification laboratories. Vague wording is returned to its author.

### 21.3 Conflicts

Some requirements conflict. Network engineers want leakage by street, which would need customer-level billing volumes, while the data protection officer wants analysts to see aggregated data only. Kofi proposes district-level aggregation with a minimum of fifty properties per area, which supports repair planning without exposing individual consumption. The compromise is recorded with the reasons and approved by both owners. He notes that conflicts handled openly produce better designs than conflicts discovered after systems are built. The data protection officer signs the final note.

### 21.4 Priorities

With twenty-four requirements listed, Kofi asks owners to rank them using impact on the regulator's figure and on customers. Owner assignment, reconciliation and timeliness rank highest. Documentation standards rank lower. He uses the ranking to plan the specialist chapters, tackling the highest-impact requirements first. Prof. Varga reminds him that unranked requirement lists encourage teams to do the easiest items first, which can leave the most important risks unaddressed for months while effort goes elsewhere. The ranked list is published on the governance intranet page.

### Worked example

Kofi gathers leakage indicator requirements from four sources, rewrites them as testable statements, resolves a street-level conflict with district aggregation and ranks twenty-four requirements with owners.

> **Synthetic case.** Requirements are synthetic.

### Errors and limits

A threshold without a measurement method is not testable; define both.

### Exercises

- **EX061 — Timeliness requirement.** What timeliness statement did Kofi write? *Rubric:* 3 = feed by 06:00 on at least 95% of days;; 2 = correct;; 1 = partial;; 0 = none.
- **EX062 — Street conflict.** How was the street-level conflict resolved? *Rubric:* 3 = district aggregation with at least fifty properties;; 2 = correct;; 1 = none;; 0 = none.
- **EX063 — Top ranks.** Which requirements ranked highest? *Rubric:* 3 = owner assignment, reconciliation and timeliness;; 2 = most;; 1 = one;; 0 = none.

<a id="ch-22"></a>

## Chapter 22 — Data governance: system and data models

### Learning outcomes

You will (1) model data flows and lineage for an indicator; (2) find ownership gaps from a lineage graph; (3) keep models current.

### 22.1 Modelling the chain

Kofi models the leakage indicator as a directed graph. The board report figure depends on a key performance indicator, which depends on billed volume and supplied volume. Billed volume depends on meter readings and tariffs; meter readings depend in part on manual readings from a field application; supplied volume depends on raw flow sensor data. Each node is a data set or calculation with an owner. The graph makes dependencies explicit, which a written description of the process tends to blur. Nodes are named.

### Lab — Upstream lineage and ownership gaps for the leakage figure

```python
"""Trace upstream lineage of a published figure through a synthetic pipeline graph (stdlib only)."""
edges = {
    "board_report.leakage_pct": ["kpi.leakage"],
    "kpi.leakage": ["billing.volume_billed", "scada.volume_supplied"],
    "billing.volume_billed": ["meters.reading", "customers.tariff"],
    "scada.volume_supplied": ["sensors.flow_raw"],
    "meters.reading": ["field_app.manual_read"],
    "customers.tariff": [], "sensors.flow_raw": [], "field_app.manual_read": [],
}
owners = {"kpi.leakage": "ops analytics", "billing.volume_billed": "billing", "scada.volume_supplied": "network ops",
          "meters.reading": "metering", "customers.tariff": "billing", "sensors.flow_raw": None, "field_app.manual_read": None}
def up(n, seen):
    for p in edges.get(n, []):
        if p not in seen: seen.add(p); up(p, seen)
    return seen
src = up("board_report.leakage_pct", set())
print(f"upstream nodes {len(src)}; sources {sorted(n for n in src if not edges[n])}")
print(f"nodes without an owner: {sorted(n for n in src if owners.get(n) is None)}")
```

Run with `python3 lab_lineage.py`. Verified output:

```text
upstream nodes 7; sources ['customers.tariff', 'field_app.manual_read', 'sensors.flow_raw']
nodes without an owner: ['field_app.manual_read', 'sensors.flow_raw']
```

### 22.2 What the trace shows

Running the lab traces seven upstream nodes behind the board figure. Three are sources with no further inputs: customer tariffs, manual readings from the field application and raw flow sensor data. Two nodes have no owner: the manual readings and the raw sensor flows. Both feed the figure the regulator sees. Kofi notes that the most basic inputs, closest to the physical world, are exactly where ownership is missing, because they sit between engineering teams and nobody claimed them. Kofi reports both gaps.

### 22.3 Closing the gaps

Kofi proposes owners for the two gaps: the metering manager for manual readings and the network operations manager for raw flow data. Each accepts after agreeing what ownership means: approving quality rules, responding to issues within agreed times and signing off changes. He adds owners to the graph and reruns the trace, which now shows no unowned nodes. The rerun becomes a monthly check, since new data sets added to the chain could reopen gaps. Both owners sign a short ownership statement.

### 22.4 Keeping models current

Lineage models age as systems change. Kofi proposes that any change to the leakage pipeline must update the graph in the same release, enforced by a review checklist. He also compares the graph with the warehouse's query logs every quarter to find dependencies that exist in practice but not in the model. Prof. Varga explains that a model which drifts from reality is worse than none, because people trust it and make decisions based on incorrect assumptions. Two such dependencies appear. Both are added promptly.

### Worked example

Kofi models the leakage chain as a graph, traces seven upstream nodes with three sources and two unowned nodes, assigns owners and keeps the model current with release checks and log comparisons.

> **Synthetic case.** The graph is synthetic; outputs come from lab_lineage.py.

### Errors and limits

Static lineage misses runtime dependencies; compare with logs.

### Exercises

- **EX064 — Upstream count.** How many upstream nodes are behind the board figure? *Rubric:* 3 = seven;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX065 — Unowned nodes.** Which nodes had no owner? *Rubric:* 3 = field_app.manual_read and sensors.flow_raw;; 2 = both;; 1 = one;; 0 = none.
- **EX066 — Drift check.** How does Kofi find dependencies missing from the model? *Rubric:* 3 = quarterly comparison with query logs;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-23"></a>

## Chapter 23 — Data governance: threat and failure analysis

### Learning outcomes

You will (1) analyse threats and failure modes affecting governed data; (2) rank them by likelihood and impact; (3) map mitigations to owners.

### 23.1 Failure modes

Kofi runs a failure mode and effects analysis on the leakage chain. For each node he asks how it could fail, what effect the failure would have on the figure and how it would be detected. Failure modes include a stuck flow sensor reporting constant values, a billing extract missing a district, a tariff change applied late and a manual read keyed with a decimal error. Each failure mode receives severity, occurrence and detection scores agreed with the owners concerned. Scores are recorded.

### 23.2 Threats

He adds deliberate threats using NIST SP 800-30r1 as a guide: an insider altering readings to hide a billing error, malware on the control network corrupting sensor data and a vendor employee changing a file format without notice. For each threat he identifies the source, the vulnerability exploited and the impact on the leakage figure. He notes that threats and accidental failures often produce the same symptoms, so detection controls should serve both purposes rather than being designed separately. Each threat has an owner.

### 23.3 Ranking

Kofi ranks the combined list. A stuck flow sensor ranks highest, because it is likely, affects supplied volume directly and could go unnoticed for weeks. Missing billing districts rank second. The insider threat ranks lower in likelihood but high in impact. He shows the ranking to owners, who agree that detection improvements for sensors should be the first investment, since earlier detection reduces the impact of every downstream failure in the chain. The ranking is reviewed again after the first detectors have operated for three months.

### 23.4 Mitigations

Each high-ranked item receives a mitigation and an owner: a flat-line detector on flow sensors owned by network operations, a district completeness check owned by billing and tamper-evident logs for reading edits owned by metering. Kofi records residual risk after each mitigation. Prof. Varga notes that a ranked analysis with named owners is what turns a list of worries into a governance plan, because it says who does what first and how anyone will know whether it worked. Residual risks are reported quarterly.

### Worked example

Kofi analyses failure modes and threats on the leakage chain, ranks a stuck flow sensor highest, and assigns detectors, completeness checks and tamper-evident logs to owners.

> **Synthetic case.** The analysis is synthetic; NIST SP 800-30r1 is real.

### Errors and limits

Scores agreed by one person are guesses; agree them with owners.

### Exercises

- **EX067 — Top risk.** Which failure ranked highest? *Rubric:* 3 = a stuck flow sensor;; 2 = correct;; 1 = other;; 0 = none.
- **EX068 — Shared symptoms.** Why should detection serve threats and failures? *Rubric:* 3 = they often produce the same symptoms;; 2 = correct;; 1 = none;; 0 = none.
- **EX069 — Sensor mitigation.** What mitigation targets stuck sensors? *Rubric:* 3 = a flat-line detector owned by network operations;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-24"></a>

## Chapter 24 — Data governance: methods I

### Learning outcomes

You will (1) choose quality dimensions for the leakage chain; (2) select measurement methods; (3) define thresholds with owners.

### 24.1 Choosing dimensions

Kofi selects quality dimensions from Wang and Strong's framework and Batini's review: completeness, validity, accuracy, timeliness and consistency. For flow sensors, accuracy and completeness matter most. For billing volumes, consistency with meter readings matters most. For the board figure, timeliness and traceability matter. He explains that choosing dimensions per data set avoids measuring everything everywhere, which wastes effort and buries important signals among less important ones. Kofi records the chosen dimensions for each data set in the catalogue, together with a sentence explaining why each one matters to the people who use that data.

### 24.2 Measurement methods

For each dimension he defines a method. Completeness is the share of expected readings received. Validity is the share passing format and range rules. Accuracy for sensors is checked against a portable reference meter during maintenance visits. Consistency compares billed volumes with meter totals. Timeliness is arrival time against the agreed deadline. ISO 8000-8 stresses that quality claims must state how they were measured, so each method is written down alongside its formula. Each formula is also implemented once in the shared library so every team computes it identically.

### 24.3 Thresholds

Kofi agrees thresholds with owners: completeness at least 99 percent per district per day, validity at least 98 percent, sensor accuracy within two percent of the reference and arrival by 06:00 on 95 percent of days. Thresholds are based on the previous year's synthetic performance and the regulator's tolerance. He records that thresholds will be reviewed after six months, because they were set with limited data and may prove too tight or too loose in practice. The review date is entered in the governance calendar so that it is not forgotten.

### 24.4 Method limitations

Each method has limits. Reference meter checks happen only during maintenance, so accuracy is sampled, not continuous. Validity rules catch impossible values but not plausible wrong ones. Kofi lists limitations alongside each method and plans complementary checks, such as comparing neighbouring sensors. Prof. Varga emphasises that stating limitations protects the organisation from overconfidence and helps readers judge how much weight a quality score can bear in a decision. The limitations appear on the dashboard next to each score, so that readers see them at the moment they interpret a figure.

### Worked example

Kofi chooses dimensions per data set, defines measurement methods with formulas, agrees thresholds with owners for six-month review and lists method limitations with complementary checks.

> **Synthetic case.** Thresholds are synthetic; Wang and Strong (1996), Batini et al. (2009) and ISO 8000-8:2015 are real.

### Errors and limits

Thresholds copied from another utility ignore local conditions.

### Exercises

- **EX070 — Sensor dimensions.** Which dimensions matter most for flow sensors? *Rubric:* 3 = accuracy and completeness;; 2 = both;; 1 = one;; 0 = none.
- **EX071 — Accuracy method.** How is sensor accuracy checked? *Rubric:* 3 = against a portable reference meter during maintenance;; 2 = correct;; 1 = none;; 0 = none.
- **EX072 — Validity limit.** What can validity rules not catch? *Rubric:* 3 = plausible but wrong values;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) produce a first design for governed leakage data; (2) present it for critique; (3) revise after feedback.

### 25.1 The brief

The first design studio asks Kofi to produce a governance design for the leakage chain in two weeks: owners, rules, lineage, monitoring and reporting. He works with two classmates who play the roles of network operations and billing owners. The brief requires a one-page summary, a lineage diagram, a rule catalogue and a monitoring dashboard sketch. The studio format mirrors professional practice, where designs are presented to peers and stakeholders before resources are committed to building them. Each student also writes a reflection.

### 25.2 First design

Kofi's design places all rules in a central quality service that every data set passes through. The service records results in one database and feeds a single dashboard. Owners receive daily emails with their figures. He argues that centralisation gives consistency and one place to look. His classmates question whether one service could handle sensor data arriving every minute alongside monthly billing extracts, and whether owners would read daily emails for very long. Kofi notes both questions for the panel and admits he has no answers yet.

### 25.3 Critique

The studio panel, led by Prof. Varga, praises the lineage and ownership work but challenges the central service as a single point of failure. If it stops, no data are checked. They also note that daily emails would quickly be ignored. One panellist suggests running rules close to each source, with results flowing to a shared store, and alerting owners only when thresholds are breached, alongside a weekly summary that shows trends over time. The panel gives written feedback within two days of the session.

### 25.4 Revision

Kofi revises the design: rules run within each pipeline using a shared rule library, results go to a common store, alerts fire only on threshold breaches and owners receive a weekly trend summary. He records the original design, the critique and the reasons for the changes in a decision record. He reflects that the critique improved the design because the panel looked at failure and human behaviour, which he had underweighted while focusing on technical consistency. The panel accepts the revised design at the next session.

### Worked example

Kofi's first centralised design is critiqued as a single point of failure with ignorable emails, and he revises to distributed rules, a common results store, breach alerts and weekly summaries.

> **Synthetic case.** The studio is synthetic.

### Errors and limits

Defending a design instead of listening wastes critique.

### Exercises

- **EX073 — Central weakness.** What weakness did the panel see in the central service? *Rubric:* 3 = single point of failure;; 2 = correct;; 1 = none;; 0 = none.
- **EX074 — Alert change.** How were owner notifications changed? *Rubric:* 3 = alerts only on breaches plus weekly summary;; 2 = correct;; 1 = partial;; 0 = none.
- **EX075 — Underweighted.** What had Kofi underweighted? *Rubric:* 3 = failure and human behaviour;; 2 = both;; 1 = one;; 0 = none.

<a id="ch-26"></a>

## Chapter 26 — Data governance: architecture alternatives

### Learning outcomes

You will (1) compare architectures for governed data; (2) evaluate them against requirements; (3) record the choice.

### 26.1 Three options

Kofi compares three architectures for Tidewater's governed data. A central warehouse with a governance layer holds all curated data in one place. A data mesh gives each domain team responsibility for publishing its data as a product with agreed standards. A hybrid keeps a central warehouse for regulatory reporting while domains own operational data. He describes each option's data flows, ownership model and the controls each would need to satisfy the requirements from chapter 21. Each option is drawn with the same notation for comparison.

### 26.2 Evaluation

He scores each option against the ranked requirements. The central warehouse scores well on consistency and reconciliation but poorly on ownership, because the central team becomes de facto owner. The mesh scores well on ownership but poorly on reconciliation across domains at Tidewater's current maturity. The hybrid scores best overall: regulatory figures stay reconciled centrally, while domain teams own and publish their source data with standard quality rules and metadata. Kofi shows the scoring sheet to owners so they can challenge any score they consider unfair.

### 26.3 Costs and skills

Kofi estimates costs and skills. The mesh requires every domain team to have data engineering skills, which Tidewater lacks outside the analytics team. The hybrid requires training for domain owners and stewards but not new engineering teams. He includes a three-year plan for building skills, after which more responsibility could move to domains. He notes that architecture choices must fit the organisation's capabilities, not just its aspirations, or they fail during implementation. The plan names training courses, mentors and checkpoints at which progress will be reviewed formally.

### 26.4 Recording the choice

Kofi writes an architecture decision record choosing the hybrid, listing the alternatives, scores, costs, risks and conditions for revisiting the decision, such as domain teams reaching agreed skill levels. The governance board approves it. Prof. Varga notes that recording conditions for revisiting a choice keeps architecture decisions alive, since they encourage the organisation to reconsider when circumstances change rather than defending an outdated choice out of habit. The record is stored with the other decision records, and the board diary schedules a review after eighteen months to check whether the conditions have been met.

### Worked example

Kofi compares central, mesh and hybrid architectures, scores them against requirements, chooses the hybrid given Tidewater's skills and records conditions for revisiting the decision.

> **Synthetic case.** Options are synthetic.

### Errors and limits

Fashionable architectures may not fit; score against your requirements.

### Exercises

- **EX076 — Mesh weakness.** Why did the mesh score poorly at Tidewater? *Rubric:* 3 = weak cross-domain reconciliation at current maturity;; 2 = correct;; 1 = none;; 0 = none.
- **EX077 — Chosen option.** Which architecture was chosen? *Rubric:* 3 = the hybrid;; 2 = correct;; 1 = other;; 0 = none.
- **EX078 — Revisit condition.** Give one condition for revisiting the decision. *Rubric:* 3 = domain teams reaching agreed skill levels;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-27"></a>

## Chapter 27 — Data governance: control design

### Learning outcomes

You will (1) design preventive, detective and corrective controls for data; (2) set control ownership; (3) define control evidence.

### 27.1 Control types

Kofi designs controls for the leakage chain in three types. Preventive controls stop bad data entering: schema constraints and input validation in the field application. Detective controls find problems: daily quality rules, flat-line detectors and reconciliation. Corrective controls fix problems: documented procedures for re-requesting files, correcting readings with approval and restating figures. He explains that relying only on detection leaves owners constantly cleaning up, while prevention reduces the volume of problems at their source. Each type has a named owner in the catalogue.

### 27.2 Control catalogue

Each control in the catalogue has an identifier, purpose, type, owner, frequency, evidence produced and linked requirement. For example, control DQ-04 checks district completeness daily, is owned by billing, produces a results table and supports the completeness requirement. The catalogue contains thirty-one controls. He maps them to the risks from chapter 23 and finds that two medium risks have no control, so he designs additional controls for them before implementation begins. The catalogue is stored in the repository and versioned, so every change to a control is traceable.

### 27.3 Evidence

For each control, Kofi defines what evidence shows it operated: stored rule results with timestamps, alert logs, approval records for corrections. He explains that auditors will ask not only whether controls exist, but whether they ran and whether issues were followed up. Evidence that is generated automatically and stored centrally is more reliable than evidence assembled manually before audits, which tends to be incomplete and arrives too late to reveal problems. Kofi configures each control to write its evidence to a shared store with retention of seven years.

### 27.4 Control testing

Kofi plans control testing. Each quarter, a steward tests a sample of controls by introducing synthetic errors into a test environment and confirming that controls detect them and alerts reach owners. Controls that fail testing are fixed and retested. Prof. Varga notes that untested controls provide comfort rather than assurance, and that deliberately injecting errors is one of the few ways to confirm that detective controls work before a real failure relies on them. Test results are reported to the governance board each quarter.

### Worked example

Kofi designs preventive, detective and corrective controls, builds a thirty-one-control catalogue, fills two gaps, defines automatic evidence and plans quarterly error-injection tests.

> **Synthetic case.** Controls are synthetic.

### Errors and limits

Controls without evidence cannot be shown to work.

### Exercises

- **EX079 — Corrective example.** Give one corrective control. *Rubric:* 3 = re-requesting files, approved corrections or restating figures;; 2 = correct;; 1 = none;; 0 = none.
- **EX080 — Catalogue size.** How many controls are in the catalogue? *Rubric:* 3 = thirty-one;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX081 — Testing method.** How are controls tested each quarter? *Rubric:* 3 = injecting synthetic errors in test;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-28"></a>

## Chapter 28 — Data governance: implementation I

### Learning outcomes

You will (1) implement data quality rules in code; (2) measure pass rates; (3) interpret combined results.

### 28.1 The rule library

Kofi implements the first quality rules in a shared library used by every pipeline. Each rule is a function with an identifier, description, owner and threshold read from configuration. The first three rules check that a meter identifier is present, that a reading is not below the previous reading for the same meter and that daily use is under 300 cubic metres, an implausible amount for any domestic or small business customer in Tidewater's area. Every rule is also documented in the catalogue.

### Lab — Pass rates for three meter reading rules on 10,000 synthetic rows

```python
"""Run validation rules on synthetic meter readings and report pass rates (stdlib only)."""
import random
random.seed(8)
rows = []
for i in range(10000):
    prev = random.uniform(100, 5000); cur = prev + random.uniform(0, 60)
    if random.random() < 0.02: cur = prev - random.uniform(1, 50)        # rollback
    if random.random() < 0.01: cur = prev + random.uniform(500, 2000)    # spike
    mid = f"M{i:06d}" if random.random() > 0.005 else ""
    rows.append((mid, prev, cur))
rules = {
    "meter id present": lambda r: bool(r[0]),
    "reading not below previous": lambda r: r[2] >= r[1],
    "daily use under 300 m3": lambda r: r[2] - r[1] < 300,
}
for name, f in rules.items():
    ok = sum(1 for r in rows if f(r)); print(f"{name:28s} pass {ok/len(rows):.3f}")
allok = sum(1 for r in rows if all(f(r) for f in rules.values()))
print(f"rows passing all rules {allok} of {len(rows)} ({100*allok/len(rows):.1f}%)")
```

Run with `python3 lab_rules.py`. Verified output:

```text
meter id present             pass 0.995
reading not below previous   pass 0.980
daily use under 300 m3       pass 0.990
rows passing all rules 9650 of 10000 (96.5%)
```

### 28.2 Running the rules

The lab runs the rules on 10,000 synthetic readings. The meter identifier rule passes 99.5 percent of rows, the not-below-previous rule 98.0 percent and the daily use rule 99.0 percent. Rows passing all three rules number 9,650, or 96.5 percent. Kofi notes that the combined rate is lower than any single rate, because failures fall on different rows. Owners see their own rule rates, but the combined figure is what billing actually receives. Kofi therefore asks the dashboard to show the all-rules figure prominently, with the individual rule rates shown underneath for owners who need to investigate their own failures.

### 28.3 Interpreting failures

Kofi examines failures. Readings below the previous value come mainly from meter replacements, where the new meter starts at zero. That is not an error in the reading but a missing link between old and new meters. He works with metering to record replacements so the rule can compare readings from the same meter only. Missing identifiers come from manual reads keyed without scanning, which the field application will now prevent by requiring a scan. Both fixes are scheduled for the next release.

### 28.4 Against thresholds

Compared with the thresholds agreed in chapter 24, validity at 96.5 percent falls short of the 98 percent target. Kofi reports this honestly to the governance board with the causes found and the fixes planned, estimating that the replacement fix alone would raise the combined pass rate above target. Prof. Varga notes that reporting a miss with a credible plan builds more trust than adjusting thresholds downward to make figures look acceptable. The board accepts the plan and asks for an update after the next release, with the rates recalculated on fresh data.

### Worked example

Kofi implements a shared rule library, runs three rules on 10,000 rows with pass rates of 99.5, 98.0 and 99.0 percent and 96.5 percent passing all, traces causes and reports the miss against target.

> **Synthetic case.** Data are synthetic; outputs come from lab_rules.py.

### Errors and limits

Averaging rule rates overstates quality; report the all-rules rate.

### Exercises

- **EX082 — All-rules rate.** What share of rows passed all rules? *Rubric:* 3 = 96.5% (9,650 of 10,000);; 2 = correct;; 1 = partial;; 0 = none.
- **EX083 — Below-previous cause.** What mainly caused readings below the previous value? *Rubric:* 3 = meter replacements starting at zero;; 2 = correct;; 1 = none;; 0 = none.
- **EX084 — Miss handling.** How did Kofi handle missing the target? *Rubric:* 3 = reported it honestly with causes and fixes;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-29"></a>

## Chapter 29 — Data governance: measurement

### Learning outcomes

You will (1) measure timeliness against a service level; (2) find patterns in breaches; (3) report service performance.

### 29.1 The service level

The daily supplied-volume feed must reach the warehouse by 06:00 so the morning leakage view is ready for network engineers. Kofi measures arrival times over ninety synthetic days. He records the time each feed lands and compares it with the deadline. He explains that a service level is only useful if it is measured continuously and reported to both the supplier and the consumer, so each side knows whether the agreement is being kept. The supplier here is network operations. It runs the export job each morning.

### Lab — Feed arrivals against a 06:00 service level over 90 synthetic days

```python
"""Measure daily feed timeliness against a 06:00 service level over 90 synthetic days (stdlib only)."""
import random
random.seed(19)
arr = [random.gauss(5.2, 0.6) + (1.5 if 40 <= d < 47 else 0) for d in range(90)]   # hours after midnight
late = [d for d, a in enumerate(arr) if a > 6.0]
print(f"days {len(arr)}; feed after 06:00 on {len(late)} days ({100*len(late)/len(arr):.1f}%)")
print(f"late days in the week 40-46: {sum(1 for d in late if 40 <= d < 47)} of 7")
```

Run with `python3 lab_sla.py`. Verified output:

```text
days 90; feed after 06:00 on 11 days (12.2%)
late days in the week 40-46: 7 of 7
```

### 29.2 Results

The lab shows the feed arrived after 06:00 on 11 of 90 days, or 12.2 percent. The service level target is 95 percent on time, which allows about four or five late days; Tidewater achieved 87.8 percent. All seven days in the week from day 40 to day 46 were late. The other four late days were scattered. Kofi notes that a single summary figure hides this pattern, which points to a specific event rather than general slowness. Kofi plots the daily arrival times so that the cluster is visible at a glance to every reader.

### 29.3 Finding the cause

Kofi investigates the late week with network operations. During that week, a control system upgrade added a backup job that ran before the export, delaying the feed by about an hour and a half every day. Nobody connected the upgrade to the late feed because the warehouse team was not told about the change. He recommends that changes affecting the export schedule notify the data owner, and that the upgrade's backup job be moved. The backup job is rescheduled to after the export.

### 29.4 Reporting service

Kofi designs a monthly service report showing on-time percentage, a daily arrival chart with the deadline marked, clusters of breaches and causes found. The report goes to the network operations owner and the data consumers. Prof. Varga notes that showing the daily chart rather than only the percentage lets readers see patterns themselves, and that service reports should explain breaches rather than merely count them, since counting alone gives no basis for improvement. The first report is discussed at the monthly operations meeting.

### Worked example

Kofi measures 11 late days of 90 (12.2 percent), with all seven late in week 40 to 46, traces them to an upgrade's backup job and designs a monthly service report with a daily chart.

> **Synthetic case.** Arrivals are synthetic; outputs come from lab_sla.py.

### Errors and limits

Averages hide clusters; plot daily values.

### Exercises

- **EX085 — Late share.** On what share of days was the feed late? *Rubric:* 3 = 12.2% (11 of 90);; 2 = correct;; 1 = partial;; 0 = none.
- **EX086 — Cluster cause.** What caused the late week? *Rubric:* 3 = an upgrade's backup job running before the export;; 2 = correct;; 1 = none;; 0 = none.
- **EX087 — Scattered days.** How many late days fell outside that week? *Rubric:* 3 = four;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify that implemented controls meet requirements; (2) use synthetic error injection; (3) report verification results.

### 30.1 Verification plan

The first verification laboratory checks whether the controls implemented so far meet the requirements from chapter 21. Kofi writes a plan listing each requirement, the control that should satisfy it, the test method and the pass criterion. For example, the completeness requirement is verified by removing one district from a synthetic billing extract and confirming that control DQ-04 raises an alert within an hour. The plan is reviewed by Prof. Varga before testing begins. Each test has a pass criterion agreed in advance.

### 30.2 Error injection

Kofi prepares a synthetic dataset with known errors: missing districts, readings below previous values, negative flows, a stuck sensor and a file with swapped columns. He runs the pipeline and records which controls detect which errors. Of twelve injected errors, ten are detected. The stuck sensor is missed because the flat-line detector needs six hours of constant values and the injection lasted four. The swapped columns pass because both columns hold plausible numbers. Kofi records both misses in the test log. Both are investigated.

### 30.3 Responding to misses

For the stuck sensor, Kofi discusses with network operations whether four hours of constant flow is suspicious. They agree that for large mains it is, and reduce the window for those sensors to three hours. For swapped columns, he adds a check that compares each column's distribution with its history, which would flag reversed values. He reruns the injection, and all twelve errors are detected. Each change is recorded in the control catalogue with its reason. Both owners approve both changes in writing, with dates.

### 30.4 Verification report

The report lists requirements, controls, tests, results before and after changes and remaining limitations. Kofi notes that verification shows controls work on known errors, not that they catch every possible problem. Prof. Varga explains that verification answers whether we built the controls right, while validation, later in the course, asks whether we built the right controls for the people who rely on the leakage figure. The report is filed with the control catalogue and becomes the baseline against which the second verification laboratory will later compare its own results.

### Worked example

Kofi injects twelve errors, detects ten, shortens the flat-line window for large mains, adds distribution checks for swapped columns, reruns with all twelve detected and reports limitations.

> **Synthetic case.** The laboratory is synthetic.

### Errors and limits

Passing injected tests does not prove completeness; state limits.

### Exercises

- **EX088 — Detection count.** How many injected errors were detected at first? *Rubric:* 3 = ten of twelve;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX089 — Swapped fix.** What check catches swapped columns? *Rubric:* 3 = comparing each column's distribution with history;; 2 = correct;; 1 = none;; 0 = none.
- **EX090 — Verification versus validation.** What does verification answer? *Rubric:* 3 = whether controls were built right;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-31"></a>

## Chapter 31 — Data governance: implementation II

### Learning outcomes

You will (1) implement metadata and catalogue entries for governed data; (2) automate ownership and classification; (3) make governance visible to users.

### 31.1 The catalogue

Kofi implements a data catalogue for the leakage chain. Each data set has an entry with its description, owner, steward, classification, quality rules, lineage links, refresh schedule and retention period. He populates entries for the seven upstream nodes and the board figure, then adds the source systems. Users searching for supplied volume now find one authoritative entry instead of several similar tables with unclear differences. He explains that a catalogue turns governance decisions into information people meet when they actually look for data.

### 31.2 Automating metadata

Manual catalogue entries go stale. Kofi automates what he can: schema details, refresh times and quality results are pulled from the warehouse and rule library each night. Owners and descriptions remain manual but are checked for staleness; entries not reviewed in a year are flagged to stewards. He notes that automation keeps technical facts accurate while human review keeps meaning accurate, and that the two need different maintenance processes because they change for different reasons and at different speeds. Stewards clear flagged entries monthly.

### 31.3 Classification in practice

Each data set is classified as public, internal, confidential or restricted. Customer billing volumes are confidential; the priority services register is restricted. Kofi links classifications to warehouse access policies, so changing a classification changes who can read the data without separate requests. When an analyst creates a derived table joining confidential billing data, the classification is inherited automatically. He tests inheritance with synthetic tables to confirm that derived data never receive a lower classification than their inputs. Access requests fall because permissions follow classification.

### 31.4 Visible governance

Kofi adds quality badges to catalogue entries showing the latest all-rules pass rate and service level performance. Users can see whether a data set is currently trustworthy before using it. Network engineers begin checking badges before planning repairs, and ask owners about poor scores. Prof. Varga observes that visibility creates healthy pressure, because owners prefer to fix problems rather than have colleagues see persistent poor scores, and users gain the information they need to judge suitability. Badges link to the rule descriptions behind each score.

### Worked example

Kofi builds catalogue entries for the leakage chain, automates technical metadata with stale-entry checks, links classification to access with inheritance and adds quality badges that engineers consult.

> **Synthetic case.** The catalogue is synthetic.

### Errors and limits

Badges can mislead if rules are weak; link to rule descriptions.

### Exercises

- **EX091 — Automated fields.** Which metadata are pulled automatically? *Rubric:* 3 = schema details, refresh times and quality results;; 2 = most;; 1 = one;; 0 = none.
- **EX092 — Inheritance rule.** What classification does a derived table get? *Rubric:* 3 = never lower than its inputs;; 2 = correct;; 1 = none;; 0 = none.
- **EX093 — Badge effect.** How did badges change engineers' behaviour? *Rubric:* 3 = they check badges and ask owners about poor scores;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-32"></a>

## Chapter 32 — Data governance: reliability

### Learning outcomes

You will (1) reconcile data across systems; (2) quantify reconciliation gaps; (3) assign and track reconciliation breaks.

### 32.1 Why reconcile

The leakage figure subtracts billed volume from supplied volume. If billing misses meter readings, billed volume falls and leakage appears higher than it really is. Kofi reconciles field meter readings with readings recorded in billing to measure how reliably data pass from one system to the other. Reconciliation is one of the oldest data controls, used in accounting long before computers, and it remains effective because it compares independent records of the same facts rather than trusting either one. Kofi runs it monthly.

### Lab — Reconciling 8,000 field reads with billing records

```python
"""Reconcile monthly meter reads between field app and billing system (stdlib only)."""
import random
random.seed(27)
field = {f"M{i:05d}": round(random.uniform(10, 40), 1) for i in range(8000)}
billing = dict(field)
for k in random.sample(list(field), 120): del billing[k]                    # lost in transfer
for k in random.sample(list(billing), 60): billing[k] = round(billing[k] * 10, 1)  # unit error
missing = [k for k in field if k not in billing]
mismatch = [k for k in billing if abs(billing[k] - field[k]) > 0.05]
print(f"field reads {len(field)}; missing in billing {len(missing)}; value mismatches {len(mismatch)}")
print(f"reconciled share {100*(len(field)-len(missing)-len(mismatch))/len(field):.2f}%")
```

Run with `python3 lab_reconcile.py`. Verified output:

```text
field reads 8000; missing in billing 120; value mismatches 60
reconciled share 97.75%
```

### 32.2 Reconciliation results

The lab compares eight thousand synthetic field reads with billing. One hundred and twenty reads are missing from billing entirely, and sixty appear with a different value. The reconciled share, reads present with matching values, is 97.75 percent. Kofi explains that the two kinds of breaks have different causes and owners: missing reads usually come from transfer failures, while value mismatches usually come from manual corrections in billing that were not applied back to the meter data store. Each break type is counted separately.

### 32.3 Effect on leakage

Kofi estimates the effect of missing reads on the leakage figure. Because each missing read lowers billed volume, leakage is overstated. He calculates the volume associated with the missing reads in the synthetic data and shows that it shifts district leakage upward noticeably in the two districts with the most breaks. This explains why those districts appeared to be leaking more than neighbouring districts with similar pipes, and prevents repair crews being sent to the wrong places. The corrected figures are shared with planners.

### 32.4 Tracking breaks

Each break becomes a record with an owner, cause and status. Transfer failures go to the integration team; mismatches go to billing. Kofi sets a target to resolve breaks within ten working days and reports ageing weekly. Breaks older than the target are escalated to the governance board. Prof. Varga explains that reconciliation without break tracking measures problems without fixing them, and that ageing reports show whether teams are keeping up or falling behind. The first ageing report shows most breaks are closed within target.

### Worked example

Kofi reconciles 8,000 field reads, finding 120 missing in billing and 60 mismatches for 97.75 percent reconciled, links breaks to overstated leakage and tracks breaks by owner and age.

> **Synthetic case.** Reads are synthetic; outputs come from lab_reconcile.py.

### Errors and limits

Reconciling a system with itself proves nothing; use independent records.

### Exercises

- **EX094 — Reconciled share.** What share of reads reconciled? *Rubric:* 3 = 97.75%;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX095 — Missing reads effect.** How do missing reads affect leakage? *Rubric:* 3 = they overstate it;; 2 = correct;; 1 = understate;; 0 = none.
- **EX096 — Mismatch owner.** Who owns value mismatches? *Rubric:* 3 = billing;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-33"></a>

## Chapter 33 — Data governance: safety and resilience

### Learning outcomes

You will (1) relate data governance to physical safety; (2) design resilient data supply for operations; (3) plan for degraded modes.

### 33.1 Data and safety

Some Tidewater data affect physical safety. Pressure and flow readings guide decisions on valve operations; chlorine readings protect public health. Kofi distinguishes these safety-relevant data from business data. Changes to their quality rules, sources or processing require review by the operations safety engineer as well as the data owner. He explains that a governance process designed for billing data, where errors can be corrected later, is not adequate for data whose errors could lead to unsafe actions. Kofi lists these data sets explicitly.

### 33.2 Resilient supply

Operators need sensor data during incidents, when networks and systems are stressed. Kofi reviews the resilience of the sensor data supply: redundant communication paths for critical sites, local displays at treatment works and a second historian server in a separate building. He finds that the leakage dashboard depends on a single warehouse server, which is acceptable for planning but not for incident response. He recommends that incident response never depend on the analytics platform for critical readings. Operators approve the recommendation in writing.

### 33.3 Degraded modes

Kofi writes procedures for degraded modes: what operators do when sensor data are missing, delayed or suspected wrong. Procedures include using manual readings from site staff, comparing with neighbouring sensors and marking decisions made on degraded data in the operations log. He tests the procedures in a tabletop exercise with operators, who point out that manual readings need standard forms and units to be usable, which he adds to the procedure. A second exercise with the revised forms goes smoothly, and operators keep copies in the control room.

### 33.4 Learning from incidents

After each operational incident, Kofi proposes a data review asking whether data contributed, whether data quality controls detected problems and whether degraded mode procedures worked. Findings feed back into controls and procedures. Prof. Varga relates this to safety engineering practice, where learning from incidents without blame is essential, and notes that data governance in safety contexts must borrow these practices rather than relying solely on compliance checks. The first such review, after a burst main, finds that a pressure sensor alarm was ignored because it had fired falsely many times before.

### Worked example

Kofi separates safety-relevant data with extra review, assesses resilient sensor supply, writes and tests degraded-mode procedures and adds data reviews after incidents.

> **Synthetic case.** The scenarios are synthetic.

### Errors and limits

Treating safety data like business data underestimates harm.

### Exercises

- **EX097 — Extra reviewer.** Who else reviews changes to safety-relevant data? *Rubric:* 3 = the operations safety engineer;; 2 = correct;; 1 = none;; 0 = none.
- **EX098 — Dashboard dependency.** Why must incident response not rely on the leakage dashboard? *Rubric:* 3 = it depends on a single warehouse server;; 2 = correct;; 1 = none;; 0 = none.
- **EX099 — Tabletop finding.** What did operators point out? *Rubric:* 3 = manual readings need standard forms and units;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-34"></a>

## Chapter 34 — Data governance: integration

### Learning outcomes

You will (1) integrate governance controls across teams and systems; (2) manage change across interfaces; (3) test end to end.

### 34.1 Bringing pieces together

By this point Kofi has owners, rules, lineage, catalogue entries, reconciliation and service reporting, built in different systems by different teams. Integration means ensuring they work together: rule failures appear in the catalogue badges, lineage links to owners, reconciliation breaks reach the right queues and service reports include causes from incident reviews. He builds an integration map showing every connection between governance components and the system that implements each one. The map shows which connections are automatic and which depend on a person remembering a manual step, and those manual steps become candidates for automation.

### 34.2 Change across interfaces

Kofi introduces a change notice process for interfaces in the leakage chain. Any team changing a field, schedule or format must notify affected owners two weeks in advance, with a test file. When the metering vendor plans a firmware update that changes timestamp precision, the notice allows billing to adjust its parser before the change goes live. Previously such changes were discovered only after failures, when readings had already been lost or misassigned. The vendor accepts the process and nominates a contact for notices.

### 34.3 End-to-end testing

Kofi designs an end-to-end test that pushes a synthetic day of data from simulated meters and sensors through every system to the leakage figure. The test checks that expected values appear at each stage, that controls fire on injected errors and that catalogue badges update. The first run reveals that reconciliation results reach the break queue but not the catalogue, so the badge shows stale figures. He fixes the connection and reruns the test successfully. The test now runs after every release automatically.

### 34.4 Integration ownership

Kofi notes that integration problems sit between teams, so nobody owns them by default. He proposes that the data governance lead owns the end-to-end test and integration map, with each team owning its components. Prof. Varga explains that integration ownership prevents the common failure where every component works in isolation but the whole fails, and that someone must be accountable for how pieces work together across organisational lines. The governance board confirms this assignment and adds the end-to-end test result to its monthly dashboard of governance health.

### Worked example

Kofi maps connections between governance components, introduces change notices that catch a timestamp change, builds an end-to-end test that finds a stale badge and assigns integration ownership.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

Component tests passing does not mean the system works.

### Exercises

- **EX100 — Notice period.** How much notice do interface changes need? *Rubric:* 3 = two weeks with a test file;; 2 = correct;; 1 = partial;; 0 = none.
- **EX101 — End-to-end finding.** What did the first end-to-end run reveal? *Rubric:* 3 = reconciliation results did not reach the catalogue;; 2 = correct;; 1 = none;; 0 = none.
- **EX102 — Integration owner.** Who owns the end-to-end test? *Rubric:* 3 = the data governance lead;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design governance for a new data source; (2) apply lessons from the first studio; (3) defend the design under questioning.

### 35.1 The new source

The second design studio introduces a new data source: acoustic loggers that listen for leaks on pipes and send daily noise summaries. Tidewater plans to install two thousand loggers. Kofi must design governance for the logger data, including owners, rules, lineage into the leakage process, privacy considerations and retention. The brief requires the design to reuse existing components where possible and to justify any new ones, reflecting the lesson that governance should scale without rebuilding everything. The installation is planned over two years.

### 35.2 Reusing components

Kofi reuses the rule library for range and completeness checks, the catalogue for metadata, the change notice process for the vendor interface and the reconciliation pattern to compare logger alerts with confirmed leaks found by repair crews. He adds one new component: a model card describing how the vendor's algorithm turns noise into leak probability, including its known false positive rate. He explains that algorithmic outputs need their own documentation because their quality depends on training data users cannot see. The vendor supplies the rate.

### 35.3 Privacy questions

Loggers placed on pipes outside homes might capture sounds beyond pipe noise. Kofi checks the vendor specification and confirms the device records only frequency summaries, not audio. He records this in the data protection assessment and requires the vendor to notify any change that would capture audio. The panel questions whether summaries could reveal household activity patterns. He concedes the possibility for loggers near single homes and proposes aggregating daily summaries before analysts see them. The panel accepts this proposal with a review clause.

### 35.4 Defending the design

The panel tests Kofi's design with scenarios: a firmware update increases false positives, loggers in one district stop reporting and a journalist asks whether Tidewater listens to homes. He answers each using the components and records in his design. The panel notes improvement over the first studio, particularly in anticipating failure and people's concerns. Prof. Varga comments that the best designs show their reasoning, so reviewers can test them rather than simply trust the designer. The panel approves the design with minor wording changes requested.

### Worked example

Kofi designs governance for acoustic loggers by reusing rules, catalogue, notices and reconciliation, adds a model card, addresses privacy with summaries and aggregation and defends the design under scenarios.

> **Synthetic case.** The loggers are synthetic.

### Errors and limits

Vendor assurances need verification; check specifications.

### Exercises

- **EX103 — New component.** What new component did Kofi add? *Rubric:* 3 = a model card for the leak algorithm;; 2 = correct;; 1 = none;; 0 = none.
- **EX104 — Audio check.** Do the loggers record audio? *Rubric:* 3 = no, only frequency summaries;; 2 = correct;; 1 = yes;; 0 = none.
- **EX105 — Panel praise.** What improvement did the panel note? *Rubric:* 3 = anticipating failure and people's concerns;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-36"></a>

## Chapter 36 — Data governance: performance and scale

### Learning outcomes

You will (1) keep governance controls efficient as data grow; (2) measure control cost; (3) prioritise controls by value.

### 36.1 Growth

Smart meter readings grow from daily to hourly as Tidewater upgrades meters, multiplying volume by twenty-four. Acoustic loggers add more. Kofi estimates that the rule library would take far longer each night at the new volume if run unchanged. He explains that governance controls are workloads with costs, and that designs which work at today's scale may fail when volumes increase, causing late checks or skipped controls that undermine the whole governance approach. Kofi presents the estimate before the meter upgrade begins, so that changes are ready in time.

### 36.2 Making controls efficient

Kofi changes rules to process only new and changed records rather than full histories, partitions data by district so checks run in parallel and moves simple range checks into the ingestion step where data are already being read. He measures runtime on a synthetic dataset at the new volume and confirms the nightly checks now finish well before the morning deadline. He documents the design choices so later engineers understand why checks are structured this way. Range checks at ingestion also reject bad readings sooner.

### 36.3 Control cost

Kofi records the computing cost and staff time of each control. A detailed distribution comparison on every column costs far more than its findings justify for low-risk tables. He proposes risk-based frequency: high-risk data checked continuously, medium-risk daily and low-risk weekly. The governance board approves the approach. He notes that governance competes for resources with other work, so showing value for cost helps sustain support from managers who must fund it. Each data set's risk level is recorded in the catalogue, so the schedule follows automatically from the classification.

### 36.4 Value of controls

To prioritise, Kofi lists for each control the problems it detected over six months and their impact. Some controls found nothing, which could mean the risk is absent or the control is weak. He tests silent controls by injection before retiring any, and retires two that duplicate stronger checks. Prof. Varga stresses that controls which never fire should be tested rather than assumed useless, since silence can reflect success or failure. The remaining silent controls stay in place, because injection showed that each still detects the errors it was designed to catch.

### Worked example

Kofi prepares controls for hourly meter data with incremental, partitioned and early checks, records control costs, applies risk-based frequency and tests silent controls before retiring duplicates.

> **Synthetic case.** Volumes are synthetic.

### Errors and limits

Retiring silent controls without testing them may remove needed protection.

### Exercises

- **EX106 — Volume growth.** By how much does hourly reading multiply volume? *Rubric:* 3 = twenty-four times;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX107 — Efficiency change.** Name one efficiency change. *Rubric:* 3 = incremental processing, district partitions or ingestion checks;; 2 = one;; 1 = none;; 0 = none.
- **EX108 — Silent controls.** What did Kofi do before retiring silent controls? *Rubric:* 3 = tested them by injection;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-37"></a>

## Chapter 37 — Data governance: operations

### Learning outcomes

You will (1) run governance as daily operations; (2) handle data incidents; (3) maintain runbooks and on-call.

### 37.1 Daily operations

Governance needs routines. Kofi defines a daily cycle: overnight controls run, alerts reach owners by seven in the morning, stewards triage alerts by nine and the morning leakage view publishes with quality badges. Weekly, owners review trends and break ageing. Monthly, the governance board reviews service reports and decisions. He documents the cycle in an operations calendar so everyone knows when to expect information and when they must act on it. The calendar is shared with all owners and stewards, and reminders are sent automatically before each review meeting.

### 37.2 Data incidents

A data incident is an event where data quality or availability falls badly enough to affect decisions. Kofi defines severity levels, from a single district's missing data to a wrong leakage figure sent to the regulator. Each level has response times, communication rules and a lead. When a billing extract fails on a reporting day, the incident lead informs the regulator's contact that figures will be a day late rather than sending estimated numbers silently. The regulator's contact thanks Tidewater for the early warning.

### 37.3 Runbooks

For common alerts Kofi writes runbooks: step-by-step guides covering how to confirm the problem, likely causes, fixes and who to inform. The runbook for a stuck flow sensor explains how to compare with neighbouring sensors, request a site visit and mark affected data. He tests runbooks by asking a steward who did not write them to follow each one with a synthetic incident, revising steps that cause confusion during the test. Runbooks are stored next to the alerts they cover, so the link appears in each alert message.

### 37.4 On-call

Data alerts can occur at night. Kofi proposes an on-call rota among data engineers for critical data such as the safety-relevant sensor feeds, with clear escalation to operations engineers. Non-critical alerts wait until morning. He reviews alert volumes to ensure on-call staff are not woken for issues that could wait. Prof. Varga notes that sustainable operations require attention to staff workload, because exhausted on-call engineers make mistakes and leave. Alert thresholds that wake staff unnecessarily are adjusted after each monthly review of night-time alerts and their outcomes.

### Worked example

Kofi sets daily, weekly and monthly governance routines, defines data incident severity with regulator communication, tests runbooks with a steward and designs a sustainable on-call rota.

> **Synthetic case.** Operations are synthetic.

### Errors and limits

Sending estimates silently damages trust; communicate delays.

### Exercises

- **EX109 — Triage time.** By when do stewards triage alerts? *Rubric:* 3 = nine in the morning;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX110 — Reporting-day failure.** What did the incident lead do when an extract failed on reporting day? *Rubric:* 3 = told the regulator figures would be a day late;; 2 = correct;; 1 = none;; 0 = none.
- **EX111 — Runbook test.** How are runbooks tested? *Rubric:* 3 = a steward who did not write them follows them on a synthetic incident;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-38"></a>

## Chapter 38 — Data governance: validation

### Learning outcomes

You will (1) validate governance with the people who use the data; (2) gather evidence of usefulness; (3) adjust based on findings.

### 38.1 Validation questions

Verification showed controls work as designed; validation asks whether the design serves users. Kofi interviews network engineers, billing analysts, the regulatory reporting manager and two operations staff. He asks whether they trust the leakage figure more than a year ago, whether badges and alerts help their work and what still causes problems. He also reviews whether repair crews found leaks in the districts that the improved figure prioritised, which is an outcome measure. Interviews follow a written guide so answers can be compared fairly.

### 38.2 Findings

Users report more trust, citing badges and reconciliation. Network engineers say district leakage now matches field experience better. However, billing analysts find some alerts confusing because rule names are technical. Operations staff rarely use the catalogue, preferring to call colleagues. Repair crews found confirmed leaks at a higher rate in prioritised districts than before, though Kofi notes other changes, such as new crews, may also explain some of the improvement. Kofi reports these findings to the governance board, including the negative ones, so that the picture is balanced and credible.

### 38.3 Adjustments

Kofi rewrites alert messages in plain language with suggested actions. For operations staff, he adds key catalogue information to the control room display they already use instead of expecting them to visit the catalogue. He plans a follow-up review in six months. He notes that validation sometimes shows that good controls go unused because they do not fit how people work, and that adapting delivery can matter as much as improving controls. Billing analysts confirm that the rewritten alerts are much easier to act on.

### 38.4 Evidence of value

Kofi compiles validation evidence for the governance board: interview themes, the leak confirmation comparison with its caveats and usage of badges and catalogue. Prof. Varga reminds him to separate what users said from what was measured, and to avoid claiming that governance caused the improvement in leak finding without stronger evidence. The board accepts the evidence as encouraging and asks for a better comparison design in the next year. Kofi agrees to work with the analytics team on a comparison that accounts for crew changes and seasonal patterns.

### Worked example

Kofi interviews users and checks leak confirmations, finds more trust but confusing alerts and unused catalogue, rewrites alerts, brings information to control room displays and reports evidence with caveats.

> **Synthetic case.** Interviews and outcomes are synthetic.

### Errors and limits

User satisfaction alone does not show effectiveness; combine with outcome measures.

### Exercises

- **EX112 — Billing complaint.** What confused billing analysts? *Rubric:* 3 = technical rule names in alerts;; 2 = correct;; 1 = none;; 0 = none.
- **EX113 — Operations fix.** How did Kofi reach operations staff? *Rubric:* 3 = key catalogue information on the control room display;; 2 = correct;; 1 = none;; 0 = none.
- **EX114 — Causal caution.** What did Prof. Varga warn against? *Rubric:* 3 = claiming governance caused better leak finding without stronger evidence;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-39"></a>

## Chapter 39 — Data governance: maintainability

### Learning outcomes

You will (1) keep governance sustainable as people and systems change; (2) manage knowledge transfer; (3) retire obsolete controls and data.

### 39.1 People change

Owners and stewards move jobs. Kofi finds that when the billing steward left, nobody updated tariff reference data for two months. He proposes handover checklists for governance roles, deputies for each owner and steward and an annual confirmation that role holders still hold their roles. Ownership records in the catalogue are linked to the staff directory, so leavers trigger a reminder to the governance lead to assign a successor. Deputies attend the monthly owner reviews, so they already understand current issues when they need to take over a role.

### 39.2 Knowledge transfer

Much governance knowledge sits in people's heads: why a threshold was set, which vendor contact actually fixes problems. Kofi encourages owners to write short notes in decision records and runbooks. He runs a session where outgoing and incoming stewards walk through open breaks together. He explains that maintainable governance depends on recorded reasons, since new staff otherwise either undo sensible choices or preserve outdated ones without knowing why they exist. The session is recorded in notes and repeated whenever a steward role changes hands.

### 39.3 Retiring things

Data sets and controls that are no longer needed still cost effort and carry risk. Kofi introduces an annual review of catalogue entries, retiring data sets with no recent use after checking with owners and applying retention rules. He finds old extracts containing customer details last used years ago and arranges their deletion with records of approval. Retiring controls follows the injection test approach from earlier chapters. The review also finds three tables that nobody can explain, which are archived and flagged until an owner is identified or they can be deleted.

### 39.4 Sustaining effort

Kofi measures governance effort: hours spent by owners and stewards each month. He finds effort concentrated in a few people, which risks burnout and single points of failure. He proposes spreading steward duties and automating repetitive checks. Prof. Varga notes that governance often fails not through bad design but through fatigue, as enthusiastic early participants tire, and that sustainable effort must be planned as deliberately as any control. The governance board agrees to include steward time in job plans, so that the work is recognised rather than done on top of other duties.

### Worked example

Kofi adds handover checklists, deputies and directory links, records reasons for knowledge transfer, retires old extracts with approval and spreads steward effort to prevent fatigue.

> **Synthetic case.** Roles are synthetic.

### Errors and limits

Governance relying on a few enthusiasts is fragile; plan for turnover.

### Exercises

- **EX115 — Steward departure.** What happened when the billing steward left? *Rubric:* 3 = tariff reference data went unupdated for two months;; 2 = correct;; 1 = none;; 0 = none.
- **EX116 — Leaver trigger.** What triggers successor assignment? *Rubric:* 3 = directory links that remind the governance lead;; 2 = correct;; 1 = none;; 0 = none.
- **EX117 — Effort risk.** What risk did concentrated effort create? *Rubric:* 3 = burnout and single points of failure;; 2 = both;; 1 = one;; 0 = none.

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) re-verify the governed chain after changes; (2) compare with the first laboratory; (3) report residual gaps.

### 40.1 Scope

The second verification laboratory repeats the first one's tests and adds new ones for components built since: catalogue inheritance, reconciliation break routing, change notices, degraded modes and logger data rules. Kofi updates the verification plan with each requirement, control, test and pass criterion. He also includes tests for the hourly data volume, since performance changes could cause controls to miss their deadlines and therefore fail even though their logic is correct. Kofi also adds an inventory of every tool that can read or write governed data, which becomes part of the plan.

### 40.2 Results

All twelve original injected errors are detected, confirming the fixes from the first laboratory remain effective. Of the new tests, most pass. Two fail: a derived table created through a rarely used tool did not inherit classification, and a degraded mode alert reached the wrong team because of an outdated contact list. Performance tests show checks complete before the deadline at hourly volume, with room for growth. Kofi notes that both failures involve parts of the system that were added or changed outside the main release process, which suggests a review step is missing there.

### 40.3 Fixing gaps

Kofi works with the warehouse team to apply classification inheritance to the rarely used tool, and replaces the contact list with links to the on-call rota. He reruns both tests successfully. He notes that both failures came from components outside the main path, which tests often miss, and recommends that future verification include an inventory of all tools and contact points that touch governed data. The inventory is built during the laboratory and finds two further tools, a reporting add-in and an export utility, which are added to the test plan and pass their tests.

### 40.4 Comparison and report

The report compares the first and second laboratories: more requirements covered, more controls, fewer failures relative to tests and faster fixes. It lists residual gaps, such as limited testing of the logger algorithm. Prof. Varga notes that repeating verification after change is essential, because systems drift, and that comparing results over time shows whether governance is maturing or merely accumulating paperwork. The report is presented to the governance board with a short summary for non-specialists, and the board decides that verification should be repeated every year and after any major change to the leakage chain.

### Worked example

Kofi re-verifies the chain, detects all original errors, finds an inheritance gap and an outdated contact list, fixes both and reports progress and residual gaps against the first laboratory.

> **Synthetic case.** The laboratory is synthetic.

### Errors and limits

Testing only the main path misses side routes into governed data.

### Exercises

- **EX118 — New failures.** How many new tests failed? *Rubric:* 3 = two;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX119 — Contact fix.** What replaced the outdated contact list? *Rubric:* 3 = links to the on-call rota;; 2 = correct;; 1 = none;; 0 = none.
- **EX120 — Side-route lesson.** Where did both failures come from? *Rubric:* 3 = components outside the main path;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-41"></a>

## Chapter 41 — Data governance: system optimization

### Learning outcomes

You will (1) optimise the governed chain as a whole; (2) balance quality, cost and timeliness; (3) avoid optimising one part at the expense of others.

### 41.1 Whole-chain view

Kofi looks for improvements across the whole leakage chain rather than within single teams. Billing had tuned its extract to run faster by skipping a validation step, which pushed errors downstream to reconciliation, where fixing them took far longer. He shows the trade-off with timings and break counts. The whole chain performs better when billing restores the validation, even though the billing step itself becomes slower. Local optimisation had made the overall system worse while every team believed it was helping. Billing agrees.

### 41.2 Balancing objectives

Quality, cost and timeliness pull in different directions. Earlier deadlines leave less time for checks; more checks cost more computing and staff time. Kofi builds a simple table showing, for several schedule options, expected on-time rates, check coverage and cost. Owners choose an option that keeps full checks for high-risk data while moving low-risk checks later in the day. He explains that making trade-offs explicit lets owners choose consciously rather than discovering them when something breaks unexpectedly. The chosen option is recorded with reasons.

### 41.3 Bottlenecks

Kofi identifies the bottleneck in the chain: manual approval of reading corrections, which waits for one supervisor. Corrections pile up before month end, delaying reconciliation and the leakage figure. He proposes delegating approvals for small corrections to trained stewards, with supervisors approving large ones and reviewing a sample of small ones. The queue clears faster, and audit sampling shows no increase in incorrect corrections. Improving the bottleneck helps the whole chain far more than speeding up steps that were already fast. Supervisors agree.

### 41.4 Measuring improvement

Kofi measures the chain before and after changes: time from meter reading to leakage figure, share of figures published on schedule and number of restatements. All three improve over the following quarter. Prof. Varga notes that system-level measures prevent teams from claiming success on local measures while the overall outcome stagnates, and that the leakage figure's timeliness and stability are what the regulator and network engineers actually experience. Kofi adds the three chain measures to the governance board's monthly dashboard, so that any slipping trend is visible to everyone early.

### Worked example

Kofi reverses a local billing shortcut that harmed the chain, presents explicit trade-offs, relieves a correction approval bottleneck with delegated steward approvals and measures chain-level improvement.

> **Synthetic case.** Timings are synthetic.

### Errors and limits

Optimising one team's measure can hurt the system; measure the chain.

### Exercises

- **EX121 — Billing shortcut.** What did billing's shortcut cause? *Rubric:* 3 = errors pushed to slower reconciliation;; 2 = correct;; 1 = none;; 0 = none.
- **EX122 — Bottleneck.** What was the bottleneck? *Rubric:* 3 = manual approval of corrections by one supervisor;; 2 = correct;; 1 = none;; 0 = none.
- **EX123 — Chain measures.** Name the three chain measures. *Rubric:* 3 = reading-to-figure time, on-schedule share and restatements;; 2 = all;; 1 = some;; 0 = none.

<a id="ch-42"></a>

## Chapter 42 — Data governance: applied research

### Learning outcomes

You will (1) frame a research question from governance practice; (2) design a study with synthetic data; (3) report findings with limits.

### 42.1 The question

Kofi's applied research asks whether reconciliation breaks predict errors in district leakage estimates. If they do, break counts could serve as an early warning before figures are published. He frames the question precisely: in synthetic district data, is the number of reconciliation breaks in a month associated with the size of later corrections to that district's leakage figure? He notes that the question is useful to Tidewater because it would let stewards focus checking effort where errors are likely. Prof. Varga approves it.

### 42.2 Study design

Kofi generates synthetic data for forty districts over twenty-four months, with breaks and corrections linked through a known relationship plus noise. He fits a simple linear relationship using Python's statistics module and checks whether the estimated slope recovers the relationship he built in. He explains that testing methods on synthetic data with known answers shows whether the analysis can find a real effect before applying it to real data, where the true answer is unknown. He fixes the random seed so results repeat exactly.

### 42.3 Interpreting results

The analysis recovers a positive association close to the value built in, with wide variation between districts. Kofi cautions that recovering a planted effect only shows the method works, not that real districts behave this way. He outlines a plan to apply the method to real anonymised district data under Tidewater's approval, with Shadish, Cook and Campbell's discussion of validity guiding which alternative explanations, such as district size, must be checked. He also notes that the strength of association in real data may be much weaker than in the planted example.

### 42.4 Reporting

Kofi writes a short paper with the question, synthetic design, results, limits and a plan for real data. He shares code so others can reproduce the synthetic results. Prof. Varga notes that a clear statement of what the study can and cannot show is the most valuable part of applied research for practitioners, who will otherwise read more into results than they support, especially when results confirm what they already wanted to believe. The paper is presented at a departmental seminar, where questions sharpen the limits section.

### Worked example

Kofi asks whether reconciliation breaks predict leakage corrections, tests the method on synthetic districts with a planted relationship, recovers it, states limits and plans a real-data study.

> **Synthetic case.** Data are synthetic; Shadish, Cook and Campbell (2002) is real.

### Errors and limits

Recovering a planted effect does not prove a real one.

### Exercises

- **EX124 — Research question.** What did Kofi ask? *Rubric:* 3 = whether breaks predict later leakage corrections;; 2 = correct;; 1 = none;; 0 = none.
- **EX125 — Synthetic purpose.** Why use synthetic data with known answers? *Rubric:* 3 = to check the method can find a real effect;; 2 = correct;; 1 = none;; 0 = none.
- **EX126 — Alternative explanation.** Name one alternative explanation to check. *Rubric:* 3 = district size;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) apply governance in a working utility setting; (2) adapt academic methods to practical constraints; (3) reflect on professional conduct.

### 43.1 The placement

Kofi spends a placement term in Tidewater's data team. He moves from course exercises to real daily work, though all examples in this book stay synthetic. He joins morning triage, writes runbooks and supports a regulatory submission. He notices that practical constraints such as limited time, competing priorities and legacy systems shape what governance can achieve. Methods from the course remain useful but need adapting, for example running a lighter failure analysis for small changes. He keeps a weekly journal of what he adapts and why.

### 43.2 Working with owners

Owners have other jobs. Kofi learns to prepare short briefings with clear questions so owners can decide quickly. When the metering manager is too busy to review rule changes, Kofi proposes a monthly batch review rather than ad hoc requests, which the manager accepts. He reflects that respecting owners' time makes governance more likely to be supported, while demanding attention for every small question tends to make owners avoid the process. Other owners ask for the same monthly arrangement, and it becomes the team's standard approach.

### 43.3 A regulatory submission

Kofi helps prepare the annual leakage submission. He assembles evidence: lineage, control results, reconciliation, service reports and validation findings. The regulator's reviewer asks how Tidewater knows flow sensors are accurate. Kofi provides reference meter checks and their limits, and notes the planned improvements. The reviewer accepts the evidence and records the limits. He sees how the governance work of earlier chapters turns into answers that external parties find credible. The reviewer also asks that next year's submission show progress on the improvements Kofi listed, which the team adds to its plan.

### 43.4 Professional conduct

During the placement Kofi notices a colleague editing a reading without the required approval to meet a deadline. He raises it privately, explaining the risk, and the colleague submits the edit for approval. Kofi reflects on the duty to uphold controls even under pressure. Prof. Varga notes that professional bodies expect engineers to act with integrity and to raise concerns, and that small lapses tolerated under pressure gradually weaken controls that protect customers and the public. He does not report the colleague further, as the edit was corrected.

### Worked example

Kofi adapts methods during a placement, batches owner reviews, supports a regulatory submission with evidence and limits and addresses an unapproved edit professionally.

> **Synthetic case.** The placement is synthetic.

### Errors and limits

Bypassing controls under deadline pressure erodes them; raise concerns.

### Exercises

- **EX127 — Owner time.** How did Kofi respect the metering manager's time? *Rubric:* 3 = a monthly batch review of rule changes;; 2 = correct;; 1 = none;; 0 = none.
- **EX128 — Regulator question.** What did the regulator's reviewer ask? *Rubric:* 3 = how Tidewater knows flow sensors are accurate;; 2 = correct;; 1 = none;; 0 = none.
- **EX129 — Unapproved edit.** How did Kofi handle the unapproved edit? *Rubric:* 3 = raised it privately and the edit went for approval;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define a capstone project on governed data; (2) plan scope, risks and evidence; (3) agree success criteria.

### 44.1 Project choice

Kofi's capstone project is to design and demonstrate a governance package for the pressure management programme, which adjusts valves to reduce leakage. Pressure data affect safety and leakage, so the project combines lessons from the whole course. He chooses it because the programme is expanding and its data currently lack owners, rules and lineage. The capstone must produce a working demonstration on synthetic data, documentation and evidence that controls work. The operations director supports the choice and agrees to provide an engineer as a contact, which makes the project relevant to Tidewater.

### 44.2 Scope

Kofi limits scope to pressure sensor data, valve settings and the link from pressure changes to leakage estimates in three synthetic districts. He excludes the control logic of the valves themselves, which belongs to operations engineers. Clear scope prevents the project from growing beyond what one student can deliver in a term. He lists deliverables: lineage, owner map, rule catalogue, control tests, a dashboard sketch and a decision record for each major choice. The scope statement is signed by Prof. Varga and the operations engineer.

### 44.3 Risks

He identifies project risks: synthetic data that do not reflect real pressure behaviour, limited access to operations engineers and time lost to tool problems. For each risk he plans a response, such as validating synthetic patterns with an operations engineer early and keeping the code simple using only the standard library. He reviews risks weekly. Prof. Varga reminds him that project risk management is a professional skill in its own right, separate from the technical content. The risk log is kept with the project files.

### 44.4 Success criteria

Kofi agrees success criteria with Prof. Varga and an operations engineer: owners named and accepted for all data sets in scope, rules covering safety-relevant thresholds, injected errors detected at an agreed rate and a demonstration understood by an operations audience. Each criterion has a measure. He notes that agreeing criteria at the start prevents disputes later about whether the project succeeded and focuses effort on what matters to the people who will use the results. The criteria are written into the project plan and cannot be changed without agreement.

### Worked example

Kofi chooses governance for pressure management, scopes it to sensors, valve settings and three districts, plans risks with early validation and agrees measurable success criteria.

> **Synthetic case.** The project is synthetic.

### Errors and limits

Unclear scope is the most common capstone failure; write it down.

### Exercises

- **EX130 — Excluded area.** What did Kofi exclude from scope? *Rubric:* 3 = valve control logic;; 2 = correct;; 1 = none;; 0 = none.
- **EX131 — Synthetic risk response.** How will Kofi check synthetic pressure data? *Rubric:* 3 = validate patterns with an operations engineer early;; 2 = correct;; 1 = none;; 0 = none.
- **EX132 — Audience criterion.** Who must understand the demonstration? *Rubric:* 3 = an operations audience;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) respond to reviewer findings; (3) record decisions after review.

### 45.1 Preparing

Halfway through the capstone, Kofi's design goes to an independent review by an engineer from another utility and a data governance consultant, neither involved in the project. He prepares a review pack: problem statement, scope, design, decision records, test plans and known weaknesses. He lists weaknesses openly so reviewers can spend their time on unknown problems. Prof. Varga explains that independent review is valuable precisely because reviewers lack the designer's assumptions and will question what the designer takes for granted. The pack is sent a week ahead.

### 45.2 Findings

Reviewers raise three findings. First, the rules treat all pressure sensors alike, though sensors at critical points need tighter thresholds. Second, lineage stops at the leakage estimate and does not show where pressure data feed customer complaint analysis. Third, the owner map names the operations manager for all pressure data, which concentrates too much in one person. They also praise the decision records for making reasoning easy to follow and test. Each finding is written with an explanation and the evidence that led the reviewers to raise it.

### 45.3 Responding

Kofi responds to each finding in writing: he adds sensor categories with different thresholds, extends lineage to complaint analysis after confirming the dependency with the customer team and splits ownership between the operations manager for critical sites and district managers for others. For each response he records the change, the reasoning and the residual concern. He discusses one finding where he partly disagrees, explaining his reasons, and the reviewers accept a compromise. The compromise concerns the number of sensor categories, which is reduced from five to three.

### 45.4 After review

The review record lists findings, responses, changes and open items. It goes into the capstone evidence dossier. Kofi reflects that reviewers found issues he had missed despite careful work, because familiarity hides gaps. Prof. Varga notes that welcoming review rather than defending against it marks a mature engineer, and that a documented review trail shows assessors how the design improved, which is more convincing than a design presented as if flawless from the start. The open items are scheduled for the second half of the capstone.

### Worked example

Kofi prepares a review pack listing weaknesses, receives three findings on thresholds, lineage and ownership, responds in writing with changes and a negotiated compromise and records the review.

> **Synthetic case.** The review is synthetic.

### Errors and limits

Hiding known weaknesses wastes reviewers' time.

### Exercises

- **EX133 — Threshold finding.** What did reviewers say about thresholds? *Rubric:* 3 = critical sensors need tighter thresholds;; 2 = correct;; 1 = none;; 0 = none.
- **EX134 — Ownership change.** How was ownership split? *Rubric:* 3 = operations manager for critical sites, district managers for others;; 2 = correct;; 1 = partial;; 0 = none.
- **EX135 — Why review.** Why are independent reviewers valuable? *Rubric:* 3 = they lack the designer's assumptions;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) build and test the capstone governance package; (2) demonstrate it; (3) evaluate it against success criteria.

### 46.1 Building

Kofi builds the package on synthetic data: a pressure data generator with realistic daily cycles, the rule library extended with sensor categories, lineage including complaint analysis, catalogue entries and an alert dashboard. He uses only the Python standard library, as planned, which keeps the code readable for operations engineers. He documents each component with its purpose, owner and test. The build follows the release process from earlier chapters, with code review by a classmate and tests before each merge. Each merge is logged.

### 46.2 Testing

He injects errors into the synthetic data: stuck sensors, sudden spikes, missing hours and a valve setting changed without a record. The controls detect most errors. Missing hours at one district are detected late, because the completeness check runs daily rather than hourly. He changes the check to hourly for critical sites. A further run detects all injected errors within the agreed times, and he records both runs in the test log with the change between them. The change is approved by the operations engineer.

### 46.3 Demonstration

Kofi demonstrates the package to an audience of operations staff, an owner and Prof. Varga. He walks through an incident: a stuck sensor at a critical site, the alert, the runbook, the degraded mode procedure and the effect on the leakage estimate. Operations staff ask practical questions about alert volumes and false alarms. He shows alert statistics from the test period. The audience confirms they understood the demonstration and could use the dashboard. They also suggest adding sensor location maps, which Kofi includes afterwards.

### 46.4 Evaluation

Kofi evaluates the project against success criteria. Owners are named and accepted for all data sets; rules cover safety-relevant thresholds; injected errors were all detected after the hourly change; the operations audience understood the demonstration. He notes limits: synthetic data cannot capture all real behaviour, and long-term operation is untested. Prof. Varga approves the evaluation, praising its honesty about limits alongside clear evidence for each criterion. The evaluation is written as a short report, with each criterion followed by its measure, the result achieved and the evidence that supports it, so that examiners can check every claim.

### Worked example

Kofi builds a standard-library governance package for pressure data, finds late detection of missing hours and moves to hourly checks for critical sites, demonstrates an incident walkthrough and evaluates against criteria.

> **Synthetic case.** The package and data are synthetic.

### Errors and limits

Demonstrations that hide failures mislead; show the test log.

### Exercises

- **EX136 — Late detection.** What was detected late at first? *Rubric:* 3 = missing hours at one district;; 2 = correct;; 1 = none;; 0 = none.
- **EX137 — Fix for late detection.** What fixed it? *Rubric:* 3 = hourly completeness checks for critical sites;; 2 = correct;; 1 = none;; 0 = none.
- **EX138 — Stated limits.** Name one limit Kofi stated. *Rubric:* 3 = synthetic data or untested long-term operation;; 2 = one;; 1 = none;; 0 = none.

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) run a failure and recovery trial on governed data; (2) measure recovery; (3) improve recovery procedures.

### 47.1 The trial

Kofi runs a trial in which the pressure data platform fails during a simulated high-demand day. The synthetic scenario removes the main historian for three hours. The trial tests whether operators can continue safely using degraded mode procedures, whether data are recovered completely afterwards and whether governance records show what happened. Participants include two operators, a data steward and the on-call engineer. Prof. Varga observes and records timings without intervening, so the trial reflects how the team really responds. Everyone is briefed beforehand.

### 47.2 During the failure

Operators switch to local displays and manual readings within fifteen minutes, following the procedure. The on-call engineer receives the alert promptly but spends time finding the recovery instructions, which were stored on the failed server. The steward marks affected data in the log. Kofi notes that keeping recovery instructions on the system they recover is a classic mistake, and that the trial revealed it in a safe setting rather than during a real incident. He records the delay in finding the instructions with its timing.

### 47.3 Recovery

After the historian returns, buffered readings from site devices are reloaded. Kofi reconciles the reloaded readings with site buffers and finds a short gap where one buffer had filled and overwritten older data. He measures recovery time and completeness and records the gap with its cause. Network operations agrees to increase buffer size at critical sites. He notes that recovery is not complete until data are reconciled, not merely when systems restart. The reconciliation results are attached to the trial report for the governance board.

### 47.4 Improvements

Kofi records improvements: recovery instructions moved to a separate location with printed copies, larger buffers at critical sites and a reconciliation step added to the recovery runbook. A second short trial confirms that the engineer finds instructions quickly. Prof. Varga notes that trials are valuable because they expose dependencies that documents conceal, and that governance of data includes planning for the data's survival through failures, not only its quality in normal operation. The board asks that a similar trial be run every year with different participants and scenarios.

### Worked example

Kofi runs a historian failure trial, finds recovery instructions stored on the failed server and a buffer overwrite gap, and improves storage of instructions, buffer sizes and recovery reconciliation.

> **Synthetic case.** The trial is synthetic.

### Errors and limits

Declaring recovery when systems restart ignores lost data; reconcile first.

### Exercises

- **EX139 — Instruction problem.** Where were recovery instructions stored? *Rubric:* 3 = on the failed server;; 2 = correct;; 1 = none;; 0 = none.
- **EX140 — Data gap cause.** What caused the data gap? *Rubric:* 3 = a buffer filled and overwrote older data;; 2 = correct;; 1 = none;; 0 = none.
- **EX141 — Recovery definition.** When is recovery complete? *Rubric:* 3 = when data are reconciled;; 2 = correct;; 1 = restart;; 0 = none.

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble an evidence dossier for governed data; (2) link claims to evidence; (3) package it for assessors and regulators.

### 48.1 Purpose

Kofi assembles an evidence dossier for the capstone and the wider leakage governance work. The dossier must let an assessor or regulator verify claims without asking Kofi to explain. Each claim, such as that pressure data have named owners or that controls detect stuck sensors, links to evidence: ownership records, test logs, review findings, trial reports and decision records. He explains that a dossier is an argument supported by evidence, not a pile of documents. Each link is checked before the dossier is issued.

### 48.2 Structure

Kofi structures the dossier around the requirements: for each requirement, the claim, the controls, the evidence and the limitations. An index lets readers jump to any requirement. Evidence files are stored with dates and versions, and their integrity is recorded with hashes computed using Python's hashlib, so readers can confirm files have not changed since assembly. He also includes the independent review record and his responses, which show how the design developed. Each file's hash is listed in the index beside its title, date and version number.

### 48.3 Linking claims

Kofi checks every claim for evidence and finds two claims without it: that stewards were trained and that retention rules apply to pressure data. For training, he obtains attendance records. For retention, he discovers that the rule exists in policy but was never configured for pressure data, so he configures it, tests it and adds the result. He notes that assembling evidence can reveal gaps between policy and practice that nobody had noticed. Both new pieces of evidence are added to the index with their hashes.

### 48.4 Audience

Kofi writes a summary for non-specialists and keeps technical detail in appendices. He asks a classmate unfamiliar with the project to find evidence for three randomly chosen claims, timing the search. Each takes under five minutes. Prof. Varga notes that dossiers succeed when readers can navigate them independently, and that the discipline of evidencing every claim makes engineers more careful about what they claim in the first place. Kofi revises two index entries that slowed his classmate down, making their titles clearer and adding cross references from related requirements.

### Worked example

Kofi structures a dossier by requirement with hashed evidence files, finds two unsupported claims and closes a retention configuration gap, and tests navigation with an unfamiliar classmate.

> **Synthetic case.** The dossier is synthetic.

### Errors and limits

Claims without evidence weaken the whole dossier; remove or support them.

### Exercises

- **EX142 — Hashing purpose.** Why are evidence files hashed? *Rubric:* 3 = to confirm they have not changed;; 2 = correct;; 1 = none;; 0 = none.
- **EX143 — Retention gap.** What did the retention claim reveal? *Rubric:* 3 = the rule was never configured for pressure data;; 2 = correct;; 1 = none;; 0 = none.
- **EX144 — Navigation test.** How was navigation tested? *Rubric:* 3 = an unfamiliar classmate found evidence for random claims;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis on data governance; (2) present design, evidence and evaluation; (3) discuss contribution and limits.

### 49.1 Thesis argument

Kofi's thesis argues that engineering methods, such as interface control, verification, failure analysis and recovery trials, make data governance in utilities more reliable than policy-led approaches alone. He supports the argument with the leakage chain work and the pressure capstone, both on synthetic data. He frames the contribution as a practical method for applying engineering discipline to governance, and positions it against DAMA-DMBOK2 and ISO/IEC 38505-1, which describe governance functions but leave engineering methods open. Prof. Varga approves this framing after discussion.

### 49.2 Structure

The thesis has chapters on context, literature, method, the leakage chain, the capstone, evaluation and discussion. The literature chapter reviews data quality frameworks, governance decision rights, standards such as ISO 8000 and data management principles including FAIR. The method chapter explains how each engineering technique was adapted. Results chapters present designs, tests and trials with evidence from the dossier. Kofi writes the evaluation chapter around the success criteria agreed at the start of the capstone. Each chapter opens with the claim it supports and closes with a summary.

### 49.3 Limits

Kofi devotes a section to limits. All data were synthetic, so effects on real operations remain untested. The work took place in one fictional utility, so generalising to others needs care. Some evaluations relied on small groups of users. He suggests future work: applying the methods to real anonymised data, comparing with utilities using policy-led governance and measuring long-term costs. Prof. Varga notes that a strong limits section increases rather than reduces the thesis's credibility. Each limit is linked to a specific future work item.

### 49.4 Writing process

Kofi writes the thesis over four months, sharing chapters with Prof. Varga for feedback. Early drafts describe activities in sequence; feedback pushes him to organise around the argument instead. He checks every citation against the original source and uses decision records and the dossier as primary evidence. He reflects that writing clarified his own thinking, because explaining why each method mattered exposed assumptions he had made without noticing during the project. He keeps a log of feedback received and changes made, which he includes as an appendix.

### Worked example

Kofi argues that engineering methods strengthen utility data governance, structures his thesis around evidence and criteria, states synthetic-data and single-case limits and reorganises drafts around the argument.

> **Synthetic case.** The thesis is synthetic; cited standards and frameworks are real.

### Errors and limits

Theses organised as diaries hide the argument; organise around claims.

### Exercises

- **EX145 — Thesis claim.** What does the thesis argue? *Rubric:* 3 = engineering methods make utility data governance more reliable;; 2 = correct;; 1 = none;; 0 = none.
- **EX146 — Future work.** Name one future work item. *Rubric:* 3 = real anonymised data, comparison with other utilities or long-term costs;; 2 = one;; 1 = none;; 0 = none.
- **EX147 — Feedback change.** How did feedback change the drafts? *Rubric:* 3 = reorganised around the argument;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend an engineering thesis before examiners; (2) answer challenges with evidence; (3) reflect on professional growth.

### 50.1 Preparing the defense

Kofi prepares a twenty-minute presentation covering the argument, key designs, evidence and limits. He anticipates questions by asking classmates to play examiners and challenge each claim. He prepares backup slides with test logs, trial timings and review findings. He practises explaining technical points in plain language, since one examiner is a regulator rather than an engineer, and the presentation must work for both specialist and general audiences. He also rehearses timing carefully, cutting slides until the talk fits comfortably within the allowed time with room for an unexpected question at the end.

### 50.2 Questions

Examiners ask why synthetic results should persuade a utility to invest, how the methods would work in a smaller utility with fewer staff and whether governance controls could slow emergency response. Kofi answers using evidence and limits: synthetic tests show methods work mechanically, smaller utilities could adopt a reduced set prioritised by risk and safety procedures keep emergency actions independent of governance approval while recording them for later review. Each answer refers to a specific page of the thesis or dossier, so examiners can check the evidence for themselves.

### 50.3 Difficult moment

The regulator examiner challenges a claim in the thesis that leakage figures became more accurate, pointing out that the evidence shows more consistency, not proven accuracy. Kofi agrees, explains the difference and offers to revise the wording. The examiners appreciate the response. Prof. Varga later tells him that accepting a valid challenge gracefully demonstrated the integrity examiners look for, and that overstated claims are common in theses and easily corrected when the author listens. The revised wording becomes one of the minor corrections required.

### 50.4 Reflection

After passing with minor corrections, Kofi reflects on his growth over five years: from basic programming and measurement to designing, testing and defending governance for complex utility data. He values most the habits of evidence, review and honesty about limits. He plans to join Tidewater's data team and continue professional development. The next course in this area turns to privacy and data protection, where governed data meet the rights of the people they describe. He thanks his supervisor and classmates in the acknowledgements.

### Worked example

Kofi prepares for mixed examiners, answers questions on persuasiveness, small utilities and emergencies, accepts a valid challenge about accuracy versus consistency and reflects on five years of growth.

> **Synthetic case.** The defense is synthetic.

### Errors and limits

Defending an overstated claim damages credibility; correct it.

### Exercises

- **EX148 — Emergency question.** How do safety procedures handle emergencies? *Rubric:* 3 = emergency actions stay independent of approval but are recorded;; 2 = correct;; 1 = none;; 0 = none.
- **EX149 — Accuracy challenge.** What did the regulator challenge? *Rubric:* 3 = accuracy was claimed but consistency was shown;; 2 = correct;; 1 = none;; 0 = none.
- **EX150 — Valued habits.** Which habits does Kofi value most? *Rubric:* 3 = evidence, review and honesty about limits;; 2 = all;; 1 = some;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Kofi Mensah, Prof. Elena Varga, Northfield Polytechnic, Tidewater Water and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** About 2.16 million readings per day.

**EX002.** A failed feed rather than lower water use.

**EX003.** It sharply reduces total storage over seven years.

**EX004.** Meters with readings but no linked premise.

**EX005.** Twelve.

**EX006.** Every source the report relies on.

**EX007.** Supplied volume looks higher, so estimated leakage falls.

**EX008.** It inflated that district's demand a thousandfold.

**EX009.** Unit, last calibration date and owner.

**EX010.** It shows data owners what failed and why.

**EX011.** Stop when the structure is wrong; record and continue for single bad rows.

**EX012.** An off-by-one error in timestamp handling.

**EX013.** Summary, background, method, findings, impact and recommendations.

**EX014.** Approval to add unit validation to every data feed.

**EX015.** Date, decision, who made it, options considered and evidence.

**EX016.** Within half a percent.

**EX017.** About two percent.

**EX018.** Leakage plus measurement error plus timing differences.

**EX019.** 2 percent (8 of 400).

**EX020.** The interval reaches above 3 percent.

**EX021.** A firmware update on a batch of meters.

**EX022.** When it cannot transmit for longer than its seven-day storage.

**EX023.** Apparent duplicate or missing hours in local time.

**EX024.** The origin of the data.

**EX025.** A name, a description and a function.

**EX026.** The rule rejected legitimate meter replacements.

**EX027.** Older meters report daily, so hourly completeness would fail them.

**EX028.** A wrong pressure reading could leave a hospital without water.

**EX029.** Yearly confirmation with each customer and strict access limits.

**EX030.** He lacked the competence to judge its contamination risk.

**EX031.** Ownership changed at every network boundary.

**EX032.** Its protocol does not authenticate sensors.

**EX033.** Around storms.

**EX034.** He limited it to the processing account and the data team group.

**EX035.** Each job checks its predecessor finished with expected row counts.

**EX036.** A date library update changing timestamp parsing.

**EX037.** That readings point to real meters and meters to real premises.

**EX038.** Three.

**EX039.** So past bills can be explained using the facts that applied then.

**EX040.** Every accepted reading has a valid meter and unit.

**EX041.** A vendor file arriving with a new column order.

**EX042.** Configuration values that data owners can review.

**EX043.** Availability and integrity.

**EX044.** A shared analyst account, replaced with named accounts.

**EX045.** Owner approval and encryption.

**EX046.** As a customer billing complaint far from its cause.

**EX047.** Fields, units, formats, timing, error handling and contacts.

**EX048.** Deletion.

**EX049.** Rejects were measured but nobody reliably acted on them.

**EX050.** Use weekly reject data and limit changes to small steps.

**EX051.** One week, down from three.

**EX052.** Production personal data never enter test; use synthetic data.

**EX053.** New tagged data sets get protections automatically.

**EX054.** Data owners, when data sets are registered.

**EX055.** 230.

**EX056.** No; they are pseudonymised and still personal data.

**EX057.** In a script file, now moved to the key management service.

**EX058.** Nobody.

**EX059.** Maintain rules and definitions day to day.

**EX060.** The leakage indicator reported to the regulator.

**EX061.** The daily volume feed arrives by 06:00 on at least 95 percent of days.

**EX062.** District-level aggregation with a minimum of fifty properties.

**EX063.** Owner assignment, reconciliation and timeliness.

**EX064.** Seven.

**EX065.** Manual readings from the field app and raw sensor flows.

**EX066.** By comparing the graph with warehouse query logs each quarter.

**EX067.** A stuck flow sensor.

**EX068.** Because threats and accidental failures often look alike.

**EX069.** A flat-line detector owned by network operations.

**EX070.** Accuracy and completeness.

**EX071.** Against a portable reference meter during maintenance visits.

**EX072.** Plausible wrong values.

**EX073.** It was a single point of failure.

**EX074.** Alerts only on breaches, plus a weekly trend summary.

**EX075.** Failure and human behaviour.

**EX076.** Reconciliation across domains was weak at current maturity.

**EX077.** The hybrid.

**EX078.** Domain teams reaching agreed skill levels.

**EX079.** A documented procedure for correcting readings with approval.

**EX080.** Thirty-one.

**EX081.** By injecting synthetic errors in a test environment.

**EX082.** 96.5 percent, 9,650 of 10,000 rows.

**EX083.** Meter replacements, where new meters start at zero.

**EX084.** He reported it with causes and a fix plan rather than lowering the threshold.

**EX085.** 12.2 percent, 11 of 90 days.

**EX086.** A control system upgrade added a backup job before the export.

**EX087.** Four.

**EX088.** Ten of twelve.

**EX089.** Comparing each column's distribution with its history.

**EX090.** Whether we built the controls right.

**EX091.** Schema details, refresh times and quality results.

**EX092.** Never lower than its most sensitive input.

**EX093.** They check badges before using data and query owners on poor scores.

**EX094.** 97.75 percent.

**EX095.** They make leakage look higher than it is.

**EX096.** Billing.

**EX097.** The operations safety engineer.

**EX098.** It depends on a single warehouse server.

**EX099.** Manual readings need standard forms and units.

**EX100.** Two weeks, with a test file.

**EX101.** Reconciliation results were not reaching the catalogue badges.

**EX102.** The data governance lead.

**EX103.** A model card describing the vendor's leak algorithm.

**EX104.** No, only frequency summaries.

**EX105.** Better anticipation of failure and people's concerns.

**EX106.** Twenty-four times.

**EX107.** Processing only new and changed records.

**EX108.** Tested them by error injection.

**EX109.** By nine in the morning.

**EX110.** Informed the regulator's contact of a one-day delay.

**EX111.** Another steward follows them during a synthetic incident.

**EX112.** Alerts with technical rule names.

**EX113.** By adding key catalogue information to their control room display.

**EX114.** Claiming governance caused the improvement without stronger evidence.

**EX115.** Tariff reference data were not updated for two months.

**EX116.** A leaver in the staff directory triggers a reminder.

**EX117.** Burnout and single points of failure.

**EX118.** Two.

**EX119.** Links to the on-call rota.

**EX120.** Components outside the main path.

**EX121.** Errors moved downstream where fixing them took longer.

**EX122.** Manual approval of reading corrections by one supervisor.

**EX123.** Time to figure, on-schedule share and restatements.

**EX124.** Whether reconciliation breaks predict corrections to district leakage.

**EX125.** To check the method recovers a known effect.

**EX126.** District size.

**EX127.** By proposing a monthly batch review.

**EX128.** How Tidewater knows the flow sensors are accurate.

**EX129.** He raised it privately and the colleague submitted it for approval.

**EX130.** The valves' control logic.

**EX131.** By validating patterns with an operations engineer early.

**EX132.** An operations audience.

**EX133.** Sensors at critical points need tighter thresholds.

**EX134.** Critical sites to the operations manager, others to district managers.

**EX135.** They do not share the designer's assumptions.

**EX136.** Missing hours at one district.

**EX137.** Hourly completeness checks for critical sites.

**EX138.** Synthetic data cannot capture all real behaviour.

**EX139.** On the server that had failed.

**EX140.** A site buffer filled and overwrote older readings.

**EX141.** When data are reconciled, not when systems restart.

**EX142.** So readers can confirm files are unchanged.

**EX143.** The policy rule had never been configured for pressure data.

**EX144.** A classmate found evidence for three random claims, each in under five minutes.

**EX145.** That engineering methods make utility data governance more reliable than policy alone.

**EX146.** Applying the methods to real anonymised data.

**EX147.** From activity sequence to argument-based structure.

**EX148.** Emergency actions do not wait for governance approval but are recorded for review.

**EX149.** The evidence showed consistency, not proven accuracy.

**EX150.** Evidence, review and honesty about limits.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and standards were checked against their publisher pages. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009). Methodologies for data quality assessment and improvement. *ACM Computing Surveys, 41*(3), 1–52. https://doi.org/10.1145/1541880.1541883
- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-188
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- ISO/IEC. (2017). *ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data*. <https://www.iso.org/standard/56639.html>
- Khatri, V., & Brown, C. V. (2010). Designing data governance. *Communications of the ACM, 53*(1), 148–152. https://doi.org/10.1145/1629175.1629210
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.
