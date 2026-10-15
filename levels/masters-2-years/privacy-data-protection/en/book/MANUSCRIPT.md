# Privacy and Data Protection: Master's Course

- Language: English (`en`); course 165, Master's course (2 years).
- Editorial state: **published**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students evaluating whether an operational change improves compliance with data subject rights.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs summarise synthetic access-request times, estimate sample sizes and compute a bootstrap difference with stratification; no real requests or customers are involved. Legal analysis is teaching, not legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one master's student studying whether a self-service portal improves on-time answers to access requests: the question and literature, an advanced seminar, design and ethics, rival explanations, proposal and pilot, data and analysis, writing and limitations, and the defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Hana Kobayashi** | Master's student | Invented |
| **Dr. Owen Pritchard** | Supervisor | Invented |
| **Ellery Institute of Technology** | Fictional university | Invented |
| **Brookfield Online Retail** | Fictional retailer serving EU and Brazilian customers | Invented |

### Core sources

Regulation (EU) 2016/679 (GDPR) Articles 12 and 15; Lei 13.709/2018 (LGPD) Article 19; EDPB Guidelines 01/2022 on the right of access; Solove (2006), [doi:10.2307/40041279](https://doi.org/10.2307/40041279); Acquisti et al. (2015), [doi:10.1126/science.aaa1465](https://doi.org/10.1126/science.aaa1465); Shadish, Cook and Campbell (2002); Efron and Tibshirani (1994). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn a compliance problem into a researchable question; (2) run a structured literature search; (3) describe the baseline performance of a data subject rights process.

### 1.1 From complaint to question

Hana Kobayashi is a master's student at the fictional Ellery Institute of Technology, supervised by Dr. Owen Pritchard. Her placement is with the fictional Brookfield Online Retail, which sells household goods to customers across the European Union and Brazil. Customers have complained that requests to see their personal data take too long. Article 15 of the GDPR gives people a right of access, and Article 12(3) requires a response without undue delay and in any event within one month, extendable by two further months for complex or numerous requests. Hana's question is whether a self-service access portal raises the share of requests answered on time.

### 1.2 Why a measurable outcome

Hana chooses on-time completion as her main outcome because it is defined by law, already recorded in Brookfield's ticket system and meaningful to customers. She also records days to completion, because a portal could move requests from day twenty-nine to day twenty-five without changing the on-time share. She writes both outcomes down before collecting any data. Dr. Pritchard reminds her that an outcome chosen because it is easy to count can still be the wrong one, so she adds a short justification that links each outcome to the interest of the person making the request.

### 1.3 Literature method

Hana searches legal, regulatory and empirical sources separately, because they answer different questions. For law she reads the GDPR articles directly and the LGPD, Lei 13.709/2018, whose Article 19 requires a full access response within fifteen days. For regulatory interpretation she reads the EDPB Guidelines 01/2022 on the right of access, which explain timing, identity checks and the format of answers. For empirical evidence she searches for studies of rights-request handling and records every search string, database and date, so that her review can be repeated by an examiner and later updated.

### 1.4 Baseline performance

Before any change, Hana describes the current process using 200 synthetic requests modelled on Brookfield's ticket statistics. Requests through the web form have a median of 18 days and 94.8% are completed within thirty days. Email requests have a median of 28 days with 62.5% on time, and postal requests a median of 46 days with only 29.2% on time. Overall, 74.0% of requests meet the thirty-day mark. Hana notes that the channel mix matters as much as speed, because most late requests arrive by email or post, where staff must re-key information by hand.

### Lab — Baseline completion times by channel

```python
# 200 synthetic subject access requests: days to complete and share within one month (30 days), by channel.
import random, statistics
r = random.Random(5)
ch = {"web form": (18, 9), "email": (27, 12), "post": (36, 14)}
rows = []
for _ in range(200):
    c = r.choices(list(ch), weights=[5, 4, 1])[0]
    rows.append((c, max(1, round(r.gauss(*ch[c])))))
for c in ch:
    d = [x for k, x in rows if k == c]
    print(f"{c:9s} n={len(d):3d} median {statistics.median(d):4.0f} days  within 30: {sum(x <= 30 for x in d)/len(d):5.1%}")
d = [x for _, x in rows]
print(f"all       n={len(d):3d} median {statistics.median(d):4.0f} days  within 30: {sum(x <= 30 for x in d)/len(d):5.1%}")
```

Run with `python3 lab_deadline.py`. Verified output:

```text
web form  n= 96 median   18 days  within 30: 94.8%
email     n= 80 median   28 days  within 30: 62.5%
post      n= 24 median   46 days  within 30: 29.2%
all       n=200 median   23 days  within 30: 74.0%
```

### Worked example

Hana frames the question "does a self-service portal raise on-time completion of access requests?", fixes two outcomes and finds a baseline of 74.0% within thirty days, with postal requests worst at 29.2%.

> **Synthetic case.** Ellery, Brookfield and all requests are synthetic; GDPR Articles 12 and 15, LGPD Article 19 and EDPB Guidelines 01/2022 are real.

### Errors and limits

Thirty days approximates "one month", which varies by calendar. A synthetic baseline is only as good as the statistics it was built from.

### Exercises

- **EX001 — Legal deadline.** What deadline does GDPR Article 12(3) set for answering an access request? *Rubric:* 3 = without undue delay and within one month, extendable by two months for complexity or volume;; 2 = one month only;; 1 = no deadline;; 0 = none.
- **EX002 — LGPD timing.** How long does LGPD Article 19 allow for a full access response? *Rubric:* 3 = fifteen days for a clear and complete declaration;; 2 = about two weeks;; 1 = one month;; 0 = none.
- **EX003 — Second outcome.** Why does Hana also record days to completion? *Rubric:* 3 = on-time share can hide improvements or delays within the month;; 2 = mentions detail;; 1 = ignores it;; 0 = none.
- **EX004 — Search records.** Why record search strings, databases and dates? *Rubric:* 3 = so the review can be repeated and updated;; 2 = mentions transparency;; 1 = omits;; 0 = none.
- **EX005 — Worst channel.** Which channel performs worst at baseline, and how badly? *Rubric:* 3 = post: median 46 days, 29.2% on time;; 2 = names post;; 1 = names email;; 0 = none.
- **EX006 — Overall baseline.** What share of all baseline requests is on time? *Rubric:* 3 = 74.0%;; 2 = about three quarters;; 1 = wrong;; 0 = none.
- **EX007 — Outcome justification.** Why link each outcome to the requester's interest? *Rubric:* 3 = an easy metric can miss what matters to the person exercising the right;; 2 = mentions relevance;; 1 = says counting is enough;; 0 = none.

### Synthesis

Chapter 1 frames the question and baseline. Chapter 2 holds an advanced seminar on what access rights are for.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Privacy and data protection: advanced seminar

### Learning outcomes

You will (1) explain the purpose of the right of access; (2) connect access rights to privacy theory; (3) evaluate where speed conflicts with security.

### 2.1 What access is for

In Dr. Pritchard's seminar the class reads the EDPB access guidelines, which describe the right of access as a way for people to know whether and how their data are processed and to check its lawfulness. Access is often the first step toward other rights such as rectification or erasure. Hana realises that a fast answer that is incomplete would fail this purpose. Her study therefore needs a quality check as well as a timing measure. She adds a completeness review of a sample of answers, judged against the Article 15 list of information that must be provided.

### 2.2 Access and privacy theory

The seminar links access to wider theory. Solove (2006) classifies problems such as exclusion, where people are not told about or allowed to participate in how their data are used, under information processing. Access requests are a direct remedy for exclusion. Nissenbaum's contextual integrity offers another lens: customers who gave addresses for delivery may be surprised to find them used for profiling, and an access answer reveals such flows. Acquisti, Brandimarte and Loewenstein (2015) remind the class that people are often uncertain about their own privacy preferences, which makes clear access answers even more valuable.

### 2.3 Identity checks

Speed can conflict with security. If the portal releases data to anyone who types an email address, an attacker could obtain a customer's order history. The EDPB guidelines say identity checks must be proportionate: a controller should not demand more data than needed and may rely on existing authentication, such as a customer account login. Hana records that the portal uses the existing account login and asks for extra proof only for requests from people without an account. She adds misdirected disclosure as a safety outcome, because a faster process that leaks data would be worse than a slow one.

### 2.4 Seminar discussion

The class debates whether automation removes useful human judgement. A classmate argues that staff may notice when a request comes from an abusive former partner seeking another person's data. Hana agrees and designs the portal to route requests with unusual signals, such as a request for a household account, to a trained person. She notes that the GDPR allows limits where rights of others would be harmed, as Article 15(4) states for copies. The discussion convinces her that her study must report not only on-time rates but also how exceptions are handled and how often they arise.

### Worked example

Hana adds a completeness check against Article 15, a misdirected-disclosure safety outcome and an exception route to her design after the seminar.

> **Synthetic case.** Classmates and the portal are synthetic; Solove (2006), Nissenbaum (2004), Acquisti et al. (2015), GDPR Article 15(4) and EDPB Guidelines 01/2022 are real.

### Errors and limits

Theory frames the question but does not measure it. Exception routes can become slow back doors if not monitored.

### Exercises

- **EX008 — Purpose of access.** What purpose does the EDPB attribute to the right of access? *Rubric:* 3 = knowing whether and how data are processed and checking lawfulness;; 2 = mentions transparency;; 1 = says it is customer service;; 0 = none.
- **EX009 — Exclusion.** Which Solove problem does an access request remedy directly? *Rubric:* 3 = exclusion;; 2 = names information processing;; 1 = names a wrong category;; 0 = none.
- **EX010 — Proportionate checks.** What makes an identity check proportionate? *Rubric:* 3 = it asks for no more than needed and reuses existing authentication;; 2 = mentions minimal data;; 1 = demands ID always;; 0 = none.
- **EX011 — Safety outcome.** Why add misdirected disclosure as an outcome? *Rubric:* 3 = a faster process that leaks data to the wrong person would be a net harm;; 2 = mentions security;; 1 = ignores it;; 0 = none.
- **EX012 — Exception routing.** Why route household-account requests to a person? *Rubric:* 3 = to catch requests that may harm others, as Article 15(4) contemplates;; 2 = mentions abuse;; 1 = automates all;; 0 = none.
- **EX013 — Preference uncertainty.** How does Acquisti et al. (2015) support clear access answers? *Rubric:* 3 = people are uncertain about preferences, so seeing actual data helps them decide;; 2 = mentions behaviour;; 1 = cites wrongly;; 0 = none.
- **EX014 — Completeness standard.** Against what does Hana judge an answer complete? *Rubric:* 3 = the Article 15 list of required information;; 2 = mentions Article 15;; 1 = gut feeling;; 0 = none.

### Synthesis

Chapter 2 widens the outcome set to quality and safety. Chapter 3 designs the study with ethics and reproducibility.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) choose a quasi-experimental design for an operational change; (2) plan ethics for research on rights requests; (3) set up a reproducible analysis.

### 3.1 Choosing a design

Brookfield will launch the portal for all customers on one date, so Hana cannot randomise customers. She chooses an interrupted comparison: 240 requests in the six months before launch and 240 in the six months after. Shadish, Cook and Campbell (2002) warn that such designs are vulnerable to history, maturation and changes in who is studied, so she plans to measure the request mix in both periods. She also records any other change at Brookfield during the study, such as staffing, so that it can be considered as an alternative explanation rather than discovered too late.

### 3.2 Ethics of studying requests

Rights requests contain sensitive personal data and sometimes reveal disputes. Hana's ethics application to Ellery and Brookfield's data protection officer limits her access to ticket metadata: channel, dates, complexity and outcome. She never reads request content. Brookfield extracts metadata under its own legitimate interest in improving compliance, documented in its records, and Hana receives a pseudonymised extract. She states that she will not attempt to link tickets to customers. Every result is reported in aggregate only, and categories with fewer than ten requests are merged so that no individual can be inferred.

### 3.3 Reproducible analysis

Hana writes her analysis in a script with a fixed random seed and keeps it in version control. Every figure in the dissertation is generated by the script rather than typed by hand. She stores the pseudonymised extract inside Brookfield's environment and runs the script there, exporting only aggregate tables. This arrangement means that an examiner can inspect the code and rerun it on synthetic data with the same structure, while the real extract never leaves the company. Dr. Pritchard calls this "bringing the code to the data" and asks her to describe it in the methods chapter.

### 3.4 Defining complexity

Because complex requests take longer, Hana must define complexity before seeing results. She classes a request as complex if it involves more than one system holding the person's data, a third-party processor, or a request for a copy of call recordings. Two staff members classify a sample independently to check agreement. The definition is recorded in the protocol. She explains that if complexity were defined after the results, it could be adjusted to favour the portal, which would undermine the whole design and leave her conclusions open to a charge of convenient post-hoc categories.

### Worked example

Hana chooses an interrupted before-and-after design with 240 requests per period, limits herself to pseudonymised metadata analysed inside Brookfield and defines complexity before seeing results.

> **Synthetic case.** The design and extract are synthetic; Shadish, Cook and Campbell (2002) is real.

### Errors and limits

Interrupted designs cannot rule out every alternative; measuring the request mix only reduces one threat.

### Exercises

- **EX015 — Why not randomise.** Why can Hana not randomise customers to the portal? *Rubric:* 3 = Brookfield launches it for everyone on one date;; 2 = mentions launch;; 1 = says randomisation is unethical;; 0 = none.
- **EX016 — Validity threats.** Name two threats Shadish, Cook and Campbell associate with such designs. *Rubric:* 3 = history and changes in who is studied (also maturation);; 2 = names one;; 1 = names none;; 0 = none.
- **EX017 — Metadata only.** What data may Hana see? *Rubric:* 3 = pseudonymised ticket metadata: channel, dates, complexity, outcome;; 2 = lists some;; 1 = says full tickets;; 0 = none.
- **EX018 — Small categories.** Why merge categories with fewer than ten requests? *Rubric:* 3 = to avoid inferring individuals from small counts;; 2 = mentions privacy;; 1 = omits;; 0 = none.
- **EX019 — Code to data.** What does "bringing the code to the data" mean here? *Rubric:* 3 = the script runs inside Brookfield and only aggregates leave;; 2 = mentions location;; 1 = exports data;; 0 = none.
- **EX020 — Pre-defined complexity.** Why define complexity before seeing results? *Rubric:* 3 = to stop the definition being tuned to favour the portal;; 2 = mentions bias;; 1 = says it is tidy;; 0 = none.

### Synthesis

Chapter 3 fixes design, ethics and reproducibility. Chapter 4 lists competing explanations for any improvement.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Privacy and data protection: competing explanations

### Learning outcomes

You will (1) list rival explanations for an apparent improvement; (2) design checks for each; (3) decide which rivals the study can and cannot exclude.

### 4.1 Rival one: a simpler mix

If customers after launch make simpler requests, on-time rates could rise even if the portal does nothing. Hana plans to compare the share of complex requests in the two periods and to report results separately for simple and complex requests. If the portal helps, she expects improvement within both groups, not only a change in the mix. This approach follows the standard advice of stratifying by a known confounder, which means comparing like with like before drawing conclusions about the intervention, and it is easy for a reader to understand without advanced statistics.

### 4.2 Rival two: more staff

Brookfield might hire more privacy staff at the same time, which would also speed responses. Hana asks the data protection officer for monthly staffing figures for both periods and records any change. If staffing rises, she will note it as a rival that the study cannot separate from the portal and will say so plainly. She explains that an honest dissertation names the rivals it cannot rule out, rather than hiding them, so that Brookfield's managers know how much weight to place on her findings when deciding whether to extend the portal to other request types.

### 4.3 Rival three: regression and attention

The portal launch follows a period of complaints, which may have been an unusually bad stretch. Performance could improve simply because a bad period ended, a pattern called regression to the mean. Staff may also work harder because they know they are being watched. Hana collects twelve months of history before the study to check whether the pre-period was unusual, and she keeps the measurement unobtrusive by using routine ticket data rather than asking staff to log extra information, which could change their behaviour while also adding work for an already busy team.

### 4.4 Rival four: quality trade-off

Faster answers might be less complete. Hana's completeness check on a sample of forty answers from each period addresses this. If on-time rates rise but completeness falls, the improvement is not genuine compliance. She also tracks misdirected disclosures, which must stay at zero. Dr. Pritchard asks her to commit in advance to a rule: the portal counts as an improvement only if on-time completion rises and neither completeness nor safety worsens. Hana writes this rule into the protocol, so that a headline percentage alone cannot be presented as success.

### Worked example

Hana lists four rivals (simpler mix, staffing, regression and attention, quality trade-off) and pairs each with a check: stratification, staffing records, longer history, completeness and safety outcomes.

> **Synthetic case.** Brookfield's staffing and history are synthetic.

### Errors and limits

Checks reduce but rarely remove rival explanations; unknown rivals remain.

### Exercises

- **EX021 — Stratify by complexity.** How does Hana check the "simpler mix" rival? *Rubric:* 3 = compares complex share and reports results within simple and complex groups;; 2 = mentions complexity;; 1 = ignores mix;; 0 = none.
- **EX022 — Staffing rival.** What will Hana do if staffing rises at launch? *Rubric:* 3 = report it as an unseparable rival;; 2 = mentions staff;; 1 = ignores it;; 0 = none.
- **EX023 — Regression to mean.** What is regression to the mean in this study? *Rubric:* 3 = improvement because an unusually bad period ended;; 2 = mentions chance;; 1 = confuses with trend;; 0 = none.
- **EX024 — Unobtrusive data.** Why use routine ticket data rather than extra logging? *Rubric:* 3 = extra logging could change staff behaviour and add work;; 2 = mentions observation;; 1 = omits;; 0 = none.
- **EX025 — Improvement rule.** State Hana's pre-committed improvement rule. *Rubric:* 3 = on-time rises and neither completeness nor safety worsens;; 2 = two parts;; 1 = one part;; 0 = none.
- **EX026 — Unknown rivals.** Why can listing rivals never be complete? *Rubric:* 3 = some explanations are unknown to the researcher;; 2 = mentions limits;; 1 = claims completeness;; 0 = none.

### Synthesis

Chapter 4 arms the design against rival explanations. Chapter 5 writes the proposal and checks sample size.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) estimate the sample needed to detect a change in a proportion; (2) pilot data extraction; (3) write a concise proposal.

### 5.1 How many requests

Hana asks whether 240 requests per period are enough. Using the baseline on-time rate of 0.74 and the usual settings of five per cent significance and eighty per cent power, the lab estimates the requests needed per period. Detecting a rise to 0.85 needs 211 requests, a rise to 0.90 needs 90 and a rise to 0.95 needs 46. With 240 per period she can detect a rise to 0.85 or more. A smaller improvement could be real but missed, and she writes that sentence into the proposal so that a null result is not misread as proof that the portal failed.

### 5.2 The pilot extraction

Before the main study, Hana pilots the metadata extract on one month of tickets. She finds two problems. Some tickets record the date the case was closed rather than the date the answer was sent, and some postal requests were logged only when scanned, days after arrival. Both errors would distort the timing outcome. She agrees corrections with Brookfield: completion means the date the answer was sent, and receipt means the date stamped in the post room. The EDPB access guidelines support counting from receipt, which confirms that her corrected definition matches the legal clock.

### 5.3 Writing the proposal

The proposal fits on six pages. It states the question, the outcomes and their justification, the design and rivals, the sample size, the ethics arrangements and the analysis plan. Hana includes a table that pairs each rival with its check and a timeline that ends three months before submission. Dr. Pritchard asks her to cut background and add one paragraph on what Brookfield will do with each possible result, because a study that cannot change a decision is hard to justify to a busy organisation that is lending staff time to the research.

### 5.4 Decision value

Hana writes the decision paragraph. If the portal improves on-time completion without harming quality, Brookfield will retire the email route for access requests and promote the portal. If it improves timing but harms quality, Brookfield will add a completeness check before answers are sent. If it changes nothing, Brookfield will investigate the postal process, the slowest channel. Each result leads to a specific action. She notes that writing the decision paragraph also forced her to clarify what counts as harm to quality, which made the measurement plan sharper and easier for the data protection officer to approve.

### Lab — Requests needed to detect a change in on-time completion

```python
# Requests per arm needed to detect a rise in on-time completion (two-sided alpha 0.05, power 0.80).
import math
za, zb = 1.959964, 0.841621
def n(p1, p2):
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p1 - p2) ** 2)
for p2 in [0.85, 0.90, 0.95]:
    print(f"on-time 0.74 -> {p2:.2f}: {n(0.74, p2):4d} requests per period")
```

Run with `python3 lab_power.py`. Verified output:

```text
on-time 0.74 -> 0.85:  211 requests per period
on-time 0.74 -> 0.90:   90 requests per period
on-time 0.74 -> 0.95:   46 requests per period
```

### Worked example

Hana finds that 240 requests per period detect a rise from 0.74 to 0.85 (211 needed), fixes two timing errors found in the pilot and ties every possible result to a Brookfield action.

> **Synthetic case.** Ticket data and pilot errors are synthetic; EDPB Guidelines 01/2022 are real.

### Errors and limits

Power formulas assume independent requests; repeat requesters break this slightly. A detectable change is not the same as an important one.

### Exercises

- **EX027 — Needed sample.** How many requests per period detect a rise from 0.74 to 0.90? *Rubric:* 3 = 90;; 2 = about ninety;; 1 = wrong;; 0 = none.
- **EX028 — Null result meaning.** Why must a null result not be read as failure? *Rubric:* 3 = the study may miss a real improvement smaller than detectable;; 2 = mentions power;; 1 = treats null as proof;; 0 = none.
- **EX029 — Pilot errors.** Name the two timing errors the pilot found. *Rubric:* 3 = closure date instead of answer date; postal requests logged at scanning;; 2 = names one;; 1 = vague;; 0 = none.
- **EX030 — Legal clock.** Why count from the post-room stamp? *Rubric:* 3 = the deadline runs from receipt, as the guidelines confirm;; 2 = mentions receipt;; 1 = uses scan date;; 0 = none.
- **EX031 — Proposal decision paragraph.** What does the decision paragraph add? *Rubric:* 3 = ties each result to a concrete action at Brookfield;; 2 = mentions use;; 1 = omits;; 0 = none.
- **EX032 — Detectable versus important.** Distinguish a detectable change from an important one. *Rubric:* 3 = detectable depends on sample size; important depends on harm to requesters;; 2 = defines one;; 1 = confuses them;; 0 = none.

### Synthesis

Chapter 5 sizes and pilots the study. Chapter 6 collects the data and analyses it with a bootstrap interval.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) estimate a difference in proportions with a bootstrap interval; (2) stratify by a confounder; (3) interpret results against the pre-committed rule.

### 6.1 Headline result

After six months, Hana runs the analysis on 240 requests per period, here reproduced on synthetic data. On-time completion rises from 0.708 to 0.929, a difference of 0.221. A bootstrap with 4,000 resamples, following Efron and Tibshirani (1994), gives a 95% interval from 0.154 to 0.287. The interval excludes zero by a wide margin. But the request mix also changed: complex requests fell from 33% of the total to 17%, which is exactly the rival she predicted in Chapter 4, so the headline difference cannot be read as the portal's effect on its own.

### 6.2 Within strata

Hana therefore looks within groups. Simple requests improve from 0.800 to 0.960, a difference of 0.160. Complex requests improve from 0.525 to 0.780, a difference of 0.255. Both groups improve, so the portal effect is not just a change in mix, although part of the headline difference comes from the mix. She reports both the overall and stratified results in the same table, with the stratified figures given first, so that readers do not take the larger overall number as the effect of the portal and cannot quote it without seeing the qualification.

### 6.3 Quality and safety

The completeness review finds that 38 of 40 sampled answers met the Article 15 checklist after launch, compared with 35 of 40 before, so quality did not fall. No misdirected disclosures were recorded in either period. Staffing records show no change. Applying her pre-committed rule, Hana concludes that the portal counts as an improvement. She is careful to add that the review sample is small and that a single misdirected disclosure in future would change the assessment, so the safety outcome must keep being monitored after the dissertation ends and must be owned by someone at Brookfield.

### 6.4 What remains uncertain

Hana lists what her data cannot show. The study covers one company and one year; the portal launched alongside a website redesign that may have pushed customers toward online channels; and the bootstrap interval reflects sampling variation, not the design's weaknesses. She writes that the portal is associated with a substantial improvement within both simple and complex requests, and that the most likely explanation is the portal, with the website redesign as a remaining rival. Dr. Pritchard praises the sentence because it says exactly as much as the evidence allows.

### Lab — Bootstrap difference and stratified rates

```python
# Before/after on-time rates with a bootstrap 95% interval, overall and within simple vs complex requests.
import random
r = random.Random(9)
def period(n, p_simple, p_complex, share_complex):
    out = []
    for _ in range(n):
        cx = r.random() < share_complex
        out.append((cx, r.random() < (p_complex if cx else p_simple)))
    return out
before = period(240, 0.82, 0.55, 0.30); after = period(240, 0.95, 0.70, 0.15)
rate = lambda s: sum(ok for _, ok in s) / len(s)
def boot(a, b, k=4000):
    d = sorted(rate(r.choices(b, k=len(b))) - rate(r.choices(a, k=len(a))) for _ in range(k))
    return d[int(0.025 * k)], d[int(0.975 * k)]
lo, hi = boot(before, after)
print(f"overall on-time {rate(before):.3f} -> {rate(after):.3f}; difference {rate(after)-rate(before):.3f} (95% CI {lo:.3f} to {hi:.3f})")
print(f"complex share {sum(c for c, _ in before)/240:.2f} -> {sum(c for c, _ in after)/240:.2f}")
for cx, name in [(False, "simple"), (True, "complex")]:
    a = [x for x in before if x[0] == cx]; b = [x for x in after if x[0] == cx]
    print(f"{name:7s} {rate(a):.3f} -> {rate(b):.3f}; difference {rate(b)-rate(a):.3f}")
```

Run with `python3 lab_diff.py`. Verified output:

```text
overall on-time 0.708 -> 0.929; difference 0.221 (95% CI 0.154 to 0.287)
complex share 0.33 -> 0.17
simple  0.800 -> 0.960; difference 0.160
complex 0.525 -> 0.780; difference 0.255
```

### Worked example

Hana reports on-time completion rising from 0.708 to 0.929 (difference 0.221, 95% interval 0.154 to 0.287), shows improvement within simple (0.160) and complex (0.255) requests, and confirms that completeness and safety did not worsen.

> **Synthetic case.** All rates are synthetic; Efron and Tibshirani (1994) is real.

### Errors and limits

Bootstrap intervals assume independent requests and do not cover design bias. Stratifying by one confounder leaves others.

### Exercises

- **EX033 — Bootstrap interval.** What 95% interval did the bootstrap give for the overall difference? *Rubric:* 3 = 0.154 to 0.287;; 2 = roughly 0.15 to 0.29;; 1 = wrong;; 0 = none.
- **EX034 — Mix shift.** How did the complex share change, and why does it matter? *Rubric:* 3 = 33% to 17%; part of the gain could come from easier requests;; 2 = gives figures only;; 1 = ignores it;; 0 = none.
- **EX035 — Complex stratum.** What happened to on-time completion for complex requests? *Rubric:* 3 = 0.525 to 0.780, difference 0.255;; 2 = direction only;; 1 = wrong;; 0 = none.
- **EX036 — Rule applied.** Does the portal meet the pre-committed rule, and why? *Rubric:* 3 = yes; timing rose, completeness 38/40 vs 35/40, no misdirected disclosures;; 2 = yes without evidence;; 1 = no;; 0 = none.
- **EX037 — Interval limits.** What does the bootstrap interval not capture? *Rubric:* 3 = design weaknesses such as the website redesign rival;; 2 = mentions bias;; 1 = says it captures all uncertainty;; 0 = none.
- **EX038 — Reporting order.** Why put stratified results first? *Rubric:* 3 = the overall figure exaggerates the portal effect because of mix change;; 2 = mentions clarity;; 1 = puts overall first;; 0 = none.

### Synthesis

Chapter 6 produces a bounded, stratified result. Chapter 7 writes it up with honest limitations.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure a dissertation around a claim; (2) write limitations that inform decisions; (3) report privacy safeguards used in the research.

### 7.1 Structure around a claim

Hana organises the dissertation around one claim: the portal is associated with higher on-time completion within both simple and complex access requests, without loss of completeness or safety. Each chapter supports part of that claim. The literature review explains why on-time access matters, the method explains the design and rivals, the results report the stratified figures, and the discussion weighs the remaining rival. Dr. Pritchard asks her to remove a section on cookie banners that she found interesting but that does not support the claim, and she agrees after moving the notes to a future-work appendix.

### 7.2 Limitations that matter

Hana writes limitations as information for decision-makers rather than apologies. One company limits generalisation to similar retailers; the website redesign remains an unseparated rival; the completeness sample of forty answers per period can detect only large changes; and the legal analysis follows the GDPR and LGPD texts and EDPB guidance, not court decisions. For each limitation she states its likely direction: for instance, the redesign probably inflates the effect slightly. This tells Brookfield's managers how to adjust their expectations rather than leaving them to guess how serious each weakness is.

### 7.3 Reporting safeguards

A dissertation about privacy must show it respected privacy. Hana's methods chapter describes the metadata-only extract, the analysis inside Brookfield, the merging of small categories and the ban on linking tickets to customers. She also reports one incident: an early extract contained a free-text notes column, which she noticed and returned unopened. Reporting the incident shows the safeguards worked and gives other students an example of what to watch for. Brookfield's data protection officer reviews the chapter before submission and confirms that it reveals nothing about individual customers.

### 7.4 Writing for two audiences

Hana writes the dissertation for examiners and a two-page summary for Brookfield. The summary leads with the decision: retire the email route for access requests and keep monitoring completeness and misdirected disclosures. It states the result in plain numbers, names the remaining rival and recommends a follow-up after the redesign settles. She avoids terms such as bootstrap in the summary, replacing them with "a range that the true improvement very probably lies in". Dr. Pritchard notes that a good summary lets a manager act correctly even if they never read the dissertation itself.

### Worked example

Hana builds the dissertation around one claim, writes limitations with their likely direction, reports a caught free-text incident and produces a two-page decision summary.

> **Synthetic case.** The incident and summary are synthetic; GDPR, LGPD and EDPB Guidelines 01/2022 are real.

### Errors and limits

A short summary can lose nuance; it should point to the full limitations.

### Exercises

- **EX039 — Cut section.** Why did Hana remove the cookie-banner section? *Rubric:* 3 = it did not support the central claim;; 2 = mentions focus;; 1 = keeps it;; 0 = none.
- **EX040 — Direction of bias.** Why state the likely direction of each limitation? *Rubric:* 3 = so decision-makers know how to adjust expectations;; 2 = mentions usefulness;; 1 = lists limits only;; 0 = none.
- **EX041 — Free-text incident.** What should Hana do when an extract contains free-text notes? *Rubric:* 3 = return it unopened and report the incident;; 2 = returns it;; 1 = reads it;; 0 = none.
- **EX042 — Legal scope limit.** What is the limit of Hana's legal analysis? *Rubric:* 3 = it uses statutes and EDPB guidance, not case law;; 2 = mentions sources;; 1 = omits;; 0 = none.
- **EX043 — Plain language.** How does the summary describe the bootstrap interval? *Rubric:* 3 = as a range the true improvement very probably lies in;; 2 = similar phrase;; 1 = uses jargon;; 0 = none.
- **EX044 — DPO review.** Why does the data protection officer review the methods chapter? *Rubric:* 3 = to confirm it reveals nothing about individual customers;; 2 = mentions privacy;; 1 = omits;; 0 = none.

### Synthesis

Chapter 7 writes a bounded dissertation and a decision summary. Chapter 8 faces independent review and the defense.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) respond to an independent reviewer; (2) defend design choices; (3) agree follow-up actions with the organisation.

### 8.1 Independent review

Before the defense, an independent reviewer from another university reads the dissertation. She raises three points: the bootstrap ignores repeat requesters, the completeness sample is small, and the dissertation does not discuss requests refused as manifestly unfounded or excessive under Article 12(5). Hana checks the data: repeat requesters are 3% of requests, so she reruns the analysis without them and the result barely changes. She adds a sentence about the completeness sample and a short section on refusals, which turn out to be rare, two in each period, and documented in both periods.

### 8.2 The defense

At the defense, the examiners ask why Hana did not wait a year to separate the website redesign. She answers that Brookfield needed a decision within the year and that her design makes the remaining rival explicit, so the decision can be revisited. They ask whether the portal's login-based identity check could exclude customers without accounts. She explains that such requests still go to staff with proportionate checks, and that their on-time rate is reported separately in an appendix. The examiners accept both answers and recommend minor corrections focused on clearer tables.

### 8.3 Follow-up with Brookfield

After the defense, Hana meets Brookfield's data protection officer to agree follow-up. Brookfield will retire the email route for access requests, keep the postal route for people who prefer it and add a monthly report on on-time completion, completeness and misdirected disclosures. A second review in a year will test whether the improvement persists after the website redesign settles. Hana hands over her analysis script so that Brookfield can produce the monthly report itself, and she confirms that the script runs only on pseudonymised metadata inside the company's environment.

### 8.4 Reflection

Hana reflects that the most useful parts of her study were decided early: an outcome defined by law, rivals listed before data, and a rule for what counts as improvement. The statistical analysis mattered, but it was the design that made the result believable. She also learned that privacy research must respect privacy itself, which shaped every data decision. Dr. Pritchard asks her to write these lessons as advice for next year's students, and she includes them in the dissertation's final pages as practical guidance for anyone studying a compliance process.

### Worked example

Hana answers a reviewer by rerunning without repeat requesters and adding refusals, defends her timing choice and agrees monthly monitoring and a second review with Brookfield.

> **Synthetic case.** The reviewer, examiners and follow-up are synthetic; GDPR Article 12(5) is real.

### Errors and limits

Handing over a script does not guarantee correct use; Brookfield needs an owner who understands it.

### Exercises

- **EX045 — Repeat requesters.** How did Hana address repeat requesters? *Rubric:* 3 = reran without them (3%), result barely changed;; 2 = mentions rerun;; 1 = ignores;; 0 = none.
- **EX046 — Article 12(5).** What does Article 12(5) allow? *Rubric:* 3 = refusing or charging for manifestly unfounded or excessive requests;; 2 = mentions refusal;; 1 = wrong;; 0 = none.
- **EX047 — Timing defense.** Why did Hana not wait a year for the redesign to settle? *Rubric:* 3 = Brookfield needed a decision, and the rival is explicit for later review;; 2 = mentions deadline;; 1 = says it was unnecessary;; 0 = none.
- **EX048 — No-account requests.** How are requests from people without accounts handled? *Rubric:* 3 = routed to staff with proportionate checks and reported separately;; 2 = mentions staff;; 1 = excluded;; 0 = none.
- **EX049 — Monitoring set.** What will Brookfield's monthly report include? *Rubric:* 3 = on-time completion, completeness and misdirected disclosures;; 2 = two;; 1 = one;; 0 = none.
- **EX050 — Design lesson.** What does Hana say made the result believable? *Rubric:* 3 = the design decided early: legal outcome, rivals, improvement rule;; 2 = mentions design;; 1 = says statistics;; 0 = none.

### Synthesis

Chapter 8 completes the master's route with a defended result and monitored follow-up. The worked results follow, then the references.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Hana Kobayashi, Dr. Owen Pritchard, Ellery Institute of Technology, Brookfield Online Retail and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Without undue delay and in any event within one month of receipt, extendable by two further months where necessary.

**EX002.** Up to fifteen days for a clear and complete declaration.

**EX003.** Days to completion show shifts that the binary on-time share would miss.

**EX004.** Recorded searches make the review reproducible and easy to update.

**EX005.** Post: median 46 days and only 29.2% completed within thirty days.

**EX006.** 74.0% of the 200 requests are completed within thirty days.

**EX007.** Linking outcomes to requesters' interests guards against choosing an outcome only because it is easy to count.

**EX008.** It lets people know whether and how their data are processed and verify that processing is lawful.

**EX009.** Exclusion: not being told about or allowed to participate in uses of one's data.

**EX010.** It uses no more data than necessary, for example relying on the customer's existing login.

**EX011.** Because speed bought by sending data to the wrong person is worse than a slow correct answer.

**EX012.** Human review can catch requests that seek someone else's data, protecting others' rights.

**EX013.** Because people's privacy preferences are uncertain and context-dependent, clear answers help them judge real flows.

**EX014.** Against the information Article 15 requires, such as purposes, recipients and retention.

**EX015.** The portal goes live for all customers at once, so no comparison group can be assigned.

**EX016.** History and selection shifts in who is studied; maturation is another.

**EX017.** Only pseudonymised metadata: channel, dates, complexity and outcome, never request content.

**EX018.** Small cells can point to individuals; merging them protects requesters.

**EX019.** Analysis runs where the extract lives, and only aggregate tables are exported.

**EX020.** A definition fixed in advance cannot be adjusted to flatter the intervention.

**EX021.** She measures the complex share in each period and reports on-time rates separately for simple and complex requests.

**EX022.** Name it openly as a rival the design cannot separate from the portal.

**EX023.** After an unusually bad stretch, performance tends to improve anyway, which could be mistaken for a portal effect.

**EX024.** Routine data avoids staff changing behaviour because they are being watched.

**EX025.** The portal counts as better only if on-time completion rises without loss of completeness or safety.

**EX026.** Some rivals are unknown, so a study can only address those it can identify.

**EX027.** 90 requests per period.

**EX028.** With 240 per period, improvements smaller than to 0.85 may go undetected, so no difference is not proof of no effect.

**EX029.** Tickets used closure dates instead of sent dates, and postal requests were logged late at scanning.

**EX030.** Because the legal time limit runs from when the controller receives the request.

**EX031.** It links each possible outcome to a specific Brookfield action.

**EX032.** Detectability is statistical; importance is about real effects on people and compliance.

**EX033.** 0.154 to 0.287.

**EX034.** Complex requests fell from 33% to 17%, so some of the headline gain reflects a simpler mix.

**EX035.** It rose from 0.525 to 0.780, a difference of 0.255.

**EX036.** Yes: on-time completion rose while completeness held (38/40) and safety stayed at zero incidents.

**EX037.** It reflects sampling variation only, not bias from rivals like the redesign.

**EX038.** The overall difference includes a mix shift, so stratified effects better reflect the portal.

**EX039.** It was interesting but did not support the dissertation's claim, so she moved it to future work.

**EX040.** Knowing whether a weakness inflates or deflates the effect lets managers adjust their expectations.

**EX041.** Return it unopened, get a corrected extract and report the incident in the methods chapter.

**EX042.** It follows the GDPR, LGPD and EDPB guidance, not court decisions.

**EX043.** As "a range that the true improvement very probably lies in".

**EX044.** To check that the published text cannot reveal any individual customer.

**EX045.** She reran the analysis excluding the 3% repeat requesters and the result hardly changed.

**EX046.** A controller may charge a reasonable fee or refuse manifestly unfounded or excessive requests, bearing the burden of proof.

**EX047.** Brookfield needed a decision within the year; the design states the rival so the decision can be revisited.

**EX048.** Staff handle them with proportionate identity checks, and their timing is reported separately.

**EX049.** On-time completion, completeness and misdirected disclosures.

**EX050.** Early design choices: a legally defined outcome, listed rivals and a pre-committed improvement rule.

<a id="references"></a>

## References

Every DOI was resolved through doi.org on 12 October 2026; laws and guidelines link to their official publishers. Re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. *Science, 347*(6221), 509–514. <https://doi.org/10.1126/science.aaa1465>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- European Data Protection Board. (2023). *Guidelines 01/2022 on data subject rights — Right of access* (Version 2.0 adopted 28 March 2023; Version 2.1 with minor corrections, 30 May 2024). <https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en>
- Efron, B., & Tibshirani, R. J. (1994). *An introduction to the bootstrap*. Chapman and Hall/CRC. <https://doi.org/10.1201/9780429246593>
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.
