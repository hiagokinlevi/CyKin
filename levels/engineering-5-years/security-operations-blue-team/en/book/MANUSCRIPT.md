# Security Operations and Blue Team: Engineering Course

- Language: English (`en`); course 130, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; Nine offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students who will design, build, verify and operate security monitoring systems and the SOC processes around them.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: monitor and respond only on systems you are authorised to defend; no exploit code, no payloads, no attack procedures and no instructions for evading detection. Detections are taught from the defender's side using synthetic telemetry. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the foundation chapters apply mathematics, computing and engineering practice to security operations, and the specialist chapters follow one SOC placement from a customer-portal account-takeover incident to a validated capstone that closes a depot monitoring gap. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Amara Osei** | Engineering student on placement | Invented |
| **Paolo Ricci** | Detection engineer and mentor | Invented |
| **Kingsbridge Engineering University** | Fictional university | Invented |
| **Lindqvist Freight** | Fictional logistics company and SOC host | Invented |

### Core sources

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker and Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Full list in [References](#references).

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

You will (1) model an alert queue with rates of change; (2) read a derivative as "how fast the backlog grows"; (3) connect continuous models with hourly data; (4) explain why SOC staffing is a rate problem.

### 1.1 Why calculus in a SOC

Security operations handle flows: alerts arrive, analysts clear them, and the backlog is what is left. Calculus is the language of change. If A(t) is the arrival rate and C(t) the clearing rate, the backlog B(t) changes as dB/dt = A(t) − C(t). When arrivals exceed capacity, the backlog rises; when capacity exceeds arrivals, it falls.

The same equation describes a bath filling while the plug is half open. For a SOC lead, its value is that it separates two questions people often mix up: how many alerts arrived today, and how fast they arrived compared with how fast the team can work. A day with a modest total can still overwhelm a shift if most alerts arrive within two hours.

### 1.2 The course case

**Amara Osei**, an engineering student at the fictional **Kingsbridge Engineering University**, joins the security operations centre of the fictional **Lindqvist Freight** on placement. Her mentor is detection engineer **Paolo Ricci**. On her first day the customer portal suffers a burst of failed logins, and the alert queue grows faster than the two analysts on shift can clear it.

The burst is a common pattern on public login pages: many failed attempts against many usernames, often from a small range of addresses. Amara's first task is not to decide whether an attack happened but to understand why the queue grew, which leads directly into rates. The same incident returns throughout the book, each chapter looking at it through a different tool.

### 1.3 From continuous to discrete

Real data comes in hourly counts, not smooth curves. The derivative becomes a difference: backlog change per hour equals arrivals that hour minus alerts handled. The integral — total backlog — becomes a running sum.

In symbols, B[n] = B[n−1] + A[n] − C[n], with the rule that backlog cannot fall below zero, since an idle analyst cannot clear alerts that do not exist yet. The hourly step is a choice; per-minute counts would show more detail but more noise. Amara builds the running sum in a spreadsheet first, one row per hour, so every step can be checked by hand.

### Lab — queue as a rate

```python
"""Alert queue as a rate problem: backlog change = arrivals - handled, per hour (synthetic)."""
arrivals = [40, 55, 70, 90, 85, 60, 45, 30]   # alerts per hour, 08:00-16:00
capacity = 60                                  # alerts the shift can triage per hour
backlog = 0
peak = 0
for h, a in enumerate(arrivals):
    handled = min(capacity, backlog + a)
    rate = a - handled
    backlog += rate
    peak = max(peak, backlog)
    print(f"{8+h:02d}:00 arrivals={a:3} handled={handled:3} d(backlog)/dt={rate:+4} backlog={backlog:3}")
print("peak backlog", peak, "| backlog at 16:00", backlog)
```

Run with `python3 lab_queue.py`. Verified output:

```text
08:00 arrivals= 40 handled= 40 d(backlog)/dt=  +0 backlog=  0
09:00 arrivals= 55 handled= 55 d(backlog)/dt=  +0 backlog=  0
10:00 arrivals= 70 handled= 60 d(backlog)/dt= +10 backlog= 10
11:00 arrivals= 90 handled= 60 d(backlog)/dt= +30 backlog= 40
12:00 arrivals= 85 handled= 60 d(backlog)/dt= +25 backlog= 65
13:00 arrivals= 60 handled= 60 d(backlog)/dt=  +0 backlog= 65
14:00 arrivals= 45 handled= 60 d(backlog)/dt= -15 backlog= 50
15:00 arrivals= 30 handled= 60 d(backlog)/dt= -30 backlog= 20
peak backlog 65 | backlog at 16:00 20
```

### 1.4 Reading the result

With a capacity of 60 alerts per hour, the backlog stays at zero until 10:00, then grows at +10, +30 and +25 per hour, peaking at 65 alerts by 13:00. It only begins to fall at 14:00 and is still 20 at 16:00. The peak follows the area between the arrival curve and the capacity line, not the single worst hour.

The surprise for Amara is that the backlog keeps rising after the worst hour has passed. As long as arrivals exceed sixty, the queue grows, even if more slowly. It falls only once arrivals drop below capacity, and then only by the size of that gap each hour. That is why the queue lingered into the afternoon although the burst itself was over by early afternoon.

### 1.5 Engineering meaning

Adding one analyst at 10:00 would raise capacity above the peak arrival rate and keep the backlog near zero. Rates, not daily totals, tell you when help is needed.

The same model answers other questions too: how long a backlog of 65 takes to clear at a given spare capacity, or how early help must arrive to keep the peak under a target. Paolo points out that real analysts do not clear alerts at a fixed rate, since hard alerts take longer, so the model gives a planning estimate rather than a precise forecast.

### Worked example

Paolo asks Amara how long an alert that arrives at 12:00 waits. She reasons that it joins a queue of 40 alerts with capacity 60 per hour, so it waits about 40 minutes before an analyst reaches it — long enough to matter for a live credential attack.

> **Synthetic case.** Lindqvist Freight, Kingsbridge University, Amara and Paolo are invented; the counts come from the lab script.

### Errors and limits

The model assumes every alert takes the same time and analysts never pause; real triage time varies widely, so treat results as first estimates.

### Exercises

- **EX001 — Backlog equation.** Write the equation for backlog change and explain each term. *Rubric:* 3 = dB/dt = A − C with arrivals and clearing explained; 2 = equation without meaning; 1 = words only; 0 = none.
- **EX002 — Peak timing.** When and why does the backlog peak in the lab? *Rubric:* 3 = 13:00 at 65; arrivals exceed capacity 10:00–12:00 and equal it at 13:00; 2 = peak value only; 1 = wrong time; 0 = none.
- **EX003 — Waiting time.** Estimate the wait for an alert arriving at 12:00. *Rubric:* 3 = about 40 minutes from 40 queued at 60/h; 2 = method without number; 1 = guess; 0 = none.

### Synthesis

Alert queues follow rates; treating arrivals and capacity as functions of time shows when backlogs form and how much extra capacity removes them.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) use sets and relations to describe users, hosts and alerts; (2) apply logic to detection conditions; (3) count combinations for correlation rules; (4) reason about graphs of logons.

### 2.1 Sets in detection

A detection often asks set questions. Which users failed to log in from network N? Which of them later succeeded? If F is the set of usernames with failures and S the set with successes from the same network, F ∩ S are accounts that may have been guessed correctly.

Set notation turns a vague hunch into a precise query. The intersection does not prove compromise; a customer who mistyped a password twice and then succeeded also lands in F ∩ S. What it does is shrink the list from everyone who failed to the few worth a closer look, which is what a triage step should do.

### 2.2 Logic

Rule conditions are logical formulas. "Process is PowerShell AND parent is an Office application" is a conjunction; adding OR widens a rule; adding NOT narrows it. Writing conditions in logic makes their scope explicit and testable, which is how the Sigma format expresses detection logic.

Mistakes in logic produce real errors: writing OR where AND was meant can turn a precise rule into one that fires on every Office document. Truth tables help check small rules by listing every combination of conditions and the expected outcome. Sigma rules use named selections joined in a condition line, which keeps the logic readable even when each selection has many fields.

### 2.3 Relations and graphs

A logon from user u to host h is a pair (u, h). Together the pairs form a bipartite graph. An account that suddenly connects to many new hosts shows as a node whose degree jumps.

Degree here means the number of distinct hosts an account touches in a time window. A help-desk account might normally connect to dozens, while a payroll clerk connects to two or three, so the jump matters relative to each account's own history. Graphs also show paths, such as an account reaching a server through an intermediate host, which lists of pairs hide.

### 2.4 Counting

Correlation rules combine events. With 7 event types, a rule over any 3 types in order has 7 × 6 × 5 = 210 possibilities. Counting shows why exhaustive correlation explodes and why rules must be chosen from threat knowledge, such as MITRE ATT&CK techniques.

If order does not matter, the count drops to 7 choose 3, which is 35, but adding time windows and field conditions multiplies the possibilities again. No team can write and test hundreds of correlations, so threat knowledge narrows the search to sequences attackers actually use. ATT&CK provides that grounding by describing techniques observed in real intrusions.

### 2.5 Case use

During the portal burst, Amara lists F (usernames with failures from 203.0.113.0/24) and S (usernames with success from the same network). One name, u5, is in both: a candidate compromised customer account.

The address range 203.0.113.0/24 is reserved for documentation, which suits a synthetic case. Amara writes both sets out explicitly, which lets Paolo check her reasoning line by line. The next step is not to lock u5 at once but to check the success's details, such as time, device and what the session did, before deciding on action.

### 2.6 Precision of language

Discrete maths forces exact language: "many" becomes "more than 5 distinct usernames in 10 minutes". That precision makes rules reviewable.

Reviewable means another analyst can read the rule and agree, or disagree, on what it should catch. 'Many' invites arguments; 'more than five in ten minutes' invites a test. The precise version can also be tuned with evidence, by counting how often legitimate users exceed five failures in ten minutes and adjusting the threshold with data rather than opinion. Units belong in every threshold.

### Worked example

Amara writes the rule condition as: count(distinct username where result = fail and source in N, 10 min) > 5 AND exists(username in that set where result = ok). Paolo notes that the second clause turns a noisy "spray" alert into a sharper "possible compromise" alert.

> **Synthetic case.** Usernames and networks are synthetic.

### Errors and limits

Set logic is exact but the data is not: missing logs make sets incomplete, so empty results do not prove absence.

### Exercises

- **EX004 — Intersection.** Why does F ∩ S matter in the portal case? *Rubric:* 3 = accounts failed then succeeded from same network: possible guessed credentials; 2 = partial; 1 = set definition only; 0 = none.
- **EX005 — Correlation count.** How many ordered 3-type sequences come from 7 event types, and what does that imply? *Rubric:* 3 = 210; exhaustive correlation explodes, choose by threat knowledge; 2 = number only; 1 = wrong number; 0 = none.
- **EX006 — Sharper rule.** What does the second clause of Amara's rule add? *Rubric:* 3 = turns spray alert into possible-compromise alert by requiring a success; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Sets, logic, graphs and counting give detection rules exact meaning and show why rule choice must be guided by threat knowledge.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical limits to sensor and storage design; (2) reason about signal, noise and sampling in telemetry; (3) estimate power and heat for SOC infrastructure; (4) recognise physical failure modes.

### 3.1 Signals and noise

Physics describes measurements as signal plus noise. Telemetry is similar: real attack activity is the signal, normal activity is the noise. A sensor that samples too rarely misses short signals, just as a slow oscilloscope misses fast pulses.

The ratio between the two decides how easy detection is. A loud attack against a quiet network stands out; a quiet attack hidden in busy normal traffic does not. Defenders can improve the ratio by collecting fields that separate the two, such as process parentage, rather than simply collecting more data that adds noise as quickly as signal.

### 3.2 Sampling

If a network sensor exports flow summaries every 5 minutes, a 20-second burst appears smeared into one record. Faster sampling resolves bursts but multiplies data volume. Engineering chooses a rate that resolves the signals of interest at acceptable cost.

The smearing is an averaging effect: the burst's intensity spread across five minutes looks like a mild rise rather than a spike. A rule tuned on per-minute data would then miss it. Amara compares the portal's per-request web logs with the five-minute flow summaries for the same period and sees the burst's pace clearly in one, while the other holds only a single large record.

### 3.3 Energy and heat

A SIEM cluster draws electrical power and turns it into heat. Doubling ingestion may need more servers, more cooling and more rack space. Physical capacity limits how much telemetry a SOC can keep.

Each server's power use turns almost entirely into heat that cooling must remove, so power and cooling budgets grow together. A data room with fixed cooling can reach its limit before the budget for servers runs out. Planning ingestion growth therefore involves facilities staff, not just the SIEM team, and long retention may be cheaper on slower, cooler archive storage.

### 3.4 Physical failures

Disks wear out, power supplies fail, fibres get cut. Monitoring infrastructure needs redundancy; a single failed collector can silence a whole site's logs.

A silent collector is worse than a noisy one, because the absence of logs can look like the absence of attacks. SOCs therefore monitor the monitoring: each source has an expected volume, and a sharp drop raises its own alert. Redundant collectors, dual power supplies and separate network paths reduce the chance that one failure blinds a whole site.

### 3.5 Time and clocks

Clocks drift because oscillators are physical devices. NTP keeps them close, but drift of seconds can reorder events across hosts. NIST SP 800-92 stresses time synchronisation in log management.

Order matters in investigations: did the login come before the file access or after? Network Time Protocol adjusts each clock against reference servers, typically keeping drift to milliseconds on a healthy network. Logs should record times in UTC with the zone stated, so events from different regions can be compared without conversion mistakes.

### 3.6 Case link

The Lindqvist portal logs come from three web servers. One server's clock is 4 seconds fast, so failures logged there appear slightly later than they happened.

Four seconds sounds trivial, but during a burst of several attempts per second it reorders events across servers. A success on another server could appear to happen before the failures that preceded it. Amara notes the offset in her analysis and corrects for it rather than editing the logs, and the operations team fixes the server's time synchronisation.

### Electromagnetic and physical security

Physical access to network closets lets someone add a tap or unplug a sensor. Sensors, collectors and their cabling are part of the monitored estate and need locks and tamper alarms.

### Worked example

Amara compares the portal's 5-minute flow summaries with per-request web logs. Flows show one large record for 203.0.113.0/24 at 10:05; the web logs show 600 attempts spread over 40 seconds inside it. She notes that flow data detected the burst but could not show its pace.

> **Synthetic case.** Servers and figures are invented.

### Errors and limits

Physical analogies help intuition but telemetry noise is not random in the physical sense; it follows business patterns.

### Exercises

- **EX007 — Sampling effect.** What happens to a 20-second burst in 5-minute flow summaries? *Rubric:* 3 = smeared into one record; pace lost; 2 = partial; 1 = vague; 0 = none.
- **EX008 — Clock drift.** Why does a 4-second clock error matter? *Rubric:* 3 = reorders events across hosts; time sync needed (SP 800-92); 2 = partial; 1 = it does not; 0 = none.
- **EX009 — Physical capacity.** How does physics limit telemetry retention? *Rubric:* 3 = power, cooling, space and disk limit servers and storage; 2 = one factor; 1 = vague; 0 = none.

### Synthesis

Physical limits on sampling, clocks and infrastructure shape what telemetry a SOC can collect and trust.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small programs that read and summarise log records; (2) use variables, loops, conditions and functions; (3) test a program on known input; (4) keep code readable for reviewers.

### 4.1 Programs as precise procedures

A program is a procedure a computer follows exactly. In a SOC, small programs count, filter and summarise records faster and more consistently than people. Because they are exact, mistakes in them are repeated exactly too, so they must be tested.

A person counting failed logins by eye might miss a few lines or count one twice, and each count would differ slightly. A program gives the same answer every time, which is reassuring when it is right and dangerous when it is wrong. That is why SOC scripts are reviewed and tested like any other engineering artefact before analysts rely on their output.

### 4.2 Core constructs

Variables hold values such as a count. Loops visit every record. Conditions choose what to count. Functions package a step, such as "extract the /24 network from an address", so it can be reused and tested alone.

Amara's first script uses all four: a dictionary of counts keyed by network, a loop over log lines, a condition selecting failed logins and a function returning the /24 prefix. Keeping the prefix step in its own function means she can test it with tricky addresses, such as ones at the edge of a range, without running the whole script.

### 4.3 Reading records

Logs arrive as lines of text or structured records. A program splits each line into fields, converts types (text to numbers or times) and handles malformed lines without crashing, recording how many were skipped.

Real logs contain truncated lines, unexpected encodings and fields in odd formats. A script that crashes on the first bad line gives no answer at all; one that silently ignores bad lines may give a wrong one. Counting skipped lines and reporting them alongside results lets the reader judge whether the data were clean enough to trust.

### 4.4 Testing on known input

Before running on real logs, Amara feeds her function five hand-made lines whose correct answer she already knows. If the output differs, the code is wrong, not the data.

Her five lines include an ordinary failure, a success, a malformed line, an address at the boundary of a /24 range and a line with a time from a different zone. Each tests one possible mistake. When the first run counts the malformed line as a failure, she fixes the parser and reruns before touching real data.

### 4.5 Readability

Short functions, clear names and comments on intent help Paolo review her code. Code that only its author understands is a risk in operations.

In a SOC, scripts are often run at 3 a.m. by someone other than their author, during an incident. A function named `failed_logins_by_network` explains itself; one named `proc2` does not. Comments should say why a step exists, for example that one log source writes local time, rather than restating what the code does.

### 4.6 Standard library first

Python's standard library reads CSV, JSON and dates. Using it avoids installing unreviewed packages on SOC machines.

Every installed package is code from outside the organisation running on machines that see sensitive data. Each one needs review, updates and trust in its maintainers. For counting, filtering and parsing common formats, the standard library is enough, and SOC machines stay simpler to secure and rebuild. Larger tools are added deliberately when a real need appears. Paolo keeps a short list of approved packages, each with a named owner who tracks its updates.

### Version control

Amara keeps her scripts in the team's version-control repository. Each change has a message explaining why, and Paolo reviews changes before they run on production data. History lets the team see which version produced a given result.

### Worked example

Amara's first function returns the /24 network for an IPv4 address. Her test cases include "203.0.113.14" → "203.0.113.0/24" and a malformed "203.0.113" which must return None rather than crash. One test fails at first because she forgot the malformed case; she fixes it before using the function on portal logs.

> **Synthetic case.** Code and data are synthetic.

### Errors and limits

Passing tests show the code handles the cases you thought of, not all cases; add tests when new inputs surprise you.

### Exercises

- **EX010 — Malformed lines.** How should a log program treat malformed lines? *Rubric:* 3 = skip without crashing and count skipped lines; 2 = skip only; 1 = crash; 0 = none.
- **EX011 — Known-input testing.** Why test on hand-made lines first? *Rubric:* 3 = correct answer known, so differences reveal code errors; 2 = partial; 1 = no reason; 0 = none.
- **EX012 — Standard library.** Why prefer the standard library on SOC machines? *Rubric:* 3 = avoids unreviewed third-party packages; already available; 2 = partial; 1 = speed; 0 = none.

### Synthesis

Small, tested, readable programs make log analysis consistent; their exactness is a strength only when they are checked.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write clear technical notes, tickets and design documents; (2) adapt communication to analysts, managers and customers; (3) present data honestly with tables and charts; (4) use precise language for uncertainty.

### 5.1 Audiences

Analysts need exact fields and times; managers need impact and decisions; customers need what happened and what to do. One incident produces several documents, each written for its reader.

Writing one document for all three fails each of them: analysts lose detail, managers drown in it, customers get jargon. Amara starts each piece by asking what the reader must do after reading it. That question decides what to include, from field names for the analyst to a single recommended decision for the manager.

### 5.2 Tickets

A good SOC ticket states what was observed, when (with time zone), on which assets, what was done, and what is still unknown. Knerler, Parker and Zimmerman (2022) emphasise clear communication as a SOC strategy in its own right.

Stating what is unknown is the part most often skipped, yet it tells the next shift where to look. A time without a zone forces a reader to guess, and a wrong guess can reorder the story. Assets should be named by identifiers the asset inventory uses, so other teams can find them without asking.

### 5.3 Design documents

Engineering changes, such as a new detection, need a short design document: problem, proposal, alternatives, risks, test plan and rollback.

Writing alternatives forces the author to show why the proposal beats other options, not just that it works. A test plan states how the detection will be shown to fire on the target behaviour and stay quiet on normal activity. Rollback explains how to remove the change quickly if it floods the queue after deployment. Paolo reviews each document before the rule goes live.

### 5.4 Honest charts

Charts must start axes at zero for counts, label units and time zones, and avoid smoothing away spikes that matter.

A count axis starting at 900 can make a rise from 950 to 1,000 look like a doubling. Unlabelled time zones can shift a spike into the wrong shift. Smoothing with a long moving average makes trend lines look tidy but can erase the very burst an incident chart is meant to show, so raw counts should appear alongside any smoothed line. Captions state the data source.

### 5.5 Words for uncertainty

"Confirmed", "likely" and "possible" should be used consistently. Amara's team defines them in a style guide so readers know how sure the writer is.

Without agreed meanings, one writer's 'likely' is another's 'possible', and a manager may act on a stronger claim than the evidence supports. The style guide links each word to the evidence expected: 'confirmed' needs direct evidence such as a log entry, 'likely' needs several consistent indicators, and 'possible' marks a lead not yet checked. The guide fits on one page.

### 5.6 Case

After the portal burst, Amara writes three items: the analyst ticket, a manager summary and a draft customer notice for account u5's owner, reviewed by Paolo and the communications team.

The ticket lists the failure counts, the network, u5's successful login time and session actions, with times in UTC. The manager summary gives the impact in two sentences and states what has already been done and the change now proposed. The customer notice explains in plain words that unusual sign-in activity was seen and what the customer should do.

### Review before sending

Anything leaving the SOC is reviewed by a second person: one checks facts against the ticket, the other checks tone and clarity. For customer notices, the communications team approves the final wording, because a misleading notice can do more harm than the incident itself. Amara keeps the reviewed versions with the ticket.

### Worked example

Amara's manager summary: "On Monday 10:05–10:06 UTC, about 600 login attempts from one network targeted customer portal accounts. One customer account was accessed successfully and has been locked; the customer has been contacted. No staff systems were affected. A rate-limit change is proposed."

> **Synthetic case.** The incident and texts are invented.

### Errors and limits

Clear writing cannot fix wrong facts; check figures against sources before sending.

### Exercises

- **EX013 — Ticket fields.** List five things a good SOC ticket states. *Rubric:* 3 = observed, time with zone, assets, actions, unknowns; 2 = three; 1 = one; 0 = none.
- **EX014 — Uncertainty words.** Why define "confirmed", "likely" and "possible" in a style guide? *Rubric:* 3 = consistent meaning lets readers know certainty; 2 = partial; 1 = style only; 0 = none.
- **EX015 — Manager summary.** What does Amara's summary include and leave out? *Rubric:* 3 = time, scale, impact, actions, proposal; leaves out raw technical detail; 2 = partial; 1 = copy of ticket; 0 = none.

### Synthesis

Communicate for each reader, with precise uncertainty and honest charts; clarity is part of SOC engineering.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use integrals to total quantities over time; (2) apply exponential growth and decay to log volumes and retention; (3) use series approximations for capacity planning; (4) connect continuous models to storage costs.

### 6.1 Integrals as totals

Storage needed for logs is the integral of ingestion rate over the retention period. If a SIEM ingests r(t) gigabytes per day, storage after T days is the area under r(t) from 0 to T.

When the rate is constant, the area is just a rectangle: rate times days. Real ingestion rises on weekdays, falls at weekends and jumps during incidents, so the area has an uneven top edge. Summing daily figures from the SIEM's own volume reports gives the area directly, and comparing that sum with the rectangle estimate shows how much the simple model misses.

### 6.2 Exponential growth

If log volume grows 3% per month, volume after n months is V₀·1.03ⁿ. After two years it is about double. Capacity plans that assume flat volume fail.

The doubling comes from 1.03²⁴ ≈ 2.03. A useful shortcut is the rule of 70: dividing 70 by the percentage growth rate gives the approximate doubling time, here about 23 months. Growth like this comes from new systems being connected, more verbose logging after incidents and business expansion, so it tends to continue unless someone deliberately trims sources. Amara plots both projections.

### 6.3 Decay

Value of old logs decays: most investigations use recent data. A simple model treats the chance of needing a day's logs as decaying exponentially with age, informing tiered storage — hot, warm, cold.

Under such a model, if the chance of needing a given day halves every month, logs three months old are needed an eighth as often as fresh ones. That suggests fast, expensive storage for recent data and slower, cheaper storage later. The model is a simplification: some investigations, such as slow insider cases, reach far back, which is why cold storage is kept searchable rather than discarded.

### 6.4 Approximations

For small growth rates, (1 + g)ⁿ ≈ 1 + ng for short periods, a quick check on spreadsheets.

At 3% over three months, the linear estimate gives 9% against an exact 9.27%, close enough for a sanity check. Over two years it gives 72% against an exact 103%, badly wrong. The approximation's value is in catching gross spreadsheet errors quickly, such as a misplaced decimal, not in replacing the exact calculation for planning. Amara uses it to check her storage spreadsheet: a 3% monthly rise over one quarter should add roughly 9% to ingestion, and a cell showing 90% would point straight to a misplaced decimal.

### 6.5 Case

Lindqvist's SIEM ingests 120 GB per day and keeps 90 days hot. Paolo asks Amara whether the current 12 TB hot tier will last a year if volume grows 3% monthly.

The question has two parts: how much hot storage today's rate needs, and how that need changes as ingestion grows over the year. Amara sets it up as a rate multiplied by the retention window, first at today's rate and then at the rate a year from now. She notes that the hot tier holds a rolling window, so what matters is the ingestion rate at the time, not the total collected during the year.

### 6.6 Retention rules

Retention is also set by policy and law; NIST SP 800-92 recommends defining retention per log type. Maths informs cost; policy decides minimums.

A log type needed for regulatory audits may have to be kept for years, even if investigations rarely touch it; debug logs from a test system may be kept for days. The SOC proposes retention based on investigative value, legal and compliance teams set minimums, and storage cost shapes which tier each type sits in for each part of its life.

### Rates of change in cost

The derivative of storage cost with respect to retention days is the daily ingestion cost. Seeing cost as a rate helps managers compare keeping ten more days of logs against other uses of the budget. Amara presents both the total and the marginal cost for each log type, so decisions can be made source by source rather than all at once.

### Worked example

Amara computes today's hot need: 120 GB × 90 = 10.8 TB. In 12 months ingestion is 120 × 1.03¹² ≈ 171 GB/day, so 90 days need about 15.4 TB, exceeding 12 TB. She recommends moving firewall logs older than 30 days to the warm tier.

> **Synthetic case.** Volumes and tiers are invented.

### Errors and limits

Growth rarely follows a smooth curve; new log sources add steps. Revisit plans quarterly.

### Exercises

- **EX016 — Storage integral.** Express storage as an integral and compute today's hot need. *Rubric:* 3 = area under ingestion over retention; 10.8 TB; 2 = one part; 1 = wrong; 0 = none.
- **EX017 — Growth effect.** What hot storage is needed in 12 months at 3% monthly growth? *Rubric:* 3 = about 171 GB/day, 15.4 TB, exceeds 12 TB; 2 = partial; 1 = flat assumption; 0 = none.
- **EX018 — Policy versus maths.** What decides minimum retention, and what does maths decide? *Rubric:* 3 = policy/law sets minimum; maths informs cost and tiering; 2 = partial; 1 = maths decides all; 0 = none.

### Synthesis

Integrals and growth models turn ingestion rates into storage plans, within retention limits set by policy.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) apply Bayes' rule to alert precision; (2) distinguish false-positive rate from precision; (3) summarise data with medians and percentiles; (4) recognise base-rate effects.

### 7.1 Conditional probability

Two questions are easy to confuse. "If an attack happens, how likely is an alert?" is the true-positive rate. "If an alert fires, how likely is an attack?" is precision. Bayes' rule connects them through the base rate.

Confusing them leads to bad decisions. A vendor may advertise that its detector catches 99% of attacks, which is the true-positive rate, while analysts experience something different: most alerts they open turn out to be benign. Bayes' rule shows how both can be true at once, because precision depends heavily on how rare attacks are among the events being judged.

### 7.2 Base rates

Axelsson (2000) showed that when attacks are rare among events, even a good detector produces mostly false alarms. Precision falls as prevalence falls.

Axelsson's argument applied this to intrusion detection systems at a time when vendors focused on detection rates. Suppose only one event in ten thousand is malicious; even a false-positive rate of one in a thousand produces ten false alarms for each real one. The practical lesson is that false-positive rates must be extremely low, or alerts must be filtered further before reaching people.

### Lab — Bayes for one rule

```python
"""Bayes' rule for one detection rule at Lindqvist Freight (synthetic figures)."""
p_attack = 0.002          # share of evaluated logon bursts that are credential stuffing
tpr, fpr = 0.90, 0.01
p_alert = tpr * p_attack + fpr * (1 - p_attack)
ppv = tpr * p_attack / p_alert
print(f"P(alert)={p_alert:.5f}  P(attack|alert)={ppv:.3f}")
print(f"per 100,000 bursts: true alerts={tpr*p_attack*1e5:.0f} false alerts={fpr*(1-p_attack)*1e5:.0f}")
```

Run with `python3 lab_bayes.py`. Verified output:

```text
P(alert)=0.01178  P(attack|alert)=0.153
per 100,000 bursts: true alerts=180 false alerts=998
```

### 7.3 Reading the result

With 0.2% of logon bursts being credential stuffing, a 90% true-positive rate and a 1% false-positive rate, precision is 0.153: about one alert in seven is real. Per 100,000 bursts, 180 true and 998 false alerts are expected.

Seeing the counts makes the point vivid: 998 false alarms against 180 real ones. Halving the false-positive rate to 0.5% would cut false alarms to 499 and raise precision to about 0.27, so improving specificity pays off more than improving detection here. Amara checks the arithmetic by building the full table of attacks and non-attacks before trusting the formula's output.

### 7.4 Summaries

Triage times are skewed: most are quick, a few take hours. Medians and 90th percentiles describe them better than means.

A few long investigations can drag the mean far above what a typical alert takes, giving a misleading picture of daily work. The median says what a typical alert costs; the 90th percentile shows how long the slow ones run, which matters for staffing. Amara reports both, with the number of alerts in the sample, so readers can see how solid the figures are.

### 7.5 Using statistics

Amara uses these numbers to argue that the burst rule needs a second condition (a success in the burst) to raise precision before paging analysts at night.

Requiring a success within the burst changes the base rate: bursts with a success are a far smaller, more suspicious group, so a much larger share of alerts that fire on them are real. The trade-off is that attacks which fail entirely no longer page anyone at night. Amara proposes logging those to a daytime review queue so they are still seen.

### Intervals for rates

An observed false-positive rate of 1% from 2,000 benign bursts has uncertainty: the true rate might be somewhat higher or lower. Amara reports rates with 95% intervals and notes the sample size, so readers do not treat 1% as exact. When samples are small, she says so and avoids decisions that depend on fine differences between rules. Paolo asks every rule proposal to include the sample on which its rates were measured.

### Worked example

Paolo asks: "If we halve the false-positive rate, what happens?" Amara recomputes with 0.5%: precision rises to about 0.27. Halving false positives nearly doubles the share of real alerts, which is more useful than raising sensitivity from 90% to 95%.

> **Synthetic case.** Rates come from the lab script; the 0.5% case is her recalculation.

### Errors and limits

Rates estimated from small samples are uncertain; report intervals when possible.

### Exercises

- **EX019 — Two questions.** Distinguish true-positive rate from precision. *Rubric:* 3 = P(alert given attack) vs P(attack given alert); 2 = partial; 1 = same; 0 = none.
- **EX020 — Lab precision.** What precision does the lab give, and what does it mean? *Rubric:* 3 = 0.153; about 1 in 7 alerts real; 180 vs 998; 2 = number only; 1 = wrong; 0 = none.
- **EX021 — Which lever.** Why is halving the false-positive rate worth more than raising sensitivity here? *Rubric:* 3 = base rate low: FP dominates; precision rises to about 0.27; 2 = partial; 1 = sensitivity better; 0 = none.

### Synthesis

Bayes' rule and base rates explain why precision, not just detection rate, decides whether a rule is useful.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) explain how CPU, memory, storage and I/O shape telemetry; (2) relate processes and privilege to endpoint events; (3) reason about performance costs of sensors; (4) identify architectural sources of evidence.

### 8.1 Components

A computer runs instructions on a CPU, keeps working data in memory, stores files on disks and talks to the world through input/output devices. Each component can be observed: CPU use, memory regions, file writes and network packets.

Each observation point answers a different question. Process creation shows what ran; memory inspection can reveal code that never touched disk; file writes show what was changed or dropped; network packets show where data went. No single view sees everything, which is why SOCs combine endpoint, network and log data rather than relying on one source.

### 8.2 Privilege levels

Processors separate privileged kernel code from user programs. Endpoint detection agents often run partly in the kernel to see process creation and file activity reliably, which is powerful but means agent bugs can crash machines.

Code in the kernel can see and intercept activity that user programs cannot, including attempts to tamper with the agent itself. The same power means a faulty kernel component can halt the whole machine, so agent updates are rolled out in stages with test groups first. Engineers weigh visibility gained against the stability risk on critical servers.

### 8.3 Processes and threads

A process is a running program with its own memory; threads are paths of execution inside it. Endpoint telemetry records process creation, parent process and command line, which detections use heavily.

Parent–child relationships tell a story: a web server process starting a command shell is unusual and worth attention, while a user's desktop starting a browser is not. Detections that combine parent, child and command-line arguments are far more precise than ones that look at a process name alone.

### 8.4 Caches and performance

Sensors consume CPU cycles and memory. An agent that inspects every file write may slow a busy server. Engineers balance visibility against performance, testing on representative machines.

Inspecting every file write means intercepting it, examining it and letting it continue, which adds latency to busy disks. Agents often exclude known high-volume paths, such as database files, to reduce cost, but each exclusion is a blind spot attackers could use. Engineers test agents under realistic load and document every exclusion with its reason.

### 8.5 Storage paths

Logs pass from memory buffers to disk to network. A crash can lose buffered events. Knowing the path explains gaps after reboots.

Most logging systems buffer events in memory and write them in batches for efficiency. A sudden power loss or crash discards whatever was in the buffer. Forwarders may buffer again before sending across the network. Knowing where buffers sit helps an analyst explain why the last seconds before a crash are missing, rather than suspecting deletion. Forwarders with disk-backed queues lose less.

### 8.6 Firmware

Below the operating system lies firmware. Changes there are rarely visible to normal telemetry, so integrity checks and vendor updates matter.

Firmware runs before the operating system starts and can influence everything after it, which makes changes there especially serious. Normal endpoint agents start too late to observe much of it. Defenders rely on measured boot, vendor signature checks on updates and comparison of firmware versions against expected values across the fleet. Unexpected version differences between identical servers are investigated, not dismissed.

### 8.7 Case

Lindqvist's portal servers run an endpoint agent. During the burst, CPU on one server reaches 95%, mostly from the web service, not the agent; Amara checks before blaming the sensor.

Blaming the agent would have been an easy guess, since sensors are often suspected when servers slow down. Amara checks per-process CPU figures and sees the web service consuming most of it while answering the flood of login attempts. The agent's share stays small. The finding points to rate limiting on the portal rather than tuning the sensor.

### Worked example

Paolo asks why the portal server lost 30 seconds of agent events at 10:06. Amara reads the agent's health log: the event buffer filled while the network link was saturated by the burst, and older events were dropped. She proposes a larger buffer and a health alert when drops occur.

> **Synthetic case.** Servers and logs are invented.

### Errors and limits

Architecture knowledge explains where data can be lost, but each product behaves differently; read vendor documentation.

### Exercises

- **EX022 — Kernel agents.** Why do many endpoint agents run partly in the kernel, and what is the risk? *Rubric:* 3 = reliable visibility of process/file events; bugs can crash systems; 2 = one side; 1 = vague; 0 = none.
- **EX023 — Lost events.** Explain the 30-second event loss at 10:06. *Rubric:* 3 = buffer filled during network saturation; older events dropped; 2 = partial; 1 = agent bug guess; 0 = none.
- **EX024 — Performance trade.** How do engineers decide how much a sensor may inspect? *Rubric:* 3 = balance visibility vs CPU/memory; test on representative machines; 2 = partial; 1 = maximum always; 0 = none.

### Synthesis

Architecture explains what telemetry exists, what it costs and where it can be lost.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure larger programs into modules; (2) use data structures for efficient lookups; (3) handle errors and edge cases deliberately; (4) write unit tests for detection logic.

### 9.1 From scripts to programs

As Amara's tools grow, she separates parsing, logic and output into modules. Each can be tested and replaced without touching the others.

A single long script mixes concerns: changing the output format risks breaking the parser. Modules with clear boundaries let Amara swap the parser for a new log format while the counting logic stays untouched and tested. The structure also lets Paolo review one module at a time, which keeps reviews short and focused. Each module has its own tests, and a small main program ties them together.

### 9.2 Data structures

Dictionaries give fast lookups — for example, mapping a username to its failure count. Sets answer membership questions quickly. Choosing the right structure turns minutes into seconds on large logs.

Looking up a username in a list means scanning every entry until a match appears; with a million entries, that is slow when repeated for every log line. A dictionary jumps to the entry almost directly. Sets do the same for 'have I seen this before?' questions, which detection logic asks constantly, such as whether an address is already on a watch list.

### 9.3 Errors

Programs meet missing fields, odd encodings and huge lines. Deliberate handling — catching specific errors, counting them and continuing — keeps analyses complete and honest.

Catching every error with one broad handler hides real bugs, such as a mistyped variable name. Catching specific errors, such as a value that cannot be parsed as a time, handles expected problems while letting unexpected ones surface. The count of handled errors goes into the output so readers know how many records were set aside. Silence is worse.

### 9.4 Unit tests

Python's unittest module lets Amara write tests such as "five failures for distinct users in one network should trigger; four should not". Tests run automatically before each change is merged.

A pair of tests on either side of the threshold pins down exactly where the rule's behaviour changes. Running tests automatically before merging means a later change that shifts the threshold by accident fails immediately, rather than being discovered when a real attack slips through. Tests also serve as documentation of what the rule is meant to do.

### 9.5 Edge cases

Boundary values (exactly the threshold), empty input and duplicate events are where detection code usually breaks. Tests target them first.

A rule that triggers on 'more than five' and one that triggers on 'five or more' differ only at exactly five, and that is where bugs hide. Empty input tests that the code reports nothing rather than crashing. Duplicate events, common when a log forwarder retries, test that the same failure is not counted twice. Amara lists these cases before writing the rule, not after a bug appears.

### 9.6 Performance

For a day of portal logs (2 million lines), reading line by line uses little memory; loading all into a list may exhaust it.

Two million lines of a few hundred bytes each can occupy far more memory once each line becomes a separate Python object. Reading one line at a time and updating counters keeps memory use flat. Amara measures both approaches on a sample day and records the peak memory of each, which justifies the streaming design in the review.

### 9.7 Reviews

Paolo reviews code for correctness and clarity; a second pair of eyes catches logic slips that tests missed.

Tests check what the author thought to test; a reviewer asks about what was not considered. Paolo spots that Amara's code treats usernames as case-sensitive while the portal does not, so 'U5' and 'u5' were counted separately. A test is added for that case, and the review notes become a checklist for future detection code. Reviews are logged with the reviewer's name, so later readers know someone checked the code before it went live.

### Logging inside tools

Amara's tools log their own actions: input file, its hash, records read, records skipped and output written. When a result is questioned weeks later, the tool's log shows exactly what it processed. This self-logging costs a few lines of code and saves hours of doubt.

### Worked example

Amara's test for "exactly 5 failures" fails: her code uses "> 5" while the design says "at least 5". She asks Paolo which is intended; they choose "≥ 5", update the design document and the code together, and keep the test.

> **Synthetic case.** Tests and data are synthetic.

### Errors and limits

Tests encode understanding at the time written; if the threat changes, tests may enforce outdated logic.

### Exercises

- **EX025 — Data structure choice.** Which structure suits counting failures per user, and why? *Rubric:* 3 = dictionary: fast keyed updates; 2 = partial; 1 = list; 0 = none.
- **EX026 — Boundary bug.** What did the "exactly 5" test reveal, and how was it fixed? *Rubric:* 3 = code used > 5 vs design ≥ 5; aligned design, code and test; 2 = partial; 1 = ignored; 0 = none.
- **EX027 — Streaming.** Why read large logs line by line? *Rubric:* 3 = low memory use; avoids exhausting memory; 2 = partial; 1 = faster always; 0 = none.

### Synthesis

Structured code, suitable data structures and tests on edge cases make detection logic reliable.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering ethics to security operations; (2) balance monitoring with privacy; (3) handle conflicts between speed and safety; (4) report concerns responsibly.

### 10.1 Duties

Engineers owe duties to the public, employers and colleagues. In a SOC, monitoring protects people but also observes them. Ethical practice means collecting what the purpose requires and no more.

Duty to the public includes the customers whose accounts are protected and whose data passes through monitored systems. Duty to the employer means doing competent, honest work. Duty to colleagues means not monitoring them beyond what policy permits. Collecting only what the purpose requires limits the harm if monitoring data is ever misused or leaked.

### 10.2 Privacy and monitoring

Staff and customers have privacy interests. Lindqvist's monitoring policy tells staff what is monitored and why; SOC access to content (such as email bodies) needs case approval.

Telling staff what is monitored is both fair and practical: people who know the rules are less likely to feel betrayed when monitoring reveals a problem. Metadata, such as who emailed whom and when, is less intrusive than content. Requiring case approval before reading content keeps the more intrusive step tied to a specific, justified need.

### 10.3 Safety of actions

Response actions can harm operations: blocking a network might stop delivery trucks' route updates. Engineers consider side effects and use approved playbooks.

Lindqvist's trucks depend on network access for route and delivery updates, so cutting a network segment during a response could strand drivers or delay shipments. Playbooks list known dependencies for each action and who must be told before it is taken. Where risk is high, a narrower action, such as blocking one address, is tried before a broad one.

### 10.4 Honesty

Reports must not hide failures, such as a missed detection, even when embarrassing. Hiding them prevents learning.

A missed detection is information: it shows a gap in data, logic or process. Reporting it lets the team fix the gap and lets managers judge risk accurately. Concealing it leaves the gap open and erodes trust when it surfaces later, which it often does during the next incident's review. At Lindqvist, missed detections appear in the monthly report with what was changed afterwards, so the same gap is visibly closed rather than quietly forgotten.

### 10.5 Conflicts

When a manager asks for monitoring of one employee without an investigation request, Amara declines and refers to policy and HR process.

Monitoring a single employee without a formal request could serve a personal dispute rather than a security need and may break employment law or the monitoring policy. Amara does not judge the manager's motives; she explains the process and points to HR, which can open an investigation if one is warranted. She records the request and her response.

### 10.6 Raising concerns

If a practice seems unsafe or unlawful, engineers raise it through defined channels, documenting facts.

Defined channels include the line manager, the security lead, the compliance team and, where these fail, any whistle-blowing route the organisation provides. Documenting facts rather than opinions keeps the concern specific and checkable. Raising it early, before harm occurs, gives the organisation a chance to fix the practice quietly. Amara learns where Lindqvist's whistle-blowing policy is published during her first week. Retaliation against someone raising a concern in good faith is itself a breach of most codes and many laws.

### 10.7 Professional codes

Engineering and computing bodies publish codes stressing public good, competence and honesty; Amara reads her university's code during induction.

Codes are short and general, so they guide judgement rather than replacing it. Amara notes three points relevant to her placement: act within her competence, be honest about results and limits, and put public safety ahead of convenience. She refers back to them when the monitoring request in her placement tests those principles. Membership bodies can discipline members who breach them, which gives the codes weight.

### Consent and transparency

Customers are told in the portal's privacy notice that login activity is logged for security. Transparency does not replace minimisation, but it lets people understand monitoring and complain if it is misused. The SOC reviews the notice with legal staff each year so it matches real practice.

### Worked example

During the portal incident, a colleague suggests blocking the whole 203.0.113.0/24 range permanently. Amara notes that the range belongs to a cloud provider also used by a logistics partner. Paolo agrees to a temporary block with monitoring and a review after 24 hours, documented in the ticket.

> **Synthetic case.** The situation and people are invented.

### Errors and limits

Ethics guides judgement but does not give automatic answers; discuss hard cases with supervisors.

### Exercises

- **EX028 — Minimal collection.** What does "collect what the purpose requires" mean in a SOC? *Rubric:* 3 = monitor for defined purpose, no extra content without approval; 2 = partial; 1 = collect all; 0 = none.
- **EX029 — Declining a request.** Why did Amara decline monitoring one employee? *Rubric:* 3 = no investigation request; refer to policy and HR; 2 = partial; 1 = complied; 0 = none.
- **EX030 — Range block.** Why was the permanent block rejected? *Rubric:* 3 = range shared with partner; temporary block with review instead; 2 = partial; 1 = blocked; 0 = none.

### Synthesis

Ethical SOC engineering limits monitoring to its purpose, weighs side effects of actions and reports honestly.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) explain addressing, ports and common protocols; (2) read network telemetry such as flows and web logs; (3) aggregate activity by network; (4) recognise limits of IP-based attribution.

### 11.1 Layers

Networks move data in layers: physical links, IP addressing and routing, TCP or UDP transport, and applications such as HTTPS. Telemetry exists at each layer: link statistics, flow records, and application logs.

Each layer answers different questions. Link statistics show whether a cable or port is saturated; flow records show who talked to whom, for how long and how many bytes moved; application logs show what was asked for and what came back. During the portal burst, flows reveal the volume from one network, but only the web server logs show which usernames were tried.

### 11.2 Addresses and networks

IPv4 addresses are grouped into networks by prefix. A /24 network shares its first three octets. Attack traffic from one hosting provider often spans many addresses in a few networks, so aggregating by network reveals bursts that per-address counts hide.

Counting per address can make a distributed attack look harmless: fifty addresses with two attempts each never trip a per-address threshold of five. Grouping by /24 collapses them into one network with a hundred attempts. The choice of prefix length is a trade-off, since a wider prefix catches more spread-out activity but also merges unrelated customers behind the same provider.

### Lab — failures by network

```python
"""Count failed portal logins by source /24 network and by distinct usernames (synthetic)."""
from collections import defaultdict
log = [("203.0.113.10","u1","fail"),("203.0.113.11","u2","fail"),("203.0.113.12","u3","fail"),
       ("203.0.113.13","u4","fail"),("203.0.113.14","u5","ok"),("198.51.100.20","u6","fail"),
       ("198.51.100.20","u6","fail"),("198.51.100.20","u6","ok"),("203.0.113.15","u7","fail"),
       ("203.0.113.16","u8","fail")]
fails = defaultdict(int); users = defaultdict(set)
for ip, user, res in log:
    net = ".".join(ip.split(".")[:3]) + ".0/24"
    users[net].add(user)
    if res == "fail": fails[net] += 1
for net in sorted(fails):
    print(f"{net:17} failures={fails[net]} distinct_users={len(users[net])}")
```

Run with `python3 lab_failed.py`. Verified output:

```text
198.51.100.0/24   failures=2 distinct_users=1
203.0.113.0/24    failures=6 distinct_users=7
```

### 11.3 Reading the result

The 203.0.113.0/24 network produced 6 failures, one each against six usernames, and touched 7 distinct usernames in all once u5's success is counted — many accounts, few attempts each, the pattern of credential stuffing. 198.51.100.0/24 shows 2 failures and a success for one user: a customer mistyping a password.

The pattern matters more than the totals. Many usernames with one attempt each suggests someone working through a list of leaked credentials, hoping some customers reused passwords. A single username with a couple of failures and then a success looks like an ordinary person who forgot which password they used. A rule that only counted failures would treat both networks alike and miss that distinction.

### 11.4 HTTPS visibility

Encrypted web traffic hides content from network sensors; the web server's own logs show paths, status codes and usernames. Choosing where to observe is an engineering decision.

Breaking encryption on the network to inspect content is possible with interception proxies, but it adds risk, cost and privacy concerns. For the portal, the server already sees decrypted requests, so its logs are the natural place to observe logins. Network sensors still help with volume and timing, while the server logs supply the meaning of each request.

### 11.5 Attribution limits

An address identifies a connection point, not a person. Shared proxies, cloud ranges and address reuse make blocking and attribution imprecise.

Many customers may share one address behind a mobile carrier's gateway, so blocking it can lock out innocent users. Attackers rent cloud servers and abandon them within hours, so an address that was hostile yesterday may belong to someone else tomorrow. SOC reports therefore describe addresses as sources of activity rather than naming who was behind them. Blocks on addresses are given expiry dates.

### 11.6 Protocol knowledge

Knowing that login uses POST to /login and returns 401 on failure lets Amara write accurate parsing.

Without that knowledge, a parser might count every request to the login page, including people simply loading the form, as an attempt. Knowing the method, path and status codes lets Amara count only submitted credentials and separate failures from successes. She confirms the details with the portal developers rather than guessing from a sample, since a redirect after login could hide the real outcome.

### DNS and time

DNS logs show which names hosts look up, often revealing contacts before connections happen. Network devices must share synchronised time so flows, DNS and web logs line up; without it, correlation across layers becomes guesswork.

### Worked example

Amara notices that one address, 203.0.113.14, produced the success for u5. She checks the web log: the same session then requested /account/address with a change at 10:07. She adds this to the ticket as a possible account takeover action.

> **Synthetic case.** Addresses use documentation ranges; events are synthetic.

### Errors and limits

Aggregating by /24 can merge unrelated users of large providers; confirm with other signals.

### Exercises

- **EX031 — Network aggregation.** Why aggregate failures by /24 network? *Rubric:* 3 = bursts spread over many addresses appear together; 2 = partial; 1 = no reason; 0 = none.
- **EX032 — Stuffing pattern.** Which network shows credential stuffing, and why? *Rubric:* 3 = 203.0.113.0/24: many users, few attempts each; 2 = network only; 1 = wrong; 0 = none.
- **EX033 — Follow-up action.** What did the successful session do next? *Rubric:* 3 = requested address change at 10:07; possible takeover; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Network telemetry gains meaning through aggregation and protocol knowledge, within the limits of IP attribution.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) explain how operating systems manage processes, files, users and logs; (2) locate key security events on Windows and Linux; (3) relate OS audit settings to detection coverage; (4) recognise how configuration changes telemetry.

### 12.1 What an OS does

The operating system schedules processes, manages memory, controls access to files and devices, and authenticates users. Every one of these functions can produce security events if auditing is enabled.

Auditing turns these background functions into records: a process starting, a file opened, a user signing in. Most systems ship with only part of this enabled, because full auditing produces large volumes and some performance cost. Choosing which functions to audit is therefore a design decision tied to the detections the SOC intends to run.

### 12.2 Windows events

Windows records logons, process creation, service installation and policy changes in its event logs when audit policy enables them. Process creation with command line, for example, must be switched on deliberately; without it, many endpoint detections have nothing to match.

A default installation may record that a process started but not the command line it was given, which is where much of the useful detail lives. Group Policy lets administrators enable auditing consistently across many machines. Amara checks a sample of portal servers and finds the command-line setting is not applied uniformly, a gap her coverage table later traces to an older build template.

### 12.3 Linux logs

Linux systems record authentication in system logs, and the audit subsystem can record file access and program execution according to rules. Like Windows, coverage depends on configuration.

Authentication messages land in files such as the system's auth log or in the systemd journal, depending on the distribution. The audit subsystem uses rules that name what to watch, for example execution of any program by a web service account. Each rule adds volume, so rules are written for specific risks rather than recording everything the system does.

### 12.4 Users and privilege

Operating systems separate normal users from administrators. Events that change privilege — adding a user to an administrators group, for instance — are high-value signals for detection.

Attackers who gain a foothold usually want more rights, so changes in group membership often appear early in an intrusion. Such changes are also rare in normal operations, which makes them good detection candidates with few false positives. Legitimate changes still occur, so alerts are checked against the change-management record for an approved request. Removals from privileged groups are logged too.

### 12.5 Services and scheduled tasks

Programs can be set to start automatically. New services and scheduled tasks are common persistence mechanisms described in MITRE ATT&CK, so their creation is worth logging.

Persistence lets an attacker's program survive a reboot or a user logging out. Legitimate software also installs services, especially during updates, so a raw alert on every new service would be noisy. Detections narrow it down, for example to services running from user-writable folders or tasks created by unusual parent processes, and analysts compare against known software deployments.

### 12.6 Configuration as coverage

Detection coverage is only as good as audit configuration. Amara builds a table listing each detection rule and the OS setting it depends on, then checks that the settings are deployed by policy on every server class.

The table reveals gaps that rule testing alone would miss: a rule can pass its tests in the lab yet never fire in production because the event it needs is not generated there. Amara's check finds that one server class records process creation without the command line. Fixing the policy restores coverage for several rules at once, and the table is rechecked after every build change.

### 12.7 Log size and rotation

Event logs have maximum sizes; when full, old events are overwritten. Forwarding logs to the SIEM promptly prevents loss.

On a busy server, a small event log can wrap in hours, so evidence of an attack in the morning may be gone by the afternoon. Attackers sometimes generate noise deliberately to push older entries out. Forwarding events to the SIEM within seconds keeps a copy outside the host, and alerts on forwarding gaps show when a server stops sending. Log size settings are part of the build standard.

### Worked example

Amara's table reveals that the portal web servers lack command-line logging for process creation because they were built from an older template. Three detection rules therefore could never fire on those servers. Paolo raises a change to update the template and verifies afterwards with a harmless test process.

> **Synthetic case.** Servers, templates and rules are invented.

### Errors and limits

Enabling more auditing increases volume and cost; enable what detections and investigations need.

### Exercises

- **EX034 — Coverage dependency.** Why can a detection rule never fire on some servers? *Rubric:* 3 = required audit setting (e.g. command-line logging) not enabled; 2 = partial; 1 = rule bug; 0 = none.
- **EX035 — Privilege events.** Why are group membership changes high-value signals? *Rubric:* 3 = they change privilege; attackers seek admin rights; 2 = partial; 1 = noise; 0 = none.
- **EX036 — Template fix.** How was the web server gap fixed and verified? *Rubric:* 3 = updated build template; harmless test process confirmed logging; 2 = partial; 1 = ignored; 0 = none.

### Synthesis

Operating systems produce rich security events only when configured to; mapping rules to settings reveals blind spots.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) model security data in tables and documents; (2) write queries that join and aggregate events; (3) design schemas for consistent fields; (4) reason about indexing and query cost.

### 13.1 Security data as data

A SIEM is a data system: it ingests records, stores them, indexes fields and answers queries. Good data design makes detections faster and more accurate.

Treating the SIEM as a data system brings in database ideas: schemas, indexes, query plans and capacity. A poorly designed table can make a simple question take minutes, which matters when an analyst is mid-incident. Amara learns to read query statistics, such as how many records were scanned to answer each search. Slow searches are then rewritten or indexed.

### 13.2 Schemas

If one source calls the user field "user", another "username" and a third "acct", every query must remember all three. Normalising fields to a common schema at ingestion — one name for user, source address, host, action and outcome — simplifies rules and reduces mistakes.

Normalising at ingestion means converting each source's fields once, when data arrives, rather than in every query that reads it. Values need the same care: one source may write 'FAIL', another 'failure', another a numeric code. The mapping for each source is documented and tested, because a mistake there silently breaks every rule that relies on the field.

### 13.3 Joins

Many questions join data: "which hosts did the account that logged in from 203.0.113.14 touch next?" joins web logs with internal authentication logs on username and time.

Joining on username alone can mislead if two systems spell names differently or if the same name belongs to a customer and an employee. Time adds a second key, limiting matches to events close together. Joins are often costly, so engineers filter each side first, for instance to the one suspect address, before combining them.

### 13.4 Aggregation

Counting, grouping and windowing (for example, per 10 minutes) are the core of threshold detections.

A threshold detection takes raw events, groups them by a key such as source network, counts them within a time window and compares the count with a limit. Fixed windows can split a burst across a boundary so neither half crosses the threshold. Sliding windows avoid that at higher computational cost, a trade-off Amara tests on the portal data. She records how many bursts each window type finds on the same day of data.

### 13.5 Indexes and cost

Indexed fields are fast to search; unindexed full-text searches are slow and expensive. Engineers index fields that detections and analysts use most, such as user, host and source address.

An index works like the index of a book: it points straight to records holding a given value, instead of reading every page. Each index takes storage and slows ingestion slightly. Choosing indexed fields from the queries analysts actually run, rather than indexing everything, keeps both search speed and storage cost under control.

### 13.6 Data quality

Missing values, wrong types and duplicates distort results. Quality checks at ingestion catch them early.

A time field parsed in the wrong zone can shift events by hours and break correlations; duplicate events can double counts and trigger thresholds falsely. Ingestion checks count records failing validation per source and alert when the rate jumps, which often signals a format change after a software update on the sending system. Each source has an owner who is told when its rejection rate rises, so the fix happens at the sender rather than through workarounds in every query.

### 13.7 Retention per table

Different tables may need different retention: authentication logs kept longer than verbose debug logs.

Authentication records help reconstruct account misuse months later, so they earn long retention. Verbose debug output is rarely useful beyond a few days and costs a great deal to keep. Setting retention per table, with reasons recorded, lets the SOC spend storage where investigations actually need it while meeting legal minimums. The retention table is reviewed yearly with the legal team, and any change is recorded with the reason and approver.

### Time windows

Windowed aggregation needs care at boundaries: a burst spanning 10:09–10:11 may split across two 10-minute windows and miss a threshold in both.

### Worked example

Amara finds the portal logs store the timestamp as local time text while internal logs use UTC. Her join returns nothing because times never match. She adds a parsing step converting portal times to UTC at ingestion, re-runs the join and finds u5's session touched no internal systems.

> **Synthetic case.** Tables and fields are invented.

### Errors and limits

Normalisation can lose source detail; keep the original raw record alongside normalised fields.

### Exercises

- **EX037 — Field normalisation.** Why normalise field names at ingestion? *Rubric:* 3 = one name per concept simplifies queries and reduces errors; 2 = partial; 1 = style; 0 = none.
- **EX038 — Failed join.** Why did Amara's join return nothing, and how was it fixed? *Rubric:* 3 = local-time text vs UTC; convert at ingestion; 2 = partial; 1 = bad query guess; 0 = none.
- **EX039 — Indexing choice.** Which fields should be indexed first? *Rubric:* 3 = most used by detections and analysts: user, host, source address; 2 = partial; 1 = all; 0 = none.

### Synthesis

Treat security data as a designed data system: consistent schemas, careful joins, sensible indexes and quality checks.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) apply requirements, design, testing and release practices to detection content; (2) use version control and code review for rules; (3) plan deployment and rollback; (4) manage technical debt in a SOC.

### 14.1 Detection as code

Detection rules are software. Writing them as text files in a standard format such as Sigma, storing them in version control and reviewing changes brings software engineering discipline to the SOC.

Version control records who changed a rule, when and why, which answers questions after an incident such as whether a detection was active at the time. A standard format like Sigma also makes rules portable between SIEM products, and lets teams share and review rules using ordinary software tools rather than a vendor console.

### 14.2 Requirements

Each rule starts with a requirement: what behaviour, on which assets, with what acceptable false-positive rate and response. Requirements trace to threats, often expressed as ATT&CK techniques.

Writing the requirement before the rule keeps the work aimed at a real risk. Stating an acceptable false-positive rate up front gives the test a pass mark. Naming the response tells the rule's author how much detail an alert must carry: an alert that triggers an account lock needs stronger evidence than one that only feeds a daily review.

### 14.3 Testing

Rules are tested against recorded benign data (to measure false positives) and against safe test events (to confirm they fire). Tests run automatically when a change is proposed.

Recorded benign data might be a week of normal portal logs; safe test events are synthetic records crafted to look like the target behaviour without any real attack. A rule that fires on the synthetic burst but stays quiet on the normal week passes. Running both automatically on every change catches regressions before deployment.

### 14.4 Review

A second engineer reviews logic, performance and documentation. Review catches overly broad conditions before they flood analysts.

Performance is easy to overlook: a rule that searches every record for a substring might work on test data but strain the SIEM in production. The reviewer also checks that documentation tells an analyst what to do when the rule fires. Paolo uses a short checklist so reviews are consistent across reviewers and rules. Review comments and the author's responses stay attached to the change in version control.

### 14.5 Release and rollback

New rules deploy first in a "monitor only" mode that records matches without alerting. After a week of acceptable results, they move to alerting. If problems appear, the previous version is restored from version control.

Monitor mode shows how often a rule would fire on live data without adding to the analysts' queue. Acceptable results mean the match rate and precision meet the requirement. Because every version lives in version control, rollback is quick and leaves a record, unlike editing a rule in place in a console with no history.

### 14.6 Technical debt

Old, untested rules accumulate. Paolo schedules a quarterly review to retire rules that no longer match any asset or threat.

A rule written for a server decommissioned two years ago still consumes processing and may confuse new analysts. Rules whose tests no longer pass, or that have no tests at all, carry hidden risk. The quarterly review lists each rule with its last match, test status and owner, and retired rules are kept in version history rather than deleted outright.

### 14.7 Documentation

Each rule carries a description, author, references, known benign triggers and response guidance.

Known benign triggers save analysts time: if a backup job routinely trips a rule, the documentation says so and how to recognise it. References link the rule to the threat it addresses. Response guidance gives the first steps, so a newer analyst can act correctly at night without waiting for the rule's author. A rule missing any of these fields fails the automated checks and cannot be merged, so documentation is never left for later and forgotten.

### Ownership

Every rule has a named owner who answers questions and reviews its performance.

### Worked example

Amara writes her portal stuffing rule as a Sigma-style file with a requirement link, two test cases and response guidance. In monitor-only mode it matches four times in a week: two real bursts and two load tests by the web team. She adds an exception tied to the load-test tool's signed user agent and a calendar check, then promotes the rule.

> **Synthetic case.** The rule and week are invented.

### Errors and limits

Process overhead can slow urgent detections; keep an emergency path with later review.

### Exercises

- **EX040 — Monitor-only mode.** What is monitor-only deployment, and why use it? *Rubric:* 3 = records matches without alerting to measure noise first; 2 = partial; 1 = no alerting ever; 0 = none.
- **EX041 — Load-test exception.** How were load-test matches handled? *Rubric:* 3 = exception tied to signed user agent and calendar check; 2 = partial; 1 = deleted rule; 0 = none.
- **EX042 — Rule documentation.** List four things each rule document contains. *Rubric:* 3 = description, author, references, benign triggers, response guidance (four); 2 = three; 1 = one; 0 = none.

### Synthesis

Detection-as-code applies requirements, tests, review and staged release to keep rules reliable.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) explain confidentiality, integrity and availability; (2) relate threats, vulnerabilities and controls; (3) place security operations within the NIST CSF 2.0 functions; (4) distinguish prevention from detection and response.

### 15.1 The three properties

Confidentiality keeps information from unauthorised people; integrity keeps it accurate and unaltered; availability keeps systems usable. The portal incident touched all three: customer data could be seen, addresses altered, and the login service slowed.

Thinking in all three keeps the response balanced. A team focused only on confidentiality might miss that customers' delivery addresses could have been changed, an integrity problem that could misdirect parcels. Availability suffered too, as genuine customers met slow logins during the burst. Amara's incident notes record the effect on each property separately.

### 15.2 Threats, vulnerabilities, controls

A threat is a possible cause of harm; a vulnerability is a weakness it can exploit; a control reduces risk. Reused customer passwords are the vulnerability credential stuffing exploits; rate limiting and multi-factor authentication are controls.

Separating the three clarifies what each fix does. Lindqvist cannot stop criminals buying leaked password lists, the threat, and cannot force customers to stop reusing passwords, the vulnerability. It can add controls that make reused passwords less useful, such as slowing repeated attempts and asking for a second factor.

### 15.3 CSF 2.0 functions

The NIST Cybersecurity Framework 2.0 organises outcomes into Govern, Identify, Protect, Detect, Respond and Recover. A SOC mainly delivers Detect and Respond, but depends on Identify (asset knowledge) and feeds Govern with risk information.

Without Identify, the SOC would not know which systems the portal depends on or who owns them. Feeding Govern means turning incident lessons into risk information that leaders use for decisions, such as funding MFA for customers. Mapping SOC work to the functions also shows where the team relies on others to deliver its own outcomes.

### 15.4 Prevention and detection

No prevention is perfect. Detection finds what prevention missed, and response limits harm. A balanced programme invests in all three.

Spending everything on prevention leaves the organisation blind when a control fails; spending everything on detection lets avoidable attacks through and floods analysts. Response turns detection into reduced harm, so a detection with no one able to act on it adds little. Budgets are argued using incidents like the portal burst, which needed all three. Each function has its own measures.

### 15.5 Defence in depth

Several layers — rate limits, bot detection, MFA, monitoring of account changes — mean one failure does not lead to full compromise.

Each layer catches a share of what slips past the one before. Rate limits slow the attempts, bot detection blocks automated clients, MFA stops a correct password from being enough, and monitoring of account changes spots misuse after login. Layers should fail independently, so a single misconfiguration cannot disable several at once. Amara lists which portal layers existed during the burst and which were missing.

### 15.6 Least privilege

Accounts get only the rights they need, limiting damage when one is misused.

At Lindqvist, the portal's database account can read and update customer records but cannot drop tables or read staff data. If an attacker controlled the portal, the damage would be limited to what that account allows. SOC analysts follow the same rule: they get read access to logs, while response actions such as account locks need separate permissions. Rights are reviewed each quarter and removed when roles change.

### 15.7 Case mapping

Amara maps the portal incident: the vulnerability (password reuse by customers), the missing control (no MFA option for customers), the detection (her burst rule) and the response (account lock, notice).

The mapping shows where effort would have the most effect. Detection and response worked, but both acted after a customer account had been entered. Adding an MFA option would address the gap before login succeeds. Amara presents the map to Paolo as a one-page table, which later becomes input to the security team's risk discussion with management.

### Risk as the organiser

Risk combines how likely harm is and how bad it would be. Lindqvist ranks the customer portal high because it holds addresses and delivery schedules, so its monitoring gets priority over internal test systems.

### Worked example

Paolo asks Amara which CSF function a new customer MFA option falls under. She answers Protect, and notes that monitoring MFA enrolment rates and failed second factors would add a Detect outcome.

> **Synthetic case.** Mapping and controls are invented.

### Errors and limits

Frameworks organise thinking but do not set priorities; risk assessment does.

### Exercises

- **EX043 — CIA in the case.** Show how the incident touched confidentiality, integrity and availability. *Rubric:* 3 = data visible, address altered, service slowed; 2 = two; 1 = one; 0 = none.
- **EX044 — Vulnerability and control.** Name the vulnerability and two controls for credential stuffing. *Rubric:* 3 = password reuse; rate limiting and MFA; 2 = one control; 1 = vague; 0 = none.
- **EX045 — CSF placement.** Which CSF functions does a SOC mainly deliver, and which does it rely on? *Rubric:* 3 = Detect and Respond; relies on Identify, informs Govern; 2 = partial; 1 = one; 0 = none.

### Synthesis

Security fundamentals frame SOC work: properties to protect, risks to reduce and functions to deliver.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) view the SOC as a system of people, process and technology; (2) define interfaces and requirements across components; (3) manage trade-offs with explicit criteria; (4) plan lifecycle from concept to retirement.

### 16.1 The SOC as a system

A SOC combines people (analysts, engineers), processes (triage, escalation) and technology (sensors, SIEM, case management). Zimmerman (2014) argued that many SOCs over-invest in tools and under-invest in people and process; systems thinking keeps them in balance.

A new SIEM bought without analysts trained to use it, or without a triage process to receive its alerts, adds cost but little protection. Systems thinking asks how a change in one part affects the others: a new detection adds alerts, which adds analyst workload, which may need a process change. Amara learns to ask that chain of questions before proposing any tool.

### 16.2 Interfaces

Each component exchanges something: sensors send events to the SIEM, the SIEM sends alerts to the case system, analysts send escalations to incident responders. Each interface needs a defined format, timing and owner.

Most failures between teams happen at interfaces nobody owns. If the SIEM changes its alert format and nobody tells the case system's administrator, alerts may arrive with missing fields, or not at all. Writing down format, timing and owner for each interface turns an assumption into an agreement that can be checked, and gives someone the duty to notice when it breaks.

### 16.3 Requirements flow

Top-level needs ("detect account takeover within 15 minutes") break down into component requirements: portal logs delivered within 2 minutes, rule latency under 5 minutes, analyst acknowledgement within 8 minutes.

The parts add up: two minutes for delivery, five for the rule and eight for acknowledgement give exactly fifteen, which leaves no slack. If log delivery slips to four minutes, the whole target fails even though the rule and the analysts are on time. Paolo suggests tightening component budgets so the total leaves a margin, and monitoring each one separately.

### 16.4 Trade-offs

More data improves visibility but costs storage and analyst attention. Systems engineers state criteria (detection time, cost, analyst load) and compare options against them.

Stating criteria before comparing options stops people from picking the option they already liked and then finding reasons. Weights make priorities explicit: if detection time matters most, a costlier option that halves it may win. Amara builds a small table for adding depot network sensors, scoring each option on the agreed criteria with the evidence behind each score.

### 16.5 Lifecycle

Components are planned, built, operated, maintained and retired. Retiring an old sensor needs a replacement first, or coverage silently disappears.

Retirement is the phase most often neglected. A sensor switched off during a hardware refresh can leave a gap that nobody notices until an incident needs its data. Planning retirement means checking which rules depend on the component, confirming the replacement produces equivalent data, and running both in parallel for a short period before switching the old one off. Owners sign off each retirement.

### 16.6 Verification

Each requirement has a test: a timed synthetic event checks that the 15-minute target is met end to end.

The synthetic event is injected at the portal, as if from a real login burst, and timestamps are recorded at each stage: log arrival, rule firing, alert creation and analyst acknowledgement. Comparing the stage times with the component budgets shows exactly where delay occurs. The test runs regularly, not once, because performance drifts as volumes and staffing change. Missed targets open a ticket.

### 16.7 Case

Amara draws Lindqvist's SOC as a block diagram and labels each interface with format, latency and owner.

Drawing the diagram reveals two interfaces with no named owner: the feed from the load balancer and the link between the case system and the on-call paging service. It also shows that the portal logs pass through an intermediate collector that nobody had listed. Each gap becomes a task, and the diagram is stored with the SOC's architecture documents. Paolo reviews it with her.

### Failure modes of the system

System-level failures often sit at interfaces: a format change upstream silently breaks parsing downstream. Amara adds a parsing-error alert at each interface.

### Worked example

Her timed test injects a harmless synthetic portal login burst at 14:00:00. The SIEM receives it at 14:01:40, the rule fires at 14:05:10, and an analyst acknowledges at 14:11:30 — 11.5 minutes end to end, inside the 15-minute requirement. The slowest step is analyst acknowledgement.

> **Synthetic case.** The SOC design and test are invented.

### Errors and limits

End-to-end tests at quiet times may understate delays during busy periods; repeat them under load.

### Exercises

- **EX046 — Balance.** What imbalance did Zimmerman (2014) warn about? *Rubric:* 3 = over-investing in tools vs people and process; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Requirement breakdown.** Break "detect within 15 minutes" into component requirements. *Rubric:* 3 = log delivery, rule latency, acknowledgement with times; 2 = two; 1 = one; 0 = none.
- **EX048 — Timed test.** What did the end-to-end test show? *Rubric:* 3 = 11.5 min total; inside target; acknowledgement slowest; 2 = partial; 1 = wrong; 0 = none.

### Synthesis

Systems engineering connects SOC people, process and technology through defined interfaces, requirements and tests.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) explain feedback loops in security operations; (2) model tuning as a control system; (3) recognise oscillation and instability in alert thresholds; (4) design stable feedback with measurement.

### 17.1 Feedback loops

A feedback loop measures an output and adjusts an input to reach a target. A thermostat measures temperature and switches heating. In a SOC, analysts measure alert quality and adjust rules.

A loop has four parts: a target, a measurement, a comparison and an adjustment. If any part is missing, the loop does not work. Many SOCs have the adjustment, since engineers do tune rules, but lack a clear target or a reliable measurement, so tuning becomes a reaction to whichever complaint was loudest that week.

### 17.2 Tuning as control

Suppose the target is fewer than 20 false alerts per day from a rule. If the measured count is higher, the threshold rises; if real attacks are missed, it falls. This is a control loop with the engineer as controller.

The loop has two opposing pressures: false alerts push the threshold up, missed attacks push it down. A good controller balances both rather than reacting only to the more visible one. False alerts are seen every day by analysts, while misses may stay hidden, so engineers must deliberately look for misses or the threshold will drift upward over time.

### 17.3 Oscillation

If adjustments are too large or too fast, the system overshoots: the threshold jumps up, misses an attack, jumps down, floods analysts. Small, measured steps with time to observe effects avoid oscillation.

A thermostat that switched heating fully on and off at the slightest change would make a room swing between too hot and too cold. Rule tuning behaves the same way. Changing a threshold from five to six, then watching for a fortnight, gives clear evidence of the effect. Changing from five to fifteen and back within a week tells nobody anything.

### 17.4 Delay

Feedback in SOCs is slow: the effect of a change on missed attacks may not be known for weeks. Long delays make aggressive tuning dangerous.

A missed attack may surface only when a customer complains or when a later investigation finds earlier signs. If an engineer raises a threshold today, the cost of that change may not appear for a month. Faster signals, such as injected test events that should be caught, shorten the loop by showing immediately whether a change has opened a gap.

### 17.5 Positive feedback

Some loops amplify: an overloaded queue makes analysts close alerts faster with less care, which hides misses, which leads to more silent compromise. Recognising such loops lets managers break them.

The loop feeds itself: more silent compromises lead to more incidents later, which add more work, which increases the pressure to close alerts quickly. Breaking it might mean temporarily disabling low-value rules to give analysts time, or adding staff. Managers who track only queue length may see the queue shrink and believe things improved, while quality falls.

### 17.6 Measurement

Feedback is only as good as its measurement. Labelled samples of closed alerts and periodic safe test events provide signals about misses.

Labelled samples mean reviewing a random selection of closed alerts and checking whether the closing decision was right. That shows how often benign closures were actually wrong. Safe test events, injected without warning, show whether the full chain from sensor to analyst still works. Both give the loop data about misses, which ordinary alert counts cannot reveal. Both feed the monthly review.

### 17.7 Case

Amara's portal rule threshold starts at 5 failures per 10 minutes; Paolo asks her to plan its tuning loop.

Amara's plan names the target, at most a set number of false alerts per day with no missed test bursts; the measurements, daily counts and weekly injected bursts; the step size, one failure at a time; and the wait, two weeks between changes. Paolo approves it with one addition: any change and its result must be written in the rule's history. Amara starts the loop next Monday.

### Worked example

Amara proposes: measure weekly false alerts and test-event detection; change the threshold by at most one step per fortnight; never raise it if any test event was missed. After four weeks the rule settles at 6 failures, with 8 false alerts per day and all test events caught.

> **Synthetic case.** Thresholds and counts are invented.

### Errors and limits

Treating tuning as control is a model; attackers adapt deliberately, unlike heat in a room.

### Exercises

- **EX049 — Oscillation cause.** What causes threshold oscillation, and how is it avoided? *Rubric:* 3 = large/fast changes; small steps with observation time; 2 = partial; 1 = vague; 0 = none.
- **EX050 — Harmful loop.** Describe one positive feedback loop in a SOC. *Rubric:* 3 = overload → hasty closures → missed attacks → more compromise; 2 = partial; 1 = vague; 0 = none.
- **EX051 — Tuning plan.** State Amara's tuning rules and the outcome. *Rubric:* 3 = ≤ 1 step per fortnight; no raise if test missed; settled at 6, 8 false/day, all tests caught; 2 = partial; 1 = outcome only; 0 = none.

### Synthesis

Treat tuning as a slow feedback loop: measure carefully, adjust gently and watch for amplifying loops.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) describe security architecture as structured placement of controls; (2) design network zones and trust boundaries; (3) place sensors where they see the most relevant activity; (4) evaluate architecture against threats.

### 18.1 What architecture means

Security architecture decides where controls sit and how components trust each other. It is the structure that makes individual controls work together rather than a pile of products.

Products bought separately may overlap in some areas and leave gaps in others. Architecture starts from the systems and data to protect, decides which controls each needs, and then chooses products to fill those roles. It also defines how the parts trust one another, such as which systems may send logs to the SIEM and how they prove who they are.

### 18.2 Zones and boundaries

Lindqvist separates the internet-facing portal, internal business systems, the depot networks that run handheld scanners, and the SOC's own systems. Each boundary has rules about what may cross it. Boundaries are where monitoring is most informative, because legitimate traffic across them is limited and known.

Inside a zone, many systems talk freely and traffic is hard to judge. At a boundary, only specific flows should pass: the portal may call the order system on one port, depots may send scan data to one server. Anything else crossing is suspicious by definition, which gives monitoring a clear baseline to compare against.

### 18.3 Sensor placement

Sensors belong where they see relevant activity with little noise: at the web tier for the portal, at domain controllers for authentication, at the boundary between business and depot networks. Placing one large sensor at the internet edge sees much traffic but little context.

An edge sensor sees every packet from the internet, most of it scanning noise, without knowing which customer account a request concerned. A sensor at the web tier sees the decrypted request and the username. Placing sensors where the meaning is available, rather than where the volume is highest, gives analysts fewer, richer events to work with.

### 18.4 Protecting the SOC

The SIEM and case system are valuable targets: they show what defenders can see. They sit in their own zone with separate administrator accounts and multi-factor authentication.

An attacker who controls the SIEM can see which alerts exist, learn which actions are being detected, or delete evidence. Separate administrator accounts mean a compromised staff account in the business zone cannot reach SOC systems. The SOC monitors its own systems too, with alerts on configuration changes and on logins from outside the SOC zone.

### 18.5 Mapping to threats

Architects check each important ATT&CK technique against the architecture: which control prevents it, which sensor would see it, and which team would respond. Gaps become backlog items. D3FEND helps name the defensive technique each control provides.

The exercise produces a table: each technique in a row, with columns for prevention, detection and response owner. Empty cells are gaps. Not every gap needs closing; some techniques are unlikely against Lindqvist, and the risk discussion decides priorities. D3FEND's names, such as credential hardening, make it easier to compare controls across products.

### 18.6 Simplicity

Complex architectures hide gaps. Fewer, well-understood boundaries are easier to monitor.

Each extra boundary needs its own rules, sensors and maintenance, and exceptions accumulate over time until nobody remembers why a flow is allowed. Merging zones that serve the same purpose can make monitoring clearer. Amara notes that Lindqvist has three slightly different depot network designs, which multiplies the work of defining normal traffic for each. She proposes one standard depot design, rolled out as each site's equipment is replaced, so the baseline only needs defining once.

### 18.7 Case

Amara reviews where the portal's logs are produced and finds that the load balancer, which sees the true client addresses, was not forwarding its logs; the web servers saw only the balancer's address for some requests.

Because the balancer replaced client addresses with its own for some requests, the web servers' logs showed many attempts from one internal address. Aggregating by network then grouped unrelated customers together and hid the real sources. Forwarding the balancer's logs, and configuring it to pass the original address in a header, fixes both the data and the rule's accuracy.

### Worked example

Before that change goes in, Paolo approves it only after checking that the header cannot be trusted from outside: the balancer overwrites any header a client sends, so the recorded address is reliable.

> **Synthetic case.** The architecture and zones are invented.

### Errors and limits

Architecture diagrams drift from reality; verify with traffic and configuration, not only drawings.

### Exercises

- **EX052 — Boundary monitoring.** Why is monitoring most informative at trust boundaries? *Rubric:* 3 = legitimate crossing traffic is limited and known; 2 = partial; 1 = vague; 0 = none.
- **EX053 — Load balancer gap.** What gap did Amara find, and how was it closed safely? *Rubric:* 3 = balancer logs not forwarded; client header added, balancer overwrites client-sent header; 2 = partial; 1 = ignored; 0 = none.
- **EX054 — SOC protection.** How are the SOC's own systems protected? *Rubric:* 3 = own zone, separate admin accounts, MFA; 2 = two; 1 = one; 0 = none.

### Synthesis

Good architecture places controls and sensors at boundaries, protects the SOC itself and is checked against threats.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) explain authentication, authorisation and multi-factor methods; (2) relate identity events to detection; (3) describe hashing, encryption and signatures in SOC tooling; (4) recognise identity-based attacks from the defender's view.

### 19.1 Identity as the new perimeter

Many attacks today use valid credentials rather than technical exploits. Authentication logs — successes, failures, MFA challenges, token issuance — are therefore among a SOC's most valuable data.

With cloud services and remote work, there is no single network edge that all access crosses. Credentials are what grant access, so attackers buy, guess or steal them. Logs from identity systems show who tried to sign in, from where, with what result and which second factor was used, which makes them central to spotting misuse.

### 19.2 Authentication and authorisation

Authentication proves who a user is; authorisation decides what they may do. The portal authenticates customers by password; Lindqvist staff use single sign-on with MFA. Authorisation logs show access to sensitive functions, such as changing a delivery address.

A correct password satisfies authentication, but the portal still decides whether that customer may view a given order. Logs from each step answer different questions: authentication logs show who got in, authorisation logs show what they tried to do. An attacker who signs in successfully often shows up later in authorisation logs through unusual actions.

### 19.3 MFA signals

MFA reduces credential-stuffing success. Its logs add signals: repeated MFA prompts denied by the user may indicate someone holding the password; a sudden change of MFA device warrants checking.

Denied prompts suggest that the password is known to someone else, since the real user is refusing a sign-in they did not start. Repeated prompts sent in quick succession may be an attempt to wear the user down until they approve one. A new MFA device registered right after a sign-in from an unfamiliar place deserves prompt review.

### 19.4 Hashing

A cryptographic hash gives a fixed-length fingerprint of data. SOCs use hashes to identify files and verify that exported evidence is unchanged. Passwords should be stored using slow, salted password-hashing functions so stolen databases resist cracking.

A file hash lets analysts search across many machines for the same file without moving the file itself. Exported evidence hashed at export can be checked later by anyone. Password hashing is different: functions designed to be slow and salted make each guess expensive, so a stolen database cannot be checked against billions of guesses quickly.

### 19.5 Encryption and signatures

Encryption protects confidentiality in transit (TLS) and at rest. Digital signatures prove origin and integrity: signed software, signed log batches. Signed load-test tools, as in chapter 14, let rules make reliable exceptions.

Encryption in transit stops someone on the network from reading logins; encryption at rest protects stored data if a disk is stolen. Signatures answer a different question: did this come from who it claims, unchanged? A rule can safely exclude load tests from a tool whose signature verifies, while still alerting on an unsigned copy using the same name.

### 19.6 Identity attacks seen defensively

Credential stuffing, password spraying and token theft all leave traces in identity logs. The defender's job is to collect those logs and know normal patterns, not to reproduce the attacks.

Credential stuffing tries leaked username and password pairs across many accounts; password spraying tries a few common passwords against many accounts; token theft reuses a session token without needing the password at all. Each pattern looks different in logs, and detections are built from those defensive views using synthetic data rather than from live attempts.

### 19.7 Case

After the incident, Lindqvist offers customers optional MFA and alerts on address changes immediately after a login from a new network.

Optional MFA protects customers who choose it; the address-change alert protects everyone, because a change of delivery address is often what an attacker wants after entering an account. The alert combines two signals, a new network and a sensitive change, though its first week shows how often honest customers who move house also match both. The security team plans to review uptake of MFA after six months. Customers are told how to enable it.

### Worked example

Amara designs a rule: "address change within 10 minutes of a successful login from a network not seen for that customer in 90 days". In monitor-only mode it fires 12 times in a week; 11 are customers who moved house and logged in from a new home network. She adds a customer email confirmation step for such changes instead of an analyst alert, keeping the alert only when the confirmation fails.

> **Synthetic case.** Rules and counts are invented.

### Errors and limits

Identity logs from external providers may arrive late or lack fields; check delivery times.

### Exercises

- **EX055 — Why identity logs.** Why are authentication logs among the most valuable SOC data? *Rubric:* 3 = attacks often use valid credentials; logs show their use; 2 = partial; 1 = vague; 0 = none.
- **EX056 — MFA signals.** Give two MFA-related detection signals. *Rubric:* 3 = repeated denied prompts; new MFA device; 2 = one; 1 = vague; 0 = none.
- **EX057 — Confirmation design.** How did Amara reduce noise from the address-change rule? *Rubric:* 3 = customer email confirmation; alert only on failed confirmation; 2 = partial; 1 = deleted rule; 0 = none.

### Synthesis

Identity events and cryptographic tools are central SOC material; design detections around how legitimate users behave.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Security operations and blue team: engineering context

### Learning outcomes

You will (1) describe the SOC's mission and services in engineering terms; (2) relate SOC functions to the organisation's risk; (3) identify stakeholders and constraints; (4) frame SOC engineering problems for the rest of the course.

### 20.1 Mission first

Knerler, Parker and Zimmerman (2022) open with "know what you are protecting and why". Lindqvist protects customer data, delivery operations and payment flows. Engineering choices follow from that mission, not from tool features.

Starting with tools leads to collecting whatever the tool supports. Starting with the mission leads to asking what harm would matter most: stolen customer data, stopped deliveries or diverted payments. Those answers decide which systems need the best coverage and which alerts deserve a page at night, so engineering effort follows business impact.

### 20.2 SOC services

Lindqvist's SOC provides monitoring and triage, incident response coordination, detection engineering, vulnerability intake and threat intelligence consumption. Each service has customers inside the company and measurable outputs.

Treating each as a service clarifies who it serves and how to measure it. Monitoring serves the whole company and is measured by detection and response times; detection engineering serves the analysts and is measured by rule quality; vulnerability intake serves IT teams and is measured by how quickly reports reach owners. Unclear services tend to drift into unplanned work.

### 20.3 Constraints

Budget, staff numbers, regulation and legacy systems constrain design. The depot scanners run old software that cannot host agents, so network monitoring must cover them.

Constraints are design inputs, not excuses. Old scanner software that cannot run an agent rules out endpoint telemetry, so the design shifts to observing scanner traffic on the depot network. Budget may limit sensors to the busiest depots first. Regulation may require keeping certain logs for set periods. Each constraint is written down so later readers understand the design.

### 20.4 Stakeholders

The CISO sets priorities; IT operations own systems; legal and privacy staff set limits; business units feel the impact of response actions. SOC engineers must work with all of them.

IT operations may resist a sensor that could slow their systems; legal staff may limit what content can be collected; business units may object to an account lock during peak delivery hours. Engineers who involve them early hear these concerns while design is still flexible. Amara keeps a stakeholder list with what each group cares about most.

### 20.5 Engineering problems ahead

The course follows four problems at Lindqvist: detecting account takeover on the portal; monitoring depot networks without agents; keeping the SIEM within capacity; and proving the SOC works through verification.

Each problem draws on different skills: account takeover on identity data and statistics, depot monitoring on networks and architecture, SIEM capacity on data systems and maths, and verification on testing and measurement. Following the same company through all four lets the course show how decisions in one area, such as storage tiering, constrain options in another.

### 20.6 Maturity

The SOC-CMM (van Os, 2016) assesses business, people, process, technology and services. Lindqvist's self-assessment shows strong technology but weak process documentation, guiding priorities.

A maturity model gives a structured way to see strengths and weaknesses across a whole SOC. Strong technology with weak process documentation means tools work but outcomes depend on which analyst is on shift. The self-assessment suggests writing playbooks before buying more tools, and it gives a baseline to repeat later and show progress. The assessment is repeated each year by the same method.

### 20.7 Measures of success

Success is not "no incidents" but faster detection, better decisions and less harm.

A quiet year may mean nothing happened, or that nothing was detected; the two look the same in an incident count. Better measures include time from first evidence to detection, time to containment, and how often response decisions were later judged correct. Lindqvist's SOC reports these monthly, alongside honest notes on any missed detection. Each measure has a stated target, and trends over several months matter more than any single month's figure, which can swing with one large incident.

### Funding the SOC

The SOC's budget competes with other IT work. Engineers who can show how a change reduces risk or analyst time win support more easily than those who ask for tools.

### Worked example

Amara writes a one-page context brief: mission, services, constraints, stakeholders and the four engineering problems. Paolo adds one constraint she missed — the SOC has only two analysts on night shift — which shapes every alerting decision.

> **Synthetic case.** Lindqvist's SOC and its assessment are invented.

### Errors and limits

Context changes with the business; revisit the brief when the company changes.

### Exercises

- **EX058 — Mission link.** How does the mission guide engineering choices? *Rubric:* 3 = what is protected drives priorities, not tool features; 2 = partial; 1 = vague; 0 = none.
- **EX059 — Depot constraint.** Why must depot scanners be monitored from the network? *Rubric:* 3 = old software cannot host agents; 2 = partial; 1 = no reason; 0 = none.
- **EX060 — Night shift.** Why does the two-analyst night shift matter? *Rubric:* 3 = limits alert volume they can handle; shapes alerting; 2 = partial; 1 = irrelevant; 0 = none.

### Synthesis

SOC engineering starts from mission, services, constraints and stakeholders; the rest of the course solves problems within them.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Security operations and blue team: requirements

### Learning outcomes

You will (1) elicit SOC requirements from stakeholders and threats; (2) write measurable functional and non-functional requirements; (3) trace requirements to threats and tests; (4) prioritise requirements under constraints.

### 21.1 Sources of requirements

Requirements come from the mission, threats, regulations, incidents and analysts' pain. The portal incident produced the requirement "detect likely account takeover on the customer portal within 15 minutes".

Each source pulls in a different direction. Threats suggest what attackers will try; regulations set minimums such as retention; incidents expose gaps that actually hurt; analysts' pain reveals where work is wasted on noisy rules or missing context. Collecting from all of them avoids a requirement set that reflects only the loudest voice, and the source of each is recorded beside it.

### 21.2 Functional requirements

These say what the system does: ingest load-balancer logs; correlate failures and successes per network; raise an alert with the customer ID, source network and subsequent actions.

Each statement is phrased as something the system must do, so a tester can check it directly: feed in load-balancer logs and see whether they are ingested; create a failure burst followed by a success and see whether the correlation fires; open the alert and see whether it carries the three named fields. Vague verbs like 'support' or 'handle' are avoided.

### 21.3 Non-functional requirements

These say how well: latency under 5 minutes from event to alert; availability of 99.5% for the pipeline; no more than 10 false alerts per day to the night shift; data retained 90 days hot.

These qualities are often where systems disappoint, because they are easy to forget during design. A rule that is logically perfect but alerts twenty minutes late misses the target. A 99.5% availability target allows about 44 hours of pipeline downtime per year, which Amara compares with the maintenance windows already planned, to check that the figure is realistic.

### 21.4 Measurable wording

"Fast" and "accurate" cannot be tested. Each requirement states a number, a condition and a measurement method.

For example, 'fast' becomes '95% of alerts created within 5 minutes of the triggering event, measured from event time to alert time over a calendar month'. The method matters as much as the number: measuring from ingestion time rather than event time would hide delays in log delivery and make the pipeline look better than it is. Amara rewrites every requirement in this form and asks Paolo to try writing a test for each; any he cannot test goes back for rewording.

### 21.5 Traceability

A table links each requirement to its source (threat, regulation, incident), the design element that meets it and the test that verifies it. ATT&CK technique IDs give a common reference for threat sources.

The table works in both directions. Reading forward from a threat shows whether anything addresses it; reading backward from a test shows why it exists. A changed regulation is traced the same way, from its row to the requirements and tests that cite it. Using technique IDs means the security team and outside reports can refer to the same threat without ambiguity.

### 21.6 Prioritisation

With limited staff, Amara and Paolo rank requirements as must, should or could, guided by risk and cost.

A must is something without which the system fails its purpose, such as detecting account takeover; a should adds real value but can wait, such as enriching alerts with customer tier; a could is nice to have. Ranking openly lets managers see what will not be delivered this quarter, rather than discovering it later when time runs out. Musts are funded first; coulds wait for spare capacity.

### 21.7 Change control

Requirements change; each change is recorded with reason and approval, and affected tests are updated.

Without it, requirements shift quietly through conversations, and tests end up checking something no one agreed to. Recording the reason keeps changes honest: lowering the false-alert limit because analysts complained is different from lowering it because the night shift was reduced. Updating tests alongside keeps verification aligned with what the system is now expected to do. Paolo approves each change, and the requirement keeps its history so earlier test results can still be interpreted against the version in force then.

### Acceptance criteria

Each requirement has acceptance criteria agreed before building: what result in which test counts as passed. Agreeing them early prevents arguments later about whether the work is done, and gives analysts a clear promise about what the new detection will deliver.

### Worked example

Amara's requirement R-07 reads: "The pipeline shall raise a possible-takeover alert within 15 minutes of a successful portal login that follows at least 6 failures for distinct users from the same /24 in 10 minutes; verified monthly by a timed synthetic event." Paolo approves it as a must.

> **Synthetic case.** Requirements are invented.

### Errors and limits

Too many requirements become unmanageable; focus on those tied to real risks.

### Exercises

- **EX061 — Functional versus non-functional.** Give one functional and one non-functional requirement from the case. *Rubric:* 3 = e.g. correlate failures/successes; latency under 5 minutes; 2 = one; 1 = confused; 0 = none.
- **EX062 — Measurable wording.** Rewrite "alerts must be fast" as a measurable requirement. *Rubric:* 3 = number, condition, measurement; 2 = partial; 1 = unchanged; 0 = none.
- **EX063 — Traceability table.** What columns does the traceability table have? *Rubric:* 3 = requirement, source, design element, test; 2 = three; 1 = one; 0 = none.

### Synthesis

Measurable, traceable, prioritised requirements turn incidents and threats into engineering work.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Security operations and blue team: system and data models

### Learning outcomes

You will (1) model the SOC pipeline as stages and data stores; (2) define the event data model; (3) model entities such as users, hosts and customers; (4) use models to find gaps.

### 22.1 Pipeline model

Lindqvist's pipeline has stages: collect (agents, syslog, cloud APIs), transport, parse and normalise, enrich (asset and identity data), store, detect, alert, and case management. Each stage can fail, delay or distort data.

Thinking in stages helps locate problems. A missing alert could mean the event was never collected, was dropped in transport, failed to parse, lacked enrichment the rule needed, aged out of storage, or never matched the rule. Each stage gets its own health measures, so an analyst can trace an event through the pipeline and find where it disappeared.

### 22.2 Event model

Every normalised event carries time (UTC), source, host, user, action, outcome, and raw record reference. A shared model lets one rule work across sources.

Keeping a reference to the raw record matters because normalisation can lose detail or introduce errors; an analyst may need the original line to check what the source actually said. Recording time in UTC avoids confusion between sources in different zones. Because every source maps to the same fields, a rule about failed logins works across the portal, VPN and staff sign-in.

### 22.3 Entity model

Entities persist across events: a customer, an employee, a host, a network. Entity tables hold attributes such as criticality, owner and normal locations, used for enrichment.

Events are moments; entities give them context. An alert about a host means more when the alert also shows that the host is a payment server owned by finance. Normal locations for a customer help judge whether a login from a new country is unusual. Entity tables need updating, since stale data misleads analysts as surely as missing data.

### 22.4 Relationships

Customers own accounts; employees use hosts; hosts sit in zones. Modelling relationships lets analysts ask "which zone is this host in?" automatically.

Without modelled relationships, an analyst must look up each link manually in different systems, which is slow during an incident. With them, an alert can show automatically that the host belongs to a depot zone and that its usual user is on leave. Relationships also let rules reason across entities, for example flagging an employee using a host outside their own zone.

### 22.5 Gaps from models

Walking through the model stage by stage, Amara checks each source: is it collected, parsed, enriched and covered by detections? Depot networks are collected but not enriched, because the asset inventory lacks depot devices.

The walk-through is systematic: for each source, four yes-or-no questions. Missing enrichment for depot devices means alerts about them carry only an address, with no owner, location or role, so analysts must investigate from scratch. The fix is upstream: adding depot devices to the asset inventory, which helps IT operations as well as the SOC.

### 22.6 Model ownership

The data model is owned by the detection engineering team; changes are versioned like rules.

An owner decides which fields exist and what they mean, and reviews proposed changes. Versioning lets rules declare which model version they expect, so a field rename does not silently break them. Without ownership, different engineers add fields with overlapping meanings, and over time the shared model splinters into source-specific dialects. The owner publishes a changelog, and rule authors read it before each release. Deprecated fields stay available for one release so rules can migrate without a gap in coverage.

### 22.7 Models and people

Models also include who acts at each stage: which team fixes parsing errors, who maintains enrichment tables.

A pipeline diagram that shows only systems hides the human work that keeps it running. Naming the team responsible for parser failures means alerts about broken parsing reach someone who can act. Naming the owner of enrichment tables means stale entries have someone accountable. Amara adds an owner to every stage on the pipeline diagram. Each owner also has a backup named, so a parser failure during holidays still reaches someone able to fix it.

### Enrichment freshness

Enrichment tables must be current. A host reassigned from finance to depots still tagged 'finance' misleads analysts. Amara adds a freshness date to each table.

### Worked example

Amara's coverage matrix lists 14 sources against 6 stages. Two cells are empty for depot networks (enrichment, detection) and one for the portal load balancer (detection, newly collected). She turns each empty cell into a backlog item with an owner.

> **Synthetic case.** Sources and matrix are invented.

### Errors and limits

Models simplify; a source marked "collected" may still have gaps in time or fields.

### Exercises

- **EX064 — Pipeline stages.** List the pipeline stages in order. *Rubric:* 3 = collect, transport, parse/normalise, enrich, store, detect, alert, case; 2 = most in order; 1 = few; 0 = none.
- **EX065 — Depot gap.** Why were depot networks not enriched? *Rubric:* 3 = asset inventory lacked depot devices; 2 = partial; 1 = no reason; 0 = none.
- **EX066 — Matrix use.** How did Amara use the coverage matrix? *Rubric:* 3 = empty cells became owned backlog items; 2 = partial; 1 = filed it; 0 = none.

### Synthesis

Pipeline, event and entity models expose where data is missing, unenriched or undetected.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Security operations and blue team: threat and failure analysis

### Learning outcomes

You will (1) analyse threats relevant to the organisation using ATT&CK; (2) analyse failure modes of the monitoring system; (3) combine threat and failure views into priorities; (4) document analyses for review.

### 23.1 Threat analysis

Lindqvist's threat analysis asks which adversaries target logistics firms and which techniques they use. Public reporting and ATT&CK groups show credential abuse, phishing of staff, ransomware and fraud through customer accounts.

Starting with adversaries who target the sector keeps the analysis grounded in what actually happens to similar firms. For a logistics company, delivery fraud and payment diversion are as relevant as data theft. ATT&CK groups document techniques seen in real campaigns, which turns general concern about ransomware into specific behaviours the SOC can look for.

### 23.2 Technique coverage

For each relevant technique, the team records data sources needed, detections present and confidence. Coverage maps show strengths (credential abuse on the portal) and gaps (lateral movement in depot networks).

Confidence records how sure the team is that a detection would work, based on testing rather than on its existence. A rule written but never tested earns low confidence. The coverage map makes priorities visible to managers who cannot read rules: strong in one area, weak in another, with the evidence behind each rating.

### 23.3 Failure analysis

The monitoring system itself fails: sources go silent, parsers break after upgrades, enrichment tables go stale, rules are disabled and forgotten. A failure mode and effects table lists each failure, its effect on detection, how it would be noticed and its likelihood.

The format comes from engineering safety analysis, where it is used for machines and plants. Applied to monitoring, each row asks: if this part fails, which detections stop working, how quickly would we know, and how likely is it? A parser breaking after an upgrade is likely and may go unnoticed for days, so it ranks high.

### 23.4 Silent failures

The worst failures are silent: a source stops sending and nothing alerts. These get detection of their own, covered in chapter 47.

Silence is dangerous because the absence of alerts looks the same as the absence of attacks. A source that normally sends ten thousand events an hour and suddenly sends none should itself raise an alarm. Expected volumes per source, with alerts on large drops, turn silence into a visible signal. Some sources are naturally quiet at night, so thresholds compare each hour with the same hour on previous weeks rather than with a flat daily average.

### 23.5 Combining views

Priority is highest where an important technique depends on a fragile component — for example, account-takeover detection depending on a single load-balancer log feed.

Threat analysis shows what matters; failure analysis shows what is fragile. Their overlap is where a single failure would blind the SOC to an important technique. The load-balancer feed is a clear example: if it stops, account-takeover detection degrades. The response is either a second feed or close monitoring of the existing one. Amara marks such overlaps in red on the coverage map.

### 23.6 Review

Analyses are reviewed by analysts, IT operations and the CISO's office, then revisited after incidents or major changes.

Analysts know which detections are trusted in practice; IT operations know which components are fragile; the CISO's office knows business priorities. Each view corrects the others. Revisiting after incidents keeps the analysis current, since an incident often reveals a technique or failure mode the original review overlooked. Each review produces a dated version with a short list of changes and who requested them, so later readers can see how the team's view of threats and failures evolved over time.

### 23.7 Avoiding bias

Teams overweight recent incidents. Using ATT&CK as a checklist helps consider techniques that have not yet hit Lindqvist.

After the portal incident, attention focuses on credential abuse, and it is tempting to spend all effort there. A checklist forces the team to look systematically at other techniques, such as misuse of remote management tools in depots, that have not yet caused trouble. Recent pain is a useful signal but a poor complete guide. Each technique left out is marked with a short reason.

### Insider and fraud threats

Not every threat is external. Staff with access to customer accounts could misuse it, and fraudsters may use legitimate portal features. These threats rely on business logs, such as address changes and refunds, more than on technical telemetry.

### Worked example

Amara's failure table entry: "Load-balancer log feed stops → no account-takeover alerts → noticed only by chance → likelihood medium (feed broke twice last year) → priority high. Action: heartbeat monitoring and a second feed path."

> **Synthetic case.** The analyses are invented.

### Errors and limits

Threat reports describe others' experiences; tailor them to your environment.

### Exercises

- **EX067 — Coverage record.** What is recorded for each relevant technique? *Rubric:* 3 = data sources, detections, confidence; 2 = two; 1 = one; 0 = none.
- **EX068 — Silent failure.** Why are silent failures the worst? *Rubric:* 3 = nothing alerts, so detection disappears unnoticed; 2 = partial; 1 = vague; 0 = none.
- **EX069 — Combined priority.** Why was the load-balancer feed ranked high? *Rubric:* 3 = important detection depends on fragile single feed; 2 = partial; 1 = random; 0 = none.

### Synthesis

Combine threat coverage with failure analysis of the monitoring system to set priorities.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Security operations and blue team: methods I

### Learning outcomes

You will (1) design threshold and correlation detections; (2) evaluate rules against labelled windows; (3) compare rule variants by true and false positives; (4) choose variants by operational purpose.

### 24.1 Threshold rules

A threshold rule fires when a count in a window crosses a limit: at least 5 distinct users failing from one /24 in 10 minutes.

Counting distinct users rather than total failures targets the stuffing pattern: many accounts, few tries each. A single customer failing ten times would not trip the rule, which is intended. The window and limit are parameters to tune, and the rule's documentation records the values chosen and the evidence that led to them. Five in ten minutes is the starting point.

### 24.2 Correlation rules

A correlation rule requires several conditions, possibly from different sources: failures followed by a success, or a success followed by an address change.

Correlation adds meaning by joining steps that are weak alone. Failures happen constantly; a success alone is normal; failures followed by a success from the same network suggest a guessed password. An address change after a new-network login is more suspicious than either event separately. Such rules need sources with aligned times and shared fields. Clock offsets between sources must be small.

### Lab — comparing rule variants

```python
"""Evaluate a Sigma-style burst rule over synthetic 10-minute windows with labels."""
windows = [  # (window, distinct users failed, any success, label)
    ("09:50", 2, True, "benign"), ("10:00", 7, True, "attack"), ("10:10", 6, False, "attack"),
    ("10:20", 1, False, "benign"), ("11:00", 9, False, "benign"),   # load test
    ("13:30", 5, True, "attack"), ("14:00", 3, True, "benign"), ("15:00", 6, False, "benign")]
def rule(users, success, threshold): return users >= threshold and success
for t in (5, 6):
    tp = sum(rule(u, s, t) and l == "attack" for _, u, s, l in windows)
    fp = sum(rule(u, s, t) and l == "benign" for _, u, s, l in windows)
    fn = sum(not rule(u, s, t) and l == "attack" for _, u, s, l in windows)
    print(f"threshold={t} with-success: TP={tp} FP={fp} FN={fn}")
tp = sum(u >= 5 and l == "attack" for _, u, s, l in windows); fp = sum(u >= 5 and l == "benign" for _, u, s, l in windows)
print(f"threshold=5 no success clause: TP={tp} FP={fp} FN={3-tp}")
```

Run with `python3 lab_rule.py`. Verified output:

```text
threshold=5 with-success: TP=2 FP=0 FN=1
threshold=6 with-success: TP=1 FP=0 FN=2
threshold=5 no success clause: TP=3 FP=2 FN=0
```

### 24.3 Reading the result

With the success clause and threshold 5, the rule catches 2 of 3 attack windows with no false alerts; at threshold 6 it catches only 1. Without the success clause, threshold 5 catches all 3 attack windows but adds 2 false alerts — the 11:00 load test and a 15:00 window.

The figures show the trade-off clearly. Requiring a success makes the rule precise but costs one attack window, an attempt that never succeeded. Dropping the clause catches every attempt but adds noise, including a load test that a signed-tool exception could remove. Raising the threshold to six loses another real window without removing any false alerts, since there were none.

### 24.4 Purpose decides

The no-success variant detects attempts; the success variant detects likely compromise. Lindqvist uses both: attempts go to a daytime queue for rate-limit tuning; likely compromise pages the night shift.

Neither variant is simply better; each answers a different question. Attempts matter for tuning defences, such as rate limits, and can wait for daytime. Likely compromise needs action within minutes, so it justifies waking someone. Splitting the rule by purpose gives each the right urgency instead of forcing one compromise threshold on both needs.

### 24.5 Labels

Evaluation needs labelled windows. Labels come from investigated incidents, authorised tests and analyst review of samples.

Each label source has weaknesses. Investigated incidents are reliable but few; authorised tests are clean but may not look like real attacks; analyst reviews are plentiful but can be wrong. Recording where each label came from lets evaluators weight them and check whether results depend heavily on one kind of label. Beside each of her eight windows, Amara writes which source supplied its label and who confirmed it, so a reviewer can challenge any single label.

### 24.6 Small samples

Eight windows illustrate the method only; real evaluation uses weeks of data.

With eight windows, a single mislabelled one changes the results dramatically. Weeks of data give hundreds of windows, enough to estimate rates with useful confidence and to see variation between weekdays and weekends. The small set remains valuable for teaching and for unit tests, where every window can be checked by hand. Amara states the sample size beside every figure she reports, so nobody mistakes the teaching example for a measured performance of the rule in production.

### Rule naming and severity

Each variant gets a clear name and severity. 'Portal stuffing attempts' is low and queued; 'Portal possible takeover' is high and pages. Names tell analysts what to expect before they open the alert, which speeds triage and reduces confusion between similar rules.

### Worked example

Amara presents the results to Paolo as a table of variants, with a recommendation: page on "threshold 5 with success", queue "threshold 5 without success" for daytime review. The missed 10:10 attack window had no success, so the paging rule correctly stayed quiet — the attacker had not yet got in. This moves the paging threshold back from the 6 that the earlier tuning loop settled on to 5. That loop tuned the failures-only rule, where raising the threshold was the only way to cut false alerts. Once the success clause is added, it removes the false alerts by itself: on the lab windows, threshold 5 with a success has no false alerts and catches two attack windows, while 6 catches only one. Keeping 6 would lose detection and gain nothing, so R-07's threshold is amended to 5 through change control.

> **Synthetic case.** Windows and labels come from the lab script.

### Errors and limits

Labels themselves can be wrong; review disputed ones.

### Exercises

- **EX070 — Variant results.** Report TP, FP and FN for the three variants. *Rubric:* 3 = 5+success 2/0/1; 6+success 1/0/2; 5 no success 3/2/0; 2 = two; 1 = one; 0 = none.
- **EX071 — Two purposes.** Why keep both a success and a no-success variant? *Rubric:* 3 = attempts vs likely compromise; different queues; 2 = partial; 1 = pick one; 0 = none.
- **EX072 — The missed window.** Why is missing the 10:10 window acceptable for the paging rule? *Rubric:* 3 = no success yet: no compromise to page about; 2 = partial; 1 = not acceptable; 0 = none.

### Synthesis

Design rule variants for distinct purposes and choose them by measured results on labelled data.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) work in a team on an open-ended SOC design problem; (2) generate and compare alternative designs; (3) present a design with rationale; (4) respond to critique in a studio setting.

### 25.1 The studio problem

Teams design monitoring for Lindqvist's depot networks, where handheld scanners and old workstations cannot run agents. The design must detect unusual connections from depots into business systems.

Unusual connections might include a scanner talking to a finance server, or a depot workstation reaching systems it has never used before. Without agents, the design must rely on network observation. Teams also need to consider that depots differ in size and connectivity, so one design must work for a small rural depot and a large hub.

### 25.2 Generating alternatives

Amara's team lists three options: network flow monitoring at the depot-to-business boundary; a network detection sensor with protocol analysis; and tightening firewall rules with logging of denied connections.

Listing several options before evaluating any prevents the first idea from becoming the only one. The three differ in kind: one observes flows, one inspects content, one restricts traffic and records refusals. Each has different costs and blind spots, which the criteria comparison will bring out, and a hybrid may emerge once the pieces are understood.

### 25.3 Criteria

They compare options on visibility, cost, operational load, privacy and failure modes, using a weighted table.

Visibility asks what each option can see; cost includes hardware, licences and staff time; operational load asks who maintains it; privacy considers whether staff traffic content is collected; failure modes ask what happens when it breaks. Weights are agreed before scoring, and each score cites evidence such as a vendor datasheet or a measurement. Privacy carries a high weight because depot staff use the same network for personal messages during breaks, and the company's monitoring policy limits content collection.

### 25.4 Studio critique

Each team presents for ten minutes; peers and staff challenge assumptions. The studio values clear reasoning over polished slides.

Critique is aimed at the design, not the people. Typical challenges are 'what happens if the sensor fails?' or 'how will you know the rules work?'. Slides with impressive diagrams but no reasoning score poorly. Staff note recurring weaknesses across teams and address them in the next teaching session. Feedback is written on cards and handed to each team after its slot, so comments are not lost and quieter students can contribute too.

### 25.5 Iteration

After critique, teams revise. Amara's team learns that the boundary firewall already logs allowed and denied flows; combining firewall logs with a small number of allow rules is cheaper than a new sensor.

The finding came from asking depot IT staff during critique, which shows the value of involving people who know the existing systems. Using the firewall's existing logs costs almost nothing in hardware. Tight allow rules shrink normal traffic to a short list, so any denied or unexpected flow stands out clearly in the logs.

### 25.6 Documentation

The final design includes a diagram, data flows, requirements met, risks and a test plan.

The diagram shows where logs come from and where they go; data flows give formats and volumes; requirements met link back to the brief; risks state what could go wrong; the test plan shows how the design will be proved. A reviewer who missed the presentation should understand the design from the document alone. Amara's team limits the document to six pages. Appendices hold detail.

### 25.7 Teamwork

Roles rotate: presenter, scribe, critic. Everyone explains every part.

Rotating roles stops one confident member from presenting everything while others stay silent. The scribe records decisions and critique; the critic looks for weaknesses before outsiders do. Requiring everyone to explain every part means the staff can question any member, which reveals whether understanding is shared or held by one person. At the end, each member writes a short note on what they contributed and what they learned from another member, which staff read alongside the team's design.

### Privacy in the design

Depot devices are used by drivers and warehouse staff. The design logs connection metadata only, not content, and keeps it for 30 days, which the privacy officer reviews and approves. Teams include such reviews in the plan rather than adding them at the end.

### Worked example

The team's final design: restrict depot-to-business traffic to five required services, log all denied attempts, alert when a depot device attempts a new destination more than three times in an hour, and review weekly. Estimated cost: configuration time only. Main risk: firewall log feed failure, covered by heartbeat monitoring.

> **Synthetic case.** The studio and designs are invented.

### Errors and limits

Studio designs are untested; chapter 30's laboratory verifies them.

### Exercises

- **EX073 — Three options.** List the three depot monitoring options considered. *Rubric:* 3 = flow monitoring, network sensor, firewall tightening with logging; 2 = two; 1 = one; 0 = none.
- **EX074 — Critique outcome.** What did critique change in the design? *Rubric:* 3 = used existing firewall logs; cheaper than new sensor; 2 = partial; 1 = vague; 0 = none.
- **EX075 — Final design.** Summarise the final design and its main risk. *Rubric:* 3 = 5 services allowed, denied logged, alert on repeated new destinations, weekly review; feed failure risk; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Studios teach design through alternatives, criteria and critique; the cheapest good design often reuses what exists.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Security operations and blue team: architecture alternatives

### Learning outcomes

You will (1) compare SOC architecture models such as centralised, distributed and hybrid; (2) evaluate SIEM, data-lake and managed-service options; (3) weigh build-versus-buy decisions; (4) document architecture decisions with their reasons.

### 26.1 SOC models

Zimmerman (2014) and Knerler, Parker and Zimmerman (2022) describe SOC structures from small centralised teams to tiered, distributed and federated models. Lindqvist, with one head office and forty depots, runs a small central SOC with depot IT staff as local contacts.

Structure follows size and spread. A tiered model with many specialists suits a large organisation; a federated model suits one with independent business units. Lindqvist's forty depots are too many for central staff to visit but too small to have their own analysts, so depot IT contacts act as eyes and hands on site when needed.

### 26.2 Data platform options

A traditional SIEM indexes events for fast search and built-in rules. A data-lake approach stores cheaply and queries flexibly but needs more engineering. Many SOCs combine them: hot SIEM for recent, high-value data and a lake for long-term, bulk data.

A SIEM's indexing makes searches fast but costs storage and licence fees per volume. A lake stores raw data cheaply but searches more slowly and needs engineers to build queries and pipelines. Combining them puts data where its use justifies its cost: recent authentication logs in the SIEM, months of firewall logs in the lake.

### 26.3 Managed services

A managed detection provider can watch at night and bring wider threat knowledge, but knows less about local context and needs clear escalation agreements. Lindqvist considers using one for night coverage.

Night coverage by a provider can be cheaper than a full in-house night shift. The risks are that the provider escalates too much or too little, or lacks context to judge alerts. Clear agreements state which alerts the provider handles, what it may do on its own, and how quickly it must call Lindqvist's on-call engineer.

### 26.4 Build versus buy

Building gives control and fit; buying gives speed and support. Engineers estimate total cost over several years, including staff time, not just licence price.

A built tool fits exactly but needs people to maintain it after its authors move on. A bought tool comes with updates and support but may force processes to fit its design. Comparing five-year costs, including staff hours for integration and upkeep, often changes the picture from licence price alone. Lindqvist's comparison for its case system shows that a cheaper licence would cost more in integration work within two years, which tips the decision.

### 26.5 Decision records

Each major choice is written as an architecture decision record: context, options, decision, consequences. Future engineers can see why things are as they are.

Records are short, often one page, and written when the decision is made. Consequences include both benefits and costs, such as lock-in to a vendor format. When a later team wonders why the lake uses a particular format, the record explains the reasoning and the options rejected, saving them from repeating the analysis. Lindqvist stores them next to the code.

### 26.6 Reversibility

Prefer choices that can be undone. Keeping raw logs in an open format makes changing platforms later possible.

Some choices are hard to reverse: data stored only in a proprietary format may need costly conversion to move. Keeping raw logs in open formats such as JSON lines alongside the platform's own copy preserves options. Reversible choices let a team move faster, since a mistake can be corrected without a major project. Contract terms count too: a short initial term with a vendor is easier to leave than a five-year commitment signed for a discount.

### 26.7 Case

With storage growing (chapter 6), Lindqvist must decide whether to expand the SIEM or add a lake for firewall and DNS logs.

Expanding the SIEM keeps everything in one place but costs more as volume grows. Adding a lake for firewall and DNS logs, which are bulky but searched less often, keeps the SIEM for high-value data. Amara prepares the comparison with five-year cost estimates and the effect on investigation speed for each log type. The decision goes to the CISO with a recommendation and is recorded as a decision record.

### Worked example

Amara's decision record recommends keeping portal, identity and endpoint data in the SIEM for 90 days and sending firewall and DNS logs to a lake after 14 days, with searches from the lake for investigations. Consequence noted: lake queries take minutes, not seconds, so hunt playbooks must allow for that.

> **Synthetic case.** Options and decisions are invented.

### Errors and limits

Vendor claims about scale and cost need testing with your own data.

### Exercises

- **EX076 — Hybrid platform.** Explain the hybrid SIEM-plus-lake approach. *Rubric:* 3 = hot SIEM for recent high-value data, lake for bulk/long-term; 2 = partial; 1 = one only; 0 = none.
- **EX077 — Managed night cover.** Name one benefit and one risk of a managed provider for nights. *Rubric:* 3 = coverage and wider knowledge vs less local context, escalation agreements; 2 = one side; 1 = vague; 0 = none.
- **EX078 — Decision record.** What sections make up an architecture decision record? *Rubric:* 3 = context, options, decision, consequences; 2 = three; 1 = one; 0 = none.

### Synthesis

Compare SOC structures and data platforms on total cost, fit and reversibility, and record why decisions were made.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Security operations and blue team: control design

### Learning outcomes

You will (1) design detective and responsive controls with defined triggers and actions; (2) specify playbooks for common alerts; (3) design safeguards against harmful automated actions; (4) map controls to D3FEND techniques.

### 27.1 Detective and responsive controls

A detective control finds activity; a responsive control acts on it. For portal takeover, detection is the possible-takeover rule; response is locking the account, invalidating sessions and contacting the customer.

Each needs the other. A detection with no planned response leaves analysts unsure what to do at 3 a.m., while a response with no reliable detection either never triggers or triggers on the wrong accounts. Designing them together lets Amara match the strength of evidence to the strength of action: a likely takeover justifies invalidating sessions, while a mere attempt does not justify locking the customer out.

### 27.2 Playbooks

A playbook lists the steps an analyst follows for an alert type: verify, scope, contain, notify, record. It names the data to check and the decision points. NIST SP 800-61r3 places such response activities within the broader risk-management cycle.

Decision points are where the playbook asks the analyst to judge rather than follow: is the success from the customer's usual device? Has the address already been changed? Naming the data to check at each point stops analysts from skipping evidence under pressure. The playbook also says when to stop and escalate, so analysts know the limits of their own authority during an incident.

### 27.3 Automated actions

Some steps can be automated: invalidating a session is low-risk and fast. Others, such as blocking a network range, can harm legitimate users and need a human decision.

Invalidating a session forces a fresh login; if the customer is genuine, they simply sign in again, so a wrong decision costs little. Blocking a network range might cut off a mobile carrier serving thousands of customers, so a wrong decision costs a great deal. Amara sorts each candidate action by the cost of being wrong and only automates those where a mistake is cheap and easily reversed.

### 27.4 Safeguards

Automation needs limits: maximum actions per hour, exclusions for critical accounts, and automatic alerts if limits are reached. A runaway automation can lock out thousands of customers.

A rule bug or a flood of synthetic test events could trigger the automation thousands of times in minutes. A cap on actions per hour turns a potential disaster into a contained one. Critical accounts, such as those used by depot systems, are excluded because locking them would stop deliveries. Reaching a limit pauses the automation and pages an engineer, who decides whether to continue.

### 27.5 D3FEND mapping

D3FEND names defensive techniques such as authentication event thresholding and account locking. Mapping controls to it clarifies what each control actually does and helps find gaps.

Product names and marketing terms vary, which makes it hard to tell whether two tools overlap or leave gaps. D3FEND gives a shared vocabulary describing what a control does to the adversary's activity. Mapping Lindqvist's portal controls shows thresholding and account locking are present, while nothing yet analyses session behaviour after login, which suggests where to invest next.

### 27.6 Testing controls

Each control is tested with safe synthetic events, and response playbooks are rehearsed in exercises.

Synthetic events check that detection fires and that automation acts within its limits. Exercises check the human parts: does the analyst find the playbook, does customer service know what to tell a locked-out customer, does the escalation contact answer? Exercises often reveal small problems, such as an out-of-date phone number, that no technical test would catch. Findings from each exercise are logged with an owner and a date for the fix.

### 27.7 Case

Amara designs the possible-takeover playbook with Paolo and the customer service manager.

Involving customer service early matters because they will speak to customers whose accounts were locked. The manager asks for a short script explaining why access was reset and how to regain it, and for a field in the alert showing whether the customer has already been contacted. Both requests go into the playbook before it is tested. The finished playbook is rehearsed once with a synthetic alert before go-live, with the customer service manager playing the customer.

### Customer experience

Responsive controls touch customers. The hold message on the portal explains that the account is paused for safety and gives the support number, so legitimate customers are not left confused.

### Worked example

The playbook automates session invalidation and a temporary account hold, capped at 20 accounts per hour; above that, automation pauses and pages the on-call engineer. An analyst confirms within 30 minutes, contacts the customer through the registered phone number and records the outcome.

> **Synthetic case.** The playbook is invented.

### Errors and limits

Playbooks age as systems change; review after each use.

### Exercises

- **EX079 — Detective versus responsive.** Give a detective and a responsive control for portal takeover. *Rubric:* 3 = possible-takeover rule; lock account/invalidate sessions; 2 = one; 1 = confused; 0 = none.
- **EX080 — Automation safeguard.** What safeguard limits the automated hold? *Rubric:* 3 = cap of 20 accounts/hour; pause and page above it; 2 = partial; 1 = vague; 0 = none.
- **EX081 — Human decision.** Why should network-range blocking need a human? *Rubric:* 3 = may harm legitimate users; judgement needed; 2 = partial; 1 = speed; 0 = none.

### Synthesis

Design controls as detection plus response, automate low-risk steps with limits, and map controls to named defensive techniques.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Security operations and blue team: implementation I

### Learning outcomes

You will (1) implement a detection and its pipeline changes; (2) use staged environments; (3) manage configuration as code; (4) record implementation evidence.

### 28.1 From design to build

Implementation turns R-07 and the playbook into working parts: load-balancer log forwarding, parser updates, the rule, the alert routing and the automation.

R-07 is the requirement identifier for possible-takeover detection, and keeping that label through implementation lets each component point back to why it exists. Building the parts in dependency order matters: the rule cannot be tested until the parser produces the fields it needs, and routing cannot be checked until the rule creates alerts. Amara draws up a short build plan with that order.

### 28.2 Environments

Changes go first to a test SIEM with replayed synthetic data, then to production in monitor-only mode, then to alerting. Each stage has entry and exit criteria.

Entry criteria say what must be true before a change enters a stage, such as passing unit tests. Exit criteria say what must be shown before it leaves, such as a week in monitor-only mode with false alerts below the limit. Skipping stages saves days but risks discovering problems in production, where they affect analysts and customers.

### 28.3 Configuration as code

Parser configurations, rules and routing are stored in version control and deployed by a pipeline, not edited by hand in consoles. This makes changes reviewable and reversible.

Hand edits in a console leave no clear record of who changed what and why, and they are easy to make by mistake. A pipeline applies the same reviewed configuration every time. If a change causes problems, reverting the commit and redeploying restores the previous state in minutes, with a full record of what happened.

### 28.4 Parser updates

The load-balancer logs use a new format. Amara writes a parser, tests it on 1,000 sample lines, and checks that every field maps to the event model.

A thousand lines include normal requests, failures, unusual characters in usernames and a few malformed lines. Amara counts how many lines parse fully, how many partly and how many fail, and checks a sample by hand against the raw text. Fields such as client address must map to the event model's source field, or the rule will group the wrong values.

### 28.5 Change management

Production changes follow Lindqvist's change process: a ticket, a review, a window and a rollback plan.

The ticket describes the change and its purpose; review checks the risk; the window chooses a time when problems affect the fewest people; rollback says exactly how to undo it. Detection changes are sometimes treated as low-risk, but a parser change can break many rules at once, so they follow the same process as other production changes. Amara's first ticket is reviewed by Paolo and the SIEM administrator.

### 28.6 Evidence

Implementation records include commits, test results, change tickets and screenshots of monitor-only results. Auditors and future engineers use them.

Months later, someone may ask when the rule went live and whether it was tested. Commits answer what changed; test results answer whether it worked; tickets answer who approved it; monitor-only results answer how it behaved on real data before alerting. Keeping these together saves time in audits and during incident reviews. Amara links all four from the requirement's row in the traceability table, so the trail starts from R-07.

### 28.7 Pairing

Amara pairs with an analyst during routing configuration so alerts land where analysts expect them.

Engineers think in terms of rules and queues; analysts think in terms of shifts and workloads. The analyst points out that alerts routed to a general queue would be missed at night, when only the on-call queue is watched. Pairing catches that kind of mismatch before deployment, and gives the analyst a sense of ownership of the new alerts. They finish with a test alert that the analyst opens on the on-call screen.

### Rollback rehearsal

Before the production change, Amara rehearses rollback in the test SIEM: she deploys the new parser, then restores the previous version from version control and checks that parsing returns to the old behaviour. A rollback never practised is a hope, not a plan. The rehearsal takes ten minutes and is recorded in the change ticket.

### Worked example

During the test stage, 12 of 1,000 sample lines fail to parse: they contain an extra field added by a balancer update. Amara extends the parser, adds the 12 lines as test cases and re-runs: 1,000 parse cleanly. Only then does she request the production change.

> **Synthetic case.** Lines and counts are invented.

### Errors and limits

Test data may not include every production variant; monitor parse errors after release.

### Exercises

- **EX082 — Stages.** Describe the three implementation stages. *Rubric:* 3 = test SIEM with replay, production monitor-only, alerting; 2 = two; 1 = one; 0 = none.
- **EX083 — Parse failures.** What caused the 12 parse failures, and how were they handled? *Rubric:* 3 = extra field from balancer update; parser extended, lines added as tests; 2 = partial; 1 = ignored; 0 = none.
- **EX084 — Configuration as code.** Why deploy configuration from version control? *Rubric:* 3 = reviewable, reversible, consistent; 2 = partial; 1 = style; 0 = none.

### Synthesis

Implement through staged environments, version-controlled configuration and recorded evidence.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Security operations and blue team: measurement

### Learning outcomes

You will (1) define SOC metrics linked to goals; (2) compute robust summaries of response times; (3) avoid metrics that distort behaviour; (4) present measurements with context.

### 29.1 Why measure

Knerler, Parker and Zimmerman (2022) treat measurement as a strategy: "measure performance to improve performance". Metrics show whether changes help and where effort should go.

Without measurement, a SOC cannot tell whether a new rule reduced harm or just added noise, or whether a staffing change helped. Measures also support honest conversations with management about what the team can deliver. The aim is improvement, not judging individuals, which affects how metrics are chosen and shared. Lindqvist starts with a handful of measures and adds more only when a clear question needs answering.

### 29.2 Choosing metrics

Good SOC metrics tie to goals: time from detection to acknowledgement, share of incidents detected internally rather than reported by customers, coverage of priority techniques, and false-alert rates per rule.

Each metric should answer a question someone actually asks. Time to acknowledgement tells the CISO how quickly the SOC reacts; internal versus customer-reported detection shows whether monitoring finds problems first; technique coverage shows breadth; false-alert rates per rule show where tuning is needed. Collecting metrics nobody uses wastes effort and clutters reports.

### Lab — response-time summaries

```python
"""Median and 90th percentile of detection-to-acknowledgement minutes (synthetic)."""
import statistics
minutes = [3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 11, 12, 14, 18, 41]
q = statistics.quantiles(minutes, n=10, method="inclusive")
print(f"n={len(minutes)} mean={statistics.mean(minutes):.1f} median={statistics.median(minutes)} p90={q[8]:.1f}")
```

Run with `python3 lab_latency.py`. Verified output:

```text
n=15 mean=10.2 median=7 p90=16.4
```

### 29.3 Reading the result

Fifteen acknowledgement times give a mean of 10.2 minutes but a median of 7 and a 90th percentile of 16.4. One 41-minute case pulls the mean up. The median describes the typical case, the 90th percentile the slow tail that matters for the 15-minute requirement.

Reporting only the mean would suggest the team typically takes ten minutes, when most acknowledgements happen in about seven. Reporting only the median would hide that a tenth of cases take over sixteen minutes, beyond the requirement. Amara looks at the 41-minute case separately and finds it arrived during a shift handover, which points to a process fix.

### 29.4 Distorting metrics

Kokulu et al. (2019) found metric mismatches common in SOCs. Rewarding fast closure can produce careless closure. Pair speed metrics with quality checks, such as reviewed samples of closed alerts.

Once a number becomes a target, people find ways to move it that do not reflect real improvement. If analysts are judged by alerts closed per hour, quick closures without investigation become rational. Using several metrics together makes any single one harder to game. The sample of closed alerts is drawn at random each week, so analysts cannot predict which closures will be reviewed.

### 29.5 Context

A metric without context misleads: acknowledgement time rose last month because night staffing fell, not because analysts slowed. Reports include such explanations.

A chart showing slower acknowledgements could lead managers to blame analysts or demand overtime. With the explanation that night staffing fell from two to one, the conversation turns to staffing decisions instead. Amara adds a short notes column to the monthly report for events such as staffing changes, incidents and new rules. Reports compare each month with the same month last year where seasonal patterns matter.

### 29.6 Data quality

Metrics depend on case-system timestamps; analysts who acknowledge late in the tool but act early make data wrong. Training and tooling fix this.

If analysts start investigating from an email notification and only click acknowledge later, the case system records a slower time than reality. The metric then misleads in the opposite direction. Making acknowledgement automatic when an analyst opens the alert, and training staff on why timestamps matter, aligns the data with what actually happened. Amara checks a sample of cases against chat logs.

### Coverage metrics

Coverage of priority ATT&CK techniques is measured as the share with at least one tested detection. Untested detections do not count, because a rule that has never fired on a safe test event may not work. Lindqvist reports this share quarterly, with the list of gaps attached so the figure cannot hide which techniques are missing.

### Worked example

Amara reports: "Median acknowledgement 7 minutes, 90th percentile 16.4 against a 15-minute target. The slowest case (41 minutes) occurred during a shift handover; we propose overlapping handovers by 15 minutes."

> **Synthetic case.** Times come from the lab script.

### Errors and limits

Fifteen values are few; percentiles from small samples are unstable.

### Exercises

- **EX085 — Lab summaries.** Report the mean, median and 90th percentile. *Rubric:* 3 = 10.2, 7, 16.4; 2 = two; 1 = one; 0 = none.
- **EX086 — Why median.** Why describe acknowledgement with median and percentile rather than mean? *Rubric:* 3 = skewed; outlier pulls mean; tail matters for target; 2 = partial; 1 = mean fine; 0 = none.
- **EX087 — Distortion guard.** How can a speed metric be kept from causing careless closure? *Rubric:* 3 = pair with quality checks of reviewed closed alerts; 2 = partial; 1 = remove metrics; 0 = none.

### Synthesis

Measure what links to goals, summarise robustly, guard against distortion and always report context.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify detection logic with automated unit tests; (2) verify pipeline behaviour with safe synthetic events; (3) record verification evidence; (4) distinguish verification from validation.

### 30.1 Verification versus validation

Verification asks "did we build it right?" — does the rule behave as specified? Validation asks "did we build the right thing?" — does it help detect real threats in operation? This laboratory focuses on verification.

A rule can pass every verification test and still be useless if it targets behaviour attackers do not use, or if real attacks look different from the test data. Validation answers that question later, with operational evidence. Keeping the two separate stops a team from claiming a rule 'works' when they have only shown it matches its specification.

### 30.2 The laboratory

The laboratory is a test SIEM isolated from production, with replayed synthetic logs. No real customer data and no attack tools are used; test events are crafted log records that look like the behaviour the rule targets.

Isolation stops test events from reaching production analysts and wasting their time. Replayed synthetic logs give realistic volume and variety without exposing customer data. Crafted records let the tester control exactly which conditions are present, which is how boundary cases are tested precisely. The laboratory is rebuilt from configuration so its state is known before each run.

### Lab — unit tests for the burst rule

```python
"""Unit tests for a detection function, run with the standard library (synthetic cases)."""
import io, unittest
def burst(users_failed, any_success, threshold=5):
    return users_failed >= threshold and any_success
class T(unittest.TestCase):
    def test_fires_at_threshold(self): self.assertTrue(burst(5, True))
    def test_quiet_below(self): self.assertFalse(burst(4, True))
    def test_needs_success(self): self.assertFalse(burst(9, False))
    def test_zero(self): self.assertFalse(burst(0, False))
if __name__ == "__main__":
    r = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(unittest.defaultTestLoader.loadTestsFromTestCase(T))
    print("tests run", r.testsRun, "failures", len(r.failures))
```

Run with `python3 lab_unittest.py`. Verified output:

```text
tests run 4 failures 0
```

### 30.3 Reading the result

Four tests run and none fail: the rule fires at exactly 5 distinct failing users with a success, stays quiet at 4, stays quiet without a success even at 9 users, and stays quiet with no activity. These encode the boundary and the success clause decided in chapters 9 and 24.

Each test checks one aspect of behaviour. Firing at five and staying quiet at four pins down the threshold exactly; staying quiet at nine without a success shows that the success clause really is required; staying quiet with no activity shows the rule does not misfire on empty windows. Four passing tests together describe the rule's intended behaviour.

### 30.4 Pipeline tests

Unit tests check logic; pipeline tests check that a synthetic record entering the collector produces an alert in the case system with correct fields. Amara injects three records and checks each field in the resulting alert.

A rule can be correct while the pipeline around it breaks: a field renamed by the parser, a routing rule sending alerts to the wrong queue, or a time conversion error. Checking every field in the final alert, such as customer ID, source network and subsequent actions, confirms the whole chain works, not just the rule's logic.

### 30.5 Evidence

The laboratory record lists the test, version, input, expected and actual results, date and tester.

Recording the rule version ties each result to an exact configuration, so a later change can be compared. Expected and actual results side by side make failures obvious. The tester's name and date show accountability. These records become part of the evidence that the rule was verified before going live. Failed tests stay in the record after they are fixed, alongside the rerun, so the history shows what went wrong and how it was corrected.

### 30.6 Repeatability

Tests run automatically on each rule change, so verification is continuous, not a one-off.

Rules change often through tuning, parser updates and field renames. A test run only once at creation says nothing about the rule six months later. Running the suite on every change catches regressions immediately, and a failing test blocks deployment until someone fixes the rule or justifies changing the test. The suite takes under two minutes, so engineers run it locally before proposing a change, and the shared pipeline runs it again before merging.

### Test data hygiene

Synthetic test records carry a marker field so they never mix with real alerts or metrics.

### Worked example

The pipeline test reveals that the alert lacks the customer ID: the routing template referenced an old field name. Amara fixes the template, re-runs, and records both the failure and the fix. The unit tests alone would never have found this.

> **Synthetic case.** Tests and records are synthetic.

### Errors and limits

Passing verification does not show the rule catches real attackers; that is validation, covered in chapter 38.

### Exercises

- **EX088 — V and V.** Distinguish verification from validation. *Rubric:* 3 = built right vs right thing; spec vs real effectiveness; 2 = partial; 1 = same; 0 = none.
- **EX089 — Four tests.** What do the four unit tests check? *Rubric:* 3 = threshold boundary 5/4, success clause, empty input; 2 = three; 1 = one; 0 = none.
- **EX090 — Pipeline finding.** What did the pipeline test catch that unit tests could not? *Rubric:* 3 = missing customer ID from template field name; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Verify logic with unit tests and the whole pipeline with safe synthetic events, recording every result.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Security operations and blue team: implementation II

### Learning outcomes

You will (1) implement depot network monitoring from the studio design; (2) integrate firewall logs and allow-list policy; (3) implement enrichment for depot assets; (4) manage rollout across many sites.

### 31.1 From studio to production

The depot design from chapter 25 now becomes real: restrict depot-to-business traffic to five services, log denials, and alert on repeated attempts to new destinations.

Five services cover what depots legitimately need from business systems, such as delivery updates and stock queries. Everything else is denied and logged. Alerting on repeated attempts to new destinations filters out one-off mistakes while catching a device persistently trying to reach systems it should not, which is the behaviour the design was meant to reveal.

### 31.2 Asset enrichment

Detection needs to know which addresses are depots. Amara works with IT to add depot subnets and device types to the asset inventory, then to the enrichment tables.

Without enrichment, a denial log shows only an address, and an analyst must look up which depot and device it belongs to. With depot subnets and device types in the inventory, alerts arrive showing 'handheld scanner, Depot 14' immediately. The inventory work also helps IT operations, who had no complete list of depot devices before.

### 31.3 Phased rollout

Forty depots cannot change at once. Three pilot depots go first; issues found there are fixed before the rest follow in groups of ten.

Three pilot depots are chosen to cover different sizes and equipment, so problems that affect only some depot types are likely to appear. Groups of ten after that keep the number of depots affected by any new problem manageable. Each group starts only after the previous one has run cleanly for a set period. Lessons are written up after each group.

### 31.4 Pilot findings

In the pilot, a label printer at one depot needs to reach a print server not on the allowed list. The firewall denies it, printing stops and the depot calls IT. The team adds the print service, documents why, and checks other depots for the same printers before the next group.

The printer problem shows why the allowed list needs input from people who know depot operations, not just network diagrams. Checking other depots before the next group prevents the same outage elsewhere. Documenting why the print service was added keeps the allowed list understandable, so future reviewers do not remove it as an unexplained exception.

### 31.5 Coordination

Depot managers get a notice before changes, a contact number and a rollback promise.

Depot managers run busy sites where an unexplained outage can delay deliveries. A notice in advance lets them plan around the change; a contact number gives them someone to call; a rollback promise reassures them that a problem will be reversed quickly rather than debated. Good coordination makes later rollouts easier because trust has been built. Afterwards, managers are asked how the change went. Their answers shape the next notice.

### 31.6 Monitoring the rollout

A dashboard shows denials per depot per hour; a spike after a change signals a missed legitimate service.

Before a change, denials at a depot are near zero because traffic was not restricted. A sharp rise immediately after the change usually means a legitimate service was missed, as with the printer. Watching the dashboard during each rollout window lets the team react within minutes rather than waiting for complaints from depot staff. A spike outside a rollout window is treated as a possible security event instead.

### 31.7 Closure

After all depots, the team reviews denial rates and alert volume against the design estimates.

Comparing actual results with estimates checks whether the design assumptions held. If denials are far higher than expected, the allowed list may still be missing services; if alerts are far higher, thresholds may need tuning. The review is written up and linked to the design document, closing the loop from studio to operation. Paolo reads it before the project is closed, and the final figures become the baseline for routine monitoring of depot traffic from then on.

### Documenting exceptions

Every allowed service has an owner and a reason in the policy file.

### Worked example

After rollout, depot denials average 40 per day across all sites, mostly devices retrying an old update server. The new-destination alert fires twice in the first week; both are a contractor's laptop connected to a depot network. The second leads IT to enforce network access control for visiting devices.

> **Synthetic case.** Depots, devices and counts are invented.

### Errors and limits

Restricting traffic can break unknown dependencies; pilots reduce but do not remove that risk.

### Exercises

- **EX091 — Phased rollout.** Why pilot at three depots first? *Rubric:* 3 = find issues like printer dependency before wider impact; 2 = partial; 1 = speed; 0 = none.
- **EX092 — Printer issue.** How was the printer problem handled? *Rubric:* 3 = added print service, documented, checked other depots before next group; 2 = partial; 1 = removed restriction; 0 = none.
- **EX093 — Contractor alert.** What did the new-destination alerts reveal, and what followed? *Rubric:* 3 = contractor laptop on depot network; network access control enforced; 2 = partial; 1 = false alarms; 0 = none.

### Synthesis

Implement site-wide changes with enrichment, pilots, coordination and monitoring of side effects.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Security operations and blue team: reliability

### Learning outcomes

You will (1) define reliability targets for the monitoring pipeline; (2) identify single points of failure; (3) design redundancy and graceful degradation; (4) measure availability and data completeness.

### 32.1 Reliability targets

The pipeline has a target of 99.5% availability and 99.9% completeness of priority sources. Completeness — the share of expected events that arrive — matters as much as uptime, because a running pipeline with missing data still blinds the SOC.

Uptime alone is misleading: a pipeline can be running while silently dropping a share of events. Completeness measures what actually arrives. For priority sources such as authentication logs, 99.9% means at most one event in a thousand lost, which keeps the chance of missing an attack's key event low while remaining achievable with reasonable engineering.

### 32.2 Single points of failure

Lindqvist's pipeline has one collector per site and one load-balancer log feed. If either fails, a whole source disappears.

One collector per site means a hardware fault there silences every source at that site until it is repaired. The single load-balancer feed means takeover detection depends on one path. Listing these points is the first step; deciding which to remove depends on cost and on the detections each one supports. Amara lists both on the failure analysis with the detections each one supports, which shows the feed carries the most important detection.

### 32.3 Redundancy

Two collectors per site in active-passive mode, and a second feed path for load-balancer logs, remove the main single points. Redundancy costs money, so it goes first where detection value is highest.

Active-passive means one collector works while the other waits, taking over if the first fails. That is simpler than splitting load between both and avoids duplicate events. Starting with sites and feeds that support the most important detections gives the most protection for each unit of budget, and lower-value sources follow if budget allows.

### 32.4 Graceful degradation

When the SIEM is overloaded, the pipeline should drop low-value debug logs first, not authentication logs. Priority queues implement this.

When capacity runs short, something must be lost; the question is what. Debug logs are rarely needed for detection, while authentication logs are central. Priority queues let the pipeline drop low-priority events first under pressure. The drop is logged, so the SOC knows which data are missing for that period. Priorities are set per source in the pipeline configuration and reviewed when new sources join.

### 32.5 Measuring completeness

Comparing events counted at sources with events stored in the SIEM shows loss. A daily reconciliation report lists sources below 99.9%.

Sources can report how many events they sent, and the SIEM knows how many it stored; the difference is loss in between. Where sources cannot report counts, collectors can count what they received instead. The daily report lists each source's ratio, and any below target gets investigated by the source owner. The report goes to source owners each morning and is summarised weekly for Paolo.

### 32.6 Error budgets

If availability falls below target, new features pause and reliability work takes priority until the budget recovers.

A 99.5% target leaves 0.5% of time as an allowance for downtime. This gives a clear, pre-agreed rule for balancing new work against stability, instead of a fresh argument each time something breaks. The budget resets each quarter; at 99.5%, the allowance is about eleven hours per quarter. Product managers and SOC leads agree this rule in advance, so pausing feature work when the budget is spent is routine rather than a dispute.

### 32.7 Case

In week one of reconciliation, the portal web servers show 99.95% completeness; the depot firewall shows 97.8% because of a UDP syslog path that drops packets under load.

UDP syslog sends messages without confirmation, so packets dropped under load are simply lost. A 2.2% loss means about one denial in fifty never reaches the SIEM. Switching the depot firewall to TCP or a forwarding agent with acknowledgement and buffering would fix it, and the reconciliation report will show whether completeness rises above target.

### Monitoring the monitors

Collectors, parsers and the SIEM itself report health metrics — queue depth, parse errors, ingestion lag — to a separate monitoring system. If the SIEM is unhealthy, it cannot be trusted to alert on its own failure, so the health alerts go through an independent path to the on-call engineer.

### Worked example

Amara moves the depot firewall to TCP-based log forwarding with a local buffer. Completeness rises to 99.96%. She adds the change to the reliability log and keeps the reconciliation report running daily.

> **Synthetic case.** Figures are invented.

### Errors and limits

Completeness checks depend on accurate source counts, which some devices do not provide.

### Exercises

- **EX094 — Completeness.** Why is completeness as important as availability? *Rubric:* 3 = pipeline can run while missing data, still blinding SOC; 2 = partial; 1 = less important; 0 = none.
- **EX095 — Degradation order.** Under overload, which logs should drop first? *Rubric:* 3 = low-value debug before authentication; priority queues; 2 = partial; 1 = random; 0 = none.
- **EX096 — Firewall fix.** What caused the 97.8% completeness, and what fixed it? *Rubric:* 3 = UDP syslog drops; TCP forwarding with buffer; 99.96%; 2 = partial; 1 = ignored; 0 = none.

### Synthesis

Reliable monitoring needs targets for both uptime and completeness, redundancy where value is highest and graceful degradation.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Security operations and blue team: safety and resilience

### Learning outcomes

You will (1) assess safety risks of SOC actions on operations; (2) design response that preserves critical services; (3) plan SOC resilience when its own systems fail; (4) exercise resilience scenarios.

### 33.1 Safety of response

Response actions can harm the business. Isolating a depot workstation might stop dispatch for a shift. Playbooks state which assets are safety- or business-critical and require approval before isolating them.

A dispatch workstation that stops for a shift could leave dozens of trucks without routes and customers without deliveries. That harm may exceed the risk from a suspicious process, especially if the evidence is weak. Requiring approval for critical assets makes the trade-off explicit: the analyst presents the evidence, the business owner weighs operational impact, and the decision and its reasons are recorded in the case.

### 33.2 Critical services

Lindqvist lists services that must continue: dispatch, driver routing, customer tracking and payments. For each, the SOC agrees acceptable actions and contacts in advance.

Agreeing actions in advance avoids arguments during an incident, when time is short and stress is high. For dispatch, the agreed action might be blocking one suspicious connection rather than isolating the whole machine. Each service has a named business contact with a phone number that works at night, and the list is checked every quarter because people change roles.

### 33.3 SOC resilience

The SOC itself can fail: the SIEM may go down, the case system may be unavailable, or the SOC office may be inaccessible. NIST CSF 2.0's Recover function and SP 800-61r3 call for planning and practising recovery.

A SOC that depends entirely on its SIEM is blind when the SIEM is down, which is exactly when an attacker who caused the outage would act. Planning for recovery means listing the SOC's own dependencies, deciding how long each can be missing, and preparing alternatives. Practising those plans matters, because untested recovery steps often fail on the first real attempt.

### 33.4 Fallbacks

If the SIEM fails, analysts can query critical sources directly using read-only accounts and runbooks. If the case system fails, a shared offline template records actions until it returns.

Read-only accounts let analysts look at authentication and firewall logs on their source systems without risk of changing them. Runbooks give the exact steps, since analysts used to the SIEM's interface may not know each source's own tools. The offline template captures times, actions and decisions, so the case history can be entered into the case system afterwards without gaps.

### 33.5 Exercises

Twice a year the SOC rehearses: "SIEM unavailable for four hours during a portal attack". Rehearsals reveal missing access, outdated runbooks and unclear roles.

Combining an outage with an attack makes the exercise realistic: real failures often coincide with incidents, sometimes because the attacker caused them. Four hours is long enough for workarounds to be needed rather than waited out. Observers note where analysts hesitated, which steps were missing and which contacts did not answer, and each finding gets an owner and a deadline.

### 33.6 Recovery

After a failure, the SOC checks for gaps in data, replays buffered logs and reviews whether detections missed anything during the outage.

Logs buffered at sources or collectors during the outage may arrive in a burst when the SIEM returns. Rules that run on live data may not process them, so engineers rerun key detections over the outage window. Any gap that could not be recovered is recorded, so later investigations know that period has incomplete data. Paolo signs off the gap list.

### 33.7 Case

In the first exercise, analysts discover the read-only accounts for direct log access had expired.

Nobody had noticed because the accounts were never used in normal operations; they expired silently under the password policy. Had the outage been real, analysts would have lost an hour or more getting access approved. The fix is a quarterly check that logs into each fallback account, and an alert two weeks before any of them expires. Amara also adds the fallback accounts to the access review list, so their owners confirm each quarter that they are still needed.

### Communication during failure

When SOC systems fail, the SOC tells IT operations and the CISO what visibility is lost and for how long, so others can take extra care.

### Worked example

The exercise report lists three findings: expired direct-access accounts (renewed and added to quarterly checks), runbook steps referring to retired servers (updated), and no agreed decision-maker for isolating dispatch systems at night (the operations duty manager is named). The next exercise is scheduled.

> **Synthetic case.** The exercise is invented.

### Errors and limits

Exercises are planned; real failures surprise. Keep runbooks simple enough to use under stress.

### Exercises

- **EX097 — Critical assets.** Why must playbooks mark critical assets? *Rubric:* 3 = isolation could stop dispatch; need approval; 2 = partial; 1 = no reason; 0 = none.
- **EX098 — SIEM fallback.** What can analysts do if the SIEM fails? *Rubric:* 3 = query critical sources directly with read-only accounts and runbooks; 2 = partial; 1 = wait; 0 = none.
- **EX099 — Exercise findings.** List the three exercise findings. *Rubric:* 3 = expired accounts, outdated runbooks, no night decision-maker; 2 = two; 1 = one; 0 = none.

### Synthesis

Safe response protects critical services, and a resilient SOC plans and rehearses how to work when its own systems fail.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Security operations and blue team: integration

### Learning outcomes

You will (1) integrate the SOC with IT service management, identity and customer service systems; (2) design reliable interfaces and data exchanges; (3) handle integration failures; (4) test integrations end to end.

### 34.1 Why integration matters

A detection is only useful if its result reaches the people and systems that act. The possible-takeover alert must reach the case system, the customer service queue and the identity platform that holds accounts.

An alert sitting in the SIEM helps nobody until an analyst acts on it, a customer service agent knows what to tell the customer, and the identity platform actually blocks the account. Each handover is a point where information can be lost or delayed. Integration design maps every handover, including what data must pass across it and how quickly.

### 34.2 IT service management

Alerts that need IT action, such as fixing a log feed, become tickets in the IT service system with agreed priority mapping: SOC "high" means IT "P2", with a four-hour response.

Without an agreed mapping, a SOC 'high' might land in IT's queue as a routine request and wait days. The mapping translates urgency into terms the receiving team already uses. Four hours is agreed with IT as realistic for their staffing. Tickets carry a link back to the SOC case, so both teams can follow progress.

### 34.3 Identity platform

The automation calls the customer identity platform's interface to place holds and invalidate sessions. The interface uses a dedicated service account with only those permissions, and every call is logged.

A dedicated account with only hold and invalidate permissions limits damage if the automation is misused or compromised: it cannot read customer data or change passwords. Logging every call creates an audit trail showing which accounts were held, when and by which alert. Those logs are themselves monitored for unusual volumes.

### 34.4 Customer service

Customer service sees a simplified view: "account on security hold, reason: suspicious login, contact customer by registered phone". They do not see raw logs.

Raw logs contain details that customer service does not need and could misread or disclose. The simplified view gives exactly what an agent needs to act: that the account is held, why in plain terms, and how to contact the customer safely. Using the registered phone number guards against an attacker who changed the email address.

### 34.5 Interface contracts

Each integration has a contract: data fields, formats, rate limits, error codes and owner. Contracts prevent silent breakage when one side changes.

Rate limits matter because the automation might call the identity platform many times during a large incident. Error codes let the automation tell 'account not found' from 'platform overloaded'. Owners on both sides are notified of planned changes. Contracts are stored with the integration code and tested, so a breaking change shows up before production. Version numbers mark each contract revision.

### 34.6 Failure handling

If the identity platform does not respond, the automation retries twice, then raises a high-priority alert for manual action. It never assumes success.

Assuming success when the platform does not answer could leave a compromised account active while the SOC believes it is held. Two retries cover brief network hiccups without delaying too long. The manual alert gives an analyst the details needed to place the hold by hand through the platform's console, and the case records which path was used.

### 34.7 Testing

Integration tests run monthly with a synthetic test customer account reserved for this purpose.

A reserved test account behaves like a real customer but belongs to no one, so holds and session invalidation can be exercised safely. Monthly testing catches changes on the identity platform's side, such as a renamed field or a revoked permission. Test results are logged and failures open a ticket with the integration owner. A test that leaves the reserved account on hold is itself a failure, so the test ends by releasing the hold and checking that the account works normally again.

### Ownership of integrations

Each integration has an owner on both sides who is told before changes.

### Worked example

The first monthly test fails: the hold is placed but the customer service queue never receives the case, because a firewall change blocked the SOC's connection to the service system. The failure-handling path alerts the on-call engineer, who fixes the rule; the test is re-run and passes.

> **Synthetic case.** Systems and tests are invented.

### Errors and limits

Integrations multiply dependencies; each one is a new place to fail.

### Exercises

- **EX100 — Priority mapping.** Why map SOC priorities to IT priorities explicitly? *Rubric:* 3 = shared meaning and response times across teams; 2 = partial; 1 = style; 0 = none.
- **EX101 — Least-privilege account.** How is the identity interface account limited? *Rubric:* 3 = only hold and invalidate permissions; all calls logged; 2 = partial; 1 = admin account; 0 = none.
- **EX102 — Test failure.** What did the first integration test reveal? *Rubric:* 3 = firewall change blocked case delivery; failure path alerted; fixed; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Integrations carry detections to action; contracts, least privilege, failure handling and regular tests keep them working.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design a solution to a cross-cutting SOC problem in a team; (2) balance technical, human and cost factors; (3) produce a design ready for implementation; (4) critique other teams' designs constructively.

### 35.1 The problem

Night shift has two analysts. Studio II asks teams to reduce night alert load by 40% without increasing missed priority incidents.

Two analysts at night cannot investigate everything that arrives, so some alerts wait or are closed quickly. Reducing load without increasing missed incidents is a constraint pulling in two directions, which is what makes it a design problem rather than a simple cut. Teams must show evidence for both halves of the goal. Teams receive a month of anonymised alert data and the incident list for the same period, so their proposals can be checked against what actually happened.

### 35.2 Options explored

Amara's team considers: moving low-severity rules to a morning queue; a managed provider for overflow; automation of enrichment so each alert takes less time; and stricter rule promotion criteria.

Each option attacks load differently: rescheduling removes alerts from the night entirely, overflow shares them with outsiders, enrichment makes each one quicker, and promotion criteria stop new noisy rules from reaching nights. They can be combined, but each has risks, such as morning backlogs or the provider's lack of context. Costs are estimated for each.

### 35.3 Analysis

Using a month of alert data, they find 55% of night alerts come from five rules, three of which have never led to an incident. Moving those three to morning review cuts night load by 31%. Automated enrichment saves about two minutes per remaining alert.

Data change the discussion from opinion to evidence. Five rules generating over half the night alerts is a typical concentration, and three of them with no incidents ever is strong evidence of low value at night. Two minutes saved on each remaining alert adds up across a shift, giving analysts time for real investigations.

### 35.4 Human factors

Analysts in the studio session warn that moving alerts to morning creates a morning backlog. The team schedules a 30-minute morning review slot and limits the queue.

Engineers might count the problem solved once alerts leave the night queue, but analysts know someone must handle them later. A morning backlog left unchecked would grow and push other work aside. Scheduling a fixed slot and limiting the queue keeps the moved work visible and bounded. The analysts also ask that morning review be shared on a rota, so it does not fall on whoever arrives first.

### 35.5 The design

Move three rules to morning review; automate enrichment for the top ten alert types; set promotion criteria for new night-paging rules (precision above 0.3 in monitor-only mode); review after one month.

Each element addresses a finding: rescheduling the three no-incident rules, enrichment for the most common alert types, and promotion criteria so new rules prove their value before paging anyone at night. A precision above 0.3 means at least three in ten alerts are real. The one-month review checks both load and missed incidents.

### 35.6 Critique of others

Amara's team questions another team's proposal to page only on "critical" assets: the asset inventory marks only 40% of systems, so many unclassified assets would never page.

The flaw is in the data, not the idea: paging only on critical assets would work if criticality were known for every system. With only 40% classified, the other 60% would never page, whatever happened on them. Amara's team suggests treating unclassified assets as critical until the inventory is completed. The other team accepts the point and revises its proposal before the final presentation.

### 35.7 Readiness

The design includes owners, a timeline and a rollback: rules can be restored to night paging in minutes.

Owners make sure each change has someone responsible for it. The timeline sets when each part goes live and when the review happens. Rollback in minutes means that if missed incidents rise, the three rules return to night paging immediately, which makes the trial safe to run. The one-month review compares night alert counts and missed priority incidents with the month before, using the same definitions. Paolo and the night-shift lead attend it together.

### Worked example

The estimated effect: 31% fewer night alerts from rule moves plus time saved by enrichment, equivalent to a 42% reduction in analyst minutes. Risk: a real incident from a moved rule waits until morning; mitigated because those three rules have high-severity companions that still page.

> **Synthetic case.** Data and designs are invented.

### Errors and limits

Estimates from one month may not hold during seasonal peaks such as holiday deliveries.

### Exercises

- **EX103 — Load source.** What did the alert data reveal? *Rubric:* 3 = 55% from five rules; three never led to incidents; 2 = partial; 1 = vague; 0 = none.
- **EX104 — Morning backlog.** How did the design address the analysts' warning? *Rubric:* 3 = scheduled 30-minute morning slot and queue limit; 2 = partial; 1 = ignored; 0 = none.
- **EX105 — Constructive critique.** What weakness did Amara's team find in another design? *Rubric:* 3 = paging only critical assets misses unclassified 60%; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Cross-cutting studio problems need data, human input and constructive critique to reach implementable designs.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Security operations and blue team: performance and scale

### Learning outcomes

You will (1) size SIEM ingestion and storage from source rates; (2) plan for peaks; (3) measure query performance; (4) decide what to filter, summarise or tier.

### 36.1 Events per second

Ingestion is measured in events per second (EPS). Summing sources gives the average; peaks during incidents or business hours can be several times higher.

Average EPS sets the baseline for storage and licensing; peak EPS sets the size of collectors and processing. A system sized only for the average will lag or drop events exactly when activity spikes, often during an incident. Engineers measure EPS per source over several weeks to see daily, weekly and seasonal patterns. Amara records results per source in a table.

### Lab — sizing the pipeline

```python
"""Events-per-second and storage sizing for a SIEM (synthetic sources)."""
sources = {"portal_web": 900, "windows_events": 1400, "firewall": 2600, "dns": 1100}  # average EPS
bytes_per_event = 550
peak_factor = 2.5
eps = sum(sources.values())
gb_day = eps * bytes_per_event * 86400 / 1e9
print(f"average EPS={eps} peak EPS={eps*peak_factor:.0f}")
print(f"raw GB/day={gb_day:.1f}  90-day hot TB={gb_day*90/1000:.1f}")
```

Run with `python3 lab_capacity.py`. Verified output:

```text
average EPS=6000 peak EPS=15000
raw GB/day=285.1  90-day hot TB=25.7
```

### 36.2 Reading the result

Four sources give 6,000 EPS on average and 15,000 at a 2.5× peak. At 550 bytes per event, raw volume is 285.1 GB per day, and 90 days hot would need 25.7 TB — far above the 12 TB tier, confirming the need for the tiering decided in chapter 26.

The arithmetic: 6,000 events per second times 86,400 seconds times 550 bytes gives about 285 GB a day. Ninety days of that is far beyond the hot tier. Peak rate matters for processing but not for storage, since storage follows the daily total. The comparison makes tiering a necessity rather than an option.

### 36.3 Peaks

Pipelines must handle peaks without dropping priority data. Buffers absorb short spikes; sustained peaks need capacity or graceful degradation.

A buffer acts like a reservoir: it fills during a spike and drains when the rate falls. If a peak lasts longer than the buffer can hold, events must be dropped or processed more slowly. Graceful degradation decides which events go first, keeping authentication and other priority sources intact. Buffer sizes are set from the longest spikes measured on each source over the past year, with a margin, and the margin is checked again after any major new source joins.

### 36.4 Reducing volume

Options: filter events with no detection or investigation value, summarise high-volume sources (for example, firewall flows into hourly aggregates), and tier storage. Each reduction is checked against detection and investigation needs before applying.

Filtering removes events entirely, so it needs the most care: something that seems useless now may matter in a later investigation. Summarising keeps the pattern but loses detail, such as individual flows. Tiering keeps everything but moves older data to cheaper storage. Each choice is recorded with the reason and the checks done.

### 36.5 Query performance

Rules that scan large time ranges or unindexed fields slow everything. Engineers measure rule run times and rewrite the slowest.

A rule that searches thirty days of firewall logs every five minutes repeats enormous work and competes with analysts' searches. Engineers list rules by run time and resource use, then rewrite the worst, for example by narrowing the time range or using indexed fields. The improvement is measured before and after. A run-time report is produced weekly and the slowest five rules are named in it.

### 36.6 Scale tests

Before peak season, the team replays a day of synthetic logs at 3× speed in the test SIEM to check that rules keep up.

Replaying at three times normal speed simulates a heavy peak without waiting for one. The test watches rule delays, queue lengths and dropped events. If rules fall behind, the team adds capacity or optimises queries before the busy season, not during it. Results are compared with the previous year's test. The synthetic day includes a simulated incident burst, so the test reflects the uneven load of a real busy day.

### Cost visibility

Amara publishes the monthly cost per source so owners see what their logs cost. Teams that send verbose debug logs often reduce them once they see the bill, without any SOC request.

### Worked example

At this volume the earlier tiering, 90 days in the SIEM with firewall and DNS moving to the lake after 14 days, no longer fits, so Amara tightens it: her plan keeps portal, Windows and DNS events hot for 30 days and moves firewall events to the lake after 7 days with hourly summaries kept hot. Hot storage falls to about 10 TB. Before applying, she checks that no detection uses raw firewall events older than 7 days.

> **Synthetic case.** Rates and sizes come from the lab script.

### Errors and limits

Bytes per event vary by source; measure each source rather than using one average.

### Exercises

- **EX106 — Sizing result.** Report average EPS, peak EPS, GB/day and 90-day hot TB. *Rubric:* 3 = 6,000; 15,000; 285.1; 25.7; 2 = three; 1 = one; 0 = none.
- **EX107 — Volume reduction.** Name three ways to reduce stored volume. *Rubric:* 3 = filter, summarise, tier; 2 = two; 1 = one; 0 = none.
- **EX108 — Safety check.** What did Amara check before tiering firewall events? *Rubric:* 3 = no detection uses raw firewall events older than 7 days; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Size from measured rates, plan for peaks, and reduce volume only after checking detection and investigation needs.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Security operations and blue team: operations

### Learning outcomes

You will (1) run day-to-day SOC operations: shifts, handovers and queues; (2) apply triage and escalation procedures; (3) manage analyst workload and wellbeing; (4) improve operations from daily feedback.

### 37.1 Shifts and handovers

Lindqvist's SOC runs day and night shifts. Handovers use a template: open cases, alerts awaiting action, system health issues and expected events (such as planned maintenance). Chapter 29's slowest case happened at handover; overlapping shifts by 15 minutes now gives time to talk.

Written handovers stop knowledge from leaving with the outgoing analyst. Expected events, such as maintenance windows, prevent the incoming shift from treating planned outages as attacks. Fifteen minutes of overlap allows a conversation about anything the template does not capture, such as an analyst's unease about an alert that has not yet produced firm evidence.

### 37.2 Triage

Analysts follow a triage sequence: confirm the alert is valid, gather context from enrichment, decide benign, suspicious or malicious, and either close with reason or escalate. Sundaramurthy et al. (2014) observed that much of this knowledge is tacit; written triage notes per rule make it shareable.

Confirming validity first avoids investigating alerts caused by broken parsing or test events. Context from enrichment answers who, what and where quickly. Closing with a reason, rather than simply closing, gives data for tuning and lets reviewers check decisions. Written notes per rule capture what experienced analysts know but rarely write down.

### 37.3 Escalation

Escalation paths name who to call for each alert type, with times. Analysts never hesitate to escalate; false escalations are reviewed without blame.

Hesitation is dangerous: an analyst who waits to be sure may lose the time needed to contain an attack. The review asks what information would have helped decide, which often leads to better enrichment or clearer playbooks. Contact lists are checked weekly. When a named person does not answer within the stated time, the path lists who comes next, so analysts never wait on a single phone.

### 37.4 Workload

Alert fatigue lowers accuracy (Alahmadi et al., 2022). Queue limits, rotation between alert types and protected time for investigation reduce fatigue.

Fatigue builds when analysts handle similar alerts for hours, making mistakes more likely. Queue limits stop a single analyst being buried; rotation varies the work; protected time lets analysts finish deep investigations without constant interruption. Managers track queue sizes per analyst, not just in total. Amara checks whether her rules add to the heaviest queues. When they do, she looks first at enrichment or tuning that could make each alert faster to handle.

### 37.5 Wellbeing

Night work and incidents are stressful. Managers watch for burnout signs and share incident load.

Signs of burnout include withdrawal, irritability, rising errors and frequent sickness. Sharing incident load means the same person is not on every major incident. Managers offer debriefs after distressing cases and make sure night workers get proper rest between shifts. Healthy staff make better decisions. Lindqvist offers confidential counselling to SOC staff, and managers mention it openly so that using it carries no stigma. Rotas are planned at least four weeks ahead.

### 37.6 Daily feedback

Each morning, the team spends ten minutes on yesterday's noisy rules and confusing alerts; engineers take actions.

Ten minutes each morning keeps small problems from growing. Analysts mention the alerts that wasted time or were hard to understand; engineers note actions, such as adding a field or adjusting a threshold. Tracking actions to completion shows analysts that their feedback has effect, which keeps them giving it. Actions appear on a shared board, each marked with an owner and a due date, and finished items are announced at the next meeting.

### 37.7 Engineering in operations

Amara spends one day a week in the queue, so she sees the effect of her rules on analysts first-hand.

Seeing alerts from the analyst's chair reveals problems that are invisible from the engineering side: missing context, confusing titles or rules that fire at the worst moments. Amara rewrites two alert titles after her first day in the queue. The practice also builds trust between engineers and analysts. She logs what she sees each week and brings the most common complaints to the morning feedback meeting.

### Closing well

A closed alert records the reason in a sentence a colleague could check later.

### Worked example

During her queue day, Amara triages an address-change alert where the confirmation email failed. Enrichment shows the login came from a new network but the device fingerprint matched the customer's usual phone. She escalates rather than closes, noting the mixed signals; the customer confirms they changed mobile provider. She suggests adding device continuity to enrichment.

> **Synthetic case.** Shifts and the alert are invented.

### Errors and limits

Procedures cannot cover every alert; analysts' judgement and escalation remain essential.

### Exercises

- **EX109 — Handover template.** What does the handover template cover? *Rubric:* 3 = open cases, pending alerts, system health, expected events; 2 = three; 1 = one; 0 = none.
- **EX110 — Tacit knowledge.** How does the SOC make tacit triage knowledge shareable? *Rubric:* 3 = written triage notes per rule; 2 = partial; 1 = vague; 0 = none.
- **EX111 — Mixed signals.** Why did Amara escalate the address-change alert? *Rubric:* 3 = mixed signals: new network but usual device; escalate rather than close; 2 = partial; 1 = closed it; 0 = none.

### Synthesis

Smooth operations depend on clear handovers, shared triage knowledge, managed workload and engineers who see the queue.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Security operations and blue team: validation

### Learning outcomes

You will (1) validate that detections work against realistic behaviour; (2) plan authorised purple-team validation; (3) measure detection coverage of priority techniques; (4) feed validation results into improvement.

### 38.1 Validation questions

Validation asks whether the SOC detects what matters in real conditions. Verification (chapter 30) proved rules match their specifications; validation tests whether the specifications and the whole system catch realistic behaviour.

A rule can match its specification perfectly while the specification itself is wrong, for example by assuming attackers always fail many times before succeeding. Validation tests the assumptions by using realistic behaviour, which may differ from what engineers imagined. It also checks the whole system, including analysts and playbooks, rather than rules alone.

### 38.2 Purple-team validation

In a purple-team exercise, an authorised team performs agreed, safe simulations of techniques while defenders watch. Scope, timing and stop conditions are approved by the CISO. The SOC sees which simulations produced alerts, which produced only logs and which left nothing.

Watching together is what makes it purple rather than red: the goal is learning, not catching the defenders out. Stop conditions protect operations, such as halting if a simulation affects a live service. Recording which simulations left no trace at all identifies data gaps, often the most valuable finding of the exercise.

### 38.3 Technique selection

Lindqvist chooses twelve priority ATT&CK techniques from its threat analysis, including valid account use, new services and remote logons into depot networks.

Twelve is enough to cover the most important risks without overwhelming the team in one exercise. Choosing from the threat analysis keeps the selection relevant to Lindqvist rather than generic. Including depot techniques tests the newly built monitoring, which has not yet seen realistic activity. The list is agreed with the CISO, and each technique is linked to the threat analysis entry that justified it, so the selection can be revisited when the analysis changes.

### 38.4 Outcomes

For each simulation the result is: alerted, logged but no alert, or not logged. Each category leads to a different fix: tuning, new detection or new data source.

Alerted means the full chain worked. Logged but no alert means the data exist but no rule uses them, so the fix is a new or tuned detection. Not logged means the SOC was blind, so the fix starts with collecting a new source. Counting outcomes across techniques gives a clear coverage picture.

### 38.5 Real incidents

Validation also uses real incidents: did the SOC detect them, or did customers report them first? The portal takeover was detected internally — a validation point for R-07.

Real incidents test the system against actual attackers rather than simulations. A customer reporting an incident first is a sign that detection failed somewhere. The portal takeover being caught internally supports R-07, though a single case is limited evidence, and the SOC keeps counting over time. Amara logs each incident's detection source in the case system so the share found internally can be counted.

### 38.6 Avoiding gaming

Defenders do not get the simulation script in advance; otherwise detections are tuned to the test rather than the behaviour.

If defenders know exactly which simulations will run and when, they can tune rules to catch those specific events, which inflates results without improving real detection. Keeping the details secret, while sharing the general scope, ensures the exercise tests how the SOC would perform against unannounced activity. The authorised team keeps its detailed plan with the CISO's office, and defenders learn the specifics only during the debrief after the exercise ends.

### 38.7 Repeat

Validation repeats quarterly; results feed the coverage metric from chapter 29.

Quarterly repetition shows whether fixes worked and whether coverage drifts as systems change. Techniques that alerted last time are tested again, because a parser change or rule edit could have broken them. The trend over several quarters gives managers a clear view of progress. Results are compared quarter by quarter in a single table, with each technique's outcome over time. A technique that moves from alerted to logged-only is treated as a regression and investigated like a defect, with an owner and a deadline.

### Safety of exercises

Simulations avoid depot systems during dispatch peaks and stop immediately if any business service slows.

### Worked example

Of twelve simulated techniques, seven alerted, three were logged but did not alert, and two left no trace — both in depot networks where only denied connections are logged. The team adds an alert for a logged-only technique and raises a project to log allowed connections from depots to domain controllers.

> **Synthetic case.** The exercise and results are invented.

### Errors and limits

Simulations are approximations of real attackers and run under known conditions.

### Exercises

- **EX112 — Three outcomes.** Name the three simulation outcome categories and their fixes. *Rubric:* 3 = alerted, logged-no-alert (new rule), not logged (new data source); 2 = two; 1 = one; 0 = none.
- **EX113 — Exercise results.** Summarise the validation results. *Rubric:* 3 = 7 alerted, 3 logged only, 2 no trace in depots; 2 = partial; 1 = wrong; 0 = none.
- **EX114 — No script.** Why are defenders not given the simulation script? *Rubric:* 3 = prevents tuning to the test instead of behaviour; 2 = partial; 1 = secrecy; 0 = none.

### Synthesis

Validation tests the whole system against realistic behaviour; its results turn directly into tuning, detections and data sources.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Security operations and blue team: maintainability

### Learning outcomes

You will (1) design detections and pipelines that remain maintainable; (2) manage rule lifecycle and retirement; (3) document for future engineers; (4) reduce operational toil.

### 39.1 Maintenance costs

Every rule, parser and integration costs time to maintain. A SOC with 400 rules nobody understands is weaker than one with 150 well-kept rules.

Each rule needs someone to check that its data source still exists, that its fields have not been renamed and that its threshold still suits current traffic. Multiply that by hundreds and a small team cannot keep up, so rules decay quietly. Fewer, better-understood rules mean each gets attention, analysts trust what fires, and gaps are easier to see when the set is reviewed against the threat analysis.

### 39.2 Rule lifecycle

Rules move through proposed, testing, monitor-only, active, under review and retired. Each state has entry criteria. Rules that never fire or never lead to action are reviewed for retirement.

Entry criteria stop rules from skipping steps: a rule cannot become active without a passing test and a week in monitor-only mode with acceptable results. 'Under review' is a holding state for rules whose data source changed or whose precision fell. A rule that has not fired in a year may be protecting against something rare, so retirement needs a reason, not just silence, and is approved by Paolo.

### 39.3 Readable rules

Clear names, comments explaining intent, and references to the requirement and ATT&CK technique let others maintain rules when the author leaves.

A rule named 'portal_burst_v3_final' tells a maintainer little; 'portal possible takeover: failures then success from one network' tells them what it is for. Comments explain choices, such as why the window is ten minutes. References link the rule to R-07 and the relevant technique, so a reviewer can judge whether a proposed change still serves the original need.

### 39.4 Shared components

Common logic, such as "is this address in a depot subnet?", lives in one shared lookup rather than copied into twenty rules, so a change happens in one place.

If twenty rules each contain their own list of depot subnets, adding a new depot means editing twenty files, and one will be missed. A shared lookup fed from the asset inventory updates every rule at once. Shared components need tests and an owner of their own, since a mistake there affects every rule that uses them.

### 39.5 Toil

Toil is repetitive manual work that scales with load: restarting a stuck collector by hand, copying alert fields into tickets. Engineers automate toil to free analysts.

Toil grows with the business: more depots mean more collectors to restart, more alerts mean more fields to copy. It also wears people down and invites mistakes. Amara measures how many minutes a week analysts spend copying alert fields into tickets and finds it is over three hours. Automating the copy is a small engineering task with a clear return.

### 39.6 Documentation

Runbooks, architecture records and rule notes are kept beside the code and reviewed with changes.

Documentation kept elsewhere drifts away from what the code actually does. Keeping it beside the code means a reviewer sees both together and can ask why a runbook was not updated when the rule changed. Review checklists include a documentation line, so changes without updated notes are sent back. Runbooks are tested by someone other than their author at least once a year: they follow the steps on a test system and note anything unclear or out of date.

### 39.7 Knowledge transfer

Before Amara's placement ends, she runs a handover session and pairs Paolo's next junior with her on two rules.

A handover session explains how the depot logging works, where its weak points are and which decisions are still open. Pairing on real rules teaches more than reading notes, because the junior asks questions as problems arise. Amara records the session and updates the runbooks with every question the junior asked that the documentation did not answer. Paolo attends the session and signs off the handover list.

### Dependency tracking

Each rule lists the data sources and lookups it depends on. When a system is decommissioned, a query over these lists shows which rules are affected, so retirement happens deliberately rather than leaving rules that silently never fire.

### Worked example

Amara's quarterly rule review finds 31 rules that have not fired in a year. Twelve cover techniques still relevant and are verified with test events — they stay. Fifteen depend on a decommissioned system and are retired. Four duplicate newer rules and are merged. The review notes why each decision was made.

> **Synthetic case.** Counts are invented.

### Errors and limits

A rule that never fires may still be valuable if the behaviour is rare and serious; test before retiring.

### Exercises

- **EX115 — Lifecycle states.** List the rule lifecycle states. *Rubric:* 3 = proposed, testing, monitor-only, active, under review, retired; 2 = four; 1 = two; 0 = none.
- **EX116 — Quarterly review.** What happened to the 31 silent rules? *Rubric:* 3 = 12 kept after tests, 15 retired, 4 merged; 2 = two; 1 = one; 0 = none.
- **EX117 — Toil.** Define toil and give an example. *Rubric:* 3 = repetitive manual work that scales with load; e.g. restarting collectors; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Maintainable SOCs keep fewer, clearer rules with defined lifecycles, shared components and little toil.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify an end-to-end requirement under varied conditions; (2) analyse which stage causes failures; (3) report pass or fail with evidence; (4) propose fixes and re-verify.

### 40.1 Purpose

Laboratory II verifies requirement R-07 — possible-takeover alert acknowledged within 15 minutes — not just in quiet conditions but during busy periods, at night and at shift handover.

Quiet-condition tests from the first laboratory showed the rule works; they did not show the whole response chain meets its time target when conditions are difficult. Busy periods slow pipelines and distract analysts; nights have fewer staff; handovers split attention. Testing the requirement under those conditions shows whether it holds when it matters most. Each condition gets its own run.

### 40.2 Method

Five timed synthetic injections run in production under a test customer account, with analysts aware a test may happen but not when. Times are captured at ingestion, detection and acknowledgement.

Running in production is necessary because the laboratory cannot reproduce real load or real analyst behaviour. A reserved test account keeps the injections away from real customers. Telling analysts a test may happen, without saying when, respects them while keeping their behaviour natural. Timestamps at each stage let the team see where any delay occurred.

### Lab — timing five runs

```python
"""End-to-end verification of requirement R-07 from five timed synthetic injections (seconds after injection)."""
runs = {  # run: (siem_received, rule_fired, analyst_ack)
    "R1 quiet":    (95, 310, 690),
    "R2 quiet":    (102, 298, 610),
    "R3 busy":     (240, 520, 1180),
    "R4 night":    (98, 305, 820),
    "R5 handover": (110, 330, 1010),
}
limit = 15 * 60
for name, (s, f, a) in runs.items():
    print(f"{name:12} ingest={s:4}s detect={f-s:4}s ack={a-f:4}s total={a/60:5.1f} min {'PASS' if a <= limit else 'FAIL'}")
```

Run with `python3 lab_e2e.py`. Verified output:

```text
R1 quiet     ingest=  95s detect= 215s ack= 380s total= 11.5 min PASS
R2 quiet     ingest= 102s detect= 196s ack= 312s total= 10.2 min PASS
R3 busy      ingest= 240s detect= 280s ack= 660s total= 19.7 min FAIL
R4 night     ingest=  98s detect= 207s ack= 515s total= 13.7 min PASS
R5 handover  ingest= 110s detect= 220s ack= 680s total= 16.8 min FAIL
```

### 40.3 Reading the result

Three runs pass (11.5, 10.2 and 13.7 minutes). The busy-period run fails at 19.7 minutes: ingestion slowed to 240 seconds and acknowledgement took 660 seconds. The handover run fails at 16.8 minutes, almost entirely from slow acknowledgement.

The total for the busy run, 19.7 minutes, breaks down into four minutes of ingestion, about five minutes of detection and eleven of acknowledgement. Both slow stages exceeded their budgets. The handover failure is a single-stage problem: the pipeline was fine, but nobody picked up the alert quickly while shifts changed over.

### 40.4 Stage analysis

Detection time stays near 200–280 seconds in all runs. The failures come from ingestion under load and from analyst acknowledgement under load or handover.

Stable detection times mean the rule itself is not the problem; effort spent making it faster would not fix the failures. Ingestion slows under load because portal logs compete with everything else in the queue. Acknowledgement slows when analysts are busy or changing shifts. Separating stages makes the right fixes obvious. Amara plots each run as a stacked bar, one segment per stage, which makes the pattern visible at a glance.

### 40.5 Fixes

Ingestion: raise the priority of portal logs in the pipeline queue. Acknowledgement: page the possible-takeover alert to a dedicated device rather than the shared queue, and keep the 15-minute handover overlap.

Raising priority for portal logs means they move ahead of bulk logs when the pipeline is busy. A dedicated paging device for takeover alerts makes them stand out from the general queue, so they are not lost among routine work. Keeping the handover overlap gives the incoming analyst time to pick up urgent alerts.

### 40.6 Re-verification

After fixes, two further busy and handover runs pass at 12.9 and 13.4 minutes.

Re-running the conditions that failed is essential; passing quiet-condition tests again would prove nothing new. Both new results fall comfortably under fifteen minutes. Two runs are still a small sample, so the timed injections continue monthly, and the results feed the requirement's verification record. If a later monthly run fails, the same stage analysis is repeated before any fix is chosen. A new failure in a stage that passed before suggests something changed, such as higher volume or a new shift pattern, and that change is investigated first.

### Test hygiene in production

The test customer account is flagged so its alerts are excluded from metrics and customer service never calls a real person. After each run, Amara confirms the test hold has been released and records the clean-up in the laboratory log. Analysts are thanked, not judged, for slow acknowledgements; the point is to find system causes.

### Worked example

Amara's laboratory report states: "R-07 initially failed in 2 of 5 conditions (busy, handover). Causes: ingestion lag and acknowledgement delay. After prioritised ingestion and dedicated paging, re-runs passed. Requirement status: verified under tested conditions; retest each quarter."

> **Synthetic case.** Times come from the lab script; the re-runs are recorded results.

### Errors and limits

Five runs give limited coverage; extreme peaks remain untested.

### Exercises

- **EX118 — Pass and fail.** Which runs passed and which failed? *Rubric:* 3 = R1, R2, R4 pass; R3 busy 19.7 and R5 handover 16.8 fail; 2 = partial; 1 = wrong; 0 = none.
- **EX119 — Failure stages.** Which stages caused the failures? *Rubric:* 3 = ingestion under load; acknowledgement under load and at handover; 2 = partial; 1 = detection; 0 = none.
- **EX120 — Fixes applied.** What fixes were made, and what did re-verification show? *Rubric:* 3 = prioritised portal ingestion, dedicated paging; re-runs passed 12.9 and 13.4; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Verify end-to-end requirements under realistic conditions, find the failing stage, fix it and verify again.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Security operations and blue team: system optimization

### Learning outcomes

You will (1) optimise SOC performance across detection quality, speed and cost; (2) use data to choose optimisation targets; (3) avoid local optimisations that harm the whole; (4) evaluate optimisations after deployment.

### 41.1 What to optimise

The SOC balances detection quality, time to respond, analyst load and cost. Improving one can harm another: cheaper storage slows investigations; more rules raise load.

Optimising one measure in isolation can make the SOC worse overall. A team that only cut cost might move all logs to slow storage and lose hours in each investigation. Naming the four measures together keeps trade-offs visible, and proposals must state their expected effect on each. Amara writes the four measures at the top of every optimisation proposal, with current values, so readers can see what is at stake.

### 41.2 Finding bottlenecks

Laboratory II showed acknowledgement, not detection, limited response time. Optimising rule speed further would have changed nothing. Optimisation starts at the bottleneck.

In any chain, the slowest stage limits the whole. The rule took about four minutes; acknowledgement took up to eleven. Halving rule time would save two minutes at best, while fixing acknowledgement saved far more. Measuring each stage before optimising avoids spending effort where it cannot help. Amara compares the stage times side by side in one table before suggesting any change, and she circles the slowest stage in each run.

### 41.3 Data-driven targets

Amara ranks candidate improvements by expected effect on the 90th-percentile response time and analyst minutes per day, using measured data from earlier chapters.

Ranking by expected effect uses numbers already gathered: stage times from the laboratory, alert volumes from the night-load study and handling times from triage records. Each candidate gets an estimate with its assumptions. The ranking guides where to start, and actual results later show how good the estimates were. Paolo reviews the assumptions before work starts on any of them.

### 41.4 Local versus global

Moving rules to a morning queue optimised night load but could slow response to those alerts. The team tracks the moved rules' outcomes to make sure the global effect is positive.

A change can look good in its own area while causing harm elsewhere. Moving rules to the morning lightened the night, but if one of those rules ever caught a real attack at night, the delay could matter. Tracking outcomes of the moved rules checks that the overall result is still positive.

### 41.5 Automation priorities

Automated enrichment saved two minutes per alert; automating customer phone lookup saves another minute for takeover alerts. Small savings on frequent tasks add up.

A minute saved on an alert that occurs twice a month barely matters; a minute saved on one that occurs fifty times a day adds up to hours each week. Phone lookup for takeover alerts is frequent and repetitive, so automating it is worth the effort. Amara lists candidates by frequency times time saved. Phone lookup goes first.

### 41.6 Post-deployment review

Each optimisation is reviewed after a month: did the metric move, and did anything else get worse?

A month gives enough data to see whether the targeted metric moved. Checking other metrics catches side effects, such as faster acknowledgement but more errors in closure reasons. If the change did not help, it is rolled back or adjusted rather than kept because it was planned. The review is a short written note with the before-and-after figures, signed off by Paolo. Notes for changes that were rolled back are kept too, since they record what did not work and stop the same idea being retried without new evidence.

### 41.7 Diminishing returns

After the main bottlenecks are fixed, further gains cost more; at some point, effort is better spent on validation gaps.

The first fixes remove large, obvious delays; later ones chase seconds at rising cost. Once response time is well within target, effort may do more good closing a technique that currently leaves no trace. Choosing when to stop optimising is itself an engineering decision, made with data. Amara proposes a simple rule: once the 90th percentile sits well inside target for three months, optimisation pauses and validation gaps take priority.

### Cost optimisation

Cost is optimised last and separately: licence tiers, storage classes and retention are reviewed yearly. Savings are reinvested only after checking they do not reduce detection or investigation capability, which Amara documents in the review.

### Worked example

Amara's optimisation review: night alert minutes down 41% (target 40%); p90 acknowledgement for takeover alerts 12.8 minutes (target 15); no missed priority incidents; morning queue averaging 22 minutes of work. She recommends shifting effort to the depot logging gap from validation.

> **Synthetic case.** Figures are invented.

### Errors and limits

One month of data may include unusual weeks; continue tracking.

### Exercises

- **EX121 — Bottleneck first.** Why start optimisation at the bottleneck? *Rubric:* 3 = improving non-bottleneck stages does not change overall result; 2 = partial; 1 = vague; 0 = none.
- **EX122 — Local effect check.** How did the team ensure the morning-queue change helped overall? *Rubric:* 3 = tracked moved rules' outcomes for slower response harm; 2 = partial; 1 = assumed; 0 = none.
- **EX123 — Next effort.** Why did Amara recommend moving to the depot logging gap? *Rubric:* 3 = targets met; diminishing returns; validation gap more valuable; 2 = partial; 1 = random; 0 = none.

### Synthesis

Optimise the whole system starting at its bottleneck, check for side effects, and know when to switch effort elsewhere.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Security operations and blue team: applied research

### Learning outcomes

You will (1) frame an engineering research question from SOC data; (2) review relevant studies; (3) run a small, ethical study inside the organisation; (4) report results with limits.

### 42.1 Research in practice

Engineers often need evidence their organisation lacks. Applied research answers a local question with a careful method, borrowing ideas from published studies.

Published studies rarely match a particular SOC's data, tools and customers. Applied research asks a narrow question that matters locally, uses data the organisation already holds and states its limits honestly. Borrowing methods from published work, such as how to label alerts or measure outcomes, gives the local study a stronger foundation. Results are written up so others can check them.

### 42.2 The question

Amara asks: "Does adding device continuity (same device as usual) to takeover alerts reduce false escalations without missing real takeovers?" It comes from her queue day in chapter 37.

During her queue days, Amara noticed that many takeover alerts turned out to be customers logging in from their usual phone after mistyping passwords. Device continuity, whether the device matches the customer's history, might separate these from real takeovers. Framing the question with both benefits and risks keeps the study balanced. She writes the question down first.

### 42.3 Literature

Alahmadi et al. (2022) argue alarms should be contextual; Hassan et al. (2019) show context from provenance can rank alerts. Sommer and Paxson (2010) caution that patterns learned in one environment may not transfer.

The literature supports the idea that context helps analysts judge alerts, which justifies testing device continuity. The caution about transfer matters too: results found at Lindqvist may not hold at another company, and patterns may shift over time even at Lindqvist. Amara uses these sources to frame her method and limits.

### 42.4 Method

Amara labels three months of takeover alerts (82 in total) as real or benign using case outcomes, then checks how device continuity would have changed the decision. She pre-states her measure: escalations avoided and real takeovers that would have been de-prioritised.

Stating the measure before looking at the data prevents choosing whichever result looks best afterwards. Case outcomes give labels grounded in investigation rather than guesses. Asking how device continuity would have changed each decision is a retrospective test, which avoids putting customers at risk while the idea is evaluated.

### 42.5 Ethics

The study uses existing case records; customer identifiers are removed before analysis, and the privacy officer approves the use.

Even though the records already exist, using them for research is a new purpose that needs approval. Removing identifiers before analysis means Amara does not see which customer each alert concerned. The privacy officer checks that the purpose is legitimate and that results will be reported only in aggregate. The approval and its conditions are filed with the study, and the de-identified data set is deleted once the results have been reviewed.

### 42.6 Results

Device continuity would have de-prioritised 29 of 70 benign alerts and 1 of 12 real takeovers. The missed case involved a customer whose phone had been stolen.

De-prioritising 29 of 70 benign alerts would save real analyst time. Missing one of twelve real takeovers is a serious cost, because that customer suffered harm. The stolen-phone case shows the weakness: an attacker using the victim's own device looks continuous by design. The result shows why a single signal should not decide alone. Amara reports both counts together so neither the saving nor the miss is hidden.

### 42.7 Decision

The team adds device continuity as information on the alert, not as an automatic de-prioritiser, and logs analyst decisions for review.

Showing device continuity as information lets analysts use it while still judging each case, so the stolen-phone pattern would not be automatically dismissed. Logging their decisions creates new data to check later whether analysts use the field well. The team can revisit automation if more evidence accumulates. A review after three months will check whether analysts use the field well and whether any real takeover was wrongly set aside.

### Sharing results

Amara presents the findings at the SOC's monthly review and stores the analysis script with the case data references.

### Worked example

Amara's report concludes: "Device continuity is a useful signal but not a safe filter: in one of 12 real cases the attacker used the customer's own stolen device. We display it as context and will re-measure after three months."

> **Synthetic case.** Figures are invented.

### Errors and limits

Eighty-two alerts from one company give rough estimates; results may not transfer elsewhere.

### Exercises

- **EX124 — Research question.** State Amara's research question. *Rubric:* 3 = device continuity on takeover alerts reduces false escalations without missing real takeovers; 2 = partial; 1 = vague; 0 = none.
- **EX125 — Study results.** Report the effect on benign and real alerts. *Rubric:* 3 = 29 of 70 benign de-prioritised; 1 of 12 real (stolen phone); 2 = partial; 1 = one number; 0 = none.
- **EX126 — Display not filter.** Why show continuity as context rather than filter on it? *Rubric:* 3 = it would have hidden a real takeover; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Applied research brings published ideas and careful local measurement together to make safer engineering decisions.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work in a professional SOC setting under supervision; (2) apply professional conduct and confidentiality; (3) contribute to real operational improvements; (4) reflect on practice.

### 43.1 The placement

Amara's final-year practice period is a full-time term in Lindqvist's SOC, supervised by Paolo with learning goals agreed with her university tutor.

A full-time term lets Amara work on projects long enough to see them through, rather than observing from the side. Learning goals agreed with her tutor ensure the placement serves her education as well as Lindqvist's needs. Paolo's supervision gives her someone accountable for her work and her development. Halfway through, the tutor visits to check progress against the goals and to hear from Paolo how the placement is going.

### 43.2 Conduct

She signs confidentiality terms, follows access rules and never takes data off company systems. Coursework uses only synthetic or approved anonymised material.

Real customer and company data are confidential, and a student moving between university and workplace is a possible leak point. Keeping data on company systems removes that risk. Using only synthetic or approved anonymised material for coursework lets her write about her work without exposing anything sensitive. Breaking these rules would end the placement and could carry legal consequences, which the induction explains plainly.

### 43.3 Contributions

Her goals: deliver the depot logging project, maintain three rules, spend one day per week in the queue and write two runbooks.

The goals mix project delivery, ongoing maintenance, operational exposure and documentation, so she sees several sides of SOC engineering. Each is concrete enough to check at the end: the project delivered or not, the rules maintained or not. Paolo and the tutor agree them at the start. Progress against each goal is noted at every weekly meeting, so slippage shows up early and can be discussed while there is still time to adjust.

### 43.4 Supervision

Weekly meetings review progress, problems and learning. Paolo signs off production changes.

Weekly meetings catch problems early, before they derail a project. Discussing learning, not just tasks, keeps the placement educational. Requiring Paolo's sign-off on production changes protects Lindqvist and Amara alike: a mistake by a student is caught before it affects customers. Meeting notes are kept, and actions from one week are checked at the start of the next. Amara brings an agenda; Paolo adds topics he wants to raise, such as feedback from analysts on her rules. The notes later support her placement report.

### 43.5 Professional relationships

Working with IT operations, customer service and depot managers teaches negotiation: depot managers care about dispatch, not detections, so she frames requests in their terms.

Framing requests in terms others care about makes cooperation easier. Asking a depot manager to accept a logging change for better detections may get a shrug; explaining that it helps keep dispatch running safely gets attention. Amara learns to listen first to what each group needs. She also learns to put agreements in writing after meetings, so everyone remembers the same commitments.

### 43.6 Reflection

A weekly journal records what happened, what she learned and what she would change. The tutor reviews it.

Writing weekly turns experience into learning. Recording what she would change makes her think about alternatives while the details are fresh. The tutor's comments point out patterns she might miss, such as underestimating how long reviews take. Entries are short, often half a page. Over the term the journal shows how her judgement changed, which becomes evidence in her placement report. She also notes moments when she was unsure what to do and how she decided.

### 43.7 Public-service angle

Lindqvist shares anonymised indicators of credential stuffing with a sector information-sharing group, a practice Knerler, Parker and Zimmerman (2022) encourage. Amara prepares one submission under supervision.

Sharing indicators helps other firms block the same credential-stuffing sources and spot similar patterns. Anonymising protects Lindqvist's customers. Preparing a submission under supervision teaches what can and cannot be shared, and how to describe indicators so others can use them. The submission is checked by Paolo and the privacy officer before sending. She learns that indicators age quickly, so each one carries a first-seen and last-seen date.

### Learning agreement

The learning agreement between Lindqvist, the university and Amara states goals, supervision, working hours, confidentiality and how the placement is assessed. If the host asks for work outside the agreement, such as covering night shifts alone, Amara can refer to it and her tutor can intervene. The agreement protects both the student and the company.

### Worked example

A journal entry: "Depot manager refused a change during peak week. I had planned around our schedule, not theirs. Rescheduled for the following Tuesday morning; next time I will check the depot calendar first." Paolo notes this as evidence of professional growth.

> **Synthetic case.** The placement is invented.

### Errors and limits

Placement experience depends on the host; tutors check that learning goals are met.

### Exercises

- **EX127 — Placement goals.** List Amara's four placement goals. *Rubric:* 3 = depot logging project, three rules, queue day, two runbooks; 2 = three; 1 = one; 0 = none.
- **EX128 — Framing requests.** How did working with depot managers change her approach? *Rubric:* 3 = frame requests in their terms; check their calendar; 2 = partial; 1 = vague; 0 = none.
- **EX129 — Sharing indicators.** What did Lindqvist share, and with whom? *Rubric:* 3 = anonymised stuffing indicators with sector sharing group; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Supervised practice builds professional conduct, relationships and reflection alongside technical contribution.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define a capstone project with scope, requirements and plan; (2) justify the project from evidence; (3) plan verification and validation; (4) manage risks and stakeholders.

### 44.1 Choosing the project

Amara's capstone closes the depot gap found in validation: "Detect remote logons from depot networks to domain controllers within 15 minutes, with no more than 5 false alerts per week."

Choosing a gap found by validation means the capstone addresses a real, evidenced weakness rather than a topic picked for interest alone. The requirement states the behaviour, the time limit and the acceptable noise, so success can be measured objectively at the end. Her tutor and Paolo approve the choice before work begins.

### 44.2 Evidence for the need

Two simulated techniques left no trace in depot networks (chapter 38); the threat analysis ranks depot-to-domain-controller movement high (chapter 23).

Two sources point to the same gap: simulations showed the SOC was blind there, and the threat analysis ranked the risk highly. Together they justify the effort. A capstone resting on a single weak signal would be harder to defend to the panel. Amara cites both in the capstone proposal, quoting the exact simulation outcomes and the risk ranking, so assessors can trace the motivation to evidence rather than to her own preference.

### 44.3 Scope

In: allowed-connection logging at the depot boundary for domain-controller ports; enrichment; one detection; playbook. Out: agents on depot devices; changes to depot applications.

Stating what is out matters as much as what is in. Agents on depot devices are excluded because the old software cannot host them; application changes are excluded because they belong to other teams. A tight scope makes twelve weeks realistic and keeps the project focused on the logging and detection that close the gap. Any request to widen the scope goes through the change log.

### 44.4 Requirements

Functional: log allowed depot-to-DC connections; alert on interactive logons from depot devices not on the approved list. Non-functional: 15-minute latency; completeness 99.9%; ≤5 false alerts per week.

Each requirement can be tested: logs either arrive or not, alerts either fire for unapproved devices or not, times and rates can be measured. The approved list is the key design element, since it decides which logons count as suspicious, and it needs an owner to keep it current. Each requirement has an identifier and appears in a traceability table, linked to its source and its planned test.

### 44.5 Plan

Weeks 1–3 design and review; 4–6 build in test; 7–8 pilot at three depots; 9–10 rollout; 11–12 verification, validation and report.

Three weeks of design and review give time to catch problems before building. Building in the test environment avoids disrupting depots. A three-depot pilot tests real conditions on a small scale. Two weeks of rollout and two of evaluation complete the cycle, with the report at the end. Fortnightly reviews with Paolo check progress against these dates. If the pilot slips by more than a week, rollout is shortened rather than evaluation, because evaluation produces the evidence the capstone depends on.

### 44.6 Verification and validation plan

Unit tests for logic, pipeline tests, timed synthetic logons, and a purple-team re-test of the two missed techniques.

Unit and pipeline tests verify the build; timed synthetic logons verify the latency requirement. Re-testing the two missed techniques with the purple team validates that the gap is actually closed, which is the point of the project. Each test has expected results written before it runs, so outcomes are judged against criteria rather than impressions. The purple-team re-test uses the same technique descriptions as the original validation, making the before-and-after comparison fair.

### 44.7 Risks

Log volume could exceed estimates; depot changes could disrupt dispatch. Mitigations: volume estimate from a one-day capture; pilots and change windows.

A one-day capture gives a real measurement of log volume before committing to the design, rather than relying on guesses. Pilots and change windows reduce the chance of disrupting dispatch. Each risk has an owner and a trigger for action if it begins to materialise. The risk list is reviewed at each fortnightly meeting with Paolo. New risks are added as they appear.

### Stakeholder map

Amara maps stakeholders for the capstone: depot managers (dispatch continuity), IT operations (firewall load), the SOC (alert quality) and the privacy officer (connection metadata). Each gets a named contact and a planned update at the end of each phase, so nobody is surprised when changes reach their area.

### Worked example

The capstone proposal is reviewed by Paolo, her tutor and the IT operations lead. The operations lead adds a requirement: logging changes must not add more than 2% CPU on boundary firewalls. Amara adds it with a measurement method.

> **Synthetic case.** The project is invented.

### Errors and limits

Capstone scope must fit the time available; resist adding features.

### Exercises

- **EX130 — Capstone requirement.** State the capstone's headline requirement. *Rubric:* 3 = detect depot-to-DC remote logons within 15 min, ≤5 false/week; 2 = partial; 1 = vague; 0 = none.
- **EX131 — Scope boundaries.** What is out of scope, and why does that matter? *Rubric:* 3 = agents on depot devices, app changes; keeps project feasible; 2 = partial; 1 = vague; 0 = none.
- **EX132 — Added requirement.** What did the operations lead add? *Rubric:* 3 = ≤2% firewall CPU, with measurement; 2 = partial; 1 = vague; 0 = none.

### Synthesis

A capstone is justified by evidence, bounded in scope, planned with verification and shaped by stakeholders.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) respond to review findings; (3) classify findings by severity; (4) record decisions and changes.

### 45.1 Why independent review

Designers miss their own assumptions. An engineer from another team, unconnected to the project, reviews Amara's capstone design.

Amara has lived with the design for weeks, so certain choices feel obvious to her even when they rest on untested beliefs, such as assuming depots use only one logon protocol. A reviewer from another team brings different habits and no stake in the design looking good. Choosing someone unconnected also means the review cannot be dismissed later as a friendly sign-off, which matters when the capstone is assessed.

### 45.2 Review package

Diagram, data flows, requirements, rule logic, test plan, risk register and rollout plan, sent a week ahead.

Sending everything a week ahead gives the reviewer time to read carefully rather than reacting during a meeting. Each document answers a different question: the diagram shows structure, data flows show volumes and formats, the rule logic shows what will fire, and the risk register shows what Amara already worries about. A missing document would itself be a finding, since the reviewer cannot check what is absent.

### 45.3 Findings

The reviewer raises: (1) the approved-device list is maintained by hand and will drift; (2) the rule ignores logons over a protocol the depots also use; (3) the playbook lacks a step to check for the same account on other depots; (4) the volume estimate came from a quiet day.

Each finding targets a different weakness. A hand-maintained list will slowly diverge from reality as devices change. Ignoring a second protocol leaves a path attackers could use. Without checking other depots, an analyst might contain one site while the same account is active elsewhere. A quiet-day estimate understates the load the design must handle. None of these was in Amara's own risk register, which shows why the review was worth doing.

### 45.4 Severity

Findings are classed as blocking, major or minor. Finding 2 is blocking: a coverage gap. Findings 1 and 4 are major; finding 3 is minor.

Blocking means the design cannot proceed until the finding is fixed, because building it would knowingly leave the gap the project exists to close. Major findings must be fixed before go-live but need not stop the build. Minor findings can be scheduled. Classing severity openly lets Amara put effort where it matters and lets assessors see that the most serious issue was handled first.

### 45.5 Responses

Amara extends the rule to the second protocol; links the approved list to the asset inventory with a weekly reconciliation; re-estimates volume from a busy-day capture; adds the playbook step.

Each response addresses the finding's cause rather than its symptom. Linking the list to the inventory makes drift visible every week, instead of relying on someone remembering to update it. A busy-day capture tests the design against realistic load. Extending the rule closes the gap without changing its basic structure, so earlier tests remain relevant with additions for the new protocol.

### 45.6 Record

A review log lists each finding, severity, response and status. The reviewer confirms closure of the blocking finding before build.

The log makes the review traceable: anyone can see what was found, how seriously it was taken and what was done. Requiring the reviewer to confirm closure of the blocking finding prevents the designer from simply declaring it fixed. The log goes into the evidence dossier, where assessors can check that every finding was answered. Major findings are rechecked before go-live.

### 45.7 Culture

Reviews are about the design, not the designer; Amara thanks the reviewer and asks to review someone else's design next term.

If reviews felt like personal criticism, designers would hide weaknesses and argue with findings rather than fixing them. Treating the design as the subject lets both sides be candid. Offering to review someone else's work next term completes the exchange and shows Amara values the practice rather than merely enduring it. The reviewer, in turn, notes two design ideas worth borrowing for their own team's work, which shows that reviews teach in both directions.

### Preparing as a designer

Before the review Amara lists the assumptions she is least sure of and sends them with the package, inviting the reviewer to test them first.

### After the review

The review log is kept with the capstone report so assessors can see how the design changed and why.

### Worked example

The busy-day re-estimate shows 3.2 times the earlier volume, still within the lake's capacity but above the firewall CPU limit on two large depots. Amara changes those depots to log only connection starts, which keeps CPU under 2%.

> **Synthetic case.** The review is invented.

### Errors and limits

One reviewer cannot catch everything; reviews reduce but do not remove design risk.

### Exercises

- **EX133 — Blocking finding.** Which finding was blocking, and why? *Rubric:* 3 = ignored second protocol: coverage gap; 2 = partial; 1 = wrong; 0 = none.
- **EX134 — Drift fix.** How was approved-list drift addressed? *Rubric:* 3 = linked to asset inventory with weekly reconciliation; 2 = partial; 1 = vague; 0 = none.
- **EX135 — Busy-day estimate.** What did the busy-day re-estimate change? *Rubric:* 3 = 3.2× volume; two depots log connection starts only to keep CPU < 2%; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Independent review finds assumptions designers cannot see; classify, respond and record each finding.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) build and roll out the capstone system; (2) verify it against requirements; (3) validate it with an authorised re-test; (4) document results and remaining gaps.

### 46.1 Build

The build follows the reviewed design: firewall logging changes, parser, enrichment link to the asset inventory, rule covering two protocols, and the playbook.

Following the reviewed design closely matters because the review's findings were resolved against that version. Any deviation during build goes back to the reviewer for a quick check. Each component is built and tested in the test environment first, in dependency order: logging before parsing, parsing before enrichment, enrichment before the rule, and the playbook last once alerts can be produced.

### 46.2 Pilot

Three depots pilot for two weeks. One false alert per week arises from a depot IT technician using a non-approved laptop; the technician's device is registered properly.

The false alert is a useful one: a technician using an unregistered laptop on the depot network is exactly the kind of device the approved list should know about. Registering it properly fixes the alert and improves the inventory. One false alert per week is well inside the target of five, which supports moving on to full rollout.

### 46.3 Rollout

Remaining depots follow in groups, with CPU monitored on each firewall; all stay below 2%.

Watching firewall CPU guards against the risk that extra logging slows depot networks and disrupts dispatch. Below 2% shows the change adds little load. Rolling out in groups means any problem affects only a few depots before it is caught, and the pilot's lessons are applied to each new group. Each group's figures are posted on the rollout dashboard, and depot managers receive a short note confirming their site has changed and whom to call if something looks wrong.

### 46.4 Verification

Unit and pipeline tests pass. Timed synthetic logons measure 9.8 to 13.1 minutes end to end. Completeness reconciliation shows 99.94%.

The timed results fall well inside the fifteen-minute requirement, even at the slowest. Completeness above 99.9% meets the target for priority sources. Passing unit and pipeline tests shows the logic and data flow behave as specified. Together these verify that the system was built as designed. Amara records the date, rule version and tester beside each result, so the evidence can be matched to the exact configuration that produced it, even after later changes.

### 46.5 Validation

The purple team re-runs the two techniques that previously left no trace; both now alert, and analysts follow the playbook correctly.

Verification showed the system matched its specification; validation shows it now catches the realistic behaviour that was missed before. Analysts following the playbook correctly shows the human side works too. Closing the two gaps found earlier is the central evidence that the capstone achieved its purpose. The purple team's report is filed in the dossier with the earlier report, so the before-and-after comparison is easy to make.

### 46.6 Remaining gaps

Logons using the domain controllers' web management interface are not covered; they are logged as a follow-up item.

Reporting what is still uncovered is part of honest engineering. The web management interface is a different path that the new rule does not watch. Logging it as a follow-up means it is tracked with an owner rather than forgotten, and readers of the report know the limits of what was delivered. Amara estimates the effort needed to cover that path and hands the item to Paolo's backlog with her notes.

### 46.7 Report

The capstone report presents requirements with pass or fail, evidence, and gaps, with all data synthetic or anonymised.

Presenting requirements with a clear pass or fail lets readers see results at a glance. Evidence references let them check each one. Gaps show what still needs work. Keeping all data synthetic or anonymised means the report can be shared with assessors without exposing Lindqvist's systems or customers. Paolo reads the draft before submission and checks that each pass claim matches its evidence, sending back two claims whose wording went further than the data.

### Handover to operations

When the capstone ends, the rule, parser and playbook pass to the detection engineering team. Amara walks the on-call analysts through the playbook, adds the rule to the quarterly review list and records the owner. A system no one owns after the student leaves would decay quickly.

### Lessons from the build

The largest delay came from waiting for change windows at depots, not from engineering. Amara notes for future projects that scheduling with operations should start in the design phase.

### Worked example

Amara's results table: latency requirement met (max 13.1 min); false alerts 1, 0, 0, 1 per week (≤5 met); completeness 99.94% (met); CPU ≤ 1.7% (met); validation 2/2 techniques alerted. Gap: web management interface — open, owner assigned.

> **Synthetic case.** Results are invented.

### Errors and limits

Four weeks of operation is short; long-term false-alert rates may differ.

### Exercises

- **EX136 — Pilot false alert.** What caused the pilot false alert, and how was it resolved? *Rubric:* 3 = technician's unregistered laptop; registered properly; 2 = partial; 1 = suppressed; 0 = none.
- **EX137 — Requirements met.** Summarise verification results against requirements. *Rubric:* 3 = latency ≤13.1, false ≤1/week, completeness 99.94%, CPU ≤1.7%; 2 = three; 1 = one; 0 = none.
- **EX138 — Remaining gap.** What gap remains, and how is it handled? *Rubric:* 3 = web management interface logons; follow-up item with owner; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Build, verify and validate against each requirement, and report remaining gaps openly.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) plan a controlled failure trial of the monitoring pipeline; (2) detect silent source failures; (3) measure recovery and data loss; (4) improve resilience from trial results.

### 47.1 Purpose

The trial checks whether the SOC notices when its own data stops, and how well it recovers. Silent failures were ranked high in chapter 23.

Monitoring that fails silently is dangerous because the SOC continues to believe it can see activity it no longer receives. Testing this deliberately is the only way to know whether the safeguards work. The trial also tests recovery: once data flows again, how much of the gap can be filled, and how quickly? Results go into the reliability records.

### 47.2 Plan

With change approval, the team stops log forwarding from one portal web server for an hour during a quiet period, without telling analysts the exact time. A rollback is ready.

Change approval keeps the trial within Lindqvist's normal process and makes sure IT knows it is deliberate. A quiet period limits the risk of missing a real attack during the gap. Not telling analysts the exact time tests whether the silence check works, rather than whether people remember a scheduled event.

### Lab — detecting silent sources

```python
"""Detect log sources that have gone silent compared with their usual cadence (synthetic)."""
now = 600  # minutes since midnight (10:00)
last_seen = {"portal-web-1": 598, "portal-web-2": 599, "portal-web-3": 541, "dc-01": 597, "fw-edge": 520}
expected_gap = {"portal-web-1": 5, "portal-web-2": 5, "portal-web-3": 5, "dc-01": 5, "fw-edge": 120}
for src in sorted(last_seen):
    gap = now - last_seen[src]
    status = "SILENT" if gap > 3 * expected_gap[src] else "ok"
    print(f"{src:13} gap={gap:3} min expected<={expected_gap[src]:3} {status}")
```

Run with `python3 lab_silence.py`. Verified output:

```text
dc-01         gap=  3 min expected<=  5 ok
fw-edge       gap= 80 min expected<=120 ok
portal-web-1  gap=  2 min expected<=  5 ok
portal-web-2  gap=  1 min expected<=  5 ok
portal-web-3  gap= 59 min expected<=  5 SILENT
```

### 47.3 Reading the result

At 10:00, portal-web-3 has been silent for 59 minutes against an expected gap of at most 5, so it is flagged SILENT. The edge firewall's 80-minute gap is normal for its 120-minute cadence. Expected cadence per source avoids false alarms from naturally quiet sources.

Each source is judged against its own normal rhythm. A web server sending events every few seconds is clearly broken after 59 minutes of silence; a firewall that reports every two hours is not broken after 80 minutes. Without per-source cadence, the check would either miss quiet failures or alarm constantly on naturally slow sources.

### 47.4 Detection in the trial

The silence check runs every 10 minutes and pages on-call. In the trial, it paged 17 minutes after forwarding stopped, because the threshold was three times the expected gap plus the check interval.

The threshold of three times a five-minute gap gives fifteen minutes; with the check running every ten minutes, detection could take up to twenty-five. Seventeen minutes falls in that range, but it means a portal server could be silent for a quarter of an hour before anyone knew. The trial measures this delay precisely so it can be shortened.

### 47.5 Recovery

After forwarding restarts, buffered events arrive; reconciliation shows 99.2% of the hour's events recovered, with the rest lost when the local buffer filled.

Local buffers hold events while forwarding is stopped and send them when it resumes. The 0.8% lost when it filled shows the buffer was too small for an hour's gap. Reconciliation counts make the loss measurable instead of a guess. Amara notes which events were lost by time range, so investigators know exactly which minutes are incomplete. Her follow-up ticket asks for a larger buffer, sized from the event volume measured during that hour.

### 47.6 Improvements

Lower the silence threshold for portal servers to two times the gap; enlarge the local buffer to cover two hours.

A lower multiplier shortens detection for portal servers, whose steady flow makes false alarms unlikely. A two-hour buffer covers longer outages without loss. Both changes are tested again in the next trial to confirm they work as intended and do not create new noise. Both changes go through the normal change process with tests, and the threshold change is announced to analysts, who may notice more frequent pages from portal servers at first.

### Who knows about the trial

Only the trial lead, on-call engineer and SOC manager know the time; everyone else learns afterwards.

### Worked example

Amara's trial report: "Failure noticed after 17 minutes (target 15) — threshold lowered. 0.8% of events lost — buffer enlarged. Re-trial next month." The next trial pages after 12 minutes with no loss.

> **Synthetic case.** Times and figures come from the lab script and invented trials.

### Errors and limits

A planned trial at a quiet time is gentler than a real failure during an incident.

### Exercises

- **EX139 — Silence logic.** Why use an expected gap per source? *Rubric:* 3 = sources have different cadences; avoids false alarms; 2 = partial; 1 = one threshold; 0 = none.
- **EX140 — Trial timing.** Why did paging take 17 minutes, and what changed? *Rubric:* 3 = 3× gap threshold plus check interval; lowered to 2×; 2 = partial; 1 = unknown; 0 = none.
- **EX141 — Data loss.** What data was lost and how was it prevented next time? *Rubric:* 3 = 0.8% when buffer filled; buffer enlarged to two hours; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Deliberately fail parts of the pipeline under control to prove silent failures are noticed and recovery works.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble an evidence dossier proving the capstone meets its requirements; (2) organise evidence for assessors and auditors; (3) protect sensitive content; (4) link every claim to its evidence.

### 48.1 Purpose

The dossier lets someone who was not there check every claim. Assessors use it to grade; Lindqvist keeps it for auditors and future engineers.

Claims in a report are only as strong as the evidence behind them. The dossier gathers that evidence in one place so an assessor, auditor or future engineer can check any statement without asking Amara. It also protects Lindqvist: when someone later asks how the depot detection was proved, the answer is on file. Amara builds it as the project runs.

### 48.2 Structure

Requirements table with status; design documents and review log; implementation records (commits, change tickets); verification results (unit, pipeline, timed tests); validation results (purple-team re-test); reliability results (completeness, failure trial); operational data (false alerts per week); remaining gaps.

The order follows the project from need to operation, so a reader can trace how each stage built on the last. Including remaining gaps alongside successes shows a complete picture. Operational data, such as false alerts per week, show how the system behaves in normal use, not just in tests.

### 48.3 Claim–evidence links

Each claim in the report points to a dossier item by ID: "Latency met (E-14: timed test results, 5 runs)". Unsupported claims are removed.

An ID lets a reader jump straight to the supporting item. Stating what the item contains, such as five runs, tells them how strong the evidence is. Removing unsupported claims keeps the report honest: if Amara cannot point to evidence, the claim does not belong in the report. Amara builds the link table before writing the conclusions, so the conclusions cannot claim more than the table supports.

### 48.4 Sensitive content

Host names, depot addresses and rule details that would help evasion are replaced with placeholders in the assessor copy; the full version stays inside Lindqvist with access control.

Details that would help someone evade detection, such as exact rule conditions, should not circulate beyond those who need them. Placeholders keep the assessor copy readable while removing risk. The full version stays under access control inside Lindqvist, where engineers and auditors with a need can consult it. The privacy officer checks the assessor copy.

### 48.5 Integrity

Exported files are listed with hashes so later readers can confirm they are unchanged.

A hash list lets anyone recompute each file's hash and compare it with the recorded value. A match shows the file has not changed since export, whether by accident or deliberately. The hash list itself is signed off by Paolo, tying it to a known point in time. Assessors receive the hash list separately from the files. Recomputing a few hashes takes minutes and gives them confidence that what they are grading is exactly what was submitted, with no later edits.

### 48.6 Completeness check

Paolo checks that each requirement has at least one verification and, where relevant, one validation item.

A requirement with no verification item has not been shown to work; one with no validation item, where validation applies, has not been shown to matter in practice. Paolo's check catches gaps before submission. Any missing items are either added or the requirement's status is marked as unproven. He also samples five claims at random and follows each to its evidence. Two links point to outdated file names, which Amara corrects before the dossier is sealed.

### 48.7 Format

Plain formats — PDF for documents, CSV for data, text for scripts — keep the dossier readable for years.

Proprietary formats may need software that is unavailable years later. PDF, CSV and plain text open in many tools on any system. Choosing them means the dossier can still be read when Lindqvist's current tools have been replaced, which matters for audits that may come much later. Amara converts a spreadsheet with formulas into CSV plus a short note explaining how each derived column was calculated, so nothing depends on the spreadsheet program.

### Reading order

The dossier opens with a one-page index mapping each requirement to its evidence items, so an assessor can start from any requirement and reach the proof in two steps. A short glossary explains internal terms such as depot zone and possible-takeover alert. Amara asks a fellow student unfamiliar with Lindqvist to find three pieces of evidence using only the index; both difficulties she reports lead to clearer item titles.

### Worked example

Paolo's check finds requirement "completeness ≥ 99.9%" supported only by one week of reconciliation. Amara adds the full four-week reconciliation export as E-22 and updates the requirements table.

> **Synthetic case.** The dossier is invented.

### Errors and limits

Dossiers record what was tested; untested behaviour remains uncertain.

### Exercises

- **EX142 — Dossier sections.** List five dossier sections. *Rubric:* 3 = five of requirements, design/review, implementation, verification, validation, reliability, operations, gaps; 2 = three; 1 = one; 0 = none.
- **EX143 — Claim links.** How are claims linked to evidence? *Rubric:* 3 = each claim cites dossier item ID; unsupported removed; 2 = partial; 1 = vague; 0 = none.
- **EX144 — Completeness gap.** What gap did Paolo find, and how was it fixed? *Rubric:* 3 = completeness backed by one week only; full four-week export added; 2 = partial; 1 = vague; 0 = none.

### Synthesis

A dossier links every claim to evidence, protects sensitive detail and lets others check the work.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis that presents problem, design, implementation and evaluation; (2) discuss trade-offs and limitations; (3) relate the work to literature and practice; (4) write clearly for examiners and practitioners.

### 49.1 Structure

Introduction and problem; background and literature; requirements; design and alternatives; implementation; verification and validation; operation and reliability; discussion; limitations; conclusions; references; appendices.

The structure mirrors the engineering process, so readers can follow the work in the order it happened. Separating discussion from results keeps interpretation apart from measured facts. Limitations get their own chapter, which gives them proper weight rather than hiding them in the conclusion. References and appendices hold detail that would slow the main text, such as full test tables and the review log, so the chapters stay readable for both examiners.

### 49.2 The argument

Amara's thesis argues that a small SOC can close a network-monitoring gap in agentless depots using existing firewalls, measured requirements and staged validation, at low cost and without disrupting operations.

A thesis needs a claim that the evidence can support or refute. Amara's names the context, the method and the outcomes, so each part can be checked against the dossier. 'Low cost' and 'without disrupting operations' are supported by CPU measurements, the absence of dispatch outages and the reuse of existing firewalls.

### 49.3 Literature

Knerler, Parker and Zimmerman (2022) for SOC strategy; NIST SP 800-92 for log management; ATT&CK for technique coverage; Alahmadi et al. (2022) for alarm quality; Sundaramurthy et al. (2014) for analyst practice.

Each source supports a specific part of the argument: SOC strategy for the overall approach, log management guidance for the pipeline, ATT&CK for coverage, alarm-quality research for alert design and analyst studies for the playbook. Citing them where they are used, rather than in a general list, shows how each shaped the work.

### 49.4 Trade-offs

Logging only connection starts at two depots saved CPU but lost duration data; device continuity was shown as context rather than filter; volume was controlled by tiering.

Naming trade-offs shows the design was chosen, not just built. Losing duration data at two depots saved firewall load but limits some investigations there. Showing device continuity as context keeps analysts' judgement in the loop. Tiering controlled volume while keeping data available for longer investigations. Amara explains each with the figures that justified it, so examiners can weigh the choice themselves.

### 49.5 Limitations

One organisation; synthetic and anonymised data; short operation period; simulations chosen by people who knew the design.

Each limitation narrows how far the results can be generalised. One organisation may have unusual traffic; synthetic data may lack real oddities; a short period may hide slow problems; simulations by people who knew the design may be easier to catch than real attacks. Stating them lets readers judge the evidence fairly. She also notes which limitation would matter most to another SOC trying to reuse the approach, and what evidence would reduce it.

### 49.6 Style

Plain language, defined terms, figures with units, numbered requirements matched to evidence IDs.

Plain language makes the thesis accessible to both examiners. Defined terms prevent confusion between similar words, such as verification and validation. Units on every figure avoid misreadings. Matching requirement numbers to evidence IDs lets a reader check any result in a few seconds. Amara asks a classmate outside security to read two chapters and mark any sentence they had to read twice. Those sentences are rewritten. Acronyms are spelled out on first use in each chapter.

### 49.7 Practitioner value

A short appendix gives a reusable checklist for other SOCs with agentless sites.

A checklist distils the project into steps they can follow: confirm boundary logging, link an approved list to inventory, test with timed injections, validate with purple-team simulations. It turns a thesis into something useful beyond the university. Each item names the evidence that showed it mattered at Lindqvist, so readers can judge whether it applies to their own sites. The checklist fits on one page and avoids product names, which keeps it useful regardless of tools.

### Writing schedule

Amara drafts method and results chapters during the capstone while details are fresh, leaving introduction and discussion until results are final. Her tutor reviews one chapter every two weeks. Figures are generated by scripts stored with the dossier, so a corrected number updates every figure consistently rather than by hand.

### Ethics statement

The thesis states that no real customer data appears in it and that all operational figures were approved for release by Lindqvist.

### Worked example

Her tutor asks her to cut the background chapter by a third and expand the discussion of what failed — the first latency verification and the silent-source delay — because examiners value learning from failure.

> **Synthetic case.** The thesis is invented.

### Errors and limits

A thesis describes one project; generalisation needs other sites.

### Exercises

- **EX145 — Thesis argument.** State the thesis's central argument. *Rubric:* 3 = small SOC closes agentless depot gap with existing firewalls, measured requirements and staged validation, low cost; 2 = partial; 1 = vague; 0 = none.
- **EX146 — Trade-offs.** Name two trade-offs discussed. *Rubric:* 3 = connection-start logging lost duration; continuity as context; tiering (two); 2 = one; 1 = vague; 0 = none.
- **EX147 — Tutor advice.** What did the tutor ask Amara to change, and why? *Rubric:* 3 = shorten background, expand failures; examiners value learning from failure; 2 = partial; 1 = style; 0 = none.

### Synthesis

An engineering thesis tells a clear, evidenced story, discusses trade-offs and failures honestly and serves practitioners too.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) present and defend the engineering work; (2) answer technical and professional questions; (3) reflect on development across the course; (4) plan continued professional growth.

### 50.1 The defense

A 30-minute presentation and 45 minutes of questions from an academic examiner and an industry examiner.

The two examiners bring different perspectives: the academic checks method and reasoning, the industry examiner checks practical value and professional judgement. Thirty minutes forces Amara to focus on the most important points. Forty-five minutes of questions tests whether she understands the work deeply enough to defend it. The examiners have read the thesis and dossier beforehand, so questions can go straight to detail. The outcome is decided privately after the session and given to Amara the same day.

### 50.2 Presentation

Problem and evidence of need; requirements; design and review; results against requirements; failures and fixes; remaining gaps; lessons.

The order follows the thesis argument. Including failures and fixes shows learning, not only success. Amara rehearses with Paolo and a classmate, timing each part so she does not run out of time before the results. Slides carry few words and clear figures, such as the stacked stage-time bars, which the examiners can read quickly. Every result slide names its evidence ID so examiners can check the dossier during questions.

### 50.3 Expected questions

"Why not deploy agents?" "How do you know five false alerts per week is acceptable?" "What happens when the person maintaining the approved-device list leaves?" "What would you do differently?"

Preparing for likely questions lets Amara answer clearly rather than improvising. Each question probes a different weakness: design choices, how a threshold was set, sustainability after she leaves, and self-reflection. She writes short answers backed by evidence for each and practises delivering them. She also prepares for the question she fears most, about the uncovered web interface path.

### 50.4 Answering

Answer directly, show evidence, admit limits. On false alerts: the night shift agreed the threshold based on measured triage time; it is reviewed quarterly.

Direct answers show confidence; evidence shows the answer is grounded; admitting limits shows honesty. The false-alert threshold came from measured triage time and agreement with the night shift, not from a guess, and quarterly review ensures it stays appropriate. When she does not know an answer, Amara says so and explains how she would find out, which examiners generally respect more than a confident guess that later turns out to be wrong.

### 50.5 Professional questions

The industry examiner asks how Amara handled a disagreement with depot managers; she describes rescheduling around dispatch and what she learned.

The industry examiner is interested in how Amara works with others, a skill that matters as much as technical ability in a SOC. Describing a real disagreement and how she resolved it, by rescheduling around dispatch, shows she can balance security goals with business needs. She admits that her first proposal ignored dispatch peaks and explains how the managers' feedback changed the rollout schedule.

### 50.6 Reflection

From calculus of queues in chapter 1 to the capstone, the course built a path: model, measure, design, verify, validate, operate.

The path from modelling queues to building and validating a detection shows how the early chapters' tools became practical skills. Each step built on earlier ones: measurement relied on statistics, design on architecture, verification on programming. Amara sees the course as a single connected method rather than separate subjects. The examiners ask which early subject she used most; she names statistics, because almost every decision rested on measured rates and percentiles.

### 50.7 Next steps

Amara plans to join Lindqvist as a junior detection engineer and to study for further qualifications.

Joining Lindqvist lets Amara continue the depot work, including the follow-up on the web management interface. Further qualifications deepen her knowledge in areas she found challenging during the capstone. She leaves the placement with a clear plan and a record of evidence of what she can do. Paolo agrees to stay her mentor during her first year, and they set goals for her first six months on the team.

### Preparing

Amara rehearses twice with Paolo and once with fellow students who play hostile examiners. Each rehearsal produces a list of weak answers, which she strengthens with evidence from the dossier. She prepares backup slides for detailed questions on latency and completeness but keeps the main talk short and focused on decisions.

### After the defense

Examiners return minor corrections within a week: two figures need clearer units and one limitation needs expanding. Amara makes them, her tutor confirms, and the final thesis and dossier index are deposited.

### Worked example

Asked "What would you do differently?", Amara answers: "Start operational scheduling in design, test under busy conditions earlier, and involve analysts in requirements from day one — every late fix in my project traced to one of those."

> **Synthetic case.** The defense is invented.

### Errors and limits

A defense samples the work; the dossier carries the full evidence.

### Exercises

- **EX148 — Talk outline.** Outline the defense presentation. *Rubric:* 3 = need, requirements, design/review, results, failures, gaps, lessons; 2 = five; 1 = two; 0 = none.
- **EX149 — Threshold justification.** How did Amara justify five false alerts per week? *Rubric:* 3 = agreed with night shift from measured triage time; reviewed quarterly; 2 = partial; 1 = arbitrary; 0 = none.
- **EX150 — Differently.** What three things would Amara do differently? *Rubric:* 3 = scheduling in design, busy testing earlier, analysts in requirements; 2 = two; 1 = one; 0 = none.

### Synthesis

The defense closes the course: model, measure, design, verify, validate and operate, with honest reflection on what to improve.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Amara Osei, Paolo Ricci, Kingsbridge Engineering University, Lindqvist Freight and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The backlog changes at dB/dt = A(t) − C(t): arrivals per hour minus alerts cleared per hour.

**EX002.** It peaks at 65 alerts at 13:00, because arrivals ran above the capacity of 60 from 10:00 to 12:00 and only matched it at 13:00.

**EX003.** Roughly 40 minutes: 40 alerts are ahead of it and the shift clears 60 per hour.

**EX004.** It holds accounts that failed and then succeeded from the attacking network, the ones most likely to have been guessed correctly.

**EX005.** 7 × 6 × 5 = 210, so rules cannot cover every combination and must be chosen using threat knowledge.

**EX006.** It requires at least one success from the same set, turning a general spraying alert into a specific possible-compromise alert.

**EX007.** It is folded into a single 5-minute record, so the burst is visible but its pace and shape are lost.

**EX008.** It can put events from that server in the wrong order relative to others, which is why log management guidance stresses time synchronisation.

**EX009.** More data needs more servers, power, cooling and storage space, all of which are physically limited and costly.

**EX010.** It should skip them safely and record how many were skipped, so data loss is visible.

**EX011.** Because the correct answer is known in advance, any difference shows a bug in the code rather than something in the data.

**EX012.** It avoids installing unreviewed third-party packages on sensitive machines and is already available everywhere Python is.

**EX013.** What was observed, when with time zone, which assets, what was done, and what remains unknown.

**EX014.** So every reader understands the same level of certainty from the same word.

**EX015.** It gives timing, scale, impact, actions taken and a proposed change, without the field-level detail analysts need.

**EX016.** Storage is the integral of ingestion rate over the retention window; today 120 GB × 90 days = 10.8 TB.

**EX017.** About 15.4 TB, since daily ingestion reaches roughly 171 GB, which exceeds the 12 TB tier.

**EX018.** Policy and law set minimum retention; maths estimates cost and guides tiering within those limits.

**EX019.** True-positive rate is the chance of an alert when an attack happens; precision is the chance an alert is a real attack.

**EX020.** 0.153, so roughly one alert in seven is real: about 180 true against 998 false per 100,000 bursts.

**EX021.** Because false alarms dominate at this low base rate, halving them lifts precision to about 0.27, much more than a small sensitivity gain would.

**EX022.** Kernel components see process and file activity reliably, but a defect there can crash the whole machine.

**EX023.** The agent's buffer filled while the link was saturated by the burst, so older events were discarded.

**EX024.** They balance visibility against CPU and memory cost and test settings on machines that resemble production.

**EX025.** A dictionary, because each username maps directly to its count with fast lookups and updates.

**EX026.** The code used greater-than while the design meant at-least; both were aligned to ≥ 5 and the test kept.

**EX027.** It keeps memory use small, whereas loading millions of lines at once can exhaust memory.

**EX028.** Monitor only what the security purpose needs and access content such as email bodies only with case approval.

**EX029.** There was no authorised investigation, so she referred the manager to policy and the HR process.

**EX030.** The range also served a logistics partner, so a temporary block with 24-hour review avoided disrupting legitimate traffic.

**EX031.** Attackers spread attempts across many addresses in the same networks, so grouping reveals bursts per-address counts hide.

**EX032.** 203.0.113.0/24, because its six failures hit six different usernames, one attempt each, and seven usernames appear there in all.

**EX033.** It requested an address change at 10:07, suggesting the account was taken over.

**EX034.** Because the audit setting the rule depends on, such as command-line process logging, is not enabled there.

**EX035.** They grant more privilege, which attackers seek, so changes deserve attention.

**EX036.** The server template was updated through a change, and a harmless test process confirmed command lines were now logged.

**EX037.** So every rule and query uses one name for each concept instead of remembering source-specific variants.

**EX038.** The portal stored local-time text while internal logs used UTC; converting portal times at ingestion fixed the join.

**EX039.** The fields detections and analysts query most, such as user, host and source address.

**EX040.** The rule records matches without alerting so its noise can be measured before analysts are paged.

**EX041.** With a narrow exception using the load tool's signed user agent and a calendar check.

**EX042.** A description, the author, references, known benign triggers and response guidance.

**EX043.** Customer data could be viewed, an address was altered, and the login service slowed under the burst.

**EX044.** Customers reusing passwords; rate limiting and multi-factor authentication reduce the risk.

**EX045.** It mainly delivers Detect and Respond, relying on Identify for asset knowledge and informing Govern.

**EX046.** Spending heavily on tools while neglecting people and process.

**EX047.** Portal logs delivered within 2 minutes, rule latency under 5 minutes and analyst acknowledgement within 8 minutes.

**EX048.** The burst was acknowledged 11.5 minutes after injection, within target, with analyst acknowledgement the slowest step.

**EX049.** Overly large or quick adjustments overshoot; small steps with time to observe effects prevent it.

**EX050.** An overloaded queue pushes analysts to close alerts hastily, which hides misses and allows more compromise, adding further load.

**EX051.** At most one threshold step per fortnight and no increase after any missed test event; it settled at 6 failures with 8 false alerts a day and all test events caught.

**EX052.** Because legitimate traffic across a boundary is limited and well known, unusual crossings stand out.

**EX053.** Load-balancer logs were not forwarded; they were added, and web logs now record a client-address header that the balancer overwrites so clients cannot forge it.

**EX054.** They sit in a separate zone with dedicated administrator accounts protected by multi-factor authentication.

**EX055.** Because many attacks use stolen but valid credentials, which only identity logs reveal.

**EX056.** Repeated MFA prompts the user denies, and an unexpected change of the registered MFA device.

**EX057.** She added an email confirmation to the customer and kept an analyst alert only when confirmation failed.

**EX058.** Engineering priorities follow what the company must protect — customer data, deliveries, payments — rather than what tools can do.

**EX059.** Their old software cannot run endpoint agents, so network monitoring is the only option.

**EX060.** With only two analysts at night, every alert routed to them must be worth their limited time.

**EX061.** Functional: correlate failures and successes per network; non-functional: alert latency under 5 minutes.

**EX062.** "Alerts shall be raised within 5 minutes of the triggering event, measured by monthly timed synthetic events."

**EX063.** The requirement, its source, the design element meeting it and the test verifying it.

**EX064.** Collect, transport, parse and normalise, enrich, store, detect, alert, and case management.

**EX065.** The asset inventory did not contain depot devices, so there was nothing to enrich with.

**EX066.** Each empty cell became a backlog item with a named owner.

**EX067.** The data sources it needs, the detections present and the confidence in them.

**EX068.** Because nothing signals them, detection coverage disappears without anyone noticing.

**EX069.** Account-takeover detection depends on that single feed, which has broken before.

**EX070.** Threshold 5 with success: 2, 0, 1; threshold 6 with success: 1, 0, 2; threshold 5 without success: 3, 2, 0.

**EX071.** One detects attempts for daytime tuning work; the other detects likely compromise and pages the night shift.

**EX072.** The attack at 10:10 had not succeeded, so there was no compromise to page about; the attempts rule still captures it.

**EX073.** Flow monitoring at the boundary, a network detection sensor, and tighter firewall rules with denied-connection logging.

**EX074.** They found the boundary firewall already logged flows, so firewall logs plus allow rules beat buying a sensor.

**EX075.** Allow five services, log denials, alert when a depot device tries a new destination more than three times an hour, review weekly; the main risk is the log feed failing.

**EX076.** Recent high-value data is kept in the SIEM for fast search while bulk and older data goes to a cheaper lake.

**EX077.** It adds night coverage and broader threat knowledge, but knows less about local context and depends on clear escalation agreements.

**EX078.** Context, options considered, the decision and its consequences.

**EX079.** Detective: the possible-takeover rule; responsive: locking the account and invalidating its sessions.

**EX080.** A cap of 20 accounts per hour, after which automation pauses and pages the on-call engineer.

**EX081.** Because blocking a range can cut off legitimate customers or partners, which needs human judgement.

**EX082.** A test SIEM with replayed synthetic data, then production in monitor-only mode, then full alerting.

**EX083.** An extra field from a balancer update; the parser was extended and the lines kept as test cases.

**EX084.** It makes every change reviewable, reversible and consistent across environments.

**EX085.** Mean 10.2 minutes, median 7 minutes, 90th percentile 16.4 minutes.

**EX086.** Times are skewed; one long case inflates the mean, while the median shows the typical case and the 90th percentile the tail that threatens the target.

**EX087.** Pair it with quality measures such as regular review of a sample of closed alerts.

**EX088.** Verification checks the rule matches its specification; validation checks it actually helps detect real threats in operation.

**EX089.** That the rule fires at 5 users with success, stays quiet at 4, needs a success even at 9 users, and stays quiet with no activity.

**EX090.** The alert lacked the customer ID because the routing template used an old field name.

**EX091.** To discover problems, such as the printer dependency, before they affect all forty depots.

**EX092.** The print service was allowed with a documented reason, and other depots were checked for the same printers before the next group.

**EX093.** A contractor's laptop on a depot network; IT then enforced network access control for visiting devices.

**EX094.** Because a pipeline can be up while silently missing events, leaving the SOC blind.

**EX095.** Low-value debug logs should drop before authentication and other priority logs, using priority queues.

**EX096.** UDP syslog dropped packets under load; switching to TCP forwarding with a local buffer raised completeness to 99.96%.

**EX097.** Because isolating them could halt business operations such as dispatch, so approval is required first.

**EX098.** Query critical sources directly with read-only accounts following runbooks, recording actions offline.

**EX099.** Expired direct-access accounts, runbooks naming retired servers, and no named night decision-maker for isolating dispatch.

**EX100.** So that a SOC "high" reliably becomes an IT P2 with a known four-hour response.

**EX101.** It can only place holds and invalidate sessions, and every call it makes is logged.

**EX102.** A firewall change had blocked delivery to customer service; the failure path alerted on-call, who fixed it before a re-test passed.

**EX103.** Five rules produced 55% of night alerts, and three had never led to an incident.

**EX104.** With a dedicated 30-minute morning review slot and a cap on that queue.

**EX105.** Paging only on critical assets would ignore the 60% of systems the inventory had not classified.

**EX106.** 6,000 EPS average, 15,000 at peak, 285.1 GB per day and 25.7 TB for 90 days hot.

**EX107.** Filter valueless events, summarise high-volume sources and tier older data to cheaper storage.

**EX108.** That no detection rule depended on raw firewall events older than seven days.

**EX109.** Open cases, alerts awaiting action, system health issues and expected events such as maintenance.

**EX110.** By writing triage notes for each rule, capturing what experienced analysts check.

**EX111.** The signals conflicted — a new network but the customer's usual device — so she escalated instead of guessing.

**EX112.** Alerted; logged but not alerted, fixed with a new or tuned detection; not logged, fixed by adding a data source.

**EX113.** Seven alerted, three were only logged, and two left no trace, both in depot networks.

**EX114.** So detections are not tailored to the test rather than to the underlying behaviour.

**EX115.** Proposed, testing, monitor-only, active, under review and retired.

**EX116.** Twelve were kept after test events confirmed them, fifteen retired with a decommissioned system, and four merged into newer rules.

**EX117.** Repetitive manual work that grows with load, such as restarting a stuck collector by hand.

**EX118.** R1, R2 and R4 passed; R3 (busy, 19.7 minutes) and R5 (handover, 16.8 minutes) failed.

**EX119.** Ingestion slowed during the busy period and acknowledgement was slow both then and at handover; detection stayed steady.

**EX120.** Portal logs were prioritised and the alert paged to a dedicated device; re-runs passed at 12.9 and 13.4 minutes.

**EX121.** Because improving stages that are not limiting, such as detection here, would not change overall response time.

**EX122.** By tracking what happened to alerts from the moved rules to confirm no harm from slower response.

**EX123.** Response targets were met, further optimisation would yield little, and the depot gap from validation posed more risk.

**EX124.** Whether adding device continuity to takeover alerts cuts false escalations without causing real takeovers to be missed.

**EX125.** It would have de-prioritised 29 of 70 benign alerts and 1 of 12 real takeovers, the latter involving a stolen phone.

**EX126.** Because filtering would have hidden a real takeover in which the attacker held the customer's own device.

**EX127.** Deliver the depot logging project, maintain three rules, work one queue day a week and write two runbooks.

**EX128.** She learned to frame requests around dispatch needs and to check the depot calendar before scheduling.

**EX129.** Anonymised credential-stuffing indicators with a sector information-sharing group.

**EX130.** Detect remote logons from depot networks to domain controllers within 15 minutes with no more than five false alerts a week.

**EX131.** Agents on depot devices and changes to depot applications are excluded, keeping the project achievable.

**EX132.** That logging must not raise boundary firewall CPU by more than 2%, measured before and after.

**EX133.** Finding 2, because ignoring the second protocol left a coverage gap in the core requirement.

**EX134.** The list was linked to the asset inventory and reconciled weekly.

**EX135.** Volume was 3.2 times higher, so two large depots log only connection starts to stay under the 2% CPU limit.

**EX136.** A depot technician's unregistered laptop; the device was registered properly.

**EX137.** Maximum latency 13.1 minutes, at most one false alert a week, 99.94% completeness and firewall CPU no higher than 1.7%.

**EX138.** Logons through the domain controllers' web management interface, recorded as a follow-up with an owner.

**EX139.** Because sources report at different rates; a firewall that naturally sends every two hours should not be flagged after one.

**EX140.** The threshold of three times the gap plus the 10-minute check interval delayed it; the threshold was lowered to twice the gap.

**EX141.** About 0.8% of the hour's events, lost when the buffer filled; the buffer was enlarged to cover two hours.

**EX142.** The requirements table, design and review log, implementation records, verification results and validation results.

**EX143.** Each claim cites a dossier item ID, and any claim without evidence is removed.

**EX144.** Completeness was supported by only one week; the four-week reconciliation export was added as E-22.

**EX145.** A small SOC can close the agentless-depot monitoring gap using existing firewalls, measured requirements and staged validation, cheaply and without disrupting operations.

**EX146.** Logging only connection starts saved CPU but lost duration data, and device continuity was shown as context rather than used as a filter.

**EX147.** To shorten the background and expand discussion of failures, because examiners value how the project learned from them.

**EX148.** Need, requirements, design and review, results against requirements, failures and fixes, remaining gaps, lessons.

**EX149.** The night shift agreed it based on measured triage time, and it is reviewed every quarter.

**EX150.** Start scheduling with operations during design, test under busy conditions earlier and involve analysts in requirements from the start.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and telemetry in this book are synthetic unless a sentence cites a public source.


- Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. *31st USENIX Security Symposium*, 2783–2800. <https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi>
- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations* (NIST SP 800-137). <https://doi.org/10.6028/NIST.SP.800-137>
- Hassan, W. U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., & Bates, A. (2019). NoDoze: Combatting threat alert fatigue with automated provenance triage. *NDSS Symposium*. <https://doi.org/10.14722/ndss.2019.23349>
- Kaloroumakis, P. E., & Smith, M. J. (2021). *Toward a Knowledge Graph of Cybersecurity Countermeasures* (MITRE D3FEND). The MITRE Corporation. <https://d3fend.mitre.org/resources/D3FEND.pdf>
- Kent, K., & Souppaya, M. (2006). *Guide to Computer Security Log Management* (NIST SP 800-92). <https://doi.org/10.6028/NIST.SP.800-92>
- Knerler, K., Parker, I., & Zimmerman, C. (2022). *11 Strategies of a World-Class Cybersecurity Operations Center* (2nd ed.). The MITRE Corporation. <https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center>
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., & Ahn, G.-J. (2019). Matched and mismatched SOCs: A qualitative study on security operations center issues. *ACM CCS 2019*, 1955–1970. <https://doi.org/10.1145/3319535.3354239>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (NIST SP 800-61 Rev. 3). <https://doi.org/10.6028/NIST.SP.800-61r3>
- SigmaHQ. *Sigma: Generic signature format for SIEM systems* (rule specification and repository). <https://github.com/SigmaHQ/sigma>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018, rev. 2020). *MITRE ATT&CK: Design and Philosophy* (MP180360R1). The MITRE Corporation. <https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf>
- Sundaramurthy, S. C., Case, J., Truong, T., Zomlot, L., & Hoffmann, M. (2014). A tale of three security operation centers. *ACM Workshop on Security Information Workers (SIW '14)*, 43–50. <https://doi.org/10.1145/2663887.2663904>
- van Os, R. (2016). *SOC-CMM: Designing and Evaluating a Tool for Measurement of Capability Maturity in Security Operations Centers* (Master's thesis). Luleå University of Technology. <https://ltu.diva-portal.org/smash/get/diva2:1031560/FULLTEXT02>
- Vielberth, M., Böhm, F., Fichtinger, I., & Pernul, G. (2020). Security operations center: A systematic study and open challenges. *IEEE Access*, 8, 227756–227779. <https://doi.org/10.1109/ACCESS.2020.3045514>
- Zimmerman, C. (2014). *Ten Strategies of a World-Class Cybersecurity Operations Center*. The MITRE Corporation. ISBN 978-0-692-24310-7. <https://www.mitre.org/sites/default/files/publications/pr-13-1028-mitre-10-strategies-cyber-ops-center.pdf>
