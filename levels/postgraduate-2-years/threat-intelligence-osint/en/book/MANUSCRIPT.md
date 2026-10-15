# Threat Intelligence and OSINT: A Postgraduate Book

- Language: English (`en`); postgraduate course, two years.
- Editorial state: **published**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, with outputs embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working professionals moving into cyber threat intelligence (CTI) leadership or specialist roles.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical boundary: no collection on real private individuals, no terms-of-service evasion, no deanonymisation, no contact with adversary infrastructure. Organisations, people and indicators are **synthetic** unless a sentence cites a public source; addresses use RFC 5737 ranges and domains use `.example`.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–3 cover advanced decision-making, current practice and specialist evidence (with an analysis-of-competing-hypotheses lab). Chapters 4–6 cover risk and ethics, design alternatives and controlled evaluation (with a triage-rule evaluation lab). Chapters 7–9 cover organisational integration (with a TLP dissemination-gate lab), difficult cases and leadership. Chapters 10–12 cover research critique, an applied project and transfer. Each chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, five exercises scored 0–3, a synthesis and a **Continue studying** block.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Northmere Logistics Group (NLG)** — freight forwarding, warehouses and a customs-brokerage platform | Organisation building a CTI function | Invented |
| **Rafael Moreau** | Experienced security engineer studying part-time while leading NLG's new CTI function | Invented |
| **Freight and Ports Sharing Community (FPSC)** | Sector community exchanging intelligence under TLP 2.0 | Invented |

### Core sources

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) and [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); Hutchins et al. [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf); NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |
| [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame CTI around decisions rather than topics; (2) write decision-centred intelligence requirements; (3) use expected-loss reasoning without false precision; (4) record decisions and the intelligence behind them.

### 1.1 Decisions first

A CTI function earns its budget when it changes decisions: what to patch first, which supplier connection to restrict, whether to pay for a new detection capability. Rafael starts NLG's programme by interviewing decision-makers — the chief operating officer, the head of infrastructure, the customs-platform owner — and listing the decisions they face in the next year. The interviews produce a short list rather than a wish list: whether to segment the warehouse management network, which supplier remote access to restrict, and how to prioritise patching on the customs platform. Rafael records each decision with its owner and deadline in a register the COO can see.

### 1.2 Requirements tied to decisions

Each decision becomes a requirement: "Before the Q3 renewal of remote-access tooling, which access techniques are adversaries using against logistics firms?" A good requirement names the decision, the deadline and the consumer. Topic lists ("ransomware", "APT groups") cannot be closed and never end. Rafael rewrites every topic he receives as a requirement of this form. When the infrastructure head asked for everything about ransomware, the requirement became the segmentation question with a deadline before the budget round. Each requirement is closed when the decision is made and recorded, so the list stays short.

### 1.3 Expected loss, roughly

Decision-makers compare options. Rough expected-loss reasoning — likelihood band multiplied by impact range — helps them, as long as bands stay bands. "Likely (55–80%) attempt within a year; impact two to five days of warehouse disruption" supports a choice better than a single invented number. For NLG, a warehouse outage of two to five days means missed deliveries and contract penalties, which the operations team can estimate. Rafael gives likelihood and impact as ranges and shows how the choice changes across them. The segmentation decision was supported this way, without anyone claiming a precise probability.

### 1.4 Value of information

Before collecting, ask whether any plausible answer would change the decision. If the board will fund multi-factor authentication for all remote access regardless, further intelligence on the threat adds little decision value; effort should move elsewhere. At NLG, the board had already decided to require multi-factor authentication for supplier access, so Rafael did not spend effort on more reporting about that threat. He moved the time to the segmentation question, where the answer could change what was funded. Writing down why a requirement was dropped keeps the decision visible to the team. He asks this question for every new request before collection starts.

### 1.5 Decision records

Record the decision, the date, the intelligence used, its confidence and who decided. Later reviews can then separate bad luck from bad judgment. The segmentation decision record lists the decision, its date, the intelligence on lateral movement into operational networks, the moderate-confidence assessment and the COO as decider. Without such a record, a later incident could make a sound decision look careless, or a lucky one look wise. Rafael stores records in the platform, linked to the requirements they closed, and reviews a sample each year.

### 1.6 Time horizons

Strategic decisions run over years, operational over weeks, tactical over hours. Each horizon needs different collection and a different cadence of reporting; mixing them in one weekly bulletin satisfies no one. At NLG, the segmentation decision is strategic, supplier access changes are operational, and an incident needs tactical updates within hours. Rafael sets a different product for each: an annual threat profile, a monthly brief for leadership and short incident updates. Each consumer receives only the horizon they act on, which keeps reports short.

### Worked example

The infrastructure head asks for "everything about ransomware". Rafael reframes: the real decision is whether to isolate the warehouse management network from office IT this year. He scopes intelligence to techniques used for lateral movement into operational networks in the logistics sector and a short impact estimate. The decision — to fund segmentation — is recorded with a moderate-confidence assessment.

> **Synthetic case.** NLG and its decisions are invented.

### Errors and limits

Decision framing can narrow vision; keep a small horizon-scanning effort for surprises.

### Exercises

- **EX001 — Reframe a topic.** Turn "tell me about ransomware" into a decision-centred requirement for a firm you know. *Rubric:* 3 = names decision, deadline, consumer; 2 = two; 1 = still topic; 0 = none.
- **EX002 — Information value.** When does additional intelligence have little decision value? *Rubric:* 3 = when no plausible answer changes the choice; 2 = partial; 1 = never; 0 = none.
- **EX003 — Banded estimate.** Write an expected-loss statement using bands, not point values. *Rubric:* 3 = likelihood band + impact range + confidence; 2 = two; 1 = point estimate; 0 = none.
- **EX004 — Record contents.** List the fields of a decision record. *Rubric:* 3 = decision, date, intelligence used, confidence, decider; 2 = three; 1 = one; 0 = none.
- **EX005 — Horizon mismatch.** Why does a single weekly bulletin serve strategic and tactical consumers badly? *Rubric:* 3 = different horizons, detail and cadence; 2 = partial; 1 = it serves well; 0 = none.

### Synthesis

Start from decisions, tie requirements to them, reason in bands, weigh information value and record what was decided.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Threat intelligence and OSINT: current practice

### Learning outcomes

You will (1) survey how mature CTI teams operate today; (2) compare internal, community and commercial sourcing; (3) assess the role of automation and its limits; (4) position a new function realistically.

### 2.1 What mature teams do

Mature teams run a requirements process, maintain a threat profile of relevant adversaries and techniques, feed detection engineering, support incident response and brief leadership. NIST SP 800-150 emphasises sharing relationships and clear rules for what can be shared. Many teams use a threat intelligence platform storing STIX 2.1 objects and exchanging them over TAXII 2.1. For a new function like NLG's, this list shows the destination rather than the first year's scope. Rafael uses it to explain to leadership what a mature team does, then picks the parts that match NLG's decisions: requirements, a sector threat profile and support for detection engineering.

### 2.2 Sourcing mix

Internal telemetry and incidents give the most relevant evidence. Communities like FPSC give sector context and early warning. Commercial providers add breadth and finished reporting. Open sources — advisories, vendor research, certificate logs — fill gaps when collected lawfully and within terms of service. Rafael's benchmarking with peer firms showed that buying broad commercial feeds first often brings low relevance. He starts with internal incident review and FPSC membership, which give the most relevant evidence for NLG, and defers commercial spending until requirements show gaps. The source catalogue records each source, its terms of use and which requirements it serves.

### 2.3 Automation

Automation ingests, deduplicates, enriches and distributes indicators. It does not judge relevance well, nor write assessments. Teams that automate everything flood defenders with low-value indicators; those that automate nothing drown in copy-paste. At NLG, the platform ingests FPSC indicators and removes duplicates automatically, but deciding whether an advisory matters to the customs platform is an analyst's job. Rafael limits automatic distribution to indicators that pass the triage rule, so the operations centre receives fewer, more relevant items. He reviews the automation each quarter for items that slipped through or were wrongly filtered.

### 2.4 Technique-centred practice

Following Bianco's Pyramid of Pain, mature teams invest in technique-level intelligence mapped to ATT&CK, because detections built on behaviour last longer than those built on hashes and addresses. For NLG, technique-level intelligence means describing how adversaries use valid accounts or remote services against logistics firms, so detections can look for that behaviour. Hashes and addresses from FPSC still help in incidents, but they change quickly. Rafael's final project builds its backlog from techniques for this reason, and maps each item to ATT&CK so the operations centre can track coverage.

### 2.5 Starting small

A two-person team should pick a few requirements, one community, internal incident data and a modest platform — and prove value before expanding. Rafael's first year follows this advice: a handful of requirements from the decision interviews, FPSC as the one community, internal incident review, and an open-source platform. Proving value means showing decisions that intelligence informed, such as segmentation funding. Expansion, such as a commercial feed, waits until requirements show a gap that existing sources cannot fill. He agrees this plan with the COO before spending anything.

### 2.6 Common anti-patterns

Buying several feeds before defining requirements; publishing a daily newsletter nobody reads; measuring success by indicator volume; keeping intelligence inside the CTI team rather than embedding it in detection and response workflows. Peer firms in FPSC described the first anti-pattern directly: they bought large feeds and later cut them for low relevance. Rafael uses the list as a check on his own plan. Instead of a daily newsletter, NLG gets products tied to decisions; instead of counting indicators, he measures consumer actions; and an analyst is embedded in the operations centre two days a week.

### Worked example

Rafael benchmarks against three peer firms through FPSC conversations. Two bought large commercial feeds first and later cut them for low relevance. He chooses FPSC membership plus internal incident review for year one, with a small STIX-capable platform, and defers commercial spending until requirements show gaps.

> **Synthetic case.** The peers and choices are invented.

### Errors and limits

Peer practice is anecdotal; what works for a large firm may not suit NLG.

### Exercises

- **EX006 — Most relevant source.** Which source type usually gives the most relevant evidence, and why? *Rubric:* 3 = internal telemetry/incidents—what actually reached you; 2 = name; 1 = commercial; 0 = none.
- **EX007 — Automation boundary.** Name two tasks automation does well and one it does poorly in CTI. *Rubric:* 3 = e.g. ingest/dedupe well; relevance judgment poorly; 2 = partial; 1 = all well; 0 = none.
- **EX008 — Pyramid logic.** Why do mature teams favour technique-level intelligence? *Rubric:* 3 = harder for adversaries to change; detections last; 2 = partial; 1 = easier to collect; 0 = none.
- **EX009 — Anti-pattern spot.** Identify an anti-pattern in "we measure success by indicators ingested". *Rubric:* 3 = activity metric not outcome; volume ≠ value; 2 = partial; 1 = good metric; 0 = none.
- **EX010 — Year-one plan.** Justify Rafael's deferral of commercial feeds. *Rubric:* 3 = requirements first; peers cut low-relevance feeds; prove value; 2 = one reason; 1 = cost only; 0 = none.

### Synthesis

Mature practice is requirements-led, technique-centred and selectively automated; start small and prove value.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Threat intelligence and OSINT: specialist evidence

### Learning outcomes

You will (1) apply analysis of competing hypotheses (ACH); (2) weigh diagnostic versus non-diagnostic evidence; (3) handle deception and gaps; (4) state conclusions with calibrated confidence.

### 3.1 Why ACH

Heuer's analysis of competing hypotheses asks analysts to list all reasonable hypotheses, score each piece of evidence against each, and favour the hypothesis with the least inconsistent evidence. It counters the habit of accepting the first plausible story. At NLG, the first plausible story after the data theft was an external extortion crew, because extortion emails followed. ACH forced Rafael to test that story alongside supplier compromise and insider misuse, using the same evidence for each. The matrix is kept with the assessment, so reviewers can see how each item was scored.

### Lab — competing hypotheses

```python
"""Lab (ch 03): analysis of competing hypotheses - count inconsistencies per hypothesis (synthetic)."""
H = ["H1 criminal extortion crew", "H2 insider misuse", "H3 supplier compromise"]
# C = consistent, I = inconsistent, N = neutral
E = {"E1 login from supplier VPN range": "NIC",
     "E2 data staged at 02:00 local": "CCC",
     "E3 extortion note received": "CNN",
     "E4 credentials used were service account": "ICC",
     "E5 same tool seen at two other firms": "CIC"}
score = [0, 0, 0]
for e, row in E.items():
    for k, v in enumerate(row):
        score[k] += v == "I"
for h, s in sorted(zip(H, score), key=lambda x: x[1]):
    print(f"{h}: {s} inconsistent")
print("least inconsistent:", min(zip(score, H))[1])
```

Run with `python3 lab_ach.py`. Verified output:

```text
H3 supplier compromise: 0 inconsistent
H1 criminal extortion crew: 1 inconsistent
H2 insider misuse: 2 inconsistent
least inconsistent: H3 supplier compromise
```

### 3.2 Reading the result

Three hypotheses about a data theft at NLG are tested against five evidence items. Supplier compromise (H3) has no inconsistent evidence; criminal extortion (H1) has one; insider misuse (H2) has two. H3 is the leading hypothesis, but H1 is close. Close scores mean the ranking could change with one new piece of evidence, so Rafael treats H3 as the leading explanation, not a conclusion. His report keeps H1 as plausible and names verification of the supplier VPN log as the most valuable next step.

### 3.3 Diagnosticity

Evidence consistent with every hypothesis — data staged at 02:00 (E2) — does not help choose. Diagnostic evidence discriminates: the login from the supplier VPN range (E1) is inconsistent with an external crew and neutral for an insider. Analysts should collect more diagnostic evidence rather than more evidence. For Rafael, this means the next effort should go to verifying the supplier VPN log with the supplier, not collecting more logs that fit every hypothesis. He lists which evidence items are diagnostic and which are not in the assessment, so leadership can see why one verification step matters more than many additional logs.

### 3.4 Deception and gaps

Adversaries plant false clues; tools are sold widely. Ask which evidence would be easy to fake and give it less weight. List what evidence is missing and what it would show. In the NLG case, a VPN address could be borrowed by an attacker using stolen supplier credentials, so E1 does not prove the supplier itself acted. Rafael notes this beside E1 and lists missing evidence, such as the supplier's own VPN log, with what each would show. Gaps are written into the assessment itself, so leadership knows what the conclusion does not yet rest on.

### 3.5 Confidence

A one-point margin between H3 and H1 supports low-to-moderate confidence. ICD 203 asks analysts to explain the basis of confidence, including gaps. Rafael's report states the basis for low-to-moderate confidence: the close margin, reliance on one diagnostic item and missing supplier logs. Explaining confidence lets leadership decide how much to act on the assessment. The supplier access restrictions went ahead because they were sensible under either leading hypothesis.

He also says what would raise confidence: confirmation from the supplier's own VPN log that the session came from its staff, or evidence that the supplier credentials had been stolen elsewhere.

### 3.6 Sensitivity

Ask which single evidence item, if wrong, would change the ranking. If E1's VPN attribution is mistaken, H1 and H3 tie. That tells Rafael where to verify first. Sensitivity analysis turns a list of evidence into a plan for verification. Because E1 decides the ranking, Rafael asks the supplier to check its VPN log before spending time elsewhere. He records the result of the check when it arrives, and updates the matrix and the confidence statement in a marked revision of the assessment.

### Worked example

Rafael's report states: "The leading explanation is a compromise of a supplier's access (low-to-moderate confidence). An external extortion crew remains plausible. Verifying the supplier VPN log (E1) with the supplier is the most valuable next step." He shares the assessment with leadership only, at TLP:AMBER+STRICT.

> **Synthetic case.** The theft and evidence are invented.

### Errors and limits

ACH counts are judgments; equal weights hide strong evidence. Use counts to structure debate, not as verdicts.

### Exercises

- **EX011 — Lab ranking.** Report the lab's hypothesis ranking with inconsistency counts. *Rubric:* 3 = H3 0, H1 1, H2 2; 2 = order only; 1 = wrong; 0 = none.
- **EX012 — Non-diagnostic item.** Which evidence item is non-diagnostic, and why? *Rubric:* 3 = E2—consistent with all; 2 = item only; 1 = E1; 0 = none.
- **EX013 — Sensitivity point.** Which evidence item should be verified first, and why? *Rubric:* 3 = E1; changing it ties H1/H3; 2 = item only; 1 = E3; 0 = none.
- **EX014 — Easy to fake.** Give an example of evidence an adversary could easily plant. *Rubric:* 3 = e.g. language strings, tool reused/sold, extortion branding; with reason; 2 = example; 1 = vague; 0 = none.
- **EX015 — Confidence phrase.** Why does Rafael say low-to-moderate confidence? *Rubric:* 3 = narrow margin; key evidence unverified; 2 = one; 1 = high; 0 = none.

### Synthesis

Test competing hypotheses, seek diagnostic evidence, guard against deception and calibrate confidence to margins and gaps.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) integrate threat intelligence into enterprise risk assessment; (2) apply data-protection principles to OSINT at scale; (3) govern ethically sensitive collection; (4) handle conflicts between business pressure and ethics.

### 4.1 Threat in the risk register

Risk registers often score likelihood by gut feeling. CTI can anchor the likelihood column: observed sector techniques, actors' known interest in logistics, and NLG's exposure. Each likelihood should cite the intelligence and its confidence, and be revisited when intelligence changes. Rafael works with NLG's risk team to rewrite the likelihood entries for ransomware, supplier compromise and customs-platform exploitation. Each now cites FPSC reporting, NLG's incidents and exposure, with a confidence level. When intelligence changes, such as new sector reporting, the entry is reviewed rather than left at its old score.

### 4.2 OSINT at scale

Monitoring public sources for brand abuse, leaked credentials or exposed NLG data touches personal data. Under the GDPR, NLG needs a lawful basis (often legitimate interests, with a documented balancing test), purpose limitation, minimisation and retention limits. A data-protection impact assessment is wise for systematic monitoring. At NLG, monitoring leak sites and code repositories for exposed credentials could collect employees' and customers' personal data. Rafael writes the balancing test with the privacy officer, limits searches to NLG domains and brands, and sets a retention period for anything collected. The data-protection impact assessment is completed and signed by the privacy officer before monitoring begins.

### 4.3 Collection governance

A collection policy lists approved sources and methods, prohibited ones (fake personas, purchasing stolen data, accessing closed criminal markets without legal approval), approval routes and audit. Analysts should know before a crisis what they may not do. NLG's policy names the approved sources, such as FPSC, public advisories and a contracted provider for leak-site monitoring, and lists prohibited methods. Approval routes say who can authorise a new method, and the ethics panel handles anything not already listed. When the leak-site claim appeared, the team used the contracted provider, as the policy required, rather than visiting the site from a corporate machine.

### 4.4 Purchasing stolen data

A vendor offers NLG's leaked customer database "for verification". Paying may fund criminals, may be unlawful and creates a new copy of personal data. The ethical path runs through legal counsel, law enforcement and incident response, not procurement. Rafael's answer follows the collection policy: the offer goes to legal counsel and incident response, and law enforcement is informed. Buying the data would not prove what was taken, since the seller could alter it, and it would put more personal data into NLG's systems. The refusal and its reasons are recorded, so the same offer can be answered quickly if it returns.

### 4.5 Pressure

Executives under stress may ask for intrusive actions — "find out who the hacker is". Analysts need the policy and the confidence to say no, offering lawful alternatives. When the COO asked Rafael to unmask the sender of an extortion email, he explained that identifying individuals is a police matter and offered a lawful assessment of the extortion group's typical behaviour instead. The policy gave him a clear basis for refusing, and the alternative gave the COO something useful.

Rafael keeps a short list of lawful alternatives ready, so a refusal never leaves an executive empty-handed.

### 4.6 Ethics review

A small ethics panel — legal, privacy, security leadership — reviews new collection methods once, then approves them for routine use. This avoids both ad hoc risk-taking and paralysis. At NLG, the panel reviewed the contracted leak-site monitoring service before it was used, approving it with conditions on what could be retrieved and stored. After approval, analysts could request retrievals routinely without returning to the panel each time. New methods, such as monitoring closed forums, would need a fresh review.

The panel meets only when a new method is proposed, which at NLG has been a few times a year.

### Worked example

After an extortion email, the COO asks Rafael to "unmask" the sender. Rafael explains NLG's policy: CTI will preserve evidence, assess the threat and support law enforcement; identifying individuals is a police matter. He offers a lawful assessment of the extortion group's typical behaviour based on public reporting and FPSC intelligence.

> **Synthetic case.** The email and exchange are invented.

### Errors and limits

Law varies by country; this chapter is not legal advice. Involve counsel early.

### Exercises

- **EX016 — Register anchor.** How can CTI improve a risk register's likelihood column? *Rubric:* 3 = cite observed techniques/actor interest/exposure with confidence; revisit; 2 = partial; 1 = gut feel fine; 0 = none.
- **EX017 — Lawful basis.** Which GDPR elements apply to systematic brand-abuse monitoring? *Rubric:* 3 = lawful basis/balancing test, purpose limitation, minimisation, retention, DPIA; 2 = three; 1 = one; 0 = none.
- **EX018 — Stolen database offer.** Give three reasons not to buy the leaked database. *Rubric:* 3 = funds criminals, may be unlawful, new copy of personal data; 2 = two; 1 = one; 0 = none.
- **EX019 — Unmask request.** What lawful alternative did Rafael offer the COO? *Rubric:* 3 = threat assessment of group behaviour, evidence preservation, police support; 2 = partial; 1 = complied; 0 = none.
- **EX020 — Panel purpose.** What does a one-time ethics review of a method achieve? *Rubric:* 3 = avoids ad hoc risk and paralysis; routine approval; 2 = partial; 1 = bureaucracy only; 0 = none.

### Synthesis

Anchor risk in intelligence, govern OSINT under data-protection law, refuse unlawful collection and offer lawful alternatives.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Threat intelligence and OSINT: design alternatives

### Learning outcomes

You will (1) compare centralised, embedded and outsourced CTI models; (2) evaluate platform options; (3) choose data models and sharing protocols; (4) document design rationale.

### 5.1 Organisational models

A centralised team serves everyone from one place and keeps standards consistent but can drift from operational needs. Embedded analysts sit in the security operations centre or risk team and stay close to consumers but may lose common method. Outsourced intelligence brings scale but limited business context. Hybrids are common. NLG chooses a hybrid: a small central CTI function with one analyst embedded in the security operations centre two days a week. The central function keeps method and requirements consistent, while the embedded analyst learns what detection engineers need.

### 5.2 Platform options

Options range from spreadsheets and a shared mailbox, through open-source threat intelligence platforms, to commercial platforms. Criteria: STIX 2.1 support, TAXII 2.1 client and server, TLP enforcement, integration with detection tools, cost and maintainability. Rafael scores three options against these criteria, with the CTI analyst and an operations centre engineer. Spreadsheets fail on TLP enforcement and sharing; a commercial platform scores highest but costs four times the budget; an open-source platform with STIX and TAXII support scores well enough. He chooses the open-source option and records the scores and reasons in a decision record.

### 5.3 Data model

Using STIX 2.1 internally keeps sharing simple: indicators, attack patterns, relationships and reports map directly to community exchange. Custom fields should use STIX extensions rather than ad hoc columns. At NLG, storing data in STIX means indicators received from FPSC keep their structure and relationships, and NLG's own reports can be shared back without conversion. It also makes migration to another platform feasible later, which was one reason Rafael accepted an open-source platform. Custom fields, such as a link to NLG's asset inventory, use STIX extensions.

### 5.4 Protocols

TAXII 2.1 collections let NLG pull from FPSC and publish to it. Email remains necessary for human-readable products, and must carry TLP labels in the subject and body as TLP 2.0 recommends. NLG pulls FPSC collections automatically and publishes sanitised indicators back when it has something useful to share. Human-readable products, such as the monthly leadership brief, go by email with TLP labels in both subject and body. Rafael checks that the platform applies labels consistently, since a missing label is one way restricted material leaks.

### 5.5 Design rationale

Record options, criteria, scores and the reason for the choice. Future leaders can revisit decisions when conditions change. Rafael's platform decision record lists the three options, the criteria, scores and the reason for choosing the open-source platform. It also notes the conditions that would reopen the decision, such as a large budget increase or the platform failing to keep up with STIX releases. His successor can then revisit the choice without repeating the analysis.

The record sits in the platform beside the requirements that motivated the choice, so anyone reviewing the platform can find it.

### 5.6 Reversibility

Prefer designs that can be changed cheaply. A standards-based data model allows platform replacement later; proprietary formats lock data in. Choosing STIX for NLG's data means the platform can be replaced without losing years of intelligence or rebuilding relationships between objects. Rafael also avoids custom integrations that only work with one product. Reversibility made the cheaper open-source platform an acceptable risk, since a later move to a commercial product would not strand data.

Rafael checks reversibility again before agreeing any integration that would tie the operations centre's tools to the platform.

### Staffing the design

A design needs people to run it. Two analysts can support one community relationship, internal incident review and a modest platform; adding hunting or a public research blog would need more. Match ambition to headcount explicitly in the design document.

### Worked example

Rafael scores three options. Spreadsheets fail on TLP enforcement and sharing. A commercial platform scores highest on features but costs four times the budget. An open-source platform with STIX and TAXII support scores well enough, and because data is stored in STIX, migrating later is feasible. He chooses it, embedding one analyst in the security operations centre two days a week.

> **Synthetic case.** The scores and options are invented.

### Errors and limits

Open-source platforms need maintenance skills; count staff time as cost.

### Exercises

- **EX021 — Model trade-off.** Compare centralised and embedded CTI on one strength and one weakness each. *Rubric:* 3 = consistency vs drift; closeness vs method loss; 2 = partial; 1 = one; 0 = none.
- **EX022 — Platform criteria.** List four criteria for choosing a CTI platform. *Rubric:* 3 = four of STIX, TAXII, TLP enforcement, integration, cost, maintainability; 2 = three; 1 = one; 0 = none.
- **EX023 — Extensions over columns.** Why use STIX extensions for custom fields? *Rubric:* 3 = keeps standard compatibility/sharing; 2 = partial; 1 = no reason; 0 = none.
- **EX024 — Email marking.** How should human-readable email products carry TLP? *Rubric:* 3 = label in subject and body per TLP 2.0; 2 = one place; 1 = optional; 0 = none.
- **EX025 — Hidden cost.** What cost is often missed when choosing open-source platforms? *Rubric:* 3 = staff time/maintenance skills; 2 = vague; 1 = licence; 0 = none.

### Synthesis

Choose organisational and technical designs against explicit criteria, favour standards and reversibility, and record rationale.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Threat intelligence and OSINT: controlled evaluation

### Learning outcomes

You will (1) evaluate CTI processes with labelled data; (2) compute and interpret precision and recall; (3) design fair comparisons; (4) choose a rule according to consumer cost.

### 6.1 Why evaluate

Claims such as "our triage rule catches what matters" need evidence. A controlled evaluation applies alternatives to the same labelled set and compares outcomes. At NLG, the question was which triage rule to use for incoming advisories before the operations centre receives them. Rafael's team built a set of synthetic items with labels agreed before either rule was run, then applied both rules to the same set. The result gave the security operations lead evidence for the choice instead of a preference.

### Lab — two triage rules

```python
"""Lab (ch 06): compare two triage rules on 20 labelled synthetic items."""
truth = [1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0]
ruleA = [1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0]   # broad keyword rule
ruleB = [1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0]   # asset-match rule
def pr(p):
    tp = sum(a and b for a, b in zip(p, truth)); fp = sum(a and not b for a, b in zip(p, truth))
    fn = sum(b and not a for a, b in zip(p, truth))
    return tp, fp, fn, round(tp/(tp+fp), 2), round(tp/(tp+fn), 2)
for n, r in (("A", ruleA), ("B", ruleB)):
    tp, fp, fn, p, rc = pr(r)
    print(f"rule {n}: tp={tp} fp={fp} fn={fn} precision={p} recall={rc}")
```

Run with `python3 lab_eval.py`. Verified output:

```text
rule A: tp=6 fp=4 fn=0 precision=0.6 recall=1.0
rule B: tp=4 fp=0 fn=2 precision=1.0 recall=0.67
```

### 6.2 Reading the result

On twenty labelled synthetic items, rule A (broad keywords) finds all six relevant items but raises four false alarms: precision 0.6, recall 1.0. Rule B (match against NLG's asset inventory) raises no false alarms but misses two relevant items: precision 1.0, recall 0.67. Rule A wastes analyst time on items that do not matter to NLG, while rule B misses items that do.

In NLG terms, rule A flags ten of the twenty items, and four of those ten would reach the operations centre as advisories about products NLG does not run, which is what precision 0.6 means here. Rule B flags four items, all relevant, but silently drops two that concern a supplier's product.

### 6.3 Which is better?

Neither in general. If analyst time is scarce and misses can be caught elsewhere, rule B fits. If missing a relevant item is costly — for example, a vulnerability in a customs platform — rule A, or B with a secondary check, fits. The choice depends on costs, not on one metric. For NLG, Rafael recommended rule B plus an inventory update, with a monthly broad-keyword sweep as a safety net. That combination saves analyst time while reducing the risk of missing an item about the customs platform.

### 6.4 Fair comparison

Use the same items, labels made before seeing rule outputs, and labellers blind to which rule flagged what. Report sample size; twenty items gives wide uncertainty. Twenty items is enough to see the trade-off but too few to estimate precision or recall closely, so Rafael reports counts with each figure. Labels were agreed before the rules ran, and the labeller did not know which rule flagged each item. He records the method with the results, so the evaluation can be repeated with more items.

### 6.5 Error analysis

Read the misses. Rule B missed two items about a supplier product absent from the inventory — an inventory gap, not a rule flaw. Fixing the inventory may help more than changing the rule. Reading the two misses showed both concerned a supplier product missing from NLG's asset inventory. Rule B could not match what the inventory did not contain. Rafael asks the asset owners to add the product and checks whether other supplier products are missing. The fix improves rule B and every other process that uses the inventory.

### 6.6 Repeating over time

Threats change; rerun the evaluation quarterly with fresh labelled items. New suppliers, platforms and adversary techniques can change which rule works best. Each quarter, Rafael's team labels a fresh set of synthetic items, applies both rules and compares the results with earlier quarters. If rule B's misses rise, the inventory or the rule needs attention. The results are reported to the security operations lead with counts and the date of each run.

Each quarter's labelled set is kept, so later comparisons can include earlier items as well as fresh ones.

### Beyond triage

The same method evaluates other processes: indicator expiry rules, enrichment sources or report templates. Define the outcome, label a sample, apply alternatives and compare. The discipline matters more than the specific metric.

### Worked example

Rafael reports: "Rule B saves about four triage reviews per twenty items at the cost of two misses, both caused by inventory gaps. Recommend rule B plus an inventory update, and a monthly broad-keyword sweep as a safety net." The security operations lead agrees.

> **Synthetic case.** The items and rules are invented.

### Errors and limits

Labels can be wrong; double-label a sample. Small sets justify only tentative conclusions.

### Exercises

- **EX026 — Lab metrics.** Give precision and recall for both rules. *Rubric:* 3 = A 0.6/1.0, B 1.0/0.67; 2 = one rule; 1 = wrong; 0 = none.
- **EX027 — Cost-based choice.** When would rule A be preferable? *Rubric:* 3 = when misses are costly and analyst time available; 2 = partial; 1 = always; 0 = none.
- **EX028 — Blind labelling.** Why should labellers not know which rule flagged an item? *Rubric:* 3 = avoids bias favouring a rule; 2 = partial; 1 = no reason; 0 = none.
- **EX029 — Root of misses.** What caused rule B's misses and what fix follows? *Rubric:* 3 = inventory gap; update inventory; 2 = one; 1 = rule bug; 0 = none.
- **EX030 — Sample caution.** What does a sample of twenty items imply for conclusions? *Rubric:* 3 = wide uncertainty; tentative; repeat; 2 = partial; 1 = definitive; 0 = none.

### Synthesis

Evaluate with labelled data, read both precision and recall, choose by consumer costs and analyse errors before redesigning.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Threat intelligence and OSINT: organizational integration

### Learning outcomes

You will (1) embed CTI into security operations, incident response and risk; (2) enforce TLP in dissemination workflows; (3) design service agreements with consumers; (4) measure integration.

### 7.1 Integration points

CTI feeds detection engineering (technique priorities), the security operations centre (indicators and context), incident response (adversary profiles during incidents, aligned with NIST SP 800-61r3), vulnerability management (exploitation intelligence) and risk (likelihood). Each needs a defined input format and owner. At NLG, each integration point has an owner and a format: the detection team receives technique priorities as backlog items, the operations centre receives indicators through the platform, incident response receives adversary profiles on request, and the risk team receives likelihood updates. Rafael agrees each with its consumer and records it in a service agreement.

### Lab — dissemination gate

```python
"""Lab (ch 07): TLP 2.0 dissemination gate - fail closed on unknown labels (synthetic)."""
RANK = {"TLP:CLEAR": 0, "TLP:GREEN": 1, "TLP:AMBER": 2, "TLP:AMBER+STRICT": 3, "TLP:RED": 4}
AUD = {"public": 0, "community": 1, "client": 2, "internal": 3, "named": 4}
items = [("R1", "TLP:GREEN", "community"), ("R2", "TLP:AMBER", "public"),
         ("R3", "TLP:AMBER+STRICT", "client"), ("R4", "TLP:CLEAR", "public"), ("R5", "AMBER", "internal")]
for rid, lab, aud in items:
    if lab not in RANK:
        print(rid, lab, aud, "BLOCK unknown label"); continue
    print(rid, lab, aud, "ALLOW" if AUD[aud] >= RANK[lab] else "BLOCK")
```

Run with `python3 lab_gate.py`. Verified output:

```text
R1 TLP:GREEN community ALLOW
R2 TLP:AMBER public BLOCK
R3 TLP:AMBER+STRICT client BLOCK
R4 TLP:CLEAR public ALLOW
R5 AMBER internal BLOCK unknown label
```

### 7.2 Reading the result

A GREEN report to the community is allowed; AMBER to the public is blocked; AMBER+STRICT to a client is blocked, because it is limited to the recipient organisation; CLEAR to the public is allowed. A label written "AMBER" without the TLP prefix is unrecognised, so the gate fails closed and blocks it. Failing closed on an unrecognised label protects FPSC material even when someone makes a simple formatting mistake. Rafael uses these results to explain the gate to the customer-facing teams who most often ask to share intelligence.

### 7.3 Fail closed

When a label is missing or unknown, block and ask. A gate that guesses will sooner or later leak restricted partner material and damage trust in the community. When the sales manager tried to forward an AMBER+STRICT advisory to a customer, the gate blocked it, and Rafael asked FPSC for a version that could be shared. FPSC agreed to a sanitised GREEN summary, which went to the customer instead. Blocking first and asking afterwards kept NLG's standing in the community and still gave the customer something useful.

### 7.4 Service agreements

Agree with each consumer what they receive, in what format, how fast and how they give feedback. For example, the operations centre gets validated indicators within four hours of FPSC receipt; leadership gets a monthly two-page brief. Written agreements make expectations clear on both sides, so missed deliveries can be discussed against something concrete. The operations centre knows when to expect validated indicators and how to report false positives; leadership knows the brief will arrive monthly and what it covers. Rafael reviews each agreement every six months, using feedback to adjust timing or format, and records changes.

### 7.5 Measuring integration

Measure consumer actions: detections created from intelligence, vulnerabilities reprioritised, risk entries updated. Survey consumers twice a year. Counting actions shows whether intelligence changed what consumers do, which is the purpose of the function. Rafael's report lists, for each quarter, detections created, vulnerabilities reprioritised and risk entries updated, with examples. The survey asks consumers what was useful and what they ignored, and the answers shape the next quarter's priorities and products.

The first survey showed that the operations centre valued indicator context more than the indicators themselves, and Rafael changed the format accordingly.

### 7.6 Clients and partners

NLG serves customers who sometimes ask for threat information. TLP:AMBER allows sharing with clients on a need-to-know basis; AMBER+STRICT does not. Customer-facing teams must know the difference before passing anything on. At NLG, customer-facing staff are trained to check the label before passing anything on and to ask the CTI team when unsure. The sales manager's attempt to forward an AMBER+STRICT advisory showed why. A short guide explains what each label permits, with NLG examples.

The guide is part of induction for new customer-facing staff.

### Worked example

A sales manager wants to forward an FPSC AMBER+STRICT advisory to a major customer. The gate blocks it. Rafael asks FPSC whether a version can be released at TLP:AMBER or GREEN; FPSC agrees to a sanitised GREEN summary, which goes to the customer.

> **Synthetic case.** The advisory and customer are invented.

### Errors and limits

Automated gates only see labels; mislabelled content still leaks. Train senders.

### Exercises

- **EX031 — Gate outcomes.** Which lab items were blocked, and why? *Rubric:* 3 = R2 AMBER→public, R3 STRICT→client, R5 unknown label; reasons; 2 = items only; 1 = one; 0 = none.
- **EX032 — Fail closed.** Defend failing closed on unknown labels. *Rubric:* 3 = guessing risks leaks/trust; ask originator; 2 = partial; 1 = fail open; 0 = none.
- **EX033 — Customer request.** How was the sales manager's request resolved lawfully? *Rubric:* 3 = asked FPSC for sanitised lower-TLP version; 2 = partial; 1 = forwarded; 0 = none.
- **EX034 — Service agreement.** Draft one consumer service agreement line. *Rubric:* 3 = consumer, content, format, speed, feedback; 2 = three; 1 = vague; 0 = none.
- **EX035 — Integration measure.** Name two consumer-side measures of integration. *Rubric:* 3 = detections created, vulns reprioritised, risk updated, surveys; 2 = one; 1 = indicators ingested; 0 = none.

### Synthesis

Integrate CTI at defined points, enforce TLP with a fail-closed gate, agree service levels and measure consumer action.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Threat intelligence and OSINT: difficult cases

### Learning outcomes

You will (1) handle attribution pressure; (2) manage intelligence about insiders; (3) respond to unverified public claims of breach; (4) work under incomplete information during crises.

### 8.1 Attribution pressure

Executives and media want a name. For most defensive decisions, the techniques and infrastructure matter more than the identity. When attribution is offered, state the evidence, alternatives and confidence; distinguish "activity cluster resembling public reporting on a group" from "the group did it". The Diamond Model separates adversary from capability and infrastructure precisely because those can be shared or sold. At NLG, leadership wanted a name for the extortion group, but the decisions in front of them concerned supplier access and segmentation, not identity. Rafael's report described the activity, compared it with public reporting at stated confidence, and focused on techniques NLG could defend against. Naming a group would not have changed those decisions, and a wrong name could have misled them.

### 8.2 Insider cases

Intelligence suggesting an insider must go to human resources and legal under a defined procedure. CTI analysts should not monitor colleagues informally; it may be unlawful and undermines trust. Keep such material on a strict need-to-know basis. At NLG, the ACH matrix kept insider misuse as a hypothesis, but Rafael did not investigate colleagues himself. Evidence relevant to an insider would go to human resources and legal under the defined procedure, and only those with a need to know would see it. This protects any formal investigation and keeps staff trust in the CTI team intact.

### 8.3 Public claims of breach

A leak-site post claims NLG data. Steps: preserve the claim passively (screenshot from a safe, approved environment or through a contracted provider), assess plausibility from any sample against internal records, inform incident response and legal, and avoid public comment. Do not download large "samples" onto corporate systems without legal advice. When a leak site claimed 200 GB of NLG customs data, the contracted provider retrieved the listing, and the file names matched a decommissioned test environment. Rafael's update gave moderate confidence and said incident response was verifying. Legal handled any notifications, and nobody at NLG commented publicly while the claim was being checked.

### 8.4 Crisis tempo

During incidents, analysts publish short updates with explicit confidence and time stamps, superseding earlier ones clearly. Wrong early statements are normal; unmarked corrections are not. During the leak-site claim, Rafael's updates each carried a time and confidence level, and later updates said clearly which earlier statement they replaced. Short updates kept leadership informed without waiting for a full assessment. If an early update turns out wrong, the correction states what changed and why.

Each update is stored in order in the incident record, so the sequence of statements can be reviewed afterwards against what was later confirmed.

### 8.5 Partner sensitivity

If the compromise came through a supplier, coordinate disclosure through FPSC and contracts rather than naming them publicly. Naming a supplier publicly before facts are confirmed could damage a relationship NLG depends on and expose the supplier to unfair blame. Contracts set out how incidents are reported between the parties, and FPSC gives a trusted channel for warning other members. Rafael coordinates with legal on any disclosure, including what FPSC members are told and when.

Supplier names appear only in AMBER+STRICT material until the supplier and legal agree otherwise.

### 8.6 Wellbeing

Difficult cases are stressful. Rotate on-call duties and debrief afterwards; tired analysts make worse judgments. NLG's CTI team is small, so a long incident can fall on one or two people. Rafael rotates on-call duties, ends each difficult case with a short debrief and makes sure analysts take time off after intense periods. He treats this as part of quality, since tired analysts misjudge evidence.

After the leak-site claim, the debrief covered what went well and what the team would change, and Rafael gave the two analysts on call a day off in lieu.

### Worked example

A leak site claims 200 GB of NLG customs data. A contracted provider retrieves the listing. The published file names match an old test environment decommissioned last year. Rafael's update: "Claim likely relates to a legacy test system (moderate confidence); no evidence yet of production data exposure; incident response is verifying." Legal handles notifications.

> **Synthetic case.** The claim and data are invented.

### Errors and limits

Absence of evidence early in a crisis is weak; keep assessments provisional.

### Exercises

- **EX036 — Cluster wording.** Rewrite "Group X attacked NLG" to reflect moderate evidence. *Rubric:* 3 = activity resembles public reporting on X; moderate confidence; alternatives; 2 = partial; 1 = unchanged; 0 = none.
- **EX037 — Insider routing.** Where must insider-related intelligence go, and why not to CTI monitoring? *Rubric:* 3 = HR/legal under procedure; informal monitoring unlawful/trust; 2 = partial; 1 = CTI investigates; 0 = none.
- **EX038 — Leak-site steps.** List four steps after a leak-site claim. *Rubric:* 3 = preserve passively, assess plausibility, inform IR/legal, no public comment; 2 = three; 1 = one; 0 = none.
- **EX039 — Crisis corrections.** How should a wrong early crisis update be corrected? *Rubric:* 3 = new timestamped update explicitly superseding; 2 = partial; 1 = silent edit; 0 = none.
- **EX040 — Supplier naming.** Why avoid naming the supplier publicly? *Rubric:* 3 = coordinate via FPSC/contracts; fairness, legal, trust; 2 = partial; 1 = name them; 0 = none.

### Synthesis

Resist premature attribution, route insider matters properly, assess leak claims carefully and correct openly in crises.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Threat intelligence and OSINT: leadership and assurance

### Learning outcomes

You will (1) lead a CTI team; (2) assure analytic quality with review processes; (3) report to boards; (4) build a sustainable programme.

### 9.1 Leading analysts

Analysts need clear requirements, time for depth, and protection from constant interruption. A leader shields the team from ad hoc requests by routing them through the requirements process. At NLG, requests from executives arrived by email and in corridors, pulling analysts away from planned work. Rafael routes every request through the requirements process, where it is scoped and prioritised. Analysts get protected time for deeper work, and requesters get a clear answer about when to expect results.

Urgent requests still reach the team quickly, but they are logged so their volume is visible.

### 9.2 Quality assurance

Use ICD 203 standards as a review checklist: sourcing described, uncertainty expressed, assumptions separated from judgments, alternatives considered, relevant and logical. Every assessment above routine level gets a second reader. Track how often reviews change conclusions. After three months of Rafael's review log, second readers changed the confidence level in 30% of assessments and the main judgment in 5%. He uses these figures to show the board that review adds value, and to find where analysts most often need help.

The checklist is kept short so second readers use it every time.

### 9.3 Calibration over time

Record probability judgments and later outcomes; compute how often "likely" events happened. Calibration feedback improves judgment more than training slides. Rafael starts a simple record of every probability judgment his team makes, such as likely or unlikely, with the date and the outcome when it becomes known. After enough judgments, the team can see whether its likely really happens more often than its unlikely. He discusses results in team meetings without blaming individuals, since the aim is better-calibrated words for the whole team.

### 9.4 Board reporting

Boards need a short view: what threats matter, how NLG's exposure is changing, what decisions intelligence informed, and what is uncertain. Avoid dramatic imagery and lists of actors. At NLG, Rafael's board report covered the threats most relevant to logistics, changes in exposure such as supplier access, and two decisions intelligence informed: segmentation funding and supplier access restrictions. It also stated what remained uncertain, such as the leading explanation for the data theft. The board could see the function's value from those decisions without reading technical detail.

### 9.5 Sustainability

Document processes, cross-train, keep a budget line, and show value with outcome measures. Programmes built around one person collapse when that person leaves. Rafael documents NLG's processes, trains the analyst who will succeed him and keeps a budget line for FPSC membership and the platform. When he was promoted, the handover worked because these were in place: six months later, the decision-record practice continued without him.

He also keeps the source catalogue and platform documentation current, so a new analyst can start without needing him. The cross-training plan pairs each process with a second person who has carried it out at least once under supervision.

### 9.6 External assurance

Occasional peer review by another FPSC member's CTI lead — under a mutual non-disclosure agreement — gives an outside view of method quality. A CTI lead from another FPSC member reviews a sample of NLG assessments against ICD 203 standards and gives written feedback. The mutual non-disclosure agreement protects both organisations' material, including anything shared at AMBER. Rafael records the findings and actions, and offers the same review in return.

The review covers method quality, not NLG's internal incidents, so it can be arranged without sharing sensitive operational detail. Rafael schedules it once a year, and the first review recommended clearer statements of assumptions.

### Hiring and development

Hire for curiosity, writing and judgment as much as for tool skills; tools change faster than habits of mind. Give each analyst a development plan with one analytic skill, one technical skill and one domain topic per year, such as logistics operations or customs systems. Pairing junior analysts with reviewers on real products teaches faster than courses alone, and rotating analysts briefly through incident response keeps their work grounded in operational reality.

### Worked example

Rafael introduces a review log. After three months, second readers changed the confidence level in 30% of assessments and the main judgment in 5%. He presents these figures to the board as evidence that review adds value, alongside two decisions intelligence informed: segmentation funding and supplier access restrictions.

> **Synthetic case.** The figures are invented.

### Errors and limits

Quality checklists can become box-ticking; rotate reviewers and discuss real cases.

### Exercises

- **EX041 — Request shielding.** How does a leader protect analysts from ad hoc requests? *Rubric:* 3 = route through requirements process/prioritise; 2 = partial; 1 = accept all; 0 = none.
- **EX042 — Review checklist.** Name four ICD 203-based review checks. *Rubric:* 3 = four valid standards; 2 = three; 1 = one; 0 = none.
- **EX043 — Calibration method.** Describe how to measure analysts' calibration. *Rubric:* 3 = record judgments with probabilities, compare outcome frequencies per band; 2 = partial; 1 = survey; 0 = none.
- **EX044 — Board content.** What four things should a board CTI report cover? *Rubric:* 3 = threats, exposure change, decisions informed, uncertainty; 2 = three; 1 = actor list; 0 = none.
- **EX045 — Review value.** Interpret the review-log figures. *Rubric:* 3 = review often adjusts confidence, rarely main judgment; adds value; 2 = partial; 1 = wasteful; 0 = none.

### Synthesis

Lead through requirements, assure quality with standards-based review and calibration, report clearly to boards and build for continuity.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) read academic and practitioner CTI research critically; (2) evaluate methods and data; (3) assess transferability to your organisation; (4) write a structured critique.

### 10.1 Types of source

Peer-reviewed papers, standards (STIX, TAXII, SP 800-150), government guidance (ICD 203), foundational practitioner papers (Hutchins et al.; Caltagirone et al.) and vendor reports differ in review, incentives and evidence. Know which you are reading. Rafael's team reads each type of source differently, with its incentives in mind. Peer-reviewed papers explain their method; standards define formats but not effectiveness; government guidance sets analytic standards; practitioner papers give models; vendor reports may be shaped by commercial interest. When the team read a vendor study claiming its feed detects 90% of threats, they checked its method before trusting the claim.

### 10.2 Method questions

What data was used, from where, over what period? How were labels created? What comparison was made? Are results reproducible? Could the authors' interests shape the conclusion? Applied to the vendor study, these questions showed that threats were defined as items in the vendor's own catalogue, so the 90% figure measured the feed against itself. The team could not reproduce the result outside the vendor. Rafael records the answers to each question when the team reviews a source, so later readers can see why it was trusted or not.

### 10.3 Transferability

A study on a large technology company's feeds may not transfer to a mid-sized logistics firm. Ask whether populations, threat exposure and resources are similar. Before applying any study's results at NLG, Rafael's team asks whether the studied organisations face similar threats, use similar tools and have similar staff. A finding about a large technology company's feed may not hold for a logistics firm with a small CTI team. Where transfer is uncertain, the team tests the idea on NLG's own data first.

### 10.4 Reading foundational models critically

The kill chain was written for intrusion campaigns against defence contractors; it fits insider or cloud-identity attacks less well. The Diamond Model is a framework for organising events, not a method that produces conclusions by itself. ATT&CK reflects publicly reported behaviour, biased toward what vendors observe. At NLG, the kill chain helps describe a ransomware intrusion but fits poorly for supplier credential misuse. Rafael uses the Diamond Model to organise events from the data theft, but conclusions still come from ACH. ATT&CK frequencies in his project are labelled as reflecting reported behaviour, not all activity.

### 10.5 Structured critique

Summary, contribution, method strengths, method weaknesses, transferability, and what you would do with it. Keep tone professional. Rafael's team writes a one-page critique of each paper read in the monthly group, following this structure. The vendor study critique concluded that its claim was unverifiable externally, and the team decided not to rely on it in procurement. Critiques are stored with the source catalogue, so future readers find the team's view next to the source.

Critiques avoid personal comments about authors and focus on whether the method supports the claims.

### 10.6 Building a reading habit

A monthly reading group of two papers keeps the team current. Each session ends with one change to try or a reason not to. At NLG, the group meets monthly and picks papers related to current requirements, such as technique frequency or triage evaluation. Ending each session with one change to try links reading to practice. Rafael records the changes tried and whether they helped, so the group can see which papers influenced NLG's work.

Analysts take turns choosing papers, so the reading reflects different parts of the team's work.

### Finding good sources

Use scholarly databases and conference proceedings for peer-reviewed work, standards bodies for specifications and official guidance, and reputable practitioner venues for applied studies. Record why each source was selected, and prefer primary sources over summaries that may distort them.

### Worked example

Rafael's team reads a vendor study claiming its feed "detects 90% of threats". The method section defines threats as items in the vendor's own catalogue — a circular measure. The team notes the claim is unverifiable externally and decides not to rely on it in procurement.

> **Synthetic case.** The vendor study is invented.

### Errors and limits

Critique is easier than building; pair every criticism with a constructive suggestion.

### Exercises

- **EX046 — Circular claim.** Explain why the vendor's 90% figure is circular. *Rubric:* 3 = threats defined by own catalogue; self-referential; 2 = partial; 1 = valid; 0 = none.
- **EX047 — Method checklist.** List five method questions for a CTI study. *Rubric:* 3 = data, source/period, labels, comparison, reproducibility/interests; 2 = three; 1 = one; 0 = none.
- **EX048 — Kill chain fit.** For which attack types does the kill chain fit poorly? *Rubric:* 3 = insider, cloud-identity abuse; reason; 2 = one; 1 = vague; 0 = none.
- **EX049 — Transfer test.** What should you compare before applying a study's results to NLG? *Rubric:* 3 = population, exposure, resources similarity; 2 = two; 1 = vague; 0 = none.
- **EX050 — Diamond role.** Is the Diamond Model a method that produces conclusions? Explain. *Rubric:* 3 = no, organising framework; analysis supplies conclusions; 2 = no; 1 = yes; 0 = none.

### Synthesis

Read sources by type, interrogate methods, check transferability and critique constructively.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) deliver a scoped CTI improvement project at work; (2) apply evaluation methods from earlier chapters; (3) manage stakeholders and ethics; (4) report outcomes honestly.

### 11.1 Choosing the project

Rafael's project: build an intelligence-driven detection backlog. Using ATT&CK-coded FPSC reports and NLG incidents, rank techniques by sector frequency, NLG exposure and current detection coverage, then deliver the top ten as detection requirements to the operations centre. The project answers a decision the operations centre faces each quarter: which detections to build next. Ranking by sector frequency, NLG exposure and current coverage combines intelligence with knowledge of NLG's own systems. Delivering ten requirements rather than a long list keeps the backlog realistic for the detection team.

### 11.2 Scope and ethics

In scope: public and FPSC reports (respecting TLP), internal incident summaries, current detection inventory. Out of scope: offensive testing, adversary infrastructure interaction, personal data beyond what incidents already hold. Respecting TLP means FPSC content marked AMBER or AMBER+STRICT stays out of anything shared beyond permitted recipients, including the academic report. Excluding offensive testing and adversary infrastructure keeps the project within NLG's collection policy. Personal data is limited to what incident records already hold, as the privacy officer agreed.

The privacy officer signs off the scope before coding begins.

### 11.3 Method

Code reports to techniques with a second coder on a sample; compute frequencies; score exposure with asset owners; mark coverage as none, partial or full with the detection team. Combine scores transparently. A second coder on a sample checks that technique coding is consistent, and disagreements are discussed and recorded. Asset owners score exposure because they know which systems face the internet or suppliers. The detection team marks coverage because it knows what rules exist. Rafael publishes the scoring formula with the backlog, so anyone can see why an item ranked where it did.

### 11.4 Evaluation

Success measures: number of backlog items implemented within the term; detection coverage change; time from intelligence to detection requirement. Compare with the previous quarter. Each measure tests a different part of the project's value: implementation shows whether the operations centre used the backlog, coverage change shows whether NLG can see more techniques, and time to requirement shows whether intelligence reaches detection faster. Comparing with the previous quarter gives a baseline, and Rafael reports counts rather than percentages alone.

Rafael set these measures with the operations lead before work began.

### 11.5 Stakeholders

Agree with the operations lead how many requirements the team can absorb. Ten realistic items beat thirty ignored ones. The operations lead knows how many detections the team can build in a term. Agreeing the number in advance means the backlog is sized to capacity, and items that are not delivered are visible as carried over rather than quietly dropped. Rafael and the lead review progress fortnightly, and seven of the ten items shipped within the term.

The operations lead also agrees which detections need testing time in the shared calendar.

### 11.6 Reporting

The final report states what was delivered, measured effects, limits and next steps. Restricted FPSC content stays out of the academic version. Rafael's report states that seven of ten items shipped, describes the coverage change, and lists limits such as the small sample of coded reports. Next steps include the remaining three items, which carry over to the next quarter's backlog. The academic version describes FPSC reporting only in general terms, so no restricted content leaves NLG and FPSC.

His supervisors review both the academic and the executive versions before submission.

### Safe detection testing

Testing new detections should use approved, harmless simulations — for example, an administrator performing a scripted unusual login from a test account — scheduled with the operations team and recorded in advance so nobody mistakes the test for a real incident.

### Worked example

Coding 40 reports yields Valid Accounts (T1078) and Remote Services (T1021) as high-frequency techniques with partial coverage at NLG. Exploit Public-Facing Application (T1190) has low frequency but high exposure because of the customs portal. The backlog places T1078 anomalies, supplier remote-service monitoring and portal exploitation alerts in the top three. Seven of ten items ship within the term.

> **Synthetic case.** The counts and outcomes are invented.

### Errors and limits

Coverage self-assessments are optimistic; test detections with safe simulations approved by the operations team.

### Exercises

- **EX051 — Ranking factors.** Which three factors ranked the backlog? *Rubric:* 3 = sector frequency, NLG exposure, detection coverage; 2 = two; 1 = one; 0 = none.
- **EX052 — Low-frequency item.** Why did T1190 rank high despite low frequency? *Rubric:* 3 = customs portal exposure; 2 = partial; 1 = random; 0 = none.
- **EX053 — Absorbable backlog.** Why agree capacity with the operations lead? *Rubric:* 3 = realistic delivery; ignored items waste effort; 2 = partial; 1 = unnecessary; 0 = none.
- **EX054 — Success measures.** Give two measurable success criteria for the project. *Rubric:* 3 = items implemented, coverage change, time to requirement; 2 = one; 1 = vague; 0 = none.
- **EX055 — Academic version.** What must be removed from the academic report? *Rubric:* 3 = restricted FPSC/TLP content; sensitive NLG detail; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Scope a useful project, use transparent scoring, agree capacity, measure outcomes and keep restricted material out of academic outputs.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) consolidate the course's methods into a personal practice framework; (2) transfer them to new organisations or sectors; (3) plan continuing development; (4) hand over a programme responsibly.

### 12.1 A personal framework

Summarise your practice on one page: decision-first requirements (chapter 1), sourcing mix (2), ACH and calibration (3, 9), risk and ethics governance (4), standards-based design (5), controlled evaluation (6), TLP-enforced integration (7), crisis discipline (8), research critique (10). Rafael's own page follows this outline, with an example from NLG for each item: the segmentation decision for requirements, FPSC and incident review for sourcing, the data-theft matrix for ACH, the leak-site case for crisis discipline, and the vendor study for critique. The page becomes part of his handover pack, so his successor sees the method as well as the records.

### 12.2 Transfer

Moving to another sector changes threats, regulators and communities but not the method. A healthcare or energy organisation will need sector-specific sharing communities and safety considerations, but requirements, evaluation and TLP discipline transfer intact. Rafael notes that NLG's own method came from general CTI practice adapted to logistics: the requirements process, ACH and TLP gates would work unchanged in another sector. What changes is the community, the threats that matter and regulators' expectations. A healthcare organisation would also need to consider patient safety when deciding what to share and how quickly.

### 12.3 Continuing development

Follow ATT&CK and STIX updates, take part in community working groups, read research, and track your own calibration. Mentoring others consolidates learning. Rafael's plan after promotion includes staying in FPSC working groups and continuing the calibration record he started for the team. He mentors the analyst who took over the CTI function, which also helps him reflect on what worked. Updates to ATT&CK and STIX are reviewed for changes that affect NLG's platform or detection backlog.

He reviews his calibration record each year to see where his estimates drifted.

### 12.4 Handover

If you leave, hand over requirements, source catalogue, platform documentation, decision records, review logs and community contacts with introductions. Transfer TLP-restricted relationships properly; memberships are often organisational, not personal. When Rafael handed over NLG's CTI function, the pack included all of these, and he introduced his successor to FPSC contacts in person during a two-week overlap. FPSC confirmed the new analyst's access under the existing membership. Six months later the decision-record practice continued, which showed the handover had worked.

He also leaves notes on open requirements and who asked for each one.

### 12.5 Reflecting on limits

CTI informs decisions under uncertainty; it rarely delivers certainty. Mature practitioners are comfortable saying "we do not know" and explaining what would reduce uncertainty. In the data-theft case, Rafael's report said the leading explanation was supplier compromise at low-to-moderate confidence and named what would reduce the uncertainty: the supplier's VPN log. Leadership could act on supplier access restrictions without waiting for certainty. Saying what is unknown made the assessment more useful, not less.

Rafael asks his successor to keep this habit, and to write the missing evidence into every assessment so readers know what could change it.

### 12.6 Final assessment

The course closes with a portfolio: the decision record set, an ACH product, an evaluation report and the project report, each reviewed against ICD 203 standards. Each piece of the portfolio shows a different skill from the course. The decision records show requirements tied to decisions; the ACH product shows structured analysis; the evaluation report shows controlled comparison; the project report shows integration with detection. Rafael's portfolio uses his NLG work, with restricted FPSC content removed before assessment.

Rafael's tutor reviews the portfolio against the assessment criteria before it is submitted.

### Mentoring the next lead

Teaching the method to a successor tests whether it is written down clearly. Rafael's successor drafts the next quarter's requirements while he reviews; gaps in documentation surface quickly and are fixed before he leaves. A short checklist of recurring tasks with owners and dates completes the transfer.

### Worked example

Rafael is promoted to lead security across NLG. He hands the CTI function to an analyst he trained, with a two-week overlap. The handover pack includes FPSC introductions; FPSC confirms the new analyst's access under the existing membership. Six months later, the decision-record practice continues without him.

> **Synthetic case.** The promotion and handover are invented.

### Errors and limits

Frameworks age; review yours annually.

### Exercises

- **EX056 — One-page framework.** Draft your own one-page CTI practice framework with five elements. *Rubric:* 3 = five elements tied to chapters; 2 = three; 1 = list of tools; 0 = none.
- **EX057 — Sector transfer.** What changes and what stays when moving CTI practice to healthcare? *Rubric:* 3 = threats/communities/regulators change; method stays; 2 = partial; 1 = everything changes; 0 = none.
- **EX058 — Membership transfer.** Why must community memberships be transferred formally? *Rubric:* 3 = memberships organisational; TLP trust/agreements; 2 = partial; 1 = personal; 0 = none.
- **EX059 — Handover pack.** List five handover items. *Rubric:* 3 = five of requirements, sources, platform docs, decision records, review logs, contacts; 2 = three; 1 = one; 0 = none.
- **EX060 — Saying unknown.** Why is "we do not know" a mature answer? *Rubric:* 3 = honest uncertainty plus path to reduce it; 2 = partial; 1 = weakness; 0 = none.

### Synthesis

Consolidate a personal framework, transfer method across sectors, keep learning and hand over responsibly.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Northmere Logistics Group, Rafael Moreau, the Freight and Ports Sharing Community and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Example: "By 30 June, for the CIO's remote-access renewal, which initial-access techniques have been used against logistics companies in the last 12 months?"

**EX002.** When every plausible finding would lead to the same decision — for example, a control already committed regardless of the threat picture.

**EX003.** "An extortion attempt against NLG within 12 months is likely (55–80%); a successful one would disrupt warehouse operations for two to five days; moderate confidence."

**EX004.** The decision taken, its date, the intelligence relied on, that intelligence's confidence, and who made the decision.

**EX005.** Strategic readers need trends over years and little detail; tactical readers need indicators within hours. A weekly mix is too slow for one and too granular for the other.

**EX006.** Internal telemetry and incident records, because they show what actually targeted or reached the organisation.

**EX007.** Automation ingests and deduplicates well; it judges relevance to the business poorly.

**EX008.** Adversaries change techniques more slowly and at greater cost than hashes or addresses, so behaviour-based detections stay useful longer.

**EX009.** It counts activity rather than outcomes; large volumes can mean noise, not protection.

**EX010.** Without defined requirements he cannot judge a feed's relevance, peers dropped similar feeds for that reason, and a small proven programme justifies later spending.

**EX011.** H3 supplier compromise 0 inconsistent; H1 criminal extortion crew 1; H2 insider misuse 2. H3 leads.

**EX012.** E2, data staged at 02:00, because it is consistent with all three hypotheses and so cannot distinguish them.

**EX013.** E1, the supplier VPN login; if it is wrong, H1 and H3 tie, so it carries the ranking.

**EX014.** Tool names or language strings left in files: easy to insert to suggest a different group.

**EX015.** H3 leads H1 by a single inconsistency and its key supporting evidence is not yet verified.

**EX016.** Base each likelihood on cited intelligence — sector techniques, actor interest in logistics, NLG exposure — with confidence, and revisit when it changes.

**EX017.** A lawful basis with a documented legitimate-interests balancing test, purpose limitation, data minimisation, retention limits and a data-protection impact assessment.

**EX018.** Payment may fund criminals; buying may be unlawful; it creates another copy of personal data that NLG must then protect.

**EX019.** A lawful assessment of the extortion group's typical behaviour, plus evidence preservation and support to law enforcement.

**EX020.** It lets new methods be judged carefully once and then used routinely, avoiding both improvised risky collection and endless delay.

**EX021.** Centralised teams keep methods consistent but drift from operational needs; embedded analysts stay close to consumers but may lose shared method.

**EX022.** STIX 2.1 support, TAXII 2.1 support, TLP enforcement and integration with detection tools (also cost and maintainability).

**EX023.** Extensions keep objects valid under the standard so they can still be exchanged with partners.

**EX024.** Put the TLP label in the subject line and in the body, as TLP 2.0 advises for email.

**EX025.** The staff time and skills needed to install, update and maintain the platform.

**EX026.** Rule A: precision 0.6, recall 1.0 (tp 6, fp 4, fn 0). Rule B: precision 1.0, recall 0.67 (tp 4, fp 0, fn 2).

**EX027.** When missing a relevant item is expensive — such as a vulnerability in a critical platform — and analysts can absorb extra false alarms.

**EX028.** Knowing which rule flagged an item can bias labels toward or against that rule.

**EX029.** Both misses concerned a supplier product missing from the inventory; updating the inventory is the fix.

**EX030.** Results are uncertain and could shift with a few items; treat them as provisional and repeat with more data.

**EX031.** R2 (AMBER to public — beyond AMBER's audience), R3 (AMBER+STRICT to a client — limited to the organisation) and R5 (label "AMBER" unrecognised, so fail closed).

**EX032.** Guessing will eventually release restricted partner material and destroy trust; blocking and asking costs only a short delay.

**EX033.** Rafael asked FPSC for a version releasable to the customer; FPSC issued a sanitised TLP:GREEN summary.

**EX034.** "Security operations centre: validated FPSC indicators in STIX via the platform within four hours; feedback through the weekly review."

**EX035.** Detections created from intelligence and vulnerabilities reprioritised because of exploitation reports.

**EX036.** "The activity resembles public reporting on Group X (moderate confidence); shared tooling or imitation could explain the overlap."

**EX037.** To human resources and legal under the insider procedure; informal monitoring by CTI may breach employment and privacy law and damage trust.

**EX038.** Preserve the claim through an approved passive method, assess plausibility against internal records, inform incident response and legal, and make no public comment.

**EX039.** Issue a new time-stamped update that explicitly states it supersedes the earlier one and what changed.

**EX040.** Disclosure should be coordinated through FPSC and contracts; public naming risks unfairness, legal exposure and loss of partner trust.

**EX041.** By routing all requests through the requirements process, where they are prioritised against existing commitments.

**EX042.** Sources described, uncertainty expressed and explained, assumptions distinguished from judgments, and alternatives analysed.

**EX043.** Log each judgment with its probability band, later record whether the event happened, and compare actual frequencies with the bands.

**EX044.** Relevant threats, how NLG's exposure is changing, decisions intelligence informed, and key uncertainties.

**EX045.** Review frequently corrects confidence (30%) and occasionally the main judgment (5%), showing it improves products at modest cost.

**EX046.** The study counts as "threats" only what the vendor already catalogues, so detection is measured against its own definition.

**EX047.** What data, from which sources and period; how labels were made; what comparison was used; whether it can be reproduced; and whether authors' interests could shape findings.

**EX048.** Insider misuse and cloud-identity attacks, which skip phases such as delivery and exploitation.

**EX049.** Whether the studied organisations resemble NLG in size, sector threat exposure and security resources.

**EX050.** No. It organises events into adversary, capability, infrastructure and victim; conclusions come from the analyst's reasoning over that structure.

**EX051.** Technique frequency in sector reporting, NLG's exposure, and current detection coverage.

**EX052.** NLG's internet-facing customs portal makes exploitation of public applications highly relevant despite few sector reports.

**EX053.** Agreeing capacity keeps the backlog deliverable; items beyond the team's capacity would be ignored and waste analysis effort.

**EX054.** Number of backlog items implemented during the term and the change in detection coverage for ranked techniques.

**EX055.** Any FPSC material not released for publication and sensitive details of NLG systems.

**EX056.** Example: decision-first requirements; sourcing mix led by internal data; ACH with calibrated confidence; fail-closed TLP dissemination; quarterly controlled evaluation of triage.

**EX057.** Threat actors, sharing communities, regulators and safety concerns change; requirements, evaluation, analytic standards and TLP discipline stay.

**EX058.** Memberships and sharing agreements belong to the organisation and depend on trust; access must be re-authorised through the community.

**EX059.** Requirements list, source catalogue, platform documentation, decision records and community contacts with introductions (also review logs).

**EX060.** It states uncertainty honestly and, paired with what would resolve it, guides further collection instead of encouraging false confidence.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- Bianco, D. (2013). The Pyramid of Pain. <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>
- Caltagirone, S., Pendergast, A. and Betz, C. (2013). The Diamond Model of Intrusion Analysis. Technical Report ADA586960, Center for Cyber Intelligence Analysis and Threat Research. <https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf>
- European Union. Regulation (EU) 2016/679 (General Data Protection Regulation). <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- FIRST. Traffic Light Protocol (TLP) version 2.0. <https://www.first.org/tlp/>
- Heuer, R. J. (1999). Psychology of Intelligence Analysis. CIA Center for the Study of Intelligence. <https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/>
- Hutchins, E. M., Cloppert, M. J. and Amin, R. M. (2011). Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains. Lockheed Martin. <https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf>
- Kent, S. (1964). Words of Estimative Probability. CIA Studies in Intelligence. <https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf>
- MITRE ATT&CK Enterprise matrix, groups, software and technique pages. <https://attack.mitre.org/>
- NIST SP 800-150 (2016). Guide to Cyber Threat Information Sharing. <https://doi.org/10.6028/NIST.SP.800-150>
- NIST SP 800-61 Rev. 3 (2025). Incident Response Recommendations and Considerations for Cybersecurity Risk Management. <https://doi.org/10.6028/NIST.SP.800-61r3>
- OASIS. STIX Version 2.1 (Committee Specification / OASIS Standard). <https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html>
- OASIS. TAXII Version 2.1. <https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html>
- ODNI. Intelligence Community Directive 203: Analytic Standards (2015, amended 2022). <https://www.odni.gov/files/documents/ICD/ICD-203.pdf>
