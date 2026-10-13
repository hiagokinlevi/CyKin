# Threat Intelligence and OSINT: A Professional Course Book

- Language: English (`en`); professional course, six months.
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, with outputs embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working practitioners adding cyber threat intelligence (CTI) and OSINT skills to an IT or security role.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical boundary: no collection on real private individuals, no terms-of-service evasion, no deanonymisation, no contact with adversary infrastructure. Organisations, people and indicators are **synthetic** unless a sentence cites a public source; addresses use RFC 5737 ranges and domains use `.example`.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–4 cover foundations, stakeholders, authorised practice and core methods. Chapters 5–8 cover tools and interpretation (with a triage-scoring lab), workflow, controls and verification, and a supervised case. Chapters 9–12 cover communication and ethics, quality and troubleshooting, a supervised laboratory (with a brief-release check lab) and the practice portfolio. Each chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, five exercises scored 0–3, a synthesis and a **Continue studying** block.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Bramwell Insurance Brokers (BIB)** — 300 staff, a client portal, a CRM and broker email | Organisation served by CTI | Invented |
| **Priya Nair** | IT support lead taking on CTI duties part-time | Invented |
| **Financial Services Sharing Group (FSSG)** | Sector community sharing intelligence under TLP 2.0 | Invented |

### Core sources

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) and [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); Hutchins et al. [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf); NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) |
| [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) restate core security concepts in a CTI context; (2) describe the intelligence cycle as a working routine; (3) name the main models and standards; (4) set realistic goals for a part-time CTI role.

### 1.1 Starting point

Priya has run IT support at Bramwell Insurance Brokers for eight years. She knows the systems, the users and the help desk. Her manager adds CTI to her role: one day a week to turn outside information about threats into better defences.

Section one point one develops security foundations for practitioners with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section one point one, FSSG expects security claims to carry owners and dates.

Section one point one treats starting point core terms as testable only when evidence and ticket IDs are recorded.

### 1.2 Core terms

Threat: an actor or event that could cause harm. Vulnerability: a weakness. Risk: likelihood combined with impact. Control: a measure that reduces risk. Intelligence informs the threat side so controls are chosen well.

Section one point two develops security foundations for practitioners with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section one point two, FSSG expects security claims to carry owners and dates.

Section one point two treats starting point core terms as testable only when evidence and ticket IDs are recorded.

### 1.3 The cycle as a routine

Direction (what does BIB need to know?), collection (FSSG, advisories, internal reports), processing (cleaning indicators), analysis (what it means for BIB), dissemination (to whoever acts) and feedback. For Priya it becomes a weekly checklist.

Section one point three develops security foundations for practitioners with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section one point three, FSSG expects security claims to carry owners and dates.

Section one point three treats starting point core terms as testable only when evidence and ticket IDs are recorded.

### 1.4 Models

MITRE ATT&CK names adversary techniques — Phishing is T1566. The Hutchins et al. kill chain shows phases where defenders can act. The Diamond Model describes events by adversary, capability, infrastructure and victim.

Section one point four develops security foundations for practitioners with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section one point four, FSSG expects security claims to carry owners and dates.

Section one point four treats starting point core terms as testable only when evidence and ticket IDs are recorded.

### 1.5 Standards

STIX 2.1 for data, TAXII 2.1 for exchange, FIRST TLP 2.0 for sharing limits, NIST SP 800-150 for sharing practice.

Section one point five develops security foundations for practitioners with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section one point five, FSSG expects security claims to carry owners and dates.

Section one point five treats starting point core terms as testable only when evidence and ticket IDs are recorded.

For section one point five, Bramwell Insurance Brokers will not accept security work without a written trail.

### 1.6 Realistic goals

In one day a week Priya can triage FSSG items, match indicators against email and DNS logs, brief the help desk and report monthly. Deep malware analysis and attribution are out of scope.

Section one point six develops security foundations for practitioners with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section one point six, FSSG expects security claims to carry owners and dates.

Section one point six treats starting point core terms as testable only when evidence and ticket IDs are recorded.

### 1.7 What brokers face

Insurance brokers hold personal and financial client data and move money. Business email compromise, credential phishing against the client portal and ransomware are the main concerns reported in the sector.

Section one point seven develops security foundations for practitioners with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section one point seven, FSSG expects security claims to carry owners and dates.

Section one point seven treats starting point core terms as testable only when evidence and ticket IDs are recorded.

### 1.8 Learning plan

Each chapter adds one routine to her week, so the role grows steadily.

Section one point eight develops security foundations for practitioners with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section one point eight, FSSG expects security claims to carry owners and dates.

Section one point eight treats starting point core terms as testable only when evidence and ticket IDs are recorded.

For section one point eight, Bramwell Insurance Brokers will not accept security work without a written trail.

### Worked example

Priya's first weekly checklist: Monday, read FSSG items and triage; Tuesday morning, search logs for this week's indicators; Wednesday, send the help desk a short scam update; last Friday of the month, write a one-page summary for her manager.

> **Synthetic case.** BIB and Priya are invented.

### Errors and limits

A part-time role cannot cover everything; agree priorities in writing.

### Exercises

- **EX001 — Define risk.** Define risk and explain how CTI contributes to it. *Rubric:* 3 = likelihood × impact; CTI informs threat/likelihood; 2 = definition; 1 = vague; 0 = none.
- **EX002 — Weekly routine.** Turn the intelligence cycle into a weekly routine for a part-time role. *Rubric:* 3 = all stages mapped to days/tasks; 2 = most; 1 = list; 0 = none.
- **EX003 — Out of scope.** Name two tasks outside Priya's realistic scope. *Rubric:* 3 = malware analysis, attribution; 2 = one; 1 = log search; 0 = none.
- **EX004 — Broker threats.** List three threats brokers commonly face. *Rubric:* 3 = BEC, portal credential phishing, ransomware; 2 = two; 1 = one; 0 = none.
- **EX005 — Model purpose.** Match ATT&CK, the kill chain and the Diamond Model to what each describes. *Rubric:* 3 = techniques; phases; event vertices; 2 = two; 1 = one; 0 = none.

### Synthesis

CTI informs risk decisions through a steady cycle, shaped by models and standards and sized to the time available.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Threat intelligence and OSINT: service and stakeholder context

### Learning outcomes

You will (1) identify BIB's intelligence consumers and their decisions; (2) write priority intelligence requirements; (3) match products to consumers; (4) manage expectations.

### 2.1 Consumers

The managing director decides budgets. The operations manager decides on process changes such as payment verification. The IT team configures email and network controls. The help desk talks to staff. The compliance officer handles regulators and data protection.

Section two point one develops threat intelligence and osint service with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section two point one, FSSG expects threat claims to carry owners and dates.

Section two point one treats consumers requirements products expectations as testable only when evidence and ticket IDs are recorded.

### 2.2 Requirements

Priya interviews each and writes requirements: "Which fraud methods target brokers' payment processes this quarter?" (operations); "Which vulnerabilities in our CRM and portal are being exploited?" (IT); "Are BIB credentials or client data exposed publicly?" (compliance).

Section two point two develops threat intelligence and osint service with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section two point two, FSSG expects threat claims to carry owners and dates.

Section two point two treats consumers requirements products expectations as testable only when evidence and ticket IDs are recorded.

### 2.3 Products

Managing director: quarterly half-page. Operations: alerts when a fraud method appears. IT: indicator lists and vulnerability notes. Help desk: weekly scam update. Compliance: notices of data exposure.

Section two point three develops threat intelligence and osint service with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section two point three, FSSG expects threat claims to carry owners and dates.

Section two point three treats consumers requirements products expectations as testable only when evidence and ticket IDs are recorded.

For section two point three, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 2.4 Expectations

Priya explains that CTI reduces surprise but cannot predict every attack. She agrees what "urgent" means: active exploitation of a system BIB runs, or a fraud method targeting BIB by name.

Section two point four develops threat intelligence and osint service with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section two point four, FSSG expects threat claims to carry owners and dates.

Section two point four treats consumers requirements products expectations as testable only when evidence and ticket IDs are recorded.

### 2.5 Business email compromise

Fraudsters impersonate clients or insurers to redirect payments. The operations manager's decision — whether to require call-back verification for changed bank details — depends on intelligence about how common this is in the sector.

Section two point five develops threat intelligence and osint service with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section two point five, FSSG expects threat claims to carry owners and dates.

Section two point five treats consumers requirements products expectations as testable only when evidence and ticket IDs are recorded.

### 2.6 Feedback

Each consumer gets a two-question form quarterly.

Section two point six develops threat intelligence and osint service with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section two point six, FSSG expects threat claims to carry owners and dates.

Section two point six treats consumers requirements products expectations as testable only when evidence and ticket IDs are recorded.

For section two point six, Bramwell Insurance Brokers will not accept threat work without a written trail.

Section two point six fails closed if threat evidence is missing rather than guessing.

### 2.7 Saying no

Requests outside requirements, such as researching a difficult client's personal life, are declined politely.

Section two point seven develops threat intelligence and osint service with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section two point seven, FSSG expects threat claims to carry owners and dates.

Section two point seven treats consumers requirements products expectations as testable only when evidence and ticket IDs are recorded.

For section two point seven, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 2.8 Writing it down

A one-page requirements list, approved by the manager, guides what Priya collects.

Section two point eight develops threat intelligence and osint service with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section two point eight, FSSG expects threat claims to carry owners and dates.

Section two point eight treats consumers requirements products expectations as testable only when evidence and ticket IDs are recorded.

For section two point eight, Bramwell Insurance Brokers will not accept threat work without a written trail.

### Regulatory context

Financial regulators expect firms to manage operational and cyber risk. Showing that intelligence informed controls — such as call-back verification — helps the compliance officer evidence good practice during reviews.

### Worked example

FSSG reports that three brokers lost client premiums through fake insurer bank-detail changes. Priya alerts the operations manager with the method and two sender domains. The manager introduces call-back verification for any bank-detail change the same week.

> **Synthetic case.** The losses and change are invented.

### Errors and limits

Requirements change; review them every quarter.

### Exercises

- **EX006 — Consumer map.** Map three BIB consumers to the decisions they make. *Rubric:* 3 = three correct pairs; 2 = two; 1 = one; 0 = none.
- **EX007 — Write a requirement.** Write one priority intelligence requirement for the compliance officer. *Rubric:* 3 = specific question, consumer, timeframe; 2 = two; 1 = topic; 0 = none.
- **EX008 — BEC decision.** Which decision did the FSSG fraud report support? *Rubric:* 3 = call-back verification for bank-detail changes; 2 = partial; 1 = vague; 0 = none.
- **EX009 — Urgent definition.** How did Priya define "urgent"? *Rubric:* 3 = active exploitation of BIB system or fraud naming BIB; 2 = one; 1 = everything; 0 = none.
- **EX010 — Decline politely.** Why decline researching a client's personal life? *Rubric:* 3 = outside requirements; privacy/law; 2 = partial; 1 = do it; 0 = none.

### Synthesis

Know your consumers, write requirements with them, match products to decisions and manage expectations.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) work within written authorisation; (2) apply TLP 2.0 and data-protection rules; (3) handle evidence with provenance; (4) recognise actions that need legal or management approval.

### 3.1 Authorisation

Priya's role description and the IT security policy list what she may do: read intelligence sources, search BIB logs, draft requests, share sanitised items with FSSG. Anything else needs approval.

Section three point one develops authorized practice and evidence handling with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section three point one, FSSG expects authorized claims to carry owners and dates.

Section three point one treats authorisation tlp data protection as testable only when evidence and ticket IDs are recorded.

### 3.2 TLP 2.0

CLEAR: public. GREEN: community. AMBER: BIB and its clients on need-to-know. AMBER+STRICT: BIB only. RED: named people. Priya stores items with labels and checks before forwarding.

Section three point two develops authorized practice and evidence handling with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section three point two, FSSG expects authorized claims to carry owners and dates.

Section three point two treats authorisation tlp data protection as testable only when evidence and ticket IDs are recorded.

For section three point two, Bramwell Insurance Brokers will not accept authorized work without a written trail.

### 3.3 Data protection

Logs and emails contain personal data of staff and clients. Under the GDPR-style rules BIB follows, she uses only what is needed, keeps extracts briefly and removes personal details before sharing.

Section three point three develops authorized practice and evidence handling with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section three point three, FSSG expects authorized claims to carry owners and dates.

Section three point three treats authorisation tlp data protection as testable only when evidence and ticket IDs are recorded.

### 3.4 Evidence

When a phishing email is reported, she saves the original message file, records who reported it and when, and computes a hash of the file. Analysis uses a copy.

Section three point four develops authorized practice and evidence handling with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section three point four, FSSG expects authorized claims to carry owners and dates.

Section three point four treats authorisation tlp data protection as testable only when evidence and ticket IDs are recorded.

### 3.5 Approval needed

Contacting police, requesting takedowns, notifying regulators, buying intelligence services, or engaging with suspected criminals. Each goes through management and, where needed, legal advice.

Section three point five develops authorized practice and evidence handling with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section three point five, FSSG expects authorized claims to carry owners and dates.

Section three point five treats authorisation tlp data protection as testable only when evidence and ticket IDs are recorded.

For section three point five, Bramwell Insurance Brokers will not accept authorized work without a written trail.

### 3.6 OSINT boundaries

Public sources only, within terms of service, no fake accounts, no closed forums, no attempts to identify private individuals.

Section three point six develops authorized practice and evidence handling with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section three point six, FSSG expects authorized claims to carry owners and dates.

Section three point six treats authorisation tlp data protection as testable only when evidence and ticket IDs are recorded.

For section three point six, Bramwell Insurance Brokers will not accept authorized work without a written trail.

### 3.7 Records

A simple log: item, source, label, action, date.

Section three point seven develops authorized practice and evidence handling with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section three point seven, FSSG expects authorized claims to carry owners and dates.

Section three point seven treats authorisation tlp data protection as testable only when evidence and ticket IDs are recorded.

For section three point seven, Bramwell Insurance Brokers will not accept authorized work without a written trail.

Section three point seven fails closed if authorized evidence is missing rather than guessing.

### 3.8 Mistakes

If something is shared wrongly, report it at once and ask recipients to delete it.

Section three point eight develops authorized practice and evidence handling with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section three point eight, FSSG expects authorized claims to carry owners and dates.

Section three point eight treats authorisation tlp data protection as testable only when evidence and ticket IDs are recorded.

For section three point eight, Bramwell Insurance Brokers will not accept authorized work without a written trail.

### Chain of custody

If an incident may lead to legal action, evidence handling must show who held each item and when. Priya records every transfer of the saved email file — to the IT manager, to an external responder — with date, recipient and purpose.

### Worked example

A client forwards a suspicious email claiming to come from BIB. Priya saves the original, hashes it, removes the client's details from her working notes and shares the sender domain with FSSG at GREEN. The compliance officer decides whether the client must be told anything further.

> **Synthetic case.** The email is invented.

### Errors and limits

Policies need updating as the role grows.

### Exercises

- **EX011 — Approval list.** Name four actions requiring management or legal approval. *Rubric:* 3 = four of police, takedown, regulator, purchase, engaging criminals; 2 = three; 1 = one; 0 = none.
- **EX012 — Evidence steps.** List the evidence steps for a reported phishing email. *Rubric:* 3 = save original, record reporter/time, hash, work on copy; 2 = three; 1 = one; 0 = none.
- **EX013 — AMBER+STRICT reach.** Who may receive TLP:AMBER+STRICT material? *Rubric:* 3 = BIB only, need-to-know; 2 = partial; 1 = clients; 0 = none.
- **EX014 — Client email decision.** Who decides on informing the client further, and why? *Rubric:* 3 = compliance officer; regulatory/data duties; 2 = partial; 1 = Priya; 0 = none.
- **EX015 — Fake accounts.** Why are fake accounts forbidden for OSINT? *Rubric:* 3 = breaches terms/law/ethics; risk to BIB; 2 = partial; 1 = allowed; 0 = none.

### Synthesis

Work inside written authority, apply TLP and data protection, preserve evidence and escalate actions that need approval.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Threat intelligence and OSINT: core methods

### Learning outcomes

You will (1) triage, grade and tag intelligence; (2) write calibrated judgments; (3) consider alternative explanations; (4) produce short, actionable notes.

### 4.1 Triage

Relevant? Timely? Actionable? Source known? Most items fail relevance and are logged only.

Section four point one develops threat intelligence and osint core with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section four point one, FSSG expects threat claims to carry owners and dates.

Section four point one treats triage grading tagging calibrated as testable only when evidence and ticket IDs are recorded.

For section four point one, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 4.2 Grading

Admiralty scale: source A–F, information 1–6. FSSG with a good record: B. A vendor blog: C until its record is known. Anonymous posts: F.

Section four point two develops threat intelligence and osint core with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section four point two, FSSG expects threat claims to carry owners and dates.

Section four point two treats triage grading tagging calibrated as testable only when evidence and ticket IDs are recorded.

For section four point two, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 4.3 Tagging

Tag ATT&CK techniques supported by the text: invoice fraud by email (T1566 if links or attachments are used; otherwise a social-engineering pretext), credential use (T1078), encryption for impact (T1486).

Section four point three develops threat intelligence and osint core with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section four point three, FSSG expects threat claims to carry owners and dates.

Section four point three treats triage grading tagging calibrated as testable only when evidence and ticket IDs are recorded.

### 4.4 Calibrated words

Use a fixed scale: unlikely (20–45%), roughly even (45–55%), likely (55–80%), very likely (80–95%). ICD 203 asks analysts to express uncertainty clearly and explain confidence.

Section four point four develops threat intelligence and osint core with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section four point four, FSSG expects threat claims to carry owners and dates.

Section four point four treats triage grading tagging calibrated as testable only when evidence and ticket IDs are recorded.

For section four point four, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 4.5 Alternatives

Before concluding, ask: what else could explain this? A spike in failed logins may be an attack — or a password-policy change forcing resets.

Section four point five develops threat intelligence and osint core with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section four point five, FSSG expects threat claims to carry owners and dates.

Section four point five treats triage grading tagging calibrated as testable only when evidence and ticket IDs are recorded.

For section four point five, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 4.6 Notes

Three lines: what happened; what it means for BIB with likelihood and confidence; what to do and who does it.

Section four point six develops threat intelligence and osint core with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section four point six, FSSG expects threat claims to carry owners and dates.

Section four point six treats triage grading tagging calibrated as testable only when evidence and ticket IDs are recorded.

For section four point six, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 4.7 Consistency

Priya and the IT manager grade the same five items monthly and compare.

Section four point seven develops threat intelligence and osint core with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section four point seven, FSSG expects threat claims to carry owners and dates.

Section four point seven treats triage grading tagging calibrated as testable only when evidence and ticket IDs are recorded.

For section four point seven, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 4.8 Time

Triage in minutes; analysis only for items that pass.

Section four point eight develops threat intelligence and osint core with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section four point eight, FSSG expects threat claims to carry owners and dates.

Section four point eight treats triage grading tagging calibrated as testable only when evidence and ticket IDs are recorded.

For section four point eight, Bramwell Insurance Brokers will not accept threat work without a written trail.

Section four point eight fails closed if threat evidence is missing rather than guessing.

### Business email compromise signs

Requests to change bank details, urgency, a slightly altered sender domain and replies directed elsewhere are common signs. Intelligence about current pretexts — fake insurer mergers, new payment portals — helps staff recognise them quickly, and gives the operations manager concrete examples for training sessions.

### Worked example

Failed logins on the client portal triple overnight. Alternative explanations: credential stuffing, or clients locked out after a portal update. Priya checks: the update changed the login page and support calls rose. She writes: "Spike likely caused by the update (moderate confidence); a small share of attempts came from addresses FSSG flagged, so stuffing may also be occurring. Action: IT to review those addresses; support to send clients reset guidance."

> **Synthetic case.** The spike is invented.

### Errors and limits

Scales reduce ambiguity, not error; track outcomes.

### Exercises

- **EX016 — Grade a blog.** What grade would a new vendor blog's source receive and why? *Rubric:* 3 = C (or similar) until record known; 2 = grade; 1 = A; 0 = none.
- **EX017 — Alternative.** Give an alternative explanation for a failed-login spike. *Rubric:* 3 = policy change/update lockouts; 2 = vague; 1 = none; 0 = none.
- **EX018 — Likely band.** What range does "likely" cover on the scale? *Rubric:* 3 = 55–80%; 2 = close; 1 = wrong; 0 = none.
- **EX019 — Two causes.** Why did Priya's note mention both causes? *Rubric:* 3 = evidence for both; avoid ignoring minority attack; 2 = partial; 1 = indecision; 0 = none.
- **EX020 — Note lines.** What are the three lines of a note? *Rubric:* 3 = what, meaning with likelihood/confidence, action/owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Triage fast, grade and tag with reasons, write calibrated judgments, consider alternatives and keep notes actionable.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Threat intelligence and OSINT: tools and interpretation

### Learning outcomes

You will (1) use a simple scoring tool for triage; (2) interpret its output critically; (3) use passive OSINT tools within their terms; (4) know when tool output needs human judgment.

### 5.1 Why score

Priya receives about forty items a week. A transparent score — relevance, freshness, source grade — puts the most useful first.

Section five point one develops threat intelligence and osint tools with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section five point one, FSSG expects threat claims to carry owners and dates.

Section five point one treats why score reading the as testable only when evidence and ticket IDs are recorded.

For section five point one, Bramwell Insurance Brokers will not accept threat work without a written trail.

### Lab — triage scoring

```python
"""Lab (ch 05): score incoming items on relevance, timeliness and source grade, then sort (synthetic)."""
GRADE = {"A": 3, "B": 2, "C": 1, "D": 0, "E": 0, "F": 0}
items = [("Q1", "broker portal phishing wave", True, 2, "B"),
         ("Q2", "ransomware in manufacturing", False, 1, "B"),
         ("Q3", "flaw in our CRM version", True, 5, "A"),
         ("Q4", "forum claim of broker data sale", True, 1, "F"),
         ("Q5", "old address list", True, 40, "C")]
for qid, title, relevant, age_days, grade in items:
    score = (3 if relevant else 0) + (2 if age_days <= 7 else 0) + GRADE[grade]
    items[items.index((qid, title, relevant, age_days, grade))] = (score, qid, title)
for score, qid, title in sorted(items, reverse=True):
    print(qid, score, title, "-> analyse" if score >= 6 else "-> log only" if score < 5 else "-> check")
```

Run with `python3 lab_triage.py`. Verified output:

```text
Q3 8 flaw in our CRM version -> analyse
Q1 7 broker portal phishing wave -> analyse
Q4 5 forum claim of broker data sale -> check
Q5 4 old address list -> log only
Q2 4 ransomware in manufacturing -> log only
```

### 5.2 Reading the result

Q3, a flaw in BIB's CRM version from an A-grade source within five days, scores 8 and goes to analysis. Q1, the broker-portal phishing wave from FSSG, scores 7 — analysis. Q4, a forum claim that broker data is for sale, scores 5 — check, because it is relevant and fresh but from an F source. Q5 (relevant but 40 days old) and Q2 (fresh but about manufacturing) score 4 and are logged only.

Section five point two develops threat intelligence and osint tools with a Bramwell Insurance Brokers note Priya Nair can demo offline.

### 5.3 Interpreting

Scores order work; they do not decide. Q4 is low-grade but could matter if true; Priya checks whether BIB data appears in the claim's sample through FSSG rather than visiting the forum.

Section five point three develops threat intelligence and osint tools with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section five point three, FSSG expects threat claims to carry owners and dates.

Section five point three treats why score reading the as testable only when evidence and ticket IDs are recorded.

### 5.4 OSINT tools

Certificate-transparency search for lookalikes of bramwell.example; national advisories; vendor vulnerability pages. Used within terms.

Section five point four develops threat intelligence and osint tools with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section five point four, FSSG expects threat claims to carry owners and dates.

Section five point four treats why score reading the as testable only when evidence and ticket IDs are recorded.

For section five point four, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 5.5 Tool limits

A score ignores context the tool does not know — such as a planned CRM upgrade making Q3 moot next week.

Section five point five develops threat intelligence and osint tools with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section five point five, FSSG expects threat claims to carry owners and dates.

Section five point five treats why score reading the as testable only when evidence and ticket IDs are recorded.

For section five point five, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 5.6 Adjusting weights

If too many irrelevant items reach analysis, adjust weights and document the change.

Section five point six develops threat intelligence and osint tools with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section five point six, FSSG expects threat claims to carry owners and dates.

Section five point six treats why score reading the as testable only when evidence and ticket IDs are recorded.

For section five point six, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 5.7 Spreadsheet versions

The same scoring works in a spreadsheet; the script is easier to audit.

Section five point seven develops threat intelligence and osint tools with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section five point seven, FSSG expects threat claims to carry owners and dates.

Section five point seven treats why score reading the as testable only when evidence and ticket IDs are recorded.

For section five point seven, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 5.8 Review

Monthly, compare scores with what actually proved useful.

Section five point eight develops threat intelligence and osint tools with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section five point eight, FSSG expects threat claims to carry owners and dates.

Section five point eight treats why score reading the as testable only when evidence and ticket IDs are recorded.

For section five point eight, Bramwell Insurance Brokers will not accept threat work without a written trail.

Section five point eight fails closed if threat evidence is missing rather than guessing.

### Recording tool runs

Save each week's scored list with the date. Later comparison of scores against what proved useful needs those records.

### Worked example

A certificate-transparency search shows "bramwell-claims.example" registered yesterday. Not a BIB domain. Priya scores it high (relevant, fresh, reliable log), checks with marketing that it is not a new campaign site, and asks IT to block it and management to approve a takedown request.

> **Synthetic case.** The domain is invented.

### Errors and limits

Scores encode assumptions; review them.

### Exercises

- **EX021 — Lab order.** Give the lab's ranking with actions. *Rubric:* 3 = Q3 8, Q1 7 analyse; Q4 5 check; Q5, Q2 4 log; 2 = order; 1 = partial; 0 = none.
- **EX022 — Q4 handling.** How should Priya check the forum claim safely? *Rubric:* 3 = via FSSG/contracted provider, not visiting forum; 2 = partial; 1 = visit forum; 0 = none.
- **EX023 — Missing context.** Give an example of context a score cannot know. *Rubric:* 3 = planned upgrade or similar; 2 = vague; 1 = none; 0 = none.
- **EX024 — Lookalike check.** Why ask marketing before blocking the new domain? *Rubric:* 3 = may be legitimate campaign site; 2 = partial; 1 = no need; 0 = none.
- **EX025 — Weight change.** What should accompany any change to scoring weights? *Rubric:* 3 = documentation with reason, review; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Use transparent scoring to order work, interpret it with context, keep OSINT passive and review the tool against outcomes.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Threat intelligence and OSINT: operational workflow

### Learning outcomes

You will (1) run a repeatable weekly CTI workflow; (2) track items from arrival to closure; (3) coordinate with IT and the help desk; (4) handle urgent items outside the routine.

### 6.1 The week

Monday: FSSG items scored and triaged. Tuesday: indicator matching in email and DNS logs; requests drafted. Wednesday: help-desk scam update. Thursday: follow-ups. Last Friday: monthly summary.

Section six point one develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point one, FSSG expects threat claims to carry owners and dates.

Section six point one treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point one, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 6.2 Tracking

Each item gets a ticket: arrival, source, label, grade, score, decision, actions, closure date. Open tickets show what is pending.

Section six point two develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point two, FSSG expects threat claims to carry owners and dates.

Section six point two treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point two, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 6.3 Coordination

IT applies blocks and patches; the help desk briefs staff; operations changes processes. Priya's requests name the owner and deadline.

Section six point three develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point three, FSSG expects threat claims to carry owners and dates.

Section six point three treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point three, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 6.4 Urgent path

Active exploitation of BIB's CRM or portal, or a fraud method naming BIB, skips the routine: phone the owner, open a priority ticket, inform the manager.

Section six point four develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point four, FSSG expects threat claims to carry owners and dates.

Section six point four treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point four, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 6.5 Closure

Items close when action is done and verified, or when a decision not to act is recorded with reason.

Section six point five develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point five, FSSG expects threat claims to carry owners and dates.

Section six point five treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point five, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 6.6 Cover

When Priya is away, the IT manager follows the same checklist, using her handover note.

Section six point six develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point six, FSSG expects threat claims to carry owners and dates.

Section six point six treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point six, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 6.7 Metrics

Items received, analysed, actioned; time from arrival to action; blocks that stopped connections.

Section six point seven develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point seven, FSSG expects threat claims to carry owners and dates.

Section six point seven treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point seven, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 6.8 Workload

If the week overflows, Priya drops lowest-scored items first and tells her manager.

Section six point eight develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point eight, FSSG expects threat claims to carry owners and dates.

Section six point eight treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point eight, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 6.9 FSSG feedback

Every month she tells FSSG which items helped BIB; communities improve when members respond.

Section six point nine develops threat intelligence and osint operational with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section six point nine, FSSG expects threat claims to carry owners and dates.

Section six point nine treats the week tracking coordination as testable only when evidence and ticket IDs are recorded.

For section six point nine, Bramwell Insurance Brokers will not accept threat work without a written trail.

### Handover note

A short handover note lists open tickets with next steps, scheduled reports and any urgent items in progress. The IT manager can continue the routine from it without calling Priya on leave.

### Worked example

On Wednesday FSSG reports active exploitation of the CRM version BIB runs. Priya uses the urgent path: she phones the IT manager, opens a priority ticket and informs her manager. The vendor fix is applied that evening; she verifies the version the next morning and closes the ticket with evidence.

> **Synthetic case.** The exploitation report is invented.

### Errors and limits

Routines can make people miss unusual items; read summaries of logged-only items weekly.

### Exercises

- **EX026 — Ticket fields.** List six ticket fields Priya uses. *Rubric:* 3 = six of arrival, source, label, grade, score, decision, actions, closure; 2 = four; 1 = two; 0 = none.
- **EX027 — Urgent triggers.** What triggers the urgent path? *Rubric:* 3 = active exploitation of BIB system; fraud naming BIB; 2 = one; 1 = any item; 0 = none.
- **EX028 — Closure rule.** When may an item be closed? *Rubric:* 3 = action verified, or decision not to act recorded; 2 = one; 1 = anytime; 0 = none.
- **EX029 — Overflow.** What should Priya do when the week overflows? *Rubric:* 3 = drop lowest-scored first; tell manager; 2 = one; 1 = work weekends silently; 0 = none.
- **EX030 — CRM case.** Describe the steps taken for the CRM exploitation report. *Rubric:* 3 = phone, priority ticket, manager, patch, verify, close; 2 = most; 1 = some; 0 = none.

### Synthesis

Run a weekly routine, track every item, coordinate owners, keep an urgent path and close with evidence.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Threat intelligence and OSINT: controls and verification

### Learning outcomes

You will (1) turn intelligence into control requests; (2) choose controls by indicator and technique; (3) verify controls after change; (4) avoid collateral damage.

### 7.1 Requests

Each request states intelligence and source, label, the control change, expected benefit, side effects, verification and review date.

Section seven point one develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point one, FSSG expects threat claims to carry owners and dates.

Section seven point one treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

For section seven point one, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 7.2 Choosing controls

Sender domains to the email gateway; malicious domains to DNS filtering; hashes to endpoint protection; technique intelligence to configuration — for example, multi-factor authentication on the client portal against Valid Accounts (T1078), and call-back verification against payment fraud.

Section seven point two develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point two, FSSG expects threat claims to carry owners and dates.

Section seven point two treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

### 7.3 Process controls

Not all controls are technical. Business email compromise is best countered by verification procedures, dual approval for payments and staff awareness.

Section seven point three develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point three, FSSG expects threat claims to carry owners and dates.

Section seven point three treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

For section seven point three, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 7.4 Verification

Technical: test lookups, harmless test messages, configuration checks. Process: ask operations to confirm call-backs happened for the month's bank-detail changes.

Section seven point four develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point four, FSSG expects threat claims to carry owners and dates.

Section seven point four treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

For section seven point four, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 7.5 Collateral damage

Blocking a domain used by an insurer partner would disrupt business; check with operations first.

Section seven point five develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point five, FSSG expects threat claims to carry owners and dates.

Section seven point five treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

For section seven point five, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 7.6 Review

Blocks expire; process controls are reviewed annually.

Section seven point six develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point six, FSSG expects threat claims to carry owners and dates.

Section seven point six treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

For section seven point six, Bramwell Insurance Brokers will not accept threat work without a written trail.

Section seven point six fails closed if threat evidence is missing rather than guessing.

### 7.7 Recording

The control register lists every change made because of intelligence.

Section seven point seven develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point seven, FSSG expects threat claims to carry owners and dates.

Section seven point seven treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

For section seven point seven, Bramwell Insurance Brokers will not accept threat work without a written trail.

Section seven point seven fails closed if threat evidence is missing rather than guessing.

### 7.8 Measuring effect

Count blocked connections, quarantined messages and prevented fraudulent payments reported by operations.

Section seven point eight develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point eight, FSSG expects threat claims to carry owners and dates.

Section seven point eight treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

For section seven point eight, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 7.9 ATT&CK mitigations

Technique pages list mitigations that can inspire requests, adapted to BIB's tools.

Section seven point nine develops threat intelligence and osint controls with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section seven point nine, FSSG expects threat claims to carry owners and dates.

Section seven point nine treats requests choosing controls process as testable only when evidence and ticket IDs are recorded.

For section seven point nine, Bramwell Insurance Brokers will not accept threat work without a written trail.

### Staff awareness as a control

Awareness sessions using current, real-looking but synthetic examples help staff spot pretexts. Short monthly reminders beat a long annual course. Priya supplies the examples from intelligence; the help desk delivers them in team meetings. Reports of suspicious messages from staff are counted as a sign that awareness is working, and each report receives a thank-you reply.

### Worked example

Priya requests multi-factor authentication for brokers' remote email access, citing FSSG reports of credential phishing against three brokers. IT enables it for a pilot group. Verification: sign-in logs show the second factor requested for each pilot login. A month later, failed sign-ins from flagged addresses no longer succeed.

> **Synthetic case.** The pilot is invented.

### Errors and limits

A control's absence of alerts does not prove it works; test it.

### Exercises

- **EX031 — BEC controls.** Which controls best counter business email compromise? *Rubric:* 3 = verification call-backs, dual approval, awareness; 2 = two; 1 = firewall; 0 = none.
- **EX032 — Process verification.** How can a process control be verified? *Rubric:* 3 = confirm call-backs happened for actual changes; 2 = partial; 1 = assume; 0 = none.
- **EX033 — Partner domain.** Why check with operations before blocking a domain? *Rubric:* 3 = may be partner insurer; business disruption; 2 = partial; 1 = no need; 0 = none.
- **EX034 — MFA verification.** How was the MFA pilot verified? *Rubric:* 3 = sign-in logs show second factor per login; 2 = partial; 1 = none; 0 = none.
- **EX035 — Register.** Why keep a register of intelligence-driven changes? *Rubric:* 3 = traceability, review, evidence of value; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Request controls with evidence, include process controls, verify technically and procedurally, avoid collateral damage and record changes.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Threat intelligence and OSINT: supervised case analysis

### Learning outcomes

You will (1) analyse a realistic incident under supervision; (2) build a timeline; (3) map events to ATT&CK and kill-chain phases; (4) present findings with confidence and gaps.

### 8.1 The case

A broker receives an email apparently from an insurer announcing new bank details. Finance pays one premium to the new account before call-back verification catches a second request. Priya analyses the case with an external responder as supervisor.

Section eight point one develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point one, FSSG expects threat claims to carry owners and dates.

Section eight point one treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

### 8.2 Timeline

Collect times from the email gateway, finance system and call-back log. Convert all to UTC. Order events: lookalike domain registered; email received; first payment; second request; call-back; fraud confirmed.

Section eight point two develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point two, FSSG expects threat claims to carry owners and dates.

Section eight point two treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

### 8.3 Mapping

Domain registration: Acquire Infrastructure (T1583) — preparation. Email: Phishing (T1566) as delivery of a pretext. No malware or account compromise is evident.

Section eight point three develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point three, FSSG expects threat claims to carry owners and dates.

Section eight point three treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

For section eight point three, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 8.4 Diamond view

Adversary: unknown fraud group. Capability: social-engineering pretext. Infrastructure: lookalike domain and a bank account. Victim: BIB finance team.

Section eight point four develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point four, FSSG expects threat claims to carry owners and dates.

Section eight point four treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

For section eight point four, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 8.5 Confidence and gaps

High confidence in the sequence; low confidence about whether the insurer's own mailbox was compromised. Ask the insurer through proper channels.

Section eight point five develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point five, FSSG expects threat claims to carry owners and dates.

Section eight point five treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

For section eight point five, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 8.6 Lessons

Call-back verification worked on the second request; it was not yet mandatory on the first.

Section eight point six develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point six, FSSG expects threat claims to carry owners and dates.

Section eight point six treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

For section eight point six, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 8.7 Sharing

A GREEN item to FSSG with the lookalike domain and pretext, without client details.

Section eight point seven develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point seven, FSSG expects threat claims to carry owners and dates.

Section eight point seven treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

For section eight point seven, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 8.8 Supervisor review

The responder checks Priya's timeline and wording before release.

Section eight point eight develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point eight, FSSG expects threat claims to carry owners and dates.

Section eight point eight treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

For section eight point eight, Bramwell Insurance Brokers will not accept threat work without a written trail.

Section eight point eight fails closed if threat evidence is missing rather than guessing.

### 8.9 Legal steps

Management reports the fraud to the bank and police; Priya provides the timeline.

Section eight point nine develops threat intelligence and osint supervised with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eight point nine, FSSG expects threat claims to carry owners and dates.

Section eight point nine treats the case timeline mapping as testable only when evidence and ticket IDs are recorded.

For section eight point nine, Bramwell Insurance Brokers will not accept threat work without a written trail.

### Kill chain view

On the kill chain, the case covers weaponization of a pretext, delivery by email and actions on objectives as payment. There is no exploitation or installation, which explains why technical tools saw nothing unusual.

### Worked example

Priya's timeline shows the lookalike domain was registered four days before the email. Her report: "Payment fraud using a lookalike insurer domain (high confidence on sequence). No evidence of BIB system compromise. Insurer mailbox compromise not excluded. Recommend mandatory call-back for all bank-detail changes and lookalike monitoring for insurer partners."

> **Synthetic case.** The fraud is invented.

### Errors and limits

Missing logs at partners limit conclusions; state them.

### Exercises

- **EX036 — Timeline order.** Order the case's events. *Rubric:* 3 = registration, email, payment, second request, call-back, confirmation; 2 = mostly; 1 = muddled; 0 = none.
- **EX037 — Technique map.** Map the registration and email to ATT&CK. *Rubric:* 3 = T1583; T1566; 2 = one; 1 = wrong; 0 = none.
- **EX038 — Diamond vertices.** Fill the Diamond vertices for the case. *Rubric:* 3 = all four correct; 2 = three; 1 = one; 0 = none.
- **EX039 — Open question.** What remained uncertain, and how should it be resolved? *Rubric:* 3 = insurer mailbox compromise; ask insurer through channels; 2 = one; 1 = none; 0 = none.
- **EX040 — Recommendation.** What two recommendations followed? *Rubric:* 3 = mandatory call-back; lookalike monitoring for partners; 2 = one; 1 = vague; 0 = none.

### Synthesis

Build a UTC timeline, map to models, state confidence and gaps, share sanitised lessons and accept review.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) write reports for different audiences; (2) express uncertainty honestly; (3) handle ethical dilemmas in reporting; (4) apply handling labels to every product.

### 9.1 Bottom line first

Start with the judgment and the action. Detail follows for those who need it.

Section nine point one develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point one, FSSG expects communication claims to carry owners and dates.

Section nine point one treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point one, Bramwell Insurance Brokers will not accept communication work without a written trail.

### 9.2 Audiences

Managing director: risk and decisions. Operations: process changes. IT: technical details. Staff: what to look for and how to report.

Section nine point two develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point two, FSSG expects communication claims to carry owners and dates.

Section nine point two treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point two, Bramwell Insurance Brokers will not accept communication work without a written trail.

### 9.3 Uncertainty

Use the agreed probability words and a confidence level, and say what would change the judgment. ICD 203 standards — sourcing, uncertainty, alternatives, logic — make a good self-check.

Section nine point three develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point three, FSSG expects communication claims to carry owners and dates.

Section nine point three treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point three, Bramwell Insurance Brokers will not accept communication work without a written trail.

### 9.4 Labels

Every product carries a TLP label in the header. Staff awareness notes are usually CLEAR internally; FSSG-derived detail may be AMBER.

Section nine point four develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point four, FSSG expects communication claims to carry owners and dates.

Section nine point four treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point four, Bramwell Insurance Brokers will not accept communication work without a written trail.

### 9.5 Ethical dilemmas

Pressure to make a threat sound bigger to win budget; pressure to downplay an incident to avoid embarrassment. Both damage trust. Report what the evidence supports.

Section nine point five develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point five, FSSG expects communication claims to carry owners and dates.

Section nine point five treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point five, Bramwell Insurance Brokers will not accept communication work without a written trail.

### 9.6 Naming people

Reports name roles, not staff who clicked a link. Blame discourages reporting.

Section nine point six develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point six, FSSG expects communication claims to carry owners and dates.

Section nine point six treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point six, Bramwell Insurance Brokers will not accept communication work without a written trail.

### 9.7 Clients

Client details stay out of intelligence products; the compliance officer manages client communications.

Section nine point seven develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point seven, FSSG expects communication claims to carry owners and dates.

Section nine point seven treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point seven, Bramwell Insurance Brokers will not accept communication work without a written trail.

### 9.8 Length

One page for most products; appendices for detail.

Section nine point eight develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point eight, FSSG expects communication claims to carry owners and dates.

Section nine point eight treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point eight, Bramwell Insurance Brokers will not accept communication work without a written trail.

Section nine point eight fails closed if communication evidence is missing rather than guessing.

### 9.9 Review

A colleague reads each management report before release.

Section nine point nine develops communication ethics and reporting with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section nine point nine, FSSG expects communication claims to carry owners and dates.

Section nine point nine treats bottom line first audiences as testable only when evidence and ticket IDs are recorded.

For section nine point nine, Bramwell Insurance Brokers will not accept communication work without a written trail.

Section nine point nine fails closed if communication evidence is missing rather than guessing.

### Report structure

A standard structure helps readers find things: label and date; bottom line; key judgments with likelihood and confidence; evidence summary; recommended actions with owners; gaps and next steps. Priya keeps a template so every report looks the same, which saves her time and lets the managing director read each one in under two minutes. When a report needs more detail, she adds an appendix rather than lengthening the main page, so the bottom line stays visible at the top.

### Worked example

After the fraud case, a director asks Priya to describe it as "a sophisticated cyber attack" in the board report. Priya explains the evidence shows a simple lookalike-domain pretext, and that accurate wording helps the board fund the right control — payment verification — rather than expensive technical tools.

> **Synthetic case.** The exchange is invented.

### Errors and limits

Plain words can oversimplify; keep detail available.

### Exercises

- **EX041 — Board wording.** Why did Priya resist "sophisticated cyber attack"? *Rubric:* 3 = inaccurate; misdirects investment; 2 = partial; 1 = agreed; 0 = none.
- **EX042 — Naming staff.** Why name roles rather than staff who clicked? *Rubric:* 3 = blame discourages reporting; 2 = partial; 1 = name them; 0 = none.
- **EX043 — Self-check standards.** Name three ICD 203-style checks for a report. *Rubric:* 3 = three valid; 2 = two; 1 = one; 0 = none.
- **EX044 — Audience fit.** What does the operations manager need from a report? *Rubric:* 3 = process change implications/actions; 2 = partial; 1 = indicators; 0 = none.
- **EX045 — Label placement.** Where must the TLP label appear in a product? *Rubric:* 3 = header (and email subject); every product; 2 = partial; 1 = optional; 0 = none.

### Synthesis

Lead with the bottom line, fit the audience, state uncertainty, label every product and resist pressure to distort.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Threat intelligence and OSINT: quality and troubleshooting

### Learning outcomes

You will (1) measure the quality of CTI products; (2) detect and fix common faults; (3) collect consumer feedback; (4) improve continuously.

### 10.1 Quality dimensions

Relevance, timeliness, accuracy, clarity and actionability. Each can be checked: was the item about BIB systems? delivered before it mattered? confirmed or withdrawn later? understood? acted on?

Section ten point one develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point one, FSSG expects threat claims to carry owners and dates.

Section ten point one treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point one, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 10.2 Common faults

Stale indicators causing false blocks; missed items because email alerts went to spam; wrong labels; notes without clear actions.

Section ten point two develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point two, FSSG expects threat claims to carry owners and dates.

Section ten point two treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point two, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 10.3 Troubleshooting

Trace the item's path: received, triaged, analysed, sent, acted. Find where it stopped.

Section ten point three develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point three, FSSG expects threat claims to carry owners and dates.

Section ten point three treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point three, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 10.4 Feedback

Quarterly two-question forms; quick chats with the help desk. "What helped? What was noise?"

Section ten point four develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point four, FSSG expects threat claims to carry owners and dates.

Section ten point four treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point four, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 10.5 Improvements

One change per month: shorter notes, earlier scam updates, new lookalike monitoring.

Section ten point five develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point five, FSSG expects threat claims to carry owners and dates.

Section ten point five treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point five, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 10.6 Accuracy tracking

Record judgments with probability words; later note what happened. Over time, see if "likely" events happened more often than "unlikely" ones.

Section ten point six develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point six, FSSG expects threat claims to carry owners and dates.

Section ten point six treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point six, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 10.7 Source review

Each quarter, review sources: items received, used, withdrawn.

Section ten point seven develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point seven, FSSG expects threat claims to carry owners and dates.

Section ten point seven treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point seven, Bramwell Insurance Brokers will not accept threat work without a written trail.

Section ten point seven fails closed if threat evidence is missing rather than guessing.

### 10.8 False positives

When a block is wrong, remove it quickly, apologise, find the cause, adjust rules.

Section ten point eight develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point eight, FSSG expects threat claims to carry owners and dates.

Section ten point eight treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point eight, Bramwell Insurance Brokers will not accept threat work without a written trail.

### 10.9 Documentation

Keep a short improvement log.

Section ten point nine develops threat intelligence and osint quality with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section ten point nine, FSSG expects threat claims to carry owners and dates.

Section ten point nine treats quality dimensions common faults as testable only when evidence and ticket IDs are recorded.

For section ten point nine, Bramwell Insurance Brokers will not accept threat work without a written trail.

Section ten point nine fails closed if threat evidence is missing rather than guessing.

### Peer comparison

Twice a year Priya swaps an anonymised product with a peer at another FSSG member and each reviews the other's work against the same quality dimensions. The outside view catches habits she no longer notices, such as long sentences or vague actions, and gives her ideas from a team facing similar threats with different tools. The peer review is covered by FSSG's sharing agreement, and only TLP:GREEN or CLEAR material is exchanged.

### Worked example

The help desk says scam updates arrive on Wednesday, after Monday's peak of suspicious calls. Priya moves the update to Monday morning using the previous week's data. Calls needing escalation fall slightly over the next month; she records the change and result in her improvement log.

> **Synthetic case.** The change is invented.

### Errors and limits

Small teams have small samples; treat measures as indicators.

### Exercises

- **EX046 — Quality list.** Name five quality dimensions. *Rubric:* 3 = relevance, timeliness, accuracy, clarity, actionability; 2 = three; 1 = one; 0 = none.
- **EX047 — Spam fault.** How would Priya find that FSSG alerts were going to spam? *Rubric:* 3 = trace path; item received? check mail filters; 2 = partial; 1 = guess; 0 = none.
- **EX048 — Timing change.** Why move the scam update to Monday? *Rubric:* 3 = match call peak; 2 = partial; 1 = random; 0 = none.
- **EX049 — Calibration over time.** How can Priya check her probability words? *Rubric:* 3 = record judgments and outcomes; compare frequencies; 2 = partial; 1 = ask manager; 0 = none.
- **EX050 — Wrong block.** List the steps after a wrong block. *Rubric:* 3 = remove quickly, apologise, find cause, adjust; 2 = three; 1 = one; 0 = none.

### Synthesis

Measure quality, trace faults, gather feedback, make one improvement at a time and track accuracy.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) run an automated pre-release check on a brief; (2) fix failures before release; (3) explain each check's purpose; (4) extend checks responsibly.

### 11.1 Lab rules

Offline, synthetic, standard library. The supervisor reviews outputs and the corrected brief.

Section eleven point one develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point one, FSSG expects supervised claims to carry owners and dates.

Section eleven point one treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point one, Bramwell Insurance Brokers will not accept supervised work without a written trail.

Section eleven point one fails closed if supervised evidence is missing rather than guessing.

### Lab — brief release check

```python
"""Lab (ch 11): assemble a one-page brief and refuse to release it if checks fail (synthetic)."""
brief = {"tlp": "TLP:GREEN", "bluf": "Phishing against broker portals is likely to continue this month.",
         "confidence": "moderate", "actions": ["Block 3 sender domains", "Remind staff about portal logins"],
         "text": "Sample sent to j.smith@bramwell.example was reported."}
checks = [("label valid", brief["tlp"] in {"TLP:CLEAR", "TLP:GREEN", "TLP:AMBER", "TLP:AMBER+STRICT", "TLP:RED"}),
          ("bottom line first", bool(brief["bluf"])),
          ("confidence stated", brief["confidence"] in {"low", "moderate", "high"}),
          ("actions listed", len(brief["actions"]) > 0),
          ("no staff email", "@bramwell.example" not in brief["text"])]
for name, ok in checks:
    print(f"{name}: {'pass' if ok else 'FAIL'}")
print("release" if all(ok for _, ok in checks) else "HOLD: fix failures before release")
```

Run with `python3 lab_brief.py`. Verified output:

```text
label valid: pass
bottom line first: pass
confidence stated: pass
actions listed: pass
no staff email: FAIL
HOLD: fix failures before release
```

### 11.2 Reading the result

The brief has a valid TLP:GREEN label, a bottom line first, a confidence level and listed actions. It fails one check: the text contains a staff email address at bramwell.example. The script holds the release until the failure is fixed.

Section eleven point two develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point two, FSSG expects supervised claims to carry owners and dates.

Section eleven point two treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

### 11.3 Fixing

Replace "j.smith@bramwell.example" with "a staff member". Rerun: all checks pass and the script prints "release".

Section eleven point three develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point three, FSSG expects supervised claims to carry owners and dates.

Section eleven point three treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point three, Bramwell Insurance Brokers will not accept supervised work without a written trail.

### 11.4 Why each check

Label: wrong or missing labels cause leaks. Bottom line: busy readers act on the first sentence. Confidence: readers need to know how sure we are. Actions: intelligence without action is news. Staff email: personal data does not belong in a GREEN community product.

Section eleven point four develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point four, FSSG expects supervised claims to carry owners and dates.

Section eleven point four treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

### 11.5 Limits of checks

The script finds email addresses only for BIB's domain; it misses names and client addresses. A human read remains mandatory.

Section eleven point five develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point five, FSSG expects supervised claims to carry owners and dates.

Section eleven point five treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Bramwell Insurance Brokers will not accept supervised work without a written trail.

### 11.6 Extending

Students may add a check for phone numbers, or for probability words outside the agreed scale. Each new check gets a test case.

Section eleven point six develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point six, FSSG expects supervised claims to carry owners and dates.

Section eleven point six treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Bramwell Insurance Brokers will not accept supervised work without a written trail.

### 11.7 Holding is safe

The script holds rather than releases when anything fails — a fail-closed design.

Section eleven point seven develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point seven, FSSG expects supervised claims to carry owners and dates.

Section eleven point seven treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point seven, Bramwell Insurance Brokers will not accept supervised work without a written trail.

Section eleven point seven fails closed if supervised evidence is missing rather than guessing.

### 11.8 Lab report

Record the first run, the fix, the second run and one proposed extension with its test case.

Section eleven point eight develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point eight, FSSG expects supervised claims to carry owners and dates.

Section eleven point eight treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point eight, Bramwell Insurance Brokers will not accept supervised work without a written trail.

### 11.9 Supervisor sign-off

The supervisor signs only after reading the corrected brief.

Section eleven point nine develops supervised laboratory with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section eleven point nine, FSSG expects supervised claims to carry owners and dates.

Section eleven point nine treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point nine, Bramwell Insurance Brokers will not accept supervised work without a written trail.

Section eleven point nine fails closed if supervised evidence is missing rather than guessing.

### Running in practice

After the lab, Priya runs the check on every real brief before release, on her work machine, with the output saved to the ticket.

### Worked example

Priya extends the check to flag any probability word not on BIB's scale. Her test brief uses "probable" and the check fails as intended; she rewrites it as "likely" and the brief passes.

> **Synthetic case.** The brief and extension are invented teaching material.

### Errors and limits

Automated checks catch patterns, not meaning.

### Exercises

- **EX051 — Lab failure.** Which check failed and why? *Rubric:* 3 = no staff email; address in text; 2 = check only; 1 = label; 0 = none.
- **EX052 — Fix and rerun.** How is the failure fixed and confirmed? *Rubric:* 3 = replace with role; rerun shows release; 2 = one; 1 = ignore; 0 = none.
- **EX053 — Check purposes.** Explain why the confidence check exists. *Rubric:* 3 = readers need to know certainty; 2 = partial; 1 = decoration; 0 = none.
- **EX054 — Missed by script.** Name something the script would miss. *Rubric:* 3 = names, client addresses, other domains; 2 = vague; 1 = nothing; 0 = none.
- **EX055 — New check.** Propose a new check with a test case. *Rubric:* 3 = check + failing test + passing test; 2 = check + one test; 1 = check only; 0 = none.

### Synthesis

Automate simple pre-release checks, hold on failure, fix and rerun, and keep a human read for what scripts miss.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a CTI practice portfolio; (2) reflect on growth and gaps; (3) plan the next six months of the role; (4) hand over or sustain the routine.

### 12.1 Portfolio contents

Requirements list; weekly routine and ticket samples (sanitised); triage scoring with a review; the fraud case report; a control request with verification; a management report; the improvement log; the lab outputs.

Section twelve point one develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point one, FSSG expects practice claims to carry owners and dates.

Section twelve point one treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

### 12.2 Sanitising

All portfolio items use synthetic or sanitised content. FSSG material appears only as GREEN summaries or not at all. Staff and clients are never named.

Section twelve point two develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point two, FSSG expects practice claims to carry owners and dates.

Section twelve point two treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

For section twelve point two, Bramwell Insurance Brokers will not accept practice work without a written trail.

### 12.3 Reflection

What changed at BIB because of CTI? Call-back verification, MFA for remote email, lookalike monitoring. What remains weak? Partner mailbox compromise, limited log retention.

Section twelve point three develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point three, FSSG expects practice claims to carry owners and dates.

Section twelve point three treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

For section twelve point three, Bramwell Insurance Brokers will not accept practice work without a written trail.

### 12.4 Next six months

Extend lookalike monitoring to insurer partners; formalise FSSG feedback; train the IT manager as backup; review requirements with the new operations manager.

Section twelve point four develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point four, FSSG expects practice claims to carry owners and dates.

Section twelve point four treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Bramwell Insurance Brokers will not accept practice work without a written trail.

### 12.5 Sustaining

Document the routine, keep templates, schedule reviews and keep the manager's support by showing outcomes.

Section twelve point five develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point five, FSSG expects practice claims to carry owners and dates.

Section twelve point five treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Bramwell Insurance Brokers will not accept practice work without a written trail.

### 12.6 Assessment

The portfolio is assessed on safety, accuracy, usefulness and reflection, using the course rubric.

Section twelve point six develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point six, FSSG expects practice claims to carry owners and dates.

Section twelve point six treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

For section twelve point six, Bramwell Insurance Brokers will not accept practice work without a written trail.

### 12.7 Continuing learning

Follow ATT&CK and TLP updates, attend FSSG meetings, read sector advisories and consider the technical or postgraduate courses.

Section twelve point seven develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point seven, FSSG expects practice claims to carry owners and dates.

Section twelve point seven treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

For section twelve point seven, Bramwell Insurance Brokers will not accept practice work without a written trail.

### 12.8 Mentoring

Explaining the routine to a colleague confirms that it is documented well enough to survive absence.

Section twelve point eight develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point eight, FSSG expects practice claims to carry owners and dates.

Section twelve point eight treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

For section twelve point eight, Bramwell Insurance Brokers will not accept practice work without a written trail.

### 12.9 Celebrate

Note concrete wins: a prevented payment, a blocked lookalike, an avoided outage.

Section twelve point nine develops practice portfolio and final review with a Bramwell Insurance Brokers note Priya Nair can demo offline.

Under section twelve point nine, FSSG expects practice claims to carry owners and dates.

Section twelve point nine treats portfolio contents sanitising reflection as testable only when evidence and ticket IDs are recorded.

For section twelve point nine, Bramwell Insurance Brokers will not accept practice work without a written trail.

### Feedback from consumers

Before the final review, Priya asks each consumer for one sentence on what CTI changed for them. The operations manager cites call-back verification; the help desk cites Monday scam updates. These quotes, kept anonymous, strengthen the portfolio's evidence.

### Worked example

Priya's portfolio review shows twelve control changes traced to intelligence in six months, two prevented fraud attempts reported by operations and one false-positive block, fixed within an hour. Her plan names the IT manager as trained backup and schedules a requirements review in January.

> **Synthetic case.** The figures are invented.

### Errors and limits

Portfolios show selected work; assessors may ask to see routine samples.

### Exercises

- **EX056 — Portfolio list.** List six portfolio items. *Rubric:* 3 = six valid; 2 = four; 1 = two; 0 = none.
- **EX057 — Sanitising rule.** How should FSSG material appear in the portfolio? *Rubric:* 3 = only GREEN summaries or not at all; no names; 2 = partial; 1 = full; 0 = none.
- **EX058 — Remaining weakness.** Name two remaining weaknesses at BIB. *Rubric:* 3 = partner mailbox compromise; log retention; 2 = one; 1 = none; 0 = none.
- **EX059 — Six-month plan.** Give three items for the next six months. *Rubric:* 3 = three valid; 2 = two; 1 = one; 0 = none.
- **EX060 — Concrete wins.** Why record concrete wins? *Rubric:* 3 = show value, keep support/budget; 2 = partial; 1 = vanity; 0 = none.

### Synthesis

Assemble a sanitised portfolio, reflect honestly, plan ahead, build backup and show concrete value.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Bramwell Insurance Brokers, Priya Nair, the Financial Services Sharing Group and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Risk is the likelihood of harm combined with its impact; CTI improves the likelihood estimate by showing which threats are active and relevant.

**EX002.** Monday direction and collection from FSSG; Tuesday processing and log matching; Wednesday analysis and dissemination to the help desk; monthly feedback and summary to the manager.

**EX003.** Reverse-engineering malware and attributing attacks to named groups.

**EX004.** Business email compromise, credential phishing against the client portal and ransomware.

**EX005.** ATT&CK catalogues techniques; the kill chain orders intrusion phases; the Diamond Model describes an event by adversary, capability, infrastructure and victim.

**EX006.** The managing director sets budgets; the operations manager sets payment processes; the IT team configures controls.

**EX007.** "Each month, for the compliance officer, are any BIB staff credentials or client records being offered or published on public sites?"

**EX008.** Introducing call-back verification before acting on any change to bank details.

**EX009.** Active exploitation of a system BIB runs, or a fraud method that targets BIB by name.

**EX010.** It is outside CTI's requirements and would intrude on the client's privacy without lawful purpose.

**EX011.** Contacting police, requesting takedowns, notifying regulators and engaging with suspected criminals (also buying intelligence services).

**EX012.** Save the original message file, record who reported it and when, compute its hash, and analyse only a copy.

**EX013.** Only people inside BIB who need to know.

**EX014.** The compliance officer, because notification duties to clients involve regulation and data-protection law.

**EX015.** They breach platform terms and possibly law, are deceptive, and expose BIB to legal and reputational harm.

**EX016.** C — fairly reliable — until its track record can be checked; it can move up or down later.

**EX017.** A portal update or password-policy change that locked many legitimate clients out.

**EX018.** 55–80%.

**EX019.** The evidence supported the update as the main cause, but some attempts came from flagged addresses, so ignoring the attack possibility would be unsafe.

**EX020.** What happened; what it means for BIB with likelihood and confidence; and what action is needed by whom.

**EX021.** Q3 (8) and Q1 (7) go to analysis; Q4 (5) is checked; Q5 and Q2 (4 each) are logged only.

**EX022.** Ask FSSG or a contracted provider whether any sample contains BIB data, rather than visiting the forum herself.

**EX023.** A planned CRM upgrade next week that would remove the vulnerable version anyway.

**EX024.** The domain might be a legitimate new marketing site registered by BIB staff or an agency.

**EX025.** A written record of the change, the reason and a later check that it improved results.

**EX026.** Arrival date, source, TLP label, grade, score and decision (also actions and closure date).

**EX027.** Active exploitation of a system BIB runs, or a fraud method that names BIB.

**EX028.** When the action is complete and verified, or when a reasoned decision not to act is recorded.

**EX029.** Drop the lowest-scored items first and tell her manager about the overflow.

**EX030.** She phoned the IT manager, opened a priority ticket, informed her manager; the fix was applied that evening, she verified the version next morning and closed the ticket with evidence.

**EX031.** Call-back verification for bank-detail changes, dual approval for payments and staff awareness of pretexts.

**EX032.** Ask operations to show that call-backs were made for each bank-detail change during the period.

**EX033.** The domain could belong to an insurer partner, and blocking it would disrupt business.

**EX034.** Sign-in logs showed the second factor being requested for every pilot user's login.

**EX035.** It shows which changes came from intelligence, supports reviews and expiry, and evidences the programme's value.

**EX036.** Lookalike domain registered; email received; first payment made; second request received; call-back performed; fraud confirmed.

**EX037.** Registering the lookalike domain is Acquire Infrastructure (T1583); the email is Phishing (T1566) delivering the pretext.

**EX038.** Adversary: unknown fraud group. Capability: bank-detail-change pretext. Infrastructure: lookalike domain and receiving bank account. Victim: BIB finance team.

**EX039.** Whether the insurer's own mailbox was compromised; BIB should ask the insurer through its formal contacts.

**EX040.** Make call-back verification mandatory for every bank-detail change, and monitor for lookalike domains of insurer partners.

**EX041.** It was inaccurate — a simple lookalike pretext — and would push the board toward technical spending instead of payment verification.

**EX042.** Blaming individuals makes staff hide mistakes and stop reporting suspicious messages.

**EX043.** Describe source quality, express uncertainty with confidence, and consider alternative explanations.

**EX044.** What process change is recommended, why, and what it costs the team in effort.

**EX045.** In the header of every product, and in the subject line when sent by email.

**EX046.** Relevance, timeliness, accuracy, clarity and actionability.

**EX047.** By tracing an expected item: if it never reached triage, check whether it arrived and inspect mail filter quarantine and spam folders.

**EX048.** Suspicious calls peak on Monday, so an update on Wednesday arrived after it was most needed.

**EX049.** Log each judgment's probability word and later outcome, then compare how often each word's events actually happened.

**EX050.** Remove the block quickly, apologise to affected users, find why it happened and adjust the rule or source.

**EX051.** "No staff email" failed because the text contained j.smith@bramwell.example.

**EX052.** Replace the address with a role such as "a staff member", then rerun; all checks pass and the script prints "release".

**EX053.** Readers must know how certain the judgment is to decide how strongly to act on it.

**EX054.** Personal names without email addresses, client addresses or email addresses at other domains.

**EX055.** Check: phone numbers absent. Failing test: "call 01632 960123". Passing test: "call the help desk".

**EX056.** Requirements list, sanitised ticket samples, triage scoring review, fraud case report, control request with verification and management report.

**EX057.** Only as TLP:GREEN summaries, or left out, with no staff or client names.

**EX058.** Possible compromise of partner insurers' mailboxes, and short log retention limiting investigations.

**EX059.** Extend lookalike monitoring to insurer partners, train the IT manager as backup and review requirements with the new operations manager.

**EX060.** Concrete outcomes show leadership the role's value and keep support and time allocated to it.

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
