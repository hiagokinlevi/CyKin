# Threat Intelligence and OSINT: A Postgraduate Book

- Language: English (`en`); postgraduate course, two years.
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, with outputs embedded from real runs. Independent review and the 300-page A4 verification remain open.
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

A CTI function earns its budget when it changes decisions: what to patch first, which supplier connection to restrict, whether to pay for a new detection capability. Rafael starts NLG's programme by interviewing decision-makers — the chief operating officer, the head of infrastructure, the customs-platform owner — and listing the decisions they face in the next year.

Section one point one develops advanced security decision-making with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section one point one, FPSC expects advanced claims to carry owners and dates.

### 1.2 Requirements tied to decisions

Each decision becomes a requirement: "Before the Q3 renewal of remote-access tooling, which access techniques are adversaries using against logistics firms?" A good requirement names the decision, the deadline and the consumer. Topic lists ("ransomware", "APT groups") cannot be closed and never end.

Section one point two develops advanced security decision-making with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section one point two, FPSC expects advanced claims to carry owners and dates.

Section one point two treats decisions first requirements tied as testable only when evidence and ticket IDs are recorded.

### 1.3 Expected loss, roughly

Decision-makers compare options. Rough expected-loss reasoning — likelihood band multiplied by impact range — helps them, as long as bands stay bands. "Likely (55–80%) attempt within a year; impact two to five days of warehouse disruption" supports a choice better than a single invented number.

Section one point three develops advanced security decision-making with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section one point three, FPSC expects advanced claims to carry owners and dates.

Section one point three treats decisions first requirements tied as testable only when evidence and ticket IDs are recorded.

### 1.4 Value of information

Before collecting, ask whether any plausible answer would change the decision. If the board will fund multi-factor authentication for all remote access regardless, further intelligence on the threat adds little decision value; effort should move elsewhere.

Section one point four develops advanced security decision-making with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section one point four, FPSC expects advanced claims to carry owners and dates.

Section one point four treats decisions first requirements tied as testable only when evidence and ticket IDs are recorded.

### 1.5 Decision records

Record the decision, the date, the intelligence used, its confidence and who decided. Later reviews can then separate bad luck from bad judgment.

Section one point five develops advanced security decision-making with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section one point five, FPSC expects advanced claims to carry owners and dates.

Section one point five treats decisions first requirements tied as testable only when evidence and ticket IDs are recorded.

For section one point five, Northmere Logistics Group will not accept advanced work without a written trail.

### 1.6 Time horizons

Strategic decisions run over years, operational over weeks, tactical over hours. Each horizon needs different collection and a different cadence of reporting; mixing them in one weekly bulletin satisfies no one.

Section one point six develops advanced security decision-making with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section one point six, FPSC expects advanced claims to carry owners and dates.

Section one point six treats decisions first requirements tied as testable only when evidence and ticket IDs are recorded.

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

Mature teams run a requirements process, maintain a threat profile of relevant adversaries and techniques, feed detection engineering, support incident response and brief leadership. NIST SP 800-150 emphasises sharing relationships and clear rules for what can be shared. Many teams use a threat intelligence platform storing STIX 2.1 objects and exchanging them over TAXII 2.1.

Section two point one develops threat intelligence and osint current with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section two point one, FPSC expects threat claims to carry owners and dates.

### 2.2 Sourcing mix

Internal telemetry and incidents give the most relevant evidence. Communities like FPSC give sector context and early warning. Commercial providers add breadth and finished reporting. Open sources — advisories, vendor research, certificate logs — fill gaps when collected lawfully and within terms of service.

Section two point two develops threat intelligence and osint current with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section two point two, FPSC expects threat claims to carry owners and dates.

Section two point two treats what mature teams do as testable only when evidence and ticket IDs are recorded.

### 2.3 Automation

Automation ingests, deduplicates, enriches and distributes indicators. It does not judge relevance well, nor write assessments. Teams that automate everything flood defenders with low-value indicators; those that automate nothing drown in copy-paste.

Section two point three develops threat intelligence and osint current with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section two point three, FPSC expects threat claims to carry owners and dates.

Section two point three treats what mature teams do as testable only when evidence and ticket IDs are recorded.

### 2.4 Technique-centred practice

Following Bianco's Pyramid of Pain, mature teams invest in technique-level intelligence mapped to ATT&CK, because detections built on behaviour last longer than those built on hashes and addresses.

Section two point four develops threat intelligence and osint current with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section two point four, FPSC expects threat claims to carry owners and dates.

Section two point four treats what mature teams do as testable only when evidence and ticket IDs are recorded.

### 2.5 Starting small

A two-person team should pick a few requirements, one community, internal incident data and a modest platform — and prove value before expanding.

Section two point five develops threat intelligence and osint current with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section two point five, FPSC expects threat claims to carry owners and dates.

Section two point five treats what mature teams do as testable only when evidence and ticket IDs are recorded.

For section two point five, Northmere Logistics Group will not accept threat work without a written trail.

### 2.6 Common anti-patterns

Buying several feeds before defining requirements; publishing a daily newsletter nobody reads; measuring success by indicator volume; keeping intelligence inside the CTI team rather than embedding it in detection and response workflows.

Section two point six develops threat intelligence and osint current with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section two point six, FPSC expects threat claims to carry owners and dates.

Section two point six treats what mature teams do as testable only when evidence and ticket IDs are recorded.

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

Heuer's analysis of competing hypotheses asks analysts to list all reasonable hypotheses, score each piece of evidence against each, and favour the hypothesis with the least inconsistent evidence. It counters the habit of accepting the first plausible story.

Section three point one develops threat intelligence and osint specialist with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section three point one, FPSC expects threat claims to carry owners and dates.

Section three point one treats why ach reading the as testable only when evidence and ticket IDs are recorded.

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

Three hypotheses about a data theft at NLG are tested against five evidence items. Supplier compromise (H3) has no inconsistent evidence; criminal extortion (H1) has one; insider misuse (H2) has two. H3 is the leading hypothesis, but H1 is close.

Section three point two develops threat intelligence and osint specialist with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section three point two, FPSC expects threat claims to carry owners and dates.

Section three point two treats why ach reading the as testable only when evidence and ticket IDs are recorded.

### 3.3 Diagnosticity

Evidence consistent with every hypothesis — data staged at 02:00 (E2) — does not help choose. Diagnostic evidence discriminates: the login from the supplier VPN range (E1) is inconsistent with an external crew and neutral for an insider. Analysts should collect more diagnostic evidence rather than more evidence.

Section three point three develops threat intelligence and osint specialist with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section three point three, FPSC expects threat claims to carry owners and dates.

Section three point three treats why ach reading the as testable only when evidence and ticket IDs are recorded.

### 3.4 Deception and gaps

Adversaries plant false clues; tools are sold widely. Ask which evidence would be easy to fake and give it less weight. List what evidence is missing and what it would show.

Section three point four develops threat intelligence and osint specialist with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section three point four, FPSC expects threat claims to carry owners and dates.

Section three point four treats why ach reading the as testable only when evidence and ticket IDs are recorded.

### 3.5 Confidence

A one-point margin between H3 and H1 supports low-to-moderate confidence. ICD 203 asks analysts to explain the basis of confidence, including gaps.

Section three point five develops threat intelligence and osint specialist with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section three point five, FPSC expects threat claims to carry owners and dates.

Section three point five treats why ach reading the as testable only when evidence and ticket IDs are recorded.

For section three point five, Northmere Logistics Group will not accept threat work without a written trail.

### 3.6 Sensitivity

Ask which single evidence item, if wrong, would change the ranking. If E1's VPN attribution is mistaken, H1 and H3 tie. That tells Rafael where to verify first.

Section three point six develops threat intelligence and osint specialist with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section three point six, FPSC expects threat claims to carry owners and dates.

Section three point six treats why ach reading the as testable only when evidence and ticket IDs are recorded.

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

Risk registers often score likelihood by gut feeling. CTI can anchor the likelihood column: observed sector techniques, actors' known interest in logistics, and NLG's exposure. Each likelihood should cite the intelligence and its confidence, and be revisited when intelligence changes.

Section four point one develops advanced risk and ethics with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section four point one, FPSC expects advanced claims to carry owners and dates.

Section four point one treats threat in the risk as testable only when evidence and ticket IDs are recorded.

### 4.2 OSINT at scale

Monitoring public sources for brand abuse, leaked credentials or exposed NLG data touches personal data. Under the GDPR, NLG needs a lawful basis (often legitimate interests, with a documented balancing test), purpose limitation, minimisation and retention limits. A data-protection impact assessment is wise for systematic monitoring.

Section four point two develops advanced risk and ethics with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section four point two, FPSC expects advanced claims to carry owners and dates.

Section four point two treats threat in the risk as testable only when evidence and ticket IDs are recorded.

### 4.3 Collection governance

A collection policy lists approved sources and methods, prohibited ones (fake personas, purchasing stolen data, accessing closed criminal markets without legal approval), approval routes and audit. Analysts should know before a crisis what they may not do.

Section four point three develops advanced risk and ethics with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section four point three, FPSC expects advanced claims to carry owners and dates.

Section four point three treats threat in the risk as testable only when evidence and ticket IDs are recorded.

### 4.4 Purchasing stolen data

A vendor offers NLG's leaked customer database "for verification". Paying may fund criminals, may be unlawful and creates a new copy of personal data. The ethical path runs through legal counsel, law enforcement and incident response, not procurement.

Section four point four develops advanced risk and ethics with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section four point four, FPSC expects advanced claims to carry owners and dates.

Section four point four treats threat in the risk as testable only when evidence and ticket IDs are recorded.

### 4.5 Pressure

Executives under stress may ask for intrusive actions — "find out who the hacker is". Analysts need the policy and the confidence to say no, offering lawful alternatives.

Section four point five develops advanced risk and ethics with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section four point five, FPSC expects advanced claims to carry owners and dates.

Section four point five treats threat in the risk as testable only when evidence and ticket IDs are recorded.

For section four point five, Northmere Logistics Group will not accept advanced work without a written trail.

### 4.6 Ethics review

A small ethics panel — legal, privacy, security leadership — reviews new collection methods once, then approves them for routine use. This avoids both ad hoc risk-taking and paralysis.

Section four point six develops advanced risk and ethics with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section four point six, FPSC expects advanced claims to carry owners and dates.

Section four point six treats threat in the risk as testable only when evidence and ticket IDs are recorded.

For section four point six, Northmere Logistics Group will not accept advanced work without a written trail.

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

A centralised team serves everyone from one place and keeps standards consistent but can drift from operational needs. Embedded analysts sit in the security operations centre or risk team and stay close to consumers but may lose common method. Outsourced intelligence brings scale but limited business context. Hybrids are common.

Section five point one develops threat intelligence and osint design with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section five point one, FPSC expects threat claims to carry owners and dates.

### 5.2 Platform options

Options range from spreadsheets and a shared mailbox, through open-source threat intelligence platforms, to commercial platforms. Criteria: STIX 2.1 support, TAXII 2.1 client and server, TLP enforcement, integration with detection tools, cost and maintainability.

Section five point two develops threat intelligence and osint design with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section five point two, FPSC expects threat claims to carry owners and dates.

Section five point two treats organisational models platform options as testable only when evidence and ticket IDs are recorded.

### 5.3 Data model

Using STIX 2.1 internally keeps sharing simple: indicators, attack patterns, relationships and reports map directly to community exchange. Custom fields should use STIX extensions rather than ad hoc columns.

Section five point three develops threat intelligence and osint design with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section five point three, FPSC expects threat claims to carry owners and dates.

Section five point three treats organisational models platform options as testable only when evidence and ticket IDs are recorded.

### 5.4 Protocols

TAXII 2.1 collections let NLG pull from FPSC and publish to it. Email remains necessary for human-readable products, and must carry TLP labels in the subject and body as TLP 2.0 recommends.

Section five point four develops threat intelligence and osint design with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section five point four, FPSC expects threat claims to carry owners and dates.

Section five point four treats organisational models platform options as testable only when evidence and ticket IDs are recorded.

### 5.5 Design rationale

Record options, criteria, scores and the reason for the choice. Future leaders can revisit decisions when conditions change.

Section five point five develops threat intelligence and osint design with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section five point five, FPSC expects threat claims to carry owners and dates.

Section five point five treats organisational models platform options as testable only when evidence and ticket IDs are recorded.

For section five point five, Northmere Logistics Group will not accept threat work without a written trail.

### 5.6 Reversibility

Prefer designs that can be changed cheaply. A standards-based data model allows platform replacement later; proprietary formats lock data in.

Section five point six develops threat intelligence and osint design with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section five point six, FPSC expects threat claims to carry owners and dates.

Section five point six treats organisational models platform options as testable only when evidence and ticket IDs are recorded.

For section five point six, Northmere Logistics Group will not accept threat work without a written trail.

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

Claims such as "our triage rule catches what matters" need evidence. A controlled evaluation applies alternatives to the same labelled set and compares outcomes.

Section six point one develops threat intelligence and osint controlled with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section six point one, FPSC expects threat claims to carry owners and dates.

Section six point one treats why evaluate reading the as testable only when evidence and ticket IDs are recorded.

For section six point one, Northmere Logistics Group will not accept threat work without a written trail.

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

On twenty labelled synthetic items, rule A (broad keywords) finds all six relevant items but raises four false alarms: precision 0.6, recall 1.0. Rule B (match against NLG's asset inventory) raises no false alarms but misses two relevant items: precision 1.0, recall 0.67.

Section six point two develops threat intelligence and osint controlled with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section six point two, FPSC expects threat claims to carry owners and dates.

Section six point two treats why evaluate reading the as testable only when evidence and ticket IDs are recorded.

### 6.3 Which is better?

Neither in general. If analyst time is scarce and misses can be caught elsewhere, rule B fits. If missing a relevant item is costly — for example, a vulnerability in a customs platform — rule A, or B with a secondary check, fits. The choice depends on costs, not on one metric.

Section six point three develops threat intelligence and osint controlled with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section six point three, FPSC expects threat claims to carry owners and dates.

### 6.4 Fair comparison

Use the same items, labels made before seeing rule outputs, and labellers blind to which rule flagged what. Report sample size; twenty items gives wide uncertainty.

Section six point four develops threat intelligence and osint controlled with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section six point four, FPSC expects threat claims to carry owners and dates.

Section six point four treats why evaluate reading the as testable only when evidence and ticket IDs are recorded.

For section six point four, Northmere Logistics Group will not accept threat work without a written trail.

### 6.5 Error analysis

Read the misses. Rule B missed two items about a supplier product absent from the inventory — an inventory gap, not a rule flaw. Fixing the inventory may help more than changing the rule.

Section six point five develops threat intelligence and osint controlled with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section six point five, FPSC expects threat claims to carry owners and dates.

Section six point five treats why evaluate reading the as testable only when evidence and ticket IDs are recorded.

### 6.6 Repeating over time

Threats change; rerun the evaluation quarterly with fresh labelled items.

Section six point six develops threat intelligence and osint controlled with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section six point six, FPSC expects threat claims to carry owners and dates.

Section six point six treats why evaluate reading the as testable only when evidence and ticket IDs are recorded.

For section six point six, Northmere Logistics Group will not accept threat work without a written trail.

Section six point six fails closed if threat evidence is missing rather than guessing.

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

CTI feeds detection engineering (technique priorities), the security operations centre (indicators and context), incident response (adversary profiles during incidents, aligned with NIST SP 800-61r3), vulnerability management (exploitation intelligence) and risk (likelihood). Each needs a defined input format and owner.

Section seven point one develops threat intelligence and osint organizational with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section seven point one, FPSC expects threat claims to carry owners and dates.

Section seven point one treats integration points reading the as testable only when evidence and ticket IDs are recorded.

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

A GREEN report to the community is allowed; AMBER to the public is blocked; AMBER+STRICT to a client is blocked, because it is limited to the recipient organisation; CLEAR to the public is allowed. A label written "AMBER" without the TLP prefix is unrecognised, so the gate fails closed and blocks it.

Section seven point two develops threat intelligence and osint organizational with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section seven point two, FPSC expects threat claims to carry owners and dates.

### 7.3 Fail closed

When a label is missing or unknown, block and ask. A gate that guesses will sooner or later leak restricted partner material and damage trust in the community.

Section seven point three develops threat intelligence and osint organizational with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section seven point three, FPSC expects threat claims to carry owners and dates.

Section seven point three treats integration points reading the as testable only when evidence and ticket IDs are recorded.

### 7.4 Service agreements

Agree with each consumer what they receive, in what format, how fast and how they give feedback. For example, the operations centre gets validated indicators within four hours of FPSC receipt; leadership gets a monthly two-page brief.

Section seven point four develops threat intelligence and osint organizational with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section seven point four, FPSC expects threat claims to carry owners and dates.

Section seven point four treats integration points reading the as testable only when evidence and ticket IDs are recorded.

### 7.5 Measuring integration

Measure consumer actions: detections created from intelligence, vulnerabilities reprioritised, risk entries updated. Survey consumers twice a year.

Section seven point five develops threat intelligence and osint organizational with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section seven point five, FPSC expects threat claims to carry owners and dates.

Section seven point five treats integration points reading the as testable only when evidence and ticket IDs are recorded.

For section seven point five, Northmere Logistics Group will not accept threat work without a written trail.

### 7.6 Clients and partners

NLG serves customers who sometimes ask for threat information. TLP:AMBER allows sharing with clients on a need-to-know basis; AMBER+STRICT does not. Customer-facing teams must know the difference before passing anything on.

Section seven point six develops threat intelligence and osint organizational with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section seven point six, FPSC expects threat claims to carry owners and dates.

Section seven point six treats integration points reading the as testable only when evidence and ticket IDs are recorded.

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

Executives and media want a name. For most defensive decisions, the techniques and infrastructure matter more than the identity. When attribution is offered, state the evidence, alternatives and confidence; distinguish "activity cluster resembling public reporting on a group" from "the group did it". The Diamond Model separates adversary from capability and infrastructure precisely because those can be shared or sold.

Section eight point one develops threat intelligence and osint difficult with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eight point one, FPSC expects threat claims to carry owners and dates.

### 8.2 Insider cases

Intelligence suggesting an insider must go to human resources and legal under a defined procedure. CTI analysts should not monitor colleagues informally; it may be unlawful and undermines trust. Keep such material on a strict need-to-know basis.

Section eight point two develops threat intelligence and osint difficult with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eight point two, FPSC expects threat claims to carry owners and dates.

Section eight point two treats attribution pressure insider cases as testable only when evidence and ticket IDs are recorded.

### 8.3 Public claims of breach

A leak-site post claims NLG data. Steps: preserve the claim passively (screenshot from a safe, approved environment or through a contracted provider), assess plausibility from any sample against internal records, inform incident response and legal, and avoid public comment. Do not download large "samples" onto corporate systems without legal advice.

Section eight point three develops threat intelligence and osint difficult with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eight point three, FPSC expects threat claims to carry owners and dates.

### 8.4 Crisis tempo

During incidents, analysts publish short updates with explicit confidence and time stamps, superseding earlier ones clearly. Wrong early statements are normal; unmarked corrections are not.

Section eight point four develops threat intelligence and osint difficult with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eight point four, FPSC expects threat claims to carry owners and dates.

Section eight point four treats attribution pressure insider cases as testable only when evidence and ticket IDs are recorded.

For section eight point four, Northmere Logistics Group will not accept threat work without a written trail.

### 8.5 Partner sensitivity

If the compromise came through a supplier, coordinate disclosure through FPSC and contracts rather than naming them publicly.

Section eight point five develops threat intelligence and osint difficult with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eight point five, FPSC expects threat claims to carry owners and dates.

Section eight point five treats attribution pressure insider cases as testable only when evidence and ticket IDs are recorded.

For section eight point five, Northmere Logistics Group will not accept threat work without a written trail.

### 8.6 Wellbeing

Difficult cases are stressful. Rotate on-call duties and debrief afterwards; tired analysts make worse judgments.

Section eight point six develops threat intelligence and osint difficult with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eight point six, FPSC expects threat claims to carry owners and dates.

Section eight point six treats attribution pressure insider cases as testable only when evidence and ticket IDs are recorded.

For section eight point six, Northmere Logistics Group will not accept threat work without a written trail.

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

Analysts need clear requirements, time for depth, and protection from constant interruption. A leader shields the team from ad hoc requests by routing them through the requirements process.

Section nine point one develops threat intelligence and osint leadership with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section nine point one, FPSC expects threat claims to carry owners and dates.

Section nine point one treats leading analysts quality assurance as testable only when evidence and ticket IDs are recorded.

### 9.2 Quality assurance

Use ICD 203 standards as a review checklist: sourcing described, uncertainty expressed, assumptions separated from judgments, alternatives considered, relevant and logical. Every assessment above routine level gets a second reader. Track how often reviews change conclusions.

Section nine point two develops threat intelligence and osint leadership with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section nine point two, FPSC expects threat claims to carry owners and dates.

Section nine point two treats leading analysts quality assurance as testable only when evidence and ticket IDs are recorded.

### 9.3 Calibration over time

Record probability judgments and later outcomes; compute how often "likely" events happened. Calibration feedback improves judgment more than training slides.

Section nine point three develops threat intelligence and osint leadership with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section nine point three, FPSC expects threat claims to carry owners and dates.

Section nine point three treats leading analysts quality assurance as testable only when evidence and ticket IDs are recorded.

For section nine point three, Northmere Logistics Group will not accept threat work without a written trail.

### 9.4 Board reporting

Boards need a short view: what threats matter, how NLG's exposure is changing, what decisions intelligence informed, and what is uncertain. Avoid dramatic imagery and lists of actors.

Section nine point four develops threat intelligence and osint leadership with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section nine point four, FPSC expects threat claims to carry owners and dates.

Section nine point four treats leading analysts quality assurance as testable only when evidence and ticket IDs are recorded.

### 9.5 Sustainability

Document processes, cross-train, keep a budget line, and show value with outcome measures. Programmes built around one person collapse when that person leaves.

Section nine point five develops threat intelligence and osint leadership with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section nine point five, FPSC expects threat claims to carry owners and dates.

Section nine point five treats leading analysts quality assurance as testable only when evidence and ticket IDs are recorded.

For section nine point five, Northmere Logistics Group will not accept threat work without a written trail.

### 9.6 External assurance

Occasional peer review by another FPSC member's CTI lead — under a mutual non-disclosure agreement — gives an outside view of method quality.

Section nine point six develops threat intelligence and osint leadership with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section nine point six, FPSC expects threat claims to carry owners and dates.

Section nine point six treats leading analysts quality assurance as testable only when evidence and ticket IDs are recorded.

For section nine point six, Northmere Logistics Group will not accept threat work without a written trail.

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

Peer-reviewed papers, standards (STIX, TAXII, SP 800-150), government guidance (ICD 203), foundational practitioner papers (Hutchins et al.; Caltagirone et al.) and vendor reports differ in review, incentives and evidence. Know which you are reading.

Section ten point one develops research reading and critique with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section ten point one, FPSC expects research claims to carry owners and dates.

Section ten point one treats types of source method as testable only when evidence and ticket IDs are recorded.

### 10.2 Method questions

What data was used, from where, over what period? How were labels created? What comparison was made? Are results reproducible? Could the authors' interests shape the conclusion?

Section ten point two develops research reading and critique with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section ten point two, FPSC expects research claims to carry owners and dates.

Section ten point two treats types of source method as testable only when evidence and ticket IDs are recorded.

For section ten point two, Northmere Logistics Group will not accept research work without a written trail.

### 10.3 Transferability

A study on a large technology company's feeds may not transfer to a mid-sized logistics firm. Ask whether populations, threat exposure and resources are similar.

Section ten point three develops research reading and critique with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section ten point three, FPSC expects research claims to carry owners and dates.

Section ten point three treats types of source method as testable only when evidence and ticket IDs are recorded.

For section ten point three, Northmere Logistics Group will not accept research work without a written trail.

### 10.4 Reading foundational models critically

The kill chain was written for intrusion campaigns against defence contractors; it fits insider or cloud-identity attacks less well. The Diamond Model is a framework for organising events, not a method that produces conclusions by itself. ATT&CK reflects publicly reported behaviour, biased toward what vendors observe.

Section ten point four develops research reading and critique with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section ten point four, FPSC expects research claims to carry owners and dates.

Section ten point four treats types of source method as testable only when evidence and ticket IDs are recorded.

### 10.5 Structured critique

Summary, contribution, method strengths, method weaknesses, transferability, and what you would do with it. Keep tone professional.

Section ten point five develops research reading and critique with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section ten point five, FPSC expects research claims to carry owners and dates.

Section ten point five treats types of source method as testable only when evidence and ticket IDs are recorded.

For section ten point five, Northmere Logistics Group will not accept research work without a written trail.

### 10.6 Building a reading habit

A monthly reading group of two papers keeps the team current. Each session ends with one change to try or a reason not to.

Section ten point six develops research reading and critique with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section ten point six, FPSC expects research claims to carry owners and dates.

Section ten point six treats types of source method as testable only when evidence and ticket IDs are recorded.

For section ten point six, Northmere Logistics Group will not accept research work without a written trail.

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
- **EX048 — Kill chain fit.** For which attack types does the kill chain fit poorly? *Rubric:* 3 = insider, cloud-identity abuse; reason; 2 = one; 1 = none; 0 = none.
- **EX049 — Transfer test.** What should you compare before applying a study's results to NLG? *Rubric:* 3 = population, exposure, resources similarity; 2 = two; 1 = none; 0 = none.
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

Rafael's project: build an intelligence-driven detection backlog. Using ATT&CK-coded FPSC reports and NLG incidents, rank techniques by sector frequency, NLG exposure and current detection coverage, then deliver the top ten as detection requirements to the operations centre.

Section eleven point one develops applied project with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eleven point one, FPSC expects applied claims to carry owners and dates.

Section eleven point one treats choosing the project scope as testable only when evidence and ticket IDs are recorded.

### 11.2 Scope and ethics

In scope: public and FPSC reports (respecting TLP), internal incident summaries, current detection inventory. Out of scope: offensive testing, adversary infrastructure interaction, personal data beyond what incidents already hold.

Section eleven point two develops applied project with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eleven point two, FPSC expects applied claims to carry owners and dates.

Section eleven point two treats choosing the project scope as testable only when evidence and ticket IDs are recorded.

For section eleven point two, Northmere Logistics Group will not accept applied work without a written trail.

### 11.3 Method

Code reports to techniques with a second coder on a sample; compute frequencies; score exposure with asset owners; mark coverage as none, partial or full with the detection team. Combine scores transparently.

Section eleven point three develops applied project with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eleven point three, FPSC expects applied claims to carry owners and dates.

Section eleven point three treats choosing the project scope as testable only when evidence and ticket IDs are recorded.

### 11.4 Evaluation

Success measures: number of backlog items implemented within the term; detection coverage change; time from intelligence to detection requirement. Compare with the previous quarter.

Section eleven point four develops applied project with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eleven point four, FPSC expects applied claims to carry owners and dates.

Section eleven point four treats choosing the project scope as testable only when evidence and ticket IDs are recorded.

For section eleven point four, Northmere Logistics Group will not accept applied work without a written trail.

### 11.5 Stakeholders

Agree with the operations lead how many requirements the team can absorb. Ten realistic items beat thirty ignored ones.

Section eleven point five develops applied project with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eleven point five, FPSC expects applied claims to carry owners and dates.

Section eleven point five treats choosing the project scope as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Northmere Logistics Group will not accept applied work without a written trail.

### 11.6 Reporting

The final report states what was delivered, measured effects, limits and next steps. Restricted FPSC content stays out of the academic version.

Section eleven point six develops applied project with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section eleven point six, FPSC expects applied claims to carry owners and dates.

Section eleven point six treats choosing the project scope as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Northmere Logistics Group will not accept applied work without a written trail.

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
- **EX055 — Academic version.** What must be removed from the academic report? *Rubric:* 3 = restricted FPSC/TLP content; sensitive NLG detail; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Scope a useful project, use transparent scoring, agree capacity, measure outcomes and keep restricted material out of academic outputs.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) consolidate the course's methods into a personal practice framework; (2) transfer them to new organisations or sectors; (3) plan continuing development; (4) hand over a programme responsibly.

### 12.1 A personal framework

Summarise your practice on one page: decision-first requirements (chapter 1), sourcing mix (2), ACH and calibration (3, 9), risk and ethics governance (4), standards-based design (5), controlled evaluation (6), TLP-enforced integration (7), crisis discipline (8), research critique (10).

Section twelve point one develops final review and transfer with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section twelve point one, FPSC expects final claims to carry owners and dates.

Section twelve point one treats personal framework transfer continuing as testable only when evidence and ticket IDs are recorded.

For section twelve point one, Northmere Logistics Group will not accept final work without a written trail.

### 12.2 Transfer

Moving to another sector changes threats, regulators and communities but not the method. A healthcare or energy organisation will need sector-specific sharing communities and safety considerations, but requirements, evaluation and TLP discipline transfer intact.

Section twelve point two develops final review and transfer with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section twelve point two, FPSC expects final claims to carry owners and dates.

Section twelve point two treats personal framework transfer continuing as testable only when evidence and ticket IDs are recorded.

### 12.3 Continuing development

Follow ATT&CK and STIX updates, take part in community working groups, read research, and track your own calibration. Mentoring others consolidates learning.

Section twelve point three develops final review and transfer with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section twelve point three, FPSC expects final claims to carry owners and dates.

Section twelve point three treats personal framework transfer continuing as testable only when evidence and ticket IDs are recorded.

For section twelve point three, Northmere Logistics Group will not accept final work without a written trail.

### 12.4 Handover

If you leave, hand over requirements, source catalogue, platform documentation, decision records, review logs and community contacts with introductions. Transfer TLP-restricted relationships properly; memberships are often organisational, not personal.

Section twelve point four develops final review and transfer with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section twelve point four, FPSC expects final claims to carry owners and dates.

Section twelve point four treats personal framework transfer continuing as testable only when evidence and ticket IDs are recorded.

### 12.5 Reflecting on limits

CTI informs decisions under uncertainty; it rarely delivers certainty. Mature practitioners are comfortable saying "we do not know" and explaining what would reduce uncertainty.

Section twelve point five develops final review and transfer with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section twelve point five, FPSC expects final claims to carry owners and dates.

Section twelve point five treats personal framework transfer continuing as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Northmere Logistics Group will not accept final work without a written trail.

### 12.6 Final assessment

The course closes with a portfolio: the decision record set, an ACH product, an evaluation report and the project report, each reviewed against ICD 203 standards.

Section twelve point six develops final review and transfer with a Northmere Logistics Group note Rafael Moreau can demo offline.

Under section twelve point six, FPSC expects final claims to carry owners and dates.

Section twelve point six treats personal framework transfer continuing as testable only when evidence and ticket IDs are recorded.

For section twelve point six, Northmere Logistics Group will not accept final work without a written trail.

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
