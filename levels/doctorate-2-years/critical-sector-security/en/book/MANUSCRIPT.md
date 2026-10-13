# Critical Infrastructure and Sector Security: Doctoral Research Methods and Thesis Practice

- Language: English (`en`); doctoral research track, two years; approximately 1,600 hours of planned study (course 207 of 207, the final course in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **draft**. Chapters 1–8 of 8 have authored teaching text, exercises EX001–EX050 and matching worked results. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: advanced researchers who already hold research experience and a defensible question about the security and resilience of critical infrastructure — energy, water, healthcare, transport, communications, finance and public services. Entry knowledge: the content planned for the [master's](../../../../masters-2-years/critical-sector-security/en/book/PLAN.md) and [postgraduate](../../../../postgraduate-2-years/critical-sector-security/en/book/PLAN.md) tracks in this area (still outlines at the time of writing), or equivalent professional experience, plus working literacy in probability, basic graph theory, simulation and qualitative interviewing. The companion [doctoral OT, IoT and cyber-physical security course](../../../ot-iot-security/README.md) studies the control-system layer in depth; this book studies the *sector and cross-sector* layer that sits above it.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights and are not relicensed here.
- Educational boundary: this track is an independent educational blueprint. It is not an accredited doctoral program, grants no degree, and grants no authority to access, scan, test or study any real infrastructure, operator, dataset or person. Every organization, region, asset, person, record, dataset, benchmark and numerical result in a worked example is **synthetic** unless a sentence explicitly cites a public source. Nothing in this book is an operational procedure for a real utility.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

Read the eight chapters in order. They follow the arc of one doctoral project. Chapter 1 sets the integrity, safety and method standards that every later step must meet in a domain where a careless experiment can hurt people. Chapter 2 maps the research frontier and finds a genuine open question. Chapter 3 turns it into a falsifiable contribution. Chapter 4 replicates the baselines the contribution must beat and pilots the study procedure. Chapter 5 runs the main study and validates it independently. Chapter 6 submits the claims to adversarial peer critique and revises them. Chapter 7 assembles the thesis and its reproducibility archive under the information-protection rules that govern infrastructure data. Chapter 8 prepares the defense and a responsible publication plan.

Each chapter contains teaching sections, definitions, a worked example, a practical activity with offline code, a list of common errors and limits, numbered exercises and a synthesis. Write your own answer to every exercise before opening the [worked results](#worked-results). At this level most exercises have more than one defensible answer; the worked results show one and the rubric shows what a reviewer would reward or reject.

Keep four labels in every research note you write while studying this book: **observation** (what a named source recorded), **inference** (what you conclude from observations, and under which assumptions), **claim** (the statement you intend to defend, with its scope) and **decision** (what someone chose to do because of it). In infrastructure research a fifth label is indispensable: **consequence** — the physical, health, economic or societal effect on people who depend on a service. Most errors in this field come from confusing a cyber observation with a consequence claim.

### Why a separate doctoral course on critical infrastructure

Operational technology (OT) security asks how a control system can be attacked and defended. Critical-infrastructure (CI) security asks a different set of questions: which *functions* a society cannot lose, how long it can lose them, how the loss of one propagates into others, who is responsible for each link, which rules apply, and how evidence about any of this can be gathered without endangering the services under study. The unit of analysis moves from the device and the plant to the **service, the sector and the system of systems**. A doctoral contribution here may be a model, a measurement method, a policy evaluation, an empirical study of operators or a validated design principle; it is rarely a new exploit and should almost never be one.

### The synthetic research corpus used in this book

The book follows one invented doctoral project, the **Cascade Study**, which asks whether a *dependency-aware restoration ordering* — restoring electrical feeders in the order in which the critical services they support would otherwise exhaust their buffers — reduces the loss of critical services after a cyber-induced distribution outage, compared with a conventional ordering that maximizes customers restored, and at what cost to ordinary customers. Its fictional settings are:

| Synthetic element | Role in the book | Boundary |
|---|---|---|
| **Riverbend Region** — Riverbend Electric Cooperative (REC), Riverbend Water Authority (RWA), St. Calder Hospital, Meridian Telecom central office, Riverbend County emergency dispatch | Primary study context with four distribution feeders F1–F4 (Chapters 1, 3, 5). | Invented region; no real utility, hospital, carrier, staff, asset or record. |
| **Port Halvard** | Second, coastal context with a different feeder topology, two restoration crews and fuel-resupply contracts (Chapter 5 independent validation, Chapter 6). | Invented region. |
| **GridWater-Sim** | A synthetic "published" co-simulation benchmark whose baseline cannot initially be reproduced (Chapter 4). | Invented benchmark; it is not a real tool or dataset and should not be searched for. |
| Synthetic studies **P1–P8** | Fictional papers used to practise appraisal and literature mapping (Chapter 2). | Invented; they stand in for kinds of study, not for real authors. |
| Operator participants **P01–P12** | Fictional interviewees and tabletop participants (Chapters 1, 5, 6). | Invented; no human-subjects data appear anywhere in this book. |

All numbers produced in the labs come from synthetic fixtures printed in the text and run with Python 3 standard library only. They demonstrate a method; they are not findings about any real infrastructure.

### Source policy

Every factual statement about a standard, a regulation, a public incident or a published study links to a source the author consulted. Standards and regulations change; each is cited with its version and date and should be re-verified before you rely on it. Where a concept is standard methodological vocabulary (for example, the distinction between verification and validation of a model), the text says so rather than inventing a reference. A source supports the general claim beside it, never the synthetic case details. Public incident reports are used only at the level of detail their publishers released, and no operational attack instruction is reproduced.

## Contents

1. [Advanced research integrity and methods](#ch-01) — consequence as the object of study, evidence in infrastructure research, safety and dual-use ethics, protected information, resilience metrics and the defensible protocol.
2. [Critical infrastructure and sector security: research frontier](#ch-02) — policy and standards landscape, interdependency modelling families, detection and testbed research, sector-specific evidence and a falsifiable gap.
3. [Original contribution proposal](#ch-03) — mechanism, dependency graphs with buffers, hypotheses, baselines, rival explanations and predeclared failure conditions.
4. [Baseline replication and pilot](#ch-04) — reproducing an inoperability model and a detection benchmark, evaluation pitfalls, model verification and a bounded pilot.
5. [Main study and independent validation](#ch-05) — simulation experiments with uncertainty, operator tabletop studies, validation against history and experts, and a second context.
6. [Peer critique and revision](#ch-06) — model–policy circularity, boundary conditions, model mismatch, negative results, dual-use review and narrowing claims.
7. [Thesis synthesis and reproducibility archive](#ch-07) — argument structure, tiered artifact release under infrastructure-information rules, synthetic data and model documentation.
8. [Defense and publication plan](#ch-08) — claim audit, defense preparation, venues, coordinated disclosure, policy translation and the post-doctoral research program.

The [worked results](#worked-results) contain EX001–EX050. A [glossary](#glossary) and [references](#references) close the book.

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Define critical infrastructure, critical function, dependency, interdependency and resilience precisely enough that a measurement can be attached to each, and explain why the definitions used by different governments are not interchangeable.
2. Distinguish cyber observations from consequence claims and state what evidence is needed to move from one to the other.
3. Apply research-integrity safeguards — pre-specification, deviation logs, separation of exploratory and confirmatory work, conflict-of-interest disclosure — to studies whose partners are regulated operators.
4. Identify the safety, dual-use, legal and information-protection hazards of infrastructure research and design proportionate safeguards, using the Menlo Report principles as a working structure.
5. Choose and defend resilience and consequence metrics, recognizing that metric choice can reverse the ranking of scenarios and that observation windows censor unrecovered outages.
6. Write a research protocol that a hostile but fair reviewer — and a utility's safety officer — could audit, including stop conditions.

The chapter is the methodological contract for the rest of the book. Chapter 2 reads the literature with its evidence vocabulary; Chapter 3 uses its protocol template; Chapters 4–5 use its metrics and validity tools; Chapters 6–8 use its integrity, safety and information-protection standards to judge the finished work.

### 1.1 What is being studied: services, functions and consequences

#### 1.1.1 Definitions that carry weight

"Critical infrastructure" is a legal and policy term before it is a technical one, and its definition decides what a study is allowed to generalize to. In the United States the statutory definition in the USA PATRIOT Act (42 U.S.C. § 5195c(e)) describes systems and assets "so vital to the United States that the incapacity or destruction of such systems and assets would have a debilitating impact on security, national economic security, national public health or safety". U.S. policy organizes those assets into sectors; the [National Security Memorandum on Critical Infrastructure Security and Resilience (NSM-22)](https://www.govinfo.gov/content/pkg/DCPD-202400358/html/DCPD-202400358.htm), issued 30 April 2024, rescinded and replaced Presidential Policy Directive 21 (2013), retained the sector structure, named the Cybersecurity and Infrastructure Security Agency (CISA) as national coordinator and assigned Sector Risk Management Agencies ([CISA overview](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience); [Congressional Research Service summary](https://www.congress.gov/crs-product/IF12716)). The CRS summary notes that a later administration may rescind or modify NSM-22 without congressional action, so a thesis must cite the instrument in force on a stated date.

The European Union uses two coordinated instruments: [Directive (EU) 2022/2557 on the resilience of critical entities (CER)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj) for all-hazards resilience of designated critical entities and [Directive (EU) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/) for cybersecurity of essential and important entities. A study that calls a hospital "critical infrastructure" in the U.S. sense and an "essential entity" in the NIS2 sense is not using synonyms: the populations differ, the obligations differ and the reporting thresholds differ.

A complementary lens is the **function** rather than the asset. CISA's [National Critical Functions set](https://www.cisa.gov/national-critical-functions-set), released in April 2019, lists 55 functions grouped as *Connect*, *Distribute*, *Manage* and *Supply* — for example, "Distribute electricity" or "Supply water". Functions cross sectors and organizations. For research, the functional lens has a decisive advantage: it names something whose *loss* can be measured (service delivered, people affected, duration) rather than something whose *compromise* can be observed (a host, a credential, a controller).

Working definitions used in this book:

| Term | Working definition | What you must measure to use it |
|---|---|---|
| **Critical service** | A service whose interruption beyond a stated duration causes harm to health, safety, security or essential economic activity for a stated population. | Population served, harm threshold, tolerable outage duration. |
| **Dependency** | A one-directional relation in which the state of service *B* depends on service *A* ([Rinaldi, Peerenboom and Kelly, 2001](https://doi.org/10.1109/37.969131)). | Direction, type, buffer, coupling strength. |
| **Interdependency** | A bidirectional relation: each service's state depends on the other's, directly or through a chain (same source). | The cycle and its timing. |
| **Buffer** | Stored capacity that lets a dependant keep operating after losing a supplier: fuel, batteries, water storage, inventory, manual procedures. | Duration under stated load, and how it is depleted. |
| **Consequence** | The effect on people and on the functions they rely on, measured in service units (customer-hours, patient diversions, litres not delivered). | A unit, a population, a time window. |
| **Resilience** | The ability of a system to withstand, absorb, recover from and adapt to a disruption; operationalized by metrics over a performance curve (§1.6). | A performance measure over time and a chosen summary. |

Rinaldi, Peerenboom and Kelly classify interdependencies as **physical** (a material output of one is an input of another), **cyber** (dependence on information transmitted through an information infrastructure), **geographic** (a local event affects co-located components) and **logical** (any other mechanism, such as markets or policy). Their six "dimensions" — environment, coupling and response behavior, type of failure (cascading, escalating, common cause), infrastructure characteristics, state of operation and type of interdependency — remain a useful checklist for what a model ignores. A doctoral study should state which of these dimensions it models and which it holds fixed.

#### 1.1.2 The cyber observation is not the consequence

The defining epistemic problem of the field is the gap between what can be observed about a cyber event and what happened to people. Consider three public examples, described only at the level their publishers released:

- The December 2015 attack on three Ukrainian electricity distribution companies interrupted power to roughly 225,000 customers for several hours; the joint [E-ISAC and SANS defense use case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and) (March 2016) describes credential theft, remote operation of distribution management systems, destructive malware and a telephone denial-of-service against customer call centers. The *consequence* (customers without power, for hours) depended on the operators' ability to restore manually — a buffer that was organizational, not technical.
- The malware described by CISA as [CrashOverride](https://www.cisa.gov/news-events/alerts/2017/06/12/crashoverride-malware) (alert TA17-163A, June 2017) targeted electricity substations in Ukraine in 2016. A capability analysis of malware tells you what *could* be commanded; it does not by itself tell you what *was* lost.
- CISA's analysis of [HatMan (also known as TRITON or TRISIS)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf) describes malware targeting a safety instrumented system. Here the most important consequence is one that did not occur — and research claims about "near misses" need special care because the counterfactual is unobservable.

Each case links a cyber observation (malware, access, commands) to a consequence (outage, trip, avoided harm) through a chain of physical and organizational mechanisms. A research claim that skips the chain — "attacks on substations cause blackouts" — is not wrong so much as unsupported. Write the chain explicitly; every link is a place where a buffer, a manual procedure, a protection system or a human decision can break it.

#### 1.1.3 The claim ladder for infrastructure research

The IR doctoral book in this series introduced a claim ladder ([observation, inference, case claim, research claim](../../../incident-response-resilience/en/book/MANUSCRIPT.md#ch-01)). Infrastructure research needs one more rung, because the field's central claims are about consequences in physical systems that the researcher usually cannot observe directly:

| Level | Kind of statement | Example (synthetic) | Typical evidence |
|---|---|---|---|
| L1 Observation | A named source recorded something. | "REC's outage management system logged feeder F3 open at 02:10." | Preserved record with clock state. |
| L2 Inference | A conclusion from observations under stated assumptions. | "F3 was opened by a remote command, not by protection." | Command logs, relay event records, assumptions stated. |
| L3 Case claim | A statement about what happened in one event. | "The treatment plant ran on generator for 7 h, then lost pressure in the high zone." | Converging records from several owners. |
| L4 Consequence claim | A statement about effects on people or functions. | "About 2,500 customers lacked potable water pressure for about 5 h." | Service records, customer reports, field verification. |
| L5 Research claim | A general statement about a population of systems or events. | "Dependency-aware restoration reduces critical-service loss in distribution outages." | Many cases, a validated model, or a designed study. |

Moving up a rung always adds assumptions. The protocol in §1.8 requires every claim in a thesis to be tagged with its rung and its assumptions.

### 1.2 Evidence in infrastructure research

#### 1.2.1 Five sources of evidence and their characteristic biases

1. **Incident records and public reports.** Rare, selectively disclosed, written for purposes other than research, and shaped by legal exposure. Publication bias is extreme: events with dramatic consequences or attributable adversaries are reported; quietly absorbed disruptions are not. The *population* of incidents is unknown.
2. **Operational data from partners.** SCADA historians, outage management records, work orders, alarm logs. High fidelity but owned by the operator, often protected by law or contract, and produced by systems tuned for operations rather than measurement. Sampling is decided by the partner's willingness, which correlates with maturity.
3. **Testbeds.** Physical or hybrid laboratory plants such as the Secure Water Treatment (SWaT) testbed described by [Goh, Adepu, Junejo and Mathur (2016)](https://doi.org/10.1007/978-3-319-71368-7_8). They allow controlled attacks and labeled data, at the cost of scale, age and realism: a six-stage teaching plant is not a city's water system.
4. **Models and simulations.** Network, flow, input–output, agent-based, system-dynamics and co-simulation models (Chapter 2). They allow counterfactuals and scale but prove only what their structure and parameters permit; their validity must be established, not assumed ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)).
5. **People.** Interviews, surveys, tabletop exercises and observation of operators, emergency managers and regulators. They reveal buffers that exist only as practice — manual workarounds, informal mutual aid — and also reveal what people *say* they would do, which is not what they do under stress.

Strong doctoral work **triangulates**: a model's prediction is checked against a historical record, a testbed experiment and the judgment of operators, and the thesis explains what each source can and cannot vouch for.

#### 1.2.2 The base-rate and denominator problem

Infrastructure incidents with physical consequences are rare. A study that collects "cyber incidents affecting utilities" from public sources has a numerator without a denominator: it cannot say how often such incidents occur, only how often they are *reported*. Rates require a defined population (all utilities of a type in a jurisdiction), a defined period and a reporting mechanism with known completeness. Mandatory reporting regimes may eventually help: the U.S. Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA) requires CISA to issue rules; CISA's 2024 proposed rule would require reporting of covered incidents within 72 hours and of ransom payments within 24 hours, and the final rule was sent for interagency review on 1 October 2026 after missing earlier targets ([Inside Privacy, 2026](https://www.insideprivacy.com/critical-infrastructure/cisa-submits-final-circia-rule-for-omb-review/)). Until a final rule is published and effective, and until its data are made available to researchers under some access regime, no thesis should treat reporting obligations as data.

#### 1.2.3 Hindsight, counterfactuals and "near misses"

Consequence claims in this field are often counterfactual: "had the operators not switched to manual control, the outage would have lasted days." Counterfactuals are legitimate research objects only when they are produced by an explicit model whose assumptions are disclosed and whose sensitivity is reported. Hindsight makes the actual path look inevitable and the alternatives look obvious; Chapter 5's tabletop design shows how to present scenarios to participants without outcome knowledge.

### 1.3 Integrity when partners are regulated operators

#### 1.3.1 Pressures specific to the field

Questionable research practices — selective reporting, flexible analysis, hypothesizing after results are known — are general ([Simmons, Nelson and Simonsohn, 2011](https://doi.org/10.1177/0956797611417632); [Kerr, 1998](https://doi.org/10.1207/s15327957pspr0203_4)). Infrastructure research adds four pressures:

- **Regulatory exposure.** An operator partner may fear that a finding will be read as non-compliance. Pressure to soften or delay results is predictable and must be handled by a written publication agreement *before* data access (§1.5.3).
- **Funding by interested parties.** Vendors of detection products, sector associations and agencies fund research. Funding is not corruption, but undisclosed funding is an integrity failure and favorable framing of a funder's product is a known risk.
- **Classification and sensitivity.** Some results cannot be published in full. The temptation is to publish the favorable part. The rule in this book: if a result cannot be published, the *existence* of the withheld analysis and its direction must be disclosed to examiners under the access arrangement, and the public text must not claim more than the public evidence supports.
- **Simulation flexibility.** A model has many free parameters. Tuning them until a proposed method wins is the simulation equivalent of p-hacking. The safeguard is to fix parameter distributions, scenario sets and metrics before comparing methods (Chapter 3), and to report all scenario families, not only those where the method wins.

#### 1.3.2 Pre-specification for simulation and mixed-methods studies

Preregistration is not only for experiments with human participants ([Nosek et al., 2018](https://doi.org/10.1073/pnas.1708274114)). For a simulation study, pre-specify: the model version and its verification tests; parameter distributions and their sources; the scenario families and how many draws of each; the comparison policies, including the strongest available baseline; the primary metric, the secondary or safety metric and any non-inferiority margin; the seeds; and the analysis (paired differences, interval method). For interviews and tabletops, pre-specify the sampling frame, the protocol, the coding frame's starting categories and the rule for adding categories. A **deviation log** records every change with date, reason and whether results had been seen.

#### 1.3.3 Originality and provenance

Infrastructure literature is spread across engineering, operations research, economics, public policy and computer security, and the same idea is often rediscovered under different names: "dependency-aware restoration" in power engineering, "restoration prioritization" in emergency management, "service-level criticality" in IT. A doctoral originality claim therefore needs a search across disciplines (Chapter 2) and an honest statement of what is new: the method, the application, the evidence or the synthesis.

### 1.4 Safety, dual use and ethics

#### 1.4.1 Why infrastructure research needs its own ethical analysis

The [Menlo Report](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) (Dittrich and Kenneally, 2012) adapted the Belmont principles — respect for persons, beneficence, justice — to information and communication technology research and added **respect for law and public interest**. Applying it to infrastructure research reveals stakeholders who are absent from most security studies: the population served by the infrastructure, who never consented and may be harmed by an experiment that goes wrong; the operator's staff, who may be exposed to blame; and third parties connected by interdependency.

| Menlo principle | Infrastructure-specific application |
|---|---|
| Respect for persons | Informed consent for interviewed or observed staff; protection from disciplinary use of research data; separate consent for audio recording. The served population cannot consent, so their interests must be represented by risk minimization. |
| Beneficence | No experiment on production control systems. Physical-safety review for any lab that energizes equipment. Weigh the benefit of publishing a vulnerability or weakness pattern against the uplift it gives to an adversary. |
| Justice | Do not concentrate research burden (and risk of exposure) on small, under-resourced utilities that cannot say no to a funder; do not design restoration methods that systematically disadvantage a population without saying so (Chapter 3's non-inferiority margin). |
| Respect for law and public interest | Comply with information-protection regimes (§1.5), export controls where relevant, computer-misuse law and partner contracts; be transparent about methods so the public interest in accountable research is served. |

#### 1.4.2 Hard rules used in this book

1. **Never test on production.** No scanning, probing, fuzzing or command injection against any live operational system, including "just reading" with industrial protocols, without a written authorization from the asset owner that names scope, time, safety controls and a stop authority. NIST's [Guide to Operational Technology Security, SP 800-82 Rev. 3](https://doi.org/10.6028/NIST.SP.800-82r3) (September 2023) explains why OT differs from IT: availability and safety dominate, devices may fail under traffic that IT systems tolerate, and changes require engineering review. NIST released an initial public draft of Revision 4 in September 2026, with comments due 30 November 2026 ([CSRC page](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); cite the revision you used.
2. **Simulate or emulate first.** Use models, co-simulation, digital twins or isolated testbeds. When a physical testbed is used, it needs its own safety case (pressure, voltage, chemical dosing) reviewed by a qualified engineer.
3. **Separate capability from consequence in publication.** A thesis may publish how a class of failure propagates and what buffers stop it; it should not publish an asset-specific target list or a step-by-step path to a physical effect.
4. **Have a stop authority.** Any study involving a partner's staff or systems names a person on the partner side who can stop it instantly, and the protocol says what happens to data collected before the stop.

#### 1.4.3 Dual-use review

A dual-use review asks three questions before any publication: *Uplift* — does this result make it materially easier for an adversary to cause harm, compared with what is already public? *Defensive value* — does it help defenders more than attackers, and do defenders have the means to act on it? *Mitigation* — can the harmful part be generalized, delayed (until fixes exist) or moved to controlled access without losing scientific value? Chapter 6 runs a full dual-use review of the Cascade Study's results; Chapter 8 places it in a coordinated-disclosure timeline.

### 1.5 Protected information and data agreements

#### 1.5.1 Regimes the researcher will meet

Infrastructure data often fall under legal protection regimes separate from personal-data law. In the United States, examples include Protected Critical Infrastructure Information (PCII), Chemical-terrorism Vulnerability Information (CVI), Sensitive Security Information (SSI) in transportation and Critical Energy/Electric Infrastructure Information (CEII) at the Federal Energy Regulatory Commission. Their scope and handling rules are defined by statute and regulation and change over time; read the current rule and the partner's interpretation before accepting data. In the EU, CER and NIS2 impose confidentiality on information exchanged with authorities. Personal data in interview notes, rosters and call recordings fall under ordinary privacy law (for example, the GDPR in the EU).

This book does not give legal advice. It requires that the protocol (§1.8) name each regime that may apply, the person who decided whether it applies, and the handling consequence.

#### 1.5.2 The information-sensitivity test

Even without a formal regime, apply a sensitivity test to every artifact: *Does it identify a specific asset, its location, its vulnerability or its dependency in a way that would help someone harm it?* Feeder-to-facility maps, generator fuel capacities, backup-communication paths and restoration priorities are exactly what an adversary planning a cascading effect wants. The Cascade Study's central data — which feeder serves which critical facility and how long its buffer lasts — is therefore sensitive *even when every number is approximate*. Chapter 7 builds the release tiers that follow from this.

#### 1.5.3 Agreements before access

Negotiate before collecting anything: a data-use agreement (scope, storage, retention, destruction, breach notification); a publication agreement (the partner may review for protected information and factual error within a fixed period, but may not veto findings it dislikes); an authorship and acknowledgement policy; and a staff-protection clause (research data will not be used for discipline). Record the agreements in the protocol's appendix. A study without a publication agreement has, in practice, given its partner a veto.

### 1.6 Measurement: resilience and consequence metrics

#### 1.6.1 The performance curve

Most quantitative resilience metrics summarize a **performance curve** *Q(t)*: the fraction of normal service delivered over time, before, during and after a disruption. [Bruneau et al. (2003)](https://doi.org/10.1193/1.1623497) framed seismic community resilience in terms of reduced failure probabilities, reduced consequences and reduced recovery time, and their widely reproduced "resilience triangle" measures the loss as the area between full service and *Q(t)* over the recovery period. [Haimes (2009)](https://doi.org/10.1111/j.1539-6924.2009.01216.x) argued that resilience is a function of the specific threat and system state, not a single property. NIST's [SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1) (December 2021) frames cyber resiliency as the ability to anticipate, withstand, recover from and adapt to adverse conditions, stresses or attacks on systems that use or are enabled by cyber resources.

Common summaries of *Q(t)*:

| Metric | Definition | Sensitive to | Blind to |
|---|---|---|---|
| Resilience loss (area) | ∫ (1 − Q(t)) dt over the window | Depth × duration | Whether a short deep loss is worse than a long shallow one for people |
| Worst performance | 1 − min Q(t) | Depth | Duration |
| Time to recovery | First full-service time minus disruption start | Duration | Depth |
| Customer-hours lost | Σ customers × hours without service | Population and duration | Criticality of the customers |
| Weighted critical-service loss | Σ weight × hours a critical service is unavailable | Predeclared priorities | Ordinary customers, unless included |

No metric is neutral. Each embeds a value judgment about whose loss counts and how depth trades against duration. A doctoral study must justify its primary metric by the decision it informs, report at least one alternative, and show whether conclusions change.

#### 1.6.2 Censoring

If a service has not recovered when the observation window closes, its time to recovery is **censored**: the true value is at least the observed value. Averaging censored durations as if they were complete biases results toward faster recovery. Report the number censored, use survival methods when the sample allows, or extend the window. In simulations the window is a design choice; choose it so that censoring is rare under all policies compared, or report it.

#### 1.6.3 Construct validity of consequence weights

A weighted consequence metric needs weights. Weights elicited from operators, emergency managers or published criticality frameworks are value judgments, not measurements. Predeclare them, cite where they came from, and run the analysis with alternative weight sets (Chapter 6). If the conclusion depends on one weight set, the claim must say so.

### 1.7 Common failure modes in infrastructure research claims

- **Cyber-to-consequence leap.** Treating access or malware capability as evidence of physical consequence.
- **Topology as reality.** Using a network diagram as if it captured flows, buffers, protections and human operators.
- **Testbed generalization.** Reporting detection accuracy on one small testbed as accuracy "for water systems".
- **Unvalidated simulation.** Presenting model outputs without verification, without comparison to any historical event and without sensitivity analysis.
- **Metric shopping.** Reporting whichever resilience metric favors the proposed method.
- **Sampling on the dramatic outcome.** Building theory only from famous incidents.
- **Ignoring the human buffer.** Omitting manual operation, mutual aid and improvisation, which public reports repeatedly identify as decisive in restoration.
- **Silent sensitivity.** Publishing data that enables targeting because each number "seemed harmless".

### 1.8 Writing a defensible research protocol

A protocol for an infrastructure study contains, at minimum:

1. **Question and claim rung.** The research question, the intended claim, its rung (L1–L5) and its scope (systems, sectors, jurisdictions, hazards).
2. **Definitions and metrics.** Each construct, its operationalization, primary and secondary metrics, window and censoring rule.
3. **Evidence sources.** Which of the five sources (§1.2.1), why, and what each cannot vouch for.
4. **Design.** Comparison conditions, baselines, scenario families, sampling, assignment.
5. **Pre-specification.** What is fixed before results; the deviation log.
6. **Safety and ethics.** Menlo analysis, hard rules (§1.4.2), physical-safety review, stop authority, human-subjects approval where applicable.
7. **Information protection.** Applicable regimes, sensitivity test, storage, release tiers.
8. **Agreements.** Data use, publication, authorship, staff protection.
9. **Analysis plan.** Estimators, uncertainty, sensitivity analyses, alternative metrics and weights.
10. **Stop and abandonment conditions.** When the study stops (safety, partner withdrawal, data breach) and when the claim is abandoned or narrowed (predeclared failure conditions, Chapter 3).
11. **Conflicts of interest and funding.**
12. **Reproducibility plan.** What will be released at which tier (Chapter 7).

### 1.9 Worked example: the Cascade Study's first protocol review

The doctoral candidate (synthetic) proposes to study restoration ordering in the Riverbend Region. The first draft says: *"We will obtain REC's outage records and SCADA logs for the last five years, identify cyber-related outages and show that restoring critical customers first would have reduced harm."* A protocol review finds:

| Problem | Why it fails | Revision |
|---|---|---|
| "Cyber-related outages" in five years of one cooperative | Likely zero or one event; no denominator; no variation to study. | Use historical *all-cause* distribution outages to calibrate restoration durations, and a co-simulation for cyber scenarios. |
| "Would have reduced harm" | Counterfactual with no model; hindsight. | Explicit model with predeclared parameters; tabletop study with operators blind to the outcome. |
| "Critical customers first" | Undefined; conflates customer count with criticality. | Define critical services (telecom office, water treatment, hospital, dispatch), their buffers and predeclared weights. |
| SCADA logs requested | High sensitivity; not needed for the question. | Request outage-management summaries at feeder level, aggregated; no network or protocol data. |
| No partner agreement | Partner veto by default. | Data-use and publication agreements with a 30-day factual review and no veto on findings. |
| No safety metric | A method that helps hospitals but leaves thousands of homes dark longer is a policy choice. | Secondary metric: customer-hours lost, with a non-inferiority margin justified with the partner (Chapter 3). |
| Feeder–facility map would appear in the thesis | Targeting value. | Synthetic region in public text; real mapping only in controlled-access appendix, if at all. |

The revised question becomes: *In distribution outages that require manual, sequential feeder restoration, does ordering restoration by critical-service time-to-impact reduce weighted critical-service loss compared with ordering by customers restored, and by how much does it increase customer-hours lost?* It is answerable, measurable, safe to study and honest about its trade-off.

### 1.10 Practical activity: resilience metrics can reverse rankings

The following offline lab computes three summaries of three synthetic performance curves and flags whether each is censored. Run it with Python 3; no packages are needed.

```python
# Lab 1 - resilience metrics on three synthetic performance curves (offline, standard library only)
# Q(t) = delivered fraction of normal service (1.0 = full), sampled hourly over a 48-hour window.
def curve(drop_at, depth, hold, recover_hours, window=48):
    q = []
    for t in range(window + 1):
        if t < drop_at:
            q.append(1.0)
        elif t < drop_at + hold:
            q.append(1.0 - depth)
        elif t < drop_at + hold + recover_hours:
            frac = (t - drop_at - hold) / recover_hours
            q.append(round(1.0 - depth * (1 - frac), 4))
        else:
            q.append(1.0)
    return q

def metrics(q):
    loss = sum((1.0 - a) + (1.0 - b) for a, b in zip(q, q[1:])) / 2  # trapezoid, hour units
    worst = 1.0 - min(q)
    down = [t for t, v in enumerate(q) if v < 1.0]
    if not down:
        return round(loss, 2), worst, 0, False
    recovered = q[-1] >= 1.0
    ttr = (max(down) + 1 - min(down)) if recovered else None
    return round(loss, 2), round(worst, 2), ttr, not recovered

scenarios = {
    "A_deep_short": curve(drop_at=2, depth=0.90, hold=3, recover_hours=4),
    "B_shallow_long": curve(drop_at=2, depth=0.25, hold=20, recover_hours=10),
    "C_unrecovered": curve(drop_at=30, depth=0.40, hold=30, recover_hours=6),
}
print("scenario        loss_h  worst  ttr_h  censored")
for name, q in scenarios.items():
    loss, worst, ttr, cens = metrics(q)
    print(f"{name:15} {loss:6.2f}  {worst:5.2f}  {str(ttr):5}  {cens}")
```

Expected output:

```text
scenario        loss_h  worst  ttr_h  censored
A_deep_short      4.95   0.90  7      False
B_shallow_long    6.38   0.25  30     False
C_unrecovered     7.40   0.40  None   True
```

Read the output carefully. By *worst performance*, A is far worse than B; by *area loss* and *time to recovery*, B is worse than A. Scenario C has the largest area loss in the window, but its loss is truncated at hour 48: the true loss is larger and its time to recovery is unknown. The lab demonstrates three points of §1.6: rankings depend on the metric; censoring hides the worst cases; and a single "resilience score" hides a value judgment. If A is a water-pressure loss that triggers a boil-water notice and B is a reduced-pressure period without health effect, neither area nor duration captures the decisive difference — a threshold on depth does.

### 1.11 Common errors and limits

- Treating a sector label as a population definition.
- Claiming consequences from cyber observations without the physical and organizational chain.
- Using an asset count or a network centrality as a consequence measure.
- Reporting a single resilience metric without justifying it or testing an alternative.
- Averaging censored recovery times.
- Requesting operational data the question does not need.
- Starting data collection before a publication agreement exists.
- Treating "synthetic" as a reason to skip the sensitivity test: synthetic data calibrated to a real place can still identify it.

The limit of this chapter is that integrity safeguards reduce, but do not remove, the risk of misleading results. Their purpose is to make errors *detectable* by others.

### Exercises — chapter 1

**EX001 — Claim-ladder audit.** *Objective:* separate observations from consequence claims. *Inputs:* the synthetic statement "Logs show the attacker accessed REC's distribution management system at 01:52; the resulting outage left the hospital without power and patients were endangered; this shows that rural cooperatives are the weakest point in the grid." *Constraints:* use the five rungs of §1.1.3. *Steps:* (1) split the statement into its component assertions; (2) assign each a rung; (3) name the hidden assumption behind each; (4) name one observation that would defeat each; (5) rewrite the statement so that it claims only what the evidence could support. *Expected evidence:* table and rewrite. *Rubric:* 3 = every assertion correctly laddered, the hospital-generator buffer and the generalization flagged, rewrite properly bounded; 2 = one assertion mis-laddered; 1 = rewrite still overclaims; 0 = none.

**EX002 — Definition and population.** *Objective:* see how legal definitions change a study population. *Inputs:* NSM-22 (via the CISA page), the CER Directive and NIS2 as cited in §1.1.1. *Constraints:* do not paraphrase from memory; quote the definitional text you rely on, with article or section. *Steps:* (1) for a regional hospital, a small drinking-water utility and a payment processor, state whether each is in scope of each instrument and in which category; (2) name one consequence of the differences for a cross-jurisdiction comparative study. *Expected evidence:* 3 × 3 table with citations and a paragraph. *Rubric:* 3 = accurate with exact citations and a sound design consequence; 2 = one category error; 1 = uncited; 0 = none.

**EX003 — Interdependency typing.** *Objective:* apply Rinaldi et al.'s types. *Inputs:* the Riverbend dependencies: TEL on F2; HOSP on F2 and on WATER; WATER on F3; water SCADA on TEL; the electricity cooperative's billing on the payment processor; generator fuel deliveries on road access. *Constraints:* one primary type per relation, justified. *Steps:* classify each as physical, cyber, geographic or logical; identify any cycle; state which dependency a pure power-flow model would omit. *Expected evidence:* table and a paragraph. *Rubric:* 3 = types justified, absence of a cycle among the listed services noted, fuel/road and billing identified as outside a power-flow model; 2 = one misclassification; 1 = no justification; 0 = none.

**EX004 — Menlo analysis.** *Objective:* identify stakeholders and safeguards. *Inputs:* the revised Cascade Study question in §1.9, which includes interviews with REC dispatchers and a tabletop exercise. *Constraints:* use the four principles; at least six stakeholders. *Steps:* list stakeholders; for each principle, name the main risk and a safeguard; name the stop authority and the data that are destroyed if the partner withdraws. *Expected evidence:* stakeholder table and safeguard table. *Rubric:* 3 = served population, staff discipline risk, information sensitivity and partner pressure addressed with concrete safeguards; 2 = one principle thin; 1 = generic; 0 = none.

**EX005 — Sensitivity test.** *Objective:* decide what may be published. *Inputs:* five artifacts: (a) aggregated restoration durations by feeder class; (b) a list of hospitals with generator fuel days; (c) the model code; (d) the interview coding frame; (e) a map of which feeder serves the regional water treatment plant. *Constraints:* apply §1.5.2; propose a tier: public, controlled, withheld. *Steps:* (1) decide whether each artifact identifies a specific asset, location, vulnerability or dependency; (2) assign a tier; (3) justify the tier; (4) propose a transformation that would allow wider release. *Expected evidence:* table. *Rubric:* 3 = (b) and (e) withheld or transformed, (a) and (c) public, (d) public if no quotes, with transformations; 2 = one misjudged; 1 = all public or all withheld; 0 = none.

**EX006 — Metric reversal.** *Objective:* use Lab 1. *Inputs:* the lab code. *Constraints:* offline. *Steps:* (1) run the lab and record the output; (2) add a fourth metric, "hours below 0.5", and report it for all scenarios; (3) change the window to 72 hours and report what happens to C; (4) write 150 words on which metric you would choose as primary for a drinking-water service and why. *Expected evidence:* code change, outputs, paragraph. *Rubric:* 3 = correct values, C becomes uncensored with larger loss, metric choice justified by a health threshold; 2 = one value wrong; 1 = no justification; 0 = not run.

**EX007 — Protocol skeleton.** *Objective:* write an auditable protocol. *Inputs:* the revised question in §1.9. *Constraints:* all twelve elements of §1.8; at most three pages. *Steps:* (1) draft each of the twelve protocol elements of §1.8 in order; (2) mark each element as fixed or open; (3) write two stop conditions and two abandonment conditions; (4) list what a hostile reviewer would attack first. *Expected evidence:* protocol draft. *Rubric:* 3 = all elements concrete, stop and abandonment conditions distinct, information protection specific; 2 = one or two elements vague; 1 = missing safety or agreements; 0 = none.

### Chapter synthesis

Infrastructure research studies consequences for people through chains of physical, cyber and organizational mechanisms that the researcher rarely observes directly. Its evidence comes from rare and selectively reported incidents, protected operational data, small testbeds, models and people; each source has characteristic biases and must be triangulated. Integrity safeguards — pre-specification, deviation logs, disclosure — are needed because partners are regulated, funders are interested and simulations are flexible. Safety and dual-use risks are real: never test on production, simulate first, separate capability from consequence in publication, and name a stop authority. Information about dependencies and buffers is sensitive even when approximate. Resilience metrics embed value judgments; choose them for the decision at hand and show whether conclusions survive alternatives. The protocol is the contract that makes all of this auditable.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Critical infrastructure and sector security: research frontier

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Search the scattered literature on infrastructure security and resilience across engineering, operations research, economics, policy and computer security with a documented, repeatable protocol.
2. Explain the main families of interdependency models, what each assumes and what kind of claim each can support.
3. Read standards and regulations — NIST CSF 2.0, NIST SP 800-82, IEC 62443, NERC CIP, NIS2, CER and sector guidance — as *research objects* whose effectiveness is itself an open question.
4. Appraise detection and testbed research for the evaluation pitfalls documented in the security and time-series literature.
5. Classify an evidence gap (absent, weak, conflicting, untransferred) and convert a topic into a falsifiable contribution statement.

Chapter 1 supplied the claim ladder and the evidence sources; this chapter uses them to read the field. Chapter 3 will turn the gap chosen here into a contribution proposal.

### 2.1 Why the literature is hard to find

A doctoral candidate in infrastructure security inherits at least five literatures that rarely cite each other:

| Community | Typical questions | Typical outlets and vocabulary |
|---|---|---|
| Reliability and risk engineering | Failure propagation, restoration, risk metrics, resilience curves | *Reliability Engineering & System Safety*, *Risk Analysis*; "inoperability", "resilience triangle", "fragility". |
| Power, water and transport engineering | Network physics, protection, restoration sequencing | IEEE power and smart-grid journals, water-resources journals; "service restoration", "black start", "pressure zone". |
| Operations research | Scheduling, network design, interdiction | OR journals; "weighted completion time", "interdiction", "stochastic program". |
| Computer and OT security | Attacks, detection, testbeds, protocols | Security conferences and the CPS-security workshops; "anomaly detection", "testbed", "threat model". |
| Public policy, law and management | Regulation, partnership, incentives, reporting | Policy journals and government reports; "sector risk management", "public–private partnership", "critical entity". |

Dedicated venues such as the *International Journal of Critical Infrastructure Protection* and the CRITIS conference series bridge some of these, but a search confined to security venues will miss most restoration and interdependency work, and a search confined to engineering will miss threat-informed work. Rinaldi, Peerenboom and Kelly's framework ([2001](https://doi.org/10.1109/37.969131)) is the most common shared ancestor and a good seed for citation chaining in both directions.

### 2.2 Systematic scoping across disciplines

#### 2.2.1 Choosing the review type

A **systematic review** answers a focused question with an exhaustive search and formal appraisal; a **scoping review** maps the extent and nature of a body of work; a **narrative review** is an expert synthesis without a reproducible search. For a doctoral frontier chapter, a scoping review with a documented protocol is usually right: it is reproducible, it shows the shape of the field and it identifies where a systematic review would be premature. Report it using the relevant items of [PRISMA 2020](https://doi.org/10.1136/bmj.n71) — search sources, dates, strings, screening, reasons for exclusion and a flow diagram — even where the full checklist does not apply.

#### 2.2.2 A search protocol for the Cascade Study

1. **Question.** What is known about the effect of restoration ordering, informed by cross-sector dependencies, on the consequences of infrastructure outages, including cyber-induced outages?
2. **Concept blocks.** (restoration OR recovery OR "service restoration" OR prioritization) AND (interdependen* OR dependen* OR cascad*) AND (infrastructure OR utility OR "distribution system" OR "lifeline").
3. **Sources.** At least one engineering index, one general scholarly index and one policy source (government reports, after-action reports), plus backward and forward citation chaining from two seed papers.
4. **Eligibility.** Studies that compare at least two restoration orderings or that quantify dependency-driven consequence; exclude purely topological vulnerability rankings that do not model service.
5. **Screening.** Two screeners on a sample of titles and abstracts with agreement measured before splitting the work; disagreements resolved by discussion and logged.
6. **Coding frame.** Model family; validation type (none, face, historical, field); data source; whether the authors also built the testbed or model they evaluate; outcome metric; hazard type (natural, accidental, cyber); comparison baseline.
7. **Stopping rule.** Stop chaining when two consecutive rounds add no eligible study.

#### 2.2.3 Appraisal for models and simulations

Clinical appraisal tools fit poorly. For model-based papers, appraise: Is the model's structure justified by the mechanism it represents? Are parameters sourced? Was the implementation verified (does the code do what the paper says)? Was the model validated, and against what — face validity, historical events, field data ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20))? Is there a sensitivity analysis? Is the comparison baseline strong? Are code and inputs available? A model paper that cannot answer the verification and validation questions supports at most a claim about the model, not about infrastructure.

### 2.3 The policy and standards landscape as a research object

Standards and regulations are not only background; whether they work is one of the field's biggest open questions. The current landscape (verify versions before citing):

- **NIST Cybersecurity Framework 2.0** ([CSWP 29, February 2024](https://doi.org/10.6028/NIST.CSWP.29)) added a *Govern* function to Identify, Protect, Detect, Respond and Recover. It is outcome-based and voluntary in most sectors; research question: do organizations that adopt it experience fewer or less consequential disruptions, and how would one know?
- **NIST SP 800-82 Rev. 3** ([September 2023](https://doi.org/10.6028/NIST.SP.800-82r3)) broadened scope from industrial control systems to operational technology and added an OT overlay for SP 800-53 Rev. 5 controls. An initial public draft of Rev. 4 was released in September 2026 ([CSRC](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).
- **ISA/IEC 62443** is a series of standards for industrial automation and control system security. Part 3-2 defines the system under consideration, partitions it into **zones** and **conduits**, assesses risk and assigns a **target security level (SL-T)**; Part 3-3 states system requirements under seven foundational requirements — identification and authentication control, use control, system integrity, data confidentiality, restricted data flow, timely response to events and resource availability ([IEC 62443-3-2 catalogue page](https://webstore.iec.ch/en/publication/30727)). Research question: does an assigned SL-T predict resistance to realistic adversaries, and how can achieved security levels be measured rather than asserted?
- **NERC CIP** reliability standards are mandatory for the North American bulk electric system. In June 2025 FERC approved [CIP-015-1 on internal network security monitoring](https://www.federalregister.gov/documents/2025/07/02/2025-12309/critical-infrastructure-protection-reliability-standard-cip-015-1-cyber-security-internal-network) (Order No. 907), with implementation phased over years ([NERC standard page](https://www.nerc.com/standards/reliability-standards/cip/cip-015-1)). A mandatory standard with a phased rollout is a natural experiment — if researchers can obtain outcome data, which is rarely the case.
- **EU NIS2 and CER** (both 2022) impose risk-management and reporting obligations on essential and important entities and resilience obligations on critical entities; national transposition varies, which creates cross-country variation of research interest.
- **Finance.** The CPMI–IOSCO [Guidance on cyber resilience for financial market infrastructures](https://www.bis.org/cpmi/publ/d146.htm) (June 2016) supplements the Principles for Financial Market Infrastructures; it is the source of the widely discussed expectation that critical operations be designed to resume quickly after a disruption, which creates a tension between speed of resumption and integrity of data — a research problem with no settled answer.
- **Consequence-driven Cyber-informed Engineering (CCE)**, developed at Idaho National Laboratory, proceeds through four phases — consequence prioritization, system-of-systems analysis, consequence-based targeting, and mitigations and protections ([INL CCE page](https://inl.gov/national-security/cce/); [Bochman and Freeman, 2021](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710)). It starts from consequences rather than vulnerabilities, which aligns with this book's emphasis; whether it yields better mitigation choices than vulnerability-driven methods has, to the author's knowledge, not been tested with comparative designs.

The common research gap across the landscape is **outcome evidence**: the frameworks are justified by expert consensus and incident lessons, but comparative studies linking their adoption to consequences are rare, because outcome data are rare, protected and confounded by organizational maturity.

### 2.4 Interdependency modelling families

[Ouyang (2014)](https://doi.org/10.1016/j.ress.2013.06.040) reviewed modelling and simulation of interdependent infrastructure systems and grouped approaches into empirical, agent-based, system-dynamics-based, economic-theory-based, network-based and other approaches. Each family supports a different kind of claim.

| Family | Core idea | Supports claims about | Main limits |
|---|---|---|---|
| Empirical | Analyse records of past disruptions and their spread | What has happened; frequency of dependency types in reports | Reporting bias; few events; no counterfactuals |
| Agent-based | Simulate autonomous decision-makers and assets | Emergent behaviour, operator decisions | Many parameters; validation hard |
| System dynamics | Stocks, flows and feedback loops over time | Aggregate dynamics, policy feedback | Coarse; structure assumed |
| Economic (input–output) | Leontief-style propagation of inoperability or output loss between sectors ([Haimes and Jiang, 2001](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1))) | Sector-level economic loss and ranking | Linear, static or quasi-static; sector aggregation hides facilities |
| Network — topology | Graphs and percolation | Structural fragility; qualitative cascade regimes | No flows, buffers or operators |
| Network — flow | Physical flows (power flow, hydraulics) on networks | Engineering consequences within a sector | Data-hungry; cross-sector coupling hard |
| Co-simulation | Couple domain simulators (power, water, communications) | Cross-sector timing with physical fidelity | Integration error; synchronization; heavy |

**Topological cascades.** [Buldyrev et al. (2010)](https://doi.org/10.1038/nature08932) showed in a percolation model of two interdependent networks that the coupling can produce abrupt, catastrophic collapse and that, unlike in single networks, broader degree distributions can increase vulnerability to random failure. The result is a landmark for structural insight. It is also a frequent source of overclaiming: the model assumes all-or-nothing dependence, no buffers, no restoration and specific coupling patterns. Citing it as evidence that a particular city's power and communications will collapse abruptly is a category error — L5 structural insight presented as an L4 consequence claim.

**Input–output inoperability.** The inoperability input–output model (IIM) writes the equilibrium inoperability vector *q* as *q* = *A\*q* + *c\**, so *q* = (*I* − *A\**)⁻¹ *c\**, where *A\** holds interdependency coefficients and *c\** an initial perturbation. Chapter 4 replicates an IIM calculation and shows how a matrix-convention error silently changes results.

**Where buffers live.** A theme across families is that consequence timing is governed by **buffers** — generator fuel, battery autonomy, storage, inventory, manual procedures — that topology ignores and that flow models often hold constant. Restoration research in power engineering does model sequencing, but frequently within one sector and with the objective of customers or load restored. The Cascade Study sits in this seam: cross-sector buffer timing as the driver of *restoration ordering*.

### 2.5 Detection and testbed research: evaluation as a frontier

Much of the security-side literature studies attack detection in industrial processes. Its problems are increasingly well documented:

- **Closed-world evaluation.** [Sommer and Paxson (2010)](https://doi.org/10.1109/SP.2010.25) argued that machine-learning intrusion detection is poorly matched to the open, shifting world of real networks, and that evaluations often fail to capture the cost of errors and the semantic gap between an anomaly and an attack.
- **Pitfalls in ML security research.** [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) identified ten pitfalls — among them sampling bias, data snooping, spurious correlations, inappropriate baselines and metrics, the base-rate fallacy, lab-only evaluation and inappropriate threat models — and found several in each of 30 top-venue papers they reviewed.
- **Inflated time-series metrics.** [Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) showed that the *point adjustment* protocol common in time-series anomaly detection, which marks a whole anomalous segment as detected if any point in it is flagged, can make even random scores look state-of-the-art; they proposed PA%K. Chapter 4 reproduces the effect.
- **Small, old, author-built testbeds.** Public datasets from testbeds such as SWaT ([Goh et al., 2016](https://doi.org/10.1007/978-3-319-71368-7_8)) and the BATADAL water-distribution competition ([Taormina et al., 2018](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969)) enabled comparison, which is a major contribution. They also concentrate the field on a few systems with specific attack sets; results transfer to other plants only by argument.

For a CI thesis, detection is relevant mainly as a **buffer against consequence**: detection that arrives after a service's buffer is exhausted changes nothing for the people served. Framing detection by time-to-consequence rather than by F1 is an under-explored bridge between the two literatures.

### 2.6 Sector-specific and threat evidence

- **Energy.** The 2015 Ukrainian distribution attack, documented by [E-ISAC and SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and), is the most cited public case of a cyber attack causing customer outages; it is also one case, with restoration achieved through manual operation.
- **Water.** Water systems are numerous, often small and under-resourced, which makes sector-wide evidence hard to collect; much quantitative work uses simulated distribution networks such as BATADAL's.
- **Healthcare.** [Neprash et al. (2022)](https://doi.org/10.1001/jamahealthforum.2022.4873) documented a rising number of ransomware attacks on U.S. health care delivery organizations from 2016 to 2021 and their effects on operations; such work connects a cyber event to care delivery — the consequence rung — using public and regulatory data.
- **Threat model shift.** CISA's joint advisory [AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a) (February 2024) assessed that a state-sponsored actor known as Volt Typhoon pre-positioned in IT networks of communications, energy, transportation and water organizations to enable potential disruption, using valid accounts and living-off-the-land techniques. For research, pre-positioning means that the relevant scenario is *simultaneous, multi-sector, adversary-timed* disruption — exactly where single-sector restoration rules may fail.
- **Cyber-physical precedent.** [Langner's 2013 analysis of Stuxnet](https://archive.org/details/to-kill-a-centrifuge) is a classic account of a cyber-physical attack designed around process knowledge. Its lesson for CI research is that consequential attacks are engineered against physical processes and their safety margins, which is why consequence-first methods such as CCE exist.

### 2.7 Classifying the gap

The IR doctoral book distinguishes four kinds of evidence gap; they apply here unchanged:

| Gap type | Meaning | Infrastructure example | Right next study |
|---|---|---|---|
| Absent | No study addresses the question | No comparative test of CCE against vulnerability-driven prioritization | First comparative design, even small |
| Weak | Studies exist but cannot support the claim | Restoration-ordering benefits shown only in unvalidated models built by the proposers | Independent validation; stronger baselines |
| Conflicting | Credible studies disagree | Topological and flow models rank the same assets differently | Study that discriminates between mechanisms |
| Untransferred | Evidence exists in another domain | Hospital surge-planning evidence not applied to restoration ordering | Transfer test with explicit boundary conditions |

### 2.8 Worked example: appraising the restoration-ordering literature (synthetic)

The Cascade Study's scoping review (synthetic) found eight eligible papers, P1–P8:

| ID | Family | Validation | Independent of the authors' own model or testbed? | Claim supported |
|---|---|---|---|---|
| P1 | Network topology | None | No | C1 centrality identifies most consequential assets |
| P2 | Network topology | Face (expert review) | No | C1 |
| P3 | Input–output | Historical (regional outage) | Yes | C2 IIM ranks sectors by economic loss |
| P4 | Agent-based | Face | No | C3 dependency-aware restoration reduces critical loss |
| P5 | Co-simulation | Historical | No | C3 |
| P6 | Input–output | Historical | Yes | C2 |
| P7 | Co-simulation | Field (utility exercise) | Yes | C3 |
| P8 | Empirical | Field (after-action records) | Yes | C4 backup-power duration dominates cascade timing |

Appraisal: C1 has only self-validated topological evidence — it is *weak*. C2 has two independent historical validations — the strongest claim in the set, though about economic loss, not service. C3 has three studies but only one that is independent and strongly validated; P4 and P5 were evaluated in the authors' own models, which invites model–policy circularity (Chapter 6). C4 rests on one empirical study. The frontier is therefore C3: plausible, repeatedly *proposed*, weakly *tested*.

### 2.9 Practical activity: code the literature map

```python
# Lab 2 - coding a synthetic literature map for interdependency-modelling claims (offline)
# Fields: id, model family, validation, independent of authors' own testbed?, claim supported
studies = [
    ("P1", "network-topology", "none",       False, "C1"),
    ("P2", "network-topology", "face",       False, "C1"),
    ("P3", "input-output",     "historical", True,  "C2"),
    ("P4", "agent-based",      "face",       False, "C3"),
    ("P5", "co-simulation",    "historical", False, "C3"),
    ("P6", "input-output",     "historical", True,  "C2"),
    ("P7", "co-simulation",    "field",      True,  "C3"),
    ("P8", "empirical",        "field",      True,  "C4"),
]
claims = {
    "C1": "Topological centrality identifies the assets whose loss causes the largest service cascade",
    "C2": "Input-output inoperability ranks sectors by economic loss after a regional outage",
    "C3": "Dependency-aware restoration lowers critical-service loss compared with siloed restoration",
    "C4": "Backup-power duration is the dominant buffer controlling cascade timing",
}
STRONG = {"historical", "field"}
for cid, text in claims.items():
    rows = [s for s in studies if s[4] == cid]
    strong_indep = [s[0] for s in rows if s[2] in STRONG and s[3]]
    if len(strong_indep) >= 2:
        state = "supported (>=2 independent strong validations)"
    elif strong_indep:
        state = "single-source; needs replication"
    else:
        state = "open: no independent strong validation"
    print(f"{cid}: {state}; evidence={[s[0] for s in rows]}; strong+independent={strong_indep}")
```

Expected output:

```text
C1: open: no independent strong validation; evidence=['P1', 'P2']; strong+independent=[]
C2: supported (>=2 independent strong validations); evidence=['P3', 'P6']; strong+independent=['P3', 'P6']
C3: single-source; needs replication; evidence=['P4', 'P5', 'P7']; strong+independent=['P7']
C4: single-source; needs replication; evidence=['P8']; strong+independent=['P8']
```

Record exact output in your reproduction log, not a paraphrase.

The rule encoded in `STRONG` and in the independence flag is a *choice*. Changing it changes which claims are "supported". A literature map must publish its coding rule so readers can disagree with it explicitly.

Two checks are worth making before trusting the map. First, run it with the independence flag removed: C3 then counts P5 as a strong validation and is reported as supported, which shows how much of the verdict rests on that one coding decision. Second, have a second coder classify validation and independence for all eight papers without seeing the first coder's sheet, and record where they disagree. Disagreement over whether a utility exercise counts as field validation, as in P7, is a finding about the coding frame, and the frame should be tightened before the map is used to choose a gap.

### 2.10 From map to frontier: the contribution test

A gap becomes a doctoral contribution when it passes four tests: **Open** — the documented search shows it is not already answered; **Important** — an answer would change a decision someone actually makes (here, restoration ordering in emergency operations); **Feasible** — data, models, partners and ethics allow it within the program; **Falsifiable** — a stated observation would show the claim wrong. Drafting format: *"In [population/context], [intervention] compared with [strongest baseline] will change [primary metric] by at least [smallest effect of interest] without worsening [safety metric] beyond [margin]; this will be refuted if [observation]."*

The Cascade Study's statement (to be refined in Chapter 3): *In distribution outages requiring sequential manual feeder restoration, ordering by critical-service time-to-impact, compared with ordering by customers restored, reduces predeclared weighted critical-service loss by at least 20%, while increasing customer-hours lost by no more than 15%; this is refuted if the reduction is below 20% in an independently built model of a second region, or if operators in a blinded tabletop do not choose the ordering when given the same information.*

### 2.11 Common errors and limits

- Searching only security venues and declaring a gap that engineering has already filled.
- Citing percolation results as consequence predictions for specific places.
- Treating standards as evidence of effectiveness rather than as hypotheses about it.
- Comparing detection papers by headline F1 without checking the evaluation protocol.
- Counting studies instead of appraising their independence and validation.
- Writing a gap as a topic ("interdependencies in smart cities") instead of a falsifiable statement.

- Treating a dedicated venue such as the CRITIS series as covering the whole field, when most restoration work appears in engineering and operations-research outlets.
- Reading a framework's widespread adoption as outcome evidence; adoption shows that people chose it, not that consequences fell.
- Coding a paper as independent because its authors differ from the proposers, without checking whether it reuses the proposers' model or testbed.
- Stopping citation chaining early because the first rounds confirmed the expected gap.

### Exercises — chapter 2

**EX008 — Search protocol.** *Objective:* write a reproducible cross-disciplinary search. *Inputs:* a question of your choice about infrastructure security or resilience. *Constraints:* at least three source types (engineering index, general index, policy source); citation chaining. *Steps:* (1) state the question; (2) build concept blocks and strings; (3) define eligibility and exclusion reasons; (4) define screening, agreement and stopping rule. *Expected evidence:* protocol (≤ 2 pages). *Rubric:* 3 = repeatable, cross-disciplinary, agreement measured, stopping rule explicit; 2 = one element vague; 1 = keyword list only; 0 = none.

**EX009 — Model-paper appraisal.** *Objective:* appraise a simulation paper for the claim it can support. *Inputs:* synthetic study P5 (co-simulation, historical validation, authors' own model). *Constraints:* use §2.2.3. *Steps:* list what you would check for structure, parameters, verification, validation, sensitivity, baseline and availability; state the strongest claim P5 can support and its rung. *Expected evidence:* appraisal form and one-sentence claim. *Rubric:* 3 = identifies self-built model, unknown verification, single historical event and baseline strength as decisive, claim limited to the model; 2 = one issue missed; 1 = accepts claim as L5; 0 = none.

**EX010 — Model-family fit.** *Objective:* match questions to modelling families. *Inputs:* four questions: (a) Which sectors lose most output after a week-long regional power loss? (b) How long until a hospital loses water pressure after a feeder outage? (c) Do operators share fuel informally between utilities during long outages? (d) Is a two-network system with random coupling prone to abrupt collapse? *Constraints:* one primary family per question, with a reason and a limit. *Steps:* (1) restate what each question asks you to predict or explain; (2) choose the primary modelling family from §2.4; (3) justify the choice by the claim it supports; (4) name the family's most important limit for that question. *Expected evidence:* table. *Rubric:* 3 = (a) input–output, (b) flow/co-simulation or buffer model, (c) empirical/qualitative or agent-based informed by interviews, (d) topology/percolation, each with sound limits; 2 = one mismatch; 1 = two or more; 0 = none.

**EX011 — Standard as hypothesis.** *Objective:* turn a standard into a testable claim. *Inputs:* IEC 62443-3-2 zones, conduits and SL-T (§2.3). *Constraints:* one testable hypothesis; name the outcome measure and a feasible design. *Steps:* state the implicit causal claim of the standard; write a hypothesis; propose a design (e.g., red-team exercises on testbed zones at different SL-T); name two confounders. *Expected evidence:* one page. *Rubric:* 3 = hypothesis observable, design safe and feasible, confounders real (assessor skill, asset age); 2 = design vague; 1 = restates the standard; 0 = none.

**EX012 — Repair the literature map.** *Objective:* make a coding rule match a stated standard. *Inputs:* Lab 2. *Constraints:* offline; keep all rows. *Steps:* (1) add a `hazard` field (P5 and P7 "cyber", all others "all-hazards"); (2) change the rule so that a claim about *cyber-induced* outages is supported only by independent strong validations with hazard "cyber"; (3) run and record exact output for C3; (4) explain in 100 words what changed and why it matters. *Expected evidence:* modified code, exact output, explanation. *Rubric:* 3 = correct code; C3 remains single-source (P7 only), and the learner notes that C1, C2 and C4 now have no strong independent support for *cyber-induced* outages, with a clear explanation of hazard transfer; 2 = output correct, explanation thin; 1 = rule wrong; 0 = not run.

**EX013 — Classify the gap.** *Objective:* distinguish gap types. *Inputs:* four synthetic statements: (a) "Two flow-model studies disagree on whether water storage or generator fuel dominates hospital outage timing"; (b) "Hospital surge-capacity research exists, but no study links it to restoration ordering"; (c) "Three vendor white papers claim their platform halves restoration time"; (d) "No study in our documented search compares CCE with vulnerability-driven prioritization." *Constraints:* one type each, justified; propose the next study. *Steps:* (1) restate each as a question; (2) list the evidence for it; (3) assign one gap type; (4) name the study that would close it. *Expected evidence:* four paragraphs. *Rubric:* 3 = conflicting, untransferred, weak, absent with sound next steps; 2 = one error; 1 = two errors; 0 = none.

**EX014 — Falsifiable statement and frontier memo.** *Objective:* convert a topic into a contribution. *Inputs:* the topic "resilience of payment systems during regional power outages". *Constraints:* use the drafting format in §2.10; the refuting observation must be feasible; 400–600 words; cite only sources you have read. *Steps:* (1) write the statement; (2) apply the four tests; (3) revise once; (4) explain which adjacent question must be answered first and why. *Expected evidence:* statement, test notes, revision, memo. *Rubric:* 3 = passes all tests with a feasible refuter and a justified ordering of questions; 2 = one test weak; 1 = still a topic; 0 = none.

### Chapter synthesis

The infrastructure-security frontier is spread across five literatures with different vocabularies; a doctoral search must cross them deliberately and document how. Standards and regulations are hypotheses about what reduces consequence, and outcome evidence for them is scarce. Interdependency models come in families that support different claims; topological results give structural insight, input–output models give sector-level economics, and flow or co-simulation models give engineering timing — none substitutes for validation. Detection research is improving its evaluation practice; for CI, detection matters as a buffer measured against time-to-consequence. Appraise independence and validation, not counts. The Cascade Study's gap — dependency-aware restoration ordering is often proposed and weakly tested — is open, important, feasible and can be made falsifiable.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 08

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Original contribution proposal

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Type a doctoral contribution (artifact, method, measurement, empirical finding, theory) and state the evidence each type requires.
2. Specify a mechanism as a chain of links that predicts a *pattern* of results, including where the intervention should not help.
3. Represent cross-sector dependencies as a graph with buffers, compute time-to-impact, and explain what the representation leaves out.
4. Relate restoration ordering to classical scheduling theory and use that relation to choose baselines and predict trade-offs.
5. Write primary, mechanism, contribution-over-best-practice and non-inferiority hypotheses with a justified smallest effect of interest.
6. Build a rival-explanation table and a set of predeclared failure conditions that would narrow or abandon the claim.

Chapter 2 identified the gap: dependency-aware restoration ordering is often proposed and weakly tested. This chapter turns it into a proposal that could be wrong. Chapter 4 will replicate the baselines and pilot the procedure.

### 3.1 What kind of contribution?

| Type | Example in CI security | Minimum evidence |
|---|---|---|
| Artifact | An open co-simulation of distribution, water and telecom | Verification tests; documentation; evidence of use by others |
| Method | A procedure for computing restoration priorities from dependency data | Comparison against the strongest current practice on stated metrics, in more than one context |
| Measurement | A validated instrument for buffer duration or dependency-map accuracy | Reliability and validity evidence |
| Empirical finding | "Operators already prioritize critical facilities but do not use buffer timing" | A sampled, documented study of operators |
| Theory | A mechanism explaining when dependency-aware ordering helps | Predictions that discriminate it from rivals, tested |

The Cascade Study's intended contribution is a **method with a mechanism**: a rule for ordering restoration (the artifact is incidental) and an account of *when* it outperforms current practice. Saying this early matters, because "we built a simulator and our method won" is an artifact demonstration, not a method contribution.

### 3.2 Restoration ordering as a scheduling problem

When a single restoration crew must restore feeders one at a time, restoration ordering is a **single-machine scheduling problem**: each feeder *j* is a job with processing time *p_j* (manual switching, inspection, re-energization) and the objective depends on what is being minimized.

- If the objective is **customer-hours lost**, each feeder contributes (customers on *j*) × (completion time *C_j*). Minimizing Σ *w_j C_j* on one machine is solved exactly by ordering jobs by *w_j / p_j* in decreasing order — **Smith's rule** ([Smith, 1956](https://doi.org/10.1002/nav.3800030106)). With equal expected restoration times, this is simply "most customers first". The conventional ordering used as a baseline in this book is therefore not naive: it is *optimal for customer-hours* in this idealized setting.
- If the objective is **critical-service loss**, a service *s* fed by feeder *j* is lost only from the moment its buffer *b_s* is exhausted until the feeder is restored: loss_s = *w_s* × max(0, *C_j* + lag − *b_s*). The buffer acts like a due date, and the objective resembles **weighted tardiness**. Single-machine total weighted tardiness is strongly NP-hard ([Lenstra, Rinnooy Kan and Brucker, 1977](https://doi.org/10.1016/S0167-5060(08)70743-X)), so practical rules are heuristics. Ordering by earliest due date — here, earliest time-to-impact — is a classical heuristic that ignores weights.

This relation gives the study three things a purely security framing would miss. First, a **theoretical prediction of the trade-off**: any ordering that departs from Smith's rule must increase expected customer-hours, so a non-inferiority margin on customer-hours is not optional. Second, an **upper bound on achievable benefit**: with few feeders, exhaustive enumeration gives an oracle ordering for each scenario draw, which shows how much room any heuristic leaves. Third, **a known failure mode of the proposed heuristic**: an earliest-time-to-impact rule ignores weights and fan-out, so it can lose to a rule that restores the feeder protecting the most weighted services, even if that feeder's first impact is slightly later. Chapter 6 shows exactly this.

### 3.3 Dependency graphs with buffers

#### 3.3.1 Representation

Represent each supplier → dependant relation as a directed edge labelled with the dependant's buffer for that supplier. If supplier *A* fails at time *t_A*, dependant *B* fails at *t_A* + *b_AB* unless restored first. If *B* fails when *any* of its suppliers fails (an "OR" of failures — no redundancy), *B*'s failure time is the minimum over incoming paths, which is a shortest-path computation with buffers as edge weights.

#### 3.3.2 Time-to-impact lab

```python
# Lab 3 - time-to-impact on a synthetic Riverbend dependency graph (offline, standard library only)
# Edge (supplier -> dependant, buffer_hours): the dependant fails `buffer_hours` after it loses that supplier.
import heapq
edges = [
    ("F2", "TEL", 8),     # telecom central office: batteries plus generator fuel on hand
    ("F2", "HOSP", 26),   # hospital: generator fuel on hand
    ("F3", "WATER", 9),   # treatment plant generator + clearwell storage
    ("F3", "WSCADA", 2),  # water SCADA server UPS
    ("TEL", "WSCADA", 0), # remote telemetry needs the carrier circuit
    ("WATER", "HOSP", 4), # hospital on-site water storage
    ("TEL", "DISPATCH", 1),  # emergency dispatch: ring-down backup lasts 1 h
    ("F1", "RES", 0), ("F4", "COM", 0),
]
def time_to_impact(initial):  # initial: {node: failure time}
    graph = {}
    for s, d, b in edges:
        graph.setdefault(s, []).append((d, b))
    best = dict(initial)
    pq = [(t, n) for n, t in initial.items()]
    heapq.heapify(pq)
    while pq:
        t, n = heapq.heappop(pq)
        if t > best.get(n, float("inf")):
            continue
        for d, b in graph.get(n, []):
            if t + b < best.get(d, float("inf")):
                best[d] = t + b
                heapq.heappush(pq, (t + b, d))
    return best
tti = time_to_impact({"F1": 0, "F2": 0, "F3": 0, "F4": 0})
for node in sorted(tti, key=lambda n: (tti[n], n)):
    print(f"{node:9} fails at t={tti[node]:>3} h")
degree = {}
for s, d, _ in edges:
    degree[s] = degree.get(s, 0) + 1
    degree[d] = degree.get(d, 0) + 1
print("degree ranking:", sorted(degree, key=lambda n: (-degree[n], n))[:4])
```

Expected output:

```text
COM       fails at t=  0 h
F1        fails at t=  0 h
F2        fails at t=  0 h
F3        fails at t=  0 h
F4        fails at t=  0 h
RES       fails at t=  0 h
WSCADA    fails at t=  2 h
TEL       fails at t=  8 h
DISPATCH  fails at t=  9 h
WATER     fails at t=  9 h
HOSP      fails at t= 13 h
degree ranking: ['TEL', 'F2', 'F3', 'HOSP']
```

Three lessons. **Indirect paths dominate:** the hospital's own generator gives 26 hours, but it fails at hour 13 through the water path (9 + 4). A study that recorded only each facility's direct power buffer would misjudge its priority by half a day. **Degree is not consequence:** degree centrality ranks TEL first, which is reasonable here, but it ranks HOSP above WATER and says nothing about timing. **The OR assumption is strong:** water SCADA fails at hour 0 + 0 via TEL *only* if telemetry has no alternative path; in many utilities operators can run the plant locally without SCADA, so WSCADA's failure may have no service consequence. The graph must distinguish *loss of a function* from *loss of a service*.

#### 3.3.3 What the representation leaves out

Edges with fixed buffers omit: **depletion dynamics** (a generator's fuel lasts longer at partial load); **redundancy** ("AND" logic — a hospital with two independent feeds fails only when both fail); **restoration dependencies** (a feeder cannot be re-energized without communications to field crews — a dependency in the *recovery* direction); **human buffers** (manual operation, mutual aid, fuel deliveries that extend buffers if roads and telecom work); and **adversary adaptation** (an adversary who knows the priority list can target its top). A proposal must list which omissions could reverse its conclusions and how the study will test them (§3.7).

### 3.4 The mechanism

A mechanism is a chain of links, each of which could fail, that predicts a *pattern*, not only an average effect:

1. Critical services draw on buffers whose durations differ widely (hours for telecom batteries and dispatch backups, days for hospital fuel).
2. In a multi-feeder outage requiring sequential manual restoration, the order of restoration determines which buffers are exhausted.
3. Conventional practice either maximizes customers restored (Smith's rule) or restores "critical customers" first in an order that does not use buffer timing.
4. Ordering by time-to-impact restores the feeders whose critical services would fail first, so fewer buffers are exhausted.
5. Therefore weighted critical-service loss falls.

The mechanism predicts a pattern:

- **Benefit over customer-first ordering** whenever critical services sit on feeders with few customers.
- **Benefit over critical-flag ordering only when they disagree** — when the buffer-time order among critical feeders differs from the customer-count order among them. When the orders coincide, the two rules are identical and the benefit must be zero.
- **No benefit when buffers exceed total restoration time** — if every buffer outlasts the outage, ordering cannot matter for critical services.
- **A cost in customer-hours** relative to Smith's rule, larger when critical services sit on small feeders.
- **Fragility to map error** — if the dependency map or buffers are wrong, the ordering can be worse than a simple flag list.

A mechanism that predicts where the intervention fails is worth more than one that predicts only success, because the failures are what distinguish it from rivals.

### 3.5 Hypotheses, metrics and the smallest effect of interest

Primary metric: **weighted critical-service loss** over a 72-hour window, with predeclared weights (hospital 5, water 4, telecom 3, emergency dispatch 4 per service-hour), elicited from the partners' emergency-management staff before any simulation (Chapter 1, §1.6.3). Secondary (safety) metric: **customer-hours lost** (thousands).

- **H1 (benefit over customer-first).** DEP reduces mean weighted critical-service loss by at least 20% compared with SILO.
- **H2 (contribution over best practice).** DEP reduces mean weighted critical-service loss by at least 10% compared with CRITFLAG (critical-customer flag list ordered by customers), in each study region.
- **H3 (mechanism pattern).** The DEP − CRITFLAG difference is zero when the two orders coincide and grows with the number of positions in which they differ; it shrinks toward zero as buffers grow relative to restoration time.
- **H4a/H4b (non-inferiority).** DEP increases mean customer-hours lost by no more than 15% compared with SILO (H4a) and with CRITFLAG (H4b).

**Smallest effects of interest.** The 20% and 10% thresholds and the 15% margin are *practical* judgments, not statistical conventions: partners stated (synthetic) that a change in restoration practice requires retraining, procedure revision and regulator explanation, which they would undertake only for a reduction of at least 10% in critical-service loss relative to their current critical-flag practice; and the cooperative's board would not accept more than 15% additional customer-hours without public consultation. Record who set each threshold and when; a threshold chosen after seeing results is worthless.

Note that H4a is predicted to *fail* by scheduling theory whenever critical services sit on small feeders. Predeclaring it anyway is correct: the study should report the size of the trade-off honestly rather than hide it, and a failed non-inferiority test is a finding for policy-makers.

### 3.6 Baselines

A contribution is only as strong as the baseline it beats.

| Baseline | Why include it | What beating it would show |
|---|---|---|
| **SILO** — most customers first | Optimal for customer-hours under equal durations (Smith's rule); common default | That criticality-aware ordering protects critical services — expected and weak as a contribution |
| **CRITFLAG** — feeders with any listed critical facility first, by customers | Represents widespread practice of maintaining critical-customer lists | The actual contribution: that *timing* information adds value beyond a list |
| **ORACLE** — best of all orderings for each draw (computable for ≤ 6–7 feeders) | Upper bound on any rule | How much room is left; whether DEP is near-optimal |
| **RANDOM** (optional) | Sanity check | That the metric is not degenerate |

Beating SILO is necessary but not sufficient; the claim lives or dies against CRITFLAG. The worked example in §3.9 shows how a proposal that omitted CRITFLAG would have looked impressive and been wrong.

### 3.7 Rival explanations

| Rival | Prediction that would support it | Design feature that tests it |
|---|---|---|
| Any criticality list explains the gain, not timing | DEP ≈ CRITFLAG | CRITFLAG baseline; H2 |
| The gain is an artifact of weights | Gain disappears with equal or alternative weights | Weight sensitivity (Chapter 6) |
| The gain is an artifact of short buffers in the chosen region | Gain vanishes with realistic longer buffers | Buffer-scaling analysis; second region with fuel contracts |
| The model was built to favor DEP (circularity) | Gain shrinks in an independently built model or with a wrong map | Second region built by a different modeller from partner data; map-error test |
| Operators would not follow the ordering | Tabletop choices differ from DEP even with time-to-impact display | Blinded operator tabletop (Chapter 5) |
| One-crew assumption drives the result | Gain disappears with several crews | Port Halvard with two crews |
| Discretization or implementation error | Results change with time step or implementation | Verification against an independent event-based implementation (Chapter 4) |

### 3.8 Failure conditions and risk register

**Predeclared failure conditions** (each maps to a claim change):

| Condition | Consequence for the claim |
|---|---|
| H2 fails in both regions | Abandon the method contribution; report that timing adds nothing measurable over critical-flag lists; retain the scheduling analysis as a theoretical contribution. |
| H2 fails in one region and holds in the other | Narrow to the conditions that distinguish them; test H3 to see if the mechanism explains the difference. |
| H3 pattern absent (gain unrelated to order divergence) | Mechanism unsupported; any gain is unexplained and must not be generalized. |
| H4b fails | Report a trade-off; the method is not "free" relative to current practice. |
| Gain collapses under plausible map errors | Claim conditional on map accuracy; add map-audit as a prerequisite. |
| Operators reject the ordering in tabletop | Claim limited to "a decision aid whose adoption is unproven"; study adoption barriers. |

**Risk register** (selection): partner withdrawal (mitigation: synthetic-region design that does not depend on one partner's data); sensitive data exposure (tiered storage, no real maps in public text); simulator error (independent re-implementation and unit tests); tabletop participants identifiable (aggregate reporting, no role-plus-utility combinations in public text); funder pressure (publication agreement signed before work starts).

### 3.9 Worked example: the proposal that nearly omitted the real baseline

The candidate's first draft compared DEP with SILO only and reported, in a pilot run, an almost 90% reduction in weighted critical-service loss. The supervisory committee asked two questions: *What do utilities actually do today?* and *What would a perfect ordering achieve?* Interviews (synthetic) with three dispatchers revealed that all three utilities keep a critical-customer list and restore those feeders early. The candidate added CRITFLAG and ORACLE. The pilot then showed DEP and CRITFLAG nearly indistinguishable in Riverbend, both far from ORACLE. The committee's verdict: the 90% figure measured the value of *having a critical-customer list*, which is not new; the open question is whether *timing* adds value, and Riverbend alone — with only two critical feeders, ordered the same way by most rules — cannot answer it. The proposal was revised to predeclare H2 and H3, to choose a second region on stated design criteria (more critical feeders, divergent buffer and customer orders, two crews, fuel contracts) *before* any simulation there, and to run a many-region analysis in which the divergence between orders varies systematically.

This is the single most important design decision in the book: **choose the comparison that represents best current practice, not the one that makes the method look best.**

### 3.10 Common errors and limits

- Comparing against a straw-man baseline (no prioritization at all, or random).
- Omitting the cost side of a trade-off that scheduling theory predicts.
- Defining "critical" after seeing which facilities benefit.
- Encoding buffers as point values without uncertainty.
- Treating a graph with OR semantics as if it modelled redundancy.
- Writing a mechanism that predicts only success.
- Setting the smallest effect of interest by statistical convention instead of practical consequence.

- Choosing the second context after seeing which kind of region favours the method, rather than fixing selection criteria in advance.
- Treating an earliest-time-to-impact rule as optimal when scheduling theory shows the weighted problem is hard and the rule ignores weights and fan-out.
- Recording only each facility's direct power buffer, so that indirect paths such as the hospital's dependence on water are missed.
- Letting the partner who supplies the data also choose the thresholds without recording who set them and when.

### Exercises — chapter 3

**EX015 — Contribution typing.** *Objective:* match claims to evidence. *Inputs:* four synthetic thesis claims: (a) "We release GridWater-Sim 2.0"; (b) "Our buffer-duration survey instrument is reliable"; (c) "Utilities rarely use buffer timing when ordering restoration"; (d) "Time-to-impact ordering reduces critical-service loss." *Constraints:* use §3.1. *Steps:* (1) assign each claim a contribution type; (2) state the minimum evidence that type requires; (3) state which claim depends on another; (4) say which claim the Cascade Study must not make from (a) alone. *Expected evidence:* table. *Rubric:* 3 = correct types and evidence, (d) dependent on (a) only as instrument, (c) needs sampled empirical study; 2 = one error; 1 = generic evidence; 0 = none.

**EX016 — Scheduling theory check.** *Objective:* apply Smith's rule. *Inputs:* Riverbend customers F1 9000, F2 1200, F3 2500, F4 6000; restoration durations 4, 3, 5 and 4 hours respectively; one crew. *Constraints:* show calculations. *Steps:* (1) compute w/p for each feeder; (2) give Smith's order; (3) compute customer-hours (thousands) for Smith's order and for the order F2, F3, F1, F4; (4) state the percentage increase. *Expected evidence:* calculations. *Rubric:* 3 = order F1, F4, F3, F2 (ratios 2250, 1500, 500, 400), totals 135.7 and 227.6 thousand customer-hours, an increase of 67.7%; 2 = arithmetic slip; 1 = wrong rule; 0 = none.

**EX017 — Time-to-impact extension.** *Objective:* extend Lab 3. *Inputs:* Lab 3. *Constraints:* offline. *Steps:* (1) add a fuel-delivery dependency: the hospital's generator buffer becomes 60 h if TEL is available for ordering fuel, modelled by replacing the F2 → HOSP buffer with 60 and adding TEL → HOSP with buffer 30; (2) run and record HOSP's failure time; (3) explain why the result did not change; (4) state what the OR-semantics graph cannot express about this fuel arrangement. *Expected evidence:* code, output, explanation. *Rubric:* 3 = HOSP still 13 h via water; explains that a buffer *extension conditional on another service* is an AND/conditional relation the OR graph cannot express; 2 = output right, explanation partial; 1 = wrong output; 0 = not run.

**EX018 — Hypothesis set.** *Objective:* operationalize hypotheses. *Inputs:* the mechanism in §3.4, applied to a different domain of your choice (e.g., restoring telecom sites after a cyber incident at a carrier, with hospitals and dispatch as dependants). *Constraints:* one benefit hypothesis, one contribution-over-best-practice hypothesis, one mechanism-pattern hypothesis and one non-inferiority hypothesis; justified thresholds. *Steps:* (1) write each hypothesis with population, intervention, comparator, outcome and direction; (2) define each outcome operationally; (3) justify each threshold by a practical consequence. *Expected evidence:* hypothesis block. *Rubric:* 3 = complete and operational, best-practice comparator named, thresholds justified by consequences and owners; 2 = one element vague; 1 = thresholds arbitrary; 0 = none.

**EX019 — Rival-explanation table.** *Objective:* design against alternatives. *Inputs:* your EX018 hypotheses. *Constraints:* at least six rivals. *Steps:* (1) list at least six rival explanations for a positive result; (2) for each, state the prediction that would support it; (3) name the design feature that tests it. *Expected evidence:* table. *Rubric:* 3 = six or more plausible rivals including baseline adequacy, weights, circularity and adoption, each with a concrete design feature; 2 = four or five; 1 = generic; 0 = none.

**EX020 — Failure conditions and second-context criteria.** *Objective:* make the contribution falsifiable and avoid cherry-picking the validation context. *Inputs:* your proposal. *Constraints:* at least five failure conditions with consequences; selection criteria for a second context written *before* it is modelled. *Steps:* (1) write failure conditions mapped to claim changes; (2) write three to five context-selection criteria derived from the mechanism; (3) explain how a reviewer could verify the criteria were fixed in advance. *Expected evidence:* two lists and a paragraph. *Rubric:* 3 = each condition changes a specific claim, criteria derived from the mechanism (order divergence, crew count, buffer range), timestamped preregistration named; 2 = criteria not mechanism-derived; 1 = vague; 0 = none.

### Chapter synthesis

A doctoral contribution must say what kind it is and must beat the strongest current practice, not a straw man. Restoration ordering is a scheduling problem: Smith's rule makes "most customers first" optimal for customer-hours, while buffer-limited critical services create a weighted-tardiness objective for which simple rules are heuristics. That theory predicts the trade-off, provides an oracle bound and exposes the proposed rule's weakness. Dependency graphs with buffers reveal indirect paths that dominate timing, but their OR semantics, fixed buffers and missing human and recovery-direction dependencies must be named. The mechanism predicts a pattern — benefit only where timing and customer counts disagree, none when buffers are long, a cost in customer-hours and fragility to map error — and the hypotheses, baselines, rivals and failure conditions are written so that each part of that pattern could be shown false.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 08

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Baseline replication and pilot

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Distinguish reproduction, replication and robustness checks, and choose which one a baseline needs.
2. Reproduce a published model calculation, predeclare a tolerance, diagnose a discrepancy and write a reproduction log.
3. Verify a simulator with invariants, unit tests and an independent implementation before trusting any comparison it produces.
4. Recognize evaluation-protocol artifacts — point adjustment, temporal leakage, testbed-specific features — that inflate detection baselines.
5. Elicit and document model parameters from experts with explicit uncertainty.
6. Design a bounded pilot whose purpose is feasibility, with go/no-go criteria, and explain why a pilot must not be used to estimate the effect size.

Chapter 3 fixed the hypotheses, baselines and failure conditions. Before the main study can compare DEP with SILO, CRITFLAG and ORACLE, every number those comparisons depend on must be shown to mean what it claims.

### 4.1 Reproduction, replication, robustness

The [National Academies (2019)](https://doi.org/10.17226/25303) distinguish **reproducibility** — obtaining consistent results using the same input data, computational steps, methods and conditions of analysis — from **replicability** — obtaining consistent results across studies aimed at the same question, each with its own data. A third activity, often called a **robustness** check, varies analytic choices on the same data. Infrastructure theses need all three:

| Activity | Cascade Study example | What it guards against |
|---|---|---|
| Reproduction | Re-run a published inoperability calculation with the published matrix | Misreading conventions; coding errors in the baseline |
| Replication | Build Port Halvard independently and test whether the Riverbend result holds | Context-specific or model-specific findings |
| Robustness | Vary weights, buffers, time step, horizon | Results that depend on one arbitrary choice |

### 4.2 Reproducing a model calculation: the inoperability input–output model

#### 4.2.1 The model

Haimes and Jiang's inoperability input–output model ([2001](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1))) adapts Leontief's input–output economics to infrastructure. Each sector *i* has an inoperability *q_i* between 0 (fully operable) and 1 (fully inoperable). The equilibrium after an initial perturbation *c\** is *q* = *A\*q* + *c\**, hence *q* = (*I* − *A\**)⁻¹ *c\**. The element *A\*_ij* is the inoperability contributed to sector *i* per unit inoperability of sector *j*. The convention matters: the row is the *receiving* sector, the column the *supplying* sector. Papers and software differ in notation, and some derive *A\** from economic input–output tables through normalization steps that are easy to get subtly wrong.

#### 4.2.2 Reproduction lab

A synthetic "published" paper reports that, after a perturbation making power 50% inoperable, water reaches an equilibrium inoperability of 0.236 in a three-sector model. Predeclare a tolerance of ± 0.005 (rounding in the publication), then reproduce:

```python
# Lab 4a - reproducing an inoperability input-output (IIM) result (offline, standard library only)
# q = (I - A*)^-1 c*. Convention: A*[i][j] = inoperability contributed to sector i per unit inoperability of sector j.
def solve(a, c):
    n = len(c)
    m = [[(1.0 if i == j else 0.0) - a[i][j] for j in range(n)] + [c[i]] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[piv] = m[piv], m[col]
        for r in range(n):
            if r != col:
                f = m[r][col] / m[col][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[col])]
    return [m[i][n] / m[i][i] for i in range(n)]
sectors = ["power", "water", "telecom"]
A = [[0.00, 0.05, 0.10],   # power depends a little on water (cooling) and telecom (SCADA comms)
     [0.40, 0.00, 0.15],   # water depends strongly on power
     [0.30, 0.02, 0.00]]   # telecom depends on power
c = [0.50, 0.00, 0.00]    # initial perturbation: power 50% inoperable
q = solve(A, c)
print("convention A* (row = receiving sector):", [round(x, 3) for x in q])
At = [list(r) for r in zip(*A)]
qt = solve(At, c)
print("transposed by mistake:               ", [round(x, 3) for x in qt])
```

Expected output:

```text
convention A* (row = receiving sector): [0.528, 0.236, 0.163]
transposed by mistake:                [0.528, 0.028, 0.057]
```

With the correct convention the reproduction matches (water 0.236). With the matrix transposed — an error that produces no warning, no crash and a plausible-looking vector — water's inoperability falls by almost an order of magnitude, and the *ranking* of sectors changes: telecom now appears more affected than water. Power's own value happens to agree in both cases, which is exactly what makes the error dangerous: a replicator who checks only the perturbed sector would declare success.

#### 4.2.3 The reproduction log

A reproduction log records: the target value and its source (page, table); the tolerance, fixed *before* running; software environment (language version, operating system); inputs and their provenance; the exact output; discrepancies and their diagnosis; and the decision (reproduced, reproduced after correction, not reproduced). When the original authors' convention is ambiguous, write to them; record the correspondence. A non-reproduction is a result, not an embarrassment, and belongs in the thesis.

#### 4.2.4 What a reproduced IIM can and cannot support

Reproducing the calculation shows only that the arithmetic is understood. The IIM remains linear and equilibrium-based: it does not model buffers, timing or restoration order, and its coefficients are usually derived from economic flows rather than engineering dependencies. In the Cascade Study it serves as a **sector-level cross-check** — do the sectors the IIM ranks as most affected match the services the buffer model shows failing? — not as a competitor to the restoration model.

### 4.3 The GridWater-Sim discrepancy (synthetic)

The synthetic benchmark GridWater-Sim reports, for a Riverbend-like configuration, a mean weighted critical-service loss under customer-first restoration that the candidate's re-implementation could not match within the predeclared tolerance. Diagnosis followed the order that most often finds the cause:

1. **Inputs.** Were the same parameter distributions used? The benchmark documentation gave triangular distributions as (low, mode, high); Python's `random.triangular` takes (low, high, mode). Swapping mode and high silently shifts the mean.
2. **Semantics.** Does "restored" mean re-energized or service resumed? GridWater-Sim applied a one-hour restart lag only to water; the re-implementation applied it to every service.
3. **Numerics.** The benchmark advanced time in fixed steps; the re-implementation computed exact outage intervals. Fixed steps introduce discretization error that depends on the step and on where buffer expiries fall within a step.
4. **Randomness.** Were seeds and draw order identical? Draw order matters: drawing durations before buffers in one implementation and after in another produces different scenario sets from the same seed.

After aligning (1) and (2), the remaining difference was within tolerance and shrank with smaller time steps, confirming (3). The thesis records the benchmark as *reproduced after correcting a parameter-order ambiguity*, reports the original and corrected values, and adopts the exact-interval implementation with the time-step version kept as an independent check.

### 4.4 Verifying a simulator

Verification asks whether the model is implemented correctly; validation asks whether it represents the real system adequately for its purpose ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)). Verification comes first, because validating a buggy implementation is meaningless.

**Invariants** that any correct restoration simulator must satisfy:

- If every buffer exceeds the horizon, weighted critical-service loss is zero under every ordering.
- Two policies that produce the same order produce identical results on identical draws.
- The oracle's loss is less than or equal to every policy's loss on every draw.
- Increasing a buffer, holding everything else fixed, never increases loss.
- Customer-hours under Smith's rule are less than or equal to those under any other ordering when restoration durations are equal.
- Loss and customer-hours are non-negative and bounded by weight × horizon and customers × horizon.

**Unit tests** check the smallest components: interval arithmetic for a single service; the effect of a dependency with an on-site buffer; crew assignment with two crews. **Cross-implementation tests** compare two independently written implementations on fixed draws. **Extreme-condition tests** use zero buffers, zero durations and one feeder. Keep the tests in the archive (Chapter 7); a reviewer who can run them trusts the comparisons more than one who must take them on faith.

### 4.5 Replicating a detection baseline: evaluation artifacts

Even though the Cascade Study does not propose a detector, its time-to-impact analysis depends on when a disruption is recognized, and the candidate must be able to judge detection baselines reported for infrastructure. The common inflation mechanisms are evaluation choices, not model properties.

#### 4.5.1 Point adjustment

[Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) showed that point adjustment (PA) — counting a whole anomalous segment as detected when any point in it is flagged — can make random scores look excellent. The following lab reproduces the effect on synthetic labels:

```python
# Lab 4b - how point adjustment (PA) inflates detection scores (offline, standard library only)
import random
random.seed(42)
N = 2000
labels = [0] * N
for start, length in [(300, 60), (900, 120), (1500, 80)]:
    for t in range(start, start + length):
        labels[t] = 1
scores = [random.random() for _ in range(N)]          # a detector that knows nothing
thr = sorted(scores)[int(0.97 * N)]                    # alarm on the top 3% of scores
pred = [1 if s > thr else 0 for s in scores]
def f1(p, y):
    tp = sum(1 for a, b in zip(p, y) if a and b)
    fp = sum(1 for a, b in zip(p, y) if a and not b)
    fn = sum(1 for a, b in zip(p, y) if b and not a)
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    return round(2 * prec * rec / (prec + rec), 3) if prec + rec else 0.0
def segments(y):
    segs, t = [], 0
    while t < len(y):
        if y[t]:
            s = t
            while t < len(y) and y[t]:
                t += 1
            segs.append((s, t))
        else:
            t += 1
    return segs
def adjust(p, y, k=0.0):
    q = list(p)
    for s, e in segments(y):
        hit = sum(p[s:e]) / (e - s)
        if hit > k:
            for t in range(s, e):
                q[t] = 1
    return q
print("point-wise F1           :", f1(pred, labels))
print("F1 after PA             :", f1(adjust(pred, labels), labels))
print("F1 after PA%K (K = 0.20):", f1(adjust(pred, labels, 0.20), labels))
print("segments hit by >=1 alarm:", sum(1 for s, e in segments(labels) if any(pred[s:e])), "of", len(segments(labels)))
```

Expected output:

```text
point-wise F1           : 0.05
F1 after PA             : 0.911
F1 after PA%K (K = 0.20): 0.05
segments hit by >=1 alarm: 3 of 3
```

A detector with no information scores 0.911 after PA because each long segment contains, by chance, at least one of the 3% random alarms. PA%K with K = 20% removes the inflation here. For CI research the lesson goes further: neither metric says *when* the first true alarm occurred relative to the segment's start, which is what matters for buffers. A consequence-relevant metric is **detection latency relative to time-to-impact** — the fraction of incidents detected before the earliest dependent service's buffer is exhausted.

#### 4.5.2 Other artifacts

- **Temporal leakage.** Random train/test splits of time series let a model learn from the future. Use time-ordered splits that mimic deployment.
- **Testbed-specific features.** A detector may learn signatures of the testbed's attack-injection tooling or its specific sensors rather than of attacks.
- **Attack-set coverage.** A dataset's attacks were chosen by its builders; performance on them says little about other attack classes ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)).
- **Base rates.** A false-positive rate that looks small on a balanced dataset can swamp operators at realistic base rates ([Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 4.6 Eliciting parameters

The model's buffers, restoration durations and weights come from people. Structured expert elicitation — preparing experts, asking for quantiles rather than single values, feeding back implied distributions and recording rationales — reduces anchoring and overconfidence ([O'Hagan et al., 2006](https://doi.org/10.1002/0470033312)). For the Cascade Study (synthetic):

| Parameter | Elicited from | Form | Documentation |
|---|---|---|---|
| Feeder restoration duration | Three REC dispatchers | Minimum, most likely, maximum for manual switching without SCADA | Rationale per value; disagreement recorded |
| Telecom buffer | Carrier's facilities engineer | Battery autonomy under measured load, generator fuel hours | Load assumption stated |
| Water buffer | RWA operations manager | Generator autonomy plus storage drawdown to minimum pressure | Demand assumption (season) stated |
| Hospital buffer | Facilities director | Fuel on hand at typical load; on-site water hours | Code requirements and actual inventory distinguished |
| Weights | Emergency-management panel | Pairwise comparisons converted to weights | Elicited before any simulation; signed and dated |

Triangular distributions are a pragmatic choice for three-point elicitations; they are not physically derived. Chapter 6 tests whether conclusions depend on the distribution family.

### 4.7 The pilot

#### 4.7.1 What a pilot is for

A pilot tests **feasibility**: whether procedures, materials, timing, data flows and instruments work. It is not a small main study. Effect sizes estimated from pilots are too imprecise to plan sample sizes or to support claims ([Leon, Davis and Kraemer, 2011](https://doi.org/10.1016/j.jpsychires.2010.10.008)). The Cascade Study pilot had two strands:

1. **Simulation pilot.** Run all four policies on 50 draws to check that the code, logging and invariants work, that runtime allows the planned number of draws, and that censoring at 72 hours is rare. The pilot *results* (differences between policies) are logged as exploratory and not interpreted.
2. **Tabletop pilot.** Three operators (synthetic participants P01–P03, not eligible for the main study) worked through a 40-minute scenario with and without a time-to-impact display. Questions: Do they understand the display? Does the scenario reveal the outcome too early? How long does each decision take? Does the consent and debrief process work?

#### 4.7.2 Go/no-go criteria (predeclared)

| Criterion | Threshold | Pilot result (synthetic) | Decision |
|---|---|---|---|
| Invariant tests pass | All | All | Go |
| Censoring at 72 h | < 1% of service-draws | 0% | Go |
| Runtime for 500 draws incl. oracle | < 1 hour | Minutes | Go |
| Participants correctly read the display | ≥ 2 of 3 | 3 of 3 after one wording change | Go with revision |
| Scenario reveals outcome prematurely | No | Yes — an inject mentioned "hospital diversion" | Revise inject; re-pilot one participant |
| Session length | ≤ 60 min | 55 min | Go |

Every revision is logged in the deviation log with the date and confirmation that no main-study data existed.

### 4.8 Worked example: the pilot that changed the scenario

In the tabletop pilot, P02 asked why the hospital's generator buffer was shown as 26 hours when "everyone knows the water goes first". The candidate had displayed only direct power buffers. The display was revised to show **effective time-to-impact** (the minimum over all paths, as in Lab 3) alongside direct buffers, with the path shown. This changed the instrument — a legitimate pilot outcome — and raised a methodological point for the main study: the comparison between "with display" and "without display" now tested the effective-time-to-impact display, not merely any criticality information. The hypotheses for the tabletop were refined accordingly, *before* the main study, and the change was preregistered as an amendment.

### 4.9 Common errors and limits

- Declaring a reproduction successful after checking a single output.
- Setting tolerances after seeing the discrepancy.
- Treating the benchmark's code as the specification when it disagrees with its paper, or vice versa, without recording which was followed.
- Validating a simulator before verifying it.
- Reporting point-adjusted F1 for infrastructure detection without latency relative to consequence.
- Asking experts for single numbers and treating them as certain.
- Using pilot effect sizes to plan or to claim.

- Checking only the perturbed sector in a reproduction, as with power in the transposed inoperability matrix, which agrees under both conventions.
- Assuming a library's parameter order matches the paper's notation, as with the triangular distribution in the GridWater-Sim case.
- Interpreting differences between policies in a pilot, when the pilot's purpose is feasibility and its results are logged as exploratory.
- Changing a tabletop instrument after the pilot without recording the change in the deviation log.

### Exercises — chapter 4

**EX021 — Reproduction log.** *Objective:* document a reproduction attempt. *Inputs:* Lab 4a. *Constraints:* run offline; tolerance ± 0.005 fixed before running. *Steps:* (1) record the target (water 0.236); (2) run the transposed matrix first and record the discrepancy; (3) diagnose using the matrix convention; (4) run the correct convention; (5) write the log entry with environment details. *Expected evidence:* reproduction log. *Rubric:* 3 = exact outputs, convention diagnosis, environment recorded, notes that power agrees in both runs; 2 = one element missing; 1 = no diagnosis; 0 = not run.

**EX022 — IIM perturbation analysis.** *Objective:* use a reproduced model for a bounded claim. *Inputs:* Lab 4a with the correct convention. *Constraints:* offline. *Steps:* (1) compute *q* for perturbations power 0.5 and telecom 0.5 separately; (2) compute *q* for both together; (3) check whether the joint result equals the sum of the separate results and explain why; (4) state one claim the model supports and one it cannot. *Expected evidence:* three vectors and a paragraph. *Rubric:* 3 = correct vectors, linearity (superposition) explained, claim limited to equilibrium inoperability without timing; 2 = vectors correct, explanation thin; 1 = errors; 0 = none.

**EX023 — Parameter-order trap.** *Objective:* detect a silent input error. *Inputs:* a distribution documented as (low = 4, mode = 8, high = 12). *Constraints:* use Python's `random.triangular(low, high, mode)`. *Steps:* (1) compute the theoretical mean, (low + mode + high) / 3, for the correct call `triangular(4, 12, 8)`; (2) estimate the mean of the mistaken call `triangular(4, 8, 12)` from 100,000 seeded draws and record the minimum and maximum; explain what the mistaken call actually samples; state which test would have caught it. *Expected evidence:* two means and explanation. *Rubric:* 3 = correct mean 8.0; the mistaken call treats 8 as *high* and 12 as *mode*, so CPython's formula returns 4 + 4·√(2u) for uniform *u* — values in [4, ≈ 9.66] with mean ≈ 7.77, not a triangular distribution at all; a mean check alone is weak, while checking that the sample maximum approaches 12 and plotting a histogram catches it; 2 = error identified, test weak; 1 = error missed; 0 = none.

**EX024 — Invariant tests.** *Objective:* write verification tests. *Inputs:* the invariants in §4.4 and the simulator you will meet in Chapter 5 (Lab 5), or your own. *Constraints:* at least four invariants as executable assertions. *Steps:* (1) choose at least four invariants from §4.4; (2) write each as an executable assertion; (3) run the assertions on fixed draws; (4) deliberately introduce a bug, such as removing the restart lag for one service, and show which test fails. *Expected evidence:* test code and output before and after the bug. *Rubric:* 3 = four or more meaningful invariants, the bug caught, explanation of why; 2 = tests run but the bug is not caught; 1 = trivial tests; 0 = none.

**EX025 — Latency-relative detection metric.** *Objective:* define a consequence-relevant detection metric. *Inputs:* Lab 4b and Lab 3's time-to-impact values (the earliest critical impact at 2 h for water SCADA, 8 h for telecom). *Constraints:* define the metric formally. *Steps:* (1) define "detected before impact" for a segment with known start and a known time-to-impact; (2) compute it for the random detector, treating each time step as 6 minutes and taking time-to-impact as 2 h for every segment; (3) compare with the F1 values. *Expected evidence:* definition, computed fraction, paragraph. *Rubric:* 3 = sound definition and correct computation from the first alarm index in each segment, with the contrast to PA explained; 2 = definition fine, computation error; 1 = vague; 0 = none.

**EX026 — Pilot plan.** *Objective:* design a feasibility pilot. *Inputs:* your own study from earlier exercises. *Constraints:* at least six go/no-go criteria with thresholds; explicit statement of what will not be estimated. *Steps:* (1) list the pilot's feasibility questions; (2) set predeclared thresholds; (3) define what happens on "no-go" for each; (4) define who may participate and why pilot participants are excluded from the main study. *Expected evidence:* pilot plan. *Rubric:* 3 = criteria measurable, feasibility-only, exclusion justified, revision process logged; 2 = one criterion vague; 1 = pilot used to estimate effect; 0 = none.

### Chapter synthesis

Before comparing methods, make sure the numbers mean what they claim. Reproduce baselines with a tolerance fixed in advance, check more than one output, and record conventions — a transposed matrix produced a plausible, wrong answer that agreed on the one value a hurried replicator would check. Diagnose discrepancies through inputs, semantics, numerics and randomness. Verify simulators with invariants, unit tests and an independent implementation before validating them. Treat detection baselines with suspicion when they rely on point adjustment, random splits or a single testbed, and prefer latency relative to time-to-impact for infrastructure. Elicit parameters with uncertainty and provenance. Use the pilot to fix procedures and instruments, never to estimate effects.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 08

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Main study and independent validation

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Design a paired simulation experiment with common random numbers, a justified number of draws and an oracle bound.
2. Distinguish Monte Carlo uncertainty from parameter uncertainty and structural uncertainty, and say which one a reported interval describes.
3. Interpret a mixed pattern of supported and unsupported hypotheses without rescuing the favorable ones.
4. Design and analyse a blinded operator tabletop study whose outcome is the *consequence* of the choices made, not stated preference.
5. Validate a model using face, historical, extreme-condition and operational validity evidence, and state what each establishes.
6. Run an independent validation in a second context selected on predeclared criteria and reason about transportability.

Chapter 4 verified the simulator, reproduced the baselines and piloted the procedures. This chapter runs the confirmatory study exactly as preregistered and then tests whether its result travels.

### 5.1 Designing the simulation experiment

#### 5.1.1 Paired comparisons and common random numbers

Each simulation draw samples one scenario: restoration durations for every feeder and buffers for every service. Every policy is evaluated on *the same* draw. This **common random numbers** design removes shared between-scenario variance from the comparison: the quantity of interest is the per-draw difference between two policies, whose variance is Var(A) + Var(B) − 2 Cov(A, B). Pairing helps exactly as much as the two policies' losses are positively correlated across draws. When two policies trade off — one protects water on a draw where the other protects telecom — the correlation is weak and pairing helps little; EX028 shows this happening in Riverbend. Analyse paired differences anyway, because they are the correct estimand, but do not assume that pairing guarantees precision.

#### 5.1.2 How many draws?

The Monte Carlo standard error of a mean difference is *s_d* / √*n*, where *s_d* is the standard deviation of the per-draw differences. In the pilot (Chapter 4) the standard deviation of DEP − CRITFLAG differences in Riverbend was about 7 weighted service-hours, so 500 draws give a 95% half-width of about 1.96 × 7 / √500 ≈ 0.6. The smallest effect of interest for H2 is 10% of CRITFLAG's loss; because CRITFLAG's loss in Riverbend is small (about 4), that threshold is about 0.4 — smaller than the half-width. The preregistration therefore fixed a three-way **decision rule**: H2 is *supported* if the interval lies wholly below −10% of CRITFLAG's mean loss, *rejected* if it lies wholly above that threshold (a reduction of at least 10% is ruled out), and *inconclusive* otherwise, in which case the planned remedy was 2,000 additional draws without the oracle. Record the calculation and the rule; do not increase *n* after seeing a "nearly significant" result outside the rule you wrote.

#### 5.1.3 What a Monte Carlo interval means

A bootstrap or normal interval over simulation draws describes **Monte Carlo uncertainty** — how much the estimate would move with more draws *from this model with these parameter distributions*. It says nothing about **parameter uncertainty** (whether the elicited distributions are right) or **structural uncertainty** (whether the model's form is right). With enough draws, any difference becomes "statistically significant" inside a model. Report Monte Carlo intervals for completeness, but base claims on effect sizes relative to the smallest effect of interest, and address parameter and structural uncertainty with sensitivity analyses and validation (§5.4 and Chapter 6).

### 5.2 The confirmatory simulation study

#### 5.2.1 The simulator

The event-based simulator below implements the preregistered design. A service is unavailable while its feeder is de-energized beyond its buffer, or while a service it depends on is unavailable beyond its on-site buffer; a one-hour restart lag follows restoration. Crews take the next feeder in the policy's order as soon as they are free. Customer-hours are computed per feeder. ORACLE enumerates every ordering for each draw. Save the code as `lab5_mc.py`; Chapter 6 imports it.

```python
# Lab 5 - paired Monte Carlo comparison of restoration orderings (offline, standard library only)
# Event-based: a service is unavailable while its feeder is down beyond its buffer, or while a
# service it depends on is unavailable beyond its on-site buffer; restart lag applies after restoration.
import itertools, random, statistics

RIVERBEND = {
    "customers": {"F1": 9000, "F2": 1200, "F3": 2500, "F4": 6000},
    "crews": 1, "dur": (2, 6, 4),          # triangular(low, high, mode) hours per feeder
    "services": {  # name: (feeder, buffer triangular, weight, (depends_on, on-site hours) or None)
        "WATER": ("F3", (4, 14, 8), 4.0, None),
        "TEL":   ("F2", (4, 12, 8), 3.0, None),
        "HOSP":  ("F2", (8, 48, 24), 5.0, ("WATER", 4.0)),
    },
}
PORT_HALVARD = {
    "customers": {"H1": 7000, "H2": 3000, "H3": 1500, "H4": 4000, "H5": 800, "H6": 5000},
    "crews": 2, "dur": (1.5, 5, 3),
    "services": {
        "WATER2":   ("H4", (10, 30, 20), 4.0, None),
        "HOSP2":    ("H2", (48, 96, 72), 5.0, ("WATER2", 6.0)),
        "TEL2":     ("H3", (2, 6, 4), 3.0, None),
        "DISPATCH": ("H5", (1, 3, 2), 4.0, None),
    },
}
H, LAG = 72.0, 1.0

def draw(region, rng, buffer_scale=1.0):
    dur = {f: rng.triangular(*region["dur"]) for f in sorted(region["customers"])}
    buf = {s: rng.triangular(*v[1]) * buffer_scale for s, v in sorted(region["services"].items())}
    return dur, buf

def restore_times(order, dur, crews):
    free, done = [0.0] * crews, {}
    for f in order:
        i = min(range(crews), key=lambda k: free[k])
        free[i] += dur[f]
        done[f] = free[i]
    return done

def outage(region, done, buf):
    """Return {service: (start, end)} of unavailability, clipped to [0, H]."""
    out = {}
    def solve(s):
        if s in out:
            return out[s]
        feeder, _, _, dep = region["services"][s]
        ivs = []
        if buf[s] < done[feeder]:
            ivs.append((buf[s], done[feeder] + LAG))
        if dep:
            d = solve(dep[0])
            if d and d[0] + dep[1] < d[1]:
                ivs.append((d[0] + dep[1], d[1]))
        out[s] = (min(a for a, _ in ivs), max(b for _, b in ivs)) if ivs else None
        return out[s]
    for s in region["services"]:
        solve(s)
    return {s: (max(0.0, iv[0]), min(H, iv[1])) for s, iv in out.items() if iv}

def evaluate(region, order, dur, buf):
    done = restore_times(order, dur, region["crews"])
    loss = sum(region["services"][s][2] * (e - b) for s, (b, e) in outage(region, done, buf).items() if e > b)
    cust_h = sum(c * min(H, done[f]) for f, c in region["customers"].items()) / 1000.0
    return loss, cust_h

def silo(region):
    return sorted(region["customers"], key=lambda f: -region["customers"][f])

def critflag(region, believed_feeder=None):
    feeder_of = {s: v[0] for s, v in region["services"].items()}
    feeder_of.update(believed_feeder or {})   # the critical-customer list may also be out of date
    crit = set(feeder_of.values())
    return sorted(region["customers"], key=lambda f: (f not in crit, -region["customers"][f]))

def dep(region, believed_feeder=None):
    svc = dict(region["services"])
    if believed_feeder:                       # planner's (possibly wrong) dependency map
        for s, f in believed_feeder.items():
            svc[s] = (f,) + svc[s][1:]
    mean = {s: sum(v[1]) / 3 for s, v in svc.items()}
    tti = {}
    def t(s):
        if s not in tti:
            dep_ = svc[s][3]
            tti[s] = min(mean[s], t(dep_[0]) + dep_[1]) if dep_ else mean[s]
        return tti[s]
    key = {f: min([t(s) for s, v in svc.items() if v[0] == f], default=float("inf")) for f in region["customers"]}
    return sorted(region["customers"], key=lambda f: (key[f], -region["customers"][f]))

def experiment(region, n=500, seed=7, buffer_scale=1.0, believed_feeder=None, oracle=True):
    rng = random.Random(seed)
    policies = {"SILO": silo(region), "CRITFLAG": critflag(region, believed_feeder), "DEP": dep(region, believed_feeder)}
    res = {k: [] for k in list(policies) + (["ORACLE"] if oracle else [])}
    cust = {k: [] for k in policies}
    perms = list(itertools.permutations(region["customers"]))
    for _ in range(n):
        dur, buf = draw(region, rng, buffer_scale)
        for k, order in policies.items():
            l, c = evaluate(region, order, dur, buf)
            res[k].append(l)
            cust[k].append(c)
        if oracle:
            res["ORACLE"].append(min(evaluate(region, list(p), dur, buf)[0] for p in perms))
    return policies, res, cust

def boot_ci(x, seed=11, b=1000):
    rng = random.Random(seed)
    means = sorted(statistics.fmean(rng.choices(x, k=len(x))) for _ in range(b))
    return round(means[int(0.025 * b)], 2), round(means[int(0.975 * b)], 2)

if __name__ == "__main__":
    for name, region in (("Riverbend", RIVERBEND), ("Port Halvard", PORT_HALVARD)):
        policies, res, cust = experiment(region)
        print(f"== {name}: orders {policies}")
        for k, v in res.items():
            extra = f"  customer-hours(k) {statistics.fmean(cust[k]):7.1f}" if k in cust else ""
            print(f"  {k:8} weighted critical loss {statistics.fmean(v):6.2f}{extra}")
        d = [a - b for a, b in zip(res["DEP"], res["CRITFLAG"])]
        print("  DEP - CRITFLAG loss: mean", round(statistics.fmean(d), 2), "95% CI", boot_ci(d))
        r = statistics.fmean(cust["DEP"]) / statistics.fmean(cust["SILO"]) - 1
        r2 = statistics.fmean(cust["DEP"]) / statistics.fmean(cust["CRITFLAG"]) - 1
        print("  DEP customer-hours vs SILO:", f"{r:+.1%}", "| vs CRITFLAG:", f"{r2:+.1%}")
```

Expected output:

```text
== Riverbend: orders {'SILO': ['F1', 'F4', 'F3', 'F2'], 'CRITFLAG': ['F3', 'F2', 'F1', 'F4'], 'DEP': ['F2', 'F3', 'F1', 'F4']}
  SILO     weighted critical loss  52.75  customer-hours(k)   133.0
  CRITFLAG weighted critical loss   3.97  customer-hours(k)   222.5
  DEP      weighted critical loss   4.32  customer-hours(k)   227.6
  ORACLE   weighted critical loss   1.79
  DEP - CRITFLAG loss: mean 0.35 95% CI (-0.23, 0.97)
  DEP customer-hours vs SILO: +71.2% | vs CRITFLAG: +2.3%
== Port Halvard: orders {'SILO': ['H1', 'H6', 'H4', 'H2', 'H3', 'H5'], 'CRITFLAG': ['H4', 'H2', 'H3', 'H5', 'H1', 'H6'], 'DEP': ['H5', 'H3', 'H4', 'H2', 'H1', 'H6']}
  SILO     weighted critical loss  53.93  customer-hours(k)   103.2
  CRITFLAG weighted critical loss  31.63  customer-hours(k)   148.5
  DEP      weighted critical loss   9.61  customer-hours(k)   163.2
  ORACLE   weighted critical loss   9.61
  DEP - CRITFLAG loss: mean -22.01 95% CI (-22.4, -21.59)
  DEP customer-hours vs SILO: +58.2% | vs CRITFLAG: +9.9%
```

#### 5.2.2 Reading the results against the hypotheses

| Hypothesis | Riverbend (main) | Port Halvard (independent validation) | Verdict |
|---|---|---|---|
| H1: DEP reduces loss ≥ 20% vs SILO | 52.75 → 4.32 (−92%) | 53.93 → 9.61 (−82%) | Supported in both |
| H2: DEP reduces loss ≥ 10% vs CRITFLAG | +0.35 (95% MC interval −0.23 to 0.97), wholly above the −0.40 threshold: a 10% reduction is ruled out | −22.01 of 31.63 (−70%) | **Not supported** in Riverbend; supported in Port Halvard |
| H3: gain grows with order divergence | Orders differ in 2 positions (F2/F3 swapped) yet no gain | Orders differ in all 4 critical positions; large gain | Partly; Riverbend is an anomaly to explain (§5.2.3) |
| H4a: customer-hours ≤ +15% vs SILO | +71.2% | +58.2% | **Fails** in both |
| H4b: customer-hours ≤ +15% vs CRITFLAG | +2.3% | +9.9% | Holds in both |
| ORACLE gap | DEP 4.32 vs ORACLE 1.79 | DEP 9.61 = ORACLE 9.61 | DEP far from optimal in Riverbend; optimal in Port Halvard |

The honest summary is mixed. Criticality-aware ordering of *any* kind protects critical services dramatically compared with customer-first ordering, at a large cost in customer-hours that scheduling theory predicted (Chapter 3). Whether *timing* adds value over a critical-customer list depends on the region: none in Riverbend, a great deal in Port Halvard. The preregistered failure condition "H2 fails in one region and holds in the other" applies: narrow the claim to the conditions that distinguish the regions and test the mechanism.

#### 5.2.3 Explaining the Riverbend anomaly without rescuing the hypothesis

In Riverbend, DEP restores F2 (telecom and hospital) before F3 (water), because telecom's expected time-to-impact (8 h) is slightly earlier than water's (8.7 h). CRITFLAG restores F3 first because it has more customers. But F3 protects *two* weighted services — water directly and the hospital through its water dependency — while restoring F2 first protects telecom and only the hospital's power path, which has a long buffer. An earliest-time-to-impact rule ignores **weights and fan-out**; Chapter 3 named this as the heuristic's known weakness. ORACLE's much lower loss confirms that neither rule is close to optimal in Riverbend.

This explanation is post hoc. It is legitimate to report it as a *hypothesis generated by the confirmatory study*, to be tested in new data (Chapter 6 tests it across many synthetic regions); it is not legitimate to re-run the main study with a revised rule and report that as confirmatory.

### 5.3 The operator tabletop study

#### 5.3.1 Why people, not only models

A restoration rule that operators will not follow has no consequence. The tabletop study asks whether, given the effective time-to-impact display piloted in Chapter 4, experienced operators choose orderings that the model rates as lower-consequence, and why or why not.

#### 5.3.2 Design (synthetic)

- **Participants.** Twelve operators and emergency managers (P01–P12) from three synthetic utilities, recruited through partners with individual consent, none from the pilot. Participation was voluntary and unpaid beyond expenses; managers did not learn who took part.
- **Within-subject crossover.** Each participant ordered restoration in two isomorphic scenarios — Port Halvard-like topology with renamed feeders and shuffled positions — once with a conventional display (customer counts and critical-customer flags) and once with the effective time-to-impact display added. Order of displays and scenario versions was counterbalanced.
- **Blinding.** Scenarios contained no outcome information; injects were checked in the pilot for premature cues. Analysts scoring the free-text rationales did not know which display condition produced them.
- **Outcome.** The *chosen ordering*, evaluated in the simulator on the same 500 draws as the main study — so the outcome is the model-estimated consequence of the participant's decision, not their stated preference. Secondary: decision time; rationale codes.
- **Analysis.** Paired comparison of whether each participant chose the DEP ordering under each display; exact McNemar test on discordant pairs; descriptive consequence differences; thematic analysis of rationales.

#### 5.3.3 Results (synthetic)

| Conventional display → time-to-impact display | Participants |
|---|---|
| Not DEP → DEP | 7 |
| Not DEP → not DEP | 5 |
| DEP → not DEP | 0 |
| DEP → DEP | 0 |

All seven discordant pairs moved toward DEP. Under the null hypothesis that a switch in either direction is equally likely, the exact two-sided probability of seven or more switches in one direction out of seven is 2 × 0.5⁷ = 0.0156. With twelve participants from three utilities, this is evidence that the display *can* change choices in a tabletop, not an estimate of how often operators would change practice. Among the five who did not adopt DEP, four kept a CRITFLAG-like order. Rationale codes (two coders, disagreements resolved and logged) included: *institutional expectation* ("the board measures us on customers restored"; 4 participants), *distrust of buffer figures* ("I've seen hospital fuel logs — they're never what's on paper"; 3) and *field logistics* ("crews are near the big feeder already"; 3). The last theme identifies a variable the model omits: travel time between feeders, which makes restoration durations order-dependent.

#### 5.3.4 What the tabletop can and cannot support

It supports: the display is comprehensible; it shifts tabletop choices toward lower modelled consequence; operators raise specific objections that the model must address. It cannot support: real-world adoption; effects under stress, fatigue and incomplete information; or effects in utilities unlike the three sampled. Tabletops are also performances — participants know they are observed — which pushes toward "correct-looking" answers.

### 5.4 Validating the model

Following [Sargent (2013)](https://doi.org/10.1057/jos.2012.20), validation is evidence that a model is adequate *for its intended purpose* — here, ranking restoration orderings by critical-service consequence — not that it is "true".

| Validation type | Cascade Study evidence (synthetic) | What it establishes | What it does not |
|---|---|---|---|
| Face validity | Twelve tabletop participants and two partner engineers reviewed model structure and outputs | Structure is recognizable to practitioners; no glaring omissions except travel time | That parameters are right |
| Historical validation | Riverbend's 2019 ice-storm outage (all-cause, synthetic record): the model, given recorded feeder restoration times, predicted water pressure loss at 9 h and hospital diversion at 13 h; records show 11 h and none (hospital trucked water at 10 h) | Timing of the water failure is in the right range; the model omits mutual aid (trucked water), a human buffer | Accuracy for cyber-induced scenarios; any generalization from one event |
| Extreme-condition tests | Zero buffers, infinite buffers, single feeder, one service | Behaviour at boundaries is sensible (Chapter 4 invariants) | Behaviour in the interior |
| Parameter variability | Buffer scaling and weight sets (Chapter 6) | Which conclusions depend on which parameters | Structural adequacy |
| Operational validity | Agreement between model ranking of orderings and operators' expert ranking on six scenarios: 5 of 6 top choices agree | Model ranks orderings much as experts do in familiar cases | Whether either is right in unfamiliar cases |

The historical validation produced an important correction: the model treats buffers as fixed, but real operators extend buffers — trucked water, fuel deliveries, load shedding at the hospital. A model without these human buffers is **conservative about consequence** and may **overstate the benefit of reordering**, because it ignores alternatives that operators would use anyway. The thesis must state this.

### 5.5 Independent validation in a second context

#### 5.5.1 Selection on predeclared criteria

Port Halvard was chosen *before* simulation, on criteria derived from the mechanism and recorded in the preregistration amendment of Chapter 3: more critical feeders (four), divergence between buffer order and customer order among critical feeders, two crews, and long hospital buffers backed by fuel contracts. A different modeller built the Port Halvard configuration from partner documentation without access to Riverbend results. These steps reduce, but do not remove, the risk of a validation context that favours the method: the criteria themselves were chosen to give the mechanism a chance to operate. That is acceptable for a test of the mechanism, *not* for an estimate of how often the method helps across real regions. Chapter 6 addresses the second question with many randomly generated regions.

#### 5.5.2 Transportability

A result transports from one context to another when the causal structure relevant to it is shared and the differences are measured. [Pearl and Bareinboim (2014)](https://doi.org/10.1214/14-STS486) formalize when experimental findings can be transported between populations. Informally, for the Cascade Study: the mechanism (buffers, sequential restoration, weighted consequence) is shared; the *moderators* that differ — number of critical feeders, order divergence, crew count, buffer lengths — must be measured in any target region before the result is applied. A utility that knows these four things about itself can estimate whether DEP is likely to beat its current list; one that does not, cannot.

### 5.6 Reporting the main study

Report, at minimum: the preregistration and all amendments with dates; the deviation log; every hypothesis with its verdict, including failures; effect sizes relative to smallest effects of interest; Monte Carlo intervals labelled as such; ORACLE gaps; tabletop design, consent, attrition and results with exact tests and qualitative themes; each validation type with what it establishes; and the two regions' configuration *at the level of detail allowed by the information-protection tiers* (Chapter 7). Follow a recognized reporting structure for simulation studies where one exists in the target venue, and for the tabletop follow the transparency expectations of human-subjects research in your field.

### 5.7 Common errors and limits

- Analysing two policies' means separately instead of paired differences.
- Increasing the number of draws until a difference is "significant".
- Presenting a Monte Carlo interval as uncertainty about the world.
- Re-running the confirmatory study with a rule revised after seeing results and calling it confirmatory.
- Choosing a validation context because the method will do well there, without saying so.
- Measuring operators' stated preferences instead of the consequences of their choices.
- Treating face validity as validation of parameters.

- Reading the Riverbend failure of H2 as a reason to revise DEP and rerun the main study under the same preregistration.
- Reporting a statistically significant tabletop shift as evidence of adoption, when twelve participants from three utilities only show that a display can change choices.
- Treating one historical event, such as the 2019 ice storm, as validation for cyber-induced scenarios.
- Omitting the ORACLE gap, which shows how far any rule is from the best ordering.

### Exercises — chapter 5

**EX027 — Run and interpret the main study.** *Objective:* reproduce and interpret Lab 5. *Inputs:* the code in §5.2.1. *Constraints:* offline; record exact output. *Steps:* (1) run the lab; (2) fill the hypothesis table in §5.2.2 from your output; (3) compute the relative change of DEP versus CRITFLAG in each region; (4) write a 150-word results paragraph that a hostile reviewer would accept. *Expected evidence:* output, table, paragraph. *Rubric:* 3 = exact output, H2 reported as failed in Riverbend and supported in Port Halvard, H4a failure reported, no rescue; 2 = correct numbers, paragraph overstates; 1 = errors; 0 = not run.

**EX028 — Paired versus unpaired.** *Objective:* see why common random numbers matter. *Inputs:* Lab 5. *Constraints:* offline. *Steps:* (1) for Riverbend, compute the standard deviation of DEP losses, of CRITFLAG losses and of the per-draw differences; (2) compute an unpaired 95% interval for the difference of means using the normal approximation; (3) compare with the paired interval; (4) explain the difference in 100 words. *Expected evidence:* three standard deviations, two intervals, explanation. *Rubric:* 3 = SDs about 6.36 (DEP), 4.57 (CRITFLAG) and 6.79 (differences); unpaired interval about −0.34 to 1.04 versus paired −0.24 to 0.95; explains that pairing helped only modestly because the policies' losses are weakly correlated — they trade off which service fails on a given draw — and that the difference SD can exceed each policy's SD while still being below √(Var A + Var B); 2 = numbers right, explanation assumes pairing always shrinks variance; 1 = error; 0 = none.

**EX029 — Uncertainty taxonomy.** *Objective:* classify uncertainty. *Inputs:* five statements: (a) "with 5,000 draws the interval would narrow"; (b) "the hospital's fuel may be lower than the facilities director said"; (c) "travel time between feeders is not modelled"; (d) "the weights reflect one panel's values"; (e) "buffers may not be triangular". *Constraints:* classify each as Monte Carlo, parameter, structural or value uncertainty and name the method that addresses it. *Steps:* (1) classify each statement; (2) justify the class in one sentence; (3) name the method that reduces or exposes that uncertainty. *Expected evidence:* table. *Rubric:* 3 = (a) Monte Carlo, (b) parameter, (c) structural, (d) value, (e) parameter or structural with justification, with appropriate methods; 2 = one error; 1 = two or more; 0 = none.

**EX030 — Tabletop design critique.** *Objective:* strengthen a human-subjects design. *Inputs:* §5.3.2. *Constraints:* propose at least five improvements within ethical and practical limits. *Steps:* (1) identify the threats — demand characteristics, small sample, three utilities, the absence of time pressure, isomorphic-scenario recognition; (2) propose a design change for each; (3) state what each change costs. *Expected evidence:* table. *Rubric:* 3 = five or more real threats with feasible changes and honest costs; 2 = three or four; 1 = generic; 0 = none.

**EX031 — Validation evidence matrix.** *Objective:* plan validation for your own model. *Inputs:* a model from your research or the Cascade Study. *Constraints:* at least four validation types; for each, the evidence, what it establishes and what it does not. *Steps:* (1) choose at least four validation types from §5.4; (2) for each, state the evidence you would collect; (3) state what that evidence establishes and what it does not; (4) identify which validation would be most damaging to your claim if it failed. *Expected evidence:* matrix and paragraph. *Rubric:* 3 = types well chosen, limits honest, most damaging test identified and planned early; 2 = limits thin; 1 = face validity only; 0 = none.

**EX032 — Transportability memo.** *Objective:* advise a third utility. *Inputs:* a synthetic utility with five feeders, three carrying critical services whose buffer order matches their customer order, one crew. *Constraints:* 300 words; use the moderators in §5.5.2. *Steps:* (1) measure the four moderators for this utility; (2) predict DEP's gain over CRITFLAG; (3) state what data you would need to change your prediction. *Expected evidence:* memo. *Rubric:* 3 = predicts no gain because the orders coincide, explains the moderators, and notes that weights or fan-out could still matter; 2 = prediction right, reasoning thin; 1 = predicts a gain; 0 = none.

### Chapter synthesis

The main study compared four orderings on paired draws with an oracle bound. Criticality-aware ordering of any kind protected critical services dramatically compared with customer-first restoration and cost far more customer-hours than the predeclared margin — a trade-off for policy, not a free gain. Timing information added nothing over a critical-customer list in Riverbend and a great deal in Port Halvard; the post hoc explanation (weights and fan-out ignored by an earliest-time rule) is a new hypothesis, not a rescue. A blinded tabletop showed that a time-to-impact display can shift operators' choices toward lower modelled consequence and surfaced omitted variables such as crew travel time. Validation established that the model is adequate for ranking orderings in familiar cases and conservative because it omits human buffers. Monte Carlo intervals described simulation noise only; parameter, structural and value uncertainty remain for Chapter 6.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 08

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Peer critique and revision

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Organize adversarial critique of one's own thesis — internal red-teaming, structured external review and adversarial collaboration — and record it.
2. Detect model–policy circularity and test it with deliberate model mismatch.
3. Map boundary conditions with sensitivity analysis and with many generated contexts, while recognizing that the generator is itself a model.
4. Distinguish a confirmatory revision from an exploratory one and label each.
5. Write negative and narrowed results so that they are useful to others.
6. Conduct a dual-use review of research findings and decide what to publish, generalize, delay or restrict.
7. Write a response to reviewers that changes claims rather than defending them.

Chapter 5 produced a mixed result: strong benefit over customer-first ordering, a trade-off that failed its margin, no benefit over critical-flag lists in one region and a large benefit in another. This chapter is where the thesis earns its claims by trying to destroy them.

### 6.1 Critique as method

Peer review at publication is too late and too shallow to be the main quality control of a doctoral project. Build critique into the project:

- **Internal red team.** Before submission, a colleague who did not work on the study is asked to break the main claim, with access to code, data and preregistration. Their report is answered in writing.
- **Structured external review.** Partners and domain experts review the model structure and the claims, using a form that asks for the *strongest* objection, not a general impression.
- **Adversarial collaboration.** Where a credible researcher holds an opposing view (for example, that topology-based prioritization is sufficient), design a joint test whose outcomes both sides agree in advance would change their view.
- **Pre-mortem.** Imagine the thesis was rejected at defense; write the examiner's reasons. Then test each reason.

All critique and responses go into the thesis's revision record. Examiners trust work whose weaknesses have visibly been attacked.

### 6.2 The red-team report on the Cascade Study (synthetic)

An internal red team produced five main objections:

1. **Circularity.** "DEP is computed from the model's own buffers and dependency map and then evaluated in the same model. Of course it does well. In reality the planner's map is wrong."
2. **Short-buffer artefact.** "Riverbend's buffers are short relative to restoration times. With realistic fuel contracts nothing you do matters."
3. **Context selection.** "Port Halvard was chosen to make the mechanism operate. Two regions, one picked for the method, cannot estimate how often DEP helps."
4. **Heuristic weakness.** "Your own oracle shows DEP is far from optimal in Riverbend. Why should anyone adopt a rule you know is suboptimal?"
5. **Dual use.** "You have shown that critical-service loss depends on which feeder is restored first and on whether the planner's map is right. That tells an adversary what to attack: the restoration-priority data."

Each objection is a hypothesis about the result. The rest of the chapter tests them.

### 6.3 Practical activity: boundary conditions, mismatch and many regions

The lab imports the Lab 5 simulator (save it as `lab5_mc.py` in the same folder).

```python
# Lab 6 - boundary conditions, model mismatch and many synthetic regions (offline)
# Save Lab 5 as lab5_mc.py in the same folder first.
import random, statistics
import lab5_mc as m

def mean_gain(region, **kw):
    _, res, cust = m.experiment(region, n=300, oracle=False, **kw)
    return (statistics.fmean(res["DEP"]) - statistics.fmean(res["CRITFLAG"]),
            statistics.fmean(res["DEP"]) - statistics.fmean(res["SILO"]))

print("1) Riverbend buffer scaling: (DEP-CRITFLAG, DEP-SILO) mean loss")
for s in (0.5, 1.0, 2.0, 4.0):
    a, b = mean_gain(m.RIVERBEND, buffer_scale=s)
    print(f"   scale {s:3.1f}: {a:7.2f} {b:7.2f}")

print("2) Model mismatch: water plant truly on F1, planner believes F3")
true = {**m.RIVERBEND, "services": {**m.RIVERBEND["services"], "WATER": ("F1",) + m.RIVERBEND["services"]["WATER"][1:]}}
_, res, _ = m.experiment(true, n=300, oracle=False, believed_feeder={"WATER": "F3"})
print("   mean loss SILO %.2f CRITFLAG %.2f DEP %.2f" % tuple(statistics.fmean(res[k]) for k in ("SILO", "CRITFLAG", "DEP")))

print("3) 200 random synthetic regions: gain of DEP over CRITFLAG vs rank divergence")
def random_region(rng):
    feeders = [f"G{i}" for i in range(1, 6)]
    cust = {f: rng.choice([500, 1000, 2000, 4000, 8000]) for f in feeders}
    crit = rng.sample(feeders, 3)
    services = {}
    for i, f in enumerate(crit):
        lo = rng.choice([1, 4, 12, 36])
        services[f"S{i}"] = (f, (lo, lo * 3, lo * 2), rng.choice([3.0, 4.0, 5.0]), None)
    return {"customers": cust, "crews": 1, "dur": (2, 6, 4), "services": services}
def divergence(region):
    flag = [f for f in m.critflag(region) if f in {v[0] for v in region["services"].values()}]
    depo = [f for f in m.dep(region) if f in flag]
    return sum(1 for a, b in zip(flag, depo) if a != b)
rng = random.Random(2026)
rows = []
for _ in range(200):
    r = random_region(rng)
    _, res, _ = m.experiment(r, n=60, oracle=False)
    rows.append((divergence(r), statistics.fmean(res["DEP"]) - statistics.fmean(res["CRITFLAG"])))
for d in sorted({d for d, _ in rows}):
    g = [x for dd, x in rows if dd == d]
    print(f"   positions differing={d}: regions={len(g):3d} mean gain={statistics.fmean(g):7.2f} share DEP worse={sum(x > 0 for x in g)/len(g):.2f}")
```

Expected output:

```text
1) Riverbend buffer scaling: (DEP-CRITFLAG, DEP-SILO) mean loss
   scale 0.5:    6.10  -86.14
   scale 1.0:    0.38  -47.57
   scale 2.0:    0.02   -7.25
   scale 4.0:    0.00    0.00
2) Model mismatch: water plant truly on F1, planner believes F3
   mean loss SILO 29.41 CRITFLAG 26.21 DEP 22.29
3) 200 random synthetic regions: gain of DEP over CRITFLAG vs rank divergence
   positions differing=0: regions= 69 mean gain=   0.00 share DEP worse=0.00
   positions differing=2: regions= 77 mean gain= -11.21 share DEP worse=0.01
   positions differing=3: regions= 54 mean gain= -23.97 share DEP worse=0.00
```

#### 6.3.1 Objection 1: circularity

In part 2 the true water plant is on F1, but both the critical-customer list and the DEP planner believe it is on F3. Every criticality-aware policy degrades sharply: DEP from 4.32 to 22.29, CRITFLAG from 3.97 to 26.21. SILO actually improves (52.75 → 29.41) because it restores F1 first for customer reasons and thereby happens to restore water. The objection is **sustained in a stronger form than the red team stated**: the value of *any* criticality-aware ordering depends on the accuracy of the dependency map. The revision is to make map accuracy a stated precondition of the claim, to add a map-audit procedure to the method and to recommend measuring map error in any field application. This turns a weakness into a contribution: a *measurable* prerequisite that utilities can check.

#### 6.3.2 Objection 2: short buffers

Part 1 scales every buffer. As buffers double, DEP's advantage over SILO falls from 47.57 to 7.25 weighted service-hours and disappears at four times the elicited buffers. The objection is **sustained as a boundary condition**: when buffers comfortably exceed total restoration time, ordering does not matter for critical services. This is exactly the mechanism's prediction in Chapter 3, so the result supports the mechanism while limiting the claim's scope. It also reveals something the red team did not raise: at *half* the elicited buffers, DEP is **worse** than CRITFLAG by 6.10 — the heuristic weakness of objection 4 grows when buffers are short, because mistakes about which feeder protects more weighted services cost more.

#### 6.3.3 Objection 3: context selection

Part 3 generates 200 synthetic regions with five feeders, three critical services, random customer counts, buffer ranges and weights, and classifies them by how many positions differ between the CRITFLAG and DEP orders among critical feeders. Where the orders coincide (69 regions), the gain is exactly zero — as it must be. Where they differ in two positions (77 regions), DEP reduces mean loss by 11.21 and is worse in about 1% of regions; where they differ in three (54 regions), by 23.97, never worse in this sample. The pattern predicted by H3 holds across contexts that were not chosen for the method.

The red team's objection is nevertheless **partly sustained**: the generator draws customer counts and buffers independently, and that assumption fixes how often divergence occurs. Real regions may have correlations in either direction. If large feeders tend to host facilities with long buffers (large hospitals with large fuel stores), CRITFLAG's largest-first order runs opposite to DEP's shortest-buffer-first order and divergence becomes *more* common; if large feeders tend to host short-buffer services (dense-area telecom hubs on battery), the two orders agree and divergence becomes rarer. The frequency of divergence in real regions is an *empirical* question the thesis cannot answer with synthetic generators; the claim must be conditional on divergence, which a utility can measure about itself.

#### 6.3.4 Objection 4: a known-suboptimal heuristic

Sustained. The oracle bound shows that a rule using weights and fan-out — for example, ordering feeders by the weighted value of the services they protect per hour of restoration, accounting for dependencies — could do better. The candidate may develop such a rule, but it must be labelled **exploratory**: it would be designed after seeing the confirmatory results and must be confirmed on new configurations (new regions, new seeds, preregistered) before any claim is made. The thesis can legitimately present it as the most promising next step.

### 6.4 Sensitivity analysis beyond one factor at a time

Varying one factor at a time (buffers, then weights, then durations) misses interactions — the buffer-scaling result shows that the heuristic's weakness interacts with buffer length. **Global sensitivity analysis** varies all uncertain inputs together and apportions output variance to inputs and their interactions; [Saltelli et al. (2008)](https://doi.org/10.1002/9780470725184) is a standard primer. For a thesis, a practical sequence is: one-at-a-time screening to find inputs that matter; a structured design (for example, a factorial over the few that matter); then, if resources allow, variance-based indices. Report what the conclusion depends on, in the reader's terms: *"DEP's advantage over critical-flag ordering requires divergence between buffer and customer orders, a dependency map without feeder errors, and buffers shorter than about twice the expected restoration time."*

Value sensitivity is distinct from parameter sensitivity. The predeclared weights encode one panel's priorities. Re-run with alternative weight sets — equal weights, weights from a second panel, weights that include ordinary customers — and report whether conclusions change (EX034).

### 6.5 Negative results and narrowing

The Cascade Study now has a narrowed claim:

> In synthetic distribution-outage scenarios requiring sequential manual restoration, ordering by critical-service time-to-impact reduces predeclared weighted critical-service loss relative to critical-customer-flag ordering **only** when the two orders differ, the dependency map is accurate and buffers are short relative to restoration time; where these conditions hold, the reduction is large and the additional customer-hours relative to flag ordering are within a 15% margin. Any criticality-aware ordering protects critical services far better than customer-first ordering, at a customer-hour cost of roughly 60–70% in the regions studied, which exceeds the predeclared margin and is a policy trade-off rather than a technical improvement. The earliest-time-to-impact heuristic can underperform flag ordering when buffers are very short, because it ignores weights and fan-out.

Notice what the narrowed claim does: it states conditions a utility can measure; it reports the failed margin; it reports where the method loses; and it separates the robust finding (criticality-aware ordering versus customer-first) from the conditional contribution (timing versus lists). A negative result about H2 in Riverbend is not hidden; it is the evidence that defines the boundary.

**Publish negative results usefully.** State the hypothesis, the design, the effect size with its interval and the smallest effect of interest it rules out. "No significant difference" is useless; "a reduction of 10% or more relative to flag ordering is ruled out in Riverbend" is useful.

### 6.6 Dual-use review of the findings

Applying the three questions of Chapter 1 (§1.4.3):

| Finding | Uplift to an adversary | Defensive value | Decision |
|---|---|---|---|
| Criticality-aware ordering protects critical services; cost in customer-hours | Negligible: widely understood | Supports policy debate on restoration priorities | Publish |
| Value depends on dependency-map accuracy | Moderate: suggests that corrupting or stealing restoration-priority data and critical-customer lists could amplify an attack | High: tells utilities to protect the integrity and confidentiality of restoration-priority data and to audit maps | Publish at the general level with the defensive recommendation; no examples of how to alter such data |
| Synthetic regions, code and parameters | Low: invented places | High: reproducibility | Publish (Chapter 7, tier T0) |
| Partner-derived buffer ranges and feeder–facility relations | High: targeting information | Low beyond the partner | Withhold; describe aggregate ranges only |
| Tabletop rationales | Low | Moderate | Publish themes without role-plus-utility identifiers |

The second row illustrates a recurring pattern in infrastructure research: a resilience finding often doubles as an attack-surface finding. The relevant threat context is public — CISA's [AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a) describes pre-positioning in infrastructure IT networks, where planning data typically lives — so the defensive recommendation (integrity protection and audit of restoration-priority data) has clear value. Coordinate with partners and, where appropriate, the relevant sector information-sharing body before publication (Chapter 8).

### 6.7 Responding to reviewers

A good response letter quotes each comment, states whether it is accepted, partly accepted or not accepted, describes the change (with location), and — when not accepted — gives evidence rather than opinion. Most importantly, it **changes claims**, not just wording. Compare:

- *Defensive:* "We thank the reviewer. Port Halvard was selected on predeclared criteria, so selection bias is not a concern."
- *Responsive:* "Partly accepted. Port Halvard was selected on predeclared mechanism-derived criteria, which makes it a fair test of the mechanism but not an estimate of how often DEP helps. We added a 200-region analysis (§6.3.3), narrowed the claim to regions with order divergence and stated that the frequency of divergence in real regions is unknown (Limitations, item 4)."

### 6.8 Common errors and limits

- Treating peer review as a hurdle instead of a method.
- Evaluating a policy only in the model used to derive it.
- Reporting only one-factor-at-a-time sensitivity.
- Treating a random-context generator as a sample of reality.
- Presenting an exploratory revision as confirmatory.
- Writing negative results as "not significant".
- Skipping dual-use review because results are "only simulations".

- Accepting a red-team objection in its original form without testing whether a stronger version holds, as happened with circularity.
- Treating a boundary condition as a defeat rather than as a confirmed prediction of the mechanism that narrows the claim.
- Assuming a random-region generator's independence assumptions match real regions, where customer counts and buffers may be correlated.
- Writing a response letter that thanks reviewers and defends the original claim instead of changing it where the evidence requires.
- Publishing partner-derived buffer ranges because they look harmless in aggregate.

### Exercises — chapter 6

**EX033 — Red-team report.** *Objective:* attack your own claim. *Inputs:* the Cascade Study claim before narrowing (Chapter 5 summary) or your own. *Constraints:* at least five objections, each stated as a testable hypothesis. *Steps:* (1) write each objection; (2) say what evidence would sustain or dismiss it; (3) design the test; (4) predict the outcome before running anything. *Expected evidence:* report. *Rubric:* 3 = objections specific and testable, including circularity and context selection, with predictions recorded before testing; 2 = one or two untestable; 1 = generic; 0 = none.

**EX034 — Weight sensitivity.** *Objective:* test value sensitivity. *Inputs:* Lab 5 and Lab 6. *Constraints:* offline. *Steps:* (1) set all service weights to 1.0 in both regions; (2) re-run the main comparison; (3) record DEP, CRITFLAG and SILO losses; (4) state whether each verdict of the hypothesis table changes; (5) explain why. *Expected evidence:* modified code, outputs, paragraph. *Rubric:* 3 = exact outputs, correct verdict analysis, explanation tied to fan-out and weights; 2 = outputs right, explanation thin; 1 = errors; 0 = not run.

**EX035 — Map-error experiment.** *Objective:* quantify fragility to map error. *Inputs:* Lab 6 part 2. *Constraints:* offline. *Steps:* (1) repeat the mismatch with the telecom office truly on F4 while the planners believe F2; (2) record the losses; (3) compare with part 2; (4) propose a map-audit procedure with a measurable accuracy target. *Expected evidence:* outputs and procedure. *Rubric:* 3 = correct outputs, comparison with the water mismatch, audit procedure measurable (sampled field verification, accuracy rate, owner sign-off); 2 = procedure vague; 1 = not run correctly; 0 = none.

**EX036 — Generator critique.** *Objective:* recognize the generator as a model. *Inputs:* `random_region` in Lab 6. *Constraints:* propose a change that encodes a plausible real-world correlation. *Steps:* (1) modify the generator so that larger feeders tend to host critical services with longer buffers; (2) re-run part 3; (3) compare the distribution of divergence and gains with the original part 3; (4) predict, then check, what the opposite correlation would do; (5) explain what this means for the claim. *Expected evidence:* code, output, paragraph. *Rubric:* 3 = correlation implemented sensibly; learner notices that this correlation makes CRITFLAG and DEP orders run in opposite directions, so divergence becomes *more* frequent (regions with no divergence fall sharply), and explains that the opposite correlation would make it rarer, so the claim must stay conditional on measured divergence; 2 = implementation sound but the direction of the effect misread; 1 = no comparison; 0 = none.

**EX037 — Dual-use decision.** *Objective:* decide publication treatment. *Inputs:* four findings from your own research or: (a) a list of water utilities whose SCADA is reachable via a specific vendor's remote-access product; (b) the observation that remote-access products are a common entry point across sectors; (c) a method to estimate time-to-impact from public facility data; (d) the time-to-impact estimates for named hospitals in one city. *Constraints:* the three questions of §1.4.3. *Steps:* (1) assess uplift for each finding; (2) assess defensive value; (3) decide among publish, generalize, delay and restrict; (4) state who should be notified before publication. *Expected evidence:* table. *Rubric:* 3 = (a) restrict and notify via coordinated disclosure, (b) publish, (c) publish with care, (d) withhold or restrict, with sound reasoning; 2 = one misjudged; 1 = two or more; 0 = none.

**EX038 — Response letter.** *Objective:* change claims in response to critique. *Inputs:* the five red-team objections in §6.2. *Constraints:* one response per objection; at least two must lead to a changed claim. *Steps:* (1) quote each objection; (2) mark it accepted, partly accepted or not accepted; (3) describe the change and its location; (4) give evidence for any non-acceptance. *Expected evidence:* response letter. *Rubric:* 3 = responsive rather than defensive, claims changed where warranted, exploratory work labelled; 2 = mostly responsive; 1 = defensive; 0 = none.

### Chapter synthesis

Critique is part of the method. The red team's objections became hypotheses and tests. Circularity was sustained in a stronger form — every criticality-aware policy depends on an accurate dependency map — which became a measurable precondition and a defensive recommendation. Short buffers were confirmed as a boundary condition predicted by the mechanism, and very short buffers exposed the heuristic's weakness. A 200-region analysis supported the mechanism across contexts not chosen for it while reminding us that a generator is a model. The narrowed claim states measurable conditions, reports the failed margin and separates the robust finding from the conditional contribution. Dual-use review showed that a resilience finding can also be an attack-surface finding and decided what to publish at what level.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 08

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Thesis synthesis and reproducibility archive

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Structure a thesis as an argument in which every claim is linked to evidence, warrant, scope and limitation.
2. Decide between a monograph and a thesis by publication and integrate either into one coherent argument.
3. Design a tiered reproducibility archive that releases as much as is lawful and safe, under infrastructure-information protection.
4. Distinguish invented synthetic data from synthetic data calibrated to real places, and assess residual disclosure risk.
5. Document models, datasets and simulation studies with recognized structures.
6. Write a limitations section that informs rather than apologizes.

Chapter 6 produced the narrowed claim. This chapter assembles the thesis around it and builds the archive that lets others check it without exposing the infrastructure it studies.

### 7.1 The thesis as an argument

A thesis is not a report of everything done; it is an argument for a contribution. A useful scaffold is Toulmin's analysis of arguments ([Toulmin, 1958/2003](https://doi.org/10.1017/CBO9780511840005)): a **claim** supported by **data** (evidence) through a **warrant** (the reason the evidence supports the claim), with **backing** for the warrant, a **qualifier** (how strongly) and **rebuttals** (conditions under which the claim fails). Applied to infrastructure research:

| Element | Cascade Study example |
|---|---|
| Claim | Time-to-impact ordering reduces weighted critical-service loss relative to critical-flag ordering when orders diverge, maps are accurate and buffers are short. |
| Data | Riverbend and Port Halvard paired simulations; 200-region analysis; map-error and buffer-scaling tests. |
| Warrant | The simulator represents buffer exhaustion and sequential restoration adequately for ranking orderings. |
| Backing | Verification tests; reproduction of baselines; historical validation of water timing; operational validity against expert rankings. |
| Qualifier | In synthetic regions, single scenario class (distribution outages requiring manual sequential restoration), predeclared weights. |
| Rebuttals | Map errors; long buffers; weight sets favouring fan-out; omitted human buffers and travel time; real-world divergence frequency unknown. |

Each chapter of the thesis should contribute an identifiable element. A chapter that supplies none is a candidate for an appendix.

### 7.2 Monograph or thesis by publication

A **monograph** presents one integrated argument; a **thesis by publication** collects papers with an integrating introduction and conclusion. Infrastructure theses often mix genres — a model paper, an empirical study of operators, a policy analysis — which suits publication-based theses, but the integrating chapters must do real work: state the overarching claim, show how each paper contributes data or backing, reconcile differences in scope between papers and present limitations across the whole. Regulations about format, co-authorship statements and prior publication differ between institutions; this educational track does not grant degrees and cannot advise on any institution's rules beyond pointing out that they must be checked early.

### 7.3 Structure of the Cascade Study thesis

1. **Introduction.** Problem, gap, contribution types, overarching claim and its scope.
2. **Background.** Definitions, interdependency and resilience literature, restoration practice, scheduling theory (Chapters 1–2 of this book).
3. **Method.** Mechanism, hypotheses, baselines, protocol, ethics and information protection (Chapter 3).
4. **Verification and baselines.** Reproductions, verification tests, elicitation and pilot (Chapter 4).
5. **Main study and validation.** Simulations, tabletop, validation, second region (Chapter 5).
6. **Critique and boundaries.** Red-team tests, sensitivity, many-region analysis, narrowed claim, dual-use review (Chapter 6).
7. **Discussion.** What practitioners and policy-makers can do with the narrowed claim; what remains unknown.
8. **Limitations.**
9. **Conclusion.**
10. **Appendices.** Preregistration and amendments, deviation log, verification test listing, elicitation protocols, tabletop materials, archive manifest.

### 7.4 The reproducibility archive

#### 7.4.1 Goals and constraints

Reproducibility in this field must satisfy two goals that pull in opposite directions: enabling others to check the work, and not publishing information that helps someone harm infrastructure or identifies people. The [FAIR principles](https://doi.org/10.1038/sdata.2016.18) — findable, accessible, interoperable, reusable — help here because FAIR does not mean open: data can be findable and its access conditions clearly described while access itself is controlled.

#### 7.4.2 Release tiers

| Tier | Who may access | What it holds in the Cascade Study | Conditions |
|---|---|---|---|
| T0 Public | Anyone | Simulator code, tests, synthetic region definitions, seeds, outputs, analysis scripts, tabletop materials without identifiers | Licence stated; persistent identifier |
| T1 Registered | Researchers who register and accept terms | Aggregated elicitation ranges stripped of partner identity; expanded scenario sets | Terms of use prohibit re-identification and targeting |
| T2 Controlled | Approved researchers under an agreement and, where applicable, ethics approval | Pseudonymized tabletop transcripts and coded rationales | Data-use agreement; secure environment; audit |
| T3 Withheld | Not released; described only | Partner-derived feeder–facility relations, real buffer inventories, maps | Existence and nature described in the thesis so that examiners know what is missing and why |

The archive's **manifest** lists every file with a cryptographic hash and its tier, so that anyone can verify that the public files are the ones used, and examiners can see what exists at higher tiers.

#### 7.4.3 Practical activity: building a tiered manifest

```python
# Lab 7 - build a tiered reproducibility manifest for a synthetic thesis archive (offline)
import hashlib, json, os, tempfile
files = {
    "code/lab5_mc.py": b"# simulation code\n",
    "data/synthetic_riverbend_params.csv": b"feeder,customers\nF1,9000\nF2,1200\nF3,2500\nF4,6000\n",
    "data/partner_feeder_map.csv": b"feeder,substation,gps\nF2,SUB-7,redacted\n",
    "results/mc_summary.json": b'{"mean_dloss": -46.86}\n',
    "docs/operator_interview_notes.txt": b"P03: we restore by customer count\n",
}
RULES = [  # first matching rule wins; order matters
    ("partner_", "T3-withheld: partner-owned infrastructure detail; describe, do not release"),
    ("interview", "T2-controlled: human-subjects data; release only under approved access agreement"),
    ("synthetic_", "T0-public"),
    ("code/", "T0-public"),
    ("results/", "T0-public"),
]
def tier(path):
    for key, label in RULES:
        if key in path:
            return label
    return "UNCLASSIFIED: stop and review"
with tempfile.TemporaryDirectory() as root:
    manifest = []
    for rel, content in sorted(files.items()):
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(content)
        manifest.append({"path": rel, "sha256": hashlib.sha256(content).hexdigest()[:16], "tier": tier(rel)})
    print(json.dumps(manifest, indent=1))
    print("public files:", sum(m["tier"].startswith("T0") for m in manifest), "of", len(manifest))
```

Expected output:

```text
[
 {
  "path": "code/lab5_mc.py",
  "sha256": "e9db014f8aeb90da",
  "tier": "T0-public"
 },
 {
  "path": "data/partner_feeder_map.csv",
  "sha256": "160cefe894e75af9",
  "tier": "T3-withheld: partner-owned infrastructure detail; describe, do not release"
 },
 {
  "path": "data/synthetic_riverbend_params.csv",
  "sha256": "66bd4b5c8f37d273",
  "tier": "T0-public"
 },
 {
  "path": "docs/operator_interview_notes.txt",
  "sha256": "35c6e20265ce92c5",
  "tier": "T2-controlled: human-subjects data; release only under approved access agreement"
 },
 {
  "path": "results/mc_summary.json",
  "sha256": "7bde71d2f02e64ad",
  "tier": "T0-public"
 }
]
public files: 3 of 5
```

Two design choices deserve attention. First, the rules are **ordered** and the first match wins: if the "synthetic" rule were placed before the "partner" rule, a file named `synthetic_partner_feeders.csv` would be published. Order the most restrictive rules first. Second, an unmatched file returns **"UNCLASSIFIED: stop and review"** rather than a default tier; a release pipeline should fail closed. Real pipelines would also scan file *contents* (coordinates, asset identifiers, names), not only paths.

### 7.5 Synthetic data: invented versus calibrated

The regions in this book are **invented**: their numbers were chosen to teach, and they correspond to no place. A thesis based on a real partner would more likely produce **calibrated** synthetic data — generated to match statistical properties of real data. Calibration preserves research value and also preserves some disclosure risk: if the real region has a single hospital on a small feeder with a short-buffer water plant, a calibrated synthetic region that preserves those relations may still point to it. Assess residual risk explicitly: Could an informed person match the synthetic configuration to a real one? Would that match reveal anything not already public? Generalizing (ranges instead of values), perturbing, and mixing several real configurations reduce risk; the assessment and the chosen measures belong in the archive documentation.

### 7.6 Documenting models, data and studies

- **Models.** For agent-based components, the ODD protocol — overview, design concepts, details — gives a standard structure ([Grimm et al., 2006](https://doi.org/10.1016/j.ecolmodel.2006.04.023)). For any simulator, document purpose, entities and state variables, processes and scheduling, inputs and their sources, verification tests and known limitations.
- **Datasets.** Datasheets record motivation, composition, collection process, preprocessing, uses, distribution and maintenance ([Gebru et al., 2021](https://doi.org/10.1145/3458723)).
- **Learned components.** If the study includes a learned model (for example, a detector), a model card records intended use, evaluation conditions and limitations ([Mitchell et al., 2019](https://doi.org/10.1145/3287560.3287596)).
- **Computation.** Pin language and library versions, record seeds, provide a single command that regenerates every table and figure, and include the verification tests. [Sandve et al. (2013)](https://doi.org/10.1371/journal.pcbi.1003285) give ten practical rules.

### 7.7 Writing limitations

A limitations section is part of the argument: it states the rebuttal conditions and their likely direction. Weak limitations sections list generic caveats ("more research is needed"). Strong ones say, for each limitation, *what* it is, *how* it could change the result and *in which direction*, and *what study* would resolve it. For the Cascade Study:

| Limitation | Possible effect | Direction | Resolving study |
|---|---|---|---|
| Human buffers (trucked water, fuel deliveries, load shedding) omitted | Model overstates consequence of all orderings and the benefit of reordering | Toward smaller benefit | Model buffer extension as conditional on telecom and roads; validate against after-action records |
| Travel time between feeders omitted | Orderings that jump between distant feeders cost more than modelled | Toward smaller benefit of DEP when critical feeders are dispersed | Add a travel-time matrix; re-run |
| Synthetic regions only | Frequency of divergence in real regions unknown | Unknown | Survey of utilities measuring divergence, under T3 protection |
| Weights from one panel | Verdicts change with weights (EX034) | Either | Multiple panels; report verdicts per weight set |
| Tabletop sample of 12 from 3 utilities | Adoption evidence weak | Toward overstatement of adoptability | Larger, stratified study; field pilot during exercises |
| Cyber scenario class limited to distribution outages requiring manual restoration | Does not cover attacks on restoration tools or on priority data | Unknown | Scenario family including integrity attacks on planning data (motivated by §6.6) |

### 7.8 Worked example: assembling the archive

The candidate's first archive plan placed everything at T2 "to be safe". The committee rejected it: over-restriction prevents verification and is not safe, only unaccountable. The revised plan used the tier table in §7.4.2, published all code and synthetic configurations at T0 with a single regeneration command, placed tabletop transcripts at T2 under the consent terms participants signed, and recorded the T3 partner material in a description that told examiners exactly which analyses depended on it — none of the confirmatory results did, by design, because the study used invented regions for all public claims and used partner data only for elicitation ranges and face validity. That design decision, made in Chapter 1, is what made a largely public archive possible.

### 7.9 Common errors and limits

- Writing the thesis as a chronological lab notebook rather than an argument.
- Restricting everything, or publishing everything, instead of tiering.
- Equating FAIR with open.
- Treating calibrated synthetic data as automatically safe.
- Release scripts that fail open.
- Limitations sections without direction or resolving studies.

- Placing everything at a restrictive tier to be safe, which prevents verification and makes the work unaccountable rather than safe.
- Ordering release rules so that a permissive pattern such as synthetic matches before a restrictive one such as partner.
- Classifying files by name alone, without scanning contents for coordinates, asset identifiers or names.
- Letting confirmatory results depend on withheld partner material, so examiners cannot check them.
- Omitting a single command that regenerates every table and figure from the public files.

### Exercises — chapter 7

**EX039 — Argument map.** *Objective:* expose the thesis argument. *Inputs:* the narrowed claim of §6.5. *Constraints:* use all six Toulmin elements. *Steps:* (1) map the claim; (2) mark which thesis chapter supplies each element; (3) identify the weakest warrant and the evidence that would strengthen it. *Expected evidence:* map and paragraph. *Rubric:* 3 = complete map, weakest warrant correctly identified (model adequacy for real regions, or omitted human buffers) with a specific strengthening study; 2 = one element thin; 1 = claim and data only; 0 = none.

**EX040 — Tier assignment.** *Objective:* tier a realistic archive. *Inputs:* ten artifacts: simulator code; verification tests; Riverbend configuration; elicitation forms with partner names; aggregated elicitation ranges; tabletop audio; coded rationales; consent forms; a partner's restoration procedure; final figures. *Constraints:* use the four tiers; justify each. *Steps:* (1) assign each artifact a tier; (2) justify the tier in one line; (3) propose a transformation that would move each restricted item to a more open tier. *Expected evidence:* table. *Rubric:* 3 = sensible tiers (code, tests, configurations and figures T0; aggregated ranges T1; coded rationales T2 or T1 if de-identified; audio, consent forms and named elicitation forms T2 or T3; partner procedure T3) with transformations; 2 = one or two misjudged; 1 = uniform tiering; 0 = none.

**EX041 — Fail-closed manifest.** *Objective:* improve Lab 7. *Inputs:* Lab 7. *Constraints:* offline. *Steps:* (1) add a file `data/synthetic_partner_feeders.csv`; (2) show that the current rule order classifies it correctly and explain why; (3) move the `synthetic_` rule first, re-run and record the failure; (4) add a content check that refuses public tier for any file containing the string `SUB-`. *Expected evidence:* code, outputs, explanation. *Rubric:* 3 = demonstrates the ordering hazard, the content check works, explanation links to fail-closed design; 2 = partial; 1 = not run; 0 = none.

**EX042 — Residual disclosure assessment.** *Objective:* assess calibrated synthetic data. *Inputs:* a synthetic region calibrated to a real county with one hospital, two water plants and five feeders, preserving which feeder hosts the hospital. *Constraints:* use the questions in §7.5. *Steps:* (1) assess the re-identification risk; (2) assess what a match would reveal; (3) propose transformations and evaluate their cost to research value. *Expected evidence:* one-page assessment. *Rubric:* 3 = recognizes re-identification through unique structure, proposes mixing or generalization, weighs research value honestly; 2 = assessment shallow; 1 = declares synthetic safe; 0 = none.

**EX043 — Model documentation.** *Objective:* document the Lab 5 simulator. *Inputs:* Lab 5 code. *Constraints:* follow the model elements in §7.6; at most two pages. *Steps:* (1) write purpose, entities, processes and scheduling; (2) list inputs and their sources; (3) list the verification tests; (4) list known limitations, including at least three from §7.7. *Expected evidence:* document. *Rubric:* 3 = accurate to the code (event-based intervals, restart lag, crew assignment, OR semantics for dependencies), limitations specific; 2 = minor inaccuracies; 1 = generic; 0 = none.

**EX044 — Limitations section.** *Objective:* write limitations that inform. *Inputs:* your own study or the Cascade Study. *Constraints:* at least five limitations, each with effect, direction and resolving study. *Steps:* (1) list the limitations; (2) state the effect and direction of each; (3) name the study that would resolve each; (4) rank them by how much they could change the main claim. *Expected evidence:* table and ranking paragraph. *Rubric:* 3 = specific, directional, with resolving studies and a justified ranking; 2 = directions missing for some; 1 = generic caveats; 0 = none.

### Chapter synthesis

The thesis is an argument: claim, data, warrant, backing, qualifier and rebuttals, each supplied by an identifiable part of the work. Infrastructure research must reconcile reproducibility with protection of the infrastructure studied and of the people involved; tiered archives with hashed manifests do this, and FAIR principles describe access without implying openness. Release tooling should fail closed and check content, not only names. Invented synthetic data carry little disclosure risk; calibrated synthetic data need an explicit residual-risk assessment. Document models, data and computation with recognized structures. Limitations state direction and resolving studies, which turns them into the next research agenda.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 08

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Defense and publication plan

### Learning outcomes and connection

By the end of this chapter the learner will be able to:

1. Audit a thesis claim register for unsupported, unscoped and overgeneralized claims before the defense.
2. Prepare for a defense by anticipating the strongest examiner questions and answering with evidence, scope and limits.
3. Plan a sequence of publications across communities that preserves the integrity of the overall argument.
4. Integrate coordinated disclosure and sector coordination into the publication timeline when findings touch vulnerabilities or attack surfaces.
5. Translate a narrowed research claim into policy and practice recommendations without inflating it.
6. Turn the thesis's limitations into a credible post-doctoral research program.

Chapter 7 assembled the thesis and its archive. This chapter prepares the candidate to defend it and to release it responsibly — the final step of the book and of the 207-course study path.

### 8.1 The claim audit

Before the defense, every claim in the thesis — in the abstract, introduction, chapter conclusions and general conclusion — goes into a **claim register** with its evidence, scope and limitations. Abstracts and conclusions are where overclaiming accumulates, because they are written last, in a hurry, for impact.

#### 8.1.1 Practical activity: an automated first pass

```python
# Lab 8 - audit a thesis claim register before the defense (offline)
claims = [
    {"id": "K1", "text": "Dependency-aware restoration reduced weighted critical-service loss in the Riverbend model",
     "evidence": ["Ch5-MC"], "scope": "synthetic model, single crew, 4 feeders", "limits": ["model-policy circularity"], "status": "supported"},
    {"id": "K2", "text": "The benefit persists when generator fuel buffers double",
     "evidence": ["Ch6-boundary"], "scope": "gen_scale 2-4", "limits": [], "status": "supported"},
    {"id": "K3", "text": "Operators would adopt the dependency-aware ordering",
     "evidence": [], "scope": "", "limits": [], "status": "supported"},
    {"id": "K4", "text": "Dependency-aware restoration improves resilience of US utilities",
     "evidence": ["Ch5-MC", "Ch6-PortHalvard"], "scope": "two synthetic regions", "limits": ["no field data"], "status": "supported"},
]
OVERREACH = ("US utilities", "all utilities", "proves", "always")
for c in claims:
    problems = []
    if c["status"] == "supported" and not c["evidence"]:
        problems.append("no evidence for a supported claim")
    if not c["scope"]:
        problems.append("scope missing")
    if not c["limits"]:
        problems.append("no stated limitation")
    if any(w in c["text"] for w in OVERREACH) and "synthetic" in c["scope"]:
        problems.append("text generalizes beyond its synthetic scope")
    print(c["id"], "OK" if not problems else "; ".join(problems))
```

Expected output:

```text
K1 OK
K2 no stated limitation
K3 no evidence for a supported claim; scope missing; no stated limitation
K4 text generalizes beyond its synthetic scope
```

The script catches three classic failures. K2 is supported but states no limitation — yet Chapter 6 showed that the benefit over SILO shrinks sharply as buffers grow, so "persists when buffers double" needs the qualifier that the benefit falls by about 85% at twice the buffers. K3 is marked supported with no evidence: the tabletop showed that a display *can shift choices in a tabletop*, which is not adoption. K4 generalizes from two synthetic regions to "US utilities". A keyword filter is crude — it would miss "nationwide" or "the grid" — so the script is a first pass; the decisive audit is a human reading every claim against the register.

#### 8.1.2 Corrected claims

| ID | Corrected text |
|---|---|
| K1 | In the synthetic Riverbend model, all criticality-aware orderings reduced weighted critical-service loss by about 90% relative to customer-first ordering, at about 70% more customer-hours; time-to-impact ordering did not improve on critical-flag ordering there. |
| K2 | The advantage of criticality-aware ordering over customer-first ordering fell by about 85% when buffers were doubled and vanished at four times the elicited buffers. |
| K3 | In a tabletop with twelve participants from three synthetic utilities, a time-to-impact display shifted seven participants' chosen orderings toward the lower-consequence ordering; adoption in practice was not studied. |
| K4 | Across two synthetic regions and 200 generated regions, time-to-impact ordering improved on critical-flag ordering only where their orders diverged; how often this occurs in real regions is unknown. |

### 8.2 Preparing the defense

#### 8.2.1 What examiners test

Examiners test whether the candidate is an independent researcher: whether they understand their contribution's limits better than anyone, can defend design choices against alternatives, and know the literature well enough to place the work. Expect questions in six families:

| Family | Example question for the Cascade Study | What a strong answer contains |
|---|---|---|
| Contribution | "What is new here, given that utilities already keep critical-customer lists?" | The narrowed claim; the conditions under which timing adds value; the measurable preconditions (divergence, map accuracy); the scheduling-theory framing. |
| Design | "Why simulation and a tabletop rather than a field study?" | Safety and ethics (never test on production); rarity of real events; the use of historical validation; what a field pilot during exercises would add next. |
| Validity | "Isn't the result circular?" | The mismatch test; independent modeller for Port Halvard; the generator analysis; what remains circular. |
| Values | "Who decided that hospitals matter five times more than a telecom office, and why should anyone accept it?" | Elicitation process, panel, date, sensitivity of verdicts to weights (EX034), explicit statement that weights are a policy choice. |
| Ethics and dual use | "Have you just told adversaries to attack restoration-priority data?" | The dual-use review; general-level publication; defensive recommendation; coordination before publication. |
| Field knowledge | "How does your work relate to consequence-driven engineering approaches?" | CCE's consequence-first logic; the thesis as a contribution to the *recovery* side; differences in unit of analysis. |

#### 8.2.2 Mock defenses

Hold at least two mock defenses: one with friendly experts in the domain and one with a hostile methodologist from outside it. Record the questions you could not answer well; each is either a gap in the thesis (fix it), a gap in your preparation (study it) or a genuine open question (say so in the defense — "I don't know, and here is how I would find out" is a strong answer).

#### 8.2.3 Answering

Answer the question asked, then give evidence, then state the limit. Avoid three habits: defending a claim stronger than the thesis makes; conceding a point that the thesis actually addresses because of nerves; and filling silence with speculation. When an examiner proposes an alternative explanation you did not test, the best response describes the test that would distinguish it and what each outcome would mean.

### 8.3 Publication plan

#### 8.3.1 Sequencing papers

The Cascade Study naturally divides into papers for different communities:

1. **Methods/OR paper.** Restoration ordering under buffer-limited critical services: the scheduling framing, the oracle bound, the heuristic and its failure modes, the 200-region analysis. Audience: reliability, risk and operations-research venues.
2. **Infrastructure-security paper.** Dependency-map integrity as a precondition of criticality-aware restoration, with the mismatch results and the dual-use-reviewed defensive recommendation. Audience: critical-infrastructure-protection venues and CPS-security workshops.
3. **Human-factors paper.** The tabletop study: display, choices, rationales and omitted variables. Audience: human factors and emergency management.
4. **Replication note.** The GridWater-Sim reproduction after correcting a parameter-order ambiguity, with the verification tests. Audience: the benchmark's community; also valuable as a data or software paper.

Publish the archive's T0 components with persistent identifiers alongside the first paper, so later papers cite the same versioned artifacts. Each paper must state the overall claim's scope and must not cite another paper from the thesis as stronger evidence than it is.

#### 8.3.2 Preprints, embargoes and sensitive results

Preprints accelerate feedback and establish priority. For results that touch attack surfaces, decide *before* the preprint whether coordination is needed (§8.4); a preprint is a publication. Funders and partners may have notice periods in their agreements (Chapter 1, §1.5.3); honour them, and refuse any request that would amount to a veto on findings.

### 8.4 Coordinated disclosure and sector coordination

Infrastructure research can produce three kinds of sensitive finding, each with its own route:

| Finding | Example | Route |
|---|---|---|
| A product vulnerability | A flaw in a vendor's outage-management software found while building the simulator | Coordinated vulnerability disclosure to the vendor, directly or through a coordinator such as [CISA's CVD program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program); international practice is described in ISO/IEC 29147 (disclosure) and ISO/IEC 30111 (handling). |
| An organization-specific weakness | A partner's critical-customer list has wrong feeder assignments | Private report to the partner under the data-use agreement; never published in identifiable form. |
| A sector-level attack surface | Restoration-priority data and dependency maps are high-value targets whose corruption amplifies outages | Coordinate with partners and, where appropriate, the relevant sector information-sharing organization before publication; publish at a general level with defensive recommendations. |

Build the coordination period into the timeline. CISA describes its process as covering supplier outreach, analysis, remediation coordination and advisory publication, and notes that it may disclose after a period if a vendor is unresponsive; read the current policy rather than relying on a summary. The thesis records what was disclosed, to whom, when, and what was withheld.

### 8.5 Translating to policy and practice

Policy audiences need recommendations that follow from the evidence and say how confident they are. From the narrowed Cascade Study claim, defensible recommendations are:

1. **Make the trade-off explicit.** Prioritizing critical services in restoration costs ordinary customers time without power; the size of that cost should be estimated and discussed in emergency plans and, where appropriate, public consultation. (Strong evidence within the model; the direction is a scheduling-theory result.)
2. **Audit dependency maps.** Criticality-aware restoration is only as good as the feeder-to-facility map and buffer data behind it; utilities and their partners should verify these regularly. (Strong evidence of fragility within the model.)
3. **Protect restoration-priority data.** Treat critical-customer lists, dependency maps and buffer inventories as sensitive and integrity-critical. (Inference from the mismatch results and public threat reporting; moderate confidence.)
4. **Measure divergence before changing practice.** A utility can determine whether time-to-impact ordering would change its current critical-list order; if not, it gains nothing from adopting it. (Conditional on the model; low cost to check.)

These map naturally onto risk-management processes that already exist — sector risk management under NSM-22 in the United States, risk assessments of critical entities under the CER Directive in the EU — without claiming that any authority should mandate them. A policy brief is two pages, states its evidence base and its limits, and links to the thesis and archive.

### 8.6 The post-doctoral program

The limitations table of Chapter 7 is a research agenda. A credible three-study program:

1. **Real-region divergence survey** (empirical, protected): measure, under T3 protection, how often time-to-impact and critical-list orders diverge across a sample of utilities. This answers the question the synthetic generators could not.
2. **Human-buffer modelling** (model + validation): represent buffer extension (fuel deliveries, trucked water) as conditional on telecom and road access, validate against after-action records, and re-test the restoration claims.
3. **Integrity attacks on planning data** (security + simulation): model adversarial corruption of dependency maps and priority lists, evaluate detection and audit strategies, and estimate their consequence value — a direct continuation of the dual-use finding, conducted with sector partners.

Each study has a falsifiable claim, a safe design and a partner model, and each would change a decision someone makes.

### 8.7 Worked example: a defense exchange (synthetic)

*Examiner:* "Your Port Halvard region was designed to make your method win. Why should I believe anything beyond Riverbend, where it failed?"

*Candidate:* "You are right that Port Halvard was selected so that the mechanism could operate; the selection criteria were preregistered before simulation, and a different modeller built it, but it is a test of the mechanism, not an estimate of how often the method helps. That is why I ran the 200-region analysis, where the gain over flag ordering is exactly zero whenever the two orders coincide and grows with divergence, and why the thesis claims nothing about how often divergence occurs in real regions. The Riverbend failure is part of the claim: it shows the method adds nothing where orders coincide or where weights and fan-out favour another order. If you want an estimate for real utilities, the study I would run first is the divergence survey I describe in the conclusion."

The answer concedes what is true, cites the specific evidence, restates the narrowed claim and names the next study. It does not defend the original, broader claim.

### 8.8 Common errors and limits

- Abstracts and conclusions that claim more than the chapters.
- Treating the defense as a presentation rather than an examination of independence.
- Publishing papers whose claims drift beyond the thesis's scope.
- Posting preprints before deciding whether coordination is needed.
- Policy recommendations without confidence levels or evidence links.
- Post-doctoral plans that repeat the thesis instead of addressing its limitations.

- Keeping a claim register but auditing it only by keyword, which misses overreach phrased as nationwide or the grid.
- Answering an examiner's alternative explanation by defending the original claim instead of describing the test that would distinguish them.
- Posting the infrastructure-security paper before partners and the sector information-sharing body have been consulted on the map-integrity finding.
- Citing one paper from the thesis as stronger evidence than it is in the next paper.
- Writing policy recommendations that imply a mandate the evidence does not support.

### Exercises — chapter 8

**EX045 — Claim audit.** *Objective:* audit a claim register. *Inputs:* Lab 8. *Constraints:* offline. *Steps:* (1) run the lab and record the output; (2) add a claim K5, "Our method makes the grid resilient to cyber attacks", with evidence `["Ch5-MC"]`, scope "synthetic model" and limits `["no field data"]`; (3) show that the script misses it; (4) improve the check and re-run; (5) write corrected text for K5. *Expected evidence:* code, outputs, corrected claim. *Rubric:* 3 = demonstrates the miss, a sensible improved check (for example, terms such as "the grid" or "resilient to" combined with synthetic scope), corrected claim properly bounded; 2 = check improved but the claim is still inflated; 1 = not run; 0 = none.

**EX046 — Examiner question bank.** *Objective:* prepare for the defense. *Inputs:* your thesis or the Cascade Study. *Constraints:* at least two questions in each of the six families in §8.2.1; a model answer of at most 120 words for the three hardest. *Steps:* (1) write at least two questions in each family; (2) mark the three hardest; (3) draft a model answer of at most 120 words for each; (4) identify any question that reveals a gap in the thesis rather than in your preparation. *Expected evidence:* question bank and answers. *Rubric:* 3 = questions sharp and specific, answers follow the question–evidence–limit pattern, at least one real gap identified; 2 = answers defensive; 1 = generic questions; 0 = none.

**EX047 — Publication plan.** *Objective:* sequence papers with integrity. *Inputs:* the Cascade Study or your thesis. *Constraints:* three to five papers; audience, claim and evidence for each; archive versioning; coordination checkpoints. *Steps:* (1) list the papers with their audiences; (2) state each paper's claim and the evidence it uses; (3) map the shared artifacts and their versions; (4) mark where coordination or dual-use review must happen before release. *Expected evidence:* plan with a timeline. *Rubric:* 3 = papers distinct and non-overlapping in claims, shared versioned artifacts, coordination placed before any preprint touching attack surfaces; 2 = overlaps or missing checkpoints; 1 = list of titles only; 0 = none.

**EX048 — Disclosure routing.** *Objective:* route sensitive findings. *Inputs:* four synthetic findings: (a) the simulator's partner utility exports its critical-customer list to an unauthenticated internal web page; (b) a commercial outage-management product accepts unsigned configuration imports; (c) across three partners, buffer inventories on paper exceed physical inventories by 20–40%; (d) restoration crews' radio procedures depend on a single repeater site. *Constraints:* §8.4 routes; state timing and what is published. *Steps:* (1) classify each finding by kind; (2) choose the route; (3) state who is notified and when; (4) state what is eventually published and at what level. *Expected evidence:* table. *Rubric:* 3 = (a) private report to the partner, (b) CVD with the vendor or a coordinator, (c) private reports plus general publication of the gap between paper and physical inventories, (d) private report and a general finding about single points of failure in restoration communications, with sound timing; 2 = one misrouted; 1 = two or more; 0 = none.

**EX049 — Policy brief.** *Objective:* translate without inflating. *Inputs:* the narrowed claim of §6.5 and recommendations in §8.5. *Constraints:* two pages; confidence level and evidence link for every recommendation; one paragraph on what the research does not show. *Steps:* (1) write the brief; (2) mark each sentence as evidence, inference or recommendation; (3) remove any sentence that cannot be traced to the thesis. *Expected evidence:* brief with markings. *Rubric:* 3 = recommendations traceable and qualified, non-findings explicit, accessible language; 2 = some untraceable sentences; 1 = advocacy without evidence; 0 = none.

**EX050 — Post-doctoral research program.** *Objective:* convert limitations into research. *Inputs:* your EX044 limitations table or §7.7. *Constraints:* three studies; each with a falsifiable claim, a safe design, a partner model and the decision it would change. *Steps:* (1) choose three limitations; (2) design a study for each; (3) order the studies by dependency and value; (4) state what result would end the program. *Expected evidence:* two-page program. *Rubric:* 3 = studies directly address the most consequential limitations, are falsifiable and safe, and are ordered by dependency, with an honest stopping result; 2 = one study weak; 1 = repeats the thesis; 0 = none.

### Chapter synthesis

The defense examines independence: the candidate must know the contribution's limits better than anyone. A claim register, audited by script and by reading, removes the overclaims that accumulate in abstracts and conclusions. Examiners' questions fall into predictable families; answer with evidence and limits, and name the study that would settle what you do not know. Publish in sequence across communities with versioned shared artifacts, and decide on coordination before any preprint touches an attack surface. Route vulnerabilities, organization-specific weaknesses and sector-level attack surfaces differently. Translate narrowed claims into recommendations with confidence levels. The limitations become the next research program — the natural end of a doctoral course and of this study path.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 08

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Finish the 207-course route →](../SUBJECTS.md)

This is the final chapter of this course and of the 207-course study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

Each worked result shows one defensible answer and explains what the rubric rewards. Alternative answers can earn full credit when they meet the same standard of evidence, scope and honesty about limits. Numerical results come from the offline labs in this book run with Python 3 standard library; if your output differs, first check the Python version, the seed and whether you changed the order of random draws.

### Chapter 1: EX001–EX007

**EX001 — Claim-ladder audit.**

| # | Assertion | Rung | Hidden assumption | Defeating observation |
|---|---|---|---|---|
| 1 | Logs show access to the distribution management system (DMS) at 01:52. | L1 if the log is preserved with clock state; otherwise L2 | The log source is intact and its clock is correct; "attacker" is already an inference | Log shows a scheduled vendor session; clock offset |
| 2 | The access was by an attacker. | L2 | The session was unauthorized | Session matches an authorized maintenance ticket |
| 3 | The access caused the outage. | L3 causal case claim | Commands were issued and the feeder opened because of them, not protection | Relay records show a protection trip; no command in DMS logs |
| 4 | The hospital lost power. | L4 consequence | The hospital's generator did not start or ran out | Generator logs show seamless transfer |
| 5 | Patients were endangered. | L4 consequence, strong | Clinical services were affected | Hospital reports no service change |
| 6 | Rural cooperatives are the weakest point in the grid. | L5 research claim from one case | One case represents a population; comparison with other utility types | Any base-rate comparison |

Rewrite: "In this synthetic case, the DMS recorded a session at 01:52 (DMS clock) whose authorization has not yet been established. A feeder serving the hospital opened at some point after; whether a command caused it, and whether the hospital lost power rather than transferring to its generator, has not been established. No conclusion about cooperatives in general follows from one case." Full credit requires flagging the generator buffer (the most likely reason the consequence claim is false) and the generalization.

**EX002 — Definition and population.** A defensible answer quotes: the statutory definition used by U.S. policy (42 U.S.C. § 5195c(e)) and NSM-22's sector structure via CISA's page; CER Article 2 definitions of "critical entity" and its annex of sectors; NIS2 Article 3 with Annexes I and II (essential and important entities). Typical classification: the regional hospital falls in the U.S. Healthcare and Public Health sector, is a likely NIS2 entity in the health sector depending on size and national rules, and may be designated a critical entity under CER only if the Member State identifies it; the small water utility is in the U.S. Water sector, may fall below NIS2 size thresholds unless a Member State applies the rules to it, and is in CER's drinking-water sector if designated; the payment processor is in the U.S. Financial Services sector, falls under financial-sector rules in the EU (NIS2 contains lex specialis provisions in relation to sector-specific acts such as DORA) and under CER's banking or financial-market infrastructure sectors if designated. Design consequence: a cross-jurisdiction comparison must define its population by a common functional criterion (for example, population served and function) rather than by legal category, and report the legal status of each unit as a covariate. The rubric rewards exact citations and treats designation-dependent cases as conditional rather than certain.

**EX003 — Interdependency typing.**

| Relation | Type | Justification |
|---|---|---|
| TEL on F2 | Physical | Electricity is a material input |
| HOSP on F2 | Physical | Same |
| HOSP on WATER | Physical | Water is a material input |
| WATER on F3 | Physical | Same |
| Water SCADA on TEL | Cyber | Dependence on information carried by the telecom network |
| Billing on payment processor | Logical (or cyber) | Financial and contractual mechanism; affects operations only over days, not service delivery |
| Generator fuel on road access | Physical, with a geographic component if roads and feeders share hazards | Fuel is a material input; access may fail from the same local event |

No cycle exists among the listed services (no service in the list depends back on HOSP, WATER or TEL). A pure power-flow model would omit the fuel–road dependency, the billing dependency and the TEL dependency of water SCADA. Full credit notes that the absence of a cycle is a property of this list, not of the region: telecom often needs water for cooling and power utilities need telecom for restoration, which would create cycles.

**EX004 — Menlo analysis.** Stakeholders: dispatchers interviewed; emergency managers in the tabletop; REC, RWA, hospital and carrier as organizations; the served population; regulators; the funder; the research team. Principle-by-principle: *respect for persons* — individual consent separate from employer permission, audio optional, withdrawal without penalty, no data to managers; *beneficence* — no contact with live systems, simulation only, sensitivity test on all artifacts, physical-safety review not required because nothing is energized; *justice* — do not burden only the smallest utility; report the customer-hour trade-off so no population's loss is hidden; *law and public interest* — data-use and publication agreements, applicable information-protection regimes identified, transparent methods. Stop authority: a named partner official and the principal investigator. On withdrawal: identifiable interview data destroyed; aggregated, de-identified contributions retained only if consent forms said so. The rubric rewards concrete safeguards, especially protection of staff from disciplinary use and treatment of the served population as a stakeholder.

**EX005 — Sensitivity test.**

| Artifact | Tier | Reasoning and transformation |
|---|---|---|
| (a) Aggregated restoration durations by feeder class | Public | No specific asset or location; keep classes broad |
| (b) Hospitals with generator fuel days | Withheld | Identifies specific facilities and their buffer — targeting data. Transform to an anonymous distribution of fuel days across facility types if needed |
| (c) Model code | Public | Contains no infrastructure data; check that defaults are synthetic |
| (d) Interview coding frame | Public | No quotes or identifiers; quotes go to controlled tier |
| (e) Map of feeder serving the regional water plant | Withheld | Specific dependency of a specific asset. Describe in the thesis as "partner-supplied mapping, used for elicitation only" |

**EX006 — Metric reversal.** Output with the added metric (hourly samples with Q < 0.5): A 5 h, B 0 h, C 0 h. With a 72-hour window, C's loss rises from 7.40 to 13.40 hour-units, its time to recovery becomes 36 h and it is no longer censored; A and B are unchanged. For drinking water, a defensible primary metric is **hours below a pressure or quality threshold associated with a boil-water advisory or loss of fire-flow**, because health consequence is threshold-driven; area loss and time to recovery are secondary. Full credit names the threshold's source (utility regulation or public-health guidance in the jurisdiction) rather than inventing a value, and notes that the 0.5 threshold in the lab is illustrative.

**EX007 — Protocol skeleton.** A strong protocol fixes the question and claim rung (L5 conditional, within a scenario class); defines weighted critical-service loss and customer-hours, a 72-hour window and censoring rule; names model, elicitation, tabletop and historical records as evidence sources with their limits; specifies the four policies and two regions; pre-specifies parameters, seeds, metrics, the non-inferiority margin and the decision rule; contains the Menlo analysis, the "never test on production" rule and human-subjects approval for interviews and the tabletop; names information-protection regimes and storage; attaches data-use and publication agreements; and lists stop conditions (partner request; any data breach; any participant distress) distinct from abandonment conditions (H2 fails in both regions; model fails historical validation by more than a predeclared margin). The hostile reviewer would attack weights, circularity and context selection first.

### Chapter 2: EX008–EX014

**EX008 — Search protocol.** A model protocol for "Do ransomware incidents at hospitals affect patient outcomes in neighbouring hospitals?": concept blocks (ransomware OR cyberattack OR "cyber incident") AND (hospital OR "health system") AND (diversion OR spillover OR "neighboring" OR "nearby") AND (outcome OR mortality OR "length of stay"); sources: a biomedical index, a general scholarly index and government and sector reports; chaining from two seed studies; eligibility: studies with a comparison group or time series; screening by two reviewers on a 10% sample with agreement reported before splitting; stop when two consecutive chaining rounds add nothing. The rubric rewards cross-disciplinary sources and measured agreement.

**EX009 — Model-paper appraisal.** Structure: does the co-simulation represent buffers and restoration? Parameters: sourced or assumed? Verification: no evidence of tests in the description — unknown. Validation: one historical event, using the authors' own model; good but single. Sensitivity: unknown. Baseline: if the comparison is customer-first only, it is a weak baseline (Chapter 3). Availability: unknown. Strongest supportable claim: "In the authors' co-simulation, calibrated to one historical event, dependency-aware restoration reduced critical-service loss compared with [their baseline]" — a claim about the model (L2–L3), not about infrastructure in general.

**EX010 — Model-family fit.** (a) Input–output (IIM or economic I–O): it estimates sector-level output loss; limit — linear, no timing, facility detail aggregated away. (b) Flow or co-simulation, or a buffer-timing model like Lab 3: limit — needs facility-level data and validated buffers. (c) Empirical qualitative study (interviews, after-action records), possibly informing an agent-based model: limit — self-report and small samples. (d) Topological percolation: limit — abstract; no buffers or flows; structural insight only.

**EX011 — Standard as hypothesis.** Implicit claim: assigning and implementing SL-T per zone reduces the likelihood that an adversary of the corresponding capability achieves a consequential effect. Hypothesis: "In testbed zones implemented to SL 3 requirements, red teams of fixed capability achieve a predefined process-level effect less often, or take longer, than in otherwise identical zones implemented to SL 1." Design: isolated testbed, several equivalent zones, independent red teams blind to SL, predefined effects that are simulated rather than physical. Confounders: red-team skill and fatigue; implementation quality independent of nominal SL; learning across trials. The rubric rewards safety (testbed only) and measuring achieved rather than asserted security.

**EX012 — Repair the literature map.** Add a sixth field and filter on `s[5] == "cyber"`. Output for C3: `single-source; needs replication; strong+independent=['P7']`. C3's status is unchanged because P7 is both independent and cyber, but C1, C2 and C4 now have no qualifying support for *cyber-induced* outage claims. Explanation: evidence from all-hazard outages transfers to cyber-induced outages only by argument — cyber scenarios can be simultaneous, adversary-timed and can corrupt restoration tools — so a cyber claim needs either cyber-specific validation or an explicit transfer argument.

**EX013 — Classify the gap.** (a) *Conflicting*: next study discriminates mechanisms — measure both buffers and their depletion in the same facilities. (b) *Untransferred*: next study tests whether surge-capacity planning variables predict optimal restoration order. (c) *Weak*: vendor white papers with conflicts of interest; next study is an independent comparison with a strong baseline. (d) *Absent*: next study is a first comparative design, even a small tabletop comparison of CCE and vulnerability-driven prioritization.

**EX014 — Falsifiable statement and frontier memo.** Example statement: "In regional power outages longer than eight hours, card-payment acceptance at grocery and pharmacy outlets falls below 50% of normal within the first four hours because of telecom backhaul and point-of-sale power dependence, unless outlets hold offline-authorization capability; this is refuted if transaction records from two independent regions show acceptance above 50% at four hours among outlets without offline capability." Test notes: open (no regional study found in the documented search, hypothetically), important (food and medicine access during outages), feasible (aggregated transaction data via a payment network partner), falsifiable (stated observation). The memo argues that the dependency mapping of outlets to backhaul must come first, because without it acceptance cannot be attributed to telecom versus power. The rubric rewards a feasible refuter and a reasoned order of questions.

### Chapter 3: EX015–EX020

**EX015 — Contribution typing.** (a) Artifact — needs documentation, verification tests and evidence of use. (b) Measurement — needs reliability (test–retest, inter-rater) and validity evidence. (c) Empirical finding — needs a sampled, documented study of utilities, with sampling frame and response rates. (d) Method — needs comparison against the strongest current practice on stated metrics in more than one context. (d) uses (a) as an instrument; (a) alone cannot support (d), because the simulator's existence says nothing about whether the method beats current practice. (c) is a precondition for knowing whether (d) is novel in practice.

**EX016 — Scheduling theory check.** Ratios *w/p*: F1 9000/4 = 2250; F2 1200/3 = 400; F3 2500/5 = 500; F4 6000/4 = 1500. Smith's order: F1, F4, F3, F2. Completion times 4, 8, 13, 16 h → customer-hours = 9000·4 + 6000·8 + 2500·13 + 1200·16 = 135,700 → 135.7 thousand. Order F2, F3, F1, F4: completions 3, 8, 12, 16 → 1200·3 + 2500·8 + 9000·12 + 6000·16 = 227,600 → 227.6 thousand. Increase 67.7%. (In this book's labs, customer-hours are also counted per feeder until restoration; the restart lag applies only to critical services.)

**EX017 — Time-to-impact extension.** With F2 → HOSP = 60 and TEL → HOSP = 30, the hospital's failure time via power is min(60, 8 + 30 = 38) = 38 h, but via water it is 9 + 4 = 13 h, so HOSP still fails at 13 h. The result does not change because the binding path is water. More fundamentally, the arrangement "the generator lasts 60 h *if* telecom works to order fuel, otherwise 26 h" is a *conditional buffer* — an AND/OR combination that a shortest-path graph with fixed edge weights cannot express. Modelling it requires state-dependent buffers (as in Lab 5's dependency intervals, extended) or a simulation in which fuel deliveries are events that require TEL.

**EX018 — Hypothesis set.** Example for telecom-site restoration after a carrier cyber incident: *Benefit* — "Restoring cell sites in order of dependent-service time-to-impact reduces weighted loss of emergency-call capacity and hospital connectivity by ≥ 20% compared with restoring by subscribers served." *Best practice* — "…by ≥ 10% compared with the carrier's existing priority-site list." *Mechanism* — "The gain is zero where list order and time-to-impact order coincide and grows with divergence; it vanishes when site battery autonomy exceeds total restoration time." *Non-inferiority* — "Subscriber-hours lost increase by ≤ 15% compared with the priority-site list." Outcomes defined operationally (for example, emergency-call attempts that fail per hour, from network counters in a simulation). Thresholds justified by the carrier's stated change cost and the regulator's service-quality expectations, with owners and dates.

**EX019 — Rival-explanation table.** Rivals: any priority list explains the gain (test: list baseline); weights (test: alternative weights); short batteries in the chosen network (test: battery scaling, second network); circularity (test: independent model, map error); adoption (test: tabletop with engineers); single crew or travel ignored (test: crews and travel matrix); traffic rerouting to neighbouring sites makes the order irrelevant (test: model with neighbour coverage). Full credit includes at least circularity, baseline adequacy, weights and adoption.

**EX020 — Failure conditions and second-context criteria.** Failure conditions: as in §3.8, adapted. Second-context criteria derived from the mechanism: at least three critical-service sites; divergence between list order and time-to-impact order in at least two positions; buffer range overlapping total restoration time; a crew model different from the first context. Verification by reviewers: a timestamped preregistration amendment (in a public registry or a repository commit with a signed tag) dated before any simulation of the second context, plus the modeller's attestation that they had no access to first-context results.

### Chapter 4: EX021–EX026

**EX021 — Reproduction log.** Target: water 0.236 (synthetic paper, Table 2). Tolerance ± 0.005 fixed before running. Run 1 (matrix transposed): `[0.528, 0.028, 0.057]` — water differs by 0.208, outside tolerance; power matches. Diagnosis: the paper defines *A\*_ij* as the effect on *i* of *j*; the input file was read column-major. Run 2 (correct convention): `[0.528, 0.236, 0.163]` — reproduced. Environment: Python version, operating system, date. Decision: reproduced after correcting a convention error in our input handling. Note: power agreeing in both runs shows why checking one output is insufficient.

**EX022 — IIM perturbation analysis.** Power 0.5 alone: `[0.528, 0.236, 0.163]`. Telecom 0.5 alone: `[0.057, 0.101, 0.519]`. Both: `[0.585, 0.336, 0.682]`, which equals the sum of the two separate vectors (to rounding), because the IIM is linear: *q* = (*I* − *A\**)⁻¹ *c\** and the inverse distributes over the sum of perturbations. Supported claim: "in this linear equilibrium model, a combined power and telecom perturbation raises water inoperability to about 0.34". Unsupported: anything about timing, buffers, thresholds or restoration order — and any claim that inoperability above 1 is meaningful (linear models can exceed physical bounds for large perturbations).

**EX023 — Parameter-order trap.** Correct call `triangular(4, 12, 8)`: mean (4 + 8 + 12) / 3 = 8.0. Mistaken call `triangular(4, 8, 12)` passes high = 8 and mode = 12; CPython computes *c* = (12 − 4)/(8 − 4) = 2 and returns 4 + 4·√(2*u*), so values range from 4 to about 9.66 and the mean is about 7.77 (a seeded run of 100,000 draws gave minimum 4.02, maximum 9.66, mean 7.77). The output is not a triangular distribution and exceeds the documented "high" of 8 while never reaching 12. A mean check alone (7.77 versus 8.0) is easily dismissed as noise; a range check against the documented bounds and a histogram reveal the error immediately.

**EX024 — Invariant tests.** Example assertions using Lab 5: (1) with every buffer set above 72 h, every policy's loss is 0; (2) `evaluate` with identical orders gives identical results; (3) ORACLE ≤ each policy on each draw; (4) increasing one service's buffer by 1 h never increases loss on fixed draws; (5) with equal durations, SILO's customer-hours ≤ every permutation's. Removing the restart lag for one service is *not* caught by any of these invariants — it lowers all policies' losses consistently. It is caught by a **unit test** on a single service: feeder restored at 5 h, buffer 2 h → expected outage interval (2, 6). Full credit draws the lesson: invariants test structure, unit tests test semantics; you need both.

**EX025 — Latency-relative detection metric.** Definition: for each anomalous segment *k* with start *s_k*, first alarm *a_k* (the first flagged index in the segment) and time-to-impact *T_k*, the segment is "detected before impact" if *a_k* exists and (*a_k* − *s_k*) × Δ*t* < *T_k*. With Δ*t* = 6 min and *T* = 2 h (20 steps): segment 1 first alarm at offset 21 steps (2.1 h) → no; segment 2 at offset 0 → yes; segment 3 at offset 29 steps (2.9 h) → no. Fraction detected before impact = 1/3. Contrast: PA-F1 0.911, point-wise F1 0.05, PA%K 0.05. The latency metric shows that a detector with no information beats the buffer only by chance — information that PA-F1 hides entirely.

**EX026 — Pilot plan.** A strong plan lists feasibility questions (recruitment rate, comprehension of materials, session length, data capture, runtime, invariant tests), sets thresholds as in §4.7.2, specifies no-go responses (revise and re-pilot; change recruitment route; reduce scope), excludes pilot participants from the main study because they have seen the materials and their choices would be contaminated, and states explicitly that no effect size will be estimated or reported as evidence.

### Chapter 5: EX027–EX032

**EX027 — Run and interpret the main study.** The exact output is printed in §5.2.1. Relative change of DEP versus CRITFLAG: Riverbend 4.32 / 3.97 − 1 = +8.8% (DEP slightly worse); Port Halvard 9.61 / 31.63 − 1 = −69.6%. Model paragraph: "Relative to customer-first ordering, both criticality-aware orderings reduced weighted critical-service loss by more than 80% in both synthetic regions, while increasing customer-hours by 58–71%, which exceeds the predeclared 15% margin (H4a not met). Relative to critical-flag ordering, time-to-impact ordering produced no reduction in Riverbend (mean difference +0.35, 95% Monte Carlo interval −0.23 to 0.97; a 10% reduction is ruled out) and a 70% reduction in Port Halvard, where it matched the oracle; customer-hours rose by 2.3% and 9.9% respectively, within the margin (H4b met). Intervals reflect simulation noise only."

**EX028 — Paired versus unpaired.** Riverbend, 500 draws: SD of DEP losses ≈ 6.36, of CRITFLAG ≈ 4.57, of per-draw differences ≈ 6.79. Unpaired 95% interval for the mean difference ≈ 0.35 ± 1.96 × √((6.36² + 4.57²)/500) ≈ −0.34 to 1.04; paired ≈ −0.24 to 0.95. Pairing helped only modestly. The two policies' losses are weakly positively correlated: on many draws one protects water and the other telecom, so their losses move in different directions. The variance of differences, Var(A) + Var(B) − 2 Cov(A, B), can therefore exceed either policy's variance while remaining below the unpaired sum. Common random numbers are still correct; their precision gain is an empirical matter.

**EX029 — Uncertainty taxonomy.** (a) Monte Carlo — more draws. (b) Parameter — elicitation with uncertainty, verification of inventories, sensitivity analysis. (c) Structural — model extension (travel times), comparison of model structures. (d) Value — alternative weight sets, transparent reporting of verdicts per set, deliberation with stakeholders. (e) Parameter (distribution family) or structural (if the shape reflects a mechanism such as depletion) — test alternative families and report sensitivity.

**EX030 — Tabletop design critique.**

| Threat | Change | Cost |
|---|---|---|
| Demand characteristics (participants guess the "right" answer) | Include filler scenarios where DEP is not optimal; neutral framing | Longer sessions |
| Small sample, three utilities | Recruit across more utilities, stratified by size | Recruitment effort; more agreements |
| No time pressure or fatigue | Timed decisions within a longer exercise; embed in a scheduled utility drill | Realism versus burden; drill owners' consent |
| Recognition of isomorphic scenarios | Vary surface features more; separate sessions by days | Logistics; attrition |
| Display tested only in combination with timing information | Add a third arm: flag list with paths shown but no times | More participants needed |
| Outcome scored in the same model used to design DEP | Score choices also by independent expert panel | Panel time |

**EX031 — Validation evidence matrix.** A strong answer chooses face, historical, extreme-condition, parameter-variability and operational validity; is honest that historical validation of rare cyber events is impossible and substitutes all-cause events with a transfer argument; and identifies the most damaging test — for the Cascade Study, historical validation of buffer timing, because if buffers are systematically wrong, every ordering result changes — and schedules it before the main study.

**EX032 — Transportability memo.** The utility has three critical feeders whose buffer order matches their customer order and one crew. Moderators: divergence zero; crews one; buffers unknown relative to restoration time; map accuracy unknown. Prediction: time-to-impact ordering will produce the same order as the critical list, so the gain is zero. Caveats: if weights or fan-out (one feeder protecting several weighted services) differ, a weight-aware rule might still help — that is outside the tested claim. Data that would change the prediction: corrected buffers (which might change the order), evidence of map errors, or dependencies not on the list.

### Chapter 6: EX033–EX038

**EX033 — Red-team report.** Model objections are those in §6.2, plus, for example, "the 72-hour horizon censors long outages" (test: extend to 120 h and count censored services) and "triangular distributions understate tails" (test: lognormal buffers with equal medians). Each objection states its prediction before testing; for example, "if circularity drives the result, a wrong map will remove DEP's advantage over SILO" — Chapter 6 found it reduced DEP's loss advantage over SILO from about 48 to about 7 weighted service-hours, while all criticality-aware policies degraded.

**EX034 — Weight sensitivity.** With all weights set to 1.0 (500 draws, seed 7): Riverbend SILO 15.00, CRITFLAG 1.32, DEP 1.07, ORACLE 0.54; DEP − CRITFLAG −0.25 (95% Monte Carlo interval −0.41 to −0.08). Port Halvard SILO 14.95, CRITFLAG 8.61, DEP 2.49, ORACLE 2.49; DEP − CRITFLAG −6.12 (−6.24 to −6.00). Verdicts: H1 unchanged (supported); H2 in Riverbend changes from *rejected* to *inconclusive* under the preregistered rule — the point estimate is a 19% reduction, but the interval's upper end (−0.08) does not lie wholly below the threshold (−0.13); H2 in Port Halvard unchanged (supported); H4 unaffected (customer-hours do not depend on weights). Explanation: with predeclared weights, F3 first protects two heavily weighted services (water 4 and the hospital via water 5), which favours CRITFLAG's order; with equal weights, restoring telecom early matters relatively more and DEP's earliest-time-to-impact rule gains. Conclusion: the Riverbend verdict depends on values; the thesis must report verdicts by weight set.

**EX035 — Map-error experiment.** Telecom truly on F4, planners believe F2 (300 draws, seed 7, no oracle): SILO 29.01, CRITFLAG 26.82, DEP 31.11. With a correct map, CRITFLAG and DEP both choose F4, F3, F2, F1 and reach 4.90. Compared with the water mismatch (§6.3.1), the telecom error hurts DEP even more: DEP becomes the worst of the three policies, because it confidently restores F2 first for a telecom office that is not there. Audit procedure: for every listed critical facility, sample-based field verification of the feeding feeder each year and after any network reconfiguration; target ≥ 98% accuracy on a random sample of at least 50 facility–feeder pairs (or all, if fewer); owner sign-off; discrepancies corrected within 30 days; audit results stored at controlled tier.

**EX036 — Generator critique.** Implementing "larger feeders host longer-buffer services" (assign sorted buffer levels to critical feeders sorted by customers, smallest buffer to smallest feeder; 200 regions, seed 2026): no-divergence regions fall from 69 to 9; two-position divergence 77 regions, mean gain −24.85; three-position divergence 114 regions, mean gain −19.02. The opposite correlation (shortest buffer on the largest feeder) gives 162 regions with no divergence, 35 with two positions (mean gain −8.65) and 3 with three (−17.24). Interpretation: the generator's correlation assumption, not the method, controls how often DEP helps. The claim must remain conditional on measured divergence, and the frequency in real regions must be measured, not simulated.

**EX037 — Dual-use decision.** (a) *Restrict and notify*: specific, actionable, high uplift — coordinated disclosure through the vendor and a coordinator; notify the affected utilities through appropriate channels; publish only aggregate findings after remediation. (b) *Publish*: general pattern widely discussed in public advisories; defensive value high. (c) *Publish with care*: the method helps planners; avoid releasing ready-made pipelines that ingest public facility data for named places. (d) *Withhold or restrict*: named-hospital estimates are targeting data with little defensive value beyond those hospitals; share privately with them if accurate.

**EX038 — Response letter.** Model responses: (1) circularity — *partly accepted*; mismatch tests added, claim made conditional on map accuracy, map audit recommended. (2) Short buffers — *accepted as a boundary condition*; buffer scaling added, claim limited to buffers shorter than about twice restoration time. (3) Context selection — *partly accepted*; 200-region analysis added, claim limited to measured divergence, frequency in real regions listed as unknown. (4) Heuristic weakness — *accepted*; weight-aware rule presented as exploratory future work, not as a result. (5) Dual use — *accepted*; dual-use review added; restoration-priority data recommendation published at a general level after coordination. Each response cites the section changed.

### Chapter 7: EX039–EX044

**EX039 — Argument map.** Claim, data, warrant, backing, qualifier and rebuttals as in §7.1, with chapters: data (Chapters 5–6), warrant (Chapter 4 verification and Chapter 5 validation), backing (Chapter 4 reproductions and tests), qualifier (Chapter 3 scope plus Chapter 6 conditions), rebuttals (Chapter 6 and Limitations). Weakest warrant: that the model ranks orderings adequately for *real* regions, since historical validation covers one all-cause event and omits human buffers. Strengthening: validation of buffer timing against several after-action records, with human buffers modelled explicitly.

**EX040 — Tier assignment.** Simulator code T0; verification tests T0; Riverbend configuration T0 (invented); elicitation forms with partner names T3 (or T2 if partners consent to controlled access) — transform by stripping identities and aggregating to T1; aggregated elicitation ranges T1 (T0 if partners agree and no unique structure remains); tabletop audio T2 — destroy after transcription if consent says so; coded rationales T2, or T1 after de-identification and removal of role-plus-utility combinations; consent forms T2 (administrative, never released); partner restoration procedure T3 — describe its existence and role only; final figures T0.

**EX041 — Fail-closed manifest.** With the original rule order, `data/synthetic_partner_feeders.csv` matches `partner_` first and is classified T3 (correct). Moving the `synthetic_` rule first classifies it as T0-public (wrong) — an ordering hazard. A content check: before assigning T0, read the bytes and refuse T0 if `b"SUB-"` (or any pattern from a list of asset-identifier formats) occurs, returning "UNCLASSIFIED: stop and review". Lesson: put the most restrictive rules first, fail closed on no match, and check content as well as names.

**EX042 — Residual disclosure assessment.** Risk: the configuration (one hospital, two water plants, five feeders, hospital on a particular feeder) is a near-unique structural fingerprint of the county; someone with local knowledge could match it. A match would reveal which feeder serves the hospital and the elicited buffers — targeting information. Transformations: mix structures from several counties; generalize to ranges; drop the feeder–hospital link and replace it with a randomized assignment preserving only the statistic of interest (for example, the distribution of divergence). Cost: weaker link to the real case; the thesis must state which results depend on preserved structure.

**EX043 — Model documentation.** Purpose: rank restoration orderings by weighted critical-service loss and customer-hours in distribution outages requiring manual sequential restoration. Entities: feeders (customers, restoration duration), services (feeder, buffer, weight, optional dependency with on-site buffer), crews. Processes and scheduling: crews take feeders in policy order as soon as free; service outage intervals computed exactly from buffer expiry to restoration plus a one-hour restart lag; dependency intervals start at the supplier's outage start plus on-site buffer and end with the supplier's restoration; intervals clipped to 72 h; dependencies have OR semantics. Inputs: triangular distributions from elicitation; weights from the emergency-management panel. Verification: the invariants and unit tests of EX024. Limitations: no travel time; no human buffer extension; OR semantics only; fixed buffers (no depletion dynamics); single scenario class.

**EX044 — Limitations section.** A strong answer resembles §7.7, with five or more limitations each given effect, direction and resolving study, and ranks them: (1) human buffers omitted (could reduce all reordering benefits), (2) synthetic regions (frequency of divergence unknown), (3) weights (verdicts change), (4) travel time (reduces DEP benefit where critical feeders are dispersed), (5) tabletop scale (adoption unproven).

### Chapter 8: EX045–EX050

**EX045 — Claim audit.** The original output flags K2, K3 and K4 (see §8.1.1). K5 is reported "OK" because none of the keywords appear. Improved check: extend `OVERREACH` with phrases such as "the grid", "resilient to", "makes", "secure", or better, require an explicit scope phrase ("in the synthetic…") in the text of any claim whose scope field contains "synthetic". Corrected K5: "In two synthetic regions, time-to-impact restoration ordering reduced modelled critical-service loss after distribution outages under stated conditions; it does not prevent cyber attacks, and its effect on real grids is untested."

**EX046 — Examiner question bank.** Hardest three for the Cascade Study, with model answers: (1) "Isn't the result circular?" — answer with the mismatch and independent-modeller evidence and admit what remains circular (ORACLE and DEP still share the model). (2) "Why should anyone accept your weights?" — they shouldn't without scrutiny; describe elicitation and the verdict-by-weight-set table; weights are a policy input that the method makes explicit. (3) "Without a field study, what do you know about real utilities?" — that the conditions for benefit are measurable; that the divergence survey is the next study; that no field claim is made. A real gap revealed: the thesis has no evidence on whether crews can follow a reordered plan given travel times — a gap in the work, to be stated as a limitation.

**EX047 — Publication plan.** As in §8.3.1, with: the T0 archive v1.0 released with paper 1; papers 2–4 citing archive versions; the dual-use review and sector coordination completed before any preprint of paper 2; partner notice periods respected for papers using elicitation ranges; and a statement in each paper of its scope relative to the thesis's overall claim.

**EX048 — Disclosure routing.**

| Finding | Kind | Route and timing | Published |
|---|---|---|---|
| (a) Partner exposes its critical-customer list | Organization-specific | Immediate private report under the data-use agreement; confirm fix | Never in identifiable form; possibly a general note that priority lists need access control |
| (b) Unsigned configuration imports in a commercial product | Product vulnerability | CVD with the vendor, directly or via a coordinator; publication after remediation or under the coordinator's policy | Advisory-level description after coordination |
| (c) Paper versus physical buffer inventories | Organization-specific and sector-level | Private reports to each partner; then general publication of the gap | Aggregate finding without identities |
| (d) Single repeater site for crew radios | Organization-specific with sector relevance | Private report to the utility; general finding on single points of failure in restoration communications after coordination | General finding only |

**EX049 — Policy brief.** A strong brief opens with the problem (restoration order determines which critical services fail), states four recommendations with confidence levels and evidence links (§8.5), includes a paragraph "What this research does not show" (effects in real utilities, frequency of divergence, adoption under stress, any cyber-prevention effect), uses plain language, and links to the thesis and the T0 archive. Every sentence is marked; sentences that cannot be traced to the thesis are removed.

**EX050 — Post-doctoral research program.** As in §8.6: (1) divergence survey — claim "divergence occurs in at least a quarter of surveyed utilities", design under T3 protection, partner model via sector associations, decision changed: whether to promote time-to-impact ordering at all; (2) human-buffer modelling — claim "including fuel and water deliveries reduces the modelled benefit of reordering by less than half", validated against after-action records; (3) integrity attacks on planning data — claim "map audits at 98% accuracy limit the consequence amplification of corrupted priority data to a stated bound". Order: (1) first, because if divergence is rare, (2) and (3) matter more than further method work. Stopping result: if the survey finds divergence in very few utilities and map errors are rare, the program should pivot from ordering methods to buffer verification.

<a id="glossary"></a>

## Glossary

- **Buffer** — Stored capacity (fuel, batteries, water storage, inventory, manual procedures) that lets a dependant keep operating after losing a supplier, for a duration that depends on load.
- **Censoring** — Incomplete observation of a duration because the observation window closed before the event (for example, recovery) occurred.
- **Common random numbers** — Evaluating every compared policy on the same simulated draws so that comparisons are paired.
- **Consequence** — The effect of a disruption on people and the functions they rely on, measured in service units over a time window.
- **Critical-flag ordering (CRITFLAG)** — In this book, restoring feeders that host listed critical facilities first, ordered among themselves by customers served.
- **Critical function** — A function of government or the private sector whose disruption would have a debilitating effect on security, the economy, public health or safety; CISA's National Critical Functions set lists 55.
- **Critical service** — A service whose interruption beyond a stated duration harms health, safety, security or essential economic activity for a stated population.
- **Customer-first ordering (SILO)** — In this book, restoring feeders in decreasing order of customers served; optimal for customer-hours under equal durations (Smith's rule).
- **Dependency / interdependency** — A one-directional / bidirectional relation in which a service's state depends on another's (Rinaldi, Peerenboom and Kelly, 2001).
- **Divergence** — The number of positions in which two restoration orders differ among critical feeders; in this book, the moderator of DEP's advantage over CRITFLAG.
- **Dual-use review** — Assessment of a research result's uplift to adversaries, defensive value and possible mitigations before publication.
- **Dependency-aware ordering (DEP)** — In this book, restoring feeders in increasing order of the earliest expected time-to-impact of the critical services they support.
- **Inoperability input–output model (IIM)** — A Leontief-based linear model of equilibrium inoperability propagation between sectors (Haimes and Jiang, 2001).
- **Model–policy circularity** — Evaluating a policy in the same model from which it was derived, so that model errors cannot show up as policy failures.
- **Non-inferiority margin** — The largest worsening of a secondary or safety metric accepted in exchange for a benefit on the primary metric, fixed in advance.
- **Oracle ordering** — The best ordering for a given draw, found by exhaustive enumeration; an upper bound on what any rule could achieve.
- **Performance curve** — The fraction of normal service delivered over time before, during and after a disruption.
- **Point adjustment (PA)** — An evaluation protocol that counts a whole anomalous segment as detected if any point in it is flagged; known to inflate scores (Kim et al., 2022).
- **Release tier** — The access level (public, registered, controlled, withheld) at which an archive artifact is made available.
- **Reproduction / replication** — Obtaining consistent results with the same data and methods / with new data addressing the same question (National Academies, 2019).
- **Resilience loss** — The area between full service and the performance curve over a window.
- **Smallest effect of interest** — The smallest effect that would change a real decision, justified by practical consequence and fixed before analysis.
- **Target security level (SL-T)** — In IEC 62443-3-2, the desired security level for a zone or conduit, determined through risk assessment.
- **Time-to-impact** — The time after an initiating failure at which a dependent service fails, computed over all dependency paths.
- **Verification / validation** — Showing that a model is implemented correctly / that it is adequate for its intended purpose (Sargent, 2013).
- **Zones and conduits** — In IEC 62443, groupings of assets with common security requirements and of the communication channels between them.

<a id="references"></a>

## References

Standards, regulations and policy instruments change. Versions and dates below are those consulted for this draft (October 2026); re-verify before relying on them.

**Policy, law and standards**

- Bank for International Settlements, Committee on Payments and Market Infrastructures, and International Organization of Securities Commissions. [Guidance on Cyber Resilience for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d146.htm). June 2016.
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set). April 2019.
- Cybersecurity and Infrastructure Security Agency. [National Security Memorandum on Critical Infrastructure Security and Resilience (overview)](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Congressional Research Service. [The 2024 National Security Memorandum on Critical Infrastructure Security and Resilience](https://www.congress.gov/crs-product/IF12716). IF12716.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- Federal Energy Regulatory Commission. [Critical Infrastructure Protection Reliability Standard CIP-015-1 — Cyber Security — Internal Network Security Monitoring](https://www.federalregister.gov/documents/2025/07/02/2025-12309/critical-infrastructure-protection-reliability-standard-cip-015-1-cyber-security-internal-network). Order No. 907, *Federal Register*, 2 July 2025.
- International Electrotechnical Commission. [IEC 62443-3-2:2020, Security for industrial automation and control systems — Part 3-2: Security risk assessment for system design](https://webstore.iec.ch/en/publication/30727).
- Inside Privacy (Covington & Burling). [CISA Submits Final CIRCIA Rule for OMB Review](https://www.insideprivacy.com/critical-infrastructure/cisa-submits-final-circia-rule-for-omb-review/). October 2026. (Secondary source on regulatory status.)
- NERC. [CIP-015-1 standard page](https://www.nerc.com/standards/reliability-standards/cip/cip-015-1).
- NIST. [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29). NIST CSWP 29, February 2024.
- NIST. Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST SP 800-160 Vol. 2 Rev. 1, December 2021.
- NIST. Stouffer, K., Pease, M., Tang, C., Zimmerman, T., Pillitteri, V., Lightman, S., Hahn, A., Saravia, S., Sherule, A., and Thompson, M. [Guide to Operational Technology (OT) Security](https://doi.org/10.6028/NIST.SP.800-82r3). NIST SP 800-82 Rev. 3, September 2023. [CSRC page with Rev. 4 draft note](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- The White House. [National Security Memorandum on Critical Infrastructure Security and Resilience (NSM-22)](https://www.govinfo.gov/content/pkg/DCPD-202400358/html/DCPD-202400358.htm). 30 April 2024.

**Incident and threat reports**

- CISA. [CrashOverride Malware (TA17-163A)](https://www.cisa.gov/news-events/alerts/2017/06/12/crashoverride-malware). June 2017.
- CISA. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf).
- CISA and partners. [PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a). February 2024.
- E-ISAC and SANS ICS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). 18 March 2016 (archived copy at the National Security Archive).
- Langner, R. [To Kill a Centrifuge: A Technical Analysis of What Stuxnet's Creators Tried to Achieve](https://archive.org/details/to-kill-a-centrifuge). The Langner Group, November 2013 (Internet Archive copy).

**Infrastructure, resilience and modelling**

- Bochman, A. A., and Freeman, S. [Countering Cyber Sabotage: Introducing Consequence-Driven, Cyber-Informed Engineering (CCE)](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710). CRC Press, 2021.
- Bruneau, M., Chang, S. E., Eguchi, R. T., Lee, G. C., O'Rourke, T. D., Reinhorn, A. M., Shinozuka, M., Tierney, K., Wallace, W. A., and von Winterfeldt, D. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra* 19(4), 2003.
- Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., and Havlin, S. [Catastrophic Cascade of Failures in Interdependent Networks](https://doi.org/10.1038/nature08932). *Nature* 464, 2010.
- Goh, J., Adepu, S., Junejo, K. N., and Mathur, A. [A Dataset to Support Research in the Design of Secure Water Treatment Systems](https://doi.org/10.1007/978-3-319-71368-7_8). CRITIS 2016, LNCS 10242.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis* 29(4), 2009.
- Haimes, Y. Y., and Jiang, P. [Leontief-Based Model of Risk in Complex Interconnected Infrastructures](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1)). *Journal of Infrastructure Systems* 7(1), 2001.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- Lenstra, J. K., Rinnooy Kan, A. H. G., and Brucker, P. [Complexity of Machine Scheduling Problems](https://doi.org/10.1016/S0167-5060(08)70743-X). *Annals of Discrete Mathematics* 1, 1977.
- Neprash, H. T., McGlave, C. C., et al. [Trends in Ransomware Attacks on US Hospitals, Clinics, and Other Health Care Delivery Organizations, 2016–2021](https://doi.org/10.1001/jamahealthforum.2022.4873). *JAMA Health Forum* 3(12), 2022.
- Ouyang, M. [Review on Modeling and Simulation of Interdependent Critical Infrastructure Systems](https://doi.org/10.1016/j.ress.2013.06.040). *Reliability Engineering & System Safety* 121, 2014.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine* 21(6), 2001.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation* 7(1), 2013.
- Smith, W. E. [Various Optimizers for Single-Stage Production](https://doi.org/10.1002/nav.3800030106). *Naval Research Logistics Quarterly* 3(1–2), 1956.
- Taormina, R., et al. [Battle of the Attack Detection Algorithms: Disclosing Cyber Attacks on Water Distribution Networks](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969). *Journal of Water Resources Planning and Management* 144(8), 2018.

**Research methods, evaluation and integrity**

- Arp, D., Quiring, E., Pendlebury, F., Warnecke, A., Pierazzi, F., Wressnegger, C., Cavallaro, L., and Rieck, K. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). USENIX Security Symposium, 2022.
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- Gebru, T., Morgenstern, J., Vecchione, B., Wortman Vaughan, J., Wallach, H., Daumé III, H., and Crawford, K. [Datasheets for Datasets](https://doi.org/10.1145/3458723). *Communications of the ACM* 64(12), 2021.
- Grimm, V., et al. [A Standard Protocol for Describing Individual-Based and Agent-Based Models](https://doi.org/10.1016/j.ecolmodel.2006.04.023). *Ecological Modelling* 198(1–2), 2006.
- Kerr, N. L. [HARKing: Hypothesizing After the Results Are Known](https://doi.org/10.1207/s15327957pspr0203_4). *Personality and Social Psychology Review*, 1998.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *Proceedings of the AAAI Conference on Artificial Intelligence* 36(7), 2022.
- Leon, A. C., Davis, L. L., and Kraemer, H. C. [The Role and Interpretation of Pilot Studies in Clinical Research](https://doi.org/10.1016/j.jpsychires.2010.10.008). *Journal of Psychiatric Research* 45(5), 2011.
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. [Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596). FAT* 2019.
- National Academies of Sciences, Engineering, and Medicine. [Reproducibility and Replicability in Science](https://doi.org/10.17226/25303). 2019.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *PNAS*, 2018.
- O'Hagan, A., Buck, C. E., Daneshkhah, A., Eiser, J. R., Garthwaite, P. H., Jenkinson, D. J., Oakley, J. E., and Rakow, T. [Uncertain Judgements: Eliciting Experts' Probabilities](https://doi.org/10.1002/0470033312). Wiley, 2006.
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. [The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews](https://doi.org/10.1136/bmj.n71). *BMJ*, 2021.
- Pearl, J., and Bareinboim, E. [External Validity: From Do-Calculus to Transportability Across Populations](https://doi.org/10.1214/14-STS486). *Statistical Science* 29(4), 2014.
- Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D., Saisana, M., and Tarantola, S. [Global Sensitivity Analysis: The Primer](https://doi.org/10.1002/9780470725184). Wiley, 2008.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology* 9(10), 2013.
- Simmons, J. P., Nelson, L. D., and Simonsohn, U. [False-Positive Psychology](https://doi.org/10.1177/0956797611417632). *Psychological Science*, 2011.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). IEEE Symposium on Security and Privacy, 2010.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. [The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18). *Scientific Data*, 2016.

Companion CyberABC material: the [doctoral Incident Response book](../../../incident-response-resilience/en/book/MANUSCRIPT.md) (claim ladder and research-integrity methods reused in Chapter 1) and the [doctoral OT, IoT and cyber-physical security course](../../../ot-iot-security/README.md) (control-system layer).

**Case boundary.** The Riverbend Region, Port Halvard, Riverbend Electric Cooperative, Riverbend Water Authority, St. Calder Hospital, Meridian Telecom, GridWater-Sim, studies P1–P8, participants P01–P12, the Cascade Study and every number produced by the labs are invented for teaching. Sources support the general statements beside which they are cited, never the synthetic details.

**Edition metadata.** Draft edition, October 2026. Reviewer: pending. A4 release verification: pending; a preliminary layout preflight is recorded in [the progress review](../../../../../STRUCTURE_REVIEW.md#a4-preflight).
