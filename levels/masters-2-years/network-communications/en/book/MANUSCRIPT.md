# Network and Communications Security: Master's Course

- Language: English (`en`); course 172, Master's course (2 years).
- Editorial state: **published**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students researching network detection quality who must design, govern and defend an applied study with an industry partner.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only networks and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, flow records, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one master's student studying intrusion detection alert tuning at a fictional logistics company, from question and literature method through the base-rate problem, study design and ethics, competing explanations, proposal and pilot, data analysis, dissertation writing and an independent review and viva. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Amara Okoye** | Master's student | Invented |
| **Dr Felix Brandt** | Supervisor | Invented |
| **Easterly University** | Fictional university | Invented |
| **Corvane Logistics** | Fictional partner (two data centres) | Invented |

### Core sources

NIST [SP 800-41r1](https://doi.org/10.6028/NIST.SP.800-41r1), [SP 800-77r1](https://doi.org/10.6028/NIST.SP.800-77r1), [SP 800-94](https://doi.org/10.6028/NIST.SP.800-94), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-153](https://doi.org/10.6028/NIST.SP.800-153) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); [CIS Controls v8](https://www.cisecurity.org/controls/v8); IETF [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), [RFC 4301](https://www.rfc-editor.org/rfc/rfc4301) and [RFC 2827](https://www.rfc-editor.org/rfc/rfc2827). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) frame a master's question about intrusion detection alert quality; (2) search and screen literature systematically; (3) define measures.

### 1.1 The case

Amara Okoye is a master's student at the fictional Easterly University, supervised by Dr Felix Brandt. Her industry partner is the fictional Corvane Logistics, whose small security team receives over four thousand network intrusion detection alerts a week from sensors at its two data centres. Analysts admit they skim most alerts and close them in bulk. Amara's dissertation asks a focused question: can documented tuning of the alert rules cut alert volume substantially while keeping nearly all detections of the events the team cares about? The question matters because an analyst who ignores most alerts will eventually ignore an important one.

### 1.2 Literature method

Amara searches two digital libraries and the NIST publications site with fixed search strings, records the number of results, and screens titles and abstracts against written inclusion criteria: empirical or authoritative work on network intrusion detection, alert quality or tuning. She keeps a log of every decision so another student could repeat the search. Core sources emerge quickly: NIST SP 800-94 on intrusion detection and prevention systems, Axelsson (2000) on the base-rate fallacy, Paxson's 1999 description of Bro and Sommer and Paxson (2010) on the limits of machine learning in this domain.

### 1.3 Defining the measures

Amara chooses three measures. Alert volume is alerts per week, normalised by traffic so that quieter weeks do not look like improvement. Precision is the share of alerts that correspond to events the team would act on. Recall is the share of those actionable events that produce at least one alert. Recall needs a labelled set of known events, which she builds with the team from a week of past incidents and authorised test activity recorded in their change logs, never by generating attacks herself.

### 1.4 Scope and boundaries

The study covers rule tuning only: suppressing known benign sources, adjusting thresholds and disabling rules for services Corvane does not run. It does not evaluate new detection products or machine learning. All observation uses alert exports and labelled records provided by Corvane under a data agreement; Amara does not run traffic against their sensors.

Amara's scope covers alert rules on Corvane's two sensors over a fixed period, using synthetic replays where real data cannot leave the company. It excludes endpoint tools and the response process after triage. Stating these boundaries prevents the dissertation from overclaiming and tells readers which questions remain open.

### Worked example

Amara's question statement, search log and three measure definitions fit on two pages and are approved by Dr Brandt and Corvane's security lead before data collection.

> **Synthetic case.** Amara Okoye, Easterly University, Corvane Logistics and all figures are synthetic.

### Errors and limits

Measuring only alert volume rewards switching rules off; recall must be measured alongside it.

### Exercises

- **EX001 — Why tuning matters.** Explain why bulk-closing alerts is a security risk. *Rubric:* 3 = important alerts ignored among noise;; 2 = risk;; 1 = vague;; 0 = none.
- **EX002 — Search log.** What should a literature search log record? *Rubric:* 3 = strings, sources, dates, counts, decisions;; 2 = some;; 1 = vague;; 0 = none.
- **EX003 — Normalising volume.** Why normalise alert volume by traffic? *Rubric:* 3 = traffic changes confound;; 2 = fairness;; 1 = vague;; 0 = none.
- **EX004 — Precision and recall.** Define precision and recall for alert rules. *Rubric:* 3 = both correct;; 2 = one;; 1 = vague;; 0 = none.
- **EX005 — Labelled set source.** How is the labelled event set built without attacking anything? *Rubric:* 3 = past incidents and authorised tests from records;; 2 = records;; 1 = attacks;; 0 = none.
- **EX006 — Volume-only danger.** What perverse outcome does a volume-only measure reward? *Rubric:* 3 = switching rules off;; 2 = fewer alerts;; 1 = vague;; 0 = none.
- **EX007 — Scope boundary.** Name two things outside the study's scope. *Rubric:* 3 = new products and ML;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

A precise question, a logged literature method and paired volume, precision and recall measures frame the study.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Network and communications security: advanced seminar

### Learning outcomes

You will (1) explain how network intrusion detection works; (2) analyse the base-rate problem; (3) discuss alert triage practice.

### 2.1 How detection works

Network intrusion detection systems inspect traffic or flow records and raise alerts when patterns match signatures or deviate from expected behaviour. NIST SP 800-94 distinguishes signature-based, anomaly-based and stateful protocol analysis methods. Signatures are precise for known patterns but miss novel ones; anomaly methods can find new patterns but produce more false alarms. Paxson's Bro, now Zeek, emphasised policy scripts that describe what the operator cares about, a philosophy that fits Amara's tuning focus.

For Amara, the practical consequence is that each rule's false alarms on Corvane's traffic must be measured rather than assumed from its description.

Understanding this explains why tuning matters.

### Lab — The base-rate problem

```python
"""Precision of an alert rule at different base rates (Axelsson's point), synthetic numbers (stdlib only)."""
tpr, fpr, events = 0.95, 0.01, 1_000_000
for prev in (0.1, 0.01, 0.001, 0.0001):
    tp = tpr * prev * events; fp = fpr * (1 - prev) * events
    print(f"base rate {prev:<7} true alerts {tp:9.0f} false alerts {fp:8.0f} precision {tp/(tp+fp):.3f}")
```

Run with `python3 lab_baserate.py`. Verified output:

```text
base rate 0.1     true alerts     95000 false alerts     9000 precision 0.913
base rate 0.01    true alerts      9500 false alerts     9900 precision 0.490
base rate 0.001   true alerts       950 false alerts     9990 precision 0.087
base rate 0.0001  true alerts        95 false alerts     9999 precision 0.009
```

### 2.2 Reading the base rates

With a rule that detects 95 percent of malicious events and falsely alerts on only 1 percent of benign events, precision is 0.913 when one event in ten is malicious, but only 0.009 when one in ten thousand is. Axelsson (2000) made exactly this point: in real networks malicious events are rare, so even a good detector produces mostly false alarms. Tuning that lowers the false positive rate on benign traffic therefore matters more than small gains in detection rate.

At one malicious event in ten thousand, the rule raises roughly a hundred false alerts for every true one.

### 2.3 Triage in practice

In seminar, Amara compares triage practices from published guidance and partner interviews. Effective teams group related alerts, enrich them with asset and owner information, and document why alerts are closed. Weak practice closes alerts without notes, which loses the information needed to tune rules. She notes that closure notes are also her best source of labels, linking triage quality to research quality.

Triage means deciding quickly which alerts need investigation. Analysts check the rule, the hosts involved and recent context, then close, escalate or investigate. Time pressure makes bulk closing tempting, which is the behaviour Amara's study aims to reduce.

### Flow records as a second view

Signatures inspect packet content, but much of Corvane's traffic is encrypted with TLS, which hides payloads from the sensors. Flow records, standardised as IPFIX in RFC 7011, summarise each connection by addresses, ports, timing and byte counts without content. Amara notes that flow data remain useful when payloads are encrypted, for example to see that a backup server transfers large volumes at night, and that this context helps judge alerts. It also protects privacy better than full packet capture, since it records who talked to whom rather than what was said.

### Worked example

Amara presents the base-rate table and shows that Corvane's estimated prevalence puts them close to the 0.001 row, explaining why analysts see mostly false alerts.

> **Synthetic case.** Rates are synthetic.

### Errors and limits

Quoting a detector's accuracy without the base rate misleads decision makers.

### Exercises

- **EX008 — Detection methods.** Contrast signature and anomaly detection in two sentences. *Rubric:* 3 = strengths and weaknesses of both;; 2 = definitions;; 1 = vague;; 0 = none.
- **EX009 — Precision collapse.** Using the lab, state precision at base rates 0.01 and 0.0001. *Rubric:* 3 = 0.490 and 0.009;; 2 = one;; 1 = vague;; 0 = none.
- **EX010 — Tuning priority.** Why does lowering false positive rate matter more than raising detection rate here? *Rubric:* 3 = base rate effect;; 2 = noise;; 1 = vague;; 0 = none.
- **EX011 — Closure notes.** Why are closure notes valuable for research? *Rubric:* 3 = source of labels and tuning info;; 2 = records;; 1 = vague;; 0 = none.
- **EX012 — Enrichment.** How does asset enrichment help triage? *Rubric:* 3 = context on importance and owner;; 2 = context;; 1 = vague;; 0 = none.
- **EX013 — Policy philosophy.** What did Bro's design emphasise? *Rubric:* 3 = operator-defined policy scripts;; 2 = policy;; 1 = vague;; 0 = none.
- **EX014 — Prevalence estimate.** Why does Corvane's prevalence near 0.001 explain analyst experience? *Rubric:* 3 = precision about 0.09;; 2 = mostly false;; 1 = vague;; 0 = none.

### Synthesis

Low base rates make false positive control the central problem of alert quality.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) design a before-after study with controls; (2) secure ethics and data agreements; (3) plan reproducible analysis.

### 3.1 Design

Amara uses an interrupted time-series design: four weeks before tuning and four weeks after, measuring alerts per hundred gigabytes, precision and recall each week. A true randomised design is impossible because tuning applies to the whole sensor estate, so she strengthens inference by normalising for traffic, recording all other changes during the period and testing recall on the same labelled event set before and after.

The design compares alert volume and detection of key events before and after documented tuning, using the same replay set. Measures and analysis are fixed in advance.

### 3.2 Ethics and data

Alerts contain internal addresses, hostnames and sometimes usernames. Corvane exports alerts with addresses replaced by consistent pseudonyms and removes payload excerpts, which could contain personal data. Amara's ethics approval covers interviews with analysts and the use of pseudonymised alert data; no customer data are involved. Data remain on a Corvane-managed analysis machine she accesses remotely, and only aggregate results leave it.

Alerts contain addresses and hostnames that can identify staff. Amara works under a data agreement, uses synthetic replays where possible, and stores extracts securely.

### 3.3 Tuning governance

Every tuning change is proposed by Amara, reviewed by an analyst and approved by the security lead, then recorded with the rule identifier, the change and the reason. Changes that disable a rule require evidence that the protected service does not exist at Corvane. This governance prevents the study from weakening detection to improve its numbers.

Every tuning change is proposed, reviewed by a second analyst, and recorded with its reason, so no detection is removed without justification.

Changes can be reversed quickly.

### 3.4 Reproducibility

All analysis is scripted, with scripts and synthetic sample data in a repository. Each figure is generated from code, and the dissertation lists the script version for each table, so examiners can rerun the analysis on the synthetic data.

Reproducibility requires that someone else could repeat the analysis and get the same result. Amara keeps the rule set versions, replay set identifiers, scripts and settings in version control, records the environment used, and writes a short guide to rerunning each step. Where company data cannot be shared, she provides synthetic data with the same structure so the method itself can be checked.

### Analysis plan

Amara writes the analysis plan before any post-tuning data exist. She will compare mean weekly alerts per hundred gigabytes before and after, report the weekly series rather than only averages, and compute precision and recall on the labelled set with the rules as configured before and after. She decides in advance that any lost detection will be investigated individually and reported, whatever the overall recall. Fixing these choices early protects the study from selecting whichever analysis happens to look best once results are visible.

### Worked example

The design document lists measures, weeks, governance steps and the change register template, approved by the security lead.

> **Synthetic case.** The design is synthetic.

### Errors and limits

Before-after designs are vulnerable to coincident changes; record everything else that changes.

### Exercises

- **EX015 — Time-series design.** Why use four weeks either side? *Rubric:* 3 = capture weekly variation;; 2 = more data;; 1 = vague;; 0 = none.
- **EX016 — Payload removal.** Why remove payload excerpts from exports? *Rubric:* 3 = may contain personal data;; 2 = privacy;; 1 = vague;; 0 = none.
- **EX017 — Disabling evidence.** What evidence is required to disable a rule? *Rubric:* 3 = service absent at Corvane;; 2 = justification;; 1 = vague;; 0 = none.
- **EX018 — Governance purpose.** How does tuning governance protect validity? *Rubric:* 3 = prevents gaming metrics by weakening detection;; 2 = oversight;; 1 = vague;; 0 = none.
- **EX019 — Data location.** Why keep data on a Corvane machine? *Rubric:* 3 = control and minimisation;; 2 = security;; 1 = vague;; 0 = none.
- **EX020 — Coincident changes.** Give an example of a coincident change to record. *Rubric:* 3 = sensor upgrade or traffic shift;; 2 = example;; 1 = vague;; 0 = none.

### Synthesis

A governed, normalised before-after design with reproducible scripts is credible within its limits.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Network and communications security: competing explanations

### Learning outcomes

You will (1) identify alternative explanations for falling alerts; (2) test them with data; (3) report honestly.

### 4.1 Why alternatives matter

If alerts fall after tuning, tuning is the obvious explanation but not the only one. Traffic might have dropped, a sensor might have failed, a noisy server might have been retired, or analysts might have changed how alerts are exported. A dissertation that ignores these risks claiming an effect that is not there.

A drop in alerts could come from tuning, but also from lower traffic, a holiday period or a sensor outage. Ruling these out strengthens the claim.

Each is checked in turn.

### Lab — Normalising by traffic

```python
"""Alerts per 100 GB of traffic over 8 weeks, to separate tuning from traffic changes (synthetic, stdlib only)."""
alerts = [4210, 4050, 4390, 4120, 1180, 1090, 1240, 1150]
gb = [820, 790, 860, 805, 610, 590, 640, 600]
for w, (a, g) in enumerate(zip(alerts, gb), 1):
    print(f"week {w} {'pre ' if w<=4 else 'post'} alerts {a:5d} traffic {g:4d} GB  per100GB {a/g*100:6.1f}")
pre = sum(a/g for a, g in zip(alerts[:4], gb[:4]))/4*100; post = sum(a/g for a, g in zip(alerts[4:], gb[4:]))/4*100
print(f"mean per100GB pre {pre:.1f} post {post:.1f}; traffic fell {1-sum(gb[4:])/sum(gb[:4]):.1%}")
```

Run with `python3 lab_normalise.py`. Verified output:

```text
week 1 pre  alerts  4210 traffic  820 GB  per100GB  513.4
week 2 pre  alerts  4050 traffic  790 GB  per100GB  512.7
week 3 pre  alerts  4390 traffic  860 GB  per100GB  510.5
week 4 pre  alerts  4120 traffic  805 GB  per100GB  511.8
week 5 post alerts  1180 traffic  610 GB  per100GB  193.4
week 6 post alerts  1090 traffic  590 GB  per100GB  184.7
week 7 post alerts  1240 traffic  640 GB  per100GB  193.8
week 8 post alerts  1150 traffic  600 GB  per100GB  191.7
mean per100GB pre 512.1 post 190.9; traffic fell 25.5%
```

### 4.2 Reading the normalised series

Raw alerts fall from about 4,200 to 1,200 per week, a 72 percent drop. But traffic also fell by 25.5 percent in the post period, because a seasonal customer moved to another provider. Normalised alerts fall from 512 to 191 per hundred gigabytes, still a large reduction, so traffic explains only part of the raw change. The weekly series also shows a sharp step at week five, matching the tuning date, rather than a gradual decline.

Raw counts alone would credit tuning with the whole 72 percent drop; normalising separates out the volume lost with the departed customer.

Normalising per unit of traffic removes volume effects.

### 4.3 Testing other explanations

Sensor health logs show no outages. The change register shows no export changes. One noisy server was retired in week six, after the step, so it cannot explain the week-five change. Amara records each explanation, the evidence checked and her conclusion in a table.

Amara tests each alternative explanation against the evidence. She compares traffic volume, sensor uptime and calendar periods across the before and after windows, and checks whether alert volume changed on rules that were not tuned. If untuned rules stayed stable while tuned rules fell, tuning becomes the most plausible explanation.

### Analyst behaviour

One more explanation is harder to test: analysts might close or escalate alerts differently once they know a study is running, which could change closure notes and therefore labels. Amara addresses this by fixing the labelled set before tuning, using records from earlier weeks, so labels cannot be influenced by the study. She also compares the share of alerts closed without notes before and after; it falls slightly, which suggests analysts write better notes now that volume is lower, a welcome side effect but one she reports as a possible bias in later label sets.

### Worked example

The competing explanations table has five rows: traffic, sensor failure, retired server, export change and analyst behaviour, each with evidence and verdict.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Normalising by the wrong denominator, such as hosts instead of traffic, can create or hide effects.

### Exercises

- **EX021 — Alternative list.** List four alternative explanations for falling alerts. *Rubric:* 3 = four;; 2 = three;; 1 = fewer;; 0 = none.
- **EX022 — Normalised result.** State the normalised change. *Rubric:* 3 = 512 to 191 per 100 GB;; 2 = direction;; 1 = vague;; 0 = none.
- **EX023 — Step timing.** Why does the week-five step support the tuning explanation? *Rubric:* 3 = coincides with change date;; 2 = timing;; 1 = vague;; 0 = none.
- **EX024 — Retired server.** Why can the retired server not explain the step? *Rubric:* 3 = retired after the step;; 2 = timing;; 1 = vague;; 0 = none.
- **EX025 — Denominator choice.** Why might hosts be a poor denominator? *Rubric:* 3 = alerts track traffic not hosts;; 2 = mismatch;; 1 = vague;; 0 = none.
- **EX026 — Evidence table.** What columns does the explanations table need? *Rubric:* 3 = explanation, evidence, verdict;; 2 = two;; 1 = vague;; 0 = none.

### Synthesis

Testing alternatives shows the tuning explanation survives, with traffic accounting for part of the raw drop.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write the dissertation proposal; (2) pilot tuning on one sensor; (3) refine the procedure.

### 5.1 Proposal

The proposal states the question, measures, design, governance, ethics and analysis plan. It sets success criteria in advance: at least a 50 percent reduction in normalised alert volume with recall no lower than 0.90 on the labelled set.

Fixing recall at no lower than 0.90 stops a large volume cut from being bought by silencing rules that catch real attacks.

The proposal sets out the question, design, measures, timeline, risks and data handling, and is approved by her supervisor and Corvane before work begins. It becomes the reference against which later changes are judged, and any departure is recorded with a reason.

### 5.2 Pilot sensor

Tuning is piloted on one sensor for two weeks. Amara reviews the top twenty noisiest rules by volume, consulting closure notes. Most noise comes from three sources: a backup server's scheduled transfers matching a data-exfiltration rule, a monitoring system's scans of its own hosts and rules for services Corvane does not run.

The pilot uses one sensor in one data centre, limiting impact if tuning removes something important, while giving realistic evidence.

Analysts on that sensor agree to report anything unusual.

### 5.3 Pilot changes

The backup server and monitoring system are added as documented exceptions to the specific rules they trigger, not globally. Rules for absent services are disabled with evidence. Thresholds for one scanning rule are raised from five to twenty connections per minute after analysts confirm legitimate tools exceed five.

Each pilot change is logged with the rule, the reason, the reviewer and the expected effect, then compared with what actually happened.

Unexpected effects are reviewed before further changes.

Patterns guide rollout.

### 5.4 Pilot lessons

The pilot shows that exceptions must be narrow: an early draft exempted the backup server from all rules, which reviewers rejected. The procedure is revised to require rule-specific exceptions with an expiry date.

The pilot showed which parts of the method worked and which needed revision. Amara records lessons such as rules whose tuning needed more context than expected, and adjusts the procedure for the full rollout. Lessons are written down promptly with evidence, so the rollout plan is based on what happened rather than on recollection.

### Choosing what to tune first

With hundreds of rules, Amara needs an order. She ranks rules by alert volume and by how often their alerts were closed as benign, focusing first on rules that are both noisy and almost always benign. Rules that fire rarely but are sometimes real are left alone, even if they produce occasional false alarms, because the cost of missing their true detections is high. This ordering puts the analysts' effort where it reduces the most noise for the least risk, and it makes each change easy to justify in the register.

### Worked example

The pilot sensor's normalised alerts fall by 64 percent with no labelled event missed.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Global exceptions for noisy hosts create blind spots if those hosts are compromised.

### Exercises

- **EX027 — Success criteria.** State the two success criteria. *Rubric:* 3 = both;; 2 = one;; 1 = vague;; 0 = none.
- **EX028 — Noise sources.** Name the three main noise sources. *Rubric:* 3 = three;; 2 = two;; 1 = one;; 0 = none.
- **EX029 — Narrow exceptions.** Why reject a global exception for the backup server? *Rubric:* 3 = blind spot if compromised;; 2 = too broad;; 1 = vague;; 0 = none.
- **EX030 — Threshold change.** What justified raising the scanning threshold? *Rubric:* 3 = analyst confirmation legitimate tools exceed five;; 2 = evidence;; 1 = vague;; 0 = none.
- **EX031 — Expiry dates.** Why give exceptions expiry dates? *Rubric:* 3 = force review;; 2 = review;; 1 = vague;; 0 = none.
- **EX032 — Pilot result.** What was the pilot result? *Rubric:* 3 = 64% reduction, no missed events;; 2 = reduction;; 1 = vague;; 0 = none.

### Synthesis

The pilot refines tuning into narrow, documented, expiring changes.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) apply tuning estate-wide; (2) measure precision and recall; (3) analyse results.

### 6.1 Rollout

After the pilot, the revised procedure is applied to all sensors in week five, with each change in the register. Amara collects four weeks of post-tuning data.

The rollout extends tuning to both sensors in planned stages, using the revised procedure from the pilot. Each stage has the same review and logging, plus checks that alert volume and key detections behave as expected. Analysts are briefed before each stage, and any surprising drop in a rule's alerts is investigated before the next stage begins.

### Lab — Precision and recall

```python
"""Alert counts and recall on a labelled synthetic week, before and after tuning (stdlib only)."""
before = {"alerts": 4210, "true": 38, "labelled_true_events": 40}
after = {"alerts": 1180, "true": 37, "labelled_true_events": 40}
for k, d in (("before", before), ("after", after)):
    print(f"{k:6} alerts {d['alerts']:5d}  precision {d['true']/d['alerts']:.3f}  recall {d['true']/d['labelled_true_events']:.3f}")
print(f"alert reduction {1-after['alerts']/before['alerts']:.1%}; true detections lost {before['true']-after['true']}")
```

Run with `python3 lab_tuning.py`. Verified output:

```text
before alerts  4210  precision 0.009  recall 0.950
after  alerts  1180  precision 0.031  recall 0.925
alert reduction 72.0%; true detections lost 1
```

### 6.2 Reading the result

Alerts fall 72 percent in raw terms. Precision rises from 0.009 to 0.031, meaning analysts now see about three actionable alerts per hundred instead of one. Recall falls from 0.950 to 0.925: one labelled event that previously alerted no longer does. Both success criteria are met, but the lost detection must be examined, not hidden.

She reports both volume reduction and detection retention with intervals.

She also notes which rules drove most of the reduction, because a few noisy rules often account for most volume.

### 6.3 Examining the miss

The missed event was an authorised test of unusual file transfer from a server that the backup exception now covers. The exception was narrower than in the pilot draft but still too broad in time. Amara proposes restricting the backup exception to the scheduled backup window, and checks on the labelled set that this restores the detection without much increase in alerts.

The miss is treated as a lesson, not hidden.

Its cause informs the review procedure.

Retesting confirms the fix.

### Weekly stability

Averages can hide unstable weeks. Amara plots weekly precision and recall across the four post-tuning weeks and finds them stable, with recall at 0.925 in every week because the same labelled event is missed. Alerts per hundred gigabytes vary between about 185 and 194, a narrow band compared with the pre-tuning level above 510. This stability suggests the improvement is not an artefact of one quiet week. She also checks the four busiest rules after tuning to confirm none has become a new dominant source of noise, which would indicate a tuning change had shifted the problem rather than solved it.

### Analyst time

The practical value of tuning is analyst time. Before tuning, analysts estimated spending about two minutes per alert they actually looked at, and they looked at only a fraction. After tuning, with roughly a quarter of the volume, they report looking at most alerts and closing them with notes. Amara records these estimates from short structured interviews, treating them as self-reported and approximate. Even so, they show the direction of benefit that matters to Corvane: attention is now spread over fewer alerts, so the actionable ones are more likely to be noticed.

### Worked example

With the window restriction, recall returns to 0.950 and weekly alerts rise by only 40.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Celebrating volume reduction while ignoring a lost detection would misrepresent the result.

### Exercises

- **EX033 — Precision meaning.** Explain precision 0.031 in analyst terms. *Rubric:* 3 = about 3 per 100 actionable;; 2 = three percent;; 1 = vague;; 0 = none.
- **EX034 — Recall change.** What does recall 0.950 to 0.925 mean? *Rubric:* 3 = one fewer detected event;; 2 = lower;; 1 = vague;; 0 = none.
- **EX035 — Miss cause.** What caused the miss? *Rubric:* 3 = backup exception too broad in time;; 2 = exception;; 1 = vague;; 0 = none.
- **EX036 — Fix test.** How was the fix tested? *Rubric:* 3 = rerun on labelled set;; 2 = tested;; 1 = vague;; 0 = none.
- **EX037 — Cost of fix.** What did the fix cost in alerts? *Rubric:* 3 = about 40 per week;; 2 = small;; 1 = vague;; 0 = none.
- **EX038 — Honest reporting.** Why report the lost detection prominently? *Rubric:* 3 = integrity and improvement;; 2 = honesty;; 1 = vague;; 0 = none.

### Synthesis

Tuning met its criteria, and analysing the one miss improved the procedure further.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure the dissertation; (2) write limitations; (3) make recommendations.

### 7.1 Structure

The dissertation follows introduction, literature, method, results, competing explanations, discussion and conclusion, with appendices for the change register, scripts and synthetic data.

The dissertation follows a clear structure: introduction and question, literature, method, results, discussion, limitations and recommendations. Each chapter opens by stating its purpose and closes by linking to the next. Readers can then find what they need quickly, and examiners can check that the argument flows from question to evidence to conclusion without gaps.

Signposting helps busy readers.

### 7.2 Limitations

One organisation, eight weeks, a labelled set of forty events, and a before-after design without randomisation. Labels depend on past incident records, which may miss events nobody noticed. Amara states each limit and its likely effect on results.

Amara states her study's limitations honestly: a single partner, a limited period, synthetic replays that may not capture every real pattern, and a small set of key events. For each, she explains the likely effect on the results and how future work could address it.

### 7.3 Recommendations

Corvane should keep the change register, review exceptions quarterly, maintain the labelled set by adding each new confirmed incident and rerun recall checks after any major tuning. Other organisations can adopt the procedure, but must build their own labelled sets.

Recommendations follow from the evidence: adopt documented tuning with peer review, measure detection retention alongside volume, and review tuned rules periodically. Each is practical for a small team.

Each states its cost, owner and how success would be measured.

Priorities are stated.

### 7.4 Writing for practitioners

A two-page summary for Corvane leads with the outcome in operational terms: analysts now handle about 1,200 alerts a week instead of 4,200, with the same detections.

Practitioners need findings they can act on, so Amara also writes a short summary for Corvane's team. It explains in plain language what was done, what changed, what the risks were, and what to do next, with one table of key results. Technical detail stays in the dissertation, while the summary focuses on decisions and next steps that busy analysts and managers can apply directly.

### Ethical reflection

Amara includes a short reflection on ethics. The study handled pseudonymised internal data and interviews, and its main risk was weakening detection. Governance, the labelled recall check and the investigation of the lost detection were her responses. She also reflects that tuning can conceal problems if exceptions are granted for convenience, and recommends that exception owners be accountable for their entries. Writing this down shows examiners that ethical thinking ran through the study rather than ending with the approval form, and it gives Corvane a clear principle for future tuning.

### Threats to validity summary

She closes the limitations chapter with a table of threats grouped by type. Internal validity: coincident changes, partly addressed by the explanations table. Construct validity: labels from past incidents may not represent all relevant events. External validity: one logistics firm with two data centres. Statistical conclusion validity: eight weeks of data limit precision of estimates. Each threat lists what was done and what remains. A structured table helps readers compare this study with others and see quickly where its evidence is strongest and weakest.

### Worked example

Dr Brandt's review asks Amara to move the base-rate explanation earlier, since it motivates the whole study.

> **Synthetic case.** The dissertation is synthetic.

### Errors and limits

Limitations written as a token paragraph do not help readers judge results.

### Exercises

- **EX039 — Appendix contents.** List three appendices. *Rubric:* 3 = register, scripts, data;; 2 = two;; 1 = one;; 0 = none.
- **EX040 — Label limit.** How might labels bias recall? *Rubric:* 3 = unnoticed events missing;; 2 = incomplete;; 1 = vague;; 0 = none.
- **EX041 — Labelled set upkeep.** How should Corvane maintain the labelled set? *Rubric:* 3 = add confirmed incidents;; 2 = update;; 1 = vague;; 0 = none.
- **EX042 — Practitioner lead.** Write the summary's first sentence. *Rubric:* 3 = operational outcome;; 2 = partial;; 1 = vague;; 0 = none.
- **EX043 — Structure change.** Why move the base-rate explanation earlier? *Rubric:* 3 = motivates study;; 2 = clarity;; 1 = vague;; 0 = none.
- **EX044 — Transferability.** What must other organisations do to adopt the procedure? *Rubric:* 3 = build their own labelled sets;; 2 = adapt;; 1 = vague;; 0 = none.

### Synthesis

Clear structure and honest limits make the dissertation useful to examiners and practitioners.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) obtain independent review; (2) prepare the viva; (3) plan follow-up.

### 8.1 Independent review

A second analyst at Corvane, not involved in tuning, reviews a random sample of fifty changes against the register's justifications. Forty-eight are judged appropriate; two exceptions are tightened.

Before submission, an independent reviewer who was not involved in the study reads the dissertation and checks whether conclusions follow from the evidence. Amara records each comment and her response, revising where the reviewer found claims stronger than the data supported. This step catches blind spots that close involvement makes hard to see, and it prepares her for examination.

### 8.2 Viva preparation

Amara expects questions on causation, generalisability and the lost detection. She prepares a slide showing the normalised series and the explanations table.

Preparing for the viva, Amara rereads the dissertation, lists likely questions about design, measures, alternatives and the missed detection, and prepares short evidence-based answers. She practises explaining her contribution in a few sentences. A mock viva with colleagues helps her handle unexpected questions calmly and admit uncertainty where evidence is limited, which examiners respect more than overconfident answers.

### 8.3 The viva

Examiners ask why recall was measured on only forty events. Amara explains the trade-off between label quality and quantity and proposes growing the set over time.

In the viva, examiners test whether Amara understands her work and its limits. She listens carefully, answers the question asked, and refers to specific evidence in the dissertation. When she does not know something, she says so and explains how it could be found out. She notes any corrections the examiners request, so they can be addressed promptly and accurately afterwards.

### 8.4 Follow-up

Corvane adopts quarterly exception reviews. Amara plans a short paper with Dr Brandt.

After the viva, Amara makes required corrections and records each change. She sends Corvane the practitioner summary, returns or deletes company data as the agreement requires, and archives her code and synthetic data. She also considers publishing a short paper, with the partner's agreement, so other small teams can benefit from the findings and method.

She thanks the analysts who took part, and offers a short session explaining results to the team.

### Answering a hostile question

One examiner asks whether the study simply proved that switching off rules reduces alerts. Amara answers with evidence rather than defensiveness: only rules for absent services were disabled, each with proof; most reduction came from narrow exceptions and thresholds; and recall was checked on a fixed labelled set, with the one lost detection investigated and fixed. She adds that the concern is legitimate, which is exactly why the governance and recall checks were built into the design from the start. The examiner accepts the answer and asks for the governance section to be summarised in the abstract.

### Lessons for future students

Amara writes a short note for future students on the programme. Agree data access and governance before the start date, because approvals took three weeks. Build the labelled set early, since it limits every later analysis. Measure normalised volume from the first day. And treat practitioners as co-investigators: Corvane's analysts suggested two of the most effective tuning changes. Dr Brandt adds the note to the programme's guidance for industry-partnered dissertations.

### Worked example

The examiners accept the dissertation with minor corrections.

> **Synthetic case.** The viva is synthetic.

### Errors and limits

Independent review loses value if the reviewer helped design the changes.

### Exercises

- **EX045 — Review sample.** What did the independent review find? *Rubric:* 3 = 48 of 50 appropriate, 2 tightened;; 2 = mostly fine;; 1 = vague;; 0 = none.
- **EX046 — Reviewer independence.** Why must the reviewer be uninvolved? *Rubric:* 3 = avoid bias;; 2 = independence;; 1 = vague;; 0 = none.
- **EX047 — Small label set.** Defend the 40-event label set. *Rubric:* 3 = quality over quantity, growth plan;; 2 = small;; 1 = vague;; 0 = none.
- **EX048 — Viva slide.** Which slide best answers causation questions? *Rubric:* 3 = normalised series and explanations table;; 2 = series;; 1 = vague;; 0 = none.
- **EX049 — Adoption.** What did Corvane adopt? *Rubric:* 3 = quarterly exception reviews;; 2 = reviews;; 1 = vague;; 0 = none.
- **EX050 — Outcome.** What was the viva outcome? *Rubric:* 3 = minor corrections;; 2 = pass;; 1 = vague;; 0 = none.

### Synthesis

Independent review and an honest viva complete the study.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Amara Okoye, Dr Felix Brandt, Easterly University, Corvane Logistics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** When analysts close alerts in bulk, a real detection is likely to be dismissed with the noise.

**EX002.** Search strings, databases, dates, result counts and screening decisions.

**EX003.** A drop in traffic alone would reduce alerts and look like improvement.

**EX004.** Precision: share of alerts that are actionable; recall: share of actionable events that produce an alert.

**EX005.** From past incident records and authorised test activity documented in change logs.

**EX006.** Disabling detection rules, which cuts alerts but also detections.

**EX007.** Evaluating new detection products and machine learning methods.

**EX008.** Signatures precisely match known patterns but miss new ones. Anomaly methods can catch new behaviour but raise more false alarms.

**EX009.** 0.490 at 0.01 and 0.009 at 0.0001.

**EX010.** With rare malicious events, false positives dominate, so reducing them improves precision far more.

**EX011.** They record why alerts were benign or real, providing labels and tuning evidence.

**EX012.** It shows which system and owner are involved, so analysts judge importance quickly.

**EX013.** Policy scripts expressing what the operator cares about.

**EX014.** At that base rate, roughly nine in ten alerts are false.

**EX015.** Several weeks show normal variation, so a change is not mistaken for noise.

**EX016.** Payloads may include personal or confidential content not needed for the study.

**EX017.** Evidence that the service the rule protects does not exist at Corvane.

**EX018.** It prevents improving alert numbers by removing needed detection.

**EX019.** Corvane retains control and only aggregates leave its environment.

**EX020.** A sensor software upgrade during the study period.

**EX021.** Lower traffic, sensor failure, retired noisy server, export change.

**EX022.** From about 512 to 191 alerts per 100 GB.

**EX023.** The drop occurs exactly when tuning was applied rather than gradually.

**EX024.** It was retired in week six, after the drop in week five.

**EX025.** Alert counts depend on traffic volume more than on the number of hosts.

**EX026.** Explanation, evidence checked and verdict.

**EX027.** At least 50 percent reduction in normalised alerts and recall at least 0.90.

**EX028.** Backup transfers, monitoring scans, rules for absent services.

**EX029.** If the backup server were compromised, no rule would alert on it.

**EX030.** Analysts confirmed legitimate tools routinely exceed five connections per minute.

**EX031.** So they are reconsidered rather than becoming permanent.

**EX032.** A 64 percent drop in normalised alerts with no labelled events missed.

**EX033.** About three of every hundred alerts are worth acting on.

**EX034.** One labelled event no longer produced an alert.

**EX035.** The backup exception covered the server at all times, not just its backup window.

**EX036.** By rerunning the labelled set with the window-restricted exception.

**EX037.** About 40 extra alerts per week.

**EX038.** Hiding it would misrepresent the trade-off, and examining it improved the procedure.

**EX039.** Change register, scripts and synthetic data.

**EX040.** Events nobody noticed are absent, so recall may be overestimated.

**EX041.** Add each new confirmed incident and authorised test.

**EX042.** Analysts now handle about 1,200 alerts a week instead of 4,200 while detecting the same labelled events.

**EX043.** It explains why tuning matters, so readers need it first.

**EX044.** Build and maintain their own labelled event sets.

**EX045.** 48 of 50 changes appropriate; two exceptions tightened.

**EX046.** Someone who designed the changes would be inclined to approve them.

**EX047.** High-quality labels were limited; the set will grow with each confirmed incident.

**EX048.** The normalised weekly series with the competing explanations table.

**EX049.** Quarterly exception reviews.

**EX050.** Accepted with minor corrections.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Barker, E., Dang, Q., Frankel, S., Scarfone, K., & Wouters, P. (2020). *Guide to IPsec VPNs* (NIST SP 800-77 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-77r1>
- Center for Internet Security. (2021). *CIS Critical Security Controls v8*. <https://www.cisecurity.org/controls/v8>
- Chandramouli, R., & Rose, S. (2013). *Secure Domain Name System (DNS) deployment guide* (NIST SP 800-81-2). NIST. <https://doi.org/10.6028/NIST.SP.800-81-2>
- Claise, B., Trammell, B., & Aitken, P. (2013). *Specification of the IP Flow Information Export (IPFIX) protocol* (RFC 7011). IETF. <https://www.rfc-editor.org/rfc/rfc7011>
- Ferguson, P., & Senie, D. (2000). *Network ingress filtering* (RFC 2827, BCP 38). IETF. <https://www.rfc-editor.org/rfc/rfc2827>
- Gerhards, R. (2009). *The Syslog protocol* (RFC 5424). IETF. <https://www.rfc-editor.org/rfc/rfc5424>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Kaufman, C., Hoffman, P., Nir, Y., Eronen, P., & Kivinen, T. (2014). *Internet Key Exchange Protocol Version 2 (IKEv2)* (RFC 7296). IETF. <https://www.rfc-editor.org/rfc/rfc7296>
- Kent, S., & Seo, K. (2005). *Security architecture for the Internet Protocol* (RFC 4301). IETF. <https://www.rfc-editor.org/rfc/rfc4301>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Lepinski, M., & Kent, S. (2012). *An infrastructure to support secure Internet routing* (RFC 6480). IETF. <https://www.rfc-editor.org/rfc/rfc6480>
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Paxson, V. (1999). Bro: A system for detecting network intruders in real-time. *Computer Networks*, 31(23–24), 2435–2463. <https://doi.org/10.1016/S1389-1286(99)00112-7>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Scarfone, K., & Hoffman, P. (2009). *Guidelines on firewalls and firewall policy* (NIST SP 800-41 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-41r1>
- Scarfone, K., & Mell, P. (2007). *Guide to intrusion detection and prevention systems (IDPS)* (NIST SP 800-94). NIST. <https://doi.org/10.6028/NIST.SP.800-94>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *2010 IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Souppaya, M., & Scarfone, K. (2012). *Guidelines for securing wireless local area networks (WLANs)* (NIST SP 800-153). NIST. <https://doi.org/10.6028/NIST.SP.800-153>
- Sriram, K., & Montgomery, D. (2019). *Resilient interdomain traffic exchange: BGP security and DDoS mitigation* (NIST SP 800-189). NIST. <https://doi.org/10.6028/NIST.SP.800-189>
- Wool, A. (2004). A quantitative study of firewall configuration errors. *Computer*, 37(6), 62–67. <https://doi.org/10.1109/MC.2004.2>
