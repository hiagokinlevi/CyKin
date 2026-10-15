# Incident Response and Cyber Resilience: Doctoral Research Methods and Thesis Practice

- Language: English (`en`); doctoral research track, two years; approximately 1,600 hours of planned study (course 200 of 207 in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **published**. Chapters 1–8 of 8 have authored teaching text, exercises EX001–EX050 and matching worked results. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: advanced researchers who already hold research experience and a defensible question about incident response or cyber resilience. Entry knowledge: the practitioner foundations of the [rapid](../../../../rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md), [professional](../../../../professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md) and [technical](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md) books, or equivalent experience, plus introductory statistics and qualitative-methods literacy.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights and are not relicensed here.
- Educational boundary: this track is an independent educational blueprint. It is not an accredited doctoral program, grants no degree, and grants no authority to collect, access or study real incident records. Every organization, person, record, dataset, benchmark and result named in a worked example is **synthetic** unless a sentence explicitly cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

Read the eight chapters in order. They follow the arc of one doctoral project: Chapter 1 sets the integrity and method standards that every later step must meet; Chapter 2 finds a genuine open question; Chapter 3 turns it into a falsifiable contribution; Chapter 4 replicates the baseline and pilots the procedure; Chapter 5 runs the main study; Chapter 6 tests whether the result travels; Chapter 7 submits the claims to adversarial critique; and Chapter 8 assembles the thesis and its reproducibility archive.

Each chapter contains teaching sections, definitions, a worked example, a practical activity, a list of common errors and limits, numbered exercises and a synthesis. Write your own answer to every exercise before opening the [worked results](#worked-results). The exercises at this level rarely have one correct answer; the worked results show a defensible answer and the rubric shows what a reviewer would reward or reject.

Keep four labels in every research note you write while studying this book: **observation** (what a named source recorded), **inference** (what you conclude from one or more observations, and under which assumptions), **claim** (the statement you intend to defend to others, with its scope), and **decision** (what you or someone else chose to do because of it). Chapter 1 explains why the distinction is the foundation of incident-response research rather than a stylistic preference.

### The synthetic research corpus used in this book

The book follows one invented doctoral project, the **Handoff Study**, which asks whether a structured handoff artifact improves the quality of incident decisions made by a receiving responder when telemetry is incomplete. Its fictional settings are:

| Synthetic element | Role in the book | Boundary |
|---|---|---|
| **Northbridge Municipal Services CSIRT (NMS-CSIRT)** | Primary field context for the proposed study of sensitive incident records (Chapters 1, 3, 5). | Invented organization; no real municipality, staff or records. |
| **Kestrel Freight Logistics SOC (KFL-SOC)** | Second context with different staffing and telemetry quality (Chapter 6). | Invented organization. |
| **OpenTriage-S** | A synthetic "public benchmark" of triage cases whose published baseline cannot initially be reproduced (Chapters 1, 4). | Invented benchmark; it is not a real dataset and should not be searched for. |
| **Harbor Library**, **Cedar Training Network**, **Lumen Library Reservations** | Synthetic cases from the [rapid](../../../../rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md), [professional](../../../../professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md) and [technical](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md) books, reused here only as *scenario seeds* for simulated study conditions. | Teaching fixtures, not empirical data. Nothing measured on them is evidence about real organizations. |

All numbers produced in this book's labs come from synthetic fixtures printed in the text. They demonstrate a method; they are not findings.

### Source policy

Every factual statement about a standard, a regulation or a published study links to the source the author consulted. When a widely taught concept is used without a specific source (for example, the four-part validity vocabulary in Chapter 1), the text says it is a standard methods concept and does not attach an invented reference. Dated sources are labeled as dated. A source supports the general claim beside it, never the synthetic case details.

## Contents

1. [Advanced research integrity and methods](#ch-01) — epistemology of incident evidence, integrity, reproducibility under constraint, ethics, measurement validity and the defensible protocol.
2. [Research frontier in incident response systems](#ch-02) — systematic scoping, competing theories and a falsifiable gap.
3. [Original response-science contribution proposal](#ch-03) — mechanism, hypothesis, baseline, risk and predeclared failure conditions.
4. [Replication of baselines and pilot protocol](#ch-04) — reproducing a benchmark, dataset shift, power and a bounded pilot.
5. [Main study of incident decision quality](#ch-05) — assignment, blinded review, error analysis and uncertainty.
6. [Independent validation across contexts](#ch-06) — external validity, heterogeneity and boundary conditions.
7. [Peer critique and revision of claims](#ch-07) — adversarial review, negative results and narrowing a contribution.
8. [Thesis synthesis and reproducibility archive](#ch-08) — argument, open artifacts, data governance and limitations.

The [worked results](#worked-results) contain EX001–EX050. A [glossary](#glossary) and [references](#references) close the book.

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Classify any statement in an incident record or a research paper as an observation, an inference or a claim, and state what would be needed to promote it to the next level.
2. Explain why incident evidence is unusual as research data: it is produced by systems not designed for research, altered by the response itself, read with hindsight, and usually encumbered by privacy, legal and contractual restrictions.
3. Apply integrity safeguards (pre-specification, deviation logs, separation of exploratory and confirmatory work, conflict-of-interest disclosure) to an incident-response study.
4. Design a tiered reproducibility plan that releases as much as can lawfully and safely be released, and say honestly what cannot be checked.
5. Identify the stakeholders, authorizations and harms involved in studying real incidents, using the Menlo Report principles as a working structure.
6. Choose and defend measures of response quality, recognizing threats to construct validity, censoring in time-based metrics, base-rate effects and rater disagreement.
7. Write a research protocol that a hostile but fair reviewer could audit, including the conditions under which the study would be stopped or its claim abandoned.

The chapter is the methodological contract for the rest of the book. Chapter 2 will use its claim vocabulary to read the literature; Chapter 3 will use its protocol template; Chapters 4–6 will use its measurement and validity tools; Chapters 7–8 will use its integrity and reproducibility standards to judge the finished work.

### 1.1 Incident response as an object of research

Practitioners learn incident response as a set of activities. The current NIST guidance, [SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (April 2025, superseding Rev. 2 of 2012), frames those activities as part of cybersecurity risk management organized by the six CSF 2.0 Functions — Govern, Identify, Protect, Detect, Respond and Recover — and places continuous improvement in the Identify Function's Improvement category (ID.IM). Its [full text](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) notes that preparation activities are broader risk-management work that *supports* response, while Detect, Respond and Recover form the response itself, and that lessons learned should often be shared as soon as they are identified rather than after recovery ends. Recovery planning and testing are treated in [SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) (December 2016), which emphasizes prioritizing resources, realistic test scenarios and learning from past events, including other organizations' events.

A researcher needs a different stance. The question is not "what should a responder do next?" but "what do we have warrant to believe about how response works, and how confident should we be?" That shift has five consequences.

**First, the unit of analysis must be chosen, not assumed.** A study can be about an *incident* (a bounded case), a *decision* within an incident (for example, the choice to isolate a host), an *actor* (a responder, a team, a vendor), an *artifact* (a playbook, a handoff note, a detection rule), an *organization* or a *population of organizations*. Many weak claims in the field come from measuring at one level and concluding at another: counting tickets (an artifact level) and concluding about team capability (an organizational level), or interviewing three analysts and concluding about "SOCs."

**Second, incidents are rarely repeatable.** A chemist can rerun a reaction; an incident happens once, in a particular organization, against a particular adversary, with particular staff on shift. Researchers approximate repetition in three ways: by studying *many* incidents (with all the heterogeneity that brings), by *simulating* incidents in exercises or laboratories (with the realism gap that brings), or by studying *components* that do repeat, such as triage decisions on a stream of alerts. Each approach buys some control at the price of some relevance; none is free.

**Third, the response changes the evidence.** Containment, reimaging, password resets and log rotation alter or destroy the records a later analyst would want. The decision of what to collect is itself a response decision. A research dataset built from incident records is therefore not a passive sample of what happened; it is a sample of what the responders *chose and were able to preserve*.

**Fourth, outcomes are adversarial and partly unobservable.** An undetected intrusion produces no incident record. A "successful" containment might reflect a capable team or an adversary who had already achieved its goal and left. Ground truth is often unavailable, delayed or contested.

**Fifth, the work is sociotechnical.** Response quality depends on tools, telemetry, procedures, authority, fatigue, communication and organizational incentives. Fieldwork in security operations centers illustrates this: an [anthropological study of a corporate SOC over six months](https://www.usenix.org/conference/soups2015/proceedings/presentation/sundaramurthy) modeled analyst burnout as a human-capital problem arising from cycles among human, technical and managerial factors, and an [interview study of 18 SOC analysts and managers](https://doi.org/10.1145/3319535.3354239) reported disagreements between managers and analysts that could undermine effectiveness. A survey of SOC literature in [IEEE Access (2020)](https://doi.org/10.1109/ACCESS.2020.3045514) concluded that research tends to address people and technology while neglecting the processes, especially non-technical ones, that connect them. A study that measures only the tool will miss most of what determines response quality.

These consequences do not make rigorous research impossible. They make it necessary to be explicit about what each study can and cannot show.

### 1.2 The epistemology of incident evidence

#### 1.2.1 What counts as evidence

SP 800-61 Rev. 3 adopts a broad definition: under subcategory RS.AN-07, it notes that formal chain-of-custody handling may not be performed for every incident, but that collected incident data is still evidence, "grounds for belief or disbelief; data on which to base proof or to establish truth or falsehood," a definition it attributes to NIST SP 800-160 Vol. 1 ([SP 800-61r3 PDF, Table 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf)). The same table asks organizations to preserve the integrity and provenance of incident data (RS.AN-07) and of the records of actions taken during an investigation (RS.AN-06), and warns that incident response records can contain sensitive information about exploited vulnerabilities, breaches and users.

For research, the useful part of this definition is that evidence is defined by its *role in belief*, not by its form. A log line, a ticket comment, a screenshot, an interview transcript and a responder's memory can all be evidence. What differs is how much they can support and how their support can fail.

Every piece of incident evidence has at least these properties, and a research dataset should record them explicitly:

| Property | Question | Typical failure |
|---|---|---|
| Producer | Which system or person generated the record, under which configuration? | A parser or collector, not the original system, created the field. |
| Event time vs. record time vs. collection time | When did the thing happen, when was it written, when was it collected? | Treating ingestion time as event time; unknown clock offset. |
| Scope of observation | What could this producer have seen at all? | Reading absence in a source that never covered the asset. |
| Custody and integrity | Who held it, how was it copied, can the bytes be verified? | Derived extracts with no link back to originals. |
| Selection | Why does this record exist in the dataset and not others? | Only escalated incidents were retained; low-severity ones expired. |
| Interpretation layer | Is this a raw record, a normalized field, an analyst label, or a narrative? | A label ("malicious") is stored in the same column as raw values. |

The technical book in this series develops the operational side of these properties ([producer clocks, collection receipts and derived views](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md#ch-05)). At doctoral level the point is that *each property is also a validity threat* to any claim built on the data.

#### 1.2.2 Observation, inference and claim

The most important habit in incident-response research is to keep three kinds of statement apart.

- An **observation** is what a named source recorded, stated with its producer and time: "The VPN concentrator log exported at 14:02 UTC contains a successful authentication for account `u-417` from address 192.0.2.10 at 03:11 UTC."
- An **inference** is a conclusion drawn from one or more observations under stated assumptions: "Assuming the concentrator clock was within one minute of UTC and the account is not shared, the account holder or someone with their credentials authenticated at about 03:11."
- A **claim** is the statement a researcher or responder will defend to others, with an explicit scope: "In this incident, initial access most likely used valid credentials (moderate confidence; the alternative of a session-token replay is not excluded because token logs were unavailable)."

A research claim sits one level higher again: "Across the 41 incidents in our sample, receiving responders who were given a structured handoff note reached a correct containment decision more often than those who were not." Its warrant depends on every observation and inference beneath it, on the sampling of incidents and on the measurement of "correct."

Two disciplined practices follow. First, **every claim should be traceable** downward to the inferences and observations that support it, so that a reviewer can find exactly where an assumption entered. Second, **every inference should name the observation that would defeat it.** "The account was not shared" is a defeater-bearing assumption; if an identity-management record shows two people using `u-417`, the inference collapses. Writing the defeater before looking for it is a small act of pre-commitment that protects against confirmation bias.

The **evidence ladder** below is a teaching device used throughout this book; it is not a published standard.

| Level | Example statement | What would promote it | What would demote it |
|---|---|---|---|
| L0 Report | "The help desk says users cannot log in." | A system record showing failed authentications. | The reporter misidentified the system. |
| L1 Observation | "IdP log shows 312 failures for 40 accounts between 09:00 and 09:10 UTC." | Integrity check, known coverage, clock check. | Log is a sampled or derived view. |
| L2 Inference | "A credential-stuffing attempt is plausible." | Source distribution, password-spray pattern, threat context. | A misconfigured client explains the failures. |
| L3 Case claim | "This incident was a credential-stuffing attempt with no confirmed compromise." | Exhaustive check of successes against expected behavior. | One unexplained success. |
| L4 Research claim | "MFA prompts reduced successful stuffing in our sample." | Comparison group, adequate sample, valid outcome measure. | Selection: MFA was deployed only where risk was lower. |

*In plain terms:* Claims climb the ladder only when stronger evidence arrives, and they fall when that evidence is contradicted; the table tells you what would move each claim up or down.

#### 1.2.3 Absence of evidence

Incident analysts constantly reason from absence: "no outbound traffic to the suspicious domain," "no further logins." Absence is evidence only when three conditions hold: the source **covered** the relevant asset and period, the source **would have recorded** the event if it had occurred (it was configured, running and not saturated), and the analyst **searched correctly** (right fields, right time zone, right identifiers). A research protocol that uses "no recurrence within 30 days" as an outcome inherits all three conditions. If telemetry coverage changed after the incident — as it often does when an organization adds monitoring during recovery — then recurrence detection is not comparable before and after.

#### 1.2.4 Hindsight and outcome knowledge

Everyone who studies an incident after the fact knows how it ended. In experiments reported by [Fischhoff (1975)](https://doi.org/10.1037/0096-1523.1.3.288), receiving outcome knowledge increased the judged likelihood of the reported outcome and changed which details seemed relevant, while judges were largely unaware of that influence and overestimated what they — and others — would have known without it. In the safety-science tradition, Richard Cook's short treatise [*How Complex Systems Fail*](https://how.complexsystems.fail/) states that hindsight biases post-accident assessments of human performance, and argues that post-accident attribution to a single "root cause" is fundamentally wrong because overt failure requires multiple contributing faults.

That second point sits in visible tension with SP 800-61 Rev. 3, which recommends analyzing an incident "to find the underlying or systemic root causes" (RS.AN-03, R3, in the [PDF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf)). A researcher should not resolve the tension by picking a side; it should be operationalized. Note that NIST's wording is plural and includes "systemic." A study that codes "root cause" as a single categorical variable is making a modeling choice that Cook's argument would reject; a study that codes *contributing factors* as a set, with the evidence for each, is compatible with both sources. State the choice and justify it.

Hindsight affects research design in concrete ways:

- **Judging decision quality by outcome** (outcome bias). A containment decision that turned out well may have been poorly reasoned given what was known at the time; one that turned out badly may have been the best available choice. Chapter 5 separates *decision quality given information available at decision time* from *outcome*.
- **Retrospective interviews.** Responders interviewed after an incident reconstruct their reasoning with knowledge they did not have. Interview protocols should anchor questions to time-stamped artifacts ("At 10:40 the ticket says X; what else were you looking at then?").
- **Coding of reports.** Coders who read the end of a post-incident report before its timeline will code early decisions differently. Blind coders to outcomes where possible, or present information in time order with later sections withheld.

#### 1.2.5 The response as an intervention on its own evidence

Because responders shape what is recorded, incident data have *reactivity*. Three patterns matter for research. **Instrumentation drift**: monitoring added after an incident increases detection of later events, making it look as if incidents rose. **Selective preservation**: well-resourced teams preserve more, so their incidents look more "complete" and better understood. **Narrative convergence**: post-incident reports are written to explain; contradictory early observations are often omitted from the final narrative. A researcher using reports as data should, where permitted, also obtain the contemporaneous working record (tickets, chat logs, action logs — the RS.AN-06 records) and treat the final report as one interpretation among others.

### 1.3 Research integrity applied to incident-response research

Research integrity is usually summarized as honesty, transparency and accountability in proposing, performing and reporting research. In incident response, the general principles meet specific temptations.

#### 1.3.1 Questionable research practices and why IR is vulnerable

The broader scientific literature has documented how flexible analysis inflates false findings. [Ioannidis (2005)](https://doi.org/10.1371/journal.pmed.0020124) argued, using a simple model, that the probability a published positive finding is true falls with small samples, small effects, many tested relationships, flexible designs and strong interests. [Simmons, Nelson and Simonsohn (2011)](https://doi.org/10.1177/0956797611417632) showed through simulations and demonstrations that undisclosed flexibility in data collection and analysis can make false-positive results very likely. [Gelman and Loken (2014)](https://doi.org/10.1511/2014.111.460) described how this can happen even without deliberate "fishing": when analysis choices depend on the data, the effective number of comparisons is larger than the one analysis reported (the "garden of forking paths"). [Kerr (1998)](https://doi.org/10.1207/s15327957pspr0203_4) named the practice of presenting a post hoc hypothesis as if it were a priori: *HARKing*, hypothesizing after the results are known.

Incident-response research has every risk factor these authors identify:

- **Small samples.** A single organization may experience a handful of major incidents per year.
- **Many possible outcome measures.** Time to detect, time to contain, time to recover, scope, cost, recurrence, analyst confidence, stakeholder satisfaction, each with several definitions.
- **Flexible case definitions.** What counts as one incident versus two? When does an incident start?
- **Strong interests.** Vendors evaluate their own products; teams evaluate their own processes; researchers depend on partner organizations who would prefer flattering results.
- **Post hoc narratives.** Incidents arrive as stories, and stories invite explanation after the fact.

Security has its own documented versions. [Arp et al. (USENIX Security 2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) identified ten pitfalls in machine-learning-based security research — sampling bias, label inaccuracy, data snooping, spurious correlations, biased parameter selection, inappropriate baselines, inappropriate performance measures, base-rate fallacy, lab-only evaluation and inappropriate threat models — and reported them to be widespread in a study of 30 papers from top-tier security venues. [Pendlebury et al. (USENIX Security 2019)](https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury) argued that published malware-classification results were inflated by spatial bias (unrepresentative train/test distributions) and temporal bias (time splits that would be impossible in deployment). [Sommer and Paxson (2010)](https://doi.org/10.1109/SP.2010.25) explained why machine-learning approaches to network intrusion detection struggle outside the "closed world" of their training assumptions. Although these papers focus on detection, their pitfalls transfer directly to research on triage tools, automated response and decision support.

#### 1.3.2 Pre-specification and preregistration

[Nosek et al. (2018)](https://doi.org/10.1073/pnas.1708274114) describe preregistration as specifying the research plan in advance, before seeing the outcome data, so that confirmatory (hypothesis-testing) analyses can be distinguished from exploratory (hypothesis-generating) ones. The [Registered Reports](https://www.cos.io/initiatives/registered-reports) format goes further: peer review of the question and method happens before data collection, and a protocol that passes is provisionally accepted regardless of results, which removes the incentive to produce a positive story.

Three adaptations make pre-specification workable in incident-response research.

1. **Pre-specify against data you have not yet seen, not against time.** Field studies of incidents often begin with partial access to historical records. A preregistration is honest only if it is written before the researcher has examined the outcome variables in the data being used for confirmation. If you have already explored part of a dataset, preregister against a held-out part, or against incidents that have not yet occurred (prospective collection), and say so.
2. **Pre-specify qualitative work differently.** An interview or ethnographic study cannot specify its findings in advance, but it can specify its sampling logic, interview guide, coding procedure, the point at which coding categories will be frozen, and how disconfirming cases will be sought. "Exploratory" is a legitimate label; it is not a license to present exploratory patterns as confirmed.
3. **Keep a deviation log.** Real incident studies deviate: a partner withdraws, a log source turns out to be unusable, an incident type is reclassified. Every deviation should be recorded with date, reason, who decided, and whether it was made before or after seeing outcome data. A protocol with a transparent deviation log is more credible than one that claims to have gone perfectly.

#### 1.3.3 Originality, attribution and provenance

At doctoral level, originality means that the contribution is new *and* that its relation to prior work is accurately represented. Incident-response research presents specific attribution problems:

- **Practitioner knowledge without a citable source.** Much of the field's knowledge lives in talks, blogs, vendor reports and internal wikis. When a practice is common but undocumented, say so ("widely reported by practitioners; we found no peer-reviewed evaluation") rather than either claiming it as your idea or attaching a citation that does not actually support it.
- **Vendor and industry reports.** Reports such as large annual breach reports compiled from vendors' and partners' caseloads can be valuable, but their samples reflect who engaged those organizations and what they chose to publish. Cite them for what they are — descriptive accounts of a particular caseload — and do not use their percentages as population estimates.
- **Data provenance.** Every dataset used in a thesis should have a provenance record: who created it, from which sources, under which permission, with which transformations, and which version was analyzed. "We used a public dataset" is insufficient if the dataset has several versions or was relabeled.
- **AI-assisted writing and analysis.** Where language models or automated tools generate text, code, labels or summaries, record what was generated, by which tool and version, and how it was checked. A generated citation must be verified against the actual source before it is used — fabricated references are an integrity failure regardless of how they were produced.

#### 1.3.4 Conflicts of interest and partner pressure

Incident-response research often depends on partners: an organization that provides records, a vendor that provides a tool, a funder interested in a result. A conflict-of-interest statement should name each relationship and, more importantly, the protocol should *structurally* limit the conflict: pre-specified outcomes, independent coders blind to condition, publication rights agreed before data access, and an explicit statement of what the partner may review (accuracy and confidentiality, not conclusions). If a partner can veto publication of unfavorable results, the study cannot support a claim of effectiveness, and the thesis should say so.

### 1.4 Reproducibility and open science under constraint

#### 1.4.1 Definitions

This book follows the definitions adopted by the U.S. National Academies of Sciences, Engineering, and Medicine in [*Reproducibility and Replicability in Science* (2019)](https://www.nationalacademies.org/read/25303/chapter/3): **reproducibility** is obtaining consistent results using the same input data, computational steps, methods, code and conditions of analysis (also called computational reproducibility); **replicability** is obtaining consistent results across studies aimed at the same scientific question, each of which has obtained its own data. The report notes that even a rigorous, transparent study may fail to replicate, because new data differ.

The distinction matters in incident response because the two are blocked by different obstacles. Reproducibility is blocked mainly by *access*: the original incident records usually cannot be shared. Replicability is blocked mainly by *heterogeneity*: no two organizations, incidents or adversaries are alike, so a second study is never a pure repetition. Chapter 4 addresses reproduction of a baseline; Chapter 6 addresses replication across contexts.

#### 1.4.2 Open-science expectations in security venues

Open science is becoming a formal expectation in security research. The [USENIX Security 2026 call for papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) requires every paper to include a separate "Ethical Considerations" appendix and a separate "Open Science" appendix listing where the artifacts needed to evaluate the contribution are located; artifacts must be available at submission or their unavailability must be explained. The [FAIR principles](https://doi.org/10.1038/sdata.2016.18) (Wilkinson et al., 2016) describe data stewardship goals — findable, accessible, interoperable and reusable — that apply to metadata even when the data themselves are restricted. [Munafò et al. (2017)](https://doi.org/10.1038/s41562-016-0021) collect measures across methods, reporting, reproducibility, evaluation and incentives intended to improve the reliability of research.

#### 1.4.3 The constraint taxonomy

Incident data are almost always restricted. A doctoral researcher should identify *which* constraint applies to *which* artifact, because each constraint permits different mitigations.

| Constraint | Typical source | What it forbids | What it may still permit |
|---|---|---|---|
| Personal data | Account names, IP addresses, email content, HR actions in incident records. | Publishing records that identify or single out individuals. | Aggregates, de-identified extracts after risk assessment, synthetic data, access in a controlled enclave. |
| Legal privilege and litigation holds | Investigations run under counsel; regulatory proceedings. | Disclosure of privileged material; sometimes any discussion. | Methods description; post-proceeding release; data held by a neutral party. |
| Contract and vendor confidentiality | Customer contracts, MSSP agreements, tool licenses. | Naming the client or tool, sharing telemetry or rules. | Anonymized organization descriptors; tool-agnostic descriptions; vendor review for confidentiality only. |
| Operational security | Live vulnerabilities, detection logic, adversary infrastructure. | Details that would help an adversary evade or attack. | Delayed release, generalized descriptions, coordinated disclosure. |
| Information-sharing labels | Material received under [FIRST Traffic Light Protocol 2.0](https://www.first.org/tlp/) labels (TLP:RED, TLP:AMBER, TLP:AMBER+STRICT, TLP:GREEN, TLP:CLEAR). | Sharing beyond the label's boundary. | Use within the boundary; seeking the source's permission to relabel. FIRST notes TLP is *not* a formal classification scheme and was not designed to handle licensing terms. |

*In plain terms:* Each constraint removes some actions from the researcher's menu but rarely all of them; the last column shows what work remains possible inside the limit.

#### 1.4.4 De-identification is not a magic word

Removing names does not make incident data anonymous. Incident records are high-dimensional and sparse: a combination of timestamps, rare software versions, internal hostnames and job roles can single out an organization or a person. [Narayanan and Shmatikov (2008)](https://doi.org/10.1109/SP.2008.33) demonstrated robust de-identification attacks on large sparse datasets using small amounts of auxiliary information. [Sweeney (2002)](https://doi.org/10.1142/S0218488502001648) formalized *k*-anonymity as a model in which each released record is indistinguishable from at least *k*−1 others on identifying attributes. [Dwork, McSherry, Nissim and Smith (2006)](https://doi.org/10.1007/11681878_14) introduced calibrating noise to the sensitivity of a query, the foundation of differential privacy, which bounds what a released statistic can reveal about any individual record. NIST's [SP 800-188](https://csrc.nist.gov/pubs/sp/800/188/final) (September 2023) describes de-identification techniques *and governance* for government datasets, with the goal of limiting disclosure risks to individuals and establishments while allowing meaningful statistical analysis.

Two lessons follow for incident-response researchers. First, **organizations are data subjects too.** An "anonymized" incident narrative that mentions a regional utility, a ransomware family and a date range may identify the organization to anyone in the sector. SP 800-188's explicit inclusion of establishments is a useful reminder. Second, **de-identification is a governance process, not a transformation.** Document the threat model (who might try to re-identify, with what auxiliary data), the technique, the residual risk and who approved release.

#### 1.4.5 A tiered artifact plan

Because "release everything" is rarely possible and "release nothing" is rarely necessary, plan artifact release in tiers:

| Tier | Artifact | Reproducibility value | Typical constraint |
|---|---|---|---|
| T0 | Protocol, preregistration, deviation log, codebook, instruments. | Lets others audit and replicate the design. | Usually releasable. |
| T1 | Analysis code and environment specification, run on a **synthetic dataset with the same schema**. | Lets others verify the computation pipeline and catch bugs. | Usually releasable; synthetic data must not leak real records. |
| T2 | Aggregate results and summary statistics, possibly with formal privacy protection. | Lets others check reported numbers and do meta-analysis. | Small cells may need suppression. |
| T3 | De-identified record-level data, under a data-use agreement. | Allows reanalysis by vetted researchers. | Requires risk assessment, legal review, partner approval. |
| T4 | Original data in a controlled environment (enclave) where external reviewers run approved code. | Closest to full reproduction. | Requires infrastructure and a custodian willing to host it. |
| T5 | Full public release. | Maximum. | Rare for real incident data. |

A strong thesis aims for T0–T2 at minimum and states, in its Open Science section, why higher tiers were not possible and what a reviewer can and cannot check. Synthetic data deserve their own caution: they validate the *pipeline*, not the *finding*. A model trained or evaluated only on synthetic incidents has demonstrated nothing about real incidents unless the synthetic generator itself has been validated against real distributions — and even then only for the properties checked.

### 1.5 Ethics and authorization for studying real incidents

#### 1.5.1 Why incident research needs its own ethical analysis

Biomedical and behavioral research ethics grew around the 1979 Belmont Report's principles of respect for persons, beneficence and justice. [*The Menlo Report*](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) (August 2012; now marked by DHS as archived content) adapted those principles for information and communication technology research and added a fourth, **respect for law and public interest**. It proposes operationalizing them through stakeholder identification and informed consent; balancing risks and benefits; fairness and equity; and compliance, transparency and accountability, supported by ethical review boards and internal self-evaluation such as an Ethical Impact Assessment. The report argues that ICT research raises new challenges because of ubiquitously connected environments overlaid with varied and often discordant legal regimes. Although archived, its principles remain a clear structure for analysis; check current institutional and legal requirements separately.

Incident research raises problems that a generic human-subjects form does not anticipate:

- **The people in the data did not volunteer.** Employees whose accounts appear in incident records, customers whose data were exposed and third parties whose systems were used as infrastructure are all affected by research on those records.
- **Responders are workers.** Interviewing or observing responders creates risks of performance evaluation, blame and employment consequences, especially after a damaging incident. Consent obtained through a manager may not be free.
- **Organizations can be harmed.** Publication can reveal security weaknesses, attract regulators or litigants, or damage reputation, even when no individual is identified.
- **Adversaries are stakeholders of a peculiar kind.** Research may reveal detection gaps or response patterns useful to attackers. The ethical concern is not the adversary's interest but the downstream harm to defenders and the public.
- **The research can interfere with response.** Collecting extra data, interviewing during an active incident or delaying containment to observe would be an intervention with real costs.

#### 1.5.2 Applying the four principles

| Menlo principle | Incident-research question | Example safeguard |
|---|---|---|
| Respect for persons | Who is represented in the data, and can they consent or be protected? | Responder consent obtained by the researcher, not a supervisor; data subjects protected by minimization and de-identification when consent is impracticable. |
| Beneficence | What harms (privacy, employment, security, reputational, legal) could result, and are they proportionate to the expected knowledge? | Ethical Impact Assessment; stop rules; delayed or generalized publication of exploitable details. |
| Justice | Who bears risks and who benefits? | Avoid studying only under-resourced organizations because they are easier to access, while publishing results that benefit well-resourced vendors. |
| Respect for law and public interest | Is the study lawful in every relevant jurisdiction and transparent to those accountable for it? | Written data-use agreement; legal review of cross-border transfer; transparent methods and limitations. |

*In plain terms:* The Menlo principles become concrete only when each one is turned into a question about the specific incident data and a safeguard that answers it.

#### 1.5.3 Layers of authorization

Permission to study incident data comes in layers, and each must be obtained separately. A responder's operational access to records is **not** research authorization.

1. **Legal basis.** Does the jurisdiction permit processing these records for research? Data-protection law, sector rules, employment law and contractual terms may all apply. In the United States, federally supported human-subjects research falls under the Common Rule; other jurisdictions have their own regimes. This book does not provide legal advice; the protocol should record which legal review occurred and its conclusion.
2. **Data controller or owner permission.** The organization that holds the records must authorize the specific use, scope and duration, normally in a data-use agreement.
3. **Ethics review.** An independent research ethics board, where one exists, should review the protocol. If the researcher has no institutional board, the protocol should still include an Ethical Impact Assessment and an external reviewer, and the thesis should state the absence of formal review.
4. **Participant consent.** For interviews, surveys and observation, obtain informed consent from each participant, including the right to withdraw and clear statements about what will be published.
5. **Operational coordination.** Agree with the incident lead how research activity will be paused or abandoned if it conflicts with an active response. The response always takes priority.

#### 1.5.4 Specific hazards and safeguards

**Incidental discoveries.** Researchers analyzing incident data may find a still-open vulnerability, an unreported compromise or evidence of wrongdoing. The protocol should state in advance to whom such findings are reported and how quickly, and that the researcher will not investigate further outside scope.

**Dual use and release timing.** A study showing that a class of detection rule fails under a specific condition is valuable to defenders and attackers alike. Consider coordinated disclosure to affected vendors, delayed release of technical specifics and publication of defensive guidance alongside findings.

**Responder welfare.** Fieldwork in SOCs has documented burnout and morale cycles ([Sundaramurthy et al., SOUPS 2015](https://www.usenix.org/conference/soups2015/proceedings/presentation/sundaramurthy)). Asking exhausted responders to complete research instruments during or soon after a major incident adds burden. Offer timing control, keep instruments short and never make participation a condition of work.

**Blame.** Post-incident studies can become instruments for assigning fault. State in the consent material that individual-level findings will not be reported to management, and design analysis at the team or process level unless participants explicitly agree otherwise.

**Stop rules.** A protocol should list conditions that pause or end the study: an active incident requiring the data custodian's full attention, discovery of a legal hold, a participant complaint, evidence of re-identification risk exceeding the approved threshold, or a request by the data owner to withdraw.

### 1.6 Measurement validity for response quality

#### 1.6.1 Constructs, operationalizations and the four validities

Most incident-response research ultimately wants to say something about *quality*: of a decision, a response, a team, a tool or a plan. Quality is a **construct**, an abstract property that cannot be observed directly. Researchers **operationalize** it through measures: time intervals, correctness against a reference answer, expert ratings, scope of impact, recurrence, cost. The quality of a study depends on how well the measures capture the construct.

Methods textbooks commonly organize threats into four families. This book uses that standard vocabulary without attaching it to a single source:

- **Construct validity**: do the measures represent the intended construct? (Does time-to-contain measure response quality, or only speed?)
- **Internal validity**: does the observed relationship reflect the proposed cause rather than a confounder? (Did the new playbook improve outcomes, or did it arrive at the same time as additional staff?)
- **External validity**: does the result hold for other settings, people, incidents and times? (Does a result from a university SOC hold in a hospital?)
- **Statistical conclusion validity**: are inferences about the size and uncertainty of an effect justified by the data and analysis? (Twelve incidents cannot establish a small effect.)

#### 1.6.2 The trouble with time metrics

Time-based measures — mean time to detect, to respond, to contain, to recover — are attractive because they are numeric and appear objective. They carry at least five threats.

1. **Definition ambiguity.** "Detect" can mean the first alert, the first human acknowledgement, or the moment an analyst concluded an incident was real. "Contain" can mean the first containment action or the point at which no further adversary activity was observed. Two organizations reporting "mean time to contain" may be measuring different intervals.
2. **Unknown start times.** Intrusion start is often inferred retrospectively and revised as investigation proceeds. Time-to-detect therefore depends on how hard the team looked for the beginning.
3. **Censoring.** At the time a dataset is closed, some incidents are not yet contained. Excluding them biases averages downward, because the excluded incidents are, by definition, the slow ones. Section 1.10's lab demonstrates this.
4. **Goal displacement.** When a time metric becomes a performance target, teams can improve it by closing tickets early, splitting incidents or reclassifying them. The measure then tracks behavior around the target rather than the underlying quality.
5. **Speed versus correctness.** A fast containment that disrupts a critical service, or that alerts an adversary before scope is known, may be worse than a slower one. Time measures should be paired with correctness and harm measures.

#### 1.6.3 Correctness and the ground-truth problem

Correctness requires a reference answer. In real incidents the reference is often unavailable; in simulations it is available because the designer wrote it, but then the study measures performance on the designer's scenario. Three strategies help.

- **Expert panel reference.** Multiple independent experts, blind to condition, judge what a good decision would have been *given the information available at decision time*. Their agreement must be measured.
- **Designed scenarios with known ground truth.** Synthetic or exercise scenarios in which the true state is known. The realism gap must be acknowledged, and SP 800-84's guidance on exercise design ([CSRC page](https://csrc.nist.gov/pubs/sp/800/84/final), September 2006) should be treated as a dated starting point for exercise structure, not a current evaluation standard.
- **Multi-criteria rubrics.** Score separate dimensions — scope accuracy, appropriateness of containment, preservation of evidence, communication, harm avoided — rather than a single overall grade.

Labels in real operational data are especially fragile. In a [qualitative study of SOC practitioners](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi), Alahmadi, Axon and Martinovic reported that most alarms practitioners considered false positives were attributed to *benign triggers* — true alarms explained by legitimate behavior in the environment — and argued that vendors and researchers need to distinguish types of false positive to evaluate tools properly. A study that treats analyst dispositions ("false positive") as ground truth is therefore measuring a mixture of detection error and environmental context. Arp et al.'s "label inaccuracy" pitfall names the same risk.

#### 1.6.4 Rater agreement

When human judges score decisions or code reports, their agreement is part of measurement validity. [Cohen's kappa (1960)](https://doi.org/10.1177/001316446002000104) corrects observed agreement for agreement expected by chance:

κ = (pₒ − pₑ) / (1 − pₑ)

where pₒ is observed proportion of agreement and pₑ is the agreement expected if the raters' category frequencies were independent. [Landis and Koch (1977)](https://doi.org/10.2307/2529310) proposed verbal benchmarks for kappa values that are widely quoted; treat any such benchmarks as conventions, not thresholds of truth. Low agreement means the construct is not being measured consistently: fix the rubric, train raters and re-measure before analyzing outcomes. Report agreement on the actual study data, not only on training items.

#### 1.6.5 Base rates

Many incident-response tools are classifiers: they flag alerts, prioritize cases or recommend actions. The value of a flag to a responder depends on the **positive predictive value** (the proportion of flagged items that are truly positive), which depends heavily on the base rate. With 99% sensitivity and a 1% false-positive rate, a flag is right about 92% of the time when 10% of items are truly malicious, but only about 9% of the time when 0.1% are — the computation is shown in Section 1.10. Arp et al. list ignoring this effect as the *base-rate fallacy*. Any research claim about the operational usefulness of a triage tool must state the base rate in the evaluation data and in the intended deployment.

### 1.7 Common failure modes in incident-response research claims

The table below catalogs failure modes a doctoral reviewer should look for. Most have counterparts in the general methods literature; the examples are specific to incident response.

| Failure mode | How it appears in IR research | Defensive practice |
|---|---|---|
| Survivorship and visibility bias | Studying only detected, reported or publicly disclosed incidents and generalizing to all incidents. | State the sampling frame; discuss what kinds of incident cannot appear in it. |
| Caseload bias | Treating a vendor's or responder firm's caseload as representative of all organizations. | Describe the caseload; avoid population percentages. |
| Outcome bias | Rating decisions by how incidents ended. | Rate decisions on information available at decision time; blind raters to outcome. |
| Hindsight in coding | Coders read the full report before coding early events. | Time-ordered presentation; outcome-blind coding. |
| Instrumentation drift | Monitoring changes over the study period, altering detection rates. | Record telemetry changes; compare like-for-like coverage. |
| Temporal leakage | Training or tuning on incidents that occurred after test incidents ([Pendlebury et al., 2019](https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury)). | Time-respecting splits. |
| Label inaccuracy | Analyst dispositions used as ground truth ([Alahmadi et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi)). | Audit labels; distinguish benign triggers from errors. |
| Base-rate neglect | Reporting accuracy on balanced test sets. | Report PPV at realistic prevalence. |
| Single-site generalization | One organization's result presented as general. | Name boundary conditions; seek replication (Chapter 6). |
| Exercise-to-reality leap | Tabletop performance equated with real incident performance. | Treat exercise results as evidence about exercise performance unless linked to field outcomes. |
| Lessons-learned counting | Number of improvement actions recorded treated as improvement achieved. | Measure whether actions were implemented and whether later outcomes changed. |
| Self-report as performance | Survey confidence treated as capability. | Pair self-report with observed performance. |
| Root-cause monism | One "root cause" coded per incident. | Code contributing factors with evidence (§1.2.4). |
| Undisclosed flexibility | Many outcomes or case definitions tried; best reported. | Pre-specify; report all outcomes; keep deviation log. |
| Conflicted evaluation | Tool vendor or team evaluates itself without structural safeguards. | Independent raters; pre-agreed publication rights. |

*In plain terms:* Most of these failures make results look better than they are; the right-hand column is the habit that prevents each one, and a protocol should show where each habit is applied.

### 1.8 Worked example: a proposed study using sensitive incident records and a public benchmark

*All organizations, records and numbers in this example are synthetic.*

A doctoral candidate, working with the fictional **Northbridge Municipal Services CSIRT (NMS-CSIRT)**, proposes the following study:

> "We will show that our triage-assistant model improves incident response by training it on five years of NMS-CSIRT incident tickets and testing it on the public OpenTriage-S benchmark, where it achieves higher accuracy than the published baseline."

A reviewer applying this chapter would decompose it.

**Step 1 — Identify the claim and its scope.** "Improves incident response" is a construct-level claim about real response. The proposed evidence is accuracy on a benchmark. The claim exceeds the evidence by at least two levels: from benchmark accuracy to triage decision quality, and from triage decision quality to response outcomes. A defensible restatement: "On OpenTriage-S, the model's top-1 triage category matches the benchmark label more often than the published baseline does, under a time-respecting split; we do not test effects on real response decisions."

**Step 2 — Examine the data.** NMS-CSIRT tickets contain employee names, citizen data in attachments, internal hostnames and descriptions of unremediated weaknesses. Ticket dispositions were entered by analysts under time pressure. Some ticket categories changed definition in year three when the CSIRT adopted a new taxonomy. OpenTriage-S is a public benchmark with labels created by its authors.

Threats identified:

- *Label inaccuracy* in tickets (analyst dispositions; category redefinition).
- *Dataset shift* between NMS-CSIRT and OpenTriage-S (different organization, taxonomy and alert sources); the model is trained on one distribution and tested on another, which is legitimate only if the claim is about transfer.
- *Baseline reproduction*: the candidate has not rerun the published baseline. If the benchmark's evaluation script or split differs from the one used in the paper, the comparison is invalid. Chapter 4 develops this.
- *Base rate*: OpenTriage-S is balanced across categories; NMS-CSIRT's real distribution is highly skewed.

**Step 3 — Ethics and authorization.** The candidate's employment at NMS-CSIRT gives operational access, not research authorization. Required: data-owner approval through a data-use agreement; legal review of using citizen data for model training; ethics review; minimization (remove attachments, replace names with stable pseudonyms, generalize hostnames); a re-identification assessment considering that a municipal CSIRT is small and its incidents may have been reported locally; and an agreement on how trained model weights may be released, since models can memorize training records.

**Step 4 — Reproducibility plan.**

| Tier | Plan |
|---|---|
| T0 | Preregister hypotheses, splits, metrics and baseline procedure before training on the confirmation split. |
| T1 | Release training and evaluation code; provide a synthetic NMS-like ticket set with the same schema. |
| T2 | Release confusion matrices and per-category metrics on NMS data, suppressing cells below an agreed threshold. |
| T3 | No record-level release of NMS data. Model weights not released unless a memorization test passes an agreed threshold. |
| OpenTriage-S | Full reproduction: release exact benchmark version, split, seeds and evaluation script. |

**Step 5 — Revised research question.** "Does a triage-assistant model trained on one organization's tickets transfer to a different organization's benchmark well enough to exceed a reproduced baseline, and how much does performance change under a time-respecting split and at the deployment base rate?" This is narrower, testable and honest about its limits — and it leaves the bigger question (effect on real response decisions) for a later study design such as the one in Chapter 5.

### 1.9 Writing a defensible research protocol

A protocol is a public commitment that allows others to audit what was planned against what was done. For an incident-response study, the following structure covers what reviewers, ethics boards and data owners will ask.

| Section | Required content | Common weakness |
|---|---|---|
| 1. Title, version, date, registration ID | Protocol version and change history. | No version control; silent revisions. |
| 2. Question and claim | The research question, the specific claim to be tested, and its scope (unit of analysis, population, setting). | Claim broader than design. |
| 3. Background and gap | What is known, with verified citations; what is unknown. | Citations that do not support the stated gap. |
| 4. Hypotheses and predictions | Predictions stated so that a specified result would count against them. | Hypotheses that every outcome supports. |
| 5. Design | Observational, quasi-experimental, experimental, qualitative or mixed; comparison conditions; assignment. | No comparison condition. |
| 6. Setting and sampling | Sites, inclusion and exclusion criteria, sampling frame, expected sample size and its justification. | Convenience sample without discussion. |
| 7. Data sources and provenance | Each source with producer, time semantics, coverage, custody and transformations. | Mixed raw and derived data. |
| 8. Measures | Constructs, operational definitions, instruments, rater training and agreement targets. | Time metrics without definitions or censoring plan. |
| 9. Analysis plan | Primary and secondary analyses, handling of missing and censored data, multiple comparisons, sensitivity analyses. | Analysis decided after seeing data. |
| 10. Validity threats | Construct, internal, external and statistical-conclusion threats and mitigations. | Generic list unrelated to design. |
| 11. Ethics and authorization | Legal basis, data-owner approval, ethics review, consent, Ethical Impact Assessment, incidental-finding procedure. | "Data are anonymized" with no assessment. |
| 12. Data management and security | Storage, access control, retention, destruction, breach procedure. | Research data stored with weaker controls than operational data. |
| 13. Reproducibility and release plan | Tiered artifact plan; what cannot be released and why. | Promise to "share upon request." |
| 14. Stop rules and deviation handling | Conditions to pause or end; deviation log procedure. | None. |
| 15. Roles and conflicts | Who does what; funding; conflicts and structural safeguards; publication rights. | Partner veto not disclosed. |
| 16. Timeline and risks | Milestones; dependency on partner access; contingency. | No fallback if access is withdrawn. |

Two habits distinguish strong protocols. First, they contain **predeclared failure conditions**: "If inter-rater κ on the pilot is below the target we set in Section 8, we will revise the rubric and repeat the pilot; we will not proceed to the main study." Second, they make the **counterfactual** explicit: what would the comparison condition look like, and why is it a fair alternative rather than a straw man?

### 1.10 Practical activity: an offline measurement lab

*All records are synthetic.* The following Python script uses only the standard library. It computes, for twelve synthetic incidents, (a) a naive mean time-to-contain that drops incidents still open when observation closed, (b) a lower-bound mean that counts open incidents at their observed duration, (c) a Kaplan–Meier median that treats open incidents as censored, (d) Cohen's kappa for two raters who judged each response "adequate" or "inadequate," and (e) positive predictive values at two base rates. Run it offline; it reads and writes no files.

```python
"""OpenCyber Academy doctoral IR, Chapter 1 offline lab. All records are synthetic."""
from collections import Counter

# case_id, hours_to_contain (None = not contained when observation closed), observed_hours, rater_a, rater_b
CASES = [
    ("S01", 2.0, 2.0, "adequate", "adequate"),
    ("S02", 5.5, 5.5, "adequate", "inadequate"),
    ("S03", None, 72.0, "inadequate", "inadequate"),
    ("S04", 1.0, 1.0, "adequate", "adequate"),
    ("S05", 30.0, 30.0, "inadequate", "inadequate"),
    ("S06", None, 48.0, "inadequate", "adequate"),
    ("S07", 8.0, 8.0, "adequate", "adequate"),
    ("S08", 3.0, 3.0, "adequate", "adequate"),
    ("S09", None, 96.0, "inadequate", "inadequate"),
    ("S10", 12.0, 12.0, "adequate", "inadequate"),
    ("S11", 0.5, 0.5, "adequate", "adequate"),
    ("S12", 20.0, 20.0, "inadequate", "inadequate"),
]

def naive_mean_contained(cases):
    xs = [c[1] for c in cases if c[1] is not None]
    return sum(xs) / len(xs), len(xs)

def km_median(cases):
    """Kaplan-Meier product-limit estimate; returns first time S(t) <= 0.5, or None."""
    events = sorted((c[2], c[1] is not None) for c in cases)
    at_risk, surv = len(events), 1.0
    i = 0
    while i < len(events):
        t = events[i][0]
        d = sum(1 for e in events if e[0] == t and e[1])
        n_t = sum(1 for e in events if e[0] == t)
        if d:
            surv *= (at_risk - d) / at_risk
            if surv <= 0.5:
                return t, round(surv, 4)
        at_risk -= n_t
        i += n_t
    return None, round(surv, 4)

def cohen_kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in set(a) | set(b))
    return po, pe, (po - pe) / (1 - pe)

def ppv(sens, fpr, prevalence):
    tp = sens * prevalence
    fp = fpr * (1 - prevalence)
    return tp / (tp + fp)

if __name__ == "__main__":
    mean, k = naive_mean_contained(CASES)
    print(f"contained cases: {k} of {len(CASES)}")
    print(f"naive mean hours (contained only): {mean:.2f}")
    lb = sum(c[2] for c in CASES) / len(CASES)
    print(f"lower-bound mean hours (censored counted at observed time): {lb:.2f}")
    t, s = km_median(CASES)
    print(f"Kaplan-Meier median hours: {t} (S={s})")
    po, pe, kappa = cohen_kappa([c[3] for c in CASES], [c[4] for c in CASES])
    print(f"observed agreement: {po:.3f}; chance agreement: {pe:.3f}; kappa: {kappa:.3f}")
    print(f"PPV at 0.1% prevalence, 99% sensitivity, 1% FPR: {ppv(0.99, 0.01, 0.001):.3f}")
    print(f"PPV at 10% prevalence, 99% sensitivity, 1% FPR: {ppv(0.99, 0.01, 0.10):.3f}")
```

Expected output (verified by running the script with Python 3):

```text
contained cases: 9 of 12
naive mean hours (contained only): 9.11
lower-bound mean hours (censored counted at observed time): 24.83
Kaplan-Meier median hours: 8.0 (S=0.5)
observed agreement: 0.750; chance agreement: 0.500; kappa: 0.500
PPV at 0.1% prevalence, 99% sensitivity, 1% FPR: 0.090
PPV at 10% prevalence, 99% sensitivity, 1% FPR: 0.917
```

**Interpretation.** The naive mean (9.11 hours) silently removes the three slowest incidents. Counting them at their observed durations raises the mean to 24.83 hours, and even that is only a *lower bound*, because those incidents were still open. The true mean cannot be estimated from these data without further follow-up or a model for the tail. The Kaplan–Meier median (8.0 hours) uses the censored cases correctly as "at risk" until they leave observation and is the most defensible single summary here. The raters agreed on 9 of 12 cases (75%), but because both rated roughly half the cases "adequate," half of that agreement is expected by chance, giving κ = 0.50: the rubric needs work before it can support an outcome analysis. Finally, the same classifier performance yields a very different value to responders depending on prevalence.

### 1.11 Using the synthetic case corpus as a methods resource

The lower-level books in this series built three synthetic cases: Harbor Library (rapid), Cedar Training Network (professional) and Lumen Library Reservations (technical). At doctoral level they are useful as **scenario seeds** for simulated study conditions — for example, as tabletop cases presented to responders under two workflows in Chapter 5. They are *not* data. Their timelines were written to teach, so their ground truth is known and their difficulty was chosen by an author. Any measurement taken on them is evidence about how participants perform on those scenarios, under those conditions. A thesis that uses them should cite them as instruments, document which version was used, and resist the temptation to generalize from "responders did better on the Harbor scenario" to "responders do better."

### Common errors and limits

- Treating operational access to incident records as research authorization.
- Calling data "anonymized" because names were removed, without a re-identification assessment that considers organizations as well as individuals.
- Reporting a time metric without defining its start and end events or handling censored incidents.
- Using analyst dispositions as ground truth without auditing them.
- Writing a preregistration after exploring the confirmation data, or omitting the deviation log.
- Citing a vendor caseload report as a population estimate.
- Coding a single "root cause" per incident without justifying the modeling choice.
- Generalizing from synthetic or exercise scenarios to field performance.
- Attaching a citation that has not been read, or one generated by a tool and not verified.
- Limit of this chapter: it gives structures for legal and ethical analysis but is not legal advice and does not replace an institutional review.

### Exercises — chapter 1

**EX001 — Claim ladder audit.** *Objective:* separate observation, inference and claim in incident writing. *Inputs:* the synthetic post-incident paragraph below. *Constraints:* use only the paragraph; do not add facts. *Steps:* (1) split the paragraph into atomic statements; (2) label each as report, observation, inference, case claim or research claim (§1.2.2); (3) for each inference, name its hidden assumption and one defeating observation; (4) rewrite the final sentence as a scoped claim. *Expected evidence:* a table of statements with labels, assumptions and defeaters, plus the rewritten claim. *Rubric:* 3 = every statement correctly labeled, every inference has a testable defeater, rewrite is scoped; 2 = one mislabel or vague defeater; 1 = labels present but inferences treated as observations; 0 = no separation.

> *Synthetic paragraph:* "At 02:14 the EDR console showed `powershell.exe` launched by `winword.exe` on host FIN-22. The user had opened a phishing email. The attacker then moved laterally to FIN-31 using stolen credentials, as shown by a 02:40 logon event. Our new email filter, deployed last month, would have blocked the message. This proves that email filtering reduces ransomware risk."

**EX002 — Hindsight-resistant interview guide.** *Objective:* design data collection that limits outcome bias. *Inputs:* a synthetic incident timeline with five time-stamped artifacts of your choosing (alert, ticket note, chat message, containment action, status update). *Constraints:* the guide must be usable 2–4 weeks after the incident; no question may reveal the final outcome before asking about earlier reasoning. *Steps:* (1) write six to eight questions anchored to the artifacts in time order; (2) mark which questions risk eliciting post hoc rationalization and how you mitigate it; (3) write a one-paragraph consent statement that addresses blame and employment risk. *Expected evidence:* the guide, mitigation notes and consent paragraph. *Rubric:* 3 = time-anchored, outcome-blind ordering, explicit mitigation, consent addresses blame and withdrawal; 2 = one of these weak; 1 = generic questions; 0 = leading questions or outcome revealed first.

**EX003 — Constraint mapping and tiered release.** *Objective:* produce an honest open-science plan for restricted incident data. *Inputs:* the NMS-CSIRT worked example in §1.8, plus the following added facts: two incidents are under a litigation hold; one threat-intelligence feed used in tickets was received as TLP:AMBER; the CSIRT's MSSP contract forbids naming the MSSP. *Constraints:* use the constraint taxonomy (§1.4.3) and tiers (§1.4.5). *Steps:* (1) list each artifact the thesis would produce; (2) map each to its binding constraints; (3) assign a release tier and justify it; (4) draft the thesis's "Open Science" paragraph (150–250 words). *Expected evidence:* artifact–constraint–tier table and paragraph. *Rubric:* 3 = every constraint correctly applied, tiers maximal but lawful, paragraph states what reviewers cannot check; 2 = one misapplied constraint; 1 = blanket "data unavailable"; 0 = proposes releasing restricted material.

**EX004 — Ethical Impact Assessment.** *Objective:* apply the four Menlo principles to a concrete study. *Inputs:* a proposed study in which a researcher will observe NMS-CSIRT's on-call responders during live incidents for three months and record decision points. *Constraints:* use the Menlo structure (§1.5.2) and authorization layers (§1.5.3); the response must always take priority. *Steps:* (1) list stakeholders and their risks; (2) for each principle, state the main risk and a safeguard; (3) list required authorizations in order; (4) write five stop rules; (5) state the incidental-discovery procedure. *Expected evidence:* a two-page assessment. *Rubric:* 3 = stakeholders include data subjects, responders, organization and public; safeguards specific; stop rules testable; 2 = one stakeholder group or layer missing; 1 = generic ethics text; 0 = treats manager approval as sufficient consent.

**EX005 — Measurement lab.** *Objective:* quantify how censoring, rater agreement and base rates change conclusions. *Inputs:* the script in §1.10. *Constraints:* run offline; record exact outputs. *Steps:* (1) run the script and confirm the expected output; (2) in a copy, delete the three censored cases entirely and recompute the Kaplan–Meier median; (3) in another copy, change rater B's judgment of S10 to "adequate" and recompute kappa; (4) compute PPV for 99% sensitivity and 1% FPR at 1% prevalence; (5) write 150 words interpreting all three changes. *Expected evidence:* the outputs and interpretation. *Rubric:* 3 = exact values and correct interpretation of bias direction; 2 = values correct, interpretation thin; 1 = one value wrong; 0 = no runs.

**EX006 — Failure-mode review of a claim.** *Objective:* apply the failure-mode catalog (§1.7) as a reviewer. *Inputs:* this synthetic abstract: "We surveyed 212 security leaders. Organizations that ran quarterly tabletop exercises reported 40% faster containment than those that did not. Tabletop exercises therefore cut containment time by 40%." *Constraints:* identify at least five distinct failure modes; do not invent additional data. *Steps:* (1) name each failure mode and quote the phrase that triggers it; (2) explain the alternative explanation it opens; (3) propose a design change; (4) rewrite the conclusion to match the evidence. *Expected evidence:* review table and rewritten conclusion. *Rubric:* 3 = five or more correctly identified with design changes and a properly scoped rewrite; 2 = three or four; 1 = generic criticism; 0 = accepts the claim.

**EX007 — Defensible protocol skeleton.** *Objective:* write the first version of a protocol for the revised NMS-CSIRT question (§1.8, Step 5). *Inputs:* the sixteen-section template in §1.9. *Constraints:* 1,200–2,000 words; at least three predeclared failure conditions; the analysis plan must handle censoring if any time measure is used and must state base rates. *Steps:* complete every section; mark assumptions you could not verify. *Expected evidence:* versioned protocol (v0.1) with a deviation-log template. *Rubric:* 3 = all sections, claim matches design, failure conditions testable, release tiers and stop rules present; 2 = one or two sections thin; 1 = several missing; 0 = protocol claims effect on real response from benchmark accuracy.

### Chapter synthesis

Incident-response research studies events that happen once, are shaped by the response itself, are read with hindsight and are wrapped in legal and ethical restrictions. Those conditions do not excuse weak claims; they demand explicit ones. The researcher's basic tools are the observation–inference–claim distinction, pre-specification with a transparent deviation log, a tiered reproducibility plan that releases what can safely be released, layered authorization and an Ethical Impact Assessment, measures whose validity is argued rather than assumed, and a protocol that states in advance what would count as failure. Chapter 2 uses these tools to read the research literature and locate a question that is genuinely open.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Research frontier in incident response systems

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Scope a literature search on an incident-response question systematically, with a recorded protocol that another researcher could repeat.
2. Read primary studies for the *claim they can support*, using Chapter 1's evidence ladder and failure-mode catalog.
3. Distinguish competing theoretical accounts of incident decision-making and say what each predicts differently.
4. Build a literature map that shows where evidence is strong, weak, conflicting or absent.
5. State a research gap as a falsifiable proposition rather than a topic, and test whether filling it would be a contribution.

Chapter 1 established how to judge a single claim. This chapter applies that judgment to a *body* of work. Its output — a literature map and a falsifiable gap statement — becomes the input to Chapter 3's contribution proposal.

### 2.1 Why "the literature" is harder to find in incident response

Incident-response knowledge is spread across very different kinds of publication:

| Source type | Examples | Strength | Typical weakness |
|---|---|---|---|
| Peer-reviewed security venues | Security conferences and journals; usable-security venues for human studies. | Methods scrutiny; citable. | Few studies of real response; detection-heavy. |
| Human-factors, safety and organizational research | Situation awareness, naturalistic decision-making, resilience engineering. | Mature theory of decisions under pressure. | Rarely tested in security settings. |
| Standards and government guidance | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final). | Consensus practice; widely adopted vocabulary. | Recommendations, not empirical tests of effectiveness. |
| Public incident reviews | Government or independent board reviews of significant incidents, such as those of the [Cyber Safety Review Board](https://www.cisa.gov/resources-tools/groups/cyber-safety-review-board-csrb) established under Executive Order 14028. | Rich case detail; access to parties. | Single cases; selection of high-profile events; mandate shapes questions. |
| Vendor and industry reports | Annual breach and threat reports from response and security firms. | Large caseloads; current. | Caseload bias; definitions vary; methods often thin. |
| Practitioner talks, blogs, postmortems | Conference talks, engineering blogs, published postmortems. | Operational detail; candid. | Uneven verification; survivorship. |

*In plain terms:* No single source type is trustworthy on its own: peer-reviewed studies are rigorous but narrow, practitioner sources are realistic but unaudited, so a review must state in advance how it will weigh each.

A doctoral literature review must decide, in advance, which of these it will treat as **evidence** for an empirical claim, which as **context** (what practitioners believe or recommend), and which as **case material**. Mixing them without labels is how a review ends up citing a vendor percentage as if it were a population estimate, or a standard's recommendation as if it were a tested finding.

### 2.2 Systematic scoping

#### 2.2.1 Systematic review, scoping review, narrative review

A **systematic review** answers a focused question by locating, appraising and synthesizing all eligible studies using a predefined, reproducible method. A **scoping review** maps the extent and nature of evidence on a broader topic without necessarily appraising quality in depth. A **narrative review** synthesizes selectively according to the author's judgment. All three are legitimate; the integrity failure is to present a narrative review as if it were systematic.

The [PRISMA 2020 statement](https://doi.org/10.1136/bmj.n71) (Page et al., 2021), which updated the [2009 PRISMA statement](https://doi.org/10.1371/journal.pmed.1000097), provides a reporting guideline for systematic reviews, including a checklist and a flow diagram that records how many records were identified, screened, excluded (with reasons) and included. PRISMA was developed mainly for health research, and some items (for example, risk-of-bias tools designed for clinical trials) need adaptation for security. Its core discipline transfers directly: say where you searched, with which terms, when, how records were screened and by whom, and why each excluded full text was excluded.

#### 2.2.2 A search protocol for an IR question

Write the search protocol before searching, and version it like the research protocol in Chapter 1.

1. **Question in structured form.** For decision-support research, a useful frame is *population* (who decides — tier-1 analysts, incident leads), *intervention or exposure* (the decision aid, process or condition), *comparison* (what they would otherwise do), *outcome* (decision quality, time, error, workload) and *context* (SOC, CSIRT, MSSP, exercise, field).
2. **Sources.** Bibliographic databases and digital libraries of the main security, human-factors and computing publishers; proceedings of usable-security venues; standards bodies; selected grey literature with explicit inclusion criteria.
3. **Search strings.** Synonym sets for each element, e.g. *("incident response" OR "security operations" OR SOC OR CSIRT) AND (triage OR "alert" OR "decision support" OR handoff) AND (study OR evaluation OR experiment OR interview)*. Record the exact string per database and the date run.
4. **Eligibility criteria.** Empirical study (any design) of human or human–machine decisions in a security-response setting; excludes purely algorithmic detection papers *unless* they evaluate effects on analyst decisions.
5. **Screening.** Two screeners independently screen titles and abstracts and then full texts, with disagreement resolved by discussion and agreement recorded (Chapter 1's kappa applies).
6. **Extraction.** A form recording design, setting, sample, measures, main claim, the claim's evidence-ladder level and key threats.
7. **Snowballing.** Backward (references) and forward (citations) searches from included studies, recorded separately.
8. **Stopping rule.** State when the search ends — for example, when two successive snowballing rounds yield no new eligible study.

#### 2.2.3 Appraisal without a clinical toolkit

Security lacks widely adopted risk-of-bias instruments for human studies. Build an appraisal form from Chapter 1: unit of analysis; sampling frame and selection; construct definitions and measure validity; comparison condition; blinding; rater agreement; base rates; time-respecting splits for learned components; artifact availability; ethics statement. For machine-learning components, the ten pitfalls of [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) serve as a ready checklist. Record each judgment with a quotation or page reference so that a second appraiser can check it.

### 2.3 Competing theoretical accounts of incident decision-making

A gap is meaningful only relative to theory: what do we expect to happen, and why? Several traditions offer different accounts of how responders decide, and they make different predictions about what would help.

#### 2.3.1 Situation awareness

[Endsley (1995)](https://doi.org/10.1518/001872095779049543) proposed a theory of situation awareness in dynamic systems with three levels: perception of elements in the environment, comprehension of their meaning and projection of their future status. Applied to response, the theory predicts that decision errors often arise from failures of perception (the relevant signal was not seen), comprehension (seen but misread) or projection (understood but its consequences not anticipated), and that aids should be designed for the level at which failures occur. Its prediction for a handoff: the receiving responder's errors will cluster at comprehension and projection if the handoff transmits facts without their significance.

#### 2.3.2 Naturalistic decision-making and skilled intuition

[Kahneman and Klein (2009)](https://doi.org/10.1037/a0016755), writing from the heuristics-and-biases and naturalistic decision-making traditions respectively, argued that skilled intuition can develop when the environment is sufficiently regular to be predictable and when people have adequate opportunity to learn those regularities through practice and feedback. Applied to response, this predicts that intuition will be reliable for frequent, well-fed-back tasks (routine alert dispositions in a stable environment) and unreliable for rare, novel or poorly fed-back ones (a first-of-its-kind intrusion, or dispositions never checked against outcome). It predicts that decision aids will help most where feedback is poor.

#### 2.3.3 Sociotechnical and organizational accounts

Fieldwork such as the [six-month anthropological study of a corporate SOC](https://www.usenix.org/conference/soups2015/proceedings/presentation/sundaramurthy) treats response performance as an emergent property of human, technical and managerial factors in cycles — for example, morale, skill growth, automation and management metrics reinforcing one another. The [interview study by Kokulu et al. (2019)](https://doi.org/10.1145/3319535.3354239) found disagreements between SOC managers and analysts. These accounts predict that a decision aid will succeed or fail depending on organizational fit — whether it changes workload, autonomy, metrics and trust — not only on its information content.

#### 2.3.4 Detection-centric and automation accounts

Much security research implicitly treats response quality as downstream of detection quality: better alerts, fewer false positives, better prioritization. This account predicts that improving classifier performance improves response. [Sommer and Paxson (2010)](https://doi.org/10.1109/SP.2010.25) and [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) show why lab performance may not translate to operations, and [Alahmadi et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi) show that "false positive" in practice often means a benign trigger, which a better classifier of maliciousness would not remove.

#### 2.3.5 Safety-science accounts

The complex-systems view summarized in [*How Complex Systems Fail*](https://how.complexsystems.fail/) treats failure as the joint product of multiple contributing factors and treats practitioners' adaptations as a source of safety as well as risk. It predicts that interventions that constrain responders' adaptive capacity (rigid playbooks, punitive metrics) may reduce some errors while increasing brittleness in novel incidents.

#### 2.3.6 Using competing accounts productively

The accounts are not mutually exclusive, but they make **different predictions** about the same intervention. That is what makes them scientifically useful. Consider a structured handoff note for incidents transferred between shifts:

| Account | Predicted effect of a structured handoff note | Observation that would favor this account |
|---|---|---|
| Situation awareness | Improves receiving responder's comprehension and projection if it transmits significance and expectations, not just facts. | Error reduction concentrated in comprehension/projection-type errors. |
| Skilled intuition | Helps most on novel or poorly fed-back incident types; little effect on routine ones. | Interaction between incident novelty and handoff condition. |
| Sociotechnical | Effect depends on workload, trust and whether the note is required by management metrics. | Effect varies by team and disappears when notes become box-ticking. |
| Detection-centric | Little effect; decision quality is bounded by alert quality. | No improvement when alert quality is held constant. |
| Safety science | Improves typical cases but may reduce adaptation in unusual ones if the template constrains reporting. | Worse performance on cases that do not fit the template. |

*In plain terms:* The theories disagree about what a handoff note should change; a good study measures the thing on which their predictions differ, not only whether the note "helps."

A study designed to discriminate among these predictions contributes more than one designed only to show that "the note helps."

### 2.4 Unresolved evidence

An open question exists when evidence is **absent**, **weak**, **conflicting** or **untransferred** (strong in one setting but untested in the setting of interest). Distinguish these carefully:

- *Absent*: no eligible study tests the claim. Verify by a documented search, not by a quick query.
- *Weak*: studies exist but cannot support the claim at the required level (e.g., only self-report, only single site, no comparison).
- *Conflicting*: well-conducted studies disagree. The interesting question is usually *why* — different populations, measures or contexts.
- *Untransferred*: strong evidence from another domain (aviation, medicine) has not been tested in security response, and there are reasons to doubt transfer (adversarial environment, different feedback structure).

The [IEEE Access survey of SOC research](https://doi.org/10.1109/ACCESS.2020.3045514) is an example of a published claim about *where* evidence is thin: it reports that research tends to address human and technological aspects while neglecting the processes, especially non-technical ones, that connect them. A doctoral researcher should treat such a statement as a starting hypothesis about the literature and verify it with their own documented search for the specific question at hand — surveys age, and their scope may differ from yours.

### 2.5 The contribution test

Not every gap is worth filling. A gap qualifies as a doctoral contribution when it passes four tests:

1. **Falsifiability.** It can be stated as a proposition that some feasible observation would refute. "Little is known about handoffs in incident response" is a topic. "Receiving responders given a structured handoff note make fewer comprehension-level errors than those given free-text notes, under incomplete telemetry" is falsifiable.
2. **Consequence.** If the proposition were shown true or false, some belief or practice would change. Ask who would decide differently.
3. **Novelty relative to the documented search.** The search protocol shows the proposition has not been tested at the required level in this setting.
4. **Feasibility under Chapter 1's constraints.** The data, authorization and measures exist or can be obtained ethically within the program.

A useful drafting format is: **"Current evidence supports A at level X in setting S. It does not establish B in setting T because [absent/weak/conflicting/untransferred evidence]. If B holds, practitioners would [decision]; if it does not, they would [other decision]. B can be tested by [design] and would be refuted by [observation]."**

### 2.6 Worked example: several primary studies of decision support during incident triage

*The real studies below are summarized from their published abstracts and pages linked; the synthetic studies are invented and labeled.*

A candidate's search on decision support during triage yields, among others:

| ID | Study | Type | Setting | Main claim | Ladder level | Key limits for our question |
|---|---|---|---|---|---|---|
| R1 | [Alahmadi, Axon and Martinovic (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi) | Survey (n = 20) and qualitative interviews (n = 21) | SOC practitioners | Most perceived FPs are benign triggers; elicit alarm properties (Reliable, Explainable, Analytical, Contextual, Transferable). | L2–L3 (qualitative, practitioner perspectives) | Does not test a decision aid's effect on decisions. |
| R2 | [Kokulu et al. (2019)](https://doi.org/10.1145/3319535.3354239) | 18 semi-structured interviews | SOC analysts and managers | Technical and non-technical issues; manager–analyst disagreements. | L2–L3 | Perception data; no outcome measures. |
| R3 | [Sundaramurthy et al. (2015)](https://www.usenix.org/conference/soups2015/proceedings/presentation/sundaramurthy) | Six-month anthropological fieldwork, grounded theory | One corporate SOC | Burnout as a human-capital problem with vicious cycles. | L3 (one site, rich) | One site; not about handoffs or aids directly. |
| R4 | [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) | Literature analysis + experiments | ML security systems | Ten pitfalls widespread. | L4 (about research practice) | About ML evaluation, not human decisions. |
| S1 | *Synthetic:* "Lab study of an alert-ranking aid" | Experiment, 24 students, 10 scenarios | University lab | Aid increased correct dispositions. | L4 in lab | Students, not responders; designer-labeled scenarios; no handoff. |
| S2 | *Synthetic:* "Vendor evaluation of an AI triage assistant" | Before/after in one MSSP | Field | 35% lower time-to-triage. | L2 | Vendor-run; time only; concurrent staffing change; no correctness measure. |
| S3 | *Synthetic:* "Shift handoff in a national CSIRT" | Interviews, 9 responders | Field | Handoffs lose context about hypotheses ruled out. | L2–L3 | Small, single site; no intervention tested. |

*In plain terms:* Read across the rows: the real studies describe context and trust, while the synthetic quantitative studies estimate effects in narrow settings; nobody has yet connected the two.

**Synthesis.** Real qualitative work (R1–R3) consistently points to context, trust, workload and organizational factors as determinants of triage quality. Experimental evidence about decision aids (S1) is lab-only with non-expert participants. Field evidence (S2) measures speed, not correctness, and is conflicted. Evidence specific to handoffs (S3) is qualitative and single-site. The candidate's gap statement:

> "Current evidence describes, at qualitative levels and in single sites, that context is lost at incident handoffs (S3) and that context determines how analysts judge alerts (R1). No study in our documented search tests whether a structured handoff artifact changes the *correctness* of receiving responders' decisions, as opposed to their speed, under incomplete telemetry. If it does, CSIRTs would adopt and standardize such artifacts; if it does not, effort should shift elsewhere (for example, to telemetry or staffing). This can be tested by a controlled simulation with responders as participants, scored by blinded expert raters, and would be refuted by no difference — or a difference favoring free-text notes — in comprehension- and projection-level errors."

This statement passes the four tests: it is falsifiable, consequential, novel relative to the documented search and feasible with simulation (Chapter 5). It also names a theoretical discriminator (error type), drawn from the situation-awareness account.

### 2.7 Practical activity: build a literature map

A literature map is a matrix with **claims** as rows and **studies** as columns. Each cell records whether the study supports, contradicts or does not address the claim, at which evidence level, and with which main limitation. Unlike a citation list, a map shows the *shape* of evidence. The following offline script builds a simple text map from a synthetic extraction table and flags claims supported only below a chosen level. It uses only the standard library.

```python
"""Chapter 2 literature-map helper. Study entries S1-S3 are synthetic; R1-R3 summarize published abstracts."""
EXTRACTION = [
    # (study, claim, direction, level)
    ("R1", "context-determines-alert-judgment", "supports", 3),
    ("R2", "manager-analyst-misalignment", "supports", 3),
    ("R3", "organizational-cycles-drive-performance", "supports", 3),
    ("S1", "aid-improves-correctness", "supports", 4),
    ("S2", "aid-improves-speed", "supports", 2),
    ("S3", "handoff-loses-context", "supports", 3),
    ("S1", "aid-improves-speed", "not-addressed", 0),
]
FIELD_THRESHOLD = 4  # a claim needs at least one level-4 field study to count as established

def build_map(rows):
    claims = {}
    for study, claim, direction, level in rows:
        claims.setdefault(claim, []).append((study, direction, level))
    return claims

if __name__ == "__main__":
    for claim, entries in sorted(build_map(EXTRACTION).items()):
        best = max((lvl for s, d, lvl in entries if d == "supports"), default=0)
        status = "established" if best >= FIELD_THRESHOLD else "open"
        cells = ", ".join(f"{s}:{d}:L{l}" for s, d, l in entries)
        print(f"{claim:42s} best=L{best} {status:11s} [{cells}]")
```

Expected output:

```text
aid-improves-correctness                   best=L4 established [S1:supports:L4]
aid-improves-speed                         best=L2 open        [S2:supports:L2, S1:not-addressed:L0]
context-determines-alert-judgment          best=L3 open        [R1:supports:L3]
handoff-loses-context                      best=L3 open        [S3:supports:L3]
manager-analyst-misalignment               best=L3 open        [R2:supports:L3]
organizational-cycles-drive-performance    best=L3 open        [R3:supports:L3]
```

The output deliberately exposes a flaw in the script's rule: it marks "aid-improves-correctness" as *established* because S1 is a level-4 study — but S1 is a **lab** study with students, and the script's threshold was described as requiring a *field* study. A map is only as good as its coding scheme. Exercise EX012 asks you to fix this by adding a setting attribute and re-running.

### 2.8 From map to frontier

The research frontier is not "everything not yet studied." It is the set of claims that (a) matter for decisions, (b) are theoretically contested or unexamined, and (c) can now be tested because of new data, methods or access. A frontier statement for a thesis typically names two or three adjacent open claims and explains why the chosen one is the right first step — usually because its answer changes how the others should be studied.

For the Handoff Study, the adjacent claims are: whether handoff artifacts change correctness (chosen); whether effects depend on telemetry completeness (deferred to Chapter 6 as a boundary condition); and whether artifacts change long-term team learning (out of scope — would require longitudinal field access).

### 2.9 Decision science under uncertainty: a deeper reading

Section 2.3 introduced the theoretical accounts briefly so that the literature map could be built. A doctoral candidate needs more: enough command of each tradition to know what it actually claims, what its evidence base looks like, and where it is routinely misapplied to security work. This section revisits the decision-science traditions in that spirit. It is not a survey of psychology; it is a reading guide for an incident-response researcher who must use these theories as sources of testable predictions.

#### 2.9.1 Situation awareness as a measurable construct

Endsley's theory paper is frequently cited in security; her companion measurement paper is cited far less, and that asymmetry matters. In [*Measurement of Situation Awareness in Dynamic Systems* (Endsley, 1995)](https://doi.org/10.1518/001872095779049499) she discusses how situation awareness can be measured, including a freeze-probe approach in which a simulation is paused and the operator is asked questions about the current and projected state of the situation. The method that emerged from this line of work is widely known as SAGAT. Three features of the approach are directly relevant to incident-response research.

First, measurement is **tied to a task analysis**. The probe questions are not generic ("how aware are you?") but derived from the information requirements of the particular role. For a receiving responder after a handoff, the requirements would include which hosts are known compromised, which hypotheses are already excluded, which telemetry sources are unavailable, and what the adversary is expected to do next. A researcher who skips the requirements analysis and writes probe questions from intuition is measuring their own model of the task, not the responder's.

Second, the approach **distinguishes levels**. Because perception, comprehension and projection are probed separately, the researcher can test the mechanism claimed in Chapter 3 rather than only the net effect. That is the reason the Handoff Study separates perception errors from comprehension-and-projection errors: a handoff aid that improves the latter without the former is evidence for the mechanism, while an aid that improves only perception suggests a different mechanism (for example, that the template simply lists more facts).

Third, freeze-probe measurement is **intrusive**. Pausing a scenario can itself change behavior: participants may anticipate probes and rehearse facts they would otherwise ignore. Endsley discusses this concern; a study that uses freeze probes should report how often and when they occurred and should check whether performance after probes differs from performance before them. In a within-subject design, the probe schedule must be identical across conditions, or the probe becomes a confound.

The practical lesson for incident-response research is that "situation awareness" is not a feeling to be rated on a seven-point scale at the end of an exercise. Self-ratings of awareness exist and have uses, but they answer a different question (how confident does the responder feel?) and are known in the human-factors literature to diverge from probe-based measures. A thesis that reports only self-rated awareness should not claim to have measured awareness in Endsley's sense.

#### 2.9.2 Recognition-primed decisions

The naturalistic decision-making tradition began with field studies of experienced decision makers working under time pressure. In [*Rapid Decision Making on the Fire Ground* (Klein, Calderwood and Clinton-Cirocco, 1986)](https://doi.org/10.1177/154193128603000616), the authors reported interviews with fireground commanders and found that commanders rarely described comparing multiple options against one another. Instead they described recognizing the situation as a type, which suggested a plausible course of action, which they then evaluated by mentally simulating it — and modified or replaced only if the simulation exposed a problem. This pattern became known as the recognition-primed decision (RPD) model. [Klein (2008)](https://doi.org/10.1518/001872008X288385) later summarized the naturalistic decision-making program as studying how people actually make decisions in demanding real-world settings rather than how they should decide under idealized assumptions.

For incident-response research, RPD changes what a decision aid should be expected to do.

- **Aids that present option lists may be ignored by experts.** If an experienced responder recognizes the situation and generates one workable action, a tool that presents five ranked options may be used to confirm the action already chosen rather than to choose among options. A study that measures whether the "top recommendation" was followed will then overestimate the tool's influence.
- **Aids that support recognition and mental simulation may help most.** Information that sharpens the recognition step (what *kind* of incident is this?) or that supplies inputs to the simulation step (what will happen if we isolate this host?) fits the way experts are described as deciding. The SHA's "expectations" field is designed with this in mind: it hands the receiver the sender's projection, which the receiver can then simulate against.
- **Novices may decide differently.** RPD describes experienced decision makers. Students and junior analysts, who lack a repertoire of situation types, may compare options more deliberately or may adopt the first option seen. A study that pools novices and experts may average two different decision processes and find a muddy effect that describes neither. This is a reason to stratify by experience (Chapter 5 §5.2) and to pre-specify experience as a moderator.

RPD also implies a caution about research methods. The original evidence was based on interviews after the fact. Retrospective reports are vulnerable to reconstruction and to the hindsight bias discussed in Chapter 1. Critical-decision interviewing techniques attempt to reduce this by anchoring the interview on specific moments and cues, but they cannot eliminate it. When an incident-response study borrows these methods, it should state that the decision process it reports is the process as described, not as observed.

#### 2.9.3 Heuristics, biases and the conditions for trusting intuition

The heuristics-and-biases tradition, introduced to a broad audience in [Tversky and Kahneman (1974)](https://doi.org/10.1126/science.185.4157.1124), described judgmental heuristics — representativeness, availability, and adjustment from an anchor — that are often useful but lead to systematic errors in identifiable conditions. The paper predates computer incident response, but each heuristic has an obvious response analogue: judging an alert as malicious because it resembles a remembered intrusion (representativeness), estimating the likelihood of ransomware from recent headlines (availability), and failing to revise an initial scope estimate as evidence accumulates (anchoring).

A doctoral researcher should resist two tempting moves. The first is to **diagnose biases from outcomes**: "the team anchored on the first hypothesis" is often written after an incident ended badly, but the same persistence would be called "focus" if the first hypothesis had been right. Without a record of the evidence available at each decision point, an anchoring diagnosis is a hindsight judgment. The second move is to **assume laboratory effect sizes transfer** to practice. Heuristics research largely used controlled tasks with defined probabilities; incident work involves ambiguous cues, collaboration and tools. The direction of a bias may carry over while its magnitude does not.

The productive synthesis is the one already cited in §2.3.2: [Kahneman and Klein (2009)](https://doi.org/10.1037/a0016755) agreed that intuitive judgment deserves trust when the environment is regular enough to be learned and the decision maker has had adequate practice with feedback. Incident response is not one environment but many. Disposition of a high-volume, well-understood alert type with confirmed outcomes may meet both conditions; scoping a novel intrusion in an unfamiliar network meets neither. A research design can operationalize this distinction by classifying scenarios by **feedback quality** (how often, and how quickly, would a real responder learn whether such a judgment was right?) and testing whether a decision aid's effect is larger where feedback is poor. That is a sharper prediction than "aids help," and it can fail.

#### 2.9.4 Sensemaking and the collapse of shared frames

Weick's analysis of the Mann Gulch fire, [*The Collapse of Sensemaking in Organizations* (Weick, 1993)](https://doi.org/10.2307/2393339), examined how a smokejumper crew's shared understanding of their situation and their roles broke down as conditions changed faster than the crew could reinterpret them. The analysis is a case study and should be cited as such: it generates concepts, not effect sizes. Its value for incident-response research is a vocabulary for phenomena that the situation-awareness framing can miss.

- **Sensemaking is social.** Understanding is constructed in interaction — in what people say to each other, which interpretations get voiced and which are suppressed. A handoff is precisely such an interaction. A study that measures only the receiver's individual awareness may miss whether the handoff conversation surfaced disagreements.
- **Role structure supports meaning.** Weick argued that when the crew's role structure dissolved, so did the shared basis for interpreting events. In response, role ambiguity (who is incident lead after the shift change?) may degrade understanding as much as missing facts. A handoff aid that transfers facts but leaves role transfer implicit could leave this failure untouched.
- **Commitment to a frame can be dangerous when the frame is wrong.** Dropping a familiar interpretation is costly; teams tend to hold it until evidence is overwhelming.

These ideas generate testable predictions. For example, if role ambiguity is a separate pathway, then adding an explicit "decision authority" field to the SHA should reduce errors of omission (actions nobody took because everybody assumed someone else would) even if it does not change comprehension scores. A thesis can treat sensemaking as a rival account of the same phenomenon and design a measure that distinguishes them.

#### 2.9.5 Drift toward boundaries

[Rasmussen (1997)](https://doi.org/10.1016/S0925-7535(97)00052-0) argued that risk management in a dynamic society is a control problem across levels — from government and regulators through companies and management to staff and work — and that work practices tend to migrate under pressures of efficiency and least effort toward the boundary of acceptable performance. Safety, in this view, depends on making boundaries visible and on feedback across levels, not only on rules at the operational level.

For incident response, Rasmussen's framing directs attention to decisions far from the console: staffing levels, alert-volume targets, outsourcing contracts, and reporting obligations. A response team under persistent pressure to close tickets quickly may migrate toward closing ambiguous cases as benign — not because any individual decides to accept risk, but because the local gradient rewards it. The Handoff Study is a micro-level intervention; Rasmussen's framing reminds the researcher that its effect may be swamped or reversed by pressures at higher levels. A transportability analysis (Chapter 6) that ignores management metrics is incomplete.

#### 2.9.6 What the traditions jointly imply for design

| Tradition | Unit of analysis | Typical evidence | Most useful prediction for the Handoff Study | Typical misuse in security research |
|---|---|---|---|---|
| Situation awareness | Individual operator in a dynamic task | Probe-based measures in simulation | Errors cluster at comprehension and projection when significance is not transmitted | Equating self-rated confidence with awareness |
| Naturalistic decision-making | Experienced practitioner in the field | Interviews, observation | Experts use the aid to support recognition and simulation, not option comparison | Applying expert findings to novice samples |
| Heuristics and biases | Individual judgment | Controlled experiments | Aid effect largest where feedback is poor and cues are ambiguous | Diagnosing bias from bad outcomes |
| Sensemaking | Group interaction | Case analysis | Role transfer is a separate pathway from fact transfer | Treating case narratives as effect estimates |
| Sociotechnical safety | Multi-level system | Case studies, modeling | Higher-level pressures moderate local interventions | Citing "complexity" to avoid making predictions |

*In plain terms:* Each tradition looks at a different level — one person, an expert, a judgment, a group, a whole system — and each makes a different, testable prediction about the handoff aid. The bottom row of misuses is a checklist for reviewing your own draft.

### 2.10 Incident-response teams and crisis coordination as research objects

#### 2.10.1 What empirical work on response teams shows

Direct empirical research on incident-response teams remains thinner than research on detection. [Ahmad, Hadgkiss and Ruighaver (2012)](https://doi.org/10.1016/j.cose.2012.04.001) studied incident response teams in organizational settings and discussed challenges in how response supports the wider security function, including the tendency for response to concentrate on technical recovery while organizational learning from incidents receives less attention. Together with the SOC fieldwork already cited in §2.3.3 and the interview evidence of [Kokulu et al. (2019)](https://doi.org/10.1145/3319535.3354239), it supports a cautious generalization: in the organizations studied, the "after" phases of response — learning, feedback to prevention, and dissemination — were weaker than the "during" phases. This is consistent with [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)'s decision to place improvement (ID.IM) inside the CSF's continuous functions rather than at the end of a linear life cycle.

For a doctoral literature review, the important feature of this body of work is its **method profile**: case studies, interviews and fieldwork in a small number of organizations, usually in one country and one sector, often without a comparison condition. That profile is appropriate for building concepts and inappropriate for estimating prevalence. A review that writes "studies show that most organizations neglect lessons learned" has converted a recurring qualitative theme into a population statement. The correct sentence names the method and setting: "interview and case studies in several organizations repeatedly report…"

#### 2.10.2 The incident command system as a coordination template

Large incidents involve coordination across teams and organizations: internal IT, legal, communications, executives, outside forensic firms, insurers, law enforcement, regulators and, sometimes, other victims. Public-safety disciplines developed the incident command system (ICS) for multi-agency emergencies. [Bigley and Roberts (2001)](https://doi.org/10.2307/3069401) studied ICS in a fire-department setting and analyzed it as a form of high-reliability organizing for complex and volatile task environments. Their analysis emphasizes that ICS combines a formal, bureaucratic structure with mechanisms that allow that structure to change quickly — roles can be activated, merged or reassigned as the incident evolves — and with practices for building and maintaining shared understanding of the situation.

Two cautions apply when security programs adopt ICS vocabulary. First, an organizational chart with ICS titles is not ICS in the sense Bigley and Roberts analyze; the flexibility mechanisms and the training that makes rapid restructuring safe are the substance. Second, fire departments respond to physically visible incidents with shared professional norms; cyber incidents are often ambiguous in scope for days and involve parties with conflicting legal interests. Whether ICS-style structures improve cyber-incident coordination is an empirical question, not a settled fact. A thesis that proposes them should treat that as a hypothesis.

#### 2.10.3 Cognition, communication, coordination and control

[Comfort (2007)](https://doi.org/10.1111/j.1540-6210.2007.00827.x), writing on crisis management in public administration, organized the problem around four linked capacities: cognition (recognizing the degree of emerging risk), communication, coordination and control. The framing is useful for incident-response researchers because it locates failures *between* organizations as well as within them. A cyber incident affecting a regional health network may involve a hospital, its managed-service provider, a software vendor, a national CSIRT and a regulator. Each has partial information; none controls the whole response. Delays and errors often arise at the interfaces: information that one party holds but cannot share under its contract or classification rules, or a decision that requires authority no single party has.

The Handoff Study as written examines handoffs between shifts in one team. The same mechanism — loss of hypotheses, gaps and expectations at a boundary — plausibly operates at organizational boundaries, with additional distortions introduced by information-sharing constraints such as [TLP 2.0](https://www.first.org/tlp/) designations, legal privilege and contractual confidentiality. That is a legitimate direction for future work (Chapter 8 §8.5), and it is also a reason to be careful about transporting a within-team result to cross-organization coordination.

### 2.11 Automation, AI assistance and the reliance problem

#### 2.11.1 Use, misuse, disuse and abuse

Much current interest in response research concerns automated triage, summarization and recommendation. The human-factors literature on automation provides the conceptual tools to study this well. [Parasuraman and Riley (1997)](https://doi.org/10.1518/001872097778543886) distinguished **use** of automation from **misuse** (over-reliance), **disuse** (under-reliance, such as ignoring or disabling it) and **abuse** (automating functions without due regard for the consequences for human performance). Each maps onto familiar response phenomena: analysts accepting an automated "benign" verdict without checking (misuse), analysts muting a noisy detection rule (disuse), and organizations automating containment actions whose failure modes no human is positioned to catch (abuse).

[Lee and See (2004)](https://doi.org/10.1518/hfes.46.1.50_30392) reviewed research on trust in automation and argued that the design goal is **appropriate reliance** — trust calibrated to the automation's actual capabilities in context — rather than maximal trust. [Parasuraman and Manzey (2010)](https://doi.org/10.1177/0018720810376055) reviewed complacency and automation bias and proposed an integrated, attention-based account of how both arise in human use of automation.

#### 2.11.2 Research design consequences for AI-assisted response

These ideas sharpen the pitfalls already listed in Chapter 1 from [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp):

1. **Accuracy of the aid is not the outcome.** A triage model's precision and recall describe the aid; the research question concerns the decisions of the human–aid team. A study that reports only model metrics has not studied response.
2. **Measure reliance directly.** To test calibration, the study must include cases where the aid is wrong. If the aid is correct on every scenario, agreement with the aid cannot be distinguished from good judgment. A well-designed evaluation deliberately includes a pre-specified fraction of aid errors and measures whether participants detect them.
3. **Separate conditions in which the aid is right from those in which it is wrong.** The aggregate effect of an aid can be positive while it causes serious harm on its error cases. Report outcomes stratified by aid correctness.
4. **Expect learning over time.** Reliance changes with exposure. A one-session laboratory study measures first impressions; operational reliance after months may differ. State the time horizon of the claim.
5. **Audit leakage before reporting accuracy.** [Kapoor and Narayanan (2023)](https://doi.org/10.1016/j.patter.2023.100804) documented data leakage as a widespread source of irreproducible and overoptimistic results across fields that use machine learning, and proposed a taxonomy of leakage types. In incident data, the commonest forms are temporal (training on cases that postdate test cases), duplicate (near-identical alerts in both splits) and label leakage (features computed from analyst notes that encode the disposition).
6. **Large language models add their own pitfalls.** When an assistant generates incident summaries, the outputs vary across runs and model versions, may contain fluent but unsupported statements, and may have been exposed during training to public material similar to the evaluation cases. A study should fix and record the model version and generation settings, run multiple samples, have raters score factual support against the source record, and treat public benchmarks as possibly contaminated. These points follow from general reproducibility requirements; they do not depend on any particular vendor's claims.

#### 2.11.3 A testable reliance prediction for the Handoff Study

Suppose a later version of the SHA is pre-filled by a summarization model. The reliance literature predicts that receivers will check pre-filled fields less carefully than fields written by a colleague whose reliability they know. A discriminating design would compare (a) human-written SHA, (b) model-pre-filled SHA with no errors, and (c) model-pre-filled SHA with one seeded error per scenario in the "ruled-out hypotheses" field, measuring whether the error propagates into the receiver's decision. Condition (c) is ethically acceptable in simulation and is the only way to estimate the cost of misuse.

### 2.12 Measuring response quality: what the metrics literature warns

Operational response programs report metrics such as mean time to detect, mean time to respond, ticket counts and SLA compliance. Research needs metrics with known validity. [Pendleton et al. (2016)](https://doi.org/10.1145/3005714) surveyed systems security metrics and organized them around vulnerabilities, defenses, threats and situations; their survey is useful for showing how varied and loosely defined such metrics are. [Herley and van Oorschot (2017)](https://doi.org/10.1109/SP.2017.38) examined security as a scientific pursuit and criticized, among other things, claims that cannot be tested and the gap between security claims and the observations that could support them.

From these sources and from the measurement discussion in Chapter 1, five warnings follow for incident-response metrics.

1. **Time metrics are censored and gamed.** Time to contain depends on when detection occurred, which depends on attacker behavior and on the detection pipeline. Incidents still open at the end of a reporting window are censored (Chapter 1's lab). Teams under time targets can close tickets early. A time metric needs a precise start event, end event, and a rule for open cases.
2. **Counts confound workload with performance.** More incidents handled may mean better throughput or worse prevention.
3. **Outcome metrics confound decision quality with luck.** A contained incident may reflect good decisions or a clumsy adversary (§1.2.4).
4. **Proxies drift.** A metric that was a good proxy when introduced loses validity once people optimize it.
5. **Aggregates hide distribution.** Mean time to respond can improve while the worst cases worsen. Report distributions and tails.

The Handoff Study's choice of rater-scored decision errors against pre-defined defensible options is a response to these warnings: it measures the decision directly, at a known moment, against a standard fixed before the outcome is known. Its cost is ecological validity, which Chapter 6 addresses.

### Common errors and limits

- Calling a review "systematic" without a recorded, repeatable search protocol and screening record.
- Treating standards' recommendations or vendor percentages as tested empirical findings.
- Mapping topics instead of claims; the map then cannot show contradictions.
- Declaring absence of evidence after one database query.
- Stating a gap as a topic ("handoffs are understudied") rather than a falsifiable proposition.
- Choosing a theory after the results to explain them (Chapter 1's HARKing) rather than using competing theories to design a discriminating test.
- Limit: this chapter's summaries of published studies rely on their abstracts and public pages; a real review must read and appraise full texts.

### Exercises — chapter 2

**EX008 — Search protocol.** *Objective:* write a repeatable search protocol. *Inputs:* the Handoff Study question. *Constraints:* at least three sources of different types; explicit eligibility criteria; stopping rule. *Steps:* (1) state the question in population–intervention–comparison–outcome–context form; (2) write search strings for two databases; (3) define eligibility and exclusion reasons; (4) define screening and agreement procedure; (5) define a stopping rule. *Expected evidence:* versioned protocol (≤ 2 pages). *Rubric:* 3 = repeatable by another researcher, criteria unambiguous, agreement measured; 2 = one element vague; 1 = keyword list only; 0 = none.

**EX009 — Appraisal form application.** *Objective:* appraise a study for the claim it can support. *Inputs:* synthetic study S2 (§2.6). *Constraints:* use the appraisal elements in §2.2.3. *Steps:* complete the form; assign an evidence level; list the three most serious threats; state the strongest claim S2 can support. *Expected evidence:* completed form and one-sentence claim. *Rubric:* 3 = threats correctly identified (vendor conflict, speed-only, concurrent change, single site), claim properly limited; 2 = one threat missed; 1 = accepts 35% figure as effect; 0 = no appraisal.

**EX010 — Competing predictions.** *Objective:* derive discriminating predictions from theory. *Inputs:* the five accounts in §2.3 and a proposed intervention of your choice (not the handoff note), e.g., automatic enrichment of alerts with asset-owner data. *Constraints:* each prediction must name an observable. *Steps:* build a table like §2.3.6; identify the one observation that would best discriminate between the two most plausible accounts. *Expected evidence:* table and a paragraph. *Rubric:* 3 = predictions differ and are observable, discriminator well chosen; 2 = predictions overlap; 1 = generic; 0 = no theory link.

**EX011 — Classify the evidence gap.** *Objective:* distinguish absent, weak, conflicting and untransferred evidence. *Inputs:* four synthetic statements: (a) "Two large field studies disagree on whether alert-volume caps reduce misses"; (b) "Checklists reduced errors in surgical handoffs; no security studies exist"; (c) "Three vendor reports claim AI triage halves response time"; (d) "No study in our documented search measured responder fatigue across 24-hour incidents." *Constraints:* justify each classification and propose the next research step. *Steps:* (1) restate each candidate gap as a question; (2) list the evidence that exists for it; (3) assign one gap type and justify it in one sentence; (4) name the study that would close it. *Expected evidence:* four short paragraphs. *Rubric:* 3 = all classified correctly with appropriate next steps; 2 = one misclassified; 1 = two or more; 0 = none.

**EX012 — Repair the literature map.** *Objective:* make a coding scheme match its stated rule. *Inputs:* the script in §2.7. *Constraints:* offline; keep all original rows. *Steps:* (1) add a setting field ("lab" or "field") to each row (R1–R3, S2, S3 field; S1 lab); (2) change the rule so a claim is established only with a level-4 *field* study; (3) run and record the output; (4) explain in 100 words what changed and why it matters. *Expected evidence:* modified code, exact output, explanation. *Rubric:* 3 = correct code, exact output with no claim established, clear explanation; 2 = output correct, explanation thin; 1 = rule still wrong; 0 = not run.

**EX013 — Falsifiable gap statement.** *Objective:* convert a topic into a contribution. *Inputs:* the topic "incident communication with executives during ransomware." *Constraints:* use the drafting format in §2.5; the refuting observation must be feasible. *Steps:* write the statement; test it against the four contribution tests; revise once. *Expected evidence:* draft, test notes, revision. *Rubric:* 3 = passes all four tests with explicit refutation; 2 = one test weak; 1 = still a topic; 0 = none.

**EX014 — Frontier memo.** *Objective:* justify a first study among adjacent open claims. *Inputs:* your EX013 statement and two adjacent open claims you identify. *Constraints:* 400–600 words; cite only sources you have read. *Steps:* describe the three claims; explain dependencies; justify the first; state what is out of scope and why. *Expected evidence:* memo. *Rubric:* 3 = dependencies clear, choice justified by how its answer shapes the others, scope honest; 2 = justification by convenience only; 1 = no dependency analysis; 0 = none.

### Chapter synthesis

A research frontier is found, not asserted. It emerges from a documented search, an appraisal that reads each study for the claim it can bear, a map of claims rather than topics, and competing theories that predict different outcomes. The output is a falsifiable gap statement that would change decisions if answered. Chapter 3 turns the Handoff Study's gap statement into a specific contribution with a mechanism, hypotheses, a baseline and predeclared failure conditions.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 08

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Original response-science contribution proposal

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Classify a proposed contribution as empirical, artifact, method or theory, and state what kind of evidence each requires.
2. Specify a causal mechanism precisely enough that it predicts *where* and *how* an effect should appear.
3. Write hypotheses with operational outcomes, a smallest effect of interest and directional predictions.
4. Choose a credible baseline and an active comparison that rule out trivial explanations.
5. List alternative explanations and design features that separate them from the proposed mechanism.
6. Predeclare failure conditions and a risk register for the project.

Chapter 2 produced a falsifiable gap: whether a structured handoff artifact changes the correctness of a receiving responder's decisions under incomplete telemetry. This chapter turns that gap into a proposal that a committee could approve and a hostile reviewer could not easily dismiss. Chapter 4 will test whether the baseline and the procedure are viable.

### 3.1 What counts as a contribution

A doctoral contribution changes what a competent community has warrant to believe or do. In incident-response research it usually takes one of four forms, often combined:

| Type | Example | Evidence it needs |
|---|---|---|
| Empirical | "Structured handoffs reduce comprehension errors under incomplete telemetry." | A study with comparison, valid measures and adequate precision. |
| Artifact | "A handoff template and tool that responders can use." | Evidence of usability and effect; documentation; availability. |
| Method | "A scoring protocol for incident decision quality with demonstrated rater agreement." | Reliability and validity evidence; reuse by others. |
| Theory | "Handoff errors are mainly failures of projection, not perception." | Discriminating predictions tested against alternatives (Chapter 2 §2.3.6). |

*In plain terms:* A contribution's type determines the evidence it must produce; an artifact needs evidence that it changes behavior, not just that people like it.

A common weakness is to propose an artifact and evaluate only whether people like it. Preference is a legitimate outcome for usability, but it is not evidence that the artifact improves decisions. Another weakness is to call a method "validated" because it was used once. State which type the thesis claims, and match evidence to type.

### 3.2 Mechanism before measurement

A **mechanism** explains *how* an intervention would produce an effect. Specifying it does three jobs: it tells the researcher which outcomes to measure, it predicts where the effect should be large or absent, and it gives critics something precise to attack.

The Handoff Study's mechanism, grounded in the situation-awareness account of [Endsley (1995)](https://doi.org/10.1518/001872095779049543), can be written as a chain:

1. During an incident, the sending responder holds working hypotheses, knowledge of what has been ruled out, knowledge of which telemetry is missing, and expectations about what will happen next.
2. Free-text handoffs tend to transmit current facts and pending tasks but omit *ruled-out hypotheses*, *known telemetry gaps* and *expectations* (this premise is supported only at qualitative level by synthetic study S3 in Chapter 2 and must be checked in the pilot).
3. Without these, the receiving responder (a) re-investigates eliminated hypotheses, (b) reads absence of evidence in missing telemetry as evidence of absence (Chapter 1 §1.2.3), and (c) fails to anticipate scheduled or likely developments.
4. A **Structured Handoff Artifact (SHA)** with required fields for these items transmits them.
5. Therefore receiving responders with an SHA will make fewer errors of comprehension (misreading the significance of missing data) and projection (failing to anticipate), but *not necessarily* fewer errors of perception (failing to see a signal present in the data).

The final clause is what makes the mechanism scientifically useful: it predicts a *pattern*, not just an improvement. If SHA reduced perception errors as much as comprehension errors, the proposed mechanism would be in doubt, and a more general explanation — for example, that any additional structure focuses attention — would gain support.

#### 3.2.1 The SHA specification (synthetic artifact)

| Field | Content | Mechanism link |
|---|---|---|
| H-current | Up to three working hypotheses, each with a confidence level and the key evidence. | Comprehension |
| H-ruled-out | Hypotheses eliminated, with the observation that eliminated each. | Prevents re-investigation |
| T-gaps | Telemetry sources unavailable or unreliable for affected assets, with the time window. | Prevents absence-of-evidence errors |
| Actions | Actions taken (with time and approver) and actions pending (with owner and deadline). | Continuity |
| Expect | What the sender expects to happen next and what would change their assessment. | Projection |
| Authority | Who can approve containment, communication and recovery decisions now. | Decision rights |

*In plain terms:* Every field in the handoff artifact exists because the mechanism says a particular kind of error is caused by missing information; a field without a mechanism link is decoration.

### 3.3 Hypotheses, outcomes and the smallest effect of interest

A hypothesis should name the population, condition, comparison, outcome and direction. For the Handoff Study:

- **H1 (primary).** Among experienced responders receiving a simulated incident at a handoff point under incomplete telemetry, those receiving an SHA will make fewer comprehension- and projection-type decision errors per scenario than those receiving the organization's standard free-text handoff.
- **H2 (mechanism pattern).** The reduction in H1 will be larger than any reduction in perception-type errors.
- **H3 (secondary).** SHA will not increase time to the first containment decision by more than a pre-specified margin (a non-inferiority hypothesis on speed).

**Outcome definitions.** Errors are coded by two blinded expert raters against a scenario-specific reference that lists, for each decision point, the information available at that moment (Chapter 1 §1.2.4) and the defensible options. Each error is assigned to *perception* (relevant signal present in the materials but not used), *comprehension* (signal used but significance misread, including treating missing telemetry as negative evidence) or *projection* (failure to anticipate a development signaled in the materials). The codebook, examples and rater-training procedure are part of the protocol, and agreement is reported (Chapter 1 §1.6.4).

**Smallest effect of interest (SEOI).** Before any data, the researcher states the smallest difference that would matter in practice. Here the reasoning might be: "A reduction of fewer than 0.5 comprehension/projection errors per scenario would not justify the time cost of completing an SHA during a busy shift." The SEOI must be justified by practical consequence, not chosen to make a study feasible, and it drives the sample-size reasoning in Chapter 4. A SEOI also lets a null result be informative: if the confidence interval excludes effects as large as the SEOI, the study supports "no practically important effect," not merely "no significant effect."

### 3.4 Baselines and comparisons

A **baseline** is what the intervention is compared against. A weak baseline makes any intervention look good. Three principles:

1. **Use what practitioners actually do, not a degraded version.** The baseline is NMS-CSIRT's standard free-text handoff, written by responders who are given the same time as the SHA group. Comparing SHA with "no handoff" would test a different and less interesting question.
2. **Add an active control when a trivial explanation is plausible.** SHA asks senders to spend more time and write more. An *attention-control* condition — a free-text handoff with the same minimum length and time allocation but no required fields — separates "structure" from "more effort."
3. **Reproduce published baselines before claiming improvement.** If a prior study reports a baseline error rate or a benchmark score, it should be reproduced under your conditions (Chapter 4). The [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) pitfall of *inappropriate baselines* applies to human-study designs as well as to machine learning.

The proposal thus has three conditions: **Standard** (free text, usual practice), **Attention-control** (free text with equalized effort) and **SHA**. H1 compares SHA with Standard; a secondary comparison of SHA with Attention-control tests whether structure matters beyond effort.

### 3.5 Alternative explanations and how to separate them

For every proposed mechanism, list rival explanations and the design feature that addresses each:

| Alternative explanation | Why plausible | Design feature |
|---|---|---|
| More effort, not structure | SHA takes longer to write and read. | Attention-control condition with equalized time and length. |
| Sender quality | Better senders write better handoffs regardless of format. | Handoffs pre-written for each scenario by trained senders, standardized across conditions; or senders randomized. |
| Novelty / demand effects | Participants try harder with a new artifact or guess the hypothesis. | Cover story limited to "comparing handoff formats"; all conditions presented as legitimate; outcome raters blind. |
| Scenario difficulty imbalance | Some scenarios are easier. | Each participant sees each condition across scenarios in a counterbalanced order (within-subject design) or scenarios randomized. |
| Rater expectation | Raters favor SHA if they know the condition. | Raters see decisions only, with condition-identifying text removed. |
| Learning across scenarios | Later scenarios are easier because of practice. | Counterbalanced order; period effect modeled. |
| Telemetry gap salience, not handoff | Scenarios with obvious gaps are solved by anyone. | Vary gap salience as a factor; test interaction. |

*In plain terms:* For each competing explanation of a positive result, the design includes a specific feature that would expose it; the table is the study's internal-validity defence in compact form.

This table becomes the core of the protocol's internal-validity section and is often the part of a proposal reviewers read most closely.

### 3.6 Predeclared failure conditions

A proposal should say, before data are collected, what results would count against the contribution and what the researcher would do. For the Handoff Study:

| ID | Condition | Consequence |
|---|---|---|
| F1 | Pilot rater agreement on error type below the protocol target. | Revise codebook and repeat pilot; do not start main study. |
| F2 | In the pilot, free-text handoffs already contain ruled-out hypotheses and telemetry gaps in most cases. | Mechanism premise 2 fails; redesign or abandon SHA as framed. |
| F3 | Main-study confidence interval for H1 excludes the SEOI. | Report a precise null: SHA does not produce a practically important reduction under these conditions. |
| F4 | SHA reduces perception errors as much as comprehension/projection errors (H2 fails). | Report that the mechanism is not supported even if H1 holds; reframe as general structure effect. |
| F5 | SHA vs. Attention-control shows no difference while both beat Standard. | Contribution is effort, not structure; narrow the claim. |
| F6 | SHA increases time to first containment decision beyond the non-inferiority margin. | Report trade-off; do not recommend adoption without addressing time cost. |

*In plain terms:* These are the results that would force the claim to shrink, written down before the data exist so that nobody can explain them away afterwards.

Each condition maps to a specific narrowing of the claim. That mapping is what makes the contribution falsifiable in practice rather than in principle.

### 3.7 Risk register

Doctoral projects fail more often from access, recruitment and measurement problems than from wrong hypotheses. A risk register names each risk, its likelihood, its impact and the mitigation.

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Partner withdraws access to responders. | Medium | High | Recruit from two organizations; design simulations that need no partner data. |
| Recruitment shortfall (experienced responders are busy). | High | High | Short sessions; scheduled around shifts; remote participation; power planned for a realistic sample (Chapter 4). |
| Scenarios unrealistic. | Medium | High | Build from synthetic cases reviewed by practitioners; pilot realism ratings. |
| Rater availability. | Medium | Medium | Train three raters; two per item; third for adjudication. |
| Ethics review delay. | Medium | Medium | Submit early; staged approval for pilot. |
| Results unfavorable to partner. | Medium | Medium | Publication rights agreed before data collection (Chapter 1 §1.3.4). |

*In plain terms:* The main risks are practical (recruitment, data access, rater time), and each has a named mitigation that can be checked during the pilot.

### 3.8 Evaluation criteria for the contribution

State how a committee should judge the thesis, regardless of the direction of results:

1. Was the baseline reproduced and the procedure piloted with measured rater agreement (Chapter 4)?
2. Did the main study test H1–H3 as preregistered, with deviations logged (Chapter 5)?
3. Was the effect, or its absence, tested in a second context (Chapter 6)?
4. Did the claims survive or get narrowed by adversarial critique (Chapter 7)?
5. Are the artifacts (SHA, codebook, scenarios, analysis code, synthetic data) available at the tiers promised (Chapter 8)?

A proposal that commits to these criteria makes a negative result publishable and useful.

### 3.9 Worked example: from gap statement to proposal summary

*Synthetic.* The candidate writes a one-page proposal summary:

> **Title.** Structured handoffs and decision errors under incomplete telemetry: a preregistered simulation study.
>
> **Contribution type.** Empirical and artifact, with a theory test (error-type pattern).
>
> **Problem.** Context is reported to be lost when incidents change hands (qualitative evidence only), and missing telemetry invites absence-of-evidence errors (§1.2.3). No study in our documented search compares handoff formats on decision correctness.
>
> **Mechanism.** SHA transmits ruled-out hypotheses, telemetry gaps and expectations, which should reduce comprehension and projection errors but not perception errors.
>
> **Design.** Within-subject simulation; three conditions (Standard, Attention-control, SHA); six synthetic scenarios seeded from the Harbor Library, Cedar Training Network and Lumen Library Reservations cases; standardized handoffs written by trained senders; counterbalanced order; blinded raters.
>
> **Hypotheses.** H1, H2, H3 as in §3.3. SEOI 0.5 errors per scenario. Non-inferiority margin for time stated in protocol.
>
> **Failure conditions.** F1–F6.
>
> **Ethics.** Participants are consenting professionals working only on synthetic material; no incident records are used; consent addresses voluntary participation and non-disclosure of individual performance to employers.
>
> **Artifacts.** SHA template, scenarios, codebook, analysis code and anonymized decision data released under tiers T0–T2 and, if consent permits, de-identified T3.

The summary fits on one page and every element maps to a section of the full protocol.

### 3.10 Practical activity: mechanism stress test

Take your own proposed mechanism and attempt to break it in writing, in three passes:

1. **Premise pass.** For each link in the chain, state the evidence for it and its ladder level. Mark any link supported only by intuition.
2. **Pattern pass.** Write down at least one outcome the mechanism predicts should *not* change. If you cannot, the mechanism is not yet specific enough.
3. **Rival pass.** For each rival explanation, write what result would favor it over your mechanism, and confirm your design can observe that result.

Record the stress test in the protocol appendix; reviewers value seeing that the researcher attacked their own idea first.

### 3.11 Drawing the causal model before choosing measures

The mechanism chain in §3.2 is a narrative. Before data collection, it is worth translating it into a simple causal diagram: nodes for variables, arrows for assumed direct causal influence. No special software or notation is needed; the value lies in forcing every assumption into the open. For the Handoff Study, a minimal diagram contains:

- **Handoff format** (Standard or SHA) → **content transmitted** (hypotheses, ruled-out items, gaps, expectations) → **receiver comprehension and projection** → **decision quality**.
- **Receiver experience** → comprehension and projection, and → decision quality directly (experts may compensate for poor handoffs).
- **Telemetry completeness of the scenario** → comprehension and projection (gaps make understanding harder) and → the *value* of transmitted gap information (an effect modifier).
- **Sender effort and time available** → content transmitted (a rushed sender transmits less in either format).
- **Scenario difficulty** → decision quality.

Three design consequences follow from drawing it.

1. **Which variables must be controlled by design.** Scenario difficulty affects the outcome but not the format; balancing scenarios across conditions (§5.2) removes it as a confound. Sender effort affects content in both arms; if the SHA takes longer to write, a study that gives senders unlimited time measures the SHA under unrealistic conditions. The protocol must fix the sender's time budget equal across arms.
2. **Which variables are mediators and must not be "adjusted away."** Content transmitted lies on the causal path. Adjusting the primary analysis for the number of fields completed would remove part of the effect the study is trying to estimate. Mediators belong in a separate, labeled mechanism analysis.
3. **Which variables are moderators to pre-specify.** Experience and telemetry completeness are candidates. Pre-specifying them, with predicted directions, turns post-hoc subgroup hunting into a test.

The diagram also exposes what the study cannot learn. Nothing in it represents the organizational pressures discussed in §2.9.5. That omission is acceptable for a simulation study but must appear in the limitations as a boundary on the claim.

### 3.12 Construct validity of "decision quality"

The primary outcome is only as credible as the argument that it measures what the thesis says it measures. A construct-validity argument for rater-scored decision errors has several strands, each of which can be planned in the proposal.

- **Content.** The defensible-option sets for each decision point come from an expert panel. Document who the experts are (role, years of practice, sector), how disagreements were resolved, and how many decision points were dropped because experts could not agree. Dropped points are informative: they mark where "correct" is genuinely contested.
- **Response process.** Do raters score what the rubric intends? Think-aloud sessions with two raters scoring a sample of decisions can reveal rubric ambiguities before the main study.
- **Internal structure.** If comprehension and projection errors are distinct constructs, they should not be perfectly correlated, and the study's mechanism claim requires that they be scored separately with acceptable agreement for each.
- **Relations to other variables.** Error counts should be higher for novices than experts and higher in scenarios with more telemetry gaps. If they are not, either the measure or the scenarios are suspect. These are **known-groups** checks and can be run in the pilot.
- **Consequences.** If decision-error scores were ever used for performance evaluation of real responders, the incentive to game them would change their meaning. The thesis should state that its scores are research instruments, not personnel measures.

### 3.13 Justifying the smallest effect of interest

Section 3.3 introduced the smallest effect of interest (SEOI). Doctoral committees increasingly ask *why* that value. [Lakens (2022)](https://doi.org/10.1525/collabra.33267) discussed several approaches to justifying sample size, among them planning for a smallest effect of interest, accepting a sample size fixed by resource constraints and reporting the resulting precision honestly, and using heuristics; he cautioned against unjustified conventions. Applying that discussion to the Handoff Study suggests four defensible justifications, which can be combined:

1. **Practitioner elicitation.** Ask several experienced incident leads how large a reduction in misread situations would make them adopt a new handoff format, given its cost in sender time. Record the elicitation protocol and the spread of answers, not only the median.
2. **Cost–benefit anchoring.** If the SHA adds two minutes per handoff, how many errors must it prevent per handoff to be worth the time? Even rough numbers make the SEOI an argument rather than a guess.
3. **Measurement resolution.** An effect smaller than the scoring instrument can reliably detect (given rater disagreement) is not a meaningful target.
4. **Resource-bounded precision.** If only a fixed number of qualified participants can be recruited, state the precision that sample buys and accept that some true effects of practical interest may not be distinguishable from zero.

The SEOI also defines what counts as "no meaningful effect." With an SEOI declared, the study can use **equivalence testing**: [Lakens (2017)](https://doi.org/10.1177/1948550617697177) presented a practical introduction to the two one-sided tests (TOST) procedure, which asks whether the effect is reliably smaller than the bounds set by the SEOI. Without equivalence logic, a null result can only be called "not significant," which is uninformative. Chapter 5 applies TOST to the safety outcome.

### 3.14 Designing to discriminate between rival theories

Section 2.3.6 argued that the best studies test points where theories disagree. The proposal should show concretely how the Handoff Study does this. Using the deeper reading of Chapter 2 §2.9:

| Rival account | Distinctive prediction | Design element that tests it | Outcome that would favor it |
|---|---|---|---|
| Situation awareness (mechanism of record) | SHA reduces comprehension and projection errors more than perception errors | Separate scoring of perception vs. comprehension/projection | Effect concentrated in comprehension/projection |
| "More information" account | SHA helps only because it transmits more facts | Word-count-matched Standard condition, or adjustment in a labeled mechanism analysis | Effect vanishes when amount of information is equated |
| Naturalistic decision-making | Experts benefit through the expectations field; novices benefit less or differently | Pre-specified experience moderator; field-level usage logging | Expert advantage tied to expectations-field use |
| Kahneman–Klein conditions | Larger effect where feedback is poor | Scenarios classified a priori by feedback quality | Interaction with feedback class |
| Sensemaking | Role ambiguity is a separate pathway | Optional decision-authority field in a factorial extension | Fewer omission errors independent of comprehension change |
| Sociotechnical | Effect depends on organizational fit | Second context (Chapter 6) | Effect varies with context features |

*In plain terms:* Each row names a competing explanation, what it alone predicts, and the piece of the design that can tell it apart from the others. A result that fits only the first row supports the mechanism; a result that fits the second row means the template's structure did not matter.

The word-count-matched condition deserves comment because it is the cheapest and most often omitted control. If SHA handoffs are on average 40% longer than free-text handoffs, any benefit could be due to length. Instructing Standard-condition senders to write handoffs of similar length, or comparing within length bands, separates "structure" from "more words." Omitting the control does not invalidate the study, but it limits the claim to "the SHA as typically written," not "the SHA's structure."

### 3.15 Extensions the proposal should anticipate but not promise

A proposal earns credibility by being narrow. Still, a committee will ask where the work leads. Two extensions follow naturally from Chapter 2 and should appear as clearly labeled future directions, with their own risks.

**Cross-organizational handoffs.** Coordination research ([Comfort, 2007](https://doi.org/10.1111/j.1540-6210.2007.00827.x); [Bigley and Roberts, 2001](https://doi.org/10.2307/3069401)) locates many crisis failures at organizational boundaries. Extending the SHA to handoffs between a victim organization and an external responder introduces new variables: information withheld for legal reasons, TLP markings, differing vocabularies, and divergent incentives. The mechanism may be the same; the confounds multiply. Recruitment requires two cooperating organizations per dyad, which makes the sample far harder to obtain.

**Model-assisted handoffs.** A summarization model could draft the SHA from tickets and chat. The reliance literature (§2.11) predicts both benefits (completeness) and risks (unchecked errors). An extension study would need seeded errors and stratified reporting by model correctness. Its ethics review must address the processing of incident communications by a model, including where the model runs and whether inputs are retained — a data-protection question as much as a research-design one.

Labeling these as future work is not modesty for its own sake: it prevents scope creep from weakening the core study and gives the defense (Chapter 8) a ready answer to "what next?"

### 3.16 Defending the proposal

The proposal defense or qualifying review tests whether the candidate understands their own design. Prepare short, evidence-based answers to the questions most likely to be asked:

1. *Why simulation rather than real incidents?* Because real incidents cannot be randomized, their decision quality cannot be judged blind to outcome, and access to raw decision records is rarely granted. Simulation buys internal validity at the price of ecological validity, and Chapter 6 partially repays that price.
2. *Why should practitioners care about rater scores?* Because the scores are anchored to defensible-option sets elicited from practitioners and validated by known-groups checks (§3.12).
3. *What if the effect is null?* Then equivalence testing against the SEOI (§3.13) tells whether the SHA is practically useless or the study was too imprecise; both are reportable results with pre-declared consequences (§3.6).
4. *What if experts and novices differ?* That is a pre-specified moderator with a theory-based prediction (§3.14), not a post-hoc rescue.
5. *What is the contribution if the mechanism is wrong but the effect is real?* An empirical contribution with a narrowed theoretical claim; the failure conditions in §3.6 say so in advance.

Writing these answers before data collection often reveals design gaps that are still cheap to fix.

### Common errors and limits

- Proposing an artifact and measuring only satisfaction.
- A mechanism that predicts improvement everywhere, so no pattern could count against it.
- A "no intervention" baseline when practitioners already do something.
- Omitting an attention-control condition when effort is a plausible explanation.
- Choosing the smallest effect of interest to fit the available sample.
- Failure conditions that lead to no change in claims.
- Limit: the SHA, scenarios and premises in this chapter are synthetic teaching material; their real-world plausibility must be checked by pilot work and practitioner review.

### Exercises — chapter 3

**EX015 — Contribution typing.** *Objective:* match claims to evidence. *Inputs:* four synthetic thesis claims: (a) "We release an open-source playbook engine"; (b) "Our scoring rubric for containment decisions is reliable"; (c) "Responders rely on intuition more for familiar incident types"; (d) "Our playbook engine reduces containment errors." *Constraints:* use §3.1. *Steps:* type each claim; state the minimum evidence needed; identify one claim that is really two. *Expected evidence:* table. *Rubric:* 3 = correct types, appropriate evidence, (a)/(d) relationship noted; 2 = one error; 1 = generic evidence; 0 = none.

**EX016 — Mechanism specification.** *Objective:* write a pattern-predicting mechanism. *Inputs:* an intervention of your choice (e.g., an automated timeline view, a pairing policy for night shifts). *Constraints:* at least four links; at least one predicted non-effect. *Steps:* write the chain; attach evidence level to each link; state the non-effect. *Expected evidence:* mechanism chain and justification. *Rubric:* 3 = specific chain with testable non-effect and honest evidence levels; 2 = non-effect weak; 1 = no pattern; 0 = none.

**EX017 — Hypotheses and SEOI.** *Objective:* operationalize hypotheses. *Inputs:* your EX016 mechanism. *Constraints:* one primary, one mechanism-pattern and one safety or non-inferiority hypothesis; a justified SEOI. *Steps:* write hypotheses with population, condition, comparison, outcome, direction; define outcomes operationally; justify SEOI by consequence. *Expected evidence:* hypotheses block. *Rubric:* 3 = complete, operational, SEOI justified by practice; 2 = one element vague; 1 = SEOI arbitrary; 0 = none.

**EX018 — Baseline critique.** *Objective:* detect weak baselines. *Inputs:* a synthetic design: "We compared our AI-generated incident summary with no summary, using 20 student volunteers; the AI group answered more scenario questions correctly." *Constraints:* propose at least two improved comparison conditions. *Steps:* identify baseline problems; propose Standard and Active-control conditions; state which rival each addresses. *Expected evidence:* critique and redesign. *Rubric:* 3 = identifies no-summary straw man, population mismatch, effort/length confound; proposes human-written summary and length-matched control; 2 = one missed; 1 = superficial; 0 = none.

**EX019 — Rival-explanation table.** *Objective:* design against alternatives. *Inputs:* your EX016–EX017 work. *Constraints:* at least six rivals. *Steps:* build a table like §3.5. *Expected evidence:* table. *Rubric:* 3 = six or more plausible rivals with concrete design features; 2 = four or five; 1 = generic; 0 = none.

**EX020 — Failure conditions and risk register.** *Objective:* make the contribution falsifiable in practice. *Inputs:* your proposal. *Constraints:* at least five failure conditions with consequences; at least five risks. *Steps:* write both tables; check that each failure condition narrows a specific claim. *Expected evidence:* two tables. *Rubric:* 3 = each condition maps to a claim change, risks have mitigations; 2 = one or two conditions lack consequence; 1 = vague; 0 = none.

### Chapter synthesis

A strong proposal states a mechanism that predicts a pattern, tests it against a realistic baseline and an active control, lists rival explanations with design features that separate them, sets a smallest effect of interest by practical consequence, and predeclares what results would narrow or refute the claim. The Handoff Study now has hypotheses H1–H3, three conditions and failure conditions F1–F6. Chapter 4 asks whether its baselines can be reproduced and its procedure works before the main study is run.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 08

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Replication of baselines and pilot protocol

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Attempt to reproduce a published baseline, document every discrepancy and diagnose its cause before claiming improvement.
2. Recognize dataset shift — covariate, label and concept shift — and temporal leakage in incident-response datasets and benchmarks.
3. Plan sample size from the smallest effect of interest, using a transparent calculation and a sensitivity range.
4. Design a pilot study whose purpose is feasibility, not effect estimation, with predeclared progression criteria.
5. Make computational work reproducible: versioned data, pinned environment, recorded seeds, hashes and a run log.

Chapter 3 proposed the Handoff Study and stated failure conditions F1 and F2, which depend on pilot results. This chapter tests the ground under the main study: are the baselines what we think they are, and does the procedure work? Chapter 5 runs the main study only if the pilot's progression criteria are met.

### 4.1 Why replicate a baseline first

A claim of improvement is a claim about a *difference*. If the baseline is wrong, the difference is meaningless. Baselines go wrong in incident-response research for ordinary reasons: a benchmark has several versions; an evaluation script differs from the one described; a split was random in the code but described as temporal; labels were corrected after publication; preprocessing silently dropped rows. [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) list *inappropriate baselines* and *data snooping* among the pitfalls they found widespread in security papers using machine learning, and [Pendlebury et al. (2019)](https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury) showed that time splits which would be impossible in deployment inflated published malware-classification results.

Using the definitions adopted in Chapter 1 from the [National Academies (2019)](https://www.nationalacademies.org/read/25303/chapter/3), reproducing a baseline is a *reproducibility* exercise (same data, code and conditions) when the original artifacts are available, and becomes a *replication* when you must re-collect data. In either case, the goal is not to embarrass the original authors but to establish the reference point for your own claim.

### 4.2 A reproduction procedure

1. **Freeze the target.** Record the exact numbers, tables and conditions you intend to reproduce, with page or table references.
2. **Obtain artifacts.** Data (with version identifier and hash), code (with commit), environment, splits, seeds, preprocessing steps. List what is missing.
3. **Run as published.** Make no improvements yet. Record environment details and all outputs.
4. **Compare.** For each target number, record reproduced value, difference and whether it lies within a tolerance you set *before* running.
5. **Diagnose discrepancies** systematically: data version, split, preprocessing, metric definition (micro vs. macro averaging, label set), randomness, software versions, hardware nondeterminism.
6. **Contact authors** with a precise, courteous description if a discrepancy remains. Record the exchange.
7. **Report** the reproduction honestly, including what could not be reproduced, and choose your comparison point: the reproduced value under documented conditions, not the published number.

A **reproduction log** captures each step with timestamps and decisions. It belongs in the thesis archive (Chapter 8).

### 4.3 Dataset shift and temporal leakage

Incident data change over time: adversaries adapt, organizations deploy new tools, taxonomies are revised and analysts relabel. Three kinds of shift matter:

- **Covariate shift**: the distribution of inputs changes (new log sources, new alert types) while the relation between input and label is stable.
- **Label shift**: class proportions change (a phishing wave raises the share of phishing cases), changing base rates and thus positive predictive value (Chapter 1 §1.6.5).
- **Concept shift (drift)**: the relation between inputs and labels changes (the same alert pattern now indicates a different activity, or a label definition changes).

**Temporal leakage** occurs when information from the future enters training or tuning: a random split that puts later incidents in training and earlier ones in testing; features computed with knowledge available only after the incident; or labels revised using hindsight. The deployment-faithful rule is simple: *train only on what would have been available at the time of each prediction*.

Human-study analogues exist. A scenario set calibrated on responders who later serve as participants leaks information; a codebook revised after seeing main-study decisions leaks outcome knowledge into measurement. Treat these with the same rule: freeze instruments before the data they will evaluate.

### 4.4 Power and sample size

**Statistical power** is the probability that a study detects an effect of a given size if it exists. Underpowered studies waste participants' time, produce unstable estimates and, when combined with selective publication, inflate published effect sizes (Chapter 1 §1.3.1). [Cohen (1992)](https://doi.org/10.1037/0033-2909.112.1.155) provided a widely used primer on power analysis for common tests.

For a within-subject comparison like the Handoff Study's (each participant experiences both SHA and Standard), a normal-approximation sample size for a two-sided paired test is

n ≈ ((z₁₋α/₂ + z₁₋β) · σ_d / δ)²

where δ is the smallest effect of interest (Chapter 3 §3.3), σ_d is the standard deviation of within-participant differences, α is the two-sided significance level and 1 − β is the power. The difficult input is σ_d: it must come from prior data or a pilot, and it is uncertain. The defensible practice is to report a **sensitivity range** — required n across plausible σ_d values — and to plan for the pessimistic end. With small samples a *t*-based calculation or simulation is more accurate than the normal approximation; the approximation is used here for transparency.

Precision can replace power as the planning target: plan n so that the expected confidence-interval half-width is smaller than the SEOI. This aligns with Chapter 3's goal of making a null result informative.

### 4.5 Pilot studies: feasibility, not effect

A pilot asks whether the main study *can be done as designed*, not whether the intervention works. Effect estimates from small pilots are too imprecise to justify or cancel a main study and invite selective decisions. Pilot objectives for the Handoff Study:

| Objective | Measure | Progression criterion (predeclared) |
|---|---|---|
| Recruitment | Eligible responders consenting per month. | ≥ the rate needed to reach planned n within the program timeline. |
| Session completion | Proportion completing all scenarios. | ≥ 90%. |
| Scenario realism | Participant realism ratings; practitioner review comments. | Median rating at or above the protocol's threshold; no scenario flagged as implausible by two or more reviewers. |
| Rater agreement (F1) | Cohen's kappa on error type. | ≥ protocol target; otherwise revise codebook and repeat. |
| Mechanism premise (F2) | Proportion of Standard handoffs that already contain ruled-out hypotheses and telemetry gaps. | Below a protocol threshold; otherwise SHA has nothing to add. |
| Variance estimate | σ_d of error counts. | Used to update sample size; not used to estimate the effect. |
| Procedure fidelity | Senders' handoffs match condition specifications. | All deviations corrected before main study. |

*In plain terms:* A pilot tests whether the study can be run, not whether the intervention works; each objective has a threshold, decided in advance, that says proceed, amend or stop.

The outcome of a pilot is one of three decisions: **proceed** (all criteria met), **proceed with amendments** (fixable problems, documented as protocol revisions before the main study) or **stop or redesign** (a premise failed). Pilot participants should normally not be reused in the main study, because they have learned the scenarios.

### 4.6 Worked example: a synthetic benchmark whose published baseline cannot initially be reproduced

*OpenTriage-S and its paper are synthetic.* A (fictional) paper introduces OpenTriage-S, a benchmark of 20 triage cases across nine months, and reports a "source-majority" baseline — predict the most common label seen for each alert source in training — with accuracy **0.833** on its test split. The Handoff Study candidate wants to use OpenTriage-S to check a triage component and must first reproduce that number.

**Attempt 1.** The candidate downloads the current release (labels v1.1), uses the test-case list printed in the paper's appendix and obtains **0.667**. The discrepancy exceeds the preregistered tolerance of ±0.02.

**Diagnosis.** The repository's changelog shows that v1.1 corrected three labels (T05, T08 and T09) after community review. The paper used v1.0. Re-running on v1.0 reproduces **0.833** exactly. The baseline is reproducible — but only on labels now known to contain errors.

**A second problem.** Inspecting the published split reveals that the training set includes cases from months 7–9 while the test set includes cases from months 1–6: the split is not time-respecting. In particular, the source "vpn" is assigned the label "account" because "account" cases appear only in months 7–9 — information that would not have existed when early cases were triaged. Under a time-respecting split (train months 1–6, test months 7–9) with corrected labels, accuracy falls to **0.375**, partly because the label "account" never appears in training at all — a case of concept shift that the published split hid.

The offline script below reproduces all three numbers and also computes paired-design sample sizes for the Handoff Study's SEOI under two variance assumptions.

```python
"""Chapter 4 offline lab. OpenTriage-S is a synthetic benchmark invented for this book."""
from collections import Counter, defaultdict
from statistics import NormalDist

# case_id, month, source, label_v1_0, label_v1_1
CASES = [
    ("T01", 1, "mail", "phish", "phish"), ("T02", 1, "edr", "malware", "malware"),
    ("T03", 2, "mail", "phish", "phish"), ("T04", 2, "vpn", "benign", "benign"),
    ("T05", 3, "mail", "phish", "benign"), ("T06", 3, "edr", "malware", "malware"),
    ("T07", 4, "vpn", "benign", "benign"), ("T08", 4, "mail", "phish", "benign"),
    ("T09", 5, "edr", "malware", "benign"), ("T10", 5, "vpn", "benign", "benign"),
    ("T11", 6, "mail", "phish", "phish"), ("T12", 6, "edr", "malware", "malware"),
    ("T13", 7, "vpn", "account", "account"), ("T14", 7, "mail", "phish", "phish"),
    ("T15", 8, "vpn", "account", "account"), ("T16", 8, "edr", "malware", "malware"),
    ("T17", 9, "vpn", "account", "account"), ("T18", 9, "mail", "benign", "benign"),
    ("T19", 9, "vpn", "account", "account"), ("T20", 9, "edr", "malware", "malware"),
]
PUBLISHED_TEST = {"T02", "T04", "T08", "T11", "T16", "T20"}  # split listed in the (synthetic) paper

def fit(train, label_idx):
    by_src = defaultdict(Counter)
    for c in train:
        by_src[c[2]][c[label_idx]] += 1
    return {s: cnt.most_common(1)[0][0] for s, cnt in by_src.items()}

def accuracy(model, test, label_idx):
    return sum(model.get(c[2]) == c[label_idx] for c in test) / len(test)

def run(name, train, test, label_idx):
    m = fit(train, label_idx)
    print(f"{name:34s} n_test={len(test):2d} acc={accuracy(m, test, label_idx):.3f}")

def paired_n(delta, sd_diff, alpha=0.05, power=0.80):
    z = NormalDist().inv_cdf
    return ((z(1 - alpha / 2) + z(power)) * sd_diff / delta) ** 2

if __name__ == "__main__":
    pub_train = [c for c in CASES if c[0] not in PUBLISHED_TEST]
    pub_test = [c for c in CASES if c[0] in PUBLISHED_TEST]
    run("published split, labels v1.0", pub_train, pub_test, 3)
    run("published split, labels v1.1", pub_train, pub_test, 4)
    t_train = [c for c in CASES if c[1] <= 6]
    t_test = [c for c in CASES if c[1] >= 7]
    run("time split (m1-6 / m7-9), v1.1", t_train, t_test, 4)
    print("unseen test labels in time split:", sorted({c[4] for c in t_test} - {c[4] for c in t_train}))
    for sd in (1.0, 1.5):
        print(f"paired n for delta=0.5, sd_diff={sd}: {paired_n(0.5, sd):.1f}")
```

Expected output (verified with Python 3):

```text
published split, labels v1.0       n_test= 6 acc=0.833
published split, labels v1.1       n_test= 6 acc=0.667
time split (m1-6 / m7-9), v1.1     n_test= 8 acc=0.375
unseen test labels in time split: ['account']
paired n for delta=0.5, sd_diff=1.0: 31.4
paired n for delta=0.5, sd_diff=1.5: 70.6
```

**What the candidate reports.** "We reproduced the published OpenTriage-S baseline (0.833) using label version 1.0 and the published split. With corrected labels (v1.1) the same baseline scores 0.667. The published split is not time-respecting; under a time-respecting split with v1.1 labels the baseline scores 0.375, and one test label is absent from training. We use the time-respecting v1.1 configuration as our reference and report the others for comparability." This paragraph is more valuable to the field than a claim of beating 0.833.

**Sample size.** With δ = 0.5 errors per scenario, α = 0.05 and 80% power, the approximation requires about 32 participants if σ_d = 1.0 and about 71 if σ_d = 1.5. The pilot's variance estimate will choose between these; the candidate plans recruitment for the pessimistic case and reports the sensitivity range in the protocol.

### 4.7 Making the computation reproducible

Minimum practice for every analysis in a thesis:

| Element | Practice |
|---|---|
| Data versions | Record dataset name, version and a cryptographic hash of each input file. |
| Code | Version control with tagged commits for every reported result. |
| Environment | Record interpreter and library versions; provide a lock file or container specification. |
| Randomness | Fix and record seeds; report variability across seeds for stochastic methods. |
| Run log | For each reported number: command, commit, data hash, environment, timestamp (with zone), output file. |
| Separation | Keep raw, intermediate and derived data in separate locations; never overwrite raw inputs (the [technical book](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md#ch-12) treats the operational version of this rule). |

*In plain terms:* Reproducibility is a set of small habits — pinned versions, fixed seeds, recorded hashes, one command to rerun — each cheap at the start and expensive to retrofit.

### 4.8 Practical activity: write the pilot report

After a pilot, write a short report with: objectives and criteria (copied from the protocol), results for each criterion, decision (proceed / amend / stop), list of protocol amendments with version numbers, and the updated sample-size calculation. The report is dated before the main study begins, establishing that amendments were made before main-study data existed.

For the SHA study, the report would state whether pilot rater agreement on error type met the protocol target (failure condition F1) and whether free-text handoffs already carried ruled-out hypotheses and telemetry gaps (F2). Either failure leads to amend or stop, never to a quiet start of the main study.

### 4.9 Reproducibility as a spectrum, not a badge

[Peng (2011)](https://doi.org/10.1126/science.1213847) described reproducibility in computational science as a spectrum running from publication alone, through publication with code, code and data, and finally linked and executable code and data, with full replication as the gold standard beyond it. The spectrum framing is useful for incident-response research because the field's constraints (Chapter 1 §1.4) often make the top of the spectrum unreachable for real data. A thesis can still state where on the spectrum each artifact sits and why, which is more informative than a binary "available / not available" statement.

[Sandve et al. (2013)](https://doi.org/10.1371/journal.pcbi.1003285) offered ten simple rules for reproducible computational research. Several translate directly into the baseline-reproduction step of an incident-response thesis:

- **Record how every result was produced.** For a baseline, this includes the exact dataset version, the split, the preprocessing, the model configuration and the random seeds — not only the code repository URL.
- **Avoid manual data manipulation steps.** Hand-editing a label file "to fix obvious errors" is a manual step that nobody can reproduce. If labels must be corrected, write the correction as code with a reason for each change, as the Chapter 4 lab does with the label-version difference.
- **Archive the exact versions of external programs.** Security tooling changes quickly; a parser update can change extracted features.
- **Version-control custom scripts.**
- **Record intermediate results** in standardized formats where possible, so that a discrepancy can be localized to a stage.
- **Note the underlying random seeds** for analyses that include randomness.
- **Store raw data behind plots**, and generate hierarchical analysis output so that summary numbers can be traced to their inputs.
- **Connect textual statements to underlying results**, so that every number in the thesis can be traced to code output.
- **Provide public access** to scripts, runs and results where constraints allow.

The last rule is where incident data usually stops. The answer is not to abandon the others: a fully scripted pipeline on restricted data, with a synthetic fixture that exercises the same code, still lets a reviewer check the computation even if they cannot check the inputs.

### 4.10 Leakage in incident data: a working taxonomy

[Kapoor and Narayanan (2023)](https://doi.org/10.1016/j.patter.2023.100804) reviewed published reports of data leakage across scientific fields using machine learning and argued that leakage is a widespread cause of overoptimistic, irreproducible results. They proposed a taxonomy distinguishing, among other things, lack of a clean separation of training and test data, use of features that would not be legitimately available at prediction time, and test data drawn from a distribution different from the one the scientific claim concerns, and they proposed "model info sheets" for documenting how leakage was ruled out. Their taxonomy maps onto incident data with some security-specific instances:

| Leakage form | Incident-data instance | Detection check |
|---|---|---|
| No clean train–test separation | The same incident appears as several alerts, some in each split | Group splits by incident identifier, not alert identifier |
| Duplicates | Near-identical phishing emails or scanner alerts across splits | Hash or fuzzy-match content across splits before training |
| Temporal | Training on months after the test period | Enforce a time cut; report performance by month |
| Illegitimate features | Ticket fields filled in after disposition (e.g., "closure category") used as inputs | For each feature, record when in the workflow it is populated |
| Label from the future | Labels revised after later investigation, used as if known at triage | Keep label version history; evaluate against the label available at decision time and the later "truth" separately |
| Sampling bias in test set | Test cases selected because they were well-documented (often the escalated ones) | Compare test-set composition to the full case population |

*In plain terms:* Leakage means the model saw, directly or indirectly, information it would not have when making a real decision. Each row is a common way this happens with incident data, and the last column is the check that catches it.

The "label from the future" row deserves emphasis because it is easy to miss and because it bears on decision quality. A triage decision judged against a label assigned weeks later, after forensic analysis, conflates two questions: was the decision right given what was known, and was the case ultimately malicious? The Handoff Study's decision-point design (Chapter 5 §5.1) separates them for human decisions; baseline replications of automated triage should do the same for model decisions.

### 4.11 Documenting a baseline: datasheets and model cards

When a baseline is reproduced, the reproduction itself becomes an artifact that others will rely on. Two documentation formats from machine-learning research are useful templates. [Gebru et al. (2021)](https://doi.org/10.1145/3458723) proposed **datasheets for datasets**, which document a dataset's motivation, composition, collection process, preprocessing, uses, distribution and maintenance. [Mitchell et al. (2019)](https://doi.org/10.1145/3287560.3287596) proposed **model cards**, which document a trained model's intended use, the factors relevant to its performance, its metrics, evaluation data, training data, quantitative analyses, ethical considerations, and caveats.

Adapted to an incident-response baseline, the minimum documentation answers:

1. **Collection context.** Which organization(s), sector, period, and detection pipeline produced the cases? What was *not* collected (e.g., cases closed without tickets)?
2. **Labeling.** Who assigned labels, with what guidance, at what point in the workflow, and how often were labels revised? What is the inter-rater agreement, if measured?
3. **Known shifts.** Which events during the collection period changed the data-generating process — tooling changes, staffing changes, policy changes, large campaigns?
4. **Intended use and misuse.** For which decisions is the baseline intended to serve as a comparison? For which would it mislead?
5. **Performance by factor.** Results broken down by month, source, and case type, not only aggregated.

The OpenTriage-S worked example in §4.6 is synthetic, but the reproduction log learners write for EX021 and EX026 should follow this structure.

### 4.12 What pilots can and cannot tell you

Section 4.5 stated that pilots establish feasibility rather than effect. The reason deserves a precise statement, because candidates under time pressure are tempted to use a pilot's effect estimate to set the main study's sample size.

A pilot with, say, eight participants yields an effect estimate with a very wide interval. If the main study is powered on that point estimate, two problems follow. When the pilot happened to produce a large estimate, the main study will be underpowered for the true, smaller effect. When the pilot happened to produce a small estimate, the study may be abandoned although a meaningful effect exists. In both cases the decision is driven by noise. The SEOI-based justification of §3.13 avoids this: the main study is sized to detect the smallest effect worth knowing about, regardless of what the pilot estimated.

What pilots *can* estimate usefully:

- **Variability of the outcome** (the standard deviation of within-participant differences), with caution, because small samples estimate variance imprecisely too; a conservative choice is to plan with a value toward the upper end of plausible estimates.
- **Rater agreement** for each scored construct, which determines whether the outcome measure is usable.
- **Completion rates, timing and dropout**, which determine recruitment targets.
- **Protocol failures**: facilitator hints, scenario ambiguities, materials that reveal condition, and technical breakdowns.
- **Floor and ceiling effects**: if almost everyone makes zero errors in a scenario, that scenario cannot show an effect.

A pilot report that states "the pilot showed a promising effect" is a warning sign. A pilot report that states "the pilot showed the procedure is feasible, rater agreement for comprehension errors met the predeclared threshold, one scenario showed a ceiling effect and was replaced" is what a committee wants to read.

### 4.13 Replicating the human baseline, not only the model

Incident-response theses frequently compare a new aid with "current practice." Current practice is itself a baseline that needs replication. In the Handoff Study, the Standard condition stands in for free-text handoffs as practiced. Three checks establish that it is a fair baseline:

1. **Ecological check.** Collect a small sample of real, de-identified free-text handoffs (with permission) and compare their length and content categories with Standard-condition handoffs written in the simulation. If simulation handoffs are far shorter or omit categories that real ones contain, the baseline is a straw man.
2. **Effort check.** Senders in the Standard condition should receive the same time and the same instructions to be complete as SHA senders. A baseline written hastily inflates the comparison.
3. **Expert endorsement.** Ask practitioners whether Standard-condition handoffs look like what they receive. Record disagreement.

The general principle, shared with the reproduction of computational baselines, is that a comparison is only as informative as the weakest condition is honest.

### Common errors and limits

- Comparing against a published number without reproducing it under your conditions.
- "Fixing" a baseline during reproduction, so the comparison is no longer to the published method.
- Random splits for time-ordered incident data.
- Treating a pilot's effect estimate as evidence for or against the intervention.
- Choosing σ_d optimistically to make the required sample feasible.
- Reusing pilot participants in the main study.
- Limit: the normal approximation underestimates n for small samples; use a *t*-based calculation or simulation for final planning.

### Exercises — chapter 4

**EX021 — Reproduction log.** *Objective:* document a reproduction attempt. *Inputs:* the script in §4.6. *Constraints:* run offline; set tolerance ±0.02 before running. *Steps:* (1) record target (0.833); (2) run with v1.1 labels first and record the discrepancy; (3) diagnose using the case data; (4) run with v1.0; (5) write the log entry with environment details. *Expected evidence:* reproduction log. *Rubric:* 3 = exact outputs, label-version diagnosis, environment recorded, tolerance predeclared; 2 = one element missing; 1 = no diagnosis; 0 = not run.

**EX022 — Leakage audit.** *Objective:* detect temporal leakage. *Inputs:* the OpenTriage-S cases and published split. *Constraints:* identify specific case IDs. *Steps:* list test cases that occur earlier than some training cases; show which learned rule depends on future data; state the deployment-faithful split. *Expected evidence:* audit table and explanation. *Rubric:* 3 = identifies vpn→account learned from months 7–9 and its effect on T04, proposes time split; 2 = identifies leakage but not mechanism; 1 = vague; 0 = none.

**EX023 — Shift classification.** *Objective:* distinguish shift types. *Inputs:* (a) a SOC adds cloud audit logs in month 7; (b) a phishing wave triples phishing share in month 8; (c) the CSIRT redefines "account compromise" to include token theft in month 7; (d) OpenTriage-S's "account" label appears only after month 6. *Constraints:* one type per item with justification; consequence for evaluation. *Steps:* (1) for each scenario, compare training and evaluation distributions of inputs and labels; (2) classify the shift (covariate, label, concept or none); (3) state the consequence for the baseline estimate. *Expected evidence:* four paragraphs. *Rubric:* 3 = (a) covariate, (b) label shift, (c) concept shift, (d) concept/label emergence with justification; 2 = one error; 1 = two errors; 0 = none.

**EX024 — Sample-size sensitivity.** *Objective:* plan n transparently. *Inputs:* the `paired_n` function. *Constraints:* offline. *Steps:* compute n for δ = 0.5 with σ_d = 1.2; for δ = 0.25 with σ_d = 1.0; and for δ = 0.5, σ_d = 1.0 at 90% power; write a 120-word recommendation. *Expected evidence:* values and recommendation. *Rubric:* 3 = values correct to one decimal, recommendation plans for pessimistic case and notes approximation limits; 2 = values correct, recommendation thin; 1 = one value wrong; 0 = none.

**EX025 — Pilot criteria.** *Objective:* design feasibility criteria. *Inputs:* the Handoff Study and §4.5. *Constraints:* at least six criteria; at least one that can stop the study. *Steps:* write objectives, measures, thresholds and decisions. *Expected evidence:* table. *Rubric:* 3 = feasibility-focused, thresholds predeclared, stop criterion linked to a premise; 2 = includes effect-based criterion; 1 = vague; 0 = none.

**EX026 — Reproducibility checklist for your own analysis.** *Objective:* make a computation auditable. *Inputs:* any analysis you have run (or the Chapter 1 lab). *Constraints:* follow §4.7. *Steps:* produce data hashes, environment record, commit or file hash, and a run-log entry. *Expected evidence:* the record. *Rubric:* 3 = another person could rerun and compare; 2 = one element missing; 1 = description only; 0 = none.

### Chapter synthesis

Before claiming improvement, establish the reference point. Reproduce the baseline as published, diagnose discrepancies, and choose a deployment-faithful configuration as the real comparison. Plan sample size from the smallest effect of interest with an honest variance range, and pilot for feasibility with predeclared progression criteria. The Handoff Study now has a reproduced, corrected reference for its triage component and a pilot that determines whether F1 and F2 are triggered. Chapter 5 runs the main study.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 08

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Main study of incident decision quality

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Execute an ethically reviewed study according to its protocol, with randomization, counterbalancing and allocation concealment where appropriate.
2. Organize blinded review of decisions so that raters judge decision quality without knowing condition or outcome.
3. Preserve raw decisions and the full chain from raw data to reported numbers.
4. Analyze effects with uncertainty intervals, relate them to the smallest effect of interest and avoid significance-only reporting.
5. Conduct error analysis and harms analysis as first-class results, not afterthoughts.
6. Handle deviations, missing data and multiplicity transparently.

Chapter 4's pilot determined whether the Handoff Study could proceed and fixed the sample size. This chapter runs the main study and analyzes it. Chapter 6 then asks whether the result holds in a different context.

### 5.1 Decision quality as the outcome

Chapter 1 separated decision quality from outcome (§1.2.4). In a simulation, the separation can be enforced by design: each scenario has defined **decision points**, and at each point the scenario designer and an expert panel record the information available and the set of defensible options *given that information*. A decision is judged against that set, not against how the scenario "ends." This approach has two benefits: decisions remain judgeable even when the scenario's later events are random or adversarial, and raters can be blinded to outcomes because there are none to see at the moment of judgment.

Decision quality can have several dimensions. The Handoff Study's primary outcome is the count of comprehension and projection errors (Chapter 3 §3.3). Secondary outcomes include perception errors (for the mechanism pattern, H2), time to first containment decision (H3), and **harmful actions** — decisions that would cause avoidable harm, such as isolating a host that serves a critical public function when a narrower option was defensible. Harm is pre-specified as a safety outcome, because an intervention that reduces errors of understanding while increasing harmful actions is not an improvement.

### 5.2 Assignment

**Within-subject designs.** Each participant experiences all conditions on different scenarios. This controls for individual differences in skill, which are large among responders, and needs fewer participants. It introduces order and carryover effects: participants learn, tire, or carry the SHA's structure into later Standard trials. Mitigations: counterbalance the order of conditions and the pairing of scenarios to conditions (for example, with a Latin square), and present SHA conditions last for half of participants and first for the other half; test for period and carryover effects in analysis.

**Between-subject designs.** Each participant experiences one condition. There is no carryover, but more participants are needed and randomization must balance skill. Stratify randomization by experience level when samples are small.

**Allocation concealment.** The person enrolling participants should not know or influence the next assignment. Generate the assignment schedule in advance with a recorded seed, store it where the session facilitator cannot modify it, and reveal each assignment only at session start.

**Fidelity.** Record whether each session followed the protocol: correct materials, correct timing, no facilitator hints. Fidelity failures are deviations (§5.6), not data to be quietly discarded.

### 5.3 Blinded review

Raters are the measurement instrument. Blinding keeps them from measuring their expectations.

- **Strip condition cues.** Decisions are transcribed into a neutral format; references to SHA field names or to "the template" are redacted by someone other than the raters.
- **Randomize order.** Raters see decisions in random order across participants and conditions.
- **Independent rating.** At least two raters rate every decision independently; disagreements are adjudicated by a third rater or by structured discussion, with the pre-adjudication ratings preserved for agreement statistics.
- **Calibration items.** Mix previously rated items into each batch to detect drift.
- **Check the blind.** After rating, ask raters to guess condition for a sample; report guessing accuracy. If raters guess well above chance, blinding failed partially and the result should be discussed accordingly.

### 5.4 Preserving raw decisions

Every number in the results should be traceable to raw records: session recordings or logs (where consented), participant decision forms, raw rater sheets before adjudication, adjudication notes and the analysis scripts. Keep raw records immutable and hashed; derive analysis files by script. This chain is what makes the study auditable, and it is the core of the reproducibility archive in Chapter 8. Raw records also enable later critics (Chapter 7) to recode decisions under alternative outcome definitions.

In the SHA study the raw rater sheets matter most, because error-type coding is where adjudication can quietly change an outcome.

### 5.5 Analysis with uncertainty

#### 5.5.1 Estimates, not verdicts

Report the **estimated effect** with a **confidence interval** and relate the interval to the smallest effect of interest (SEOI). A p-value can be reported, but a conclusion such as "significant" or "not significant" alone discards the information readers need. Four interpretive cases arise:

| Interval relative to zero and SEOI | Interpretation |
|---|---|
| Entirely above SEOI | Effect present and practically important. |
| Above zero, includes SEOI | Effect present; practical importance uncertain. |
| Includes zero, excludes SEOI | No practically important effect (precise null). |
| Includes zero and SEOI | Inconclusive; study too imprecise. |

*In plain terms:* Where the confidence interval sits relative to zero and to the smallest effect that matters tells you which of these sentences you are allowed to write; "significant" alone is never enough.

#### 5.5.2 Models

Within-subject data with several scenarios per participant are naturally analyzed with mixed-effects models (random effects for participant and scenario; fixed effects for condition, period and possibly experience). The lab below uses simpler paired analyses so that every step can be checked by hand: a paired *t*-interval and an exact sign-flip permutation test, which assumes only that, under the null hypothesis of no condition effect, the sign of each participant's difference is equally likely to be positive or negative.

#### 5.5.3 Multiplicity

The protocol names one primary outcome. Secondary and exploratory outcomes are reported with their intervals and labeled; if many are tested, the protocol states whether and how it adjusts for multiple comparisons. Undisclosed multiplicity is one of the "forking paths" of Chapter 1.

### 5.6 Deviations, missing data and exclusions

- **Deviation log.** Every departure from protocol is logged with date, description, reason, whether outcome data had been seen, and its handling.
- **Missing data.** Report how many decisions are missing and why. Prefer analyses that use all available data under explicit assumptions; present sensitivity analyses for plausible departures from those assumptions.
- **Exclusions.** Only predeclared exclusion rules may be applied in the primary analysis. If a new problem is discovered (for example, a participant who had seen the scenarios before), report the primary analysis as planned *and* a sensitivity analysis with the exclusion, and let readers see both.

### 5.7 Error analysis and harms

An average effect hides where the intervention helps, does nothing or hurts. Error analysis reads the decisions themselves:

- Which scenarios and decision points account for most errors in each condition?
- Did SHA reduce the predicted error types (comprehension, projection) and not others (perception)? This is the mechanism test, H2.
- Did SHA introduce *new* errors — for example, anchoring on the sender's stated hypotheses, or overtrusting a "T-gaps" list that omitted a gap?
- Which participants were harmed or unaffected, and do they share characteristics?

**Harms analysis** treats safety outcomes with the same rigor as benefits. Because harmful actions are rare, a study is usually underpowered to detect an increase. The honest report gives the interval and states that harms of a given size cannot be excluded.

### 5.8 Worked example: simulated incident cases scored by independent responders under two workflows

*All participants, scenarios and results are synthetic.* The figure below is a 12-participant teaching excerpt; Chapter 4's planning required 32–71 participants, so the excerpt is deliberately small enough to check by hand. Each participant handled three scenarios under Standard handoff and three under SHA (scenarios seeded from the Harbor Library, Cedar Training Network and Lumen Library Reservations cases, counterbalanced). Two blinded raters coded errors; adjudicated counts are summed over the three scenarios per condition.

```python
"""Chapter 5 offline lab: synthetic within-subject results for the Handoff Study."""
from itertools import product
from statistics import mean, stdev

# participant: (standard_cp_errors, sha_cp_errors, standard_perception, sha_perception, standard_harm, sha_harm)
# cp = comprehension + projection errors summed over 3 scenarios per condition
DATA = {
    "P01": (5, 3, 2, 2, 0, 0), "P02": (4, 4, 1, 1, 0, 1), "P03": (6, 3, 2, 1, 1, 0),
    "P04": (3, 2, 1, 1, 0, 0), "P05": (7, 4, 3, 3, 1, 0), "P06": (4, 3, 1, 2, 0, 0),
    "P07": (5, 5, 2, 2, 0, 0), "P08": (6, 4, 2, 2, 1, 1), "P09": (2, 2, 0, 1, 0, 0),
    "P10": (5, 2, 1, 1, 0, 0), "P11": (4, 3, 2, 2, 0, 1), "P12": (6, 5, 2, 1, 0, 1),
}
T_CRIT_DF11 = 2.201  # two-sided 95% critical value of Student's t with 11 df (standard tables)

def paired(idx_a, idx_b):
    d = [v[idx_a] - v[idx_b] for v in DATA.values()]  # positive = fewer errors with SHA
    m, s = mean(d), stdev(d)
    half = T_CRIT_DF11 * s / len(d) ** 0.5
    return d, m, s, (m - half, m + half)

def sign_flip_p(d):
    obs = abs(sum(d))
    hits = sum(1 for signs in product((1, -1), repeat=len(d))
               if abs(sum(x * s for x, s in zip(d, signs))) >= obs)
    return hits / 2 ** len(d)

if __name__ == "__main__":
    for label, a, b in (("comprehension+projection", 0, 1), ("perception", 2, 3), ("harmful actions", 4, 5)):
        d, m, s, ci = paired(a, b)
        print(f"{label:25s} mean_diff={m:.3f} sd={s:.3f} 95%CI=({ci[0]:.3f}, {ci[1]:.3f}) exact_p={sign_flip_p(d):.4f}")
```

Expected output (verified with Python 3):

```text
comprehension+projection  mean_diff=1.417 sd=1.165 95%CI=(0.677, 2.157) exact_p=0.0039
perception                mean_diff=0.000 sd=0.603 95%CI=(-0.383, 0.383) exact_p=1.0000
harmful actions           mean_diff=-0.083 sd=0.669 95%CI=(-0.508, 0.341) exact_p=1.0000
```

**Interpretation.**

- *Primary outcome (H1).* SHA participants made on average 1.417 fewer comprehension/projection errors over three scenarios, i.e. about 0.47 per scenario, with a 95% interval of about 0.23 to 0.72 errors per scenario (dividing the reported interval by three). The interval excludes zero (exact permutation p ≈ 0.004), so an effect is likely present. But the SEOI was 0.5 errors per scenario, and the interval includes values both below and above it. The correct conclusion is: *"an effect is present; whether it reaches the practically important threshold is uncertain."* Writing "SHA meaningfully reduces errors" would overstate the evidence.
- *Mechanism pattern (H2).* Perception errors show no difference (mean 0.000, interval −0.38 to 0.38 over three scenarios). This is the pattern the mechanism predicted. With 12 participants the perception interval is wide enough that a modest reduction cannot be excluded, so H2 is *consistent with* the mechanism rather than *strongly confirming* it.
- *Harms.* Harmful actions were slightly *more* frequent under SHA (mean difference −0.083, where negative means more harm with SHA), interval −0.51 to 0.34. No increase is demonstrated, but an increase of up to half a harmful action per three scenarios cannot be excluded. The exact p-value of 1.000 reflects the discreteness of five ±1 differences, not proof of no effect. Error analysis should read all seven harmful actions (four under SHA, three under Standard) to see whether SHA's "H-current" field anchored participants on a sender's hypothesis.
- *Reporting.* All three results are reported, including the uncomfortable harms result. The primary result is not upgraded because the mechanism pattern looks favorable.

### 5.9 Practical activity: results section skeleton

Write a results section in this order: participant flow (recruited, consented, randomized, completed, excluded with reasons); fidelity and deviations; rater agreement and blinding check; primary outcome estimate and interval relative to SEOI; mechanism outcome; safety outcome; secondary outcomes; sensitivity analyses; error analysis. Each number must reference the script and data hash that produced it.

In the SHA study, the primary estimate is the difference in comprehension and projection errors per scenario, read against the SEOI of 0.5. If the interval excludes the SEOI, failure condition F3 applies and the section reports a precise null. Placing participant flow first lets a reader judge whether exclusions could explain the estimate before seeing it.

### 5.10 Reporting the study so that others can judge it

Clinical trials have the most developed reporting guidance for randomized studies. The [CONSORT 2010 statement (Schulz, Altman and Moher, 2010)](https://doi.org/10.1136/bmj.c332) provides a checklist and a participant flow diagram for reporting parallel-group randomized trials. The Handoff Study is a within-subject simulation experiment, not a clinical trial, and CONSORT should not be applied mechanically. But its core demands transfer well and are frequently unmet in security user studies:

- **A flow diagram** showing how many people were assessed for eligibility, enrolled, allocated to each sequence, completed each period, and were analyzed — with reasons for every loss.
- **The randomization method**, including sequence generation, allocation concealment mechanism, and who implemented each step (Chapter 5 §5.2).
- **Who was blinded** — participants, facilitators, raters, analysts — and how.
- **Pre-specified primary and secondary outcomes**, with any changes after the study began and the reasons.
- **Harms**, reported for each condition.
- **Where the full protocol can be accessed** and how it was registered.

A thesis chapter can include a short "reporting checklist" table mapping each of these items to a page. Examiners use such tables; reviewers of later papers will expect them.

### 5.11 Missing data: mechanisms before methods

[Rubin (1976)](https://doi.org/10.1093/biomet/63.3.581) established the framework still used to reason about missing data, in which the key question is how the probability that a value is missing relates to the data. The modern vocabulary distinguishes three cases:

- **Missing completely at random (MCAR):** missingness is unrelated to any study variable — for example, a recording failure caused by a power cut. Analyzing complete cases is unbiased, though less precise.
- **Missing at random (MAR):** missingness depends on observed variables but not on the missing value itself once those are accounted for — for example, novices are more likely to skip the final scenario, and experience is recorded. Methods that condition on the observed variables (model-based analysis, multiple imputation) can recover unbiased estimates.
- **Missing not at random (MNAR):** missingness depends on the unobserved value — for example, participants who were confused by a scenario (and would have made many errors) abandon it. No method can fully correct this from the observed data; only sensitivity analyses can show how conclusions change under assumed departures.

In incident simulations, MNAR is a realistic threat, because difficulty, confusion and dropout are linked. The protocol should therefore (1) design to prevent missingness (short sessions, breaks, technical rehearsal), (2) record reasons for every missing value, (3) pre-specify the primary handling method, and (4) pre-specify a sensitivity analysis — for example, assigning missing scenario scores the worst observed value in that condition, then the best, and reporting both. If conclusions survive both extremes, missingness is not driving them.

### 5.12 Multiplicity done properly

Section 5.5.3 noted that secondary outcomes multiply the chance of a false positive. A common correction controls the **familywise error rate** (for example, Bonferroni), which guards against even one false positive but becomes very conservative as outcomes multiply. [Benjamini and Hochberg (1995)](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) introduced control of the **false discovery rate** — the expected proportion of false positives among the outcomes declared significant — and a simple step-up procedure to achieve it. For a family of secondary outcomes in an exploratory-but-disciplined study, false-discovery-rate control is often the better trade-off.

The procedure: sort the *m* p-values from smallest to largest; find the largest rank *k* such that the *k*-th smallest p-value is at most *(k/m)·q*, where *q* is the chosen false discovery rate; declare the outcomes with ranks 1 through *k* significant. The "step-up" feature means an outcome can be declared significant even if its own p-value exceeds its own rank's threshold, provided a higher-ranked p-value passes.

The Handoff Study also needs a different kind of claim for its safety outcome. "No significant increase in harmful actions" is not evidence of safety; it may reflect imprecision. The correct question is whether any increase is reliably smaller than a pre-declared margin — an equivalence question (§3.13). Using a 90% confidence interval, the two one-sided tests procedure at α = 0.05 concludes equivalence when the whole interval lies inside the margin.

The following lab applies both procedures to synthetic secondary outcomes.

```python
# Synthetic secondary outcomes of the Handoff Study (illustrative only).
# Each: (name, estimate, standard_error) for the SHA-minus-Standard difference.
from statistics import NormalDist
N = NormalDist()
outcomes = [
    ("perception_errors",        -0.10, 0.20),
    ("time_to_containment_min",  -1.80, 0.75),
    ("harmful_actions",           0.05, 0.09),
    ("escalation_errors",        -0.40, 0.17),
    ("documentation_gaps",       -0.55, 0.30),
]
def p_two_sided(est, se):
    return 2 * (1 - N.cdf(abs(est / se)))
ps = [(name, p_two_sided(e, s)) for name, e, s in outcomes]
# Benjamini-Hochberg step-up at q = 0.05
q = 0.05
m = len(ps)
ranked = sorted(ps, key=lambda x: x[1])
k_max = 0
for k, (_, p) in enumerate(ranked, start=1):
    if p <= k / m * q:
        k_max = k
rejected = {name for name, _ in ranked[:k_max]}
print("outcome                   p_raw   BH_reject")
for name, p in ps:
    print(f"{name:<24} {p:6.4f}   {name in rejected}")
# Equivalence (TOST) for harmful actions with margin +/- 0.25 actions per participant
name, est, se = outcomes[2]
margin = 0.25
z = N.inv_cdf(0.95)
lo, hi = est - z * se, est + z * se
print(f"harmful_actions 90% CI: [{lo:.3f}, {hi:.3f}] margin +/-{margin}")
print("equivalent within margin:", lo > -margin and hi < margin)
```

Expected output:

```text
outcome                   p_raw   BH_reject
perception_errors        0.6171   False
time_to_containment_min  0.0164   True
harmful_actions          0.5785   False
escalation_errors        0.0186   True
documentation_gaps       0.0668   False
harmful_actions 90% CI: [-0.098, 0.198] margin +/-0.25
equivalent within margin: True
```

**Reading the output.** Time to containment and escalation errors are declared discoveries at q = 0.05. Note escalation errors: its p-value (0.0186) is the second smallest and passes its rank threshold of 2/5 × 0.05 = 0.02, and because the procedure steps up, the smallest p-value (0.0164) is also declared even though it exceeds its own threshold of 0.01. Documentation gaps (p ≈ 0.067) are not declared, and the results paragraph should describe that estimate with its interval rather than as "no effect." For harmful actions, the 90% interval [−0.098, 0.198] lies within ±0.25, so the study can claim that any increase in harmful actions is smaller than the pre-declared margin — a far stronger safety statement than "not significant." The claim is only as good as the margin: had the protocol set ±0.15, the upper bound 0.198 would exceed it and equivalence could not be claimed.

*In plain terms:* The first table tells you which secondary results survive a correction for testing five things at once; the last two lines show that the study can positively say the SHA does not meaningfully increase harmful actions, because the plausible range of the effect sits inside the safety margin chosen in advance.

### 5.13 Analytic flexibility: many analysts and the multiverse

Even with a pre-registered plan, many analysis choices remain: how to treat scenarios with a facilitator deviation, whether to model scenario as a random effect, whether to count a decision with two errors as one or two. [Silberzahn et al. (2018)](https://doi.org/10.1177/2515245917747646) gave the same dataset and research question to many independent analysis teams and found substantial variation in their estimates, arising from reasonable but different analytic choices. [Steegen et al. (2016)](https://doi.org/10.1177/1745691616658637) proposed **multiverse analysis**: performing the analysis across the full set of reasonable processing and analysis choices and reporting the distribution of results, to make transparent how much conclusions depend on those choices.

For a thesis, a compact multiverse is achievable. List the defensible choices (for example: three rules for handling deviations × two outcome codings × with or without scenario random effects = 12 specifications), run the analysis for each, and report the range of estimates along with the pre-registered one. If all twelve point in the same direction and most exclude zero, the conclusion is robust to analytic choice. If they scatter, the honest conclusion is weaker, and the thesis should say which choice drives the difference. The pre-registered analysis remains primary; the multiverse is a robustness check, not a menu.

### 5.14 Models for within-subject incident data

The worked example uses paired differences because they are transparent. A full analysis usually fits a **mixed-effects model** with fixed effects for condition, period and sequence, and random intercepts for participants and scenarios. The model's advantages are practical:

- It uses all observations, including participants with one missing scenario, rather than discarding incomplete pairs.
- Random scenario effects acknowledge that scenarios are a sample from a larger population of possible incidents, so conclusions generalize beyond the specific scenarios used — a point emphasized in discussions of the generalizability of experimental findings (see Chapter 6 §6.8).
- Period and sequence terms test carryover and learning.

Its risks: models with many random effects may fail to converge on small samples, and analysts then simplify the model in data-dependent ways — another source of flexibility. Pre-specify the model and a fallback sequence ("if the full model does not converge, drop the random slope first, then…"). Count outcomes (errors per scenario) may call for a Poisson or negative-binomial link rather than a normal model; check over-dispersion and pre-specify the choice.

### 5.15 Qualitative evidence inside the experiment

Numbers show whether the SHA changed errors; they do not show how. Brief, structured debriefs after each condition — "What did you understand to be the main hypothesis when you took over? What did you think had been ruled out? What did you expect to happen next?" — provide process evidence. Two rules keep them from contaminating the primary outcome: hold debriefs after all scored decisions in the scenario are recorded, and analyze transcripts with a codebook developed before unblinding, with codes for the mechanism categories (hypotheses, ruled-out items, gaps, expectations, roles). Agreement between the qualitative pattern and the quantitative mechanism test is convergent evidence; disagreement is a finding to report, not to hide. The sensemaking account (§2.9.4) predicts that debriefs will reveal role confusion that the error scores miss — a specific, checkable expectation.

### 5.16 Harms analysis in depth

Harm in the Handoff Study is a decision that would cause avoidable damage relative to a defensible alternative. Treating harm as a first-class result means:

1. **Defining harm categories in advance**: over-containment (isolating a critical service unnecessarily), under-containment (leaving an attacker foothold that a defensible option would have removed), evidence destruction (actions that would compromise forensic data), and unauthorized disclosure (sharing information beyond its TLP or legal constraints).
2. **Reporting each category by condition**, not only the total, because an intervention could reduce under-containment while increasing over-containment.
3. **Reviewing every harmful decision qualitatively.** Harmful decisions are rare and individually informative. A short narrative for each, written by a rater blind to condition, often reveals scenario design flaws or plausible failure modes of the aid.
4. **Using equivalence logic** for the safety claim, as in §5.12.

### Common errors and limits

- Judging decisions by scenario outcome rather than information available at the decision point.
- Letting the facilitator who knows the condition also rate decisions.
- Reporting "significant" without an interval or reference to the SEOI.
- Dropping participants post hoc without a sensitivity analysis showing the effect of the exclusion.
- Treating absence of a significant harm as absence of harm.
- Ignoring order and carryover in within-subject designs.
- Limit: the lab's paired analysis ignores scenario-level variation; a full analysis would model participants and scenarios jointly.

### Exercises — chapter 5

**EX027 — Assignment schedule.** *Objective:* design concealed, counterbalanced assignment. *Inputs:* 24 participants, conditions Standard and SHA, scenarios A–F (three per condition), two experience strata. *Constraints:* balance order and scenario-condition pairing within strata. *Steps:* produce the schedule logic (e.g., Latin-square-based); describe concealment; describe fidelity checks. *Expected evidence:* schedule description and procedures. *Rubric:* 3 = balanced order and pairing within strata, seed recorded, concealment credible; 2 = one balance missing; 1 = simple alternation; 0 = none.

**EX028 — Blinding protocol.** *Objective:* protect rating from expectation. *Inputs:* sample decision text: "Per the T-gaps field, DNS logs were unavailable for 02:00–04:00, so I did not treat the lack of lookups as evidence of no C2." *Constraints:* preserve meaning; remove condition cues. *Steps:* redact the text; list three other cue types; design a blinding check. *Expected evidence:* redacted text and protocol. *Rubric:* 3 = cues removed without changing reasoning, check designed; 2 = one cue type missed; 1 = meaning altered; 0 = none.

**EX029 — Interpret against SEOI.** *Objective:* draw calibrated conclusions. *Inputs:* the lab output. *Constraints:* convert to per-scenario units. *Steps:* state primary, mechanism and harms conclusions in one sentence each; classify the primary result by the table in §5.5.1. *Expected evidence:* three sentences and classification. *Rubric:* 3 = "present, practical importance uncertain," mechanism "consistent with," harms "not excluded"; 2 = one overstatement; 1 = significance-only; 0 = none.

**EX030 — Sensitivity analysis.** *Objective:* handle a discovered exclusion. *Inputs:* after unblinding, the deviation log shows P10 had seen two scenarios in a prior training course. *Constraints:* the primary analysis stays as planned. *Steps:* compute the paired analysis without P10 (t critical value 2.228 for 10 df); compute the exact sign-flip p; report both analyses. *Expected evidence:* numbers and paragraph. *Rubric:* 3 = mean 1.273, interval (0.531, 2.014), p 0.0078 and correct reporting of both; 2 = numbers right, reporting wrong; 1 = replaces primary; 0 = none.

**EX031 — Error analysis plan.** *Objective:* read decisions, not averages. *Inputs:* the Handoff Study. *Constraints:* at least five questions; include possible new errors caused by SHA. *Steps:* write questions, data needed and how each answer would change the claim. *Expected evidence:* plan. *Rubric:* 3 = includes anchoring/overtrust, per-scenario and per-participant analyses, links to claim; 2 = generic; 1 = averages only; 0 = none.

**EX032 — Results paragraph.** *Objective:* write publishable, calibrated results. *Inputs:* lab output, your EX030 result. *Constraints:* 200–300 words; every number traceable. *Steps:* follow §5.9 order for primary, mechanism, harms and sensitivity. *Expected evidence:* paragraph. *Rubric:* 3 = calibrated, complete, harms reported, sensitivity included; 2 = one omission; 1 = overclaims; 0 = none.

### Chapter synthesis

A main study earns trust through execution discipline: concealed and counterbalanced assignment, blinded raters with measured agreement, preserved raw decisions, estimates with intervals interpreted against a predeclared smallest effect of interest, and equal rigor for harms. In the synthetic excerpt, SHA reduced comprehension and projection errors with uncertain practical importance, left perception errors unchanged as predicted, and could not exclude a small increase in harmful actions. Chapter 6 asks whether this pattern survives a different organization with different staffing and telemetry.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 08

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Independent validation across contexts

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Explain external validity and transportability for incident-response findings, and identify the contextual features that plausibly modify an effect.
2. Distinguish direct (close) replication from conceptual replication and choose between them for a stated purpose.
3. Quantify heterogeneity between contexts and interpret it cautiously when few contexts exist.
4. State boundary conditions — where a method stops working — as findings rather than failures.
5. Design a second-context study that tests a predicted boundary rather than merely repeating the first study.

Chapter 5 found, in one synthetic organization, that SHA reduced comprehension and projection errors with uncertain practical importance. A single context cannot show whether the result depends on that organization's staffing, telemetry, culture or scenarios. This chapter tests the claim in a second context. Chapter 7 will then expose the combined evidence to critique.

### 6.1 Why incident-response results travel poorly

Chapter 1 (§1.1) noted that incidents are unrepeatable and sociotechnical. The consequence for generalization is that many features of a context can **modify** an effect:

| Contextual feature | Plausible modification of the SHA effect |
|---|---|
| Telemetry completeness | Fewer gaps → less benefit from the T-gaps field. |
| Staffing model | Follow-the-sun handoffs across regions → more handoffs, more language and time-zone barriers → possibly more benefit. |
| Responder experience | Veterans may already convey ruled-out hypotheses → less benefit. |
| Existing handoff culture | Strong verbal handoff norms → SHA redundant or disruptive. |
| Incident mix | Routine incidents need little handoff context. |
| Tooling | Case-management tools with structured fields → Standard already partly structured. |
| Regulatory pressure | Documentation requirements may make SHA a compliance task, changing how it is filled in (the sociotechnical account in Chapter 2 §2.3.3). |

*In plain terms:* Each contextual difference between organizations is a reason the effect might be larger, smaller or absent elsewhere; the table turns those reasons into testable moderators.

**External validity** asks whether a result holds for other populations, settings, treatments and outcomes. **Transportability** asks a sharper question: given what we know about how the target context differs, what effect should we expect there? Transportability reasoning requires a mechanism (Chapter 3) because only a mechanism tells us which differences matter.

### 6.2 Kinds of replication

The [National Academies (2019)](https://www.nationalacademies.org/read/25303/chapter/3) define replicability as obtaining consistent results across studies aimed at the same scientific question, each with its own data, and note that a rigorous study may still fail to replicate. Within that definition, it helps to distinguish:

- **Direct (close) replication**: the same protocol, materials and analysis in a new sample. It tests whether the original result was a chance finding or an artifact of a particular sample.
- **Conceptual replication**: the same hypothesis tested with different operationalizations — different scenarios, measures or populations. It tests whether the result depends on specific materials.
- **Boundary test**: a deliberate change in one contextual feature predicted by the mechanism to modify the effect. It tests the mechanism itself.

For doctoral work, a boundary test is often the most informative second study, because it can strengthen the mechanism *whichever* way it comes out — provided the prediction was registered before the data were collected. The large collaborative replication effort reported by the [Open Science Collaboration (2015)](https://doi.org/10.1126/science.aac4716), which attempted to replicate 100 published psychology studies, illustrates both the value of systematic replication and the debate over what counts as a successful replication; that debate is a reason to define the replication criterion in advance.

### 6.3 Heterogeneity

When an effect is estimated in several contexts, the estimates differ for two reasons: sampling error and real differences. Meta-analysis separates them. Under a **fixed-effect** model all contexts share one true effect; under a **random-effects** model true effects vary around a mean. Cochran's Q tests whether observed dispersion exceeds what sampling error would produce, and **I²**, proposed by [Higgins and Thompson (2002)](https://doi.org/10.1002/sim.1186) and popularized in [Higgins et al. (2003)](https://doi.org/10.1136/bmj.327.7414.557), describes the proportion of total variation attributable to heterogeneity rather than chance.

With only two or three contexts, these statistics are very imprecise: Q has little power, I² has a wide uncertainty interval, and random-effects variance estimates are unstable. A doctoral thesis with two contexts should therefore treat heterogeneity statistics as *descriptive*, rely primarily on the **registered boundary prediction** and the **within-context moderator analysis**, and avoid reporting a pooled effect as if it described any real context when heterogeneity is evident.

### 6.4 Boundary conditions as findings

A **boundary condition** is a value of a contextual feature beyond which the effect weakens, disappears or reverses. In incident-response practice, boundary conditions are highly actionable: they tell an organization whether to adopt a method. "SHA helps when telemetry is sparse but adds little where it is dense" is more useful than "SHA helps on average."

A boundary claim requires evidence of the same quality as a main effect. In particular, a boundary observed only *across* contexts is confounded by every other difference between those contexts. Stronger evidence comes from varying the feature *within* a context — for example, presenting scenarios with high and low telemetry gaps to the same participants — so that staffing, culture and tooling are held constant.

### 6.5 Designing the second-context study

The Handoff Study's second context is the synthetic **Kestrel Freight Logistics SOC (KFL-SOC)**: a 24×7 tiered SOC with follow-the-sun handoffs between two regions, mature EDR coverage and a case-management tool with some structured fields. Compared with NMS-CSIRT, it differs on telemetry (dense vs. sparse), staffing (tiered, multi-region vs. small, single-site) and tooling.

**Registered predictions (before KFL data collection):**

- **P6.1 (boundary):** the SHA effect on comprehension/projection errors will be smaller at KFL than at NMS, because KFL's dense telemetry produces fewer gaps for the T-gaps field to convey.
- **P6.2 (within-context moderator):** within KFL, the SHA effect will be larger in scenarios designed with high telemetry gaps than in low-gap scenarios.
- **P6.3 (mechanism pattern):** perception errors will remain unaffected at KFL.

**Design choices:** same SHA, codebook and rater training (direct replication of procedure); new scenarios adapted to logistics operations but with a crossed factor of telemetry-gap level (conceptual replication plus boundary test); raters from outside both organizations; preregistration of P6.1–P6.3 and of the analysis.

### 6.6 Worked example: a second synthetic service context with different staffing and telemetry quality

*All values are synthetic.* The script below takes the NMS effect from Chapter 5 (mean 1.417, standard error 1.165/√12 ≈ 0.336) and a KFL effect, pools them with inverse-variance weights, computes Q and I², and tests the KFL within-context gap interaction. Intervals use the normal approximation (±1.96 SE), so the NMS interval differs slightly from the *t*-interval in Chapter 5.

```python
"""Chapter 6 offline lab: combine two synthetic contexts and test heterogeneity."""
from math import sqrt

# context: (mean reduction in comprehension+projection errors per 3 scenarios, standard error)
CONTEXTS = {
    "NMS-CSIRT (sparse telemetry)": (1.417, 0.336),
    "KFL-SOC (dense telemetry)":    (0.350, 0.250),
}
# KFL-SOC split by scenario telemetry-gap level: (mean reduction, SE)
KFL_BY_GAP = {"high-gap scenarios": (0.900, 0.400), "low-gap scenarios": (0.050, 0.300)}

def fixed_effect(effects):
    w = {k: 1 / se ** 2 for k, (m, se) in effects.items()}
    pooled = sum(w[k] * effects[k][0] for k in effects) / sum(w.values())
    se_pooled = sqrt(1 / sum(w.values()))
    q = sum(w[k] * (effects[k][0] - pooled) ** 2 for k in effects)
    df = len(effects) - 1
    i2 = max(0.0, (q - df) / q) if q > 0 else 0.0
    return pooled, se_pooled, q, i2

def diff(a, b):
    d = a[0] - b[0]
    se = sqrt(a[1] ** 2 + b[1] ** 2)
    return d, se, d / se

if __name__ == "__main__":
    for k, (m, se) in CONTEXTS.items():
        print(f"{k:30s} effect={m:.3f} 95%CI=({m - 1.96*se:.3f}, {m + 1.96*se:.3f})")
    pooled, se, q, i2 = fixed_effect(CONTEXTS)
    print(f"fixed-effect pooled={pooled:.3f} 95%CI=({pooled - 1.96*se:.3f}, {pooled + 1.96*se:.3f}) Q={q:.2f} I2={i2:.2f}")
    d, se_d, z = diff(*CONTEXTS.values())
    print(f"context difference={d:.3f} SE={se_d:.3f} z={z:.2f}")
    d, se_d, z = diff(KFL_BY_GAP["high-gap scenarios"], KFL_BY_GAP["low-gap scenarios"])
    print(f"KFL gap interaction={d:.3f} SE={se_d:.3f} z={z:.2f}")
```

Expected output (verified with Python 3):

```text
NMS-CSIRT (sparse telemetry)   effect=1.417 95%CI=(0.758, 2.076)
KFL-SOC (dense telemetry)      effect=0.350 95%CI=(-0.140, 0.840)
fixed-effect pooled=0.730 95%CI=(0.337, 1.123) Q=6.49 I2=0.85
context difference=1.067 SE=0.419 z=2.55
KFL gap interaction=0.850 SE=0.500 z=1.70
```

**Interpretation.**

- *P6.1 (boundary).* The KFL effect (0.35 per three scenarios, interval −0.14 to 0.84) is smaller than NMS's (1.42). The difference (1.07, SE 0.42, z ≈ 2.55) is consistent with the registered prediction. But the two contexts differ in telemetry, staffing, tooling *and* scenarios; the across-context difference alone cannot attribute the change to telemetry.
- *P6.2 (moderator).* Within KFL, SHA's effect was 0.90 in high-gap scenarios and 0.05 in low-gap scenarios; the interaction (0.85, SE 0.50, z ≈ 1.70) is in the predicted direction but imprecise. Because it holds staffing and tooling constant, this within-context evidence is *more diagnostic* of the telemetry mechanism than the across-context difference, even though it is less precise.
- *Pooling.* The fixed-effect pooled estimate (0.73) is arithmetically correct but describes neither context; Q = 6.49 on 1 df and I² ≈ 0.85 indicate substantial heterogeneity (with the caveat that two contexts give an imprecise I²). Reporting "SHA reduces errors by 0.73" would misrepresent the evidence.
- *Claim revision.* "SHA reduced comprehension and projection errors where telemetry was sparse; in a context with dense telemetry, the overall effect was small and uncertain, concentrated in scenarios with high telemetry gaps. These results are consistent with the proposed mechanism and suggest telemetry completeness as a boundary condition; confirming that would require more contexts or a stronger within-context test."

### 6.7 Practical activity: transportability memo

For a third organization of your choice (real or synthetic, described only at a level that exposes no confidential information), write a memo that: lists its values on each feature in §6.1; predicts the SHA effect using the mechanism and the two-context evidence; states the uncertainty; and proposes the smallest study that would check the prediction there. The memo is a reasoning exercise, not a recommendation to adopt.

A memo for a small library service such as Harbor Library would first have to say whether its responders hand off between shifts at all, since the mechanism works through handoffs.

### 6.8 The generalizability problem, stated precisely

[Yarkoni (2022)](https://doi.org/10.1017/S0140525X20001685) argued that much of psychology suffers a "generalizability crisis": verbal claims are stated at a level of generality far beyond what the statistical models support, because those models treat only participants as a random sample while treating stimuli, tasks, settings and experimenters as fixed. If the verbal claim is about *incident handoffs in general*, then scenarios, organizations and facilitators are also samples from larger populations, and their variability belongs in the uncertainty of the estimate.

For incident-response research this critique has teeth. A study using four scenarios written by one researcher, run in one organization, can at most support claims about those scenarios in that organization unless the variation across scenarios and organizations is modeled or the claim is narrowed. Two practical consequences follow:

1. **Model scenarios as random effects** (Chapter 5 §5.14) and, if there are several sites, sites as well. The resulting intervals will be wider — honestly so.
2. **Match the verbal claim to the sampled variation.** If only one scenario author wrote all scenarios, say so, and consider recruiting a second author whose scenarios serve as a replication of stimulus sampling.

[Simons, Shoda and Lindsay (2017)](https://doi.org/10.1177/1745691617708630) proposed that empirical papers include a **Constraints on Generality (COG)** statement specifying the target populations of participants, materials, procedures and contexts to which the authors expect the findings to generalize, and the reasons. A COG statement for the Handoff Study might read:

> We expect the SHA's reduction in comprehension and projection errors to generalize to shift handoffs among responders with at least one year of operational experience, in incidents where investigation continues across shifts and telemetry is incomplete. We have no evidence about handoffs between organizations, handoffs under active legal constraint, or teams whose working language differs from the template's. We expect smaller or absent effects where telemetry is complete and incidents are routine, because the mechanism depends on transmitting uncertainty that such incidents lack.

The statement is falsifiable: a replication within the stated constraints that finds no effect counts against the claim, while a failure outside them marks a boundary rather than a refutation.

### 6.9 Transportability as a formal question

[Pearl and Bareinboim (2014)](https://doi.org/10.1214/14-STS486) treated external validity as a problem of **transportability**: when can a causal effect estimated in one population be used to infer the effect in another, given knowledge about how the populations differ? They represent differences as explicit features of a causal diagram and derive conditions under which the target effect can be computed from source experiments plus observational information in the target. The full formal apparatus exceeds this book; three of its ideas are directly usable.

- **Name the differences.** Transport is only meaningful once the researcher has listed which mechanisms or distributions differ between source and target. The table in §6.1 is the start of this list.
- **Distinguish differences in distribution from differences in mechanism.** If the target organization simply has more novice responders, and the effect for novices and experts is known separately, the target effect can be re-weighted. If the target organization's handoffs work differently (for example, overlapping shifts with spoken handoff), the mechanism itself differs and re-weighting cannot help.
- **Some effects are not transportable from available data.** When the relevant difference affects the mechanism and nothing in the source study measures it, the honest conclusion is that the target effect is unknown — not that it equals the source effect.

The transportability memo in §6.7 is an informal application: features mapped, mechanism reasoned through, a minimal check proposed. The formal framework explains why the memo must distinguish "different mix" from "different mechanism."

### 6.10 Random-effects synthesis across several sites

With two contexts, Chapter 6 compared estimates directly. With more sites, a **random-effects meta-analysis** summarizes them. [DerSimonian and Laird (1986)](https://doi.org/10.1016/0197-2456(86)90046-2) proposed a widely used method for meta-analysis in clinical trials that estimates the between-study variance (τ²) from the heterogeneity statistic Q and incorporates it into the pooled estimate's weights. The heterogeneity measures Q and I² were introduced in §6.3 with [Higgins and Thompson (2002)](https://doi.org/10.1002/sim.1186) and [Higgins et al. (2003)](https://doi.org/10.1136/bmj.327.7414.557).

Two quantities answer different questions:

- The **confidence interval for the random-effects mean** answers: *what is the average effect across sites like these?*
- The **prediction interval** answers: *what effect should we expect at a new site like these?* It adds the between-site variance to the uncertainty in the mean. A common form uses a t distribution with *k* − 2 degrees of freedom for *k* sites.

For practitioners deciding whether to adopt the SHA, the prediction interval is usually the more relevant number. The following lab uses a synthetic five-site extension of the Handoff Study.

```python
# Synthetic five-site extension of the Handoff Study (illustrative only).
# site: (mean reduction in comprehension+projection errors, standard error)
import math
sites = {
    "NMS-CSIRT": (1.10, 0.25),
    "KFL-SOC":   (0.45, 0.30),
    "Site-C":    (0.90, 0.35),
    "Site-D":    (0.20, 0.40),
    "Site-E":    (1.30, 0.45),
}
y = [v[0] for v in sites.values()]
v = [v[1] ** 2 for v in sites.values()]
w = [1 / vi for vi in v]
fixed = sum(wi * yi for wi, yi in zip(w, y)) / sum(w)
Q = sum(wi * (yi - fixed) ** 2 for wi, yi in zip(w, y))
k = len(y)
C = sum(w) - sum(wi ** 2 for wi in w) / sum(w)
tau2 = max(0.0, (Q - (k - 1)) / C)
I2 = max(0.0, (Q - (k - 1)) / Q) * 100 if Q > 0 else 0.0
wr = [1 / (vi + tau2) for vi in v]
rand = sum(wi * yi for wi, yi in zip(wr, y)) / sum(wr)
se_r = math.sqrt(1 / sum(wr))
t_crit = 3.182  # t(0.975, df = k - 2 = 3)
pi_half = t_crit * math.sqrt(tau2 + se_r ** 2)
print(f"fixed-effect mean: {fixed:.3f}")
print(f"Q = {Q:.3f} on {k-1} df; tau^2 = {tau2:.4f}; I^2 = {I2:.1f}%")
print(f"random-effects mean: {rand:.3f} (SE {se_r:.3f})")
print(f"95% CI: [{rand-1.96*se_r:.3f}, {rand+1.96*se_r:.3f}]")
print(f"95% prediction interval: [{rand-pi_half:.3f}, {rand+pi_half:.3f}]")
```

Expected output:

```text
fixed-effect mean: 0.810
Q = 6.363 on 4 df; tau^2 = 0.0666; I^2 = 37.1%
random-effects mean: 0.794 (SE 0.191)
95% CI: [0.420, 1.167]
95% prediction interval: [-0.227, 1.814]
```

**Reading the output.** The average effect across these five synthetic sites is clearly positive (random-effects mean 0.794, 95% CI 0.420 to 1.167). Moderate heterogeneity (I² ≈ 37%) means sites differ by more than sampling error alone. The prediction interval for a new site runs from −0.227 to 1.814: a new organization similar to these could plausibly see anything from a small worsening to a large improvement. The average is a confident claim; the prediction for any one site is not. With only five sites, τ² itself is estimated imprecisely, so even the prediction interval is approximate; the thesis should say so.

*In plain terms:* On average across sites the handoff template helps, and we are fairly sure of that. But for any single new organization, the plausible range includes "no benefit at all," because sites genuinely differ. Adoption decisions should look at the second range, not the first.

### 6.11 Organizational and cross-organizational context as moderators

Section 2.10 described research on response teams and on crisis coordination. For validation across contexts, these literatures suggest moderators that go beyond staffing and telemetry:

- **Handoff modality.** Written-only handoffs versus overlapping shifts with spoken briefing. The SHA may add more where no spoken briefing occurs.
- **Role structure.** Teams with an explicit incident-lead role and documented transfer of that role versus teams where leadership is informal. Weick's analysis (§2.9.4) suggests role structure affects shared understanding independently.
- **Management metrics.** Teams measured on ticket closure time versus teams measured on post-incident review quality. Rasmussen's account (§2.9.5) predicts that closure-time pressure erodes the time senders invest in handoffs.
- **External parties.** Incidents involving outside responders, where legal privilege and TLP constraints (§2.10.3) limit what a handoff may contain.
- **Language and terminology.** A template's fields presuppose shared meanings for terms like "contained" or "ruled out." Across organizations — and across languages — those meanings can diverge.

Each moderator should enter the transportability memo with a predicted direction derived from the mechanism, and the second-context study should measure at least the ones that differ between the two contexts.

### 6.12 Ecological validity: what simulation leaves out

A simulation can be made realistic in content and still differ from practice in ways that matter for the mechanism:

- **Stakes.** Real incidents carry career and organizational consequences; simulation errors do not. Stress may impair or sharpen comprehension.
- **Interruptions and concurrent work.** Real receivers take over an incident while handling others. A handoff that is read in a quiet simulation may be skimmed in practice.
- **Time scales.** Real investigations span days; simulated ones span an hour. The "expectations" field may age differently.
- **Team history.** Real senders and receivers know each other's reliability; simulation dyads often do not. The reliance literature (§2.11) predicts that known reliability changes how carefully a handoff is read.

None of these invalidates the simulation result. Each is a specific reason the effect could differ in the field, and each suggests a field measure: for example, sampling real handoffs before and after SHA adoption and scoring them for transmitted hypotheses, ruled-out items and gaps — a mechanism measure that does not require judging real decisions. Such a study would test the first link of the causal chain in practice, which is a meaningful contribution even without an outcome measure.

### Common errors and limits

- Calling any second study a "replication" without saying which kind.
- Pooling heterogeneous contexts and reporting the average as the effect.
- Treating a non-significant result in the second context as "failure to replicate" without comparing intervals.
- Attributing an across-context difference to one feature when several differ.
- Running boundary analyses after seeing data and presenting them as predicted.
- Limit: two contexts cannot establish a general boundary; they can only make one more or less plausible.

### Exercises — chapter 6

**EX033 — Modifier analysis.** *Objective:* identify contextual modifiers via mechanism. *Inputs:* the SHA mechanism (Chapter 3 §3.2) and §6.1. *Constraints:* at least six features; each tied to a link in the mechanism. *Steps:* list features, predicted direction, mechanism link and how to measure each. *Expected evidence:* table. *Rubric:* 3 = six or more features with mechanism links and measures; 2 = links weak; 1 = generic list; 0 = none.

**EX034 — Replication type choice.** *Objective:* match replication design to purpose. *Inputs:* three purposes: (a) check whether Chapter 5's result was a chance finding; (b) check whether results depend on the specific Harbor/CTN/LLR-seeded scenarios; (c) test whether telemetry density limits SHA. *Constraints:* justify each choice and name one design element. *Steps:* (1) list what will be held constant and what will vary; (2) choose direct, conceptual or extension replication; (3) justify the choice against the question Chapter 6 must answer. *Expected evidence:* three short paragraphs. *Rubric:* 3 = direct, conceptual, boundary test with sound elements; 2 = one mismatch; 1 = two; 0 = none.

**EX035 — Heterogeneity computation.** *Objective:* compute and interpret heterogeneity. *Inputs:* the script in §6.6. *Constraints:* offline. *Steps:* (1) run and confirm; (2) change KFL to (1.100, 0.250) and rerun; (3) interpret both Q/I² values with the caveat about two contexts. *Expected evidence:* outputs and paragraph. *Rubric:* 3 = correct values and caveated interpretation; 2 = values correct, no caveat; 1 = one value wrong; 0 = none.

**EX036 — Across vs. within evidence.** *Objective:* weigh confounded and unconfounded moderator evidence. *Inputs:* §6.6 results. *Constraints:* 200–300 words. *Steps:* explain why the within-KFL interaction is more diagnostic despite lower precision; propose a design that strengthens it. *Expected evidence:* paragraph. *Rubric:* 3 = explains confounding of across-context comparison, values precision appropriately, proposes stronger within design; 2 = partial; 1 = prefers z-value only; 0 = none.

**EX037 — Revised claim with boundaries.** *Objective:* write a boundary-aware claim. *Inputs:* Chapters 5–6 results. *Constraints:* ≤ 120 words; include scope, effect, boundary and uncertainty. *Steps:* (1) state the population and setting; (2) state the effect with its interval; (3) name the boundary condition and the evidence for it; (4) cut words until every remaining word carries scope or uncertainty. *Expected evidence:* claim. *Rubric:* 3 = scoped, calibrated, boundary as plausible not proven; 2 = one overstatement; 1 = pooled average as claim; 0 = none.

**EX038 — Transportability memo.** *Objective:* apply §6.7. *Inputs:* a third context description. *Constraints:* 400–600 words. *Steps:* follow §6.7. *Expected evidence:* memo. *Rubric:* 3 = features mapped, prediction reasoned through mechanism with uncertainty, minimal check proposed; 2 = prediction without uncertainty; 1 = adoption recommendation without evidence; 0 = none.

### Chapter synthesis

A result from one incident-response context is a hypothesis about others. Testing it in a second context is most informative when the mechanism predicts *where* the effect should change and the prediction is registered before data. In the synthetic Handoff Study, the effect shrank in a dense-telemetry context and, within that context, was concentrated in high-gap scenarios — consistent with telemetry completeness as a boundary condition, though two contexts cannot establish it. Chapter 7 submits the combined claims to adversarial critique.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 08

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Peer critique and revision of claims

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Organize adversarial review of one's own work before submission, including red-team reading and adversarial collaboration.
2. Classify a critique as conceptual, methodological, analytical, reproducibility-related or presentational, and choose the right response.
3. Reproduce a contested analysis under a critic's alternative definition and report both versions.
4. Revise a contribution statement so that it claims exactly what survives critique.
5. Report negative and partial results so that they are useful to others.

Chapters 5 and 6 produced a two-context result with a plausible boundary condition. Before dissemination, those claims must survive people trying to break them. Chapter 8 then assembles what survives into the thesis and its archive.

### 7.1 Why critique is part of the method

Peer review is often experienced as an obstacle after the work is done. In research practice it is better understood as a **method step**: independent critics test whether the inferential chain from observation to claim holds. [Munafò et al. (2017)](https://doi.org/10.1038/s41562-016-0021) list evaluation measures — including pre-publication and post-publication review and the use of independent methodological support — among practices intended to make research more reliable. The [Registered Reports](https://www.cos.io/initiatives/registered-reports) format moves the most consequential review — of question and method — before data collection, so that critique can change the design rather than only the narrative.

Incident-response research needs critique for a specific reason: authors are often close to practice, partner organizations, or the artifact under test. Chapter 1 (§1.3.4) described structural safeguards against conflicted evaluation; critique by people who do not share the author's commitments is another.

### 7.2 Organizing critique before submission

- **Red-team reading.** Ask two or three colleagues to read the thesis chapter or paper *as a hostile reviewer*, with a brief: "Find the weakest link between observations and the main claim." Give them the protocol, deviation log and analysis code, not only the manuscript.
- **Methods review.** Ask a methodologist outside the field to review measurement and analysis; ask a practitioner outside the partner organization to review scenario realism and practical relevance.
- **Reproduction by a third party.** Ask someone to rerun the analysis from the archive (Chapter 8) without help. Every question they ask reveals missing documentation.
- **Adversarial collaboration.** When a critic holds a competing theory (Chapter 2 §2.3), invite them to agree in advance on a test whose outcomes would favor one account or the other. The agreement is recorded before data are examined.
- **Pre-mortem.** Imagine the paper has been retracted two years from now. Write down the most likely reasons. Each reason is a check to perform now.

### 7.3 Classifying critiques

| Critique type | Example in incident-response research | Appropriate response |
|---|---|---|
| Conceptual | "Your outcome measures information transmission, not decision quality." | Clarify construct; possibly redefine outcome or narrow claim. |
| Methodological | "Raters could infer condition from answer format." | Report blinding check; sensitivity analysis; acknowledge limit. |
| Analytical | "Your paired test ignores scenario variation." | Re-analyze with a mixed model; report both. |
| Reproducibility | "I cannot regenerate Table 3 from the archive." | Fix the archive; report the correction. |
| Presentational | "The abstract implies field effectiveness." | Revise wording to match evidence. |
| External validity | "Simulation participants were all volunteers from cooperative teams." | Describe sample; narrow scope; propose replication. |

*In plain terms:* Different critiques need different responses: a measurement critique calls for reanalysis, a scope critique for narrower wording, a misreading for clearer text.

Three responses are always available: **concede** (the critic is right; revise), **defend** (the critic is mistaken; explain why with evidence) and **test** (the question is empirical; run the analysis the critic proposes and report the result). The weakest response is to rephrase without changing anything.

### 7.4 Reproducing contested analyses

When a critic proposes an alternative definition or analysis, the default is to **run it and report it**, unless it is clearly invalid. Report the original preregistered analysis as primary, the critic's analysis as a sensitivity or robustness analysis, and explain any divergence. Never replace the primary analysis silently; never suppress the alternative because it is less favorable. If the alternative analysis reveals that the original claim depended on one contestable choice, the claim should be narrowed.

For the SHA study, a critic might recode errors under a broader definition of projection error; the raw rater sheets kept under §5.4 make that rerun possible.

### 7.5 Worked example: external reviewers challenge the main study's outcome definition

*Synthetic.* An external reviewer of the Handoff Study writes:

> "Your primary outcome counts 'treating missing telemetry as negative evidence' as a comprehension error. But the SHA's T-gaps field *tells* participants which telemetry is missing. Of course they then make fewer such errors. This is not evidence that SHA improves comprehension; it is evidence that participants read the form. What happens to your effect if you exclude gap-misread errors?"

**Classification.** Conceptual and analytical: it challenges whether the outcome measures the construct claimed ("comprehension") and proposes a testable alternative.

**Response plan.** *Partly defend*: transmitting gap information *is* the proposed mechanism (Chapter 3 §3.2, link 4), and receiving responders in real handoffs do misread gaps, so reducing those errors is a legitimate decision-quality improvement. *Partly concede*: the primary outcome bundles gap-misreads with other comprehension and projection errors, so the claim "SHA improves comprehension" may overstate a narrower effect. *Test*: recode the synthetic decisions into gap-misread errors and all other comprehension/projection errors, and report both.

```python
"""Chapter 7 offline lab: recode the Chapter 5 synthetic outcome under a reviewer's alternative definition."""
from itertools import product
from statistics import mean, stdev

# participant: ((standard_gap_misread, standard_other_cp), (sha_gap_misread, sha_other_cp))
SPLIT = {
    "P01": ((2, 3), (0, 3)), "P02": ((1, 3), (1, 3)), "P03": ((2, 4), (0, 3)),
    "P04": ((1, 2), (0, 2)), "P05": ((3, 4), (1, 3)), "P06": ((1, 3), (0, 3)),
    "P07": ((1, 4), (1, 4)), "P08": ((2, 4), (1, 3)), "P09": ((0, 2), (0, 2)),
    "P10": ((2, 3), (0, 2)), "P11": ((1, 3), (0, 3)), "P12": ((2, 4), (1, 4)),
}
T_CRIT_DF11 = 2.201

def summarize(label, d):
    m, s = mean(d), stdev(d)
    h = T_CRIT_DF11 * s / len(d) ** 0.5
    obs = abs(sum(d))
    p = sum(1 for sg in product((1, -1), repeat=len(d))
            if abs(sum(x * y for x, y in zip(d, sg))) >= obs) / 2 ** len(d)
    print(f"{label:28s} mean_diff={m:.3f} 95%CI=({m - h:.3f}, {m + h:.3f}) exact_p={p:.4f}")

if __name__ == "__main__":
    total = [sum(s) - sum(h) for s, h in SPLIT.values()]
    gap = [s[0] - h[0] for s, h in SPLIT.values()]
    other = [s[1] - h[1] for s, h in SPLIT.values()]
    summarize("original outcome (all c+p)", total)
    summarize("gap-misread errors only", gap)
    summarize("other c+p errors only", other)
    print(f"share of reduction from gap-misreads: {sum(gap) / sum(total):.2f}")
```

Expected output (verified with Python 3):

```text
original outcome (all c+p)   mean_diff=1.417 95%CI=(0.677, 2.157) exact_p=0.0039
gap-misread errors only      mean_diff=1.083 95%CI=(0.580, 1.587) exact_p=0.0039
other c+p errors only        mean_diff=0.333 95%CI=(0.020, 0.646) exact_p=0.1250
share of reduction from gap-misreads: 0.76
```

**Interpretation.** About three-quarters (0.76) of the reduction comes from gap-misread errors. The reduction in other comprehension and projection errors is small (0.33 over three scenarios, about 0.11 per scenario). Its *t*-interval barely excludes zero, while the exact sign-flip test gives p = 0.125 — with only four non-zero differences out of twelve, the evidence for any broader effect is weak and method-dependent. The reviewer's challenge therefore changes the claim substantially.

**Revised contribution statement.**

| Version | Statement |
|---|---|
| Before critique | "SHA improves receiving responders' comprehension and projection under incomplete telemetry." |
| After critique | "SHA reduces receiving responders' errors of misreading missing telemetry as negative evidence, by explicitly transmitting known telemetry gaps. Evidence that it improves other aspects of comprehension or projection is weak in our data." |

*In plain terms:* The claim got smaller and more precise after critique; that is a gain, because practitioners now know where it applies.

The revised claim is narrower and more useful: it tells practitioners exactly what the artifact does, and it tells researchers which part of the original mechanism (ruled-out hypotheses, expectations) remains untested. The response letter thanks the reviewer, reports the new analysis, and revises abstract, discussion and conclusions accordingly.

### 7.6 Negative and partial results

A negative result — no effect, or an effect smaller than the SEOI — is informative when the study was adequately powered, measured validly and preregistered. Chapter 3's failure conditions (F3–F6) were written to make such results interpretable. Report them with the same structure as positive results: estimate, interval, relation to SEOI, mechanism checks and limitations. Distinguish clearly between "evidence of absence" (a precise null excluding the SEOI) and "absence of evidence" (an imprecise result). Archive negative results even if a venue declines them; Chapter 8's archive is designed to hold them.

### 7.7 Writing the response to reviewers

A good response document has, for each comment: the comment quoted; the classification; the response (concede, defend, test); what changed, with locations; and any new analysis, with code and output referenced. Keep the tone factual. Where you defend, give evidence, not assertion. Where you concede, do not hedge the revision into meaninglessness.

Suppose a reviewer argues that the SEOI of 0.5 errors per scenario was chosen to make the study feasible. The response quotes the cost–benefit anchoring from §3.13, reports the precision the sample actually achieved and, if the reviewer is right, narrows the claim. Each response names the page or file where the change can be checked.

### 7.8 Post-publication critique and correction

Critique continues after publication. If an error is found — a coding mistake, an archive that does not reproduce a table, a misdescribed sample — correct it publicly, through the venue's correction process and in the archive's change log. Corrections are an integrity strength. A thesis should state how readers can report problems and how corrections will be handled (Chapter 8).

For the SHA study, a correction might concern a scenario whose error count was mis-adjudicated. The change log would record the old and new values, the script that recomputes the primary estimate and whether the interval's relation to the SEOI changed.

### 7.9 Critique as structured adversarial review

Section 7.2 described organizing critique before submission. At doctoral level it helps to treat internal critique as a designed activity with roles, inputs and outputs, much like a red-team exercise in security.

**Roles.** Assign at least three critics with different vantage points: a methodologist (design, measurement, statistics), a practitioner (realism of scenarios, plausibility of the mechanism, operational cost), and an ethicist or data steward (consent, data handling, dual use). Ask each to produce their strongest objections independently before any discussion, to avoid convergence on the first objection voiced.

**Inputs.** Give critics the protocol, the pre-registration, the analysis code, the de-identified data or synthetic fixture, and the draft results — but ask the methodologist to read the protocol and code *before* the results, so that critique of the design is not shaped by the findings.

**Outputs.** A numbered objection list, each with a type (§7.3), severity (would it change the main claim, a secondary claim, or only wording?), and a suggested test. The candidate then responds in the format of §7.7, as if to a journal.

The practice exploits a finding already discussed in Chapter 5: [Silberzahn et al. (2018)](https://doi.org/10.1177/2515245917747646) showed that independent analysts given the same data and question can reach materially different estimates through reasonable choices. A critic who reanalyzes the data independently, without seeing the candidate's code, is a one-person version of that design. If their estimate agrees, robustness is demonstrated; if not, the discrepancy localizes a fragile choice.

### 7.10 Common critiques of incident-response studies and how strong responses look

Experience with security user studies and with the pitfalls catalogued by [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) suggests a recurring set of critiques. Anticipating them is cheaper than answering them after review.

| Critique | Weak response | Strong response |
|---|---|---|
| "Students are not real responders." | "Students are a common sample in this field." | Report experience stratification; show the effect (or its absence) in the experienced stratum; narrow the claim to the population sampled. |
| "Scenarios were written to favor the SHA." | "Scenarios were realistic." | Scenarios written or reviewed by practitioners blind to hypotheses; per-scenario effects reported; a scenario where the SHA was predicted not to help included as a negative control. |
| "Raters could tell the condition." | "Raters were instructed not to guess." | Report a blinding check: raters guessed condition, and their accuracy was compared with chance. |
| "The effect is just longer handoffs." | "The template is more complete by design." | Present the length-matched comparison or the labeled mediation analysis (§3.14). |
| "Lab results do not transfer to operations." | "Future work will address this." | Present the second-context result, the COG statement and the prediction interval (Chapter 6). |
| "The metric does not capture what matters in practice." | "The metric was validated." | Show the construct-validity evidence (§3.12) and the practitioner-elicited SEOI. |
| "The study ignores organizational pressure." | Silence. | Concede; state it as a boundary; point to the moderator list in §6.11. |

*In plain terms:* Weak responses defend; strong responses show evidence or narrow the claim. The left column is predictable enough that a candidate can prepare the right column before submission.

The blinding check in the third row is inexpensive and seldom reported. After rating, ask each rater to guess the condition for each decision. If guessing accuracy is near chance, blinding held. If it is well above chance, report it and examine whether rater scores differ between correctly and incorrectly guessed items.

### 7.11 When critique concerns unfalsifiable claims

[Herley and van Oorschot (2017)](https://doi.org/10.1109/SP.2017.38) criticized parts of security research for claims that cannot be refuted by any observation. A thesis is vulnerable to this critique whenever its claims are hedged so heavily that no result could contradict them — for example, "structured handoffs can improve situational understanding in some contexts." The repair is to restore content: state the population, the outcome, the expected size, and the result that would count against the claim. Paradoxically, a more falsifiable claim is more defensible, because reviewers can see exactly what evidence supports it.

A useful self-test: for each claim in the abstract, write down an observation that would show it to be false. If none exists, the claim is not yet scientific; if the observation is one the study could have made and did not, the claim needs that study.

### 7.12 Registered reports and pre-publication review of design

Section 7.8 discussed correction after publication. The complementary approach moves critique earlier. Under the registered-report model described by the [Center for Open Science](https://www.cos.io/initiatives/registered-reports), a study's introduction, methods and analysis plan are peer reviewed before data are collected, and a journal can commit in principle to publish the results if the protocol is followed. For a doctoral program, the same logic can be applied internally: the committee reviews and signs off the protocol, which then becomes the standard against which the final analysis is checked. Critique received at that stage changes the design rather than requiring the candidate to defend a flawed one.

The candidate should record how protocol-stage critique changed the design, because examiners value evidence that critique was used, and because it distinguishes design changes made before data from those made after.

### 7.13 Responding to practitioner critique

Incident-response research has two audiences: researchers and practitioners. Practitioner critique often arrives in a different register — "this would never work on a night shift with three people" — and is easy to dismiss as anecdote. It should instead be translated into a testable claim about a moderator or a boundary: *with staffing below some level, senders lack time to complete the SHA, and completeness drops.* That claim can be checked in field data (completeness of SHA fields by staffing level) or added to the transportability memo. Translating critique into hypotheses respects the critic and strengthens the thesis.

When practitioner and researcher critiques conflict — a methodologist wants more control, a practitioner wants more realism — the conflict is usually a trade-off between internal and external validity. The candidate's job is not to satisfy both but to state which the study prioritized, why, and what the follow-up study would prioritize instead.

### 7.14 Critique of AI-assisted extensions

If the thesis includes or proposes model-assisted handoffs (§3.15), anticipate critiques specific to that component:

- **Version dependence.** Results may not hold for later model versions. Record the exact version and settings; present results as conditional on them.
- **Benchmark contamination.** Public scenarios similar to the evaluation set may have appeared in a model's training data. Use privately written scenarios and say so.
- **Evaluation by another model.** If a model was used to score outputs, critics will ask how its scores relate to human judgment. Report agreement on a human-rated subset, or avoid model-based scoring for primary outcomes.
- **Reliance effects.** The reliance literature ([Parasuraman and Manzey, 2010](https://doi.org/10.1177/0018720810376055); [Lee and See, 2004](https://doi.org/10.1518/hfes.46.1.50_30392)) predicts over-reliance; reviewers will ask whether the design included model errors. If not, the claim must be limited to cases where the model is correct, which is not a deployable claim.

### Common errors and limits

- Treating reviewers as opponents to be persuaded rather than as tests to pass.
- Replacing the primary analysis with a critic's alternative, or ignoring the alternative.
- Revising wording without changing claims.
- Calling an imprecise null "no effect."
- Asking only friendly colleagues for review.
- Limit: critique cannot rescue a study whose raw data or design are inadequate; it can only reveal that.

### Exercises — chapter 7

**EX039 — Pre-mortem.** *Objective:* anticipate failure. *Inputs:* the Handoff Study as of Chapter 6. *Constraints:* at least six plausible retraction or major-correction reasons. *Steps:* list reasons; for each, name the check that would detect it now. *Expected evidence:* table. *Rubric:* 3 = six or more specific reasons with concrete checks; 2 = some generic; 1 = vague; 0 = none.

**EX040 — Critique classification and response.** *Objective:* respond appropriately. *Inputs:* five synthetic reviewer comments: (a) "Raters could tell SHA answers by their bullet format"; (b) "You should use a mixed model"; (c) "The abstract says 'responders' but participants were volunteers from two teams"; (d) "I could not run your analysis: missing file `decisions_v3.csv`"; (e) "Situation awareness theory is outdated." *Constraints:* classify each and choose concede, defend or test. *Steps:* (1) classify each critique using §7.3; (2) decide accept, partially accept or rebut; (3) name the analysis or text change that follows; (4) draft the reply. *Expected evidence:* table with response drafts. *Rubric:* 3 = correct classifications and proportionate responses, (e) answered with evidence about predictions, not dismissal; 2 = one weak; 1 = defensive throughout; 0 = none.

**EX041 — Contested analysis.** *Objective:* reproduce a critic's alternative. *Inputs:* the script in §7.5. *Constraints:* offline. *Steps:* run; then compute the effect on gap-misread errors as a share of the standard condition's gap-misreads (relative reduction); write 150 words on what the alternative analysis does and does not show. *Expected evidence:* outputs, relative reduction and paragraph. *Rubric:* 3 = exact outputs, relative reduction correct (≈ 0.72), balanced interpretation; 2 = outputs correct, interpretation one-sided; 1 = one value wrong; 0 = none.

**EX042 — Revised contribution statement.** *Objective:* narrow a claim honestly. *Inputs:* Chapters 5–7 results. *Constraints:* ≤ 150 words; integrate the boundary from Chapter 6 and the narrowing from §7.5. *Steps:* (1) quote the Chapter 3 contribution statement; (2) mark each phrase that later evidence weakened; (3) rewrite with the narrowed scope; (4) add one sentence saying what was dropped and why. *Expected evidence:* statement. *Rubric:* 3 = narrowed to gap-misread mechanism, boundary noted, untested elements named; 2 = one omission; 1 = unchanged; 0 = none.

**EX043 — Negative result report.** *Objective:* report a null usefully. *Inputs:* suppose the KFL direct replication had found −0.05 (95% CI −0.40 to 0.30) per three scenarios. *Constraints:* use SEOI 1.5 per three scenarios. *Steps:* classify (evidence of absence or absence of evidence); write a 150-word results paragraph; state the implication for the claim. *Expected evidence:* paragraph. *Rubric:* 3 = precise null correctly identified, claim implications drawn; 2 = classification right, implications thin; 1 = "failed to replicate" only; 0 = none.

**EX044 — Response letter excerpt.** *Objective:* write a professional response. *Inputs:* the reviewer comment in §7.5. *Constraints:* 250–400 words; include classification, response, changes and new analysis. *Steps:* (1) quote the reviewer point verbatim; (2) answer in one sentence; (3) give the evidence and its location; (4) state the manuscript change, with page or section. *Expected evidence:* letter excerpt. *Rubric:* 3 = partly defend, partly concede, test reported, concrete changes listed; 2 = no concrete changes; 1 = purely defensive; 0 = none.

### Chapter synthesis

Critique is the method step that tests the chain from observation to claim with people who do not share the author's commitments. Organized red-team reading, third-party reproduction and adversarial collaboration find weaknesses before publication; concede, defend or test are the honest responses. In the Handoff Study, a reviewer's challenge to the outcome definition showed that most of the effect came from transmitting telemetry gaps, and the contribution was narrowed accordingly. Chapter 8 assembles the narrowed claim, its evidence and its artifacts into a thesis and reproducibility archive.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 08

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Thesis synthesis and reproducibility archive

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Structure a thesis as an argument whose main claim is traceable to evidence, qualifications and answered objections.
2. Assemble a reproducibility archive with documented provenance, integrity manifests, permissions and release tiers.
3. Write a data-governance plan covering access, retention, destruction and correction after the thesis is submitted.
4. State limitations and future work precisely enough to guide the next researcher.
5. Prepare a defense that anticipates the strongest objections.

This chapter integrates the whole book. Chapter 1's integrity and reproducibility standards become the archive's requirements; Chapters 2–7 supply the content of the argument. The learner leaves with a thesis whose claims are exactly as strong as its evidence.

### 8.1 The thesis as an argument

A doctoral thesis is not a report of everything done; it is an **argument** that a contribution is warranted. A classic model of practical argument, associated with the philosopher Stephen Toulmin, distinguishes a **claim**, the **grounds** (evidence) offered for it, the **warrant** connecting grounds to claim, **backing** for the warrant, a **qualifier** expressing strength, and **rebuttals** (conditions under which the claim would not hold). The model is useful here because it maps directly onto this book's vocabulary:

| Argument element | Handoff Study example | Source chapter |
|---|---|---|
| Claim | SHA reduces gap-misread errors by receiving responders. | Ch. 7 (revised) |
| Grounds | Within-subject simulation results at NMS; replication and gap interaction at KFL; subtype analysis. | Ch. 5–7 |
| Warrant | Blinded expert coding of decisions against information available at each decision point validly measures decision errors. | Ch. 1 §1.6; Ch. 5 §5.1 |
| Backing | Rater agreement; blinding check; pilot realism ratings; reproduced baselines. | Ch. 4–5 |
| Qualifier | "In simulation; where telemetry is sparse; effect size uncertain relative to SEOI." | Ch. 5–6 |
| Rebuttals | Dense telemetry; responders who already convey gaps; harms not excluded; field effectiveness untested. | Ch. 6–7 |

*In plain terms:* The thesis is one argument: a claim, the evidence for it, the reason the evidence supports it, and the limits — each traceable to a chapter.

The thesis chapters should follow the argument, not the chronology of the project. A reader should be able to find, for any sentence in the conclusion, the grounds, warrant and qualifiers that support it.

### 8.2 Integrating failures and narrowed claims

Doctoral work rarely ends with the claim it started with. The Handoff Study began with "SHA improves comprehension and projection" and ended with "SHA reduces gap-misread errors where telemetry is sparse." That trajectory is a strength when it is documented: the thesis should show the original claim, the evidence and critique that narrowed it, and the final claim. Hiding the trajectory invites the suspicion that the final claim was chosen after the fact (Chapter 1's HARKing). A **claim-evolution table** in the introduction or conclusion makes the trajectory explicit:

| Stage | Claim | What changed it |
|---|---|---|
| Proposal (Ch. 3) | SHA reduces comprehension and projection errors, not perception errors. | — |
| Main study (Ch. 5) | Effect present; practical importance uncertain; harms not excluded. | Interval includes SEOI; harms interval. |
| Second context (Ch. 6) | Effect smaller where telemetry is dense; boundary plausible. | KFL results; within-context interaction. |
| Critique (Ch. 7) | Effect mainly on gap-misread errors. | Reviewer's outcome challenge; subtype analysis. |

*In plain terms:* The claim narrowed at each stage, and every narrowing has a cited cause; that trail is what makes the final claim credible.

### 8.3 The reproducibility archive

The archive is the thesis's evidence made inspectable. It implements the tiered plan from Chapter 1 (§1.4.5) and should be designed to answer a reviewer's question: *"Can I verify each number, and if not, why not?"*

#### 8.3.1 Structure

```text
handoff-study-archive/
  README.md                 # what is here, how to run, what is NOT here and why
  CITATION.cff              # how to cite the archive (optional but useful)
  LICENSES.md               # licenses per component (text, code, data)
  PERMISSIONS.md            # permissions register: what each partner/participant allowed
  MANIFEST.sha256           # integrity manifest for every file
  protocol/                 # protocol versions, preregistrations, deviation log, pilot report
  instruments/              # SHA template, scenarios, codebook, rater training, consent forms (blank)
  data/
    synthetic/              # schema-matched synthetic data for running the pipeline (T1)
    aggregate/              # released aggregates with suppression notes (T2)
    restricted/README.md    # description of restricted data and access procedure (T3/T4); no data
  code/                     # analysis scripts, environment lock file, run log
  results/                  # outputs regenerated by code, with hashes
  review/                   # reviewer comments and responses, red-team notes, reproduction reports
  CHANGELOG.md              # corrections after release
```

#### 8.3.2 Provenance and FAIR metadata

Every dataset needs a provenance record: source, permission, collection dates, transformations (with scripts), version and hash. Even restricted data can follow the [FAIR principles](https://doi.org/10.1038/sdata.2016.18) at the metadata level: the restricted dataset's *description* can be findable (indexed in a repository with a persistent identifier), its access procedure *accessible* (documented), its schema *interoperable* (standard formats and a data dictionary) and its terms *reusable* (clear conditions). FAIR does not require that the data themselves be open.

#### 8.3.3 Licenses and rights

Use explicit licenses per component. In this repository, original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); a thesis archive may choose differently. Data released under a data-use agreement must not be relicensed openly. Cited works retain their own rights. Consent forms determine what participant data can ever be released; the permissions register records those limits so that later archive maintainers do not exceed them.

#### 8.3.4 Integrity

A cryptographic hash manifest lets anyone verify that files have not changed since release. The [technical book's](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md#ch-11) record-integrity chapter covers the operational use of digests; in an archive, the manifest is regenerated at each release and recorded in the change log.

### 8.4 Data governance after submission

Governance continues after the defense. The plan should specify:

- **Custodian.** Who is responsible for restricted data after the candidate leaves the program.
- **Access procedure.** How a qualified researcher requests restricted data or enclave access; who decides; what agreements are required.
- **Retention and destruction.** How long restricted data are kept, as permitted by the data-use agreement and consent, and how destruction is verified and recorded.
- **Re-identification response.** What happens if someone reports that released data can be re-identified: withdraw the release, notify affected parties as required, and record the event.
- **Corrections.** How errors are reported and corrected (Chapter 7 §7.8), with change-log entries and, where applicable, notices through the publication venue.

### 8.5 Limitations and future work

A limitations section is not a list of apologies. Each limitation should state **what it limits** (which claim), **in what direction** it could bias results (if known), and **what would resolve it**. For the Handoff Study:

| Limitation | Affected claim | Possible direction | Resolution |
|---|---|---|---|
| Simulation, not field incidents | Any claim about real response | Unknown; simulation may exaggerate or understate | Field study with consenting teams under Chapter 1 authorization |
| Volunteer participants from two organizations | External validity | Likely favorable (motivated volunteers) | Recruitment from more organizations; non-volunteer sampling |
| Gap-misread outcome aligned with T-gaps field | Construct breadth | Inflates breadth of comprehension claim (now narrowed) | Test ruled-out-hypotheses and expectation fields separately |
| Two contexts only | Boundary condition | Cannot separate telemetry from other context features | More contexts; within-context manipulation at multiple sites |
| Harms imprecisely estimated | Safety | Small increase not excluded | Larger study with harms as co-primary |

*In plain terms:* Each limitation is tied to the claim it weakens and to the study that could resolve it; this is the honest source of future work.

**Future work** follows from the limitations and the untested parts of the mechanism. It should be specific enough that another researcher could begin: name the question, the design and the first falsifying observation.

### 8.6 Preparing the defense

A defense tests whether the candidate understands the limits of their own work. Preparation:

1. **Objection inventory.** Collect every serious objection from reviewers, red-team readers and the pre-mortem (Chapter 7). For each, prepare a short answer with evidence and a slide or reference location.
2. **Strongest-objection rehearsal.** Ask a colleague to argue the strongest case against the main claim; answer without defensiveness.
3. **Archive walkthrough.** Be ready to show, live, how a reported number is regenerated from the archive.
4. **Scope discipline.** Practice answering "Does SHA improve incident response?" with the claim as actually supported, not the claim one wishes were supported.

### 8.7 Worked example: the study protocols, synthetic datasets, analysis code and reviewer exchanges

*Synthetic.* The candidate assembles the Handoff Study archive. The script below builds a miniature version in a temporary directory, writes an integrity manifest, verifies it, then simulates an unrecorded edit to the deviation log and shows that verification detects it. It writes nothing outside the temporary directory, which is deleted when the script ends.

```python
"""Chapter 8 offline lab: build and verify a hash manifest for a synthetic thesis archive.
Writes only inside a temporary directory that is deleted afterwards."""
import hashlib, tempfile
from pathlib import Path

FILES = {
    "protocol/protocol_v1.2.md": "Handoff Study protocol v1.2 (synthetic)\n",
    "protocol/deviation_log.csv": "id,date,description,outcome_seen\nD01,2026-03-02,P10 prior exposure,yes\n",
    "data/synthetic/decisions_schema.json": '{"participant": "str", "condition": "str", "errors": "int"}\n',
    "code/ch05_analysis.py": "print('analysis placeholder')\n",
    "PERMISSIONS.md": "T3 decision data: released under data-use agreement only.\n",
}

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def build(root):
    for rel, text in FILES.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))  # bytes: identical hashes on every OS
    lines = [f"{sha256(root / rel)}  {rel}" for rel in sorted(FILES)]
    (root / "MANIFEST.sha256").write_bytes(("\n".join(lines) + "\n").encode("utf-8"))
    return lines

def verify(root):
    bad = []
    for line in (root / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        if sha256(root / rel) != digest:
            bad.append(rel)
    return bad

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for line in build(root):
            print(line[:16] + "...  " + line.split("  ", 1)[1])
        print("verify (untouched):", verify(root) or "all match")
        (root / "protocol/deviation_log.csv").write_bytes(b"id,date,description,outcome_seen\n")
        print("verify (after edit):", verify(root))
```

Expected output (verified with Python 3; files are written as bytes so the digests are identical on every operating system):

```text
5b99143807791992...  PERMISSIONS.md
56a6b195fb7d31dc...  code/ch05_analysis.py
97d916df3e33a455...  data/synthetic/decisions_schema.json
73a36f3f76dd754b...  protocol/deviation_log.csv
419c6fe74043bbaa...  protocol/protocol_v1.2.md
verify (untouched): all match
verify (after edit): ['protocol/deviation_log.csv']
```

**Interpretation.** A manifest makes silent changes visible. The edit to the deviation log — the very file that records departures from protocol — is detected immediately. In a real archive, any legitimate change produces a new release with a regenerated manifest and a change-log entry explaining it.

The candidate's README states plainly: "This archive lets you run every analysis on schema-matched synthetic data and regenerate every reported aggregate from released aggregate files. Participant-level decision data are available only under a data-use agreement, as permitted by participants' consent (see PERMISSIONS.md). No incident records from any organization were used. Scenario materials are synthetic and derived from the OpenCyber Academy Harbor Library, Cedar Training Network and Lumen Library Reservations teaching cases."

### 8.8 Practical activity: archive audit

Ask a colleague who has not worked on the project to audit the archive using only its README. They should record: whether they could run the pipeline; whether each reported number could be regenerated or was explained as restricted; whether licenses and permissions were clear; and every question they had to ask. Each question becomes a documentation fix before release.

For the SHA archive, the decisive test is whether the primary estimate can be regenerated from hashed raw rater sheets by script, and whether restricted items such as consented session recordings are explained rather than silently missing.

### 8.9 A specimen archive layout with documentation

Section 8.3.1 described the structure of the reproducibility archive. This section gives a fuller specimen for the Handoff Study, combining the reproducibility rules of [Sandve et al. (2013)](https://doi.org/10.1371/journal.pcbi.1003285), the documentation formats of [Gebru et al. (2021)](https://doi.org/10.1145/3458723) and [Mitchell et al. (2019)](https://doi.org/10.1145/3287560.3287596), and the FAIR principles of [Wilkinson et al. (2016)](https://doi.org/10.1038/sdata.2016.18).

```text
handoff-study-archive/
  README.md                 entry point: what, how to run, what is missing and why
  LICENSE-code              e.g., an OSI-approved license for code
  LICENSE-docs              e.g., a Creative Commons license for text and synthetic data
  CITATION.cff              how to cite the archive
  MANIFEST.sha256           hash of every file (Chapter 8 lab)
  protocol/
    protocol_v1.0.pdf       as approved by the ethics board
    protocol_changes.md     every amendment with date, reason, and before/after
    preregistration.pdf     time-stamped registration
  materials/
    scenarios/              scenario scripts (synthetic; safe to share)
    sha_template.md         the artifact itself
    rater_rubric.md         scoring rubric with worked examples
    expert_panel.md         defensible-option elicitation procedure and dropped points
  data/
    DATASHEET.md            datasheet: collection, composition, labeling, known shifts, uses
    synthetic/              fixture with the same schema as the restricted data
    restricted/ACCESS.md    how qualified researchers can request access; no data here
  analysis/
    environment.lock        exact versions of interpreter and packages
    run_all.sh              one command: fixture → every number in the thesis
    primary.py, secondary.py, multiverse.py, metaanalysis.py
    outputs/                generated tables and figures with the commit that produced them
  critique/
    internal_review.md      objection list and responses (Chapter 7)
    reviewer_letters/       journal exchanges, with permission
  governance/
    data_management_plan.md roles, retention, destruction, access decisions
    incident_log.md         any data incidents involving study data
```

Three choices in this specimen deserve justification.

**A separate restricted-access path.** The restricted decision data cannot be published. The archive therefore states exactly what exists, who holds it, and under what conditions it can be accessed, and it provides a synthetic fixture with the same schema so that `run_all.sh` executes end to end. This places the archive at a defined point on Peng's spectrum ([Peng, 2011](https://doi.org/10.1126/science.1213847)): code and synthetic data are fully executable; the real data are findable and accessible under conditions, satisfying the "F" and conditional "A" of FAIR without violating consent.

**Changes as first-class files.** `protocol_changes.md` turns deviations into documentation. A reader comparing the pre-registration with the final analysis should not need to infer differences.

**Critique in the archive.** Including the internal objection list and reviewer exchanges is unusual but valuable: it lets future researchers see which threats were raised and how they were addressed, which is part of the evidence for the claim.

### 8.10 Long-term stewardship of incident-research data

Incident-research data often outlive the doctoral project and remain sensitive. Section 8.4 listed the elements of a governance plan. In practice, three failure patterns recur:

1. **Orphaned data.** The candidate graduates; the restricted data remain on a departmental server with no steward. Requests go unanswered, or worse, access controls lapse. Remedy: name a steward by role (not only by person), with a successor, in the data management plan.
2. **Consent drift.** Later researchers request the data for purposes the original consent did not cover. Remedy: record the consent scope in machine-readable form in `ACCESS.md` and require requesters to state their purpose against it.
3. **Re-identification risk growth.** Data de-identified in one year may become re-identifiable as auxiliary data accumulate — the lesson of [Narayanan and Shmatikov (2008)](https://doi.org/10.1109/SP.2008.33) and [Sweeney (2002)](https://doi.org/10.1142/S0218488502001648) discussed in Chapter 1. Remedy: schedule periodic re-assessment and retain the authority to withdraw or further restrict access.

Retention should be set by the consent terms and institutional policy, not by convenience. When the retention period ends, destruction should be logged in `incident_log.md` or a governance log, with the manifest updated to show which files no longer exist.

### 8.11 Writing the thesis for two audiences

A thesis is examined by researchers but read, if it is useful, by practitioners. The research audience needs the argument (§8.1), the evidence and its limits. The practitioner audience needs to know what to do differently, under what conditions, and at what cost. A short **practitioner summary** — two pages, written after the thesis is complete — should state:

- The claim in operational terms ("for shift handoffs during multi-day investigations with incomplete telemetry…").
- The size of the expected benefit and its range for a new organization (the prediction interval of §6.10, not only the average).
- The cost (sender time per handoff) and the known risks (no evidence of increased harmful actions within the declared margin; untested for cross-organization handoffs).
- How to evaluate adoption locally — for example, by sampling handoffs before and after adoption and scoring them for transmitted hypotheses and gaps (§6.12).

Writing the practitioner summary is also a test of the thesis: if the summary cannot be written without overstating, the thesis's claims may be overstated too.

### 8.12 The defense as a final critique round

The defense is the last structured critique before the claim enters the literature. Preparing for it reuses the materials of earlier chapters:

- The **objection inventory** (EX050) draws on the critique table in §7.10, the limitation table in §8.5 and the rival-account table in §3.14.
- The **claim-evolution table** (EX046) shows examiners that narrowing was evidence-driven.
- The **archive** lets an examiner verify any number on the spot: "which script produced Table 5.3?" should be answerable by pointing to a file and commit.

Expect examiners to probe the joints of the argument where theory meets measurement: whether rater-scored errors measure situation awareness in Endsley's sense ([Endsley, 1995](https://doi.org/10.1518/001872095779049499)), whether expert decision processes described by naturalistic decision-making research ([Klein, 2008](https://doi.org/10.1518/001872008X288385)) were represented in the sample, and whether the prediction interval supports any adoption recommendation. The candidate who has already written these answers into the thesis will find the defense a discussion rather than an interrogation.

### 8.13 What remains open in incident-response science

A doctoral thesis ends with future work; a book on doctoral research in incident response can end with the field's open questions, as they appear from the literature reviewed here.

1. **Valid, shareable outcome measures.** The field lacks widely accepted measures of response decision quality that can be used across organizations without exposing sensitive data.
2. **Cross-organizational coordination evidence.** Crisis-management research ([Comfort, 2007](https://doi.org/10.1111/j.1540-6210.2007.00827.x)) and command-system research ([Bigley and Roberts, 2001](https://doi.org/10.2307/3069401)) offer frameworks; controlled evidence about cyber-incident coordination across organizations is scarce.
3. **Human–AI response teams.** The reliance literature predicts misuse and disuse; incident-response studies that measure both, with seeded model errors and long time horizons, are rare.
4. **Longitudinal and field evidence.** Most controlled evidence is from single-session simulations. Studies that follow an intervention through months of operation, even with weaker designs, would test whether simulation effects persist.
5. **Theory that makes risky predictions.** The traditions in §2.9 provide candidate mechanisms; few security studies test them against each other. Designs that discriminate among accounts would turn the field's growing empirical base into cumulative knowledge.

Each of these is a thesis-sized problem. A candidate who finishes the Handoff Study is well placed to start the next one.

### Common errors and limits

- Organizing the thesis chronologically rather than as an argument.
- Presenting only the final claim and hiding how it was narrowed.
- An archive that contains code but no description of what is missing and why.
- Relicensing restricted data or participant material beyond consent.
- No custodian or access procedure after the candidate leaves.
- Limitations listed without affected claims or resolution paths.
- Limit: this chapter describes archive practice in general terms; specific repositories, identifiers and institutional requirements must be checked at the time of deposit.

### Exercises — chapter 8

**EX045 — Argument map.** *Objective:* map the thesis argument. *Inputs:* the Handoff Study's final claim. *Constraints:* use all six argument elements in §8.1; each element cites a chapter section. *Steps:* (1) write the final claim; (2) fill grounds, warrant, backing, qualifier and rebuttal in a table; (3) attach a chapter section to each cell; (4) mark any cell whose backing is weaker than the claim needs. *Expected evidence:* argument table. *Rubric:* 3 = complete, traceable, qualifiers and rebuttals honest; 2 = one element weak; 1 = claim and grounds only; 0 = none.

**EX046 — Claim-evolution table.** *Objective:* document narrowing. *Inputs:* Chapters 3–7. *Constraints:* at least four stages; each change linked to specific evidence. *Steps:* (1) extract the claim as stated in Chapters 3, 5, 6 and 7; (2) tabulate them in order; (3) for each change, cite the result that caused it; (4) write the explanation. *Expected evidence:* table and 100-word explanation of why the trajectory strengthens the thesis. *Rubric:* 3 = complete with evidence links and a sound explanation; 2 = missing a stage; 1 = no evidence links; 0 = none.

**EX047 — Archive README.** *Objective:* write an honest archive entry point. *Inputs:* the structure in §8.3.1. *Constraints:* 300–500 words; include run instructions, what is not included and why, licenses, permissions and how to report problems. *Steps:* (1) list the archive's top-level folders; (2) write a quick-start command sequence and test it; (3) list every excluded item with the reason; (4) add licenses, permissions and a contact route. *Expected evidence:* README. *Rubric:* 3 = a stranger could run it and understand every gap; 2 = one element missing; 1 = code-only README; 0 = none.

**EX048 — Manifest lab.** *Objective:* verify integrity. *Inputs:* the script in §8.7. *Constraints:* offline. *Steps:* (1) run and confirm the output; (2) modify the script so that it also detects a file *added* after the manifest was built (e.g., `data/synthetic/extra.csv`); (3) run and record the output. *Expected evidence:* modified code and output. *Rubric:* 3 = detects added files without false positives on the manifest itself, outputs recorded; 2 = detects but flags the manifest; 1 = not working; 0 = none.

**EX049 — Data-governance plan.** *Objective:* plan post-submission stewardship. *Inputs:* the Handoff Study's restricted decision data. *Constraints:* cover the five elements of §8.4. *Steps:* (1) inventory the restricted data and its consent terms; (2) assign a steward and a successor; (3) define access, retention and destruction procedures; (4) define how requests and incidents involving the data are handled. *Expected evidence:* one-page plan. *Rubric:* 3 = named roles, concrete procedures and retention consistent with consent; 2 = one element vague; 1 = generic; 0 = none.

**EX050 — Defense objection inventory.** *Objective:* prepare for the strongest objections. *Inputs:* the whole book. *Constraints:* at least eight objections spanning integrity, measurement, external validity, ethics and reproducibility. *Steps:* list each objection, a short evidence-based answer and the location of supporting material. *Expected evidence:* inventory. *Rubric:* 3 = eight or more serious objections with honest answers, including concessions; 2 = some answers defensive; 1 = trivial objections; 0 = none.

### Chapter synthesis

A thesis in incident-response research is an argument whose claims are exactly as strong as their evidence, with the narrowing of those claims documented rather than hidden. Its reproducibility archive makes the evidence inspectable within legal and ethical limits, with provenance, integrity manifests, explicit permissions and a plan for stewardship after submission. The Handoff Study ends with a narrow, useful and honest claim, an archive that a stranger can audit, and a list of future studies that begin where its limits do. That is the standard this book has aimed to teach.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 08

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

Each worked result shows one defensible answer and explains what the rubric rewards. Alternative answers can earn full credit when they meet the same standard of evidence, scope and honesty about limits.

### Chapter 1: EX001–EX007

**EX001 — Model claim ladder audit.**

| # | Statement | Label | Hidden assumption | Defeating observation |
|---|---|---|---|---|
| 1 | At 02:14 the EDR console showed `powershell.exe` launched by `winword.exe` on FIN-22. | Observation (L1), if the console record is preserved with its clock state. | EDR clock accurate; parent–child relation recorded by the agent, not inferred by the console. | EDR clock offset; parent PID reuse. |
| 2 | The user had opened a phishing email. | Inference (L2) presented as fact. | The Word document came from email, and the email was malicious. | Document arrived by USB or file share; email was legitimate. |
| 3 | The attacker moved laterally to FIN-31 using stolen credentials. | Case claim (L3) built on an unstated chain. | The 02:40 logon was not legitimate, the credentials came from FIN-22, and the same actor is involved. | Logon matches a scheduled task or the user's normal behavior. |
| 4 | …as shown by a 02:40 logon event. | Observation (L1), source unspecified. | Logon record exists on FIN-31 or the domain controller. | No such record in the named source. |
| 5 | Our new email filter would have blocked the message. | Counterfactual inference (L2) with no test. | Filter rules match this message's features. | Replay of the message through the filter in a lab is not blocked. |
| 6 | This proves that email filtering reduces ransomware risk. | Research claim (L4) from one case. | One case generalizes; ransomware occurred (it is not mentioned). | Any of the above defeaters; base rate across many organizations. |

Rewrite: "In this synthetic incident, an Office process started PowerShell on FIN-22 at 02:14 (EDR time) and a logon to FIN-31 was recorded at 02:40; whether these are linked, and whether the document came from email, has not been established. A lab replay could test whether the current filter would block the original message, if the message is recovered. No conclusion about ransomware risk follows from one case." Full credit requires noticing that ransomware appears only in the conclusion and that "would have blocked" is untested.

**EX002 — Model interview guide (excerpt).** Artifacts: A1 alert 09:12; A2 ticket note 09:30 "suspicious OAuth consent"; A3 chat 09:41 "should we revoke tokens?"; A4 containment 10:05 tokens revoked; A5 status 11:00. Questions: (1) "When you first saw A1 at 09:12, what else was on your screen or in your queue?" (2) "Your note at 09:30 says 'suspicious OAuth consent.' What made it look suspicious at that moment?" (3) "What other explanations were you considering around 09:30–09:40?" (4) "At 09:41 a colleague asked about revoking tokens. What information did you have, and what did you not have, that mattered for that choice?" (5) "Who needed to agree before 10:05, and how did you reach them?" (6) "What would have made you choose differently at 10:05?" (7) Only after these: "Looking back now, what do you know that you didn't know then?" — explicitly separating later knowledge. Mitigations: questions 3 and 6 elicit alternatives rather than justification; question 7 isolates hindsight; the interviewer shows each artifact as it was, not annotated. Consent: "Participation is voluntary and you may stop or withdraw your data until [date]. Your answers will be reported only at team or process level; no individual assessment will be shared with your management or used in performance review. Direct quotations will be anonymized and shown to you before use." Reviewers reward time order, outcome-last design and a consent statement that the participant's manager does not administer.

**EX003 — Model constraint map.**

| Artifact | Binding constraints | Tier | Justification |
|---|---|---|---|
| Protocol, preregistration, codebook, deviation log | None material (scrub MSSP name). | T0 public | No personal data; contract satisfied by removal of MSSP name. |
| Training/eval code, environment | Contract (no tool or MSSP names in comments/config). | T1 public with synthetic schema-matched data | Verifies pipeline. |
| NMS ticket-level data | Personal data; litigation hold (2 incidents); TLP:AMBER content; contract. | Not released (no T3) | Small CSIRT raises re-identification risk; held incidents cannot be disclosed. |
| Aggregate metrics on NMS data | Small cells may identify; held incidents. | T2, excluding the 2 held incidents with disclosure of exclusion, cell suppression below agreed threshold | Allows numeric checking. |
| Ticket text features derived from TLP:AMBER feed | TLP:AMBER limits sharing to need-to-know within recipient organization and clients. | Not released; feature described generically | Relabeling requires source permission. |
| OpenTriage-S runs | None. | T5 public | Exact version, split, seeds, script. |
| Model weights | Memorization risk of personal data and AMBER content. | Withheld pending memorization test | Release only if the agreed test passes. |

Open Science paragraph (model): "We release the protocol, preregistration, deviation log, codebook and all analysis code, with a synthetic dataset that matches the NMS ticket schema so that the pipeline can be executed end to end. All OpenTriage-S experiments are fully reproducible from the released benchmark version, split and seeds. NMS ticket data cannot be released: they contain personal data, two incidents are subject to a litigation hold and have been excluded from all reported results, some fields derive from threat intelligence received under TLP:AMBER, and a service contract forbids identifying a provider. We report aggregate NMS results with cells below the agreed threshold suppressed. Reviewers can therefore verify our computations and our benchmark results but cannot independently verify the NMS-specific numbers; we have asked the data owner to consider enclave access for future replication." Full credit requires stating what cannot be checked.

**EX004 — Model Ethical Impact Assessment (summary).** Stakeholders: on-call responders (employment, stress, blame), employees and citizens appearing in incident data (privacy), NMS (security exposure, reputation, legal), the public served by municipal services (service disruption if research interferes), other defenders (benefit) and the researcher (dual role if employed by NMS). Respect for persons: responder consent obtained by the researcher in private, with opt-out per shift and no manager knowledge of who declined; data subjects protected by recording decision points, not personal data. Beneficence: the researcher never asks questions during time-critical actions; field notes exclude credentials and exploitable details; results on unremediated weaknesses are delayed until fixed. Justice: responders bear the burden, so findings are shared with them first and the study offers a usable artifact back. Law and public interest: data-use agreement, legal review of observing communications, ethics-board approval, transparent reporting. Authorizations in order: legal review → NMS data-owner agreement → ethics review → incident-lead operational agreement → individual consent. Stop rules: (1) the incident lead asks the researcher to leave — immediate pause; (2) an incident involves a legal hold — exclude it; (3) a participant withdraws — remove their data; (4) a critical public-service outage — suspend observation; (5) a field-note security incident — stop and report. Incidental discovery: report to the incident lead within the shift; no independent investigation. A zero-score answer relies on manager approval or treats observation as risk-free.

**EX005 — Model lab results.** (1) Output as in §1.10. (2) Deleting the censored cases leaves nine contained incidents; the Kaplan–Meier median becomes **5.5 hours** (survival 0.4444 after the fifth event), down from 8.0. Dropping censored cases does not just lose information; it removes the slowest cases and biases the summary toward speed. (3) Recoding S10 for rater B gives observed agreement **0.833**, chance agreement **0.514** and κ **0.657**. One changed judgment moved kappa by about 0.16 — a reminder that twelve items give a very unstable estimate. (4) PPV at 1% prevalence = 0.99×0.01 / (0.99×0.01 + 0.01×0.99) = **0.500**: half of flags are false. Interpretation should note that censoring bias, rater instability and base-rate dependence each change a study's headline conclusion without any change in the underlying response.

**EX006 — Model failure-mode review.**

| Failure mode | Trigger | Alternative explanation | Design change |
|---|---|---|---|
| Self-report as performance | "surveyed … reported" | Leaders' beliefs about speed differ from measured speed. | Use recorded containment times with defined start/end. |
| Confounding (internal validity) | "Organizations that ran…" | Better-resourced organizations both run exercises and contain faster. | Measure and adjust for size, staffing, telemetry; or compare within organizations before and after adopting exercises. |
| Definition ambiguity | "containment" | Respondents use different definitions. | Provide a definition; collect start and end events. |
| Selection/response bias | "212 security leaders" | Leaders proud of exercises more likely to respond. | Report response rate and sampling frame. |
| Causal overreach | "therefore cut" | Association, not effect. | Quasi-experimental or experimental design. |
| Exercise-to-reality leap | Tabletop → real containment | Exercise frequency marks maturity rather than causing speed. | Link exercise findings to specific implemented changes. |
| Censoring/aggregation | "40% faster" | Unknown treatment of ongoing incidents and of outliers. | Report medians with censoring handling and intervals. |

Rewrite: "Among 212 responding security leaders, those reporting quarterly tabletop exercises also reported shorter typical containment times. Because times were self-reported, definitions were not standardized and organizations were not compared on resources, this association does not show that exercises cause faster containment." Full credit requires at least five distinct modes and a non-causal rewrite.

**EX007 — Model protocol skeleton (key elements).** Title: "Cross-organization transfer of a triage-assistant model: a preregistered benchmark study," v0.1 with change log. Claim: top-1 category agreement with benchmark labels on OpenTriage-S exceeds a *reproduced* baseline under time-respecting splits; no claim about real response outcomes. Hypotheses: H1 the model exceeds the reproduced baseline's macro-F1 on OpenTriage-S by at least a preregistered margin; H2 performance under the time-respecting split is lower than under a random split (testing temporal bias). Design: retrospective model development on NMS tickets with time-ordered train/validation splits; frozen model evaluated once on the OpenTriage-S test split. Data: NMS tickets years 1–5 with taxonomy-change mapping documented; OpenTriage-S exact version. Measures: macro-F1, per-class precision/recall, PPV at NMS's observed base rates; no time measures (so no censoring needed — stated explicitly). Analysis: bootstrap confidence intervals; one primary comparison; sensitivity analysis excluding year-3 transition tickets. Failure conditions: (a) if the published baseline cannot be reproduced within a preregistered tolerance, report the discrepancy and compare only against the reproduced value; (b) if the model does not exceed the margin, report a null result; (c) if a memorization test detects personal data in model outputs, withhold weights. Ethics: legal review, data-use agreement, ethics review, pseudonymization, re-identification assessment. Release: tiers as in §1.8. Stop rules: data-owner withdrawal, legal hold discovery, re-identification risk above threshold. Roles and conflicts: candidate employed by NMS — disclosed; an external coder audits labels blind to model output. Reviewers penalize any protocol that converts benchmark gains into claims about response quality.

### Chapter 2: EX008–EX014

**EX008 — Model search protocol.** Question: *Population* — responders who receive an in-progress incident from another responder (shift change, escalation, team transfer); *Intervention* — a structured handoff artifact or procedure; *Comparison* — unstructured or no handoff; *Outcome* — correctness of subsequent decisions, errors, time, workload; *Context* — SOC, CSIRT, MSSP, exercise or field. Sources: two computing digital libraries, one human-factors database, usable-security proceedings, standards bodies (NIST), and grey literature limited to published postmortems with a timeline. Example string: `("incident response" OR "security operations" OR SOC OR CSIRT OR "incident handling") AND (handoff OR "hand-off" OR "shift change" OR handover OR escalation) AND (study OR experiment OR evaluation OR interview OR observation)`; record date run and hit counts. A second string for transfer evidence: `(handoff OR handover) AND (checklist OR structured) AND (error OR "adverse event")` in the human-factors database. Eligibility: empirical studies of handoffs or of decisions after transfer in security-response settings; transfer studies from other high-tempo domains are included as a separate stratum. Exclusions with coded reasons: not empirical; no handoff or transfer; detection-only; duplicate. Screening: two screeners independently screen titles and abstracts, then full texts; compute kappa on title/abstract screening; disagreements resolved by discussion, with a third reviewer if needed. Stopping: after two consecutive snowballing rounds with no new eligible study. Full marks require a protocol another person could execute and obtain the same candidate set from on the same date.

**EX009 — Model appraisal of S2.** Unit: one MSSP team, before/after. Selection: vendor chose the site. Construct: "time-to-triage" defined by the vendor tool's own timestamps, so tool adoption changes the measurement instrument (instrumentation threat). No correctness measure. Comparison: historical, with a concurrent staffing increase (confounder). No blinding, no rater agreement (no raters). Base rates not reported. Artifacts unavailable. Conflict: vendor-run. Level: L2. Most serious threats: (1) concurrent staffing change confounds the before/after comparison; (2) measurement instrument changed with the intervention; (3) speed only — correctness may have fallen. Strongest supportable claim: "In one MSSP, recorded time-to-triage was lower in the period after the assistant was introduced, during which staffing also increased; the study does not isolate the assistant's effect or assess decision correctness." Zero credit for any answer that reports "35% faster because of the assistant."

**EX010 — Model competing predictions (alert enrichment with asset-owner data).**

| Account | Prediction | Observable |
|---|---|---|
| Situation awareness | Improves comprehension (significance of affected asset) → better prioritization of high-value assets. | Fewer misprioritized high-value alerts. |
| Skilled intuition | Largest gains for analysts new to the environment, who lack learned asset knowledge; little gain for veterans. | Interaction of tenure × enrichment. |
| Sociotechnical | Gains depend on whether owner data are trusted and current; stale data reduce trust and use. | Use logs and accuracy of owner data predict effect. |
| Detection-centric | No effect on correctness of malicious/benign disposition. | Disposition accuracy unchanged. |
| Safety science | Helps typical cases; may anchor analysts on the listed owner and slow escalation when the owner is wrong. | Errors in cases with deliberately incorrect owner data. |

Best discriminator between the situation-awareness and skilled-intuition accounts: the tenure interaction. Situation awareness predicts benefit across tenure for comprehension errors; skilled intuition predicts benefit mainly for novices. Full credit requires observables that differ between accounts.

**EX011 — Model gap classification.** (a) *Conflicting*: well-conducted field studies disagree; the next step is to compare populations, definitions of "miss" and alert environments to find moderators, and possibly design a study that measures the suspected moderator. (b) *Untransferred*: strong evidence exists in surgery, but transfer to security is untested and doubtful (adversary, different feedback); the next step is a security study that tests the mechanism, not just the checklist form. (c) *Weak*: vendor reports are conflicted, use undefined measures and likely caseload bias; the next step is an independent evaluation with correctness measures. (d) *Absent* (conditional on the documented search being adequate): the next step is descriptive work — measure fatigue in long incidents ethically — before any intervention study.

**EX012 — Model repaired map.** Modified code adds a `setting` field and computes `best_field` only from field studies (see the code in §2.7 extended with a fifth tuple element). Exact output:

```text
aid-improves-correctness                   best_field=L0 open        [S1:supports:L4:lab]
aid-improves-speed                         best_field=L2 open        [S2:supports:L2:field, S1:not-addressed:L0:lab]
context-determines-alert-judgment          best_field=L3 open        [R1:supports:L3:field]
handoff-loses-context                      best_field=L3 open        [S3:supports:L3:field]
manager-analyst-misalignment               best_field=L3 open        [R2:supports:L3:field]
organizational-cycles-drive-performance    best_field=L3 open        [R3:supports:L3:field]
```

Explanation: the original rule ignored setting, so one lab experiment with students "established" a claim about field correctness. After the repair, no claim is established; aid-improves-correctness shows best_field = L0 because its only support is lab-based. The episode demonstrates that a literature map encodes judgments, and a coding scheme that diverges from its stated rule silently manufactures a consensus. Different variable names earn full credit if the output is equivalent.

**EX013 — Model gap statement.** Draft: "Executive communication during ransomware is understudied." Revision: "Current evidence (practitioner guidance and single public case reviews) describes executive communication during ransomware at L0–L3 and recommends regular structured updates. It does not establish whether update *format* — a fixed decision-oriented brief (options, confidence, deadlines) versus narrative status — changes the quality of executive decisions such as whether to engage law enforcement or restore from backup, because no controlled comparison exists in our documented search. If decision-oriented briefs improve decision quality, response teams would adopt them as standard; if not, effort should go to the content of analysis rather than its format. This can be tested in a tabletop simulation with experienced executives randomized to brief format, scored by blinded panels on pre-specified decision criteria, and would be refuted by no difference or by worse decisions under the structured format." Tests: falsifiable (yes, refutation stated); consequential (adoption decision); novel (conditional on search); feasible (simulation with consenting executives — recruitment is the main risk, noted).

**EX014 — Model frontier memo (outline).** Claims: C1 brief format changes executive decision quality (chosen); C2 the effect depends on executives' prior incident experience; C3 brief format changes the time to decision. Dependencies: C2 is a moderator of C1 and is meaningful only if C1 shows an effect or a heterogeneous pattern; C3 is secondary because faster decisions are not better decisions unless C1 is understood. Justification: C1 first, with experience measured as a pre-specified exploratory moderator so that C2 can be designed properly later. Out of scope: real-incident field study (authorization and ethics barriers in active ransomware response; Chapter 1 §1.5) and legal-advice quality. Full credit requires reasoning about how the first answer shapes the next studies, not convenience alone.

### Chapter 3: EX015–EX020

**EX015 — Model contribution typing.** (a) Artifact: needs availability, documentation, installability and a description of intended use; it claims nothing about effects. (b) Method: needs reliability evidence (inter-rater agreement on realistic items, with raters not involved in development) and some validity evidence (scores relate to expert judgments or outcomes). (c) Theory/empirical: needs discriminating evidence that reliance on intuition varies with familiarity — e.g., think-aloud or behavioral measures across familiar and novel scenarios, with a definition of "intuition." (d) Empirical: needs a comparison study with valid error measures. The pair (a)/(d) is the trap: a thesis often releases (a) and implies (d). Claim (d) is really two claims — that the engine is used as intended and that its use reduces errors — so adherence must be measured.

**EX016 — Model mechanism (night-shift pairing policy).** (1) Night-shift responders work alone and are fatigued (L1–L2: rosters show solo staffing; fatigue literature outside security). (2) Fatigue and lack of a second viewpoint increase anchoring on the first hypothesis (L2, untransferred). (3) Pairing provides a second viewpoint at decision points (design fact). (4) Therefore paired responders revise initial hypotheses more often when disconfirming evidence appears, reducing anchoring-type errors. Predicted non-effect: no change in perception errors for signals presented prominently — pairing addresses interpretation, not visibility. Full credit requires the non-effect and honest evidence levels.

**EX017 — Model hypotheses.** H1: In simulated night-shift scenarios with planted disconfirming evidence, paired responders will revise an initial incorrect hypothesis within the scenario more often than solo responders (proportion of scenarios with revision). H2: The difference in anchoring errors will exceed the difference in perception errors for prominently presented signals. H3 (safety): Pairing will not increase time to first containment decision by more than 10 minutes (non-inferiority). SEOI for H1: an absolute increase of 15 percentage points in revision rate. Justification: pairing doubles night staffing cost for the period; a smaller improvement would not justify it to a CSIRT manager facing that cost. Full credit requires a consequence-based SEOI.

**EX018 — Model baseline critique.** Problems: "no summary" is a straw man — responders normally receive a human-written summary or ticket; students are not the target population; the AI summary may simply be longer or take more time to read (effort/length confound); scenario questions may be answerable by text matching against the summary. Redesign: Standard = human-written summary by trained responders under realistic time; Active-control = human-written summary length-matched to AI output; AI condition; participants = practicing responders; outcome = decisions scored by blinded raters, not recall questions. The Standard condition addresses the straw man; length-matched control addresses effort and length; the population change addresses external validity.

**EX019 — Model rival table (pairing).** Rivals: (1) more total person-time → control with solo responder given double time; (2) social desirability — paired responders perform for each other → measure and blind outcome raters; (3) partner expertise asymmetry → balance pair composition by tenure; (4) scenario order/learning → counterbalance; (5) fatigue not induced in simulation → run sessions at actual night hours or measure sleepiness; (6) communication overhead hides benefit → measure time separately; (7) demand characteristics → neutral cover story. Six or more with concrete features earns full credit.

**EX020 — Model failure conditions and risks (pairing).** Failure conditions: P1 pilot shows anchoring errors are rare in solo condition → mechanism premise fails, redesign scenarios or abandon; P2 CI for H1 excludes SEOI → precise null; P3 doubled-time solo control matches pairing → effect is time, not second viewpoint; narrow claim; P4 perception errors drop as much as anchoring → mechanism unsupported; P5 time increase exceeds margin → report trade-off, no adoption recommendation. Risks: night-session recruitment (high/high → compensated sessions, remote), participant fatigue welfare (medium/high → session limits, opt-out), scenario realism (medium/high → practitioner review), rater drift (medium/medium → calibration items), partner policy change (low/medium → two partners). Each failure condition names the claim it changes.

### Chapter 4: EX021–EX026

**EX021 — Model reproduction log.** Target: accuracy 0.833 for the source-majority baseline on the published split (synthetic paper, appendix). Tolerance ±0.02, recorded before running. Run 1: labels v1.1, published split → 0.667; difference −0.166, outside tolerance. Diagnosis: comparing v1.0 and v1.1 columns shows T05, T08 and T09 changed. Only T08 is in the published test set: v1.0 says "phish," v1.1 says "benign"; the baseline predicts "phish" for mail, so one test case flips from correct to incorrect (5/6 → 4/6). Training changes (T05, T09) do not alter the majority for mail (phish 3 vs. benign 2) or edr (malware 2 vs. benign 1). Run 2: labels v1.0 → 0.833, within tolerance. Environment: record `python3 --version`, OS, script hash (e.g., `sha256sum ch04_lab.py`) and timestamp with zone. Conclusion: reproducible on v1.0; v1.1 is the corrected reference. Full marks require the predeclared tolerance and the case-level diagnosis.

**EX022 — Model leakage audit.** Published test cases T02 (month 1), T04 (2), T08 (4) and T11 (6) precede training cases T13–T15 and T17–T19 (months 7–9). The learned rule for "vpn" is "account" (4 account vs. 2 benign in training), and every "account" training case comes from months 7–9. When T04 (month 2) is predicted, the rule uses information that would not exist until five months later. Here the leakage happens to *hurt* T04 (true label benign), which shows that leakage is a validity problem regardless of whether it inflates or deflates a score: the number does not describe deployment. A deployment-faithful split trains on months 1–6 and tests on months 7–9 (or rolls forward month by month). Full credit requires naming the vpn→account rule and the case IDs.

**EX023 — Model shift classification.** (a) Covariate shift: new input type; existing label relations may hold, but models have no experience with the new source, so evaluate separately on new-source cases. (b) Label shift: class proportions change; PPV of phishing flags rises and other classes' PPV falls; report metrics at the new base rate. (c) Concept shift: label definition changes, so pre- and post-change labels are not comparable; map or relabel before training across the change. (d) Emergence of a new class — a form of concept/label shift; a model trained only on earlier months cannot predict it, so report "unseen class" performance explicitly. Different terminology (e.g., "prior probability shift" for (b)) earns credit if correctly explained.

**EX024 — Model sample sizes.** δ = 0.5, σ_d = 1.2, 80% power → **45.2** (round up to 46). δ = 0.25, σ_d = 1.0 → **125.6** (126). δ = 0.5, σ_d = 1.0, 90% power → **42.0** (43). Recommendation: "Halving the SEOI roughly quadruples n, so the SEOI must be justified by consequence, not chosen to fit recruitment. Because σ_d is uncertain until the pilot, plan recruitment for σ_d = 1.5 (≈71 participants at 80% power) and treat 32 as optimistic. The normal approximation understates n for small samples; confirm the final figure with a t-based calculation or simulation, and add allowance for attrition."

**EX025 — Model pilot criteria.** As in §4.5, with numeric thresholds, for example: recruitment ≥ 6 consenting responders per month; completion ≥ 90%; realism median ≥ 4 on a 5-point scale with no scenario flagged by two or more reviewers; kappa ≥ protocol target (F1 — stop and revise if not met); Standard handoffs containing both ruled-out hypotheses and telemetry gaps in < 30% of cases (F2 — stop or redesign if exceeded); fidelity 100% after correction; σ_d estimated for planning only. Penalize any criterion such as "proceed if SHA shows improvement."

**EX026 — Model reproducibility record (Chapter 1 lab).** Input: `ch01_lab.py` with its SHA-256 hash recorded; no data files (fixture embedded). Environment: interpreter version, OS. Command: `python3 ch01_lab.py > out.txt`. Output hash recorded. Timestamp with zone, operator, and a note that results match the expected output in §1.10. Version control: commit ID or, absent a repository, file hash and archive location. Full credit requires enough detail for byte-level comparison by another person.

### Chapter 5: EX027–EX032

**EX027 — Model assignment schedule.** Split 24 participants into two experience strata of 12. Within each stratum, use a balanced design crossing order (SHA-first vs. Standard-first) with scenario-set allocation (set 1 = A, B, C; set 2 = D, E, F under SHA vs. under Standard), giving four sequences; assign three participants per sequence per stratum. Within each block, order the three scenarios by a 3×3 Latin square so each scenario appears in each position equally often. Generate the sequence list with a recorded seed before recruitment begins, held by a team member not involved in sessions; the facilitator opens each participant's assignment only at session start. Fidelity: checklist per session (correct packets, timer, no hints), with a second person auditing 20% of recordings where consent permits. Full credit requires balance within strata and credible concealment.

**EX028 — Model blinding.** Redacted: "DNS logs were unavailable for 02:00–04:00, so I did not treat the lack of lookups as evidence of no C2." (The information is kept; the cue "Per the T-gaps field" is removed. Because Standard participants could also learn of the gap from free text, the reasoning itself does not reveal condition.) Other cues: SHA field names (H-ruled-out, Expect), characteristic formatting (bulleted fields), and references to "the template" or "the form"; also differences in length if SHA prompts longer answers — mitigate by transcribing to a neutral format. Blinding check: after rating, raters guess condition for a random 20% of items; report accuracy with an interval against 50%.

**EX029 — Model interpretation.** Primary: "SHA reduced comprehension and projection errors by about 0.47 per scenario (95% CI about 0.23 to 0.72); an effect is likely present, but whether it reaches the predeclared practical threshold of 0.5 is uncertain" — the "above zero, includes SEOI" case. Mechanism: "Perception errors did not differ (0.00 per three scenarios, CI −0.38 to 0.38), consistent with the predicted pattern; modest effects cannot be excluded." Harms: "Harmful actions were slightly more frequent with SHA (−0.08 per three scenarios, CI −0.51 to 0.34); an increase cannot be excluded."

**EX030 — Model sensitivity.** Without P10 the differences are [2, 0, 3, 1, 3, 1, 0, 2, 0, 1, 1]: mean **1.273**, SD **1.104**, 95% CI **(0.531, 2.014)** over three scenarios (≈0.18 to 0.67 per scenario), exact sign-flip p **0.0078**. Report: "In the preregistered primary analysis including all participants, the reduction was 1.42 (0.68 to 2.16). A deviation log entry recorded after unblinding showed that P10 had prior exposure to two scenarios; excluding P10 in a sensitivity analysis gives 1.27 (0.53 to 2.01). Conclusions are unchanged in direction; the estimated effect is somewhat smaller and practical importance remains uncertain." Zero credit for silently replacing the primary analysis.

**EX031 — Model error analysis plan.** (1) Per-scenario error distribution by condition — does the effect concentrate in scenarios with large telemetry gaps (supporting the mechanism) or appear uniformly (suggesting a general effect)? (2) Per decision point — which points drive the difference? (3) New error types under SHA — anchoring on H-current, or overtrust in an incomplete T-gaps list (code a specific "inherited error" category). (4) Harmful actions — read all cases; were they preceded by SHA content? (5) Participant heterogeneity — do novices and veterans differ (links to the skilled-intuition account)? (6) Rater disagreement items — are disagreements concentrated in one error type, indicating construct ambiguity? Each answer either supports, narrows or challenges H1/H2.

**EX032 — Model results paragraph.** "Twelve participants completed all six scenarios (teaching excerpt). Raters' pre-adjudication agreement is reported in Table X. In the preregistered primary analysis, participants made 1.42 fewer comprehension and projection errors over three scenarios with SHA than with Standard handoffs (95% CI 0.68 to 2.16; exact sign-flip p = 0.004), equivalent to 0.47 per scenario (0.23 to 0.72). The interval includes the predeclared smallest effect of interest (0.5 per scenario), so practical importance is uncertain. Perception errors did not differ (0.00; −0.38 to 0.38), consistent with the predicted mechanism. Harmful actions were slightly more frequent with SHA (−0.08; −0.51 to 0.34); an increase cannot be excluded, and all seven harmful actions (four with SHA, three with Standard) are examined in the error analysis. A sensitivity analysis excluding one participant with prior scenario exposure gave 1.27 (0.53 to 2.01). Analyses: `ch05_lab.py`, data hash recorded in the run log."

### Chapter 6: EX033–EX038

**EX033 — Model modifier table.**

| Feature | Predicted direction | Mechanism link | Measure |
|---|---|---|---|
| Telemetry completeness | More gaps → larger effect | T-gaps prevents absence-of-evidence errors | Source coverage per asset class; gap count per scenario |
| Handoff frequency | More handoffs → larger cumulative effect | Context loss per transfer | Handoffs per incident from case records |
| Responder experience | More experience → smaller effect | Veterans already transmit ruled-out hypotheses | Tenure; pilot content analysis of free-text handoffs |
| Existing structured tooling | More structure → smaller effect | Standard already carries fields | Field inventory of case tool |
| Language/time-zone distance | Greater distance → larger effect | Explicit Expect/Authority fields reduce ambiguity | Region pairs in handoffs |
| Compliance pressure on documentation | Higher pressure → possibly smaller effect (box-ticking) | Field quality degrades | Content-quality rating of SHA entries |
| Incident novelty | More novel → larger effect | Projection depends on transmitted expectations | Scenario novelty rating |

**EX034 — Model replication choices.** (a) Direct replication: same protocol, materials and scenarios with a new sample from a comparable population; key element — identical codebook and analysis, preregistered criterion for consistency (e.g., new interval overlaps the original and excludes zero). (b) Conceptual replication: new scenarios not seeded from Harbor/CTN/LLR, built by different designers, same hypotheses and codebook; key element — independent scenario authorship. (c) Boundary test: manipulate telemetry density as a crossed factor within participants, with a registered interaction prediction; key element — gap level varied within context to avoid confounding.

**EX035 — Model heterogeneity.** Original: pooled 0.730 (0.337, 1.123), Q = 6.49, I² = 0.85. Variant with KFL = (1.100, 0.250): pooled **1.213** (95% CI ≈ 0.820 to 1.606), **Q = 0.57**, **I² = 0.00**; context difference 0.317 (SE 0.419, z ≈ 0.76). Interpretation: in the original, the two estimates differ more than sampling error predicts, so a pooled value misdescribes both contexts. In the variant, there is no evidence of heterogeneity — but with two contexts Q has little power and I² = 0 does not demonstrate homogeneity; it means the data cannot distinguish the contexts. Full marks require the caveat.

**EX036 — Model paragraph.** "The across-context difference (1.07, z ≈ 2.55) is the more precise estimate, but NMS and KFL differ in telemetry density, staffing model, tooling, incident mix and scenarios. Any of these, alone or together, could explain the smaller KFL effect, so precision does not buy diagnosticity. The within-KFL comparison of high- and low-gap scenarios holds participants, organization, tooling and raters constant and varies only the scenario's telemetry gap, which is the feature the mechanism names. It is less precise (z ≈ 1.70) but it isolates the candidate cause. To strengthen it: preregister the interaction as primary; increase scenarios per gap level; use matched scenario pairs identical except for gap level; and replicate the within-context manipulation at NMS, so that the interaction is tested in both contexts."

**EX037 — Model claim.** "In two synthetic organizations, a structured handoff artifact reduced receiving responders' comprehension and projection errors where telemetry was sparse (about 0.47 per scenario; practical importance uncertain). Where telemetry was dense, the overall effect was small and uncertain and appeared concentrated in scenarios with high telemetry gaps. Telemetry completeness is a plausible boundary condition; establishing it requires more contexts. Perception errors were not affected in either context." (≈ 85 words.)

**EX038 — Model memo (outline).** Third context: a synthetic university SOC with student analysts, sparse telemetry, frequent shift handoffs, no structured case tool and low compliance pressure. Mapping: telemetry sparse (→ larger effect), experience low (→ larger), tooling unstructured (→ larger), handoffs frequent (→ larger), compliance low (→ no box-ticking penalty). Prediction: effect at least as large as at NMS, with wide uncertainty because student analysts differ from the professional populations tested (an external-validity gap in population, not only context). Minimal check: a small within-subject replication of the NMS protocol with 20–30 analysts, primary outcome the same, registered prediction "effect ≥ NMS lower bound." The memo must not recommend adoption on the basis of prediction alone.

### Chapter 7: EX039–EX044

**EX039 — Model pre-mortem.**

| Possible reason for retraction or major correction | Check now |
|---|---|
| Raters were effectively unblinded by SHA formatting. | Blinding-check accuracy; neutral transcription audit. |
| Outcome mostly measured reading the T-gaps field (construct problem). | Subtype analysis (§7.5). |
| Analysis file differs from preregistered plan without disclosure. | Diff analysis code against preregistration; complete deviation log. |
| Archive does not reproduce reported tables. | Third-party reproduction from archive. |
| Scenarios leaked to participants beforehand (as with P10). | Exposure questionnaire; sensitivity analysis. |
| Participant identifiability in released decision data. | Re-identification review of T3 release. |
| Partner organization identifiable from scenario details. | Review by someone from the sector, not the partner. |
| Misreported sample (e.g., excerpt numbers presented as full study). | Participant-flow table checked against raw records. |

**EX040 — Model responses.** (a) Methodological — test: report blinding-check accuracy; if above chance, run a sensitivity analysis with neutral re-transcription; acknowledge. (b) Analytical — test: fit a mixed model with participant and scenario random effects; report alongside the paired analysis. (c) Presentational/external validity — concede: revise abstract to "volunteer responders from two organizations." (d) Reproducibility — concede: add the file or correct the reference, rerun the archive check, log the correction. (e) Conceptual — defend with evidence: the study used situation awareness to generate discriminating predictions (error types), and the results are reported regardless; invite the reviewer to name a competing account with different predictions, and note that the error-type pattern can be re-examined under that account. Full credit requires proportionate, evidence-based responses.

**EX041 — Model contested analysis.** Outputs as in §7.5: total 1.417 (0.677, 2.157), gap-misread 1.083 (0.580, 1.587), other 0.333 (0.020, 0.646) with exact p 0.125; share 0.76. Relative reduction in gap-misreads: standard total 18, SHA total 5 → (18 − 5)/18 ≈ **0.72**. Interpretation: "SHA reduced gap-misread errors by about 72% relative to Standard. This is the effect the mechanism predicts, so the reviewer's analysis does not refute the mechanism; it localizes it. What it shows is that the broader claim of improved comprehension and projection rests mainly on one error subtype; the remaining effect is small and its significance depends on the test used. It does not show that SHA is merely a reading test — gap misreads occur in real handoffs and lead to wrong scope decisions — but it does mean the claim should be stated in terms of telemetry-gap transmission."

**EX042 — Model revised contribution.** "Across two synthetic organizations, a structured handoff artifact reduced receiving responders' errors of treating missing telemetry as evidence of absence, by explicitly listing known telemetry gaps. The effect was clear where telemetry was sparse and smaller and uncertain where it was dense, consistent with telemetry completeness as a boundary condition. Evidence that the artifact improves other aspects of comprehension or projection — through ruled-out hypotheses or stated expectations — is weak and remains to be tested. A small increase in harmful actions could not be excluded." (≈ 95 words.)

**EX043 — Model negative result.** The interval (−0.40 to 0.30 per three scenarios) excludes the SEOI of 1.5: this is **evidence of absence** of a practically important effect in that replication, not merely absence of evidence. Paragraph: "In the direct replication at KFL-SOC, SHA did not reduce comprehension and projection errors (−0.05 over three scenarios; 95% CI −0.40 to 0.30). The interval excludes the predeclared smallest effect of interest (1.5 per three scenarios), indicating no practically important effect under these conditions. Blinding and rater agreement met protocol targets." Implication: the NMS result does not transport to dense-telemetry contexts under direct replication; the claim must be restricted to sparse-telemetry settings pending further tests, and the possibility that the NMS result was inflated by chance should be discussed.

**EX044 — Model response excerpt.** "We thank the reviewer for this important point. **Classification:** conceptual and analytical. **Response:** We partly agree. Transmitting telemetry-gap information is the mechanism we proposed (Section 3.2, link 4), and misreading missing telemetry as negative evidence is a consequential error in real handoffs, so we regard its reduction as a genuine decision-quality improvement. However, we agree that our primary outcome bundled this error type with other comprehension and projection errors, and that our claim of improved 'comprehension' could overstate a narrower effect. **New analysis:** We recoded all decisions into gap-misread errors and other comprehension/projection errors (script `ch07_lab.py`; data hash in the run log). About 76% of the reduction came from gap-misreads (1.08 of 1.42 per three scenarios); the reduction in other errors was 0.33 (95% CI 0.02 to 0.65; exact sign-flip p = 0.125). We report this as a preregistered-outcome sensitivity analysis; the primary analysis is unchanged. **Changes:** We revised the abstract, Section 6 (discussion) and the conclusion to state that SHA reduces gap-misread errors and that evidence for broader comprehension effects is weak (pages X–Y). We added the subtype analysis as Table Z and a limitation noting the alignment between the T-gaps field and this outcome subtype. We also identify ruled-out hypotheses and expectation fields as untested components for future work."

### Chapter 8: EX045–EX050

**EX045 — Model argument map.** Claim: "In simulation, SHA reduces receiving responders' gap-misread errors where telemetry is sparse." Grounds: NMS within-subject results (Ch. 5 §5.8), KFL replication and within-context gap interaction (Ch. 6 §6.6), subtype analysis (Ch. 7 §7.5). Warrant: blinded coding against information available at each decision point measures decision errors (Ch. 1 §1.6; Ch. 5 §5.1, §5.3). Backing: rater agreement and blinding check (Ch. 5 §5.3), pilot realism and fidelity (Ch. 4 §4.5), reproduced triage baseline (Ch. 4 §4.6). Qualifier: "in simulation; sparse telemetry; practical importance relative to SEOI uncertain." Rebuttals: dense telemetry (Ch. 6), teams that already convey gaps (Ch. 3 F2), possible harms (Ch. 5 §5.8), untested field effectiveness (Ch. 8 §8.5). Full credit requires every element traceable to a section.

**EX046 — Model claim evolution.** Use the four-stage table in §8.2, with each "what changed it" cell citing the specific estimate or analysis (e.g., "CI 0.23–0.72 per scenario includes SEOI 0.5"; "KFL 0.35 vs. NMS 1.42; within-KFL interaction 0.85"; "76% of reduction from gap-misreads"). Explanation: "The trajectory shows that each narrowing followed predeclared criteria or external critique rather than the author's preference. A reader can see that the final claim was not chosen after the results to fit them; it is what survived tests designed to break the original claim. That makes the narrow claim more credible than the broad one ever was."

**EX047 — Model README (outline).** Sections: *Purpose* (what the archive supports); *Quick start* (environment lock file, one command to run the pipeline on synthetic data and regenerate aggregates); *Contents* (directory map); *What is not here and why* (participant-level decisions restricted by consent and data-use agreement; no incident records used at all); *Access to restricted data* (custodian role, request procedure, agreements); *Licenses* (text, code and data separately; restricted data not openly licensed); *Permissions register* (pointer to PERMISSIONS.md); *Integrity* (how to verify MANIFEST.sha256); *Citation*; *Reporting problems and corrections* (contact role and CHANGELOG policy). Full credit requires that a stranger could run it and understand every gap.

**EX048 — Model manifest extension.** Replace `verify` with a function that compares the manifest with the files actually present, excluding the manifest itself:

```python
def verify_full(root):
    listed = {}
    for line in (root / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        listed[rel] = digest
    on_disk = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    on_disk.discard("MANIFEST.sha256")
    changed = sorted(r for r, d in listed.items() if r in on_disk and sha256(root / r) != d)
    missing = sorted(set(listed) - on_disk)
    added = sorted(on_disk - set(listed))
    return {"changed": changed, "missing": missing, "added": added}
```

Output when run on the archive built by `build`, then after adding `data/synthetic/extra.csv`:

```text
untouched: {'changed': [], 'missing': [], 'added': []}
after add: {'changed': [], 'missing': [], 'added': ['data/synthetic/extra.csv']}
```

The function also reports deleted files ("missing"). Excluding `MANIFEST.sha256` from the on-disk set avoids a false positive. (The function needs `build` and `sha256` from the §8.7 script and `from pathlib import Path`.)

**EX049 — Model governance plan.** Custodian: the supervising research group's data steward role (not the candidate personally), with a named deputy role. Access: written request describing purpose; review by custodian plus one independent researcher; data-use agreement forbidding re-identification attempts and onward sharing; analysis within an enclave where feasible. Retention: participant-level data kept for the period stated in the consent form (e.g., five years after publication), then destroyed with a recorded destruction certificate; aggregates and synthetic data retained indefinitely. Re-identification response: suspend access, investigate within a stated period, notify the ethics body and affected participants as required, record in CHANGELOG. Corrections: an issue-reporting address or tracker; corrections released as new versions with a regenerated manifest and change-log entry; notice to the publication venue if a published number changes.

**EX050 — Model objection inventory (selection).** (1) "Simulation doesn't reflect real incidents." — Concede scope; show realism ratings; claim limited to simulation (§8.5). (2) "Raters knew the condition." — Blinding-check results; neutral transcription (Ch. 5 §5.3). (3) "Your outcome is aligned with the intervention." — Subtype analysis and narrowed claim (Ch. 7 §7.5). (4) "Two contexts can't support a boundary claim." — Agree; claim stated as plausible; within-context evidence (Ch. 6 §6.4). (5) "Harms were ignored." — Harms were prespecified and reported; an increase is not excluded (Ch. 5 §5.8). (6) "The sample is small and volunteer-based." — Power planning and sensitivity ranges (Ch. 4 §4.4); external-validity limitation. (7) "Your triage baseline was cherry-picked." — Reproduction log showing published, corrected and time-respecting results (Ch. 4 §4.6). (8) "Could participants be identified from released data?" — Release tiers, consent limits and re-identification review (Ch. 1 §1.4; Ch. 8 §8.4). (9) "Did you change the analysis after seeing results?" — Preregistration, deviation log and the hash manifest (Ch. 1 §1.3.2; Ch. 8 §8.7). Full credit requires honest concessions where warranted.

<a id="glossary"></a>

## Glossary

- **Observation / inference / claim:** what a named source recorded; a conclusion drawn from observations under stated assumptions; the statement defended to others with an explicit scope (Ch. 1 §1.2.2).
- **Evidence ladder:** this book's teaching device (L0 report to L4 research claim) for tracking how far a statement has been warranted; not a published standard.
- **Defeater:** an observation that, if found, would invalidate an inference.
- **Outcome bias / hindsight bias:** judging a decision by its result; overestimating, after the fact, how foreseeable an outcome was.
- **Preregistration:** a time-stamped plan of hypotheses, design and analysis written before the outcome data used for confirmation are examined.
- **Registered Report:** a publication format in which question and method are peer reviewed before data collection.
- **Deviation log:** a dated record of every departure from protocol, with reason and whether outcome data had been seen.
- **HARKing:** presenting a hypothesis formed after seeing results as if it had been formed beforehand.
- **Reproducibility / replicability:** consistent results from the same data and code; consistent results across studies collecting their own data (National Academies, 2019).
- **Release tier (T0–T5):** this book's scale for artifact release, from protocol-only to full public data.
- **De-identification:** removing the association between data and data subjects; a governance process whose residual risk must be assessed.
- **Construct / operationalization:** an abstract property such as decision quality; the concrete measure used for it.
- **Censoring:** incomplete observation of a time-to-event outcome, e.g. incidents not yet contained when the dataset closes.
- **Cohen's kappa:** chance-corrected agreement between two raters on categorical judgments.
- **Positive predictive value (PPV):** proportion of flagged items that are truly positive; depends strongly on base rate.
- **Mechanism:** a causal chain explaining how an intervention produces an effect, specific enough to predict a pattern.
- **Smallest effect of interest (SEOI):** the smallest effect that would matter in practice, fixed before data collection.
- **Attention-control condition:** a comparison condition equalizing effort or exposure without the active ingredient.
- **Dataset shift:** covariate, label or concept change between training/reference data and the target data.
- **Temporal leakage:** use of information from the future relative to the prediction or decision being evaluated.
- **Pilot (feasibility) study:** a small study testing whether the main study can be run as designed, with predeclared progression criteria.
- **Allocation concealment:** preventing those who enroll participants from knowing or influencing upcoming assignments.
- **Boundary condition:** a value of a contextual feature beyond which an effect weakens, disappears or reverses.
- **Heterogeneity (Q, I²):** variation in effects across contexts beyond sampling error, and its descriptive proportion.
- **Transportability:** reasoning about the expected effect in a new context using knowledge of how it differs.
- **Concede / defend / test:** the three honest responses to a critique.
- **Claim-evolution table:** a record of how a contribution statement changed across a project and why.
- **Integrity manifest:** a list of cryptographic digests for archive files, used to detect changes.
- **Permissions register:** a record of what each partner and participant allowed to be used and released.

<a id="references"></a>

## References

Standards, guidance and policy (dates as shown on the publishers' pages when consulted in October 2026):

- NIST. [SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025; supersedes Rev. 2 (2012). [PDF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf).
- NIST. [SP 800-184, *Guide for Cybersecurity Event Recovery*](https://csrc.nist.gov/pubs/sp/800/184/final). December 2016.
- NIST. [SP 800-84, *Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities*](https://csrc.nist.gov/pubs/sp/800/84/final). September 2006 — dated; used only for exercise structure.
- NIST. [SP 800-86, *Guide to Integrating Forensic Techniques into Incident Response*](https://csrc.nist.gov/pubs/sp/800/86/final). August 2006 — dated; presents forensics from an IT rather than a law-enforcement view; technical details need current verification.
- NIST. [SP 800-188, *De-Identifying Government Datasets: Techniques and Governance*](https://csrc.nist.gov/pubs/sp/800/188/final). September 2023.
- FIRST. [*Traffic Light Protocol (TLP) Version 2.0*](https://www.first.org/tlp/). Authoritative from August 2022.
- Dittrich, D., Kenneally, E., et al. [*The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research*](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. DHS, August 2012 (now marked as archived content).
- USENIX. [*USENIX Security '26 Call for Papers*](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) — Ethical Considerations and Open Science appendix requirements.
- CISA. [*Cyber Safety Review Board (CSRB)*](https://www.cisa.gov/resources-tools/groups/cyber-safety-review-board-csrb) — established under Executive Order 14028.
- Center for Open Science. [*Registered Reports*](https://www.cos.io/initiatives/registered-reports).
- National Academies of Sciences, Engineering, and Medicine. [*Reproducibility and Replicability in Science*](https://www.nationalacademies.org/read/25303/chapter/3). 2019. [doi:10.17226/25303](https://doi.org/10.17226/25303).

Incident-response, security-operations and security-research studies:

- Ahmad, A., Hadgkiss, J., and Ruighaver, A. B. [Incident Response Teams – Challenges in Supporting the Organisational Security Function](https://doi.org/10.1016/j.cose.2012.04.001). *Computers & Security* 31(5), 2012.
- Alahmadi, B. A., Axon, L., and Martinovic, I. [99% False Positives: A Qualitative Study of SOC Analysts' Perspectives on Security Alarms](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi). USENIX Security 2022.
- Arp, D., Quiring, E., Pendlebury, F., Warnecke, A., Pierazzi, F., Wressnegger, C., Cavallaro, L., and Rieck, K. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). USENIX Security 2022.
- Herley, C., and van Oorschot, P. C. [SoK: Science, Security and the Elusive Goal of Security as a Scientific Pursuit](https://doi.org/10.1109/SP.2017.38). IEEE Symposium on Security and Privacy 2017.
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., and Ahn, G.-J. [Matched and Mismatched SOCs: A Qualitative Study on Security Operations Center Issues](https://doi.org/10.1145/3319535.3354239). ACM CCS 2019.
- Pendlebury, F., Pierazzi, F., Jordaney, R., Kinder, J., and Cavallaro, L. [TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time](https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury). USENIX Security 2019.
- Pendleton, M., Garcia-Lebron, R., Cho, J.-H., and Xu, S. [A Survey on Systems Security Metrics](https://doi.org/10.1145/3005714). *ACM Computing Surveys* 49(4), 2016.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). IEEE Symposium on Security and Privacy 2010.
- Sundaramurthy, S. C., et al. [A Human Capital Model for Mitigating Security Analyst Burnout](https://www.usenix.org/conference/soups2015/proceedings/presentation/sundaramurthy). SOUPS 2015.
- Sundaramurthy, S. C., McHugh, J., Ou, X., Rajagopalan, S. R., and Wesch, M. [An Anthropological Approach to Studying CSIRTs](https://doi.org/10.1109/MSP.2014.84). IEEE Security & Privacy, 2014.
- Vielberth, M., Böhm, F., Fichtinger, I., and Pernul, G. [Security Operations Center: A Systematic Study and Open Challenges](https://doi.org/10.1109/ACCESS.2020.3045514). IEEE Access 8, 2020.

Research methods, decision-making and privacy:

- Benjamini, Y., and Hochberg, Y. [Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). *Journal of the Royal Statistical Society, Series B* 57(1), 1995.
- Bigley, G. A., and Roberts, K. H. [The Incident Command System: High-Reliability Organizing for Complex and Volatile Task Environments](https://doi.org/10.2307/3069401). *Academy of Management Journal* 44(6), 2001.
- Cohen, J. [A Coefficient of Agreement for Nominal Scales](https://doi.org/10.1177/001316446002000104). *Educational and Psychological Measurement*, 1960.
- Cohen, J. [A Power Primer](https://doi.org/10.1037/0033-2909.112.1.155). *Psychological Bulletin*, 1992.
- Comfort, L. K. [Crisis Management in Hindsight: Cognition, Communication, Coordination, and Control](https://doi.org/10.1111/j.1540-6210.2007.00827.x). *Public Administration Review* 67(s1), 2007.
- Cook, R. I. [*How Complex Systems Fail*](https://how.complexsystems.fail/). Cognitive Technologies Laboratory, University of Chicago; original copyright 1998–2000.
- DerSimonian, R., and Laird, N. [Meta-analysis in Clinical Trials](https://doi.org/10.1016/0197-2456(86)90046-2). *Controlled Clinical Trials* 7(3), 1986.
- Dwork, C., McSherry, F., Nissim, K., and Smith, A. [Calibrating Noise to Sensitivity in Private Data Analysis](https://doi.org/10.1007/11681878_14). Theory of Cryptography Conference, 2006.
- Endsley, M. R. [Measurement of Situation Awareness in Dynamic Systems](https://doi.org/10.1518/001872095779049499). *Human Factors* 37(1), 1995.
- Endsley, M. R. [Toward a Theory of Situation Awareness in Dynamic Systems](https://doi.org/10.1518/001872095779049543). *Human Factors*, 1995.
- Fischhoff, B. [Hindsight ≠ Foresight: The Effect of Outcome Knowledge on Judgment under Uncertainty](https://doi.org/10.1037/0096-1523.1.3.288). *Journal of Experimental Psychology: Human Perception and Performance*, 1975.
- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., and Crawford, K. [Datasheets for Datasets](https://doi.org/10.1145/3458723). *Communications of the ACM* 64(12), 2021.
- Gelman, A., and Loken, E. [The Statistical Crisis in Science](https://doi.org/10.1511/2014.111.460). *American Scientist*, 2014.
- Higgins, J. P. T., and Thompson, S. G. [Quantifying Heterogeneity in a Meta-analysis](https://doi.org/10.1002/sim.1186). *Statistics in Medicine*, 2002.
- Higgins, J. P. T., Thompson, S. G., Deeks, J. J., and Altman, D. G. [Measuring Inconsistency in Meta-analyses](https://doi.org/10.1136/bmj.327.7414.557). *BMJ*, 2003.
- Ioannidis, J. P. A. [Why Most Published Research Findings Are False](https://doi.org/10.1371/journal.pmed.0020124). *PLoS Medicine*, 2005.
- Kahneman, D., and Klein, G. [Conditions for Intuitive Expertise: A Failure to Disagree](https://doi.org/10.1037/a0016755). *American Psychologist*, 2009.
- Kapoor, S., and Narayanan, A. [Leakage and the Reproducibility Crisis in Machine-Learning-Based Science](https://doi.org/10.1016/j.patter.2023.100804). *Patterns* 4(9), 2023.
- Kerr, N. L. [HARKing: Hypothesizing After the Results Are Known](https://doi.org/10.1207/s15327957pspr0203_4). *Personality and Social Psychology Review*, 1998.
- Klein, G. [Naturalistic Decision Making](https://doi.org/10.1518/001872008X288385). *Human Factors* 50(3), 2008.
- Klein, G. A., Calderwood, R., and Clinton-Cirocco, A. [Rapid Decision Making on the Fire Ground](https://doi.org/10.1177/154193128603000616). *Proceedings of the Human Factors Society Annual Meeting* 30(6), 1986.
- Lakens, D. [Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses](https://doi.org/10.1177/1948550617697177). *Social Psychological and Personality Science* 8(4), 2017.
- Lakens, D. [Sample Size Justification](https://doi.org/10.1525/collabra.33267). *Collabra: Psychology* 8(1), 2022.
- Landis, J. R., and Koch, G. G. [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310). *Biometrics*, 1977.
- Lee, J. D., and See, K. A. [Trust in Automation: Designing for Appropriate Reliance](https://doi.org/10.1518/hfes.46.1.50_30392). *Human Factors* 46(1), 2004.
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. [Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596). FAT* 2019.
- Moher, D., Liberati, A., Tetzlaff, J., Altman, D. G., and the PRISMA Group. [Preferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement](https://doi.org/10.1371/journal.pmed.1000097). *PLoS Medicine*, 2009.
- Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., et al. [A Manifesto for Reproducible Science](https://doi.org/10.1038/s41562-016-0021). *Nature Human Behaviour*, 2017.
- Narayanan, A., and Shmatikov, V. [Robust De-anonymization of Large Sparse Datasets](https://doi.org/10.1109/SP.2008.33). IEEE Symposium on Security and Privacy 2008.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *PNAS*, 2018.
- Open Science Collaboration. [Estimating the Reproducibility of Psychological Science](https://doi.org/10.1126/science.aac4716). *Science*, 2015.
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., et al. [The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews](https://doi.org/10.1136/bmj.n71). *BMJ*, 2021.
- Parasuraman, R., and Manzey, D. H. [Complacency and Bias in Human Use of Automation: An Attentional Integration](https://doi.org/10.1177/0018720810376055). *Human Factors* 52(3), 2010.
- Parasuraman, R., and Riley, V. [Humans and Automation: Use, Misuse, Disuse, Abuse](https://doi.org/10.1518/001872097778543886). *Human Factors* 39(2), 1997.
- Pearl, J., and Bareinboim, E. [External Validity: From Do-Calculus to Transportability Across Populations](https://doi.org/10.1214/14-STS486). *Statistical Science* 29(4), 2014.
- Peng, R. D. [Reproducible Research in Computational Science](https://doi.org/10.1126/science.1213847). *Science* 334(6060), 2011.
- Rasmussen, J. [Risk Management in a Dynamic Society: A Modelling Problem](https://doi.org/10.1016/S0925-7535(97)00052-0). *Safety Science* 27(2–3), 1997.
- Rubin, D. B. [Inference and Missing Data](https://doi.org/10.1093/biomet/63.3.581). *Biometrika* 63(3), 1976.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology* 9(10), 2013.
- Schulz, K. F., Altman, D. G., and Moher, D. [CONSORT 2010 Statement: Updated Guidelines for Reporting Parallel Group Randomised Trials](https://doi.org/10.1136/bmj.c332). *BMJ* 340, 2010.
- Silberzahn, R., Uhlmann, E. L., Martin, D. P., et al. [Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results](https://doi.org/10.1177/2515245917747646). *Advances in Methods and Practices in Psychological Science* 1(3), 2018.
- Simmons, J. P., Nelson, L. D., and Simonsohn, U. [False-Positive Psychology](https://doi.org/10.1177/0956797611417632). *Psychological Science*, 2011.
- Simons, D. J., Shoda, Y., and Lindsay, D. S. [Constraints on Generality (COG): A Proposed Addition to All Empirical Papers](https://doi.org/10.1177/1745691617708630). *Perspectives on Psychological Science* 12(6), 2017.
- Steegen, S., Tuerlinckx, F., Gelman, A., and Vanpaemel, W. [Increasing Transparency Through a Multiverse Analysis](https://doi.org/10.1177/1745691616658637). *Perspectives on Psychological Science* 11(5), 2016.
- Sweeney, L. [k-Anonymity: A Model for Protecting Privacy](https://doi.org/10.1142/S0218488502001648). *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems*, 2002.
- Tversky, A., and Kahneman, D. [Judgment under Uncertainty: Heuristics and Biases](https://doi.org/10.1126/science.185.4157.1124). *Science* 185(4157), 1974.
- Weick, K. E. [The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster](https://doi.org/10.2307/2393339). *Administrative Science Quarterly* 38(4), 1993.
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. [The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18). *Scientific Data*, 2016.
- Yarkoni, T. [The Generalizability Crisis](https://doi.org/10.1017/S0140525X20001685). *Behavioral and Brain Sciences* 45, 2022 (published online 2020).

Companion OpenCyber Academy books (synthetic case sources): [rapid](../../../../rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md) (Harbor Library), [professional](../../../../professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md) (Cedar Training Network) and [technical](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md) (Lumen Library Reservations).

**Case boundary.** NMS-CSIRT, KFL-SOC, OpenTriage-S, the Handoff Study, the SHA artifact, all participants, all numbers in the labs and the synthetic studies S1–S3 are invented for teaching. Sources support the general methodological statements beside which they are cited, never the synthetic details.

**Edition metadata.** Draft edition, October 2026. Reviewer: pending. A4 verification: not yet rendered.
