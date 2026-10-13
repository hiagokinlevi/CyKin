# Critical Infrastructure and Sector Security: Coordination, Governance and Exercises for Practitioners

- Language: English (`en`); professional course, six months; approximately 360 hours of planned study (course 046 of 207 in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **draft**. Chapters 1–12 of 12 have authored teaching text, five offline labs, exercises EX001–EX060 and matching worked results. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: entry-level practitioners who will **coordinate** security in an organization that runs an essential service — newly appointed security or resilience coordinators, operations supervisors who have inherited cyber duties, risk and compliance officers, continuity planners and project managers in water, energy, healthcare, transport, finance and public services. Entry knowledge: security basics and a working understanding of how the relevant service is delivered.
- How this course differs from its neighbours. The [technical book](../../../../technical-18-months/critical-sector-security/en/book/MANUSCRIPT.md) teaches hands-on depth: decoding protocols, hardening hosts, configuring firewalls. The [technologist book](../../../../technologist-3-years/critical-sector-security/en/book/MANUSCRIPT.md) teaches implementers to build and hand over a monitored service. The [rapid book](../../../../rapid-1-month/critical-sector-security/en/book/MANUSCRIPT.md) is a first introduction. **This professional book is about coordination and governance**: who decides, who is told, who is accountable, how risk is ranked and accepted, how suppliers are held to account, how a tabletop exercise is designed and evaluated, and how all of this is shown to a board or regulator with evidence. You will not configure anything in this book. You will learn to ask the questions that make sure the right people configure the right things, in the right order, and can prove it.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights and are not relicensed here.
- Educational boundary: this course is an independent educational blueprint. It is not an accredited programme, grants no qualification and grants no authority over, or access to, any real infrastructure, operator, dataset or person. Every organization, place, person, contract, deadline, log line and number in a worked example or lab is **synthetic** unless a sentence explicitly cites a public source. The "Kestrel Vale" notification deadlines are illustrative: real duties come from your own law, regulator, licence and contracts. Nothing in this book is legal, clinical or regulatory advice.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

The twelve chapters follow one newly appointed **cyber-resilience coordinator** through six months at a mid-sized water utility. The course outcome is to **operate a repeatable coordination workflow and communicate findings** about critical-infrastructure security, under supervision.

- **Months 1–2 (Chapters 1–4)** build the foundation: what a coordinator is for, the service and its stakeholders, authorized work and decision records, and a consequence-led risk register.
- **Months 3–4 (Chapters 5–8)** turn that into a working programme: frameworks and assessments read critically, roles and a RACI, controls owned and verified with evidence, and a supervised supplier-access case.
- **Months 5–6 (Chapters 9–12)** test and present it: notification and crisis communication, finding and fixing failures in the programme itself, a full tabletop exercise, and a final portfolio with a board briefing.

Every chapter has learning outcomes, teaching sections with definitions, a worked example, a practical activity, common errors and limits, five numbered exercises and a synthesis. Five chapters contain a short Python lab. The labs are not programming lessons: each is a checklist made executable, so you can see exactly which rule flags which record and argue with the rule. They use the Python 3 standard library only (outputs in this draft were produced with Python 3.13.5), need no network, packages, privileges or real data, and every output is printed in the text. You can complete every exercise without running code by reading the printed output. Write your answer to each exercise before opening the [worked results](#worked-results); the 0–3 rubric shows what an assessor rewards, and a different defensible answer can earn full credit.

Keep four labels in every coordination note: **decided** (what was decided, by whom, when, on what basis), **assumed** (what the decision relies on that nobody has checked), **owed** (what someone has promised, to whom, by when) and **open** (what is unknown, and who is finding out).

### The synthetic setting used in this book

| Synthetic element | Role in the book | Boundary |
|---|---|---|
| **Kestrel Vale** — a fictional region with its own fictional regulator and national CSIRT | Setting for all examples. | Invented place and law. |
| **Kestrel Water** — drinking-water utility, 180,000 people, treatment works KW-TW and pumping/dosing stations KW-01 to KW-12 | The reader's employer. The reader is the **cyber-resilience coordinator**, reporting to the chief operating officer. | Invented. |
| People: A. Mensah (operations manager), L. Ferreira (security lead, part-time from the IT department), J. Tan (control-systems engineer), C. Okafor (customer services and billing), R. Adeyemi (communications), M. Holt (chief executive), E. Varga (chief operating officer), T. Lindqvist (board audit and risk committee chair) | Colleagues. | Invented; no real person. |
| **Kestrel Vale Regional Operations Centre (KVROC)** | Shared monitoring service used by the utility. | Invented. |
| **Kestrel Grid**, **Kestrel General Hospital** | Power supplier and the most critical customer. | Invented. |
| Suppliers HydroLogic Ltd, ScadaCo, Vale Pumps, MeterWorks, Northgate Integration | Third parties in Chapters 8–11. | Invented; any resemblance to real firms is accidental. |

Because the data are synthetic, the book can tell you what a real coordinator rarely knows for certain. Use that to learn how programmes fail, never as evidence about real organizations.

### Source policy

Every factual statement about a framework, law, standard, public incident or published guidance links to a source consulted in October 2026. Standards, guidance and laws change and differ between jurisdictions: re-verify each before relying on it. Ordinary management vocabulary (RACI, risk owner, holding statement) is not given an invented reference. A citation supports the general claim beside it, never the synthetic details. Public incidents are described only at the level their publishers released.

### Professional rules for coordination work

1. You coordinate; you do not authorize yourself. Every assessment, test, supplier session or change needs the approval of the person who owns the affected service (Chapter 3).
2. Operations has the last word on physical safety. A security recommendation that could affect treatment, pressure or dosing goes through the operations manager, every time.
3. Never ask anyone to "just check" a live control system without that approval, and never forward credentials, network diagrams or register maps by ordinary email or chat.
4. Report what you know, label what you assume, and correct promptly what you got wrong (Chapter 9).
5. Treat people as the system's strength. Exercises test plans, not individuals (Chapter 11).

## Contents

1. [Security foundations for practitioners](#ch-01) — essential services, consequence, the coordinator's job and the language of risk.
2. [Service and stakeholder context](#ch-02) — critical functions, dependencies and the people who must be in the room.
3. [Authorized practice and evidence handling](#ch-03) — who may authorize what, decision records and information sharing.
4. [Core methods](#ch-04) — a consequence-led risk register, ownership and acceptance. Lab 4.
5. [Tools and interpretation](#ch-05) — frameworks, assessments, maturity scores and metrics read critically.
6. [Operational workflow](#ch-06) — roles, a RACI, IT/OT change governance and escalation. Lab 6.
7. [Controls and verification](#ch-07) — control ownership, assurance levels and time-limited exceptions.
8. [Supervised case analysis](#ch-08) — a supplier remote-access case and third-party governance. Lab 8.
9. [Communication, ethics and reporting](#ch-09) — notification clocks, critical customers, holding statements and honesty. Lab 9.
10. [Quality and troubleshooting](#ch-10) — diagnosing a coordination programme that is not working. Lab 10.
11. [Supervised laboratory](#ch-11) — designing, running and evaluating a tabletop exercise.
12. [Practice portfolio and final review](#ch-12) — portfolio, board briefing and a 90-day plan.

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes and connection

After this chapter you should be able to:

- explain what makes a service "essential" and why its security is judged by **consequence** to people, not by damage to computers;
- describe the coordinator's job and distinguish it from the engineer's, the security analyst's and the executive's;
- use the core vocabulary of risk — asset, threat, vulnerability, likelihood, consequence, risk owner, risk appetite — precisely enough that colleagues can act on your sentences;
- place your work inside a recognised framework (the six functions of the NIST Cybersecurity Framework 2.0) without mistaking the framework for the work.

This chapter assumes only security basics. Everything later in the book builds on the distinctions made here.

### 1.1 What an essential service is

An **essential service** is one whose interruption harms people, the economy or public order quickly and at scale: drinking water, electricity, healthcare, transport, payments, emergency communications. Governments list them differently. The United States groups sixteen critical infrastructure sectors ([CISA, Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors)) and describes the underlying **national critical functions** — for example "supply water" or "provide medical care" — that cut across sectors ([CISA, National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set)). The European Union's NIS2 Directive names sectors of "high criticality" and places duties on essential and important entities, including on their management bodies ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)).

The useful idea in all these lists is the same: the thing to protect is a **function delivered to people**, not a building or a server. Kestrel Water does not exist to run computers; it exists so that 180,000 people can drink safe water at adequate pressure every hour of every day. Its computers matter to the extent that the function depends on them.

### 1.2 Consequence first

In an office, the classic security triad is often recited as confidentiality, integrity and availability, in that order. In an essential service the order of concern usually changes. NIST's guide to operational technology security notes that OT systems directly affect the physical world and that their priorities — human safety, availability and integrity of control — differ from typical IT priorities ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).

For a coordinator this has a practical meaning. When you rank a problem, ask in this order:

1. **Could it hurt someone?** (wrong chemical dose, loss of pressure to a hospital, a worker exposed to a moving pump);
2. **Could it stop the service, and for how long, for how many people?**
3. **Could it make the service untrustworthy** — operators no longer sure the screens show the truth?
4. **Could it expose information** — customer data, network designs, vulnerability reports?

A data breach of the billing system is serious and may carry legal duties, but a silent change to a chlorine setpoint is a different category of problem. A coordinator who cannot explain that difference in one sentence to a board will see money go to the wrong place.

### 1.3 The coordinator's job

Kestrel Water's chief operating officer, E. Varga, wrote the role description for the new post. Its core is three verbs: **connect**, **decide-enable** and **evidence**.

- **Connect.** Operations, IT, engineering, customer services, communications, suppliers and the executive all hold part of the picture. The coordinator makes sure the parts meet: the right people know about a risk, a change or an incident in time.
- **Decide-enable.** The coordinator rarely makes the important decisions. The operations manager decides whether to run a station manually; the chief executive decides what to tell the public. The coordinator makes sure the decision has an owner, the information it needs, a deadline, and a record.
- **Evidence.** The coordinator can show, to a board, auditor or regulator, what was decided, why, and whether it was done.

The coordinator is **not** the engineer who reconfigures the firewall, the analyst who reads the logs, or the executive who accepts the risk. Confusing these roles is the most common failure of new coordinators: they either try to do the technical work themselves (and lose sight of the programme) or make decisions that belong to someone with authority over the service (and are later overruled or blamed).

### 1.4 The vocabulary of risk

Precise words save hours in meetings. The following definitions follow common usage in [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), simplified for practice:

- **Asset** — anything the service depends on: equipment, software, data, people, suppliers, buildings.
- **Threat** — a circumstance or actor with the potential to cause harm (a criminal group, a careless update, a flood).
- **Vulnerability** — a weakness a threat could exploit (a supplier account without multi-factor authentication).
- **Likelihood** — how probable it is that the harm happens in a given period, given the controls that exist.
- **Consequence** (or impact) — what happens to the service and to people if it does.
- **Risk** — the combination: a statement of what could happen, how, how likely and how bad.
- **Risk owner** — the person with authority and budget to decide how the risk is treated. Usually a manager of the affected service, not the coordinator.
- **Risk appetite** — how much risk the organization's leadership is willing to accept in pursuit of its objectives, stated in advance.
- **Treatment** — reduce, avoid, transfer (for example insurance or a contract) or accept the risk.

A well-formed risk statement has a cause, an event and a consequence: "*Because* the pump supplier's remote account has no second factor, *an attacker with the supplier's password could* log in to station controllers *and change pump setpoints, causing* loss of pressure to up to 20,000 customers including the hospital." Compare "vendor access risk", which nobody can own or treat.

### 1.5 Frameworks as maps

The NIST Cybersecurity Framework 2.0 organises outcomes into six functions: **Govern, Identify, Protect, Detect, Respond and Recover** ([NIST CSWP 29, The NIST Cybersecurity Framework 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)). Version 2.0 added Govern, which covers strategy, roles, policy, risk management and supply-chain risk — most of what this book is about. The UK's Cyber Assessment Framework, written for operators of essential services, is organised around objectives such as managing security risk and minimising the impact of incidents ([NCSC, Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf)).

A framework is a map of outcomes. It tells you what a good programme achieves, not how your utility should achieve it, and certainly not that you have achieved it. Chapter 5 shows how to read framework-based assessments without being fooled by them.

### 1.6 Worked example: the first week (synthetic)

On her first day the new coordinator receives three requests:

1. The IT department asks her to "sign off" a new antivirus product for the control-room computers by Friday.
2. The board audit chair, T. Lindqvist, asks for "our cyber risk score" for next month's committee.
3. The operations manager, A. Mensah, mentions that a pump supplier "sometimes logs in from home" to fix station KW-07.

A weak response treats them as three tasks. A coordinator's response sorts them by consequence and by who owns the decision:

| Request | Consequence question | Whose decision? | Coordinator's action |
|---|---|---|---|
| Antivirus on control-room PCs | Could the product block or slow the operator screens? (NIST SP 800-82 warns that IT tools can disrupt OT) | Operations manager, advised by the control-systems engineer and supplier | Ask J. Tan whether the control-system supplier supports the product; arrange a test on a non-production machine; do **not** sign off alone. |
| Board's "risk score" | What decision will the board take with it? | Board (appetite); executive (treatment) | Offer a short list of the top consequence-ranked risks with owners and dates instead of a single number (Chapter 4). |
| Supplier home logins | Could someone else use that access to change pump settings? | Operations manager owns the station; security lead advises | Record it as a candidate risk with a full cause-event-consequence statement; schedule a supplier-access review (Chapter 8). |

The third item, raised casually, is the most consequential. Coordinators learn to hear risk in conversation.

### 1.7 Practical activity

Pick an essential service you know (your own employer, or a public one described in a news report). Write, in no more than one page: the function it delivers to people; three things it depends on; and one well-formed risk statement with cause, event and consequence. Mark which parts you know and which you assume.

Then hand the page to a colleague and ask them to name the risk owner from your statement alone. If they cannot, the consequence or the affected service is probably too vague. Compare your function with the Kestrel Water sentence about safe water at adequate pressure for 180,000 people: it names who is served and what they need.

### 1.8 Common errors and limits

- Treating "security" as the IT department's property. In an essential service, operations owns the consequence.
- Writing risks as nouns ("ransomware", "insider") instead of statements someone can own.
- Asking for a single risk score. Scores hide which service, which people and which decision.
- Mistaking a framework profile for evidence that controls work.
- This chapter simplifies: real risk methods (Chapter 4) need calibration, data and judgement, and laws differ between countries.

- Signing off a change that belongs to someone else, as the coordinator avoided with the antivirus request for the control-room computers.
- Treating a casual remark, such as a supplier who sometimes logs in from home, as small talk rather than a candidate risk.

### Exercises — chapter 1

**EX001 — Rewrite risks.** *Objective:* produce ownable risk statements. *Inputs:* the register entries "ransomware", "old PCs" and "supplier access". *Steps:* rewrite each as a cause-event-consequence statement set at Kestrel Water. *Expected evidence:* three statements. *Rubric:* 3 = each has a cause, an event and a service consequence measured in people or time, and names the affected function; 2 = one lacks a consequence; 1 = still generic; 0 = none.

**EX002 — Order of concern.** *Objective:* apply consequence-first ranking. *Inputs:* four events: (a) billing database copied by an intruder; (b) operator screens at KW-03 freeze for 40 minutes; (c) chlorine setpoint at KW-05 changed without approval; (d) internal network diagram emailed to a wrong address. *Steps:* rank them and justify. *Expected evidence:* ranking with one sentence each. *Rubric:* 3 = (c) first on safety grounds, (b) second for loss of view and potential loss of control, then (d) and (a) with reasoning about who is harmed and how; notes that legal duties may still make (a) urgent; 2 = correct top two only; 1 = ranks (a) first without reasoning; 0 = none.

**EX003 — Role boundaries.** *Objective:* separate coordination from authority. *Inputs:* the antivirus request in 1.6. *Steps:* write the email you would send to IT and to A. Mensah. *Expected evidence:* two short messages. *Rubric:* 3 = declines sole sign-off, names the decision owner, asks for supplier compatibility, a non-production test and a rollback plan, proposes a date; 2 = correct owner without test request; 1 = signs off; 0 = none.

**EX004 — Map to CSF 2.0.** *Objective:* use a framework as a map. *Inputs:* the three requests in 1.6. *Steps:* assign each to one or more CSF 2.0 functions and explain. *Expected evidence:* three assignments. *Rubric:* 3 = antivirus → Protect (and Govern for decision rights); risk score → Govern; supplier logins → Govern (supply chain) and Identify/Protect; notes that a function label is not evidence; 2 = labels without reasons; 1 = one label; 0 = none.

**EX005 — Hear the risk.** *Objective:* spot risk in conversation. *Inputs:* the remark "the night shift keeps the station door propped open because the badge reader is slow." *Steps:* write a risk statement, name a likely owner and one question you would ask before proposing any fix. *Expected evidence:* statement, owner, question. *Rubric:* 3 = statement links physical access to control equipment and consequence; owner is the station or operations manager; question respects why staff do it (for example, how slow, and is the door needed for emergency exit?); 2 = no question; 1 = blames staff; 0 = none.

### Chapter synthesis

An essential service is a function delivered to people, and its security is measured by consequence: safety, continuity, trustworthiness, then confidentiality. The coordinator connects the people who hold parts of the picture, makes sure decisions have owners and records, and keeps evidence. Precise risk statements and a framework used as a map — not as proof — are the first tools of the job.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Critical infrastructure and sector security: service and stakeholder context

### Learning outcomes and connection

After this chapter you should be able to:

- describe a critical service as a chain of functions and dependencies, upstream and downstream;
- build a stakeholder map that distinguishes who decides, who must be told and who can help;
- recognise how sectors differ — water, energy, healthcare, transport, finance — in what "harm" means and who regulates it;
- identify cascading effects between sectors and the coordination they require.

Chapter 1 defined the service by its consequence. This chapter draws the people and dependencies around it.

### 2.1 A service is a chain

Drinking water at Kestrel Water passes through a chain: abstraction from the river, treatment at KW-TW, chemical dosing, pumping and storage at KW-01 to KW-12, distribution, metering and billing. Each link depends on things the utility does not fully control: electricity from Kestrel Grid, chemicals delivered by road, telecommunications for telemetry, a monitoring service at KVROC, software and maintenance from suppliers, and people with scarce skills.

CISA's national critical functions describe this view at national level: functions such as "supply water" depend on others such as "provide electricity" and "provide internet-based content, information and communication services" ([CISA, National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set)). The coordinator's version is local and concrete: a one-page dependency map that a new manager could read in five minutes.

### 2.2 Upstream, downstream, shared

Three kinds of dependency matter to a coordinator:

- **Upstream** — what the service needs: power, chemicals, communications, suppliers, staff.
- **Downstream** — who needs the service and how badly: households, schools, the hospital's sterilisation unit and dialysis, fire hydrants, food businesses.
- **Shared** — components or people several functions rely on at once: one telecommunications carrier for all telemetry, one supplier engineer who knows every station, one shared monitoring centre.

Shared dependencies are where single events become wide outages. A coordinator's most valuable question in any meeting is often: "*What else uses that?*"

### 2.3 Stakeholders and their roles

A **stakeholder** is anyone who affects, or is affected by, the security of the service. For coordination, classify each by what you need from them:

| Class | Meaning | Kestrel Water examples |
|---|---|---|
| **Decides** | Has authority over the service, budget or public message | Chief executive, chief operating officer, operations manager, board |
| **Does** | Carries out the work | Control-systems engineer, IT, suppliers, KVROC analysts, shift operators |
| **Must be told** | Has a legal, contractual or safety right to know | Regulator and national CSIRT, Kestrel General Hospital, public health authority, insurer |
| **Can help** | Offers capability or information | Sector information-sharing group, national CSIRT, mutual-aid partners, Kestrel Grid's control room |
| **Is affected** | Experiences the consequence | Customers, staff, neighbouring utilities |

One stakeholder can sit in several classes. The hospital "must be told" when water quality or pressure is at risk and is also "affected"; it may also "help" by telling you which of its systems need water most.

### 2.4 How sectors differ

The coordination pattern is common, but the meaning of harm and the regulatory landscape differ:

- **Water**: public health is the dominant consequence; operators often run small sites with few staff; manual operation is frequently possible for a while. CISA and partners have published water-specific advisories after attacks on internet-exposed controllers ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)).
- **Electricity**: real-time balance and cascading failure across networks; outages affect every other sector. The 2015 attacks on Ukrainian distribution companies caused outages for customers and were followed by manual restoration ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01)).
- **Healthcare**: patient safety and clinical continuity; many connected medical devices; clinical staff decide on diversion and downtime procedures.
- **Transport and pipelines**: safety of movement and fuel supply; business systems can force operational shutdowns even when control systems are untouched. In the 2021 DarkSide ransomware case, CISA and the FBI issued an advisory about attacks on a critical-infrastructure company's IT network ([CISA AA21-131A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a)).
- **Finance**: integrity of transactions and public confidence; strong existing regulation of operational resilience.

The professional lesson: when you coordinate across sectors (water with power, hospital with water), translate your consequence into theirs. "Station KW-02 offline" means nothing to the hospital; "lower pressure on the east side from 14:00 to about 18:00, water safe to drink" does.

### 2.5 Worked example: the hospital dependency (synthetic)

Kestrel General Hospital is supplied by the east zone, fed by stations KW-02 and KW-07. The coordinator asks four questions and records the answers:

| Question | Answer (synthetic) | Source |
|---|---|---|
| What does the hospital use water for that cannot wait? | Sterile services, dialysis, kitchens, fire suppression, cooling of the imaging suite | Hospital estates manager, meeting 12 Feb |
| How long can it cope without mains supply? | About 6 hours on stored water for priority uses | Hospital's own business continuity plan (not seen; assumed) |
| Who at the hospital must be called, day and night? | Estates on-call; out of hours, the site duty manager | Hospital switchboard confirmed |
| What does our contract or agreement promise? | A call within 2 hours of any event likely to affect supply or quality | Supply agreement, clause 7 |

The coordinator then marks "6 hours" as **assumed**, because she has not seen the plan. An assumption on which a decision depends is a task: she asks to see the relevant section. This pattern — record source and confidence for every dependency fact — runs through the book.

### 2.6 Practical activity

Draw a dependency map for one essential service with at least five upstream, three downstream and one shared dependency. For each, name a contact and whether you have verified the information or assumed it.

Use the hospital table as a model: for each dependency, record the answer, its source and whether you saw the evidence yourself. Any fact marked as assumed should become a task with a person to ask. Date the map and name who will review it, because suppliers, contacts and coping times change. A map with no shared dependency usually means you have not yet asked what else uses the carrier, the monitoring service or the one engineer who knows every station.

### 2.7 Common errors and limits

- Mapping systems instead of functions — a list of servers is not a dependency map.
- Forgetting people as dependencies (a single expert, a single on-call manager).
- Treating "must be told" stakeholders as optional until an incident.
- Speaking your own sector's jargon to another sector.
- Dependency maps go stale; date them and set a review owner.

- Accepting a critical customer's coping time without seeing the plan it comes from, as the coordinator avoided with the hospital's six hours.
- Describing an outage in your own terms to another sector, instead of saying what it means for them, such as lower pressure from 14:00 to about 18:00 with water safe to drink.

### Exercises — chapter 2

**EX006 — Classify stakeholders.** *Objective:* use the five classes. *Inputs:* regulator, KVROC, HydroLogic Ltd, a local school, the chief executive, Kestrel Grid's control room. *Steps:* classify each, allowing more than one class. *Expected evidence:* table with one reason per row. *Rubric:* 3 = defensible classes with multiple classes where justified (for example Kestrel Grid as upstream dependency, "can help" and also "must be told" if the utility's load changes); 2 = one class each; 1 = several wrong; 0 = none.

**EX007 — Find the shared dependency.** *Objective:* identify single points. *Inputs:* telemetry for all twelve stations uses one carrier; KVROC monitors three utilities; one HydroLogic engineer services every station. *Steps:* explain the consequence of losing each and the coordination question you would raise. *Expected evidence:* three short analyses. *Rubric:* 3 = recognises loss of view across all stations (carrier), shared impact across utilities and reduced monitoring (KVROC), key-person risk (engineer); raises "what else uses that" and contingency; 2 = two of three; 1 = lists only; 0 = none.

**EX008 — Translate the consequence.** *Objective:* communicate across sectors. *Inputs:* "KW-07 will run on manual from 10:00 for six hours because of a suspected compromise of the supplier link." *Steps:* rewrite for the hospital estates manager. *Expected evidence:* message under 80 words. *Rubric:* 3 = states effect on supply in the hospital's terms (pressure, safety, duration), what the hospital should do, next update time and contact; avoids technical detail and speculation; 2 = missing next update; 1 = forwards the technical sentence; 0 = none.

**EX009 — Verify an assumption.** *Objective:* manage confidence. *Inputs:* the "6 hours" assumption in 2.5. *Steps:* describe how you would verify it and what you would do if the real figure were 2 hours. *Expected evidence:* plan and consequence. *Rubric:* 3 = ask for the specific plan section or a meeting with estates, record date and source; at 2 hours, the 2-hour notification promise becomes inadequate, so revise the agreement and plan alternative supply (tankers) with the hospital; 2 = verification only; 1 = accepts assumption; 0 = none.

**EX010 — Sector difference.** *Objective:* recognise sector meaning of harm. *Inputs:* the same ransomware infection of business IT at (a) a water utility and (b) a fuel pipeline operator. *Steps:* explain why each might shut down operations even if control systems are clean, citing the relevant public advisory where appropriate. *Expected evidence:* two paragraphs. *Rubric:* 3 = explains dependence of operations on business functions (billing, scheduling, monitoring) and caution about spread, cites AA21-131A only at its published level and avoids claims beyond it; 2 = generic; 1 = assumes OT was hit; 0 = none.

### Chapter synthesis

A critical service is a chain of functions with upstream, downstream and shared dependencies, and a set of stakeholders who decide, do, must be told, can help or are affected. Sectors differ in what harm means, so a coordinator translates consequences into the receiving sector's terms. Record the source and confidence of every dependency fact; an unverified assumption behind a decision is a task.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 12

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes and connection

After this chapter you should be able to:

- explain who may authorize security work on an essential service and what a valid authorization contains;
- write a **decision record** that would survive a regulator's or auditor's questions a year later;
- manage the evidence a coordination programme produces: what to keep, where, for how long, and who may see it;
- share sensitive information with partners using an agreed marking scheme (the Traffic Light Protocol).

Chapter 2 identified who decides. This chapter makes their decisions explicit, recorded and safe to share.

### 3.1 Why authorization is a coordination problem

Security work on an essential service — an assessment, a vulnerability scan, a supplier maintenance session, a penetration test, even "just looking" at a controller's configuration — can affect the service. In control environments, NIST notes that some routine IT activities, including active scanning, can disrupt operations ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). Authorization exists so that the person responsible for the consequence agrees in advance to what will happen, and so that everyone can later show what was agreed.

The coordinator is usually the person who **assembles** an authorization: drafts the scope, gets the right signatures, distributes it and keeps it. The coordinator is rarely the person who **grants** it.

### 3.2 What a valid authorization contains

Use the following elements for any assessment, test or third-party work on operational systems. NIST's testing guide describes rules of engagement with similar content for technical assessments ([NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)).

| Element | Question it answers |
|---|---|
| Purpose | Why is this work being done? |
| Systems in scope — and out of scope | Exactly which sites, systems, accounts; and which are excluded (for example dosing controllers, safety systems) |
| Activities permitted — and prohibited | What may be done (read configuration, review documents) and what may not (write, reboot, active scan) |
| People | Who will do the work, by name, and who supervises |
| Window | Start and end date and time, with time zone |
| Conditions | Operations present; stop conditions; communication channel |
| Data handling | What may be copied, where it is stored, when it is destroyed |
| Authority | Name, role and signature of the service owner (and of the supplier's manager where relevant) |

A **stop condition** is a pre-agreed event that ends the work immediately — "any unexpected alarm at the station; any operator request; any loss of view on the operator screens". Stop conditions turn "be careful" into something checkable.

### 3.3 Decision records

Coordination produces decisions: accept a risk, delay a patch, isolate a station, notify a regulator. A **decision record** is a short, dated note that captures:

1. the decision, in one sentence;
2. who made it, and under what authority;
3. the options considered and why this one was chosen;
4. the information available at the time, and what was unknown;
5. conditions and review date ("revisit if the supplier releases a fix, or by 30 June");
6. who was informed.

The point of item 4 is fairness to the decision-maker. A decision made at 02:00 with partial information can be good even if the outcome is bad. Without a record, hindsight rewrites history. With one, an organization can learn which decisions were poor and which were unlucky.

### 3.4 Evidence handling for a coordinator

A coordinator handles evidence of three kinds:

- **Governance evidence** — authorizations, decision records, risk acceptances, meeting minutes, exercise reports. Kept as the organization's record; protect integrity (who changed what) and retain according to policy.
- **Incident evidence** — logs, images, emails gathered during an incident. Its collection is technical work; the coordinator ensures it is requested early, its custody is recorded and access is limited. NIST's incident response guidance stresses preparing for evidence collection before incidents happen ([NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)).
- **Sensitive design information** — network diagrams, vulnerability reports, supplier access lists. Not evidence of wrongdoing but highly useful to an attacker. Store in an access-controlled location, never in general email threads.

Three practical rules: one authoritative location per record type; a named owner for each location; and no secrets (passwords, keys) in any record.

### 3.5 Sharing: the Traffic Light Protocol

Partners — the national CSIRT, a sector information-sharing group, the hospital — need information to protect themselves. The **Traffic Light Protocol (TLP)** is a widely used marking scheme that tells recipients how far they may share it ([FIRST, TLP 2.0](https://www.first.org/tlp/)):

- **TLP:RED** — for the named recipients only;
- **TLP:AMBER** — recipients may share within their organization and its clients on a need-to-know basis; **TLP:AMBER+STRICT** limits it to the recipient's organization only;
- **TLP:GREEN** — may be shared within the recipient's community, not publicly;
- **TLP:CLEAR** — no restriction beyond normal copyright.

TLP marks sharing permission, not confidentiality classification, and does not replace legal duties. Mark the subject line and the start of the message, and choose the least restrictive label that still protects people.

### 3.6 Worked example: authorizing a supplier assessment (synthetic)

ScadaCo offers a free "security health check" of the treatment works' control system. The coordinator drafts the authorization:

- **Purpose:** review configuration of the supervisory servers against ScadaCo's hardening guide.
- **In scope:** the two supervisory servers at KW-TW and their documentation. **Out of scope:** all station controllers, the dosing system, the network firewall.
- **Permitted:** read-only review of exported configuration files, supervised interview with J. Tan. **Prohibited:** network scanning, installing software, changing any setting, copying data off site except the final report.
- **People:** M. Ilic (ScadaCo), supervised by J. Tan.
- **Window:** 21 April 2026, 09:00–13:00 local time.
- **Stop conditions:** any operator request; any alarm at KW-TW.
- **Data handling:** the report is marked TLP:AMBER+STRICT, delivered by the agreed secure file-transfer service and stored in the security record library; ScadaCo deletes working notes within 14 days and confirms in writing.
- **Authority:** A. Mensah (operations manager, owner of KW-TW); ScadaCo's service manager countersigns.

On the day, M. Ilic asks to "quickly run a discovery tool to check versions". J. Tan refuses, because the authorization prohibits scanning, and records the request. The decision record notes the refusal and that the version check will be done from documentation instead. This is the authorization working as intended.

### 3.7 Practical activity

Take any routine supplier visit at an organization you know and write its authorization in the table format of 3.2. Mark which elements you could not fill in; those are the gaps in that organization's practice.

Choose a visit that touches a system someone would worry about, such as a maintenance session on a controller, rather than a cleaner or a delivery. Write the stop conditions as events anyone on site could recognise. Then ask the person who would sign as service owner whether they agree with your scope and exclusions; their answer usually reveals a system you forgot. Keep your draft and their comments together as evidence of the gap you found.

### 3.8 Common errors and limits

- "Verbal OK" from someone without authority over the service.
- Scope written as "the OT network" with no exclusions.
- No stop conditions, or stop conditions nobody on site knows.
- Decision records written after the outcome is known.
- Sending design information as ordinary email attachments.
- TLP used as if it were a legal classification or to hide information from people who need it.

- Letting the supplier redefine the work on the day, as ScadaCo's request to run a discovery tool would have done if J. Tan had not refused it.
- Keeping no record of a refusal, so a later reviewer cannot see that the authorization was enforced.

### Exercises — chapter 3

**EX011 — Repair an authorization.** *Objective:* find missing elements. *Inputs:* "OK for Northgate to do a pentest on the OT network next week — A. Mensah (via chat)". *Steps:* list the missing elements and rewrite it. *Expected evidence:* gap list and rewrite. *Rubric:* 3 = identifies purpose, scope and exclusions, permitted/prohibited activities, named people, window with time zone, stop conditions, data handling and written authority; rewrite excludes safety and dosing systems and prefers non-intrusive methods; 2 = most elements; 1 = minor edits; 0 = none.

**EX012 — Write a decision record.** *Objective:* record a decision fairly. *Inputs:* at 02:10 the duty manager decided to keep KW-05 in automatic despite an unexplained remote login, because manual operation needed a staff callout of 90 minutes. *Steps:* write the six-part record. *Expected evidence:* the record. *Rubric:* 3 = all six parts, with unknowns stated at the time (whether the login was malicious), conditions (watch dosing values, revisit at 06:00) and who was informed; 2 = missing options or unknowns; 1 = narrative only; 0 = none.

**EX013 — Choose a TLP label.** *Objective:* apply TLP 2.0. *Inputs:* (a) indicators of a phishing campaign targeting water utilities, to send to the sector group; (b) a report naming Kestrel Water's unpatched controller models, for KVROC; (c) a public advice note for customers. *Steps:* choose labels and justify. *Expected evidence:* three labels. *Rubric:* 3 = (a) GREEN (community benefit), (b) AMBER+STRICT or RED (sensitive to the utility; KVROC needs it), (c) CLEAR; reasons given; 2 = labels without reasons; 1 = everything RED; 0 = none.

**EX014 — Evidence locations.** *Objective:* organise governance evidence. *Inputs:* authorizations in an engineer's inbox, risk acceptances in board minutes, exercise reports on a shared drive, supplier access lists in a spreadsheet emailed monthly. *Steps:* propose a scheme. *Expected evidence:* one-paragraph scheme with owners. *Rubric:* 3 = one authoritative access-controlled location per record type, named owners, retention, version history, stop emailing access lists; 2 = location without owners; 1 = "use SharePoint"; 0 = none.

**EX015 — Stop condition test.** *Objective:* make caution checkable. *Inputs:* a supplier firmware update at KW-09 scheduled for 13:00–15:00. *Steps:* write three stop conditions and say who has authority to invoke them. *Expected evidence:* conditions and authority. *Rubric:* 3 = observable conditions (unexpected alarm, loss of view, overrun beyond 15:00, operator request) and the operator on shift or operations manager can stop without justification; 2 = vague conditions; 1 = supplier decides; 0 = none.

### Chapter synthesis

Authorization makes the owner of the consequence agree in advance to exactly what will happen, and lets everyone prove it later. A valid authorization has scope with exclusions, permitted and prohibited activities, named people, a window, stop conditions, data handling and written authority. Decision records capture what was known at the time; governance evidence lives in owned, controlled locations; TLP tells partners how far they may share.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 12

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Critical infrastructure and sector security: core methods

### Learning outcomes and connection

After this chapter you should be able to:

- run a simple, repeatable risk-assessment cycle for an essential service and keep a usable risk register;
- explain why multiplying likelihood by consequence can mislead in critical infrastructure and how to rank by consequence first;
- make sure every risk has an owner, a treatment, a due date and a review date, and detect when it does not;
- record a risk acceptance properly, with authority, conditions and expiry.

Chapters 1–3 gave you language, context and records. This chapter turns them into the coordinator's central method.

### 4.1 The risk-assessment cycle

NIST describes risk assessment as a process of preparing, conducting, communicating and maintaining the assessment ([NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). For a coordinator, a workable cycle has five steps:

1. **Frame** — which service, which time horizon, which consequences count and what the leadership's appetite is.
2. **Identify** — collect candidate risks from incidents, audits, staff conversations, supplier reviews, advisories and exercises.
3. **Analyse** — write each as cause-event-consequence; estimate likelihood and consequence with the people who know.
4. **Decide** — the risk owner chooses a treatment and a date; acceptance goes to the right level of authority.
5. **Monitor** — review on a schedule and when something changes; report the top risks upward.

The register is the memory of this cycle. If the register is out of date, the cycle has stopped, whatever the policy says.

### 4.2 Scales and their limits

Most organizations score likelihood and consequence on 1–5 scales. Make them meaningful by anchoring each level in your service's terms. A consequence scale for Kestrel Water might be:

| Level | Consequence (anchored) |
|---|---|
| 5 | Risk to health or life; unsafe water reaches customers; or loss of supply to a critical customer beyond its coping time |
| 4 | Loss of supply or pressure to more than 10,000 people for more than 12 hours; regulator enforcement likely |
| 3 | Localised supply loss; significant cost; customer data exposure with notification duty |
| 2 | Disruption absorbed by manual operation; internal cost |
| 1 | Negligible effect on service |

The usual product, likelihood × consequence, is convenient but has two known problems. First, it lets a frequent minor problem outrank a rare catastrophic one (4 × 3 = 12 beats 2 × 5 = 10). Second, the numbers are ordinal labels, not measurements, so arithmetic on them is weaker than it looks. In essential services, a sensible convention is to rank **consequence first** — anything that can hurt people or exceed a critical customer's coping time goes to the top — and use the product only to order risks of similar consequence. Whatever rule you choose, write it down so that the ranking is reproducible and arguable.

### 4.3 Ownership and hygiene

A risk without an owner is a worry, not a managed risk. Register hygiene means each entry has: an owner with authority over the affected service; a treatment decision; a due date for the treatment; a last-review date; and a link to the evidence of progress. A coordinator checks hygiene regularly, because register decay is silent: nobody notices that a "high" risk was last reviewed eight months ago until something happens.

In Lab 4, R02 shows all three failures at once: no owner, a review seven months old and an overdue treatment, on a level-5 risk.

### 4.4 Accepting risk

Acceptance is a legitimate treatment — no organization can fix everything at once. A proper acceptance records who accepted the risk (at a level of authority matching its consequence), what compensating measures apply, under what conditions the acceptance lapses, and when it expires. NIS2 requires the management bodies of essential and important entities to approve cybersecurity risk-management measures and oversee their implementation ([Directive (EU) 2022/2555, Article 20](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Whatever your jurisdiction, risks with level-5 consequences should be accepted by the executive or board, never quietly by the coordinator.

### 4.5 Worked example: reviewing the register (synthetic)

In March, the coordinator reviews Kestrel Water's register before the board audit and risk committee. She uses **Lab 4**, which encodes the ranking convention and hygiene checks so that anyone can rerun them.

**Lab 4** (save as `lab04.py`, run with `python3 lab04.py`):

```python
# Lab 4 - consequence-led risk register review (offline, standard library only; all data synthetic)
import datetime as dt
TODAY = dt.date(2026, 3, 2)
# id, title, owner, likelihood 1-5, consequence 1-5, service affected, last review, treatment due
REGISTER = [
    ("R01", "Remote vendor access to station RTUs without MFA", "A. Mensah", 4, 5, "drinking water", "2026-01-10", "2026-04-30"),
    ("R02", "Single engineer knows chlorine dosing logic",       "",          3, 5, "drinking water", "2025-08-01", "2026-02-01"),
    ("R03", "Billing portal phishing of customer accounts",      "C. Okafor", 5, 3, "billing",        "2026-02-20", "2026-06-30"),
    ("R04", "Historian backups never test-restored",             "J. Tan",    3, 4, "drinking water", "2025-12-15", "2026-01-31"),
    ("R05", "Grid supply loss at pumping station KW-07",         "A. Mensah", 2, 5, "drinking water", "2026-02-01", "2026-09-30"),
    ("R06", "Office printer firmware outdated",                  "IT desk",   4, 1, "office IT",      "2026-02-25", "2026-05-31"),
    ("R07", "Hospital not told of planned pressure work",        "L. Ferreira",3, 4, "hospital supply","2025-06-30", "2026-03-31"),
]
SERVICE_WEIGHT = {"drinking water": 3, "hospital supply": 3, "billing": 1, "office IT": 0}
rows = []
for rid, title, owner, l, c, svc, rev, due in REGISTER:
    score = l * c
    flags = []
    if not owner: flags.append("NO OWNER")
    if (TODAY - dt.date.fromisoformat(rev)).days > 180: flags.append("REVIEW STALE")
    if dt.date.fromisoformat(due) < TODAY: flags.append("TREATMENT OVERDUE")
    if c == 5: flags.append("SEVERE CONSEQUENCE")
    rows.append((score, c, SERVICE_WEIGHT[svc], rid, title, flags))
print("Ranked by score only:")
for score, c, w, rid, title, flags in sorted(rows, key=lambda r: (-r[0], r[3])):
    print(f"  {rid} score={score:2d}")
print("Ranked by consequence, then service weight, then score:")
for i, (score, c, w, rid, title, flags) in enumerate(sorted(rows, key=lambda r: (-r[1], -r[2], -r[0], r[3])), 1):
    print(f"  {i}. {rid} c={c} w={w} score={score:2d} {'; '.join(flags) or 'ok'}")
print("Needs governance action:", ", ".join(r[3] for r in sorted(rows, key=lambda r: r[3]) if any(f != 'SEVERE CONSEQUENCE' for f in r[5])))
```

Expected output (Python 3.13.5):

```text
Ranked by score only:
  R01 score=20
  R02 score=15
  R03 score=15
  R04 score=12
  R07 score=12
  R05 score=10
  R06 score= 4
Ranked by consequence, then service weight, then score:
  1. R01 c=5 w=3 score=20 SEVERE CONSEQUENCE
  2. R02 c=5 w=3 score=15 NO OWNER; REVIEW STALE; TREATMENT OVERDUE; SEVERE CONSEQUENCE
  3. R05 c=5 w=3 score=10 SEVERE CONSEQUENCE
  4. R04 c=4 w=3 score=12 TREATMENT OVERDUE
  5. R07 c=4 w=3 score=12 REVIEW STALE
  6. R03 c=3 w=1 score=15 ok
  7. R06 c=1 w=0 score= 4 ok
Needs governance action: R02, R04, R07
```

Read the two rankings. By score alone, the billing phishing risk R03 (15) ties with R02 and sits above R05 — a grid supply loss at a pumping station that could leave thousands without water. Ranked by consequence then by the importance of the affected service, the three level-5 drinking-water risks come first. The hygiene flags show where governance, not technology, is failing: R02 (a single engineer who understands the chlorine dosing logic) has **no owner**, has not been reviewed for seven months and its treatment is overdue; R04's restore test is overdue; R07's review is stale. These three go to the committee as **governance actions**, with a proposed owner for R02 (A. Mensah, who owns dosing).

Note what the lab does not do. It does not tell you whether "likelihood 4" for R01 is right — that comes from conversation with people who know the supplier and the threat. It makes the ranking rule explicit and the hygiene checks repeatable; it does not make the judgement for you.

### 4.6 Practical activity

Change the ranking key in Lab 4 to sort by score alone and show the result to a colleague. Ask which order they would defend at a board meeting after a pressure failure at the hospital. Then write your organization's ranking rule in two sentences.

Notice where R03 and R05 land in each order, because that is the argument you would face after an outage: a billing phishing risk ranked above loss of supply at a pumping station is hard to defend. Then add one invented risk with consequence 5 and likelihood 1 and check where it falls under each rule. Finally, run the hygiene checks with a different TODAY date, such as six months later, and see which reviews and treatments become stale or overdue without anyone noticing.

### 4.7 Common errors and limits

- Scales without anchors, so "4" means different things to different people.
- Arithmetic on ordinal scores presented as precision ("risk 13.6").
- Owners who are coordinators or committees instead of managers with authority.
- Acceptances without expiry, which become permanent by default.
- Registers that list technologies ("SCADA") instead of risk statements.
- Treating the register as the goal; it is only the memory of decisions.

- Letting a level-5 risk sit without an owner because nobody wants it, as R02 did for months.
- Scoring likelihood without talking to the people who know the supplier or the threat, so the number reflects the coordinator's guess.

### Exercises — chapter 4

**EX016 — Anchor a scale.** *Objective:* make likelihood meaningful. *Inputs:* the consequence scale in 4.2. *Steps:* write a five-level likelihood scale anchored in time and evidence. *Expected evidence:* the scale. *Rubric:* 3 = levels tied to periods or evidence (for example 5 = has occurred here in the last year or is being actively attempted in the sector; 1 = no known occurrence in the sector, would need multiple unlikely conditions); notes that existing controls are taken into account; 2 = periods only; 1 = words like "high"; 0 = none.

**EX017 — Read Lab 4.** *Objective:* interpret ranking and hygiene. *Inputs:* Lab 4 output. *Steps:* explain why R03 moves from joint second to sixth and why R05 moves up; list the governance actions and who should own each. *Expected evidence:* explanation and list. *Rubric:* 3 = R03 has consequence 3 on billing; R05 has consequence 5 on drinking water; actions: R02 owner (A. Mensah) and overdue treatment, R04 overdue restore test (J. Tan with A. Mensah as service owner), R07 stale review (L. Ferreira, or move to the coordinator for the hospital liaison); 2 = explanation without owners; 1 = repeats output; 0 = none.

**EX018 — Accept a risk properly.** *Objective:* record acceptance. *Inputs:* the board decides it cannot fund replacing station controllers at KW-10 this year. *Steps:* draft the acceptance record. *Expected evidence:* record. *Rubric:* 3 = names the risk statement, accepting authority (chief executive or board, given consequence), compensating measures (for example no remote access, monitoring by KVROC, spare parts), conditions that end the acceptance (new advisory, incident), expiry date and review owner; 2 = no expiry; 1 = "accepted"; 0 = none.

**EX019 — Extend the lab.** *Objective:* encode another hygiene rule. *Inputs:* Lab 4. *Steps:* add a flag "ACCEPTANCE EXPIRED" using a new field, test it with one expired and one valid acceptance and show the output. *Expected evidence:* code change and output. *Rubric:* 3 = field added for every row, rule correct, two test cases demonstrate both outcomes, and "Needs governance action" includes the expired one; 2 = works without tests; 1 = rule only; 0 = none.

**EX020 — Present to the committee.** *Objective:* communicate the register. *Inputs:* Lab 4 output. *Steps:* write the one-page summary for the audit and risk committee. *Expected evidence:* summary. *Rubric:* 3 = top consequence-ranked risks in plain language with owners and dates, governance actions with requested decisions, explicit statement of the ranking rule and its limits, no single "score"; 2 = lists risks without asks; 1 = pastes the table; 0 = none.

### Chapter synthesis

Risk assessment is a cycle — frame, identify, analyse, decide, monitor — and the register is its memory. Anchor scales in your service's terms, rank by consequence first in essential services, and treat scores as ordinal. Every risk needs an owner with authority, a treatment, dates and evidence; acceptance is legitimate only with matching authority, conditions and expiry.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 12

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Critical infrastructure and sector security: tools and interpretation

### Learning outcomes and connection

After this chapter you should be able to:

- choose between the main public frameworks and baselines for an essential service and explain what each is for;
- read a self-assessment or maturity score critically: what it measures, who produced it, and what it cannot show;
- design a small set of programme metrics that drive decisions instead of decorating reports;
- interpret technical findings handed to you by engineers and suppliers well enough to ask the right follow-up questions.

The coordinator's "tools" are mostly documents and measures. Chapter 4 built the register; this chapter supplies the external yardsticks and the numbers that report on it.

### 5.1 The framework landscape

You will meet several overlapping references. Each has a distinct purpose:

| Reference | What it is for | Typical use by a coordinator |
|---|---|---|
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Outcome taxonomy (Govern, Identify, Protect, Detect, Respond, Recover) | Structure the programme and profiles; talk to executives |
| [CISA Cross-Sector Cybersecurity Performance Goals (CPGs)](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) | A prioritised subset of high-impact practices for critical infrastructure | Quick baseline; find obvious gaps first |
| [NCSC Cyber Assessment Framework (CAF)](https://www.ncsc.gov.uk/collection/caf) | Outcome-based assessment for operators of essential services, with indicators of good practice | Structured self-assessment, regulator dialogue (UK context) |
| [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | Standards for industrial automation and control system security, covering asset owners, integrators and product suppliers | Procurement and supplier requirements; programme expectations for OT |
| [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Guidance on securing OT | Shared vocabulary with engineers |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Catalogue of security and privacy controls | Detailed control language when needed |

The coordinator's rule: **one primary structure** (for example CSF 2.0) for the programme, with other references mapped to it, rather than four parallel spreadsheets. Regulatory requirements in your jurisdiction come first; frameworks help you meet them, they do not replace them.

### 5.2 Reading an assessment

An assessment result such as "Protect: 2.4 / 4" or "CPG coverage 71%" invites false confidence. Before you repeat it, ask five questions:

1. **What was assessed?** Which sites, systems and processes — and which were not?
2. **Who assessed, how?** Self-assessment by the system's owner, a peer, an independent assessor? By interview, document review or test?
3. **What counts as "met"?** A written policy, a policy in use, or a policy shown to work?
4. **When?** Assessments age quickly after reorganisations, supplier changes and incidents.
5. **What decision does it support?** If no decision changes depending on the number, it is decoration.

A self-assessment is valuable — it is cheap and builds understanding — but it measures what owners believe. Chapter 7 adds ways to obtain stronger evidence.

### 5.3 Metrics that drive decisions

Good programme metrics share three properties: they relate to a consequence or to a control that protects one; their owner can change them; and a threshold triggers a known action. Compare:

| Weak metric | Better metric | Action on threshold |
|---|---|---|
| Number of security policies | % of level-5 risks with an owner and an in-date treatment | Below 100% → executive escalation |
| Phishing emails blocked | Median time from supplier contract end to account removal | Over 5 working days → access process review |
| Vulnerabilities found | % of internet-facing operational interfaces (should be zero) | Any → immediate owner notification |
| Training completion | % of on-call managers who took part in an exercise in the last 12 months | Below 80% → schedule exercise |

Counts of activity ("we blocked 40,000 attacks") are easily produced and rarely useful for decisions. Prefer measures of exposure, timeliness and coverage of the things that matter most.

### 5.4 Interpreting technical findings

Engineers, KVROC and suppliers send findings. You do not need to verify them technically, but you must ask questions that make them decision-ready:

- **What is affected** — which site, which function, which consequence level?
- **How do you know** — observed directly, inferred, or reported by a tool that may be wrong?
- **What is the exposure** — reachable from the internet, from the office network, only on site?
- **What is the recommended action, by whom, by when, and what does it disrupt?**
- **Is there a public advisory?** If so, link it; advisories such as CISA's water-sector alert on internet-exposed controllers with default passwords ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)) help executives understand that a finding is not hypothetical.

### 5.5 Worked example: a CPG self-assessment (synthetic)

L. Ferreira completed a CPG checklist for Kestrel Water and reports "71% of goals met". The coordinator asks the five questions and finds: the assessment covered the corporate network and the treatment works but **not** the twelve stations; answers were "yes" if a policy existed; and it was done before HydroLogic's remote-access arrangement changed. Two "met" items — on multi-factor authentication for remote access and on revoking credentials of departing staff — have no evidence for supplier accounts.

She reports to the executive: "*A self-assessment of corporate IT and the treatment works found most baseline practices in place on paper. It did not cover the stations, and two items that matter most for the stations — multi-factor authentication for remote access and timely removal of accounts — are unverified for suppliers. I propose a supplier-access review in May (Chapter 8) and to repeat the assessment including stations by September.*" The 71% stays in an appendix.

### 5.6 Practical activity

Take any public dashboard or annual-report statement about cybersecurity (for example "100% of staff trained"). Apply the five questions and rewrite it as a decision-ready statement, noting what you would need to know.

Write your rewrite in the same form as the coordinator's report on the CPG self-assessment: what was covered, how it was judged, what was left out and what decision follows. If the statement supports no decision, say so; that is a finding in itself. Keep the original figure, but put it after the context rather than at the front. Note the date of the statement and whether anything has changed since, such as a reorganisation or a new supplier.

### 5.7 Common errors and limits

- Running several frameworks in parallel without mapping.
- Reporting percentages without scope and method.
- Choosing metrics because data is easy to get.
- Treating supplier marketing ("62443-compliant") as an assessment of your installation.
- Forgetting that frameworks and baselines are revised; cite version and date.

- Counting a goal as met because a policy exists, as the CPG self-assessment did, without asking whether it is in use or shown to work.
- Leaving out part of the service, such as the twelve stations, and still reporting one figure for the whole utility.
- Repeating an assessment result to the executive before asking when it was done and what has changed since.

### Exercises — chapter 5

**EX021 — Choose a primary structure.** *Objective:* select and map frameworks. *Inputs:* Kestrel Water must report to its regulator, buys OT systems from suppliers and has a board unfamiliar with security. *Steps:* propose a primary structure and how the CPGs and 62443 relate to it. *Expected evidence:* a short rationale. *Rubric:* 3 = regulatory requirements first, CSF 2.0 as programme structure for the board, CPGs as prioritised baseline mapped to it, 62443 used for supplier and procurement requirements; 2 = choice without mapping; 1 = "do all"; 0 = none.

**EX022 — Interrogate a score.** *Objective:* apply the five questions. *Inputs:* "Detect maturity 3.1/5, up from 2.6". *Steps:* write the five questions applied to this score and say what answer would make the improvement credible. *Expected evidence:* questions and criteria. *Rubric:* 3 = asks scope, assessor and method, definition of levels, date and decision supported; credible if same scope and method, independent or evidence-based, and linked to an observed outcome (for example detection of an exercise inject); 2 = questions only; 1 = accepts; 0 = none.

**EX023 — Fix the metrics.** *Objective:* design decision-driving metrics. *Inputs:* current monthly report: emails blocked, antivirus detections, policies approved, staff trained. *Steps:* replace with four metrics including owner and threshold action. *Expected evidence:* table. *Rubric:* 3 = metrics tied to consequence and control (for example level-5 risk hygiene, supplier account removal time, exposure of operational interfaces, exercise participation), each with owner and action; 2 = metrics without actions; 1 = cosmetic changes; 0 = none.

**EX024 — Make a finding decision-ready.** *Objective:* question a technical finding. *Inputs:* KVROC email: "Saw RDP from internet to hmi-02 last night, recommend blocking." *Steps:* write the reply. *Expected evidence:* reply. *Rubric:* 3 = asks which site and function hmi-02 serves, whether connection was successful, source and evidence, whether still exposed; asks who can block and what blocking disrupts (supplier access?); involves operations owner; treats as potentially urgent; 2 = asks some; 1 = "please block"; 0 = none.

**EX025 — Report honestly.** *Objective:* communicate an assessment's limits. *Inputs:* worked example 5.5. *Steps:* rewrite the executive message for the board in under 100 words. *Expected evidence:* message. *Rubric:* 3 = states coverage gap and unverified items plainly, gives plan and date, avoids the percentage as headline; 2 = mentions percentage first but includes limits; 1 = "71% compliant"; 0 = none.

### Chapter synthesis

Frameworks and baselines are yardsticks: pick one primary structure, satisfy the law first, and map the rest. Read every assessment by scope, method, definition, date and decision supported. Measure exposure, timeliness and coverage of what matters, with owners and threshold actions. Make technical findings decision-ready by asking what, how known, how exposed, who acts and what it disrupts.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 12

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Critical infrastructure and sector security: operational workflow

### Learning outcomes and connection

After this chapter you should be able to:

- define the roles a critical-infrastructure security programme needs and how they relate to operations;
- build and check a RACI matrix so that every key activity has exactly one accountable person and a clear lead;
- run change governance across IT and OT without either blocking operations or bypassing safety;
- design an escalation path from a shift operator to the executive that works at 03:00 on a Sunday.

Chapter 5 gave you yardsticks. This chapter makes the programme run, day to day.

### 6.1 Roles

At Kestrel Water's size, the roles below may be shared by a handful of people. What matters is that each is assigned:

- **Executive sponsor** (chief operating officer) — owns the programme, accepts high risks, resolves conflicts between departments.
- **Service owners** (operations manager for treatment and stations; customer-services manager for billing) — own risks and decisions for their services.
- **Coordinator** — runs the cycle: register, records, exercises, reporting, supplier reviews.
- **Security lead** — technical security advice and monitoring liaison with KVROC.
- **Control-systems engineer** — configuration and change on operational systems.
- **Communications lead** — public and media messages.
- **Incident lead** (rotating, on call) — commands the response when an incident is declared.
- **Suppliers** — do work under authorization; never own decisions about your service.

NIST's incident response guidance emphasises defining roles and responsibilities, including those outside the security team, before incidents ([NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)).

### 6.2 RACI

A **RACI** matrix lists activities against people with one letter each: **R**esponsible (does the work), **A**ccountable (answers for the outcome and signs off — exactly one per activity), **C**onsulted (two-way input before the decision), **I**nformed (told after). Two rules catch most defects:

1. Exactly one **A** per activity. Zero means nobody answers; two means each assumes the other will.
2. At least one **R**, and where several, one named lead.

Add two coordinator's checks: nobody should be accountable for approving their own access or work; and nobody should carry so many R and A entries in an incident that they become a bottleneck.

### 6.3 Change governance across IT and OT

Changes to operational systems can affect the physical process. A workable change process for a small utility has three classes:

- **Standard** — pre-approved, low-risk, repeatable (replacing a failed operator keyboard): log it.
- **Normal** — assessed and approved by the service owner, with a test or rollback plan and a window agreed with operations.
- **Emergency** — needed now to protect people or the service; approved verbally by the incident lead or service owner, recorded within 24 hours and reviewed afterwards.

The coordinator's interest is that security-relevant changes (new remote access, firewall rule changes, new suppliers, software on control-room computers) cannot slip into "standard", and that emergency changes made during incidents are reviewed rather than becoming permanent.

### 6.4 Escalation

An escalation path answers, for each severity: who is called, by whom, how, within what time, and what happens if they do not answer. Write it as a table with deputies, test it (Chapter 11), and put it where night-shift operators can find it without a computer — a printed card in the control room — because the incident might have taken the computers.

Kestrel Water's card lists the incident lead, the operations manager and the security lead with a named deputy for each, plus mobile numbers that do not depend on the corporate network.

### 6.5 Worked example: checking the incident RACI (synthetic)

The coordinator drafts Kestrel Water's incident RACI and runs **Lab 6**, which applies the rules of 6.2.

**Lab 6** (save as `lab06.py`, run with `python3 lab06.py`):

```python
# Lab 6 - RACI matrix check for incident coordination (offline, standard library only; synthetic)
PEOPLE = ["Coordinator", "Ops manager", "Security lead", "Comms", "Vendor", "CEO"]
# activity -> one letter per person (R responsible, A accountable, C consulted, I informed, - none)
RACI = {
    "Declare cyber incident":            "R A C I - I",
    "Decide to isolate stations":        "C A R I C I",
    "Switch stations to manual operation":"I A - - - I",
    "Notify regulator":                  "R - C C - A",
    "Brief hospital (critical customer)":"R C I R - A",
    "Approve vendor remote session":     "C A A - R -",
    "Public statement":                  "C C C R - -",
}
issues = []
load = {p: 0 for p in PEOPLE}
for act, codes in RACI.items():
    c = codes.split()
    assert len(c) == len(PEOPLE), act
    a = [p for p, x in zip(PEOPLE, c) if x == "A"]
    r = [p for p, x in zip(PEOPLE, c) if x == "R"]
    for p, x in zip(PEOPLE, c):
        if x in "RA": load[p] += 1
    if len(a) != 1: issues.append(f"{act}: {len(a)} accountable ({', '.join(a) or 'none'})")
    if not r: issues.append(f"{act}: nobody responsible")
    if len(r) > 1: issues.append(f"{act}: {len(r)} responsible ({', '.join(r)}) - name a lead")
    if act.startswith("Approve") and c[PEOPLE.index("Vendor")] in "RA":
        issues.append(f"{act}: vendor is responsible for approving its own access")
for i in issues: print("ISSUE", i)
print("R/A load:", ", ".join(f"{p}={n}" for p, n in load.items()))
print(f"{len(issues)} issues in {len(RACI)} activities")
```

Expected output (Python 3.13.5):

```text
ISSUE Switch stations to manual operation: nobody responsible
ISSUE Brief hospital (critical customer): 2 responsible (Coordinator, Comms) - name a lead
ISSUE Approve vendor remote session: 2 accountable (Ops manager, Security lead)
ISSUE Approve vendor remote session: vendor is responsible for approving its own access
ISSUE Public statement: 0 accountable (none)
R/A load: Coordinator=3, Ops manager=4, Security lead=2, Comms=2, Vendor=1, CEO=2
5 issues in 7 activities
```

Five defects in seven activities:

- **Switch stations to manual operation** has an accountable owner (operations manager) but nobody responsible — in practice, shift operators and on-call technicians do it, and they are missing from the matrix. The fix is to add the shift supervisor as R.
- **Brief hospital** has two responsibles. The coordinator and communications might each think the other called. Name the coordinator as lead (it is an operational liaison) with communications consulted on wording.
- **Approve vendor remote session** has two accountables and lists the vendor as responsible. The operations manager should be the single A (owns the stations); the security lead is C; the vendor *requests* access and is I about the decision — a party must never approve its own access.
- **Public statement** has no accountable person. The chief executive should be A, communications R.

The load line shows the operations manager carrying four R/A entries — during an incident, the same person is running the plant. The coordinator proposes a deputy for the incident-related entries. The lab checks structure only; whether the right people were chosen is a judgement for the executive sponsor.

### 6.6 Practical activity

Write a RACI for "onboard a new supplier with remote access" using at least five roles, then check it against the four rules by hand or by editing Lab 6.

Include the supplier as a role and make sure it never approves its own access, which Lab 6 checks explicitly. Name who is accountable for creating the account, who checks that the contract has the security clauses, and who is informed when the account is enabled. Then count each person's R and A entries: if one name appears on nearly every line, onboarding will stall whenever that person is on leave. Show the result to the operations manager and ask whether anyone is missing.

### 6.7 Common errors and limits

- Committees as accountable ("the security board").
- RACIs written for normal days only, not incidents.
- Emergency changes never reviewed.
- Escalation lists without deputies, or only stored on the network.
- A RACI is a social contract: publish it, walk through it with each person, and update it after reorganisations.

- Leaving the people who actually do the work off the matrix, as Lab 6 found with shift operators for manual operation.
- Allowing a party to approve its own access, such as a supplier marked responsible for approving its remote session.
- Giving one person so many R and A entries that the incident depends on them alone.

### Exercises — chapter 6

**EX026 — Fix the RACI.** *Objective:* correct defects. *Inputs:* Lab 6 matrix. *Steps:* propose corrected rows for the five issues and rerun the check (by hand or code). *Expected evidence:* corrected matrix and clean result. *Rubric:* 3 = zero issues, vendor never A or R for approval, a shift role added for manual operation, a single lead for hospital briefing, CEO accountable for public statement; 2 = one issue remains; 1 = partial; 0 = none.

**EX027 — Classify changes.** *Objective:* apply change classes. *Inputs:* (a) new firewall rule allowing a supplier VPN; (b) replacing a failed UPS battery in a station cabinet; (c) disabling a compromised account during an incident; (d) installing a monitoring agent on the historian. *Steps:* classify and justify. *Expected evidence:* four classes. *Rubric:* 3 = (a) normal (security-relevant), (b) standard if pre-approved procedure exists, (c) emergency with post-review, (d) normal with supplier compatibility check; 2 = three right; 1 = all standard; 0 = none.

**EX028 — Escalation card.** *Objective:* design a usable escalation path. *Inputs:* roles in 6.1. *Steps:* write the printed card for night-shift operators for a suspected cyber event. *Expected evidence:* card content. *Rubric:* 3 = observable triggers, first call and deputy with phone numbers placeholders, time limits, what to do meanwhile (safety first, do not switch off computers without instruction, note times), when to call the incident lead directly; 2 = no deputies; 1 = "call IT"; 0 = none.

**EX029 — Bottleneck analysis.** *Objective:* use the load line. *Inputs:* Lab 6 load output. *Steps:* propose how to reduce the operations manager's incident load without weakening safety authority. *Expected evidence:* proposal. *Rubric:* 3 = keeps safety decisions with operations but delegates liaison and vendor approval to a named deputy or the incident lead, with the operations manager consulted; 2 = delegation without safety caveat; 1 = moves safety decisions to IT; 0 = none.

**EX030 — Emergency change review.** *Objective:* close emergency changes. *Inputs:* during an incident, an engineer added a firewall rule blocking all supplier access and created a temporary local admin account. *Steps:* describe the post-incident review. *Expected evidence:* review steps. *Rubric:* 3 = list emergency changes from the record, decide keep/modify/revert for each with owner, remove temporary account, restore supplier access only through the normal process, update documentation; 2 = some steps; 1 = "leave it"; 0 = none.

### Chapter synthesis

A programme runs on assigned roles, a RACI with one accountable per activity and a named lead, change governance that keeps security-relevant changes visible, and an escalation path that works offline at night. Check the RACI for structure, ownership of approvals and incident load; review every emergency change after the event.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 12

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Critical infrastructure and sector security: controls and verification

### Learning outcomes and connection

After this chapter you should be able to:

- describe a control in terms a manager can own: objective, owner, operation and evidence;
- distinguish levels of assurance — stated, documented, observed, tested — and decide which level each control needs;
- plan a proportionate verification programme for the controls that protect level-5 consequences;
- manage exceptions to controls as time-limited, owned risk decisions.

Chapter 6 made the programme run. This chapter asks whether its protections actually work.

### 7.1 What a control is, for a manager

A **control** is a measure that modifies risk ([NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) catalogues thousands of them). For coordination purposes, describe each important control on one card:

- **Objective** — which risk it addresses and how ("prevents use of a stolen supplier password to log in to stations");
- **Owner** — who answers for it working;
- **Operation** — what happens, how often, by whom ("remote access gateway requires a second factor for every supplier account");
- **Evidence** — what would show it is working, and where it is kept;
- **Failure signal** — what you would see if it stopped working.

Controls without owners decay just like risks without owners.

### 7.2 Levels of assurance

How sure are you that a control works? Four useful levels:

| Level | Meaning | Example evidence |
|---|---|---|
| Stated | Someone says it exists | "Yes, suppliers use MFA" in a meeting |
| Documented | A policy or design describes it | Remote-access standard v2 |
| Observed | Records show it operating | Gateway configuration export; login logs showing second-factor events |
| Tested | A deliberate test showed it stops what it should | A supervised attempt to log in with password only is refused, recorded in a test report |

Higher levels cost more. A proportionate programme aims for **tested** on controls protecting level-5 consequences, **observed** for level 3–4, and accepts **documented** for the rest. Continuous monitoring guidance from NIST describes maintaining ongoing awareness of whether controls remain effective ([NIST SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)).

### 7.3 Who verifies

- **First line** — control owners check their own controls (self-assessment, routine checks).
- **Second line** — the coordinator or security function reviews evidence and samples.
- **Third line** — internal audit or an independent assessor gives assurance to the board.

The coordinator usually designs the verification plan and runs second-line checks. Tests on operational systems must be authorized like any other work (Chapter 3), and in control environments a "test" is often a review of configuration and logs rather than an active attempt.

Second-line checks should sample evidence directly rather than accept the owner's summary.

### 7.4 Exceptions

Sometimes a control cannot be applied: an old station controller cannot support a second factor; a medical device cannot be patched without losing its certification. An **exception** is a recorded, owned decision to operate without the control, which is a form of risk acceptance (Chapter 4). It needs: the control and system concerned; the reason; compensating measures; the accepting authority; an expiry date; and a plan to remove the exception. An exception register is reviewed with the risk register.

At Kestrel Water, the KW-10 controller exception went to the board with an expiry in March.

### 7.5 Worked example: verifying three controls (synthetic)

The coordinator chooses three controls that protect level-5 risks and checks each:

| Control | Stated / documented | Observed | Tested | Finding |
|---|---|---|---|---|
| C1: MFA for all supplier remote access | Yes — remote-access standard v2 | Gateway export shows MFA on 5 of 6 supplier accounts | Not yet | ScadaCo's account lacks MFA (later confirmed in Lab 8). **Gap.** |
| C2: Historian backups restorable within 24 h | Yes — backup procedure | Backup jobs succeed nightly | Last restore test: never | **Unverified** — successful backup ≠ successful restore (links to risk R04). |
| C3: Dosing limits enforced in controller logic | Yes — design document | Limits visible in configuration review by J. Tan | Supervised bench test by supplier on spare controller, recorded 3 Feb | **Verified** to tested level for the spare; production configuration matches by checksum. |

The verification plan that follows: fix C1 within 30 days (owner A. Mensah); schedule a restore test for C2 within 60 days with a timed result (owner J. Tan); repeat C3 check after any logic change. The coordinator reports each control's assurance level, not a single "controls effective" statement.

### 7.6 Practical activity

Write control cards (objective, owner, operation, evidence, failure signal) for two controls at an organization you know, and assign each a current assurance level with justification.

For each card, say what the failure signal would look like in practice, such as a supplier login with no second-factor event in the gateway log. Explain why you chose the assurance level, citing the evidence you actually saw. Then decide what level the control should reach, given the consequence it protects, and what one step would raise it, for example a restore test for a backup that has only been observed succeeding. Keep cards short enough that an owner will update them.

### 7.7 Common errors and limits

- Equating "the job succeeded" with "the control works" (backups, patches).
- Verification only at the stated or documented level for critical controls.
- Active testing of operational systems without authorization and operations' agreement.
- Exceptions without expiry, which silently become the design.
- Reporting controls as "effective" without saying how that was established.

- Treating a supplier's own statement that MFA is enabled as observed evidence, when only the gateway export shows it.
- Verifying a control once and never again, so a later configuration change silently removes it.
- Testing a spare or bench system and forgetting to confirm that production matches, as C3 did by checksum.

### Exercises — chapter 7

**EX031 — Write a control card.** *Objective:* make a control ownable. *Inputs:* "Supplier accounts are removed when contracts end." *Steps:* write the five-part card. *Expected evidence:* card. *Rubric:* 3 = objective tied to a risk, owner with authority (operations manager or contract owner), operation with trigger and time limit, evidence (monthly reconciliation of accounts against contracts), failure signal (accounts for ended contracts exist); 2 = missing failure signal; 1 = restates sentence; 0 = none.

**EX032 — Assign assurance targets.** *Objective:* apply proportionality. *Inputs:* controls: MFA for supplier access; password policy for office laptops; manual-operation procedure for stations; visitor badges at head office. *Steps:* assign target assurance levels and justify by consequence. *Expected evidence:* four targets. *Rubric:* 3 = tested for supplier MFA and manual operation (via exercise or drill), documented or observed for the others with reasoning; 2 = targets without reasons; 1 = all tested; 0 = none.

**EX033 — Design a restore test.** *Objective:* verify C2. *Inputs:* worked example. *Steps:* outline the test, success criteria and authorization. *Expected evidence:* outline. *Rubric:* 3 = restore to isolated environment, not production; timed against 24 h objective; checks data completeness for a chosen period; authorized by service owner; result recorded with date and evidence; 2 = no success criteria; 1 = "check backup logs"; 0 = none.

**EX034 — Write an exception.** *Objective:* manage a control gap. *Inputs:* KW-10's controller cannot support MFA for local engineering access. *Steps:* draft the exception. *Expected evidence:* exception record. *Rubric:* 3 = control and system, reason, compensating measures (no remote path, physical access control, change monitoring), accepting authority matched to consequence, expiry, removal plan; 2 = no expiry; 1 = "not possible"; 0 = none.

**EX035 — Report assurance.** *Objective:* communicate verification honestly. *Inputs:* worked example table. *Steps:* write three lines for the executive, one per control. *Expected evidence:* three lines. *Rubric:* 3 = each states assurance level reached, gap or result, owner and date; avoids "effective" without evidence; 2 = missing dates; 1 = "controls effective"; 0 = none.

### Chapter synthesis

A control is something a manager can own: objective, owner, operation, evidence and failure signal. Assurance rises from stated to documented, observed and tested; aim for tested on controls protecting the worst consequences. Verify proportionately through three lines, authorize tests like any other work, and keep exceptions owned, compensated and time-limited.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 12

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Critical infrastructure and sector security: supervised case analysis

### Learning outcomes and connection

After this chapter you should be able to:

- analyse a supplier-access problem as a governance case: contracts, accounts, people and evidence;
- run a periodic third-party remote-access review and act on its findings proportionately;
- write supplier security requirements into contracts and onboarding;
- present a case analysis to a supervisor with decisions requested, evidence attached and uncertainty labelled.

This is the book's first supervised case. It brings together risk (Chapter 4), roles (Chapter 6) and control verification (Chapter 7).

### 8.1 Why suppliers matter so much here

Essential services depend on suppliers for equipment, software, maintenance and monitoring. Supplier remote access is convenient — a pump expert can fix a problem from 200 kilometres away at night — and it is also a recurring route of compromise. CISA's guidance on primary mitigations for OT lists reducing exposure and securing remote access among its priorities ([CISA, Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology)). NIST's supply-chain guidance treats suppliers as part of the organization's risk and recommends integrating supply-chain risk management into governance and acquisition ([NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final)). NIS2 lists supply-chain security among the risk-management measures entities must take ([Directive (EU) 2022/2555, Article 21](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)).

### 8.2 The supplier lifecycle

Governance of a supplier with access follows a lifecycle:

1. **Select** — security questions in procurement proportionate to the access requested.
2. **Contract** — security obligations: named individuals, MFA, notification of incidents and staff departures, right to review, data handling, support for your incident response.
3. **Onboard** — accounts created per named person, least access, approval process for sessions (Chapter 6).
4. **Operate** — sessions approved, logged and reviewed; periodic access reviews.
5. **Change** — new staff, new systems, mergers: re-review.
6. **Exit** — accounts removed, data returned or destroyed, confirmation recorded.

Most real problems sit at the joins: a contract that ended but whose account survived; an engineer who left the supplier but whose password did not.

### 8.3 The access review

A periodic **access review** reconciles three sources: the list of accounts (what exists), the contracts register (what should exist) and session records (what is used). Typical findings and proportionate responses:

| Finding | Why it matters | Proportionate response |
|---|---|---|
| Account for ended contract | Nobody is accountable for its use | Disable now; confirm with supplier |
| Unused for more than 90 days | Unneeded exposure | Disable; re-enable on request through process |
| Shared or unnamed account | Actions cannot be attributed | Replace with named accounts; meanwhile restrict |
| No MFA | Password alone grants access | Fix or record a time-limited exception |
| Usage far above expected | May be legitimate project, misuse or compromise | Ask the supplier and the internal owner; review session records before concluding |

The last row needs care. Unusual volume is a **question**, not an accusation.

### 8.4 Worked case: the May review (synthetic)

Following the control gaps in Chapter 7, the coordinator runs the first supplier-access review on 4 May 2026, under an authorization from A. Mensah that permits read-only export of the gateway account list and session log. **Lab 8** reproduces the reconciliation.

**Lab 8** (save as `lab08.py`, run with `python3 lab08.py`):

```python
# Lab 8 - third-party remote-access review (offline, standard library only; all data synthetic)
import datetime as dt
TODAY = dt.date(2026, 5, 4)
# account, supplier, named person, MFA, contract end, last session, sessions in 90 days
ACCOUNTS = [
    ("v-hydro1",  "HydroLogic Ltd",  "P. Novak",  True,  "2027-03-31", "2026-04-28", 6),
    ("v-hydro2",  "HydroLogic Ltd",  "",          True,  "2027-03-31", "2026-04-30", 11),
    ("v-scadaco", "ScadaCo",         "M. Ilic",   False, "2026-12-31", "2026-03-15", 2),
    ("v-pumps",   "Vale Pumps",      "D. Ruiz",   True,  "2025-11-30", "2026-02-10", 1),
    ("v-meter",   "MeterWorks",      "K. Sato",   True,  "2026-09-30", "2025-10-02", 0),
    ("v-integr",  "Northgate Integration", "S. Brandt", True, "2026-08-31", "2026-05-01", 19),
]
SESSIONS_EXPECTED = {"HydroLogic Ltd": 8, "ScadaCo": 4, "Vale Pumps": 2, "MeterWorks": 2, "Northgate Integration": 4}
for acct, sup, person, mfa, end, last, n90 in ACCOUNTS:
    f = []
    if not person: f.append("shared/unnamed account")
    if not mfa: f.append("no MFA")
    if dt.date.fromisoformat(end) < TODAY: f.append("contract ended - disable")
    if (TODAY - dt.date.fromisoformat(last)).days > 90: f.append("unused >90 days - disable")
    if n90 > 2 * SESSIONS_EXPECTED[sup]: f.append(f"{n90} sessions vs ~{SESSIONS_EXPECTED[sup]} expected - ask why")
    print(f"{acct:10s} {sup:22s} {'OK' if not f else '; '.join(f)}")
```

Expected output (Python 3.13.5):

```text
v-hydro1   HydroLogic Ltd         OK
v-hydro2   HydroLogic Ltd         shared/unnamed account
v-scadaco  ScadaCo                no MFA
v-pumps    Vale Pumps             contract ended - disable
v-meter    MeterWorks             unused >90 days - disable
v-integr   Northgate Integration  19 sessions vs ~4 expected - ask why
```

The coordinator's analysis, labelled:

- **Decided (by A. Mensah, 4 May):** disable `v-pumps` (Vale Pumps' contract ended in November) and `v-meter` (unused since October) today; replace `v-hydro2` with a named account within 14 days and restrict it meanwhile to supervised sessions.
- **Owed:** ScadaCo to enable MFA on `v-scadaco` within 30 days, or an exception to be proposed with compensating measures (Chapter 7); owner A. Mensah.
- **Open:** `v-integr` — Northgate Integration had 19 sessions in 90 days against about 4 expected. The coordinator **does not** conclude misuse. She asks J. Tan whether a project explains it and asks Northgate's account manager for the work log. J. Tan replies that Northgate is commissioning the new telemetry link at KW-11, which was approved in March; the work log matches 17 of 19 sessions. Two sessions on 12 and 19 April at 02:00 are not in the work log. Those two are passed to the security lead and KVROC for review of session records, under the incident escalation path, with the supplier informed only after the security lead agrees.
- **Assumed:** the gateway export is complete. (Next review: also compare against the firewall's allowed sources.)

The case shows the coordinator's discipline: act quickly on clear governance failures, ask before accusing, escalate the residual unexplained activity through the proper path, and record what is assumed.

### 8.5 Contract and onboarding requirements

From the case, the coordinator drafts standard clauses for new supplier contracts with remote access: named individuals only; MFA; sessions only through the utility's gateway, approved per session or per scheduled window; supplier to notify the utility within 24 hours of staff departure and promptly of any security incident that could affect the utility; work logs available on request; cooperation in incident response; deletion of utility data at contract end, confirmed in writing. ISA/IEC 62443 includes requirements for service providers and integrators that can inform such clauses ([ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Legal wording is for your legal team; your job is to specify the security outcome.

### 8.6 Supervised presentation

Present the case to your supervisor (here, E. Varga) in five parts: what was reviewed and under what authority; findings with evidence; decisions already taken and by whom; decisions requested from the supervisor (budget for MFA on ScadaCo's side, approval of contract clauses); and open questions with owners and dates.

Keep each part short and label it, so the supervisor can stop you at any point and still know what is decided and what is asked. In the May review, the two unexplained Northgate sessions belong under open questions with their owner, not under findings. Bring the Lab 8 output and the authorization as attachments, and state plainly what was assumed, such as that the gateway export was complete. End by repeating the decisions requested and the date by which they are needed.

### 8.7 Common errors and limits

- Treating unusual activity as proof of compromise — or ignoring it as "probably the project".
- Removing access needed for safety-critical support without a fallback.
- Reviews using only one source (accounts without contracts or sessions).
- Contract clauses that cannot be checked.
- The lab models one gateway; real environments have several access paths (dial-up, cellular modems, supplier-installed remote tools) that the review must find.

- Disabling an account for a supplier whose support is needed for a dosing problem in progress, without arranging an alternative.
- Closing a review once the obvious findings are fixed, while two unexplained sessions remain open without an owner.

### Exercises — chapter 8

**EX036 — Read Lab 8.** *Objective:* interpret review results. *Inputs:* Lab 8 output. *Steps:* for each account state the finding, risk and proportionate response with owner. *Expected evidence:* six rows. *Rubric:* 3 = matches 8.4 including restraint on `v-integr` and a fallback for `v-scadaco`; 2 = correct actions but accusatory on `v-integr`; 1 = disables everything; 0 = none.

**EX037 — Extend the review.** *Objective:* add a source. *Inputs:* Lab 8. *Steps:* add a "last staff confirmation" date per account and flag accounts whose supplier has not confirmed its staff list in 180 days; show output. *Expected evidence:* code and output. *Rubric:* 3 = field added for all rows with test values that trigger and do not trigger, output shown, explains why staff confirmation matters (departures); 2 = no explanation; 1 = rule only; 0 = none.

**EX038 — Draft contract clauses.** *Objective:* specify supplier obligations. *Inputs:* 8.5. *Steps:* write five checkable clauses in plain language. *Expected evidence:* clauses. *Rubric:* 3 = each clause has a measurable obligation and a way to verify (for example staff departure notice within 24 hours, verified at quarterly review); 2 = not checkable; 1 = "supplier will be secure"; 0 = none.

**EX039 — Handle the two night sessions.** *Objective:* escalate unexplained activity properly. *Inputs:* 8.4. *Steps:* write the message to the security lead and the decision you need. *Expected evidence:* message. *Rubric:* 3 = facts with times in UTC and source, what is known (17 of 19 explained), what is not, request for session-record review via escalation path, guidance not to alert the supplier yet, sensitive handling (TLP:RED or AMBER+STRICT), next check time; 2 = no handling guidance; 1 = "please investigate Northgate"; 0 = none.

**EX040 — Present the case.** *Objective:* supervised presentation. *Inputs:* 8.6. *Steps:* write the five-part briefing in under 300 words. *Expected evidence:* briefing. *Rubric:* 3 = all five parts, decisions requested explicitly, uncertainty labelled, no unsupported accusation; 2 = missing requested decisions; 1 = narrative only; 0 = none.

### Chapter synthesis

Supplier access is governed across a lifecycle — select, contract, onboard, operate, change, exit — and most failures sit at the joins. An access review reconciles accounts, contracts and sessions; respond proportionately, treat anomalies as questions, and escalate what remains unexplained through the proper path. Turn lessons into checkable contract requirements and present cases with decisions requested and uncertainty labelled.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 12

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes and connection

After this chapter you should be able to:

- identify every notification duty an incident can trigger — legal, regulatory, contractual, insurance — and run their clocks;
- write a holding statement and a critical-customer briefing that are accurate, useful and honest about uncertainty;
- apply ethical principles to communication: truthfulness, proportionality, fairness to individuals, and correction of errors;
- report incidents and programme status to executives and boards in a form that supports decisions.

Chapters 1–8 built and exercised the programme internally. This chapter faces outward.

### 9.1 Who must be told, and when

An incident at an essential service can start several clocks at once. Under NIS2, for example, entities must send the national CSIRT or competent authority an **early warning within 24 hours** of becoming aware of a significant incident, an **incident notification within 72 hours**, and a **final report within one month** after the notification ([Directive (EU) 2022/2555, Article 23](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). Other jurisdictions, sectors and contracts set different triggers and periods; personal-data breaches may carry separate duties; insurers usually require prompt notice. A coordinator prepares in advance a **notification register**: each duty, its trigger, recipient, deadline, content, owner and channel.

Two details decide whether you meet a clock: **what starts it** (detection, awareness, determination that the incident is "significant") and **who records that moment**. Agree both before incidents, and record the start time in UTC in the decision log.

### 9.2 Critical customers

Hospitals, care homes, dialysis patients, other utilities and emergency services may need to act before the public does. Their needs are practical: what is affected, what they should do, for how long, when the next update comes, and whom to call. Agreements with them (Chapter 2) often promise a call within a short period. Keep their contacts tested and keep the message free of technical detail.

Kestrel General Hospital's agreement promises a call within two hours of any event likely to affect supply or quality; its estates on-call, and out of hours the site duty manager, are the contacts.

### 9.3 Public communication

A **holding statement** is a short, factual message issued early, before the full picture is known. It says what is known, what the organization is doing, what (if anything) the public should do, and when more information will come. It does not speculate on cause or attribution, does not minimise ("no impact") without evidence, and does not reveal details useful to an attacker. The communications lead drafts; the accountable executive approves (Chapter 6); operations confirms any safety statement ("the water is safe to drink") is true.

### 9.4 Ethics

Communication about essential services carries public-safety weight. Four principles:

- **Truthfulness** — never state as fact what is assumed; never deny what you know.
- **Proportionality** — enough detail for people to protect themselves, no more; avoid causing unnecessary alarm and avoid helping attackers.
- **Fairness to individuals** — do not name or blame an employee or supplier publicly on incomplete information; human error is usually a system problem.
- **Correction** — when a statement turns out to be wrong, correct it promptly and visibly.

Internally, a **blameless** culture of reporting — people report mistakes and near misses without fear — gives the coordinator the early signals that external reporting depends on.

### 9.5 Worked example: the Saturday clocks (synthetic)

On Saturday 13 June 2026, at 21:40 UTC, the incident lead determines that unauthorised access to the supervisory network is a significant incident. Kestrel Vale's fictional rules mirror NIS2's 24 h / 72 h / one-month pattern; the hospital's agreement requires a call within 2 hours; the insurance policy requires notice within 48 hours. On Tuesday evening, the coordinator checks the register with **Lab 9**.

**Lab 9** (save as `lab09.py`, run with `python3 lab09.py`):

```python
# Lab 9 - notification clocks after an incident (offline, standard library only; synthetic obligations)
# The deadlines are ILLUSTRATIVE for the fictional Kestrel Vale jurisdiction; real duties come from your own
# law, regulator and contracts. The 24 h / 72 h / one-month pattern mirrors EU NIS2 Article 23.
from datetime import datetime, timedelta, timezone
UTC = timezone.utc
aware = datetime(2026, 6, 13, 21, 40, tzinfo=UTC)        # incident judged significant (Saturday evening)
OBLIGATIONS = [  # name, hours after awareness, recipient
    ("Critical-customer call (contract)", 2,      "Kestrel General Hospital"),
    ("Regulator early warning",          24,     "Kestrel Vale CSIRT"),
    ("Insurer notice (policy)",          48,     "insurer"),
    ("Regulator incident notification",  72,     "Kestrel Vale CSIRT"),
    ("Regulator final report",           24*30,  "Kestrel Vale CSIRT"),   # 'one month' modelled as 30 days
]
SENT = {"Critical-customer call (contract)": datetime(2026, 6, 13, 23, 55, tzinfo=UTC),
        "Regulator early warning": datetime(2026, 6, 14, 18, 5, tzinfo=UTC),
        "Regulator incident notification": datetime(2026, 6, 16, 22, 30, tzinfo=UTC)}
NOW = datetime(2026, 6, 16, 23, 0, tzinfo=UTC)
for name, h, who in OBLIGATIONS:
    due = aware + timedelta(hours=h)
    sent = SENT.get(name)
    if sent:
        delta = (sent - due).total_seconds() / 3600
        state = f"sent {sent:%a %d %H:%M}Z, {'LATE by' if delta > 0 else 'early by'} {abs(delta):.2f} h"
    else:
        state = "OVERDUE - not sent" if NOW > due else f"open, {(due - NOW).total_seconds()/3600:.1f} h left"
    print(f"{name:35s} due {due:%a %d %b %H:%M}Z  {state}")
```

Expected output (Python 3.13.5):

```text
Critical-customer call (contract)   due Sat 13 Jun 23:40Z  sent Sat 13 23:55Z, LATE by 0.25 h
Regulator early warning             due Sun 14 Jun 21:40Z  sent Sun 14 18:05Z, early by 3.58 h
Insurer notice (policy)             due Mon 15 Jun 21:40Z  OVERDUE - not sent
Regulator incident notification     due Tue 16 Jun 21:40Z  sent Tue 16 22:30Z, LATE by 0.83 h
Regulator final report              due Mon 13 Jul 21:40Z  open, 646.7 h left
```

Three problems emerge. The hospital call was 15 minutes late: the coordinator was on the call with the regulator's duty officer and the comms lead believed she would phone the hospital — the two-responsible defect from Chapter 6 in real life. The insurer was never notified: nobody had the policy in the notification register. The regulator's 72-hour notification was 50 minutes late because the chief executive's approval was sought at 21:00 for a 21:40 deadline. The early warning, prepared from a template, went in early.

The coordinator records these facts in the decision log without blame, notifies the insurer immediately with an explanation, and adds two actions for the review: put the insurance duty in the register with an owner, and set internal deadlines for approvals (for example "approval requested no later than 6 hours before the external deadline"). The lab computes clocks; it does not decide what counts as "aware" — that remains a documented judgement.

### 9.6 Reporting to executives and boards

A short incident report for executives covers: what happened (facts, labelled confidence); impact on service and people; what has been done and decided; duties met and missed; risks now; decisions needed. Programme reports (monthly or quarterly) use the decision-driving metrics of Chapter 5 and the top consequence-ranked risks of Chapter 4.

For the Saturday incident, the executive report would show that the hospital call was fifteen minutes late, the insurer was not told and the 72-hour notification was late, with the causes found rather than names. It would end with the two actions for the register and the approval deadlines, and ask the executive to confirm both. Keep it to one page and attach the clock calculations, so that a reader can check each time without trusting the summary.

### 9.7 Practical activity

Draft a notification register for an organization you know with at least five duties. For each, write what starts the clock and who records it. Mark any duty whose source you have not verified.

Include contracts and insurance as well as law, since the Saturday incident showed that an insurer's notice period can be missed simply because nobody listed it. For each duty, name an owner, set an internal deadline for approval ahead of the external one, and record the source document with its clause. Check whether two duties are started by the same moment; if so, agree who records that moment and in which time zone. Review the register whenever a contract or policy is renewed.

### 9.8 Common errors and limits

- Notification duties discovered during the incident.
- No internal deadline for approvals, so the external deadline is missed.
- Holding statements that promise "no impact" before evidence exists.
- Naming individuals or suppliers prematurely.
- Real legal duties vary; confirm yours with legal counsel and your regulator. This book's clocks are illustrative.

- Leaving one call, such as the hospital briefing, to two people who each assume the other will make it.
- Starting each clock from a different moment because nobody agreed what counts as aware.
- Forgetting contractual and insurance duties because the register lists only regulators.

### Exercises — chapter 9

**EX041 — Read Lab 9.** *Objective:* interpret notification clocks. *Inputs:* Lab 9 output. *Steps:* for each obligation, state the status and the root cause of any miss using 9.5. *Expected evidence:* five rows. *Rubric:* 3 = hospital late 0.25 h (unclear responsibility), early warning met, insurer overdue (not in register), notification late 0.83 h (late approval), final report open with 646.7 h; root causes are process, not people; 2 = statuses only; 1 = partial; 0 = none.

**EX042 — Write a holding statement.** *Objective:* communicate early and honestly. *Inputs:* the utility is investigating unauthorised access to systems that monitor water treatment; operations staff are running two stations manually; water quality tests are normal. *Steps:* write a statement under 120 words. *Expected evidence:* statement. *Rubric:* 3 = facts only, what is being done, what customers should do (nothing unless advised; how updates will come), next update time, no speculation or attacker-useful detail, safety statement only as confirmed by operations; 2 = minor speculation; 1 = "no impact, all fine"; 0 = none.

**EX043 — Brief the hospital.** *Objective:* critical-customer communication. *Inputs:* same incident; east zone pressure may drop for up to 4 hours tomorrow during a controlled switchover. *Steps:* write the call script. *Expected evidence:* script. *Rubric:* 3 = effect in hospital terms, timing, safety of water, what the hospital may need to do (stored water, priorities), next update, 24 h contact; asks what the hospital needs; 2 = no question to the hospital; 1 = technical detail; 0 = none.

**EX044 — Ethical dilemma.** *Objective:* apply principles. *Inputs:* a journalist asks whether a supplier's engineer caused the incident; internal evidence suggests the supplier's stolen laptop was involved, unconfirmed. *Steps:* write the answer and justify. *Expected evidence:* answer and reasoning. *Rubric:* 3 = declines to attribute or name on unconfirmed information, explains investigation ongoing, commits to update, reasoning cites truthfulness and fairness; 2 = correct answer without reasoning; 1 = names supplier; 0 = none.

**EX045 — Fix the approval process.** *Objective:* prevent late notifications. *Inputs:* 9.5. *Steps:* design internal deadlines and delegation for the three external clocks. *Expected evidence:* design. *Rubric:* 3 = internal deadlines before each external one, named deputy approvers when the chief executive is unavailable, templates prepared, clock start recorded in UTC by the incident lead, insurer added to register; 2 = deadlines only; 1 = "be faster"; 0 = none.

### Chapter synthesis

Incidents start several clocks at once; know them in advance, agree what starts each and who records it, and set internal approval deadlines ahead of external ones. Critical customers need practical messages early; the public needs truthful, proportionate holding statements. Communicate without blame or speculation, correct errors visibly, and report to executives with facts, impact, decisions and duties.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue studying — chapter 09 of 12

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Critical infrastructure and sector security: quality and troubleshooting

### Learning outcomes and connection

After this chapter you should be able to:

- recognise the common failure patterns of security coordination programmes;
- troubleshoot a coordination failure methodically — symptom, hypotheses, evidence, cause, fix — instead of blaming people;
- measure the quality of decisions in an exercise or incident, not only their speed;
- run a corrective-action process that actually closes actions.

Chapter 9 exposed real coordination failures. This chapter treats the programme itself as a system that can be diagnosed and improved.

### 10.1 How programmes fail

Most coordination failures fall into a few patterns:

- **Ownership gaps** — activities or risks with no accountable person (Chapters 4 and 6).
- **Duplicated responsibility** — two people each think the other acted.
- **Stale information** — contacts, dependency maps, supplier lists or registers that were right last year.
- **Paper controls** — documented but never observed or tested (Chapter 7).
- **Bottlenecks** — one person on every critical path.
- **Action decay** — lessons identified after every exercise, never implemented.
- **Speed without quality** — decisions taken on time but without rationale, wrong information or the right people.

### 10.2 Troubleshooting a coordination failure

Use the same discipline engineers use for technical faults:

1. **State the symptom** precisely ("the hospital was called 15 minutes after the contractual 2 hours").
2. **List hypotheses** ("nobody owned the call"; "contact number wrong"; "the 2-hour clock started at a different moment for different people").
3. **Gather evidence** — decision logs, call records, interviews — without blame.
4. **Eliminate** hypotheses the evidence contradicts.
5. **Fix the cause**, not the symptom, and decide how you will verify the fix.

A useful habit: ask "what made this the reasonable thing to do at the time?" People rarely act carelessly in a crisis; they act on the information and roles they had.

### 10.3 Decision quality

Timeliness is easy to measure; quality is harder but more important. For each key decision in an exercise or incident, check: Did it have an owner? Was it taken within the target time? Was the rationale recorded? Were the people who needed to be consulted, consulted? Was it based on verified information, with assumptions labelled? NIST's guide to test, training and exercise programmes describes evaluating exercises against objectives and capturing lessons ([NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final)).

### 10.4 Worked example: the May tabletop log (synthetic)

In the May tabletop exercise DRY CREEK (its design is the worked example of Chapter 11), an evaluator kept a decision log. **Lab 10** checks it.

**Lab 10** (save as `lab10.py`, run with `python3 lab10.py`):

```python
# Lab 10 - tabletop decision-log quality check (offline, standard library only; synthetic exercise log)
import csv, io
LOG = """minute,inject,decision,owner,target_min,taken_min,recorded_rationale
0,I1 HMI shows unexpected setpoint change,convene incident team,Coordinator,15,9,yes
20,I2 vendor reports stolen laptop,suspend vendor remote access,Ops manager,30,52,yes
35,I3 station KW-04 dosing alarm,switch KW-04 to manual,Ops manager,10,6,no
50,I4 journalist calls,holding statement,,30,41,yes
65,I5 hospital asks about water safety,brief hospital,Coordinator,20,,no
80,I6 regulator early-warning clock,send early warning,Coordinator,60,44,yes
"""
rows = list(csv.DictReader(io.StringIO(LOG)))
met = 0
for r in rows:
    f = []
    if not r["owner"]: f.append("no owner")
    if not r["taken_min"]: f.append("no decision taken")
    elif int(r["taken_min"]) > int(r["target_min"]): f.append(f"late {int(r['taken_min'])-int(r['target_min'])} min")
    else: met += 1
    if r["recorded_rationale"] != "yes": f.append("no rationale recorded")
    print(f"{r['inject'][:2]} {r['decision']:30s} {'ok' if not f else '; '.join(f)}")
print(f"decisions within target: {met}/{len(rows)}")
```

Expected output (Python 3.13.5):

```text
I1 convene incident team          ok
I2 suspend vendor remote access   late 22 min
I3 switch KW-04 to manual         no rationale recorded
I4 holding statement              no owner; late 11 min
I5 brief hospital                 no decision taken; no rationale recorded
I6 send early warning             ok
decisions within target: 3/6
```

The headline "3/6 within target" hides more than it shows:

- I3's decision to switch KW-04 to manual was fast (6 minutes against 10) and counted as on time, but **no rationale was recorded**. For a safety-related decision, that matters: in a real incident, the review would not know whether it was taken because of dosing data, a precaution or a guess.
- I4's holding statement had **no owner** — the communications defect from Chapter 6 again — and was late.
- I5, the hospital briefing, **was never decided**. In the hot wash, players said they "assumed comms had it".
- I2, suspending vendor access, was 22 minutes late. Players explained that nobody knew whether suspending HydroLogic's access would stop support for a dosing problem then in progress. That is a **missing information** cause, not slowness.

The coordinator's troubleshooting table:

| Symptom | Hypotheses | Evidence | Cause | Fix | Verify by |
|---|---|---|---|---|---|
| I5 hospital briefing not done | No owner; contact unknown; forgotten under load | Hot wash: "assumed comms had it"; RACI had two R | Duplicated responsibility | Single lead in RACI; hospital call on the incident checklist | Next exercise inject on hospital |
| I2 vendor suspension late | Approval unclear; impact unknown | Players asked who depends on HydroLogic access | Missing dependency information | Add "who depends on this supplier's access" to supplier register | Lab 8 review includes dependency column |
| I3 no rationale | Log template lacks field; time pressure | Template has no rationale column | Tool design | Add rationale field; scribe role | Lab 10 rerun shows rationale |

### 10.5 Closing corrective actions

Lessons do not improve anything until they become actions with owners, dates and verification — and are closed. Track them in one place, review them at the risk committee, and verify each closure with evidence (the next exercise, a test, a document). A useful programme metric is the percentage of exercise actions closed and verified within their due date.

In the DRY CREEK review, each fix has a matching verification: the next exercise inject on the hospital, a supplier register with a dependency column checked in the next access review, and a rerun of Lab 10 showing recorded rationales.

### 10.6 Practical activity

Take a recent failure in any team you know (a missed deadline, a duplicated task). Fill the troubleshooting table without naming individuals and propose a fix with a verification method.

Write the symptom as a precise fact with times or counts, as in the hospital example, rather than a judgement. List at least three hypotheses before looking for evidence, and note which evidence ruled each one out. Ask what made the action reasonable for the people involved at the time. Then choose a fix that changes a role, a tool or information, not one that asks people to try harder, and say how you will know it worked, for example in the next exercise or review.

### 10.7 Common errors and limits

- Reporting exercise success as speed alone.
- Concluding "human error" and stopping.
- Fixes that are exhortations ("communicate better").
- Actions without verification, closed on the owner's word.
- Over-correcting with heavy process that slows real responses; keep fixes proportionate.

- Fixing the symptom, such as reminding staff to call the hospital, while the RACI still lists two responsible people.
- Counting a fast decision as good when no rationale was recorded, as with the KW-04 switch to manual in DRY CREEK.
- Tracking actions in several places so that nobody can see which are overdue.

### Exercises — chapter 10

**EX046 — Read Lab 10.** *Objective:* interpret decision quality. *Inputs:* Lab 10 output. *Steps:* explain why "3/6 within target" overstates performance and name the most serious defect. *Expected evidence:* explanation. *Rubric:* 3 = I3 counted on time without rationale; I5 not taken at all (critical-customer risk); I4 unowned; most serious is I5 or I3 with reasoning; 2 = lists defects without judgement; 1 = accepts 3/6; 0 = none.

**EX047 — Add a quality rule.** *Objective:* encode another check. *Inputs:* Lab 10. *Steps:* add `safety` and `consulted` columns; flag any safety-related decision whose owner is not the operations manager and where the operations manager was not consulted; test with the six original rows plus one invented row in which the security lead decides to isolate a station without consulting operations; show the output. *Expected evidence:* code and output. *Rubric:* 3 = columns populated for all rows, rule restricted to safety decisions, the invented row flagged and I3 (owned by operations) not flagged, with that result explained; 2 = rule flags every row lacking a consulted entry; 1 = rule only; 0 = none.

**EX048 — Troubleshoot I4.** *Objective:* apply 10.2. *Inputs:* I4 row and Chapter 6 RACI. *Steps:* fill the troubleshooting table for the holding statement. *Expected evidence:* one table row with hypotheses. *Rubric:* 3 = at least two hypotheses, evidence (RACI had no A for public statement), cause, fix (CEO A, comms R, template), verification (next exercise); 2 = no verification; 1 = "comms were slow"; 0 = none.

**EX049 — Diagnose stale information.** *Objective:* recognise decay. *Inputs:* in an incident, the hospital's out-of-hours number reached a disconnected line. *Steps:* propose a cause analysis and a durable fix. *Expected evidence:* analysis and fix. *Rubric:* 3 = cause: no owner or schedule for contact verification; fix: owned quarterly test calls, update on hospital reorganisations, second contact route; verification metric; 2 = one-off update; 1 = blame; 0 = none.

**EX050 — Close actions.** *Objective:* design corrective-action tracking. *Inputs:* the three fixes in 10.4. *Steps:* write an action log with owner, due date, evidence of closure and verification method. *Expected evidence:* log. *Rubric:* 3 = each has an owner with authority, realistic date, closure evidence distinct from owner's statement, and verification in a later exercise or review; 2 = no verification; 1 = list only; 0 = none.

### Chapter synthesis

Coordination programmes fail in recognisable ways — ownership gaps, duplicated responsibility, stale information, paper controls, bottlenecks, action decay and speed without quality. Troubleshoot them like faults, from symptom through hypotheses and evidence to cause, without blame. Measure decision quality, not just speed, and close corrective actions only with verified evidence.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue studying — chapter 10 of 12

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes and connection

After this chapter you should be able to:

- design a discussion-based **tabletop exercise** for an essential service, with objectives, scenario, injects, roles and evaluation criteria;
- facilitate it safely and fairly, keeping it a test of plans rather than of people;
- evaluate it with a hot wash, an after-action report and an improvement plan;
- assess an exercise design against a rubric under supervision.

For a professional coordinator, the laboratory is the exercise room. This chapter assembles everything so far — stakeholders, authorization, risk, RACI, supplier access, notification clocks, decision quality — into one supervised exercise.

### 11.1 Types of exercise

Exercise programmes distinguish **discussion-based** exercises (seminars, workshops, tabletops), where participants talk through a scenario, from **operations-based** exercises (drills, functional exercises, full-scale exercises), where they carry out actions. The US Homeland Security Exercise and Evaluation Program (HSEEP) sets out this progression and a design–conduct–evaluate–improve cycle ([FEMA, HSEEP](https://www.fema.gov/emergency-managers/national-preparedness/exercises/hseep)). NIST's guide covers test, training and exercise programmes for IT plans ([NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final)). CISA publishes ready-made tabletop exercise packages for critical-infrastructure scenarios ([CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages)), and the UK NCSC offers "Exercise in a Box" ([NCSC, Exercise in a Box](https://www.ncsc.gov.uk/information/exercise-in-a-box)).

A tabletop is the right first step: cheap, safe — nothing touches a live system — and excellent at exposing gaps in roles, information and communication.

### 11.2 Design

A design document has seven parts:

1. **Objectives** — three to five, each **observable**: "Within 30 minutes of the relevant inject, the team decides whether to suspend supplier access, with owner and rationale recorded." Avoid "test our response".
2. **Scope and assumptions** — which plans are tested, which teams play, what is out of scope ("the technical forensic process is not played").
3. **Scenario** — plausible, synthetic, sector-appropriate, based on public threat information at a general level; never a real colleague's mistake.
4. **Injects** — timed pieces of new information (an alarm, a phone call, a journalist, a regulator deadline). Each inject maps to at least one objective and has an expected decision.
5. **Roles** — players (decide as they would), facilitator (runs the clock, presents injects, keeps discussion moving), evaluators (observe against objectives, keep the decision log), scribe, and a **safety officer** or trusted agent who can pause the exercise.
6. **Evaluation criteria** — what "met", "partially met" and "not met" mean for each objective.
7. **Logistics and rules** — date, room, no real systems touched, "exercise, exercise, exercise" on every written inject so nothing can be mistaken for a real event, and a real-world stop phrase.

### 11.3 Facilitation

Open with ground rules: this tests plans, not people; there are no trick questions; decide as you would in reality; say when you would need information you do not have. Keep the clock honest and resist rescuing players — if the team has no way to reach the hospital, the gap is the finding. Record decisions, not opinions about performance.

In DRY CREEK the facilitator did not supply the missing hospital contact or assign the call when players hesitated; that silence produced the clearest finding of the exercise.

### 11.4 Evaluation and improvement

Immediately after: a **hot wash** — each participant says what worked and what did not. Within two weeks: an **after-action report** (AAR) that rates each objective with evidence from the decision log, and an **improvement plan** that turns findings into owned, dated, verifiable actions (Chapter 10). The AAR is shared at the appropriate TLP level; it names gaps in plans and tools, not individuals.

The DRY CREEK report rated O3 as not met and turned it into one action with an owner, a date and a re-test inject.

### 11.5 Worked example: exercise "DRY CREEK" (synthetic)

**Objectives.** (O1) Declare or decline a cyber incident within 15 minutes of the first indicator, with rationale. (O2) Decide on suspending a supplier's remote access within 30 minutes, knowing which operations depend on it. (O3) Brief the hospital within its 2-hour agreement, with one named lead. (O4) Meet the illustrative regulator early-warning deadline with an approved message. (O5) Issue a holding statement with an accountable approver within 45 minutes of media contact.

**Scenario.** On a Friday evening, a HydroLogic engineer's laptop is reported stolen; an hour later, KVROC reports a remote session to station KW-04 from HydroLogic's account at an unusual hour, and an operator sees an unexpected change of dosing setpoint, which the controller's limits reject. All synthetic.

**Inject table (extract).**

| Time | Inject | Objectives | Expected decision |
|---|---|---|---|
| 00:00 | KVROC call: unusual supplier session to KW-04 | O1 | Convene incident team; record start time |
| 00:10 | Operator: setpoint change attempted, rejected by limits | O1 | Declare incident; operations safety assessment |
| 00:20 | HydroLogic: engineer's laptop stolen yesterday | O2 | Suspend HydroLogic access; arrange alternative support for dosing |
| 00:40 | Hospital estates calls asking about rumours | O3 | Named lead briefs hospital; next update set |
| 00:55 | Local journalist calls comms | O5 | Holding statement approved by chief executive |
| 01:20 | Facilitator: "it is now 20 hours since determination" | O4 | Early warning approved and sent |

**Roles.** Players: E. Varga (executive), A. Mensah, L. Ferreira, R. Adeyemi, the on-call engineer, M. Holt joining at 00:55. Facilitator: the coordinator. Evaluators: an internal auditor and a peer coordinator from a neighbouring utility under a confidentiality agreement. Safety officer: shift supervisor, with the stop phrase "real world, real world".

**Evaluation (from the evaluator's log, analysed with the Lab 10 method).** O1 met (9 minutes, rationale recorded). O2 partially met — decision at 52 minutes because nobody knew who else relied on HydroLogic's access. O3 not met — the hospital call was never assigned. O4 met. O5 partially met — statement issued late, no owner until the chief executive arrived. These findings fed directly into the corrective actions of Chapter 10.

### 11.6 Exercise-design rubric

| Criterion | 3 (excellent) | 1 (weak) |
|---|---|---|
| Objectives | Observable, time-bound, linked to plans | "Test response" |
| Scenario | Plausible, synthetic, sector-specific, proportionate | Hollywood or a real colleague's error |
| Injects | Each mapped to objectives with expected decisions | Random surprises |
| Roles and safety | Facilitator, evaluators, safety officer, stop phrase; no live systems | Players evaluate themselves; live systems touched |
| Evaluation | Criteria in advance; decision log; AAR and improvement plan with owners | Feelings-based debrief |
| Ethics | Tests plans, not people; findings anonymised | Scores individuals |

Use the rubric on the DRY CREEK design: its objectives are observable and time-bound, each inject maps to one.

### 11.7 Practical activity (supervised)

Design a 90-minute tabletop for an essential service of your choice using the seven parts of 11.2, with at least four objectives and six injects. Ask your supervisor or a peer to score it against the rubric before you run it.

Base the scenario on public threat information at a general level, as DRY CREEK used a stolen supplier laptop and an unusual remote session, and never on a real colleague's mistake. Map every inject to an objective with an expected decision, and name a safety officer with a stop phrase. Mark every written inject as an exercise. After scoring, revise the design and record what the reviewer changed, so the supervisor can see how feedback was used.

### 11.8 Common errors and limits

- Too many objectives; nothing is evaluated properly.
- Scenarios so severe that every plan fails and nothing specific is learned.
- Facilitators who rescue players or let senior people dominate.
- Exercise injects that could be mistaken for real messages.
- AARs that never become actions.
- A tabletop shows whether plans and roles make sense; it does not show that procedures can be carried out at speed — that needs drills.

- Choosing evaluators who are also players, so nobody observes the decisions independently.
- Ignoring a hot-wash remark such as "we assumed comms had it", which in DRY CREEK pointed to the real cause.

### Exercises — chapter 11

**EX051 — Make objectives observable.** *Objective:* write evaluable objectives. *Inputs:* "Test our communication", "Check supplier management", "See if people know the plan". *Steps:* rewrite each. *Expected evidence:* three objectives. *Rubric:* 3 = each states a decision or action, a time limit and what is recorded; 2 = no time limits; 1 = still vague; 0 = none.

**EX052 — Write injects.** *Objective:* map injects to objectives. *Inputs:* DRY CREEK objectives. *Steps:* write two new injects that test O2 and O4 more deeply, with expected decisions. *Expected evidence:* two inject rows. *Rubric:* 3 = plausible, synthetic, each mapped with expected decision (for example HydroLogic asks to reconnect to fix dosing; regulator duty officer asks for an update before the deadline); marked "exercise"; 2 = unmapped; 1 = unrealistic; 0 = none.

**EX053 — Score a design.** *Objective:* apply the rubric. *Inputs:* a colleague's design: one objective "test incident response"; scenario is a nation-state attack causing a dam failure; the CEO evaluates; injects sent from the CEO's real email account. *Steps:* score each criterion and propose fixes. *Expected evidence:* scores and fixes. *Rubric:* 3 = low scores on objectives, scenario proportion, roles/evaluation independence and safety (real email risks confusion); fixes for each; 2 = fixes without scores; 1 = accepts; 0 = none.

**EX054 — Write the AAR summary.** *Objective:* evaluate against objectives. *Inputs:* DRY CREEK evaluation in 11.5. *Steps:* write the AAR summary table with rating, evidence and recommended action per objective. *Expected evidence:* five rows. *Rubric:* 3 = ratings consistent with evidence, actions owned and verifiable, no individual blamed; 2 = actions vague; 1 = narrative; 0 = none.

**EX055 — Facilitation challenge.** *Objective:* handle a facilitation problem. *Inputs:* in the exercise, the chief executive dominates and decides everything, including technical isolation. *Steps:* describe what the facilitator does during and after. *Expected evidence:* actions. *Rubric:* 3 = during: invite role owners by name, ask "who would decide this in reality?", record; after: raise in AAR as a plan/role clarity finding, brief the executive privately and respectfully; 2 = only after; 1 = ignores; 0 = none.

### Chapter synthesis

A tabletop exercise is the coordinator's laboratory: safe, cheap and powerful at exposing gaps in roles, information and communication. Design it with observable objectives, a plausible synthetic scenario, injects mapped to objectives, independent evaluators and a safety officer. Facilitate to test plans, not people; evaluate with a hot wash, an after-action report and an improvement plan whose actions are owned and verified.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue studying — chapter 11 of 12

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes and connection

After this chapter you should be able to:

- assemble a professional portfolio that shows, with evidence, what you can do as a coordinator;
- brief a board on critical-infrastructure security in ten minutes with decisions requested;
- write a realistic 90-day plan for a new coordination role;
- assess your own work against the course outcome and identify what you still need to learn.

This chapter closes the course: it pulls the outputs of Chapters 1–11 together and tests whether you can **operate a repeatable workflow and communicate findings**.

### 12.1 The portfolio

A coordinator's portfolio is not a certificate; it is a set of work products that someone else could check. Build it from the exercises you completed, sanitised and clearly marked as course work on synthetic data:

| Artefact | From chapter | What it shows |
|---|---|---|
| Dependency and stakeholder map | 2 | You can see the service and its people |
| Authorization and decision record | 3 | You make work and decisions accountable |
| Risk register extract with ranking rule | 4 | You can rank by consequence and keep hygiene |
| Metrics set with thresholds | 5 | You measure what drives decisions |
| Corrected RACI and escalation card | 6 | You make roles unambiguous |
| Control cards and verification plan | 7 | You know the difference between stated and tested |
| Supplier-access case briefing | 8 | You can analyse and present a case fairly |
| Notification register and holding statement | 9 | You can face outward honestly and on time |
| Troubleshooting table and action log | 10 | You improve the programme, not just report it |
| Tabletop design, AAR and improvement plan | 11 | You can test the whole system safely |

Add a one-page **reflection**: what you would do differently, and one area you need to learn more about (for example, technical OT fundamentals from the technical course, or legal duties in your jurisdiction).

### 12.2 The board briefing

Boards of essential-service operators increasingly carry explicit responsibility for cybersecurity risk management (for example NIS2's requirements on management bodies, [Directive (EU) 2022/2555, Article 20](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)). A ten-minute briefing has five parts:

1. **Context** — the service, the consequence that matters, and the threat picture at the level of public advisories.
2. **Where we stand** — top consequence-ranked risks with owners and dates; assurance levels of the key controls.
3. **What we learned** — the last exercise or incident, in two or three findings.
4. **What we are doing** — the plan, with progress against it.
5. **What we need from you** — decisions: risk acceptances, budget, appetite statements, priorities.

Avoid jargon, single scores and fear. Boards act on clear consequences, credible plans and specific requests.

### 12.3 The 90-day plan

A new coordinator's first 90 days, distilled from this book:

- **Days 1–30: listen and map.** Meet every "decides" and "must be told" stakeholder; draft the dependency map; read the risk register, incident history and supplier list; record what is assumed.
- **Days 31–60: fix ownership.** Owners for every level-5 risk; a RACI for incidents; an escalation card; a notification register; a first supplier-access review.
- **Days 61–90: test and report.** A first tabletop on the most likely high-consequence scenario; an AAR and improvement plan; a first board briefing with decisions requested.

Resist the temptation to start with a new framework, a new tool or a long policy. Ownership, information and rehearsal first.

### 12.4 Worked example: the October board briefing (synthetic)

The coordinator's ten-minute briefing to Kestrel Water's audit and risk committee, chaired by T. Lindqvist, in summary:

1. *Context.* "Our job is safe water for 180,000 people, including Kestrel General Hospital. Public advisories describe attacks on internet-exposed water controllers ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)); we have checked and have none exposed, confirmed in September."
2. *Where we stand.* "Three risks could affect health or the hospital; all now have owners. Supplier MFA is in place for five of six suppliers and verified by test for two; restore of the historian was tested in August in 19 hours against a 24-hour objective."
3. *What we learned.* "Exercise DRY CREEK showed we did not know who calls the hospital and that suspending a supplier is slow when we don't know who depends on it. Both are fixed; we will retest in January."
4. *What we are doing.* "Five of seven exercise actions closed and verified; two due in November."
5. *What we need.* "First, accept the KW-10 controller exception until March, with compensating measures. Second, approve the supplier contract clauses for all renewals. Third, set an appetite statement: no level-5 risk without a funded treatment for more than 12 months."

Every number has a source in the portfolio. Nothing is a single score.

### 12.5 Final review

The course outcome asks you to operate a repeatable workflow and communicate findings. Check yourself against the cycle:

- **Frame and identify** — can you describe a service by consequence and find risks in conversation?
- **Analyse and decide** — can you write ownable risks, rank them reproducibly and record decisions and acceptances?
- **Organise** — can you assign roles, govern change and escalate?
- **Verify** — can you distinguish stated from tested and design proportionate checks?
- **Communicate** — can you meet clocks and brief customers, the public and the board honestly?
- **Improve** — can you test with an exercise and close actions with evidence?

Where the answer is "not yet", the chapter number tells you where to return.

### 12.6 Practical activity

Assemble your portfolio from your exercise answers. Ask a peer to review it against the final rubric (EX060) and to try to verify three claims from your evidence alone.

Choose claims that matter, such as "supplier MFA verified by test for two suppliers" or "historian restored in 19 hours", and see whether your peer can find the record, date and owner behind each from the portfolio alone. Where they cannot, fix the evidence rather than the wording. Mark every item clearly as course work on synthetic data, and remove anything that could identify a real organization or person before you share it.

### 12.7 Common errors and limits

- Portfolios of certificates instead of work products.
- Board briefings without requests.
- 90-day plans that start with tools.
- Presenting synthetic course work as real organizational findings.
- This course does not make you a technical OT specialist or a lawyer; know when to call one.

- Reporting a claim to the board without a source in the portfolio, so nobody can check it later.
- Asking the board for a decision without saying what happens if it declines, such as how long the KW-10 exception would otherwise run.
- Updating the portfolio once and letting it go stale after the course ends.

### Exercises — chapter 12

**EX056 — Portfolio index.** *Objective:* assemble evidence. *Inputs:* your exercise answers. *Steps:* produce the portfolio index with artefact, chapter, and the claim each supports. *Expected evidence:* index of at least eight artefacts. *Rubric:* 3 = each artefact linked to a specific claim and exercise, sanitised and labelled synthetic; 2 = index without claims; 1 = list of chapters; 0 = none.

**EX057 — Board briefing.** *Objective:* communicate to governance. *Inputs:* 12.2 and your portfolio. *Steps:* write the briefing script (max. 600 words). *Expected evidence:* script. *Rubric:* 3 = five parts, consequences in plain language, sourced numbers, assurance levels stated, three specific requests; no single score; 2 = no requests; 1 = technical report; 0 = none.

**EX058 — 90-day plan.** *Objective:* plan a role. *Inputs:* a new coordinator post at a regional hospital trust. *Steps:* write the 90-day plan with three phases and deliverables. *Expected evidence:* plan. *Rubric:* 3 = adapts to healthcare (clinical leadership as decision-makers, medical devices, patient safety, critical internal dependencies), ownership before tools, exercise and board report by day 90; 2 = generic; 1 = tool-first; 0 = none.

**EX059 — Verify a claim.** *Objective:* test evidence. *Inputs:* the claim "restore of the historian was tested in August in 19 hours". *Steps:* list the evidence you would expect in the portfolio to support it and two questions a sceptical auditor would ask. *Expected evidence:* list and questions. *Rubric:* 3 = test plan, authorization, timed log, result record, data-completeness check; questions about scope (full or partial restore) and environment (isolated or production-like); 2 = evidence only; 1 = "trust the engineer"; 0 = none.

**EX060 — Self-assessment.** *Objective:* reflect against the course outcome. *Inputs:* 12.5. *Steps:* rate yourself 0–3 on the six cycle areas with evidence for each and a learning plan for the two lowest. *Expected evidence:* six ratings and a plan. *Rubric:* 3 = honest ratings each backed by a portfolio artefact, specific learning plan with resources and dates; 2 = ratings without evidence; 1 = all 3s; 0 = none.

### Chapter synthesis

A professional coordinator shows competence through checkable work products: maps, records, registers, RACIs, control cards, case briefings, notification registers, exercise reports and improvement plans. Brief boards with consequences, evidence and specific requests; start a new role with ownership, information and rehearsal; and assess yourself honestly against the full cycle — frame, decide, organise, verify, communicate, improve.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue studying — chapter 12 of 12

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

These are model answers. A different answer that meets the rubric's standard of evidence and honesty about limits earns full credit. All organizations, people and data are synthetic.

### Chapter 1

**EX001.** (1) "Because office and control-room computers share a network and unpatched remote-desktop services, ransomware entering through phishing could encrypt the operator workstations at KW-TW, forcing manual operation of treatment for days and risking supply to 180,000 people." (2) "Because the control-room PCs run an unsupported operating system for which no fixes are issued, a known flaw could be used to disable the operator screens, causing loss of view of dosing and pressure until replacements are installed." (3) "Because a pump supplier's remote account has no second factor, anyone with its password could log in to station controllers and change pump setpoints, causing loss of pressure to up to 20,000 customers including the hospital." Each names cause, event and consequence in people or time.

**EX002.** (c) first: an unapproved chlorine change threatens health directly. (b) second: 40 minutes without view means operators cannot see or correct the process, and it may indicate interference. (d) third: the diagram helps an attacker plan and must be recalled and assessed. (a) fourth for operational consequence — but it may carry personal-data notification duties with short deadlines, so it can be first in **urgency of action** for the legal team. Ranking by consequence does not mean ignoring duties.

**EX003.** To IT: "Thank you — I can't sign this off alone, because it runs on operator workstations and could affect the control system. The decision is A. Mensah's as owner. Could you ask the control-system supplier whether the product is supported, and propose a test on a non-production machine with a rollback plan? I'll book 30 minutes with Operations next Tuesday." To A. Mensah: a summary, the request, and the proposed date. Full credit requires no sole sign-off and a named owner.

**EX004.** Antivirus: Protect (platform security) and Govern (who decides on changes to operational systems). Risk score: Govern (risk management strategy, oversight). Supplier logins: Govern (supply-chain risk management), Identify (asset and risk), Protect (identity and access). A label shows where the topic sits, not whether anything works.

**EX005.** Risk: "Because the station door is propped open at night, an unauthorised person could enter KW-03 and tamper with control equipment, causing unsafe operation or loss of supply." Owner: operations manager (or station manager). Question: "How slow is the reader, and is the door also used as an emergency exit or for deliveries at night?" — the fix may be a faster reader, not a reprimand.

### Chapter 2

**EX006.** Regulator: must be told; can help (guidance). KVROC: does (monitoring); can help; shared dependency. HydroLogic: does; upstream dependency; must be told about relevant incidents under contract. School: is affected; possibly must be told if it hosts vulnerable people (local policy). Chief executive: decides. Kestrel Grid control room: upstream dependency; can help (restoration priorities); must be told when large load changes are planned.

**EX007.** Carrier: losing it removes telemetry from all twelve stations at once — operators lose view everywhere; question: is there a second path or a manual-reading plan? KVROC: an outage or compromise affects three utilities and reduces detection; question: what happens to monitoring if KVROC is unavailable, and who else depends on it? HydroLogic engineer: key-person risk — illness or departure leaves no one able to fix stations; question: is knowledge documented and is there a second engineer? The common question: "What else uses that?"

**EX008.** "Kestrel Water to Hospital Estates: from 10:00 today for about six hours we are running the pumping station that serves your site under manual control as a precaution. Water remains safe to drink. Pressure may be slightly lower; we do not expect an interruption. Please make sure your stored-water plan is ready in case. Next update by 12:00 or sooner if anything changes. Contact: duty coordinator, [24 h number]." (Under 80 words, no technical detail.)

**EX009.** Ask the estates manager for the relevant section of the hospital's continuity plan or a short meeting; record date and source; change the entry from "assumed" to "verified (source, date)". If the real figure is 2 hours, a promise to call "within 2 hours" leaves no time to act: renegotiate to a much shorter notification (for example 30 minutes), plan alternative supply with the hospital (tankers, priority valves), and raise a level-5 risk for the dependency.

**EX010.** Water utility: if billing, scheduling or remote monitoring are encrypted, managers may stop or restrict automated operation as a precaution against spread and because they cannot see or charge for service; operation may continue manually. Fuel pipeline: CISA's advisory AA21-131A describes DarkSide ransomware targeting a critical-infrastructure company's IT network and urges measures to prevent business disruption; operations can be halted when business systems needed to run them are unavailable or when the operator chooses caution. Full credit avoids claiming the control systems were compromised and stays at the advisory's level.

### Chapter 3

**EX011.** Missing: purpose; exact systems and exclusions; permitted and prohibited activities; named testers and supervisor; window with time zone; stop conditions; data handling; written authority (chat is not a record; who at Northgate countersigns?). Rewrite: "Purpose: assess exposure of the supervisory network from the office network. In scope: firewall between office and supervisory zones, two supervisory servers at KW-TW. Out of scope: station controllers, dosing system, safety interlocks. Permitted: configuration review, passive traffic review from an approved mirror port; prohibited: active scanning of controllers, exploitation, any write. People: S. Brandt (Northgate), supervised by J. Tan. Window: 9 June 2026 09:00–15:00 local. Stop: any alarm, loss of view, operator request. Data: report TLP:AMBER+STRICT via secure transfer; working notes deleted within 14 days. Authority: A. Mensah (signed), Northgate service manager (countersigned)."

**EX012.** Decision: keep KW-05 in automatic. By: duty manager, under the operations incident procedure, 02:10 local. Options: (a) manual operation — 90-minute callout, risk of handling errors at night; (b) stay automatic with watch — chosen. Known: one unexplained remote login at 01:52; dosing values normal; limits active. Unknown: whether the login was malicious; whether the account was misused elsewhere. Conditions: operator to watch dosing and pressure every 15 minutes; switch to manual on any unexpected change; revisit at 06:00 with security lead. Informed: security lead, incident lead, operations manager (message 02:15).

**EX013.** (a) TLP:GREEN — the sector benefits and the information is not specific to the utility. (b) TLP:AMBER+STRICT (or RED if only named KVROC analysts need it) — it reveals the utility's weaknesses. (c) TLP:CLEAR — intended for the public.

**EX014.** One access-controlled record library with folders per record type: authorizations and decision records (owner: coordinator); risk acceptances and exceptions (owner: coordinator, decisions by named authorities, linked from board minutes); exercise reports (owner: coordinator); supplier access lists (owner: operations manager; exported from the gateway, never emailed). Version history on, retention per policy, access reviewed twice a year.

**EX015.** Stop if: any unexpected alarm at KW-09 or its neighbours; any loss of view on operator screens; the update runs beyond 15:00; the controller does not return to its expected state within the planned time; the operator on shift requests it. The operator on shift and the operations manager can stop work at any time without justification; the supplier must stop and leave the system in the agreed safe state.

### Chapter 4

**EX016.** 5: has occurred here in the last 12 months, or is being actively attempted against similar operators now (public advisory). 4: has occurred in the sector in the last 2 years with conditions present here. 3: has occurred in the sector; would need one further condition here. 2: known in other sectors; would need several conditions. 1: no known occurrence; would need multiple unlikely conditions. Ratings account for controls that exist and are verified (Chapter 7).

**EX017.** R03 has the joint-second score (15) but consequence 3 on billing (service weight 1), so it falls to sixth under the consequence-first rule. R05's score is 10, but consequence 5 on drinking water lifts it to third. Governance actions: R02 — assign owner (A. Mensah, who owns dosing), set a new treatment date, review now; R04 — overdue restore test (J. Tan to run; A. Mensah as service owner); R07 — stale review (the coordinator as hospital liaison, or L. Ferreira as recorded owner, to review with the hospital).

**EX018.** "Risk R10: Because station KW-10's controllers are unsupported and cannot be fixed, a known weakness could be used to stop pumping, causing loss of supply to about 8,000 people. Accepted by: chief executive, M. Holt, on behalf of the board, 14 October 2026. Compensating measures: no remote access to KW-10; KVROC monitoring of the station network; physical access control; spare controllers held; manual-operation procedure drilled. Lapses if: a public advisory shows active exploitation, an incident occurs at KW-10, or a compensating measure fails. Expiry: 31 March 2027. Review owner: A. Mensah; coordinator to track."

**EX019.** Add an eighth field `acceptance_expiry` (None where no acceptance), for example R05 "2026-02-28" (expired) and R06 "2026-12-31" (valid). Rule: `if exp and dt.date.fromisoformat(exp) < TODAY: flags.append("ACCEPTANCE EXPIRED")`. Output now shows R05 with "ACCEPTANCE EXPIRED" and R06 without it, and "Needs governance action" becomes R02, R04, R05, R07. Full credit shows both cases.

**EX020.** Summary: "Our ranking rule puts anything that can affect health or the hospital first, then uses likelihood. Top risks: (1) supplier remote access without MFA — owner A. Mensah, fix by 30 April; (2) only one engineer understands the dosing logic — currently unowned; we ask the committee to confirm A. Mensah as owner and fund documentation and a second engineer by September; (3) grid supply loss at KW-07 — standby generator study due September. Governance actions: the historian restore test is overdue (now booked for April) and the hospital-supply risk review is stale (meeting set for March). Limits: likelihood ratings are expert judgements; the ranking is reproducible from the attached rule." No single score.

### Chapter 5

**EX021.** Regulatory requirements first (they are mandatory). Use CSF 2.0 as the programme structure and for board reporting because it is outcome-based and includes Govern. Use the CPGs as a prioritised baseline mapped to CSF functions, to find high-impact gaps quickly. Use ISA/IEC 62443 for OT procurement and supplier requirements (service provider and product requirements), referenced from the Govern supply-chain outcomes.

**EX022.** Scope: same systems and sites as the 2.6 assessment? Assessor and method: self-assessment, peer or independent; interview or evidence? Definition: what does level 3 mean, and did it change? Date: before or after the KVROC contract change? Decision: what will we do differently because of 3.1? Credible if same scope and method, evidence-based or independent, and linked to an observed outcome such as KVROC detecting the exercise injects within the target time.

**EX023.** (1) % of level-5 risks with owner and in-date treatment — owner: coordinator; < 100% → executive escalation. (2) Median working days from supplier contract end or staff departure to account removal — owner: operations manager; > 5 → access process review. (3) Number of operational interfaces reachable from the internet — owner: security lead; > 0 → immediate owner notification and fix. (4) % of on-call managers in an exercise within 12 months — owner: coordinator; < 80% → schedule exercise.

**EX024.** "Thanks — this could be urgent. Which site and function does hmi-02 serve? Was the connection successful or only attempted, and what is the source and evidence (log extract with UTC times)? Is it still reachable now? Blocking may cut a supplier's legitimate access — who uses that path? I'm calling A. Mensah now as owner; please stay on standby to block on his approval, and treat this under the incident escalation path until we know more."

**EX025.** "We assessed office IT and the treatment works against a national baseline; most practices exist on paper. The twelve pumping stations were not included, and two practices that matter most for them — strong authentication for supplier access and prompt removal of accounts — are unverified. We will review supplier access in May and reassess including stations by September."

### Chapter 6

**EX026.** Add a seventh role, "Shift supervisor", and correct the rows (Coordinator, Ops manager, Security lead, Comms, Vendor, CEO, Shift supervisor): Switch stations to manual — `I A - - - I R`; Brief hospital — `R C I C - A -` (coordinator is the single lead, comms consulted on wording); Approve vendor remote session — `C A R - I - I` (operations manager the single A, security lead checks the request, the vendor is only informed); Public statement — `C C C R - A -`; the other rows gain `I`, `C` or `-` for the shift supervisor. Rerunning Lab 6 with these rows prints "0 issues in 7 activities" and the load line `Coordinator=3, Ops manager=4, Security lead=2, Comms=1, Vendor=0, CEO=3, Shift supervisor=1`. The operations manager still carries four R/A entries, which EX029 addresses.

**EX027.** (a) Normal: new security-relevant access path; owner approval, rule review and expiry. (b) Standard, if a pre-approved procedure exists for battery replacement; otherwise normal. (c) Emergency: approved by incident lead, recorded within 24 hours, reviewed afterwards. (d) Normal: supplier compatibility check, test, rollback plan.

**EX028.** Card: "Suspected cyber event — call if: screens show changes nobody made; unexpected logins or messages; controls not responding; KVROC calls. 1) Keep the process safe — follow normal operating procedures; switch to manual only as procedures allow. 2) Do not switch off or restart computers unless instructed. 3) Note times and what you saw. 4) Call duty incident lead [number]; no answer in 10 minutes → deputy [number]; then operations manager [number]. 5) Immediate danger to people or water quality → operations manager directly and emergency procedures."

**EX029.** Keep safety decisions (manual operation, isolation affecting the process) with the operations manager. Delegate vendor-session approval during incidents to a named operations deputy or the incident lead with operations consulted; hand hospital liaison to the coordinator; ensure a deputy operations manager is on call so the plant always has someone focused on it.

**EX030.** List emergency changes from the incident log; for each, decide keep, modify or revert with an owner: the "block all supplier access" rule becomes a normal change — restore access per supplier through the normal approval process once the review is complete; remove the temporary local admin account and verify removal; update diagrams and records; record the review as a decision record.

### Chapter 7

**EX031.** Objective: prevents use of supplier accounts by people no longer under contract (risk R01 and supplier-departure risks). Owner: operations manager (as contract and station owner). Operation: when a contract ends or the supplier notifies a staff departure, the account is disabled within 5 working days; monthly the coordinator reconciles gateway accounts against the contract register. Evidence: reconciliation record and gateway export, stored in the record library. Failure signal: any account whose contract has ended or whose named person has left.

**EX032.** Supplier MFA: tested (protects level-5 consequences; supervised password-only login refused). Manual-operation procedure: tested through drills or exercises (it is the safety fallback). Office laptop password policy: observed (configuration export) — consequence level 3. Head-office visitor badges: documented or observed — lower consequence for the service.

**EX033.** Restore the latest historian backup into an isolated environment (not production), authorized by A. Mensah, with J. Tan running it. Start a timer at the decision to restore; success if the historian is usable within 24 hours and data for a chosen 7-day period is complete compared with a known reference. Record times, steps, problems and result in a test report; file it and update control C2's assurance level to "tested" with date.

**EX034.** "Exception E-07: control 'MFA for engineering access' not applied to KW-10 local engineering interface. Reason: controller firmware cannot support it; replacement planned. Compensating: no remote path to KW-10; locked cabinet with logged keys; configuration checksums compared weekly; KVROC alerts on any engineering session. Accepted by: chief operating officer E. Varga (consequence 4), 1 October 2026. Expiry: 31 March 2027. Removal plan: controller replacement in the 2027 capital programme; owner A. Mensah."

**EX035.** C1 supplier MFA: observed on 5 of 6 accounts; ScadaCo gap to be fixed by 3 June (A. Mensah). C2 historian restore: backups observed nightly but restore never tested; test booked within 60 days (J. Tan). C3 dosing limits: tested on a spare controller 3 February and production matched by checksum; recheck after any logic change (J. Tan).

### Chapter 8

**EX036.** `v-hydro1`: no finding; keep. `v-hydro2`: unnamed account — actions not attributable; replace with named account within 14 days, supervised sessions meanwhile (A. Mensah). `v-scadaco`: no MFA — password alone grants access; ScadaCo to enable within 30 days or exception with compensating measures; keep a supervised fallback for urgent support (A. Mensah). `v-pumps`: contract ended — disable now and confirm with Vale Pumps. `v-meter`: unused > 90 days — disable; re-enable on request. `v-integr`: 19 vs ~4 sessions — ask J. Tan and Northgate; a project explains 17; escalate the two unexplained night sessions to the security lead. No accusation.

**EX037.** Add a field `staff_confirmed` (date the supplier last confirmed its list of people with access), for example "2026-04-01" for HydroLogic and "2025-09-15" for Northgate. Rule: `if (TODAY - dt.date.fromisoformat(conf)).days > 180: f.append("staff list unconfirmed >180 days")`. Output then shows the flag on `v-integr` and not on `v-hydro1`. It matters because supplier staff departures are a common way for valid credentials to outlive their owners.

**EX038.** (1) Only named individuals listed in Annex A may access; changes notified in writing before access (verified at each quarterly review). (2) Every remote session uses the utility's gateway with multi-factor authentication (verified from gateway configuration and logs). (3) Supplier notifies the utility within 24 hours when a listed person leaves or loses a device used for access (verified by quarterly staff-list confirmation). (4) Supplier provides work logs for any session within 2 working days of request (verified by sampling). (5) At contract end, supplier confirms in writing within 14 days that utility data has been deleted (verified by record in the library).

**EX039.** "TLP:AMBER+STRICT. L. — the supplier access review found 19 Northgate sessions in 90 days. J. Tan and Northgate's work log account for 17 (KW-11 telemetry commissioning, approved March). Two are unexplained: 12 April and 19 April, both starting 02:00 local (01:00 UTC), source and target in the attached gateway export. Unknown: who connected and what was done. I ask you to review the session records under the incident escalation path and advise whether to restrict the account. Please don't contact Northgate until you've decided. I'll check in at 16:00."

**EX040.** (1) Reviewed: all six supplier accounts on the remote-access gateway, 4 May, read-only export authorized by A. Mensah. (2) Findings: one unnamed account, one without MFA, one for an ended contract, one unused, one with unusual volume (evidence attached). (3) Decided by A. Mensah: two accounts disabled; named replacement within 14 days. (4) Requested from you: approve standard contract clauses for renewals; approve budget for ScadaCo MFA if they cannot fund it; confirm monthly reviews. (5) Open: two unexplained Northgate night sessions — with the security lead, update Friday; assumption that the gateway is the only access path — firewall comparison by June (J. Tan).

### Chapter 9

**EX041.** Hospital call: due 23:40Z Saturday, sent 23:55Z — 0.25 h late; cause: two people believed the other would call (duplicated responsibility). Early warning: due 21:40Z Sunday, sent 18:05Z — early by 3.58 h; template worked. Insurer: due 21:40Z Monday — overdue, not sent; cause: duty missing from the register. Incident notification: due 21:40Z Tuesday, sent 22:30Z — 0.83 h late; cause: approval requested 40 minutes before the deadline. Final report: open, 646.7 h left. All causes are process gaps.

**EX042.** "Kestrel Water is investigating unauthorised access to computer systems that help us monitor water treatment. As a precaution, our operators are running two pumping stations manually. Water quality tests are normal and tap water remains safe to drink. You do not need to do anything. We are working with the relevant authorities and will update this page and our social media channels by 18:00 today, or sooner if anything changes."

**EX043.** "This is [name], Kestrel Water duty coordinator. Tomorrow between 09:00 and 13:00 we will switch the stations serving your site in a controlled way. Water stays safe to drink. Pressure may drop on the east side for up to four hours; supply should not stop. Please check your stored-water arrangements for sterile services and dialysis. Is there anything on your site that needs full pressure in that window, or a time that would be worse for you? I'll call again at 08:00 tomorrow to confirm; our 24-hour number is [number]."

**EX044.** "We are investigating with the relevant authorities and it would not be right to speculate about the cause or about any individual or company while that work continues. We will share what we can when we can confirm it." Reasoning: the information is unconfirmed (truthfulness); naming a supplier or person could unfairly harm them and may be wrong (fairness); we commit to updating (correction and transparency).

**EX045.** Internal deadlines: hospital call — owner (coordinator) calls within 60 minutes of clock start; early warning — draft at 12 h, approval requested by 18 h; incident notification — draft at 48 h, approval requested by 60 h; insurer — added to register, notified with the early warning. Delegation: if the chief executive is unavailable, the chief operating officer approves, then the operations director. Templates prepared for each. The incident lead records clock start in UTC in the decision log.

### Chapter 10

**EX046.** "3/6" counts I3 as success although no rationale was recorded for a safety decision, and treats I5 — a critical customer never briefed — as merely one failure among six. I4 had no owner. The most serious defect is I5: in a real incident, the hospital would not have been warned (or I3 if you argue unrecorded safety decisions are worse; reasoning required).

**EX047.** Add `safety` (yes for I2 and I3) and `consulted` (for example I3 "Security lead", I2 "Coordinator") columns, and the rule `if r["safety"] == "yes" and r["owner"] != "Ops manager" and "Ops manager" not in r["consulted"]: f.append("operations not consulted")`. With the original six rows the new flag never fires — I2 and I3 are both owned by the operations manager, so safety authority sat where it should. The invented row `95,I7 station alarm,isolate KW-09 network,Security lead,15,12,yes,yes,Coordinator` is flagged "operations not consulted". Explaining why I3 is correctly not flagged earns full credit; forcing a flag onto I3 does not.

**EX048.** Symptom: holding statement 11 minutes late and unowned. Hypotheses: (1) no accountable approver; (2) no template; (3) comms lead unsure what could be said. Evidence: Chapter 6 RACI had no A for public statement; hot wash said "waiting for someone senior". Cause: ownership gap. Fix: CEO accountable, comms responsible, pre-approved template, deputy approver. Verify: next exercise media inject, statement within 45 minutes with recorded approver.

**EX049.** Cause: no owner or schedule for verifying critical contacts; the hospital reorganised and nobody was told. Fix: the coordinator owns the critical-contacts list; quarterly test calls recorded; the hospital agreement requires notification of contact changes; a second route (hospital switchboard to site duty manager). Metric: % of critical contacts verified in the last quarter (target 100%).

**EX050.** A1: single lead for hospital briefing in RACI and checklist — owner E. Varga; due 30 June; closure evidence: published RACI v2; verification: hospital inject in January exercise. A2: "who depends on this supplier's access" column in supplier register — owner A. Mensah; due 31 July; evidence: register export; verification: next Lab 8 review. A3: rationale field and scribe role in decision log template — owner coordinator; due 15 June; evidence: template v2; verification: Lab 10 rerun of next exercise shows rationale for all decisions.

### Chapter 11

**EX051.** (1) "Within 20 minutes of the media inject, a holding statement is approved by the accountable executive and its approval time recorded." (2) "Within 30 minutes of the supplier-compromise inject, the team decides whether to suspend that supplier's access, records owner and rationale, and identifies who depends on it." (3) "When the night-shift operator inject is presented, the operator role reaches the incident lead or deputy within 10 minutes using only the printed escalation card."

**EX052.** O2 inject (00:35): "HydroLogic duty engineer calls: they need to reconnect now to fix a dosing pump fault at KW-02." Expected: refuse remote reconnection; arrange supervised on-site support or manual operation; record decision. O4 inject (01:10): "Regulator duty officer emails asking whether an early warning is coming, deadline in 4 hours." Expected: confirm approval route and send by deadline; record time. Both marked "EXERCISE — EXERCISE — EXERCISE".

**EX053.** Objectives 1 (vague; rewrite as observable). Scenario 1 (catastrophic and implausible; nothing specific learned; use a plausible supplier-compromise scenario). Injects 1 (unmapped). Roles and safety 0 (CEO evaluates own exercise; real email account risks confusion with a real event; use marked exercise channel, independent evaluators, safety officer). Evaluation 1 (no criteria). Ethics: risk of judging people; restate ground rules.

**EX054.** O1 met — declared at 9 min with rationale; action: none. O2 partially met — 52 min vs 30; dependency unknown; action: dependency column in supplier register (A. Mensah, July). O3 not met — no owner; action: single lead in RACI and checklist (E. Varga, June). O4 met — early warning approved and sent; action: none, keep template. O5 partially met — late, no owner until CEO arrived; action: CEO accountable, deputy approver, template (R. Adeyemi, June). No individual named as at fault.

**EX055.** During: thank the chief executive, then ask the operations manager directly, "In reality, who would decide on isolating KW-04?"; invite each role owner by name; record who decided. After: record in the AAR as "decision rights for technical isolation were unclear in practice" with an action to confirm them in the RACI; brief the chief executive privately beforehand on the AAR finding, respectfully, framing it as a plan issue.

### Chapter 12

**EX056.** Example index: 1. Dependency map (EX009) — "I verify the assumptions behind critical-customer decisions." 2. Authorization rewrite (EX011) — "I make work on operational systems accountable." 3. Decision record (EX012) — "I record decisions fairly with unknowns." 4. Register summary (EX020) — "I rank by consequence and keep hygiene." 5. Metrics (EX023) — "I measure what drives decisions." 6. RACI and card (EX026, EX028) — "I make roles unambiguous." 7. Control cards and plan (EX031, EX033) — "I distinguish stated from tested." 8. Supplier case (EX040) — "I analyse cases fairly." 9. Notification design (EX045) — "I meet clocks." 10. AAR and action log (EX054, EX050). All labelled "course work on synthetic data".

**EX057.** A script following 12.4: context in consequence terms with one sourced advisory; top risks with owners and assurance levels; two or three exercise findings and their fixes; progress against plan; three requests (an exception acceptance with expiry, contract clauses, an appetite statement). Every number traceable to the portfolio.

**EX058.** Days 1–30: meet clinical and estates leadership, medical-devices team, IT, suppliers, the regulator's contact; map clinical services and their dependencies (power, water, medical gases, networks, devices); read incident history. Days 31–60: owners for patient-safety-level risks, incident RACI including clinical decision-makers (diversion, downtime procedures), escalation card, notification register (including any health-sector duties), supplier review of device maintainers. Days 61–90: tabletop on loss of clinical systems with clinical leadership playing, AAR, board briefing with requests.

**EX059.** Evidence: authorized test plan; timed log (start, steps, end); result record with data-completeness check against a reference period; problems and fixes; sign-off by service owner. Auditor questions: "Was it a full restore of the system or only of the database?" and "Was it restored to an isolated environment that resembles production, and would the same time apply to a site-wide outage?"

**EX060.** Model: Frame and identify 3 (EX001, EX005); Analyse and decide 2 (EX017, EX018 — likelihood calibration still weak); Organise 3 (EX026); Verify 2 (EX033 — never designed a real test with an engineer); Communicate 3 (EX042, EX043); Improve 2 (EX050). Learning plan: work through Chapters 5–9 of the technical course for OT verification fundamentals by December; calibrate likelihood with two sector advisories per month and a peer coordinator review by January.

<a id="glossary"></a>

## Glossary

- **Accountable (RACI)** — the single person who answers for an activity's outcome and signs it off.
- **After-action report (AAR)** — a report rating an exercise or incident against objectives, with evidence and recommendations.
- **Assurance level** — how strongly a control's operation is established: stated, documented, observed or tested.
- **Authorization** — a written, specific approval by the owner of the consequence, defining scope, activities, people, window, stop conditions and data handling.
- **Critical customer** — a recipient of the service for whom interruption quickly harms people (for example a hospital).
- **Decision record** — a dated record of a decision, its maker, options, known and unknown information, conditions and recipients.
- **Essential service** — a service whose interruption harms people, the economy or public order quickly and at scale.
- **Exception** — an owned, compensated, time-limited decision to operate without a required control.
- **Holding statement** — an early, factual public message issued before the full picture is known.
- **Hot wash** — the immediate debrief after an exercise.
- **Inject** — a timed piece of scenario information presented during an exercise.
- **Notification register** — a list of every external duty to inform, with trigger, recipient, deadline, owner and channel.
- **RACI** — a matrix of activities against roles: Responsible, Accountable, Consulted, Informed.
- **Risk appetite** — the amount of risk leadership is willing to accept, stated in advance.
- **Risk owner** — the person with authority and budget to decide how a risk is treated.
- **Stop condition** — a pre-agreed, observable event that ends authorized work immediately.
- **Tabletop exercise** — a discussion-based exercise in which participants talk through their response to a scenario.
- **Traffic Light Protocol (TLP)** — a marking scheme indicating how far recipients may share information.

<a id="references"></a>

## References

Standards, laws, guidance and public pages change. Versions and dates below are those consulted for this draft (October 2026); re-verify before relying on them. A citation supports the general claim beside it in the text, never the synthetic case details.

### Laws, frameworks and guidance

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology).
- Cybersecurity and Infrastructure Security Agency. [CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages).
- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency and Federal Bureau of Investigation. [DarkSide Ransomware: Best Practices for Preventing Business Disruption from Ransomware Attacks (AA21-131A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a). May 2021.
- Cybersecurity and Infrastructure Security Agency et al. [IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including US Water and Wastewater Systems Facilities (AA23-335A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a). December 2023.
- European Parliament and Council. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj), in particular Articles 20, 21 and 23.
- Federal Emergency Management Agency. [Homeland Security Exercise and Evaluation Program (HSEEP)](https://www.fema.gov/emergency-managers/national-preparedness/exercises/hseep).
- FIRST. [Traffic Light Protocol (TLP) version 2.0](https://www.first.org/tlp/).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Cyber Security Centre (UK). [Exercise in a Box](https://www.ncsc.gov.uk/information/exercise-in-a-box).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0, CSWP 29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), February 2024; [Cybersecurity Framework home](https://www.nist.gov/cyberframework).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-84, Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).
- National Institute of Standards and Technology. [SP 800-137, Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/pubs/sp/800/137/final).
- National Institute of Standards and Technology. [SP 800-161 Rev. 1, Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final).

### Software documentation

- Python Software Foundation. [csv](https://docs.python.org/3/library/csv.html) and [datetime](https://docs.python.org/3/library/datetime.html). Python 3 documentation.
