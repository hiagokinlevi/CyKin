# Threat Intelligence and OSINT: A Bachelor's Book

- Language: English (`en`); bachelor's course, four years.
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; seven offline labs use only the Python 3 standard library on synthetic data, with outputs embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: undergraduates preparing to work as junior cyber threat intelligence (CTI) analysts or to continue into research.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical boundary: no collection on real private individuals, no terms-of-service evasion, no deanonymisation, no contact with adversary infrastructure. Organisations, people and indicators are **synthetic** unless a sentence cites a public source; addresses use RFC 5737 ranges and domains use `.example`.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–18 build reasoning, computing, writing, privacy, evidence and research foundations through intelligence examples. Chapters 19–32 teach CTI and OSINT theory, cases, models, data, methods, controls, verification, failure analysis, operations and interfaces, with two laboratories. Chapters 33–40 cover research methods, a comparative project, the capstone, community practice, evidence review and the thesis. Each chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, three exercises scored 0–3, a synthesis and a **Continue studying** block.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Halden County Health Trust (HCHT)** — three hospitals, a regional laboratory and a patient portal | Organisation served by CTI | Invented |
| **Amara Diallo** | Undergraduate on a part-time internship in HCHT's security team | Invented |
| **Health Sector Sharing Circle (HSSC)** | Regional community exchanging intelligence under TLP 2.0 | Invented |

### Core sources

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) and [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); Hutchins et al. [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf); NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) distinguish deduction, induction and abduction in intelligence work; (2) spot common fallacies in threat reporting; (3) use proportions and ratios correctly; (4) state the assumptions behind a conclusion.

### 1.1 Three kinds of inference

Deduction moves from rules to certain conclusions: if every TLP:RED report goes only to named recipients and Amara is not named, she may not read it. Induction generalises from cases: five sector reports began with phishing, so phishing is a common entry route. Abduction proposes the best explanation for an observation: a burst of failed logins at night may be password guessing. Intelligence analysis relies heavily on abduction, which is why its conclusions must be stated with uncertainty.

Amara labels each conclusion with the inference that produced it.

### 1.2 Fallacies in reports

Post hoc reasoning: an outage followed a phishing email, so the email caused it. Base-rate neglect: a detector with a 99% hit rate sounds decisive until you remember how rare real attacks are. Survivorship: studying only incidents that were detected tells you little about those that were not. Naming the fallacy in a peer's draft is a useful review skill.

In Amara's first review of an HSSC draft, she marks one sentence that blames a ransomware outbreak on a supplier because the supplier's update came the day before. The draft offers no other link. She suggests rewording it as a hypothesis and listing what evidence would confirm or rule it out, which turns a fallacy into a useful question for the next analyst.

### 1.3 Proportions and ratios

"Phishing appeared in 3 of 5 reports" is a proportion, 60%. Reporting "60%" alone hides that the sample is five. Always give the numerator and the denominator, especially when the denominator is small.

Amara writes "3 of 5 reports" in her notes and adds the period they cover. When a later quarter brings twenty reports, the proportion can be compared fairly, and readers can see that the first figure rested on very few cases. A percentage from five items can swing by twenty points with one more report, so presenting it alone suggests far more precision than the evidence has.

### 1.4 Assumptions

Every conclusion rests on assumptions. Writing them down — the reports are representative; the timestamps are accurate — lets readers judge how far to trust the result.

Amara keeps a short list of assumptions at the end of each note she writes for HCHT's security team. When one turns out to be wrong, such as a feed whose timestamps use a different time zone, she can see at once which conclusions depended on it and revise only those. Unstated assumptions are the hardest errors to find, because nobody knows to check them.

### Estimating before computing

Before running numbers, Amara writes a rough expectation: about half the sector reports will mention phishing. If the computed figure is wildly different, she checks the data and the code before believing the surprise. Rough estimates catch spreadsheet errors, duplicated rows and misread columns early.

### Worked example

A vendor blog claims "ransomware attacks on hospitals rose 300%". Amara asks: 300% of what baseline, over what period, counted how? The blog counts publicly reported incidents, which may rise because reporting rules changed. She records the claim as "reported incidents increased; underlying rate unknown".

> **Synthetic case.** The blog claim is invented; HCHT is fictional.

### Errors and limits

Logic tidies reasoning but cannot replace evidence. Percentages from tiny samples mislead even when arithmetic is right.

### Exercises

- **EX001 — Inference type.** Which kind of inference is "night-time failed logins suggest password guessing"? *Rubric:* 3 = abduction (best explanation), with reason; 2 = name only; 1 = deduction; 0 = none.
- **EX002 — Spot the fallacy.** "The outage happened after the phishing email, so the email caused it." Name the fallacy. *Rubric:* 3 = post hoc ergo propter hoc, with why; 2 = name only; 1 = wrong fallacy; 0 = none.
- **EX003 — Baseline question.** List three questions to ask about "attacks rose 300%". *Rubric:* 3 = baseline, period, counting method (or reporting change); 2 = two; 1 = one; 0 = none.

### Synthesis

Name your inference type, catch fallacies, give numerators with percentages and write assumptions down.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the components of a hospital's computing estate relevant to CTI; (2) explain what logs each component produces; (3) identify where indicators can be checked; (4) recognise medical devices as special cases.

### 2.1 The estate

HCHT runs staff workstations, clinical applications, a patient portal, email, a directory service, cloud mailboxes, laboratory systems and networked medical devices. Each has owners, update routes and logs. CTI is only useful if it reaches the place where it can be checked or enforced.

Amara's first task is to list, for each part of the estate, who owns it, how it is updated and what it logs. The list shows where intelligence can be used quickly, such as email filtering, and where it cannot, such as laboratory systems run by a supplier under contract.

### 2.2 Logs as sensors

Email gateways log senders and attachments; web proxies log URLs; DNS resolvers log lookups; endpoints log processes; the directory logs logons. When HSSC shares a malicious domain, Amara can search DNS and proxy logs for past contacts — a retrospective hunt.

A retrospective hunt answers a simple question: did anything at HCHT contact this domain before we knew it was malicious? Amara checks that log retention covers the period the HSSC report describes, since a hunt cannot find contacts older than the oldest log. Where retention is short, she notes the gap rather than reporting a clean result.

### 2.3 Enforcement points

Email filters, DNS blocking, proxy categories and endpoint rules can act on indicators. Each has a different blast radius. Blocking a domain at DNS affects every device that uses the resolver, including clinical systems.

A wrong block at DNS could stop a clinical application from reaching a supplier's service and delay patient care. Amara therefore records, for each enforcement point, who can change it, how quickly a block can be reversed and which systems it affects. Indicators with low confidence go to monitoring first, where they raise alerts without stopping traffic, until the evidence supports a block.

### 2.4 Medical devices

Infusion pumps and imaging systems often run old operating systems and cannot be patched quickly. They may not tolerate scanning or agent software. CTI about threats to such devices goes to the clinical engineering team, who decide on network isolation rather than host changes.

Amara learns that patient safety comes first: a security change that stops a pump working is worse than the threat it was meant to address. Intelligence about these devices is phrased for clinical engineers, naming the device model and the exposure, and they decide what change is safe for patients.

### 2.5 Asset inventory

An accurate inventory lets analysts answer "do we run the affected product?" within minutes when an advisory arrives. Without it, every advisory triggers a guessing exercise.

HCHT's inventory lists software products and versions for workstations and servers, but medical devices are recorded by model only, so Amara notes that advisories about device software need extra checking with clinical engineering. Keeping the inventory current is an operations task; Amara's role is to report where gaps slowed an answer, so that the owners can fix them.

### Cloud and supplier systems

Some HCHT services run on supplier platforms: cloud mail, the appointment portal and pathology software. Their logs sit with the supplier. Contracts should state what logs HCHT can obtain and how fast, because an indicator hunt is impossible without access to the relevant records.

### Worked example

HSSC shares an advisory about a vulnerable imaging-server product. Amara queries the inventory: two servers at one hospital match. She sends the advisory to clinical engineering with the asset identifiers, rather than to the general IT queue, because the servers are certified medical systems.

> **Synthetic case.** The advisory and servers are invented.

### Errors and limits

Inventories go stale; confirm with owners. Do not scan medical devices without clinical engineering approval.

### Exercises

- **EX004 — Log source.** Which log would show whether any HCHT device looked up a malicious domain last week? *Rubric:* 3 = DNS resolver logs (proxy as secondary); 2 = proxy only; 1 = endpoint antivirus; 0 = none.
- **EX005 — Device route.** Why did Amara route the imaging advisory to clinical engineering? *Rubric:* 3 = certified medical systems; special change/safety process; owners; 2 = owners only; 1 = convenience; 0 = none.
- **EX006 — Blast radius.** Give one risk of blocking a domain at the DNS resolver in a hospital. *Rubric:* 3 = may break clinical systems relying on it/collateral; 2 = vague; 1 = no risk; 0 = none.

### Synthesis

Know the estate, its logs and enforcement points, treat medical devices separately and keep the inventory current.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write Python functions that clean and classify indicators; (2) use strings, lists, sets and dictionaries; (3) handle bad input explicitly; (4) keep scripts free of network collection.

### 3.1 Why analysts program

Analysts receive indicators in emails, PDFs and spreadsheets. Small scripts extract, clean and compare them faster and more accurately than copying by hand. Programming here is a reading and checking tool, not a collection tool.

Amara writes her first script to read indicators from a spreadsheet shared by HSSC, remove duplicates and compare them with a list exported from the email gateway. Done by hand, the comparison took an hour and missed two matches; the script takes seconds and gives the same answer each time it runs.

### 3.2 Types for intelligence

A string holds one indicator. A list keeps order, such as events in time. A set removes duplicates and supports intersection — which indicators appear in both our logs and the feed? A dictionary maps an indicator to its metadata: source, TLP, first seen.

Choosing the right type makes the question easy to answer. Amara's script stores feed indicators in a set, so the overlap with HCHT's logs is a single intersection, and keeps metadata in a dictionary, so each match comes with its source and TLP label. Without the label, she could not tell which matches may be shared with other teams.

### 3.3 Classifying values

A simple function decides whether a string looks like an IPv4 address, a domain or a hash. The standard library's `ipaddress` module validates addresses; length and character checks distinguish SHA-256 hashes (64 hexadecimal characters) from other strings.

Amara tests the function with examples of each type and with tricky cases, such as a domain that contains digits or a hash with uppercase letters. A misclassified value could send a domain to an address blocklist, where it would do nothing, while the analyst believed it was blocked.

### 3.4 Explicit failure

If a value fits no type, return "unknown" and keep it for review. Guessing creates false indicators that may later block legitimate services.

Amara's script writes unknown values to a separate file with the line they came from, so she can check them by hand. Many turn out to be defanged indicators, such as domains with brackets around the dots, which the script now handles explicitly. Explicit failure turned a silent error into a list of improvements and kept false indicators out of the blocklists.

### 3.5 No hidden collection

Scripts in this course read local files only. Code that fetches web pages, queries external services or logs into platforms is outside this chapter and requires terms, permission and supervision.

Amara asks two questions of her own work: where does each input come from, and was she allowed to use it? Her scripts take files that HSSC or HCHT systems have already provided, which keeps her inside the permissions of her internship. Any collection step is a separate decision for her supervisor, with its own approval and record.

### Readable code

Analysts share scripts with colleagues who must trust the output. Clear function names, short docstrings and a small test with known inputs make a script reviewable. A test such as feeding one valid hash, one truncated hash and one domain shows reviewers exactly how edge cases behave before the script touches real data.

### Worked example

Amara receives 40 values pasted from a PDF. Her classifier labels 18 domains, 12 IPv4 addresses, 7 SHA-256 hashes and 3 unknowns — two were truncated hashes and one a domain with a stray bracket from defanging. She fixes the bracket, reports the truncated hashes back to the sender and stores 38.

> **Synthetic case.** The PDF values are invented.

### Errors and limits

Pattern checks confirm shape, not maliciousness. A valid-looking domain can still be a typo.

### Exercises

- **EX007 — Pick a type.** Which Python type finds indicators present in both the feed and HCHT's logs, and how? *Rubric:* 3 = set intersection (&); 2 = set only; 1 = list loop without dedupe; 0 = none.
- **EX008 — Hash shape.** What shape does a SHA-256 hash have as text? *Rubric:* 3 = 64 hexadecimal characters; 2 = 64 characters; 1 = 32; 0 = none.
- **EX009 — Truncated value.** What should Amara do with the two truncated hashes? *Rubric:* 3 = mark unknown, do not store as indicators, report to sender; 2 = discard; 1 = pad and store; 0 = none.

### Synthesis

Use the right data type, validate shape, fail explicitly and keep scripts local.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) structure an argument with claim, evidence and reasoning; (2) cite sources correctly; (3) write with appropriate hedging; (4) adapt academic habits to intelligence writing.

### 4.1 Claim, evidence, reasoning

A paragraph makes one claim, presents evidence and explains why the evidence supports the claim. "Phishing is the most common entry route in HSSC reports (claim); it appears in 3 of 5 reports from 2026 (evidence); the other routes appear at most twice (reasoning)." Readers can then challenge the evidence rather than guess your meaning.

Amara uses this pattern in every paragraph of her reports. Her supervisor can then check the evidence quickly, and a reader who disagrees knows exactly which part to question. When a claim has no evidence yet, she labels it as a hypothesis and says what would test it.

### 4.2 Citation

Cite specifications for definitions (STIX 2.1 for object types), papers for models (Hutchins et al. for the kill chain), and data sources for numbers. Paraphrase and cite; quote only when exact wording matters. Never cite a TLP-restricted report in public coursework.

Amara keeps a reference list for each piece of coursework and checks that every TLP marking allows the use she makes of a source. For an essay on phishing in health care she cites public reports only, and describes HSSC trends in general terms without naming any restricted report, so the essay can be shared with her class.

### 4.3 Hedging

"Proves" is rarely justified. "Suggests", "is consistent with" and calibrated words such as "likely" signal uncertainty honestly. Over-hedging — "might possibly perhaps" — is as unhelpful as overclaiming.

Amara learns to choose one calibrated word per judgment and to say what it rests on, such as "likely, based on two independent reports". A reader can act on that, or ask for more evidence, which is the point of hedging honestly. She avoids stacking qualifiers, which hides the judgment rather than expressing its uncertainty.

### 4.4 Academic versus intelligence style

Academic writing often builds to a conclusion. Intelligence writing states the bottom line first. ICD 203 asks analytic products to be clear and logical; both styles share that aim but differ in order. Amara learns both.

In practice, Amara writes coursework essays in academic style and her HCHT notes with the bottom line in the first sentence, followed by the evidence. Busy readers in the security team may read only that first line, so it must be accurate on its own. Her supervisor checks that the evidence below actually supports it.

### 4.5 Revision

Read drafts aloud, cut words that do not change meaning, and ask a peer to restate your main claim.

Amara reads her first HCHT note aloud and finds two sentences that say the same thing. A peer restates her main claim as "block these domains" when she meant "monitor these domains", so she rewrites the opening line to make the action clear. Revision is where most of the clarity in a report comes from, and she plans time for it rather than treating it as optional.

### Writing for non-specialists

Clinical managers read HCHT security notes too. Replace jargon with plain words or define it once: 'phishing (fraudulent email that tricks people into acting)'. Short sentences, active voice and concrete actions — 'report suspicious invoices to the service desk' — make guidance usable by busy ward staff who have minutes, not hours, to read it.

### Worked example

Amara's first essay paragraph mixes three claims about phishing, ransomware and insiders. Her tutor asks for one claim per paragraph. She splits it into three, each with its own evidence, and moves her conclusion to the opening sentence for the intelligence-style version.

> **Synthetic case.** The essay is invented.

### Errors and limits

Citing a source does not make it reliable; assess it. Academic integrity rules forbid presenting others' analysis as your own.

### Exercises

- **EX010 — Build a paragraph.** Write a claim-evidence-reasoning paragraph about one ATT&CK technique in a fictional sector. *Rubric:* 3 = all three parts clear; 2 = two; 1 = claim only; 0 = none.
- **EX011 — Restricted source.** May Amara cite an HSSC TLP:AMBER report in a public essay? *Rubric:* 3 = no; use public sources or synthetic examples; 2 = no; 1 = yes with attribution; 0 = none.
- **EX012 — Order difference.** How does intelligence writing order differ from typical academic writing? *Rubric:* 3 = bottom line first vs build-up to conclusion; 2 = partial; 1 = no difference; 0 = none.

### Synthesis

One claim per paragraph, cite precisely and lawfully, hedge honestly and know when to lead with the conclusion.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) define threat, vulnerability, risk and control; (2) describe the CTI life cycle; (3) distinguish strategic, operational and tactical intelligence; (4) explain why healthcare is attractive to attackers.

### 5.1 Core terms

A threat is a potential cause of harm — an actor or event. A vulnerability is a weakness. Risk combines likelihood and impact. A control reduces risk. CTI informs the threat part of that equation so that controls go where they matter.

For HCHT, the threat is a criminal group sending phishing to clinical staff, the vulnerability is an unpatched remote access service and the risk is high because an outage would affect patient care. Intelligence about the group's methods helps decide which controls to strengthen first.

### 5.2 The CTI life cycle

Direction (what do decision-makers need?), collection, processing, analysis, dissemination and feedback. In practice, direction is often missing; analysts then collect everything and help no one. Priority intelligence requirements fix that.

Amara helps draft HCHT's first requirements with her supervisor: which threats could disrupt clinical services, which suppliers are targeted, and which techniques are seen in health-sector attacks. Each requirement names who needs the answer and how often. Collection then focuses on sources that answer them, and feedback shows whether the answers were useful, so the cycle improves over time.

### 5.3 Three levels

Strategic: trends and intent for executives — for example, criminal groups targeting hospitals for extortion. Operational: campaigns and timing for incident leads — a phishing wave against health trusts this month. Tactical: indicators and techniques for analysts — sender domains and T1566 Phishing.

Each level reaches a different audience and needs a different style. Amara practises writing the same HSSC report three ways: a short paragraph for the board, a page for incident leads and a list of indicators with techniques for analysts. Mixing levels, such as giving the board indicator lists, wastes the reader's time and hides what they need to decide.

### 5.4 Why healthcare

Hospitals hold sensitive data, run around the clock and cannot tolerate downtime, which increases pressure to pay extortion. Legacy systems and many suppliers widen exposure. Strategic intelligence helps boards understand this context without sensationalism.

Amara's briefing for HCHT's board uses sector reports to describe the threat accurately and links each point to a decision the board can take, such as funding faster recovery for clinical systems. She avoids alarming language and uses figures only when their source and sample are clear.

### 5.5 Intelligence versus information

A feed of domains is information. An assessment that a campaign targets laboratory systems and that HCHT should block specific domains and brief laboratory staff is intelligence — analysed and tied to a decision.

Amara checks every product she writes against this test: what decision does it support, and who makes it? A list she cannot connect to a decision is kept as information and stored for later searches, not sent as intelligence. This keeps the security team's inbox for material that asks something of them, and it helps HSSC see which of its shared items were actually used.

### Who consumes intelligence at HCHT

Consumers include the service desk, network team, clinical engineering, the data protection officer and the board. Each needs different detail at different speed. Mapping consumers and their decisions is the first practical step in direction, because it shows which questions intelligence must answer and in which format each audience can actually use the answer.

### Worked example

HCHT's chief executive asks whether the trust is "a target". Amara's supervisor answers at the strategic level: health organisations in the region have faced extortion campaigns; HCHT's exposure is typical; the main defensive priorities are phishing resistance and backups. Indicators are left out of the executive brief.

> **Synthetic case.** The briefing is invented.

### Errors and limits

Fear-driven briefings distort investment. Levels overlap; label the intended audience.

### Exercises

- **EX013 — Level label.** Classify "sender domains in this week's phishing wave". *Rubric:* 3 = tactical, with audience; 2 = tactical; 1 = strategic; 0 = none.
- **EX014 — Missing stage.** Which life-cycle stage is most often missing, and what fixes it? *Rubric:* 3 = direction; priority intelligence requirements; 2 = direction only; 1 = collection; 0 = none.
- **EX015 — Exec omission.** Why leave indicators out of the chief executive's brief? *Rubric:* 3 = wrong level/audience; executives need strategic context and decisions; 2 = partial; 1 = secrecy; 0 = none.

### Synthesis

Use core terms precisely, start the cycle with direction, match the level to the audience and turn information into intelligence.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) use sets and relations to model indicators and actors; (2) represent intelligence as graphs; (3) reason about paths and connected components; (4) recognise the limits of link analysis.

### 6.1 Sets and relations

Each feed is a set of indicators. Union combines feeds; intersection shows agreement; difference shows what only one source holds. A relation pairs elements: (domain, resolves-to, address). STIX 2.1 relationship objects express exactly this — a source object, a relationship type and a target object.

Amara uses set operations to compare two HSSC feeds and finds that they overlap in only a third of their indicators. Agreement between independent sources raises confidence; indicators found in only one feed are not wrong, but they need more checking before a block.

### 6.2 Graphs

Treat indicators, malware families and campaigns as nodes and relationships as edges. Graphs make pivots visible: two phishing domains that resolved to the same address become linked through that address node. The Diamond Model's four vertices — adversary, capability, infrastructure, victim — are themselves a small graph for each event.

Amara builds a small graph from one HSSC report and checks each edge against its source before drawing conclusions. Each edge carries the source that reported it and the date, so a link that rests on an old or weak report can be identified and, if needed, removed without rebuilding the whole graph.

### 6.3 Paths and components

A path connects two nodes through edges. A connected component is a group where every node reaches every other. Analysts sometimes treat a component as "one campaign". That is a hypothesis, not a fact.

Amara writes "these indicators form one connected group, which may be one campaign" rather than "this is one campaign". She then looks for evidence that would separate them, such as different delivery techniques or timing. A component built through a shared hosting address, for example, may join unrelated actors, so the hypothesis needs testing before anyone acts on it.

### 6.4 Shared infrastructure trap

Shared hosting, content delivery networks and cloud addresses connect unrelated customers. One address serving thousands of domains links them all in a naive graph. Before trusting a link, ask how many other things share that node; high-degree nodes are often noise.

Amara checks the number of domains on each address with the hosting provider's public information or a passive DNS record, and drops edges through nodes that serve many unrelated sites. She records each removed edge and the reason, so a reviewer can see the choice.

### 6.5 Directed versus undirected

"Domain resolves to address" has a direction; "appeared in the same report" does not. Keep direction where it carries meaning, or you will reason backwards.

Amara stores each relationship with its type and direction, following the STIX relationship objects. Reversing an edge, for example reading "address resolves to domain", could lead to the false conclusion that every domain on a shared address belongs to the same actor. Undirected links like co-occurrence in a report are kept separate and treated as weaker evidence, since they show only that two things were mentioned together.

### 6.6 Degree as a warning sign

The degree of a node is the number of its edges. A sudden hub in a small intelligence graph is worth inspecting: it might be a genuine command server, or a public resolver, a webmail provider or a mistaken parsing artefact.

Amara adds a degree check to her graph script that lists any node above a chosen threshold for manual review. The threshold is set from the graph's normal shape, and each flagged node is checked against public information before it is kept. A public resolver or a webmail provider is removed with a note; a genuine server is kept and highlighted.

### Worked example

Amara links six HSSC phishing domains. Five join into one component through a single address. She checks the address: it belongs to a large hosting provider and serves many unrelated sites. She removes it as a pivot; the six domains split into three small groups, two linked by a shared registration email pattern. Her note says "two domains may be related; evidence weak".

> **Synthetic case.** The domains and hosting details are invented.

### Errors and limits

Graphs show co-occurrence, not intent. A drawing with many lines looks convincing; test each edge.

### Exercises

- **EX016 — Set operation.** Which set operation lists indicators only HSSC holds, not HCHT's own blocklist? *Rubric:* 3 = difference (HSSC − HCHT); 2 = named but direction wrong; 1 = intersection; 0 = none.
- **EX017 — High degree.** Why did Amara drop the hosting address as a pivot? *Rubric:* 3 = shared/high-degree node links unrelated sites; false linkage; 2 = partial; 1 = it was malicious; 0 = none.
- **EX018 — Diamond vertices.** Name the four vertices of the Diamond Model. *Rubric:* 3 = adversary, capability, infrastructure, victim; 2 = three; 1 = one or two; 0 = none.

### Synthesis

Sets and graphs organise intelligence; check high-degree nodes, keep direction and treat components as hypotheses.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain DNS, HTTP(S) and SMTP at the level CTI needs; (2) read email headers for sender clues; (3) understand why encrypted traffic limits visibility; (4) relate protocols to ATT&CK techniques.

### 7.1 DNS

The Domain Name System maps names to addresses. Resolver logs record which device asked for which name and when. Because almost every connection starts with a lookup, DNS is the most widely useful source for checking domain indicators.

Amara checks how long HCHT keeps resolver logs and whether they record the internal address of the device or only the address of a forwarding server, which would hide which workstation asked. Both facts decide whether a retrospective search for an HSSC domain can find the device that contacted it, and both are written into her notes on each source.

### 7.2 HTTP and HTTPS

Web traffic carries most user activity and much malicious command traffic. ATT&CK's Application Layer Protocol technique (T1071) describes adversaries blending into normal web, mail or DNS traffic. With HTTPS, a proxy may see only the server name, not the full path, unless traffic is inspected — a decision that has privacy and legal implications in a hospital.

HCHT's legal and privacy staff decided which categories of traffic may be inspected, and health-related sites used by staff for personal care are excluded. Amara works with what the proxy records under that decision, usually the server name and the time, and notes when an indicator cannot be checked because only the full path would reveal it.

### 7.3 SMTP and headers

Email headers record the path a message took: Received lines, the envelope sender and authentication results (SPF, DKIM, DMARC). A display name saying "HCHT Payroll" means nothing if authentication fails and the sending domain is a lookalike.

Amara learns to read the authentication results first, then the sending domain, and only then the display name, which is the easiest part for an attacker to fake. She compares lookalike domains in HSSC reports with HCHT's own domains to see which tricks are aimed at the trust.

### 7.4 Ports and services

Unusual ports or protocols can hint at tunnelling, but many legitimate medical systems use unusual ports too. Context from asset owners beats rules of thumb.

Amara asks the clinical engineering team which ports their devices use before treating any unusual port as suspicious. A list of known clinical ports, kept with the asset inventory, stops alerts from firing on normal imaging traffic and lets real anomalies stand out. Each entry records the device model and the owner who confirmed it.

### 7.5 Time and addresses

Network logs record times in different zones and addresses that may be translated by firewalls. Normalise times to UTC and note address translation before correlating with shared indicators.

Amara found that HCHT's proxy recorded local time while HSSC reports use UTC, which made a contact appear an hour before the domain was first seen. After normalising, the order made sense. She now records the time zone and any address translation for every log source in a short table, so other analysts can correlate events without rediscovering the same problems.

### 7.6 Authentication results in practice

SPF checks whether the sending server may send for the envelope domain; DKIM checks a signature over the message; DMARC ties them to the visible From domain and states the owner's policy. A message can pass SPF for a lookalike domain the attacker controls, so passing checks alone proves only who sent it, not that the sender is benign.

Amara adds this to her checklist for phishing reports. For every reported phishing message she records the three results and whether the visible domain is HCHT's own, a known partner's or a lookalike. That makes the pattern of spoofing visible over time.

### Worked example

A ward manager forwards a suspicious "salary update" email. Amara reads the headers: the From domain is hcht-payrolI.example (capital I for l), SPF passes for that lookalike domain, and DMARC alignment fails against the real domain. She records the lookalike as a phishing indicator (T1566) and shares it with HSSC at TLP:GREEN after removing the staff recipient's address.

> **Synthetic case.** The email and domains are invented.

### Errors and limits

Headers before your own gateway can be forged. Inspection of encrypted traffic requires policy approval and staff notice.

### Exercises

- **EX019 — Header verdict.** SPF passes but DMARC alignment fails against the real domain. What does that tell Amara? *Rubric:* 3 = sender is authorised for the lookalike, not the real domain; spoof/lookalike; 2 = partial; 1 = email is safe; 0 = none.
- **EX020 — Best domain source.** Why is DNS the most useful source for domain indicators? *Rubric:* 3 = nearly all connections begin with lookups; broad coverage; 2 = partial; 1 = encryption; 0 = none.
- **EX021 — HTTPS limit.** What can a proxy usually see in HTTPS traffic without inspection? *Rubric:* 3 = server name (SNI)/destination, not path or content; 2 = destination only; 1 = everything; 0 = none.

### Synthesis

DNS, web and mail logs are the CTI analyst's main checkpoints; read headers critically and respect the limits of encrypted visibility.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) parse a CSV indicator feed with the standard library; (2) validate each row and record reasons for rejection; (3) report counts honestly; (4) design scripts that can be audited.

### 8.1 Feeds as files

HSSC distributes a daily CSV with columns for type, value, first-seen date and TLP. Spreadsheets mangle such files — turning long numbers into scientific notation or stripping leading zeros — so Amara processes them with Python's `csv` module instead.

She keeps the original file unchanged and writes processed output to a new file, so any question about the feed can be checked against what HSSC actually sent. Opening the original in a spreadsheet is avoided even for a quick look, because saving it by accident could change values without anyone noticing.

### Lab — validating a feed

```python
"""Lab 2 (ch 08): parse a synthetic CSV feed with the csv module and count accepted/rejected rows."""
import csv, io
data = """type,value,first_seen,tlp
domain,portal-login.example,2026-09-01,TLP:GREEN
ipv4,203.0.113.50,2026-09-02,TLP:AMBER
domain,,2026-09-02,TLP:GREEN
sha256,abc123,2026-09-03,TLP:GREEN
url,http://files.example/x,2026-09-04,TLP:CLEAR
"""
ok, bad = [], []
for row in csv.DictReader(io.StringIO(data)):
    if not row["value"]:
        bad.append(("empty value", row)); continue
    if row["type"] == "sha256" and len(row["value"]) != 64:
        bad.append(("sha256 length", row)); continue
    ok.append(row)
print("accepted", len(ok), "rejected", len(bad))
for reason, row in bad:
    print(" reject:", reason, row["type"], row["first_seen"])
```

Run with `python3 lab_csvfeed.py`. Verified output:

```text
accepted 3 rejected 2
 reject: empty value domain 2026-09-02
 reject: sha256 length sha256 2026-09-03
```

### 8.2 Reading the result

Three rows pass; two fail. One has an empty domain value; another claims to be a SHA-256 hash but has the wrong length. Each rejection is printed with its date and reason, so Amara can send precise feedback to HSSC rather than "your feed is broken".

The feedback goes to HSSC's contact with the row numbers, so the mistakes can be fixed at the source for every member. She also checks whether the same faults appeared in earlier files. None had.

### 8.3 Validation rules

Rules check presence (no empty value), shape (hash length, valid address), allowed vocabulary (TLP labels from FIRST TLP 2.0: CLEAR, GREEN, AMBER, AMBER+STRICT, RED) and date format. Rules should be few, explicit and tested.

Amara writes one test for each rule using a small file of good and bad rows, so changing a rule shows immediately which cases it affects. She keeps the list of rules in the script's documentation and shares it with HSSC, so the community knows what HCHT checks and can catch problems before the feed is sent. New rules are added only after a real problem shows they are needed.

### 8.4 Never silently drop

A script that skips bad rows without saying so makes counts untrustworthy. Always report accepted and rejected totals.

Amara's import prints both totals and writes rejected rows to a file with the reason for each. If the totals do not add up to the number of rows in the feed, the script stops with an error. A silent drop once hid a column change in a feed for a week, until a missing domain was noticed by chance, which is why the rule is now strict.

### 8.5 Idempotence

Running the import twice should not create duplicates. Use the value plus type as a key and update metadata rather than adding new rows.

Amara tests this by importing the same feed twice and checking that the row count does not change, while the last-seen date updates. Idempotence matters because imports are rerun after failures, and duplicates would inflate counts in reports and make one indicator appear to come from two sources, raising confidence that the evidence does not support.

### 8.6 Encoding and delimiters

Feeds arrive with different encodings and separators. Open files with an explicit encoding, sniff or declare the delimiter, and strip invisible characters such as byte-order marks from the first header. Many baffling "missing column" errors are just a hidden character in the first field name.

Amara adds both steps to her import function. The import prints the detected encoding and delimiter, so a change in how HSSC produces the file is noticed at once instead of appearing later as a puzzling error. Amara keeps a small set of sample files with different encodings as tests.

### Worked example

The next day the feed contains a row with TLP "AMBER STRICT" (space instead of plus). Amara's script rejects it with reason "unknown TLP label". She asks HSSC to correct it rather than guessing, because treating it as AMBER would loosen a restriction.

> **Synthetic case.** The feed rows are invented.

### Errors and limits

Valid format is not truth. A well-formed indicator can be wrong or stale; validation is only the first gate.

### Exercises

- **EX022 — Lab rejections.** Which two rows failed in the lab, and why? *Rubric:* 3 = empty domain (09-02); bad sha256 length (09-03); 2 = one; 1 = counts only; 0 = none.
- **EX023 — TLP typo.** Why must "AMBER STRICT" not be mapped automatically to AMBER? *Rubric:* 3 = would loosen restriction; ask sender; 2 = partial; 1 = harmless; 0 = none.
- **EX024 — Re-run safety.** How should the importer avoid duplicates when run twice? *Rubric:* 3 = key on type+value; update not insert; 2 = dedupe vaguely; 1 = delete all first; 0 = none.

### Synthesis

Parse with code, validate explicitly, report rejections and keep imports idempotent.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) design a small indicator table; (2) query it with SQL through Python's `sqlite3`; (3) find stale indicators; (4) store handling labels alongside data.

### 9.1 Why a database

A spreadsheet works until two analysts edit it at once. A small SQLite database gives one source of truth, queries instead of manual filtering, and a record of what was known when.

Amara moves her indicator list from a shared spreadsheet into SQLite after two analysts overwrote each other's notes. The database file is backed up with the team's other records, and every change is made through her import script or a reviewed query, so it is clear who changed what and when.

### 9.2 Table design

Columns: value, type, source, TLP label, first_seen, last_seen and status. Storing TLP with each row means queries can filter what may be shared before anything leaves HCHT.

Status records whether an indicator is active, under review or expired. Amara adds a constraint so the TLP column accepts only the five valid labels, which stops a typo from creating a label that queries would miss. First and last seen dates let the team show how long an indicator has been relevant, which matters for ageing decisions.

### Lab — querying the store

```python
"""Lab 3 (ch 09): store synthetic indicators in an in-memory SQLite database and query by TLP and age."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("create table ioc(value text primary key, type text, tlp text, last_seen text)")
db.executemany("insert into ioc values(?,?,?,?)", [
    ("portal-login.example", "domain", "TLP:GREEN", "2026-10-01"),
    ("203.0.113.50", "ipv4", "TLP:AMBER", "2026-07-15"),
    ("files.example", "domain", "TLP:CLEAR", "2026-10-08"),
    ("198.51.100.7", "ipv4", "TLP:GREEN", "2026-05-02"),
])
q = "select value, tlp from ioc where tlp in ('TLP:CLEAR','TLP:GREEN') and last_seen >= ? order by value"
for row in db.execute(q, ("2026-09-01",)):
    print(row)
print("stale:", db.execute("select count(*) from ioc where last_seen < '2026-09-01'").fetchone()[0])
```

Run with `python3 lab_sql.py`. Verified output:

```text
('files.example', 'TLP:CLEAR')
('portal-login.example', 'TLP:GREEN')
stale: 2
```

### 9.3 Reading the result

The query returns two domains with their TLP labels: files.example at TLP:CLEAR and portal-login.example at TLP:GREEN. A second query counts two indicators whose last_seen date is older than the review threshold — candidates for expiry.

The query filters by TLP before returning rows, so a list prepared for sharing cannot include restricted entries by mistake. Amara reviews the two expiry candidates with the supervisor before changing their status, since one may still be active according to a recent HSSC update.

### 9.4 Indicator ageing

Addresses change hands; domains are re-registered. An indicator from last year may now belong to an innocent party. Ageing rules — review after 90 days for addresses, longer for hashes — keep blocklists accurate. Bianco's Pyramid of Pain explains why: low-level indicators are cheap for adversaries to change.

Amara applies the rules through a scheduled query that lists indicators due for review. Each review asks whether the indicator still appears in recent reports or logs. If not, it is moved to monitoring or expired, and the reason is recorded. Hashes age more slowly because a file's hash never changes, although the file may stop being used.

### 9.5 Parameterised queries

Always pass values as parameters, never by string concatenation. This prevents malformed values from corrupting queries.

Amara's scripts use parameters for every query that includes a value from a feed, even when the value has already been validated. Feeds sometimes contain quotes or semicolons inside domain names that were defanged by hand, and a concatenated query could fail or change in unexpected ways. Parameters remove the risk entirely and make the code easier to read and review. It is a simple, permanent habit.

### 9.6 Keeping history

When an indicator is retired, set its status to "expired" rather than deleting the row. A later investigation may ask whether HCHT was blocking that address on a particular day, and only a history of status changes with dates can answer the question honestly.

Amara adds a small history table that records each status change with the date and the analyst. That makes it possible to answer such questions with dates rather than memory, and it lets the team measure how long indicators usually stay active before they are retired.

### Worked example

Before sending a weekly summary to HSSC members, Amara filters for rows labelled TLP:CLEAR or TLP:GREEN only. A TLP:AMBER row from a partner is automatically excluded. She also exports the stale list to the network team for review rather than deleting rows herself.

> **Synthetic case.** All rows are invented.

### Errors and limits

A database inherits the quality of its inputs. Labels must be entered correctly at import.

### Exercises

- **EX025 — Lab output.** What did the domain query return? *Rubric:* 3 = files.example CLEAR and portal-login.example GREEN; 2 = one; 1 = count only; 0 = none.
- **EX026 — Why store TLP.** Why keep the TLP label in each row? *Rubric:* 3 = filter shareable data by query before release; 2 = partial; 1 = decoration; 0 = none.
- **EX027 — Stale handling.** What should happen to the two stale indicators? *Rubric:* 3 = review with owners; expire not delete silently; 2 = delete; 1 = keep forever; 0 = none.

### Synthesis

Model indicators with labels and dates, query safely, age indicators and keep history.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) state the legal and ethical limits of OSINT collection; (2) respect platform terms of service; (3) apply data-protection principles; (4) recognise when to stop and ask.

### 10.1 Public is not unlimited

Information visible online is not automatically free to collect, combine and keep. Data-protection law such as the EU GDPR applies to personal data however it was obtained: collection needs a lawful basis, a specific purpose and minimisation. Combining scattered public facts about a person can create a profile that harms them.

Amara's tasks concern infrastructure, such as domains and hosting, not people. When a source includes personal details, such as a registrant's name in a domain record, she records only what the requirement needs and notes why it was kept. HCHT's data protection officer reviews the team's retention of any personal data each year.

### 10.2 Terms of service

Platforms set rules about automated access, account use and data reuse. Fake personas, scraping against terms and logging in to closed groups expose the analyst and employer to legal and reputational risk. HCHT's policy forbids them without legal sign-off.

Amara checks the terms of each public source before using it, and keeps a short note of what is allowed. When a source forbids automated access, she uses it manually or not at all. Sign-off from legal staff is recorded with the source, so later analysts know the decision and its limits.

### 10.3 Authorisation

Analysts act within a written mandate: which questions, which sources, which methods. Interacting with adversary infrastructure — visiting live phishing pages from a work laptop, registering for criminal forums — is outside an intern's authority and can alert adversaries or break the law.

Amara's mandate lists the HSSC feeds, HCHT's own logs and a short list of approved public sources, with the methods allowed for each. When a task seems to need something outside the list, such as checking a live phishing page, she asks her supervisor, who may arrange it in an isolated environment or decide it is not needed.

### 10.4 Proportionality

Ask whether the intelligence need justifies the intrusion. Identifying a phishing domain's hosting provider for a takedown is proportionate; researching the private life of a suspected individual is not CTI's job and belongs, if anywhere, with law enforcement.

Amara writes the purpose of each collection step in her notes and checks it against this test before starting. If the purpose cannot be stated in terms of protecting HCHT's systems or patients, the step is dropped. Her supervisor reviews a sample of her notes each month to confirm the practice is followed.

### 10.5 Stop and ask

When a task feels uncomfortable, pause and ask the supervisor. Record the question and answer.

Amara's notebook has a page for such questions, with the date, the answer and who gave it. Early in her internship she asked whether she could search a social media site for a phishing sender's profile; the answer was no, since the requirement was about the domain, not the person. Recording the answer means the same question does not need to be asked again, and it shows reviewers how decisions were made.

### 10.6 Ethics codes and peers

Professional codes — for example those of security certification bodies — ask members to act honourably and protect society. Peers help too: describing a planned collection to a colleague often exposes problems the analyst had not noticed. HCHT runs a short weekly "method check" where interns present any new source before use.

Amara presents her first new source in week three. The check takes ten minutes. Interns describe the source, what it would answer, its terms and any personal data involved, and a colleague asks questions. Several sources have been dropped or limited after a check, and the notes are kept with the team's source list.

### Worked example

A colleague suggests creating a fake profile to join a closed forum where hospital data might be sold. Amara declines and escalates. The supervisor explains that HCHT will instead ask HSSC and its commercial intelligence provider, who operate under contracts and legal review, whether HCHT data has appeared.

> **Synthetic case.** The scenario is invented.

### Errors and limits

Law varies by jurisdiction; this chapter is not legal advice. Consult HCHT's data protection officer.

### Exercises

- **EX028 — Public data.** Explain why public visibility does not make personal data free to collect. *Rubric:* 3 = data-protection law applies; purpose, minimisation, profiling harm; 2 = partial; 1 = it is free; 0 = none.
- **EX029 — Forum request.** What should Amara do when asked to create a fake profile? *Rubric:* 3 = decline, escalate; use authorised partners; 2 = decline only; 1 = comply; 0 = none.
- **EX030 — Proportionate or not.** Is researching a suspect's family on social media proportionate CTI? *Rubric:* 3 = no; outside mandate; law enforcement; 2 = no; 1 = yes; 0 = none.

### Synthesis

Collect lawfully, follow terms, stay within mandate, weigh proportionality and ask when unsure.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) relate operating-system concepts to ATT&CK techniques; (2) identify endpoint telemetry useful for checking intelligence; (3) explain privilege and its abuse; (4) read a technique page critically.

### 11.1 Processes and command interpreters

An operating system runs processes, each started by a parent. Attackers often use built-in interpreters — PowerShell, command shells, scripting hosts — which ATT&CK groups under Command and Scripting Interpreter (T1059). Because administrators use the same tools, detection depends on context: which parent, which user, which time.

Amara notes that a hospital's administrators run scripts at night for backups and updates, so a script at night is not suspicious on its own. The useful question is whether the parent process and account match what the administrators normally use.

### 11.2 Privilege

Accounts carry privileges. Attackers prefer valid accounts (T1078) because using real credentials looks like normal work. Least privilege limits what a stolen account can do.

For HCHT, valid accounts include supplier accounts used for remote maintenance of clinical systems. Amara learns that intelligence about stolen supplier credentials is especially urgent, since such accounts often have broad access. She checks that each supplier account in the directory has an owner and an expiry date, and reports those without either to the identity team.

### 11.3 Endpoint telemetry

Process creation events with command lines, logon events and service installations are the endpoint logs most relevant to CTI. If a report says a group ran a specific scheduled task name, Amara can search for that name in HCHT's endpoint data.

Before searching, Amara confirms with the endpoint team which systems send process data, since medical devices and some laboratory systems do not run the agent. Where telemetry is missing, the search result says so, rather than implying that nothing was found.

### 11.4 Reading a technique page

Each ATT&CK technique page has a description, procedure examples drawn from public reporting, mitigations and detection notes. Procedure examples show that someone observed this; they do not show how common it is.

Amara uses technique pages to understand what a report describes, not to estimate how likely HCHT is to see it. When a report maps an incident to a technique, she reads the procedure examples to see whether the mapping fits. Detection notes give ideas for searches, which she checks with the endpoint team before running.

### 11.5 Remote services

Remote Services (T1021) covers attackers moving between systems using legitimate remote access. In a hospital, remote desktop is used by suppliers, so baselines of who connects where are essential.

Amara helps the team build a baseline of supplier connections: which supplier connects to which systems, from which addresses and at what times. A connection outside the baseline is not proof of an attack, but it is worth a quick check with the supplier. The baseline is reviewed each quarter with clinical engineering, since maintenance schedules change and new suppliers are added.

### 11.6 Patching and support status

Unsupported operating systems no longer receive fixes, so intelligence about vulnerabilities affecting them has no patch remedy. The inventory should record support status, and advisories touching unsupported systems trigger compensating controls — segmentation, restricted access, extra monitoring — agreed with the system owner.

Amara adds support status to her advisory notes, so readers see at once whether patching is possible. Compensating controls are reviewed when the owner's replacement plan changes. Amara keeps a short list of unsupported systems with their controls and owners, so an advisory can be checked against it quickly, and she notes when a replacement date has slipped.

### Worked example

HSSC reports that an intruder at another trust used remote desktop from a supplier account at 03:00. Amara asks the HCHT endpoint team for remote logons by supplier accounts outside business hours over 30 days. Two appear; both match scheduled maintenance tickets. She records "checked; no match" with the query and dates.

> **Synthetic case.** The report and logons are invented.

### Errors and limits

Absence in logs may mean missing logging. Record coverage when reporting "no match".

### Exercises

- **EX031 — Technique choice.** An attacker logs in with a stolen supplier password. Which ATT&CK technique fits? *Rubric:* 3 = Valid Accounts T1078 with reason; 2 = name only; 1 = T1059; 0 = none.
- **EX032 — Procedure caution.** What does a procedure example on an ATT&CK page not tell you? *Rubric:* 3 = frequency/prevalence or whether it targets you; 2 = partial; 1 = it tells everything; 0 = none.
- **EX033 — No-match record.** What should Amara include when recording "no match"? *Rubric:* 3 = query, period, data source and coverage gaps; 2 = two; 1 = verdict only; 0 = none.

### Synthesis

Map OS behaviour to techniques, use endpoint telemetry to check reports, and record coverage with every negative result.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) express analytic confidence with calibrated words; (2) check wording against a probability scale; (3) explain base rates; (4) avoid false precision.

### 12.1 Words of estimative probability

Sherman Kent showed that readers interpret "probable" anywhere from roughly 20% to 90%. ICD 203 requires analytic products to express likelihood consistently. Teams adopt a scale — for example "very likely" for 80–95% — and stick to it.

Amara uses the team's scale in every product and adds it as a footnote, so readers outside the team can interpret the words. Kent's finding shows that the problem is not careless writing but genuinely different readings of the same words. A shared scale gives the words a fixed meaning, and the footnote lets readers at HSSC or HCHT's board apply it the same way.

### Lab — checking estimative words

```python
"""Lab 1 (ch 12): map estimative words to a published probability scale and flag misuse (synthetic)."""
SCALE = {"almost no chance": (0, 5), "very unlikely": (5, 20), "unlikely": (20, 45),
         "roughly even chance": (45, 55), "likely": (55, 80), "very likely": (80, 95),
         "almost certainly": (95, 100)}
claims = [("C1", "likely", 70), ("C2", "very likely", 60), ("C3", "unlikely", 30), ("C4", "probable", 75)]
for cid, word, analyst_pct in claims:
    if word not in SCALE:
        print(cid, f"'{word}' not on team scale -> rewrite")
        continue
    lo, hi = SCALE[word]
    print(cid, word, f"{analyst_pct}%", "consistent" if lo <= analyst_pct <= hi else f"INCONSISTENT (scale {lo}-{hi}%)")
```

Run with `python3 lab_wep.py`. Verified output:

```text
C1 likely 70% consistent
C2 very likely 60% INCONSISTENT (scale 80-95%)
C3 unlikely 30% consistent
C4 'probable' not on team scale -> rewrite
```

### 12.2 Reading the result

Claim C1 says "likely" at 70% — consistent. C2 says "very likely" but assigns 60%, outside the team's 80–95% band, so the wording overstates confidence. C3 "unlikely" at 30% is consistent. C4 uses "probable", which is not on the team scale and must be rewritten.

Amara returns the draft with the two inconsistent claims marked and the scale attached. The author can either change the word or change the number, but must explain which judgment is correct. Consistency is checked before anything leaves the team, because readers outside it will act on the word they see, not on a number they never read.

### 12.3 Base rates

If one email in ten thousand is malicious, a filter flagging 1% of email produces mostly false alarms even if it catches every phish. Always ask about the base rate before judging a detection.

Amara applies this to an alert rule proposed after an HSSC report and finds that most of its expected alerts would be harmless. The team narrows the rule before deploying it. After narrowing, the rule fires a few times a week, and each alert is checked within the day, which the team can sustain.

### 12.4 False precision

"There is a 73.4% chance this group is responsible" implies measurement that does not exist. Use bands.

Amara replaces such figures in drafts with a word from the team's scale and a short reason. A precise number suggests that the probability was calculated from data, when in practice it reflects an analyst's judgment based on incomplete evidence. Bands are honest about that and easier for readers to act on. If a number is needed for a model, it is given as a range and labelled as an estimate.

### 12.5 Likelihood versus confidence

Likelihood describes how probable an event is; confidence describes the quality of the evidence and reasoning behind the judgment. ICD 203 asks analysts to express and explain both.

Amara learns to write both in one sentence, such as "likely, with moderate confidence because only one source reports it". The two can differ: an event can be likely while confidence is low, if the evidence is thin. Readers need both to decide how much weight to give a judgment. Amara checks every judgment in her drafts for both parts.

### 12.6 Small samples

With five reports, one more or one fewer mention swings a percentage by twenty points. When samples are small, report counts, avoid ranking close values and say that the pattern could change with more data. Statistics cannot rescue a sample that simply contains too little information.

Amara applies this to HSSC's quarterly summary. Several quarters contain only a handful of reports per category, so she asks HSSC to show counts beside each percentage and to mark rankings that depend on one or two reports. HSSC adopts the change for the next summary.

### Worked example

Amara drafts: "It is probable the phishing wave will reach HCHT this week." Her script flags "probable" as off-scale. She rewrites: "It is likely (55–80%) HCHT staff will receive emails from this wave this week; moderate confidence, based on HSSC reports from three nearby trusts."

> **Synthetic case.** The draft and reports are invented.

### Errors and limits

Scales reduce ambiguity but do not make judgments correct. Track outcomes to check calibration over time.

### Exercises

- **EX034 — Lab inconsistency.** Which claim was inconsistent in the lab and why? *Rubric:* 3 = C2: "very likely" at 60%, scale 80–95%; 2 = C2 only; 1 = C4; 0 = none.
- **EX035 — Base-rate trap.** Explain why a filter flagging 1% of email might produce mostly false alarms. *Rubric:* 3 = malicious base rate far below 1%; most flags benign; 2 = partial; 1 = filter broken; 0 = none.
- **EX036 — Two dimensions.** Distinguish likelihood from confidence. *Rubric:* 3 = probability of event vs quality of evidence/reasoning; 2 = partial; 1 = same; 0 = none.

### Synthesis

Use a shared scale, check base rates, avoid false precision and state both likelihood and confidence.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) explain why credentials are a prime target; (2) connect identity intelligence to controls; (3) handle credential-exposure reports responsibly; (4) recognise multi-factor fatigue and session theft at a conceptual level.

### 13.1 Identity as the perimeter

Cloud email and remote access mean a valid password can reach clinical systems from anywhere. Valid Accounts (T1078) and Phishing (T1566) often combine: phish the credential, then log in. CTI about credential phishing therefore leads to identity controls, not only email filters.

### 13.2 Multi-factor authentication

MFA blocks most password-only attacks. Adversaries respond by repeatedly prompting users until one approves, or by stealing session tokens after login. Intelligence that such methods are active in the sector justifies number-matching prompts and conditional access.

### 13.3 Credential exposure reports

Sometimes a partner reports HCHT email addresses and passwords found in a public dump. Handle them as personal data: restrict access, never paste passwords into tickets, force resets via the identity team and inform the data protection officer.

### 13.4 Service and supplier accounts

Shared supplier accounts are hard to attribute and often exempt from MFA. Intelligence about supplier compromise in the sector should trigger a review of these accounts first.

### 13.5 Measuring control effect

After acting on intelligence, check whether the risky pattern declined: fewer successful logons from new countries, fewer approved repeated prompts.

### 13.6 Least privilege and reviews

Regular access reviews remove accounts of leavers and rights that are no longer needed. Intelligence that attackers in the sector are reusing dormant accounts turns a routine review into a priority: dormant privileged accounts are disabled first, with owners confirming any that must stay.

### Worked example

HSSC warns of a campaign sending fake MFA prompts to health staff. Amara checks sign-in logs with the identity team: one nurse approved a prompt at 02:14 from an unfamiliar location. The account is reset, sessions revoked, and the nurse is contacted kindly rather than blamed. HCHT enables number matching.

> **Synthetic case.** The campaign and sign-in are invented.

### Errors and limits

Location data is imprecise; travel and VPNs cause false flags. Blame-free handling keeps staff reporting.

### Exercises

- **EX037 — Combined techniques.** Which two ATT&CK techniques combine in credential phishing followed by login? *Rubric:* 3 = T1566 and T1078 with order; 2 = names; 1 = one; 0 = none.
- **EX038 — Dump handling.** List three safe-handling steps for a credential-dump report. *Rubric:* 3 = restrict access, no passwords in tickets, resets via identity team/inform DPO; 2 = two; 1 = one; 0 = none.
- **EX039 — Control check.** How can HCHT tell whether number matching helped? *Rubric:* 3 = measure approved suspicious prompts/successful risky logons before vs after; 2 = vague; 1 = assume; 0 = none.

### Synthesis

Treat identity as the perimeter, turn credential intelligence into identity controls and handle exposed credentials as personal data.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) identify personal data in intelligence products; (2) redact it before sharing; (3) distinguish victim data from adversary infrastructure; (4) apply minimisation and retention.

### 14.1 Personal data in CTI

Phishing samples contain recipients' names and addresses; incident notes mention staff; logs hold device owners. Under data-protection law these are personal data, and in a hospital some may relate to patients, which carries stricter duties.

### 14.2 Redaction before sharing

Before sending a sample to HSSC, remove staff emails, phone numbers and any patient identifiers. Replace them with labels so the analytic meaning survives: "[staff-email] received the message".

### Lab — redacting a sample

```python
"""Lab 4 (ch 14): redact email addresses and phone numbers from a synthetic incident note before sharing."""
import re
note = ("Phish reported by j.okoro@halden-health.example at 09:14; caller back on +44 20 7946 0958. "
        "Sender domain portal-login.example; reply-to billing@portal-login.example.")
internal = re.compile(r"[\w.+-]+@halden-health\.example")
phone = re.compile(r"\+\d[\d ]{8,}\d")
out = internal.sub("[staff-email]", note)
out = phone.sub("[phone]", out)
print(out)
print("adversary address kept:", "billing@portal-login.example" in out)
```

Run with `python3 lab_redact.py`. Verified output:

```text
Phish reported by [staff-email] at 09:14; caller back on [phone]. Sender domain portal-login.example; reply-to billing@portal-login.example.
adversary address kept: True
```

### 14.3 Reading the result

The staff email and phone number are replaced by placeholders. The adversary's sending address is kept, because it is the indicator other members need. The script reports "adversary address kept: True", confirming it did not over-redact.

### 14.4 Minimisation and retention

Collect only what the question needs and keep it only as long as needed. A retention period for raw phishing samples — say 90 days — limits exposure if HCHT's own systems are breached.

### 14.5 Patient data

Never share patient data through intelligence channels. If an incident involves patient records, the data protection officer leads, and notifications follow law, not CTI habits.

### 14.6 Pseudonymisation versus anonymisation

Replacing a name with a stable label is pseudonymisation: the data can still be linked back by whoever holds the key, so it remains personal data under GDPR. True anonymisation removes any reasonable means of re-identification. Most CTI sharing achieves only the former, so access controls still matter.

### Worked example

A phishing email's body includes a fake invoice listing a real HCHT consultant's name. Amara's automated redaction misses it because it only matches emails and phone numbers. Her manual review catches it, and she adds a step: every shared sample gets a human read for names before release.

> **Synthetic case.** The sample is invented.

### Errors and limits

Pattern-based redaction misses names and free text. Automate the easy cases; review the rest by hand.

### Exercises

- **EX040 — Over-redaction.** Why must the adversary's sending address be kept? *Rubric:* 3 = it is the shared indicator others need; not victim data; 2 = partial; 1 = redact all; 0 = none.
- **EX041 — Missed name.** What process change followed the missed consultant name? *Rubric:* 3 = mandatory human review for names before release; 2 = vague; 1 = none needed; 0 = none.
- **EX042 — Pseudonyms.** Is data with stable placeholder labels anonymous under GDPR? *Rubric:* 3 = no, pseudonymised, still personal data if linkable; 2 = no; 1 = yes; 0 = none.

### Synthesis

Find personal data, redact with care, keep the indicators, minimise, retain briefly and never route patient data through CTI.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) distinguish observation, inference and assessment; (2) record provenance for each piece of evidence; (3) measure the usefulness of intelligence; (4) separate activity metrics from outcome metrics.

### 15.1 Three layers

An observation: "the proxy logged a connection to portal-login.example at 09:41". An inference: "the user probably clicked the phishing link". An assessment: "HCHT was likely targeted by the sector campaign". Each layer needs its own support, and reports should label which is which.

### 15.2 Provenance

For every item record who reported it, when, through which channel, under which TLP, and what it is based on. Without provenance, an indicator copied between feeds appears to have many sources when it has one — circular reporting.

### 15.3 Measuring intelligence

Counting indicators ingested measures activity. Outcome measures ask: did intelligence lead to a block that stopped something, a hunt that found something, or a decision that changed? Fewer, better indicators can produce more value.

### 15.4 Feedback

Consumers should tell producers what helped. HSSC's monthly feedback form asks members which items led to action. Amara fills it in honestly, including "no action needed".

### 15.5 Timeliness

An indicator delivered after the campaign ended has little value. Record the time between first sighting and HCHT action.

### 15.6 Precision and recall for blocks

Precision asks what share of blocked items were truly malicious; recall asks what share of malicious items were blocked. A feed with high recall but poor precision floods the service desk with complaints; one with high precision but low recall misses campaigns. Track both rather than a single "hits" count.

### Worked example

Three feeds report the same domain. Amara checks provenance: two cite the third. She records one independent source, not three, and her confidence stays moderate. Later she logs that blocking the domain stopped two clicks — an outcome metric for the quarterly review.

> **Synthetic case.** The feeds and clicks are invented.

### Errors and limits

Outcomes are hard to attribute to intelligence alone. Report contribution, not proof.

### Exercises

- **EX043 — Layer label.** Label "the user probably clicked the link" as observation, inference or assessment. *Rubric:* 3 = inference, with reason; 2 = inference; 1 = observation; 0 = none.
- **EX044 — Circular reporting.** How did provenance change Amara's count of sources? *Rubric:* 3 = three reports, one independent source; 2 = partial; 1 = three sources; 0 = none.
- **EX045 — Metric type.** Is "50,000 indicators ingested this month" an activity or outcome metric? Suggest an outcome alternative. *Rubric:* 3 = activity; e.g. blocks that stopped clicks/hunt findings; 2 = activity only; 1 = outcome; 0 = none.

### Synthesis

Separate evidence layers, keep provenance, measure outcomes and feed back to producers.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) describe defence in depth in a hospital network; (2) place CTI inputs at each layer; (3) explain segmentation for clinical systems; (4) choose where an indicator should be enforced.

### 16.1 Layers

Email filtering, web proxy, DNS filtering, endpoint protection, identity controls, segmentation and backups form layers. No single layer stops every attack; intelligence helps tune each.

### 16.2 CTI at each layer

Sender domains feed email filters; malicious domains feed DNS and proxy; hashes feed endpoint tools; technique intelligence informs detection rules and hardening; ransomware intelligence (Data Encrypted for Impact, T1486) informs backup isolation.

### 16.3 Segmentation

Clinical devices sit in separate network zones with tightly limited paths. Intelligence about lateral movement through remote services strengthens the case for blocking unnecessary paths between office and clinical zones.

### 16.4 Choosing enforcement

Block where the indicator is reliable and the blast radius is acceptable. A hash of a known malicious file is safe to block on endpoints. A shared cloud address is not safe to block at the firewall.

### 16.5 Architecture reviews

When HCHT designs a new system, the CTI team summarises relevant techniques seen in the sector so architects can design against them from the start.

### 16.6 Backups as a CTI consumer

Sector intelligence that ransomware groups seek and delete backups before encrypting (T1490 Inhibit System Recovery is a related ATT&CK technique) tells the infrastructure team what to protect: offline or immutable copies, separate credentials for backup administration and regular restore tests that prove recovery works.

### Worked example

A sector report describes attackers encrypting file servers after deleting backups. Amara maps it to T1486 and passes it to the infrastructure lead with a question: are HCHT backups offline or immutable? They are not for one site. The lead adds an immutable copy, citing the report in the change request.

> **Synthetic case.** The report and backup gap are invented.

### Errors and limits

Architecture changes take time; intelligence should inform priorities, not demand instant redesign.

### Exercises

- **EX046 — Layer match.** Which layer should receive a SHA-256 hash of a malicious attachment? *Rubric:* 3 = endpoint (and mail attachment scanning), with reason; 2 = endpoint; 1 = firewall; 0 = none.
- **EX047 — Cloud address.** Why not block a shared cloud address at the firewall? *Rubric:* 3 = many legitimate services share it; collateral; 2 = partial; 1 = always block; 0 = none.
- **EX048 — Backup question.** What question did ransomware intelligence prompt, and what changed? *Rubric:* 3 = offline/immutable backups? immutable copy added at one site; 2 = one; 1 = vague; 0 = none.

### Synthesis

Feed each layer the intelligence it can use, enforce where reliable and harmless, and use technique intelligence to shape architecture.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain hashing, encryption and signatures at concept level; (2) understand what a file hash proves; (3) relate certificates to phishing infrastructure; (4) handle encrypted intelligence channels.

### 17.1 Hashes

A cryptographic hash such as SHA-256 maps a file to a fixed-length fingerprint. Identical files give identical hashes; changing one byte changes the hash completely. That makes hashes precise indicators — and fragile ones, because adversaries can alter files trivially. Bianco's Pyramid of Pain places hashes at the bottom: easy for defenders, trivial for attackers to change.

### 17.2 Encryption

Encryption protects confidentiality. Ransomware abuses it (T1486). TLS protects web traffic, including adversaries' command traffic. Encryption therefore shapes what defenders can see.

### 17.3 Signatures and certificates

Digital signatures show who signed data and that it was not altered. Certificates bind a domain name to a key. Free, automated certificates mean phishing sites routinely show a padlock; the padlock proves encryption, not legitimacy.

### 17.4 Certificate transparency

Publicly trusted certificates are recorded in public logs. Searching them for names resembling HCHT's domains can reveal lookalike sites early — an ethical, passive OSINT method.

### 17.5 Protecting intelligence

HSSC distributes TLP:AMBER material through an encrypted portal. Downloading it to personal devices or forwarding by ordinary email breaks the sharing agreement.

### 17.6 Fuzzy and partial matching

Because one changed byte defeats an exact hash, some tools compute similarity hashes that score how alike two files are. They help group variants but produce scores, not proof; a high similarity between two benign installers is common. Treat them as leads for human review.

### Worked example

A staff member asks whether a site is safe "because it has a padlock". Amara explains the padlock means the connection is encrypted, not that the site is genuine. She then checks certificate-transparency records and finds the lookalike domain got its certificate two days ago — consistent with new phishing infrastructure.

> **Synthetic case.** The site is invented.

### Errors and limits

Hash matches identify exact files only. New certificates are common for legitimate sites too.

### Exercises

- **EX049 — Hash fragility.** Why are hashes low on the Pyramid of Pain? *Rubric:* 3 = trivially changed by adversary; precise but brittle; 2 = partial; 1 = hard to change; 0 = none.
- **EX050 — Padlock myth.** What does a browser padlock prove? *Rubric:* 3 = encrypted connection to holder of certificate for that name; not legitimacy; 2 = encryption; 1 = safe site; 0 = none.
- **EX051 — Passive check.** Name a passive OSINT source for spotting lookalike domains early. *Rubric:* 3 = certificate-transparency logs, with reason; 2 = name; 1 = visiting sites; 0 = none.

### Synthesis

Understand what cryptographic artefacts prove, use certificate transparency passively and protect restricted intelligence in transit.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) frame a researchable question; (2) choose qualitative or quantitative methods; (3) design a small coding scheme for reports; (4) consider ethics approval for research with people.

### 18.1 Research questions

"Is CTI useful?" is too broad. "Which HSSC report types led members to take a defensive action in 2026?" names a population, a period and an outcome. Good questions can be answered with available, lawful data.

### 18.2 Methods

Quantitative methods count — how many reports mention phishing. Qualitative methods interpret — how analysts describe confidence. Many CTI studies combine both: code reports, count codes, then interview analysts.

### 18.3 Coding scheme

Define categories in advance with examples: "entry route: phishing (T1566), exploited public application (T1190), valid account (T1078), unknown". Two coders label the same reports and compare; disagreements refine the definitions.

### 18.4 Sampling

Public reports are a biased sample — vendors publish what is interesting or marketable. State the bias rather than pretending the sample represents all incidents.

### 18.5 Ethics

Interviews with analysts need informed consent and, in a university, ethics review. Do not ask participants to reveal TLP-restricted content.

### 18.6 Literature search

Before collecting data, search for prior work: peer-reviewed papers, standards and reputable practitioner reports. Record search terms and databases so the review can be repeated, and note when a source is a vendor blog rather than reviewed research.

### Reliability between coders

When two coders label twenty reports, count how often they agree and discuss each disagreement. Persistent disagreement on one category usually means its definition is vague — for example, whether a malicious link in a text message counts as phishing. Tighten the definition, add an example, and recode a fresh sample to check that agreement improved before analysing the full set.

### Worked example

Amara's first question, "What do hackers do to hospitals?", is refined with her tutor to "Which initial-access techniques appear in public 2025–2026 incident reports about European health providers?" She drafts a four-category coding scheme and pilots it on five synthetic reports.

> **Synthetic case.** The pilot reports are invented.

### Errors and limits

Small samples cannot support strong claims. Report method limits alongside findings.

### Exercises

- **EX052 — Sharpen a question.** Rewrite "Is CTI useful?" as a researchable question. *Rubric:* 3 = population, period, measurable outcome; 2 = two; 1 = still vague; 0 = none.
- **EX053 — Public bias.** Describe one bias in public incident reports. *Rubric:* 3 = selection—vendors publish notable/marketable cases, so counts skew; 2 = vague; 1 = none; 0 = none.
- **EX054 — Interview rule.** What must Amara obtain before interviewing analysts? *Rubric:* 3 = informed consent and ethics review; avoid restricted content; 2 = consent only; 1 = nothing; 0 = none.

### Synthesis

Ask narrow questions, mix methods sensibly, code consistently, admit sampling bias and respect research ethics.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Threat intelligence and OSINT: scope and theory

### Learning outcomes

You will (1) define CTI and OSINT; (2) explain the role of models such as the kill chain and Diamond Model; (3) describe sharing frameworks — STIX, TAXII, TLP; (4) locate CTI in risk management.

### 19.1 Definitions

Cyber threat intelligence is analysed knowledge about adversaries' intent, capability and activity that supports defensive decisions. OSINT is intelligence derived from publicly available sources, collected lawfully. NIST SP 800-150 frames threat information sharing as a way for organisations to improve defences collectively.

### 19.2 Models

Hutchins, Cloppert and Amin's intrusion kill chain (2011) breaks intrusions into phases from reconnaissance to actions on objectives, showing defenders can act at any phase. The Diamond Model (Caltagirone et al., 2013) describes each event by adversary, capability, infrastructure and victim. MITRE ATT&CK catalogues techniques observed in real intrusions.

### 19.3 Sharing standards

STIX 2.1 defines a JSON vocabulary for indicators, threat actors, attack patterns and relationships. TAXII 2.1 defines how to exchange STIX over HTTPS. FIRST TLP 2.0 labels tell recipients how widely they may share.

### 19.4 CTI and risk

CTI changes the likelihood estimates in risk assessments and informs which controls to prioritise. Without a link to risk decisions, CTI becomes a news service.

### 19.5 Theory and practice

Models are lenses, not laws. Each simplifies; analysts choose the one that answers the question at hand.

### 19.6 Choosing a model

Use the kill chain when asking where to interrupt an intrusion, the Diamond Model when asking how events connect through shared infrastructure or capability, and ATT&CK when asking which behaviours to detect. Mixing them is fine if the report says which lens produced each conclusion.

### Worked example

Amara describes one phishing event with the Diamond Model: adversary unknown; capability a credential-harvesting page; infrastructure portal-login.example; victim an HCHT finance clerk. She then places it on the kill chain at delivery and maps it to T1566. Each lens answers a different question.

> **Synthetic case.** The event is invented.

### Errors and limits

Kill-chain linearity breaks for insider or cloud attacks. ATT&CK reflects reported behaviour, not the full population.

### Exercises

- **EX055 — Model choice.** Which model would you use to ask "where could we have stopped this intrusion"? *Rubric:* 3 = kill chain, with reason; 2 = name; 1 = TLP; 0 = none.
- **EX056 — STIX vs TAXII.** Distinguish STIX 2.1 from TAXII 2.1. *Rubric:* 3 = STIX is data format; TAXII is transport protocol over HTTPS; 2 = partial; 1 = same; 0 = none.
- **EX057 — Without risk.** What happens when CTI is not linked to risk decisions? *Rubric:* 3 = becomes news without action/priority; 2 = vague; 1 = nothing; 0 = none.

### Synthesis

CTI is decision-support built on models and shared through standards; choose the right lens and link it to risk.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Threat intelligence and OSINT: foundational cases

### Learning outcomes

You will (1) analyse published cases that shaped CTI practice; (2) extract lessons without repeating attack details; (3) compare cases using models; (4) relate lessons to HCHT.

### 20.1 The kill chain paper

Hutchins et al. described defenders tracking a persistent adversary across repeated intrusions, using indicators from earlier phases to block later attempts. The lesson: intelligence from one intrusion protects against the next, and defenders gain when they analyse failed attempts too.

### 20.2 Group reporting

Public reporting on long-running groups, catalogued in ATT&CK group entries such as G0016 (APT29), showed that adversaries reuse techniques more stably than infrastructure. The lesson: behavioural detection outlasts indicator lists.

### 20.3 Ransomware against health

Many public advisories describe ransomware disrupting hospitals. Common lessons: phishing or exposed services as entry, valid-account abuse, encryption for impact (T1486), and the decisive role of tested, isolated backups.

### 20.4 Supply chain

Compromises of trusted software updates (Supply Chain Compromise, T1195) showed that trusted channels can deliver malicious code. The lesson for HCHT: supplier intelligence and update monitoring matter.

### 20.5 Reading cases ethically

Case studies teach patterns; reproducing malware or step-by-step procedures is unnecessary and inappropriate in coursework.

### 20.6 Comparing cases

A comparison table helps: for each case list entry technique, persistence approach, impact and the defensive lesson. Patterns across rows — credentials appear again and again — are more useful than any single dramatic story, and the table keeps attention on defence rather than on adversary mystique.

### From case to local question

Each case should end with a question for HCHT: do we monitor supplier updates, are backups isolated, would we notice valid-account abuse at night? Writing that question turns history into a concrete check that an owner can answer within a week.

### Worked example

Amara builds a table of three public health-sector ransomware cases: entry route, time to impact, backup status, recovery time. Two recovered faster because backups were offline. She presents the table, with sources, in a team learning session.

> **Synthetic case.** Amara's table and session are invented; real cases would be cited from public sources.

### Errors and limits

Published cases favour dramatic events. Avoid overgeneralising from them.

### Exercises

- **EX058 — Kill chain lesson.** State the main lesson of the Hutchins et al. paper for defenders. *Rubric:* 3 = intelligence from each intrusion (incl. failed) blocks later phases/attempts; 2 = partial; 1 = vague; 0 = none.
- **EX059 — Behaviour vs infrastructure.** Why does behavioural detection outlast indicator lists? *Rubric:* 3 = techniques change less than domains/addresses; 2 = partial; 1 = opposite; 0 = none.
- **EX060 — Backup pattern.** What pattern did Amara's ransomware table reveal? *Rubric:* 3 = offline backups → faster recovery; 2 = partial; 1 = none; 0 = none.

### Synthesis

Foundational cases teach durable lessons: reuse intelligence across intrusions, detect behaviour, protect backups, watch suppliers.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Threat intelligence and OSINT: system models

### Learning outcomes

You will (1) model the HCHT intelligence system as inputs, processes and outputs; (2) identify feedback loops; (3) find bottlenecks; (4) express the model in STIX object terms.

### 21.1 Intelligence as a system

Inputs: HSSC reports, public advisories, vendor feeds, internal incidents. Processes: triage, validation, enrichment, analysis, storage. Outputs: blocks, hunts, briefings, shared reports. Feedback: consumers report what helped. Drawing this flow shows where work piles up.

### 21.2 Bottlenecks

At HCHT, analysis is done by one supervisor and one intern. If triage passes every item to analysis, the queue grows faster than it shrinks. A triage rule — only items matching HCHT assets or the sector proceed — keeps the system stable.

### 21.3 Feedback loops

Positive loop: useful briefings bring more questions, which sharpen direction. Negative loop: too many false-positive blocks make the network team ignore CTI requests. Healthy systems monitor both.

### 21.4 STIX as a data model

STIX 2.1 represents intelligence as objects: indicator, malware, threat-actor, attack-pattern, campaign, identity, report, and relationship objects linking them. Each object has an identifier, timestamps and optional marking definitions such as TLP. Mapping HCHT's database columns to STIX makes later sharing easier.

### 21.5 Boundaries

The model's boundary excludes clinical decisions; CTI informs them through owners, not directly.

### 21.6 Capacity arithmetic

If forty items arrive per week and each takes thirty minutes to analyse, twenty analyst-hours are needed. Two people with other duties may provide eight. Without triage the backlog grows by about twenty-four items weekly; writing this arithmetic down makes the case for stricter filters or more staff in plain terms.

### Service levels

Agree simple targets with consumers: urgent indicators reviewed within four hours, routine items within three working days. Targets turn the system model into commitments and reveal quickly when capacity no longer matches demand.

### Worked example

Amara maps a week: 140 items arrived; 40 passed triage; 12 were analysed; 3 led to action. The bottleneck is analysis. She proposes tighter triage criteria and a template that halves write-up time. The supervisor agrees to trial both for a month.

> **Synthetic case.** The counts are invented.

### Errors and limits

System diagrams simplify human judgment. Measure before and after changes.

### Exercises

- **EX061 — Find the bottleneck.** In Amara's week, where was the bottleneck and how do you know? *Rubric:* 3 = analysis; 40 in, 12 done; 2 = analysis; 1 = collection; 0 = none.
- **EX062 — Negative loop.** Describe a negative feedback loop in CTI delivery. *Rubric:* 3 = false-positive blocks → network team ignores CTI; 2 = vague; 1 = none; 0 = none.
- **EX063 — STIX mapping.** Which STIX object type links an indicator to a malware object? *Rubric:* 3 = relationship (e.g. "indicates"); 2 = relationship; 1 = report; 0 = none.

### Synthesis

Model CTI as a system, manage bottlenecks, watch feedback loops and map data to STIX.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Threat intelligence and OSINT: data and dependencies

### Learning outcomes

You will (1) catalogue HCHT's intelligence sources and their dependencies; (2) assess single points of failure; (3) evaluate source licences and terms; (4) plan for source loss.

### 22.1 Source catalogue

For each source record: provider, content type, format, delivery method, licence or terms, TLP, cost and owner. HSSC (STIX over TAXII 2.1, membership agreement), a national advisory service (public web pages), a commercial feed (contract), and internal incident records.

### 22.2 Dependencies

The commercial feed depends on a contract renewal; HSSC depends on volunteer staff; the import scripts depend on one analyst's knowledge. Each is a dependency that can fail.

### 22.3 Terms and licences

Commercial feeds often forbid redistribution. Before sharing an indicator learned from a paid feed with HSSC, Amara checks the licence. Public advisories may permit reuse with attribution.

### 22.4 Single points of failure

If the only person who understands the import script leaves, the pipeline stops. Documentation, a second trained person and simple code reduce that risk.

### 22.5 Coverage gaps

Sources cover some threats better than others. National advisories may underweight medical-device threats; vendor feeds may focus on commodity malware. A coverage table shows gaps.

### 22.6 Source evaluation over time

Sources change: a once-excellent feed may degrade after an acquisition, or a volunteer group may stop publishing. A quarterly check — volume, timeliness, proportion of items leading to action — catches decline before analysts notice that a source has quietly become noise.

### Internal sources

HCHT's own incidents are its most relevant intelligence: they show what actually reached the trust. Service-desk tickets about suspicious email, endpoint alerts and lessons-learned notes should flow into the catalogue as sources, with the same care for personal data as external material.

### Worked example

The commercial contract lapses for a week due to a procurement delay. Amara's catalogue shows which detections depend on that feed. The team switches those to HSSC data temporarily and raises the dependency in the risk register.

> **Synthetic case.** The lapse is invented.

### Errors and limits

Catalogues go out of date; review quarterly.

### Exercises

- **EX064 — Licence check.** Why must Amara check before sharing a paid-feed indicator with HSSC? *Rubric:* 3 = licence may forbid redistribution; 2 = partial; 1 = no check needed; 0 = none.
- **EX065 — Human dependency.** Give two ways to reduce the single-analyst dependency. *Rubric:* 3 = documentation; second trained person (or simpler code); 2 = one; 1 = vague; 0 = none.
- **EX066 — Catalogue fields.** List four fields of a source-catalogue entry. *Rubric:* 3 = four of provider/format/delivery/licence/TLP/cost/owner; 2 = three; 1 = one or two; 0 = none.

### Synthesis

Know your sources, their terms and dependencies, and plan for their failure.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Threat intelligence and OSINT: methods I

### Learning outcomes

You will (1) code reports to ATT&CK techniques; (2) compute technique frequency; (3) interpret frequency cautiously; (4) turn frequency into defensive priorities.

### 23.1 Coding reports

Read each report and tag techniques with ATT&CK identifiers, citing the sentence that supports each tag. Avoid tagging from headlines; tag only what the text describes.

### Lab — technique frequency

```python
"""Lab 5 (ch 23): rank ATT&CK techniques by frequency across synthetic sector reports."""
from collections import Counter
reports = {
    "R1": ["T1566", "T1204", "T1059"], "R2": ["T1566", "T1078"], "R3": ["T1190", "T1059", "T1486"],
    "R4": ["T1566", "T1204", "T1486"], "R5": ["T1078", "T1021", "T1486"],
}
c = Counter(t for ts in reports.values() for t in ts)
for tid, n in c.most_common():
    print(f"{tid} in {n}/{len(reports)} reports")
```

Run with `python3 lab_freq.py`. Verified output:

```text
T1566 in 3/5 reports
T1486 in 3/5 reports
T1204 in 2/5 reports
T1059 in 2/5 reports
T1078 in 2/5 reports
T1190 in 1/5 reports
T1021 in 1/5 reports
```

### 23.2 Reading the result

Across five synthetic HSSC reports, Phishing (T1566) and Data Encrypted for Impact (T1486) appear in three each. User Execution (T1204), Command and Scripting Interpreter (T1059) and Valid Accounts (T1078) appear in two. Exploit Public-Facing Application (T1190) and Remote Services (T1021) appear once.

### 23.3 Caution

Five reports is tiny. Frequency reflects what reporters noticed and wrote down, not what happened. A technique appearing once may matter more if HCHT is exposed to it — an unpatched internet-facing system makes T1190 relevant despite its low count.

### 23.4 From frequency to priority

Priority combines frequency, HCHT exposure and control gaps. Phishing is frequent, and HCHT already has training and filtering; remote services appear once, but supplier remote access is poorly monitored. The final priority list might rank remote-service monitoring above more phishing training.

### 23.5 Recording

Keep the coding sheet with report identifiers and supporting sentences so others can verify.

### 23.6 Coding granularity

ATT&CK has techniques and sub-techniques. Coding at sub-technique level gives detail but splits small samples into tiny counts; coding at technique level is coarser but more stable. Choose one level for a given study and state it, or counts become incomparable.

### Comparing with internal incidents

Set the sector counts beside HCHT's own incident tags. If internal incidents show valid-account abuse far more often than sector reports, local conditions matter more than the sector average.

### Worked example

Amara's first coding tags T1059 in a report that only says "the attacker ran commands". Her supervisor asks for the supporting sentence; it does not specify an interpreter. They keep the tag but note "low specificity" in the sheet.

> **Synthetic case.** The reports are invented.

### Errors and limits

Coding is subjective; double-code a sample to check agreement.

### Exercises

- **EX067 — Lab leaders.** Which techniques appeared most often in the lab? *Rubric:* 3 = T1566 and T1486, 3/5 each; 2 = one; 1 = wrong; 0 = none.
- **EX068 — Low count, high priority.** Why might T1190 deserve priority despite appearing once? *Rubric:* 3 = HCHT exposure (unpatched internet-facing system); 2 = partial; 1 = no; 0 = none.
- **EX069 — Supporting sentence.** Why record the supporting sentence for each tag? *Rubric:* 3 = verifiability and review of coding; 2 = partial; 1 = formatting; 0 = none.

### Synthesis

Code carefully, count honestly, read counts in context and combine them with exposure to set priorities.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Threat intelligence and OSINT: controls

### Learning outcomes

You will (1) map techniques to mitigations using ATT&CK; (2) write an intelligence-driven control request; (3) estimate the cost and side effects of a control; (4) verify that a control works.

### 24.1 From technique to mitigation

Each ATT&CK technique page lists mitigations — for phishing, user training, filtering and restricting web content; for valid accounts, multi-factor authentication and privileged account management. These are starting points, not prescriptions.

### 24.2 The control request

A good request states: the intelligence (with source and TLP), the technique, the proposed control, the expected benefit, side effects, owner and a deadline. It does not demand; it informs the owner's decision.

### 24.3 Side effects

Blocking macros in documents stops one delivery route but may break a laboratory spreadsheet used daily. Ask owners about impact before proposing.

### 24.4 Verification

After a control is applied, test it safely: send a harmless test document through the filter, or confirm a blocked domain fails to resolve. Record the test.

### 24.5 Decay

Controls decay: exceptions are added, rules disabled during outages and never re-enabled. Recheck quarterly.

### 24.6 Detection as a control

Not every risk can be prevented. Where prevention would break clinical work, a detection rule plus a rehearsed response may be the right control. The request then names who receives alerts, how fast they must act and what they will do, so the detection does not become an unread dashboard.

### Prioritising requests

Owners receive many requests. Rank yours by technique frequency, HCHT exposure and the cost of the control, and send few strong requests rather than many weak ones. A short cover note explaining the ranking helps owners plan their own work around it.

### Worked example

Intelligence shows a sector wave using malicious document attachments (User Execution, T1204). Amara drafts a request to the email team: quarantine macro-enabled attachments from external senders, with an exception process for two known suppliers. The team accepts; Amara verifies with a harmless test file and logs the result.

> **Synthetic case.** The wave and suppliers are invented.

### Errors and limits

Mitigations listed on ATT&CK vary in strength. Prefer controls you can test.

### Exercises

- **EX070 — Request contents.** List five elements of an intelligence-driven control request. *Rubric:* 3 = five of intelligence/source/TLP, technique, control, benefit, side effects, owner, deadline; 2 = three; 1 = one; 0 = none.
- **EX071 — Laboratory spreadsheet.** Why ask owners before proposing a macro block? *Rubric:* 3 = may break critical workflow; exceptions needed; 2 = partial; 1 = no need; 0 = none.
- **EX072 — Verify a block.** How can Amara safely verify a domain block? *Rubric:* 3 = test resolution/connection from a test device fails; record; 2 = partial; 1 = assume; 0 = none.

### Synthesis

Map techniques to mitigations, ask with evidence, weigh side effects, verify and recheck.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Threat intelligence and OSINT: Laboratory I

### Learning outcomes

You will (1) run an end-to-end mini pipeline on synthetic data; (2) combine validation, storage and redaction; (3) write a lab report; (4) reflect on lab safety and data rules.

### 25.1 Lab design

This laboratory combines earlier labs into one exercise. Students receive a synthetic HSSC CSV feed, validate it (chapter 8), load accepted rows into SQLite (chapter 9), redact a synthetic phishing sample (chapter 14) and produce a one-page shareable summary filtered to TLP:CLEAR and TLP:GREEN.

### 25.2 Environment rules

Work only in the course virtual machine with no internet route. Use standard-library Python. Do not paste real HCHT data or real indicators from work into the lab. If a lab file seems to contain real personal data, stop and tell the instructor.

### 25.3 Steps

First, run validation and note rejections with reasons. Second, load accepted rows and query by type and label. Third, redact the sample and confirm the adversary address survives. Fourth, write the summary: what was received, what was rejected, what may be shared and with whom.

### 25.4 The lab report

A lab report has aim, method, results, problems and reflections. Results include exact counts and script outputs; problems include anything that surprised you. Reflection asks what would change with real data.

### 25.5 Assessment

Marks reward correct outputs, clear reasoning, honest problems and correct handling labels. Pretty formatting earns nothing extra.

### 25.6 Reproducibility

A classmate should be able to repeat your work from the report alone. Record script versions, input file names, the order of steps and any manual edits. If you corrected a value by hand, say so; hidden manual fixes make results impossible to reproduce.

### 25.7 Pairing

Students work in pairs: one runs the scripts, the other checks outputs against expectations and records discrepancies. Roles swap halfway. Pairing catches mistakes early and practises the review habit that real teams rely on.

### Worked example

Amara's pair finds that the summary includes a row labelled TLP:AMBER because the filter compared labels case-sensitively and the row said "tlp:amber". They normalise labels to upper case at import, rerun, and note the bug in their report's problems section.

> **Synthetic case.** The feed and bug are invented teaching material.

### Errors and limits

A lab proves the pipeline on clean synthetic data; real feeds are messier.

### Exercises

- **EX073 — Lab order.** Put validation, redaction, storage and summary in a sensible order and justify one step's position. *Rubric:* 3 = validate → store → redact → summarise, with reason; 2 = order only; 1 = muddled; 0 = none.
- **EX074 — Case bug.** What caused the AMBER row to leak into the summary, and what fixed it? *Rubric:* 3 = case-sensitive comparison; normalise at import; 2 = one; 1 = vague; 0 = none.
- **EX075 — Real data.** What should a student do if lab data looks like real personal data? *Rubric:* 3 = stop, do not use, tell instructor; 2 = stop; 1 = carry on; 0 = none.

### Synthesis

Combine the pieces, follow lab rules, report honestly and make your work reproducible.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Threat intelligence and OSINT: methods II

### Learning outcomes

You will (1) grade sources and information with the Admiralty system; (2) decide how graded items may be used; (3) separate source reliability from information credibility; (4) record grading reasons.

### 26.1 Two letters, two questions

The Admiralty (NATO) system grades source reliability from A (completely reliable) to F (cannot be judged) and information credibility from 1 (confirmed) to 6 (cannot be judged). A reliable source can pass on doubtful information; an unknown source can report something confirmed by other evidence.

### Lab — grading and use

```python
"""Lab 6 (ch 26): combine source reliability (A-F) and information credibility (1-6) into a handling rule."""
items = [("I-1", "B", 2), ("I-2", "E", 3), ("I-3", "A", 5), ("I-4", "C", 3), ("I-5", "F", 6)]
for iid, rel, cred in items:
    if rel in "AB" and cred <= 2:
        rule = "use for action"
    elif rel == "F" or cred == 6:
        rule = "cannot judge - seek corroboration"
    elif cred >= 5 or rel == "E":
        rule = "hold - low confidence"
    else:
        rule = "use with caveat"
    print(iid, rel + str(cred), rule)
```

Run with `python3 lab_admiralty.py`. Verified output:

```text
I-1 B2 use for action
I-2 E3 hold - low confidence
I-3 A5 hold - low confidence
I-4 C3 use with caveat
I-5 F6 cannot judge - seek corroboration
```

### 26.2 Reading the result

I-1 is B2 — usually reliable, probably true — use for action. I-2 is E3 — unreliable source, possibly true — hold. I-3 is A5 — completely reliable source but improbable information — hold until checked; even good sources make mistakes. I-4 is C3 — fairly reliable, possibly true — use with a caveat. I-5 is F6 — cannot be judged on either axis.

### 26.3 Decision rules

The lab encodes simple rules: act on combinations of A–B with 1–2; caveat C with 3; hold anything with E or 5; F6 needs more information. Teams agree their rules in advance so grading drives consistent decisions.

### 26.4 Reasons

Write why: "B — HSSC has been accurate in 18 of 20 past items" is reviewable; "B — seems fine" is not.

### 26.5 Re-grading

Grades change as evidence arrives. Keep history so later reviewers know what was believed when.

### 26.6 Grading OSINT

Open sources range from official advisories to anonymous posts. A national agency advisory might rate B; an anonymous social-media claim, E or F until corroborated. Grade the specific author or channel, not "the internet", and remember that a reliable outlet can still repeat someone else's unverified claim.

### Worked example

A post on a public forum claims HCHT data is for sale. Source: unknown poster (F). Information: no sample, unverifiable (6). Amara records F6, does not alarm management, and asks HSSC whether any member has corroborating information. HSSC reports similar unverified claims about several trusts. The item stays F6 with a note.

> **Synthetic case.** The post is invented.

### Errors and limits

Grades are judgments, not measurements. Two analysts may disagree; discuss.

### Exercises

- **EX076 — A5 decision.** Why does the lab hold I-3 even though its source is A? *Rubric:* 3 = information improbable (5); reliable sources can err; verify; 2 = partial; 1 = should act; 0 = none.
- **EX077 — Grade the forum post.** Grade the forum claim and explain each letter/number. *Rubric:* 3 = F6 with reasons for both; 2 = grade only; 1 = wrong; 0 = none.
- **EX078 — Good reason.** Write a reviewable reason for grading a source B. *Rubric:* 3 = evidence-based track record; 2 = vague evidence; 1 = opinion; 0 = none.

### Synthesis

Grade source and information separately, decide by agreed rules, record reasons and re-grade as evidence changes.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Threat intelligence and OSINT: verification

### Learning outcomes

You will (1) verify indicators passively before action; (2) corroborate claims with independent sources; (3) check whether intelligence matches HCHT's environment; (4) record verification steps.

### 27.1 Passive verification

Check indicators without touching adversary systems: public DNS records, certificate-transparency logs, registration data where available, and reputable public reputation services. Visiting a live phishing page from a work device is not passive and is not allowed.

### 27.2 Independence

Two reports are independent only if they rest on different observations. Ask each source what its claim is based on. Citations to the same vendor blog do not corroborate each other.

### 27.3 Environmental match

An advisory about a product HCHT does not run is lower priority, however severe. Check the inventory, versions and exposure.

### 27.4 Internal corroboration

The best verification is often internal: did HCHT's mail gateway receive messages from the reported sender? Did any device contact the domain? Internal sightings both verify and measure relevance.

### 27.5 Recording

A verification record lists each check, its result, the time and the analyst. Others can repeat or challenge it.

### 27.6 Verifying claims, not only indicators

Narrative claims need checking too: "the group always demands payment within 48 hours" may come from one case. Trace the claim to its original source, see what evidence it cited and whether later reporting confirmed it. Unverified claims stay in the report only with a clear caveat.

### Time-boxing verification

Verification can expand forever. Set a time box proportional to urgency: fifteen minutes for a domain already seen in HCHT mail, longer for a strategic claim. When the box expires, report what was verified and what was not, so decision-makers are not kept waiting for certainty that may never come.

### Worked example

HSSC shares a domain tagged as phishing. Amara checks certificate-transparency logs (certificate issued yesterday), public DNS (resolves to a hosting provider), and HCHT mail logs (four messages yesterday to finance staff). Internal sightings confirm relevance; she escalates for blocking and user notification.

> **Synthetic case.** The domain and messages are invented.

### Errors and limits

Passive checks can mislead: new certificates are normal. Weight internal evidence highly.

### Exercises

- **EX079 — Not passive.** Why is visiting a live phishing page from a work laptop not passive verification? *Rubric:* 3 = contacts adversary infrastructure; can alert/expose/infect; policy breach; 2 = partial; 1 = it is fine; 0 = none.
- **EX080 — Independence test.** What question establishes whether two reports are independent? *Rubric:* 3 = what each is based on—different observations?; 2 = partial; 1 = same date?; 0 = none.
- **EX081 — Best evidence.** Which check gave Amara the strongest reason to escalate? *Rubric:* 3 = internal mail logs showing four messages to finance; 2 = mail logs; 1 = certificate; 0 = none.

### Synthesis

Verify passively, demand independence, match to the environment, prize internal sightings and record every check.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Threat intelligence and OSINT: failure analysis

### Learning outcomes

You will (1) analyse intelligence failures without blame; (2) distinguish collection, analysis and dissemination failures; (3) recognise cognitive biases; (4) produce actionable lessons.

### 28.1 Kinds of failure

Collection failure: the signal never arrived. Analysis failure: it arrived but was misjudged. Dissemination failure: the judgment was right but reached the wrong person or too late. Action failure: the right person received it but did not act. Each needs a different fix.

### 28.2 Cognitive biases

Heuer's Psychology of Intelligence Analysis describes how analysts see what they expect, anchor on first impressions and favour evidence that confirms their view. Structured techniques such as analysis of competing hypotheses push analysts to test alternatives.

### 28.3 Blameless review

Reviews ask what happened and why, not who to punish. People who fear blame hide mistakes, and the organisation stops learning.

### 28.4 Timeline first

Build a timeline of when information arrived, who saw it and what they did. Failures often sit in gaps between teams.

### 28.5 Lessons that change things

"Be more careful" is not a lesson. "Add an owner field to every advisory and confirm receipt within one day" is.

### 28.6 Near misses

A near miss — a phishing email noticed by chance before anyone clicked — is free learning. Reviewing near misses with the same structure as incidents reveals weak points before they cause harm, and staff find these reviews less threatening because nothing went wrong.

### Worked example

An HSSC advisory about a vulnerable remote-access appliance reached HCHT on a Friday. The general IT mailbox received it; nobody owned it. On Tuesday, the appliance was probed. The review finds a dissemination failure: no routing rule for appliance advisories. The lesson adds the appliance to the inventory with an owner and routes advisories by product match.

> **Synthetic case.** The advisory and probing are invented.

### Errors and limits

Hindsight makes signals look obvious. Judge decisions by what was known at the time.

### Exercises

- **EX082 — Failure type.** Classify the Friday advisory failure and justify. *Rubric:* 3 = dissemination—right information, no owner/routing; 2 = type only; 1 = collection; 0 = none.
- **EX083 — Bias example.** Give an example of confirmation bias in CTI work. *Rubric:* 3 = specific example favouring confirming evidence about an actor/attribution; 2 = generic definition; 1 = unrelated; 0 = none.
- **EX084 — Actionable lesson.** Rewrite "be more careful with advisories" as an actionable lesson. *Rubric:* 3 = specific owner/process/timeframe; 2 = partial; 1 = still vague; 0 = none.

### Synthesis

Classify failures by stage, guard against bias, review without blame and write lessons that change process.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Threat intelligence and OSINT: operations

### Learning outcomes

You will (1) run a weekly CTI cycle; (2) prioritise with intelligence requirements; (3) apply TLP correctly in daily handling; (4) maintain a work log.

### 29.1 Weekly rhythm

Monday: review requirements and open items. Daily: triage incoming items, verify urgent ones, push indicators. Thursday: draft the weekly brief. Friday: send feedback to HSSC and close items. A rhythm keeps a small team predictable.

### 29.2 Requirements

HCHT's priority intelligence requirements include: campaigns targeting UK and EU health providers; vulnerabilities in products in the inventory; credential exposure of HCHT accounts; threats to medical devices. Items outside them get a light touch.

### 29.3 TLP in practice

TLP:CLEAR may be shared publicly. TLP:GREEN within the community but not publicly. TLP:AMBER within the recipient organisation and its clients on a need-to-know basis; AMBER+STRICT within the organisation only. TLP:RED to named recipients only. When HCHT re-shares, it keeps the original label or stricter.

### 29.4 Work log

Record each item: arrival, source, TLP, grade, decision, actions, closure. The log supports handover, audit and failure review.

### 29.5 Handover

When Amara is away, the log tells her supervisor what is pending.

### 29.6 Urgent path

Some items cannot wait for the weekly rhythm: a campaign actively hitting HCHT mailboxes, or a vulnerability under exploitation in an internet-facing product HCHT runs. The urgent path skips the brief: phone the owner, open a priority ticket, record decisions in the log, and summarise in the next weekly brief.

### Worked example

On Wednesday an HSSC TLP:AMBER+STRICT item reports a supplier compromise affecting a pathology system HCHT uses. Amara logs it, informs the pathology system owner directly (inside HCHT), and does not forward it to the supplier, because AMBER+STRICT forbids sharing outside HCHT. The supervisor asks HSSC whether the supplier may be contacted.

> **Synthetic case.** The item and supplier are invented.

### Errors and limits

Rhythms break during incidents; the log keeps continuity.

### Exercises

- **EX085 — Strict handling.** Why may Amara not forward the AMBER+STRICT item to the supplier? *Rubric:* 3 = AMBER+STRICT limits to recipient organisation only; ask originator; 2 = partial; 1 = may forward; 0 = none.
- **EX086 — Outside requirements.** How should items outside the requirements be handled? *Rubric:* 3 = light touch—log, minimal effort unless relevant; 2 = partial; 1 = full analysis; 0 = none.
- **EX087 — Log fields.** List five fields of the work log. *Rubric:* 3 = five of arrival, source, TLP, grade, decision, actions, closure; 2 = three; 1 = one; 0 = none.

### Synthesis

Run a steady rhythm, steer by requirements, apply TLP exactly and keep a log.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Threat intelligence and OSINT: Laboratory II

### Learning outcomes

You will (1) produce a STIX 2.1-style bundle by hand from a synthetic incident; (2) apply TLP marking; (3) peer-review a classmate's bundle; (4) explain choices in a short memo.

### 30.1 The task

From a synthetic incident description — a phishing email, a credential page, a later suspicious login — students write a JSON bundle containing an indicator, an attack-pattern for T1566, an attack-pattern for T1078, a relationship linking them, and a report object. Each object gets an identifier, created and modified timestamps and a TLP marking reference.

### 30.2 Why by hand

Writing objects by hand teaches what each field means before tools hide it. Students use Python's `json` module only to check that the file parses.

### 30.3 Patterns

STIX indicators carry a pattern in STIX pattern language, for example matching a domain name value. Students copy the form from the specification rather than inventing syntax, and cite the section.

### 30.4 Peer review

Pairs swap bundles and check: does every relationship point to objects that exist? Are timestamps in UTC? Is the TLP marking present on each object? Is any personal data present?

### 30.5 Memo

A half-page memo explains modelling choices: why a relationship type was chosen, what was left out and why.

### 30.6 Identifiers and versions

STIX identifiers combine the object type and a UUID. When an object changes, its identifier stays the same and the modified timestamp moves forward. Students who create a new identifier for every edit break references from other objects, a mistake peer reviewers learn to spot quickly.

### 30.7 Assessment

Marks reward a valid, minimal bundle with correct references and labels, a thoughtful memo and constructive review comments on a peer's work.

### Worked example

Amara's reviewer finds her relationship object points to an attack-pattern identifier with a typo, so the link dangles. She fixes it and adds a small script check: every relationship's source and target identifiers must exist in the bundle.

> **Synthetic case.** The incident is invented teaching material.

### Errors and limits

Hand-written bundles are for learning; production systems generate and validate them with tools.

### Exercises

- **EX088 — Dangling link.** What check catches a relationship pointing to a missing object? *Rubric:* 3 = verify source_ref/target_ref exist among bundle ids; 2 = partial; 1 = JSON parse; 0 = none.
- **EX089 — Edit semantics.** When editing a STIX object, what stays the same and what changes? *Rubric:* 3 = id same; modified timestamp updates; 2 = one; 1 = new id; 0 = none.
- **EX090 — Review list.** Give three peer-review checks for a bundle. *Rubric:* 3 = references exist, UTC timestamps, TLP markings (or no personal data); 2 = two; 1 = one; 0 = none.

### Synthesis

Hand-build a small bundle to learn STIX, review rigorously and explain your modelling choices.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Threat intelligence and OSINT: advanced cases

### Learning outcomes

You will (1) reconstruct an intrusion timeline across kill-chain phases; (2) distinguish preparation from intrusion phases; (3) identify defensive opportunities at each phase; (4) present a timeline clearly.

### 31.1 From events to phases

Hutchins et al. defined phases: reconnaissance, weaponization, delivery, exploitation, installation, command and control, and actions on objectives. Placing timestamped events into phases shows the intrusion's tempo and where defenders could have acted.

### Lab — ordering phases

```python
"""Lab 7 (ch 31): order synthetic incident events by time and label kill-chain phases."""
events = [
    ("2026-09-03 10:02", "beacon to files.example over HTTPS", "command and control"),
    ("2026-09-03 09:41", "user opens invoice attachment", "exploitation"),
    ("2026-09-03 09:30", "phishing email delivered", "delivery"),
    ("2026-09-02 18:00", "lookalike domain registered", "weaponization"),
    ("2026-09-03 09:45", "scheduled task created", "installation"),
]
for t, what, phase in sorted(events):
    print(t, f"{phase:20}", what)
first, last = min(events)[0], max(events)[0]
print("span:", first, "->", last)
```

Run with `python3 lab_phases.py`. Verified output:

```text
2026-09-02 18:00 weaponization        lookalike domain registered
2026-09-03 09:30 delivery             phishing email delivered
2026-09-03 09:41 exploitation         user opens invoice attachment
2026-09-03 09:45 installation         scheduled task created
2026-09-03 10:02 command and control  beacon to files.example over HTTPS
span: 2026-09-02 18:00 -> 2026-09-03 10:02
```

### 31.2 Reading the result

The script orders five synthetic events: weaponization at 2026-09-02 18:00, delivery at 09:30 the next day, exploitation at 09:41, installation at 09:45 and command and control at 10:02. The span is 2026-09-02 18:00 to 2026-09-03 10:02.

### 31.3 A labelling caution

The "weaponization" event is actually the registration of a lookalike domain. ATT&CK classifies that as resource development — Acquire Infrastructure (T1583) — which happens before the intrusion. The kill chain's weaponization phase strictly means pairing an exploit with a deliverable payload. Analysts should say which framework's terms they use; here the event is better called preparation.

### 31.4 Tempo

From delivery to command and control took 32 minutes. That window tells HCHT that alerting on the first phases must reach a human within minutes, not the next day.

### 31.5 Opportunities

Domain monitoring could flag registration; email filtering could block delivery; endpoint controls could stop installation; DNS monitoring could catch command traffic.

### 31.6 Presenting timelines

A good timeline figure uses one time zone, labels each event with its evidence source, and marks gaps where nothing is known. Readers then see not only what happened but where the record is thin, which guides the next questions.

### Worked example

Amara presents the timeline to the incident lead, marking each phase with the control that could have acted. The lead picks two: lookalike-domain monitoring through certificate transparency and faster alert routing for endpoint installation events.

> **Synthetic case.** The intrusion is invented.

### Errors and limits

Real intrusions loop and skip phases; a linear timeline is a simplification.

### Exercises

- **EX091 — Tempo.** How long from delivery to command and control in the lab, and what does it imply? *Rubric:* 3 = 32 minutes; alerts must reach humans within minutes; 2 = number only; 1 = wrong; 0 = none.
- **EX092 — Mislabel.** Why is domain registration better labelled preparation than weaponization? *Rubric:* 3 = it is resource development/T1583; weaponization = pairing exploit and payload; 2 = partial; 1 = no difference; 0 = none.
- **EX093 — Phase control.** Name a control for the delivery phase in this case. *Rubric:* 3 = email filtering of lookalike sender/attachments, with link to phase; 2 = name; 1 = backup; 0 = none.

### Synthesis

Order events into phases, name terms precisely, read the tempo and pick controls per phase.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Threat intelligence and OSINT: interdisciplinary interfaces

### Learning outcomes

You will (1) work with legal, privacy, clinical and communications colleagues; (2) translate CTI for each; (3) recognise their constraints; (4) avoid overstepping roles.

### 32.1 Legal

Lawyers advise on data protection, contracts with intelligence providers and obligations to report incidents. They need facts and uncertainty stated clearly, not jargon.

### 32.2 Privacy

The data protection officer decides on personal-data processing, retention and breach notification. CTI involving personal data — credential dumps, phishing samples — goes through them.

### 32.3 Clinical leadership

Clinicians decide on patient-safety trade-offs. If intelligence suggests isolating a laboratory system, the clinical lead weighs that against delayed test results. CTI provides the threat picture; clinicians decide.

### 32.4 Communications

If an incident becomes public, communications staff need accurate, approved facts. CTI analysts should never speak to media or post publicly about incidents.

### 32.5 Procurement

Supplier risk assessments benefit from intelligence about supplier compromises. Procurement needs short, sourced summaries they can include in contracts and reviews.

### 32.6 Shared vocabulary

Words carry different meanings across professions. "Incident" for clinicians may mean patient harm; for security, any policy breach. "Confidential" has a legal meaning for lawyers that differs from a TLP label. Agree a small glossary for joint work and define terms on first use in every cross-team note.

### Human resources and insiders

When intelligence touches staff behaviour — a pattern of policy breaches or suspected insider activity — human resources and legal lead, under employment law and fair procedure. CTI analysts provide facts on request and avoid informal investigations of colleagues, which can be unlawful and destroy trust. Keep such matters out of routine briefs and share them only with the people formally assigned.

### Worked example

A ransomware advisory names a pathology supplier used by HCHT. Amara briefs procurement (contract clauses on incident notification), the clinical lead (contingency for manual reporting) and the data protection officer (possible patient-data exposure if the supplier is hit). Each brief is one paragraph in that audience's terms.

> **Synthetic case.** The advisory and supplier are invented.

### Errors and limits

Translation can drop uncertainty. Keep likelihood and confidence in every version.

### Exercises

- **EX094 — Who decides.** Who decides whether to isolate a laboratory system, and what does CTI contribute? *Rubric:* 3 = clinical/system owner decides; CTI provides threat picture; 2 = partial; 1 = CTI decides; 0 = none.
- **EX095 — Media call.** A journalist calls Amara about an incident. What should she do? *Rubric:* 3 = not comment; refer to communications; 2 = decline; 1 = answer; 0 = none.
- **EX096 — Word clash.** Give one term that means different things to clinicians and security staff. *Rubric:* 3 = e.g. "incident" with both meanings; 2 = term only; 1 = none; 0 = none.

### Synthesis

Serve each profession in its language, respect their decisions and keep uncertainty intact in translation.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse coded data with simple statistics; (2) measure inter-coder agreement; (3) present results with uncertainty; (4) write a methods section others can replicate.

### 33.1 From codes to tables

After coding reports, build a table of technique counts by period or sector. Present counts and denominators. A simple bar chart works if axes are labelled and the sample size is visible.

### 33.2 Agreement

Percentage agreement between two coders is easy but inflated by chance. Cohen's kappa corrects for agreement expected by chance. Values near 0 mean chance-level agreement; values above roughly 0.6 are often treated as substantial, though thresholds are conventions.

### 33.3 Uncertainty

With small samples, report ranges or say "too few to compare". Do not run significance tests on a handful of reports and present them as findings.

### 33.4 Methods section

Describe sources, inclusion criteria, dates, coding scheme, coders, agreement and limitations. A reader should be able to repeat the study with the same public sources.

### 33.5 Open materials

Share coding sheets and scripts where licences allow, removing restricted content. Public sources can be listed; TLP-restricted ones cannot.

### 33.6 Negative results

A study that finds no difference between periods is still informative if the method was sound. Report it plainly; hiding unexciting results distorts the literature and wastes the next student's effort repeating the same work.

### Choosing charts

Bar charts suit category counts; line charts suit change over time; tables suit small datasets where exact numbers matter. Avoid pie charts with many slices and three-dimensional effects that distort size. Every chart needs a title, labelled axes, the sample size and the source, so a reader can judge it without the surrounding text. When counts are tiny, a table is usually more honest than any chart.

### Worked example

Amara and a classmate code 30 public health-sector incident reports. They agree on 24 of 30 entry-route labels (80%), but kappa is 0.62 because phishing dominates, inflating chance agreement. They report both, discuss the six disagreements and refine two definitions.

> **Synthetic case.** The study figures are invented for teaching.

### Errors and limits

Kappa depends on category prevalence. Report the confusion table alongside it.

### Exercises

- **EX097 — Kappa reason.** Why is kappa lower than raw agreement in Amara's study? *Rubric:* 3 = corrects for chance agreement, high with dominant phishing category; 2 = chance only; 1 = error; 0 = none.
- **EX098 — Methods contents.** List five things a methods section must describe. *Rubric:* 3 = five of sources, inclusion, dates, scheme, coders, agreement, limitations; 2 = three; 1 = one; 0 = none.
- **EX099 — Tiny sample test.** Why avoid significance tests on five reports? *Rubric:* 3 = too little power; misleading findings; describe instead; 2 = partial; 1 = fine; 0 = none.

### Synthesis

Tabulate honestly, measure agreement with chance correction, respect uncertainty and write replicable methods.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two intelligence-sharing arrangements; (2) build fair comparison criteria; (3) gather evidence lawfully; (4) recommend with stated trade-offs.

### 34.1 The project

Students compare two arrangements: a sector sharing community like HSSC and a commercial intelligence feed. Criteria include relevance to health, timeliness, format (STIX/TAXII support), handling rules, cost, licence terms and feedback mechanisms.

### 34.2 Fair criteria

Define criteria before looking at evidence, so you do not pick criteria that favour a preferred answer. Weight them by HCHT's requirements, and publish the weights.

### 34.3 Evidence

Use documentation, public descriptions, membership agreements available to HCHT and interviews with consenting staff. Do not request trial accounts under false pretences or share HCHT data to test a vendor.

### 34.4 Scoring

Score each criterion 0–3 with written evidence. Sensitivity check: does the recommendation change if one weight changes? If yes, say so.

### 34.5 Recommendation

Recommend with trade-offs: "Keep HSSC as primary for health relevance; add the commercial feed only for vulnerability exploitation data if budget allows."

### 34.6 Comparing like with like

The community shares analysed reports; the feed delivers bulk indicators. Comparing raw volume favours the feed unfairly. Normalise where you can — for example, items that matched HCHT's inventory per month — so the comparison reflects usefulness, not size.

### Stakeholder input

Ask the network team, service desk and supervisor which criteria matter to them and why. Their answers shape weights and reveal hidden requirements — for example, the network team may need indicators in a format their firewall imports directly. Record each stakeholder's view so the final weights can be traced back to real needs rather than the analyst's taste.

### Worked example

Amara's scoring gives HSSC 2.4 and the commercial feed 2.1. When she raises timeliness weight, the feed edges ahead. Her report states that the choice depends on how much HCHT values speed over sector relevance, and suggests a three-month trial measurement.

> **Synthetic case.** The scores are invented.

### Errors and limits

Vendor claims are marketing until verified. Small trials may not reflect long-term value.

### Exercises

- **EX100 — Criteria timing.** Why define criteria before gathering evidence? *Rubric:* 3 = avoids picking criteria to favour a preferred answer; 2 = partial; 1 = order irrelevant; 0 = none.
- **EX101 — Sensitivity.** What did the sensitivity check reveal, and how did Amara report it? *Rubric:* 3 = timeliness weight flips result; stated dependency and proposed trial; 2 = one; 1 = vague; 0 = none.
- **EX102 — Unfair metric.** Why is raw indicator volume an unfair comparison? *Rubric:* 3 = favours bulk feed; volume ≠ usefulness; normalise by relevance; 2 = partial; 1 = fair; 0 = none.

### Synthesis

Fix criteria first, gather evidence lawfully, score with reasons, test sensitivity and recommend with trade-offs.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) write a capstone proposal for a CTI project; (2) define scope, deliverables and success measures; (3) plan data handling and ethics; (4) identify risks to completion.

### 35.1 Choosing a topic

Good capstones solve a real, bounded problem with lawful data. Amara proposes "A lookalike-domain early-warning process for HCHT using certificate-transparency data", which is passive, useful and achievable in one semester.

### 35.2 Structure

Background (the problem and why it matters), aim and questions, method, data and ethics, deliverables, timeline, risks and evaluation plan. Two to three pages is enough.

### 35.3 Scope

State what is in and out. In: generating candidate lookalike names, matching them against public certificate logs, triage rules, a weekly report. Out: contacting domain registrars, takedowns, active scanning of found sites.

### 35.4 Success measures

Measurable: number of HCHT-relevant lookalikes found in a pilot month; share confirmed malicious or suspicious by the supervisor; analyst time per week. Set targets modestly.

### 35.5 Data and ethics

Certificate-transparency data is public, but results may include domains registered by individuals for innocent reasons. Store only domain names and certificate dates; do not research registrants personally. Obtain supervisor and university approval.

### 35.6 Risks

Data volume may exceed laptop capacity; many false positives may overwhelm triage; the supervisor may be unavailable during incidents. Each risk gets a mitigation.

### 35.7 Supervision agreement

Agree meeting frequency, how feedback will be given and what happens if HCHT priorities change mid-project. A one-paragraph agreement signed by student, academic tutor and workplace supervisor prevents later misunderstanding about ownership of results and what may be published.

### Timeline planning

Break the semester into milestones: literature and rules in weeks one to three, pilot generation in weeks four to six, weekly checks in weeks seven to ten, analysis and writing afterwards. Build two buffer weeks for illness or incidents.

### Worked example

Amara's tutor challenges her success measure "find all lookalikes". It is unmeasurable. She replaces it with "list candidate names from 20 generation rules, check them weekly for one month, and report precision as confirmed suspicious divided by flagged".

> **Synthetic case.** The proposal is invented.

### Errors and limits

Proposals change; record changes and reasons in an appendix.

### Exercises

- **EX103 — Out of scope.** Name two activities Amara excluded and why. *Rubric:* 3 = contacting registrars/takedown/active scanning, with reason (authority, legality); 2 = two without reasons; 1 = one; 0 = none.
- **EX104 — Measurable success.** Why is "find all lookalikes" a poor success measure? *Rubric:* 3 = unknowable total; unmeasurable; replace with precision/defined checks; 2 = partial; 1 = fine; 0 = none.
- **EX105 — Registrant privacy.** What data rule protects people who register similar domains innocently? *Rubric:* 3 = store only domain names/dates; no personal research on registrants; 2 = partial; 1 = none; 0 = none.

### Synthesis

Choose a bounded, lawful problem, scope it, measure success realistically and plan ethics and risks.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) contribute to a sharing community responsibly; (2) prepare an item for HSSC; (3) give and receive feedback in a community; (4) reflect on professional conduct.

### 36.1 Placement

During field practice Amara spends four weeks with HSSC's coordination desk, under its membership agreement and a confidentiality undertaking. She sees how items arrive, are checked and are distributed.

### 36.2 Preparing a contribution

A good contribution is relevant to members, verified, redacted, labelled with TLP and clear about confidence. It includes what was observed, when, and what members can do. NIST SP 800-150 notes that organisations should establish sharing rules and protect sensitive information before contributing.

### 36.3 Community norms

Respect labels absolutely; credit sources; correct errors publicly within the community; do not use member information for commercial advantage. Trust is the community's only currency.

### 36.4 Feedback

When a member reports that an indicator caused false positives, the desk updates the item and thanks them. Feedback is how the community learns.

### 36.5 Reflection

Amara keeps a reflective journal: what surprised her, what she would do differently, what professional standards she saw tested.

### 36.6 Community practice beyond work

Some students volunteer with public-interest projects, such as helping small charities understand phishing. Such work needs the same discipline: clear scope agreed in writing, no access to systems without permission, and no collection of personal data beyond what the charity asks to protect.

### Mentoring

Each placement student has a named mentor who reviews every outgoing item. Asking questions early is expected; mentors prefer ten small questions to one serious mistake.

### Worked example

Amara drafts her first HSSC item about a voicemail-themed phishing lure seen at HCHT. Her mentor returns it: the sample still contains a ward extension number. She redacts it, adds a TLP:GREEN label and a short "what to do" line, and the item goes out. Two members report blocking the sender.

> **Synthetic case.** The lure and responses are invented.

### Errors and limits

Placements expose students to restricted material; confidentiality continues after the placement ends.

### Exercises

- **EX106 — Missed extension.** What did Amara miss in her first HSSC draft, and why does it matter? *Rubric:* 3 = ward extension number—identifies staff/internal detail; 2 = item only; 1 = nothing; 0 = none.
- **EX107 — Community currency.** Explain why respecting labels matters so much in a sharing community. *Rubric:* 3 = trust; breaches make members stop sharing; 2 = partial; 1 = rules only; 0 = none.
- **EX108 — Contribution checklist.** List four qualities of a good contribution. *Rubric:* 3 = four of relevant, verified, redacted, labelled, confidence, actions; 2 = three; 1 = one; 0 = none.

### Synthesis

Contribute verified, redacted, labelled items; honour norms; welcome feedback; reflect on conduct.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critique a published intelligence report; (2) separate evidence from assertion; (3) assess analytic standards using ICD 203; (4) give constructive peer critique.

### 37.1 The seminar

Each student brings a public vendor or government CTI report and leads a 20-minute critique. The class asks: what is claimed, what evidence supports it, how confident should we be, and what is missing?

### 37.2 ICD 203 standards

ICD 203 lists analytic tradecraft standards, including describing source quality, expressing uncertainty, distinguishing intelligence from assumptions and judgments, considering alternatives, and being relevant and logically argued. They make a useful checklist for any report.

### 37.3 Evidence versus assertion

A report saying "the actor is state-sponsored" without citing evidence is asserting. One that lists infrastructure overlap, tooling and timing — and states confidence — is arguing.

### 37.4 Alternatives

Did the report consider other explanations? A false-flag possibility, a shared tool sold to many criminals, or coincidence?

### 37.5 Constructive critique

Start with what the report does well; then name specific gaps; propose improvements. Critique the work, not the authors.

### 37.6 Commercial context

Vendor reports also market products. That does not make them wrong, but it shapes what is emphasised — threats their product detects, dramatic names, large numbers. Note the publisher's interest alongside the evidence quality, and look for independent corroboration of headline figures.

### Leading the discussion

The presenter prepares three questions for the class and a one-slide summary of the report's key claims. Timekeeping matters: leave half the slot for discussion, and end by agreeing which parts of the report the class would trust for decisions.

### Worked example

Amara reviews a public report attributing hospital attacks to a named group. It shows overlapping infrastructure but does not discuss shared hosting, and it uses "almost certainly" without explaining the evidence weight. She notes the report is useful for its technique list (T1566, T1486) but rates its attribution confidence as low pending more evidence.

> **Synthetic case.** The report is invented.

### Errors and limits

Public reports omit restricted evidence; absence of evidence in the text does not prove absence of evidence altogether.

### Exercises

- **EX109 — Standards list.** Name three ICD 203 analytic standards. *Rubric:* 3 = three valid (source quality, uncertainty, distinguish assumptions/judgments, alternatives, relevance, logic); 2 = two; 1 = one; 0 = none.
- **EX110 — Alternative explanation.** Suggest an alternative to "shared infrastructure means the same group". *Rubric:* 3 = shared hosting/tools sold widely/coincidence; 2 = vague; 1 = none; 0 = none.
- **EX111 — Missing evidence caution.** Why should a reviewer be careful about concluding a public report "has no evidence"? *Rubric:* 3 = restricted evidence may be withheld; absence in text ≠ absence; 2 = partial; 1 = not careful; 0 = none.

### Synthesis

Read reports against standards, demand evidence, seek alternatives, note interests and critique constructively.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) implement the capstone process in small, testable steps; (2) keep a decision log; (3) manage scope changes; (4) protect data during implementation.

### 38.1 Small steps

Amara builds her lookalike process in stages: a generator that produces candidate names from HCHT's domains using simple rules (character swaps, added words like "portal" or "login", different top-level domains); a matcher that compares candidates with a downloaded, public certificate-transparency extract; a triage sheet. Each stage is tested on synthetic inputs before use.

### 38.2 Decision log

Each design choice is dated with reasons: "Dropped homoglyph rule for Cyrillic letters — produced 4,000 candidates, mostly noise; revisit later." The log becomes part of the final report.

### 38.3 Scope changes

Midway, the supervisor asks to include HSSC member domains. Amara records the request, estimates extra effort, and agrees with her tutor to include only three members as a pilot, keeping the original deliverables intact.

### 38.4 Data protection

Downloaded extracts are stored on the HCHT analysis server, not a personal laptop. Results go to the supervisor only. Domains matching individuals' names are excluded from reports unless clearly impersonating HCHT.

### 38.5 Weekly checks

Every week Amara runs the matcher, triages new matches and records precision: how many flagged domains the supervisor judged suspicious.

### 38.6 Testing with synthetic inputs

Before using real extracts, Amara writes a synthetic list containing known lookalikes, unrelated names and edge cases such as uppercase letters and trailing dots. The matcher must flag exactly the planted lookalikes. When a change to the rules is made, the same test is rerun so regressions show up immediately.

### Worked example

In week two the matcher flags hcht-careers.example. Triage finds a certificate issued the same day and a login form described in public scan results from a reputable passive service. The supervisor rates it suspicious and starts HCHT's takedown process through the proper team. Amara logs the match but takes no action herself.

> **Synthetic case.** The domain and results are invented.

### Errors and limits

Rule-based generation misses creative lookalikes. Report what the rules cannot catch.

### Exercises

- **EX112 — Homoglyph drop.** Why was the Cyrillic homoglyph rule dropped, and how was it recorded? *Rubric:* 3 = 4,000 noisy candidates; logged with date/reason; revisit; 2 = one; 1 = no reason; 0 = none.
- **EX113 — Scope request.** How did Amara handle the request to add member domains? *Rubric:* 3 = recorded, estimated, agreed limited pilot with tutor, kept deliverables; 2 = partial; 1 = accepted all; 0 = none.
- **EX114 — Takedown role.** Who acted on the suspicious domain, and why not Amara? *Rubric:* 3 = supervisor via proper takedown team; intern lacks authority; 2 = partial; 1 = Amara; 0 = none.

### Synthesis

Build in tested steps, log decisions, control scope, protect data and leave actions to those authorised.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate the capstone against its success measures; (2) compute precision and discuss recall limits; (3) gather user feedback; (4) state limitations and future work.

### 39.1 Against the proposal

Evaluation returns to the proposal's measures. Amara planned to report precision, analyst time and number of relevant lookalikes in a pilot month.

### 39.2 Results

Over four weeks, the matcher flagged 25 domains; the supervisor judged 6 suspicious, giving precision of 24%. Analyst time averaged 50 minutes per week. One suspicious domain led to a takedown request.

### 39.3 Recall

Recall — the share of all real lookalikes found — cannot be measured directly because the total is unknown. Amara estimates partial recall by checking whether three lookalikes reported independently by HSSC during the month were caught: two were, one used a pattern her rules lacked.

### 39.4 User feedback

The supervisor values the weekly sheet but asks for fewer obvious false positives, such as domains belonging to unrelated organisations with similar initials.

### 39.5 Limitations

Only certificate-issuing domains are visible; domains without certificates are missed. Rules are English-centric. One month is short.

### 39.6 Future work

Add rules for the missed pattern, filter domains with long legitimate histories, and test for three more months.

### 39.7 Cost and benefit

Fifty minutes a week is modest compared with the effort of responding to a successful credential-phishing campaign. The evaluation states the cost plainly and avoids claiming savings it cannot measure; the benefit is presented as earlier warning of six suspicious domains, one of which was taken down.

### Comparing with the baseline

Before the pilot, lookalikes reached the team only when staff reported suspicious emails. Comparing dates shows whether the new process warned earlier.

### Worked example

Amara's draft claims the system "protects HCHT from lookalike phishing". Her tutor asks for evidence. She rewrites: "In a four-week pilot, the process gave early warning of six suspicious domains, one subsequently taken down; its effect on actual phishing success was not measured."

> **Synthetic case.** The results are invented.

### Errors and limits

Short pilots overstate novelty effects; long-term value needs longer measurement.

### Exercises

- **EX115 — Precision.** Compute precision from 25 flagged and 6 judged suspicious. *Rubric:* 3 = 24% with formula; 2 = number; 1 = wrong; 0 = none.
- **EX116 — Recall estimate.** How did Amara estimate recall without knowing the total? *Rubric:* 3 = checked independently reported HSSC lookalikes—2 of 3 caught; 2 = partial; 1 = guessed; 0 = none.
- **EX117 — Overclaim fix.** Rewrite "protects HCHT from lookalike phishing" honestly. *Rubric:* 3 = early warning of six domains in pilot; effect unmeasured; 2 = softened; 1 = unchanged; 0 = none.

### Synthesis

Measure against the plan, report precision and partial recall, listen to users and state limits plainly.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) structure a bachelor's thesis in CTI; (2) present findings to technical and non-technical audiences; (3) handle restricted material in public documents; (4) answer examiners' questions with evidence.

### 40.1 Thesis structure

Abstract, introduction, background (models: kill chain, Diamond, ATT&CK; standards: STIX/TAXII 2.1, TLP 2.0, SP 800-150), method, implementation, evaluation, discussion, ethics and limitations, conclusion, references and appendices (decision log, coding sheets).

### 40.2 Public versus restricted

Theses are often published by the university. Any TLP:AMBER or RED material from HSSC must be excluded or replaced by synthetic examples. HCHT domains and names may need anonymising with the trust's agreement. Ask HCHT to review the final draft for sensitive content.

### 40.3 The presentation

Ten minutes: problem, approach, key result, limits, what HCHT should do next. One chart showing precision over weeks says more than five tables.

### 40.4 Two audiences

Examiners want method and rigour. HCHT managers want "should we keep doing this?" Prepare a one-page summary for managers with a clear recommendation and its cost.

### 40.5 Answering questions

Answer with evidence and admit what you did not measure. "I don't know, but here is how I would find out" is a strong answer.

### 40.6 After the thesis

Hand the process over properly: documentation, scripts in HCHT's repository, a named owner and a short training session. A capstone that stops when the student leaves delivers little lasting value; a handed-over process keeps protecting the organisation.

### Citing standards correctly

Cite specification versions and dates, such as STIX 2.1 and TLP 2.0, because later versions change definitions. Examiners notice when a thesis quotes outdated guidance.

### Worked example

An examiner asks whether the 24% precision is good. Amara answers that there is no universal benchmark; at 50 minutes per week, the supervisor considered six early warnings worth the time, and she proposes tracking precision as rules improve. She also notes recall was only partially estimated.

> **Synthetic case.** The examination is invented.

### Errors and limits

A thesis is a snapshot; threats and tools move on. Date your conclusions.

### Exercises

- **EX118 — Restricted content.** What must happen to HSSC TLP:AMBER material before the thesis is published? *Rubric:* 3 = exclude or replace with synthetic examples; HCHT/HSSC review; 2 = exclude; 1 = include with credit; 0 = none.
- **EX119 — Manager summary.** What must the one-page manager summary contain? *Rubric:* 3 = clear recommendation, cost/effort, key result; 2 = two; 1 = method detail; 0 = none.
- **EX120 — Unknown answer.** How should Amara answer a question she cannot answer from her data? *Rubric:* 3 = admit, explain how she would find out; 2 = admit; 1 = guess; 0 = none.

### Synthesis

Structure the thesis rigorously, keep restricted material out of public work, speak to both audiences and hand the process over.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Halden County Health Trust, Amara Diallo, the Health Sector Sharing Circle and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Abduction — it proposes the most plausible explanation for an observation without proving it.

**EX002.** Post hoc ergo propter hoc: assuming that because one event followed another, the first caused the second.

**EX003.** What was the baseline number? Over what period was the rise measured? How were attacks counted — and did reporting rules change?

**EX004.** The DNS resolver logs; web proxy logs can corroborate for HTTP traffic.

**EX005.** The imaging servers are certified medical systems with their own safety and change process, owned by clinical engineering.

**EX006.** If a legitimate clinical service shares the domain or depends on it, the block could interrupt patient care.

**EX007.** A set: `feed & seen` returns values present in both collections.

**EX008.** Exactly 64 hexadecimal characters (0–9, a–f).

**EX009.** Label them unknown, keep them out of the indicator store, and ask the sender for the complete values.

**EX010.** Example: "Valid-account abuse (T1078) is a recurring route in the fictional retail reports (claim); it appears in four of six incidents (evidence); because the attackers used real credentials, perimeter controls did not alert (reasoning)."

**EX011.** No. TLP:AMBER limits sharing to the recipient organisation; a public essay must rely on public sources or synthetic examples.

**EX012.** Intelligence writing puts the bottom-line judgment first; academic writing usually builds the argument before concluding.

**EX013.** Tactical — operational detail for analysts configuring filters and hunting.

**EX014.** Direction; written priority intelligence requirements from decision-makers fix it.

**EX015.** Executives decide on priorities and investment; indicators are tactical detail that does not help their decision.

**EX016.** The difference HSSC minus HCHT: elements in the HSSC set that are absent from the blocklist set.

**EX017.** The address serves many unrelated websites, so linking through it creates false connections between domains with no common operator.

**EX018.** Adversary, capability, infrastructure and victim (Caltagirone, Pendergast and Betz, 2013).

**EX019.** The lookalike domain's owner authorised the sending server, but the message is not aligned with HCHT's real domain — a classic lookalike phish.

**EX020.** Almost every network connection begins with a name lookup, so resolver logs cover nearly all devices and applications.

**EX021.** Typically the destination address and server name, not the URL path or the content.

**EX022.** The domain row dated 2026-09-02 had an empty value; the sha256 row dated 2026-09-03 had the wrong length. Three rows were accepted.

**EX023.** AMBER+STRICT limits sharing to the recipient organisation only; mapping it to AMBER would allow wider sharing than the source intended.

**EX024.** Use type plus value as a unique key and update the existing record's metadata instead of inserting a new row.

**EX025.** ('files.example', 'TLP:CLEAR') and ('portal-login.example', 'TLP:GREEN'); a separate count found 2 stale indicators.

**EX026.** So the summary query can exclude restricted rows automatically and nothing beyond its label leaves HCHT.

**EX027.** Send them for review; if confirmed outdated, mark them expired with a date so the history survives.

**EX028.** Data-protection law covers personal data regardless of source; collection needs a lawful basis and purpose, must be minimal, and aggregation can create harmful profiles.

**EX029.** Decline, tell the supervisor, and route the question to HSSC or a contracted provider operating under legal review.

**EX030.** No. It exceeds CTI's mandate and intrudes on uninvolved people; identification of individuals is a law-enforcement matter.

**EX031.** Valid Accounts (T1078): the attacker abuses legitimate credentials rather than exploiting software.

**EX032.** How often the behaviour occurs, or whether it is relevant to your organisation — it only shows it was observed and reported.

**EX033.** The exact query, the date range, the data source searched, and any known gaps in logging coverage.

**EX034.** C2: it uses "very likely" with a 60% estimate, but the team scale reserves that phrase for 80–95%.

**EX035.** If only about 0.01% of email is malicious, flagging 1% means roughly a hundred benign messages for every real phish.

**EX036.** Likelihood is how probable the event is; confidence is how good the evidence and reasoning behind that estimate are.

**EX037.** Phishing (T1566) to obtain the credential, then Valid Accounts (T1078) to use it.

**EX038.** Limit who can see the report; never copy passwords into tickets; force resets through the identity team and notify the data protection officer.

**EX039.** Compare the number of approved suspicious prompts and risky successful sign-ins before and after the change over similar periods.

**EX040.** It is adversary infrastructure — the indicator other HSSC members must block — not information about a victim.

**EX041.** Every sample now receives a manual read for names and free-text identifiers before it is shared.

**EX042.** No. Stable labels are pseudonymisation; if anyone can re-link them, the data remains personal data.

**EX043.** Inference — it goes beyond the logged connection to infer a user action.

**EX044.** Two of the three feeds cited the third, so there was a single independent source and confidence did not rise.

**EX045.** Activity. An outcome alternative is the number of blocked connections that prevented credential entry or the number of hunts that found real activity.

**EX046.** Endpoint protection and mail attachment scanning — they inspect files and can block exact hashes reliably.

**EX047.** Many legitimate services share cloud addresses, so blocking one could cut off clinical or business systems.

**EX048.** Are backups offline or immutable? One site lacked this, so an immutable copy was added.

**EX049.** Changing one byte of a file creates a new hash, so the adversary pays almost nothing to evade a hash block.

**EX050.** That the connection is encrypted to whoever holds a valid certificate for that name — not that the site is honest.

**EX051.** Certificate-transparency logs: they publicly record new certificates, so lookalike names appear without contacting the site.

**EX052.** Example: "What share of HSSC advisories in 2026 led members to report a defensive action within 30 days?"

**EX053.** Selection bias: vendors publish unusual or commercially useful cases, so common, dull intrusions are under-represented.

**EX054.** Informed consent from each participant and university ethics approval; questions must avoid restricted material.

**EX055.** The intrusion kill chain, because it lays out phases at which defenders can detect or disrupt the attack.

**EX056.** STIX 2.1 is the JSON language describing threat information; TAXII 2.1 is the HTTPS protocol for exchanging it.

**EX057.** It turns into a news feed: interesting reading that changes no control or priority.

**EX058.** Defenders can use what they learn from every intrusion attempt, even failed ones, to stop the same adversary at earlier phases next time.

**EX059.** Adversaries change domains and addresses cheaply, but their techniques and habits change slowly.

**EX060.** Organisations with offline backups recovered faster than those without.

**EX061.** Analysis: forty items reached it but only twelve were completed, so work accumulated there.

**EX062.** Repeated false-positive blocks annoy the network team, who then deprioritise CTI requests, so even good intelligence acts more slowly.

**EX063.** A relationship object, for example of type "indicates", from the indicator to the malware.

**EX064.** The commercial licence may prohibit redistribution, so sharing could breach the contract.

**EX065.** Write clear documentation of the pipeline and train a second person to run and fix it.

**EX066.** Provider, delivery method, licence or terms, and TLP (also format, cost and owner).

**EX067.** Phishing (T1566) and Data Encrypted for Impact (T1486), each in 3 of 5 reports.

**EX068.** If HCHT runs an unpatched internet-facing application, its exposure makes the technique important regardless of how often others reported it.

**EX069.** So reviewers can check that each tag is supported by the text and correct mis-coding.

**EX070.** The intelligence with source and TLP, the ATT&CK technique, the proposed control, the expected benefit and side effects (plus owner and deadline).

**EX071.** Laboratory staff rely on a macro spreadsheet; an unconsulted block could halt test reporting.

**EX072.** From an approved test device, check that the domain no longer resolves or connects, and log the time and result.

**EX073.** Validate, then store, then redact the sample, then summarise; validation comes first so bad rows never enter the database.

**EX074.** The filter compared labels case-sensitively, so "tlp:amber" did not match the exclusion; converting labels to upper case at import fixed it.

**EX075.** Stop working with it, do not copy it anywhere, and tell the instructor immediately.

**EX076.** The information is graded 5, improbable; even completely reliable sources sometimes pass on errors, so it is held until verified.

**EX077.** F6: F because the poster cannot be assessed; 6 because no sample or evidence allows the claim to be judged.

**EX078.** "B: this provider's last 20 reports were checked and 18 proved accurate."

**EX079.** It makes contact with adversary infrastructure, which can reveal HCHT's interest, expose the device and breaks policy.

**EX080.** Ask what observation each report is based on; only reports resting on different observations are independent.

**EX081.** HCHT's own mail logs showing four messages to finance staff — direct evidence of relevance.

**EX082.** Dissemination failure: the correct advisory arrived but no owner received it, so nothing happened until the probing.

**EX083.** Having decided a phishing wave came from a familiar criminal group, an analyst notes only the overlapping domains and ignores differences in lure language and timing that point elsewhere.

**EX084.** "Every advisory is matched to the inventory, assigned an owner within one working day, and the owner confirms receipt in the ticket."

**EX085.** TLP:AMBER+STRICT restricts sharing to HCHT itself; contacting the supplier needs the originator's permission.

**EX086.** Log them briefly and set them aside unless a later check shows relevance to HCHT.

**EX087.** Arrival time, source, TLP label, grade, decision (also actions taken and closure date).

**EX088.** Collect all object identifiers in the bundle and confirm each relationship's source_ref and target_ref appears in that set.

**EX089.** The identifier stays the same; the modified timestamp is updated to the time of the change.

**EX090.** Every relationship points to existing objects; timestamps are UTC; each object carries a TLP marking (and no personal data is present).

**EX091.** 32 minutes (09:30 to 10:02); detection on early phases must reach a responder within minutes.

**EX092.** Registering a domain is acquiring infrastructure (resource development, T1583), done before the intrusion; kill-chain weaponization strictly means building the payload.

**EX093.** Email filtering that blocks the lookalike sender domain and quarantines its messages.

**EX094.** The clinical lead and system owner decide, weighing patient safety; CTI supplies the threat likelihood and evidence.

**EX095.** Make no comment and refer the journalist to HCHT communications.

**EX096.** "Incident": for clinicians, an event affecting patient care; for security, any security-policy violation or attack event.

**EX097.** Kappa subtracts the agreement expected by chance; because most reports are phishing, coders would often agree by chance alone.

**EX098.** Sources, inclusion criteria, date range, coding scheme and agreement measure (also coders and limitations).

**EX099.** Five observations give almost no statistical power, so tests produce misleading results; describe the counts instead.

**EX100.** Choosing criteria first prevents the analyst from selecting measures that favour the option they already prefer.

**EX101.** Increasing the timeliness weight made the commercial feed win; she reported that the choice depends on that priority and proposed a measured trial.

**EX102.** Bulk feeds always win on volume, but volume does not equal usefulness; compare relevant matches instead.

**EX103.** Contacting registrars or requesting takedowns (outside an intern's authority) and actively scanning found sites (not passive and may be unlawful).

**EX104.** Nobody can know the total number of lookalikes, so success cannot be measured; a defined check with precision can be.

**EX105.** Keep only domain names and certificate dates and do not investigate the people behind registrations.

**EX106.** A ward extension number remained, exposing internal contact details that should never leave HCHT.

**EX107.** Members share only if they trust that labels will be respected; one breach can make them stop contributing.

**EX108.** Relevant to members, verified, redacted, labelled with TLP (also clear confidence and suggested actions).

**EX109.** Properly describe the quality of sources; express and explain uncertainty; incorporate analysis of alternatives (also distinguish intelligence from assumptions, be relevant, use logical argument).

**EX110.** The infrastructure may be a shared hosting service or a tool sold to many criminals, so different groups could appear connected.

**EX111.** Authors may hold restricted evidence they cannot publish; the text lacking evidence does not prove the judgment is unfounded.

**EX112.** It generated about 4,000 mostly irrelevant candidates; she logged the date and reason and noted it for later review.

**EX113.** She recorded the request, estimated the effort and agreed with her tutor to pilot three member domains while keeping original deliverables.

**EX114.** The supervisor started HCHT's takedown process through the responsible team; Amara has no authority to act on external domains.

**EX115.** Precision = suspicious ÷ flagged = 6 ÷ 25 = 24%.

**EX116.** She checked whether lookalikes that HSSC reported independently during the month were also caught: two of three were.

**EX117.** "During a four-week pilot the process warned early of six suspicious domains, one later taken down; its effect on phishing success was not measured."

**EX118.** It must be removed or replaced with synthetic examples, and HCHT (and HSSC if referenced) should review the draft before publication.

**EX119.** A clear recommendation on whether to continue, the weekly cost in analyst time and the headline result from the pilot.

**EX120.** Say she does not know from her data, then describe the measurement or study that would answer it.

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
