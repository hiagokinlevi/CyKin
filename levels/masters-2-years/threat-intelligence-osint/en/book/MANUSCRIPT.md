# Threat Intelligence and OSINT: A Master's Research Book

- Language: English (`en`); master's course, two years.
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX056 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, with outputs embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students who will design and defend a bounded empirical study in cyber threat intelligence (CTI) or OSINT practice.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical boundary: no collection on real private individuals, no terms-of-service evasion, no access to adversary systems. Organisations, people and datasets are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–2 frame a question and survey the field; 3 covers design, ethics and reproducibility; 4 trains competing-hypothesis reasoning; 5 is proposal and pilot; 6 collects and analyses; 7 writes with limitations; 8 handles independent review and defence. Each chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, seven exercises scored 0–3, a synthesis and a **Continue studying** block.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Coastline Ports Sharing Group (CPSG)** — a sector community of twelve port operators exchanging indicators over TAXII 2.1 | Population studied | Invented |
| **Lucía Ferraz** | Master's student measuring whether membership shortens time-to-block | Invented |
| **Prof. Daniel Okafor** | Dissertation supervisor | Invented |

### Core sources

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) and [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); Hutchins et al. [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf); NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn a practitioner worry into a researchable question; (2) run a documented literature search with inclusion criteria; (3) grade sources by type and reliability; (4) keep a search log that someone else can repeat.

### 1.1 From worry to question

Port security managers in CPSG believe that sharing indicators "helps". Lucía converts that belief into a question with a population, an intervention, a comparison and an outcome: among port operators, does receiving indicators through CPSG's TAXII 2.1 collection shorten the time between an indicator's first publication and a block rule in the member's controls, compared with similar operators outside the group? That structure makes clear what data she needs and what she does not.

The outcome, hours from publication to block, is the part port managers had never measured.

### 1.2 Search method

A literature method states databases, search strings, date limits, languages, and inclusion and exclusion rules. Lucía searches digital libraries for "threat intelligence sharing" AND (effectiveness OR evaluation OR measurement), 2011–2026, English and Spanish. She includes empirical studies and standards; she excludes marketing pages without method.

Her first run of that string returned 412 records. The Spanish-language limb matters for a ports question, because several port authorities in her region publish security guidance only in Spanish; leaving it out would bias the review towards English-speaking operators. The date limit starts in 2011, before STIX and TAXII 2.1, so that early sharing studies are included.

### 1.3 Grading sources

Standards such as NIST SP 800-150 and the OASIS STIX/TAXII 2.1 specifications define practice and formats. Peer-reviewed studies test claims. Vendor reports describe observations under commercial incentives. Government guidance such as ICD 203 sets analytic norms. A literature chapter should keep these strands distinct so that a reader knows which claims are measured and which are recommended.

Lucía's 19 included works split along these lines: 4 standards, 9 peer-reviewed studies and 6 grey-literature reports. Only 3 of the studies measured an outcome rather than describing a process, so her literature chapter can say exactly how thin the measured evidence is, instead of letting six confident vendor reports stand in for it.

### 1.4 The search log

Each search gets a row: date, database, string, hits, screened, included, reason for exclusions. The log is an appendix, and it lets an examiner see that the review was not cherry-picked.

Lucía's log shows the funnel in numbers: 412 records, 300 removed on titles, 80 more on abstracts, and 19 included after full-text reading. Each removal step names its reason, such as "no measured outcome" or "marketing page without method". An examiner who doubts an exclusion can find the row and judge it, and another student can rerun the same strings on the same date range and compare the counts.

### Worked example

Lucía's first string returns 412 records. Screening titles removes 300 off-topic items; abstracts remove 80 more; full-text reading leaves 19 included works: 4 standards, 9 peer-reviewed studies, 6 grey-literature reports. She notes that only 3 studies measure an outcome rather than describing a process — the start of her gap.

> **Synthetic case.** CPSG and Lucía's search counts are invented.

### Errors and limits

Searching only one database, or changing inclusion rules after reading results, biases a review. A master's review is systematic in method even when it is not a full systematic review.

### Exercises

- **EX001 — PICO shape.** Label the population, intervention, comparison and outcome in Lucía's question. *Rubric:* 3 = all four correct; 2 = three; 1 = one or two; 0 = none.
- **EX002 — Inclusion rule.** Write one inclusion and one exclusion criterion for her review. *Rubric:* 3 = one clear criterion of each tied to question; 2 = one clear; 1 = vague; 0 = none.
- **EX003 — Strand placement.** Place NIST SP 800-150 in the right source strand and explain. *Rubric:* 3 = standard/guidance; defines practice, not measured outcomes; 2 = strand only; 1 = peer-reviewed study; 0 = none.
- **EX004 — Log row.** Write a complete search-log row for her first search. *Rubric:* 3 = date, database, string, hits, screened, included, exclusion reasons; 2 = five fields; 1 = two; 0 = none.
- **EX005 — Funnel numbers.** From 412 hits, how many remained after abstract screening? *Rubric:* 3 = 32; 2 = method right; 1 = wrong; 0 = none.
- **EX006 — Gap seed.** What observation from the screening suggests a research gap? *Rubric:* 3 = few studies measure outcomes (3 of 19); 2 = few studies; 1 = many studies; 0 = none.
- **EX007 — Cherry-picking.** Why must inclusion rules be fixed before screening? *Rubric:* 3 = prevents selecting sources to fit a conclusion; repeatability; 2 = fairness vaguely; 1 = speed; 0 = none.

### Synthesis

Structure the question, document the search, keep source strands separate, and log every step so the review can be repeated.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Threat intelligence and OSINT: advanced seminar

### Learning outcomes

You will (1) compare the intelligence cycle with CTI practice in a SOC; (2) explain strategic, operational and tactical intelligence; (3) relate the kill chain, Diamond Model and ATT&CK to analyst tasks; (4) discuss OSINT's legal and ethical limits at seminar depth.

### 2.1 Cycle versus practice

Textbook intelligence moves through direction, collection, processing, analysis, dissemination and feedback. In a port SOC the cycle is compressed and noisy: requirements arrive as incident tickets, collection is a feed subscription, and feedback is rare. Seminar discussion should ask where the cycle breaks — usually at direction and feedback.

Lucía's question tests one point where the cycle breaks. CPSG members receive indicators by TAXII subscription, so collection works; what nobody measured was dissemination into controls, the time from publication to a block rule. Her study adds a feedback loop the group never had.

### 2.2 Three levels

Strategic intelligence informs boards about adversary intent and trends; operational intelligence describes campaigns and their timing; tactical intelligence supplies indicators and technique detail. Lucía's study sits at the tactical–operational boundary: indicators and how quickly they become controls.

Lucía's seminar bulletin about the phishing wave against port agents shows the boundary in practice: its campaign timing is operational, while its indicators are tactical. Her study measures the tactical part, how fast indicators become block rules, and says nothing about whether board-level strategy changed because of CPSG.

### 2.3 Models as tools for tasks

Hutchins et al. help decide where to place controls across phases. The Diamond Model helps pivot from one event to related events through shared infrastructure or capability. ATT&CK supplies a common vocabulary — for example T1566 Phishing or T1071 Application Layer Protocol — that lets a sharing group describe behaviour beyond fragile indicators, which Bianco's Pyramid of Pain ranks as more costly for adversaries to change.

Lucía's seminar mapping of the port-agent phishing wave to T1566 is the example: the bulletin's domains and IP addresses will be stale within days, but the behaviour description remains useful to members who never saw the original indicators.

### 2.4 OSINT at seminar depth

Open sources include company filings, ship-tracking broadcasts, public code repositories and news. Using them still raises duties: data-protection law where people are identifiable, platform terms, and the risk of tipping off subjects. Seminar exercises use synthetic profiles only.

For a ports group the risk is concrete. Ship-tracking broadcasts and company filings can be combined to show which agent handled which vessel, and identify the staff targeted by the phishing wave. Lucía's study needs none of that: her data are timings from members' controls, so OSINT on people stays outside the design, and seminar exercises use synthetic profiles instead.

### 2.5 TLP and sharing culture

FIRST TLP 2.0 defines CLEAR, GREEN, AMBER, AMBER+STRICT and RED. Communities like CPSG depend on members honouring labels; one breach can end sharing for years.

CPSG's collection is TLP:AMBER, which is why Lucía needs the governance board's agreement and why her dissertation, written for the university library, must be TLP:CLEAR. A figure caption naming a port's city would have been such a breach, and the leak reviewer caught one before submission. The board's three conditions, groups of at least three, no port names and deletion of raw timings, are how Lucía's study honours AMBER while still producing a public dissertation.

### Worked example

In seminar, Lucía presents a CPSG bulletin about a phishing wave against port agents. She classifies it as operational (campaign timing), maps the behaviour to T1566, notes that the indicators are low on the Pyramid of Pain, and argues that the ATT&CK mapping is the more durable contribution.

> **Synthetic case.** The bulletin and phishing wave are invented.

### Errors and limits

Treating every feed as "intelligence" confuses data with analysis. OSINT legality varies by jurisdiction; seminar conclusions are not legal advice.

### Exercises

- **EX008 — Broken stage.** Which intelligence-cycle stages most often break in a SOC, and why? *Rubric:* 3 = direction and feedback, with reason; 2 = one with reason; 1 = collection only; 0 = none.
- **EX009 — Level call.** Classify "ransomware groups increasingly target logistics firms" by intelligence level. *Rubric:* 3 = strategic (trend for decision-makers); 2 = level only; 1 = tactical; 0 = none.
- **EX010 — Durable layer.** Why is the ATT&CK mapping more durable than the bulletin's IP list? *Rubric:* 3 = behaviours costlier to change than IPs (Pyramid of Pain); 2 = partial; 1 = IPs more durable; 0 = none.
- **EX011 — Diamond use.** Give a pivot the Diamond Model enables with the phishing bulletin's sender domain. *Rubric:* 3 = infrastructure → other events/victims using same domain/registrant; 2 = vague pivot; 1 = none; 0 = none.
- **EX012 — TLP five.** List the five TLP 2.0 labels. *Rubric:* 3 = CLEAR, GREEN, AMBER, AMBER+STRICT, RED; 2 = four; 1 = old WHITE label; 0 = none.
- **EX013 — Tip-off risk.** Why can careless OSINT collection harm an investigation? *Rubric:* 3 = may alert subject/adversary, causing changes or harm; 2 = vague risk; 1 = no risk; 0 = none.
- **EX014 — Kill-chain placement.** Where in the kill chain does a phishing email arrive? *Rubric:* 3 = delivery; 2 = adjacent phase with reason; 1 = actions on objectives; 0 = none.

### Synthesis

Know where the cycle breaks, label the level, prefer durable behaviour descriptions, and practise OSINT within law, terms and TLP.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) choose between observational and quasi-experimental designs; (2) identify confounders in sharing studies; (3) obtain consent from sharing-community members for research use; (4) plan a reproducible analysis.

### 3.1 Observational limits

Lucía cannot randomly assign ports to CPSG membership. She can compare members with non-members, but members may differ — larger budgets, more staff — and those differences, not sharing, might explain faster blocking. A design that ignores this is a correlation study dressed as an evaluation.

Lucía's design responds with two comparisons: four ports that joined CPSG in 2025 are compared with themselves before and after joining, and members are compared with six volunteer non-members matched on size. Neither removes all differences, but they fail in different ways, so agreement between them is more convincing than either alone.

### 3.2 Handling confounders

Options include matching members to non-members of similar size, comparing the same port before and after joining, or adjusting for SOC staffing. Each choice is written into the proposal, not chosen after seeing which gives the nicer result.

Lucía chose both matching on size and a before-and-after stratum for the four ports that joined in 2025, and wrote that choice into the proposal before collecting any timings. If the before-and-after stratum shows a consistent drop on joining, she can speak more strongly than the cross-sectional comparison allows.

### 3.3 Consent and TLP

CPSG data carries TLP:AMBER. Research use needs explicit agreement from the community's governance board, and each member must be able to opt out. Results will be aggregated so that no single member's timings can be recovered. Non-member data must come from voluntary participants, not from probing their infrastructure.

The governance board approved Lucía's design with three conditions: results aggregated to groups of at least three, no port names, and deletion of raw timings after the dissertation is marked. The six non-member ports supplied their own timings voluntarily; nothing was collected from their infrastructure without their participation.

### 3.4 Personal data

Time-to-block logs may include analyst user names. Lucía removes them at source; she needs timings, not people. Data-protection law such as the GDPR applies even in security research, and minimisation is the simplest compliance step.

Removing names at source means the member's export to Lucía contains only timestamps, indicator type and decision. If an analyst's name were kept even in a working file, the data would identify the person who was slow to block a particular indicator, a harm to that analyst that the study does not need to risk.

### 3.5 Reproducibility plan

Analysis scripts in the standard library, a data dictionary, synthetic sample files and a fixed random seed for any resampling. The plan is part of the proposal.

For Lucía, the synthetic sample files mirror the data dictionary exactly, so an examiner without access to CPSG's AMBER data can still run every script. The fixed seed matters for the bootstrap interval around the medians; without it, a rerun would give a slightly different interval and look like an error. The synthetic files use exactly the fields in her data dictionary, `t_pub`, `t_block`, `ttb_h`, `ioc_type` and `decision`, so the same scripts run on both.

### Worked example

Lucía proposes a before-and-after design for four ports that joined CPSG in 2025, plus matched comparison with six non-members who volunteer. The governance board approves with conditions: aggregation to groups of at least three, no port names, and deletion of raw timings after the dissertation is marked.

> **Synthetic case.** The design, ports and board conditions are invented.

### Errors and limits

Small samples cannot support causal claims even with good design; frame findings accordingly. Consent by a board does not override an individual member's opt-out.

### Exercises

- **EX015 — Confounder name.** Name one confounder between CPSG membership and faster blocking. *Rubric:* 3 = plausible confounder (budget, staff size, maturity) with mechanism; 2 = name only; 1 = unrelated; 0 = none.
- **EX016 — Design pick.** Why does a before-and-after design help with that confounder? *Rubric:* 3 = same port compared with itself holds stable traits constant; 2 = partial; 1 = no help; 0 = none.
- **EX017 — Board condition.** Explain the purpose of "aggregation to groups of at least three". *Rubric:* 3 = prevents recovering single member's data; 2 = privacy vaguely; 1 = statistics only; 0 = none.
- **EX018 — Non-member data.** How may Lucía obtain non-member timings? *Rubric:* 3 = voluntary participants sharing their own logs under agreement; never probing; 2 = voluntary only; 1 = scan their systems; 0 = none.
- **EX019 — Minimise logs.** What field should be removed from time-to-block logs and why? *Rubric:* 3 = analyst usernames; not needed; personal data; 2 = remove names; 1 = keep all; 0 = none.
- **EX020 — Opt-out conflict.** The board approves but one member opts out. What happens? *Rubric:* 3 = exclude that member's data; board consent does not override; 2 = exclude; 1 = include; 0 = none.
- **EX021 — Seed reason.** Why fix a random seed for resampling? *Rubric:* 3 = identical results on rerun; reproducibility; 2 = vague; 1 = speed; 0 = none.

### Synthesis

Name confounders early, pick a design that weakens them, obtain board and member consent, minimise personal data, and plan reproducibility before data arrive.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Threat intelligence and OSINT: competing explanations

### Learning outcomes

You will (1) build an analysis-of-competing-hypotheses (ACH) matrix; (2) identify diagnostic evidence; (3) express a judgment with calibrated estimative language; (4) record what new evidence would change the judgment.

### 4.1 Why competing explanations

Analysts tend to settle on the first plausible story. Heuer's method forces several hypotheses onto the table and asks which evidence is inconsistent with each. The hypothesis with the fewest serious inconsistencies survives — provisionally.

Lucía's seminar exercise on the CPSG ransomware incident uses three hypotheses: a criminal ransomware crew (H1), an insider (H2) and state-aligned espionage (H3). Listing all three before reading the evidence stops the most common story, ransomware means criminals, from closing the question too early. In the CPSG ransomware exercise, all three are scored against the same five evidence items, E1 to E5, so no hypothesis is judged on evidence chosen to suit it.

### Lab 1 — ACH matrix

```python
"""Lab 1 (ch 04): analysis of competing hypotheses - count inconsistencies per hypothesis (synthetic)."""
hyps = ["H1 criminal ransomware crew", "H2 insider", "H3 state-aligned espionage"]
# per evidence item: C consistent, I inconsistent, N neutral for H1,H2,H3
evidence = [
    ("E1 data staged then encrypted",         "C", "N", "I"),
    ("E2 access from a contractor VPN account", "C", "C", "C"),
    ("E3 ransom note with payment portal",     "C", "I", "I"),
    ("E4 activity outside staff working hours", "C", "I", "N"),
    ("E5 tooling sold on criminal markets",    "C", "N", "I"),
]
for i, h in enumerate(hyps):
    inc = sum(1 for e in evidence if e[i + 1] == "I")
    print(f"{h:30} inconsistent={inc}")
diag = [e[0] for e in evidence if len(set(e[1:])) > 1]
print("diagnostic items:", len(diag), "of", len(evidence))
```

Run with `python3 lab_ach.py`. Verified output:

```text
H1 criminal ransomware crew    inconsistent=0
H2 insider                     inconsistent=2
H3 state-aligned espionage     inconsistent=3
diagnostic items: 4 of 5
```

### 4.2 Reading the matrix

H1, a criminal ransomware crew, has no inconsistencies; H2, an insider, has two; H3, state-aligned espionage, has three. Item E2 — access from a contractor VPN account — fits every hypothesis and is therefore not diagnostic. Four of five items discriminate. The matrix does not prove H1; it shows H1 is least contradicted by this evidence.

Lucía's written judgment follows directly: it is likely, 55–80% on her scale, that a criminal crew conducted the intrusion, and an insider role cannot be excluded. The non-diagnostic E2 is worth naming in the write-up, because analysts often cite such evidence first.

### 4.3 Estimative language

ICD 203 asks products to express uncertainty and to distinguish evidence from judgment. Kent's essay on words of estimative probability showed how readers interpret "probable" very differently. A team should publish its own scale — for example "likely" meaning roughly 55–80% — and use it consistently.

Lucía's ransomware judgment uses that scale: "likely (55–80%)". A member reading "likely" in one CPSG bulletin and "likely" in another should take the same meaning from both, which only works if the group publishes its scale and every writer applies it.

### 4.4 Change triggers

Every judgment carries indicators that would change it: evidence of data sale without ransom (would raise H3), or a confession from a disgruntled employee (would raise H2). Writing triggers prevents silent drift.

Lucía's written assessment names one trigger in its last sentence: evidence of data sale without a ransom demand would lower the criminal-crew assessment. Naming the trigger in the product lets a member who later sees such evidence know at once that the judgment should be reopened. Lucía's matrix needs both kinds of trigger because E2, access from a contractor VPN account, fits every hypothesis and cannot settle the question by itself.

### 4.5 ATT&CK as evidence vocabulary

Mapping evidence to ATT&CK — staging and T1486 Data Encrypted for Impact for E1 — helps other analysts check whether behaviour matches a known group's profile without overrelying on names.

For the CPSG incident, T1486 describes the encryption itself, and the contractor VPN access in E2 can be mapped to valid-account use. Members comparing that profile with published group reports can see whether the behaviour fits, while the write-up avoids naming a group on the strength of one similarity. In Lucía's matrix, the T1486 label sits beside E1 as a description of what was observed; it is not treated as evidence for any particular group.

### Worked example

A CPSG member suffers a ransomware incident. Lucía, as a seminar exercise, builds the matrix and writes: "We assess it is likely (55–80%) that a criminal ransomware crew conducted this intrusion; an insider role cannot be excluded. Evidence of data sale without a ransom demand would lower this assessment."

> **Synthetic case.** The incident and evidence items are invented.

### Errors and limits

ACH depends on the hypotheses considered; a missing hypothesis cannot win. Counting inconsistencies is a heuristic, not a probability calculation.

### Exercises

- **EX022 — Matrix result.** Quote the inconsistency counts for H1, H2 and H3. *Rubric:* 3 = 0, 2, 3; 2 = two right; 1 = one; 0 = none.
- **EX023 — Non-diagnostic.** Which evidence item is not diagnostic, and why? *Rubric:* 3 = E2; consistent with all hypotheses; 2 = E2 only; 1 = wrong item; 0 = none.
- **EX024 — Survives, not proven.** Why is "H1 is proven" the wrong conclusion? *Rubric:* 3 = least contradicted only; hypotheses set may be incomplete; evidence limited; 2 = one reason; 1 = it is proven; 0 = none.
- **EX025 — Scale entry.** Define "likely" on a published team scale and explain why the definition matters. *Rubric:* 3 = numeric range + readers interpret words differently (Kent); 2 = range only; 1 = no range; 0 = none.
- **EX026 — Trigger.** Write one change trigger that would raise H2. *Rubric:* 3 = specific observable evidence favouring insider; 2 = vague; 1 = none; 0 = none.
- **EX027 — Missing hypothesis.** Propose a fourth hypothesis worth adding. *Rubric:* 3 = plausible distinct hypothesis (e.g. hacktivist, access broker reselling) with reason; 2 = name only; 1 = duplicate; 0 = none.
- **EX028 — Technique ID.** Give the ATT&CK technique ID for data encrypted for impact. *Rubric:* 3 = T1486; 2 = name only; 1 = wrong ID; 0 = none.

### Synthesis

List rivals, seek inconsistencies, report survivors with calibrated words, and write what would change your mind.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write a dissertation proposal with measurable aims; (2) define each variable in a data dictionary; (3) run a pilot to check feasibility; (4) revise the plan from pilot evidence without changing the question.

### 5.1 Aims and measures

Aim 1: measure median time-to-block for indicators received via CPSG. Aim 2: compare with matched non-members. Aim 3: describe how often shared indicators were judged not worth blocking. Each aim names its variable and its analysis.

Aim 3 is easy to forget but matters for interpretation. If members ignore many shared indicators as low-value, a fast median for the blocked ones may hide the fact that most indicators never become controls. Reporting the blocked, monitored and ignored proportions beside the median keeps the result honest.

### 5.2 Data dictionary

`t_pub`: timestamp the indicator was first published to the TAXII collection (UTC). `t_block`: timestamp a block rule became active in the member's control. `ttb_h`: hours between them. `ioc_type`: domain, ip, hash or url. `decision`: blocked, monitored, ignored. Every field has a type, unit and allowed values.

The dictionary also decides how a missing value is handled: an indicator that was ignored has no `t_block`, so its `ttb_h` is empty rather than zero, and it is counted under Aim 3, not in the median. Fixing that rule before data arrive prevents ignored indicators being treated as instant blocks.

### 5.3 Pilot

A pilot with one member and two weeks of synthetic-format logs tests whether `t_block` is recorded at all. Many organisations log rule edits only in change tickets with day-level precision, which would make hour-level timings impossible.

Lucía's pilot found exactly this split: the first member's firewall recorded rule activation to the second, while the second member's ticketing tool held dates only. Finding it in the pilot, with two weeks of logs, cost little; finding it after the main collection would have forced a redesign.

### 5.4 Revising without drifting

If the pilot shows day-level precision only, Lucía can change the unit to days — a measurement revision — but should not change the question to something easier, such as "do members like the feed?" That would be scope drift.

Lucía's revision kept both units: hours for members with precise logs, and days for the others as a separate stratum, with the reduced precision noted as a limitation. The question, time from publication to block, did not change; only how precisely some members could answer it.

### 5.5 Indicator formats

CPSG publishes STIX 2.1 indicator objects. The pilot confirms that `created` and `valid_from` are populated, giving a trustworthy `t_pub`. Objects missing required properties are logged as data-quality findings for the community.

The data-quality findings are recorded by publishing member class, not by member, following the board's aggregation rule. An indicator without `valid_from` still counts for Aim 3 if a member acted on it, but it cannot contribute a publication time to the median. The pilot member's two weeks of logs gave Lucía a first count of such findings before the main export arrived.

### Worked example

The pilot member's firewall records rule activation to the second, but the second member uses a ticketing tool with dates only. Lucía keeps hours for members with precise logs, records days for the others as a separate stratum, and notes the reduced precision as a limitation.

> **Synthetic case.** Pilot members and logging tools are invented.

### Errors and limits

A pilot is not a small version of the result; do not report its medians as findings. Changing the question after a pilot requires supervisor approval and a new ethics check.

### Exercises

- **EX029 — Variable entry.** Write a complete data-dictionary entry for `ttb_h`. *Rubric:* 3 = name, definition, type, unit, derivation; 2 = three of those; 1 = name only; 0 = none.
- **EX030 — Pilot purpose.** What specific feasibility question does the two-week pilot answer? *Rubric:* 3 = whether t_block is logged with usable precision; 2 = data exists generally; 1 = whether sharing works; 0 = none.
- **EX031 — Precision fix.** How does Lucía handle a member logging dates only? *Rubric:* 3 = separate day-level stratum + limitation; 2 = drop member; 1 = guess hours; 0 = none.
- **EX032 — Drift test.** Is switching to "do members like the feed?" a revision or drift? Explain. *Rubric:* 3 = drift; changes construct away from time-to-block; 2 = drift; 1 = revision; 0 = none.
- **EX033 — Aim three.** Why is the "ignored" decision value important for Aim 3? *Rubric:* 3 = captures indicators judged not worth blocking; avoids survivorship view; 2 = partial; 1 = irrelevant; 0 = none.
- **EX034 — STIX time.** Which STIX 2.1 properties give a trustworthy publication time? *Rubric:* 3 = created (and valid_from) on the indicator; 2 = one; 1 = name; 0 = none.
- **EX035 — Pilot numbers.** May Lucía cite the pilot median in her results chapter? *Rubric:* 3 = no; pilot only tests feasibility; mention in methods; 2 = no; 1 = yes; 0 = none.

### Synthesis

Measurable aims, a precise dictionary, a pilot aimed at feasibility, and revisions that keep the question intact.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) validate incoming structured data before analysis; (2) compute and compare medians for skewed timing data; (3) report effect sizes with honest uncertainty; (4) separate descriptive findings from causal claims.

### 6.1 Validate first

Members export STIX 2.1 objects from CPSG's TAXII collection with their block logs. Before any statistics, Lucía checks that objects carry required properties and well-formed identifiers. Malformed objects are counted and reported to the community, not silently repaired.

Lucía's demonstration batch checks three objects, and only one passes. Across the full study export, 94% of indicators were valid. Counting failures before analysis tells the reader how much of CPSG's data could contribute timings at all. An invalid object that a member still blocked or monitored is counted under Aim 3, because the member's decision happened even though its publication time cannot be trusted.

### Lab 2 — STIX property check

```python
"""Lab 3 (ch 06): check synthetic STIX 2.1-style objects for common required properties."""
import json, re
objs = json.loads("""[
 {"type":"indicator","spec_version":"2.1","id":"indicator--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
  "created":"2026-09-01T10:00:00.000Z","modified":"2026-09-01T10:00:00.000Z",
  "pattern":"[domain-name:value = 'c2.example']","pattern_type":"stix","valid_from":"2026-09-01T10:00:00Z"},
 {"type":"indicator","spec_version":"2.1","id":"indicator-123",
  "created":"2026-09-02T10:00:00.000Z","modified":"2026-09-02T10:00:00.000Z","pattern_type":"stix"},
 {"type":"threat-actor","id":"threat-actor--0f9c3a5e-6b1d-4c39-9a8e-2b9f6a7d1c11",
  "created":"2026-09-03T10:00:00.000Z","modified":"2026-09-03T10:00:00.000Z","name":"SYNTH-CARRION"}
]""")
COMMON = ["type", "spec_version", "id", "created", "modified"]
EXTRA = {"indicator": ["pattern", "pattern_type", "valid_from"], "threat-actor": ["name"]}
for o in objs:
    miss = [k for k in COMMON + EXTRA.get(o["type"], []) if k not in o]
    bad_id = not re.fullmatch(o["type"] + r"--[0-9a-f-]{36}", o.get("id", ""))
    probs = miss + (["id format"] if bad_id else [])
    print(o.get("id"), "OK" if not probs else "PROBLEMS: " + ", ".join(probs))
```

Run with `python3 lab_stix.py`. Verified output:

```text
indicator--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f OK
indicator-123 PROBLEMS: pattern, valid_from, id format
threat-actor--0f9c3a5e-6b1d-4c39-9a8e-2b9f6a7d1c11 PROBLEMS: spec_version
```

### 6.2 What the check shows

The first indicator passes. The second lacks `pattern` and `valid_from` and has an identifier that is not `type--UUID`. The threat-actor object lacks `spec_version`, which STIX 2.1 requires on domain objects. Only valid objects contribute `t_pub` values.

Each failure has a different consequence. Without `valid_from`, the indicator has no trustworthy publication time, so it cannot contribute to time-to-block. A malformed identifier breaks links between objects. A missing `spec_version` suggests the publishing tool predates STIX 2.1 or is misconfigured, which is useful feedback for that member class.

### Lab 3 — time-to-block medians

```python
"""Lab 2 (ch 06): median time-to-block (hours) for synthetic sharing-community members vs non-members."""
from statistics import median
members = [2.0, 3.5, 1.0, 6.0, 2.5, 4.0, 3.0]
non_members = [9.0, 14.0, 5.0, 22.0, 11.0, 8.0]
mm, mn = median(members), median(non_members)
print(f"members n={len(members)} median={mm:.1f}h")
print(f"non-members n={len(non_members)} median={mn:.1f}h")
print(f"difference={mn - mm:.1f}h ratio={mn / mm:.2f}")
```

Run with `python3 lab_ttb.py`. Verified output:

```text
members n=7 median=3.0h
non-members n=6 median=10.0h
difference=7.0h ratio=3.33
```

### 6.3 Reading the medians

Timing data are skewed — a few slow cases dominate means — so medians are reported. Members' median is 3.0 hours, non-members' 10.0 hours: a difference of 7.0 hours, ratio 3.33. With samples of seven and six, uncertainty is wide; a bootstrap interval or a rank-based test would be reported beside the medians.

Lucía's write-up puts the 3.0- and 10.0-hour medians next to their interval, not alone in a sentence. With six non-members, one unusually slow port can move the median by hours, so the interval tells members how much weight the difference can bear.

### 6.4 Description versus cause

The result describes faster blocking among members in this sample. Given the confounders discussed in Chapter 3, Lucía writes "is associated with" rather than "causes", unless the before-and-after stratum shows a consistent change on joining.

The four ports that joined CPSG in 2025 are the stratum that could support a stronger claim. If each blocked faster after joining than before, under the same staff and tools, the association becomes harder to explain by size or budget, though still not proof of cause.

### 6.5 Reporting data quality back

The validation counts are themselves a contribution. Lucía sends CPSG a short data-quality note listing how many objects lacked required properties, grouped by publishing member class, so producers can fix their exports. The note follows the same aggregation rule as the dissertation.

With 94% of indicators valid in the full export, the note can tell producers that one object in roughly seventeen could not contribute a publication time. Grouping by member class, not by member, keeps the note within the board's aggregation rule.

### Worked example

Lucía reports: 3 objects checked, 1 valid in the demonstration batch; across the real study export (synthetic), 94% of indicators were valid. Median time-to-block 3.0 h for members versus 10.0 h for matched non-members, with small samples flagged.

> **Synthetic case.** All objects, timings and percentages are invented.

### Errors and limits

Repairing malformed data by guessing creates fiction. Reporting a ratio without sample sizes misleads readers.

### Exercises

- **EX036 — Invalid object.** Which problems does the lab report for `indicator-123`? *Rubric:* 3 = pattern, valid_from, id format; 2 = two; 1 = one; 0 = none.
- **EX037 — Actor problem.** Why does the threat-actor object fail? *Rubric:* 3 = missing spec_version, required in STIX 2.1; 2 = missing field; 1 = name missing; 0 = none.
- **EX038 — Median choice.** Why report medians rather than means for time-to-block? *Rubric:* 3 = skewed data; outliers distort mean; 2 = vague; 1 = means better; 0 = none.
- **EX039 — Median quote.** Quote both medians and the ratio from the lab. *Rubric:* 3 = 3.0 h, 10.0 h, 3.33; 2 = two; 1 = one; 0 = none.
- **EX040 — Causal wording.** Rewrite "CPSG membership cuts blocking time by 70%" with appropriate wording. *Rubric:* 3 = association + sample size/uncertainty caveat; 2 = association only; 1 = unchanged; 0 = none.
- **EX041 — Uncertainty tool.** Name one method to express uncertainty around a difference in medians. *Rubric:* 3 = bootstrap CI or rank-based test (Mann–Whitney) correctly described; 2 = name only; 1 = t-test on means without caveat; 0 = none.
- **EX042 — Repair temptation.** Should Lucía invent a `valid_from` equal to `created` for the broken indicator? *Rubric:* 3 = no; exclude and report data-quality issue; 2 = no; 1 = yes; 0 = none.

### Synthesis

Validate before counting, prefer medians for skewed times, show sample sizes and uncertainty, and say "associated with" until design supports more.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure a dissertation around research questions; (2) write a limitations section that strengthens rather than apologises; (3) present results to two audiences — examiners and practitioners; (4) handle restricted data in the written product.

### 7.1 Structure follows questions

Introduction states the question and why ports care. Literature shows what is known and the gap. Methods describe design, data dictionary, ethics and validation. Results answer each aim in order. Discussion interprets, compares with literature, and states implications. Conclusion is short. Each results subsection should open with the aim it answers.

Lucía's results chapter has three subsections, one per aim: median time-to-block for members, comparison with matched non-members, and the share of indicators blocked, monitored or ignored. Her discussion then takes up the automation judgment, labelled as such.

### 7.2 Strong limitations

A strong limitation names the problem, its likely direction of bias, and what was done about it. "Small sample" alone is weak. "With seven members and six non-members, the median difference is imprecise; the bootstrap interval is wide and crosses small effects, so practical significance is uncertain" is strong.

Lucía's day-level stratum gets the same treatment: members with ticket dates only have timings rounded to whole days, which probably overstates their time-to-block; analysing them separately prevents that error from widening the gap between members and non-members.

### 7.3 Two audiences

Examiners want method and argument. CPSG members want a one-page brief: what the median gap was, what it suggests for staffing and automation, and what it does not show. The brief carries the same caveats in plainer language.

Lucía's brief to the CPSG board says the member median was 3.0 hours against 10.0 for matched non-members, that two members with automated TAXII-to-firewall pipelines accounted for the fastest blocks, and that small samples and self-reported automation limit both points. It does not tell members to buy automation; it suggests what to measure next.

### 7.4 Restricted data in writing

The dissertation is likely to be public through the university library, so it is written as TLP:CLEAR. No member names, no indicator values from the AMBER collection, no quotations from member bulletins. Synthetic examples illustrate formats.

The leak review caught the one place this failed: a figure caption named a port's city, which would identify the member. Lucía replaced it with "Member C", logged the change and notified the board. Synthetic STIX examples illustrate the format in the methods chapter without carrying any real indicator values.

### 7.5 Judgment language

When interpreting, separate observation ("members blocked faster in this sample") from judgment ("automation of TAXII ingestion likely explains part of the gap"), as ICD 203 recommends for analytic products. Label the judgment's confidence and basis.

Lucía's discussion labels her automation explanation as a judgment with moderate confidence, because automation status was self-reported by members, and proposes a follow-up study that measures it directly from pipeline logs. The observation sentence carries the 3.0- and 10.0-hour medians and their interval; the judgment sentence carries its confidence and the self-reported basis. A reader who rejects the judgment still has the observation intact.

### Worked example

Lucía's discussion argues that two members with automated TAXII-to-firewall pipelines account for the fastest blocks. She labels this a judgment with moderate confidence, notes that automation status was self-reported, and suggests a follow-up study that measures it directly.

> **Synthetic case.** Automation details and members are invented.

### Errors and limits

Hiding limitations to look stronger invites examiner attack. Practitioner briefs that drop caveats can cause poor investment decisions.

### Exercises

- **EX043 — Opening line.** How should each results subsection open? *Rubric:* 3 = by naming the aim/question it answers; 2 = with data; 1 = with literature; 0 = none.
- **EX044 — Weak to strong.** Upgrade the limitation "data were limited" into a strong limitation. *Rubric:* 3 = specific problem + bias direction + mitigation; 2 = two parts; 1 = unchanged; 0 = none.
- **EX045 — Brief contents.** List three items for the one-page practitioner brief. *Rubric:* 3 = finding, implication, what it does not show (caveats); 2 = two; 1 = full method; 0 = none.
- **EX046 — TLP of thesis.** What TLP level should the dissertation text assume, and one consequence? *Rubric:* 3 = CLEAR; no AMBER indicator values/member names; 2 = CLEAR only; 1 = AMBER; 0 = none.
- **EX047 — Observation vs judgment.** Label "two members have automated pipelines and the fastest times" and "automation explains the gap". *Rubric:* 3 = first observation (self-reported), second judgment; 2 = one right; 1 = both facts; 0 = none.
- **EX048 — Self-report caveat.** Why must self-reported automation status be flagged? *Rubric:* 3 = unverified; may be inaccurate/biased; affects causal judgment; 2 = partial; 1 = no need; 0 = none.
- **EX049 — Follow-up design.** Propose how a follow-up could measure automation directly. *Rubric:* 3 = observable measure (pipeline logs, config review with consent); 2 = vague; 1 = survey again; 0 = none.

### Synthesis

Let questions shape the text, write limitations with direction and mitigation, brief practitioners honestly, and write as if TLP:CLEAR.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) commission an independent methods review before submission; (2) prepare for viva questions on design and ethics; (3) respond to review findings transparently; (4) plan dissemination back to the community that provided data.

### 8.1 Independent methods review

A colleague outside the project reruns the analysis from the archive using synthetic sample files and checks that every figure matches. A second reader checks that no restricted information leaked into text, tables or figure captions. Both reviews are documented.

In Lucía's case, the figure-checking colleague found that all medians reproduced exactly from the archive. The leak reviewer found one caption that named a port's city. Each finding and its correction went into the change log, so the examiners could see both reviews were real, not formal steps.

### 8.2 Likely viva questions

Why not a randomised design? How did you handle confounding? What did members consent to? What would change your conclusion? Why medians? Is the STIX validation rule set complete? Practise answers that cite the dissertation's own pages.

For Lucía, the confounding answer cites the matched comparison and the before-and-after stratum; the medians answer cites the skewed timing data; and "what would change your conclusion" cites evidence that the before-and-after stratum shows no drop on joining. Answers rooted in her own design are harder to dislodge.

### 8.3 Responding to findings

If the reviewer finds a figure that does not match, fix it, record the correction in a change log, and check whether any conclusion changes. Examiners respect a visible correction more than an invisible one discovered later.

Lucía's change log shows the pattern for a different finding, the caption that named a port's city: the change, its date and the board notification are all recorded. Had a median failed to reproduce, the same log would show the corrected value and whether the 7.0-hour gap still held.

### 8.4 Returning value

CPSG gave data; the community should get results first. Lucía presents the brief to the governance board before public defence, under the agreed aggregation rules. NIST SP 800-150 stresses that sharing relationships rely on trust and reciprocity; research that extracts without returning erodes both.

The brief also carries the data-quality note, which members can act on immediately: by fixing exports that lack `valid_from` or `spec_version`, producers make the next study, and their own consumers' automation, more reliable. The 3.0- and 10.0-hour medians reached the CPSG board before the examiners saw them, which keeps the reciprocity NIST SP 800-150 describes.

### 8.5 After the defence

Delete raw timings as agreed, archive code and synthetic samples, and record the deletion. If publishing a paper, recheck that the published version still meets the board's conditions.

For Lucía, the deletion record is the last item the board receives: which files were deleted, when, and by whom. Any paper drafted later from the dissertation is rechecked against the three board conditions before submission. Archived code and synthetic samples stay available, so the study can still be rerun after the raw timings are gone. The deletion does not weaken reproducibility, because the archive was designed around synthetic files from the start.

### Worked example

The leak reviewer finds that one figure caption names a port's city, which would identify the member. Lucía replaces it with "Member C", logs the change, and notifies the board. The figure-checking colleague finds all medians reproduce exactly.

> **Synthetic case.** The review findings and board notification are invented.

### Errors and limits

A friend who helped with analysis is not independent. Presenting to the community after publication may breach the agreement.

### Exercises

- **EX050 — Two reviews.** What do the two independent reviewers each check? *Rubric:* 3 = reproducibility of figures + leakage of restricted info; 2 = one; 1 = grammar; 0 = none.
- **EX051 — Randomisation answer.** Draft a one-sentence viva answer to "why not randomise?" *Rubric:* 3 = cannot assign membership ethically/practically; used before-after and matching; 2 = partial; 1 = unaware; 0 = none.
- **EX052 — Caption leak.** Why does naming a port's city break the agreement? *Rubric:* 3 = identifies member despite aggregation rule; 2 = privacy vaguely; 1 = harmless; 0 = none.
- **EX053 — Correction log.** What does a correction-log entry contain? *Rubric:* 3 = what changed, why, date, effect on conclusions; 2 = two; 1 = none; 0 = none.
- **EX054 — Community first.** Why present to the board before public defence? *Rubric:* 3 = reciprocity/trust; agreement; chance to check aggregation; 2 = courtesy; 1 = unnecessary; 0 = none.
- **EX055 — Deletion proof.** After marking, what must Lucía do with raw timings? *Rubric:* 3 = delete as agreed and record deletion; 2 = delete; 1 = keep; 0 = none.
- **EX056 — Paper recheck.** What must be rechecked before turning the dissertation into a paper? *Rubric:* 3 = board conditions (aggregation, no names) still met in new text/figures; 2 = vague; 1 = nothing; 0 = none.

### Synthesis

Get independent eyes on numbers and leaks, rehearse design and ethics answers, correct in the open, and give results back to the people who shared.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX056. Coastline Ports Sharing Group, Lucía Ferraz, Prof. Daniel Okafor and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Population: port operators. Intervention: receiving indicators through CPSG's TAXII 2.1 collection. Comparison: similar operators outside CPSG. Outcome: time from indicator publication to a block rule.

**EX002.** Include: empirical studies measuring an outcome of threat-information sharing. Exclude: vendor marketing pages without described method or data.

**EX003.** Standards and guidance strand: SP 800-150 explains how to set up and run sharing, but it does not measure the outcome Lucía studies.

**EX004.** Example: "2026-02-03 | Library A | "threat intelligence sharing" AND (effectiveness OR evaluation OR measurement), 2011–2026 | 412 hits | 112 abstracts screened | 19 included | excluded: off-topic, no method, duplicates."

**EX005.** 32 (412 − 300 − 80).

**EX006.** Only 3 of the 19 included works measure an outcome; most describe processes, so measured effectiveness is the thin area.

**EX007.** Rules set after reading results can be bent to keep agreeable sources and drop inconvenient ones; fixed rules make the review repeatable and unbiased.

**EX008.** Direction and feedback: SOCs rarely receive written requirements, and consumers seldom report whether intelligence helped, so the cycle runs open-loop.

**EX009.** Strategic — a sector trend aimed at executives and planners rather than at analysts writing rules.

**EX010.** Adversaries change IP addresses cheaply, but changing behaviour such as their phishing technique costs more, so the T1566 mapping stays useful longer.

**EX011.** From the sender domain (infrastructure), find other events in the community data that used the same domain or registrant, revealing further victims or campaigns.

**EX012.** TLP:CLEAR, TLP:GREEN, TLP:AMBER, TLP:AMBER+STRICT, TLP:RED.

**EX013.** Visible lookups or contact can alert the subject, who may change infrastructure, destroy evidence or retaliate, and it can expose the investigator.

**EX014.** Delivery.

**EX015.** SOC staffing: larger ports both join communities more often and have more analysts to write block rules quickly.

**EX016.** Comparing a port with its own pre-membership period holds stable characteristics like size and budget constant, isolating the change around joining.

**EX017.** With at least three ports in each group, no reader can work backwards to one member's timings.

**EX018.** From non-member operators who volunteer and share their own logs under a written agreement — never by probing their systems.

**EX019.** Analyst usernames: the study needs timings, not people, so removing them minimises personal data processing.

**EX020.** That member's data is excluded entirely; the board's approval does not override an individual opt-out.

**EX021.** So anyone rerunning the analysis gets exactly the same resampled results.

**EX022.** H1 inconsistent=0, H2 inconsistent=2, H3 inconsistent=3.

**EX023.** E2, access from a contractor VPN account: it is consistent with all three hypotheses, so it cannot discriminate between them.

**EX024.** H1 is only the least contradicted among the hypotheses considered; the evidence set is small and an unlisted explanation could fit better.

**EX025.** Example: "likely" = 55–80%. Kent showed readers assign very different numbers to the same word, so a published range keeps meaning consistent.

**EX026.** Example: discovery that the contractor account was used from a staff workstation inside the port during the intrusion.

**EX027.** Example: an initial-access broker who sold the VPN access to the ransomware crew — distinct because two actors would be involved.

**EX028.** T1486.

**EX029.** `ttb_h`: hours from indicator publication (`t_pub`) to block-rule activation (`t_block`); float; unit hours; derived as (t_block − t_pub)/3600 s; missing if not blocked.

**EX030.** Whether members record block-rule activation time (`t_block`) with enough precision to compute hours.

**EX031.** Analyse that member in a separate day-level stratum and report the lower precision as a limitation.

**EX032.** Drift: it replaces the time-to-block construct with satisfaction, answering a different and easier question.

**EX033.** It records indicators members chose not to block, so the study does not look only at indicators that succeeded.

**EX034.** The indicator's `created` timestamp, supported by `valid_from`.

**EX035.** No. Pilot data test feasibility; they belong in the methods chapter, not in results.

**EX036.** `PROBLEMS: pattern, valid_from, id format`.

**EX037.** It lacks `spec_version`, which STIX 2.1 requires on every domain object.

**EX038.** A few very slow blocks skew the distribution; the median reflects the typical case without being dragged by outliers.

**EX039.** Members median 3.0 h, non-members median 10.0 h, ratio 3.33.

**EX040.** Example: "In this small sample (7 members, 6 non-members), membership was associated with a lower median time-to-block (3.0 h vs 10.0 h); causation is not established."

**EX041.** A bootstrap confidence interval for the difference in medians, resampling each group with replacement many times; or a Mann–Whitney rank test.

**EX042.** No. Exclude the object from timing analysis and report it as a data-quality finding; inventing values fabricates data.

**EX043.** By stating which aim or research question it answers.

**EX044.** Example: "Only members with second-level logs could contribute hour-level timings, likely over-representing better-resourced ports and biasing member medians downward; a day-level stratum was analysed separately."

**EX045.** The median gap found, the implication for staffing or automation, and what the study does not show (no causal proof, small sample).

**EX046.** TLP:CLEAR, so no AMBER indicator values, member names or bulletin quotations may appear.

**EX047.** The first is an observation (based on self-report); the second is an analytic judgment.

**EX048.** Members' descriptions of their own automation were not verified and may be inaccurate, which weakens any judgment that automation explains the gap.

**EX049.** With member consent, review pipeline logs or configurations to record whether TAXII ingestion creates block rules without human steps, and timestamp each stage.

**EX050.** One reruns the analysis to confirm every figure reproduces; the other checks text, tables and captions for leaked restricted information.

**EX051.** "Membership cannot be randomly assigned to port operators, so I used a before-and-after comparison for joining members plus matched volunteer non-members to reduce confounding."

**EX052.** A city can identify a single member port, defeating the aggregation rule the board imposed.

**EX053.** What changed, why, the date, and whether any conclusion moved as a result.

**EX054.** CPSG shared data on trust; presenting first honours reciprocity and lets the board confirm aggregation rules were met before anything is public.

**EX055.** Delete the raw timings as the agreement requires and keep a dated record of the deletion.

**EX056.** That every new sentence, table and figure still meets the board's conditions — aggregation to three or more and no member names or locations.

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
