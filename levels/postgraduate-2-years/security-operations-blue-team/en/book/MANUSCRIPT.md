# Security Operations and Blue Team: Postgraduate Course

- Language: English (`en`); course 153, Postgraduate course (2 years).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
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

**Daniel Okoro** leads the SOC of the fictional **Meridian Health Insurance** and studies on a postgraduate programme at the fictional **Hollins College**, tutored by **Prof. Miriam Achebe**. Every night his analysts decide whether to contain, monitor or close alerts without knowing for certain what is happening. Postgraduate practice makes those decisions explicit. The contractor-account alert that opens this book is the first such decision: at 23:40, with a 30% belief that the export was malicious, the night team had to choose between stopping a legitimate batch job and risking a large disclosure of health data. Daniel's programme asks him to write down how that choice was made.

### 1.2 The case

At 23:40 an alert reports a contractor account exporting claims records from an unusual address. Analysts estimate a 30% chance it is malicious. Disabling the account would stop a contractor's legitimate batch job; waiting risks a large disclosure of health data. The analysts' 30% estimate came from what they could see at that moment: the address was unusual, but the account belonged to a contractor that did run batch exports. Nobody could reach the contractor at that hour, which is why the decision had to be made on partial evidence rather than after a phone call.

### 1.3 Expected cost

Each option has a cost if the activity is malicious and a cost if benign. Multiplying by probabilities and summing gives an expected cost. It does not predict what will happen; it shows which option is least costly on average given current beliefs. For the contractor alert, the costs differ sharply by option. Containing a benign job costs a delayed batch and an apology; closing a malicious export costs a disclosure of health records. The lab sets each cost from Meridian's own estimates, so the calculation shows how the team's beliefs and values combine, not an objective price of harm.

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

At a 30% chance of malice, containing now has an expected cost of 11.6k, against 42.4k for monitoring and 180k for closing. At 5%, monitoring becomes cheaper. The best choice depends on the probability, so better evidence is worth gathering quickly. This is why Daniel's analysts kept investigating after containing at 23:52. If evidence had lowered the probability well below 30%, monitoring would have become the cheaper option and the account could have been restored. The contractor's report the next morning ended the uncertainty, but the decision was made, and is judged, on the 30% known at the time.

### 1.5 Beyond numbers

Costs of health-data disclosure include regulatory, contractual and human harm that is hard to price. Decisions also respect legal duties that are not trade-offs. Expected cost informs judgement; it does not replace it. In the contractor case, a disclosure would have harmed policyholders whose health data was exposed, in ways a figure of 180k cannot capture, and Meridian's duty to protect that data does not depend on the arithmetic. Daniel uses the numbers to check that the choice was reasonable, then asks whether any duty points the other way.

### 1.6 Recording decisions

The on-call manager logs the decision, the probability estimate, the evidence and who decided. Reviewers can later judge the decision on what was known, not on hindsight. For the contractor incident, the record shows containment at 23:52, the 30% estimate, the unusual address as evidence and the on-call manager as decider. When the contractor later confirmed phished credentials, nobody claimed the analysts had known; the record showed they acted on cost, which protects good decisions that might have turned out differently. Reviews of cases that turned out benign use the same record format, so a correct decision to escalate is judged on what was known at the time.

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

Current SOCs combine SIEM or data platforms, endpoint detection, identity analytics, case management and automation. Many use managed services for some hours or functions. Knerler, Parker and Zimmerman (2022) describe eleven strategies covering mission, authority, structure, staffing, response, intelligence, data, tools, communication, measurement and expansion. Meridian's SOC uses most of these components but staffs only daytime hours, which the contractor incident exposed. The eleven strategies give Daniel a checklist for comparing Meridian with others in the sector, and later for choosing among night-coverage options.

### 2.2 Detection engineering

Detections are increasingly managed as code in shared formats such as Sigma, mapped to MITRE ATT&CK and tested before release. This shifts SOCs from buying content to engineering it. At Meridian, the claims-export rule that fired on the contractor account is now kept in version control with a Sigma description and a mapping to ATT&CK, and every change is tested on stored alerts before release. That practice lets Daniel show the board which techniques his team covers and which it does not, and it is what makes tested coverage measurable later. Rules bought from vendors are reviewed in the same way before they are switched on.

### 2.3 Alert overload

Studies continue to report alert fatigue and benign triggers (Alahmadi et al., 2022). Automation and better context are common responses, with mixed results. Meridian's own alert queue shows the pattern: many claims-access flags turn out to be benign triggers caused by project work, like the handler assigned 900 legacy claims. Daniel's response combines better context, such as assignment data as enrichment, with automation only where the decision is simple. His later critique of the Alahmadi paper led him to separate benign triggers from false positives in closure codes, so the two can be counted apart.

### 2.4 Managed detection and response

Outsourcing night or tier-1 work gives coverage but risks losing local knowledge. Contracts need clear escalation, data access and quality measures. For Meridian, this risk shaped the choice of a hybrid night model rather than full outsourcing. The managed provider handles tier-1 triage, while escalation goes to Meridian's own on-call engineers who know the claims system and the contractors. The contract names escalation targets, data access and quality reviews, and the first night P1 tested the runbook. Gaps in the provider's escalation notes were fixed in the runbook template rather than left to goodwill.

### 2.5 Maturity assessment

The SOC-CMM (van Os, 2016) lets SOCs self-assess across business, people, process, technology and services. Meridian's last assessment showed strong tooling but weak service definitions. The weak service definitions found by the assessment led directly to Daniel's service catalogue, which lists what the SOC provides to each business unit with scope and service levels. Meridian's next assessment will show whether the catalogue closed that gap. Using the same model each time keeps the comparison fair across years and gives the board a familiar format for progress. Daniel files the assessment evidence so the next assessor can check it.

### 2.6 Regulation

Health insurers face data protection and sector regulation; incident reporting timelines shape SOC procedures. For Meridian, the contractor export was a possible disclosure of health data, so legal and the data protection officer had to be informed quickly and the time of awareness recorded. Procedures name who decides whether a case is notifiable and how the SOC supports that decision with facts. The partner breach later in the book followed the same path, and the business request to delay notification was refused because these duties do not bend to a product launch.

### 2.7 Comparing with peers

Daniel joins a sector forum where SOC leads share anonymised practices and metrics. The forum's comparisons are anonymised, so Daniel learns from patterns rather than from named companies. It was through the forum that he noticed two peers had service catalogues while Meridian did not, which became one of his first improvements. He shares Meridian's own figures on the same basis, after checking with the CISO what may be disclosed. The forum also gives him peers to ask when a decision has no clear precedent at Meridian.

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

Some SOC questions need evidence beyond network and endpoint logs: application access logs, HR role data and business workload. At Meridian, claims-system logs record each record a handler opens. These sources answer questions that endpoint telemetry cannot, such as whether a handler's access matched assigned work. Using them needs agreement from the system owners and HR, and a clear purpose recorded before analysis begins. At Meridian, access to claims logs for monitoring was agreed with the claims system owner, HR and staff representatives, with the purpose written into the insider-risk policy before any baseline was computed.

### 3.2 Insider risk

Insurers worry about staff viewing records without business need, for curiosity or fraud. Monitoring such access must be fair: people are compared with peers doing similar work, not with the whole company. At Meridian, claims handlers in different teams have very different workloads, so a company-wide threshold would flag busy teams and miss unusual individuals in quiet ones. Peer comparison makes the baseline fair to each team, and the fairness policy decides who may see a flag and when. At Meridian, each peer group is one claims team.

### 3.3 Peer baselines

A peer-group median is robust to one unusual person. Comparing each handler's weekly views with their team's median highlights unusual workloads. Meridian's lab computes a weekly median of record views for each team and divides each handler's views by it, so a ratio near 1 means typical workload. A ratio well above that is a flag for review. Because the median ignores a single extreme value, the person being flagged cannot raise their own team's baseline enough to hide, and a quiet week for one colleague does not make everyone else look busy.

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

In team A, h04 viewed 1,260 records against a peer median of 410 — a ratio of 3.07, flagged for review. All other handlers in both teams are within 0.92–1.05 of their medians. Team B's lower volumes do not distort team A's comparison because each team has its own baseline. The result is a single flag, not a finding about h04's conduct. The review then looks for a business reason, which in this case was the assignment of 900 legacy claims for a migration project.

### 3.5 Interpreting outliers

A flag is a question, not an accusation. High volume may reflect assignment to a backlog, a special project or a data-quality task. At Meridian, h04's flag turned out to be a migration project, and the assignment table showed every viewed record was assigned. The reviewer recorded that explanation and closed the flag without telling h04's manager, as the fairness policy requires. Adding assignment data as enrichment means similar project work will be explained before a reviewer ever sees it.

### 3.6 Fairness and privacy

Insider-risk monitoring is governed by policy agreed with HR, legal and staff representatives. Reviews are done by a small, trained group; managers are not told of flags unless review finds a concern. In h04's case, the review group checked the assignment table and closed the flag; the manager was never told. Audit of the reviewers' own searches shows that the access granted for monitoring is used only for it. Staff representatives receive annual figures on flags and outcomes, which lets them check that monitoring falls fairly across teams.

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

SOC decisions are risk decisions with ethical content: monitoring staff, sharing data with partners and choosing whom to notify after a breach. At Meridian these choices are concrete: whether to monitor claims handlers' record access, what to share with a partner during an investigation, and when to notify policyholders after the partner breach. Each affects people who are not in the room when the decision is made, so the SOC records how their interests were weighed. Daniel's programme treats these as part of SOC work, not as matters for legal alone.

### 4.2 Ethical lenses

Consequences ask which choice produces the least harm. Duties ask what obligations apply regardless of outcome, such as honesty to affected people. Fairness asks whether burdens fall equally. Using several lenses reveals considerations one would miss. For the keystroke-timing proposal, the consequence lens asked whether it would reduce account sharing; the duty lens asked whether staff had been told; the fairness lens asked whether claims staff alone would bear an intrusive measure. Together they supported the ethics review's rejection in favour of device and session checks, which meet the same purpose with less intrusion.

### 4.3 Business pressure

After the contractor incident, a business manager asks the SOC to delay notifying affected policyholders until after a product launch. Legal duties and honesty make that unacceptable; Daniel escalates to the CISO and the data protection officer. Daniel's escalation is recorded with the request, the reason it was refused and who was informed. The CISO and the data protection officer then decide the notification timing on legal grounds, and the business manager is told why. The record protects the SOC if the request is later disputed, and shows that a delay requested for commercial reasons was not left to the SOC to grant or refuse alone.

### 4.4 Employee trust

Heavy-handed monitoring can damage trust and reporting. Transparent policies, proportionate monitoring and fair review keep trust. Meridian's insider-risk policy was written with staff representatives, which made it easier for claims handlers to accept peer comparison. If staff believed every view was watched by managers, they might stop reporting suspicious requests, which is one of the SOC's best sources of insider-risk leads. Trust is therefore part of detection, not just a matter of goodwill. Annual figures on flags shared with staff representatives support that trust.

### 4.5 Safeguards

Meridian's safeguards: written purpose for each monitoring use, minimum access for reviewers, audit of SOC searches, and an ethics review for new monitoring of people. These safeguards were tested when the keystroke-timing monitor was proposed: the written purpose, account sharing, was examined by the ethics review and found to be achievable by less intrusive means. Audit of SOC searches also means that if an analyst browsed records out of curiosity, the SOC's own monitoring would show it. Each safeguard has a named owner at Meridian and is reviewed yearly with the ethics review that rejected the keystroke-timing monitor.

### 4.6 Third parties

Contractors and partners have access too; contracts set their security obligations and the SOC's rights to monitor and investigate. The partner case later in the book depended on this: the contract's incident clause gave Meridian the right to ask for the partner's evidence, while Meridian could not see the partner's internal systems itself. Contractor contracts now also require 24/7 contacts, a change that came from the contractor-account incident. Daniel checks each new contract's security clauses with procurement before signing. The partner breach relied on both clauses at once.

### 4.7 Accountability

Decisions with ethical weight are recorded with the reasoning, so they can be examined later. Daniel's records of the keystroke-timing rejection and the refused notification delay both state the decision, the lenses applied, the people consulted and the alternative chosen. If a regulator or an employee later questions either decision, the record shows that it was reasoned, not improvised, and who was accountable for it. The same record format is used for decisions to monitor and for decisions not to.

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

Meridian's SOC is staffed 07:00–19:00; nights rely on on-call engineers. The contractor incident at 23:40 was caught only because the on-call engineer was awake. The board asks for 24/7 coverage options. The question therefore is not whether to cover nights but how. Daniel frames it as a choice among options, each scored against criteria agreed with the CISO, so the board can see why one is recommended and what it would cost. He sets the decision and its success measures down before scoring, so that the criteria cannot be adjusted after the preferred option is known.

### 5.2 Alternatives

Option A: hire for in-house 24/7 (five more analysts). Option B: managed detection and response for nights. Option C: hybrid — managed tier-1 at night with in-house escalation and an automated containment playbook for high-confidence alerts. Each option answers the contractor incident differently. A gives Meridian analysts at 23:40 every night; B gives a provider who may not know which contractors run batch jobs; C gives a provider for first triage, Meridian's own engineers for decisions, and automation that can act within seconds on alerts above a confidence threshold. The automated playbook is limited to suspending export rights, not whole accounts.

### 5.3 Criteria

Detection quality, response speed, cost, local knowledge, data control and resilience. Each is weighted with the CISO. Weighting with the CISO makes the trade-offs explicit. Data control matters more at a health insurer than at many firms, because policyholder records must stay within agreed processing; local knowledge matters because many alerts depend on knowing which contractors work which hours. Daniel records the agreed weights in the board paper before any option is scored, so nobody can say the weights were chosen to favour a result.

### 5.4 Scoring

A scores high on knowledge and control but high cost and hiring risk; B is cheapest but weakest on knowledge; C balances them. Each score has a written reason in the board paper: A's hiring risk comes from the difficulty of recruiting five analysts for nights, and B's weakness on knowledge comes from the provider not knowing Meridian's contractors and claims system. The reasons let the board challenge a score instead of the whole recommendation. A balanced score for C reflects that its weaknesses can be managed with quality reviews and automation limits.

### 5.5 Sensitivity

Daniel checks whether the recommendation changes if weights shift. C stays best unless cost weight is doubled, when B wins narrowly. The recommendation is therefore robust to reasonable disagreement. The sensitivity check answers the board's obvious question: what if you weighted cost differently? Showing that C survives most plausible changes, and naming the one change under which B wins, makes the recommendation honest about where it is fragile. If the board cares mostly about cost, it can choose B knowing the trade-off it is accepting in local knowledge and escalation quality.

### 5.6 Risks of C

Managed analysts may escalate too much or too little; automation could wrongly disable accounts. Mitigations: quality reviews, escalation targets, automation limits. Daniel's success measures for C turn these risks into numbers the board can check after six months: escalation precision above 50%, and no wrongful automated containments of critical accounts. The automation is limited to suspending export rights, not disabling accounts, so a wrong trigger disrupts less. Quality reviews sample the provider's closed alerts each month. The board paper names an owner for each mitigation, such as the quality reviews of the provider's closed alerts.

### 5.7 Presenting

The board paper shows options, scores, sensitivity and risks on two pages. Two pages force Daniel to choose what matters: the board sees each option's score, how the recommendation holds when weights change, and the risks of C with mitigations. Supporting detail, such as the scoring reasons, sits in an appendix for members who want it. The board chose C with a six-month review, and the paper's success measures became the review's criteria. The appendix also lists the scoring reasons and the sensitivity table.

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

Daniel's team writes a new triage playbook for claims-export alerts that starts with three automated enrichment lookups — assignment data, contractor status and export destination — before analyst review. The three lookups answer the questions analysts ask most often on claims-export alerts: whether the records were assigned, whether the contractor is still active, and whether the export went to an expected destination. Putting the answers in front of the analyst before review is meant to shorten triage without changing who decides. The evaluation then tests whether triage actually shortened for claims-export alerts, without changing who made the decision.

### 6.2 Evaluation design

For four weeks, alerts are assigned alternately to the old and new playbook by alert number, so busy and quiet periods fall into both groups. Analysts rotate between playbooks. Sixteen alerts fall in each group. Assigning by alert number removes the team's choice of which alerts get the new playbook, which could otherwise favour easy alerts. Rotation spreads analyst skill across both groups. The design was written before the first alert was assigned, and the sample of 32 alerts was fixed by the four-week window rather than chosen after looking at results.

### 6.3 Measure

Triage time in minutes from pickup to decision, plus decision accuracy checked by a senior analyst. Triage time is taken from case-system fields, so it does not depend on analysts' memory. The senior analyst checking accuracy reviews each decision against the evidence without knowing in advance which playbook was used, as far as the case notes allow. Measuring accuracy beside speed guards against a playbook that is faster only because it skips checks, which would show up as more wrong decisions in that group.

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

The median triage time fell from 24.5 to 17.5 minutes, a difference of 7.0. The bootstrap 95% interval for the difference is 3.5 to 11.0 minutes, which excludes zero. Medians suit skewed times; bootstrapping gives an interval without assuming a distribution. With only 16 alerts per group, the interval is wide: the true saving could be as small as 3.5 minutes or as large as 11. Daniel reports the interval with the point estimate so that the board does not read 7.0 minutes as a precise figure. The three-month recheck adds alerts and should narrow it.

### 6.5 Accuracy

The senior analyst found one wrong decision in each group, so faster triage did not cost accuracy in this sample. One error per group in 16 alerts is too few to show that accuracy is equal; it shows only that the sample gives no sign of a loss. Daniel's report therefore says equal accuracy in this sample and plans to recheck error rates after three months of routine use, when more alerts will have been handled under the new playbook and novelty will have worn off.

### 6.6 Confounding

Alternating assignment protects against time-of-day effects; rotation protects against one fast analyst using one playbook. Remaining risk: analysts knew which playbook they used and may have tried harder with the new one. Daniel states this risk in his report and plans a recheck after three months, when the new playbook has become routine and any novelty effect has faded. If the saving shrinks markedly by then, part of the original gain was probably effort rather than enrichment. Blinding analysts was not possible, because the enrichment results are visible on the screen, so the recheck is the best available control.

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

NIST CSF 2.0's Govern function places cybersecurity within enterprise risk management. The SOC is one part: it detects and responds, but depends on business units for context and on IT for action. At Meridian, the SOC's place under Govern means that its risk reports go to the enterprise risk committee, not only to IT. The claims operations manager supplies context on assignment and workload; IT performs account actions; legal and the data protection officer decide on notification. The SOC coordinates these but owns only detection and investigation, which is why escalation paths matter as much as tools.

### 7.2 Service levels

Daniel's service catalogue sets levels: P1 alerts acknowledged in 15 minutes, investigations started within 4 hours, monthly reports to each business unit. These levels came from the service catalogue Daniel drafted after comparing Meridian with forum peers. They also give the board measurable targets: the 15-minute P1 acknowledgement is the indicator that dipped in March and later recovered under the hybrid night model. Each level names who measures it and where it is reported. Each level is reported monthly to the business unit it serves, with misses explained.

### 7.3 Escalation paths

For claims-system alerts, escalation goes to the claims operations manager for business context, to IT for account actions, to legal and the DPO for possible breaches, and to HR only when misconduct is suspected after review. The order protects staff: HR is involved only after review suggests misconduct, as with flags like h04's that turned out to be project work. In the partner case, escalation reached legal and the data protection officer early because health data might have been copied. The escalation runbook names a person and a deputy for each path, so nobody has to search for contacts at night.

### 7.4 Risk reporting

The SOC reports risks in business terms to the enterprise risk committee: likelihood and impact of data disclosure, trends and treatment actions. For the contractor-account weakness, Daniel's report to the committee described the likelihood of a repeat, the possible disclosure of health data, and the treatment: the contractor directory, the confirmation request and the rule allowing immediate suspension of export rights. The committee tracks that treatment until the applied project reports its results, alongside other enterprise risks of similar size.

### 7.5 Hybrid model integration

With the managed night service, integration includes data access agreements, an escalation runbook and a shared case system. The provider's first night P1, a burst of failed logins to the claims portal, tested this integration. The runbook routed it to the on-call engineer, but the provider's note lacked the source network, so Daniel added that field to the escalation template. The shared case system meant both teams saw the same record, and the provider's quality was reviewed against the escalation precision target the board had set.

### 7.6 Change management

New monitoring or response capabilities are introduced with communication to affected teams, training and feedback. When the automated suspension of contractor export rights was introduced, Daniel briefed procurement and contractor managers first, explaining that suspension covers only exports and is reviewed within four hours. Analysts were trained on the review step, and contractors' feedback after the first suspensions informed small changes. Introducing it silently would have made the first wrongful suspension look like an attack on contractors. Before launch, analysts practised the four-hour review step on test scenarios built from past claims-export alerts.

### 7.7 Relationships

Daniel meets each business unit lead quarterly; regular contact makes incident calls smoother. These meetings paid off in the partner case: the claims operations manager already knew Daniel and could confirm within hours which weekend work had been approved. Without that relationship, the SOC would have waited for formal requests to move through several teams. Each meeting also lets business leads raise concerns about monitoring before they turn into complaints, which keeps insider-risk work acceptable to staff. Notes from each meeting record open requests and owners, so a business lead's concern about monitoring is followed up at the next one.

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

Difficult cases are those where evidence points in several directions, stakes are high and time is short. The SOC must decide without certainty and revise as evidence arrives. The partner case is Meridian's example: its own logs were consistent with approved overtime, while the partner's SOC suspected misuse, and policyholder health data might already be outside Meridian. Daniel's team had to act before knowing which story was true, using the expected-cost reasoning from the contractor incident and written hypotheses to guide what to collect next.

### 8.2 Case one: the partner

A claims-processing partner reports that one of its staff may have copied Meridian policyholder data. Meridian's logs show the partner account accessed 2,300 records over a weekend, within its contract scope but at an unusual time. The access sat within contract scope, so nothing in Meridian's logs proved wrongdoing; the unusual weekend timing and the partner's own report raised the question. Meridian could see what its systems recorded but not what happened to the data once the partner's staff had it. The case therefore depended on the partner's evidence and the contract's incident clause.

### 8.3 Conflicting evidence

The partner says the weekend work was approved overtime; the partner's own SOC suspects misuse. Meridian cannot see the partner's internal systems. Daniel writes both explanations down as hypotheses and lists the evidence that would separate them: an overtime approval record from the partner's manager would support the first; an export copied to removable media would support the second. Meridian cannot gather the latter itself, so the request under the incident clause names exactly what the partner should provide and by when.

### 8.4 Actions

Daniel's team preserves Meridian's logs, suspends the partner account's export rights pending review, informs the DPO and legal, and asks the partner for its evidence under the contract's incident clause. Suspending export rights, not the whole account, follows the reasoning of the contractor incident: it limits further harm while leaving the partner's legitimate claims work running. Informing the DPO early starts the record of awareness time, which matters if the case becomes notifiable. The request for evidence cites the contract clause, so the partner knows its obligation and the deadline for meeting it.

### 8.5 Communicating uncertainty

To the CISO, Daniel writes: "We know the account accessed 2,300 records within scope at unusual hours. We do not yet know whether data was copied. Likelihood of misuse: moderate, based on the partner SOC's concern. Next update: 18:00." The message separates what is known from what is not, gives a likelihood with its basis, and sets a time for the next update. The CISO can act on it without having to ask what each phrase means. A fixed update time also stops repeated calls for news.

### 8.6 Revising

The partner's evidence shows a USB copy of an export. The case becomes a confirmed breach; notification begins. Because export rights had already been suspended, the confirmed breach did not grow while the evidence was gathered. The awareness time recorded when the DPO was first informed allowed legal to calculate notification deadlines accurately. Daniel's earlier message to the CISO had said moderate likelihood, which the outcome did not contradict, and the review later judged the suspension a sound decision made before certainty.

### 8.7 Pressure

Under pressure, teams jump to conclusions or freeze. Written hypotheses and update times keep thinking clear. In the partner case, Daniel's written hypotheses kept the team from settling on overtime simply because it was the comfortable explanation, and set update times stopped the team from waiting indefinitely for certainty. The CISO received updates on schedule even when there was little new, so leadership did not fill the silence with its own assumptions. The same habit applies on any night with a difficult alert.

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

Leading a SOC means setting direction, protecting analysts from overload, developing people and representing the SOC to the organisation. Knerler, Parker and Zimmerman (2022) stress hiring and growing staff as a core strategy. For Daniel, protecting analysts from overload meant pushing for the hybrid night model rather than adding night shifts to his daytime team. Developing people meant rotations into detection engineering, and representing the SOC meant the board paper and quarterly meetings with business leads. The March dip, when two analysts left, showed how much the service depends on people.

### 9.2 Assurance

Executives and auditors ask: is the SOC working? Assurance answers with evidence: service-level performance, tested detection coverage, exercise results and incident outcomes. Daniel's half-year report to the audit committee uses two of these indicators, P1 acknowledgement and tested coverage of priority techniques, with incident outcomes alongside. When an auditor asked how coverage is tested, he could show the test records, which made the indicator credible. Assurance without records to back it is only a claim the committee has to trust.

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

P1 acknowledgement within 15 minutes rose from 85% in January to 95% by June, with a dip to 79% in March. Tested coverage of priority techniques rose steadily from 52% to 68%. The March dip coincided with two analysts leaving; the hybrid night model began in April. The dip has a known cause and a known response, which is what an audit committee needs. Daniel does not claim the hybrid model caused the recovery, only that the two coincided; the six-month review is where that question will be examined.

### 9.4 Honest reporting

Daniel reports the dip and its cause rather than averaging it away. Assurance that hides problems loses credibility when problems appear. In the half-year report, the March figure of 79% appears in the chart and the text, with the departure of two analysts as its cause and the hybrid night model as the response. Averaging the six months would have hidden a month in which nearly one P1 in five was acknowledged late. The committee asked about the dip, and Daniel's answer came from records rather than reassurance.

### 9.5 Culture

Blameless reviews, time for learning and recognition of good escalations build a culture where analysts raise problems early. At Meridian, good escalations are recognised in the monthly team meeting, including ones that turned out benign, such as the night P1 the on-call engineer judged needed no action. Reviews of the contractor and partner cases focused on decisions and information, not blame. Analysts who expect blame for a wrong call tend to escalate late or not at all, which is the opposite of what the SOC needs.

### 9.6 People development

Each analyst has a development plan: training, rotation into detection engineering and mentoring. Daniel reviews each plan every six months with the analyst. Rotation into detection engineering lets analysts see how rules are written and tested, which improves their triage. His own plan includes mentoring a senior analyst toward team leadership, so the SOC does not depend on him alone. Plans are adjusted when someone leaves, as in March, so that remaining analysts are not simply given more of the same work.

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

Research can test ideas SOCs adopt on faith. Daniel's programme asks students to critique three papers relevant to their work. For Meridian, research matters when it challenges a practice the team takes for granted, such as counting every benign alert as a false positive. Daniel chose papers on analyst experience, false positives and alert ranking because each touches a decision his SOC makes every week. His critiques end with a concrete action or a reason for taking none, so the reading changes practice rather than only knowledge.

### 10.2 Paper one

Kokulu et al. (2019) interviewed SOC staff and found mismatches between managers and analysts on issues such as metrics and automation. Strength: rich qualitative data from several SOCs. Limit: interview samples may not represent all SOCs. For Meridian, the paper's relevance is the mismatch on metrics: Daniel's managers value acknowledgement times, while his analysts may experience them as pressure that ignores difficult cases. His planned survey of his own analysts tests whether the mismatch exists at Meridian before changing any metric. A finding from other SOCs is a reason to ask, not an answer.

### 10.3 Paper two

Alahmadi, Axon and Martinovic (2022) surveyed and interviewed SOC practitioners about false positives, finding many are benign triggers. Strength: distinguishes types of false positive. Limit: self-reported perceptions, not measured alert data. The distinction matched Meridian's experience directly: h04's flag was a benign trigger, a correct detection of activity that had a business reason. Daniel's critique concludes that Meridian will record benign triggers separately from false positives in closure codes. Because the paper measured perceptions, he will check his own closure data before changing any rule.

### 10.4 Paper three

Hassan et al. (2019) proposed NoDoze, ranking alerts using provenance graphs, and evaluated it on enterprise data. Strength: quantitative evaluation. Limit: requires detailed provenance data many SOCs do not collect. For Meridian, the method's provenance requirement is the obstacle: the SOC does not collect detailed process provenance across endpoints, so NoDoze could not be applied without new data collection. Daniel records the idea of ranking alerts by context as worth watching, and notes that Meridian's assignment enrichment is a much simpler step in the same direction. His critique states that a quantitative evaluation elsewhere does not transfer automatically to a different data set.

### 10.5 Critique structure

Question, method, sample, findings, validity, relevance to practice and open questions. Daniel applies the structure to each paper in the same order, which makes his three critiques comparable and shows where each is strong or weak. For Alahmadi et al., the validity point was that results are perceptions; for NoDoze, relevance to practice was limited by data Meridian lacks. The open questions in each critique became items he could test with Meridian's own data. Using one structure also makes it easy to see when a critique skips a step, such as validity.

### 10.6 Relating to Meridian

Kokulu's mismatch finding prompts Daniel to survey his own analysts about metrics; Alahmadi's distinction informs how Meridian labels closed alerts. Neither change is adopted on the papers' authority alone. The survey checks whether Kokulu's finding holds at Meridian, and the closure-label change will be followed by a look at Meridian's own closure data before rules are modified. Research suggests where to look; local evidence decides what to do. Daniel records both steps in his critique, so Prof. Achebe can see how each paper led to a specific action.

### 10.7 Avoiding cherry-picking

Daniel searches for studies disagreeing with each paper's conclusions and notes them. For each paper he records at least one study that found differently or questioned the method, and states whether it changes his conclusion. This guards against choosing papers that confirm what he already believed, which is easy when the reading list is chosen by the reader. Prof. Achebe asks students to submit the disagreeing studies with their critiques. Where no disagreeing study could be found, he says so in the critique, rather than implying the conclusion is settled.

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

Daniel's applied project reduces time to contain compromised contractor accounts, the weakness exposed in chapter 1. The contractor incident showed that containment depended on reaching contractor managers, which often failed at night. The project tests whether changes to contacts, confirmation and authority shorten that time without causing unfair disruption to contractors. Daniel sets the measures before starting, so the result can be judged against the six-month baseline rather than an impression. The project's scope is contractor accounts only; staff accounts follow the existing process.

### 11.2 Baseline

Over the previous six months, four contractor compromises took a median of 3.5 hours from first alert to containment, mostly waiting for contractor managers to confirm activity. Four cases make the baseline imprecise, and Daniel reconstructed it from tickets after the fact, which he later named as the main thing he would do differently. Still, the pattern was clear: most of the time was spent waiting for a contractor manager to answer. The interventions target that wait directly. Daniel names timestamps recorded as cases happen, not reconstructed from tickets afterwards, as the requirement for any better baseline.

### 11.3 Interventions

A contractor directory with 24/7 contacts; an automated step that sends the contractor's manager a confirmation request; and a rule allowing analysts to suspend contractor export rights immediately for high-severity alerts, with review within four hours. Each intervention targets the waiting time found in the baseline. The directory removes the search for a contact at night; the automated request reaches the manager without an analyst drafting a message; and the suspension rule lets analysts act before confirmation arrives. Limiting suspension to export rights and requiring review within four hours keep the authority proportionate to the uncertainty.

### 11.4 Stakeholders

Procurement (contracts must require 24/7 contacts), contractor managers, IT and legal. Procurement adds a clause to new contracts. Each stakeholder had a stake in the design. Contractor managers needed to know what a confirmation request would look like and how quickly to answer; IT needed a way to suspend export rights alone; legal checked that suspension without notice fitted the contracts. Daniel met each group before launch, which made the first suspension less of a surprise to everyone involved. Legal checked the suspension clause against existing contractor agreements before the first suspension took place.

### 11.5 Risks

Wrongful suspension disrupts contractor work; mitigated by fast review and limiting suspension to export rights, not all access. The project counts wrongful suspensions as a measure, so the cost of the new rule is visible beside its benefit. Contractor managers can ask for immediate review, and every suspension is checked by a senior analyst within four hours. Limiting the action to exports means a wrongly suspended contractor can still do most of their work while the review takes place. This keeps the authority proportionate to the uncertainty at the moment of the alert.

### 11.6 Measurement

Time to contain for contractor compromises and test scenarios; count of wrongful suspensions. Time to contain is measured from the first alert to the suspension of export rights, using case-system timestamps, the same definition as the baseline. Test scenarios are reported beside real compromises, because they are planned and may run faster. Wrongful suspensions are counted with their duration, so the cost of the new rule is visible next to its benefit. Daniel fixed these definitions before the first case under the new process.

### 11.7 Result

Over the next four months, two real compromises and six test scenarios were contained in a median of 22 minutes. One wrongful suspension lasted 40 minutes before review restored access. The sample is small and mixes real cases with test scenarios, so Daniel describes the result as a large improvement on a small sample rather than a precise figure. The wrongful suspension shows the review step working; it also shows the real cost of acting early, which he reports rather than hides.

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

The programme took Daniel from explicit decision-making (chapter 1) through specialist evidence, ethics, design, evaluation, integration, difficult cases, assurance and research to an applied project. Each chapter added a method that the next used: the expected-cost reasoning from the contractor night reappeared in the partner case, peer baselines fed the fairness indicators, and the controlled evaluation of the triage playbook shaped how the applied project measured its result. Looking back lets Daniel see which methods he now uses without thinking and which still need practice.

### 12.2 Transferable methods

Expected-cost reasoning, peer baselines, controlled evaluation with robust statistics, structured critique and honest assurance apply beyond claims and contractors. Each has been used at Meridian outside its first setting: expected cost in the partner case, controlled evaluation for the managed provider's escalations, and honest assurance in the half-year report. What transfers is the discipline of stating beliefs, comparisons and uncertainty explicitly, not the particular numbers. The methods also give Daniel a shared language with the board, audit and legal, who meet the same reasoning in their own work.

### 12.3 Transfer example

Daniel applies controlled evaluation to the managed provider's escalation quality, comparing escalations before and after a template change. The comparison uses the same discipline as the triage evaluation: a defined measure, escalation precision and completeness of the provider's notes, collected the same way before and after the change. Because the template change followed the night P1 whose note lacked the source network, Daniel can check whether that gap closed. He notes that other changes at the provider during the same period could also affect the result.

### 12.4 Sustainability

Improvements must survive staff changes: playbooks documented, owners named, metrics automated and reviews scheduled. For the contractor project, this means the directory has an owner in procurement, the confirmation step is documented in the runbook, time to contain is reported automatically each month, and the suspension rule is reviewed yearly. If Daniel left Meridian, the improvement would continue without him. The same test is applied to the triage playbook and the service catalogue. Daniel lists each improvement with its owner, its documentation and its review date in a register that his successor would inherit.

### 12.5 Final review

The programme's final review is a viva with Prof. Achebe and an external SOC leader. Questions probe judgement: "When would you not use expected cost?" "How would you know insider monitoring had become unfair?" Both questions test whether Daniel understands the limits of his methods rather than only how to use them. An external SOC leader brings practical scepticism that a tutor alone might not, which is why the viva includes one. Daniel prepares by rereading his own decision records and the case reviews, since the examiners draw their questions from his submitted work.

### 12.6 Answers

On fairness, Daniel cites indicators: rising flags concentrated in one team or role without business explanation, or complaints through staff representatives. Such signs trigger a policy review. On expected cost, he answers that he would not rely on it when a legal duty settles the question, as when the business asked to delay notifying policyholders; there the duty decides, and costs only inform how to carry it out. Both answers name a concrete signal or limit rather than a general principle, which is what the examiners were looking for.

### 12.7 Development

Daniel plans to mentor a senior analyst into team leadership and to present the contractor project at the sector forum. Mentoring a senior analyst addresses the risk shown in March, when the SOC's performance depended on a few people. Presenting the contractor project at the forum returns something to the peers whose comparisons helped him start. Both plans have dates and are recorded with his own development plan, which Prof. Achebe reviews at the end of the programme. He also plans to repeat the analyst survey a year later to see whether metrics changes helped.

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
