# Critical Infrastructure and Sector Security: Foundations, Evidence and Practice

- Language: English (`en`); bachelor's course, four years; approximately 3,200 hours of planned study (course 115 of 207 in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **draft**. Chapters 1–40 of 40 have authored teaching text; exercises EX001–EX080 (two per chapter) have matching worked results; fourteen offline labs are embedded with their verified output. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. The plan's target of three exercises per chapter is not yet met. Draft-chapter coverage is not a completed book.
- Audience: broad security and computing students who want to work on the services societies cannot do without — healthcare, energy, water, transport, finance and public services. Entry knowledge: secondary-school mathematics, basic computer use and the ability to read and write clear English prose. The book builds probability, programming, networks, data, identity and cryptography from Chapter 1.
- Relation to the other books in this area: the [engineering book](../../../../engineering-5-years/critical-sector-security/en/book/MANUSCRIPT.md) teaches how to *design, build and verify* one secure system against requirements; the [master's book](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) teaches how to design and defend one ethically reviewed empirical study; the [doctoral book](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) asks for an original contribution to knowledge. **This bachelor's book is about breadth and judgement**: understanding how several critical sectors work and depend on each other, reading evidence critically, comparing methods and controls with explicit assumptions, and taking part safely in the protection and incident work of a real organisation. Its capstone (Chapters 35–40) is a comparative, evidence-led project, not a system build and not a dissertation.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights and are not relicensed here.
- Educational boundary: this course is an independent educational blueprint. It is not an accredited degree and grants no authority to access, scan, test or modify any real system. Every organisation, site, device, address, person and number in a worked example is **synthetic** unless a sentence explicitly cites a public source. Nothing here is an operational procedure for a real hospital, utility, bank or operator, and nothing is legal advice.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

The forty chapters follow the eight semesters of the plan. **Chapters 1–18** are the foundations every security graduate needs — mathematical reasoning, computing, programming, writing, security literacy, discrete structures, networks, data, ethics, operating systems, probability, identity, privacy, measurement, architecture, cryptography and research method — each taught through a critical-service example from its first page. **Chapters 19–32** are the field core: what makes infrastructure "critical", the public cases that shaped the field, system models of operational technology, dependencies between sectors, risk-assessment methods, controls, verification, failure analysis, operations and incident response, with two laboratories (25, 30). **Chapters 33–40** are research practice, a comparative project, field practice and the capstone sequence ending in a thesis and presentation.

Every chapter has learning outcomes, teaching sections with definitions, a worked example, a practical activity, common errors and limits, two exercises and a synthesis. Fourteen chapters embed an offline lab written for the Python 3 standard library; the printed outputs were produced by running the code with Python 3.13. Write your answer before opening the [worked results](#worked-results).

Keep four headings in your study notes for every case you analyse: **service** (what people depend on, and how quickly harm follows its loss), **dependency** (what the service needs — power, communications, people, suppliers, data), **evidence** (what you actually know, from which source, with what limits) and **decision** (what you would recommend, compared with what alternative, and under which assumptions). The most common failure at bachelor's level is not a missing fact; it is a confident recommendation that never states its assumptions or compares it with anything.

### The synthetic county used in this book

| Synthetic element | Role | Boundary |
|---|---|---|
| **Calder County** and its **County Resilience Partnership (CRP)** | A region whose operators share plans and exercises | Invented; no real place |
| **Calder Valley Hospital (CVH)** — 420 beds, emergency department, imaging, laboratory, building-management system (BMS), standby generators | Healthcare operator | Invented |
| **Calder Power Networks (CPN)** — electricity distribution, Substation North, feeder RTUs, control room, remote-access gateway | Energy operator | Invented; no real product named |
| **Calder Water (CW)** — treatment works, pumps, 10-hour treated-water storage, telemetry | Water operator | Invented |
| **Calder Transit (CT)** — light rail with signalling and ticketing | Transport operator | Invented |
| **Calder Mutual** — a regional bank with card and payment services | Financial operator | Invented |
| **County Emergency Dispatch Centre (CEDC)** — call handling and computer-aided dispatch (CAD) | Public service | Invented |
| All IP addresses (10.x, and 198.51.100.x from the documentation range), keys, probabilities, costs (in pounds, £) and lab outputs | Teaching data | Synthetic; the demo key in Lab 8 is published and must never be used |

### Source policy

Factual claims about laws, standards, incidents and published studies are linked to public sources where cited. This draft has **not** received an independent source-by-source verification, so readers should recheck the exact version, date and supported scope before relying on a claim. Classic results (Bayes' theorem, the definition of a hash function and the Saltzer–Schroeder principles) are paired with classic references. The Oldsmar discussion links both an early account and a later revision so that the initial allegation is not mistaken for a settled finding. Standards behind paywalls (including IEC 62443) are cited through public overview or catalogue pages; the draft does not quote unverified clauses.

## Contents

1. [Mathematical reasoning](#ch-01)
2. [Computing systems](#ch-02)
3. [Programming I](#ch-03)
4. [Academic writing](#ch-04)
5. [Security literacy](#ch-05)
6. [Discrete structures](#ch-06)
7. [Networks and protocols](#ch-07)
8. [Programming II](#ch-08)
9. [Data and databases](#ch-09)
10. [Ethics and authorized practice](#ch-10)
11. [Operating systems](#ch-11)
12. [Probability and statistics](#ch-12)
13. [Identity and access](#ch-13)
14. [Privacy foundations](#ch-14)
15. [Evidence and measurement](#ch-15)
16. [Security architecture](#ch-16)
17. [Cryptography concepts](#ch-17)
18. [Research methods I](#ch-18)
19. [Critical infrastructure and sector security: scope and theory](#ch-19)
20. [Critical infrastructure and sector security: foundational cases](#ch-20)
21. [Critical infrastructure and sector security: system models](#ch-21)
22. [Critical infrastructure and sector security: data and dependencies](#ch-22)
23. [Critical infrastructure and sector security: methods I](#ch-23)
24. [Critical infrastructure and sector security: controls](#ch-24)
25. [Laboratory I](#ch-25)
26. [Critical infrastructure and sector security: methods II](#ch-26)
27. [Critical infrastructure and sector security: verification](#ch-27)
28. [Critical infrastructure and sector security: failure analysis](#ch-28)
29. [Critical infrastructure and sector security: operations](#ch-29)
30. [Laboratory II](#ch-30)
31. [Critical infrastructure and sector security: advanced cases](#ch-31)
32. [Critical infrastructure and sector security: interdisciplinary interfaces](#ch-32)
33. [Research methods II](#ch-33)
34. [Comparative project](#ch-34)
35. [Capstone proposal](#ch-35)
36. [Field or community practice](#ch-36)
37. [Evidence review seminar](#ch-37)
38. [Capstone implementation](#ch-38)
39. [Capstone evaluation](#ch-39)
40. [Thesis and presentation](#ch-40)

The [worked results](#worked-results) contain EX001–EX080. A [glossary](#glossary) and [references](#references) close the book.



<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes and connection

After this chapter you can (1) turn a vague worry ("what if the dispatch centre loses its internet link?") into a quantity with units; (2) compute an expected annual loss and explain why it is not the same as the worst credible event; (3) estimate orders of magnitude and check a calculation by bounding it; and (4) state the assumptions behind a number so that someone else can disagree with them precisely. The chapter introduces the synthetic Calder County used throughout the book and prepares Chapter 6 (discrete structures) and Chapter 12 (probability and statistics).

### 1.1 Why security needs numbers — and why numbers are not enough

Critical-sector security is full of comparisons. Should Calder Valley Hospital spend money on a second network link or on testing its generators? Should Calder Power Networks patch a feeder controller now, during a planned outage next month, or never? These are decisions under uncertainty, and the only honest way to compare them is to make the uncertainty explicit. **Mathematical reasoning** here does not mean advanced mathematics. It means four habits: give every quantity a unit; write down where every number came from; check a result by estimating it another way; and say what would change the answer.

A **quantity** is a number with a unit: 4 hours, £2,000 per hour, 0.3 events per year. Most errors in risk arithmetic are unit errors: multiplying a probability per year by a cost per hour, or adding a percentage to a count. Writing units next to every term — and cancelling them as you go — catches these errors before anyone else does.

### 1.2 Expected value and its limits

For a one-event annual model, if an event has probability $p$ and costs $C$ when it happens, its **expected annual loss** (EAL) is $p \times C$. Expected losses for distinct cost components add even when the events are dependent: this is the linearity of expectation. The analyst must still avoid counting the *same* consequence twice when scenarios overlap. Independence is needed for some probability calculations, such as multiplying the probabilities of two failures, but not for adding expected costs. Expected value helps compare a control's yearly cost with the loss it might avoid. It can also hide important differences: a 1-in-100 catastrophe and a near-certain nuisance may have the same product. For a hospital, a 72-hour loss of power is not "the same" as seventy-two one-hour losses: patients who need ventilation, dialysis or surgery are harmed by duration, not by an average. So every expected-value table in this book is paired with a **worst credible event** — the most severe outcome you believe could realistically occur, stated with its duration.

Probabilities used in such tables are rarely measured. They are estimates from incident records, sector reports or expert judgement. That is acceptable only if you say so. A good habit is to write the source in brackets — "(estimate, CEDC operations manager, 2026)" — and to try the calculation with half and double the estimate. If the decision does not change, the estimate is good enough; if it does, it needs more evidence. Chapter 15 returns to this idea as **sensitivity analysis**.

### 1.3 Orders of magnitude and bounding

Before calculating precisely, estimate. A hospital with 420 beds might lose on the order of thousands of pounds per hour of disruption in cancelled procedures and diverted ambulances, not tens or millions. An estimate that lands three orders of magnitude away from the careful calculation is a sign that a unit or a decimal point has slipped. **Bounding** is the related skill: if you cannot estimate a quantity, find numbers it must lie between. If a generator test programme costs at least £8,000 (staff time) and at most £15,000 (staff time plus fuel and contractor), a decision that holds at both ends does not need the exact figure.

### 1.4 Worked example: two proposals in Calder County (synthetic)

**This case is synthetic.** Calder County's **County Resilience Partnership (CRP)** has money for one of two proposals.

- **A — second internet link for the County Emergency Dispatch Centre (CEDC)**, cost £18,000 a year. Without it, CRP estimates a 0.30 annual chance of a 4-hour link outage and a 0.02 chance of a 48-hour outage (a cut cable on the single route), each costing £2,000 per hour in fallback staffing and delay.
- **B — a generator test programme for Calder Valley Hospital**, cost £12,000 a year. Without it, the estimate is a 0.10 chance of a 12-hour failure to start during a grid outage and a 0.01 chance of a 72-hour failure, each costing £5,000 per hour.

For A, EAL = 0.30 × 4 h × £2,000/h + 0.02 × 48 h × £2,000/h = £2,400 + £1,920 = £4,320 a year. For B, EAL = 0.10 × 12 × 5,000 + 0.01 × 72 × 5,000 = £6,000 + £3,600 = £9,600. Neither option "pays for itself" in expected terms (ratios 0.24 and 0.80), which is common for resilience spending: we buy protection against tails, not averages. The worst credible events (£96,000 and £360,000) make B the stronger case — and B's harm is to patients, which no pound figure fully expresses. The recommendation is B, with the stated assumption that the probability estimates are within a factor of two.

### 1.5 Practical activity: Lab 1

The lab reproduces the comparison. Change one probability at a time by a factor of two and see whether the ranking changes.

```python
# Lab 1 - expected loss versus worst credible case for two options (synthetic Calder data, offline)
options = {
    "A: second ISP link for dispatch centre": {"cost": 18_000, "scenarios": [(0.30, 4, 2_000), (0.02, 48, 2_000)]},
    "B: backup generator test programme":     {"cost": 12_000, "scenarios": [(0.10, 12, 5_000), (0.01, 72, 5_000)]},
}
# each scenario: (annual probability it occurs without the option, outage hours, loss per hour in GBP)
for name, o in options.items():
    eal = sum(p * h * c for p, h, c in o["scenarios"])
    worst = max(h * c for p, h, c in o["scenarios"])
    print(f"{name}: expected annual loss avoided = {eal:,.0f}; worst single event = {worst:,.0f}; cost = {o['cost']:,}")
    print(f"   ratio avoided/cost = {eal / o['cost']:.2f}")
```

Expected output:

```text
A: second ISP link for dispatch centre: expected annual loss avoided = 4,320; worst single event = 96,000; cost = 18,000
   ratio avoided/cost = 0.24
B: backup generator test programme: expected annual loss avoided = 9,600; worst single event = 360,000; cost = 12,000
   ratio avoided/cost = 0.80
```

The lab assumes each option removes its scenarios completely. Real controls reduce probability or duration partially; Exercise EX002 asks you to model that.

Two runs show what the lab is for. Halving B's 0.10 probability to 0.05 lowers its expected loss to £6,600, still above A's £4,320, so the ranking holds. Doubling A's 0.02 chance of a 48-hour outage to 0.04 raises A to £6,240, still below B. Because neither single change flips the order, the recommendation for the generator programme is robust to a factor of two in any one estimate, which is exactly the claim the worked example made.

### 1.6 Common errors and limits

- Multiplying quantities with incompatible units (per-year by per-hour without converting).
- Presenting an estimated probability as if it were measured.
- Ranking options by expected loss alone when harm to people depends on duration.
- Forgetting that controls rarely remove a risk entirely.
- Adding probabilities of events that are not mutually exclusive (Chapter 12 shows the correct rule).

Each error has a Calder example. The EX001 colleague multiplied a per-year probability by hours and called the result pounds per hour. Writing "0.02 chance" with no source makes CEDC's guess look like a measured rate. Ranking A and B by expected loss alone would hide that B's £360,000 tail is 72 hours without reliable hospital power. And the lab's own assumption, that each option removes its scenarios entirely, is the fourth error built into a teaching model on purpose.

### Exercises — chapter 1

**EX001 — Unit discipline.** *Objective:* find and fix unit errors. *Inputs:* a colleague writes "EAL = 0.02 per year × 48 hours × £2,000 = £1,920 per hour". *Steps:* (1) cancel the units term by term; (2) state the correct unit of the result; (3) explain in one sentence why the mistake matters for comparing with a £18,000 annual cost. *Expected evidence:* corrected expression with units. *Rubric:* 3 = correct unit (£ per year) and a clear reason; 2 = correct unit, weak reason; 1 = notices an error but misstates it; 0 = none.

**EX002 — Partial effectiveness.** *Objective:* model a control that only reduces a risk. *Inputs:* Lab 1. *Steps:* suppose option B halves the probability of each scenario rather than removing it; modify the lab to compute the loss avoided; then double both of B's probabilities and recompute. *Expected evidence:* two numbers and a two-sentence recommendation. *Rubric:* 3 = correct values (£4,800 and £9,600) and a recommendation that mentions worst credible events; 2 = numbers right, weak argument; 1 = one number; 0 = none.

### Chapter synthesis

Security decisions are comparisons under uncertainty. Give quantities units, separate expected loss from worst credible harm, check results by estimation and bounding, and say which assumptions would change the decision. A number with no stated source or sensitivity is an opinion in disguise.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes and connection

After this chapter you can (1) describe the layers of a computing system — hardware, firmware, operating system, applications, data and people — and say where security decisions are made in each; (2) distinguish information technology (IT) from operational technology (OT) and explain why their priorities differ; (3) describe the life cycle of a device in a critical service, from procurement to disposal; and (4) explain why the oldest component in a system often sets its security. It builds on Chapter 1's habit of explicit quantities and prepares Chapter 3, where you will write code to inspect a device inventory.

### 2.1 Layers and trust

A computer is a stack. At the bottom is **hardware**: processor, memory, storage and interfaces. Above it is **firmware**, the low-level code stored on the device that starts it and controls hardware. The **operating system** (Chapter 11) shares the hardware between programs and enforces who may do what. **Applications** do the work people care about — an infusion-pump drug library, a dispatch system, a payment switch. **Data** is what applications create and consume. **People** configure, use and maintain all of it. Each layer trusts the layers below it: an application cannot be more trustworthy than the operating system it runs on, and an operating system cannot detect firmware that lies to it. This is why secure boot, signed firmware and vendor support matter so much in critical services (Chapter 17).

### 2.2 IT and OT

**Information technology** handles information: email, records, payments, scheduling. **Operational technology** monitors and controls physical processes: valves, breakers, pumps, signals, ventilators. NIST describes OT as systems that "interact with the physical environment (or manage devices that interact with the physical environment)" ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). The distinction matters because the consequences differ. When an IT system fails, information is unavailable or wrong; when an OT system fails, water may stop, a breaker may not open, or a train may not receive a signal. OT devices are typically expected to run for 15–25 years, may not tolerate a reboot during operation, and are often certified in a particular configuration so that patching requires vendor approval. Healthcare adds a third category, **medical devices**, which are regulated products whose software cannot simply be changed by the hospital.

### 2.3 The device life cycle

Security is decided long before an attack. At **procurement**, a buyer can require supported software, a vulnerability-disclosure process and a software bill of materials (SBOM — a list of software components, see [CISA SBOM](https://www.cisa.gov/sbom)). At **installation**, defaults can be changed and the device placed in the right network zone. During **operation**, it needs monitoring, patching where possible and compensating controls where not. At **end of support**, the vendor stops issuing fixes; the device still works, which is exactly why it stays in service. At **disposal**, data must be removed. A hospital imaging workstation bought in 2014 on an operating system whose support ended in 2020 is not a careless anomaly; it is the normal consequence of a 15-year medical device on a 10-year operating system.

### 2.4 Worked example: Calder Valley Hospital imaging (synthetic)

**This case is synthetic.** CVH's imaging department runs workstation IMG-01, attached to a scanner certified by its manufacturer with a specific operating system that reached end of support in 2020. The manufacturer offers an upgrade only with a new scanner (£400,000). Options are: (a) replace now; (b) keep it and isolate it — allow only the connections it needs to the image archive, remove email and web browsing, monitor its traffic; (c) do nothing. Option (c) leaves a known-unpatched machine on a flat clinical network. Option (a) removes the risk but costs a capital budget the hospital does not have this year. Option (b) is the usual answer: a **compensating control** that reduces exposure until replacement, with a named owner and a replacement date. The decision record says which risk remains — a malicious file arriving through the archive connection — and how it is monitored.

### 2.5 Practical activity

Choose one device you use daily (a phone, a home router, a laptop). Without opening it or changing anything, find from the vendor's public pages: its firmware or OS version, whether it is still supported, and how updates are delivered. Write a five-line life-cycle note: procurement, installation, operation, end of support, disposal. Do the same for one *imagined* device in a critical service — a CVH infusion pump — and list what you would need to ask its vendor.

For the pump, ask the vendor about the drug-library update process, the support end date for its firmware and who may install updates.

### 2.6 Common errors and limits

- Assuming "it still works" means "it is still safe": unsupported devices accumulate unfixed vulnerabilities.
- Treating OT like IT: rebooting a controller during operation, or scanning it aggressively, can disrupt the physical process.
- Ignoring firmware: it is code, it has vulnerabilities, and it is rarely inventoried.
- Forgetting people as a layer: most systems are configured by someone under time pressure.

At CVH the four errors meet in IMG-01: it still works, so it stayed on the clinical network; its scanner certification makes it OT-like in its patch constraints; nobody listed its firmware; and the radiographers who use it chose the shared desktop settings. The limit of this chapter is that it names layers without measuring how many devices sit in each.

### Exercises — chapter 2

**EX003 — Locate the decision.** *Objective:* connect layers to controls. *Inputs:* five controls: signed firmware updates, operating-system user accounts, an application's drug-library limits, database backups, staff training. *Steps:* assign each to a layer and state one failure each control does not address. *Expected evidence:* a five-row table. *Rubric:* 3 = correct layers and a plausible gap for each; 2 = one error; 1 = layers only; 0 = none.

**EX004 — IT or OT?** *Objective:* reason about consequences. *Inputs:* CPN's billing system, CPN's feeder RTU, CVH's patient-administration system, CVH's BMS that controls theatre ventilation. *Steps:* classify each as IT, OT or medical device; name the worst plausible consequence of its failure; say whether a vendor-approved patch window is likely needed. *Expected evidence:* table and two sentences on the BMS. *Rubric:* 3 = correct classes, consequences tied to physical effects for OT; 2 = minor slip; 1 = classes only; 0 = none.

### Chapter synthesis

Computing systems are stacks of trust, from hardware to people. OT and medical devices control physical outcomes, live for decades and cannot always be patched, so security relies on procurement terms, placement and compensating controls. The oldest, least-supported component often defines the real exposure.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 40

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes and connection

After this chapter you can (1) write short Python programs using variables, conditions, loops, functions, lists and dictionaries; (2) read structured text (CSV) with the standard library; (3) turn a question about a system ("which devices are past end of support?") into a filter, a count and a report; and (4) test a program against a small case whose answer you already know. It builds on Chapter 2's device life cycle and prepares Chapter 8, where programs become robust against bad input.

### 3.1 Why a security student programs

Security work in critical services is mostly about knowing what you have and noticing what changed. Both need data processing: inventories with thousands of rows, logs with millions of lines, advisories published daily. A spreadsheet works for fifty rows; a short program works for fifty thousand and can be rerun tomorrow. Python is used here because its standard library reads CSV, JSON, dates and databases without installing anything, and because readable code is easier to review — a property that matters when your output informs a decision about patient safety.

### 3.2 The core constructs

A **variable** names a value (`year = 2026`). A **condition** chooses between paths (`if eos < year:`). A **loop** repeats work for each item (`for row in rows:`). A **function** packages a step with a name and inputs so it can be tested alone. A **list** holds items in order; a **dictionary** maps keys to values (`row["os"]`). The `csv` module turns each line of a CSV file into a dictionary keyed by the header. The `collections.Counter` class counts how often each value appears. With these you can answer most inventory questions.

Two disciplines matter from the start. First, **test against a known answer**: before running on the real file, run on five rows you checked by hand. Second, **print what you excluded**, not only what you found: a filter that silently drops rows with a blank date will report "no unsupported devices" for exactly the devices nobody documented.

### 3.3 Worked example and Lab 2: CVH inventory triage (synthetic)

**This case is synthetic.** CVH's clinical engineering team exports an eight-row sample of its device inventory. The question: which devices run software past its end of support, where are they, and are any non-clinical devices sitting on the clinical network?

```python
# Lab 2 - triage a synthetic hospital device inventory with the standard library (offline)
import csv, io
from collections import Counter
DATA = """asset,type,os,os_end_of_support,network,clinical
INF-01,infusion pump,RTOS-x 2.1,2030,clinical-vlan,yes
INF-02,infusion pump,RTOS-x 1.4,2021,clinical-vlan,yes
IMG-01,imaging workstation,Windows 7,2020,clinical-vlan,yes
IMG-02,imaging workstation,Windows 10,2025,clinical-vlan,yes
LAB-01,lab analyser,Linux 3.10,2019,lab-vlan,yes
ADM-01,office pc,Windows 11,2031,corporate,no
ADM-02,office pc,Windows 10,2025,clinical-vlan,no
BMS-01,building controller,vendor fw 4,2027,bms-vlan,no
"""
YEAR = 2026
rows = list(csv.DictReader(io.StringIO(DATA)))
unsupported = [r for r in rows if int(r["os_end_of_support"]) < YEAR]
print("assets:", len(rows), "| unsupported:", len(unsupported))
for r in unsupported:
    print(f"  {r['asset']:7} {r['type']:20} {r['os']:12} EoS {r['os_end_of_support']} clinical={r['clinical']}")
print("by network:", dict(Counter(r["network"] for r in unsupported)))
misplaced = [r["asset"] for r in rows if r["clinical"] == "no" and r["network"] == "clinical-vlan"]
print("non-clinical devices on clinical VLAN:", misplaced)
```

Expected output:

```text
assets: 8 | unsupported: 5
  INF-02  infusion pump        RTOS-x 1.4   EoS 2021 clinical=yes
  IMG-01  imaging workstation  Windows 7    EoS 2020 clinical=yes
  IMG-02  imaging workstation  Windows 10   EoS 2025 clinical=yes
  LAB-01  lab analyser         Linux 3.10   EoS 2019 clinical=yes
  ADM-02  office pc            Windows 10   EoS 2025 clinical=no
by network: {'clinical-vlan': 4, 'lab-vlan': 1}
non-clinical devices on clinical VLAN: ['ADM-02']
```

Interpretation: four clinical devices are unsupported, which is a replacement-planning problem with compensating controls (Chapter 2). ADM-02 is different: an unsupported office PC on the clinical network is the cheapest finding to fix — upgrade it and move it. The rows are teaching data: the device labels are invented, and although some operating-system names are familiar, treat every end-of-support year here as sample input and check any real product against its vendor's published lifecycle page.

### 3.4 Practical activity

Extend Lab 2: (1) add a row with an empty `os_end_of_support` and observe the error; (2) change the program so such rows are reported as "unknown — needs owner" rather than crashing or being skipped; (3) write one `assert` that checks the count of unsupported devices for the original eight rows is 5.

Step (2) is the important one. A row reported as "unknown — needs owner" puts a name on a gap; a skipped row hides it, and a crash stops the report for everyone. The `assert` in step (3) is a test with a known answer: if a later change to the filter makes it print 4 or 6, the test fails before anyone reads a wrong report.

### 3.5 Common errors and limits

- Comparing numbers stored as text (`"2025" < "2026"` happens to work; `"9" < "10"` does not).
- Silently skipping malformed rows.
- Hard-coding the current year so the report goes stale; read it from the clock, but keep it fixed in tests.
- Treating an inventory export as the truth: it is only as good as the last person who updated it (Chapter 22).

In Lab 2 the second error would have hidden VEN-01 in EX005, the third would have made the 2025 devices look supported again if the year were left at 2025, and the fourth applies to the whole export: ADM-02 appears on the clinical VLAN only because someone recorded its network correctly.

### Exercises — chapter 3

**EX005 — Unknowns are findings.** *Objective:* make missing data visible. *Inputs:* Lab 2 plus a ninth row `VEN-01,ventilator,,,clinical-vlan,yes`. *Steps:* modify the program to print an "unknown" section; explain why an unknown support date on a ventilator should be escalated. *Expected evidence:* code change, output and two sentences. *Rubric:* 3 = no crash, VEN-01 reported as unknown, escalation reason tied to clinical consequence; 2 = works without reasoning; 1 = crash avoided by skipping; 0 = none.

**EX006 — A function you can test.** *Objective:* separate logic from data. *Inputs:* Lab 2. *Steps:* write `def is_unsupported(row, year) -> bool`, test it with three hand-made rows (supported, unsupported, boundary year equal to `year`), and state your rule for the boundary. *Expected evidence:* function, tests and the rule. *Rubric:* 3 = correct function, all three tests, boundary rule stated and justified; 2 = boundary not discussed; 1 = function only; 0 = none.

### Chapter synthesis

Short, readable programs turn inventories into decisions. Filter, count and report — and always report what you could not classify. Test against cases you know, keep logic in functions, and remember that the program is only as true as its data.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 40

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes and connection

After this chapter you can (1) structure a short technical argument as claim, evidence, reasoning and limits; (2) cite sources so that a reader can find exactly what you relied on; (3) write for two audiences at once — a specialist who will check your reasoning and a decision-maker who has five minutes; and (4) distinguish your own analysis from what a source says. It builds on Chapter 1's explicit assumptions and prepares Chapter 18 (research methods) and the capstone thesis (Chapter 40).

### 4.1 Writing is part of the security work

In critical services, much security work ends as a document: a risk assessment, an incident report, a recommendation to a board, a submission to a regulator. A correct analysis that is badly written is often ignored; a well-written analysis with a hidden assumption can mislead a whole organisation. Academic writing is training for both problems. Its core is the **argument**: a claim supported by evidence through stated reasoning, with its limits acknowledged. Toulmin's model names these parts — claim, data (evidence), warrant (the reasoning that connects them), backing, qualifier and rebuttal ([Toulmin, *The Uses of Argument*](https://doi.org/10.1017/CBO9780511840005)). You do not need the vocabulary in every paragraph, but you should be able to point to each part.

### 4.2 Structure for two readers

Put the conclusion first. A decision-maker reads the first paragraph; a specialist reads everything. A useful structure for a short report is: **summary** (the recommendation and its main reason, in three sentences); **context** (what service, what question, what scope); **evidence** (what you examined and found, with sources); **analysis** (how the evidence supports the recommendation, and the alternatives you compared); **limits** (what you did not examine, what would change your conclusion); **references**. Use headings that say something ("Unsupported devices are concentrated in imaging") rather than labels ("Findings").

### 4.3 Citation and honesty

Cite a source whenever you state a fact you did not establish yourself, and cite the specific document — the NIST publication number and revision, the agency advisory identifier, the article's DOI — not "according to NIST". Quote sparingly and exactly; paraphrase in your own words and still cite. Separate **reporting** ("CISA's advisory states that…") from **inference** ("this suggests that…") from **recommendation** ("CVH should…"). Never cite a source you have not read; if you rely on a summary of a paywalled standard, cite the summary. Generative tools can draft fluent text that contains invented citations: every reference in your work must be one you opened and checked.

### 4.4 Worked example: rewriting a weak paragraph (synthetic)

**Weak (synthetic student draft):** "Hospitals are very vulnerable to cyber attacks, as everyone knows from WannaCry. CVH has lots of old computers so it is at high risk and should buy a new firewall."

Problems: an unsupported universal claim ("everyone knows"); a real incident used without a source or a precise lesson; "lots" and "high" without numbers; a recommendation that does not follow from the evidence (old computers are not fixed by a firewall).

**Revised:** "The UK National Audit Office found that the 2017 WannaCry ransomware disrupted at least a third of NHS trusts in England, and that affected organisations had unpatched or unsupported Windows systems ([NAO, 2017](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/)). CVH's sample inventory shows four of five clinical devices past end of support (Chapter 3, Lab 2). We recommend isolating these devices to the connections they need and setting replacement dates, rather than relying on a perimeter firewall, because the NAO case shows harm spreading inside hospital networks. This recommendation assumes the sample is representative; a full inventory is needed to confirm it."

### 4.5 Practical activity

Take a one-page news article about any infrastructure incident. Write a 250-word brief for a hospital director: three-sentence summary, what is known (with the article and any primary source it cites), what is uncertain, and one question CVH should ask itself. Mark each sentence R (reporting), I (inference) or C (recommendation).

A good brief keeps the three kinds of sentence visibly apart. "The utility reported a six-hour outage (R)" is reporting; "the outage probably began in the billing system (I)" is inference and should name its basis; "CVH should check whether its own billing system can stop clinical work (C)" is a recommendation. Where the article cites a primary source, open it and cite that instead.

### 4.6 Common errors and limits

- Burying the conclusion on page four.
- Citing a secondary summary as if it were the primary source.
- Words that hide quantities: "many", "significant", "critical" without a number or definition.
- Recommendations that do not follow from the evidence presented.
- Plagiarism, including close paraphrase without citation and unacknowledged AI-generated text.

The weak paragraph in the worked example shows four of these at once: "everyone knows" hides a source, "lots of old computers" hides a count, "high risk" hides a definition, and "buy a new firewall" does not follow from unsupported devices. The fifth error is the one assessors check mechanically: a sentence close to the NAO report's wording without a citation is plagiarism even if the facts are right.

### Exercises — chapter 4

**EX007 — Find the warrant.** *Objective:* expose hidden reasoning. *Inputs:* "Calder Mutual's payment system had no outage last year, so it is secure." *Steps:* identify claim, evidence and the unstated warrant; explain why the warrant fails; rewrite the claim so it is supported by the evidence. *Expected evidence:* three labelled parts and a rewritten sentence. *Rubric:* 3 = warrant identified ("absence of outage implies absence of weakness"), failure explained, defensible rewrite; 2 = partial; 1 = claim/evidence only; 0 = none.

**EX008 — Summary first.** *Objective:* write for a decision-maker. *Inputs:* the Chapter 1 worked example. *Steps:* write a 120-word summary recommending option B, including the main reason, the main assumption and what would change the recommendation. *Expected evidence:* the summary. *Rubric:* 3 = recommendation in the first sentence, reason, assumption and reversal condition, ≤ 120 words; 2 = one element missing; 1 = recommendation buried; 0 = none.

### Chapter synthesis

Good security writing states a claim, shows the evidence, makes the reasoning explicit and admits the limits — conclusion first, sources exact, reporting kept apart from inference and recommendation. Write as if a specialist will check every sentence and a decision-maker will read only the first three.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 40

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes and connection

After this chapter you can (1) define confidentiality, integrity and availability and explain why critical services often rank them differently from office IT; (2) use the vocabulary asset, threat, vulnerability, likelihood, impact, risk and control correctly; (3) describe the main classes of threat actor and attack technique at a conceptual level; and (4) read a security advisory and extract what it means for a given organisation. It builds on Chapters 1–4 and prepares Chapter 16 (architecture) and Chapter 19 (the field's scope).

### 5.1 The vocabulary

An **asset** is something of value: a service, a system, data, a building, people's time. A **threat** is a potential cause of harm — an actor (a criminal group, an insider, a state) or an event (a flood, a failed update). A **vulnerability** is a weakness a threat can exploit: an unpatched flaw, a shared password, a single cable route. **Likelihood** is how probable it is that a threat exploits a vulnerability in a period; **impact** is the harm if it does. **Risk** combines them — informally "likelihood × impact", though Chapter 23 shows why the multiplication is often misleading. A **control** (or safeguard) is a measure that reduces likelihood or impact. NIST's risk-assessment guide sets out this vocabulary and process ([SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)).

### 5.2 The CIA triad in critical services

**Confidentiality** means information is disclosed only to those authorised; **integrity** means information and systems are not altered without authorisation; **availability** means they work when needed. Office IT often puts confidentiality first because breaches of personal data carry legal and reputational costs. In OT, the order is often reversed: a water utility cares first that pumps run (availability) and that commands and readings are genuine (integrity); the secrecy of a tank level matters much less. NIST's OT guide makes this point and adds **safety** as an overriding concern ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). Healthcare mixes both: patient records demand confidentiality, while infusion pumps and ventilators demand integrity and availability. A security professional in a critical sector must ask, for each asset, which property failing would hurt people first.

### 5.3 Actors and techniques

Threat actors differ in motive and capability. **Criminal groups** seek money, most visibly through ransomware that encrypts data and threatens to publish it. **State-sponsored groups** may seek intelligence or the ability to disrupt services in a crisis. **Hacktivists** seek attention. **Insiders** may be malicious or, far more often, make mistakes. **Accidents** — failed updates, misconfigurations, cut cables — cause many outages without any adversary. Techniques are catalogued in public knowledge bases such as MITRE ATT&CK; the version for industrial control systems lists tactics from initial access to "impair process control" ([MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)). At bachelor's level you should be able to read such a catalogue and say which techniques a control addresses; you are not asked to perform them.

### 5.4 Worked example: reading an advisory for CPN (synthetic)

**This case is synthetic.** A vendor advisory (invented) states: "Remote-access gateway VPN-G versions before 9.3 allow an unauthenticated attacker to execute code. Exploitation has been observed. Fixed in 9.3." Calder Power Networks runs VPN-G 9.1 at head office, reachable from the internet, used by engineers to reach the control network.

Extract: *asset* — the gateway and everything reachable through it; *vulnerability* — the flaw in 9.1; *threat* — any actor scanning the internet, made more likely by observed exploitation; *impact* — potential access to the control network, hence to feeder operation; *control options* — upgrade to 9.3 now, or disable the gateway until upgraded and use a supervised alternative. Public catalogues such as CISA's Known Exploited Vulnerabilities list exist precisely to raise the priority of flaws exploited in the wild ([CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)). The decision is not difficult; the literacy lies in recognising that "remote access to OT" plus "exploited" plus "internet-facing" outranks a higher-scored flaw on an isolated device.

### 5.5 Practical activity

Pick one recent advisory from [CISA's ICS advisories](https://www.cisa.gov/news-events/ics-advisories). Without testing anything, extract asset, vulnerability, affected versions, exploitation status, vendor fix and recommended mitigations. Then write two sentences on how the priority would change for an operator whose device is (a) internet-facing and (b) on an isolated network.

Write the exposure answer as a change in priority with a reason, not a new score. Internet-facing plus exploited usually moves an advisory to emergency handling, as with CPN's VPN-G 9.1; the same flaw on a device reachable only from an isolated cell can wait for the next planned window if compensating controls are checked.

### 5.6 Common errors and limits

- Using "threat", "vulnerability" and "risk" interchangeably.
- Assuming confidentiality always comes first.
- Treating every incident as an attack; many outages are accidents, and the response differs.
- Learning attack techniques operationally without authorisation (Chapter 10).

EX010 shows the first error: calling the cable cut a vulnerability confuses the threat (roadworks) with the weakness (a single cable route). The second makes a CW dosing controller look like a privacy problem when integrity is what protects customers. The third treats a cut cable or a failed update as an incident to investigate for an attacker, delaying repair. The fourth is why every lab here is offline.

### Exercises — chapter 5

**EX009 — Rank the properties.** *Objective:* apply CIA by asset. *Inputs:* CVH patient records; CW chlorine-dosing controller; Calder Mutual's card-authorisation service; CEDC's call recordings. *Steps:* rank C, I and A for each and justify the top property in one sentence. *Expected evidence:* table. *Rubric:* 3 = defensible rankings with harm-based reasons (dosing: integrity/safety first); 2 = one weak; 1 = rankings without reasons; 0 = none.

**EX010 — Vocabulary under pressure.** *Objective:* use terms precisely. *Inputs:* "The risk is that the cable is cut by roadworks, which is a vulnerability for CEDC." *Steps:* rewrite using asset, threat, vulnerability and impact correctly. *Expected evidence:* one or two sentences. *Rubric:* 3 = roadworks as threat, single cable route as vulnerability, dispatch availability as impact; 2 = one term misplaced; 1 = two misplaced; 0 = none.

### Chapter synthesis

Security literacy is precise vocabulary applied to real consequences. Assets, threats, vulnerabilities, likelihood, impact and controls are distinct ideas. In critical services availability, integrity and safety often outrank confidentiality, and the right priority for an advisory depends on exposure and exploitation, not on a score alone.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 40

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes and connection

After this chapter you can (1) use sets and set operations to reason about inventories and permissions; (2) write logical conditions and check them with truth tables; (3) model dependencies between services as a directed graph and compute what is affected when one node fails; and (4) recognise when an exhaustive check is feasible and when the number of states makes it impossible. It builds on Chapter 3's programming and prepares Chapter 13 (access), Chapter 22 (dependencies) and Chapter 28 (failure analysis).

### 6.1 Sets and relations

A **set** is a collection of distinct items. The devices on the clinical network form a set $C$; the devices past end of support form a set $U$; their **intersection** $C \cap U$ is the set to isolate first. The **union** $A \cup B$ collects items in either; the **difference** $A \setminus B$ keeps items in $A$ but not $B$. Access control is set reasoning: a user's effective permissions are the union of the permissions of their roles, and a separation-of-duties rule says certain pairs must never both be in that union (Chapter 13). A **relation** connects items of two sets — "user *u* holds role *r*", "service *s* depends on service *t*". Many security questions are questions about relations: who can reach what, what depends on what.

### 6.2 Logic

A **proposition** is true or false. Combine propositions with **and** ($\wedge$), **or** ($\vee$) and **not** ($\neg$). A rule such as "a payment above £10,000 is released only if it is created by one person and approved by a different person, or if it is an emergency transfer approved by two directors" is a logical expression; writing it formally exposes gaps ("what if the creator is also a director?"). A **truth table** lists every combination of inputs; with $n$ inputs it has $2^n$ rows. For 4 inputs that is 16 rows — easy. For 40 inputs it is about $10^{12}$ rows — impossible to check by hand, which is why complex systems need structure, testing and argument rather than exhaustive enumeration. **De Morgan's laws** — $\neg(A \wedge B) \equiv \neg A \vee \neg B$ — let you rewrite "not allowed" conditions as "allowed" conditions and check that both say the same thing.

### 6.3 Graphs

A **graph** is a set of nodes and edges. In a **directed graph**, edges have direction; we write $u \to v$ to mean "$v$ depends on $u$". Starting from a failed node, a **breadth-first search** visits every node reachable along edges: that set is everything that can be affected. The number of nodes reachable from a node is its **reach**; nodes with high reach are candidates for extra protection or backup. Graphs also expose **single points of failure**: a node whose removal disconnects services from what they need. Rinaldi, Peerenboom and Kelly's classic paper describes infrastructures as interdependent in exactly this sense — physical, cyber, geographic and logical ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131)).

### 6.4 Worked example and Lab 3: Calder County dependencies (synthetic)

**This case is synthetic.** The CRP drew a first dependency map: the electricity substation feeds water pumps, the hospital's mains supply, the telecom exchange and rail signalling; the telecom exchange carries dispatch, card payments, water telemetry and the hospital's cloud image archive.

```python
# Lab 3 - cross-sector dependency closure on a directed graph (synthetic Calder County, offline)
from collections import deque
# edge u -> v means "v depends on u"
DEPENDS = {
    "grid-substation-N": ["water-pumps", "hospital-main", "telecom-exchange", "rail-signalling"],
    "telecom-exchange": ["dispatch-cad", "card-payments", "water-telemetry", "hospital-pacs-cloud"],
    "water-pumps": ["hospital-water"],
    "water-telemetry": ["water-pumps"],
    "dispatch-cad": ["ambulance-dispatch"],
    "hospital-main": [],
    "card-payments": ["fuel-retail"],
    "rail-signalling": [], "hospital-water": [], "hospital-pacs-cloud": [],
    "ambulance-dispatch": [], "fuel-retail": [],
}
def affected(start):
    seen, q = {start}, deque([start])
    while q:
        for v in DEPENDS.get(q.popleft(), []):
            if v not in seen:
                seen.add(v); q.append(v)
    return sorted(seen - {start})
for node in ("grid-substation-N", "telecom-exchange", "water-telemetry"):
    a = affected(node)
    print(f"{node}: {len(a)} affected -> {', '.join(a)}")
fan = sorted(((len(affected(n)), n) for n in DEPENDS), reverse=True)[:3]
print("highest reach:", fan)
```

Expected output:

```text
grid-substation-N: 11 affected -> ambulance-dispatch, card-payments, dispatch-cad, fuel-retail, hospital-main, hospital-pacs-cloud, hospital-water, rail-signalling, telecom-exchange, water-pumps, water-telemetry
telecom-exchange: 8 affected -> ambulance-dispatch, card-payments, dispatch-cad, fuel-retail, hospital-pacs-cloud, hospital-water, water-pumps, water-telemetry
water-telemetry: 2 affected -> hospital-water, water-pumps
highest reach: [(11, 'grid-substation-N'), (8, 'telecom-exchange'), (2, 'water-telemetry')]
```

Read the result carefully. The graph says *can be affected*, not *will fail*: it ignores backup power, storage and manual operation. That is deliberate — the first map finds where to look; Chapter 22 adds time and backup autonomy. It also reveals a modelling choice: water pumps depend on telemetry here only if they cannot run locally. Every edge is a claim that someone should be able to justify.

### 6.5 Practical activity

Add an edge you think is missing (for example, the hospital's water depends on the water-treatment works, which depends on the substation) and an alternative path (a second telecom exchange). Recompute reach. Write three sentences on what the change does and does not show.

Adding "treatment works → hospital water" and "substation → treatment works" raises the substation's reach further, while a second exchange removes nothing from the plain reachability count: the search still marks every node that one path can reach. That is the limitation EX012 asks you to explain, and it is the reason to write AND and OR dependencies differently.

### 6.6 Common errors and limits

- Confusing edge direction ("depends on" versus "supplies"); write the convention at the top of every diagram.
- Treating reachability as certainty of failure.
- Building a graph from one organisation's view: other operators know dependencies you do not.
- Trying to enumerate state spaces that are exponentially large.

In Lab 3 the convention line `edge u -> v means "v depends on u"` is what makes the 11-node reach of the substation readable; reversed, the same list would claim the substation depends on fuel retail. Reach of 11 means exposure, not failure, since the hospital has 72 hours of generator autonomy. The map is CRP's first view and lacks what CW and CPN engineers know. And the truth table argument scales the other way: 40 binary inputs give about a trillion rows.

### Exercises — chapter 6

**EX011 — Sets for triage.** *Objective:* use set operations. *Inputs:* C = {INF-01, INF-02, IMG-01, IMG-02, ADM-02}; U = {INF-02, IMG-01, IMG-02, LAB-01, ADM-02}; K (devices with a known exploited flaw) = {IMG-01, ADM-02}. *Steps:* compute $C \cap U$, $(C \cap U) \cap K$ and $U \setminus C$; say which set you would act on first and why. *Expected evidence:* three sets and a reason. *Rubric:* 3 = all correct and priority to $(C \cap U) \cap K$ = {IMG-01, ADM-02}; 2 = one error; 1 = two errors; 0 = none.

**EX012 — An alternative path.** *Objective:* see how redundancy changes reach. *Inputs:* Lab 3. *Steps:* model that dispatch-cad can also use a satellite link independent of the exchange, so losing the exchange alone no longer stops dispatch. Explain why a simple reachability search cannot express this, and propose a modelling change. *Expected evidence:* explanation and proposal. *Rubric:* 3 = recognises OR-dependency (needs any one of several suppliers) versus AND-dependency, proposes nodes requiring all/any inputs; 2 = recognises problem only; 1 = edits edges incorrectly; 0 = none.

### Chapter synthesis

Sets describe inventories and permissions; logic makes rules exact and checkable; graphs make dependencies visible and computable. Each model answers a narrower question than it seems to: reachability shows exposure, not failure, and exhaustive checking only works while the state space is small.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 40

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes and connection

After this chapter you can (1) explain layering, addressing, ports and the difference between a connection's client and server; (2) describe how industrial protocols such as Modbus differ from modern internet protocols in their security assumptions; (3) express a network-segmentation policy as zones, conduits and an allowlist; and (4) check observed flows against that policy and interpret the violations. It builds on Chapters 3 and 6 and prepares Chapter 16 (architecture) and Chapter 24 (controls).

### 7.1 Layers, addresses and ports

Networks are built in layers. The **link** layer moves frames between neighbouring devices (Ethernet, Wi-Fi). The **internet** layer moves packets between networks using IP addresses. The **transport** layer provides either a reliable byte stream (TCP; see [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)) or individual datagrams (UDP), and uses **port numbers** to identify the service on a host. The **application** layer carries the meaning: HTTPS for web, Modbus/TCP on port 502 for industrial polling, OPC UA commonly on port 4840. In a TCP connection the **client** opens the connection to the server's listening port; the reply uses the same connection. Who initiates is security-relevant: a field controller that suddenly *opens* connections to the control room is behaving differently from one that only answers.

### 7.2 Industrial protocols and their assumptions

Many industrial protocols were designed for closed serial links in the 1970s–1990s. Modbus, for example, defines function codes to read and write registers and coils, and its classic form has no authentication: any device that can send a well-formed request to a controller can ask it to write ([Modbus specification](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf)). This is not a bug in an implementation; it is the design assumption that only trusted devices can reach the wire. Once such protocols run over IP networks, that assumption must be enforced by the network: segmentation, allowlists and monitoring. Modern protocols add security (TLS 1.3 provides authenticated, encrypted channels — [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)), but upgrading thousands of field devices takes decades.

### 7.3 Zones, conduits and allowlists

A **zone** is a group of assets with similar security requirements; a **conduit** is the controlled communication path between zones. The ISA/IEC 62443 series uses these terms for industrial systems ([ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). A typical utility has a corporate zone, a demilitarised zone (DMZ) where data is exchanged, a control zone (SCADA servers, operator HMIs) and a field zone (controllers, RTUs). An **allowlist** policy names the flows that are allowed — source zone, destination zone, port, purpose — and denies everything else. The policy is only half the control; the other half is checking that observed traffic matches it.

### 7.4 Worked example and Lab 4: checking CW's flows (synthetic)

**This case is synthetic.** Calder Water allows three conduits: corporate users view the historian in the DMZ over HTTPS; a collector in the DMZ reads from the control zone over OPC UA; the SCADA server polls field controllers over Modbus/TCP. A one-hour flow summary is checked against the policy.

```python
# Lab 4 - check observed flows against a zone-and-conduit allowlist (synthetic, offline)
ALLOW = {  # (source zone, destination zone, destination port): purpose
    ("corporate", "dmz", 443): "historian web view",
    ("dmz", "control", 4840): "OPC UA read from historian replica collector",
    ("control", "field", 502): "Modbus/TCP polling of field controllers",
}
ZONE = {"10.1.": "corporate", "10.5.": "dmz", "10.20.": "control", "10.30.": "field"}
def zone(ip):
    return next((z for p, z in ZONE.items() if ip.startswith(p)), "unknown")
FLOWS = [  # src, dst, dport  (synthetic NetFlow-style summary)
    ("10.1.4.22", "10.5.0.10", 443), ("10.5.0.11", "10.20.0.5", 4840),
    ("10.20.0.5", "10.30.1.7", 502), ("10.1.4.80", "10.20.0.5", 3389),
    ("10.20.0.9", "198.51.100.23", 443), ("10.30.1.7", "10.20.0.5", 502),
]
for s, d, p in FLOWS:
    key = (zone(s), zone(d), p)
    verdict = ALLOW.get(key)
    print(f"{s:>13} -> {d:<14} :{p:<5} {key[0]:>9}->{key[1]:<8} {'ALLOW ' + verdict if verdict else 'VIOLATION'}")
```

Expected output:

```text
    10.1.4.22 -> 10.5.0.10      :443   corporate->dmz      ALLOW historian web view
    10.5.0.11 -> 10.20.0.5      :4840        dmz->control  ALLOW OPC UA read from historian replica collector
    10.20.0.5 -> 10.30.1.7      :502     control->field    ALLOW Modbus/TCP polling of field controllers
    10.1.4.80 -> 10.20.0.5      :3389  corporate->control  VIOLATION
    10.20.0.9 -> 198.51.100.23  :443     control->unknown  VIOLATION
    10.30.1.7 -> 10.20.0.5      :502       field->control  VIOLATION
```

Three violations, three different meanings. A remote-desktop connection (port 3389) from corporate straight into the control zone bypasses the DMZ — perhaps an engineer's shortcut, perhaps an intruder. A control-zone host reaching an internet address (198.51.100.23 is a documentation address standing in for a real one) may be a vendor's update check or data leaving. A field device *initiating* Modbus to the SCADA server reverses the normal direction. None proves an attack; each needs an owner to explain it, and the explanation becomes evidence (Chapter 15).

### 7.5 Practical activity

On a computer you own, list your own active connections (for example with `netstat` or `ss`) and classify five as client or server, local or remote, and expected or unexpected. Do not scan any other system.

Use the state column of `ss` or `netstat`: a local address with a listening port is a server; a connection to a remote port 443 is a client. Mark anything you cannot explain and find the program behind it with your operating system's tools on your own machine.

### 7.6 Common errors and limits

- Writing allowlists by port alone, ignoring source and destination zones.
- Assuming "internal" means "trusted".
- Confusing reply traffic with initiated connections when reading flow logs.
- Treating a violation as proof of compromise rather than as a question.

Lab 4 shows why: a port-only rule allowing 502 would have passed the field device that initiated Modbus to the SCADA server, a reversal of the normal direction. The corporate RDP connection into control is "internal" and still a violation. In flow logs, the SCADA server's replies on 502 are not new connections and must not be read as such. And each of the three violations goes to an owner as a question first.

### Exercises — chapter 7

**EX013 — Explain the violations.** *Objective:* reason from flows to hypotheses. *Inputs:* Lab 4 output. *Steps:* for each violation give one benign and one malicious explanation, and the evidence that would distinguish them. *Expected evidence:* a three-row table. *Rubric:* 3 = plausible pairs and specific distinguishing evidence (change tickets, user logins, destination ownership, device configuration); 2 = generic evidence; 1 = explanations only; 0 = none.

**EX014 — Least flow.** *Objective:* tighten a policy. *Inputs:* the ALLOW table. *Steps:* propose two refinements that make the policy narrower without breaking its purposes (for example, host-level rather than zone-level rules, read-only function codes) and say how each would be enforced and checked. *Expected evidence:* two refinements with enforcement and check. *Rubric:* 3 = both narrower, enforceable and checkable; 2 = one; 1 = vague; 0 = none.

### Chapter synthesis

Networks carry the assumptions of their protocols. Classic industrial protocols trust whoever can reach them, so critical services enforce trust with zones, conduits and allowlists — and then check observed flows against the policy. A violation is a question to an owner, not a verdict.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 40

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes and connection

After this chapter you can (1) validate untrusted input with explicit rules and reject what does not conform; (2) handle errors so that a program fails safely and visibly; (3) write unit tests, including tests for boundary and malformed cases; and (4) explain why parsing is a security boundary. It builds on Chapter 3 and Chapter 7 and prepares Chapter 9 (data) and Chapter 27 (verification).

### 8.1 Input is a security boundary

Every program that reads data from outside — a file, a network message, an operator's entry — makes assumptions about it. When the assumptions are wrong, programs crash, mis-compute or, worse, do something an attacker chose. Software weakness catalogues are dominated by input-handling errors: injection, out-of-bounds reads and writes, improper input validation ([CWE Top 25](https://cwe.mitre.org/top25/)). The defensive pattern is to **parse, don't guess**: define exactly what valid input looks like, convert raw text into typed values in one place, and reject anything else with a clear error.

### 8.2 Validation rules

For a setpoint sent to a pumping station, valid input might be: a number; finite (not "NaN" or infinity); within engineering limits (0.5–4.5 m); changing by no more than 0.5 m from the current value; from an authorised source. Each rule should be explicit, tested and logged when it rejects. **Allowlisting** (accept only known-good forms) is stronger than **denylisting** (reject known-bad forms) because attackers find forms you did not think of. Python's `float("nan")` succeeds, and `nan < 0.5` and `nan > 4.5` are both false — so a range check written as "reject if below or above" quietly *accepts* NaN. The robust check is "accept only if `math.isfinite(x)` and `0.5 <= x <= 4.5`".

### 8.3 Errors and failing safely

When validation fails, the program must do something defined: reject the command and keep the last good value, raise an alarm, log the reason. It must not continue with a default that happens to be dangerous (a setpoint of zero), and it must not swallow the error silently (`except: pass`). In control contexts, "safe" is a process decision — a valve may need to fail closed for chlorine but open for cooling water — so the programmer implements a failure state that the process owner has specified, rather than inventing one.

### 8.4 Testing

A **unit test** checks one function against known cases. Good test sets include **typical** values, **boundaries** (exactly 0.5 and 4.5), **just outside** boundaries (0.49, 4.51), **malformed** inputs (empty string, "abc", "1e309", "nan"), and **state-dependent** cases (a valid value that changes too fast). Python's built-in `unittest` module or plain `assert` statements are sufficient at this level. A test that has never failed has never been shown to work: run each new test once against a deliberately broken version.

Run the seven listed tests against both versions as the practical activity asks.

### 8.5 Worked example: CW setpoint validator (synthetic)

**This case is synthetic.** Calder Water's operator interface sends tank-level setpoints as text. Version 1 of the validator:

```python
def accept_v1(text, current):
    x = float(text)
    if x < 0.5 or x > 4.5: return False
    if abs(x - current) > 0.5: return False
    return True
```

`accept_v1("nan", 3.0)` returns True: both comparisons with NaN are false, and `abs(nan - 3.0) > 0.5` is also false. `accept_v1("abc", 3.0)` raises an exception that, depending on the caller, may crash the interface. Version 2:

```python
import math
def accept_v2(text, current):
    try:
        x = float(text)
    except ValueError:
        return False
    return math.isfinite(x) and 0.5 <= x <= 4.5 and abs(x - current) <= 0.5
```

Version 2 states what is acceptable rather than what is not. Tests: `("3.2", 3.0)` → True; `("4.5", 4.2)` → True; `("4.51", 4.2)` → False; `("nan", 3.0)` → False; `("inf", 3.0)` → False; `("abc", 3.0)` → False; `("2.0", 3.0)` → False (step too large).

The `try` block turns a crash into a rejection, and `math.isfinite` removes NaN and infinity before any comparison. What v2 still does not do is say why it rejected: the operator interface should log which rule failed.

### 8.6 Practical activity

Implement both versions and the seven tests above. Run the tests against v1 and record which fail; then against v2. Add two tests of your own that you think v2 might still get wrong (hint: whitespace, very long strings, a comma decimal separator) and decide whether the behaviour is acceptable.

Against v1, expect the "nan" test to fail (it returns True) and "abc" to raise instead of returning False. Against v2 all seven should pass. For your own tests, " 3.2 " with spaces is accepted by Python's `float`, which is probably fine; "3,2" is rejected, which may surprise an operator using a comma decimal. Decide whether that rejection should produce a clear message rather than silent refusal.

### 8.7 Common errors and limits

- Range checks that pass NaN.
- Catching every exception and continuing.
- Validation in the user interface only, not where the command is executed.
- Tests that only cover typical values.
- Believing validation makes a channel authentic: a valid-looking forged command still passes (Chapter 17 adds authentication).

At CW the third error is the dangerous one: if only the operator interface checks setpoints, any other client that can reach the PLC over Modbus bypasses validation entirely, as Lab 4's field-zone conduit shows. The fifth error links to Lab 8: a well-formed 2.0 m setpoint passes v2 whether an operator or an intruder sent it.

### Exercises — chapter 8

**EX015 — Break v1.** *Objective:* find inputs that defeat a denylist check. *Inputs:* `accept_v1`. *Steps:* find three distinct inputs for which v1 gives an unsafe or undefined result, and explain each. *Expected evidence:* inputs and explanations. *Rubric:* 3 = NaN accepted; non-numeric text (or an empty string) raises an unhandled exception; and a third distinct case, such as a NaN *current* value, which makes the step check pass for any in-range setpoint; 2 = two; 1 = one; 0 = none.

**EX016 — Specify the failure state.** *Objective:* connect code to process safety. *Inputs:* a rejected setpoint at a chlorine-dosing pump and at a raw-water inlet valve. *Steps:* for each, state what the program should do on rejection, who should decide that, and what must be logged. *Expected evidence:* two short specifications. *Rubric:* 3 = keep last good value plus alarm, process owner decides, log fields named (time, source, raw input, rule failed); 2 = partial; 1 = generic; 0 = none.

### Chapter synthesis

Parsing is a security boundary. Define valid input precisely, accept only that, fail into a state the process owner chose, log every rejection and test boundaries and malformed cases. Validation catches malformed input; it does not prove that well-formed input came from someone authorised.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 40

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes and connection

After this chapter you can (1) design a small relational schema with keys; (2) write SQL queries that filter, join and order; (3) explain why data types matter, using version numbers as the example; and (4) prevent SQL injection with parameterised queries. It builds on Chapters 3 and 8 and prepares Chapter 14 (privacy), Chapter 15 (measurement) and Chapter 22 (dependencies).

### 9.1 Why relational data

Security questions combine facts held in different places: which assets exist, what software they run, which advisories affect that software, who owns each asset, which ones face the internet. A **relational database** stores each kind of fact once, in a **table** of rows and columns, and connects tables through **keys** ([Codd, 1970](https://doi.org/10.1145/362384.362685)). A **primary key** identifies a row uniquely (an asset ID); a **foreign key** refers to a row in another table (an asset's product name, matching an advisory's product). A **join** combines rows that match. Storing each fact once avoids the familiar failure of spreadsheets: two copies that disagree.

### 9.2 SQL in four clauses

`SELECT` names the columns you want; `FROM ... JOIN ... ON` names the tables and how they match; `WHERE` filters rows; `ORDER BY` sorts. `GROUP BY` with `COUNT` summarises. Python's standard library includes `sqlite3`, a complete embedded database, so you can practise without a server. Two cautions. First, a join silently drops rows with no match: an asset whose product name is misspelled simply disappears from a vulnerability report. Use a `LEFT JOIN` and look for nulls when completeness matters. Second, **types** decide comparisons. Version strings compared as text put "3.10" before "3.4", because the character "1" sorts before "4".

### 9.3 Injection

If a program builds SQL by pasting user input into a string — `"... WHERE id = '" + user_input + "'"` — an input such as `x' OR '1'='1` changes the query's meaning. This is **SQL injection**, persistently among the most dangerous software weaknesses ([CWE Top 25](https://cwe.mitre.org/top25/)). The fix is structural: **parameterised queries** (`db.execute("... WHERE id = ?", (user_input,))`) send data separately from code, so input can never become SQL.

In Lab 5 every query with an input, such as looking up one asset by ID, should use a `?` placeholder.

### 9.4 Worked example and Lab 5: CPN advisory matching (synthetic)

**This case is synthetic.** Calder Power Networks keeps an asset table and imports vendor advisories. The question: which assets run a version older than the fixed version, ordered so that known-exploited and internet-exposed items come first? A small custom function compares versions numerically.

```python
# Lab 5 - asset and vulnerability joins in SQLite (synthetic Calder Power data, offline)
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE asset(id TEXT PRIMARY KEY, site TEXT, role TEXT, product TEXT, version TEXT, internet_exposed INTEGER);
CREATE TABLE advisory(product TEXT, fixed_in TEXT, severity TEXT, known_exploited INTEGER);
INSERT INTO asset VALUES
 ('RTU-11','Substation North','feeder RTU','RTU-K','3.2',0),
 ('RTU-12','Substation North','feeder RTU','RTU-K','3.4',0),
 ('HMI-01','Control room','operator HMI','HMI-S','7.0',0),
 ('VPN-01','Head office','remote access gateway','VPN-G','9.1',1),
 ('HIS-01','DMZ','historian replica','HIST-P','5.5',0);
INSERT INTO advisory VALUES
 ('RTU-K','3.4','high',0), ('VPN-G','9.3','critical',1), ('HIST-P','5.1','medium',0);
""")
def vkey(v): return tuple(int(x) for x in v.split("."))
db.create_function("vlt", 2, lambda a, b: int(vkey(a) < vkey(b)))
q = """SELECT a.id, a.role, a.version, v.fixed_in, v.severity, v.known_exploited, a.internet_exposed
       FROM asset a JOIN advisory v ON a.product = v.product
       WHERE vlt(a.version, v.fixed_in)
       ORDER BY v.known_exploited DESC, a.internet_exposed DESC, v.severity"""
for row in db.execute(q):
    print(row)
print("string comparison '3.10' < '3.4':", "3.10" < "3.4", "| numeric:", vkey("3.10") < vkey("3.4"))
```

Expected output:

```text
('VPN-01', 'remote access gateway', '9.1', '9.3', 'critical', 1, 1)
('RTU-11', 'feeder RTU', '3.2', '3.4', 'high', 0, 0)
string comparison '3.10' < '3.4': True | numeric: False
```

Two assets need action, the gateway first (this is the Chapter 5 advisory). HMI-01 has no advisory and does not appear; HIS-01 is already past the fix. Note that `ORDER BY v.severity` sorts the *words* alphabetically ("critical" < "high" < "medium"), which happens to be correct here and would be wrong with "low". A severity rank column is the robust design.

### 9.5 Practical activity

(1) Change the join to a `LEFT JOIN` and list assets with no advisory record — is "no advisory" the same as "no vulnerability"? (2) Write a parameterised query that returns one asset by ID; then show, with a deliberately unsafe string-built query on your in-memory database only, how `' OR '1'='1` returns every row.

The `LEFT JOIN` shows HMI-01 with nulls in the advisory columns. "No advisory" means no advisory in this feed for product HMI-S, not that the HMI has no flaw; it may have a vendor bulletin outside the feed or none published yet. For part (2), the unsafe query must only run against your in-memory database, never a real one.

### 9.6 Common errors and limits

- Comparing versions, dates or numbers stored as text.
- Inner joins that silently drop unmatched rows.
- Building SQL with string concatenation.
- Trusting product names to match exactly across vendor feeds and local inventories.

Lab 5 contains two of these errors deliberately. The version comparison would treat "3.10" as older than "3.4" if done as text, wrongly marking an updated RTU as vulnerable. The inner join drops HMI-01 silently. And the product names "RTU-K" and "VPN-G" only join because the sample was typed consistently; real vendor feeds spell products differently and need a mapping table.

### Exercises — chapter 9

**EX017 — Count by site.** *Objective:* summarise with SQL. *Inputs:* Lab 5. *Steps:* write a query that returns, per site, the number of assets needing an update. *Expected evidence:* query and result. *Rubric:* 3 = correct `GROUP BY` with the version filter, result Head office 1, Substation North 1; 2 = counts all assets; 1 = syntax only; 0 = none.

**EX018 — Severity order.** *Objective:* fix a fragile sort. *Inputs:* Lab 5 with an extra advisory severity "low". *Steps:* explain why `ORDER BY severity` would misplace "low", and give two fixes. *Expected evidence:* explanation and fixes. *Rubric:* 3 = alphabetical ordering puts "low" before "medium"; fixes: a numeric rank column or a lookup table/`CASE` expression; 2 = one fix; 1 = explanation only; 0 = none.

### Chapter synthesis

Relational data lets you answer cross-cutting security questions with one query, if keys, types and joins are right. Compare versions numerically, look for what joins drop, rank severities with numbers and never build SQL from untrusted strings.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue studying — chapter 09 of 40

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes and connection

After this chapter you can (1) explain why authorisation, not technical ability, defines legitimate security work; (2) write a simple rules-of-engagement document for an exercise; (3) handle an accidental discovery about a real system through coordinated disclosure; and (4) reason about conflicts between security, safety, privacy and service continuity using a professional code. It builds on Chapters 1–9 and governs every practical activity in the rest of the book.

### 10.1 Authorisation is the line

The same command can be maintenance or a crime. What separates them is **authorisation**: explicit permission from someone entitled to give it, for a defined scope, time and method. Most jurisdictions criminalise unauthorised access to computer systems, and in critical services unauthorised testing can also endanger people: a scan that is harmless to a laptop can crash a controller. So this book's rule is simple and absolute — practical work uses the book's synthetic labs, systems you own, or systems whose owner has given written, specific permission. Curiosity about a real utility's exposed device is not permission.

### 10.2 Rules of engagement

Authorised exercises are written down in **rules of engagement** (RoE): who authorises (by name and role); scope (which systems, which addresses, explicitly what is excluded — safety systems usually are); time window; permitted methods; stop conditions ("any unexpected process alarm: stop and call the shift engineer"); communication plan; handling of data found; and how results will be reported. An RoE protects the service, the organisation and the tester. In OT, the RoE is usually agreed with operations and safety engineers, not only the IT security team, and often limits testing to passive observation or offline replicas.

### 10.3 Disclosure

If you find a vulnerability by accident — a public page exposing a control interface, a misdirected email — the ethical path is to stop, not to explore further, and to report privately to the owner or through a coordinator. **Coordinated vulnerability disclosure** gives the owner or vendor time to fix before details are published; national bodies such as CISA run programmes that coordinate between finders and vendors ([CISA CVD programme](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program)). Record what you saw and when, keep it confidential, and do not retain data you were not entitled to access.

### 10.4 Professional codes and conflicts

The ACM Code of Ethics asks computing professionals to contribute to society and human well-being, avoid harm, be honest and respect privacy, and to "access computing and communication resources only when authorized or when compelled by the public good" ([ACM Code, 2018](https://www.acm.org/code-of-ethics)). Real dilemmas set these duties against each other. Should a hospital delay a security patch to a ventilator fleet because the update requires taking devices out of service during a respiratory-illness peak? Should a utility share an incident's details with other utilities when its lawyers advise silence? A structured approach helps: identify stakeholders and harms; identify duties and who holds them; consider alternatives (patch a subset, add a compensating control); decide; record the reasoning and who accepted the residual risk.

### 10.5 Worked example: the open HMI (synthetic)

**This case is synthetic.** A student searching for internship information on Calder Water's public website follows a link that opens a web page titled "Pump Station 4 — operator view". No password was requested. The ethical response: do not click anything on the page, do not try other links, take one screenshot of the address bar and title only if needed to report, close the page, and email CW's published security contact (or, if none, the national CERT/CSIRT) saying what was seen, when and how it was reached. Do not post about it. Do not "check whether it is really live". The student's university ethics adviser should be informed. In this synthetic case CW thanks the student, removes the link and finds that the page was a vendor demonstration left on a web server — a reminder that the finder rarely knows the full picture.

### 10.6 Practical activity

Write a one-page RoE for Laboratory I (Chapter 25), which runs only the book's offline labs on your own computer. Even for a trivial scope, fill every heading: authoriser, scope, exclusions, window, methods, stop conditions, data handling and reporting.

For the stop conditions, "any unexpected behaviour of my own computer, or any attempt by a script to reach the network" is specific and observable. Name yourself as authoriser and tester for the scope, and your tutor as the person told if a stop condition occurs.

### 10.7 Common errors and limits

- "It was publicly reachable, so it was allowed."
- Verbal authorisation, or authorisation from someone who does not own the system.
- Scope creep during a test ("while I'm here…").
- Keeping data found during a test after the engagement.
- Treating ethics as a compliance checklist rather than a reasoning duty.

The open-HMI worked example tests the first three. The page was publicly reachable, but nobody at CW authorised a visit; a classmate saying "go ahead" does not own the system; and clicking "just one more link" to check whether it is live is scope creep. The fourth would apply if the student kept the screenshot after reporting. The fifth is why the student also told the ethics adviser.

### Exercises — chapter 10

**EX019 — Write the stop conditions.** *Objective:* protect a live service during an authorised test. *Inputs:* CPN authorises a passive network-traffic capture in its control room for one day. *Steps:* write five stop conditions and say who is called for each. *Expected evidence:* list. *Rubric:* 3 = five specific, observable conditions (process alarm, unexpected device behaviour, discovery of safety-system traffic outside scope, operator request, data of a sensitive type) with named roles; 2 = generic; 1 = fewer than three; 0 = none.

**EX020 — The patch dilemma.** *Objective:* structure an ethical decision. *Inputs:* the ventilator-patch example in this chapter's discussion of professional codes. *Steps:* list stakeholders and harms, two alternatives to "patch all now" or "patch none", and write a 150-word decision record naming who accepts the residual risk. *Expected evidence:* the analysis and record. *Rubric:* 3 = harms on both sides, credible alternatives (staged patching, isolation plus monitoring), clinical and security owners named; 2 = one side only; 1 = opinion without structure; 0 = none.

### Chapter synthesis

Authorisation defines legitimate security work. Write rules of engagement, stop when you stumble on something real and report it privately, and reason through conflicts between duties explicitly, recording who accepted which risk. In critical services, careless testing can harm people.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue studying — chapter 10 of 40

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes and connection

After this chapter you can (1) explain processes, memory protection, file permissions and privilege; (2) describe how an operating system enforces least privilege and where it cannot; (3) compare general-purpose, real-time and embedded operating systems in critical services; and (4) build a hardening checklist and a patch decision for a device that cannot be rebooted at will. It builds on Chapter 2's layers and prepares Chapter 13 (identity) and Chapter 24 (controls).

### 11.1 What the operating system does

The **operating system** (OS) shares one machine between many programs and users. A **process** is a running program with its own memory; the OS uses hardware memory protection so one process cannot read or overwrite another's memory. The **kernel** is the privileged core that manages hardware; user programs ask it for services through **system calls**. Files carry **permissions** — on Unix-like systems, read, write and execute for the owner, a group and others — and the OS checks them on every access. **Privilege** is the ability to bypass such checks: the Unix root account, the Windows Administrator. Saltzer and Schroeder's principles of **least privilege** and **complete mediation** — every access checked, every program given only the rights it needs — remain the foundation ([Saltzer and Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939)).

### 11.2 Kinds of OS in critical services

**General-purpose** systems (Windows, Linux, macOS) run servers, operator workstations and office PCs; they are feature-rich, patched frequently and widely attacked. **Real-time operating systems** (RTOS) guarantee that tasks meet deadlines — a protection relay must act within milliseconds — and run in controllers, relays and medical devices; they are small and less often patched. **Embedded firmware** in sensors and simple devices may have no separation between programs at all. The consequence: the strongest OS protections exist on the machines that are easiest to replace, and the weakest on the machines that last longest.

### 11.3 Hardening

**Hardening** reduces what an attacker can use. A practical checklist: remove or disable unused services and software; change default accounts and passwords; run services as unprivileged accounts; enable logging and send logs off the host; restrict removable media; enable application allowlisting where the workload is stable (operator workstations are good candidates — they run the same few programs for years); keep time synchronised so logs can be correlated. Each item should be checkable — a hardening standard that cannot be verified is a wish.

### 11.4 Patching in operations

On office IT, patching is routine. On an operator workstation or controller, a patch may require vendor validation, a maintenance window and a rollback plan, because a failed update can stop the process. A **risk-based patch decision** asks: is the flaw exploitable on this device as deployed (reachable? requires local access?); is it known to be exploited; what does the device control; what compensating controls exist; when is the next window? The result is one of: patch now (emergency change), patch in the next window, mitigate and monitor until replacement, or accept with a named owner. NIST's OT guide discusses these trade-offs ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

### 11.5 Worked example: CT signalling workstation (synthetic)

**This case is synthetic.** Calder Transit's signalling control workstation runs a general-purpose OS. A monthly update fixes a flaw that lets a local, low-privileged user become administrator. The workstation has no internet access, no email, application allowlisting enabled, and only three named signallers log in. The vendor validates OS updates quarterly; the next validated bundle is in seven weeks. Decision: **patch in the next window**, because exploitation needs a local account on a tightly controlled machine; meanwhile confirm allowlisting is enforced and review the three accounts. Had the flaw been remotely exploitable over a network service the workstation exposes, the answer would have been an emergency change or disabling that service.

### 11.6 Practical activity

On your own computer, list running processes and the account each runs as; find one service you do not use and find out how it could be disabled (do not disable anything you are unsure about). Write a five-item hardening checklist for a CEDC call-handling workstation, each item with how it would be verified.

For the CEDC workstation, write items such as "call handlers log in with individual accounts without administrator rights; check: list local administrators monthly" or "USB storage blocked; check: insert a test drive during the quarterly review".

### 11.7 Common errors and limits

- Running everything as administrator "to avoid permission problems".
- Hardening once and never verifying drift.
- Applying office-IT patch cadence to OT without validation and rollback.
- Assuming a device with no OS user interface has no OS.

The CT signalling workstation shows the alternatives: allowlisting and three named accounts instead of administrator use, a quarterly vendor-validated bundle instead of the office's monthly cadence, and a review that checks allowlisting is still enforced. The fourth error covers CVH's infusion pumps, which run an RTOS that needs vendor updates.

### Exercises — chapter 11

**EX021 — Patch decision.** *Objective:* apply the risk-based questions. *Inputs:* a remotely exploitable flaw in the web interface of a CVH BMS controller; the interface is reachable from the corporate network; the vendor fix needs a 30-minute controller restart; theatre ventilation depends on the BMS. *Steps:* answer the five risk-based patch questions of this chapter and recommend. *Expected evidence:* answers and recommendation with interim controls. *Rubric:* 3 = restrict access to the interface immediately, schedule the restart with estates and theatres in a planned window, monitor; 2 = right outcome, weak interim controls; 1 = "patch immediately" with no consideration of ventilation; 0 = none.

**EX022 — Verifiable hardening.** *Objective:* make controls checkable. *Inputs:* three vague items: "secure the accounts", "turn on logging", "lock down USB". *Steps:* rewrite each as a specific, verifiable statement with the check. *Expected evidence:* three rewritten items. *Rubric:* 3 = specific, observable, with a check method; 2 = specific but no check; 1 = still vague; 0 = none.

### Chapter synthesis

The OS enforces separation, permissions and privilege; least privilege and complete mediation are its guiding ideas. In critical services the most durable devices often have the weakest protections, so hardening must be verifiable and patching must be risk-based, scheduled and reversible.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue studying — chapter 11 of 40

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes and connection

After this chapter you can (1) apply the addition, complement and multiplication rules and say when events are independent; (2) use Bayes' theorem to interpret an alert, including the effect of the base rate; (3) compute the chance of at least one failure over repeated trials and the chance that enough of $n$ redundant units are available; and (4) summarise skewed data with medians and percentiles. It builds on Chapter 1 and prepares Chapters 15, 27 and 29.

### 12.1 Rules you will use constantly

Probabilities are numbers between 0 and 1. The **complement** rule: $P(\text{not } A) = 1 - P(A)$. For **independent** events, $P(A \text{ and } B) = P(A)P(B)$. For any events, $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$ — adding without subtracting the overlap double-counts. "At least one" problems are easiest by complement: if a backup fails silently on a given day with probability $p$, independently each day, the chance of at least one silent failure in $n$ days is $1 - (1-p)^n$. Independence is an assumption, often false: two generators fed from the same fuel tank fail together. Such **common-cause** failures are why redundancy is weaker than the multiplication rule suggests.

### 12.2 Conditional probability and Bayes

$P(A \mid B)$ is the probability of $A$ given that $B$ occurred. Bayes' theorem relates the two directions:
$$P(\text{malicious} \mid \text{alert}) = \frac{P(\text{alert} \mid \text{malicious})\,P(\text{malicious})}{P(\text{alert})}.$$
A detector with a 95% **true-positive rate** and 1% **false-positive rate** sounds excellent. If only 1 event in 1,000 is malicious, most alerts are still false: the **base rate** dominates. This is the most important statistical idea in security operations, and it explains why analysts drown in alerts.

### 12.3 Binomial reasoning for redundancy

If $n$ identical units are each available with probability $1-p$, independently, the number available follows a **binomial** distribution: $P(k \text{ available}) = \binom{n}{k}(1-p)^k p^{n-k}$. A pumping station that needs at least 10 of its 12 pumps can compute how often it meets demand.

For the 12-pump station in Lab 6, with each pump unavailable 10 % of the time, the sum over 10, 11 and 12 available pumps gives 0.889. A shared maintenance crew or a single power feed breaks the independence assumption, so the real figure is lower. Adding a thirteenth pump raises the result to about 0.966, which is the kind of comparison a capital request needs.

### 12.4 Describing data

Times to detect and recover from incidents are **skewed**: most are short, a few are very long. The **mean** is pulled up by the long tail; the **median** (middle value) is not; **percentiles** (the 90th percentile, p90) describe the tail. Report median and p90 together, with the sample size (Chapter 29, Lab 12).

Lab 12 shows the effect: its mean time to detect is 27.2 hours while the median is 4.0.

For a board, the sentence "half of incidents were detected within 4 hours; one in ten took more than about 56" carries more information than any single average.

### 12.5 Worked example and Lab 6 (synthetic)

**This case is synthetic.** Calder Mutual's monitoring service sees 20,000 events a day; analysts estimate 1 in 1,000 is malicious; the detector's rates are those above. CW's nightly telemetry backup fails silently with probability 0.002 per day. A pumping station has 12 pumps each unavailable 10% of the time.

```python
# Lab 6 - base rates, alarm volume and repeated trials (synthetic, offline)
from math import comb
prior, tpr, fpr = 0.001, 0.95, 0.01
ppv = tpr * prior / (tpr * prior + fpr * (1 - prior))
print(f"P(malicious | alert) = {ppv:.3f}")
events_per_day = 20_000
print(f"expected false alerts/day = {events_per_day * (1 - prior) * fpr:.0f}; true = {events_per_day * prior * tpr:.0f}")
p_day = 0.002   # chance per day that a given backup fails silently
for days in (30, 365):
    print(f"P(at least one silent backup failure in {days} days) = {1 - (1 - p_day) ** days:.3f}")
n, p = 12, 0.1  # 12 independent pumps, each unavailable 10% of the time
need = 10
print(f"P(at least {need} of {n} available) = {sum(comb(n, k) * (1-p)**k * p**(n-k) for k in range(need, n+1)):.3f}")
```

Expected output:

```text
P(malicious | alert) = 0.087
expected false alerts/day = 200; true = 19
P(at least one silent backup failure in 30 days) = 0.058
P(at least one silent backup failure in 365 days) = 0.518
P(at least 10 of 12 available) = 0.889
```

Fewer than 1 alert in 11 is real; analysts face about 200 false alerts a day. A "rare" daily backup failure is more likely than not over a year — which is why restore drills, not backup logs, are the evidence that matters. And a station needing 10 of 12 pumps falls short about 11% of the time under these assumptions: if pump outages share a cause (one maintenance crew, one power feed), it will be worse.

### 12.6 Common errors and limits

- Ignoring the base rate (the "95% accurate" fallacy).
- Multiplying probabilities of events that share a cause.
- Reporting a mean for skewed times without the median and tail.
- Treating estimated inputs as exact; the outputs inherit their uncertainty.

Lab 6 gives each a number: 95 % detection still yields a 0.087 chance that an alert is real; two generators sharing fuel fail together far more often than 0.05 squared (EX024); the 27.2-hour mean detection time in Lab 12 describes no incident; and the 0.002 daily backup failure rate is itself an estimate, so the 0.518 yearly figure inherits its uncertainty.

### Exercises — chapter 12

**EX023 — Change the base rate.** *Objective:* see how prior and false-positive rate drive alert value. *Inputs:* Lab 6. *Steps:* compute $P(\text{malicious}\mid\text{alert})$ for prior 0.01 and, separately, for prior 0.001 with FPR 0.001. Explain which change helps more and what it means operationally. *Expected evidence:* two values and an explanation. *Rubric:* 3 = ≈ 0.490 and ≈ 0.487 with an explanation that lowering FPR (tuning, enrichment) is the lever analysts control; 2 = values only; 1 = one value; 0 = none.

**EX024 — Common cause.** *Objective:* quantify the effect of shared causes. *Inputs:* two backup generators each failing to start with probability 0.05; with probability 0.02 a shared cause (contaminated common fuel) fails both. *Steps:* compute the probability both fail assuming independence, then with the common cause (approximate as $0.02 + 0.05^2$), and comment. *Expected evidence:* two numbers and a comment. *Rubric:* 3 = 0.0025 versus ≈ 0.0225, roughly nine times worse, and a remedy (separate fuel, fuel testing); 2 = numbers only; 1 = one number; 0 = none.

### Chapter synthesis

Probability rules are simple; their assumptions are not. Base rates decide whether an alert is worth reading, "rare per day" becomes "likely per year", redundancy is weakened by common causes and skewed data needs medians and percentiles. State independence assumptions and test what happens when they fail.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue studying — chapter 12 of 40

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes and connection

After this chapter you can (1) distinguish identification, authentication and authorisation; (2) compare authentication factors and explain why phishing-resistant methods matter for remote access to critical systems; (3) design role-based access with separation of duties; and (4) run an access review that finds orphaned, dormant, shared and toxic-combination accounts. It builds on Chapter 6 (sets) and Chapter 11 (privilege) and prepares Chapter 16 (architecture) and Chapter 24 (controls).

### 13.1 Three questions

**Identification** answers "who do you claim to be?" (a username). **Authentication** answers "prove it" — with something you know (a password), have (a token or phone) or are (a fingerprint). **Authorisation** answers "what may you do?" — the permissions attached to the authenticated identity. Errors at each stage differ: weak authentication lets the wrong person in; excessive authorisation lets the right person (or whoever stole their session) do too much. NIST's digital-identity guidelines set requirements for authenticators and recommend phishing-resistant options for higher assurance ([SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final)).

### 13.2 Factors and remote access

Passwords are guessed, reused and phished. One-time codes sent by text or typed from an app add a second factor but can be relayed by a convincing fake login page. **Phishing-resistant** authenticators bind the login cryptographically to the genuine site, so a fake site receives nothing usable. For remote access into OT and other critical systems — the path in the CPN advisory of Chapter 5 — strong authentication is necessary but not sufficient: the session should land on a controlled jump host, be time-limited, approved per session for vendors, and recorded.

### 13.3 Roles and separation of duties

In **role-based access control** (RBAC), permissions attach to roles ("scada-operator", "payments-approve") and people receive roles. Roles make reviews tractable: one checks fifty roles, not fifty thousand individual permissions. **Separation of duties** forbids certain combinations: the person who creates a payment must not approve it; the engineer who changes control logic should not also control the firewall that logs the change. Expressed with sets (Chapter 6), a **toxic combination** $T$ is violated when $T \subseteq \text{roles}(u)$.

In Lab 7, the two TOXIC sets encode exactly these rules.

### 13.4 The account life cycle and reviews

Accounts are created when people join (**joiner**), changed when they move (**mover**) and removed when they leave (**leaver**). Failures accumulate at every step: movers keep old roles ("privilege creep"), leavers' accounts linger, vendors' accounts are created for a project and never removed, and shared operator accounts make actions untraceable. An **access review** compares accounts with an authoritative source (the HR system, the vendor contract register) and with usage.

Lab 7 shows each failure: *ben* left but kept his account, *vendorx* has no HR owner and has not logged in for 304 days, and *ops1* is shared. Usage data matters as much as HR status: *dev* is active in HR but dormant for 214 days in a privileged role.

### 13.5 Worked example and Lab 7 (synthetic)

**This case is synthetic.** A joint review of accounts across CPN's control system and Calder Mutual's payment system (combined here only for teaching) uses HR status, last login and two toxic combinations.

```python
# Lab 7 - access review: orphans, dormant accounts and toxic combinations (synthetic, offline)
from datetime import date
TODAY = date(2026, 10, 1)
HR = {"ana": "active", "ben": "left", "chloe": "active", "dev": "active"}
ACCOUNTS = [  # user, roles, last login, shared?
    ("ana",   {"scada-operator"},                       date(2026, 9, 30), False),
    ("ben",   {"scada-engineer"},                       date(2026, 5, 2),  False),
    ("chloe", {"payments-create", "payments-approve"},  date(2026, 9, 29), False),
    ("dev",   {"scada-engineer", "firewall-admin"},     date(2026, 3, 1),  False),
    ("ops1",  {"scada-operator"},                       date(2026, 9, 30), True),
    ("vendorx", {"remote-support"},                     date(2025, 12, 1), False),
]
TOXIC = [{"payments-create", "payments-approve"}, {"scada-engineer", "firewall-admin"}]
for user, roles, last, shared in ACCOUNTS:
    issues = []
    if user not in HR: issues.append("no HR owner")
    elif HR[user] != "active": issues.append("owner has left")
    if (TODAY - last).days > 90: issues.append(f"dormant {(TODAY - last).days} d")
    if shared: issues.append("shared account")
    issues += ["toxic: " + "+".join(sorted(t)) for t in TOXIC if t <= roles]
    print(f"{user:8} {', '.join(issues) if issues else 'ok'}")
```

Expected output:

```text
ana      ok
ben      owner has left, dormant 152 d
chloe    toxic: payments-approve+payments-create
dev      dormant 214 d, toxic: firewall-admin+scada-engineer
ops1     no HR owner, shared account
vendorx  no HR owner, dormant 304 d
```

Actions: disable *ben* now (leaver); remove one of *chloe*'s payment roles; remove *dev*'s dormant privileged roles and ask whether he needs either; *ops1* is a shared control-room login — common in 24/7 operations where a fast handover matters — so replace it with individual logins and quick user switching, or at least record who is on shift; *vendorx* should be disabled and re-enabled per support session under a named sponsor. Note what the script cannot see: whether *ana*'s role still matches her job.

### 13.6 Common errors and limits

- Equating "authenticated" with "authorised".
- Reviews that confirm accounts exist rather than whether they are needed.
- Removing shared accounts in a control room without a workable alternative, so staff share passwords instead.
- Forgetting service and vendor accounts, which have no HR record.

In Lab 7 the script confirms that *ana*'s account is "ok" only in the sense that she is active and not dormant; whether she still needs `scada-operator` needs her manager. Removing *ops1* outright would lead the control room to share one person's password, which is worse. And *ops1* and *vendorx* both show "no HR owner", which is the signal that service and vendor accounts need a different authoritative source, such as the contract register.

### Exercises — chapter 13

**EX025 — Design the roles.** *Objective:* apply least privilege and separation of duties. *Inputs:* CEDC needs call handlers, dispatchers, supervisors, a CAD administrator and a vendor support engineer. *Steps:* define five roles with key permissions and two toxic combinations. *Expected evidence:* role table and combinations. *Rubric:* 3 = sensible least-privilege roles, toxic pairs justified (e.g. CAD admin + audit-log admin; vendor support + permanent access); 2 = roles without combinations; 1 = vague; 0 = none.

**EX026 — Extend the review.** *Objective:* add a rule. *Inputs:* Lab 7. *Steps:* add a check that flags any account with a privileged role (`scada-engineer`, `firewall-admin`, `payments-approve`) that has not been re-approved in 180 days, given a new field `approved` (a date). Choose dates so at least one account is flagged and show the output. *Expected evidence:* code and output. *Rubric:* 3 = correct logic, test data chosen to show both flagged and unflagged cases; 2 = works, weak test; 1 = logic error; 0 = none.

### Chapter synthesis

Identity answers three different questions. Use strong, phishing-resistant authentication for critical remote access, grant permissions through roles, forbid toxic combinations and review accounts against authoritative sources and actual use. Shared and vendor accounts need workable alternatives, not just prohibitions.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue studying — chapter 13 of 40

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes and connection

After this chapter you can (1) explain the difference between security and privacy; (2) apply data-protection principles such as lawfulness, purpose limitation, minimisation and storage limitation; (3) identify personal data in critical-service systems, including data that becomes personal when combined; and (4) recommend privacy-protective designs for monitoring and incident data. It builds on Chapter 9 (data) and Chapter 10 (ethics) and prepares Chapter 29 (operations) and the capstone's ethics requirements.

### 14.1 Security is not privacy

Security protects systems and information from unauthorised access, change and loss. **Privacy** concerns whether the processing of information about people — even authorised processing — is appropriate, proportionate and fair. A perfectly secure hospital database can still violate privacy if it is used for a purpose patients were never told about. The [NIST Privacy Framework](https://www.nist.gov/privacy-framework) treats privacy risk as arising from data processing itself, overlapping with but distinct from cybersecurity risk.

CT's clone detection is the example: secure storage of two years of taps would still be a privacy problem.

### 14.2 Principles

The EU General Data Protection Regulation sets out principles that are widely mirrored elsewhere: lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; and accountability ([Regulation (EU) 2016/679, Article 5](https://eur-lex.europa.eu/eli/reg/2016/679/oj)). Health data is a **special category** requiring additional conditions. You do not need to become a lawyer, but you must recognise when a design question is also a data-protection question and involve the organisation's data-protection officer — and you must never present this book's summary as legal advice for a specific case.

### 14.3 Personal data in unexpected places

Critical services hold obvious personal data (patient records, bank accounts, emergency calls) and less obvious data. Smart-meter readings at short intervals can reveal when a household is home. Ticketing data from a transit card traces a person's movements. Security logs record who logged in, from where and when — personal data about staff. **Combination** matters: neither a postcode nor a date of birth alone usually identifies someone, but together with sex they often do. Pseudonymisation (replacing names with codes) reduces risk but is not anonymisation if the key exists or re-identification is possible.

### 14.4 Privacy in security operations

Security monitoring collects data about people by design. Privacy-protective practice: collect what the detection purpose needs, not everything available; restrict access to raw logs; set retention periods; pseudonymise where analysis does not need names; document the purpose and lawful basis; and, in an incident, share indicators (addresses, file hashes) rather than personal data where possible. During a breach involving personal data, notification duties may apply on short timescales, so incident plans include the data-protection officer from the start.

CT's revised design applies four of these: 30-day detail, keyed pseudonyms, two named analysts and a stated purpose.

### 14.5 Worked example: CT ticketing analytics (synthetic)

**This case is synthetic.** Calder Transit's security team wants to detect cloned transit cards by looking for the same card used at two stations too far apart in too short a time. The proposed design copies every card tap (card ID, station, time) for two years into the security analytics platform. A privacy review asks: is two years needed? (Clone detection needs minutes to days; retain full detail for 30 days, then aggregate.) Is the card ID needed in clear? (A keyed pseudonym suffices for matching; only confirmed cases are re-identified, by the fraud team.) Who can query it? (Two named analysts, logged.) Is passenger travel history being created as a side effect? (Yes — which is why the design limits retention and access.) The revised design meets the detection purpose with a fraction of the privacy risk.

### 14.6 Practical activity

Choose one service you use (a transit card, a smart meter, a hospital app). From its public privacy notice, list the personal data collected, the stated purposes and retention. Identify one data item whose purpose is unclear and draft a question you could send the provider.

Notice whether the notice states retention in days or years, or only "as long as necessary"; the latter is a question worth asking. Note whether security monitoring is listed as a purpose at all. Draft your question politely and specifically, for example asking how long journey-level data is kept before aggregation and who can access it.

### 14.7 Common errors and limits

- "We are secure, therefore we are compliant."
- Collecting everything "in case it is useful".
- Calling pseudonymised data anonymous.
- Forgetting staff data in logs.
- Giving legal conclusions without the organisation's legal and data-protection advisers.

Each appears in this chapter's examples. CT's original two-year tap copy was secure and still disproportionate. "In case it is useful" is how the full card ID ended up in the analytics platform. Keyed pseudonyms are reversible by the fraud team, so they are not anonymous. CVH's access-monitoring proposal in EX027 logs staff names, which is staff personal data. And none of these designs should be called lawful without the data-protection officer.

### Exercises — chapter 14

**EX027 — Minimise a log.** *Objective:* apply minimisation to security monitoring. *Inputs:* a CVH proposal to log every staff access to patient records with full patient name, diagnosis, staff name, workstation, time, retained indefinitely, to detect inappropriate access. *Steps:* propose a minimised design meeting the same purpose. *Expected evidence:* field list, retention, access and a sentence on purpose. *Rubric:* 3 = record identifier instead of diagnosis, defined retention, restricted access, purpose stated, staff informed; 2 = partial; 1 = "log less" without design; 0 = none.

**EX028 — Combination risk.** *Objective:* recognise re-identification. *Inputs:* CW publishes "anonymised" hourly consumption per meter with postcode and property type. *Steps:* explain two re-identification risks and two mitigations. *Expected evidence:* explanation. *Rubric:* 3 = small postcodes with unique property types identify households, occupancy inferable from hourly patterns; mitigations: aggregation thresholds, coarser time or location, access agreements; 2 = one each; 1 = vague; 0 = none.

### Chapter synthesis

Privacy asks whether processing about people is appropriate, not only whether it is secure. Apply purpose limitation, minimisation and storage limitation — especially to security monitoring itself — recognise that combinations re-identify, and involve data-protection specialists rather than offering legal conclusions.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue studying — chapter 14 of 40

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes and connection

After this chapter you can (1) distinguish a measurement, an indicator and a claim; (2) judge evidence by its source, method, recency and independence; (3) design a security metric that is valid, reliable and hard to game; and (4) use sensitivity analysis to decide whether uncertain evidence is good enough for a decision. It builds on Chapters 1, 4 and 12 and prepares Chapter 18 (research methods), Chapter 27 (verification) and Chapter 37 (evidence review).

### 15.1 What counts as evidence

A **claim** is a statement that something is true ("our backups can restore the dispatch system within four hours"). **Evidence** is what supports or undermines it. Evidence varies in strength. A **demonstration** (a timed restore drill on the production configuration, last month) is stronger than a **document** (a backup policy) which is stronger than an **assertion** ("the vendor says it works"). Ask four questions of any evidence: *Source* — who produced it, and do they have an interest in the answer? *Method* — how was it produced, and could someone repeat it? *Recency* — does it still describe the system as it is now? *Independence* — was it checked by someone other than the person who made the claim?

### 15.2 Measurement and metrics

A **measurement** is a value obtained by a defined procedure (restore time in minutes, measured from start to the first successful dispatch transaction). An **indicator** or **metric** is a measurement used to track something we care about. Good metrics are **valid** (they measure what matters — percentage of critical assets with a tested restore, not number of backup jobs), **reliable** (two people measuring get the same result), **timely** and **hard to game**. Goodhart's warning applies: once a measure becomes a target, people optimise the measure. A patch metric of "percentage of systems patched within 30 days" encourages excluding hard systems from the denominator; report the denominator and the exclusions.

### 15.3 Uncertainty and sensitivity

Most security evidence is uncertain: small samples (Chapter 12), estimates (Chapter 1), proxies. **Sensitivity analysis** asks how much the decision changes when an uncertain input changes. If a recommendation holds across the plausible range, the evidence is adequate for that decision even if imprecise. If it flips, either gather better evidence on that input or make the decision robust (choose the option that is acceptable across the range). This is a practical antidote to both false precision and paralysis.

Lab 1 is the model: B stays ahead when any one probability is halved or doubled.

### 15.4 Worked example: is CEDC's dispatch restorable? (synthetic)

**This case is synthetic.** CEDC's board asks: "Can we restore computer-aided dispatch within four hours after ransomware?" Available evidence:

| Evidence | Type | Source | Recency | Independent? |
|---|---|---|---|---|
| Backup policy says nightly backups, 4-h restore objective | Document | IT team | 2024 | No |
| Backup software reports 362/365 successful jobs | Measurement (of backup, not restore) | Tool | Last year | No |
| Restore drill: database restored in 2 h 40 min, application not tested | Partial demonstration | IT team | 8 months ago | No |
| Vendor statement: "full restore typically under 3 hours" | Assertion | Vendor | Undated | No |

Assessment: no evidence demonstrates the *claim* — a restore of the whole dispatch service, including application servers, integrations and credentials, under ransomware conditions (where the backup server itself may be encrypted). The honest answer to the board is "unknown, with partial evidence that the database alone restores within four hours". Recommendation: an end-to-end restore drill into an isolated environment, observed by internal audit, measuring time to first successful test dispatch; and confirmation that at least one backup copy is offline or immutable.

### 15.5 Practical activity

Take one claim about a service you use ("my phone backs up my photos"). List the evidence you have, classify each item by type, source, recency and independence, and design one test that would demonstrate the claim. Do not run anything on systems you do not own.

For a phone backup, the strongest test is a restore of one photo to another device you own, timed, with the date recorded. A backup app's "last backup: today" is a measurement of the backup, not of the restore.

### 15.6 Common errors and limits

- Treating backup success as restore evidence.
- Metrics that count activity instead of outcomes.
- Denominators that silently exclude the hardest cases.
- Ignoring the interest of the evidence's source.
- Demanding precision a decision does not need, or accepting confidence it has not earned.

CEDC's evidence table shows the first: 362 of 365 successful jobs say nothing about restoring the application. The second appears when a team reports number of backup jobs instead of tested restores. The third is the patch metric with hard systems left out. The fourth is the vendor's undated "under 3 hours". The fifth cuts both ways: the board does not need minutes, but it cannot accept "probably fine".

### Exercises — chapter 15

**EX029 — Grade the evidence.** *Objective:* apply the four questions. *Inputs:* claim "Calder Mutual's card service fails over to its second data centre within 15 minutes"; evidence: architecture diagram (2025), last year's failover test report by the operations team (14 min), auditor's note that the test was announced a week ahead. *Steps:* grade each item and state what the evidence does and does not show. *Expected evidence:* table and two sentences. *Rubric:* 3 = recognises the test as a real but announced, non-independent demonstration and asks for an unannounced or independently observed test under realistic load; 2 = partial; 1 = accepts the claim; 0 = none.

**EX030 — Fix a metric.** *Objective:* design a valid, hard-to-game metric. *Inputs:* "number of phishing-awareness courses completed". *Steps:* propose a better metric for the risk of credential phishing, define its measurement and name one way it could be gamed. *Expected evidence:* definition and gaming risk. *Rubric:* 3 = outcome-oriented metric (e.g. share of privileged accounts with phishing-resistant authentication, or report rate in authorised simulations) with defined procedure and honest gaming risk; 2 = better but loosely defined; 1 = activity metric; 0 = none.

### Chapter synthesis

Evidence has a source, a method, a date and a degree of independence. Measure outcomes rather than activity, report denominators, and use sensitivity analysis to decide whether uncertain evidence is good enough. "Unknown, with partial evidence" is often the most honest and useful answer.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue studying — chapter 15 of 40

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes and connection

After this chapter you can (1) apply classic design principles — least privilege, fail-safe defaults, economy of mechanism, complete mediation, separation of privilege; (2) describe a layered reference architecture for a critical-service operator from enterprise to field; (3) explain defence in depth and zero trust and their limits in operational technology; and (4) design secure remote access for vendors. It builds on Chapters 7, 11 and 13 and prepares Chapter 21 (system models) and Chapter 24 (controls).

### 16.1 Principles that last

Saltzer and Schroeder's 1975 principles still frame security architecture ([Saltzer and Schroeder](https://doi.org/10.1109/PROC.1975.9939)): **economy of mechanism** (keep it simple enough to verify); **fail-safe defaults** (deny unless allowed); **complete mediation** (check every access); **open design** (security should not depend on secrecy of the design); **separation of privilege** (require more than one condition — two people, two keys); **least privilege**; **least common mechanism** (minimise shared components); and **psychological acceptability** (if it is too hard to use, people bypass it). Each is a lens for reviewing a design: "what here is not mediated? what is shared? what will operators bypass at 03:00?"

### 16.2 A layered reference architecture

Critical-service operators commonly separate: the **enterprise** zone (email, office, business systems); a **DMZ** for data exchange (historian replicas, patch servers, remote-access jump hosts); **operations/control** (SCADA servers, HMIs, engineering workstations); **field** (controllers, RTUs, protection relays); and **safety** systems that act independently to prevent harm. Traffic between layers passes through conduits with explicit rules (Chapter 7). NIST's OT guide and the ISA/IEC 62443 series describe such architectures ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). The point is not the drawing but the **property** it should guarantee: no direct path from the internet or email to anything that controls a physical process.

### 16.3 Defence in depth and zero trust

**Defence in depth** layers independent controls so one failure is not catastrophic: segmentation, hardening, authentication, monitoring, backups, manual fallback. Its weakness is **common mode**: layers that share an administrator account or a management server fall together. **Zero trust** removes implicit trust based on network location; every request is authenticated and authorised per resource ([NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)). In enterprise IT it is a strong direction. In OT, many devices cannot authenticate individual requests, so zero-trust ideas apply mostly at the boundaries — users, engineering workstations, remote access — while segmentation protects the devices that cannot help themselves.

### 16.4 Remote access

Vendors and engineers need remote access; uncontrolled remote access is one of the most common paths into OT. A defensible pattern: access terminates on a **jump host** in the DMZ, never directly in the control zone; **phishing-resistant multi-factor** authentication; **per-session approval** by the operator on shift for vendors; **time-limited** accounts; **session recording**; and an **off switch** the control room can use. Each element answers a specific failure.

CPN's redesign uses every element; the remaining risk is the approved session itself.

### 16.5 Worked example: CPN's remote access (synthetic)

**This case is synthetic.** CPN's current design: the internet-facing VPN-G gateway (Chapter 5) places users directly on the control network; three vendors have permanent accounts; passwords only. Redesign: VPN-G upgraded and moved to terminate on a DMZ jump host; vendor accounts disabled by default and enabled per ticket by the control-room supervisor for up to four hours; phishing-resistant MFA for staff; sessions recorded on a server the vendors cannot reach; a physical switch in the control room that disables the remote-access conduit. Residual risk, stated: an approved vendor session is still trusted during its window; recording supports detection and accountability but does not prevent misuse in real time.

### 16.6 Practical activity

Draw the Calder Water architecture from Chapter 7 with its zones and the three allowed conduits. Annotate each conduit with the principle it serves and the control enforcing it. Mark the one component whose compromise would hurt most and explain why.

In CW's architecture each conduit serves a principle: the corporate-to-DMZ HTTPS view applies least privilege, the DMZ collector's OPC UA read applies complete mediation at the conduit, and the SCADA-to-field Modbus polling relies on fail-safe defaults by denying everything else. The SCADA server is a strong candidate for the component whose compromise hurts most, because it can both see and command every field controller.

### 16.7 Common errors and limits

- Architecture diagrams that show intended, not actual, connections.
- "Dual-homed" machines that bridge zones and bypass the conduit.
- Layers that share administrators, credentials or management tools.
- Applying zero trust slogans to devices that cannot authenticate.

In CW's case, the Lab 4 RDP connection from corporate directly into control is the first error: a path the diagram does not show. A dual-homed engineering laptop is the usual cause. CVH's management server that administers firewalls, endpoint protection and backups with one account (EX032) is the third. The fourth applies to RTUs and PLCs.

### Exercises — chapter 16

**EX031 — Principle review.** *Objective:* use principles as review lenses. *Inputs:* CPN's original remote-access design in this chapter's worked example. *Steps:* name four Saltzer–Schroeder principles it violates and how. *Expected evidence:* four principle–violation pairs. *Rubric:* 3 = four correct (least privilege, fail-safe defaults, complete mediation, separation of privilege, or least common mechanism) with specific explanation; 2 = three; 1 = one or two; 0 = none.

**EX032 — Common mode.** *Objective:* find hidden shared dependencies. *Inputs:* CVH has segmentation firewalls, endpoint protection and backups — all administered from one management server using one domain-administrator account. *Steps:* explain the common-mode risk and propose two changes. *Expected evidence:* explanation and changes. *Rubric:* 3 = compromise of the account/server disables all three layers; changes such as separate admin tiers/credentials and offline backups; 2 = one change; 1 = vague; 0 = none.

### Chapter synthesis

Architecture turns principles into enforced properties: no direct path from the internet to anything that moves the physical world. Layer independent controls, watch for common modes, apply zero trust where devices can participate and segment where they cannot, and treat remote access as the most important conduit to design well.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue studying — chapter 16 of 40

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes and connection

After this chapter you can (1) explain what hashing, symmetric encryption, message authentication codes, public-key encryption and digital signatures each guarantee and do not guarantee; (2) explain why integrity and authenticity, more than secrecy, are the cryptographic needs of control systems; (3) use HMAC with a sequence number to reject altered and replayed commands; and (4) make a log tamper-evident with a hash chain and an external anchor. It builds on Chapters 5 and 8 and prepares Chapter 24 (controls) and Chapter 29 (operations).

### 17.1 The tools and their guarantees

A **cryptographic hash function** such as SHA-256 maps any input to a fixed-size digest; it is infeasible to find two inputs with the same digest or to recover the input ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)). A hash alone proves nothing about *who* produced data: anyone can recompute it. **Symmetric encryption** (e.g. AES, [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)) provides confidentiality with a shared key. A **message authentication code** (MAC) such as HMAC ([RFC 2104](https://www.rfc-editor.org/rfc/rfc2104); [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final)) lets a holder of the shared key verify that a message was produced by another key holder and not altered. **Public-key** cryptography ([Diffie and Hellman, 1976](https://doi.org/10.1109/TIT.1976.1055638); [Rivest, Shamir and Adleman, 1978](https://doi.org/10.1145/359340.359342)) allows **digital signatures**: anyone with the public key can verify, only the private-key holder can sign — the basis for signed firmware and certificates. Protocols such as TLS 1.3 combine these to give authenticated, encrypted channels ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)).

### 17.2 What control systems need

For a breaker command, secrecy is rarely the point; **authenticity** (it came from the control centre), **integrity** (it was not altered) and **freshness** (it is not an old command replayed) are. A MAC provides the first two. Freshness needs a **sequence number** or timestamp inside the authenticated message, and a receiver that rejects anything not newer than the last accepted value. Without freshness, an attacker who recorded yesterday's valid "OPEN" can replay it today.

Lab 8 demonstrates both: the altered breaker name fails the MAC, and sequence 41 is rejected once it has been accepted.

### 17.3 Keys are the hard part

Cryptography moves the problem from protecting data to protecting keys. Who generates keys, where they are stored, how they are rotated and revoked, and what happens when a field device's key leaks — these determine real security. Keys must never be hard-coded in published code (the key in Lab 8 is deliberately public), never shared across all devices, and should live in hardware where possible. Planning ahead also matters: NIST finalised its first post-quantum cryptography standards in 2024 ([NIST, 2024](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)), and infrastructure with 20-year lifetimes needs the ability to change algorithms ("crypto-agility").

### 17.4 Worked example and Lab 8 (synthetic)

**This case is synthetic.** CPN authenticates breaker commands with HMAC-SHA-256 over a message containing a sequence number, and keeps a hash-chained log of operator actions whose latest head is copied hourly to a separate server (the **anchor**).

```python
# Lab 8 - HMAC message authentication and a hash-chained log (synthetic; DEMO KEY ONLY, offline)
import hmac, hashlib
KEY = b"demo-key-published-in-a-textbook-never-use"
def tag(msg): return hmac.new(KEY, msg, hashlib.sha256).hexdigest()[:16]
cmd = b"seq=41;breaker=F7;op=OPEN"
t = tag(cmd)
print("tag:", t)
print("valid original:", hmac.compare_digest(t, tag(cmd)))
print("valid altered :", hmac.compare_digest(t, tag(b"seq=41;breaker=F2;op=OPEN")))
last_seq = 41
print("replay of seq 41 accepted?", 41 > last_seq)
# hash chain: each entry commits to the previous head
def chain(entries):
    head, heads = "0" * 64, []
    for e in entries:
        head = hashlib.sha256((head + e).encode()).hexdigest(); heads.append(head)
    return heads
log = ["08:00 login ana", "08:05 setpoint PS2 4.1m", "08:09 logout ana"]
good = chain(log)
log[1] = "08:05 setpoint PS2 2.0m"
bad = chain(log)
print("anchored head:", good[-1][:12], "| recomputed after edit:", bad[-1][:12])
print("first differing entry:", next(i for i, (a, b) in enumerate(zip(good, bad)) if a != b))
```

Expected output:

```text
tag: 347e6a26d1844d03
valid original: True
valid altered : False
replay of seq 41 accepted? False
anchored head: c5754d1d1639 | recomputed after edit: 65e0b2a20fac
first differing entry: 1
```

The altered breaker name fails verification; the replayed sequence number is rejected; the edited log no longer matches the anchored head, and comparison shows the first altered entry. Truncating the tag to 64 bits keeps the printout short; real systems use the full tag or a standard truncation. The hash chain detects editing **only** if the anchor is out of the editor's reach — someone who controls both the log and the anchor can rebuild the whole chain.

### 17.5 Common errors and limits

- Using a plain hash where a MAC or signature is needed.
- Authenticating messages without freshness.
- Comparing tags with `==` instead of a constant-time comparison.
- One shared key for every device.
- Believing encryption makes a compromised endpoint trustworthy.

In Lab 8 a plain SHA-256 of the command would let anyone who changes it compute a new digest. The MAC without `seq=` would accept yesterday's OPEN. The lab uses `hmac.compare_digest` rather than `==`. One key on every RTU means one leaked key compromises the network. And encryption would not help if the control-centre HMI itself sends forged commands.

### Exercises — chapter 17

**EX033 — Choose the primitive.** *Objective:* match needs to tools. *Inputs:* (a) firmware updates for CVH infusion pumps from the manufacturer; (b) commands from CPN's control centre to its own RTUs; (c) patient records on a lost laptop; (d) detecting edits to an audit log. *Steps:* choose a primitive for each and justify. *Expected evidence:* four choices. *Rubric:* 3 = signatures, MAC with freshness (or an authenticated channel), symmetric encryption with key protection, hash chain with external anchor; 2 = one wrong; 1 = two wrong; 0 = none.

**EX034 — Break the anchor.** *Objective:* reason about trust in the anchor. *Inputs:* Lab 8. *Steps:* explain how an administrator with write access to both the log server and the anchor could hide an edit, and propose two design changes that prevent it. *Expected evidence:* attack description and changes. *Rubric:* 3 = recompute chain and overwrite anchor; changes: anchor held by a different team/system with append-only storage, periodic external publication or signed timestamps; 2 = one change; 1 = description only; 0 = none.

### Chapter synthesis

Each primitive guarantees something specific: hashes detect change only against a trusted reference, MACs and signatures give authenticity, sequence numbers give freshness and encryption gives secrecy. In control systems authenticity, integrity and freshness matter most, and real security depends on key management and on keeping anchors out of an attacker's reach.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue studying — chapter 17 of 40

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes and connection

After this chapter you can (1) turn a topic into a researchable question; (2) choose between descriptive, comparative, experimental and case-study designs; (3) find, screen and summarise literature systematically and record how; and (4) identify threats to validity in a security study. It builds on Chapters 4, 12 and 15 and prepares Chapter 23 (risk methods), Chapter 33 (research methods II) and the capstone proposal (Chapter 35).

### 18.1 From topic to question

"Ransomware in hospitals" is a topic. A **research question** is specific enough that evidence could answer it and someone could disagree: "In publicly reported ransomware incidents affecting hospitals in 2017–2024, how often did reports describe a fallback to paper processes, and what limits of that fallback did they mention?" A good question names the population (which hospitals, which incidents), the variables (fallback described, limits mentioned), the time frame and the kind of answer (a proportion and themes). At bachelor's level, questions that compare — options, sectors, methods — fit the course's outcome better than questions that claim to discover something new.

### 18.2 Designs

**Descriptive** studies say what is (an inventory survey; a count of advisories by sector). **Comparative** studies contrast groups or options using the same criteria. **Experimental** studies change one thing deliberately and measure the effect, ideally against a control (the detector threshold experiment of Chapter 27). **Case studies** examine one or a few cases in depth, using several sources; they explain how and why, but generalise cautiously. Choose the design that the question needs, not the one that seems most scientific.

For the CEDC backup question, comparative is the fitting design: three strategies scored on the same criteria. An experiment would compare drills under controlled conditions, and a case study would examine one past restore in depth. Each answers a different question, so choose the design after writing the question.

### 18.3 Literature, systematically

Searching for sources is itself a method and should be recorded: databases and sites searched, search terms, date, inclusion and exclusion criteria, numbers found and kept. Distinguish **primary** sources (an agency advisory, a regulator's report, a peer-reviewed study) from **secondary** (a news article or blog summarising them). Prefer primary, cite what you read (Chapter 4), and record why you excluded what you excluded so that someone else could repeat the screening. A simple spreadsheet — source, type, date, relevance, key finding, limits — is enough.

### 18.4 Validity

Four classic threats. **Construct validity**: does the measure capture the concept? (Counting "incidents reported" measures reporting, not incidents.) **Internal validity**: is the claimed cause really the cause? (Hospitals with more security staff may report more incidents because they detect more.) **External validity**: does the result generalise? (Findings from large urban hospitals may not apply to rural clinics.) **Reliability**: would another researcher get the same result? (Two coders classifying incident reports should agree; measure their agreement.) Sommer and Paxson's critique of machine-learning intrusion detection is a classic example of external-validity problems in security research ([Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 18.5 Worked example: a comparative question (synthetic plan)

**This plan is synthetic.** A student in the CRP's internship programme asks: "Which of three backup strategies best supports four-hour restoration of CEDC's dispatch service?" Design: comparative, using the same criteria (restore time measured in an isolated drill, resilience to backup-server compromise, operational burden, cost). Data: three timed restores in an isolated test environment provided by CEDC under written authorisation, vendor documentation, and interviews with two administrators. Validity notes: three drills are a small sample (report intervals, Chapter 37); the test environment may differ from production (external validity — document differences); the student designed the drills (reliability — have an administrator repeat one). Output: a recommendation with stated assumptions, not a universal claim about backup products.

### 18.6 Practical activity

Write three research questions on one topic of your choice in critical-sector security: one descriptive, one comparative and one case-study question. For each, name the population, variables, time frame and the type of evidence you would need.

For example, on unsupported medical devices: descriptive, "how many CVH clinical devices were past end of support in 2026?"; comparative, "which of three approaches reduces exposure most within a budget?"; case study, "how did one hospital manage its imaging workstations during a replacement delay?" Note for each whether the evidence is obtainable under authorisation.

### 18.7 Common errors and limits

- Questions too broad to answer or too narrow to matter.
- Unrecorded literature searches that cannot be repeated.
- Over-generalising from one case.
- Mistaking correlation in incident data for cause.
- Collecting data about people or real systems without ethical approval and authorisation (Chapter 10).

The CEDC backup plan avoids these by naming the population (CEDC's dispatch service), limiting the claim to three strategies, recording sources, and treating three drills as a small sample. A study of "ransomware in hospitals" would fail the first test. A student who interviewed CEDC administrators without consent would fail the fifth whatever the quality of the analysis.

### Exercises — chapter 18

**EX035 — Sharpen the question.** *Objective:* make a topic researchable. *Inputs:* topic "phishing in the energy sector". *Steps:* write a research question with population, variables, time frame and answer type; state which design fits. *Expected evidence:* question and design. *Rubric:* 3 = specific, answerable with obtainable evidence, design justified; 2 = specific but evidence unobtainable; 1 = still a topic; 0 = none.

**EX036 — Name the threat.** *Objective:* identify validity threats. *Inputs:* "Hospitals that bought product X had 40% fewer reported ransomware incidents, so X prevents ransomware." *Steps:* name and explain three validity threats. *Expected evidence:* three threats. *Rubric:* 3 = construct (reported vs actual), internal (confounders such as budget/maturity, selection), external (which hospitals), or reliability; 2 = two; 1 = one; 0 = none.

### Chapter synthesis

Research starts with a question specific enough to be answered and disputed. Choose the design the question needs, search and screen literature in a way someone else could repeat, and name the threats to validity before a reviewer does.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue studying — chapter 18 of 40

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Chapter 19 — Critical infrastructure and sector security: scope and theory

### Learning outcomes and connection

After this chapter you can (1) explain what makes infrastructure "critical" and compare how the United States, the European Union and the United Kingdom define and organise it; (2) use the ideas of critical functions, interdependency and resilience to analyse a service; (3) compare three theoretical lenses — risk, resilience and safety/systems — and say what each sees and misses; and (4) place an organisation in its regulatory and sector context. It opens the field core of the book and builds on all of Chapters 1–18.

### 19.1 What "critical" means

Infrastructure is **critical** when its disruption would seriously harm health, safety, economic security or the functioning of society. Governments operationalise this differently. The United States designates sixteen critical-infrastructure sectors, from energy and water to healthcare and financial services ([CISA, Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors)), and complements sectors with a set of **National Critical Functions** — functions such as "supply water" or "provide medical care" whose disruption would be debilitating ([CISA, NCF set](https://www.cisa.gov/national-critical-functions-set)). The European Union regulates cybersecurity of "essential" and "important" entities across many sectors through the NIS2 Directive ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)), the broader physical and operational resilience of "critical entities" through the CER Directive ([Directive (EU) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)), and the digital operational resilience of financial entities through DORA ([Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)). The UK's National Cyber Security Centre publishes the Cyber Assessment Framework used to assess operators of essential services ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)).

The **functions view** is often more useful than the sector view. Calder Valley Hospital is "healthcare", but the function people need is "provide emergency care", which depends on electricity, water, communications, dispatch and supply chains run by other sectors.

### 19.2 Three lenses

**Risk** (Chapter 23) asks: what could happen, how likely, how bad, and which controls reduce it most for the money? Its strength is prioritisation; its weakness is that rare, novel or cascading events are poorly captured by likelihood estimates. **Resilience** asks: when disruption happens — whatever its cause — how does the service absorb, adapt and recover? Haimes defines resilience as the ability to withstand a major disruption within acceptable degradation and recover within acceptable time and cost ([Haimes, 2009](https://doi.org/10.1111/j.1539-6924.2009.01216.x)); Bruneau and colleagues measured it as the loss of service quality over time ([Bruneau et al., 2003](https://doi.org/10.1193/1.1623497)). NIST's cyber-resiliency engineering guidance applies these ideas to systems ([SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1)). **Safety and systems** views treat accidents as the result of inadequate control over interacting components rather than single failures ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)) and remind us that human error is usually a symptom of system design ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). A competent analyst uses all three: risk to prioritise, resilience to prepare for what risk analysis missed, systems thinking to understand how organisations and technology fail together.

### 19.3 What is distinctive about the field

Five features recur across sectors: **physical consequences** (harm to people and environment, not only data); **long-lived technology** (Chapter 2); **interdependency** (Chapter 22); **regulation and public accountability**; and **mixed ownership** — most infrastructure is privately operated but publicly relied upon, so incentives to invest in rare-event protection are weak. These features explain why "apply the enterprise IT playbook" fails and why sector-specific knowledge matters.

At Calder these features are concrete: CVH's harm is physical (patients), CPN's RTUs last decades, the substation feeds four other services (Lab 3), each operator answers to its own regulator, and most are private companies whose failure harms county residents who are not their customers.

### 19.4 Worked example: profiling CEDC (synthetic)

**This case is synthetic.** A sector profile of the County Emergency Dispatch Centre: *function* — receive emergency calls and dispatch ambulances, fire and police; *harm from loss* — delayed response within minutes; *dependencies* — telecom (calls and CAD data), power (UPS and generator), CAD vendor cloud services, staff; *regulatory context* — public-service duties and, depending on jurisdiction, cybersecurity obligations for essential entities (to be verified with counsel); *lenses* — risk: ransomware on CAD is the top scenario; resilience: the paper-and-radio fallback must sustain dispatch for hours; systems: a 2 a.m. switchover to paper is a human-factors problem as much as a technical one. The profile does not yet say what to do; it says what questions matter.

### 19.5 Practical activity

Choose one real sector in your country. From official sources, find: who designates it as critical, which law or framework sets its cybersecurity obligations, which agency supervises it and which public guidance applies. Record each source with its date. Do not assume the EU, US or UK model applies elsewhere.

Record the jurisdiction and the date of each source, because definitions change: the EU replaced its earlier network-security directive with NIS2, and national transposition dates differ. Where a framework applies only above a size threshold, note the threshold and whether the operator you chose meets it.

### 19.6 Common errors and limits

- Equating "critical infrastructure" with "OT".
- Reading a sector list as a list of independent sectors.
- Using one lens and ignoring what the others reveal.
- Stating legal obligations without checking the current text and jurisdiction.

CEDC shows the first error: a dispatch centre has almost no OT and is still critical. Lab 3 shows the second: the substation, telecom and water entries depend on each other. Using only the risk lens on CEDC would miss the 2 a.m. paper-switchover problem. And the CEDC profile deliberately leaves its legal obligations "to be verified with counsel".

### Exercises — chapter 19

**EX037 — Functions not sectors.** *Objective:* apply the functions view. *Inputs:* Calder Mutual. *Steps:* name two critical functions it supports, their dependencies on other sectors, and the harm timeline if each stops. *Expected evidence:* short profile. *Rubric:* 3 = functions such as "provide payment services" and "provide cash access", dependencies on power/telecom/other financial infrastructure, harm timeline (hours for payments, days for salaries/benefits); 2 = sector-level only; 1 = vague; 0 = none.

**EX038 — Three lenses.** *Objective:* compare theories on one case. *Inputs:* CW treatment works. *Steps:* write one question each lens would ask and one thing each might miss. *Expected evidence:* three pairs. *Rubric:* 3 = risk (likely scenarios; misses novel cascades), resilience (recovery/degraded modes; may underweight prevention economics), systems (control structure, human/organisational factors; harder to quantify); 2 = two lenses; 1 = one; 0 = none.

### Chapter synthesis

Infrastructure is critical because society depends on its functions. Jurisdictions organise it differently through sectors, functions and laws such as NIS2, CER and DORA. Risk, resilience and systems thinking are complementary lenses, and the field's distinctive features — physical consequence, longevity, interdependency, regulation and mixed ownership — explain why it needs its own discipline.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue studying — chapter 19 of 40

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Chapter 20 — Critical infrastructure and sector security: foundational cases

### Learning outcomes and connection

After this chapter you can (1) summarise six public cases that shaped the field from their primary or authoritative sources; (2) separate what the sources establish from what is commonly repeated; (3) extract transferable lessons and compare them across sectors; and (4) handle revised accounts honestly. It builds on Chapter 19 and prepares Chapter 31 (advanced cases) and the capstone. All descriptions stay at the level of the cited sources; no case is taught as a technique.

### 20.1 Reading a case

For each case, record: **date and sector**; **what happened to the service** (scope, duration, people affected); **initial access and spread** only as the source describes; **response**; **source type** (government advisory, audit report, peer-reviewed analysis, company statement, journalism); and **what remains uncertain**. Early reports are often wrong; later reports often correct them. A good analyst cites both.

For Oldsmar this record has two dates: the 2021 advisory and the 2023 statement that revised it. Both belong in the record, with the advisory's account labelled as superseded rather than deleted.

### 20.2 Six cases

**Ukraine power distribution, December 2015.** CISA's alert describes coordinated attacks on three regional distribution companies that caused outages affecting approximately 225,000 customers, with remote operation of breakers, destruction of some systems and disruption of call centres; power was restored by switching to manual operation ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01); see also the [E-ISAC/SANS analysis](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and)). *Lesson:* manual fallback and staff who can operate without automation were decisive.

**WannaCry and the NHS, May 2017.** The UK National Audit Office found that the ransomware disrupted at least a third of NHS trusts in England, led to cancelled appointments and diverted ambulances, and that the affected organisations had unpatched or unsupported Windows systems; the NHS had not rehearsed a national response ([NAO, 2017](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/)). *Lesson:* untargeted malware can cause clinical harm; basic hygiene and rehearsed coordination matter.

**TRITON/HatMan, 2017.** CISA's malware analysis report describes malware designed to interact with a specific safety instrumented system controller, the layer meant to prevent physical harm ([CISA MAR-17-352-01](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)). *Lesson:* safety systems are targets, and their independence from control networks must be real.

**Oldsmar water treatment, February 2021.** CISA's advisory reported that unidentified actors accessed a water-treatment plant's control system through remote-access software and increased the sodium hydroxide setpoint, which an operator noticed and reversed ([CISA AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)). In 2023 a former city manager said the event was likely an employee error rather than an intrusion ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). *Lesson:* whatever the cause, unmanaged remote access and reliance on one attentive operator were weaknesses — and public narratives can be revised.

**Colonial Pipeline, May 2021.** The joint CISA–FBI advisory on DarkSide ransomware reports that the actors deployed ransomware against a pipeline company's IT network, that there was no indication its OT networks had been directly affected, and that the company proactively disconnected certain OT systems to ensure their safety ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)). CISA's two-year retrospective names the company and recalls the fuel queues along the eastern seaboard that followed ([CISA, 2023](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years)). *Lesson:* an IT compromise can stop OT operations through business dependencies and precautionary decisions, without touching the control system.

**CrowdStrike update, July 2024.** A faulty security-software update crashed Windows machines worldwide; Microsoft estimated about 8.5 million devices were affected, disrupting airlines, hospitals and banks ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)). *Lesson:* no adversary is needed; a shared software dependency is a single point of failure across sectors.

### 20.3 Comparing the cases

| Case | Cause | Sector effect | Transferable lesson |
|---|---|---|---|
| Ukraine 2015 | Deliberate attack | Power cut | Manual operation capability |
| WannaCry 2017 | Untargeted malware | Clinical disruption | Hygiene, rehearsed coordination |
| TRITON 2017 | Targeted malware | Safety layer threatened | Safety-system independence |
| Oldsmar 2021 | Disputed | Near-miss chemical dosing | Remote access governance; revised accounts |
| Colonial 2021 | Ransomware on IT | Precautionary OT shutdown | IT–OT business dependency |
| CrowdStrike 2024 | Faulty update | Cross-sector outage | Shared-dependency concentration |

The table compresses each case into one lesson so they can be compared; it is not a summary of what happened. Read across the "Cause" column: two of the six involve no targeted attack on the control system at all.

### 20.4 Worked example: lessons for CVH (synthetic application)

**The application is synthetic; the cases are cited above.** For Calder Valley Hospital the transferable lessons are: (1) rehearse operation without IT (paper processes, as Ukraine's operators did without automation); (2) inventory and isolate unsupported devices (WannaCry); (3) confirm that a BMS compromise cannot stop theatre ventilation's local safety controls (TRITON's lesson about independent layers); (4) govern remote access to the BMS (Oldsmar); (5) map which clinical processes depend on business IT such as patient administration (Colonial); and (6) plan for mass failure of a shared endpoint product (CrowdStrike).

### 20.5 Common errors and limits

- Repeating vivid details that no primary source supports.
- Citing the first account and ignoring the correction.
- Treating every case as an attack.
- Turning a case study into an attack recipe.

Common examples: claiming Oldsmar was "a hack" without the 2023 revision; repeating outage durations not in the cited source; calling CrowdStrike an attack; or describing Stuxnet's techniques when the lesson is the failed assumption. Each of the six summaries here stays at the level its source supports, and EX039 asks you to check one.

### Exercises — chapter 20

**EX039 — Primary source check.** *Objective:* separate source from repetition. *Inputs:* one of the six cases in this chapter. *Steps:* read the cited source and list three facts it states, one commonly repeated claim it does not state (find one in a news article or blog), and how you would phrase the case for a report. *Expected evidence:* list and phrasing. *Rubric:* 3 = accurate facts with locations in the source, an unsupported claim identified, careful phrasing; 2 = facts only; 1 = facts from secondary sources; 0 = none.

**EX040 — Cross-sector lesson.** *Objective:* transfer a lesson. *Inputs:* Colonial Pipeline. *Steps:* apply its lesson to Calder Transit: which business IT systems could force a precautionary stop of rail operations, and what could prevent that? *Expected evidence:* two dependencies and two measures. *Rubric:* 3 = e.g. ticketing/revenue, crew scheduling, passenger information; measures such as pre-agreed degraded-operation rules and separating operational from business dependencies; 2 = one each; 1 = generic; 0 = none.

### Chapter synthesis

The field's foundational cases teach through comparison: manual fallback, hygiene, safety-system independence, remote-access governance, IT–OT business dependency and shared-dependency concentration. Read the primary sources, keep revisions in view and transfer lessons, not techniques.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue studying — chapter 20 of 40

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 →](#ch-21)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Chapter 21 — Critical infrastructure and sector security: system models

### Learning outcomes and connection

After this chapter you can (1) describe a control loop and the components of a SCADA or industrial control system; (2) place assets in a layered reference model from field devices to enterprise; (3) model a service as a chain of functions with degraded modes; and (4) say what kinds of attack or failure each part of the model is exposed to. It builds on Chapters 7, 16 and 19 and prepares Chapter 22 (data and dependencies) and Chapter 28 (failure analysis).

### 21.1 The control loop

Every physical process controlled by computers follows a loop: a **sensor** measures (tank level, line current, train position); a **controller** compares the measurement with a **setpoint** and computes an action; an **actuator** acts (pump speed, breaker trip, signal aspect); the process responds; the sensor measures again. **Programmable logic controllers** (PLCs) and **remote terminal units** (RTUs) run the loop locally. A **SCADA** system (supervisory control and data acquisition) supervises many loops across a wide area: it collects measurements, shows them to operators on **human–machine interfaces** (HMIs), stores history in a **historian** and sends setpoints and commands. **Safety instrumented systems** (SIS) watch for dangerous conditions and act independently to bring the process to a safe state ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

The loop gives a precise vocabulary for what can go wrong: false **measurements** (the controller acts on a lie), false **commands** (the actuator does something unintended), loss of **view** (operators cannot see), loss of **control** (operators cannot act), and compromise of **protection** (the SIS cannot act). MITRE ATT&CK for ICS organises impacts in similar terms, such as loss of view, loss of control and manipulation of control ([ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)).

### 21.2 A layered reference model

A layered model — widely known as the Purdue model — places assets by function: level 0 the physical process with sensors and actuators; level 1 basic control (PLCs, RTUs, SIS); level 2 supervisory control (HMIs, local SCADA); level 3 site operations (historians, engineering workstations); a DMZ; and levels 4–5 enterprise IT. The model is a teaching and segmentation aid, not a law of nature: cloud-connected sensors, vendor remote services and wireless field devices cross levels. Use it to ask "which paths cross levels, and are they controlled?"

### 21.3 Service chains and degraded modes

Operators care about services, not levels. Model a service as a chain of functions with **degraded modes**: Calder Water's "supply safe water" = abstract raw water → treat → monitor quality → store → pump → distribute. Each function has normal, degraded and failed states. "Monitor quality" degraded might mean manual sampling every hour instead of continuous analysers; "pump" degraded might mean local control by staff at the station without SCADA. A service model that includes degraded modes shows how long the service can continue when automation is lost — the question Ukraine's operators answered in 2015 (Chapter 20).

### 21.4 Worked example: CPN feeder restoration (synthetic)

**This case is synthetic.** Calder Power Networks' service "restore supply after a feeder fault": a protection relay trips the faulted section (level 1, independent of SCADA); the RTU reports the trip (level 1→2); the operator sees it on the HMI (level 2) and remotely recloses or reconfigures (level 2→1); customers are informed via the outage system (level 4). Failure analysis by element: if the relay fails, a fault persists — safety issue; if the RTU link fails, operators lose view of that feeder — degraded mode: dispatch a crew; if the HMI is compromised, false status could lead operators to energise a line where crews are working — safety issue that procedures (locks, permits, verbal confirmation) must catch; if the outage system fails, customers are not informed — a service-quality issue. The model shows that the most severe consequences sit where cyber manipulation meets human safety procedures.

### 21.5 Practical activity

Draw the control loop and layered model for one Calder service other than water or power (rail signalling or hospital theatre ventilation). Label each component with its level, which of view/control/protection it supports, and one degraded mode.

For theatre ventilation, the sensor might be a duct pressure or air-change sensor at level 0, the BMS controller at level 1, the estates workstation at level 2, and the BMS server at level 3. A degraded mode is local manual control of the air-handling units. Mark which component supports view, control or protection; a hard-wired minimum-airflow interlock, if present, is protection.

### 21.6 Common errors and limits

- Treating the layered model as a description of real traffic.
- Ignoring safety systems or assuming they are always independent.
- Modelling assets without the service they support.
- Assuming loss of SCADA means loss of the service.

CPN's feeder model shows the first two: the relay sits at level 1 and acts without SCADA, but if it were networked with the HMI its independence would need evidence. The third error would list RTUs without saying they serve feeder restoration. The fourth ignores the degraded mode of dispatching a crew when an RTU link fails.

### Exercises — chapter 21

**EX041 — Name the loss.** *Objective:* use the loop vocabulary. *Inputs:* (a) a historian outage; (b) an HMI showing frozen values; (c) a forged setpoint accepted by a PLC; (d) a disabled SIS trip. *Steps:* classify each as loss of view, loss of control, manipulation or loss of protection, and state the immediate risk. *Expected evidence:* four classifications. *Rubric:* 3 = (a) loss of historical view, low immediate risk; (b) loss of view, dangerous because operators may act on stale data; (c) manipulation of control; (d) loss of protection, highest severity; 2 = one wrong; 1 = two wrong; 0 = none.

**EX042 — Degraded modes.** *Objective:* model continuity without automation. *Inputs:* Calder Transit's "run a safe train service". *Steps:* write the function chain and a degraded mode for three functions, with the constraint each imposes (e.g. reduced frequency). *Expected evidence:* chain and modes. *Rubric:* 3 = sensible chain (signalling, train control, crew communication, passenger information, ticketing) with realistic degraded modes and constraints; 2 = chain without constraints; 1 = vague; 0 = none.

### Chapter synthesis

Control systems are loops of sensing, deciding and acting, supervised by SCADA and protected by independent safety systems. Layered models aid segmentation; service chains with degraded modes show how long a service can survive without automation. The worst consequences arise where manipulation meets safety and human procedure.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Continue studying — chapter 21 of 40

[← Chapter 20](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 →](#ch-22)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Chapter 22 — Critical infrastructure and sector security: data and dependencies

### Learning outcomes and connection

After this chapter you can (1) build and maintain an asset and dependency inventory from several imperfect sources; (2) add time to a dependency model using backup autonomy; (3) compute which services are lost for outages of different lengths and identify the weak links; and (4) state the data-quality limits of such models. It builds on Chapters 6, 9 and 21 and prepares Chapter 23 (risk methods) and Chapter 28 (failure analysis).

### 22.1 Inventory is evidence, not a list

No organisation knows exactly what it has. Asset data comes from purchasing records, network observations, configuration databases, vendor documentation and walking the site; each source misses something. Treat the inventory as evidence with sources and dates (Chapter 15): for each asset record who confirmed it and when. **Passive** network observation finds devices that talk; it misses idle and serial devices. **Active** scanning finds more but can disrupt fragile OT devices and must only be done under authorisation with operations' agreement (Chapter 10). Dependencies are harder still: they live in people's heads, contracts and unwritten habits.

### 22.2 Kinds of dependency

Rinaldi and colleagues distinguish **physical** (power to pumps), **cyber** (telemetry over telecom), **geographic** (cables in the same trench) and **logical** (financial or regulatory ties) interdependencies ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131)). Add **people** (one engineer who knows the legacy system) and **suppliers** (a single CAD vendor, a cloud region). Chapter 6's graph showed *what can be affected*; time turns it into *what will be lost when*. Each service has **autonomy**: how long it continues on its own backup — batteries, generators and fuel, stored water, paper processes.

### 22.3 Worked example and Lab 9 (synthetic)

**This case is synthetic.** The CRP collected backup autonomy for key services during a regional grid outage. Card payments depend on telecom exchange A, which has batteries only; exchange B also has a generator.

```python
# Lab 9 - which services survive a grid outage of a given length? (synthetic backup autonomy, offline)
AUTONOMY_H = {  # hours each service keeps running on its own backup
    "hospital (generator, fuel on site)": 72, "telecom exchange A (batteries)": 4,
    "telecom exchange B (batteries + generator)": 48, "water pumps (no generator)": 0,
    "water treated storage": 10, "dispatch centre (UPS + generator)": 24,
    "card payments (relies on telecom)": None, "rail signalling (UPS)": 2,
}
for outage in (1, 6, 30):
    down = []
    for s, h in AUTONOMY_H.items():
        if h is None:   # dependent service: fails when 4-h exchange A fails
            h = AUTONOMY_H["telecom exchange A (batteries)"]
        if h < outage: down.append(s.split(" (")[0])
    print(f"outage {outage:>2} h -> {len(down)} services lost: {', '.join(down) or 'none'}")
```

Expected output:

```text
outage  1 h -> 1 services lost: water pumps
outage  6 h -> 4 services lost: telecom exchange A, water pumps, card payments, rail signalling
outage 30 h -> 6 services lost: telecom exchange A, water pumps, water treated storage, dispatch centre, card payments, rail signalling
```

Interpretation: the shortest autonomies set the early story — pumps stop at once (customers still receive stored water for about 10 hours), rail signalling stops after 2 hours, and card payments fail after 4 hours because exchange A has no generator. At 30 hours, water supply and dispatch are lost. The hospital's 72 hours looks reassuring, but its water arrives from storage that lasts 10 hours: a building can be powered and still unusable. The model is crude — it ignores dependencies of the backups themselves (who refuels the dispatch generator after 24 hours, and over which roads?) — but it already identifies three cheap questions: can exchange A get a generator; can water pumps get a mobile generator connection point; and what fuel-delivery agreements exist across operators?

### 22.4 Data quality

Every number above is an operator's claim. Generator autonomy depends on fuel actually in the tank, starting reliability (Chapter 12, EX024) and load. Battery autonomy degrades with age. Record the evidence behind each autonomy — a test, a design figure, an estimate — and run the model with pessimistic values. A dependency model is only as good as its least-checked number.

In Lab 9, halving every autonomy (EX043) moves water treated storage into the 6-hour loss list.

For CEDC's generator, the evidence would be the last load test date and the fuel level on the day of the survey.

### 22.5 Common errors and limits

- Treating one inventory source as complete.
- Recording dependencies without time.
- Taking autonomy figures from design documents without tests.
- Forgetting second-order dependencies of backups (fuel, staff, roads).
- Active scanning of OT without authorisation and operational agreement.

Lab 9 illustrates the first three: a design autonomy of 72 hours for the hospital assumes a full tank, and exchange A's 4 hours assumes healthy batteries. The fourth is the refuelling question behind the dispatch centre's 24 hours. The fifth is why the CRP's inventory relied on passive observation and operator statements rather than scanning.

### Exercises — chapter 22

**EX043 — Fix the weak link.** *Objective:* test an intervention. *Inputs:* Lab 9. *Steps:* give card payments the autonomy of exchange B (48 h), and rerun. Then halve every autonomy (pessimistic case) and rerun for 6 h. Report both and recommend. *Expected evidence:* two outputs and a recommendation. *Rubric:* 3 = card payments survive to 48 h in the first run; the pessimistic 6-h run loses telecom exchange A, water pumps, water treated storage, card payments and rail signalling (5 services); recommendation addresses evidence for autonomy figures; 2 = runs without recommendation; 1 = one run; 0 = none.

**EX044 — Second-order dependencies.** *Objective:* look behind backups. *Inputs:* the dispatch centre's 24-hour generator. *Steps:* list four dependencies of that backup itself and one way to evidence each. *Expected evidence:* list. *Rubric:* 3 = fuel supply contract and delivery route, staff to operate/refuel, generator start reliability (test records), cooling/ventilation or switchgear; each with evidence; 2 = three; 1 = one or two; 0 = none.

### Chapter synthesis

Inventories and dependency maps are evidence with sources, dates and gaps. Adding time — backup autonomy — turns exposure into a timeline of loss, exposes weak links such as a battery-only exchange and reveals that a powered building can still be unusable. Test autonomy claims and look behind each backup to its own dependencies.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Continue studying — chapter 22 of 40

[← Chapter 21](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 →](#ch-23)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Chapter 23 — Critical infrastructure and sector security: methods I

### Learning outcomes and connection

After this chapter you can (1) carry out a structured risk assessment following the stages in NIST SP 800-30; (2) explain the weaknesses of risk matrices; (3) apply a consequence-first approach that starts from the worst effects on the service; and (4) compare the two approaches on one case and say when each is appropriate. It builds on Chapters 1, 12, 15 and 19–22 and prepares Chapter 24 (controls) and Chapter 26 (methods II).

### 23.1 A structured risk assessment

NIST SP 800-30 describes risk assessment in stages: **prepare** (purpose, scope, assumptions, sources); **conduct** (identify threat sources and events, vulnerabilities and predisposing conditions, determine likelihood and impact, determine risk); **communicate** results; and **maintain** the assessment as things change ([SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). The method's strength is discipline: it forces you to write down scope and assumptions, and to say where each judgement came from. Its outputs are usually qualitative ratings (very low to very high) on scales the organisation defines.

### 23.2 The trouble with matrices

Many organisations combine likelihood and impact ratings in a 5×5 **risk matrix**. Matrices are easy to communicate but have known problems. Ordinal labels ("3 = possible") are multiplied as if they were numbers. Very different risks receive the same cell. Rare, catastrophic events land in the same colour as frequent minor ones. Ratings depend heavily on who is in the room. Chapter 1's habit helps: where possible, put rough quantities behind the labels (an annual probability range, an outage duration, a harm), and show the worst credible consequence separately from the rating.

### 23.3 Consequence-first

For critical services, likelihood is often the least knowable input: adversaries adapt, and the events that matter most are rare. A **consequence-first** approach starts from the other end: identify the outcomes that must not happen (loss of water supply to the hospital for more than 8 hours; uncontrolled chlorine dosing), trace which functions and systems could cause them, and ask what an adversary or failure would need to achieve each. Idaho National Laboratory's **Consequence-driven Cyber-informed Engineering** (CCE) formalises this: identify high-consequence events, map the systems involved, illuminate the paths an adversary would take, and mitigate — preferably with engineering changes that remove the possibility rather than detect it ([INL CCE](https://inl.gov/national-security/cce/)). ISA/IEC 62443-3-2 also bases its risk assessment for system design on zones, conduits and consequences ([IEC 62443-3-2 catalogue page](https://webstore.iec.ch/en/publication/30727)).

### 23.4 Worked example: chlorine dosing at CW (synthetic)

**This case is synthetic.** *Risk-matrix view:* the threat "unauthorised change to chlorine dosing setpoint" is rated likelihood 2 (unlikely) and impact 5 (severe) = 10, amber. The register says "monitor". *Consequence-first view:* the unacceptable outcome is "water leaving the works with chlorine outside safe limits for long enough to harm customers". Paths: a setpoint change from the HMI (operator error or compromise); a forged command to the dosing PLC over the control network; a sensor reporting false residual chlorine so the controller over-doses; a vendor laptop connected to the PLC. Engineering mitigations that do not depend on detecting the attacker: a hard-wired maximum dosing-pump rate; an independent residual-chlorine analyser on the outlet that trips the outlet valve via a separate circuit; a physical key switch for PLC programming mode. The matrix said "monitor"; the consequence analysis produced three concrete changes, one of which (the hard limit) removes the most dangerous outcome regardless of how the attacker got in.

### 23.5 Practical activity

Take Calder Transit's light-rail signalling. Write one unacceptable consequence, three paths to it (at least one non-malicious), and one engineering mitigation that removes or bounds the consequence. Then rate the same scenario on a 5×5 matrix and compare what each approach told you.

For signalling, an unacceptable consequence might be "two trains authorised into the same block". Paths include a corrupted interlocking configuration after maintenance (non-malicious), a forged command from a compromised control workstation, and a failed track circuit misread as clear. An engineering mitigation is the interlocking's own safety logic, independent of the control workstation. On a 5×5 matrix the same scenario may score 5 for impact and 1 for likelihood, giving a cell that understates it.

### 23.6 Common errors and limits

- Multiplying ordinal labels as if they were measurements.
- Rating likelihood for novel adversary actions with false confidence.
- Treating "monitor" as a mitigation.
- Consequence-first analysis that only lists consequences and never maps paths or mitigations.
- Ignoring non-malicious paths to the same consequence.

The chlorine example shows the third error directly: the matrix result "monitor" left the dangerous outcome possible. The first error produced its score of 10. The consequence analysis avoided the fourth by naming paths and mitigations, and the fifth by listing operator error and false sensor readings as paths beside compromise.

### Exercises — chapter 23

**EX045 — Same cell, different risk.** *Objective:* expose matrix limits. *Inputs:* risk A: likelihood 5, impact 2 (daily nuisance outages of the staff Wi-Fi); risk B: likelihood 2, impact 5 (loss of CVH theatre ventilation). *Steps:* compute both matrix scores, explain why the equal score misleads and propose how to present them instead. *Expected evidence:* scores and explanation. *Rubric:* 3 = both 10; explains ordinal misuse and the different nature of harm; proposes separate worst-credible-consequence column or quantitative ranges; 2 = partial; 1 = scores only; 0 = none.

**EX046 — Consequence-first.** *Objective:* apply the method. *Inputs:* Calder Mutual's payment switch. *Steps:* define one unacceptable consequence, map three paths and give one engineering mitigation and one procedural one. *Expected evidence:* the analysis. *Rubric:* 3 = specific consequence (e.g. fraudulent high-value transfers released, or payments unavailable > 4 h on salary day), plausible paths including insider/error, engineering mitigation (hard transaction limits, out-of-band confirmation) and procedural one; 2 = generic; 1 = consequence only; 0 = none.

### Chapter synthesis

Structured risk assessment brings discipline to scope, assumptions and judgement; risk matrices simplify communication but distort comparisons. Consequence-first methods such as CCE start from what must not happen and favour engineering mitigations that bound harm regardless of the attacker. Use both, and say which one drives each recommendation.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Continue studying — chapter 23 of 40

[← Chapter 22](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 →](#ch-24)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Chapter 24 — Critical infrastructure and sector security: controls

### Learning outcomes and connection

After this chapter you can (1) use a framework — NIST CSF 2.0, the UK CAF or sector goals — to organise controls; (2) classify controls by type (preventive, detective, corrective) and nature (technical, procedural, physical, engineering); (3) map controls to the scenarios and techniques they address and find gaps; and (4) choose controls appropriate to OT constraints. It builds on Chapters 16 and 23 and prepares Laboratory I (Chapter 25) and Chapter 27 (verification).

### 24.1 Frameworks as organisers

A **framework** organises outcomes so nothing large is forgotten. NIST's Cybersecurity Framework 2.0 groups outcomes under six functions: Govern, Identify, Protect, Detect, Respond and Recover ([NIST CSF 2.0](https://www.nist.gov/cyberframework)). The UK CAF expresses outcomes and indicators of good practice for operators of essential services ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)). Sector-specific goals exist too — for example, the US Department of Health and Human Services' healthcare cybersecurity performance goals ([HHS HPH CPGs](https://hphcyber.hhs.gov/performance-goals.html)). Detailed control catalogues such as NIST SP 800-53 list specific controls ([SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)). Frameworks tell you *what outcomes* to achieve; they do not tell you which risk matters most for your service — that comes from Chapter 23.

### 24.2 Types of control

**Preventive** controls stop an event (allowlisting, authentication, a hard-wired limit). **Detective** controls notice it (monitoring, integrity checks, alarms). **Corrective** or **recovery** controls restore service (backups, manual procedures, spare equipment). By nature, controls are **technical**, **procedural** (two-person approval, change management), **physical** (locked cabinets, key switches) or **engineering** (designs that make a harmful state impossible, such as a pump sized so it cannot overdose). In OT, engineering and physical controls are often the most reliable, because they keep working when computers are compromised.

### 24.3 Mapping and gaps

A control is only valuable against something. Build a **mapping** from scenarios (or catalogued techniques, for example from [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)) to controls, with each control marked preventive, detective or corrective. Gaps show up as scenarios with only detective controls (you will know, but not stop it), with no corrective control (you cannot recover), or covered only by controls that share a single point of failure (Chapter 16's common mode). The mapping also exposes **orphan controls** that address nothing on your list — candidates for review.

### 24.4 OT constraints

Some controls standard in IT are risky or impossible in OT: endpoint agents that consume controller resources, automatic patching, active scanning, account lockout on an operator HMI during an emergency (locking out the operator may be more dangerous than the attacker). Alternatives include passive network monitoring, application allowlisting on stable workstations, read-only data diodes for one-way flows, physical key switches for programming modes, and procedural controls tied to the operator's shift log.

CVH's BMS map in this chapter applies these alternatives.

### 24.5 Worked example: CVH BMS control map (synthetic)

**This case is synthetic.**

| Scenario | Preventive | Detective | Corrective | Gap |
|---|---|---|---|---|
| Remote compromise of BMS via corporate network | Firewall allowlist to BMS server; MFA for BMS admin | Passive monitoring of BMS VLAN | Local manual control of air-handling units | None obvious; verify manual control drill |
| Malicious or mistaken change to theatre ventilation setpoints | Role-based change rights | Alarm on out-of-range air changes | Estates on-call restores setpoints | No independent limit: add hard-wired minimum airflow interlock |
| Vendor laptop on BMS controller | Locked cabinets; vendor escort | — | Restore controller config from backup | No detection; config backup untested |

The map turns a vague "BMS is a risk" into two specific actions: an engineering interlock and a tested configuration restore.

### 24.6 Common errors and limits

- Treating framework completion as risk reduction.
- Counting controls instead of mapping them to scenarios.
- Relying solely on detection for consequences that need prevention.
- Importing IT controls into OT without considering operational safety.

The CVH BMS map avoids each: it counts no controls, it maps them to three scenarios, it adds an engineering interlock where only detection existed, and it rejects IT controls such as automatic patching of the BMS controller. A framework score of "Protect: implemented" would have told the hospital nothing about theatre airflow.

### Exercises — chapter 24

**EX047 — Classify controls.** *Objective:* use type and nature. *Inputs:* offline backups; two-person payment approval; outlet chlorine analyser tripping a valve; SIEM alert on new admin accounts; key switch for PLC programming. *Steps:* classify each by type and nature. *Expected evidence:* table. *Rubric:* 3 = backups corrective/technical; two-person approval preventive/procedural; analyser trip preventive (limits consequence)/engineering; SIEM alert detective/technical; key switch preventive/physical; 2 = one error; 1 = two errors; 0 = none.

**EX048 — Find the gap.** *Objective:* map and judge. *Inputs:* the CVH table. *Steps:* add one scenario (ransomware on the BMS server) with controls in each column, then name the single most valuable improvement and justify it. *Expected evidence:* row and justification. *Rubric:* 3 = plausible controls including tested restore and local manual control; improvement justified by consequence; 2 = row without justification; 1 = incomplete row; 0 = none.

### Chapter synthesis

Frameworks organise outcomes; risk analysis decides priorities; mappings connect controls to the scenarios they address and reveal gaps. Prefer combinations of prevention, detection and recovery, and in OT favour engineering and physical controls that keep working when computers do not.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Continue studying — chapter 24 of 40

[← Chapter 23](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 →](#ch-25)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes and connection

After this laboratory you can (1) combine inventory, network-flow, vulnerability and access evidence into one assessment of a synthetic operator; (2) record methods, versions and outputs so that someone else can reproduce your results; (3) separate findings, interpretations and recommendations; and (4) assess your own work against a rubric. It integrates Labs 2, 4, 5 and 7 (Chapters 3, 7, 9 and 13) and the methods of Chapters 15, 23 and 24. It is the first project checkpoint of the course.

### 25.1 Purpose and rules

This laboratory is a contained assessment of the **synthetic** Calder operators using only the book's offline labs. Its rules of engagement (Chapter 10, practical activity) apply: your own computer, no network access to real systems, no real data. The skill being assessed is not running code — that is the easy part — but **assembling evidence into a defensible judgement** and documenting it so that another student could reproduce it.

Your RoE from Chapter 10's practical activity is the authorisation document for this laboratory.

### 25.2 The task

You are an intern for the County Resilience Partnership. Produce a 1,500-word **assessment note** answering: "Across the evidence available, what are the three highest-priority security improvements for Calder's operators, and how confident are we?" Use:

1. **Lab 2** (CVH inventory): unsupported and misplaced devices.
2. **Lab 4** (CW flows): violations of the conduit policy.
3. **Lab 5** (CPN advisories): vulnerable assets, ordered by exploitation and exposure.
4. **Lab 7** (access review): orphaned, dormant, shared and toxic accounts.

The question asks for three priorities across four operators, which forces comparison: a CW conduit violation and a CPN gateway flaw must be ranked against each other by consequence, not reported in separate lists.

### 25.3 Method and reproducibility

Record for each lab: the file name and a SHA-256 hash of the script you ran (`python3 -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" lab05.py`), the Python version, the exact output and any change you made. Reproducibility is evidence: a reader who reruns your script and gets the same output can trust your findings section without trusting you ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)).

Hash the script you actually ran, after any edits.

### 25.4 Structure of the note

1. **Summary** — three priorities, one sentence each, with confidence (high/medium/low) and why.
2. **Scope and method** — what was examined, how, what was not.
3. **Findings** — facts from outputs only (e.g. "VPN-01 runs 9.1; the fix is 9.3; the advisory states exploitation").
4. **Analysis** — consequence-first reasoning (Chapter 23): which findings could lead to the worst outcomes for which service.
5. **Recommendations** — each mapped to findings, with control type (Chapter 24) and owner.
6. **Limits** — sample size, synthetic data, unverified claims.
7. **Appendix** — hashes, versions, outputs.

Keep findings and analysis apart, as the format requires.

### 25.5 Worked example: one priority, fully argued (synthetic)

**Priority 1 — upgrade and re-architect CPN remote access (confidence: high).** *Finding:* VPN-01 (internet-exposed) runs a version older than the fix for an exploited, critical flaw (Lab 5). *Finding:* the original design places remote users directly on the control network (Chapter 16). *Analysis:* this is the shortest path from the internet to feeder control; the consequence is loss of control of distribution, the most severe outcome in the CPN service model (Chapter 21). *Recommendation:* emergency upgrade to 9.3 (corrective/technical; owner: CPN infrastructure lead, this week), then terminate remote access on a DMZ jump host with per-session vendor approval (preventive/technical and procedural; owner: CPN OT security, next quarter). *Confidence:* high, because the finding comes directly from version data and the advisory, and the consequence follows from the architecture. *Limit:* the lab cannot show whether the flaw has already been exploited; a compromise assessment of VPN-01 is recommended.

### 25.6 Assessment rubric

| Criterion | 3 (strong) | 2 | 1 | 0 |
|---|---|---|---|---|
| Evidence use | Every finding traceable to a lab output | Mostly traceable | Some unsupported claims | No evidence |
| Prioritisation | Consequence-first, compared across operators | Reasoned within operators | Ordered by severity labels only | None |
| Recommendations | Mapped to findings, typed, owned, dated | Mapped, missing owners | Generic | None |
| Limits and confidence | Specific and honest | Generic | Token | Absent |
| Reproducibility | Hashes, versions, outputs | Outputs only | Partial | None |

The rubric rewards the same habits as the worked priority: every finding traced to output, consequences compared across operators, owners and dates on recommendations, honest limits and a reproducible appendix. A note that scores 3 on evidence but 1 on prioritisation has listed findings without judging them.

### 25.7 Common errors and limits

- Listing every finding instead of prioritising.
- Recommendations that do not follow from any finding.
- Mixing facts and interpretations in the findings section.
- Claiming certainty that synthetic data cannot provide.

A note that lists all six Lab 4 flows, all five unsupported devices and every Lab 7 account has made the first error. Recommending MFA for CW without a finding about CW accounts is the second. Writing "the RDP connection is an intruder" in findings is the third. Claiming high confidence about real-world exploitation from synthetic data is the fourth.

### Exercises — chapter 25

**EX049 — Priorities 2 and 3.** *Objective:* complete the assessment. *Inputs:* Labs 2, 4, 7. *Steps:* write priorities 2 and 3 in the format of the worked priority above. *Expected evidence:* two argued priorities. *Rubric:* use the laboratory's assessment rubric; 3 = e.g. CW corporate→control RDP and control→internet flows investigated and closed (Lab 4), and leaver/toxic/vendor accounts (Lab 7) or isolation of unsupported clinical devices (Lab 2), each with consequence reasoning, owner and confidence; lower scores per rubric.

**EX050 — Reproducibility check.** *Objective:* verify a peer's work. *Inputs:* a classmate's appendix (or your own, exchanged). *Steps:* rerun each script, compare hashes and outputs, and write a 100-word verification statement. *Expected evidence:* the statement. *Rubric:* 3 = hashes and outputs compared, any discrepancy explained (e.g. edited script, Python version); 2 = outputs only; 1 = statement without rerunning; 0 = none.

### Chapter synthesis

Laboratory I turns separate exercises into one judgement. Trace every finding to reproducible output, reason from consequences across operators, map recommendations to findings and owners, and state confidence and limits explicitly.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Continue studying — chapter 25 of 40

[← Chapter 24](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 →](#ch-26)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Chapter 26 — Critical infrastructure and sector security: methods II

### Learning outcomes and connection

After this chapter you can (1) build structured threat models of a system using data-flow diagrams and a threat checklist; (2) apply systems-theoretic hazard analysis (STPA) to find unsafe control actions; (3) design and run a tabletop exercise as a method for testing plans; and (4) compare these methods with the risk methods of Chapter 23 and choose among them. It builds on Chapters 21–24 and prepares Chapter 27 (verification) and Chapter 28 (failure analysis).

### 26.1 Threat modelling with data flows

A **data-flow diagram** shows processes, data stores, external entities, flows and **trust boundaries** (where data crosses from one level of trust to another). Threat modelling walks each element and asks a checklist of questions. A widely used checklist, STRIDE, asks about **S**poofing identity, **T**ampering with data, **R**epudiation (denying an action), **I**nformation disclosure, **D**enial of service and **E**levation of privilege. Every flow that crosses a trust boundary deserves the full checklist. The output is a list of threats with the element, the threat type and a proposed mitigation.

### 26.2 STPA: hazards from control structure

Leveson's **STAMP** model treats accidents as the result of inadequate control rather than chains of component failure ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)). Its analysis method, **STPA**, proceeds: define losses and hazards; model the **control structure** (who controls what, with which feedback); for each control action, identify **unsafe control actions** (UCAs) in four forms — not provided when needed, provided when unsafe, provided too early/late or out of order, stopped too soon or applied too long; then find causal scenarios, including manipulated feedback or commands. STPA suits critical services because it treats operators, procedures, software and attackers within one structure.

### 26.3 Tabletop exercises

A **tabletop exercise** walks a team through a scenario in discussion, step by step, with injects ("it is now 03:40; the CAD screens show a ransom note"). It tests plans, roles and communication without touching live systems. Good tabletops have objectives (e.g. "test the decision to switch to paper dispatch"), a realistic synthetic scenario, a facilitator, observers recording decisions and timings, and a **hot debrief** followed by an improvement plan. They are evidence of preparedness only to the extent that findings are acted on.

### 26.4 Choosing methods

| Method | Best for | Weakness |
|---|---|---|
| Risk assessment (Ch. 23) | Prioritising across many scenarios | Likelihood estimates weak for novel threats |
| Consequence-first / CCE | Worst outcomes, engineering mitigations | Can neglect frequent moderate harms |
| STRIDE threat model | Software and data flows | Weak on physical process and humans |
| STPA | Control structures, human and software interactions | Effortful; needs process knowledge |
| Tabletop | Plans, roles, communication | Discussion is not execution |

For CEDC, the table suggests STPA for dispatch control and a tabletop for the paper fallback, as the chapter does; a risk assessment then ranks the resulting work.

### 26.5 Worked example: STPA for CEDC dispatch (synthetic)

**This case is synthetic.** Loss: delayed emergency response. Hazard: an ambulance is not dispatched to a life-threatening call within target time. Control structure: call handler → CAD → dispatcher → ambulance crew (via radio and mobile data terminals); feedback from vehicle location system to CAD. Control action: "assign nearest available ambulance". UCAs: *not provided* — CAD queue frozen after a failed update; *provided when unsafe* — CAD assigns a unit shown "available" because location feedback is stale or spoofed; *too late* — manual fallback adopted only after 20 minutes because nobody owns the decision; *stopped too soon* — a dispatcher cancels an assignment after a duplicate-call merge error. Each UCA leads to requirements: a CAD freeze alarm, staleness indicators on vehicle locations, a named fallback decision owner with a 5-minute trigger, and confirmation before cancelling a high-priority assignment. Note that two UCAs involve no attacker at all.

### 26.6 Common errors and limits

- Threat models without trust boundaries.
- STPA reduced to a list of component failures.
- Tabletops with no objectives or follow-up.
- Picking the most impressive method rather than the one the question needs.

The CEDC STPA avoided the second error by naming unsafe control actions, two without any attacker. A STRIDE review of the CW historian flow without marking the DMZ-to-control trust boundary would make the first. A tabletop without the objective "decide on paper dispatch" makes the third. And choosing STPA to impress when the question is "which backup strategy" makes the fourth.

### Exercises — chapter 26

**EX051 — STRIDE a flow.** *Objective:* apply the checklist. *Inputs:* the CW flow "historian collector in DMZ reads OPC UA from SCADA server". *Steps:* write one threat for each STRIDE letter with a mitigation. *Expected evidence:* six rows. *Rubric:* 3 = six plausible threats with matching mitigations (e.g. spoofed collector → mutual certificates; tampering → signed/authenticated session; DoS → rate limits on SCADA side); 2 = four or five; 1 = fewer; 0 = none.

**EX052 — Design a tabletop.** *Objective:* plan an exercise. *Inputs:* CVH, scenario "ransomware encrypts the patient-administration system on a Saturday night". *Steps:* write objectives (two), participants, four injects with times and the evidence you will record. *Expected evidence:* plan. *Rubric:* 3 = measurable objectives, clinical and technical participants, escalating realistic injects (including data-protection and communication decisions), recorded timings and decisions; 2 = partial; 1 = scenario only; 0 = none.

### Chapter synthesis

Threat modelling finds threats where data crosses trust boundaries; STPA finds unsafe control actions in socio-technical structures; tabletops test plans and people. Each sees what others miss, so choose by the question — and remember that many hazards involve no adversary at all.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Continue studying — chapter 26 of 40

[← Chapter 25](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 →](#ch-27)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Chapter 27 — Critical infrastructure and sector security: verification

### Learning outcomes and connection

After this chapter you can (1) distinguish verification ("built right") from validation ("right thing built") for security controls; (2) design a test that could show a control does *not* work; (3) evaluate a detector with precision and recall and choose a threshold with explicit trade-offs; and (4) report verification results with their conditions and limits. It builds on Chapters 8, 12, 15 and 24 and prepares Chapter 29 (operations) and Laboratory II (Chapter 30).

### 27.1 Verification and validation

**Verification** checks that a control does what its specification says: the firewall blocks port 3389 from corporate to control; the setpoint validator rejects NaN. **Validation** checks that the control achieves its purpose in the real setting: corporate users cannot reach control systems by *any* path; operators cannot send unsafe setpoints. A control can pass verification and fail validation (the firewall rule works, but a dual-homed engineering laptop bypasses it). Good verification is **falsifiable**: it is designed so that a broken control would fail the test. A test that would pass whether or not the control works proves nothing.

### 27.2 Kinds of test

**Configuration review** compares settings with a baseline. **Functional tests** exercise the control with expected and forbidden inputs (Chapter 8's boundary tests). **Flow tests** confirm that disallowed paths are blocked (Chapter 7, under authorisation). **Restore drills** verify recovery controls end to end (Chapter 15). **Detection tests** replay labelled synthetic or benign-but-suspicious activity to see whether monitoring alerts. In OT, testing on the live process is restricted; use test benches, offline replicas or planned windows agreed with operations.

For CW's corporate-to-control rule, a flow test from an authorised corporate host to control addresses in a planned window is functional; a configuration review alone is not.

### 27.3 Evaluating detectors

A detector produces scores; a threshold turns them into alerts. Compare alerts with ground truth labels: **true positives** (TP), **false positives** (FP), **false negatives** (FN). **Precision** = TP/(TP+FP): of the alerts, how many were real? **Recall** = TP/(TP+FN): of the real events, how many were caught? Raising the threshold usually increases precision and decreases recall. With rare malicious events (Chapter 12's base rate), precision can be poor even with excellent per-event error rates. Choose a threshold by asking what each miss and each false alarm costs the service — and remember that labelled evaluation data seldom matches live conditions ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)).

### 27.4 Worked example and Lab 10 (synthetic)

**This case is synthetic.** Calder Mutual evaluates an anomaly detector on 5,025 labelled events, 25 of them malicious (seed 10).

```python
# Lab 10 - detection evaluation on a labelled synthetic event set (offline)
import random
random.seed(10)
events = []  # (score from a detector, truly malicious?)
for _ in range(5000):
    events.append((random.gauss(0.30, 0.12), False))
for _ in range(25):
    events.append((random.gauss(0.70, 0.15), True))
for thr in (0.5, 0.6, 0.7):
    tp = sum(1 for s, m in events if s >= thr and m)
    fp = sum(1 for s, m in events if s >= thr and not m)
    fn = sum(1 for s, m in events if s < thr and m)
    prec = tp / (tp + fp) if tp + fp else 0
    print(f"threshold {thr}: TP={tp:2} FP={fp:3} FN={fn:2} precision={prec:.2f} recall={tp/(tp+fn):.2f}")
```

Expected output:

```text
threshold 0.5: TP=23 FP=215 FN= 2 precision=0.10 recall=0.92
threshold 0.6: TP=20 FP= 36 FN= 5 precision=0.36 recall=0.80
threshold 0.7: TP=18 FP=  2 FN= 7 precision=0.90 recall=0.72
```

At 0.5 the team catches 23 of 25 but wades through 215 false alerts; at 0.7 nearly every alert is real but 7 attacks are missed. Neither is "correct". A defensible choice might use 0.7 for paging the on-call analyst and 0.5 for a daily review queue — two thresholds for two costs. The report states the conditions: synthetic scores, one seed, 25 positives (so recall estimates are coarse — Chapter 37), and unknown similarity to live traffic.

### 27.5 Common errors and limits

- Tests that cannot fail.
- Reporting accuracy on imbalanced data (99.5% "accuracy" by never alerting here).
- Choosing thresholds without stating costs.
- Evaluating on data that resembles training data more than reality.
- Verifying in a lab and claiming validation in production.

Lab 10 shows the second error numerically: never alerting scores 99.5 % accuracy. Choosing 0.5 or 0.7 without saying what a missed attack or an extra 215 false alerts cost is the third. A firewall rule tested only from the lab replica is the fifth. A test that would report "blocked" because the test host was switched off is the first.

### Exercises — chapter 27

**EX053 — Make it falsifiable.** *Objective:* design a meaningful test. *Inputs:* claim "the CW firewall prevents corporate users from reaching the control zone". *Steps:* design a verification test and a validation test, each with a result that would show the claim false, and the authorisation needed. *Expected evidence:* two test designs. *Rubric:* 3 = rule-level test from a corporate host to control addresses on all ports in a planned window, plus validation looking for alternative paths (dual-homed hosts, remote access, wireless) via configuration and flow review; authorisation stated; 2 = one test; 1 = non-falsifiable; 0 = none.

**EX054 — Accuracy trap.** *Objective:* see why accuracy misleads. *Inputs:* Lab 10. *Steps:* compute accuracy for threshold 0.7 and for a detector that never alerts; explain why both look "excellent". *Expected evidence:* two numbers and explanation. *Rubric:* 3 = (5025−2−7)/5025 ≈ 0.9982 and 5000/5025 ≈ 0.9950; explains class imbalance and recommends precision/recall; 2 = numbers only; 1 = one number; 0 = none.

### Chapter synthesis

Verification asks whether a control works as specified; validation asks whether it achieves its purpose. Design tests that could fail, evaluate detectors with precision and recall at thresholds chosen for stated costs, and report conditions and limits alongside the numbers.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Continue studying — chapter 27 of 40

[← Chapter 26](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 →](#ch-28)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Chapter 28 — Critical infrastructure and sector security: failure analysis

### Learning outcomes and connection

After this chapter you can (1) build a simple fault tree with AND and OR gates and compute the top-event probability under independence; (2) carry out a failure modes and effects analysis (FMEA) for a small system; (3) add a cyber path to a safety analysis and see how it changes the result; and (4) conduct a blameless post-incident review that looks for system causes. It builds on Chapters 12, 21, 22 and 26 and prepares Chapter 29 (operations) and Chapter 31 (advanced cases).

### 28.1 Fault trees

A **fault tree** starts from an undesired **top event** and decomposes it into causes connected by **gates**. An **AND** gate means all inputs must occur; an **OR** gate means any one suffices. With independent basic events, AND multiplies probabilities and OR combines them as $1 - \prod (1 - p_i)$. Fault trees make assumptions explicit and show which basic events dominate. They are traditionally built for random failures; security analysis adds paths where an adversary can make an event happen on purpose — and an adversary's "probability" is not a property of hardware.

### 28.2 FMEA

**Failure modes and effects analysis** works bottom-up: for each component, list ways it can fail (fails to start, fails open, gives false reading), the effect on the system, how it would be detected, and existing controls; then rank. FMEA finds single-component problems well and interactions poorly, which is why it pairs with STPA (Chapter 26) and fault trees.

EX056 applies FMEA to CW's dosing pump and analyser.

A row for CW's dosing pump reads: component dosing pump; mode runs at maximum rate; effect over-chlorination at the outlet; detection outlet residual analyser alarm; existing control hard-wired maximum pump rate.

### 28.3 Worked example and Lab 11 (synthetic)

**This case is synthetic.** Top event at CVH: "hospital loses mains-quality power to critical loads". Physically, this needs a grid outage AND failure of the backup (generator fails to start OR fuel contaminated OR automatic transfer switch fails). Separately, the hospital's BMS can command the essential-supply panel; a compromise of the BMS could shed critical loads regardless of the grid.

```python
# Lab 11 - a small fault tree for "hospital loses mains-quality power" (synthetic annual probabilities)
P = {"grid": 0.05, "gen_fails_start": 0.02, "fuel_contaminated": 0.005, "ats_fails": 0.01, "cyber_bms": 0.002}
# top = grid AND (backup fails); backup fails = gen_fails_start OR fuel_contaminated OR ats_fails
# separately: a compromised building-management system can shed critical loads whatever the grid state
backup_fails = 1 - (1 - P["gen_fails_start"]) * (1 - P["fuel_contaminated"]) * (1 - P["ats_fails"])
top_physical = P["grid"] * backup_fails
top = 1 - (1 - top_physical) * (1 - P["cyber_bms"])
print(f"P(backup fails on demand) = {backup_fails:.5f}")
print(f"P(top) physical only = {top_physical:.6f}")
print(f"P(top) with BMS path  = {top:.6f}")
print(f"share from cyber path ~ {P['cyber_bms'] / top:.0%}")
```

Expected output:

```text
P(backup fails on demand) = 0.03465
P(top) physical only = 0.001733
P(top) with BMS path  = 0.003729
share from cyber path ~ 54%
```

Under these synthetic numbers the physical design is good: two independent failures are needed. The cyber path is a single event that bypasses the AND gate and roughly doubles the top-event probability. The deeper point does not depend on the 0.002 estimate: an attacker does not fail at random, so a path that needs only one "event" under adversary control can dominate whatever number you write. The engineering response is to restore the AND structure — make critical loads impossible to shed from the BMS (a hard-wired inhibit, or BMS control limited to non-critical panels) — rather than only to lower the estimated probability.

### 28.4 Blameless post-incident review

When failures happen, a **blameless review** asks how the system allowed a reasonable person's action to cause harm, not who to punish. Reason's model of organisational accidents describes defences as layers with holes that occasionally align ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). Ask: what did people know at the time; what made their action seem right; which defences were absent or bypassed; what will we change in the system? Blame suppresses reporting, and unreported near-misses are lost evidence.

In the Lab 11 case, a blameless review of a lost-power event would ask why the BMS could shed critical loads at all.

### 28.5 Common errors and limits

- Multiplying probabilities of events with common causes (Chapter 12).
- Treating adversary actions as random failures.
- FMEA without interactions; fault trees without the human.
- Reviews that end with "human error" and retraining.

Lab 11 assumes independence of generator failure and fuel contamination; EX024 shows how a shared fuel tank breaks that. The BMS path is the second error made explicit: 0.002 is not a property of the BMS. The third appears if an FMEA of the generator ignores the operator who must start it manually. A review ending "estates engineer error; retrain" is the fourth.

### Exercises — chapter 28

**EX055 — Restore the AND gate.** *Objective:* see the effect of an engineering fix. *Inputs:* Lab 11. *Steps:* model a fix where the BMS can shed critical loads only if a grid outage is also present (i.e. the cyber path joins the grid AND gate as an extra backup-failure cause). Compute the new top-event probability. *Expected evidence:* modified code and value. *Rubric:* 3 = backup fails = 1−(0.98)(0.995)(0.99)(0.998) ≈ 0.03658, top ≈ 0.001829, with comment that the cyber path now needs a coincident grid outage; 2 = approach right, arithmetic slip; 1 = unchanged structure; 0 = none.

**EX056 — FMEA rows.** *Objective:* apply bottom-up analysis. *Inputs:* CW chlorine-dosing pump and its residual analyser. *Steps:* write four FMEA rows (component, failure mode, effect, detection, existing control). *Expected evidence:* table. *Rubric:* 3 = realistic modes (pump runs at max, pump stops, analyser reads low, analyser frozen) with effects on water safety and credible detections; 2 = three; 1 = vague; 0 = none.

### Chapter synthesis

Fault trees and FMEA make failure assumptions explicit, top-down and bottom-up. Adding cyber paths reveals single events that bypass designed redundancy; the strongest response restores structural independence rather than tuning an estimate. When failures happen, review the system, not the person.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Continue studying — chapter 28 of 40

[← Chapter 27](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 →](#ch-29)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Chapter 29 — Critical infrastructure and sector security: operations

### Learning outcomes and connection

After this chapter you can (1) describe security operations for a critical-service operator — monitoring, triage, escalation, change and vulnerability management; (2) adapt incident response to operational technology, where keeping the process safe comes first; (3) measure operational performance with time-to-detect and time-to-recover using medians and percentiles; and (4) write a playbook step that respects both security and operations. It builds on Chapters 12, 15, 24, 27 and 28 and prepares Laboratory II (Chapter 30).

### 29.1 What security operations do

Day to day, a security operations function **monitors** (logs, network traffic, alerts), **triages** (is this real? how bad?), **escalates** (to whom, how fast), **coordinates change** (no surprise changes on OT systems), and **manages vulnerabilities** (Chapters 5, 9, 11). For a critical-service operator, the defining feature is the partnership with **operations**: control-room staff, engineers and clinicians know what normal looks like for the process, and they own the decisions that affect it. Security operations that do not talk to the control room will misread alerts and, worse, take actions that hurt the service.

### 29.2 Incident response in OT

NIST's incident-response recommendations, revised in 2025, place response within overall cybersecurity risk management and the CSF 2.0 functions ([SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). In OT the order of priorities shifts: **first keep the process safe** (which may mean moving to manual or local control), **then contain** (isolate affected IT or OT segments without cutting what the process needs), **then investigate and recover**. Disconnecting a compromised server is reflexive in IT; in OT the operator must first know what that server does — pulling the historian is harmless, pulling the only SCADA server may blind operators during a storm. Evidence must also be preserved: images of engineering workstations, controller configurations, network captures and the operator log. Playbooks are agreed in advance with operations, safety and, where personal data may be involved, data protection (Chapter 14).

### 29.3 Measuring operations

Common measures are **time to detect** (TTD: first malicious or faulty activity to detection) and **time to recover** (TTR: detection to restored service). Their distributions are skewed (Chapter 12): most incidents are handled quickly; a few take days. Report **median**, **90th percentile** and **sample size**, and inspect the outliers individually — the long tail is where lessons live. Beware of incentives: a TTD target can encourage logging the "detection" time generously.

Lab 12's 15 records show why: mean 27.2 hours, median 4.

Inspect the 240-hour detection individually; it was a slow credential misuse.

### 29.4 Worked example and Lab 12 (synthetic)

**This case is synthetic.** CRP members pooled 15 sanitised incident records from the last two years.

```python
# Lab 12 - time to detect and recover: mean, median and percentiles from synthetic tickets (offline)
import statistics as st
TTD_H = [0.5, 1, 1, 2, 2, 3, 3, 4, 6, 8, 12, 20, 36, 70, 240]   # hours from first malicious activity to detection
TTR_H = [2, 3, 3, 4, 5, 5, 6, 8, 8, 10, 12, 16, 24, 48, 96]
for name, xs in (("time to detect", TTD_H), ("time to recover", TTR_H)):
    q = st.quantiles(xs, n=10, method="inclusive")
    print(f"{name}: n={len(xs)} mean={st.mean(xs):.1f} median={st.median(xs):.1f} p90={q[8]:.1f} max={max(xs)}")
print("mean TTD without the 240 h outlier:", round(st.mean(TTD_H[:-1]), 1))
```

Expected output:

```text
time to detect: n=15 mean=27.2 median=4.0 p90=56.4 max=240
time to recover: n=15 mean=16.7 median=8.0 p90=38.4 max=96
mean TTD without the 240 h outlier: 12.0
```

The mean time to detect (27.2 h) describes no real incident: half were detected within 4 hours, and one took ten days. Removing that single record cuts the mean by more than half. The useful report says: "median 4 h, 90th percentile about 56 h, n = 15; the 240-hour case was a slow credential misuse found during an access review" — and then asks why monitoring missed it. Percentiles on 15 records are rough; the method of computing them should be stated (here, the "inclusive" method of Python's `statistics.quantiles`).

### 29.5 A playbook step (synthetic)

*CPN playbook, step 3 — suspected compromise of an engineering workstation:* (1) Security analyst informs the control-room supervisor; supervisor confirms no switching operation depends on the workstation now. (2) Supervisor authorises isolation; analyst isolates the workstation's network port, leaving it powered (to preserve memory). (3) Engineer checks controller configurations the workstation could have changed, comparing with the last known-good backup. (4) Analyst records times, decisions and authorisers in the incident log. Each step names who decides and why the order matters.

Without step (1), isolation could interrupt a switching operation.

### 29.6 Common errors and limits

- Security teams acting on OT without operations' authorisation.
- Pulling power or wiping systems before evidence is preserved.
- Reporting mean times for skewed data.
- Playbooks that exist only on the systems the incident has disabled.

The CPN playbook avoids the first two by having the supervisor authorise isolation and leaving the workstation powered. Lab 12 shows the third. The fourth is why CRP members keep printed copies of playbooks in each control room, since an incident may disable the document system that holds them.

### Exercises — chapter 29

**EX057 — Report the tail.** *Objective:* summarise skewed data honestly. *Inputs:* Lab 12. *Steps:* write a 100-word summary for the CRP board of TTD and TTR, including sample size, one limitation and one question about the longest case. *Expected evidence:* the summary. *Rubric:* 3 = medians and p90 with n, mean's distortion noted, limitation (small, sanitised, self-reported detection times), pointed question; 2 = numbers without caveat; 1 = means only; 0 = none.

**EX058 — Safe containment.** *Objective:* order actions in OT response. *Inputs:* ransomware detected on CW's historian server in the control zone; SCADA servers appear unaffected. *Steps:* write the first five actions in order with who decides each. *Expected evidence:* ordered list. *Rubric:* 3 = confirm process state with operations; prepare manual/local operation; isolate historian from control zone with operations' approval; preserve evidence; check SCADA and controllers against known-good, with roles named; 2 = sensible but unordered or roles missing; 1 = IT-style "shut everything down"; 0 = none.

### Chapter synthesis

Security operations in critical services work hand in hand with operations: keep the process safe first, contain without blinding operators, preserve evidence and recover. Measure with medians, percentiles and sample sizes, and investigate the outliers that averages hide.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Continue studying — chapter 29 of 40

[← Chapter 28](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 →](#ch-30)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes and connection

After this laboratory you can (1) run a contained, two-part exercise — a facilitated tabletop and an offline evidence analysis — for a cross-sector scenario; (2) reconstruct a timeline from synthetic logs and verify log integrity; (3) evaluate decisions against plans and measures; and (4) write an after-action report with an improvement plan. It integrates Chapters 17, 21, 22, 26, 27 and 29 and is the second project checkpoint.

### 30.1 Scenario (synthetic)

**This scenario is synthetic.** At 02:10 on a winter night, Calder Water's control room reports that pump station PS2's level setpoint changed from 4.1 m to 2.0 m at 01:52. Nobody admits to the change. At 02:30, CPN reports a fault on Substation North that will take 6 hours to repair. The CEDC duty manager asks whether hospital water supply is at risk. Teams of four play CW operations, CW security, CPN control and CVH estates; a facilitator delivers injects.

The scenario combines two events that each operator could handle alone.

### 30.2 Part A — tabletop (90 minutes)

Objectives: (1) decide within 20 minutes whether to move PS2 to local control; (2) produce a consolidated cross-operator status for CEDC by 03:00; (3) decide what evidence to preserve. Injects: 02:40 — CW security finds a vendor remote session was active 01:45–01:58; 02:55 — CVH estates reports 72 h generator fuel but asks about water; 03:20 — a local journalist calls CW. Observers record decision times, who decided and on what evidence.

Observers should note the minute each decision was made, by whom and on what evidence, so the after-action report can compare times with the objectives. The 20-minute objective for PS2 starts at 02:10.

### 30.3 Part B — evidence analysis (offline)

Using Lab 8's hash-chain function, teams receive three files: the operator log, the anchored head from the separate anchor server, and the vendor-session record. They recompute the chain, find which entry (if any) was altered, and align it with the session times. Using Lab 9's autonomy model (Chapter 22) with the 6-hour outage, they state which services are lost and when, and whether hospital water depends on PS2. Every result must be reproducible: script hash, Python version, output.

Lab 9 gives 10 hours of treated storage.

### 30.4 Worked example: the timeline and its limits (synthetic)

| Time | Event | Source | Confidence |
|---|---|---|---|
| 01:45 | Vendor remote session opens | Remote-access record | High (system record) |
| 01:52 | PS2 setpoint 4.1 → 2.0 m | Operator log entry 2 | Medium — chain recomputation shows entry 2 does not match the anchored head, so the log was altered after the fact |
| 01:58 | Vendor session closes | Remote-access record | High |
| 02:10 | Operators notice | Shift log | High |
| 02:30 | Substation North fault (6 h) | CPN control | High |

Interpretation: the setpoint change coincides with the vendor session, and the log entry recording it was altered — consistent with a malicious or careless change hidden afterwards, but not proof of who did it. Cross-sector: with a 6-hour grid outage CW's pumps stop at once and treated storage (10 h) carries supply (Lab 9); a lowered setpoint means less stored water than planned, shortening that autonomy — the dangerous interaction is between two individually manageable events. Decisions: move PS2 to local control and restore the setpoint (operations), suspend vendor remote access (security, with CW director), preserve the vendor session record, the log server image and the anchor (security), inform CEDC and CVH with an estimated water autonomy range (operations, by 03:00), and refer media to the agreed spokesperson.

### 30.5 After-action report

Structure: objectives and whether met (with times); what went well; what did not; root causes (systemic, blameless — Chapter 28); improvement actions with owners and dates; evidence appendix. Distinguish **exercise artefacts** (things that happened only because it was an exercise) from real findings.

In this scenario, the journalist call at 03:20 tests a real procedure; a facilitator's late inject is an exercise artefact. Improvement actions follow from root causes, such as unmanaged vendor remote access, not from individual errors.

Each action needs a verification step, as EX060 asks.

### 30.6 Assessment rubric

| Criterion | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| Decisions | Timely, owned, evidence-based | Timely or evidence-based | Late or unowned | None |
| Timeline | Sourced, confidence graded, integrity checked | Sourced | Unsourced | None |
| Cross-sector reasoning | Interaction identified and quantified | Identified | Single-sector | None |
| Report | Actions owned and dated; artefacts separated | Actions vague | Narrative only | None |

A team that restores the setpoint quickly but cannot say who decided scores 2 for decisions. A timeline whose 01:52 row is marked high confidence despite the altered log entry scores 1. Cross-sector reasoning earns 3 only if the shortened water autonomy is estimated, not just mentioned.

### Exercises — chapter 30

**EX059 — Confidence grading.** *Objective:* justify evidence weights. *Inputs:* the worked timeline in this laboratory. *Steps:* explain the confidence of each row and what additional evidence would raise the 01:52 row to high. *Expected evidence:* explanations. *Rubric:* 3 = system records high; altered log entry medium because the time and value of the original entry are unknown; raising it needs PLC/controller event logs, historian trend of the setpoint, vendor-side session recording; 2 = partial; 1 = assertions; 0 = none.

**EX060 — Improvement plan.** *Objective:* turn findings into actions. *Inputs:* the scenario. *Steps:* write five improvement actions with owner, date and how completion will be verified. *Expected evidence:* table. *Rubric:* 3 = e.g. per-session vendor approval and recording, setpoint change alarms with limits, anchor on separate team's system, cross-operator status template, joint exercise with CPN; each verifiable; 2 = actions without verification; 1 = vague; 0 = none.

### Chapter synthesis

Laboratory II combines people and evidence: decide under time pressure, reconstruct timelines from sources of graded confidence, verify integrity and reason across sectors. The most dangerous situations often arise from the interaction of two individually manageable events.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Continue studying — chapter 30 of 40

[← Chapter 29](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 →](#ch-31)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-31"></a>

## Chapter 31 — Critical infrastructure and sector security: advanced cases

### Learning outcomes and connection

After this chapter you can (1) analyse cases where harm came through the physical process, safety systems or shared suppliers rather than data theft; (2) compare cases systematically on cause, path, consequence, detection and recovery; (3) reason about supply-chain and concentration risk across sectors; and (4) draw defensible, bounded lessons for an operator. It builds on Chapter 20 and Chapters 21–30, and prepares the comparative project (Chapter 34).

### 31.1 Beyond the headline

Advanced case analysis asks not "what happened?" but "which assumption failed, and is that assumption present here?" Three families of cases illustrate assumptions that critical services rely on.

**Process manipulation designed to stay hidden.** Langner's analysis of Stuxnet describes malware that manipulated industrial controllers driving centrifuges while presenting normal-looking values to operators ([Langner, 2011](https://doi.org/10.1109/MSP.2011.67)). *Failed assumption:* what the operator sees is what the process does. *Transferable lesson:* independent measurement paths for critical variables, and physical limits that do not depend on the controller.

**Attacks on the safety layer.** The TRITON/HatMan analysis describes malware targeting a safety instrumented system controller ([CISA MAR-17-352-01](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)). *Failed assumption:* the safety system is independent of the networks an attacker can reach. *Lesson:* physically enforce SIS programming modes (key switches), separate SIS networks and treat SIS engineering workstations as the most sensitive assets.

**Shared dependency failure.** The July 2024 faulty security update that crashed about 8.5 million Windows devices ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)) and the 2021 precautionary shutdown after ransomware on a pipeline company's IT network ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)) show harm arriving through dependencies rather than the control system. *Failed assumption:* our risk is bounded by our own systems. *Lesson:* map concentration (many services relying on one product, vendor or cloud region), stage updates, and plan degraded operation that does not need business IT.

### 31.2 Supply chains

Every operator runs software and hardware built by others, often through long chains of components. Public measures include **software bills of materials** listing components ([CISA SBOM](https://www.cisa.gov/sbom)), frameworks for build integrity such as SLSA ([SLSA](https://slsa.dev/)), secure development practices for suppliers ([NIST SSDF, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)) and "secure by design" expectations on manufacturers ([CISA Secure by Design](https://www.cisa.gov/securebydesign)). At bachelor's level, the operator's levers are mainly contractual and architectural: require SBOMs and vulnerability disclosure, test updates before deployment, stage rollouts, keep the ability to roll back, and avoid letting one supplier's failure stop several critical functions at once.

### 31.3 A comparison frame

| Dimension | Stuxnet (as analysed) | TRITON/HatMan | 2024 update outage |
|---|---|---|---|
| Cause | Deliberate, targeted | Deliberate, targeted | Accidental |
| Path | Into controllers | Into safety controller | Through a shared product |
| Consequence | Physical damage hidden from view | Potential loss of protection | Mass loss of availability |
| Failed assumption | View = reality | SIS independence | Risk bounded by own systems |
| Generic control | Independent measurement, physical limits | Physical SIS controls, segregation | Staged updates, concentration mapping, degraded modes |

Read the "Failed assumption" row first; it is the transferable part. Each generic control addresses that assumption rather than the specific technique.

### 31.4 Worked example: concentration at Calder (synthetic)

**This case is synthetic.** The CRP surveys its members: CVH, CEDC and Calder Mutual all use the same endpoint-security product, configured for automatic updates; CEDC and CT use the same CAD/scheduling cloud region; CW and CPN use the same OT integrator with remote access to both. Single events that could hit several sectors at once: a faulty endpoint update (hospital, dispatch, bank simultaneously); a cloud-region outage (dispatch and transit); a compromise of the integrator (water and power). Recommendations: stagger endpoint updates (a small canary group first, critical dispatch consoles last); confirm CEDC's paper-and-radio fallback does not need the cloud; require per-session approval and separate credentials for the integrator at each operator, and include it in the joint exercise. The point is not that these suppliers are bad; it is that the county's risk is shared and must be analysed jointly.

### 31.5 Common errors and limits

- Drawing lessons from vivid but unsourced details.
- Treating targeted state operations as the typical threat for every operator.
- Ignoring accidental shared-dependency failures because no adversary is involved.
- Teaching techniques instead of failed assumptions.

The Calder concentration example avoids these: it uses no technique detail, treats an accidental endpoint update as seriously as an integrator compromise, and does not assume a state actor. Repeating unsourced claims about Stuxnet's origin would be the first error.

The fourth error would turn a TRITON lesson into a description of how to reach a safety controller.

### Exercises — chapter 31

**EX061 — Find the assumption.** *Objective:* abstract a case. *Inputs:* the Ukraine 2015 case (Chapter 20). *Steps:* state two assumptions that failed and one assumption that held and helped recovery, with source support. *Expected evidence:* three assumptions. *Rubric:* 3 = e.g. remote access/operator workstations were trustworthy (failed), call centres would remain reachable (failed), manual operation was possible (held), each tied to the CISA alert; 2 = two; 1 = one; 0 = none.

**EX062 — Concentration map.** *Objective:* identify shared dependencies. *Inputs:* the Calder concentration survey in this chapter's worked example. *Steps:* draw a bipartite map (suppliers ↔ operators), mark the supplier with the highest reach and propose one measure per supplier. *Expected evidence:* map and measures. *Rubric:* 3 = endpoint product reaches three operators across three sectors (highest), measures specific (staged updates, fallback independence, integrator controls); 2 = map without measures; 1 = list; 0 = none.

### Chapter synthesis

Advanced cases teach through failed assumptions: what operators see is real, safety systems are independent, risk is bounded by our own systems. Compare cases on cause, path, consequence and assumption; manage supply-chain and concentration risk jointly across operators; and turn lessons into generic controls rather than technique knowledge.

<!-- cyberabc:chapter-navigation:start ch-31 -->
### Continue studying — chapter 31 of 40

[← Chapter 30](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 →](#ch-32)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-32"></a>

## Chapter 32 — Critical infrastructure and sector security: interdisciplinary interfaces

### Learning outcomes and connection

After this chapter you can (1) explain how law and regulation, economics, safety engineering, human factors and public communication shape security decisions in critical services; (2) translate a technical finding for lawyers, finance officers, clinicians, engineers and the public; (3) recognise when a security problem is really an incentive or organisational problem; and (4) work across disciplines without overstepping your expertise. It builds on Chapters 10, 14, 19 and 28–31 and prepares the field practice (Chapter 36) and capstone.

### 32.1 Law and regulation

Critical services are regulated. Examples consulted for this book: the EU's NIS2 Directive sets risk-management and incident-reporting obligations for essential and important entities ([NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)); DORA sets ICT-risk requirements for financial entities ([DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)); in North America, NERC's Critical Infrastructure Protection standards apply to the bulk electric system ([NERC CIP](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx)); in the US water sector, America's Water Infrastructure Act of 2018 required risk and resilience assessments and emergency response plans from community water systems above a size threshold ([EPA, AWIA](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans)). As a security professional you need to know that such obligations exist, where to find the current text, and when to involve legal counsel — not to interpret them alone. Compliance is a floor: meeting a standard does not prove the service is resilient.

### 32.2 Economics and incentives

Much infrastructure is privately operated, but its failure harms people who are not its customers — an **externality**. Investments that protect against rare events compete with visible, near-term costs, and the benefit (an outage that did not happen) is invisible. Regulation, insurance, procurement requirements and public reporting are ways of changing incentives. Recognising an incentive problem prevents a common mistake: proposing a technically excellent control that no budget holder has a reason to fund. Chapter 1's expected-loss and worst-credible-event framing is the bridge to a finance audience.

### 32.3 Safety engineering and human factors

Safety engineers have long practice in analysing hazards, independent protection layers and management of change (Chapters 26 and 28). Security and safety can conflict — an account lockout that blocks an operator in an emergency; a patch that invalidates a safety certification — and must be reconciled jointly. Human-factors specialists study how people actually work: alarm floods, fatigue on night shifts, workarounds when procedures do not fit reality. Reason's work shows errors as consequences of system design ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)). A control that operators cannot use under stress will be bypassed (Saltzer and Schroeder's psychological acceptability).

### 32.4 Communication

Different audiences need different translations of the same finding. **Clinicians** need to know the effect on patient care and what to do differently. **Engineers** need the technical mechanism and constraints. **Finance** needs costs, avoided losses and options. **Lawyers** need facts, dates and obligations triggered. **The public** needs honest, timely information on the service and on what they should do — without details that help attackers. Agreed spokespeople and pre-approved message templates are part of incident preparation (Chapter 30's journalist inject).

The four messages in this chapter's worked example apply this.

### 32.5 Worked example: one finding, four audiences (synthetic)

**This case is synthetic.** Finding: CVH's theatre ventilation can be changed from the BMS, which is reachable from the corporate network with password-only authentication.

- *Theatre lead:* "A misuse of the building system could reduce theatre air changes. Until we fix it, estates will check ventilation readings at the start of each list and you should report any alarm immediately."
- *Estates engineer:* "BMS admin interface reachable from corporate VLAN; password-only. Proposal: allowlist to two estates workstations, MFA, hard-wired minimum airflow interlock."
- *Finance:* "Cost about £25,000 one-off; it addresses a scenario whose worst credible outcome is cancelled surgery for several days. Alternatives and their costs are attached."
- *Data protection and legal:* "No personal data involved; no reporting obligation triggered by the finding itself; we will reassess if exploitation is detected."

### 32.6 Common errors and limits

- Giving legal opinions without counsel.
- Proposing controls without a funding argument.
- Ignoring safety or clinical consequences of security controls.
- One message for all audiences.

The worked example avoids each: the legal message says what was checked and when it will be reassessed; the finance message gives a cost and its worst credible outcome; the theatre message names the clinical check; and four audiences receive four messages. A single technical email to all would have failed the theatre lead and finance.

### Exercises — chapter 32

**EX063 — Translate for the board.** *Objective:* communicate across disciplines. *Inputs:* the Lab 11 result (cyber path roughly doubles the probability of losing critical power in the synthetic model). *Steps:* write a 120-word note to CVH's board with the finding, the proposed engineering fix, the cost framing and the limits of the model. *Expected evidence:* note. *Rubric:* 3 = plain language, consequence for patients, fix restores independence, honest about synthetic numbers and adversary non-randomness; 2 = partial; 1 = jargon; 0 = none.

**EX064 — Safety–security conflict.** *Objective:* reconcile duties. *Inputs:* a policy to lock HMI accounts after five failed logins. *Steps:* explain the safety risk, and propose an alternative meeting the security purpose. *Expected evidence:* explanation and alternative. *Rubric:* 3 = operator locked out during an emergency; alternatives such as physical-access-controlled console with monitoring, rate limiting without lockout, alerting on failures, emergency override with audit; 2 = one; 1 = vague; 0 = none.

### Chapter synthesis

Security in critical services sits among law, economics, safety, human factors and communication. Know where obligations live and when to call counsel, recognise incentive problems, reconcile safety and security jointly, design for people under stress and translate each finding for the audience who must act on it.

<!-- cyberabc:chapter-navigation:start ch-32 -->
### Continue studying — chapter 32 of 40

[← Chapter 31](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 →](#ch-33)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes and connection

After this chapter you can (1) design interviews and document analysis as qualitative methods, including ethical approval and consent; (2) code qualitative data with a codebook and check agreement between coders; (3) make a quantitative analysis reproducible; and (4) combine qualitative and quantitative evidence in a mixed-methods design. It builds on Chapter 18 and prepares the comparative project (Chapter 34) and the capstone (Chapters 35–40).

### 33.1 Qualitative methods

Many important questions in critical-sector security are about people and organisations: why operators bypass a control, how incident decisions were made, what practitioners believe works. **Semi-structured interviews** follow a guide of open questions while allowing follow-up. **Document analysis** examines plans, reports and policies. Both require **ethical approval** from your institution when they involve people, **informed consent** (participants know the purpose, what will be recorded and how it will be stored, and can withdraw), and protection of participants and their organisations: no detail that identifies a person or exposes a vulnerability of a real operator should appear in your thesis. Interview notes about security weaknesses are sensitive data; store them encrypted and delete them on schedule (Chapter 14).

### 33.2 Coding and agreement

**Coding** assigns labels to passages: "fallback to paper", "vendor dependency", "unclear decision owner". A **codebook** defines each code with inclusion and exclusion rules and an example. To check **reliability**, two people code the same sample independently and measure agreement. Raw percentage agreement overstates reliability because some agreement happens by chance; **Cohen's kappa** corrects for this: $\kappa = (p_o - p_e)/(1 - p_e)$, where $p_o$ is observed agreement and $p_e$ the agreement expected by chance from each coder's label frequencies. Disagreements are not failures; discussing them sharpens the codebook.

### 33.3 Reproducible quantitative analysis

A reproducible analysis keeps raw data unchanged, does all transformations in scripts, records versions and random seeds, and produces every number in the report from code ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)). The labs in this book follow these rules: fixed seeds, standard library only, printed outputs reproduced in the text. If a simulation or model is used, state how it was checked against reality — verification and validation of simulation models is its own discipline ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)).

### 33.4 Mixed methods

Quantitative evidence says **how much**; qualitative evidence says **how and why**. A mixed-methods design might count, across 30 public incident reports, how many mention a fallback to manual operation (quantitative), then interview four operators about what makes manual fallback work (qualitative). The combination is stronger than either, provided each part is done properly and the integration — how one informs the other — is explicit.

State in advance how the parts connect.

In the 30-report example, the count tells you how often reports mention manual fallback, and the interviews explain why fallback sometimes fails, for example because staff have not practised it. Integration means the interview guide asks about the conditions the count revealed.

### 33.5 Worked example: coding incident reports (synthetic data)

**The data are synthetic.** Two students code 20 incident-report excerpts for the presence of the code "unclear decision owner". They agree on 16 of 20 ($p_o = 0.80$). Student A applied the code to 8 excerpts; student B to 6. Chance agreement: both "yes" $= (8/20)(6/20) = 0.12$; both "no" $= (12/20)(14/20) = 0.42$; $p_e = 0.54$. Kappa $= (0.80 - 0.54)/(1 - 0.54) = 0.26/0.46 \approx 0.57$ — moderate agreement. The students review the four disagreements, find that one coded "decision delayed" as "owner unclear" even when the owner was named, and tighten the definition: "applies only when the report states or shows that participants did not know who held the decision".

### 33.6 Common errors and limits

- Interviewing practitioners without ethics approval or consent.
- Publishing identifiable details of real operators' weaknesses.
- Reporting percentage agreement as reliability.
- Analysis steps done by hand and not recorded.
- "Mixed methods" that are two separate studies never integrated.

In the coding example, reporting 80 % agreement instead of kappa 0.57 would be the third error. Interviewing CRP engineers about remote access without consent and approval would be the first, and quoting a named operator's unpatched gateway would be the second. A spreadsheet edited by hand without a record would be the fourth.

### Exercises — chapter 33

**EX065 — Compute kappa.** *Objective:* measure reliability. *Inputs:* two coders, 40 excerpts, agree on 34; coder A applied the code 10 times, coder B 12 times. *Steps:* compute $p_o$, $p_e$ and $\kappa$, and interpret. *Expected evidence:* working and interpretation. *Rubric:* 3 = $p_o = 0.85$; $p_e = 0.25 \times 0.30 + 0.75 \times 0.70 = 0.075 + 0.525 = 0.60$; $\kappa = 0.625$, substantial-to-moderate agreement with a note that interpretation scales are conventions; 2 = arithmetic slip; 1 = $p_o$ only; 0 = none.

**EX066 — Consent and protection.** *Objective:* design ethical qualitative work. *Inputs:* plan to interview three CRP operators' engineers about remote-access practices. *Steps:* write the consent information (five points) and three data-protection measures. *Expected evidence:* lists. *Rubric:* 3 = purpose, voluntary participation/withdrawal, what is recorded, storage/retention, how results are anonymised, plus encryption, pseudonyms, no vulnerability details in outputs/host review; 2 = partial; 1 = generic; 0 = none.

### Chapter synthesis

Qualitative methods answer how and why; they need ethics approval, consent and protection of participants and organisations. Codebooks and kappa make coding reliable; scripts, seeds and versions make quantitative analysis reproducible; mixed methods are only as good as their integration.

<!-- cyberabc:chapter-navigation:start ch-33 -->
### Continue studying — chapter 33 of 40

[← Chapter 32](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 →](#ch-34)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes and connection

After this project you can (1) compare three or more options against explicit criteria with weights and evidence; (2) test how sensitive the ranking is to the weights; (3) present a comparison that a decision-maker can challenge; and (4) recognise when a weighted score hides a decisive consideration. It builds on Chapters 1, 15, 23 and 24 and prepares the capstone proposal (Chapter 35). It is the course's central expression of its outcome: compare methods, evaluate evidence and design defensible solutions.

### 34.1 Multi-criteria comparison

Decisions about critical services involve several criteria that do not share a unit: consequence reduction, operational burden, cost, time to implement, strength of evidence that the option works. **Multi-criteria decision analysis** scores each option on each criterion, weights the criteria, and combines them — most simply as a weighted sum. Its value lies less in the final number than in making the criteria, scores and weights visible so that people can argue about them productively.

Lab 13 shows this: the weights and scores are on the page and can be challenged.

### 34.2 Doing it honestly

Define each criterion so that higher is better (invert costs and burdens). Score on an anchored scale ("5 = removes the worst credible consequence; 1 = no measurable effect"). Record the evidence behind each score (Chapter 15). Set weights *before* scoring, ideally with stakeholders, to avoid tuning weights to a favourite. Then run **sensitivity analysis**: vary the weights and see whether the winner changes. If it changes only under implausible weights, the decision is robust; if small changes flip it, report that the decision depends on a value judgement and name it.

### 34.3 When a score is not enough

Some considerations are **constraints**, not criteria: a legal obligation, a safety requirement, a minimum service level. An option that violates a constraint is excluded, whatever its score. Others are **vetoes** by people with authority (a clinical director's refusal of an option that disrupts theatres). Handle these explicitly before scoring.

For CEDC, a regulator's four-hour restoration requirement is a constraint (EX068), excluding options that cannot demonstrate it.

A clinical director's veto of an option that closes theatres for a week is handled the same way.

### 34.4 Worked example and Lab 13 (synthetic)

**This case is synthetic.** The CRP compares three ransomware-resilience options for CEDC on four criteria with weights 0.4, 0.2, 0.2, 0.2.

```python
# Lab 13 - weighted comparison of three options and weight sensitivity (synthetic scores, offline)
CRITERIA = ["consequence reduction", "operational burden (inverted)", "cost (inverted)", "evidence strength"]
W = [0.4, 0.2, 0.2, 0.2]
SCORES = {  # 1-5, higher is better
    "network segmentation project": [5, 2, 2, 4],
    "managed detection service":    [3, 4, 3, 3],
    "offline backups + restore drills": [4, 4, 4, 5],
}
def total(s, w): return sum(a * b for a, b in zip(s, w))
for name, s in SCORES.items():
    print(f"{name:33} {total(s, W):.2f}")
print("weight on consequence needed for segmentation to win:")
for wc in (0.4, 0.5, 0.6, 0.7, 0.8):
    rest = (1 - wc) / 3
    w = [wc, rest, rest, rest]
    best = max(SCORES, key=lambda k: total(SCORES[k], w))
    print(f"  w_consequence={wc:.1f} -> {best}")
```

Expected output:

```text
network segmentation project      3.60
managed detection service         3.20
offline backups + restore drills  4.20
weight on consequence needed for segmentation to win:
  w_consequence=0.4 -> offline backups + restore drills
  w_consequence=0.5 -> offline backups + restore drills
  w_consequence=0.6 -> offline backups + restore drills
  w_consequence=0.7 -> network segmentation project
  w_consequence=0.8 -> network segmentation project
```

Backups with restore drills win under the agreed weights and remain ahead until consequence reduction carries between 0.6 and 0.7 of the total weight. The report therefore says: "Recommended: offline backups with restore drills. The recommendation reverses only if the partnership values consequence reduction at more than about two-thirds of the decision, in which case segmentation is preferred. The options are not exclusive; segmentation is the strongest second-year candidate." Note what the scores do not capture: backups recover from ransomware but do not prevent the data theft that often accompanies it — a consideration to state explicitly, not hide in a number.

### 34.5 Project deliverable

A 2,500-word comparative report on a question of your choice within the Calder case or a documented public topic (for example, three approaches to remote access, three backup strategies, three monitoring options): constraints, criteria with anchored scales, evidence per score, weights set in advance, sensitivity analysis, recommendation with reversal conditions, and limits.

Use Lab 13's structure for your sensitivity analysis and report the weight at which the winner changes.

State the reversal condition in words, as Lab 13's report does: the weight at which the recommendation would change and the value judgement that weight represents.

### 34.6 Common errors and limits

- Scoring first and choosing weights afterwards.
- Unanchored scores ("4 because it feels good").
- Ignoring constraints and vetoes.
- Presenting a weighted total as objective truth.
- Treating options as mutually exclusive when they can be combined.

Lab 13 avoids the first by fixing weights at 0.4, 0.2, 0.2, 0.2 before scoring. The report also notes that segmentation and backups can be combined, avoiding the fifth error. A score of 4 for evidence strength needs the drill records behind it; without them it is the second error.

Presenting 4.20 as proof would be the fourth.

### Exercises — chapter 34

**EX067 — Find the crossover.** *Objective:* locate the reversal point. *Inputs:* Lab 13. *Steps:* compute the exact consequence weight at which segmentation and backups tie, using the equal-split rule for the other weights. *Expected evidence:* derivation and value. *Rubric:* 3 = segmentation $5w + (2+2+4)(1-w)/3$, backups $4w + (4+4+5)(1-w)/3$; tie when $w = 5(1-w)/3$, so $w = 5/8 = 0.625$; 2 = numeric search to 0.62–0.63; 1 = range 0.6–0.7 only; 0 = none.

**EX068 — Add a constraint.** *Objective:* handle a non-compensatory requirement. *Inputs:* CEDC's regulator requires demonstrated restoration within 4 hours. *Steps:* explain how this changes the analysis and which evidence each option must provide. *Expected evidence:* explanation. *Rubric:* 3 = treated as constraint not criterion; only options that demonstrate restoration qualify (backups with drills directly; segmentation/detection do not restore, so need to be combined with a recovery capability); 2 = treated as heavy weight; 1 = ignored; 0 = none.

### Chapter synthesis

Comparison is the bachelor's core skill: explicit criteria, anchored scores, evidence, weights set in advance, sensitivity analysis and stated reversal conditions. Constraints and vetoes come before scoring, and a weighted total is a structured argument, not a verdict.

<!-- cyberabc:chapter-navigation:start ch-34 -->
### Continue studying — chapter 34 of 40

[← Chapter 33](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 →](#ch-35)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes and connection

After this chapter you can (1) choose a capstone topic that is comparative, feasible, ethical and useful; (2) write a proposal with question, context, method, evidence plan, ethics, risks and timeline; (3) define success criteria and deliverables in advance; and (4) obtain the authorisations your project needs. It builds on Chapters 18, 25, 30, 33 and 34 and starts the capstone sequence (Chapters 35–40).

### 35.1 What a bachelor's capstone is

The capstone demonstrates the course outcome: comparing theories and methods, evaluating evidence and designing a defensible solution for a critical-sector problem. It is neither an engineering build of a complete system (that is the engineering course) nor an original contribution to knowledge (that is the doctorate). A strong bachelor's capstone takes a **real decision problem** — often from a host organisation (Chapter 36) or a well-documented public topic — compares **at least three options or methods** with explicit criteria and evidence, and ends with a **recommendation and its limits**. Typical scale: about 400 hours of work over two semesters, a 10,000–12,000-word thesis and a presentation.

### 35.2 Choosing a topic

Test each candidate against five questions. **Comparative?** Are there real alternatives to compare? **Feasible?** Can you get the evidence in the time — documents, labs, authorised tests, interviews? **Ethical and authorised?** Does it need ethics approval, host permission, data-protection measures (Chapters 10, 14, 33)? **Useful?** Would someone act on the answer? **Bounded?** Can you say what is out of scope? Topics fail most often on feasibility: "evaluate the security of the national grid" is not a capstone; "compare three approaches to vendor remote access for a small distribution operator, using public guidance, a synthetic lab and two practitioner interviews" is.

### 35.3 The proposal

1. **Title and question** (Chapter 18): population, variables, time frame, answer type.
2. **Context and motivation**: the service, the decision, who needs it.
3. **Literature and sources**: what is known, with a recorded search strategy.
4. **Options and criteria** (Chapter 34): candidate options, constraints, criteria with anchored scales, how weights will be set.
5. **Method and evidence plan**: for each criterion, what evidence and how obtained (documents, lab measurements, authorised tests, interviews).
6. **Ethics and authorisation**: approvals needed, rules of engagement, data handling.
7. **Risks to the project**: access refused, data unavailable, scope creep — and fallbacks (e.g. synthetic data if host data is withdrawn).
8. **Success criteria and deliverables**: what will exist at the end and how it will be judged.
9. **Timeline**: milestones aligned with Chapters 36–40.

### 35.4 Worked example: a proposal outline (synthetic)

**This proposal is synthetic.** *Question:* "For a mid-sized hospital, which of three approaches to managing unsupported clinical devices — accelerated replacement, network isolation with monitoring, or vendor-managed secure gateways — best reduces exposure within a fixed annual budget, judged on consequence reduction, clinical disruption, cost and evidence strength?" *Context:* CVH (synthetic host) has unsupported imaging and laboratory devices (Lab 2). *Sources:* public guidance on medical-device and OT security, the NAO WannaCry report, sector performance goals. *Method:* a synthetic inventory of 120 devices built from published categories; a lab model of exposure under each option; two interviews with clinical engineers (ethics approval requested). *Ethics:* no real device data; interviews anonymised; host review of outputs. *Risks:* interviews refused → rely on documents and state the gap. *Success criteria:* comparison with sensitivity analysis and reversal conditions; recommendation defended at presentation. *Timeline:* proposal approved week 4; evidence collection weeks 5–14; analysis weeks 15–20; draft thesis week 24; presentation week 28.

### 35.5 Common errors and limits

- Topics that are descriptive only, with no comparison.
- Evidence plans that assume access you do not yet have.
- No fallback when a host withdraws.
- Success criteria written after the results.

The worked proposal avoids these: it compares three options, requests interviews but has a document fallback, and fixes success criteria before evidence collection.

Each error has a typical symptom. A topic such as "the state of hospital device security" produces a description with nothing to recommend. An evidence plan that assumes host data before the host has agreed collapses in week six. A project without a fallback stalls when an interviewee withdraws. Success criteria written after the results always look met, which is why the worked proposal fixes them in week four.

### Exercises — chapter 35

**EX069 — Topic triage.** *Objective:* apply the five tests. *Inputs:* three candidate topics: (a) "Is AI good for security?"; (b) "Compare three methods for detecting false sensor data in a water-tank model, using a synthetic dataset"; (c) "Test the firewall of my local water utility". *Steps:* apply the five questions to each and choose. *Expected evidence:* table and choice. *Rubric:* 3 = (a) not bounded or comparative as stated; (b) feasible, comparative, ethical; (c) unauthorised and unethical — reject; choose (b); 2 = right choice, weak reasoning; 1 = wrong choice; 0 = none.

**EX070 — Evidence plan.** *Objective:* connect criteria to evidence. *Inputs:* the worked proposal outline in this chapter. *Steps:* for each of the four criteria, state the evidence, its source and one threat to its validity. *Expected evidence:* four rows. *Rubric:* 3 = specific evidence (lab exposure model output, interview data on disruption, published costs, quality grading of sources) with matching validity threats; 2 = three; 1 = vague; 0 = none.

### Chapter synthesis

A bachelor's capstone answers a real decision problem by comparing options with evidence and ending in a bounded recommendation. A good proposal fixes the question, criteria, evidence plan, ethics, risks, success criteria and timeline before the work begins.

<!-- cyberabc:chapter-navigation:start ch-35 -->
### Continue studying — chapter 35 of 40

[← Chapter 34](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 →](#ch-36)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes and connection

After this chapter you can (1) prepare for a placement with a critical-service operator or a community organisation, including agreements on scope, confidentiality and supervision; (2) work safely and usefully in an operational environment as a learner; (3) keep a reflective practice log; and (4) produce outputs that serve the host without exposing it. It builds on Chapters 10, 14, 29, 32 and 35 and feeds evidence into the capstone.

### 36.1 Why practice matters

Critical services are learned on site: the smell of a pumping station, the rhythm of a control-room shift change, the way clinicians actually use devices. Field practice — a placement with an operator, a regulator or a security team, or community practice such as helping a small charity, school or clinic improve basic security — tests your knowledge against reality and gives your capstone grounded evidence. It also teaches the professional behaviours no lab can: listening first, asking before touching, and keeping confidences.

### 36.2 The placement agreement

Before starting, agree in writing with the host and your university: **supervisor** on site and academic supervisor; **activities** permitted (observation, document review, authorised tasks) and forbidden (any change to live systems without supervision; any testing without written RoE); **confidentiality** — what you may record, what you may take away, and that any coursework is reviewed by the host before submission; **data protection**; **health and safety** induction (OT sites have physical hazards); and what happens if you discover something serious (escalate to your site supervisor immediately, not to your classmates).

### 36.3 Working as a learner on site

Most of your value as a student comes from **fresh eyes and time**: documenting what experienced staff no longer notice, tidying an inventory, drafting a procedure, comparing current practice with public guidance. Do not judge before understanding — a "bad practice" may be a workaround for a real constraint (the shared control-room login of Chapter 13). Ask why. Record your observations factually, separate them from interpretation, and check them with the person concerned.

The week's log entry in this chapter shows this: the missing tickets were a slow tool at night, not carelessness.

### 36.4 Community practice

Small organisations that support communities — a food bank, a rural clinic, a volunteer ambulance service — often depend on critical services and have little security capacity. A structured, low-risk contribution: an asset list, account and backup review against a simple published baseline, a one-page incident contact sheet, and a short staff session. The same authorisation and confidentiality rules apply; your duty of care is higher, not lower, when the organisation cannot judge your advice.

Agree the contribution in writing with the organisation's lead.

### 36.5 Reflective log

Keep a weekly log with four headings: **what I did**, **what I observed**, **what surprised me and why**, **what I would do differently**. Reflection turns experience into learning and provides evidence for assessment. Keep the log sanitised from the start: no system names, addresses, credentials or personal data — write "the remote-access gateway" not its hostname.

Sanitising at writing time avoids a risky clean-up later.

Write the log the same week, while the details are accurate, and keep it separate from host documents.

### 36.6 Worked example: a week's log entry (synthetic)

**This entry is synthetic.** *Did:* shadowed CW's control room for two night shifts; helped reconcile the telemetry inventory with the site list. *Observed:* 7 of 42 outstations in the inventory had no recorded firmware version; operators phone the station technician when a reading looks wrong rather than raising a ticket. *Surprised:* the operators' informal checks catch sensor faults faster than the alarm system — but leave no record. *Differently:* I assumed the missing tickets were carelessness; the supervisor explained the ticketing tool is slow at night. Proposal for host: a two-field paper "sensor query" sheet transcribed each morning, so the knowledge becomes evidence. Approved by site supervisor for inclusion in coursework in sanitised form.

### 36.7 Common errors and limits

- Starting without a written agreement.
- Taking photographs, files or notes that the host has not approved.
- Judging practice before understanding constraints.
- Reflective logs that describe activity but not learning.

The CW log entry avoids all four: the placement had an agreement, the paper sheet proposal was approved before inclusion, the student asked why tickets were missing before judging, and the entry records a changed assumption. EX072 shows the second error in its most dangerous form: a recorded credential.

Ask your site supervisor which notes may leave the site.

### Exercises — chapter 36

**EX071 — Draft the agreement.** *Objective:* set up a safe placement. *Inputs:* a four-week placement with CEDC's IT team. *Steps:* write the agreement headings with one specific clause each. *Expected evidence:* the draft. *Rubric:* 3 = supervisors, permitted/forbidden activities (no access to live CAD changes), confidentiality and host review, data protection (call recordings excluded), safety, escalation path; 2 = generic clauses; 1 = missing key items; 0 = none.

**EX072 — Sanitise a log.** *Objective:* protect the host. *Inputs:* "Tuesday: logged into vpn.caldermutual.example as jsmith/Summer2026 to look at the SWIFT gateway 10.4.2.8; noticed it still runs version 7." *Steps:* rewrite so it is safe to submit and still useful. *Expected evidence:* rewritten entry and three things removed. *Rubric:* 3 = removes hostname, credentials, address, person and precise version, keeps the learning ("observed an outdated payment-gateway component; raised with supervisor"); also notes the credential should never have been recorded and must be reported for change; 2 = removes most; 1 = partial; 0 = none.

### Chapter synthesis

Field and community practice ground the course in reality. Agree scope, confidentiality, supervision and escalation in writing; contribute fresh eyes and time; understand constraints before judging; keep a sanitised reflective log; and let the host review anything that leaves the site.

<!-- cyberabc:chapter-navigation:start ch-36 -->
### Continue studying — chapter 36 of 40

[← Chapter 35](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 →](#ch-37)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes and connection

After this seminar you can (1) critically review a security study, report or vendor claim using a structured checklist; (2) quantify the uncertainty of small-sample results with confidence intervals; (3) give and receive peer review that improves work; and (4) decide how much weight a piece of evidence deserves in your capstone. It builds on Chapters 15, 18, 27 and 33 and prepares capstone implementation and evaluation (Chapters 38–39).

### 37.1 A review checklist

For any study, report or claim: **Question** — what exactly is claimed? **Data** — where did it come from, how much, how representative? **Method** — could it be repeated; was there a comparison or control? **Results** — are uncertainties reported; do numbers add up? **Validity** — construct, internal, external, reliability (Chapter 18)? **Interests** — who funded or produced it, and what would they prefer to find? **Limits** — does the work state them, and are its conclusions within them? In security, common weaknesses include evaluation on unrealistic data, base-rate neglect, and results that do not transfer to live environments ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp); [Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)). In time-series anomaly detection, Kim and colleagues showed that a popular evaluation protocol can make even random scores look strong ([Kim et al., 2022](https://ojs.aaai.org/index.php/AAAI/article/view/20680)).

### 37.2 Small samples and intervals

Critical-service evidence often comes from few observations: five restore drills, twenty exercises, a dozen incidents. A point estimate ("85% of drills met the objective") hides how uncertain it is. A **confidence interval** gives a range of plausible values. Two common approaches for a proportion: the **bootstrap**, which resamples the observed data many times ([Efron, 1979](https://doi.org/10.1214/aos/1176344552)), and the **Wilson score interval**, a formula that behaves well for small samples and proportions near 0 or 1 ([Wilson, 1927](https://doi.org/10.1080/01621459.1927.10502953)). The bootstrap is general but behaves poorly at small sizes and near boundaries — it can never produce a value above the maximum observed, so with 4 of 5 successes it may suggest an upper bound of 100%.

### 37.3 Worked example and Lab 14 (synthetic)

**This case is synthetic.** CEDC ran 20 restore drills; 17 met the 4-hour objective. A smaller operator ran 5; 4 met it.

```python
# Lab 14 - bootstrap confidence interval for a restore-drill success rate (synthetic, seed 14, offline)
import random
random.seed(14)
drills = [1] * 17 + [0] * 3          # 20 restore drills, 17 met the 4-hour objective
obs = sum(drills) / len(drills)
boots = sorted(sum(random.choice(drills) for _ in drills) / len(drills) for _ in range(10_000))
lo, hi = boots[249], boots[9749]
print(f"observed success = {obs:.2f}; 95% bootstrap interval = [{lo:.2f}, {hi:.2f}]")
small = [1, 1, 1, 0, 1]
boots = sorted(sum(random.choice(small) for _ in small) / len(small) for _ in range(10_000))
print(f"with only 5 drills (4 met): [{boots[249]:.2f}, {boots[9749]:.2f}]")
from math import sqrt
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z * sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
print("Wilson 95%% for 17/20: [%.2f, %.2f]; for 4/5: [%.2f, %.2f]" % (*wilson(17, 20), *wilson(4, 5)))
```

Expected output:

```text
observed success = 0.85; 95% bootstrap interval = [0.70, 1.00]
with only 5 drills (4 met): [0.40, 1.00]
Wilson 95% for 17/20: [0.64, 0.95]; for 4/5: [0.38, 0.96]
```

Both methods say the same thing in substance: 17 of 20 is consistent with a true success rate anywhere from about two-thirds to about 95%; 4 of 5 is consistent with anything from under 40% to nearly always. The bootstrap's upper bound of 1.00 is an artefact of resampling data that contains no value above 1; the Wilson interval is the better choice here. For the board, the message is: "we have good but not conclusive evidence that restores usually meet four hours; one in four failing would not surprise us". Five drills cannot support a claim of reliability.

### 37.4 Peer review

Seminar groups exchange capstone evidence chapters. A useful review states what the work claims, what is convincing, the two or three most important problems (each with a suggested fix), and minor points. Review the work, not the person; be specific ("the restore-time claim rests on one drill in a test environment; can you add the drill's conditions and an interval?"). Authors respond point by point: accepted and changed, or declined with reasons.

A good response quotes each point and states the change made or the reason declined.

### 37.5 Common errors and limits

- Reporting a proportion without its sample size or interval.
- Treating vendor benchmarks as independent evidence.
- Reviews that only praise or only attack.
- Ignoring how evaluation protocols can inflate results.

Lab 14 shows the first: "85 %" without "of 20" and an interval hides that the true rate may be 64 %. A detector vendor's own benchmark (EX074) is the second. A review that says only "great work" helps nobody. The fourth is Kim and colleagues' point about evaluation protocols.

Each review point should name the evidence it questions.

### Exercises — chapter 37

**EX073 — How many drills?** *Objective:* relate sample size to precision. *Inputs:* the Wilson function from Lab 14. *Steps:* compute the Wilson 95% interval for 34/40 and 85/100 and comment on how evidence accumulates. *Expected evidence:* two intervals and a comment. *Rubric:* 3 = approximately [0.71, 0.93] and [0.77, 0.91], width shrinking roughly with the square root of n; recommends a drill programme; 2 = intervals only; 1 = one; 0 = none.

**EX074 — Review a claim.** *Objective:* apply the checklist. *Inputs:* a vendor brochure (synthetic): "Our OT anomaly detector achieved 99.7% accuracy on a public water-testbed dataset." *Steps:* apply the checklist and list four questions to ask the vendor. *Expected evidence:* review and questions. *Rubric:* 3 = accuracy misleading under imbalance (Chapter 27), testbed realism and transfer, evaluation protocol, interests; questions on precision/recall at operating threshold, live deployment results, false alarms per day, independent evaluation; 2 = partial; 1 = generic; 0 = none.

### Chapter synthesis

Evidence review is structured scepticism: question, data, method, results, validity, interests and limits. Report small-sample results with intervals — Wilson for proportions — and let peer review improve work by being specific, prioritised and respectful.

<!-- cyberabc:chapter-navigation:start ch-37 -->
### Continue studying — chapter 37 of 40

[← Chapter 36](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 →](#ch-38)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes and connection

After this chapter you can (1) execute a capstone plan while controlling scope and recording decisions; (2) collect and manage evidence so that every result traces to its source; (3) build a small, reproducible model or lab that supports your comparison; and (4) handle setbacks — lost access, surprising results — honestly. It builds on Chapters 25, 30, 34, 35 and 37 and prepares the evaluation (Chapter 39).

### 38.1 Working to a plan

Implementation turns the proposal (Chapter 35) into evidence. Keep three living documents. A **project log** (date, what you did, what you decided and why). An **evidence register** (item, source, date, type, how obtained, where stored, which criterion it supports — Chapter 15). A **change record** for any departure from the proposal, with your supervisor's agreement. Scope creep is the commonest capstone failure: new questions are interesting, but each must either replace something or wait for "future work".

In the week-14 checkpoint, the declined interview is recorded as a change with supervisor approval.

### 38.2 Building the supporting model

Most bachelor capstones need a small artefact: an exposure model, a dependency simulation, a detector comparison, a coded dataset. Build it with the habits of the labs: standard tools, fixed seeds, scripts not manual steps, outputs saved with the script hash, and **tests** that check the model on cases with known answers before you trust it on new ones (Chapter 8). Document what the model leaves out. A model that reproduces a hand-calculated simple case and states its assumptions is worth more than an elaborate one nobody can check.

### 38.3 Collecting evidence from people and hosts

Interviews follow the approved protocol and consent (Chapter 33). Host documents are handled under the placement agreement (Chapter 36). Anything about a real operator's vulnerabilities is held securely and appears in the thesis only in sanitised, host-approved form. If access is withdrawn, use the fallback in your proposal and record the change; do not quietly substitute guesses for data.

Record each item in the evidence register when it arrives.

For the unsupported-devices capstone, interview notes are pseudonymised on the day, stored encrypted, and deleted on the schedule in the consent form. If the host withdraws its device list, the proposal's synthetic inventory replaces it, and the change record says so.

### 38.4 Surprising and negative results

Results that contradict your expectation are evidence too. If restore drills in your lab model show that the option you expected to win cannot meet the objective, report it and investigate why — perhaps a dependency you had not modelled. Do not adjust parameters until the result "looks right"; if you change a parameter, record why and show both results. Honest negative findings are among the most useful outputs a capstone can produce for a host.

The gateway finding in the week-14 checkpoint is a worked example.

### 38.5 Worked example: an implementation checkpoint (synthetic)

**This checkpoint is synthetic.** Week 14 of the unsupported-devices capstone (Chapter 35). *Done:* synthetic inventory of 120 devices built from published categories (script `make_inventory.py`, seed 38, hash recorded); exposure model for three options with tests reproducing a hand-worked 5-device case; one interview completed, one declined. *Changed:* the second interview is replaced by a document review of two public guidance sources (change record approved by supervisor; validity note: practitioner perspective now rests on one interview). *Surprise:* the vendor-gateway option reduced exposure least for imaging devices, because those devices also accept connections from the image archive, which the gateway does not mediate. Instead of treating this as an error, the student models archive-side controls as a variant and records the finding. *Next:* sensitivity analysis on weights; evidence grading; draft results chapter.

### 38.6 Common errors and limits

- Losing the link between results and the evidence behind them.
- Manual analysis steps that cannot be repeated.
- Tuning a model until it agrees with expectations.
- Silent changes of scope or method.

The week-14 checkpoint avoids each: the inventory script has a seed and hash, the model is tested on a hand-worked case, the gateway surprise is kept, and the interview substitution is recorded. Changing the vendor-gateway parameters until imaging exposure looked smaller would have been the third error.

Each is fixed by the same habit: record the step when you take it.

### Exercises — chapter 38

**EX075 — Evidence register.** *Objective:* make traceability concrete. *Inputs:* the week-14 checkpoint in this chapter. *Steps:* write five rows of the evidence register with all fields. *Expected evidence:* table. *Rubric:* 3 = five complete rows (inventory script output with hash, model test results, interview notes reference, two guidance documents) each linked to a criterion; 2 = missing fields; 1 = list; 0 = none.

**EX076 — Report a surprise.** *Objective:* handle unexpected results honestly. *Inputs:* the gateway finding from the week-14 checkpoint. *Steps:* write a 150-word results paragraph that reports the finding, its cause, the variant tested and its limits. *Expected evidence:* paragraph. *Rubric:* 3 = clear finding, mechanism, variant result reported separately, limits (synthetic inventory, one model), no overclaiming; 2 = partial; 1 = hides or minimises the surprise; 0 = none.

### Chapter synthesis

Implementation is disciplined evidence collection: log decisions, register evidence, record changes, build small tested reproducible models, protect host and participant data, and report surprises as findings. The capstone's credibility rests on the trace from each claim back to its evidence.

<!-- cyberabc:chapter-navigation:start ch-38 -->
### Continue studying — chapter 38 of 40

[← Chapter 37](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 →](#ch-39)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes and connection

After this chapter you can (1) evaluate your capstone's results against the success criteria fixed in the proposal; (2) carry out sensitivity and robustness checks on your comparison; (3) state limitations specifically, with their likely direction of effect; and (4) seek and respond to independent review before the final thesis. It builds on Chapters 34, 37 and 38 and prepares the thesis and presentation (Chapter 40).

### 39.1 Against the criteria you set

Evaluation begins with the proposal's success criteria (Chapter 35). Were they met, partly met or not met? Report each honestly with evidence. Then evaluate the **comparison** itself: are the scores supported by the evidence register; would another person, using your anchored scales, give similar scores (ask one); did any constraint exclude an option?

In the worked evaluation, practitioner input was only partly met.

Asking a second person to score two options with your anchored scales is a quick reliability check; if their scores differ by more than one point on any criterion, your anchors need clearer wording before the thesis.

### 39.2 Sensitivity and robustness

Re-run your comparison under plausible variations: different weights (Lab 13), pessimistic and optimistic evidence (Chapter 22's halved autonomy), alternative model assumptions (Chapter 38's archive variant). A **robust** recommendation holds across most variations; a **fragile** one depends on a specific assumption, which you must name. Present the result as a short table: variation, winner, comment.

The worked table applies four such variations.

The worked evaluation shows a fragile result: the gateway wins once cost weight exceeds 0.45, and accelerated replacement wins when isolation's monitoring is assumed not to work. Both are named in the conclusion as reversal conditions, so a reader can see which value judgement and which assumption the recommendation rests on.

### 39.3 Limitations with direction

"The sample was small" is a weak limitation. A useful limitation says **what**, **why it matters** and **in which direction** it probably biases the result. For example: "The exposure model assumes every unsupported device is equally exploitable; in practice internet-adjacent devices are more exposed, so the model probably *understates* the benefit of isolation for imaging devices." Directional limitations let readers adjust your conclusions rather than discard them.

The worked evaluation gives three directional limitations.

Where the direction is genuinely unknown, as with the synthetic inventory, say so explicitly rather than leaving the limitation undirected by omission.

### 39.4 Independent review

Before the thesis is final, ask someone outside your project — a peer from the seminar (Chapter 37), your host supervisor, an academic not involved — to review the evaluation chapter. Record their points and your responses. Independence is the weakest link in most evidence (Chapter 15); the capstone is where you practise strengthening it.

The worked evaluation's reviewer changed the main table.

In the worked evaluation the reviewer's point about unstaffed monitoring changed the main table: the pessimistic variation became a headline result, and the recommendation became conditional. Record the reviewer's role and independence beside each point, so an assessor can judge how much weight the review carries.

### 39.5 Worked example: evaluation table (synthetic)

**This evaluation is synthetic.** Unsupported-devices capstone:

| Success criterion (from proposal) | Result | Evidence |
|---|---|---|
| Comparison of three options with anchored scales | Met | Evidence register rows 1–14 |
| Sensitivity analysis with reversal conditions | Met | Isolation wins unless cost weight > 0.45 |
| Practitioner input on clinical disruption | Partly met | One interview; second replaced by documents |
| Recommendation defended with limits | Met (pending presentation) | Draft chapter 6 |

| Variation | Winner | Comment |
|---|---|---|
| Agreed weights | Isolation with monitoring | Baseline |
| Cost weight 0.4 | Isolation with monitoring | Robust |
| Cost weight 0.6 | Vendor gateway | Fragile above 0.45 |
| Archive-side controls added to gateway | Isolation (narrowly) | Gateway gap partly closed |
| Pessimistic evidence for isolation | Accelerated replacement | Depends on monitoring actually working |

Limitations (directional): synthetic inventory (direction unknown — stated as such); one practitioner interview (probably *understates* clinical disruption of isolation, so isolation's score may be optimistic); exposure model ignores attacker targeting (probably *understates* the value of removing the most exposed devices first). Reviewer's main point: "isolation's advantage depends on monitoring being staffed; show what happens if alerts are not reviewed." Response: the pessimistic variation addresses this and is now in the main table.

### 39.6 Common errors and limits

- Moving the goalposts: evaluating against criteria invented after results.
- Sensitivity analysis on irrelevant parameters only.
- Limitations without direction.
- Reviews from people who helped produce the work.

The worked evaluation avoids the first by using the proposal's criteria, varies the weights that matter, gives each limitation a direction, and uses a reviewer who did not help produce the work.

The second error is common: varying the evidence-strength weight, which barely changes the ranking, while leaving cost untouched, which flips it. A limitation such as "one interview" with no direction leaves the reader unable to adjust the result. A reviewer who helped build the exposure model cannot provide independent review of it.

### Exercises — chapter 39

**EX077 — Directional limitations.** *Objective:* write useful limitations. *Inputs:* the Chapter 34 comparison (Lab 13). *Steps:* write three limitations, each with what, why and probable direction. *Expected evidence:* three limitations. *Rubric:* 3 = specific (e.g. scores by one assessor — direction unknown, raise via second scorer; backups' score ignores data theft — overstates its benefit against double-extortion ransomware; cost scores exclude staff time for drills — overstates backups' cost advantage); 2 = without direction; 1 = generic; 0 = none.

**EX078 — Respond to review.** *Objective:* handle critique. *Inputs:* reviewer says "your restore-time evidence is from one test environment and five drills". *Steps:* write a response that accepts, partially accepts or declines with reasons, and states any change. *Expected evidence:* response. *Rubric:* 3 = accepts the limitation, adds Wilson interval (Chapter 37), states the test–production differences and the direction of bias, adjusts confidence in the recommendation; 2 = accepts without change; 1 = defensive; 0 = none.

### Chapter synthesis

Evaluate against the criteria you set before the results, test the comparison's robustness, state limitations with their direction and invite independent review. A fragile recommendation honestly labelled is more useful than a robust-looking one that hides its assumption.

<!-- cyberabc:chapter-navigation:start ch-39 -->
### Continue studying — chapter 39 of 40

[← Chapter 38](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 →](#ch-40)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes and connection

After this chapter you can (1) structure a bachelor's thesis that reports a comparative, evidence-led capstone; (2) write a conclusion that answers the question within the evidence; (3) present and defend the work to a mixed audience of academics and practitioners; and (4) handle questions, including those you cannot answer, honestly. It completes the course, drawing on every chapter, especially 4, 15, 34 and 35–39.

### 40.1 Thesis structure

A typical 10,000–12,000-word bachelor's thesis in this course:

1. **Abstract** (≈ 250 words): question, method, main result, recommendation, key limitation.
2. **Introduction**: the service, the decision problem, the question, why it matters, the structure.
3. **Background and literature**: concepts and prior work, with the recorded search strategy.
4. **Method**: options, constraints, criteria and scales, weights and how set, evidence plan, models, ethics and authorisation.
5. **Results**: evidence per option and criterion, scores, sensitivity analysis — facts, not interpretation.
6. **Discussion**: what the results mean, comparison with literature, robustness, directional limitations.
7. **Conclusion and recommendation**: the answer, the recommendation, reversal conditions, future work.
8. **References** and **appendices**: evidence register, scripts with hashes, consent forms (blank), host approval.

Write the method chapter first (you know it best), results second, introduction and conclusion last. Every number in the results must come from a script or a register entry.

### 40.2 The conclusion

A strong conclusion answers the question asked — not a broader one — and says how strongly. Compare: "Network isolation is the best way to secure medical devices" (overclaims) versus "For a mid-sized hospital with the synthetic inventory studied, isolation with monitored conduits reduced exposure most per pound, provided alerts are reviewed daily; the recommendation reverses if cost dominates the decision (weight above 0.45) or if monitoring is unstaffed." The second is narrower and far more useful.

The conditional version names the reversal points from the evaluation table.

### 40.3 The presentation

Twenty minutes for a mixed panel: problem and question (3 min), method (4), results (6), recommendation and limits (4), what you would do next (3). One idea per slide; show the comparison table and the sensitivity result; put details in backup slides. Rehearse aloud with a timer and with a non-specialist.

Put the sensitivity table on its own slide.

For the unsupported-devices capstone, the results minutes show the comparison table and the evaluation's variation table; the limits minutes name the staffing condition. Backup slides hold the evidence register and the model test. A rehearsal with a non-specialist usually reveals jargon such as "conduit" that needs one sentence of explanation.

### 40.4 Answering questions

Questions fall into families: *scope* ("why not include X?"), *method* ("why these weights?"), *evidence* ("how do you know this score?"), *validity* ("would this hold in a large hospital?"), *ethics* ("how did you protect the host?") and *application* ("what should the hospital do on Monday?"). Prepare two answers for each family. When you do not know, say so, say how you would find out and, if you discover an error, acknowledge and correct it. Panels value honesty about limits more than confident improvisation.

### 40.5 Worked example: a defensible answer (synthetic)

**This exchange is synthetic.** *Panel:* "Your recommendation depends on monitoring being staffed. Hospitals are short of staff. Isn't your conclusion unrealistic?" *Candidate:* "That is the main fragility in my result. In the pessimistic variation, where alerts are not reviewed, accelerated replacement wins (Table 6.3). So my recommendation is conditional: isolation with monitoring where the hospital can commit to daily review — for example through a shared service across the partnership — and accelerated replacement of the most exposed imaging devices where it cannot. I could not test staffing levels directly; a follow-up study would measure alert review times across several hospitals."

### 40.6 Common errors and limits

- Results and discussion mixed together.
- Conclusions broader than the evidence.
- Slides crowded with text; running out of time before the recommendation.
- Defensive or invented answers to hard questions.
- Disclosing host-identifying information in slides.

The worked answer to the staffing question avoids the fourth error; it cites Table 6.3 and admits an untested assumption.

A results chapter that says "isolation is clearly better" mixes interpretation into results. A conclusion about "medical devices" generally claims more than a 120-device synthetic inventory supports. Slides that reach the recommendation in minute 19 leave no time for limits. And a host's device names on a slide breach the placement agreement even if the thesis was sanitised.

### Exercises — chapter 40

**EX079 — Write the abstract.** *Objective:* compress the capstone. *Inputs:* the synthetic capstone of Chapters 35–39. *Steps:* write a 200–250-word abstract with question, method, main result, recommendation with condition and one limitation. *Expected evidence:* abstract. *Rubric:* 3 = all five elements, numbers where relevant, no overclaiming; 2 = one missing; 1 = descriptive only; 0 = none.

**EX080 — Question bank.** *Objective:* prepare for defence. *Inputs:* your capstone (or the synthetic one). *Steps:* write one question per family listed under answering questions and a three-sentence answer to each. *Expected evidence:* six questions and answers. *Rubric:* 3 = realistic hard questions with honest, evidence-linked answers and at least one "I don't know, but…" answer; 2 = easy questions; 1 = questions only; 0 = none.

### Chapter synthesis

The thesis reports a comparison, not a story: method, results, discussion and a conclusion that answers exactly the question asked with its conditions. Present the comparison and its sensitivity clearly, prepare for every family of question and answer hard ones honestly — that is the professional habit this course exists to build.

<!-- cyberabc:chapter-navigation:start ch-40 -->
### Continue studying — chapter 40 of 40

[← Chapter 39](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

Answers are model results, not the only acceptable ones. Accept a different answer that meets the same standard of evidence, reasoning and honesty about limits. Numbers refer to the synthetic data in this book.

**EX001.** Units: (1/year) × h × (£/h) = £/year. The result is £1,920 **per year**, not per hour. Writing "per hour" would make the scenario look 8,760 times larger than it is when compared with an annual cost of £18,000, inverting the decision.

**EX002.** Halving B's probabilities, the loss avoided is half of £9,600 = **£4,800** a year (ratio 0.40). If the original probability estimates were doubled and the control still halves them, the avoided loss is half of £19,200 = **£9,600**. Recommendation: B is still preferred because its worst credible event (72 h without backup power in a hospital) is the larger harm to people, and the expected-value comparison favours B under both assumptions; the uncertainty in the probabilities does not change the ranking.

**EX003.** Signed firmware updates — firmware layer (does not address a malicious but correctly signed update from a compromised vendor). OS user accounts — operating system (does not stop an authorised user's mistake). Drug-library limits — application (does not catch a wrong drug chosen within limits). Database backups — data (do not help if backups are encrypted too, or never restored). Staff training — people (does not stop a convincing, targeted lure every time).

**EX004.** Billing — IT (worst: revenue and customer service disruption; patch normally). Feeder RTU — OT (worst: loss of view/control of distribution; vendor-approved window). Patient administration — IT, but clinically important (worst: delayed care through lost scheduling and records; normal patching with clinical change control). BMS for theatre ventilation — OT in a healthcare setting (worst: unsafe air changes cancelling surgery or risking infection; estates and clinical coordination and vendor-approved window). The BMS shows that "building systems" are OT whose consequences are clinical.

**EX005.** Change the filter to handle `row["os_end_of_support"] == ""` separately: `unknown = [r for r in rows if not r["os_end_of_support"].strip()]`, report them under "UNKNOWN — needs owner", and compute `unsupported` only from rows with a date. Output adds `VEN-01 ventilator`. A ventilator with an unknown support status is life-sustaining equipment on the clinical network whose patch exposure nobody can state; escalate to clinical engineering for the vendor's support statement and placement review.

**EX006.** `def is_unsupported(row, year): return int(row["os_end_of_support"]) < year`. Tests: EoS 2030 → False; 2020 → True; EoS equal to `year` (2026) → False under this rule. Rule stated: a device whose support ends *during* the current year is still supported now, but should be flagged in a separate "ends this year" list; an alternative defensible rule treats `<=` as unsupported to be conservative. Either is acceptable if stated and tested.

**EX007.** Claim: "the payment system is secure". Evidence: "no outage last year". Warrant: "absence of outage implies absence of exploitable weakness" — false, because weaknesses may be unexploited, exploitation may cause no outage (fraud, data theft) or be undetected. Supported rewrite: "Calder Mutual's payment system had no recorded outage last year; this says nothing by itself about its exposure to attack, which requires assessment."

**EX008.** Model (≈ 100 words): "We recommend funding the hospital generator test programme (option B). It avoids an estimated £9,600 of expected loss a year against £12,000 cost, compared with £4,320 against £18,000 for a second dispatch link, and it addresses the more serious worst case: up to 72 hours without backup power at Calder Valley Hospital. These estimates assume the outage probabilities are right to within a factor of two; the ranking holds across that range. We would revisit the choice if new evidence showed the dispatch link's single cable route at much higher risk, for example during planned road works."

**EX009.** Patient records: C > I > A (disclosure harms patients and breaches law; integrity also matters for care). Chlorine dosing: I/safety > A > C (a wrong setpoint poisons or under-disinfects water). Card authorisation: I ≈ A > C (fraudulent or unavailable payments; card data confidentiality also regulated — accept C high with reasoning). Call recordings: C ≈ I > A (sensitive personal content; evidential integrity; availability needed for review but not real-time).

**EX010.** "The asset is CEDC's dispatch service. A cut cable from roadworks is a threat; the single cable route is a vulnerability; the impact would be loss of dispatch connectivity, delaying emergency response."

**EX011.** $C \cap U$ = {INF-02, IMG-01, IMG-02, ADM-02}. $(C\cap U)\cap K$ = {IMG-01, ADM-02}. $U \setminus C$ = {LAB-01}. Act first on {IMG-01, ADM-02}: unsupported, on the clinical network and with a known exploited flaw. ADM-02 is also the cheapest to fix.

**EX012.** Reachability treats every edge as "fails if the supplier fails" (AND over all suppliers). With a satellite alternative, dispatch fails only if **both** the exchange and the satellite link fail (OR over suppliers). Model change: mark each node as needing **all** of its inputs or **any one** of them, and propagate failure accordingly (an AND/OR dependency graph, as used in fault trees, Chapter 28).

**EX013.** RDP corporate→control: benign — engineer's undocumented shortcut; malicious — intruder pivoting from a phished PC; distinguish by change tickets, the user logged on at 10.1.4.80, authentication logs on 10.20.0.5 and whether the session followed a phishing alert. Control→internet: benign — vendor software update check; malicious — command-and-control or data exfiltration; distinguish by destination ownership, process making the connection, volume and periodicity. Field→control Modbus initiation: benign — misconfigured device after maintenance; malicious — compromised field device probing; distinguish by device configuration versus baseline, maintenance records and the function codes used.

**EX014.** (1) Host-level rules: allow only the collector 10.5.0.11 to reach only the SCADA server 10.20.0.5 on 4840, rather than any DMZ host to any control host; enforce in the firewall; check with flow logs. (2) Restrict Modbus to read function codes from the SCADA server except for named write registers, using an industrial-protocol-aware firewall; check by reviewing rejected-write logs. Other valid refinements: one-way transfer for the historian, time-of-day rules for engineering access.

**EX015.** (1) `"nan"` is accepted because every comparison with NaN is false. (2) `"abc"` (or `""`) raises `ValueError`, crashing or leaving the caller in an undefined state. (3) If `current` is NaN (e.g. a failed sensor read), `abs(x - current) > 0.5` is false for any `x`, so any in-range setpoint passes the step check. `"inf"` is rejected by the range check — but only because it is greater than 4.5, which is luck, not design.

**EX016.** Chlorine dosing pump: keep last good setpoint, raise an operator alarm, do not move toward maximum; the process owner (water-quality manager) decides this failure behaviour. Raw-water inlet valve: keep last good position and alarm; operations decide whether a fallback position is needed to protect treatment capacity. Log for both: timestamp, source (user/station), raw input, parsed value if any, rule that failed, current value, action taken.

**EX017.** `SELECT a.site, COUNT(*) FROM asset a JOIN advisory v ON a.product = v.product WHERE vlt(a.version, v.fixed_in) GROUP BY a.site;` → Head office 1; Substation North 1.

**EX018.** Text sort orders "critical" < "high" < "low" < "medium", so "low" sorts before "medium" — wrong. Fixes: store a numeric `severity_rank` (critical 4, high 3, medium 2, low 1) and sort by it; or sort with `CASE severity WHEN 'critical' THEN 4 ... END`, or join a lookup table.

**EX019.** Stop conditions and calls: (1) any unexpected process alarm or operator-reported anomaly — control-room supervisor; (2) any device behaviour change coinciding with capture equipment connection — supervisor and OT engineer; (3) observing safety-system traffic or networks outside scope — stop capture, OT security lead; (4) operator or supervisor asks to stop — comply immediately; (5) discovery of personal data or credentials in clear — stop, secure files, data-protection officer and OT security lead.

**EX020.** Stakeholders: patients on ventilators, clinicians, clinical engineering, security, hospital management, vendor. Harms of patching all now: devices unavailable during peak demand, possible update failures. Harms of not patching: exposure to exploitation causing device malfunction. Alternatives: patch in batches as devices rotate out of use; isolate the fleet to a dedicated network segment with monitoring until patched; vendor-supported update at the bedside during low-dependency periods. Decision record names the clinical director and the security lead as joint risk owners, records the rationale, the interim controls and a completion date.

**EX021.** Exploitable as deployed: yes, remotely from the corporate network. Known exploited: assume unknown; check. Controls: theatre ventilation — high consequence. Compensating controls: restrict interface access now to two estates workstations; monitor. Window: schedule the 30-minute restart with estates and theatres when theatres are not in use (e.g. a weekend night), with manual ventilation checks. Recommendation: restrict now, patch in the earliest safe window, confirm afterwards.

**EX022.** "Secure the accounts" → "Every HMI login is an individual named account; no default vendor accounts are enabled; checked monthly by exporting the account list and comparing with the roster." "Turn on logging" → "Security and application logs are forwarded to the central log server within 5 minutes; checked weekly by confirming the latest event from each host." "Lock down USB" → "USB mass-storage is disabled by policy on operator workstations; checked by quarterly policy export and a test with an approved device."

**EX023.** Prior 0.01: $0.95 \times 0.01/(0.95\times0.01 + 0.01\times0.99) \approx 0.490$. Prior 0.001, FPR 0.001: $0.95\times0.001/(0.95\times0.001 + 0.001\times0.999) \approx 0.487$. A tenfold lower false-positive rate helps as much as a tenfold higher base rate. Analysts cannot change the base rate, but they can lower the FPR through tuning, context enrichment and allowlisting — the practical lever.

**EX024.** Independent: $0.05^2 = 0.0025$. With common cause: ≈ $0.02 + 0.0025 = 0.0225$, about nine times worse. Remedy: separate fuel supplies or fuel testing and polishing, different generator models or start systems, and periodic load tests.

**EX025.** Roles: call handler (create incidents, view CAD); dispatcher (assign units, update incidents); supervisor (override, reassign, view reports); CAD administrator (configure system, manage accounts; no dispatch); vendor support (time-limited, session-approved access to test environment by default). Toxic pairs: CAD administrator + audit-log administrator (could hide own changes); vendor support + permanent production access; dispatcher + CAD administrator (could alter rules and act on them unseen).

**EX026.** Add `approved` dates to each tuple; flag if `roles & PRIV` and `(TODAY - approved).days > 180`. With, for example, *dev* approved 2025-11-01 (334 days) and *chloe* approved 2026-07-01 (92 days), output adds "re-approval overdue 334 d" to *dev* only. The test must show one flagged and one not flagged privileged account.

**EX027.** Minimised design: log staff ID, patient record identifier (not name or diagnosis), workstation, timestamp, access type; retain 2 years (or the period set by the hospital's policy), restricted to the privacy officer and two named auditors; purpose stated as detecting inappropriate access; staff informed through policy and login notice; re-identification of the patient only for confirmed investigations.

**EX028.** Risks: in small postcodes, a unique property type (e.g. the only detached house) identifies a household; hourly patterns reveal occupancy, routines and absences. Mitigations: publish only aggregates over a minimum number of meters (e.g. ≥ 10), coarsen time (daily) or location; provide fine data only under access agreements to approved researchers.

**EX029.** Diagram (2025) — document, team-produced, a year old, not independent: shows design intent only. Failover test report (14 min) — demonstration, by operations, last year, not independent: real evidence that failover *can* work. Auditor's note — independent, recent: shows the test was announced, so staff were prepared and conditions favourable. Conclusion: evidence that failover can meet 15 minutes under prepared conditions; not that it would during an unannounced failure under load. Ask for an unannounced or independently observed test with recorded load.

**EX030.** Metric: "proportion of privileged and remote-access accounts using phishing-resistant authentication", measured monthly from the identity system as (accounts with phishing-resistant authenticators) / (all privileged and remote-access accounts), denominator and exclusions reported. Gaming risk: reclassifying accounts as non-privileged to shrink the denominator — mitigated by an independent definition of privilege. (An authorised-simulation report rate is also acceptable, with gaming via predictable simulations.)

**EX031.** Least privilege — remote users land on the whole control network; fail-safe defaults — vendor accounts permanently enabled; complete mediation — no per-session check of who is connecting or why; separation of privilege — a password alone grants access, no second factor or operator approval; least common mechanism — one gateway shared by all users and vendors directly into control.

**EX032.** One account or server compromise disables firewall rules, endpoint protection and backups together — the three "layers" share a single mechanism. Changes: separate administrative tiers and credentials (and management hosts) for network, endpoint and backup systems with phishing-resistant MFA; keep at least one backup copy offline or immutable and managed outside the domain.

**EX033.** (a) Digital signatures — anyone can verify, only the manufacturer can sign. (b) MAC with sequence numbers (or a mutually authenticated channel such as TLS where devices support it) — authenticity, integrity and freshness. (c) Symmetric disk encryption with the key protected by hardware and the user's authentication. (d) Hash chain with an externally held anchor (or signed log entries).

**EX034.** An administrator with both log and anchor access edits an entry, recomputes every following head and overwrites the anchor with the new head; verification then passes. Prevention: hold the anchor on a system administered by a different team with append-only storage; periodically publish or countersign heads with a trusted timestamp service; alert on any anchor rewrite.

**EX035.** Example: "Among electricity distribution operators in [one country] that published incident or annual reports in 2020–2025, how often are phishing-initiated incidents mentioned, and which mitigations do the reports describe?" — descriptive with a comparative element (mitigations), evidence from public reports. Alternatively, a comparative question about two phishing-resistant authentication approaches in a lab.

**EX036.** Construct: "reported incidents" measures reporting and detection, not attacks. Internal: hospitals that buy X may also have larger budgets, more staff or different exposure (confounding); selection — buyers differ systematically. External: findings from the hospitals studied may not transfer. Reliability: different definitions of "ransomware incident" across hospitals.

**EX037.** Functions: "provide payment services" (card authorisation, transfers) and "provide access to cash". Dependencies: power, telecom (exchanges, carriers), national payment schemes and clearing, card networks, cloud providers, staff. Harm timeline: card payment failures hurt within hours (fuel, food purchases); salary and benefit payments within days; loss of cash access compounds harm if card payments are also down.

**EX038.** Risk: "which scenarios at the works are most likely and damaging?" — may miss novel cascades or adversary adaptation. Resilience: "how long can the works supply safe water in degraded modes, and how fast does it recover?" — may underweight cost-effective prevention. Systems: "which control actions by operators, software and procedures could be unsafe?" — harder to quantify and to prioritise.

**EX039.** Example (Oldsmar): CISA states unidentified actors accessed the SCADA system via remote-access software, increased the sodium hydroxide setpoint, and an operator reversed the change. Commonly repeated but unsupported by that advisory: claims about the attacker's identity. Report phrasing: "In February 2021 CISA reported an apparent unauthorised change to chemical dosing at a Florida water plant; in 2023 a former city official said it was likely employee error. Either way, the case illustrates the risk of unmanaged remote access."

**EX040.** Dependencies: ticketing and revenue systems (operating without revenue collection may be refused), crew rostering and scheduling, passenger-information systems, maintenance management (safety-critical defect records). Measures: pre-agreed degraded-operation rules (e.g. free travel, paper rosters) approved by management in advance; separation and backup of operationally necessary data such as defect records; regular exercises of running trains without business IT.

**EX041.** (a) Loss of historical view — low immediate risk, reduced trend analysis. (b) Loss of view — dangerous: operators may act on stale data. (c) Manipulation of control — direct process effect. (d) Loss of protection — highest severity: the last automatic barrier is gone.

**EX042.** Chain: signalling (route setting and train detection) → train control/driving → crew and control communication → passenger information → ticketing. Degraded modes: signalling failure — manual authority to proceed with reduced speed and frequency; radio failure — fixed telephones at stations, trains held at platforms; passenger information failure — staff announcements, reduced service notices; ticketing failure — free travel or paper tickets. Constraints: lower capacity, more staff, longer journey times.

**EX043.** With card payments given 48 h autonomy: at 6 h, 3 services lost (exchange A, water pumps, rail signalling); at 30 h, 5 lost (card payments survive). Halved autonomies at 6 h: 5 services lost — telecom exchange A (2 h), water pumps, water treated storage (5 h), card payments (2 h), rail signalling (1 h). Recommendation: re-home card payments to exchange B or add a generator at exchange A, and replace design-figure autonomies with tested values, since the pessimistic case loses water storage within 6 h.

**EX044.** Fuel supply contract and delivery route (evidence: contract, delivery test during an exercise); staff to run and refuel (evidence: rota and training records); generator start and load reliability (evidence: monthly test logs under load); switchgear/transfer switch and cooling (evidence: maintenance records, test of automatic transfer).

**EX045.** Both score 10. The equal score hides that A is frequent and minor while B is rare and severe (theatre cancellations, patient harm), and that ordinal labels cannot be multiplied meaningfully. Present a worst-credible-consequence column and approximate quantitative ranges (frequency per year, outage duration, harm), or treat B under consequence-first analysis.

**EX046.** Consequence: "fraudulent high-value transfers released" (or "payments unavailable > 4 h on salary day"). Paths: compromised operator credentials; insider creating and approving via a toxic role combination (Lab 7); malicious change to the payment switch's rules; mistaken bulk file upload. Engineering: hard per-transaction and daily limits enforced in the switch, out-of-band confirmation for transfers above a threshold. Procedural: two-person approval with separated roles.

**EX047.** Offline backups — corrective, technical. Two-person approval — preventive, procedural. Outlet chlorine analyser tripping a valve — preventive (bounds the consequence), engineering. SIEM alert on new admin accounts — detective, technical. Key switch for PLC programming — preventive, physical.

**EX048.** Row: "Ransomware on BMS server" — preventive: application allowlisting, restricted admin access, segmentation from corporate; detective: monitoring of the BMS server and backups; corrective: tested restore of BMS server and configurations, local manual control of air handling. Most valuable improvement: a tested restore plus a rehearsed local-control procedure, because local control keeps theatres safe whatever the cause of BMS loss.

**EX049.** Priority 2 (confidence: medium): investigate and close the CW corporate→control RDP flow and the control→internet flow (Lab 4) — they bypass the DMZ, and the consequence path leads to water treatment control; owners: CW OT security (investigate this week), CW network team (rules). Priority 3 (confidence: high): disable the leaver account, remove toxic combinations and move vendor access to per-session approval (Lab 7) — direct paths to unauthorised control actions and payment fraud; owners: system owners, within one week. Isolation of unsupported clinical devices (Lab 2) is an acceptable alternative third priority with consequence reasoning.

**EX050.** Model statement: "I reran Labs 2, 4, 5 and 7 from the appendix with Python 3.13. Hashes of lab02, lab04 and lab07 matched; lab05's did not because the author had added a LEFT JOIN query, documented in their change notes. All printed outputs matched the appendix, including the extra query's output. The findings section is reproducible."

**EX051.** S: a rogue host spoofs the collector — mutual certificate authentication, host-level rules. T: values altered in transit — authenticated and integrity-protected OPC UA session. R: collector denies queries — logging on the SCADA side with time sync. I: collector exposes more tags than needed — read-only account limited to required tags. D: excessive polling loads the SCADA server — rate limits and resource monitoring. E: collector account can write — read-only role, server-side enforcement.

**EX052.** Objectives: (1) decide within 30 minutes whether to switch to paper patient administration, (2) make the data-protection assessment and decide on notification within the plan's timescale. Participants: on-call manager, emergency department lead, IT on-call, data-protection officer, communications, estates. Injects: 23:10 ransom note on admin screens; 23:40 emergency department cannot see bed state; 00:30 evidence that patient data was copied out; 01:30 journalist enquiry. Record: decision times, decision owners, information used, plan deviations.

**EX053.** Verification: in an authorised window, from a test host on the corporate network, attempt connections to each control-zone address on a defined port list; the claim is false if any connection succeeds. Validation: review configurations and flow logs for alternative paths — dual-homed hosts, remote-access gateways, wireless bridges, vendor modems; the claim is false if any path from corporate to control exists. Authorisation: written RoE from CW operations and security with stop conditions.

**EX054.** Threshold 0.7: errors = FP 2 + FN 7 = 9; accuracy = 5,016/5,025 ≈ 0.9982. Never alerting: accuracy = 5,000/5,025 ≈ 0.9950. Both look excellent because 99.5% of events are benign; accuracy rewards ignoring the rare class. Report precision and recall (0.90/0.72 versus undefined/0).

**EX055.** With the BMS path now requiring a grid outage: backup fails = $1 - 0.98 \times 0.995 \times 0.99 \times 0.998 \approx 0.03658$; top = $0.05 \times 0.03658 \approx 0.001829$ — about half the previous 0.003729 and only slightly above the physical-only 0.001733. The cyber path now needs a coincident grid outage, restoring the two-event structure; an adversary able to cause a grid outage as well remains a residual risk.

**EX056.** Dosing pump runs at maximum — overdosing, water unsafe — detected by outlet analyser high alarm — hard-wired rate limit, analyser trip. Pump stops — under-disinfection — analyser low alarm, pump-run feedback — duty/standby pump. Analyser reads low (drift) — controller increases dosing — comparison with manual sample/second analyser — calibration schedule. Analyser frozen — no response to real changes — "stale value" alarm on unchanging reading — maintenance checks.

**EX057.** Model: "Across 15 incidents shared by CRP members, half were detected within 4 hours; the 90th percentile was about 56 hours; one case took 240 hours. Recovery took a median of 8 hours (90th percentile about 38 hours). The mean detection time (27 h) is distorted by the single longest case. These records are few, sanitised and rely on self-reported start times. Why did monitoring miss the 240-hour credential misuse for ten days?"

**EX058.** (1) Operations confirm process state and that SCADA and controllers behave normally — control-room supervisor. (2) Prepare local/manual operation for critical stations in case SCADA is affected — operations manager. (3) Isolate the historian from the control zone (and DMZ conduits) — security analyst with supervisor's authorisation. (4) Preserve evidence: memory and disk image of the historian, firewall and flow logs — security. (5) Check SCADA servers, engineering workstations and controller configurations against known-good baselines — OT engineer with security. Then recovery and notification decisions.

**EX059.** System records (remote-access logs, CPN control) are high because they are generated automatically by separate systems. Operators noticing at 02:10 is high (shift log, multiple witnesses). The 01:52 setpoint change is medium: the anchored head shows the log was altered, so neither the recorded time nor value can be trusted. Raising it to high needs the PLC's own event log or setpoint audit trail, the historian trend of the setpoint and tank level, and the vendor's session recording.

**EX060.** Actions: per-session vendor approval with recording (CW OT security, 1 month; verify via session logs); alarm on setpoint changes outside limits or rate (CW engineering, 2 months; verify with test change); move the log anchor to a system run by another team (CW IT, 1 month; verify by access review); cross-operator status template and contact list (CRP coordinator, 6 weeks; verify in next exercise); joint CW–CPN exercise on combined grid and process events (CRP, 6 months; verify by after-action report).

**EX061.** Failed: that operator workstations and remote access were only usable by legitimate staff (CISA reports remote operation of breakers); that call centres would remain available to customers (CISA reports disruption of customer call centres). Held: that manual operation of substations was possible — CISA reports power was restored by switching to manual mode.

**EX062.** Map: endpoint product ↔ CVH, CEDC, Calder Mutual (reach 3, three sectors — highest); cloud region ↔ CEDC, CT (reach 2); OT integrator ↔ CW, CPN (reach 2). Measures: staged endpoint updates with canary groups and a tested rollback; confirm CEDC and CT fallbacks work without the cloud region; separate per-operator integrator credentials, per-session approval and joint monitoring.

**EX063.** Model: "Our power-resilience model (synthetic numbers) shows CVH's backup design needs two failures to cut power to critical areas — a grid outage and a backup failure. One weakness bypasses this: the building-management system can switch off critical circuits on its own. If it were misused, patients in theatres and intensive care could lose power without any grid problem. We propose an engineering change (about £25,000, illustrative) so that the building system cannot shed critical circuits. The model's probabilities are estimates and an attacker does not behave randomly, so the case rests on removing the single point of failure, not on the exact numbers."

**EX064.** Risk: an operator who mistypes a password under stress — or an attacker deliberately entering wrong passwords — locks the HMI during an emergency, preventing control. Alternatives: no lockout on control-room HMIs, combined with physical access control to the room, rate limiting, alerting on repeated failures and an emergency override procedure with audit; strong authentication where it does not impede response (e.g. smart cards).

**EX065.** $p_o = 34/40 = 0.85$. Coder A: 10/40 = 0.25 yes; B: 12/40 = 0.30 yes. $p_e = 0.25 \times 0.30 + 0.75 \times 0.70 = 0.075 + 0.525 = 0.60$. $\kappa = (0.85 - 0.60)/(1 - 0.60) = 0.625$. Conventionally described as substantial agreement; scales are conventions, so report the value, discuss disagreements and refine the codebook.

**EX066.** Consent information: purpose of the study; voluntary participation and the right to withdraw up to a stated date; what is recorded (notes or audio) and why; how data are stored, for how long and who sees them; how results will be reported (anonymised, no organisation-identifying or vulnerability details, host review). Data protection: encrypted storage, pseudonyms for people and organisations, deletion of raw notes after transcription and on schedule, and no technical vulnerability specifics in any output.

**EX067.** Segmentation score $= 5w + 8(1-w)/3$; backups $= 4w + 13(1-w)/3$. Tie: $w = 5(1-w)/3 \Rightarrow 3w = 5 - 5w \Rightarrow w = 5/8 = 0.625$. Both score 4.125 there. Above 0.625 segmentation wins.

**EX068.** The requirement is a constraint, not a weighted criterion: an option that cannot demonstrate 4-hour restoration is excluded. Backups with restore drills can provide the demonstration directly (drill records, ideally independently observed). Segmentation and managed detection reduce the likelihood or spread of ransomware but do not restore service; they qualify only in combination with a demonstrated recovery capability. The comparison becomes one of combinations meeting the constraint.

**EX069.** (a) Not comparative or bounded as written; could be reframed. (b) Comparative, feasible with a synthetic dataset, ethical, useful for operators, bounded — choose (b). (c) Unauthorised testing of a real utility — unethical and likely unlawful; reject (Chapter 10).

**EX070.** Consequence reduction — lab exposure-model outputs for each option; threat: the model's simplified exposure assumptions. Clinical disruption — interview data and published clinical-engineering guidance; threat: one or two interviews may not represent other hospitals. Cost — published price ranges and staff-time estimates; threat: prices vary and may be outdated. Evidence strength — grading of sources with the Chapter 15 questions; threat: grading by one person (mitigate with a second grader).

**EX071.** Supervisors: named CEDC IT manager and academic supervisor. Permitted: observation, document review, inventory updates in the test environment; forbidden: any change to live CAD or telephony, any testing without written RoE. Confidentiality: no removal of documents; coursework reviewed by CEDC before submission. Data protection: no access to call recordings or incident records with personal data. Safety: site induction including emergency procedures. Escalation: any serious discovery reported immediately to the site supervisor only.

**EX072.** Safe version: "Tuesday: reviewed the payment-gateway environment with my supervisor; observed a component that appears older than the current supported release; raised it with my supervisor for follow-up." Removed: hostname, credentials, IP address, person's username and exact version. The credential must never be recorded; report to the supervisor that it was written down so it can be changed.

**EX073.** 34/40: Wilson ≈ [0.71, 0.93]. 85/100: ≈ [0.77, 0.91]. The point estimate is the same (0.85) but the interval narrows roughly with $1/\sqrt{n}$; to claim reliability with useful precision, CEDC needs a programme of regular drills, not a single campaign.

**EX074.** Review: "accuracy" on an imbalanced dataset is uninformative (Chapter 27); a single public testbed may not represent live water systems (external validity); the evaluation protocol may inflate results (Kim et al., 2022); the vendor has an interest. Questions: precision and recall at the threshold you recommend; false alarms per day in live deployments; evaluation protocol and whether training and test data were separated in time; any independent evaluation or customer references in comparable utilities.

**EX075.** Rows (item / source / date / type / how obtained / storage / criterion): (1) synthetic inventory, `make_inventory.py` seed 38 with hash / author / week 8 / measurement / script / project repo / consequence; (2) model test results for the 5-device case / author / week 10 / verification / script / repo / evidence strength; (3) interview 1 notes, pseudonym P1 / clinical engineer / week 11 / qualitative / consented interview / encrypted store / clinical disruption; (4) guidance document A / public body / year / document / download / references folder / clinical disruption; (5) guidance document B / public body / year / document / download / references folder / consequence and cost.

**EX076.** Model: "Contrary to expectation, the vendor-gateway option reduced exposure least for imaging devices (Table 5.2). The cause is that imaging devices also accept connections from the image archive, which the gateway does not mediate. A variant adding archive-side controls closed part of the gap (Table 5.3), but isolation still scored higher. Both results are reported because the original configuration reflects how gateways are commonly deployed. The finding rests on a synthetic inventory and one exposure model; it should be checked against real network data before generalising."

**EX077.** (1) Scores were assigned by one assessor: direction unknown; mitigate with a second independent scorer. (2) The backups score ignores data theft in double-extortion ransomware: probably *overstates* backups' benefit relative to options that reduce intrusion. (3) Cost scores exclude staff time for restore drills: probably *overstates* backups' cost advantage. Other defensible limitations are acceptable with direction.

**EX078.** Model: "Accepted. The restore-time evidence comes from five drills in one test environment. I have added a Wilson 95% interval (0.38–0.96 for 4 of 5) and a table of differences between test and production (data volume, integrations, staff). Because production restores involve more data and integrations, the drills probably understate real restore times. I have lowered the confidence of the recommendation from high to medium and recommended an independently observed production-scale drill."

**EX079.** Model (≈ 220 words): "Hospitals keep clinical devices whose software is no longer supported, because devices outlive their operating systems. This capstone asked which of three approaches — accelerated replacement, network isolation with monitoring, or vendor-managed secure gateways — best reduces exposure for a mid-sized hospital within a fixed budget. Using a synthetic inventory of 120 devices built from published categories, an exposure model tested against a hand-worked case, one practitioner interview and public guidance, the options were compared on consequence reduction, clinical disruption, cost and evidence strength with weights set in advance. Isolation with monitoring scored highest and remained preferred unless cost carried more than 45% of the decision weight, in which case vendor gateways were preferred, or monitoring alerts were not reviewed, in which case accelerated replacement of the most exposed imaging devices was preferred. Vendor gateways underperformed for imaging devices because archive connections bypass them. We recommend isolation with monitored conduits where daily alert review can be committed, and prioritised replacement elsewhere. The main limitation is the synthetic inventory and single interview, which probably make isolation's clinical disruption look smaller than it is."

**EX080.** Example questions: scope — "Why not include cloud-hosted imaging?" (out of scope by design; would change exposure; future work). Method — "Why these weights?" (set with the host before scoring; sensitivity shown; reversal at 0.45). Evidence — "How do you know isolation's disruption score?" (one interview plus guidance; acknowledged as weak; directional limitation). Validity — "Would this hold in a large teaching hospital?" ("I don't know; the inventory mix differs; I would test with their category distribution"). Ethics — "How did you protect the host?" (synthetic data, anonymised interview, host review). Application — "What should the hospital do on Monday?" (restrict and monitor the imaging conduits; start the replacement case for the top five exposed devices).



<a id="glossary"></a>

## Glossary

- **Allowlist** — a policy that permits only listed flows, programs, values or users; everything else is denied.
- **Anchor** — a trusted copy of a hash-chain head kept outside the reach of whoever controls the log.
- **Autonomy (backup)** — how long a service continues on its own backup power, storage or manual process.
- **Base rate** — how common a condition is before any test or alert; it dominates the meaning of an alert.
- **Common cause / common mode** — a single cause that defeats several supposedly independent safeguards.
- **Compensating control** — a measure that reduces exposure when the preferred control (e.g. patching) is not possible.
- **Conduit** — a controlled communication path between zones.
- **Consequence-first analysis** — risk analysis that starts from unacceptable outcomes and traces paths to them (e.g. CCE).
- **Constraint (decision)** — a requirement that excludes options regardless of their score.
- **Critical function** — a function (e.g. "supply water") whose disruption would seriously harm society.
- **DMZ** — a network zone between enterprise and control systems for controlled data exchange.
- **Expected annual loss (EAL)** — probability per year multiplied by loss per event, summed over scenarios.
- **FMEA** — failure modes and effects analysis; bottom-up analysis of how components fail and what follows.
- **Fault tree** — a top-down model of an undesired event built from AND and OR gates over basic events.
- **HMAC** — a keyed message authentication code built from a hash function.
- **HMI** — human–machine interface used by operators to view and control a process.
- **Kappa (Cohen's)** — agreement between two coders corrected for chance.
- **Least privilege** — giving each user or program only the access it needs.
- **OT (operational technology)** — systems that monitor or control physical processes.
- **Precision / recall** — the share of alerts that are real / the share of real events that are caught.
- **Rules of engagement (RoE)** — written terms authorising a test or exercise: scope, methods, window, stop conditions.
- **SCADA** — supervisory control and data acquisition; wide-area supervision of control loops.
- **Sensitivity analysis** — checking whether a decision changes when uncertain inputs or weights change.
- **SIS** — safety instrumented system; independent automatic protection that brings a process to a safe state.
- **STPA** — system-theoretic process analysis; finds unsafe control actions in a control structure.
- **Toxic combination** — a set of roles that must not be held by one person (separation of duties).
- **Validation / verification** — achieving the purpose in the real setting / meeting the specification.
- **Wilson interval** — a confidence interval for a proportion that behaves well with small samples.
- **Zone** — a group of assets with similar security requirements.

<a id="references"></a>

## References

Laws, standards, guidance and incident pages change. Versions and dates below are those consulted for this draft (October 2026); re-verify before relying on them.

**Policy, law, standards and frameworks**

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
- Cybersecurity and Infrastructure Security Agency. [ICS Advisories](https://www.cisa.gov/news-events/ics-advisories).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- International Electrotechnical Commission. [IEC 62443-3-2:2020 — Security risk assessment for system design (catalogue page)](https://webstore.iec.ch/en/publication/30727).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- MITRE. [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/).
- Modbus Organization. [Modbus Application Protocol Specification](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework). February 2024.
- National Institute of Standards and Technology. [NIST Privacy Framework](https://www.nist.gov/privacy-framework).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final). September 2012.
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025.
- National Institute of Standards and Technology. [SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final). September 2023.
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST, December 2021.
- National Institute of Standards and Technology. [SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final). August 2020.
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final). February 2022.
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final); [FIPS 197, Advanced Encryption Standard](https://csrc.nist.gov/pubs/fips/197/final); [FIPS 198-1, The Keyed-Hash Message Authentication Code (HMAC)](https://csrc.nist.gov/pubs/fips/198-1/final).
- National Institute of Standards and Technology. [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). 13 August 2024.
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- Open Source Security Foundation. [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/).
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, February 1997.
- Rescorla, E. [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446). IETF, August 2018.
- Eddy, W. (ed.). [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293). IETF, August 2022.
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).

**Professional ethics**

- Association for Computing Machinery. [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics). 2018.

**Incidents and sector evidence**

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency and Federal Bureau of Investigation. [DarkSide Ransomware: Best Practices for Preventing Business Disruption from Ransomware Attacks (AA21-131A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a). May 2021, updated July 2021.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Cybersecurity and Infrastructure Security Agency. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf). 2019.
- E-ISAC and SANS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). March 2016 (archived copy).
- Langner, R. [Stuxnet: Dissecting a Cyberwarfare Weapon](https://doi.org/10.1109/MSP.2011.67). *IEEE Security & Privacy*, 9(3), 49–51, 2011.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems*, 21(6), 11–25, 2001.
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

**Computing, security, safety and resilience**

- Bruneau, M., Chang, S. E., Eguchi, R. T., et al. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra*, 19(4), 733–752, 2003.
- Codd, E. F. [A Relational Model of Data for Large Shared Data Banks](https://doi.org/10.1145/362384.362685). *Communications of the ACM*, 13(6), 377–387, 1970.
- Diffie, W., and Hellman, M. [New Directions in Cryptography](https://doi.org/10.1109/TIT.1976.1055638). *IEEE Transactions on Information Theory*, 22(6), 644–654, 1976.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis*, 29(4), 498–501, 2009.
- Leveson, N. [A New Accident Model for Engineering Safer Systems](https://doi.org/10.1016/S0925-7535(03)00047-X). *Safety Science*, 42(4), 237–270, 2004.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320(7237), 768–770, 2000.
- Rivest, R. L., Shamir, A., and Adleman, L. [A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](https://doi.org/10.1145/359340.359342). *Communications of the ACM*, 21(2), 120–126, 1978.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.

**Evidence, research and argument**

- Arp, D., Quiring, E., Pendlebury, F., et al. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). *USENIX Security Symposium*, 2022.
- Efron, B. [Bootstrap Methods: Another Look at the Jackknife](https://doi.org/10.1214/aos/1176344552). *The Annals of Statistics*, 7(1), 1–26, 1979.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *AAAI*, 2022.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology*, 9(10), e1003285, 2013.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation*, 7(1), 12–24, 2013.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). *IEEE Symposium on Security and Privacy*, 2010.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
- Wilson, E. B. [Probable Inference, the Law of Succession, and Statistical Inference](https://doi.org/10.1080/01621459.1927.10502953). *Journal of the American Statistical Association*, 22(158), 209–212, 1927.
