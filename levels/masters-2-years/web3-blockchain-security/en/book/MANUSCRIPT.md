# Web3, Blockchain and Cryptoasset Security: Master's Research Track

- Language: English (`en`); course 170, Master's research track (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students and practitioners researching how privileged control of smart contracts relates to security incidents.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only contracts, wallets and systems you are authorised to assess, on local simulations or test networks; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic ledgers, transactions, contract inventories and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one master's student studying whether single keys, multi-signature wallets and timelocks are associated with key-related incidents, from question and systematic search, through an advanced seminar, study design and ethics, competing explanations, proposal and pilot, data collection and stratified analysis, writing and limitations, to independent review and defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Tariq Haddad** | Master's student | Invented |
| **Dr Ingrid Larsen** | Supervisor | Invented |
| **Northmoor University** | Fictional university | Invented |
| **Lumen Analytics** | Fictional monitoring partner | Invented |

### Core sources

Nakamoto, [Bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf); Wood, [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf); NIST [IR 8202](https://doi.org/10.6028/NIST.IR.8202); [SWC registry](https://swcregistry.io/); [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/); EEA [EthTrust Security Levels v3](https://entethalliance.org/specs/ethtrust-sl/v3/); [ConsenSys smart contract best practices](https://consensys.github.io/smart-contract-best-practices/); Atzei et al. ([2017](https://doi.org/10.1007/978-3-662-54455-6_8)); Luu et al. ([2016](https://doi.org/10.1145/2976749.2978309)). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) frame a master's question about privileged control of smart contracts; (2) design a systematic literature search; (3) record search decisions reproducibly.

### 1.1 The case

Tariq Haddad is a master's student at the fictional Northmoor University, supervised by Dr Ingrid Larsen. His partner is the fictional Lumen Analytics, a small firm that monitors blockchain protocols for its clients. Many protocols keep privileged functions, such as upgrading contract code or pausing transfers, controlled by administrator keys. Tariq asks whether the way those privileges are controlled, a single key, a multi-signature wallet, or a multi-signature wallet with a timelock delay, is associated with fewer key-related incidents. All protocols and data in this book are synthetic.

### 1.2 Sharpening the question

A good dissertation question is narrow enough to answer in a year. Tariq defines privileged control as any function that can change contract code, parameters or funds without a user's own transaction. He defines a key-related incident as an unauthorised or mistaken use of such a function that harmed users, according to a public post-incident report. He limits the population to Ethereum-compatible protocols with published administrative arrangements. Precise definitions prevent the question drifting as he reads, and make it clear which cases count.

### 1.3 Search method

Tariq designs a systematic search. He lists databases and venues, including IEEE and ACM digital libraries, and grey literature such as the EEA EthTrust Security Levels, the OWASP Smart Contract Top 10 and ConsenSys best practices. He writes search strings combining terms for smart contracts, upgradeability, administrator keys, multi-signature and timelock, and he sets inclusion criteria: peer-reviewed or standards-body sources, published in English, addressing privileged control or its failures. A written method lets others repeat the search and judge what might be missing.

### 1.4 Screening and recording

Search results are screened in two passes: title and abstract, then full text. Tariq records every decision with a reason in a spreadsheet, and Dr Larsen screens a random ten percent independently to check consistency. Of 212 records, 31 are included after full-text review. He draws a flow diagram showing how many were excluded at each stage and why. Recording screening decisions turns a reading list into evidence that the review was systematic rather than selective. The spreadsheet is kept with the dissertation appendices.

### 1.5 What the literature says

Included sources agree on principles but offer little measurement. The EthTrust specification notes that a malicious actor with a privileged key can cause harm that code review cannot prevent, and recommends timelock delays for sensitive operations. ConsenSys best practices discuss upgradeability risks. Atzei and colleagues (2017) classify attacks by cause but focus on code rather than key governance. Tariq finds no study comparing incident rates across control types with explicit attention to confounding, which shapes his contribution. He summarises each included source in a structured table.

### Worked example

Tariq defines privileged control and key-related incidents, searches six sources with written strings, and screens 212 records to 31 included, with a flow diagram and a 10% double-screen.

> **Synthetic case.** Tariq Haddad, Ingrid Larsen, Northmoor University, Lumen Analytics and all data are synthetic; EEA EthTrust, OWASP Smart Contract Top 10, ConsenSys best practices and Atzei et al. (2017) are real sources.

### Errors and limits

Reading only well-known blog posts without a search method produces a biased picture of the evidence.

### Exercises

- **EX001 — Control types.** Which three control types does Tariq compare? *Rubric:* 3 = single key, multisig, multisig with timelock;; 2 = three;; 1 = two;; 0 = none.
- **EX002 — Incident definition.** How is a key-related incident defined? *Rubric:* 3 = unauthorised or mistaken privileged use that harmed users per public report;; 2 = privileged misuse;; 1 = any bug;; 0 = none.
- **EX003 — Grey literature.** Name one grey-literature source searched. *Rubric:* 3 = EEA EthTrust;; 2 = OWASP;; 1 = novels;; 0 = none.
- **EX004 — Screening check.** How was screening consistency checked? *Rubric:* 3 = supervisor double-screened a random 10%;; 2 = 10%;; 1 = none;; 0 = none.
- **EX005 — Included count.** How many records were included? *Rubric:* 3 = 31 of 212;; 2 = 31;; 1 = 212;; 0 = none.
- **EX006 — EthTrust recommendation.** What does EthTrust recommend for sensitive operations? *Rubric:* 3 = timelock delays;; 2 = timelock;; 1 = single key;; 0 = none.
- **EX007 — Literature gap.** What gap did Tariq find? *Rubric:* 3 = no comparison of incident rates across control types with confounding;; 2 = measurement;; 1 = none;; 0 = none.

### Synthesis

A narrow question, a written search method and recorded screening decisions make a literature review reproducible.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Web3, blockchain and cryptoasset security: advanced seminar

### Learning outcomes

You will (1) explain blockchain trust assumptions; (2) analyse privileged roles and upgradeability; (3) discuss transaction ordering and monitoring.

### 2.1 Trust assumptions

In the seminar, Tariq revisits foundations. Nakamoto's Bitcoin paper shows how a public ledger can be secured without a central party, provided honest participants control most computing power. Wood's yellow paper defines Ethereum's account model and virtual machine. NIST IR 8202 explains that permissioned and permissionless ledgers make different trust assumptions. Tariq's point for the seminar is that contracts inherit these assumptions but add new ones: whoever holds privileged keys becomes a trusted party, often unnoticed by users. He illustrates this with a simple diagram of trust relationships.

### 2.2 Upgradeability

Contracts are immutable by default, but many protocols use a proxy pattern so that the code behind a fixed address can be replaced. The EthTrust specification explains that this means the system cannot be considered immutable, because the upgrade authority could point the proxy at new code. Upgradeability lets teams fix bugs, but concentrates power. The seminar discusses how documentation, access control on upgrade functions and independent review of each new implementation reduce the risk, from the defender's side. Tariq records which forms of upgrade control he will code in his study.

### 2.3 Multi-signature and timelocks

A multi-signature wallet requires several keyholders to approve an action, so one lost or stolen key is not enough. A timelock delays execution of an approved action for a set period, giving users and monitors time to see it and respond, for example by withdrawing funds. Tariq notes these controls address different failures: multi-signature reduces single-key compromise and mistakes, while timelocks add visibility. Neither helps if keyholders collude, which is why governance and transparency also matter. He records the distinction in his codebook definitions.

### 2.4 Ordering and monitoring

Daian and colleagues (2020) showed that transaction ordering creates opportunities for value extraction, and EthTrust discusses ordering attacks and recommends timelocks for sensitive operations as one mitigation. Monitoring firms like Lumen watch queued privileged actions and alert clients. The seminar asks whether a timelock window is long enough for monitors to detect, confirm and communicate a concern, a measurable question Tariq adds to his dissertation as a secondary aim. He records how Lumen defines a confirmed alert, so that detection times are measured consistently across all queued changes in the pilot and main study.

### 2.5 Seminar critique

Peers challenge Tariq: protocols that adopt timelocks may also be better funded and more careful overall, so any lower incident rate might reflect care, not the control. Another asks whether public reports undercount small incidents. Tariq records both as competing explanations to address in design. Dr Larsen notes that a dissertation that names and tests its competing explanations is stronger than one that ignores them, even if it cannot rule them all out. He adds both points to his design notes for the next chapter.

### Worked example

The seminar links ledger trust assumptions to privileged keys, upgradeability, multi-signature and timelocks; peers raise care and reporting bias as competing explanations.

> **Synthetic case.** Seminar content and peers are synthetic; Nakamoto (2008), Wood, NIST IR 8202, EEA EthTrust and Daian et al. (2020) are real sources.

### Errors and limits

Assuming a contract is immutable without checking for upgrade authority misjudges who users must trust.

### Exercises

- **EX008 — Permissioned difference.** What does NIST IR 8202 say about permissioned ledgers? *Rubric:* 3 = different trust assumptions from permissionless;; 2 = trust;; 1 = identical;; 0 = none.
- **EX009 — Proxy effect.** Why does a proxy pattern break immutability? *Rubric:* 3 = upgrade authority can point to new code;; 2 = replaceable code;; 1 = none;; 0 = none.
- **EX010 — Multisig purpose.** What does multi-signature reduce? *Rubric:* 3 = single-key compromise and mistakes;; 2 = single key risk;; 1 = delay;; 0 = none.
- **EX011 — Timelock purpose.** What does a timelock add? *Rubric:* 3 = time for users and monitors to see and respond;; 2 = visibility;; 1 = speed;; 0 = none.
- **EX012 — Collusion limit.** When do neither control help? *Rubric:* 3 = when keyholders collude;; 2 = collusion;; 1 = never;; 0 = none.
- **EX013 — Secondary aim.** What secondary aim did Tariq add? *Rubric:* 3 = whether timelock window allows detection and response;; 2 = window;; 1 = none;; 0 = none.
- **EX014 — Care confounder.** What competing explanation did peers raise? *Rubric:* 3 = careful, well-funded teams adopt timelocks;; 2 = care;; 1 = luck;; 0 = none.

### Synthesis

Privileged keys add trusted parties to blockchain systems, and controls like multi-signature and timelocks address distinct failures.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) design an observational study; (2) plan ethical data use; (3) prepare reproducible analysis.

### 3.1 Observational design

Tariq cannot assign control types to protocols, so he designs an observational study of forty protocols with published administrative arrangements over a fixed three-year window. For each protocol he records control type at the start of the window, size measured by value managed, team size, audit history and whether a key-related incident occurred. Observational designs cannot prove causation, but careful measurement of likely confounders lets him test whether associations survive adjustment. He writes each variable's definition before collecting any data, and records the window dates.

### 3.2 Data sources

Data come from public sources only: protocol documentation, public governance records, published audit reports and post-incident reports. Lumen Analytics provides timestamps of queued privileged actions from its monitoring records for the secondary aim, with client permission and with protocol names pseudonymised. Tariq writes a codebook for each variable, including how to classify mixed arrangements, such as multi-signature for upgrades but a single key for pausing, which he codes by the weakest control on any fund-affecting function. Sources are logged with retrieval dates.

### 3.3 Ethics

Although data are public, Tariq considers harm. Publishing a list of protocols with weak controls could direct attackers to them. His ethics approval requires that results be reported in aggregate, with no protocol identified, and that any currently live weakness he notices be reported privately to the team through their published security contact before the dissertation is submitted. The university's ethics committee approves the plan, noting the responsible disclosure step. Tariq also stores data on an encrypted university drive. He records the security contacts he would use, with dates.

### 3.4 Reproducibility

Tariq's analysis uses short Python scripts with only the standard library, kept under version control with the codebook and a data dictionary. Each figure in the dissertation is produced by a script, and a single command reruns them all. He keeps a log of decisions, such as reclassifying a protocol after reading its governance forum, with dates and reasons. Reproducible analysis lets examiners check every number and protects him from mistakes made by hand-editing tables. The repository is shared with Dr Larsen.

### 3.5 Power and limits

With forty protocols and an expected incident rate around one in five, Tariq's study has limited power to detect modest differences. He states this in advance and plans to report risk ratios with intervals rather than relying on significance tests. He also notes measurement limits: incidents may go unreported, and control types may change during the window. Stating limits in the design chapter shows examiners he understood them before seeing results. He also records the minimum difference he could plausibly detect, so readers can judge results fairly.

### Worked example

The design covers 40 protocols over three years with five recorded variables, aggregate-only reporting, private disclosure of live weaknesses and scripted analysis.

> **Synthetic case.** Protocols, data and approvals are synthetic.

### Errors and limits

Publishing named lists of weakly controlled protocols could direct attackers to them.

### Exercises

- **EX015 — Study size.** How many protocols are studied? *Rubric:* 3 = forty over three years;; 2 = 40;; 1 = 400;; 0 = none.
- **EX016 — Mixed coding.** How are mixed arrangements coded? *Rubric:* 3 = by the weakest control on any fund-affecting function;; 2 = weakest;; 1 = strongest;; 0 = none.
- **EX017 — Reporting rule.** How must results be reported? *Rubric:* 3 = in aggregate, no protocol identified;; 2 = aggregate;; 1 = by name;; 0 = none.
- **EX018 — Live weakness.** What happens if a live weakness is noticed? *Rubric:* 3 = reported privately to the team's security contact;; 2 = private disclosure;; 1 = published;; 0 = none.
- **EX019 — Rerun command.** How are figures reproduced? *Rubric:* 3 = one command reruns all scripts;; 2 = scripts;; 1 = by hand;; 0 = none.
- **EX020 — Power plan.** How does Tariq handle limited power? *Rubric:* 3 = report risk ratios with intervals;; 2 = intervals;; 1 = ignore;; 0 = none.

### Synthesis

A careful observational design with confounders, ethical reporting and scripted analysis supports honest conclusions.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Web3, blockchain and cryptoasset security: competing explanations

### Learning outcomes

You will (1) describe the crude association; (2) identify confounders; (3) plan analyses that test alternatives.

### 4.1 The crude comparison

Tariq first summarises incidents by control type without adjustment. A standard-library script reads the synthetic counts and prints rates and a risk ratio. Crude comparisons are a starting point, showing whether there is any association to explain, but they mix the effect of the control with everything else that differs between groups. He treats the result as a question rather than an answer. Tariq keeps the output with its date and the version of the data file. He also writes down, before running the stratified analysis, what pattern each competing explanation would predict, so he cannot adjust predictions after seeing the results.

### Lab — Crude incident rates

```python
"""Admin-control type versus key-related incidents in 40 synthetic protocols (read-only)."""
# control type: (protocols, with key-related incident)
DATA = {"single key": (12, 5), "multisig": (16, 3), "multisig+timelock": (12, 1)}

def main():
    for k, (n, i) in DATA.items():
        print(f"{k}: {i}/{n} incidents ({100 * i / n:.1f}%)")
    n = sum(v[0] for v in DATA.values()); i = sum(v[1] for v in DATA.values())
    print(f"all: {i}/{n} ({100 * i / n:.1f}%)")
    r1 = DATA["single key"][1] / DATA["single key"][0]
    r3 = DATA["multisig+timelock"][1] / DATA["multisig+timelock"][0]
    print(f"risk ratio single key vs multisig+timelock: {r1 / r3:.1f}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_controls.py`. Verified output:

```text
single key: 5/12 incidents (41.7%)
multisig: 3/16 incidents (18.8%)
multisig+timelock: 1/12 incidents (8.3%)
all: 9/40 (22.5%)
risk ratio single key vs multisig+timelock: 5.0
```

### 4.2 Reading the crude result

The run shows key-related incidents in 5 of 12 single-key protocols (41.7 percent), 3 of 16 multi-signature protocols (18.8 percent) and 1 of 12 with multi-signature and timelock (8.3 percent), 9 of 40 overall. The crude risk ratio for single key against multi-signature with timelock is 5.0. Tariq notes how few events lie behind these percentages: one incident more or less in the timelock group would change the ratio dramatically, so the estimate is fragile. He reports the counts alongside every percentage.

With a single timelocked incident, the ratio of 5.0 rests on one event: a second incident in that group would halve it to 2.5.

### 4.3 Competing explanations

Tariq lists explanations other than the control itself. Size: larger protocols may have bigger teams and more audits, and also adopt stronger controls. Care: teams that adopt timelocks may be generally more careful. Reporting: larger protocols may attract more scrutiny, so their incidents are more likely to be reported, which would work against his finding. Change over time: newer protocols may start with stronger controls. Each explanation predicts a different pattern, which tells him what to check. He writes each in one sentence.

### 4.4 Testing alternatives

For size, he will stratify by value managed. For care, he will use audit count before the window as a proxy and check whether the association persists among audited protocols. For reporting, he will compare reported incidents with Lumen's monitoring alerts for a subset. For change over time, he will check deployment year. Matching each explanation to a test makes the analysis plan concrete and shows examiners that alternatives were taken seriously, not just mentioned. Dr Larsen approves the plan.

### Worked example

Crude rates fall from 41.7% for single key to 8.3% for multisig with timelock (risk ratio 5.0), and four competing explanations are each matched to a planned test.

> **Synthetic case.** Protocols and counts are synthetic.

### Errors and limits

Reporting a crude risk ratio as the effect of a control ignores confounding by size and care.

### Exercises

- **EX021 — Crude rates.** What were the crude incident rates? *Rubric:* 3 = 41.7%, 18.8%, 8.3%;; 2 = falling;; 1 = equal;; 0 = none.
- **EX022 — Risk ratio.** What crude risk ratio did the lab report? *Rubric:* 3 = 5.0;; 2 = five;; 1 = 1.0;; 0 = none.
- **EX023 — Fragility.** Why is the estimate fragile? *Rubric:* 3 = few events, one incident would change it a lot;; 2 = small counts;; 1 = none;; 0 = none.
- **EX024 — Reporting direction.** How might reporting bias work here? *Rubric:* 3 = against the finding, larger protocols report more;; 2 = against;; 1 = for;; 0 = none.
- **EX025 — Care proxy.** What proxy measures care? *Rubric:* 3 = audit count before the window;; 2 = audits;; 1 = age;; 0 = none.
- **EX026 — Size test.** How is the size explanation tested? *Rubric:* 3 = stratify by value managed;; 2 = stratify;; 1 = ignore;; 0 = none.

### Synthesis

Crude associations raise questions; competing explanations matched to tests turn them into an analysis plan.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) finalise the proposal; (2) pilot data collection; (3) examine the timelock window with pilot data.

### 5.1 The proposal

Tariq's proposal combines the main observational study with the secondary aim about timelock windows. It states the question, definitions, data sources, codebook, analysis plan, ethics approvals and a timeline. Dr Larsen reviews it with a second academic, who asks for clearer handling of protocols that changed control type during the window; Tariq adds a rule to code exposure time under each control. A reviewed proposal settles disagreements before data collection rather than after. The revised proposal is signed and filed.

### 5.2 Piloting data collection

Tariq pilots coding on six protocols not in the main sample. Two coders classify control type and incidents independently and agree on all control types but disagree on one incident, a mistaken parameter change that caused losses but was quickly reversed. They agree it counts, since users were harmed, and the codebook gains an example. Pilots expose ambiguities that would otherwise introduce inconsistent coding across forty protocols. The pilot also shows that coding one protocol takes about forty minutes, which lets Tariq plan the main collection schedule realistically.

### Lab — Timelock window

```python
"""Does a timelock window exceed monitoring detection-and-response time? (synthetic, read-only)"""
WINDOW_H = 48
# hours from a queued privileged change to an independent monitor raising and confirming an alert
DETECT_H = [3, 5, 6, 8, 9, 11, 14, 18, 22, 26, 31, 40, 52, 70]

def main():
    inside = [d for d in DETECT_H if d <= WINDOW_H]
    print(f"queued changes reviewed {len(DETECT_H)}, window {WINDOW_H} h")
    print(f"confirmed within window {len(inside)}/{len(DETECT_H)} ({100 * len(inside) / len(DETECT_H):.1f}%)")
    s = sorted(DETECT_H); mid = len(s) // 2
    print(f"median detection {(s[mid - 1] + s[mid]) / 2:.1f} h, max {max(s)} h")
    for w in (24, 72):
        print(f"if window were {w} h: {sum(d <= w for d in DETECT_H)}/{len(DETECT_H)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_window.py`. Verified output:

```text
queued changes reviewed 14, window 48 h
confirmed within window 12/14 (85.7%)
median detection 16.0 h, max 70 h
if window were 24 h: 9/14
if window were 72 h: 14/14
```

### 5.3 Window results

Using fourteen synthetic queued privileged changes from Lumen's records, the script compares hours from queueing to a confirmed monitor alert with a 48-hour timelock. Twelve of fourteen, 85.7 percent, are confirmed within the window; the median is 16 hours and the longest 70 hours. With a 24-hour window only nine would be confirmed in time; with 72 hours all fourteen. Tariq notes that detection is not the end: users still need time to act after an alert. He reports the data source and its limits.

### 5.4 Adjusting the plan

The pilot suggests that the secondary aim should measure time to user notification as well as confirmation, so Tariq adds that variable with Lumen's agreement. He also records the two slow cases' reasons, both changes queued on a weekend when staff coverage was low, as context. Each change is recorded as a pre-collection amendment. Pilots are valuable precisely because they change the plan while change is still cheap. He also asks Lumen how weekend coverage is arranged, so the context is accurate rather than assumed.

### Worked example

Proposal review adds an exposure-time rule; the pilot clarifies incident coding; 12 of 14 queued changes are confirmed within 48 hours (median 16 h).

> **Synthetic case.** Protocols, changes and timings are synthetic.

### Errors and limits

Assuming a timelock is long enough without measuring detection and response times gives false comfort.

### Exercises

- **EX027 — Review addition.** What rule did the proposal review add? *Rubric:* 3 = code exposure time under each control;; 2 = exposure time;; 1 = none;; 0 = none.
- **EX028 — Pilot disagreement.** What did coders disagree on? *Rubric:* 3 = a quickly reversed mistaken parameter change;; 2 = reversed change;; 1 = control type;; 0 = none.
- **EX029 — Within window.** How many changes were confirmed within 48 hours? *Rubric:* 3 = 12 of 14, 85.7%;; 2 = 12;; 1 = 14;; 0 = none.
- **EX030 — Median time.** What was the median detection time? *Rubric:* 3 = 16 hours;; 2 = 16;; 1 = 48;; 0 = none.
- **EX031 — Shorter window.** How many would be confirmed with 24 hours? *Rubric:* 3 = 9 of 14;; 2 = nine;; 1 = all;; 0 = none.
- **EX032 — Slow cases.** Why were two cases slow? *Rubric:* 3 = queued on a weekend with low coverage;; 2 = weekend;; 1 = bug;; 0 = none.

### Synthesis

A reviewed proposal and a pilot that tests both coding and the timelock question make the main study sound.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) collect and code the main dataset; (2) analyse stratified results; (3) interpret with competing explanations in mind.

### 6.1 Collecting data

Tariq codes all forty protocols over six weeks, with a second coder double-coding a random quarter. Agreement on control type is complete, and on incidents one disagreement is resolved using the codebook example from the pilot. He records exposure time for three protocols that strengthened controls mid-window. Data and decisions are stored with the scripts. Disciplined collection gives the analysis a dataset whose every value can be traced to a source and a rule. Coders log time spent per protocol.

### Lab — Stratified comparison

```python
"""Stratify the control/incident comparison by protocol size (synthetic, read-only)."""
# (size, control, protocols, incidents)
ROWS = [
    ("small", "single key", 9, 4), ("small", "multisig", 6, 2), ("small", "multisig+timelock", 3, 1),
    ("large", "single key", 3, 1), ("large", "multisig", 10, 1), ("large", "multisig+timelock", 9, 0),
]

def main():
    for size in ("small", "large"):
        print(size)
        for s, c, n, i in ROWS:
            if s == size:
                print(f"  {c}: {i}/{n} ({100 * i / n:.1f}%)")
    small = sum(n for s, _, n, _ in ROWS if s == "small")
    print(f"share of single-key protocols that are small: {9}/{12}; small protocols overall: {small}/40")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_strata.py`. Verified output:

```text
small
  single key: 4/9 (44.4%)
  multisig: 2/6 (33.3%)
  multisig+timelock: 1/3 (33.3%)
large
  single key: 1/3 (33.3%)
  multisig: 1/10 (10.0%)
  multisig+timelock: 0/9 (0.0%)
share of single-key protocols that are small: 9/12; small protocols overall: 18/40
```

### 6.2 Stratified results

Stratifying by size changes the picture. Among small protocols, incidents occur in 4 of 9 single-key, 2 of 6 multi-signature and 1 of 3 timelocked protocols. Among large protocols, the rates are 1 of 3, 1 of 10 and 0 of 9. Nine of the twelve single-key protocols are small, while most timelocked ones are large. The association is weaker within strata than in the crude comparison, which shows that size explains part, though apparently not all, of the crude difference.

Among large protocols, one incident in three single-key protocols sets that rate at 33.3 percent, so even the stratified figures rest on very few events. Tariq therefore reports the stratified counts beside the crude ratio of 5.0.

### 6.3 Other checks

Restricting to protocols with at least one prior audit, the ordering of rates by control type persists but rests on very few incidents. Deployment year shows newer protocols more often start with timelocks, a pattern consistent with changing norms. For a subset, Lumen's alerts reveal two unreported small incidents, both in single-key protocols, suggesting reporting bias did not favour his hypothesis. Tariq presents these checks together so readers see how the evidence fits across tests. Each check is reported with its counts and limits.

### 6.4 Interpretation

Tariq concludes that stronger privileged controls are associated with fewer key-related incidents, that part of the crude association reflects size, and that the remaining association is uncertain because events are few. He recommends multi-signature with timelocks as consistent with EthTrust guidance and his data, while stating clearly that his study cannot prove causation. Interpretation that matches the strength of evidence earns more trust than a confident headline. He also notes that a larger dataset across several firms would be needed to estimate the effect precisely, and suggests how such data might be shared safely.

### Worked example

Stratification shows weaker but persisting associations; nine of twelve single-key protocols are small; unreported incidents in single-key protocols argue against reporting bias favouring the hypothesis.

> **Synthetic case.** Protocols and results are synthetic; EEA EthTrust is a real source.

### Errors and limits

Presenting crude rates as the final result hides the role of protocol size.

### Exercises

- **EX033 — Double-coding share.** What share was double-coded? *Rubric:* 3 = a random quarter;; 2 = 25%;; 1 = all;; 0 = none.
- **EX034 — Small strata.** What were the small-protocol rates? *Rubric:* 3 = 4/9, 2/6, 1/3;; 2 = small;; 1 = zero;; 0 = none.
- **EX035 — Large strata.** What were the large-protocol rates? *Rubric:* 3 = 1/3, 1/10, 0/9;; 2 = large;; 1 = equal;; 0 = none.
- **EX036 — Size imbalance.** How many single-key protocols were small? *Rubric:* 3 = 9 of 12;; 2 = nine;; 1 = three;; 0 = none.
- **EX037 — Unreported incidents.** What did Lumen's alerts reveal? *Rubric:* 3 = two unreported small incidents in single-key protocols;; 2 = two;; 1 = none;; 0 = none.
- **EX038 — Final claim.** What is Tariq's conclusion about causation? *Rubric:* 3 = association shown, causation not proven;; 2 = association;; 1 = proven;; 0 = none.

### Synthesis

Stratified analysis and multiple checks give a nuanced, defensible interpretation of observational data.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure the dissertation; (2) write limitations honestly; (3) connect findings to practice.

### 7.1 Structure

Tariq structures the dissertation as introduction, systematic review, design, results, discussion and conclusion, with appendices for the codebook, search strings, flow diagram and scripts. Each results section begins with the question it answers and ends with a one-sentence summary. Dr Larsen asks him to keep the discussion separate from results so readers can see what was observed before what he thinks it means. A clear structure lets examiners follow the argument without hunting for evidence. Appendices are cross-referenced from the text.

### 7.2 Limitations

Tariq writes limitations in specific terms: forty protocols and nine incidents give imprecise estimates; incidents may be underreported; control type is coded from documentation that may not match practice; care is measured only through audit count; and the timelock analysis uses fourteen changes from one monitoring firm. For each, he states the likely direction of bias where possible. Specific limitations are useful to future researchers, while vague ones only signal that something might be wrong. He also explains how each limitation could be addressed.

### 7.3 Practice implications

For practitioners, Tariq translates findings carefully: protocols with privileged functions should document who controls them, use multi-signature for fund-affecting powers, and use timelocks long enough for monitoring and user response, with his pilot suggesting that 48 hours may be too short over weekends. He links these to EthTrust and ConsenSys guidance, noting that his data are consistent with that guidance rather than independently proving it. He adds that teams should publish their privileged-control arrangements so users and monitors can judge the risk, and that timelock periods should be chosen with monitoring coverage in mind.

### 7.4 Writing process

Tariq writes in short daily sessions, sharing chapters with Dr Larsen as they are drafted. Her comments focus on claims that outrun evidence and on figures that need clearer labels. He keeps a change log of major revisions. Two weeks before submission he reruns every script from a clean copy to confirm that every number in the text matches the outputs. Careful process prevents late surprises such as a mismatched table discovered by an examiner. Dr Larsen signs off the final draft.

### Worked example

The dissertation separates results from discussion, lists five specific limitations with bias directions, and links practice advice to EthTrust and ConsenSys guidance.

> **Synthetic case.** Writing, comments and results are synthetic; EEA EthTrust and ConsenSys best practices are real sources.

### Errors and limits

Writing vague limitations hides the specific weaknesses future researchers need to know.

### Exercises

- **EX039 — Results and discussion.** Why keep results and discussion separate? *Rubric:* 3 = readers see observations before interpretation;; 2 = clarity;; 1 = length;; 0 = none.
- **EX040 — Limitation example.** Name one stated limitation. *Rubric:* 3 = nine incidents give imprecise estimates;; 2 = underreporting;; 1 = none;; 0 = none.
- **EX041 — Bias direction.** What does Tariq state for each limitation? *Rubric:* 3 = likely direction of bias;; 2 = direction;; 1 = cost;; 0 = none.
- **EX042 — Weekend implication.** What did the pilot suggest about 48 hours? *Rubric:* 3 = may be too short over weekends;; 2 = weekends;; 1 = too long;; 0 = none.
- **EX043 — Guidance relation.** How do findings relate to guidance? *Rubric:* 3 = consistent with but not independently proving it;; 2 = consistent;; 1 = contradict;; 0 = none.
- **EX044 — Final rerun.** What was done two weeks before submission? *Rubric:* 3 = reran all scripts from a clean copy;; 2 = rerun;; 1 = nothing;; 0 = none.

### Synthesis

Clear structure, specific limitations and carefully bounded practice advice make a dissertation credible and useful.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) obtain independent review; (2) defend methods and conclusions; (3) plan dissemination responsibly.

### 8.1 Independent review

Before submission, Tariq asks a researcher outside his department to review the dissertation using a short checklist: is the question answered, are methods reproducible, are claims supported, and are limitations honest? The reviewer reruns the scripts and confirms the outputs. She suggests adding a sensitivity analysis treating the reversed parameter change as a non-incident. Tariq adds it and reports that the pattern holds. Independent review catches what familiarity hides. Tariq records the reviewer's comments and his responses in an appendix so examiners can see how the dissertation changed.

### 8.2 The defense

In the oral defense, examiners ask why forty protocols, how control types were verified, what the stratified results mean, and whether the timelock analysis generalises. Tariq answers with page references and data, acknowledging where evidence is thin. One examiner asks what he would do with more time; he proposes a larger multi-firm study of timelock windows with notification times. Clear, honest answers matter more than defending every choice as perfect. After the defense, examiners request two clarifications, which Tariq makes within a week and records in the final version.

### 8.3 Dissemination

Tariq writes a short practitioner brief for Lumen's clients and a paper draft for a workshop. Both report aggregate results only, with no protocol named. Before sharing, Lumen's security lead checks that nothing could help someone target protocols with weak controls. Dr Larsen reminds him that disseminating research is part of the work, and that defenders benefit most when findings are presented with practical, clearly bounded advice. Feedback from Lumen's clients is collected to see whether the brief was understood, and Tariq revises one unclear recommendation.

### 8.4 Reflection

In his reflective appendix, Tariq notes what he would change: start the pilot earlier, collect notification times from the beginning, and recruit a second monitoring firm. He also notes what worked: the systematic search, scripted analysis and matching competing explanations to tests. Reflection shows examiners that he can evaluate his own work critically, which is a core outcome of a master's research degree. Dr Larsen adds her own short assessment of his growth as a researcher, noting that he handled competing explanations with particular care, and the appendix is filed with the dissertation.

### Worked example

An independent reviewer reruns scripts and adds a sensitivity analysis; the defense is passed, and an aggregate-only brief and workshop paper are prepared after security review.

> **Synthetic case.** Reviewers, examiners and outputs are synthetic.

### Errors and limits

Disseminating protocol-level results could direct attackers to weakly controlled systems.

### Exercises

- **EX045 — Review checklist.** What does the independent review checklist ask? *Rubric:* 3 = question answered, reproducible, supported, honest limitations;; 2 = four checks;; 1 = style;; 0 = none.
- **EX046 — Sensitivity analysis.** What sensitivity analysis was added? *Rubric:* 3 = treat reversed parameter change as non-incident;; 2 = reversed change;; 1 = none;; 0 = none.
- **EX047 — More-time answer.** What would Tariq do with more time? *Rubric:* 3 = larger multi-firm timelock study with notification times;; 2 = bigger study;; 1 = nothing;; 0 = none.
- **EX048 — Dissemination rule.** How are results disseminated? *Rubric:* 3 = aggregate only, no protocol named;; 2 = aggregate;; 1 = named;; 0 = none.
- **EX049 — Security check.** Who checks the brief before sharing? *Rubric:* 3 = Lumen's security lead;; 2 = security lead;; 1 = nobody;; 0 = none.
- **EX050 — Reflection change.** Name one thing Tariq would change. *Rubric:* 3 = start the pilot earlier;; 2 = second firm;; 1 = nothing;; 0 = none.

### Synthesis

Independent review, honest defense and responsible dissemination complete a master's dissertation.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Tariq Haddad, Dr Ingrid Larsen, Northmoor University, Lumen Analytics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A single key, a multi-signature wallet, and a multi-signature wallet with a timelock.

**EX002.** An unauthorised or mistaken use of a privileged function that harmed users, per a public report.

**EX003.** EEA EthTrust, the OWASP Smart Contract Top 10 or ConsenSys best practices.

**EX004.** Dr Larsen independently screened a random ten percent.

**EX005.** 31 of 212.

**EX006.** Timelock delays for sensitive operations.

**EX007.** No study comparing incident rates across control types with attention to confounding.

**EX008.** They make different trust assumptions from permissionless ledgers.

**EX009.** The upgrade authority can point the proxy at new code.

**EX010.** The impact of a single compromised key and individual mistakes.

**EX011.** Time for users and monitors to see a queued action and respond.

**EX012.** When keyholders collude.

**EX013.** Whether the timelock window is long enough for monitors to detect, confirm and communicate concerns.

**EX014.** That better-funded, more careful teams adopt timelocks, explaining lower incident rates.

**EX015.** Forty protocols over a three-year window.

**EX016.** By the weakest control on any fund-affecting function.

**EX017.** In aggregate, with no protocol identified.

**EX018.** It is reported privately to the team's published security contact.

**EX019.** A single command reruns all scripts producing each figure.

**EX020.** By reporting risk ratios with intervals rather than relying on significance tests.

**EX021.** 41.7% single key, 18.8% multisig and 8.3% multisig with timelock.

**EX022.** 5.0, single key against multisig with timelock.

**EX023.** Few events lie behind it, so one more or fewer incident changes the ratio greatly.

**EX024.** Against the finding, because larger protocols with stronger controls may report more.

**EX025.** Audit count before the study window.

**EX026.** By stratifying by value managed.

**EX027.** Code exposure time under each control for protocols that changed type.

**EX028.** A mistaken parameter change that caused losses but was quickly reversed.

**EX029.** 12 of 14, 85.7 percent.

**EX030.** 16 hours.

**EX031.** Nine of fourteen.

**EX032.** They were queued on a weekend when staff coverage was low.

**EX033.** A random quarter of protocols.

**EX034.** 4 of 9 single key, 2 of 6 multisig and 1 of 3 timelocked.

**EX035.** 1 of 3 single key, 1 of 10 multisig and 0 of 9 timelocked.

**EX036.** Nine of twelve.

**EX037.** Two unreported small incidents, both in single-key protocols.

**EX038.** Stronger controls are associated with fewer incidents, but causation is not proven.

**EX039.** So readers see what was observed before what it means.

**EX040.** Few incidents, underreporting, documentation-based coding, a weak care proxy or one monitoring firm.

**EX041.** The likely direction of bias where possible.

**EX042.** It may be too short over weekends.

**EX043.** They are consistent with EthTrust and ConsenSys guidance, not independent proof.

**EX044.** Every script was rerun from a clean copy to confirm numbers matched.

**EX045.** Whether the question is answered, methods are reproducible, claims supported and limitations honest.

**EX046.** Treating the reversed parameter change as a non-incident.

**EX047.** A larger multi-firm study of timelock windows including notification times.

**EX048.** In aggregate only, with no protocol named.

**EX049.** Lumen's security lead.

**EX050.** Start the pilot earlier, collect notification times from the start, or recruit a second firm.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Atzei, N., Bartoletti, M., & Cimoli, T. (2017). A survey of attacks on Ethereum smart contracts (SoK). In *Principles of Security and Trust (POST 2017)*, LNCS 10204, 164–186. Springer. <https://doi.org/10.1007/978-3-662-54455-6_8>
- Buterin, V. (2014). *Ethereum whitepaper: A next-generation smart contract and decentralized application platform*. ethereum.org. <https://ethereum.org/en/whitepaper/>
- ConsenSys Diligence. (n.d.). *Ethereum smart contract security best practices*. <https://consensys.github.io/smart-contract-best-practices/>
- Daian, P., Goldfeder, S., Kell, T., Li, Y., Zhao, X., Bentov, I., Breidenbach, L., & Juels, A. (2020). Flash Boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability. *2020 IEEE Symposium on Security and Privacy*, 910–927. <https://doi.org/10.1109/SP40000.2020.00040>
- Durieux, T., Ferreira, J. F., Abreu, R., & Cruz, P. (2020). Empirical review of automated analysis tools on 47,587 Ethereum smart contracts. *Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering*, 530–541. <https://doi.org/10.1145/3377811.3380364>
- Enterprise Ethereum Alliance. (2025). *EEA EthTrust Security Levels specification, version 3*. <https://entethalliance.org/specs/ethtrust-sl/v3/>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Luu, L., Chu, D.-H., Olickel, H., Saxena, P., & Hobor, A. (2016). Making smart contracts smarter. *Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security*, 254–269. <https://doi.org/10.1145/2976749.2978309>
- Nakamoto, S. (2008). *Bitcoin: A peer-to-peer electronic cash system*. <https://bitcoin.org/bitcoin.pdf>
- OWASP Foundation. (n.d.). *OWASP Smart Contract Top 10*. <https://owasp.org/www-project-smart-contract-top-10/>
- Perez, D., & Livshits, B. (2021). Smart contract vulnerabilities: Vulnerable does not imply exploited. *30th USENIX Security Symposium*. <https://www.usenix.org/conference/usenixsecurity21/presentation/perez>
- SmartContractSecurity. (n.d.). *Smart Contract Weakness Classification (SWC) registry*. <https://swcregistry.io/>
- Tsankov, P., Dan, A., Drachsler-Cohen, D., Gervais, A., Bünzli, F., & Vechev, M. (2018). Securify: Practical security analysis of smart contracts. *Proceedings of the 2018 ACM SIGSAC Conference on Computer and Communications Security*, 67–82. <https://doi.org/10.1145/3243734.3243780>
- Wood, G. (n.d.). *Ethereum: A secure decentralised generalised transaction ledger* (Ethereum yellow paper, continuously revised). <https://ethereum.github.io/yellowpaper/paper.pdf>
- Yaga, D., Mell, P., Roby, N., & Scarfone, K. (2018). *Blockchain technology overview* (NIST IR 8202). NIST. <https://doi.org/10.6028/NIST.IR.8202>
