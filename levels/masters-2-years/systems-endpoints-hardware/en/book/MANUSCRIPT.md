# Systems, Endpoint and Hardware Security: Master's Course

- Language: English (`en`); course 173, Master's course (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students who must compare competing explanations of endpoint security problems with careful observational research.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only servers, endpoints and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, inventories, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one master's student from a manufacturer's laptops drifting away from their security baseline, through question and literature method, a baseline seminar, study design and ethics, competing explanations, proposal and pilot, analysis, writing and independent review. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Chloé Dubois** | Master's student | Invented |
| **Dr Arjun Mehta** | Supervisor | Invented |
| **Redbourne University** | Fictional university | Invented |
| **Halvorsen Engineering** | Fictional manufacturer | Invented |

### Core sources

NIST [SP 800-123](https://doi.org/10.6028/NIST.SP.800-123), [SP 800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4), [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128), [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5) and [SP 800-193](https://doi.org/10.6028/NIST.SP.800-193); [CIS Controls v8](https://www.cisecurity.org/controls/v8) and [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); DISA [STIGs](https://public.cyber.mil/stigs/); Microsoft [Windows security baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines); Linux [kernel self-protection](https://www.kernel.org/doc/html/latest/security/self-protection.html). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn an operational problem into a researchable question; (2) search and screen literature systematically; (3) define terms precisely.

### 1.1 The problem

Chloé Dubois is a master's student at the fictional Redbourne University, supervised by Dr Arjun Mehta. Her study partner is the fictional Halvorsen Engineering, a manufacturer with 600 Windows laptops managed centrally. Halvorsen applies a security baseline derived from the CIS Benchmarks and Microsoft's security baselines, yet its quarterly reports show that about a quarter of laptops drift away from it. The IT manager, Sven Halvorsen, wants to know why, because each explanation suggests a different fix.

Section one point one develops research question and literature method with a Redbourne University note Chloé Dubois can demo offline.

### 1.2 The question

Chloé asks: which device and user characteristics are associated with baseline drift on Halvorsen's laptops? She defines drift as any baseline setting differing from its required value at the monthly check.

Section one point two develops research question and literature method with a Redbourne University note Chloé Dubois can demo offline.

Under section one point two, Dr Arjun Mehta expects research claims to carry owners and dates.

Section one point two treats the problem the question as testable only when evidence and ticket IDs are recorded.

### 1.3 Literature method

She searches digital libraries with fixed terms, records the date and counts, screens titles and abstracts against inclusion criteria, and keeps a log so another person could repeat the search.

Section one point three develops research question and literature method with a Redbourne University note Chloé Dubois can demo offline.

Under section one point three, Dr Arjun Mehta expects research claims to carry owners and dates.

Section one point three treats the problem the question as testable only when evidence and ticket IDs are recorded.

### 1.4 Key sources

NIST SP 800-128 describes security-focused configuration management, including baselines and monitoring for unauthorised change. CIS Controls v8 lists secure configuration of enterprise assets as a core safeguard. Dietrich et al. (2018) show that operators often explain misconfigurations by time pressure and unclear responsibility.

Section one point four develops research question and literature method with a Redbourne University note Chloé Dubois can demo offline.

Under section one point four, Dr Arjun Mehta expects research claims to carry owners and dates.

Section one point four treats the problem the question as testable only when evidence and ticket IDs are recorded.

### 1.5 Defining terms

She distinguishes drift (a change after compliance) from never-compliant devices, which point to deployment problems rather than drift.

Section one point five develops research question and literature method with a Redbourne University note Chloé Dubois can demo offline.

Under section one point five, Dr Arjun Mehta expects research claims to carry owners and dates.

Section one point five treats the problem the question as testable only when evidence and ticket IDs are recorded.

For section one point five, Redbourne University will not accept research work without a written trail.

### Scope

The study covers laptops only, not servers or phones.

### Worked example

Dr Mehta asks why her question says "associated with" rather than "causes". Chloé explains that she will observe existing records without changing anything, so she can show association, and will discuss causation only with care.

> **Synthetic case.** Chloé, Dr Mehta, Sven and Halvorsen are synthetic.

### Errors and limits

A vague definition of drift would let the result depend on how settings are counted.

### Exercises

- **EX001 — Problem.** What operational problem started the study? *Rubric:* 3 = ~quarter of laptops drift from baseline; 2 = partial; 1 = none; 0 = none.
- **EX002 — Question wording.** State Chloé's research question. *Rubric:* 3 = characteristics associated with drift; 2 = partial; 1 = none; 0 = none.
- **EX003 — Drift definition.** How is drift defined? *Rubric:* 3 = any setting differs at monthly check; 2 = partial; 1 = none; 0 = none.
- **EX004 — Search log.** Why keep a search log? *Rubric:* 3 = repeatability; 2 = partial; 1 = none; 0 = none.
- **EX005 — SP 800-128.** What does SP 800-128 contribute? *Rubric:* 3 = baselines and change monitoring; 2 = partial; 1 = none; 0 = none.
- **EX006 — Never-compliant.** Why separate never-compliant devices? *Rubric:* 3 = deployment problem not drift; 2 = partial; 1 = none; 0 = none.
- **EX007 — Association.** Why say "associated with"? *Rubric:* 3 = observational design; 2 = partial; 1 = none; 0 = none.

### Synthesis

A precise question and repeatable search set up the study.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Systems, endpoints and hardware security: advanced seminar

### Learning outcomes

You will (1) examine endpoint baselines in depth; (2) measure drift on a small sample; (3) discuss which settings matter most.

### 2.1 Baselines

A baseline is a documented set of settings. CIS Benchmarks give consensus recommendations, DISA STIGs give stricter requirements for defence systems, and Microsoft publishes Windows security baselines. Halvorsen's baseline selects six settings: disk encryption, firewall, SMB version 1 disabled, autorun disabled, a screen lock within ten minutes and no extra local administrator users.

Section two point one develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section two point one, Dr Arjun Mehta expects systems claims to carry owners and dates.

### 2.2 Why these settings

Disk encryption protects lost laptops; the firewall limits network exposure; SMB1 is an old file-sharing protocol with known weaknesses; autorun can launch software from removable media; screen locks protect unattended devices; local administrators can change any setting.

Section two point two develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section two point two, Dr Arjun Mehta expects systems claims to carry owners and dates.

Section two point two treats baselines why these settings as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — baseline sample

```python
"""Check synthetic laptop settings against a small baseline and count drift per setting (stdlib only)."""
baseline = {"disk_encryption": "on", "firewall": "on", "smb1": "off", "autorun": "off", "screen_lock_min": 10, "local_admin_users": 0}
laptops = [
 {"disk_encryption": "on", "firewall": "on", "smb1": "off", "autorun": "off", "screen_lock_min": 10, "local_admin_users": 0},
 {"disk_encryption": "on", "firewall": "off", "smb1": "off", "autorun": "off", "screen_lock_min": 30, "local_admin_users": 1},
 {"disk_encryption": "off", "firewall": "on", "smb1": "off", "autorun": "on", "screen_lock_min": 10, "local_admin_users": 1},
 {"disk_encryption": "on", "firewall": "on", "smb1": "off", "autorun": "off", "screen_lock_min": 10, "local_admin_users": 0},
 {"disk_encryption": "on", "firewall": "on", "smb1": "on", "autorun": "off", "screen_lock_min": 15, "local_admin_users": 2},
 {"disk_encryption": "on", "firewall": "on", "smb1": "off", "autorun": "off", "screen_lock_min": 10, "local_admin_users": 0}]
def ok(k, v): return v <= baseline[k] if k in ("screen_lock_min", "local_admin_users") else v == baseline[k]
drifted = [i for i, l in enumerate(laptops) if not all(ok(k, l[k]) for k in baseline)]
print(f"laptops {len(laptops)}, fully compliant {len(laptops)-len(drifted)}, drifted {len(drifted)}")
for k in baseline:
    n = sum(not ok(k, l[k]) for l in laptops)
    if n: print(f"  {k}: {n}")
```

Run with `python3 lab_baseline.py`. Verified output:

```text
laptops 6, fully compliant 3, drifted 3
  disk_encryption: 1
  firewall: 1
  smb1: 1
  autorun: 1
  screen_lock_min: 2
  local_admin_users: 3
```

### 2.3 Reading the sample

In six sample laptops, three comply fully and three drift. Extra local administrator users appear on all three drifted laptops; other failures appear once or twice.

Section two point three develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section two point three, Dr Arjun Mehta expects systems claims to carry owners and dates.

Section two point three treats baselines why these settings as testable only when evidence and ticket IDs are recorded.

For section two point three, Redbourne University will not accept systems work without a written trail.

### 2.4 Seminar discussion

The class discusses whether local administrator rights cause drift or whether people who need admin rights also change settings for work reasons. Both are plausible, which motivates chapter 4.

Section two point four develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section two point four, Dr Arjun Mehta expects systems claims to carry owners and dates.

Section two point four treats baselines why these settings as testable only when evidence and ticket IDs are recorded.

### Impact varies

Not all drift is equally serious. A laptop without disk encryption exposes all its data if lost, while a screen lock of fifteen minutes instead of ten is a smaller change. Chloé records drift per setting so later analysis can weigh serious settings separately, and she notes that the study's main outcome treats any drift as drift, a simplification she will discuss as a limitation.

### Worked example

A classmate asks why the screen lock counts as drift when set to 15 minutes. Chloé explains the baseline requires ten minutes or less, and the definition counts any difference, though impact varies by setting.

> **Synthetic case.** Synthetic sample.

### Errors and limits

Six laptops illustrate the method; they cannot estimate rates.

### Exercises

- **EX008 — Baseline sources.** Name three baseline sources. *Rubric:* 3 = CIS, STIGs, Microsoft baselines; 2 = two; 1 = one; 0 = none.
- **EX009 — Six settings.** List Halvorsen's six settings. *Rubric:* 3 = encryption, firewall, SMB1 off, autorun off, lock ≤10, no extra admins; 2 = five; 1 = three; 0 = none.
- **EX010 — Lab result.** What did the sample show? *Rubric:* 3 = 3 compliant, 3 drifted; admin users on all 3; 2 = partial; 1 = none; 0 = none.
- **EX011 — SMB1.** Why disable SMB1? *Rubric:* 3 = old protocol with known weaknesses; 2 = partial; 1 = none; 0 = none.
- **EX012 — Admin ambiguity.** What two explanations fit the admin link? *Rubric:* 3 = admin causes drift; work needs cause both; 2 = partial; 1 = none; 0 = none.
- **EX013 — Screen lock.** Why does 15 minutes count as drift? *Rubric:* 3 = baseline requires ≤10; 2 = partial; 1 = none; 0 = none.
- **EX014 — Sample limit.** Why can the sample not estimate rates? *Rubric:* 3 = only six laptops; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know what each baseline setting protects before measuring drift.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) design an observational study; (2) address privacy and ethics; (3) plan reproducible analysis.

### 3.1 Design

Chloé uses six months of monthly compliance records for all 600 laptops, linked to device attributes: local administrator flag, location (remote or office), department and last policy refresh.

Section three point one develops study design ethics and reproducibility with a Redbourne University note Chloé Dubois can demo offline.

Under section three point one, Dr Arjun Mehta expects study claims to carry owners and dates.

Section three point one treats design ethics reproducibility variables as testable only when evidence and ticket IDs are recorded.

### 3.2 Ethics

Records link devices to users. Chloé works with pseudonymised device IDs; department is the finest grouping reported; results are never used to assess individuals. Redbourne's ethics committee and Halvorsen's data protection lead approve the plan.

Section three point two develops study design ethics and reproducibility with a Redbourne University note Chloé Dubois can demo offline.

Under section three point two, Dr Arjun Mehta expects study claims to carry owners and dates.

Section three point two treats design ethics reproducibility variables as testable only when evidence and ticket IDs are recorded.

### 3.3 Reproducibility

The analysis plan is written before data access; code runs on the extract and produces every table.

Section three point three develops study design ethics and reproducibility with a Redbourne University note Chloé Dubois can demo offline.

Under section three point three, Dr Arjun Mehta expects study claims to carry owners and dates.

Section three point three treats design ethics reproducibility variables as testable only when evidence and ticket IDs are recorded.

For section three point three, Redbourne University will not accept study work without a written trail.

### 3.4 Variables

The outcome is drift during the six months; candidate explanations are local admin, remote working and department.

Section three point four develops study design ethics and reproducibility with a Redbourne University note Chloé Dubois can demo offline.

Under section three point four, Dr Arjun Mehta expects study claims to carry owners and dates.

Section three point four treats design ethics reproducibility variables as testable only when evidence and ticket IDs are recorded.

For section three point four, Redbourne University will not accept study work without a written trail.

### 3.5 Bias

Devices replaced during the study are excluded and counted, so exclusion is visible.

Section three point five develops study design ethics and reproducibility with a Redbourne University note Chloé Dubois can demo offline.

Under section three point five, Dr Arjun Mehta expects study claims to carry owners and dates.

Section three point five treats design ethics reproducibility variables as testable only when evidence and ticket IDs are recorded.

For section three point five, Redbourne University will not accept study work without a written trail.

### Analysis plan contents

The plan lists each comparison, the statistic used, the threshold for significance and how missing values are handled. It also states what would count as evidence against each explanation. For example, if admin and non-admin devices drifted at similar rates, Explanation A would be weakened.

The plan is shared with Dr Mehta and timestamped in the university's repository before Chloé receives the full extract.

### Data storage

The extract is stored on an encrypted university drive with access limited to Chloé and Dr Mehta, and deleted after the dissertation is examined, as the approvals require.

### Consent and notice

Halvorsen informs staff through its usual privacy notice that device compliance data may be analysed in pseudonymised form for security improvement, and the works council is briefed before data are shared.

### Worked example

Halvorsen's works council asks whether results could be used to discipline staff. Chloé shows the approval terms: device-level, pseudonymised, department-level reporting only.

> **Synthetic case.** Synthetic.

### Errors and limits

Pseudonymisation reduces but does not remove re-identification risk in small departments.

### Exercises

- **EX015 — Data.** What data does the design use? *Rubric:* 3 = 6 months records for 600 laptops with attributes; 2 = partial; 1 = none; 0 = none.
- **EX016 — Pseudonymisation.** How are users protected? *Rubric:* 3 = pseudonymised IDs, department-level reporting; 2 = partial; 1 = none; 0 = none.
- **EX017 — Approvals.** Who approved the plan? *Rubric:* 3 = ethics committee, data protection lead; 2 = partial; 1 = none; 0 = none.
- **EX018 — Explanations.** Name the three candidate explanations. *Rubric:* 3 = local admin, remote, department; 2 = two; 1 = one; 0 = none.
- **EX019 — Exclusions.** How are replaced devices handled? *Rubric:* 3 = excluded and counted; 2 = partial; 1 = none; 0 = none.
- **EX020 — Works council.** What did the works council ask? *Rubric:* 3 = discipline use; 2 = partial; 1 = none; 0 = none.

### Synthesis

Design for privacy and reproducibility from the start.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Systems, endpoints and hardware security: competing explanations

### Learning outcomes

You will (1) state competing explanations with mechanisms; (2) predict observable differences; (3) plan how to tell them apart.

### 4.1 Explanation A: local admin

Users with local administrator rights can change any setting. Saltzer and Schroeder (1975) set out least privilege: each program and user should operate with the fewest privileges needed. Prediction: higher drift among admin devices.

Section four point one develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section four point one, Dr Arjun Mehta expects systems claims to carry owners and dates.

Section four point one treats explanation local admin explanation as testable only when evidence and ticket IDs are recorded.

### 4.2 Explanation B: remote working

Remote laptops may miss policy refreshes when off the corporate network. Prediction: higher drift among remote devices, especially those with old refresh dates.

Section four point two develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section four point two, Dr Arjun Mehta expects systems claims to carry owners and dates.

Section four point two treats explanation local admin explanation as testable only when evidence and ticket IDs are recorded.

For section four point two, Redbourne University will not accept systems work without a written trail.

### 4.3 Explanation C: department needs

Engineering software may require settings changes. Prediction: higher drift in the engineering department.

Section four point three develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section four point three, Dr Arjun Mehta expects systems claims to carry owners and dates.

Section four point three treats explanation local admin explanation as testable only when evidence and ticket IDs are recorded.

For section four point three, Redbourne University will not accept systems work without a written trail.

### 4.4 Overlap

Engineers are more often admins and more often remote, so explanations overlap. Chloé plans stratified comparisons.

Section four point four develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section four point four, Dr Arjun Mehta expects systems claims to carry owners and dates.

Section four point four treats explanation local admin explanation as testable only when evidence and ticket IDs are recorded.

For section four point four, Redbourne University will not accept systems work without a written trail.

### 4.5 Settings pattern

Each explanation predicts different settings: admins change many settings; missed refreshes leave settings that recently changed; engineering changes firewall rules for licence servers.

Section four point five develops systems endpoints and hardware security with a Redbourne University note Chloé Dubois can demo offline.

Under section four point five, Dr Arjun Mehta expects systems claims to carry owners and dates.

Section four point five treats explanation local admin explanation as testable only when evidence and ticket IDs are recorded.

For section four point five, Redbourne University will not accept systems work without a written trail.

### Testing the predictions

Chloé plans three comparisons: admin versus non-admin, remote versus office and engineering versus other departments. She then plans to repeat the remote comparison within admin and non-admin groups separately. If the remote effect disappears within groups, admin rights are the more likely explanation. If it persists, missed refreshes matter independently.

She also plans to examine refresh dates directly: if remote devices with recent refreshes still drift, missed refreshes cannot be the main cause.

### Rival explanations from operators

Talking briefly with two Halvorsen administrators, Chloé hears a fourth idea: a software installer used by finance resets the screen lock. She records it as a possible minor explanation for one setting.

### Limits

Some explanations may act together, so the analysis looks for patterns rather than a single cause.

### Worked example

Dr Mehta suggests writing predictions before data. Chloé adds them to the plan with dates.

> **Synthetic case.** Synthetic.

### Errors and limits

Explanations that predict the same pattern cannot be distinguished; seek distinct predictions.

### Exercises

- **EX021 — Least privilege.** Who stated the least privilege principle cited? *Rubric:* 3 = Saltzer and Schroeder 1975; 2 = partial; 1 = none; 0 = none.
- **EX022 — Remote mechanism.** What mechanism links remote work to drift? *Rubric:* 3 = missed policy refreshes; 2 = partial; 1 = none; 0 = none.
- **EX023 — Department mechanism.** Why might engineering drift more? *Rubric:* 3 = software needs settings changes; 2 = partial; 1 = none; 0 = none.
- **EX024 — Overlap.** Why are the explanations hard to separate? *Rubric:* 3 = engineers often admins and remote; 2 = partial; 1 = none; 0 = none.
- **EX025 — Distinct predictions.** How do settings patterns differ? *Rubric:* 3 = admins many; refresh recent; engineering firewall; 2 = two; 1 = one; 0 = none.
- **EX026 — Prediction timing.** Why write predictions before data? *Rubric:* 3 = avoid fitting after; 2 = partial; 1 = none; 0 = none.

### Synthesis

Competing explanations need distinct, pre-stated predictions.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write a proposal with analysis plan; (2) pilot the data extract; (3) check completeness before analysis.

### 5.1 Proposal

The proposal sets out the question, three explanations with predictions, data, ethics terms and analysis: compare drift proportions across groups with risk ratios and chi-square tests, then stratify by department.

Section five point one develops proposal and pilot with a Redbourne University note Chloé Dubois can demo offline.

Under section five point one, Dr Arjun Mehta expects proposal claims to carry owners and dates.

Section five point one treats proposal pilot extract reading as testable only when evidence and ticket IDs are recorded.

### 5.2 Pilot extract

Halvorsen's IT team provides a pilot extract of 120 laptops for one month to test the pipeline.

Section five point two develops proposal and pilot with a Redbourne University note Chloé Dubois can demo offline.

Under section five point two, Dr Arjun Mehta expects proposal claims to carry owners and dates.

Section five point two treats proposal pilot extract reading as testable only when evidence and ticket IDs are recorded.

For section five point two, Redbourne University will not accept proposal work without a written trail.

### Lab — Lab — pilot completeness

```python
"""Check completeness of a synthetic pilot extract before analysis (stdlib only)."""
rows = 120
missing = {"last_policy_refresh": 9, "local_admin_flag": 0, "location": 4, "department": 2}
for k, m in missing.items():
    print(f"{k}: {rows-m}/{rows} present ({(rows-m)/rows*100:.1f}%)")
complete = rows - 13
print(f"rows complete on all fields: {complete}/{rows} ({complete/rows*100:.1f}%)")
```

Run with `python3 lab_pilot.py`. Verified output:

```text
last_policy_refresh: 111/120 present (92.5%)
local_admin_flag: 120/120 present (100.0%)
location: 116/120 present (96.7%)
department: 118/120 present (98.3%)
rows complete on all fields: 107/120 (89.2%)
```

### 5.3 Reading completeness

Local admin flag is complete (120/120). Last policy refresh is present for 111 (92.5%), location for 116 (96.7%) and department for 118 (98.3%). Some rows miss more than one field; 107 of 120 rows (89.2%) are complete on every field.

Section five point three develops proposal and pilot with a Redbourne University note Chloé Dubois can demo offline.

Under section five point three, Dr Arjun Mehta expects proposal claims to carry owners and dates.

Section five point three treats proposal pilot extract reading as testable only when evidence and ticket IDs are recorded.

### 5.4 Fixing gaps

Missing refresh dates come from laptops that had not checked in during the month. Rather than drop them, Chloé records them as "no refresh in month", which is itself relevant to Explanation B.

Section five point four develops proposal and pilot with a Redbourne University note Chloé Dubois can demo offline.

Under section five point four, Dr Arjun Mehta expects proposal claims to carry owners and dates.

Section five point four treats proposal pilot extract reading as testable only when evidence and ticket IDs are recorded.

### 5.5 Revising the plan

The plan now states how each missing field is handled.

Section five point five develops proposal and pilot with a Redbourne University note Chloé Dubois can demo offline.

Under section five point five, Dr Arjun Mehta expects proposal claims to carry owners and dates.

Section five point five treats proposal pilot extract reading as testable only when evidence and ticket IDs are recorded.

For section five point five, Redbourne University will not accept proposal work without a written trail.

Section five point five fails closed if proposal evidence is missing rather than guessing.

### Pipeline checks

Beyond completeness, Chloé checks that device IDs are unique, that dates fall within the month and that setting values match expected formats. Two devices appear twice because they were renamed mid-month; she merges them using the pseudonymised hardware ID. These checks take a day but prevent errors that would be hard to find later.

### Pilot is not results

She does not look at drift rates by group in the pilot, so the pilot cannot influence her predictions.

### Supervisor review

Dr Mehta reviews the pilot report and confirms the missing-data rules before the full extract is requested.

### Timeline

The full extract follows two weeks later.

### Version

The plan is versioned.

### Worked example

Sven asks whether missing data biases results. Chloé shows that dropping no-refresh laptops would hide exactly the devices Explanation B is about.

> **Synthetic case.** Synthetic.

### Errors and limits

Dropping incomplete rows silently can remove the cases that matter most.

### Exercises

- **EX027 — Analysis plan.** Which tests does the plan use? *Rubric:* 3 = risk ratios, chi-square, stratification; 2 = two; 1 = one; 0 = none.
- **EX028 — Pilot size.** How large was the pilot extract? *Rubric:* 3 = 120 laptops one month; 2 = partial; 1 = none; 0 = none.
- **EX029 — Lab figures.** How many rows were complete on all fields? *Rubric:* 3 = 107/120 (89.2%); 2 = partial; 1 = none; 0 = none.
- **EX030 — Refresh gaps.** Why were refresh dates missing? *Rubric:* 3 = laptops did not check in; 2 = partial; 1 = none; 0 = none.
- **EX031 — Handling.** How were missing refresh dates recorded? *Rubric:* 3 = no refresh in month; 2 = partial; 1 = none; 0 = none.
- **EX032 — Bias.** Why not drop them? *Rubric:* 3 = they are the cases for Explanation B; 2 = partial; 1 = none; 0 = none.

### Synthesis

Pilot the data and decide missing-data rules before analysis.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) analyse drift across explanations; (2) interpret risk ratios and tests; (3) check overlap with stratification.

### 6.1 Main data

Six months for 600 laptops: 138 drifted (23%), consistent with Halvorsen's reports.

Section six point one develops data collection and analysis with a Redbourne University note Chloé Dubois can demo offline.

Under section six point one, Dr Arjun Mehta expects data claims to carry owners and dates.

Section six point one treats main data reading results as testable only when evidence and ticket IDs are recorded.

For section six point one, Redbourne University will not accept data work without a written trail.

Section six point one fails closed if data evidence is missing rather than guessing.

### Lab — Lab — competing explanations

```python
"""Compare drift rates across competing explanations with risk ratios and chi-square (stdlib only)."""
def test(name, a_drift, a_n, b_drift, b_n):
    p1, p2 = a_drift/a_n, b_drift/b_n
    tot = a_drift + b_drift; n = a_n + b_n
    chi = 0
    for d, m in ((a_drift, a_n), (b_drift, b_n)):
        for obs, exp in ((d, m*tot/n), (m-d, m*(n-tot)/n)): chi += (obs-exp)**2/exp
    print(f"{name}: {a_drift}/{a_n} ({p1*100:.1f}%) vs {b_drift}/{b_n} ({p2*100:.1f}%), RR {p1/p2:.2f}, chi2 {chi:.1f}")
test("local admin vs none", 66, 120, 72, 480)
test("remote vs office", 58, 200, 80, 400)
test("engineering dept vs other", 41, 150, 97, 450)
```

Run with `python3 lab_explain.py`. Verified output:

```text
local admin vs none: 66/120 (55.0%) vs 72/480 (15.0%), RR 3.67, chi2 86.7
remote vs office: 58/200 (29.0%) vs 80/400 (20.0%), RR 1.45, chi2 6.1
engineering dept vs other: 41/150 (27.3%) vs 97/450 (21.6%), RR 1.27, chi2 2.1
```

### 6.2 Reading results

Local admin devices drifted 55.0% versus 15.0% (risk ratio 3.67, chi-square 86.7). Remote devices drifted 29.0% versus 20.0% (RR 1.45, chi-square 6.1). Engineering drifted 27.3% versus 21.6% (RR 1.27, chi-square 2.1, below the 3.84 threshold for p < 0.05 with one degree of freedom).

Section six point two develops data collection and analysis with a Redbourne University note Chloé Dubois can demo offline.

Under section six point two, Dr Arjun Mehta expects data claims to carry owners and dates.

Section six point two treats main data reading results as testable only when evidence and ticket IDs are recorded.

### 6.3 Stratification

Within non-admin devices, remote and office drift rates are close; within admin devices, both are high. This suggests the remote effect partly reflects admin rights.

Section six point three develops data collection and analysis with a Redbourne University note Chloé Dubois can demo offline.

Under section six point three, Dr Arjun Mehta expects data claims to carry owners and dates.

Section six point three treats main data reading results as testable only when evidence and ticket IDs are recorded.

For section six point three, Redbourne University will not accept data work without a written trail.

### 6.4 Settings pattern

Admin devices drifted on many settings, matching Explanation A's prediction.

Section six point four develops data collection and analysis with a Redbourne University note Chloé Dubois can demo offline.

Under section six point four, Dr Arjun Mehta expects data claims to carry owners and dates.

Section six point four treats main data reading results as testable only when evidence and ticket IDs are recorded.

For section six point four, Redbourne University will not accept data work without a written trail.

Section six point four fails closed if data evidence is missing rather than guessing.

### 6.5 Conclusion

Local admin rights are the strongest association; remote working adds little once admin rights are considered; department shows no clear association.

Section six point five develops data collection and analysis with a Redbourne University note Chloé Dubois can demo offline.

Under section six point five, Dr Arjun Mehta expects data claims to carry owners and dates.

Section six point five treats main data reading results as testable only when evidence and ticket IDs are recorded.

For section six point five, Redbourne University will not accept data work without a written trail.

### Effect size and significance

A chi-square test says whether a difference is unlikely by chance; the risk ratio says how large it is. The admin difference is both large and clear. The remote difference is smaller and, after stratification, mostly explained by admin rights. Chloé reports both measures so readers can judge importance, not only significance.

She also notes that with 600 devices, even small differences can reach significance, so effect sizes matter more for decisions.

### The finance installer

The fourth explanation is confirmed for one setting: finance laptops show screen lock drift after the installer runs. Halvorsen asks the vendor for a fix.

### Robustness

Excluding devices with any missing field changes the admin risk ratio only slightly, supporting the main finding.

### Reporting

Results go to Sven in a short memo.

### Archive

Outputs are archived.

### Worked example

Sven asks what to do. Chloé suggests removing standing local admin rights and providing a request process for temporary elevation, then re-measuring.

> **Synthetic case.** Synthetic.

### Errors and limits

Association does not prove that removing admin rights will reduce drift; re-measure after change.

### Exercises

- **EX033 — Overall drift.** What overall drift rate was observed? *Rubric:* 3 = 138/600 (23%); 2 = partial; 1 = none; 0 = none.
- **EX034 — Admin result.** Report the admin comparison. *Rubric:* 3 = 55% vs 15%, RR 3.67, chi2 86.7; 2 = two; 1 = one; 0 = none.
- **EX035 — Department result.** Why is the department result not significant? *Rubric:* 3 = chi2 2.1 below 3.84; 2 = partial; 1 = none; 0 = none.
- **EX036 — Stratified finding.** What did stratification show about remote work? *Rubric:* 3 = effect largely reflects admin rights; 2 = partial; 1 = none; 0 = none.
- **EX037 — Recommendation.** What did Chloé recommend? *Rubric:* 3 = remove standing admin, temporary elevation, re-measure; 2 = two; 1 = one; 0 = none.
- **EX038 — Caution.** What caution applies? *Rubric:* 3 = association not proof; 2 = partial; 1 = none; 0 = none.

### Synthesis

Compare explanations directly and check overlap before concluding.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) write findings clearly; (2) state limitations honestly; (3) connect to literature and practice.

### 7.1 Structure

The dissertation follows question, literature, design, results and discussion, with each figure traceable to code.

Section seven point one develops dissertation writing and limitations with a Redbourne University note Chloé Dubois can demo offline.

Under section seven point one, Dr Arjun Mehta expects dissertation claims to carry owners and dates.

Section seven point one treats structure linking literature limitations as testable only when evidence and ticket IDs are recorded.

For section seven point one, Redbourne University will not accept dissertation work without a written trail.

### 7.2 Linking literature

The admin finding supports least privilege (Saltzer and Schroeder, 1975) and CIS Controls v8 safeguards on administrative privileges; the operator perspective in Dietrich et al. (2018) helps explain why admin rights were granted widely.

Section seven point two develops dissertation writing and limitations with a Redbourne University note Chloé Dubois can demo offline.

Under section seven point two, Dr Arjun Mehta expects dissertation claims to carry owners and dates.

Section seven point two treats structure linking literature limitations as testable only when evidence and ticket IDs are recorded.

### 7.3 Limitations

One organisation; six months; observational design; monthly checks miss changes reverted within a month.

Section seven point three develops dissertation writing and limitations with a Redbourne University note Chloé Dubois can demo offline.

Under section seven point three, Dr Arjun Mehta expects dissertation claims to carry owners and dates.

Section seven point three treats structure linking literature limitations as testable only when evidence and ticket IDs are recorded.

For section seven point three, Redbourne University will not accept dissertation work without a written trail.

### 7.4 Practice implications

Halvorsen can reduce standing admin rights and should re-measure drift after six months.

Section seven point four develops dissertation writing and limitations with a Redbourne University note Chloé Dubois can demo offline.

Under section seven point four, Dr Arjun Mehta expects dissertation claims to carry owners and dates.

Section seven point four treats structure linking literature limitations as testable only when evidence and ticket IDs are recorded.

For section seven point four, Redbourne University will not accept dissertation work without a written trail.

### 7.5 Writing style

Chloé reports counts with percentages and avoids causal language.

Section seven point five develops dissertation writing and limitations with a Redbourne University note Chloé Dubois can demo offline.

Under section seven point five, Dr Arjun Mehta expects dissertation claims to carry owners and dates.

Section seven point five treats structure linking literature limitations as testable only when evidence and ticket IDs are recorded.

For section seven point five, Redbourne University will not accept dissertation work without a written trail.

Section seven point five fails closed if dissertation evidence is missing rather than guessing.

### Presenting results

Chloé presents results in a table with groups, counts, percentages, risk ratios and test statistics, followed by a short paragraph interpreting each. She adds a figure showing drift by setting for admin and non-admin devices, which makes the pattern easier to see.

Each table has a note stating the data period and that devices are pseudonymised.

### Contribution

The dissertation contributes a measured comparison of three common explanations at one organisation and a reusable analysis plan for others.

### Reader testing

She asks Sven to read the discussion and confirm that practical implications are clear for an IT manager.

### Word budget

She keeps the discussion within the word limit by cutting background that does not support the argument.

### Ethics statement

The dissertation includes an ethics statement describing approvals, pseudonymisation, department-level reporting and data deletion, so readers can judge how participants were protected.

### Final checks

Before submission, Chloé re-runs all code from a clean copy and confirms every number in the text matches the outputs. She also asks a classmate to read the limitations section for clarity.

### Worked example

Dr Mehta notices a sentence saying admin rights "cause" drift. Chloé changes it to "are strongly associated with".

> **Synthetic case.** Synthetic.

### Errors and limits

Limitations written last are often weak; draft them alongside results.

### Exercises

- **EX039 — Literature link.** Which sources support the admin finding? *Rubric:* 3 = Saltzer-Schroeder, CIS Controls v8; 2 = partial; 1 = none; 0 = none.
- **EX040 — Dietrich role.** How does Dietrich et al. (2018) help? *Rubric:* 3 = explains why admin rights were granted; 2 = partial; 1 = none; 0 = none.
- **EX041 — Limitations.** List the four limitations. *Rubric:* 3 = one org, six months, observational, monthly checks; 2 = three; 1 = two; 0 = none.
- **EX042 — Monthly gap.** What do monthly checks miss? *Rubric:* 3 = changes reverted within a month; 2 = partial; 1 = none; 0 = none.
- **EX043 — Wording fix.** How was the causal sentence fixed? *Rubric:* 3 = strongly associated with; 2 = partial; 1 = none; 0 = none.
- **EX044 — Next step.** What should Halvorsen do next? *Rubric:* 3 = reduce admin, re-measure; 2 = partial; 1 = none; 0 = none.

### Synthesis

Write clearly, link to literature and state limits honestly.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) undergo independent review; (2) defend findings; (3) plan follow-up.

### 8.1 Independent review

A second examiner re-runs the analysis from the code and extract and obtains the same tables.

Section eight point one develops independent review and defense with a Redbourne University note Chloé Dubois can demo offline.

Under section eight point one, Dr Arjun Mehta expects independent claims to carry owners and dates.

Section eight point one treats independent review defense questions as testable only when evidence and ticket IDs are recorded.

For section eight point one, Redbourne University will not accept independent work without a written trail.

### 8.2 Defense questions

Examiners ask about the remote result, missing data and generalisation.

Section eight point two develops independent review and defense with a Redbourne University note Chloé Dubois can demo offline.

Under section eight point two, Dr Arjun Mehta expects independent claims to carry owners and dates.

Section eight point two treats independent review defense questions as testable only when evidence and ticket IDs are recorded.

For section eight point two, Redbourne University will not accept independent work without a written trail.

Section eight point two fails closed if independent evidence is missing rather than guessing.

### 8.3 Answers

Chloé explains the stratified comparison, the no-refresh coding and that results apply to centrally managed fleets similar to Halvorsen.

Section eight point three develops independent review and defense with a Redbourne University note Chloé Dubois can demo offline.

Under section eight point three, Dr Arjun Mehta expects independent claims to carry owners and dates.

Section eight point three treats independent review defense questions as testable only when evidence and ticket IDs are recorded.

For section eight point three, Redbourne University will not accept independent work without a written trail.

### 8.4 Follow-up

Halvorsen removes standing admin rights from 120 devices; a follow-up six months later will test whether drift falls.

Section eight point four develops independent review and defense with a Redbourne University note Chloé Dubois can demo offline.

Under section eight point four, Dr Arjun Mehta expects independent claims to carry owners and dates.

Section eight point four treats independent review defense questions as testable only when evidence and ticket IDs are recorded.

For section eight point four, Redbourne University will not accept independent work without a written trail.

### 8.5 Reflection

Pre-stated predictions kept the analysis focused.

Section eight point five develops independent review and defense with a Redbourne University note Chloé Dubois can demo offline.

Under section eight point five, Dr Arjun Mehta expects independent claims to carry owners and dates.

Section eight point five treats independent review defense questions as testable only when evidence and ticket IDs are recorded.

For section eight point five, Redbourne University will not accept independent work without a written trail.

Section eight point five fails closed if independent evidence is missing rather than guessing.

### What the examiners valued

Examiners praise the pre-registered predictions, the stratified analysis and the honest treatment of missing data. They suggest that a follow-up could measure drift weekly rather than monthly to capture short changes, and that interviewing users could explain why admin rights were requested in the first place.

Chloé incorporates these suggestions into her future work section.

### Course review

The course moved from a practical question through literature, baselines, design and ethics, competing explanations, pilot, analysis, writing and defense, each step building on the last.

### Sharing with Halvorsen

Chloé presents a short summary to Halvorsen's IT team, focusing on the admin finding, the finance installer and the re-measurement plan.

### Data deletion

After examination, the extract is deleted as agreed, and the deletion is confirmed in writing to Halvorsen.

### Thanks

She thanks Dr Mehta, Sven and the IT team.

### Publication

With Dr Mehta, Chloé plans a short practitioner article summarising the admin finding for IT managers, using only aggregate figures.

### Next steps

Chloé hopes to run the follow-up study with Halvorsen and compare drift before and after admin rights were removed.

### Worked example

An examiner asks whether users resisted. Chloé reports that Halvorsen added a same-day elevation process, which reduced complaints.

> **Synthetic case.** Synthetic.

### Errors and limits

A defense is stronger when weaknesses are named before examiners raise them.

### Exercises

- **EX045 — Reproduction.** How was the analysis independently checked? *Rubric:* 3 = examiner re-ran code; 2 = partial; 1 = none; 0 = none.
- **EX046 — Questions.** Which topics did examiners raise? *Rubric:* 3 = remote result, missing data, generalisation; 2 = two; 1 = one; 0 = none.
- **EX047 — Scope of findings.** To which organisations do findings apply? *Rubric:* 3 = centrally managed similar fleets; 2 = partial; 1 = none; 0 = none.
- **EX048 — Follow-up.** What follow-up is planned? *Rubric:* 3 = remove admin from 120, re-measure in six months; 2 = partial; 1 = none; 0 = none.
- **EX049 — Resistance.** How was user resistance handled? *Rubric:* 3 = same-day elevation; 2 = partial; 1 = none; 0 = none.
- **EX050 — Lesson.** What kept the analysis focused? *Rubric:* 3 = pre-stated predictions; 2 = partial; 1 = none; 0 = none.

### Synthesis

Independent reproduction and honest answers strengthen a defense.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Chloé Dubois, Dr Arjun Mehta, Redbourne University, Halvorsen Engineering and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** About a quarter of laptops drift from the security baseline.

**EX002.** Which device and user characteristics are associated with baseline drift.

**EX003.** Any baseline setting differing from its required value at the monthly check.

**EX004.** So another person could repeat the search.

**EX005.** Guidance on baselines and monitoring for unauthorised change.

**EX006.** They indicate deployment problems rather than drift.

**EX007.** The design observes records, showing association rather than causation.

**EX008.** CIS Benchmarks, DISA STIGs and Microsoft security baselines.

**EX009.** Disk encryption, firewall, SMB1 off, autorun off, lock within 10 minutes, no extra local admins.

**EX010.** Three compliant, three drifted, with extra admin users on all drifted laptops.

**EX011.** It is an old protocol with known weaknesses.

**EX012.** Admin rights enable drift, or work needs drive both admin rights and setting changes.

**EX013.** The baseline requires ten minutes or less.

**EX014.** It has only six laptops.

**EX015.** Six months of compliance records for 600 laptops with attributes.

**EX016.** Pseudonymised IDs and department-level reporting.

**EX017.** Redbourne's ethics committee and Halvorsen's data protection lead.

**EX018.** Local admin rights, remote working and department.

**EX019.** Excluded and counted.

**EX020.** Whether results could be used to discipline staff.

**EX021.** Saltzer and Schroeder (1975).

**EX022.** Missed policy refreshes off the network.

**EX023.** Engineering software may require settings changes.

**EX024.** Engineers are more often admins and remote.

**EX025.** Admins change many; missed refresh leaves recent changes; engineering changes firewall rules.

**EX026.** To avoid fitting explanations to results.

**EX027.** Risk ratios and chi-square tests with stratification by department.

**EX028.** 120 laptops for one month.

**EX029.** 107 of 120 (89.2%).

**EX030.** The laptops had not checked in during the month.

**EX031.** As "no refresh in month".

**EX032.** They are exactly the devices Explanation B concerns.

**EX033.** 138 of 600, 23%.

**EX034.** 55.0% vs 15.0%, RR 3.67, chi-square 86.7.

**EX035.** Chi-square 2.1 is below 3.84.

**EX036.** The remote effect partly reflects admin rights.

**EX037.** Remove standing admin rights, allow temporary elevation, re-measure.

**EX038.** Association does not prove removal will reduce drift.

**EX039.** Saltzer and Schroeder (1975) and CIS Controls v8.

**EX040.** It helps explain why admin rights were granted widely.

**EX041.** One organisation, six months, observational, monthly checks miss short changes.

**EX042.** Changes reverted within a month.

**EX043.** Changed to "are strongly associated with".

**EX044.** Reduce standing admin rights and re-measure drift.

**EX045.** A second examiner re-ran the code and obtained the same tables.

**EX046.** The remote result, missing data and generalisation.

**EX047.** Centrally managed fleets similar to Halvorsen.

**EX048.** Remove admin rights from 120 devices and re-measure after six months.

**EX049.** A same-day elevation process.

**EX050.** Pre-stated predictions.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Center for Internet Security. (n.d.). *CIS Benchmarks*. <https://www.cisecurity.org/cis-benchmarks>
- Center for Internet Security. (2021). *CIS Critical Security Controls v8*. <https://www.cisecurity.org/controls/v8>
- Cooper, D., Polk, W., Regenscheid, A., & Souppaya, M. (2011). *BIOS protection guidelines* (NIST SP 800-147). NIST. <https://doi.org/10.6028/NIST.SP.800-147>
- Defense Information Systems Agency. (n.d.). *Security Technical Implementation Guides (STIGs)*. <https://public.cyber.mil/stigs/>
- Dietrich, C., Krombholz, K., Borgolte, K., & Fiebig, T. (2018). Investigating system operators' perspective on security misconfigurations. *2018 ACM SIGSAC Conference on Computer and Communications Security (CCS '18)*, 1272–1289. <https://doi.org/10.1145/3243734.3243794>
- Forrest, S., Hofmeyr, S. A., Somayaji, A., & Longstaff, T. A. (1996). A sense of self for Unix processes. *1996 IEEE Symposium on Security and Privacy*, 120–128. <https://doi.org/10.1109/SECPRI.1996.502675>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Johnson, A., Dempsey, K., Ross, R., Gupta, S., & Bailey, D. (2011, updated 2019). *Guide for security-focused configuration management of information systems* (NIST SP 800-128). NIST. <https://doi.org/10.6028/NIST.SP.800-128>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Kent, K., & Souppaya, M. (2006). *Guide to computer security log management* (NIST SP 800-92). NIST. <https://doi.org/10.6028/NIST.SP.800-92>
- Kernel development community. (n.d.). *Kernel self-protection*. <https://www.kernel.org/doc/html/latest/security/self-protection.html>
- Kim, Y., Daly, R., Kim, J., Fallin, C., Lee, J. H., Lee, D., Wilkerson, C., Lai, K., & Mutlu, O. (2014). Flipping bits in memory without accessing them: An experimental study of DRAM disturbance errors. *41st International Symposium on Computer Architecture (ISCA)*, 361–372. <https://doi.org/10.1109/ISCA.2014.6853210>
- Kocher, P., Horn, J., Fogh, A., Genkin, D., Gruss, D., Haas, W., Hamburg, M., Lipp, M., Mangard, S., Prescher, T., Schwarz, M., & Yarom, Y. (2019). Spectre attacks: Exploiting speculative execution. *2019 IEEE Symposium on Security and Privacy*, 1–19. <https://doi.org/10.1109/SP.2019.00002>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Li, F., & Paxson, V. (2017). A large-scale empirical study of security patches. *2017 ACM SIGSAC Conference on Computer and Communications Security (CCS '17)*, 2201–2215. <https://doi.org/10.1145/3133956.3134072>
- Microsoft. (n.d.). *Windows security baselines*. <https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines>
- Microsoft. (n.d.). *BitLocker overview*. <https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/>
- Microsoft. (n.d.). *Application Control for Windows*. <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol>
- Nappa, A., Johnson, R., Bilge, L., Caballero, J., & Dumitraș, T. (2015). The attack of the clones: A study of the impact of shared code on vulnerability patching. *2015 IEEE Symposium on Security and Privacy*, 692–708. <https://doi.org/10.1109/SP.2015.48>
- Regenscheid, A. (2018). *Platform firmware resiliency guidelines* (NIST SP 800-193). NIST. <https://doi.org/10.6028/NIST.SP.800-193>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Scarfone, K., Jansen, W., & Tracy, M. (2008). *Guide to general server security* (NIST SP 800-123). NIST. <https://doi.org/10.6028/NIST.SP.800-123>
- Souppaya, M., & Scarfone, K. (2013). *Guide to malware incident prevention and handling for desktops and laptops* (NIST SP 800-83 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-83r1>
- Souppaya, M., & Scarfone, K. (2022). *Guide to enterprise patch management planning: Preventive maintenance for technology* (NIST SP 800-40 Rev. 4). NIST. <https://doi.org/10.6028/NIST.SP.800-40r4>
