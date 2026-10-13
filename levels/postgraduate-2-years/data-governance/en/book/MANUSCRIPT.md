# Data Governance: Postgraduate Course

- Language: English (`en`); course 141, Postgraduate course (2 years).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working practitioners on a part-time postgraduate route who must lead data governance in their own organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs measure the share of synthetic carrier tracking events arriving within fifteen minutes and review stale and unapproved accounts on a synthetic shipment data set. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one practitioner from an operating model, ownership and quality management through timeliness, metadata, access, privacy, partner contracts and board reporting to a work-based capstone and its presentation. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lucía Herrera** | Practitioner student, data analyst | Invented |
| **Dr. Samuel Achebe** | Supervisor | Invented |
| **Westbridge Business School** | Fictional school | Invented |
| **Corran Freight** | Fictional logistics company, about 12,000 shipments a day | Invented |

### Core sources

DAMA-DMBOK2 (2017); ISO/IEC 38505-1:2017; ISO 8000-8:2015; Wang and Strong (1996); NIST Privacy Framework 1.0; GDPR. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — The practitioner and Corran Freight

### Learning outcomes

You will (1) describe the postgraduate route and its case; (2) state the governance problems at Corran Freight; (3) plan a work-based learning approach.

### 1.1 The student

Lucía Herrera is a data analyst who has worked for six years at Corran Freight, a fictional logistics company moving goods for retailers across a national road network. She enrols in a two-year part-time postgraduate diploma in data governance at the fictional Westbridge Business School, studying alongside her job. Her supervisor, Dr. Samuel Achebe, explains that the course is designed for practitioners: each module asks students to apply ideas directly to their own organisation, using synthetic data in all assessed labs and exercises.

### 1.2 Corran Freight

Corran Freight operates three hundred lorries, works with three subcontracted carriers and handles about twelve thousand shipments a day. Its data include shipment orders, tracking events from vehicles and carriers, driver records, customer contracts and invoices. Customers increasingly demand accurate arrival estimates and proof of delivery. Lucía's manager has asked her to lead improvements in data governance, because disputes over late deliveries are costing money and nobody can say which tracking data are reliable enough to settle them. Lucía has seen these disputes first hand.

### 1.3 The problems

Lucía lists the problems she sees: tracking events from carriers arrive late or not at all, customer addresses are inconsistent between the order and billing systems, access to driver data is granted informally and the weekly performance report to the board uses definitions that differ from those in customer contracts. Dr. Achebe asks her to describe each problem by its business effect, such as disputed invoices, rather than its technical symptom, so that later proposals connect to outcomes managers care about.

### 1.4 Work-based learning

The course uses work-based learning: Lucía will investigate her organisation, apply frameworks, propose changes and reflect on results. Dr. Achebe warns that insiders can miss what outsiders see and may hesitate to challenge colleagues. He asks her to keep a reflective log and to seek views from people outside her team. She agrees to share her plans with her manager each term, so the organisation understands what she is studying and can benefit from her proposals. Her manager welcomes the arrangement and offers support.

### Worked example

Lucía, an analyst at Corran Freight, starts a practitioner diploma, lists late carrier events, inconsistent addresses, informal driver data access and mismatched report definitions and plans reflective work-based learning.

> **Synthetic case.** Corran Freight, Westbridge and all people are synthetic.

### Errors and limits

Describing problems technically rather than by business effect loses managers' attention.

### Exercises

- **EX001 — Course format.** What kind of course is Lucía taking? *Rubric:* 3 = a part-time practitioner postgraduate diploma;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX002 — Shipment volume.** About how many shipments does Corran handle daily? *Rubric:* 3 = about twelve thousand;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX003 — Report mismatch.** What is wrong with the board report definitions? *Rubric:* 3 = they differ from customer contract definitions;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX004 — Insider risk.** What risk do insiders face in research? *Rubric:* 3 = missing what outsiders see and hesitating to challenge;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX005 — Problem framing.** How should problems be described? *Rubric:* 3 = by business effect;; 2 = partly correct;; 1 = technical;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Governance operating model

### Learning outcomes

You will (1) compare governance operating models; (2) select one for a mid-sized company; (3) define a governance group's mandate.

### 2.1 Models

Dr. Achebe introduces operating models. A centralised model places governance decisions in one team. A federated model shares decisions between a central office setting standards and business units applying them. A decentralised model leaves decisions to units with light coordination. DAMA-DMBOK2 discusses these options and notes that the right one depends on culture, size and how data are shared. Lucía observes that Corran's data cross departments constantly, from sales orders to operations and finance, which argues against leaving decisions entirely to each department.

### 2.2 Choosing for Corran

Lucía compares models against Corran's situation: one head office, three regional depots, shared systems and a small data team. A fully centralised model would overload the data team and ignore depot knowledge. A decentralised model would perpetuate inconsistent definitions. She proposes a federated model: a central governance office of two people sets standards and runs reporting, while owners in operations, sales and finance make decisions for their domains within those standards. Lucía shows the comparison as a short table, with one row per model and one column per factor.

### 2.3 The governance group

She drafts a mandate for a governance group chaired by the chief operating officer. The group approves policies and standards, resolves disputes between domains, sets priorities for quality work and reviews performance quarterly. Its members are the domain owners and the head of IT. ISO/IEC 38505-1 describes the governing body's role as evaluating, directing and monitoring data use, and Lucía maps each mandate item to one of these three activities to show completeness. The chief operating officer reviews the draft mandate and accepts it.

### 2.4 Starting small

Dr. Achebe warns against launching a large programme. Lucía proposes starting with one critical data set, shipment tracking, where disputes create clear costs. Success there would build credibility for expanding to customer and driver data. She drafts a six-month plan and presents it to her manager, who agrees to propose it to the chief operating officer. She notes in her log that a narrow start makes results visible quickly, which matters in a company focused on daily operations. The officer approves it.

### Worked example

Lucía compares centralised, federated and decentralised models, proposes a federated model with a two-person office, drafts a governance group mandate mapped to evaluate, direct and monitor and starts with shipment tracking.

> **Synthetic case.** Corran Freight is synthetic; DAMA-DMBOK2 and ISO/IEC 38505-1:2017 are real.

### Errors and limits

Launching governance across all data at once spreads effort too thin.

### Exercises

- **EX006 — Chosen model.** Which model did Lucía propose? *Rubric:* 3 = federated;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX007 — Office size.** How many people staff the central office? *Rubric:* 3 = two;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX008 — Group chair.** Who chairs the governance group? *Rubric:* 3 = the chief operating officer;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX009 — Mandate mapping.** What three activities did Lucía map the mandate to? *Rubric:* 3 = evaluate, direct, monitor;; 2 = all;; 1 = some;; 0 = none.
- **EX010 — First data set.** Which data set comes first? *Rubric:* 3 = shipment tracking;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Data ownership in a logistics network

### Learning outcomes

You will (1) assign ownership across internal and external data; (2) handle data created by partners; (3) write ownership statements.

### 3.1 Internal domains

Lucía maps Corran's data domains: customers and contracts owned by the sales director, shipments and tracking owned by the operations director, drivers and vehicles owned by the fleet manager and invoices owned by the finance director. Each owner appoints a steward. She finds that tracking events are disputed territory: operations uses them for planning, sales quotes them to customers and finance uses them to support invoices. She proposes operations as owner, since it controls the processes that create the events. The others agree.

### 3.2 Partner data

Carriers send tracking events for shipments they handle. Corran cannot control how carriers capture events, but it decides how those events are used. Lucía distinguishes ownership of the source, which stays with the carrier, from accountability for Corran's use of the data, which belongs to the operations director. She notes that governance for partner data works through agreements and monitoring rather than direct control, which later chapters on third-party data develop further. Lucía records this distinction in each owner's statement for clarity.

### 3.3 Ownership statements

For each domain Lucía writes a one-page ownership statement: the data covered, decisions the owner makes, the steward, key quality expectations and escalation routes. The operations director's statement includes approving tracking quality rules and deciding when carrier data are reliable enough to support customer claims. Owners review and sign their statements. She notes that writing decisions explicitly reveals gaps, such as nobody having authority to approve new data uses. The governance group assigns that authority to the relevant domain owner, with legal advice where needed.

### 3.4 Testing ownership

To test whether ownership works, Lucía brings a real type of question to each owner: may sales share tracking histories with a customer's insurer? The operations director decides with input from legal, and the decision is recorded. She notes that ownership becomes real only when owners actually make decisions, and that early test questions help owners practise their role before more difficult cases arrive under pressure. Lucía runs one such test question with each owner during the first quarter, and records each decision in a shared log for later reference.

### Worked example

Lucía maps four domains, assigns contested tracking events to operations, separates partner source ownership from accountability for use, writes signed ownership statements and tests them with an insurer sharing question.

> **Synthetic case.** Ownership assignments are synthetic.

### Errors and limits

Assigning ownership to whoever uses data most ignores who controls its creation.

### Exercises

- **EX011 — Tracking owner.** Who owns tracking events? *Rubric:* 3 = the operations director;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX012 — Partner distinction.** What stays with carriers? *Rubric:* 3 = ownership of the source data;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX013 — Statement gap.** What gap did statements reveal? *Rubric:* 3 = no authority to approve new data uses;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX014 — Test question.** What test question did Lucía use? *Rubric:* 3 = whether sales may share tracking histories with an insurer;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX015 — Signing.** Who signs ownership statements? *Rubric:* 3 = the owners;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Quality management for shipment data

### Learning outcomes

You will (1) define quality expectations for shipment data; (2) build a quality management cycle; (3) prioritise issues by cost.

### 4.1 Expectations

Lucía works with the operations steward to define quality expectations for shipment data. Each shipment must have a valid customer, origin, destination, promised delivery window and status. Tracking must show collection, depot arrival, departure and delivery events. Proof of delivery must include time and signature or photograph. She bases the dimensions on Wang and Strong and the measurement approach on ISO 8000-8, recording for each expectation how it will be measured and what threshold applies. The steward reviews each threshold with depot supervisors before adoption.

### 4.2 The quality cycle

She sets up a cycle: define rules, measure results daily, analyse failures weekly, improve causes and review rules quarterly. This mirrors improvement cycles used in operations, which helps operations staff accept it. Results feed a dashboard for the steward and a weekly summary for the owner. Lucía notes that the cycle's value lies in the improve step; measuring without fixing causes merely documents decline in more detail. Lucía writes the cycle as a one-page procedure, and the steward follows it from the first week, holding a short meeting each Friday to analyse failures.

### 4.3 Cost of poor quality

To prioritise, Lucía estimates the cost of quality failures. Missing proof of delivery leads to disputed invoices that finance writes off. Wrong destination codes lead to misrouted shipments and re-delivery costs. Late tracking events lead to customer service calls. Using synthetic figures based on typical volumes, she shows that missing proof of delivery costs most. The governance group agrees to tackle it first, since its effect on revenue is direct and measurable. Lucía shows the estimated annual cost of each failure type in a simple chart for the group.

### 4.4 Fixing proof of delivery

Lucía investigates missing proofs. Most come from one carrier whose drivers use paper notes scanned days later, and some from Corran drivers whose handheld devices lose signal in rural areas. The carrier agrees to adopt Corran's mobile app. Corran devices are updated to store proofs offline and send them when signal returns. After two months, missing proofs fall markedly, and disputed invoices decline. Dr. Achebe notes that costing quality failures made prioritisation straightforward. Lucía records the before and after figures in the quality log.

### Worked example

Lucía defines shipment and tracking expectations with measurements, sets a define-measure-analyse-improve-review cycle, ranks missing proof of delivery as costliest and fixes carrier paper notes and offline device storage.

> **Synthetic case.** Figures are synthetic; Wang and Strong (1996) and ISO 8000-8:2015 are real.

### Errors and limits

Measuring quality without fixing causes only documents decline.

### Exercises

- **EX016 — Proof contents.** What must proof of delivery include? *Rubric:* 3 = time and signature or photograph;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX017 — Costliest failure.** Which failure cost most? *Rubric:* 3 = missing proof of delivery;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX018 — Carrier cause.** Why were a carrier's proofs missing? *Rubric:* 3 = paper notes scanned days later;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX019 — Device fix.** How were Corran devices fixed? *Rubric:* 3 = store proofs offline and send later;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX020 — Cycle value.** Where does the quality cycle's value lie? *Rubric:* 3 = the improve step;; 2 = partly correct;; 1 = measure;; 0 = none.

<a id="ch-05"></a>

## Chapter 5 — Timeliness of carrier events

### Learning outcomes

You will (1) measure event timeliness by source; (2) compare partners fairly; (3) use results in partner management.

### 5.1 Why timeliness matters

Customers see tracking updates on Corran's website and expect them to reflect reality. If an event arrives an hour late, the customer may call to ask where a shipment is, or a planner may dispatch a replacement vehicle unnecessarily. Lucía defines timeliness as the delay between when an event happened and when Corran received it, and sets a target that events arrive within fifteen minutes. She measures it separately for each carrier, since each uses different systems. Customers notice delays quickly.

### Lab — Share of synthetic carrier events arriving within fifteen minutes

```python
"""Share of synthetic shipment status events arriving within 15 minutes, by carrier (stdlib only)."""
import random
random.seed(9)
mean = {"Carrier A": 6, "Carrier B": 9, "Carrier C": 21}
for c, m in mean.items():
    d = [random.expovariate(1/m) for _ in range(3000)]
    print(f"{c}: within 15 min {100*sum(x <= 15 for x in d)/len(d):.1f}%")
```

Run with `python3 lab_timeliness.py`. Verified output:

```text
Carrier A: within 15 min 91.9%
Carrier B: within 15 min 81.7%
Carrier C: within 15 min 51.0%
```

### 5.2 Results

The lab simulates three thousand events per carrier. Carrier A delivers 91.9 percent of events within fifteen minutes, Carrier B 81.7 percent and Carrier C only 51.0 percent. Lucía notes that the difference is large enough to matter for customers: shipments handled by Carrier C will show stale status about half the time. She checks that the synthetic event mix is similar across carriers, so the comparison is not distorted by different shipment types or routes. She presents the shares in a table with the number of events behind each figure.

### 5.3 Fair comparison

Before presenting results, Lucía considers fairness. Carrier C operates more rural routes in reality, where signal is weaker, so some delay may be outside its control. She plans to compare carriers on similar routes in a follow-up and to discuss results with each carrier before drawing conclusions. Dr. Achebe notes that partner data governance relies on cooperation, and presenting results as shared problems tends to work better than presenting them as accusations. She records this plan in her log and shares it with Dr. Achebe for comment.

### 5.4 Using the results

Lucía shares results with each carrier. Carrier C explains that its system sends events in batches every half hour to save mobile data costs. Corran offers to cover the cost difference for real-time sending on its shipments, judging that fewer customer calls will repay it. Carrier C agrees. Lucía adds timeliness targets to the carrier agreements due for renewal and schedules monthly reporting of each carrier's results. The next month's results show Carrier C's events arriving much faster, and customer calls about its shipments begin to fall as a result.

### Worked example

Lucía measures event delay by carrier, finds 91.9, 81.7 and 51.0 percent within fifteen minutes, considers route differences, learns Carrier C batches events every half hour and agrees real-time sending with targets.

> **Synthetic case.** Events are synthetic; outputs come from lab_timeliness.py.

### Errors and limits

Comparing partners without considering conditions can be unfair.

### Exercises

- **EX021 — Timeliness definition.** How did Lucía define timeliness? *Rubric:* 3 = delay between event and receipt by Corran;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX022 — Carrier C share.** What share of Carrier C events arrived within fifteen minutes? *Rubric:* 3 = 51.0%;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX023 — Fairness factor.** What might partly explain Carrier C's delays? *Rubric:* 3 = more rural routes with weaker signal;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX024 — Real cause.** What did Carrier C reveal as the cause? *Rubric:* 3 = batching events every half hour;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX025 — Agreement change.** What was added to renewing agreements? *Rubric:* 3 = timeliness targets;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-06"></a>

## Chapter 6 — Metadata, lineage and catalogue

### Learning outcomes

You will (1) document definitions behind key measures; (2) trace lineage of a board measure; (3) build a lightweight catalogue.

### 6.1 Definitions

The board's on-time delivery measure counts shipments delivered by the end of the promised day. Customer contracts define on time as within the promised delivery window, often two hours. The board sees ninety-plus percent on time while customers complain. Lucía documents both definitions in a glossary and proposes that the board measure follow contract windows, with the old measure renamed same-day delivery. The governance group agrees, accepting that the reported figure will fall. Lucía writes both definitions into the glossary with their sources.

### 6.2 Lineage

Lucía traces the on-time measure from the board report back through the reporting database, the shipment system and tracking events from Corran devices and carriers. She finds that shipments without a delivery event are excluded from the measure entirely, rather than counted as late or unknown. This inflates the figure. She records the lineage in the catalogue and recommends that missing delivery events be counted as unknown and reported separately. The operations director approves this change, and the board report adds a separate line for unknown delivery status.

### 6.3 A lightweight catalogue

Corran has no catalogue tool. Lucía creates entries in the company's existing wiki for the twelve most used data sets and measures, each with description, owner, steward, source, refresh time, definition links and known issues. She asks stewards to update entries when changes occur. Within a few weeks, planners begin linking to entries in emails. She notes that a modest catalogue that people use is better than an ambitious one awaiting a budget. Stewards update the entries during their weekly quality meeting.

### 6.4 Communicating the change

When the board measure changes, the reported figure drops sharply. Lucía prepares a short note explaining the new definition, why it matches contracts and how the old figure overstated performance. She includes both figures for three months so the board can see the bridge. Dr. Achebe notes that changing definitions without explanation damages trust, while explaining openly builds confidence that the new figure is more honest. The board accepts the new measure, and the chair asks that future definition changes always be explained in the same way, with both figures shown side by side.

### Worked example

Lucía documents conflicting on-time definitions and aligns the board measure with contract windows, finds excluded shipments without delivery events, builds wiki catalogue entries and explains the falling figure to the board.

> **Synthetic case.** Measures are synthetic.

### Errors and limits

Excluding records with missing events inflates performance figures.

### Exercises

- **EX026 — Contract definition.** How do contracts define on time? *Rubric:* 3 = within the promised delivery window;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX027 — Exclusion finding.** What did lineage reveal? *Rubric:* 3 = shipments without delivery events were excluded;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX028 — Catalogue platform.** Where did Lucía build catalogue entries? *Rubric:* 3 = the company wiki;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX029 — Bridge period.** How long were both figures shown? *Rubric:* 3 = three months;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX030 — Old measure name.** What was the old measure renamed? *Rubric:* 3 = same-day delivery;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-07"></a>

## Chapter 7 — Access governance

### Learning outcomes

You will (1) review access to a governed data set; (2) find stale and unapproved accounts; (3) set up recurring owner reviews.

### 7.1 Why review access

Access to the shipment data set has grown over years as staff joined, changed roles and left. IT grants access on request, often without asking the owner. Lucía explains that every unnecessary account increases the chance of misuse or a compromised password exposing customer and driver details. She proposes a review that the operations director, as owner, will approve, comparing each account's last use and approval record against agreed rules for who should have access. The owner approves the review plan within a week.

### Lab — Stale and unapproved accounts on a synthetic shipment data set

```python
"""Review access to a synthetic shipment data set: stale and unapproved accounts (stdlib only)."""
import random, datetime as dt
random.seed(5)
today = dt.date(2026, 3, 31)
acc = []
for i in range(240):
    last = today - dt.timedelta(days=min(400, int(random.expovariate(1/45))))
    approved = random.random() > 0.07
    acc.append((f"u{i:03d}", last, approved))
stale = [a for a in acc if (today - a[1]).days > 90]
unapp = [a for a in acc if not a[2]]
both = [a for a in stale if not a[2]]
print(f"accounts {len(acc)}; unused over 90 days {len(stale)} ({100*len(stale)/len(acc):.1f}%)")
print(f"no owner approval {len(unapp)}; stale and unapproved {len(both)}")
```

Run with `python3 lab_access.py`. Verified output:

```text
accounts 240; unused over 90 days 30 (12.5%)
no owner approval 17; stale and unapproved 2
```

### 7.2 Results

The lab reviews 240 synthetic accounts with a reference date of 31 March 2026. Thirty accounts, 12.5 percent, have not been used for more than ninety days. Seventeen have no record of owner approval. Two accounts are both stale and unapproved, making them the highest priority for removal, since nobody approved them and nobody seems to use them. Lucía notes that stale and unapproved accounts are different problems with different fixes, so she reports them separately. Lucía shares the lists with the operations director the same day for decisions.

### 7.3 Acting on results

The operations director reviews the list. Stale accounts are disabled after their holders' managers confirm no need; three are kept for staff on long leave, with a note and an expiry date. Unapproved accounts are reviewed one by one: most are legitimate and receive retrospective approval, while a few belong to contractors whose work ended, and these are removed. The two accounts in both groups are removed immediately. Each decision is recorded with its reason. The review takes three weeks to complete in full.

### 7.4 Making it recurring

Lucía proposes quarterly access reviews for the shipment data set and twice-yearly reviews for less sensitive sets. IT changes the request process so that new access requires owner approval, recorded automatically. Leavers' accounts are disabled through the human resources leaver process. Dr. Achebe notes that one-off clean-ups decay quickly, and that sustainable access governance depends on changing the processes that created the problem as well as fixing its current state. The first quarterly review after these changes finds far fewer stale accounts, which suggests that the process changes are working.

### Worked example

Lucía reviews 240 accounts, finding 30 unused over ninety days (12.5 percent), 17 unapproved and 2 in both groups, has the owner act on each with recorded reasons and makes reviews and approvals recurring.

> **Synthetic case.** Accounts are synthetic; outputs come from lab_access.py.

### Errors and limits

Clean-ups without process changes decay quickly.

### Exercises

- **EX031 — Stale share.** What share of accounts were unused over ninety days? *Rubric:* 3 = 12.5% (30 of 240);; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX032 — Highest priority.** Which accounts were highest priority? *Rubric:* 3 = the two both stale and unapproved;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX033 — Long-leave handling.** How were long-leave accounts handled? *Rubric:* 3 = kept with a note and expiry date;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX034 — Request change.** How did IT change the request process? *Rubric:* 3 = new access requires recorded owner approval;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX035 — Leaver control.** How are leavers' accounts handled? *Rubric:* 3 = disabled through the HR leaver process;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-08"></a>

## Chapter 8 — Privacy and driver data

### Learning outcomes

You will (1) assess privacy risks in vehicle telematics; (2) apply purpose limitation and minimisation; (3) involve affected people.

### 8.1 Telematics

Corran's lorries record location, speed, braking and engine data every few seconds. These data support route planning, fuel efficiency and safety. Because each lorry is assigned to a driver, the data are personal data about drivers under the GDPR. Lucía finds that managers have begun using telematics to monitor drivers' break times, a purpose not mentioned in the driver privacy notice. She raises this with the data protection officer as a potential purpose limitation problem. The officer agrees and opens an assessment.

### 8.2 Assessment

Lucía helps the data protection officer carry out a data protection impact assessment for telematics. It describes the processing, assesses necessity and proportionality, identifies risks to drivers, such as unfair discipline based on misread data, and proposes safeguards. The NIST Privacy Framework's govern and control functions help structure the safeguards: policies on permitted uses, access limited by role and retention of detailed location data for ninety days, with aggregates kept longer. The assessment is signed by the officer and the fleet manager as owner.

### 8.3 Involving drivers

The assessment recommends consulting drivers. Lucía helps organise sessions with driver representatives. Drivers accept safety and route uses but object to minute-by-minute break monitoring, noting that legal break rules are already recorded by tachographs. Corran agrees that telematics will not be used for break monitoring and that any disciplinary use requires review by a second manager with the driver's representative present. The privacy notice is updated to describe permitted uses clearly. Driver representatives review the new notice before it is issued to all drivers.

### 8.4 Minimisation

Lucía examines whether all collected data are needed. Engine data at second-by-second detail serve maintenance but not planning; she proposes that planners receive data aggregated per trip. Location data outside working hours, when drivers take lorries home in some depots, are switched off. Dr. Achebe notes that these changes reduced risk without losing operational benefit, and that involving drivers produced better safeguards than managers alone would have designed. The fleet manager approves both changes, and the assessment is updated to record them with the date of each decision.

### Worked example

Lucía finds telematics used for unannounced break monitoring, supports an impact assessment with role access and ninety-day retention, consults drivers who reject break monitoring and minimises engine and off-duty location data.

> **Synthetic case.** Practices are synthetic; the GDPR and NIST Privacy Framework 1.0 are real. This is not legal advice.

### Errors and limits

New uses of employee data without notice breach purpose limitation.

### Exercises

- **EX036 — Unannounced use.** What unannounced use did Lucía find? *Rubric:* 3 = monitoring driver break times;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX037 — Location retention.** How long is detailed location data kept? *Rubric:* 3 = ninety days;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX038 — Driver objection.** What did drivers object to? *Rubric:* 3 = minute-by-minute break monitoring;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX039 — Discipline safeguard.** What safeguard applies to disciplinary use? *Rubric:* 3 = second manager review with representative present;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX040 — Off-duty data.** What happens to location data outside working hours? *Rubric:* 3 = switched off;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-09"></a>

## Chapter 9 — Third-party data and contracts

### Learning outcomes

You will (1) govern data exchanged with partners; (2) write data clauses into contracts; (3) monitor partner compliance.

### 9.1 Data flows with partners

Corran exchanges data with carriers, customers, a fuel card provider, an insurer and a software vendor hosting the tracking platform. Lucía lists each flow: data sent and received, purpose, legal basis and current contract terms. She finds that the tracking platform vendor processes customer and driver data on Corran's behalf but the contract lacks the processor terms required by Article 28 of the GDPR. The legal team prioritises updating that contract. Lucía also finds two flows with no written agreement at all, which legal adds to its list.

### 9.2 Data clauses

Lucía drafts standard data clauses with legal: purpose, data quality obligations such as timeliness targets, security, onward sharing, retention, breach notification within a set time, audit rights and return or deletion at the end. For carriers, quality clauses matter most; for the platform vendor, security and processor terms matter most. She notes that standard clauses speed up negotiations and ensure that data obligations are not forgotten when commercial terms dominate discussions. Legal approves the clauses, and they are used in the next three contract renewals.

### 9.3 Monitoring partners

Clauses need monitoring. Lucía designs a partner scorecard with timeliness, completeness and incident reporting for each carrier, reviewed monthly with the carrier. For the platform vendor, she requests its independent security assurance report annually and checks that agreed controls appear. When a carrier misses timeliness targets for three consecutive months, the agreement's escalation clause triggers a joint improvement plan rather than immediate penalties. The plan sets out actions on both sides, such as Corran fixing its own interface errors and the carrier upgrading its devices, with a date for reviewing progress together.

### 9.4 Ending relationships

When Corran replaces its fuel card provider, Lucía checks that the old provider returns or deletes Corran's data as the contract requires. The provider confirms deletion in writing, and Lucía records the confirmation. She also checks that Corran's own systems stop sending data to the old provider. Dr. Achebe notes that exit is the most neglected stage of partner governance, and that confirming deletion protects both the company and the people whose data were shared. She adds an exit checklist to the procedure.

### Worked example

Lucía lists partner flows, finds missing processor terms for the platform vendor, drafts standard data clauses, monitors carriers with scorecards and vendor assurance reports and confirms deletion when a provider is replaced.

> **Synthetic case.** Partners are synthetic; GDPR Article 28 is real.

### Errors and limits

Contracts negotiated on commercial terms alone often omit data obligations.

### Exercises

- **EX041 — Missing terms.** What was missing from the platform vendor contract? *Rubric:* 3 = GDPR Article 28 processor terms;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX042 — Carrier clause focus.** Which clauses matter most for carriers? *Rubric:* 3 = quality obligations;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX043 — Vendor assurance.** What does Lucía request from the vendor annually? *Rubric:* 3 = its independent security assurance report;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX044 — Three-month miss.** What happens after three months of missed targets? *Rubric:* 3 = a joint improvement plan;; 2 = partly correct;; 1 = penalties;; 0 = none.
- **EX045 — Exit check.** What did Lucía confirm when changing fuel card provider? *Rubric:* 3 = written confirmation of deletion;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-10"></a>

## Chapter 10 — Metrics, reporting and the board

### Learning outcomes

You will (1) design governance metrics for executives; (2) link metrics to business outcomes; (3) report honestly on progress.

### 10.1 Choosing metrics

Lucía chooses a small set of governance metrics for the board: proof of delivery completeness, carrier event timeliness, on-time delivery under contract definitions, disputed invoice value, access review completion and open high-priority data issues. Each links to an outcome the board cares about, such as revenue lost to disputes. She avoids metrics that measure activity alone, such as number of meetings held, which say little about whether governance improves the business. The governance group reviews the list and agrees each target with the relevant owner before the first report.

### 10.2 Building the report

The quarterly report fits on two pages: a table of metrics with targets and trends, three highlights, three concerns and decisions needed. Lucía writes in plain language and explains any change in definitions. She includes a chart of disputed invoice value before and after the proof of delivery fix. She notes that boards have limited time, so reports should make it easy to see what is working, what is not and what the board must decide. The board chair welcomes the format.

### 10.3 Attribution

The board asks whether governance caused the fall in disputed invoices. Lucía explains that the proof of delivery fixes are the most likely cause, since disputes fell mainly for shipments handled by the carrier that switched apps, but that other factors, such as a new customer contract template, may also contribute. She presents the evidence and its limits. Dr. Achebe notes that honest attribution protects credibility when future results are less favourable. She includes a short note on these limits directly beneath the chart.

### 10.4 Decisions

The report asks the board for two decisions: funding to extend governance to customer master data and approval of a policy that all new data sharing requires an owner's approval. The board approves both. Lucía records the decisions and their owners. She reflects that linking governance to visible financial outcomes made the board receptive, and that asking for specific decisions turned the report from information into action. Both decisions appear in the next report with their progress, so the board can see that its approvals led to action.

### Worked example

Lucía selects outcome-linked metrics, writes a two-page board report with highlights, concerns and decisions, attributes falling disputes cautiously and secures funding and a sharing policy.

> **Synthetic case.** Metrics are synthetic.

### Errors and limits

Claiming full credit for improvements with several causes damages credibility.

### Exercises

- **EX046 — Activity metric.** What kind of metric did Lucía avoid? *Rubric:* 3 = activity-only metrics such as meetings held;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX047 — Report length.** How long is the quarterly report? *Rubric:* 3 = two pages;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX048 — Other cause.** What other factor might reduce disputes? *Rubric:* 3 = a new customer contract template;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX049 — Board approvals.** What did the board approve? *Rubric:* 3 = customer master data funding and a sharing approval policy;; 2 = both;; 1 = one;; 0 = none.
- **EX050 — Report purpose.** What turned the report into action? *Rubric:* 3 = asking for specific decisions;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-11"></a>

## Chapter 11 — Capstone project

### Learning outcomes

You will (1) design a capstone governance intervention; (2) implement it with stakeholders; (3) evaluate results against a baseline.

### 11.1 Choosing the intervention

For her capstone, Lucía chooses to govern customer address data, which the board funded. Addresses differ between the order and billing systems, causing misdelivered invoices and failed deliveries. She defines the problem with a baseline: share of customers whose addresses differ between systems, failed deliveries attributed to address errors and invoices returned undelivered. She agrees success criteria with the sales director as owner and Dr. Achebe as supervisor before starting. She records the baseline figures in her project log before any change is made to either system.

### 11.2 Design

Lucía designs the intervention: the order system becomes the authoritative source for delivery addresses, the billing system for invoice addresses, with clear rules on which changes flow where. A steward in sales reviews mismatches weekly. Address validation is added at order entry using a postcode lookup. Customers can update addresses through a portal that writes to the authoritative system. She records each design choice in a decision record with alternatives considered. The sales director approves the design after a review with IT and billing staff.

### 11.3 Implementation

Implementation takes four months. IT builds the address flows and validation; sales trains staff on the portal. Lucía runs weekly checks and finds an unexpected problem: some customers have several valid delivery sites, which the original design treated as mismatches. She revises rules to allow multiple delivery sites per customer with one invoice address. She notes that implementation reveals assumptions that design discussions missed, which is why monitoring during rollout matters. The revised rules are tested on synthetic cases before going live.

### 11.4 Evaluation

After implementation, Lucía compares results with the baseline using synthetic figures that mirror her observations. Address mismatches, failed deliveries due to address errors and returned invoices all fall. She checks whether other changes coincided, finding a seasonal drop in volume that could partly explain fewer failures, and adjusts her claims. She documents limits and recommends continued monitoring. Dr. Achebe approves the evaluation as balanced and well evidenced. She presents the before and after figures in a short table, with a note beside each figure explaining how it was measured.

### Worked example

Lucía governs customer addresses with a baseline and agreed criteria, designs authoritative sources, steward review, validation and a portal, adjusts for multiple delivery sites and evaluates cautiously against the baseline.

> **Synthetic case.** The project and figures are synthetic.

### Errors and limits

Evaluating without a baseline makes improvement impossible to show.

### Exercises

- **EX051 — Address problem.** What problems did address differences cause? *Rubric:* 3 = misdelivered invoices and failed deliveries;; 2 = both;; 1 = one;; 0 = none.
- **EX052 — Delivery authority.** Which system is authoritative for delivery addresses? *Rubric:* 3 = the order system;; 2 = partly correct;; 1 = billing;; 0 = none.
- **EX053 — Surprise.** What unexpected issue appeared? *Rubric:* 3 = customers with several valid delivery sites;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX054 — Coinciding change.** What coinciding change did Lucía find? *Rubric:* 3 = a seasonal drop in volume;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX055 — Validation method.** How are addresses validated at entry? *Rubric:* 3 = a postcode lookup;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-12"></a>

## Chapter 12 — Capstone presentation and next steps

### Learning outcomes

You will (1) present a capstone to academic and industry assessors; (2) reflect on professional development; (3) plan governance beyond the course.

### 12.1 The presentation

Lucía presents her capstone to Dr. Achebe, a second academic and Corran's chief operating officer. She covers the problem, baseline, design, implementation, evaluation and limits in twenty minutes. The chief operating officer asks how the address rules will be maintained after Lucía's course ends. She explains that the sales steward owns the weekly review, the rules are documented in the catalogue and the governance group reviews address metrics quarterly. The chief operating officer is satisfied with this answer and confirms the arrangements.

### 12.2 Assessor questions

The second academic asks how Lucía separated the effect of her intervention from seasonal changes. She explains her comparison with the same period in the previous year and acknowledges that this is imperfect. He also asks what she would do differently. She says she would have checked customer site structures before designing rules. The assessors praise her candour and the clear link between governance actions and business outcomes throughout the project. Lucía notes their feedback in her reflective log for later use.

### 12.3 Professional reflection

In her final reflective essay, Lucía notes how her role changed: from analyst producing reports to a practitioner leading governance across departments. She learned to frame problems by business effect, involve affected people such as drivers, negotiate with partners and present honestly to the board. She also notes difficulties, such as challenging senior colleagues, and how evidence and agreed ownership made those conversations easier over time. She also notes that her reflective log helped her see patterns in her own progress that she would otherwise have missed.

### 12.4 Next steps

Lucía proposes next steps for Corran: extend governance to invoice data, automate partner scorecards and run an annual maturity assessment. She is promoted to data governance lead. Dr. Achebe reminds her that governance is never finished, as businesses and regulations change. The next course in this area turns to privacy and data protection, where governed data meet the rights of the people they describe. Lucía thanks Dr. Achebe and her colleagues at Corran, and plans to mentor the next analyst who joins the course from the company.

### Worked example

Lucía presents her capstone, explains how address governance will be sustained, answers questions on seasonality and design hindsight, reflects on her development and is promoted to governance lead.

> **Synthetic case.** The presentation is synthetic.

### Errors and limits

Capstones that end without ownership for sustaining changes fade.

### Exercises

- **EX056 — Sustaining rules.** Who owns the weekly address review afterwards? *Rubric:* 3 = the sales steward;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX057 — Seasonality method.** How did Lucía address seasonality? *Rubric:* 3 = comparison with the same period the previous year;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX058 — Hindsight.** What would Lucía do differently? *Rubric:* 3 = check customer site structures before designing rules;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX059 — New role.** What role does Lucía take next? *Rubric:* 3 = data governance lead;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX060 — Proposed extension.** Which data are governed next? *Rubric:* 3 = invoice data;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Lucía Herrera, Dr. Samuel Achebe, Westbridge Business School, Corran Freight and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A two-year part-time postgraduate diploma for practitioners.

**EX002.** About twelve thousand.

**EX003.** They differ from definitions in customer contracts.

**EX004.** Missing what outsiders would see and hesitating to challenge colleagues.

**EX005.** By their business effect, such as disputed invoices.

**EX006.** A federated model.

**EX007.** Two.

**EX008.** The chief operating officer.

**EX009.** Evaluating, directing and monitoring.

**EX010.** Shipment tracking.

**EX011.** The operations director.

**EX012.** Ownership of how the source data are captured.

**EX013.** Nobody had authority to approve new data uses.

**EX014.** Whether sales may share tracking histories with a customer's insurer.

**EX015.** The owners themselves.

**EX016.** Time plus a signature or photograph.

**EX017.** Missing proof of delivery.

**EX018.** Its drivers used paper notes scanned days later.

**EX019.** They now store proofs offline and send when signal returns.

**EX020.** In the improve step.

**EX021.** The delay between when an event happened and when Corran received it.

**EX022.** 51.0 percent.

**EX023.** More rural routes with weaker signal.

**EX024.** Its system batched events every half hour.

**EX025.** Timeliness targets with monthly reporting.

**EX026.** Within the promised delivery window.

**EX027.** Shipments missing delivery events were excluded from the measure.

**EX028.** In the existing company wiki.

**EX029.** Three months.

**EX030.** Same-day delivery.

**EX031.** 12.5 percent, 30 of 240.

**EX032.** The two accounts that were both stale and unapproved.

**EX033.** Kept with a note and an expiry date.

**EX034.** New access now needs owner approval, recorded automatically.

**EX035.** Disabled through the human resources leaver process.

**EX036.** Managers monitoring drivers' break times.

**EX037.** Ninety days, with aggregates kept longer.

**EX038.** Minute-by-minute break monitoring.

**EX039.** Review by a second manager with the driver's representative present.

**EX040.** Collection is switched off.

**EX041.** Processor terms required by GDPR Article 28.

**EX042.** Data quality obligations such as timeliness.

**EX043.** Its independent security assurance report.

**EX044.** A joint improvement plan.

**EX045.** Written confirmation that the old provider deleted Corran's data.

**EX046.** Activity-only metrics such as meetings held.

**EX047.** Two pages.

**EX048.** A new customer contract template.

**EX049.** Funding for customer master data and an owner-approval sharing policy.

**EX050.** Asking the board for specific decisions.

**EX051.** Misdelivered invoices and failed deliveries.

**EX052.** The order system.

**EX053.** Customers with several valid delivery sites.

**EX054.** A seasonal drop in shipment volume.

**EX055.** With a postcode lookup.

**EX056.** The sales steward.

**EX057.** By comparing with the same period in the previous year.

**EX058.** Check customer site structures before designing rules.

**EX059.** Data governance lead.

**EX060.** Invoice data.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and standards were checked against their publisher pages. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- ISO/IEC. (2017). *ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data*. <https://www.iso.org/standard/56639.html>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0*. https://doi.org/10.6028/NIST.CSWP.10
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
