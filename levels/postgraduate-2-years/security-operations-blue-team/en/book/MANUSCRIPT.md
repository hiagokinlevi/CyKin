# Security Operations and Blue Team: Postgraduate Course

- Language: English (`en`); course 153, Postgraduate course (2 years).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; Four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: experienced practitioners who lead or shape security operations and must make, evaluate and defend SOC decisions.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: monitor and respond only on systems you are authorised to defend; no exploit code, no payloads, no attack procedures and no instructions for evading detection. Detections are taught from the defender's side using synthetic telemetry. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one SOC team lead at a health insurer from a night-time contractor-account incident through design, evaluation, difficult cases and assurance to an applied project. Run each lab where it appears, attempt the five exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Daniel Okoro** | SOC team lead and postgraduate student | Invented |
| **Prof. Miriam Achebe** | Programme tutor | Invented |
| **Meridian Health Insurance** | Fictional insurer | Invented |
| **Hollins College** | Fictional college | Invented |

### Core sources

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker and Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame SOC decisions under uncertainty with explicit costs; (2) compare response options by expected cost; (3) recognise when probability estimates change the best option; (4) record decisions and their rationale.

### 1.1 Decisions under uncertainty

**Daniel Okoro** leads the SOC of the fictional **Meridian Health Insurance** and studies on a postgraduate programme at the fictional **Hollins College**, tutored by **Prof. Miriam Achebe**. Every night his analysts decide whether to contain, monitor or close alerts without knowing for certain what is happening. Postgraduate practice makes those decisions explicit.

Section one point one develops advanced security decision-making with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section one point one, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

### 1.2 The case

At 23:40 an alert reports a contractor account exporting claims records from an unusual address. Analysts estimate a 30% chance it is malicious. Disabling the account would stop a contractor's legitimate batch job; waiting risks a large disclosure of health data.

Section one point two develops advanced security decision-making with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section one point two, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section one point two treats decisions under uncertainty the as testable only when evidence and ticket IDs are recorded.

### 1.3 Expected cost

Each option has a cost if the activity is malicious and a cost if benign. Multiplying by probabilities and summing gives an expected cost. It does not predict what will happen; it shows which option is least costly on average given current beliefs.

Section one point three develops advanced security decision-making with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section one point three, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section one point three treats decisions under uncertainty the as testable only when evidence and ticket IDs are recorded.

### Lab — comparing response options

```python
"""Expected cost of three response options for a suspicious claims-system session (synthetic)."""
p_malicious = 0.30
options = {  # option: (cost if malicious, cost if benign)  in thousands
    "contain now (disable account)": (20, 8),
    "monitor 2 hours then decide":   (140, 0.5),
    "close as benign":               (600, 0),
}
for name, (cm, cb) in options.items():
    ev = p_malicious * cm + (1 - p_malicious) * cb
    print(f"{name:30} expected cost = {ev:6.1f}k")
for p in (0.05, 0.30):
    best = min(options, key=lambda o: p*options[o][0] + (1-p)*options[o][1])
    print(f"p(malicious)={p:.2f} -> lowest expected cost: {best}")
```

Run with `python3 lab_decision.py`. Verified output:

```text
contain now (disable account)  expected cost =   11.6k
monitor 2 hours then decide    expected cost =   42.4k
close as benign                expected cost =  180.0k
p(malicious)=0.05 -> lowest expected cost: monitor 2 hours then decide
p(malicious)=0.30 -> lowest expected cost: contain now (disable account)
```

### 1.4 Reading the result

At a 30% chance of malice, containing now has an expected cost of 11.6k, against 42.4k for monitoring and 180k for closing. At 5%, monitoring becomes cheaper. The best choice depends on the probability, so better evidence is worth gathering quickly.

Section one point four develops advanced security decision-making with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section one point four, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section one point four treats decisions under uncertainty the as testable only when evidence and ticket IDs are recorded.

### 1.5 Beyond numbers

Costs of health-data disclosure include regulatory, contractual and human harm that is hard to price. Decisions also respect legal duties that are not trade-offs. Expected cost informs judgement; it does not replace it.

Section one point five develops advanced security decision-making with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section one point five, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section one point five treats decisions under uncertainty the as testable only when evidence and ticket IDs are recorded.

### 1.6 Recording decisions

The on-call manager logs the decision, the probability estimate, the evidence and who decided. Reviewers can later judge the decision on what was known, not on hindsight.

Section one point six develops advanced security decision-making with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section one point six, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section one point six treats decisions under uncertainty the as testable only when evidence and ticket IDs are recorded.

For section one point six, Meridian Health Insurance will not accept advanced work without a written trail.

### Worked example

Daniel's analysts contain at 23:52. The next morning, the contractor confirms the export was not theirs: their credentials had been phished. The decision record shows that containment was chosen at 30% belief because the disclosure cost dominated, not because the outcome was known.

> **Synthetic case.** Meridian, Hollins College and all people and figures are invented; costs come from the lab script.

### Errors and limits

Probabilities in SOC decisions are judgements; state them as ranges and update them as evidence arrives.

### Exercises

- **EX001 — Expected cost.** Define expected cost for a response option. *Rubric:* 3 = probability-weighted sum of costs if malicious and if benign; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Lab values.** Give the three expected costs at p = 0.30. *Rubric:* 3 = 11.6k, 42.4k, 180.0k; 2 = two; 1 = one; 0 = none.
- **EX003 — Switching point.** What changes at p = 0.05, and why does it matter? *Rubric:* 3 = monitoring becomes cheapest; best option depends on probability; evidence valuable; 2 = partial; 1 = nothing; 0 = none.
- **EX004 — Limits of numbers.** Why does expected cost not replace judgement? *Rubric:* 3 = hard-to-price harms; legal duties not trade-offs; 2 = partial; 1 = it does; 0 = none.
- **EX005 — Decision record.** What should a decision record contain? *Rubric:* 3 = decision, probability, evidence, decider, time; 2 = three; 1 = one; 0 = none.

### Synthesis

Make SOC decisions explicit: estimate probabilities and costs, compare options and record the reasoning for fair later review.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Security operations and blue team: current practice

### Learning outcomes

You will (1) survey current SOC practice and its tensions; (2) relate practice to published frameworks and studies; (3) assess one's own SOC against peers; (4) identify practices worth adopting.

### 2.1 The modern SOC

Current SOCs combine SIEM or data platforms, endpoint detection, identity analytics, case management and automation. Many use managed services for some hours or functions. Knerler, Parker and Zimmerman (2022) describe eleven strategies covering mission, authority, structure, staffing, response, intelligence, data, tools, communication, measurement and expansion.

Section two point one develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section two point one, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section two point one treats the modern soc detection as testable only when evidence and ticket IDs are recorded.

### 2.2 Detection engineering

Detections are increasingly managed as code in shared formats such as Sigma, mapped to MITRE ATT&CK and tested before release. This shifts SOCs from buying content to engineering it.

Section two point two develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section two point two, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section two point two treats the modern soc detection as testable only when evidence and ticket IDs are recorded.

### 2.3 Alert overload

Studies continue to report alert fatigue and benign triggers (Alahmadi et al., 2022). Automation and better context are common responses, with mixed results.

Section two point three develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section two point three, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section two point three treats the modern soc detection as testable only when evidence and ticket IDs are recorded.

For section two point three, Meridian Health Insurance will not accept security work without a written trail.

### 2.4 Managed detection and response

Outsourcing night or tier-1 work gives coverage but risks losing local knowledge. Contracts need clear escalation, data access and quality measures.

Section two point four develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section two point four, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section two point four treats the modern soc detection as testable only when evidence and ticket IDs are recorded.

For section two point four, Meridian Health Insurance will not accept security work without a written trail.

### 2.5 Maturity assessment

The SOC-CMM (van Os, 2016) lets SOCs self-assess across business, people, process, technology and services. Meridian's last assessment showed strong tooling but weak service definitions.

Section two point five develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section two point five, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section two point five treats the modern soc detection as testable only when evidence and ticket IDs are recorded.

For section two point five, Meridian Health Insurance will not accept security work without a written trail.

### 2.6 Regulation

Health insurers face data protection and sector regulation; incident reporting timelines shape SOC procedures.

Section two point six develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section two point six, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section two point six treats the modern soc detection as testable only when evidence and ticket IDs are recorded.

For section two point six, Meridian Health Insurance will not accept security work without a written trail.

### 2.7 Comparing with peers

Daniel joins a sector forum where SOC leads share anonymised practices and metrics.

Section two point seven develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section two point seven, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section two point seven treats the modern soc detection as testable only when evidence and ticket IDs are recorded.

For section two point seven, Meridian Health Insurance will not accept security work without a written trail.

### Threat-informed defence

Many SOCs now prioritise work by the techniques their likely adversaries use, drawn from intelligence and ATT&CK, rather than by what tools happen to alert on. This keeps detection effort tied to real risk.

### Worked example

Daniel compares Meridian with three forum peers. Two have documented service catalogues listing what the SOC provides to each business unit; Meridian does not. He drafts a catalogue: monitoring, investigation, insider-risk support, detection engineering and incident coordination, each with scope and service levels.

> **Synthetic case.** The forum and comparisons are invented.

### Errors and limits

Peer practice reflects their context; adopt practices for reasons that apply to you.

### Exercises

- **EX006 — Eleven strategies.** Name four of the eleven SOC strategy areas. *Rubric:* 3 = four of mission, authority, structure, staffing, response, intelligence, data, tools, communication, measurement, expansion; 2 = three; 1 = one; 0 = none.
- **EX007 — Detection as code.** What shift does detection-as-code represent? *Rubric:* 3 = from buying content to engineering tested, versioned detections; 2 = partial; 1 = vague; 0 = none.
- **EX008 — MDR risk.** What is the main risk of managed detection and response? *Rubric:* 3 = losing local knowledge; needs escalation and quality terms; 2 = partial; 1 = cost; 0 = none.
- **EX009 — Maturity gap.** What did Meridian's SOC-CMM assessment reveal? *Rubric:* 3 = strong tooling, weak service definitions; 2 = partial; 1 = none; 0 = none.
- **EX010 — Service catalogue.** What did Daniel's draft catalogue list? *Rubric:* 3 = monitoring, investigation, insider support, detection engineering, coordination with scope and levels; 2 = three; 1 = one; 0 = none.

### Synthesis

Current practice blends engineering, automation and sourcing choices; compare with peers to find practices that fit your context.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Security operations and blue team: specialist evidence

### Learning outcomes

You will (1) use specialist evidence such as access logs, peer baselines and business context; (2) build peer-group comparisons for insider-risk monitoring; (3) interpret outliers carefully; (4) protect fairness and privacy in people-focused monitoring.

### 3.1 Specialist evidence

Some SOC questions need evidence beyond network and endpoint logs: application access logs, HR role data and business workload. At Meridian, claims-system logs record each record a handler opens.

Section three point one develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section three point one, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section three point one treats specialist evidence insider risk as testable only when evidence and ticket IDs are recorded.

### 3.2 Insider risk

Insurers worry about staff viewing records without business need, for curiosity or fraud. Monitoring such access must be fair: people are compared with peers doing similar work, not with the whole company.

Section three point two develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section three point two, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section three point two treats specialist evidence insider risk as testable only when evidence and ticket IDs are recorded.

### 3.3 Peer baselines

A peer-group median is robust to one unusual person. Comparing each handler's weekly views with their team's median highlights unusual workloads.

Section three point three develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section three point three, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section three point three treats specialist evidence insider risk as testable only when evidence and ticket IDs are recorded.

For section three point three, Meridian Health Insurance will not accept security work without a written trail.

### Lab — peer comparison

```python
"""Compare each claims handler's record views with their peer-group median (synthetic, one week)."""
import statistics
views = {"team-A": {"h01": 410, "h02": 395, "h03": 430, "h04": 1260, "h05": 405},
         "team-B": {"h11": 120, "h12": 135, "h13": 128, "h14": 118, "h15": 131}}
for team, people in views.items():
    med = statistics.median(people.values())
    for h, v in people.items():
        ratio = v / med
        print(f"{team} {h} views={v:5} peer median={med:5.0f} ratio={ratio:4.2f} {'REVIEW' if ratio >= 2.5 else ''}")
```

Run with `python3 lab_peer.py`. Verified output:

```text
team-A h01 views=  410 peer median=  410 ratio=1.00 
team-A h02 views=  395 peer median=  410 ratio=0.96 
team-A h03 views=  430 peer median=  410 ratio=1.05 
team-A h04 views= 1260 peer median=  410 ratio=3.07 REVIEW
team-A h05 views=  405 peer median=  410 ratio=0.99 
team-B h11 views=  120 peer median=  128 ratio=0.94 
team-B h12 views=  135 peer median=  128 ratio=1.05 
team-B h13 views=  128 peer median=  128 ratio=1.00 
team-B h14 views=  118 peer median=  128 ratio=0.92 
team-B h15 views=  131 peer median=  128 ratio=1.02
```

### 3.4 Reading the result

In team A, h04 viewed 1,260 records against a peer median of 410 — a ratio of 3.07, flagged for review. All other handlers in both teams are within 0.92–1.05 of their medians. Team B's lower volumes do not distort team A's comparison because each team has its own baseline.

Section three point four develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section three point four, Prof. Miriam Achebe expects security claims to carry owners and dates.

### 3.5 Interpreting outliers

A flag is a question, not an accusation. High volume may reflect assignment to a backlog, a special project or a data-quality task.

Section three point five develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section three point five, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section three point five treats specialist evidence insider risk as testable only when evidence and ticket IDs are recorded.

For section three point five, Meridian Health Insurance will not accept security work without a written trail.

### 3.6 Fairness and privacy

Insider-risk monitoring is governed by policy agreed with HR, legal and staff representatives. Reviews are done by a small, trained group; managers are not told of flags unless review finds a concern.

Section three point six develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section three point six, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section three point six treats specialist evidence insider risk as testable only when evidence and ticket IDs are recorded.

### Worked example

Daniel's analyst checks the claims system's assignment table: h04 was assigned 900 legacy claims for a migration project that week. Views were of assigned records only. The flag is closed with a note, and the assignment data is added as enrichment so future project work is visible automatically.

> **Synthetic case.** Handlers and figures come from the lab script.

### Errors and limits

Peer baselines fail when a team is small or roles differ within it.

### Exercises

- **EX011 — Peer median.** Why compare to a peer-group median rather than the company average? *Rubric:* 3 = similar work; robust to one outlier; 2 = partial; 1 = no reason; 0 = none.
- **EX012 — Lab flag.** Which handler was flagged and with what ratio? *Rubric:* 3 = h04, 1,260 vs 410, ratio 3.07; 2 = partial; 1 = wrong; 0 = none.
- **EX013 — Outlier meaning.** What does a flag mean in insider monitoring? *Rubric:* 3 = a question to review, not an accusation; 2 = partial; 1 = guilt; 0 = none.
- **EX014 — Governance.** Who agrees the insider-monitoring policy? *Rubric:* 3 = HR, legal, staff representatives (with SOC); 2 = two; 1 = one; 0 = none.
- **EX015 — Flag resolution.** How was h04's flag resolved and what changed? *Rubric:* 3 = migration assignment; closed; assignment data added as enrichment; 2 = partial; 1 = none; 0 = none.

### Synthesis

Specialist evidence enables insider-risk monitoring, but only with fair baselines, context and strong governance.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) analyse SOC risk decisions with ethical frameworks; (2) balance security, privacy and employee trust; (3) handle conflicts between business pressure and duty; (4) design ethical safeguards into SOC processes.

### 4.1 Risk and ethics together

SOC decisions are risk decisions with ethical content: monitoring staff, sharing data with partners and choosing whom to notify after a breach.

Section four point one develops advanced risk and ethics with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section four point one, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section four point one treats risk and ethics together as testable only when evidence and ticket IDs are recorded.

For section four point one, Meridian Health Insurance will not accept advanced work without a written trail.

### 4.2 Ethical lenses

Consequences ask which choice produces the least harm. Duties ask what obligations apply regardless of outcome, such as honesty to affected people. Fairness asks whether burdens fall equally. Using several lenses reveals considerations one would miss.

Section four point two develops advanced risk and ethics with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section four point two, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section four point two treats risk and ethics together as testable only when evidence and ticket IDs are recorded.

### 4.3 Business pressure

After the contractor incident, a business manager asks the SOC to delay notifying affected policyholders until after a product launch. Legal duties and honesty make that unacceptable; Daniel escalates to the CISO and the data protection officer.

Section four point three develops advanced risk and ethics with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section four point three, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section four point three treats risk and ethics together as testable only when evidence and ticket IDs are recorded.

### 4.4 Employee trust

Heavy-handed monitoring can damage trust and reporting. Transparent policies, proportionate monitoring and fair review keep trust.

Section four point four develops advanced risk and ethics with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section four point four, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section four point four treats risk and ethics together as testable only when evidence and ticket IDs are recorded.

For section four point four, Meridian Health Insurance will not accept advanced work without a written trail.

### 4.5 Safeguards

Meridian's safeguards: written purpose for each monitoring use, minimum access for reviewers, audit of SOC searches, and an ethics review for new monitoring of people.

Section four point five develops advanced risk and ethics with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section four point five, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section four point five treats risk and ethics together as testable only when evidence and ticket IDs are recorded.

For section four point five, Meridian Health Insurance will not accept advanced work without a written trail.

### 4.6 Third parties

Contractors and partners have access too; contracts set their security obligations and the SOC's rights to monitor and investigate.

Section four point six develops advanced risk and ethics with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section four point six, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section four point six treats risk and ethics together as testable only when evidence and ticket IDs are recorded.

For section four point six, Meridian Health Insurance will not accept advanced work without a written trail.

### 4.7 Accountability

Decisions with ethical weight are recorded with the reasoning, so they can be examined later.

Section four point seven develops advanced risk and ethics with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section four point seven, Prof. Miriam Achebe expects advanced claims to carry owners and dates.

Section four point seven treats risk and ethics together as testable only when evidence and ticket IDs are recorded.

For section four point seven, Meridian Health Insurance will not accept advanced work without a written trail.

### Speaking up

Analysts who see something wrong — a manager misusing SOC access, or a request to hide findings — need a safe route to raise it. Meridian's policy names the CISO and an independent ethics contact.

### Worked example

The ethics review for a proposed keystroke-timing monitor for claims staff rejects it: the purpose (detecting account sharing) can be met by less intrusive means, such as device and session checks. Daniel records the decision and the alternative adopted.

> **Synthetic case.** The proposals and reviews are invented.

### Errors and limits

Ethical frameworks do not give single answers; they structure discussion.

### Exercises

- **EX016 — Three lenses.** Name three ethical lenses and what each asks. *Rubric:* 3 = consequences, duties, fairness with questions; 2 = two; 1 = one; 0 = none.
- **EX017 — Delay request.** How did Daniel handle the request to delay notification? *Rubric:* 3 = unacceptable; escalated to CISO and DPO; 2 = partial; 1 = agreed; 0 = none.
- **EX018 — Trust.** Why does heavy monitoring risk security itself? *Rubric:* 3 = erodes trust and reporting; 2 = partial; 1 = no effect; 0 = none.
- **EX019 — Safeguards list.** List three of Meridian's ethical safeguards. *Rubric:* 3 = purpose, minimum access, audit, ethics review (three); 2 = two; 1 = one; 0 = none.
- **EX020 — Keystroke decision.** Why was keystroke-timing monitoring rejected? *Rubric:* 3 = purpose met by less intrusive device/session checks; 2 = partial; 1 = cost; 0 = none.

### Synthesis

Treat SOC risk decisions as ethical decisions; use several lenses, resist improper pressure and build safeguards into process.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security operations and blue team: design alternatives

### Learning outcomes

You will (1) generate alternative designs for SOC coverage; (2) evaluate in-house, managed and hybrid options; (3) use weighted criteria and sensitivity checks; (4) present a recommendation with trade-offs.

### 5.1 The design question

Meridian's SOC is staffed 07:00–19:00; nights rely on on-call engineers. The contractor incident at 23:40 was caught only because the on-call engineer was awake. The board asks for 24/7 coverage options.

Section five point one develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section five point one, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section five point one treats the design question alternatives as testable only when evidence and ticket IDs are recorded.

### 5.2 Alternatives

Option A: hire for in-house 24/7 (five more analysts). Option B: managed detection and response for nights. Option C: hybrid — managed tier-1 at night with in-house escalation and an automated containment playbook for high-confidence alerts.

Section five point two develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section five point two, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section five point two treats the design question alternatives as testable only when evidence and ticket IDs are recorded.

### 5.3 Criteria

Detection quality, response speed, cost, local knowledge, data control and resilience. Each is weighted with the CISO.

Section five point three develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section five point three, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section five point three treats the design question alternatives as testable only when evidence and ticket IDs are recorded.

For section five point three, Meridian Health Insurance will not accept security work without a written trail.

### 5.4 Scoring

A scores high on knowledge and control but high cost and hiring risk; B is cheapest but weakest on knowledge; C balances them.

Section five point four develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section five point four, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section five point four treats the design question alternatives as testable only when evidence and ticket IDs are recorded.

For section five point four, Meridian Health Insurance will not accept security work without a written trail.

### 5.5 Sensitivity

Daniel checks whether the recommendation changes if weights shift. C stays best unless cost weight is doubled, when B wins narrowly. The recommendation is therefore robust to reasonable disagreement.

Section five point five develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section five point five, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section five point five treats the design question alternatives as testable only when evidence and ticket IDs are recorded.

### 5.6 Risks of C

Managed analysts may escalate too much or too little; automation could wrongly disable accounts. Mitigations: quality reviews, escalation targets, automation limits.

Section five point six develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section five point six, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section five point six treats the design question alternatives as testable only when evidence and ticket IDs are recorded.

For section five point six, Meridian Health Insurance will not accept security work without a written trail.

### 5.7 Presenting

The board paper shows options, scores, sensitivity and risks on two pages.

Section five point seven develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section five point seven, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section five point seven treats the design question alternatives as testable only when evidence and ticket IDs are recorded.

For section five point seven, Meridian Health Insurance will not accept security work without a written trail.

### Stakeholder views

Daniel interviews analysts, the on-call engineers and the CISO before scoring. Analysts worry that a managed provider will send vague escalations at 03:00; engineers want fewer night calls. These views shape the escalation targets written into option C and make the final design one that the people running it can support.

### Worked example

The board chooses C with a six-month review. Daniel defines success: night P1 alerts acknowledged within 15 minutes, escalation precision above 50%, no wrongful automated containments of critical accounts.

> **Synthetic case.** Options and scores are invented.

### Errors and limits

Scoring tables give an appearance of precision; the discussion around weights matters more than the numbers.

### Exercises

- **EX021 — Three options.** Describe options A, B and C. *Rubric:* 3 = in-house 24/7, MDR nights, hybrid with escalation and automation; 2 = two; 1 = one; 0 = none.
- **EX022 — Criteria.** List the six evaluation criteria. *Rubric:* 3 = detection, speed, cost, knowledge, control, resilience; 2 = four; 1 = two; 0 = none.
- **EX023 — Sensitivity.** What did the sensitivity check show? *Rubric:* 3 = C robust unless cost weight doubled (then B); 2 = partial; 1 = none; 0 = none.
- **EX024 — Risks of C.** Name two risks of option C and their mitigations. *Rubric:* 3 = over/under escalation (reviews, targets); wrongful automation (limits); 2 = one; 1 = none; 0 = none.
- **EX025 — Success measures.** What success measures were set? *Rubric:* 3 = night P1 ack ≤15 min, escalation precision >50%, no wrongful critical containments; 2 = two; 1 = one; 0 = none.

### Synthesis

Generate real alternatives, score them on agreed criteria, test sensitivity and present trade-offs honestly.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Security operations and blue team: controlled evaluation

### Learning outcomes

You will (1) design a controlled evaluation of a SOC process change; (2) analyse skewed operational data with medians and bootstrap intervals; (3) guard against confounding; (4) report effects with uncertainty.

### 6.1 The change

Daniel's team writes a new triage playbook for claims-export alerts that starts with three automated enrichment lookups — assignment data, contractor status and export destination — before analyst review.

Section six point one develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section six point one, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section six point one treats the change evaluation design as testable only when evidence and ticket IDs are recorded.

### 6.2 Evaluation design

For four weeks, alerts are assigned alternately to the old and new playbook by alert number, so busy and quiet periods fall into both groups. Analysts rotate between playbooks. Sixteen alerts fall in each group.

Section six point two develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section six point two, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section six point two treats the change evaluation design as testable only when evidence and ticket IDs are recorded.

### 6.3 Measure

Triage time in minutes from pickup to decision, plus decision accuracy checked by a senior analyst.

Section six point three develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section six point three, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section six point three treats the change evaluation design as testable only when evidence and ticket IDs are recorded.

For section six point three, Meridian Health Insurance will not accept security work without a written trail.

### Lab — bootstrap difference in medians

```python
"""Bootstrap interval for the difference in median triage minutes between two playbooks (synthetic)."""
import random, statistics
random.seed(42)
old = [18, 22, 25, 19, 30, 27, 21, 24, 35, 20, 26, 23, 29, 31, 22, 28]
new = [14, 17, 16, 21, 15, 19, 18, 13, 25, 16, 20, 17, 22, 15, 19, 18]
obs = statistics.median(old) - statistics.median(new)
diffs = []
for _ in range(5000):
    a = [random.choice(old) for _ in old]; b = [random.choice(new) for _ in new]
    diffs.append(statistics.median(a) - statistics.median(b))
diffs.sort()
print(f"median old={statistics.median(old)} new={statistics.median(new)} difference={obs}")
print(f"bootstrap 95% interval [{diffs[124]}, {diffs[4874]}]")
```

Run with `python3 lab_bootstrap.py`. Verified output:

```text
median old=24.5 new=17.5 difference=7.0
bootstrap 95% interval [3.5, 11.0]
```

### 6.4 Reading the result

The median triage time fell from 24.5 to 17.5 minutes, a difference of 7.0. The bootstrap 95% interval for the difference is 3.5 to 11.0 minutes, which excludes zero. Medians suit skewed times; bootstrapping gives an interval without assuming a distribution.

Section six point four develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section six point four, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section six point four treats the change evaluation design as testable only when evidence and ticket IDs are recorded.

### 6.5 Accuracy

The senior analyst found one wrong decision in each group, so faster triage did not cost accuracy in this sample.

Section six point five develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section six point five, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section six point five treats the change evaluation design as testable only when evidence and ticket IDs are recorded.

For section six point five, Meridian Health Insurance will not accept security work without a written trail.

### 6.6 Confounding

Alternating assignment protects against time-of-day effects; rotation protects against one fast analyst using one playbook. Remaining risk: analysts knew which playbook they used and may have tried harder with the new one.

Section six point six develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section six point six, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section six point six treats the change evaluation design as testable only when evidence and ticket IDs are recorded.

### Practical significance

A 7-minute saving per alert across about 400 claims-export alerts a month frees roughly 47 analyst hours, enough to fund a weekly threat-hunting session.

### Next step

After three months the team repeats the measurement on routine data.

### Worked example

Daniel's report: "The new playbook reduced median triage time by 7.0 minutes (95% bootstrap interval 3.5–11.0) over 32 alerts, with equal accuracy. Analysts were not blind to condition; we will recheck after three months of routine use."

> **Synthetic case.** Times come from the lab script.

### Errors and limits

Thirty-two alerts give a wide interval; operational change may wear off or improve with familiarity.

### Exercises

- **EX026 — Assignment.** How were alerts assigned and why? *Rubric:* 3 = alternating by number; spreads busy/quiet periods; 2 = partial; 1 = random choice by analyst; 0 = none.
- **EX027 — Lab result.** Report medians, difference and interval. *Rubric:* 3 = 24.5, 17.5, 7.0, [3.5, 11.0]; 2 = partial; 1 = wrong; 0 = none.
- **EX028 — Why bootstrap.** Why use medians and bootstrap here? *Rubric:* 3 = skewed times; no distribution assumption; 2 = partial; 1 = habit; 0 = none.
- **EX029 — Accuracy check.** Did speed cost accuracy? *Rubric:* 3 = no; one error per group; 2 = partial; 1 = unknown; 0 = none.
- **EX030 — Remaining confound.** What confounding risk remains? *Rubric:* 3 = analysts not blind; may try harder with new; 2 = partial; 1 = none; 0 = none.

### Synthesis

Controlled operational evaluations need fair assignment, robust statistics, accuracy checks and honest notes on confounding.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Security operations and blue team: organizational integration

### Learning outcomes

You will (1) integrate the SOC with business units, IT, legal and HR; (2) define service levels and escalation paths; (3) align SOC work with enterprise risk management; (4) manage change across teams.

### 7.1 The SOC in the organisation

NIST CSF 2.0's Govern function places cybersecurity within enterprise risk management. The SOC is one part: it detects and responds, but depends on business units for context and on IT for action.

Section seven point one develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section seven point one, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section seven point one treats the soc in the as testable only when evidence and ticket IDs are recorded.

### 7.2 Service levels

Daniel's service catalogue sets levels: P1 alerts acknowledged in 15 minutes, investigations started within 4 hours, monthly reports to each business unit.

Section seven point two develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section seven point two, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section seven point two treats the soc in the as testable only when evidence and ticket IDs are recorded.

For section seven point two, Meridian Health Insurance will not accept security work without a written trail.

### 7.3 Escalation paths

For claims-system alerts, escalation goes to the claims operations manager for business context, to IT for account actions, to legal and the DPO for possible breaches, and to HR only when misconduct is suspected after review.

Section seven point three develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section seven point three, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section seven point three treats the soc in the as testable only when evidence and ticket IDs are recorded.

### 7.4 Risk reporting

The SOC reports risks in business terms to the enterprise risk committee: likelihood and impact of data disclosure, trends and treatment actions.

Section seven point four develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section seven point four, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section seven point four treats the soc in the as testable only when evidence and ticket IDs are recorded.

For section seven point four, Meridian Health Insurance will not accept security work without a written trail.

### 7.5 Hybrid model integration

With the managed night service, integration includes data access agreements, an escalation runbook and a shared case system.

Section seven point five develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section seven point five, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section seven point five treats the soc in the as testable only when evidence and ticket IDs are recorded.

For section seven point five, Meridian Health Insurance will not accept security work without a written trail.

### 7.6 Change management

New monitoring or response capabilities are introduced with communication to affected teams, training and feedback.

Section seven point six develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section seven point six, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section seven point six treats the soc in the as testable only when evidence and ticket IDs are recorded.

For section seven point six, Meridian Health Insurance will not accept security work without a written trail.

### 7.7 Relationships

Daniel meets each business unit lead quarterly; regular contact makes incident calls smoother.

Section seven point seven develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section seven point seven, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section seven point seven treats the soc in the as testable only when evidence and ticket IDs are recorded.

For section seven point seven, Meridian Health Insurance will not accept security work without a written trail.

### Measuring integration

Daniel tracks how often escalations reach the right team first time. Early in the hybrid model, 70% did; after runbook updates, 92% did.

### Worked example

When the managed provider escalates its first night P1 — a burst of failed logins to the claims portal — the runbook directs it to the on-call engineer, who decides no action is needed. The escalation took 11 minutes; the provider's note lacked the source network, so Daniel updates the runbook template.

> **Synthetic case.** Arrangements and events are invented.

### Errors and limits

Integration depends on people; turnover can break paths that look fine on paper.

### Exercises

- **EX031 — Govern link.** How does CSF 2.0 Govern relate to the SOC? *Rubric:* 3 = places SOC within enterprise risk management; 2 = partial; 1 = vague; 0 = none.
- **EX032 — Escalation routes.** List the escalation routes for claims alerts. *Rubric:* 3 = claims ops, IT, legal/DPO, HR only after review; 2 = three; 1 = one; 0 = none.
- **EX033 — Risk language.** How does the SOC report to the risk committee? *Rubric:* 3 = business terms: likelihood, impact, trends, treatments; 2 = partial; 1 = technical; 0 = none.
- **EX034 — First escalation.** What did the first night escalation reveal? *Rubric:* 3 = note lacked source network; template updated; 2 = partial; 1 = nothing; 0 = none.
- **EX035 — Quarterly meetings.** Why meet business leads quarterly? *Rubric:* 3 = relationships make incident calls smoother; 2 = partial; 1 = reporting only; 0 = none.

### Synthesis

Integrate the SOC through service levels, escalation paths, risk reporting and steady relationships.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security operations and blue team: difficult cases

### Learning outcomes

You will (1) handle ambiguous cases where evidence conflicts; (2) manage cases involving staff, partners or regulators; (3) make and revise judgements under pressure; (4) communicate uncertainty to decision-makers.

### 8.1 Ambiguity

Difficult cases are those where evidence points in several directions, stakes are high and time is short. The SOC must decide without certainty and revise as evidence arrives.

Section eight point one develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eight point one, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section eight point one treats ambiguity case one the as testable only when evidence and ticket IDs are recorded.

### 8.2 Case one: the partner

A claims-processing partner reports that one of its staff may have copied Meridian policyholder data. Meridian's logs show the partner account accessed 2,300 records over a weekend, within its contract scope but at an unusual time.

Section eight point two develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eight point two, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section eight point two treats ambiguity case one the as testable only when evidence and ticket IDs are recorded.

### 8.3 Conflicting evidence

The partner says the weekend work was approved overtime; the partner's own SOC suspects misuse. Meridian cannot see the partner's internal systems.

Section eight point three develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eight point three, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section eight point three treats ambiguity case one the as testable only when evidence and ticket IDs are recorded.

For section eight point three, Meridian Health Insurance will not accept security work without a written trail.

### 8.4 Actions

Daniel's team preserves Meridian's logs, suspends the partner account's export rights pending review, informs the DPO and legal, and asks the partner for its evidence under the contract's incident clause.

Section eight point four develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eight point four, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section eight point four treats ambiguity case one the as testable only when evidence and ticket IDs are recorded.

### 8.5 Communicating uncertainty

To the CISO, Daniel writes: "We know the account accessed 2,300 records within scope at unusual hours. We do not yet know whether data was copied. Likelihood of misuse: moderate, based on the partner SOC's concern. Next update: 18:00."

Section eight point five develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eight point five, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section eight point five treats ambiguity case one the as testable only when evidence and ticket IDs are recorded.

### 8.6 Revising

The partner's evidence shows a USB copy of an export. The case becomes a confirmed breach; notification begins.

Section eight point six develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eight point six, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section eight point six treats ambiguity case one the as testable only when evidence and ticket IDs are recorded.

For section eight point six, Meridian Health Insurance will not accept security work without a written trail.

### 8.7 Pressure

Under pressure, teams jump to conclusions or freeze. Written hypotheses and update times keep thinking clear.

Section eight point seven develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eight point seven, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section eight point seven treats ambiguity case one the as testable only when evidence and ticket IDs are recorded.

For section eight point seven, Meridian Health Insurance will not accept security work without a written trail.

### Regulators

When a breach is confirmed, the DPO leads contact with the regulator. The SOC supplies a factual timeline and evidence list, and answers follow-up questions through the DPO so statements stay consistent.

### Worked example

In the review, Daniel notes that suspending export rights early, before certainty, limited further harm with little cost to the partner's legitimate work — consistent with the expected-cost reasoning of chapter 1.

> **Synthetic case.** The case is invented.

### Errors and limits

Cross-organisation evidence is often incomplete; contracts determine what can be obtained.

### Exercises

- **EX036 — Defining difficulty.** What makes a SOC case difficult? *Rubric:* 3 = conflicting evidence, high stakes, short time; 2 = two; 1 = one; 0 = none.
- **EX037 — Initial actions.** List the initial actions in the partner case. *Rubric:* 3 = preserve logs, suspend export rights, inform DPO and legal, request partner evidence; 2 = three; 1 = one; 0 = none.
- **EX038 — Uncertainty message.** What elements did Daniel's message to the CISO contain? *Rubric:* 3 = known facts, unknowns, likelihood with basis, next update time; 2 = three; 1 = one; 0 = none.
- **EX039 — Revision.** What evidence changed the case? *Rubric:* 3 = partner showed USB copy of export; 2 = partial; 1 = none; 0 = none.
- **EX040 — Early suspension.** Why was early suspension justified in hindsight and at the time? *Rubric:* 3 = limited harm at low cost under uncertainty; 2 = partial; 1 = hindsight only; 0 = none.

### Synthesis

Difficult cases demand early proportionate action, clear communication of uncertainty and willingness to revise.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Security operations and blue team: leadership and assurance

### Learning outcomes

You will (1) lead a SOC team through change; (2) provide assurance to executives and auditors with evidence; (3) track performance and coverage over time; (4) build a culture of learning.

### 9.1 Leadership

Leading a SOC means setting direction, protecting analysts from overload, developing people and representing the SOC to the organisation. Knerler, Parker and Zimmerman (2022) stress hiring and growing staff as a core strategy.

Section nine point one develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section nine point one, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section nine point one treats leadership assurance reading the as testable only when evidence and ticket IDs are recorded.

### 9.2 Assurance

Executives and auditors ask: is the SOC working? Assurance answers with evidence: service-level performance, tested detection coverage, exercise results and incident outcomes.

Section nine point two develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section nine point two, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section nine point two treats leadership assurance reading the as testable only when evidence and ticket IDs are recorded.

For section nine point two, Meridian Health Insurance will not accept security work without a written trail.

### Lab — assurance indicators

```python
"""Monthly assurance indicators for the SOC (synthetic)."""
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
p1_met = [17, 18, 15, 19, 20, 21]; p1_total = [20, 20, 19, 21, 21, 22]
tested_cov = [52, 55, 55, 61, 64, 68]   # % priority techniques with tested detections
for m, met, tot, cov in zip(months, p1_met, p1_total, tested_cov):
    print(f"{m} P1 acknowledged within 15 min: {met}/{tot} = {met/tot:.0%}  tested coverage: {cov}%")
```

Run with `python3 lab_assurance.py`. Verified output:

```text
Jan P1 acknowledged within 15 min: 17/20 = 85%  tested coverage: 52%
Feb P1 acknowledged within 15 min: 18/20 = 90%  tested coverage: 55%
Mar P1 acknowledged within 15 min: 15/19 = 79%  tested coverage: 55%
Apr P1 acknowledged within 15 min: 19/21 = 90%  tested coverage: 61%
May P1 acknowledged within 15 min: 20/21 = 95%  tested coverage: 64%
Jun P1 acknowledged within 15 min: 21/22 = 95%  tested coverage: 68%
```

### 9.3 Reading the result

P1 acknowledgement within 15 minutes rose from 85% in January to 95% by June, with a dip to 79% in March. Tested coverage of priority techniques rose steadily from 52% to 68%. The March dip coincided with two analysts leaving; the hybrid night model began in April.

Section nine point three develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section nine point three, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section nine point three treats leadership assurance reading the as testable only when evidence and ticket IDs are recorded.

### 9.4 Honest reporting

Daniel reports the dip and its cause rather than averaging it away. Assurance that hides problems loses credibility when problems appear.

Section nine point four develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section nine point four, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section nine point four treats leadership assurance reading the as testable only when evidence and ticket IDs are recorded.

For section nine point four, Meridian Health Insurance will not accept security work without a written trail.

### 9.5 Culture

Blameless reviews, time for learning and recognition of good escalations build a culture where analysts raise problems early.

Section nine point five develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section nine point five, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section nine point five treats leadership assurance reading the as testable only when evidence and ticket IDs are recorded.

For section nine point five, Meridian Health Insurance will not accept security work without a written trail.

### 9.6 People development

Each analyst has a development plan: training, rotation into detection engineering and mentoring.

Section nine point six develops security operations and blue team with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section nine point six, Prof. Miriam Achebe expects security claims to carry owners and dates.

Section nine point six treats leadership assurance reading the as testable only when evidence and ticket IDs are recorded.

For section nine point six, Meridian Health Insurance will not accept security work without a written trail.

### Managing the provider

Assurance includes the managed night service. Daniel reviews a monthly sample of its escalations and closures with the provider, scoring clarity, correctness and timeliness, and shares the results with the CISO alongside internal indicators.

### Worked example

Daniel's half-year assurance report to the audit committee shows both indicators, explains the March dip, lists three untested priority techniques with plans, and summarises one confirmed breach and its lessons. An auditor asks how coverage is tested; Daniel provides the test records.

> **Synthetic case.** Indicators come from the lab script.

### Errors and limits

Indicators measure what can be counted; some important qualities, such as judgement, need qualitative evidence.

### Exercises

- **EX041 — Assurance evidence.** List four types of assurance evidence. *Rubric:* 3 = service levels, tested coverage, exercises, incident outcomes; 2 = three; 1 = one; 0 = none.
- **EX042 — Lab trends.** Describe both indicator trends. *Rubric:* 3 = P1 85%→95% with March dip 79%; coverage 52%→68%; 2 = partial; 1 = one; 0 = none.
- **EX043 — March dip.** What explained the March dip? *Rubric:* 3 = two analysts left; before hybrid model; 2 = partial; 1 = unknown; 0 = none.
- **EX044 — Honest reporting.** Why report the dip rather than average it away? *Rubric:* 3 = credibility; hidden problems undermine assurance; 2 = partial; 1 = looks better; 0 = none.
- **EX045 — Auditor question.** How did Daniel answer the auditor's coverage question? *Rubric:* 3 = provided test records; 2 = partial; 1 = verbal; 0 = none.

### Synthesis

SOC leadership pairs developing people with evidence-based, honest assurance.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) read SOC research papers critically; (2) assess methods, samples and claims; (3) relate findings to one's own SOC; (4) write a structured critique.

### 10.1 Why read research

Research can test ideas SOCs adopt on faith. Daniel's programme asks students to critique three papers relevant to their work.

Section ten point one develops research reading and critique with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section ten point one, Prof. Miriam Achebe expects research claims to carry owners and dates.

Section ten point one treats why read research paper as testable only when evidence and ticket IDs are recorded.

For section ten point one, Meridian Health Insurance will not accept research work without a written trail.

### 10.2 Paper one

Kokulu et al. (2019) interviewed SOC staff and found mismatches between managers and analysts on issues such as metrics and automation. Strength: rich qualitative data from several SOCs. Limit: interview samples may not represent all SOCs.

Section ten point two develops research reading and critique with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section ten point two, Prof. Miriam Achebe expects research claims to carry owners and dates.

Section ten point two treats why read research paper as testable only when evidence and ticket IDs are recorded.

### 10.3 Paper two

Alahmadi, Axon and Martinovic (2022) surveyed and interviewed SOC practitioners about false positives, finding many are benign triggers. Strength: distinguishes types of false positive. Limit: self-reported perceptions, not measured alert data.

Section ten point three develops research reading and critique with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section ten point three, Prof. Miriam Achebe expects research claims to carry owners and dates.

Section ten point three treats why read research paper as testable only when evidence and ticket IDs are recorded.

### 10.4 Paper three

Hassan et al. (2019) proposed NoDoze, ranking alerts using provenance graphs, and evaluated it on enterprise data. Strength: quantitative evaluation. Limit: requires detailed provenance data many SOCs do not collect.

Section ten point four develops research reading and critique with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section ten point four, Prof. Miriam Achebe expects research claims to carry owners and dates.

Section ten point four treats why read research paper as testable only when evidence and ticket IDs are recorded.

### 10.5 Critique structure

Question, method, sample, findings, validity, relevance to practice and open questions.

Section ten point five develops research reading and critique with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section ten point five, Prof. Miriam Achebe expects research claims to carry owners and dates.

Section ten point five treats why read research paper as testable only when evidence and ticket IDs are recorded.

For section ten point five, Meridian Health Insurance will not accept research work without a written trail.

### 10.6 Relating to Meridian

Kokulu's mismatch finding prompts Daniel to survey his own analysts about metrics; Alahmadi's distinction informs how Meridian labels closed alerts.

Section ten point six develops research reading and critique with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section ten point six, Prof. Miriam Achebe expects research claims to carry owners and dates.

Section ten point six treats why read research paper as testable only when evidence and ticket IDs are recorded.

For section ten point six, Meridian Health Insurance will not accept research work without a written trail.

### 10.7 Avoiding cherry-picking

Daniel searches for studies disagreeing with each paper's conclusions and notes them.

Section ten point seven develops research reading and critique with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section ten point seven, Prof. Miriam Achebe expects research claims to carry owners and dates.

Section ten point seven treats why read research paper as testable only when evidence and ticket IDs are recorded.

For section ten point seven, Meridian Health Insurance will not accept research work without a written trail.

### Reading groups

Daniel starts a monthly reading group where analysts present one paper and its relevance. Reading together spreads critical habits beyond the leader and often surfaces practical objections that a single reader would miss, such as data the SOC does not actually collect.

### Worked example

Daniel's critique of the Alahmadi paper concludes: "The benign-trigger distinction is directly useful; we will add 'benign trigger' as a closure code separate from 'false positive'. Because results are perceptions, we will measure our own closure data before changing rules."

> **Synthetic case.** Meridian's actions are invented; the paper summaries describe the cited works.

### Errors and limits

Critiques by practitioners may overweight relevance and underweight rigour; balance both.

### Exercises

- **EX046 — Kokulu finding.** Summarise Kokulu et al.'s main finding and one limit. *Rubric:* 3 = manager-analyst mismatches; interview sample representativeness; 2 = partial; 1 = one; 0 = none.
- **EX047 — Alahmadi limit.** What is the main limit of Alahmadi et al.? *Rubric:* 3 = self-reported perceptions, not measured alerts; 2 = partial; 1 = none; 0 = none.
- **EX048 — NoDoze limit.** Why might NoDoze be hard to adopt? *Rubric:* 3 = needs detailed provenance data; 2 = partial; 1 = cost; 0 = none.
- **EX049 — Critique structure.** List the critique structure elements. *Rubric:* 3 = question, method, sample, findings, validity, relevance, open questions; 2 = five; 1 = two; 0 = none.
- **EX050 — Action taken.** What action followed the Alahmadi critique? *Rubric:* 3 = add benign-trigger closure code; measure own data first; 2 = partial; 1 = none; 0 = none.

### Synthesis

Critical reading tests ideas before adoption and links research findings to measured local practice.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) plan and execute an applied SOC improvement project; (2) measure baseline and outcome; (3) manage stakeholders and risks; (4) report results for decision-makers.

### 11.1 The project

Daniel's applied project reduces time to contain compromised contractor accounts, the weakness exposed in chapter 1.

Section eleven point one develops applied project with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eleven point one, Prof. Miriam Achebe expects applied claims to carry owners and dates.

Section eleven point one treats the project baseline interventions as testable only when evidence and ticket IDs are recorded.

For section eleven point one, Meridian Health Insurance will not accept applied work without a written trail.

### 11.2 Baseline

Over the previous six months, four contractor compromises took a median of 3.5 hours from first alert to containment, mostly waiting for contractor managers to confirm activity.

Section eleven point two develops applied project with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eleven point two, Prof. Miriam Achebe expects applied claims to carry owners and dates.

Section eleven point two treats the project baseline interventions as testable only when evidence and ticket IDs are recorded.

For section eleven point two, Meridian Health Insurance will not accept applied work without a written trail.

### 11.3 Interventions

A contractor directory with 24/7 contacts; an automated step that sends the contractor's manager a confirmation request; and a rule allowing analysts to suspend contractor export rights immediately for high-severity alerts, with review within four hours.

Section eleven point three develops applied project with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eleven point three, Prof. Miriam Achebe expects applied claims to carry owners and dates.

Section eleven point three treats the project baseline interventions as testable only when evidence and ticket IDs are recorded.

### 11.4 Stakeholders

Procurement (contracts must require 24/7 contacts), contractor managers, IT and legal. Procurement adds a clause to new contracts.

Section eleven point four develops applied project with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eleven point four, Prof. Miriam Achebe expects applied claims to carry owners and dates.

Section eleven point four treats the project baseline interventions as testable only when evidence and ticket IDs are recorded.

For section eleven point four, Meridian Health Insurance will not accept applied work without a written trail.

### 11.5 Risks

Wrongful suspension disrupts contractor work; mitigated by fast review and limiting suspension to export rights, not all access.

Section eleven point five develops applied project with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eleven point five, Prof. Miriam Achebe expects applied claims to carry owners and dates.

Section eleven point five treats the project baseline interventions as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Meridian Health Insurance will not accept applied work without a written trail.

### 11.6 Measurement

Time to contain for contractor compromises and test scenarios; count of wrongful suspensions.

Section eleven point six develops applied project with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eleven point six, Prof. Miriam Achebe expects applied claims to carry owners and dates.

Section eleven point six treats the project baseline interventions as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Meridian Health Insurance will not accept applied work without a written trail.

### 11.7 Result

Over the next four months, two real compromises and six test scenarios were contained in a median of 22 minutes. One wrongful suspension lasted 40 minutes before review restored access.

Section eleven point seven develops applied project with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section eleven point seven, Prof. Miriam Achebe expects applied claims to carry owners and dates.

Section eleven point seven treats the project baseline interventions as testable only when evidence and ticket IDs are recorded.

For section eleven point seven, Meridian Health Insurance will not accept applied work without a written trail.

### Project governance

The project has a sponsor (the CISO), a fortnightly check-in and a simple risk log. When procurement's legal review delayed the contract clause by three weeks, the log made the slip visible early and Daniel adjusted the plan to start with existing contracts' contacts instead of waiting.

### Ethics of testing

Test scenarios used dedicated test contractor accounts, approved in writing by the CISO, so no real contractor was suspended for a test.

### Worked example

Daniel's project report to the CISO: baseline 3.5 hours; outcome 22 minutes median (small sample); one wrongful suspension, reviewed promptly; recommendation to keep the process and extend the 24/7 contact clause to renewing contracts.

> **Synthetic case.** The project is invented.

### Errors and limits

Two real cases and six tests are few; the effect estimate is uncertain.

### Exercises

- **EX051 — Baseline cause.** What caused the 3.5-hour baseline? *Rubric:* 3 = waiting for contractor managers to confirm activity; 2 = partial; 1 = unknown; 0 = none.
- **EX052 — Interventions.** List the three interventions. *Rubric:* 3 = 24/7 directory, automated confirmation request, immediate export suspension with review; 2 = two; 1 = one; 0 = none.
- **EX053 — Risk mitigation.** How was wrongful suspension risk limited? *Rubric:* 3 = fast review; suspend export rights only; 2 = partial; 1 = none; 0 = none.
- **EX054 — Outcome.** Report the outcome measures. *Rubric:* 3 = median 22 min over 2 real + 6 tests; 1 wrongful suspension 40 min; 2 = partial; 1 = one; 0 = none.
- **EX055 — Procurement role.** What did procurement change? *Rubric:* 3 = added 24/7 contact clause to contracts; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Applied projects improve SOCs when baselines, interventions, risks and outcomes are measured and reported plainly.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) review learning and outcomes across the programme; (2) transfer methods to other SOC problems; (3) plan continued professional development; (4) hand over improvements sustainably.

### 12.1 Looking back

The programme took Daniel from explicit decision-making (chapter 1) through specialist evidence, ethics, design, evaluation, integration, difficult cases, assurance and research to an applied project.

Section twelve point one develops final review and transfer with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section twelve point one, Prof. Miriam Achebe expects final claims to carry owners and dates.

Section twelve point one treats looking back transferable methods as testable only when evidence and ticket IDs are recorded.

For section twelve point one, Meridian Health Insurance will not accept final work without a written trail.

### 12.2 Transferable methods

Expected-cost reasoning, peer baselines, controlled evaluation with robust statistics, structured critique and honest assurance apply beyond claims and contractors.

Section twelve point two develops final review and transfer with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section twelve point two, Prof. Miriam Achebe expects final claims to carry owners and dates.

Section twelve point two treats looking back transferable methods as testable only when evidence and ticket IDs are recorded.

For section twelve point two, Meridian Health Insurance will not accept final work without a written trail.

### 12.3 Transfer example

Daniel applies controlled evaluation to the managed provider's escalation quality, comparing escalations before and after a template change.

Section twelve point three develops final review and transfer with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section twelve point three, Prof. Miriam Achebe expects final claims to carry owners and dates.

Section twelve point three treats looking back transferable methods as testable only when evidence and ticket IDs are recorded.

For section twelve point three, Meridian Health Insurance will not accept final work without a written trail.

### 12.4 Sustainability

Improvements must survive staff changes: playbooks documented, owners named, metrics automated and reviews scheduled.

Section twelve point four develops final review and transfer with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section twelve point four, Prof. Miriam Achebe expects final claims to carry owners and dates.

Section twelve point four treats looking back transferable methods as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Meridian Health Insurance will not accept final work without a written trail.

### 12.5 Final review

The programme's final review is a viva with Prof. Achebe and an external SOC leader. Questions probe judgement: "When would you not use expected cost?" "How would you know insider monitoring had become unfair?"

Section twelve point five develops final review and transfer with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section twelve point five, Prof. Miriam Achebe expects final claims to carry owners and dates.

Section twelve point five treats looking back transferable methods as testable only when evidence and ticket IDs are recorded.

### 12.6 Answers

On fairness, Daniel cites indicators: rising flags concentrated in one team or role without business explanation, or complaints through staff representatives. Such signs trigger a policy review.

Section twelve point six develops final review and transfer with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section twelve point six, Prof. Miriam Achebe expects final claims to carry owners and dates.

Section twelve point six treats looking back transferable methods as testable only when evidence and ticket IDs are recorded.

### 12.7 Development

Daniel plans to mentor a senior analyst into team leadership and to present the contractor project at the sector forum.

Section twelve point seven develops final review and transfer with a Meridian Health Insurance note Daniel Okoro can demo offline.

Under section twelve point seven, Prof. Miriam Achebe expects final claims to carry owners and dates.

Section twelve point seven treats looking back transferable methods as testable only when evidence and ticket IDs are recorded.

For section twelve point seven, Meridian Health Insurance will not accept final work without a written trail.

### Feedback from the team

Daniel asks his analysts what changed for them during the programme. They name fewer night calls, clearer playbooks and the new closure codes; they also say the pace of change was tiring. He plans a quieter quarter focused on consolidation before the next initiative, and records this in his development plan.

### Worked example

The external examiner asks what Daniel would do differently. He answers: "Measure baselines before the first incident forces it; I had to reconstruct the contractor baseline from tickets, which was slow and imprecise."

> **Synthetic case.** The review is invented.

### Errors and limits

Reflection is partial; colleagues' feedback adds views one cannot see alone.

### Exercises

- **EX056 — Transferable methods.** List four transferable methods from the programme. *Rubric:* 3 = expected cost, peer baselines, controlled evaluation, critique, assurance (four); 2 = three; 1 = one; 0 = none.
- **EX057 — Transfer example.** Where did Daniel transfer controlled evaluation? *Rubric:* 3 = provider escalation quality before/after template change; 2 = partial; 1 = none; 0 = none.
- **EX058 — Sustainability.** What makes improvements survive staff changes? *Rubric:* 3 = documented playbooks, owners, automated metrics, scheduled reviews; 2 = three; 1 = one; 0 = none.
- **EX059 — Fairness signals.** How would Daniel know insider monitoring had become unfair? *Rubric:* 3 = flags concentrated without business reason; complaints via representatives; 2 = partial; 1 = none; 0 = none.
- **EX060 — Differently.** What would Daniel do differently? *Rubric:* 3 = measure baselines before incidents force it; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Postgraduate practice ends by transferring methods, sustaining improvements and continuing to learn.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Daniel Okoro, Prof. Miriam Achebe, Meridian Health Insurance, Hollins College and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The probability of malice times the cost if malicious, plus the probability of benign times the cost if benign.

**EX002.** Contain now 11.6k, monitor 42.4k, close 180.0k.

**EX003.** Monitoring becomes cheapest, showing that the right action depends on belief, so fast evidence is valuable.

**EX004.** Some harms, such as human impact of health-data disclosure, are hard to price, and legal duties are not open to trade-off.

**EX005.** The decision, the probability estimate, the evidence used, who decided and when.

**EX006.** Mission, authority, staffing and measurement (others include structure, response, intelligence, data, tools, communication and expansion).

**EX007.** A move from buying vendor content to engineering, testing and versioning detections in shared formats.

**EX008.** Losing local context, which must be offset by clear escalation, data access and quality terms.

**EX009.** Tooling was strong but service definitions were weak.

**EX010.** Monitoring, investigation, insider-risk support, detection engineering and incident coordination, each with scope and service levels.

**EX011.** Peers do similar work, and the median is not pulled by one unusual person.

**EX012.** h04, with 1,260 views against a median of 410, a ratio of 3.07.

**EX013.** It raises a question for review; it is not an accusation.

**EX014.** HR, legal and staff representatives, together with the SOC.

**EX015.** h04 had been assigned 900 legacy claims for a migration; the flag was closed and assignment data added as enrichment.

**EX016.** Consequences (least harm), duties (obligations regardless of outcome) and fairness (who bears burdens).

**EX017.** He treated it as unacceptable under legal duties and honesty and escalated to the CISO and data protection officer.

**EX018.** It erodes employee trust, and people who distrust the SOC report less.

**EX019.** Written purpose for monitoring, minimum reviewer access and audit of SOC searches.

**EX020.** Because device and session checks could meet the same purpose less intrusively.

**EX021.** A: hire for in-house 24/7; B: managed service at night; C: managed night tier-1 with in-house escalation and automated containment for high-confidence alerts.

**EX022.** Detection quality, response speed, cost, local knowledge, data control and resilience.

**EX023.** C remained best unless the cost weight was doubled, when B narrowly won.

**EX024.** Poor escalation by the provider, mitigated by quality reviews and targets; wrongful automated containment, mitigated by limits.

**EX025.** Night P1 alerts acknowledged within 15 minutes, escalation precision above 50% and no wrongful automated containment of critical accounts.

**EX026.** Alternately by alert number, so busy and quiet periods appeared in both groups.

**EX027.** Old 24.5, new 17.5 minutes; difference 7.0; 95% interval 3.5–11.0.

**EX028.** Triage times are skewed, and the bootstrap gives an interval without assuming a distribution.

**EX029.** No; the senior review found one wrong decision in each group.

**EX030.** Analysts knew which playbook they used and may have worked harder with the new one.

**EX031.** It places the SOC's work inside enterprise risk management and governance.

**EX032.** Claims operations for context, IT for account actions, legal and the DPO for possible breaches, and HR only when review suggests misconduct.

**EX033.** In business terms: likelihood and impact of disclosure, trends and treatment actions.

**EX034.** The provider's note lacked the source network, so the runbook template was updated.

**EX035.** Regular contact builds relationships that make urgent incident calls quicker and easier.

**EX036.** Evidence that points in different directions, high stakes and little time.

**EX037.** Preserve logs, suspend the partner account's export rights, inform the DPO and legal, and request the partner's evidence.

**EX038.** What is known, what is not, a likelihood with its basis, and the next update time.

**EX039.** The partner's evidence of a USB copy of an export.

**EX040.** At the time, it limited possible harm at little cost to legitimate work; the outcome confirmed the reasoning.

**EX041.** Service-level performance, tested detection coverage, exercise results and incident outcomes.

**EX042.** P1 acknowledgement rose from 85% to 95% with a March dip to 79%; tested coverage rose from 52% to 68%.

**EX043.** Two analysts had left, before the hybrid night model started in April.

**EX044.** Because assurance that hides problems loses credibility when they surface.

**EX045.** By providing the records of detection tests.

**EX046.** SOC managers and analysts disagree on issues like metrics and automation; interview samples may not represent all SOCs.

**EX047.** It relies on practitioners' perceptions rather than measured alert data.

**EX048.** It depends on detailed provenance data many SOCs do not collect.

**EX049.** Question, method, sample, findings, validity, relevance to practice and open questions.

**EX050.** Add a separate "benign trigger" closure code and measure Meridian's own closure data before changing rules.

**EX051.** Mostly waiting for contractor managers to confirm whether activity was legitimate.

**EX052.** A 24/7 contractor contact directory, an automated confirmation request to the manager, and immediate suspension of export rights with review within four hours.

**EX053.** By reviewing within four hours and suspending only export rights, not all access.

**EX054.** A median of 22 minutes to contain across two real cases and six tests, with one wrongful suspension lasting 40 minutes.

**EX055.** It added a clause requiring 24/7 contacts in new contracts.

**EX056.** Expected-cost decisions, peer baselines, controlled evaluation with robust statistics and structured critique.

**EX057.** To the managed provider's escalation quality, before and after a template change.

**EX058.** Documented playbooks, named owners, automated metrics and scheduled reviews.

**EX059.** If flags concentrated in a team or role without business explanation, or staff representatives raised complaints.

**EX060.** Measure baselines in advance rather than reconstructing them after an incident.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and telemetry in this book are synthetic unless a sentence cites a public source.


- Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. *31st USENIX Security Symposium*, 2783–2800. <https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi>
- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations* (NIST SP 800-137). <https://doi.org/10.6028/NIST.SP.800-137>
- Hassan, W. U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., & Bates, A. (2019). NoDoze: Combatting threat alert fatigue with automated provenance triage. *NDSS Symposium*. <https://doi.org/10.14722/ndss.2019.23349>
- Kaloroumakis, P. E., & Smith, M. J. (2021). *Toward a Knowledge Graph of Cybersecurity Countermeasures* (MITRE D3FEND). The MITRE Corporation. <https://d3fend.mitre.org/resources/D3FEND.pdf>
- Kent, K., & Souppaya, M. (2006). *Guide to Computer Security Log Management* (NIST SP 800-92). <https://doi.org/10.6028/NIST.SP.800-92>
- Knerler, K., Parker, I., & Zimmerman, C. (2022). *11 Strategies of a World-Class Cybersecurity Operations Center* (2nd ed.). The MITRE Corporation. <https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center>
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., & Ahn, G.-J. (2019). Matched and mismatched SOCs: A qualitative study on security operations center issues. *ACM CCS 2019*, 1955–1970. <https://doi.org/10.1145/3319535.3354239>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (NIST SP 800-61 Rev. 3). <https://doi.org/10.6028/NIST.SP.800-61r3>
- SigmaHQ. *Sigma: Generic signature format for SIEM systems* (rule specification and repository). <https://github.com/SigmaHQ/sigma>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018, rev. 2020). *MITRE ATT&CK: Design and Philosophy* (MP180360R1). The MITRE Corporation. <https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf>
- Sundaramurthy, S. C., Case, J., Truong, T., Zomlot, L., & Hoffmann, M. (2014). A tale of three security operation centers. *ACM Workshop on Security Information Workers (SIW '14)*, 43–50. <https://doi.org/10.1145/2663887.2663904>
- van Os, R. (2016). *SOC-CMM: Designing and Evaluating a Tool for Measurement of Capability Maturity in Security Operations Centers* (Master's thesis). Luleå University of Technology. <https://ltu.diva-portal.org/smash/get/diva2:1031560/FULLTEXT02>
- Vielberth, M., Böhm, F., Fichtinger, I., & Pernul, G. (2020). Security operations center: A systematic study and open challenges. *IEEE Access*, 8, 227756–227779. <https://doi.org/10.1109/ACCESS.2020.3045514>
- Zimmerman, C. (2014). *Ten Strategies of a World-Class Cybersecurity Operations Center*. The MITRE Corporation. ISBN 978-0-692-24310-7. <https://www.mitre.org/sites/default/files/publications/pr-13-1028-mitre-10-strategies-cyber-ops-center.pdf>
