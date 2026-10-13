# Incident Response and Cyber Resilience: Specialist Practice, Command and Assurance

- Language: English (`en`); postgraduate course, two years; approximately 600 hours of planned study (course 154 of 207 in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **draft**. Chapters 1–12 of 12 have authored teaching text, exercises EX001–EX060 and matching worked results; four chapters include an offline Python lab whose printed output was verified with Python 3.13. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: experienced specialists — incident leads, senior analysts, security managers and consultants — who hold a prior degree or equivalent professional experience and now lead organization-scale response choices.
- Relation to the other books in this area: the practitioner books ([rapid](../../../../rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md), [professional](../../../../professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md), [technical](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md)) teach how to act in a response; the technologist book teaches implementing and running a response service; the [bachelor's book](../../../../bachelors-4-years/incident-response-resilience/en/book/MANUSCRIPT.md) builds foundations and applied judgement; the [engineering book](../../../../engineering-5-years/incident-response-resilience/en/book/MANUSCRIPT.md) designs response systems; the [master's](../../../../masters-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) and [doctoral](../../../../doctorate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) books teach research. **This postgraduate book teaches specialist practice**: framing and owning decisions under appetite and uncertainty, enterprise incident command, integrating expert, legal and privacy inputs, coordinated containment, controlled recovery evaluation, leadership and assurance, and redesigning and transferring an incident program.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights.
- Educational boundary: an independent educational blueprint, not an accredited qualification, legal advice or authority to access any real system or data. Every organization (notably the fictional multi-division **Calder Group** with its Retail, Logistics and Financial Services divisions), person, account, address, case and number in an example or exercise is **synthetic** unless a sentence cites a public source. Regulatory descriptions (GDPR, NIS2, SEC rules) are summaries to verify against current texts with counsel.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

Read the twelve chapters in order; they follow one fictional enterprise through a year of difficult incidents and a program redesign. Chapters 1–4 establish how specialists frame decisions against risk appetite, run enterprise incident command, integrate specialist evidence and test requests for proportionality. Chapters 5–8 apply this to coordinated containment, controlled recovery evaluation, legal–privacy–operations integration and cases with conflicting evidence. Chapters 9–10 address leadership briefings, assurance claims and critical reading of published evidence. Chapters 11–12 are the applied project: redesign one part of the incident program, pilot it, evaluate it and transfer it.

Each chapter has learning outcomes, teaching sections, a synthetic worked example, common errors and limits, five exercises with 0–3 rubrics and a synthesis, followed by a **Continue studying** block. Labs in Chapters 1, 6, 8 and 11 run offline with the Python 3 standard library; compare your output with the printed expected output and investigate any difference. Scores in the labs are structured judgements made visible, not measurements.

Keep five labels in your decision log: **fact** (from evidence, with source), **assessment** (analyst judgement with confidence), **determination** (by a qualified specialist such as counsel or the privacy officer), **decision** (by the accountable owner) and **action** (executed, with time and owner). The specialist's commonest failure is not a technical error but an unowned decision or an assurance claim without evidence.

## Contents

1. [Advanced security decision-making](#ch-01)
2. [Current practice in enterprise incident command](#ch-02)
3. [Specialist evidence in complex investigations](#ch-03)
4. [Advanced risk and ethics](#ch-04)
5. [Alternatives for coordinated containment](#ch-05)
6. [Controlled evaluation of recovery strategies](#ch-06)
7. [Integration across legal, privacy and operations](#ch-07)
8. [Difficult cases with conflicting evidence](#ch-08)
9. [Response leadership and assurance decisions](#ch-09)
10. [Research reading and critique](#ch-10)
11. [Applied project: redesign an incident program](#ch-11)
12. [Final review and organizational transfer plan](#ch-12)

The [worked results](#worked-results) contain EX001–EX060. A [glossary](#glossary) and [references](#references) close the book.

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes and connection

After this chapter you can (1) frame an incident decision so that the options, the decision owner, the time horizon and the evaluation criteria are explicit; (2) translate the organization's **risk appetite** into thresholds that a commander can use at 03:00; (3) separate the uncertainty you can reduce from the uncertainty you must decide through; (4) write a decision record that a board, a regulator or an auditor can read a year later; and (5) define conditions that require the decision to be revisited. You arrive with a degree or equivalent experience and have handled incidents. This book does not teach you how to respond — it teaches you how to make, lead and defend organization-scale response choices as a specialist. Chapter 2 places these decisions inside an incident-command structure.

### 1.1 What changes at specialist level

Earlier courses ask "what is the right action?". At specialist level, the more frequent question is "who must decide what, with which information, by when, and how will the decision be judged?". Decisions now affect several business units, involve legal and regulatory exposure, and are taken before the facts are complete. Two failure modes dominate: **decision avoidance** (waiting for certainty that will not arrive while harm accumulates) and **decision capture** (the loudest stakeholder's preference becomes the decision without anyone owning the trade-off). Both are prevented by structure, not by courage.

### 1.2 Framing

A decision frame has six parts:

1. **Decision statement** — one sentence: "Whether to take the customer-order API offline during the investigation of suspected data exposure."
2. **Owner** — the single accountable person (and deputy) with authority for this decision.
3. **Options** — at least three, including a partial or staged option and "continue as now". Binary framing hides the best answers.
4. **Criteria** — what the organization cares about here: harm to people, legal exposure, service continuity, evidence, cost, reputation. Criteria come from policy and appetite, not from the moment.
5. **Horizon** — when the decision must be made and how long it binds.
6. **Information plan** — what can be learned before the deadline and what cannot.

Framing is the specialist's main lever. A badly framed decision ("shut it down or not?") forces a bad choice even with perfect analysis.

### 1.3 Risk appetite into thresholds

**Risk appetite** is the amount and type of risk an organization is willing to pursue or retain; **risk tolerance** is the acceptable variation around it. Boards express appetite in words ("very low appetite for loss of customer personal data; moderate appetite for short service interruptions outside peak periods"). Commanders need thresholds: "if there is a credible indication (≥ 'possible' on our scale) that customer personal data is being extracted, we accept interruption of up to 4 hours of non-peak service to stop it without further executive approval". Translating appetite into such pre-approved thresholds is preparation work; during an incident it removes hours of escalation. NIST's guidance on integrating cybersecurity with enterprise risk management (NIST IR 8286 series) discusses appetite and tolerance in this sense.

### 1.4 Reducible and irreducible uncertainty

Some uncertainty shrinks with effort before the deadline — whether a log shows outbound transfer, whether a backup is intact. Some does not — the attacker's next move, whether a regulator will view a choice as reasonable. Spend investigative effort on reducible uncertainty that could change the decision (the **value of information**, introduced at bachelor's level), and decide through the rest with explicit assumptions. A useful discipline is to write: "If we learn X by 14:00, we choose A; otherwise B."

In Calder's order-API case, that sentence became the O4 escalation trigger.

### 1.5 Decision quality versus outcome quality

A good decision can have a bad outcome and vice versa. Judge decisions by the information, options and reasoning available at the time, not by what happened. This is not an excuse: it is the only fair basis for learning, and it is how a well-prepared decision record protects the people who made the decision. Hindsight bias (Fischhoff, 1975) will otherwise rewrite history.

Calder's order-API record is built for this test: it lists the gateway logs reviewed up to 09:40, the partner list and the board's appetite statement v3, so a later reviewer can judge O4 on what was known at 10:25, not on what the investigation found afterwards.

### 1.6 Residual risk and acceptance

Every option leaves **residual risk**. The owner must accept it explicitly, in writing, with its expected duration and the conditions under which it will be re-examined. Unaccepted residual risk is a common finding in post-incident and audit reviews.

Calder's O4 record states its residual risk plainly: records retrieved with the key before rotation may already be exposed, and that question remains under investigation. Writing it down makes the group incident commander's acceptance visible and gives the privacy and legal workflow a clear starting point if overnight extraction is later confirmed. It also tells the board exactly which risk it carried during the holiday sale.

### 1.7 Revisit conditions

Decisions under uncertainty must state **revisit triggers**: new facts (evidence of exfiltration), elapsed time (every 6 hours), threshold breaches (customer complaints above a level), or stakeholder events (regulator inquiry). Triggers prevent both stubbornness and churn.

The order-API record shows all four kinds of trigger at work: any bulk retrieval after key rotation moves Calder to O3, taking the API offline, without a new meeting, because that move was pre-approved; confirmed overnight extraction starts the privacy and legal notification workflow; and the decision is re-examined every six hours whatever happens. A regulator inquiry or a partner complaint would be sensible additions.

### 1.8 Worked example and lab (synthetic): the order API during a critical period

*Fictional.* Calder Group, a multi-division retail and logistics company, detects at 09:40 on the Friday before a national holiday sale that an API key for the customer-order API was used from an unrecognized address overnight. Records retrievable with the key include names, addresses and order histories (no payment card data, which is tokenized by a processor). The sale generates about 40% of the quarter's online revenue in four days.

Options: O1 continue and monitor; O2 rotate the key and add an address allow-list (minutes of disruption for two partners); O3 take the API offline until the investigation concludes (stops partner fulfilment; estimated 12–48 hours); O4 rotate key, allow-list, and rate-limit bulk queries, with a pre-agreed escalation to O3 if any bulk retrieval is seen after rotation.

Appetite (board statement, fictional): very low for customer personal data loss; moderate for revenue loss under 2% of the quarter; very low for regulatory non-compliance.

Save as `lab01.py`. It scores options on criteria with weights derived from the appetite statement and tests whether the choice survives plausible changes in two uncertain inputs.

```python
# Lab PG-01 - appetite-weighted option comparison with a robustness check (synthetic, stdlib only)
from itertools import product

WEIGHTS = {"data": 0.45, "revenue": 0.20, "regulatory": 0.25, "evidence": 0.10}
# score 0 (worst) .. 10 (best) per criterion; 'data' depends on p = P(ongoing extraction)
def scores(p, outage_hours):
    rev_o3 = max(0, 10 - outage_hours / 4)        # longer outage, worse revenue score
    return {
        "O1 monitor":            {"data": 10 - 10*p, "revenue": 10, "regulatory": 10 - 8*p, "evidence": 7},
        "O2 rotate+allowlist":   {"data": 10 - 3*p,  "revenue": 9,  "regulatory": 10 - 3*p, "evidence": 8},
        "O3 offline":            {"data": 10,        "revenue": rev_o3, "regulatory": 9,     "evidence": 9},
        "O4 rotate+limit+trigger": {"data": 10 - 1.5*p, "revenue": 8.5, "regulatory": 10 - 1.5*p, "evidence": 8},
    }
def best(p, h):
    s = scores(p, h)
    tot = {o: round(sum(WEIGHTS[c]*v for c, v in crit.items()), 2) for o, crit in s.items()}
    return max(tot, key=tot.get), tot

b, tot = best(0.3, 24)
print("base case p=0.3, outage 24h:", tot, "->", b)
wins = {}
for p, h in product((0.1, 0.3, 0.5, 0.7, 0.9), (12, 24, 48)):
    w, _ = best(p, h)
    wins.setdefault(w, []).append((p, h))
for w, cells in sorted(wins.items()):
    print(f"{w}: best in {len(cells)} of 15 scenarios", cells if len(cells) < 5 else "")
```

Expected output:

```text
base case p=0.3, outage 24h: {'O1 monitor': 7.75, 'O2 rotate+allowlist': 8.97, 'O3 offline': 8.45, 'O4 rotate+limit+trigger': 9.19} -> O4 rotate+limit+trigger
O2 rotate+allowlist: best in 3 of 15 scenarios [(0.1, 12), (0.1, 24), (0.1, 48)]
O3 offline: best in 3 of 15 scenarios [(0.5, 12), (0.7, 12), (0.9, 12)]
O4 rotate+limit+trigger: best in 9 of 15 scenarios 
```

Interpretation: O4 is best in 9 of 15 combinations, including every combination with a 24- or 48-hour outage once extraction is at least moderately likely. Its neighbours tell you where the decision is fragile. If extraction is unlikely (p = 0.1), the lighter O2 edges ahead because O4's rate limit costs some revenue — the two are close and either is defensible. If extraction is likely and the outage would be short (12 hours, p ≥ 0.5), going offline wins. The scores are structured judgements, not measurements; the value of the exercise is that it shows which uncertainty matters (here, how likely ongoing extraction is, and how long O3 would really take) and designs the escalation trigger around it. That is why O4 includes a pre-approved move to O3 if bulk retrieval is seen after rotation, and why estimating O3's real outage length is worth an hour of the API owner's time.

**Decision record (excerpt).** Decision: O4. Owner: Group incident commander (deputy named). Time: 10:25. Information used: API gateway logs 00:00–09:40; partner list; board appetite statement v3. Key assumptions: payment data not reachable via this API (confirmed by architecture review 2025, re-checked today with the API owner); allow-list covers all legitimate partners (owner confirmation 10:15). Residual risk accepted: records retrieved before rotation may already be exposed; under investigation. Revisit triggers: any bulk retrieval after rotation (→ O3 immediately, pre-approved); confirmation of overnight extraction (→ privacy/legal notification workflow); every 6 hours.

### 1.9 Common errors and limits

- Binary framing that omits staged or partial options.
- Appetite statements that never become operational thresholds.
- Seeking information that cannot change the decision while the deadline passes.
- Judging the decision by its outcome.
- Treating weighted scores as measurements; they are a disciplined way to expose judgement, and their weights must come from the organization, not the analyst.

Calder's order-API case shows the first and last errors side by side. Framing the choice as "keep the API up or take it down" would have left out O4, the staged option the lab found best in 9 of 15 combinations. And O4's weights came from the board's appetite statement, not from the analyst's own sense of which harm mattered more.

### Exercises — chapter 1

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX001 — Reframe.** *Inputs:* an executive asks: "Do we pay the ransom or not?" *Steps:* write a full six-part frame with at least four options. *Rubric:* 3 = frame complete; options include restore-without-paying, partial restore with prioritized services, engage negotiator for time while restoring, and payment (subject to legal and sanctions review); owner single and named by role; 2 = binary options remain; 1 = no criteria; 0 = none.

**EX002 — Appetite to threshold.** *Inputs:* appetite statement "low appetite for disruption to warehouse operations; very low appetite for safety incidents". *Steps:* write two pre-approved thresholds a commander can act on without further approval. *Rubric:* 3 = observable trigger, permitted action, limit, notification duty; 2 = trigger vague; 1 = restates appetite; 0 = none.

**EX003 — Run and stress Lab PG-01.** *Steps:* run the lab; change the regulatory weight to 0.10 and data to 0.60; report the new pattern of wins and what it implies. *Rubric:* 3 = output reported and correctly interpreted (O4 remains robust or the pattern change is explained); 2 = output only; 1 = not run; 0 = none.

**EX004 — Information plan.** *Steps:* for the order-API case in this chapter's worked example list three pieces of reducible uncertainty with the decision each could change, and one irreducible uncertainty. *Rubric:* 3 = each reducible item tied to a specific option switch and deadline; irreducible example correct; 2 = not tied to options; 1 = list only; 0 = none.

**EX005 — Revisit triggers.** *Steps:* critique the revisit triggers in this chapter's order-API worked example and add two. *Rubric:* 3 = identifies gaps (no trigger for new key misuse elsewhere, partner complaints, regulator contact) with measurable triggers; 2 = adds triggers without critique; 1 = generic; 0 = none.

### Chapter synthesis

Specialist decisions are won in framing: one owner, several options including staged ones, criteria from appetite, thresholds approved in advance, effort spent on uncertainty that can change the choice, robustness checks, accepted residual risk and explicit revisit triggers.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Current practice in enterprise incident command

### Learning outcomes and connection

You will be able to (1) design an incident-command structure that works across divisions with conflicting reporting lines; (2) define the commander's authority, delegation and information cadence; (3) build a handoff protocol that survives shift changes and fatigue; and (4) stress-test a command charter against realistic failure points. Chapter 1 established how individual decisions are framed; this chapter places them inside an organization. Chapter 5 uses the structure to coordinate containment.

### 2.1 Why command structures

Large incidents fail more often from coordination than from technical ignorance. The Incident Command System (ICS), developed for wildfire response in the United States in the 1970s and embedded in the National Incident Management System (NIMS), introduced principles that transfer well: a single incident commander, **unity of command** (each person reports to one supervisor in the incident), **manageable span of control** (roughly three to seven direct reports), modular expansion, common terminology and a written incident action plan per operational period. Cyber incidents adapt these principles rather than copy the full structure.

### 2.2 The commander's role

The **incident commander** owns the incident: sets objectives, approves the action plan, makes or delegates decisions within pre-approved thresholds (Chapter 1) and escalates the rest. The commander is not the best technician; doing hands-on analysis is a common failure because it consumes attention needed for coordination. A **deputy** shares load and provides continuity.

Calder's charter enforces this: the group incident commander comes from a pre-approved roster of six trained people, with a deputy, and divisional CIOs sit in the command meeting as business liaisons rather than directing technical work themselves.

### 2.3 Functional sections

A typical enterprise cyber structure: **Operations** (technical investigation, containment, recovery — often split into workstreams), **Planning** (situation status, timeline, action plan, documentation), **Communications** (internal, customers, media, regulators via legal), **Legal and privacy** (advice, notification analysis, privilege), **Business liaison** (division leaders, service owners), and **Logistics** (people, tools, external retainer firms, rest rotations). In smaller incidents one person may hold several functions; the roles still exist.

At Calder, Planning maintains the incident record and the situation reports, and Business liaison is where the three divisional CIOs sit. A commander with eleven people reporting directly can regroup them into these six sections plus a deputy, which is the exercise this chapter sets.

### 2.4 Conflicting reporting lines

In enterprises, people in the incident report to divisional managers outside it. Unity of command during the incident must be agreed in policy: for the incident's duration, participants take incident tasking from the incident structure, while their line managers retain HR authority. Divisional leaders join as liaisons, not as parallel commanders. Without this agreement, the most senior person in the room becomes the de facto commander regardless of competence.

Calder learned this from a previous incident: three CIOs each ordered containment in their own divisions, and one isolated a shared directory server, breaking authentication for the other two. The group CISO was informed but not in command. The charter now states that divisional CIOs cannot order containment on shared services.

### 2.5 Information cadence

Set a **battle rhythm**: fixed times for situation updates (for example every 2 hours for the core team, every 6 for executives), a standard situation report format (facts, assessment, actions, decisions needed, next update), and a single source of truth (case record or shared document) that Planning maintains. Ad hoc requests for updates are redirected to the next scheduled update unless a decision is pending.

Calder's charter sets this rhythm: a 15-minute core sync every 2 hours in a standing format, an executive brief at 08:00 and 18:00, and Planning maintaining the single incident record. When a division head asks for an extra update mid-afternoon, the answer is the 18:00 brief, unless a decision she owns is waiting.

### 2.6 Delegation and thresholds

Delegate decisions with explicit bounds: "Operations lead may isolate any non-production host; production isolation requires commander approval unless the Chapter 1 threshold applies." Record delegations so that responsibility is clear in review.

Calder's charter writes its bounds the same way: Operations may contain within a single division's non-shared assets, while shared services such as identity, network core and email need the commander's approval. That rule is what would have stopped one CIO isolating the shared directory server in the earlier incident. Delegations made during an incident go into the decision log with the time and the person delegating, so a later review can see who had authority to act and when.

### 2.7 Handoffs and fatigue

Long incidents need **operational periods** (for example 12 hours) with formal handoffs. A handoff includes: current objectives, situation summary, active workstreams and owners, pending decisions, recent decisions and their reasons, risks and watch items, and contacts. The incoming commander reads back the key points. Fatigue degrades judgement; schedule rest deliberately, including for leaders.

Calder's stress test found the gap this list guards against: at the 19:00 shift change, the incoming commander found a pending decision, whether to force-reset all Logistics passwords, with no record of why it had been deferred. The handoff template now requires the options, the reason for deferral and the deadline. Commanders may serve at most two consecutive 12-hour periods.

### 2.8 Worked example (synthetic): a multi-division charter

*Fictional.* Calder Group has three divisions — Retail, Logistics and Financial Services — each with its own IT team and CIO, plus a group security team. A suspected identity-provider compromise affects all three.

Problem observed in a previous incident (fictional): three CIOs each ordered containment in their divisions; one isolated a shared directory server, breaking the others' authentication. The group CISO was "informed" but not in command.

Charter (excerpt):
- Activation: group security duty manager declares a group incident when more than one division is affected or a shared service is involved.
- Command: group incident commander from a pre-approved roster of six trained people (two per region), with a deputy. Divisional CIOs serve as **business liaisons** and sit in the command meeting; they cannot order containment on shared services.
- Thresholds: Operations may contain within a single division's non-shared assets; shared services (identity, network core, email) need commander approval.
- Cadence: core sync every 2 hours (15 minutes, standing format); executive brief at 08:00 and 18:00; Planning maintains the incident record.
- Handoff: 12-hour periods at 07:00 and 19:00; written handoff with read-back; commanders may not serve more than two consecutive periods.

Stress test — shift change at 19:00 during active containment: the incoming commander finds a pending decision (whether to force-reset all Logistics passwords) without the context of why it was deferred. Fix: pending decisions in the handoff must include options, the reason for deferral and the deadline. The test also reveals that the deputy roster lacks coverage for weekends in one region — a logistics action.

### 2.9 Common errors and limits

- The commander doing technical work.
- Divisional leaders acting as parallel commanders.
- Updates on demand instead of on a rhythm.
- Handoffs without pending decisions and their reasons.
- Copying ICS terminology without the training and exercises that make it work.

Calder's charter answers each error in turn. The commander comes from a trained roster and does not take hands-on work. Divisional CIOs act as liaisons, not parallel commanders, and cannot order containment on shared services. A fixed sync and briefing rhythm replaces updates on demand. Handoffs must carry pending decisions with their reasons. The roster itself was tested in an exercise, which is how the weekend coverage gap in one region was found.

### Exercises — chapter 2

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX006 — Span of control.** *Inputs:* a commander has 11 direct reports. *Steps:* restructure to a manageable span and justify. *Rubric:* 3 = groups into sections (operations, planning, communications, legal/privacy, liaison, logistics) with leads, 4–6 direct reports; 2 = reduces span without logic; 1 = unchanged; 0 = none.

**EX007 — Unity of command clause.** *Steps:* write the policy clause that resolves conflicting reporting lines during incidents. *Rubric:* 3 = incident tasking authority, line-manager retention of HR authority, liaison role for divisional leaders, dispute escalation path; 2 = partial; 1 = vague; 0 = none.

**EX008 — Situation report.** *Inputs:* this chapter's multi-division charter worked example, at 14:00. *Steps:* write a one-page situation report in the standard format. *Rubric:* 3 = facts with sources, assessment with confidence, actions with owners, decisions needed with deadlines, next update; 2 = missing decisions; 1 = narrative; 0 = none.

**EX009 — Handoff template.** *Steps:* design a written handoff template with read-back items. *Rubric:* 3 = objectives, situation, workstreams/owners, pending decisions (options, reason for deferral, deadline), recent decisions with reasons, risks, contacts, read-back of top three; 2 = misses pending decision detail; 1 = list of notes; 0 = none.

**EX010 — Stress test plan.** *Steps:* design a 60-minute exercise that stress-tests the charter against a shift change and an absent deputy. *Rubric:* 3 = objectives, injects at handoff and deputy absence, observable criteria, observers, corrective-action capture; 2 = injects without criteria; 1 = generic; 0 = none.

### Chapter synthesis

Enterprise command needs one commander with trained deputies, sections with clear leads, unity of command agreed in policy, a fixed information rhythm, bounded delegation and handoffs that carry pending decisions and their reasons — tested under shift change and absence.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 12

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Specialist evidence in complex investigations

### Learning outcomes and connection

You will be able to (1) read forensic, cloud-audit and identity-trace reports critically; (2) reconcile conflicting specialist findings; (3) request clarifying evidence precisely; and (4) write a confidence statement that a non-specialist executive and a legal adviser can both use. Chapter 2 gave you the command structure; this chapter equips the commander or specialist lead to integrate expert evidence. Chapter 8 extends the method to cases where evidence conflicts deeply.

### 3.1 The specialist report as evidence

At this level, much evidence reaches you as reports written by others: internal forensic analysts, external retained firms, cloud providers, vendors. A report is a chain of claims built on artefacts, tools and interpretation. Reading it well means separating (a) the artefacts examined, (b) the methods and tools (with versions), (c) the observations, (d) the interpretations, and (e) the stated limitations — and noticing when one is missing.

Calder's ransomware case shows why: the external firm's report H and the internal cloud team's report C each reached a sound conclusion from different artefact sets. Neither had seen the other's logs.

### 3.2 Forensic reports

A host forensic report should state the acquisition method (live response, disk image, memory capture), hashes, the timeline of artefacts (process execution, file creation, registry or configuration changes), interpretation (for example "initial execution via a malicious document at 10:02") and limits (timestamp reliability, anti-forensics, missing logs). NIST SP 800-86 describes the integration of forensic techniques into response; standards such as ISO/IEC 27037 cover identification, collection, acquisition and preservation of digital evidence.

Report H in Calder's ransomware case had most of these elements: appliance logs with 30-day retention, a jump-host image, and an interpretation of the 01:12 VPN session. What it lacked was a statement that IdP logs had not been examined, which was the limit that mattered.

### 3.3 Cloud audit reports

Cloud evidence comes from provider logs whose completeness depends on configuration and licence (bachelor's Chapter 31 showed the effect of missing data-read logs). A cloud report should state which log types were available, their retention, any gaps, and the query logic used. Provider statements about their own systems are evidence too, but with limited verifiability.

Report C at Calder was a cloud report of this kind: it used IdP sign-ins and control-plane logs to trace a phished administrator and the access key created minutes later. Its conclusion was strong on what those logs showed, but it had not checked whether the key was used from Calder's VPN pool or on-premises ranges, which is exactly the question Calder later sent back to the cloud team.

### 3.4 Identity traces

Identity investigations follow principals across IdP sign-ins, token issuance, application sessions and privileged operations. Common pitfalls: assuming a sign-in location is the user's location; ignoring non-interactive token refreshes; confusing the account that authenticated with the service that acted on its behalf.

The Calder reconciliation turned on such a trace. The 01:12 VPN session looked like an exploit to the host-based firm, but it authenticated with valid credentials of an account whose password had been reset by the phished cloud administrator on 30 May. Following the principal across the IdP, the cloud control plane and the VPN connected two reports that each saw only one segment of the path.

### 3.5 Expert limitation

Experts are fallible and have incentives: an external firm may be cautious to limit liability; an internal team may be reluctant to find gaps in its own controls; a vendor may minimize its product's role. Ask each expert: *What did you examine? What did you not examine? What would change your conclusion? How confident are you, and why?*

At Calder these questions produced the two clarifying requests: the external firm was asked to review VPN authentication logs for 28 May to 3 June for a named list of accounts, and the internal team was asked whether the 28 May access key was used from the VPN pool or on-premises ranges.

### 3.6 Reconciling disagreements

When reports disagree, tabulate: claim, report A's position and basis, report B's position and basis, what explains the difference (different artefacts, different time windows, different assumptions), and what evidence would discriminate. Often the disagreement dissolves into "they examined different things".

Calder's table is a model. On initial access, report H said VPN exploit on 3 June and report C said phished admin on 28 May. The difference was explained by artefact sets: H never saw IdP logs, and C never examined the VPN. The discriminating evidence was whether the 01:12 session used credentials of an account compromised on 28 May. Once checked, both reports turned out to be partly right.

### 3.7 Confidence statements

A confidence statement gives the conclusion, the confidence level on a defined scale, the main supporting evidence, the main alternative and why it is less likely, and what would change the assessment. Analytic standards in intelligence (for example the US Intelligence Community Directive 203) require such expressions of confidence and the distinction between assumptions and judgements; the same discipline is useful in incident reports.

Calder's statement follows this form: moderate confidence that initial access occurred on 28 May through phishing of a cloud administrator, with the IdP sign-ins, the access key and the 30 May reset as support, and the VPN-exploit theory as the main alternative.

### 3.8 Worked example (synthetic): initial access disputed

*Fictional.* Calder Group's Logistics division was hit by ransomware. Two reports disagree on initial access.

Report H (external forensic firm, host-based): initial access via exploitation of the internet-facing VPN appliance on 3 June, based on appliance logs showing an unusual session at 01:12 and subsequent RDP from the VPN pool to a jump host. Artefacts: appliance logs (30-day retention), jump-host image.

Report C (internal cloud team): initial access via a phished cloud administrator on 28 May, based on IdP sign-ins from an anonymizing service and creation of an access key used later to download a backup. Artefacts: IdP logs, cloud control-plane logs.

Reconciliation table:
| Claim | H | C | Explanation | Discriminating evidence |
|---|---|---|---|---|
| Initial access | VPN exploit 3 June | Phished admin 28 May | Different artefact sets; H never saw IdP logs; C never examined the VPN | Whether the VPN session at 01:12 used credentials of an account compromised on 28 May; whether the cloud key's use links to on-premises hosts |
| Earliest activity | 3 June | 28 May | Window: VPN logs only go back 30 days to 10 May, so H could have seen 28 May activity if it occurred on the VPN | VPN logs for 28 May–3 June |

Clarifying requests: to H — "Please review the VPN authentication logs for 28 May–3 June for sessions by any account in the attached list (the cloud admin and accounts it could reset) and state whether the 01:12 session used valid credentials or an exploit signature." To C — "Please identify whether the access key created on 28 May was used from any address in the VPN pool or Calder's on-premises ranges."

Possible synthesis after responses (fictional): the 01:12 VPN session authenticated with valid credentials of an account whose password was reset by the phished cloud admin on 30 May. Both reports were partly right: initial access was the phishing (28 May); the VPN session was a later step, not an exploit.

Confidence statement: "We assess with moderate confidence that initial access occurred on 28 May through phishing of a cloud administrator. Supporting evidence: IdP sign-ins from an anonymizing service, an access key created minutes later, and a password reset of the account later used on the VPN. The alternative — an exploited VPN vulnerability on 3 June — is less likely because the VPN session authenticated with valid credentials and no exploit signature was found. Our assessment would change if an earlier compromise of the cloud admin's device were found or if the VPN vendor confirms an authentication-bypass vulnerability affecting our version."

### 3.9 Common errors and limits

- Accepting the more authoritative-sounding report without checking what it examined.
- Forcing a single narrative before discriminating evidence is obtained.
- Vague requests ("please look again") to experts.
- Confidence words without defined meaning.

Calder's ransomware case shows how the first error happens. The external firm's report H sounded authoritative and arrived first, but its artefacts were VPN appliance logs and a jump-host image; it never saw the IdP. Reconciling it with report C took two precise requests, one to each team, naming dates, accounts and address ranges. A request to "look again" would have produced two longer versions of the same reports.

### Exercises — chapter 3

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX011 — Deconstruct a report.** *Inputs:* Report H summary. *Steps:* separate artefacts, methods, observations, interpretations and limitations; list what is missing. *Rubric:* 3 = all five layers, missing items named (tool versions, IdP data not examined, retention); 2 = four layers; 1 = summary; 0 = none.

**EX012 — Expert questions.** *Steps:* write five questions to an external firm's lead before accepting their conclusion. *Rubric:* 3 = scope examined/not examined, methods and versions, alternatives considered, confidence basis, what would change the view; 2 = three; 1 = generic; 0 = none.

**EX013 — Precise request.** *Steps:* rewrite "Can the cloud team check the logs again?" into a precise request. *Rubric:* 3 = specific log source, time window, entities, question, output format and deadline; 2 = missing window or entities; 1 = still vague; 0 = none.

**EX014 — Confidence scale.** *Steps:* define a four-level confidence scale for your organization's incident reports with criteria for each level. *Rubric:* 3 = levels with evidential criteria (independent sources, quality, alternatives excluded), distinct from likelihood terms; 2 = levels without criteria; 1 = words only; 0 = none.

**EX015 — Executive version.** *Steps:* rewrite the confidence statement from this chapter's disputed-initial-access worked example for the executive committee in 80 words. *Rubric:* 3 = conclusion, confidence, implication for decisions, what is being done, what could change it; plain language; 2 = too technical; 1 = drops uncertainty; 0 = none.

### Chapter synthesis

Treat specialist reports as layered claims; ask what each expert examined and did not; reconcile disagreements by locating their different evidence; request discriminating evidence precisely; and state conclusions with defined confidence and change conditions.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 12

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes and connection

You will be able to (1) apply proportionality, necessity and least intrusion to investigative and monitoring requests; (2) handle competing duties — to the organization, to employees, to customers and to the law; (3) design a review record that makes an ethical decision auditable; and (4) recommend a less intrusive authorized plan that still answers the question. Chapter 3 dealt with evidence quality; this chapter deals with the legitimacy of obtaining evidence at all. Chapter 7 adds the legal and privacy integration.

### 4.1 Why specialists face harder ethical questions

Specialists receive requests from executives that practitioners never see: "monitor everyone in finance", "read the union representative's email", "keep all logs forever". They also hold the technical means to comply. Ethical competence here is the ability to say "not like that — here is a way that answers your real question" and to document why.

Calder's division head made such a request: full keystroke and screen monitoring of all 120 Financial Services staff for three months, after one alert about one analyst's credential. The specialist's answer was to investigate that credential first and strengthen controls for everyone.

### 4.2 Proportionality and necessity

Data-protection law and human-rights frameworks commonly test interferences with privacy by asking whether they pursue a **legitimate aim**, are **necessary** (no less intrusive means would work) and **proportionate** (the intrusion is balanced against the benefit). The European Data Protection Board's and earlier Article 29 Working Party's guidance on employee monitoring (for example Opinion 2/2017 on data processing at work) applies these ideas to workplace monitoring: blanket, continuous monitoring is rarely proportionate; targeted, time-limited, transparent measures are more defensible. Jurisdictions differ; counsel decides legality, but the specialist designs options that can pass the test.

### 4.3 Competing duties

Responders owe duties to the employer (protect assets), to employees (fair treatment, privacy), to customers and data subjects (protect their data, be honest about breaches), and to the law (preservation, cooperation, non-interference). These conflict: protecting the organization's reputation can tempt under-reporting; protecting assets can tempt over-monitoring. Name the duties in the decision record and show how the plan honours each.

In Calder's monitoring request, the duty to the employer is met by investigating the credential and adding phishing-resistant MFA; the duty to employees by rejecting blanket keystroke and screen capture; and the duty to the law by leaving the legal basis for any enhanced logging to counsel.

### 4.4 Confidentiality and privilege

Investigations may involve information subject to legal privilege, trade secrets or third-party confidentiality. Route such matters through counsel; structure engagement of external investigators so that confidentiality is protected (in some jurisdictions, through counsel), without using privilege to hide facts that must be disclosed.

At Calder, counsel instructed the legal hold on the exposed customer-contact export before operations changed anything, and the investigation repository was limited to six named people. Privilege may protect the analysis, but it cannot delay the GDPR notification that the privacy officer determined was required, and the decision log records both without mixing them up.

### 4.5 Consent and its limits

In employment, consent is rarely "freely given" because of the power imbalance; data-protection authorities generally discourage relying on employee consent for monitoring. Prefer other legal bases established by counsel, combined with transparency (policy notices) and safeguards.

At Calder, option D, 30 days of enhanced logging of data-export events, does not rely on consent. Counsel confirms its legal basis, staff receive notice, and access is limited to two named investigators. Transparency here is a safeguard in its own right: staff know what is logged and why, so the monitoring is less likely to damage trust in the division even though nobody was asked to agree to it.

### 4.6 The review record

An auditable ethical decision records: the request and requester; the stated aim; options considered with intrusion and effectiveness; legal basis (from counsel); safeguards (scope, duration, access, retention, oversight); the decision and decider; and a review date. This record protects the people affected and the people deciding.

Calder's record for the monitoring request follows this list: request from the division head on 14 June; options A to D with intrusion and effectiveness; legal basis for D to be confirmed by counsel; safeguards for D of 30 days, export events only, two named investigators, deletion after closure and staff notice; decision B plus C with D conditional; decider the CISO with counsel and HR; review on 1 July.

### 4.7 Worked example (synthetic): broad monitoring request

*Fictional.* After a single alert that a Financial Services analyst's credential was used from an unknown device, Calder's division head asks the security team to "turn on full keystroke and screen monitoring for all 120 staff in the division for three months".

Aim (legitimate): detect further credential misuse and data theft.

Options:
- A: Full keystroke and screen monitoring of 120 staff for 3 months — highly intrusive, captures personal communications and health information typed in personal portals, low necessity (the alert concerns one credential), high legal risk.
- B: Investigate the specific credential: IdP sign-ins, device registration, data access by the account; interview the analyst with HR — targeted, proportionate.
- C: Strengthen controls for the division: phishing-resistant MFA, device compliance for sign-in, data-loss-prevention rules for bulk exports with alerts reviewed by security — preventive, transparent, low intrusion.
- D: Time-limited enhanced logging (30 days) of data-export events for the division, with notice to staff and access limited to two investigators — targeted to the risk, transparent.

Recommendation: B immediately; C as standing improvement; D if B finds evidence of export or the account had access to high-risk data. Reject A as disproportionate and unnecessary.

Review record (excerpt): Request (division head, 14 June); aim; options A–D with intrusion and effectiveness; legal basis to be confirmed by counsel for D; safeguards for D (30 days, export events only, two named investigators, deletion after case closure, staff notice); decision B+C, D conditional; decider: CISO with counsel and HR; review 1 July.

### 4.8 Common errors and limits

- Treating the requester's proposed method as the requirement rather than their aim.
- Relying on employee consent as a legal basis.
- Recording only the decision, not the alternatives and reasons.
- Ethics reasoning cannot replace legal advice; equally, legality does not guarantee proportionality.

Calder's case shows the first error being avoided. The division head's method was blanket keystroke and screen monitoring, but the aim was to detect further credential misuse and data theft. Options B and C met that aim with far less intrusion, and D stayed available if B found evidence of export. Recording all four options, not only the decision, lets an auditor see that option A was rejected for reasons.

### Exercises — chapter 4

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX016 — Necessity test.** *Inputs:* request to collect all browser history of a team to find who uploaded a confidential file to a personal cloud. *Steps:* propose two less intrusive means and test each for effectiveness. *Rubric:* 3 = proxy/DLP logs filtered to known cloud-storage domains and the file's hash/name; file-share audit of who accessed the file; explains why each answers the question; 2 = one; 1 = accepts request; 0 = none.

**EX017 — Duties map.** *Inputs:* a breach of customer data caused by a misconfiguration made by a well-liked senior engineer. *Steps:* map duties to employer, employee, customers and law, and identify one conflict. *Rubric:* 3 = all four with concrete obligations and a conflict (e.g., fairness to engineer vs complete disclosure of cause); 2 = three; 1 = generic; 0 = none.

**EX018 — Review record.** *Steps:* complete the full review record for option D in this chapter's broad-monitoring-request worked example. *Rubric:* 3 = all fields, safeguards measurable, review date, legal basis left to counsel; 2 = missing safeguards; 1 = narrative; 0 = none.

**EX019 — Pushback script.** *Steps:* write a 120-word response to the division head declining option A while offering a path that meets the aim. *Rubric:* 3 = acknowledges aim, explains risk briefly, offers B/C/D with timelines, invites decision; 2 = declines without alternative; 1 = complies; 0 = none.

**EX020 — Privilege boundary.** *Steps:* describe how you would structure an external forensic engagement with counsel's involvement, and one thing privilege must not be used for. *Rubric:* 3 = engagement via counsel where appropriate, defined scope, separate operational remediation communications, privilege not used to conceal facts subject to disclosure duties; 2 = partial; 1 = misunderstands; 0 = none.

### Chapter synthesis

Test every investigative request for aim, necessity and proportionality; map competing duties explicitly; prefer targeted, transparent, time-limited measures; do not rely on employee consent; and keep an auditable record of alternatives, safeguards and review.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 12

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Alternatives for coordinated containment

### Learning outcomes and connection

You will be able to (1) design containment across cloud and on-premises environments with shared identity; (2) sequence actions to avoid alerting the adversary prematurely or leaving gaps; (3) assess dependencies and blast radius of each action; (4) define approval and rollback gates; and (5) compare two coordinated strategies and recommend one. Chapters 1 and 2 provided decision framing and command; this chapter applies them to the most consequential operational decision in many incidents.

### 5.1 Coordinated versus piecemeal containment

Piecemeal containment — each team acting as it discovers something — warns the adversary and leaves alternative footholds. **Coordinated containment** gathers enough scoping information, then executes a planned set of actions within a short window so that the adversary loses access everywhere at once. The trade-off is time: waiting to coordinate allows harm to continue. The commander decides where on this spectrum to sit, using the thresholds of Chapter 1.

Calder's identity compromise shows the trade-off: the big-bang strategy needed 36 hours of preparation, while executive mailboxes were being read throughout.

### 5.2 Scoping before acting

Coordinated containment needs a scope: compromised identities (users, service principals, keys), hosts, persistence mechanisms, external infrastructure and data at risk. Scope is never complete; decide what level of confidence is "enough" and what monitoring will catch what you missed.

At Calder the scope listed a compromised on-premises domain admin, a synchronized cloud global admin, an OAuth application with mail-read consent, a web shell on the file-transfer server, a partner service principal the adversary may have read, and 300 users whose credentials may have been harvested. Monitoring for old credentials and new persistence was the answer to whatever the list missed.

### 5.3 Identity first

When identity spans cloud and on-premises (for example, directory synchronization or federation), the adversary can re-enter through either side. Typical sequence: revoke sessions and tokens across the IdP and federated applications; reset credentials (including service-account secrets and, where a directory's key-signing material may be compromised, rotate it according to vendor guidance, which may require two resets separated by replication time); remove rogue federation trusts, application consents and MFA registrations; then block known infrastructure. Doing host cleanup before identity containment invites immediate re-compromise.

### 5.4 Dependencies and blast radius

Each action has dependants. Rotating a service-account secret used by twenty integrations breaks them unless updated in step; disabling a federation trust may cut off a partner. Build an action-dependency table with owners who will update dependants in the window.

Calder's partner service principal is the example: its secret was rotated with the partner on the call, and a temporary secret was kept for one hour as rollback. Forcing sign-out and password reset for 300 users had a dependant too: the helpdesk had to be staffed for the calls that followed, which is why it appears on the gate checklist.

### 5.5 Approval and rollback gates

Gates are points where the commander confirms preconditions: scope accepted; dependants ready; communications drafted; monitoring in place. Each action has a rollback plan and a rollback trigger (for example, failure of a critical integration for more than 15 minutes).

Calder's gate checklist named the conditions: scope review signed off, partner engaged, user communication ready, helpdesk staffed, monitoring for old credentials and new persistence deployed, and partner rollback prepared. Its rollback trigger was concrete: if the partner integration was still failing after 30 minutes, the temporary secret would be reinstated under monitoring.

### 5.6 Execution and verification

Execute in a defined window with a single coordinator calling steps and recording completion times. Verify immediately: no successful authentication with old credentials, no activity from revoked sessions, alerts for re-entry attempts.

At Calder the window was two hours on a weekend, with seven steps called in order, from egress blocks to the 300 user resets. Verification afterwards was what later allowed the Day 3 briefing to say that no attacker activity had been seen for 40 hours, and to back that with an assurance table rather than a hope.

### 5.7 Worked example (synthetic): identity compromise across cloud and on-premises

*Fictional.* At Calder Group, an adversary has: a compromised on-premises domain admin account; a cloud global administrator account (synchronized from on-premises); an OAuth application with mail-read consent; and a web shell on an on-premises file-transfer server. A partner integration uses a service principal that the adversary may have read.

Strategy S1 — "big bang" in a 2-hour weekend window: (1) block known adversary IPs and domains at egress; (2) remove web shell and isolate the file-transfer server; (3) disable the OAuth application and revoke its consent; (4) reset the domain admin and cloud global admin, revoke all admin sessions; (5) rotate the directory's key-signing secrets per vendor guidance (twice, with replication interval); (6) rotate the partner service principal secret with the partner on the call; (7) force sign-out and password reset for 300 users whose credentials may have been harvested. Pros: adversary loses all known access simultaneously. Cons: requires 36 hours of preparation; weekend window delays action; large user impact.

Strategy S2 — staged: immediately disable the OAuth app and revoke admin sessions (stops mail reading, the observed harm), then over 48 hours rotate other credentials and remove the web shell. Pros: stops observed harm now. Cons: warns the adversary, who may use the web shell or harvested credentials to establish new persistence.

Gate checklist for S1: scope review signed off; partner engaged; user communication ready; helpdesk staffed; monitoring rules for old credentials and new persistence deployed; rollback for partner integration (temporary secret retained for 1 hour). Rollback trigger: partner integration failing after 30 minutes → reinstate temporary secret under monitoring.

Recommendation (fictional): S1, with one immediate action pulled forward — disabling the OAuth application — because mail reading of executive mailboxes is ongoing harm and the action reveals little about the rest of the plan. This is a hybrid justified by the specific harm and its low signalling cost.

### 5.8 Common errors and limits

- Cleaning hosts before containing identity.
- Rotating shared secrets without dependants ready.
- No verification after execution.
- Treating the plan as final: new scope found during execution needs a decision, not improvisation.
- Vendor-specific steps (for example directory key rotation) must follow current vendor guidance.

Calder's plan avoided the first two errors by design: identity steps (admin resets, session revocation, key-signing secret rotation) were in the same window as host clean-up, and the partner secret was rotated with the partner on the call. Pulling the OAuth app disablement forward was a recorded decision, not an improvisation, justified by ongoing reading of executive mailboxes and the action's low signalling cost.

### Exercises — chapter 5

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX021 — Action-dependency table.** *Steps:* build the table for S1 with action, dependants, owner, readiness check and rollback. *Rubric:* 3 = all seven actions with realistic dependants and rollbacks; 2 = five; 1 = actions only; 0 = none.

**EX022 — Sequence critique.** *Steps:* explain why step 2 (web shell removal) before step 4 (admin resets) might be risky, and propose a better order. *Rubric:* 3 = removal may alert adversary who still holds admin credentials; place host actions in the same window after or simultaneous with identity actions; 2 = partial; 1 = no issue seen; 0 = none.

**EX023 — Choose with criteria.** *Steps:* compare S1, S2 and the hybrid on harm stopped, signalling, user impact, preparation time and residual risk; recommend. *Rubric:* 3 = table and recommendation consistent with criteria and Chapter 1 thresholds; 2 = recommendation without table; 1 = preference only; 0 = none.

**EX024 — Verification plan.** *Steps:* list six verification checks for the hour after execution. *Rubric:* 3 = old-credential authentication attempts, revoked-session activity, new OAuth consents, new federation trusts, web-shell path requests, partner integration health; 2 = four; 1 = two; 0 = none.

**EX025 — Gate briefing.** *Steps:* write the 5-minute gate briefing the commander gives before execution. *Rubric:* 3 = objectives, scope confidence, steps and owners, rollback triggers, communications, go/no-go poll; 2 = missing rollback; 1 = narrative; 0 = none.

### Chapter synthesis

Coordinate containment: scope enough, contain identity first, map dependants, gate on readiness, define rollback triggers, execute in one window with a single coordinator, verify immediately — and pull forward only actions that stop ongoing harm at low signalling cost.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 12

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Controlled evaluation of recovery strategies

### Learning outcomes and connection

You will be able to (1) design a controlled comparison of recovery strategies before committing production; (2) validate restored data against independent references; (3) handle uncertainty in downstream synchronization; (4) define acceptance and fallback criteria; and (5) report the evaluation's limitations. Chapter 5 contained the adversary; this chapter returns services safely. Chapter 8 deals with conflicting evidence, which often surfaces during recovery validation.

### 6.1 Recovery as an experiment

Specialists rarely have one obvious recovery path. Restoring a database from a verified backup may lose recent transactions; replaying logs may reintroduce attacker changes; rebuilding from upstream systems may be incomplete. Rather than choose by intuition, run a **controlled evaluation**: restore candidates into isolated environments, measure them against the same validation suite, and compare. NIST SP 800-184 emphasizes planning, testing and improvement of recovery; SP 800-209 discusses storage infrastructure security including backup protection.

Calder Logistics faced exactly this when its order database was encrypted: a verified nightly backup or a more recent but unverified replica.

### 6.2 Validation references

Validate restored data against references that the adversary did not control: upstream systems of record, partner records, financial reconciliations, previously exported reports with hashes, and samples confirmed by business users. Each reference has its own errors; disagreements must be investigated, not averaged.

At Calder, the warehouse management system was the reference: it independently recorded 1,000 order events between 02:00 and 10:03, including 40 orders flagged as created by the adversary. Counting each candidate against that set showed what each one contained, which neither candidate could show about itself.

### 6.3 Downstream synchronization

Restored systems feed others: a restored order database must re-synchronize with warehouse, invoicing and customer-notification systems. If downstream systems processed data after the restore point, the two can diverge (duplicate shipments, missing invoices). Map the synchronization paths and decide, per path, whether to replay, reconcile or freeze.

Calder's order database feeds warehouse dispatch and invoicing. Restoring the 02:00 backup and reconstructing 960 legitimate orders from the warehouse system meant invoicing had to be reconciled against the rebuilt set, which is why a zero invoicing difference is one of the acceptance criteria.

### 6.4 Acceptance and fallback

Acceptance criteria: data validation thresholds, functional tests, security checks, performance, and owner sign-off. Fallback: if a criterion fails after go-live, what is the path — revert to manual operation, switch to the alternative candidate, or partial operation?

Calder's criteria for the order database were specific: the restored base hash matches the backup manifest; reconstructed orders equal the warehouse system's 960 legitimate orders minus customer cancellations; zero orders go to the fraud drop address; the invoicing difference is zero; and the owner signs off. The fallback was manual dispatch from the warehouse system for 24 hours if reconstruction failed validation.

### 6.5 Worked example and lab (synthetic): two restore candidates

*Fictional.* Calder Logistics' order database was encrypted. Candidate R1: nightly backup from 02:00 (verified hash, immutable storage). Candidate R2: an asynchronous replica whose replication stopped at 09:41, 22 minutes before encryption at 10:03 — more recent but not verified; the adversary had access to the primary from 08:15.

Validation reference: the warehouse management system (WMS) independently recorded 1,000 order events between 02:00 and 10:03, including 40 orders the investigation flagged as created by the adversary (fraudulent orders to a drop address). Save as `lab06.py`.

```python
# Lab PG-06 - compare two restore candidates against an independent reference (synthetic, stdlib only)
import random
random.seed(6)

# Reference (WMS) orders 02:00-10:03: ids 1..1000; ids 601..640 fraudulent (created 08:20-09:30)
legit = set(range(1, 601)) | set(range(641, 1001))
fraud = set(range(601, 641))
order_minute = {i: 120 + (i * 483) // 1000 for i in range(1, 1001)}   # minutes after midnight, 02:00..10:03
replica_stop = 9*60 + 41
R1 = set()                                                           # nightly backup: none of today's orders
R2 = {i for i in range(1, 1001) if order_minute[i] <= replica_stop}
R2 -= set(random.sample(sorted(R2), 7))                              # replication lag losses
for name, cand in (("R1 nightly", R1), ("R2 replica", R2)):
    have_legit = len(cand & legit)
    have_fraud = len(cand & fraud)
    to_reenter = len(legit - cand)
    print(f"{name}: legit present {have_legit}, fraudulent present {have_fraud}, legit to re-enter {to_reenter}")
```

Expected output:

```text
R1 nightly: legit present 0, fraudulent present 0, legit to re-enter 960
R2 replica: legit present 909, fraudulent present 40, legit to re-enter 51
```

Interpretation: R2 saves re-entry of about 900 legitimate orders but contains all 40 fraudulent orders and lost 7 records in replication; it also carries any undiscovered attacker changes made between 08:15 and 09:41. R1 is clean with respect to today's activity but requires re-entering 960 orders from the WMS. A defensible hybrid is: restore R1 (trusted base), then reconstruct today's orders from the WMS (the independent reference), excluding the 40 flagged fraudulent orders and holding for review any order whose attributes match fraud patterns. This uses R2 only as a cross-check, not as a source. The lab's numbers depend on the synthetic generator; the method — counting what each candidate contains against an independent reference — is the point.

Acceptance criteria (excerpt): restored base hash matches backup manifest; reconstructed orders equal WMS legit set (960) minus orders cancelled by customers; zero orders to the fraud drop address; invoicing reconciliation difference zero; owner sign-off. Fallback: if WMS reconstruction fails validation, continue manual dispatch from WMS for 24 hours while investigating.

### 6.6 Common errors and limits

- Choosing the most recent copy by default.
- Validating a restore against itself.
- Ignoring downstream synchronization until duplicates appear.
- Treating an independent reference as perfect — it can be wrong too; investigate disagreements.

Calder's replica R2 shows the first error. It was 22 minutes more recent than encryption at 10:03, but it contained all 40 fraudulent orders and any undiscovered attacker changes made after 08:15. Choosing it by default would have restored the attacker's work. Validating against the warehouse system, not against the database itself, is what exposed the difference, and even that reference needs its flagged orders reviewed, not trusted blindly.

### Exercises — chapter 6

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX026 — Run and explain.** *Steps:* run Lab PG-06; change the seed to 7 and report what changes and what does not. *Rubric:* 3 = output reported; explains that only which 7 replication losses occur changes, counts stay (909/40/51) because the sample size is fixed; 2 = output only; 1 = not run; 0 = none.

**EX027 — Synchronization map.** *Steps:* map downstream paths from the order database (warehouse, invoicing, customer notifications, analytics) and choose replay, reconcile or freeze for each. *Rubric:* 3 = each path with choice and reason (e.g., freeze notifications until reconciled to avoid messaging fraudulent orders); 2 = choices without reasons; 1 = list only; 0 = none.

**EX028 — Acceptance criteria.** *Steps:* complete the acceptance criteria and fallback for the hybrid. *Rubric:* 3 = data, function, security, performance, sign-off; fallback with trigger; 2 = missing security or trigger; 1 = vague; 0 = none.

**EX029 — Evaluation report.** *Steps:* write a 150-word report of the comparison for the commander, including limitations. *Rubric:* 3 = method, results, recommendation, limitations (synthetic generator, reference reliability, undiscovered changes); 2 = no limitations; 1 = opinion; 0 = none.

**EX030 — When to choose R2.** *Steps:* describe conditions under which R2 would be the better base. *Rubric:* 3 = attacker access start verified after replica stop, or strong integrity verification of replica, and re-entry infeasible; 2 = one condition; 1 = vague; 0 = none.

### Chapter synthesis

Treat recovery choices as controlled comparisons: restore candidates in isolation, validate against independent references, map downstream synchronization, define acceptance and fallback — and prefer a clean base rebuilt from trusted references over a recent but untrusted copy.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 12

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Integration across legal, privacy and operations

### Learning outcomes and connection

You will be able to (1) identify notification triggers across overlapping regimes and route them to the right specialist; (2) coordinate legal holds with operational recovery; (3) apply data minimization to the investigation itself; (4) maintain a decision log that separates facts, assessments and specialist determinations; and (5) avoid speculation in records that may be disclosed. Chapter 4 handled ethics; this chapter integrates legal and privacy functions into the running incident. Chapter 9 turns to leadership briefings.

### 7.1 The integration problem

In large incidents, three functions pull in different directions: operations wants to restore quickly (which can destroy evidence), legal wants to preserve and control communications (which can slow operations), and privacy wants to determine exposure precisely (which needs investigative effort). The specialist's job is to make these demands explicit, sequence them and record who decided what.

Calder Financial Services shows all three pulls at once: operations wanted the exposed storage link closed, counsel wanted the object preserved, and the privacy officer needed to know what the customer-tier field revealed. The decision log sequenced them within three hours.

### 7.2 Notification triggers

Triggers vary by regime. Examples to verify for your jurisdictions: the GDPR (personal-data breach notification to the supervisory authority within 72 hours of awareness where feasible, unless unlikely to result in risk); the EU NIS2 Directive (Directive (EU) 2022/2555) for essential and important entities — an early warning within 24 hours of becoming aware of a significant incident, an incident notification within 72 hours and a final report within one month; US public companies' Form 8-K Item 1.05 disclosure within four business days after determining a cybersecurity incident is material (SEC rule adopted 2023); sector rules (health, finance) and contracts with customers and partners. Each regime defines "awareness" and "significant" differently. The specialist ensures that the facts needed for each determination are produced on time — and that awareness timestamps are recorded.

### 7.3 Legal hold and operational recovery

When counsel issues a hold, operations must preserve specified data. Conflicts arise when recovery reimages systems or rotates logs. Resolve by preserving before changing: capture images, export logs, snapshot cloud resources, record hashes, then proceed. Build this into recovery runbooks so it is not negotiated under pressure.

At Calder Financial Services the order was right: counsel instructed the hold at 11:12, and at 11:20 operations disabled the storage link while retaining the exported object under that hold. Closing the exposure did not require deleting anything, so preservation cost a few minutes, not the evidence.

### 7.4 Minimization in the investigation

Investigations themselves process personal data. Apply minimization: collect what the question requires, restrict access to investigation repositories, pseudonymize in working analyses, and set retention for case data (bachelor's Chapter 14 covers the basics). Over-collection increases the breach surface of the investigation.

Calder's repository for the customer-contact exposure is the pattern: at 14:00, access was limited to six named people, and working analyses used pseudonymized customer IDs. The investigation needed to know which records were in the export, not to read 52,000 names, emails and phone numbers again and again.

### 7.5 The decision log

Maintain one log in which each entry has: time; type (fact, assessment, determination, decision, action); content; source or basis; owner; and, for determinations, the specialist responsible (for example, "Privacy officer determined notification to authority required under GDPR Art. 33"). Facts come from evidence; assessments from analysts; determinations from qualified specialists; decisions from the authorized owner.

Calder Financial Services' log shows every type in use: the 11:05 fact from storage access logs, the 11:20 action, the 11:40 assessment with moderate confidence, the privacy officer's 12:30 determination, counsel's 13:15 determination and the commander's 13:30 decision.

### 7.6 Avoiding speculation in records

Incident records may be disclosed in litigation or regulatory inquiry. Write precisely: facts with sources, assessments with confidence, no guesses about motives or blame, no casual statements ("we totally missed this"). This is not concealment; it is accuracy.

Calder's log ends with an explicit note of what is absent: no speculation about who downloaded the data, and no characterization of the misconfiguration as anyone's negligence. The 11:40 entry calls exposure "likely" with moderate confidence and gives the reason, three downloads whose size matches the object, rather than asserting that all 52,000 records were stolen.

### 7.7 Worked example (synthetic): customer contact records

*Fictional.* Calder Financial Services, operating in an EU member state and listed in the US, finds that an export of 52,000 customer contact records (name, email, phone, customer tier) was accessible through a misconfigured storage link for 9 days. Access logs show 3 downloads from unknown addresses.

Decision log (excerpt):
- 11:05 Fact — Storage access logs show the export object downloaded 3 times from two unknown addresses on 4 and 6 June (source: storage access log export, hash recorded).
- 11:20 Action — Link disabled; object retained under legal hold (operations; counsel instructed hold at 11:12).
- 11:40 Assessment — Exposure of contact data for 52,000 customers is likely (confidence moderate: downloads observed; content of the downloads matches the object size).
- 12:30 Determination — Privacy officer: personal-data breach; notification to the supervisory authority required (GDPR Art. 33); awareness time recorded as 10:52 when the security team confirmed exposure. Deadline: 72 hours.
- 13:15 Determination — Counsel: NIS2 does not apply to this entity (classification reviewed); materiality under SEC rules to be assessed by disclosure committee; contractual notifications to two partners required within 48 hours.
- 13:30 Decision — Incident commander: customer notification preparation begins in parallel; final decision after privacy officer's risk assessment of the customer-tier field (could indicate wealth status).
- 14:00 Action — Investigation repository access limited to six named people; working analyses use pseudonymized customer IDs.

Note what is absent: no speculation about who downloaded the data, no characterization of the misconfiguration as anyone's negligence.

### 7.8 Common errors and limits

- Not recording awareness time, making deadlines indefensible.
- Responders making legal determinations.
- Recovery destroying held data.
- Investigation repositories becoming the next breach.
- Regulatory details change; verify current texts and seek counsel.

Calder's log avoids the first error: it records awareness at 10:52, when the security team confirmed exposure, which starts the 72-hour GDPR clock. The determinations come from the privacy officer and counsel, not from responders. The legal hold came before the link was disabled. And the repository was restricted to six people with pseudonymized IDs, so the investigation did not create a second copy of the problem.

### Exercises — chapter 7

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX031 — Trigger matrix.** *Steps:* build a matrix of regimes (GDPR, NIS2, SEC 8-K, one sector rule, contracts) with trigger, clock start, deadline and determining specialist for the entity in this chapter's customer-contact-records worked example. *Rubric:* 3 = accurate, verifiable entries with sources and "to verify" where unsure; 2 = some errors; 1 = generic; 0 = none.

**EX032 — Preserve-then-change runbook.** *Steps:* write the preservation steps that precede reimaging a server under legal hold. *Rubric:* 3 = memory capture if relevant, disk image with hash, log export, configuration snapshot, chain-of-custody record, counsel confirmation; 2 = missing hashes/custody; 1 = "back it up"; 0 = none.

**EX033 — Classify log entries.** *Inputs:* five entries: "IP 198.51.100.4 downloaded the file"; "The attacker is probably a competitor"; "Notification required under Art. 33"; "Disable the link"; "Exposure likely". *Steps:* classify each and fix any that do not belong. *Rubric:* 3 = fact, speculation (remove or reframe), determination (needs owner), decision/action, assessment (needs confidence); 2 = one error; 1 = no fixes; 0 = none.

**EX034 — Minimization plan.** *Steps:* write a minimization plan for the investigation repository in this chapter's customer-contact-records worked example. *Rubric:* 3 = data scope, pseudonymization, access list, retention, deletion, audit; 2 = four elements; 1 = vague; 0 = none.

**EX035 — Awareness dispute.** *Inputs:* an analyst noticed an odd link on 8 June but escalated on 11 June. *Steps:* explain how awareness might be argued and what the specialist should record. *Rubric:* 3 = explains that awareness generally means reasonable certainty of a breach, determined by counsel; record both times and facts; do not backdate or omit; 2 = partial; 1 = picks the later date silently; 0 = none.

### Chapter synthesis

Integrate legal, privacy and operations through one decision log that separates facts, assessments, specialist determinations and decisions; record awareness times; preserve before changing; minimize the investigation's own data; and write records that remain accurate when disclosed.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 12

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Difficult cases with conflicting evidence

### Learning outcomes and connection

You will be able to (1) build a hypothesis–evidence matrix and use it to find diagnostic evidence; (2) assess provenance and missingness when sources conflict; (3) seek disconfirmation deliberately; and (4) express confidence that reflects unresolved conflict. Chapter 3 reconciled specialist reports; this chapter handles cases where conflict persists. Chapter 9 shows how to brief leaders before it is resolved.

### 8.1 When evidence conflicts

Conflict has a limited number of sources: different things were measured; one source is wrong (clock error, parsing, configuration); one source was manipulated; the world is more complex than the hypotheses (both sources right, hypotheses incomplete). Each predicts different follow-up results; that is how you discriminate.

Calder Retail's payroll export is such a conflict: identity logs name `hr-lead-2`, while the HR workstation's host timeline shows only `hr-assist-5` logged on at the time. Each of the four sources of conflict gives a hypothesis to test.

### 8.2 Analysis of competing hypotheses

Heuer's *Psychology of Intelligence Analysis* (CIA Center for the Study of Intelligence, 1999) describes **Analysis of Competing Hypotheses** (ACH): list hypotheses, list evidence, mark each cell as consistent, inconsistent or neutral, focus on evidence that is **diagnostic** (consistent with some hypotheses and inconsistent with others), and prefer the hypothesis with the least inconsistent evidence rather than the most consistent. ACH does not produce truth; it structures attention and exposes assumptions.

Calder's lab shows the method: of four hypotheses, H2 has no inconsistent evidence, H1 and H4 one each, and H3 two.

### 8.3 Provenance and missingness

Weight evidence by provenance (who recorded it, how, with which dependencies) and by what could have been missing. A log that would have recorded an event if it occurred, but did not, is diagnostic; a log that was not collecting at the time is neutral.

In Calder's payroll case, the application's record of who performed the export is weighted by how it is produced: if the application records the token owner rather than the session user, the identity log's naming of `hr-lead-2` is consistent with several hypotheses. That is why H4, a logging or attribution error, stays on the list until the deployed version is tested.

### 8.4 Seeking disconfirmation

For the leading hypothesis, ask "what would we expect to see if it were false?" and look for that. Confirmation bias pushes teams to collect more consistent evidence, which is often non-diagnostic.

For Calder's leading hypothesis, H2, the team named what would disconfirm it: `hr-assist-5` on a video call in another application with keyboard activity at 22:47, or `hr-lead-2` admitting to sharing credentials for a legitimate task. It also checks the assumptions behind the diagnostic evidence: DHCP lease records for the workstation address, and a lab test of how the application records users.

### 8.5 Worked example and lab (synthetic): two accounts, one timeline

*Fictional.* At Calder Retail, payroll data was exported at 22:47 on 9 June. Identity logs show the export performed by `hr-lead-2`; the host timeline from the HR workstation shows `hr-assist-5` logged on interactively at 22:40–23:05 and no `hr-lead-2` logon.

Hypotheses: H1 `hr-lead-2`'s credentials were stolen and used remotely; H2 `hr-assist-5` used `hr-lead-2`'s credentials at the workstation (credential sharing or theft by a colleague); H3 a scheduled export ran under `hr-lead-2`'s delegated token, and `hr-assist-5`'s presence is coincidental; H4 a logging or attribution error (the application records the token owner, not the session user).

Save as `lab08.py`.

```python
# Lab PG-08 - a hypothesis-evidence matrix with diagnosticity (synthetic, stdlib only)
H = ["H1 remote theft", "H2 local use by colleague", "H3 scheduled job", "H4 attribution error"]
# C = consistent, I = inconsistent, N = neutral
E = {
    "E1 IdP: export by hr-lead-2 at 22:47":                 "CCCC",
    "E2 host: hr-assist-5 interactive 22:40-23:05":           "NCNN",
    "E3 IdP sign-in for hr-lead-2 from workstation IP 22:44": "ICIC",
    "E4 no scheduled job in export service config":           "CCIC",
    "E5 app docs: records session user, not token owner":     "CCCI",
}
def tally():
    inc = {h: 0 for h in H}
    for ev, marks in E.items():
        for h, m in zip(H, marks):
            inc[h] += (m == "I")
    return inc
print("inconsistencies:", tally())
diag = [ev for ev, m in E.items() if len(set(m) - {"N"}) > 1]
print("diagnostic evidence:", diag)
```

Expected output:

```text
inconsistencies: {'H1 remote theft': 1, 'H2 local use by colleague': 0, 'H3 scheduled job': 2, 'H4 attribution error': 1}
diagnostic evidence: ['E3 IdP sign-in for hr-lead-2 from workstation IP 22:44', 'E4 no scheduled job in export service config', 'E5 app docs: records session user, not token owner']
```

Interpretation: H2 has no inconsistent evidence; H1 and H4 one each; H3 two. E1 is consistent with everything and so is not diagnostic — yet it is the evidence most teams would cite first. The diagnostic items are E3, E4 and E5. Before concluding, test the assumptions behind them: is the workstation IP in E3 really that workstation (DHCP lease records)? Is E5's documentation accurate for the deployed version (test in a lab)? Is there another job scheduler? Seek disconfirmation of H2: if `hr-assist-5` was on a video call in another application at 22:47 with keyboard activity, or if `hr-lead-2` admits sharing credentials for a legitimate task, the picture changes. Note the ethical and HR dimension: H2 implicates a named person; handle through HR and counsel with due process (Chapter 4), and do not circulate the hypothesis widely.

Confidence statement: "The export at 22:47 was most likely performed using `hr-lead-2`'s credentials from the HR workstation while `hr-assist-5` was logged on there (moderate confidence). Remote credential theft is less likely because the sign-in came from the workstation's address. This assessment depends on the workstation address mapping and on the application recording the session user; both are being verified. No conclusion about any individual's intent is drawn."

### 8.6 Common errors and limits

- Counting consistent evidence instead of focusing on inconsistent and diagnostic evidence.
- Treating the matrix as a calculator; the marks are judgements that need provenance.
- Omitting the "error in the evidence" hypothesis.
- Concluding about people's intent from technical evidence.

Calder's matrix shows the first error clearly: E1 was consistent with every hypothesis and so told the team nothing, yet it was the evidence most teams would cite first. H4, the error-in-the-evidence hypothesis, stayed on the list. And because H2 implicates a named person, the confidence statement ends with "no conclusion about any individual's intent is drawn", with HR and counsel handling the next steps.

### Exercises — chapter 8

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX036 — Run and extend.** *Steps:* run Lab PG-08; add evidence E6 "DHCP shows workstation IP assigned to a different host at 22:44" marked appropriately; report the change. *Rubric:* 3 = sensible marks (for example E6 = "CINC"), output reported, E3's reliability reassessed; 2 = output only; 1 = not run; 0 = none.

**EX037 — Missingness.** *Steps:* explain how you would treat the absence of `hr-lead-2` logon on the host timeline — diagnostic or neutral — and what determines it. *Rubric:* 3 = depends on whether the host logs network/remote logons and whether a web session would produce a host logon at all; likely neutral for a web application; 2 = partial; 1 = treats as proof; 0 = none.

**EX038 — Disconfirmation plan.** *Steps:* list three tests that could disconfirm H2. *Rubric:* 3 = specific, non-intrusive first (application session device ID, browser profile on workstation, other activity of hr-assist-5 at 22:47), with HR involvement for interviews; 2 = two; 1 = generic; 0 = none.

**EX039 — Assumption register.** *Steps:* list the assumptions behind E3–E5 with how to verify each. *Rubric:* 3 = IP-to-host mapping, clock alignment, app attribution semantics, completeness of job configs; verification methods; 2 = two; 1 = vague; 0 = none.

**EX040 — Communication boundary.** *Steps:* write who should know about H2 at this stage and why. *Rubric:* 3 = need-to-know: commander, HR lead, counsel, investigators; not the wider team or the named person's manager without HR; reasons: fairness, legal risk, evidence integrity; 2 = partial; 1 = broadcast; 0 = none.

### Chapter synthesis

In conflicting cases, list competing hypotheses including evidence error, focus on diagnostic and inconsistent evidence, verify the assumptions that make evidence diagnostic, seek disconfirmation, and state confidence without conclusions about intent.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 12

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Response leadership and assurance decisions

### Learning outcomes and connection

You will be able to (1) brief executives and boards with fact-limited statements before root cause is known; (2) make and record assurance claims with their basis; (3) define measurable closure conditions; (4) set a review cadence; and (5) accept or escalate residual risk at the right level. Chapters 1–8 built decisions, structure and evidence; this chapter is about leading with them upward.

### 9.1 The leadership gap after containment

After containment, pressure shifts: executives want to know "are we safe?", "who did it?", "what will it cost?" — often before the investigation can answer. Leaders who over-promise ("we are fully secure") create reputational and legal risk; leaders who say nothing lose trust and control of the narrative. The specialist provides fact-limited briefings that are useful without being speculative.

Calder's Day 3 briefing found that balance: it said no attacker activity had been seen in 40 hours, and also that how the attacker first got in was not yet known.

### 9.2 Assurance claims

An **assurance claim** is a statement that a property holds ("the adversary no longer has access to our identity platform") with a basis (tests, evidence, coverage) and a confidence. Assurance cases in safety engineering structure claims, arguments and evidence (for example Goal Structuring Notation). For incidents, a simple table suffices: claim, evidence, coverage gaps, confidence, owner. Never make an assurance claim whose evidence you cannot show.

Calder's Day 3 table has such a row: the claim "no attacker access to identity platform" rests on no authentications with old credentials, no new federation trusts or consents in 40 hours and tested monitoring rules, with the unknown initial access route as the stated gap and moderate confidence.

### 9.3 Briefing structure

For executives: bottom line (one sentence), what we know (with confidence), what we don't know yet (and when we expect to), what we have done, decisions needed from you, risks to watch, next briefing. Keep technical detail in an appendix. For boards: add implications for strategy, regulation and oversight duties, and the residual risks they are being asked to accept.

Calder's Day 3 briefing follows this order. Its bottom line is one sentence; the payment-systems claim carries moderate confidence because logs earlier than 30 days were unavailable; and its two decisions are funding phishing-resistant MFA for administrators and accepting residual risk of undiscovered persistence until the monitoring period ends.

### 9.4 Closure conditions

An incident should close when measurable conditions are met, not when attention fades. Typical conditions: containment verified for a defined period with monitoring; eradication tests passed; recovery accepted by owners; notifications completed; evidence preserved; corrective actions assigned with owners and dates; post-incident review scheduled. Residual risks transferred to the risk register.

Calder's identity incident set its conditions in advance: 30 days without re-entry indicators; initial access identified and remediated, or documented as unknown with compensating controls; mailbox exposure determined and notifications completed; corrective actions assigned; and a review held. The second condition admits that an answer may never come.

### 9.5 Delegation and residual risk acceptance

Residual risk must be accepted by someone with authority proportional to its size. Define in advance which levels accept what (for example, the CISO up to a threshold; the executive committee above it; the board for risks affecting strategy).

At Calder, the residual risk that undiscovered persistence exists until the 30-day monitoring period ends was put to the executive committee in the Day 3 briefing, not accepted by the incident commander, because it affected the whole group's identity platform. A lower-impact risk, such as a single division's delayed log review, would sit within the CISO's threshold.

### 9.6 Review cadence

After closure: 30-day check of monitoring results and corrective actions; 90-day review of effectiveness; inclusion in quarterly risk reporting.

For Calder's identity compromise, the 30-day check coincides with the end of the re-entry monitoring period set in the closure conditions. It asks whether any indicator fired and whether phishing-resistant MFA for administrators has been funded and deployed as decided on Day 3. The 90-day review asks whether the corrective actions worked: whether the initial access route has been found or documented as unknown with compensating controls. Quarterly risk reporting keeps the accepted residual risk visible until it is retired.

### 9.7 Worked example (synthetic): executive briefing before root cause

*Fictional.* Day 3 of the Calder identity compromise (Chapter 5). Containment executed Saturday; root cause (how the domain admin credential was first obtained) not yet established.

Briefing (excerpt):
- **Bottom line:** We removed all known attacker access on Saturday and have seen no attacker activity in the 40 hours since; we do not yet know how the attacker first got in.
- **Known (confidence):** Attacker accessed executive mailboxes via a malicious app for 6 days (high); attacker held domain and cloud admin rights (high); no evidence of access to payment systems, which are separately managed (moderate — logs reviewed for 30 days; earlier logs unavailable).
- **Not yet known:** initial access route (expected within 5 days from forensic firm); full list of mailbox items read (expected 48 hours).
- **Done:** containment in one window; 300 users reset; monitoring for re-entry in place.
- **Decisions needed:** approve funding for phishing-resistant MFA for all administrators (€X, 6 weeks); accept residual risk that undiscovered persistence exists until the 30-day monitoring period ends.
- **Next briefing:** Thursday 08:00.

Assurance table (excerpt): Claim "no attacker access to identity platform" — evidence: no authentications with old credentials, no new federation trusts or consents in 40 hours, monitoring rules tested — gaps: unknown initial access route — confidence: moderate — owner: identity workstream lead.

Closure conditions: 30 days without re-entry indicators; initial access identified and remediated or documented as unknown with compensating controls; mailbox exposure determined and notifications completed; corrective actions assigned; review held.

### 9.8 Common errors and limits

- "We are secure" without basis.
- Closing when attention fades rather than when conditions are met.
- Residual risk accepted by whoever is in the room.
- Technical detail crowding out decisions in executive briefings.

Calder's Day 3 briefing avoids each error. It never says "we are secure"; it says no attacker activity has been seen for 40 hours, with an assurance table behind the claim. Closure waits for the 30-day conditions. The residual risk of undiscovered persistence goes to the executive committee as a decision. Technical detail stays in the appendix, and the decisions needed are listed on the first page.

### Exercises — chapter 9

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX041 — Rewrite a briefing.** *Inputs:* "The hackers are gone. Our team did an amazing job. We think it was a nation-state." *Steps:* rewrite as a fact-limited executive briefing. *Rubric:* 3 = the briefing structure taught in this chapter, claims with confidence, no attribution speculation, decisions requested; 2 = structure partly; 1 = minor edits; 0 = none.

**EX042 — Assurance table.** *Steps:* write three rows of an assurance table for the end of a ransomware recovery. *Rubric:* 3 = claims with evidence, coverage gaps, confidence and owner; 2 = missing gaps; 1 = claims only; 0 = none.

**EX043 — Closure conditions.** *Steps:* write closure conditions for a business email compromise that caused a fraudulent payment. *Rubric:* 3 = account containment verified, mail rules removed, payment recovery status, bank and law-enforcement reports, supplier verification controls, notifications, corrective actions; measurable; 2 = five; 1 = vague; 0 = none.

**EX044 — Risk acceptance matrix.** *Steps:* design a matrix that assigns residual-risk acceptance authority by impact level. *Rubric:* 3 = levels with criteria and accepting roles, review periods; 2 = levels without criteria; 1 = one role; 0 = none.

**EX045 — Board paper.** *Steps:* write a 200-word board paper section on the Calder incident's residual risks and requested decisions. *Rubric:* 3 = oversight framing, residual risks with likelihood/impact, decisions, timeline for assurance; 2 = operational detail dominates; 1 = narrative; 0 = none.

### Chapter synthesis

Lead upward with fact-limited briefings, evidence-backed assurance claims, measurable closure conditions, residual risk accepted at the right level and a review cadence that outlasts the incident's attention span.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue studying — chapter 09 of 12

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes and connection

You will be able to (1) read a published response-effectiveness study for design, population, outcome and limitations; (2) distinguish industry surveys, vendor incident datasets and academic studies; (3) judge whether a finding transfers to your organization; and (4) turn a published claim into a local validation question. Specialists are asked "what does the evidence say?" constantly; this chapter teaches the reading that the answer needs. Chapter 11 uses it to justify a program redesign.

### 10.1 Kinds of evidence about response effectiveness

- **Industry surveys and cost studies** — for example IBM's annual *Cost of a Data Breach* report (research conducted by the Ponemon Institute), which interviews organizations that experienced breaches and estimates costs, comparing groups by practices such as incident-response planning and testing.
- **Incident-response provider datasets** — for example Mandiant's annual *M-Trends*, which reports metrics such as median dwell time across incidents the firm investigated.
- **Breach corpora** — for example Verizon's *Data Breach Investigations Report*, built from contributed incident and breach data.
- **Academic studies** — controlled experiments, observational studies of organizations, qualitative studies of teams.
Each has typical strengths and biases; none is "the evidence" alone.

### 10.2 A reading protocol

For any study, record: (1) question; (2) population and how it was sampled; (3) unit of analysis (incident, organization, analyst); (4) outcome and how measured; (5) comparison and design; (6) confounders addressed; (7) results with uncertainty; (8) limitations stated and unstated; (9) funding and interests; (10) applicability to your setting.

Applied to the two Calder readings, the protocol exposes their limits quickly. The cost report's population is breached organizations that agreed to be interviewed, with costs from an activity-based model; the provider report's population is incidents that one provider investigated, and its client mix changes each year. Neither is Calder's population of 400 mostly small, internally handled incidents a year.

### 10.3 Typical biases

- **Selection**: provider datasets include only incidents the provider was hired for — usually larger, more severe, or in organizations that buy such services. Survey participants are organizations willing to participate.
- **Survivorship and detection**: dwell time can only be measured for detected intrusions; an improvement in median dwell time can reflect better detection of short intrusions, more ransomware (which announces itself) or a changing mix.
- **Confounding**: organizations with tested IR plans also tend to have more security budget, maturity and staff; lower breach cost may reflect all of these.
- **Measurement**: costs estimated by models and interviews; categories change between editions.
- **Interest**: vendors publish data that may support their products; this does not make the data wrong, but readers should look for it.

### 10.4 Transfer and local validation

A finding transfers when the mechanism plausibly operates in your setting and your population resembles the study's. Rather than adopting a headline number ("IR testing saves $X"), formulate a local question your own data can address: "Did our tabletop-tested playbooks shorten our time from detection to containment for comparable incidents?" — with the methods of bachelor's Chapter 33 and master's-level design if needed.

Calder's local question follows this approach: for incidents of severity 2 or higher in 2025–2026, is time from detection to containment shorter for incident types with a tabletop-tested playbook, after accounting for incident type and division? Calder's own case records can answer it, which no external report can.

### 10.5 Worked example: two published sources, different populations

*Sources (read the current editions yourself; figures change annually):* IBM, *Cost of a Data Breach Report*; Mandiant (Google Cloud), *M-Trends*.

Claim type A (cost report): organizations with incident-response teams and regularly tested IR plans report lower average breach costs than those without. Reading: population = breached organizations that agreed to be interviewed, across countries and industries; unit = breach; outcome = estimated total cost via an activity-based model; comparison = cross-sectional groups by practice; confounders = partially addressed by reporting factors' associations with cost; limitations: self-selection, model-based costs, correlation not causation, practices co-occur.

Claim type B (provider report): global median dwell time has declined over the years. Reading: population = incidents investigated by the provider; unit = intrusion; outcome = time from earliest evidence of compromise to detection; comparison = across years; limitations: provider client mix changes, detection of intrusions that are never found is impossible, ransomware share affects the median, definitions of "earliest evidence" depend on available logs.

Transfer to Calder Group (synthetic): Calder's 400 incidents a year are mostly small and internally handled — unlike B's population. Calder is a large retailer and logistics firm; A's sample includes similar organizations but cost drivers (regulation, region) differ. Local validation question: "For Calder incidents of severity 2 or higher in 2025–2026, is time from detection to containment shorter for incident types with a tabletop-tested playbook than for those without, after accounting for incident type and division?"

### 10.6 Common errors and limits

- Quoting headline numbers without population and method.
- Treating year-over-year changes in provider datasets as global trends.
- Inferring causation from cross-sectional surveys.
- Dismissing vendor research entirely; it is often the only large-scale data — read it carefully instead.

The two reports read for Calder show where each error comes from. Quoting the cost report's lower average breach cost for tested plans as a saving would ignore self-selection and a cross-sectional comparison. Treating the provider's falling dwell time as a global trend would ignore its changing client mix. Yet both are worth reading: they suggest the local question Calder can test with its own data.

### Exercises — chapter 10

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX046 — Protocol on a real report.** *Steps:* apply the ten-point protocol to the current edition of one of the two reports, citing page numbers. *Rubric:* 3 = all ten points with page references and unstated limitations identified; 2 = seven; 1 = summary; 0 = none.

**EX047 — Dwell-time mechanisms.** *Steps:* list four mechanisms other than "defenders got better" that could reduce median dwell time in a provider dataset. *Rubric:* 3 = ransomware share, client mix, earlier engagement, log retention changes, definition changes; 2 = three; 1 = one; 0 = none.

**EX048 — Confounding diagram.** *Steps:* draw a causal diagram for "tested IR plan → lower breach cost" with at least three confounders. *Rubric:* 3 = budget, maturity, industry/regulation, size, insurance; correct arrows; 2 = two confounders; 1 = no confounders; 0 = none.

**EX049 — Local question.** *Steps:* write a local validation question and design sketch for the claim "automation reduces breach lifecycle". *Rubric:* 3 = bounded question, outcome definition, comparison, confounders, data source, limitation; 2 = missing comparison; 1 = restated claim; 0 = none.

**EX050 — Executive summary of evidence.** *Steps:* write 120 words for executives answering "does IR testing pay off?" *Rubric:* 3 = honest synthesis: consistent association in surveys, causal evidence limited, plausible mechanisms, local measurement plan; 2 = overclaims; 1 = headline number only; 0 = none.

### Chapter synthesis

Read every study for population, unit, outcome, comparison and interests; recognize selection, detection and confounding biases typical of industry data; transfer findings only through plausible mechanisms; and convert published claims into local validation questions.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue studying — chapter 10 of 12

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Applied project: redesign an incident program

### Learning outcomes and connection

You will be able to (1) conduct a gap assessment of an incident program using evidence; (2) generate and compare design options; (3) pilot one change with an evaluation plan; (4) evaluate the pilot against explicit criteria; and (5) involve stakeholders throughout. This project integrates the whole book: decision framing (1), command (2), evidence (3, 8), ethics and law (4, 7), containment and recovery (5, 6), leadership (9) and research reading (10). Chapter 12 transfers the results into the organization.

### 11.1 Gap assessment

Assess the program against a reference (NIST SP 800-61 Rev. 3 and CSF 2.0 outcomes; the FIRST CSIRT Services Framework for service scope) and against its own incident data. Evidence sources: case records, after-action reports, interviews, exercise results, metrics. A gap is a difference between required and actual capability, backed by evidence, with an impact statement.

Calder's assessment found two gaps this way: after-action reports cited handoff delays in 9 of 14 major incidents, and case records were incomplete in 40% of severity-2 cases. Each is a measured difference between what the charter requires and what happened.

### 11.2 Prioritization

Prioritize gaps by impact, frequency and feasibility. Recurring findings across after-action reports are strong signals; one dramatic incident is a weaker one.

Calder's handoff gap qualified as a strong signal on all three counts: it recurred in 9 of 14 after-action reports, it delayed the incoming lead's first action on live cases, and the cheapest option, a template with read-back, could be piloted in weeks. A single spectacular failure in one division would have been weaker evidence, however memorable. The 40% incomplete case records were linked to the same handoffs, so one change might address both gaps.

### 11.3 Design options

For each priority gap, generate at least two options with different cost and disruption profiles (process change, tooling, staffing, training, contractual). Evaluate them with the multi-criteria method used at bachelor's level, weights agreed with stakeholders.

Calder's options were a handoff template with read-back (process, low cost), a case-management workflow with required fields and reminders (tooling, medium cost), or both. The template was piloted first because it could be tested in weeks, while the workflow became a budget item for the next cycle.

### 11.4 Piloting

Choose one change to pilot in a bounded part of the organization for a defined period, with criteria fixed in advance, a comparison (another division or the pre-period, ideally both), data collection plan and stop rules.

Calder's pilot met each requirement: option A in the Logistics division for 8 weeks, with Retail as a concurrent comparison; criteria fixed in advance, a 20% fall in median minutes to first action, 85% record completeness and no increase in time to containment; and data from case-system events. Choosing one change made the result attributable.

### 11.5 Evaluation

Evaluate against the criteria; include process measures (was the change used as designed?), outcome measures, and unintended effects. Report uncertainty; small pilots rarely give precise effects.

Calder's result shows why the comparison and the caveats matter. Median minutes to first action fell 36% in Logistics and 5% in Retail over the same weeks, and completeness reached 87%. But with 10 to 12 handoffs per period, staff aware they were in a pilot, and a template that also prompts record completion, the effect is an estimate, and time to containment still had to be checked before rollout.

### 11.6 Worked example and lab (synthetic): handoff delays

*Fictional.* Calder's after-action reports from the past year show handoff delays in 9 of 14 major incidents; case records are incomplete in 40% of severity-2 cases. Gap: no standard handoff or minimum case-record content. Options: (A) handoff template plus read-back (process; low cost); (B) case-management workflow with required fields and automated reminders (tooling; medium cost); (C) both. Pilot: option A in the Logistics division for 8 weeks; Retail as a concurrent comparison. Criteria: median minutes from shift change to the incoming lead's first action on the case falls by at least 20%; case-record completeness (required fields present at closure) reaches 85%; no increase in time to containment.

Save as `lab11.py`.

```python
# Lab PG-11 - evaluate a handoff pilot with a concurrent comparison (synthetic, stdlib only)
from statistics import median

# minutes from shift change to incoming lead's first action, per handoff
LOG_PRE  = [42, 35, 50, 38, 61, 44, 39, 47, 55, 40]
LOG_POST = [25, 31, 22, 40, 28, 19, 33, 27, 36, 24, 30, 26]
RET_PRE  = [45, 37, 52, 41, 48, 39, 58, 43]
RET_POST = [44, 40, 39, 47, 51, 38, 42, 46, 41]
COMPLETE = {"Logistics": (47, 54), "Retail": (31, 49)}   # (complete records, closed cases) in pilot weeks

def pct(a, b): return 100 * (b - a) / a
lp, lq, rp, rq = map(median, (LOG_PRE, LOG_POST, RET_PRE, RET_POST))
print(f"Logistics median {lp} -> {lq} ({pct(lp, lq):+.0f}%)")
print(f"Retail    median {rp} -> {rq} ({pct(rp, rq):+.0f}%)")
print(f"difference in change: {pct(lp, lq) - pct(rp, rq):+.0f} percentage points")
for d, (c, n) in COMPLETE.items():
    print(f"{d} completeness {c}/{n} = {100*c/n:.0f}%")
```

Expected output:

```text
Logistics median 43.0 -> 27.5 (-36%)
Retail    median 44.0 -> 42 (-5%)
difference in change: -32 percentage points
Logistics completeness 47/54 = 87%
Retail completeness 31/49 = 63%
```

Interpretation: in Logistics, median minutes to first action fell 36% while Retail fell 5% over the same weeks; the difference (about 32 points) suggests most of the improvement is associated with the pilot rather than seasonal factors. Completeness reached 87% against an 85% criterion. Caveats: 10–12 handoffs per period are few; divisions differ; staff knew they were in a pilot; the template also prompts record completion, so the two outcomes are not independent. Time to containment (not shown) must be checked for adverse effects before rollout. Recommendation: extend the template group-wide with option B scoped for the next budget cycle, and continue measurement.

### 11.7 Common errors and limits

- Gaps asserted without evidence.
- Piloting several changes at once, so effects cannot be separated.
- Criteria set after results.
- Declaring success from small samples without a comparison.

Calder's pilot avoided each of these errors. The two gaps came from after-action reports and case records, not from opinion. Only option A was piloted, with B deferred to the budget cycle. The 20% and 85% criteria were set before the eight weeks began. Retail served as a concurrent comparison, which separated the pilot's effect from seasonal change. Even so, the small number of handoffs is reported as a limit, and rollout includes continued measurement.

### Exercises — chapter 11

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX051 — Gap statement.** *Steps:* write two evidence-backed gap statements for Calder with impact. *Rubric:* 3 = requirement, evidence (sources, counts), impact, owner; 2 = no evidence counts; 1 = opinion; 0 = none.

**EX052 — Option comparison.** *Steps:* compare A, B and C on cost, time to implement, disruption, expected effect and evidence strength; recommend a pilot. *Rubric:* 3 = table and justified pilot choice (A first because cheap, fast, testable); 2 = recommendation without table; 1 = preference; 0 = none.

**EX053 — Run and critique Lab PG-11.** *Steps:* run the lab and list four threats to the conclusion. *Rubric:* 3 = output reported; small n, Hawthorne effect, non-equivalent divisions, correlated outcomes, regression to the mean; 2 = two threats; 1 = not run; 0 = none.

**EX054 — Stop rules.** *Steps:* write stop rules for the pilot. *Rubric:* 3 = adverse effects (containment time increase beyond threshold, staff burden complaints), data-quality failure, incident severity override; 2 = one; 1 = vague; 0 = none.

**EX055 — Stakeholder plan.** *Steps:* identify stakeholders and their involvement at each project stage. *Rubric:* 3 = division leads, SOC, service owners, HR (for shift practices), executives; involvement at assessment, design, pilot, evaluation; 2 = list only; 1 = security only; 0 = none.

### Chapter synthesis

Redesign an incident program from evidence: assess gaps with sources, prioritize recurrent high-impact gaps, compare options, pilot one change with pre-set criteria and a concurrent comparison, evaluate honestly with stop rules, and involve stakeholders at every stage.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue studying — chapter 11 of 12

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Final review and organizational transfer plan

### Learning outcomes and connection

You will be able to (1) assemble a transfer package that lets the organization own and sustain the redesigned program; (2) plan training and acceptance; (3) record unresolved issues and residual risks honestly; (4) defend trade-offs before stakeholders; and (5) schedule an evidence-based reassessment. This final chapter completes the Chapter 11 project and the course: specialist work is only valuable if it survives the specialist's departure.

### 12.1 Why transfer fails

Programs designed by specialists often decay: templates stop being used, owners change jobs, metrics are no longer collected, exercises lapse. Transfer fails when ownership, resources and feedback are not built in. The aim is a program the organization runs without you, with signals that tell it when it is drifting.

Calder's transfer package is designed against each of these causes: owners named in the receiving organization, a monthly report to the CISO, and a 90-day review that would show the handoff template falling out of use.

### 12.2 The transfer package

Contents: (1) design rationale — the problem, evidence, options considered and why the chosen design; (2) operating documents — procedures, templates, RACI, thresholds; (3) measurement plan — definitions, data sources, owners, reporting cadence; (4) training materials and records; (5) pilot evaluation report with limitations; (6) open issues and residual risks register; (7) reassessment schedule; (8) contacts and decision rights for future changes. Each item has a named owner in the receiving organization.

Calder's package for the handoff template has all eight: rationale with the 9-of-14 finding and pilot results; template v1.2, read-back guidance and RACI; measures with sources and owners; training records; the pilot report; open issues with owners; reassessment dates; and decision rights for future changes.

### 12.3 Training and acceptance

Train by role, with exercises not just slides; measure acceptance by observed use (for example, percentage of handoffs using the template) rather than attendance. Acceptance by the receiving owner should be explicit and recorded, like service acceptance after recovery.

Calder trained by shift team: a 45-minute role-based session plus a 20-minute handoff drill, with completion and drill observations recorded. Acceptance is measured by the template use rate in the case system, reported monthly, and formally by the group SOC manager as the accountable owner.

### 12.4 Residual issues

List what the redesign did not solve and why: budget, dependencies on other programs, unresolved evidence questions. Assign each to an owner and a review date, or explicitly accept it at the right level (Chapter 9).

Calder's package lists two: Retail's ticketing system cannot enforce required fields until the tooling project, owned by the IT service management lead with a Q3 review; and night-shift staffing remains thin in one region, accepted by the CISO as residual risk until the budget review. Naming both prevents the rollout from being reported as a complete fix.

### 12.5 Defending trade-offs

Stakeholders will challenge choices: "why not the tool?", "why this metric?", "the template slows us down". Prepare a trade-off register: decision, alternatives, reasons, evidence, conditions under which you would decide differently. Concede where evidence is weak.

Calder's register answered the Retail CIO's objection that the template adds paperwork with data: about 4 minutes per handoff, against roughly 15 minutes saved before the incoming lead's first action. It also set a condition for changing course: if template time exceeds 10 minutes, the decision is revisited.

### 12.6 Reassessment

Schedule reassessment based on evidence: a 90-day review of adoption and outcome measures, a 6-month exercise testing the redesigned process, and an annual program review. Define triggers for earlier review: a major incident where the process failed, a significant drop in adoption, organizational change (merger, outsourcing).

Calder's schedule follows this pattern: a 90-day review of template adoption and time to first action, a handoff stress-test exercise at six months, and an annual program review. The earlier-review triggers matter most for Calder's structure: a merger or outsourcing of a division's IT would change who hands off to whom.

### 12.7 Worked example (synthetic): transferring the handoff redesign

*Fictional.* The Chapter 11 pilot succeeded in Logistics. The transfer package for group-wide adoption:

- Rationale: 9 of 14 after-action reports cite handoff delays; pilot reduced median time to first action by 36% versus 5% in comparison division; completeness 87%.
- Operating documents: handoff template v1.2; read-back guidance; RACI (SOC shift lead responsible; group SOC manager accountable).
- Measurement: time from shift change to first action (source: case-system events; owner: SOC analytics); template use rate; completeness at closure; time to containment as guardrail metric. Monthly report to the CISO.
- Training: 45-minute role-based session plus a 20-minute handoff drill per shift team; record of completion and drill observation.
- Open issues: Retail's ticketing system cannot enforce required fields until the tooling project (option B) — owner: IT service management lead, review in Q3; night-shift staffing remains thin in one region — accepted by CISO as residual risk until budget review.
- Reassessment: 90-day adoption and outcome review; handoff stress-test exercise at 6 months; triggers as above.
- Decision rights: changes to the template approved by group SOC manager; changes to thresholds by CISO.

Stakeholder defense (fictional): Retail CIO: "The template adds paperwork." Response: "The pilot measured about 4 minutes per handoff on average and reduced time to first action by about 15 minutes. We will track template time and revisit if it exceeds 10 minutes."

### 12.8 Common errors and limits

- Transfer packages that are document dumps without owners.
- Training measured by attendance.
- Hiding residual issues to declare success.
- No reassessment schedule; programs drift silently.

Calder's package was built to avoid each error: every item has a named owner in the receiving organization; training is measured by template use rate and observed drills, not attendance; the two open issues are listed with owners rather than hidden; and the reassessment dates are fixed. The monthly report to the CISO is the signal that will show drift first.

### Exercises — chapter 12

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX056 — Package checklist.** *Steps:* turn this chapter's transfer package into a checklist with owner and acceptance evidence for each item. *Rubric:* 3 = eight items with owners and evidence; 2 = six; 1 = list without owners; 0 = none.

**EX057 — Adoption metric.** *Steps:* define the template-use rate precisely and its data source, and set a threshold that triggers review. *Rubric:* 3 = numerator/denominator, source, period, threshold with reason; 2 = vague denominator; 1 = no definition; 0 = none.

**EX058 — Trade-off register.** *Steps:* write three entries. *Rubric:* 3 = decision, alternatives, reasons, evidence strength, reversal conditions; 2 = missing reversal conditions; 1 = list; 0 = none.

**EX059 — Reassessment plan.** *Steps:* write the 90-day review agenda with inputs and decisions. *Rubric:* 3 = adoption, outcomes, guardrails, feedback, open issues; decisions (continue/adjust/stop, B funding); 2 = inputs only; 1 = date only; 0 = none.

**EX060 — Final reflection.** *Steps:* in 250 words, reflect on how your approach as a specialist differs from your earlier practitioner approach, using two chapters of this book. *Rubric:* 3 = specific shifts (framing, structure, evidence integration, ethics, leadership) with examples; honest about limits; 2 = generic; 1 = summary; 0 = none.

### Chapter synthesis

Specialist work counts only when the organization can sustain it: transfer a package with owners, train by practice, measure adoption and outcomes, record residual issues honestly, defend trade-offs with evidence and schedule reassessment with triggers.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue studying — chapter 12 of 12

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

Each worked result shows one defensible answer. Specialist exercises often admit several good answers; full credit goes to answers that meet the same standard of framing, evidence, proportionality and honesty about limits. Lab outputs were produced with Python 3.13 and the standard library. Calder Group and all cases, people and numbers are synthetic unless a cited source is named.

### Chapter 1: EX001–EX005

**EX001.** Decision statement: "How to restore operations after encryption of the logistics planning servers, including whether any payment is considered." Owner: CEO as accountable executive, advised by incident commander; deputy named. Options: (a) restore from offline backups, prioritizing warehouse dispatch; (b) staged restore with manual workarounds for lower-priority services; (c) engage a specialist negotiator to gain time and information while (a) proceeds; (d) payment, only after legal and sanctions screening and only if (a)–(c) cannot meet safety or critical-service needs; (e) continue manual operations. Criteria: safety, critical service continuity, legal and sanctions compliance, data-exposure risk (payment does not guarantee deletion), cost, precedent. Horizon: decision on restoration path within 6 hours; payment consideration (if ever) not before backup integrity is known. Information plan: backup integrity check (reducible within hours); attacker's claims of data theft (partly reducible via logs); attacker reliability (irreducible).

**EX002.** (1) "If the incident commander has credible indication that a compromised system can issue commands to warehouse conveyor or robotics controllers, isolate the warehouse control network from corporate IT immediately, accepting up to a full shift of manual operation; notify the operations director within 15 minutes." (2) "If containment of corporate systems would stop dispatch for more than 2 hours, the commander may approve up to 2 hours of dispatch disruption; longer requires the operations director's approval within 30 minutes or the commander's decision stands." The first reflects very low safety appetite, the second low appetite for disruption.

**EX003.** With weights data 0.60, revenue 0.20, regulatory 0.10, evidence 0.10, the output is: base case O4 9.19, O2 8.97, O3 8.60, O1 7.66 (O4 still best); wins O2 3 (all p = 0.1), O3 5, O4 7. Shifting weight from regulatory to data moves two more cells to O3: when the organization weights its own data-protection objective more heavily, going offline becomes the best answer across more of the high-probability region. The conclusion is conditional on weights the board must own; a commander should not tune weights during an incident to justify a preferred option.

**EX004.** (1) Whether gateway logs show bulk retrieval overnight (reducible within an hour): if yes, raise p and consider O3, and start notification analysis. (2) Whether any legitimate partner uses an address outside the allow-list (reducible by partner contact before rotation): if yes, adjust the allow-list rather than choose O3. (3) Whether the same key is configured in other systems (reducible via secrets inventory): if yes, rotation must be coordinated, possibly favouring a short planned outage. Irreducible: whether the actor will return with other credentials.

**EX005.** Gaps: no trigger for misuse of other keys or accounts; no trigger based on partner or customer reports; no trigger tied to regulator or media contact; the 6-hour review lacks an owner. Additions: "any authentication with the old key after rotation → treat as active intrusion, escalate to O3 decision within 15 minutes"; "regulator, law-enforcement or media inquiry → convene legal, privacy and communications within 1 hour"; "review owner: deputy commander at each 6-hour mark, recorded."

### Chapter 2: EX006–EX010

**EX006.** Commander's direct reports: deputy, Operations lead (with workstream leads for identity, endpoint, network beneath), Planning lead (scribe, timeline, documentation), Communications lead, Legal/privacy lead, Business liaison lead (divisional liaisons), Logistics lead (staffing, vendors). That is 6–7 including the deputy, each section absorbing several of the original 11. Justification: manageable span and clear channels while keeping specialist functions visible.

**EX007.** "During a declared group incident, all staff assigned to the incident receive incident tasks from the incident command structure. Line managers retain authority for HR matters and must release assigned staff for the duration agreed by the commander. Divisional executives participate through the business liaison function and may not direct containment of shared services. Disputes about resource release or decisions are escalated to the group CISO, and if unresolved within 30 minutes, to the COO, whose decision is recorded."

**EX008.** Facts: suspected compromise of the group IdP admin account `idp-admin-3` (IdP log, 02:14); new federation trust added at 02:31 (IdP audit). Assessment: likely compromise of IdP administration (confidence: likely). Actions: federation trust disabled 10:20 (Operations, identity workstream; verified); admin credentials rotated (in progress, ETA 15:00). Decisions needed: whether to force reauthentication of all users (commander, by 16:00; options and impacts attached). Next update 16:00.

**EX009.** Template fields: (1) incident objectives; (2) situation summary (facts, assessment, confidence); (3) workstreams with owner, status, next step; (4) pending decisions: question, options, why deferred, deadline, who decides; (5) decisions made this period with reasons; (6) risks and watch items; (7) external commitments (regulator, customers) with times; (8) contacts and on-call; (9) read-back: incoming commander repeats objectives, top pending decision and top risk.

**EX010.** Objectives: handoff transfers pending decisions without loss; command continues when the deputy is unavailable. Scenario: mid-containment of an IdP compromise. Injects: T+20 handoff begins; T+25 outgoing commander "leaves" before finishing; T+30 deputy unreachable; T+40 Logistics CIO requests to isolate shared directory. Criteria: incoming commander can state the top pending decision and its deadline by T+30; a fallback commander is reached by T+40 via roster; the CIO request is routed to the commander rather than executed. Observers: two, one at command, one at liaison. Output: after-action list with owners.

### Chapter 3: EX011–EX015

**EX011.** Artefacts: VPN appliance logs (30-day retention), jump-host disk image. Methods: log review and image timeline analysis (tools and versions not stated — missing). Observations: unusual VPN session at 01:12 on 3 June; RDP from the VPN pool to the jump host. Interpretations: the session was an exploit; it was initial access. Limitations stated: none (missing). Missing: whether the session authenticated with credentials; IdP and cloud logs not examined; exploit signature evidence; appliance version and vulnerability mapping.

**EX012.** (1) Which systems and logs did you examine, and which did you not? (2) Which tools and versions did you use, and how were artefacts acquired and hashed? (3) What alternative explanations for initial access did you consider and how did you exclude them? (4) What is your confidence and what is it based on? (5) What evidence, if found, would change your conclusion?

**EX013.** "Please query the IdP sign-in logs and cloud control-plane logs for 25 May 00:00 UTC to 4 June 23:59 UTC for the accounts `ca-admin-2`, `svc-backup` and `log-ops-7`, and report: all sign-ins with source address and authentication method; all access-key creations and uses with source address; any password resets performed by these accounts. Provide raw exports with query text and a short summary by 16:00 today."

**EX014.** High: multiple independent sources of good quality agree; plausible alternatives tested and excluded. Moderate: credible evidence with some gaps, or one strong source with partial corroboration; alternatives less likely but not excluded. Low: limited, single-source or indirect evidence; significant alternatives remain. Insufficient: evidence does not allow a judgement. Confidence describes the evidence base; likelihood terms ("likely", "unlikely") describe the probability of the conclusion. Report both when helpful.

**EX015.** "Our current assessment, with moderate confidence, is that the attackers first got in on 28 May by tricking a cloud administrator, not by breaking the VPN on 3 June. This means our response focuses on cloud administrator access and password resets made since 28 May. We are verifying with the VPN vendor and searching for earlier activity; either could change this view. Next update tomorrow 09:00."

### Chapter 4: EX016–EX020

**EX016.** (1) Query proxy and DLP logs for uploads to personal cloud-storage domains in the relevant window, filtered by the file's name, size or hash — answers "who uploaded" if traffic passes the proxy. (2) File-share audit logs showing who accessed or downloaded the file before the upload — narrows the candidate set without browsing data. Both target the question; neither collects unrelated browsing. If both fail (for example, upload from a personal device), escalate with counsel rather than broaden collection automatically.

**EX017.** Employer: protect assets, investigate cause, fix controls. Employee: fair, non-scapegoating process; due process if discipline is considered; privacy. Customers: honest notification where required; mitigation. Law: notification duties, preservation, cooperation with authorities. Conflict: pressure to describe the cause vaguely to protect the engineer (or the organization) versus accurate disclosure; resolution: describe the technical cause accurately, keep individual names out of external communication, and handle accountability through a just-culture process.

**EX018.** Request: enhanced export logging for Financial Services. Requester: division head, 14 June. Aim: detect further data export after credential misuse. Options considered: A–D. Chosen: D, conditional on B finding export activity or high-risk access. Legal basis: to be confirmed by counsel before activation. Safeguards: 30 days; export events only (not content); two named investigators; access logged; deletion within 30 days of case closure; notice to staff via policy channel. Decider: CISO with counsel and HR. Review: 1 July or at case closure.

**EX019.** "I share your concern about further misuse, and we are acting now. Full keystroke and screen monitoring of all 120 staff would capture large amounts of unrelated personal information and is unlikely to be lawful or necessary for one compromised credential. Instead, today we are investigating that account's activity and devices; this week we will require phishing-resistant MFA and compliant devices for the division; and if we find signs of export we can enable 30 days of export-event logging with staff notice. I'd like your approval for this plan by 17:00."

**EX020.** Counsel engages the external firm under an agreement that defines scope (root cause and exposure analysis) and reporting lines to counsel, where this is recognized in the jurisdiction; technical remediation instructions flow through the incident structure separately so operations are not delayed. Privilege must not be used to withhold facts the organization is legally required to disclose to regulators or affected people, or to obstruct authorities.

### Chapter 5: EX021–EX025

**EX021.** (1) Egress block — dependants: none expected; owner network; check: rules staged; rollback: remove rules. (2) Web shell removal/isolation — dependants: partners using file transfer; owner server team; check: partner notified; rollback: restore from clean image. (3) OAuth app disable — dependants: none legitimate (confirm); owner identity; rollback: re-enable. (4) Admin resets and session revocation — dependants: scripts using admin accounts (should be none); owner identity; rollback: none (by design). (5) Key-signing rotation — dependants: all directory authentication; owner directory team; check: vendor procedure rehearsed; rollback: per vendor. (6) Partner service principal — dependant: partner integration; owner integration lead with partner; rollback: temporary secret for 1 hour. (7) User resets — dependants: helpdesk capacity, users; owner service desk; rollback: none; mitigation: staffing and communications.

**EX022.** Removing the web shell first, with admin credentials still valid, tells the adversary they have been discovered while they still hold privileged access; they can create new persistence within minutes. Better: identity actions (3–5) and host actions (2) in the same tightly coordinated window, with identity containment completed first or simultaneously, and egress blocks applied just before.

**EX023.** S1: stops all known access at once; low signalling; high user impact; 36 hours preparation; residual risk of unknown footholds. S2: stops observed harm now; high signalling; moderate impact; low preparation; high residual risk of new persistence. Hybrid: stops mail reading now with low signalling; remainder as S1. Recommendation: hybrid, because ongoing harm is high and the pulled-forward action reveals little; consistent with a threshold permitting immediate action against ongoing data access.

**EX024.** (1) Any authentication attempt using reset admin credentials (alert). (2) Any API activity from revoked sessions or tokens. (3) New OAuth application consents in the tenant. (4) New or changed federation trusts or IdP settings. (5) HTTP requests to the web-shell path on any server. (6) Partner integration health and error rates. Also: DNS queries to blocked domains from any host.

**EX025.** "Objective: remove all known adversary access in one window. Scope: confidence moderate; known items 1–7; monitoring for unknowns ready. Steps and owners: as called by the coordinator, in order; report completion times. Rollback triggers: partner integration failure > 30 min; directory authentication failure beyond test users. Communications: user notice at step 7; partner on the call. Go/no-go: each lead confirms readiness — network, server, identity, directory, integration, service desk, communications."

### Chapter 6: EX026–EX030

**EX026.** With seed 7 the printed counts are unchanged: R1 0/0/960; R2 909/40/51. The seed only chooses *which* seven replicated orders are lost; the number lost is fixed, and in both seeds none of the seven is a fraudulent order (a different seed could select one, giving 39 fraudulent present). The recommendation must not depend on such generator detail: what matters is that the replica contains the fraudulent orders and possibly undiscovered changes, while the nightly backup does not.

**EX027.** Warehouse (WMS): reconcile — WMS is the reference; restored orders must match it. Invoicing: freeze until reconciliation, then replay from the reconstructed order set, to avoid invoices for fraudulent orders. Customer notifications: freeze; resume only for reconstructed legitimate orders to avoid confusing or alerting the fraud drop address. Analytics: rebuild after recovery from the final data; mark the incident window.

**EX028.** Data: base hash matches manifest; reconstructed legitimate orders equal WMS legit set; zero orders to fraud drop address or matching fraud patterns without review. Function: create, update, cancel and ship a test order in isolation. Security: database credentials rotated; no adversary accounts; monitoring for the drop address. Performance: response times within 20% of baseline under test load. Sign-off: Logistics service owner. Fallback: if reconciliation differs by more than 0.5% or invoicing fails, revert to manual WMS dispatch for 24 hours.

**EX029.** "We compared two restore candidates against the warehouse system's independent record of 1,000 orders made today. The nightly backup is clean but requires re-entering 960 legitimate orders; the replica is more recent but contains all 40 fraudulent orders, lost 7 records, and may hold undiscovered attacker changes since 08:15. We recommend restoring the nightly backup and rebuilding today's orders from the warehouse record, excluding flagged fraud and reviewing suspicious matches. Limits: the warehouse record may contain errors; fraud flags may be incomplete; the comparison uses one reference."

**EX030.** R2 would be preferable if (a) the investigation verified that adversary access to the primary began after the replica stopped, or (b) the replica's contents can be verified record-by-record against trusted references and any adversary changes removed with high confidence, and (c) re-entering orders from other sources is infeasible within the recovery-time objective.

### Chapter 7: EX031–EX035

**EX031.** GDPR: trigger personal-data breach; clock from awareness; 72 hours to authority where feasible (Art. 33), without undue delay to individuals if high risk (Art. 34); privacy officer/counsel. NIS2: trigger significant incident for in-scope entities; early warning 24 h, notification 72 h, final report 1 month; counsel determines scope (here: not applicable). SEC Form 8-K Item 1.05: trigger material cybersecurity incident; 4 business days after materiality determination; disclosure committee/counsel. Sector rule: e.g., financial supervisor's operational-incident reporting — to verify for the jurisdiction. Contracts: per agreement (here 48 hours to two partners); legal/contract owners. Mark sources and verification dates.

**EX032.** (1) Confirm hold scope with counsel. (2) If volatile evidence matters, capture memory with a documented tool and hash it. (3) Acquire a disk image (or cloud snapshot), compute SHA-256, record in the custody log. (4) Export relevant logs (system, application, security) with hashes. (5) Snapshot configuration (services, users, scheduled tasks, network settings). (6) Store in the evidence repository with access logging; counsel confirms preservation complete; then reimage.

**EX033.** (1) Fact — add source and time. (2) Speculation — remove; if a hypothesis is needed, log as "attribution: not assessed". (3) Determination — add who determined it and basis. (4) Decision/action — add owner and time. (5) Assessment — add confidence and basis.

**EX034.** Scope: storage logs, the export's schema and record counts; not the full customer dataset unless needed for notification lists. Pseudonymization: customer IDs hashed with a case key in working files; mapping held by privacy officer. Access: six named people; read-only for most. Retention: case closure plus period set by counsel. Deletion: documented, verified. Audit: repository access logged and reviewed weekly.

**EX035.** Awareness for GDPR purposes is commonly interpreted (in regulators' guidance) as the point when the controller has a reasonable degree of certainty that a security incident has compromised personal data; a brief period of investigation to establish this is accepted, but unreasonable delay is not. The determination belongs to counsel and the privacy officer. Record both facts — the 8 June observation and the 11 June escalation — and the reasons for the gap; never backdate or omit. The gap is also a process finding for review.

### Chapter 8: EX036–EX040

**EX036.** If DHCP shows the IP belonged to a different host at 22:44, E3 no longer places the sign-in at the HR workstation. Mark E6 as consistent with H1 (remote or other-host use), inconsistent with H2 (local use at the workstation), neutral or consistent with H3, consistent with H4 — e.g., "CINC". Rerun: H2 now has one inconsistency, and E3's marks should be revisited (E3 becomes less reliable). The lesson: diagnostic evidence rests on assumptions (IP mapping) that themselves need provenance.

**EX037.** If the export was performed through a web application, an interactive or network logon by `hr-lead-2` on the workstation host would not necessarily be created — the browser session uses web authentication. So the absence is neutral unless the host would have logged the relevant activity. It becomes diagnostic only if the authentication path requires a host logon (for example, a thick client using Windows integrated authentication).

**EX038.** (1) Check the application's session details for device identifier or browser fingerprint and compare with the workstation's browser profile. (2) Review the workstation's browser history/profile for `hr-lead-2` sessions (with authorization, minimal scope). (3) Check `hr-assist-5`'s concurrent activity at 22:47 in other systems (for example, an active call or ticket work elsewhere) to see if local use was plausible. Interviews only through HR with due process.

**EX039.** E3: IP-to-host mapping (verify DHCP/NAC records); clock alignment between IdP and host (verify with shared events). E4: the export service's job configuration is complete and current (verify with service owner and change history; check other schedulers). E5: the application records session user, not token owner (verify in the deployed version via lab test and vendor confirmation).

**EX040.** At this stage: incident commander, HR lead, counsel and the two investigators — need-to-know. Not the wider incident team, not the line manager without HR's process, not the named employee until HR and counsel decide on an interview. Reasons: fairness and presumption of innocence; legal exposure (defamation, employment law); avoiding contamination of evidence or tipping off.

### Chapter 9: EX041–EX045

**EX041.** "Bottom line: We have removed all attacker access we know of and have seen no further activity in 24 hours; investigation continues. Known: the attacker used a compromised staff account to access the finance file share for 3 days (high confidence). Not yet known: how the account was compromised; whether files were copied (results expected Wednesday). Done: account disabled, passwords reset for the finance team, monitoring increased. Decision needed: approve the external forensic firm's extended scope. Attribution: not assessed and not needed for current decisions. Next update: Wednesday 09:00."

**EX042.** (1) Claim: restored systems are free of known ransomware artefacts. Evidence: hash and indicator scans across 412 restored hosts; EDR coverage 100% of restored hosts. Gaps: unknown variants; 6 legacy hosts without EDR. Confidence: moderate. Owner: endpoint lead. (2) Claim: backups used were not tampered with. Evidence: immutable storage logs, hash match to manifests. Gaps: none known. Confidence: high. Owner: backup lead. (3) Claim: attacker cannot re-enter via known paths. Evidence: VPN patched, credentials rotated, MFA enforced, no old-credential use in 72 h. Gaps: initial access route unconfirmed. Confidence: moderate. Owner: identity lead.

**EX043.** (1) Compromised mailbox: sessions revoked, password reset, MFA re-registered; no sign-ins from attacker infrastructure for 14 days. (2) Malicious inbox rules and forwarding removed across all mailboxes (scan result zero). (3) Payment: recall requested; bank case reference recorded; recovered amount documented. (4) Law-enforcement report filed (reference). (5) Supplier bank-detail changes now require call-back verification (procedure published, tested). (6) Notifications to affected parties completed as determined by counsel. (7) Corrective actions assigned with owners and dates; review held.

**EX044.** Low (contained to one non-critical system, no personal data, < €10k): accepted by security manager; review 6 months. Medium (one business unit or limited personal data, < €250k): CISO; review quarterly. High (multiple units, significant personal data or regulatory exposure, < €2m): executive committee; review monthly until reduced. Critical (strategic, safety or > €2m): board or its risk committee; review at each meeting. Criteria and thresholds set by the organization's risk framework.

**EX045.** "The board is asked to note the residual risks after the identity compromise and to approve two decisions. Residual risks: (1) undiscovered persistence may remain until 30 days of monitoring complete on 15 July — likelihood low to moderate, impact high; (2) the initial access route is not yet confirmed — moderate likelihood of recurrence via the same route until known; (3) regulatory review of the mailbox exposure is possible. Decisions: approve funding for phishing-resistant MFA for all privileged users by September; approve an independent assurance review of identity administration reporting to the audit committee in Q4. Management will report closure against defined conditions at the next meeting."

### Chapter 10: EX046–EX050

**EX046.** Answers depend on the edition. A strong answer records the report's stated methodology section (sample size, countries, interview method, cost model), its definition of the outcomes, which practices are compared, whether any adjustment for confounders is described, and its stated limitations; it adds unstated ones (self-selection, model uncertainty, practice co-occurrence) and declares the publisher's interests. Every figure is quoted with page numbers from the edition consulted.

**EX047.** (1) More ransomware and extortion cases, which reveal themselves quickly, lowering the median. (2) Changes in the provider's client mix (more organizations with mature monitoring). (3) Clients engaging the provider earlier in incidents. (4) Better or worse log retention changing the measurable "earliest evidence". (5) Definition or methodology changes between editions.

**EX048.** Nodes: tested IR plan; breach cost; security budget; organizational maturity; size; industry/regulation; cyber insurance. Arrows: budget → tested plan, budget → lower cost (other controls); maturity → tested plan, maturity → cost; size → both; industry/regulation → both (requirements and cost of notification); insurance → plan (insurer requirements) and → cost accounting. A naive comparison mixes these effects with the plan's.

**EX049.** "Among Calder incidents of severity 2+ in 2025–2026, was time from detection to containment shorter when an automated containment action (session revocation, host isolation) was available for the incident type than when it was not, within the same incident types before and after automation was introduced?" Outcome: hours from first alert to verified containment (executing-system timestamps). Comparison: before/after within types, with types never automated as a control (difference-in-differences). Confounders: staffing changes, detection rule changes, incident mix. Data: case system plus control-plane logs. Limitation: few incidents per type; automation introduced alongside other changes.

**EX050.** "Large industry surveys consistently find that organizations with tested incident-response plans report lower breach costs. These are associations from self-selected samples, and organizations that test plans also tend to invest more in security generally, so the surveys cannot show how much testing itself saves. The mechanisms are plausible: faster decisions, fewer coordination failures. We recommend continuing tabletop testing, which is inexpensive, and measuring our own time-to-containment for tested versus untested playbooks over the next year to estimate the effect for Calder."

### Chapter 11: EX051–EX055

**EX051.** (1) "Requirement: handoffs between shifts preserve pending decisions and context. Evidence: handoff delays noted in 9 of 14 major-incident after-action reports (2025–2026); median 43 minutes to first action after shift change in Logistics. Impact: delayed containment decisions during overnight incidents. Owner: SOC lead." (2) "Requirement: case records contain minimum fields at closure. Evidence: 40% of severity-2 cases lacked root cause, affected service or containment time (case-system query, 412 cases). Impact: metrics and lessons unreliable. Owner: incident program manager."

**EX052.** A: cost low; 2 weeks; disruption low; expected effect moderate on handoffs; evidence: healthcare handover literature and internal reports. B: cost medium; 3–4 months; disruption medium; effect on completeness high, handoffs moderate; evidence: vendor claims. C: highest cost and time; combined effect; hardest to evaluate. Pilot A first: cheap, fast, testable within one quarter, and its results inform B's requirements.

**EX053.** Output as printed. Threats: (1) small numbers of handoffs; one or two unusual shifts move medians; (2) Hawthorne effect — Logistics staff knew they were observed; (3) divisions differ in incident types and staffing; (4) the two outcomes are correlated through the same template; (5) regression to the mean if Logistics was chosen because of a bad period. Also: possible differences in how "first action" was recorded.

**EX054.** Stop or pause if: (1) median time to containment in Logistics increases by more than 20% over two consecutive weeks; (2) on-call staff report the template adds more than 10 minutes per handoff on average; (3) more than 20% of handoff records are missing, making evaluation impossible; (4) the commander declares a severity-1 incident in which the template obstructs response (template becomes optional for that incident, and the event is logged).

**EX055.** Assessment: division IT leads and SOC (data, interviews), service owners (impact). Design: SOC shift leads (template content), HR (shift and rest rules), communications (format). Pilot: Logistics SOC and service owners; Retail as comparison informed but unchanged. Evaluation: independent analyst, program manager, division leads. Throughout: executive sponsor receives monthly summary.

### Chapter 12: EX056–EX060

**EX056.** (1) Rationale — owner group SOC manager; evidence: document accepted at governance meeting. (2) Operating documents — SOC manager; evidence: published in procedure library with version. (3) Measurement plan — SOC analytics lead; evidence: first monthly report delivered. (4) Training — SOC training coordinator; evidence: completion ≥ 95% and drill observations. (5) Pilot report — program manager; evidence: archived with limitations. (6) Open issues register — risk manager; evidence: entries in the risk register with owners. (7) Reassessment schedule — CISO office; evidence: calendar entries and agenda. (8) Decision rights — CISO; evidence: RACI approved.

**EX057.** Template-use rate = handoffs with a completed template (all mandatory sections filled) ÷ all shift handoffs on open severity-1/2 cases, per month. Source: case-system handoff events and template records. Threshold: below 80% for two consecutive months triggers review, because the pilot showed effects with ~95% use and lower use likely erodes benefits.

**EX058.** (1) Decision: process template before tooling. Alternatives: tooling first; both. Reasons: speed, cost, testability. Evidence: pilot (moderate). Reverse if: adoption falls below 80% or tooling becomes available at low cost. (2) Decision: median time to first action as primary metric. Alternatives: time to containment. Reasons: closer to the mechanism; less confounded. Evidence: moderate. Reverse if: data quality of first-action events is poor. (3) Decision: read-back required. Alternatives: optional. Reasons: catches omissions. Evidence: handover literature, pilot observations (moderate). Reverse if: drills show no omissions caught over 6 months and staff burden high.

**EX059.** Inputs: adoption rate by division; time to first action and time to containment trends; completeness; staff survey on burden; open issues status. Agenda: (1) adoption; (2) outcomes vs pilot; (3) guardrails; (4) feedback; (5) open issues; (6) decisions: continue, adjust template, escalate tooling funding (option B), adjust thresholds. Output: decision record with owners.

**EX060.** Answers vary. Strong reflections identify concrete shifts — for example, from choosing an action to framing a decision with options and an owner (Chapter 1), from analysing one source to integrating conflicting specialist reports (Chapters 3 and 8), from compliance thinking to proportionality (Chapter 4), and from reporting technical status to briefing for decisions and accepting residual risk at the right level (Chapter 9) — with an honest note on what remains hard.

<a id="glossary"></a>

## Glossary

- **Analysis of competing hypotheses (ACH)** — A method that tabulates evidence against several hypotheses and focuses on inconsistent and diagnostic evidence.
- **Assurance claim** — A statement that a security property holds, with its evidence, coverage gaps, confidence and owner.
- **Awareness time** — The recorded moment an organization became reasonably certain of a reportable incident; starts many notification clocks.
- **Battle rhythm** — The fixed schedule of incident meetings, updates and reports.
- **Closure conditions** — Measurable conditions that must hold before an incident is closed.
- **Coordinated containment** — A planned set of containment actions executed within a short window so that the adversary loses access everywhere at once.
- **Decision record** — A written record of a decision's frame, options, information, assumptions, owner, residual risk and revisit triggers.
- **Determination** — A judgement within a specialist's competence, such as counsel's view on a notification obligation.
- **Diagnostic evidence** — Evidence consistent with some hypotheses and inconsistent with others.
- **Incident commander** — The single accountable leader of an incident who sets objectives and approves the action plan.
- **Legal hold** — An instruction to preserve specified information when litigation or regulatory action is anticipated.
- **Proportionality** — The requirement that an intrusion be balanced against the benefit of its legitimate aim.
- **Residual risk** — Risk remaining after chosen actions, which must be explicitly accepted at an appropriate level.
- **Revisit trigger** — A condition that requires a decision to be reconsidered.
- **Risk appetite** — The amount and type of risk an organization is willing to pursue or retain.
- **Span of control** — The number of people reporting directly to one supervisor in the incident structure.
- **Transfer package** — The documents, owners, measures and schedules that allow an organization to sustain a redesigned program.
- **Unity of command** — The principle that each person in an incident reports to one supervisor.

<a id="references"></a>

## References

Standards, regulations and web pages change. Versions and dates below are those consulted for this draft (October 2026); re-verify before relying on them. Every Harbourline, Riverside, Calder or other organization, person, case, address and number in this book is synthetic unless a sentence cites a public source.

- National Institute of Standards and Technology. [Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile, SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025; supersedes Rev. 2 (2012).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework). February 2024.
- Bartock, M., et al. [Guide for Cybersecurity Event Recovery, NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final). December 2016.
- Kent, K., et al. [Guide to Integrating Forensic Techniques into Incident Response, NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final). August 2006 (tool-specific details dated).
- FIRST. [CSIRT Services Framework, version 2.1](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1). 2019.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj), in particular Articles 5, 33 and 34.
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- Fischhoff, B. Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty. *Journal of Experimental Psychology: Human Perception and Performance* 1(3):288–299, 1975. https://doi.org/10.1037/0096-1523.1.3.288
- National Institute of Standards and Technology. [Integrating Cybersecurity and Enterprise Risk Management (ERM), NIST IR 8286](https://csrc.nist.gov/pubs/ir/8286/final). October 2020.
- National Institute of Standards and Technology. [Data Integrity: Storage Infrastructure Security Guidelines, NIST SP 800-209](https://csrc.nist.gov/pubs/sp/800/209/final). October 2020.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj), Article 23 on reporting obligations.
- U.S. Securities and Exchange Commission. [SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies](https://www.sec.gov/newsroom/press-releases/2023-139). Press release 2023-139, 26 July 2023 (Form 8-K Item 1.05).
- Article 29 Data Protection Working Party. Opinion 2/2017 on data processing at work (WP 249). June 2017.
- Office of the Director of National Intelligence. [Intelligence Community Directive 203: Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf). 2015.
- Heuer, R. J., Jr. [Psychology of Intelligence Analysis](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/). CIA Center for the Study of Intelligence, 1999.
- Federal Emergency Management Agency. [National Incident Management System (NIMS)](https://www.fema.gov/emergency-managers/nims), including the Incident Command System.
- ISO/IEC 27037:2012, *Guidelines for identification, collection, acquisition and preservation of digital evidence*.
- IBM. [Cost of a Data Breach Report](https://www.ibm.com/reports/data-breach) (annual; research by the Ponemon Institute). Edition consulted must be stated by the reader.
- Mandiant (Google Cloud). [M-Trends](https://cloud.google.com/security/resources/m-trends) (annual).
- Verizon. [Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/dbir/) (annual).
