# Security Architecture and Engineering: Engineering Course

- Language: English (`en`); course 122, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; fifteen offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students who will design, verify and operate secure systems.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs compute growth, closure, probabilities, availability, fault trees, rate limits, rule differences, metrics and digests on synthetic data, and use sqlite3 in memory to show injection and its fix; nothing touches a real system. Production designs use vetted products and standards; never roll your own cryptography. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one engineering student from mathematics, physics and programming foundations through networks, systems engineering and security architecture to a full back-office design, two studios, two verification labs, a recovery trial, a dossier, a thesis and a defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Sofia Mbeki** | Engineering student | Invented |
| **Daniel Ferreira** | Security architect and mentor | Invented |
| **Kestrel Polytechnic University** | Fictional university | Invented |
| **Corvia Regional Transit** | Fictional transit operator | Invented |

### Core sources

Saltzer and Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); NIST [SP 800-160 Vol. 1 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v1r1), [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5), [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); Shostack (2014); Anderson (2020); SABSA; TOGAF G152. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) use rates of change to reason about growing security workloads; (2) model exponential growth of log volume; (3) recognise when a linear estimate fails.

### 1.1 The case and why calculus

Sofia Mbeki is a first-year student in the five-year engineering programme at the fictional Kestrel Polytechnic University. Her industry partner throughout the course is the fictional Corvia Regional Transit, which runs buses and trams, a contactless fare system, a passenger app and depot networks. Her mentor there is security architect Daniel Ferreira. Every person, organisation and number here is synthetic. Sofia wonders why an architecture course starts with calculus. Daniel's answer is practical: architects size systems that grow, and derivatives describe how fast things change. A log pipeline, a certificate fleet or a rule base that grows faster than expected becomes a security problem long before anyone notices.

### 1.2 Exponential growth of logs

Corvia's fare-system logs grow about four per cent per month as new devices are installed. Sofia models volume as V(t) = V0 e^(kt), where k is the monthly growth rate in continuous form. The derivative dV/dt = kV shows that the increase each month is proportional to the current volume, so absolute growth accelerates. The lab below computes the volume after two years from a synthetic starting point and the time until the current storage budget is exceeded. The result shows the budget runs out more than a year earlier than a straight-line estimate predicts, which matters because dropped logs blind the security monitoring team.

### Lab — Log growth and storage budget

```python
# Synthetic log volume: V(t) = V0 * e^(k t), k from 4%/month; compare with tangent-line forecast.
import math
V0, budget = 8.0, 20.0            # TB at month 0, storage budget in TB
k = math.log(1.04)
exp_v = lambda t: V0 * math.exp(k * t)
lin_v = lambda t: V0 + k * V0 * t  # tangent line at t=0
m = next(t for t in range(200) if exp_v(t) > budget)
ml = next(t for t in range(200) if lin_v(t) > budget)
print(f"month 24: exponential {exp_v(24):.1f} TB, linear {lin_v(24):.1f} TB")
print(f"budget {budget} TB exceeded: exponential month {m}, linear month {ml}")
```

Run with `python3 lab_growth.py`. Verified output:

```text
month 24: exponential 20.5 TB, linear 15.5 TB
budget 20.0 TB exceeded: exponential month 24, linear month 39
```

### 1.3 When linear estimates fail

A linear estimate assumes a constant increase per month and is accurate only over short periods. Sofia compares the tangent line at month zero, the derivative-based linear forecast, with the exponential model. For the first few months they agree closely; by month twenty-four they diverge by a large margin. Architects often plan capacity from last year's increase, which is a linear view of an exponential process. The lesson is general: whenever a quantity grows in proportion to itself, such as connected devices or stored events, use a growth model and revisit it as real data arrive.

### Worked example

Sofia fits a four per cent monthly growth model to synthetic log volumes, computes when storage is exceeded and shows Daniel the gap between linear and exponential forecasts.

> **Synthetic case.** Kestrel Polytechnic, Corvia Regional Transit, Sofia, Daniel and all figures are invented.

### Errors and limits

Real growth is rarely smooth; new device rollouts cause jumps. Models must be refitted to measured data.

### Exercises

- **EX001 — Proportional growth.** What does dV/dt = kV tell Sofia about log growth? *Rubric:* 3 = increase each month is proportional to current volume, so absolute growth accelerates;; 2 = proportional;; 1 = constant growth;; 0 = none.
- **EX002 — Budget month.** In the lab, in which month is the storage budget first exceeded under the exponential model? *Rubric:* 3 = month 24, versus month 39 for the linear forecast;; 2 = month 24;; 1 = vague;; 0 = none.
- **EX003 — Linear planning.** Why is planning from last year's increase risky for log storage? *Rubric:* 3 = it applies a linear view to an exponential process and underestimates growth;; 2 = underestimates;; 1 = accurate;; 0 = none.

### Synthesis

Calculus lets architects see how fast security workloads grow and avoid linear plans for exponential systems.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) represent access rights as relations and graphs; (2) compute transitive closure to find indirect access; (3) use set operations to check separation of duties.

### 2.1 Access as a relation

Daniel shows Sofia that an access-control list is a relation: a set of pairs (subject, object). Group membership is another relation: (user, group). Groups can contain groups. Writing these as sets lets Sofia reason precisely. If user ana is in group fare-ops, and fare-ops is in group fare-admins, and fare-admins can modify tariff tables, then ana can modify tariffs, even though no single entry says so. Discrete mathematics gives the tool for this: composition of relations and transitive closure, which make indirect rights visible instead of leaving them buried in nested groups that nobody reads.

### 2.2 Transitive closure

The transitive closure of a relation adds every pair reachable through a chain. Sofia writes a small Python program that takes Corvia's synthetic nested group memberships and computes, for every user, all groups they belong to directly or indirectly, then the objects those groups can access. The lab below runs on a synthetic directory and shows one contractor account inheriting tariff-modification rights through three levels of nesting. The audit had missed it because reviewers looked only at direct memberships. Closure computations of this kind underlie many commercial access-review tools, but understanding them lets an engineer check the tools.

### Lab — Indirect rights via transitive closure

```python
# Transitive closure of synthetic nested groups; find indirect tariff rights and SoD conflicts.
member = {"ana": {"fare-ops"}, "ben": {"tariff-approvers"}, "contractor-07": {"vendor-support"},
          "vendor-support": {"field-tech"}, "field-tech": {"fare-ops"}, "fare-ops": {"fare-admins"},
          "dina": {"tariff-approvers", "fare-ops"}}
rights = {"fare-admins": {"tariff:create"}, "tariff-approvers": {"tariff:approve"}}
def closure(x, seen=None):
    seen = seen or set()
    for g in member.get(x, ()):
        if g not in seen: seen.add(g); closure(g, seen)
    return seen
users = ["ana", "ben", "contractor-07", "dina"]
eff = {u: set().union(*(rights.get(g, set()) for g in closure(u))) for u in users}
for u in users: print(f"{u:14} groups={len(closure(u))} rights={sorted(eff[u])}")
create = {u for u in users if "tariff:create" in eff[u]}; approve = {u for u in users if "tariff:approve" in eff[u]}
print("create & approve conflict:", sorted(create & approve))
```

Run with `python3 lab_closure.py`. Verified output:

```text
ana            groups=2 rights=['tariff:create']
ben            groups=1 rights=['tariff:approve']
contractor-07  groups=4 rights=['tariff:create']
dina           groups=3 rights=['tariff:approve', 'tariff:create']
create & approve conflict: ['dina']
```

### 2.3 Separation of duties as sets

Corvia requires that nobody can both create a tariff change and approve it. In set terms, the set of users able to create and the set able to approve must be disjoint. Sofia computes both sets from the closure and their intersection. A non-empty intersection is a violation. This is the separation of privilege principle from Saltzer and Schroeder (1975) expressed as a simple set test. She notes that set reasoning catches structural violations but not collusion between two people, which needs process controls such as logging and review.

### Worked example

Sofia computes the closure of synthetic nested groups, finds a contractor with indirect tariff rights and tests create and approve sets, finding dina in both.

> **Synthetic case.** Users, groups and rights are synthetic; Saltzer and Schroeder (1975) is real.

### Errors and limits

Closure assumes memberships are current; stale data hide or invent rights. Disjoint sets do not prevent collusion.

### Exercises

- **EX004 — Hidden right.** Which account gained tariff rights indirectly in the lab, and through how many levels? *Rubric:* 3 = contractor-07, through a chain of four groups ending in fare-admins;; 2 = account;; 1 = vague;; 0 = none.
- **EX005 — SoD test.** How is separation of duties expressed with sets? *Rubric:* 3 = creators and approvers sets must be disjoint; intersection empty;; 2 = disjoint;; 1 = union;; 0 = none.
- **EX006 — Collusion gap.** What does a disjoint-set check fail to prevent? *Rubric:* 3 = collusion between two different people;; 2 = collusion;; 1 = nothing;; 0 = none.

### Synthesis

Relations, closure and set tests turn tangled access rules into precise, checkable statements.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical phenomena to hardware security risks; (2) explain why emanations and power use can leak information; (3) connect physical limits to architecture choices.

### 3.1 Information is physical

Sofia's physics module covers electricity, signals and heat. Daniel connects it to security: computers are physical devices, so computation produces measurable effects such as power variation, electromagnetic emission, timing differences and heat. Anderson (2020) describes how such side channels have leaked keys and data. For an architect, the lesson is not to build measurement rigs but to recognise where physical access or proximity creates risk, such as fare-card readers mounted on public buses where an attacker can touch, open or attach instruments to the device for hours without being noticed by staff.

### 3.2 Power, timing and emissions

Power consumption varies with the operations a chip performs. If a device's power use depends on secret data, an attacker measuring it can sometimes recover the secret; this is called power analysis. Timing works similarly in software, which is why constant-time comparisons are used for secrets. Electromagnetic emissions from cables and screens can carry signals too. Sofia learns that defending against these is mainly a job for hardware designers and certified secure elements, and that an architect's responsibility is to choose components evaluated against such attacks for places where attackers have physical access.

### 3.3 Physical limits in architecture

Physics also sets limits that architects must respect. Signal propagation and network latency mean a tram's fare validator cannot always reach the central server in time, so it must make some decisions offline with locally stored keys and deny lists. Batteries and heat limit how much cryptographic work a handheld inspector device can do. Physical tamper resistance costs money and size. Sofia writes a short note for Daniel explaining that fare validators should use secure elements for keys and should be designed to work offline safely, because physics, not preference, forces that design.

### Worked example

Sofia lists three physical side channels, maps them to Corvia's on-vehicle fare readers and argues for secure elements and safe offline operation.

> **Synthetic case.** Device placements and design notes are synthetic; Anderson (2020) is real.

### Errors and limits

Side-channel risk depends on attacker access and skill; not every device needs the same protection. Physics limits change as hardware improves.

### Exercises

- **EX007 — Physical access risk.** Why are on-bus fare readers more exposed to side channels than data-centre servers? *Rubric:* 3 = attackers can touch and instrument them for long periods in public;; 2 = access;; 1 = same risk;; 0 = none.
- **EX008 — Architect role.** What is the architect's responsibility regarding power analysis? *Rubric:* 3 = choose components evaluated against it where physical access exists;; 2 = choose components;; 1 = build rigs;; 0 = none.
- **EX009 — Offline by physics.** Why must fare validators make some decisions offline? *Rubric:* 3 = latency and connectivity limits mean the server may be unreachable in time;; 2 = latency;; 1 = preference;; 0 = none.

### Synthesis

Physics shapes both the threats to devices and the constraints on secure architecture designs.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small, readable programs that validate input; (2) handle errors without leaking sensitive detail; (3) use the standard library rather than reinventing security functions.

### 4.1 Programs that check input

Sofia's first programming course uses Python. Daniel asks her to write a parser for synthetic fare-tap records: card identifier, validator identifier, timestamp and amount. Her first version trusts every field. He gives her malformed lines, such as a negative amount, a timestamp in the future and a card identifier with unexpected characters, and the program either crashes or accepts nonsense. She rewrites it to validate each field against an allow-list pattern and range, rejecting the line with a reason. Input validation at boundaries is one of the most basic secure-design habits, and it starts with the first programs a student writes.

### 4.2 Errors without leaks

When validation fails, the program must report enough for an operator to fix the problem but not expose secrets or internal details to whoever supplied the input. Sofia separates two messages: a short public error such as invalid record, and a detailed internal log entry with the line number and reason, written to a file with restricted permissions. She avoids printing stack traces to users. Daniel explains that verbose errors in web services have revealed database names, file paths and versions to attackers, giving them a map. Error handling is part of the interface and deserves the same design care.

### 4.3 Standard library first

Sofia needs random identifiers for test cards. She first uses the random module, then learns that for anything security-relevant Python's secrets module is required, because it draws from the operating system's secure source. She also needs to compare an authentication tag and learns to use hmac.compare_digest. Daniel's rule is simple: use the standard library or a well-maintained package for security functions, read its documentation, and never write a cipher, hash or random generator yourself. Programming skill is shown by composing reliable parts correctly, not by recreating them.

### Worked example

Sofia rewrites a fare-record parser with allow-list validation, separate public and internal error messages, and secrets-generated test identifiers.

> **Synthetic case.** Records, formats and identifiers are synthetic.

### Errors and limits

Allow-lists need maintenance when formats change. Internal logs can still leak if their permissions or retention are wrong.

### Exercises

- **EX010 — Three malformed fields.** Name three malformed inputs Daniel used to break Sofia's first parser. *Rubric:* 3 = negative amount, future timestamp, card id with unexpected characters;; 2 = two;; 1 = one;; 0 = none.
- **EX011 — Two messages.** What two kinds of error message does Sofia produce? *Rubric:* 3 = short public message and detailed internal log with restricted access;; 2 = both;; 1 = stack trace;; 0 = none.
- **EX012 — secrets module.** Why must test card identifiers use secrets instead of random? *Rubric:* 3 = secrets uses the OS secure source; random is predictable;; 2 = secure source;; 1 = no difference;; 0 = none.

### Synthesis

Early programs teach security when they validate inputs, keep error details internal and rely on vetted library functions.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write architecture decision records; (2) draw diagrams others can review; (3) explain security trade-offs to non-specialists.

### 5.1 Decision records

Daniel introduces the architecture decision record, a short document stating the context, the decision, the options considered, the consequences and the date. Sofia writes one for a simple choice: whether fare validators should store a full deny list of blocked cards or query the server each time. The record explains the options, chooses local deny lists with hourly updates for offline resilience and states the consequence that a newly blocked card may work for up to an hour. Decision records let future engineers understand why a design looks the way it does instead of guessing or repeating old debates.

### 5.2 Reviewable diagrams

Sofia learns that a diagram is for review, not decoration. A good data-flow diagram shows processes, data stores, external entities, data flows and trust boundaries, the notation Shostack (2014) uses for threat modelling. Every arrow is labelled with what flows and over what protocol. Every boundary is drawn where trust changes, such as between a bus and the depot network. She redraws a cluttered vendor diagram into a clean one with a legend and a version number. Reviewers can then point to exactly the element they question, which makes reviews faster and more precise.

### 5.3 Explaining trade-offs

Corvia's finance director asks why the fare system cannot block stolen cards instantly. Sofia writes a half-page explanation without jargon: validators work offline on vehicles, they update their lists every hour, and instant blocking would require constant connectivity that buses do not have. She states the risk, a stolen card used for at most an hour, and the cost of reducing it. Daniel praises the explanation because it states the trade-off plainly and lets the director decide whether more frequent updates are worth the extra data costs, rather than hiding the decision inside technical language.

### Worked example

Sofia writes a decision record on deny lists, redraws a vendor diagram with labelled flows and boundaries and explains the one-hour blocking window to the finance director.

> **Synthetic case.** Decisions, diagrams and the director are synthetic; Shostack (2014) is real.

### Errors and limits

Decision records go stale if not updated when decisions change. Plain explanations can omit edge cases that matter.

### Exercises

- **EX013 — ADR fields.** List the fields of an architecture decision record. *Rubric:* 3 = context, decision, options, consequences, date;; 2 = four;; 1 = two;; 0 = none.
- **EX014 — Boundary placement.** Where should a trust boundary be drawn in a data-flow diagram? *Rubric:* 3 = where trust changes, such as between a bus and the depot network;; 2 = trust change;; 1 = anywhere;; 0 = none.
- **EX015 — Blocking window.** What risk did Sofia state to the finance director? *Rubric:* 3 = a stolen card may be used for up to an hour;; 2 = one hour;; 1 = vague;; 0 = none.

### Synthesis

Clear records, reviewable diagrams and plain trade-off explanations make security decisions visible and accountable.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use integrals to accumulate rates over time; (2) estimate exposure windows from changing rates; (3) apply series approximations to reason about repeated small risks.

### 6.1 Accumulating rates

Calculus II introduces integration: summing a rate over time to get a total. Daniel gives Sofia a synthetic curve of fraudulent tap attempts per hour across a day, rising at rush hour and falling at night. The total number of attempts is the area under the curve. She approximates the integral with the trapezoid rule using hourly samples. Integration appears whenever a security quantity is a rate: bytes per second of exfiltration, failed logins per minute or exposure per day. Totals, not peaks alone, often determine the business impact that architects must explain.

### 6.2 Exposure windows

Corvia's deny lists update hourly, so a stolen card remains usable until the next update. If thefts happen at a varying rate through the day, the expected misuse depends on the rate integrated over each exposure window. Sofia computes expected misuse for hourly and quarter-hourly updates by integrating the synthetic theft-use rate multiplied by the average remaining window. The lab below compares the two update intervals. Quarter-hourly updates cut expected misuse substantially, and the result gives the finance director a number to weigh against the data cost discussed in chapter 5.

### Lab — Exposure under two update intervals

```python
# Expected misuse of stolen cards before deny-list update; synthetic hourly theft-use rate.
rate = [0.2]*6 + [1.5, 3.0, 2.5, 1.0, 0.8, 0.9, 1.2, 0.9, 0.8, 1.0, 2.0, 3.2, 2.6, 1.1, 0.6, 0.4] + [0.2]*2
assert len(rate) == 24
def misuse(update_h):          # each use happens on average update_h/2 hours before the list catches up
    return sum(r * update_h / 2 for r in rate) * 1.0
print(f"daily theft-use events: {sum(rate):.1f}")
for h in (1.0, 0.25):
    print(f"update every {h*60:.0f} min -> expected misuse {misuse(h):.1f} uses/day")
import math
p, n = 0.001, 800
print(f"P(at least one error) exact {1 - (1 - p)**n:.2f}, n*p approx {n*p:.2f}")
```

Run with `python3 lab_exposure.py`. Verified output:

```text
daily theft-use events: 25.1
update every 60 min -> expected misuse 12.6 uses/day
update every 15 min -> expected misuse 3.1 uses/day
P(at least one error) exact 0.55, n*p approx 0.80
```

### 6.3 Series and repeated small risks

Small risks repeated many times add up. If each of many independent fare validators has a small probability p of a configuration error in a month, the probability that at least one has an error is 1 minus (1 minus p) to the power n. For small p, a series approximation gives roughly n times p, which is easy to compute mentally. Sofia uses this to show that a one-in-a-thousand error rate across eight hundred validators means a high chance of at least one error each month, an argument for automated configuration checking rather than hoping each device is right.

### Worked example

Sofia integrates a synthetic fraud-rate curve, compares expected misuse under hourly and quarter-hourly updates and uses a series approximation to argue for automated validator checks.

> **Synthetic case.** Rates, validator counts and costs are synthetic.

### Errors and limits

Integrals of estimated rates inherit the estimates' errors. The n times p approximation breaks down when n times p is not small.

### Exercises

- **EX016 — Area meaning.** What does the area under the fraud-attempt curve represent? *Rubric:* 3 = the total number of attempts over the day;; 2 = total;; 1 = peak;; 0 = none.
- **EX017 — Update comparison.** According to the lab, how does expected misuse change from hourly to quarter-hourly updates? *Rubric:* 3 = falls to about a quarter, from 12.6 to 3.1 uses;; 2 = falls;; 1 = rises;; 0 = none.
- **EX018 — At least one error.** With p = 0.001 and n = 800, what is the approximate chance of at least one error? *Rubric:* 3 = about 0.55 (exact) or 0.8 by n p, which overestimates here;; 2 = approx;; 1 = 0.001;; 0 = none.

### Synthesis

Integration and series turn rates and repeated small risks into totals that justify architecture choices.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) apply conditional probability to security alerts; (2) explain the base-rate problem for detection; (3) summarise security data with appropriate statistics.

### 7.1 Conditional probability

Corvia's fraud detector flags suspicious taps. Its vendor states that it detects ninety-five per cent of fraudulent taps and wrongly flags only one per cent of legitimate ones. Sofia learns to ask a different question: given that a tap is flagged, how likely is it to be fraud? That is a conditional probability, and Bayes' theorem connects it to the detector's rates and to the base rate, the share of all taps that are fraudulent. Architects need this reasoning because they decide how alerts flow to analysts and whether automatic blocking is safe.

### 7.2 The base-rate problem

Fraud is rare: in Corvia's synthetic data, about one tap in two thousand. Sofia computes the probability that a flagged tap is fraud. The lab below shows it is under five per cent: most flags are false alarms, despite the detector's impressive-sounding rates. Automatically blocking every flagged card would therefore inconvenience many honest passengers. This is the base-rate problem, and it affects intrusion detection everywhere. Sofia recommends that flags feed a review queue and that only combinations of signals trigger blocking, a design decision that follows directly from the arithmetic.

### Lab — Base rates and alert precision

```python
# P(fraud | flag) via Bayes with synthetic rates.
base, tpr, fpr = 1/2000, 0.95, 0.01
taps = 1_000_000
fraud = taps * base; legit = taps - fraud
tp, fp = fraud * tpr, legit * fpr
print(f"taps {taps:,}: fraud {fraud:.0f}, flagged true {tp:.0f}, flagged false {fp:.0f}")
print(f"P(fraud | flag) = {tp / (tp + fp):.3f}")
```

Run with `python3 lab_bayes.py`. Verified output:

```text
taps 1,000,000: fraud 500, flagged true 475, flagged false 9995
P(fraud | flag) = 0.045
```

### 7.3 Summarising data well

Sofia also learns to summarise. Response times for fraud reviews are skewed: most are quick, a few take days. The mean is pulled up by the slow cases, so she reports the median and the ninetieth percentile alongside it. When comparing two months, she reports counts with their denominators, not just percentages, so readers can see how much data lies behind each figure. Daniel warns that many security dashboards show averages of skewed data and percentage changes on tiny numbers, both of which mislead decision makers about what is actually happening.

### Worked example

Sofia applies Bayes' theorem to vendor rates, shows most flags are false alarms at a one-in-two-thousand base rate, and redesigns the alert flow with a review queue.

> **Synthetic case.** Detector rates and fraud data are synthetic.

### Errors and limits

Vendor rates measured on other data may not hold at Corvia. Independence assumptions between signals are often false.

### Exercises

- **EX019 — Question reversal.** Which probability matters to an analyst looking at a flagged tap? *Rubric:* 3 = probability of fraud given a flag;; 2 = conditional;; 1 = detection rate;; 0 = none.
- **EX020 — Lab precision.** What share of flagged taps were fraud in the lab? *Rubric:* 3 = about 4.5 per cent;; 2 = under five per cent;; 1 = 95 per cent;; 0 = none.
- **EX021 — Skewed summary.** Why report the median and 90th percentile for review times? *Rubric:* 3 = data are skewed and the mean is pulled up by slow cases;; 2 = skew;; 1 = mean only;; 0 = none.

### Synthesis

Probability reasoning about base rates turns impressive detector claims into realistic alert designs.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) describe CPU, memory and storage layers relevant to security; (2) explain privilege rings and memory protection; (3) explain hardware roots of trust and secure boot.

### 8.1 Layers of a computer

Sofia studies how processors, caches, main memory and storage work together. Daniel connects each layer to security. Caches speed up memory access but timing differences between cached and uncached data have enabled side-channel attacks such as those Anderson (2020) discusses. Main memory holds keys and secrets while programs run, so physical access or bugs can expose them. Storage keeps data at rest, which is why fare-system servers encrypt disks. Understanding layers helps an architect ask where a secret lives at each moment and which component must be trusted to protect it there.

### 8.2 Privilege and memory protection

Processors provide privilege levels: the operating system kernel runs with high privilege, applications with lower privilege. The memory management unit gives each process its own address space, so one program cannot read another's memory without permission. These hardware mechanisms implement complete mediation and least privilege at the lowest level. When a bug lets a program cross these boundaries, the whole system's guarantees fail. Sofia sees why virtual machines and containers depend on hardware features, and why kernel vulnerabilities are treated as critical: they undermine the boundaries every other control relies on.

### 8.3 Roots of trust and secure boot

A device must start from something it trusts. A hardware root of trust, such as a boot ROM and a key fused into the chip, verifies the signature of the first software loaded, which verifies the next stage, and so on: this is secure boot. Corvia's fare validators use it so that tampered firmware will not run. NIST SP 800-160 Vol. 1 Rev. 1 treats such mechanisms as part of engineering trustworthiness across the life cycle. Sofia notes the operational side: signing keys for firmware must be protected, because whoever holds them can make any firmware trusted.

### Worked example

Sofia traces where a fare validator's key lives across storage, memory and cache, and explains secure boot from boot ROM to application.

> **Synthetic case.** Device details are synthetic; Anderson (2020) and SP 800-160 Vol. 1 Rev. 1 are real.

### Errors and limits

Hardware protections have had flaws requiring microcode and design fixes. Secure boot does not protect against bugs in correctly signed software.

### Exercises

- **EX022 — Cache timing.** Why can caches create security problems? *Rubric:* 3 = timing differences between cached and uncached access can leak information;; 2 = timing;; 1 = vague;; 0 = none.
- **EX023 — Kernel bug severity.** Why are kernel vulnerabilities treated as critical? *Rubric:* 3 = they break the privilege and memory boundaries other controls rely on;; 2 = boundaries;; 1 = minor;; 0 = none.
- **EX024 — Signing key risk.** Why must firmware signing keys be protected? *Rubric:* 3 = whoever holds them can make any firmware trusted by secure boot;; 2 = trusted firmware;; 1 = not important;; 0 = none.

### Synthesis

Hardware layers, privilege mechanisms and roots of trust form the base on which every higher security control stands.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure programs into modules with clear interfaces; (2) write tests including negative tests for security behaviour; (3) manage dependencies safely.

### 9.1 Modules and interfaces

In Programming II Sofia builds a small fare-rules engine as several modules: parsing, tariff lookup, discount rules and output. Each module exposes a narrow interface and hides its internals. Daniel explains why this matters for security: narrow interfaces are easier to review, and a module that receives only validated data from the parser need not repeat every check. This is economy of mechanism at the code level. When the discount module later needs a change, Sofia can review only its interface and tests rather than the whole program, which reduces the chance of introducing a flaw elsewhere.

### 9.2 Negative tests

Sofia writes unit tests for normal fares, then Daniel asks for negative tests: inputs that must be rejected. A child discount must not apply to an adult card; a tariff zone outside the network must raise an error; an amount with more than two decimal places must be refused. Security bugs often live in what a program wrongly accepts, so tests should show that bad inputs fail. She runs the tests automatically on every change. Negative tests also document intent: a later developer can see that rejecting those inputs was deliberate and not an accident to be removed.

### 9.3 Dependencies

Sofia's program uses a third-party package to read configuration files. Daniel shows her how to pin its version, record where it came from and check for published advisories. NIST SP 800-218, the Secure Software Development Framework, recommends practices such as tracking components and responding to vulnerabilities in them. A dependency is code someone else wrote that runs with your program's privileges. Sofia learns to prefer the standard library where it suffices, choose well-maintained packages otherwise and review how much code each new dependency brings, since every line is part of the system's attack surface.

### Worked example

Sofia modularises a fare-rules engine, adds three negative tests that must fail safely and pins and records one dependency per SP 800-218 practices.

> **Synthetic case.** The engine and package are synthetic; SP 800-218 is real.

### Errors and limits

Tests show presence of checks, not absence of all bugs. Pinned dependencies still need updates when advisories appear.

### Exercises

- **EX025 — Narrow interface benefit.** How do narrow module interfaces help security review? *Rubric:* 3 = less to review and validated data need not be rechecked everywhere;; 2 = review;; 1 = vague;; 0 = none.
- **EX026 — Negative test example.** Give one negative test from Sofia's engine. *Rubric:* 3 = child discount on adult card rejected, out-of-network zone error or three-decimal amount refused;; 2 = one;; 1 = positive test;; 0 = none.
- **EX027 — Dependency practice.** What does SP 800-218 recommend about third-party components? *Rubric:* 3 = track them and respond to vulnerabilities in them;; 2 = track;; 1 = ignore;; 0 = none.

### Synthesis

Modular design, negative tests and managed dependencies make programs easier to trust and to keep trustworthy.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering codes of ethics to security decisions; (2) recognise public-safety dimensions of transit systems; (3) handle conflicts between schedules and safety.

### 10.1 Duties of an engineer

Professional engineering codes generally place public safety, health and welfare above employer or client interests, and require honesty about limits of competence. Daniel asks Sofia to read her national engineering body's code and to apply it to security work. Hiding a known weakness to meet a launch date conflicts with the duty of honesty. Claiming expertise in an area she has not studied conflicts with competence limits. Security engineers face these dilemmas regularly, and ethics provides a framework for deciding before pressure arrives, rather than improvising when a manager asks for silence.

### 10.2 Safety in transit systems

Transit systems carry people, so security failures can become safety failures. If an attacker disrupts passenger information screens during an emergency, people may go to the wrong platform. If fare gates fail closed during an evacuation, they could trap passengers. Sofia learns that fail-safe defaults from Saltzer and Schroeder (1975) must be interpreted with care: for access to data, deny by default; for physical gates during fire alarms, open by default. Security architecture in transit must be coordinated with safety engineers, who often have regulatory duties and their own analysis methods.

### 10.3 Schedule versus safety

During Sofia's placement, a contractor wants to switch on a new passenger app feature before its security review is complete, because of a press launch. Sofia, as a student, cannot approve or block it, but she can raise her concern in writing to Daniel with the specific risk: the feature exposes journey histories through an unauthenticated interface in the test build. Daniel escalates, and the feature launches a week later after a fix. The lesson is that ethics often means making a risk visible to the right person in writing, clearly and promptly.

### Worked example

Sofia maps her engineering code to three security dilemmas, distinguishes data and physical fail-safe defaults and writes a concise risk note that delays an unsafe launch.

> **Synthetic case.** The launch, contractor and app feature are synthetic; Saltzer and Schroeder (1975) is real.

### Errors and limits

Codes of ethics vary by country and body. Raising a concern does not guarantee action; escalation paths must exist.

### Exercises

- **EX028 — Paramount duty.** What do engineering codes place above employer interests? *Rubric:* 3 = public safety, health and welfare;; 2 = safety;; 1 = profit;; 0 = none.
- **EX029 — Gate default.** During a fire alarm, should fare gates fail open or closed, and why? *Rubric:* 3 = open, so passengers can evacuate; safety overrides fare protection;; 2 = open;; 1 = closed;; 0 = none.
- **EX030 — Student action.** What could Sofia do about the premature launch? *Rubric:* 3 = raise the specific risk in writing to Daniel for escalation;; 2 = written concern;; 1 = nothing;; 0 = none.

### Synthesis

Ethical engineering puts public safety first, adapts defaults to safety context and makes risks visible in writing.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) map Corvia's network zones and protocols; (2) explain what TLS, VPNs and segmentation protect; (3) identify architectural weaknesses in a flat network.

### 11.1 Mapping zones

Sofia draws Corvia's network: buses and trams connect over cellular links to a depot gateway; depots connect to the central data centre; the passenger app and website sit in a cloud environment; corporate offices have their own network. Each zone has different users, devices and threats. She lists the protocols crossing each boundary, such as HTTPS for the app, a VPN from vehicles to depots and a vendor's proprietary protocol for fare validators. A map like this is the starting point for every architecture review, because protections must be placed where traffic crosses trust boundaries.

### 11.2 What protocols protect

TLS, specified in RFC 8446, protects data in transit between two endpoints with encryption, integrity and server authentication. A VPN creates an encrypted tunnel between networks, so vehicle traffic crossing public cellular networks is protected. Neither controls what happens inside an endpoint or which internal systems a connected device may reach. Segmentation does that, by limiting which zones can talk to which. Sofia notes that a VPN which drops every bus straight into the central network without filtering would protect confidentiality on the cellular link but give a compromised bus a path to everything.

### 11.3 Weaknesses of flat networks

In Corvia's older depot, staff laptops, fare servers and printers share one network segment. Sofia explains the risk to Daniel: one infected laptop can reach fare servers directly, and monitoring cannot easily tell normal from abnormal traffic when everything talks to everything. Anderson (2020) describes incidents where flat internal networks let attackers move freely. She proposes separating zones with firewalls and allowing only required flows, the approach later formalised in zero trust guidance such as SP 800-207, and lists the flows each zone legitimately needs as the basis for rules.

### Worked example

Sofia maps six Corvia zones and their boundary protocols, explains the limits of VPN tunnels and proposes segmenting the flat depot network by required flows.

> **Synthetic case.** Zones and flows are synthetic; RFC 8446, SP 800-207 and Anderson (2020) are real.

### Errors and limits

Network maps go stale quickly. Segmentation rules must be maintained or they drift back toward flat.

### Exercises

- **EX031 — VPN limit.** What does a vehicle VPN not control? *Rubric:* 3 = which internal systems the connected device can reach;; 2 = reach;; 1 = confidentiality;; 0 = none.
- **EX032 — Flat depot risk.** Name two problems with the flat depot network. *Rubric:* 3 = infected laptop reaches fare servers; monitoring cannot separate normal from abnormal;; 2 = two;; 1 = one;; 0 = none.
- **EX033 — Rule basis.** What should segmentation rules be based on? *Rubric:* 3 = the flows each zone legitimately needs;; 2 = required flows;; 1 = all flows;; 0 = none.

### Synthesis

Network architecture places protocols and segmentation where traffic crosses trust boundaries, not only where it crosses the internet.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) explain process isolation, users and permissions; (2) harden a server baseline; (3) relate OS logging to architecture-level detection.

### 12.1 Isolation and permissions

Operating systems isolate processes and control access to files through users, groups and permissions. Sofia studies a Linux fare server: the fare service runs as its own account, which can read its configuration and write its logs but cannot modify system files. Administrators use separate accounts with elevated rights only when needed. These are least privilege applied to the operating system. She finds one legacy script running as root for convenience, and Daniel explains that a single compromised root process undermines every other permission, so the script is rewritten to run under a restricted account.

### 12.2 Baseline hardening

Corvia uses a hardening baseline for servers: disable unused services, remove default accounts, apply updates on a schedule, enforce strong authentication for administrators and enable host firewalls. SP 800-53 Rev. 5 control families such as configuration management and system and information integrity describe these expectations. Sofia applies the baseline to a lab server and records each change. She learns that hardening reduces attack surface but that a baseline is only useful if deviations are detected, so she also schedules a configuration check that reports drift from the baseline each week.

### 12.3 Logging for detection

Operating systems log logins, privilege changes, process starts and service failures. An architect decides which of these logs are collected centrally, how long they are kept and who can alter them. Sofia configures her lab server to send authentication and privilege logs to a central collector that administrators of the server cannot modify, so an intruder with server access cannot erase evidence. She documents which events are collected and why. Logging design is an architecture decision, because it determines whether attacks can be noticed and investigated at all.

### Worked example

Sofia removes a root-running script, applies and records a hardening baseline with weekly drift checks and sends tamper-resistant logs to a central collector.

> **Synthetic case.** Servers, scripts and baseline settings are synthetic; SP 800-53 Rev. 5 is real.

### Errors and limits

Baselines can break legacy software; test before rollout. Central logs can be overwhelmed without filtering.

### Exercises

- **EX034 — Root script danger.** Why was the root-running script rewritten? *Rubric:* 3 = a compromised root process undermines all other permissions;; 2 = root risk;; 1 = style;; 0 = none.
- **EX035 — Drift checks.** Why schedule weekly configuration checks after hardening? *Rubric:* 3 = to detect deviations from the baseline over time;; 2 = drift;; 1 = not needed;; 0 = none.
- **EX036 — Log immutability.** Why send logs to a collector the server's admins cannot modify? *Rubric:* 3 = an intruder on the server cannot erase evidence;; 2 = evidence;; 1 = speed;; 0 = none.

### Synthesis

Operating-system isolation, hardened baselines and protected logs provide the host-level foundation of security architecture.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) classify data in a transit organisation; (2) prevent injection with parameterised queries; (3) design data retention and minimisation.

### 13.1 Classifying data

Corvia holds several kinds of data: card identifiers and journey histories, payment tokens, staff records, timetable data and vehicle telemetry. Sofia helps classify them. Journey histories are personal data revealing where people live and work; payment tokens are sensitive financial data; timetables are public. Classification drives architecture: personal and payment data need encryption, access controls and logging, while public data needs integrity but not confidentiality. Daniel stresses that classification must be done before design, because retrofitting protection to a database full of mixed data is expensive and often incomplete.

### 13.2 Parameterised queries

Sofia writes a query to look up journeys by card identifier. Her first version builds the SQL string by concatenating user input. Daniel shows her that input such as a quote followed by OR 1=1 changes the query's meaning and returns every journey, an injection attack. The fix is a parameterised query, where the database driver passes the input as data, never as code. The lab below demonstrates both with Python's built-in sqlite3 module on a synthetic table. The concatenated query leaks all rows; the parameterised one returns none for the malicious input.

### Lab — Concatenated versus parameterised query

```python
# Injection vs parameterised query with stdlib sqlite3 on a synthetic table.
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE journeys (card TEXT, stop TEXT)")
db.executemany("INSERT INTO journeys VALUES (?, ?)", [("C100", "Harbour"), ("C100", "Market"), ("C200", "Depot"), ("C300", "Airport")])
evil = "X' OR '1'='1"
rows_bad = db.execute(f"SELECT * FROM journeys WHERE card = '{evil}'").fetchall()   # never do this
rows_ok = db.execute("SELECT * FROM journeys WHERE card = ?", (evil,)).fetchall()
print("concatenated query rows:", len(rows_bad))
print("parameterised query rows:", len(rows_ok))
print("legit lookup C100:", len(db.execute("SELECT * FROM journeys WHERE card = ?", ("C100",)).fetchall()))
```

Run with `python3 lab_sqli.py`. Verified output:

```text
concatenated query rows: 4
parameterised query rows: 0
legit lookup C100: 2
```

### 13.3 Retention and minimisation

Storing data forever increases the damage of any breach. Sofia proposes a retention design: detailed journey histories kept for ninety days for customer service and fraud investigation, then aggregated into anonymous counts for planning. Payment tokens are kept only as long as the payment provider requires. ISO/IEC 27002:2022 includes controls on information deletion and data masking. She documents each retention period with its purpose. Minimisation is an architectural control: data that is not stored cannot be stolen, and a smaller data set is easier to protect well.

### Worked example

Sofia classifies five Corvia data types, demonstrates injection and its fix in sqlite3 and proposes a ninety-day retention design for journey histories.

> **Synthetic case.** Data, tables and retention periods are synthetic; ISO/IEC 27002:2022 is real.

### Errors and limits

Aggregation can still allow re-identification in small groups. Retention rules depend on law and must be checked with counsel.

### Exercises

- **EX037 — Journey sensitivity.** Why are journey histories personal data needing protection? *Rubric:* 3 = they reveal where people live, work and travel;; 2 = location;; 1 = public;; 0 = none.
- **EX038 — Lab injection result.** What did the lab return for the malicious input under each query style? *Rubric:* 3 = concatenated returned all 4 rows; parameterised returned 0;; 2 = both;; 1 = same;; 0 = none.
- **EX039 — Minimisation logic.** Why is data minimisation a security control? *Rubric:* 3 = data not stored cannot be stolen and smaller sets are easier to protect;; 2 = not stolen;; 1 = not a control;; 0 = none.

### Synthesis

Data architecture classifies before designing, keeps input as data, and stores only what is needed for as long as needed.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) integrate security activities into a development life cycle; (2) run a lightweight design review; (3) use code review and automated checks effectively.

### 14.1 Security in the life cycle

Sofia joins a Corvia team building a new fare-refund service for a semester. Their life cycle has requirements, design, implementation, testing, release and maintenance. Daniel shows her where security fits: abuse cases alongside requirements, threat modelling at design, secure coding and review during implementation, security tests before release and vulnerability response afterwards. NIST SP 800-218 organises such practices into groups for preparing the organisation, protecting software, producing well-secured software and responding to vulnerabilities. Integrating security into each phase costs less than trying to add it at the end.

### 14.2 Lightweight design review

Before coding starts, the team holds a one-hour design review. They draw a data-flow diagram of the refund service, mark trust boundaries and walk each element through STRIDE categories as Shostack (2014) describes. They find that refund requests could be replayed to obtain double refunds, and that support staff could approve their own refund requests. Mitigations are recorded: unique request identifiers checked server-side, and a rule that approvers must differ from requesters. Sofia notes that one hour found two serious issues that would have been costly to fix after release.

### 14.3 Reviews and automation

During implementation, every change is reviewed by another engineer using a short checklist: input validation, authorisation checks, error handling and logging. Automated checks run static analysis and dependency scanning on each commit. Sofia learns that tools catch common patterns but miss design flaws such as the self-approval issue, while humans tire of repetitive checks that tools do well. Combining them is efficient. The team tracks findings to closure and reviews any finding the tools missed to improve the checklist, a feedback loop that improves the process itself.

### Worked example

Sofia maps SP 800-218 practice groups to the refund project, takes part in a STRIDE review finding replay and self-approval issues and helps refine the review checklist.

> **Synthetic case.** The refund service and findings are synthetic; SP 800-218 and Shostack (2014) are real.

### Errors and limits

Lightweight reviews miss issues outside the diagram. Tools produce false positives that teams learn to ignore if not tuned.

### Exercises

- **EX040 — SP 800-218 groups.** Name the four practice groups of SP 800-218. *Rubric:* 3 = prepare the organisation, protect software, produce well-secured software, respond to vulnerabilities;; 2 = three;; 1 = one;; 0 = none.
- **EX041 — Refund findings.** Which two issues did the design review find? *Rubric:* 3 = replayed refund requests and self-approval by support staff;; 2 = both;; 1 = one;; 0 = none.
- **EX042 — Tools versus humans.** What kind of flaw do tools typically miss? *Rubric:* 3 = design flaws such as self-approval logic;; 2 = design flaws;; 1 = syntax;; 0 = none.

### Synthesis

Security fits every life-cycle phase, with short design reviews and combined human and automated checks catching different flaws.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) define assets, threats, vulnerabilities and risk; (2) apply the Saltzer and Schroeder principles to a design; (3) distinguish preventive, detective and corrective controls.

### 15.1 Core vocabulary

Sofia's security fundamentals course gives precise words. An asset is something of value, such as the fare database. A threat is a potential cause of harm, such as a fraud group. A vulnerability is a weakness a threat could exploit, such as an unauthenticated interface. Risk combines the likelihood that a threat exploits a vulnerability with the impact on the asset; NIST SP 800-30 Rev. 1 describes how to assess it. Using these words carefully avoids confused debates in which one person talks about attackers and another about bugs, each thinking they mean the same thing.

### 15.2 Design principles in use

Sofia applies Saltzer and Schroeder's principles to the refund service from chapter 14. Least privilege: support staff can view refunds but only supervisors can approve large ones. Fail-safe defaults: if the authorisation service is unreachable, refunds are refused, not approved. Complete mediation: every refund request is checked, not only the first in a session. Open design: security does not depend on hiding how the service works. Psychological acceptability: approval screens are simple enough that supervisors do not look for shortcuts. Writing each principle beside a concrete design choice makes abstract ideas useful in review.

### 15.3 Kinds of controls

Controls can prevent, detect or correct. Authentication and authorisation prevent unauthorised refunds. Logging and monitoring detect suspicious patterns, such as one card receiving many refunds. Corrective controls restore normal operation, such as reversing fraudulent refunds and revoking compromised accounts. Sofia learns that no preventive control is perfect, so every important asset needs detection and correction too. ISO/IEC 27002:2022 groups controls into organisational, people, physical and technological themes, a different view that helps check whether non-technical controls such as training and procedures have been considered.

### Worked example

Sofia defines asset, threat, vulnerability and risk for the refund service, maps five design principles to concrete choices and lists preventive, detective and corrective controls.

> **Synthetic case.** The refund service and controls are synthetic; SP 800-30 Rev. 1, Saltzer and Schroeder (1975) and ISO/IEC 27002:2022 are real.

### Errors and limits

Vocabulary varies between standards; define terms in each document. Principles can conflict and require judgement.

### Exercises

- **EX043 — Vulnerability versus threat.** Give a Corvia example of a threat and of a vulnerability. *Rubric:* 3 = threat: fraud group; vulnerability: unauthenticated interface;; 2 = both;; 1 = swapped;; 0 = none.
- **EX044 — Fail-safe refund.** How does fail-safe default apply when the authorisation service is down? *Rubric:* 3 = refunds are refused, not approved;; 2 = refuse;; 1 = approve;; 0 = none.
- **EX045 — ISO themes.** What four themes does ISO/IEC 27002:2022 use to group controls? *Rubric:* 3 = organisational, people, physical, technological;; 2 = three;; 1 = one;; 0 = none.

### Synthesis

Precise vocabulary, explicit principles and balanced control types form the fundamentals every architecture decision uses.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) describe the systems-engineering life cycle; (2) apply NIST SP 800-160 Vol. 1 Rev. 1 concepts to a transit system; (3) build traceability from needs to verification.

### 16.1 The life cycle

Systems engineering manages complex systems from concept to retirement. Daniel explains that a fare system involves hardware on vehicles, software in data centres, cloud services, people and contracts, so it must be engineered as a whole. Life-cycle stages include concept, development, production, utilisation, support and retirement. Security concerns arise in each: requirements in concept, design reviews in development, secure manufacturing in production, monitoring in utilisation, patching in support and data destruction at retirement. Sofia realises that many security failures she has read about happened in support or retirement, stages that projects often neglect.

### 16.2 Engineering trustworthiness

NIST SP 800-160 Vol. 1 Rev. 1 treats security as part of system trustworthiness and integrates it into systems-engineering processes. It emphasises stakeholder protection needs, security requirements derived from them, architecture and design that satisfy those requirements, and assurance that the system actually does so. It also lists design principles, extending Saltzer and Schroeder with ideas such as least persistence and continuous protection. Sofia uses the publication to structure a short paper on the fare validator, linking passenger protection needs to requirements such as tamper evidence and protected keys.

### 16.3 Traceability

Traceability links each stakeholder need to requirements, design elements and verification evidence. Sofia builds a small traceability table: the need that passengers' journey data stays private links to requirements for encryption in transit and at rest, which link to design elements such as TLS and disk encryption, which link to tests and configuration checks. When a test fails or a requirement changes, traceability shows what else is affected. Without it, teams cannot tell whether every need has been met or which design element exists for which reason.

### Worked example

Sofia maps security concerns to six life-cycle stages, structures a validator paper with SP 800-160 Vol. 1 Rev. 1 concepts and builds a needs-to-tests traceability table.

> **Synthetic case.** The validator paper and table are synthetic; SP 800-160 Vol. 1 Rev. 1 is real.

### Errors and limits

Traceability tables become burdensome if too detailed. Life-cycle models are simplifications of iterative real projects.

### Exercises

- **EX046 — Neglected stages.** Which life-cycle stages are often neglected for security? *Rubric:* 3 = support and retirement;; 2 = both;; 1 = development;; 0 = none.
- **EX047 — SP 800-160 flow.** What chain does SP 800-160 Vol. 1 Rev. 1 emphasise? *Rubric:* 3 = protection needs to requirements to design to assurance;; 2 = chain;; 1 = vague;; 0 = none.
- **EX048 — Traceability value.** What does traceability show when a requirement changes? *Rubric:* 3 = which design elements and tests are affected;; 2 = affected items;; 1 = nothing;; 0 = none.

### Synthesis

Systems engineering spreads security across the whole life cycle and keeps needs, designs and evidence linked.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) describe feedback loops in security operations; (2) simulate an adaptive rate limiter; (3) recognise oscillation and lag in control systems.

### 17.1 Feedback in security

A feedback loop measures an output, compares it with a target and adjusts an input. Sofia finds feedback throughout security operations: a rate limiter that tightens when failed logins rise, an autoscaler that adds capacity during a traffic flood, and an organisation that adjusts controls after incidents. Control theory, which she studies for engineering, gives tools to reason about whether such loops settle smoothly, react too slowly or overreact. Daniel notes that badly tuned security automation can cause outages, which attackers may exploit deliberately by triggering it.

### 17.2 Simulating a rate limiter

The passenger app's login service uses an adaptive rate limiter: if failed logins in a minute exceed a target, the allowed request rate is reduced; if they fall below, it is relaxed. Sofia simulates this with synthetic attack traffic arriving at minute five and stopping at minute fifteen. With a proportional gain that is too high, the allowed rate swings up and down, alternately blocking legitimate users and letting attacks through. With a moderate gain, it settles. The lab below prints both runs so she can see the difference rather than just reading about it.

### Lab — Adaptive rate limiter gains

```python
# Adaptive rate limiter (proportional control) on synthetic failed-login traffic.
def run(gain, minutes=24, target=50):
    allowed, out = 200.0, []
    for t in range(minutes):
        attack = 400 if 5 <= t < 15 else 0
        failures = min(allowed, 40 + attack) * (0.9 if attack else 0.3)
        allowed = max(20.0, min(400.0, allowed - gain * (failures - target)))
        out.append(round(allowed))
    return out
for g in (2.5, 0.6):
    r = run(g)
    swings = sum(1 for a, b, c in zip(r, r[1:], r[2:]) if (b - a) * (c - b) < 0)
    print(f"gain {g}: allowed/min = {r}")
    print(f"  direction changes: {swings}")
```

Run with `python3 lab_feedback.py`. Verified output:

```text
gain 2.5: allowed/min = [295, 390, 400, 400, 400, 20, 100, 20, 100, 20, 100, 20, 100, 20, 100, 195, 290, 385, 400, 400, 400, 400, 400, 400]
  direction changes: 9
gain 0.6: allowed/min = [223, 246, 268, 291, 314, 174, 110, 81, 67, 61, 58, 57, 56, 56, 56, 78, 101, 124, 147, 170, 192, 215, 238, 261]
  direction changes: 1
```

### 17.3 Lag and oscillation

Two problems recur in feedback systems: lag, where the response arrives too late, and oscillation, where the response overshoots repeatedly. A rate limiter measuring over long windows lags behind sudden attacks; one reacting to every second may oscillate. Sofia relates this to incident response: an organisation that changes policy only once a year lags, while one that reverses decisions weekly oscillates and confuses staff. She proposes that automated controls have bounded adjustment sizes, minimum and maximum limits and human review when limits are reached, to keep feedback stable.

### Worked example

Sofia simulates an adaptive rate limiter with two gains, shows oscillation at high gain and proposes bounded, reviewed automatic adjustments.

> **Synthetic case.** Traffic and limiter parameters are synthetic.

### Errors and limits

Simple proportional models ignore attacker adaptation. Simulation results depend on assumed traffic shapes.

### Exercises

- **EX049 — Automation exploit.** How might attackers exploit badly tuned security automation? *Rubric:* 3 = trigger it deliberately to cause outages for legitimate users;; 2 = trigger;; 1 = vague;; 0 = none.
- **EX050 — High gain result.** What happened in the lab with the high gain? *Rubric:* 3 = allowed rate oscillated, swinging between blocking users and admitting attacks;; 2 = oscillated;; 1 = settled;; 0 = none.
- **EX051 — Stabilising proposal.** Name two safeguards Sofia proposes for automated controls. *Rubric:* 3 = bounded adjustments, min and max limits, human review at limits (two);; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Security automation is a feedback system, and it needs tuning and bounds to avoid lag and oscillation.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) describe enterprise security architecture frameworks; (2) build a layered architecture view for Corvia; (3) link business attributes to technical controls.

### 18.1 Frameworks for architecture

Security architecture organises controls into a coherent design rather than a collection of products. SABSA, described by Sherwood, Clark and Lynas (2005), starts from business requirements expressed as attributes, such as available, private or auditable, and traces them through layers down to physical components and operations. The Open Group's guide on integrating risk and security within TOGAF shows how to bring security into each phase of enterprise architecture development. Sofia learns that frameworks provide vocabulary and structure; their value lies in making assumptions and dependencies visible across teams.

### 18.2 Layered view of Corvia

Sofia builds a simple layered view of the fare system. At the business layer: collect fares accurately, protect passenger privacy, keep services running. At the logical layer: identity services, payment tokenisation, logging and key management. At the physical layer: secure elements in validators, hardware security modules for keys, segmented networks. At the operational layer: monitoring, incident response and patch management. Each control appears in one layer and links to the attribute it supports. The view exposes gaps, such as no operational owner for the key management service.

### 18.3 Attributes to controls

Daniel asks Sofia to trace the attribute passenger privacy downward. At the logical layer it requires minimised data and access control; at the physical layer encrypted storage and segmented networks; at the operational layer access reviews and breach response. Each link is a design claim that can be verified. When a proposed change removes a control, the trace shows which business attribute is weakened. This top-down link is SABSA's central contribution: it keeps security spending tied to what the organisation values rather than to fashionable technologies.

### Worked example

Sofia builds a four-layer architecture view of Corvia's fare system, traces passenger privacy from attribute to operation and finds a missing owner for key management.

> **Synthetic case.** The architecture view and gap are synthetic; SABSA and TOGAF G152 are real.

### Errors and limits

Layered views simplify cross-cutting concerns. Attribute traces can become paperwork if not kept current.

### Exercises

- **EX052 — SABSA starting point.** Where does SABSA start an architecture? *Rubric:* 3 = business requirements expressed as attributes;; 2 = attributes;; 1 = technology;; 0 = none.
- **EX053 — Gap found.** What gap did Sofia's layered view expose? *Rubric:* 3 = no operational owner for key management;; 2 = owner;; 1 = vague;; 0 = none.
- **EX054 — Removing a control.** What does the attribute trace show when a change removes a control? *Rubric:* 3 = which business attribute is weakened;; 2 = attribute;; 1 = nothing;; 0 = none.

### Synthesis

Security architecture links business attributes to controls across layers so gaps and trade-offs become visible.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) design identity flows for staff, passengers and devices; (2) place cryptographic mechanisms in the architecture; (3) plan key management as an architectural service.

### 19.1 Three kinds of identity

Corvia has staff identities in a corporate directory, passenger identities in the app's account system and device identities for validators and vehicles. Each needs a different design. Staff use single sign-on with multi-factor authentication. Passengers use app accounts with optional passkeys, and many travel anonymously with cards. Devices authenticate with certificates issued by Corvia's internal authority and stored in secure elements. Sofia draws all three flows on one diagram and finds that a shared vendor support account bypasses staff single sign-on, an identity gap that undermines the strong design elsewhere.

### 19.2 Placing cryptography

Sofia lists where cryptography protects the system. TLS from RFC 8446 protects app and web traffic. A VPN protects vehicle links. Validators sign tap records so the back office can detect tampering. Payment data is tokenised by the payment provider, so Corvia never stores card numbers. Databases encrypt at rest. Each mechanism serves a specific goal from the classification in chapter 13. She learns that an architect's job is to choose and place standard mechanisms, not to design new ones, and that every mechanism brings key management obligations the architecture must meet.

### 19.3 Key management as a service

Keys need generation, storage, distribution, rotation, revocation and destruction. NIST SP 800-57 Part 1 Rev. 5 gives guidance on these phases and on cryptoperiods. Sofia proposes treating key management as an architectural service with its own owner, hardware security modules for root and signing keys, and documented procedures for each phase. This connects back to the gap found in chapter 18. Daniel agrees, adding that the service must be tested through rotation and recovery exercises, because key management that has never been exercised often fails when it is first needed.

### Worked example

Sofia diagrams staff, passenger and device identities, finds a shared vendor account bypassing single sign-on, lists five placed cryptographic mechanisms and proposes key management as an owned service.

> **Synthetic case.** Identities and mechanisms are synthetic; RFC 8446 and SP 800-57 Part 1 Rev. 5 are real.

### Errors and limits

Passkeys and certificates still depend on recovery processes that can be abused. Hardware security modules add cost and operational complexity.

### Exercises

- **EX055 — Identity gap.** What identity gap did Sofia find? *Rubric:* 3 = a shared vendor support account bypassing staff single sign-on;; 2 = shared account;; 1 = vague;; 0 = none.
- **EX056 — Tokenisation benefit.** Why does tokenisation help Corvia? *Rubric:* 3 = it never stores card numbers, reducing exposure;; 2 = no card numbers;; 1 = vague;; 0 = none.
- **EX057 — Key life cycle.** List four key management phases. *Rubric:* 3 = four of generation, storage, distribution, rotation, revocation, destruction;; 2 = three;; 1 = one;; 0 = none.

### Synthesis

Identity and cryptography are architectural services whose flows, placements and key life cycles must be designed and owned.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Security architecture and engineering: engineering context

### Learning outcomes

You will (1) describe the regulatory, contractual and organisational context of Corvia's architecture; (2) identify stakeholders and constraints; (3) write a context statement for a project.

### 20.1 Regulatory and contractual context

From year three Sofia works on a real-scale project: redesigning Corvia's fare back office. Daniel first asks her to understand the context. Card payments bring obligations from the payment industry; personal data brings privacy law; public funding brings audit requirements; and vendor contracts limit what Corvia can change in validators. She lists each obligation, its source and what it requires architecturally, such as segmentation of payment systems or deletion of personal data on request. Context constrains design before any technical choice is made, so ignoring it leads to designs that cannot be approved.

### 20.2 Stakeholders and constraints

Sofia identifies stakeholders: passengers, fare-collection staff, finance, the data protection officer, the operations centre, validator and payment vendors, auditors and the transit authority board. Each has needs and constraints. Finance needs accurate reconciliation; operations needs systems that work during outages; the data protection officer needs minimisation and access logs; vendors need stable interfaces. Constraints include a fixed budget, a three-year timeline and legacy validators that cannot be replaced until year five. She records each constraint because architecture is the art of meeting needs within constraints, not designing an ideal system.

### 20.3 The context statement

Sofia writes a two-page context statement for the project: purpose, scope, stakeholders, obligations, constraints, assumptions and out-of-scope items. Daniel reviews it with the project board, who correct two assumptions: payment tokenisation is already contracted, and the passenger app is out of scope. Correcting assumptions at this stage costs a meeting; correcting them after design costs months. The context statement becomes the first document in the architecture record and is referenced by every later decision, so reviewers can check whether a design still fits its context.

### Worked example

Sofia lists four sources of obligations, maps eight stakeholders and constraints and writes a context statement corrected by the project board.

> **Synthetic case.** Obligations, stakeholders and board decisions are synthetic.

### Errors and limits

Legal interpretation needs qualified advice. Context changes during long projects and must be revisited.

### Exercises

- **EX058 — Obligation example.** Give one obligation and its architectural effect. *Rubric:* 3 = payment obligations require segmentation of payment systems; privacy requires deletion support;; 2 = one pair;; 1 = vague;; 0 = none.
- **EX059 — Legacy constraint.** Which constraint limits validator changes? *Rubric:* 3 = legacy validators cannot be replaced until year five;; 2 = legacy;; 1 = budget;; 0 = none.
- **EX060 — Corrected assumptions.** Which two assumptions did the board correct? *Rubric:* 3 = tokenisation already contracted; passenger app out of scope;; 2 = both;; 1 = one;; 0 = none.

### Synthesis

Engineering context sets the obligations, stakeholders and constraints that every architecture decision must respect.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Security architecture and engineering: requirements

### Learning outcomes

You will (1) write verifiable security requirements; (2) derive requirements from protection needs and abuse cases; (3) select controls from catalogues with justification.

### 21.1 Verifiable requirements

A requirement such as the system shall be secure cannot be verified. Sofia learns to write requirements that can be tested: refund approvals above fifty euros shall require a second approver distinct from the requester; tap records shall be signed by the validator and rejected by the back office if the signature fails; administrative access shall require multi-factor authentication. Each requirement names who or what, the condition and the expected behaviour. She adds a verification method to each, such as test, inspection or analysis, so that the team knows from the start how compliance will be shown.

### 21.2 Abuse cases

Use cases describe what legitimate users do; abuse cases describe what attackers or careless insiders might do. Sofia writes abuse cases for the back office: a fraudster replays signed tap records to create fake journeys for refund claims; an insider exports journey histories to sell; a compromised vendor account pushes a malicious tariff table. Each abuse case leads to requirements, such as replay detection with unique record identifiers, export logging and approval, and signed tariff tables verified before use. Abuse cases make requirements concrete and help stakeholders understand why each exists.

### 21.3 Selecting controls

NIST SP 800-53 Rev. 5 provides a catalogue of controls; ISO/IEC 27002:2022 provides another. Sofia uses them to check her requirements for gaps rather than copying them wholesale. For example, the catalogue's audit and accountability family reminds her to require log protection and review, which she had missed. For each selected control she records the requirement it supports and the reason. Selecting controls with justification avoids both gaps and bloated designs that implement controls nobody needs, consuming budget that could address real risks.

### Worked example

Sofia writes twelve verifiable requirements with verification methods, three abuse cases with derived requirements and uses SP 800-53 Rev. 5 to find a missing log-review requirement.

> **Synthetic case.** Requirements and abuse cases are synthetic; SP 800-53 Rev. 5 and ISO/IEC 27002:2022 are real.

### Errors and limits

Requirements can conflict, such as logging versus privacy. Catalogues are broad; tailoring requires judgement.

### Exercises

- **EX061 — Verifiable rewrite.** Rewrite the system shall be secure as a verifiable requirement for refunds. *Rubric:* 3 = refunds above 50 euros require a second approver distinct from the requester, verified by test;; 2 = verifiable;; 1 = vague;; 0 = none.
- **EX062 — Abuse case derivation.** Which requirement follows from the replayed tap record abuse case? *Rubric:* 3 = unique record identifiers with replay detection;; 2 = replay detection;; 1 = vague;; 0 = none.
- **EX063 — Catalogue use.** How did Sofia use SP 800-53 Rev. 5? *Rubric:* 3 = to check for gaps, finding a missing log protection and review requirement;; 2 = gap check;; 1 = copied all;; 0 = none.

### Synthesis

Good security requirements are verifiable, grounded in abuse cases and checked against catalogues with justification.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Security architecture and engineering: system and data models

### Learning outcomes

You will (1) model the back office with components, interfaces and data flows; (2) mark trust boundaries and data classifications on the model; (3) keep models consistent with the system.

### 22.1 Component and interface model

Sofia models the fare back office as components: tap ingestion, journey construction, fare calculation, refunds, reporting and an integration layer to the payment provider. Each component has defined interfaces with message formats and authentication requirements. Modelling interfaces explicitly helps find places where data enters without validation or where a component trusts another more than it should. She notices that reporting reads directly from the journey database rather than through an interface, bypassing access controls, and records this as a design issue for review.

### 22.2 Boundaries and classifications

On the data-flow version of the model, Sofia marks trust boundaries: between validators and ingestion, between the back office and the payment provider, and between the back office and staff workstations. She labels each data flow with its classification from chapter 13. Flows that carry personal data across boundaries need encryption and authentication; flows carrying public data need integrity. The labelled model becomes the basis for threat modelling in the next chapter. It also makes it easy to answer an auditor's question about where personal data travels.

### 22.3 Keeping models true

Models drift from reality as systems change. Sofia proposes three practices: store the model in version control beside the code, review it in every design review and compare it quarterly with observed network flows and access logs. When the comparison finds a flow not in the model, either the model or the system is wrong, and both possibilities are worth knowing. Daniel notes that outdated diagrams are worse than none, because they give false confidence, so the model must have an owner responsible for keeping it accurate.

### Worked example

Sofia models six back-office components, finds reporting bypassing access controls, labels flows by classification and sets up quarterly model-to-reality checks.

> **Synthetic case.** Components and flows are synthetic.

### Errors and limits

Models abstract away details where flaws can hide. Observed flows may miss rare paths used only during incidents.

### Exercises

- **EX064 — Bypass issue.** What design issue did the component model reveal? *Rubric:* 3 = reporting reading the journey database directly, bypassing access controls;; 2 = bypass;; 1 = vague;; 0 = none.
- **EX065 — Personal data flows.** What do flows carrying personal data across boundaries need? *Rubric:* 3 = encryption and authentication;; 2 = both;; 1 = vague;; 0 = none.
- **EX066 — Drift response.** What does it mean when observed flows include one not in the model? *Rubric:* 3 = either the model or the system is wrong; investigate both;; 2 = investigate;; 1 = ignore;; 0 = none.

### Synthesis

Accurate system and data models, with boundaries and classifications, are the foundation of threat analysis and audit answers.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Security architecture and engineering: threat and failure analysis

### Learning outcomes

You will (1) threat-model the back office with STRIDE; (2) build a fault tree for a critical failure; (3) combine threat and failure views into prioritised risks.

### 23.1 STRIDE on the model

Using the data-flow model from chapter 22, Sofia and two engineers walk each element through STRIDE: spoofing, tampering, repudiation, information disclosure, denial of service and elevation of privilege, following Shostack (2014). They find that the ingestion interface accepts records from any device presenting a certificate from the internal authority, including retired validators; that refund decisions are not logged with the approver's identity, enabling repudiation; and that a burst of malformed records could exhaust the journey-construction queue. Each threat gets an owner, a proposed mitigation and a link to the requirement it affects.

### 23.2 Fault tree for revenue loss

Threat modelling asks what attackers can do; failure analysis asks how the system can fail, whatever the cause. Sofia builds a fault tree for the top event that a day's fare revenue cannot be reconciled. It occurs if tap records are lost or if the fare calculation is wrong. Records are lost if both the validator buffer overflows and the upload link is down for long enough. She assigns synthetic probabilities and computes the top-event probability with AND and OR gates, assuming independence. The lab below shows the calculation and which branch dominates.

### Lab — Fault tree for unreconciled revenue

```python
# Fault tree for "day's revenue cannot be reconciled" with synthetic daily probabilities (independence assumed).
p_buffer_overflow = 0.02
p_link_down_long = 0.05
p_records_lost = p_buffer_overflow * p_link_down_long          # AND gate
p_tariff_change_day = 0.10
p_calc_error_given_change = 0.08
p_calc_error = p_tariff_change_day * p_calc_error_given_change  # AND gate
p_top = 1 - (1 - p_records_lost) * (1 - p_calc_error)            # OR gate
print(f"records lost      {p_records_lost:.4f}")
print(f"calculation error {p_calc_error:.4f}")
print(f"top event         {p_top:.4f}  (~{p_top*365:.1f} days/year)")
```

Run with `python3 lab_fta.py`. Verified output:

```text
records lost      0.0010
calculation error 0.0080
top event         0.0090  (~3.3 days/year)
```

### 23.3 Combining views

The fault tree shows that calculation errors after tariff changes dominate the risk, more than lost records. The threat model shows that a malicious tariff table pushed through a compromised vendor account could cause exactly that failure. Combining the two views, Sofia rates signed and verified tariff tables as the top mitigation, because it addresses both accidental and malicious causes of the most likely failure. She notes that independence assumptions in fault trees can understate risk when one cause, such as a power cut, triggers several branches at once.

### Worked example

Sofia runs a STRIDE session finding three threats, builds a fault tree for unreconciled revenue and prioritises signed tariff tables because both analyses point to tariff errors.

> **Synthetic case.** Threats, probabilities and the fault tree are synthetic; Shostack (2014) is real.

### Errors and limits

Fault-tree probabilities are often guesses; their ranking is more useful than absolute values. STRIDE can miss threats outside the model.

### Exercises

- **EX067 — Retired validators.** Which spoofing threat did the STRIDE session find? *Rubric:* 3 = retired validators with internal certificates could still submit records;; 2 = retired devices;; 1 = vague;; 0 = none.
- **EX068 — Dominant branch.** Which branch dominated the fault tree in the lab? *Rubric:* 3 = fare calculation error after tariff change;; 2 = calculation;; 1 = lost records;; 0 = none.
- **EX069 — Independence caveat.** Why can independence assumptions understate risk? *Rubric:* 3 = a common cause like a power cut can trigger several branches together;; 2 = common cause;; 1 = overstate;; 0 = none.

### Synthesis

Threat modelling and fault trees together reveal which mitigations reduce both malicious and accidental failure.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Security architecture and engineering: methods I

### Learning outcomes

You will (1) compare qualitative and quantitative risk methods; (2) run a risk assessment following SP 800-30 Rev. 1; (3) document risk decisions with owners.

### 24.1 Qualitative and quantitative

Risk can be rated qualitatively, with scales like low, medium and high, or quantitatively, with estimated frequencies and losses. Qualitative methods are fast and help discussion but hide large differences within a category. Quantitative methods force explicit assumptions but can create false precision when inputs are guesses. Sofia uses both: a qualitative pass to rank many risks, then quantitative estimates with ranges for the top few, where decisions involve real money. She records the assumptions behind each number so that readers can challenge them rather than accept a figure at face value.

### 24.2 Running an assessment

NIST SP 800-30 Rev. 1 describes preparing the assessment, conducting it by identifying threat sources, events, vulnerabilities, likelihood and impact, communicating results and maintaining the assessment. Sofia follows these steps for the back office. She defines scope and assumptions, identifies threat sources from the STRIDE session and the context statement, rates likelihood and impact on agreed scales and records each risk. The method's value is consistency: another assessor using the same scales and information should reach similar ratings, which makes results comparable over time and across systems.

### 24.3 Risk decisions and owners

Each risk needs a decision: mitigate, transfer, avoid or accept. Sofia prepares a risk register where each entry has an owner with authority to decide. The finance director accepts a residual risk of up to one hour of stolen-card use, documented in chapter 5. The head of operations owns the risk of validator certificate misuse and approves a revocation project. Daniel stresses that engineers recommend but business owners decide, and that accepted risks must be reviewed regularly, because acceptance made under one context may be wrong after the context changes.

### Worked example

Sofia ranks twenty back-office risks qualitatively, estimates ranges for the top three, follows SP 800-30 Rev. 1 steps and assigns owners and decisions in a register.

> **Synthetic case.** Risks, ratings and owners are synthetic; SP 800-30 Rev. 1 is real.

### Errors and limits

Risk scales mean different things to different people unless anchored with examples. Quantitative ranges remain uncertain.

### Exercises

- **EX070 — Qualitative weakness.** What is a weakness of qualitative risk scales? *Rubric:* 3 = they hide large differences within one category;; 2 = hides differences;; 1 = vague;; 0 = none.
- **EX071 — SP 800-30 steps.** Name the four main steps of SP 800-30 Rev. 1. *Rubric:* 3 = prepare, conduct, communicate, maintain;; 2 = three;; 1 = one;; 0 = none.
- **EX072 — Who decides.** Who decides whether to accept a risk? *Rubric:* 3 = the business owner with authority, not the engineer;; 2 = owner;; 1 = engineer;; 0 = none.

### Synthesis

Sound risk methods combine quick ranking with explicit estimates and put decisions in the hands of accountable owners.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) develop an architecture design in a studio setting; (2) present and defend design choices; (3) incorporate critique into revisions.

### 25.1 Studio brief

In Design Studio I, Sofia's team of four receives a brief: design the secure architecture for Corvia's new depot charging management system, which schedules electric bus charging and connects to the energy supplier's portal. They have four weeks. They start with context, stakeholders and protection needs, then draw a component model and data flows. The studio format mirrors professional practice: designs are developed iteratively, reviewed by peers and practitioners and revised. Daniel acts as client, answering questions about constraints and refusing to make design decisions for them.

### 25.2 Presenting choices

At the midpoint review the team presents three options: charging control in the cloud with remote commands to depots; control at each depot with cloud reporting only; and a hybrid. They argue for depot-local control because buses must charge even when the internet link fails, with signed schedules from the cloud and local fallback rules. A reviewer challenges how they will stop a compromised depot controller from damaging chargers. They have no answer yet and say so honestly, recording the question as an open issue rather than inventing a response under pressure.

### 25.3 Revising from critique

In the following week the team researches the open issue with the charger vendor's documentation and safety engineers. They add hardware limits in chargers that cannot be overridden by the controller, separate the controller network from corporate systems and require two-person approval for changes to fallback rules. At the final review they show how each change answers the critique and what risk remains. Sofia learns that a design studio rewards honest uncertainty followed by research, and that critique is most useful when recorded and answered explicitly in the next version.

### Worked example

Sofia's team compares three charging-control options, chooses depot-local control with signed schedules, records an open issue on compromised controllers and answers it with hardware limits and segmentation.

> **Synthetic case.** The charging system, vendor and reviews are synthetic.

### Errors and limits

Studio designs lack production detail; real constraints may change choices. Hardware limits depend on vendor implementation quality.

### Exercises

- **EX073 — Local control reason.** Why did the team choose depot-local charging control? *Rubric:* 3 = buses must charge even when internet links fail;; 2 = resilience;; 1 = cost;; 0 = none.
- **EX074 — Unanswered challenge.** How did the team handle the challenge they could not answer? *Rubric:* 3 = said so honestly and recorded it as an open issue;; 2 = open issue;; 1 = invented answer;; 0 = none.
- **EX075 — Final mitigations.** Name two mitigations added after critique. *Rubric:* 3 = non-overridable charger hardware limits, network separation, two-person approval for fallback rules (two);; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

A design studio teaches architecture through options, honest open issues and revisions that answer critique explicitly.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Security architecture and engineering: architecture alternatives

### Learning outcomes

You will (1) generate architecture alternatives for the back office; (2) evaluate them against weighted criteria; (3) document why the chosen option won.

### 26.1 Generating alternatives

For the fare back office, Sofia generates three alternatives. Alternative A keeps a single on-premises cluster with improved segmentation. Alternative B moves processing to a cloud provider with managed key services. Alternative C splits the system: tap ingestion and fare calculation stay on-premises, while reporting and analytics move to the cloud with only pseudonymised data. Daniel insists on at least three options, because comparing only two often hides a better middle path, and a do-minimum option provides a baseline against which the value of change can be judged.

### 26.2 Weighted evaluation

Sofia and the stakeholders agree criteria and weights: security of personal data, resilience during outages, cost over five years, migration risk and fit with the legacy validators. Each alternative is scored by three people independently, then scores are discussed where they differ. Alternative C scores highest overall, mainly because it keeps personal data on-premises while gaining cloud scalability for analytics. Sofia records how sensitive the result is: if cost weight doubles, A wins. Sensitivity shows stakeholders which assumptions drive the decision, inviting debate on those rather than on the final number.

### 26.3 Documenting the choice

Sofia writes an architecture decision record for alternative C, listing the options, criteria, weights, scores, sensitivity results and consequences, including new risks such as the pseudonymisation process being a single point of failure for privacy. The record also states conditions under which the decision should be revisited, such as a change in cloud pricing or regulatory guidance. Daniel explains that decisions documented this way can be audited and revisited calmly, while undocumented decisions are reopened repeatedly whenever a new manager arrives with a different preference.

### Worked example

Sofia generates three back-office alternatives, scores them on five weighted criteria with sensitivity analysis and records alternative C with its new risks and revisit conditions.

> **Synthetic case.** Alternatives, weights and scores are synthetic.

### Errors and limits

Weighted scoring can hide disagreements behind averages. Pseudonymised data may be re-identifiable when combined with other data.

### Exercises

- **EX076 — Three options.** Why does Daniel insist on at least three alternatives? *Rubric:* 3 = two options hide middle paths; a do-minimum gives a baseline;; 2 = middle path;; 1 = no reason;; 0 = none.
- **EX077 — Sensitivity result.** What happens to the decision if the cost weight doubles? *Rubric:* 3 = alternative A wins instead of C;; 2 = A wins;; 1 = C still;; 0 = none.
- **EX078 — New risk.** What new risk does alternative C introduce? *Rubric:* 3 = pseudonymisation process becomes a single point of failure for privacy;; 2 = pseudonymisation;; 1 = vague;; 0 = none.

### Synthesis

Comparing several alternatives with explicit weights and sensitivity makes architecture decisions transparent and revisitable.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Security architecture and engineering: control design

### Learning outcomes

You will (1) design controls that meet specific requirements; (2) layer preventive, detective and corrective controls; (3) specify controls precisely enough to implement and test.

### 27.1 Designing to requirements

Sofia designs controls for the requirement that tariff tables must be authentic before use. The preventive control is a digital signature: tariff tables are signed in the tariff office with a key held in a hardware security module, and every consumer verifies the signature with a pinned public key before loading. The detective control logs every load with the table's version and hash, and alerts if a version appears that the tariff office did not publish. The corrective control lets operations roll back to the last verified table within minutes. Each control links to the requirement and abuse case it serves.

### 27.2 Defence in depth with purpose

Layering controls is useful only if layers fail independently. Sofia checks her tariff-table design: if the signing key were stolen, signatures would verify, so the detective control compares loaded versions with an independent publication list kept by finance. If verification code had a bug, the detective control would still notice unexpected versions. If both failed, rollback limits damage. She notes that two controls depending on the same key or the same database do not provide real depth. Defence in depth means asking, for each layer, what happens if the previous one fails.

### 27.3 Precise specifications

A control specification must say enough to implement and test. Sofia writes: the signature algorithm is Ed25519 as specified in RFC 8032; the public key is pinned in configuration and rotated only through change control; verification failure stops loading and raises a high-priority alert; logs include table identifier, version, hash and verifying component. She attaches test cases: a correctly signed table loads; a modified table is rejected; a table signed with an unknown key is rejected. Precise specifications prevent each implementer from making different assumptions that leave gaps between components.

### Worked example

Sofia designs signed tariff tables with an HSM-held key, independent version checks and rollback, tests layer independence and writes a specification with three test cases.

> **Synthetic case.** The tariff design is synthetic; RFC 8032 is real.

### Errors and limits

Pinned keys complicate emergency rotation. Detective controls depend on someone responding to alerts.

### Exercises

- **EX079 — Three control types.** Name the preventive, detective and corrective controls for tariff tables. *Rubric:* 3 = signature verification; version logging and alerts; rollback;; 2 = three;; 1 = one;; 0 = none.
- **EX080 — Independence check.** Why compare loaded versions with finance's independent list? *Rubric:* 3 = it still detects misuse if the signing key is stolen;; 2 = independent;; 1 = redundant;; 0 = none.
- **EX081 — Specification test.** Give one test case from the specification. *Rubric:* 3 = correctly signed loads, modified rejected or unknown key rejected;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Good control design ties each control to a requirement, layers controls that fail independently and specifies them precisely.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Security architecture and engineering: implementation I

### Learning outcomes

You will (1) translate architecture into implementation tasks; (2) apply secure configuration and secrets handling; (3) keep implementation aligned with the architecture.

### 28.1 From architecture to tasks

Sofia's team begins implementing the back-office ingestion component. She breaks the architecture into tasks: certificate-based device authentication, record schema validation, replay detection with a store of recent record identifiers, signed-record verification and structured logging. Each task references the requirement and control specification it implements and includes acceptance tests. This prevents the common drift in which developers implement what is easy and the architecture's harder controls are quietly postponed. Task references also let reviewers check coverage: every requirement should map to at least one completed task.

### 28.2 Configuration and secrets

The ingestion service needs a private key for its TLS server certificate and credentials for its database. Sofia ensures neither is stored in source code or container images. Secrets come from a managed secret store at runtime, readable only by the service's identity, and are rotated on a schedule. Configuration is version-controlled and reviewed, with security-relevant settings such as TLS versions and allowed certificate issuers checked automatically against the specification. She finds a test credential committed in an early branch, removes it from history and has it rotated, recording the incident.

### 28.3 Staying aligned

During implementation the team discovers that replay detection needs more memory than expected at peak load. A developer proposes skipping it during peaks. Sofia raises it as an architecture change, not a coding decision, because it weakens a requirement. The team instead uses a time-bounded store keyed by record identifier and validator, which fits memory limits. She updates the architecture record and the specification. Daniel stresses that implementation always teaches something; the discipline is to feed that learning back into the architecture rather than letting the built system silently diverge.

### Worked example

Sofia maps ingestion requirements to five implementation tasks, moves secrets to a managed store, handles a committed test credential and routes a replay-detection change through architecture review.

> **Synthetic case.** The ingestion component and incident are synthetic.

### Errors and limits

Secret stores become critical dependencies needing high availability. Removing secrets from history does not undo exposure; rotation is still required.

### Exercises

- **EX082 — Task references.** Why does each task reference a requirement? *Rubric:* 3 = prevents postponing hard controls and lets reviewers check coverage;; 2 = coverage;; 1 = vague;; 0 = none.
- **EX083 — Committed credential.** What steps followed finding a committed test credential? *Rubric:* 3 = removed from history and rotated, incident recorded;; 2 = both;; 1 = removed only;; 0 = none.
- **EX084 — Replay change route.** Why was skipping replay detection treated as an architecture change? *Rubric:* 3 = it weakens a requirement, so it needs architecture review;; 2 = requirement;; 1 = coding choice;; 0 = none.

### Synthesis

Implementation honours the architecture when tasks trace to requirements, secrets stay out of code and discoveries feed back into design.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Security architecture and engineering: measurement

### Learning outcomes

You will (1) define security metrics tied to architecture goals; (2) compute coverage and timeliness metrics from synthetic data; (3) avoid metrics that reward the wrong behaviour.

### 29.1 Metrics tied to goals

Daniel asks Sofia to propose metrics for the back-office architecture. She starts from goals: authentic tariff tables, timely revocation of retired devices, protected personal data and quick recovery. For each she defines one or two metrics: percentage of tariff loads with verified signatures; median days from device retirement to certificate revocation; percentage of personal-data stores with encryption and access logging enabled; and time to restore ingestion in recovery tests. Each metric has a definition, data source, target and owner. Metrics without goals tend to measure what is easy rather than what matters.

### 29.2 Computing metrics

Sofia writes a script that reads synthetic records of device retirements and revocations and data-store configurations, and computes the metrics. The lab below shows that revocation timeliness is poor, with a long tail of devices revoked weeks after retirement and some never revoked, while encryption coverage is high. She presents counts and denominators alongside percentages. The numbers immediately prioritise work: the revocation process, not encryption, needs attention. Measurement turns the threat found in chapter 23 into a tracked improvement with a baseline.

### Lab — Revocation timeliness and coverage

```python
# Synthetic device retirement/revocation records and data-store configs.
import statistics
delays = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 12, 15, 21, 28, 35, 44, None, None, None]   # None = never revoked
done = [d for d in delays if d is not None]
print(f"retired devices: {len(delays)}, revoked: {len(done)}, never revoked: {delays.count(None)}")
print(f"median days to revoke (revoked only): {statistics.median(done)}")
print(f"revoked within 7 days: {sum(d <= 7 for d in done)}/{len(delays)}")
stores = {"journeys": (True, True), "refunds": (True, True), "staff": (True, False), "reports": (True, True), "archive": (True, True)}
cov = sum(e and l for e, l in stores.values())
print(f"personal-data stores encrypted+logged: {cov}/{len(stores)}")
```

Run with `python3 lab_metrics.py`. Verified output:

```text
retired devices: 20, revoked: 17, never revoked: 3
median days to revoke (revoked only): 8
revoked within 7 days: 8/20
personal-data stores encrypted+logged: 4/5
```

### 29.3 Metrics that mislead

Metrics shape behaviour. If the team is rewarded for closing vulnerability tickets quickly, they may close tickets without verification. If the metric is number of controls implemented, they may implement easy controls rather than important ones. Sofia proposes pairing metrics: closure speed with reopen rate; control count with coverage of high-priority risks. She also warns against reporting a metric without its denominator or trend. Anderson (2020) discusses how security metrics can be gamed. Good metrics are few, tied to goals and reviewed to see whether they still drive the intended behaviour.

### Worked example

Sofia defines five goal-linked metrics, computes revocation timeliness and encryption coverage from synthetic data and pairs metrics to resist gaming.

> **Synthetic case.** Metrics data are synthetic; Anderson (2020) is real.

### Errors and limits

Metrics measure proxies, not security itself. Small denominators make percentages unstable.

### Exercises

- **EX085 — Goal-linked metric.** Give a metric for the goal of timely revocation of retired devices. *Rubric:* 3 = median days from retirement to revocation;; 2 = metric;; 1 = count of devices;; 0 = none.
- **EX086 — Lab revocation result.** What did the lab show for revocation timeliness? *Rubric:* 3 = median 8 days for revoked devices, 3 of 20 never revoked, only 8 of 20 within a week;; 2 = both;; 1 = good;; 0 = none.
- **EX087 — Paired metric.** Which metric should be paired with ticket closure speed? *Rubric:* 3 = reopen rate;; 2 = reopen;; 1 = vague;; 0 = none.

### Synthesis

Security metrics should follow goals, show denominators and be paired so they reward real improvement.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify that implemented controls meet their specifications; (2) run positive and negative test cases for record authenticity and replay; (3) record verification evidence.

### 30.1 Purpose of verification

Verification asks whether the system was built as specified. In Verification Laboratory I, Sofia tests the ingestion component's authenticity and replay controls in an isolated lab with synthetic validators. Her test plan comes directly from the control specifications: each requirement has positive tests showing correct behaviour and negative tests showing that bad inputs are rejected. The lab environment uses synthetic keys and data only. Verification evidence will support the assurance case later, so every test records inputs, expected results, actual results, environment version and date in a consistent format.

### 30.2 Authenticity and replay tests

In the lab, validators authenticate tap records with a message authentication code using a key shared with ingestion, a simplified stand-in for the production signatures, implemented with Python's hmac module. Sofia's script sends four synthetic records: an authentic new record, a duplicate of it, a record with an altered amount and a record from a retired validator whose key has been removed. The lab below shows ingestion accepting only the first. She compares the results with expected outcomes and finds all four match. A mismatch would have been a defect to raise, not a test to adjust.

### Lab — Authenticity and replay verification

```python
# Lab ingestion check: HMAC stand-in for validator signatures + replay store. Synthetic keys only.
import hmac, hashlib
keys = {"V-101": b"lab-key-101", "V-102": b"lab-key-102"}       # V-099 retired: key removed
seen = set()
def tag(k, rec): return hmac.new(k, rec, hashlib.sha256).hexdigest()
def ingest(vid, rec, t):
    k = keys.get(vid)
    if k is None: return "reject: unknown or retired validator"
    if not hmac.compare_digest(tag(k, rec), t): return "reject: bad tag"
    rid = rec.split(b",")[0]
    if (vid, rid) in seen: return "reject: replay"
    seen.add((vid, rid)); return "accept"
r = b"R-5521,C100,2.40"
t = tag(keys["V-101"], r)
print("authentic:", ingest("V-101", r, t))
print("duplicate:", ingest("V-101", r, t))
print("altered amount:", ingest("V-101", b"R-5522,C100,0.10", tag(keys["V-101"], b"R-5522,C100,2.40")))
print("retired validator:", ingest("V-099", b"R-7,C200,2.40", tag(b"old-099", b"R-7,C200,2.40")))
```

Run with `python3 lab_ingest.py`. Verified output:

```text
authentic: accept
duplicate: reject: replay
altered amount: reject: bad tag
retired validator: reject: unknown or retired validator
```

### 30.3 Recording evidence

Sofia writes a verification report with a table of tests, outcomes and evidence links, and notes what was not verified: performance under peak load, behaviour during database failover and the production signature path, which uses a different mechanism. She signs and dates the report and stores it with a hash in the project's evidence repository. Daniel reminds her that verification shows conformance to specification; whether the specification itself is adequate is a separate question addressed by validation, which comes later in the course.

### Worked example

Sofia runs four authenticity and replay tests in an isolated lab, finds all match expectations and records a report listing three areas not yet verified.

> **Synthetic case.** The lab, keys and records are synthetic; HMAC stands in for production signatures.

### Errors and limits

Lab environments differ from production in scale and timing. Passing tests depend on the quality of the test cases.

### Exercises

- **EX088 — Verification question.** What question does verification answer? *Rubric:* 3 = was the system built as specified;; 2 = as specified;; 1 = is it useful;; 0 = none.
- **EX089 — Lab outcomes.** Which of the four lab records were accepted? *Rubric:* 3 = only the authentic new record; duplicate, altered and retired rejected;; 2 = only first;; 1 = several;; 0 = none.
- **EX090 — Not verified.** Name one area Sofia's report lists as not verified. *Rubric:* 3 = peak load, database failover or production signature path;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Verification tests controls against their specifications with positive and negative cases and records honest evidence of scope.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Security architecture and engineering: implementation II

### Learning outcomes

You will (1) implement certificate life-cycle automation for devices; (2) integrate revocation with asset management; (3) handle legacy components that cannot meet the target design.

### 31.1 Automating device certificates

The metrics in chapter 29 showed slow revocation of retired validators. In Implementation II, Sofia's team automates the device certificate life cycle. New validators receive certificates through an enrolment process that requires an asset record and an approved installation ticket. Certificates have short validity and renew automatically while the device is in service. The design follows key management phases from SP 800-57 Part 1 Rev. 5. Automation reduces both the manual work that caused delays and the chance of human error, but it also concentrates trust in the enrolment service, which must itself be protected and monitored.

### 31.2 Linking to asset management

Revocation now triggers from the asset management system: when a validator is marked retired, lost or stolen, an event calls the internal authority to revoke its certificate and adds it to the ingestion deny list. Sofia writes integration tests for each status change. She also adds a daily reconciliation that compares active certificates with in-service assets and alerts on mismatches. Integration across systems is where many security processes fail, because each team assumes another handles the step, so the reconciliation acts as a safety net for missed events.

### 31.3 Legacy exceptions

About one hundred older validators cannot support automatic renewal. Sofia does not pretend they meet the design. She documents them as exceptions with compensating controls: longer-lived certificates stored in their secure elements, ingestion rules limiting their accepted record rates, quarterly manual checks and a replacement date in year five. Each exception has an owner and an expiry date. Daniel explains that honest exception management is a sign of mature architecture; designs that claim full compliance while hiding legacy gaps leave the organisation exposed to risks nobody is tracking.

### Worked example

Sofia's team automates validator enrolment and renewal, triggers revocation from asset status changes with daily reconciliation and documents one hundred legacy validators as owned, expiring exceptions.

> **Synthetic case.** Devices, systems and counts are synthetic; SP 800-57 Part 1 Rev. 5 is real.

### Errors and limits

Automated enrolment becomes a high-value target. Reconciliation depends on asset records being accurate.

### Exercises

- **EX091 — Enrolment condition.** What must exist before a validator receives a certificate? *Rubric:* 3 = an asset record and an approved installation ticket;; 2 = both;; 1 = vague;; 0 = none.
- **EX092 — Reconciliation purpose.** What does the daily reconciliation catch? *Rubric:* 3 = mismatches between active certificates and in-service assets from missed events;; 2 = mismatches;; 1 = nothing;; 0 = none.
- **EX093 — Exception contents.** What does each legacy exception include? *Rubric:* 3 = compensating controls, owner and expiry or replacement date;; 2 = three;; 1 = vague;; 0 = none.

### Synthesis

Implementation II closes measured gaps through automation and integration while managing legacy exceptions honestly.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Security architecture and engineering: reliability

### Learning outcomes

You will (1) compute availability of components in series and parallel; (2) design redundancy for security services; (3) recognise when security controls reduce reliability.

### 32.1 Series and parallel

Reliability engineering gives simple rules. Components in series, all needed for the service, multiply their availabilities, so the whole is less available than any part. Components in parallel, any one sufficient, combine so the whole is more available than each. Sofia applies this to ingestion, which needs the load balancer, the ingestion service, the secret store and the database in series. The lab below computes overall availability with synthetic figures and shows how adding a second secret-store instance in parallel changes the result. Security services such as secret stores are often forgotten when availability is planned.

### Lab — Series and parallel availability

```python
# Series/parallel availability with synthetic component figures.
comp = {"load balancer": 0.9995, "ingestion": 0.999, "secret store": 0.998, "database": 0.9995}
def series(xs):
    p = 1.0
    for x in xs: p *= x
    return p
def parallel(a, n): return 1 - (1 - a) ** n
base = series(comp.values())
red = series([comp["load balancer"], comp["ingestion"], parallel(comp["secret store"], 2), comp["database"]])
print(f"single secret store: {base:.4f}  (~{(1-base)*8760:.0f} h/yr down)")
print(f"two secret stores:   {red:.4f}  (~{(1-red)*8760:.0f} h/yr down)")
```

Run with `python3 lab_avail.py`. Verified output:

```text
single secret store: 0.9960  (~35 h/yr down)
two secret stores:   0.9980  (~18 h/yr down)
```

### 32.2 Redundancy for security services

Authentication, key management and logging are dependencies of almost everything. If the identity provider fails, staff cannot log in; if the secret store fails, services cannot start; if logging fails, attacks go unseen. Sofia proposes redundancy for each: clustered identity providers across two sites, replicated secret stores, and local log buffering when the central collector is unreachable. She also documents what happens in degraded mode, such as validators continuing with cached deny lists. Designing degraded behaviour deliberately is safer than discovering it during an outage.

### 32.3 When security hurts reliability

Some controls reduce availability. Strict certificate validation fails closed if the revocation service is unreachable; aggressive rate limiting can block legitimate surges; mandatory multi-factor authentication fails if the second-factor service is down. Sofia lists such cases and decides each deliberately: tap ingestion soft-fails revocation checks for a short period using cached lists, while administrative access hard-fails. The decision follows from the asset and the threat: revenue collection must continue, while administrative access can wait. Reliability and security are both properties of the same system and must be traded off explicitly.

### Worked example

Sofia computes ingestion availability with and without a redundant secret store, designs redundancy for three security services and records fail-open and fail-closed decisions.

> **Synthetic case.** Availability figures are synthetic.

### Errors and limits

Independence assumptions overstate parallel benefits when replicas share a failure cause. Soft-fail windows can be abused.

### Exercises

- **EX094 — Series rule.** How do availabilities combine in series? *Rubric:* 3 = multiply; the whole is less available than any part;; 2 = multiply;; 1 = add;; 0 = none.
- **EX095 — Lab redundancy effect.** What did the lab show when the secret store was duplicated? *Rubric:* 3 = availability rose from 0.9960 to 0.9980, roughly halving downtime from about 35 to 18 hours a year;; 2 = rise;; 1 = fall;; 0 = none.
- **EX096 — Fail decision.** Which path soft-fails revocation checks, and which hard-fails? *Rubric:* 3 = tap ingestion soft-fails briefly; administrative access hard-fails;; 2 = both;; 1 = reversed;; 0 = none.

### Synthesis

Reliability engineering applies to security services, and fail-open or fail-closed choices must follow from assets and threats.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Security architecture and engineering: safety and resilience

### Learning outcomes

You will (1) distinguish security, safety and resilience goals; (2) apply resilience techniques from systems-engineering guidance; (3) design for graceful degradation under attack.

### 33.1 Three related goals

Security protects against intentional harm, safety protects people from physical harm whatever the cause, and resilience is the ability to anticipate, withstand, recover from and adapt to adverse conditions. In transit systems they overlap. A ransomware attack on the operations centre is a security event that may become a safety issue if passenger information fails during disruptions. Sofia learns that the three communities use different methods and vocabularies, and that architects must bring them together, for example by inviting safety engineers to threat-modelling sessions for systems that affect passengers or vehicles.

### 33.2 Resilience techniques

NIST SP 800-160 Vol. 1 Rev. 1 links resilience to engineering trustworthy systems, and SP 800-160 Vol. 2 Rev. 1 describes cyber-resiliency techniques such as redundancy, diversity, segmentation, adaptive response and non-persistence, each with guidance on when it helps. Sofia applies several to Corvia's operations centre: segmentation to contain spread, offline backups to recover, a diverse backup communication channel for drivers and pre-planned manual operating procedures. She writes each technique beside the adverse condition it addresses. Resilience planning assumes that prevention will sometimes fail and asks how the mission continues anyway, and which people must act when it does.

### 33.3 Graceful degradation

Sofia designs degradation levels for the fare system. Level one: central back office unavailable, validators continue offline with cached tariffs and deny lists. Level two: validators unavailable, inspectors accept visual proof and fares are suspended. Level three: operations centre compromised, services run on manual timetables with radio communication. Each level has a trigger, a decision maker and a return procedure. Rehearsing these levels shows staff that a cyber incident need not stop the trams, which reduces pressure to pay ransoms or rush unsafe restorations.

### Worked example

Sofia separates security, safety and resilience goals, maps four resilience techniques to adverse conditions and defines three degradation levels with triggers and owners.

> **Synthetic case.** Degradation levels and procedures are synthetic; SP 800-160 Vol. 1 Rev. 1 and Vol. 2 Rev. 1 are real.

### Errors and limits

Manual procedures decay without practice. Degradation may itself create fraud opportunities that need monitoring.

### Exercises

- **EX097 — Resilience definition.** Define resilience in this chapter's terms. *Rubric:* 3 = ability to anticipate, withstand, recover from and adapt to adverse conditions;; 2 = three parts;; 1 = security only;; 0 = none.
- **EX098 — Diverse channel.** Which resilience technique does a backup driver communication channel represent? *Rubric:* 3 = diversity or redundancy of communication;; 2 = diversity;; 1 = segmentation;; 0 = none.
- **EX099 — Ransom pressure.** How do rehearsed degradation levels reduce ransom pressure? *Rubric:* 3 = staff know services can continue manually, so there is less urgency to pay;; 2 = continuity;; 1 = vague;; 0 = none.

### Synthesis

Resilient architecture assumes prevention can fail and designs safe, rehearsed ways for the mission to continue.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Security architecture and engineering: integration

### Learning outcomes

You will (1) secure integrations with external partners; (2) design API authentication and authorisation for partner access; (3) manage shared responsibility at integration boundaries.

### 34.1 Partner integrations

Corvia integrates with a payment provider, a regional mobility app that sells Corvia tickets, the energy supplier and a data-analytics consultancy. Each integration crosses a trust boundary and carries contractual and technical obligations. Sofia lists for each the data exchanged, the direction, the authentication method and the party responsible for each control. She finds that the mobility app uses a single long-lived API key shared by all its servers, while the consultancy receives monthly data exports by email. Both are integration weaknesses that the architecture should address.

### 34.2 API design for partners

Sofia proposes a partner API gateway. Partners authenticate with short-lived tokens obtained using client credentials bound to certificates, rather than static keys. Each token carries scopes limiting what the partner can do: the mobility app may sell tickets and query fares, but not read journey histories. The gateway enforces rate limits, validates schemas and logs every request with partner identity. Data exports to the consultancy move to a secure transfer service with pseudonymised data and access expiry. These choices apply least privilege and complete mediation at the boundary.

### 34.3 Shared responsibility

At every integration, some controls belong to Corvia and some to the partner. Sofia writes a responsibility matrix: Corvia protects the gateway and validates requests; the partner protects its credentials and its own users; both must report incidents within agreed times. The matrix is attached to contracts. When the mobility app later suffers a breach of its own customer accounts, the matrix makes clear which party notifies which passengers and which tokens Corvia revokes. Clarity about responsibility avoids gaps where each party assumes the other handles a control.

### Worked example

Sofia inventories four partner integrations, replaces a shared static API key with certificate-bound short-lived scoped tokens and writes a responsibility matrix used during a partner breach.

> **Synthetic case.** Partners, integrations and the breach are synthetic.

### Errors and limits

Gateways become single points of failure and must be resilient. Contracts cannot force partners to secure their own systems.

### Exercises

- **EX100 — Two weaknesses.** Which two integration weaknesses did Sofia find? *Rubric:* 3 = mobility app's shared long-lived API key; consultancy exports by email;; 2 = both;; 1 = one;; 0 = none.
- **EX101 — Scope example.** What may the mobility app's tokens allow, and not allow? *Rubric:* 3 = sell tickets and query fares, not read journey histories;; 2 = both parts;; 1 = all access;; 0 = none.
- **EX102 — Matrix in breach.** How did the responsibility matrix help during the partner breach? *Rubric:* 3 = clarified who notifies passengers and which tokens Corvia revokes;; 2 = clarity;; 1 = vague;; 0 = none.

### Synthesis

Secure integration combines scoped, short-lived credentials at gateways with written shared responsibility.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) lead a multi-disciplinary design for a larger system; (2) reconcile conflicting stakeholder requirements; (3) produce a design package suitable for independent review.

### 35.1 The brief

Design Studio II is larger: Sofia leads a team of six, including two students from other engineering disciplines, to design the security architecture of Corvia's planned account-based ticketing, where passengers tap bank cards or phones and fares are calculated in the back office rather than stored on cards. The brief includes privacy, payment, accessibility and operational requirements. Sofia's role is to coordinate, not to decide everything. She sets up a shared decision log, assigns each team member an area and holds short daily check-ins so conflicts surface early.

### 35.2 Reconciling conflicts

Requirements collide. Fraud analysts want detailed journey histories kept for two years; the privacy lead wants ninety days; customer service wants histories visible to agents for disputes; the accessibility lead wants simple account recovery for passengers who lose phones, which fraud analysts fear will enable account takeover. Sofia runs a session where each side states the underlying need. The result: detailed data for ninety days, aggregated fraud features for two years, agent views showing only the disputed journeys and recovery through verified bank-card taps rather than security questions. Each compromise is recorded with its rationale.

### 35.3 The design package

The final package contains the context statement, requirements with verification methods, the component and data-flow models, threat model, alternatives analysis, control specifications, degradation levels, open issues and the decision log. Sofia checks that every requirement traces to controls and tests. The package goes to an independent reviewer from another university, who identifies two gaps: no plan for key compromise in the tokenisation service and an unclear owner for passenger data deletion requests. Sofia's team adds both. Producing a package others can review is the deliverable, more than any single diagram.

### Worked example

Sofia leads a six-person studio on account-based ticketing, reconciles four conflicting requirements through stated needs and assembles a reviewable package that closes two gaps found by an external reviewer.

> **Synthetic case.** The studio, team and reviewer are synthetic.

### Errors and limits

Studio compromises may not survive real negotiations. Package completeness does not guarantee design quality.

### Exercises

- **EX103 — Leader's role.** What is Sofia's main role as studio lead? *Rubric:* 3 = coordinate, surface conflicts and keep a decision log, not decide everything;; 2 = coordinate;; 1 = decide all;; 0 = none.
- **EX104 — Retention compromise.** What retention compromise did the team reach? *Rubric:* 3 = detailed data 90 days, aggregated fraud features two years;; 2 = both;; 1 = one;; 0 = none.
- **EX105 — Reviewer gaps.** What two gaps did the independent reviewer find? *Rubric:* 3 = no key-compromise plan for tokenisation; unclear owner for deletion requests;; 2 = both;; 1 = one;; 0 = none.

### Synthesis

Large designs succeed when needs behind conflicting requirements are surfaced and the result is packaged for independent review.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Security architecture and engineering: performance and scale

### Learning outcomes

You will (1) analyse the performance cost of security controls; (2) size rate limiting with a token bucket; (3) design controls that scale with demand.

### 36.1 The cost of controls

Every control consumes resources. TLS handshakes cost CPU; signature verification adds latency per record; logging consumes storage and network bandwidth; deep inspection slows traffic. At small scale these costs are invisible, but account-based ticketing will process millions of taps per day. Sofia measures the cost of each control in a lab and estimates totals at peak. She finds that signature verification is cheap per record but adds up, while verbose debug logging would exceed storage budgets within weeks. Measuring costs early prevents later pressure to switch controls off when performance suffers.

### 36.2 Token bucket sizing

The partner gateway from chapter 34 must limit request rates without blocking legitimate bursts, such as many ticket purchases before a concert. Sofia models a token bucket: tokens refill at a steady rate, each request consumes one, and the bucket's capacity allows short bursts. The lab below simulates a synthetic burst of requests against two bucket sizes with the same refill rate. The small bucket rejects many legitimate requests during the burst; the larger one absorbs nearly all of it while still capping sustained abuse. Sizing comes from observed traffic, not guesswork.

### Lab — Token bucket burst handling

```python
# Token bucket vs synthetic burst: 20 req/s refill, burst of 300 requests over 5 s.
def run(capacity, refill=20.0, seconds=20):
    tokens, rejected = capacity, 0
    for t in range(seconds):
        tokens = min(capacity, tokens + refill)
        demand = 60 if 5 <= t < 10 else 10
        ok = min(demand, int(tokens)); tokens -= ok; rejected += demand - ok
    return rejected
for cap in (20, 200):
    print(f"capacity {cap:3d}: rejected {run(cap)} of {5*60 + 15*10} requests")
```

Run with `python3 lab_bucket.py`. Verified output:

```text
capacity  20: rejected 200 of 450 requests
capacity 200: rejected 20 of 450 requests
```

### 36.3 Designing for scale

Controls that work for one server may not scale. A central authorisation service called for every tap becomes a bottleneck and a single point of failure. Sofia proposes caching authorisation decisions with short lifetimes, distributing verification to ingestion nodes with shared public keys and partitioning logs by time and region. Each change keeps the security property while improving scale, and each introduces a new consideration, such as how quickly cached decisions reflect revocations. She documents these trade-offs so operations staff understand why, for example, a revoked partner token may work for up to a minute.

### Worked example

Sofia measures control costs, sizes a token bucket for concert bursts and redesigns authorisation and logging to scale while documenting cache-related revocation delays.

> **Synthetic case.** Traffic, costs and bucket parameters are synthetic.

### Errors and limits

Lab measurements may not reflect production hardware. Caches create windows where revoked rights still work.

### Exercises

- **EX106 — Hidden cost.** Which control would exceed storage budgets within weeks? *Rubric:* 3 = verbose debug logging;; 2 = logging;; 1 = TLS;; 0 = none.
- **EX107 — Bucket comparison.** How did the two bucket sizes handle the synthetic burst? *Rubric:* 3 = capacity 20 rejected 200 of 450; capacity 200 rejected 20;; 2 = both;; 1 = same;; 0 = none.
- **EX108 — Cache trade-off.** What trade-off does caching authorisation decisions introduce? *Rubric:* 3 = revoked rights may keep working until the cache expires;; 2 = revocation delay;; 1 = vague;; 0 = none.

### Synthesis

Scalable security measures control costs, sizes limits from real traffic and documents the trade-offs of distributing controls.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Security architecture and engineering: operations

### Learning outcomes

You will (1) design security operations for the new architecture; (2) define detection use cases from the threat model; (3) plan patching and change management that preserve security properties.

### 37.1 Operations by design

An architecture is only as good as its operation. Sofia works with Corvia's operations centre to plan how the new back office will be run securely: who monitors which alerts, who can change configurations, how incidents are escalated and how access is reviewed. She uses NIST CSF 2.0, whose functions are govern, identify, protect, detect, respond and recover, to check that each function has owners and procedures for the new system. Operations planning during design avoids building systems that nobody can monitor or maintain properly after the project team leaves.

### 37.2 Detection from threats

Sofia turns threats from chapter 23 into detection use cases. For replayed tap records: alert when replay rejections from one validator exceed a threshold. For malicious tariff tables: alert on any unpublished version. For insider export of journey data: alert when exports exceed normal volume or occur outside working hours. Each use case lists the data source, the logic, expected false positives and the response playbook. Deriving detection from the threat model ensures monitoring focuses on what matters to this system rather than on generic alerts copied from vendor templates.

### 37.3 Patching and change

Changes can break security properties. Sofia defines a change process where any change touching authentication, cryptography, network rules or logging needs security review and re-running of relevant verification tests from chapters 30 and 40. Routine patches follow a schedule with emergency paths for critical vulnerabilities. She also requires that the architecture model be updated when a change alters flows or components. Daniel notes that most organisations struggle not with designing secure systems but with keeping them secure through years of small, well-intended changes.

### Worked example

Sofia maps the back office to CSF 2.0 functions, derives three detection use cases from the threat model and defines a change process with security re-verification.

> **Synthetic case.** Use cases and processes are synthetic; NIST CSF 2.0 is real.

### Errors and limits

Detection thresholds need tuning after launch. Change processes can become bottlenecks if every change needs full review.

### Exercises

- **EX109 — CSF functions.** List the six CSF 2.0 functions. *Rubric:* 3 = govern, identify, protect, detect, respond, recover;; 2 = five;; 1 = three;; 0 = none.
- **EX110 — Insider export detection.** How is insider export of journey data detected? *Rubric:* 3 = alert on unusual export volume or out-of-hours exports;; 2 = volume or time;; 1 = vague;; 0 = none.
- **EX111 — Review trigger.** Which changes need security review and re-verification? *Rubric:* 3 = those touching authentication, cryptography, network rules or logging;; 2 = three;; 1 = all trivial;; 0 = none.

### Synthesis

Operational security is designed alongside the architecture, with detection derived from threats and change control that protects security properties.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Security architecture and engineering: validation

### Learning outcomes

You will (1) distinguish validation from verification; (2) validate the architecture against stakeholder needs and real use; (3) use red-team exercises and user studies as validation evidence.

### 38.1 Building the right system

Verification asked whether the system was built as specified; validation asks whether the specification meets real needs. A perfectly verified system can still fail its users or miss real threats. Sofia plans validation for the back office: review with stakeholders whether privacy needs are actually met in daily practice, observe customer service agents using the dispute screens and commission an authorised red-team exercise to test whether realistic attackers can achieve their goals despite the controls. Validation often finds problems in requirements themselves, which no amount of verification would reveal.

### 38.2 Red-team findings

An authorised red team from a specialist firm, working under written rules of engagement that exclude live passenger data and vehicles, attempts to obtain journey histories. They do not break any cryptography; instead, they phish a customer service agent and use the agent's legitimate access to look up journeys of chosen people. Every control worked as specified. The finding shows a requirement gap: agents could look up any card without a linked dispute. Sofia adds a requirement that lookups need an open case and are reviewed, which verification would never have found.

### 38.3 User studies

Sofia also observes six agents handling synthetic disputes. They find the new screens confusing and share notes in a chat tool, copying journey details outside the protected system. This is a validation failure of psychological acceptability. The team redesigns the screens to show case notes inside the system and removes the need to copy data. Sofia notes that security controls that ignore real work patterns push people into workarounds that undermine the architecture, so user studies are a security activity, not only a usability one.

### Worked example

Sofia plans validation, a red team obtains journey data via a phished agent's legitimate access revealing a requirement gap, and a user study finds data copied to chat, leading to redesigned screens.

> **Synthetic case.** The red team, agents and findings are synthetic.

### Errors and limits

Red-team exercises cover only the paths tried. Observed users may behave differently when watched.

### Exercises

- **EX112 — Validation versus verification.** How does validation differ from verification? *Rubric:* 3 = validation checks the specification meets real needs; verification checks build matches specification;; 2 = both;; 1 = same;; 0 = none.
- **EX113 — Red-team route.** How did the red team obtain journey histories? *Rubric:* 3 = phished an agent and used legitimate access to look up chosen cards;; 2 = phishing;; 1 = broke crypto;; 0 = none.
- **EX114 — Workaround cause.** Why did agents copy data to chat? *Rubric:* 3 = screens were confusing and lacked case notes;; 2 = usability;; 1 = malice;; 0 = none.

### Synthesis

Validation tests whether the architecture serves real needs and resists real attackers, revealing requirement gaps verification cannot.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Security architecture and engineering: maintainability

### Learning outcomes

You will (1) design for maintainable security over a long life; (2) plan cryptographic agility and component replacement; (3) manage technical debt in security controls.

### 39.1 Long-lived systems

Transit systems run for decades. Validators bought today may still operate in fifteen years, long after their software libraries stop receiving updates. Sofia studies maintainability: the ease of changing a system safely. For security this means the ability to patch components, rotate keys, replace algorithms and update rules without redesign. She reviews the back-office design for maintainability and finds that the tariff-verification component hard-codes one signature algorithm and one key, which would make future changes risky and slow. She proposes configuration-driven key and algorithm selection with versioned formats.

### 39.2 Cryptographic agility

Algorithms age. NIST published post-quantum standards FIPS 203, 204 and 205 in 2024, and organisations will need to migrate from current public-key algorithms over the coming years. Sofia designs the tariff-signing format with a version field and an algorithm identifier, so the back office can accept both current and future signature types during a transition. She inventories every place public-key cryptography is used, a prerequisite for planning migration. Agility does not mean supporting every algorithm; it means being able to change deliberately, with tested procedures, when change becomes necessary.

### 39.3 Security technical debt

Shortcuts accumulate: an exception granted for a demo that was never removed, a firewall rule added during an incident and forgotten, a deprecated protocol kept for one old partner. Sofia creates a security debt register listing each item, its risk, its owner and the plan to remove it. Items are reviewed quarterly, and new exceptions must have expiry dates. She presents the register to the architecture board as a normal part of maintenance, not a confession. Making debt visible lets the organisation pay it down deliberately instead of discovering it during an incident.

### Worked example

Sofia replaces a hard-coded signature algorithm with versioned, configuration-driven selection, inventories public-key use for post-quantum planning and starts a security debt register.

> **Synthetic case.** Components and debt items are synthetic; FIPS 203, 204 and 205 are real.

### Errors and limits

Agility adds complexity and downgrade risks if old algorithms remain accepted too long. Debt registers need executive attention to be effective.

### Exercises

- **EX115 — Hard-coded issue.** What maintainability problem did Sofia find in tariff verification? *Rubric:* 3 = a hard-coded signature algorithm and key;; 2 = hard-coded;; 1 = vague;; 0 = none.
- **EX116 — Agility enabler.** Which format features enable cryptographic agility for tariff signatures? *Rubric:* 3 = a version field and algorithm identifier;; 2 = both;; 1 = vague;; 0 = none.
- **EX117 — Debt register.** What does each security debt register entry include? *Rubric:* 3 = risk, owner and removal plan;; 2 = three;; 1 = vague;; 0 = none.

### Synthesis

Maintainable security plans for change in algorithms, components and rules, and keeps security debt visible.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify network segmentation against an approved flow matrix; (2) automate configuration verification; (3) report deviations with evidence.

### 40.1 Flow matrix as specification

The back office's network design defines an approved flow matrix: which zones may connect to which, on which ports. In Verification Laboratory II, Sofia verifies that the implemented firewall rules match the matrix. A rule allowing a flow not in the matrix is excess access; a matrix flow without a rule is a broken function. She exports synthetic firewall rules from the lab environment and compares them programmatically with the matrix, rather than reading hundreds of rules by eye, which is slow and error-prone. The script itself is reviewed like any other control.

### 40.2 Automated comparison

Sofia's script reads the approved matrix and the exported rules, normalises them and computes differences. The lab below runs on synthetic data and reports two excess rules, one allowing staff workstations to reach the journey database directly and one an any-to-any rule left from testing, and one missing flow from ingestion to the logging collector. The comparison runs automatically after every change, turning a one-time audit into continuous verification. She stores outputs as evidence linked to change tickets, so auditors can see when each deviation appeared and when it was closed.

### Lab — Firewall rules against the flow matrix

```python
# Compare synthetic firewall rules with an approved zone flow matrix.
approved = {("validators", "ingestion", 443), ("ingestion", "journey-db", 5432), ("ingestion", "logging", 6514),
            ("reporting", "journey-db", 5432), ("admin-jump", "ingestion", 22)}
rules = ["validators ingestion 443", "ingestion journey-db 5432", "reporting journey-db 5432",
         "admin-jump ingestion 22", "staff-ws journey-db 5432", "any any any"]
impl = {(a, b, int(p) if p != "any" else p) for a, b, p in (r.split() for r in rules)}
for x in sorted(impl - approved, key=str): print("EXCESS ", *x)
for x in sorted(approved - impl, key=str): print("MISSING", *x)
```

Run with `python3 lab_flows.py`. Verified output:

```text
EXCESS  any any any
EXCESS  staff-ws journey-db 5432
MISSING ingestion logging 6514
```

### 40.3 Reporting deviations

Each deviation becomes a finding with the rule, the matrix entry it violates, the risk and a proposed fix. The any-to-any rule is critical because it defeats segmentation entirely; the workstation-to-database rule is high, recreating the bypass found in chapter 22; the missing logging flow is medium because it silently weakens detection. Sofia's report also states what the verification covers: rule configuration, not runtime behaviour, so a follow-up test sends synthetic traffic to confirm enforcement. Verification evidence is strongest when configuration checks and behavioural tests agree.

### Worked example

Sofia compares synthetic firewall rules with the approved flow matrix, finds two excess rules and one missing flow, rates them and adds behavioural tests.

> **Synthetic case.** Zones, rules and the matrix are synthetic.

### Errors and limits

Configuration exports may not reflect rules in effect. Matrices must be kept current or verification checks the wrong target.

### Exercises

- **EX118 — Excess versus missing.** What is the difference between an excess rule and a missing flow? *Rubric:* 3 = excess allows unapproved access; missing breaks an approved function;; 2 = both;; 1 = same;; 0 = none.
- **EX119 — Lab deviations.** Which deviations did the lab report? *Rubric:* 3 = excess staff-to-journey-db and any-to-any; missing ingestion-to-logging;; 2 = three;; 1 = one;; 0 = none.
- **EX120 — Coverage statement.** What does configuration verification not cover? *Rubric:* 3 = runtime enforcement behaviour;; 2 = runtime;; 1 = everything covered;; 0 = none.

### Synthesis

Automated comparison of configurations with approved flows turns segmentation into continuously verified architecture.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Security architecture and engineering: system optimization

### Learning outcomes

You will (1) frame control selection as an optimisation under budget; (2) compare greedy and exhaustive selection on synthetic data; (3) recognise limits of numeric optimisation in security.

### 41.1 Choosing under constraints

Corvia's security budget for next year cannot fund every proposed control. Sofia frames the choice as optimisation: each candidate control has a cost and an estimated risk reduction from the risk assessment in chapter 24, and the goal is to maximise total reduction within budget. This is a version of the knapsack problem from discrete mathematics. Framing the decision this way makes assumptions explicit and lets stakeholders see why one control was preferred over another, rather than relying on whoever argues loudest in a budget meeting.

### 41.2 Greedy versus exhaustive

Sofia compares two methods on eight synthetic candidate controls. A greedy method picks controls in order of reduction per unit cost until the budget is used. An exhaustive search tries every combination, feasible here because eight items give only 256 subsets. The lab below shows that greedy selection comes close but misses the best combination, because it fills the budget with small efficient items and leaves no room for one large, valuable control. For larger problems exhaustive search becomes impossible, and engineers use better algorithms or accept approximations knowingly.

### Lab — Greedy and exhaustive control selection

```python
# Greedy vs exhaustive control selection under budget (synthetic costs and risk reductions).
from itertools import combinations
C = {"mfa-admins": (8, 10), "egress-filter": (15, 13), "log-review": (20, 14), "hsm-keys": (50, 34),
     "edr-depots": (35, 20), "phish-training": (12, 9), "backup-offline": (25, 17), "waf": (30, 15)}
B = 100
g, cost, val = [], 0, 0
for k, (c, v) in sorted(C.items(), key=lambda kv: kv[1][1] / kv[1][0], reverse=True):
    if cost + c <= B: g.append(k); cost += c; val += v
best = max((s for r in range(len(C) + 1) for s in combinations(C, r) if sum(C[k][0] for k in s) <= B),
           key=lambda s: sum(C[k][1] for k in s))
print(f"greedy:     value {val}, cost {cost}, {sorted(g)}")
print(f"exhaustive: value {sum(C[k][1] for k in best)}, cost {sum(C[k][0] for k in best)}, {sorted(best)}")
```

Run with `python3 lab_knapsack.py`. Verified output:

```text
greedy:     value 63, cost 80, ['backup-offline', 'egress-filter', 'log-review', 'mfa-admins', 'phish-training']
exhaustive: value 74, cost 98, ['backup-offline', 'egress-filter', 'hsm-keys', 'mfa-admins']
```

### 41.3 Limits of the numbers

Optimisation is only as good as its inputs. Risk-reduction estimates are uncertain, controls interact, so two controls may overlap rather than add, and some controls are mandatory for compliance regardless of score. Sofia runs the selection with low and high estimates and shows which controls are chosen in every scenario; those are robust choices. She presents the result as decision support, not a decision. Daniel adds that the exercise's main value is the conversation it forces about estimates, which often reveals that nobody knows how much a popular control actually reduces risk.

### Worked example

Sofia frames next year's controls as a budgeted knapsack problem, shows greedy selection missing the optimum on synthetic data and identifies robust choices across estimate ranges.

> **Synthetic case.** Controls, costs and reductions are synthetic.

### Errors and limits

Additive risk reduction is unrealistic when controls overlap. Mandatory controls must be fixed before optimisation.

### Exercises

- **EX121 — Problem type.** Which classic problem does budgeted control selection resemble? *Rubric:* 3 = the knapsack problem;; 2 = knapsack;; 1 = sorting;; 0 = none.
- **EX122 — Greedy shortfall.** In the lab, how did greedy selection compare with the exhaustive optimum? *Rubric:* 3 = greedy reached 63 at cost 80; the optimum was 74 at cost 98 and included hsm-keys;; 2 = both values;; 1 = equal;; 0 = none.
- **EX123 — Robust choice.** What makes a control a robust choice? *Rubric:* 3 = it is selected under both low and high estimates;; 2 = both scenarios;; 1 = highest score;; 0 = none.

### Synthesis

Optimisation frames security investment clearly, but uncertain and interacting estimates make its output advice, not a verdict.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Security architecture and engineering: applied research

### Learning outcomes

You will (1) formulate an applied research question from engineering practice; (2) design a small study using Corvia data responsibly; (3) report findings with limits.

### 42.1 A question from practice

Sofia's applied research project asks whether short-lived device certificates, introduced in chapter 31, reduced the window during which retired validators could still authenticate. The question comes from practice and matters to Corvia. She defines the outcome as days between retirement and the last successful authentication, compares devices retired before and after the change, and lists rivals such as a simultaneous improvement in asset records. Herley and van Oorschot (2017) warn against security claims that cannot be tested; her question names exactly what would show no effect.

### 42.2 Responsible data use

The study uses Corvia's operational logs, which contain device identifiers but no passenger data. Sofia agrees with Daniel and the data protection officer which fields she may use, stores extracts in an access-controlled project area and deletes them after the study. She pseudonymises device identifiers in all outputs. Even technical data can be sensitive: a list of devices that kept authenticating after retirement could guide an attacker to weak spots. Her report therefore presents aggregates and distributions, not device lists, and she shares the detailed list only with the operations owner.

### 42.3 Findings with limits

Devices retired after the change stopped authenticating within a median of two days, compared with eleven days before. The asset-record improvement happened at the same time, so Sofia cannot separate the two causes fully; she notes that devices whose asset records were already accurate before the change also improved, which weakly supports the certificate effect. She reports the finding with this limitation and recommends continued monitoring. The project teaches her that even modest engineering questions need careful design to produce trustworthy answers.

### Worked example

Sofia studies authentication after retirement before and after short-lived certificates, uses logs under agreed limits and reports a fall from eleven to two days with a confound noted.

> **Synthetic case.** Logs, devices and results are synthetic; Herley and van Oorschot (2017) is real.

### Errors and limits

Before-after designs cannot exclude simultaneous changes. Small device counts make medians unstable.

### Exercises

- **EX124 — Outcome definition.** What outcome did Sofia measure? *Rubric:* 3 = days between retirement and last successful authentication;; 2 = defined;; 1 = vague;; 0 = none.
- **EX125 — Device list caution.** Why does the report avoid listing individual devices? *Rubric:* 3 = such a list could guide attackers to weak spots;; 2 = attacker map;; 1 = no reason;; 0 = none.
- **EX126 — Confound.** What confound limits the conclusion? *Rubric:* 3 = asset-record improvements happened at the same time;; 2 = asset records;; 1 = vague;; 0 = none.

### Synthesis

Applied research turns engineering changes into tested claims when questions, data handling and limits are explicit.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a professional architecture team; (2) apply course methods under real time and budget pressure; (3) reflect on differences between study and practice.

### 43.1 Joining the team

In year five Sofia spends a semester as a junior member of Corvia's architecture team. Her tasks are real but supervised: reviewing designs submitted by project teams, maintaining the architecture model, joining threat-modelling sessions and drafting decision records. She quickly finds that projects rarely arrive with complete context statements or requirements. Much of her work is asking the questions from chapters 20 and 21 of busy project managers, politely and persistently, because the review cannot proceed without answers. Professional architecture is as much about facilitation as about technical knowledge.

### 43.2 Pressure and pragmatism

A project to add a new partner for bike-share integration must launch in three weeks. A full design process is impossible. Sofia and her supervisor agree a proportionate review: confirm the integration uses the partner gateway with scoped tokens, check the data shared against the classification, run a one-hour threat-modelling session and record two residual risks for the business owner to accept. They document what was not reviewed. Sofia learns that proportionate review, with honest records of its limits, protects the organisation better than either blocking every project or approving without looking.

### 43.3 Study versus practice

Sofia keeps a reflective journal. In study, problems were well defined and information complete; in practice, information is partial and changes weekly. In study, she owned her designs; in practice, she influences designs owned by others. Methods still apply, but in lighter forms: a quick data-flow sketch rather than a full model, a ranked risk list rather than a quantitative analysis. Her supervisor's feedback notes that her strength is clear writing and her development area is negotiation. The journal becomes part of her final portfolio.

### Worked example

Sofia reviews project designs, runs a proportionate three-week review for a bike-share integration with two accepted residual risks and records reflections comparing study and practice.

> **Synthetic case.** The team, projects and feedback are synthetic.

### Errors and limits

Proportionate reviews can miss issues; their limits must be recorded. Placement experience in one organisation may not generalise.

### Exercises

- **EX127 — Facilitation finding.** What did Sofia find much of her review work consisted of? *Rubric:* 3 = asking context and requirement questions of busy project managers;; 2 = questions;; 1 = coding;; 0 = none.
- **EX128 — Proportionate review.** What did the bike-share review include? *Rubric:* 3 = gateway and scoped tokens check, data classification check, one-hour threat model, two accepted residual risks;; 2 = three;; 1 = vague;; 0 = none.
- **EX129 — Development area.** What development area did her supervisor note? *Rubric:* 3 = negotiation;; 2 = negotiation, without explanation;; 1 = writing;; 0 = none.

### Synthesis

Professional practice applies course methods proportionately, records limits and relies on facilitation as much as technique.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define a capstone architecture problem with scope and success criteria; (2) plan the capstone's evidence; (3) secure supervisor and partner agreement.

### 44.1 Choosing the problem

For her capstone Sofia chooses the security architecture of Corvia's account-based ticketing back office, building on Design Studio II but at implementation depth for a defined slice: tap ingestion, fare calculation and dispute handling. The problem is real, bounded and assessable. She writes success criteria: all high-priority threats mitigated or accepted by owners; verification tests passing for every security requirement in scope; a recovery trial meeting a stated recovery time; and an independent review with no unresolved critical findings. Clear criteria let examiners judge success without relying on impressions.

### 44.2 Planning evidence

Sofia plans the evidence she will produce: the requirements and traceability table, threat model, control specifications, verification reports, a recovery trial report, metrics baselines and the independent review report. Each piece of evidence supports a claim in the final assurance case. She schedules them backwards from the submission date, leaving time for revisions after the independent review. Daniel warns that capstones fail more often from late evidence than from poor design, because students leave testing and documentation until the end when there is no time to fix what they reveal.

### 44.3 Agreement and boundaries

Sofia writes a capstone charter signed by her university supervisor, Daniel and Corvia's head of fare systems. It states scope, deliverables, the lab environment she may use, data restrictions and how Corvia may use her work. It excludes production changes; any implementation happens in a lab mirror. It also covers intellectual property and publication: her thesis may describe the architecture in general terms but not reveal specific weaknesses. Agreeing these points early prevents disputes later and protects both the student and the partner.

### Worked example

Sofia scopes a three-component capstone with four success criteria, schedules seven evidence items backwards from submission and signs a charter with three parties.

> **Synthetic case.** The capstone, charter and parties are synthetic.

### Errors and limits

Success criteria can be gamed if too narrow. Lab mirrors may lack production complexity.

### Exercises

- **EX130 — Success criteria.** Name two of Sofia's capstone success criteria. *Rubric:* 3 = two of threats mitigated or accepted, verification tests passing, recovery time met, review with no critical findings;; 2 = one;; 1 = vague;; 0 = none.
- **EX131 — Common failure.** Why do capstones often fail, according to Daniel? *Rubric:* 3 = evidence produced too late to fix what it reveals;; 2 = late evidence;; 1 = bad design;; 0 = none.
- **EX132 — Charter exclusion.** What does the charter exclude? *Rubric:* 3 = production changes; work happens in a lab mirror;; 2 = production;; 1 = nothing;; 0 = none.

### Synthesis

A capstone starts with a bounded problem, measurable success criteria, a planned evidence trail and a signed charter.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) respond to review findings; (3) review another student's design constructively.

### 45.1 Preparing for review

Sofia submits her capstone design package to an independent reviewer, a senior architect from another transit operator, under a confidentiality agreement. She includes a reading guide stating the scope, key decisions, known open issues and specific questions she wants examined, such as whether her replay-detection design holds at peak load. Guiding the reviewer makes the review more useful: an unguided reviewer may spend hours on minor diagrams while missing the decisions that matter most. She also lists what is out of scope so the reviewer does not assume it was forgotten.

### 45.2 Responding to findings

The reviewer returns twelve findings: one critical, four major and seven minor. The critical finding is that dispute handling lets agents adjust fares without a second approval above a threshold, repeating a pattern seen in chapter 14. Sofia fixes it with a dual-approval rule and new tests. For one major finding, about log retention, she disagrees and explains why with reference to the privacy requirements; the reviewer accepts the explanation. She records every finding, response and evidence in a table. Responding well means fixing what is right and arguing respectfully where she has evidence.

### 45.3 Reviewing others

Sofia also reviews a classmate's capstone on depot access control. She uses the same approach she valued: read the guide, focus on key decisions, classify findings by severity and suggest fixes. She finds that badge revocation depends on a nightly batch, leaving a day-long window for dismissed staff. She phrases the finding with the scenario, the impact and a suggested improvement, avoiding judgemental language. Reviewing teaches as much as being reviewed, because it trains her to see her own designs through a sceptical outsider's eyes.

### Worked example

Sofia guides an external reviewer, fixes a critical dual-approval gap, argues one major finding with evidence and reviews a classmate's depot access design.

> **Synthetic case.** Reviewers, findings and the classmate's design are synthetic.

### Errors and limits

One reviewer has blind spots; important designs benefit from several. Disagreements need evidence, not seniority.

### Exercises

- **EX133 — Reading guide.** What does Sofia's reading guide include? *Rubric:* 3 = scope, key decisions, open issues, specific questions, out-of-scope items;; 2 = three;; 1 = vague;; 0 = none.
- **EX134 — Critical finding.** What was the critical finding and its fix? *Rubric:* 3 = agents adjusting fares without second approval; dual approval above threshold;; 2 = both;; 1 = vague;; 0 = none.
- **EX135 — Classmate finding.** What weakness did Sofia find in the classmate's design? *Rubric:* 3 = nightly batch revocation leaves day-long access for dismissed staff;; 2 = batch;; 1 = vague;; 0 = none.

### Synthesis

Independent review is most valuable when guided, answered with fixes or evidence and practised in both directions.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) implement and verify the capstone slice in a lab mirror; (2) build an assurance case linking claims to evidence; (3) manage scope changes late in a project.

### 46.1 Implementation in the mirror

Sofia implements the capstone slice in a lab mirror of the back office using synthetic validators and passengers. She configures ingestion with device certificates, replay detection and signed tariff loading; fare calculation with versioned tariffs; and dispute handling with dual approval. She reruns the verification suites from chapters 30 and 40, adapted to the new design, and adds tests for findings from the independent review. All in-scope security requirements now have passing tests, with two documented exceptions where the lab cannot reproduce production hardware.

### 46.2 The assurance case

An assurance case is a structured argument that a system meets its security claims, supported by evidence. Sofia's top claim is that the back-office slice protects fare integrity and passenger privacy within the stated scope. Sub-claims cover authentic inputs, correct calculation, controlled disputes and protected data. Each sub-claim links to requirements, controls, verification results and review findings. NIST SP 800-160 Vol. 1 Rev. 1 emphasises assurance as evidence-based confidence. The case makes gaps visible: one sub-claim relies only on design review, so she adds a test.

### 46.3 Late scope changes

Two months before submission, Corvia asks her to add refunds to the capstone. Sofia assesses the change: refunds would need new requirements, threat analysis and tests, risking the quality of everything else. She proposes instead to document how the architecture would extend to refunds, without implementing it, and to list it as future work. Her supervisor and Daniel agree. Managing scope means protecting the quality of committed work; saying no with a reasoned alternative is a professional skill, not a failure to cooperate.

### Worked example

Sofia implements the slice in a lab mirror with passing tests, builds an assurance case that exposes a sub-claim lacking tests, and declines a late refund addition with a documented extension plan.

> **Synthetic case.** The lab mirror, assurance case and request are synthetic; SP 800-160 Vol. 1 Rev. 1 is real.

### Errors and limits

Assurance cases can give false confidence if evidence is weak. Lab exceptions must be validated later in production.

### Exercises

- **EX136 — Lab exceptions.** How many requirements could not be tested in the lab, and why? *Rubric:* 3 = two, because the lab cannot reproduce production hardware;; 2 = count and reason;; 1 = vague;; 0 = none.
- **EX137 — Assurance gap.** What gap did the assurance case reveal? *Rubric:* 3 = one sub-claim relied only on design review; a test was added;; 2 = review only;; 1 = vague;; 0 = none.
- **EX138 — Scope response.** How did Sofia respond to the late refund request? *Rubric:* 3 = proposed documenting the extension as future work instead of implementing;; 2 = alternative;; 1 = accepted;; 0 = none.

### Synthesis

A capstone becomes convincing when implementation, verification and an assurance case link every claim to evidence within a protected scope.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) plan a controlled failure and recovery trial; (2) measure recovery against objectives; (3) improve recovery procedures from trial evidence.

### 47.1 Planning the trial

Sofia's capstone includes a recovery trial in the lab mirror. The scenario: ransomware encrypts the fare-calculation servers, and the team must restore service from offline backups while validators continue offline. Objectives are a recovery time of four hours for fare calculation and no loss of tap records, since validators buffer them. She writes the plan with roles, steps, success criteria, safety limits and an abort procedure, and informs everyone involved. Trials are rehearsed carefully because the purpose is to learn safely, not to cause a real outage.

### 47.2 Running and measuring

During the trial, the team rebuilds servers from images, restores the database from the last offline backup, reloads verified tariff tables and replays buffered tap records. Sofia records times for each step. The lab below summarises the synthetic timings: total recovery exceeds the four-hour objective because database restore and record replay take longer than planned. No tap records are lost. Measured times replace optimistic estimates in the recovery plan, which is the main value of the trial: the plan now reflects what the team can actually do.

### Lab — Recovery trial timings

```python
# Synthetic recovery trial step timings (minutes) vs a 4-hour objective.
steps = [("declare and isolate", 20), ("rebuild servers from images", 55), ("restore database", 120),
         ("reload verified tariffs", 15), ("replay buffered tap records", 95), ("reconcile and sign-off", 20)]
total = sum(m for _, m in steps)
for s, m in steps: print(f"{s:30} {m:4d} min")
print(f"total {total} min = {total/60:.1f} h; objective 240 min; met: {total <= 240}")
print("tap records lost: 0 (validators buffered all records)")
```

Run with `python3 lab_recovery.py`. Verified output:

```text
declare and isolate              20 min
rebuild servers from images      55 min
restore database                120 min
reload verified tariffs          15 min
replay buffered tap records      95 min
reconcile and sign-off           20 min
total 325 min = 5.4 h; objective 240 min; met: False
tap records lost: 0 (validators buffered all records)
```

### 47.3 Improving the procedure

The team analyses the overrun. Database restore was slow because backups were compressed with a setting that limits parallel restore; record replay was slow because it processed records one at a time. Sofia proposes changing the backup format and batching replay, then reruns those two steps, cutting their combined time sharply. She updates the recovery runbook and schedules the next full trial. NIST CSF 2.0's recover function emphasises improving recovery planning from lessons learned, and the trial puts that principle into practice with numbers rather than opinions.

### Worked example

Sofia runs a ransomware recovery trial in the lab mirror, measures a total time over the four-hour objective with no record loss, and fixes restore and replay bottlenecks.

> **Synthetic case.** The trial, timings and fixes are synthetic; NIST CSF 2.0 is real.

### Errors and limits

Lab trials omit real-world stress and coordination problems. Backups must be tested for integrity, not only speed.

### Exercises

- **EX139 — Trial objectives.** What were the two recovery objectives? *Rubric:* 3 = fare calculation restored in four hours and no tap records lost;; 2 = both;; 1 = one;; 0 = none.
- **EX140 — Lab timing result.** What total recovery time did the lab report, and which steps overran? *Rubric:* 3 = 325 minutes (5.4 hours); database restore (120 min) and record replay (95 min) dominated;; 2 = both;; 1 = met;; 0 = none.
- **EX141 — Two fixes.** Which two fixes did Sofia propose? *Rubric:* 3 = change backup compression to allow parallel restore; batch record replay;; 2 = both;; 1 = one;; 0 = none.

### Synthesis

Recovery trials replace optimistic estimates with measured times and drive concrete improvements to recovery procedures.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) compile an evidence dossier supporting the assurance case; (2) protect evidence integrity with manifests; (3) map evidence to standards for external audiences.

### 48.1 Compiling the dossier

Sofia compiles her capstone evidence into a dossier: requirements and traceability, threat model, decision records, control specifications, verification reports, independent review responses, recovery trial report, metrics baselines and the assurance case. Each item has an identifier, date, author and the claims it supports. The dossier is organised by the assurance case structure so that an examiner can follow any claim down to its evidence. Daniel notes that the same discipline is used in regulated industries, where auditors expect to trace claims to evidence without asking engineers to explain from memory.

### 48.2 Integrity of evidence

Evidence that can be changed silently is weak. Sofia generates a manifest listing every dossier file with its SHA-256 digest, as specified in FIPS 180-4, and stores the manifest separately with her supervisor. Anyone can later verify that the dossier has not been altered since submission. The lab below builds a manifest for synthetic dossier files and verifies it, flagging a file edited after the manifest was created. For stronger guarantees the manifest itself could be signed, but for an academic submission the separately held copy is sufficient.

### Lab — Dossier manifest

```python
# SHA-256 manifest for synthetic dossier files (FIPS 180-4 via hashlib).
import hashlib
files = {"assurance_case.md": b"Claim C1 fare integrity...\n", "threat_model.md": b"STRIDE table v4\n",
         "verification_report.md": b"30 tests, 30 pass\n", "recovery_trial.md": b"total 325 min\n"}
manifest = {k: hashlib.sha256(v).hexdigest() for k, v in files.items()}
files["verification_report.md"] = b"30 tests, 30 pass (edited)\n"
for k, v in files.items():
    print(f"{k:24} {'OK' if hashlib.sha256(v).hexdigest() == manifest[k] else 'CHANGED'}")
```

Run with `python3 lab_dossier.py`. Verified output:

```text
assurance_case.md        OK
threat_model.md          OK
verification_report.md   CHANGED
recovery_trial.md        OK
```

### 48.3 Mapping to standards

External readers often ask how a design relates to known standards. Sofia adds a mapping table linking her controls to NIST SP 800-53 Rev. 5 control families and ISO/IEC 27002:2022 controls, with a note that the mapping shows coverage of topics, not certification or compliance. For example, signed tariff tables map to integrity-related controls, and access reviews for dispute agents map to access control. The mapping helps Corvia's auditors and future engineers place her work in familiar frameworks, while the note prevents readers from overstating what the mapping proves.

### Worked example

Sofia organises her dossier by assurance claim, creates a SHA-256 manifest held by her supervisor and maps controls to SP 800-53 Rev. 5 and ISO/IEC 27002:2022 with a coverage-only caveat.

> **Synthetic case.** Dossier contents are synthetic; FIPS 180-4, SP 800-53 Rev. 5 and ISO/IEC 27002:2022 are real.

### Errors and limits

Manifests detect change but not whether original evidence was sound. Mappings can be misread as compliance claims.

### Exercises

- **EX142 — Dossier organisation.** How is the dossier organised and why? *Rubric:* 3 = by assurance-case structure so any claim can be traced to evidence;; 2 = structure;; 1 = alphabetical;; 0 = none.
- **EX143 — Lab manifest result.** Which file did the dossier lab flag? *Rubric:* 3 = verification_report.md, edited after the manifest was created;; 2 = named file;; 1 = vague;; 0 = none.
- **EX144 — Mapping caveat.** What caveat accompanies the standards mapping? *Rubric:* 3 = it shows topic coverage, not certification or compliance;; 2 = coverage;; 1 = compliance;; 0 = none.

### Synthesis

An evidence dossier makes the assurance case auditable, tamper-evident and understandable in familiar standards.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis that argues from evidence; (2) present design rationale, results and limitations; (3) contribute reusable knowledge to practice.

### 49.1 The thesis argument

Sofia's thesis argues that a layered back-office architecture with authenticated inputs, versioned signed tariffs, dual-controlled disputes and rehearsed recovery can protect fare integrity and passenger privacy for account-based ticketing within stated assumptions. The thesis is not a project diary. Each chapter supports part of the argument: context and requirements, design and alternatives, implementation and verification, validation and recovery, and discussion. She writes the conclusion first as a list of claims, then checks that each chapter delivers evidence for at least one claim and that no claim lacks support.

### 49.2 Rationale and results

For each major design choice the thesis explains the alternatives considered, the criteria and the reasons, drawing on the decision records. Results include verification pass rates, the red-team and user-study findings, the recovery trial times before and after improvement, and metrics such as revocation timeliness. Sofia presents numbers with context: the recovery time improved after fixes but has been demonstrated only in a lab mirror. She references real standards such as SP 800-160 Vol. 1 Rev. 1 and SP 800-53 Rev. 5 where they informed choices, and avoids implying that following a standard guarantees security.

### 49.3 Limitations and reuse

Limitations include the lab mirror's differences from production, the synthetic passenger data, the single-organisation context and the absence of long-term operational evidence. Sofia states each with its likely effect. To make the work reusable, she generalises patterns: signed configuration with independent publication checks, revocation triggered by asset status with reconciliation, and proportionate review for fast projects. Each pattern includes when it applies and when it does not. Reusable patterns are often the most valuable output of an engineering thesis, because other engineers can adapt them without repeating the whole project.

### Worked example

Sofia structures her thesis around listed claims, presents rationale and measured results with context, states four limitations and generalises three reusable patterns.

> **Synthetic case.** Thesis content is synthetic; SP 800-160 Vol. 1 Rev. 1 and SP 800-53 Rev. 5 are real.

### Errors and limits

Patterns abstracted from one case may not transfer. Lab results need production confirmation.

### Exercises

- **EX145 — Not a diary.** How does a thesis differ from a project diary? *Rubric:* 3 = it argues claims with evidence rather than narrating events;; 2 = argument;; 1 = same;; 0 = none.
- **EX146 — Recovery context.** What context does Sofia give for the improved recovery time? *Rubric:* 3 = demonstrated only in a lab mirror;; 2 = lab only;; 1 = production;; 0 = none.
- **EX147 — Reusable pattern.** Name one reusable pattern from the thesis. *Rubric:* 3 = signed config with independent publication checks, asset-triggered revocation with reconciliation, or proportionate review;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

An engineering thesis argues from evidence, explains rationale honestly and leaves reusable patterns for practice.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend an engineering thesis before examiners and practitioners; (2) answer challenges with evidence and acknowledged limits; (3) plan professional development after graduation.

### 50.1 Preparing to defend

Sofia prepares a twenty-minute presentation focused on the problem, key decisions, evidence and limits, rather than on everything she did. She anticipates questions: why not move everything to the cloud, how the design handles a stolen tariff-signing key, whether the red-team finding means the design failed and how her patterns apply to smaller operators. For each she prepares an answer pointing to a section of the thesis or a piece of evidence in the dossier. She rehearses with Daniel and classmates, timing herself and practising short, direct answers.

### 50.2 Answering challenges

An examiner asks whether the signed-tariff design is pointless if the signing key is stolen. Sofia explains the layered design: the independent publication list maintained by finance would reveal unpublished versions, and rollback limits damage; she concedes that a coordinated compromise of both the key and finance's list would defeat the controls. A practitioner asks whether the red-team success shows failure. She answers that it validated the specification by revealing a requirement gap, which was fixed. Conceding precisely where the design stops is more convincing than claiming it cannot fail.

### 50.3 After the defense

The examiners pass the thesis with minor corrections: clarify the assurance case notation and add a paragraph on post-quantum migration timing. Sofia completes them and archives the thesis and dossier with their manifest. Daniel offers her a junior architect position at Corvia. Her development plan includes leading a full threat-modelling programme, studying the NIST post-quantum standards in depth and mentoring next year's placement student. Her reflection notes that five years taught her that security architecture is the discipline of making trade-offs explicit, evidenced and owned.

### Worked example

Sofia defends her thesis, concedes the joint key-and-list compromise limit, frames the red-team finding as validation success, completes corrections and plans her first professional year.

> **Synthetic case.** Examiners, questions and the job offer are synthetic.

### Errors and limits

Defense performance is not the same as design quality. Corrections should not change claims without new evidence.

### Exercises

- **EX148 — Presentation focus.** What does Sofia's presentation focus on? *Rubric:* 3 = problem, key decisions, evidence and limits rather than everything done;; 2 = focus;; 1 = everything;; 0 = none.
- **EX149 — Key-theft answer.** What limit does Sofia concede about stolen tariff keys? *Rubric:* 3 = a coordinated compromise of the key and finance's publication list would defeat controls;; 2 = joint compromise;; 1 = vague;; 0 = none.
- **EX150 — Final reflection.** How does Sofia summarise security architecture in her reflection? *Rubric:* 3 = making trade-offs explicit, evidenced and owned;; 2 = three parts;; 1 = technology;; 0 = none.

### Synthesis

A final defense shows mastery by explaining decisions, conceding limits precisely and turning study into professional practice.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Sofia Mbeki, Daniel Ferreira, Kestrel Polytechnic University, Corvia Regional Transit and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** That each month's increase is proportional to the current volume, so absolute growth keeps accelerating.

**EX002.** Month 24 (20.5 TB against a 20 TB budget), fifteen months before the linear forecast predicts.

**EX003.** Because it treats an exponential process as linear and underestimates future volume.

**EX004.** contractor-07, via vendor-support, field-tech and fare-ops into fare-admins: four groups deep.

**EX005.** The set of users who can create and the set who can approve must have an empty intersection.

**EX006.** Two different people colluding, one creating and one approving, which needs process controls.

**EX007.** Because attackers can physically reach, open and instrument them for long periods in a public vehicle.

**EX008.** To select evaluated secure components, such as secure elements, wherever attackers can get physical access.

**EX009.** Because network latency and connectivity gaps mean the central server cannot always answer in time.

**EX010.** A negative amount, a timestamp in the future and a card identifier with unexpected characters.

**EX011.** A short public invalid record message, and a detailed log entry with line and reason in a restricted file.

**EX012.** Because secrets draws from the operating system's cryptographically secure source, while random can be predicted.

**EX013.** Context, decision, options considered, consequences and date.

**EX014.** Wherever the level of trust changes, for example between on-vehicle devices and the depot network.

**EX015.** That a stolen card could still be used for up to an hour until the next deny-list update.

**EX016.** The total number of fraudulent attempts across the day.

**EX017.** Expected misuse falls from 12.6 to 3.1 uses per day, a quarter of the hourly figure.

**EX018.** About 0.55 exactly; the n times p shortcut gives 0.8, which overestimates because n p is not small.

**EX019.** The probability that the tap is fraud given that it was flagged.

**EX020.** About 4.5 per cent; over 95 per cent of flags were false alarms.

**EX021.** Because review times are skewed, so the mean misrepresents the typical case and the tail.

**EX022.** Because access-time differences reveal what data was recently used, enabling side channels.

**EX023.** Because they let code cross the hardware-enforced boundaries that every other control depends on.

**EX024.** Because anyone with the signing key can produce firmware that secure boot will accept.

**EX025.** They reduce what must be reviewed and let modules rely on validated inputs instead of repeating checks.

**EX026.** Applying a child discount to an adult card must be rejected.

**EX027.** Tracking components used and responding to vulnerabilities found in them.

**EX028.** Public safety, health and welfare.

**EX029.** Open, because passenger evacuation takes priority over fare enforcement.

**EX030.** Write a clear note of the specific risk to her mentor so it can be escalated.

**EX031.** It does not limit which internal systems a compromised vehicle can reach once connected.

**EX032.** An infected laptop can reach fare servers directly, and monitoring cannot distinguish normal flows.

**EX033.** On a list of the flows each zone actually needs, allowing only those.

**EX034.** Because if it were compromised, root privileges would undermine every other permission on the server.

**EX035.** Because systems drift from the baseline, and the baseline is useful only if deviations are noticed.

**EX036.** So an attacker who gains server access cannot delete the record of their actions.

**EX037.** Because they reveal individuals' home, work and travel patterns.

**EX038.** The concatenated query returned all 4 rows, while the parameterised query returned 0.

**EX039.** Because data that is never kept cannot leak, and less data is easier to protect properly.

**EX040.** Prepare the organisation, protect the software, produce well-secured software and respond to vulnerabilities.

**EX041.** Replay of refund requests for double refunds and staff approving their own refunds.

**EX042.** Design-level flaws such as the self-approval problem, which need human review.

**EX043.** A fraud group is a threat; an unauthenticated interface is a vulnerability it could exploit.

**EX044.** Refund requests are refused until authorisation can be checked.

**EX045.** Organisational, people, physical and technological.

**EX046.** Support, including patching, and retirement, including data destruction.

**EX047.** From stakeholder protection needs to security requirements, to architecture and design, to assurance that they are met.

**EX048.** It shows which design elements and verification evidence depend on that requirement.

**EX049.** By deliberately triggering it so it blocks legitimate users, turning the control into a denial of service.

**EX050.** During the attack it swung between 20 and 100 requests per minute every minute (9 direction changes), while gain 0.6 settled near 56 with 1 change.

**EX051.** Bounded adjustment sizes and minimum and maximum limits, with human review when limits are hit.

**EX052.** From business requirements expressed as attributes, such as private or available.

**EX053.** The key management service had no operational owner.

**EX054.** It shows which business attribute that control supported and is now weakened.

**EX055.** A shared vendor support account that bypasses single sign-on and multi-factor authentication.

**EX056.** Corvia never stores actual card numbers, so a breach of its systems cannot expose them.

**EX057.** Generation, storage, rotation and revocation, plus distribution and destruction.

**EX058.** Payment industry obligations require segmenting payment systems from other networks.

**EX059.** Legacy validators cannot be replaced until year five.

**EX060.** That payment tokenisation was already contracted, and that the passenger app was out of scope.

**EX061.** Refunds above fifty euros shall require approval by a second person distinct from the requester, verified by test.

**EX062.** Each tap record must carry a unique identifier, and duplicates must be detected and rejected.

**EX063.** To check her requirements for gaps; it revealed a missing log protection and review requirement.

**EX064.** Reporting read directly from the journey database instead of through an interface, bypassing access controls.

**EX065.** Encryption and authentication of the flow.

**EX066.** Either the model is outdated or the system has an unexpected flow; both must be investigated.

**EX067.** Retired validators still holding internal certificates could submit records, because certificates were not revoked.

**EX068.** Fare calculation errors after tariff changes: 0.0080 per day against 0.0010 for lost records, with the top event at 0.0090 (about 3.3 days a year).

**EX069.** Because a common cause such as a power cut can make several branches fail together.

**EX070.** They group very different risks together under labels like high.

**EX071.** Prepare for the assessment, conduct it, communicate results and maintain it.

**EX072.** A business owner with authority; engineers recommend.

**EX073.** Because buses must still charge when the depot's internet connection fails.

**EX074.** They admitted they had no answer yet and recorded it as an open issue.

**EX075.** Charger hardware limits the controller cannot override, and separation of the controller network from corporate systems.

**EX076.** Because comparing only two can hide a better middle option, and a minimal option gives a baseline.

**EX077.** Alternative A, the on-premises option, would win.

**EX078.** The pseudonymisation process becomes a single point of failure for passenger privacy.

**EX079.** Signature verification before loading, logging and alerting on unpublished versions, and rollback to the last verified table.

**EX080.** Because if the signing key were stolen, signatures would still verify, but the independent list would reveal unpublished versions.

**EX081.** A tariff table modified after signing must be rejected.

**EX082.** So hard controls are not silently dropped, and reviewers can check every requirement is implemented.

**EX083.** It was removed from repository history, rotated and recorded as an incident.

**EX084.** Because it would weaken a security requirement, which only an architecture decision can change.

**EX085.** The median number of days between device retirement and certificate revocation.

**EX086.** A median of 8 days among revoked devices, only 8 of 20 revoked within a week and 3 never revoked; encryption and logging covered 4 of 5 stores.

**EX087.** The reopen rate, to show whether tickets were closed without real fixes.

**EX088.** Whether the system was built according to its specifications.

**EX089.** Only the first authentic record; the duplicate, altered and retired-validator records were rejected.

**EX090.** Behaviour during database failover.

**EX091.** An asset record and an approved installation ticket.

**EX092.** Certificates still active for devices not in service, caused by missed integration events.

**EX093.** Compensating controls, an owner and an expiry tied to the replacement date.

**EX094.** They multiply, so the service is less available than its weakest component.

**EX095.** Overall availability rose from 0.9960 to 0.9980, about 35 to 18 hours of downtime a year, because the secret store was the weakest link.

**EX096.** Tap ingestion soft-fails using cached lists for a short time; administrative access hard-fails.

**EX097.** The ability to anticipate, withstand, recover from and adapt to adverse conditions.

**EX098.** Diversity, providing an alternative channel that does not share the main system's failure modes.

**EX099.** Because staff know services can keep running at reduced levels, so there is less pressure to pay or restore unsafely.

**EX100.** The mobility app's single long-lived shared API key, and monthly data exports to the consultancy by email.

**EX101.** Selling tickets and querying fares, but not reading journey histories.

**EX102.** It made clear which party notified affected passengers and which tokens Corvia should revoke.

**EX103.** To coordinate the team, keep a shared decision log and surface conflicts early.

**EX104.** Detailed journey data for ninety days, with aggregated fraud features kept for two years.

**EX105.** No plan for compromise of the tokenisation service's keys, and no clear owner for passenger deletion requests.

**EX106.** Verbose debug logging at account-based ticketing volumes.

**EX107.** With the same 20 per second refill, capacity 20 rejected 200 of 450 requests while capacity 200 rejected only 20.

**EX108.** A revoked token or right can keep working until the cached decision expires, up to a minute.

**EX109.** Govern, identify, protect, detect, respond and recover.

**EX110.** By alerting when exports exceed normal volume or occur outside working hours.

**EX111.** Changes affecting authentication, cryptography, network rules or logging.

**EX112.** Verification checks the system matches its specification; validation checks the specification meets real needs.

**EX113.** By phishing a customer service agent and using that agent's legitimate lookup access.

**EX114.** Because the screens were confusing and offered no place for case notes, so they used chat instead.

**EX115.** The component hard-coded one signature algorithm and one key.

**EX116.** A version field and an algorithm identifier in the signed format.

**EX117.** The item's risk, an owner and a plan to remove it.

**EX118.** An excess rule allows access not in the matrix; a missing flow blocks something the matrix requires.

**EX119.** Excess rules for staff workstations to the journey database and an any-to-any test rule, plus a missing ingestion-to-logging flow.

**EX120.** Whether rules are actually enforced at runtime, which needs behavioural traffic tests.

**EX121.** The knapsack problem: maximise value within a weight, here cost, limit.

**EX122.** Greedy reached a reduction of 63 using 80 of the budget, while the exhaustive optimum reached 74 at cost 98 by including the large hsm-keys control.

**EX123.** It is chosen in every estimate scenario, from low to high.

**EX124.** The number of days between a device's retirement and its last successful authentication.

**EX125.** Because a list of devices still authenticating after retirement could help an attacker find weak points.

**EX126.** Asset-record improvements occurred at the same time as the certificate change.

**EX127.** Asking project managers for missing context and requirements so reviews could proceed.

**EX128.** Confirming gateway use with scoped tokens, checking shared data classification, a one-hour threat-modelling session and two residual risks accepted by the owner.

**EX129.** Negotiation, alongside her strength in clear writing.

**EX130.** All high-priority threats mitigated or accepted, and verification tests passing for every in-scope requirement.

**EX131.** Because testing and documentation are left so late that problems they reveal cannot be fixed.

**EX132.** Any changes to production systems; implementation is limited to a lab mirror.

**EX133.** Scope, key decisions, known open issues, specific questions and what is out of scope.

**EX134.** Agents could adjust fares without second approval; Sofia added dual approval above a threshold with tests.

**EX135.** Badge revocation ran as a nightly batch, leaving dismissed staff up to a day of access.

**EX136.** Two, because the lab could not reproduce certain production hardware.

**EX137.** A sub-claim supported only by design review, for which Sofia added a test.

**EX138.** She proposed documenting how refunds would fit as future work rather than implementing them.

**EX139.** Restore fare calculation within four hours and lose no tap records.

**EX140.** Total recovery took 325 minutes, 5.4 hours, over the 240-minute objective, with database restore at 120 and replay at 95 minutes dominating.

**EX141.** Changing the backup format to allow parallel restore and batching the tap-record replay.

**EX142.** By the assurance case structure, so an examiner can trace each claim to its evidence.

**EX143.** verification_report.md, which was edited after the manifest was created.

**EX144.** That it shows coverage of topics only, not certification or compliance.

**EX145.** It is an argument supporting claims with evidence, not a chronological account of work.

**EX146.** That it has been demonstrated only in a lab mirror, not in production.

**EX147.** Revocation triggered by asset status changes, backed by daily reconciliation.

**EX148.** The problem, key decisions, evidence and limits, not a full account of all work.

**EX149.** That if both the signing key and finance's independent publication list were compromised together, the controls would fail.

**EX150.** As the discipline of making trade-offs explicit, evidenced and owned.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- International Organization for Standardization. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- Joint Task Force. (2018). *Risk management framework for information systems and organizations* (NIST SP 800-37 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-37r2>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., & McQuaid, R. (2021). *Developing cyber-resilient systems: A systems security engineering approach* (NIST SP 800-160 Vol. 2 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v2r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure software development framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
- The Open Group. (2016, revised 2022). *Integrating risk and security within a TOGAF enterprise architecture* (TOGAF Series Guide G152). The Open Group.
- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Josefsson, S., & Liusvaara, I. (2017). *Edwards-curve digital signature algorithm (EdDSA)* (RFC 8032). IETF. <https://www.rfc-editor.org/rfc/rfc8032>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
