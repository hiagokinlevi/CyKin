# Threat Intelligence and OSINT: An Engineering Book

- Language: English (`en`); engineering course, five years.
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; nine offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students who will design, build, verify and operate threat-intelligence platforms and OSINT workflows as dependable systems.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical boundary: no collection on real private individuals, no terms-of-service evasion, no deanonymisation and no interaction with adversary infrastructure. Every organisation, person, indicator and number is **synthetic** unless a sentence cites a public source; addresses use RFC 5737 ranges and domains use `.example`.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–19 apply mathematics, computing and security foundations to intelligence problems. Chapters 20–41 engineer a CTI platform from requirements through models, controls, implementation, measurement, reliability, integration, scale, operations, validation and optimisation, with studios and verification labs. Chapters 42–50 cover research, practice, capstone, review, failure trials, the evidence dossier, thesis and defence. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, three exercises scored 0–3, a synthesis and a **Continue studying** block.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Brightwater Energy Networks (BEN)** — regional electricity distributor with a 14-person SOC | Organisation that needs CTI | Invented |
| **Lantern** — BEN's in-house CTI platform (TAXII 2.1 ingestion, STIX 2.1 store, enrichment, dissemination) | System engineered in the book | Invented |
| **Kofi Mensah** | Engineering student on placement in BEN's security engineering team | Invented |

### Core sources

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) and [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); Hutchins et al. [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf); NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |
| [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) read rates of change in intelligence workloads; (2) interpret a derivative as "how fast is this growing now"; (3) approximate an area under a curve to total a workload; (4) avoid extrapolating a local slope too far.

### 1.1 Rates in a SOC

Indicators arrive in Lantern at a rate that changes during the day: low overnight, rising when partner communities in other time zones publish. If N(t) is the cumulative count of indicators received by hour t, its derivative N′(t) is the arrival rate. Engineers size parsers and enrichment workers for the peak of N′, not for the daily average, because queues form when instantaneous arrival exceeds service.

A feed that delivers most of its daily volume in two morning hours needs workers sized for those hours, even though the average looks gentle. Kofi plots the rate rather than the running total when he checks this, because a cumulative curve hides bursts inside its steady climb.

### 1.2 Slopes from data

Real data are discrete. A difference quotient — (N(t+1) − N(t)) / 1 hour — estimates the rate. Smoothing over several hours reduces noise but hides short bursts; the choice depends on whether you are planning capacity (use peaks) or reporting trends (smooth).

Kofi keeps two views of the same counts for that reason. The raw hourly differences go to the capacity review, where a single busy hour matters. A six-hour moving average goes into the monthly report, where readers want to know whether partner volume is growing. Each chart says which one it is. Missing hours are left as gaps rather than filled, because an invented value would distort both the peak and the trend.

### 1.3 Areas as totals

If r(t) is the rate of analyst-hours needed to triage alerts, the integral of r over a shift is the total effort. A trapezoid sum over hourly samples is accurate enough for staffing.

With samples every hour, the trapezoid rule averages each pair of neighbouring rates and multiplies by one hour. Summing those slices across an eight-hour shift gives the analyst-hours the shift must cover. If the result is eleven hours of work and three analysts are on shift, the plan has slack; if it is thirty, the team needs help or a narrower triage scope. The estimate is only as good as the samples, so a missing hour is marked, not guessed.

### 1.4 Limits of local slopes

A burst during a major campaign may show a steep slope. Projecting that slope a month ahead predicts absurd volumes. Derivatives describe now; models of cause are needed for forecasts.

Kofi saw this when a partner published a large backlog of old indicators in one afternoon. The hourly rate jumped tenfold, then fell back the next day. Had he sized Lantern from that afternoon's slope, BEN would have bought hardware for a load that never returned. A forecast needs an explanation of why volume changes, such as a new partner joining, and the slope only tells him that something changed.

### Practice note — Units and dashboards

Lantern's dashboard once plotted the cumulative total where operators expected a rate, and the night shift read a calm flat line as a sudden spike when the axis rescaled. Kofi now labels every chart either 'per hour' or 'cumulative since 00:00 UTC', and the capacity review uses only rate charts.

### Worked example

Kofi samples Lantern's cumulative indicator count at 08:00 (12,400), 09:00 (12,700) and 10:00 (13,300). The rate rose from 300 to 600 per hour. He sizes the parser for at least 600 per hour plus headroom, and notes that the jump coincided with a partner's morning bulletin — a scheduled, not structural, increase.

> **Synthetic case.** Lantern's counts are invented for this chapter.

### Errors and limits

Confusing the cumulative count with the rate leads to absurd capacity plans. Calculus here measures workloads; it does not predict adversaries.

### Exercises

- **EX001 — Hourly rate.** Using Kofi's samples, compute the arrival rate between 09:00 and 10:00. *Rubric:* 3 = 600 per hour with method; 2 = number only; 1 = uses cumulative; 0 = none.
- **EX002 — Peak or mean.** Explain why parser capacity is sized for peak rate rather than daily mean. *Rubric:* 3 = queues form when arrival exceeds service; mean hides bursts; 2 = partial; 1 = mean is fine; 0 = none.
- **EX003 — Trapezoid total.** Analyst-hours needed are 2, 4 and 6 per hour at three consecutive hourly samples. Estimate total effort over those two hours. *Rubric:* 3 = 8 analyst-hours via trapezoids; 2 = method right; 1 = sums to 12; 0 = none.

### Synthesis

Rates size systems, areas total effort, and local slopes must not be stretched into forecasts.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) represent intelligence relationships as a graph; (2) compute reachability with breadth-first search; (3) relate graph pivots to the Diamond Model; (4) explain why disconnected components matter for attribution claims.

### 2.1 Sets and relations

An indicator set is a set; "event uses infrastructure" is a relation. Union, intersection and difference let engineers compare feeds; relations let them link events. STIX 2.1 expresses relations explicitly through relationship objects such as "indicates" or "uses".

Kofi compares two partner feeds by intersecting their domain sets. The overlap tells him how much the second feed adds; the difference shows what only one partner has seen. A union is what Lantern must store. Relations carry more than membership: a pair such as an indicator and the malware it indicates says how two things are connected, and the type of that link matters when an analyst later decides how far to trust it.

### 2.2 Graphs and pivots

Treat events, infrastructure, capabilities and victims as nodes and their links as edges. The Diamond Model of Caltagirone, Pendergast and Betz describes analytic pivoting along exactly these edges: from an event to its infrastructure, from infrastructure to other events. Breadth-first search counts hops, which is a natural limit on how far an analyst should trust a chain of inferences.

The hop count in the lab therefore doubles as a trust measure. One hop from an event is something the evidence shows directly; three hops is a chain of inferences, each of which could be wrong.

### Lab 2 — pivot graph

```python
"""Lab 2 (ch 02): breadth-first pivot over a synthetic Diamond-style relationship graph."""
from collections import deque
edges = [("event-1", "c2.example"), ("c2.example", "event-4"), ("event-4", "victim-B"),
         ("event-1", "victim-A"), ("event-7", "loader-x"), ("loader-x", "event-9")]
g = {}
for a, b in edges:
    g.setdefault(a, set()).add(b); g.setdefault(b, set()).add(a)
def reach(start, max_hops):
    seen, q = {start: 0}, deque([start])
    while q:
        n = q.popleft()
        if seen[n] == max_hops:
            continue
        for m in sorted(g[n]):
            if m not in seen:
                seen[m] = seen[n] + 1; q.append(m)
    return seen
for node, hops in sorted(reach("event-1", 3).items(), key=lambda x: (x[1], x[0])):
    print(hops, node)
print("event-7 reachable:", "event-7" in reach("event-1", 10))
```

Run with `python3 lab_graph.py`. Verified output:

```text
0 event-1
1 c2.example
1 victim-A
2 event-4
3 victim-B
event-7 reachable: False
```

### 2.3 Components

event-7 and its loader are not reachable from event-1. Two components mean no evidence in this graph links the activities. Claims that both belong to one campaign need new evidence, not wishful edges.

The lab output shows this split plainly: the search from event-1 never reaches event-7 however many hops it allows. An analyst may still suspect a connection, perhaps because the two loaders behave alike, but that suspicion belongs in the notes as a hypothesis to test. Drawing an edge without evidence would make the graph agree with the analyst and teach nobody anything. If new evidence arrives, such as a shared certificate, the edge is added with its source, and the components merge on the record.

### 2.4 Hop limits

Each hop adds uncertainty. Lantern caps automatic pivots at three hops and labels anything further as an analyst hypothesis.

The limit follows from simple arithmetic. If each link is right nine times in ten, a three-hop chain is right only about seven times in ten, and a five-hop chain little better than half the time. Automatic pivots beyond three hops would fill reports with links that are as likely wrong as right. An analyst can still follow a longer chain by hand, but the result is labelled as a hypothesis, and the reasoning for each extra hop is written down so a reviewer can check it.

### Practice note — Edge weights

Not every edge deserves equal trust. Lantern weights an edge by specificity: a unique self-signed certificate shared by two servers is a strong link; a popular public resolver is almost none. Weighted reachability lets an analyst ask which nodes are reachable through strong edges only, which usually shrinks a dramatic campaign graph to something defensible.

### Worked example

Kofi runs the pivot from event-1. Within three hops it reaches c2.example, victim-A, event-4 and victim-B. He reports that victim-B is linked to event-1 only through shared infrastructure, a three-hop chain, and recommends notifying victim-B's sector contact with that caveat.

> **Synthetic case.** All nodes are invented.

### Errors and limits

Shared infrastructure such as a large hosting provider creates false links; weight edges by specificity. Graph reachability is not attribution.

### Exercises

- **EX004 — Hop count.** At how many hops does the lab reach victim-B? *Rubric:* 3 = 3; 2 = correct with no explanation of path; 1 = wrong; 0 = none.
- **EX005 — Separate component.** What does "event-7 reachable: False" imply for a campaign claim? *Rubric:* 3 = no linking evidence in graph; claim needs new evidence; 2 = partial; 1 = same campaign; 0 = none.
- **EX006 — Shared hosting trap.** Why might an edge through a large shared hosting IP create a false link? *Rubric:* 3 = many unrelated tenants share it; low specificity; 2 = vague; 1 = no issue; 0 = none.

### Synthesis

Sets compare, graphs link, hops cost confidence, and disconnected components are honest silence.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate signal propagation and bandwidth to collection latency; (2) estimate storage growth for retained intelligence; (3) understand power and cooling as constraints on always-on platforms; (4) connect physical timing to timestamp accuracy.

### 3.1 Latency has a floor

Light in fibre travels about 200,000 km per second, so a round trip between continents costs tens of milliseconds before any processing. A TAXII 2.1 poll across an ocean will never be instant; engineers set polling intervals and timeouts with that floor in mind.

Kofi measured a poll from Lantern to a partner server on another continent and saw about a hundred milliseconds before the first byte arrived. That cost is fixed by distance. A timeout shorter than the floor fails every request, while one far longer hides real outages. He sets the timeout at several seconds and records each poll's duration, so a slow partner shows up in the logs instead of as missing data.

### 3.2 Bandwidth and bulk feeds

A bulk feed of 2 GB each night over a 100 Mbit/s link takes roughly 160 seconds at full rate, ignoring overheads. If the link is shared with operational traffic for substations, scheduling transfers away from peak use is a physical, not merely administrative, decision.

The worked example adds overhead and schedules the transfer at 02:00 for this reason. A large download during the day could compete with telemetry from substations, which BEN cannot afford to delay. Rate limiting the transfer is another option, trading a longer download for a smaller share of the link.

### 3.3 Storage growth

Storing 50,000 STIX objects per day at about 2 KB each is roughly 100 MB per day, around 36 GB per year before indexes. Indexes and enrichment can triple that. Retention policies are therefore engineering inputs.

Kofi turns these figures into a retention question for the CTI lead: how long must expired indicators stay searchable? Keeping two years of raw objects plus indexes could approach two hundred gigabytes, while summarising expired items after ninety days keeps the store far smaller. The answer depends on whether investigations need old indicators, and that is a requirement to agree with analysts rather than a choice for the storage team.

### 3.4 Clocks

Server clocks drift. If Lantern's collector and BEN's firewall disagree by two minutes, time-to-block measurements are wrong by two minutes. Network time synchronisation and recorded clock sources matter for evidence.

Kofi checks that every Lantern server and the firewall take time from the same synchronised source, and that each log records which source it used. When the firewall's clock was found running fast during a test, he corrected past measurements by the known offset and noted the correction beside the results. A metric built on unsynchronised clocks can show negative times to block, which is the quickest sign that something is wrong.

### 3.5 Power and heat

An on-premises Lantern cluster draws power and needs cooling. In an energy company that sounds trivial, but SOC rooms are not data centres; capacity planning includes the room.

Kofi estimated the draw of three servers and found it close to what the room's cooling could remove on a hot afternoon. Adding a fourth server would have needed new cooling, a cost the original plan had missed. Placing the cluster in BEN's data centre instead removed the problem, at the price of a longer network path to the SOC.

### Practice note — Latency budgets

End-to-end latency is a sum: network round trips, queue waits, parsing, enrichment and the firewall push. Kofi writes a budget table with a target for each term so that a 30-minute service level can be checked component by component. When one term grows, the table shows which stage stole the time.

### Worked example

Kofi estimates nightly transfer time for a 2 GB partner archive: 2 GB × 8 = 16 Gbit, / 0.1 Gbit/s = 160 s. With 30% protocol overhead he plans about 210 s and schedules it at 02:00, away from substation telemetry peaks.

> **Synthetic case.** Feed sizes and link speeds are invented.

### Errors and limits

Back-of-envelope figures guide design; measure before committing hardware. Bits and bytes are a frequent factor-of-eight error.

### Exercises

- **EX007 — Transfer time.** Estimate transfer time for 500 MB over 50 Mbit/s, ignoring overhead. *Rubric:* 3 = 80 s with method; 2 = right method slip; 1 = byte/bit error; 0 = none.
- **EX008 — Yearly storage.** Estimate one year's raw storage at 20,000 objects/day × 2 KB. *Rubric:* 3 ≈ 14.6 GB (40 MB/day); 2 = order right; 1 = off by 1000; 0 = none.
- **EX009 — Clock skew.** How does a 2-minute clock skew affect a time-to-block metric? *Rubric:* 3 = biases each measurement by up to 2 minutes; need NTP and recorded source; 2 = "inaccurate"; 1 = no effect; 0 = none.

### Synthesis

Physics sets floors on latency, budgets for bandwidth and storage, and the accuracy of every timestamp an analyst trusts.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small, pure functions that transform intelligence records; (2) use standard-library types for strings, sets and dictionaries; (3) test functions against known inputs; (4) refuse to write collection code that violates terms or privacy.

### 4.1 Records as dictionaries

A parsed indicator is naturally a dictionary: `{"type": "domain", "value": "c2.example", "source": "partner-A", "tlp": "TLP:GREEN"}`. Functions that take one record and return a new one are easy to test and compose.

The dictionary keeps each field named, so code reads clearly and missing fields can be checked. Kofi's functions never change the record they receive; they return a new one, which means an earlier version is still available if a later step goes wrong. A record that lacks a source or a TLP label is rejected at this stage rather than stored without them.

### 4.2 Pure functions first

A pure function has no side effects: given the same input it returns the same output and writes nothing. Normalising a domain to lower case is pure. Writing to the database is not. Keep the pure parts separate so most of the code can be tested without infrastructure.

Kofi's parser follows that split. The functions that clean and validate a record are pure and have dozens of quick tests. A thin outer layer reads from the feed and writes to the store, and that layer is tested less often against a test database. When a bug appears, the pure tests usually locate it in seconds.

### 4.3 Defanged text

Reports often "defang" indicators — `hxxp`, `[.]` — so that nobody clicks them. A parser must refang them only inside the platform, never in outputs that humans will paste into browsers. Lantern stores the normal form and renders the defanged form in reports.

The two forms must never be confused. If a report shows a live link and an analyst clicks it, the click may reach attacker infrastructure, which the book's ethical boundary forbids. Kofi's rendering function defangs every domain and address, and a test fails if any report output contains a working scheme.

### 4.4 Tests

For each function, write three known-answer cases: a normal value, an edge case, and malformed input. Malformed input should produce an explicit error or a rejected flag, never a guessed value.

For a function that normalises a domain, the normal case might be a mixed-case name that should come back in lower case. The edge case could be a name with a trailing dot, and the malformed case a string with a space inside it. Writing these three tests before the function itself often reveals what the function should do when the input is strange, which is where real feeds cause trouble.

### 4.5 What not to program

Students sometimes ask how to scrape a social platform for threat actors' personal details. Lantern's code collects only from sources whose terms permit it and only the fields needed. Automated collection that evades rate limits, logins or terms is out of scope.

The rule protects people as well as BEN. Personal details of a suspected actor may belong to someone uninvolved, and gathering them can breach privacy law and platform terms. Lantern's sources are listed with the terms that allow their use, and adding a new source needs the CTI lead's approval before any code is written. Kofi's code reviews check that list.

### Worked example

Kofi writes `refang(s)` replacing `hxxp` and `[.]`. His tests: `"hxxp://a[.]example"` → `"http://a.example"`; `"a.example"` unchanged; `""` → rejected. A colleague's version returned an empty string for empty input; Kofi's rejects it, so empty values never become stored indicators.

> **Synthetic case.** Kofi's function and tests are invented.

### Errors and limits

Copy-pasted parsing snippets can contain network calls; read them. Refanged strings in reports invite accidental clicks.

### Exercises

- **EX010 — Purity check.** Is a function that normalises case and also logs to a file pure? Why? *Rubric:* 3 = no; file write is a side effect; 2 = no; 1 = yes; 0 = none.
- **EX011 — Refang rule.** Where may refanged indicators appear, and where must they stay defanged? *Rubric:* 3 = refanged inside platform processing/storage; defanged in human-facing reports; 2 = one half; 1 = everywhere refanged; 0 = none.
- **EX012 — Empty input.** What should `refang("")` return under Kofi's design, and why? *Rubric:* 3 = rejected/error so empty values never stored; 2 = error only; 1 = empty string; 0 = none.

### Synthesis

Small pure functions, explicit rejection, defanged outputs and collection code that respects terms.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write requirements, design notes and incident summaries in plain English; (2) separate facts, assumptions and judgments as ICD 203 recommends; (3) apply TLP labels to engineering documents; (4) choose figures that reduce rather than add confusion.

### 5.1 Writing for the reader's decision

Every document answers a reader's question. A requirement answers "what must the system do?" A design note answers "why this way?" An intelligence summary answers "what should I do now?" Start with the answer, then support it.

An analyst reading a summary at the start of a shift wants to know whether to block, watch or ignore. If that answer is buried in the fourth paragraph, the reader may act on the wrong one. Kofi puts the recommended action in the first sentence and the evidence below it, so a reader who stops early still acts correctly and one who reads on can check the reasoning.

### 5.2 Fact, assumption, judgment

"Partner A's feed delivered 12,000 indicators yesterday" is a fact. "Partner A's feed is mostly current" is an assumption unless measured. "We should prioritise Partner A for automated blocking" is a judgment. ICD 203's tradecraft standards ask writers to distinguish information from assumptions and judgments; engineers benefit from the same discipline.

Kofi marks each kind in his drafts. A fact carries its source and date, an assumption says what would confirm it, and a judgment states who made it. Readers can then challenge the right thing.

### 5.3 TLP on documents

A design note that contains partner names under an AMBER sharing agreement inherits that restriction. Put the TLP 2.0 label in the header and footer. Untagged documents tend to spread.

Kofi's template puts the label in both places so that a printed page still shows it. A document that mixes material should carry the most restrictive label among its parts, or be split so the wider part can travel further. Partner names are often the restricted element, and replacing them with a neutral identifier may let the rest be shared.

### 5.4 Figures

A single chart of time-to-block by source is clearer than a dashboard of twenty gauges. Label axes with units; state the period and the data source in the caption.

Kofi tested a dashboard of many gauges on the night shift and found nobody could say which source was slowest. A single bar chart sorted by median time to block answered that in seconds. Each chart he publishes now has a caption giving the period, the source of the data and the unit, so a reader can judge whether a change is real or a result of a different measurement.

### 5.5 Review

Ask a reviewer to state your main point back in one sentence. If they cannot, rewrite.

Kofi tries this with a colleague before sending any design note. When the colleague described his note on enrichment as being about logging, he found the conclusion was in the last paragraph. Moving it to the top fixed the problem. A second check is to ask what action the reader should take; if the reviewer cannot say, the note lacks a clear request. Both checks take a few minutes and spare readers a confusing document.

### Practice note — Short forms

Executives read the first paragraph and the figure. Analysts read the indicator table. Engineers read the decision record. Kofi writes each document with a three-line summary at the top — decision, reason, deadline — so every reader can stop early without missing the action they own.

### Worked example

Kofi drafts a note recommending a second enrichment worker. The first draft opens with three paragraphs of history. He rewrites: "Add one enrichment worker before 1 March; queue delay exceeded 10 minutes on 9 of 30 days (fact). We assume volume grows 20% this year (assumption)." The manager approves in one reading.

> **Synthetic case.** The note and figures are invented.

### Errors and limits

Over-labelling everything RED stops necessary sharing; under-labelling leaks. Plain language is not the same as vague language.

### Exercises

- **EX013 — Label sentences.** Classify "the queue exceeded 10 minutes on 9 of 30 days" and "volume will grow 20%". *Rubric:* 3 = fact; assumption (or forecast judgment); 2 = one right; 1 = both facts; 0 = none.
- **EX014 — Inherited label.** A design note quotes partner names covered by an AMBER agreement. What TLP label should the note carry? *Rubric:* 3 = at least TLP:AMBER (inherits); 2 = some label; 1 = CLEAR; 0 = none.
- **EX015 — Caption contents.** List three things a chart caption should state. *Rubric:* 3 = units/metric, period, data source; 2 = two; 1 = title only; 0 = none.

### Synthesis

Answer first, separate fact from assumption and judgment, label sensitivity, and make each figure carry its units and source.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) model indicator confidence decay with an exponential function; (2) solve for the time a value crosses a threshold; (3) choose half-lives per indicator type; (4) recognise when decay models mislead.

### 6.1 Why decay

Indicators lose value: adversaries rotate IP addresses quickly and domains more slowly, while behaviours described by ATT&CK techniques persist for months or years. Bianco's Pyramid of Pain captures this ordering. Lantern encodes it as a confidence score that decays over time unless re-observed.

The score is not a measure of how dangerous an indicator is. It estimates how likely the indicator still points at hostile activity. An address that was malicious last week may now belong to an unrelated customer of the same hosting firm, and blocking it would cut off legitimate traffic. Decay builds that risk into Lantern without anyone having to remember to remove old entries by hand.

### 6.2 The model

c(t) = c₀ · e^(−t·ln2/h), where h is the half-life in days. After one half-life confidence halves; after two it quarters. Solving c(t) = floor gives t = h · ln(c₀/floor) / ln 2.

In words, the score falls by the same fraction every day, so the drop is large while confidence is high and small near the floor. The second formula answers the practical question: how many days until this indicator needs review? Kofi uses it to schedule re-validation rather than letting entries linger. Changing the half-life changes the slope, but the shape stays the same.

### Lab 1 — decay

```python
"""Lab 1 (ch 06): exponential confidence decay for a synthetic indicator, c(t) = c0 * exp(-t * ln2 / h)."""
import math
c0, half_life_days, floor = 90.0, 14.0, 30.0
for t in (0, 7, 14, 21, 28):
    print(f"day {t:2d}: confidence {c0 * math.exp(-t * math.log(2) / half_life_days):5.1f}")
t_floor = half_life_days * math.log(c0 / floor) / math.log(2)
print(f"falls below {floor:.0f} after {t_floor:.1f} days -> retire or re-validate")
```

Run with `python3 lab_decay.py`. Verified output:

```text
day  0: confidence  90.0
day  7: confidence  63.6
day 14: confidence  45.0
day 21: confidence  31.8
day 28: confidence  22.5
falls below 30 after 22.2 days -> retire or re-validate
```

### 6.3 Choosing half-lives

Half-lives are engineering parameters fitted from re-observation data: how often does an IP indicator still appear malicious after a week? Lantern starts with 14 days for IPs, 45 for domains and none for file hashes (which do not change but may become irrelevant), then adjusts from evidence.

Kofi records each starting value with the reasoning behind it. The fourteen days for addresses reflects how quickly hosting customers change; the longer period for domains reflects registration costs. Hashes do not decay because a file never changes, yet they are reviewed when the malware family stops appearing.

### 6.4 Re-observation

A sighting resets c to a new value. The model therefore describes staleness, not truth.

When a partner reports the same address again, or BEN's own sensors see it in hostile traffic, Lantern raises the score to the value set for that kind of sighting and the clock starts again. An indicator that keeps being seen stays active for as long as it is seen. One that is never seen again fades out on schedule, whatever its initial confidence. The record keeps every sighting with its source, so an analyst can see why the score is what it is.

### 6.5 When the model misleads

A dormant infrastructure reused after months will have decayed to near zero. Retired indicators should be archived, not deleted, so analysts can still match historical events.

Kofi saw this with a domain that had been quiet for six months and then reappeared in a phishing run. Its score had fallen far below the blocking floor, so Lantern did not block it automatically. Because the archive still held it, the analyst who saw the new sighting found the earlier campaign at once and raised the score by hand. Deleting retired entries would have lost that history.

### Practice note — Re-fitting half-lives

Each quarter Kofi samples retired indicators and checks how many reappeared in later sightings. If IP indicators are still being sighted after 30 days at a meaningful rate, the 14-day half-life is too short. The refit is recorded with its sample size so later reviewers can judge whether the change was justified.

### Worked example

With c₀ = 90, h = 14 days and a floor of 30, the lab shows confidence 45.0 at day 14 and crossing the floor after 22.2 days. Lantern schedules re-validation on day 22 and removes the indicator from automated blocking unless re-observed.

> **Synthetic case.** Parameters are illustrative, not measured.

### Errors and limits

A neat curve can hide poor data; fit half-lives from evidence. Decay suits indicators, not judgments about adversary intent.

### Exercises

- **EX016 — Day-14 value.** What confidence does the lab print at day 14, and why that number? *Rubric:* 3 = 45.0; one half-life halves 90; 2 = number only; 1 = wrong; 0 = none.
- **EX017 — Floor time.** Using the formula, after how many days does confidence cross 30? *Rubric:* 3 = 22.2 days with formula; 2 = number only; 1 = 28; 0 = none.
- **EX018 — Archive not delete.** Why archive decayed indicators rather than deleting them? *Rubric:* 3 = historical matching/reuse of infrastructure; retrospective analysis; 2 = vague; 1 = delete is fine; 0 = none.

### Synthesis

Exponential decay encodes staleness, half-lives come from evidence, and retired indicators stay searchable.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) compute precision from sensitivity, false-positive rate and prevalence; (2) explain the base-rate effect on alerting; (3) express judgments with calibrated probability words; (4) choose summaries suited to skewed data.

### 7.1 The base-rate effect

A rule that matches 95% of malicious connections and wrongly matches 2% of benign ones sounds excellent. But if only 1 in 100 connections is malicious, most alerts are false. If only 1 in 1,000 is malicious, almost all are.

The lab makes the point with numbers. At the lower prevalence almost two thousand benign connections are flagged for under a hundred malicious ones. Analysts quickly learn to ignore such alerts, and then they miss the true ones. The rule itself has not changed between the two rows; only the traffic it runs against has. That is why Kofi always asks where a rule will run before judging how good it is.

### Lab 3 — base rate

```python
"""Lab 3 (ch 07): base-rate effect on alert precision for a synthetic indicator match rule."""
for prevalence in (0.01, 0.001):
    sens, fpr, n = 0.95, 0.02, 100000
    bad = n * prevalence; good = n - bad
    tp, fp = bad * sens, good * fpr
    print(f"prevalence {prevalence:.3f}: TP={tp:.0f} FP={fp:.0f} precision={tp/(tp+fp):.3f}")
```

Run with `python3 lab_bayes.py`. Verified output:

```text
prevalence 0.010: TP=950 FP=1980 precision=0.324
prevalence 0.001: TP=95 FP=1998 precision=0.045
```

### 7.2 Reading the lab

At prevalence 0.010, 950 true and 1,980 false positives give precision 0.324. At 0.001, precision falls to 0.045: about 21 false alerts for each true one. Engineering response: lower the false-positive rate, raise prevalence by applying the rule only where malicious traffic is likelier, or route matches to enrichment before analysts.

The third option is what the worked example recommends. A match then adds weight to other evidence instead of paging an analyst on its own. Kofi also checks the arithmetic by hand once, because a lab that disagrees with a simple calculation usually has a bug.

### 7.3 Calibrated words

Analysts translate probabilities into words. Kent's essay on words of estimative probability showed readers interpret "probable" inconsistently; teams should publish a mapping. ICD 203 also asks that uncertainty be expressed properly.

Lantern's reporting guide gives each word a range: for example, likely means a probability between about 0.55 and 0.80. Analysts choose a word from the table instead of from instinct, and a reader can look up what it means. Kofi checks drafts for words outside the table, such as possibly, which readers interpret anywhere from rare to even chance. The table is reviewed each year with the people who read the reports, so the words keep the meaning readers expect.

### 7.4 Skewed data

Time-to-block and enrichment latency are right-skewed. Medians and percentiles (p90, p99) describe them better than means.

Most indicators are blocked within minutes, but a few wait for hours because a partner held them or an approval was slow. Those few pull the mean far above what a typical indicator experiences. The median shows the usual case and the ninetieth percentile shows how bad the slow cases get. Kofi reports both, with the count of items, so readers can see the long tail without it distorting the typical figure. A single mean would describe no actual indicator.

### Practice note — Recall and coverage

Precision answers how many alerts are true; recall answers how many malicious events were caught. A feed that is very precise but covers a small part of the threat landscape may still leave BEN exposed. Lantern therefore reports both, and estimates recall from incident reviews where the full set of malicious events was later established. Kofi also keeps a small table of the assumed prevalence for each traffic segment, because the same rule behaves very differently on the guest Wi-Fi than on the substation management network.

### Worked example

Kofi evaluates a proposed rule matching any connection to a feed's IPs. He estimates prevalence near 0.001 in BEN's traffic, computes precision 0.045, and recommends using the rule as an enrichment input rather than a direct page to analysts.

> **Synthetic case.** Rates are illustrative.

### Errors and limits

Prevalence is hard to know; state assumptions. Precision without recall hides missed threats.

### Exercises

- **EX019 — Precision quote.** What precision does the lab give at prevalence 0.001? *Rubric:* 3 = 0.045; 2 = approx; 1 = 0.95; 0 = none.
- **EX020 — Engineering fix.** Name two ways to improve precision for this rule. *Rubric:* 3 = two of lower FPR / scope to higher-prevalence segments / enrichment gate; 2 = one; 1 = raise sensitivity only; 0 = none.
- **EX021 — Percentile choice.** Why report p90 enrichment latency instead of mean? *Rubric:* 3 = skewed tail matters for user experience/SLA; mean hides it; 2 = vague; 1 = mean better; 0 = none.

### Synthesis

Base rates dominate alert quality, words need numbers behind them, and skewed metrics need percentiles.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) relate CPU, memory and storage hierarchy to intelligence processing; (2) estimate whether a workload is CPU-, memory- or I/O-bound; (3) explain caching for enrichment lookups; (4) recognise hardware trust anchors in collection systems.

### 8.1 The hierarchy

Registers and caches are fast and small; main memory larger and slower; solid-state storage slower again; network storage slowest. Lantern's hot set — indicators matched against live traffic — must fit in memory, or every match waits on disk.

Kofi checked this with a simple test. Matching a batch against an in-memory set took a few milliseconds; the same lookups against an on-disk index took tens of milliseconds, mostly waiting for reads. The cold archive can live on slower storage because analysts query it occasionally and can wait a second for an answer.

### 8.2 Bound by what

Parsing JSON-formatted STIX objects is CPU-heavy. Joining indicators with sightings is memory-heavy. Loading archives is I/O-heavy. Profiling identifies the binding resource; buying the wrong hardware is common and expensive.

Kofi learned this when a request for faster disks arrived to fix slow parsing. Profiling showed the parser was using a full processor core while the disks sat idle. Faster disks would have changed nothing. A second worker process, which cost nothing but configuration, roughly doubled throughput. Each profile is saved with the hardware it ran on, so later comparisons are fair.

### 8.3 Caching enrichment

Enrichment — adding WHOIS-style registration data, passive DNS or internal asset context — often repeats lookups. A cache keyed by indicator with a time-to-live avoids repeated queries and respects third-party rate limits and terms. Cached data must expire, both for accuracy and because some providers' terms limit retention.

Kofi sets the time to live per provider, using the shortest of what accuracy needs and what the provider's terms allow. The cache records when each entry was fetched, so an analyst can tell whether data is fresh.

### 8.4 Hardware roots of trust

Collection servers that sign exported data rely on keys. A hardware security module or TPM keeps signing keys out of ordinary memory, improving the integrity of what Lantern shares.

Without such a module the key sits in a file that anyone with administrator access to the server could copy, and a copied key lets an attacker sign false indicators that partners would trust. With it, signing still works but the key cannot be exported. Kofi's design lists which servers hold signing keys and who may use them, and the module's logs show every signing operation for later review.

### 8.5 Memory sizing

One million indicators averaging 200 bytes in an in-memory set need about 200 MB plus overhead; Python objects can triple that. Measure.

Kofi built a set of a million test strings and measured it rather than trusting the arithmetic. The result was several times the raw data size, because each string object carries its own overhead. He then sized the matcher's memory with room for a year of growth and a margin, and recorded the measurement method so it can be repeated when volumes change. A compact representation, such as storing hashes of values, could reduce the footprint if memory became tight.

### Practice note — Profiling discipline

Kofi profiles before and after every performance change and keeps the reports. Changes that do not move the measured bottleneck are rolled back even if they 'should' help. This habit stops the team from accumulating clever optimisations that add complexity but no speed.

### Worked example

Profiling shows Lantern's matcher spends 70% of its time waiting on disk. Kofi moves the active indicator set (about 400,000 entries) into memory, cutting match latency from 40 ms to 3 ms per batch, and adds a 24-hour TTL cache for enrichment lookups to stay within a provider's daily query quota.

> **Synthetic case.** Profiles and timings are invented.

### Errors and limits

Caches can serve stale data; TTLs are a correctness choice, not only a performance one. Respect provider terms on retention.

### Exercises

- **EX022 — Binding resource.** A job's CPU sits at 15% while disk wait is high. What binds it? *Rubric:* 3 = I/O; move hot data to memory or faster storage; 2 = I/O only; 1 = CPU; 0 = none.
- **EX023 — TTL reasons.** Give two reasons an enrichment cache needs a TTL. *Rubric:* 3 = freshness + provider retention terms/rate limits; 2 = one; 1 = none needed; 0 = none.
- **EX024 — Memory estimate.** Estimate raw memory for 400,000 indicators × 200 bytes. *Rubric:* 3 = 80 MB (plus overhead noted); 2 = number only; 1 = off by 1000; 0 = none.

### Synthesis

Know which resource binds, keep the hot set in memory, cache with expiry, and anchor signing keys in hardware.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure a parser as a pipeline of stages; (2) handle errors without losing records silently; (3) parse JSON safely with the standard library; (4) write property-style tests for normalisation.

### 9.1 Pipelines

Lantern's ingestion is a chain: fetch → decode → validate → normalise → deduplicate → store. Each stage takes records and yields records plus rejects. Generators in Python let large feeds stream without loading everything into memory.

Each stage can be tested on its own with a short list of records, and a failure in one stage does not hide what the others did. Kofi's logs show how many records entered and left every stage, so a sudden drop points to the stage that caused it. When a partner sends a very large archive, streaming means memory use stays flat rather than growing with the file.

### 9.2 Errors as data

A malformed object is not an exception to swallow; it is a reject record with a reason, the source and the original bytes' hash. Reject counts per source become a data-quality metric that partners can act on.

Kofi's reject records keep the hash rather than the content, so a partner's restricted data is not copied into logs that wider staff can read. If the same reason appears for many records from one source, the partner probably changed something on their side. The report sent to them gives counts and examples, which is usually enough for them to find and fix the problem.

### 9.3 Safe JSON

`json.loads` parses data without executing code, unlike evaluating text. Limit input sizes to avoid memory exhaustion and validate types after parsing; JSON numbers, strings and nulls arrive in unexpected places.

Kofi sets a maximum size for each object before parsing, so a huge input is rejected instead of filling memory. After parsing he checks that each field has the expected type: a timestamp field holding a number, or a list where a string was expected, is a reject with a clear reason. Older code that evaluated text as a program to save effort was removed during his first month.

### 9.4 Properties

Instead of only example tests, state properties: normalising twice equals normalising once (idempotence); output is always lower case; no output contains whitespace at either end. Generate many random inputs and check the properties hold.

Kofi's random inputs include mixed case, leading and trailing spaces, empty strings and characters from other alphabets. A property test found that his domain normaliser left a trailing dot in place, which made two forms of the same name count as different indicators. Fixing it removed a few hundred duplicates from the store.

### 9.5 Versioning parsers

When a partner changes its export format, a new parser version is deployed alongside the old one until the switch is verified. Each stored object records the parser version that produced it.

Running both versions on the same input for a few days shows whether the new one produces the same records, more rejects or different values. Only when the differences are understood does the old parser stop. Recording the version on each object means that if a bug is found later, the affected records can be identified and reprocessed rather than guessed.

### Practice note — Backpressure

When a downstream stage slows, upstream stages must not keep pushing until memory runs out. Bounded queues between stages give backpressure: producers wait when a queue is full. Lantern's collector pauses polling when the validation queue is at capacity and records the pause, so operators see it rather than discovering missing data later.

### Worked example

A partner sends 5,000 objects with 37 malformed timestamps. Kofi's pipeline stores 4,963, writes 37 rejects with reason "created not RFC 3339", and emails the partner's data-quality contact a count and two example hashes — not the raw objects, which are TLP:AMBER.

> **Synthetic case.** Counts and the partner are invented.

### Errors and limits

Silently dropping bad records hides partner problems; silently fixing them invents data. Do not evaluate untrusted text as code.

### Exercises

- **EX025 — Reject record.** List four fields a reject record should carry. *Rubric:* 3 = four of reason, source, hash, timestamp, parser version; 2 = two; 1 = one; 0 = none.
- **EX026 — Idempotence.** State the idempotence property for a normaliser and why it matters. *Rubric:* 3 = norm(norm(x)) == norm(x); repeated processing stable; 2 = statement only; 1 = wrong; 0 = none.
- **EX027 — Partner report.** Why send hashes and counts rather than the malformed objects themselves? *Rubric:* 3 = TLP/minimisation; partner can locate via hash; 2 = partial; 1 = send everything; 0 = none.

### Synthesis

Stream through stages, treat errors as data, parse safely, test properties and record parser versions.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering-ethics duties to intelligence systems; (2) identify privacy and legal limits on OSINT; (3) design for safe failure in a critical-infrastructure context; (4) know when to escalate a concern.

### 10.1 Duties

Engineers owe duties to the public, the employer and the profession. In CTI that means protecting people whose data passes through the platform, honouring sharing agreements and refusing work that would facilitate harm.

For Kofi these duties are concrete. Personal data that arrives in a feed is limited to what analysis needs and deleted on schedule. Partner material marked AMBER stays within the agreed audience. If BEN asked for a capability that could hurt people, such as monitoring staff outside work, the duty to the public outweighs the instruction.

### 10.2 OSINT limits

Public does not mean unrestricted. Platform terms of service may forbid automated collection; data-protection law such as the EU GDPR applies to identifiable people even in public posts; aggregating harmless facts can create a profile that endangers someone. Lantern's OSINT module therefore collects organisational data — domains, certificates, published advisories — not personal social profiles.

Kofi checks each new OSINT source against its terms before writing any code, and records the outcome in the source register. A source that forbids automated access is read by hand, if at all, and nothing from it is stored in bulk.

### 10.3 Safe failure in an energy company

If Lantern pushes a bad block list to firewalls protecting substation telemetry, it could cut operational visibility. Safety design: operational-technology segments receive blocks only after human approval, and a malformed list causes the push to stop, not to clear the firewall.

Kofi's push service checks the list before sending it: it must parse, it must not be empty and it must not have shrunk by more than a set amount since the last push. A failed check stops the push and alerts the on-call engineer while the firewall keeps its current rules. For substation segments an operator approves each change, because a wrong block there can blind the control room.

### 10.4 Escalation

If a manager asks Kofi to scrape employee social accounts "to find insiders", he declines, documents the request and escalates to the privacy officer. Ethical refusal is part of engineering competence.

Writing down the request, who made it and what he did protects both Kofi and BEN. The privacy officer can then decide whether any legitimate concern lies behind it and how to address it lawfully, for example through BEN's existing insider-risk process. Kofi does not need to win the argument himself. He needs to make sure the right person hears it.

### 10.5 Dual use

Tooling that maps an adversary's infrastructure could also map a journalist's. Access controls, purpose limits and audit logs reduce misuse.

Kofi's design gives the infrastructure-mapping tools to a small group, requires a recorded purpose for each query and logs who searched for what. A monthly review samples the logs for searches that do not fit the purpose, such as names of people rather than domains. The controls do not make misuse impossible, but they make it visible, which deters most of it and allows the rest to be found.

### Practice note — Professional codes

Engineering institutions publish codes of conduct that put public welfare first. In a security context those codes support refusal: a request that harms people or breaks the law is outside professional practice even if an employer insists. Kofi keeps a copy of his institution's code beside the privacy policy he references in design reviews.

### Worked example

A request arrives to enrich every internal alert with the employee's home address "for context". Kofi asks what decision needs it; none does. The field is removed from the design and the decision recorded with the privacy officer's agreement.

> **Synthetic case.** The request and decision are invented.

### Errors and limits

Ethics is not a checkbox at the end of design. This chapter is not legal advice.

### Exercises

- **EX028 — Profile risk.** Why can aggregating public facts about an employee be harmful even if each is public? *Rubric:* 3 = creates profile enabling stalking/harm; data-protection duties; 2 = privacy vaguely; 1 = harmless; 0 = none.
- **EX029 — Fail-safe push.** What should Lantern do if the generated block list for OT segments fails validation? *Rubric:* 3 = stop push, keep last good list, alert human; 2 = stop push; 1 = push empty list; 0 = none.
- **EX030 — Insider scrape.** Describe Kofi's correct response to the scraping request. *Rubric:* 3 = decline, document, escalate to privacy/legal; 2 = decline only; 1 = comply; 0 = none.

### Synthesis

Protect people, honour terms and law, fail safely in critical environments, and escalate requests that cross lines.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) explain HTTPS as the transport for TAXII 2.1; (2) read DNS records relevant to indicators; (3) understand how network address translation and shared hosting affect attribution; (4) configure collection to respect rate limits.

### 11.1 TAXII over HTTPS

TAXII 2.1 is a RESTful API over HTTPS. Clients discover API roots, list collections and get or add objects with pagination. Mutual authentication and TLS protect the channel; the TAXII specification defines the endpoints and media types, not the trust relationships, which come from agreements.

For Lantern this means a partner's server presents a certificate that Kofi's collector checks, and the collector presents its own certificate so the partner knows who is asking. Which collections BEN may read is set by the sharing agreement and enforced by the partner. A valid connection does not make the content trustworthy; it only shows where it came from.

### 11.2 DNS in intelligence

A domain indicator resolves through DNS to addresses that may change hourly. A records, CNAMEs and name servers each tell a different story. Passive DNS — historical resolution data from licensed providers — shows how infrastructure moved.

Kofi records the time of every resolution Lantern performs, because an answer without a time cannot be compared with anything. A domain that pointed at a hostile address last month may point at a parked page today. Passive DNS lets an analyst ask what the domain resolved to on the day of a sighting, which is the question an investigation usually needs answered. The provider's licence limits how long that history may be kept, and Lantern follows it.

### 11.3 NAT and shared hosting

Many devices can sit behind one public address; many websites can share one hosting address. Blocking such an address can cause collateral damage, and associating everything behind it with an adversary is a classic analytic mistake.

BEN met this when a partner listed an address used by a cloud provider's shared gateway. Blocking it would have cut off several services that BEN depends on. The worked example shows the safer route: block the specific domain at the DNS layer, where it does not affect other tenants, and record why the address was not blocked. Analysts should say that an address hosted hostile content, not that it belongs to the adversary.

### 11.4 Rate limits and politeness

Collection from partner TAXII servers follows their published limits. Back off on HTTP 429 responses; never rotate identities to evade limits.

A response with that status asks the client to slow down, and many servers say how long to wait. Lantern's collector honours that value, doubles its wait on repeated refusals and stops after a set number of tries, raising an alert for an engineer. Using many accounts or addresses to get around a limit would break the agreement and damage BEN's standing with the partner. A collector that respects limits keeps its access; one that does not loses it.

### 11.5 Ports and protocols in ATT&CK

ATT&CK technique T1071 Application Layer Protocol describes adversaries communicating over common protocols to blend in. Network indicators alone therefore miss much command-and-control; behavioural analytics complement them.

An attacker who sends commands over ordinary web traffic to a fresh domain leaves no indicator Lantern already knows. What may still stand out is the pattern: regular check-ins at fixed intervals, unusual amounts of data or connections from a host that never browses. Kofi passes these analytics to the detection team as a complement to the indicator feeds rather than a replacement.

### Practice note — Pagination and completeness

TAXII 2.1 responses can be paginated. A collector that reads only the first page will report success while missing most objects. Lantern follows the `more` and `next` indicators until the server reports completion, and records the count received per poll so that sudden drops become visible.

### Worked example

Kofi sees that a partner's indicator resolves to an address shared by 3,000 websites at a hosting provider. He marks it "do not block at perimeter", forwards it for DNS-layer blocking of the specific domain instead, and documents the reason.

> **Synthetic case.** The indicator and hosting count are invented.

### Errors and limits

DNS answers vary by resolver and time. Never test partner endpoints beyond agreed use.

### Exercises

- **EX031 — TAXII transport.** What does TAXII 2.1 specify, and what must come from agreements? *Rubric:* 3 = API/endpoints/media types over HTTPS; trust/permissions/sharing terms from agreements; 2 = one half; 1 = TAXII defines trust; 0 = none.
- **EX032 — Shared address.** Why block the domain rather than the address in Kofi's example? *Rubric:* 3 = address shared by many sites; collateral; domain specific; 2 = partial; 1 = block address; 0 = none.
- **EX033 — HTTP 429.** What is the correct client behaviour on HTTP 429 from a partner server? *Rubric:* 3 = back off/respect Retry-After; never evade; 2 = slow down; 1 = rotate IPs; 0 = none.

### Synthesis

TAXII rides on HTTPS, DNS tells time-dependent stories, shared addresses mislead, and polite clients back off.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) run intelligence services under least-privilege accounts; (2) use OS logs as evidence of platform behaviour; (3) isolate parsers that handle untrusted input; (4) patch and configure hosts for an always-on platform.

### 12.1 Service accounts

Lantern's collector runs as a dedicated account with permission only to its working directory and outbound HTTPS to partner servers. It cannot read the firewall configuration it eventually influences; a separate, audited service does that.

If the collector were compromised through a malicious partner file, the attacker would hold an account that can only read its own folder and talk to partner servers. They could not change firewall rules or reach the analysts' reports. Kofi lists each service account with its permissions and reviews the list after every release, removing any right that crept in for a test and was never taken back.

### 12.2 Logs as platform evidence

Authentication logs, process starts and file modifications show what the platform itself did. When a partner asks whether a TLP:RED report was accessed, the OS and application logs answer.

That question needs logs that were kept, protected from change and synchronised in time. Lantern sends host logs to a separate store where platform administrators can read but not delete them. Kofi tested the answer once by opening a test report and checking that the access appeared within a minute, with the user, the time and the object. A partner who trusts BEN with restricted material may ask for such a check, and BEN should be able to answer it confidently.

### 12.3 Isolating parsers

Partner files are untrusted input. Parsers run in a container or sandbox with no network access beyond what they need, read-only file systems where possible, and memory limits. A bug in a parser then cannot become a foothold in the SOC.

Kofi tests the sandbox by giving the parser a file that tries to open a network connection and another that tries to write outside its folder. Both attempts fail and are logged. A failed test would block the release until the sandbox is fixed.

### 12.4 Patching

Platforms facing the internet need prompt patching. A maintenance window, a tested image and a rollback snapshot let BEN patch weekly without long outages.

Kofi's routine applies patches first to a test host that replays a day of synthetic feed traffic. If the pipeline output matches the expected snapshot, the same image goes to production in the weekly window. A snapshot taken just before lets the team return to the previous state within minutes if something breaks. Urgent fixes for actively exploited flaws can skip the weekly wait, with the same test and rollback steps compressed into hours.

### 12.5 Time and scheduling

Cron or systemd timers schedule polls and decay recalculations. Record timers in configuration management so changes are reviewed.

An unreviewed timer is easy to miss. Kofi once found a decay job set to run every minute after a test, which loaded the database for no reason. Because timers now live in configuration management, such a change shows up in review and in the host baseline. Each timer records its purpose and owner, so nobody has to guess whether it can be removed. Times are set in UTC to avoid surprises when the clocks change.

### Practice note — Host baselines

A baseline lists expected processes, open ports and scheduled tasks for each Lantern host. A nightly comparison flags drift: an unexpected listener or a new timer. Baselines are kept in configuration management and reviewed after every approved change so that alerts mean something.

### Worked example

A partner archive contains a deliberately malformed file (synthetic test). The parser crashes inside its sandbox; the container restarts; a reject record is written. Nothing else on the host is affected, and the crash appears in logs with the file's hash for the partner.

> **Synthetic case.** The malformed file and sandbox behaviour are invented.

### Errors and limits

Running everything as root is fast to deploy and slow to recover from. Sandboxes reduce but do not remove risk.

### Exercises

- **EX034 — Collector rights.** Should the collector account be able to write firewall rules? Explain. *Rubric:* 3 = no; least privilege/separation; separate audited service; 2 = no; 1 = yes; 0 = none.
- **EX035 — Access question.** Which evidence answers "who opened the TLP:RED report?" *Rubric:* 3 = application access logs + OS authentication logs; 2 = one; 1 = ask staff; 0 = none.
- **EX036 — Sandbox settings.** Name three sandbox settings for a parser of untrusted files. *Rubric:* 3 = three of no/limited network, read-only FS, memory/CPU limits, unprivileged user; 2 = two; 1 = one; 0 = none.

### Synthesis

Least privilege, logs as evidence, sandboxed parsers and disciplined patching keep the platform trustworthy.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) normalise and de-duplicate indicators before storage; (2) choose keys and indexes for intelligence queries; (3) model provenance for every stored object; (4) design retention and deletion.

### 13.1 Normalisation

The same domain can arrive as `C2.Example.`, `c2.example` or defanged text. Without normalisation the store fills with duplicates and match counts lie.

The lab shows the effect: seven inputs, four real values. A match count based on raw strings would claim BEN saw seven distinct indicators when it saw four. Kofi's normaliser lowers case where case does not matter, removes a trailing dot from domains, strips spaces and refangs text, each step tested on its own. The order of the steps is fixed and documented.

### Lab 4 — normalise and de-duplicate

```python
"""Lab 4 (ch 13): normalise and de-duplicate synthetic indicators before storage."""
raw = ["C2.Example.", "c2.example", "hxxp://drop[.]example/a", "http://drop.example/a",
       "203.0.113.9", " 203.0.113.9 ", "198.51.100.44"]
def norm(s):
    s = s.strip().lower().replace("hxxp", "http").replace("[.]", ".")
    return s[:-1] if s.endswith(".") else s
seen, out = set(), []
for r in raw:
    n = norm(r)
    if n not in seen:
        seen.add(n); out.append(n)
print(f"raw={len(raw)} unique={len(out)}")
for o in out:
    print(" ", o)
```

Run with `python3 lab_dedupe.py`. Verified output:

```text
raw=7 unique=4
  c2.example
  http://drop.example/a
  203.0.113.9
  198.51.100.44
```

### 13.2 Reading the result

Seven raw strings collapse to four unique values. The trailing dot, capitals, defanging and surrounding spaces were all noise. Normalisation rules must be documented, versioned and idempotent.

Kofi treats the rules as part of the data model. Each rule has a written reason, a test, and a version number stored with every record it produced. Running the normaliser on its own output must give the same result, which the property tests in the programming chapter check. If a rule changes, older records can be found by version and reprocessed, rather than leaving two different normal forms in the store at once.

### 13.3 Keys and indexes

STIX 2.1 objects carry an `id` of the form `type--UUID`. Lantern keys objects by that id and indexes normalised indicator values for fast matching. Sightings are keyed by indicator id and time.

The identifier never changes, even if the indicator's description or confidence does, so references from relationships and sightings stay valid. Indexes are chosen from the questions analysts ask most. Kofi measured matching speed with and without the value index and found the difference large enough to justify its storage cost. Rarely used queries can run more slowly instead of having their own indexes.

### 13.4 Provenance

Each object records its source, TLP label, collection time and parser version. Duplicate indicators from two sources are stored once with both provenance entries, so analysts see corroboration.

Corroboration only counts if the sources are independent. If partner B simply copies partner A's feed, two entries add nothing. Kofi's model records where each partner says it obtained an indicator when the partner provides that, so analysts can spot repeated rather than independent reporting. The most restrictive label of any source travels with the shared record, so merging never relaxes a sharing limit.

### 13.5 Retention

Retention follows agreements and law. Deletion must reach backups within a stated period; "deleted from the UI" is not deletion.

Kofi's design gives each source a retention period from its agreement. A scheduled job removes expired records from the live store, and backups older than the longest period are destroyed on a fixed cycle, so nothing survives longer than allowed. The job writes a log of counts removed per source, which the privacy officer reviews. If a partner asks for deletion, the same log shows when it was done.

### Practice note — Query patterns

Analysts ask three kinds of question: does this value exist, what is related to it, and what changed recently. Exact-match lookups need hash indexes on normalised values; relationship queries need indexes on source and target ids; recency queries need time indexes. Designing indexes from real questions avoids both slow queries and wasted storage. Bulk deletions are rehearsed on a copy first, because a mistaken normalisation rule applied during deletion can remove far more than intended.

### Worked example

Kofi merges two partners' feeds. Normalisation finds that 18% of partner B's indicators already exist from partner A. Rather than discard them, Lantern adds partner B's provenance to the existing records, raising their corroboration count.

> **Synthetic case.** Feeds and percentages are invented.

### Errors and limits

Over-aggressive normalisation can merge distinct values (for example case-sensitive URL paths). Test rules against real formats.

### Exercises

- **EX037 — Unique count.** How many unique values does the lab produce from seven inputs? *Rubric:* 3 = 4; 2 = correct with one wrong listed value; 1 = 7; 0 = none.
- **EX038 — Corroboration.** Why keep both provenance entries for a duplicate indicator? *Rubric:* 3 = shows corroboration from independent sources; audit; 2 = audit only; 1 = discard duplicates; 0 = none.
- **EX039 — Path case.** Give an example where lower-casing a whole URL could be wrong. *Rubric:* 3 = case-sensitive path/query on server; 2 = vague; 1 = never wrong; 0 = none.

### Synthesis

Normalise carefully, key by stable ids, keep provenance, and make deletion real.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) apply version control, code review and continuous integration to a CTI platform; (2) manage dependencies with supply-chain care; (3) write change records that link to requirements; (4) separate configuration from code.

### 14.1 Version control and review

Every change to Lantern goes through a branch, an automated test run and a second engineer's review. Parser changes need a reviewer who understands the partner format.

Review is more than reading code. The reviewer runs the tests, checks that the change matches what was asked and asks what happens with bad input. For parser changes, a sample of real partner records under the agreement is run through both versions. Kofi has seen reviews catch a field being read from the wrong position, which tests on clean synthetic data had passed.

### 14.2 Continuous integration

CI runs unit tests, property tests and a replay of a synthetic feed through the whole pipeline, comparing outputs with a known-good snapshot. A difference fails the build until explained.

The replay is what made the change in the worked example visible: the snapshot showed exactly how many indicators would stay in blocking. A failing replay is not always a bug. Sometimes the change is intended, and the engineer updates the snapshot with a note explaining why. What matters is that every difference in output is explained before release.

### 14.3 Dependencies

Third-party libraries can carry vulnerabilities or be compromised. Pin versions, review updates, and prefer the standard library for small tasks. ATT&CK T1195 Supply Chain Compromise reminds defenders that their own tooling is a target.

Kofi's rule is that each new library needs a reason the standard library cannot meet, a named owner and a check of its maintainers and recent history. Updates arrive in a weekly batch, read before merging, and the build fails if a dependency is fetched without a fixed version and hash. Lantern holds partner data and influences firewalls, which makes a compromised library in its build an attractive route for an attacker.

### 14.4 Traceability

Each change cites the requirement or defect it addresses. When an auditor asks why the TLP gate allows AMBER to "org", the history links to the requirement and the TLP 2.0 definition.

Kofi links each commit to a ticket, and each ticket to a requirement number in the requirements document. An auditor can follow the chain from code back to the reason for it in a few clicks. Changes without a linked reason are not merged. This also helps when removing code: if the requirement has been withdrawn, the link shows which parts can go.

### 14.5 Configuration

Partner endpoints, credentials references and thresholds live in configuration, not code. Secrets live in a vault; configuration stores only references.

Separating them means the same tested code can run in test and production with different settings, and changing a threshold does not need a new build. Configuration changes still go through review, because a wrong threshold can do as much harm as a bug. Kofi keeps a short description beside each setting saying what it controls and who may change it. A credential is never pasted into configuration, even temporarily; the vault reference is the only thing stored.

### Practice note — Release notes

Each Lantern release ships with notes written for analysts: what behaviour changed, which thresholds moved and how to report problems. Analysts who understand a change are less likely to mistake new behaviour for an incident, and they report regressions faster.

### Worked example

A pull request lowers the decay floor from 30 to 20. CI's replay shows 1,240 more indicators would remain in automated blocking. The reviewer asks for the requirement; none exists. The change is rejected until the SOC lead agrees and a requirement is written.

> **Synthetic case.** The pull request and counts are invented.

### Errors and limits

Tests on synthetic data cannot prove behaviour on all partner data; keep sampling real formats under agreement. Speed pressure is the usual enemy of review.

### Exercises

- **EX040 — Replay value.** What does the synthetic-feed replay in CI catch that unit tests may miss? *Rubric:* 3 = end-to-end behaviour changes across stages; 2 = integration bugs vaguely; 1 = nothing; 0 = none.
- **EX041 — Rejected change.** Why was the decay-floor change rejected? *Rubric:* 3 = no requirement/owner agreement; large behavioural impact; 2 = one; 1 = tests failed; 0 = none.
- **EX042 — Secret location.** Where do partner credentials live, and what does configuration hold? *Rubric:* 3 = vault; config holds references; 2 = vault only; 1 = in code; 0 = none.

### Synthesis

Review, replay, pin, trace and keep secrets out of code.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to intelligence data; (2) define threat, vulnerability and risk; (3) place CTI within NIST CSF 2.0 functions; (4) explain why the CTI platform is itself a target.

### 15.1 CIA for intelligence

Confidentiality: TLP:RED reports must reach only named recipients. Integrity: a tampered indicator could block a legitimate supplier or, worse, a safety system's update server. Availability: when a campaign starts, analysts need the platform most.

Kofi writes a short note for each kind of data in Lantern stating which of the three properties matters most. Partner reports are mainly about confidentiality, block lists about integrity, and the matching service about availability. Controls are chosen from that note rather than applied equally everywhere.

### 15.2 Threat, vulnerability, risk

A threat is a potential cause of harm (an adversary or an accident). A vulnerability is a weakness that could be used. Risk combines likelihood and impact. CTI informs the threat side: which adversaries, which techniques, which targets.

Kofi keeps the terms apart in his reports. A partner bulletin about an actor targeting energy companies is threat information. An unpatched remote-access server at BEN is a vulnerability. The risk is that this actor uses that server, judged by how likely and how damaging that would be. Intelligence changes the likelihood estimate; it does not fix the server.

### 15.3 CTI in CSF 2.0

NIST CSF 2.0 organises outcomes as Govern, Identify, Protect, Detect, Respond and Recover. Threat intelligence feeds Identify (risk assessment), Detect (rules) and Respond (context), and sharing agreements are a Govern matter.

Placing intelligence work in these functions helps BEN explain its value. A new detection rule written from a partner report is a Detect outcome; a briefing that changes the risk register is Identify. Agreements about what BEN may share, with whom and under what label sit under Govern, because they set obligations for the whole organisation rather than one team. Kofi tags each Lantern output with the function it serves.

### 15.4 The platform as target

An adversary who poisons Lantern could make BEN block its own suppliers or ignore real threats. Integrity controls — signed feeds where available, source reputation, anomaly checks on volume — protect against poisoning.

Kofi's anomaly checks compare each delivery with that source's history. A sudden jump in volume, many indicators for well-known services or entries that match BEN's allow-list all hold the delivery for review. Source reputation falls when a partner's entries are later found wrong, which lowers the confidence of its future deliveries until the record improves.

### 15.5 Kill chain as defensive map

Hutchins et al. argued that defenders can act at every phase. Lantern's outputs map to phases: domain blocks to delivery and command and control, behavioural analytics to installation and actions on objectives.

The mapping shows where BEN's defences are thin. When Kofi tallied Lantern's outputs by phase, most fell in delivery and command and control, because indicators are easy to share for those phases. Few addressed what an intruder does after gaining a foothold. That gap became a request to the detection team for behavioural analytics on internal hosts.

### Practice note — Accountability

Every automated block must be explainable: which indicator, which source, which confidence, which rule. Lantern stores that chain with the block so that when a supplier complains, the SOC can answer in minutes and correct the source rather than guessing.

### Worked example

A partner feed suddenly includes BEN's own payroll provider's domain. Kofi's anomaly check flags it because the domain appears in BEN's allow-list of critical suppliers. Analysts confirm the entry was a partner error; blocking would have stopped salary payments.

> **Synthetic case.** The feed error and supplier are invented.

### Errors and limits

Allow-lists can themselves be abused; review them. CIA is a starting vocabulary, not a full risk method.

### Exercises

- **EX043 — Integrity harm.** Describe one integrity failure in Lantern and its operational consequence. *Rubric:* 3 = tampered/poisoned indicator → blocking legitimate service or missing threat; 2 = vague tamper; 1 = confidentiality example; 0 = none.
- **EX044 — CSF placement.** Name two CSF 2.0 functions that CTI supports, with an example each. *Rubric:* 3 = two functions with matching examples; 2 = two names; 1 = one; 0 = none.
- **EX045 — Poison check.** Why compare feed contents with an allow-list of critical suppliers? *Rubric:* 3 = catches poisoning/errors that would block critical services; 2 = partial; 1 = speed; 0 = none.

### Synthesis

Apply CIA to intelligence itself, place CTI in CSF, and protect the platform from poisoning.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) define a system boundary and its stakeholders; (2) write a concept of operations for a CTI platform; (3) manage interfaces with an interface control document; (4) plan the life cycle from concept to retirement.

### 16.1 Boundary and stakeholders

Lantern's boundary includes collectors, store, enrichment, analyst interface and dissemination. Outside it: partner servers, BEN's firewalls and SIEM, the sector ISAC. Stakeholders include SOC analysts, OT engineers, the privacy officer, partners and executives.

### 16.2 Concept of operations

A ConOps describes, in operators' words, how the system is used: "At 07:00 the duty analyst reviews overnight high-confidence indicators; automatic blocks apply to IT segments only; OT blocks await approval." It is the reference for requirements.

### 16.3 Interface control

Each interface — TAXII 2.1 with partners, the SIEM API, the firewall push — has an interface control document: data formats, rates, authentication, error handling and owners on both sides.

### 16.4 Life cycle

Concept, requirements, design, build, verification, validation, operation and retirement. Retirement matters in CTI: decommissioning a feed means telling the partner, deleting retained restricted data and removing credentials.

### 16.5 Trade studies

Build versus buy, on-premises versus cloud, open-source versus commercial threat-intelligence platforms: trade studies weigh cost, control, integration and risk with explicit criteria.

### Practice note — Stakeholder map

Kofi draws a map of stakeholders with their interest and influence. The privacy officer has high influence and a narrow interest; partners have moderate influence and a strong interest in reciprocity. The map guides who reviews which documents and avoids late surprises. Kofi keeps the ConOps to four pages so that operators actually read and correct it.

### Worked example

Kofi writes the ICD for the firewall push: STIX indicators converted to vendor rule format; maximum 5,000 rules per push; mutual TLS; failure returns error and keeps the previous rule set; owners — Lantern team and network operations.

> **Synthetic case.** The ICD values are invented.

### Errors and limits

Systems engineering paperwork that nobody reads is waste; keep documents short and used. Missing stakeholders surface late and expensively.

### Exercises

- **EX046 — Boundary call.** Is the sector ISAC's TAXII server inside Lantern's boundary? Explain. *Rubric:* 3 = no; external interface owned by ISAC; 2 = no; 1 = yes; 0 = none.
- **EX047 — ICD fields.** List five fields of an interface control document. *Rubric:* 3 = five of format, rate, auth, error handling, owners, versioning; 2 = three; 1 = one; 0 = none.
- **EX048 — Retirement steps.** What three actions retire a partner feed? *Rubric:* 3 = notify partner, delete retained restricted data, revoke credentials; 2 = two; 1 = turn off poller; 0 = none.

### Synthesis

Draw the boundary, speak the operators' language, control interfaces, and plan retirement from day one.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) model the intelligence cycle as a feedback loop; (2) identify sensors, controllers and actuators in a CTI workflow; (3) recognise oscillation and lag; (4) design feedback from consumers to producers.

### 17.1 Loops

A thermostat measures temperature, compares it with a set point, and acts. Lantern measures false-positive rates of blocks, compares them with a target, and adjusts confidence thresholds. Without measurement the loop is open and drifts.

### 17.2 Parts of the loop

Sensor: SOC tickets marking blocks as false positives. Controller: the rule that raises or lowers the threshold. Actuator: the block list pushed to firewalls. Disturbance: a partner suddenly publishing low-quality indicators.

### 17.3 Lag and oscillation

If the threshold changes daily based on yesterday's complaints, it can overshoot: too strict one day, too loose the next. Damping — small steps, averaging over a week — stabilises the loop.

### 17.4 Feedback to producers

NIST SP 800-150 encourages two-way sharing relationships. Telling partners which of their indicators caused false positives improves the whole community's loop, provided it respects TLP and agreements.

### 17.5 Human in the loop

Automated control is fine for IT perimeter blocks with low impact; for OT segments, a human approves each change, which deliberately slows the loop where mistakes are costly.

### Practice note — Set points from policy

The target false-positive rate is not an engineering choice alone. Operations managers decide how much disruption is tolerable, and Lantern's controller uses that set point. Writing the set point into policy makes later adjustments a governed decision rather than a quiet code change.

### Worked example

False-positive tickets jump from 3 to 25 after a partner adds a large unvetted list. Kofi's controller lowers the partner's weight by 10% per day, capped at 30% total, instead of disabling it outright, and sends the partner a summary of affected indicators.

> **Synthetic case.** Ticket counts and weights are invented.

### Errors and limits

Feedback signals can be biased: analysts report false positives more than missed detections. Measure both.

### Exercises

- **EX049 — Name the parts.** Identify sensor, controller and actuator in Lantern's threshold loop. *Rubric:* 3 = FP tickets; threshold rule; pushed block list; 2 = two; 1 = one; 0 = none.
- **EX050 — Damping choice.** Why limit the weight change to 10% per day? *Rubric:* 3 = avoids oscillation/overreaction to noisy signal; 2 = caution vaguely; 1 = faster is better; 0 = none.
- **EX051 — Biased signal.** Why might relying only on false-positive tickets bias the loop? *Rubric:* 3 = misses false negatives; pushes toward permissiveness; 2 = partial; 1 = no bias; 0 = none.

### Synthesis

Close the loop with measurement, damp it to avoid oscillation, share feedback upstream, and keep humans where errors are costly.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) place Lantern in BEN's zones and conduits; (2) design trust boundaries between IT, OT and partner networks; (3) apply defence in depth to an intelligence platform; (4) choose where indicators are enforced.

### 18.1 Zones

BEN separates corporate IT, the SOC zone, a DMZ for external exchanges and OT zones for substations. Lantern's collectors live in the DMZ; its store and analyst interface in the SOC zone; nothing of Lantern runs in OT.

### 18.2 Conduits

Data flows from DMZ collectors to the SOC store through one inspected conduit. Block lists flow from the SOC to IT firewalls automatically and to OT firewalls through an approval service. Each conduit has an owner and a rule set.

### 18.3 Depth

Network segmentation, mutual TLS between components, signed internal messages, role-based access for analysts and audit logging provide independent layers. Compromise of a collector should not yield the store.

### 18.4 Enforcement points

Indicators can be enforced at DNS resolvers, web proxies, firewalls and endpoint agents. Each has different collateral risk: DNS blocks a name precisely; a firewall block on a shared address affects many sites.

### 18.5 Analyst workstations

Analysts open suspicious reports and samples. Their workstations need isolation from production systems and a separate browsing environment for OSINT research to avoid exposing BEN's identity.

### Practice note — Architecture verification

Kofi verifies the diagram against reality with flow logs: every observed connection between zones must match an approved conduit. Unexpected flows become findings. This catches the shortcuts that appear during incidents and are never removed. Findings are tracked until the stray flow is either approved through change control or removed.

### Worked example

An architecture review finds that the enrichment service in the SOC zone calls external lookup APIs directly. Kofi moves outbound enrichment calls to a DMZ proxy so that the SOC zone has no direct internet access.

> **Synthetic case.** The review finding is invented.

### Errors and limits

Diagrams drift from reality; verify flows with network evidence. OT design must involve OT engineers.

### Exercises

- **EX052 — OT placement.** Why does no Lantern component run inside OT zones? *Rubric:* 3 = keep OT minimal/isolated; reduce attack surface and safety risk; 2 = partial; 1 = should run in OT; 0 = none.
- **EX053 — Enforcement pick.** For a malicious domain on shared hosting, which enforcement point is preferred and why? *Rubric:* 3 = DNS/proxy domain block; precise, avoids collateral; 2 = point only; 1 = firewall IP block; 0 = none.
- **EX054 — Enrichment egress.** What risk did moving enrichment calls to a DMZ proxy reduce? *Rubric:* 3 = SOC zone direct internet exposure/exfil path; 2 = vague; 1 = performance; 0 = none.

### Synthesis

Zone the platform, control conduits, layer defences, enforce precisely and keep analysts' research separate.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) authenticate partners and analysts with appropriate strength; (2) use digital signatures to protect feed integrity; (3) manage keys and certificates over their life cycle; (4) apply role-based access to TLP-labelled content.

### 19.1 Partner identity

TAXII 2.1 servers authenticate clients, typically with HTTP authentication over TLS or client certificates. Mutual TLS lets both sides prove identity. Credentials are per-partner so that one can be revoked without affecting others.

### 19.2 Signatures

A signature over an exported bundle lets the recipient verify that it came from Lantern and was not altered. Hash first (SHA-256), sign the hash with a private key kept in hardware, publish the public key through a trusted channel.

### 19.3 Key life cycle

Generate, distribute, use, rotate, revoke, destroy. Certificates expire; expired certificates on a TAXII client stop collection at the worst moment. Calendar and monitor them.

### 19.4 Analyst access

Roles map to TLP: all analysts read CLEAR and GREEN; the SOC team reads AMBER; AMBER+STRICT content is limited to BEN only; RED reports go to named individuals listed on each report. Access decisions are logged.

### 19.5 Multi-factor

Analyst access to Lantern requires MFA. ATT&CK T1078 Valid Accounts describes adversaries using legitimate credentials; MFA raises the cost.

### Practice note — Break-glass access

If the identity provider fails during an incident, analysts still need Lantern. A sealed break-glass account with a long random password, stored offline and logged on use, provides access. Its use triggers an alert and a review afterwards so that emergency access never becomes routine. Each break-glass use is reviewed within one working day by someone other than the user.

### Worked example

A partner's client certificate expires on a Sunday, halting their feed. Kofi adds certificate-expiry monitoring with 30-, 14- and 3-day alerts and documents a rotation runbook with the partner.

> **Synthetic case.** The expiry incident is invented.

### Errors and limits

Signatures prove origin and integrity, not truth of the content. Shared team accounts defeat access logs.

### Exercises

- **EX055 — Signature limit.** What does a valid signature on a feed prove, and what does it not? *Rubric:* 3 = origin/integrity; not accuracy of indicators; 2 = one half; 1 = proves truth; 0 = none.
- **EX056 — RED access.** Who may read a TLP:RED report in Lantern? *Rubric:* 3 = only named recipients listed on the report; 2 = small team; 1 = all SOC; 0 = none.
- **EX057 — Expiry alerts.** Propose an alert schedule for certificate expiry. *Rubric:* 3 = multiple lead times (e.g. 30/14/3 days) + owner; 2 = one alert; 1 = none; 0 = none.

### Synthesis

Authenticate per partner, sign exports, manage key life cycles, and map roles to TLP with logged access.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Threat intelligence and OSINT: engineering context

### Learning outcomes

You will (1) describe the CTI life cycle as an engineered service; (2) distinguish data, information and intelligence; (3) identify consumers and their decisions; (4) frame Lantern's mission in one sentence.

### 20.1 Data, information, intelligence

Data are raw observations: a domain in a feed. Information is organised data: the domain was seen in phishing against utilities. Intelligence is analysed information relevant to a decision: BEN should block the domain at DNS and hunt for past contacts because the campaign targets distribution operators.

### 20.2 Consumers and decisions

Consumers include SOC analysts (block, hunt, escalate), OT engineers (approve changes), risk managers (prioritise investment), executives (accept risk) and partners (their own decisions). Each needs different formats and timeliness.

### 20.3 The service view

Lantern is a service with inputs (feeds, OSINT, internal telemetry), processing (validation, enrichment, analysis) and outputs (blocks, reports, shared objects). Service levels apply: for example, high-confidence indicators reach IT enforcement within 30 minutes.

### 20.4 Mission statement

"Lantern turns shared and open-source threat information into timely, trustworthy, legally collected intelligence that helps BEN prevent and detect attacks on its IT and OT environments." Every later requirement should trace to it.

### 20.5 Frameworks as context

The Diamond Model, the kill chain, ATT&CK, STIX/TAXII and TLP give a common language with partners. Engineering adopts them where they help interoperability and analysis, not as decoration.

### Practice note — Feedback from consumers

Kofi adds a one-click 'useful / not useful' control to every Lantern report. The counts are crude, but they close a loop the intelligence cycle usually leaves open, and they reveal which products deserve investment.

### Worked example

Kofi interviews five consumers. The OT engineer says: "I don't want indicators; I want to know if a campaign targets our relay vendor." That is a strategic-operational need, so Lantern adds a vendor-watch report instead of more feeds.

> **Synthetic case.** Interviews are invented.

### Errors and limits

More feeds do not equal more intelligence. Missions that promise "complete visibility" are unverifiable.

### Exercises

- **EX058 — DII ladder.** Classify "domain seen in phishing against utilities". *Rubric:* 3 = information (organised context, not yet decision-specific); 2 = right with weak reason; 1 = intelligence; 0 = none.
- **EX059 — Consumer need.** What output best serves the OT engineer's stated need? *Rubric:* 3 = vendor-focused campaign report/watch; 2 = vague report; 1 = more indicators; 0 = none.
- **EX060 — Mission test.** Which word in Lantern's mission statement commits to lawful OSINT? *Rubric:* 3 = "legally collected" identified; 2 = points to collection; 1 = wrong; 0 = none.

### Synthesis

Climb from data to intelligence, serve named decisions, and anchor everything in a testable mission.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Threat intelligence and OSINT: requirements

### Learning outcomes

You will (1) collect priority intelligence requirements (PIRs) from stakeholders; (2) turn PIRs into system requirements; (3) write requirements that are verifiable; (4) maintain traceability.

### 21.1 PIRs

Priority intelligence requirements are questions decision-makers need answered: "Which adversaries target electricity distributors in our region?" "Are our OT vendors being targeted?" They direct collection and analysis and should be reviewed each quarter.

### 21.2 From PIR to system requirement

A PIR about OT vendors implies requirements: ingest vendor advisories; tag objects with vendor names; alert when a campaign mentions a tagged vendor. Each is a "shall" statement with a verification method.

### 21.3 Verifiable wording

"The system shall be fast" cannot be verified. "Lantern shall deliver indicators with confidence ≥ 70 to IT DNS enforcement within 30 minutes of ingestion for 95% of indicators per month" can.

### 21.4 Non-functional requirements

Confidentiality (TLP enforcement), integrity (signature verification where offered), availability (99.5% monthly), privacy (no personal social-media collection), retention and auditability are requirements too, not afterthoughts.

### 21.5 Traceability matrix

A table links PIRs → requirements → design elements → tests. When a PIR is retired, its requirements can be reviewed for removal.

### Practice note — Requirement reviews

Requirements are reviewed with the stakeholders who own them. The SOC lead signs off on timeliness, the privacy officer on minimisation, the OT engineer on approval gates. A requirement without an owner is a candidate for deletion. Kofi also records which PIR each requirement serves, so the quarterly PIR review can see immediately which parts of Lantern would lose their justification if a question were retired. That link keeps the platform from growing features nobody asked for.

### Worked example

Kofi converts the OT vendor PIR into four requirements and writes a test for each, such as "Given a synthetic advisory naming vendor V, Lantern raises an alert to the OT channel within 15 minutes."

> **Synthetic case.** The PIR and tests are invented.

### Errors and limits

Requirements that copy a vendor's product features are not stakeholder needs. Too many PIRs means none are priorities.

### Exercises

- **EX061 — Verifiable rewrite.** Rewrite "Lantern shall share quickly with partners" as a verifiable requirement. *Rubric:* 3 = metric, threshold, scope, percentage/time; 2 = metric only; 1 = unchanged; 0 = none.
- **EX062 — PIR derivation.** Derive one system requirement from "Which adversaries target regional distributors?" *Rubric:* 3 = specific shall statement (e.g. tag/report actor targeting sector) with verification; 2 = vague; 1 = unrelated; 0 = none.
- **EX063 — Privacy requirement.** Write a privacy requirement for Lantern's OSINT module. *Rubric:* 3 = verifiable prohibition/limit (no personal social profiles; organisational sources only) + test; 2 = statement without test; 1 = none; 0 = none.

### Synthesis

Ask decision-makers, derive verifiable shalls, include non-functional needs, and trace everything.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Threat intelligence and OSINT: system and data models

### Learning outcomes

You will (1) model Lantern's data with STIX 2.1 objects and relationships; (2) choose which STIX objects to support; (3) model provenance and confidence; (4) validate objects against required properties.

### 22.1 STIX 2.1 core

STIX 2.1 defines domain objects (indicator, malware, threat-actor, campaign, attack-pattern, report and others), cyber-observable objects (domain-name, ipv4-addr, file), and relationship and sighting objects. Every domain object needs `type`, `spec_version`, `id`, `created` and `modified`; indicators also need `pattern`, `pattern_type` and `valid_from`.

### 22.2 Choosing a subset

Lantern supports indicator, attack-pattern (linked to ATT&CK IDs via external references), campaign, threat-actor, malware, report, relationship and sighting. Unsupported types are stored opaquely and flagged for review rather than dropped.

### 22.3 Confidence and markings

STIX offers a `confidence` property (0–100) and marking definitions, including TLP markings. Lantern maps its internal decayed confidence to that property on export and attaches TLP 2.0 markings to every shared object.

### 22.4 Validation

Before storing, the validator checks required properties and identifier format. The masters-level lab in this course family checks the same rules; Lantern enforces them in the pipeline and counts failures per source.

### 22.5 System model

Beyond data: components (collector, validator, store, enricher, analyst UI, publisher), their interfaces and states. A state machine for an indicator — new, active, decayed, retired — makes behaviour explicit.

### Practice note — Mapping external references

Attack-pattern objects carry external references to ATT&CK technique pages, for example T1566 Phishing. Lantern validates that such references use real technique IDs, because mistyped IDs silently break detection coverage reports that group findings by technique.

### Worked example

A partner sends a threat-actor object without `spec_version`. Lantern rejects it with a reason, stores the hash, and notifies the partner's data contact. Their next export includes the property.

> **Synthetic case.** The object and partner are invented.

### Errors and limits

STIX is expressive; supporting everything adds complexity without value. Confidence numbers from different producers are not directly comparable.

### Exercises

- **EX064 — Indicator extras.** Which three properties must an indicator have beyond the common ones? *Rubric:* 3 = pattern, pattern_type, valid_from; 2 = two; 1 = one; 0 = none.
- **EX065 — Unsupported type.** How should Lantern treat a STIX type it does not support? *Rubric:* 3 = store opaquely + flag for review, not drop; 2 = flag; 1 = drop; 0 = none.
- **EX066 — State machine.** List the indicator states and one transition trigger. *Rubric:* 3 = new/active/decayed/retired + valid trigger (decay below floor, re-sighting); 2 = states only; 1 = partial; 0 = none.

### Synthesis

Use a deliberate STIX subset, validate required properties, carry confidence and TLP markings, and make states explicit.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Threat intelligence and OSINT: threat and failure analysis

### Learning outcomes

You will (1) threat-model the CTI platform itself; (2) perform a failure modes and effects analysis (FMEA); (3) rank risks by severity, occurrence and detection; (4) map adversary techniques against Lantern using ATT&CK IDs.

### 23.1 Threats to Lantern

Feed poisoning, credential theft (T1078 Valid Accounts), supply-chain compromise of a dependency (T1195), exfiltration of restricted reports, and denial of service by oversized feeds. Each threat maps to a control.

### 23.2 FMEA

For each component, list failure modes, effects and causes. Score severity (S), occurrence (O) and detection difficulty (D) on 1–10; the risk priority number RPN = S × O × D ranks attention.

### 23.3 Example rows

Collector stops silently: S6, O4, D7 → RPN 168. Bad block pushed to IT: S8, O3, D4 → 96. TLP:RED report mis-shared: S9, O2, D6 → 108. The silent collector stop ranks highest because nobody would notice for days.

### 23.4 Acting on rankings

High detection scores call for monitoring: a heartbeat alert if no objects arrive from a partner for six hours. High severity calls for prevention and approval gates.

### 23.5 Accidents

Not every failure is malicious. A partner's mistaken mass upload or a clock error can cause harm. Failure analysis covers both.

### Practice note — Abuse cases

Alongside use cases Kofi writes abuse cases: 'A partner account uploads ten million objects', 'An analyst exports a RED report to personal mail'. Each abuse case maps to a control and a test, turning the threat model into verifiable work. The abuse cases are reviewed whenever a new partner or interface joins the platform.

### Worked example

Kofi's FMEA shows the silent collector stop at RPN 168. He adds per-partner heartbeat monitoring, reducing D to 2 and RPN to 48, and records the change in the risk register.

> **Synthetic case.** Scores are invented.

### Errors and limits

RPN multiplies ordinal scales, so treat it as a ranking aid, not a precise measure. Threat models go stale; review after major changes.

### Exercises

- **EX067 — RPN compute.** Compute RPN for S7, O3, D5. *Rubric:* 3 = 105; 2 = method right; 1 = sum; 0 = none.
- **EX068 — After heartbeat.** With D reduced from 7 to 2, what is the collector RPN? *Rubric:* 3 = 48; 2 = method; 1 = wrong; 0 = none.
- **EX069 — Technique link.** Which ATT&CK technique ID covers an attacker using a stolen analyst login? *Rubric:* 3 = T1078 Valid Accounts; 2 = name only; 1 = wrong; 0 = none.

### Synthesis

Threat-model the platform, rank failures with FMEA, add detection where failures are silent, and cover accidents as well as adversaries.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Threat intelligence and OSINT: methods I

### Learning outcomes

You will (1) apply the Diamond Model to structure an incident's intelligence; (2) map observed behaviour to ATT&CK techniques; (3) place controls along the kill chain; (4) record analytic confidence and sources.

### 24.1 Diamond structuring

For each event, record adversary (if known), capability (malware, technique), infrastructure (domains, addresses) and victim (asset, organisation). Unknown vertices stay "unknown"; filling them by guess is the classic error.

### 24.2 ATT&CK mapping

Behaviours map to technique IDs: phishing email → T1566; scripting on the host → T1059 Command and Scripting Interpreter; web-protocol C2 → T1071. Mapping supports detection engineering and comparison with group profiles.

### 24.3 Kill-chain controls

Hutchins et al. proposed a courses-of-action matrix: detect, deny, disrupt, degrade, deceive and destroy across phases. Lantern produces inputs for several cells — deny at delivery via mail filtering, detect at C2 via DNS analytics.

### 24.4 Sources and confidence

Each analytic statement cites its sources and confidence. Admiralty-style source grading or a simple scale (confirmed, probable, possible) helps readers.

### 24.5 OSINT within limits

Methods include certificate-transparency lookups for related domains and reading public advisories. Researchers do not interact with adversary infrastructure or register accounts on criminal forums for this course.

### Practice note — Analytic notes

Each incident's Diamond record carries an analytic note: what was observed, what was inferred and what remains unknown. Separating those three lines prevents later readers from mistaking an inference for an observation when the record is reused months later. Reviewers check that every inference line names the evidence it rests on.

### Worked example

A synthetic phishing incident at BEN: capability T1566 plus a script dropper (T1059), infrastructure drop.example, victim a billing clerk's workstation, adversary unknown. Courses of action: deny delivery with a mail rule; detect C2 via DNS for drop.example; hunt for T1059 on other workstations.

> **Synthetic case.** The incident is invented.

### Errors and limits

ATT&CK mapping is interpretive; two analysts may differ. Keep evidence linked.

### Exercises

- **EX070 — Unknown vertex.** How should the adversary vertex be recorded in Kofi's incident, and why? *Rubric:* 3 = unknown; avoid guessing attribution; 2 = unknown; 1 = name a group; 0 = none.
- **EX071 — Technique IDs.** Give technique IDs for the phishing email and the script execution. *Rubric:* 3 = T1566 and T1059; 2 = one; 1 = wrong; 0 = none.
- **EX072 — Course of action.** Give one deny and one detect action with kill-chain phase. *Rubric:* 3 = deny at delivery (mail rule) + detect at C2 (DNS); 2 = one; 1 = vague; 0 = none.

### Synthesis

Structure with the Diamond, map with ATT&CK, act along the kill chain, and keep sources and confidence attached.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) produce a first end-to-end design for Lantern's ingestion path; (2) present it to a review panel; (3) capture decisions in architecture decision records (ADRs); (4) respond to critique with design changes.

### 25.1 Studio brief

Design the path from partner TAXII 2.1 collections to an analyst-ready store: polling, validation, normalisation, de-duplication, provenance, TLP enforcement and monitoring. Constraints: standard-library prototypes, synthetic data, BEN's zone model.

### 25.2 ADRs

An architecture decision record states context, decision, alternatives and consequences in one page. "Poll every 15 minutes rather than subscribe to push" — context: TAXII 2.1 is pull-based for collections; consequences: up to 15 minutes latency.

### 25.3 Panel review

The panel includes an analyst, an OT engineer and a privacy officer. Each asks from their role: Is it timely? Is OT protected? Is personal data minimised?

### 25.4 Iterating

Critique becomes backlog items. Designs improve when students change them in response, not when they defend every choice.

### 25.5 Deliverables

A diagram, five ADRs, an interface list, a monitoring plan and a demonstration of the pipeline on synthetic data.

### Practice note — Demonstration discipline

The studio demonstration runs on synthetic data from a clean environment, with the commands scripted in advance. Live improvisation in front of a panel hides defects and wastes time; a scripted run shows what the design actually does. Students rehearse the scripted run twice before the panel, once on a fresh machine, so environment surprises appear in rehearsal rather than in front of reviewers. Afterwards the panel's comments and the team's responses are filed with the ADRs as the studio record.

### Worked example

The privacy officer asks why the design stores full email headers from phishing reports. Kofi's ADR had no reason. He changes the design to store only sender domain, subject hash and indicator fields, and writes a new ADR recording the change.

> **Synthetic case.** The studio panel is invented.

### Errors and limits

Studios reward clarity, not volume. A design without monitoring is incomplete.

### Exercises

- **EX073 — ADR parts.** List the four sections of an ADR. *Rubric:* 3 = context, decision, alternatives, consequences; 2 = three; 1 = one; 0 = none.
- **EX074 — Polling consequence.** State one consequence of 15-minute polling. *Rubric:* 3 = up to 15 min latency (plus load trade-off); 2 = latency vaguely; 1 = none; 0 = none.
- **EX075 — Header minimisation.** What fields replace full email headers in the revised design? *Rubric:* 3 = sender domain, subject hash, indicator fields; 2 = two; 1 = keep full headers; 0 = none.

### Synthesis

Design end to end, record decisions, invite role-based critique and change the design when critique is right.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Threat intelligence and OSINT: architecture alternatives

### Learning outcomes

You will (1) compare build, buy and community-platform options for CTI; (2) run a weighted trade study; (3) assess lock-in and data portability through STIX/TAXII support; (4) record the decision and its review date.

### 26.1 Three options

Option A: extend Lantern in-house. Option B: buy a commercial threat-intelligence platform. Option C: adopt an open-source community platform such as MISP and integrate it with BEN's controls. Each can ingest feeds and share with partners; they differ in cost, control, staffing and support.

### 26.2 Criteria and weights

Kofi agrees criteria with stakeholders before scoring: interoperability (STIX/TAXII 2.1), TLP enforcement, OT approval workflow, total cost over five years, staffing burden, data residency, and exit cost. Weights sum to 100. Agreeing weights first prevents the favourite option from shaping the criteria.

### 26.3 Portability

If a platform cannot export everything as standard STIX 2.1 bundles, leaving it later means losing history. Exit cost is a real criterion, not a footnote.

### 26.4 Hybrid answers

Trade studies often end in hybrids: a community platform for partner sharing plus a thin in-house service for OT approvals and firewall pushes. Hybrids add integration work, which must be scored too.

### 26.5 Review dates

Markets and staffing change. The decision record sets a review date — for example in two years — and the triggers that would force an earlier review, such as loss of the only engineer who knows the in-house code.

### Worked example

Scores (out of 100): A 68, B 71, C 74. Option C wins narrowly on interoperability and cost but scores lower on OT workflow. Kofi recommends C plus a small in-house OT approval service, notes that the margin is within scoring uncertainty, and asks the panel to judge the OT risk explicitly.

> **Synthetic case.** Scores and options are illustrative; no vendor is evaluated.

### Errors and limits

Close scores are ties in practice; say so. Vendor demonstrations on vendor data prove little; test with synthetic BEN-like data.

### Exercises

- **EX076 — Weights first.** Why must criteria weights be agreed before options are scored? *Rubric:* 3 = prevents biasing criteria toward a favourite; 2 = fairness vaguely; 1 = order irrelevant; 0 = none.
- **EX077 — Exit cost.** How does STIX 2.1 export capability affect exit cost? *Rubric:* 3 = full standard export lowers cost/preserves history; lack raises it; 2 = partial; 1 = unrelated; 0 = none.
- **EX078 — Narrow margin.** Scores of 71 and 74 differ by three points. How should Kofi present that? *Rubric:* 3 = within uncertainty; treat as near-tie; surface key qualitative risk; 2 = mention closeness; 1 = clear winner; 0 = none.

### Synthesis

Agree weights first, score portability, accept hybrids with their integration cost, and set a review date.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Threat intelligence and OSINT: control design

### Learning outcomes

You will (1) implement TLP 2.0 as an enforceable dissemination control; (2) fail closed on unknown labels; (3) design approval gates for high-impact actions; (4) log control decisions for audit.

### 27.1 TLP as a control

FIRST TLP 2.0 defines who may receive information: CLEAR without restriction; GREEN within the community; AMBER within the recipient organisation and its clients on a need-to-know basis; AMBER+STRICT within the organisation only; RED to named recipients only. Lantern turns those definitions into a gate on every export and every analyst view.

### Lab 5 — dissemination gate

```python
"""Lab 5 (ch 27): TLP 2.0 dissemination gate for synthetic reports and audiences."""
ALLOWED = {
    "TLP:CLEAR": {"public", "community", "org", "team"},
    "TLP:GREEN": {"community", "org", "team"},
    "TLP:AMBER": {"org", "team"},
    "TLP:AMBER+STRICT": {"team", "org-only"},
    "TLP:RED": {"named-recipients"},
}
requests = [("R-1", "TLP:GREEN", "public"), ("R-2", "TLP:AMBER", "org"),
            ("R-3", "TLP:RED", "team"), ("R-4", "TLP:CLEAR", "public"), ("R-5", "TLP:PURPLE", "team")]
for rid, label, aud in requests:
    if label not in ALLOWED:
        verdict = "BLOCK unknown label"
    else:
        verdict = "ALLOW" if aud in ALLOWED[label] else "BLOCK"
    print(rid, label, "->", aud, verdict)
```

Run with `python3 lab_tlp.py`. Verified output:

```text
R-1 TLP:GREEN -> public BLOCK
R-2 TLP:AMBER -> org ALLOW
R-3 TLP:RED -> team BLOCK
R-4 TLP:CLEAR -> public ALLOW
R-5 TLP:PURPLE -> team BLOCK unknown label
```

### 27.2 Reading the gate

GREEN to the public is blocked; AMBER to the organisation is allowed; RED to a team is blocked because only named recipients qualify; CLEAR to the public is allowed; an unknown label, TLP:PURPLE, is blocked. The lab simplifies audiences into categories; production rules also check recipient identity.

### 27.3 Fail closed

Unknown or missing labels must block, not allow. A typo in a label should never publish restricted content.

### 27.4 Approval gates

Pushes to OT firewalls, sharing beyond the community and deleting indicators are high-impact. Each requires a named approver, and the approval is recorded with the object version.

### 27.5 Audit

Every allow and block decision is logged with requester, label, audience and time. Auditors and partners can then verify that agreements were honoured.

### Training the humans

Kofi runs a short session for analysts showing the gate's decisions on real-looking synthetic examples. When people understand why GREEN cannot reach the public blog, they ask partners for publishable summaries instead of hunting for workarounds.

### Worked example

An analyst tries to post a GREEN partner bulletin to BEN's public blog. The gate blocks it; the analyst asks the partner for permission to publish a CLEAR summary instead, which the partner provides in writing.

> **Synthetic case.** The bulletin and request are invented.

### Errors and limits

Labels describe sharing limits, not classification levels in a government sense. Gates cannot stop someone retyping content; training and culture still matter.

### Exercises

- **EX079 — Gate verdicts.** Quote the lab verdicts for R-1 and R-3. *Rubric:* 3 = R-1 BLOCK (GREEN to public), R-3 BLOCK (RED to team); 2 = one; 1 = allow; 0 = none.
- **EX080 — Unknown label.** Why does R-5 block rather than allow? *Rubric:* 3 = unknown label → fail closed; 2 = unknown; 1 = should allow; 0 = none.
- **EX081 — Approval record.** What must be stored with an approved OT firewall push? *Rubric:* 3 = approver, time, object/rule version, reason; 2 = two; 1 = none; 0 = none.

### Synthesis

Encode TLP as a gate, fail closed, require approval for high-impact actions and log every decision.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Threat intelligence and OSINT: implementation I

### Learning outcomes

You will (1) implement a TAXII 2.1 client stage against a synthetic server stub; (2) implement validation and normalisation stages; (3) wire stages with bounded queues; (4) produce operator-visible metrics from the first release.

### 28.1 Client stage

The client discovers the API root, lists permitted collections, and requests objects added after the last saved checkpoint. It follows pagination until complete and stores the new checkpoint only after the batch is safely written, so a crash causes a re-fetch rather than a gap.

### 28.2 Validation and normalisation

Validation enforces STIX required properties and identifier format. Normalisation applies the documented rules from Chapter 13. Both stages emit rejects with reasons.

### 28.3 Queues

Bounded queues connect stages. If enrichment slows, validation fills its output queue and waits; the client pauses. This protects memory and makes slowness visible.

### 28.4 Metrics from day one

Objects received, accepted, rejected per source; queue depths; checkpoint age; poll duration. Metrics are cheap to add early and expensive to retrofit.

### 28.5 Synthetic server stub

Development uses a local stub that serves synthetic STIX bundles in TAXII 2.1 form. No development traffic touches partner servers, protecting partners and keeping tests reproducible.

### Configuration of partners

Each partner entry in configuration names the API root, collections, polling interval, credential reference and data contact. Adding a partner is a reviewed configuration change, not a code change, which keeps the client stage generic and makes the partner list itself auditable. Removing a partner follows the retirement steps from Chapter 16.

### Worked example

On the first test run the client saved its checkpoint before writing the batch; a forced crash then lost 200 objects. Kofi reorders the steps — write, then checkpoint — and adds a test that crashes between them and verifies no loss.

> **Synthetic case.** The bug and counts are invented.

### Errors and limits

Exactly-once delivery is hard; design for at-least-once plus idempotent writes. Testing against live partner servers is not acceptable for development.

### Exercises

- **EX082 — Checkpoint order.** Why must the checkpoint be saved after the batch is written? *Rubric:* 3 = otherwise crash loses objects; re-fetch is safe with idempotent writes; 2 = partial; 1 = order irrelevant; 0 = none.
- **EX083 — Stub reason.** Give two reasons to develop against a synthetic TAXII stub. *Rubric:* 3 = no load/risk to partners + reproducible tests; 2 = one; 1 = faster only; 0 = none.
- **EX084 — Early metric.** Which metric reveals a stalled collector, and why? *Rubric:* 3 = checkpoint age / objects received per source; rises or drops to zero when stalled; 2 = metric only; 1 = CPU; 0 = none.

### Synthesis

Checkpoint after writing, validate and normalise with rejects, bound the queues, and ship metrics with the first release.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Threat intelligence and OSINT: measurement

### Learning outcomes

You will (1) measure feed quality with precision, recall and F1 against a labelled set; (2) build a labelled evaluation set ethically; (3) measure timeliness and uniqueness; (4) report metrics with their limits.

### 29.1 Labelled sets

To measure a feed, compare it with ground truth: indicators confirmed malicious in BEN's incidents or in trusted partner investigations, plus confirmed benign values. Labels come from completed investigations, not from the feed itself, to avoid circularity.

### Lab 6 — feed evaluation

```python
"""Lab 6 (ch 29): precision and recall of a synthetic feed against a labelled ground-truth set."""
truth_bad = {"a.example", "b.example", "c.example", "d.example", "e.example"}
feed = {"a.example", "b.example", "c.example", "x.example", "y.example", "z.example"}
tp = len(feed & truth_bad); fp = len(feed - truth_bad); fn = len(truth_bad - feed)
p, r = tp / (tp + fp), tp / (tp + fn)
print(f"TP={tp} FP={fp} FN={fn}")
print(f"precision={p:.2f} recall={r:.2f} F1={2*p*r/(p+r):.2f}")
```

Run with `python3 lab_feedeval.py`. Verified output:

```text
TP=3 FP=3 FN=2
precision=0.50 recall=0.60 F1=0.55
```

### 29.2 Reading the scores

Three of the feed's six entries are confirmed malicious (precision 0.50); it found three of five known malicious values (recall 0.60); F1 is 0.55. Half the feed would be noise if blocked directly.

### 29.3 Timeliness and uniqueness

A feed that lists indicators a week after BEN saw them is of little operational value. Measure median lead time relative to first internal sighting. Uniqueness — indicators no other source provides — shows marginal value.

### 29.4 Limits

Ground truth is incomplete: unknown malicious values count as false positives when they are merely unconfirmed. Report the evaluation period, set size and labelling method with every number.

### 29.5 Using results

Metrics feed source weights in Lantern's confidence model and inform renewal decisions for paid feeds. They are shared with partners in aggregate when agreements allow, supporting the reciprocity NIST SP 800-150 describes.

### Sampling for labels

Labelling every indicator is impossible. Kofi draws a random sample stratified by indicator type, labels it from investigation records, and reports confidence intervals. A sample of a few hundred, honestly drawn, beats an enormous convenience sample of whatever happened to be investigated.

### Worked example

Kofi evaluates a paid feed over a quarter: precision 0.50, recall 0.60, median lead time −2 days (it lags internal sightings). He recommends keeping it as an enrichment source only and not renewing the premium tier.

> **Synthetic case.** Feed values are invented.

### Errors and limits

Small labelled sets give unstable estimates. Do not publish named-vendor scores from licensed data.

### Exercises

- **EX085 — Score quote.** Quote precision, recall and F1 from the lab. *Rubric:* 3 = 0.50, 0.60, 0.55; 2 = two; 1 = one; 0 = none.
- **EX086 — Circular label.** Why must labels not come from the feed being evaluated? *Rubric:* 3 = circularity inflates precision; 2 = bias vaguely; 1 = fine; 0 = none.
- **EX087 — Negative lead time.** What does a median lead time of −2 days mean operationally? *Rubric:* 3 = feed lags internal detection; low preventive value; 2 = late; 1 = early; 0 = none.

### Synthesis

Measure against independent labels, add timeliness and uniqueness, and report every metric with its limits.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) write verification procedures that trace to requirements; (2) execute them on synthetic data; (3) record pass, fail and deviation results; (4) distinguish verification ("built right") from validation ("right thing").

### 30.1 Verification versus validation

Verification checks that Lantern meets its written requirements. Validation, in Chapter 38, checks that it meets stakeholders' real needs. A platform can pass verification and still fail validation if the requirements were wrong.

### 30.2 Procedures

Each procedure names the requirement, preconditions, steps, expected result and pass criteria. "Load bundle S-07 containing 1,000 indicators of which 12 lack valid_from; expect 988 stored, 12 rejected with reason; pass if counts match exactly."

### 30.3 Coverage

The traceability matrix shows which requirements have procedures. Uncovered requirements are listed explicitly; an untested requirement is an open risk, not a silent pass.

### 30.4 Deviations

When a result differs, record a deviation with severity and owner. Do not edit the expected result to match the output without a requirement change.

### 30.5 Evidence

Logs, metric snapshots and output hashes are stored with the procedure run. A reviewer can rerun the same procedure with the same synthetic data and compare hashes.

### Regression suite

Passed procedures become automated regression tests run on every change. The suite grows with each defect fixed, so the same mistake cannot quietly return. Kofi tags each test with its requirement ID, which keeps the traceability matrix current without manual effort and shows at a glance which requirements lost coverage when a test was removed.

### Worked example

Kofi runs 42 procedures. 38 pass, 3 fail (TLP gate allowed a label with trailing space; reject reason missing for one error type; checkpoint metric not exported), and 1 is blocked by a missing test fixture. Each failure becomes a defect with an owner; the blocked one is scheduled.

> **Synthetic case.** Counts and defects are invented.

### Errors and limits

A green test run on synthetic data does not prove robustness on every partner format; extend fixtures as formats are seen. Do not count blocked procedures as passes.

### Exercises

- **EX088 — V and V.** In one sentence each, define verification and validation. *Rubric:* 3 = built to requirements; meets real needs; 2 = one; 1 = swapped; 0 = none.
- **EX089 — Trailing space.** Why is a TLP gate accepting "TLP:AMBER " (with a space) a defect? *Rubric:* 3 = inconsistent label handling; should normalise or fail closed per requirement; 2 = partial; 1 = harmless; 0 = none.
- **EX090 — Blocked count.** How should the one blocked procedure be reported? *Rubric:* 3 = separately as blocked/not executed with plan; not a pass; 2 = not passed; 1 = pass; 0 = none.

### Synthesis

Verify against written requirements with traceable procedures, record deviations honestly and keep evidence rerunnable.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Threat intelligence and OSINT: implementation II

### Learning outcomes

You will (1) implement enrichment with caching and provider-terms compliance; (2) implement sighting ingestion from internal telemetry; (3) compute decayed confidence on read; (4) publish analyst-approved objects back to partners.

### 31.1 Enrichment

Enrichment adds context: internal asset ownership for an address, passive DNS history for a domain, ATT&CK technique links for a malware family. External enrichment providers have terms on query volume, retention and redistribution. Lantern's enricher records which provider supplied each field so that redistribution rules can be enforced at export.

### 31.2 Sightings

When BEN's DNS resolver or proxy sees an indicator, Lantern records a STIX 2.1 sighting object referencing the indicator, with first and last seen times and a count. Sightings raise confidence and give partners valuable feedback when shared under agreement.

### 31.3 Confidence on read

Rather than rewriting every record nightly, Lantern stores c₀ and the last-sighting time and computes decayed confidence when queried. This avoids mass updates and keeps the model change in one function.

### 31.4 Publishing

Analysts approve objects for sharing with a TLP marking. The publisher strips enrichment fields whose provider forbids redistribution, signs the bundle and adds it to the community TAXII collection.

### 31.5 Personal data in telemetry

Sightings come from systems that know which employee's machine made a request. Lantern stores the asset identifier, not the person, and shares only aggregate counts outward.

### Practice note — rollout

New stages roll out behind a feature flag to a fraction of traffic first. Kofi compares metrics between flagged and unflagged paths for a week before full rollout.

### Worked example

A partner asks for sightings of their indicators. Lantern exports sighting objects with counts and time ranges but without internal hostnames or user names, marked TLP:AMBER per the partner agreement. The partner reports that two of their indicators had no sightings across the community and retires them.

> **Synthetic case.** The exchange is invented.

### Errors and limits

Redistributing licensed enrichment can breach contracts. Sightings can reveal a member's exposure; share only as agreed.

### Exercises

- **EX091 — Provider field.** Why record the provider of each enrichment field? *Rubric:* 3 = enforce redistribution/retention terms at export; 2 = audit; 1 = no reason; 0 = none.
- **EX092 — Sighting contents.** What does Lantern share in sighting objects, and what does it remove? *Rubric:* 3 = counts/time ranges/indicator ref; removes hostnames/users; 2 = one half; 1 = everything; 0 = none.
- **EX093 — Compute on read.** Give one advantage of computing decayed confidence on read. *Rubric:* 3 = no mass nightly rewrites/single model function; 2 = vague efficiency; 1 = none; 0 = none.

### Synthesis

Enrich within provider terms, record sightings without people, compute decay on read, and publish only what may be shared.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Threat intelligence and OSINT: reliability

### Learning outcomes

You will (1) compute availability of serial pipelines; (2) quantify the effect of redundancy; (3) set service-level objectives with error budgets; (4) decide where reliability investment pays off.

### 32.1 Serial availability

A request that must pass through every stage succeeds only if all stages are up, so availabilities multiply. Four stages that each look good can combine into something mediocre.

### Lab 7 — availability

```python
"""Lab 7 (ch 32): availability of a synthetic CTI pipeline - serial stages and a redundant pair."""
stages = {"taxii-poll": 0.995, "parser": 0.999, "enrich": 0.98, "store": 0.999}
serial = 1.0
for a in stages.values():
    serial *= a
print(f"serial availability={serial:.4f} (~{(1-serial)*8760:.0f} h/yr down)")
enrich_pair = 1 - (1 - stages["enrich"]) ** 2
improved = serial / stages["enrich"] * enrich_pair
print(f"with redundant enrich: {improved:.4f} (~{(1-improved)*8760:.0f} h/yr down)")
```

Run with `python3 lab_avail.py`. Verified output:

```text
serial availability=0.9732 (~235 h/yr down)
with redundant enrich: 0.9926 (~65 h/yr down)
```

### 32.2 Reading the lab

The serial pipeline reaches 0.9732, roughly 235 hours of downtime a year — dominated by enrichment at 0.98. Duplicating enrichment (two independent instances, either can serve) lifts the pipeline to 0.9926, about 65 hours a year. Investing in the weakest stage gives the largest gain.

### 32.3 Independence assumption

The redundancy formula assumes failures are independent. Two enrichment workers on the same host, or calling the same external provider, fail together. Real redundancy needs diverse hosts and, where possible, alternate providers.

### 32.4 SLOs and error budgets

An SLO such as "99.5% of polls succeed each month" defines an error budget of 0.5%. When the budget is spent, feature work pauses and reliability work takes priority.

### 32.5 Graceful degradation

If enrichment fails, Lantern should still store and match indicators, marking them "unenriched", rather than stopping ingestion. Degraded service beats no service in a SOC.

### Measuring what users feel

Uptime of each process is not what analysts experience. Kofi adds a synthetic probe that injects a test indicator every fifteen minutes and checks it reaches the DNS policy. The probe's success rate is the availability users actually feel, and it catches failures between components that per-process health checks miss.

### Worked example

Kofi proposes a second enrichment instance on a different host and a fallback mode that skips external enrichment when the provider is down. The measured monthly availability rises from 97.4% to 99.2% over the next quarter.

> **Synthetic case.** Figures are illustrative.

### Errors and limits

Availability numbers hide partial failures such as slow responses. Measure latency SLOs too.

### Exercises

- **EX094 — Serial result.** Quote the lab's serial availability and approximate yearly downtime. *Rubric:* 3 = 0.9732, ~235 h; 2 = one; 1 = wrong; 0 = none.
- **EX095 — Hidden dependency.** Why might two enrichment workers not be independent? *Rubric:* 3 = shared host/provider/network → common-mode failure; 2 = vague; 1 = always independent; 0 = none.
- **EX096 — Degraded mode.** What should Lantern do when external enrichment is unavailable? *Rubric:* 3 = continue ingestion/matching; mark unenriched; retry later; 2 = continue; 1 = stop pipeline; 0 = none.

### Synthesis

Multiply serial availabilities, fix the weakest stage with truly independent redundancy, manage error budgets and degrade gracefully.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Threat intelligence and OSINT: safety and resilience

### Learning outcomes

You will (1) analyse how CTI outputs could harm operational technology; (2) design safety interlocks for automated actions; (3) plan resilience against loss of feeds or partners; (4) rehearse safe rollback.

### 33.1 How intelligence can hurt operations

An over-broad block on an OT firewall could cut a SCADA master from remote terminal units, removing visibility of the grid. A mistaken "malicious" tag on a vendor update server could block a safety-relevant patch. In critical infrastructure, false positives have physical consequences.

### 33.2 Interlocks

Lantern applies interlocks: no automatic action on OT segments; an allow-list of protected operational addresses that no block may include; a maximum change size per push; and two-person approval for any OT rule. These mirror safety engineering's idea that one failure should not cause harm.

### 33.3 Resilience to source loss

If a key partner stops sharing, detection should degrade gracefully. Diverse sources, internal telemetry analytics and behaviour-based detections mapped to ATT&CK reduce dependence on any single feed.

### 33.4 Rollback

Every push records the previous rule set. A tested one-command rollback restores it within minutes. Rollback drills run quarterly in the test environment.

### 33.5 Coordinating with operations

OT engineers own operational decisions. Lantern provides advice and evidence; it does not override operations.

### Practice note — safety cases

A short safety argument states the hazard, the interlocks that prevent it and the evidence each interlock works. Reviewers can then challenge a specific link rather than the whole design.

### After an override

Whenever an engineer overrides an interlock, the next working day includes a short review of why, whether the interlock was wrong, and whether the rule should change.

### Worked example

A partner tags the address of BEN's relay vendor's update server as malicious after a compromise elsewhere. The protected-address interlock blocks the automatic push; OT engineers review, confirm the vendor's server is clean for BEN's region, and record the decision.

> **Synthetic case.** The vendor and tag are invented.

### Errors and limits

Interlocks can be bypassed under pressure; audit every override. Safety analysis must involve OT engineers.

### Exercises

- **EX097 — Physical harm.** Give one way an IT-style block could cause operational harm in a grid. *Rubric:* 3 = specific mechanism (cut SCADA visibility, block safety patch); 2 = vague; 1 = none; 0 = none.
- **EX098 — Interlock list.** Name three interlocks Lantern applies to OT actions. *Rubric:* 3 = three of no auto OT/protected allow-list/max change size/two-person approval; 2 = two; 1 = one; 0 = none.
- **EX099 — Source loss.** How does ATT&CK-mapped behavioural detection help when a feed disappears? *Rubric:* 3 = detects techniques independent of feed indicators; 2 = partial; 1 = no help; 0 = none.

### Synthesis

Treat false positives as physical risks, interlock automated actions, diversify sources and drill rollback.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Threat intelligence and OSINT: integration

### Learning outcomes

You will (1) integrate Lantern with SIEM, DNS, proxy and ticketing systems; (2) design idempotent integrations; (3) map Lantern objects to downstream formats; (4) test integrations end to end.

### 34.1 Integration targets

SIEM: indicators become correlation lookups; sightings flow back. DNS resolver: domain blocks and response-policy zones. Web proxy: URL categories. Ticketing: high-confidence matches open tickets with Diamond and ATT&CK context.

### 34.2 Idempotence

Re-sending the same block list must not duplicate rules. Integrations compare desired state with current state and apply differences only. That also makes rollback a matter of re-applying the previous desired state.

### 34.3 Mapping formats

STIX patterns such as `[domain-name:value = 'c2.example']` translate into each product's rule syntax. Unsupported pattern features are rejected with a reason rather than approximated.

### 34.4 Context in tickets

A ticket that says "match on drop.example" is weak. A ticket that adds source, confidence, TLP, related ATT&CK techniques and recommended actions lets analysts act quickly.

### 34.5 End-to-end tests

A synthetic indicator is injected at the collector; the test checks that it appears in the DNS policy, triggers a SIEM lookup on a synthetic query, and opens a ticket — then removes it and checks cleanup.

### Practice note — owners

Each integration has a named owner on the downstream team. When the DNS team upgrades its resolver, they know to run Lantern's integration test.

### Version drift

Downstream products change their APIs. Lantern pins the API version it uses for each integration and runs the end-to-end test in the downstream team's staging environment before they upgrade, so changes surface before production.

### Worked example

The proxy integration duplicated 3,000 rules after a retry. Kofi changes it to a state comparison; repeated pushes now report "0 changes", and the proxy team confirms rule counts match Lantern's desired state.

> **Synthetic case.** The duplication incident is invented.

### Errors and limits

Downstream products have rule-count limits; prioritise by confidence. Approximating unsupported patterns creates silent gaps.

### Exercises

- **EX100 — Idempotent push.** Describe how an idempotent block-list integration works. *Rubric:* 3 = compare desired vs current, apply diff only; repeat yields no change; 2 = partial; 1 = resend all; 0 = none.
- **EX101 — Ticket context.** List four context fields for a match ticket. *Rubric:* 3 = four of source, confidence, TLP, ATT&CK, recommended action, Diamond fields; 2 = two; 1 = indicator only; 0 = none.
- **EX102 — Unsupported pattern.** What should happen to a STIX pattern the proxy cannot express? *Rubric:* 3 = reject with reason/route elsewhere; never approximate silently; 2 = reject; 1 = approximate; 0 = none.

### Synthesis

Integrate by desired state, translate patterns exactly, enrich tickets with context and test the whole path.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design Lantern's analysis and dissemination layer; (2) produce product templates for different consumers; (3) defend design choices against an adversarial reviewer; (4) estimate effort and risks for the build.

### 35.1 Brief

Design how analysts turn stored objects into products: a daily tactical digest, a weekly operational summary and a quarterly strategic brief for executives, each with TLP controls, ICD 203-style judgment language and feedback capture.

### 35.2 Templates

Tactical digest: top indicators by confidence, actions taken, sightings. Operational summary: active campaigns with Diamond structure and ATT&CK techniques. Strategic brief: adversary trends relevant to electricity distribution, key judgments with estimative words and a published probability scale.

### 35.3 Adversarial review

A reviewer plays a sceptical executive: "Why should I trust this?" The design answers with source descriptions, confidence, and a track record of past judgments.

### 35.4 Effort and risk

The team estimates effort per component and lists risks: analyst time to write strategic briefs, partner consent to quote, executive attention.

### 35.5 Accessibility

Products are readable on mobile, avoid colour-only coding (TLP labels are written in text, as TLP 2.0 recommends) and include alt text for figures.

### Practice note — fewer, better products

Studio teams often propose a dozen product types. The panel pushes back: three products that are read beat twelve that are ignored.

### Measuring readership

Each product records opens and feedback clicks. After a quarter the team retires any product that nobody reads and asks its intended audience what they need instead.

### Worked example

Kofi's strategic brief template opens with three key judgments, each with an estimative phrase mapped to a range, the basis for the judgment and what would change it. The sceptical reviewer accepts the template after seeing that past judgments are tracked for accuracy.

> **Synthetic case.** The template review is invented.

### Errors and limits

Templates can become boilerplate; reviewers should check that each product says something new. Strategic products need analyst time, not just automation.

### Exercises

- **EX103 — Three products.** Match tactical, operational and strategic products to their main audience. *Rubric:* 3 = SOC analysts; IR/hunt leads; executives; 2 = two; 1 = one; 0 = none.
- **EX104 — Trust answer.** Give two design features that answer "why should I trust this?" *Rubric:* 3 = two of source description, confidence/estimative scale, track record, change triggers; 2 = one; 1 = branding; 0 = none.
- **EX105 — Colour-only.** Why should TLP labels be written in text rather than shown only by colour? *Rubric:* 3 = accessibility/colour blindness/printing; TLP 2.0 guidance; 2 = accessibility; 1 = no reason; 0 = none.

### Synthesis

Design few products for named audiences, make trust visible, plan effort honestly and keep products accessible.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Threat intelligence and OSINT: performance and scale

### Learning outcomes

You will (1) detect unstable queues where arrival exceeds service; (2) apply Little's law to estimate waiting time; (3) choose between scaling up, scaling out and shedding load; (4) protect partners when Lantern scales.

### 36.1 Unstable queues

If 120 objects per minute arrive at enrichment and only 100 per minute are served, the backlog grows by 20 each minute without limit. No amount of waiting fixes this; capacity or demand must change.

### Lab 8 — queue growth

```python
"""Lab 8 (ch 36): Little's law and backlog growth for a synthetic enrichment queue."""
arrival_per_min, service_per_min = 120, 100
backlog = 0
for minute in range(1, 6):
    backlog += arrival_per_min - service_per_min
    print(f"minute {minute}: backlog={backlog}")
L, lam = 400, 100 / 60  # items in system, throughput items/s after scaling fixes
print(f"Little's law wait W=L/lambda={L/lam:.0f} s at L={L}, lambda={lam:.2f}/s")
```

Run with `python3 lab_queue.py`. Verified output:

```text
minute 1: backlog=20
minute 2: backlog=40
minute 3: backlog=60
minute 4: backlog=80
minute 5: backlog=100
Little's law wait W=L/lambda=240 s at L=400, lambda=1.67/s
```

### 36.2 Little's law

For a stable system, the average number in the system L equals throughput λ times average time in system W. With 400 items queued and 1.67 items per second served, average wait is about 240 seconds. The law needs no assumptions about arrival patterns, which makes it a robust check on dashboards.

### 36.3 Options

Scale up (faster hardware), scale out (more workers), or shed load (skip low-value enrichment, sample low-confidence indicators). Shedding by value is often cheapest: enrich high-confidence indicators first.

### 36.4 Protecting partners

Scaling out collectors must not multiply load on partner TAXII servers. Lantern keeps one polling identity per partner and shares results internally, respecting partner rate limits.

### 36.5 Testing at scale

Load tests use synthetic bundles generated to realistic sizes, run against the TAXII stub and internal components only.

### Practice note — priority queues

Two queues — high and low confidence — with workers serving high first keep important enrichment fast during bursts while low-value work waits or is skipped.

### Capacity reviews

Every quarter Kofi compares peak arrival rates with service capacity and records the headroom percentage, so growth is planned before queues become unstable.

### Worked example

During a large campaign, arrivals jump to 120 per minute. Kofi adds two workers (service 150 per minute) and switches low-confidence indicators to a deferred queue. The backlog drains in under ten minutes, and partner polling stays unchanged.

> **Synthetic case.** Rates are invented.

### Errors and limits

Little's law describes averages; tail latency needs percentiles. Scaling the consumer of a rate-limited external provider just produces more 429 responses.

### Exercises

- **EX106 — Backlog after five.** What backlog does the lab show after five minutes, and why does it keep growing? *Rubric:* 3 = 100; arrival exceeds service by 20/min; 2 = number only; 1 = stable; 0 = none.
- **EX107 — Little's law.** Compute W for L = 300 items at λ = 2 items per second. *Rubric:* 3 = 150 s; 2 = method; 1 = 600; 0 = none.
- **EX108 — Partner load.** Why must scaling out collectors not add polling identities per partner? *Rubric:* 3 = would multiply partner load/breach rate limits; 2 = partial; 1 = fine; 0 = none.

### Synthesis

Spot instability, use Little's law for waits, scale or shed by value, and keep partners' load constant.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Threat intelligence and OSINT: operations

### Learning outcomes

You will (1) write runbooks for routine and abnormal Lantern operations; (2) define on-call responsibilities; (3) handle partner incidents such as leaked or retracted data; (4) report operational metrics to management.

### 37.1 Runbooks

Routine: daily review of collector health, reject spikes and certificate expiry. Abnormal: partner feed stops; poisoned indicators detected; enrichment provider outage; TLP breach suspected. Each runbook lists symptoms, checks, actions, escalation and closure steps.

### 37.2 On-call

One engineer is on call per week with a documented handover. Pages fire only for conditions needing action within an hour; everything else goes to a daily queue. Alert fatigue is a reliability risk.

### 37.3 Retractions

Partners sometimes retract indicators published in error. Lantern must remove them from enforcement promptly, record the retraction and inform downstream recipients who received them. STIX 2.1 supports revocation through the `revoked` property on a new object version.

### 37.4 Suspected TLP breach

If restricted content appears where it should not, the runbook says: contain (remove access), assess what was exposed, notify the originator as the agreement requires, and review the gate. Honesty with partners protects the relationship that NIST SP 800-150 describes as the basis of sharing.

### 37.5 Reporting

Monthly: availability against SLO, objects processed, reject rates, time-to-enforcement percentiles, false-positive tickets, partner feedback sent and received.

### Practice note — blameless reviews

After incidents, reviews focus on how the system allowed the error. Engineers who fear blame hide near-misses, which removes the data needed to improve.

### Handover notes

Each on-call week ends with a written handover listing open issues, partner contacts engaged and anything unusual, so the next engineer does not rediscover context during a page.

### Worked example

A partner revokes 40 indicators published by mistake. Lantern processes the revoked versions within 12 minutes, removes the blocks and forwards revocations to the two community members that received them. The monthly report records the event and time to revoke.

> **Synthetic case.** The retraction is invented.

### Errors and limits

Runbooks rot; test them in drills. Paging for everything ensures nothing is noticed.

### Exercises

- **EX109 — Revocation mechanism.** How does STIX 2.1 signal that an object is withdrawn? *Rubric:* 3 = new version with revoked: true; 2 = revoked mentioned; 1 = delete silently; 0 = none.
- **EX110 — Breach steps.** List the four runbook steps for a suspected TLP breach. *Rubric:* 3 = contain, assess, notify originator, review gate; 2 = three; 1 = one; 0 = none.
- **EX111 — Page threshold.** Which conditions should page the on-call engineer? *Rubric:* 3 = those needing action within an hour; others to daily queue; 2 = urgent ones vaguely; 1 = all alerts; 0 = none.

### Synthesis

Runbooks for routine and abnormal work, humane on-call, prompt revocation, honest breach handling and regular metrics.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Threat intelligence and OSINT: validation

### Learning outcomes

You will (1) validate Lantern against stakeholders' real needs; (2) design acceptance scenarios with operators; (3) measure decision impact, not only system metrics; (4) handle findings that requirements were wrong.

### 38.1 Validation questions

Does the SOC block threats sooner? Do OT engineers get vendor warnings they act on? Do executives understand strategic briefs? These questions concern outcomes; system metrics alone cannot answer them.

### 38.2 Acceptance scenarios

With operators, Kofi writes scenarios: "A partner shares a phishing campaign against utilities at 09:00; by 09:30 domain blocks are active, a ticket with ATT&CK context exists and the duty analyst has hunted for prior contacts." Scenarios run on synthetic data in a staging environment that mirrors production.

### 38.3 Decision impact

Measure before and after Lantern: median time from external publication to enforcement; percentage of incidents where intelligence context was available at triage; executive decisions that referenced a strategic brief. Some measures are rough; report them with their limits.

### 38.4 When requirements were wrong

Validation may show that a verified requirement serves no one — for example, a daily digest nobody reads. That is a valuable finding: change the requirement, not the measurement.

### 38.5 Independent observers

Someone outside the build team observes scenario runs and interviews users, reducing the temptation to declare success.

### Practice note — negative results

If a scenario shows Lantern adds nothing to a decision, record it plainly. Negative validation results justify retiring features and save maintenance effort.

### Feedback loop

Validation findings are scheduled into the next release plan with owners, and the scenario is rerun after the change to confirm the outcome improved.

### Worked example

Median time from partner publication to DNS enforcement fell from 9 hours (manual process) to 25 minutes. But OT engineers reported vendor alerts arrived in an inbox they rarely check. The requirement is changed to deliver vendor alerts to the OT team's ticket queue.

> **Synthetic case.** Figures are invented.

### Errors and limits

Before-and-after comparisons can be confounded by other changes; note concurrent changes. Users' praise is not measurement.

### Exercises

- **EX112 — Outcome question.** Write one validation question about Lantern that a system metric cannot answer alone. *Rubric:* 3 = outcome/decision-focused question; 2 = mixed; 1 = system metric; 0 = none.
- **EX113 — Wrong requirement.** What should happen to the vendor-alert delivery requirement? *Rubric:* 3 = change to OT ticket queue based on validation; 2 = change vaguely; 1 = keep inbox; 0 = none.
- **EX114 — Confounded gain.** Name one concurrent change that could confound the 9 h → 25 min improvement. *Rubric:* 3 = plausible concurrent change (new staff, new DNS product, policy change); 2 = vague; 1 = none possible; 0 = none.

### Synthesis

Validate outcomes with operators, measure decisions, accept that requirements can be wrong, and use independent observers.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Threat intelligence and OSINT: maintainability

### Learning outcomes

You will (1) measure and reduce maintenance burden; (2) document Lantern for successors; (3) manage technical debt explicitly; (4) plan for standards evolution (STIX/TAXII versions, ATT&CK releases).

### 39.1 Maintenance burden

Track hours spent on partner format changes, dependency updates, incident fixes and analyst requests. If maintenance consumes most of the team's time, new features should wait.

### 39.2 Documentation for successors

Architecture overview, ADRs, runbooks, partner configuration guide, data dictionary and a "first week" guide. Kofi tests documentation by asking a new engineer to add a synthetic partner using only the docs.

### 39.3 Technical debt register

Each shortcut is recorded with its cost, risk and a target date: "Proxy integration uses polling instead of the vendor's push API; risk low; revisit Q3". Debt hidden in code comments is forgotten.

### 39.4 Standards evolution

ATT&CK publishes new versions periodically, renaming or deprecating techniques. Lantern stores the ATT&CK version alongside each mapping and runs a migration report when a new version appears. STIX and TAXII versions are tracked similarly; supporting 2.1 does not guarantee compatibility with a future version.

### 39.5 Simplicity

The simplest design that meets requirements is easiest to maintain. Remove unused features found during validation.

### Practice note — bus factor

If only one person understands the firewall push, Lantern has a bus factor of one. Pairing and rotation spread knowledge.

### Deprecation policy

Features unused for two quarters are announced as deprecated, given a removal date and then deleted, with partners told when an export format is affected.

### Worked example

The new engineer adds a synthetic partner in 90 minutes using the guide, noting two unclear steps. Kofi fixes the guide. Separately, an ATT&CK update deprecates a technique used in 14 mappings; the migration report lists them and analysts remap them in an afternoon.

> **Synthetic case.** Timings and counts are invented.

### Errors and limits

Documentation that describes intentions rather than reality misleads. Pinning ATT&CK versions forever leaves mappings outdated.

### Exercises

- **EX115 — Docs test.** How did Kofi test documentation quality? *Rubric:* 3 = new engineer adds synthetic partner using only docs; gaps fixed; 2 = review by peer; 1 = none; 0 = none.
- **EX116 — Debt entry.** Write a technical-debt register entry for a hard-coded polling interval. *Rubric:* 3 = description, cost/risk, target date; 2 = two parts; 1 = comment only; 0 = none.
- **EX117 — ATT&CK version.** Why store the ATT&CK version with each mapping? *Rubric:* 3 = techniques change/deprecate; enables migration report; 2 = partial; 1 = unnecessary; 0 = none.

### Synthesis

Measure maintenance, document for strangers, register debt, track standards versions and keep designs simple.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify non-functional requirements — performance, availability, security; (2) run fault-injection tests safely; (3) verify TLP and privacy controls with negative tests; (4) compile a verification report.

### 40.1 Non-functional verification

Performance: inject synthetic bundles at 150% of peak rate and verify time-to-enforcement percentiles. Availability: kill one enrichment instance and verify continued service. Security: attempt restricted exports with test accounts lacking permission.

### 40.2 Fault injection

Faults are injected in staging: partner stub returns errors, clock skew is introduced, storage fills up. Each test states the expected degraded behaviour and verifies it. Fault injection never targets production or partner systems.

### 40.3 Negative tests for controls

Try to export a RED report to a non-named recipient; try to push an OT rule without approval; try to store a personal social-media profile via the OSINT module. Every attempt must fail and be logged.

### 40.4 Verification report

Summary of procedures executed, passes, failures, deviations, blocked items, open defects with severity and owners, and residual risks. The report goes to the design review in Chapter 45.

### 40.5 Re-verification

After fixes, failed procedures rerun, and the regression suite runs in full.

### Practice note — evidence packaging

Each procedure's logs and outputs are hashed and stored with the report, so reviewers can check that the evidence matches what the report claims.

### Residual risk

The report closes with risks that verification could not address, such as behaviour on partner formats never seen in testing, so reviewers weigh them explicitly rather than assuming coverage. Each residual risk names an owner and a monitoring approach.

### Worked example

At 150% load, p95 time-to-enforcement is 22 minutes against a 30-minute requirement: pass. The clock-skew test shows sightings timestamps off by five minutes: fail; NTP monitoring is added. All six negative control tests block and log correctly.

> **Synthetic case.** Results are invented.

### Errors and limits

Staging differs from production; record differences. Passing negative tests shows these attacks fail, not that no attack succeeds.

### Exercises

- **EX118 — Negative test.** Write one negative test for the OSINT privacy requirement. *Rubric:* 3 = attempt to store personal profile → expect rejection + log; 2 = test without expected result; 1 = positive test; 0 = none.
- **EX119 — Load verdict.** p95 is 22 min against a 30-min requirement. Verdict and reason? *Rubric:* 3 = pass; 22 ≤ 30 at stated percentile; 2 = pass; 1 = fail; 0 = none.
- **EX120 — Injection target.** Where may fault injection run, and where must it never run? *Rubric:* 3 = staging/synthetic stubs; never production or partner systems; 2 = one half; 1 = production; 0 = none.

### Synthesis

Verify performance, availability and controls with load, faults and negative tests in staging, and package evidence.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Threat intelligence and OSINT: system optimization

### Learning outcomes

You will (1) optimise Lantern for the outcome that matters — timely, accurate enforcement; (2) identify the binding constraint across people and machines; (3) evaluate optimisations with before-and-after measurement; (4) avoid optimising proxies that harm outcomes.

### 41.1 Outcome first

The target outcome is fewer successful attacks reaching BEN, approximated by time-to-enforcement for high-confidence indicators and the share of incidents with intelligence context at triage. Optimising "objects ingested per day" can make outcomes worse by flooding analysts.

### 41.2 Binding constraint

Often the slowest step is human: analyst approval for sharing, OT engineer review. Faster machines do not help if approvals wait overnight. Optimisation may mean better prioritisation of approval queues rather than new hardware.

### 41.3 Candidate optimisations

Pre-filter low-value indicators before enrichment; prioritise approval queues by confidence and asset criticality; batch firewall pushes on a fixed cadence; reduce duplicate sources whose uniqueness measured near zero.

### 41.4 Measuring the effect

Each change has a hypothesis, a metric and a comparison window. If the metric does not move, the change is reverted to avoid complexity without benefit.

### 41.5 Goodhart's warning

When a measure becomes a target, people game it. If analysts are judged on approvals per hour, they may approve poorly. Keep quality checks beside speed metrics.

### Practice note — removing work

The best optimisation is often deletion: dropping a feed that adds nothing unique removes ingestion, storage and analyst noise at once.

### Cost of complexity

Every optimisation adds code or process to maintain. Kofi estimates the yearly maintenance hours of each change and compares them with the hours it saves analysts.

### Worked example

Analyst approval of indicators for sharing has a median wait of 6 hours. Kofi sorts the queue by confidence and partner demand and adds a daily 30-minute approval slot. Median wait falls to 1.5 hours; a spot check shows no rise in later retractions.

> **Synthetic case.** Figures are invented.

### Errors and limits

Local optimisations can move bottlenecks elsewhere; re-measure the whole path. Some delays are deliberate safety controls and must not be optimised away.

### Exercises

- **EX121 — Proxy trap.** Why can maximising objects ingested per day harm outcomes? *Rubric:* 3 = more noise/analyst overload/lower precision; 2 = partial; 1 = always good; 0 = none.
- **EX122 — Quality check.** What quality check accompanied the approval-speed improvement? *Rubric:* 3 = spot check showed no rise in retractions; 2 = some check; 1 = none; 0 = none.
- **EX123 — Deliberate delay.** Name one delay in Lantern that must not be optimised away. *Rubric:* 3 = OT two-person approval (or similar safety gate) with reason; 2 = name only; 1 = none; 0 = none.

### Synthesis

Optimise outcomes, find the real constraint, measure every change, guard against Goodhart and keep safety delays.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Threat intelligence and OSINT: applied research

### Learning outcomes

You will (1) frame an engineering research question from Lantern's operational data; (2) design a study that uses synthetic or consented data; (3) evaluate results statistically with appropriate humility; (4) report findings for practitioners and researchers.

### 42.1 Questions from operations

Lantern's logs suggest questions: Does indicator half-life differ by sector partner? Does behaviour-based detection catch incidents that indicator matching misses? How much do sightings shared with partners improve their retirement decisions?

### 42.2 Data and consent

Internal operational data may be used for improvement under BEN's policies; partner data needs partner consent for research use and publication. Personal data is excluded. Where consent is lacking, synthetic data that reproduce statistical properties can test methods but not prove facts about the real world.

### 42.3 Method

Kofi studies half-lives: for each retired indicator, did it reappear in sightings within 60 days? He fits re-observation rates by indicator type and compares with the decay model's assumptions.

### 42.4 Humility in statistics

Report sample sizes and intervals. A difference between partners of two days in half-life may be noise with small samples.

### 42.5 Publication

Results are shared with partners first, in aggregate, then perhaps at a practitioner conference with BEN's approval. Raw indicators are never published.

### Practice note — reproducibility

Code, synthetic data generators and parameter files are archived so another engineer can repeat the analysis next year.

### Peer review inside BEN

Before sharing outside, a senior analyst and a data-protection reviewer read the study. The analyst checks that conclusions follow from the data; the reviewer checks that no partner or person can be identified from tables or examples.

### Worked example

Re-observation data show that domain indicators are re-sighted at meaningful rates up to about 60 days, longer than the 45-day half-life assumed. Kofi proposes raising the domain half-life and documents the sample size, interval and limits.

> **Synthetic case.** Findings are invented.

### Errors and limits

Operational data reflect BEN's environment; generalise cautiously. Do not publish partner-specific statistics without consent.

### Exercises

- **EX124 — Research question.** Write a research question Lantern data could answer. *Rubric:* 3 = specific, measurable, uses available data; 2 = vague; 1 = unanswerable; 0 = none.
- **EX125 — Synthetic limit.** What can synthetic data show in this research, and what can it not? *Rubric:* 3 = test methods/pipelines; not prove real-world facts; 2 = one half; 1 = proves all; 0 = none.
- **EX126 — Publish order.** In what order are results shared, and why? *Rubric:* 3 = partners first in aggregate, then wider with approval; reciprocity/consent; 2 = order only; 1 = public first; 0 = none.

### Synthesis

Ask operational questions, respect consent, test methods on synthetic data, report with humility and share with partners first.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within an operating organisation's governance; (2) contribute to a sector sharing community responsibly; (3) document professional practice hours and reflections; (4) handle confidential material learned on placement.

### 43.1 Placement governance

Kofi's placement at BEN is governed by an agreement covering confidentiality, supervision and what he may write about. University assignments draw on synthetic reconstructions, not BEN's real data.

### 43.2 Community contribution

As a placement engineer he attends sector ISAC calls as an observer. He learns the community's TLP habits, how members describe incidents, and how trust is built over time by sharing useful, accurate information and acknowledging others' contributions.

### 43.3 Practice log

He logs tasks, hours, skills used and reflections: what went well, what he would change, what he learned about ethics. Supervisors sign the log.

### 43.4 Confidential material

Some information he sees is TLP:RED or commercially sensitive. It never appears in coursework, social media or conversation outside need-to-know. If in doubt, he asks his supervisor.

### 43.5 Public-service settings

In a national CERT or regulator, additional rules apply: official secrecy, freedom-of-information obligations and political neutrality. ICD 203's emphasis on independence from political considerations is a useful reference for analysts in public roles.

### Practice note — asking questions

Experienced practitioners expect placement students to ask. Asking before acting on unclear sharing rules prevents the kind of mistake that ends a placement.

### Ending the placement

At the end of the placement Kofi returns equipment, has his accounts disabled, and confirms in writing that he holds no BEN data on personal devices.

### Worked example

A classmate asks Kofi which supplier was compromised in a recent incident he heard about at BEN. He declines, explains that it was shared under TLP:AMBER within BEN, and points the classmate to a public CLEAR advisory on the same campaign.

> **Synthetic case.** The exchange is invented.

### Errors and limits

Placement experience is valuable but narrow; reflect on how other organisations differ. Signing a confidentiality agreement does not override legal reporting duties.

### Exercises

- **EX127 — Coursework source.** May Kofi base a university assignment on BEN's real incident data? Explain. *Rubric:* 3 = no; use synthetic reconstructions per agreement; 2 = no; 1 = yes; 0 = none.
- **EX128 — Reflection entry.** Write a short practice-log reflection about a sharing decision. *Rubric:* 3 = task, what went well/badly, ethics lesson; 2 = two; 1 = task only; 0 = none.
- **EX129 — Classmate request.** What was correct about Kofi's response to his classmate? *Rubric:* 3 = declined restricted info; cited TLP; offered public alternative; 2 = declined; 1 = shared; 0 = none.

### Synthesis

Work inside governance, contribute to trust, log and reflect, and keep restricted material where it belongs.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) scope a capstone extending Lantern; (2) write a project charter with requirements, risks and milestones; (3) form a team with clear roles; (4) secure ethical approval for any data use.

### 44.1 Choosing a scope

Capstones should be ambitious but finishable in two semesters. Kofi's team chooses: "An OT vendor-watch service that turns vendor advisories and partner reports into approved, interlocked recommendations for BEN's OT engineers." It touches requirements, data models, controls, integration, validation and safety.

### 44.2 Charter

Problem statement, stakeholders, measurable objectives (for example, vendor-relevant alerts reach the OT queue within 15 minutes with fewer than 10% irrelevant), constraints (standard library prototypes, synthetic data, no OT automation), milestones, risks and a communication plan.

### 44.3 Team roles

Lead engineer, data modeller, controls and safety owner, validation owner. Roles rotate for some tasks so everyone touches the whole system.

### 44.4 Ethics approval

The project uses synthetic advisories and synthetic OT asset lists. If any real vendor advisories are used, only public CLEAR documents qualify, and their terms are checked. The approval is filed with the charter.

### 44.5 Risk register

Risks: scope creep, unavailable OT reviewer, ambiguous vendor naming, overconfidence in automated relevance scoring. Each has an owner and mitigation.

### Practice note — first milestone

The first milestone is a thin end-to-end slice — one synthetic advisory flowing to one OT ticket — before any component is polished.

### Supervisor cadence

The team meets its supervisor every two weeks with a one-page status: progress against milestones, risks that changed and decisions needed. Short, regular check-ins catch scope creep before it costs a semester.

### Worked example

The charter's first draft promised "detect all threats to OT". The supervisor rejects it as unverifiable. The revised objective names a measurable relevance rate and timeliness on a defined synthetic test set.

> **Synthetic case.** The team and charter are invented.

### Errors and limits

Capstones fail more often from scope than from technology. Real OT data are out of bounds unless formally approved.

### Exercises

- **EX130 — Objective rewrite.** Rewrite "detect all threats to OT" as a capstone objective. *Rubric:* 3 = measurable timeliness/relevance on defined test set; 2 = measurable but vague set; 1 = unchanged; 0 = none.
- **EX131 — Thin slice.** Why build a thin end-to-end slice first? *Rubric:* 3 = exposes integration problems early; proves path; 2 = partial; 1 = polish first; 0 = none.
- **EX132 — Advisory source.** Which real documents may the team use, if any? *Rubric:* 3 = public TLP:CLEAR vendor advisories after checking terms; 2 = public only; 1 = any; 0 = none.

### Synthesis

Scope to finish, charter with measurable aims, assign roles, file ethics approval and build a thin slice first.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design package for independent review; (2) respond to review findings with tracked actions; (3) distinguish must-fix findings from recommendations; (4) record the review outcome formally.

### 45.1 Package

Requirements and traceability, architecture and ADRs, safety argument, threat model and FMEA, verification reports from Chapters 30 and 40, privacy assessment, and open risks. Reviewers receive it a week in advance.

### 45.2 Reviewers

An external engineer from another utility, a privacy specialist, and an OT safety engineer. None worked on the design. Their independence is the point: none of them reports to the BEN manager who owns Lantern's delivery date.

### 45.3 Findings

Findings are graded: must-fix before go-live, should-fix within a set time, and observations. Each gets an owner and due date.

### 45.4 Responses

The team responds in writing: accepted with action, accepted with alternative, or disputed with evidence. Disputes are resolved by the review chair.

### 45.5 Outcome

The chair records the decision: proceed, proceed with conditions, or do not proceed. Conditions link to must-fix findings.

### Practice note — preparing reviewers

A one-page reading guide pointing reviewers to the riskiest decisions makes their limited time count.

### Review logistics

The review runs for half a day: thirty minutes of overview, then reviewers question the team on the riskiest decisions. Findings are drafted the same afternoon while details are fresh, and the team receives them within two days. Minutes record who said what so later disputes can be checked against the record.

### Worked example

The OT safety reviewer finds that the vendor-watch service can create OT tickets with recommended firewall changes but no explicit reminder of the two-person rule. Must-fix: add the rule to every recommendation and block ticket closure without both approvals. The chair grants "proceed with conditions".

> **Synthetic case.** The review and findings are invented.

### Errors and limits

Reviews by friends or managers who own the schedule are not independent. A review is a snapshot; major changes need another.

### Exercises

- **EX133 — Finding grades.** Name the three finding grades. *Rubric:* 3 = must-fix, should-fix, observation; 2 = two; 1 = one; 0 = none.
- **EX134 — Independence test.** Why can BEN's SOC manager not serve as an independent reviewer? *Rubric:* 3 = involved/owns outcome/schedule; conflict of interest; 2 = partial; 1 = can; 0 = none.
- **EX135 — Condition link.** What must a "proceed with conditions" outcome reference? *Rubric:* 3 = specific must-fix findings with owners/dates; 2 = vague conditions; 1 = nothing; 0 = none.

### Synthesis

Package evidence, use truly independent reviewers, grade and track findings, and record a formal outcome.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) complete the capstone build to the charter; (2) close review conditions; (3) validate with stakeholders on synthetic scenarios; (4) prepare handover to operations.

### 46.1 Completing the build

The vendor-watch service ingests synthetic vendor advisories and partner reports, tags vendors and products, scores relevance against BEN's synthetic OT asset list, and opens OT tickets with recommendations, TLP marking and the two-person rule.

### 46.2 Closing conditions

Each must-fix finding is closed with evidence: a test, a screenshot of the ticket template, a code reference. The review chair confirms closure.

### 46.3 Stakeholder validation

OT engineers run five scenarios. In four, recommendations are relevant and timely; in one, a vendor name variant was missed. The team adds the variant to the vendor dictionary and a rule to flag unknown names for analyst review.

### 46.4 Handover

Runbooks, on-call notes, configuration guide, known issues and a training session for the OT team. Operations signs acceptance.

### 46.5 Measured results

On the 200-item synthetic test set: 96% of relevant items alerted within 15 minutes; 7% of alerts irrelevant. Both meet the charter's objectives.

### Practice note — known issues

Listing known issues honestly at handover builds trust; operations will find them anyway.

### Post-acceptance monitoring

For the first month after acceptance the team reviews every OT ticket the service creates with the OT engineers, comparing its relevance judgments with theirs. Disagreements feed the vendor dictionary and scoring rules, and the agreement rate is reported to the supervisor as an early operational measure.

### Worked example

The final demonstration shows an advisory naming "RelayCo" (synthetic) flowing to an OT ticket in 6 minutes, with ATT&CK techniques from the advisory (for example T1190 Exploit Public-Facing Application) listed for context and the two-person approval enforced.

> **Synthetic case.** RelayCo and results are invented.

### Errors and limits

Synthetic test sets may not reflect real advisory diversity; plan to review performance on real public advisories after go-live. Acceptance is not the end of maintenance.

### Exercises

- **EX136 — Missed variant.** How did the team fix the missed vendor-name variant? *Rubric:* 3 = add variant + flag unknown names for analyst review; 2 = add variant; 1 = ignore; 0 = none.
- **EX137 — Objective check.** Do 96% within 15 min and 7% irrelevant meet the charter? Explain. *Rubric:* 3 = yes; ≥95% and <10%; 2 = yes; 1 = no; 0 = none.
- **EX138 — Handover items.** List four handover items. *Rubric:* 3 = four of runbooks, on-call notes, config guide, known issues, training; 2 = two; 1 = one; 0 = none.

### Synthesis

Build to the charter, close conditions with evidence, validate with users, hand over honestly and measure against objectives.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) plan recovery-time and recovery-point objectives for Lantern; (2) run failure drills in staging; (3) score drills against objectives; (4) turn misses into improvements.

### 47.1 RTO and RPO

Recovery time objective (RTO): how long Lantern may be down. Recovery point objective (RPO): how much data may be lost. For BEN, RTO 60 minutes and RPO 15 minutes for the store and ingestion.

### Lab 9 — drill scoring

```python
"""Lab 9 (ch 47): score a synthetic failure-and-recovery drill against RTO/RPO targets."""
RTO_MIN, RPO_MIN = 60, 15
drills = [("D1 store failover", 42, 5), ("D2 TAXII outage", 75, 0), ("D3 corrupt enrich cache", 30, 25)]
for name, recovery, dataloss in drills:
    ok_rto, ok_rpo = recovery <= RTO_MIN, dataloss <= RPO_MIN
    print(f"{name:26} RTO {'met' if ok_rto else 'MISSED'} ({recovery}m)  RPO {'met' if ok_rpo else 'MISSED'} ({dataloss}m)")
```

Run with `python3 lab_drill.py`. Verified output:

```text
D1 store failover          RTO met (42m)  RPO met (5m)
D2 TAXII outage            RTO MISSED (75m)  RPO met (0m)
D3 corrupt enrich cache    RTO met (30m)  RPO MISSED (25m)
```

### 47.2 Reading the drills

D1, store failover, met both objectives. D2, a TAXII outage simulation, missed RTO at 75 minutes because the runbook assumed a credential that had rotated. D3, corrupt enrichment cache, recovered quickly but lost 25 minutes of enrichment state, missing RPO.

### 47.3 Improving

D2: update the runbook and add a credential-validity check to the daily health report. D3: snapshot the cache every ten minutes or treat the cache as rebuildable and exclude it from RPO, documenting that choice.

### 47.4 Drill safety

Drills run in staging with synthetic data. Partners are not involved unless a joint exercise is agreed, and production enforcement is never altered by a drill.

### 47.5 Incident linkage

NIST SP 800-61 Rev. 3 frames incident response within cybersecurity risk management. Lantern's recovery plans connect to BEN's incident response plan so that an outage during a real incident is handled consistently.

### Practice note — surprise element

Some drills are announced only to the facilitator, testing the real readiness of on-call engineers rather than rehearsed performance.

### Recording drills

Each drill record lists the scenario, start and end times, actions taken, deviations from the runbook and follow-up actions with owners. Records are kept for audits and for comparing readiness across quarters.

### Worked example

After fixes, D2 is rerun: recovery in 38 minutes. D3's cache is reclassified as rebuildable; the RPO now applies only to the store, which met it.

> **Synthetic case.** Drill results are invented.

### Errors and limits

Redefining objectives to pass drills must be a documented decision, not a convenience. Staging drills miss some production behaviours.

### Exercises

- **EX139 — Drill misses.** Which drill missed RTO and which missed RPO? *Rubric:* 3 = D2 RTO; D3 RPO; 2 = one; 1 = wrong; 0 = none.
- **EX140 — RTO vs RPO.** Define RTO and RPO in one line each. *Rubric:* 3 = max downtime; max data loss; 2 = one; 1 = swapped; 0 = none.
- **EX141 — Reclassify honestly.** When is reclassifying the cache as rebuildable legitimate? *Rubric:* 3 = documented decision with justification that loss is harmless/rebuildable; 2 = documented; 1 = to pass drill; 0 = none.

### Synthesis

Set RTO and RPO, drill safely, score honestly, fix causes and document any change to objectives.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble an evidence dossier supporting the claim that Lantern and its vendor-watch extension are fit for purpose; (2) structure an assurance argument; (3) link every claim to evidence with integrity protection; (4) state residual risks and assumptions.

### 48.1 Assurance argument

Top claim: "Lantern delivers timely, trustworthy, lawfully collected intelligence to BEN's IT and OT defenders with acceptable risk." Sub-claims: timeliness, accuracy, TLP and privacy compliance, safety of OT recommendations, reliability, maintainability. Each sub-claim cites evidence.

### 48.2 Evidence types

Verification reports, validation results, drill records, review outcomes, metrics over a quarter, privacy assessment and partner feedback. Each item has a date, author, version and SHA-256 hash recorded in an index.

### 48.3 Assumptions

The argument depends on assumptions: partners label TLP correctly; NTP is reliable; OT engineers follow the two-person rule. Assumptions are stated, and where possible monitored.

### 48.4 Residual risks

Unseen partner formats, adversary poisoning that mimics legitimate patterns, staff turnover. Each risk has an owner and acceptance by an accountable manager.

### 48.5 Audience

The dossier serves BEN's risk committee, auditors and future engineers. A two-page summary leads; the full evidence sits behind it.

### Practice note — counter-evidence

The dossier includes evidence against claims too, such as the failed drill D2 and its fix. Omitting counter-evidence makes an argument look stronger and be weaker.

### Keeping the dossier alive

After go-live the dossier is updated each quarter with new metrics and drill records. Claims whose evidence has aged beyond its review date are marked as needing renewal until fresh evidence arrives.

### Worked example

Kofi's index lists 37 evidence items. A reviewer picks five at random, recomputes their hashes and finds all match. One sub-claim — maintainability — rests only on a single documentation test; the reviewer asks for a second piece of evidence, and Kofi adds the technical-debt register trend.

> **Synthetic case.** Counts are invented.

### Errors and limits

An assurance argument shows reasons for confidence, not proof of security. Evidence ages; set review dates.

### Exercises

- **EX142 — Sub-claims.** List four sub-claims under Lantern's top claim. *Rubric:* 3 = four of timeliness, accuracy, TLP/privacy, OT safety, reliability, maintainability; 2 = two; 1 = one; 0 = none.
- **EX143 — Hash spot check.** What does the reviewer's hash recomputation confirm? *Rubric:* 3 = evidence files unchanged since indexing; 2 = integrity vaguely; 1 = evidence true; 0 = none.
- **EX144 — Counter-evidence.** Why include the failed drill D2 in the dossier? *Rubric:* 3 = honesty; shows weakness and fix; strengthens credibility; 2 = partial; 1 = omit; 0 = none.

### Synthesis

Argue with structure, index evidence with hashes, state assumptions and residual risks, and include counter-evidence.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis that reports design, implementation and evaluation; (2) situate the work in standards and literature; (3) separate contributions from context; (4) present limitations and future work precisely.

### 49.1 Structure

Introduction (problem, objectives, contributions); background (CTI concepts, STIX/TAXII 2.1, ATT&CK, Diamond Model, kill chain, TLP 2.0, SP 800-150); requirements; design; implementation; verification and validation; operations evidence; discussion; conclusion.

### 49.2 Contributions

Kofi's contributions: an interlocked OT vendor-watch design; a decay-model refit procedure from re-observation data; an evaluation of feed quality with labelled sets. Background material — how STIX works — is not a contribution, however long the chapter.

### 49.3 Using sources

Cite specifications for definitions, papers for models, and BEN-approved synthetic or aggregate data for results. Every claim of fact has a citation or evidence reference.

### 49.4 Limitations

Synthetic test sets, one organisation's environment, short operational period, self-reported user feedback. For each, the likely effect on conclusions.

### 49.5 Future work

Prospective measurement of incidents prevented; cross-utility comparison with consent; automated detection of feed poisoning.

### Practice note — figures

Each figure answers one question and is referenced in the text. Architecture diagrams use the same component names as the code.

### Writing process

Kofi drafts results chapters first, while the evidence is fresh, then writes the introduction last so that it promises exactly what the thesis delivers. Each chapter goes to the supervisor with a cover note listing the questions he wants answered, which makes feedback faster and more focused than sending unexplained drafts.

### Worked example

Kofi's supervisor marks a paragraph claiming Lantern "eliminates OT risk from vendor compromise". Kofi rewrites: "On synthetic tests, the service delivered relevant vendor alerts within 15 minutes for 96% of items; it reduces, but cannot eliminate, the time OT engineers are unaware of relevant advisories."

> **Synthetic case.** The thesis text is invented.

### Errors and limits

Overclaiming is the most common thesis defect. Confidential material from placement stays out.

### Exercises

- **EX145 — Contribution or context.** Is an explanation of TAXII 2.1 endpoints a contribution? Explain. *Rubric:* 3 = no; background context; 2 = no; 1 = yes; 0 = none.
- **EX146 — Overclaim fix.** Rewrite "Lantern stops all phishing" honestly. *Rubric:* 3 = measured, scoped, hedged claim; 2 = hedged but unmeasured; 1 = unchanged; 0 = none.
- **EX147 — Limitation effect.** State the likely effect of evaluating on one organisation's environment. *Rubric:* 3 = limits generalisability; results may differ elsewhere; 2 = vague; 1 = none; 0 = none.

### Synthesis

Structure for the reader, claim only real contributions, cite precisely, and bound conclusions with limitations.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) present the thesis and dossier to an examination panel; (2) answer technical, ethical and safety questions; (3) acknowledge limits without undermining the work; (4) reflect on professional development and next steps.

### 50.1 Presentation

Twenty minutes: problem and mission; key design decisions; safety interlocks; evaluation results with uncertainty; limitations; future work. Slides show evidence, not decoration.

### 50.2 Expected questions

Why is there no automatic OT blocking? How do you prevent feed poisoning? What happens if a partner mislabels TLP? Why should we trust your feed-quality labels? What would you do differently? Answers cite pages and evidence items.

### 50.3 Ethical questions

Panels ask what Kofi refused to build. He answers: personal social-media collection, scraping against terms, home-address enrichment and OT automation without approval — each with the reason and the alternative chosen.

### 50.4 Acknowledging limits

"I don't know" followed by how one would find out is a strong answer. Defending an unsupported claim is weak.

### 50.5 Next steps

The book does not claim accreditation or a completed 300-page edition. The next stop in the study path is the engineering course in authorized offensive security and red team.

### Practice note — after the defence

Corrections required by the panel are completed, logged and approved before final submission. The archive and dossier are updated to match.

### Reflection

A short reflective statement closes the portfolio: which skills grew, which mistakes taught the most, and which ethical lines were tested during the placement and capstone.

### Worked example

An examiner asks whether Lantern could have caught a recent synthetic poisoning test that inserted a supplier domain. Kofi shows the allow-list interlock blocked it, then concedes that poisoning with an unknown but legitimate small supplier would pass, and points to future work on anomaly detection.

> **Synthetic case.** The examination exchange is invented.

### Errors and limits

Rehearsed answers that ignore the actual question frustrate examiners. Claiming the platform is "secure" invites failure.

### Exercises

- **EX148 — Refusal list.** Name three things Kofi refused to build and why. *Rubric:* 3 = three of personal social collection, terms-violating scraping, home-address enrichment, unapproved OT automation, each with reason; 2 = two; 1 = one; 0 = none.
- **EX149 — Poisoning gap.** What poisoning case does Kofi concede Lantern would miss? *Rubric:* 3 = legitimate small supplier not on allow-list; 2 = vague gap; 1 = none; 0 = none.
- **EX150 — Next course.** What is the next course after this book, and what must not be claimed about the draft? *Rubric:* 3 = course 134 RED engineering + no accreditation/finished-book claim; 2 = one; 1 = wrong; 0 = none.

### Synthesis

Present evidence, answer with references, own the refusals and the limits, and leave with a clear next step.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Brightwater Energy Networks, Lantern, Kofi Mensah and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** (13,300 − 12,700) / 1 h = 600 indicators per hour.

**EX002.** Work queues build whenever arrivals exceed service; a daily mean averages away the bursts that actually overload the parser.

**EX003.** Trapezoids: (2+4)/2 + (4+6)/2 = 3 + 5 = 8 analyst-hours.

**EX004.** Three hops: event-1 → c2.example → event-4 → victim-B.

**EX005.** Nothing in the graph links event-7 to event-1, so a shared-campaign claim needs additional evidence.

**EX006.** Thousands of unrelated customers can share one hosting address, so co-occurrence there says little about a common adversary.

**EX007.** 500 MB × 8 = 4,000 Mbit; / 50 Mbit/s = 80 s.

**EX008.** 20,000 × 2 KB = 40 MB per day; × 365 ≈ 14.6 GB per year raw.

**EX009.** Every measured interval can be off by up to two minutes in one direction; synchronise clocks with NTP and record the time source.

**EX010.** No. Writing to a log file is a side effect, so the function is not pure; split normalisation from logging.

**EX011.** Refanged values are used inside Lantern's parsing and storage; reports and messages shown to people keep the defanged form.

**EX012.** A rejection (error or flag), because an empty string must never be stored as an indicator.

**EX013.** The queue statement is a measured fact; the 20% growth is an assumption about the future.

**EX014.** At least TLP:AMBER, inherited from the agreement covering the quoted partner names.

**EX015.** The metric and its units, the time period covered, and the data source.

**EX016.** 45.0 — day 14 is exactly one half-life, so 90 halves to 45.

**EX017.** t = 14 × ln(90/30) / ln 2 = 14 × 1.585 ≈ 22.2 days.

**EX018.** Adversaries sometimes reuse old infrastructure, and analysts need to match past events; archived indicators stay searchable without driving automated blocks.

**EX019.** 0.045 — about one true alert in twenty-two.

**EX020.** Lower the false-positive rate (for example by combining with a second signal), and apply the rule only to traffic segments where malicious activity is more prevalent; an enrichment gate before paging also works.

**EX021.** Latency is right-skewed; the slow tail is what users notice and what SLAs govern, and a mean hides it.

**EX022.** Input/output — the process is waiting on disk; keep the hot set in memory or on faster storage.

**EX023.** Enrichment data go stale, and providers' terms may limit how long results can be retained or how often they are queried.

**EX024.** 400,000 × 200 B = 80 MB raw; real usage will be higher because of object overhead.

**EX025.** Any four of: rejection reason, source, hash of the original bytes, timestamp, parser version.

**EX026.** norm(norm(x)) == norm(x): re-running ingestion or re-normalising stored data never changes values, so duplicates and drift do not appear.

**EX027.** The objects are TLP:AMBER and the partner already holds them; hashes and counts let them find the bad records without Lantern re-sharing restricted content.

**EX028.** Combined facts can reveal where someone lives or how to find them, enabling harassment; processing identifiable data also triggers data-protection obligations.

**EX029.** Abort the push, keep the last known-good list active on the firewalls, and alert a human for review.

**EX030.** Decline, record the request in writing, and escalate to the privacy officer or legal team.

**EX031.** TAXII 2.1 specifies the HTTPS API — discovery, API roots, collections, object endpoints, media types; who may read or write and what may be shared come from agreements.

**EX032.** The address hosts thousands of unrelated sites, so blocking it would cause collateral damage; the domain identifies the malicious resource specifically.

**EX033.** Back off and retry after the interval the server indicates (for example Retry-After); never rotate identities or addresses to evade the limit.

**EX034.** No. Least privilege and separation of duties keep firewall changes in a separate, audited service; a compromised collector should not be able to alter controls.

**EX035.** Lantern's application access logs, corroborated by OS authentication logs for the accounts involved.

**EX036.** Any three of: no or tightly limited network access, read-only file system, memory and CPU limits, unprivileged user.

**EX037.** Four: c2.example, http://drop.example/a, 203.0.113.9 and 198.51.100.44.

**EX038.** Two independent sources reporting the same indicator is corroboration analysts need to see, and provenance supports audit of who shared what.

**EX039.** URL paths are often case-sensitive on servers, so `/Payload` and `/payload` can be different resources; lower-case only the scheme and host.

**EX040.** Changes in end-to-end behaviour — how many indicators survive all stages and reach blocking — which individual unit tests do not reveal.

**EX041.** No requirement or SOC agreement justified it, and the replay showed a large behavioural effect (1,240 extra indicators in automated blocking).

**EX042.** In a secrets vault; configuration stores only references to the vault entries.

**EX043.** A poisoned indicator listing a supplier's domain could cause BEN to block that supplier, interrupting payments or updates; alternatively, removed indicators could let a real threat through.

**EX044.** Example: Detect — indicators and techniques become detection rules; Identify — threat profiles inform risk assessment. Respond (context during incidents) and Govern (sharing agreements) also score.

**EX045.** It catches poisoned or mistaken entries that would block services BEN depends on before they reach controls.

**EX046.** No. It is an external system owned by the ISAC; Lantern interacts with it through a controlled TAXII interface.

**EX047.** Data format, rate limits, authentication, error handling, owners on each side (versioning also counts).

**EX048.** Notify the partner, delete any retained data the agreement requires deleting, and revoke the credentials used for the feed.

**EX049.** Sensor: false-positive tickets from the SOC. Controller: the threshold-adjustment rule. Actuator: the block list pushed to firewalls.

**EX050.** Small steps avoid overreacting to a noisy day and prevent the threshold oscillating between too strict and too loose.

**EX051.** Missed detections rarely produce tickets, so a loop driven only by complaints drifts toward fewer blocks and more misses.

**EX052.** OT zones should contain only what operations needs; adding a CTI platform increases attack surface and safety risk, so OT receives approved outputs only.

**EX053.** A DNS resolver or web-proxy block on the domain, because it targets the malicious name without blocking thousands of unrelated sites on the shared address.

**EX054.** It removed direct internet access from the SOC zone, shrinking exposure and a potential exfiltration path from the store.

**EX055.** It proves the bundle came from the key holder and was not altered; it does not prove the indicators are accurate.

**EX056.** Only the individuals named as recipients on that report.

**EX057.** Alerts 30, 14 and 3 days before expiry to the owning engineer and the partner contact, with a rotation runbook link.

**EX058.** Information — organised and contextualised, but not yet analysed into what BEN should do.

**EX059.** A vendor-watch report that tells the OT engineer whether campaigns target BEN's relay vendor, with recommended actions.

**EX060.** "Legally collected" — it commits Lantern's OSINT and feeds to lawful, terms-respecting collection.

**EX061.** Example: "Lantern shall publish analyst-approved TLP:GREEN indicators to the ISAC TAXII collection within 60 minutes of approval for 95% of indicators per month."

**EX062.** Example: "Lantern shall tag threat-actor objects whose reports cite targeting of electricity distribution and produce a monthly actor summary; verified by a synthetic report test."

**EX063.** Example: "The OSINT module shall collect only from organisational sources (domains, certificates, advisories) and shall not store personal social-media profiles; verified by a code review and a test that rejects such sources."

**EX064.** `pattern`, `pattern_type` and `valid_from`.

**EX065.** Store it opaquely with provenance and flag it for review, so nothing is silently lost.

**EX066.** new → active → decayed → retired. Example trigger: active → decayed when confidence falls below the floor; decayed → active on a new sighting.

**EX067.** 7 × 3 × 5 = 105.

**EX068.** 6 × 4 × 2 = 48.

**EX069.** T1078 Valid Accounts.

**EX070.** As "unknown": nothing in the evidence identifies the adversary, and guessing would contaminate later analysis.

**EX071.** Phishing email: T1566. Script execution: T1059.

**EX072.** Deny at delivery: a mail-gateway rule blocking the phishing pattern. Detect at command and control: DNS analytics alerting on drop.example lookups.

**EX073.** Context, decision, alternatives considered, consequences.

**EX074.** Indicators can wait up to 15 minutes before ingestion; shorter intervals would raise load on partner servers.

**EX075.** Sender domain, a hash of the subject line, and the extracted indicator fields.

**EX076.** If weights are set after scoring, they can be tuned so a preferred option wins; agreeing them first keeps the study honest.

**EX077.** A platform that exports everything as standard STIX 2.1 lets BEN migrate history cheaply; one that does not traps data and raises exit cost.

**EX078.** As a near-tie within scoring uncertainty, with the decisive qualitative issue — OT workflow risk — put explicitly to the panel.

**EX079.** R-1: `TLP:GREEN -> public BLOCK`. R-3: `TLP:RED -> team BLOCK`.

**EX080.** TLP:PURPLE is not a TLP 2.0 label, so the gate fails closed and blocks it.

**EX081.** The named approver, the approval time, the exact rule or object version pushed, and the reason.

**EX082.** If the checkpoint moves first and the process crashes before writing, those objects are never fetched again; writing first means a crash only causes a harmless re-fetch, made safe by idempotent writes.

**EX083.** Development traffic never loads or risks partner servers, and tests run on fixed synthetic bundles so results are reproducible.

**EX084.** Checkpoint age (or objects received per source): if it keeps growing or receipts drop to zero, the collector has stalled.

**EX085.** precision 0.50, recall 0.60, F1 0.55.

**EX086.** Using the feed's own claims as truth would count every entry as correct, inflating precision; labels must come from independent investigations.

**EX087.** The feed typically lists indicators two days after BEN already saw them, so it adds little preventive value.

**EX088.** Verification: confirming Lantern meets its written requirements. Validation: confirming it meets stakeholders' actual needs in use.

**EX089.** Label handling must be exact and specified — either normalised by a documented rule or rejected; silently accepting a variant shows the gate does not behave as required.

**EX090.** As "blocked — not executed", listed separately with the missing fixture and a scheduled date; it is not a pass.

**EX091.** So export can strip fields whose provider forbids redistribution and retention limits can be honoured per source.

**EX092.** It shares the indicator reference, sighting counts and first/last-seen times; it removes internal hostnames and user names.

**EX093.** It avoids rewriting every record nightly and keeps the decay model in one function, so changing the model changes all results at once.

**EX094.** 0.9732 serial availability, about 235 hours of downtime per year.

**EX095.** If both run on the same host, depend on the same external provider or share a network path, one fault takes both down — a common-mode failure.

**EX096.** Keep ingesting and matching, flag affected indicators as "unenriched", and enrich them when the provider returns.

**EX097.** Blocking traffic between a SCADA master and remote terminal units would remove visibility and control of substations.

**EX098.** No automatic OT actions; a protected-address allow-list that blocks may not include; a maximum change size per push; two-person approval (any three).

**EX099.** Behavioural detections look for techniques such as T1059 or T1071 in BEN's own telemetry, so they keep working without the lost feed's indicators.

**EX100.** The integration reads the target's current rules, compares them with Lantern's desired set and applies only the differences, so repeating a push changes nothing.

**EX101.** Source, confidence, TLP marking, related ATT&CK techniques (also recommended action and Diamond fields).

**EX102.** Reject it for that target with a recorded reason, and route it to an integration that can express it; never approximate silently.

**EX103.** Tactical digest → SOC analysts; operational summary → incident-response and hunt leads; strategic brief → executives.

**EX104.** Source descriptions with confidence on a published estimative scale, and a tracked record of past judgments' accuracy (change triggers also count).

**EX105.** Colour alone fails for colour-blind readers and monochrome printing; TLP 2.0 expects the label text to be shown.

**EX106.** A backlog of 100 after five minutes; it grows by 20 every minute because 120 arrive and only 100 are served.

**EX107.** W = L / λ = 300 / 2 = 150 seconds.

**EX108.** Each new identity would poll the partner separately, multiplying their load and potentially breaching agreed rate limits.

**EX109.** By issuing a new version of the object with `revoked` set to true.

**EX110.** Contain (remove access), assess what was exposed, notify the originator as the agreement requires, and review the gate that failed.

**EX111.** Only conditions that need human action within about an hour; everything else goes to a daily review queue.

**EX112.** Example: "Do duty analysts have intelligence context available when they triage phishing incidents, and does it change their actions?"

**EX113.** Change it so vendor alerts are delivered to the OT team's ticket queue, where they actually work.

**EX114.** Example: BEN also hired two SOC analysts during the same period, which alone could shorten enforcement time.

**EX115.** A new engineer added a synthetic partner using only the documentation; the two unclear steps they found were fixed.

**EX116.** Example: "Polling interval hard-coded to 15 minutes in collector; prevents per-partner tuning; risk medium; move to configuration by Q2."

**EX117.** ATT&CK versions rename and deprecate techniques; storing the version lets Lantern list mappings that need migration when a new release appears.

**EX118.** Submit a synthetic personal social-media profile URL to the OSINT module; expect rejection with reason "personal profile source not permitted" and a log entry.

**EX119.** Pass: the 95th percentile of 22 minutes is within the 30-minute requirement.

**EX120.** In staging with synthetic stubs only; never against production systems or partner servers.

**EX121.** More objects mean more noise, more false positives and more analyst workload, which can slow response to the indicators that matter.

**EX122.** A spot check of later retractions showed no increase, suggesting approval quality did not fall as speed rose.

**EX123.** The two-person approval for OT firewall changes, which deliberately slows high-impact actions to prevent operational harm.

**EX124.** Example: "For indicators retired by decay, what proportion of domains versus IP addresses are re-sighted within 60 days?"

**EX125.** Synthetic data can test whether the method and code work; they cannot establish facts about real adversary behaviour or BEN's environment.

**EX126.** Partners first, in aggregate, then wider venues with BEN's approval — because partners contributed data and must consent to its use.

**EX127.** No. The placement agreement limits use of BEN's data; assignments must use synthetic reconstructions.

**EX128.** Example: "Drafted a GREEN summary of a partner bulletin; supervisor caught a partner name that made it AMBER. Lesson: check every field for inherited restrictions before proposing a label."

**EX129.** He declined to reveal TLP:AMBER information, explained why, and pointed to a public CLEAR advisory instead.

**EX130.** Example: "On a 200-item synthetic advisory set, deliver vendor-relevant alerts to the OT queue within 15 minutes for 95% of relevant items with fewer than 10% irrelevant alerts."

**EX131.** It proves the whole path works and exposes integration problems early, before effort is spent polishing components that may need to change.

**EX132.** Only public TLP:CLEAR vendor advisories whose terms permit this use; everything else stays synthetic.

**EX133.** Must-fix before go-live, should-fix within a set time, and observation.

**EX134.** The SOC manager is a stakeholder who benefits from the platform and may own its schedule, a conflict of interest that undermines independence.

**EX135.** The specific must-fix findings, each with an owner and due date, that must be closed before go-live.

**EX136.** They added the variant to the vendor dictionary and a rule that flags unknown vendor names for analyst review.

**EX137.** Yes: 96% meets the 95% timeliness target and 7% irrelevant is below the 10% limit.

**EX138.** Runbooks, on-call notes, configuration guide, known-issues list (training session also counts).

**EX139.** D2 (TAXII outage) missed RTO at 75 minutes; D3 (corrupt enrichment cache) missed RPO with 25 minutes of loss.

**EX140.** RTO: the maximum acceptable time the service may be down. RPO: the maximum acceptable amount of data loss, measured in time.

**EX141.** When it is a documented decision showing the cache can be fully rebuilt from stored data without harm, not a convenience to pass the drill.

**EX142.** Timeliness, accuracy, TLP and privacy compliance, OT recommendation safety (reliability and maintainability also count).

**EX143.** That the sampled evidence files are byte-identical to the versions indexed — they were not altered after indexing.

**EX144.** It shows reviewers a real weakness and how it was fixed, which makes the overall argument more credible than a record of only successes.

**EX145.** No. It explains how an existing standard works; the contributions are Kofi's own designs, procedures and evaluations.

**EX146.** Example: "During the evaluation quarter, Lantern blocked 82% of confirmed phishing domains before first internal contact; it reduces but does not prevent phishing."

**EX147.** Results may not generalise to utilities with different networks, partners or staffing; other environments could perform better or worse.

**EX148.** Personal social-media collection (privacy and terms), scraping against platform terms (legal and ethical), home-address enrichment (no decision needed it; privacy), automatic OT blocking without approval (safety).

**EX149.** Poisoning that lists a legitimate small supplier not on the critical-supplier allow-list would pass the interlock.

**EX150.** Course 134, authorized offensive security and red team (engineering). The draft must not be presented as accredited or as a completed 300-page book.

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
