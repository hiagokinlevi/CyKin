# Incident Response and Cyber Resilience: Applied Research Design and the Master's Dissertation

- Language: English (`en`); master's course, two years; approximately 1,200 hours of planned study (course 177 of 207 in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **draft**. Chapters 1–8 of 8 have authored teaching text, exercises EX001–EX050 and matching worked results. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: beginning researchers who know incident response from practice or earlier study and now need to answer one bounded empirical question about how response work is done, measured or improved, with evidence another person could check. Entry knowledge: the practitioner content of the [rapid](../../../../rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md), [professional](../../../../professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md) or [technical](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md) books (or equivalent experience as an analyst, responder or coordinator), introductory statistics (proportions, means, variance, confidence intervals) and the ability to run a short Python script.
- Relation to the other books in this area: the practitioner books teach how to *do* incident response — preserve evidence, discriminate hypotheses, contain, recover and communicate. The [doctoral book](../../../../doctorate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) asks a researcher to make and defend an *original* contribution (its Handoff Study proposes a new mechanism, replicates a baseline, validates across contexts and submits claims to adversarial critique). This master's book sits between them. It asks you to **design, pilot and execute one ethically reviewed applied study well**: choose a question that can come out either way, pick a design that fits the data you can actually obtain, rule out the explanations that compete with your favoured one, report exactly what the study shows and does not show, and defend it before examiners. Novelty is welcome but not required; competence, reproducibility and honesty about limits are.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights and are not relicensed here.
- Educational boundary: this course is an independent educational blueprint. It is not an accredited master's programme, grants no degree and grants no authority to access, collect or study any real incident record, security operations centre, analyst or organization. Every organization, team, person, case vignette, ticket, dataset and numerical result in a worked example is **synthetic** unless a sentence explicitly cites a public source. Nothing here is an operational triage policy for a real organization.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

Read the eight chapters in order; together they follow one master's dissertation from first idea to examination. Chapter 1 turns a topic into an answerable question, defines exactly what number the study will estimate, and builds a documented, testable literature search. Chapter 2 is the advanced research seminar: it compares the competing models of what makes incident response "effective", shows how the choice of success measure can reverse a conclusion, and trains you to say what each model leaves unexplained. Chapter 3 chooses a design, plans its size by simulation, writes the ethics protocol and sets up a reproducible project before any data exist. Chapter 4 lists the explanations other than your intervention that could produce the same data, and builds analyses designed to embarrass the favoured claim. Chapter 5 writes the proposal and runs a pilot whose job is to test feasibility and measurement, not to find an effect. Chapter 6 collects and analyses the main-study data with traceable transformations, qualified estimates and alternative outcome definitions. Chapter 7 writes the dissertation, separates results from interpretation and states limitations with their direction. Chapter 8 prepares for independent examination: a reader who reproduces your numbers, attacks your choices and asks what would have happened had you chosen differently.

Every chapter contains teaching sections, definitions, a worked example, a practical activity with an offline Python lab, a list of common errors and limits, numbered exercises and a synthesis. Labs use the Python 3 standard library only; no network access, packages or real data are needed. Labs 6, 7 and 8 import the main-study generator printed in Chapter 6, saved as `lab6_data.py`, and Labs 7 and 8 also import the Chapter 6 analysis saved as `lab6_analysis.py`. Write your answer to each exercise before opening the [worked results](#worked-results). Many exercises have more than one defensible answer; the worked result shows one, and the rubric shows what an examiner would reward.

Keep four labels in every research note you write while studying: **observation** (what a named source or instrument recorded), **inference** (what you conclude, under which assumptions), **claim** (what you intend to defend, with its scope) and **decision** (what someone chose to do because of it). Incident-response research adds a fifth that practitioners already know: **exposure** — who or what was harmed or put at risk by the decision you are studying. The commonest error at master's level is not a wrong calculation; it is a correct calculation attached to a claim larger than the design can carry.

### What "applied research" means at this level

A master's dissertation in incident response is usually judged on four things: whether the question is clear and worth answering; whether the design fits the question and the data actually obtainable; whether the analysis was carried out competently and reproducibly; and whether the conclusions stay inside the evidence. Legitimate master's contributions include a careful controlled study of a practice that organizations adopt on faith (a triage rubric, a playbook format, a handover template), a well-executed replication of a published design with a new population, a measurement study showing that a widely used metric does not measure what people think it does, or a mixed-methods study explaining *why* an observed effect occurred. What is not acceptable is a dissertation whose numbers cannot be traced, whose data were obtained without approval, whose outcome measure was chosen after looking at the results, or whose limitations section lists weaknesses without saying which way they bias the answer.

Incident response adds three difficulties that the book returns to repeatedly. First, the events of interest are **rare, heterogeneous and not assigned by anyone**: you cannot schedule a ransomware outbreak to test a playbook, and the incidents you do observe differ in ways that matter. Second, **the records are produced by the process being studied**: a ticket's severity field, timestamps and closure code are themselves analyst decisions, so an outcome measured from tickets can move because recording practice changed rather than because response improved. Third, **access is constrained by confidentiality and by the people involved**: analysts are employees whose performance data could be used against them, and incident records contain other people's personal data and security weaknesses. Good master's designs work with these constraints rather than pretending they do not exist — for example, by studying decisions on realistic fictional cases with consenting volunteers, and by using historical operational data only for questions it can genuinely answer.

### The synthetic dissertation used in this book

The book follows one invented master's project, the **Triage Rubric Study**. Its question, refined in Chapter 1, is: *does a structured, impact-led severity rubric reduce the under-triage of high-impact incidents by security analysts, compared with their usual judgement, and at what cost in decision time and over-triage?* Under-triage — rating an incident less severe than it is — matters because severity drives escalation, staffing and notification clocks; an under-triaged incident is one that waits. The question echoes a real concern in the published literature on security operations, where analysts describe overwhelming alert volumes and false positives ([Alahmadi, Axon and Martinovic 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi)) and field studies describe how tacit, team-specific SOC practice is ([Sundaramurthy et al. 2014](https://doi.org/10.1145/2663887.2663904); [Kokulu et al. 2019](https://doi.org/10.1145/3319535.3354239)). It also echoes the wider checklist literature: a structured checklist was associated with lower surgical complications in a multi-country before-and-after study ([Haynes et al. 2009](https://doi.org/10.1056/NEJMsa0810119)), a design whose limits Chapter 4 uses as a teaching case. But every place, team, person, case and number in the Triage Rubric Study is fictional.

| Synthetic element | Role in the book | Boundary |
|---|---|---|
| **Marlow Regional Shared Services (MRSS)** — a fictional shared security operations service for local councils, schools and a water authority, with two analyst teams, **East** and **West** | Source of the historical-ticket question in Chapters 1 and 4: East adopted the rubric and, in the same month, gained senior staff. | Invented organization; no real employer, staff or tickets. |
| **SEV-4 rubric** | The intervention: a one-page, impact-led severity rubric that asks four questions about affected services, data, spread and time-criticality before an analyst assigns severity 1 (low) to 4 (critical). | Invented instrument; not a published standard. |
| **Case vignettes C01–C24** (sets A and B) and pilot cases C1–C6 | Fictional incident cases, each with a reference severity set by a fictional three-person expert panel; some are "quiet-impact" cases with little alert noise but high business impact. | Teaching fixtures written for the book. |
| **Volunteer analysts P01–P10 (pilot) and A01–A24 (main study)**, observers O1 and O2, debrief interviewees | Participants in the synthetic tabletop study. | Invented people; their "data" are generated by the labs. |
| Records with DOIs beginning `10.9999/syn` | Fictional search results used in Lab 1. | `10.9999` is not a registered publisher prefix; these records do not exist. |

All numbers produced in this book's labs come from synthetic generators printed in the text. They demonstrate a method; they are not findings about rubrics, analysts or organizations.

### Source policy

Every factual statement about a standard, a regulation or a published study links to the source the author consulted, with its identifier. Where a widely taught methods concept is used without a specific source — for example, that a crossover design removes stable between-person differences from a comparison — the text says it is a standard methods concept rather than inventing a reference. Dated sources are labelled as dated: [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) on exercise design (2006) is still useful for tabletop structure, but it predates current practice and is used here only for design vocabulary. A source supports the general claim beside it, never the synthetic case details.

## Contents

1. [Research question and literature method](#ch-01) — from topic to answerable question, the estimand, claim scope, documented searching across security, human-factors and safety literatures, known-item tests, deduplication, dual screening and the concept matrix.
2. [Advanced incident response research seminar](#ch-02) — competing models of response effectiveness, what each success measure rewards, how censoring and case mix bend metrics, evidence quality, and leading a critical seminar.
3. [Study design, ethics and reproducibility](#ch-03) — choosing among observational, quasi-experimental and controlled tabletop designs, crossover logic, design analysis by simulation, ethics with employee participants, predeclared measures and a reproducible project.
4. [Competing explanations of response outcomes](#ch-04) — multiple working hypotheses, confounding by staffing and case mix, causal diagrams, difference-in-differences, standardization, negative controls and sensitivity.
5. [Proposal and pilot of a bounded incident study](#ch-05) — the proposal as a contract, timeline and risk register, a feasibility pilot with predeclared progression criteria, protocol deviations, instrument revision and stop rules.
6. [Reproducible collection and outcome analysis](#ch-06) — data dictionary, cleaning log, the paired crossover analysis with bootstrap and permutation inference, agreement with a reference standard, debrief interviews and robustness to alternative outcome definitions.
7. [Dissertation on response effectiveness and limits](#ch-07) — structure and argument, the results-to-claims register, calibrated language, number provenance, reporting guidelines, directional limitations and negative results.
8. [Independent research review and defense](#ch-08) — how examiners read, reproduction by an independent reader, specification curves, counterexamples, the oral defense, corrections and responsible sharing.

The [worked results](#worked-results) contain EX001–EX050. A [glossary](#glossary) and [references](#references) close the book.

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes and connection

After this chapter you should be able to:

1. Distinguish a topic, a problem and a research question, and narrow one into the next with a reason for each step.
2. Write an incident-response question in a structured form (population, exposure, comparison, outcome, time) and test it against feasibility and interest criteria.
3. Classify a question as descriptive, associational, causal or explanatory, and state the strongest claim each type can support.
4. Define an **estimand** — the exact quantity the study will produce — before any data are seen.
5. Design a documented search across security, human-factors and safety literatures, test it with known items, deduplicate the results, screen them with a second reviewer and measure agreement.
6. Synthesize prior work by concept rather than by author, and locate the gap your study will address.

The chapter builds on the entry knowledge — you know what triage, severity, escalation and containment mean in practice — and prepares Chapter 2, where the studies you find are read critically against one another.

### 1.1 From topic to problem to question

#### 1.1.1 Three different things

A **topic** is an area of interest: "SOC triage", "playbooks", "ransomware recovery". A **problem** is a situation in which someone must decide or act without knowing enough: "MRSS managers must decide whether to make the SEV-4 rubric mandatory for both teams, but they do not know whether it reduces missed high-impact incidents or merely slows analysts down." A **research question** is a precisely worded request for information that, if answered, would reduce that uncertainty, and whose answer could come out either way: "Among MRSS-like analysts triaging realistic incident cases, does using the SEV-4 rubric reduce the proportion of high-impact cases rated below their reference severity, compared with usual judgement?"

Each narrowing step should be defensible. Moving from "triage" to "severity assignment" is justified because severity drives escalation and notification clocks. Moving from "all severity errors" to "under-triage of high-impact cases" is justified because the consequences are asymmetric: an over-triaged low-impact case wastes effort, an under-triaged critical case waits. Write down each step and its reason; examiners ask about them, and the reasons become your dissertation's motivation section.

#### 1.1.2 A structured form and two tests

Clinical researchers use the PICOT pattern (population, intervention, comparison, outcome, time). It transfers well to incident response once "intervention" is generalized to **exposure** — anything whose effect you want to know, whether or not someone assigned it:

| Element | Triage Rubric Study (synthetic) | Common mistake |
|---|---|---|
| **P**opulation and unit | Security analysts with at least six months of triage experience; the unit of analysis is an analyst's severity decision on one case. | Leaving the unit implicit, so that decisions, analysts and teams are mixed in one analysis. |
| **E**xposure | Using the SEV-4 rubric while triaging. | Bundling the rubric with training, new staff or new tooling so the exposure cannot be isolated. |
| **C**omparison | The same analysts' usual judgement on comparable cases. | No comparison ("after adopting the rubric, 9% of incidents were under-triaged" — compared with what?). |
| **O**utcome | Under-triage: a rating below the reference severity, among cases whose reference severity is 3 or 4. | An outcome produced by the exposure's own paperwork, or one chosen after seeing results. |
| **T**ime | One decision per case within a timed tabletop session. | No time frame for when the outcome is observed. |

Two tests then check whether the question is worth pursuing. The **FINER** criteria — feasible, interesting, novel, ethical, relevant — are a standard teaching device from clinical research design; treat them as prompts, not a scoring system. *Feasible* is the one master's students most often fail: a question about real incidents at real organizations may need data you will never be given. *Ethical* comes next: studying analysts' errors on live incidents creates risks to their employment. The Triage Rubric Study passes both by using fictional cases with consenting volunteers, at the price of realism, which Chapter 3 treats as a validity threat to be managed rather than hidden.

#### 1.1.3 Question types and the claims they permit

| Type | Example (incident response) | Minimum design | Strongest claim |
|---|---|---|---|
| Descriptive | "How often were high-impact MRSS tickets rated below their later panel severity in 2025?" | A well-defined sample and measurement | "In this population and period, the proportion was…" |
| Associational | "Are tickets triaged by senior analysts less often under-triaged?" | Comparison of groups, with confounders recorded | "Seniority was associated with…, after adjusting for…" |
| Causal | "Does the rubric reduce under-triage compared with usual judgement?" | A design with a credible counterfactual: randomization, a crossover, or a quasi-experiment with tested assumptions | "Using the rubric reduced…, under these conditions" |
| Explanatory (mechanism) | "Why do analysts under-triage quiet-impact incidents?" | Qualitative or mixed methods: think-aloud, interviews, process tracing | "Analysts described…; this account is consistent with…" |

The type of question fixes the type of claim. A descriptive study of tickets cannot say that the rubric *caused* anything, however large the sample. A causal tabletop study cannot say *how often* under-triage happens in live operations, because its cases were deliberately chosen. Mixing these up — writing a causal conclusion on a descriptive design, or a prevalence conclusion on an enriched case set — is the most common reason examiners ask for major corrections.

### 1.2 The estimand: say exactly what number you will produce

An **estimand** is the quantity a study aims to estimate, defined before data are seen. It is not the method (the **estimator**) or the number you get (the **estimate**). A useful template has five parts:

1. **Population** — whose decisions: analysts with at least six months of triage experience, of the kind MRSS employs.
2. **Conditions compared** — rubric versus usual judgement, each applied by the same analyst.
3. **Outcome variable** — under-triage (0/1) for each decision on a high-impact case.
4. **Summary measure** — the mean, across analysts, of each analyst's under-triage proportion with the rubric minus their proportion without it (a risk difference, in percentage points).
5. **Handling of intercurrent events** — what happens when an analyst withdraws, skips a case, or uses the rubric in a "usual" session. The Triage Rubric Study analyses analysts with both periods and reports how many withdrew; a sensitivity analysis keeps their available data.

Writing the estimand first protects you from two temptations. The first is choosing among summaries after seeing the data — the pooled proportion, the per-analyst mean, the odds ratio, the critical-only rate — and reporting the most impressive one. The second is quietly changing the population, for example by excluding "outliers" who did badly with the rubric. Chapter 3 turns the estimand into a predeclared analysis plan; Chapter 6 computes it; Chapter 8 asks what happens under the alternatives.

#### 1.2.1 Claim scope

Every estimand implies a **claim scope**: the population, conditions and setting to which the result applies. The Triage Rubric Study's result applies to volunteer analysts deciding on fictional cases in a timed session with a printed rubric. It does not directly apply to live triage under alert floods, to analysts without six months' experience, or to an automated triage tool. Write the scope next to the question from the start; the limitations section of Chapter 7 is then a discussion of how far you can reasonably extrapolate, not a list of afterthoughts.

### 1.3 What a literature review is for

A dissertation's review has three jobs: to show what is already known about your question, to show how others have measured the same things (so you can reuse validated measures or justify new ones), and to locate a gap. It is not an annotated bibliography, and at master's level it is rarely a full systematic review.

Choose the review type deliberately and say which you chose:

- A **narrative review** summarizes literature selected by expertise. It is fast but unreproducible; acceptable for background, not for the claim that "no study has tested X".
- A **scoping review** maps what kinds of evidence exist on a broad question, with a documented search and screening, but usually without appraising quality in depth.
- A **systematic review** answers a focused question with an exhaustive, reproducible search, explicit eligibility criteria, dual screening, quality appraisal and often a quantitative synthesis; its reporting is guided by [PRISMA 2020](https://doi.org/10.1136/bmj.n71).

For the Triage Rubric Study the defensible choice is a **scoping review with systematic elements**: a documented search, explicit criteria, a second reviewer on a sample, and a flow diagram in the PRISMA style — but no claim of exhaustiveness. The gap statement must match that choice: "In the sources searched, we found no controlled study of structured severity rubrics for security analysts" is supportable; "no such study exists" is not.

### 1.4 Searching across disciplines

#### 1.4.1 Why incident-response literature is scattered

Research about how people respond to incidents is spread across computer security venues (where SOC field studies appear), human-factors and cognitive-engineering journals (decision making under time pressure, situation awareness), safety science and medicine (checklists, triage, handover), management and organization studies (crisis coordination), and grey literature: national CSIRT annual reports, government guidance, after-action reviews and vendor reports. Each community has its own vocabulary. Clinicians speak of "under-triage" and "decision aids"; security researchers of "alert prioritization" and "analyst fatigue"; human-factors researchers of "cue utilization". A search in one community's database misses the others.

Two theoretical traditions are worth knowing by name because they predict different things about a rubric. Situation-awareness theory ([Endsley 1995](https://doi.org/10.1518/001872095779049543)) treats good decisions as depending on perceiving the right elements, understanding them and projecting their future state; a rubric that forces attention to impact elements should help. Naturalistic decision-making research ([Klein 2008](https://doi.org/10.1518/001872008X288385)) describes experts recognizing situations from patterns rather than comparing options; on that account a rubric may help novices but slow or even hinder experts. Chapter 2 develops these as competing models.

#### 1.4.2 Concept blocks

Build the search from **concept blocks**, each an OR-list of synonyms, combined with AND:

- Block 1 (setting): "security operations center" OR SOC OR CSIRT OR "incident response team" OR "security analyst*".
- Block 2 (decision): triage OR prioriti* OR severity OR escalat* OR classif*.
- Block 3 (exposure): rubric OR checklist OR "decision aid" OR "decision support" OR scale OR protocol OR playbook.
- Optional Block 4 (cross-domain transfer, searched separately): (triage OR "time pressure") AND (checklist OR "decision aid") in medicine and human factors, to find designs and measures worth borrowing.

Record each database's exact syntax, field restrictions and date of search. A search that cannot be re-run is not documented.

#### 1.4.3 Sources and the known-item test

Choose at least three bibliographic sources from different disciplines (for example, the ACM Digital Library and IEEE Xplore for security venues, a multidisciplinary index for human factors and safety, and a psychology index), plus a grey-literature plan with named source types: national CSIRT and agency reports, standards bodies (such as [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), April 2025, which frames incident response within cybersecurity risk management), professional associations such as FIRST (whose [CSIRT Services Framework](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) defines service vocabulary), and conference talks with published slides.

Before running the full search, define a **known-item set**: three to five studies you already know are relevant, found by other means (a supervisor's recommendation, a citation in a key paper). After the search, check how many it retrieved. **Known-item recall** is a rough test of sensitivity: if your search misses a study you know is relevant, it is probably missing others like it, and you must find out why (a missing synonym, a field restriction, a database not indexed) before trusting the rest.

#### 1.4.4 Citation chaining and stopping

Backward chaining (reading the reference lists of included studies) and forward chaining (finding later studies that cite them) are essential in a scattered field. Predeclare a **stopping rule**: for example, stop when two consecutive rounds of chaining add no new included study. Without a rule, chaining stops when you are tired, which is not reproducible.

### 1.5 From records to included studies

#### 1.5.1 Deduplication

The same study appears in several databases with slightly different titles, capitalization, punctuation or missing DOIs. Deduplicate in two passes: first on DOI where present, then on a normalized title plus year. Normalization must handle case, punctuation and symbols (an ampersand versus "and"); Lab 1 shows a simple version. Log how many duplicates each pass removed; the numbers feed the flow diagram.

#### 1.5.2 Two-stage screening and agreement

Screen titles and abstracts against written eligibility criteria, then read the full text of everything that survives. A second reviewer should screen at least a random sample independently. Raw agreement overstates consistency because two reviewers who both exclude most records will agree often by chance. **Cohen's kappa** ([Cohen 1960](https://doi.org/10.1177/001316446002000104)) corrects for this: κ = (p_o − p_e) / (1 − p_e), where p_o is observed agreement and p_e the agreement expected from the reviewers' marginal rates. Verbal benchmarks such as those of [Landis and Koch (1977)](https://doi.org/10.2307/2529310) ("moderate" for 0.41–0.60) are widely quoted but arbitrary; use kappa as a **diagnostic of unclear criteria**, not as a grade. The useful output of a screening-agreement exercise is the list of disagreements and the criterion revision they prompt.

#### 1.5.3 The flow diagram

Report records identified per source, duplicates removed, records screened, records excluded at each stage with reasons, and studies included. The PRISMA 2020 flow diagram is the standard template even for a scoping review. A reader should be able to reconcile every number.

### 1.6 Synthesis by concept, not by author

A weak review proceeds author by author: "Smith (2021) found… Jones (2022) found…". A strong review proceeds by concept, using a **concept matrix**: rows are studies, columns are the things your question is about.

| Study (synthetic records from Lab 1, except where cited) | Unit | Exposure | Comparison | Outcome measure | Design | Rivals raised or left open |
|---|---|---|---|---|---|---|
| Field study of SOC severity triage (10.9999/syn.001) | Ticket | None (descriptive) | — | Analyst-assigned severity vs later review | Ethnography + ticket audit | Recording practice changes over time |
| Checklist tabletop experiment (10.9999/syn.003) | Decision | Classification checklist | No checklist, between-subject | Accuracy vs answer key | Parallel randomized, students | Students are not analysts; answer key validity |
| Interrater reliability of severity scales (10.9999/syn.005) | Rating pair | Scale wording | Two scales | Weighted kappa between analysts | Agreement study | Agreement is not accuracy |
| [Haynes et al. 2009](https://doi.org/10.1056/NEJMsa0810119) (real) | Surgical patient | Safety checklist | Before vs after, eight hospitals | Complications, deaths | Pre–post, no concurrent control | Secular trends, Hawthorne effect, co-interventions |

Reading down the columns reveals the gap. In this synthetic map, nobody has compared a rubric with usual judgement *within the same experienced analysts*, with an outcome that separates under- from over-triage and a reference standard set independently of the participants. That is the Triage Rubric Study's niche, stated with the scope of the search behind it.

### 1.7 Reading a study for design, not only for findings

When you add a study to the matrix, record its design features before its result: how the unit was sampled, who assigned the exposure, what the comparison was, how the outcome was measured and by whom, and what happened to missing data. Two studies that "found the checklist works" may support very different claims: a randomized study of students with an answer key, and a before-and-after audit of tickets whose severity field was re-defined at the same time as the checklist was introduced. Chapter 2 makes this reading protocol explicit.

### 1.8 Worked example: from topic to the Triage Rubric question (synthetic)

*Starting point.* A master's student who worked as an MRSS analyst proposes the topic "making triage better". Her supervisor asks for the decision behind it. She describes the MRSS manager's dilemma: East adopted SEV-4 in January 2025 and its under-triage rate fell; West's analysts say the rubric is slow and "just box-ticking"; the manager wants to mandate it for both teams.

*First draft question.* "Does the SEV-4 rubric work?" — too vague: work at what, compared with what, for whom?

*Second draft.* "Did East's under-triage fall because of the rubric?" — a causal question about one historical event. It is interesting, but the student knows that East also gained senior analysts that month. With one team per condition and simultaneous changes, the historical data can describe and associate but will struggle to isolate the rubric. Chapter 4 analyses exactly this problem.

*Third draft (adopted).* Three linked questions:

- **RQ1 (causal, primary):** Among analysts with at least six months of triage experience, does using SEV-4 reduce the proportion of high-impact fictional cases rated below their reference severity, compared with the same analysts' usual judgement?
- **RQ2 (causal, secondary):** What does it cost — in median decision time and in over-triage of low-impact cases?
- **RQ3 (explanatory):** How do analysts describe their reasoning on cases where the rubric changed, or failed to change, their rating?

Plus a bounded **descriptive and associational strand** on MRSS historical tickets (Chapter 4), reported as context, not as the causal test.

*Estimand (RQ1).* The mean across analysts of the within-analyst difference (rubric minus usual) in the proportion of high-impact cases under-triaged, in percentage points, among analysts who complete both conditions; withdrawals reported and examined in a sensitivity analysis.

*Hoped-for claim and scope.* "For experienced analysts deciding on realistic fictional cases, the rubric reduced under-triage of high-impact cases by about X points (interval…), at a cost of Y seconds per decision." Out of scope: prevalence of under-triage in live operations; effects on novices; effects of automated tools; any statement about MRSS as a real organization.

### 1.9 Practical activity: deduplicate, test recall and measure screening agreement

Lab 1 takes a synthetic search export of fourteen records from four sources. It deduplicates in two passes, checks known-item recall against four studies the student expects to find, and computes raw agreement and Cohen's kappa for two reviewers' title-and-abstract decisions. Save it as `lab1_search.py` and run it with `python3 lab1_search.py`.

```python
# Lab 1 - known-item recall, deduplication and screening agreement for a triage-literature search (offline)
# Synthetic search export. Each record: (source, title, year, doi_or_empty). Nothing here is a real bibliography.
import re
RECORDS = [
    ("acm", "Severity Triage in a Security Operations Center: A Field Study", 2021, "10.9999/syn.001"),
    ("ieee", "Severity triage in a security operations center - a field study", 2021, "10.9999/syn.001"),
    ("acm", "Alert Fatigue and Analyst Escalation Decisions", 2022, "10.9999/syn.002"),
    ("scopus", "Alert fatigue and analyst escalation decisions", 2022, ""),
    ("ieee", "Checklists for Incident Classification: A Controlled Tabletop Experiment", 2023, "10.9999/syn.003"),
    ("scopus", "Mean Time to Respond as a SOC Performance Measure", 2020, "10.9999/syn.004"),
    ("grey", "Regional CSIRT annual report: incident categories and handling times", 2024, ""),
    ("grey", "Regional CSIRT Annual Report - Incident Categories and Handling Times", 2024, ""),
    ("acm", "Interrater reliability of incident severity scales", 2019, "10.9999/syn.005"),
    ("psyc", "Checklist use under time pressure in emergency triage", 2018, "10.9999/syn.006"),
    ("psyc", "Expertise and cue use in dynamic decision tasks", 2017, "10.9999/syn.007"),
    ("ieee", "Machine-learning alert prioritization benchmark", 2024, "10.9999/syn.008"),
    ("grey", "Vendor whitepaper: AI triage cuts MTTR by 90%", 2025, ""),
    ("scopus", "Under-triage of high-impact incidents in shared service SOCs", 2025, "10.9999/syn.009"),
]
KNOWN_ITEMS = {"10.9999/syn.003", "10.9999/syn.005", "10.9999/syn.009", "10.9999/syn.010"}

def norm(title):
    t = title.lower().replace("&", " and ")
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return " ".join(t.split())

def dedupe(records):
    seen_doi, seen_title, kept, removed = set(), set(), [], 0
    for src, title, year, doi in records:
        key_t = (norm(title), year)
        if (doi and doi in seen_doi) or key_t in seen_title:
            removed += 1
            continue
        if doi:
            seen_doi.add(doi)
        seen_title.add(key_t)
        kept.append((src, title, year, doi))
    return kept, removed

def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return po, (po - pe) / (1 - pe)

kept, removed = dedupe(RECORDS)
found = {r[3] for r in kept if r[3]}
print(f"records exported: {len(RECORDS)}  duplicates removed: {removed}  unique: {len(kept)}")
hit = sorted(KNOWN_ITEMS & found); miss = sorted(KNOWN_ITEMS - found)
print(f"known-item recall: {len(hit)}/{len(KNOWN_ITEMS)}  missing: {', '.join(miss) or 'none'}")
# Title/abstract decisions in the order of `kept` (I = include, X = exclude)
A = "IIIXIIIXXXI"
B = "IIIIXIXXXXI"
assert len(A) == len(B) == len(kept)
po, k = kappa(list(A), list(B))
print(f"raw agreement: {po:.3f}  Cohen's kappa: {k:.3f}")
for (src, title, year, doi), x, y in zip(kept, A, B):
    if x != y:
        print(f"  disagree: A={x} B={y}  [{src}] {title[:58]}")
inc = sum(1 for x, y in zip(A, B) if x == "I" and y == "I")
print(f"both include: {inc}  to adjudicate: {sum(x != y for x, y in zip(A, B))}  both exclude: {sum(x == y == 'X' for x, y in zip(A, B))}")
```

Expected output:

```text
records exported: 14  duplicates removed: 3  unique: 11
known-item recall: 3/4  missing: 10.9999/syn.010
raw agreement: 0.727  Cohen's kappa: 0.441
  disagree: A=X B=I  [scopus] Mean Time to Respond as a SOC Performance Measure
  disagree: A=I B=X  [grey] Regional CSIRT annual report: incident categories and hand
  disagree: A=I B=X  [psyc] Checklist use under time pressure in emergency triage
both include: 5  to adjudicate: 3  both exclude: 3
```

How to read it. Three duplicates were removed: one by DOI (the IEEE record of the field study), two by normalized title (the Scopus record of the alert-fatigue study, which lacked a DOI, and the second grey-literature CSIRT report). Known-item recall is three of four: `10.9999/syn.010` was not retrieved. In a real review that triggers a diagnosis — perhaps that study calls the exposure a "decision aid", which Block 3 must include, or it is indexed only in a database you did not search. Raw agreement of 0.727 sounds respectable; kappa of 0.441 shows that a good part of it is what two reviewers who exclude a lot would achieve by chance. The three disagreements point at three distinct criterion problems: whether a *measurement* paper (mean time to respond) is in scope; whether grey literature without a method section is eligible; and whether a cross-domain study (emergency medicine) belongs in the main review or in the separate design-borrowing search.

### 1.10 Common errors and limits

- Starting with a conclusion ("show that the rubric works") rather than a question that can come out either way.
- Asking a causal question of historical data where the exposure coincided with other changes, without saying how the coincidence will be addressed.
- Leaving the estimand undefined until the analysis, then choosing the summary that gives the largest effect.
- Searching one discipline's database and calling the result "the literature"; missing human-factors and safety work where the methods you need already exist.
- Ignoring grey literature in a field where CSIRT reports and agency guidance carry much of the practical evidence — or including vendor claims ("cuts MTTR by 90%") without criteria.
- Reporting raw agreement without chance correction, or kappa without examining the disagreements.
- Writing the review author by author.
- Treating a study's finding as transferable without recording its unit, population and setting.

The limit of a master's review is time: it will not be exhaustive, and it should not pretend to be. Its credibility comes from a documented, repeatable search, a known-item test and an honest statement of what was not searched.

### Exercises — chapter 1

**EX001 — From topic to question.** *Objective:* narrow a topic into an answerable question. *Inputs:* the topic "handover between shifts during long incidents". *Constraints:* one primary question; an observable exposure; an outcome that can be measured without the participants' own self-report alone. *Steps:* (1) state the decision-maker's problem; (2) write the question in the structured form of §1.1.2; (3) test it against each FINER criterion in one sentence, saying honestly what is not feasible; (4) state the claim you hope to make and its scope. *Expected evidence:* a half-page memo. *Rubric:* 3 = answerable with obtainable data, exposure and outcome observable, FINER applied honestly, claim scoped to the design; 2 = one element vague; 1 = still a topic; 0 = none.

**EX002 — Question types.** *Objective:* match questions to designs and claims. *Inputs:* (a) "What share of MRSS tickets in 2025 were re-graded upward after review?" (b) "Are tickets opened at night more often under-triaged?" (c) "Does SEV-4 reduce under-triage compared with usual judgement?" (d) "Why do analysts discount incidents with few alerts?" (e) "Did East's under-triage fall because it adopted SEV-4?" *Constraints:* use the table in §1.1.3. *Steps:* classify each; name the minimum design; name the strongest claim. *Expected evidence:* a table. *Rubric:* 3 = all classified with designs that would genuinely support the claims, and (e) recognized as causal but weakly identified by the historical data; 2 = one error; 1 = designs generic; 0 = none.

**EX003 — Search protocol and known-item test.** *Objective:* build a documented, cross-disciplinary search. *Inputs:* RQ1–RQ3 in §1.8. *Constraints:* concept blocks with synonyms from at least two disciplines; at least three bibliographic sources; a grey-literature plan naming four source types. *Steps:* (1) write the blocks; (2) list sources with a one-line justification each; (3) define a known-item set of three studies and how you will check retrieval; (4) state a stopping rule for chaining; (5) design a search-log template. *Expected evidence:* a one-page protocol and template. *Rubric:* 3 = blocks cross disciplines, grey literature specified, known-item test and stopping rule concrete, log re-runnable; 2 = one element missing; 1 = single-discipline search; 0 = none.

**EX004 — Run and extend Lab 1.** *Objective:* use deduplication and agreement as diagnostics. *Inputs:* the lab. *Constraints:* offline. *Steps:* (1) run it and record the output; (2) append the record `("psyc", "Checklist Use Under Time-Pressure in Emergency Triage", 2018, "")` to `RECORDS` (no change to the decision strings is needed if it is removed; if it is not removed, the assertion will fail — say which happened and why); (3) change reviewer B's decision on the mean-time-to-respond record from I to X and report the new raw agreement and kappa; (4) explain in about 100 words why one changed decision moves kappa more than raw agreement. *Expected evidence:* outputs and explanation. *Rubric:* 3 = correct outputs, the hyphen-versus-space normalization explained, kappa recomputed correctly, chance correction explained; 2 = one error; 1 = not run; 0 = none.

**EX005 — Repair the eligibility criteria.** *Objective:* turn disagreement into decidable criteria. *Inputs:* the three disagreements in Lab 1. *Constraints:* criteria must be decidable from a title and abstract, or from the first page of a grey report. *Steps:* (1) write inclusion and exclusion criteria covering measurement papers, grey literature and cross-domain studies; (2) apply them to the three records; (3) state what happens to a record you still cannot decide. *Expected evidence:* criteria and decisions. *Rubric:* 3 = criteria decidable, decisions consistent, undecidable records sent to full-text review rather than excluded; 2 = one inconsistency; 1 = criteria restate the topic; 0 = none.

**EX006 — Concept matrix with a real study.** *Objective:* synthesize by concept and read a design critically. *Inputs:* the matrix in §1.6 and the abstract of [Haynes et al. (2009)](https://doi.org/10.1056/NEJMsa0810119). *Constraints:* read the abstract yourself; quote numbers with their source. *Steps:* (1) check the Haynes row against the abstract and correct it if needed; (2) add a column "what the study can say about experienced professionals"; (3) write a 200-word concept-centred paragraph on "structured aids for time-pressured classification decisions" that ends with the gap. *Expected evidence:* matrix and paragraph. *Rubric:* 3 = Haynes row accurate (pre–post design across eight hospitals, complication and death rates before and after, no concurrent control), paragraph organized by concept, gap scoped to the search; 2 = paragraph author by author; 1 = numbers unsourced; 0 = none.

**EX007 — Estimand and scope memo.** *Objective:* define exactly what will be estimated. *Inputs:* RQ1 and RQ2. *Constraints:* the five-part template in §1.2. *Steps:* (1) write the estimand for RQ1; (2) write one for the time cost in RQ2; (3) list two estimands a careless analyst might compute instead and explain how they differ; (4) state the hoped-for claim and two claims explicitly out of scope. *Expected evidence:* one page. *Rubric:* 3 = estimands unambiguous, with the within-analyst contrast and intercurrent events handled, alternatives genuinely different (pooled proportion, critical-only rate, odds ratio), out-of-scope claims explicit; 2 = one estimand ambiguous; 1 = no contrast; 0 = none.

### Chapter synthesis

A dissertation stands on its question. Move from topic to problem to question deliberately, recording the reason for each narrowing. Write the question in a structured form with an observable exposure, a comparison and an outcome that matters; test it against feasibility and ethics before interest. Classify it, because the type fixes the strongest claim. Define the estimand and claim scope before seeing data. Choose and name the review type; search across security, human-factors and safety literatures and grey sources; test the search with known items; deduplicate, dual-screen and use kappa to find unclear criteria. Synthesize by concept so that the gap emerges from the matrix rather than from assertion.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Advanced incident response research seminar

### Learning outcomes and connection

After this chapter you should be able to:

1. Describe four competing models of what makes incident response "effective" and the success measure each one implies.
2. Show, with a worked dataset, how the choice of success measure — and the handling of cases that have not finished — can reverse which method looks better.
3. Read a study with a seven-question protocol that separates its design from its result, and grade its evidence for your question.
4. Lead a seminar comparison of two studies and state precisely what each model leaves unexplained.
5. Turn the seminar into a justified choice of primary and secondary outcomes for your own study.

The chapter builds on the concept matrix of Chapter 1 and prepares Chapter 3, where the outcomes chosen here are fixed in a design and a pre-analysis plan.

### 2.1 What the seminar is for

A master's research seminar is not a reading group that summarizes papers. Its purpose is to make you *disagree well*: to see that two careful studies of "the same" practice can reach different conclusions because they assumed different things about what response is for, measured different outcomes, or studied different settings. By the end of the seminar you should be able to say which assumptions your own study will adopt and defend that choice to an examiner who prefers another.

The seminar has a rhythm. Before each session, every participant reads the assigned studies using the protocol in §2.4 and writes a one-page note. In the session, one participant presents a study's design (not its conclusion) for ten minutes; a second presents the competing study; the group then works through the questions "what would each study's authors predict about the other's setting?" and "what does each model leave unexplained?". The session ends with a written statement of the disagreement — not a resolution.

### 2.2 Competing models of response effectiveness

"Effective incident response" has no single definition. Four models recur in the practitioner and research literature. Each is a coherent view; each implies a different success measure; each leaves something out.

| Model | What response is for | Typical success measure | What the model leaves unexplained |
|---|---|---|---|
| **Speed (throughput) model** | Close incidents quickly so that exposure time is short and queues do not grow. | Mean or median time to detect, respond, contain or resolve (often "MTTR"). | Whether the right incidents were handled first; incidents never escalated; cases still open at the cut-off; quality of closure. |
| **Accuracy (classification) model** | Classify and prioritize each incident correctly so that resources follow risk. | Agreement with a reference standard; under- and over-triage rates; weighted kappa. | The cost of accuracy in time; how the reference standard was set; whether correct classification leads to better outcomes. |
| **Harm-reduction (outcome) model** | Reduce the harm incidents cause to services, data and people. | Service downtime, records exposed, recovery cost, notification met on time. | Attribution: harm depends on the attacker and the environment, not only on the response; rare outcomes make studies small. |
| **Resilience (adaptive capacity) model** | Sustain essential functions and learn, adapting to surprises that no playbook anticipated. | Continuity of minimum service; time to restore; quality of after-action learning; recurrence. | Measurement: adaptive capacity is hard to observe before it is needed; studies tend to be qualitative and retrospective. |

The models are not mutually exclusive, and mature programmes use measures from several. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (April 2025) frames incident response as part of cybersecurity risk management rather than as a self-contained lifecycle, which is closest to the harm-reduction and resilience models, while [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) (2016) on recovery planning emphasizes restoring and improving capability. Operational SOC dashboards, by contrast, are often built on the speed model, because time stamps are what ticketing systems record automatically. Field studies of SOCs report that metrics chosen for ease of collection shape what analysts optimize ([Sundaramurthy et al. 2014](https://doi.org/10.1145/2663887.2663904); [Kokulu et al. 2019](https://doi.org/10.1145/3319535.3354239)).

#### 2.2.1 Decision theories underneath the models

Behind the accuracy model stand two accounts of how analysts decide, introduced in Chapter 1. **Situation awareness** ([Endsley 1995](https://doi.org/10.1518/001872095779049543)) distinguishes perceiving the relevant elements, comprehending their meaning and projecting their future status. An under-triaged quiet-impact incident, on this account, is a failure of perception or comprehension: the analyst did not attend to the affected service or its time-criticality. A rubric that forces those elements into view should help. **Naturalistic decision making** ([Klein 2008](https://doi.org/10.1518/001872008X288385)) emphasizes recognition: experienced decision-makers match situations to familiar patterns and simulate a course of action rather than comparing options. On this account, rubrics help when patterns are unfamiliar or misleading but may interfere with expert recognition and add time. A third body of work, on alert overload, argues that the dominant problem is volume and false positives, which teach analysts to discount signals ([Alahmadi, Axon and Martinovic 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi)).

These accounts make **different predictions** about a rubric study, which is exactly what makes them useful:

| Prediction | Situation awareness | Naturalistic (recognition) | Alert-overload |
|---|---|---|---|
| Effect on quiet-impact cases | Large reduction in under-triage | Reduction mainly for less experienced analysts | Reduction, because discounting is driven by low alert volume |
| Effect on noisy, obvious cases | Little | Little or slight harm (slower, no gain) | Little |
| Effect by experience | Similar across experience | Smaller for experts | Similar |
| Time cost | Moderate | Larger for experts | Moderate |

A study that measures only the overall under-triage rate cannot distinguish these accounts. One that also records case type and experience can, at least partly. This is the seminar's practical payoff: the competing models tell you which subgroups and secondary outcomes to predeclare.

### 2.3 How the success measure shapes the answer

The speed model's measures have properties that are easy to miss and that matter for any study comparing response methods.

**Censoring.** At the end of a study window some incidents are still open. If they are excluded, the mean time to resolve is computed only on incidents that finished — which are disproportionately the easy ones. A method that leaves more hard cases open will look faster. Survival-analysis methods treat open cases as **censored** observations (we know they took *at least* this long); at minimum, report how many were open, and use measures such as the share closed within a fixed time that count every case.

**Skew.** Resolution times are strongly right-skewed: most incidents close quickly, a few take days. The mean is dominated by the tail; the median describes the typical case; both should be reported, with the share of long cases.

**Escalation as cost.** A method that correctly escalates more high-impact incidents will generate more long investigations. Under the speed model it looks worse, even though under the accuracy and harm models it is doing its job.

**Case mix.** If two methods are compared on different incidents, differences in severity mix can dominate any method effect. Chapter 4 returns to this as confounding.

The accuracy model has its own traps. Its reference standard must be set **independently** of the decisions being judged (otherwise the analyst's rating partly defines the truth); agreement statistics depend on the distribution of categories; and weighted kappa ([Cohen 1968](https://doi.org/10.1037/h0026256)) gives partial credit for near misses, which is appropriate for ordinal severity but hides the asymmetry between under- and over-triage. That is why the Triage Rubric Study reports under-triage and over-triage separately, with weighted kappa as a secondary summary.

### 2.4 A seven-question reading protocol

For every study in your concept matrix, answer these questions in writing before you read its discussion section:

1. **Question and model.** What did the authors want to know, and which model of effectiveness did they assume?
2. **Unit and population.** What was a single observation (an incident, a decision, an analyst, a team)? Who or what was sampled, and how?
3. **Exposure and assignment.** What was compared with what, and who decided which unit got which condition?
4. **Outcome and its source.** How was the outcome measured, by whom, and could the exposure itself have changed the measurement?
5. **Completeness.** What happened to units that dropped out, cases still open, or missing fields?
6. **Rivals.** Which explanations other than the exposure could produce the result, and did the authors test them?
7. **Transfer.** To which populations and settings does the result plausibly apply, and what is different about yours?

Then grade the study's **evidence for your question** (not its quality in general): *direct* (same exposure, comparable population, outcome you will use), *indirect* (a related exposure, population or outcome), or *design-only* (useful for methods, not for the answer). The surgical-checklist study of [Haynes et al. (2009)](https://doi.org/10.1056/NEJMsa0810119), for example, is design-only evidence for the Triage Rubric Study: a different profession and outcome, but an instructive pre–post design whose rivals (secular trends, observation effects, simultaneous changes) are the same ones that threaten MRSS's historical data.

### 2.5 Evidence quality without a hierarchy fetish

Medical research ranks designs in a hierarchy with randomized trials near the top. The ranking captures something real — random assignment breaks the link between exposure and confounders — but applied mechanically it misleads in incident response, where randomized trials on live incidents are almost never feasible or ethical. Better questions are: *what is the counterfactual in this study, and how credible is it?* and *what would the study have shown if the favoured explanation were false?* A carefully controlled tabletop with experienced volunteers can provide stronger causal evidence about a decision aid than a large ticket audit, while the ticket audit provides better evidence about how often a problem occurs in practice. Each answers a different question; neither is simply "better".

### 2.6 Worked example: two studies, two success measures (synthetic)

The seminar is assigned two fictional studies of the same rubric at different organizations.

*Study P* ("Rubric slows response") compared 300 incidents handled under a structured rubric with 300 handled under usual practice. Its primary outcome was the **mean hours to resolve among closed incidents**. It reported that rubric incidents took longer (11.3 versus 10.2 hours) and concluded that the rubric "reduces response efficiency".

*Study Q* ("Rubric reduces missed incidents") analysed the same kind of data with **under-triage of high-impact incidents** (rating below a panel-reviewed reference) as its outcome. It reported 9.7% versus 23.7% and concluded that the rubric "improves triage".

The seminar's task is not to decide which study is right. It is to show that both can be accurate descriptions of the same data, and to explain why. Lab 2 reconstructs the situation.

### 2.7 Practical activity: one dataset, three success measures

Lab 2 simulates 300 fictional incidents, each handled once under the rubric (R) and once under usual judgement (U) — a paired simulation, so case mix is identical. Under R, high-impact incidents are under-triaged less often; correctly escalated incidents take longer because escalation triggers containment work; under-triaged high-impact incidents are discovered late, so many are still open when the 72-hour study window closes. Save it as `lab2_measures.py`.

```python
# Lab 2 - one synthetic dataset, three success measures: which triage method "wins"? (offline, stdlib only)
# The same 300 fictional incidents handled once under each method (a paired simulation). Reference impact: 1 (low) .. 4 (critical), assigned by a review panel.
# Method R (structured rubric) escalates high-impact cases more often; escalated cases take longer to close.
import random, statistics as st
CASES = random.Random(1012).choices([1, 2, 3, 4], weights=[40, 30, 20, 10], k=300)  # same cases, both methods
def simulate(method):
    rng = random.Random({"R": 61, "U": 62}[method])
    rows = []
    for ref in CASES:
        miss_p = {"R": 0.12, "U": 0.30}[method] if ref >= 3 else 0.0   # under-triage probability
        under = rng.random() < miss_p
        escalated = ref >= 3 and not under
        hours = rng.lognormvariate(1.0 + 0.25 * ref, 0.6) + (rng.uniform(10, 26) if escalated else 0.0)
        if under:                                     # missed high-impact cases reopen later, if ever
            hours += rng.lognormvariate(4.3, 0.4)
        closed_by_cutoff = hours <= 72                # study window ends; long cases still open
        rows.append((ref, under, escalated, hours, closed_by_cutoff))
    return rows
data = {m: simulate(m) for m in ("R", "U")}
print("method  closed  mean_h(closed)  median_h(closed)  under-triage(high-impact)  still_open")
for m, rows in data.items():
    closed = [r[3] for r in rows if r[4]]
    hi = [r for r in rows if r[0] >= 3]
    ut = sum(r[1] for r in hi) / len(hi)
    print(f"{m:>6}  {len(closed):>6}  {st.mean(closed):>14.1f}  {st.median(closed):>16.1f}  "
          f"{ut:>17.1%} of {len(hi):>3}  {len(rows) - len(closed):>10}")
for m, rows in data.items():
    allh = sorted(r[3] for r in rows)
    print(f"{m}: median hours including open cases (open = >72h, rank only): {st.median(allh):.1f}"
          f"  share closed within 24h: {sum(h <= 24 for h in allh) / len(allh):.1%}")
```

Expected output:

```text
method  closed  mean_h(closed)  median_h(closed)  under-triage(high-impact)  still_open
     R     296            11.3               5.2               9.7% of  93           4
     U     280            10.2               5.3              23.7% of  93          20
R: median hours including open cases (open = >72h, rank only): 5.4  share closed within 24h: 82.7%
U: median hours including open cases (open = >72h, rank only): 5.7  share closed within 24h: 80.7%
```

How to read it. Study P's measure — mean hours among closed incidents — favours U (10.2 versus 11.3 hours). Study Q's measure favours R (under-triage 9.7% versus 23.7% of the same 93 high-impact incidents). Both are arithmetically correct. The reason they disagree is visible in the last column: U leaves 20 incidents open at the cut-off against R's 4, and those open incidents are mostly missed high-impact cases — exactly the ones the speed measure silently drops. The median among closed incidents barely differs, and a measure that counts every incident (share closed within 24 hours) slightly favours R. The lesson is not "Study Q is right": it is that a success measure is a model of what response is for, and a study that does not report what it excluded can make a better method look worse.

### 2.8 Writing the disagreement

The seminar ends with a written statement in a standard form:

> *Study P and Study Q agree that the rubric lengthens work on correctly escalated incidents. They disagree about effectiveness because P measures speed among closed incidents and Q measures classification against a reference. P's measure excludes incidents still open at the cut-off, which are disproportionately under-triaged high-impact cases under usual practice; Q's measure depends on the validity of its reference panel and does not show whether better classification reduced harm. Neither study measured harm. Our study will adopt Q's primary outcome, report P's measure with censoring made explicit, and record time per decision as the cost.*

Notice what this paragraph does: it names the shared finding, locates the disagreement in the measures, states what each leaves unexplained, and turns that into design decisions.

### 2.9 Presenting in the seminar

When you present a study, spend most of your time on design: unit, assignment, outcome and rivals. Put the result on one slide at the end. Practise the sentence "the strongest claim this design supports is…". When you challenge a presenter, ask questions that could change the conclusion ("how many incidents were still open?") rather than questions that display your knowledge. Record the session's open questions; several will become your own study's secondary analyses.

### 2.10 Common errors and limits

- Treating "effectiveness" as self-evident and adopting whatever metric the ticketing system produces.
- Computing mean time to resolve on closed incidents only, without reporting how many were open or why.
- Reporting means of heavily skewed times without medians or tail shares.
- Comparing methods on different incident sets without addressing case mix.
- Treating agreement with a reference as accuracy without asking how the reference was set and by whom.
- Ranking studies by design label alone instead of asking what counterfactual each provides for *your* question.
- Ending a seminar with a vote on which study is right instead of a precise statement of the disagreement.

The limit of a seminar is that it works with published reports, which omit much of what you need (excluded cases, measurement details, deviations). Write to authors when a missing detail decides your reading, and record the question even if no reply comes.

### Exercises — chapter 2

**EX008 — Map the models.** *Objective:* relate success measures to models of effectiveness. *Inputs:* the table in §2.2. *Constraints:* one row per model. *Steps:* for each model, (1) name one measure available from a ticketing system and one that requires extra data collection; (2) give one way the measure could improve while the thing it stands for gets worse. *Expected evidence:* a table. *Rubric:* 3 = measures realistic and the "gaming" or distortion examples specific; 2 = one model weak; 1 = measures generic; 0 = none.

**EX009 — Extend Lab 2.** *Objective:* see how a study window changes a speed measure. *Inputs:* Lab 2. *Constraints:* offline; change only the 72-hour cut-off (both occurrences in the code and the label). *Steps:* (1) rerun with a 168-hour (one-week) window; (2) report closed counts, mean hours among closed incidents and still-open counts for both methods; (3) explain which direction the mean comparison moved and why; (4) state which reported measures did not change and why. *Expected evidence:* outputs and a 150-word explanation. *Rubric:* 3 = outputs correct, the movement explained by late discovery of missed cases entering the closed set, invariance of under-triage explained; 2 = one error; 1 = not run; 0 = none.

**EX010 — Predictions from theory.** *Objective:* derive testable predictions from competing decision theories. *Inputs:* §2.2.1. *Constraints:* predictions must be observable in a tabletop study. *Steps:* (1) for each of the three accounts, write one prediction that differs from the other two; (2) say what data the Triage Rubric Study must record to test it; (3) say which prediction the study as designed in Chapter 1 cannot test, and why. *Expected evidence:* a short table and paragraph. *Rubric:* 3 = predictions genuinely discriminating, data requirements concrete (case type, experience, time), untestable prediction identified honestly; 2 = predictions overlap; 1 = restates theories; 0 = none.

**EX011 — Read a real study with the protocol.** *Objective:* apply the seven-question protocol. *Inputs:* the published version of [Alahmadi, Axon and Martinovic (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi). *Constraints:* answer from the paper itself; do not rely on summaries. *Steps:* (1) answer the seven questions; (2) grade its evidence for RQ1 and for RQ3 of the Triage Rubric Study; (3) name one design choice in your study it should influence. *Expected evidence:* one page. *Rubric:* 3 = accurate description of a qualitative interview-and-survey study of SOC practitioners, evidence correctly graded as indirect for RQ1 and more direct for RQ3, design influence concrete; 2 = one answer inaccurate; 1 = summary only; 0 = none.

**EX012 — The disagreement statement.** *Objective:* write a seminar conclusion. *Inputs:* Studies P and Q, Lab 2 output. *Constraints:* 150–200 words; no verdict on which study is "right". *Steps:* follow the form in §2.8 but add one analysis that, if both studies' authors agreed to it, would narrow the disagreement. *Expected evidence:* the statement. *Rubric:* 3 = shared finding, located disagreement, what each leaves unexplained, and a narrowing analysis (for example, time-to-resolve with censored cases handled, or a harm measure); 2 = verdict creeps in; 1 = summary; 0 = none.

**EX013 — Choose and justify outcomes.** *Objective:* fix primary and secondary outcomes. *Inputs:* the four models, Lab 2, your answers to EX010. *Constraints:* one primary outcome; at most four secondary outcomes. *Steps:* (1) name and define each outcome exactly; (2) justify the primary in terms of the decision-maker's problem; (3) for each secondary, say what it guards against; (4) name one attractive outcome you will *not* use and why. *Expected evidence:* a half-page outcome specification. *Rubric:* 3 = primary justified by the problem, secondaries guarding against specific misreadings (time cost, over-triage, agreement, subgroup by case type), rejected outcome reasoned; 2 = too many outcomes; 1 = undefined outcomes; 0 = none.

**EX014 — Evidence grading.** *Objective:* grade evidence for a specific question. *Inputs:* the four rows of the concept matrix in §1.6. *Constraints:* use direct / indirect / design-only. *Steps:* grade each row for RQ1 and for the historical MRSS question, with one sentence of justification each. *Expected evidence:* a table. *Rubric:* 3 = grades differ appropriately between the two questions and the justifications name population, exposure or outcome differences; 2 = one inconsistency; 1 = all graded alike; 0 = none.

### Chapter synthesis

What counts as effective incident response depends on what response is for: speed, accuracy, harm reduction or resilience. Each model implies a measure, and each measure leaves something out. Speed measures are distorted by censoring, skew, escalation costs and case mix; accuracy measures depend on an independent reference and should separate under- from over-triage. Competing decision theories predict different patterns across case types and experience, and those predictions tell you which subgroups and secondary outcomes to predeclare. Read studies for design before results, grade their evidence for your question, and end a seminar with a precise statement of disagreement that turns into design decisions.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 08

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes and connection

After this chapter you should be able to:

1. Compare observational, quasi-experimental and controlled tabletop designs for an incident-response question and justify a choice in terms of the counterfactual each provides.
2. Explain the logic of a crossover design, its assumptions (no lasting carryover, balanced periods and case sets) and how to check them.
3. Size a study by simulation — **design analysis** — reporting power, the exaggeration of significant estimates and the false-positive rate, rather than quoting a single power formula.
4. Write an ethics protocol for research with analysts as participants, including consent, voluntariness, confidentiality from employers and handling of security-sensitive material.
5. Predeclare measures and an analysis plan, and set up a reproducible project before any data exist.

The chapter builds on the question and estimand of Chapter 1 and the outcome choices of Chapter 2, and prepares Chapter 4, which examines the explanations a design must rule out.

### 3.1 Designs for incident-response questions

#### 3.1.1 The core problem

A causal question asks what would have happened under a different condition — the **counterfactual**. We never observe it directly: an analyst either used the rubric on a case or did not. Every design is a strategy for approximating the missing counterfactual, and each strategy rests on assumptions you must state and, where possible, test. A standard introduction to this way of thinking is [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook), freely available from its authors.

#### 3.1.2 Design options

| Design | How the counterfactual is approximated | Main assumption | Fit for the Triage Rubric Study |
|---|---|---|---|
| **Cross-sectional comparison** of teams or tickets | Another team's tickets in the same period | The teams are comparable apart from the rubric | Poor: East and West differ in seniority and case mix (Chapter 4). |
| **Before–after (pre–post)** in one team | The same team before adoption | Nothing else changed at the same time | Poor: seniority changed in the same month. |
| **Difference-in-differences** on historical tickets | The other team's change over the same period | Parallel trends absent the rubric | Possible as a secondary strand; vulnerable to team-specific co-interventions. |
| **Parallel controlled tabletop** | Other analysts, randomly assigned to usual judgement | Randomization balances analysts | Valid but needs many analysts, because analysts differ a lot. |
| **Crossover controlled tabletop** | The same analyst on comparable cases without the rubric | No lasting carryover; periods and case sets balanced | Chosen: removes stable between-analyst differences; feasible with a few dozen volunteers. |

In a **crossover** design each participant experiences both conditions in sequence. The comparison of interest is *within* each participant, so stable differences between people — skill, caution, speed — cancel out. The price is three assumptions. (1) **No lasting carryover**: the first condition must not change behaviour in the second. A rubric is a worrying case, because analysts who used it first may keep its questions in mind afterwards. The usual remedy is a washout or, here, an order that can be checked: if rubric-first analysts do better in their later "usual" period than usual-first analysts do in their earlier one, carryover is suspected. (2) **No unbalanced period effect**: practice or fatigue may change performance from the first to the second period; balancing the order (half start with each condition) prevents this from biasing the comparison, and it can be estimated. (3) **Comparable case sets**: each period uses different cases, so the sets must be matched in reference severity and type and counterbalanced across sequences.

The Triage Rubric Study therefore uses four sequences, six analysts each: usual on set A then rubric on set B; usual on B then rubric on A; rubric on A then usual on B; rubric on B then usual on A. Each set has twelve fictional cases with the same distribution of reference severities: eight high-impact (four "quiet"), two of severity 2 and two of severity 1. Analysts are allocated to sequences at random, stratified by experience (more or less than three years), using a seeded random number generator whose seed is recorded in the protocol.

#### 3.1.3 The tabletop as an instrument

A controlled tabletop is a measurement instrument and must be designed like one. [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) (2006) provides vocabulary for exercise design — objectives, scenarios, injects, facilitators, evaluators — that is still useful, although it was written for organizational exercises rather than experiments. For research use, add three properties. **Standardization**: every analyst sees the same case materials in the same format, with the same time limit and instructions. **A reference standard set independently**: three senior responders not involved in the study rate each case from its full fictional ground truth, independently, and then reach consensus; disagreements are recorded (two cases, C07 and C19, are split 2–1, which Chapter 8 uses). **Fidelity checks**: an observer records whether the rubric sheet was actually completed in rubric sessions and was absent in usual sessions.

### 3.2 Threats to validity

Validity vocabulary is a standard methods concept; four families are enough for planning.

- **Internal validity** — is the difference caused by the rubric? Threats: carryover, period effects, unbalanced case sets, observers who know the condition and record times differently, analysts who guess the hypothesis and try to please.
- **Construct validity** — do the measures capture what we mean? Threats: a reference standard that reflects the panel's habits rather than impact; "under-triage" defined at one level when two-level errors matter more; time measured from an ambiguous start.
- **Statistical conclusion validity** — is the inference sound? Threats: too few analysts; treating each decision as independent when decisions are clustered within analysts; flexible analysis choices.
- **External validity** — does it transfer? Threats: fictional cases lack the noise, interruptions and stakes of live work; volunteers are more motivated than average; a printed rubric differs from one embedded in a ticketing tool.

For each threat, the protocol records a **mitigation** and a **check**. For example: observers are not told the hypothesis, and timing is checked by two observers on a sample (Chapter 5); clustering is handled by analysing per-analyst differences (Chapter 6); external validity is discussed with direction, not hidden (Chapter 7).

### 3.3 Design analysis before data

#### 3.3.1 Why simulate

Classical power formulas answer one question — the probability of a "significant" result if a specified effect is true — under simplifying assumptions. For a crossover with binary outcomes, clustered decisions and analysts who differ, the assumptions are easier to get wrong than to get right. A **design analysis** by simulation asks a broader set of questions ([Gelman and Carlin 2014](https://doi.org/10.1177/1745691614551642)): if the true effect is what we think, how often will the study detect it (**power**)? When it does, how much will the estimate exaggerate the truth (**type M**, magnitude error)? How often will it get the sign wrong (**type S**)? And if there is no effect, how often will it falsely find one? A study with low power is not merely likely to miss a real effect; its significant results are systematically too large.

#### 3.3.2 The smallest effect of interest

Before simulating, decide the **smallest effect of interest**: the effect below which the decision-maker would not change practice. MRSS managers say they would not mandate a rubric that costs time unless it cut under-triage of high-impact cases by at least 10 percentage points. That number, not the effect you hope for, should anchor the design ([Lakens 2022](https://doi.org/10.1525/collabra.33267) reviews ways of justifying sample sizes, including this one). The study also simulates a plausible effect of 15 points, taken from the synthetic pilot literature in the concept matrix.

#### 3.3.3 Simulating the design

Lab 3 simulates thousands of synthetic studies. Each analyst has a personal tendency to under-triage (a random effect on the log-odds scale), rates a fixed number of high-impact cases per condition, and is either in a crossover (both conditions) or a parallel design (one condition, twice as many cases, so the workload is equal). Save it as `lab3_design.py`.

```python
# Lab 3 - design analysis before recruiting: crossover versus parallel tabletop design (offline, stdlib only)
# Synthetic analysts differ in their own tendency to under-triage. Each analyst rates HI high-impact cases per
# condition. Outcome: under-triage proportion. We simulate many studies to see what each design can detect.
import math, random, statistics as st
def logit_inv(x): return 1 / (1 + math.exp(-x))
def one_study(rng, n_analysts, hi_per_condition, p_usual, p_rubric, design, sd_analyst=0.8):
    base = math.log(p_usual / (1 - p_usual)); eff = math.log(p_rubric / (1 - p_rubric)) - base
    diffs, rub, usu = [], [], []
    for a in range(n_analysts):
        u = rng.gauss(0, sd_analyst)
        rate = lambda cond: sum(rng.random() < logit_inv(base + u + (eff if cond else 0)) for _ in range(hi_per_condition)) / hi_per_condition
        if design == "crossover":
            diffs.append(rate(True) - rate(False))
        else:   # parallel: each analyst sees one condition, with twice the cases so total workload is equal
            hi_per_condition *= 2
            (rub if a % 2 == 0 else usu).append(rate(a % 2 == 0))
            hi_per_condition //= 2
    if design == "crossover":
        est = st.mean(diffs); se = st.stdev(diffs) / math.sqrt(len(diffs))
    else:
        est = st.mean(rub) - st.mean(usu); se = math.sqrt(st.variance(rub) / len(rub) + st.variance(usu) / len(usu))
    return est, abs(est / se) > 2.07 if se > 0 else False   # t(0.975, ~22 df) ~ 2.07
def design_check(design, n, hi, p_u, p_r, reps=2000, seed=7):
    rng = random.Random(seed)
    res = [one_study(rng, n, hi, p_u, p_r, design) for _ in range(reps)]
    sig = [e for e, s in res if s]
    true = p_r - p_u
    power = len(sig) / reps
    exagg = st.mean(abs(e) for e in sig) / abs(true) if sig and true else float("nan")
    wrong_sign = sum(1 for e in sig if e * true < 0) / len(sig) if sig and true else float("nan")
    return power, exagg, wrong_sign, st.mean(e for e, _ in res)
print("design     analysts  hi/cond  true_diff  power  exaggeration_if_sig  mean_estimate")
for design in ("crossover", "parallel"):
    for n in (12, 24, 36):
        p, x, w, m = design_check(design, n, 4, 0.30, 0.15)
        print(f"{design:<10} {n:>8}  {4:>7}  {-0.15:>9.2f}  {p:>5.2f}  {x:>19.2f}  {m:>13.3f}")
p, x, w, m = design_check("crossover", 24, 4, 0.30, 0.30)
print(f"null check (no true effect), crossover n=24: false-positive rate {p:.3f}, mean estimate {m:.3f}")
p, x, w, m = design_check("crossover", 24, 4, 0.30, 0.20)
print(f"smallest effect of interest (-0.10), crossover n=24: power {p:.2f}, exaggeration if significant {x:.2f}")
for hi in (8,):
    p, x, w, m = design_check("crossover", 24, hi, 0.30, 0.15)
    print(f"revised design, crossover n=24 with {hi} high-impact cases per condition: power {p:.2f}, exaggeration {x:.2f}")
    p, x, w, m = design_check("crossover", 24, hi, 0.30, 0.20)
    print(f"revised design at the smallest effect of interest (-0.10): power {p:.2f}, exaggeration {x:.2f}")
```

Expected output:

```text
design     analysts  hi/cond  true_diff  power  exaggeration_if_sig  mean_estimate
crossover        12        4      -0.15   0.37                 1.47         -0.142
crossover        24        4      -0.15   0.64                 1.16         -0.142
crossover        36        4      -0.15   0.81                 1.07         -0.144
parallel         12        4      -0.15   0.26                 1.81         -0.146
parallel         24        4      -0.15   0.43                 1.45         -0.146
parallel         36        4      -0.15   0.56                 1.27         -0.146
null check (no true effect), crossover n=24: false-positive rate 0.046, mean estimate 0.003
smallest effect of interest (-0.10), crossover n=24: power 0.29, exaggeration if significant 1.60
revised design, crossover n=24 with 8 high-impact cases per condition: power 0.92, exaggeration 1.02
revised design at the smallest effect of interest (-0.10): power 0.56, exaggeration 1.24
```

How to read it. With four high-impact cases per condition — the first draft protocol — a crossover with 24 analysts detects a 15-point effect only about 64% of the time, and a parallel design of the same size only 43%: between-analyst variation is large, and the crossover removes it. At 12 analysts, significant crossover estimates exaggerate the true effect by about half. The null check shows the analysis keeps its false-positive rate near the nominal 5%. The revision that matters is the number of high-impact cases per condition: with eight, the crossover with 24 analysts has power of about 0.92 for a 15-point effect, with almost no exaggeration. At the smallest effect of interest (10 points), power is still only about 0.56. The protocol says so honestly: the study is designed to detect a plausible effect and to estimate it with useful precision, but a true 10-point effect has roughly even odds of reaching conventional significance, and the dissertation will report an interval, not a verdict.

Two details are worth noticing. The "true difference" is set on each analyst's log-odds scale, so the average difference in proportions across heterogeneous analysts (the mean estimate, about −0.14) is slightly smaller than −0.15 — the estimand from Chapter 1 is the average difference in proportions, and the simulation shows the two are not identical. And the critical value 2.07 approximates a t distribution with about 22 degrees of freedom; Chapter 6 uses resampling methods that avoid this approximation.

### 3.4 Ethics with analysts as participants

#### 3.4.1 What needs review

Research that collects data from people — their decisions, times, words — normally needs approval from the university's research ethics committee (in the United States an Institutional Review Board under the Common Rule, [45 CFR 46](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46)). Using fictional cases does not remove the need: the participants are real, and their performance data are personal data. The [Belmont Report](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html) principles of respect for persons, beneficence and justice underpin most committees' reasoning, and the [Menlo Report](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) (2012) adapts them to information and communication technology research, adding respect for law and public interest. Where participants are in the European Union, the [General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj) applies to their personal data. Regulations differ by country and change; the protocol states which apply and the committee decides. This book gives no legal advice.

#### 3.4.2 Risks particular to studying analysts

- **Employment risk.** A participant's error rate, if seen by their employer, could affect their appraisal or job. The study must make it impossible for MRSS managers to see individual results.
- **Coercion.** If a manager recruits, or the student is a colleague or supervisor of participants, "voluntary" participation may not be. Recruitment goes through a neutral channel; non-participation is invisible to managers.
- **Security-sensitive material.** Cases must not contain real indicators, real vulnerabilities or details of a real organization's defences; the case writers use fictional systems.
- **Psychological load.** Timed decisions about simulated crises can be stressful; participants may stop at any time without explanation.
- **Small-population re-identification.** With 24 analysts from a handful of teams, experience band plus team plus sequence can identify a person; reported tables must avoid such combinations.

#### 3.4.3 Safeguards

Informed consent in writing, with a plain-language information sheet; the right to withdraw, including withdrawal of data up to a stated date; pseudonymous participant codes (A01–A24) generated by the student, with the key stored separately and destroyed after the study; no individual results shared with any employer; aggregated reporting with minimum cell sizes; fictional case material reviewed by a second person for real-world leakage; a debrief that explains the study's purpose after all sessions are complete. The debrief interviews (RQ3) have their own consent item, and recordings are deleted after transcription and checking.

#### 3.4.4 The application

An ethics application for this study answers, at minimum: what will participants do and for how long; how they are recruited and by whom; what data are collected, where they are stored, who can access them and when they are deleted; what risks exist and how each is reduced; and how results are reported. Attach the information sheet, consent form, case materials (or a sample), debrief guide and data management plan.

### 3.5 Predeclared measures and the analysis plan

A **pre-analysis plan** fixes, before data collection, the hypotheses, primary and secondary outcomes, the estimand, the analysis method, the handling of missing data and deviations, and the robustness checks. It can be registered publicly with a time stamp; preregistration's value is to separate confirmatory from exploratory analysis, not to forbid exploration ([Nosek et al. 2018](https://doi.org/10.1073/pnas.1708274114)). The case for doing so in fields with many analytic choices was made forcefully by [Simmons, Nelson and Simonsohn (2011)](https://doi.org/10.1177/0956797611417632), who showed how undisclosed flexibility in data collection and analysis can make false findings easy to produce.

The Triage Rubric Study's plan includes:

- **Primary outcome:** under-triage (rating ≤ reference − 1) among high-impact cases (reference 3–4), as a proportion per analyst per condition.
- **Primary analysis:** the mean of per-analyst differences (rubric − usual) with a 95% bootstrap interval resampling analysts, and a sign-flip permutation test; analysts with both periods.
- **Secondary outcomes:** median decision seconds; over-triage of low-impact cases (reference 1–2); quadratic-weighted kappa against the reference; under-triage by case type (quiet, noisy).
- **Checks:** period effect and carryover by sequence; fidelity of rubric use; observer timing agreement.
- **Robustness (predeclared):** two-level under-triage; inclusion of severity-2 cases; critical-only cases; an alternative reference for the two split-panel cases.
- **Deviations:** any change after data collection begins is logged with date, reason and whether data had been seen.

### 3.6 A reproducible project from day one

Reproducibility means another person can regenerate every number in the dissertation from the archived data and code. It is cheap at the start and expensive at the end ([Stodden et al. 2016](https://doi.org/10.1126/science.aah6168) set out practical recommendations for computational work). Set up the project before the pilot:

```text
triage-rubric-study/
  README.md            what the project is, how to run everything, software versions
  protocol/            ethics approval (redacted), pre-analysis plan, deviations log
  instruments/         case vignettes, rubric sheet, observer form, debrief guide
  data/raw/            read-only exports as received; never edited
  data/derived/        produced only by code
  code/                one script per step: clean, analyse, figures
  output/              tables and figures produced by code
  notes/               dated research notes with observation / inference / claim / decision
```

Rules: raw data are never edited by hand; every derived file is produced by a script; scripts record their seed and software version; the dissertation's numbers come from output files, not from copying. Where data cannot be shared because of confidentiality, the code and a synthetic dataset with the same structure can be, which lets others check the pipeline. The FAIR principles — findable, accessible, interoperable, reusable ([Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18)) — guide what to archive and describe, even when access must be restricted.

### 3.7 Worked example: the ethics committee's questions (synthetic)

The committee returns the application with four questions. Each answer changes the protocol.

1. *"The student previously worked at MRSS. Could participants feel obliged?"* — Recruitment moves to a professional association's mailing list and two other organizations; MRSS analysts may join, but no MRSS manager is told who did. The student does not recruit former colleagues directly.
2. *"Could results be traced to individuals?"* — Tables will report no cell combining team, experience band and sequence; individual analyst estimates appear only as an anonymous dot plot without labels.
3. *"Do the cases contain anything harmful?"* — A second reviewer checks every vignette for real indicators and real organization names; the cases use fictional services and documentation ranges for addresses.
4. *"What happens if a participant becomes distressed?"* — The facilitator pauses the session; the participant may stop without explanation and keep any thank-you voucher; the information sheet lists support contacts.

The revised protocol is resubmitted with a table mapping each question to the change made.

### 3.8 Common errors and limits

- Choosing a design for its label rather than for the counterfactual it provides.
- Running a crossover without balancing order and case sets, or without checking carryover and period effects.
- Quoting a power formula that ignores clustering of decisions within analysts.
- Sizing a study on the hoped-for effect rather than the smallest effect of interest, and then reporting a significant overestimate as the effect.
- Assuming fictional cases remove the need for ethics review.
- Letting managers recruit participants or see individual results.
- Writing the analysis plan after looking at the data.
- Editing raw data by hand, or copying numbers into the dissertation without a traceable source.

The limit of design is that every design rests on assumptions. Good design makes them explicit, checkable and few.

### Exercises — chapter 3

**EX015 — Choose a design.** *Objective:* justify a design by its counterfactual. *Inputs:* the design table in §3.1.2. *Constraints:* one primary design; at most one secondary strand. *Steps:* (1) for each of the five designs, state its counterfactual and main assumption for RQ1; (2) choose one and justify it in 150 words; (3) state what the chosen design cannot answer and which strand, if any, will address it. *Expected evidence:* a table and paragraph. *Rubric:* 3 = counterfactuals precise, choice justified by assumptions and feasibility, limits of the chosen design acknowledged; 2 = one design misdescribed; 1 = choice by label; 0 = none.

**EX016 — Carryover and period checks.** *Objective:* design the checks for a crossover. *Inputs:* the four sequences in §3.1.2. *Constraints:* use only data the study collects. *Steps:* (1) define the period effect and show how the balanced sequences let you estimate it; (2) define a carryover check; (3) say what you would do if carryover were found. *Expected evidence:* definitions and a decision rule. *Rubric:* 3 = period effect estimated from within-analyst changes by order, carryover check compares rubric-first and usual-first analysts' usual periods, response honest (for example, report the first-period comparison as a parallel design with reduced precision); 2 = one check missing; 1 = assumptions named only; 0 = none.

**EX017 — Run and extend Lab 3.** *Objective:* use design analysis to size a study. *Inputs:* Lab 3. *Constraints:* offline; add lines, do not change the existing ones. *Steps:* (1) run it and record the output; (2) add a run of the crossover with 36 analysts and 8 high-impact cases per condition at the smallest effect of interest (0.30 versus 0.20); (3) report power and exaggeration; (4) recommend 24 or 36 analysts given that recruitment beyond 24 adds an estimated three months. *Expected evidence:* outputs and a recommendation. *Rubric:* 3 = outputs correct, recommendation weighs precision at the smallest effect against time and states what will be reported either way; 2 = recommendation by power alone; 1 = not run; 0 = none.

**EX018 — Ethics risk table.** *Objective:* identify and mitigate risks. *Inputs:* §3.4. *Constraints:* at least six risks. *Steps:* for each risk give likelihood, severity, mitigation and residual risk. *Expected evidence:* a table. *Rubric:* 3 = risks specific to analysts and security material (employment, coercion, re-identification, leakage, distress, data retention), mitigations concrete, residual risk honest; 2 = generic risks; 1 = fewer than four; 0 = none.

**EX019 — Pre-analysis plan.** *Objective:* fix the analysis before data. *Inputs:* §3.5. *Constraints:* one page; every outcome defined operationally. *Steps:* write the plan, including a rule for what counts as a deviation and how deviations are logged. *Expected evidence:* the plan. *Rubric:* 3 = outcomes, estimand, method, missing data, checks and robustness all specified, confirmatory and exploratory analyses separated; 2 = one element vague; 1 = a list of intentions; 0 = none.

**EX020 — Reproducible project.** *Objective:* set up a project another person could rerun. *Inputs:* §3.6. *Constraints:* data cannot be shared publicly. *Steps:* (1) write the README a stranger would need; (2) describe the synthetic stand-in dataset you will publish and how it preserves structure without disclosing anyone; (3) list what a reproducibility reviewer would need access to under agreement. *Expected evidence:* README and a paragraph. *Rubric:* 3 = README runnable step by step with versions and seeds, synthetic stand-in described concretely, restricted access defined; 2 = one gap; 1 = folder list only; 0 = none.

### Chapter synthesis

Design is the choice of counterfactual. Historical comparisons are vulnerable to everything that changed alongside the exposure; a controlled crossover tabletop removes stable differences between analysts at the cost of assumptions about carryover, periods and case sets, which must be balanced and checked. Size the study by simulation, reporting power, exaggeration and the false-positive rate at the smallest effect of interest. Treat ethics as design: analysts are participants whose performance data could harm them, and safeguards change recruitment, reporting and storage. Fix outcomes and analysis in a pre-analysis plan, and build a reproducible project before the first datum arrives.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 08

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Competing explanations of response outcomes

### Learning outcomes and connection

After this chapter you should be able to:

1. Apply the method of multiple working hypotheses to an incident-response outcome and write a rival table whose rows make *different* predictions.
2. Draw a causal diagram for a historical response dataset and identify confounders, mediators and variables you must not adjust for.
3. Use difference-in-differences, stratification and standardization to challenge a favoured claim, stating the assumption each relies on.
4. Design negative controls and sensitivity analyses that would embarrass the favoured explanation if it were wrong.
5. Explain why the historical strand of the Triage Rubric Study is reported as context, while the causal test is the controlled tabletop.

The chapter builds on the design choice of Chapter 3 and prepares Chapter 5, where the rival table becomes part of the proposal.

### 4.1 Multiple working hypotheses and strong inference

In 1890 the geologist T. C. Chamberlin warned that a researcher with a single favoured hypothesis comes to see only the evidence that supports it, and recommended holding several working hypotheses at once ([Chamberlin, reprinted 1965](https://doi.org/10.1126/science.148.3671.754)). [Platt (1964)](https://doi.org/10.1126/science.146.3642.347) turned the idea into **strong inference**: devise alternative hypotheses, devise an observation whose possible outcomes exclude one or more of them, carry it out, and repeat. The value of a rival is not that it is likely; it is that it predicts something different from your hypothesis, so that an observation can tell them apart.

In incident response, outcomes have many causes besides the practice being studied. When under-triage falls after a rubric is introduced, the candidates include the rubric, but also new staff, a change in the kinds of incidents arriving, a change in telemetry that makes impact more visible, a change in how severity is recorded, regression from an unusually bad period, attention from being studied, and plain chance. Your job is to list them, say what each predicts, and find data that discriminate.

### 4.2 The historical puzzle at MRSS (synthetic)

MRSS's East team adopted SEV-4 on 1 January 2025. Its under-triage of high-impact tickets — judged against a panel review of a random sample of tickets after closure — fell. West did not adopt the rubric. The MRSS manager's slide reads: "East under-triage 9% vs West 18%: the rubric halves missed incidents."

What else happened? In January 2025 East also absorbed three senior analysts from a closed contract, raising its share of senior analysts from about a third to about two-thirds. East also handles a different mix of incidents: more school-network alerts with noisy signals, fewer of the quiet-impact incidents (a scheduled job silently failing at the water authority, a payroll export copied to an unusual destination) that are easiest to under-rate.

### 4.3 A rival table

| Explanation | Mechanism | Prediction that differs from the rubric hypothesis | Data that discriminate |
|---|---|---|---|
| **H0: Rubric** | Structured questions force attention to impact | East improves *after* adoption relative to West; improvement concentrated in quiet-impact cases; misrouting unchanged | DiD on under-triage; subgroup by case type; negative-control outcome |
| **R1: Seniority** | Senior analysts under-triage less | Improvement tracks the share of senior analysts; also improves outcomes the rubric does not touch (routing) | Stratify by seniority; misrouting as negative control |
| **R2: Case mix** | East sees fewer hard, quiet cases | East lower than West even *before* adoption; difference shrinks after standardizing case type | Pre-period comparison; standardization |
| **R3: Secular trend** | Both teams improve with tooling, training or attention | West also improves; DiD smaller than the crude before–after change | West's change over the same period |
| **R4: Recording change** | Severity field or panel sampling changed in 2025 | Change appears in tickets but not in independent panel review; abrupt at a configuration date | Audit trail of field definitions; panel method unchanged |
| **R5: Regression to the mean** | Adoption followed a bad quarter | Pre-period unusually high relative to longer history | Longer pre-period series |
| **R6: Chance** | Sampling variation in a few hundred reviewed tickets | Interval includes zero; effect unstable across samples | Uncertainty intervals; resampling |

Two features make this table useful. Each row predicts something specific, and the last column names data that the study can actually obtain. A rival table that says only "confounding may exist" is not a rival table.

### 4.4 Causal diagrams

A **causal diagram** (a directed acyclic graph) draws variables as nodes and assumed causal effects as arrows. It is a compact way to state assumptions and to decide what to adjust for. Tools such as dagitty ([Textor et al. 2017](https://doi.org/10.1093/ije/dyw341)) check diagrams formally; for a master's project a careful hand drawing is enough.

```text
                 Team (East/West) ──────────────┐
                    │          │                 │
                    v          v                 v
   Contract closure → Seniority  Case mix (quiet share)   Rubric adoption
                    │          │                 │
                    └────┬─────┴─────────────────┘
                         v
                  Under-triage  <── Severity recording practice
                         │
                         v
                  Panel-reviewed outcome
```

Reading the diagram: seniority and case mix both affect under-triage and are associated with the team, and therefore with rubric adoption; they are **confounders** of the rubric–outcome relationship and must be accounted for. Recording practice affects the measured outcome; if it changed with adoption it is a confounder too, which is why the outcome is panel review rather than the ticket's own field. A variable that the rubric itself changes on the way to the outcome — for example, "time spent reading the asset inventory" — is a **mediator**; adjusting for it would remove part of the effect you want to estimate. A variable caused by both the rubric and the outcome (for example, "ticket later reopened") is a **collider**; adjusting for it can create spurious associations. The diagram is an assumption, not a finding: say where you are unsure.

### 4.5 Discriminating tools and their assumptions

- **Difference-in-differences (DiD)** compares the change in East with the change in West over the same period. It removes stable differences between teams and shocks common to both. It assumes **parallel trends**: without the rubric, East would have changed as West did. A co-intervention specific to East — the senior hires — violates that assumption.
- **Stratification and standardization** compute outcomes within strata of a confounder (senior/junior × quiet/noisy) and then reweight them to a common reference mix. They remove confounding by the measured variables, and only those. With many strata and few tickets per stratum, estimates become unstable.
- **Negative-control outcomes** are outcomes the exposure cannot plausibly affect but that share the confounders. If the rubric cannot affect routing errors but seniority can, a "rubric effect" on routing is evidence of confounding. A negative control does not prove the absence of bias when null, but a non-null one is a clear warning.
- **Sensitivity analysis** asks how strong an unmeasured confounder would have to be to explain away the estimate. At master's level a simple version is enough: "if the senior hires reduced under-triage by as much as seniority does in West, how much of East's DiD would remain?"
- **Simpson's paradox** — an association that reverses or vanishes when data are split by a third variable ([Simpson 1951](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x)) — is the extreme case of confounding by mix. It is a reminder that a crude comparison can point the wrong way.

### 4.6 Competing explanations in a documented study

The surgical safety checklist study of [Haynes et al. (2009)](https://doi.org/10.1056/NEJMsa0810119) reported lower complication and death rates after a checklist was introduced in eight hospitals. Its design — before and after, without a concurrent control group — is common in operational improvement work, and the rivals a reader must consider are exactly those in §4.3: secular improvement, changes in the case mix or recording, and the effect of being observed. The point here is not to judge that study, which later research has extended and debated; it is that the same reasoning applies whenever a security team reports "after adopting the playbook, metric X improved". The incident-response literature has few controlled studies, so the habit of asking "what else changed?" is a core research skill.

### 4.7 Worked example: building the rival table into the proposal (synthetic)

The student's first draft proposal said: "Historical data from MRSS show that the rubric halved under-triage." Her supervisor asked for the rival table. Working through it changed three things.

First, the historical strand was **demoted**: its role became to describe the problem (under-triage of quiet-impact incidents occurs and matters) and to test whether the historical data are *consistent with* a rubric effect after accounting for seniority and case mix — not to estimate the effect. Second, the controlled tabletop became the **primary causal test**, because its design breaks the link between rubric use and seniority (each analyst uses both conditions) and between rubric use and case mix (case sets are matched and counterbalanced). Third, the tabletop inherited a prediction from the rival table: if the rubric works by drawing attention to impact, its effect should be concentrated in quiet-impact cases. That subgroup analysis was predeclared.

### 4.8 Practical activity: the rubric, the senior hires and the case mix

Lab 4 generates synthetic panel-reviewed high-impact tickets for East and West in 2024 and 2025 (1,500 per team per year). The generator encodes a true rubric effect of −3 percentage points in East in 2025, a seniority effect of −10 points, a quiet-impact effect of +22 points and a small improvement in both teams in 2025. Routing errors depend on seniority but not on the rubric. Save it as `lab4_rivals.py`.

```python
# Lab 4 - competing explanations for a fall in under-triage after a rubric was adopted (offline, stdlib only)
# Synthetic historical tickets from two fictional teams at Marlow Regional Shared Services (MRSS).
# East adopted the SEV-4 rubric on 2025-01-01 and, in the same month, gained senior analysts; West changed nothing.
# Only high-impact tickets (panel-reviewed reference severity 3-4) are generated; outcome = under-triaged (0/1).
import random
def make_tickets(seed=404, rubric_effect=-0.03):
    rng = random.Random(seed); rows = []
    for team in ("East", "West"):
        for year in (2024, 2025):
            n = 1500
            senior_share = {("East", 2024): 0.35, ("East", 2025): 0.65,
                            ("West", 2024): 0.35, ("West", 2025): 0.38}[(team, year)]
            quiet_share = {"East": 0.40, "West": 0.55}[team]          # quiet-impact cases are harder
            for _ in range(n):
                senior = rng.random() < senior_share
                quiet = rng.random() < quiet_share
                p = 0.10 + (0.22 if quiet else 0) + (-0.10 if senior else 0) + (-0.02 if year == 2025 else 0)
                if team == "East" and year == 2025:
                    p += rubric_effect
                under = rng.random() < max(p, 0.01)
                misrouted = rng.random() < (0.08 if senior else 0.14)   # rubric does not touch routing
                rows.append(dict(team=team, year=year, senior=senior, quiet=quiet, under=under, misrouted=misrouted))
    return rows
def rate(rows, key="under", **f):
    s = [r for r in rows if all(r[k] == v for k, v in f.items())]
    return sum(r[key] for r in s) / len(s), len(s)
if __name__ == "__main__":
    T = make_tickets()
    e25, _ = rate(T, team="East", year=2025); w25, _ = rate(T, team="West", year=2025)
    e24, _ = rate(T, team="East", year=2024); w24, _ = rate(T, team="West", year=2024)
    print(f"A crude 2025 contrast   East {e25:.3f}  West {w25:.3f}  difference {e25 - w25:+.3f}")
    print(f"B East before/after     2024 {e24:.3f}  2025 {e25:.3f}  change {e25 - e24:+.3f}")
    print(f"C difference-in-diff    East change {e25 - e24:+.3f} minus West change {w25 - w24:+.3f} = {(e25 - e24) - (w25 - w24):+.3f}")
    # D: stratify by seniority and case type, then standardize to the pooled 2024 mix (both teams)
    base = [r for r in T if r["year"] == 2024]
    strata = [(s, q) for s in (False, True) for q in (False, True)]
    w = {k: sum(1 for r in base if (r["senior"], r["quiet"]) == k) / len(base) for k in strata}
    def std(team, year):
        return sum(w[k] * rate(T, team=team, year=year, senior=k[0], quiet=k[1])[0] for k in strata)
    sd = (std("East", 2025) - std("East", 2024)) - (std("West", 2025) - std("West", 2024))
    print(f"D standardized DiD      (seniority x case type held at the 2024 mix) = {sd:+.3f}")
    em25, _ = rate(T, "misrouted", team="East", year=2025); em24, _ = rate(T, "misrouted", team="East", year=2024)
    wm25, _ = rate(T, "misrouted", team="West", year=2025); wm24, _ = rate(T, "misrouted", team="West", year=2024)
    print(f"E negative control      misrouting DiD = {(em25 - em24) - (wm25 - wm24):+.3f}  (rubric cannot affect routing)")
    print(f"  senior share          East 2024 {rate(T, 'senior', team='East', year=2024)[0]:.2f} -> 2025 {rate(T, 'senior', team='East', year=2025)[0]:.2f};"
          f"  West {rate(T, 'senior', team='West', year=2024)[0]:.2f} -> {rate(T, 'senior', team='West', year=2025)[0]:.2f}")
    print(f"  quiet-impact share    East {rate(T, 'quiet', team='East')[0]:.2f}  West {rate(T, 'quiet', team='West')[0]:.2f}")
    print(f"  generator truth       rubric effect on East 2025 = -0.030 (absolute risk)")
```

Expected output:

```text
A crude 2025 contrast   East 0.093  West 0.179  difference -0.086
B East before/after     2024 0.159  2025 0.093  change -0.066
C difference-in-diff    East change -0.066 minus West change -0.013 = -0.053
D standardized DiD      (seniority x case type held at the 2024 mix) = -0.038
E negative control      misrouting DiD = -0.017  (rubric cannot affect routing)
  senior share          East 2024 0.34 -> 2025 0.65;  West 0.33 -> 0.38
  quiet-impact share    East 0.42  West 0.55
  generator truth       rubric effect on East 2025 = -0.030 (absolute risk)
```

How to read it. The manager's crude 2025 comparison (A) says the rubric is associated with an 8.6-point reduction; East's before–after change (B) says 6.6 points. Both mix the rubric with other things. The crude contrast is inflated by case mix: East handles fewer quiet-impact cases (42% versus 55%), so it would have lower under-triage without any rubric. The before–after change includes the improvement common to both teams. Difference-in-differences (C) removes the common change and the stable team difference, giving −5.3 points — still too large, because East's senior hires are an East-specific co-intervention that DiD cannot remove. Standardizing to the 2024 mix of seniority and case type (D) gives −3.8 points, close to the generator's true −3.0. The negative-control outcome (E) is the warning light: misrouting, which the rubric cannot affect, shows a "DiD effect" of −1.7 points in East — exactly what an East-specific seniority change would produce. Note also that even with 1,500 tickets per team per year the remaining gap between D and the truth is within sampling noise; with the few hundred tickets a real panel could review, the DiD would be imprecise as well as biased.

The conclusion the student writes is calibrated: "The historical data are consistent with a modest rubric effect after accounting for seniority and case mix, but they cannot separate the rubric from the simultaneous senior hires with confidence; the negative-control outcome indicates residual confounding. The causal question is therefore addressed by the controlled study."

### 4.9 The tabletop as the answer to the rival table

Return to the rival table and ask what the crossover tabletop does to each row. R1 (seniority) and R2 (case mix) are broken by design: every analyst does both conditions on matched case sets. R3 (secular trend) becomes a period effect, balanced by order and estimable. R4 (recording) is controlled because the outcome is computed from the analyst's rating against a fixed reference, not from a ticket field. R5 (regression to the mean) does not arise, because nobody was selected for a bad period. R6 (chance) remains and is handled with intervals. New rivals appear that the historical data did not have: carryover, observers' expectations, participants guessing the hypothesis, and the artificiality of fictional cases. The tabletop does not abolish rivals; it trades a set it cannot control for a set it can.

### 4.10 Common errors and limits

- Listing "confounding" as a limitation instead of naming confounders and what they predict.
- Writing rivals that make the same predictions as the favoured hypothesis, so that no observation could separate them.
- Treating DiD as a cure for confounding when a co-intervention is specific to the treated group.
- Adjusting for mediators or colliders because "more adjustment is safer".
- Using the ticket's own severity field as the outcome when recording practice may have changed.
- Ignoring a non-null negative control because the main result looks good.
- Concluding "no confounding" from a null negative control.

The limit is that observational adjustment handles only what you measured and modelled correctly. That is why a design that removes rivals by construction is worth its artificiality for a causal question — and why its own new rivals must be listed too.

### Exercises — chapter 4

**EX021 — Rival table for a different claim.** *Objective:* write discriminating rivals. *Inputs:* the claim "after MRSS moved to 12-hour shifts, mean time to contain fell by 20%". *Constraints:* at least five rivals; each with a distinct prediction. *Steps:* complete the four columns of §4.3 for each. *Expected evidence:* a table. *Rubric:* 3 = rivals specific (case mix, staffing level, tooling, recording of "contained", censoring, regression), predictions distinct and data obtainable; 2 = one rival non-discriminating; 1 = generic; 0 = none.

**EX022 — Causal diagram.** *Objective:* encode assumptions and adjustment decisions. *Inputs:* §4.4. *Constraints:* add two variables: "telemetry coverage of the affected service" and "ticket reopened". *Steps:* (1) redraw the diagram with them; (2) classify every variable as confounder, mediator, collider or other with respect to rubric → under-triage; (3) state the adjustment set. *Expected evidence:* the diagram and a table. *Rubric:* 3 = telemetry correctly placed (a confounder if it differs by team and affects triage, or an effect modifier), reopened identified as a collider or post-outcome variable not to adjust for, adjustment set justified; 2 = one misclassification; 1 = diagram without reasoning; 0 = none.

**EX023 — Run and modify Lab 4.** *Objective:* see when DiD works. *Inputs:* Lab 4. *Constraints:* offline. *Steps:* (1) run it; (2) change East's 2025 senior share from 0.65 to 0.38 (the same as West's), rerun and report lines A–E; (3) explain why DiD and standardized DiD now agree with each other and with the truth more closely; (4) explain what happened to the negative control. *Expected evidence:* outputs and a 150-word explanation. *Rubric:* 3 = outputs correct, the parallel-trends logic explained, negative control's movement towards zero linked to removing the co-intervention; 2 = one error; 1 = not run; 0 = none.

**EX024 — Negative controls.** *Objective:* design negative controls for the tabletop. *Inputs:* the tabletop design of Chapter 3. *Constraints:* at least two negative controls, one outcome and one exposure. *Steps:* for each, state what it is, why the rubric cannot affect it (or why it cannot be the cause), and what a non-null result would mean. *Expected evidence:* a half page. *Rubric:* 3 = controls plausible (for example, accuracy on a set of identification questions unrelated to severity; a "sham" condition with an unrelated checklist), interpretation of non-null results specific; 2 = one control implausible; 1 = definitions only; 0 = none.

**EX025 — Sensitivity statement.** *Objective:* reason about unmeasured confounding. *Inputs:* Lab 4 output; suppose seniority were *unmeasured*. *Constraints:* use only numbers from the lab or the generator description. *Steps:* (1) estimate how much of DiD (C) the senior hires could explain, given a seniority effect of −10 points and the change in East's senior share relative to West's; (2) state what remains; (3) write a two-sentence sensitivity statement. *Expected evidence:* the calculation and statement. *Rubric:* 3 = calculation ≈ −10 × (0.31 − 0.05) ≈ −2.6 points, remainder ≈ −2.7 points, statement calibrated; 2 = arithmetic slip; 1 = no number; 0 = none.

**EX026 — Rivals for the tabletop.** *Objective:* list the rivals a controlled design introduces. *Inputs:* §4.9. *Constraints:* at least four rivals specific to the tabletop. *Steps:* for each, give its prediction, a mitigation in the protocol and a check in the analysis. *Expected evidence:* a table. *Rubric:* 3 = carryover, observer expectation, demand characteristics, fidelity failure and artificiality covered with concrete checks; 2 = one missing check; 1 = names only; 0 = none.

### Chapter synthesis

An outcome that improves after a change has many possible causes. Hold several working hypotheses, and write each as a mechanism with a distinct prediction and data that can test it. Draw a causal diagram to decide what to adjust for, and avoid adjusting for mediators and colliders. Difference-in-differences removes common shocks and stable differences but not co-interventions; standardization removes only measured confounding; negative controls warn of what remains. When the historical data cannot separate the favoured explanation from its rivals, say so and choose a design that breaks the links — then list the new rivals that design introduces.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 08

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot of a bounded incident study

### Learning outcomes and connection

After this chapter you should be able to:

1. Write a research proposal that works as a contract between student, supervisor, ethics committee and partners: what will be done, how it will be judged and what happens if it cannot be done.
2. Build a timeline around its critical path and a risk register with owners and triggers.
3. Design a feasibility pilot whose objectives are recruitment, procedure and measurement — not the effect.
4. Predeclare progression criteria with go, amend and stop thresholds, and audit pilot data against them.
5. Record protocol deviations and instrument revisions with an audit trail, and state the stop rules for the main study.

The chapter builds on the design (Chapter 3) and rival table (Chapter 4) and prepares Chapter 6, where the revised instruments collect the main-study data.

### 5.1 The proposal as a contract

A master's proposal is often treated as a formality before "the real work". It is better understood as a contract. It tells the supervisor what will be delivered and when; it tells the ethics committee exactly what participants will experience; it tells partner organizations what will be asked of them and what they will receive; and it tells examiners, later, what the student committed to before seeing data. A proposal that is vague in any of these directions will be renegotiated under pressure, usually at the expense of rigour.

A proposal for the Triage Rubric Study has these parts:

| Section | Content | Why it matters |
|---|---|---|
| Problem and question | The MRSS decision, RQ1–RQ3, estimand, claim scope | Fixes what success means |
| Background | Concept matrix summary, competing models, gap | Shows the question is not already answered |
| Design | Crossover tabletop; historical strand as context | Shows why this design answers this question |
| Participants and recruitment | Eligibility, neutral channels, target 24, allocation | Ethics and feasibility |
| Materials | 24 main cases plus pilot cases, rubric, observer form, debrief guide | Lets others replicate |
| Measures and analysis | Pre-analysis plan (Chapter 3) | Separates confirmation from exploration |
| Rivals | Rival table and checks (Chapter 4) | Shows what the design rules out and what it does not |
| Pilot | Objectives and progression criteria | Protects the main study |
| Ethics and data | Approval route, safeguards, data management plan | Protects participants |
| Timeline and risks | Critical path, risk register | Protects the schedule |
| Outputs | Dissertation, reproducibility package, partner briefing | Defines delivery |

### 5.2 Timeline and critical path

The **critical path** is the chain of tasks whose delay delays the whole project. In empirical master's projects it is rarely the analysis; it is approvals, recruitment and access. For the Triage Rubric Study:

```text
Month  1-2   question, review, design                 (supervisor sign-off)
Month  3     ethics application submitted             ── critical: approval 6-10 weeks
Month  3-4   case writing, panel reference ratings    ── critical: panel availability
Month  5     pilot (10 sessions)                      ── depends on approval + cases
Month  6     pilot report, instrument revision, amendment if needed
Month  7-9   main-study recruitment and 24 sessions   ── critical: recruitment rate
Month  9-10  debrief interviews, transcription
Month 10-12  analysis per pre-analysis plan
Month 12-16  writing, internal review, submission
Month 17-18  examination, corrections, partner briefing
```

Build slack after each critical task. If ethics approval takes ten weeks instead of six, the pilot moves, not the analysis plan.

### 5.3 The risk register

| Risk | Likelihood | Impact | Trigger | Response | Owner |
|---|---|---|---|---|---|
| Recruitment below 24 | Medium | High | Fewer than 12 enrolled by end of month 8 | Add second channel; extend one month; report precision achieved | Student |
| Panel disagreement on reference severity | Medium | Medium | Any case without consensus after discussion | Revise vignette or drop case before main study; record | Supervisor |
| Ethics amendment needed after pilot | High | Medium | Any change to procedure affecting participants | Submit amendment; do not start main study until approved | Student |
| Observer unavailability | Low | Medium | Fewer than two observers for a session | Single observer with audio time stamps | Student |
| Case leakage between participants | Medium | High | Participant mentions specific case content to colleague | Ask participants not to discuss; record sessions dates; check performance by date | Student |
| Data loss | Low | High | Storage failure | Encrypted institutional storage with backup; raw exports read-only | Student |

A risk register is useful only if the triggers are observable and the responses decided in advance.

### 5.4 What a pilot is for

A **pilot study** is a small version of the main study run to find out whether the main study can be done as planned. Its objectives are feasibility and process: can participants be recruited at the expected rate? Do they complete sessions? Are the instructions understood? Are the cases clear? Do the observers' forms capture what is needed? Can two observers agree on when a decision was made? Is the session length acceptable? [Thabane et al. (2010)](https://doi.org/10.1186/1471-2288-10-1) set out these purposes and warn against the most common misuse: treating the pilot as a small trial and estimating the effect. Effect estimates from a pilot are extremely imprecise, and a pilot that "finds no effect" may lead a team to abandon a good intervention, while one that finds a large effect invites an under-sized main study. The [CONSORT extension for pilot and feasibility trials](https://doi.org/10.1136/bmj.i5239) (Eldridge et al. 2016) gives a reporting framework that makes these objectives explicit.

How large should a pilot be? There is no universal number; it depends on what the pilot must estimate. [Hertzog (2008)](https://doi.org/10.1002/nur.20247) discusses how precision of feasibility estimates grows with pilot size. Ten sessions are enough to see whether procedures break and whether observers agree on a reasonable number of timing pairs; they are not enough to estimate a completion rate precisely, and the pilot report says so.

#### 5.4.1 What the Triage Rubric pilot measures

- **Completion:** proportion of booked participants who complete a session.
- **Field completeness:** proportion of required observer fields (two times and the severity rating) recorded.
- **Timing agreement:** proportion of decisions where the two observers' times are within 30 seconds.
- **Case clarity:** number of participants who flag each case as unclear.
- **Session length:** minutes per session, against a 90-minute limit agreed with the ethics committee.

The pilot uses its own six cases (C1–C6), not the main-study cases, so that main-study materials are not exposed and pilot participants can, if eligible, be excluded from the main study without wasting cases. It records ratings, but nobody computes a rubric effect from them.

### 5.5 Progression criteria

**Progression criteria** are thresholds, set before the pilot, that decide whether the main study proceeds as planned (**go**), proceeds after changes (**amend**) or does not proceed in its current form (**stop**). A traffic-light form is common: green above a threshold, amber between two, red below. The thresholds come from the main study's needs: if the main study needs 90% field completeness to compute its outcomes without heavy imputation, that is the green threshold.

| Criterion | Go (green) | Amend (amber) | Stop (red) |
|---|---|---|---|
| Completion | ≥ 0.80 | 0.60–0.79 | < 0.60 |
| Field completeness | ≥ 0.90 | 0.80–0.89 | < 0.80 |
| Timing agreement (±30 s) | ≥ 0.80 | 0.60–0.79 | < 0.60 |
| Unclear flags per case | ≤ 3 | 4–5 | > 5 (that case cannot be used unrevised) |
| Sessions over 90 minutes | none | 1–2 | > 2 |

"Stop" on a case-level criterion stops that case, not the study.

### 5.6 Practical activity: auditing ten pilot sessions

Lab 5 audits ten synthetic pilot sessions with incomplete observer notes against the criteria. One participant (P04) stopped after three cases. Save it as `lab5_pilot.py`.

```python
# Lab 5 - audit ten pilot tabletop sessions against predeclared progression criteria (offline, stdlib only)
# Synthetic pilot: ten volunteer analysts (P01-P10), each triaging 6 fictional cases while two observers time
# the severity decision. None = field left blank on the observer sheet. No outcome comparison is made here.
SESSIONS = {  # pid: (completed, minutes, [(case, o1_seconds, o2_seconds, severity_recorded, unclear_flag)])
 "P01": (True, 74, [("C1", 210, 205, 3, 0), ("C2", 95, 100, 2, 0), ("C3", 330, 290, 4, 1), ("C4", 150, 152, 1, 0), ("C5", 260, 255, 3, 0), ("C6", 120, 118, 2, 0)]),
 "P02": (True, 81, [("C1", 240, None, 3, 0), ("C2", 110, 112, 2, 0), ("C3", 410, 400, 3, 1), ("C4", 140, 141, 1, 0), ("C5", 300, 240, 4, 0), ("C6", 90, 95, 2, 0)]),
 "P03": (True, 69, [("C1", 180, 176, 2, 0), ("C2", 85, 88, 2, 0), ("C3", 290, 300, 4, 0), ("C4", 160, 158, 1, 0), ("C5", 230, 228, 3, 0), ("C6", 100, 99, 1, 0)]),
 "P04": (False, 35, [("C1", 260, 255, 3, 0), ("C2", 130, None, None, 0), ("C3", None, None, None, 1)]),
 "P05": (True, 96, [("C1", 300, 290, 3, 0), ("C2", 140, 139, 2, 0), ("C3", 520, 470, 4, 1), ("C4", 170, 172, 1, 0), ("C5", 340, 335, 3, 1), ("C6", 150, 150, 2, 0)]),
 "P06": (True, 77, [("C1", 200, 201, 3, 0), ("C2", 100, None, 2, 0), ("C3", 350, 345, 3, 1), ("C4", 145, 146, 1, 0), ("C5", 275, 210, 3, 0), ("C6", 115, 117, 2, 0)]),
 "P07": (True, 72, [("C1", 220, 222, 3, 0), ("C2", 90, 91, 2, 0), ("C3", 310, 305, 4, 0), ("C4", 150, None, 1, 0), ("C5", 250, 251, 4, 0), ("C6", 105, 104, 2, 0)]),
 "P08": (True, 88, [("C1", 250, 248, 3, 0), ("C2", 120, 119, 2, 0), ("C3", 380, 330, 3, 1), ("C4", 155, 154, 1, 0), ("C5", 280, 279, 3, 0), ("C6", 110, 108, 2, 0)]),
 "P09": (True, 70, [("C1", 190, 189, 3, 0), ("C2", 80, 82, 2, 0), ("C3", 300, 302, 4, 0), ("C4", 140, 140, 1, 0), ("C5", 240, 239, 3, 0), ("C6", 95, 96, 2, 0)]),
 "P10": (True, 84, [("C1", 230, None, 3, 0), ("C2", 105, 107, None, 0), ("C3", 360, 355, 4, 1), ("C4", 150, 149, 1, 0), ("C5", 290, 230, 3, 0), ("C6", 100, 101, 2, 0)]),
}
CRITERIA = {"completion": 0.80, "completeness": 0.90, "timing_agreement": 0.80, "max_unclear_per_case": 3, "max_minutes": 90}
done = {p: s for p, s in SESSIONS.items() if s[0]}
completion = len(done) / len(SESSIONS)
fields = [v for _, _, rows in done.values() for r in rows for v in r[1:4]]
completeness = sum(v is not None for v in fields) / len(fields)
pairs = [(r[1], r[2], r[0]) for _, _, rows in done.values() for r in rows if r[1] is not None and r[2] is not None]
agree = sum(abs(a - b) <= 30 for a, b, _ in pairs) / len(pairs)
unclear = {}
for _, _, rows in SESSIONS.values():
    for r in rows:
        unclear[r[0]] = unclear.get(r[0], 0) + r[4]
over = {p: s[1] for p, s in done.items() if s[1] > CRITERIA["max_minutes"]}
def verdict(ok, near): return "GO" if ok else ("AMEND" if near else "STOP")
print(f"completion        {len(done)}/{len(SESSIONS)} = {completion:.2f}  (>= {CRITERIA['completion']:.2f})  {verdict(completion >= 0.80, completion >= 0.60)}")
print(f"field completeness {sum(v is not None for v in fields)}/{len(fields)} = {completeness:.3f}  (>= 0.90)  {verdict(completeness >= 0.90, completeness >= 0.80)}")
print(f"timing agreement  {sum(abs(a - b) <= 30 for a, b, _ in pairs)}/{len(pairs)} pairs within 30 s = {agree:.3f}  (>= 0.80)  {verdict(agree >= 0.80, agree >= 0.60)}")
bad = sorted({c for a, b, c in pairs if abs(a - b) > 30})
print(f"  disagreements concentrated in cases: {', '.join(bad)}")
print(f"unclear flags     " + "  ".join(f"{c}:{n}" for c, n in sorted(unclear.items())) + f"  (<= 3 per case)  {verdict(max(unclear.values()) <= 3, max(unclear.values()) <= 5)}")
print(f"session length    over 90 min: {', '.join(f'{p} ({m})' for p, m in over.items()) or 'none'}  {verdict(not over, len(over) <= 2)}")
miss_by_field = [sum(r[i] is None for _, _, rows in done.values() for r in rows) for i in (1, 2, 3)]
print(f"blank fields among completed sessions: observer-1 time {miss_by_field[0]}, observer-2 time {miss_by_field[1]}, severity {miss_by_field[2]}")
```

Expected output:

```text
completion        9/10 = 0.90  (>= 0.80)  GO
field completeness 157/162 = 0.969  (>= 0.90)  GO
timing agreement  44/50 pairs within 30 s = 0.880  (>= 0.80)  GO
  disagreements concentrated in cases: C3, C5
unclear flags     C1:0  C2:0  C3:7  C4:0  C5:1  C6:0  (<= 3 per case)  STOP
session length    over 90 min: P05 (96)  AMEND
blank fields among completed sessions: observer-1 time 0, observer-2 time 4, severity 1
```

How to read it. Completion (9 of 10) and field completeness (157 of 162 fields in completed sessions) are green. Timing agreement is green overall (44 of 50 complete pairs within 30 seconds), but every disagreement is in cases C3 and C5 — the two cases where a participant could reasonably "decide" at more than one moment (C3 invites a provisional rating, then revision after reading the asset note; C5 has a late inject). That is a measurement problem, not an observer problem: the observer form does not define *which* decision moment to time. Case C3 is flagged unclear by seven participants: red at case level, so C3 cannot be used unrevised. One session ran over 90 minutes (P05, 96), which is amber. The blank fields are not random: four of the five are observer 2's time, which suggests observer 2's form layout (the time box sits on a second page) rather than inattention. P04's incomplete session is excluded from completeness figures by rule but reported, with the reason the participant gave (a work call), in the pilot report.

### 5.7 Worked example: the pilot report and protocol revision (synthetic)

*Decision: amend, then go.* The pilot report lists each criterion, the result, and the change made.

| Finding | Change | Deviation log entry |
|---|---|---|
| Timing disagreements concentrated in C3, C5 | Define the timed decision as the *first written severity on the answer sheet*; revisions are recorded separately as a secondary measure | Instrument v1.1, dated, before main study |
| C3 flagged unclear by 7 of 10 | Rewrite C3's asset note so impact is stated, not implied; re-rate with the panel; main-study cases checked for the same ambiguity | Case revision, panel re-rating recorded |
| Observer 2 left time blank 4 times | Move both time fields to the first page; add a completeness check by the facilitator before the next case | Observer form v1.1 |
| One session 96 min | Reduce main-study sessions to 12 cases per period with a 10-minute break; total under 90 minutes in pilot timing | Ethics amendment submitted (session structure) |
| P04 stopped for work reasons | Book sessions outside on-call duties; add a sentence on rescheduling to the information sheet | Information sheet v1.1 |

The report states explicitly: "No effect of the rubric was estimated from pilot data. Ratings were checked only for recording completeness." The main study starts after the ethics amendment is approved.

### 5.8 Protocol deviations and instrument revisions

A **protocol deviation** is any departure from the approved protocol: a session run with one observer, a participant who used the rubric sheet in a usual session, a case shown out of order. Record each with date, participant code, what happened, why, and whether it affects the primary outcome. A deviation is not a failure; an unrecorded deviation is. Instrument revisions get version numbers, and every datum records the instrument version that produced it. Changes made *after* main-study data have been seen require particular care: log whether the change could have been influenced by the data, and if so treat any analysis affected by it as exploratory.

### 5.9 Stop rules for the main study

Even a well-piloted study needs **stop rules**: conditions under which the main study is paused or ended. For this study they are: (1) a participant reports distress attributable to the session (pause and review with the ethics committee); (2) evidence of case leakage between participants (pause, investigate, possibly replace cases); (3) a fidelity failure rate above 10% of sessions (pause and retrain facilitators); (4) recruitment below six participants after two months of the recruitment window (consult supervisor; extend or report as an under-powered study with precision stated). There is no stop rule for "the effect looks small" — interim looks at the outcome are not planned and would compromise the analysis.

### 5.10 Common errors and limits

- Treating the proposal as a formality and leaving partners, ethics and examiners with different understandings of the study.
- Planning around the analysis and discovering that approvals and recruitment were the critical path.
- Writing a risk register without triggers or decided responses.
- Estimating the effect from the pilot, or using it to decide whether to continue.
- Setting progression criteria after seeing pilot results.
- Treating observer disagreement as carelessness when it reveals an undefined measurement moment.
- Revising instruments without version numbers, so that main-study data cannot be linked to the instrument that produced them.

The limit of a pilot is that it is small. It can reveal that something does not work; it cannot prove that everything will.

### Exercises — chapter 5

**EX027 — Proposal summary.** *Objective:* write the contract. *Inputs:* the section table in §5.1 and your answers to earlier exercises. *Constraints:* one page; every section present in one or two sentences. *Steps:* write it for the Triage Rubric Study, ending with a sentence on what will be reported if the main study recruits only 16 analysts. *Expected evidence:* the summary. *Rubric:* 3 = all sections present and consistent with the estimand, design and rivals; fallback stated honestly; 2 = one section vague; 1 = background-heavy; 0 = none.

**EX028 — Critical path and risk register.** *Objective:* protect the schedule. *Inputs:* §5.2–5.3. *Constraints:* add two risks not in the table. *Steps:* (1) identify the critical path and slack; (2) add two risks with observable triggers and decided responses; (3) say what happens to the analysis plan if the schedule slips by two months. *Expected evidence:* a timeline and table. *Rubric:* 3 = critical path correct (ethics → cases/panel → pilot → recruitment), new risks realistic (for example, a key panel member leaves; a rubric revision is requested by a partner), plan unchanged by slippage; 2 = triggers vague; 1 = generic; 0 = none.

**EX029 — Run and modify Lab 5.** *Objective:* audit pilot data and see how criteria respond. *Inputs:* Lab 5. *Constraints:* offline. *Steps:* (1) run it; (2) suppose observer 2 had recorded every blank time correctly, with the value equal to observer 1's: edit the four blanks in completed sessions accordingly and rerun; (3) report how completeness and timing agreement change; (4) explain why the C3/C5 conclusion does not change. *Expected evidence:* outputs and a paragraph. *Rubric:* 3 = completeness rises to 161/162, timing pairs rise to 54 with 48 within 30 s (0.889), the C3/C5 diagnosis unchanged and explained; 2 = one error; 1 = not run; 0 = none.

**EX030 — Progression criteria for a different pilot.** *Objective:* derive thresholds from main-study needs. *Inputs:* a pilot of a playbook-format study where participants must complete a 20-item knowledge test before and after. *Constraints:* at least four criteria. *Steps:* for each criterion, give green/amber/red thresholds and the main-study requirement that justifies each green threshold. *Expected evidence:* a table. *Rubric:* 3 = thresholds justified by main-study needs (for example, completion needed for precision; item completeness needed for scoring), case- or item-level stops distinguished from study-level; 2 = thresholds arbitrary; 1 = criteria without thresholds; 0 = none.

**EX031 — Deviation log.** *Objective:* record deviations properly. *Inputs:* three events in the main study: (a) session A09 ran with one observer; (b) analyst A14 kept the rubric sheet on the desk during the usual period and said they "glanced at it twice"; (c) case C19 was shown before C18 to analyst A20. *Constraints:* use the fields in §5.8. *Steps:* write the three entries and, for each, say whether and how it affects the primary analysis. *Expected evidence:* the log and a paragraph. *Rubric:* 3 = entries complete, (b) recognized as a fidelity failure affecting the primary outcome with a predeclared sensitivity analysis, (a) and (c) judged minor with reasons; 2 = one judgement unsupported; 1 = entries incomplete; 0 = none.

**EX032 — The pilot report paragraph.** *Objective:* report a pilot without estimating an effect. *Inputs:* Lab 5 output and §5.7. *Constraints:* 200 words; no rubric effect estimated. *Steps:* write the report's results paragraph and its decision statement. *Expected evidence:* the paragraph. *Rubric:* 3 = each criterion reported with numerator, denominator and verdict, measurement diagnosis explained, decision linked to changes; explicit statement that no effect was estimated; 2 = verdicts without numbers; 1 = effect discussed; 0 = none.

### Chapter synthesis

A proposal is a contract: it fixes the question, design, measures, rivals, ethics and outputs before data. Plan around the critical path of approvals, materials and recruitment, and keep a risk register with observable triggers. A pilot tests feasibility and measurement, never the effect. Predeclare progression criteria with go, amend and stop thresholds, audit the pilot against them, and read disagreement and missingness as diagnostics of the instruments. Record every deviation and revision with versions and dates, and set stop rules that protect participants and data, not the hoped-for result.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 08

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Reproducible collection and outcome analysis

### Learning outcomes and connection

After this chapter you should be able to:

1. Write a data dictionary and cleaning log that let another person trace every derived value to its raw source.
2. Carry out the predeclared paired analysis of a crossover study with a bootstrap interval and a permutation test, and check period effects.
3. Report secondary outcomes — time, over-triage and agreement with a reference standard — so that costs are visible beside benefits.
4. Test alternative outcome definitions and say what robustness does and does not show.
5. Analyse debrief interviews thematically, check coding consistency and integrate the two strands in a joint display.

The chapter builds on the revised instruments of Chapter 5 and prepares Chapter 7, where results become claims.

### 6.1 Collecting data with lineage

Every value in the analysis should have a **lineage**: where it came from, what was done to it and by which code. Three documents make that possible.

The **data dictionary** defines each variable:

| Variable | Type | Values | Source | Notes |
|---|---|---|---|---|
| `analyst` | string | A01–A24 | Allocation list | Pseudonym; key held separately |
| `seq` | integer | 1–4 | Allocation list | Sequence of condition and case set (§3.1.2) |
| `period` | integer | 1, 2 | Session sheet | Order within session |
| `cond` | string | U, R | Session sheet | U = usual, R = SEV-4 rubric |
| `case` | string | C01–C24 | Answer sheet | Set A = C01–C12, set B = C13–C24 |
| `ref` | integer | 1–4 | Panel consensus file v1.1 | Fixed before main study |
| `quiet` | 0/1 | | Case design file | 1 = quiet-impact case |
| `rating` | integer | 1–4 | Answer sheet, first written severity | Defined in observer form v1.1 |
| `seconds` | integer | > 0 | Observer 1 time | Observer 2 time used for agreement checks |

The **cleaning log** records every transformation in order, with the script that performed it and the number of rows affected: "Step 3: removed 12 rows of A17 period 2 placeholders (withdrawal); script `clean.py` line 41; rows 576 → 564." The **raw data** are kept read-only. A reader with the raw files, the code and the log should arrive at exactly the analysis dataset.

### 6.2 The main-study data (synthetic)

Twenty-four analysts enrolled and were allocated in order to the four sequences. Analyst A17 withdrew after period 1 for personal reasons, giving 23 analysts with both periods. Each completed period has twelve decisions, of which eight are on high-impact cases. The generator below produces the synthetic dataset; in a real study this file would be replaced by the cleaned export, and the analysis script would be unchanged. The generator encodes these assumptions, which you should treat as the "truth" of the synthetic world: analysts differ in a stable bias; quiet-impact cases are under-rated by about one severity level under usual judgement and by about 0.4 levels with the rubric; noisy cases are unaffected by the rubric; there is a small practice effect in period 2; and the rubric increases decision time by about 18%. Save it as `lab6_data.py`.

```python
# lab6_data.py - generator for the synthetic main study of the Triage Rubric Study (offline, stdlib only)
# Save under this name: Lab 6 and Lab 8 import make_study() from it. Every value is fictional.
# 24 volunteer analysts (A01-A24) triage 24 fictional cases: set A (C01-C12) and set B (C13-C24), each with
# eight high-impact cases (reference severity 3-4), half of them "quiet" (high business impact, low alert noise).
# Four sequences balance case set and condition order: U = usual judgement, R = SEV-4 rubric.
import random
SEQUENCES = {1: (("U", "A"), ("R", "B")), 2: (("U", "B"), ("R", "A")),
             3: (("R", "A"), ("U", "B")), 4: (("R", "B"), ("U", "A"))}
def make_cases(seed=11):
    rng = random.Random(seed); cases = {}
    for s, offset in (("A", 0), ("B", 12)):
        refs = [4, 4, 3, 3, 4, 3, 3, 3, 2, 2, 1, 1]
        quiet = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
        for i, (ref, q) in enumerate(zip(refs, quiet)):
            cases[f"C{offset + i + 1:02d}"] = dict(set=s, ref=ref, quiet=q, base_s=rng.uniform(150, 330))
    return cases
def make_study(seed=2031, withdrawn=("A17",), quiet_usual=-1.0, quiet_rubric=-0.4, period2=0.1, noise=0.55):
    rng = random.Random(seed); cases = make_cases(); rows = []
    for a in range(1, 25):
        aid = f"A{a:02d}"; seq = (a - 1) % 4 + 1
        bias = rng.gauss(0, 0.35); speed = rng.lognormvariate(0, 0.25)
        for period, (cond, cset) in enumerate(SEQUENCES[seq], start=1):
            if aid in withdrawn and period == 2:
                continue
            for cid, c in cases.items():
                if c["set"] != cset:
                    continue
                latent = c["ref"] + bias + c["quiet"] * (quiet_rubric if cond == "R" else quiet_usual) \
                         + (period2 if period == 2 else 0) + rng.gauss(0, noise)
                rating = min(4, max(1, round(latent)))
                secs = c["base_s"] * speed * (1.18 if cond == "R" else 1.0) * rng.lognormvariate(0, 0.2)
                rows.append(dict(analyst=aid, seq=seq, period=period, cond=cond, case=cid, ref=c["ref"],
                                 quiet=c["quiet"], rating=rating, seconds=round(secs)))
    return rows
```

The generator's seed (2031) was chosen when the book was written so that the synthetic dataset behaves like a typical draw: for some other seeds, chance produces a sizeable apparent "effect" in noisy cases where the generator has none — itself a lesson about subgroup analyses in small studies.

### 6.3 The primary analysis

The estimand (Chapter 1) is the mean, across analysts, of each analyst's under-triage proportion with the rubric minus their proportion without it. The analysis follows the pre-analysis plan:

- **Per-analyst differences.** Computing one difference per analyst respects the clustering of decisions within analysts: the 23 differences, not the 368 high-impact decisions, are the independent units.
- **Bootstrap interval.** Resample the 23 differences with replacement many times and take the 2.5th and 97.5th percentiles of the resampled means ([Efron 1979](https://doi.org/10.1214/aos/1176344552)). The percentile bootstrap is simple and transparent; with 23 units it is approximate, and the dissertation says so.
- **Sign-flip permutation test.** If the rubric had no effect, each analyst's difference would be equally likely to be positive or negative. Randomly flipping signs many times gives the distribution of the mean under that null; the p-value is the share of flipped means at least as extreme as the observed one.
- **Period check.** Compare within-analyst changes from period 1 to period 2 between analysts who went usual→rubric and those who went rubric→usual. Half their sum estimates the period effect.

Secondary outcomes are computed on the same 23 analysts: quadratic-weighted kappa between rating and reference ([Cohen 1968](https://doi.org/10.1037/h0026256)), median decision seconds, and over-triage of low-impact cases (rating above reference, among references 1–2).

### 6.4 Practical activity: the main analysis

Save the analysis as `lab6_analysis.py` in the same folder as `lab6_data.py` and run it.

```python
# Lab 6 - main analysis of the synthetic Triage Rubric Study (offline, stdlib only; imports lab6_data.py)
import random, statistics as st
from lab6_data import make_study
ROWS = make_study()
def under(r, levels=1): return r["rating"] <= r["ref"] - levels
def per_analyst(rows, cond, keep=lambda r: r["ref"] >= 3, levels=1):
    out = {}
    for r in rows:
        if r["cond"] == cond and keep(r):
            out.setdefault(r["analyst"], []).append(under(r, levels))
    return {a: sum(v) / len(v) for a, v in out.items()}
def paired(rows, **kw):
    R, U = per_analyst(rows, "R", **kw), per_analyst(rows, "U", **kw)
    both = sorted(set(R) & set(U))
    return [R[a] - U[a] for a in both], R, U, both
def boot_ci(d, reps=4000, seed=1):
    rng = random.Random(seed); m = sorted(st.mean(rng.choices(d, k=len(d))) for _ in range(reps))
    return m[int(0.025 * reps)], m[int(0.975 * reps) - 1]
def signflip_p(d, reps=20000, seed=2):
    rng = random.Random(seed); obs = abs(st.mean(d))
    hits = sum(abs(st.mean([x if rng.random() < 0.5 else -x for x in d])) >= obs - 1e-12 for _ in range(reps))
    return (hits + 1) / (reps + 1)
def wkappa(pairs, k=4):
    n = len(pairs); w = lambda i, j: 1 - ((i - j) / (k - 1)) ** 2
    po = sum(w(a, b) for a, b in pairs) / n
    pa = [sum(a == c for a, _ in pairs) / n for c in range(1, k + 1)]
    pb = [sum(b == c for _, b in pairs) / n for c in range(1, k + 1)]
    pe = sum(pa[i] * pb[j] * w(i + 1, j + 1) for i in range(k) for j in range(k))
    return (po - pe) / (1 - pe)
if __name__ == "__main__":
    d, R, U, both = paired(ROWS)
    print(f"analysts enrolled 24, with both periods {len(both)} (A17 withdrew after period 1)")
    print(f"primary: under-triage of high-impact cases  usual {st.mean(U[a] for a in both):.3f}  rubric {st.mean(R[a] for a in both):.3f}")
    lo, hi = boot_ci(d)
    print(f"  paired difference (rubric - usual) {st.mean(d):+.3f}  95% bootstrap CI {lo:+.3f} to {hi:+.3f}  sign-flip p = {signflip_p(d):.4f}")
    print(f"  analysts better / same / worse with rubric: {sum(x < 0 for x in d)} / {sum(x == 0 for x in d)} / {sum(x > 0 for x in d)}")
    # period (learning) effect: within-analyst period-2 minus period-1 rate, by condition order
    def rate(a, p): v = [under(r) for r in ROWS if r["analyst"] == a and r["period"] == p and r["ref"] >= 3]; return sum(v) / len(v)
    pd_ur = [rate(a, 2) - rate(a, 1) for a in both if int(a[1:]) % 4 in (1, 2)]
    pd_ru = [rate(a, 2) - rate(a, 1) for a in both if int(a[1:]) % 4 in (3, 0)]
    print(f"period check: P2-P1 when U->R {st.mean(pd_ur):+.3f}; when R->U {st.mean(pd_ru):+.3f}; period effect {(st.mean(pd_ur) + st.mean(pd_ru)) / 2:+.3f}")
    for q, label in ((1, "quiet"), (0, "noisy")):
        dq, *_ = paired(ROWS, keep=lambda r, q=q: r["ref"] >= 3 and r["quiet"] == q)
        print(f"  subgroup {label:<5} high-impact cases: difference {st.mean(dq):+.3f}")
    for cond in ("U", "R"):
        k = wkappa([(r["ref"], r["rating"]) for r in ROWS if r["cond"] == cond and r["analyst"] in both])
        s = st.median(r["seconds"] for r in ROWS if r["cond"] == cond and r["analyst"] in both)
        o = sum(r["rating"] > r["ref"] for r in ROWS if r["cond"] == cond and r["analyst"] in both and r["ref"] <= 2) / \
            sum(1 for r in ROWS if r["cond"] == cond and r["analyst"] in both and r["ref"] <= 2)
        print(f"secondary {cond}: weighted kappa vs reference {k:.3f}  median seconds {s:.0f}  over-triage of low-impact {o:.3f}")
    print("robustness of the primary contrast:")
    for name, kw in (("under by 2+ levels", dict(levels=2)), ("include reference-2 cases", dict(keep=lambda r: r["ref"] >= 2)),
                     ("critical cases only (ref 4)", dict(keep=lambda r: r["ref"] == 4))):
        dd, *_ = paired(ROWS, **kw)
        lo2, hi2 = boot_ci(dd)
        print(f"  {name:<28} {st.mean(dd):+.3f}  CI {lo2:+.3f} to {hi2:+.3f}")
```

Expected output:

```text
analysts enrolled 24, with both periods 23 (A17 withdrew after period 1)
primary: under-triage of high-impact cases  usual 0.538  rubric 0.364
  paired difference (rubric - usual) -0.174  95% bootstrap CI -0.245 to -0.098  sign-flip p = 0.0005
  analysts better / same / worse with rubric: 19 / 1 / 3
period check: P2-P1 when U->R -0.148; when R->U +0.198; period effect +0.025
  subgroup quiet high-impact cases: difference -0.370
  subgroup noisy high-impact cases: difference +0.022
secondary U: weighted kappa vs reference 0.623  median seconds 236  over-triage of low-impact 0.261
secondary R: weighted kappa vs reference 0.755  median seconds 281  over-triage of low-impact 0.239
robustness of the primary contrast:
  under by 2+ levels           -0.082  CI -0.120 to -0.049
  include reference-2 cases    -0.170  CI -0.239 to -0.104
  critical cases only (ref 4)  -0.246  CI -0.377 to -0.101
```

How to read it.

- **Primary result.** Averaged across the 23 analysts, the under-triage proportion for high-impact cases was 0.538 with usual judgement and 0.364 with the rubric. The mean within-analyst difference is −0.174 (−17.4 percentage points), with a 95% bootstrap interval from −24.5 to −9.8 points and a sign-flip p-value of 0.0005 (the smallest value 20,000 flips can give is about 0.00005, so this is not at a floor). Nineteen analysts did better with the rubric, one the same and three worse. These proportions are high because the case sets were deliberately enriched with quiet-impact cases; they are not estimates of how often under-triage occurs in practice.
- **Period check.** Analysts who went usual→rubric improved by 14.8 points from period 1 to 2; those who went rubric→usual worsened by 19.8 points. The estimated period effect is +2.5 points (slightly *more* under-triage in period 2) — small, and in the opposite direction to the generator's practice effect, which is a reminder that a check with 23 analysts is itself noisy. Because order was balanced, a period effect of this size does not bias the primary contrast. The asymmetry between the two orders (−14.8 versus +19.8) is also what carryover would look like if rubric-first analysts had kept some benefit; here it is within noise, and Chapter 8's sequence-level check returns to it.
- **Mechanism subgroup.** The reduction is concentrated in quiet-impact cases (−37.0 points); on noisy cases the difference is +2.2 points, consistent with no effect. This was predeclared (Chapter 4) and matches the prediction of the situation-awareness account.
- **Costs and agreement.** Weighted kappa against the reference rose from 0.623 to 0.755. Median decision time rose from 236 to 281 seconds, about 45 seconds per case. Over-triage of low-impact cases did not rise (0.261 usual, 0.239 rubric), which argues against the rival "the rubric simply pushes every rating up".
- **Robustness.** Counting only errors of two or more levels, the difference is −8.2 points (interval −12.0 to −4.9); including severity-2 cases, −17.0; critical cases only, −24.6 with a wider interval. All point the same way.

### 6.5 What robustness shows and does not show

Robustness checks show that a conclusion does not depend on one arbitrary choice. They do not show that the conclusion is *correct*: if all specifications share a flaw — a biased reference standard, say, or cases unlike real ones — they will agree with each other and all be wrong. Report robustness as "the direction and approximate size held across the predeclared alternatives", not as "the result is robust", and keep the shared assumptions in view. Chapter 8 widens the set of alternatives into a specification curve.

Two other temptations deserve naming. The first is to compute a pooled proportion over all decisions and report it with a binomial interval: that treats 368 decisions as independent and produces an interval that is too narrow. The second is to drop the three analysts who did worse with the rubric because they "did not engage with it". Unless fidelity checks recorded non-use (a deviation, with a predeclared rule), they stay in.

### 6.6 Missing data and the withdrawn analyst

A17 completed period 1 (usual judgement, sequence 1) and withdrew. The primary analysis uses analysts with both periods, as predeclared. Is that biased? It is unbiased if A17's withdrawal is unrelated to what their rubric result would have been — plausible here, since they withdrew for personal reasons before seeing the rubric — but the assumption should be stated. A sensitivity analysis can bound the effect: give A17 the worst plausible difference (no improvement, or the largest worsening observed) and the best, and report the range of the mean. With one withdrawal out of 24 the range is narrow; with six it might not be. The general framework for thinking about missing outcome data in trials, including sensitivity analyses under different assumptions, is set out by [White et al. (2011)](https://doi.org/10.1136/bmj.d40).

### 6.7 The qualitative strand

#### 6.7.1 Sampling and interviewing

RQ3 asks how analysts describe their reasoning when the rubric changed, or failed to change, their rating. After all sessions were complete, twelve analysts were invited for 30-minute debrief interviews, chosen purposively: four whose under-triage fell most, four whose results barely changed, and the three who did worse plus one more from the middle. The interviewer showed each analyst two of their own decisions — one where their usual and rubric ratings of matched cases differed, one where they did not — and asked them to reconstruct their reasoning. Twelve interviews is a judgement, not a rule; [Malterud, Siersma and Guassora (2016)](https://doi.org/10.1177/1049732315617444) argue for sizing by "information power", which depends on the narrowness of the aim, the specificity of the sample and the quality of dialogue.

#### 6.7.2 Thematic analysis

Transcripts were analysed with reflexive thematic analysis following [Braun and Clarke (2006)](https://doi.org/10.1191/1478088706qp063oa): familiarization, initial coding, searching for themes, reviewing, defining and naming, and writing. Codes were generated from the data rather than from the hypothesis, though the analyst knew the hypothesis and recorded that in a reflexive memo. Every code and theme change was dated in an **audit trail**.

#### 6.7.3 Coding consistency

In reflexive thematic analysis, inter-coder agreement statistics are contested, because the method treats coding as interpretive. For a master's dissertation, a practical compromise is for a second person to code three transcripts independently with the codebook, then discuss disagreements to sharpen code definitions, reporting the process and its effect on the codebook rather than treating a kappa as a validity certificate.

#### 6.7.4 Themes (synthetic)

1. **"The quiet ones look like housekeeping."** Analysts described quiet-impact cases as resembling routine maintenance noise; the rubric's question about which service was affected "made me look up what the job actually did" (A05).
2. **"The rubric slowed me down where I already knew."** Several experienced analysts said the rubric added time on obvious cases without changing their answer — consistent with the time cost and the null noisy-case result.
3. **"I trusted my first read."** Two of the three analysts who did worse said they completed the rubric after already deciding and adjusted answers to match their first impression — a fidelity concern that the observer form did not capture.
4. **"It gave me words for escalating."** Analysts described the rubric as justification they could cite to a shift lead when escalating a case with few alerts.

### 6.8 Integration: the joint display

Mixed-methods integration means more than placing two results side by side. A **joint display** ([O'Cathain, Murphy and Nicholl 2010](https://doi.org/10.1136/bmj.c4587) describe this and other techniques) lines up quantitative and qualitative findings on the same question and states whether they **converge**, **complement** or are **discordant**.

| Question | Quantitative result | Qualitative result | Integration |
|---|---|---|---|
| Where does the rubric help? | −37.0 points on quiet-impact cases; +2.2 on noisy | Theme 1: quiet cases resemble housekeeping; rubric prompts lookup | Converge: mechanism consistent with attention to impact |
| What does it cost? | +45 s median per case; over-triage unchanged | Theme 2: slower where the answer was already known | Converge and complement: the cost is concentrated in easy cases |
| Why did some analysts do worse? | 3 of 23 worse | Theme 3: rubric completed after deciding | Complement: suggests a fidelity mechanism not measured; generate a hypothesis, not a finding |
| Does it change escalation behaviour? | Not measured | Theme 4: rubric as justification for escalation | Qualitative only: flagged for future study |

Discordance, when it appears, is reported, not resolved by letting one strand win.

### 6.9 Worked example: the deviation that was nearly hidden (synthetic)

While checking fidelity notes, the student found that observer 1 had written "sheet completed after rating?" beside two sessions — the same two analysts who, in interview, described completing the rubric after deciding. The observer form had no field for this; the notes were in the margin. The temptation was to exclude those analysts as non-adherent, which would have improved the result. Instead, the student logged the observation as a deviation discovered after data collection, kept the analysts in the primary analysis as predeclared, and reported an exploratory analysis excluding them, labelled as such, alongside a recommendation that future studies time-stamp rubric completion. The dissertation is stronger for it: the finding about *how* rubrics fail is itself a contribution.

### 6.10 Common errors and limits

- Treating decisions as independent and reporting intervals that are too narrow.
- Omitting the period and carryover checks in a crossover.
- Reporting the benefit without the costs (time, over-triage).
- Calling a result "robust" because predeclared variations agree, without naming the assumptions they share.
- Dropping participants whose results are inconvenient without a predeclared fidelity rule.
- Presenting a subgroup found after looking at the data as if it were predeclared.
- Quoting interview excerpts selectively to support the quantitative result; ignoring discordant themes.
- Copying numbers into the text by hand instead of from output files.

The limit of the analysis is the design: precise estimates on fictional cases are still estimates about fictional cases. Chapter 7 states that limit with its direction.

### Exercises — chapter 6

**EX033 — Data dictionary and cleaning log.** *Objective:* make lineage explicit. *Inputs:* §6.1. *Constraints:* add two variables the study should have recorded but did not. *Steps:* (1) add the variables to the dictionary (for example, rubric completion time stamp; observer 2 time); (2) write the first five steps of a cleaning log for the raw answer sheets. *Expected evidence:* the table and log. *Rubric:* 3 = variables well defined with sources, log steps specific with row counts and scripts; 2 = one vague entry; 1 = generic; 0 = none.

**EX034 — Run Lab 6 and interpret.** *Objective:* compute and explain the primary analysis. *Inputs:* Lab 6. *Constraints:* offline. *Steps:* (1) run it and record the output; (2) write two sentences reporting the primary result with its interval; (3) explain in one sentence why the pooled 368-decision proportion would give a misleadingly narrow interval. *Expected evidence:* outputs and sentences. *Rubric:* 3 = numbers exact, interval and p-value correctly worded, clustering explained; 2 = one wording error ("proves"); 1 = not run; 0 = none.

**EX035 — Withdrawal sensitivity.** *Objective:* bound the effect of the missing analyst. *Inputs:* Lab 6 output. *Constraints:* assume A17's difference could be anything from the largest worsening observed among the 23 analysts to the largest improvement. *Steps:* (1) compute the observed minimum and maximum per-analyst differences (modify the lab to print them); (2) compute the mean of 24 differences under each extreme; (3) state the range. *Expected evidence:* the calculation. *Rubric:* 3 = extremes and resulting means correct, interpretation that one withdrawal cannot change the conclusion, assumption stated; 2 = arithmetic slip; 1 = no numbers; 0 = none.

**EX036 — Period and carryover.** *Objective:* interpret crossover checks. *Inputs:* the period check line. *Constraints:* use only Lab 6 output. *Steps:* (1) explain how −0.148 and +0.198 combine into the period effect; (2) explain what pattern carryover would produce; (3) say whether these numbers are evidence of carryover. *Expected evidence:* a paragraph. *Rubric:* 3 = period effect computed as half the sum, carryover pattern described (rubric-first analysts' usual period better than usual-first analysts' usual period), conclusion cautious given 23 analysts; 2 = one confusion; 1 = restatement; 0 = none.

**EX037 — Codebook entry.** *Objective:* define a qualitative code precisely. *Inputs:* Theme 3. *Constraints:* use the fields name, definition, include when, exclude when, example. *Steps:* write entries for two codes that could underlie Theme 3, and one for a code that a second coder might confuse with them. *Expected evidence:* three entries. *Rubric:* 3 = definitions distinguish "post-hoc completion" from "disagreeing with the rubric" from "time pressure", include/exclude rules usable; 2 = overlapping; 1 = labels only; 0 = none.

**EX038 — Joint display with discordance.** *Objective:* integrate honestly. *Inputs:* the joint display in §6.8. *Constraints:* add one row where the strands could be discordant. *Steps:* (1) propose a plausible discordant finding (for example, interviews say the rubric helped most on critical cases, while the critical-only estimate is imprecise); (2) write the integration cell; (3) say what further data would resolve it. *Expected evidence:* the row and a paragraph. *Rubric:* 3 = discordance stated without resolving it by fiat, further data specific; 2 = discordance explained away; 1 = no discordance; 0 = none.

### Chapter synthesis

Collect data with lineage: a data dictionary, a cleaning log and read-only raw files. Analyse a crossover within participants, with a resampling interval, a permutation test and period and carryover checks. Report costs beside benefits and test predeclared alternative outcomes, remembering that agreement among specifications is not proof of correctness. Handle missing data by stating assumptions and bounding their effect. Analyse interviews with a documented, reflexive method and integrate the strands in a joint display that reports convergence, complementarity and discordance alike.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 08

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Dissertation on response effectiveness and limits

### Learning outcomes and connection

After this chapter you should be able to:

1. Structure a dissertation so that each chapter has one job, and write an argument that a reader can follow from question to conclusion.
2. Build a results-to-claims register that keeps every claim inside the evidence that supports it.
3. Report estimates with intervals and calibrated language, including negative and inconclusive results.
4. Check number provenance automatically so that every number in the text matches the analysis output.
5. Use reporting guidelines as checklists, state limitations with their direction, and write a data and code availability statement under confidentiality constraints.

The chapter builds on the results of Chapter 6 and prepares Chapter 8, where the dissertation faces independent review.

### 7.1 Structure: one job per chapter

A conventional empirical dissertation has a recognizable shape, and examiners read faster when you use it:

| Chapter | Job | Triage Rubric Study content |
|---|---|---|
| 1 Introduction | The problem, the question, why it matters, what the reader will get | MRSS decision; RQ1–RQ3; estimand; scope; summary of findings |
| 2 Literature | What is known, competing models, the gap | Concept matrix; models of effectiveness; decision theories |
| 3 Methods | Exactly what was done, so it could be repeated | Crossover design, cases and reference panel, participants, measures, analysis plan, ethics |
| 4 Historical context | The descriptive and associational strand | MRSS tickets, rival analysis, negative control |
| 5 Results | What was found, without interpretation | Primary, secondary, checks, robustness, qualitative themes, joint display |
| 6 Discussion | What it means, for whom, with what limits | Interpretation, comparison with literature, limitations, implications |
| 7 Conclusion | Answers to the questions; what next | Direct answers to RQ1–RQ3; recommendations; future work |

The single most useful discipline is to keep **results** and **interpretation** apart. The results chapter says what the numbers and themes are; the discussion says what they mean. When a sentence in the results chapter contains "suggests", "demonstrates" or "because", it probably belongs in the discussion.

### 7.2 The argument and the results-to-claims register

A dissertation's argument is a chain: the problem matters; the question addresses it; the design can answer the question; the analysis was sound; the results are these; therefore these claims follow, within these limits. A **results-to-claims register** makes each link inspectable:

| Claim (as it will appear) | Evidence | Design support | Scope | Strength |
|---|---|---|---|---|
| "Using the rubric reduced under-triage of high-impact fictional cases by about 17 percentage points (95% interval 10 to 25)." | Primary analysis | Randomized crossover; within-analyst contrast | Experienced volunteers; fictional cases; printed rubric | Strong within scope |
| "The reduction was concentrated in quiet-impact cases." | Predeclared subgroup; theme 1 | As above, subgroup of 4 cases per condition | As above | Moderate: smaller sample, but predeclared and mechanistically supported |
| "The rubric added about 45 seconds per case." | Median times | As above | Tabletop timing, not live workload | Moderate |
| "The rubric did not increase over-triage." | Over-triage of low-impact cases | As above, 4 low-impact cases per condition | As above | Weak to moderate: few cases, interval not computed in the plan — report as "no increase observed" |
| "Adopting the rubric at MRSS would reduce missed incidents." | Extrapolation | None directly | Live operations | Not supported as a finding; can be stated as an implication with conditions |
| "The historical data show the rubric halved under-triage." | Lab 4 crude contrast | Confounded | — | **Not claimed**; the register records why |

The register is a working document, but including a condensed version in the discussion chapter shows examiners you have thought about claim strength.

### 7.3 Reporting results honestly

#### 7.3.1 Estimates and intervals, not verdicts

Report the estimate, its interval and the test, in that order of importance: "the mean within-analyst difference was −17.4 percentage points (95% bootstrap interval −24.5 to −9.8; sign-flip permutation p = 0.0005)". Avoid "significant" as a description of importance; if you use it, say "statistically significant at the 5% level" and give the interval anyway. Never write "the rubric works" or "proves".

#### 7.3.2 Calibrated verbs

| Evidence | Verb |
|---|---|
| Randomized, predeclared, precise, within scope | "reduced", "increased" (with scope) |
| Predeclared but imprecise | "was associated with a reduction of… (interval includes small effects)" |
| Observational, adjusted | "was associated with…, after adjusting for…" |
| Exploratory | "in an exploratory analysis… which requires confirmation" |
| Qualitative | "participants described…"; "this is consistent with…" |
| Extrapolation | "if these results transfer to live triage, they would imply…" |

#### 7.3.3 Negative and inconclusive results

A negative result — an interval centred on zero and excluding effects of practical interest — is a finding: "the data are inconsistent with a reduction larger than X". An **inconclusive** result — an interval including both no effect and important effects — is not a negative result and must not be reported as "no effect". In this study, the over-triage comparison and the noisy-case subgroup are inconclusive in the strict sense; the dissertation says "no increase was observed" and "no effect was detectable on noisy cases, which the design was not powered to rule out", not "the rubric has no effect on noisy cases".

#### 7.3.4 Multiplicity

The study has one primary outcome, four secondary outcomes, a subgroup analysis and four robustness checks. Only the primary outcome carries the confirmatory weight; the others are reported with their intervals and described as secondary or exploratory. If you report many p-values, say how many tests were done, so a reader can judge the chance of a false positive among them.

### 7.4 Number provenance

Most numerical errors in dissertations are not analysis errors; they are transcription errors — a number from an earlier run, a typo, a rounding inconsistency, a sample size that was not updated after a withdrawal. The remedy is mechanical: every number in the text comes from an output file, and before submission a script checks that each printed number matches. Some students generate tables and in-text numbers directly from code; others keep a list of printed numbers with their source keys, as in Lab 7. Either is acceptable; copying by hand is not.

### 7.5 Practical activity: number provenance

Lab 7 compares nine numbers printed in a synthetic draft dissertation with the analysis output. Save it as `lab7_provenance.py` next to `lab6_data.py` and `lab6_analysis.py`.

```python
# Lab 7 - number provenance: does every number in the draft dissertation match the analysis output? (offline)
# Imports lab6_data.py and lab6_analysis.py (save both). The draft sentences below are synthetic.
import statistics as st
from lab6_analysis import ROWS, paired, boot_ci, signflip_p, wkappa
d, R, U, both = paired(ROWS)
lo, hi = boot_ci(d)
med = {c: st.median(r["seconds"] for r in ROWS if r["cond"] == c and r["analyst"] in both) for c in "UR"}
kap = {c: wkappa([(r["ref"], r["rating"]) for r in ROWS if r["cond"] == c and r["analyst"] in both]) for c in "UR"}
RESULTS = {  # key -> (value, how to render it for comparison with the text)
    "n_complete": (len(both), "{:d}"),
    "diff_pp": (100 * st.mean(d), "{:.1f}"),
    "ci_lo_pp": (100 * lo, "{:.1f}"), "ci_hi_pp": (100 * hi, "{:.1f}"),
    "p_signflip": (signflip_p(d), "{:.4f}"),
    "kappa_R": (kap["R"], "{:.2f}"), "kappa_U": (kap["U"], "{:.2f}"),
    "extra_seconds": (med["R"] - med["U"], "{:.0f}"),
}
DRAFT = [  # (location, number as printed, result key)
    ("Abstract", "23", "n_complete"),
    ("Abstract", "-17.4", "diff_pp"),
    ("Abstract", "-24.5", "ci_lo_pp"),
    ("Abstract", "-9.8", "ci_hi_pp"),
    ("Results 5.2", "0.0005", "p_signflip"),
    ("Results 5.4", "0.78", "kappa_R"),
    ("Results 5.4", "0.62", "kappa_U"),
    ("Results 5.5", "38", "extra_seconds"),
    ("Discussion 6.1", "24", "n_complete"),
]
bad = 0
for where, printed, key in DRAFT:
    value, fmt = RESULTS[key]
    ok = fmt.format(value) == printed
    bad += not ok
    print(f"{'ok  ' if ok else 'FAIL'} {where:<15} printed {printed:>7}  analysis {fmt.format(value):>7}  [{key}]")
print(f"{bad} of {len(DRAFT)} printed numbers do not match the analysis output")
```

Expected output:

```text
ok   Abstract        printed      23  analysis      23  [n_complete]
ok   Abstract        printed   -17.4  analysis   -17.4  [diff_pp]
ok   Abstract        printed   -24.5  analysis   -24.5  [ci_lo_pp]
ok   Abstract        printed    -9.8  analysis    -9.8  [ci_hi_pp]
ok   Results 5.2     printed  0.0005  analysis  0.0005  [p_signflip]
FAIL Results 5.4     printed    0.78  analysis    0.76  [kappa_R]
ok   Results 5.4     printed    0.62  analysis    0.62  [kappa_U]
FAIL Results 5.5     printed      38  analysis      45  [extra_seconds]
FAIL Discussion 6.1  printed      24  analysis      23  [n_complete]
3 of 9 printed numbers do not match the analysis output
```

How to read it. Six numbers match. Three do not. The rubric kappa of 0.78 is a stale value from an earlier run before observer form v1.1 changed which rating was recorded; the time cost of 38 seconds was computed from means in an earlier draft and never updated to the predeclared medians (45 seconds); and the discussion's "24 analysts" counts enrolled analysts where the analysis used 23 with both periods. None of these errors changes the conclusion, but each would cost credibility with an examiner and the third misstates the sample. The fix is to regenerate the numbers, not to edit the script's expectations.

### 7.6 Reporting guidelines as checklists

Reporting guidelines list what a reader needs in order to judge a study. They are not quality scores and they do not dictate design; they are checklists of what to say. The relevant ones here are:

- **CONSORT** for randomized trials ([Schulz, Altman and Moher 2010](https://doi.org/10.1136/bmj.c332)) and its **extension to randomized crossover trials** ([Dwan et al. 2019](https://doi.org/10.1136/bmj.l4378)), which asks specifically about carryover, period effects and the analysis of within-participant data — directly relevant to the tabletop.
- **STROBE** for observational studies ([Vandenbroucke et al. 2007](https://doi.org/10.1371/journal.pmed.0040297)), for the historical MRSS strand.
- **SRQR**, Standards for Reporting Qualitative Research ([O'Brien et al. 2014](https://doi.org/10.1097/ACM.0000000000000388)), for the debrief interviews.
- **CONSORT pilot extension** ([Eldridge et al. 2016](https://doi.org/10.1136/bmj.i5239)) for the pilot report, if it is presented as a separate study.

Work through each checklist after drafting the methods and results, and record where each item is addressed. Items you cannot address (for example, a registry number if the plan was not registered) should be acknowledged, not ignored.

### 7.7 Directional limitations

A limitations section that lists weaknesses without saying what they do to the answer is decoration. For each limitation, state its **direction** — does it probably make the estimate too large, too small, or affect only its precision or transferability? — and, where possible, its likely size.

| Limitation | Likely direction | Reasoning |
|---|---|---|
| Fictional cases enriched with quiet-impact cases | Effect *on the overall under-triage rate in practice* would be smaller | The effect is concentrated in quiet-impact cases, which are a minority of live incidents |
| Volunteers likely more motivated | Uncertain; probably makes both conditions better; effect on the difference unclear | Motivation may raise rubric fidelity (larger effect) or usual-judgement care (smaller effect) |
| Printed rubric in a quiet room | Live effect probably smaller | Alert floods and interruptions reduce fidelity; rubric completion after deciding (theme 3) may become commoner |
| Reference standard from one panel | Uncertain direction; affects construct validity | If the panel's own habits resemble the rubric's questions, the rubric may look better than it is (Chapter 8 tests an alternative reference) |
| Time measured to first written rating | Time cost may be underestimated | Later revisions and discussions are not timed |
| One withdrawal | Negligible | Bounded in the sensitivity analysis (EX035) |
| Observers not blind to condition | Could bias times, not ratings | Ratings are written by participants; times have two-observer checks |

### 7.8 Accessible figures and tables

Choose figures that show the unit of analysis: a dot plot of the 23 per-analyst differences, with the mean and interval, shows both the effect and its spread better than a bar chart of two pooled proportions. Use colour-blind-safe palettes and do not encode meaning in colour alone; give every figure a text alternative that states its message; label axes with units; and make tables readable by screen readers (no merged cells used for layout). An accessible dissertation is easier for every examiner to read.

### 7.9 Data and code availability under sensitivity

The availability statement says what is shared, where, and under what conditions. For this study: the analysis code, the pre-analysis plan, the case vignettes, the rubric and the observer form are deposited openly; the de-identified decision-level dataset is available to bona fide researchers under a data use agreement, because combinations of team, experience band and sequence could identify participants; a synthetic dataset with the same structure (produced by `lab6_data.py`) is deposited openly so that the pipeline can be run; interview transcripts are not shared, as participants were promised, but the codebook and audit trail are. This follows the spirit of the FAIR principles ([Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18)): metadata and access routes are open even where the data themselves are restricted.

### 7.10 Worked example: rewriting the abstract (synthetic)

*First draft.* "This study proves that structured triage rubrics significantly improve SOC performance. Analysts using the SEV-4 rubric were 32% less likely to miss critical incidents (p < 0.001). Organizations should adopt rubrics."

*Problems.* "Proves" overclaims; "SOC performance" is broader than the outcome; "32% less likely" is a relative reduction (0.174/0.538) presented without the absolute difference; "critical incidents" conflates high-impact (3–4) with critical (4); "p < 0.001" is false (p = 0.0005 satisfies it, but the interval is the main result and is missing); the recommendation ignores scope and cost.

*Revised (structured).* **Background:** analysts may under-rate high-impact incidents with little alert noise. **Methods:** randomized crossover tabletop; 24 experienced volunteer analysts (23 completed both periods) rated 24 fictional cases against an independent panel reference, with and without a four-question impact rubric. **Results:** under-triage of high-impact cases fell from 53.8% to 36.4% (mean within-analyst difference −17.4 percentage points, 95% interval −24.5 to −9.8). The reduction was concentrated in quiet-impact cases. Median decision time rose by 45 seconds; over-triage of low-impact cases did not increase. **Conclusions:** in a controlled setting, the rubric reduced under-triage of high-impact cases at a modest time cost. Its effect in live operations, where quiet-impact cases are fewer and interruptions more common, is likely smaller and remains to be tested.

### 7.11 Common errors and limits

- Mixing results and interpretation.
- Claims that exceed the design (causal language on associational data; prevalence language on enriched cases).
- Relative reductions without absolute differences.
- Reporting an inconclusive result as "no effect".
- Hand-copied numbers that drift from the analysis.
- Limitations without directions.
- Availability statements that say "data available on request" without conditions or a route.

The limit of writing is that it cannot add evidence. It can only represent the evidence accurately — which, for an examiner, is most of what is being assessed.

### Exercises — chapter 7

**EX039 — Results-to-claims register.** *Objective:* keep claims within evidence. *Inputs:* Chapter 6 results and §7.2. *Constraints:* add three rows. *Steps:* add rows for (a) the kappa result, (b) theme 4 on escalation, (c) a claim about novices. For each, complete all five columns. *Expected evidence:* the rows. *Rubric:* 3 = kappa claimed as secondary with scope, theme 4 as a participant account generating a hypothesis, novice claim marked not supported (eligibility required six months' experience); 2 = one overclaim; 1 = columns incomplete; 0 = none.

**EX040 — Run and fix Lab 7.** *Objective:* enforce number provenance. *Inputs:* Lab 7. *Constraints:* fix the *draft*, not the analysis. *Steps:* (1) run it; (2) correct the three draft entries; (3) rerun and confirm 0 failures; (4) add two entries for the over-triage proportions and confirm they pass. *Expected evidence:* outputs. *Rubric:* 3 = draft corrected to 0.76, 45 and 23, rerun shows 0 of 9 (then 0 of 11) failures, new entries keyed correctly; 2 = analysis changed instead; 1 = not run; 0 = none.

**EX041 — Calibrated sentences.** *Objective:* match verbs to evidence. *Inputs:* five draft sentences: (a) "The rubric eliminates under-triage of quiet incidents." (b) "Senior analysts are better at triage." (c) "The rubric has no effect on noisy cases." (d) "Analysts hate the rubric." (e) "MRSS should mandate the rubric." *Constraints:* use §7.3.2. *Steps:* rewrite each. *Expected evidence:* five sentences. *Rubric:* 3 = each rewritten with the right verb, scope and uncertainty; (c) as inconclusive; (e) as a conditional implication; 2 = one overclaim remains; 1 = cosmetic changes; 0 = none.

**EX042 — Directional limitations.** *Objective:* state limitations with direction. *Inputs:* §7.7. *Constraints:* two new limitations. *Steps:* add two limitations (for example, case writers knew the hypothesis; the rubric was designed by the student) with direction and reasoning. *Expected evidence:* two rows. *Rubric:* 3 = directions argued (both plausibly favour the rubric, through case construction and allegiance), mitigations or checks proposed; 2 = direction asserted without reasoning; 1 = listed without direction; 0 = none.

**EX043 — Reporting checklist audit.** *Objective:* use a guideline as a checklist. *Inputs:* the [CONSORT crossover extension](https://doi.org/10.1136/bmj.l4378). *Constraints:* read the checklist items yourself. *Steps:* (1) choose five items specific to crossover trials; (2) say where the dissertation addresses each, or what is missing. *Expected evidence:* a table. *Rubric:* 3 = items genuinely crossover-specific (rationale for crossover, carryover, period effects, washout, within-participant analysis), locations or gaps precise; 2 = generic CONSORT items; 1 = fewer than five; 0 = none.

**EX044 — Availability statement.** *Objective:* share responsibly. *Inputs:* §7.9. *Constraints:* 120–180 words. *Steps:* write the statement for a version of the study that also used real, de-identified MRSS tickets under a partner agreement prohibiting disclosure. *Expected evidence:* the statement. *Rubric:* 3 = each artefact's access level stated, ticket data's restriction and route described, synthetic stand-in offered, no promise the agreement does not allow; 2 = vague route; 1 = "available on request"; 0 = none.

### Chapter synthesis

Give each dissertation chapter one job and keep results apart from interpretation. Build a results-to-claims register so every claim has evidence, design support, scope and an honest strength. Report estimates with intervals in calibrated language, distinguish negative from inconclusive results, and keep the primary outcome's confirmatory role clear. Check every printed number against the analysis output mechanically. Use reporting guidelines as checklists, write limitations with their direction, design accessible figures, and state data and code availability precisely under the constraints you accepted.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 08

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Independent research review and defense

### Learning outcomes and connection

After this chapter you should be able to:

1. Describe how examiners read a dissertation and the families of questions they ask.
2. Prepare a reproduction package and support an independent reader in reproducing your key results.
3. Answer "what if you had chosen differently?" with a specification curve rather than an assertion.
4. Find and present counterexamples to your own claims before an examiner does.
5. Conduct a defense, record corrections with an audit trail, and share results responsibly with participants, partners and the profession.

The chapter builds on the dissertation of Chapter 7 and closes the course.

### 8.1 How examiners read

Examiners rarely read a dissertation from front to back on the first pass. A common pattern is: abstract and introduction (what is claimed?), conclusion (does it match?), methods (could this design support it?), results tables (do the numbers support it?), limitations (does the author know the weaknesses?), and only then the literature review and discussion in full. They mark places where a claim is larger than its evidence, where a number cannot be traced, and where an obvious rival was not addressed. Write for that reader: put the answer to each research question where it can be found, make every number traceable, and address the rivals explicitly.

Master's examination in many systems includes an internal and an external examiner and sometimes an oral examination (viva or defense). The criteria usually resemble those in the front matter of this book: a clear question, a fitting design, competent and reproducible analysis, conclusions within the evidence, and a critical understanding of limits. Few examiners expect a master's study to be flawless; they expect you to know where its flaws are and what they do.

### 8.2 Families of questions

| Family | Typical question | What a good answer does |
|---|---|---|
| Motivation | "Why does under-triage matter more than speed?" | Links to the decision-maker's problem and the asymmetry of consequences (Chapter 2) |
| Design | "Why a crossover? What about carryover?" | States the counterfactual, the assumptions, the checks and their results |
| Measurement | "How do you know the reference standard is right?" | Describes panel independence, the split cases, and the alternative-reference analysis |
| Analysis | "Why per-analyst differences rather than a logistic mixed model?" | Explains clustering, transparency and the estimand; concedes a mixed model is a valid alternative and reports whether it would change conclusions |
| Robustness | "What if you had defined under-triage differently?" | Shows the specification curve |
| Rivals | "Isn't this just the rubric making everyone rate higher?" | Cites the over-triage result and the noisy-case null |
| Transfer | "Would this work in a real SOC at 3 a.m.?" | Gives the directional limitation and what would be needed to test it |
| Contribution | "What is new here?" | States the specific gap from the concept matrix and what the study adds, without inflating it |
| Reflexivity | "You designed the rubric. How did that affect the study?" | Acknowledges allegiance, names the safeguards (independent panel, predeclared plan) and their limits |

### 8.3 Reproduction by an independent reader

Before submission, ask someone outside the project — another student, a research software engineer — to reproduce the key results from your package without your help. Give them the README, code, the synthetic or restricted dataset and the pre-analysis plan; ask them to regenerate the primary result, the subgroup result and two tables. Record what they could not do. Common failures: undocumented software versions, a path hard-coded to your machine, a seed set in one script and not another, a manual step ("then I removed the duplicate row") that is not in the cleaning log. Each failure is cheaper to fix now than to explain in a defense.

The reader should also try to **break** your claims: run the analysis with choices you did not make, look for analysts or cases that drive the result, and check whether the result depends on the reference standard. That is the purpose of Lab 8.

### 8.4 "What if you had chosen differently?" — the specification curve

#### 8.4.1 The idea

Every analysis embodies choices: how to define the outcome, which cases to include, which reference standard to use, how to handle a withdrawal. Different reasonable choices could produce different answers. **Multiverse analysis** ([Steegen et al. 2016](https://doi.org/10.1177/1745691616658637)) and **specification curve analysis** ([Simonsohn, Simmons and Nelson 2020](https://doi.org/10.1038/s41562-020-0912-z)) run the analysis under every combination of defensible choices and display the distribution of results. The aim is not to find the best specification; it is to show how much the conclusion depends on choices.

Two cautions. The set of specifications must be *defensible* choices, decided as far as possible before looking — not every conceivable variation. And specifications are not independent evidence: twelve agreeing specifications on the same data are one dataset viewed twelve ways.

#### 8.4.2 Practical activity: the Triage Rubric specification curve

Lab 8 crosses three choices: the reference standard (the panel's consensus, or the minority view for the two cases where the panel split 2–1, C07 and C19, which the minority rated 2 rather than 3), the error threshold (one or two levels below reference) and the case inclusion rule (high-impact only, severity 2 and above, critical only). It also reports a leave-one-analyst-out range, the primary difference by sequence, and a counter-check of the rival "the rubric just inflates every rating". Save it as `lab8_review.py` next to the Chapter 6 files.

```python
# Lab 8 - an independent reader re-runs the analysis and asks "what if you had chosen differently?" (offline)
# Imports lab6_data.py and lab6_analysis.py. All data synthetic.
import statistics as st
from lab6_analysis import ROWS, paired, boot_ci
DISPUTED = {"C07", "C19"}   # panel split 2-1 on reference severity 3; the minority rated them 2
def with_reference(rows, alt):
    if not alt:
        return rows
    return [dict(r, ref=2) if r["case"] in DISPUTED else r for r in rows]
specs = []
for alt in (False, True):
    for levels in (1, 2):
        for incl_name, keep in (("ref>=3", lambda r: r["ref"] >= 3), ("ref>=2", lambda r: r["ref"] >= 2), ("ref=4", lambda r: r["ref"] == 4)):
            d, *_ = paired(with_reference(ROWS, alt), keep=keep, levels=levels)
            lo, hi = boot_ci(d, reps=2000)
            specs.append((st.mean(d), lo, hi, f"ref={'minority' if alt else 'panel'} under>={levels} {incl_name}"))
specs.sort()
print("specification curve (rubric - usual, under-triage proportion), sorted:")
for m, lo, hi, name in specs:
    print(f"  {m:+.3f}  [{lo:+.3f}, {hi:+.3f}]  {'excludes 0' if hi < 0 or lo > 0 else 'includes 0'}  {name}")
print(f"specifications: {len(specs)}  all negative: {all(m < 0 for m, *_ in specs)}  CI excludes 0: {sum(hi < 0 for _, _, hi, _ in specs)}")
d, R, U, both = paired(ROWS)
loo = [st.mean([x for a, x in zip(both, d) if a != drop]) for drop in both]
print(f"leave-one-analyst-out range: {min(loo):+.3f} to {max(loo):+.3f}  (primary {st.mean(d):+.3f})")
seq = {}
for a, x in zip(both, d):
    seq.setdefault((int(a[1:]) - 1) % 4 + 1, []).append(x)
print("primary difference by sequence: " + "  ".join(f"S{k}:{st.mean(v):+.3f} (n={len(v)})" for k, v in sorted(seq.items())))
low = lambda c: [r["rating"] > r["ref"] for r in ROWS if r["cond"] == c and r["ref"] <= 2 and r["analyst"] in both]
print(f"counter-check 'rubric just inflates every rating': over-triage of low-impact cases U {st.mean(low('U')):.3f}  R {st.mean(low('R')):.3f}")
```

Expected output:

```text
specification curve (rubric - usual, under-triage proportion), sorted:
  -0.246  [-0.391, -0.101]  excludes 0  ref=minority under>=1 ref=4
  -0.246  [-0.391, -0.101]  excludes 0  ref=panel under>=1 ref=4
  -0.174  [-0.245, -0.098]  excludes 0  ref=panel under>=1 ref>=3
  -0.170  [-0.239, -0.104]  excludes 0  ref=panel under>=1 ref>=2
  -0.135  [-0.204, -0.070]  excludes 0  ref=minority under>=1 ref>=2
  -0.118  [-0.193, -0.037]  excludes 0  ref=minority under>=1 ref>=3
  -0.116  [-0.203, -0.029]  excludes 0  ref=minority under>=2 ref=4
  -0.116  [-0.203, -0.029]  excludes 0  ref=panel under>=2 ref=4
  -0.082  [-0.120, -0.049]  excludes 0  ref=panel under>=2 ref>=3
  -0.065  [-0.096, -0.039]  excludes 0  ref=panel under>=2 ref>=2
  -0.062  [-0.106, -0.025]  excludes 0  ref=minority under>=2 ref>=3
  -0.043  [-0.074, -0.017]  excludes 0  ref=minority under>=2 ref>=2
specifications: 12  all negative: True  CI excludes 0: 12
leave-one-analyst-out range: -0.193 to -0.159  (primary -0.174)
primary difference by sequence: S1:-0.275 (n=5)  S2:-0.042 (n=6)  S3:-0.229 (n=6)  S4:-0.167 (n=6)
counter-check 'rubric just inflates every rating': over-triage of low-impact cases U 0.261  R 0.239
```

How to read it.

- **The curve.** All twelve specifications are negative and all intervals exclude zero. The estimates range from −4.3 to −24.6 points. The size depends a great deal on the choices — two-level errors are rarer, so their differences are smaller — but the direction does not.
- **Duplicates.** The two critical-only specifications are identical under both references, because the disputed cases have reference 3 and are not in the critical-only set. Twelve specifications are effectively ten. Say so; an examiner who notices first will wonder what else was not checked.
- **The reference standard matters.** Under the minority reference, the high-impact estimate falls from −17.4 to −11.8 points. Both quiet-impact cases where the panel split are cases where the rubric's questions point towards higher severity; if the minority were right, part of the apparent rubric benefit is the rubric agreeing with the majority's way of thinking. This is exactly the construct-validity worry in the limitations table (Chapter 7), now quantified.
- **Leave-one-out.** Removing any single analyst moves the primary estimate only between −19.3 and −15.9 points: no one analyst drives the result.
- **Sequences.** The difference varies by sequence, from −27.5 points (S1, five analysts) to −4.2 (S2). With five or six analysts per sequence these are noisy; but S2 — usual on set B first, then rubric on set A — is the smallest, and an examiner may ask whether set A's quiet cases are easier. The dissertation should report this, check the case-set balance (both sets have the same reference distribution and quiet count by design) and treat any case-set explanation as a hypothesis.
- **Counter-check.** Over-triage of low-impact cases is 0.261 with usual judgement and 0.239 with the rubric: the rubric did not raise every rating.

### 8.5 Counterexamples and how to present them

A counterexample is a specific case, analyst or subgroup where your claim does not hold. Look for them deliberately: the three analysts who did worse with the rubric; the noisy-case subgroup; sequence S2; the disputed cases. Present each with what it shows and what it does not. "Three of 23 analysts did worse with the rubric; two of them described completing it after deciding (theme 3). This suggests the benefit depends on using the rubric before forming an impression, which the study did not control and which live use may not ensure." A dissertation that presents its own counterexamples is more persuasive than one that hides them, because it shows the author looked.

### 8.6 Preparing for the defense

#### 8.6.1 The opening summary

Many defenses begin with a short presentation. Use it to answer four questions in about ten minutes: what was the question, what was done, what was found, and what are the limits. Show the dot plot of per-analyst differences, the subgroup result, the cost and the specification curve. Do not re-teach the literature review.

#### 8.6.2 Mock defenses

Hold at least one mock defense with people who did not supervise the project, using the question families in §8.2. Record the questions you answered poorly and prepare short, honest answers. Practise saying "I do not know, but here is how I would find out" and "that is a fair criticism; here is what it does to the conclusion".

#### 8.6.3 Answering

Answer the question asked. Concede valid points quickly and say what they change. Do not defend a choice by its popularity ("everyone uses MTTR"); defend it by its fit to the question. If an examiner proposes an alternative analysis, say whether you ran it (and what happened) or how you expect it would change the result and why.

### 8.7 After the defense: corrections

Examiners usually require corrections. Keep a **corrections table**: each requested change, where it was made, and how. Distinguish corrections that change claims from those that change presentation, and re-run the provenance check after any change to numbers. If an examiner's request would require new data collection beyond the scope agreed, discuss it with the supervisor and the examiner rather than inventing data or overstating what can be done.

| Examiner request | Change made | Location | Claim changed? |
|---|---|---|---|
| Report the minority-reference analysis in the main results, not an appendix | Moved specification curve to Results 5.6; added sentence to abstract | §5.6; abstract | Yes: primary claim now qualified by reference standard |
| Explain sequence S2 | Added case-set balance table and a paragraph | §5.7 | No |
| Remove "best practice" from conclusion | Rephrased as conditional implication | §7.2 | Yes: weaker |

### 8.8 Sharing results responsibly

#### 8.8.1 Participants first

Send participants a plain-language summary of the results before public release, as promised in the information sheet. Do not send individual results to employers, and do not publish anything that combines team, experience and sequence.

#### 8.8.2 Partners and the profession

A briefing for MRSS managers should give the result, its scope and its limits in one page: "In a controlled tabletop, the rubric reduced under-triage of high-impact fictional cases by about 17 points, mostly on quiet-impact cases, at about 45 seconds per case. The effect depends on the reference standard and on using the rubric before deciding. A live pilot with time-stamped rubric completion would be needed before a mandate." For the profession, consider a short paper or conference talk, a preprint, and depositing the case materials and code so others can replicate with their own analysts. A replication with different analysts and a different reference panel is the most valuable next study.

#### 8.8.3 Incidental findings

Research with security practitioners sometimes surfaces information about real weaknesses — a participant mentions an unpatched system, a case writer recognizes their employer's configuration. Such findings are not research data. Do not record or publish them; if they suggest a real risk, the participant or their organization should handle it through its own channels or coordinated disclosure, and the ethics committee should be told if the protocol did not anticipate it.

### 8.9 Worked example: a mock-defense exchange (synthetic)

> **Examiner:** Your rubric was written by you. The reference panel are senior responders who think like you. Isn't the study measuring how well analysts learn to agree with you?
>
> **Student:** That is a fair concern, and it is one I tried to measure rather than dismiss. The panel rated cases from their full ground truth before seeing the rubric, and none of them was involved in writing it. But two cases split the panel, and both are quiet-impact cases where the rubric's questions point towards the higher rating. When I use the minority's rating for those two, the primary estimate falls from about 17 to about 12 points, still with an interval excluding zero. So part of the effect may reflect agreement with a way of thinking rather than with an objective truth. The strongest test would be a replication with a reference panel from a different organization, which I recommend.
>
> **Examiner:** Then why not make the minority analysis primary?
>
> **Student:** Because the plan fixed the consensus reference before data, and switching after seeing the results would be choosing the analysis by its outcome. I report both prominently, and the abstract now mentions the dependence.

The answer concedes the point, quantifies it, explains the choice by reference to the plan and proposes a test. That is the pattern to practise.

### 8.10 Next steps after the master's

Some students will continue to doctoral research. The doctoral book in this area ([Incident Response doctoral course](../../../../doctorate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md)) asks for an original contribution and independent validation across contexts; a well-run master's study is good preparation, and its open questions (does the effect survive live conditions? does it depend on the reference standard? why do some analysts complete the rubric after deciding?) are the seeds of a doctoral proposal. Others will return to practice with a skill most practitioners lack: the habit of asking what else could explain an improvement, and how one would find out.

### 8.11 Common errors and limits

- Expecting the examiners to read front to back and burying the answers.
- Submitting a package nobody has tried to reproduce.
- Presenting a specification curve chosen after seeing which specifications favour the claim, or counting duplicate specifications as independent support.
- Hiding counterexamples.
- Defending choices by convention rather than by fit to the question.
- Making corrections without re-running the provenance check.
- Sharing individual results with employers, or publishing incidental security findings.

The limit of review is that reviewers see what you show them. A defense is strongest when you have shown the weak points yourself.

### Exercises — chapter 8

**EX045 — Run and extend Lab 8.** *Objective:* build and read a specification curve. *Inputs:* Lab 8. *Constraints:* offline. *Steps:* (1) run it; (2) identify the duplicated specifications and say how many distinct ones there are; (3) add a fourth choice — excluding the three analysts with the most negative differences, as a hostile reader might — and report the primary estimate under it (this is a robustness probe, not a legitimate exclusion); (4) state in two sentences what the curve shows and what it does not. *Expected evidence:* outputs and statement. *Rubric:* 3 = ten distinct specifications identified, hostile exclusion computed correctly, statement distinguishes direction from size and notes shared assumptions; 2 = one error; 1 = not run; 0 = none.

**EX046 — Question bank.** *Objective:* prepare for the defense. *Inputs:* §8.2. *Constraints:* one question from each family; answers of at most 80 words. *Steps:* write the questions and answers for the Triage Rubric Study. *Expected evidence:* nine question–answer pairs. *Rubric:* 3 = questions sharp, answers concede, quantify and propose tests where appropriate; 2 = defensive answers; 1 = questions generic; 0 = none.

**EX047 — Counterexample paragraph.** *Objective:* present your own counterexamples. *Inputs:* Lab 8 sequence results; Lab 6 better/same/worse counts; theme 3. *Constraints:* 150–200 words. *Steps:* write the paragraph for the discussion chapter. *Expected evidence:* the paragraph. *Rubric:* 3 = S2 and the three worse analysts presented with what they show and do not show, hypotheses distinguished from findings, no dismissal; 2 = counterexamples minimized; 1 = listed only; 0 = none.

**EX048 — Reproduction report.** *Objective:* act as the independent reader. *Inputs:* the eight labs of this book. *Constraints:* use only what is printed in the book. *Steps:* (1) attempt to reproduce Labs 6–8 from the printed code; (2) record your Python version and any differences; (3) write a half-page reproduction report listing what succeeded, what failed and what the author should document better. *Expected evidence:* the report. *Rubric:* 3 = versions recorded, outputs compared line by line, at least two concrete documentation improvements (for example, the file-name dependency between labs; the seed-choice note); 2 = no versions; 1 = not attempted; 0 = none.

**EX049 — Corrections table.** *Objective:* respond to examination. *Inputs:* three examiner requests: (a) "justify the 30-second timing tolerance"; (b) "the noisy-case result should be described as inconclusive, not null"; (c) "add a mixed-effects logistic model". *Constraints:* you may not collect new data. *Steps:* complete the corrections table for each, stating whether the claim changes. *Expected evidence:* the table. *Rubric:* 3 = (a) justified from the pilot and measurement needs, (b) accepted with wording change, (c) addressed by running the model or explaining how it relates to the estimand, with claim implications; 2 = one request dismissed; 1 = vague; 0 = none.

**EX050 — Partner briefing and next study.** *Objective:* share results and plan what follows. *Inputs:* the whole study. *Constraints:* a one-page briefing for MRSS and a half-page next-study proposal. *Steps:* (1) write the briefing with result, scope, cost, dependence on the reference standard and a recommendation; (2) propose the next study, naming its question, design and the rival it addresses that this study could not. *Expected evidence:* the two documents. *Rubric:* 3 = briefing accurate and scoped with no individual data, recommendation conditional, next study addresses a named limitation (live conditions, a second reference panel, rubric-completion timing); 2 = overclaims; 1 = generic; 0 = none.

### Chapter synthesis

Examiners look for claims larger than evidence, untraceable numbers and unaddressed rivals. Prepare a reproduction package and ask an independent reader to rerun and attack it. Answer "what if" questions with a specification curve of defensible choices, identifying duplicates and shared assumptions. Present your own counterexamples. In the defense, concede valid points, quantify what they change and propose tests. Record corrections with an audit trail and re-check numbers. Share results with participants first, partners with scope and limits, and the profession with materials others can use to replicate.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 08

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

Each worked result shows one defensible answer and explains what the rubric rewards. A different answer can earn full credit when it meets the same standard of evidence, scope and honesty about limits. Numerical results come from the offline labs in this book run with Python 3 (3.13 was used for this draft) and the standard library only; if your output differs, first check the Python version, the seed, and whether you changed the order of random draws. Every case, organization, person and number is synthetic unless a cited source is named.

### Chapter 1: EX001–EX007

**EX001 — From topic to question.** *Problem:* a CSIRT manager must decide whether to require a written handover note at every shift change during incidents lasting more than one shift, but does not know whether notes reduce information lost at handover or merely add work. *Question:* among responders handing over a simulated multi-shift incident (P), does a structured written handover note (E), compared with verbal handover only (C), reduce the number of predefined critical facts the incoming responder cannot report or act on within 15 minutes (O), measured at each handover (T)? *FINER:* feasible with volunteers and fictional incidents, not with live incidents (records and consent are unobtainable); interesting because handover failures are a known source of lost context; novel to the extent the search finds no controlled security study; ethical if participants consent and results are not shared with employers; relevant to the manager's decision. *Claim and scope:* "In a simulated setting, structured notes reduced lost critical facts by X" — not a claim about live incidents or long-term outcomes. The outcome is measured by an observer against a predefined fact list, not by self-report. *Rubric note:* full credit needs an honest feasibility statement; a question that requires access to a real CSIRT's incidents without saying how is a 1.

**EX002 — Question types.**

| Q | Type | Minimum design | Strongest claim |
|---|---|---|---|
| (a) | Descriptive | Defined sample of 2025 tickets with review outcome | "X% of reviewed 2025 tickets were re-graded upward" |
| (b) | Associational | Comparison of night and day tickets with case mix and staffing recorded | "Night tickets were more often under-triaged, after adjusting for…" |
| (c) | Causal | Randomized or crossover controlled design | "The rubric reduced under-triage under these conditions" |
| (d) | Explanatory | Interviews, think-aloud, process tracing | "Analysts described…; consistent with…" |
| (e) | Causal (historical) | DiD with a comparison team and tested assumptions; ideally a design that separates co-interventions | At best "consistent with an effect after adjustment", because the senior hires coincide with adoption |

*Rubric note:* (e) is the discriminating item: a student who says "DiD answers it" without mentioning the co-intervention earns 2.

**EX003 — Search protocol and known-item test.** *Blocks:* setting (SOC, CSIRT, "incident response team", "security analyst*", "security operations"); decision (triage, prioriti*, severity, escalat*, classif*, "under-triage"); exposure (rubric, checklist, "decision aid", "decision support", scale, protocol, playbook, "structured assessment"). Separate transfer search: (triage OR "time pressure") AND (checklist OR "decision aid" OR "cognitive aid") limited to emergency medicine and human factors. *Sources:* ACM Digital Library and IEEE Xplore (security venues); a multidisciplinary citation index (human factors, safety); a psychology index (decision making); grey literature from national CSIRTs and agencies, standards bodies (NIST, FIRST), professional conference proceedings with slides, and theses repositories. *Known items:* three studies the supervisor names, for example a SOC field study ([Sundaramurthy et al. 2014](https://doi.org/10.1145/2663887.2663904)), a SOC practitioner study ([Kokulu et al. 2019](https://doi.org/10.1145/3319535.3354239)) and a checklist study outside security ([Haynes et al. 2009](https://doi.org/10.1056/NEJMsa0810119)) for the transfer search; check retrieval by DOI after deduplication. *Stopping rule:* stop chaining after two consecutive rounds add no included study. *Log template:* date, source, interface, exact query string, filters, number of hits, export file name, notes. *Rubric note:* known items must be chosen before the search, and the log must allow an exact re-run.

**EX004 — Run and extend Lab 1.** (1) The output is as printed in §1.9. (2) The appended record is removed as a duplicate: normalization replaces the hyphen in "Time-Pressure" with a space and lower-cases the title, so its key ("checklist use under time pressure in emergency triage", 2018) matches the existing psychology record; the assertion still holds and the first output line becomes `records exported: 15  duplicates removed: 4  unique: 11` and the rest is unchanged. (3) With reviewer B's decision on the mean-time-to-respond record changed from I to X (B becomes `IIIXXIXXXXI`), raw agreement rises from 8/11 = 0.727 to 9/11 = 0.818, and kappa from 0.441 to 0.645 (reviewer A includes 7 of 11, B now 5 of 11; chance agreement = (7×5 + 4×6)/121 = 59/121 = 0.488; κ = (0.818 − 0.488)/(1 − 0.488) = 0.645). (4) Kappa divides the agreement *above chance* by the room above chance; with eleven records and similar marginal rates, chance agreement is near one-half, so one record moves the numerator by 1/11 while the denominator is only about one-half — roughly doubling its effect relative to raw agreement. Small screening samples give unstable kappas; use them to find disagreements, not to grade reviewers.

**EX005 — Repair the eligibility criteria.** *Inclusion:* empirical studies (quantitative, qualitative or mixed) of how security analysts or incident responders classify, prioritize or escalate incidents or alerts; studies that evaluate a structured aid for those decisions; methodological studies of how triage outcomes are *measured* if they report data. *Exclusion:* opinion pieces and vendor marketing without a described method; studies of automated prioritization with no human decision. *Grey literature:* include reports from public bodies and CSIRTs that describe their data source and definitions; exclude those that do not. *Cross-domain:* studies outside security go to the separate transfer search, not the main review. *Applied:* the MTTR record — include if it reports empirical data on the measure's behaviour (a measurement study), otherwise exclude; the CSIRT annual report — include only if it defines its categories and data source, so send to full text; the emergency-triage checklist — transfer search, not the main review. *Undecidable at title/abstract:* advance to full-text review; never exclude for lack of information.

**EX006 — Concept matrix with a real study.** The abstract of [Haynes et al. (2009)](https://doi.org/10.1056/NEJMsa0810119) describes a prospective study in eight hospitals in eight cities, with data collected before and after introduction of the surgical safety checklist; the rate of death fell from 1.5% to 0.8% and inpatient complications from 11.0% to 7.0%. The row is correct as "pre–post, eight hospitals, no concurrent control". *Added column:* "what it can say about experienced professionals" — it involved practising surgical teams, but outcomes are patient outcomes of team processes, not individual classification decisions; it cannot separate the checklist from co-occurring changes. *Paragraph (sketch):* Structured aids for time-pressured classification have been studied mainly outside security. In surgery, a checklist was followed by fewer complications in a before–after study, but the design cannot separate the checklist from secular change or observation effects. Within security, field studies describe triage as tacit and shaped by local metrics, and one synthetic tabletop with students found higher accuracy with a checklist, but with an answer key of uncertain validity and a population unlike working analysts. Agreement studies show that scale wording changes inter-analyst agreement, without testing accuracy against an independent reference. In the sources searched, no study compared a severity rubric with usual judgement within experienced analysts, separated under- from over-triage, and used an independent reference — the gap this study addresses. *Rubric note:* any number quoted from Haynes must match the abstract; the student must read it rather than rely on this answer.

**EX007 — Estimand and scope memo.** *RQ1:* population — analysts with ≥ six months' triage experience; conditions — SEV-4 versus usual judgement, within analyst; outcome — under-triage (rating ≤ reference − 1) on each high-impact case; summary — mean across analysts of (rubric proportion − usual proportion), in percentage points; intercurrent events — analysts missing a period are excluded from the primary analysis and bounded in sensitivity; rubric use in a usual session is a deviation analysed in sensitivity. *RQ2 time:* same population and conditions; outcome — seconds from case presentation to first written severity; summary — difference in medians across all decisions by condition (secondary), with per-analyst median differences reported as a check. *Careless alternatives:* (i) the pooled proportion of all high-impact decisions under each condition, which weights analysts by number of decisions and invites an interval that ignores clustering; (ii) the relative reduction (or odds ratio), which looks larger when the baseline is high and is not the decision-maker's quantity; (iii) the critical-only rate, which may be chosen because it is largest. *Claim:* "the rubric reduced under-triage of high-impact fictional cases by X points among experienced volunteers". *Out of scope:* the prevalence of under-triage in live operations; effects on novices.

### Chapter 2: EX008–EX014

**EX008 — Map the models.**

| Model | From the ticketing system | Needs extra collection | Measure improves while the goal worsens |
|---|---|---|---|
| Speed | Median time to close | Time to containment confirmed by a second source | Analysts close tickets early and reopen new ones; hard cases left open past the reporting window |
| Accuracy | Severity changes after review | Independent panel reference for a sample | Analysts rate everything high: under-triage falls, over-triage and fatigue rise |
| Harm reduction | Count of incidents with outage flag | Service downtime from service logs; records exposed | Fewer incidents classified as "outage" because the definition is narrowed |
| Resilience | Recurrence of the same root cause | After-action quality review; continuity of minimum service | After-action reports are produced on time but contain no changes |

**EX009 — Extend Lab 2.** With a 168-hour window:

```text
method  closed  mean_h(closed)  median_h(closed)  under-triage(high-impact)  still_open
     R     300            12.3               5.4               9.7% of  93           0
     U     299            16.2               5.6              23.7% of  93           1
R: median hours including open cases (open = >168h, rank only): 5.4  share closed within 24h: 82.7%
U: median hours including open cases (open = >168h, rank only): 5.7  share closed within 24h: 80.7%
```

The mean comparison reverses: U's mean among closed incidents rises from 10.2 to 16.2 hours, because 19 of its 20 previously open incidents — mostly late-discovered missed high-impact cases with very long resolution times — now close inside the window and enter the mean. R's mean rises less (11.3 to 12.3) because it had only 4 open. Under-triage and the share closed within 24 hours do not change: they do not depend on the window length (every incident is counted, and its triage outcome or 24-hour status is fixed). The lesson for Study P: its conclusion depended on an arbitrary study-window length.

**EX010 — Predictions from theory.** *Situation awareness:* the effect is concentrated in quiet-impact cases and does not depend strongly on experience. *Naturalistic decision making:* the effect is larger for less experienced analysts and the time cost is larger for experts. *Alert overload:* the effect is larger when the case presents with very few alerts, independent of impact type (a design would need a factor varying alert volume holding impact constant). *Data required:* case type (quiet/noisy) — recorded; experience band — recorded; per-case alert count — must be recorded in the case design. *Not testable as designed:* the alert-overload prediction, because in the case set alert volume and quiet-impact status are confounded (quiet cases are by construction low-noise); separating them would need cases with high impact and many alerts, and low impact and few alerts.

**EX011 — Read a real study with the protocol.** [Alahmadi, Axon and Martinovic (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi) report a qualitative study of SOC practitioners' perspectives on security alarms based on interviews and an online survey. (1) *Question/model:* how practitioners experience and handle alarms; implicitly an alert-overload view of effectiveness. *Unit/population:* practitioners recruited for interviews and survey responses; self-selected. *Exposure:* none assigned; the study is descriptive and explanatory. *Outcome/source:* practitioners' accounts. *Completeness:* the learner should report what the paper says about recruitment and response numbers. *Rivals:* accounts may reflect salient experiences rather than typical ones. *Transfer:* to SOC practice broadly, as perceptions. (2) Indirect evidence for RQ1 (it does not test an aid against a reference); more direct for RQ3, as it documents the reasoning context in which discounting happens. (3) *Design influence:* include in the case set cases where a high-impact incident is embedded in routine false-positive noise, and ask in debriefs about discounting of familiar alarms. *Rubric note:* the learner must check details against the paper; this answer deliberately avoids quoting numbers the learner should find.

**EX012 — The disagreement statement.** Use §2.8 and add: "A shared reanalysis would narrow the disagreement: compute time to resolve with open incidents treated as censored (for example, the share resolved within fixed times over a common window), and add a harm measure — hours of service affected — available for both studies. If the rubric's longer closed-case times are offset by fewer long-open missed cases, the speed disagreement disappears; if not, the trade-off is real and the decision-maker can weigh it." *Rubric note:* full credit requires no verdict and a concrete narrowing analysis.

**EX013 — Choose and justify outcomes.** *Primary:* under-triage of high-impact cases (rating ≤ reference − 1, reference 3–4), per analyst per condition — justified because the manager's concern is high-impact incidents that wait. *Secondary:* (1) median seconds to first written rating — guards against an unaffordable cost; (2) over-triage of low-impact cases — guards against "rate everything high"; (3) weighted kappa against reference — summary agreement for comparison with other studies; (4) under-triage by case type — tests the mechanism predicted by situation awareness. *Rejected:* mean time to resolve — the tabletop has no resolution phase, and Lab 2 shows the measure's sensitivity to censoring and escalation costs.

**EX014 — Evidence grading.**

| Row | For RQ1 | For the historical MRSS question |
|---|---|---|
| Field study of SOC severity triage | Indirect: describes the decision, no aid tested | Indirect: shows recording practice can drift, a rival for ticket-based outcomes |
| Checklist tabletop with students | Indirect: related aid and outcome, different population | Design-only |
| Interrater reliability of scales | Indirect: agreement, not accuracy | Design-only (measurement) |
| Haynes et al. 2009 | Design-only: different profession and outcome | Design-only, but instructive: the same pre–post rivals threaten MRSS's historical data |

### Chapter 3: EX015–EX020

**EX015 — Choose a design.** *Counterfactuals:* cross-sectional — West's tickets stand in for East-without-rubric (assumes teams comparable); pre–post — East-2024 stands in for East-2025-without-rubric (assumes nothing else changed); DiD — West's change stands in for East's change without rubric (parallel trends); parallel tabletop — randomized other analysts stand in (randomization balances analysts, but variance is large); crossover — the same analyst on matched cases stands in (no carryover, balanced periods, comparable sets). *Choice:* crossover tabletop, because it removes stable analyst differences, which Lab 3 shows dominate variance, and because its assumptions can be balanced and checked; recruitment of 24 is feasible. *Cannot answer:* prevalence of under-triage and effect in live operations; the historical strand provides context on prevalence and on whether the operational data are consistent with an effect, not a causal estimate.

**EX016 — Carryover and period checks.** *Period effect:* for each analyst compute (period-2 under-triage − period-1 under-triage). In U→R sequences this equals rubric effect + period effect; in R→U sequences it equals −rubric effect + period effect. Half the sum of the two group means estimates the period effect; half the difference estimates the rubric effect. *Carryover:* compare the usual-judgement proportions of rubric-first analysts (their period 2) with those of usual-first analysts (their period 1), adjusting for the period effect; carryover predicts better usual-judgement performance among rubric-first analysts. Formal tests of carryover in a two-period crossover have low power, so the check is descriptive. *If found:* report the period-1 comparison (rubric-first versus usual-first analysts, each in their first period) as a parallel-group estimate free of carryover, with its wider interval, alongside the crossover estimate, and discuss the difference.

**EX017 — Run and extend Lab 3.** Adding:

```python
p, x, w, m = design_check("crossover", 36, 8, 0.30, 0.20)
print(f"EX017: crossover n=36, 8 high-impact per condition, effect -0.10: power {p:.2f}, exaggeration {x:.2f}")
```

prints `EX017: crossover n=36, 8 high-impact per condition, effect -0.10: power 0.73, exaggeration 1.10`. *Recommendation:* at the smallest effect of interest, 36 analysts raise power from about 0.56 to 0.73 and reduce exaggeration from 1.24 to 1.10. That is a real gain, but three extra months threaten the critical path. A defensible recommendation is to plan for 24 with an extension to 36 if recruitment runs ahead of schedule, and in either case to report the estimate and interval rather than a significance verdict; the dissertation states that a true 10-point effect may not reach conventional significance with 24 analysts.

**EX018 — Ethics risk table.**

| Risk | Likelihood | Severity | Mitigation | Residual |
|---|---|---|---|---|
| Employer sees individual results | Low | High | No individual results shared; pseudonyms; key separate | Low |
| Coercion via manager or ex-colleague recruitment | Medium | Medium | Neutral channels; non-participation invisible | Low |
| Re-identification in small tables | Medium | Medium | Minimum cell sizes; no team × experience × sequence cells | Low–medium |
| Real indicators or configurations in cases | Low | High | Second-person review of vignettes; fictional systems | Low |
| Distress under timed simulation | Low | Medium | Right to stop; pauses; support contacts | Low |
| Interview data retained too long | Medium | Medium | Delete recordings after checking; retention period stated | Low |
| Incidental disclosure of real weaknesses in debrief | Low | High | Instruct participants not to discuss real systems; do not record such content | Low |

**EX019 — Pre-analysis plan.** A one-page plan containing: hypotheses (H1: rubric reduces under-triage of high-impact cases; H2: the reduction is larger in quiet-impact cases); primary outcome and estimand as in EX007; analysis — mean of per-analyst differences, percentile bootstrap (4,000 resamples of analysts, seed 1), sign-flip test (20,000 flips, seed 2); secondary outcomes as in EX013; checks — period, carryover (descriptive), fidelity; robustness — two-level threshold, severity ≥ 2 inclusion, critical-only, minority reference for split cases; missing data — complete pairs primary, bounds for withdrawals; *deviation rule:* any change after the first main-study session is logged with date, reason, whether outcome data had been examined, and whether the change affects confirmatory analyses; changes made after outcome data were examined render affected analyses exploratory. *Confirmatory:* H1 only; everything else secondary or exploratory.

**EX020 — Reproducible project.** *README (outline):* purpose; licence; requirements (Python 3.13, standard library only); folder layout as in §3.6; "to reproduce: (1) place the raw exports in `data/raw/` (restricted) or run `code/make_synthetic.py` to create the synthetic stand-in; (2) run `code/clean.py`; (3) run `code/analyse.py`; (4) run `code/check_numbers.py` against `dissertation/numbers.csv`"; seeds listed; expected outputs listed with hashes. *Synthetic stand-in:* generated by the same code as Lab 6 with the same variables, case structure and sequences, but participant-level values drawn from the generator, so it reproduces the pipeline and table shapes without describing any real person. *Restricted access:* a reviewer may access the de-identified decision-level data in the university's secure environment under a data use agreement; transcripts are not available.

### Chapter 4: EX021–EX026

**EX021 — Rival table for a different claim.**

| Explanation | Mechanism | Distinct prediction | Data |
|---|---|---|---|
| 12-hour shifts | Fewer handovers lose less context | Improvement concentrated in incidents spanning former shift boundaries | Time to contain by whether an incident crossed an old boundary |
| Staffing level | More analysts on shift | Improvement tracks headcount per shift, including in incidents not crossing boundaries | Rosters |
| Case mix | Fewer complex incidents | Mix of incident types changed; improvement vanishes after standardizing | Type distribution before and after |
| Tooling | New EDR or SOAR at the same time | Improvement begins at the tool's deployment date, not the shift change | Change calendar |
| Recording of "contained" | Definition loosened | Gap between "contained" and independent evidence of containment grows | Sample audit against host evidence |
| Censoring | More incidents left open past the reporting cut-off | Open-count rises; share contained within fixed time unchanged | Open incidents at cut-off |
| Regression to the mean | Change followed an unusually bad quarter | Pre-period atypical against longer history | Two years of quarterly data |

**EX022 — Causal diagram.** Add *telemetry coverage of the affected service*: it affects under-triage (impact is visible or not) and may differ by team (East's school networks are better instrumented), so it is a confounder of team/rubric → outcome and belongs in the adjustment set if measured; it may also modify the rubric's effect (the rubric helps most where impact is not visible in telemetry). Add *ticket reopened*: it is influenced by under-triage (missed cases reopen) and may be influenced by the rubric; it is post-outcome and a collider on some paths — do not adjust for it. *Classification:* seniority — confounder; case mix — confounder; recording practice — confounder of the measured outcome; telemetry — confounder/effect modifier; asset-inventory lookup time — mediator; reopened — post-outcome collider. *Adjustment set:* {seniority, case mix, telemetry coverage}, with recording practice handled by using the panel-reviewed outcome.

**EX023 — Run and modify Lab 4.** With East's 2025 senior share set to 0.38:

```text
A crude 2025 contrast   East 0.106  West 0.179  difference -0.073
B East before/after     2024 0.159  2025 0.106  change -0.053
C difference-in-diff    East change -0.053 minus West change -0.013 = -0.039
D standardized DiD      (seniority x case type held at the 2024 mix) = -0.044
E negative control      misrouting DiD = -0.002  (rubric cannot affect routing)
  senior share          East 2024 0.34 -> 2025 0.38;  West 0.33 -> 0.38
  quiet-impact share    East 0.42  West 0.55
  generator truth       rubric effect on East 2025 = -0.030 (absolute risk)
```

With the East-specific seniority change removed, parallel trends hold by construction (both teams change seniority equally), so DiD (−3.9 points) and standardized DiD (−4.4) now agree with each other to within sampling noise (each has a standard error of roughly two points with 1,500 tickets per cell) and are close to the true −3.0. The crude contrast remains biased by case mix (East has fewer quiet cases). The negative control falls to −0.2 points, essentially zero: it was signalling the co-intervention, and with the co-intervention gone the warning disappears.

**EX024 — Negative controls.** *Negative-control outcome:* include in each session four "identification" questions per period (for example, "which service owns this host?", answerable from the case packet) whose accuracy the rubric should not change; a rubric "effect" on them would suggest that rubric sessions differed in attention or time allowed, not that the rubric improved severity judgement. *Negative-control exposure:* a small sham arm — an equally long unrelated checklist (for example, about formatting the ticket) — given to a subset; if the sham reduces under-triage as much as SEV-4, the effect comes from slowing down or from being observed, not from the rubric's content. A non-null negative control would be reported and would weaken the causal interpretation; a null one supports but does not prove it.

**EX025 — Sensitivity statement.** East's senior share rose by 0.31 (0.34 → 0.65) and West's by 0.05 (0.33 → 0.38), a relative change of 0.26. With a seniority effect of −10 points, the senior hires alone would produce a DiD of about −10 × 0.26 ≈ −2.6 points. The observed DiD is −5.3 points, leaving about −2.7 points attributable to the rubric (close to the generator's −3.0). *Statement:* "If seniority were unmeasured, a seniority effect of the size seen in West could account for about half of East's difference-in-differences. The data therefore cannot distinguish a rubric effect of about three points from one near zero unless seniority is measured and adjusted for."

**EX026 — Rivals for the tabletop.**

| Rival | Prediction | Mitigation | Check |
|---|---|---|---|
| Carryover | Rubric-first analysts' usual period better than usual-first analysts' usual period | Balanced sequences | Descriptive carryover comparison; first-period parallel estimate |
| Observer expectation | Times recorded differently by condition | Two observers on a sample; observers not told hypothesis | Inter-observer timing agreement by condition |
| Demand characteristics | Participants rate higher when given a rubric because they infer the hypothesis | Neutral instructions; rubric presented as one of two methods | Over-triage of low-impact cases; noisy-case null |
| Fidelity failure | Rubric completed after deciding | Facilitator check | Rubric completion time stamp (added after this study, see §6.9) |
| Artificiality | Effects larger than in live work | Realistic case materials; time limit | Discussed as directional limitation |

### Chapter 5: EX027–EX032

**EX027 — Proposal summary.** *Problem and question:* MRSS must decide whether to mandate SEV-4; RQ1 asks whether it reduces under-triage of high-impact cases versus usual judgement (estimand: mean within-analyst difference), RQ2 its costs, RQ3 analysts' reasoning; scope: experienced volunteers, fictional cases. *Background:* SOC triage is tacit; structured aids help in other fields under designs with known rivals; no controlled within-analyst study was found. *Design:* randomized four-sequence crossover tabletop; historical tickets as context. *Participants:* 24 analysts with ≥ six months' experience via neutral channels; stratified allocation. *Materials:* 24 cases with independent panel reference, rubric, observer form v1.1, debrief guide. *Measures and analysis:* pre-analysis plan with bootstrap and permutation inference. *Rivals:* rival table with checks. *Pilot:* ten sessions with progression criteria. *Ethics and data:* committee approval, pseudonyms, restricted data, synthetic stand-in. *Timeline and risks:* critical path ethics → cases → pilot → recruitment. *Outputs:* dissertation, reproduction package, partner briefing. *Fallback:* "If only 16 analysts complete both periods, the study will report the estimate and its interval as planned; Lab 3-style design analysis indicates lower power, so the dissertation will state the smallest effect the interval can exclude rather than interpret non-significance as absence of effect."

**EX028 — Critical path and risk register.** *Critical path:* ethics approval (6–10 weeks) → case writing and panel reference (month 3–4) → pilot (month 5) → amendment (month 6) → recruitment (months 7–9). Slack: two weeks after approval, one month after recruitment. *New risks:* (1) a panel member leaves before the reference is fixed — trigger: fewer than three panel members available by month 4; response: recruit a replacement from a pre-agreed reserve list and record the change; owner: supervisor. (2) A partner asks to revise the rubric mid-study — trigger: any request after the pilot; response: decline for this study, offer to test the revision in a follow-up; owner: student. *If the schedule slips two months:* the analysis plan is unchanged; writing time is compressed and, if necessary, the qualitative strand is reduced to eight interviews, a change logged as a deviation.

**EX029 — Run and modify Lab 5.** Filling observer 2's four blank times in completed sessions with observer 1's values gives:

```text
completion        9/10 = 0.90  (>= 0.80)  GO
field completeness 161/162 = 0.994  (>= 0.90)  GO
timing agreement  48/54 pairs within 30 s = 0.889  (>= 0.80)  GO
  disagreements concentrated in cases: C3, C5
unclear flags     C1:0  C2:0  C3:7  C4:0  C5:1  C6:0  (<= 3 per case)  STOP
session length    over 90 min: P05 (96)  AMEND
blank fields among completed sessions: observer-1 time 0, observer-2 time 0, severity 1
```

Completeness rises from 157/162 to 161/162 (the remaining blank is a severity) and agreement from 44/50 to 48/54, because four new pairs, all agreeing by construction, join the denominator. The C3/C5 conclusion does not change: those disagreements arise from an undefined decision moment, not from missing fields, and the filled values are in other cases.

**EX030 — Progression criteria for a different pilot.**

| Criterion | Green | Amber | Red | Main-study requirement |
|---|---|---|---|---|
| Completion of both tests | ≥ 0.85 | 0.70–0.84 | < 0.70 | Paired pre/post scores needed for the primary analysis; precision assumed 85% completion |
| Item completeness | ≥ 0.95 of items answered | 0.90–0.94 | < 0.90 | Scale scoring requires ≤ 1 missing item per test |
| Item difficulty | No item answered correctly by > 90% at pre-test | 1–2 such items | > 2 | Ceiling items cannot show change; replace them |
| Time to complete | ≤ 25 min median | 26–35 | > 35 | Session limited to 60 minutes including the intervention |
| Item clarity | ≤ 2 "unclear" flags per item | 3–4 | > 4 (item cannot be used unrevised) | Valid items |

**EX031 — Deviation log.**

| Date | Code | What happened | Why | Affects primary outcome? |
|---|---|---|---|---|
| (session date) | A09 | Session run with one observer | Observer 2 ill | No: ratings are participant-written; timing agreement sample reduced by one session |
| (session date) | A14 | Rubric sheet on desk during usual period; analyst reports glancing twice | Facilitator did not remove materials between periods | Yes: fidelity failure contaminating the comparison; primary analysis keeps A14 as predeclared; sensitivity analysis excluding A14 reported |
| (session date) | A20 | C19 shown before C18 | Packet collation error | Minor: order within period not part of the design; noted; check whether either case's result is unusual |

**EX032 — The pilot report paragraph.** "Nine of ten booked participants completed the session (0.90; green). In completed sessions, 157 of 162 required observer fields were recorded (0.969; green); four of the five blanks were observer 2's time, which sits on the form's second page. Observer times agreed within 30 seconds for 44 of 50 complete pairs (0.880; green), but all six disagreements occurred in cases C3 and C5, where participants could revise a provisional rating; the timed decision was not defined precisely. Seven participants flagged C3 as unclear (red at case level). One session exceeded 90 minutes (amber). *Decision:* amend, then proceed. The observer form defines the timed decision as the first written severity and moves both time fields to page one; C3 is rewritten and re-rated by the panel; sessions are restructured with a break, subject to an approved amendment. No effect of the rubric was estimated from pilot data; ratings were checked only for completeness."

### Chapter 6: EX033–EX038

**EX033 — Data dictionary and cleaning log.** *Added variables:* `rubric_done_s` — integer seconds from case presentation to the facilitator's mark that the rubric sheet was completed (R sessions only; source: facilitator sheet v1.2; missing in this study, recommended for future ones); `seconds_o2` — observer 2 time (source: observer form; used only for agreement). *Cleaning log (first steps):* (1) import answer sheets `raw/answers_*.csv` (576 rows expected = 24 analysts × 24 cases; script `clean.py` lines 10–22); (2) check codes against the allocation list; 0 unknown codes; (3) remove the 12 placeholder rows of A17 period 2 (withdrawal recorded on 2026-xx-xx); rows 576 → 564; (4) join panel reference v1.1 by case; 0 unmatched; (5) compute `under` and `over` flags; check counts against a hand tally of three sheets.

**EX034 — Run Lab 6 and interpret.** The output is as printed in §6.4. *Report:* "Averaged over the 23 analysts who completed both periods, under-triage of high-impact cases was 17.4 percentage points lower with the rubric than with usual judgement (95% bootstrap interval 9.8 to 24.5 points lower; sign-flip permutation p = 0.0005). Nineteen analysts had lower under-triage with the rubric, one the same and three higher." *Clustering:* the 368 high-impact decisions are not independent — each analyst contributes 16, sharing that analyst's tendencies — so a binomial interval on the pooled proportions would treat 368 observations as if they were independent and be too narrow; the per-analyst differences are the independent units.

**EX035 — Withdrawal sensitivity.** Printing `min(d)` and `max(d)` gives −0.500 (largest improvement) and +0.250 (largest worsening); the 23 differences sum to −4.000. If A17's difference were +0.250, the mean of 24 would be (−4.000 + 0.250)/24 = −0.156; if −0.500, (−4.000 − 0.500)/24 = −0.1875. The primary estimate would lie between −15.6 and −18.8 points: a single withdrawal for reasons unrelated to the rubric cannot change the conclusion. The assumption — that the withdrawal is unrelated to the unobserved result — is stated, and the bound shows the result is insensitive to it within the observed range.

**EX036 — Period and carryover.** For U→R analysts, period-2 minus period-1 = rubric effect + period effect = −0.148; for R→U analysts, = −rubric effect + period effect = +0.198. Adding and halving: period effect ≈ (−0.148 + 0.198)/2 = +0.025. Subtracting and halving: rubric effect ≈ (−0.148 − 0.198)/2 = −0.173, consistent with the primary −0.174. Carryover (rubric-first analysts keeping some benefit in their later usual period) would make the R→U change *smaller* than the U→R change in absolute value, because their usual period would be better than it otherwise would be; here the R→U change is *larger* (0.198 versus 0.148), the opposite of what carryover predicts. With five or six analysts per sequence this is weak evidence either way; it does not suggest carryover, and the dissertation reports it descriptively.

**EX037 — Codebook entry.**

| Code | Definition | Include when | Exclude when | Example |
|---|---|---|---|---|
| Post-hoc completion | Participant describes filling the rubric after having decided a rating | Participant says they decided first, then completed the sheet | Participant used the rubric and then disagreed with it | "I knew it was a 2, so I just ticked through" (synthetic) |
| Overriding the rubric | Participant completed the rubric first but chose a different rating from what it indicated | Explicit description of disagreeing with the rubric's result | Rubric completed after deciding | "The sheet said 3 but I knew the job was a test system" |
| Time pressure | Participant attributes a decision to the session's time limit | Mentions the clock, rushing, wanting to move on | Mentions the rubric's length without time pressure | "I was watching the timer on that one" |

**EX038 — Joint display with discordance.** *Row:* question — "Where is the rubric most valuable?"; quantitative — critical-only difference −24.6 points with a wide interval (−37.7 to −10.1), based on three critical cases per set; qualitative — several interviewees said the rubric "mattered most on the really bad ones"; *integration* — partially discordant: interviews locate the value in critical cases while the quantitative strand locates it in quiet-impact cases (which include critical and severity-3 cases); the critical-only estimate is large but imprecise and overlaps with the high-impact estimate, so the strands cannot be reconciled with these data. *Resolving data:* a case set crossing critical/severity-3 with quiet/noisy, with enough cases per cell to estimate the interaction.

### Chapter 7: EX039–EX044

**EX039 — Results-to-claims register.**

| Claim | Evidence | Design support | Scope | Strength |
|---|---|---|---|---|
| "Agreement with the reference standard was higher with the rubric (weighted kappa 0.76 vs 0.62)." | Secondary outcome | Crossover; pooled decisions; no interval in the plan | Fictional cases, this panel | Moderate; descriptive secondary |
| "Some analysts described the rubric as justification for escalating cases with few alerts." | Theme 4 | Debrief interviews, purposive sample | Participants' accounts | Hypothesis-generating; not an effect on escalation |
| "The rubric would help novice analysts more." | None | Novices not eligible (≥ six months' experience) | Outside the sample | Not supported; possible future study |

**EX040 — Run and fix Lab 7.** Corrected draft entries: `("Results 5.4", "0.76", "kappa_R")`, `("Results 5.5", "45", "extra_seconds")`, `("Discussion 6.1", "23", "n_complete")`; rerun prints `0 of 9 printed numbers do not match the analysis output`. Adding over-triage results:

```python
low = lambda c: [r["rating"] > r["ref"] for r in ROWS if r["cond"] == c and r["ref"] <= 2 and r["analyst"] in both]
RESULTS["over_U"] = (sum(low("U")) / len(low("U")), "{:.3f}")
RESULTS["over_R"] = (sum(low("R")) / len(low("R")), "{:.3f}")
DRAFT += [("Results 5.4", "0.261", "over_U"), ("Results 5.4", "0.239", "over_R")]
```

placed before the checking loop, gives `0 of 11 printed numbers do not match the analysis output`.

**EX041 — Calibrated sentences.** (a) "In quiet-impact fictional cases, under-triage was 37 percentage points lower with the rubric; it was not eliminated." (b) "In MRSS historical tickets, senior analysts' tickets were less often under-triaged; this is an association, not tested causally in this study." (c) "No difference was detectable on noisy cases (+2.2 points); the study was not designed to rule out small effects there." (d) "Several experienced participants described the rubric as slowing them down on cases they found obvious." (e) "If these results transfer to live triage, mandating the rubric could reduce under-triage of quiet-impact incidents at a cost of about 45 seconds per case; a live pilot with time-stamped rubric completion would test this before a mandate."

**EX042 — Directional limitations.**

| Limitation | Likely direction | Reasoning and check |
|---|---|---|
| Case writers knew the hypothesis | Probably favours the rubric | Writers may unconsciously construct quiet cases whose missing cues are exactly those the rubric asks about. Check: have a second writer, blind to the rubric, write a replication set |
| The rubric was designed by the student | Probably favours the rubric | Allegiance can shape case construction, facilitation and interpretation. Checks: independent panel, predeclared plan, facilitator script; recommend replication by another team |

**EX043 — Reporting checklist audit.** Crossover-specific items from the [CONSORT extension for randomised crossover trials](https://doi.org/10.1136/bmj.l4378) the learner should locate include: rationale for a crossover design; whether and how carryover was addressed (washout or argument); the number of periods and sequences and how participants were allocated to sequences; analysis methods that account for the within-participant design and period effects; and results reported by period and sequence. *Locations:* rationale in Methods §3.1; carryover argument and check in Methods §3.2 and Results §5.3; sequences and allocation in Methods §3.4 (four sequences, stratified by experience); analysis in Methods §3.7; results by sequence in Results §5.6. *Gap:* no washout; the dissertation must justify why none was used (decisions are on different cases, and a rubric cannot be "washed out" of memory) and present the carryover check honestly. The learner must verify item wording against the published checklist.

**EX044 — Availability statement.** "Analysis code, the pre-analysis plan, case vignettes, the SEV-4 rubric, observer forms and the debrief guide are openly available in the project repository (archived with a persistent identifier). De-identified decision-level tabletop data are available to researchers under a data use agreement, because combinations of variables could identify participants; requests go to the university's research data service. MRSS ticket data were used under a partner agreement that prohibits disclosure; they cannot be shared, but the code that analysed them is available, and a synthetic dataset with the same structure is deposited openly so that the pipeline can be run. Interview transcripts are not available, as participants were promised; the codebook and audit trail are."

### Chapter 8: EX045–EX050

**EX045 — Run and extend Lab 8.** (1) Output as in §8.4.2. (2) The two "ref=4" specifications at each threshold are identical across references, so twelve specifications contain ten distinct ones. (3) Excluding the three analysts with the most negative differences (A13 at −0.500, then A01 and A09 at −0.375; A01, A09 and two others tie, so the choice among tied analysts is arbitrary and should be stated) gives a mean of −0.138 (−13.8 points) over the remaining 20 analysts. (4) "Across ten distinct specifications the difference was always negative, ranging from about 4 to 25 points depending mainly on the error threshold and case set; even excluding the analysts who benefited most, the reduction remained about 14 points. All specifications share the same fictional cases and the same panel, so the curve shows insensitivity to analysis choices, not correctness of the reference or transfer to live work."

**EX046 — Question bank (sample answers).** *Motivation* — "Why under-triage?" — "Because an under-triaged high-impact incident waits; over-triage costs effort. The manager's decision turns on missed incidents." *Design* — "Why no washout?" — "Cases differ by period, and rubric knowledge cannot be washed out; I balanced order and checked carryover descriptively; the pattern was opposite to carryover." *Measurement* — "Is the panel right?" — "Independent and blind to the rubric, but two cases split; under the minority view the effect falls to about 12 points; a second panel is the test." *Analysis* — "Why not a mixed model?" — "The estimand is the mean within-analyst difference in proportions; a mixed logistic model estimates a conditional odds ratio. I can report it as a check; I would expect the same direction." *Robustness* — "Two-level errors?" — "−8.2 points, interval excluding zero." *Rivals* — "Inflated ratings?" — "Over-triage of low-impact cases did not rise; noisy cases unchanged." *Transfer* — "3 a.m. SOC?" — "Probably smaller: fewer quiet cases, more interruptions, more post-hoc completion. A live pilot is needed." *Contribution* — "What is new?" — "In the sources searched, the first within-analyst controlled comparison with an independent reference that separates under- from over-triage." *Reflexivity* — "You designed the rubric." — "Yes; safeguards were an independent panel and a predeclared plan; case construction may still favour it; I recommend independent replication."

**EX047 — Counterexample paragraph.** "The reduction was not uniform. Three of 23 analysts had higher under-triage with the rubric, and two of them described completing the rubric after deciding (theme 3), which suggests that the benefit depends on using the rubric before forming an impression — a condition the study did not control. The effect also varied by sequence, from −27.5 points in sequence 1 (five analysts) to −4.2 in sequence 2 (six). With so few analysts per sequence this variation is compatible with chance, and both case sets were constructed with identical reference distributions; but sequence 2 used set A under the rubric, and differences in the specific quiet-impact cases of set A cannot be excluded. These are hypotheses for future studies, not findings; they argue against presenting the average effect as a property of every analyst or case."

**EX048 — Reproduction report.** A model report records: Python version (for example 3.12.x) and operating system; that Labs 6–8 reproduced exactly when `lab6_data.py` and `lab6_analysis.py` were saved under those names in one folder; any differences (none expected with the standard library's `random` across 3.x versions for these calls, but differences must be reported if found). Documentation improvements: state the file-name dependency at the top of each dependent lab (done in this book, but easy to miss); explain the seed choice for `lab6_data.py` (§6.2) beside the code; list expected run times (Lab 3 takes a few seconds); provide a single script that runs all labs and compares outputs with the printed ones.

**EX049 — Corrections table.**

| Request | Change | Location | Claim changed? |
|---|---|---|---|
| Justify 30-second tolerance | Added paragraph: the tolerance is about 13% of the median decision time (236 s); pilot showed disagreements beyond it were caused by undefined decision moments, now fixed; agreement under ±15 s and ±60 s reported | Methods §3.6; Appendix | No |
| Noisy-case result is inconclusive | Replaced "no effect" with "no difference detectable; not designed to rule out small effects" | Results §5.4; Discussion §6.2; abstract | Yes: weaker |
| Add mixed-effects logistic model | Explained that the predeclared estimand is a difference in proportions; reported a mixed model as an exploratory check run with standard statistical software, noting it estimates a conditional odds ratio, and stated whether its direction and approximate size agreed | Results §5.6; Appendix | No, if direction agrees; otherwise discuss |

**EX050 — Partner briefing and next study.** *Briefing:* "Result: in a controlled tabletop with 23 experienced volunteer analysts on fictional cases, the SEV-4 rubric reduced under-triage of high-impact cases by about 17 percentage points (interval 10 to 25), mainly on quiet-impact cases, at about 45 seconds per case, without increasing over-triage. Limits: fictional cases; effect smaller (about 12 points) if a minority view of two disputed cases is taken as the reference; some analysts completed the rubric after deciding. Recommendation: do not mandate on this evidence alone; run a three-month live pilot in one team with time-stamped rubric completion and panel review of a random ticket sample." No individual data. *Next study:* Question — does SEV-4 reduce under-triage in live triage? Design — stepped-wedge rollout across four teams with monthly panel review of random high-impact tickets, using a second, independent reference panel; addresses the transfer limitation and the reference-standard dependence that the tabletop could not.

<a id="glossary"></a>

## Glossary

- **Audit trail** — Dated records of codebook, theme and protocol changes that let another person follow how an analysis developed.
- **Bootstrap (percentile)** — An interval obtained by resampling the independent units with replacement and taking percentiles of the resampled statistic.
- **Carryover** — An effect of a condition in one period of a crossover that persists into the next period.
- **Censoring** — Incomplete observation of a time-to-event outcome, such as incidents still open when a study window closes.
- **Claim scope** — The population, conditions and setting to which a claim applies.
- **Cohen's kappa (κ)** — Agreement between two raters beyond chance: (observed − chance) / (1 − chance). **Weighted kappa** gives partial credit for near-miss ordinal ratings.
- **Collider** — A variable caused by two others; adjusting for it can create a spurious association between them.
- **Concept matrix** — A table organizing studies by the concepts a review is about, so that synthesis proceeds by concept rather than by author.
- **Confounder** — A variable that affects both exposure and outcome and so distorts their apparent relationship.
- **Counterfactual** — What would have happened to the same unit under a different condition.
- **Crossover design** — A design in which each participant experiences every condition in sequence, so comparisons are within participants.
- **Design analysis** — Simulation of a planned study to estimate power, exaggeration (type M) and sign (type S) errors and the false-positive rate.
- **Difference-in-differences (DiD)** — The change in a treated group minus the change in a comparison group over the same period; assumes parallel trends.
- **Estimand** — The precisely defined quantity a study aims to estimate; distinct from the estimator (method) and the estimate (result).
- **Fidelity** — The extent to which a condition was delivered as intended (for example, the rubric completed before deciding).
- **Joint display** — A table integrating quantitative and qualitative findings on the same question and stating whether they converge, complement or conflict.
- **Known-item recall** — The share of relevant studies identified in advance that a search retrieves.
- **Mediator** — A variable on the causal path from exposure to outcome; adjusting for it removes part of the effect.
- **Negative control** — An outcome the exposure cannot affect, or an exposure that cannot cause the outcome, used to detect bias.
- **Over-triage / under-triage** — Rating an incident more / less severe than its reference severity.
- **Period effect** — A systematic change in outcomes between periods of a crossover, independent of condition.
- **Pilot study** — A small preliminary study testing feasibility, procedures and measurement; not designed to estimate effects.
- **Pre-analysis plan** — A document fixing hypotheses, outcomes, estimand and analyses before data collection.
- **Progression criteria** — Predeclared thresholds deciding whether a main study proceeds, is amended or stops.
- **Quiet-impact case** — In this book's synthetic study, an incident with high business impact but little alert noise.
- **Reference standard** — The independently established "correct" classification against which ratings are judged.
- **Sign-flip permutation test** — A test of a mean within-unit difference that randomly reverses signs to generate the null distribution.
- **Simpson's paradox** — Reversal or disappearance of an association when data are split by a third variable.
- **Specification curve** — The set of results across all defensible combinations of analysis choices, displayed together.
- **Strong inference** — Devising alternative hypotheses and observations that exclude some of them, iteratively.
- **Thematic analysis** — A qualitative method for identifying and interpreting patterns of meaning across data.

<a id="references"></a>

## References

Standards, regulations and web pages change. Versions and dates below are those consulted for this draft (October 2026); re-verify before relying on them.

**Standards, guidance, ethics and law**

- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
- FIRST. [CSIRT Services Framework, version 2.1](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1).
- National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research. [The Belmont Report](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html). 1979.
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025.
- National Institute of Standards and Technology. [SP 800-84, Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final). 2006.
- National Institute of Standards and Technology. [SP 800-184, Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final). 2016.
- United States. [45 CFR Part 46, Protection of Human Subjects](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46) (electronic Code of Federal Regulations, current version).

**Security operations and decision making**

- Alahmadi, B. A., Axon, L., and Martinovic, I. [99% False Positives: A Qualitative Study of SOC Analysts' Perspectives on Security Alarms](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi). USENIX Security Symposium, 2022.
- Endsley, M. R. [Toward a Theory of Situation Awareness in Dynamic Systems](https://doi.org/10.1518/001872095779049543). *Human Factors* 37 (1995): 32–64.
- Haynes, A. B., et al. [A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population](https://doi.org/10.1056/NEJMsa0810119). *New England Journal of Medicine* 360 (2009): 491–499.
- Klein, G. [Naturalistic Decision Making](https://doi.org/10.1518/001872008X288385). *Human Factors* 50 (2008): 456–460.
- Kokulu, F. B., et al. [Matched and Mismatched SOCs: A Qualitative Study on Security Operations Center Issues](https://doi.org/10.1145/3319535.3354239). ACM CCS, 2019: 1955–1970.
- Sundaramurthy, S. C., et al. [A Tale of Three Security Operation Centers](https://doi.org/10.1145/2663887.2663904). ACM Workshop on Security Information Workers, 2014: 43–50.

**Research design, analysis and reporting**

- Braun, V., and Clarke, V. [Using Thematic Analysis in Psychology](https://doi.org/10.1191/1478088706qp063oa). *Qualitative Research in Psychology* 3 (2006): 77–101.
- Chamberlin, T. C. [The Method of Multiple Working Hypotheses](https://doi.org/10.1126/science.148.3671.754). *Science* 148 (1965, reprint of 1890): 754–759.
- Cohen, J. [A Coefficient of Agreement for Nominal Scales](https://doi.org/10.1177/001316446002000104). *Educational and Psychological Measurement* 20 (1960): 37–46.
- Cohen, J. [Weighted Kappa: Nominal Scale Agreement Provision for Scaled Disagreement or Partial Credit](https://doi.org/10.1037/h0026256). *Psychological Bulletin* 70 (1968): 213–220.
- Dwan, K., Li, T., Altman, D. G., and Elbourne, D. [CONSORT 2010 Statement: Extension to Randomised Crossover Trials](https://doi.org/10.1136/bmj.l4378). *BMJ* (2019): l4378.
- Efron, B. [Bootstrap Methods: Another Look at the Jackknife](https://doi.org/10.1214/aos/1176344552). *Annals of Statistics* 7 (1979).
- Eldridge, S. M., et al. [CONSORT 2010 Statement: Extension to Randomised Pilot and Feasibility Trials](https://doi.org/10.1136/bmj.i5239). *BMJ* (2016): i5239.
- Gelman, A., and Carlin, J. [Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors](https://doi.org/10.1177/1745691614551642). *Perspectives on Psychological Science* 9 (2014): 641–651.
- Hernán, M. A., and Robins, J. M. [Causal Inference: What If](https://miguelhernan.org/whatifbook). Chapman & Hall/CRC (freely available online from the authors).
- Hertzog, M. A. [Considerations in Determining Sample Size for Pilot Studies](https://doi.org/10.1002/nur.20247). *Research in Nursing & Health* 31 (2008): 180–191.
- Lakens, D. [Sample Size Justification](https://doi.org/10.1525/collabra.33267). *Collabra: Psychology* 8 (2022).
- Landis, J. R., and Koch, G. G. [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310). *Biometrics* 33 (1977): 159–174.
- Malterud, K., Siersma, V. D., and Guassora, A. D. [Sample Size in Qualitative Interview Studies: Guided by Information Power](https://doi.org/10.1177/1049732315617444). *Qualitative Health Research* 26 (2016): 1753–1760.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *PNAS* 115 (2018): 2600–2606.
- O'Brien, B. C., et al. [Standards for Reporting Qualitative Research: A Synthesis of Recommendations](https://doi.org/10.1097/ACM.0000000000000388). *Academic Medicine* 89 (2014): 1245–1251.
- O'Cathain, A., Murphy, E., and Nicholl, J. [Three Techniques for Integrating Data in Mixed Methods Studies](https://doi.org/10.1136/bmj.c4587). *BMJ* 341 (2010): c4587.
- Page, M. J., et al. [The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews](https://doi.org/10.1136/bmj.n71). *BMJ* (2021): n71.
- Platt, J. R. [Strong Inference](https://doi.org/10.1126/science.146.3642.347). *Science* 146 (1964): 347–353.
- Schulz, K. F., Altman, D. G., and Moher, D. [CONSORT 2010 Statement: Updated Guidelines for Reporting Parallel Group Randomised Trials](https://doi.org/10.1136/bmj.c332). *BMJ* 340 (2010): c332.
- Simmons, J. P., Nelson, L. D., and Simonsohn, U. [False-Positive Psychology](https://doi.org/10.1177/0956797611417632). *Psychological Science* 22 (2011): 1359–1366.
- Simonsohn, U., Simmons, J. P., and Nelson, L. D. [Specification Curve Analysis](https://doi.org/10.1038/s41562-020-0912-z). *Nature Human Behaviour* 4 (2020): 1208–1214.
- Simpson, E. H. [The Interpretation of Interaction in Contingency Tables](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x). *Journal of the Royal Statistical Society, Series B* 13 (1951): 238–241.
- Steegen, S., Tuerlinckx, F., Gelman, A., and Vanpaemel, W. [Increasing Transparency Through a Multiverse Analysis](https://doi.org/10.1177/1745691616658637). *Perspectives on Psychological Science* 11 (2016): 702–712.
- Stodden, V., et al. [Enhancing Reproducibility for Computational Methods](https://doi.org/10.1126/science.aah6168). *Science* 354 (2016): 1240–1241.
- Textor, J., et al. [Robust Causal Inference Using Directed Acyclic Graphs: The R Package 'dagitty'](https://doi.org/10.1093/ije/dyw341). *International Journal of Epidemiology* (2017).
- Vandenbroucke, J. P., et al. [Strengthening the Reporting of Observational Studies in Epidemiology (STROBE): Explanation and Elaboration](https://doi.org/10.1371/journal.pmed.0040297). *PLoS Medicine* 4 (2007): e297.
- White, I. R., Horton, N. J., Carpenter, J., and Pocock, S. J. [Strategy for Intention to Treat Analysis in Randomised Trials with Missing Outcome Data](https://doi.org/10.1136/bmj.d40). *BMJ* 342 (2011): d40.
- Wilkinson, M. D., et al. [The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18). *Scientific Data* 3 (2016).

Companion CyberABC material: the [doctoral Incident Response book](../../../../doctorate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md), which takes these methods to an original contribution validated across contexts; and the practitioner books at [rapid](../../../../rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md), [professional](../../../../professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md) and [technical](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md) level.

**Case boundary.** Marlow Regional Shared Services (MRSS), its East and West teams, the SEV-4 rubric, case vignettes C1–C6 and C01–C24, the reference panel, pilot participants P01–P10, main-study analysts A01–A24, observers O1 and O2, interviewees and their quotations, Studies P and Q, records with DOIs beginning 10.9999/syn, the Triage Rubric Study and every number produced by the labs are invented for teaching. Sources support the general statements beside which they are cited, never the synthetic details.

**Edition metadata.** Draft edition, October 2026. Reviewer: pending. A4 verification: not yet rendered.
