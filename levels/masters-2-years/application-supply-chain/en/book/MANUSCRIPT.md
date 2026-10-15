# Application and Software Supply Chain Security: Master's Course

- Language: English (`en`); course 175, Master's course (2 years).
- Editorial state: **published**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students who must design, run and defend an empirical study of an application-security practice.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: test and review only software you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic code and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one master's student from a recurring broken-access-control problem through literature, seminar, design, competing explanations, pilot, analysis, writing and defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Sofia Almeida** | Master's student and part-time developer | Invented |
| **Dr Marcus Lee** | Supervisor | Invented |
| **Tallyline** | Fictional invoicing and refunds web app | Invented |
| **Kingsreach University** | Fictional university | Invented |

### Core sources

[OWASP Top 10:2021](https://owasp.org/Top10/); OWASP [ASVS](https://owasp.org/www-project-application-security-verification-standard/) 4.0.3 and 5.0.0; OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/) and [SAMM](https://owaspsamm.org/); NIST [SP 800-218 (SSDF)](https://doi.org/10.6028/NIST.SP.800-218); [CWE Top 25](https://cwe.mitre.org/top25/); [SLSA v1.0](https://slsa.dev/spec/v1.0/); Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn a practical application-security problem into a researchable question; (2) search and screen literature systematically; (3) use OWASP and CWE as shared vocabularies; (4) record the search so others can repeat it.

### 1.1 The case

Sofia Almeida is a master's student at the fictional Kingsreach University, supervised by Dr Marcus Lee. She works part-time at the fictional fintech Tallyline, whose web app lets small businesses send invoices and issue refunds. Over a year, penetration tests kept finding the same kind of flaw: users able to see or change records they should not. In March, a customer could view another business's invoice by changing a number in the address. The fix worked, but a similar flaw reappeared two releases later in the refunds feature.

### 1.2 From problem to question

"Why do we keep getting this?" becomes: "Do automated authorisation tests derived from an explicit role matrix reduce the reintroduction of broken access control in a web application, and what else explains the change?" The question names an intervention, an outcome and a demand for alternative explanations.

The second half of the question matters as much as the first. Tallyline changed more than its tests during the study period, and a question that asked only whether findings fell would invite Sofia to credit the tests with everything. Asking what else explains the change commits her, before any data, to look for rival causes such as the framework upgrade.

### 1.3 Shared vocabulary

The OWASP Top 10:2021 ranks Broken Access Control (A01) first; the CWE Top 25 lists related weaknesses such as missing authorisation (CWE-862) and authorisation bypass through a user-controlled key (CWE-639). OWASP ASVS 4.0.3 chapter V4 and ASVS 5.0.0's authorisation chapter give verifiable requirements. Using these names lets Sofia's findings be compared with others.

The March flaw maps cleanly onto this vocabulary: changing a number in the address to view another business's invoice is CWE-639, and the refunds flaw two releases later is a case of missing authorisation, CWE-862. Recording both identifiers for each finding lets Sofia's counts be compared with published data on the same weaknesses.

### 1.4 Search method

Sofia searches two digital libraries and the OWASP project pages with terms for access control, authorisation testing and regression. She records the date, database, query and number of hits, screens titles and abstracts against inclusion criteria (empirical, web applications, access control), and keeps a log of exclusions with reasons.

Her log turned 412 records into 38 after title screening and 11 after full text. Only two of the eleven studied authorisation regression in web applications directly, and none used role-matrix tests in a real team. Because each exclusion has a reason in the log, Dr Lee could accept that gap as defensible rather than as a sign that the search was too narrow.

### 1.5 Grey literature

Standards and testing guides such as the OWASP Web Security Testing Guide (WSTG v4.2) are not peer-reviewed research but define practice; Sofia uses them for definitions, not as evidence of effectiveness.

In practice, the WSTG supplies the description of how to test each role against each endpoint, which Sofia's matrix tests follow. It cannot tell her whether doing so reduces recurring flaws; that is what her twelve releases are for. Keeping the two uses apart prevents a testing guide from being cited as evidence for an effect it never measured.

### 1.6 Developer behaviour

Johnson et al. (2013) found developers avoid static analysis tools that produce many false positives and poor explanations; Sofia notes that any test approach must be usable by Tallyline's developers, or it will be ignored.

This shapes the design of Sofia's tests. Each failing test names the role, the endpoint and the intended decision, so a developer can see at once that, for example, support should not be able to issue refunds. Developers later reported finding the failures clear, which is the usability Johnson et al. found missing in static tools.

### Worked example

Sofia's search log: 412 records, 38 after title screening, 11 after full text. Only two study authorisation regression in web apps directly; none use role-matrix tests in a real team. Dr Lee accepts this as a defensible gap for a master's dissertation.

> **Synthetic case.** Kingsreach University, Tallyline, its staff and all data are synthetic.

### Errors and limits

Small literatures can reflect search limits; report the search fully so readers can judge.

### Exercises

- **EX001 — The problem.** What problem triggered the study? *Rubric:* 3 = access-control flaws recurring; invoice view; refunds two releases later; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Question parts.** Name the parts of Sofia's question. *Rubric:* 3 = intervention, outcome, alternative explanations; 2 = two; 1 = one; 0 = none.
- **EX003 — OWASP rank.** Where does broken access control rank in the OWASP Top 10:2021? *Rubric:* 3 = A01, first; 2 = one; 1 = vague; 0 = none.
- **EX004 — CWE names.** Give two CWE entries related to the case. *Rubric:* 3 = CWE-862, CWE-639; 2 = one; 1 = vague; 0 = none.
- **EX005 — Search log.** What does the search log record? *Rubric:* 3 = date, database, query, hits, exclusions with reasons; 2 = partial; 1 = vague; 0 = none.
- **EX006 — Grey literature.** How does Sofia use WSTG? *Rubric:* 3 = definitions not effectiveness evidence; 2 = partial; 1 = vague; 0 = none.
- **EX007 — Usability warning.** What did Johnson et al. (2013) find? *Rubric:* 3 = developers avoid tools with false positives, poor explanations; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Ask a question with an intervention, an outcome and alternatives, and search in a way others can repeat.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Application and software supply chain security: advanced seminar

### Learning outcomes

You will (1) critically discuss secure development frameworks; (2) compare verification standards across versions; (3) relate application flaws to supply-chain practices; (4) present a seminar argument.

### 2.1 Frameworks

NIST SP 800-218, the SSDF (Souppaya et al., 2022), groups practices into preparing the organisation, protecting software, producing well-secured software and responding to vulnerabilities. OWASP SAMM v2 (2020) measures maturity in governance, design, implementation, verification and operations. Sofia's intervention sits in SSDF PW.8 (test executable code) and SAMM's verification function.

Placing the intervention in both frameworks lets Tallyline report it in the language its auditors and customers already use. PW.8 asks for executable code to be tested, and the role-matrix tests do exactly that for authorisation; SAMM's verification function gives Tallyline a way to describe how far its testing practice has matured.

### 2.2 ASVS versions

ASVS 4.0.3 (2021) and 5.0.0 (2025) both require that access control is enforced on a trusted service layer and that users cannot access records by manipulating identifiers. Version 5.0.0 reorganised chapters and requirement numbering, so Sofia records both identifiers for each test.

Recording both identifiers keeps the tests traceable whichever version a customer or auditor uses. Sofia's seminar slide maps each Tallyline test to its 4.0.3 requirement, its 5.0.0 equivalent, an SSDF practice and a SAMM activity; Dr Lee suggested adding the CWE entry as well, so findings link to weakness data.

### 2.3 Threat modelling

Shostack (2014) describes threat modelling around four questions: what are we working on, what can go wrong, what are we going to do about it, and did we do a good job. Tallyline's role matrix is a product of the first two questions applied to authorisation.

The matrix answers "what are we working on" by listing roles and endpoints, and "what can go wrong" by stating, for each pair, what must be refused. The March invoice flaw and the later refunds flaw are both cases where the answer to the second question had never been written down.

### 2.4 Supply chain links

Access checks often live in shared libraries or frameworks. If a team upgrades an authorisation library and its defaults change, flaws can return. Sofia notes the SLSA v1.0 idea that build inputs should be known and traceable; knowing which library version ran in each release helps explain regressions.

For Tallyline, this idea has a direct example: the framework upgrade in release 8 added a default deny for unmapped routes. A change in a dependency's defaults can remove flaws as well as add them, so Sofia records which framework version ran in each release. Without that record, the fall in findings after release 8 could not be split between the tests and the upgrade.

### 2.5 Seminar argument

Sofia argues that tests encoding the intended access model are a verification practice that also documents design intent, linking SSDF PW.8, SAMM verification and ASVS requirements.

Her slide made the link concrete for each test: the test that a customer cannot read another business's invoice maps to an ASVS requirement on manipulated identifiers, to PW.8 and to SAMM verification. A test that documents intended behaviour also helps when roles change, because the matrix shows what the old decision was before anyone edits it.

### 2.6 Critique

A classmate argues that tests only check the cases someone wrote down; missing roles or endpoints stay untested. Sofia accepts this and plans to measure matrix completeness.

The pilot later proved the classmate right: the matrix initially missed the "export" endpoint, and a completeness check found three more unmapped routes, internal health checks. Sofia's answer was a check that lists all routes from the framework and flags any missing from the matrix, which turns the critique into a measured quantity.

### Worked example

Sofia's seminar slide maps each Tallyline authorisation test to an ASVS 4.0.3 requirement, its 5.0.0 equivalent, an SSDF practice and a SAMM activity. Dr Lee suggests adding the CWE entry for each test so findings link to weakness data.

> **Synthetic case.** Seminar content about Tallyline is synthetic.

### Errors and limits

Mapping to frameworks shows alignment, not effectiveness.

### Exercises

- **EX008 — SSDF groups.** Name the four SSDF practice groups. *Rubric:* 3 = prepare, protect, produce, respond; 2 = three; 1 = one; 0 = none.
- **EX009 — Intervention placement.** Where does the intervention sit in SSDF and SAMM? *Rubric:* 3 = PW.8; SAMM verification; 2 = partial; 1 = vague; 0 = none.
- **EX010 — Version care.** Why record both ASVS identifiers? *Rubric:* 3 = 5.0.0 renumbered chapters; 2 = partial; 1 = vague; 0 = none.
- **EX011 — Four questions.** State Shostack's four questions. *Rubric:* 3 = working on; go wrong; do about it; good job; 2 = three; 1 = one; 0 = none.
- **EX012 — Library link.** How can libraries cause regressions? *Rubric:* 3 = upgrade changes defaults; traceable inputs help; 2 = partial; 1 = vague; 0 = none.
- **EX013 — Classmate critique.** What was the critique and response? *Rubric:* 3 = tests check only listed cases; measure matrix completeness; 2 = partial; 1 = vague; 0 = none.
- **EX014 — Mapping addition.** What did Dr Lee add to the mapping? *Rubric:* 3 = CWE entry per test; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Frameworks give vocabulary and placement; critique reveals what tests cannot see.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) design a before-and-after study in a live development team; (2) handle ethics and confidentiality for security findings; (3) plan measurement of findings and exposure to change; (4) make the study reproducible without exposing the company.

### 3.1 Design

An interrupted time series: six releases before the authorisation tests were introduced and six after. The outcome is access-control findings per release from Tallyline's regular penetration tests and bug reports, normalised by lines of code changed.

Twelve releases give six on each side of the change, enough to see whether findings fall at the point the tests were introduced rather than drifting down throughout. Using Tallyline's regular penetration tests and bug reports means the outcome was collected the same way before and after, rather than by a new process that might find more or fewer flaws.

### 3.2 Why normalise

A quiet release with little change will naturally have fewer findings. Findings per thousand changed lines (KLOC) adjusts for this.

The after period in fact changed more code, 52 KLOC against 41, so normalising works against the tests rather than in their favour. Without it, a reader could fairly ask whether quieter releases explained the drop. Using lines changed rather than total code size matters too: Tallyline's codebase grows every release, but findings come mostly from new or modified code. A KLOC-changed denominator ties the rate to the work that could introduce a flaw.

### 3.3 Ethics

Developers are not being evaluated; findings are attributed to releases, not people. Tallyline's legal team approves the use of anonymised finding counts. No real vulnerability details leave the company; the dissertation uses synthetic examples.

The ethics committee also asked whether developers might feel blamed if findings rose. Sofia added a statement to the participant information sheet and agreed with the engineering manager that results would not be used in performance reviews. Attributing findings to releases makes that promise easy to keep, because no table has a column for people.

### 3.4 Confidentiality of flaws

Unfixed flaws are never described in the dissertation. Every finding counted is fixed before publication.

In Tallyline's case that is straightforward, because the study counts findings from past releases, all of which were fixed. The dissertation's examples, such as a customer reading another business's invoice, are synthetic versions written to show the kind of flaw without the real endpoint, parameters or customer. The same rule covers the pilot. The two mismatches the role-matrix tests found, a customer reading another business's invoice and support issuing refunds, were fixed within a day, before any write-up. If a finding were still open at submission, it would be counted in the tables but left out of the text until fixed.

### 3.5 Reproducibility

Sofia publishes her analysis scripts and a synthetic dataset with the same structure, so others can run the analysis without Tallyline's data.

The synthetic dataset mirrors Tallyline's fields: release number, access-control findings, lines changed, tester-days and notable events. An examiner can run every script on it and see each table produced, even though the figures differ from Tallyline's. After the defence, an examiner asked Sofia to share the dataset with a course on secure development, which she did under CC0.

### 3.6 Measurement plan

Two people classify each finding as access control or not, using the OWASP Top 10 A01 definition, with disagreements discussed and logged.

Using the A01 definition keeps the classification tied to a public standard rather than Sofia's judgement alone. The disagreement log matters for the analysis: if the two classifiers disagreed often about borderline findings, the before-and-after counts could shift depending on who classified them. In the main data they agreed on 46 of 48. Sofia logs each disagreement with both classifiers' reasons, so a reader can see which findings were borderline and check whether moving them would change the before-and-after counts.

### Data management

Finding counts are stored in a university-encrypted folder, separate from any company system, and deleted after the dissertation is examined. Sofia records each data item, where it came from and who approved its use.

### Pre-registration

The analysis is registered before the after period begins.

### Worked example

The ethics committee asks whether developers might feel blamed if findings rise. Sofia adds a statement to the participant information sheet and agrees with the engineering manager that results will not be used in performance reviews.

> **Synthetic case.** The design and approvals are synthetic.

### Errors and limits

A before-and-after design cannot rule out other changes happening at the same time; chapter 4 addresses this.

### Exercises

- **EX015 — Design type.** What design does Sofia use? *Rubric:* 3 = interrupted time series, 6 before 6 after; 2 = partial; 1 = vague; 0 = none.
- **EX016 — Normalisation.** Why use findings per KLOC? *Rubric:* 3 = adjusts for amount of change; 2 = partial; 1 = vague; 0 = none.
- **EX017 — Ethics safeguard.** How are developers protected? *Rubric:* 3 = findings attributed to releases; not used in reviews; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Unfixed flaws.** What rule applies to unfixed flaws? *Rubric:* 3 = never described; all fixed before publication; 2 = partial; 1 = vague; 0 = none.
- **EX019 — Reproducible.** How can others reproduce without company data? *Rubric:* 3 = scripts + synthetic dataset same structure; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Classification.** How are findings classified? *Rubric:* 3 = two people with A01 definition; disagreements logged; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Normalise outcomes, protect people and flaws, and share reproducible synthetic data.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Application and software supply chain security: competing explanations

### Learning outcomes

You will (1) identify alternative explanations for a security improvement; (2) design checks for each; (3) weigh evidence fairly; (4) state what remains uncertain.

### 4.1 The worry

If access-control findings fall after tests are added, other things might explain it: fewer pentest days, a new framework, a senior developer joining, or testers focusing elsewhere.

Each alternative predicts a different pattern. Fewer pentest days would lower all findings, not just access control. A new framework would lower findings mainly in the routes it changed. A senior developer would show up as a change in review practice. Tester focus elsewhere would appear in the pentest scopes. Listing them before the results lets each be checked against data.

### 4.2 Pentest effort

Sofia records tester-days per release. They were stable (four days each), so reduced effort does not explain a fall.

Stable effort rules out the simplest alternative. If tester-days had fallen from four to two after the tests were introduced, fewer findings would be expected whatever the tests did, and the comparison would need to be adjusted for effort. Recording tester-days per release is cheap and closes that question for all twelve releases. Effort also stays comparable across the two periods because the same pentest supplier ran every test; Sofia records the supplier with the tester-days so this is checkable.

### 4.3 Framework change

In release 8 Tallyline upgraded its web framework, which added a default deny for unmapped routes. This could reduce flaws by itself. Sofia separates findings in routes the upgrade affected from others.

Separating the routes gives a cleaner test. In routes the upgrade affected, the default deny and the tests could both explain a fall. In routes the upgrade did not affect, only the tests (and the other alternatives) could. Sofia found that findings still fell sharply in the unaffected routes, which supports a real effect of the tests, though smaller than the raw comparison suggests.

### 4.4 People

A senior developer joined at release 7. Sofia notes the date and asks reviewers whether review practice changed; it did, slightly.

Release 7 is one release before the tests and the framework upgrade, so a change in review practice would overlap with both. Sofia cannot separate its effect statistically with twelve releases. She records it as a possible contributor and lets the reviewers' account of a slight change stand as the evidence. Asking reviewers rather than inferring from the data is deliberate: twelve releases cannot separate a person's effect statistically, but reviewers can say what they did differently. Their answer, a slight change, is reported as it was given.

### 4.5 Tester focus

Pentest scopes are checked: authorisation was in scope for all twelve releases.

That check matters because a fall in access-control findings could simply mean the testers stopped looking for them. Since authorisation stayed in scope throughout, a release with no access-control findings means testers looked and found none, not that they did not look. The same four tester-days per release support this. Sofia checks the scope documents for all twelve releases rather than a sample, because a single release where authorisation was dropped from scope would produce a misleading zero. The scope check takes an afternoon and closes the question fully.

### 4.6 Weighing

Some of the improvement may come from the framework default and the new developer; the tests are one cause among several. Sofia plans to report this honestly rather than credit everything to tests.

Weighing the alternatives together leads to a ranked account rather than a single cause: the tests have the strongest support, because findings fell even in routes the framework change did not affect; the framework default explains part of the fall in the routes it did affect; and the senior developer may have contributed through slightly changed review practice.

### Unchecked explanations

Sofia could not measure developer awareness directly, so she lists it as an unchecked explanation. A short survey before and after might address it in future studies, and she notes it as a recommendation.

### Diagram of causes

Sofia draws a simple diagram linking tests, the framework change, the new developer and pentest effort to the outcome. The diagram shows which paths she can measure and which she cannot, and it helps readers see why she separated framework-affected routes in the analysis.

### Worked example

Separating findings, Sofia finds that in routes unaffected by the framework change, findings still fell sharply. This supports a real effect of the tests, though smaller than the raw comparison suggests.

> **Synthetic case.** Releases, staff and findings are synthetic.

### Errors and limits

Unmeasured explanations may remain; say which you could not check.

### Exercises

- **EX021 — Four alternatives.** List four alternative explanations. *Rubric:* 3 = pentest effort, framework, new developer, tester focus; 2 = three; 1 = one; 0 = none.
- **EX022 — Effort check.** How was pentest effort checked? *Rubric:* 3 = tester-days stable at four; 2 = partial; 1 = vague; 0 = none.
- **EX023 — Framework effect.** What did the framework upgrade add? *Rubric:* 3 = default deny for unmapped routes; 2 = partial; 1 = vague; 0 = none.
- **EX024 — Separation result.** What did separating routes show? *Rubric:* 3 = unaffected routes still fell; real but smaller effect; 2 = partial; 1 = vague; 0 = none.
- **EX025 — Scope check.** Was authorisation always in scope? *Rubric:* 3 = yes, all twelve releases; 2 = one; 1 = vague; 0 = none.
- **EX026 — Honest reporting.** How will Sofia report causes? *Rubric:* 3 = tests one cause among several; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Name rival explanations, check each, and report the share of credit honestly.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write a dissertation proposal; (2) pilot the role-matrix test approach on one feature; (3) measure matrix mismatches in a pilot; (4) refine the method before the full study.

### 5.1 Proposal

Background, question, design, ethics, alternative explanations, timeline and risks, in ten pages approved by Dr Lee.

Ten pages forces each part to be specific. The alternative-explanations part lists pentest effort, the framework change, the senior developer and tester focus, each with the data that will check it. The timeline fixes when the before and after periods begin. The risks part names the main threat to the design: a small number of findings. Dr Lee's approval also fixes the analysis before data collection, which is what later lets the examiners see that the framework separation was planned, not added after results arrived.

### 5.2 Role matrix

For each role (customer, support, finance) and each endpoint, the matrix states whether access is allowed. Tests call each endpoint as each role in a test environment and compare the result with the matrix. This follows the WSTG's authorisation testing guidance, applied to Tallyline's own system with permission.

Three roles keep Tallyline's matrix small enough to review by hand, and the six decisions in the lab are a small part of it. The matrix's value comes from being complete: a role or endpoint missing from it is never tested, which is why Sofia added the route completeness check after the pilot.

### Lab — matrix check

```python
"""Compare a synthetic app's actual access decisions with the intended role matrix."""
intended = {("customer", "GET /invoices/own"): True, ("customer", "GET /invoices/other"): False,
            ("customer", "POST /refunds"): False, ("support", "GET /invoices/other"): True,
            ("support", "POST /refunds"): False, ("finance", "POST /refunds"): True}
actual = {("customer", "GET /invoices/own"): True, ("customer", "GET /invoices/other"): True,
          ("customer", "POST /refunds"): False, ("support", "GET /invoices/other"): True,
          ("support", "POST /refunds"): True, ("finance", "POST /refunds"): True}
bad = [(k, intended[k], actual[k]) for k in intended if intended[k] != actual[k]]
for (role, ep), want, got in bad:
    print(f"MISMATCH {role:8} {ep:22} intended={want} actual={got}")
print(f"{len(bad)} of {len(intended)} decisions wrong")
```

Run with `python3 lab_authz.py`. Verified output:

```text
MISMATCH customer GET /invoices/other    intended=False actual=True
MISMATCH support  POST /refunds          intended=False actual=True
2 of 6 decisions wrong
```

### 5.3 Lab result

Two of six decisions are wrong: a customer can read another business's invoice (intended no), and support can issue refunds (intended no). Both match the kinds of flaw that had recurred.

The two wrong decisions mirror the history that started the study: the March flaw let a customer view another business's invoice, and a similar flaw reappeared in refunds. A test suite that encodes the intended matrix would have failed on both before release, which is the mechanism Sofia's study puts to the test.

### 5.4 Pilot lessons

The matrix initially missed the "export" endpoint; Sofia adds a check that lists all routes from the framework and flags any not in the matrix, addressing the completeness critique from chapter 2.

The completeness check later found three more unmapped routes, all internal health checks, which were added as "deny for all user roles". The two pilot mismatches were fixed within a day. Each addition to the matrix is recorded, which is why the examiners later asked for route and role counts over time.

### 5.5 Developer feedback

Developers found failing tests clear because each names the role, endpoint and intended decision, avoiding the usability problems Johnson et al. (2013) reported for static tools.

The clarity matters because tests that developers distrust get disabled. A failing test saying "support, POST /refunds, intended deny, got allow" tells the developer exactly what to fix and where, without anyone needing to interpret a scanner's output. That is part of why developers later said the tests caught problems before review. Because each test is a single call compared against one matrix cell, a developer can fix a failure without knowing how the rest of the suite works.

### Timeline

The full study runs for six months after the pilot, covering six releases. A risk register lists what could delay it, such as release schedule changes or a pentest supplier change, with fallback plans.

### Approval

Dr Lee and Tallyline's engineering manager both sign the proposal, which records what each party has agreed to provide.

### Test environment

Tests run against a seeded test database with synthetic businesses only.

### Worked example

The two pilot mismatches are fixed within a day. The completeness check finds three more unmapped routes, all internal health checks, which are added as "deny for all user roles".

> **Synthetic case.** Pilot data are synthetic.

### Errors and limits

A test environment may differ from production configuration.

### Exercises

- **EX027 — Proposal sections.** List five proposal sections. *Rubric:* 3 = background, question, design, ethics, alternatives, timeline, risks (five); 2 = three; 1 = one; 0 = none.
- **EX028 — Matrix meaning.** What does the role matrix state? *Rubric:* 3 = per role and endpoint, allowed or not; 2 = partial; 1 = vague; 0 = none.
- **EX029 — Lab mismatches.** What mismatches did the lab find? *Rubric:* 3 = customer reads other invoice; support issues refunds; 2 = one; 1 = vague; 0 = none.
- **EX030 — Completeness fix.** How was matrix completeness addressed? *Rubric:* 3 = list framework routes; flag unmapped; 2 = partial; 1 = vague; 0 = none.
- **EX031 — Clear failures.** Why did developers find failures clear? *Rubric:* 3 = named role, endpoint, intended decision; 2 = partial; 1 = vague; 0 = none.
- **EX032 — Health checks.** How were the unmapped health checks handled? *Rubric:* 3 = deny for all user roles; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Pilot the intervention, find its blind spots and fix them before the main study.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) collect release-level findings and change size; (2) compute rates and rate ratios; (3) interpret small-sample results carefully; (4) combine numbers with team observations.

### 6.1 Collection

For each of twelve releases Sofia records access-control findings, lines changed, pentest days and notable events. Two classifiers agree on 46 of 48 findings' categories; the two disagreements are resolved by discussion.

Notable events, such as the framework upgrade in release 8 and the senior developer joining at release 7, are recorded beside the counts so that the time series can be read against them. The classifiers' high agreement means the access-control counts do not depend on who classified the findings. Recording these items for every release, not just the ones where something happened, is what makes the before and after periods comparable.

### Lab — findings per release

```python
"""Access-control findings per release before and after authorisation tests were added (synthetic)."""
before = {"r1": 3, "r2": 2, "r3": 4, "r4": 3, "r5": 2, "r6": 3}
after = {"r7": 1, "r8": 0, "r9": 1, "r10": 0, "r11": 1, "r12": 0}
for name, d in (("before", before), ("after", after)):
    print(f"{name:6} releases={len(d)} findings={sum(d.values())} mean per release={sum(d.values()) / len(d):.2f}")
```

Run with `python3 lab_regress.py`. Verified output:

```text
before releases=6 findings=17 mean per release=2.83
after  releases=6 findings=3 mean per release=0.50
```

### 6.2 Lab result

Before tests: 17 findings over six releases, 2.83 per release. After: 3 findings, 0.50 per release.

The raw counts are the starting point, not the result. Seventeen findings before and three after is a large fall, but it does not yet account for change size, the framework upgrade or the other alternatives, which is why the next steps normalise by KLOC and separate the routes affected by the upgrade. Expressed per release, that is close to three findings before against one every two releases after. The framework-separated comparison and the KLOC rate then test how much of that fall the tests can claim.

### Lab — rate per KLOC

```python
"""Findings per 1,000 changed lines, and the rate ratio after/before (synthetic)."""
before_find, before_kloc = 17, 41.0
after_find, after_kloc = 3, 52.0
rb, ra = before_find / before_kloc, after_find / after_kloc
print(f"before {rb:.3f} per KLOC, after {ra:.3f} per KLOC, rate ratio {ra / rb:.2f}")
```

Run with `python3 lab_rate.py`. Verified output:

```text
before 0.415 per KLOC, after 0.058 per KLOC, rate ratio 0.14
```

### 6.3 Rate result

Normalised by change size, the rate falls from 0.415 to 0.058 findings per KLOC, a rate ratio of 0.14. The after period actually changed more code (52 versus 41 KLOC), so the fall is not due to quieter releases.

A rate ratio of 0.14 means the after-period rate is about one seventh of the before-period rate. Because the after period changed more code, the normalised fall is if anything larger than the raw fall, which removes "quieter releases" as an explanation. Sofia states it next to the framework-separated result, so the ratio is never read as the tests' effect alone.

### 6.4 Interpreting

Twelve releases and twenty findings are a small sample; Sofia reports the ratio with its uncertainty and avoids saying "86% reduction caused by tests".

The uncertainty matters because twenty findings split over twelve releases leave many releases with zero or one finding. A single release with three more findings after the tests would change the ratio noticeably. Sofia's wording, "was followed by" and "is consistent with", keeps the claim within what such small counts can support. Sofia's table gives the ratio with an interval rather than a single figure.

### 6.5 Team observations

In interviews, developers say failing authorisation tests often caught problems before review. One says the matrix forced product managers to decide roles explicitly, which reduced arguments.

The interviews do not measure an effect; they explain a mechanism. Catching problems before review suggests the tests work at the point developers write code, and the product managers' explicit role decisions suggest the matrix also changes how requirements are written. Sofia reports both as developers' accounts, alongside the counts. Sofia reports them as developers' accounts of how the tests worked, not as evidence that findings fell; that evidence comes from the counts.

### Uncertainty

With so few findings, Sofia also reports a simple range: if the after period had three more findings by chance, the ratio would still be below 0.3, showing a clear fall.

### Release notes

Release notes help match findings to features: the refund flaw in release 5 links to a new refund screen added that release. Such links let Sofia check that findings are attributed to the right release and that no findings belong to old code that was simply tested for the first time, which would inflate the before period.

### Worked example

Combining the framework-separated analysis (chapter 4) and rates, Sofia's finding is: access-control findings fell substantially after the tests, part of the fall is explained by the framework default, and developers credit the tests with catching problems earlier.

> **Synthetic case.** All counts are synthetic.

### Errors and limits

Pentest findings depend on tester skill; changes of tester could affect counts.

### Exercises

- **EX033 — Classifier agreement.** How many findings did classifiers agree on? *Rubric:* 3 = 46 of 48; 2 = one; 1 = vague; 0 = none.
- **EX034 — Per-release figures.** Give findings per release before and after. *Rubric:* 3 = 2.83 and 0.50; 2 = one; 1 = vague; 0 = none.
- **EX035 — Rate ratio.** What is the rate ratio? *Rubric:* 3 = 0.14 (0.415 to 0.058); 2 = partial; 1 = vague; 0 = none.
- **EX036 — Change size.** Why does change size strengthen the result? *Rubric:* 3 = after period changed more code; 2 = partial; 1 = vague; 0 = none.
- **EX037 — Caution.** What does Sofia avoid claiming? *Rubric:* 3 = 86% reduction caused by tests; 2 = partial; 1 = vague; 0 = none.
- **EX038 — Product effect.** What side effect did a developer describe? *Rubric:* 3 = matrix forced explicit role decisions; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Normalise, interpret small samples with care and let practitioners explain the numbers.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure a dissertation for a security audience; (2) write limitations that inform rather than apologise; (3) present findings without exposing a company; (4) connect results to practice standards.

### 7.1 Structure

Introduction, literature, method, results, competing explanations, discussion, limitations, conclusion. Each chapter answers one question.

Giving competing explanations their own chapter, before the discussion, makes the reader meet the framework change, the senior developer and pentest effort before any interpretation of the 0.14 ratio. Each chapter answers one question, so the examiners can find, for example, how tester focus was checked without reading the whole results chapter. The structure also mirrors the proposal Dr Lee approved, so an examiner can compare what was planned with what was done chapter by chapter. Any change between the two is listed in the method chapter with its reason.

### 7.2 Limitations

One company, one application, twelve releases; a framework change during the study; pentest skill variation; tests in a test environment. Each limitation says what it means for the claim and how future work could address it.

Dr Lee called this the most useful part for practitioners, because it tells them when the approach may not work. Apps with hundreds of dynamic roles, for example, may not be manageable with a hand-written matrix; the dissertation says so, and proposes generating the matrix from the role definitions as future work.

### 7.3 Confidentiality

Tallyline is named only with permission, figures are rounded, and examples are synthetic versions of real flaws.

Rounding stops a reader from linking a figure to a specific Tallyline release or customer. The synthetic examples keep the shape of the real flaws, such as reading another business's invoice by changing a number, without the real endpoint names or parameters. Tallyline's legal team reviewed the final text against these rules before submission, the same team that approved use of the anonymised finding counts at the start. Their review is recorded with the ethics approval.

### 7.4 Linking to standards

The discussion recommends role-matrix tests as a way to meet ASVS authorisation requirements continuously and to evidence SSDF PW.8 and SAMM verification.

Continuously means on every build, not once a year: a role-matrix test that fails the build gives Tallyline evidence for PW.8 every time it runs. The discussion also notes the limit: the tests check only what the matrix lists, so ASVS requirements for complete coverage depend on the route completeness check as well. For that reason it recommends running the route check in the same build as the tests, so an unmapped route fails the build just as a wrong decision does.

### 7.5 Plain summary

A one-page summary for Tallyline's engineering team avoids jargon.

It gives the main result as "access-control findings fell sharply after the tests; part of the fall came from the framework upgrade", states that results were never used to assess individuals, and asks developers to keep the matrix and route check up to date. Each sentence matches a claim in the dissertation. The summary also explains the route completeness check in one sentence, because it is the step most likely to be dropped once the study ends and the person who wrote it moves on. A matrix that stops matching the routes would quietly stop testing new endpoints.

### 7.6 Writing style

Claims are tied to evidence with hedges where needed: "was followed by", "is consistent with".

When a sentence in the draft said the tests "reduced" findings, Sofia changed it to "was followed by a reduction", because the design shows sequence and association rather than proof of cause. The framework change makes the hedge necessary, not merely cautious. The hedges are not decoration: each one corresponds to a limitation stated in the limitations chapter, such as the framework change or the twelve-release sample, so a reader can see why the claim is worded as it is.

### Figures

Each figure has a clear caption stating what it shows and its data source.

### Abstract

The abstract states question, method, main result with its uncertainty, the main limitation and the practical implication in under 250 words. Sofia rewrites it five times, each time asking a colleague outside security whether they understand the result. A clear abstract decides whether practitioners read on.

### Recommendations

The final chapter lists recommendations by audience. For developers: write an authorisation test for every new endpoint as part of the definition of done. For product managers: decide and record roles before building features. For security teams: use the matrix as the basis for penetration test scoping, so testers focus on gaps rather than re-checking covered cases.

### Worked example

Dr Lee reads the limitations section and comments that it is the most useful part for practitioners, because it tells them when the approach may not work, such as apps with hundreds of dynamic roles.

> **Synthetic case.** Text and feedback are synthetic.

### Errors and limits

Over-hedging can hide useful findings; balance caution with clarity.

### Exercises

- **EX039 — Chapter list.** List the dissertation chapters. *Rubric:* 3 = intro, literature, method, results, alternatives, discussion, limitations, conclusion; 2 = six; 1 = three; 0 = none.
- **EX040 — Limitation form.** What must each limitation state? *Rubric:* 3 = meaning for claim; future work; 2 = partial; 1 = vague; 0 = none.
- **EX041 — Confidentiality.** How is Tallyline protected? *Rubric:* 3 = named with permission; rounded; synthetic examples; 2 = partial; 1 = vague; 0 = none.
- **EX042 — Standards link.** How do results link to ASVS and SSDF? *Rubric:* 3 = continuous ASVS authorisation; evidence PW.8; 2 = partial; 1 = vague; 0 = none.
- **EX043 — Hedging words.** Give a hedged phrasing. *Rubric:* 3 = "was followed by", "consistent with"; 2 = partial; 1 = vague; 0 = none.
- **EX044 — Dynamic roles.** When might the approach not work? *Rubric:* 3 = apps with hundreds of dynamic roles; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Write limitations that guide practitioners and claims that match evidence.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) obtain independent review of findings; (2) defend methods and claims orally; (3) respond to examiner questions with evidence; (4) plan dissemination.

### 8.1 Independent review

A security engineer from another company reviews the method and synthetic dataset, re-running the scripts. She confirms the numbers and suggests reporting the routes count over time.

Re-running the scripts on the synthetic dataset tests the method and code, not Tallyline's figures. The reviewer's suggestion, reporting the routes count over time, addresses a reader's obvious question: whether the matrix kept up with the app. Sofia adds it, and the examiners later ask for the same information. Her re-run used only the published scripts and the CC0 dataset, which is the same route any later reader would take.

### 8.2 Defense

Twenty minutes plus questions, with two examiners.

Sofia's talk follows the dissertation's order: question, design, competing explanations, results with uncertainty, limitations. She keeps the 0.14 ratio on the same slide as the framework-separated result, so the examiners never see one without the other. Sofia rehearses the talk with Dr Lee using the questions she expects most: the credibility of the 0.14 ratio with twenty findings, the framework change in release 8, and whether the matrix could miss tests. The route completeness check is ready on a backup slide, and the defence is held after Tallyline's legal team has approved the final text.

### 8.3 Questions

"Is the 0.14 ratio credible with 20 findings?" Sofia answers that it is imprecise, but direction and size are consistent with other evidence. "Would mutation of the matrix catch missing tests?" She explains the route completeness check.

Both answers rest on earlier work: the imprecision is acknowledged in the results chapter, and the route completeness check came from the pilot, where the matrix had missed the export endpoint. The examiners' questions test whether those choices were deliberate, and the dissertation shows that they were.

### 8.4 Examiner advice

Report how many routes and roles exist over time, so readers see the matrix scale.

The advice matches the independent reviewer's suggestion. Showing how many routes and roles the matrix covers at each release lets readers judge whether the approach would scale to their own apps, and whether the fall in findings happened while the matrix was growing or stable. Sofia adds a table to the results chapter with the number of routes and roles at each of the twelve releases, drawn from the framework's route list that the completeness check already produces. No new data collection is needed, because the check has been running since the pilot.

### 8.5 Dissemination

A conference short paper, a Tallyline engineering blog post with synthetic examples, and an OWASP community talk.

Each output reaches a different audience: researchers through the short paper, Tallyline's developers and customers through the blog, and practitioners through the OWASP talk. All three use the synthetic examples and the CC0 dataset, so none needs Tallyline's internal data. The blog post and the talk carry the same hedged wording as the dissertation: findings fell after the tests, and part of the fall is explained by the framework default. Using the CC0 synthetic dataset in all three means readers can reproduce the examples without any Tallyline data.

### 8.6 Next steps

Tallyline extends the matrix approach to its mobile API.

The mobile API serves the same customer, support and finance roles, so the matrix can be extended rather than rebuilt. The route completeness check will need a mobile equivalent, because the API's endpoints are listed differently from the web framework's routes. Mobile clients often call endpoints the web app never uses, so the first step is listing every mobile endpoint and adding it to the matrix with an intended decision for each role. The same three roles mean existing decisions carry over where endpoints are shared. Sofia's scripts can then compare mobile findings before and after, as the dissertation did for the web app.

### Lessons

Sofia notes that early ethics and data agreements saved time later.

### Preparation

Sofia rehearses twice with classmates, who ask the hardest questions they can think of. She prepares a backup slide for each limitation and for the framework-separated analysis, which examiners did ask about. Preparation lets her answer calmly and briefly, leaving more time for the discussion.

### After the defense

Corrections are made within two weeks, and the final dissertation is deposited in the university repository with its synthetic dataset and scripts. Sofia also writes a short note for the OWASP community describing the role-matrix approach and its limits, so other teams can try it and report back. She plans to apply for a doctoral position to test the approach across several companies.

### Worked example

The examiners award a distinction. One asks Sofia to share her synthetic dataset with a course on secure development, which she does under CC0.

> **Synthetic case.** The defense and reviews are synthetic.

### Errors and limits

A single defense cannot test generalisation; replication by others is needed.

### Exercises

- **EX045 — Reviewer role.** What did the independent reviewer do? *Rubric:* 3 = re-ran scripts; confirmed; suggested routes count; 2 = partial; 1 = vague; 0 = none.
- **EX046 — Ratio answer.** How did Sofia defend the 0.14 ratio? *Rubric:* 3 = imprecise but consistent with other evidence; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Missing tests.** How are missing tests caught? *Rubric:* 3 = route completeness check; 2 = partial; 1 = vague; 0 = none.
- **EX048 — Dissemination.** List three dissemination outputs. *Rubric:* 3 = short paper, blog, OWASP talk; 2 = two; 1 = one; 0 = none.
- **EX049 — Next step.** What did Tallyline do next? *Rubric:* 3 = extend to mobile API; 2 = partial; 1 = vague; 0 = none.
- **EX050 — Dataset sharing.** How was the dataset shared? *Rubric:* 3 = CC0 for a course; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Independent review and an honest defense turn a dissertation into shared knowledge.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Sofia Almeida, Dr Marcus Lee, Tallyline, Kingsreach University and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Broken access control kept recurring: an invoice view flaw in March, then a similar refund flaw two releases later.

**EX002.** An intervention (role-matrix authorisation tests), an outcome (reintroduction of broken access control) and alternative explanations.

**EX003.** First, as A01.

**EX004.** CWE-862 missing authorisation and CWE-639 authorisation bypass through a user-controlled key.

**EX005.** Date, database, query, number of hits and exclusions with reasons.

**EX006.** For definitions and practice, not as evidence of effectiveness.

**EX007.** Developers avoid static analysis tools with many false positives and poor explanations.

**EX008.** Prepare the organisation, protect the software, produce well-secured software and respond to vulnerabilities.

**EX009.** SSDF PW.8 (test executable code) and SAMM's verification function.

**EX010.** Because ASVS 5.0.0 reorganised and renumbered requirements.

**EX011.** What are we working on, what can go wrong, what are we going to do about it, did we do a good job?

**EX012.** Upgrading an authorisation library can change defaults; knowing versions per release helps explain regressions.

**EX013.** Tests only check written cases; Sofia plans to measure matrix completeness.

**EX014.** The CWE entry for each test.

**EX015.** An interrupted time series with six releases before and six after.

**EX016.** To adjust for how much code changed in each release.

**EX017.** Findings are attributed to releases, not people, and not used in performance reviews.

**EX018.** They are never described and every counted finding is fixed before publication.

**EX019.** Using published scripts and a synthetic dataset with the same structure.

**EX020.** By two people using the A01 definition, with disagreements discussed and logged.

**EX021.** Less pentest effort, a framework upgrade, a new senior developer and tester focus.

**EX022.** Tester-days per release were stable at four.

**EX023.** A default deny for unmapped routes.

**EX024.** Findings fell in unaffected routes too, supporting a real but smaller test effect.

**EX025.** Yes, in all twelve releases.

**EX026.** As one cause among several, not the sole reason.

**EX027.** Background, question, design, ethics and timeline.

**EX028.** For each role and endpoint, whether access is allowed.

**EX029.** A customer reading another's invoice and support issuing refunds.

**EX030.** By listing all framework routes and flagging any not in the matrix.

**EX031.** Each failure named the role, endpoint and intended decision.

**EX032.** Added as deny for all user roles.

**EX033.** 46 of 48.

**EX034.** 2.83 before and 0.50 after.

**EX035.** 0.14, from 0.415 to 0.058 findings per KLOC.

**EX036.** The after period changed more code, so fewer findings are not from quieter releases.

**EX037.** That tests caused an 86% reduction.

**EX038.** The matrix forced product managers to decide roles explicitly.

**EX039.** Introduction, literature, method, results, competing explanations, discussion, limitations and conclusion.

**EX040.** What it means for the claim and how future work could address it.

**EX041.** Named only with permission, with rounded figures and synthetic examples.

**EX042.** Tests meet ASVS authorisation requirements continuously and evidence SSDF PW.8.

**EX043.** "Was followed by" or "is consistent with".

**EX044.** In apps with hundreds of dynamic roles.

**EX045.** Re-ran the scripts, confirmed the numbers and suggested reporting routes over time.

**EX046.** It is imprecise but consistent in direction and size with other evidence.

**EX047.** By the route completeness check.

**EX048.** A conference short paper, an engineering blog post and an OWASP talk.

**EX049.** Extended the matrix approach to its mobile API.

**EX050.** Under CC0 for a secure development course.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Decan, A., Mens, T., & Constantinou, E. (2018). On the impact of security vulnerabilities in the npm package dependency network. *Proceedings of the 15th International Conference on Mining Software Repositories (MSR '18)*, 181–191. <https://doi.org/10.1145/3196398.3196401>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Johnson, B., Song, Y., Murphy-Hill, E., & Bowdidge, R. (2013). Why don't software developers use static analysis tools to find bugs? *35th International Conference on Software Engineering (ICSE)*, 672–681. <https://doi.org/10.1109/ICSE.2013.6606613>
- Kula, R. G., German, D. M., Ouni, A., Ishio, T., & Inoue, K. (2018). Do developers update their library dependencies? *Empirical Software Engineering*, 23(1), 384–417. <https://doi.org/10.1007/s10664-017-9521-5>
- Ladisa, P., Plate, H., Martinez, M., & Barais, O. (2023). SoK: Taxonomy of attacks on open-source software supply chains. *IEEE Symposium on Security and Privacy*, 1509–1526. <https://doi.org/10.1109/SP46215.2023.10179304>
- Lamb, C., & Zacchiroli, S. (2022). Reproducible builds: Increasing the integrity of software supply chains. *IEEE Software*, 39(2), 62–70. <https://doi.org/10.1109/MS.2021.3073045>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- MITRE. (2024). *CWE Top 25 Most Dangerous Software Weaknesses*. <https://cwe.mitre.org/top25/>
- Newman, Z., Meyers, J. S., & Torres-Arias, S. (2022). Sigstore: Software signing for everybody. *ACM SIGSAC Conference on Computer and Communications Security (CCS '22)*, 2353–2367. <https://doi.org/10.1145/3548606.3560596>
- NTIA. (2021). *The minimum elements for a software bill of materials (SBOM)*. U.S. Department of Commerce. <https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom>
- Ohm, M., Plate, H., Sykosch, A., & Meier, M. (2020). Backstabber's knife collection: A review of open source software supply chain attacks. *DIMVA 2020*, LNCS 12223, 23–43. <https://doi.org/10.1007/978-3-030-52683-2_2>
- OpenSSF. (2023). *SLSA: Supply-chain Levels for Software Artifacts, version 1.0*. <https://slsa.dev/spec/v1.0/>
- OWASP Foundation. (2020). *Software Assurance Maturity Model (SAMM) v2.0*. <https://owaspsamm.org/model/>
- OWASP Foundation. (2020). *Web Security Testing Guide v4.2*. <https://owasp.org/www-project-web-security-testing-guide/>
- OWASP Foundation. (2021). *Application Security Verification Standard 4.0.3*. <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP Foundation. (2021). *OWASP Top 10:2021*. <https://owasp.org/Top10/>
- OWASP Foundation. (2025). *Application Security Verification Standard 5.0.0*. <https://owasp.org/www-project-application-security-verification-standard/>
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley. ISBN 978-1-118-80999-0.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure Software Development Framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
- Thompson, K. (1984). Reflections on trusting trust. *Communications of the ACM*, 27(8), 761–763. <https://doi.org/10.1145/358198.358210>
- Torres-Arias, S., Afzali, H., Kuppusamy, T. K., Curtmola, R., & Cappos, J. (2019). in-toto: Providing farm-to-table guarantees for bits and bytes. *28th USENIX Security Symposium*, 1393–1410. <https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias>
- Wermke, D., Wöhler, N., Klemmer, J. H., Fourné, M., Acar, Y., & Fahl, S. (2022). Committed to trust: A qualitative study on security & trust in open source software projects. *IEEE Symposium on Security and Privacy*, 1880–1896. <https://doi.org/10.1109/SP46214.2022.9833686>
- Zimmermann, M., Staicu, C.-A., Tenny, C., & Pradel, M. (2019). Small world with high risks: A study of security threats in the npm ecosystem. *28th USENIX Security Symposium*, 995–1010. <https://www.usenix.org/conference/usenixsecurity19/presentation/zimmerman>
