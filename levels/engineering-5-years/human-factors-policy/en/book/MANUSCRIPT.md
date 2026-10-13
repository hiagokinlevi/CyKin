# Human Factors and Cyber Policy: Engineering Course

- Language: English (`en`); course 121, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; nineteen offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students designing, verifying and operating a security awareness and reporting programme as an engineered socio-technical system.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs model weekly reports, forgetting, rates, triage, queues, reliability, budgets and exact tests on synthetic data; no real staff, emails or accounts are involved. Any phishing simulation described is announced, approved with staff representatives, avoids lures exploiting personal distress and is reported only in aggregate. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one engineering student through a five-year course centred on a water utility's reporting programme: foundations, measurement and models, requirements and architecture, controls and implementation, verification and validation, operations, optimisation, the contractor capstone, evidence dossier, thesis and defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Aiko Tanabe** | Engineering student | Invented |
| **Prof. Joanna Kerr** | Supervisor | Invented |
| **Rivenhall Technical University** | Fictional university | Invented |
| **Greyford Water** | Fictional water utility, 600 staff | Invented |

### Core sources

Adams and Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff and Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Hansche et al. (2024), NIST SP 800-50r1; Dawkins and Jacobs (2023), [doi:10.6028/NIST.TN.2276](https://doi.org/10.6028/NIST.TN.2276); Lain, Kostiainen and Čapkun (2022), [doi:10.1109/SP46214.2022.9833766](https://doi.org/10.1109/SP46214.2022.9833766); Herley (2009), [doi:10.1145/1719030.1719050](https://doi.org/10.1145/1719030.1719050). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) use rates of change to describe security behaviour over time; (2) interpret derivatives as speeds of change in reporting; (3) relate accumulation to totals of exposure.

### 1.1 Rates in human factors

Aiko Tanabe is an engineering student at the fictional Rivenhall Technical University. Her supervisor, Prof. Joanna Kerr, links every foundation course to a running case: the fictional Greyford Water utility, whose six hundred staff include control room operators, field engineers and office teams. In calculus, Aiko learns that a derivative describes how fast something changes. At Greyford, the number of staff reporting suspicious emails changes over weeks after a campaign. The rate of change tells her whether reporting is still rising, levelling off or falling back, which matters more to planning than any single weekly count.

### 1.2 Reading a curve

Aiko models weekly reports after a campaign as rising quickly at first and then levelling. The derivative is large in the first weeks and shrinks towards zero. She learns to read where the curve bends, because that is when the campaign's effect is fading and a reminder might help. She also sees that a straight line would mislead: it would predict reports growing for ever. Choosing a shape that fits how people actually respond is the first modelling decision in any human factors analysis, and calculus gives her the vocabulary to describe it.

### 1.3 Accumulation and exposure

Integration adds up a rate over time. Aiko uses it to estimate total exposure: if a phishing email sits unreported in inboxes, the number of people who could click grows each hour until someone reports it and it is removed. The area under the curve of unreported inboxes over time measures exposure. Faster reporting shrinks that area. This simple idea links her mathematics course to Greyford's goal of reducing how long malicious emails remain available, a measure that does not depend on blaming whoever clicked.

### Worked example

Aiko describes reporting after a campaign as a curve, reads its rate of change to find when the effect fades and uses accumulation to define exposure time.

> **Synthetic case.** Rivenhall, Greyford and all people and figures are synthetic.

### Errors and limits

Smooth curves simplify noisy weekly data. Exposure models ignore how attractive each email is.

### Exercises

- **EX001 — Rate meaning.** What does the derivative of weekly reports tell Greyford? *Rubric:* 3 = whether reporting is rising, levelling off or falling;; 2 = trend;; 1 = vague;; 0 = none.
- **EX002 — Straight-line flaw.** Why would a straight line mislead for reports after a campaign? *Rubric:* 3 = it predicts reports growing for ever;; 2 = unbounded;; 1 = vague;; 0 = none.
- **EX003 — Exposure area.** How does integration define exposure? *Rubric:* 3 = area under unreported inboxes over time;; 2 = area;; 1 = count;; 0 = none.

### Synthesis

Rates and accumulation give precise language for how behaviour changes and how long people remain exposed.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) use sets and logic to state policy rules; (2) find contradictions between rules; (3) count combinations that affect usability.

### 2.1 Policy as logic

Aiko translates Greyford's password and access rules into logic. One rule says operators must lock screens when leaving a console. Another says control room consoles must stay signed in during incidents so alarms are never missed. Written as logical statements, the two clash during an incident when an operator steps away briefly. Adams and Sasse (1999) found that staff faced with conflicting or unworkable rules make their own compromises. Writing rules precisely exposes such conflicts before staff are forced to choose which rule to break.

### 2.2 Sets of people and permissions

Using sets, Aiko lists which staff groups hold which permissions. The intersection of field engineers and people with remote access to pumping stations shows who could change settings from outside the plant. The set difference between people trained on remote access and people who have it reveals eleven staff with access but no training. Sets turn vague worries into exact lists that managers can act on, and they make it easy to check whether a proposed change widens or narrows each group.

### 2.3 Counting burden

Aiko counts how many distinct sign-ins a field engineer performs on a typical day: laptop, remote access, maintenance system, email, timesheet and two vendor portals. Each has its own password rules. She computes that if each system forced changes on a different schedule, an engineer would face a password change roughly every week. Counting makes the burden visible. Sasse, Brostoff and Weirich (2001) argued that such burden drives the workarounds often blamed on users, so counting is a first step towards design changes.

### Worked example

Aiko writes two rules in logic to expose a conflict, uses set operations to find untrained staff with remote access and counts sign-in burden.

> **Synthetic case.** Rules, groups and counts are synthetic; Adams and Sasse (1999) and Sasse et al. (2001) are real.

### Errors and limits

Logic captures written rules, not informal practice. Counts depend on a typical day that may vary.

### Exercises

- **EX004 — Rule conflict.** Which two rules conflict in the control room? *Rubric:* 3 = lock screens when leaving versus stay signed in during incidents;; 2 = both rules;; 1 = vague;; 0 = none.
- **EX005 — Set difference use.** What did the set difference reveal? *Rubric:* 3 = eleven staff with remote access but no training;; 2 = untrained;; 1 = vague;; 0 = none.
- **EX006 — Change frequency.** How often might an engineer face a password change with separate schedules? *Rubric:* 3 = roughly every week;; 2 = weekly;; 1 = yearly;; 0 = none.

### Synthesis

Discrete mathematics turns policies and permissions into exact statements that reveal conflicts and burden.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical environments to human error; (2) apply signal and noise ideas to alarms; (3) consider physical security in human terms.

### 3.1 Environment and error

Aiko visits Greyford's control room. Lighting, noise from equipment, shift length and screen glare all affect how accurately operators read displays. Physics explains some of these effects: glare reduces contrast, and background noise masks audible alarms. Human errors in such conditions are often predictable consequences of the environment rather than personal failings. She notes that improving lighting and alarm tones may reduce mistakes more cheaply than retraining staff who are already competent. She lists the conditions she observes in a short table and shares it with the control room supervisor for comment.

### 3.2 Signal and noise

In physics, signal-to-noise ratio measures how clearly a signal stands out. Aiko applies it to alarms and to security alerts. If operators see hundreds of low-value alarms per shift, the important ones are lost in noise, and staff learn to acknowledge without reading. The same happens with security warnings on screens: frequent warnings teach people to click through. Herley (2009) argued that warnings with mostly false positives can be rationally ignored. Raising the signal means removing low-value alerts rather than asking people to concentrate harder.

### 3.3 Physical security and people

Aiko examines physical access. Doors to the control room use badges, but staff often hold them open for colleagues carrying equipment. She notes that physics of doors matters: a heavy door that closes slowly invites tailgating. A design change, such as a faster closer and a second entrance for deliveries, removes the pressure to hold the door. Physical controls work best when they match the tasks people perform, which is the same lesson as for digital controls. Greyford's facilities manager agrees to trial the faster closer at one site.

### Worked example

Aiko links control room conditions to predictable errors, uses signal-to-noise to explain alarm fatigue and redesigns door behaviour to reduce tailgating.

> **Synthetic case.** The control room is synthetic; Herley (2009) is real.

### Errors and limits

Environmental fixes need ergonomic expertise. Alarm reduction must not remove critical alarms.

### Exercises

- **EX007 — Predictable errors.** Why are many control room errors predictable? *Rubric:* 3 = they follow from lighting, noise, glare and shift length;; 2 = environment;; 1 = carelessness;; 0 = none.
- **EX008 — Alarm noise.** What happens when operators see hundreds of low-value alarms? *Rubric:* 3 = they acknowledge without reading;; 2 = fatigue;; 1 = vague;; 0 = none.
- **EX009 — Door redesign.** How can a door design reduce tailgating? *Rubric:* 3 = faster closer and a separate delivery entrance;; 2 = design;; 1 = signs;; 0 = none.

### Synthesis

Physical environment and signal quality shape human error, so engineers should fix conditions before blaming people.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write simple programs to analyse behaviour data; (2) handle personal data carefully in code; (3) test programs with known cases.

### 4.1 First analysis program

Aiko writes her first Python program to summarise synthetic weekly report counts from Greyford's report button. It reads a list of numbers, computes the total, the average and the week with the most reports, and prints the result. She tests it with a short list where she knows the answer by hand. Testing with known cases is a basic engineering habit, because a program that runs without errors can still give wrong answers if a loop skips the last week or divides by the wrong count.

### Lab — Summarising weekly report counts

```python
# Summarise weekly report-button counts after a campaign (synthetic).
weeks = [12, 30, 41, 35, 27, 22, 19, 18, 17, 17, 16, 16]
total = sum(weeks); peak = max(weeks); pw = weeks.index(peak) + 1
print(f"weeks {len(weeks)}, total {total}, average {total / len(weeks):.1f}, peak week {pw} ({peak})")
for i, w in enumerate(weeks, 1): print(f"week {i:2d} {'#' * (w // 2)} {w}")
```

Run with `python3 lab_weekly.py`. Verified output:

```text
weeks 12, total 270, average 22.5, peak week 3 (41)
week  1 ###### 12
week  2 ############### 30
week  3 #################### 41
week  4 ################# 35
week  5 ############# 27
week  6 ########### 22
week  7 ######### 19
week  8 ######### 18
week  9 ######## 17
week 10 ######## 17
week 11 ######## 16
week 12 ######## 16
```

### 4.2 Handling personal data

Prof. Kerr warns that behaviour data can be personal. Aiko's program works on counts per week, not on names. If she ever needs individual records, she will replace names with random codes and keep the key separately. She writes this rule at the top of her script. Programs that process staff data should collect the minimum needed, because once data is in a spreadsheet it tends to be copied, and copies are hard to track or delete. Prof. Kerr checks the rule during code review.

### 4.3 Reading the result

The lab shows twelve weeks of reports, peaking in week three after a campaign and settling at a lower level. Aiko notes that the average hides this shape, so she adds a simple printed bar for each week. Seeing the shape matches her calculus model from chapter 1. She learns that a program's output should support the decision at hand: here, when to schedule the next reminder, which the weekly bars make obvious. She saves the output with the date so that later campaigns can be compared against the same weekly pattern and baseline.

### Worked example

Aiko writes and tests a program summarising weekly reports, keeps it to counts rather than names and adds a simple bar display to reveal the shape.

> **Synthetic case.** Counts are synthetic.

### Errors and limits

Averages hide patterns. Pseudonymised data can still identify people in small groups.

### Exercises

- **EX010 — Testing habit.** Why test with a list whose answer is known? *Rubric:* 3 = a program can run but still give wrong answers;; 2 = correctness;; 1 = vague;; 0 = none.
- **EX011 — Lab peak.** Which week had the most reports in the lab, and how many? *Rubric:* 3 = week 3 with 41 reports;; 2 = week 3;; 1 = vague;; 0 = none.
- **EX012 — Data rule.** What rule did Aiko write at the top of her script? *Rubric:* 3 = use counts; pseudonymise with a separate key if individuals are needed;; 2 = minimum data;; 1 = vague;; 0 = none.

### Synthesis

Simple, tested programs on minimal data can reveal patterns that support practical decisions.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write clearly for operators and managers; (2) present behaviour data without blame; (3) adapt a message to its audience.

### 5.1 Writing for operators

Aiko writes a one-page note for control room operators explaining the report button. She uses short sentences, numbered steps and a screenshot. She avoids terms like phishing vector and uses plain words such as suspicious email. She tests the note with two operators, who suggest putting the most important step first: what to do if they have already clicked. Engineering communication succeeds when the reader can act correctly, quickly and without fear of looking foolish. The revised note is laminated and placed beside each console.

### 5.2 Presenting without blame

For managers, Aiko presents simulation results as department totals and trends, never individual names. She frames clicking as an expected outcome of good lures and focuses on reporting speed. Lain, Kostiainen and Čapkun (2022) found that reporting by staff can provide a strong signal for detection in organisations. Presenting results without blame keeps staff willing to report their own mistakes, which is when early reporting matters most. She also shows managers how a blame-free approach increased reports of genuine mistakes in the pilot team, which persuades them to keep names out of every report and to praise prompt reporting publicly.

### 5.3 Adapting the message

Aiko prepares three versions of the same findings: a chart and three bullet points for the board, a page of detail for the security team and the operator note. Each uses the same numbers but different emphasis. The board sees exposure time falling; the security team sees triage workload; operators see what to do. Prof. Kerr notes that adapting messages is not spin, as long as the facts are the same and limitations appear in every version. She keeps all three versions in one folder.

### Worked example

Aiko writes an operator note tested with users, presents results to managers without blame and adapts one finding for three audiences.

> **Synthetic case.** Notes and audiences are synthetic; Lain et al. (2022) is real.

### Errors and limits

Simplified messages can drop caveats. Department totals can still single out tiny teams.

### Exercises

- **EX013 — Operator suggestion.** What did operators suggest moving first in the note? *Rubric:* 3 = what to do if you already clicked;; 2 = clicked step;; 1 = vague;; 0 = none.
- **EX014 — Blame-free framing.** How does Aiko frame clicking for managers? *Rubric:* 3 = as an expected outcome of good lures, focusing on reporting speed;; 2 = expected;; 1 = failure;; 0 = none.
- **EX015 — Same facts.** What keeps adapted messages honest? *Rubric:* 3 = the same facts and limitations in every version;; 2 = consistency;; 1 = vague;; 0 = none.

### Synthesis

Clear, blame-free, audience-specific communication helps people act and keeps them willing to report.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) model decay of training effects; (2) compare refresher schedules; (3) recognise the limits of smooth models of behaviour.

### 6.1 Modelling decay

Aiko reads that skills and attention fade after training. She models the share of staff who would correctly spot a typical lure as starting high after training and decaying exponentially towards a lower baseline. The model has two parameters: the baseline and the rate of decay. Calculus lets her compute the half-life, the time for the extra benefit of training to halve. She emphasises to Prof. Kerr that this is a model to support planning, and that she has no evidence yet that Greyford's staff follow this exact curve.

### 6.2 Comparing schedules

Using the model, Aiko compares a single annual course with short refreshers every three months. Integrating the benefit over a year shows that frequent short refreshers keep the average higher, even if each is less intense. The lab computes the average benefit for both schedules using the same decay rate. She notes that the comparison ignores the time each schedule costs staff, which the compliance budget idea of Beautement, Sasse and Wonham (2008) says must be counted, so she adds staff minutes to the comparison.

### Lab — Average benefit of annual versus quarterly refreshers

```python
# Average training benefit over 12 months: annual vs quarterly refreshers (synthetic exponential decay).
import math
base, gain, k = 0.40, 0.45, 0.24          # baseline, boost after training, decay per month
print(f"half-life of benefit: {math.log(2) / k:.1f} months")
def avg(refresh_months):
    total, steps = 0.0, 1200
    for i in range(steps):
        t = 12 * i / steps; since = min(t - r for r in refresh_months if r <= t)
        total += base + gain * math.exp(-k * since)
    return total / steps
print(f"annual (month 0): average {avg([0]):.2f}")
print(f"quarterly (0,3,6,9): average {avg([0, 3, 6, 9]):.2f}")
```

Run with `python3 lab_decay.py`. Verified output:

```text
half-life of benefit: 2.9 months
annual (month 0): average 0.55
quarterly (0,3,6,9): average 0.72
```

### 6.3 Limits of smooth models

Real behaviour is lumpy. A single memorable incident can raise vigilance more than any refresher, and a busy period can lower it suddenly. Bada, Sasse and Nurse (2019) found that awareness campaigns often fail when they rely on information alone, so a smooth decay curve may describe knowledge rather than behaviour. Aiko writes these limits beside her model and proposes testing it against Greyford's actual reporting data before using it to set the training calendar. She notes this test as a task for her later measurement chapter, where real data will be available.

### Worked example

Aiko models training decay with a half-life, compares annual and quarterly schedules including staff time, and records the model's limits.

> **Synthetic case.** Parameters are synthetic; Beautement et al. (2008) and Bada et al. (2019) are real.

### Errors and limits

Exponential decay is an assumption. Knowledge measures may not reflect behaviour.

### Exercises

- **EX016 — Half-life.** What half-life does the lab's decay rate imply? *Rubric:* 3 = about 2.9 months;; 2 = about 3 months;; 1 = vague;; 0 = none.
- **EX017 — Schedule result.** Which schedule kept the higher average benefit in the lab? *Rubric:* 3 = quarterly: 0.72 versus 0.55 for annual;; 2 = quarterly;; 1 = annual;; 0 = none.
- **EX018 — Missing cost.** What cost did Aiko add to the comparison? *Rubric:* 3 = staff minutes spent on training;; 2 = staff time;; 1 = vague;; 0 = none.

### Synthesis

Calculus models of decay help compare schedules, provided their assumptions and costs are stated.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) estimate rates with uncertainty; (2) avoid misleading comparisons of small groups; (3) report results without identifying individuals.

### 7.1 Rates with uncertainty

Greyford's last simulation found that nine of sixty field engineers reported the email within an hour. Aiko computes the rate, fifteen percent, and a confidence interval to show how uncertain it is with only sixty people. The interval is wide, so a later result of twenty percent might not be a real improvement. She learns that every rate from a small group should carry its uncertainty, otherwise managers will react to random variation as if it were a trend. She adds the interval to every chart.

### Lab — Report rates with Wilson intervals by team

```python
# Report rates with Wilson 95% intervals by team (synthetic simulation results).
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
teams = {"field engineers": (9, 60), "office": (31, 140), "treatment": (12, 45), "lab": (4, 8), "fleet": (6, 30)}
for t, (k, n) in teams.items():
    lo, hi = wilson(k, n); flag = "  (under 20: merge before reporting)" if n < 20 else ""
    print(f"{t:15} {k}/{n} = {k/n:.1%}  95% CI {lo:.1%} to {hi:.1%}{flag}")
```

Run with `python3 lab_rates.py`. Verified output:

```text
field engineers 9/60 = 15.0%  95% CI 8.1% to 26.1%
office          31/140 = 22.1%  95% CI 16.1% to 29.7%
treatment       12/45 = 26.7%  95% CI 16.0% to 41.0%
lab             4/8 = 50.0%  95% CI 21.5% to 78.5%  (under 20: merge before reporting)
fleet           6/30 = 20.0%  95% CI 9.5% to 37.3%
```

### 7.2 Small groups

Aiko compares report rates across five teams. The smallest team, with eight people, shows the highest rate, but its interval is very wide. She warns against ranking teams publicly, because small teams swing randomly and rankings shame people for chance results. She also notes that publishing a rate for a team of eight could identify individuals. Her rule is to report only groups of twenty or more, merging small teams where necessary. The lab marks the eight-person team for merging, and she explains to the team leader why their result will not be shown separately.

### 7.3 Honest reporting

Aiko writes the results for management: overall reporting rate with its interval, change since last quarter, and a note that differences between teams are mostly within uncertainty. She includes the Phish Scale difficulty of the lure, as described by Dawkins and Jacobs (2023), because a harder lure would naturally lower reporting. Statistics in human factors work must be honest about uncertainty and context so that people are not judged by noise. She also lists what the figures cannot show, such as whether staff who did not report simply never opened the email, so managers do not overread the numbers.

### Worked example

Aiko estimates report rates with Wilson intervals, warns against ranking small teams, merges groups under twenty and reports with lure difficulty.

> **Synthetic case.** Teams and counts are synthetic; Dawkins and Jacobs (2023) is real.

### Errors and limits

Intervals assume independent responses. Merging groups hides real differences.

### Exercises

- **EX019 — Field engineer interval.** What interval did the lab give for 9 of 60? *Rubric:* 3 = 15.0%, Wilson 95% interval 8.1% to 26.1%;; 2 = wide;; 1 = vague;; 0 = none.
- **EX020 — Ranking risk.** Why not rank teams publicly by report rate? *Rubric:* 3 = small teams swing randomly and rankings shame chance results;; 2 = noise;; 1 = vague;; 0 = none.
- **EX021 — Group size rule.** What minimum group size does Aiko report? *Rubric:* 3 = twenty;; 2 = 20;; 1 = eight;; 0 = none.

### Synthesis

Rates from small groups must carry uncertainty and context, and must never single out individuals.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) relate hardware design to user security decisions; (2) understand secure hardware features users meet; (3) evaluate how design affects usable security.

### 8.1 Hardware users meet

Aiko studies how hardware shapes what users see. Laptops with a trusted platform module can store keys so that disk encryption unlocks automatically with a PIN; security keys contain small secure chips that perform authentication without revealing secrets. Users do not see the chips, but they experience the result: fewer passwords and simpler steps. Engineering hardware so that the secure path is also the easiest path is a central idea in usable security, echoing Sasse, Brostoff and Weirich (2001). She lists the features found on Greyford's laptops.

### 8.2 Design and decisions

Aiko compares two ways Greyford could protect field laptops. One asks users for a long separate disk password at start-up; the other uses the trusted platform module with a short PIN. Interviews with engineers show they would write the long password on the laptop. The hardware-backed option gives similar protection against a stolen laptop while removing the temptation. She notes that good hardware design reduces the number of security decisions users must make correctly. She presents both options to the IT manager with the interview evidence, and the hardware-backed design is chosen for the next laptop refresh.

### 8.3 Limits

Hardware features do not solve everything. Security keys can be lost, and replacement must be quick or staff will be locked out during urgent work. Firmware needs updates, which users may postpone if updates interrupt work. Aiko writes requirements: spare keys at depots, updates scheduled outside shifts and a clear recovery process. Hardware supports usable security only when the surrounding processes are designed for real working conditions. She also notes that staff need simple instructions for first use, because a confusing first experience with a security key can create lasting resistance, and she drafts a one-page guide with pictures for depots.

### Worked example

Aiko links secure hardware to simpler user steps, compares two laptop protection designs and writes supporting process requirements.

> **Synthetic case.** Designs and interviews are synthetic; Sasse et al. (2001) is real.

### Errors and limits

Hardware features vary by model. Recovery processes can become an attack path.

### Exercises

- **EX022 — Invisible chips.** How do users experience secure hardware? *Rubric:* 3 = fewer passwords and simpler steps;; 2 = simpler;; 1 = vague;; 0 = none.
- **EX023 — Laptop choice.** Why prefer the hardware-backed PIN for field laptops? *Rubric:* 3 = similar protection without engineers writing passwords on laptops;; 2 = usability;; 1 = vague;; 0 = none.
- **EX024 — Key loss requirement.** What process requirement addresses lost security keys? *Rubric:* 3 = spare keys at depots and quick recovery;; 2 = spares;; 1 = vague;; 0 = none.

### Synthesis

Hardware can make the secure path the easy path, if recovery and updates fit real work.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure a program that processes reported emails; (2) design data structures for triage; (3) protect privacy in automated processing.

### 9.1 A triage program

Greyford's security team receives many reported emails. Aiko writes a program that groups reports of the same email, counts how many staff reported each and records the time of the first report. Grouping reduces the team's workload, because twenty reports of one phishing email need one investigation. She structures the program with small functions for reading, grouping and summarising, each tested separately, so later changes are safer. She writes a short test for each function using small hand-made report lists, so that any later change that breaks grouping or timing is noticed immediately rather than discovered during a real incident.

### Lab — Grouping duplicate reports and timing the first report

```python
# Group duplicate reported emails and find first-report delay (synthetic; minutes after arrival).
reports = [("payroll@greyf0rd.co", "Update your bank details", m) for m in (9, 11, 12, 14, 15, 18, 20, 22, 25, 30, 33, 40, 41, 45)] + \
          [("it-help@vendorx.io", "Mailbox full", m) for m in (25, 31, 38, 47, 52, 60, 66, 70, 75)] + \
          [("news@supplier.example", "Monthly newsletter", m) for m in (120, 180, 200)] + \
          [("dhl-track@parcel.example", "Missed delivery", m) for m in (16, 19, 27, 29, 35, 44, 48)] + \
          [("ceo.greyford@gmail.example", "Quick favour", m) for m in (14, 17, 26, 39, 55)] + \
          [("hr@greyford.example", "Benefits survey", m) for m in (90, 95)]
groups = {}
for sender, subject, m in reports:
    key = (sender, subject.lower()); c, first = groups.get(key, (0, 10**9)); groups[key] = (c + 1, min(first, m))
print(f"{len(reports)} reports -> {len(groups)} distinct emails")
for (s, subj), (c, first) in sorted(groups.items(), key=lambda x: -x[1][0]):
    print(f"{c:3d} reports, first after {first:3d} min: {subj} <{s}>")
```

Run with `python3 lab_triage.py`. Verified output:

```text
40 reports -> 6 distinct emails
 14 reports, first after   9 min: update your bank details <payroll@greyf0rd.co>
  9 reports, first after  25 min: mailbox full <it-help@vendorx.io>
  7 reports, first after  16 min: missed delivery <dhl-track@parcel.example>
  5 reports, first after  14 min: quick favour <ceo.greyford@gmail.example>
  3 reports, first after 120 min: monthly newsletter <news@supplier.example>
  2 reports, first after  90 min: benefits survey <hr@greyford.example>
```

### 9.2 Data structures

Aiko uses a dictionary keyed by a fingerprint of each email's sender and subject. Each entry stores the count and the earliest report time. This structure makes grouping fast even with thousands of reports. The lab shows that forty reports reduce to six distinct emails, and the most reported email was first reported nine minutes after arrival. That first-report time is the key figure for exposure, linking back to her calculus model in chapter 1. She notes that a mistyped sender could split one campaign into two groups, and adds a manual merge option.

### 9.3 Privacy in processing

Reported emails may contain personal information. Aiko's program stores only sender, subject fingerprint and report times, not message bodies or reporter names. The security team can open the original email in a controlled tool when needed. She documents what the program stores and why. Minimising stored data in automated tools reduces risk if the tool's database is ever exposed, and it reassures staff that reporting does not expose their own mail. She shares the stored-field list with staff representatives, who welcome it and agree to mention it when promoting the report button.

### Worked example

Aiko writes a tested triage program that groups duplicate reports with a dictionary, finds the first-report time and stores minimal data.

> **Synthetic case.** Reports are synthetic.

### Errors and limits

Fingerprints can split variants of one campaign. Minimal storage may limit later investigations.

### Exercises

- **EX025 — Grouping benefit.** Why group duplicate reports? *Rubric:* 3 = many reports of one email need only one investigation;; 2 = workload;; 1 = vague;; 0 = none.
- **EX026 — Lab grouping.** How many distinct emails did forty reports reduce to in the lab? *Rubric:* 3 = six, the top one first reported after 9 minutes;; 2 = six;; 1 = forty;; 0 = none.
- **EX027 — Stored fields.** What does the triage program store? *Rubric:* 3 = sender, subject fingerprint and report times only;; 2 = minimal;; 1 = bodies;; 0 = none.

### Synthesis

Well-structured triage code reduces workload and measures exposure while storing only what it needs.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering ethics to security awareness work; (2) design ethical phishing simulations; (3) balance safety duties with staff wellbeing.

### 10.1 Ethics in awareness work

Prof. Kerr reminds the class that engineers owe duties to the public, employers and colleagues. Awareness programmes affect people's dignity and trust. Phishing simulations, in particular, involve deception. Aiko learns that deception can be justified only when it serves a clear safety purpose, is approved by the organisation, avoids harm and is followed by honest explanation. Treating colleagues as adversaries to be caught undermines the cooperation that security depends on, as Adams and Sasse (1999) argued. She writes these conditions at the start of her simulation design notes.

### 10.2 An ethical simulation design

Aiko drafts rules for Greyford: simulations are approved by management and staff representatives; staff are told in general that simulations happen; no lures exploit fear about pay, health, family or redundancy; landing pages never ask for real passwords and record only that a link was opened; results are reported only in aggregate; nobody is disciplined for clicking; and everyone who clicks sees a short, kind explanation with how to report next time. She cites the NIST Phish Scale to keep difficulty consistent.

### 10.3 Safety and wellbeing

Greyford's control room operators handle safety-critical alarms. Aiko recommends that simulations never be sent to control room consoles during shifts, because distraction could affect water treatment. Instead, operators receive simulations on office accounts at quieter times. She also proposes a channel for staff to raise concerns about any simulation. Ethics and safety align here: a simulation that distracts an operator during an alarm would create a real risk to the public it is meant to protect. The plant manager approves the rule.

### Worked example

Aiko states conditions for justified deception, drafts seven ethical simulation rules and keeps simulations away from safety-critical consoles.

> **Synthetic case.** Rules and settings are synthetic; Adams and Sasse (1999) and the NIST Phish Scale are real.

### Errors and limits

Even ethical simulations can upset some staff. Rules need review as threats change.

### Exercises

- **EX028 — Justified deception.** When can deception in simulations be justified? *Rubric:* 3 = clear safety purpose, approval, no harm and honest explanation afterwards;; 2 = conditions;; 1 = always;; 0 = none.
- **EX029 — Forbidden lures.** Which lure themes are excluded? *Rubric:* 3 = pay, health, family and redundancy fears;; 2 = two;; 1 = vague;; 0 = none.
- **EX030 — Control room rule.** Why avoid simulations on control room consoles during shifts? *Rubric:* 3 = distraction could affect water treatment safety;; 2 = safety;; 1 = vague;; 0 = none.

### Synthesis

Ethical simulations are approved, transparent, harmless, blame-free and kept away from safety-critical work.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) explain how email authentication helps users; (2) relate protocol signals to what users see; (3) design warnings that people can act on.

### 11.1 Email authentication

Aiko studies how email moves across networks and how domains publish records that let receiving servers check whether a message really came from them. When checks fail, the receiving system can mark or reject the message. At Greyford, many phishing emails imitate the utility's own domain. Strong domain checks stop much of that before staff ever see it. Aiko notes that every attack stopped by a protocol is one that no person has to judge, which is the most reliable form of human factors design.

### 11.2 Signals users see

Some checks result in signals shown to users, such as a banner saying a message came from outside the organisation. Aiko examines how staff read the banner. Interviews show that because almost every supplier email carries it, staff ignore it. The signal is technically correct but carries little information. She proposes showing a stronger warning only for external senders using names similar to internal staff, which is rarer and more meaningful. She tests the idea on a month of synthetic mail logs and finds the stronger warning would appear on about two messages per person per month, rare enough to be noticed.

### 11.3 Actionable warnings

Aiko applies lessons from usable security research. Whitten and Tygar (1999) showed that security interfaces confuse users when they demand understanding of concepts users do not have. A good warning says what is wrong in plain words and offers one clear action, such as reporting the email. Aiko drafts a warning: "This sender is outside Greyford but uses a Greyford colleague's name. If unsure, press Report." She tests it with ten staff, eight of whom correctly choose to report. Two staff asked what Greyford colleague meant, so she adds an example.

### Worked example

Aiko explains domain checks, finds an ignored external banner and designs a rarer, actionable warning tested with staff.

> **Synthetic case.** Warnings and tests are synthetic; Whitten and Tygar (1999) is real.

### Errors and limits

Lookalike-name detection has false positives. Warnings lose force if overused.

### Exercises

- **EX031 — Protocol value.** Why are attacks stopped by protocols valuable for human factors? *Rubric:* 3 = no person has to judge them;; 2 = no judgement;; 1 = vague;; 0 = none.
- **EX032 — Ignored banner.** Why do staff ignore the external sender banner? *Rubric:* 3 = almost every supplier email carries it;; 2 = too frequent;; 1 = vague;; 0 = none.
- **EX033 — Warning test.** How many of ten staff chose to report with the new warning? *Rubric:* 3 = eight;; 2 = 8;; 1 = vague;; 0 = none.

### Synthesis

Protocols remove many decisions, and warnings work only when they are rare, specific and actionable.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) examine how operating system prompts affect behaviour; (2) reduce unnecessary security prompts; (3) design least-privilege defaults that people accept.

### 12.1 Prompts and habits

Aiko counts security prompts that Greyford's office laptops show in a week: update reminders, permission requests, certificate warnings and administrator prompts. Staff see dozens. Most are routine, so people click through them by habit. When a rare dangerous prompt appears, the habit carries over. Herley (2009) argued that asking users to evaluate frequent warnings that are mostly harmless is a poor bargain for them. Reducing routine prompts makes the important ones stand out. She records the weekly count per laptop as a baseline before changing anything, so the effect of later changes can be measured.

### 12.2 Removing prompts

Aiko works with the IT team to remove prompts. Updates install automatically outside working hours. Common software is pre-approved, so staff need not request administrator rights to install it. Certificate warnings for internal systems are eliminated by fixing the internal certificates. After the changes, weekly prompts per laptop fall sharply. Staff notice fewer interruptions, and the IT team receives fewer help desk calls about prompts. She measures the change by counting prompts on ten laptops for a week before and after, and shares the results with staff along with a short explanation of which prompts still matter and why they should read them.

### 12.3 Accepted least privilege

Removing local administrator rights often meets resistance. Aiko designs an approach staff accept: a self-service catalogue for approved software, a fast request route for anything else with a response within one working hour, and temporary rights for engineers who need them for specific tasks. Least privilege succeeds when its costs to staff are low. She measures acceptance by counting requests and complaints for a month after the change. She also asks staff representatives to review the approach before launch, and they suggest adding commonly used engineering tools to the catalogue, which reduces requests in the first month.

### Worked example

Aiko counts weekly prompts, removes routine ones through automation and pre-approval, and designs least privilege with a catalogue and fast requests.

> **Synthetic case.** Counts and processes are synthetic; Herley (2009) is real.

### Errors and limits

Automatic updates can break software. Temporary rights need expiry checks.

### Exercises

- **EX034 — Habit risk.** Why are frequent routine prompts dangerous? *Rubric:* 3 = habitual clicking carries over to rare dangerous prompts;; 2 = habit;; 1 = vague;; 0 = none.
- **EX035 — Certificate fix.** How were internal certificate warnings removed? *Rubric:* 3 = by fixing internal certificates;; 2 = fix certs;; 1 = ignore;; 0 = none.
- **EX036 — Acceptance design.** What makes least privilege acceptable to staff? *Rubric:* 3 = self-service catalogue, one-hour requests and temporary rights;; 2 = low cost;; 1 = vague;; 0 = none.

### Synthesis

Fewer, meaningful prompts and low-cost least privilege make secure operating systems usable.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) design a data model for awareness and reporting data; (2) apply minimisation and retention; (3) prevent misuse of behaviour data.

### 13.1 A data model

Aiko designs a small database for Greyford's awareness programme. Tables hold campaigns, lure difficulty ratings, aggregate results by group and reported email fingerprints. She deliberately omits a table linking individual staff to simulation clicks. Prof. Kerr asks why; Aiko explains that individual click records invite misuse, such as appearing in performance reviews, and are not needed to evaluate the programme. Design choices in data systems encode policy decisions about how people will be treated. She presents the schema to human resources and staff representatives before building it.

### 13.2 Minimisation and retention

Where individual data is unavoidable, such as training completion required by regulation, Aiko stores only completion dates, not quiz scores. Records are deleted two years after a person leaves. Aggregate results are kept longer for trend analysis. She documents each field's purpose and retention in a data dictionary. ISO/IEC 27001:2022 expects information to be handled according to agreed rules, and a data dictionary is an easy way to show what the rules are. She reviews the dictionary with the data protection officer, who signs it off.

### 13.3 Preventing misuse

Aiko adds controls: only two security staff can query the database; every query is logged; and group results are suppressed below twenty people. She also writes a policy statement, approved by human resources and staff representatives, that awareness data will not be used for discipline. Technical and policy controls together build the trust that keeps staff reporting their mistakes, which is the behaviour the programme most needs. She also schedules an annual review of the query logs by someone outside the security team, so that any attempt to look up individuals or bypass the twenty-person threshold would be noticed and challenged.

### Worked example

Aiko designs an awareness database without individual click records, sets minimisation and retention rules and adds access, logging and use limits.

> **Synthetic case.** The database is synthetic; ISO/IEC 27001:2022 is real.

### Errors and limits

Regulators may require individual records. Aggregation thresholds can be bypassed by repeated queries.

### Exercises

- **EX037 — Omitted table.** Which table did Aiko deliberately omit? *Rubric:* 3 = individual staff linked to simulation clicks;; 2 = click table;; 1 = vague;; 0 = none.
- **EX038 — Completion record.** What is stored for required training completion? *Rubric:* 3 = completion dates only, not quiz scores;; 2 = dates;; 1 = scores;; 0 = none.
- **EX039 — Use policy.** What did the approved policy statement say? *Rubric:* 3 = awareness data will not be used for discipline;; 2 = no discipline;; 1 = vague;; 0 = none.

### Synthesis

Data system design encodes how people are treated, so minimise, restrict and limit use of behaviour data.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) apply user-centred design to a security feature; (2) run usability tests; (3) track usability defects like other defects.

### 14.1 User-centred design

Greyford wants a new report button in its email system. Aiko follows a user-centred process: interview users, sketch options, test prototypes and refine. Interviews show field engineers read email mostly on phones, often with gloves or in bright light. A small icon hidden in a menu would fail them. Her design places a large report button at the top of each message on both desktop and mobile. Software engineering practices apply to security features just as they do to any other feature.

### 14.2 Usability testing

Aiko tests the prototype with eight staff from different roles. Each is asked to report a suspicious email while she watches without helping. She records time taken and errors. Desktop users report in under five seconds; two mobile users struggle because the button scrolls off screen. She fixes the button so it stays visible. Small tests with real users find problems that designers cannot see because they already know how the feature works. She repeats the mobile test after the fix, and all eight participants succeed quickly.

### 14.3 Tracking usability defects

Aiko logs usability problems in the same defect tracker as functional bugs, with severity based on how many users fail and how important the task is. The scrolling button is a high-severity defect because reporting is the feature's main purpose. Treating usability problems as defects ensures they are fixed before release, rather than being left as matters of taste. Sasse, Brostoff and Weirich (2001) argued that security which people cannot use effectively is not effective security. The defect is fixed before release.

### Worked example

Aiko designs a report button through interviews and prototypes, tests it with eight users, fixes a mobile defect and tracks usability as defects.

> **Synthetic case.** Tests are synthetic; Sasse et al. (2001) is real.

### Errors and limits

Eight testers miss rare issues. Lab tests differ from real field conditions.

### Exercises

- **EX040 — Field conditions.** What conditions affect field engineers' email use? *Rubric:* 3 = phones, gloves and bright light;; 2 = conditions;; 1 = vague;; 0 = none.
- **EX041 — Mobile defect.** What usability defect did testing find? *Rubric:* 3 = the mobile report button scrolled off screen;; 2 = scrolling;; 1 = vague;; 0 = none.
- **EX042 — Defect severity.** Why was the scrolling problem high severity? *Rubric:* 3 = reporting is the feature's main purpose;; 2 = core task;; 1 = cosmetic;; 0 = none.

### Synthesis

Security features need user-centred design, usability testing and defect tracking like any other software.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) relate core security concepts to human behaviour; (2) recognise social engineering techniques; (3) map human-targeted threats at Greyford.

### 15.1 Concepts and people

Aiko connects confidentiality, integrity and availability to human actions. A field engineer sharing a password harms confidentiality; an operator acting on a forged instruction harms integrity; a ransomware infection started by a malicious attachment harms availability. People appear in every part of security, as attackers, targets and defenders. Seeing people as defenders as well as targets changes design priorities towards supporting good behaviour rather than only restricting bad behaviour. She writes one example of a person as defender for each goal, such as an engineer reporting a strange vendor call before acting on it.

### 15.2 Social engineering

Aiko studies how attackers manipulate people. Cialdini's (2021) principles of influence, such as authority, urgency, scarcity, reciprocity, liking and social proof, explain why lures work. Hadnagy (2018) describes how social engineers combine research about targets with these principles. A fake message from the chief executive asking for an urgent payment uses authority and urgency together. Recognising the principles helps staff spot pressure, and it helps designers add pauses where pressure is likely. She builds a one-page table mapping each principle to a typical lure and a simple pause that interrupts it, which becomes part of later training.

### 15.3 Threats at Greyford

Aiko maps human-targeted threats: phishing for remote access credentials, phone calls pretending to be vendors asking operators to change settings, invoice fraud against finance and tailgating at depots. For each she notes the influence principle used and the control that removes reliance on judgement, such as callback verification for vendor requests. The Verizon Data Breach Investigations Report (2024) is one annual source that tracks the human element in breaches, which she cites as context rather than as Greyford data. She keeps the map short enough to review each quarter.

### Worked example

Aiko links security goals to human actions, applies influence principles to lures and maps four human-targeted threats with controls.

> **Synthetic case.** Threats at Greyford are synthetic; Cialdini (2021), Hadnagy (2018) and the Verizon DBIR (2024) are real.

### Errors and limits

Influence principles explain but do not predict individual behaviour. Industry reports may not match a utility's risks.

### Exercises

- **EX043 — People as defenders.** Why see people as defenders too? *Rubric:* 3 = it shifts design towards supporting good behaviour;; 2 = support;; 1 = vague;; 0 = none.
- **EX044 — CEO lure.** Which principles does a fake urgent CEO payment request combine? *Rubric:* 3 = authority and urgency;; 2 = two;; 1 = vague;; 0 = none.
- **EX045 — Vendor call control.** Which control addresses fake vendor phone calls? *Rubric:* 3 = callback verification using a known number;; 2 = callback;; 1 = vague;; 0 = none.

### Synthesis

People are targets and defenders; understanding influence helps design controls that reduce reliance on judgement under pressure.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) treat people as components of a socio-technical system; (2) allocate functions between people and machines; (3) write requirements that include human performance.

### 16.1 Socio-technical systems

Prof. Kerr introduces systems engineering: defining needs, requirements, architecture, verification and operation across the whole life cycle. Aiko learns that a security system at Greyford includes people, procedures and technology working together. A remote access system is not just software; it includes the engineers who use it, the help desk that resets their accounts and the manager who approves access. Treating people as part of the system, rather than as external users, makes their limits and strengths part of the design rather than an afterthought.

### 16.2 Allocating functions

A classic systems engineering question is which tasks machines should do and which people should do. Aiko applies it to phishing defence. Filtering known bad emails, checking sender domains and grouping duplicate reports suit machines, which are fast and consistent. Judging unusual but plausible requests, such as an unexpected vendor instruction, suits people who know the context. She allocates each function and notes that people should not be asked to do what machines do better, such as checking every link by hand.

### 16.3 Human performance requirements

Aiko writes requirements that include people: a field engineer must be able to report a suspicious email in under ten seconds on a phone; a help desk agent must verify a caller's identity using a procedure that takes less than two minutes; an operator must never be required to enter a password while acknowledging a critical alarm. Each requirement is measurable and testable. NIST SP 800-160 Vol. 1 Rev. 1 describes systems security engineering across the life cycle, and Aiko notes that human performance belongs in those requirements alongside technical ones.

### Worked example

Aiko treats people as system components, allocates phishing defence functions between machines and people, and writes measurable human performance requirements.

> **Synthetic case.** Requirements are synthetic; SP 800-160 Vol. 1 Rev. 1 is real.

### Errors and limits

Function allocation changes as tools improve. Time limits may not suit every staff member.

### Exercises

- **EX046 — People as components.** What does treating people as system components change? *Rubric:* 3 = their limits and strengths become part of the design;; 2 = design input;; 1 = vague;; 0 = none.
- **EX047 — Machine functions.** Which phishing defence functions suit machines? *Rubric:* 3 = filtering known bad mail, domain checks, grouping reports;; 2 = two;; 1 = judging context;; 0 = none.
- **EX048 — Alarm requirement.** What does the operator requirement forbid? *Rubric:* 3 = entering a password while acknowledging a critical alarm;; 2 = password at alarm;; 1 = vague;; 0 = none.

### Synthesis

Systems engineering includes people as components, allocates tasks sensibly and writes testable human requirements.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) apply feedback loops to security behaviour; (2) design timely feedback for reporting; (3) avoid unstable or punitive feedback.

### 17.1 Feedback loops

In control engineering, a feedback loop measures an output and adjusts an input to keep the system on target. Aiko applies this idea to behaviour. When staff report a suspicious email, they act; if they hear nothing back, the loop is open and they may stop reporting. If they receive a quick thank-you and later learn what the email was, the loop closes and reporting is reinforced. She sketches Greyford's reporting process as a loop and finds that reporters currently receive no response at all.

### 17.2 Designing timely feedback

Aiko designs feedback with three parts: an automatic thank-you within a minute, a short message when the security team confirms the email was malicious or safe, and a monthly summary showing how reports helped. Timeliness matters: feedback weeks later does little to reinforce behaviour. She estimates that automation can deliver the first two parts without extra staff time. The design mirrors control principles: measure quickly, respond quickly and keep the loop simple. She writes the three messages in plain language and asks five staff whether they would find them useful, adjusting the wording after their comments.

### Lab — Simulating reporting with and without feedback

```python
# Illustrative simulation of monthly reporting rate with and without feedback (synthetic dynamics).
def run(feedback, months=12, r=0.30):
    out = []
    for _ in range(months):
        target = 0.60 if feedback else 0.15
        r += 0.35 * (target - r) if feedback else 0.12 * (target - r)
        out.append(r)
    return out
for name, fb in (("no feedback", False), ("quick feedback", True)):
    s = run(fb); print(f"{name:14} month 3 {s[2]:.0%}, month 6 {s[5]:.0%}, month 12 {s[11]:.0%}")
```

Run with `python3 lab_feedback.py`. Verified output:

```text
no feedback    month 3 25%, month 6 22%, month 12 18%
quick feedback month 3 52%, month 6 58%, month 12 60%
```

### 17.3 Unstable or punitive loops

Feedback can also harm. If staff who click a simulation receive harsh messages or are reported to managers, they learn to hide mistakes, and the loop drives the wrong behaviour. Excessive feedback, such as daily emails, causes people to ignore all messages. The lab simulates reporting under no feedback and quick feedback, showing that with feedback the reporting rate rises and stabilises, while without it the rate drifts down. Aiko notes the simulation's assumptions are illustrative, not measured. She recommends a monthly maximum for feedback messages.

### Worked example

Aiko models reporting as a feedback loop, designs three-part timely feedback and simulates its effect while warning against punitive or excessive loops.

> **Synthetic case.** Simulation parameters are synthetic.

### Errors and limits

Simple loop models omit social influences. Automated thanks can feel insincere.

### Exercises

- **EX049 — Open loop.** What happens when reporters hear nothing back? *Rubric:* 3 = the loop is open and reporting may decline;; 2 = decline;; 1 = vague;; 0 = none.
- **EX050 — Feedback parts.** What are the three parts of the feedback design? *Rubric:* 3 = instant thank-you, confirmation of verdict and monthly summary;; 2 = two;; 1 = vague;; 0 = none.
- **EX051 — Lab outcome.** How did reporting differ in the lab after 12 months? *Rubric:* 3 = 60% with feedback versus 18% without;; 2 = higher;; 1 = vague;; 0 = none.

### Synthesis

Closing the feedback loop quickly and kindly sustains reporting, while punitive or excessive feedback destabilises it.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) place human factors in security architecture; (2) design layered defences that tolerate human error; (3) use zero trust ideas to reduce reliance on vigilance.

### 18.1 Human factors in architecture

Aiko studies how architecture choices shape what people must do. If one stolen password gives access to everything, every staff member must be perfect all the time. If access is segmented and checked continuously, a single mistake has limited impact. NIST SP 800-207 describes zero trust as removing implicit trust based on network location and evaluating each access request. Aiko sees it as a human factors design: it reduces the cost of individual errors, which are inevitable in a large workforce. She explains this view to the IT team.

### 18.2 Layered defences

Aiko designs layers for Greyford's remote access: email filtering removes most phishing; phishing-resistant authentication with security keys stops stolen passwords from working; device checks block unmanaged laptops; monitoring detects unusual access; and staff reporting provides early warning. Each layer catches some failures of the others. She emphasises that staff are one layer among many, not the last line of defence, a framing that reduces pressure and blame on individuals. She draws the layers as a simple diagram for the board, showing which threat each layer addresses and how a failure in one is caught by another, so that nobody assumes a single control is enough.

### 18.3 Reducing reliance on vigilance

Aiko lists places where Greyford relies on staff noticing something: checking sender names, spotting fake login pages and verifying payment changes. For each, she asks whether architecture can remove the need. Security keys make fake login pages ineffective because the key will not authenticate to the wrong site. Payment changes require callback verification by a second person. Saltzer and Schroeder (1975) recommended designs that do not depend on users being constantly careful, and Aiko finds that principle still fits modern systems. She lists the remaining reliances for review.

### Worked example

Aiko applies zero trust as a human factors design, layers defences so staff are one layer among many and removes several reliances on vigilance.

> **Synthetic case.** Greyford's design is synthetic; SP 800-207 and Saltzer and Schroeder (1975) are real.

### Errors and limits

Layers add cost and complexity. Removing vigilance needs may reduce staff engagement if poorly explained.

### Exercises

- **EX052 — Single password risk.** What happens if one stolen password gives access to everything? *Rubric:* 3 = every staff member must be perfect all the time;; 2 = perfection;; 1 = vague;; 0 = none.
- **EX053 — Staff as a layer.** How does Aiko position staff in the layered design? *Rubric:* 3 = as one layer among many, not the last line of defence;; 2 = one layer;; 1 = last line;; 0 = none.
- **EX054 — Security key benefit.** How do security keys reduce reliance on vigilance? *Rubric:* 3 = they will not authenticate to fake login pages;; 2 = phishing-resistant;; 1 = vague;; 0 = none.

### Synthesis

Architecture that tolerates human error reduces pressure on individuals and makes security more reliable.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) compare authentication methods by usability and security; (2) explain why phishing-resistant authentication helps people; (3) plan an authentication rollout with users.

### 19.1 Comparing methods

Aiko compares authentication options for Greyford: passwords, text message codes, app approvals, app codes and security keys. She assesses each for phishing resistance, speed, cost and failure modes. Passwords are easy to phish and often reused. Text codes can be intercepted or phished in real time. App approvals can be abused by repeated prompts until a tired user accepts. Security keys resist phishing because they use cryptography tied to the genuine site, and they are quick once staff learn them. She summarises the comparison in one table.

### 19.2 Cryptography users never see

Aiko explains to staff that a security key holds a private key that never leaves the device. When signing in, the site sends a challenge, the key signs it, and the site checks the signature with the matching public key. The key also checks the site's identity, so a fake site receives nothing useful. Staff do not need to understand this to benefit; they only need to touch the key. Good cryptographic design hides complexity while removing a judgement users were bad at making.

### 19.3 Rolling out with users

Aiko plans a rollout: pilot with twenty volunteers, collect problems, issue two keys per person with one stored safely, provide a quick recovery route at depots and train staff in five minutes using a short video. She avoids text message codes as fallback because they would reintroduce phishing risk. She schedules the rollout outside winter, when burst pipes keep field staff busiest. Planning around people's work is as important as choosing the right technology. She also arranges for the pilot volunteers to act as local helpers in each depot, since colleagues often prefer to ask a peer before calling the help desk.

### Worked example

Aiko compares five authentication methods, explains security keys in plain terms and plans a staged rollout with spares, recovery and seasonal timing.

> **Synthetic case.** The rollout plan is synthetic.

### Errors and limits

Security keys need replacement logistics. Some systems may not support them yet.

### Exercises

- **EX055 — Prompt abuse.** How can app approvals be abused? *Rubric:* 3 = repeated prompts until a tired user accepts;; 2 = prompt fatigue;; 1 = vague;; 0 = none.
- **EX056 — Key and fake site.** Why does a fake site get nothing useful from a security key? *Rubric:* 3 = the key checks the site's identity before signing;; 2 = origin check;; 1 = vague;; 0 = none.
- **EX057 — No SMS fallback.** Why avoid text codes as fallback? *Rubric:* 3 = they would reintroduce phishing risk;; 2 = phishing;; 1 = cost;; 0 = none.

### Synthesis

Phishing-resistant authentication removes a hard judgement from people, if rollout respects how they work.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Human factors and cyber policy: engineering context

### Learning outcomes

You will (1) define the field of human factors and cyber policy; (2) relate policy to engineering decisions; (3) identify stakeholders at Greyford.

### 20.1 Defining the field

Aiko begins the specialist part of her course. Human factors and cyber policy studies how people interact with security, and how rules, programmes and laws shape that interaction. It covers usability of security tools, awareness and training, organisational culture, social engineering and policy design. Sasse, Brostoff and Weirich (2001) argued for an approach that treats users as partners and designs security around them. Aiko notes the field is engineering as much as psychology, because it produces requirements, designs and measurements. She writes a one-paragraph definition for her notebook.

### 20.2 Policy and engineering

Policies set requirements engineers must meet. Greyford's information security policy requires annual awareness training, strong authentication for remote access and reporting of incidents. NIST SP 800-50 Rev. 1 frames awareness and training as a learning programme with needs assessment, design, delivery and evaluation. Aiko sees that engineering choices determine whether policy is workable: a reporting requirement means little without an easy report button. She resolves to read policy as a set of design constraints and goals. She marks each policy clause with the design feature that makes it achievable, and finds two clauses with no supporting feature at all.

### 20.3 Stakeholders

Aiko lists stakeholders: operators, field engineers, office staff, managers, the security team, human resources, staff representatives, the regulator for water services and the public who depend on safe water. Each has interests. Operators want minimal interruption; human resources wants fair treatment; the regulator wants evidence of good practice; the public wants safe, reliable water. She records these in a stakeholder table. Prof. Kerr notes that human factors work fails when it serves one stakeholder, usually management, and ignores the rest. She adds contractors after a reminder.

### Worked example

Aiko defines the field, reads policy as design constraints and maps nine stakeholder groups with their interests.

> **Synthetic case.** Greyford's policy is synthetic; Sasse et al. (2001) and SP 800-50 Rev. 1 are real.

### Errors and limits

Stakeholder lists can omit quiet groups such as contractors. Policy summaries simplify legal duties.

### Exercises

- **EX058 — Field scope.** Name three topics within human factors and cyber policy. *Rubric:* 3 = usability, awareness and training, culture, social engineering, policy design;; 2 = two;; 1 = vague;; 0 = none.
- **EX059 — Policy as constraints.** How does Aiko choose to read policy? *Rubric:* 3 = as design constraints and goals;; 2 = constraints;; 1 = rules only;; 0 = none.
- **EX060 — Failure mode.** When does human factors work fail, according to Prof. Kerr? *Rubric:* 3 = when it serves only one stakeholder;; 2 = one stakeholder;; 1 = vague;; 0 = none.

### Synthesis

Human factors and cyber policy is an engineering field that turns policy and stakeholder needs into workable designs.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Human factors and cyber policy: requirements

### Learning outcomes

You will (1) elicit human factors requirements from staff; (2) write them in testable form; (3) prioritise requirements with stakeholders.

### 21.1 Eliciting requirements

Aiko runs short workshops with operators, field engineers and office staff to learn what the awareness and reporting programme must achieve for them. She asks about recent suspicious emails, what made them hard to judge and what stopped them reporting. Operators say they cannot leave consoles to read long training. Engineers say they read email on phones in vans. Office staff say they fear looking foolish if they report a genuine email. Each statement becomes a candidate requirement grounded in real experience rather than assumptions made in the security office.

### 21.2 Testable requirements

Aiko rewrites each need as a testable requirement. Training modules for operators must take no more than five minutes and be usable during quiet periods. Reporting must work on phones in one tap. Every report, including those that turn out to be safe, must receive a thank-you within one minute. No simulation result may be shared with line managers by name. Each has a measure and a test. She avoids vague phrases such as staff should be aware, which cannot be verified and therefore cannot guide design.

### 21.3 Prioritising

With twenty candidate requirements and limited budget, Aiko holds a prioritisation session with representatives of each group and the security team. They rank requirements by risk reduced, staff benefit and cost. One-tap mobile reporting and fast thank-you messages rank highest because they are cheap and address the most common barrier. A full simulation platform ranks lower because the existing tool can be configured. She records the ranking and reasons so later decisions can refer back to them. The ranking is shared with all staff in a short note so that people can see their concerns were heard.

### Worked example

Aiko elicits needs from three staff groups, rewrites them as testable requirements and prioritises twenty with stakeholders.

> **Synthetic case.** Workshops and requirements are synthetic.

### Errors and limits

Workshop participants may not represent quieter staff. Rankings reflect who attends.

### Exercises

- **EX061 — Office fear.** What barrier did office staff describe? *Rubric:* 3 = fear of looking foolish if they report a genuine email;; 2 = embarrassment;; 1 = vague;; 0 = none.
- **EX062 — Vague requirement.** Why avoid "staff should be aware" as a requirement? *Rubric:* 3 = it cannot be verified;; 2 = untestable;; 1 = vague;; 0 = none.
- **EX063 — Top priorities.** Which requirements ranked highest? *Rubric:* 3 = one-tap mobile reporting and fast thank-you messages;; 2 = both;; 1 = platform;; 0 = none.

### Synthesis

Human factors requirements come from staff experience and must be testable and prioritised openly.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Human factors and cyber policy: system and data models

### Learning outcomes

You will (1) model the awareness programme as a system; (2) model data flows for reports and simulations; (3) identify where people make decisions.

### 22.1 The programme as a system

Aiko models Greyford's awareness programme as a system with inputs, processes and outputs. Inputs include threat intelligence, staff needs and policy requirements. Processes include training, simulations, reporting, triage and feedback. Outputs include faster reporting, fewer successful attacks and evidence for the regulator. Modelling the programme this way shows that training is only one process among several, and that the output Greyford cares about depends on reporting and triage working well together. She draws the model as a one-page diagram and uses it to explain to managers why investing only in training would leave most of the system unchanged and the outcomes they want largely unaffected.

### 22.2 Data flows

Aiko draws data flows: staff report emails to the triage system; triage sends verdicts back to reporters; simulation results flow as aggregates to a dashboard; training completion flows to human resources records. She marks where personal data appears and where it is aggregated. One flow worries her: the simulation tool exports individual results by default to a spreadsheet that managers can open. She recommends turning off the export and configuring aggregate reporting only, consistent with the policy from chapter 13. The vendor confirms the change can be locked by administrators.

### 22.3 Decision points

Aiko marks every point where a person makes a decision: an employee deciding whether to report, a triage analyst deciding whether an email is malicious, a manager deciding whether to approve access, and an operator deciding whether to act on a phone request. For each she notes what information the person has, how much time and what pressure. Decision points with little information and high pressure, such as urgent phone requests, are where social engineering succeeds, so they deserve design attention first.

### Worked example

Aiko models the programme as a system, maps data flows and stops an individual-results export, and marks decision points with their pressures.

> **Synthetic case.** Models and tools are synthetic.

### Errors and limits

Models omit informal channels like chat messages. Default settings change with tool updates.

### Exercises

- **EX064 — Programme output.** Which output does Greyford care about most? *Rubric:* 3 = faster reporting and fewer successful attacks;; 2 = outcomes;; 1 = completion;; 0 = none.
- **EX065 — Export problem.** What data flow worried Aiko? *Rubric:* 3 = individual simulation results exported to a manager spreadsheet;; 2 = export;; 1 = vague;; 0 = none.
- **EX066 — Risky decision points.** Which decision points deserve attention first? *Rubric:* 3 = those with little information and high pressure, like urgent phone requests;; 2 = pressure;; 1 = vague;; 0 = none.

### Synthesis

Modelling the programme as a system reveals data risks and the pressured decision points where attackers succeed.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Human factors and cyber policy: threat and failure analysis

### Learning outcomes

You will (1) analyse how social engineering attacks unfold; (2) classify human errors; (3) design defences for each failure type.

### 23.1 Attack sequences

Aiko analyses a realistic sequence: an attacker researches Greyford staff online, sends a field engineer a message impersonating a pump vendor about an urgent firmware issue, follows up with a phone call and asks the engineer to approve a remote session. Hadnagy (2018) describes such multi-step pretexting. Each step offers a chance to stop the attack: limiting what staff publish, verifying vendor contacts, calling back on known numbers and requiring approval from a second person for remote sessions. She draws the sequence as a timeline with each defensive opportunity marked.

### 23.2 Classifying errors

Aiko uses the distinction between slips, lapses and mistakes set out by Reason (1990). A slip is a wrong action, such as clicking the wrong button; a lapse is a memory failure, such as forgetting to lock a screen; a mistake is a wrong plan, such as believing a fake vendor is genuine. Each needs a different defence: slips need forgiving interfaces, lapses need reminders or automation, and mistakes need better information or verification. Classifying errors stops the default response of more training for every problem.

### 23.3 Defences by type

Aiko maps defences. For slips, the report button has an undo and a confirmation for sending sensitive files externally. For lapses, screens lock automatically and security keys remove forgotten passwords. For mistakes, vendor requests require callback verification, and staff receive short guidance on common pretexts. She also notes violations, deliberate rule-breaking, which often signal unworkable rules rather than bad intent, as Adams and Sasse (1999) found. Violations prompt her to review rules before reinforcing them. She presents the mapping as a table that the security team can extend when new incidents occur, so that each future failure is classified before a response is chosen.

### Worked example

Aiko analyses a multi-step pretext, classifies errors as slips, lapses and mistakes, and maps defences to each, treating violations as signals.

> **Synthetic case.** The attack is synthetic; Hadnagy (2018), Reason (1990) and Adams and Sasse (1999) are real.

### Errors and limits

Error categories overlap in practice. Attackers adapt to known verification steps.

### Exercises

- **EX067 — Pretext steps.** Which steps make up the vendor pretext? *Rubric:* 3 = online research, impersonating email, follow-up call, remote session request;; 2 = three;; 1 = vague;; 0 = none.
- **EX068 — Lapse defence.** What defends against lapses? *Rubric:* 3 = reminders or automation such as auto-lock;; 2 = automation;; 1 = training;; 0 = none.
- **EX069 — Violations as signals.** What do violations often signal? *Rubric:* 3 = unworkable rules rather than bad intent;; 2 = rule design;; 1 = malice;; 0 = none.

### Synthesis

Classifying failures guides the right defence for each, and violations point to rules that need redesign.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Human factors and cyber policy: methods I

### Learning outcomes

You will (1) run a cognitive walkthrough of a security task; (2) conduct a short survey responsibly; (3) combine methods to understand a problem.

### 24.1 Cognitive walkthrough

Aiko uses a cognitive walkthrough on Greyford's password reset process. She steps through each action a user must take, asking whether the user will know what to do, see how to do it, understand feedback and know they have succeeded. She finds that the reset page asks for an employee number most field staff do not remember, and the confirmation message is ambiguous. Walkthroughs are quick, need no participants and find many problems early, though they rely on the evaluator imagining the user accurately.

### 24.2 A responsible survey

Aiko surveys staff about reporting barriers. The survey is anonymous, short and voluntary, and it asks about experiences rather than testing knowledge. She avoids leading questions and includes an open question for comments. She reports results only for groups of twenty or more. One hundred and eighty staff respond. The most common barrier is not knowing whether something is suspicious enough to report, followed by not knowing how to report on a phone. She shares the headline results with all staff within two weeks, thanking them and explaining what will change, so that respondents see their answers had an effect.

### Lab — Barrier counts and shares from survey responses

```python
# Count reporting barriers from an anonymous survey (synthetic multi-select, n=180).
n = 180
barriers = {"unsure if suspicious enough": 71, "don't know how to report on phone": 48, "worried about looking foolish": 33,
            "no time": 29, "never get feedback": 41, "didn't know reporting existed": 12}
for b, c in sorted(barriers.items(), key=lambda x: -x[1]): print(f"{b:34} {c:3d}/{n} = {c/n:.0%}")
```

Run with `python3 lab_survey.py`. Verified output:

```text
unsure if suspicious enough         71/180 = 39%
don't know how to report on phone   48/180 = 27%
never get feedback                  41/180 = 23%
worried about looking foolish       33/180 = 18%
no time                             29/180 = 16%
didn't know reporting existed       12/180 = 7%
```

### 24.3 Combining methods

The walkthrough found usability problems; the survey found uncertainty about when to report. Together they suggest two fixes: improve the reset and reporting interfaces, and tell staff clearly that any doubt is a good reason to report. Aiko notes that neither method alone would have shown both. She plans usability testing with real users next, since walkthroughs and surveys describe problems but do not show how people actually behave when using the system. She records how each finding was obtained, so readers know which claims rest on expert review and which on staff reports, and she schedules the usability tests for the following month.

### Worked example

Aiko walks through a reset task finding two problems, surveys reporting barriers responsibly and combines both methods into two fixes.

> **Synthetic case.** Survey and findings are synthetic.

### Errors and limits

Walkthroughs depend on evaluator imagination. Surveys measure perceptions, not behaviour.

### Exercises

- **EX070 — Walkthrough question.** What four questions guide each walkthrough step? *Rubric:* 3 = know what to do, see how, understand feedback, know success;; 2 = three;; 1 = vague;; 0 = none.
- **EX071 — Top barrier.** What was the most common reporting barrier in the lab? *Rubric:* 3 = unsure whether suspicious enough: 71 of 180;; 2 = uncertainty;; 1 = phone;; 0 = none.
- **EX072 — Clear message.** What message addresses that barrier? *Rubric:* 3 = any doubt is a good reason to report;; 2 = doubt;; 1 = vague;; 0 = none.

### Synthesis

Combining quick evaluation methods with responsible surveys reveals both interface and understanding problems.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) design a reporting and feedback service in a team; (2) critique designs in a studio setting; (3) iterate based on feedback.

### 25.1 The studio brief

Prof. Kerr runs a design studio. Aiko's team of four must design a reporting and feedback service for a fictional regional transport operator with drivers, depot staff and office teams. Requirements include one-tap reporting, fast feedback and no individual blame. The team includes a computer science student, a psychology student and a design student. Working across disciplines brings different ideas: the psychology student suggests framing reports as helping colleagues rather than as security duty. The team agrees roles and a schedule in the first meeting, with each member leading one part of the design.

### 25.2 Studio critique

In the midpoint critique, other teams and two practitioners review the designs. A practitioner points out that drivers cannot use phones while driving, so reporting must also work from depot terminals and by a simple phone call to a hotline. Another reviewer questions whether the monthly summary will be read. Aiko's team listens without defending and records each comment. Critique works when designers treat it as information rather than as attack. They sort the comments into must-fix and could-improve groups before the next session, and agree who will address each one.

### 25.3 Iterating

The team revises. They add depot terminal reporting and a hotline, shorten the monthly summary to three items with a picture, and test the new framing with five depot staff, who prefer it. They document what changed and why. At the final critique, practitioners note the design now fits drivers' working day. Aiko learns that iteration based on real constraints produces designs people actually use. They also keep a short change log listing every revision, the comment that prompted it and the result of the small test with depot staff, which the final reviewers use to see how the design evolved.

### Worked example

Aiko's team designs a reporting service for a transport operator, takes studio critique about drivers and iterates with terminals, a hotline and a shorter summary.

> **Synthetic case.** The transport operator and team are synthetic.

### Errors and limits

Studio projects lack real deployment pressures. Small tests may favour novelty.

### Exercises

- **EX073 — Psychology framing.** What framing did the psychology student suggest? *Rubric:* 3 = reporting as helping colleagues;; 2 = helping;; 1 = duty;; 0 = none.
- **EX074 — Driver constraint.** What constraint did the practitioner raise? *Rubric:* 3 = drivers cannot use phones while driving;; 2 = driving;; 1 = vague;; 0 = none.
- **EX075 — Design changes.** Name two changes after critique. *Rubric:* 3 = depot terminal reporting, hotline, shorter summary;; 2 = two;; 1 = vague;; 0 = none.

### Synthesis

Studio critique from people who know real constraints drives designs that fit actual work.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Human factors and cyber policy: architecture alternatives

### Learning outcomes

You will (1) compare alternative architectures for a security awareness programme; (2) weigh alternatives against human and organisational criteria; (3) justify a choice openly.

### 26.1 Three alternatives

Aiko compares three ways Greyford could organise its programme. The first is compliance-led: an annual online course and quarterly simulations measured by completion and click rates. The second is reporting-led: easy reporting, fast feedback, short monthly refreshers and simulations measured by reporting speed. The third is design-led: invest mainly in technical changes that remove decisions from staff, such as security keys and stronger filtering, with minimal training. Each reflects a different theory of what makes people secure, and each has strengths that the others lack.

### 26.2 Criteria and scoring

Aiko scores the alternatives against criteria agreed with stakeholders: risk reduction, staff burden, cost, regulatory evidence and staff trust. The lab computes weighted totals. The design-led option scores highest on risk and burden but weakest on regulatory evidence, because the regulator expects some training records. The reporting-led option scores well across most criteria. The compliance-led option scores best only on ease of producing evidence, which matches the critique by Bada, Sasse and Nurse (2019) that such campaigns rarely change behaviour. Stakeholders set the weights before seeing any scores, which prevents the weights being tuned to favour an option.

### Lab — Weighted comparison of three programme designs

```python
# Weighted comparison of three awareness programme designs (synthetic 1-5 scores).
w = {"risk": 0.30, "burden": 0.20, "cost": 0.15, "evidence": 0.15, "trust": 0.20}
s = {"compliance": {"risk": 2, "burden": 2, "cost": 4, "evidence": 5, "trust": 2},
     "reporting": {"risk": 4, "burden": 4, "cost": 4, "evidence": 3, "trust": 4},
     "design": {"risk": 5, "burden": 5, "cost": 2, "evidence": 2, "trust": 4}}
def tot(wt): return {o: sum(wt[c] * v for c, v in sc.items()) / sum(wt.values()) for o, sc in s.items()}
print("base:", {o: round(v, 2) for o, v in tot(w).items()})
print("evidence weight doubled:", {o: round(v, 2) for o, v in tot(dict(w, evidence=0.30)).items()})
```

Run with `python3 lab_options.py`. Verified output:

```text
base: {'compliance': 2.75, 'reporting': 3.85, 'design': 3.9}
evidence weight doubled: {'compliance': 3.04, 'reporting': 3.74, 'design': 3.65}
```

### 26.3 An open choice

Aiko recommends a hybrid: design-led technical changes combined with the reporting-led programme, keeping short training that also produces the records the regulator needs. She explains the trade-offs openly: the hybrid costs more in the first year, but reduces burden and risk. She notes that the weights reflect stakeholder judgements, and shows that the recommendation holds when the weight on regulatory evidence is doubled: the totals become 3.74 for reporting-led and 3.65 for design-led, both still well above compliance-led at 3.04, so the two components of the hybrid remain the strongest. The board approves the hybrid and asks for evaluation after twelve months.

### Worked example

Aiko compares compliance-led, reporting-led and design-led programmes on five weighted criteria and recommends a hybrid with a sensitivity check.

> **Synthetic case.** Scores and weights are synthetic; Bada et al. (2019) is real.

### Errors and limits

Scores are judgements. Hybrid designs can lose focus if not managed.

### Exercises

- **EX076 — Design-led weakness.** Where does the design-led option score weakest? *Rubric:* 3 = regulatory evidence;; 2 = evidence;; 1 = risk;; 0 = none.
- **EX077 — Weighted totals.** What were the weighted totals in the lab? *Rubric:* 3 = compliance 2.75, reporting 3.85, design 3.90;; 2 = ordering;; 1 = vague;; 0 = none.
- **EX078 — Hybrid robustness.** How did Aiko test the hybrid recommendation? *Rubric:* 3 = doubling the regulatory evidence weight;; 2 = sensitivity;; 1 = vague;; 0 = none.

### Synthesis

Comparing programme architectures on agreed criteria leads to an open, tested choice, often a hybrid.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Human factors and cyber policy: control design

### Learning outcomes

You will (1) design controls that support people rather than test them; (2) apply nudges ethically; (3) design verification procedures for high-risk requests.

### 27.1 Supporting controls

Aiko designs controls that help staff do the right thing. Payment change requests trigger an automatic hold and a callback by a second person using a number from the supplier file, not from the request. Remote vendor sessions require a ticket number and approval in the maintenance system. External emails with names matching staff show a specific warning. Each control removes the need for a lone judgement under pressure. Saltzer and Schroeder (1975) called this psychological acceptability: controls that are easy to use correctly are used correctly.

### 27.2 Ethical nudges

Aiko considers nudges, small design changes that make the secure choice easier or more visible. Examples include making the report button the most prominent action, setting secure defaults for file sharing and showing a short reminder when someone forwards internal files externally. She sets ethical limits: nudges must be transparent, easy to override when there is a good reason and never manipulative. A nudge that tricks people would damage trust and contradict the respect for staff that the programme depends on.

### 27.3 Verification procedures

For high-risk requests, such as changes to treatment plant settings requested by phone, Aiko writes a verification procedure: record the request, hang up, call back using the official number, confirm with a second engineer and log the outcome. The procedure takes about three minutes. She tests it with five engineers using role-play with a colleague acting as a caller, not a real deception exercise. All complete it correctly after one practice, and they suggest a laminated card by the phone. The card lists the official numbers and the steps in plain words.

### Worked example

Aiko designs payment, vendor and email controls that remove lone judgements, sets ethical limits on nudges and tests a callback procedure by role-play.

> **Synthetic case.** Controls and tests are synthetic; Saltzer and Schroeder (1975) is real.

### Errors and limits

Callback procedures fail if supplier files are wrong. Nudges lose effect over time.

### Exercises

- **EX079 — Callback number source.** Where must the callback number come from? *Rubric:* 3 = the supplier file, not the request;; 2 = known source;; 1 = the request;; 0 = none.
- **EX080 — Nudge limits.** What ethical limits apply to nudges? *Rubric:* 3 = transparent, easy to override and never manipulative;; 2 = two;; 1 = vague;; 0 = none.
- **EX081 — Role-play not deception.** How was the verification procedure tested? *Rubric:* 3 = role-play with a colleague acting as caller;; 2 = role-play;; 1 = real deception;; 0 = none.

### Synthesis

Controls should support people with easy, transparent steps that remove lone judgements under pressure.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Human factors and cyber policy: implementation I

### Learning outcomes

You will (1) implement the reporting button and feedback service; (2) manage organisational change; (3) launch with staff support.

### 28.1 Implementation

Aiko joins Greyford's IT team to implement the reporting service. They configure the email platform's report button on desktop and mobile, connect it to the triage tool, set up automatic thank-you messages and create templates for verdict messages. They test each path with synthetic emails before launch. They also set up the aggregate dashboard and remove the individual export, as planned in chapter 22. Implementation follows the requirements from chapter 21, which provide a checklist for acceptance. Each test result is logged with the date and the tester, so that later changes can be checked against the same paths and nothing is assumed to still work.

### 28.2 Managing change

Aiko knows that new processes fail when people do not understand why they exist. She writes a short explanation for staff: why reporting matters, what happens to reports and the promise that nobody is blamed for clicking. She briefs team leaders first so they can answer questions. Staff representatives co-sign the announcement. She avoids fear-based messages, which Bada, Sasse and Nurse (2019) identified as a reason campaigns fail, and focuses instead on how reporting protects colleagues and the public. Team leaders also receive a short list of likely questions with suggested answers.

### 28.3 Launch and support

The service launches on a Tuesday, avoiding Mondays when email volume is highest. Aiko staffs a help channel for the first two weeks and records questions. Most concern whether to report newsletters and supplier invoices. She updates guidance to say that unexpected invoices should be reported, while known newsletters can be ignored. Reports in the first week triple compared with the previous email address used for reporting, and the thank-you messages work on both desktop and mobile. The help channel log becomes the first source for the frequently asked questions page published a month later.

### Worked example

Aiko implements reporting and feedback, manages change through team leaders and co-signed messages, and launches with a help channel.

> **Synthetic case.** Implementation details and figures are synthetic; Bada et al. (2019) is real.

### Errors and limits

Launch spikes may fade. Help channels need staff time.

### Exercises

- **EX082 — Acceptance checklist.** What served as the acceptance checklist? *Rubric:* 3 = the requirements from chapter 21;; 2 = requirements;; 1 = vague;; 0 = none.
- **EX083 — Avoided message.** Which message style did Aiko avoid? *Rubric:* 3 = fear-based messages;; 2 = fear;; 1 = vague;; 0 = none.
- **EX084 — Common question.** What did most early questions concern? *Rubric:* 3 = whether to report newsletters and supplier invoices;; 2 = newsletters;; 1 = vague;; 0 = none.

### Synthesis

Implementation succeeds when technical setup is matched by clear, non-fear change management and early support.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Human factors and cyber policy: measurement

### Learning outcomes

You will (1) define outcome measures for the programme; (2) compute exposure time from report data; (3) avoid perverse incentives in metrics.

### 29.1 Outcome measures

Aiko defines measures for Greyford's programme: median time from arrival of a malicious email to first report; share of malicious emails reported by at least one person; share of reports that are genuine threats; staff burden from a quarterly two-question survey; and simulation click rate at fixed Phish Scale difficulty as a secondary measure. Each measure has a definition, a data source and an owner. She leads with reporting time because it relates directly to how long attacks remain active. Owners review their measures monthly with Aiko.

### 29.2 Computing exposure

The lab computes, for a month of synthetic malicious emails, the time to first report and the number of inboxes exposed until removal. Median time to first report is a few minutes, but two emails were never reported and were removed only when the filter vendor updated its rules hours later. Those two account for most of the exposure. Aiko recommends examining why they were not reported; both turn out to imitate an internal timesheet reminder that staff expected. She shares the finding with the filter vendor as well.

### Lab — Time to first report and inbox exposure

```python
# Time to first report and inbox-minutes of exposure for a month of malicious emails (synthetic).
emails = [("invoice lure", 40, 4, 30), ("mailbox full", 25, 6, 30), ("parcel", 60, 3, 25), ("ceo favour", 8, 11, 20),
          ("bank update", 35, 5, 30), ("timesheet reminder A", 120, None, 360), ("timesheet reminder B", 90, None, 300)]
# (name, recipients, minutes to first report or None, minutes to removal after report or after filter update)
total = 0; parts = []
for name, n, first, rem in emails:
    mins = (first + rem) if first is not None else rem
    exp = n * mins; total += exp; parts.append((name, first, exp))
firsts = sorted(f for _, f, _ in parts if f is not None)
print(f"median time to first report (reported emails): {firsts[len(firsts) // 2]} min; never reported: {sum(f is None for _, f, _ in parts)}")
unrep = sum(e for _, f, e in parts if f is None)
print(f"total inbox-minutes {total}; never-reported share {unrep / total:.0%}")
```

Run with `python3 lab_exposure.py`. Verified output:

```text
median time to first report (reported emails): 5 min; never reported: 2
total inbox-minutes 75613; never-reported share 93%
```

### 29.3 Perverse incentives

Aiko warns against targets that distort behaviour. A target to reduce click rates could be met by sending easier simulations less often. A target for report numbers could be met by encouraging staff to report everything, overloading triage. She proposes watching measures in pairs, such as report numbers alongside the share of genuine threats, and never tying individual pay or discipline to them. Measurement should help the programme learn, not create games. She writes these rules into the programme charter so that future managers cannot quietly introduce individual targets, and she asks the board to review the measures each year to check they still serve learning.

### Worked example

Aiko defines five measures with owners, computes reporting time and exposure from synthetic data, and pairs measures to avoid perverse incentives.

> **Synthetic case.** Data are synthetic; the Phish Scale is real.

### Errors and limits

Unreported emails are only found if detected another way. Paired measures still need judgement.

### Exercises

- **EX085 — Lead measure.** Why lead with reporting time? *Rubric:* 3 = it relates directly to how long attacks stay active;; 2 = exposure;; 1 = vague;; 0 = none.
- **EX086 — Lab exposure.** How much exposure came from the two unreported emails? *Rubric:* 3 = two never-reported emails caused 93% of inbox-minutes exposure;; 2 = most exposure;; 1 = vague;; 0 = none.
- **EX087 — Paired measures.** Why watch measures in pairs? *Rubric:* 3 = to stop one target being gamed at another's expense;; 2 = gaming;; 1 = vague;; 0 = none.

### Synthesis

Measures centred on exposure, watched in pairs and kept away from individual consequences help a programme learn.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify the reporting service against requirements; (2) run usability verification with participants; (3) record evidence of verification.

### 30.1 Requirements verification

In the verification laboratory, Aiko checks each requirement from chapter 21. She sends synthetic test emails and reports them from desktop and mobile, timing thank-you messages. She checks that the dashboard shows only groups of twenty or more and that no individual export exists. She confirms operator training modules take under five minutes. Each check produces a pass or fail with evidence such as timestamps or screenshots. Verification turns requirements into proof rather than assumption. Tests are run twice on different days to rule out chance timing effects, and any result close to a threshold is repeated.

### 30.2 Usability verification

Aiko recruits eight staff volunteers to complete tasks: report an email on a phone, find the verdict message and find guidance on what to report. She measures success and time without helping. Seven succeed on all tasks; one cannot find the guidance because it is linked only from the intranet. She adds a link to the thank-you message. Usability verification checks that requirements were met in a way real people can use, which technical checks alone cannot confirm. She also records where volunteers hesitated, even when they succeeded.

### Lab — Requirement verification results

```python
# Requirement verification results, before and after fixing a notification setting (synthetic).
reqs = ["one-tap mobile report", "thank-you within 1 minute (desktop)", "thank-you within 1 minute (mobile)",
        "dashboard groups >= 20 only", "no individual export", "operator module <= 5 minutes"]
round1 = [True, True, False, True, True, True]
for r, ok in zip(reqs, round1): print(f"{'PASS' if ok else 'FAIL'} {r}")
print(f"round 1: {sum(round1)}/{len(reqs)}; round 2 after notification fix: {len(reqs)}/{len(reqs)}")
```

Run with `python3 lab_verify.py`. Verified output:

```text
PASS one-tap mobile report
PASS thank-you within 1 minute (desktop)
FAIL thank-you within 1 minute (mobile)
PASS dashboard groups >= 20 only
PASS no individual export
PASS operator module <= 5 minutes
round 1: 5/6; round 2 after notification fix: 6/6
```

### 30.3 Recording evidence

Aiko records results in a verification table linking each requirement to its test, date, result and evidence. One requirement fails at first: mobile thank-you messages take three minutes on one phone model because of a notification setting. The IT team changes the setting and the retest passes. The table becomes evidence for the regulator and a baseline for re-verification after future changes. Prof. Kerr notes that recorded failures make verification more credible. The table is stored with the requirements document and version controlled, so that each future release can be verified against the same tests and any change in results can be traced.

### Worked example

Aiko verifies requirements with timed tests, verifies usability with eight volunteers, fixes a guidance link and a notification delay, and records evidence.

> **Synthetic case.** Tests and results are synthetic.

### Errors and limits

Volunteers may be more confident than typical staff. Phone models vary widely.

### Exercises

- **EX088 — Dashboard check.** What did Aiko verify about the dashboard? *Rubric:* 3 = only groups of twenty or more and no individual export;; 2 = aggregation;; 1 = vague;; 0 = none.
- **EX089 — Usability fix.** What usability problem did one volunteer reveal? *Rubric:* 3 = guidance linked only from the intranet;; 2 = link;; 1 = vague;; 0 = none.
- **EX090 — Lab verification.** How many requirements passed in each verification round? *Rubric:* 3 = 5 of 6 passed, then 6 of 6 after the notification fix;; 2 = 5 then 6;; 1 = vague;; 0 = none.

### Synthesis

Verification proves requirements are met technically and usably, with recorded evidence including failures.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Human factors and cyber policy: implementation II

### Learning outcomes

You will (1) implement the payment and vendor verification controls; (2) integrate controls into existing workflows; (3) train staff in the new procedures.

### 31.1 Payment controls

Aiko works with the finance team to implement the payment verification control. The finance system now places an automatic hold on any change to supplier bank details and creates a task for a second officer, who must call the supplier using the number held in the supplier file. The hold cannot be released by the person who received the request. The finance team tests the workflow with ten synthetic change requests, including two that use urgent wording, and every request is held and verified before release.

### 31.2 Vendor session controls

For remote vendor sessions to operational technology, the IT team configures the remote access gateway so that a session can start only when a valid ticket number from the maintenance system is entered and an engineer has approved the ticket. This removes the opportunity for a caller to talk an operator into opening a session by phone. Vendors are informed in writing a month before the change, and two vendors ask for a test session, which the team arranges so that real maintenance is not disrupted on the day of change.

### 31.3 Training in procedures

Aiko writes short procedure guides and runs fifteen-minute sessions for finance officers and control room operators. Sessions use worked examples and role-play rather than tests, and participants practise the callback and ticket steps. She records questions and revises the guides twice. Following the advice in NIST SP 800-50r1 (Hansche et al., 2024), she treats role-based training for staff with specific duties as distinct from general awareness, so these sessions focus only on the steps those roles must perform. Attendance is recorded for the regulator.

### Worked example

Aiko implements a payment hold with second-officer callback, ticket-gated vendor sessions and short role-based training.

> **Synthetic case.** Procedures are synthetic; NIST SP 800-50r1 is real.

### Errors and limits

Second officers may approve without calling if busy. Vendors may resist ticket gates.

### Exercises

- **EX091 — Hold release.** Who cannot release the payment hold? *Rubric:* 3 = the person who received the request;; 2 = requester;; 1 = second officer;; 0 = none.
- **EX092 — Vendor gate.** What must exist before a vendor session starts? *Rubric:* 3 = a valid approved maintenance ticket;; 2 = ticket;; 1 = a phone call;; 0 = none.
- **EX093 — Role-based training.** How does role-based training differ from general awareness? *Rubric:* 3 = it focuses on steps specific roles must perform;; 2 = role steps;; 1 = vague;; 0 = none.

### Synthesis

Controls are implemented inside workflows and supported by short role-based training.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Human factors and cyber policy: reliability

### Learning outcomes

You will (1) analyse the reliability of human-dependent controls; (2) compute the effect of independent checks; (3) recognise common-cause failures.

### 32.1 Human reliability

Every control that depends on a person can fail when that person is tired, rushed or distracted. Aiko treats the callback control as a system with a failure probability. If one officer skips the callback in five percent of cases under pressure, a single-officer control fails about one time in twenty. A second independent check reduces this, but only if the checks really are independent. Reliability analysis helps Greyford see where to add checks and where a technical control would be more dependable than any procedure.

### 32.2 Independent checks

The lab computes the probability that a fraudulent payment change passes when each of one, two or three independent checks fails with a given probability. With a 5% failure rate, two independent checks fail together in 0.25% of cases. The lab then adds a common cause, such as month-end pressure affecting both officers at once, and shows that combined failure rises sharply. This shows why Greyford schedules a different team for second checks during month-end and does not rely on the arithmetic of independence alone.

### Lab — Independent and common-cause failure of checks

```python
# Probability a fraudulent payment change passes all checks (synthetic rates).
p = 0.05
for k in (1, 2, 3): print(f"{k} independent check(s): {p ** k:.4%}")
# Common cause: on 10% of days (month-end), each check fails with 0.35 and failures are shared.
q, pc = 0.10, 0.35
both = (1 - q) * p * p + q * pc * pc
print(f"2 checks with month-end common cause: {both:.2%}")
```

Run with `python3 lab_reliability.py`. Verified output:

```text
1 independent check(s): 5.0000%
2 independent check(s): 0.2500%
3 independent check(s): 0.0125%
2 checks with month-end common cause: 1.45%
```

### 32.3 Common-cause failures

Common causes include shared pressure, shared misleading information and shared trust in a familiar name. If the fraudulent email convinces the first officer, the second officer may see the same email and be convinced too. Aiko therefore designs the second check to use different information, the supplier file number rather than the email, and a different team. She notes that independence is a design property that must be built, not assumed, and she writes it into the control description so it survives staff changes.

### Worked example

Aiko models callback reliability, shows independent checks reduce failure, and designs against common causes.

> **Synthetic case.** Probabilities are synthetic.

### Errors and limits

Real failure rates are hard to measure. Independence can erode over time.

### Exercises

- **EX094 — Two checks.** What is the joint failure rate of two independent 5% checks? *Rubric:* 3 = 0.25%;; 2 = 0.0025;; 1 = 10%;; 0 = none.
- **EX095 — Lab common cause.** How did a common cause change joint failure? *Rubric:* 3 = joint failure rose from 0.25% to 1.45%;; 2 = rise;; 1 = vague;; 0 = none.
- **EX096 — Building independence.** How did Aiko build independence into the second check? *Rubric:* 3 = different information and a different team;; 2 = different;; 1 = same email;; 0 = none.

### Synthesis

Human-dependent controls are reliable only when checks are genuinely independent and common causes are designed out.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Human factors and cyber policy: safety and resilience

### Learning outcomes

You will (1) connect security behaviour to safety at a water utility; (2) design resilience for when people are deceived; (3) rehearse recovery without deception.

### 33.1 Safety links

At a water utility, a deceived operator could allow changes to treatment settings that affect public health. Aiko works with the safety manager to link security and safety procedures. Any change to dosing settings already requires a second engineer for safety reasons; she extends that rule to remote requests, so a deceived operator alone cannot change a setting. The safety case now lists social engineering as a possible initiating event, with controls and response actions, so security and safety teams share one view of the hazard.

### 33.2 Designing for deception

Aiko assumes that someone will eventually be deceived, because no programme can prevent all deception. She designs resilience: automatic alerts on unusual settings changes, a clear way to raise concern after the fact without blame, and a quick route to reverse changes. Staff are told that reporting a mistake quickly is the most valuable thing they can do. This shifts the question from whether people can be fooled to how fast the organisation recovers when they are, which is a more achievable goal.

### 33.3 Rehearsing recovery

Greyford rehearses recovery through tabletop exercises, in which staff talk through a scenario such as a vendor impersonation that has led to a session opening. Exercises are announced, run with willing participants and focused on the response, not on catching anyone out. The first exercise reveals that the control room does not know who to call out of hours in the security team. A rota is published the next week. Rehearsing recovery openly builds confidence rather than fear, consistent with the ethical approach of the programme.

### Worked example

Aiko links security to dosing safety rules, designs for recovery after deception and runs announced tabletop exercises.

> **Synthetic case.** Scenarios are synthetic.

### Errors and limits

Tabletop exercises may miss practical problems. Alerts may be ignored.

### Exercises

- **EX097 — Safety rule extension.** Which safety rule was extended to remote requests? *Rubric:* 3 = second engineer for dosing changes;; 2 = two-person;; 1 = vague;; 0 = none.
- **EX098 — Resilience aim.** What question does designing for deception shift to? *Rubric:* 3 = how fast the organisation recovers;; 2 = recovery;; 1 = whether people are fooled;; 0 = none.
- **EX099 — Tabletop finding.** What gap did the first tabletop reveal? *Rubric:* 3 = no out-of-hours security contact known;; 2 = rota;; 1 = vague;; 0 = none.

### Synthesis

Security and safety share hazards, and resilience assumes deception will happen and rehearses recovery openly.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Human factors and cyber policy: integration

### Learning outcomes

You will (1) integrate the programme with incident response; (2) align with governance and risk management; (3) connect metrics to the risk register.

### 34.1 Incident response

Aiko integrates reporting with incident response. When triage confirms a malicious email that reached many inboxes, the triage tool opens an incident ticket automatically, notifies the response lead and removes the email from all mailboxes. Responders can see who reported first and thank them. After incidents, response leads add a short note on human factors, such as whether a control helped or got in the way. This link means that reporting has a visible effect on response and that lessons flow back into design.

### 34.2 Governance alignment

Aiko maps the programme to Greyford's governance. The Govern function of NIST CSF 2.0 expects roles, policies and oversight for cybersecurity, and the programme now has a named owner, a charter, quarterly reporting to the risk committee and an annual review. ISO/IEC 27001:2022 requires awareness and competence for people doing work that affects security, and the programme provides records of both. She avoids treating these frameworks as the goal; they provide structure, while the goal remains fewer harmful outcomes. The charter is reviewed by the risk committee each year.

### 34.3 Risk register links

Aiko links programme measures to entries in the risk register, following the approach of NIST SP 800-30r1, in which likelihood and impact estimates should be updated with evidence. The risk of payment fraud is now informed by the number of held change requests and verified fakes; the risk of OT access abuse by attempted ungated sessions. When measures change, risk owners review the entry. This turns the programme from a separate activity into a source of evidence for risk decisions across the organisation.

### Worked example

Aiko links reporting to automatic incident tickets, maps the programme to CSF 2.0 and ISO/IEC 27001, and feeds measures into the risk register.

> **Synthetic case.** The integration is synthetic; NIST CSF 2.0, ISO/IEC 27001:2022 and SP 800-30r1 are real.

### Errors and limits

Automatic incident creation may cause noise. Framework mapping can become box-ticking.

### Exercises

- **EX100 — Automatic action.** What happens when triage confirms a widely received malicious email? *Rubric:* 3 = an incident ticket opens and the email is removed;; 2 = ticket;; 1 = vague;; 0 = none.
- **EX101 — CSF function.** Which CSF 2.0 function covers roles, policies and oversight? *Rubric:* 3 = Govern;; 2 = govern, without explanation;; 1 = Protect;; 0 = none.
- **EX102 — Risk evidence.** Which measure informs the payment fraud risk? *Rubric:* 3 = held change requests and verified fakes;; 2 = held requests;; 1 = vague;; 0 = none.

### Synthesis

Integration links reporting to response, the programme to governance and measures to risk decisions.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) redesign a component after evaluation evidence; (2) present design rationale to a mixed audience; (3) respond to challenge constructively.

### 35.1 The studio brief

The second studio asks teams to redesign one component of the Greyford programme using evaluation evidence gathered so far. Aiko's team chooses the guidance on what to report, because the help channel log and usability tests showed confusion about invoices and newsletters. The brief requires a redesigned guide, a test with at least six staff and a presentation to a panel that includes a finance officer, an operator and a security manager. Teams have three weeks and must document each change and its reason.

### 35.2 Evidence-led redesign

The team rewrites the guidance as three questions: did you expect this message, does it ask you to act quickly, and does it ask for money, credentials or access. If any answer is worrying, report it. They test the new guide with eight staff using twelve synthetic emails. Correct report decisions rise from nine to eleven out of twelve on average. One tester notes that internal system emails remain hard to judge, so the team adds a short list of genuine system senders that is updated monthly.

### 35.3 Presenting and challenge

The team presents the redesign in ten minutes, starting with the evidence of confusion. The finance officer challenges whether the three questions would catch a payment fraud from a known supplier's compromised account. The team acknowledges that the guide alone would not, and points to the payment hold control as the defence for that case. The panel values the honest answer. Aiko learns that a design rationale is strongest when it shows how parts of the system cover each other's weaknesses.

### Worked example

Aiko's team redesigns reporting guidance as three questions, raises correct decisions from nine to eleven of twelve and answers challenge by pointing to layered controls.

> **Synthetic case.** The studio is synthetic.

### Errors and limits

Small tests may not generalise. Lists of genuine senders need maintenance.

### Exercises

- **EX103 — Three questions.** What are the three questions in the new guide? *Rubric:* 3 = expected, urgent, asks for money credentials or access;; 2 = three;; 1 = vague;; 0 = none.
- **EX104 — Test result.** How did correct decisions change? *Rubric:* 3 = from nine to eleven out of twelve;; 2 = rise;; 1 = vague;; 0 = none.
- **EX105 — Compromised supplier.** What answered the compromised-supplier challenge? *Rubric:* 3 = the payment hold control;; 2 = layered control;; 1 = the guide;; 0 = none.

### Synthesis

Redesign grounded in evidence and honest about limits shows how layered controls cover each other.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Human factors and cyber policy: performance and scale

### Learning outcomes

You will (1) estimate triage capacity as reporting grows; (2) model queue waiting times; (3) plan staffing and automation to keep feedback fast.

### 36.1 Growth in reports

As the reporting service succeeds, report volume grows. Greyford receives about forty reports a day after launch and expects more as staff confidence rises and the programme extends to contractors. Each report needs triage, and the promise of quick feedback depends on triage keeping pace. Aiko estimates that a triage analyst can handle about twelve reports an hour after clustering. She asks what happens to waiting times when daily volume rises, because slow feedback would undermine the effect shown in chapter 17.

### 36.2 Queue modelling

The lab simulates a day of reports arriving at random during working hours and served by one analyst at a fixed rate, and records the average wait before a verdict. At forty reports a day the average wait is about seven minutes. At eighty it doubles to fourteen, and at ninety-five, when the analyst is busy almost all the time, it reaches twenty-five minutes, rising faster with each extra report, as queueing theory predicts when utilisation approaches one. Aiko uses the result to show managers that capacity must grow before volume reaches the steep part of the curve, not after complaints begin.

### Lab — Waiting time for verdicts as report volume grows

```python
# Single analyst triage queue over an 8-hour day (synthetic, seed fixed).
import random
def day(n, rate=12, seed=1):
    r = random.Random(seed); arr = sorted(r.uniform(0, 480) for _ in range(n))
    free = 0.0; waits = []
    for a in arr:
        start = max(a, free); free = start + 60 / rate; waits.append(free - a)
    return sum(waits) / n
for n in (40, 80, 95):
    print(f"{n} reports/day: mean wait to verdict {sum(day(n, seed=s) for s in range(200)) / 200:.0f} min")
```

Run with `python3 lab_queue.py`. Verified output:

```text
40 reports/day: mean wait to verdict 7 min
80 reports/day: mean wait to verdict 14 min
95 reports/day: mean wait to verdict 25 min
```

### 36.3 Staffing and automation

Aiko proposes three measures: automatic clustering so identical reports count as one item, automatic verdicts for messages already confirmed as malicious, and a second analyst at peak times. Automation handles repetitive work, while people handle new or uncertain cases. She sets a service level of a verdict within one working hour for ninety percent of reports and a monthly check of the measure. If the service level slips for two months, staffing is reviewed. This keeps the feedback loop fast as the programme scales.

### Worked example

Aiko models verdict waiting times as reports grow and plans clustering, automatic verdicts and peak staffing to keep feedback within an hour.

> **Synthetic case.** Volumes and rates are synthetic.

### Errors and limits

Real arrivals cluster around campaigns. Automatic verdicts can be wrong.

### Exercises

- **EX106 — Analyst rate.** What triage rate did Aiko assume per analyst? *Rubric:* 3 = about twelve reports an hour;; 2 = twelve;; 1 = forty;; 0 = none.
- **EX107 — Lab queue.** How long were average waits at 40, 80 and 95 reports a day? *Rubric:* 3 = 7, 14 and 25 minutes;; 2 = rise;; 1 = vague;; 0 = none.
- **EX108 — Service level.** What service level did Aiko set? *Rubric:* 3 = verdict within one working hour for 90%;; 2 = one hour;; 1 = vague;; 0 = none.

### Synthesis

Fast feedback at scale needs capacity planned before utilisation approaches its limit.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Human factors and cyber policy: operations

### Learning outcomes

You will (1) define routine operations for the programme; (2) run ethical simulations operationally; (3) handle complaints and exceptions.

### 37.1 Routine operations

Aiko writes an operations calendar. Each week the triage team reviews clusters and sends feedback. Each month a short refresher goes out and a simulation is run at a planned difficulty. Each quarter the burden survey is sent and measures are reported to the risk committee. Each year the programme is reviewed against its charter. Every task has an owner and a backup. Routine operations matter because awareness work fades without steady attention, as the decay analysis in chapter 6 showed. Backups cover leave and illness.

### 37.2 Ethical simulations in operation

Simulations run under rules agreed with staff representatives: announced programme, no lures exploiting personal distress such as pay cuts, bonuses or health scares, no use of individual results for discipline, immediate supportive feedback and aggregate reporting only. Each template is rated with the NIST Phish Scale (Dawkins and Jacobs, 2023) and approved by a small panel including a staff representative. Lain, Kostiainen and Čapkun (2022) found that embedded training pages after clicks did not help, so feedback is short and kind rather than a lesson.

### 37.3 Complaints and exceptions

Some staff complain that simulations feel like being tricked. Aiko answers each complaint personally, explains the rules and records the theme. When several complaints cite one template that mimicked an HR message about leave, the panel withdraws it, accepting that it came too close to personal matters. Exceptions are allowed for staff on sick leave or under stress, who can opt out temporarily through their manager without giving reasons. Handling complaints well keeps the trust on which reporting depends. Themes are reported quarterly.

### Worked example

Aiko defines a weekly to yearly operations calendar, runs simulations under agreed ethical rules and withdraws a template after complaints.

> **Synthetic case.** Operations are synthetic; Dawkins and Jacobs (2023) and Lain et al. (2022) are real.

### Errors and limits

Opt-outs reduce coverage. Panels may approve borderline lures.

### Exercises

- **EX109 — Banned lures.** Which lures are banned? *Rubric:* 3 = those exploiting personal distress such as pay or health;; 2 = distress;; 1 = vague;; 0 = none.
- **EX110 — Embedded training.** Why is post-click feedback short and kind? *Rubric:* 3 = Lain et al. found embedded training pages did not help;; 2 = research;; 1 = vague;; 0 = none.
- **EX111 — Withdrawn template.** Why was one template withdrawn? *Rubric:* 3 = it mimicked an HR leave message too close to personal matters;; 2 = HR;; 1 = vague;; 0 = none.

### Synthesis

Operations need a steady calendar, ethical simulation rules and respectful handling of complaints.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Human factors and cyber policy: validation

### Learning outcomes

You will (1) distinguish validation from verification; (2) validate the programme against its purpose; (3) use mixed evidence to judge success.

### 38.1 Validation versus verification

Verification asks whether the system was built as specified; validation asks whether it achieves its purpose. Greyford's reporting service passed verification in chapter 30, but Aiko must now ask whether it actually reduces harm from deception. A service can meet every requirement and still fail its purpose if, for example, staff report only harmless emails while attacks go unreported. Validation therefore looks at outcomes in real operation, not test conditions, and needs evidence collected over months rather than days. Both are needed, in that order.

### 38.2 Validating outcomes

After nine months, Aiko compares outcomes with the year before launch. The lab computes the change in median time to first report and the share of malicious emails reported. Reporting share rises and median time falls. She also checks payment fraud attempts: three fake bank detail changes were caught by the hold control, against one loss the year before. She notes that the before-and-after comparison cannot rule out changes in attacks, so she presents the findings as consistent with success rather than proof of it.

### Lab — Before and after reporting outcomes

```python
# Before and after reporting outcomes for malicious emails (synthetic).
before = {"reported": 41, "total": 100, "times": [12, 20, 25, 30, 38, 45, 60, 75, 90]}
after = {"reported": 78, "total": 100, "times": [3, 4, 6, 8, 9, 11, 14, 18, 25]}
for name, d in (("before", before), ("after", after)):
    t = sorted(d["times"]); print(f"{name}: reported share {d['reported'] / d['total']:.0%}, median first report {t[len(t) // 2]} min")
```

Run with `python3 lab_validate.py`. Verified output:

```text
before: reported share 41%, median first report 38 min
after: reported share 78%, median first report 9 min
```

### 38.3 Mixed evidence

Aiko adds qualitative evidence: interviews with ten staff, the burden survey and the complaint log. Staff describe the report button as easy and the feedback as reassuring, though some still dislike simulations. Burden scores improve slightly. Together the evidence supports continuing the programme with adjustments. She follows the advice of Beautement, Sasse and Wonham (2008) to look at compliance budget effects, and finds that the payment hold adds work at month-end, prompting a review of finance staffing that month. Interview notes are anonymised before analysis.

### Worked example

Aiko validates the programme with before-after outcomes, caught fraud attempts and interviews, treating results as consistent with success rather than proof.

> **Synthetic case.** Outcomes are synthetic; Beautement et al. (2008) is real.

### Errors and limits

Before-after designs are weak. Attack patterns change year to year.

### Exercises

- **EX112 — Definition.** What does validation ask? *Rubric:* 3 = whether the system achieves its purpose;; 2 = purpose;; 1 = built as specified;; 0 = none.
- **EX113 — Lab outcomes.** What did the lab show for median report time and reporting share? *Rubric:* 3 = 38 to 9 minutes; 41% to 78%;; 2 = improvement;; 1 = vague;; 0 = none.
- **EX114 — Month-end burden.** What compliance budget effect did Aiko find? *Rubric:* 3 = the payment hold adds month-end work;; 2 = finance;; 1 = vague;; 0 = none.

### Synthesis

Validation tests purpose in real operation with mixed evidence and cautious claims.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Human factors and cyber policy: maintainability

### Learning outcomes

You will (1) design the programme to be maintained over years; (2) manage content and template lifecycles; (3) plan handover and documentation.

### 39.1 Lasting design

Programmes often decline when their founder leaves. Aiko designs Greyford's programme to be maintainable: documented procedures, a charter with owners, a content library with review dates and measures produced automatically from the triage tool. She avoids custom software where a supported product feature exists, because custom tools need specialists to maintain. She also budgets a fixed amount of staff time each year for review and update, so that maintenance does not depend on spare time that may never appear in a busy utility.

### 39.2 Content lifecycle

Every guide, refresher and simulation template has an owner, a creation date and a review date. Content older than a year is reviewed against current attack reports, such as the latest Verizon DBIR, and against Greyford's own reported emails. Templates are retired when they no longer reflect real lures or when complaints show they cause harm. The lab counts items due for review each quarter so that the work can be planned. A small, current library is better than a large one full of outdated examples.

### Lab — Content items due for review by quarter

```python
# Content items due for review by quarter (synthetic library of 40 items).
due = {"Q1": 9, "Q2": 11, "Q3": 14, "Q4": 6}
for q, n in due.items(): print(f"{q}: {n} items")
print("busiest:", max(due, key=due.get), "total:", sum(due.values()))
```

Run with `python3 lab_lifecycle.py`. Verified output:

```text
Q1: 9 items
Q2: 11 items
Q3: 14 items
Q4: 6 items
busiest: Q3 total: 40
```

### 39.3 Handover

Aiko writes a handover pack: the charter, the operations calendar, the requirements and verification table, the measures with their definitions and the ethical rules for simulations. A deputy shadows each task for one cycle before taking it on. She records short videos explaining the reasoning behind key decisions, because documents often record what was done but not why. Prof. Kerr notes that the reasons are what allow successors to adapt wisely rather than either freezing or abandoning the design. The pack is reviewed annually.

### Worked example

Aiko designs for maintenance with owners and review dates, plans content review by quarter and writes a handover pack with reasons.

> **Synthetic case.** Content data are synthetic; the Verizon DBIR is real.

### Errors and limits

Review dates are often missed. Handover packs go stale.

### Exercises

- **EX115 — Custom software.** Why avoid custom software? *Rubric:* 3 = it needs specialists to maintain;; 2 = maintenance;; 1 = vague;; 0 = none.
- **EX116 — Lab review load.** Which quarter had the most content due for review? *Rubric:* 3 = Q3 with 14 items;; 2 = Q3;; 1 = vague;; 0 = none.
- **EX117 — Recording reasons.** Why record the reasons for decisions? *Rubric:* 3 = so successors can adapt wisely;; 2 = adapt;; 1 = vague;; 0 = none.

### Synthesis

Maintainable programmes have owners, review dates, planned effort and handovers that explain why.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) re-verify after changes; (2) verify controls under realistic load; (3) report verification results with limits.

### 40.1 Regression verification

After a year of changes, including new guidance, automatic verdicts and the vendor gate, Aiko reruns the verification table from chapter 30 and adds tests for new requirements. Regression verification checks that changes have not broken something that worked before. One regression appears: the automatic verdict feature sends feedback without the link to guidance added after the usability test. The IT team restores the link and the retest passes. Without the table, the regression might have gone unnoticed for months while staff lost useful guidance.

### 40.2 Load verification

Aiko verifies the triage service under realistic load by replaying a synthetic campaign day with three hundred reports in two hours. She measures the time from report to verdict with automatic clustering and verdicts enabled. The lab summarises the result: most reports receive verdicts within minutes because they cluster into a few distinct emails, but a handful of unique reports wait longer for an analyst. The service level of one hour for ninety percent is met, and the slowest report waits under two hours.

### Lab — Verdict times during a synthetic campaign day

```python
# Verdict times for a synthetic campaign day: 300 reports in 2 hours.
import random
r = random.Random(7)
times = []
for i in range(300):
    if i < 270: times.append(r.uniform(1, 12))      # clustered, automatic verdicts
    elif i < 273: times.append(r.uniform(61, 104))  # unique reports waiting for analyst
    else: times.append(r.uniform(15, 58))           # unique reports handled within the hour
times[-1] = 104.0
within = sum(t <= 60 for t in times) / len(times)
print(f"within 60 min: {within:.0%}; slowest {max(times):.0f} min")
```

Run with `python3 lab_load.py`. Verified output:

```text
within 60 min: 99%; slowest 104 min
```

### 40.3 Reporting limits

Aiko reports the results with limits. The replay used synthetic reports and could not include the confusion of a real campaign, such as staff calling the help desk. Load tests ran outside working hours, so they did not compete with other systems. She recommends a live check during the next real campaign. The verification report states clearly what was tested, what was not and what remains uncertain, which allows the risk committee to judge how much confidence to place in the service.

### Worked example

Aiko reruns verification and finds a missing link regression, load-tests triage with a synthetic campaign and reports limits openly.

> **Synthetic case.** Tests are synthetic.

### Errors and limits

Synthetic replays miss real confusion. Live checks are harder to control.

### Exercises

- **EX118 — Regression found.** What regression was found? *Rubric:* 3 = automatic verdicts lacked the guidance link;; 2 = missing link;; 1 = vague;; 0 = none.
- **EX119 — Lab load.** How fast were verdicts during the campaign replay? *Rubric:* 3 = 99% within one hour; slowest 104 minutes;; 2 = met;; 1 = vague;; 0 = none.
- **EX120 — Untested factor.** What did the replay not include? *Rubric:* 3 = the confusion of a real campaign;; 2 = live effects;; 1 = vague;; 0 = none.

### Synthesis

Re-verification catches regressions, load tests check scale, and honest limits guide confidence.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Human factors and cyber policy: system optimization

### Learning outcomes

You will (1) optimise the programme under a fixed budget; (2) compare marginal benefits of investments; (3) avoid optimising one measure at the expense of the whole.

### 41.1 A fixed budget

Greyford's board gives the programme a fixed budget for the next year and asks Aiko how to spend it for the greatest reduction in risk. Options include more simulations, a second triage analyst, security keys for finance and control room staff, better email filtering and more refresher content. Each option has a cost and an estimated effect on expected losses. Optimisation here means choosing a combination that gives the most benefit within the budget, while respecting constraints such as staff burden and the ethical rules for simulations.

### 41.2 Marginal benefit

The lab ranks options by estimated loss reduction per unit of cost and selects them greedily until the budget runs out. Security keys for finance and control room staff give the largest benefit per unit cost, because they remove the risk of credential theft for the most targeted roles. More simulations give the smallest benefit per unit cost, since the programme already runs them monthly. Aiko presents the result as guidance rather than a precise answer, because the effect estimates come from judgement informed by the evaluation evidence.

### Lab — Greedy selection of investments under a budget

```python
# Greedy selection of programme investments by benefit per cost under a budget of 100 units (synthetic).
opts = [("security keys", 40, 120), ("filtering", 30, 60), ("peak analyst", 25, 45), ("refresher content", 15, 18), ("more simulations", 20, 10)]
budget = 100; spent = 0; chosen = []
for name, cost, benefit in sorted(opts, key=lambda o: o[2] / o[1], reverse=True):
    print(f"{name}: benefit/cost {benefit / cost:.2f}")
    if spent + cost <= budget: chosen.append(name); spent += cost
print("chosen:", chosen, "spent:", spent)
```

Run with `python3 lab_budget.py`. Verified output:

```text
security keys: benefit/cost 3.00
filtering: benefit/cost 2.00
peak analyst: benefit/cost 1.80
refresher content: benefit/cost 1.20
more simulations: benefit/cost 0.50
chosen: ['security keys', 'filtering', 'peak analyst'] spent: 95
```

### 41.3 Whole-system view

Aiko warns against optimising a single measure. Spending everything on reducing simulation click rates might produce a good chart but little reduction in real losses. Herley (2009) argued that security advice often costs users more effort than the harm it prevents, and optimisation should count staff effort as a real cost. She therefore includes estimated staff hours in each option. The final plan buys security keys, a second analyst at peak times and filtering improvements, and it keeps simulations at their current monthly level.

### Worked example

Aiko ranks investments by benefit per cost under a fixed budget, includes staff effort as a cost and selects keys, an analyst and filtering.

> **Synthetic case.** Costs and effects are synthetic; Herley (2009) is real.

### Errors and limits

Effect estimates are uncertain. Greedy selection is not always optimal.

### Exercises

- **EX121 — Best value.** Which option had the highest benefit per cost? *Rubric:* 3 = security keys for targeted roles;; 2 = keys;; 1 = simulations;; 0 = none.
- **EX122 — Lab selection.** What did the lab select within the budget? *Rubric:* 3 = keys, filtering and peak analyst for 95 of 100 units;; 2 = three;; 1 = vague;; 0 = none.
- **EX123 — Herley's point.** Which cost did Aiko include following Herley (2009)? *Rubric:* 3 = staff effort;; 2 = effort;; 1 = money only;; 0 = none.

### Synthesis

Optimisation weighs benefit per cost, counts staff effort and serves real losses, not single measures.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Human factors and cyber policy: applied research

### Learning outcomes

You will (1) frame an applied research question from operational data; (2) design an ethical study within the programme; (3) share findings responsibly.

### 42.1 Framing the question

Operating data raise a research question: does adding a short sentence about why an email was dangerous to the verdict message improve later reporting accuracy, compared with a plain verdict? Aiko frames the question precisely, defines reporting accuracy as the share of a person's reports that are genuine threats, and chooses a six-month horizon. She checks published work and finds that feedback content is little studied compared with training content, so the question could add useful knowledge beyond Greyford. Prof. Kerr approves the question.

### 42.2 Ethical design

Aiko designs a study that randomises teams, not individuals, to receive either the plain or the explained verdict, so that colleagues share one version. Both versions are harmless and the change is small. She seeks approval from the university ethics committee and agreement from staff representatives, informs staff that feedback wording is being compared and allows any team to opt out. Data are analysed at team level only. The design follows the same principles as the simulation rules: respect, transparency and no individual consequences.

### 42.3 Sharing findings

After six months, the explained verdict teams show slightly higher reporting accuracy, but the difference is within the range expected by chance given the number of teams. Aiko reports the result honestly as inconclusive and suggests a larger multi-organisation study. She shares findings with staff first, then with the regulator and finally in a short paper with synthetic illustrations rather than raw data. Prof. Kerr reminds her that inconclusive results are worth publishing, because unpublished null results distort the research record.

### Worked example

Aiko frames a feedback wording question, randomises teams with ethics approval and reports an inconclusive result openly.

> **Synthetic case.** The study is synthetic.

### Errors and limits

Few teams give low power. Contamination between teams is possible.

### Exercises

- **EX124 — Unit of randomisation.** What unit was randomised? *Rubric:* 3 = teams;; 2 = team;; 1 = individuals;; 0 = none.
- **EX125 — Accuracy definition.** How was reporting accuracy defined? *Rubric:* 3 = share of a person's reports that are genuine threats;; 2 = genuine share;; 1 = vague;; 0 = none.
- **EX126 — Null result.** Why publish the inconclusive result? *Rubric:* 3 = unpublished nulls distort the research record;; 2 = record;; 1 = vague;; 0 = none.

### Synthesis

Applied research turns operational questions into ethical studies and reports results honestly, including nulls.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a public-service organisation's constraints; (2) engage with regulators and the public; (3) reflect on professional practice.

### 43.1 Public-service constraints

Greyford is a public-service utility with a duty to provide safe water and report incidents to regulators. Aiko learns that decisions take longer than in private firms because spending needs board approval and procurement rules. Staff include long-serving operators who distrust new initiatives. She adapts by planning changes around budget cycles, involving operators early and explaining links to public safety. Working within these constraints is part of professional practice and not an obstacle to be resented or bypassed through informal shortcuts.

### 43.2 Regulators and the public

The regulator asks how Greyford manages the human side of cyber risk. Aiko prepares a short evidence summary: the charter, measures, verification and validation results and the ethical rules for simulations. The regulator appreciates the honesty about limits. Greyford also publishes a brief statement for customers explaining that it will never ask for bank details by email, supporting customers against impersonation scams. Engagement beyond the organisation recognises that attackers target customers and suppliers as well as staff. The statement is printed on bills as well.

### 43.3 Reflective practice

Aiko keeps a reflective log during the placement, recording decisions, surprises and what she would do differently. She notes that her early designs underestimated the time operators need to trust a new process, and that informal conversations in the control room taught her more than surveys. The ENISA cybersecurity culture guidelines emphasise understanding the existing culture before changing it, and her log shows how much of that understanding came from listening rather than measuring. The log becomes part of her professional portfolio.

### Worked example

Aiko adapts to public-service constraints, prepares evidence for the regulator, supports customers against scams and keeps a reflective log.

> **Synthetic case.** The placement is synthetic; the ENISA guidelines are real.

### Errors and limits

Reflective logs can become self-justifying. Public statements need updating.

### Exercises

- **EX127 — Constraint adaptation.** How did Aiko adapt to slow decisions? *Rubric:* 3 = planning around budget cycles and involving operators early;; 2 = planning;; 1 = bypassing rules;; 0 = none.
- **EX128 — Customer statement.** What did the customer statement promise? *Rubric:* 3 = Greyford will never ask for bank details by email;; 2 = never;; 1 = vague;; 0 = none.
- **EX129 — Biggest lesson.** What did her log show about learning culture? *Rubric:* 3 = most understanding came from listening;; 2 = listening;; 1 = surveys;; 0 = none.

### Synthesis

Professional practice respects public-service constraints, engages regulators and customers, and reflects honestly.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define a capstone design problem; (2) gather requirements and constraints; (3) plan the design and evaluation.

### 44.1 The capstone problem

Aiko's capstone tackles a gap found during the placement: contractors and temporary staff, about a fifth of the workforce, are outside most of the programme. They lack the report button on personal devices, receive no refreshers and are often the target of fake supplier messages. The capstone asks how to extend reporting, controls and feedback to contractors fairly and in proportion to their access. She defines success as contractors reporting at a rate similar to employees within six months, without adding significant burden.

### 44.2 Requirements and constraints

Aiko interviews eight contractors and four managers. Contractors want a simple way to report from any device and do not want to be monitored more than employees. Managers want contractors to follow the same verification rules for payments and access. Constraints include contracts that limit training time and devices Greyford does not control. She writes requirements, including a web form and forwarding address for reports, a ten-minute induction module and identical verification rules, and checks each against the constraints with the procurement team.

### 44.3 Design and evaluation plan

Aiko plans the design in two parts: a reporting route independent of device and an induction covering the three questions from chapter 35 and the verification steps. Evaluation will compare contractor reporting rates with employee rates monthly, using a significance test suited to small groups, and survey burden after three months. She writes a timeline with milestones for design, review, pilot and evaluation. Prof. Kerr asks her to define in advance what result would lead her to abandon the design, which she adds to the plan.

### Worked example

Aiko defines a contractor reporting capstone, gathers needs from contractors and managers and plans design and evaluation with a stopping rule.

> **Synthetic case.** The capstone is synthetic.

### Errors and limits

Contractor turnover complicates evaluation. Small groups give wide uncertainty.

### Exercises

- **EX130 — Gap addressed.** Which group did the capstone address? *Rubric:* 3 = contractors and temporary staff;; 2 = contractors;; 1 = vague;; 0 = none.
- **EX131 — Contractor concern.** What did contractors not want? *Rubric:* 3 = more monitoring than employees;; 2 = monitoring;; 1 = vague;; 0 = none.
- **EX132 — Stopping rule.** What did Prof. Kerr ask Aiko to define in advance? *Rubric:* 3 = the result that would lead her to abandon the design;; 2 = abandon;; 1 = vague;; 0 = none.

### Synthesis

A capstone starts from a real gap, gathers needs from those affected and plans evaluation with clear criteria.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) respond to reviewer findings; (3) record decisions and residual risks.

### 45.1 Preparing for review

Aiko submits the contractor design to an independent review panel: a security architect from another utility, a human factors researcher and a contractor representative. She provides the requirements, design, evaluation plan and known risks. Independent review brings perspectives that the designer cannot provide, because designers tend to see what they intended rather than what they built. She asks reviewers to focus on usability, fairness and whether the controls would stop the attacks identified in chapter 24. Reviewers receive the pack two weeks before the meeting.

### 45.2 Reviewer findings

The panel raises six findings. The architect notes that the forwarding address could be spoofed to send fake verdicts; the design is changed so verdicts arrive only through the web form account. The researcher notes that the induction module tests recall but not decisions, and suggests scenario questions. The contractor representative notes that agencies may not pass on materials, so the induction should be sent directly. The lab tallies the findings by severity and the actions taken, showing which remain open after the response.

### Lab — Tally of review findings by severity and status

```python
# Review findings tally (synthetic).
f = [("high", "closed"), ("high", "closed"), ("medium", "closed"), ("medium", "open"), ("low", "closed"), ("low", "closed")]
for s in ("high", "medium", "low"):
    print(s, "closed", sum(1 for a, b in f if a == s and b == "closed"), "open", sum(1 for a, b in f if a == s and b == "open"))
print("total closed", sum(b == "closed" for _, b in f), "open", sum(b == "open" for _, b in f))
```

Run with `python3 lab_review.py`. Verified output:

```text
high closed 2 open 0
medium closed 1 open 1
low closed 2 open 0
total closed 5 open 1
```

### 45.3 Recording residual risk

Aiko records each finding, decision and remaining risk in a review log. One medium finding remains open: contractors using personal devices may not receive verdicts quickly. She accepts this as a residual risk with a review after the pilot, and the risk owner signs the acceptance. Recording residual risks openly, in line with the risk management approach of NIST SP 800-30r1, ensures that decisions to accept risk are made by the right people and can be revisited later. The log is shared with the panel.

### Worked example

Aiko submits her design to independent reviewers, addresses spoofing, induction and distribution findings, and records one accepted residual risk.

> **Synthetic case.** The review is synthetic; NIST SP 800-30r1 is real.

### Errors and limits

Reviewers may miss issues. Accepted risks may be forgotten.

### Exercises

- **EX133 — Spoofing finding.** What did the architect find? *Rubric:* 3 = the forwarding address could be spoofed to send fake verdicts;; 2 = spoofing;; 1 = vague;; 0 = none.
- **EX134 — Lab tally.** How many findings stayed open after the response? *Rubric:* 3 = 5 closed, 1 medium open;; 2 = one open;; 1 = vague;; 0 = none.
- **EX135 — Residual acceptance.** Who signed the residual risk acceptance? *Rubric:* 3 = the risk owner;; 2 = owner;; 1 = the designer;; 0 = none.

### Synthesis

Independent review finds what designers miss, and residual risks are recorded and owned.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) pilot the capstone design; (2) analyse small-group results with an exact test; (3) decide whether to scale up.

### 46.1 Running the pilot

Aiko pilots the contractor design with sixty contractors over three months. They receive the induction directly from Greyford, can report through the web form or forwarding address and follow the same payment and access verification rules as employees. She tracks reports of real malicious emails, verdict times and burden scores. Two contractors leave and three join during the pilot, which she records. The pilot includes one month of announced simulations under the existing ethical rules, with contractor representatives on the approval panel for templates.

### 46.2 Analysing results

During the simulation month, contractors reported 21 of 60 simulated emails and employees in comparable roles reported 26 of 60. The lab computes Fisher's exact test, suitable for small groups, and finds no clear evidence of a difference. Aiko reports both rates with the test result and notes that the pilot was too small to detect modest differences. Contractors' burden scores are similar to employees', and the median verdict time for their reports is within the one-hour service level, meeting the main success criteria set in advance.

### Lab — Exact test comparing contractor and employee reporting

```python
# Fisher's exact test (two-sided) for contractor vs employee reporting in simulations (synthetic).
from math import comb
a, n1, b, n2 = 21, 60, 26, 60
K, N = a + b, n1 + n2
def p(x): return comb(n1, x) * comb(n2, K - x) / comb(N, K)
p0 = p(a)
pv = sum(p(x) for x in range(max(0, K - n2), min(K, n1) + 1) if p(x) <= p0 * (1 + 1e-9))
print(f"contractors {a}/{n1} = {a / n1:.0%}, employees {b}/{n2} = {b / n2:.0%}, two-sided p = {pv:.2f}")
```

Run with `python3 lab_fisher.py`. Verified output:

```text
contractors 21/60 = 35%, employees 26/60 = 43%, two-sided p = 0.45
```

### 46.3 Scaling decision

The stopping rule defined in chapter 44 would have triggered if contractor reporting fell below half the employee rate; it did not. Aiko recommends scaling to all contractors, with the residual risk about personal devices reviewed after another three months. The board approves. She notes that the decision rests on meeting predefined criteria rather than on a significant result, which is appropriate because the aim was parity, not superiority. Planning the decision rule in advance prevented her from interpreting the results to suit her hopes.

### Worked example

Aiko pilots contractor reporting with sixty contractors, finds no clear difference from employees with Fisher's exact test and scales up under predefined criteria.

> **Synthetic case.** Pilot data are synthetic.

### Errors and limits

Small pilots cannot show equivalence precisely. Contractor turnover affects results.

### Exercises

- **EX136 — Pilot rates.** What were the simulation reporting rates? *Rubric:* 3 = contractors 21/60 and employees 26/60;; 2 = 35% vs 43%;; 1 = vague;; 0 = none.
- **EX137 — Lab test.** What p-value did Fisher's exact test give? *Rubric:* 3 = about 0.45;; 2 = not significant;; 1 = 0.05;; 0 = none.
- **EX138 — Decision basis.** What was the scaling decision based on? *Rubric:* 3 = predefined criteria including the stopping rule;; 2 = criteria;; 1 = significance;; 0 = none.

### Synthesis

Pilots judged against predefined criteria support honest decisions even when samples are small.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) plan a failure trial for the reporting and verification system; (2) run it safely; (3) learn from what failed.

### 47.1 Planning the trial

Aiko plans a trial to test how the programme behaves when parts fail. Scenarios include the triage tool going offline during a campaign, the second finance officer being absent at month-end and the security team being unreachable at night. The trial is announced to all participants, scheduled at a quiet time and approved by operations and safety managers. No staff are deceived; the trial tests systems and procedures, not individuals. Each scenario has a defined start, observer and stop condition to ensure safety.

### 47.2 Running the trial

In the first scenario, the triage tool is taken offline for an hour. Reports queue in the mailbox as designed, but staff receive no thank-you messages and some report twice. In the second, the finance hold escalates correctly to a backup officer. In the third, the control room reaches the out-of-hours security contact within ten minutes using the rota. The lab summarises the recovery time for each scenario against its target, showing that only the triage outage exceeded its target. Observers time each step.

### Lab — Recovery times against targets for three failure scenarios

```python
# Recovery times against targets (minutes, synthetic).
s = [("triage outage", 60, 30), ("finance backup", 15, 60), ("out-of-hours contact", 10, 15)]
for name, t, target in s: print(f"{name}: {t} min vs target {target} -> {'MISSED' if t > target else 'met'}")
```

Run with `python3 lab_recovery.py`. Verified output:

```text
triage outage: 60 min vs target 30 -> MISSED
finance backup: 15 min vs target 60 -> met
out-of-hours contact: 10 min vs target 15 -> met
```

### 47.3 Learning from failure

Aiko holds a blameless review. The triage outage revealed that the fallback had no automatic acknowledgement, so staff were uncertain whether reports had arrived. The team adds a simple automatic reply from the mailbox itself, independent of the triage tool. Aiko notes that failures found in planned trials are much cheaper than those found during real attacks. She updates the verification table with a new requirement for acknowledgement during outages, closing the loop between trial and design. The reply is tested monthly.

### Worked example

Aiko runs an announced failure trial of triage, finance and out-of-hours scenarios, finds a missing acknowledgement during outages and adds a requirement.

> **Synthetic case.** The trial is synthetic.

### Errors and limits

Planned trials are less stressful than real failures. Quiet-time trials miss peak effects.

### Exercises

- **EX139 — Trial ethics.** What does the trial test? *Rubric:* 3 = systems and procedures, not individuals;; 2 = systems;; 1 = staff vigilance;; 0 = none.
- **EX140 — Lab recovery.** Which scenario exceeded its target in the lab? *Rubric:* 3 = triage outage, 60 minutes against 30;; 2 = triage;; 1 = vague;; 0 = none.
- **EX141 — Fix added.** What fix followed the triage outage? *Rubric:* 3 = an automatic reply from the mailbox itself;; 2 = acknowledgement;; 1 = vague;; 0 = none.

### Synthesis

Announced failure trials find weaknesses cheaply and feed new requirements back into design.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble an evidence dossier for the programme; (2) link claims to evidence; (3) state limitations and open questions.

### 48.1 Assembling the dossier

Aiko assembles an evidence dossier for her engineering assessment and for Greyford's regulator. It contains the requirements, design rationale, verification tables, validation results, pilot analysis, failure trial report, review log and ethical rules. Each document is versioned and dated. The dossier is organised around claims, such as the claim that the programme shortens exposure to malicious emails, with the evidence for each claim listed beneath it. This structure helps readers see what is claimed and how strongly it is supported. An index lists every item.

### 48.2 Claims and evidence

For each claim, Aiko states the evidence and its strength. The exposure claim rests on the before and after comparison and the queue analysis, which she rates as moderate because the design cannot rule out changes in attacks. The payment fraud claim rests on caught attempts and the reliability analysis. The fairness claim for contractors rests on the pilot and interviews. The lab counts claims by evidence strength. She avoids claiming that the programme changed culture, because her evidence does not measure culture directly.

### Lab — Claims by evidence strength

```python
# Claims by evidence strength (synthetic).
claims = {"shorter exposure": "moderate", "payment fraud caught": "strong", "contractor fairness": "moderate", "low staff burden": "moderate", "lasting effect": "weak"}
for s in ("strong", "moderate", "weak"): print(s, sum(v == s for v in claims.values()))
```

Run with `python3 lab_dossier.py`. Verified output:

```text
strong 1
moderate 3
weak 1
```

### 48.3 Limits and open questions

The dossier ends with limitations and open questions: whether the effects last beyond two years, whether results would hold in a larger utility and whether feedback wording matters, given the inconclusive study. She lists data that would answer each question. The panel praises the dossier for its honesty. Prof. Kerr reminds her that a dossier is a living record and should be updated as the programme continues, so that later decisions rest on current evidence rather than the snapshot taken for the assessment.

### Worked example

Aiko builds a claim-based dossier, rates evidence strength and lists open questions.

> **Synthetic case.** The dossier is synthetic.

### Errors and limits

Strength ratings are judgements. Dossiers become outdated.

### Exercises

- **EX142 — Organisation.** How is the dossier organised? *Rubric:* 3 = around claims with evidence beneath each;; 2 = claims;; 1 = by date;; 0 = none.
- **EX143 — Lab strengths.** What did the lab count? *Rubric:* 3 = 1 strong, 3 moderate, 1 weak claim;; 2 = counts;; 1 = vague;; 0 = none.
- **EX144 — Avoided claim.** Which claim did Aiko avoid? *Rubric:* 3 = that the programme changed culture;; 2 = culture;; 1 = vague;; 0 = none.

### Synthesis

An evidence dossier links each claim to graded evidence and names its limits.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) structure an engineering thesis on a human factors programme; (2) present design, verification and validation coherently; (3) write with appropriate citation and caution.

### 49.1 Thesis structure

Aiko's thesis is titled Designing a reporting-centred security programme for a water utility. Its chapters cover the problem and context, the literature, requirements, design alternatives and choice, implementation, verification, validation, the contractor capstone and conclusions. Each chapter ends with a short summary linking to the next. The structure follows the engineering life cycle, which helps examiners trace each design decision from requirement to evidence. Appendices hold the verification tables, lab code and ethical approvals, with synthetic examples replacing sensitive data. It runs to ninety pages.

### 49.2 Coherent argument

The thesis argues that a programme centred on reporting, fast feedback and supporting controls reduces exposure more effectively than a compliance-led programme, while respecting staff. Aiko supports this with her validation and pilot results, and with literature such as Adams and Sasse (1999), Sasse, Brostoff and Weirich (2001) and Bada, Sasse and Nurse (2019). She is careful to separate what her data show from what the literature suggests, and she presents her before and after results as consistent with, rather than proof of, the argument.

### 49.3 Citation and caution

Aiko checks every citation against the original source and records DOIs only where she has confirmed them. She uses cautious language: results suggest rather than prove, and effects are described with their uncertainty. She acknowledges that her case is one utility and that other organisations may differ. Prof. Kerr reads a full draft and asks for one change: to move the ethical rules for simulations from an appendix into the main text, because they are central to the design rather than an administrative detail.

### Worked example

Aiko structures her thesis along the engineering life cycle, separates her evidence from literature and states results cautiously.

> **Synthetic case.** The thesis is synthetic; the cited works are real.

### Errors and limits

One case limits generalisation. Literature may not fit the utility context.

### Exercises

- **EX145 — Structure basis.** What does the thesis structure follow? *Rubric:* 3 = the engineering life cycle;; 2 = life cycle;; 1 = vague;; 0 = none.
- **EX146 — Separation.** What does Aiko keep separate? *Rubric:* 3 = what her data show and what the literature suggests;; 2 = separation;; 1 = vague;; 0 = none.
- **EX147 — Requested change.** What change did Prof. Kerr request? *Rubric:* 3 = move the ethical simulation rules into the main text;; 2 = ethics;; 1 = vague;; 0 = none.

### Synthesis

A good engineering thesis traces decisions to evidence and states results with care.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) prepare for a final engineering defense; (2) answer questions on design and ethics; (3) reflect on the contribution and next steps.

### 50.1 Preparing

Aiko prepares a twenty-minute presentation covering the problem, design choice, verification, validation, the contractor capstone and limits. She rehearses with fellow students who ask hard questions about cost, ethics and evidence. She prepares backup slides on the reliability analysis, the queue model and the failure trial. She also prepares a one-page summary of the ethical rules for simulations, expecting questions on that topic. Preparation focuses on explaining reasoning clearly, since examiners assess understanding rather than the polish of slides. She also times each rehearsal.

### 50.2 Questions

An examiner asks whether simulations should be used at all given the risk to trust. Aiko answers that Greyford uses them sparingly, under announced and agreed rules, with no personal distress lures and no individual consequences, and that they provide calibration rather than the main measure. Another examiner asks how the design would fail; she cites the triage outage and the common-cause risk at month-end. A third asks about cost; she presents the budget analysis with staff hours included. The examiners note her consistent focus on evidence.

### 50.3 Contribution and next steps

Aiko summarises her contribution: a tested design for reporting-centred security in a utility, methods for verifying and validating it, and a fair extension to contractors. She lists next steps: a multi-site study of feedback wording, a two-year follow-up and sharing the design with other utilities through the sector forum. The examiners award the degree with commendation. Prof. Kerr reflects that the project shows how engineering discipline and respect for people can work together in security, which was the aim of the course.

### Worked example

Aiko defends her thesis, answers questions on simulation ethics, failure and cost, and summarises her contribution and next steps.

> **Synthetic case.** The defense is synthetic.

### Errors and limits

Defenses test communication as well as substance. Next steps need funding.

### Exercises

- **EX148 — Simulation role.** How does Aiko describe the role of simulations? *Rubric:* 3 = sparing calibration under agreed rules, not the main measure;; 2 = calibration;; 1 = main measure;; 0 = none.
- **EX149 — Failure examples.** Which failure modes did Aiko cite? *Rubric:* 3 = triage outage and month-end common cause;; 2 = two;; 1 = vague;; 0 = none.
- **EX150 — Next step.** Name one next step Aiko listed. *Rubric:* 3 = multi-site study of feedback wording;; 2 = study;; 1 = vague;; 0 = none.

### Synthesis

A final defense demonstrates reasoning, ethical consistency and an honest account of contribution.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Aiko Tanabe, Prof. Joanna Kerr, Rivenhall Technical University, Greyford Water and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Whether reporting is still rising, levelling off or falling back after a campaign.

**EX002.** Because it would predict reports growing without limit instead of levelling off.

**EX003.** As the area under the curve of unreported inboxes over time, which faster reporting shrinks.

**EX004.** The rule to lock screens when leaving and the rule to keep consoles signed in during incidents.

**EX005.** Eleven staff who have remote access but no remote access training.

**EX006.** Roughly once a week across their seven systems.

**EX007.** Because they follow from environmental conditions like glare, noise and long shifts.

**EX008.** They learn to acknowledge alarms without reading them, so important ones are lost.

**EX009.** With a faster closer and a separate entrance for deliveries.

**EX010.** Because a program can run without errors and still produce wrong answers.

**EX011.** Week 3, with 41 reports.

**EX012.** Work on counts, and if individual records are needed, replace names with codes and keep the key separately.

**EX013.** What to do if they have already clicked a link.

**EX014.** As an expected result of good lures, with the focus on how quickly staff report.

**EX015.** Using the same numbers and including limitations in every version.

**EX016.** About 2.9 months for the extra benefit to halve.

**EX017.** Quarterly refreshers, averaging 0.72 against 0.55 for a single annual course.

**EX018.** The staff minutes each schedule consumes.

**EX019.** 15.0%, with a 95% Wilson interval of 8.1% to 26.1%.

**EX020.** Because small teams vary by chance, so rankings shame people for random results.

**EX021.** Twenty people, merging smaller teams.

**EX022.** Through fewer passwords and simpler steps, without seeing the chips.

**EX023.** It gives similar protection while removing the temptation to write a long password on the laptop.

**EX024.** Spare keys at depots with a clear, quick recovery process.

**EX025.** Because many reports of the same email need only one investigation.

**EX026.** Six distinct emails; the most reported was first reported nine minutes after arrival.

**EX027.** Only the sender, a subject fingerprint and report times, not bodies or reporter names.

**EX028.** Only with a clear safety purpose, organisational approval, avoidance of harm and honest explanation afterwards.

**EX029.** Lures exploiting fear about pay, health, family or redundancy.

**EX030.** Because distracting an operator could affect safety-critical water treatment.

**EX031.** Because no person has to recognise and judge those messages.

**EX032.** Because it appears on almost every supplier email, so it carries little information.

**EX033.** Eight of the ten staff.

**EX034.** Because the habit of clicking through carries over when a rare dangerous prompt appears.

**EX035.** By fixing the internal certificates so the warnings no longer appear.

**EX036.** A self-service catalogue, requests answered within an hour and temporary task rights.

**EX037.** A table linking individual staff to simulation clicks.

**EX038.** Only completion dates, without quiz scores.

**EX039.** That awareness data will not be used for discipline.

**EX040.** Reading on phones, often with gloves or in bright light.

**EX041.** On mobile, the report button scrolled off screen.

**EX042.** Because reporting is the feature's main purpose.

**EX043.** Because it moves design towards supporting good behaviour rather than only restricting it.

**EX044.** Authority and urgency.

**EX045.** Callback verification using a known number for vendor requests.

**EX046.** Their limits and strengths become part of the design instead of an afterthought.

**EX047.** Filtering known bad emails, checking domains and grouping duplicate reports.

**EX048.** Requiring a password entry while acknowledging a critical alarm.

**EX049.** The loop is open and staff may stop reporting.

**EX050.** An automatic thank-you, a confirmation of whether the email was malicious, and a monthly summary.

**EX051.** With feedback the rate rose to 60% by month 12, while without it drifted down to 18%.

**EX052.** Every staff member would need to be perfect all the time.

**EX053.** As one layer among many, not the last line of defence.

**EX054.** They refuse to authenticate to the wrong site, so fake login pages fail.

**EX055.** By sending repeated prompts until a tired user accepts one.

**EX056.** Because the key checks the site's identity and will not sign for the wrong site.

**EX057.** Because they would bring phishing risk back into the system.

**EX058.** Usability of security tools, awareness and training, and organisational culture, among others.

**EX059.** As a set of design constraints and goals for engineering.

**EX060.** When it serves one stakeholder, usually management, and ignores the rest.

**EX061.** Fear of looking foolish by reporting an email that turns out to be genuine.

**EX062.** Because it cannot be verified and so cannot guide design.

**EX063.** One-tap mobile reporting and thank-you messages within a minute.

**EX064.** Faster reporting and fewer successful attacks, not training completion.

**EX065.** The tool's default export of individual results to a spreadsheet managers could open.

**EX066.** Points with little information and high pressure, such as urgent phone requests.

**EX067.** Online research, an impersonating email, a follow-up call and a request to approve a remote session.

**EX068.** Reminders or automation, such as automatic screen locking.

**EX069.** That rules are unworkable, rather than that staff have bad intent.

**EX070.** Whether users know what to do, can see how, understand the feedback and know they succeeded.

**EX071.** Not knowing whether something is suspicious enough to report, given by 71 of 180 respondents.

**EX072.** That any doubt is a good reason to report.

**EX073.** Framing reports as helping colleagues rather than as a security duty.

**EX074.** That drivers cannot use phones while driving, so other reporting routes are needed.

**EX075.** Reporting from depot terminals and a phone hotline, plus a shorter summary.

**EX076.** On regulatory evidence, because the regulator expects some training records.

**EX077.** Compliance-led 2.75, reporting-led 3.85 and design-led 3.90.

**EX078.** By checking that it still held when the weight on regulatory evidence was doubled.

**EX079.** From the supplier file, never from the request itself.

**EX080.** They must be transparent, easy to override and never manipulative.

**EX081.** Through role-play with a colleague acting as the caller, not a deception exercise.

**EX082.** The testable requirements written in chapter 21.

**EX083.** Fear-based messages, which often cause campaigns to fail.

**EX084.** Whether newsletters and supplier invoices should be reported.

**EX085.** Because it relates directly to how long malicious emails remain active.

**EX086.** Two never-reported emails caused most exposure, 93% of inbox-minutes.

**EX087.** So one measure cannot be gamed without the paired measure revealing it.

**EX088.** That it showed only groups of twenty or more and offered no individual export.

**EX089.** Guidance on what to report was linked only from the intranet, so a link was added to the thank-you message.

**EX090.** Five of six requirements passed at first, and all six after the notification setting was changed.

**EX091.** The person who received the change request cannot release the hold.

**EX092.** A valid ticket number from the maintenance system approved by an engineer.

**EX093.** It focuses only on the procedures that particular roles must carry out.

**EX094.** 0.25%, because 0.05 multiplied by 0.05 is 0.0025.

**EX095.** Joint failure rose from 0.25% to about 1.45% when month-end pressure affected both checks.

**EX096.** By using the supplier file number and a different team rather than the original email.

**EX097.** The rule that dosing changes need a second engineer.

**EX098.** How quickly the organisation recovers when someone is deceived.

**EX099.** The control room did not know who to call out of hours, so a rota was published.

**EX100.** An incident ticket opens, the lead is notified and the email is removed from all mailboxes.

**EX101.** The Govern function.

**EX102.** The number of held bank detail changes and verified fake requests.

**EX103.** Did you expect it, does it push for speed, and does it ask for money, credentials or access?

**EX104.** They rose from nine to eleven out of twelve on average.

**EX105.** The payment hold control, since the guide alone would not catch it.

**EX106.** About twelve reports an hour after clustering.

**EX107.** About 7 minutes at forty, 14 at eighty and 25 at ninety-five reports a day.

**EX108.** A verdict within one working hour for ninety percent of reports.

**EX109.** Lures exploiting personal distress, such as pay cuts, bonuses or health scares.

**EX110.** Because Lain, Kostiainen and Čapkun found embedded training pages did not help.

**EX111.** Because it mimicked an HR message about leave, too close to personal matters.

**EX112.** Whether the system achieves its purpose in real operation.

**EX113.** Median time fell from 38 to 9 minutes and reporting share rose from 41% to 78%.

**EX114.** The payment hold adds work for finance at month-end.

**EX115.** Because custom tools need specialists to maintain, unlike supported product features.

**EX116.** The third quarter, with 14 items due for review.

**EX117.** So successors can adapt the design wisely instead of freezing or abandoning it.

**EX118.** Automatic verdict messages had lost the link to guidance.

**EX119.** 99% of reports received verdicts within an hour and the slowest waited 104 minutes.

**EX120.** The confusion of a real campaign, such as help desk calls.

**EX121.** Security keys for finance and control room staff.

**EX122.** Security keys, filtering and a peak-time analyst, costing 95 of 100 budget units.

**EX123.** Staff hours, since user effort is a real cost of security advice.

**EX124.** Teams, so colleagues share one version.

**EX125.** The share of a person's reports that were genuine threats.

**EX126.** Because leaving null results unpublished distorts the research record.

**EX127.** By planning around budget cycles, involving operators early and linking to safety.

**EX128.** That Greyford will never ask customers for bank details by email.

**EX129.** That most understanding came from listening in the control room rather than measuring.

**EX130.** Contractors and temporary staff, about a fifth of the workforce.

**EX131.** To be monitored more than employees are.

**EX132.** The result that would lead her to abandon the design.

**EX133.** That the forwarding address could be spoofed to send fake verdicts.

**EX134.** Five findings closed and one medium finding remained open.

**EX135.** The risk owner.

**EX136.** Contractors 21 of 60 (35%) and employees 26 of 60 (43%).

**EX137.** About 0.45, so no clear evidence of a difference.

**EX138.** On criteria defined in advance, including the stopping rule, rather than a significant result.

**EX139.** Systems and procedures, with no staff deceived.

**EX140.** The triage outage, at 60 minutes against a 30-minute target.

**EX141.** An automatic acknowledgement from the reporting mailbox, independent of the triage tool.

**EX142.** Around claims, with the supporting evidence listed under each.

**EX143.** One strong, three moderate and one weak claim.

**EX144.** That the programme changed culture, because culture was not measured directly.

**EX145.** The engineering life cycle, from requirement to evidence.

**EX146.** What her own data show and what the literature suggests.

**EX147.** Moving the ethical rules for simulations from an appendix into the main text.

**EX148.** As sparing calibration under announced, agreed rules rather than the main measure.

**EX149.** The triage outage and the common-cause risk at month-end.

**EX150.** A multi-site study of feedback wording, a two-year follow-up or sharing through the sector forum.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Beautement, A., Sasse, M. A., & Wonham, M. (2008). The compliance budget: Managing security behaviour in organisations. *Proceedings of the 2008 New Security Paradigms Workshop*, 47–58. <https://doi.org/10.1145/1595676.1595684>
- Cialdini, R. B. (2021). *Influence, new and expanded: The psychology of persuasion*. Harper Business.
- Dawkins, S., & Jacobs, J. (2023). *NIST Phish Scale user guide* (NIST TN 2276). NIST. <https://doi.org/10.6028/NIST.TN.2276>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hadnagy, C. (2018). *Social engineering: The science of human hacking* (2nd ed.). Wiley.
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Reason, J. (1990). *Human error*. Cambridge University Press. <https://doi.org/10.1017/CBO9781139062367>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
- Verizon Business. (2024). *2024 Data breach investigations report*. Verizon. <https://www.verizon.com/business/resources/reports/dbir/>
- Whitten, A., & Tygar, J. D. (1999). Why Johnny can't encrypt: A usability evaluation of PGP 5.0. *Proceedings of the 8th USENIX Security Symposium*. USENIX. <https://www.usenix.org/conference/8th-usenix-security-symposium/why-johnny-cant-encrypt-usability-evaluation-pgp-50>
- Wilson, M., de Zafra, D. E., Pitcher, S. I., Tressler, J. D., & Ippolito, J. B. (1998). *Information technology security training requirements: A role- and performance-based model* (NIST SP 800-16). NIST. <https://doi.org/10.6028/NIST.SP.800-16>
