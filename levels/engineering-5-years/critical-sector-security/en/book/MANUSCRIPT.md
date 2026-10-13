# Critical Infrastructure and Sector Security: Engineering Secure and Resilient Systems

- Language: English (`en`); engineering course, five years; approximately 4,000 hours of planned study (course 138 of 207 in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **draft**. Chapters 1–50 of 50 have authored teaching text; exercises EX001–EX100 (two per chapter) have matching worked results; seventeen offline labs are embedded with their verified output. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. The plan's target of three exercises per chapter is not yet met. Draft-chapter coverage is not a completed book.
- Audience: future security systems designers for critical services — water, electricity, healthcare, transport, finance and communications. Entry knowledge: secondary-school mathematics and physics; the book builds calculus, probability, programming, networks and systems engineering from Chapter 1.
- Relation to the other books in this area: the [master's book](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) teaches how to design, pilot and defend one ethically reviewed empirical study; the [doctoral book](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) asks for an original, independently validated contribution to knowledge. **This engineering book is about building things**: deriving requirements from consequences, choosing architectures, implementing and verifying controls, measuring reliability and performance, trialling recovery and defending a designed system with evidence. Its research chapter (42) exists to settle design decisions, not to publish.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights and are not relicensed here.
- Educational boundary: this course is an independent educational blueprint. It is not an accredited engineering degree, grants no professional licence and grants no authority to access, scan, test or modify any real infrastructure. Every organisation, site, device, address, person and number in a worked example is **synthetic** unless a sentence explicitly cites a public source. Nothing here is an operational procedure for a real utility, hospital or operator, and nothing is legal advice.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

The fifty chapters follow the ten semesters of the plan. **Chapters 1–10** build the mathematical, physical, computing and professional foundations, each applied to an infrastructure problem from the first page. **Chapters 11–19** cover networks, operating systems, data, software engineering, security fundamentals, systems engineering, control, security architecture, and identity and cryptography. **Chapter 20** sets the sector context. **Chapters 21–42** are the field core: requirements, models, threat and failure analysis, methods, architectures, controls, implementation, measurement, reliability, safety and resilience, integration, performance, operations, validation, maintainability, optimisation and applied research, with two design studios (25, 35) and two verification laboratories (30, 40). **Chapters 43–50** are practice and the capstone sequence: placement, capstone, independent review, failure and recovery trial, evidence dossier, thesis and defense.

Every chapter has learning outcomes, teaching sections with definitions, a worked example, a practical activity, common errors and limits, two exercises and a synthesis. Seventeen chapters embed an offline lab written for the Python 3 standard library; the printed outputs were produced by running the code. Write your answer before opening the [worked results](#worked-results).

Keep four labels in your engineering notes: **requirement** (what must be true, verifiably), **design decision** (what was chosen, why, and what would change it), **evidence** (test, analysis, trial or review that supports a claim, with its version) and **residual risk** (what remains, and who owns it). The commonest failure at engineering level is not a wrong calculation; it is a claim that no evidence supports, or a residual risk nobody owns.

### The synthetic design case used in this book

The book follows one invented programme from first principles to final defense.

| Synthetic element | Role | Boundary |
|---|---|---|
| **Lowmarsh Regional Water Authority (LRWA)** — Fenwick water treatment works, pumping stations PS1–PS6, the 4,000 m³ Hollin Hill service reservoir, a control room and SCADA servers, private LTE telemetry, 42 field stations | The system being engineered | Invented utility; no real site, network or staff |
| **St Brenna's Hospital** | Critical customer fed by Hollin Hill (via PS3) and directly by PS4; about 4 h of on-site storage | Invented |
| **Telemetry Modernisation and Resilience Programme (TMRP)** | The design programme; needs N1–N4 and requirements R1–R9 (Chapters 16, 21) | Invented |
| Grid feeders F1 and F2, the LTE carrier, RTU vendors (RTU-A legacy, RTU-B new) | Dependencies and suppliers | Invented; no real product is described |
| All addresses (10.x.x.x), keys, probabilities, costs and lab outputs | Teaching data | Synthetic; the demo key in Lab 8 is published and must never be used |

### Source policy

Every factual statement about a law, standard, incident or published study links to a source consulted in October 2026. Laws and standards change: re-verify versions and dates before relying on them. Standard engineering knowledge (Ohm's law, Little's law, the definition of a derivative) is stated without a citation or with a classic reference. Incidents are described only at the level of their cited public sources, and where an early account was revised (Oldsmar), both are cited. Standards behind paywalls (IEC 62443, IEC 61508) are cited by their public catalogue or overview pages; do not quote clauses you have not read.

## Contents


1. [Calculus I](#ch-01)
2. [Discrete mathematics](#ch-02)
3. [Physics for computing](#ch-03)
4. [Programming I](#ch-04)
5. [Engineering communication](#ch-05)
6. [Calculus II](#ch-06)
7. [Probability and statistics](#ch-07)
8. [Computer architecture](#ch-08)
9. [Programming II](#ch-09)
10. [Engineering ethics and safety](#ch-10)
11. [Networks and protocols](#ch-11)
12. [Operating systems](#ch-12)
13. [Data systems](#ch-13)
14. [Software engineering](#ch-14)
15. [Security fundamentals](#ch-15)
16. [Systems engineering](#ch-16)
17. [Control and feedback basics](#ch-17)
18. [Security architecture](#ch-18)
19. [Identity and cryptography](#ch-19)
20. [Critical infrastructure and sector security: engineering context](#ch-20)
21. [Critical infrastructure and sector security: requirements](#ch-21)
22. [Critical infrastructure and sector security: system and data models](#ch-22)
23. [Critical infrastructure and sector security: threat and failure analysis](#ch-23)
24. [Critical infrastructure and sector security: methods I](#ch-24)
25. [Design studio I](#ch-25)
26. [Critical infrastructure and sector security: architecture alternatives](#ch-26)
27. [Critical infrastructure and sector security: control design](#ch-27)
28. [Critical infrastructure and sector security: implementation I](#ch-28)
29. [Critical infrastructure and sector security: measurement](#ch-29)
30. [Verification laboratory I](#ch-30)
31. [Critical infrastructure and sector security: implementation II](#ch-31)
32. [Critical infrastructure and sector security: reliability](#ch-32)
33. [Critical infrastructure and sector security: safety and resilience](#ch-33)
34. [Critical infrastructure and sector security: integration](#ch-34)
35. [Design studio II](#ch-35)
36. [Critical infrastructure and sector security: performance and scale](#ch-36)
37. [Critical infrastructure and sector security: operations](#ch-37)
38. [Critical infrastructure and sector security: validation](#ch-38)
39. [Critical infrastructure and sector security: maintainability](#ch-39)
40. [Verification laboratory II](#ch-40)
41. [Critical infrastructure and sector security: system optimization](#ch-41)
42. [Critical infrastructure and sector security: applied research](#ch-42)
43. [Industry or public-service practice](#ch-43)
44. [Engineering capstone I](#ch-44)
45. [Independent design review](#ch-45)
46. [Engineering capstone II](#ch-46)
47. [Failure and recovery trial](#ch-47)
48. [Evidence dossier](#ch-48)
49. [Engineering thesis](#ch-49)
50. [Final defense](#ch-50)

The [worked results](#worked-results) contain EX001–EX100. A [glossary](#glossary) and [references](#references) close the book.


<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes and connection

After this chapter you can (1) read a rate of change as the physical quantity an operator watches — cubic metres per hour leaving a reservoir, megawatts ramping on a feeder; (2) compute a derivative and a definite integral for the smooth demand curves used in infrastructure planning; (3) solve "how long until…" problems by integrating a rate and finding the time at which the accumulated quantity reaches a limit; and (4) explain why the average-rate shortcut can overstate hold-up time. The chapter starts the book's design case and prepares Chapter 6, where the same reservoir becomes a differential equation with inflow and control.

### 1.1 Why an infrastructure engineer needs calculus

Critical services are stocks and flows. A reservoir is a stock of treated water; pumps and consumers are flows. A battery bank is a stock of energy; the load is a flow. A hospital fuel tank, a gas line-pack, a queue of unprocessed telemetry messages: each is an amount that changes at a rate. Security and resilience questions are almost always questions about these quantities under stress. *If the pumps stop because their control network is down, how many hours of supply remain?* *If an attacker can hold a valve open, how fast does the level rise?* The answer is never a single number from a data sheet; it is an integral of a rate over time, compared with a limit that matters to people.

The derivative $dV/dt$ is the instantaneous rate at which a quantity $V$ changes. If $V(t)$ is the volume in a reservoir in cubic metres and $t$ is in hours, $dV/dt$ is in m³/h. The definite integral $\int_a^b q(t)\,dt$ of a flow $q$ is the total amount moved between times $a$ and $b$. The **fundamental theorem of calculus** links the two: if $V' = -q$, then $V(b) - V(a) = -\int_a^b q(t)\,dt$. Every hold-up calculation in this book is that sentence applied to a real stock.

### 1.2 Derivatives you will use

You need a small toolkit: the derivative of a polynomial ($d/dt\, t^n = n t^{n-1}$), of the exponential ($d/dt\, e^{kt} = k e^{kt}$), of sine and cosine ($d/dt \sin(\omega t) = \omega\cos(\omega t)$), the product and chain rules, and the idea of a stationary point where $f'(t) = 0$. Daily demand on a water network is often approximated by a mean plus a sinusoid with a 24-hour period. If $d(t) = 150 + 60\sin(2\pi t/24)$ m³/h, then $d'(t) = 60\cdot(2\pi/24)\cos(2\pi t/24) \approx 15.7\cos(2\pi t/24)$ m³/h², so demand rises fastest — by about 15.7 m³/h every hour — when the cosine is 1. That slope matters to a pump controller: if the pumps can only ramp at 10 m³/h², they will lag the demand at its steepest.

### 1.3 Integrals and accumulated quantities

The antiderivative of the demand above is $D(t) = 150t - \frac{60\cdot 24}{2\pi}\cos(2\pi t/24) + C$. The water drawn from time 0 to $T$ is $D(T) - D(0) = 150T - \frac{1440}{2\pi}(\cos(2\pi T/24) - 1)$. Notice what the sinusoid does: over a whole day it cancels, so the daily total is just $150 \times 24 = 3600$ m³; but over part of a day it does not cancel, and *when* the outage starts changes how long the stock lasts.

To answer "when does the reservoir reach its minimum safe level?", set the drawn volume equal to the usable volume and solve for $T$. Most such equations have no closed-form solution, so engineers solve them numerically. **Bisection** halves an interval that is known to contain the answer until it is small enough; it is slow but cannot fail if the function is continuous and the starting interval brackets the root.

### 1.4 Worked example: Hollin Hill hold-up time (synthetic)

**This case is synthetic.** The book follows the invented **Lowmarsh Regional Water Authority (LRWA)**, which runs the Fenwick water treatment works, six pumping stations (PS1–PS6) and the 4,000 m³ Hollin Hill service reservoir that feeds, among other customers, St Brenna's Hospital. LRWA is starting a **Telemetry Modernisation and Resilience Programme (TMRP)**; you are on the engineering team.

Suppose a fault in the telemetry network stops the pumps feeding Hollin Hill at 06:00 (t = 0), when the reservoir holds 3,400 m³ (85%). Operations policy treats 20% (800 m³) as the floor below which pressure and fire-fighting reserves are at risk. Demand is $d(t)$ above, with t = 0 at 06:00. The usable volume is 2,600 m³. A planner who divides by mean demand gets 2,600/150 = 17.3 hours. Integrating the actual curve gives about **14.6 hours**, because the outage begins as demand climbs into its morning and midday peak. The 2.7-hour difference is not rounding; it is the difference between dispatching a generator crew in time and not.

### 1.5 Practical activity: Lab 1

Run the lab with the Python 3 standard library. It finds the exact time by bisection, compares forward-Euler time-stepping at three step sizes, and prints the average-rate estimate.

```python
# Lab 1 - how long does Hollin Hill reservoir last after the pumps stop? (synthetic, offline)
import math
V0, VMIN = 3400.0, 800.0          # m3: start at 85% of 4000, alarm floor at 20%
def demand(t):                     # m3/h, t in hours after the pumps stop (t=0 is 06:00)
    return 150.0 + 60.0 * math.sin(2 * math.pi * t / 24)
def drawn(t):                      # exact integral of demand from 0 to t
    return 150.0 * t - (60.0 * 24 / (2 * math.pi)) * (math.cos(2 * math.pi * t / 24) - 1)
lo, hi = 0.0, 48.0
for _ in range(60):                # bisection on drawn(t) = V0 - VMIN
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if drawn(mid) < V0 - VMIN else (lo, mid)
print(f"exact time to 20%: {lo:.2f} h")
for dt in (1.0, 0.1, 0.01):        # forward Euler
    v, t = V0, 0.0
    while v > VMIN:
        v -= demand(t) * dt; t += dt
    print(f"Euler dt={dt:<5} reaches 20% at {t:.2f} h")
print(f"constant-average model (150 m3/h): {(V0 - VMIN) / 150:.2f} h")
print(f"dV/dt at t=6 h: {-demand(6):.1f} m3/h")
```

Expected output:

```text
exact time to 20%: 14.62 h
Euler dt=1.0   reaches 20% at 15.00 h
Euler dt=0.1   reaches 20% at 14.70 h
Euler dt=0.01  reaches 20% at 14.63 h
constant-average model (150 m3/h): 17.33 h
dV/dt at t=6 h: -210.0 m3/h
```

Euler with a one-hour step overstates the time by about 0.4 h; at 0.01 h it agrees with the exact answer to two decimals. The derivative at t = 6 h is −210 m³/h: the steepest drain in the window.

Before trusting the lab, check that its numbers agree with the worked example: the exact time should match the integrated hold-up for Hollin Hill, and the average-rate line should reproduce the planner's longer estimate. If you change the start time, keep the floor at 800 cubic metres so the comparison stays fair. A result that only appears at one step size is a property of the method, not of the reservoir.

### 1.6 Common errors and limits

- Using a mean rate for a time-varying flow over less than a full cycle.
- Mixing units (litres per second against cubic metres per hour: 1 L/s = 3.6 m³/h).
- Ignoring that "usable" volume excludes dead storage and reserves.
- Trusting a numerical method without checking it against a smaller step or an exact case.
- Treating the demand model as fact. A sinusoid is a planning approximation; real demand has weekday, weather and event effects, and demand during an emergency may fall (conservation notices) or rise (people storing water).

### Exercises — chapter 1

**EX001 — Peak slope.** *Objective:* use a derivative to compare demand with equipment limits. *Inputs:* $d(t)$ from §1.2; pumps that can ramp at most 12 m³/h per hour. *Steps:* (1) find $d'(t)$; (2) find its maximum and the clock time it occurs if t = 0 is 06:00; (3) decide whether the pumps can follow demand everywhere. *Expected evidence:* derivation and a one-sentence engineering conclusion. *Rubric:* 3 = correct derivative, maximum and time, conclusion links slope to ramp limit; 2 = one slip; 1 = derivative only; 0 = none.

**EX002 — Hold-up from a different start.** *Objective:* show that start time matters. *Inputs:* Lab 1. *Steps:* change the demand so that the outage starts at 18:00 (replace `sin(2πt/24)` with `sin(2π(t+12)/24)`), rerun, and compare with the 06:00 result and the average-rate estimate. *Expected evidence:* three numbers and a 100-word recommendation on which value an emergency plan should quote. *Rubric:* 3 = correct numbers and a recommendation to plan on the worst credible start time, with the reason; 2 = numbers right, weak recommendation; 1 = not run; 0 = none.

### Chapter synthesis

Infrastructure is stocks and flows. A derivative is a rate you can compare with what equipment can do; an integral is an amount you can compare with a limit that protects people. Hold-up time is an integral solved for its upper bound, usually numerically, and it depends on when the disruption starts. Check numerical results against an exact or finer solution, keep units explicit, and never let an average stand in for a curve when the curve is what the outage will meet.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes and connection

After this chapter you can (1) write interlock and permissive conditions as Boolean expressions and check them exhaustively with a truth table; (2) model infrastructure dependencies as a directed graph and compute what fails when one node fails; (3) use sets, relations and counting to bound how many states a control system can be in; and (4) state precisely when an exhaustive check is feasible and when it is not. The chapter builds on Chapter 1's stock-and-flow view and prepares Chapter 4, where you will implement these models in code.

### 2.1 Logic is the language of permissives

Control systems are full of rules of the form "the pump may run only if…". Write them as Boolean expressions. Let $H$ = level above high limit, $S$ = suction pressure low, $P$ = remote permit present, $M$ = local manual selected. A typical rule is $\text{RUN} = \neg H \wedge \neg S \wedge (P \vee M)$. Two rules are equivalent if they agree on every input; De Morgan's laws ($\neg(A\wedge B) = \neg A \vee \neg B$) let you rewrite trip conditions as permissives. With four inputs there are $2^4 = 16$ states, and a truth table checks every one. Security engineering adds a question safety engineering already asks: *which input can an attacker influence?* If $P$ arrives over a network, then $P \vee M$ means a forged permit is sufficient to start the pump whenever $H$ and $S$ are false. That may be acceptable — the physical trips still hold — or it may not, if running at that moment causes a pressure transient.

### 2.2 Graphs model dependency

A **directed graph** $G = (V, E)$ has nodes and arrows. Draw an arrow from $a$ to $b$ when $a$ needs $b$ to function. The set of things impacted when $b$ fails is everything that can reach $b$ along arrows — its **ancestors** in this orientation. Breadth-first search computes that set in time proportional to the number of edges. [Rinaldi, Peerenboom and Kelly (2001)](https://doi.org/10.1109/37.969131) distinguish physical, cyber, geographic and logical interdependencies between infrastructures; a dependency graph is the simplest model that can hold all four, as long as you label each edge with its type.

Graph vocabulary you will use: **path**, **cycle** (a loop of dependency — for example, the telemetry network needs grid power and the grid operator's restoration needs telemetry), **in-degree** and **out-degree**, **cut vertex** (a node whose removal disconnects the graph) and **strongly connected component**. A cut vertex in a supply graph is a single point of failure.

### 2.3 Counting, state spaces and their limits

A system with $n$ binary inputs has $2^n$ input states; with 30 inputs that is over a billion. Add internal memory (timers, latches) and the state space grows faster. Exhaustive checking is excellent for small interlocks and impossible for whole plants; for those you use structure (decomposition, invariants) and sampling (Chapter 30). The **pigeonhole principle** gives quick security bounds: a 16-bit message counter wraps after 65,536 messages, so at one message per second it repeats within about 18 hours, after which a replay check based only on that counter fails.

### 2.4 Worked example: Lowmarsh dependencies (synthetic)

LRWA's engineers list what St Brenna's Hospital supply depends on: Hollin Hill reservoir and the direct feed from PS4; Hollin Hill depends on PS3; each pump station needs grid power and its RTU; both RTUs talk over a private LTE network that is itself powered from grid feeder F1. Lab 2 encodes this and computes the impact set of each failure. Losing feeder F1 takes out the LTE network as well as PS3 — so the "redundant" telemetry for PS4, which is on feeder F2, is lost too. The two-feeder design looked diverse on the electrical drawing; the graph shows a common dependency through communications.

### 2.5 Practical activity: Lab 2

```python
# Lab 2 - dependency closure and an interlock truth table (synthetic Lowmarsh assets, offline)
from collections import deque
from itertools import product
DEPENDS = {  # asset: assets it needs in order to work
    "hospital_supply": ["hollin_res", "ps4"],
    "hollin_res": ["ps3"], "ps4": ["grid_f2", "rtu4"], "ps3": ["grid_f1", "rtu3"],
    "rtu3": ["lte"], "rtu4": ["lte"], "lte": ["grid_f1"], "fenwick_wtw": ["grid_f1", "chlorine"],
    "ps3_feed": ["fenwick_wtw"],
}
def impacted(failed):
    users = {}
    for a, ds in DEPENDS.items():
        for d in ds: users.setdefault(d, []).append(a)
    seen, q = {failed}, deque([failed])
    while q:
        n = q.popleft()
        for u in users.get(n, []):
            if u not in seen: seen.add(u); q.append(u)
    return sorted(seen - {failed})
for f in ("grid_f1", "lte", "grid_f2", "chlorine"):
    print(f"{f:9} -> {impacted(f)}")
# Pump P3 may run iff level below high AND suction not low AND (remote permit OR local manual)
rows = [(h, s, p, m, (not h) and (not s) and (p or m)) for h, s, p, m in product([0, 1], repeat=4)]
print("states allowing run:", sum(r[4] for r in rows), "of", len(rows))
```

Expected output:

```text
grid_f1   -> ['fenwick_wtw', 'hollin_res', 'hospital_supply', 'lte', 'ps3', 'ps3_feed', 'ps4', 'rtu3', 'rtu4']
lte       -> ['hollin_res', 'hospital_supply', 'ps3', 'ps4', 'rtu3', 'rtu4']
grid_f2   -> ['hospital_supply', 'ps4']
chlorine  -> ['fenwick_wtw', 'ps3_feed']
states allowing run: 3 of 16
```

Only 3 of 16 input states allow the pump to run: those with $H = S = 0$ and at least one of $P, M$.

Read the impact list for feeder F1 slowly. It contains the LTE network, both RTUs and PS4, even though PS4 itself is powered from feeder F2, because PS4's RTU reaches the control room only through LTE. That is the hidden common dependency the worked example describes. The truth table result is equally concrete: three of sixteen states allow the pump to run, and every one of them needs the high-level and low-suction inputs to be false, so a forged remote permit alone can never start the pump into a trip condition.

### 2.6 Common errors and limits

- Drawing arrows in mixed directions ("feeds" versus "depends on") in one graph.
- Treating two paths as redundant without checking shared nodes further down.
- Testing an interlock with "typical" cases only, when the table is small enough to test all.
- Forgetting that a graph models *whether* something works, not *how well*: degraded modes need weights or states (Chapter 22).
- Counter and identifier sizes chosen without counting how long until they wrap.

At LRWA these mistakes have direct consequences: a graph that mixes arrow directions would report that losing PS4 harms feeder F2, and a review that stopped at the electrical drawing would have missed the shared LTE dependency entirely.

### Exercises — chapter 2

**EX003 — Interlock rewrite.** *Objective:* manipulate Boolean expressions and reason about network-borne inputs. *Inputs:* RUN in §2.1. *Steps:* (1) write the trip condition $\neg\text{RUN}$ in sum-of-products form using De Morgan's laws; (2) list the states in which a forged remote permit changes the outcome; (3) propose a change that keeps remote operation but requires a second, independent condition. *Expected evidence:* expressions, list and proposal. *Rubric:* 3 = correct algebra, exactly the right states, proposal independent of the same network path; 2 = one slip; 1 = algebra only; 0 = none.

**EX004 — Diversity check.** *Objective:* find hidden common dependencies. *Inputs:* Lab 2. *Steps:* (1) add a battery-backed satellite link `sat` that only RTU4 uses, with no grid dependency; (2) rerun and report the impact of `grid_f1`; (3) state whether the hospital supply now survives loss of F1 and what the graph still does not tell you. *Expected evidence:* modified dictionary, output, two sentences. *Rubric:* 3 = correct modelling (rtu4 depends on lte *or* sat requires noting that this simple graph models AND-dependencies only), conclusion honest about that limit; 2 = correct output, limit missed; 1 = not run; 0 = none.

### Chapter synthesis

Write rules as logic and dependencies as graphs, then let the computer check them. Small interlocks can and should be checked exhaustively; whole systems cannot, and the counting tells you so. Look for shared nodes behind apparently diverse paths, label edges with their type, and ask of every input which ones arrive over a network an adversary might reach.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 50

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes and connection

After this chapter you can (1) use Ohm's law, power and energy to size backup supplies for control and communication equipment; (2) explain signal propagation, noise and attenuation well enough to read a link budget; (3) relate heat, temperature and component life to the reliability of field cabinets; and (4) identify physical side channels and electromagnetic effects that matter to security. It builds on Chapters 1–2 and prepares Chapter 8 (computer architecture) and Chapter 11 (networks).

### 3.1 Electricity for the systems engineer

Voltage $V$ (volts) drives current $I$ (amperes) through resistance $R$ (ohms): $V = IR$. Power is $P = VI$ watts; energy is power integrated over time, $E = \int P\,dt$, usually quoted in watt-hours. A field RTU drawing 0.5 A at 24 V uses 12 W; with an LTE modem at 6 W and a small Ethernet switch at 8 W the cabinet load is 26 W. A 24 V, 40 Ah battery stores nominally 960 Wh; usable energy is lower because batteries should not be fully discharged and capacity falls with age and cold. With a usable fraction of 0.6 and 85% conversion efficiency, the cabinet runs for $960 \times 0.6 \times 0.85 / 26 \approx 18.8$ hours. That number is a **security requirement**, not a maintenance detail: if a power outage is part of an attack, telemetry that dies after two hours blinds the operator exactly when needed. The **Ukrainian grid attack of December 2015** included disabling uninterruptible power supplies at control centres, according to the [E-ISAC and SANS defense use case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and) and the [CISA alert IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01).

### 3.2 Signals, noise and links

Signals travel through copper at a significant fraction of the speed of light, through fibre at roughly two-thirds of it, so a 100 km fibre adds about 0.5 ms one way — small compared with protocol and queueing delays (Chapter 36). Radio links lose power with distance and obstruction; engineers express gains and losses in decibels (dB), where +3 dB is about double the power and +10 dB ten times. A link budget adds transmitter power and antenna gains and subtracts path and cable losses; the remainder above the receiver's sensitivity is the **fade margin**. [Shannon (1948)](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x) showed that a channel's capacity depends on bandwidth and signal-to-noise ratio, $C = B\log_2(1 + S/N)$. The security consequence: a jammer does not need to break any cryptography; it only needs to reduce $S/N$ below what the link needs. Availability of radio telemetry is a physical property before it is a cryptographic one.

### 3.3 Heat and lifetime

Electronic components fail faster when hot. A widely used engineering rule of thumb, derived from the Arrhenius relation, is that many failure mechanisms roughly double in rate for each 10 °C rise; treat it as a heuristic to be replaced by the manufacturer's data. A sealed roadside cabinet in summer sun can be far hotter than the air. Design implications: derate, ventilate or cool, and monitor cabinet temperature — a sudden rise can also indicate a door left open.

For LRWA's roadside cabinets, the temperature sensor should report to SCADA alongside the battery voltage, so a rising trend is visible before components age early.

### 3.4 Physics and security

Physical effects leak information and allow faults. Power consumption and electromagnetic emanations can reveal cryptographic keys (side channels); voltage or clock glitches can make a processor skip instructions; DRAM rows disturbed by repeated access can flip bits in neighbours, as [Kim et al. (2014)](https://doi.org/10.1109/ISCA.2014.6853210) demonstrated. In infrastructure, physical access to field cabinets is often easier than network access, so these attacks are not exotic. Tamper switches, sealed enclosures and keys held off-device are the physical controls.

At LRWA, the cabinet at each pumping station holds the RTU and, after TMRP, its key store.

### 3.5 Worked example: PS4 cabinet hold-up (synthetic)

LRWA's TMRP requirement R5 says field telemetry must survive a 24-hour grid outage. PS4's planned cabinet draws 26 W. Required usable energy at 85% efficiency is $26 \times 24 / 0.85 \approx 734$ Wh; at a 0.6 usable fraction, nominal capacity must be at least $734/0.6 \approx 1{,}224$ Wh, or about 51 Ah at 24 V. Engineers round up to a standard 65 Ah bank to allow for ageing (capacity often specified to end-of-life at 80%: $65 \times 0.8 = 52$ Ah, which still meets the requirement). A design that met R5 only when the battery was new would fail it in year three.

### 3.6 Practical activity

Without code: build a spreadsheet or a ten-line script that computes battery hold-up from load (W), nominal capacity (Wh), usable fraction, efficiency and end-of-life capacity factor. Reproduce §3.5, then add a 15 W cabinet heater that runs whenever the outdoor temperature is below 0 °C and recompute.

Use the 26 W cabinet load, 85% efficiency, 0.6 usable fraction and 80% end-of-life factor from the worked example, so your first result reproduces the 65 Ah choice. Then add the heater and see how much the requirement grows. Write the answer as a requirement check, not a single number: state whether the bank still meets R5's 24 hours at end of life in cold weather, and what you would change if it does not. Keep your units visible in every column.

### 3.7 Common errors and limits

- Sizing for nameplate battery capacity rather than end-of-life, cold, usable capacity.
- Forgetting that the communications path (cellular base stations, fibre repeaters) has its own power dependency outside your control.
- Treating cryptographic protection as availability protection.
- Rules of thumb (10 °C doubling) used as precise predictions.

Each of these errors would make R5 look met on paper while failing it in practice. Sizing for a new battery is the commonest, because the shortfall only appears in year three. Forgetting the carrier's power dependency matters at LRWA because the LTE network shares feeder F1 with PS3. Treating encryption as availability protection is the misunderstanding EX006 asks you to correct, and a rule of thumb used as a prediction gives a precise-looking number with no real basis behind it.

### Exercises — chapter 3

**EX005 — Hold-up with heater.** *Objective:* size energy storage with a conditional load. *Inputs:* §3.5–3.6. *Steps:* compute the required nominal capacity at end of life if the 15 W heater runs for 10 of the 24 hours. *Expected evidence:* calculation with units. *Rubric:* 3 = correct energy, efficiency, usable and end-of-life factors applied; 2 = one factor missing; 1 = units wrong; 0 = none.

**EX006 — Jamming versus encryption.** *Objective:* separate confidentiality/integrity from availability. *Inputs:* a design review comment: "LTE telemetry is encrypted, so radio attacks are mitigated". *Steps:* write a 150-word reply that explains what encryption does and does not mitigate and proposes two physical or architectural controls. *Expected evidence:* reply. *Rubric:* 3 = jamming and S/N reasoning, controls that address availability (diverse path, local autonomy, detection of link loss); 2 = controls generic; 1 = misconception kept; 0 = none.

### Chapter synthesis

Power, signal and heat are where cyber meets physical. Size backup energy for end-of-life conditions and the full outage the threat model includes; treat radio availability as a matter of signal-to-noise, not cryptography; design cabinets for heat; and remember that physical access opens side channels and fault attacks that no firewall sees.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 50

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes and connection

After this chapter you can (1) write small, correct Python programs with functions, loops, conditionals, bytes and dictionaries; (2) implement a published algorithm — the Modbus RTU CRC-16 — and test it against a known vector; (3) parse untrusted binary input defensively, rejecting rather than repairing malformed data; and (4) explain why parsing code is security-critical in infrastructure. It turns Chapter 2's logic into code and prepares Chapter 9.

### 4.1 Programs as precise descriptions

A program is a description of a computation precise enough for a machine. Infrastructure software must be precise about three things beginners blur: **types** (a byte is not a character; an integer register is not a float), **boundaries** (what happens at the first and last element, at zero, at the maximum) and **failure** (what the program does with input it did not expect). Python is used in this book because its standard library covers bytes, hashing and simulation without installation. Its `bytes` type is immutable and indexable to integers; `int.from_bytes(b, "big")` converts with an explicit byte order.

### 4.2 Implementing a protocol checksum

Modbus is a long-lived industrial protocol; its serial form (RTU) ends each frame with a 16-bit cyclic redundancy check, sent low byte first, as defined in the [Modbus Application Protocol and serial-line specifications published by the Modbus Organization](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf). A CRC detects accidental corruption — noise on a serial line — with high probability. It is **not** a security mechanism: anyone can compute a valid CRC for a forged frame. Learn the difference early: integrity against nature versus integrity against an adversary (Chapter 19).

The standard Modbus CRC starts at 0xFFFF, XORs each byte into the low bits and shifts right eight times, XORing with 0xA001 when the shifted-out bit is 1. A widely published test vector is the request `01 03 00 00 00 0A` (unit 1, read 10 holding registers from address 0), whose CRC bytes are `C5 CD`. Testing against a vector before using your function is non-negotiable.

### 4.3 Defensive parsing

A parser that reads data from a field device, a network or a file is the boundary between the outside world and your program's assumptions. Rules: check length before indexing; check integrity (CRC) before trusting any field; check every field against what you asked for (unit, function, byte count); check values against physical limits; on any failure, **reject and report** — do not guess. The OWASP and CWE lists of common weaknesses ([CWE Top 25](https://cwe.mitre.org/top25/)) are dominated by input-handling errors: out-of-bounds reads and writes, improper input validation, integer overflow.

### 4.4 Worked example: reading Hollin Hill level (synthetic)

LRWA's RTU at PS3 returns two registers: reservoir level in centimetres and outlet pressure in kPa. Lab 3 builds the request frame, then parses five responses: a good one, a single-bit flip, a Modbus exception, a value outside the physical range of the tank (65535 cm — an uninitialised register) and a truncated frame. Each bad case is rejected with a reason that an operator or log analyst can act on.

Every rejection reason is written so that it points to a cause: a CRC failure suggests line noise, an exception points to the RTU's own state, and a range failure suggests a fault or an uninitialised register that maintenance should investigate.

### 4.5 Practical activity: Lab 3

```python
# Lab 3 - Modbus RTU CRC-16 and a defensive response parser (offline)
def crc16(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return crc
def frame(body: bytes) -> bytes:
    c = crc16(body); return body + bytes([c & 0xFF, c >> 8])   # low byte first
req = frame(bytes.fromhex("01030000000A"))
print("request:", req.hex(" "))
def parse(resp: bytes, unit=1, count=2, lo=0, hi=4000):
    if len(resp) < 5: return "reject: short"
    if crc16(resp[:-2]) != resp[-2] | resp[-1] << 8: return "reject: crc"
    if resp[0] != unit: return "reject: unit"
    if resp[1] & 0x80: return f"reject: exception {resp[2]}"
    if resp[1] != 3 or resp[2] != 2 * count or len(resp) != 5 + 2 * count: return "reject: shape"
    vals = [int.from_bytes(resp[3 + 2*i:5 + 2*i], "big") for i in range(count)]
    if any(not lo <= v <= hi for v in vals): return f"reject: range {vals}"
    return f"ok {vals}"
good = frame(bytes.fromhex("010304") + (3150).to_bytes(2, "big") + (212).to_bytes(2, "big"))
tests = {"good": good, "bitflip": good[:4] + bytes([good[4] ^ 1]) + good[5:],
         "exception": frame(bytes.fromhex("018302")), "outrange": frame(bytes.fromhex("010304FFFF00D4")),
         "truncated": good[:6]}
for k, v in tests.items(): print(f"{k:9} {parse(v)}")
```

Expected output:

```text
request: 01 03 00 00 00 0a c5 cd
good      ok [3150, 212]
bitflip   reject: crc
exception reject: exception 2
outrange  reject: range [65535, 212]
truncated reject: crc
```

The truncated frame is rejected by the CRC check because its last two bytes are not a CRC; a parser that checked shape first would give a clearer reason. Both orders are safe; the important property is that nothing is accepted on partial evidence.

Notice that the good response decodes to a level of 3,150 cm and a pressure of 212 kPa, both inside the physical limits configured in the parser. The out-of-range case shows why repair is dangerous: clamping 65,535 to the 4,000 cm maximum would report a full reservoir when the register had never been written. Rejecting it with the raw value in the reason gives maintenance staff the clue they need, and gives an investigator evidence that the value was not simply noise on the line.

### 4.6 Common errors and limits

- Byte-order mistakes (Modbus registers are big-endian; the CRC is transmitted low byte first).
- Indexing before checking length; trusting a length field inside the message.
- Treating a CRC as authentication.
- "Repairing" bad input (clamping 65535 to 4000) instead of rejecting it, which hides faults and attacks.
- Writing tests only for the happy path.

Each item has a matching test in Lab 3 or EX008. A parser that passes those tests but was never checked against a truncated or malformed frame has only been tested for the happy path, and the first noisy serial line at a pumping station will show what it does with input it did not expect. Write the failure tests first, because they are the ones that matter when something goes wrong in the field.

### Exercises — chapter 4

**EX007 — CRC by hand and by code.** *Objective:* verify an implementation. *Inputs:* Lab 3. *Steps:* (1) compute the CRC of `01 06 00 01 00 03` (write single register) with the function; (2) flip one bit in the data and show the CRC changes; (3) explain in two sentences why an attacker on the serial line is not stopped by the CRC. *Expected evidence:* hex values and explanation. *Rubric:* 3 = correct CRC (verify against the worked result), demonstration, correct security statement; 2 = one missing; 1 = code not run; 0 = none.

**EX008 — Parser hardening.** *Objective:* improve error reporting without weakening checks. *Inputs:* `parse()`. *Steps:* reorder checks so a truncated frame reports "short" or "shape" before CRC, add a check that rejects a response whose unit identifier is 0 (broadcast), and add two test cases. *Expected evidence:* code diff and outputs. *Rubric:* 3 = all original rejections preserved, new checks correct, tests included; 2 = one rejection lost; 1 = untested; 0 = none.

### Chapter synthesis

Write code that is explicit about types, boundaries and failure. Implement published algorithms against published test vectors. Treat every parser as a security boundary: length, integrity, shape, then physical meaning, and reject with a reason rather than guess. Keep accidental-error detection (CRC) separate in your mind from adversarial integrity (MACs and signatures).

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 50

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes and connection

After this chapter you can (1) write a requirement that can be verified; (2) produce a one-page design note, a decision record and a test report that another engineer can check; (3) present risk and uncertainty to operators, managers and regulators without overstating or hiding it; and (4) handle sensitive infrastructure detail appropriately in documents. It builds on Chapters 1–4, whose numbers you now have to communicate, and prepares the design studios (Chapters 25 and 35).

### 5.1 Writing for decisions

Engineering documents exist so that someone can make or check a decision. Lead with the decision and its basis; put derivations after. A good design note answers, in this order: what is being decided, the options considered, the recommendation, the evidence and assumptions behind it, what would change the recommendation, and who must approve. **Architecture decision records** — short, dated, numbered notes recording a decision, its context and consequences — keep the reasons for a design visible years later when the original team has moved on.

### 5.2 Requirements that can be verified

A requirement is a statement the system must satisfy, written so that a test, analysis, inspection or demonstration can show whether it does. The [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) recommends requirements that are necessary, unambiguous, verifiable, feasible and traceable. Compare: "Telemetry shall be secure" (unverifiable) with "Each telemetry message from a field RTU to the control centre shall carry a message authentication code over its contents and a monotonic counter; the receiver shall reject messages failing either check and raise an alarm within 60 s" (verifiable by test). Use "shall" for requirements, keep one requirement per sentence, and give each an identifier.

### 5.3 Numbers, uncertainty and figures

Report numbers with units, the method that produced them and their uncertainty or assumptions: "hold-up 14.6 h (integrated demand model, start 06:00, 85% initial level; 17.3 h if mean demand is assumed)". Prefer tables for exact values, line charts for time series, and never a chart without labelled axes and units. Avoid false precision: a battery hold-up computed from estimated loads is "about 19 h", not "18.83 h". Make figures readable in greyscale and by people with colour-vision deficiency.

At LRWA, the hold-up figure in the TMRP dossier carries its start time and initial level, so nobody quotes it for a different scenario.

### 5.4 Communicating risk to different readers

Operators need what to do and when; managers need consequence, cost and options; regulators need evidence of compliance and of reasoning. The same finding — "remote setpoints are accepted without authentication" — becomes, for an operator, "until patched, confirm any unexpected setpoint change by phone with the control room"; for a manager, "a forged command could start or stop pumps; fix cost 120 k, three months"; for a regulator, a mapped control gap with a dated plan. None of these versions may contradict another.

### 5.5 Sensitive information

Infrastructure documents often contain network addresses, device models, vulnerabilities and capacity limits. Mark documents by sensitivity, share on a need-to-know basis, and strip detail from versions intended for wide audiences. Public reports and student work should describe systems at the level of the [NIST Guide to OT Security (SP 800-82 Rev. 3)](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — architectural patterns — not the specific weaknesses of a named operator.

In this book every LRWA figure is synthetic, but practise the habit anyway: mark design notes for internal use, keep network addresses out of slides, and produce a reduced version for audiences outside the engineering team.

### 5.6 Worked example: a TMRP decision record (synthetic)

> **ADR-007 — Authenticate field telemetry at the application layer.** *Date:* 2026-03-04. *Status:* accepted. *Context:* RTU–SCADA traffic crosses a private LTE network operated by a third party; LTE encryption terminates at the carrier. *Options:* (a) rely on carrier encryption; (b) IPsec tunnels per RTU; (c) application-layer HMAC with counters. *Decision:* (c), with (b) where RTUs support it. *Consequences:* +22 bytes per message (Lab 8); key management required (Chapter 19); legacy RTUs at PS1 and PS2 need a gateway. *Revisit if:* the carrier contract changes or RTU firmware gains native secure protocols.

### 5.7 Practical activity

Rewrite three vague requirements from a synthetic brief ("the system shall be resilient", "alarms shall be timely", "logs shall be protected") into verifiable form, each with a verification method.

For each rewrite, name the evidence that would show the requirement is met: a test with a pass criterion, an analysis with stated assumptions, an inspection or a demonstration. Use LRWA's context where it helps. A resilient system might become a stated hold-up during a grid outage, timely alarms might become a latency target for a stated share of events, and protected logs might become integrity protection with anchors stored outside the control zone, as R8 later requires. Keep each statement to one requirement.

### 5.8 Common errors and limits

- Burying the recommendation; writing a chronology instead of an argument.
- Requirements containing "and/or", "as appropriate", "user-friendly", "secure".
- Numbers without units, method or uncertainty.
- Different stories for different audiences.
- Over-sharing sensitive detail, or under-sharing to the point that reviewers cannot check the work.

Most of these errors appear first in requirement sets. A requirement containing secure cannot be tested, so it will either be quietly dropped or claimed without evidence. Different stories for different audiences are just as damaging: if the operator note, manager summary and regulator statement in EX010 disagree about the PS4 battery, whoever reads two of them will trust none.

### Exercises — chapter 5

**EX009 — Make it verifiable.** *Objective:* write testable requirements. *Inputs:* the three vague requirements in §5.7. *Steps:* rewrite each as one or more "shall" statements with an identifier and verification method (test, analysis, inspection, demonstration). *Expected evidence:* table. *Rubric:* 3 = each measurable, single, feasible, with a fitting method; 2 = one still vague; 1 = rewording only; 0 = none.

**EX010 — Three audiences.** *Objective:* communicate one finding consistently. *Inputs:* "PS4 telemetry battery lasts 6 h at end of life; requirement R5 is 24 h". *Steps:* write a two-sentence operator note, a 100-word manager summary with options, and a regulator-facing gap statement. *Expected evidence:* three texts. *Rubric:* 3 = consistent facts, audience-appropriate actions, no sensitive excess; 2 = one inconsistency; 1 = same text three times; 0 = none.

### Chapter synthesis

Write to enable decisions: recommendation first, evidence and assumptions next, conditions for change last. Make every requirement verifiable and traceable; report numbers with units, methods and uncertainty; tailor the message, not the facts, to the reader; and treat infrastructure detail as sensitive information with a defined audience.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 50

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes and connection

After this chapter you can (1) write a first-order ordinary differential equation (ODE) for a stock with inflow and outflow; (2) solve linear first-order ODEs analytically, including exponential approach to equilibrium and its time constant; (3) solve ODEs numerically and control the step-size error; and (4) use series and sensitivity (partial derivatives) to see which parameter matters most to a resilience margin. It extends Chapter 1 and prepares Chapter 17 (control).

### 6.1 Stocks with feedback become differential equations

Chapter 1's reservoir had a known outflow and no inflow. Real stocks have flows that depend on the stock itself. Water leaving an open tank through an orifice depends on the head above it; a chlorine residual decays at a rate proportional to its concentration; a battery's terminal voltage falls with its state of charge. When the rate depends on the quantity, you get an equation like $dx/dt = f(x, t)$. The simplest important case is linear: $dx/dt = -kx + u$, with constant $k > 0$ and input $u$.

### 6.2 The linear first-order solution and the time constant

With constant $u$, the solution is $x(t) = x_\infty + (x_0 - x_\infty)e^{-kt}$, where $x_\infty = u/k$ is the equilibrium. The **time constant** $\tau = 1/k$ is the time to close about 63% of the gap; after $3\tau$ about 95% is closed, after $5\tau$ about 99%. Engineers use $\tau$ to reason about how fast a system responds to a change — and how fast it responds to an attack. Example: free chlorine in a storage tank decays with a first-order constant; if $k = 0.05$ per hour, $\tau = 20$ h. If dosing stops (by fault or malicious command), the residual halves in $\ln 2/k \approx 13.9$ h. That is the window in which an operator must notice and act before residual falls below the regulatory minimum.

### 6.3 Numerical solution and error

Most ODEs in practice are non-linear or driven by measured inputs, so you solve them numerically. Forward Euler, $x_{n+1} = x_n + h f(x_n, t_n)$, has global error proportional to the step $h$; halving $h$ roughly halves the error. Heun's method and the classical fourth-order Runge–Kutta method reduce error much faster for the same $h$. Always run a **step-size convergence check**: if halving $h$ changes the answer you care about by more than your tolerance, the step is too large. For stiff systems — some components much faster than others — explicit methods can become unstable unless $h$ is very small; Euler on $dx/dt = -kx$ is unstable for $h > 2/k$.

### 6.4 Sensitivity: which assumption matters?

A design margin depends on several parameters: initial level, demand, leak rate, pump capacity. The partial derivative of the margin with respect to each parameter, multiplied by that parameter's plausible range, shows which uncertainty dominates. For hold-up $T = V/q$ with constant demand, $\partial T/\partial V = 1/q$ and $\partial T/\partial q = -V/q^2$; a 10% error in demand moves $T$ about as much as a 10% error in usable volume, but in the opposite direction. Taylor series give the same insight for non-linear models: near a nominal point, $f(x + \Delta) \approx f(x) + f'(x)\Delta$.

### 6.5 Worked example: chlorine dosing loss (synthetic)

LRWA's Hollin Hill outlet residual is maintained at 0.8 mg/L; the synthetic operating minimum is 0.2 mg/L. With dosing stopped and first-order decay $k = 0.05$ h⁻¹, residual reaches 0.2 mg/L when $0.8e^{-0.05t} = 0.2$, i.e., $t = \ln 4 / 0.05 \approx 27.7$ h. If warm weather raises $k$ to 0.08 h⁻¹, the window shrinks to 17.3 h. The design team writes requirement R9: *loss of dosing shall alarm within 15 minutes, independent of the dosing controller's own status reports* — because a compromised controller could report normal operation. The ODE turned into a detection-time requirement with margin.

### 6.6 Practical activity

Modify Lab 1 to include constant inflow 120 m³/h from a single surviving pump and first-order leakage $0.01V$ m³/h. Integrate with Euler at three step sizes, and find the equilibrium level analytically by setting $dV/dt = 0$ with demand replaced by its mean.

Report the equilibrium level and compare it with the reservoir's capacity and floor. With one pump at 120 cubic metres per hour against a mean demand of 150, the stock must still fall unless leakage balances the difference, so check whether your analytic answer is physically possible before trusting it. Then confirm that the Euler runs converge as the step shrinks. The point of the exercise is the combination: an analytic check, a numerical result and a convergence test that agree with each other.

### 6.7 Common errors and limits

- Using exponential decay where the process is not first-order.
- Reporting a numerical solution without a step-size check.
- Ignoring that parameters (decay rates, demand) drift with temperature and season.
- Sensitivity on one parameter at a time when parameters interact; for strong interactions use global methods ([Saltelli et al., 2008](https://doi.org/10.1002/9780470725184)).

In the chlorine example, a team that used the cool-weather decay constant all year would believe it had 27.7 hours when summer leaves about 17. R9's 15-minute alarm was chosen with that seasonal range in mind, which is why the requirement does not depend on the exact constant.

### Exercises — chapter 6

**EX011 — Time constant to requirement.** *Objective:* turn dynamics into a detection-time requirement. *Inputs:* §6.5. *Steps:* (1) compute the window at $k = 0.12$ h⁻¹; (2) if operators need 4 h to restore dosing manually, compute the latest acceptable alarm time; (3) write the requirement. *Expected evidence:* numbers and requirement. *Rubric:* 3 = correct window, margin and a verifiable requirement independent of the controller; 2 = one slip; 1 = numbers only; 0 = none.

**EX012 — Euler stability.** *Objective:* see numerical instability. *Inputs:* $dx/dt = -kx$, $k = 0.5$, $x_0 = 1$. *Steps:* compute five Euler steps with $h = 1$, $h = 3$ and $h = 5$ and compare with the exact solution. *Expected evidence:* table and explanation. *Rubric:* 3 = correct values and the $h > 2/k$ instability explained; 2 = values right, explanation weak; 1 = one step size only; 0 = none.

### Chapter synthesis

When a flow depends on the stock, write an ODE. Linear first-order systems approach equilibrium exponentially with time constant $\tau$; that number becomes a detection and response requirement. Solve numerically with convergence checks and attention to stability. Use sensitivity to find which assumption dominates a margin, and design detection that does not depend on the component under suspicion.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 50

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes and connection

After this chapter you can (1) apply Bayes' rule to alarms and explain the base-rate problem; (2) compute availability of redundant paths with and without common-cause failure; (3) model rare events with the Poisson distribution; and (4) summarise data with honest uncertainty, including when to distrust a small sample. It builds on Chapters 1–6 and prepares Chapters 23 (failure analysis), 29 (measurement) and 32 (reliability).

### 7.1 Probability as a model of uncertainty

A probability is a number between 0 and 1 attached to an event under a model. Engineers use three readings: long-run frequency (pump failures per year across a fleet), degree of belief (an expert's estimate of an adversary's capability), and design allowance (a target such as 99.9% availability). Be explicit about which you mean; mixing them is how risk registers become fiction. The core rules: $P(A \cup B) = P(A) + P(B) - P(A\cap B)$; $P(A \cap B) = P(A)P(B\mid A)$; independence means $P(B\mid A) = P(B)$.

### 7.2 Bayes' rule and the base-rate problem

$P(H\mid E) = P(E\mid H)P(H)/P(E)$. Apply it to an intrusion alarm: let attacks occur in 0.1% of hourly windows, the detector fire on 95% of attacks (true-positive rate) and on 1% of benign windows (false-positive rate). The probability that an alarm means an attack is only about 8.7%. Most alarms are false even for a "99% accurate" detector, because benign windows vastly outnumber attacks. This is why operators learn to ignore alarms — and why alarm design must report the expected alarm rate and the **positive predictive value**, not only accuracy. [Sommer and Paxson (2010)](https://doi.org/10.1109/SP.2010.25) discuss this and related obstacles to anomaly detection in operational networks.

### 7.3 Redundancy and common cause

If one communications path is available with probability $a$ and paths fail independently, $n$ paths give $1-(1-a)^n$. Independence is the assumption that fails in practice: paths sharing a power feeder, a vendor, a configuration or an exploitable vulnerability fail together. The **beta-factor model** assigns a fraction $\beta$ of each unit's unavailability to common causes that defeat all units at once. With $a = 0.98$ and $\beta = 0.05$, two paths have unavailability ≈ 0.00136 instead of 0.0004: common cause dominates. In security, an identical software vulnerability in both paths is a common cause with $\beta$ close to 1 against an adversary who knows it.

### 7.4 Rare events: the Poisson model

If events arrive independently at average rate $\lambda$ per year, the number in a year is Poisson: $P(N=k) = e^{-\lambda}\lambda^k/k!$. With $\lambda = 0.5$ long grid outages per year, $P(N \ge 1) \approx 0.39$. Poisson assumes a constant rate and independence; storms, campaigns of attacks and ageing violate both, so treat it as a first approximation.

For LRWA, a long grid outage of more than four hours is the event that tests R5 and the hospital buffer together. If outages cluster in storms, the Poisson figure understates the chance of two outages within days, so the TMRP team checks it against the distributor's outage records before using it in the fault tree.

### 7.5 Describing data honestly

Report a central value with spread (median and interquartile range for skewed data such as outage durations), the sample size, and how the data were collected. A confidence interval describes sampling uncertainty under a model; it says nothing about bias in what was recorded. Small samples of rare events are especially treacherous: zero failures in 3 years of operation does not mean zero risk. The "rule of three" gives an approximate 95% upper bound of $3/n$ on a rate when 0 events are observed in $n$ trials or time units.

### 7.6 Worked example: should LRWA page the on-call engineer? (synthetic)

The TMRP proposes a network anomaly detector at the control centre with the rates in §7.2. Evaluated over hourly windows, it would page about 0.26 times a day — roughly once every four days — and about 91% of pages would be false. The team decides: page only when the network alarm coincides with a process anomaly (unexpected setpoint change or flow imbalance), and route lone network alarms to a next-business-day review queue. The decision is justified by the base rate, and its cost — slower response to a stealthy network-only attack — is recorded in the risk register.

### 7.7 Practical activity: Lab 4

```python
# Lab 4 - base rates, redundancy and rare events (synthetic numbers, offline)
import math
prior, tpr, fpr = 0.001, 0.95, 0.01
ppv = tpr * prior / (tpr * prior + fpr * (1 - prior))
print(f"P(attack | alarm) = {ppv:.3f}")
alarms_per_day = 24 * (tpr * prior + fpr * (1 - prior))
print(f"expected alarms per day (hourly windows) = {alarms_per_day:.3f}")
a = 0.98
for n in (1, 2, 3): print(f"{n} independent paths at {a}: availability {1 - (1 - a) ** n:.6f}")
beta = 0.05   # beta-factor common-cause share of unavailability
q = 1 - a
print(f"2 paths with beta={beta}: unavailability {(1 - beta) ** 2 * q ** 2 + beta * q:.6f}")
lam = 0.5
print(f"P(>=1 grid outage >4 h per year | lambda={lam}) = {1 - math.exp(-lam):.3f}")
print(f"P(>=2) = {1 - math.exp(-lam) * (1 + lam):.4f}")
```

Expected output:

```text
P(attack | alarm) = 0.087
expected alarms per day (hourly windows) = 0.263
1 independent paths at 0.98: availability 0.980000
2 independent paths at 0.98: availability 0.999600
3 independent paths at 0.98: availability 0.999992
2 paths with beta=0.05: unavailability 0.001361
P(>=1 grid outage >4 h per year | lambda=0.5) = 0.393
P(>=2) = 0.0902
```

The first two lines repeat the base-rate result from the worked example: fewer than one alarm in ten would be a real attack, and the detector would page about once every four days. The redundancy lines show how quickly independent paths improve availability, and the beta-factor line shows how a five per cent common cause wipes out most of that gain. The Poisson lines give the chance of at least one, and at least two, long grid outages in a year at LRWA's assumed rate.

### 7.8 Common errors and limits

- Reporting detector accuracy without the base rate and predictive value.
- Multiplying availabilities as if independent when paths share causes.
- Using Poisson for clustered events.
- Treating zero observed failures as zero probability.
- Point estimates without sample size and collection method.

Each error has an LRWA example. Paging the on-call engineer for every network alarm ignores the base rate. Treating the two LTE paths as independent ignores their shared feeder. Using Poisson for storm outages hides clustering, and three quiet years at PS4 do not prove the pumps cannot fail together.

### Exercises — chapter 7

**EX013 — Base rate sensitivity.** *Objective:* see how predictive value depends on prevalence. *Inputs:* Lab 4. *Steps:* compute PPV for priors 0.0001, 0.001 and 0.01 with the same detector, and for prior 0.001 with FPR 0.001. *Expected evidence:* four values and a recommendation on which parameter to improve. *Rubric:* 3 = correct values and the insight that FPR reduction matters most at low prevalence; 2 = values right; 1 = one value; 0 = none.

**EX014 — Common cause in telemetry.** *Objective:* quantify diversity. *Inputs:* two LTE paths from different carriers ($a = 0.98$ each). *Steps:* compute unavailability for $\beta$ = 0, 0.05, 0.2; name two real common causes these paths might still share. *Expected evidence:* three numbers and two causes. *Rubric:* 3 = correct numbers and plausible shared causes (site power, shared tower or backhaul, same modem firmware); 2 = generic causes; 1 = one number; 0 = none.

### Chapter synthesis

Probability is a model; say which kind. Bayes' rule makes base rates decisive for alarms; redundancy works only to the extent that failures are independent, and common causes — including shared vulnerabilities — usually dominate. Poisson is a starting point for rare events. Describe data with spread, sample size and collection method, and never treat absence of observed failures as proof of safety.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 50

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes and connection

After this chapter you can (1) describe how a processor, memory hierarchy and I/O interact, and why this matters for real-time control; (2) explain the architecture of programmable logic controllers (PLCs), RTUs and embedded controllers; (3) relate hardware features — privilege levels, memory protection, secure boot, hardware roots of trust — to security guarantees; and (4) explain how performance optimisations such as caching and speculation create vulnerabilities. It builds on Chapter 3 and prepares Chapter 12 (operating systems).

### 8.1 The machine model

A processor fetches instructions from memory, decodes and executes them, and reads and writes data in registers and memory. Memory is a hierarchy — registers, caches, main memory, storage — each level larger and slower. I/O devices connect through buses and interrupts; an interrupt suspends normal execution so the processor can service a device. **Determinism** — knowing the worst-case time an operation takes — matters more in control than average speed: a pump-protection routine that usually takes 1 ms but occasionally 50 ms because of a cache miss storm or garbage collection may miss its deadline.

### 8.2 PLCs, RTUs and embedded controllers

A PLC executes a **scan cycle**: read inputs, execute the user program, write outputs, perform communications and diagnostics, repeat — often every 10–100 ms. Its program is written in languages standardised in IEC 61131-3 (ladder logic, function block diagrams, structured text). An RTU is designed for remote sites: it gathers measurements, applies simple logic and communicates over long-distance links, tolerating intermittent connectivity. Both are long-lived: equipment installed today may run for fifteen to twenty-five years, so the security features you choose now must still be acceptable in the 2040s. Many legacy controllers accept program changes from anyone who can reach them on the network; Stuxnet exploited the path from an engineering workstation to PLC logic, as analysed by [Langner (2011)](https://doi.org/10.1109/MSP.2011.67).

### 8.3 Hardware support for security

- **Privilege levels** separate kernel from user code; a fault in user code cannot directly overwrite the kernel.
- **Memory protection units** (MPU) and **memory management units** (MMU) enforce which code may access which memory; an MPU is common in microcontrollers that lack a full MMU.
- **Execute-never** marking prevents data regions from being executed.
- **Secure boot** verifies a cryptographic signature on each stage of firmware before running it, anchored in an immutable root of trust (ROM code or fused keys). It protects against persistent firmware modification, not against a correctly signed but vulnerable image.
- **Trusted platform modules** and secure elements store keys so that software cannot read them out.

### 8.4 When speed creates leakage

Caches and speculative execution make processors fast by guessing and keeping state, and that state can leak. [Kocher et al. (2019)](https://doi.org/10.1109/SP.2019.00002) showed that speculative execution can be steered to read memory across protection boundaries (Spectre). [Kim et al. (2014)](https://doi.org/10.1109/ISCA.2014.6853210) showed that repeated DRAM access can flip bits in adjacent rows (Rowhammer). These matter most where untrusted code shares hardware with trusted code — virtualised control-centre servers, shared cloud — and less in a single-purpose PLC. The engineering lesson: hardware is part of the attack surface, and isolation that relies on shared hardware must be justified.

### 8.5 Worked example: choosing an RTU platform (synthetic)

TMRP compares two candidate RTUs. *RTU-A:* mature, deterministic, no secure boot, firmware updates unsigned, program changes authenticated only by a shared password. *RTU-B:* secure boot with vendor-signed firmware, role-based authentication for program changes, hardware key storage, but a 200 ms longer worst-case response to communication requests and a new product with limited field history. The team scores both against requirements: R1 (authenticated telemetry) needs key storage — favouring B; R7 (alarm within 60 s) is met by both, as 200 ms is negligible; maintainability over 20 years favours a vendor with a published secure-development lifecycle. The decision record selects B for new sites and a gateway for legacy RTU-A sites, with a pilot to collect field reliability data before fleet roll-out.

### 8.6 Practical activity

For a microcontroller or PLC family of your choice, read the vendor's public security manual (or a datasheet) and complete a table: privilege separation, memory protection, secure boot, signed updates, key storage, authenticated programming. Mark each "yes / no / configurable / unknown" with a source citation. Use public documents only.

Record the document title, version and date for each entry, because security features change between firmware releases. Where the manual is silent, mark the feature unknown rather than guessing, and list the question you would ask the vendor. The table is the same comparison the TMRP team made between RTU-A and RTU-B, and it shows quickly whether a product can support authenticated telemetry and key storage without a gateway.

### 8.7 Common errors and limits

- Equating "fast" with "deterministic".
- Assuming secure boot prevents exploitation of signed firmware.
- Ignoring the 20-year lifetime when choosing cryptographic and update features.
- Treating hardware isolation on shared servers as absolute.
- Treating vendor marketing as evidence; ask for documentation and test.

The RTU comparison shows these errors in practice. RTU-A is deterministic but cannot protect keys, so speed alone does not make it suitable. RTU-B's secure boot does not stop a malicious but legitimately signed logic change, which is why role-based programming access is listed beside it. Both must still be supportable in the 2040s, and the pilot exists because vendor claims are not field evidence.

### Exercises — chapter 8

**EX015 — Scan-cycle budget.** *Objective:* reason about determinism. *Inputs:* PLC scan of 20 ms nominal, 45 ms worst case; a pump-protection requirement to trip within 100 ms of a low-suction signal, which is debounced over two consecutive scans. *Steps:* compute the worst-case trip latency (input sampling just after a read, two scans to confirm, output write). *Expected evidence:* calculation and conclusion. *Rubric:* 3 = correct worst case including sampling delay and judgement against 100 ms; 2 = sampling delay omitted; 1 = nominal scan only; 0 = none.

**EX016 — What secure boot buys.** *Objective:* scope a control precisely. *Inputs:* RTU-B in §8.5. *Steps:* list two attacks secure boot prevents, two it does not, and the complementary control for each of the latter. *Expected evidence:* table. *Rubric:* 3 = accurate scope (prevents unsigned persistent firmware; not runtime exploits or malicious logic changes via legitimate programming), matched controls; 2 = one error; 1 = generic; 0 = none.

### Chapter synthesis

Architecture determines both timing and trust. Control needs worst-case, not average, performance. PLCs and RTUs are long-lived, scan-based machines whose security features must still be adequate decades from now. Hardware mechanisms — privilege, memory protection, secure boot, key storage — give specific, limited guarantees; performance features can leak across boundaries. State exactly what each mechanism protects against.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 50

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes and connection

After this chapter you can (1) structure a program into modules with clear interfaces and invariants; (2) implement simple state machines for protocol and equipment logic; (3) write unit tests, including boundary and failure tests, and measure what they cover; and (4) handle errors, time and concurrency deliberately. It builds on Chapter 4 and prepares Chapter 14 (software engineering) and Chapter 30 (verification).

### 9.1 Modules, interfaces and invariants

[Parnas (1972)](https://doi.org/10.1145/361598.361623) argued that a system should be decomposed so that each module hides a design decision likely to change. In infrastructure software, likely changes include the field protocol, the historian, and the authentication scheme. Hide each behind an interface: a `TelemetrySource` that yields validated readings, whatever the protocol. Each module should state its **invariants** — properties always true of its state — for example, "the last accepted counter for each station never decreases". Write invariants as assertions in tests and, where cheap, as runtime checks that fail safe.

### 9.2 State machines

Equipment and protocols have modes: a pump is *stopped*, *starting*, *running*, *stopping* or *tripped*; a session is *unauthenticated*, *authenticated* or *closed*. A finite state machine lists states, the events that cause transitions, guards on transitions and actions. Write it as a table and implement it from the table, rejecting any event not listed for the current state. Unlisted transitions are where both bugs and attacks live: a "stop" command arriving while *starting*, or a "write setpoint" arriving before authentication.

LRWA's pump controller in the worked example below is built exactly this way, so its tests can enumerate every pair.

### 9.3 Testing

A unit test checks one behaviour of one unit. Good test suites include: typical cases; **boundaries** (minimum, maximum, just inside, just outside); invalid input; and **regression** tests reproducing past bugs. Coverage measures which statements or branches the tests executed; it tells you what was *not* tested, not that the tested code is correct. Python's `unittest` module, in the standard library, is enough for this book.

For LRWA's pump controller, boundary tests include the 30-second start timeout at exactly 30 seconds and just beyond it, and regression tests reproduce every transition bug found in commissioning, so a fixed fault cannot quietly return in a later release.

### 9.4 Errors, time and concurrency

Decide how each error is handled: rejected with a reason, retried with a limit, or escalated. Never swallow exceptions silently in control or security code. Time is a recurring source of failure: use monotonic clocks for intervals and synchronised wall-clock time (with its source recorded) for logs; handle clock steps. Concurrency — threads, asynchronous tasks, multiple clients — creates race conditions: two operators issuing conflicting setpoints, or a check and an action separated by a window in which state changes (time-of-check to time-of-use). Prefer a single owner for each piece of state, with messages to change it.

### 9.5 Worked example: a pump state machine (synthetic)

LRWA's pump controller accepts `start`, `stop`, `trip` and `reset`. The table: *stopped* + `start` (guard: permissive true) → *starting*; *starting* + `run_confirmed` → *running*; *starting* + timeout 30 s → *tripped*; *running* + `stop` → *stopping*; any state + `trip` → *tripped*; *tripped* + `reset` (guard: local operator) → *stopped*. The guard on `reset` matters: requiring a local action after a trip means a remote attacker who causes a trip cannot immediately restart the pump into the same fault. Tests cover every listed transition and assert that every unlisted pair (for example *tripped* + `start`) is rejected and logged.

### 9.6 Practical activity

Implement the table in §9.5 in about 40 lines of Python with a dictionary keyed by `(state, event)`. Write `unittest` cases for all listed transitions and a loop that asserts every unlisted `(state, event)` pair raises an error. Count the unlisted pairs.

Your loop should print the number of unlisted pairs and confirm that each one raises an error and writes a log line. Then add a test showing that a remote reset after a trip is refused, because the guard requires a local operator. That test protects the property the worked example cares about most: an attacker who trips a pump remotely cannot restart it straight into the same fault. Keep the table and the tests in one file so a reviewer can compare them.

### 9.7 Common errors and limits

- Implementing state logic with scattered flags instead of an explicit table.
- Default branches that accept unknown events.
- Using wall-clock time for timeouts.
- Tests that only exercise the happy path; equating coverage with correctness.
- Silent exception handling.

Each error defeats a property of the pump state machine. Scattered flags make it impossible to list every transition. A default branch would let a start command through while the pump is tripped. A wall-clock timeout could fire early or never after a clock step, and an exception swallowed in the reset path would leave the pump in an unknown mode.

### Exercises — chapter 9

**EX017 — Count and test the unlisted transitions.** *Objective:* reason about completeness. *Inputs:* §9.5 (states: stopped, starting, running, stopping, tripped; events: start, stop, trip, reset, run_confirmed, timeout, stop_confirmed — add *stopping* + `stop_confirmed` → *stopped*). *Steps:* count total pairs, listed pairs and unlisted pairs; give three unlisted pairs whose rejection has a safety or security rationale. *Expected evidence:* counts and rationale. *Rubric:* 3 = correct counts and meaningful rationales; 2 = count error; 1 = no rationale; 0 = none.

**EX018 — Replay invariant.** *Objective:* express and test an invariant. *Inputs:* Lab 8's `Receiver`. *Steps:* write the invariant on `last`, a unit test that sends counters 1, 2, 2, 1, 5 and asserts accept/reject results and the final state, and state one failure mode of the invariant after a receiver restart. *Expected evidence:* test code and statement. *Rubric:* 3 = correct expected results (accept, accept, reject, reject, accept), restart issue identified (state lost → replays accepted unless persisted or keys rotated); 2 = restart missed; 1 = untested; 0 = none.

### Chapter synthesis

Decompose around decisions likely to change and state invariants. Make modes explicit as state machines and reject everything not listed. Test boundaries and failures, read coverage as a map of the untested, handle errors deliberately, use the right clock, and give each piece of shared state one owner.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue studying — chapter 09 of 50

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes and connection

After this chapter you can (1) apply professional codes of ethics to infrastructure security decisions; (2) explain the relationship between safety and security and where they conflict; (3) recognise legal and authorisation boundaries on testing and research; and (4) make and document an ethical decision under uncertainty, including when to escalate. It builds on Chapter 5 and frames every later chapter, particularly testing (Chapters 30 and 40) and practice (Chapter 43).

### 10.1 Duties of an engineer

Professional codes converge on a hierarchy: hold paramount the safety, health and welfare of the public; act within competence; be honest and objective; avoid conflicts of interest; protect confidential information. The [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics) makes public safety the first fundamental canon; the [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) asks computing professionals to avoid harm and to be honest about system capabilities and limits. In critical infrastructure the public is concrete: patients on dialysis, households without water, people waiting for an ambulance. The duty is not satisfied by following instructions if the result is foreseeable public harm.

### 10.2 Safety and security together

**Safety** protects people and the environment from harm caused by the system; **security** protects the system from deliberate misuse. In operational technology the two interact. A security control can create a safety hazard — an automatic account lockout on an operator console during an emergency, or a patch that restarts a controller during a process run. A safety mechanism can be a security target: the TRITON/TRISIS malware targeted safety instrumented system controllers, as described in CISA's [HatMan malware analysis report](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf). Good practice treats both in one hazard analysis (Chapter 33) and gives safety functions independence from the networks and systems they protect.

### 10.3 Authorisation and law

Testing a system you do not own or have written permission to test can be a crime, whatever your intentions, and in infrastructure it can endanger people. Authorisation must be written, specific (systems, times, methods), from someone entitled to give it, and include stop conditions. Research involving people or operational data needs ethics review and data agreements. Vulnerabilities you find incidentally should go to the asset owner privately or through a coordinated disclosure programme such as [CISA's CVD programme](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program). This book's labs are synthetic for exactly these reasons.

### 10.4 Deciding under uncertainty

A practical ethical decision procedure: (1) state the decision and who is affected; (2) identify duties and the facts that bear on them; (3) list options, including escalation and refusal; (4) assess consequences for the most vulnerable stakeholders; (5) choose, document the reasoning and the dissent, and set a review point. Engineers rarely face clean dilemmas; more often the problem is pressure to sign off on something not yet shown to work. "Not verified" is an honest and sufficient answer.

In the worked example that follows, the TMRP verification engineer uses exactly these five steps.

### 10.5 Worked example: the deadline sign-off (synthetic)

TMRP's commissioning deadline is Friday. Test T3 (setpoint bounds) has failed: the PS4 controller accepts a setpoint outside the safe range when sent as a NaN value. The vendor proposes commissioning with a note to fix in the next release. As the verification engineer, you apply the procedure: affected people include hospital patients if PS4 behaves unpredictably; your duty is to public safety and honest reporting; options are (a) sign, (b) refuse, (c) commission with a compensating control — remote setpoint writes disabled at the gateway, local-only operation for PS4 — and a dated fix. You recommend (c), record T3 as failed, not waived, and require re-test before remote writes are enabled. The decision is documented and signed by the operations manager, who owns the operational risk.

### 10.6 Practical activity

Write a one-page authorisation template for a test of a synthetic system: scope, methods excluded, time window, stop conditions, contacts, data handling and sign-off.

Fill in the template for a bench test of LRWA's telemetry gateway rather than for a live station. Name who may sign it, list the methods that are excluded, such as any traffic towards real RTUs, and give stop conditions that a tester can recognise without interpretation. Include a contact who can halt the test at any time and a rule for what happens to captured data afterwards. A template that would let someone test PS4 during a high-demand period has failed its purpose.

### 10.7 Common errors and limits

- Treating ethics as a compliance checklist rather than reasoning about harm.
- "Verbal permission" for testing.
- Security controls designed without considering safety in emergencies.
- Signing off what has not been verified because a schedule demands it.
- Public disclosure of infrastructure weaknesses without coordination.

The deadline sign-off in the worked example shows several of these at once: pressure to commission, a vendor offering a verbal promise to fix later, and a failed test that could easily have been marked waived. The engineer avoided each one by recording the failure and agreeing a compensating control in writing.

### Exercises — chapter 10

**EX019 — Safety–security conflict.** *Objective:* resolve a control that endangers operations. *Inputs:* proposal to lock operator HMI accounts after five failed logins. *Steps:* analyse the hazard, propose an alternative that preserves security intent, and state how you would verify it. *Expected evidence:* half-page analysis. *Rubric:* 3 = hazard clear (lockout during emergency), alternative maintains accountability and resists guessing (e.g., rate-limiting with alerting, physical-presence override, shift accounts with logging), verification stated; 2 = alternative weak; 1 = hazard only; 0 = none.

**EX020 — Incidental finding.** *Objective:* act within authorisation. *Inputs:* while studying a public utility's procurement documents for coursework, you notice an internet-facing management page of a pump controller visible in a screenshot, with the vendor and model shown. *Steps:* state what you must not do, what you should do and to whom, and what your coursework may say. *Expected evidence:* 150 words. *Rubric:* 3 = no access or probing, private notification to the owner or via CVD, coursework anonymised; 2 = one step missing; 1 = suggests "checking whether it is real"; 0 = none.

### Chapter synthesis

Public safety comes first, honestly reported. Safety and security must be analysed together because each can defeat the other. Test only with written, specific authorisation; report incidental findings privately. Decide under uncertainty with a documented procedure, and treat "not verified" as an answer you are allowed — and obliged — to give.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue studying — chapter 10 of 50

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes and connection

After this chapter you can (1) explain the layered model and the roles of Ethernet, IP, TCP, UDP and application protocols; (2) describe industrial protocols (Modbus/TCP, DNP3, IEC 60870-5-104, OPC UA) and which security properties each does or does not provide; (3) build a latency budget for telemetry; and (4) express segmentation as zones and conduits and check observed flows against it. It builds on Chapters 3 and 4 and prepares Chapters 18 (security architecture) and 26 (architecture alternatives).

### 11.1 Layers and what they promise

Networks are built in layers: physical and link (Ethernet frames on a segment), network (IP packets routed between segments), transport (TCP reliable ordered byte streams; UDP datagrams without delivery guarantees — TCP is specified in [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)), and application (the protocol that carries meaning). Each layer promises something limited. TCP guarantees order and retransmission, not authenticity. IP routes, but source addresses can be forged on many networks. Security properties must be added deliberately, usually with TLS ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)), IPsec, or application-layer authentication.

### 11.2 Industrial protocols

Classic industrial protocols were designed for closed serial networks. **Modbus/TCP** (port 502) carries function codes such as read and write registers with no authentication; anyone who can reach port 502 can issue writes. **DNP3** is widely used in water and electricity; its Secure Authentication extension adds challenge–response authentication of critical commands but is not universally deployed. **IEC 60870-5-104** is common in European power systems, with security extensions defined in IEC 62351. **OPC UA** was designed with security modes offering signing and encryption, but they must be configured — "None" is a valid policy. The lesson is consistent: protocol capability is not deployment. Check what is configured.

### 11.3 Latency, jitter and polling

Telemetry is usually polled: the SCADA master asks each RTU in turn. End-to-end latency from a physical event to an operator's screen is the sum of sensor update, RTU scan, link round-trip, master polling wait, processing and display refresh. **Jitter** is variation in latency. Write a budget, measure each element, and compare the total with the requirement; Chapter 36 adds queueing.

LRWA's budget in Lab 5 adds RTU scan, LTE round trip, polling wait and screen refresh to reach one second against a 1.5-second requirement, but the polling wait is the element that varies most, and EX022 shows how it dominates the worst case.

### 11.4 Zones, conduits and allowlists

Segmentation divides a network into **zones** with similar security requirements and controls the **conduits** between them. This vocabulary comes from the [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards). A conduit policy is an **allowlist**: specific source zone, destination zone, protocol and port, everything else denied. Verification is not reading the firewall configuration; it is checking observed flows against intended policy, because configurations drift and undocumented paths (a vendor's remote-access modem, a dual-homed laptop) bypass firewalls.

LRWA's flow review below shows why.

### 11.5 Worked example: LRWA flow review (synthetic)

LRWA defines zones: *enterprise*, *dmz*, *control* (SCADA servers), *field* (RTUs) and *eng* (engineering workstations). The intended conduits are listed in Lab 5. A week of flow records shows three violations: an enterprise host speaking Modbus directly to a field RTU (a forgotten reporting script that bypasses the DMZ), an engineering workstation opening SSH directly to an RTU rather than through the control zone jump host, and a SCADA server making DNS queries to a public resolver. Each is a finding with an owner: remove the script and serve its data from the DMZ historian; route engineering access through the jump host; point SCADA DNS at an internal resolver or none.

### 11.6 Practical activity: Lab 5

```python
# Lab 5 - check observed flows against a zone-conduit allowlist (synthetic, offline)
RULES = [  # (src_zone, dst_zone, protocol, port)
    ("control", "field", "tcp", 502), ("control", "dmz", "tcp", 443), ("dmz", "enterprise", "tcp", 443),
    ("eng", "control", "tcp", 22), ("field", "control", "udp", 20000)]
ZONE = {"10.1.0.": "control", "10.2.0.": "field", "10.3.0.": "dmz", "10.4.0.": "enterprise", "10.5.0.": "eng"}
def zone(ip): return next((z for p, z in ZONE.items() if ip.startswith(p)), "unknown")
FLOWS = [("10.1.0.5", "10.2.0.31", "tcp", 502), ("10.4.0.77", "10.2.0.31", "tcp", 502),
         ("10.2.0.31", "10.1.0.5", "udp", 20000), ("10.3.0.9", "10.4.0.20", "tcp", 443),
         ("10.5.0.12", "10.2.0.33", "tcp", 22), ("10.1.0.5", "8.8.8.8", "udp", 53),
         ("10.1.0.6", "10.3.0.9", "tcp", 443)]
for s, d, p, port in FLOWS:
    ok = (zone(s), zone(d), p, port) in RULES
    print(f"{s:>10} {zone(s):>10} -> {d:<10} {zone(d):<10} {p}/{port:<5} {'allowed' if ok else 'VIOLATION'}")
budget = {"rtu_scan": 120, "lte_rtt": 180, "scada_poll_wait": 500, "operator_view": 200}
print("end-to-end latency budget ms:", sum(budget.values()), "vs requirement 1500")
```

Expected output:

```text
  10.1.0.5    control -> 10.2.0.31  field      tcp/502   allowed
 10.4.0.77 enterprise -> 10.2.0.31  field      tcp/502   VIOLATION
 10.2.0.31      field -> 10.1.0.5   control    udp/20000 allowed
  10.3.0.9        dmz -> 10.4.0.20  enterprise tcp/443   allowed
 10.5.0.12        eng -> 10.2.0.33  field      tcp/22    VIOLATION
  10.1.0.5    control -> 8.8.8.8    unknown    udp/53    VIOLATION
  10.1.0.6    control -> 10.3.0.9   dmz        tcp/443   allowed
end-to-end latency budget ms: 1000 vs requirement 1500
```

Three of the seven flows are violations, and each matches a finding in the worked example: the enterprise reporting script speaking Modbus to a field RTU, the engineering workstation opening SSH directly to an RTU instead of through the jump host, and a SCADA server querying a public DNS resolver. The latency budget line shows a total of one second against the 1.5-second requirement, but that figure uses typical values, so treat it as a starting point for the worst-case analysis in EX022 rather than evidence that R7 is met.

### 11.7 Common errors and limits

- Equating encryption at one layer with end-to-end protection.
- Assuming an industrial protocol's optional security is enabled.
- Verifying segmentation by reading configurations only.
- Latency budgets with averages instead of worst cases.
- Allowlists by host instead of by function, which become unmaintainable.

LRWA's flow review illustrates the third error directly: the firewall configuration looked correct, yet a week of flow records showed three violations. Reading configurations would have found none of them. Allowlists written by host would also have needed constant edits as RTUs were added.

### Exercises — chapter 11

**EX021 — Extend the policy check.** *Objective:* find violations by function. *Inputs:* Lab 5. *Steps:* (1) add a flow from `10.2.0.31` to `10.4.0.77` on TCP/445; (2) add a rule so the engineering workstation can reach RTUs only via a jump host in the control zone, and model the two hops; (3) rerun and report. *Expected evidence:* code changes and output. *Rubric:* 3 = new violation detected, two-hop model correct, no rule weakens field protection; 2 = one issue; 1 = not run; 0 = none.

**EX022 — Latency against requirement.** *Objective:* budget worst-case latency. *Inputs:* RTU scan 120 ms, LTE round-trip 180 ms typical / 900 ms 99th percentile, polling wait up to one full cycle of 1.3 s (Lab 13), operator view refresh 200 ms; requirement: 95% of alarms on screen within 1.5 s and all within 5 s. *Steps:* compute typical and worst-case totals; judge both clauses; propose one design change. *Expected evidence:* table. *Rubric:* 3 = correct sums, polling wait recognised as dominant, change proposed (report-by-exception or unsolicited alarms); 2 = one sum wrong; 1 = typical only; 0 = none.

### Chapter synthesis

Each network layer promises something narrow; authenticity has to be added. Industrial protocols vary in security capability, and capability is not configuration. Budget latency with worst cases. Express segmentation as zones and conduits with allowlists, and verify it against observed flows rather than intended configurations.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue studying — chapter 11 of 50

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes and connection

After this chapter you can (1) explain processes, threads, scheduling, memory management and file systems; (2) distinguish general-purpose and real-time operating systems and choose between them; (3) apply OS security mechanisms — accounts, permissions, isolation, logging, patching — to control-centre servers and engineering workstations; and (4) plan patching and hardening under the availability constraints of operational technology. It builds on Chapter 8 and prepares Chapters 18 and 39.

### 12.1 What an operating system does

An OS multiplexes hardware among programs and provides abstractions: **processes** (isolated address spaces), **threads** (concurrent execution within a process), **virtual memory**, **files** and **devices**. The kernel runs privileged; applications request services through system calls. The scheduler decides which thread runs; its policy determines latency.

For LRWA, the SCADA servers and engineering workstations run general-purpose operating systems, while the pump protection logic runs on the RTUs and PLCs at each station. Knowing which code runs where tells you which machines need real-time guarantees and which need hardening, patching and logging of the kind described below.

### 12.2 Real-time operating systems

A **real-time** OS guarantees bounded response: tasks with deadlines are scheduled so that, if the analysis says they fit, they meet their deadlines. Fixed-priority scheduling with rate-monotonic priority assignment is a classic approach; Liu and Layland's analysis gives a sufficient utilisation bound for periodic tasks under that policy. General-purpose OSes (Windows, desktop Linux) optimise throughput and fairness; their worst-case latency is not bounded without special configuration. Rule: protection functions run on real-time controllers; supervisory functions (HMI, historian) can run on general-purpose systems.

### 12.3 OS security mechanisms

- **Least privilege:** services run under dedicated accounts with only needed rights; no shared administrator accounts. [Saltzer and Schroeder (1975)](https://doi.org/10.1109/PROC.1975.9939) set out least privilege, fail-safe defaults, complete mediation and economy of mechanism as design principles that still hold.
- **Access control:** file and object permissions; mandatory access control where available.
- **Application allowlisting:** only approved executables run — practical on single-purpose OT hosts whose software rarely changes.
- **Logging:** authentication, privilege use, service changes and process creation, forwarded off-host.
- **Hardening:** remove unused services, close unused ports, disable removable-media autorun.
- **Patching:** apply security updates, tested and scheduled.

### 12.4 Patching under availability constraints

OT systems often cannot be rebooted at will, and vendors may support only specific patch levels. Patching is therefore risk-based: assess each vulnerability's exploitability in your architecture (is the vulnerable service reachable?), its consequence, and the availability risk of applying it; then patch, mitigate (block the port, disable the feature) or accept with a review date. Keep a test system that mirrors production to validate patches. The [NIST OT guide (SP 800-82 Rev. 3)](https://csrc.nist.gov/pubs/sp/800/82/r3/final) discusses these tradeoffs.

### 12.5 Worked example: hardening the SCADA servers (synthetic)

LRWA's two SCADA servers run a general-purpose OS. The TMRP baseline: dedicated service accounts; operators log in with named accounts; local administrator disabled except a break-glass account whose password is sealed and whose use alarms; allowlisting enabled after a two-week learning period in a test environment; USB storage blocked; logs forwarded to the DMZ collector; a monthly patch window alternating between servers so one always runs. The residual risk — the vendor certifies patches 30 days after release — is mitigated by network rules that expose only the SCADA application ports to the field and the DMZ.

### 12.6 Practical activity

On a Linux virtual machine you own, list listening services (`ss -tulpn`), local accounts with login shells, and enabled services. Write a hardening note: which services you would disable on a single-purpose historian host and why. Do not run this against any system you do not own.

Record the output with the date and the machine's name, and for each service you would disable, note what would break if you were wrong. A historian host at LRWA would need its database service and log forwarding, but rarely a mail server or a file-sharing service. Compare your list with the hardening measures in the SCADA example and explain any difference. The exercise trains the habit of asking why each service is running before deciding whether it should.

### 12.7 Common errors and limits

- Running protection logic on a general-purpose OS.
- Shared accounts that destroy accountability.
- Patching by calendar without assessing exploitability — or never patching because "OT is special".
- Logs kept only on the host an attacker controls.
- Allowlisting switched on in production without a learning period.

LRWA's SCADA hardening avoids each of these: named accounts replace shared ones, logs leave the host, allowlisting followed two weeks of learning in a test environment, and the monthly patch window alternates between the two servers. The residual risk is recorded.

### Exercises — chapter 12

**EX023 — Rate-monotonic check.** *Objective:* test schedulability with the Liu–Layland bound. *Inputs:* three periodic tasks on an RTU: (C=2 ms, T=10 ms), (C=4 ms, T=40 ms), (C=10 ms, T=100 ms). *Steps:* compute utilisation; compute the bound $n(2^{1/n}-1)$ for $n = 3$; conclude. *Expected evidence:* numbers and conclusion. *Rubric:* 3 = U = 0.40, bound ≈ 0.780, schedulable by the sufficient test with the caveat that failing the bound would not prove unschedulability; 2 = caveat missing; 1 = arithmetic error; 0 = none.

**EX024 — Patch decision.** *Objective:* make a risk-based patch decision. *Inputs:* a remote-code-execution vulnerability in the OS file-sharing service; the service is enabled on the historian but blocked by the control-zone firewall from all zones except the engineering zone; vendor certification of the patch is 30 days away. *Steps:* recommend patch / mitigate / accept, with interim controls and a review date. *Expected evidence:* decision note. *Rubric:* 3 = mitigation (disable service or restrict further) now, patch after certification, monitoring, date; 2 = no interim control; 1 = "patch immediately" ignoring vendor support or "accept" without reasoning; 0 = none.

### Chapter synthesis

The OS determines both timing and the security baseline. Put deadlines on real-time platforms. Apply least privilege, allowlisting, hardening and off-host logging. Patch on assessed risk with tested procedures and compensating controls when you cannot patch yet, and keep a mirror environment to make that possible.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue studying — chapter 12 of 50

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes and connection

After this chapter you can (1) design relational and time-series data models for operational data; (2) explain transactions, consistency and replication; (3) protect data integrity with constraints, provenance and hash chains, and say exactly what each detects; and (4) plan data flows between control systems and enterprise analytics without opening a path into control. It builds on Chapters 9 and 11 and prepares Chapters 22 (data models) and 29 (measurement).

### 13.1 Models for operational data

[Codd (1970)](https://doi.org/10.1145/362384.362685) introduced the relational model: data as relations (tables) with keys, manipulated by set operations. Asset registers, work orders and user accounts fit it well. Process data — thousands of tags sampled every second — usually goes to a **historian**, a time-series store optimised for append and range queries, often with compression that discards changes smaller than a deadband. Know what your historian discards: forensic analysis may need values it never stored.

LRWA's historian stores the Hollin Hill level with deadband compression, so changes smaller than the deadband are never kept.

### 13.2 Transactions, consistency and replication

A **transaction** groups operations so that they all happen or none do (atomicity), leaving data valid (consistency), unaffected by concurrent transactions (isolation) and surviving crashes (durability). Replication copies data for availability; when replicas can disagree, systems choose between consistency and availability during a network partition. For operations: an operator's acknowledged alarm must not reappear as unacknowledged after failover; a setpoint change must not be applied twice.

In LRWA's SCADA pair, failover is the moment these properties are tested: integration testing should confirm that acknowledged alarms and applied setpoints survive the switch exactly once.

### 13.3 Integrity: what each mechanism detects

- **Constraints** (types, ranges, foreign keys) reject impossible values at entry.
- **Provenance** fields (source, collection time, transformation) let you trace a number back.
- **Checksums** detect accidental corruption.
- **Hash chains** link each record to the previous one, so editing any record changes every later hash. They detect modification *if* you have a trusted copy of a later hash (an **anchor**) stored somewhere the attacker cannot alter. They do not detect truncation of the tail unless the anchor includes the record count, and they do not prove the original data were true.
- **Digital signatures** or MACs on records or anchors bind them to a key holder.

### 13.4 Getting data out without letting attacks in

Enterprise teams want control data for reporting and analytics. The safe pattern is to push data outward — from the control zone to a DMZ historian replica — and let enterprise users query the replica, never the control historian. Where the consequence of control-zone compromise is severe, unidirectional gateways (data diodes) enforce outward-only flow physically. Lab 5's violation — an enterprise script polling an RTU directly — is the anti-pattern.

At LRWA the DMZ historian replica serves finance and asset teams, and the forgotten enterprise script found in the flow review is being retired in its favour.

### 13.5 Worked example: protecting the incident timeline (synthetic)

After an unexplained reservoir level drop on 4 March in the synthetic record, LRWA must preserve the historian extract for investigation. Lab 6 hash-chains six daily readings and stores the head hash in the incident ticket (the anchor). Editing the 4 March value is detected at index 3 and every later record. Deleting the last record is not detected by comparing heads alone if the attacker also replaces the stored head — which is why the anchor goes into a system outside the attacker's reach, together with the record count.

### 13.6 Practical activity: Lab 6

```python
# Lab 6 - a hash-chained historian extract detects edits, not deletions at the tail (offline)
import hashlib, json
recs = [{"t": f"2026-03-0{d} 06:00", "tag": "HOLLIN_LVL", "v": v} for d, v in zip(range(1, 7), [78.1, 77.4, 79.0, 41.2, 76.5, 77.9])]
def chain(rs):
    prev, out = "0" * 64, []
    for r in rs:
        h = hashlib.sha256((prev + json.dumps(r, sort_keys=True)).encode()).hexdigest()
        out.append(h); prev = h
    return out
anchor = chain(recs)
print("head:", anchor[-1][:16])
tampered = [dict(r) for r in recs]; tampered[3]["v"] = 74.0
bad = [i for i, (a, b) in enumerate(zip(anchor, chain(tampered))) if a != b]
print("first mismatch at index:", bad[0], "mismatches:", len(bad))
print("truncated head matches stored index 4:", chain(recs[:5])[-1] == anchor[4])
```

Expected output:

```text
head: a8407870e41914c1
first mismatch at index: 3 mismatches: 3
truncated head matches stored index 4: True
```

The head hash is what LRWA stores in the incident ticket. Editing the 4 March reading to hide the drop changes the hash at index three and at every later record, so the edit is detected wherever it occurs. The last line shows the weakness: a chain built from the first five records matches the stored hash at index four, so an attacker who deletes the final record and replaces the stored head would go unnoticed. EX025 closes that gap by adding the record count to the anchor.

### 13.7 Common errors and limits

- Treating historian data as complete when compression or deadbands discard detail.
- Hash chains without an independently stored anchor.
- Believing integrity mechanisms prove truth; they prove non-modification since anchoring.
- Bidirectional "reporting" connections into the control zone.
- Losing time zone and clock-source information.

The 4 March investigation depends on avoiding every one of these, from compression gaps to a missing time zone. A historian that drops small changes may have discarded the very values that would show how fast the level fell, an anchor kept on the historian server could be rewritten by the same administrator, and timestamps without a zone make the drop impossible to align with the operator log.

### Exercises — chapter 13

**EX025 — Tail truncation.** *Objective:* close the truncation gap. *Inputs:* Lab 6. *Steps:* (1) show that `chain(recs[:5])` matches the stored hash at index 4; (2) modify the anchor to include the record count and show truncation is detected; (3) state where the anchor should be stored at LRWA and why. *Expected evidence:* code and output. *Rubric:* 3 = demonstration and fix correct, anchor stored outside control and historian admins' reach; 2 = fix incomplete; 1 = not run; 0 = none.

**EX026 — Data flow design.** *Objective:* design analytics access safely. *Inputs:* the finance team wants hourly pump energy data; the asset team wants live pressure data for a dashboard. *Steps:* draw (in text) the flows, zones and direction; state which component enforces direction and what happens if the DMZ replica is compromised. *Expected evidence:* flow description and consequence analysis. *Rubric:* 3 = push to DMZ, no inbound to control, consequence limited to data confidentiality/integrity of the replica; 2 = direction not enforced; 1 = direct query of control historian; 0 = none.

### Chapter synthesis

Model operational data deliberately, know what your historian discards, and use transactions and replication with failover in mind. Every integrity mechanism detects something specific: constraints reject the impossible, hash chains detect edits relative to an independently stored anchor, signatures bind to a key holder — none proves truth. Move data outward to a DMZ and never let reporting become a path into control.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue studying — chapter 13 of 50

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes and connection

After this chapter you can (1) apply a secure software development lifecycle to infrastructure software; (2) manage requirements, design reviews, code review and inspections; (3) manage dependencies and the software supply chain with SBOMs and provenance; and (4) plan releases and updates for long-lived embedded and OT software. It builds on Chapters 5 and 9 and prepares Chapters 28, 31 and 39.

### 14.1 Why process matters

[Brooks (1987)](https://doi.org/10.1109/MC.1987.1663532) argued that software's essential difficulties — complexity, conformity, changeability, invisibility — admit no single breakthrough. Process does not remove them; it makes errors visible early, when fixing them is cheap, and leaves evidence that the work was done. For critical infrastructure the evidence is part of the product: regulators, insurers and asset owners will ask for it.

For TMRP's gateway, that evidence includes the threat model review, the test results and the signed build, all of which go into the dossier.

### 14.2 A secure development lifecycle

The [NIST Secure Software Development Framework (SP 800-218)](https://csrc.nist.gov/pubs/sp/800/218/final) groups practices into preparing the organisation, protecting the software, producing well-secured software and responding to vulnerabilities. Concretely: security requirements and threat models with every feature; secure coding standards; peer review; automated static analysis and tests in continuous integration; protected build systems; vulnerability intake and disclosure; and patches with clear advisories. [CISA's Secure by Design](https://www.cisa.gov/securebydesign) principles add that manufacturers should take ownership of customer security outcomes — secure defaults, no default passwords, memory-safe languages where feasible.

### 14.3 Reviews and inspections

[Fagan (1976)](https://doi.org/10.1147/sj.153.0182) described formal design and code inspections with defined roles and checklists, reporting that they found defects earlier and more cheaply than testing. Modern code review is lighter but keeps the principles: a second competent person reads every change, with a checklist that includes input validation, authentication, error handling and logging. Complexity metrics such as McCabe's cyclomatic complexity ([McCabe, 1976](https://doi.org/10.1109/TSE.1976.233837)) flag functions that are hard to test.

At LRWA every change to the gateway code is read by a second engineer with a checklist.

### 14.4 Dependencies and the supply chain

Most software is assembled from third-party components. A **software bill of materials (SBOM)** lists them so that, when a vulnerability is announced, you can tell whether you are affected ([CISA SBOM resources](https://www.cisa.gov/sbom)). **Provenance** — verifiable evidence of how and from what an artifact was built — protects against tampered builds; the [SLSA framework](https://slsa.dev/) defines levels of build integrity, and [reproducible builds](https://reproducible-builds.org/) let independent parties confirm that a binary matches its source.

### 14.5 Releases for long-lived systems

OT software may be maintained for twenty years. Plan for: signed updates; rollback; staged deployment (test bench, one site, fleet); compatibility windows; end-of-support dates published in advance; and an update process that works when a site is reachable only intermittently. An update mechanism is itself an attack surface and must be authenticated.

For TMRP the plan is concrete: the gateway moves from bench to PS2 to PS1, a rollback image is retained at each stage, and updates must reach stations that are only intermittently reachable over LTE. Because the gateways are recorded as technical debt with a three-year horizon, the end-of-support date is published from the start.

### 14.6 Worked example: the telemetry gateway project (synthetic)

TMRP must build a small gateway that adds HMAC authentication for legacy RTUs at PS1 and PS2. The plan: requirements R1, R2 and R7 traced to tests; a threat model reviewed by a second engineer; Python standard library only, avoiding third-party dependencies; static analysis and unit tests in CI; builds on a dedicated runner with signed artifacts and an SBOM (trivially short here); deployment to a bench, then PS2, then PS1; and a rollback image retained. Each step leaves a record in the evidence dossier (Chapter 48).

### 14.7 Practical activity

Write a one-page SSDF-mapped plan for a small tool you have written: for each of the four practice groups, list two concrete practices and the evidence each produces.

Choose something real that you have written, such as your Lab 3 parser, so the practices are concrete. For each practice, name the evidence it leaves: a review record, a test report, a signed build or an advisory template. If a practice would leave no evidence, either change it or admit that it is only an intention. Compare your plan with the TMRP gateway plan and note one practice you would add.

### 14.8 Common errors and limits

- Process documents without the practices they describe.
- Code review without a checklist or without authority to block.
- Dependencies pulled at build time without pinning or provenance.
- Update mechanisms without authentication or rollback.
- No published end-of-support date.

The TMRP gateway plan was written to avoid each of these. It uses the standard library only, so there are no unpinned dependencies; reviews follow a checklist; builds are signed with an SBOM; deployment keeps a rollback image; and the gateways have a published three-year horizon.

### Exercises — chapter 14

**EX027 — Review checklist.** *Objective:* create a review checklist for infrastructure code. *Inputs:* Lab 3 and Lab 8 code. *Steps:* write a ten-item checklist and apply it to both labs, recording one finding for each. *Expected evidence:* checklist and two findings. *Rubric:* 3 = checklist specific (input validation, constant-time comparison, key handling, error paths, logging, limits) and findings real; 2 = generic checklist; 1 = no findings; 0 = none.

**EX028 — SBOM response drill.** *Objective:* use an SBOM in a vulnerability response. *Inputs:* a synthetic SBOM listing `libmodbus 3.1.6`, `openssl 3.0.8`, `zlib 1.2.13` for the RTU-B firmware, and an advisory for one of these. *Steps:* describe the triage steps from advisory to decision, including how you determine exploitability in your deployment. *Expected evidence:* procedure. *Rubric:* 3 = match, reachability analysis, vendor contact, compensating control, communication; 2 = no reachability; 1 = "update everything"; 0 = none.

### Chapter synthesis

Process makes errors visible early and leaves evidence. Use a recognised secure development framework, review with checklists, measure complexity, and treat dependencies and builds as part of your attack surface with SBOMs and provenance. Design releases and updates for decades, with authentication, staging and rollback.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue studying — chapter 14 of 50

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes and connection

After this chapter you can (1) define confidentiality, integrity and availability and explain why their priority differs in infrastructure; (2) describe threats, vulnerabilities, risk and controls and relate them in a risk assessment; (3) apply design principles from the security literature; and (4) map a system's controls to a recognised framework. It integrates Chapters 1–14 and prepares the security architecture and identity chapters (18–19) and the sector chapters (20 onward).

### 15.1 The properties

**Confidentiality** limits who can read information; **integrity** ensures information and systems are not altered without authorisation; **availability** ensures timely, reliable access. In enterprise IT, confidentiality often leads. In infrastructure, the physical process ranks first: integrity and availability of control, then safety, then confidentiality — though confidentiality of network designs and credentials protects the others. [Avizienis et al. (2004)](https://doi.org/10.1109/TDSC.2004.2) place security alongside reliability, safety and maintainability as attributes of dependability; their taxonomy of faults, errors and failures is used throughout this book.

### 15.2 Threat, vulnerability, risk

A **threat** is a potential cause of harm (an actor with capability and intent, or a natural hazard); a **vulnerability** is a weakness that a threat can exploit; **risk** combines likelihood and consequence. [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) describes risk assessment as identifying threat sources and events, vulnerabilities, likelihood and impact. In infrastructure, start from consequence: what are the worst things that could happen to the service and to people? Idaho National Laboratory's [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/) method begins this way, asking which functions' loss or misuse would be unacceptable and working backward to what an adversary would need.

### 15.3 Controls and principles

Controls are preventive, detective, corrective or compensating, and technical, procedural or physical. Design principles from [Saltzer and Schroeder (1975)](https://doi.org/10.1109/PROC.1975.9939): economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism and psychological acceptability. Add **defence in depth** (layers whose failures are independent) and **assume breach** (design so that a compromise of one layer is detected and contained).

In TMRP's design, local manual mode with a physical key switch is an example of separation of privilege, and the independent chlorine analyser is a detection layer outside the systems it watches.

### 15.4 Frameworks

Frameworks give structure and a common vocabulary. The [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) organises outcomes as Govern, Identify, Protect, Detect, Respond and Recover. The [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) catalogue lists controls; [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) specifies requirements for industrial automation systems and components, with security levels; the UK's [NCSC Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf) is outcome-based for essential services. A framework is a checklist of outcomes, not evidence that a design achieves them.

### 15.5 Worked example: the first TMRP risk table (synthetic)

| Consequence | Threat event | Vulnerability | Existing control | Proposed control |
|---|---|---|---|---|
| Hospital loses supply > 4 h | Forged stop commands to PS3/PS4 | Unauthenticated Modbus over LTE | Carrier encryption | Authenticated telemetry (R1/R2), local manual mode |
| Unsafe chlorine levels | Dosing setpoint manipulated | No setpoint bounds at controller | Operator observation | Controller-side bounds (R3), independent analyser alarm (R9) |
| Loss of visibility | Telemetry outage during grid loss | Cabinet battery 6 h at end of life | None | 24 h battery (R5) |
| Slow recovery | Ransomware on SCADA servers | Backups online, same domain | Nightly backups | Offline backups, tested restoration (R6) |

Each row names a consequence in service terms first. The table is a hypothesis to be refined in Chapters 23 and 27.

### 15.6 Practical activity

Map each proposed control in §15.5 to one CSF 2.0 function and one SP 800-53 control family, citing the documents.

For each row of the TMRP risk table, choose the CSF function that best describes the proposed control's main purpose, and note where a control serves two. Authenticated telemetry is mainly protective, the independent analyser alarm is mainly detective, and tested offline backups support recovery. Cite the framework documents with their versions. Then write one sentence for each row explaining what the mapping does not tell you, because a correct mapping is still not evidence that the control works at LRWA.

### 15.7 Common errors and limits

- Copying enterprise priorities into OT.
- Risk registers that list vulnerabilities without consequences.
- "Defence in depth" layers that share a single point of failure.
- Treating framework mapping as proof of security.
- Likelihood scores with no stated basis.

The first TMRP risk table avoids these by naming each consequence in service terms first, so every vulnerability is tied to a harm, and by treating its likelihoods as hypotheses to refine in later chapters. Its layers are checked for shared dependencies before being called independent.

### Exercises — chapter 15

**EX029 — Principle audit.** *Objective:* apply design principles. *Inputs:* Lab 8 and the pump state machine of §9.5. *Steps:* for each, identify two Saltzer–Schroeder principles applied and one violated or not addressed, and propose a fix. *Expected evidence:* table. *Rubric:* 3 = principles applied correctly with a credible gap (e.g., Lab 8 key hard-coded violates separation/least privilege; open design is respected by HMAC); 2 = one misattribution; 1 = names only; 0 = none.

**EX030 — Consequence-first scenario.** *Objective:* start from consequence. *Inputs:* LRWA's service. *Steps:* identify two unacceptable consequences, and for each, the functions an adversary would need to misuse and the cheapest engineering control that would make the consequence physically impossible or bounded. *Expected evidence:* half page. *Rubric:* 3 = consequences in service terms, functions specific, at least one engineered physical bound (e.g., mechanical overpressure relief, hard-wired chlorine pump limit); 2 = controls all digital; 1 = generic; 0 = none.

### Chapter synthesis

Infrastructure security protects a physical service: integrity and availability of control and safety lead. Start from consequence, then threats and vulnerabilities, then controls. Apply enduring design principles, layer defences whose failures are independent, assume breach, and use frameworks as structured checklists — not as evidence.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue studying — chapter 15 of 50

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes and connection

After this chapter you can (1) apply the systems engineering lifecycle — concept, requirements, architecture, design, integration, verification, validation, operation, retirement — to a security programme; (2) decompose stakeholder needs into system and subsystem requirements with traceability; (3) manage interfaces and configuration; and (4) integrate security engineering into systems engineering rather than bolting it on. It builds on Chapters 5 and 14 and frames the whole second half of the book.

### 16.1 The lifecycle and the V

Systems engineering manages complexity by moving from needs to requirements to architecture to components, then back up through integration and verification. The **V-model** pairs each level of decomposition on the left with a level of verification on the right: stakeholder needs with validation, system requirements with system verification, subsystem design with integration tests, components with unit tests. The [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) describes this lifecycle and its technical reviews. Iterative development does not abolish the V; it runs smaller Vs more often.

### 16.2 Needs, requirements, traceability

Stakeholder needs are what people need the system to achieve, in their language: "the hospital must not lose water for more than four hours". System requirements translate needs into verifiable statements about the system (Chapter 5). **Traceability** links every requirement upward to a need and downward to design elements and verification. A requirement with no parent is gold-plating or a hidden need; a need with no requirement is a gap; a requirement with no verification is an unsupported claim (Chapter 38 and Lab 14).

### 16.3 Interfaces and configuration

Most system failures happen at interfaces — between subsystems, organisations or people. An **interface control document** specifies data, timing, protocols, power, physical connections and responsibilities on each side. **Configuration management** identifies each item (hardware, firmware versions, settings, documents), controls changes through review and keeps records so that the as-built system is known. In security, an unknown configuration is an unknown attack surface.

TMRP's three interface control documents cover RTU to gateway, gateway to SCADA and SCADA to DMZ. Each names an owner on both sides.

### 16.4 Security as a systems engineering discipline

[NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) frames systems security engineering as security activities embedded in the systems engineering technical processes: stakeholder protection needs, security requirements, architectural design for security, verification of security claims, and secure operation and disposal. Its companion, [SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1), addresses cyber resiliency: anticipating, withstanding, recovering from and adapting to adverse conditions including attack.

TMRP follows this approach: N2 is a protection need decomposed into R1 and R2, and each has a planned verification.

### 16.5 Worked example: TMRP as a system (synthetic)

TMRP's top-level needs: N1 keep the hospital supplied (≤ 4 h interruption in credible scenarios); N2 detect and contain misuse of remote control; N3 recover remote operation within one working day; N4 retain operator visibility during grid outages. These decompose into requirements R1–R9 introduced so far (authenticated telemetry, replay rejection, setpoint bounds, local manual mode, 24 h cabinet hold-up, restoration within 8 h, alarms within 60 s, log integrity, independent dosing alarm). The team writes interface control documents for RTU-to-gateway, gateway-to-SCADA and SCADA-to-DMZ, and places all RTU firmware versions and configuration files under change control. Each requirement now has a parent need and a planned verification method.

### 16.6 Practical activity

Draw a traceability matrix N1–N4 × R1–R9 and mark each requirement's parent(s). Identify any need with weak coverage.

Use a simple grid with needs as columns and requirements as rows, and mark each requirement's parent or parents. Some requirements serve more than one need: R5 supports visibility during grid outages, and R1 supports both containment and hospital supply. When you have finished, count the requirements under each need. A need supported by only one requirement deserves a second look, because a single failed test would leave it unsupported in the dossier.

### 16.7 Common errors and limits

- Requirements written after design to justify it.
- Interfaces owned by nobody.
- Configuration known only by the commissioning engineer.
- Security requirements in a separate document, never traced or verified.
- Treating the V-model as a waterfall excuse to defer testing.

In TMRP each of these has a counter-measure: requirements trace to N1 to N4, each interface has an owner, and RTU firmware and configuration are under change control. Verification is planned for every requirement before design starts, so the V is not used as a reason to defer testing.

### Exercises — chapter 16

**EX031 — Trace and find gaps.** *Objective:* build and analyse a traceability matrix. *Inputs:* §16.5. *Steps:* assign each of R1–R9 to its parent need(s); identify which need relies on the fewest requirements and propose one additional requirement. *Expected evidence:* matrix and proposal. *Rubric:* 3 = defensible mapping, weakest need identified with a verifiable new requirement; 2 = mapping errors; 1 = no proposal; 0 = none.

**EX032 — Interface control.** *Objective:* specify an interface completely. *Inputs:* the gateway-to-SCADA interface. *Steps:* list at least eight interface attributes with example values (data items, encoding, rate, latency, authentication, error handling, time source, ownership, change process). *Expected evidence:* table. *Rubric:* 3 = complete and consistent with Labs 8 and 13; 2 = missing security or ownership attributes; 1 = data only; 0 = none.

### Chapter synthesis

Systems engineering moves from needs to verified, validated systems through traceable requirements, managed interfaces and controlled configuration. Security belongs inside those processes: protection needs become requirements, requirements become architecture and design, and every security claim needs verification evidence.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue studying — chapter 16 of 50

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes and connection

After this chapter you can (1) describe open- and closed-loop control, setpoints, error and actuator limits; (2) explain proportional–integral (PI) control and integrator wind-up; (3) analyse how false sensor data — a false-data injection — drives a correct controller to an unsafe state; and (4) design residual-based detection using independent physical measurements and state its blind spots. It builds on Chapter 6 and prepares Chapters 27 and 33.

### 17.1 Feedback

A **closed-loop** controller measures a process variable, compares it with a setpoint and adjusts an actuator to reduce the error. Feedback makes systems robust to disturbances and model errors — and makes them trust their sensors completely. [Åström and Murray's *Feedback Systems*](https://fbswiki.org/wiki/index.php/Main_Page), freely available online, is the reference text for this chapter.

At Hollin Hill, the PI controller adjusts PS3's inlet flow to hold the reservoir level at its setpoint. It sees the reservoir only through the level transmitter, so whatever that transmitter reports is, for the controller, the truth. The rest of this chapter follows the consequence of that trust.

### 17.2 PI control

A proportional controller sets actuator output $u = K_p e$; it leaves a steady-state error when a constant disturbance must be balanced. Adding an integral term, $u = K_p e + K_i\int e\,dt$, removes steady-state error because the integral keeps growing until the error is zero. Actuators saturate — a pump cannot deliver more than its maximum flow — and while saturated, the integral keeps growing (**wind-up**), causing overshoot when the actuator comes out of saturation. Anti-wind-up stops integration while saturated.

### 17.3 False data and the trusting controller

If an attacker adds a bias $b$ to the level measurement, the controller regulates the *measured* level to the setpoint, so the *true* level settles at setpoint minus $b$. The controller is functioning perfectly; the process is not. This is the core of process-aware attacks: Stuxnet, as analysed by [Langner (2011)](https://doi.org/10.1109/MSP.2011.67), manipulated centrifuge speeds while replaying normal-looking values to operators. Defences cannot rely on the same sensor stream the attacker controls.

At Hollin Hill, a biased level transmitter would lower the true level while the operator's screen showed the setpoint, so the defence must come from an independent measurement.

### 17.4 Residual-based detection

A **residual** is the difference between what a measurement says and what an independent model predicts. For a reservoir, mass balance predicts level change from independently metered inflow and outflow: $\Delta h = (q_{in} - q_{out})\Delta t / A$. Two detectors: a **step residual** compares the change in measured level with the predicted change over one step; a **cumulative residual** compares the measured level with the level integrated from flows since the last trusted calibration. The step detector catches abrupt bias but not slow drift; the cumulative detector catches drift but accumulates meter error, so it needs periodic recalibration and a threshold above normal meter drift. An attacker who also controls the flow meters defeats both — independence of measurement paths is the real control.

### 17.5 Worked example: Hollin Hill level attack (synthetic)

Lab 7 simulates PI control of Hollin Hill (plan area 1,000 m², setpoint 3.0 m, outflow 300 m³/h, inlet pump 0–600 m³/h) for 48 h. A +1.5 m step bias at 10 h drives the true level down to 1.5 m; both detectors alarm at 10.0 h. A +0.04 m bias — small enough to resemble sensor error — is caught only by the cumulative detector. A slow ramp of 0.05 m/h evades the step detector entirely; the cumulative detector alarms at 10.6 h, by which time the bias is about 0.03 m. Without detection, the ramp leaves the true level at 1.1 m after 48 h.

### 17.6 Practical activity: Lab 7

```python
# Lab 7 - PI level control under sensor-bias attacks, and two residual detectors (synthetic, offline)
def run(attack=None, hours=48, dt=0.1):
    A = 1000.0                         # m2 reservoir plan area: level h (m), volume A*h (m3)
    h, integ, sp, kp, ki = 3.0, 7.5, 3.0, 400.0, 40.0   # integ preloaded so u = 300 at start
    est = h                            # mass-balance estimate from independently metered flows
    prev_meas, step_t, cum_t, hmin = h, None, None, h
    for k in range(int(hours / dt)):
        t = k * dt
        b = attack(t) if attack else 0.0
        meas = h + b
        err = sp - meas
        u = kp * err + ki * integ
        q_in = min(max(u, 0.0), 600.0)              # pump limits 0..600 m3/h
        if 0.0 < u < 600.0: integ += err * dt         # anti-windup
        q_out = 300.0
        if k > 0 and step_t is None and abs((meas - prev_meas) - (est - est_prev)) > 0.05: step_t = round(t, 1)
        if cum_t is None and abs(meas - est) > 0.03: cum_t = round(t, 1)
        prev_meas, est_prev = meas, est
        h += (q_in - q_out) / A * dt; est += (q_in - q_out) / A * dt
        hmin = min(hmin, h)
    return round(h, 2), round(hmin, 2), step_t, cum_t
print("columns: true final level m, true min level m, step-detector alarm h, cumulative-detector alarm h")
print("no attack        ", run())
print("step bias +1.5 m ", run(lambda t: 1.5 if t >= 10 else 0.0))
print("step bias +0.04 m", run(lambda t: 0.04 if t >= 10 else 0.0))
print("ramp 0.05 m/h    ", run(lambda t: 0.05 * (t - 10) if t >= 10 else 0.0))
```

Expected output:

```text
columns: true final level m, true min level m, step-detector alarm h, cumulative-detector alarm h
no attack         (3.0, 3.0, None, None)
step bias +1.5 m  (1.5, 1.4, 10.0, 10.0)
step bias +0.04 m (2.96, 2.95, None, 10.0)
ramp 0.05 m/h     (1.1, 1.1, None, 10.6)
```

Read the four rows against the worked example. Without an attack the level stays at three metres and neither detector fires. The large step bias is caught by both detectors at once, and the true level settles a metre and a half too low. The small step and the slow ramp are where the detectors differ: only the cumulative detector sees them, and the ramp, left alone, drags the true level to about one metre. Remember that the lab's flow meters are perfect, so real detection times would be later.

### 17.7 Common errors and limits

- Equating "the controller worked" with "the process is safe".
- Detection that uses the same data path as the control loop.
- Thresholds set without measuring normal noise and drift.
- Ignoring wind-up and saturation in safety reasoning.
- Simulation results presented as plant behaviour; Lab 7 is a simplified model with perfect flow meters.

For Hollin Hill, EX034 shows the dependence problem plainly: the level sensor and the inlet flow meter are both wired to RTU3, so compromising one RTU defeats both sides of the residual.

### Exercises — chapter 17

**EX033 — Threshold trade-off.** *Objective:* tune a detector. *Inputs:* Lab 7. *Steps:* (1) add Gaussian noise of standard deviation 0.01 m to the measured level (seed 17) and count false alarms of the cumulative detector in the no-attack case at thresholds 0.03 and 0.05; (2) report detection time of the ramp at both thresholds; (3) recommend a threshold. *Expected evidence:* table and recommendation. *Rubric:* 3 = experiment correctly implemented, trade-off explained, recommendation linked to response time; 2 = one threshold only; 1 = not run; 0 = none.

**EX034 — Independence argument.** *Objective:* argue detection independence. *Inputs:* LRWA's architecture: level sensor and inlet flow meter both wired to RTU3; outlet flow meter at PS4 on RTU4. *Steps:* identify which attacker positions defeat the residual detector, and propose an architectural change that improves independence. *Expected evidence:* half page. *Rubric:* 3 = compromise of RTU3 defeats both level and inflow, change proposes separate path (e.g., independent level transmitter to a separate logger or physical gauge check); 2 = partial; 1 = generic; 0 = none.

### Chapter synthesis

Feedback makes systems robust and credulous. A biased sensor drives a correct controller to an incorrect physical state. Detect with residuals built from independent physics, use step and cumulative tests for abrupt and slow attacks, set thresholds from measured noise, and remember that independence of measurement paths — not cleverness of the algorithm — is what defeats a capable attacker.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue studying — chapter 17 of 50

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes and connection

After this chapter you can (1) describe reference architectures for operational technology, including layered models and DMZs; (2) apply zero-trust principles where they fit OT and explain where they do not; (3) design remote access, logging and monitoring architectures; and (4) evaluate an architecture against consequence, not just control count. It builds on Chapters 11, 12 and 15 and prepares Chapters 26 and 27.

### 18.1 Layered OT architectures

OT architectures are commonly described in levels: physical process (level 0), sensors and actuators with basic control (1), supervisory control (2), site operations (3), a demilitarised zone, and enterprise (4–5). The model, which descends from the Purdue reference architecture and appears in the [NIST OT guide](https://csrc.nist.gov/pubs/sp/800/82/r3/final), is a tool for placing assets and conduits, not a law. Modern systems blur levels: cloud-connected sensors, vendor remote services and field devices with direct cellular links.

At LRWA, the SCADA servers sit in the control zone, the RTUs in the field zone and the historian replica in the DMZ.

### 18.2 The DMZ and data brokering

The OT DMZ sits between control and enterprise networks. No direct traffic crosses it: enterprise systems talk to DMZ services (historian replica, patch server, remote-access gateway), which talk to control systems. A useful test: if any enterprise host is compromised, can it send a packet that reaches a controller? If yes, the DMZ is decorative.

At LRWA the flow review applied this test and failed: an enterprise reporting script reached a field RTU directly. Moving that data to the DMZ historian replica is how LRWA makes its DMZ real rather than decorative, and the test is repeated after every new conduit is added.

### 18.3 Zero trust in OT

Zero trust, as described in [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final), removes implicit trust based on network location; every access is authenticated, authorised and evaluated per session. In OT the principle is valuable for human and engineering access — named identities, strong authentication, just-in-time privilege, session recording — and for new devices that support it. It fits poorly where legacy controllers cannot authenticate at all and where control loops cannot tolerate a policy decision point in their path. The engineering answer is to apply zero trust at the boundaries you can (engineering access, data brokering, gateways) and use segmentation and monitoring around what cannot authenticate.

### 18.4 Remote access

Vendor and staff remote access is a leading entry path into OT. Architect it as: an access gateway in the DMZ; multi-factor authentication; named accounts; access approved per session; connections to a jump host, never directly to controllers; session recording; and automatic expiry. The [Oldsmar water treatment incident](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a) was initially attributed to unauthorised remote access via desktop-sharing software; later statements, reported by [WUSF Public Media (2023)](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021), indicated it was likely employee error. Either way, the case illustrates why uncontrolled desktop-sharing on operator workstations is an architectural weakness, and why early incident accounts should be held provisionally.

### 18.5 Monitoring architecture

Network security monitoring in OT is usually passive: copies of traffic from switch mirror ports or taps feed sensors that understand industrial protocols and baseline normal behaviour. Logs from servers, firewalls and gateways go to a collector in the DMZ or a dedicated security zone. Monitoring must not create new paths into control: sensors receive copies only, and management interfaces sit on a separate network.

At LRWA, the passive taps sit at the control zone switch and the LTE head-end, and their management interfaces are kept off the monitored network.

### 18.6 Worked example: TMRP target architecture (synthetic)

LRWA's target: enterprise — firewall — DMZ (historian replica, remote-access gateway with MFA, patch staging, log collector) — firewall — control zone (SCADA pair, engineering jump host) — field conduit over private LTE with application-layer authentication (gateways for legacy RTUs) — RTUs and local control panels with manual mode. Passive monitoring taps sit at the control zone switch and the LTE head-end. The architecture is evaluated against consequences: forged commands require compromising either a field gateway key or the SCADA servers; enterprise compromise yields historian replica data but no packet path to field devices; loss of LTE leaves sites in local automatic or manual mode with 24 h telemetry batteries.

### 18.7 Practical activity

Draw the target architecture in text or a simple diagram and annotate each conduit with the allowlist entries from Lab 5. Then apply the DMZ test of §18.2.

Mark each conduit with its direction and protocol, and show where the passive taps sit. For every allowlist entry, ask which zone initiates the connection and whether the DMZ test still passes if that zone is compromised. Then add the engineering path through the jump host and check that no rule lets an engineering workstation reach a field RTU directly, which was one of LRWA's three flow violations. A diagram that hides direction cannot show whether the DMZ actually works.

### 18.8 Common errors and limits

- DMZs with "temporary" direct rules.
- Zero trust claimed for systems that cannot authenticate.
- Remote access that bypasses the gateway (vendor modems, desktop-sharing tools).
- Monitoring sensors with management interfaces on the monitored network.
- Architectures judged by number of controls rather than consequences prevented.

At LRWA, the third and first errors are the most likely: a vendor wanting quick access to RTU-B for diagnostics, and a temporary direct rule added during an outage. The target architecture answers both with the DMZ access gateway and change control on every conduit.

### Exercises — chapter 18

**EX035 — DMZ test.** *Objective:* test a DMZ design. *Inputs:* a proposed rule letting the enterprise ERP server write work-order status directly to the SCADA database over TCP/1433. *Steps:* apply the DMZ test; propose an alternative design that meets the business need. *Expected evidence:* analysis and design. *Rubric:* 3 = rule rejected with reason, alternative brokers data through the DMZ with the control side pulling or a one-way export; 2 = alternative still inbound; 1 = accepts rule; 0 = none.

**EX036 — Remote access architecture.** *Objective:* design vendor access. *Inputs:* the RTU-B vendor needs quarterly access for diagnostics. *Steps:* specify the access path, authentication, approval, monitoring and expiry; list the evidence that would show the design works. *Expected evidence:* specification and evidence list. *Rubric:* 3 = gateway, MFA, per-session approval, jump host, recording, expiry, and evidence (logs, test of denied direct path); 2 = no evidence; 1 = VPN directly into control; 0 = none.

### Chapter synthesis

Use layered models to place assets and conduits, make the DMZ real by allowing no direct crossing, apply zero trust where systems can authenticate and segmentation where they cannot, put all remote access through a controlled gateway, monitor passively without creating paths, and judge the architecture by the consequences it makes hard to cause.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue studying — chapter 18 of 50

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes and connection

After this chapter you can (1) explain symmetric and public-key cryptography, hashes and MACs, and choose among them; (2) design message authentication with replay protection for constrained telemetry; (3) plan key management — generation, distribution, storage, rotation, revocation — for a field fleet; and (4) design identity and authentication for people and devices. It builds on Chapters 4, 13 and 18 and prepares Chapters 27–28.

### 19.1 Primitives

- **Hash functions** (SHA-256, [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)) map data to a fixed-size digest; finding collisions or preimages should be infeasible. A hash alone authenticates nothing.
- **Symmetric encryption** (AES, [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)) uses one shared key for confidentiality.
- **Message authentication codes** (HMAC, [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final); [RFC 2104](https://www.rfc-editor.org/rfc/rfc2104)) let holders of a shared key verify that a message is unaltered and came from a key holder.
- **Public-key cryptography**, introduced by [Diffie and Hellman (1976)](https://doi.org/10.1109/TIT.1976.1055638) and realised for signatures by [Rivest, Shamir and Adleman (1978)](https://doi.org/10.1145/359340.359342), uses key pairs: anyone can verify a signature with the public key; only the private-key holder can sign.
- **Authenticated encryption** (e.g., AES-GCM) provides confidentiality and integrity together.

Never design your own primitives or protocols when a standard one fits; TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)) is the default for IP links that can run it.

### 19.2 Authenticating telemetry

For a constrained link, a common design is: payload plus a monotonic counter (or timestamp), MAC over both, receiver checks the MAC in constant time, then checks that the counter exceeds the last accepted value. The counter defeats replay; a timestamp with a freshness window defeats delay attacks but needs synchronised clocks. Truncating HMAC-SHA256 to 128 bits is common for bandwidth, with a correspondingly reduced but still very large forgery margin. Persist the last counter or rotate keys on restart, or a restart reopens replay (EX018).

### 19.3 Key management

Keys are where cryptography meets operations. Decide: who generates keys and where (ideally in hardware, never by hand); how they reach devices (factory provisioning, secure enrolment); where they are stored (secure elements, not configuration files); how they rotate (scheduled and after suspected compromise); how they are revoked; and who can access them. One key per device-pair limits the blast radius: compromising one RTU should not let an attacker impersonate another. A single fleet-wide key is a common cause with $\beta \approx 1$ (Chapter 7).

### 19.4 Identity for people and devices

People need named accounts, strong authentication (phishing-resistant multi-factor where possible — see [NIST SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final)), roles mapped to tasks, and prompt removal on departure. Devices need identities too — certificates or provisioned keys — so that a gateway knows which RTU it is talking to. Shared or default credentials are the most common identity failure in OT.

In TMRP, operators use named accounts with strong authentication at the SCADA servers, and each RTU has its own key, so the gateway knows which station sent each message.

### 19.5 Worked example: TMRP message format (synthetic)

ADR-007 chose HMAC with counters. The frame in Lab 8 carries an 8-byte counter, 2-byte station ID, 2-byte level and a 16-byte truncated HMAC-SHA256: 28 bytes, of which 22 are overhead relative to a 6-byte unauthenticated payload. Per-station keys are generated in the gateway's secure element at enrolment and stored in the RTU's key store; the SCADA side holds them in a hardware security module. Keys rotate annually and immediately on suspected compromise; the counter is persisted in non-volatile memory at each increment of 1,000 with a forward skip on restart, so replay of old messages remains impossible.

### 19.6 Practical activity: Lab 8

```python
# Lab 8 - authenticated telemetry with a counter: tamper and replay are rejected (synthetic key, offline)
import hmac, hashlib, struct
KEY = bytes.fromhex("00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff")  # demo key only
def seal(ctr, station, level_cm):
    body = struct.pack(">QHH", ctr, station, level_cm)
    return body + hmac.new(KEY, body, hashlib.sha256).digest()[:16]
class Receiver:
    def __init__(self): self.last = {}
    def accept(self, msg):
        body, tag = msg[:12], msg[12:]
        if not hmac.compare_digest(tag, hmac.new(KEY, body, hashlib.sha256).digest()[:16]): return "reject: tag"
        ctr, st, lvl = struct.unpack(">QHH", body)
        if ctr <= self.last.get(st, -1): return "reject: replay"
        self.last[st] = ctr; return f"ok st={st} ctr={ctr} level={lvl}cm"
r = Receiver(); m1, m2 = seal(1, 3, 312), seal(2, 3, 309)
forged = m2[:10] + struct.pack(">H", 150) + m2[12:]
for name, m in [("m1", m1), ("m2", m2), ("replay m1", m1), ("forged", forged)]: print(f"{name:10}", r.accept(m))
print("frame bytes:", len(m1), "overhead vs 6-byte payload:", len(m1) - 6)
```

Expected output:

```text
m1         ok st=3 ctr=1 level=312cm
m2         ok st=3 ctr=2 level=309cm
replay m1  reject: replay
forged     reject: tag
frame bytes: 28 overhead vs 6-byte payload: 22
```

The key in the lab is a published demonstration value; real keys must never appear in source code.

The first two messages from station three are accepted with increasing counters. Replaying the first message is refused because its counter is not greater than the last accepted value, and the forged message, with its level changed from 309 to 150 centimetres, fails the tag check. The final line confirms the frame size used in ADR-007: twenty-eight bytes, twenty-two of them overhead. The lab keeps state only in memory, which is why EX018 asks what happens after a restart.

### 19.7 Common errors and limits

- Hashes or CRCs used as if they were MACs.
- Non-constant-time tag comparison.
- Replay protection lost on restart.
- Fleet-wide shared keys; keys in configuration files or source code.
- Default passwords and shared accounts.
- Cryptographic choices without a plan for the system's lifetime (algorithm agility).

TMRP's design answers each item: tags are compared in constant time, counters persist across restarts, keys are per station in secure hardware, and the message format gains a suite identifier for future algorithm changes. Each choice has a test.

### Exercises — chapter 19

**EX037 — Counter persistence.** *Objective:* design restart-safe replay protection. *Inputs:* §19.5 (persist every 1,000 increments). *Steps:* explain why the RTU must skip forward on restart and by how much at least; state what the receiver must persist. *Expected evidence:* explanation. *Rubric:* 3 = skip ≥ 1,000 beyond last persisted value so no counter is reused, receiver persists last-accepted per station or rotates keys; 2 = one side only; 1 = vague; 0 = none.

**EX038 — Blast radius.** *Objective:* compare key designs. *Inputs:* 42 field stations; option A one fleet key; option B one key per station. *Steps:* compare the consequence of extracting a key from one stolen RTU, the rotation effort after that theft, and the storage required at SCADA. *Expected evidence:* table and recommendation. *Rubric:* 3 = A lets the thief forge any station and forces fleet-wide rotation; B confines forgery to one station with one rotation; storage trivial; recommendation B; 2 = one dimension missing; 1 = recommendation without reasoning; 0 = none.

### Chapter synthesis

Choose standard primitives for the property you need: hashes for fingerprints, MACs or signatures for authenticity, authenticated encryption for confidentiality with integrity. Add freshness to defeat replay and keep it across restarts. Key management is the real system: per-device keys in hardware, rotation and revocation. Give people and devices distinct, strongly authenticated identities.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue studying — chapter 19 of 50

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Chapter 20 — Critical infrastructure and sector security: engineering context

### Learning outcomes and connection

After this chapter you can (1) describe how critical infrastructure is defined and organised into sectors, and the regulatory landscape engineers work within; (2) characterise sectors by their physical processes, consequence units and technology; (3) describe interdependencies between sectors; and (4) learn from documented incidents at the level their public sources support. It is the bridge from foundations (Chapters 1–19) to the field chapters (21–50).

### 20.1 What makes infrastructure "critical"

Governments designate as critical the assets, systems and networks whose incapacity would seriously harm security, the economy, public health or safety. The United States identifies sixteen [critical infrastructure sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors) and, more recently, a set of [National Critical Functions](https://www.cisa.gov/national-critical-functions-set) that cut across organisations. The European Union's [NIS2 Directive (2022/2555)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/) sets cybersecurity obligations for essential and important entities, and the [CER Directive (2022/2557)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj) addresses the resilience of critical entities more broadly. Sector rules add detail: [NERC CIP standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx) for North American bulk electric systems, the [America's Water Infrastructure Act 2018 risk assessment requirements](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans) for US community water systems, [DORA (2022/2554)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) for EU finance, and the [HHS Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). These change; cite version and date and re-verify.

### 20.2 Sectors as engineering systems

Each sector has a physical or service process, a **consequence unit** and characteristic technology.

| Sector | Process | Consequence unit | Typical technology |
|---|---|---|---|
| Water | Treat and distribute water | People without safe water × hours | PLCs/RTUs, SCADA, dosing, telemetry |
| Electricity | Generate, transmit, distribute | MW or customers interrupted × hours | Protection relays, EMS/DMS, substation automation |
| Healthcare | Diagnose and treat | Delayed care, diversions, harm | EHR, medical devices, building systems |
| Transport | Move people and goods | Journeys disrupted, safety incidents | Signalling, traffic control, ticketing |
| Finance | Clear and settle | Transactions failed or delayed | Payment systems, market infrastructures |
| Communications | Carry voice and data | Subscribers affected × hours | Core networks, radio access, timing |

The table is a simplification for engineering orientation; each row is a career.

### 20.3 Interdependency

[Rinaldi, Peerenboom and Kelly (2001)](https://doi.org/10.1109/37.969131) classify interdependencies as physical, cyber, geographic and logical. Water needs electricity for pumping; electricity restoration needs communications; hospitals need water, power and communications; nearly everything needs accurate time. Interdependency turns local failures into regional ones and turns shared suppliers into common causes. The July 2024 faulty CrowdStrike update, which Microsoft estimated affected about 8.5 million Windows devices ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)), was not an attack, but it disrupted airlines, hospitals and other services at once through a shared software dependency.

### 20.4 Learning from documented incidents

Public incident reports are valuable and partial. Use them at the level of their sources. The [Colonial Pipeline incident](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years) in 2021 involved ransomware on business IT; the company shut down pipeline operations as a precaution — a reminder that dependency of operations on IT systems (billing, scheduling) can halt physical service without any OT compromise. The [2015 Ukrainian grid attack](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01) used remote access to operate breakers and damaged recovery capabilities. The [2017 WannaCry](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/) outbreak disrupted NHS services in England. Each has documented details and open questions; where early accounts were revised, as at Oldsmar, cite both.

### 20.5 Worked example: placing LRWA in context (synthetic)

LRWA is a water utility with a hospital among its critical customers. Its consequence unit is people-hours without safe water, weighted for vulnerable users; St Brenna's on-site storage gives about four hours of buffer. Its interdependencies: electricity (pumping, treatment), communications (LTE telemetry), chemical supply (chlorine) and time (log correlation). Its regulatory context is assumed to include a risk-and-resilience assessment duty similar to AWIA. The TMRP's scope is defined by these: the programme is not "secure the SCADA" but "keep safe water flowing to people under credible adverse conditions, including attack".

### 20.6 Practical activity

Choose one sector other than water. From public sources only, build its row of §20.2 in more detail: three consequence units, three typical technologies, two key regulations with version and date, and one documented incident with its source.

Keep the profile at the level of your sources. For each regulation, give the version, the date you consulted it and the entities it covers. For the incident, state only what the cited report says, and note any later revision, as with Oldsmar. Then compare your sector's consequence unit with LRWA's people-hours without safe water, and note one interdependency your sector shares with water, such as electricity, communications or time.

### 20.7 Common errors and limits

- Treating "critical infrastructure" as a technology category rather than a consequence category.
- Regulations quoted without version or date.
- Incident narratives repeated beyond what sources support.
- Ignoring IT dependencies of physical operations.
- One-sector thinking in an interdependent world.

LRWA's own context shows why these matter. Its critical status comes from St Brenna's and its other customers, not from the technology it runs. Its operations depend on electricity, LTE, chlorine supply and accurate time, so analysing water in isolation would miss the hidden feeder dependency found earlier. Any regulatory duty it relies on must be cited with a version and a date.

### Exercises — chapter 20

**EX039 — Sector profile.** *Objective:* profile a sector from public sources. *Inputs:* §20.6. *Steps:* produce the profile with citations. *Expected evidence:* one page. *Rubric:* 3 = accurate, cited, consequence units measurable, incident described within its sources; 2 = one uncited claim; 1 = generic; 0 = none.

**EX040 — Shared dependency.** *Objective:* reason about common causes across sectors. *Inputs:* the July 2024 CrowdStrike outage as described by Microsoft. *Steps:* explain in 200 words why a non-malicious software update produced cross-sector disruption, what engineering property it reveals, and one design practice that limits such events. *Expected evidence:* text. *Rubric:* 3 = shared dependency/common cause, privileged auto-updating component, staged rollout or diversity as practice, claims within sources; 2 = practice generic; 1 = calls it an attack; 0 = none.

### Chapter synthesis

Critical infrastructure is defined by consequence. Sectors differ in process, consequence units and technology but share interdependency on power, communications, time and common suppliers. Work within regulations by version and date, learn from incidents only as far as their sources go, and define every security programme by the service and people it protects.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue studying — chapter 20 of 50

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 →](#ch-21)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Chapter 21 — Critical infrastructure and sector security: requirements

### Learning outcomes and connection

After this chapter you can (1) elicit security and resilience requirements from consequences, stakeholders, regulations and threat information; (2) write performance-based requirements for degraded operation, recovery and safety, not only for protection; (3) derive component requirements from system requirements using security levels; and (4) negotiate requirement conflicts explicitly. It applies Chapters 5 and 16 to the sector and prepares Chapter 22.

### 21.1 Sources of requirements

Infrastructure security requirements come from five sources, and a good set traces to all of them: **consequences** (what must never happen, and what must be restored how fast); **stakeholders** (operators, customers such as hospitals, emergency services, regulators); **regulations and standards** (e.g., AWIA risk assessments, NERC CIP, NIS2 risk-management measures); **threat information** (adversary capabilities documented in sources such as [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) and CISA advisories); and **constraints** (legacy equipment, budget, staffing, safety certification).

### 21.2 Requirements for degraded operation

A system that is either "secure" or "compromised" is badly specified. Write requirements for the states in between: *During loss of the telemetry network, each pumping station shall continue in local automatic control within its configured limits for at least 72 h.* *During suspected compromise of the SCADA servers, operators shall be able to run PS3 and PS4 in local manual mode with documented procedures and staffing within 1 h of the decision.* *After an incident, remote operation shall be restored within 8 h of the decision to restore, from verified offline backups.* These are the requirements that keep people supplied.

### 21.3 Security levels and component requirements

IEC 62443-3-3 and 62443-4-2 express system and component requirements against **security levels** (SL 1–4) that reflect the capability of the adversary to be resisted, from casual or coincidental violation up to sophisticated, well-resourced attack ([ISA/IEC 62443 series overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). The risk assessment for design (IEC 62443-3-2, [catalogue page](https://webstore.iec.ch/en/publication/30727)) partitions the system into zones and conduits and assigns a target level to each. A target level then becomes concrete component requirements — for example, authentication of all human users, or protection of communication integrity. The standard text is not freely available; cite clauses only from a copy you have lawfully obtained.

### 21.4 Conflicts and negotiation

Requirements conflict: fast operator access versus strong authentication; frequent patching versus availability; detailed logging versus storage at remote sites; vendor support versus network isolation. Do not resolve conflicts silently in design. Record each, its options, and the decision with its owner — usually the person who owns the operational risk.

TMRP's first recorded conflict is between R4's local manual mode and R1's authentication, resolved with a key switch, an alarm and a local log. The owner is operations, which carries the risk of slower manual access.

### 21.5 Worked example: TMRP requirement set v1.0 (synthetic)

| ID | Requirement | Source | Verification |
|---|---|---|---|
| R1 | Telemetry and commands between field and SCADA shall carry a MAC over contents and counter; failed checks shall be rejected and alarmed. | Consequence (forged commands), ADR-007 | Test (T1, T2) |
| R2 | Replayed messages shall be rejected, including after restart of either end. | Threat (replay) | Test (T2) |
| R3 | Controllers shall reject setpoints outside configured physical bounds or exceeding the configured step, including non-finite values. | Consequence (unsafe operation) | Test (T3) |
| R4 | Each station shall support local manual operation independent of SCADA and the network. | Degraded operation | Demonstration |
| R5 | Field telemetry shall operate ≥ 24 h on battery at end-of-life capacity. | Stakeholder (visibility) | Analysis + test (T4) |
| R6 | Remote operation shall be restorable within 8 h from offline backups. | Recovery | Trial (T7, Chapter 47) |
| R7 | Priority alarms shall reach operator screens within 60 s for 99% of events. | Operations | Test (T5) |
| R8 | Security logs shall be integrity-protected with anchors outside the control zone. | Investigation | Test (T6) |
| R9 | Loss of chlorine dosing shall alarm within 15 min via a path independent of the dosing controller. | Consequence (unsafe water) | Test |

Conflict recorded: R4's local manual mode creates a path that bypasses R1's authentication. Resolution: manual mode requires physical key-switch at the panel, is alarmed at SCADA, and is logged locally.

### 21.6 Practical activity

Choose one degraded state not yet covered (e.g., loss of the chlorine supplier for 7 days) and write a requirement, its source, and verification method.

Write the requirement in the same form as the TMRP table: an identifier, a single verifiable statement, its source and a verification method. A seven-day loss of chlorine supply, for example, might lead to a minimum on-site chemical stock with an inspection, and a procedure for an alternative supplier tested by exercise. Check that your requirement does not conflict with an existing one, and if it does, record the conflict and who should decide it.

### 21.7 Common errors and limits

- Requirements for protection only, none for degradation and recovery.
- Security levels assigned without a documented risk assessment.
- Citing standard clauses without access to the text.
- Conflicts resolved silently by whoever writes the design.
- Requirements that cannot be verified within the programme's means.

TMRP's set avoids the first error by including R4, R5 and R6 for degraded operation and recovery, and avoids the fourth by recording the local manual conflict openly. Every requirement in the set can be verified with the programme's own bench, trial or demonstration.

### Exercises — chapter 21

**EX041 — Degraded-state requirements.** *Objective:* specify behaviour under stress. *Inputs:* LRWA, scenario "SCADA servers encrypted by ransomware". *Steps:* write three requirements covering continued service, detection/containment and restoration, each with source and verification. *Expected evidence:* table. *Rubric:* 3 = measurable, cover all three phases, realistic verification; 2 = one phase missing; 1 = protection only; 0 = none.

**EX042 — Conflict record.** *Objective:* document a conflict. *Inputs:* operators want the HMI to stay logged in all shift; R-new requires re-authentication after 15 min inactivity. *Steps:* write a conflict record with options, recommended resolution and owner. *Expected evidence:* record. *Rubric:* 3 = options include compensating controls (physical access control of the control room, view-only lock with quick re-auth for control actions), owner named by role; 2 = no owner; 1 = picks a side without options; 0 = none.

### Chapter synthesis

Derive requirements from consequences, stakeholders, regulations, threats and constraints. Specify degraded operation and recovery as carefully as protection. Translate target security levels into concrete component requirements through a documented risk assessment, and record every conflict with options, decision and owner.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Continue studying — chapter 21 of 50

[← Chapter 20](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 →](#ch-22)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Chapter 22 — Critical infrastructure and sector security: system and data models

### Learning outcomes and connection

After this chapter you can (1) build an asset inventory and a system model that supports security analysis; (2) model functional dependencies, data flows and trust boundaries; (3) represent degraded states, not just up/down; and (4) keep the model current and protected as sensitive information. It builds on Chapters 2, 13 and 21 and prepares Chapter 23 (threat and failure analysis).

### 22.1 Inventory first

You cannot protect what you do not know. An OT asset inventory records, for each device: identity, location, function, zone, network addresses, hardware and firmware versions, communication relationships, owner, criticality and support status. Build it from several sources and reconcile: design documents, passive network monitoring, configuration exports and site walk-downs. Each source misses things — documents drift, passive monitoring misses quiet devices, walk-downs miss virtual ones.

For LRWA, the inventory covers all 42 field stations, the SCADA pair and the gateways, built from design documents, passive monitoring at the control switch and LTE head-end, and site visits.

### 22.2 Three views of a system

- **Functional view:** what the system does — functions such as "maintain reservoir level", "disinfect", "provide operator visibility" — and which functions depend on which (Lab 2's graph).
- **Physical/network view:** where assets are and how they connect — zones, conduits, links.
- **Data-flow view:** which data move where, in which direction, with which protection, across which **trust boundaries**. Data-flow diagrams with trust boundaries are the input to threat modelling (Chapter 23).

Keep the views linked: every function maps to the assets that implement it; every flow maps to a conduit.

### 22.3 Degraded states

Up/down graphs are useful (Chapter 2) but insufficient. A pumping station may be in *remote automatic*, *local automatic*, *local manual*, *degraded* (one pump of two) or *out of service*; the reservoir may be *normal*, *low* or *below floor*. A **state model** for each critical function, with transitions caused by faults, attacks and operator actions, lets you ask: from normal operation, what sequence of events reaches an unacceptable state, and which control interrupts it?

PS4 is the obvious first candidate at LRWA, because it feeds the hospital directly.

### 22.4 The model as sensitive information

An accurate system model is a map for an adversary. Store it with access control, version it, and publish only abstractions. Treat exports to vendors and consultants under agreements. Keep a **model change log** linked to configuration management (Chapter 16) so that the model stays current; a model that is a year out of date is a liability presented as an asset.

LRWA's model, including the dependency graph and the zone allowlists, is held with access control and versioned with each configuration change.

### 22.5 Worked example: Hollin Hill functional model (synthetic)

Function F1 "supply St Brenna's" is satisfied if either path A (PS4 direct) or path B (Hollin Hill reservoir fed by PS3) is available, *and* the hospital's on-site tank bridges the gap during switchover. Path A needs PS4, its power (feeder F2 or generator) and its control (local automatic suffices). Path B needs the reservoir above floor and PS3 with power from feeder F1. Telemetry is not needed for supply — local automatic control keeps pumps running — but is needed for *visibility* (F3) and remote *intervention*. This insight changes priorities: the most important security property for F1 is that nobody can remotely command pumps into an unsafe state, while loss of telemetry is a visibility problem with a 72 h local-automatic buffer (R-local). Chapter 23's fault tree formalises exactly this AND/OR structure.

### 22.6 Practical activity

Extend Lab 2 so that each node has an AND or OR dependency type, and implement an availability function that evaluates whether `hospital_supply` works given a set of failed nodes. Test with the failures `{grid_f1}`, `{ps4}` and `{ps4, grid_f1}`.

Model the hospital supply as an OR of its two paths, with PS4's power as an OR of feeder F2 and the generator. Keep telemetry out of the supply function, as the worked example argues, but keep it in a separate visibility function so its loss still shows up. Then check your three results against EX043: the supply should survive losing feeder F1 or losing PS4, and fail only when both are lost.

### 22.7 Common errors and limits

- Inventory from one source only.
- Diagrams without trust boundaries or data direction.
- Up/down models where degraded modes decide outcomes.
- Models that are never updated, or that are shared freely.
- Treating telemetry loss and control misuse as the same consequence.

The Hollin Hill model shows the last error clearly: treating telemetry loss as loss of supply would send TMRP's budget to communications redundancy, when the property that actually protects the hospital is that pumps cannot be commanded remotely into an unsafe state.

### Exercises — chapter 22

**EX043 — AND/OR evaluation.** *Objective:* implement and use a mixed dependency model. *Inputs:* §22.6. *Steps:* implement, run the three tests, report results. *Expected evidence:* code and output. *Rubric:* 3 = correct semantics; `{grid_f1}` → supply survives via PS4 if PS4 runs in local automatic (no LTE needed); `{ps4}` → survives via reservoir; `{ps4, grid_f1}` → fails; 2 = telemetry wrongly required for supply; 1 = not run; 0 = none.

**EX044 — State model.** *Objective:* model degraded states. *Inputs:* PS4 modes in §22.3. *Steps:* draw a state model with at least five states and the events (fault, attack, operator action) between them; identify one path from *remote automatic* to *out of service* that a remote attacker could drive, and the control that breaks it. *Expected evidence:* state table and analysis. *Rubric:* 3 = coherent states and events, attack path realistic, control breaks it (e.g., trip reset requires local action); 2 = states only; 1 = up/down only; 0 = none.

### Chapter synthesis

Build the inventory from several reconciled sources, model the system in functional, physical and data-flow views with trust boundaries, represent degraded modes explicitly, and keep the model current and protected. Good models separate visibility from control and show which property actually protects the service.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Continue studying — chapter 22 of 50

[← Chapter 21](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 →](#ch-23)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Chapter 23 — Critical infrastructure and sector security: threat and failure analysis

### Learning outcomes and connection

After this chapter you can (1) perform threat modelling on data-flow diagrams with STRIDE and ATT&CK for ICS; (2) build fault trees and compute minimal cut sets and top-event probabilities; (3) combine failure and attack analysis — attack trees, bow-ties and consequence-driven scenarios; and (4) state the assumptions and limits of each method. It uses Chapters 7 and 22 and prepares Chapters 24, 27 and 33.

### 23.1 Threat modelling

Threat modelling asks, systematically, what can go wrong at each element and trust boundary of a system model. **STRIDE** — spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege — is a mnemonic for threat categories applied to each data flow, process and store. [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) catalogues adversary tactics and techniques observed against industrial systems, from initial access to impact (for example, manipulation of control or loss of view). Use STRIDE to generate candidate threats element by element and ATT&CK to check realism and completeness against observed behaviour.

### 23.2 Fault trees

A fault tree decomposes an undesired top event into combinations of basic events using AND and OR gates. A **minimal cut set** is a smallest set of basic events whose joint occurrence causes the top event; the list of minimal cut sets is the system's failure logic in its simplest form. Single-event cut sets are single points of failure. With independent basic-event probabilities, the top-event probability is computed exactly by enumeration for small trees, or approximately by summing cut-set probabilities (the **rare-event approximation**, an upper bound when probabilities are small).

### 23.3 Attack trees and bow-ties

An attack tree applies the same AND/OR structure to an adversary's goal; leaves are attacker actions with attributes such as cost, skill or detectability rather than probabilities. Assigning probabilities to deliberate attacks is questionable — adversaries adapt — so attack trees are often used to find the cheapest or least detectable path, then to place controls on it. A **bow-tie** joins causes (left), the central event, and consequences (right), showing preventive barriers before the event and mitigating barriers after it; it communicates well with operators and managers.

### 23.4 Combining failures and attacks

Infrastructure events mix accidental and deliberate causes: an attacker may wait for a storm, or a fault may mask an intrusion. Consequence-driven methods such as [INL's CCE](https://inl.gov/national-security/cce/) start from the unacceptable consequence and ask what combinations of failures and adversary actions reach it. A practical approach: build the fault tree for the consequence; mark which basic events an adversary could cause deliberately; recompute with those events set to "occurred" to see what remains as protection. Whatever remains is your real defence against a capable adversary.

### 23.5 Worked example: loss of hospital supply (synthetic)

Top event: St Brenna's loses supply for more than 4 h in a year. Following Chapter 22's model: path A (PS4) is lost if PS4 fails, or if feeder F2 *and* the PS4 generator both fail; path B is lost if the reservoir is unavailable, PS3 fails or feeder F1 fails; and the event requires both paths lost *and* the hospital tank failing to bridge (TANK). Lab 9 enumerates the tree with synthetic annual probabilities. There are six minimal cut sets, all of order three or four, because TANK appears in every one. The largest contributor is {G1, PS4, TANK}. The exact probability is 9.10 × 10⁻⁵ per year; the rare-event approximation gives 9.36 × 10⁻⁵.

Now the adversarial view: if an attacker can remotely stop PS3 and PS4 (no R1), both become "occurred" and the top event reduces to TANK alone — probability 0.03. Remote command authentication moves the system from a two-out-of-three-independent-failures problem to a single-point-of-failure problem. That comparison is the clearest argument for R1 in the whole dossier.

### 23.6 Practical activity: Lab 9

```python
# Lab 9 - fault tree: minimal cut sets and top-event probability (synthetic annual probabilities, offline)
from itertools import product
P = {"G1": 0.10, "G2": 0.08, "GEN": 0.05, "PS4": 0.02, "PS3": 0.02, "RES": 0.01, "TANK": 0.03}
# Top: hospital loses supply > 4 h = (feed A lost AND feed B lost)
# feed A (PS4 direct) lost = PS4 OR (G2 AND GEN);  feed B (reservoir) lost = RES OR PS3 OR G1
# hospital on-site tank TANK failing (empty/contaminated) is needed too: top = A AND B AND TANK
def top(s): A = s["PS4"] or (s["G2"] and s["GEN"]); B = s["RES"] or s["PS3"] or s["G1"]; return A and B and s["TANK"]
names = list(P); exact = 0.0; cuts = []
for bits in product([0, 1], repeat=len(names)):
    s = dict(zip(names, bits)); pr = 1.0
    for n in names: pr *= P[n] if s[n] else 1 - P[n]
    if top(s):
        exact += pr
        on = frozenset(n for n in names if s[n])
        cuts.append(on)
mcs = sorted({c for c in cuts if not any(o < c for o in cuts)}, key=lambda c: (len(c), sorted(c)))
for c in mcs:
    pr = 1.0
    for n in c: pr *= P[n]
    print(sorted(c), f"{pr:.2e}")
rare = sum(eval("*".join(str(P[n]) for n in c)) for c in mcs)
print(f"rare-event approx {rare:.3e}  exact {exact:.3e}")
```

Expected output:

```text
['G1', 'PS4', 'TANK'] 6.00e-05
['PS3', 'PS4', 'TANK'] 1.20e-05
['PS4', 'RES', 'TANK'] 6.00e-06
['G1', 'G2', 'GEN', 'TANK'] 1.20e-05
['G2', 'GEN', 'PS3', 'TANK'] 2.40e-06
['G2', 'GEN', 'RES', 'TANK'] 1.20e-06
rare-event approx 9.360e-05  exact 9.101e-05
```

The six cut sets each contain TANK, so the hospital's on-site storage appears in every route to the top event. The largest single contributor combines feeder F1, PS4 and the tank. The two probability figures differ slightly because the rare-event approximation counts overlapping cut sets twice, so it gives a small upper bound on the exact value. The adversarial reading in the worked example comes from setting PS3 and PS4 to certain failure and rerunning, which EX045 asks you to do yourself.

### 23.7 Common errors and limits

- Fault trees with dependent basic events treated as independent (common power, common software).
- Probabilities for deliberate attacks presented as frequencies.
- Threat models without trust boundaries.
- STRIDE lists never checked against observed adversary behaviour.
- Treating the rare-event approximation as exact when probabilities are large.

Lab 9 itself assumes independence, so a shared software flaw in both stations' RTUs would make its figures optimistic. Its probabilities for PS3 and PS4 failing are frequencies of random faults, so they say nothing about how likely an attacker is to stop both stations, which is why the adversarial case is handled by conditioning rather than by adding an attack probability.

### Exercises — chapter 23

**EX045 — Adversary-conditioned tree.** *Objective:* quantify what authentication buys. *Inputs:* Lab 9. *Steps:* (1) set PS3 and PS4 to probability 1 (attacker can stop them remotely) and compute the top-event probability; (2) instead, set G1 and G2 to 1 (attacker can cut both feeders) and recompute; (3) interpret both. *Expected evidence:* numbers and 150-word interpretation. *Rubric:* 3 = correct numbers (0.03; and with G1=G2=1, top = P(TANK)·P(PS4 or GEN) — compute), interpretation links to controls (R1; generator independence and tank); 2 = one number wrong; 1 = not run; 0 = none.

**EX046 — STRIDE on a flow.** *Objective:* threat-model one data flow. *Inputs:* the gateway-to-SCADA flow (Lab 8 frames over the LTE conduit). *Steps:* apply each STRIDE category, name an ATT&CK for ICS technique where one fits, and state the existing or proposed control. *Expected evidence:* six-row table. *Rubric:* 3 = all six categories meaningful and controls matched (e.g., spoofing → MAC; DoS → local automatic fallback); 2 = one category vacuous; 1 = list only; 0 = none.

### Chapter synthesis

Threat models generate what could go wrong at each trust boundary; ATT&CK keeps them realistic. Fault trees and minimal cut sets show failure logic and single points of failure; attack trees and bow-ties show adversary paths and barriers. Combine them by conditioning on what an adversary can cause: what remains is the defence that actually matters.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Continue studying — chapter 23 of 50

[← Chapter 22](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 →](#ch-24)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Chapter 24 — Critical infrastructure and sector security: methods I

### Learning outcomes and connection

After this chapter you can (1) select analysis methods appropriate to a design question — risk assessment, STPA, simulation, testbed experiment, tabletop exercise; (2) run a structured risk assessment and document it reproducibly; (3) plan a simulation study with explicit verification and validation; and (4) choose evidence proportionate to the decision. It builds on Chapters 15, 21 and 23 and prepares the design studio (Chapter 25).

### 24.1 Matching method to question

| Question | Method | Typical evidence |
|---|---|---|
| Which scenarios matter most? | Risk assessment (SP 800-30, IEC 62443-3-2) | Scenario table, rationale |
| Which control actions are unsafe? | STPA ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)) | Unsafe control actions, loss scenarios |
| How does the process respond? | Simulation (Labs 1, 7) | Model, V&V record, runs |
| Does the control work in practice? | Testbed experiment | Test plan, results, logs |
| Can people execute the plan? | Tabletop or functional exercise | After-action report |
| Is the design sound? | Independent review (Chapter 45) | Review findings and responses |

Engineering projects use several; a common mistake is using one method to answer another's question — for example, a tabletop exercise "showing" that a restoration time is achievable.

### 24.2 Structured risk assessment

A reproducible assessment documents: scope and assumptions; system model version; threat sources and their assumed capabilities; scenarios (threat event → vulnerability → consequence); existing controls; likelihood and consequence scales with definitions; ratings with rationale; and recommended controls. Scales must be defined in the organisation's terms (people-hours without water, not "high"). Ratings without rationale are opinions; with rationale, they can be challenged and improved.

TMRP's scales use people-hours without water at the hospital and other customers, so ratings mean the same thing to operators and managers.

### 24.3 Simulation with verification and validation

**Verification** asks whether the model is implemented correctly (does the code do what the model says?); **validation** asks whether the model represents reality well enough for its purpose. [Sargent (2013)](https://doi.org/10.1057/jos.2012.20) describes techniques: comparison with analytic results (Lab 1's Euler versus exact), extreme-condition tests, comparison with historical data, face validity with operators, and sensitivity analysis. State the model's intended use; a model valid for hold-up estimation may be invalid for transient pressure analysis.

For TMRP, the hold-up model is validated against a historical planned outage before it is used for the combined grid and telemetry scenario.

### 24.4 Exercises with people

Tabletop exercises walk a team through a scenario to test plans, roles and decisions; functional exercises perform some actions for real. Design them with objectives, injects, observers and an after-action report that records gaps without blame. They show whether people know what to do and where plans are ambiguous; they do not measure equipment performance.

TMRP's night functional exercise of local manual mode at PS3 and PS4 is the example: it uses real night staffing, records the time taken to establish manual operation, and reports the gaps it finds, but it cannot show whether the pumps or gateways meet their own requirements.

### 24.5 Worked example: choosing methods for TMRP (synthetic)

TMRP has four open questions: (1) which scenarios deserve funding — risk assessment with consequence scales in people-hours; (2) whether operators can switch PS3/PS4 to local manual within 1 h — a functional exercise at night with real staffing; (3) whether the gateway rejects forged and replayed frames — testbed tests T1–T2; (4) whether the reservoir lasts long enough during a combined grid and telemetry outage — Lab 1-style simulation validated against a historical planned outage. The plan names each method's evidence and its limit, so nobody later cites the tabletop as proof of R6.

### 24.6 Practical activity

Run a 45-minute tabletop with two classmates on the scenario "SCADA servers encrypted at 02:00", using the TMRP requirement set. Record decisions, times and gaps in an after-action report.

Assign roles before you start: the night operator, the duty manager and a facilitator who delivers injects. Use TMRP's requirements as the yardstick, especially local manual operation within one hour and restoration of remote operation within eight. Record each decision with its time and who made it. The after-action report should list what the plan did not cover, without naming anyone as the cause, and should state that a tabletop cannot show whether the eight-hour restoration is achievable.

### 24.7 Common errors and limits

- One method stretched to answer all questions.
- Undefined likelihood and consequence scales.
- Simulation presented without V&V or intended use.
- Exercise reports that blame individuals or record only successes.
- Evidence disproportionate to the decision (too little for safety-critical, too much for trivial).

TMRP's method plan guards against the first error by naming each method's limit, so a tabletop is never cited as proof that R6 is met. Its likelihood and consequence scales are defined in people-hours, and the hold-up simulation states its intended use.

### Exercises — chapter 24

**EX047 — Method match.** *Objective:* select methods. *Inputs:* four questions: (a) would forged setpoints at PS4 cause overpressure? (b) does the vendor's anomaly detector find Modbus write floods? (c) can the duty manager authorise local manual mode at night? (d) what is the annual risk ranking of eight scenarios? *Steps:* choose a method for each, its evidence and its main limit. *Expected evidence:* table. *Rubric:* 3 = (a) simulation/hydraulic analysis plus STPA, (b) testbed experiment, (c) exercise, (d) risk assessment, with honest limits; 2 = one mismatch; 1 = one method for all; 0 = none.

**EX048 — Validate a model.** *Objective:* plan V&V. *Inputs:* Lab 1 model. *Steps:* propose three verification checks and three validation checks, including one with historical data, and state the model's intended use and one use for which it is invalid. *Expected evidence:* list. *Rubric:* 3 = verification and validation distinct, historical comparison specified, invalid use identified (e.g., pressure transients, water quality); 2 = V and V mixed; 1 = vague; 0 = none.

### Chapter synthesis

Match each question to a method that can answer it and know each method's limit. Make risk assessments reproducible with defined scales and rationale; verify and validate simulations for a stated purpose; use exercises to test people and plans, not equipment; and scale the evidence to the decision it supports.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Continue studying — chapter 24 of 50

[← Chapter 23](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 →](#ch-25)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes and connection

After this chapter you can (1) run a structured design studio from brief to reviewed concept; (2) generate and compare concept alternatives against weighted criteria; (3) present a concept with its assumptions, risks and verification plan to a critical review panel; and (4) respond to review findings constructively. It integrates Chapters 16–24 into the first complete design artefact and prepares Chapter 26.

### 25.1 What a studio is

A design studio is an iterative, critiqued design exercise. Teams receive a brief, produce concepts, present them to reviewers who challenge assumptions, and revise. Its value is the critique: designs improve fastest when someone competent tries to break them early. In this course, each studio produces a **concept dossier**: problem statement, requirements excerpt, alternatives, evaluation, selected concept, risk register, verification plan and open questions.

For TMRP, Studio I's dossier covers remote operation of all six pumping stations and the Fenwick works.

### 25.2 The brief

**Studio I brief (synthetic):** LRWA must secure remote operation of PS1–PS6 and the Fenwick works. Constraints: budget 250 k (Lab 16); PS1 and PS2 have legacy RTU-A units that cannot be replaced for three years; private LTE is the only economical link; one control room, staffed 24/7 with one operator at night; the hospital needs ≤ 4 h interruption. Deliver: two to four concepts, evaluation, selection and verification plan.

The night staffing constraint is the one that most shapes the concepts, because any design that needs someone to drive to a station for every change leaves a single operator unable to keep up across six sites.

### 25.3 Generating alternatives

Generate concepts that differ in principle, not detail: (A) carrier-encrypted LTE with central firewalling only; (B) IPsec tunnels from new RTUs, gateways for legacy; (C) application-layer authentication with gateways and strong local autonomy; (D) no remote control at all — monitoring only, with operators dispatched for every change. Including an extreme (D) clarifies what remote control is worth.

The four concepts differ in where authentication happens and whether remote control exists at all. Concept D's very low operability score in the evaluation shows why an extreme is worth including.

### 25.4 Weighted evaluation

Define criteria from requirements and constraints, weight them before scoring, score each concept with evidence, and test whether the ranking survives plausible weight changes (sensitivity). A weighted sum is a structured conversation, not an oracle.

| Criterion (weight) | A | B | C | D |
|---|---:|---:|---:|---:|
| Prevents forged commands, R1 (0.30) | 1 | 4 | 4 | 5 |
| Service during network loss, R4 (0.20) | 2 | 3 | 5 | 5 |
| Operability with one night operator (0.20) | 5 | 4 | 4 | 1 |
| Cost within 250 k (0.15) | 5 | 2 | 4 | 4 |
| Legacy compatibility (0.15) | 5 | 3 | 4 | 5 |
| **Weighted score** | **3.20** | **3.35** | **4.20** | **4.05** |

D scores close to C because it is very secure, but its operability score reflects that one night operator cannot drive to six sites; it fails the hospital need in practice. The panel's challenge to the team is to show that C's lead survives if operability is weighted at 0.10 and R1 at 0.40 (EX049).

### 25.5 Presenting and responding to review

Present: the problem in one sentence, constraints, alternatives, evaluation, selection, risks, and what you have not verified. Reviewers will attack assumptions; record each finding, respond (accept, reject with reason, defer with owner) and revise. A defensive team learns nothing; a team that accepts every comment has no design.

The panel findings in EX050 are typical for TMRP: the gateway as a single point of failure, local manual mode bypassing authentication, and missing key-management staffing costs. Each needs a logged response with an owner. The second can be answered with evidence that already exists, because the key switch, alarm and local log were recorded when the conflict between R4 and R1 was resolved.

### 25.6 Practical activity

Produce the concept dossier for the Studio I brief in no more than eight pages and hold a 20-minute review with two peers acting as panel.

Keep to eight pages so the panel can read it before the review. Present the four concepts in the weighted table, show the sensitivity check and state what has not been verified. Ask the peers to attack one assumption each, such as the cost estimate or the night operability score. Record their findings in a response log with accept, reject or defer and an owner, as EX050 asks, and revise the concept before submitting the dossier.

### 25.7 Common errors and limits

- Alternatives that are variations of one idea.
- Weights chosen after scoring.
- Scores without evidence.
- No sensitivity check.
- Treating review as a test to pass rather than information.

Studio I guards against these: its four concepts differ in principle, its weights were fixed before scoring, and EX049 tests whether concept C's lead survives other weights. The panel's challenge to concept D, which scores well on security but fails night operability, is the kind of finding a review should produce. Every score cites evidence.

### Exercises — chapter 25

**EX049 — Weight sensitivity.** *Objective:* test the robustness of a selection. *Inputs:* the table in §25.4. *Steps:* recompute with weights (R1 0.40, network loss 0.20, operability 0.10, cost 0.15, legacy 0.15) and with (R1 0.20, network loss 0.20, operability 0.30, cost 0.15, legacy 0.15). *Expected evidence:* scores and conclusion. *Rubric:* 3 = correct arithmetic and an honest conclusion about when D overtakes C and what that implies; 2 = one arithmetic error; 1 = one scenario; 0 = none.

**EX050 — Review response log.** *Objective:* respond to critique. *Inputs:* three panel findings: "gateway is a single point of failure"; "local manual mode bypasses authentication"; "cost estimate ignores key management staffing". *Steps:* write a response log entry for each (accept/reject/defer, reason, change, owner). *Expected evidence:* log. *Rubric:* 3 = substantive responses with design changes where warranted (e.g., dual gateways or fail-to-local-automatic; key-switch and alarm; add operating cost line); 2 = one dismissive; 1 = accepts all without change; 0 = none.

### Chapter synthesis

A studio turns knowledge into a design under critique. Generate genuinely different alternatives, including extremes; weight criteria before scoring and test sensitivity; present assumptions and unverified claims openly; and treat review findings as design information with recorded responses.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Continue studying — chapter 25 of 50

[← Chapter 24](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 →](#ch-26)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Chapter 26 — Critical infrastructure and sector security: architecture alternatives

### Learning outcomes and connection

After this chapter you can (1) compare architectural patterns for critical systems — centralised versus distributed control, redundancy schemes, diversity, unidirectional flows, local autonomy; (2) analyse each pattern's failure and attack behaviour; (3) quantify trade-offs using availability, latency and cost models from earlier chapters; and (4) document architectural decisions with their consequences. It develops Studio I's selected concept and prepares Chapter 27.

### 26.1 Centralised and distributed control

Centralised control (one SCADA directing simple field devices) gives operators a single view and makes coordination easy, but concentrates both failure and attack. Distributed control (capable field controllers that run locally and accept supervisory targets) degrades gracefully when the centre or network is lost, at the cost of more devices to secure and configure. Most resilient designs are hierarchical: local control maintains safe operation autonomously; the centre optimises and coordinates.

TMRP's choice, the hierarchical C2, keeps local automatic control at every station.

### 26.2 Redundancy patterns

- **Hot standby:** a second unit running and ready to take over automatically (SCADA server pairs).
- **Cold standby:** a spare that must be started or installed (spare RTUs on a shelf).
- **N+1:** one more unit than needed (three pumps where two meet demand).
- **k-out-of-n voting:** used in safety systems (2-out-of-3 sensors) to tolerate one faulty or falsified input.

Each pattern must be judged against common causes (Chapter 7): two identical servers with identical software are redundant against hardware failure and not against malware.

### 26.3 Diversity

Diversity — different technologies, vendors, paths or teams — reduces common causes. It costs more and increases the skills needed, and can add attack surface. Use it where a common cause would be unacceptable: a second communication path via a different carrier and different power; a hard-wired safety trip independent of software; a manual gauge an operator can read when all electronics are suspect.

At LRWA, the case for diversity is clearest on the telemetry path, where a second carrier on separate power would remove the shared feeder F1 dependency, and at Hollin Hill, where a manual level gauge gives operators a reading they can trust when all electronics are suspect.

### 26.4 Unidirectional flows and local autonomy

Unidirectional gateways enforce outward-only data flow physically; they remove a whole class of inbound attacks on the protected side but also remove remote control through that path. Local autonomy — the ability of a site to run safely without the centre — is a resilience pattern that also limits attack consequence: a compromised centre can disrupt optimisation but should not be able to drive a site outside safe limits if those limits are enforced locally (R3).

TMRP's C3 option takes this to its limit for monitoring.

### 26.5 Worked example: three TMRP architectures compared (synthetic)

| Property | C1: Central + IPsec | C2: Hierarchical + app-layer auth (Studio I choice) | C3: Hierarchical + diode for monitoring, local-only control |
|---|---|---|---|
| Forged remote command | Requires tunnel key or SCADA compromise | Requires per-station key or SCADA compromise | Impossible remotely |
| Centre compromised | Can command any site within RTU limits | Can command any site within locally enforced bounds | Cannot command |
| Network loss | Sites hold last state | Sites run local automatic 72 h | Sites run local automatic |
| Operability | High | High | Low at night (dispatch needed) |
| Unavailability of comms, two carriers, β = 0.05 | 0.00136 | 0.00136 | n/a for control |
| Cost | Medium | Medium | Low capital, high staffing |

The table makes the residual risk of C2 explicit: a compromised SCADA centre can still issue authenticated commands within local bounds. That residual is accepted on the basis of monitoring, two-person approval for bulk setpoint changes, and local bounds that keep the process safe.

### 26.6 Practical activity

Write an ADR selecting between C2 and C3 for PS4 specifically (the hospital feed), considering that PS4's setpoints change rarely.

Start from the comparison table and from what makes PS4 special: it feeds St Brenna's directly and its setpoints change rarely. Weigh the security of removing remote setpoint writes against the cost of sending a technician for each change, especially at night with one operator on duty. State what would make you revisit the decision, such as more frequent setpoint changes. The defense in Chapter 50 later refers to an ADR with exactly this local-only option for PS4.

### 26.7 Common errors and limits

- Redundancy without diversity, claimed as resilience against attack.
- Diversity everywhere, overwhelming maintenance capability.
- Centralisation for convenience without local safe limits.
- Ignoring the operational cost of architectures that remove remote control.
- Architectural comparisons without numbers where numbers are available.

TMRP's table avoids the last error by putting numbers where they exist, such as communications unavailability with a common-cause factor, and by stating the staffing cost of C3 plainly. It also accepts C2's residual openly instead of claiming its redundancy protects against attack.

### Exercises — chapter 26

**EX051 — Voting against falsification.** *Objective:* analyse 2-out-of-3 voting. *Inputs:* three level transmitters at Hollin Hill; median selection. *Steps:* explain what one falsified transmitter can and cannot do; what an attacker controlling the common RTU that reads all three can do; and how to restore independence. *Expected evidence:* half page. *Rubric:* 3 = median tolerates one falsified input, common RTU defeats voting, independence via separate I/O or controller; 2 = common-RTU point missed; 1 = generic; 0 = none.

**EX052 — PS4 architecture decision.** *Objective:* write a decision record. *Inputs:* §26.6. *Steps:* write the ADR with context, options, decision, consequences and revisit conditions. *Expected evidence:* ADR. *Rubric:* 3 = decision justified by PS4's criticality and rare setpoint changes (C3 or C2 with local-only setpoint writes defended), consequences including operating cost, revisit triggers; 2 = weak consequences; 1 = no options; 0 = none.

### Chapter synthesis

Choose architecture by how it fails and how it can be attacked. Hierarchical control with local safe limits combines operability with graceful degradation. Redundancy protects against independent failures, diversity against common causes; unidirectional flows remove inbound attack paths along with remote control. Quantify where you can and document the residual risk you accept.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Continue studying — chapter 26 of 50

[← Chapter 25](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 →](#ch-27)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Chapter 27 — Critical infrastructure and sector security: control design

### Learning outcomes and connection

After this chapter you can (1) design controls that address specific scenarios with defined performance; (2) combine preventive, detective and recovery controls into defence in depth whose layers fail independently; (3) prefer engineered, physics-based limits for the worst consequences; and (4) specify each control so that it can be verified. It applies Chapters 15, 23 and 26 and prepares Chapters 28 and 30.

### 27.1 From scenario to control

Each scenario from Chapter 23 gets controls at three points: **prevent** the threat event, **detect** it if prevention fails, and **limit and recover** from consequences. Example — forged stop commands to PS3 and PS4: prevent with authenticated commands (R1); detect with alarms on command anomalies and unexpected state changes; limit with local automatic restart logic and the hospital tank; recover with local manual procedures (R4).

Each of these controls must then be specified and verified, as the rest of the chapter shows, before the forged-stop scenario can be called covered in the dossier.

### 27.2 Engineered limits first

For the worst consequences, the most robust controls do not depend on software at all: pressure relief valves, mechanical stops, hard-wired interlocks, chemical dosing pumps physically sized so they cannot overdose at maximum stroke. Cyber-informed engineering (see [INL CCE](https://inl.gov/national-security/cce/)) emphasises such controls because they hold even if every digital system is compromised. They cannot cover everything — a mechanical relief valve cannot stop a pump from being switched off — but they bound the worst cases.

For LRWA's dosing pump, the stroke limit sized by process engineers is such a control.

### 27.3 Independent layers

Defence in depth works only if layers fail independently. List each layer's dependencies: if authentication, monitoring and logging all depend on the SCADA servers, one compromise defeats all three. Place at least one detection layer outside the systems it watches (passive network monitoring, an independent analyser), and keep recovery materials (offline backups, procedures, spare keys) outside the reach of the threat being recovered from.

TMRP applies this by putting the chlorine analyser alarm on a separate logger and keeping offline backups away from the SCADA servers they would restore.

### 27.4 Specifying controls

A control specification states: the scenario(s) it addresses; its function; performance (detection within X, rejection rate, restoration time); dependencies; failure mode (fail-safe or fail-operational, and what that means here); owner; and verification method. Without performance and verification, a control is an intention.

The setpoint bounds specification in the worked example below shows every element: the scenario, the bounds and step limit, the alarm rule, the dependencies, retaining the last valid setpoint as its failure mode, and test T3 as verification. Its owner is the control engineering team that configures the dosing controller.

### 27.5 Worked example: setpoint bounds (synthetic)

Scenario: forged or erroneous setpoint drives the chlorine dosing pump to overdose. Controls: (1) **engineered** — dosing pump stroke physically limited so that maximum dose at maximum flow stays below a harmful concentration (sized by process engineers); (2) **preventive** — controller-side bounds and step limits (R3), implemented in the controller, not the HMI, so a compromised SCADA cannot bypass them; (3) **detective** — independent chlorine analyser alarm (R9) on a separate logger; (4) **recovery** — procedure to isolate the dosing line and flush. Specification for (2): reject setpoints outside 0.5–5.5 mg/L or changing by more than 0.5 mg/L per command, reject non-finite values, log every rejection, alarm on three rejections in 10 minutes; fail-safe = retain last valid setpoint; verified by test T3 including property-based testing (Lab 11).

### 27.6 Practical activity

Write full specifications for two controls of the forged-stop scenario in §27.1, including performance, dependencies, failure mode and verification.

Choose one preventive control, such as authenticated commands, and one recovery control, such as local manual operation at PS3 and PS4. For each, state the performance it must achieve, what it depends on and what happens when it fails. Authentication should fail closed for commands; local manual operation must work without SCADA or the network. Name an owner by role and a verification method, then check whether the two controls share any dependency that would let one event defeat both.

### 27.7 Common errors and limits

- Controls without performance criteria.
- Bounds enforced in the HMI rather than the controller.
- "Layers" that share dependencies.
- No engineered limit for the worst consequence when one is feasible.
- Recovery materials reachable by the same attacker.

The dosing example avoids each: bounds live in the controller, the analyser alarm uses a separate logger, the stroke limit is engineered, and every element has a performance target. The bounds also retain the last valid setpoint when a command is rejected, so the failure mode is stated, and each rejection is logged for the alarm rule.

### Exercises — chapter 27

**EX053 — Dependency audit of layers.** *Objective:* check independence. *Inputs:* the four controls in §27.5 and their implementation: controller bounds in the dosing PLC; analyser on separate logger; logging via SCADA. *Steps:* list dependencies of each layer; identify any shared dependency; propose a change. *Expected evidence:* table and change. *Rubric:* 3 = shared dependency found (rejection logging and alarm via SCADA), change proposed (local log plus independent alarm path); 2 = no change; 1 = list only; 0 = none.

**EX054 — Fail-safe meaning.** *Objective:* define failure modes in context. *Inputs:* authenticated telemetry gateway at PS4. *Steps:* for gateway failure, define what fail-safe means for (a) commands, (b) telemetry, (c) local control, and justify. *Expected evidence:* three definitions. *Rubric:* 3 = commands fail closed (rejected), telemetry fails visible (alarm at SCADA), local control continues automatically; 2 = one misdefined; 1 = "fail-safe = shut down"; 0 = none.

### Chapter synthesis

Design controls per scenario at prevention, detection and recovery points. Put engineered physical limits on the worst consequences, enforce bounds where the attacker cannot bypass them, make layers independent, and specify each control's performance, dependencies, failure mode, owner and verification.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Continue studying — chapter 27 of 50

[← Chapter 26](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 →](#ch-28)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Chapter 28 — Critical infrastructure and sector security: implementation I

### Learning outcomes and connection

After this chapter you can (1) implement a security control as working code with tests, from specification; (2) apply secure coding practices for input handling, cryptography and error handling; (3) build a test bench that exercises the control offline; and (4) record implementation evidence that links back to requirements. It implements Chapter 27's specifications and prepares Chapter 29.

### 28.1 From specification to code

Start from the control specification (Chapter 27): every "shall" becomes at least one test before or alongside the code. Keep the implementation small and dependency-free where possible — the gateway in this book uses only the Python standard library. Structure it as Chapter 9 recommends: a parser (Chapter 4), a verifier (Chapter 19), a state store (replay counters), and an output interface, each tested separately.

TMRP's gateway follows this structure, which is why its NaN bug could be found and fixed in the validator alone.

### 28.2 Secure coding for control paths

- Validate input before use: length, MAC, counter, shape, physical range (Labs 3 and 8).
- Compare secrets in constant time (`hmac.compare_digest`).
- Load keys from protected storage, never from source code or world-readable files.
- Treat every exception in the verification path as a rejection; never default to accept.
- Bound resource use: maximum message size, maximum queue length, rate limits per source.
- Log rejections with enough context to investigate, without logging secrets.

These rules come straight from Labs 3, 8 and 11. Each one has a test in the gateway suite.

### 28.3 The test bench

A test bench reproduces the control's environment offline: simulated RTUs that send valid, malformed, forged, replayed and delayed messages; a simulated SCADA that receives the gateway's output; and a clock you can control. Lab 15 (Chapter 40) is a compact version. Benches let you test failure modes that would be unsafe or impossible to provoke on a live system.

TMRP's bench includes simulated RTUs at PS2 and PS4, a simulated SCADA receiver and a controllable clock, so restarts, delays and replays can be produced on demand. The same harness later carries the seeded fault-injection campaign, which is why investing in it early saves time when the capstone verification begins.

### 28.4 Evidence

Record for each implementation: the requirement and specification versions implemented; the source revision; test results with tool versions; known limitations; and reviewer sign-off. This becomes part of the evidence dossier (Chapter 48).

For TMRP's setpoint validator, the record shows the specification version, the commits for v1 and v2, the T3 results for each, the known limitation that v1 accepted NaN, and the reviewer who asked the NaN question. Without that record, the later dossier finding about T3's status would have been impossible to resolve, because nobody could show which version had passed. Recording evidence while the work is done costs minutes; reconstructing it later costs days.

### 28.5 Worked example: setpoint validator v1 (synthetic)

The TMRP team implements R3 from the §27.5 specification. Version 1 checks `new < lo`, `new > hi` and the step limit, and passes the example tests: in-range accepted, above and below range rejected, too-large step rejected. Code review asks: what about NaN? In IEEE 754 arithmetic, every ordered comparison with NaN is false, so `nan < lo` and `nan > hi` are both false and `abs(nan - old) > max_step` is false — v1 accepts NaN. Version 2 rejects non-finite values explicitly and expresses the safe region positively (`lo <= new <= hi`), which is false for NaN. Chapter 30's property-based tests confirm the difference systematically (Lab 11). This is test T3's failure in Chapter 10's sign-off scenario.

### 28.6 Practical activity

Implement a minimal gateway that combines Lab 3's parser output with Lab 8's sealing, so that a validated Modbus reading becomes an authenticated frame. Write tests for each rejection path.

Keep the two parts separate behind clear interfaces: the parser returns a validated reading or a reason for rejection, and only a validated reading is sealed. Test each rejection path from Lab 3 and confirm that nothing reaches the sealing function. Then check that the sealed frame passes Lab 8's receiver and that a tampered copy is refused. Store the key outside the source file, even for this exercise, so the habit is in place before real keys appear.

### 28.7 Common errors and limits

- Code written before the specification is clear.
- Default-accept behaviour on exceptions.
- Negative checks (`if x > hi: reject`) that miss NaN; prefer positive checks of the safe region.
- Keys in source code.
- Evidence reconstructed after the fact.

The setpoint validator's first version shows the third error, and TMRP's dossier exists to prevent the last. Its NaN acceptance came from negative checks, and the fix was to state the safe region positively. Keys in TMRP's bench code are loaded from a protected file, never written in the source, and every exception in the verification path ends in a rejection that is logged.

### Exercises — chapter 28

**EX055 — NaN and friends.** *Objective:* find unsafe acceptances. *Inputs:* `validate_v1` in Lab 11. *Steps:* evaluate v1 and v2 by hand for `new` = NaN, +∞, −∞, 5.5 and 5.50001 with `old` = 5.2, and explain each result. *Expected evidence:* table. *Rubric:* 3 = v1 accepts NaN only among the specials (∞ rejected by `> hi`, −∞ by `< lo`), 5.5 accepted by both (boundary inclusive), 5.50001 rejected; v2 rejects all non-finite; explanations correct; 2 = one error; 1 = no explanations; 0 = none.

**EX056 — Rejection logging.** *Objective:* design useful logs. *Inputs:* the gateway. *Steps:* define a log record for each rejection type (tag, replay, stale, shape, range) with fields, and explain one field you deliberately exclude. *Expected evidence:* schema. *Rubric:* 3 = fields allow investigation (time source, station, counter, reason, gateway ID, message hash), excludes key material and full payload where sensitive; 2 = missing time source or station; 1 = free text; 0 = none.

### Chapter synthesis

Implement controls from specifications with tests for every "shall". Code the control path defensively: validate fully, compare in constant time, protect keys, reject on any error, bound resources, log usefully. Prefer positive checks of the safe region. Test on a bench that can produce the failures you cannot provoke live, and record evidence as you go.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Continue studying — chapter 28 of 50

[← Chapter 27](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 →](#ch-29)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Chapter 29 — Critical infrastructure and sector security: measurement

### Learning outcomes and connection

After this chapter you can (1) define security and resilience metrics that support decisions; (2) compute detection metrics — precision, recall, F1, false-alarm rate, time to detect — from labelled tests; (3) measure resilience as service performance over time through a disruption; and (4) avoid metrics that reward the wrong behaviour. It builds on Chapters 7 and 28 and prepares Chapters 30, 38 and 40.

### 29.1 What to measure

A metric is useful if it changes a decision. Three families: **control performance** (does the control do what was specified: rejection rates, detection times); **exposure** (how much attack surface or vulnerability exists: unauthenticated conduits, unpatched reachable vulnerabilities, shared accounts); and **service resilience** (how service degrades and recovers). Use the goal–question–metric approach: state the goal, the question that would show progress, and only then the metric.

For TMRP, the alarm latency for R7 measures control performance, the count of unauthenticated conduits measures exposure, and the share of demand met during the recovery trial measures resilience.

### 29.2 Detection metrics

From a labelled test set: true positives (TP), false positives (FP), false negatives (FN), true negatives (TN). **Precision** = TP/(TP+FP): of alarms, how many were real. **Recall** = TP/(TP+FN): of real events, how many were found. **F1** is their harmonic mean. Report both precision and recall with the base rate of the test set; precision in a test set with 50% attacks says little about operations with 0.1% (Chapter 7). **Time to detect** is a distribution; report median and worst cases, not only the mean. [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) list common pitfalls in evaluating machine-learning security systems, including unrealistic base rates and data snooping; [Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) show how point-adjusted evaluation can inflate time-series anomaly detection scores.

### 29.3 Resilience as performance over time

Plot service performance $Q(t)$ — for LRWA, the fraction of demand met — through a disruption. [Bruneau et al. (2003)](https://doi.org/10.1193/1.1623497) proposed measuring resilience loss as the area between full performance and $Q(t)$ from disruption to recovery. The curve shows robustness (how far performance falls), rapidity (how fast it recovers) and the total loss. Engineering requirements map onto it: R4 keeps the drop shallow; R6 shortens the recovery.

TMRP's recovery trial gives a real curve, since supply stayed in local mode while remote operation was restored.

### 29.4 Metrics that mislead

Counting blocked attacks rewards noisy firewalls; counting patches applied ignores which ones mattered; mean time to detect hides the one event detected after three weeks. When a metric becomes a target, people optimise the metric. Prefer metrics tied to consequences and verified by test.

TMRP's detector acceptance test avoids these by reporting misses and the slowest detection, not just an average. The two missed reconnaissance events stay in the report, because they are the result that changes how much LRWA can rely on the detector.

### 29.5 Worked example: anomaly detector acceptance test (synthetic)

TMRP's acceptance test of a network anomaly detector uses 14 labelled events from a test week on the bench (Lab 10): 7 malicious (write floods, unauthorised function codes, a new engineering connection) and 7 benign (maintenance, firmware backup, a failover). Results: precision 0.625, recall 0.714, F1 0.667; time to detect for detected events 2–30 minutes, median 7. The two missed attacks were both slow, low-volume reconnaissance. The acceptance decision: deploy for high-volume attack detection, do not rely on it for reconnaissance, and record that the 50% base rate of the test set makes operational precision much lower.

### 29.6 Practical activity: Lab 10

```python
# Lab 10 - detection metrics and time-to-detect from a labelled synthetic test week (offline)
# (event_id, truly_malicious, alerted, minutes_from_start_to_alert or None)
EV = [(1,1,1,4),(2,1,1,11),(3,1,0,None),(4,0,1,None),(5,0,0,None),(6,1,1,2),(7,0,1,None),
      (8,0,0,None),(9,1,1,30),(10,0,0,None),(11,0,0,None),(12,1,0,None),(13,0,1,None),(14,1,1,7)]
tp = sum(1 for e in EV if e[1] and e[2]); fp = sum(1 for e in EV if not e[1] and e[2])
fn = sum(1 for e in EV if e[1] and not e[2]); tn = sum(1 for e in EV if not e[1] and not e[2])
prec, rec = tp / (tp + fp), tp / (tp + fn)
print(f"TP={tp} FP={fp} FN={fn} TN={tn} precision={prec:.3f} recall={rec:.3f} F1={2*prec*rec/(prec+rec):.3f}")
ttd = sorted(e[3] for e in EV if e[1] and e[2])
print("time to detect (min):", ttd, "mean", round(sum(ttd)/len(ttd), 1), "median", ttd[len(ttd)//2])
```

Expected output:

```text
TP=5 FP=3 FN=2 TN=4 precision=0.625 recall=0.714 F1=0.667
time to detect (min): [2, 4, 7, 11, 30] mean 10.8 median 7
```

The counts match the worked example: five attacks detected, three benign events alarmed, two attacks missed and four benign events left quiet. The two missed attacks were slow, low-volume reconnaissance, which the detector does not see. The detection times show why a median matters: one event took thirty minutes while most were found in under ten. Because half the test events were malicious, the precision here is far higher than LRWA would see in operation, as EX057 shows.

### 29.7 Common errors and limits

- Metrics nobody uses for a decision.
- Precision reported from balanced test sets as if operational.
- Mean time to detect without distribution or misses.
- Resilience reported as uptime only.
- Metrics that become targets.

TMRP's acceptance test reports misses and the slowest detection, and its precision is stated with the test set's fifty per cent base rate, so nobody mistakes it for operational precision. Resilience is shown as the share of demand met over time, not as uptime. Every metric in it informs the deployment decision.

### Exercises — chapter 29

**EX057 — Operational precision.** *Objective:* translate test metrics to operations. *Inputs:* Lab 10 recall 0.714 and the test FP rate 3/7; operational base rate 1 malicious event per 1,000 events. *Steps:* compute the operational precision and expected false alarms per 1,000 events; interpret. *Expected evidence:* numbers and interpretation. *Rubric:* 3 = correct calculation (precision ≈ 0.0017; ≈ 428 false alarms per 1,000 events), interpretation that the FP estimate from 7 benign events is far too uncertain and the detector unusable without much lower FPR; 2 = numbers right; 1 = wrong formula; 0 = none.

**EX058 — Resilience curve.** *Objective:* compute resilience loss. *Inputs:* synthetic $Q(t)$: 100% until t = 0; 60% from 0 to 4 h; linear recovery to 100% from 4 h to 12 h. *Steps:* compute the loss area in %·h; recompute if local manual mode (R4) keeps $Q$ at 85% from 0 to 4 h. *Expected evidence:* two numbers and a sentence. *Rubric:* 3 = 160+160 = 320 %·h and 60+60 = 120 %·h with clear interpretation; 2 = one error; 1 = method only; 0 = none.

### Chapter synthesis

Measure what changes decisions: control performance, exposure and service resilience. Report precision and recall with base rates and time-to-detect distributions including misses. Represent resilience as performance over time. Distrust metrics that can be gamed or that hide the worst case.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Continue studying — chapter 29 of 50

[← Chapter 28](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 →](#ch-30)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes and connection

After this chapter you can (1) plan and run a verification campaign for security controls with defined pass/fail criteria; (2) use example-based, boundary, negative and property-based testing; (3) record results so another engineer can reproduce them; and (4) handle failed tests honestly, including re-test after fixes. It verifies Chapter 28's implementation and prepares Chapter 38 (validation) and Chapter 40 (Verification laboratory II).

### 30.1 Verification as a campaign

Verification answers: does the implementation meet its specification? A campaign plan lists, for each requirement, the test cases, environment, inputs, procedure, expected result, pass criterion and who runs it. Tests are written before execution and are not changed to make results pass. Results include environment details (software versions, seeds, configuration) so the test can be repeated.

TMRP's campaign plan lists T1 to T7 against R1 to R8, with pass criteria fixed before any test runs; R9 has no test assigned yet, which the evidence map later exposes. Each test names its environment and who runs it.

### 30.2 Kinds of test

- **Example tests** check typical behaviour.
- **Boundary tests** check edges: exactly at limits, just inside, just outside.
- **Negative tests** check that invalid input is rejected: malformed, forged, replayed, out of range.
- **Property-based tests** state a property that must hold for all inputs ("no unsafe setpoint is ever accepted") and check it on many generated inputs, including special values. They find cases no one thought to write.
- **Fault-injection tests** (Chapter 40) perturb the environment: drop, delay or corrupt messages; restart components.

Example tests show the presence of correct behaviour in chosen cases; property-based and fault-injection tests search for the absence of incorrect behaviour more broadly. None proves correctness for all inputs except in small finite domains (Chapter 2).

### 30.3 Reproducibility

Seed every random generator and print the seed; record tool and library versions; keep the test inputs; store results with the source revision. A failed test that cannot be reproduced cannot be fixed or re-verified.

TMRP's T3 record follows this rule: it gives the seed, the number of generated cases and the Python version, so anyone can rerun the property-based test and see the same thirty-one NaN acceptances on v1 and none on v2. Without the seed, a reviewer could only take the result on trust. The same record stores the source revision of each validator version.

### 30.4 Failed tests

A failed test is information. Record it as failed with evidence; analyse root cause; fix; re-run the failed test and the regression suite; record the re-test. Never re-label a failure as "not applicable" because the deadline is close (Chapter 10). If a failure is accepted temporarily, it needs a compensating control, an owner and a date.

T3 is the model: failed on v1, fixed in v2, re-tested and recorded. The v1 failure was never relabelled, and the PS4 compensating control had an owner and a date.

### 30.5 Worked example: T3 setpoint bounds (synthetic)

Test T3 verifies R3. Example tests on v1 (in range, above, below, large step) pass. The property-based test generates 2,000 cases with seed 30, one in ten drawn from special values (NaN, ±∞, exact boundaries). v1 accepts 31 unsafe values — all NaN. v2 accepts none. T3 is recorded as **failed on v1**, root cause "negative comparisons are false for NaN", fixed in v2, re-tested and **passed on v2**, with the seed and Python version recorded.

Both results stay in the record. The re-test result is later entered in the traceability matrix.

### 30.6 Practical activity: Lab 11

```python
# Lab 11 - property-based testing of a setpoint validator finds what example tests missed (offline)
import random, math
def validate_v1(new, old, lo=0.5, hi=5.5, max_step=0.5):
    if new < lo: return False
    if new > hi: return False
    if abs(new - old) > max_step: return False
    return True
def validate_v2(new, old, lo=0.5, hi=5.5, max_step=0.5):
    if not (isinstance(new, float) and math.isfinite(new)): return False
    return lo <= new <= hi and abs(new - old) <= max_step
examples = [(3.0, 3.2), (6.0, 5.8), (0.2, 0.6), (4.0, 3.0)]
print("example tests v1:", [validate_v1(n, o) for n, o in examples])
rng = random.Random(30)
specials = [float("nan"), float("inf"), -float("inf"), 5.5, 0.5]
def prop(f, trials=2000):
    fails = []
    for i in range(trials):
        old = rng.uniform(0.5, 5.5)
        new = rng.choice(specials) if i % 10 == 0 else rng.uniform(-1, 7)
        ok = f(new, old)
        safe = math.isfinite(new) and 0.5 <= new <= 5.5 and abs(new - old) <= 0.5
        if ok and not safe: fails.append(new)
    return fails
f1 = prop(validate_v1); f2 = prop(validate_v2)
print("v1 unsafe acceptances:", len(f1), "first:", f1[:1])
print("v2 unsafe acceptances:", len(f2))
```

Expected output:

```text
example tests v1: [True, False, False, False]
v1 unsafe acceptances: 31 first: [nan]
v2 unsafe acceptances: 0
```

The example tests give the same answers for both validators, so they cannot tell v1 from v2. The property-based run is what separates them: v1 accepts thirty-one unsafe values, all NaN, while v2 accepts none. The seed of thirty makes the run repeatable. Notice that the generator draws special values only one time in ten; without that, NaN would almost never appear and the bug would stay hidden however many random cases were tried. Record the seed with the result.

### 30.7 Common errors and limits

- Tests written after seeing results.
- Example tests only.
- Unseeded random tests; results without versions.
- Failures re-labelled instead of fixed.
- Claiming property-based tests prove correctness.

TMRP's T3 record avoids each of these. Its property was written before the run, its generator is seeded, the failure on v1 stayed recorded as failed, and the report claims only that no unsafe value was found among the generated cases, not that v2 is correct for every input. The seed and version are stored with the result.

### Exercises — chapter 30

**EX059 — Count the failures.** *Objective:* reason about generated tests. *Inputs:* Lab 11. *Steps:* (1) explain why all 31 unsafe acceptances are NaN; (2) estimate how many NaN cases the generator produced (one in ten cases are special values, chosen uniformly from five) and compare with 31; (3) explain why not every NaN case is an unsafe acceptance in v1 — or show that every NaN is accepted. *Expected evidence:* reasoning and numbers. *Rubric:* 3 = ≈ 200 special cases × 1/5 ≈ 40 expected NaN, 31 observed consistent with random variation, and every NaN is accepted by v1 so 31 is the NaN count; 2 = partial; 1 = no numbers; 0 = none.

**EX060 — Verification plan for R2.** *Objective:* plan tests for replay rejection. *Inputs:* R2 and Lab 8. *Steps:* write a test plan with at least six cases (including restart of each side, counter wrap or maximum, out-of-order delivery), expected results and pass criteria. *Expected evidence:* table. *Rubric:* 3 = cases cover restart and ordering, expected results consistent with the design in §19.5, criteria unambiguous; 2 = restart missed; 1 = happy path only; 0 = none.

### Chapter synthesis

Verification is a planned campaign with criteria fixed in advance. Combine example, boundary, negative, property-based and fault-injection tests; make every run reproducible; and treat failures as information to be fixed and re-verified, never relabelled.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Continue studying — chapter 30 of 50

[← Chapter 29](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 →](#ch-31)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-31"></a>

## Chapter 31 — Critical infrastructure and sector security: implementation II

### Learning outcomes and connection

After this chapter you can (1) deploy controls into operational environments through staged rollout with rollback; (2) manage keys, configuration and secrets in production; (3) integrate legacy equipment through gateways and compensating controls; and (4) commission a control with acceptance tests and operator handover. It moves Chapter 28's bench implementation into the field and prepares Chapters 32–34.

### 31.1 Staged deployment

Field deployment follows stages, each with entry and exit criteria: bench (all tests pass); pilot site with low consequence; one high-consequence site with extra monitoring and a rollback plan; fleet. Each stage has a **rollback** — the ability to return to the previous known-good state quickly — tested before it is needed. Schedule changes outside peak demand and with operators informed; in water, avoid changes during high-demand periods or when storage is low.

TMRP's stages are bench, PS2 as the low-consequence pilot, PS4 as the first high-consequence site, then the fleet.

### 31.2 Production key and secret management

On the bench, keys are files; in production they are lifecycles. Generate keys in hardware security modules or device secure elements; enrol devices with an auditable ceremony (two people, logged); store the inventory of which key belongs to which device and its rotation date; rotate; and revoke promptly when a device is lost or decommissioned. Secrets for service accounts go into a vault with access logging, not into scripts. A key inventory is itself sensitive.

For TMRP, keys are generated in the gateway's secure element at enrolment.

### 31.3 Legacy integration

Legacy devices that cannot authenticate are wrapped: a gateway placed physically adjacent (same cabinet) adds authentication on the network side and speaks the legacy protocol on a short, physically protected link. The gateway becomes part of the device's security boundary, so it needs its own hardening, monitoring and update path. Compensating controls cover what the gateway cannot: cabinet tamper alarms, local logging, and restrictions on which function codes pass through.

At PS2, the gateway sits in the RTU cabinet on a 30 cm serial link and passes only two function codes.

### 31.4 Commissioning and handover

Commissioning verifies the installed system in its real environment: site acceptance tests repeat key bench tests on site (authentication rejects forged frames; replay rejected; failover to local automatic works; alarms reach the control room within 60 s). Handover gives operators procedures, training, contacts and the known limitations. Until operators can run and recover the system, the control is not in service.

At PS2, site acceptance also found the gateway's clock drift, which was fixed and re-tested before handover. Operators were trained first.

### 31.5 Worked example: PS2 pilot (synthetic)

TMRP's pilot site is PS2 — legacy RTU-A, low consequence. Entry criteria: T1, T2, T3 (v2), T5 passed on the bench; rollback image ready; operators briefed. The gateway is installed in the RTU cabinet; the serial link is 30 cm inside the locked cabinet; the gateway passes only function codes 3 (read) and 6 (write single register) for the configured register range. Site acceptance: forged and replayed frames rejected and alarmed; pulling the LTE antenna results in local automatic operation and a communication-loss alarm within 60 s; restoring the antenna resumes telemetry with counters continuing. One finding: the gateway clock drifted 40 s in 48 h because NTP was not reachable through the new conduit; fixed by adding an internal time source to the conduit allowlist. Exit criteria met after re-test; PS4 is next.

### 31.6 Practical activity

Write the stage plan for TMRP fleet rollout with entry/exit criteria and rollback for each stage, and a two-page operator handover note for the gateway.

Use the PS2 pilot as your model for entry and exit criteria, then extend the plan to PS4 and the remaining stations. For each stage, say how rollback is done and who decides to use it. In the handover note, give operators the alarms the gateway raises, what each means, how to switch to local manual operation and whom to call. List the known limitations plainly, such as the dependence on an internal time source learned at PS2.

### 31.7 Common errors and limits

- "Big bang" deployment without pilot or rollback.
- Rollback plans never tested.
- Key enrolment by one person without records.
- Gateways treated as transparent rather than as security-critical devices.
- Commissioning without operators; handover without known limitations.

TMRP's PS2 pilot avoided these: it had a rollback image, operators were briefed before installation, and the clock-drift finding was handled as an interface fix and re-tested before PS4 began. Key enrolment follows the two-person, logged ceremony described above, and the gateway was treated as a security-critical device with its own hardening and update path.

### Exercises — chapter 31

**EX061 — Rollback criteria.** *Objective:* define when to roll back. *Inputs:* PS4 deployment. *Steps:* define three measurable rollback triggers, who decides, and the maximum time to complete rollback. *Expected evidence:* list. *Rubric:* 3 = triggers measurable (e.g., telemetry loss > 5 min not explained by link loss, any accepted message failing audit, alarm latency > 60 s for priority alarms), decision owner named by role, rollback time consistent with hospital buffer; 2 = vague triggers; 1 = no owner; 0 = none.

**EX062 — Gateway as boundary.** *Objective:* secure a legacy wrapper. *Inputs:* the PS2 gateway. *Steps:* list six controls that the gateway itself needs, and the residual risk if an attacker gains physical access to the cabinet. *Expected evidence:* list and residual statement. *Rubric:* 3 = hardening, signed updates, key protection, function-code filtering, tamper detection, logging; honest residual (physical attacker can bypass via serial link); 2 = residual missing; 1 = generic; 0 = none.

### Chapter synthesis

Deploy in stages with entry and exit criteria and tested rollback. Manage keys and secrets as lifecycles with auditable ceremonies. Wrap legacy devices with gateways that are themselves treated as security-critical, plus compensating physical controls. A control is in service only after site acceptance and operator handover.

<!-- cyberabc:chapter-navigation:start ch-31 -->
### Continue studying — chapter 31 of 50

[← Chapter 30](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 →](#ch-32)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-32"></a>

## Chapter 32 — Critical infrastructure and sector security: reliability

### Learning outcomes and connection

After this chapter you can (1) use reliability measures — failure rate, MTBF, MTTR, availability; (2) compute availability of series, parallel and repairable redundant systems with Markov models; (3) show how repair capacity and common causes change redundancy benefits; and (4) connect reliability engineering to security, where failures may be induced. It builds on Chapter 7 and prepares Chapters 33 and 41.

### 32.1 Measures

For a component with constant failure rate $\lambda$ (failures per hour), mean time between failures is $1/\lambda$. With mean time to repair $1/\mu$, steady-state availability is $A = \mu/(\lambda+\mu) = \text{MTBF}/(\text{MTBF}+\text{MTTR})$. Constant failure rates suit the useful-life period of electronics; early-life and wear-out failures need other distributions (Weibull). Components in **series** (all needed) have rates that add: $\lambda_s = \sum\lambda_i$. Components in **parallel** (any one suffices) fail only together.

At PS4, each pump's failure rate of one per two thousand hours and its 24-hour repair time give the single-pump availability used in Lab 12.

### 32.2 Repairable redundancy

Simple formulas for parallel systems assume independent units each repaired independently. Real sites often have one repair crew, so when both units are down one waits. A continuous-time Markov chain models this: states 0, 1, 2 units failed; transitions at rate $2\lambda$ from 0 to 1, $\lambda$ from 1 to 2, and $\mu$ back down from 1 and from 2 with one crew. Solving the balance equations gives steady-state probabilities; unavailability is the probability of state 2.

PS4 has exactly this constraint: two pumps, one repair crew. The Markov model in Lab 12 captures the wait.

### 32.3 Induced failures

Reliability models assume failures arrive randomly. An adversary chooses when. If an attacker can disable one pump remotely and wait for the other to fail — or disable both — the Markov numbers no longer describe the risk. Reliability engineering still matters for security: it tells you the **baseline** the attacker must overcome, the **repair capacity** that determines recovery speed, and the spare holdings that make cold standby real. Security requirements then aim to make induced failures require independent compromises (Chapter 23's conditioning).

### 32.4 Worked example: PS4 duty/standby pumps (synthetic)

Each PS4 pump has a failure rate of 1 per 2,000 h and mean repair time of 24 h with one crew. Lab 12 gives single-pump availability 0.98814 (about 104 h down a year). The 1-out-of-2 pair with one crew has availability 0.999719 — both pumps down about 148 minutes a year. The naive formula $1-(1-A)^2$ gives 0.999859, half the real unavailability, because it ignores that the second failure can occur while the single crew is busy. For the pump set's control chain — pump, starter and RTU in series with MTBFs of 2,000, 5,000 and 10,000 h — the series MTBF is 1,250 h: the chain is less reliable than its weakest element.

### 32.5 Practical activity: Lab 12

```python
# Lab 12 - availability of a duplicated pump set with repair (two-state units, one repair crew; offline)
lam, mu = 1 / 2000, 1 / 24     # failures per hour per pump, repairs per hour
A1 = mu / (lam + mu)
# states: 0 = both up, 1 = one down, 2 = both down; one crew repairs one pump at a time
# balance: p1 = (2 lam / mu) p0 ; p2 = (lam / mu) p1
p0 = 1 / (1 + 2 * lam / mu + 2 * (lam / mu) ** 2)
p1 = 2 * lam / mu * p0; p2 = lam / mu * p1
print(f"single pump availability {A1:.6f}  downtime h/yr {8760*(1-A1):.1f}")
print(f"1oo2 availability {1-p2:.8f}  P(both down) {p2:.2e}  downtime min/yr {8760*60*p2:.2f}")
print(f"naive independent 1-(1-A1)^2 = {1-(1-A1)**2:.8f}")
mtbf_series = 1 / (1/2000 + 1/5000 + 1/10000)
print(f"series MTBF pump+starter+RTU: {mtbf_series:.0f} h")
```

Expected output:

```text
single pump availability 0.988142  downtime h/yr 103.9
1oo2 availability 0.99971883  P(both down) 2.81e-04  downtime min/yr 147.78
naive independent 1-(1-A1)^2 = 0.99985939
series MTBF pump+starter+RTU: 1250 h
```

The single pump is down about 104 hours a year. The pair with one crew is down together for about 148 minutes a year, roughly twice what the naive formula suggests, because the second failure can arrive while the crew is still repairing the first. The series figure shows the control chain's weakness: pump, starter and RTU together have a mean time between failures of 1,250 hours, shorter than any one of them alone. Repair capacity, not pump quality, drives the difference.

### 32.6 Common errors and limits

- Independent-repair formulas with one crew.
- Constant failure rates for ageing equipment.
- Ignoring common causes (shared starter panel, shared power).
- Reliability numbers presented as protection against deliberate attack.
- Vendor MTBF figures used without knowing their test conditions.

For PS4 the first error halves the predicted downtime, and the third ignores that both pumps share one starter panel and one feeder. Vendor MTBF figures for the RTU should be checked against LRWA's own maintenance records before they enter the dossier, and none of these numbers says anything about an attacker who stops both pumps deliberately.

### Exercises — chapter 32

**EX063 — Two crews.** *Objective:* model repair capacity. *Inputs:* Lab 12. *Steps:* modify the Markov model for two independent crews (repair rate $2\mu$ from state 2) and compute unavailability; compare with one crew and with the naive formula. *Expected evidence:* numbers and conclusion. *Rubric:* 3 = two-crew result matches the naive independent formula (explain why), one-crew roughly double; 2 = numbers right, no explanation; 1 = not run; 0 = none.

**EX064 — Spares decision.** *Objective:* connect reliability to logistics. *Inputs:* repair time 24 h assumes a spare pump in stock; without a spare, repair takes 21 days (504 h). *Steps:* compute 1oo2 unavailability with one crew and MTTR 504 h, and recommend whether to hold a spare. *Expected evidence:* number and recommendation. *Rubric:* 3 = correct computation (use the lab formula with μ = 1/504), recommendation tied to hospital consequence; 2 = number right; 1 = wrong rate; 0 = none.

### Chapter synthesis

Reliability is measured with failure rates, repair times and availability; series chains are weaker than their weakest link; repairable redundancy depends on repair capacity, which simple formulas ignore. Adversaries induce failures on their schedule, so reliability gives the baseline and recovery capacity, while security must make induced failures require independent compromises.

<!-- cyberabc:chapter-navigation:start ch-32 -->
### Continue studying — chapter 32 of 50

[← Chapter 31](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 →](#ch-33)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-33"></a>

## Chapter 33 — Critical infrastructure and sector security: safety and resilience

### Learning outcomes and connection

After this chapter you can (1) apply System-Theoretic Process Analysis (STPA) to a control structure, including security-related causes; (2) describe safety instrumented systems and why they need independence; (3) define and engineer resilience — anticipate, withstand, recover, adapt; and (4) integrate safety, security and resilience in one analysis. It builds on Chapters 10, 17, 23 and 32 and prepares Chapters 34 and 47.

### 33.1 STPA

[Leveson (2004)](https://doi.org/10.1016/S0925-7535(03)00047-X) proposed STAMP, an accident model that treats safety as a control problem: accidents arise when constraints on system behaviour are not enforced. STPA, the analysis method built on it, proceeds: (1) define losses and hazards; (2) model the control structure — controllers, control actions, feedback; (3) identify **unsafe control actions** (UCAs) in four types: not provided when needed, provided when unsafe, provided too early/late or in the wrong order, stopped too soon or applied too long; (4) identify loss scenarios — why each UCA could occur, including flawed feedback, flawed process models and, for security (STPA-Sec), adversary action. STPA's strength is that it finds hazards from interactions where no component has failed — exactly the situation of a false-data attack.

### 33.2 Safety instrumented systems and independence

A safety instrumented system (SIS) takes a process to a safe state when a hazardous condition is detected, independent of the basic process control system. Functional safety standards (IEC 61508 and sector derivatives) assign safety integrity levels. Independence means separate sensors, logic and final elements, and in modern terms separate networks and engineering access, because a compromised engineering workstation that can reprogram both control and safety logic removes the independence. TRITON targeted SIS controllers directly ([CISA HatMan report](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)).

### 33.3 Resilience

[NIST SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1) frames cyber resiliency around the goals to anticipate, withstand, recover and adapt, with techniques such as diversity, segmentation, redundancy, non-persistence and adaptive response. [Haimes (2009)](https://doi.org/10.1111/j.1539-6924.2009.01216.x) argues that resilience must be defined relative to specific threats and system states. Engineering resilience means: design degraded modes (Chapter 22), keep capacity and buffers (storage, batteries, spares), make recovery fast and practised (Chapter 47), and learn after events.

For LRWA, the hospital tank, cabinet batteries and 72 hours of local automatic operation are buffers; the recovery trial is practice.

### 33.4 Worked example: STPA on Hollin Hill level control (synthetic)

Loss L1: hospital without water; L2: reservoir overflow and flooding. Hazards: H1 level below floor while demand continues; H2 level above overflow. Control structure: SCADA operator → PI controller (PS3 pump speed) → pump → reservoir; feedback via level transmitter. UCAs: UCA1 "controller reduces inflow when level is low" (provided when unsafe → H1); UCA2 "operator does not intervene when level falls" (not provided → H1); UCA3 "controller increases inflow when level is high" (→ H2). Scenario for UCA1: the controller's process model believes the level is high because the level feedback is falsified (Lab 7). Scenario for UCA2: operator's display shows the same falsified level. Constraints: independent level measurement with alarm (EX034); hard-wired high-level pump trip for H2; low-level alarm to operator from the independent measurement. STPA arrived at the same control as the residual detector, but from the hazard rather than from the attack.

### 33.5 Practical activity

Extend §33.4 with the dosing loop: losses, hazards, control structure, at least four UCAs (one of each type) and one loss scenario each, one of them adversarial.

Start with losses such as harm to consumers from overdosing or underdosing, and hazards such as residual chlorine outside its limits. Draw the control structure: the operator, the dosing controller, the dosing pump and the analyser that feeds back the residual. Use the controller-side bounds and the independent analyser alarm from TMRP's dosing controls when you derive constraints, and make your adversarial scenario one in which the controller's feedback is falsified.

### 33.6 Common errors and limits

- Hazard analysis that ignores adversaries, or security analysis that ignores hazards.
- SIS "independence" with shared engineering workstation or network.
- Resilience defined as "uptime".
- STPA reduced to a checklist without a control structure.

EX066 shows the second error at Fenwick, where the chlorine gas shutdown system shares the engineering workstation and network switch with the process controllers. TMRP's analysis of Hollin Hill avoids the first error by including the falsified level feedback as a loss scenario alongside random faults, and treats resilience as service delivered over time rather than server uptime.

### Exercises — chapter 33

**EX065 — UCA table.** *Objective:* identify unsafe control actions. *Inputs:* §33.5. *Steps:* produce the UCA table with four types and scenarios. *Expected evidence:* table. *Rubric:* 3 = four types correctly applied, scenarios include flawed feedback and adversary action, constraints derived; 2 = types confused; 1 = list of failures, not control actions; 0 = none.

**EX066 — Independence audit.** *Objective:* test SIS independence. *Inputs:* Fenwick's chlorine-gas leak shutdown system shares the engineering workstation and network switch with the process controllers. *Steps:* identify the independence violations and propose an architecture restoring independence, with residual risks. *Expected evidence:* half page. *Rubric:* 3 = shared workstation and switch identified, separate engineering access with physical key or separate workstation, separate network or hard-wired, residual stated; 2 = one violation missed; 1 = generic; 0 = none.

### Chapter synthesis

STPA treats losses as failures of control and finds unsafe control actions arising from interactions, including adversarial ones. Safety instrumented systems must be independent in sensors, logic, networks and engineering access. Resilience — anticipate, withstand, recover, adapt — must be defined against specific threats and engineered through degraded modes, buffers and practised recovery.

<!-- cyberabc:chapter-navigation:start ch-33 -->
### Continue studying — chapter 33 of 50

[← Chapter 32](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 →](#ch-34)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-34"></a>

## Chapter 34 — Critical infrastructure and sector security: integration

### Learning outcomes and connection

After this chapter you can (1) plan system integration incrementally with interface tests; (2) integrate security controls with operations — alarms, procedures, monitoring and incident response; (3) manage organisational interfaces with vendors, carriers and other utilities; and (4) recognise emergent behaviour that appears only when components combine. It follows Chapters 31–33 and prepares Design Studio II (Chapter 35).

### 34.1 Incremental integration

Integrate in small increments with interface tests at each step: gateway with RTU; gateway with SCADA; SCADA with historian replica; monitoring sensors with the log collector. Each step uses the interface control document (Chapter 16) as its test specification. When an integration test fails, the interface specification tells you which side is wrong — or reveals that the specification was ambiguous.

TMRP's order follows the interface control documents: gateway with RTU at PS2 first, then gateway with SCADA, then the DMZ replica.

### 34.2 Emergent behaviour

Combining correct components can produce incorrect systems. Examples: an authentication gateway that buffers messages during link loss and then releases a burst on reconnection, flooding the SCADA poller; failover of the SCADA pair that resets replay counters; an anomaly detector that flags every gateway retransmission as an attack. Integration testing must include whole-system scenarios — link loss and recovery, failover, maintenance mode — not only interface conformance.

TMRP met the first example in integration testing, as the worked example below describes. Each needs a scenario test.

### 34.3 Operations integration

A control is not integrated until operations can use it: alarms with clear meaning, priority and response procedures; dashboards that show security state alongside process state; playbooks linking security alarms to operational decisions (switch to local manual? call the duty manager?); and training. Alarm management practice — rationalising alarms so each requires an operator action — matters because floods of meaningless alarms hide real ones.

At LRWA, the playbook for an unexpected setpoint change is how gateway alarms reach operational decisions. Each new alarm is rationalised before release.

### 34.4 Organisational interfaces

Infrastructure security depends on organisations you do not control: the LTE carrier, RTU vendor, integrator, electricity distributor, neighbouring utilities for mutual aid. Make interfaces explicit in contracts and agreements: notification duties for incidents and vulnerabilities, access conditions, support response times, and joint exercises. An incident at the carrier is your incident too.

For LRWA, the LTE carrier is the clearest example, since TMRP's whole field conduit runs over its network. The contract should set notification times and joint exercises with measurable terms.

### 34.5 Worked example: the reconnection burst (synthetic)

During integration testing, the team disconnects the LTE head-end for 30 minutes. On reconnection, each of 42 gateways releases 180 buffered readings at once. The SCADA front end, sized for steady state, queues the burst; priority alarms are delayed by over two minutes, violating R7. Lab 13's queueing model explains why: utilisation above 0.9 makes delay explode. Fix: gateways forward only the latest value and any alarms immediately, then backfill history at a limited rate to the historian, not the SCADA poller. The fix is recorded as an interface change (ICD revision) and a regression test.

### 34.6 Practical activity

Design an integration test that combines SCADA failover with replay protection, stating the expected behaviour, the observations and the pass criterion.

Describe the sequence: one SCADA server fails over to its partner while gateways keep sending authenticated messages. The expected behaviour is that the receiving side continues to reject replays after failover, which means the last accepted counter for each station must be shared or persisted. Observe whether any old message is accepted and whether alarms still arrive within 60 seconds. The pass criterion is zero accepted replays and no gap in alarm delivery.

### 34.7 Common errors and limits

- Integration "big bang" at the end.
- Interface tests only, no whole-system scenarios.
- Security alarms without operational procedures.
- Contracts silent on incident notification and vulnerability disclosure.
- Treating emergent problems as one component's bug rather than an interface issue.

The reconnection burst shows the second and last errors: each component passed its interface tests, yet together they delayed alarms, and the fix was an interface change, not a single bug. Integration at LRWA proceeds one interface at a time. Each step has its own interface test.

### Exercises — chapter 34

**EX067 — Burst arithmetic.** *Objective:* quantify the reconnection burst. *Inputs:* 42 gateways × 180 readings released within 10 s; SCADA front end processes 50 messages/s. *Steps:* compute the time to drain the burst assuming it all arrives at once; compute the time a priority alarm at the back of the queue waits; compare with R7. *Expected evidence:* numbers. *Rubric:* 3 = 7,560 messages / 50 per s = 151.2 s, violates 60 s, explains priority queuing or latest-value fix; 2 = arithmetic right, no fix; 1 = wrong arithmetic; 0 = none.

**EX068 — Carrier agreement.** *Objective:* specify an organisational interface. *Inputs:* the LTE carrier contract. *Steps:* list six security-relevant clauses with measurable terms. *Expected evidence:* list. *Rubric:* 3 = incident notification time, vulnerability disclosure, maintenance notification, restoration priorities, access logging, joint exercise, with numbers; 2 = no numbers; 1 = generic; 0 = none.

### Chapter synthesis

Integrate incrementally with interface tests and whole-system scenarios, because emergent behaviour appears only in combination. Integrate controls into operations through meaningful alarms, playbooks and training. Make organisational interfaces explicit and measurable; your security depends on organisations you do not control.

<!-- cyberabc:chapter-navigation:start ch-34 -->
### Continue studying — chapter 34 of 50

[← Chapter 33](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 →](#ch-35)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes and connection

After this chapter you can (1) carry a design from concept to detailed design with quantitative justification; (2) integrate reliability, safety, security, performance and cost analyses into one argument; (3) build a structured assurance argument linking claims to evidence; and (4) defend detailed design decisions under review. It integrates Chapters 26–34 and prepares Chapters 36–40.

### 35.1 From concept to detailed design

Studio I selected a concept. Studio II details it: specific components, configurations, interfaces, procedures and verification. Every number from earlier chapters returns: hold-up times (Chapters 1, 6), battery sizing (Chapter 3), base rates (Chapter 7), latency (Chapter 11), fault tree (Chapter 23), detection metrics (Chapter 29), availability (Chapter 32), queueing (Chapter 36 preview). A detailed design is coherent when these numbers are consistent with each other and with the requirements.

For TMRP, the battery sizing, the 72 hours of local automatic operation, the hospital's four-hour buffer and the recovery time must all tell the same story; EX069 shows what happens when one of them does not.

### 35.2 Assurance arguments

An **assurance case** is a structured argument that a system meets a claim, supported by evidence. It has a top claim ("TMRP keeps the hospital supplied under credible scenarios including remote command forgery"), sub-claims (each requirement met; residual risks acceptable), arguments (why the sub-claims support the claim), and evidence (test results, analyses, reviews). Toulmin's model of argument — claim, data, warrant, backing, qualifier, rebuttal ([Toulmin, 1958/2003](https://doi.org/10.1017/CBO9780511840005)) — is a useful lens: what evidence supports the claim, why it is relevant, and what would defeat it. Explicit **defeaters** ("unless the SCADA centre is compromised") keep the argument honest.

### 35.3 Studio II brief (synthetic)

Produce the detailed design for TMRP phase 1 (PS2, PS3, PS4 and Hollin Hill): component list with security features; zone and conduit allowlists; key management procedure; local manual and failover procedures; alarm rationalisation for new security alarms; verification plan; and an assurance case for the top claim with at least four sub-claims and identified defeaters.

The brief covers the four assets that matter most to St Brenna's: PS2 as the proven pilot, PS3 and Hollin Hill as the reservoir path, and PS4 as the direct feed. The remaining stations and the Fenwick works follow in later phases, so the assurance case for phase 1 must say clearly that it does not cover them yet.

### 35.4 Worked example: one branch of the assurance case (synthetic)

*Sub-claim C2:* forged remote commands cannot cause loss of hospital supply. *Argument:* commands require a valid per-station MAC (R1) and fresh counter (R2); even accepted commands cannot drive the process beyond local bounds (R3); loss of both supply paths additionally requires the hospital tank to fail (fault tree). *Evidence:* T1, T2 passed (bench and site acceptance at PS2); T3 passed on v2; Lab 9 conditioning analysis; independent review of key management. *Defeaters:* (D1) SCADA servers compromised — commands are authentic; mitigated by local bounds and two-person approval for bulk changes, residual accepted by the operations director; (D2) per-station key extracted from a stolen RTU — confined to one station, detection by tamper alarm, rotation procedure. *Qualifier:* claim holds for scenarios in the risk register v1.2; not for physical attack on both pump stations.

### 35.5 Practical activity

Write the full assurance case for the Studio II brief and present it to a panel that is instructed to find defeaters.

Give the panel the brief, your component list and the assurance case, and ask them to find what would defeat each sub-claim. Record every defeater they find, whether you already listed it or not, and write a response: evidence that addresses it, a design change, or an explicit acceptance with an owner. Defeaters such as a compromised SCADA centre or a stolen RTU key are expected; the panel's job is to find ones you missed, such as misuse of local manual mode.

### 35.6 Common errors and limits

- Inconsistent numbers across analyses.
- Assurance cases with claims and no evidence, or evidence with no argument.
- Defeaters omitted to make the case look stronger.
- Detailed design that changes requirements silently.

EX069 is an example of the first error inside TMRP itself: R6 asks for eight hours, but the recovery trial measured twelve. A case that claimed R6 while citing the trial would be inconsistent, so the case records R6 as not met and explains why the hospital claim can still hold through local automatic operation.

### Exercises — chapter 35

**EX069 — Consistency check.** *Objective:* find inconsistencies across analyses. *Inputs:* PS4 battery hold-up 24 h (R5); hospital buffer 4 h; R6 restore remote operation in 8 h; Chapter 47's trial shows 12 h. *Steps:* identify which claims conflict and what the conflict means for the assurance case. *Expected evidence:* analysis. *Rubric:* 3 = identifies that R6 is not met (12 > 8), that supply does not depend on remote operation (local automatic) so hospital claim can still hold, and that the case must record R6 as failed with plan; 2 = partial; 1 = misses R6; 0 = none.

**EX070 — Find a defeater.** *Objective:* challenge an argument. *Inputs:* sub-claim C2 in §35.4. *Steps:* propose two further defeaters not listed and the evidence or design change that would address each. *Expected evidence:* two defeaters with responses. *Rubric:* 3 = credible defeaters (e.g., local manual mode misuse by insider; gateway firmware update path compromised; counter persistence failure) with specific responses; 2 = one weak; 1 = restates listed ones; 0 = none.

### Chapter synthesis

Detailed design makes every earlier number meet. An assurance case connects the top claim to evidence through explicit arguments, with qualifiers and defeaters stated openly. Consistency across analyses and honesty about defeaters are what make a detailed design defensible.

<!-- cyberabc:chapter-navigation:start ch-35 -->
### Continue studying — chapter 35 of 50

[← Chapter 34](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 →](#ch-36)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-36"></a>

## Chapter 36 — Critical infrastructure and sector security: performance and scale

### Learning outcomes and connection

After this chapter you can (1) model throughput, latency and utilisation with queueing theory and Little's law; (2) estimate the performance cost of security controls; (3) size systems for peak and degraded conditions, including attack-induced load; and (4) design for scale — fleets of thousands of devices — in key management, monitoring and updates. It builds on Chapters 11, 19 and 34 and prepares Chapter 41.

### 36.1 Queues everywhere

Messages wait in queues at gateways, servers and links. [Little's law](https://doi.org/10.1287/opre.9.3.383), $L = \lambda W$, relates the average number in a system $L$, the arrival rate $\lambda$ and the average time in the system $W$, under very general conditions. For the simple M/M/1 model (random arrivals, exponential service, one server with service rate $\mu$), utilisation is $\rho = \lambda/\mu$ and $W = 1/(\mu - \lambda)$. Delay grows without bound as $\rho \to 1$: at 80% utilisation the average message spends five service times in the system; at 96%, twenty-five. Size so that peak utilisation stays well below 1 — commonly under 0.7 for latency-critical paths.

### 36.2 The cost of security

Every control costs something: bytes (Lab 8's 22-byte overhead), CPU (MAC computation, TLS handshakes), latency (policy decisions, inspection), and operator time (re-authentication, approvals). Measure them on the bench. The costs are usually small relative to network round-trips, but they matter on constrained links (low-bandwidth radio), on constrained devices (small microcontrollers), and at scale.

For TMRP, the measured costs include the twenty-two extra bytes per frame, the MAC computation on each message at the SCADA-side verifier and the operator time for two-person approval of bulk setpoint changes. None is large, but the verifier's throughput limit is what the worked example has to size.

### 36.3 Peak, degraded and attack load

Size for the worst credible load: storm-time alarm floods, reconnection bursts after outages (Chapter 34), failover catch-up, and deliberate floods. An attacker who can send traffic to a gateway can push utilisation toward 1 and delay legitimate alarms; defences include rate limits per source, priority queues for alarms, early rejection of unauthenticated traffic (verify the cheap check first), and capacity margins.

For TMRP, the reconnection burst found in integration testing is the clearest example, and the verifier's priority queue for alarms is the defence chosen in the worked example.

### 36.4 Scale

At fleet scale, manual processes fail. Key enrolment, rotation and revocation must be automated with audit; monitoring must aggregate and prioritise; updates must be staged and observable; inventory must be continuously reconciled. A procedure that takes 30 minutes per device takes three weeks of staff time for a thousand devices.

LRWA has only 42 field stations today, but the same design may later be used for a much larger fleet, so TMRP automates key enrolment and rotation records from the start rather than relying on a spreadsheet maintained by one engineer.

### 36.5 Worked example: gateway sizing (synthetic)

The SCADA-side verifier can process 50 messages/s. In steady state LRWA's 42 stations generate about 20 messages/s ($\rho = 0.4$, $W \approx 33$ ms). During a storm, alarms raise arrivals to 40/s ($\rho = 0.8$, $W = 100$ ms, about 4 messages in the system). At 48/s, $W = 500$ ms and 24 messages are in the system on average. Sequential polling of 42 stations at 180 ms round-trip plus register time takes 7.8 s per cycle; six parallel channels reduce it to 1.3 s. Decisions: verifier capacity doubled to 100 messages/s for headroom; priority queue for alarms; report-by-exception for alarms rather than waiting for the poll.

### 36.6 Practical activity: Lab 13

```python
# Lab 13 - is the telemetry gateway fast enough? M/M/1 and a polling cycle (synthetic, offline)
mu = 50.0                                    # messages/s the gateway can verify and forward
for lam in (20.0, 40.0, 45.0, 48.0):
    rho = lam / mu; W = 1 / (mu - lam); L = lam * W
    print(f"lambda={lam:>4} rho={rho:.2f} W={W*1000:6.1f} ms L={L:5.1f} msgs")
stations, regs_per_poll, rtt_ms, per_reg_ms = 42, 3, 180, 2
cycle = stations * (rtt_ms + regs_per_poll * per_reg_ms)
print(f"sequential polling cycle: {cycle/1000:.2f} s; with 6 parallel channels: {cycle/6/1000:.2f} s")
```

Expected output:

```text
lambda=20.0 rho=0.40 W=  33.3 ms L=  0.7 msgs
lambda=40.0 rho=0.80 W= 100.0 ms L=  4.0 msgs
lambda=45.0 rho=0.90 W= 200.0 ms L=  9.0 msgs
lambda=48.0 rho=0.96 W= 500.0 ms L= 24.0 msgs
sequential polling cycle: 7.81 s; with 6 parallel channels: 1.30 s
```

The first four lines show delay growing sharply as arrivals approach the verifier's capacity of fifty messages a second: at twenty messages a second the average message waits about a third of a tenth of a second, while at forty-eight it waits half a second and two dozen messages are in the system. The polling lines show why LRWA uses six parallel channels: a sequential cycle of nearly eight seconds would leave alarms waiting long before they reached the verifier.

### 36.7 Common errors and limits

- Sizing for average load.
- Ignoring that delay explodes near full utilisation.
- Assuming security costs are negligible without measuring them on the target device.
- Manual procedures that do not scale.
- M/M/1 used where arrivals are bursty or service is deterministic; treat it as a first approximation.

TMRP's sizing avoids the first two errors by sizing for storm load and keeping the doubled verifier well below full utilisation, and treats the queueing results as a first approximation to be checked against bench measurements.

### Exercises — chapter 36

**EX071 — Doubling capacity.** *Objective:* quantify headroom. *Inputs:* Lab 13 with $\mu = 100$. *Steps:* compute $\rho$, $W$ and $L$ at 20, 40 and 48 messages/s; compare with $\mu = 50$. *Expected evidence:* table. *Rubric:* 3 = correct values (e.g., at 48/s: ρ = 0.48, W ≈ 19.2 ms, L ≈ 0.92) and conclusion; 2 = one error; 1 = one rate; 0 = none.

**EX072 — Flood defence.** *Objective:* design against attack load. *Inputs:* an attacker on the LTE network can send 1,000 forged frames/s to the verifier. *Steps:* propose three defences in order of cost and explain how each protects alarm latency. *Expected evidence:* list. *Rubric:* 3 = network-level filtering by source/tunnel, cheap pre-checks before MAC, per-source rate limits and priority queues, with reasoning about where load is shed; 2 = one defence; 1 = "add capacity" only; 0 = none.

### Chapter synthesis

Queues govern latency; Little's law and simple queueing models show that delay explodes as utilisation approaches one. Measure the costs of security controls, size for peak, degraded and attack load with priority for alarms, and automate fleet-scale processes from the start.

<!-- cyberabc:chapter-navigation:start ch-36 -->
### Continue studying — chapter 36 of 50

[← Chapter 35](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 →](#ch-37)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-37"></a>

## Chapter 37 — Critical infrastructure and sector security: operations

### Learning outcomes and connection

After this chapter you can (1) design security operations for OT — monitoring, triage, escalation, coordination with process operations; (2) write operational procedures and playbooks that operators can execute under stress; (3) manage change, access and vulnerabilities in daily operations; and (4) learn from incidents and near misses without blame. It builds on Chapters 18, 29 and 34 and prepares Chapters 38 and 47.

### 37.1 Security operations in OT

OT security monitoring watches network traffic, logs and process data for signs of misuse. Triage in OT differs from IT: the first question is not "is this malicious?" but "is the process safe?" Escalation paths therefore run to the control room and duty operations manager as well as to security staff. Many utilities do not have a 24/7 security team; the control room is staffed 24/7 and must be able to act on security alarms with clear playbooks, escalating to on-call security specialists.

### 37.2 Playbooks

A playbook is a short, tested procedure for a specific situation: trigger, immediate safety actions, information to collect, decisions and who makes them, communications, and return to normal. Write for a tired operator at 03:00: numbered steps, clear decision points, phone numbers, no jargon. Test each playbook in exercises and update it after every use. Incident handling guidance such as [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) provides general structure; OT playbooks add process safety steps.

LRWA's playbook for an unexpected setpoint change is written to this standard.

### 37.3 Change, access and vulnerability management

Daily operations keep the system in its designed state: change management (no configuration change without approval and record); access management (joiners, movers, leavers; vendor sessions approved per use); vulnerability management (track advisories such as [CISA ICS advisories](https://www.cisa.gov/news-events/ics-advisories), assess applicability, plan remediation, Chapter 12). Drift — undocumented changes accumulating — is the commonest way a well-designed system becomes insecure.

At LRWA, the forgotten enterprise reporting script found in the flow review is an example of drift, and change control on every conduit is how TMRP keeps such paths from reappearing.

### 37.4 Learning without blame

Incidents and near misses are evidence about the system. [Reason (2000)](https://doi.org/10.1136/bmj.320.7237.768) contrasted the person approach (blaming individuals) with the system approach (defences, barriers and latent conditions), arguing the latter is more effective. After-action reviews ask what happened, why it made sense to the people involved at the time, which defences worked or failed, and what will change. Blame suppresses reporting, and unreported near misses are lost lessons.

At LRWA, the technician who connected a laptop to the PS3 network in EX074 is treated in this way: the review asks why the jump host felt too slow and what made the shortcut possible.

### 37.5 Worked example: playbook "unexpected setpoint change" (synthetic)

*Trigger:* SCADA shows a setpoint change at any station not matching an operator action in the last 5 minutes, or a gateway logs repeated MAC failures. *Immediate safety actions:* (1) check the station's process values against independent measurements; (2) if outside normal range, restore the previous setpoint locally or switch to local manual via the duty technician; (3) do not shut down remote telemetry. *Collect:* station, time, old/new values, gateway log extract, operator log. *Decide:* duty manager decides whether to disable remote writes fleet-wide (gateway configuration switch). *Communicate:* security on-call within 30 minutes; hospital liaison if PS3/PS4 affected. *Return to normal:* remote writes re-enabled only after security on-call agrees.

### 37.6 Practical activity

Run the playbook in a tabletop with a scripted inject sequence (first a single setpoint change, then MAC failures at a second station, then a phone call from the hospital about low pressure). Record decision times and ambiguities and revise the playbook.

Run the injects in order and note the time of each decision. Watch in particular whether the team keeps remote telemetry running, as the playbook requires, and whether the duty manager decides on disabling remote writes across the fleet before the hospital call arrives. Record every point where someone asked what the playbook meant. After the tabletop, rewrite those steps and schedule a second run to check the revisions.

### 37.7 Common errors and limits

- Security alarms routed to a team that is not staffed when they fire.
- Playbooks written for experts, never tested.
- Change management bypassed "temporarily".
- After-action reviews that end with "operator error".

LRWA's playbook design answers these: security alarms reach the control room, which is staffed every hour, and the security on-call is called within 30 minutes. The playbook is tested in tabletops, and change control has no temporary exceptions. After-action reviews at LRWA look for latent conditions, such as a slow jump host, rather than ending with operator error.

### Exercises — chapter 37

**EX073 — Playbook review.** *Objective:* improve a playbook. *Inputs:* §37.5. *Steps:* identify three weaknesses (e.g., ambiguous thresholds, missing contacts, unsafe default) and rewrite the affected steps. *Expected evidence:* revised steps. *Rubric:* 3 = substantive weaknesses fixed with executable steps; 2 = cosmetic changes; 1 = critique only; 0 = none.

**EX074 — Near-miss review.** *Objective:* conduct a blameless review. *Inputs:* a technician connected a laptop to the PS3 control network to download logs, bypassing the jump host; the laptop had not been scanned. No incident followed. *Steps:* write a one-page review: what happened, why it made sense, defences that failed, system changes. *Expected evidence:* review. *Rubric:* 3 = explains local rationality (jump host slow, deadline), identifies latent conditions (no port security, no easy log path), proposes system changes; 2 = some blame; 1 = "retrain technician"; 0 = none.

### Chapter synthesis

OT security operations start with process safety and route escalation through the control room. Playbooks must be short, tested and executable under stress. Daily change, access and vulnerability management keep the system as designed, and blameless learning from incidents and near misses improves the defences.

<!-- cyberabc:chapter-navigation:start ch-37 -->
### Continue studying — chapter 37 of 50

[← Chapter 36](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 →](#ch-38)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-38"></a>

## Chapter 38 — Critical infrastructure and sector security: validation

### Learning outcomes and connection

After this chapter you can (1) distinguish validation (right system for the need) from verification (system built to its specification); (2) validate with stakeholders through demonstrations, operational trials and exercises; (3) use traceability to show which needs are supported by evidence and which are not; and (4) report validation results honestly, including partial results. It builds on Chapters 16, 24 and 30 and prepares Chapters 40 and 48.

### 38.1 Verification is not validation

A system can pass every test against its specification and still fail its users if the specification was wrong or incomplete. Validation asks whether the system meets stakeholder needs in its intended environment: can operators actually run local manual mode at night? Does the hospital actually get water within its buffer when PS4 is lost? Validation evidence comes from realistic use: operational trials, demonstrations with stakeholders, exercises and early operating data.

For TMRP, the night exercise of local manual mode is the validation activity that answers the first question.

### 38.2 Traceability as an evidence map

Trace needs to requirements to tests to results. Then ask three questions: which requirements have no test (untested claims)? Which tests failed or were not run (unsupported claims)? Which needs depend only on requirements that are not yet verified (unvalidated needs)? Lab 14 computes these for the TMRP dossier.

For TMRP the questions are concrete. R4 has no test because its demonstration was never scheduled. R9, the independent dosing alarm, has no test at all: the requirement table names a test as its verification method, but no test was ever written for it. R3's only recorded test is the failed one on v1, and R8's test has not run. N1 depends on R4, so it cannot be claimed as validated until the night exercise takes place. Lab 14 prints these gaps directly.

### 38.3 Stakeholder validation

Involve the people the system serves. Operators validate procedures and displays; maintenance staff validate repairability and spares; the hospital validates that the supply arrangements meet its needs; regulators validate compliance reasoning. Record their findings as you would review findings, with responses.

For TMRP, operators validate the local manual procedure and the new security alarms, maintenance staff check that gateways can be replaced from spares, and the hospital confirms that the supply arrangements and its four-hour buffer meet its needs. Their findings go into the same response log as the design review findings.

### 38.4 Reporting partial results

Report validation status per need: validated, partially validated (with what remains), not validated. Do not round up. "N1 partially validated: PS4 loss trial met the 4 h buffer; combined PS4 and grid F1 loss not yet trialled."

TMRP's evidence map makes this concrete: N1 depends on R4, which has not yet been demonstrated, so N1 is reported as not validated until the night exercise takes place, even though most of its other requirements have passed their tests. The status is updated after the exercise.

### 38.5 Worked example: TMRP evidence map (synthetic)

Lab 14 shows: R4 (local manual operation) has no test — it was planned as a demonstration and never scheduled; R3 has a failed test (on v1; the re-test on v2 has not yet been entered into the matrix); R8's test T6 has not run. R9 (independent dosing alarm) has no test either: its verification method is "Test", but no test identifier was ever assigned, so the evidence for it is a design intent, not a result. Verified: 5 of 9 requirements (55.6%). Consequence for validation: N1 (hospital supply) depends on R4, so N1 cannot be claimed as validated; the night-time local manual exercise is scheduled as the validation activity. The matrix also exposes an administrative gap — the v2 re-test of T3 must be recorded — which is exactly the kind of inconsistency examiners and auditors find.

### 38.6 Practical activity: Lab 14

```python
# Lab 14 - requirements traceability: what is claimed but not shown? (synthetic TMRP dossier, offline)
REQS = ["R1 auth telemetry", "R2 replay reject", "R3 setpoint bounds", "R4 local manual", "R5 24h hold-up",
        "R6 restore 8h", "R7 alarm 60s", "R8 log integrity", "R9 dosing alarm"]
TESTS = {"T1": ["R1"], "T2": ["R1", "R2"], "T3": ["R3"], "T4": ["R5"], "T5": ["R7"], "T6": ["R8"], "T7": ["R6"]}
RESULT = {"T1": "pass", "T2": "pass", "T3": "fail", "T4": "pass", "T5": "pass", "T6": "not run", "T7": "pass"}
ids = [r.split()[0] for r in REQS]
cov = {r: [t for t, rs in TESTS.items() if r in rs] for r in ids}
verified = [r for r in ids if cov[r] and all(RESULT[t] == "pass" for t in cov[r])]
print("untested:", [r for r in ids if not cov[r]])
print("tested but not passing:", [r for r in ids if cov[r] and r not in verified])
print(f"verified {len(verified)}/{len(ids)} = {100*len(verified)/len(ids):.1f}%")
```

Expected output:

```text
untested: ['R4', 'R9']
tested but not passing: ['R3', 'R8']
verified 5/9 = 55.6%
```

The output shows that R4 and R9 have no test, that R3 and R8 are tested but not passing, and that five of nine requirements are verified. R3's status is out of date rather than truly failed: the v2 re-test passed, but nobody entered it in the matrix, which is exactly the administrative gap the worked example warns about. EX075 updates the map. R9 is the harder lesson: the dosing alarm appears in the requirement set, the risk table and the dosing controls, so it feels covered, yet no test was ever assigned to it. An earlier version of this matrix left R9 out of the list entirely, which raised the verified share from five of nine to five of eight without any new evidence. A matrix must list every defined requirement, because a requirement it omits cannot be reported as untested.

### 38.7 Common errors and limits

- Calling a passed test suite "validation".
- Stakeholders consulted only at the start.
- Rounding partial validation up to "validated".
- Evidence maps not updated after re-tests.

TMRP's map shows the last error itself: the T3 re-test on v2 passed, but the matrix was never updated. Stakeholders such as operators and the hospital are involved throughout, not only when the requirements were written, and the evidence map is updated every time a re-test or demonstration produces a result, so the reported validation status never runs ahead of the evidence.

### Exercises — chapter 38

**EX075 — Update the map.** *Objective:* maintain traceability. *Inputs:* Lab 14. *Steps:* (1) add T3b (v2 re-test) covering R3 with result "pass" and remove T3's link to R3 as superseded; (2) add T8 demonstration covering R4 with result "pass"; (3) run T6 with result "pass"; recompute. *Expected evidence:* code and output. *Rubric:* 3 = eight of nine verified (88.9%), R9 still listed as untested because no dosing-alarm test exists, with a note that verification ≠ validation; 2 = one change missed; 1 = not run; 0 = none.

**EX076 — Validation plan for N1.** *Objective:* plan stakeholder validation. *Inputs:* N1 "hospital must not lose water > 4 h". *Steps:* propose two validation activities with stakeholders, realistic conditions, observations and success criteria. *Expected evidence:* plan. *Rubric:* 3 = realistic activities (night exercise of local manual with real staffing; planned isolation of PS4 with hospital monitoring), criteria tied to the 4 h buffer, stakeholders named by role; 2 = criteria vague; 1 = tests renamed as validation; 0 = none.

### Chapter synthesis

Verification asks whether the system was built right; validation asks whether it is the right system. Use traceability as an evidence map to find untested, unsupported and unvalidated claims, validate with the people the system serves under realistic conditions, and report partial results as partial.

<!-- cyberabc:chapter-navigation:start ch-38 -->
### Continue studying — chapter 38 of 50

[← Chapter 37](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 →](#ch-39)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-39"></a>

## Chapter 39 — Critical infrastructure and sector security: maintainability

### Learning outcomes and connection

After this chapter you can (1) design for maintainability over long lifecycles — updates, spares, skills, documentation; (2) manage technical debt and obsolescence in OT; (3) plan cryptographic agility and the transition to post-quantum cryptography; and (4) plan decommissioning securely. It builds on Chapters 8, 14 and 31 and prepares Chapters 41 and 44.

### 39.1 Long lifecycles

Infrastructure assets last decades; software and threats change in months. Maintainability means the system can be kept secure and functional for its whole life: components replaceable without redesign; updates possible without long outages; documentation current; skills available. Design choices that harm maintainability include proprietary protocols with a single supplier, undocumented custom code, and hardware with no update path.

For TMRP, RTUs installed now may still run in the 2040s, so the gateway design, the message format and the key management must all be maintainable over that span.

### 39.2 Technical debt and obsolescence

Technical debt is the future cost of shortcuts taken now: a hard-coded configuration, a skipped test, a gateway built "temporarily" for legacy RTUs. Record debt items with owner, cost to fix and risk of leaving them. Obsolescence management tracks end-of-sale and end-of-support dates for every component and plans replacement before support ends, holding spares where replacement is slow.

TMRP's gateways for the legacy RTU-A units at PS1 and PS2 are recorded as debt with a three-year horizon. Spares are bought before end of sale.

### 39.3 Cryptographic agility

Algorithms weaken and standards change. Cryptographic agility is the ability to change algorithms and key sizes without redesigning the system: algorithm identifiers in message formats, firmware update paths, and key management that can provision new key types. NIST published its first post-quantum cryptography standards (FIPS 203, 204 and 205) in August 2024 ([NIST announcement](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)); infrastructure equipment purchased now may still be operating when quantum-capable adversaries are plausible, so public-key mechanisms in long-lived devices need a migration path. Symmetric MACs such as HMAC-SHA256 are much less affected; key exchange and signatures are where migration matters.

### 39.4 Secure decommissioning

Retired devices contain keys, configurations and network details. Decommissioning steps: revoke keys and certificates; remove accounts; wipe or destroy storage according to policy; update inventory, models and allowlists; and remove firewall rules that served the device. Stale rules for decommissioned devices are a classic path for attackers who place a new device at an old address.

TMRP's maintainability review found that no decommissioning procedure existed, so one was written and linked to change management. It will be used first when PS2's legacy RTU-A and its gateway are replaced, as EX078 describes.

### 39.5 Worked example: TMRP maintainability review (synthetic)

The review finds: (1) the PS1/PS2 gateways are technical debt with a three-year horizon — recorded with replacement plan; (2) the message format in Lab 8 lacks an algorithm identifier — changed to include a one-byte suite ID (version 1 = HMAC-SHA256-128) before fleet roll-out, costing one byte per message; (3) RTU-B firmware signing uses a classical signature scheme — vendor asked for a post-quantum migration roadmap as a contract condition; (4) no spare LTE modems are held and the model reaches end of sale next year — buy spares now, plan replacement; (5) decommissioning procedure missing — written and linked to change management.

### 39.6 Practical activity

Build an obsolescence register for TMRP components (RTUs, gateways, modems, SCADA servers, OS, HSM) with assumed dates, support status, spares held and replacement plan.

Include every component the TMRP review mentions: RTU-A and RTU-B, the gateways, the LTE modems, the SCADA servers and their operating system, and the hardware security module. For each, record the assumed end-of-sale and end-of-support dates, the spares held and the replacement plan. Flag any component whose support ends before its planned replacement, as the review found for the LTE modems. Keep the register under change control so it stays current.

### 39.7 Common errors and limits

- Designs that require the original supplier forever.
- Technical debt that is not recorded.
- Message formats without versioning or algorithm identifiers.
- Decommissioned devices leaving keys and firewall rules behind.

TMRP's review found the third error in the Lab 8 frame and fixed it with a one-byte suite identifier before fleet rollout. It also recorded the legacy gateways as debt and wrote the missing decommissioning procedure. Spare LTE modems are bought before the model's end of sale. The new procedure revokes keys and removes stale firewall rules.

### Exercises — chapter 39

**EX077 — Agility retrofit.** *Objective:* add cryptographic agility. *Inputs:* Lab 8 frame format. *Steps:* add a one-byte suite ID and a receiver policy that accepts only configured suites; show how suite 2 (a different MAC) could be introduced during a transition period, and how suite 1 would be retired. *Expected evidence:* design and short code sketch. *Rubric:* 3 = suite ID authenticated (inside MAC), per-station allowed-suites policy, downgrade prevention, retirement step; 2 = suite ID not authenticated; 1 = description only; 0 = none.

**EX078 — Decommissioning checklist.** *Objective:* retire a device securely. *Inputs:* PS2's legacy RTU-A and gateway being replaced by RTU-B. *Steps:* write a checklist of at least eight steps with evidence for each. *Expected evidence:* checklist. *Rubric:* 3 = keys revoked, accounts removed, storage wiped, inventory/model/allowlist updated, firewall rules removed, monitoring baselines updated, spares disposition, sign-off; 2 = missing rules or keys; 1 = generic; 0 = none.

### Chapter synthesis

Design for decades: replaceable components, updatable software, current documentation, available skills. Record technical debt, manage obsolescence ahead of end of support, build cryptographic agility into formats and update paths with a post-quantum migration plan, and decommission so that nothing — keys, accounts, rules — outlives the device.

<!-- cyberabc:chapter-navigation:start ch-39 -->
### Continue studying — chapter 39 of 50

[← Chapter 38](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 →](#ch-40)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes and connection

After this chapter you can (1) design and run a seeded fault-injection campaign against a security control; (2) classify outcomes and compute detection rates per fault class; (3) find gaps between what a control detects and what a requirement needs; and (4) report a campaign reproducibly. It extends Chapter 30 to environmental faults and attacks and prepares the capstone (Chapters 44–47).

### 40.1 Fault injection

Fault injection deliberately introduces faults — corrupted, dropped, delayed, replayed or reordered messages; process restarts; clock steps; resource exhaustion — to observe how a system behaves. It tests error handling that ordinary tests rarely reach. A campaign specifies the fault model (which faults, at what rates), the system under test, the oracle (what correct behaviour is for each fault) and the measurements.

For TMRP, the receiver campaign in this chapter injects corruption, replay, delay and drops. Each fault has an oracle. Results are counted per class.

### 40.2 Oracles and classification

For each injected fault, define the expected outcome: corrupted → rejected as corrupt; replayed → rejected as replay; delayed beyond the freshness window → rejected as stale; dropped → detected as a gap (or not, if the design does not detect gaps). Classify observed outcomes against expected ones. A fault that produces "ok" when it should have been rejected is a **silent failure** — the most important class to find.

For TMRP's receiver, the drop class is the one where the oracle exposed a gap: the design had no expected outcome for a lost message, because nobody had asked what should happen.

### 40.3 Seeds, rates and coverage

Seed the fault generator, record the seed, and report counts per fault class. Choose rates that produce enough events of each class to be meaningful; a campaign of 500 messages with 5% per fault class gives roughly 25 events each — enough to find systematic failures, not enough to estimate rare ones precisely. Extend the campaign for classes of special concern.

TMRP's campaign uses seed forty, five hundred messages and five per cent per fault class, so each class produces enough events to show systematic behaviour. The capstone extends the campaign to ten thousand messages across seven fault classes, including restart and reordering.

### 40.4 Worked example: telemetry receiver campaign (synthetic)

Lab 15 sends 500 messages with seed 40; each has an 80% chance of no fault and 5% each of corruption, replay of an earlier valid message, a 120 s delay (freshness window 60 s) and drop. Results: every corrupted message was rejected as corrupt; every replay as replay; every delayed message as stale; no fault produced a silent "ok". But **drops are invisible to the receiver**: 21 messages were lost and the receiver raised nothing. The receiver's counter check rejects old counters but does not alarm on gaps. Requirement R7 (alarms within 60 s) implies that the loss of a station's data must itself be visible. Design change: alarm when no valid message arrives from a station for 60 s, and log counter gaps. The campaign is re-run after the change with the same seed.

### 40.5 Practical activity: Lab 15

```python
# Lab 15 - fault-injection campaign against the telemetry receiver (synthetic, seeded, offline)
import random, hmac, hashlib, struct
KEY = b"k" * 32
def seal(c, lvl, ts):
    b = struct.pack(">QHI", c, lvl, ts); return b + hmac.new(KEY, b, hashlib.sha256).digest()[:16]
def receive(m, state, now, max_age=60):
    b, tag = m[:14], m[14:]
    if len(m) != 30 or not hmac.compare_digest(tag, hmac.new(KEY, b, hashlib.sha256).digest()[:16]): return "corrupt"
    c, lvl, ts = struct.unpack(">QHI", b)
    if c <= state["last"]: return "replay"
    if now - ts > max_age: return "stale"
    state["last"] = c; return "ok"
rng = random.Random(40); state = {"last": 0}; tally = {}; sent = []
for i in range(1, 501):
    now = 10 * i; m = seal(i, 300, now); fault = rng.choices(["none", "corrupt", "replay", "delay", "drop"], [80, 5, 5, 5, 5])[0]
    if fault == "corrupt": m = m[:5] + bytes([m[5] ^ 0x10]) + m[6:]
    if fault == "replay" and sent: m = rng.choice(sent)
    if fault == "drop": tally[("drop", "lost")] = tally.get(("drop", "lost"), 0) + 1; continue
    arrive = now + (120 if fault == "delay" else 1)
    out = receive(m, state, arrive)
    tally[(fault, out)] = tally.get((fault, out), 0) + 1
    if fault == "none": sent.append(m)
for k in sorted(tally): print(k, tally[k])
```

Expected output:

```text
('corrupt', 'corrupt') 14
('delay', 'stale') 22
('drop', 'lost') 21
('none', 'ok') 419
('replay', 'replay') 24
```

Every corrupted, replayed and delayed message ended in the class its oracle predicted, and no fault produced a silent acceptance. The dropped messages are the finding: twenty-one were lost and the receiver raised nothing, because counter checks only reject old messages. That result led to the stale-station alarm, which fires when no valid message arrives from a station for sixty seconds, and to review finding F2. The campaign is then rerun with the same seed to confirm the change.

### 40.6 Common errors and limits

- Fault models limited to what the designer expected.
- No oracle, so outcomes cannot be judged.
- Unseeded campaigns.
- Treating "no silent failures observed" as proof.
- Not re-running the campaign after fixes.

TMRP's first campaign showed the first error: drops were silent because the designers never listed loss of data as a fault their receiver should notice. Rerunning after adding the stale-station alarm is how the fix is confirmed. Its seed is recorded, so the rerun is comparable. The drop class is now kept in every run.

### Exercises — chapter 40

**EX079 — Gap detection.** *Objective:* close the drop gap. *Inputs:* Lab 15. *Steps:* add gap detection (counter jump greater than 1 logs `gap`) and rerun with the same seed; report how many gap events are logged and why the number may differ from the number of drops. *Expected evidence:* code and output. *Rubric:* 3 = implemented correctly; explains that consecutive drops produce one gap event, and that replays and rejected messages also affect counter continuity; 2 = implemented, no explanation; 1 = not run; 0 = none.

**EX080 — Extend the fault model.** *Objective:* add faults. *Inputs:* Lab 15. *Steps:* add two fault classes — reordering (swap two consecutive messages) and receiver restart (reset `state`) — define oracles, run and report silent failures. *Expected evidence:* code, oracles and results. *Rubric:* 3 = reordering causes the earlier message to be rejected as replay (acceptable or not — argued), restart allows replays (silent failure) unless state persisted; 2 = one class; 1 = no oracle; 0 = none.

### Chapter synthesis

Fault injection exercises the error handling that ordinary tests miss. Define the fault model and oracle in advance, seed and count, classify outcomes and hunt silent failures. Lab 15 shows the typical result: the control rejects what it was designed to reject and is blind to what nobody listed — here, loss of data.

<!-- cyberabc:chapter-navigation:start ch-40 -->
### Continue studying — chapter 40 of 50

[← Chapter 39](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 →](#ch-41)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-41"></a>

## Chapter 41 — Critical infrastructure and sector security: system optimization

### Learning outcomes and connection

After this chapter you can (1) formulate security investment as an optimisation problem with objectives and constraints; (2) solve small problems exactly and understand why greedy heuristics can fail; (3) handle multiple objectives and uncertainty with Pareto analysis and sensitivity; and (4) present optimisation results as decision support, not decisions. It builds on Chapters 25, 32 and 36 and prepares the capstone.

### 41.1 Formulating the problem

Choose a set of controls $S$ to maximise benefit $\sum_{c\in S} b_c$ subject to cost $\sum_{c\in S} k_c \le B$. This is the 0/1 knapsack problem. Benefits might be expected annual loss reduction, reduction in people-hours without water, or reduction in top-event probability. Real problems add constraints (dependencies between controls, staffing limits, phases) and interactions (two controls addressing the same scenario do not add benefits).

For TMRP's phase 1, the benefits in Lab 16 are synthetic estimates of expected annual loss reduction.

### 41.2 Exact and heuristic solutions

With a handful of candidates, enumerate all subsets ($2^n$). Dynamic programming solves knapsack problems exactly in time proportional to $n \times B$ for integer costs. The **greedy** heuristic — pick by benefit/cost ratio until the budget is spent — is fast and intuitive but can leave budget unused or miss better combinations. For larger problems, integer programming solvers are standard.

Lab 16 shows the greedy failure on TMRP's seven candidates. Greedy left budget unused and missed the spare RTUs, a gap exhaustive search found at once.

### 41.3 Multiple objectives and uncertainty

Security investments trade off cost, risk reduction, operability and other goods. A solution is **Pareto-optimal** if no other solution is better in one objective without being worse in another; present the Pareto set rather than a single weighted answer. Benefits are uncertain estimates; test whether the optimal set changes when benefits vary within plausible ranges. Robust choices — those that are good across scenarios — are often preferable to choices optimal only under point estimates.

For TMRP, the robustness check in EX082 varies each benefit by twenty per cent and finds that three of the fourteen runs change the optimum, so the last part of the portfolio is a near-tie.

### 41.4 Interactions

Benefits are rarely additive. Authenticated telemetry and network monitoring both reduce forged-command risk; once authentication is in place, monitoring's additional benefit for that scenario is smaller. Model interactions by computing benefit from the scenario model (e.g., the fault tree) for each candidate set rather than adding per-control numbers.

In Lab 16 the benefits are simply added, which is a simplification: authenticated telemetry and the network detection sensor both reduce forged-command risk, so their combined value is less than the sum. A better model recomputes benefit from the fault tree for each candidate set.

### 41.5 Worked example: TMRP phase 1 portfolio (synthetic)

Seven candidate controls with synthetic costs and benefits, budget 250 k (Lab 16). Greedy by ratio picks offline backups, local manual mode, authenticated telemetry and engineering-workstation hardening: cost 215 k, benefit 480 k. Exhaustive search finds a better set — authenticated telemetry, local manual mode, offline backups and spare RTUs — at cost 250 k and benefit 530 k. Greedy took the cheap workstation hardening early and could then not afford the spare RTUs. The team presents both, notes that benefit estimates have wide uncertainty, and shows that when each benefit varies by ±20% individually, authenticated telemetry and local manual mode stay in every optimum while three runs replace offline backups and spare RTUs with the backup generator (EX082) — a robustness check, not a proof.

### 41.6 Practical activity: Lab 16

```python
# Lab 16 - choose controls under a budget: exhaustive search beats greedy here (synthetic, offline)
from itertools import combinations
C = {  # control: (cost k$, expected annual loss reduction k$)
    "auth_telemetry": (120, 260), "backup_gen_PS4": (90, 150), "local_manual_mode": (40, 110),
    "offline_backups": (30, 70), "eng_ws_hardening": (25, 40), "ndr_sensor": (100, 120), "spare_rtus": (60, 90)}
B = 250
best = max((s for r in range(len(C)+1) for s in combinations(C, r) if sum(C[c][0] for c in s) <= B),
           key=lambda s: sum(C[c][1] for c in s))
print("optimal:", sorted(best), "cost", sum(C[c][0] for c in best), "benefit", sum(C[c][1] for c in best))
g, spent = [], 0
for c in sorted(C, key=lambda c: C[c][1] / C[c][0], reverse=True):
    if spent + C[c][0] <= B: g.append(c); spent += C[c][0]
print("greedy :", sorted(g), "cost", spent, "benefit", sum(C[c][1] for c in g))
```

Expected output:

```text
optimal: ['auth_telemetry', 'local_manual_mode', 'offline_backups', 'spare_rtus'] cost 250 benefit 530
greedy : ['auth_telemetry', 'eng_ws_hardening', 'local_manual_mode', 'offline_backups'] cost 215 benefit 480
```

The exhaustive optimum spends the whole budget on authenticated telemetry, local manual mode, offline backups and spare RTUs. Greedy chooses workstation hardening early because of its good ratio, leaving too little money for the spare RTUs and finishing with less benefit and some budget unused. On seven candidates the exhaustive search is instant, so there is no reason to accept the greedy answer; with hundreds of candidates, an integer programming solver would replace both. Record both results. Note the unused budget.

### 41.7 Common errors and limits

- Adding benefits of interacting controls.
- Presenting a single optimum without sensitivity.
- Greedy heuristics used without checking against exact solutions on small instances.
- Optimisation results presented as decisions rather than inputs to decisions.
- Benefit numbers with no stated basis.

TMRP's portfolio avoids the third error by checking greedy against exhaustive search, and presents both results with the robustness check to the decision owner. Each benefit figure is labelled as a synthetic estimate, and the result is offered as decision support. Interactions are noted.

### Exercises — chapter 41

**EX081 — Budget sweep.** *Objective:* see how the optimum changes with budget. *Inputs:* Lab 16. *Steps:* compute the optimal set and benefit for budgets 150, 200, 250, 300 and 350 k; plot or tabulate the marginal benefit per extra 50 k. *Expected evidence:* table. *Rubric:* 3 = correct optima (run code), diminishing marginal benefit observed and interpreted; 2 = one error; 1 = one budget; 0 = none.

**EX082 — Robustness.** *Objective:* test sensitivity of the optimum. *Inputs:* Lab 16. *Steps:* for each control, multiply its benefit by 0.8 and by 1.2 (others unchanged), recompute the optimum, and report any change. *Expected evidence:* table of 14 runs. *Rubric:* 3 = correct results and conclusion about robustness; 2 = partial; 1 = not run; 0 = none.

### Chapter synthesis

Formulate investment choices as optimisation with explicit objectives and constraints, solve small problems exactly and distrust greedy shortcuts, model interactions instead of adding benefits, present Pareto sets and sensitivity, and offer the result as structured support for a human decision.

<!-- cyberabc:chapter-navigation:start ch-41 -->
### Continue studying — chapter 41 of 50

[← Chapter 40](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 →](#ch-42)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-42"></a>

## Chapter 42 — Critical infrastructure and sector security: applied research

### Learning outcomes and connection

After this chapter you can (1) frame an engineering question that needs new evidence; (2) design a small applied study — testbed experiment, simulation study or field measurement — with controls and reproducibility; (3) use public datasets and testbeds responsibly; and (4) report results with their limits. It is the engineering counterpart of the master's and doctoral research books and prepares the capstone and thesis (Chapters 44–49).

### 42.1 Engineering research versus academic research

This course's applied research answers a design question for a specific system, with evidence good enough for an engineering decision. It differs from the [master's book](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md), which teaches how to design and defend one ethically reviewed empirical study, and from the [doctoral book](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md), which asks for an original, independently validated contribution to knowledge. An engineering study succeeds if it changes or confirms a design decision with evidence that a reviewer can check.

### 42.2 Designing a small study

State the question and the decision it informs; define the measurement (Chapter 29); choose a design — comparison of alternatives on a testbed, a parameter sweep in simulation, or measurement of an existing system; fix the analysis before running; control for confounders (same load, same hardware, same seeds); repeat runs to measure variability; and record everything to allow reproduction ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)).

TMRP's detector study follows this pattern, with its analysis rule fixed before any run. Its seeds are recorded.

### 42.3 Public datasets and testbeds

Public industrial-security datasets and testbeds allow experiments without touching real infrastructure. The Secure Water Treatment (SWaT) testbed dataset described by [Goh et al. (2017)](https://doi.org/10.1007/978-3-319-71368-7_8) and the BATADAL competition on water distribution networks reported by [Taormina et al. (2018)](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969) are widely used. Know their limits: testbeds are smaller and cleaner than real plants, attack sets are chosen by researchers, and benchmark performance does not transfer automatically. Read evaluation pitfalls before claiming results ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp); [Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 42.4 Ethics and authorisation

Applied research on real systems requires the owner's written authorisation and, where people or personal data are involved, ethics review (Chapter 10). Results that reveal weaknesses in specific systems go to the owner, not to a conference.

For TMRP, the detector study uses simulation and LRWA's own historian data under the programme's authority. Any finding about a vendor's product would go to that vendor privately before anything is written for a wider audience, and no real station is used as an experimental subject.

### 42.5 Worked example: is the cumulative detector worth deploying? (synthetic)

Question: should TMRP deploy the cumulative mass-balance detector of Chapter 17 at Hollin Hill? Decision informed: deploy, with which threshold and recalibration interval. Study design: simulation sweep over noise levels (0.005–0.02 m), flow-meter drift (0–1%) and thresholds (0.02–0.08 m), 100 seeded runs per cell, measuring false alarms per month and detection time for ramp attacks of 0.01–0.1 m/h. Analysis fixed in advance: choose the threshold with fewer than one false alarm per month at the measured noise level and report detection time at that threshold. Validation: compare simulated noise with two weeks of historian data. Limits: perfect-mixing tank model; attacker who controls flow meters is out of scope.

### 42.6 Practical activity

Implement a reduced version of §42.5 using Lab 7: three thresholds × three noise levels × 20 seeds; report false alarms and ramp detection times in a table with variability.

Fix your analysis rule before running: for example, choose the lowest threshold with no false alarms in the no-attack runs at each noise level. Seed each run and record the seeds. Report the number of false alarms and the ramp detection time for every cell with its spread across seeds, not just the mean. Then state one limit of the reduced study, such as perfect flow meters, and the direction in which it biases your results.

### 42.7 Common errors and limits

- Studies without a decision they inform.
- Analysis chosen after seeing results.
- Single runs reported as results.
- Benchmark performance claimed to transfer to real plants.
- Weaknesses of real systems published without coordination.

The cumulative detector study in the worked example avoids each of these: it informs a deployment decision, fixes its analysis rule in advance, uses a hundred runs per cell, validates its noise model against two weeks of LRWA historian data and states that an attacker controlling the flow meters is out of scope.

### Exercises — chapter 42

**EX083 — Study protocol.** *Objective:* write a pre-specified protocol. *Inputs:* §42.5. *Steps:* write a one-page protocol: question, decision, design, measurements, analysis rule, validation, limits. *Expected evidence:* protocol. *Rubric:* 3 = complete, analysis rule fixed in advance, validation against real noise data, limits honest; 2 = analysis vague; 1 = no decision; 0 = none.

**EX084 — Dataset limits.** *Objective:* assess transfer from a testbed. *Inputs:* a vendor claims 99% detection on a public water testbed dataset. *Steps:* list five questions you would ask before accepting this for LRWA. *Expected evidence:* list. *Rubric:* 3 = base rate and false-alarm rate in operations, attack set realism, evaluation protocol (point adjustment, data leakage), plant scale/difference, adaptation to adversaries; 2 = three good questions; 1 = generic; 0 = none.

### Chapter synthesis

Engineering research answers a design question with checkable evidence. Pre-specify the study, control confounders, repeat runs, use public testbeds within their limits, obtain authorisation for anything real, and report results with their boundaries.

<!-- cyberabc:chapter-navigation:start ch-42 -->
### Continue studying — chapter 42 of 50

[← Chapter 41](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 →](#ch-43)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes and connection

After this chapter you can (1) plan and complete a supervised practice placement in an operator, vendor, integrator, regulator or public agency; (2) work within the placement's authorisation, confidentiality and safety rules; (3) keep a reflective practice log that links observed work to the course's methods; and (4) produce a placement report that is useful to the host and safe to share. It applies the whole course to real practice and prepares the capstone.

### 43.1 Purpose of practice

Practice exposes the constraints that textbooks smooth over: procurement cycles, staffing, legacy equipment, regulatory deadlines, union agreements, budgets, and the gap between procedure and practice. Engineers who have seen a control room at night design differently from those who have not.

The TMRP case in this book is synthetic; a placement is where you see how far a real utility's constraints differ from it. Notice how decisions are actually made, who owns operational risk and how long a simple change takes, because those observations will shape how you scope your capstone.

### 43.2 Placement agreement

Before starting, agree in writing: host supervisor and academic supervisor; scope of work; systems you may access and how; confidentiality and data handling; safety induction; what you may publish in your report; and how incidental findings are handled. You work under the host's authority and policies; your course gives you no authority to test or access anything.

The worked example's host approved the final report text before it left the organisation. Agreeing the publication rule in advance avoided any argument about what the report could include.

### 43.3 Reflective practice log

Keep a weekly log with four entries: **observation** (what you saw, without judgement), **connection** (which chapter's method it relates to), **difference** (where practice diverged from the method, and why it made sense locally), and **question** (what you would investigate). Reflection turns experience into transferable judgement. Do not record sensitive details in the log; record patterns.

In the worked example below, the student's observation about firmware versions follows exactly this pattern, and contains no device names. Weekly entries keep the habit.

### 43.4 Common placement work

Typical tasks for an engineering student: updating an asset inventory and reconciling it with network data (Chapter 22); drafting or reviewing a playbook (Chapter 37); supporting a risk assessment (Chapter 24); preparing a test procedure for a commissioning (Chapter 31); assessing advisories against the inventory (Chapter 12). Each produces a deliverable for the host and a sanitised learning artefact for the course.

The student in the worked example did the first task, reconciling an asset register with monitoring data. The student's deliverable to the host was a change to the work-order form.

### 43.5 Worked example: a sanitised placement report (synthetic)

A student placed with a (synthetic) regional electricity distributor writes a report section: "Observation: substation RTU firmware versions in the asset register differed from those observed in passive monitoring in 18% of a sample of 60 devices. Connection: Chapter 22's reconciliation of multiple inventory sources. Difference: the register is updated at annual maintenance visits, while firmware changes occur during unscheduled repairs; field staff had no simple way to report changes. Recommendation (accepted by host): add a firmware field to the repair work-order form and a quarterly reconciliation against monitoring data." No device names, addresses or locations appear; the host approved the text.

### 43.6 Practical activity

Draft a placement agreement for a hypothetical four-month placement at a water utility, covering all items in §43.2.

Use a water utility like LRWA as your mental model, but keep the agreement general enough for a real host to sign. Name both supervisors by role, list the systems you may see and how, and state plainly that you may not test or scan anything. Say how incidental findings are reported and who approves your report before it leaves the host. Add a safety induction date and the data you may take away, which should usually be none.

### 43.7 Common errors and limits

- Starting without a written scope and data-handling agreement.
- Treating placement access as permission to explore.
- Logs containing sensitive details.
- Reports that criticise the host without understanding local constraints.

The worked example avoids each: its scope was agreed, its log recorded patterns rather than device details, and its recommendation took account of why the register lagged behind repairs. Its criticism of the register was framed around a process gap, not around the field staff, and the host accepted the recommendation because it fitted the way repairs were actually done.

### Exercises — chapter 43

**EX085 — Placement agreement.** *Objective:* define placement boundaries. *Inputs:* §43.6. *Steps:* write the agreement. *Expected evidence:* one to two pages. *Rubric:* 3 = all §43.2 items, explicit prohibition on unscoped testing, incidental-finding route, publication approval; 2 = one missing; 1 = generic; 0 = none.

**EX086 — Reflective entry.** *Objective:* reflect usefully. *Inputs:* an observation: "operators kept a paper notebook of setpoint changes alongside the SCADA log". *Steps:* write a four-part log entry. *Expected evidence:* entry. *Rubric:* 3 = neutral observation, link to Chapters 13/37, local rationale (trust, outages, handover), investigative question; 2 = judgemental; 1 = observation only; 0 = none.

### Chapter synthesis

Practice teaches the constraints that shape real designs. Work within a written agreement and the host's authority, log observations, connections, differences and questions without sensitive detail, and deliver value to the host in a form that is safe to share.

<!-- cyberabc:chapter-navigation:start ch-43 -->
### Continue studying — chapter 43 of 50

[← Chapter 42](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 →](#ch-44)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes and connection

After this chapter you can (1) define a capstone project with a sponsor, scope, requirements and acceptance criteria; (2) plan it with a schedule, risk register and verification plan; (3) set up a reproducible engineering environment; and (4) pass a preliminary design review. The capstone integrates the course into one built and verified system and continues through Chapters 45–50.

### 44.1 What a capstone is

A capstone is a substantial engineering project in which the student designs, builds and verifies a system that meets real or realistic requirements under constraints. In this course the capstone must: address a critical-infrastructure security or resilience need; include a working artefact (software, configuration, testbed or prototype); include analysis (threat/failure, performance, reliability); and be verified against stated requirements. The capstone continues the TMRP case unless your supervisor approves another synthetic or authorised case.

The worked example below follows TMRP: restart-safe authenticated telemetry for the legacy RTUs at PS1 and PS2.

### 44.2 Scoping

A good capstone scope is narrow enough to finish and deep enough to require real engineering. Examples: an authenticated telemetry gateway with fault-injection verification; a residual-based detector with a validated simulation study; a recovery-orchestration tool with a measured restoration trial; a segmentation-verification tool with a policy model. Write a one-page scope: need, stakeholders, deliverables, out-of-scope items, constraints, and acceptance criteria.

The TMRP capstone scope in the worked example below fits on one page and leaves real RTU hardware and the carrier network out.

### 44.3 Planning

Plan with a work breakdown, schedule with milestones (preliminary design review, critical design review, verification complete, thesis draft, defense), risk register (technical, schedule, access, skills), and verification plan tracing requirements to tests. Keep a weekly log and update the risk register monthly.

For the TMRP capstone, the twelve-week schedule places the preliminary design review in the first weeks and the independent review before verification. Its risk register includes the chance that restart safety proves harder than expected, which, as the verification summary later shows, is what happened when the receiver accepted replays after a restart.

### 44.4 Environment

Set up version control, an issue tracker, a reproducible build (pinned dependencies or standard library only), automated tests, and a results directory where every result is stored with the commit, seeds and environment that produced it.

For the TMRP capstone, the gateway uses only the Python standard library, so there are no dependencies to pin, and every campaign result is stored with its seed and commit. That discipline is what lets the later dossier list a hash and version for each result.

### 44.5 Worked example: capstone scope (synthetic)

*Title:* Restart-safe authenticated telemetry for legacy RTUs. *Need:* N2/N3 of TMRP. *Deliverables:* gateway software (Python standard library), bench harness, fault-injection campaign, key-rotation procedure, thesis. *Out of scope:* real RTU hardware; carrier network. *Constraints:* 12 weeks; synthetic data. *Acceptance:* R1, R2 (including restarts), R7 verified on the bench; zero silent failures in a seeded campaign of 10,000 messages across seven fault classes; key rotation without loss of telemetry demonstrated.

Each acceptance criterion maps to a requirement or a demonstration, so the critical design review can check them one by one.

### 44.6 Practical activity

Write your capstone scope and plan, and hold a preliminary design review with your supervisor and one peer.

Base your scope on the one-page template: need, stakeholders, deliverables, items out of scope, constraints and acceptance criteria. Then prepare a short plan with milestones and a risk register. At the review, ask your supervisor and peer to challenge the acceptance criteria above all, because a criterion that cannot be tested will cause trouble at the critical design review. Record their findings and your responses.

### 44.7 Common errors and limits

- Scopes too broad ("secure the utility").
- No acceptance criteria.
- Verification planned last.
- Unreproducible environments.

The draft scope in EX087 shows the first two errors: securing water utilities with an AI system has no boundary and no acceptance criteria. The TMRP capstone scope avoids them by naming one gateway, three requirements and a measured campaign. Its verification plan was written with the scope, and its environment uses only the standard library with seeded runs, so every result can be reproduced. Its milestones are dated.

### Exercises — chapter 44

**EX087 — Scope critique.** *Objective:* tighten a scope. *Inputs:* draft scope "Build an AI system to protect water utilities from cyber attacks". *Steps:* list four problems and rewrite the scope in one page. *Expected evidence:* critique and rewrite. *Rubric:* 3 = problems (unbounded, no requirements, no data, no acceptance) and a feasible, verifiable rewrite; 2 = rewrite vague; 1 = critique only; 0 = none.

**EX088 — Risk register.** *Objective:* plan for project risks. *Inputs:* §44.5. *Steps:* write five project risks with likelihood, impact, mitigation and trigger. *Expected evidence:* table. *Rubric:* 3 = realistic risks (scope creep, restart-safety design harder than expected, bench fidelity, time, supervisor availability) with concrete triggers; 2 = no triggers; 1 = generic; 0 = none.

### Chapter synthesis

A capstone is a scoped, built and verified system. Define the need, deliverables, constraints and acceptance criteria; plan milestones, risks and verification from the start; and make the environment reproducible so that every result can be traced and re-run.

<!-- cyberabc:chapter-navigation:start ch-44 -->
### Continue studying — chapter 44 of 50

[← Chapter 43](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 →](#ch-45)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes and connection

After this chapter you can (1) conduct an independent technical review of another team's design using structured criteria; (2) write findings that are specific, evidenced and actionable; (3) classify findings by severity and recommend dispositions; and (4) receive a review of your own design and respond. It applies Fagan-style rigour (Chapter 14) to whole designs and prepares Capstone II.

### 45.1 Independence and purpose

An independent reviewer has not worked on the design and does not report to its authors. Independence catches errors that authors cannot see — shared assumptions, blind spots, wishful verification. The purpose is to improve the design and the decision about it, not to score points.

For TMRP, the reviewer of the capstone dossier is someone who did not work on the gateway and does not report to its authors. That independence is why the reviewer noticed that the assurance case cited T3 as passed while the matrix still recorded it as failed, an inconsistency the authors had read past many times.

### 45.2 Review criteria

Review against: requirements (complete, verifiable, traced); architecture (consequence-driven, failure and attack behaviour analysed); controls (specified with performance, independent layers); analyses (assumptions stated, numbers consistent); verification (plan covers requirements, failures handled honestly); operations (procedures, training, recovery); maintainability; and the assurance case (claims supported, defeaters stated).

Each criterion maps to a chapter of this book: requirements to Chapter 21, architecture to Chapter 26, controls to Chapter 27, verification to Chapters 30 and 40, operations to Chapter 37 and the assurance case to Chapter 35. Reviewers of the TMRP dossier used this list as their checklist.

### 45.3 Writing findings

A finding states: what was observed (with a reference to the document or evidence), why it matters (consequence), the criterion it fails, and a recommendation. Severity: **critical** (claim cannot be supported, or safety risk), **major** (significant gap needing change before approval), **minor** (improvement), **observation** (no change required). Avoid vague findings ("security seems weak") and design-by-reviewer (prescribing your favourite solution when several would do).

The TMRP findings in the worked example below follow this form. F4, on the battery fraction, is minor because the claim survives with a source added.

### 45.4 Responding to review

Authors respond to each finding: accept (with change), reject (with reasoning and evidence), or defer (with owner and date). The reviewer checks responses and closes or escalates findings. Disagreements that cannot be resolved go to the decision owner with both positions recorded.

For TMRP, the authors accepted F2 and added the stale-station alarm, and accepted F3 by reporting R6 as not met and costing options in ADR-015. Each response named an owner, and the reviewer checked the re-run campaign before closing F2.

### 45.5 Worked example: findings on the TMRP dossier (synthetic)

- **F1 (critical):** Assurance case sub-claim C2 cites T3 as passed, but the traceability matrix (Lab 14) records T3 failed and the v2 re-test is not recorded. *Recommendation:* record re-test evidence or downgrade the claim.
- **F2 (major):** Receiver does not alarm on missing data (Lab 15 drops silent); R7 cannot be claimed for loss-of-data events. *Recommendation:* add stale-station alarm and re-run campaign.
- **F3 (major):** Restoration trial (Chapter 47) shows 12 h against R6's 8 h; the dossier states R6 as met. *Recommendation:* report R6 as not met and present options.
- **F4 (minor):** Battery sizing uses 0.6 usable fraction without a source; cite the battery manufacturer's data.
- **F5 (observation):** The weighted concept evaluation (§25.4) is sensitive to operability weight; the decision is still defensible.

### 45.6 Practical activity

Exchange capstone dossiers with another student, review against §45.2 criteria, and write at least six findings with severities.

Choose a reviewer who has not helped with your design. For each finding, include the observation with its reference, the consequence, the criterion it fails and a recommendation. Use the four severity levels honestly. Then exchange roles and respond to the findings on your own dossier with accept, reject or defer, giving evidence for each rejection. Keep both logs for your dossier. Keep it to evidence.

### 45.7 Common errors and limits

- Reviews by people who helped design.
- Vague or unevidenced findings.
- Severity inflation or deflation.
- Authors rejecting findings without evidence.

The TMRP review avoided these: the reviewer was independent, each finding cited a document, severities matched consequences, and the authors' responses were backed by evidence and checked before closing. F5 was kept as an observation, not inflated. F1 was rated critical because the claim could not be supported as written, not because the error was embarrassing, and the authors did not reject any finding without evidence to support the rejection.

### Exercises — chapter 45

**EX089 — Rewrite weak findings.** *Objective:* write actionable findings. *Inputs:* "the key management is not great"; "testing seems incomplete"; "I would use OPC UA instead". *Steps:* rewrite each as a proper finding or explain why it should be withdrawn. *Expected evidence:* three rewrites. *Rubric:* 3 = specific observation, consequence, criterion, recommendation; third withdrawn or reframed to a requirement-based concern; 2 = one vague; 1 = rewording; 0 = none.

**EX090 — Respond to F2 and F3.** *Objective:* respond to review. *Inputs:* §45.5. *Steps:* write author responses to F2 and F3 with dispositions, changes, owners and dates. *Expected evidence:* two responses. *Rubric:* 3 = F2 accepted with design change and re-test, F3 accepted with honest reporting and options (parallelise recovery, pre-built images, revise requirement with stakeholder agreement); 2 = defensive; 1 = rejects; 0 = none.

### Chapter synthesis

Independent review finds what authors cannot see. Review against explicit criteria, write specific, evidenced, actionable findings with honest severities, and respond to each finding with accept, reject or defer — recorded and checked.

<!-- cyberabc:chapter-navigation:start ch-45 -->
### Continue studying — chapter 45 of 50

[← Chapter 44](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 →](#ch-46)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes and connection

After this chapter you can (1) complete implementation of the capstone artefact; (2) execute the full verification plan and record results; (3) close review findings; and (4) pass a critical design review with evidence. It continues Chapter 44 after the independent review and prepares the failure and recovery trial (Chapter 47).

### 46.1 Finishing the build

Freeze scope: new features now threaten verification. Close the review findings that require design changes first. Keep the main branch always passing its tests; tag the version that enters final verification.

For the TMRP capstone, scope was frozen after the independent review. F2's stale-station alarm was the design change made before the tagged version entered final verification; every later idea went to a list for future work. The restart fix came later, as a correction found by verification itself, which is the only kind of change allowed after a freeze. The main branch stayed green.

### 46.2 Executing verification

Run the full verification plan against the tagged version: unit, integration, property-based and fault-injection tests (Chapters 30 and 40). Record each result with version, seed and environment. For any failure: record, analyse, fix, re-run, record again. Do not overwrite earlier results; history is evidence.

For the TMRP capstone, the receiver's failure to reject replays after a restart was recorded, fixed by persisting the last counter per station, and re-tested, with both results kept. The tagged version was the one tested. Its seed was recorded.

### 46.3 Critical design review

At the critical design review the panel checks: requirements met with evidence; review findings closed or dispositioned; residual risks stated and owned; operations and maintenance prepared; and readiness for the trial. Bring the traceability matrix, verification results, finding log and assurance case.

For TMRP, the panel saw the verification summary below. It includes the restart failure and its fix, the stale-station alarm added after F2 and the key rotation demonstration. With F1 to F3 closed or dispositioned and R6 reported honestly, the panel could make an explicit readiness decision for the trial instead of an assumption.

### 46.4 Worked example: capstone verification summary (synthetic)

| Requirement | Tests | Result | Notes |
|---|---|---|---|
| R1 | T1, T2, campaign (corrupt class) | Pass | 0 silent failures in 10,000 messages |
| R2 | T2, restart tests (both sides), campaign (replay, reorder, restart) | Pass after fix | Receiver restart initially accepted replays; fixed by persisting last counter per station; re-tested |
| R7 | T5, stale-station alarm test | Pass after fix | Drop detection added after F2 |
| Key rotation | Demonstration | Pass | Overlap window of 10 min with both keys accepted, then old key revoked |

The restart failure was found by the extended fault model of EX080 — a direct return on the verification laboratory's investment.

### 46.5 Practical activity

Run your full verification plan and produce the summary table with links to raw results.

For each requirement, give the tests, the result and any fix, as in the TMRP summary. Keep the failed results with their dates and the fixes that followed, and link each line to the raw result files with their seeds and versions. If a test was not run, say so in the table rather than leaving it blank. The table should let a reviewer trace any claim to a file in one step.

### 46.6 Common errors and limits

- Adding features during verification.
- Overwriting failed results with later passes.
- Entering critical design review with open critical findings.

The TMRP capstone avoided these by freezing scope after review, keeping the restart failure in the record beside its later pass, and closing F1 to F3 before the critical design review. Failed results stayed in the record with the fixes that followed, so reviewers could see how each pass was earned. No feature was added during verification. Open findings were closed first.

### Exercises — chapter 46

**EX091 — Rotation design.** *Objective:* design key rotation without loss. *Inputs:* §46.4. *Steps:* describe the rotation protocol step by step, including how the receiver knows which key to try, the overlap window, failure handling and revocation. *Expected evidence:* procedure. *Rubric:* 3 = key ID in authenticated header, receiver accepts both keys during window, counters continue, rollback if new key fails, old key revoked and destroyed; 2 = no key ID; 1 = "change the key"; 0 = none.

**EX092 — Readiness decision.** *Objective:* judge readiness. *Inputs:* all requirements pass except a minor finding on documentation and an open major finding that the stale-station alarm threshold (60 s) produces two false alarms a day during LTE congestion. *Steps:* recommend go / go with conditions / no-go for the trial, with reasoning. *Expected evidence:* recommendation. *Rubric:* 3 = go with conditions (threshold tuning study during trial, operators briefed), reasoning about consequence of false alarms vs missed loss of data; 2 = no conditions; 1 = unreasoned; 0 = none.

### Chapter synthesis

Freeze scope, close findings, verify the tagged version completely and keep failure history as evidence. Enter the critical design review with traceability, results, findings and the assurance case, and leave it with an explicit readiness decision.

<!-- cyberabc:chapter-navigation:start ch-46 -->
### Continue studying — chapter 46 of 50

[← Chapter 45](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 →](#ch-47)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes and connection

After this chapter you can (1) design a controlled failure and recovery trial with safety boundaries; (2) compute critical paths and compare planned and measured recovery times; (3) observe and record human and technical performance during the trial; and (4) turn trial results into requirement status and design changes. It validates recovery requirements (R6) and prepares the evidence dossier (Chapter 48).

### 47.1 Why trial recovery

Recovery capability that has not been exercised is a hope. Backups that have not been restored may be incomplete; procedures that have not been followed may be wrong; times that have not been measured are guesses. [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) covers contingency planning, including testing, training and exercises.

TMRP's own trial showed why: the eight-hour restoration target in R6 looked reasonable until the critical path was measured. Measuring it was the point.

### 47.2 Designing the trial

Define the scenario (e.g., SCADA servers declared compromised at 02:00), the objectives (restore remote operation from offline backups; maintain supply in local mode throughout), the safety boundaries (trial on the test environment or a planned window with local operation staffed; abort criteria), the observers and the measurements (time of each task, deviations from procedure, decisions).

TMRP's trial used the scenario of SCADA servers declared compromised, with supply maintained in local mode throughout. Observers recorded each task's time and every deviation from the procedure.

### 47.3 Critical path

Recovery tasks have durations and dependencies. The **critical path** is the longest chain of dependent tasks; it sets the minimum recovery time. Tasks off the critical path have **slack**. Shortening recovery means shortening critical-path tasks or breaking dependencies — not speeding up tasks with slack.

In TMRP's trial, re-keying the RTUs had six hours of slack. Speeding it up would have changed nothing. Only imaging, rebuild and configuration restore set the twelve-hour result, which is why every option for meeting R6 targets one of those three tasks, such as pre-built standby images or imaging on spare hardware.

### 47.4 Worked example: TMRP recovery trial (synthetic)

The trial plan (Lab 17): isolate (1 h); manual operations established (1 h); forensic imaging of the SCADA servers (3 h); rebuild SCADA from offline media (4 h); restore configuration (2 h); re-key RTUs (3 h, in parallel); verify setpoints (1 h); resume remote control (1 h). The critical path runs through forensic imaging, rebuild and configuration restore: remote control returns at 12 h, against R6's 8 h. Re-keying has 6 h of slack — speeding it up achieves nothing. Options to meet 8 h: pre-built standby SCADA images (rebuild 4 h → 1 h); imaging in parallel with rebuild on spare hardware (removes 3 h from the path); or agreement with stakeholders that R6 be 12 h because supply is maintained in local mode throughout. The trial also measured that manual operations were established in 50 minutes, meeting the 1 h requirement.

### 47.5 Practical activity: Lab 17

```python
# Lab 17 - recovery critical path versus the restoration target (synthetic TMRP trial plan, offline)
T = {  # task: (hours, prerequisites)
    "isolate": (1, []), "manual_ops": (1, ["isolate"]), "forensic_image": (3, ["isolate"]),
    "rebuild_scada": (4, ["forensic_image"]), "restore_config": (2, ["rebuild_scada"]),
    "rekey_rtus": (3, ["isolate"]), "verify_setpoints": (1, ["restore_config", "rekey_rtus"]),
    "resume_remote": (1, ["verify_setpoints"])}
ef, prev = {}, {}
def finish(t):
    if t not in ef:
        d, ps = T[t]; start = max((finish(p) for p in ps), default=0)
        prev[t] = max(ps, key=finish) if ps else None; ef[t] = start + d
    return ef[t]
end = finish("resume_remote"); path, n = [], "resume_remote"
while n: path.append(n); n = prev[n]
print("restore remote control at", end, "h; critical path:", " -> ".join(reversed(path)))
print("slack of rekey_rtus:", finish("restore_config") - finish("rekey_rtus"), "h; target 8 h met:", end <= 8)
```

Expected output:

```text
restore remote control at 12 h; critical path: isolate -> forensic_image -> rebuild_scada -> restore_config -> verify_setpoints -> resume_remote
slack of rekey_rtus: 6 h; target 8 h met: False
```

The output confirms the worked example: remote control returns after twelve hours because imaging, rebuild and configuration restore run in series, and re-keying finishes six hours before it is needed. Change the plan as EX093 asks and watch the critical path move to a different chain. The lab does not include manual operations on the path to remote control, because they run in parallel; the trial measured them separately at fifty minutes against the one-hour requirement. Keep both outputs.

### 47.6 Common errors and limits

- Recovery tested only on paper.
- Trials without abort criteria or safety staffing.
- Improving tasks that have slack.
- Trial results reported as passes when the requirement was missed.
- Forensic preservation skipped to save time without a decision.

TMRP's trial avoided the fourth error by reporting R6 as not met at twelve hours, and it kept forensic imaging rather than skipping it without a decision. Abort criteria and local staffing were set before the trial began, and the options for meeting R6 target only critical-path tasks.

### Exercises — chapter 47

**EX093 — Shorten the path.** *Objective:* use the critical path. *Inputs:* Lab 17. *Steps:* (1) make `rebuild_scada` depend only on `isolate` (spare hardware, imaging in parallel) and recompute; (2) additionally reduce `rebuild_scada` to 1 h (standby image) and recompute; report the new critical path each time. *Expected evidence:* outputs. *Rubric:* 3 = correct results (run code) and the observation that the critical path moves to another chain; 2 = numbers right, path not discussed; 1 = not run; 0 = none.

**EX094 — Forensics vs speed.** *Objective:* make a documented trade-off. *Inputs:* skipping forensic imaging shortens recovery. *Steps:* write a decision note for the operations director: options, consequences for investigation, legal/regulatory and future prevention, recommendation. *Expected evidence:* one page. *Rubric:* 3 = parallel imaging on spare hardware as preferred, risks of losing evidence explained, decision owner; 2 = recommends skipping without consequences; 1 = vague; 0 = none.

### Chapter synthesis

Recovery must be trialled to be trusted. Design trials with safety boundaries and measurements, find the critical path, improve only what is on it, and report the requirement status the trial actually shows — then change the design or the requirement with stakeholders.

<!-- cyberabc:chapter-navigation:start ch-47 -->
### Continue studying — chapter 47 of 50

[← Chapter 46](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 →](#ch-48)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes and connection

After this chapter you can (1) assemble an engineering evidence dossier that supports the capstone's claims; (2) organise evidence by claim with provenance; (3) protect sensitive evidence while keeping it reviewable; and (4) check the dossier for consistency before submission. It gathers Chapters 44–47 and prepares the engineering thesis.

### 48.1 What the dossier is

The evidence dossier is the collection of artefacts that supports the assurance case: requirements and traceability; design documents and decision records; analyses (threat models, fault trees, performance, reliability); implementation records (source revision, SBOM, build provenance); verification and validation results; review findings and responses; trial reports; operational documents; and the residual-risk register with owners. Organise it by claim, not by date: a reviewer should be able to start from a claim and find its evidence in two clicks.

For TMRP, the dossier's claims are C1 to C4.

### 48.2 Provenance

Every piece of evidence states what it is, who produced it, when, from which version of the system and with which tools. Numbers in the thesis must trace to a result file (compare the master's provenance check in its Chapter 7). Use content hashes for result files and record them in an index, as Chapter 13's hash chain does for logs.

For TMRP, each entry in the dossier index carries a version, such as the gateway release or the trial date, and the first characters of its hash.

### 48.3 Sensitivity

Dossiers about infrastructure contain sensitive details. Keep a full restricted version for authorised reviewers and a redacted version for wider audiences, and record what was redacted and why. For coursework with synthetic cases, sensitivity is lower — but practise the discipline.

For TMRP, the restricted version would include gateway configurations and key-management procedures, while the redacted version describes the architecture at the level of zones and conduits. The redaction record lists each removed item and the reason, so a reviewer of the redacted version knows what was withheld and can ask for access through the proper route.

### 48.4 Consistency check

Before submission: every claim has evidence; every number in the thesis matches its source; statuses agree across documents (no "passed" in one and "failed" in another — finding F1 in Chapter 45); residual risks have owners; and all review findings are closed or dispositioned.

TMRP's dossier failed this check once, when C2 cited T3 as passed while the matrix still showed it failed. The fix was to record the v2 re-test as T3b and update every document that referred to it, so the index now shows the same status everywhere.

### 48.5 Worked example: dossier index excerpt (synthetic)

| Claim | Evidence | Version | Hash (first 12) | Status |
|---|---|---|---|---|
| C1 R1 met | T1/T2 results; campaign 10k messages | gw v1.3.0 | 3f9a1c0b7e22 | Pass |
| C2 forged commands cannot cause supply loss | Lab 9 conditioning; T3b; key mgmt review | risk reg v1.2 | 8b01d4e6aa90 | Supported with defeaters D1, D2 |
| C3 R6 restore ≤ 8 h | Recovery trial report | trial 2026-09-14 | c47e2b19f5d3 | **Not met (12 h)**; options in ADR-015 |
| C4 R5 24 h battery | Sizing analysis; T4 discharge test | cab v2 | 51d7a0e8c4f6 | Pass |

(The hashes are illustrative placeholders for the synthetic case.)

### 48.6 Practical activity

Build your dossier index with real content hashes of your result files (`hashlib.sha256`) and run the §48.4 consistency check.

Use the script from EX095 to compute the hashes, and store the index under version control so its history is part of the evidence. Then run the consistency check against your thesis draft. Every number in the draft should appear in a result file listed in the index, and every status should match. Fix any mismatch in the source document first, then regenerate the index.

### 48.7 Common errors and limits

- Dossiers organised by date or author instead of claim.
- Numbers in the thesis with no source file.
- Status inconsistencies across documents.
- Redaction without a record.

The TMRP index avoids the first error by organising evidence by claim, and its record of C3 as not met keeps the third from appearing. A redaction record accompanies the shared version. Every number in the thesis traces to a result file listed in the index, and the shared version carries a record of what was redacted and why.

### Exercises — chapter 48

**EX095 — Index script.** *Objective:* automate provenance. *Inputs:* a results folder. *Steps:* write a stdlib script that walks the folder, computes SHA-256 of each file, and writes a CSV index with path, size, hash and modification time; explain why modification time is weak evidence. *Expected evidence:* script and explanation. *Rubric:* 3 = working script, explanation (mtime is easily changed; hash plus version control commit is stronger); 2 = no explanation; 1 = not working; 0 = none.

**EX096 — Consistency audit.** *Objective:* catch inconsistencies. *Inputs:* the §48.5 excerpt and an abstract sentence "All requirements were verified and the system restores remote operation within 8 hours". *Steps:* identify the inconsistency and rewrite the sentence. *Expected evidence:* rewrite. *Rubric:* 3 = identifies C3 contradiction, rewrite accurate and still positive where justified; 2 = vague rewrite; 1 = misses it; 0 = none.

### Chapter synthesis

The dossier is the claim-organised, provenance-tracked body of evidence behind the assurance case. Keep restricted and redacted versions with a redaction record, and check consistency of every claim, number and status before anyone else does.

<!-- cyberabc:chapter-navigation:start ch-48 -->
### Continue studying — chapter 48 of 50

[← Chapter 47](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 →](#ch-49)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes and connection

After this chapter you can (1) structure an engineering thesis around a design problem, solution and evidence; (2) write results and limitations that stay within the evidence; (3) present quantitative results with uncertainty and provenance; and (4) prepare a thesis that an examiner can verify. It turns the dossier into a document and prepares the defense.

### 49.1 The engineering thesis

An engineering thesis argues that a designed system meets a need under constraints, supported by verification and validation evidence. It is not a research dissertation (the [master's book](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) covers that) and need not claim an original contribution to knowledge (the [doctoral book](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md)). Its originality, if any, lies in the design and the quality of its evidence.

For TMRP, the thesis argues that the restart-safe gateway meets R1, R2 and R7 on the bench and reports R6 as not met.

### 49.2 Structure

1. **Introduction:** need, stakeholders, consequence, scope.
2. **Background:** sector context, relevant standards and prior designs, with sources.
3. **Requirements:** derived requirements with sources and verification methods.
4. **Design:** alternatives, selection, architecture, controls, with decision records.
5. **Analysis:** threat and failure analysis, performance, reliability.
6. **Implementation:** what was built, how, with which tools.
7. **Verification and validation:** methods, results, failures and fixes.
8. **Discussion:** requirement status, residual risks, limitations, what you would do differently.
9. **Conclusion:** what was achieved and what remains.
Appendices: traceability matrix, dossier index, lab code.

The TMRP thesis follows this structure.

### 49.3 Results and limitations

Report requirement status honestly: met, met after fix, not met, not verified. For each limitation, say which claims it affects and in which direction: "the bench uses perfect clocks; real clock drift would increase stale-message rejections, so the false-stale rate reported is a lower bound". A limitation without a direction is decoration.

The TMRP discussion paragraph in the worked example below gives such a limitation: the bench used a synthetic network, so the sixty-second stale-station threshold must be re-tuned on site, where LTE congestion may raise false alarms. That sentence names the affected claim and the likely direction.

### 49.4 Writing well

Lead each chapter with its main point. Use figures with labelled axes and units; tables for exact values. Keep numbers traceable to the dossier. Write in plain technical English, define terms at first use, and use a glossary.

For TMRP, the requirement-status table appears early in the discussion, and every number in it traces to an entry in the dossier index with its hash. Each chapter opens with its main point, and terms such as stale-station alarm are defined at first use and in the glossary, so an examiner can read any chapter without hunting for definitions.

### 49.5 Worked example: discussion paragraph (synthetic)

> The gateway met R1 and R2 on the bench, including restarts of either end, after the receiver was changed to persist its last accepted counter (Section 7.3). R7 was met for priority alarms and, after review finding F2, for loss of data. R6 was not met: the recovery trial restored remote operation in 12 h against an 8 h requirement, because forensic imaging and rebuild lie in series on the critical path. Hospital supply was maintained in local mode throughout the trial, so the consequence of the shortfall is reduced visibility and intervention capability, not loss of supply. Two design options that would meet 8 h are costed in ADR-015. All results come from a synthetic bench; field performance, particularly LTE latency under congestion, may differ, and the 60 s stale-station threshold must be re-tuned on site.

### 49.6 Practical activity

Write the discussion chapter of your thesis, with a requirement-status table and directional limitations.

Use the TMRP discussion paragraph as your model. Begin with a table that gives each requirement's status as met, met after fix, not met or not verified. Then write one paragraph per significant result, including any requirement you did not meet, and end with your limitations, each naming the claim it affects and the direction of likely bias. Check every number against your dossier index before submitting.

### 49.7 Common errors and limits

- Theses organised as diaries.
- Requirement status rounded up.
- Limitations without direction or affected claims.
- Numbers that do not match the dossier.

The TMRP thesis avoids each: it is organised by argument, reports R6 as not met, gives directional limitations, and draws its numbers from the dossier index. Its requirement-status table is checked against the dossier before submission, so nothing is rounded up. Its limitations name the synthetic bench and the single recovery trial, and say in which direction each might bias the results.

### Exercises — chapter 49

**EX097 — Directional limitations.** *Objective:* write useful limitations. *Inputs:* three limitations: synthetic noise model; bench without real LTE; one recovery trial. *Steps:* for each, state the affected claim and direction of likely bias. *Expected evidence:* three sentences. *Rubric:* 3 = each has claim and direction (e.g., one trial gives no variability estimate — 12 h could be optimistic or pessimistic; real LTE latency would increase stale rejections and alarm latency); 2 = one missing direction; 1 = list only; 0 = none.

**EX098 — Abstract.** *Objective:* summarise accurately. *Inputs:* §49.5. *Steps:* write a 150-word structured abstract (need, design, methods, results, limitations). *Expected evidence:* abstract. *Rubric:* 3 = accurate including R6 not met, synthetic-bench limit stated; 2 = one overstatement; 1 = vague; 0 = none.

### Chapter synthesis

An engineering thesis argues from need to design to evidence. Structure it for an examiner, report requirement status as it is, give every limitation an affected claim and direction, and keep every number traceable to the dossier.

<!-- cyberabc:chapter-navigation:start ch-49 -->
### Continue studying — chapter 49 of 50

[← Chapter 48](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 →](#ch-50)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes and connection

After this chapter you can (1) prepare a technical defense presentation of a capstone and thesis; (2) anticipate examiner questions by family and prepare evidence-based answers; (3) handle questions you cannot answer honestly; and (4) plan corrections and handover after the defense. It closes the course.

### 50.1 What examiners test

Examiners check that the candidate understands the need and constraints; made defensible design decisions; verified claims competently; knows the limits of the evidence; and can reason about changes ("what if the requirement were 2 h?"). They read the thesis closely and probe inconsistencies.

For the TMRP defense, examiners are likely to probe the R6 shortfall and the accepted residual risk D1. They may ask what would change if the hospital buffer were two hours instead of four, and the candidate should reason from the fault tree and the local automatic mode rather than guess.

### 50.2 The presentation

Twenty minutes: need and consequence (2 min); requirements (2); alternatives and selection (3); architecture and key controls (4); verification and validation results with failures and fixes (5); requirement status and residual risks (2); limitations and next steps (2). One message per slide. Show the requirement-status table; examiners respect "not met" stated plainly.

For TMRP, the requirement-status table would show R1, R2 and R7 as met after fixes and R6 as not met at twelve hours, with the options in ADR-015. That slide prepares the panel for the questions in the worked example, and stating the shortfall before an examiner finds it earns more trust than any polished result.

### 50.3 Question families

- **Need:** why does this matter, to whom, how do you know?
- **Design:** why this and not that alternative; what would change your choice?
- **Analysis:** where does this number come from; what if this assumption is wrong?
- **Verification:** how do you know the test tests the requirement; what did your tests miss?
- **Limits:** what can you not claim; what would a field deployment reveal?
- **Ethics and safety:** what could go wrong for people; who owns the residual risk?

Prepare two answers per family with references to the dossier.

### 50.4 Honest answers

When you do not know: say so, say how you would find out, and — if you can — reason toward an answer aloud, labelled as reasoning. Do not invent numbers. When an examiner finds an error: acknowledge, assess its impact on the claims, and propose a correction.

In the worked example, the candidate does this when asked about residual risk D1: the candidate states who accepted it, the evidence that bounds it and the alternative that would remove it, without pretending the risk is negligible. No number is invented.

### 50.5 After the defense

Corrections are listed in a table: examiner request, change made, location. Hand over the artefact and dossier to the sponsor with known limitations and maintenance needs. For real projects, route any security findings through the owner's processes.

For TMRP, the handover goes to LRWA's operations director with the dossier, the open item on R6 and the note that the stale-station threshold needs re-tuning on site. Any security finding about real equipment would go through LRWA's own processes, not the thesis.

### 50.6 Worked example: answering a hard question (synthetic)

*Examiner:* "Your assurance case accepts residual risk D1 — a compromised SCADA centre issuing authentic commands. Why is that acceptable for a hospital supply?" *Candidate:* "It is accepted by the operations director, not by me, and the case states why: local bounds (R3) keep any accepted setpoint within safe limits, so the worst a compromised centre can do at PS4 is stop the pumps, and the fault tree shows that losing supply then also needs the reservoir path and the hospital tank to fail. If the examiners consider that insufficient, the alternative in ADR-012 — local-only setpoint writes at PS4 — removes remote control at that site for an estimated staffing cost of one call-out per month. I would not claim D1 is negligible; I claim it is bounded and owned."

### 50.7 Practical activity

Hold a mock defense with two peers acting as examiners using the question families; record questions you could not answer and prepare answers.

Ask your examiners to use every question family and to probe at least one number in your thesis. Record each question you could not answer, then trace the answer to your dossier afterwards. For TMRP, the hardest questions concern the R6 shortfall and residual risk D1; prepare those answers until you can give them briefly, with the evidence named, and without claiming more than the dossier supports.

### 50.8 Common errors and limits

- Presentations that hide failures.
- Defensive answers to error findings.
- Invented numbers under pressure.
- No correction plan.

The TMRP candidate avoids these by showing the R6 shortfall on a slide, acknowledging errors plainly, refusing to invent numbers and keeping a corrections table ready for the examiners' requests. Failures such as the restart replay are presented as findings that verification caught, with the fix and the re-test, which is exactly what examiners want to see. A corrections table is ready. Every claim stays within the dossier.

### Exercises — chapter 50

**EX099 — Question bank.** *Objective:* anticipate examination. *Inputs:* your thesis or the TMRP case. *Steps:* write twelve questions (two per family) and short evidence-based answers with dossier references. *Expected evidence:* bank. *Rubric:* 3 = hard, specific questions with honest answers including limits; 2 = soft questions; 1 = answers without evidence; 0 = none.

**EX100 — Corrections table.** *Objective:* plan corrections. *Inputs:* examiner requests: (1) report the variability of recovery time; (2) justify the 0.6 usable battery fraction; (3) remove the claim that the detector "prevents" attacks. *Steps:* write a corrections table with change, location and how each is evidenced. *Expected evidence:* table. *Rubric:* 3 = (1) acknowledges single trial and adds plan or repeated simulated runs, (2) adds manufacturer source or sensitivity, (3) rewording to "detects"; 2 = one weak; 1 = no locations; 0 = none.

### Chapter synthesis

The defense tests understanding, judgement and honesty about limits. Present need, design, evidence and status plainly; prepare by question family with dossier references; answer what you know, reason transparently about what you do not, and turn examiner findings into a precise corrections table and a responsible handover.

<!-- cyberabc:chapter-navigation:start ch-50 -->
### Continue studying — chapter 50 of 50

[← Chapter 49](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

Each result shows one defensible answer. Numerical results were produced by running the labs and the short scripts described, with Python 3 and the seeds given; your last digits may differ if you change the order of random draws. For design exercises, the rubric in the chapter matters more than matching the wording below.

### Chapter 1

**EX001.** $d'(t) = 60\cdot\frac{2\pi}{24}\cos(2\pi t/24) \approx 15.71\cos(2\pi t/24)$ m³/h². Maximum 15.71 m³/h² at $t = 0$ (06:00) and again every 24 h. Because 15.71 > 12, the pumps cannot follow demand everywhere: $d'(t) > 12$ when $|t| < 2.68$ h, i.e., roughly 03:20–08:40 each day. Storage must cover the shortfall during the morning ramp, which is one reason reservoirs exist.

**EX002.** Outage at 06:00: 14.62 h. Outage at 18:00: 18.62 h. Mean-demand estimate: 17.33 h. The emergency plan should quote the worst credible start time (≈ 14.6 h, or less if a lower initial level is credible), because the plan must work whenever the outage begins; the mean-demand figure is neither worst-case nor typical.

### Chapter 2

**EX003.** $\neg\text{RUN} = H \vee S \vee (\neg P \wedge \neg M)$. A forged permit changes the outcome only in states with $H = 0$, $S = 0$, $M = 0$ (where RUN would otherwise be false): one state out of 16. A proposal: require for remote start both $P$ and a second condition that does not travel the same network path — for example, a local "remote enabled" key-switch $K$: $\text{RUN} = \neg H \wedge \neg S \wedge ((P \wedge K) \vee M)$. The key-switch is set by site staff for planned remote operation.

**EX004.** With RTU4 moved to `sat` only (and `sat` depending on nothing), loss of `grid_f1` impacts `fenwick_wtw, hollin_res, hospital_supply, lte, ps3, ps3_feed, rtu3` — `ps4` and `rtu4` survive. But the lab's graph still marks `hospital_supply` impacted, because its edges are AND-dependencies: supply "needs" both the reservoir and PS4. The real logic is OR (either path suffices), which this simple graph cannot express — Chapter 22 adds AND/OR types. A better modelling of the task (RTU4 needs LTE *or* satellite) also needs OR semantics. Honest answer: the hospital likely survives loss of F1 via PS4, but this model cannot show it.

### Chapter 3

**EX005.** Daily energy: 26 W × 24 h + 15 W × 10 h = 774 Wh at the load. Divide by efficiency 0.85, usable fraction 0.6 and end-of-life factor 0.8: 774 / (0.85 × 0.6 × 0.8) ≈ 1,897 Wh nominal, ≈ 79 Ah at 24 V. A standard 80 Ah or larger bank is needed; the 65 Ah bank from §3.5 no longer meets R5 in winter.

**EX006.** Model reply: "LTE encryption protects confidentiality and, depending on configuration, integrity of traffic over the radio segment; it does nothing for availability. A jammer or a carrier outage reduces signal-to-noise below what the link needs, and no key prevents that. Encryption also ends at the carrier, so it does not authenticate our RTUs to our SCADA end-to-end. For availability: (1) design sites to run in local automatic mode for 72 h without telemetry and alarm loss of link at SCADA within 60 s; (2) provide a diverse path (second carrier with different towers and power, or satellite) for the most critical sites; (3) monitor link quality to distinguish jamming from outage."

### Chapter 4

**EX007.** `01 06 00 01 00 03` → CRC bytes `98 0B` (frame `01 06 00 01 00 03 98 0b`). Changing the last data byte to `02` gives `59 CB`. An attacker on the serial line computes the CRC of a forged frame exactly as the legitimate master does, because the algorithm has no secret; the CRC only detects accidental corruption.

**EX008.** Move `len(resp) < 5` and a full-length check (`len(resp) == 5 + 2*count` for normal responses, 5 for exceptions) before the CRC; then CRC; then `if resp[0] == 0: return "reject: broadcast"` and unit check; then function/byte-count; then range. Tests: truncated frame → "reject: shape"; frame with unit 0 and valid CRC → "reject: broadcast". All original cases keep a rejection. (Broadcast requests receive no response under Modbus; a response from unit 0 is malformed.)

### Chapter 5

**EX009.** Example: "R10 — The system shall maintain treated-water supply to St Brenna's within contract pressure during loss of any single pumping station for at least 24 h (analysis + trial)." "R7 — Priority alarms shall be displayed on operator screens within 60 s of the field event for 99% of events over a 30-day measurement (test)." "R8 — Security logs shall be forwarded off-host within 5 min and integrity-protected with daily anchors stored outside the control zone; modification of any stored record shall be detectable (test)."

**EX010.** Operator: "PS4 telemetry may go dark after about 6 h of mains loss. If PS4 telemetry is lost during a power cut, dispatch the duty technician to read local gauges at the 4 h mark." Manager: "PS4's telemetry battery lasts about 6 h at end of life against a 24 h requirement (R5). During a long outage we would lose visibility — not supply — at the hospital feed. Options: replace with an 80 Ah bank (≈ cost of one site visit plus hardware, two weeks), or add a small generator inlet; interim: technician dispatch rule." Regulator: "Gap: R5 (24 h telemetry hold-up) not met at PS4 (measured 6 h at end of life). Compensating procedure in place since [date]; remediation by [date]."

### Chapter 6

**EX011.** At $k = 0.12$ h⁻¹: window = ln 4 / 0.12 ≈ 11.6 h. With 4 h for manual restoration, the alarm must arrive within ≈ 7.6 h; with a safety margin, specify much less. Requirement: "Loss of chlorine dosing shall be alarmed to the control room within 30 min, detected by an analyser and logger independent of the dosing controller." 30 min leaves a large margin under worst-case warm-weather decay.

**EX012.** Exact: 0.6065, 0.3679, 0.2231, 0.1353, 0.0821 at t = 1…5. Euler h = 1: 0.5, 0.25, 0.125, 0.0625, 0.0312 (stable, underestimates). h = 3 (factor −0.5): −0.5, 0.25, −0.125, 0.0625, −0.0312 — oscillates in sign, physically meaningless though decaying. h = 5 (factor −1.5): −1.5, 2.25, −3.375, 5.06, −7.59 — unstable. Forward Euler on $x' = -kx$ multiplies by $(1 - kh)$ each step; $|1 - kh| > 1$ when $h > 2/k = 4$.

### Chapter 7

**EX013.** PPV: 0.009 (prior 0.0001), 0.087 (0.001), 0.490 (0.01); with prior 0.001 and FPR 0.001: 0.487. Reducing the false-positive rate tenfold improves predictive value about as much as a tenfold rise in prevalence; at low base rates, FPR is the parameter worth improving.

**EX014.** Unavailability: β = 0 → 0.0004; β = 0.05 → 0.00136; β = 0.2 → 0.00426. Shared causes: site power and battery; antenna mast or cabinet; same modem model and firmware; shared backhaul or roaming arrangements between carriers; same SIM provisioning platform.

### Chapter 8

**EX015.** Worst case: the low-suction signal appears just after an input read, so it is first seen at the next scan (up to 45 ms later); confirmation requires a second consecutive scan (45 ms); the output is written at the end of that scan. Worst case ≈ 45 + 45 + 45 = 135 ms (plus output module delay), which violates 100 ms. Fix: reduce worst-case scan, debounce with a timer in a faster task, or use a hard-wired trip.

**EX016.** Secure boot prevents: (1) persistent installation of unsigned or modified firmware; (2) booting a downgraded image if anti-rollback is enforced. It does not prevent: (1) exploitation of a vulnerability in signed firmware at runtime → patching, input validation, network restriction; (2) malicious but legitimate logic changes via the engineering interface → authenticated, role-based programming with change detection and logging.

### Chapter 9

**EX017.** 5 states × 7 events = 35 pairs. Listed: stopped+start, starting+run_confirmed, starting+timeout, running+stop, stopping+stop_confirmed, tripped+reset (6), plus `trip` from all 5 states (5) = 11. Unlisted: 24. Examples with rationale: tripped+start (restart into the fault — must require local reset); stopped+run_confirmed (a spurious or forged confirmation must not create a "running" belief); running+reset (reset must not clear a non-existent trip and mask state).

**EX018.** Invariant: for each station, `last[st]` never decreases and equals the highest accepted counter. Sequence 1, 2, 2, 1, 5 → accept, accept, reject (replay), reject (replay), accept; final `last[3] == 5`. After a receiver restart, `last` is empty, so previously seen messages are accepted again unless the receiver persists `last` or keys are rotated on restart.

### Chapter 10

**EX019.** Hazard: an operator locked out during an emergency cannot act; an attacker can deliberately lock out operators (denial of service). Alternative: no lockout on control-room HMIs; instead progressive delay after failures, alerting on repeated failures, named accounts with strong authentication, physical access control to the control room, and an emergency override with physical presence and logging. Verify by test (failed attempts produce delays and alerts, never lockout) and by exercise (operator can log in under stress).

**EX020.** Do not visit, probe or try to log in to the page, and do not share the screenshot. Notify the utility privately through its published security contact, or if none exists, through a coordinated disclosure programme such as CISA's, stating only what you observed and where. Coursework may describe the pattern ("management interfaces exposed in procurement documents") without naming the utility, vendor, model or location.

### Chapter 11

**EX021.** The new flow field → enterprise TCP/445 is a VIOLATION. Model the jump host: add rule ("control", "field", "tcp", 22); then eng `10.5.0.12` → jump host `10.1.0.20` TCP/22 allowed; jump host → RTU `10.2.0.33` TCP/22 allowed; direct eng → RTU TCP/22 remains a VIOLATION. No rule gives the engineering zone direct access to the field.

**EX022.** Typical: 120 + 180 + up to 1,300 + 200 ≈ 1.8 s if an event just misses its poll (≈ 1.15 s on average with a half-cycle wait). Worst: 120 + 900 + 1,300 + 200 ≈ 2.5 s. The 95% within 1.5 s clause is at risk because the polling wait dominates; the 5 s clause is met. Change: report-by-exception (unsolicited responses) for alarms so they do not wait for the poll.

### Chapter 12

**EX023.** U = 2/10 + 4/40 + 10/100 = 0.40. Bound for n = 3: 3(2^{1/3} − 1) ≈ 0.780. U ≤ bound, so the set is schedulable under rate-monotonic priorities. The test is sufficient, not necessary: a set exceeding the bound might still be schedulable (exact response-time analysis would decide).

**EX024.** Mitigate now: disable the file-sharing service on the historian if not needed, or restrict it to a single named engineering host; monitor for connection attempts; patch after vendor certification within the next maintenance window; review date at certification + 14 days. Accepting with no action ignores the reachable path from the engineering zone.

### Chapter 13

**EX025.** `chain(recs[:5])[-1] == anchor[4]` → True: an attacker who deletes the last record and replaces the stored head with `anchor[4]` goes undetected. Including the count — anchor = H(head ‖ n) — makes truncation detectable (verified: the truncated anchor differs). Store the anchor in the incident ticket system and a write-once archive outside the control zone and outside historian administrators' privileges.

**EX026.** Control historian pushes hourly energy data and live pressure values to a DMZ replica (outbound only, enforced by firewall or a unidirectional gateway); finance and the dashboard query the replica. No inbound connection to the control zone. If the replica is compromised, attackers can read or falsify reporting data and dashboards — a data integrity and confidentiality problem — but gain no path into control.

### Chapter 14

**EX027.** Checklist: input length checked before indexing; integrity checked before use; constant-time secret comparison; no secrets in source; error paths reject; exceptions not swallowed; bounds on loops and sizes; logging of rejections without secrets; byte order explicit; tests for every rejection path. Findings: Lab 3 — truncated frames report "crc" rather than shape (diagnostic clarity); Lab 8 — key hard-coded in source (acceptable only as a labelled demo).

**EX028.** Match the advisory to SBOM entries and versions; confirm the vulnerable function or feature is present and reachable in the RTU-B configuration (e.g., is the TLS server enabled? is the library's vulnerable parser used?); ask the vendor for an assessment and fixed firmware; apply compensating controls (restrict the conduit, disable the feature); communicate to operations; schedule update through staged deployment; record the decision.

### Chapter 15

**EX029.** Lab 8: applies open design (security rests on the key, not secrecy of the algorithm) and complete mediation (every message checked); violates least privilege/separation in that the demo key is in source code and shared across stations — fix: per-station keys from protected storage. State machine (§9.5): applies fail-safe defaults (unlisted events rejected) and separation of privilege (reset needs local operator); not addressed: economy of mechanism if implemented with scattered flags — fix: table-driven implementation.

**EX030.** Consequence 1: hospital without water > 4 h — functions misused: pump start/stop at PS3/PS4, valve positions; engineered bound: hospital on-site storage plus local automatic restart logic that a remote command cannot disable. Consequence 2: chlorine overdose — functions: dosing setpoint and pump speed; engineered bound: dosing pump physically sized so maximum stroke at maximum flow cannot exceed a harmful concentration, plus hard-wired high-residual trip.

### Chapter 16

**EX031.** One mapping: N1 ← R3, R4, R5 (partly), R9; N2 ← R1, R2, R3, R7, R8; N3 ← R6, R8; N4 ← R5, R7. N3 relies on the fewest. Proposal: "R10 — Offline backups of SCADA and controller configurations shall be taken weekly, stored outside the control and enterprise domains, and restore-tested quarterly."

**EX032.** Data items (station ID, counter, level, pressure, alarms); encoding (binary, big-endian, 28-byte frame plus suite ID); rate (1 per 10 s per station plus alarms by exception); latency (≤ 1 s at gateway); authentication (HMAC-SHA256-128, per-station key); error handling (reject and log; alarm after 3 rejections in 10 min; stale-station alarm at 60 s); time source (internal NTP via allowlisted conduit; timestamps in UTC); ownership (gateway: TMRP engineering; SCADA side: operations); change process (ICD revision under configuration control with both owners' approval).

### Chapter 17

**EX033.** Seed 17, noise σ = 0.01 m, 48 h: threshold 0.03 m → 2 false-alarm episodes without attack (≈ 1 per day), first alarm on the 0.05 m/h ramp at 10.7 h; threshold 0.05 m → 0 false-alarm episodes, first ramp alarm at 10.9 h. Recommendation: 0.05 m — the 0.2 h detection delay is small against hours of hold-up, while daily false alarms would train operators to ignore the detector. Re-check with real noise data.

**EX034.** Compromise of RTU3 lets an attacker falsify both the level and the inlet flow, so the mass balance can be made consistent and the residual stays small; compromise of RTU4 alone falsifies outflow and is detectable. Improvement: an independent level transmitter wired to a separate logger (different controller and communications path), or a regular physical gauge reading compared with SCADA.

### Chapter 18

**EX035.** The rule fails the DMZ test: a compromised ERP server could send packets directly to the SCADA database. Alternative: ERP writes work-order status to a DMZ service; a control-zone process pulls the updates (or receives them through a narrowly validated broker), validating format and content; no inbound connection from enterprise to control.

**EX036.** Path: vendor → DMZ access gateway (MFA, named vendor accounts) → session approved per request by the duty manager → jump host in control zone → RTU-B diagnostic interface only; session recorded; access expires at the end of the approved window; vendor account disabled between sessions. Evidence: gateway and jump-host logs, recorded sessions, a test showing direct vendor connection to RTUs is blocked, and quarterly review of accounts.

### Chapter 19

**EX037.** If the RTU persists its counter every 1,000 increments and restarts, the last persisted value may be up to 999 behind the last used value. To avoid reusing a counter (which the receiver would reject, or which could enable replay after a receiver reset), the RTU skips forward by at least 1,000 beyond the persisted value. The receiver must persist the last accepted counter per station, or both sides rotate keys after restart.

**EX038.** A (fleet key): one stolen RTU lets the thief forge messages for all 42 stations; recovery needs re-keying of every station. B (per-station keys): forgery confined to the stolen station; one key revoked and replaced. SCADA storage of 42 keys is trivial in an HSM. Recommendation: B.

### Chapter 20

**EX039.** Assessed by rubric; for example, electricity distribution: consequence units — customers interrupted × hours, MW not served, critical customers affected; technologies — protection relays, distribution management systems, substation RTUs; regulations — NERC CIP standards (cite version and date) and NIS2 (2022/2555) for EU operators; incident — 2015 Ukraine, described from CISA IR-ALERT-H-16-056-01.

**EX040.** Model: a single security product with privileged kernel access was installed across many organisations in different sectors and updated automatically; one faulty content update crashed Windows hosts simultaneously, and Microsoft estimated about 8.5 million devices were affected. The property is a common cause through a shared, privileged, auto-updated dependency. Practice: staged (canary) rollouts of updates — by vendors and, where possible, controlled by customers for critical systems — plus recovery procedures that do not depend on the affected hosts. It was not an attack.

### Chapter 21

**EX041.** Continued service: "On loss of SCADA, PS3 and PS4 shall continue in local automatic control and operators shall be able to operate them locally within 1 h (exercise)." Containment: "On suspected SCADA compromise, remote command paths to all stations shall be disabled from the gateways within 15 min of the decision (test)." Restoration: "Remote operation shall be restored from verified offline backups within 8 h of the decision to restore (trial)."

**EX042.** Conflict: operator continuous access vs 15-min re-authentication. Options: (a) keep re-auth; (b) no re-auth; (c) view-only display stays live; control actions require quick re-authentication (badge tap or PIN) after 15 min of inactivity, with the control room physically access-controlled. Recommendation: (c). Owner: operations manager (risk owner) with security lead.

### Chapter 22

**EX043.** With PS4 needing only `grid_f2` in local automatic mode (no LTE for supply) and supply as OR: `{grid_f1}` → supply works (via PS4); `{ps4}` → works (via reservoir); `{ps4, grid_f1}` → fails. A model that makes supply depend on telemetry wrongly fails the first case.

**EX044.** States: remote automatic, local automatic, local manual, degraded (one pump), tripped, out of service. Attack path: forged stop commands and repeated start/stop (remote automatic → tripped via starter protection) → if trip reset is remote, attacker keeps the station tripped → out of service. Control: trip reset requires local action; authenticated commands; rate limit on start commands.

### Chapter 23

**EX045.** PS3 = PS4 = 1: top = P(TANK) = 0.03. G1 = G2 = 1: path B lost; path A lost if PS4 or GEN fails: 1 − 0.98 × 0.95 = 0.069; top = 0.03 × 0.069 = 0.00207. Interpretation: remote command authentication removes the cheapest adversary path (top falls from 0.03 to 9.1 × 10⁻⁵); if an adversary can cut both feeders, the generator and the hospital tank become the decisive barriers — maintain and test them.

**EX046.** Spoofing — forged frames (ATT&CK for ICS: Spoof Reporting Message) → per-station MAC. Tampering — modified values in transit → MAC. Repudiation — disputes about commands → signed or MACed logs with anchors. Information disclosure — telemetry read on the carrier network → carrier encryption plus optional payload encryption. Denial of service — jamming or flooding (Denial of Service; Block Reporting Message) → local automatic fallback, stale-station alarm, rate limits. Elevation of privilege — compromise of gateway to issue commands → gateway hardening, function-code filtering, local bounds.

### Chapter 24

**EX047.** (a) Hydraulic simulation plus STPA of the setpoint path — limit: model fidelity for transients. (b) Testbed experiment with labelled floods — limit: lab traffic differs from site. (c) Night-time functional exercise — limit: one occasion, observer effect. (d) Structured risk assessment with defined scales — limit: estimates, not measurements.

**EX048.** Verification: compare Euler with the exact integral (Lab 1); unit tests of `demand` and `drawn`; extreme cases (zero demand → infinite hold-up; constant demand → V/q). Validation: compare predicted level drop with historian data from a planned pump outage; operator face validity of the demand curve; sensitivity to demand amplitude. Intended use: hold-up estimation for planning. Invalid for pressure transients, water quality and network hydraulics.

### Chapter 25

**EX049.** Weights (0.40, 0.20, 0.10, 0.15, 0.15): A 2.80, B 3.35, C 4.20, D 4.45 — D overtakes C. Weights (0.20, 0.20, 0.30, 0.15, 0.15): A 3.60, B 3.35, C 4.20, D 3.65. C's lead depends on operability carrying real weight; if the decision-makers value forged-command prevention far above operability, D wins on paper — but D fails the hospital need in practice at night, which suggests operability is better expressed as a constraint than a weight.

**EX050.** Gateway SPOF: accept — gateway failure must fail to local automatic with alarm; add a cold-spare gateway per region. Manual mode bypass: accept — key-switch at the panel, SCADA alarm on mode change, local log. Key management staffing: accept — add 0.2 FTE operating cost and HSM maintenance to the business case; owner: TMRP manager.

### Chapter 26

**EX051.** Median of three tolerates one falsified or failed transmitter. An attacker who controls the RTU that reads all three can falsify all three consistently, defeating voting. Restore independence by wiring transmitters to separate I/O modules or controllers with separate communications, so that no single compromise controls two of three inputs.

**EX052.** Model ADR: context — PS4 is the hospital's direct feed, setpoints change about monthly; options — C2 (remote within bounds) or C3/C2-variant (local-only setpoint writes, remote monitoring); decision — local-only setpoint writes at PS4, remote start/stop retained with authentication; consequences — monthly site visit for setpoint changes, faster local response procedures, residual D1 risk at PS4 reduced to start/stop; revisit if setpoint change frequency rises or staffing changes.

### Chapter 27

**EX053.** Engineered limit: none (mechanical). Controller bounds: dosing PLC. Analyser alarm: separate logger and its communications. Rejection logging and alarm: via SCADA — shared with the system that might be compromised. Change: local non-volatile rejection log in the PLC and an independent alarm path (analyser logger to control room by a separate route).

**EX054.** Commands fail closed: if the gateway fails, no commands pass. Telemetry fails visible: SCADA raises a stale-station alarm within 60 s. Local control continues automatically within locally enforced limits. Shutting the station down would turn a security component failure into a supply failure.

### Chapter 28

**EX055.** With `old` = 5.2: v1 — NaN accepted (all comparisons false); +∞ rejected (`> hi`); −∞ rejected (`< lo`); 5.5 accepted (|5.5 − 5.2| = 0.3 ≤ 0.5, boundary inclusive); 5.50001 rejected (`> hi`). v2 rejects NaN and ±∞ via `isfinite`, accepts 5.5, rejects 5.50001.

**EX056.** Fields: UTC timestamp and time source; gateway ID; station ID; reason code (tag, replay, stale, shape, range); counter value (if parsable); last accepted counter; SHA-256 of the received frame; source address. Exclude key material and the full payload of commands where it could reveal sensitive setpoints to log readers; the frame hash allows correlation without disclosure.

### Chapter 29

**EX057.** Recall 5/7 ≈ 0.714; test FPR 3/7 ≈ 0.429. Per 1,000 events with one malicious: expected TP ≈ 0.714, FP ≈ 428. Operational precision ≈ 0.0017. Interpretation: the FPR estimate from 7 benign events is extremely uncertain, but even an order-of-magnitude improvement leaves the detector unusable for paging; it needs a much lower FPR, measured on far more benign data.

**EX058.** Base: 40% × 4 h = 160 %·h, plus recovery triangle 0.5 × 8 × 40 = 160 → 320 %·h. With local manual at 85%: 15 × 4 = 60, plus 0.5 × 8 × 15 = 60 → 120 %·h. R4 cuts resilience loss by about 62% in this synthetic case.

### Chapter 30

**EX059.** NaN compares false with everything, so v1's negative checks never reject it, while ±∞ fail `> hi` or `< lo`. About 2,000/10 = 200 special-value cases, one fifth NaN → about 40 expected; 31 observed (the generator drew 31 NaN cases with seed 30), well within random variation (binomial standard deviation ≈ 5.7). Every NaN case is an unsafe acceptance by v1, so the 31 failures are exactly the NaN cases.

**EX060.** Cases: (1) counters 1, 2, 3 → all accepted; (2) repeat 2 → rejected; (3) lower counter → rejected; (4) receiver restart, then replay of old message → rejected (requires persisted state or key rotation); (5) sender restart → resumes at persisted + 1,000, accepted; old counters rejected; (6) out-of-order delivery (3 before 2) → 3 accepted, 2 rejected and logged (documented behaviour); (7) counter at maximum 2⁶⁴ − 1 → key rotation required before wrap; test that the sender refuses to wrap. Pass criteria: exact accept/reject outcomes and log entries.

### Chapter 31

**EX061.** Triggers: telemetry from PS4 missing > 5 min while the link is up; any accepted frame failing post-hoc audit; priority-alarm latency > 60 s on two events in an hour; unexpected pump state change. Decision owner: duty operations manager. Rollback complete within 1 h (well within the hospital's 4 h buffer), with PS4 in local automatic throughout.

**EX062.** Controls: OS and service hardening; signed firmware updates; key in a secure element; function-code and register-range filtering; cabinet tamper switch alarmed to SCADA; local and forwarded logging; disabled unused ports; physical locks. Residual: an attacker with physical access to the open cabinet can connect to the legacy serial link and command the RTU directly; tamper detection reduces dwell time but does not prevent it.

### Chapter 32

**EX063.** With two crews, the transition from state 2 back to state 1 has rate 2μ, so $p_2 = p_0 \cdot 2r \cdot r/2 = p_0 r^2$ with $r = \lambda/\mu$. Unavailability ≈ 1.41 × 10⁻⁴, equal to the naive independent formula — because independent repair is exactly what that formula assumes. One crew: 2.81 × 10⁻⁴, about double.

**EX064.** With MTTR 504 h and one crew: unavailability ≈ 0.078 (about 28 days a year with both pumps down), versus 2.8 × 10⁻⁴ with a spare. Hold a spare pump: the cost is trivial against weeks of single-path supply to the hospital.

### Chapter 33

**EX065.** Model rows for the dosing loop (losses: unsafe water; harm from overdose): not provided — controller does not increase dose when demand rises (flawed flow feedback); provided when unsafe — controller increases dose when residual is already high (falsified analyser reading by an attacker); wrong timing — dose increase applied after flow has fallen (lag in feedback); too long — dosing continues after flow stops (stuck flow signal). Constraints: independent residual monitoring, dose interlocked to flow, physical stroke limit.

**EX066.** Violations: shared engineering workstation (one compromise can reprogram both control and safety logic) and shared switch (network path and common failure). Architecture: dedicated SIS engineering workstation kept offline, SIS program changes enabled only with a physical key-switch, SIS on a separate network or hard-wired to its sensors and final elements, read-only data export to the control system. Residual: insider with physical key, supply-chain compromise of SIS firmware.

### Chapter 34

**EX067.** 42 × 180 = 7,560 messages; at 50 per second, 151.2 s to drain; a priority alarm at the back waits about 151 s, violating R7 (60 s). Fix: priority queue for alarms and latest-value forwarding with rate-limited backfill to the historian.

**EX068.** Clauses: incident notification to LRWA within 1 h of detection; vulnerability disclosure affecting the private network within 72 h; planned maintenance notified 10 working days ahead; restoration priority for LRWA sites with 4 h target; access logs for LRWA APN provided monthly; annual joint exercise.

### Chapter 35

**EX069.** R6 (8 h) conflicts with the trial result (12 h): R6 is not met. Supply to the hospital does not depend on remote operation (local automatic mode, 72 h), so the N1 claim can still hold; the assurance case must record R6 as failed with a remediation plan or a stakeholder-agreed revision. The 24 h battery and 4 h buffer are consistent.

**EX070.** D3: insider misuse of local manual mode at PS4 — response: two-person rule for manual mode during non-maintenance hours, alarm and CCTV at the panel. D4: compromise of the gateway firmware update path — response: signed updates with keys in an HSM, staged rollout, monitoring of gateway behaviour. D5: counter persistence fails after power loss — response: restart test (EX060) and key rotation on unclean restart.

### Chapter 36

**EX071.** μ = 100/s: λ = 20 → ρ = 0.20, W = 12.5 ms, L = 0.25; λ = 40 → ρ = 0.40, W ≈ 16.7 ms, L ≈ 0.67; λ = 48 → ρ = 0.48, W ≈ 19.2 ms, L ≈ 0.92. Compared with μ = 50 (33.3, 100 and 500 ms), doubling capacity removes the storm-time delay explosion.

**EX072.** (1) Network-level filtering: only gateway tunnel endpoints may reach the verifier — drops most forged traffic before any computation. (2) Cheap pre-checks (length, station ID known, counter plausibly ahead of last accepted) before computing the MAC. (3) Per-source rate limits and a strict priority queue for verified alarms, so floods are shed at the lowest priority. Adding capacity alone loses against an attacker who can scale traffic.

### Chapter 37

**EX073.** Weaknesses: "not matching an operator action" is ambiguous — define as no logged operator command for that station and parameter in the previous 5 min; no contact details — add duty manager and security on-call numbers; restoring setpoints remotely could use the compromised path — specify local restoration by the duty technician if gateway MAC failures are present.

**EX074.** What happened: technician connected a laptop to the PS3 network to download logs. Why it made sense: jump-host route is slow and requires a ticket; logs were needed for a vendor call that afternoon. Defences that failed: no switch port security; no simple approved log path; procedure assumed jump host always available. Changes: provide a DMZ log collector so technicians need not connect; enable port security; supply a scanned maintenance laptop pool; simplify jump-host access for read-only log retrieval.

### Chapter 38

**EX075.** With T3b passing for R3, T8 passing for R4 and T6 passing for R8: untested ['R9'], tested but not passing [], verified 8/9 (88.9%). R9 stays unverified until a test of the independent dosing alarm (for example, stop dosing on the bench and time the alarm on the separate logger against 15 min) is written and passed. Verification is complete for the other eight requirements; validation of N1 still needs the stakeholder activities of EX076.

**EX076.** (1) Night-time exercise: operations staff switch PS3 and PS4 to local manual with real night staffing; observe time and errors; success: manual operation within 1 h and supply pressure maintained. (2) Planned PS4 isolation during low demand with the hospital estates manager monitoring on-site storage and pressure; success: supply maintained via reservoir with storage never below the level giving 4 h of buffer. Stakeholders: operations manager, hospital estates, TMRP engineering.

### Chapter 39

**EX077.** Frame: suite ID (1 byte) ‖ counter ‖ station ‖ value ‖ tag, with the MAC computed over the suite ID too (so it cannot be altered). Receiver keeps per-station allowed suites, e.g., {1} → {1, 2} during transition → {2}. Downgrade prevention: once a station has sent suite 2, reject suite 1 from it. Retirement: remove suite 1 from all allowed sets after all stations have migrated and revoke suite-1 keys.

**EX078.** Revoke the station key and remove it from the HSM; remove gateway accounts; wipe gateway and RTU storage (or destroy); update inventory, system model and dossier; remove allowlist entries and firewall rules for the old addresses; update monitoring baselines; dispose of or quarantine spares; record sign-off by operations and security.

### Chapter 40

**EX079.** Gap detection logs 67 gap events covering 81 missing counters with seed 40. The numbers differ from the 21 drops because every message that is not accepted — corrupted (14), delayed and stale (22), dropped (21), and slots where an old frame was replayed instead of the current one (24) — leaves its counter unused; 14 + 22 + 21 + 24 = 81. Consecutive missing counters produce one gap event, so there are fewer events than missing counters.

**EX080.** With reorder and restart classes (5% each, seed 40): reordered messages arriving after their successor are rejected as replays (17) — acceptable if documented, since stale data is discarded and the newer value is already held, but log it. Receiver restarts produce no visible error (26 accepted normally), which is the danger: after a reset, any replay arriving before the next fresh message would be accepted. The campaign shows no such case by chance; a deterministic test (restart, then replay) exposes it — a silent failure unless the receiver persists state.

### Chapter 41

**EX081.** 150 k: auth telemetry + offline backups → 330; 200 k: + local manual → 440 (cost 190); 250 k: + spare RTUs → 530; 300 k: auth, backup generator, local manual, offline backups → 590 (cost 280); 350 k: + spare RTUs → 680 (cost 340). Marginal benefit per extra 50 k: 110, 90, 60, 90 — broadly diminishing, but lumpy because controls are indivisible.

**EX082.** Of the 14 runs, three change the optimum to {auth telemetry, backup generator PS4, local manual} (cost 250, benefit 520 at baseline values): backup generator benefit × 1.2, offline backups × 0.8, or spare RTUs × 0.8. All other runs keep the baseline set. Conclusion: authenticated telemetry and local manual mode are robust choices; the last 90 k of budget is a near-tie between {offline backups + spare RTUs} and the backup generator, so that part of the decision should rest on better estimates or non-monetary criteria.

### Chapter 42

**EX083.** Protocol includes: question (does the cumulative detector at threshold θ deliver < 1 false alarm per month at measured noise while detecting 0.05 m/h ramps within 2 h?); decision (deploy and set θ, recalibration interval); design (simulation sweep, 100 seeds per cell); measurements; analysis rule fixed in advance; validation against two weeks of historian noise; limits (perfect mixing, honest flow meters, single tank).

**EX084.** What false-alarm rate per day would we see at our event rate? Which attacks were in the test set and who chose them? Was evaluation point-adjusted or leakage-free (train/test split by time)? How similar is the testbed to our plant in scale and noise? How does performance hold against an adaptive attacker who knows the detector?

### Chapter 43

**EX085.** Assessed by rubric; the agreement must name supervisors, scope, access method, confidentiality, safety induction, publication approval, incidental-finding route and an explicit statement that the student will not test or explore systems outside the agreed tasks.

**EX086.** Observation: operators record setpoint changes in a paper notebook as well as in SCADA. Connection: Chapter 13 (provenance) and Chapter 37 (operations). Difference: practice duplicates the electronic log; locally rational because the notebook survives SCADA outages, supports shift handover and is trusted. Question: do the two records ever disagree, and could the notebook serve as an independent integrity check?

### Chapter 44

**EX087.** Problems: unbounded scope ("water utilities"), no requirement or acceptance criteria, no data source, technology chosen before the problem. Rewrite: e.g., "A residual-based detector for false level data at one synthetic reservoir: requirements, simulation study with seeded noise, acceptance criteria < 1 false alarm/month and detection of 0.05 m/h ramps within 2 h, 12 weeks, synthetic data only."

**EX088.** Scope creep (likelihood medium, impact high; mitigation scope freeze at CDR; trigger: new feature requests after week 6); restart-safety harder than planned (M/H; spike in week 2; trigger: design not stable by week 4); bench fidelity insufficient (M/M; review with supervisor; trigger: reviewer finding); time (H/H; buffer week; trigger: milestone slip > 1 week); supervisor availability (L/M; scheduled reviews; trigger: missed review).

### Chapter 45

**EX089.** (1) "Keys for all 42 stations are generated on an engineer's laptop (KM procedure §3.2); a compromise of that laptop exposes the fleet; fails R1's intent; recommend generation in the HSM or gateway secure element." (2) "Restart behaviour of the receiver is not covered by any test (verification plan table 4); R2 requires replay rejection after restart; recommend tests per EX060." (3) Withdraw as a design preference, or reframe: "the design does not state why the chosen protocol meets R1 and R7; add rationale."

**EX090.** F2: accepted — stale-station alarm at 60 s and counter-gap logging added; campaign re-run with seed 40; owner: gateway lead; date: two weeks. F3: accepted — dossier corrected to "R6 not met (12 h)"; options costed: parallel imaging on spare hardware (9 h), plus standby SCADA image (6 h); stakeholder review to decide between design change and revised requirement; owner: TMRP manager; date: next steering meeting.

### Chapter 46

**EX091.** Generate the new key in the HSM; distribute to the gateway with key ID k+1; for 10 minutes the receiver accepts frames tagged with either key ID (key ID inside the authenticated header); the sender switches to k+1 and counters continue; if frames with k+1 fail, roll back to k; after the window, the receiver rejects k, and k is destroyed in both places; log every step.

**EX092.** Go with conditions: start the trial with the 60 s threshold, monitored by an engineer; collect data on false stale alarms during congestion; tune the threshold (e.g., 90 s for non-critical stations) by a stated date; brief operators that stale alarms during congestion are expected. The consequence of missing a real loss of data outweighs two false alarms a day for a limited period.

### Chapter 47

**EX093.** (1) With rebuild depending only on isolation: remote control at 9 h; critical path isolate → rebuild → restore config → verify → resume; imaging moves off the path. (2) With a 1 h rebuild from a standby image: 6 h; the rebuild chain and the re-keying chain (isolate → rekey → verify → resume) now tie at 6 h, so re-keying has become critical and further gains require shortening it too.

**EX094.** Options: (a) skip imaging (fastest; evidence lost; root cause and attacker persistence may be missed; possible regulatory or legal consequences); (b) image first (slowest); (c) image in parallel using spare hardware and rebuild on clean hardware (near-fastest; evidence preserved). Recommendation: (c), with a pre-approved decision that the operations director may authorise (a) only if supply is at risk. Owner: operations director.

### Chapter 48

**EX095.** Script: `os.walk` the folder; for each file read in chunks into `hashlib.sha256`; write `path, size, sha256, mtime` with `csv.writer`. Modification time is weak evidence because it is easily changed and not bound to content; a content hash recorded in version control (commit ID and signed tag) is much stronger.

**EX096.** Inconsistency: C3 shows R6 not met (12 h). Rewrite: "All requirements except the 8-hour restoration target were verified; a recovery trial restored remote operation in 12 hours while supply continued in local mode, and two design options to meet the target are presented."

### Chapter 49

**EX097.** Synthetic noise model → affects detector false-alarm and detection-time claims; real noise is likely non-Gaussian with drift, so false alarms are probably underestimated. Bench without real LTE → affects latency and stale-rejection claims; real latency and jitter would increase stale rejections and alarm latency. One recovery trial → affects R6 status; no variability estimate, so 12 h could be optimistic or pessimistic.

**EX098.** Example: "Need: legacy RTUs at a water utility accept unauthenticated commands over LTE, putting a hospital supply at risk. Design: a gateway adding per-station HMAC authentication with restart-safe counters, local automatic fallback and stale-station alarms. Methods: bench verification, seeded fault-injection campaigns and a recovery trial on synthetic systems. Results: authentication and replay requirements were met, including restarts after a fix; alarms met 60 s; remote restoration took 12 h against an 8 h target while supply continued locally. Limitations: synthetic bench without real LTE; a single recovery trial."

### Chapter 50

**EX099.** Assessed by rubric. Strong questions include: "What happens if the HSM fails?"; "Why 60 s?"; "What did your fault model not include?"; "Who owns D1?"; "What would change if the hospital buffer were 1 h?"; answers cite dossier items and state limits.

**EX100.** (1) Add statement that one trial gives no variability estimate; add 100 seeded simulated recovery runs with task-duration ranges, report median and 90th percentile; Section 7.4 and Appendix C. (2) Cite the battery manufacturer's depth-of-discharge recommendation or add a sensitivity table for 0.5–0.8; Section 5.2. (3) Replace "prevents" with "detects" and add detection-time context; abstract and Section 8.1.

<a id="glossary"></a>

## Glossary

- **Allowlist** — a policy permitting only listed flows, programs or values; everything else is denied.
- **Anchor** — a trusted copy of a hash-chain head (with record count) stored outside the attacker's reach.
- **Assurance case** — a structured argument that a system meets a claim, linking sub-claims to evidence, with qualifiers and defeaters.
- **Availability** — fraction of time a system is able to perform its function; MTBF/(MTBF + MTTR) for a simple repairable unit.
- **Base rate** — prevalence of the event of interest; decisive for an alarm's predictive value.
- **Beta-factor** — fraction of a unit's unavailability attributed to common causes that defeat redundant units together.
- **Conduit** — a controlled communication path between zones (IEC 62443 vocabulary).
- **Critical path** — the longest chain of dependent tasks; it sets the minimum completion time.
- **Defeater** — a condition under which an argument's conclusion would not hold.
- **DMZ** — an intermediate zone through which all traffic between control and enterprise networks is brokered.
- **Fault injection** — deliberate introduction of faults to test error handling.
- **HMAC** — a keyed message authentication code built from a hash function (FIPS 198-1).
- **Local autonomy** — ability of a site to keep operating safely without the centre or the network.
- **Minimal cut set** — a smallest set of basic events whose joint occurrence causes a fault tree's top event.
- **PLC / RTU** — programmable logic controller (scan-based local control) / remote terminal unit (remote data gathering and control over long links).
- **Precision / recall** — share of alarms that are real / share of real events that are alarmed.
- **Property-based test** — a test that checks a stated property on many generated inputs, including special values.
- **Residual** — difference between a measurement and an independent model's prediction.
- **Residual risk** — risk remaining after controls; must have an owner.
- **Secure boot** — verification of firmware signatures from an immutable root of trust before execution.
- **STPA** — System-Theoretic Process Analysis; finds unsafe control actions and their causal scenarios.
- **Time constant** — for first-order systems, the time to close about 63% of the gap to equilibrium.
- **Traceability** — links from needs to requirements, design, tests and results.
- **Unsafe control action** — a control action that, in a particular context, leads to a hazard.
- **Validation / verification** — right system for the need / system built to its specification.
- **Zone** — a grouping of assets with common security requirements.

<a id="references"></a>

## References

Laws, standards, guidance and incident pages change. Versions and dates below are those consulted for this draft (October 2026); re-verify before relying on them.

**Policy, law, standards and frameworks**

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Cybersecurity and Infrastructure Security Agency. [ICS Advisories](https://www.cisa.gov/news-events/ics-advisories).
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- International Electrotechnical Commission. [IEC 62443-3-2:2020 — Security risk assessment for system design (catalogue page)](https://webstore.iec.ch/en/publication/30727).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- MITRE. [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/).
- Modbus Organization. [Modbus Application Protocol Specification](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf).
- NASA. [NASA Systems Engineering Handbook (SP-2016-6105 Rev. 2)](https://www.nasa.gov/reference/systems-engineering-handbook/).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework). February 2024.
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final). September 2012.
- National Institute of Standards and Technology. [SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025.
- National Institute of Standards and Technology. [SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final). September 2023.
- National Institute of Standards and Technology. [SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final). November 2022.
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST, December 2021.
- National Institute of Standards and Technology. [SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final). August 2020.
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final). February 2022.
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final); [FIPS 197, Advanced Encryption Standard](https://csrc.nist.gov/pubs/fips/197/final); [FIPS 198-1, The Keyed-Hash Message Authentication Code (HMAC)](https://csrc.nist.gov/pubs/fips/198-1/final).
- National Institute of Standards and Technology. [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). 13 August 2024.
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- Open Source Security Foundation. [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/).
- Reproducible Builds project. [Reproducible Builds](https://reproducible-builds.org/).
- Rescorla, E. [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446). IETF, August 2018.
- Eddy, W. (ed.). [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293). IETF, August 2022.
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, February 1997.
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).

**Professional ethics**

- Association for Computing Machinery. [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics). 2018.
- National Society of Professional Engineers. [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics).

**Incidents and sector evidence**

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Cybersecurity and Infrastructure Security Agency. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf). 2019.
- E-ISAC and SANS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). March 2016 (archived copy).
- Langner, R. [Stuxnet: Dissecting a Cyberwarfare Weapon](https://doi.org/10.1109/MSP.2011.67). *IEEE Security & Privacy*, 9(3), 49–51, 2011.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems*, 21(6), 11–25, 2001.
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

**Computing, security and dependability**

- Avizienis, A., Laprie, J.-C., Randell, B., and Landwehr, C. [Basic Concepts and Taxonomy of Dependable and Secure Computing](https://doi.org/10.1109/TDSC.2004.2). *IEEE Transactions on Dependable and Secure Computing*, 1(1), 11–33, 2004.
- Brooks, F. P. [No Silver Bullet: Essence and Accidents of Software Engineering](https://doi.org/10.1109/MC.1987.1663532). *Computer*, 20(4), 10–19, 1987.
- Codd, E. F. [A Relational Model of Data for Large Shared Data Banks](https://doi.org/10.1145/362384.362685). *Communications of the ACM*, 13(6), 377–387, 1970.
- Diffie, W., and Hellman, M. [New Directions in Cryptography](https://doi.org/10.1109/TIT.1976.1055638). *IEEE Transactions on Information Theory*, 22(6), 644–654, 1976.
- Fagan, M. E. [Design and Code Inspections to Reduce Errors in Program Development](https://doi.org/10.1147/sj.153.0182). *IBM Systems Journal*, 15(3), 182–211, 1976.
- Kim, Y., Daly, R., Kim, J., et al. [Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors](https://doi.org/10.1109/ISCA.2014.6853210). *ISCA*, 2014.
- Kocher, P., Horn, J., Fogh, A., et al. [Spectre Attacks: Exploiting Speculative Execution](https://doi.org/10.1109/SP.2019.00002). *IEEE Symposium on Security and Privacy*, 2019.
- Liu, C. L., and Layland, J. W. [Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment](https://doi.org/10.1145/321738.321743). *Journal of the ACM*, 20(1), 46–61, 1973.
- McCabe, T. J. [A Complexity Measure](https://doi.org/10.1109/TSE.1976.233837). *IEEE Transactions on Software Engineering*, SE-2(4), 308–320, 1976.
- Parnas, D. L. [On the Criteria to Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623). *Communications of the ACM*, 15(12), 1053–1058, 1972.
- Rivest, R. L., Shamir, A., and Adleman, L. [A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](https://doi.org/10.1145/359340.359342). *Communications of the ACM*, 21(2), 120–126, 1978.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.
- Shannon, C. E. [A Mathematical Theory of Communication](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). *Bell System Technical Journal*, 27(3), 379–423, 1948.

**Control, safety, reliability and resilience**

- Åström, K. J., and Murray, R. M. [Feedback Systems: An Introduction for Scientists and Engineers](https://fbswiki.org/wiki/index.php/Main_Page). Princeton University Press; free online edition.
- Bruneau, M., Chang, S. E., Eguchi, R. T., et al. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra*, 19(4), 733–752, 2003.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis*, 29(4), 498–501, 2009.
- Leveson, N. [A New Accident Model for Engineering Safer Systems](https://doi.org/10.1016/S0925-7535(03)00047-X). *Safety Science*, 42(4), 237–270, 2004.
- Little, J. D. C. [A Proof for the Queuing Formula: L = λW](https://doi.org/10.1287/opre.9.3.383). *Operations Research*, 9(3), 383–387, 1961.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320(7237), 768–770, 2000.
- Saltelli, A., Ratto, M., Andres, T., et al. [Global Sensitivity Analysis: The Primer](https://doi.org/10.1002/9780470725184). Wiley, 2008.

**Evaluation, research and argument**

- Arp, D., Quiring, E., Pendlebury, F., et al. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). *USENIX Security Symposium*, 2022.
- Goh, J., Adepu, S., Junejo, K. N., and Mathur, A. [A Dataset to Support Research in the Design of Secure Water Treatment Systems](https://doi.org/10.1007/978-3-319-71368-7_8). *Critical Information Infrastructures Security (CRITIS 2016)*, LNCS 10242, 88–99, 2017.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *AAAI*, 2022.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology*, 9(10), e1003285, 2013.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation*, 7(1), 12–24, 2013.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). *IEEE Symposium on Security and Privacy*, 2010.
- Taormina, R., Galelli, S., Tippenhauer, N. O., et al. [Battle of the Attack Detection Algorithms: Disclosing Cyber Attacks on Water Distribution Networks](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969). *Journal of Water Resources Planning and Management*, 144(8), 2018.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
