# Application and Software Supply Chain Security: Engineering Course

- Language: English (`en`); course 129, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; Nine offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students who will design, build and verify secure applications and software supply chains.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: test and review only software you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic code and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one engineering student through foundations, application and supply-chain security engineering, verification laboratories, a placement and a capstone verifier for a transit operator's mobile app. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Kwame Asante** | Engineering student | Invented |
| **Ingrid Solberg** | Lead engineer and mentor | Invented |
| **Coastline Transit** | Fictional bus and ferry operator | Invented |
| **ticket-web** | Fictional ticketing web app | Invented |

### Core sources

[OWASP Top 10:2021](https://owasp.org/Top10/); OWASP [ASVS](https://owasp.org/www-project-application-security-verification-standard/) 4.0.3 and 5.0.0; OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/) and [SAMM](https://owaspsamm.org/); NIST [SP 800-218 (SSDF)](https://doi.org/10.6028/NIST.SP.800-218); [CWE Top 25](https://cwe.mitre.org/top25/); [SLSA v1.0](https://slsa.dev/spec/v1.0/); Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014). Full list in [References](#references).

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

You will (1) use rates of change to describe how software risk grows; (2) model accumulation of unpatched exposure over time; (3) read graphs of change; (4) connect calculus ideas to the course case.

### 1.1 The case

Kwame Asante is an engineering student at the fictional Ridgeway Institute of Technology. Through his five-year course he works with the fictional Coastline Transit, whose web app "ticket-web" sells bus and ferry tickets. His industry mentor is Ingrid Solberg, Coastline's lead engineer. In Kwame's first term, Coastline found that a copy of its build output on an internal mirror did not match the published digest, and that a template library in ticket-web had a published flaw affecting output escaping. Neither caused harm, but both made Ingrid ask how her team could know, at any moment, that what runs is what was built and that its parts are safe. Kwame's course returns to these two questions throughout.

### 1.2 Rates of change

A derivative measures how fast something changes. If ticket-web's dependency count grows from 40 to 160 over four years, the average rate is 30 new components per year. The instantaneous rate tells you whether growth is speeding up: a steepening curve means review effort must grow faster too.

### 1.3 Accumulation

An integral adds up a rate over time. If a vulnerable component is present for t days at a risk rate r(t), the accumulated exposure is the area under r(t). Shortening the time to upgrade reduces this area directly; this is why later chapters measure remediation days.

### 1.4 Reading graphs

Kwame plots weekly open advisories for ticket-web. The slope after a big framework upgrade is negative for six weeks, then flattens. A flat line at a non-zero value means advisories arrive as fast as they are fixed.

### 1.5 Limits

Calculus models assume smooth change; real advisories arrive in jumps. Models are guides for reasoning, not precise forecasts.

### Worked example

Kwame models exposure for the template flaw: published on day 0, patched in ticket-web on day 9, deployed on day 11. With constant risk rate, exposure is proportional to 11 days. If deployment had waited for the monthly release (day 30), exposure would be nearly three times larger. Ingrid uses the comparison to argue for faster security releases.

> **Synthetic case.** Ridgeway Institute, Coastline Transit, ticket-web and all figures are synthetic.

### Errors and limits

Risk rates are rarely known; the model compares options rather than giving absolute risk.

### Exercises

- **EX001 — Growth rate.** What is the average yearly growth from 40 to 160 components over four years? *Rubric:* 3 = 30 per year; 2 = partial; 1 = wrong; 0 = none.
- **EX002 — Exposure area.** How does faster upgrading reduce accumulated exposure? *Rubric:* 3 = shrinks area under risk curve; 2 = partial; 1 = none; 0 = none.
- **EX003 — Flat line.** What does a flat non-zero advisory line mean? *Rubric:* 3 = arrivals equal fixes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Rates and areas give a language for growth and exposure in software.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) model software dependencies as directed graphs; (2) compute transitive dependencies with breadth-first search; (3) recognise shared nodes and cycles; (4) relate graph structure to supply-chain risk.

### 2.1 Graphs

A directed graph has nodes and arrows. Each package is a node; an arrow from A to B means A depends on B. ticket-web depends directly on three packages, which depend on others.

### 2.2 Transitive closure

The set of all nodes reachable from ticket-web is its transitive dependency set. Every node in it is code that runs inside ticket-web, even if no Coastline developer chose it.

### Lab — Lab — reaching dependencies

```python
"""Transitive dependencies of a synthetic ticketing app by breadth-first search."""
from collections import deque
deps = {"ticket-web": ["webfw", "fare-calc", "qr-make"], "webfw": ["router", "tmpl"], "fare-calc": ["decimal-x"],
        "qr-make": ["imgkit", "zipx"], "imgkit": ["zipx"], "router": [], "tmpl": ["escape-html"], "decimal-x": [],
        "zipx": [], "escape-html": []}
seen, q = set(), deque(["ticket-web"])
while q:
    for d in deps[q.popleft()]:
        if d not in seen:
            seen.add(d); q.append(d)
print("direct:", len(deps["ticket-web"]), "transitive total:", len(seen))
print("reached via more than one path: zipx" if sum("zipx" in v for v in deps.values()) > 1 else "")
```

Run with `python3 lab_graph.py`. Verified output:

```text
direct: 3 transitive total: 9
reached via more than one path: zipx
```

### 2.3 Lab result

ticket-web has 3 direct dependencies but 9 in total. zipx is reached by more than one path (from qr-make and from imgkit), so updating it may require coordinating two parents.

### 2.4 Why it matters

Decan, Mens and Constantinou (2018) measured how vulnerabilities in npm spread through such transitive links; Zimmermann et al. (2019) showed that a few packages and maintainers reach a large share of an ecosystem. Graph structure explains why one flaw can affect thousands of applications.

### 2.5 Cycles

Some ecosystems allow cycles; search must track visited nodes, as the lab's "seen" set does, or it will loop forever.

### Counting paths

Discrete mathematics also counts. If each of ticket-web's three direct dependencies brings two more, and each of those one more, the tree has up to 3 + 6 + 6 = 15 nodes before sharing is removed. Shared nodes such as zipx reduce the total but increase coupling: one upgrade decision affects several parents. Kwame keeps both numbers, unique nodes and paths, because the first measures how much code runs and the second how hard upgrades are to coordinate.

### Worked example

Kwame draws the graph on the whiteboard for Ingrid's team. The template library tmpl, which had the flaw, is not a direct dependency: it arrives through the web framework. The team had not known it was there, which is why its advisory surprised them.

> **Synthetic case.** The graph is synthetic.

### Errors and limits

Real graphs include optional and development-only dependencies, which may not run in production.

### Exercises

- **EX004 — Lab counts.** How many direct and total dependencies does the lab find? *Rubric:* 3 = 3 direct, 9 total; 2 = one; 1 = none; 0 = none.
- **EX005 — Shared node.** Why is zipx notable? *Rubric:* 3 = reached by two paths; coordinate parents; 2 = partial; 1 = none; 0 = none.
- **EX006 — tmpl surprise.** Why did the tmpl advisory surprise the team? *Rubric:* 3 = transitive via framework; unknown; 2 = partial; 1 = none; 0 = none.

### Synthesis

Dependencies form graphs; the transitive set is what really runs.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) explain the physical basis of computation and storage; (2) relate energy and heat to reliability; (3) explain how physical faults can corrupt data; (4) justify integrity checks on stored artifacts.

### 3.1 Bits as physics

Bits are stored as charge, magnetism or light. Physical effects such as radiation, heat and wear can flip bits. Memory with error-correcting codes detects and fixes single-bit errors.

### 3.2 Storage reliability

Disks and flash wear out; silent corruption is rare but real at scale. Coastline's artifact mirror stores thousands of build files for years.

### 3.3 Integrity checks

A cryptographic digest such as SHA-256 changes completely if any bit changes. Checking digests detects corruption and tampering alike; chapter 19 returns to this in the lab.

### 3.4 Heat and performance

Hot servers slow down; build machines under heavy load can time out, producing incomplete artifacts. Monitoring temperature and build duration helps catch this.

### 3.5 The mirror mismatch

Investigation showed the mismatched mirror copy was truncated during a storage failure, not tampered with. But the team could not tell which until they compared logs.

### Redundancy

Engineers protect against physical faults with redundancy: two copies on different disks, regular checks, and the ability to rebuild from source. Coastline keeps artifacts in two storage systems and can rebuild any release from its tagged source, provided the build tools and dependencies are still available. Kwame notes that rebuilding only helps if the build is reproducible, an idea from Lamb and Zacchiroli (2022) that the course returns to later.

### Checksums in practice

Kwame tests the weekly check by changing one byte in a test copy; the alert fires within minutes.

### Worked example

Kwame recommends the mirror verify the digest of every file on write and weekly thereafter, and that deployment refuse any artifact whose digest does not match the build record. Ingrid adopts both.

> **Synthetic case.** The mirror incident is synthetic.

### Errors and limits

Digests detect change but not whether the original build was trustworthy.

### Exercises

- **EX007 — Bit flips.** Name two causes of bit flips. *Rubric:* 3 = radiation, heat, wear (two); 2 = one; 1 = none; 0 = none.
- **EX008 — Digest property.** What happens to a SHA-256 digest if one bit changes? *Rubric:* 3 = changes completely; 2 = partial; 1 = none; 0 = none.
- **EX009 — Mirror cause.** What caused the mirror mismatch? *Rubric:* 3 = truncation in storage failure, not tampering; 2 = partial; 1 = none; 0 = none.

### Synthesis

Physics makes corruption possible; digests make it detectable.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write clear, small functions; (2) handle errors explicitly; (3) read and test simple code; (4) apply secure defaults from the start.

### 4.1 Small functions

A function should do one thing. Kwame writes fare_for(zone, passengers) that returns a price, separate from code that reads the form.

### 4.2 Explicit errors

If zone is unknown, the function raises an error instead of returning zero, which would make tickets free. Failing safely is a security property.

### 4.3 Testing

Each function has small tests: valid zones, unknown zone, zero passengers. Tests run on every change.

### 4.4 Secure defaults

Defaults should be the safe choice: deny unless allowed, escape output unless told otherwise. The template flaw in tmpl arose when one function's default skipped escaping for certain attributes.

### 4.5 Readability

Clear names and short functions make review effective; reviewers miss flaws in long, tangled code.

### 4.6 CWE vocabulary

MITRE's CWE Top 25 lists weaknesses such as improper input validation (CWE-20) and cross-site scripting (CWE-79). Learning their names early helps read advisories.

### Version control

All code lives in version control with history. Each change has a message explaining why it was made and links to a ticket. When the tmpl advisory arrived, the team could see exactly when the framework version that brought tmpl had been added and who reviewed it. History turns questions about the past into simple searches, and it lets the team undo a bad change quickly. Kwame learns to write commit messages that a stranger could understand a year later.

### Code style

A shared formatter keeps code consistent, so reviews focus on logic rather than layout.

### Worked example

Kwame's first pull request adds fare_for with four tests. Ingrid's review asks him to make the error message avoid echoing user input directly into the page, preventing a possible output-escaping problem.

> **Synthetic case.** Code and review are synthetic.

### Errors and limits

Tests show presence of expected behaviour, not absence of all flaws.

### Exercises

- **EX010 — Fail safely.** Why raise an error for an unknown zone? *Rubric:* 3 = returning zero would make tickets free; 2 = partial; 1 = none; 0 = none.
- **EX011 — Default flaw.** What default caused the tmpl flaw? *Rubric:* 3 = skipped escaping for some attributes; 2 = partial; 1 = none; 0 = none.
- **EX012 — Review comment.** What did Ingrid's review ask? *Rubric:* 3 = avoid echoing input into page in error; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small, tested functions with safe defaults are the first security control.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write clear technical reports; (2) present security findings to mixed audiences; (3) use diagrams effectively; (4) communicate uncertainty.

### 5.1 Audiences

Engineers want detail, managers want decisions and impact, the public wants reassurance and facts. Kwame writes the same finding three ways.

### 5.2 Report structure

Summary, context, findings, evidence, recommendations, limitations. The summary fits in five lines.

### 5.3 Diagrams

Kwame's dependency graph diagram made the tmpl surprise clear to managers in one glance.

### 5.4 Uncertainty

"We have no evidence the flaw was used" is different from "the flaw was not used". Ingrid insists on accurate phrasing.

### 5.5 Responsible detail

Reports about flaws avoid giving step-by-step misuse instructions; they describe the weakness, its effect and the fix.

### Written decisions

Important decisions are recorded in short decision records: context, options, choice, consequences. When Coastline decided to deploy security fixes outside the monthly release, the record explained the 11-day versus 30-day exposure comparison from chapter 1. New staff can read why the rule exists instead of guessing, and the team can revisit the decision if circumstances change. Kwame writes his first decision record about the digest check on the artifact mirror, keeping it to one page with a clear recommendation.

### Feedback

Kwame asks two readers, one technical and one not, to read each report before it goes out. They mark anything unclear. Most of his early drafts used jargon such as "transitive dependency" without explanation; he now adds a short definition the first time a term appears.

### Worked example

Kwame's summary for Coastline's board: "A third-party template component in ticket-web had a published flaw for 11 days before our fix was deployed. We found no evidence it was used. We have added automated checks so such components are found within a day." The board asks for a quarterly update.

> **Synthetic case.** Reports are synthetic.

### Errors and limits

Simplifying for managers must not change the meaning.

### Exercises

- **EX013 — Report sections.** List the report sections. *Rubric:* 3 = summary, context, findings, evidence, recommendations, limitations; 2 = four; 1 = two; 0 = none.
- **EX014 — Accurate phrasing.** Why say "no evidence it was used"? *Rubric:* 3 = not the same as not used; 2 = partial; 1 = none; 0 = none.
- **EX015 — Responsible detail.** What do reports avoid? *Rubric:* 3 = step-by-step misuse instructions; 2 = partial; 1 = none; 0 = none.

### Synthesis

Communicate to each audience accurately, with diagrams and honest uncertainty.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use series and growth models to reason about compounding effects; (2) model decay of unpatched versions in a user base; (3) compare exponential and linear models; (4) interpret model fit honestly.

### 6.1 Compounding

When each component brings its own dependencies, the total can grow like a geometric series. If every package added brings, on average, 0.8 new transitive packages, adding one direct dependency adds 1 + 0.8 + 0.64 + ... = 1/(1 − 0.8) = 5 packages in expectation. This simple sum explains why a small decision can enlarge the attack surface far more than expected.

### 6.2 Decay models

After Coastline releases a fixed version of its mobile ticket app, users update gradually. If 10% of the remaining old installations update each day, the share still on the old version after t days is 0.9^t: about 35% after 10 days and 4% after 30. This exponential decay model helps plan how long old server-side support for the vulnerable version must continue.

### 6.3 Linear versus exponential

Kwame fits both models to the real update data from the last app release. The exponential model fits the first two weeks well but overestimates updating later, when the remaining users are those who rarely open the app. Neither model is perfect; he reports both and the range they imply.

### 6.4 Using the models

The models inform two decisions: whether to force updates for security fixes, and how long to keep compatibility code. A forced update shortens the tail but annoys riders whose phones are old.

### 6.5 Honest fit

A good fit on past data does not guarantee future behaviour; holidays, app store delays and phone models change patterns. Kwame states the model's assumptions in every chart caption.

### Worked example

For the template fix, the server-side part is deployed at once, so the decay model applies only to the mobile app, which embedded a copy of the affected rendering code. Kwame predicts 4% of installations still unpatched after 30 days under the 10% daily model; actual data shows 7%. Coastline decides to show an update prompt after day 14.

> **Synthetic case.** Update rates and app data are synthetic.

### Errors and limits

Series and decay models simplify behaviour; validate them against observed data before relying on them.

### Exercises

- **EX016 — Expected packages.** With branching 0.8, how many packages does one direct dependency add in expectation? *Rubric:* 3 = 5; 2 = partial; 1 = wrong; 0 = none.
- **EX017 — Decay values.** What share remains after 10 and 30 days at 10% daily updating? *Rubric:* 3 = ~35% and ~4%; 2 = one; 1 = none; 0 = none.
- **EX018 — Prompt decision.** Why did Coastline add an update prompt at day 14? *Rubric:* 3 = observed 7% above predicted 4%; tail long; 2 = partial; 1 = none; 0 = none.

### Synthesis

Series and decay models make compounding and slow updating visible, within honest limits.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) reason about rare events and false alarms; (2) compute and interpret similarity scores for package names; (3) choose thresholds for review; (4) understand base rates in security checks.

### 7.1 Rare events and base rates

Most new dependencies are legitimate. If 1 in 1,000 proposed packages were malicious and a check flagged 5% of legitimate ones, most flags would still be false alarms. This is the base-rate effect: alerts must be cheap to review or teams will ignore them.

### 7.2 Lookalike names

Ohm et al. (2020) documented malicious packages that used names close to popular ones (typosquatting). A defensive check compares each newly proposed dependency name with popular names and asks a human to look when they differ by a single character.

### Lab — Lab — name similarity

```python
"""Flag new dependency names within edit distance 1 of a popular package (synthetic names)."""
def dist(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
popular = ["requestz", "escape-html", "qr-make", "fare-calc"]
proposed = ["escape-htm1", "qr-maker", "datefmt", "requests"]
for p in proposed:
    near = [x for x in popular if 0 < dist(p, x) <= 1]
    print(f"{p:12} {'REVIEW: near ' + ', '.join(near) if near else 'ok'}")
```

Run with `python3 lab_typo.py`. Verified output:

```text
escape-htm1  REVIEW: near escape-html
qr-maker     REVIEW: near qr-make
datefmt      ok
requests     REVIEW: near requestz
```

### 7.3 Lab result

Three of four proposed names are flagged: escape-htm1 (one character from escape-html), qr-maker (one from qr-make), and requests (one from requestz). datefmt is not near any popular name. The requests flag shows why review matters: in another ecosystem "requests" may be a well-known legitimate package, so the human reviewer checks publisher, history and download counts before deciding.

### 7.4 Choosing a threshold

A distance of 1 catches most single typing errors with few flags; a distance of 2 would flag many more legitimate names. Kwame measures over a month: 38 new dependency proposals, 4 flagged at distance 1, of which 1 was suspicious and blocked after review.

### 7.5 Statistics for decisions

Kwame reports the flag rate and the reviewed outcomes, not just "the check works". Over time these counts estimate the check's precision.

### Worked example

The suspicious package, a near-copy of qr-make published two days earlier by a new account, was never installed. Ingrid adds the check to the pull-request pipeline and asks for monthly counts.

> **Synthetic case.** Package names and counts are synthetic.

### Errors and limits

Similarity checks miss malicious packages with unrelated names and those introduced through legitimate maintainers' accounts.

### Exercises

- **EX019 — Base-rate effect.** Why are most flags false alarms? *Rubric:* 3 = rare malicious packages; base rate; 2 = partial; 1 = none; 0 = none.
- **EX020 — Lab flags.** Which names did the lab flag? *Rubric:* 3 = escape-htm1, qr-maker, requests; 2 = two; 1 = one; 0 = none.
- **EX021 — Month results.** What did the month of use show? *Rubric:* 3 = 38 proposals, 4 flagged, 1 blocked; 2 = partial; 1 = none; 0 = none.

### Synthesis

Similarity checks help when paired with human review and honest counts.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) explain how processors execute code and isolate processes; (2) relate memory layout to classes of software weaknesses; (3) explain hardware security features that support software; (4) connect architecture to language choice.

### 8.1 Execution

Processors fetch instructions, decode them and execute them, reading and writing memory. Operating systems use hardware features such as privilege levels and virtual memory to separate programs.

### 8.2 Memory and weaknesses

In languages without automatic bounds checks, writing past the end of a buffer can corrupt nearby data. The CWE Top 25 includes out-of-bounds write (CWE-787) and use after free (CWE-416), both memory-safety weaknesses. ticket-web's image library imgkit is written in such a language and wrapped for the web app.

### 8.3 Hardware help

Features such as non-executable memory and address randomisation make memory flaws harder to misuse, but do not remove the flaw. Defence in depth combines them with safer code.

### 8.4 Language choice

Memory-safe languages prevent many of these weaknesses by design. Coastline writes new services in memory-safe languages and isolates imgkit in a separate process with limited permissions.

### 8.5 Isolation by design

Running risky parsing code in its own process, with no network access and a time limit, limits damage if a flaw is triggered by a malformed image.

### Measuring isolation

Kwame tests the image worker's limits by feeding it synthetic oversized but harmless images in a test environment: the worker is stopped by its time limit after two seconds and restarted automatically, while the web server keeps serving tickets. The test shows the isolation works as designed, and it is repeated whenever the worker's configuration changes.

### Worked example

When the imgkit advisory (chapter 24) arrives, the isolation means the worst outcome is a crashed image-worker process, not a compromised web server. Kwame records this as evidence that architecture choices reduced the advisory's impact.

> **Synthetic case.** Components and advisories are synthetic.

### Errors and limits

Isolation adds complexity and overhead; it must be maintained as code changes.

### Exercises

- **EX022 — Memory CWEs.** Name two memory-safety CWEs. *Rubric:* 3 = CWE-787, CWE-416; 2 = one; 1 = none; 0 = none.
- **EX023 — Hardware limits.** What do hardware features not do? *Rubric:* 3 = remove the flaw; 2 = partial; 1 = none; 0 = none.
- **EX024 — imgkit isolation.** How is imgkit isolated? *Rubric:* 3 = separate process, limited permissions, no network, time limit; 2 = partial; 1 = none; 0 = none.

### Synthesis

Architecture and language choices shape which weaknesses exist and how far damage spreads.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) validate input with allowlists; (2) separate parsing from business logic; (3) handle invalid input safely; (4) write tests for validation rules.

### 9.1 Allowlists

An allowlist says exactly what is acceptable: zones A to D, one to nine passengers, four digits for card endings. Anything else is rejected. This is safer than trying to list everything bad. ASVS 4.0.3's validation chapter (V5) and the OWASP Top 10:2021 category A03 Injection both stress validating and handling input safely.

### Lab — Lab — validating fields

```python
"""Allowlist validation of synthetic ticket form fields."""
import re
rules = {"zone": re.compile(r"^[A-D]$"), "passengers": re.compile(r"^[1-9]$"), "card_last4": re.compile(r"^\d{4}$")}
inputs = [{"zone": "B", "passengers": "2", "card_last4": "4242"}, {"zone": "Z", "passengers": "2", "card_last4": "4242"},
          {"zone": "A", "passengers": "12", "card_last4": "42a2"}]
for i, form in enumerate(inputs, 1):
    bad = [k for k, rx in rules.items() if not rx.fullmatch(form.get(k, ""))]
    print(f"form {i}: {'accepted' if not bad else 'rejected ' + ', '.join(bad)}")
```

Run with `python3 lab_validate.py`. Verified output:

```text
form 1: accepted
form 2: rejected zone
form 3: rejected passengers, card_last4
```

### 9.2 Lab result

Form 1 is accepted. Form 2 is rejected because zone Z is not allowed. Form 3 is rejected for two fields: 12 passengers exceeds the single-digit rule and "42a2" is not four digits.

### 9.3 Where to validate

Validation happens on the server; browser checks improve user experience but can be bypassed. Validation is also not the only defence: output must still be escaped and queries parameterised (chapter 13).

### 9.4 Error handling

Rejected forms return a clear message naming the field, without echoing the raw input. Logs record the rejection without storing card data.

### 9.5 Testing rules

Each rule has tests for boundaries: zone A and D accepted, E rejected; 1 and 9 passengers accepted, 0 and 10 rejected.

### Canonical forms

Before validating, input is converted to a standard form: trimmed of spaces and in one character encoding. Otherwise two strings that look the same could be treated differently, letting some values slip past checks. Kwame adds a test where the zone value has a trailing space; after normalising it is accepted as B.

### Worked example

A customer complains that groups of 12 cannot buy one ticket. Product decides groups over 9 must use the group booking page. The rule stays, the error message now links to group booking, and a test confirms the link appears.

> **Synthetic case.** Forms and complaints are synthetic.

### Errors and limits

Allowlists must be kept in sync with business rules or legitimate users are blocked.

### Exercises

- **EX025 — Allowlist meaning.** What is an allowlist? *Rubric:* 3 = exactly what is acceptable; reject rest; 2 = partial; 1 = none; 0 = none.
- **EX026 — Lab rejections.** Why was form 3 rejected? *Rubric:* 3 = passengers 12; card_last4 not digits; 2 = partial; 1 = none; 0 = none.
- **EX027 — Server side.** Why validate on the server? *Rubric:* 3 = browser checks bypassable; 2 = partial; 1 = none; 0 = none.

### Synthesis

Validate with allowlists on the server, test boundaries and keep rules aligned with the business.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply professional ethics to software security work; (2) handle discovered flaws responsibly; (3) weigh public safety and service availability; (4) recognise conflicts of interest.

### 10.1 Duties

Engineers owe duties to the public, employers and the profession. For a transit app, public duties include protecting riders' payment data and keeping ticket sales available during disruptions.

### 10.2 Responsible handling

When Kwame notices that an old staff test account still works on the staging site, he reports it to Ingrid rather than exploring what it can do. Testing beyond what you are authorised to do is wrong even with good intentions.

### 10.3 Disclosure

When the team finds a flaw in an open-source component, it reports privately to the maintainers and waits for a fix before discussing it publicly, a practice known as coordinated disclosure.

### 10.4 Safety and availability

Security changes can break services. Forcing all riders to update the app during a storm, when ferries are cancelled and people need tickets for alternative buses, could cause real harm. Timing matters.

### 10.5 Conflicts of interest

Kwame's friend runs a company selling scanning tools. When Coastline evaluates scanners, Kwame declares the relationship and steps back from the decision.

### 10.6 Codes of conduct

Professional bodies' codes emphasise honesty, competence and public welfare. They help when pressure to ship conflicts with safety.

### Whistleblowing

If serious safety concerns are ignored inside an organisation, professional codes and laws in many countries protect engineers who raise them through proper channels. Kwame learns where Coastline's policy says to raise such concerns.

### Worked example

A manager asks Kwame to mark a known high-severity finding as "accepted risk" to meet a release date. Kwame explains he lacks authority to accept risk and escalates to Ingrid, who arranges a short delay and a fix.

> **Synthetic case.** Situations are synthetic.

### Errors and limits

Ethics rarely gives one right answer; record reasoning and escalate when unsure.

### Exercises

- **EX028 — Test account.** How did Kwame handle the old test account? *Rubric:* 3 = reported, did not explore; 2 = partial; 1 = none; 0 = none.
- **EX029 — Coordinated disclosure.** Describe coordinated disclosure. *Rubric:* 3 = report privately; wait for fix before public; 2 = partial; 1 = none; 0 = none.
- **EX030 — Risk acceptance.** How did Kwame respond to the risk-acceptance request? *Rubric:* 3 = lacks authority; escalated; 2 = partial; 1 = none; 0 = none.

### Synthesis

Act within authority, disclose responsibly and weigh safety, availability and honesty.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) explain how web requests travel and are protected; (2) describe TLS at a conceptual level; (3) identify where package downloads can be intercepted or altered; (4) apply network controls to the build pipeline.

### 11.1 Web requests

A rider's phone sends an HTTPS request to ticket-web. DNS finds the server address, TCP carries data, TLS encrypts and authenticates the connection, and HTTP carries the request and response. A weakness at any layer can expose data.

### 11.2 TLS

TLS lets the phone check that it is talking to Coastline's real server, using a certificate signed by a trusted authority, and then encrypts traffic. OWASP Top 10:2021 A02 Cryptographic Failures includes sending sensitive data without proper encryption.

### 11.3 Package downloads

Build servers download dependencies over the network. If downloads used plain HTTP, or if certificate checks were disabled, an attacker on the network could substitute a different package. Coastline's builds use HTTPS only, with checks enabled, and verify each package against a lockfile hash.

### 11.4 Restricting egress

Build machines are allowed to reach only the package registry mirror and source host. Unexpected outbound connections during a build are blocked and logged, which limits what a malicious install script could reach.

### 11.5 Internal mirror

Coastline uses an internal mirror of approved packages. It reduces dependence on the public registry's availability and gives one place to apply checks.

### 11.6 Monitoring

Network logs from the build environment are kept, so the team can check what a build contacted.

### Certificate checks in code

Kwame searches the codebase for any setting that turns off certificate verification and finds one in an old test script. It is removed, and a CI check now fails any change that disables verification.

### Worked example

A build fails because a new dependency's install step tries to download extra files from an unlisted host. The egress block stops it. Investigation shows the package downloads optional fonts; the team chooses a different package that does not need network access at install time.

> **Synthetic case.** Network setup and events are synthetic.

### Errors and limits

Network controls cannot stop a malicious package that only uses allowed hosts.

### Exercises

- **EX031 — TLS role.** What two things does TLS provide? *Rubric:* 3 = authentication of server and encryption; 2 = one; 1 = none; 0 = none.
- **EX032 — Download protection.** How are package downloads protected? *Rubric:* 3 = HTTPS with checks; lockfile hash; 2 = partial; 1 = none; 0 = none.
- **EX033 — Egress block.** What happened when a package tried to reach an unlisted host? *Rubric:* 3 = blocked; chose different package; 2 = partial; 1 = none; 0 = none.

### Synthesis

Protect the path packages travel and limit where builds can connect.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) explain processes, users and permissions; (2) apply least privilege to application services; (3) isolate build jobs; (4) use operating-system logs for security evidence.

### 12.1 Processes and users

Each program runs as a process owned by a user account. Permissions decide which files and devices it can use. ticket-web runs as a dedicated service user, not as an administrator.

### 12.2 Least privilege

The service user can read its code and write only to its log and temporary folders. If a flaw lets an attacker run code inside ticket-web, they gain only these limited rights.

### 12.3 Build isolation

Each build runs in a fresh, short-lived container or virtual machine, destroyed afterwards. This prevents one build from leaving files that affect the next, an issue SLSA v1.0 addresses in its build requirements for isolated builds.

### 12.4 Secrets on the system

Build credentials are injected only for the steps that need them and never written to disk. A build that prints environment variables must not reveal tokens; the CI system masks them in logs.

### 12.5 OS logs

Operating systems record process starts, logins and permission changes. These logs help answer what happened during a build or on a server.

### 12.6 Patching the OS

Base images for servers and builds are rebuilt weekly with security updates, and a record shows which image each build used.

### File permissions review

A monthly script lists files writable by the service user outside its allowed folders; any result is investigated. The first run finds an old upload folder left writable, which is fixed the same day.

### Worked example

Kwame finds that an old build agent was reused across jobs and kept a cache folder between builds. A poisoned cache could have affected later builds. Coastline replaces it with ephemeral agents and adds the agent image digest to each build record.

> **Synthetic case.** Systems and findings are synthetic.

### Errors and limits

Isolation is only as strong as the platform; keep the platform patched.

### Exercises

- **EX034 — Service user.** Why run ticket-web as a dedicated user? *Rubric:* 3 = limit rights if compromised; 2 = partial; 1 = none; 0 = none.
- **EX035 — Ephemeral builds.** Why use fresh build environments? *Rubric:* 3 = prevent leftover files affecting next build; 2 = partial; 1 = none; 0 = none.
- **EX036 — Old agent fix.** How was the reused agent problem fixed? *Rubric:* 3 = ephemeral agents; image digest in record; 2 = partial; 1 = none; 0 = none.

### Synthesis

Least privilege and isolated, recorded builds limit damage.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) design data stores with security in mind; (2) use parameterised queries to keep input as data; (3) protect sensitive fields; (4) control access to data.

### 13.1 Data design

ticket-web stores riders, tickets and payments. Card numbers are not stored; the payment provider holds them, and ticket-web keeps only a token and the last four digits.

### 13.2 Queries and injection

When code builds database queries by joining strings with user input, characters in the input can change the query's meaning. This weakness, SQL injection (CWE-89), is part of OWASP Top 10:2021 A03 Injection. The defence is parameterised queries, which send the query and the data separately.

### Lab — Lab — parameterised queries

```python
"""Parameterised queries keep input as data; string building breaks on an ordinary apostrophe."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE riders (name TEXT, zone TEXT)")
db.executemany("INSERT INTO riders VALUES (?, ?)", [("Ann O'Neil", "A"), ("Ben Cole", "B")])
name = "Ann O'Neil"
print("parameterised:", db.execute("SELECT zone FROM riders WHERE name = ?", (name,)).fetchall())
try:
    db.execute("SELECT zone FROM riders WHERE name = '" + name + "'").fetchall()
except sqlite3.OperationalError as e:
    print("string-built query failed:", e)
```

Run with `python3 lab_param.py`. Verified output:

```text
parameterised: [('A',)]
string-built query failed: near "Neil": syntax error
```

### 13.3 Lab result

With a parameterised query, looking up "Ann O'Neil" returns her zone A. The string-built version fails with a syntax error because the apostrophe in her name ends the text early. The same mechanism that breaks for an honest name is what makes string-built queries dangerous; parameterisation removes it.

### 13.4 Access to data

Staff access goes through roles: support sees tickets but not payment tokens; finance sees refunds. Database accounts used by the app have only the permissions it needs.

### 13.5 Backups and retention

Backups are encrypted and tested; rider data is deleted after the legal retention period.

### Encryption at rest

The database disk and backups are encrypted, and keys are held in a separate key service. Staff who manage backups cannot read the key service, so a stolen backup alone is useless. Kwame tests a restore every quarter to prove the backups and keys work together.

### Worked example

Code review finds one report query built with string formatting for a date filter. Although the date comes from a dropdown, Kwame changes it to a parameter, explaining that inputs can be altered before reaching the server.

> **Synthetic case.** Data and code are synthetic.

### Errors and limits

Parameterisation does not help if table or column names come from users; use allowlists for those.

### Exercises

- **EX037 — Card data.** What card data does ticket-web keep? *Rubric:* 3 = token and last four digits only; 2 = partial; 1 = none; 0 = none.
- **EX038 — Lab contrast.** What did the lab show? *Rubric:* 3 = parameterised works; string-built fails on apostrophe; 2 = partial; 1 = none; 0 = none.
- **EX039 — Dropdown reasoning.** Why parameterise a dropdown value? *Rubric:* 3 = inputs can be altered before server; 2 = partial; 1 = none; 0 = none.

### Synthesis

Keep input as data, store less sensitive data and limit access by role.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) use a development lifecycle that builds in security; (2) apply code review and continuous integration; (3) manage dependencies deliberately; (4) map practices to the SSDF.

### 14.1 Lifecycle

Coastline plans, designs, builds, tests, releases and maintains ticket-web in two-week iterations. Security activities sit in each step rather than at the end.

### 14.2 The SSDF

NIST SP 800-218 (Souppaya et al., 2022) organises secure development practices into four groups: Prepare the Organization (PO), Protect the Software (PS), Produce Well-Secured Software (PW) and Respond to Vulnerabilities (RV). Kwame maps Coastline's activities to these groups to find gaps.

### 14.3 Code review

Every change is reviewed by another engineer. A checklist prompts reviewers to look at input handling, authorisation and new dependencies.

### 14.4 Continuous integration

Each change runs tests, static analysis, the dependency name check (chapter 7) and an advisory check. Failures block merging.

### 14.5 Dependency policy

New dependencies need a reason, an owner and a check of maintenance activity. Kula et al. (2018) found that developers often do not update dependencies, so each dependency's owner is responsible for keeping it current.

### 14.6 Release

Releases are built by CI, signed, and recorded with their digests.

### Definition of done

A change is done only when it has tests, has been reviewed, passes CI and has its documentation updated. Security items are part of this definition, not optional extras: a new endpoint needs an authorisation test, and a new dependency needs a recorded owner. Kwame notices that clear rules reduce arguments during review, because everyone knows what is expected before they start.

### Retrospectives

Every iteration ends with a short review of what went well and what to improve, including security.

### Worked example

The SSDF mapping shows a gap in PO: no training plan for secure coding. Coastline adds a yearly short course and makes the review checklist part of onboarding.

> **Synthetic case.** Practices and mapping are synthetic.

### Errors and limits

A mapping shows practices exist, not that they work well.

### Exercises

- **EX040 — SSDF groups.** Name the four SSDF groups. *Rubric:* 3 = PO, PS, PW, RV; 2 = three; 1 = one; 0 = none.
- **EX041 — CI checks.** List CI checks on each change. *Rubric:* 3 = tests, static analysis, name check, advisory check; 2 = three; 1 = one; 0 = none.
- **EX042 — Gap found.** What gap did the mapping reveal? *Rubric:* 3 = no secure-coding training (PO); 2 = partial; 1 = none; 0 = none.

### Synthesis

Security belongs in every step of the lifecycle, mapped and checked.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) explain confidentiality, integrity and availability for applications; (2) identify assets, threats and controls; (3) describe the OWASP Top 10 categories; (4) apply defence in depth.

### 15.1 CIA

Confidentiality keeps rider data private; integrity ensures tickets and prices are not altered and that deployed code is what was built; availability keeps ticket sales running. Supply-chain attacks are mainly integrity attacks on code.

### 15.2 Assets and threats

Assets: payment tokens, rider accounts, the build pipeline, signing keys. Threats: criminals seeking payment data, fraudsters seeking free tickets, attackers targeting the pipeline to reach many riders.

### 15.3 OWASP Top 10:2021

The ten categories are Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration, Vulnerable and Outdated Components, Identification and Authentication Failures, Software and Data Integrity Failures, Security Logging and Monitoring Failures, and Server-Side Request Forgery. The tmpl advisory relates to Vulnerable and Outdated Components (A06); the mirror mismatch to Software and Data Integrity Failures (A08).

### 15.4 Controls

Preventive (validation, least privilege), detective (logs, advisory checks) and corrective (patching, rollback).

### 15.5 Defence in depth

No control is perfect; layers mean one failure does not lead to disaster.

### Security requirements early

Kwame learns that fixing a design flaw after release costs far more than avoiding it during design, because code, tests, documentation and users all depend on the design. OWASP Top 10:2021 added Insecure Design (A04) to stress this. Coastline therefore asks security questions in planning meetings, such as "who should be allowed to do this?" and "what happens if this input is wrong?", before any code is written.

### Least privilege principle

Every person and program gets only the access needed for its task, no more.

### Worked example

Kwame classifies Coastline's last year of findings by Top 10 category: most were A01 and A06. Ingrid uses this to prioritise authorisation tests and dependency updating.

> **Synthetic case.** Findings are synthetic.

### Errors and limits

The Top 10 is an awareness document, not a complete standard; use ASVS for verification.

### Exercises

- **EX043 — Integrity attack.** Why are supply-chain attacks mainly integrity attacks? *Rubric:* 3 = alter code that runs; 2 = partial; 1 = none; 0 = none.
- **EX044 — Category mapping.** Map the tmpl advisory and mirror mismatch to Top 10 categories. *Rubric:* 3 = A06 and A08; 2 = one; 1 = none; 0 = none.
- **EX045 — Top 10 limit.** What should be used instead of the Top 10 for verification? *Rubric:* 3 = ASVS; 2 = partial; 1 = none; 0 = none.

### Synthesis

CIA, threats and layered controls frame every later chapter.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) treat an application and its pipeline as one system; (2) define system boundaries and interfaces; (3) trace requirements to components; (4) manage change across the system.

### 16.1 The whole system

ticket-web is not just code: it includes the source repository, CI, artifact storage, deployment, servers, third-party services (payments, maps) and the people who operate them. A weakness anywhere can affect riders. Systems engineering looks at all parts together and at how they connect.

### 16.2 Boundaries

Kwame draws the system boundary: Coastline controls source, CI, mirror and servers; the payment provider and public registry are outside. Interfaces across the boundary (registry downloads, payment API calls) are where trust must be checked, because Coastline cannot inspect what happens beyond them.

### 16.3 Interfaces

Each interface has an owner and a contract: what is sent, how it is authenticated, what happens on failure. The registry interface's contract says downloads must match lockfile hashes; the payment interface's says requests are signed and responses verified.

### 16.4 Traceability

Requirements such as "only reviewed code is deployed" are traced to the components that enforce them (repository branch protection, CI policy, deployment check) and to tests that prove them. A requirement with no traced component is a gap.

### 16.5 Change management

Changes to one part, such as a new CI runner, are checked for effects on others. A change board reviews changes to the pipeline itself, since a pipeline change can affect every future release.

### 16.6 Interfaces as risk

Many supply-chain attacks in the Ladisa et al. (2023) taxonomy target interfaces between stages: source to build, build to distribution, distribution to install.

### Worked example

Kwame's traceability table finds that "only reviewed code is deployed" is enforced by branch protection, but an emergency hotfix path in the deployment tool skips the check. The team keeps the hotfix path but requires a second approver and an after-the-fact review within 24 hours.

> **Synthetic case.** The system and table are synthetic.

### Errors and limits

Large systems change constantly; keep diagrams and tables current or they mislead.

### Exercises

- **EX046 — System parts.** List five parts of the ticket-web system. *Rubric:* 3 = source, CI, artifacts, deployment, servers, third parties, people (five); 2 = three; 1 = one; 0 = none.
- **EX047 — Traceability gap.** What does a requirement with no traced component mean? *Rubric:* 3 = a gap; 2 = partial; 1 = none; 0 = none.
- **EX048 — Hotfix fix.** How was the hotfix path handled? *Rubric:* 3 = second approver; review within 24 h; 2 = partial; 1 = none; 0 = none.

### Synthesis

See the application and its pipeline as one system with owned, checked interfaces.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) explain feedback loops in engineering; (2) apply feedback to security processes; (3) recognise delays and oscillation; (4) design stable improvement loops.

### 17.1 Feedback loops

A controller measures an output, compares it with a target and adjusts. A thermostat measures temperature and switches heating. Security processes are loops too: measure open advisories, compare with targets, adjust effort.

### 17.2 The advisory loop

Coastline's target: no critical advisory open more than 7 days. Each morning, the advisory check reports open items; the team adjusts priorities. The loop's sensor is the SBOM-based check (chapter 24); its actuator is engineering time.

### 17.3 Delays

Feedback with long delays causes trouble. If the advisory report were monthly, problems would be found late and fixes would come in bursts. Daily reports shorten the loop.

### 17.4 Oscillation

Overreacting causes swings: one week everyone drops features to fix low-severity items, the next week nothing gets fixed. Clear thresholds and steady capacity keep the loop stable.

### 17.5 Positive feedback

Some loops amplify: more noise leads to ignoring alerts, which leads to more unresolved items and more noise. Recognising such loops helps break them early.

### 17.6 Measuring the loop

The loop's performance is measured by time to remediate, studied in chapter 29.

### Setting targets

Targets come from risk: 7 days for critical, 30 for high and 90 for medium advisories. They are reviewed yearly. Targets that are never met are not useful signals, and targets that are always easily met may be too loose; Kwame plots the share met each month to see whether the targets still drive the right behaviour.

### Worked example

After Coastline reduces noise by removing duplicate advisories (the same flaw reported by two sources), the daily list shrinks from 40 to 12 items and the team clears criticals within the target for three months running.

> **Synthetic case.** Targets and counts are synthetic.

### Errors and limits

Process loops involve people, who are less predictable than machines; use loops as a guide.

### Exercises

- **EX049 — Loop parts.** Name the sensor and actuator of the advisory loop. *Rubric:* 3 = SBOM-based check; engineering time; 2 = one; 1 = none; 0 = none.
- **EX050 — Delay effect.** What happens with long feedback delays? *Rubric:* 3 = late discovery, fixes in bursts; 2 = partial; 1 = none; 0 = none.
- **EX051 — Noise fix.** What reduced the daily list from 40 to 12? *Rubric:* 3 = removing duplicate advisories; 2 = partial; 1 = none; 0 = none.

### Synthesis

Short, stable feedback loops keep security work under control.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) design layered security for a web application and pipeline; (2) apply trust boundaries and least privilege; (3) choose architectural controls for supply-chain integrity; (4) document architecture decisions.

### 18.1 Layers

Coastline's architecture has edge protection (a web application firewall and rate limits), the application (validation, authorisation, escaping), data (encryption, least privilege) and pipeline (reviewed source, isolated builds, signed artifacts, verified deployment).

### 18.2 Trust boundaries

Boundaries separate zones of different trust: internet to web tier, web tier to database, CI to production. Every boundary has checks. Secrets for production are never available to pull-request builds from untrusted branches.

### 18.3 Pipeline architecture

Source changes are reviewed; builds run on hosted, isolated runners; outputs are signed; provenance records who built what from which source; deployment verifies signature and provenance. This follows the SLSA v1.0 model of build provenance and in-toto's idea (Torres-Arias et al., 2019) of recording and checking each step.

### 18.4 Signing

Signing proves who published an artifact. Sigstore (Newman et al., 2022) offers signing with short-lived certificates tied to identities, avoiding long-lived keys that can leak.

### 18.5 Decisions

Each choice has a decision record: options, trade-offs, chosen design.

### 18.6 Threat of the builder

Thompson (1984) reminds architects that build tools themselves must be trusted; Coastline pins its build tools by digest and rebuilds them from known sources where possible.

### Network segmentation

Servers are placed in separate network segments for web, application, database and build. Firewall rules between segments allow only the flows in the data model. If one segment is compromised, the attacker cannot freely reach the others, and unexpected connections are logged.

### Worked example

Kwame's architecture review shows that the staging environment shares a database account with production for reporting. The team splits the accounts, so a staging compromise cannot read production data.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Architecture on paper may differ from reality; verify with configuration reviews.

### Exercises

- **EX052 — Pipeline steps.** List the pipeline integrity steps. *Rubric:* 3 = review, isolated builds, signing, provenance, verified deployment; 2 = four; 1 = two; 0 = none.
- **EX053 — Sigstore benefit.** What does Sigstore avoid? *Rubric:* 3 = long-lived keys that can leak; 2 = partial; 1 = none; 0 = none.
- **EX054 — Staging finding.** What did the review find and fix? *Rubric:* 3 = shared DB account; split; 2 = partial; 1 = none; 0 = none.

### Synthesis

Layer controls across application, data and pipeline, with checked trust boundaries.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) explain hashing, signing and encryption for software integrity; (2) verify artifacts against published digests; (3) compare digests safely; (4) manage keys and identities for build systems.

### 19.1 Hashes

A cryptographic hash such as SHA-256 maps any data to a fixed-length digest; any change gives a different digest. Publishing the digest lets anyone check an artifact.

### Lab — Lab — verifying an artifact

```python
"""Verify a build artifact's SHA-256 against the published digest using a constant-time compare."""
import hashlib, hmac
artifact = b"ticket-web 3.2.0 build output (synthetic)"
published = hashlib.sha256(b"ticket-web 3.2.0 build output (synthetic)").hexdigest()
tampered = artifact + b" extra"
for name, blob in (("release", artifact), ("mirror copy", tampered)):
    ok = hmac.compare_digest(hashlib.sha256(blob).hexdigest(), published)
    print(f"{name:12} {'VERIFIED' if ok else 'DIGEST MISMATCH - do not deploy'}")
```

Run with `python3 lab_hash.py`. Verified output:

```text
release      VERIFIED
mirror copy  DIGEST MISMATCH - do not deploy
```

### 19.2 Lab result

The release copy matches its published digest and is verified. The mirror copy, with extra bytes, gives a digest mismatch and is marked "do not deploy". The lab uses hmac.compare_digest, a constant-time comparison, a good habit when comparing secrets and a safe default for digests.

### 19.3 Signatures

A digest proves the file matches a reference, but who published the reference? A digital signature binds the digest to an identity. Deployment checks both.

### 19.4 Keys and identities

Build signing uses short-lived credentials issued to the CI identity, not personal keys. Developers sign in with multi-factor authentication; OWASP Top 10:2021 A07 covers identification and authentication failures.

### 19.5 Encryption

Encryption protects confidentiality, for example of backups and network traffic; it is not the same as integrity protection.

### 19.6 Key management

Keys are stored in a managed key service, rotated and access-logged.

### Rotation and revocation

Credentials are rotated on a schedule and revoked at once when staff leave or a leak is suspected.

### Audit trail

Every signing event is logged with the CI job, commit and time.

### Worked example

Kwame adds digest verification to the deploy script for ticket-web. In the first month it blocks one deployment, from an outdated cache holding an older build with the same version label. The label was reused by mistake; Coastline adds a rule that version labels can never be reused.

> **Synthetic case.** Artifacts and digests are synthetic.

### Errors and limits

A digest check is only as good as the source of the expected digest; protect that source.

### Exercises

- **EX055 — Lab result.** What did the lab report for the two copies? *Rubric:* 3 = release VERIFIED; mirror MISMATCH do not deploy; 2 = partial; 1 = none; 0 = none.
- **EX056 — Signature purpose.** What does a signature add to a digest? *Rubric:* 3 = binds to publisher identity; 2 = partial; 1 = none; 0 = none.
- **EX057 — Blocked deploy.** What did the deploy check block? *Rubric:* 3 = outdated cache build with reused label; no reuse rule; 2 = partial; 1 = none; 0 = none.

### Synthesis

Hashes, signatures and managed identities let you trust what you deploy.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Application and software supply chain security: engineering context

### Learning outcomes

You will (1) describe the software supply chain from source to user; (2) identify actors and stages; (3) relate known attack classes to stages; (4) place Coastline's controls on the chain.

### 20.1 The chain

Source code is written, reviewed and stored; dependencies are fetched; code is built; artifacts are stored and distributed; software is deployed and updated. Each stage has actors: developers, maintainers, registries, CI providers and operators.

### 20.2 Attack classes

Ohm et al. (2020) and Ladisa et al. (2023) describe attacks such as malicious packages, compromised maintainer accounts, tampering with build systems and substituting artifacts during distribution. This course stays defensive: it uses these classes to decide where controls belong, not to describe how to carry attacks out.

### 20.3 Coastline's controls

Source: branch protection and review. Dependencies: lockfiles, name checks, mirror, advisory checks. Build: isolated hosted runners, pinned tools. Artifacts: signing, provenance, digest checks. Deployment: verification policy. Operation: monitoring and update process.

### 20.4 Standards

SLSA v1.0 describes build track levels with increasing provenance and isolation guarantees; the SSDF (SP 800-218) practice PS.2 asks producers to provide a way to verify release integrity; ASVS includes requirements on components and configuration.

### 20.5 Open source realities

Wermke et al. (2022) found that open-source projects vary widely in security practices and rely heavily on trust in contributors. Consumers like Coastline cannot assume upstream controls exist.

### 20.6 Engineering context

Supply chain security is an engineering problem: it requires requirements, design, measurement and verification like any other system property.

### Responsibility

Coastline names an owner for each stage of its chain, so every control has someone who maintains it.

### Worked example

Kwame's chain diagram shows one gap: the mobile app's build is done on a developer's laptop, not CI. Coastline moves it to hosted CI within a month.

> **Synthetic case.** Controls and gaps are synthetic.

### Errors and limits

A chain diagram simplifies; real chains include tools, plugins and services not shown.

### Exercises

- **EX058 — Chain stages.** List the stages of the software supply chain. *Rubric:* 3 = source, dependencies, build, artifacts, distribution, deployment/update; 2 = four; 1 = two; 0 = none.
- **EX059 — SSDF PS.2.** What does SSDF PS.2 ask? *Rubric:* 3 = way to verify release integrity; 2 = partial; 1 = none; 0 = none.
- **EX060 — Mobile gap.** What gap did the diagram show? *Rubric:* 3 = mobile build on laptop; moved to CI; 2 = partial; 1 = none; 0 = none.

### Synthesis

Map the chain, its actors and controls, then engineer the gaps closed.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Application and software supply chain security: requirements

### Learning outcomes

You will (1) write verifiable security requirements for an application and its pipeline; (2) derive requirements from standards and threats; (3) prioritise requirements; (4) define acceptance tests.

### 21.1 Sources of requirements

Requirements come from threats (what could go wrong), standards (ASVS, SSDF, SLSA), law and contracts (payment card rules) and incidents (the mirror mismatch, the tmpl advisory).

### 21.2 Writing them well

A good requirement is specific and testable: "Deployment shall refuse any artifact whose SHA-256 digest does not match the signed build record" rather than "artifacts shall be secure".

### 21.3 Application requirements

Using ASVS as a base, Coastline selects requirements for authentication, access control, validation, output encoding and logging. ASVS 4.0.3 offers three levels; Coastline targets Level 2 for ticket-web because it handles payments. ASVS 5.0.0 keeps the level idea with reorganised chapters, so Kwame records both identifiers.

### 21.4 Pipeline requirements

From SLSA v1.0: builds on a hosted platform, provenance generated by the platform, provenance verified before deployment. From SSDF: PO.3 secure toolchains, PS.1 protect code from unauthorised changes, PS.2 provide verification mechanisms, RV.1 identify vulnerabilities continuously.

### 21.5 Prioritising

Requirements are ranked by risk reduction and effort; must-haves cover the two incidents.

### 21.6 Acceptance tests

Each requirement has a test: e.g., deploy a deliberately mismatched synthetic artifact in staging and confirm refusal.

### Traceability to tests

Each requirement is linked to the tests that prove it and the component that enforces it. When a test fails, the team knows which requirement is at risk. When a requirement changes, the team knows which tests to update. Kwame keeps this link in a simple table in the repository, reviewed with every architecture change.

### Worked example

Kwame's requirement set has 42 items: 30 application (from ASVS), 12 pipeline (SLSA and SSDF). Ingrid approves 35 for this year and schedules 7 for next.

> **Synthetic case.** Requirement counts are synthetic.

### Errors and limits

Requirements lists grow; review yearly and remove ones that no longer apply.

### Exercises

- **EX061 — Good requirement.** Rewrite "artifacts shall be secure" as testable. *Rubric:* 3 = refuse artifact whose digest mismatches signed record; 2 = partial; 1 = none; 0 = none.
- **EX062 — ASVS level.** Which ASVS level and why? *Rubric:* 3 = Level 2; handles payments; 2 = partial; 1 = none; 0 = none.
- **EX063 — Acceptance test.** Give the acceptance test for the digest requirement. *Rubric:* 3 = deploy mismatched synthetic artifact in staging; confirm refusal; 2 = partial; 1 = none; 0 = none.

### Synthesis

Derive testable requirements from threats and standards and give each an acceptance test.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Application and software supply chain security: system and data models

### Learning outcomes

You will (1) model the application and pipeline as data flows; (2) identify trust boundaries on the model; (3) model the data that describes software (SBOM, provenance); (4) keep models current.

### 22.1 Data flow diagrams

Shostack (2014) recommends data flow diagrams for threat modelling: external entities, processes, data stores and flows, with trust boundaries drawn across flows. Kwame draws ticket-web: rider browser, web app, database, payment provider; and the pipeline: developer, repository, CI, mirror, artifact store, deployment.

### 22.2 Trust boundaries

Boundaries appear between rider and web app, web app and payment provider, CI and public registry, CI and production. Every flow crossing a boundary is a place to ask what could go wrong.

### 22.3 Software as data

An SBOM lists components and versions; NTIA (2021) defined minimum elements: supplier, component name, version, unique identifiers, dependency relationship, author of SBOM data and timestamp. Provenance records how an artifact was built. These are data models the pipeline produces and consumes.

### 22.4 Linking models

Each deployed artifact links to its SBOM and provenance by digest. Given a running server, the team can find exactly which components it contains.

### 22.5 Model upkeep

Models are stored with the code and updated in the same pull request as architecture changes.

### 22.6 Simplicity

Models should be just detailed enough to support decisions; a diagram nobody can read helps nobody.

### Verifying flows

Kwame compares the diagram with network logs from the build environment, confirming each logged connection appears in the model.

### Model ownership

Ingrid's team owns the models and reviews them every quarter.

### Worked example

The data flow diagram shows a flow Kwame had missed: CI sends build logs to a third-party log service. Logs may contain environment details. The team reviews log content and masks sensitive values.

> **Synthetic case.** Diagrams and flows are synthetic.

### Errors and limits

Diagrams describe intended behaviour; actual flows must be verified with network and configuration evidence.

### Exercises

- **EX064 — DFD elements.** Name the four DFD element types. *Rubric:* 3 = external entities, processes, data stores, flows; 2 = three; 1 = one; 0 = none.
- **EX065 — NTIA elements.** List four NTIA SBOM minimum elements. *Rubric:* 3 = supplier, name, version, identifiers, relationship, author, timestamp (four); 2 = two; 1 = one; 0 = none.
- **EX066 — Missed flow.** What flow was missed and fixed? *Rubric:* 3 = CI logs to third-party service; masked values; 2 = partial; 1 = none; 0 = none.

### Synthesis

Model flows, boundaries and software metadata, and keep the models current.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Application and software supply chain security: threat and failure analysis

### Learning outcomes

You will (1) apply STRIDE to the system model; (2) analyse failure modes of pipeline components; (3) rank threats and failures; (4) link each to controls.

### 23.1 STRIDE

Shostack (2014) describes STRIDE: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service and Elevation of privilege. Kwame applies it to each element and flow in the model.

### 23.2 Examples

Spoofing: a fake package with a lookalike name. Tampering: an altered artifact on the mirror. Repudiation: a deployment without a record of who approved it. Information disclosure: secrets in build logs. Denial of service: registry outage stopping builds. Elevation of privilege: a pull request from an untrusted fork gaining access to production secrets.

### 23.3 Failure modes

Failure mode and effects analysis asks how each component can fail without an attacker: mirror corruption, CI outage, expired signing certificates, clock errors breaking certificate checks.

### 23.4 Ranking

Each threat or failure is rated for likelihood and impact on a 1–3 scale; the product ranks them.

### 23.5 Linking to controls

Each high-ranked item must have a control and a test. Untracked items are risks recorded for management.

### 23.6 Review

The analysis is revisited when the architecture changes and after incidents.

### Abuse cases

For the most important features, the team writes short abuse cases alongside user stories: how might someone misuse the refund feature or the ticket transfer? Abuse cases guide tests and controls without describing attack techniques in detail. They help product managers understand why some features need extra checks, such as a limit on refunds per day.

### Residual risk

Items without full controls are reported to management as accepted or planned risks.

### Worked example

Top-ranked items: untrusted fork pull requests reaching secrets (likelihood 2, impact 3), mirror tampering (2, 3) and expired signing certificates stopping releases (3, 2). Controls exist for the first two; for the third, the team adds certificate expiry monitoring with 30 days' warning.

> **Synthetic case.** Ratings are synthetic.

### Errors and limits

STRIDE prompts thinking but does not guarantee completeness.

### Exercises

- **EX067 — STRIDE letters.** What does STRIDE stand for? *Rubric:* 3 = spoofing, tampering, repudiation, information disclosure, DoS, elevation of privilege; 2 = five; 1 = three; 0 = none.
- **EX068 — Fork threat.** Which STRIDE category is the untrusted fork case? *Rubric:* 3 = elevation of privilege; 2 = partial; 1 = none; 0 = none.
- **EX069 — New control.** What control was added for certificate expiry? *Rubric:* 3 = monitoring with 30 days' warning; 2 = partial; 1 = none; 0 = none.

### Synthesis

STRIDE and failure analysis turn models into ranked, controlled risks.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Application and software supply chain security: methods I

### Learning outcomes

You will (1) generate and use an SBOM; (2) match components to advisories with version ranges; (3) prioritise affected components; (4) integrate the check into CI.

### 24.1 Generating SBOMs

CI generates an SBOM for every build from the lockfile and build metadata, in a standard format, stored with the artifact.

### 24.2 Matching advisories

Advisories list affected version ranges and fixed versions. Matching must compare versions numerically, not as text: "2.0.9" is lower than "2.0.10".

### Lab — Lab — SBOM against advisories

```python
"""Match SBOM components to synthetic advisories with affected version ranges."""
def v(s): return tuple(int(x) for x in s.split("."))
sbom = {"webfw": "4.1.2", "tmpl": "2.0.9", "zipx": "1.3.0", "decimal-x": "0.9.4", "imgkit": "5.2.1"}
advisories = [("ADV-101", "tmpl", "2.0.0", "2.0.10"), ("ADV-102", "zipx", "1.0.0", "1.2.5"),
              ("ADV-103", "imgkit", "5.0.0", "5.2.2"), ("ADV-104", "webfw", "3.0.0", "3.9.9")]
for aid, pkg, lo, fixed in advisories:
    have = sbom.get(pkg)
    hit = have and v(lo) <= v(have) < v(fixed)
    print(f"{aid} {pkg:7} installed {have} affected [{lo}, {fixed}) -> {'AFFECTED, upgrade to ' + fixed if hit else 'not affected'}")
```

Run with `python3 lab_sbom.py`. Verified output:

```text
ADV-101 tmpl    installed 2.0.9 affected [2.0.0, 2.0.10) -> AFFECTED, upgrade to 2.0.10
ADV-102 zipx    installed 1.3.0 affected [1.0.0, 1.2.5) -> not affected
ADV-103 imgkit  installed 5.2.1 affected [5.0.0, 5.2.2) -> AFFECTED, upgrade to 5.2.2
ADV-104 webfw   installed 4.1.2 affected [3.0.0, 3.9.9) -> not affected
```

### 24.3 Lab result

Two of four advisories apply: ADV-101 affects tmpl 2.0.9 (fixed in 2.0.10) and ADV-103 affects imgkit 5.2.1 (fixed in 5.2.2). zipx 1.3.0 is past its fixed version 1.2.5, and webfw 4.1.2 is outside ADV-104's range. Note that comparing "2.0.9" and "2.0.10" as text would wrongly suggest 2.0.9 is newer.

### 24.4 Prioritising

Not every affected component is equally urgent. Kwame considers severity, whether the vulnerable function is reachable in ticket-web, and the exploitation likelihood estimated by EPSS (Jacobs et al., 2021). imgkit is isolated (chapter 8), which reduces its urgency; tmpl renders every page, so it goes first.

### 24.5 In CI

The check runs on every build and nightly against the current release, because new advisories appear for unchanged code.

### Handling false matches

Sometimes an advisory names a component but the affected function is in an optional module Coastline does not install. The team records a short justification and marks the advisory not applicable, with a review date. These records prevent the same question being asked every night.

### Reporting

Nightly results go to the team chat with links to each advisory and owner.

### Worked example

The nightly run flags ADV-103 for imgkit two days after publication. The team upgrades within 6 days, inside the 30-day high-severity target, and documents that isolation limited the risk meanwhile.

> **Synthetic case.** SBOM and advisories are synthetic.

### Errors and limits

Advisory data can be late or wrong; SBOMs can miss vendored or copied code.

### Exercises

- **EX070 — Version comparison.** Why compare versions numerically? *Rubric:* 3 = text order wrong: 2.0.9 vs 2.0.10; 2 = partial; 1 = none; 0 = none.
- **EX071 — Lab hits.** Which advisories applied? *Rubric:* 3 = ADV-101 tmpl, ADV-103 imgkit; 2 = one; 1 = none; 0 = none.
- **EX072 — Priority reasoning.** Why fix tmpl before imgkit? *Rubric:* 3 = tmpl renders every page; imgkit isolated; 2 = partial; 1 = none; 0 = none.

### Synthesis

SBOMs plus correct version matching and context-aware prioritisation make advisories actionable.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) work in a team on a supply-chain design problem; (2) produce alternative designs; (3) critique designs against requirements; (4) present a recommendation.

### 25.1 The brief

Kwame's studio team of four receives a brief from Coastline: design how the mobile ticket app, now built in CI, should be signed, verified and updated, meeting the requirements from chapter 21.

### 25.2 Alternatives

Option A: traditional long-lived signing key in a hardware module. Option B: keyless signing with short-lived certificates tied to the CI identity (the Sigstore model). Option C: platform app-store signing only.

### 25.3 Critique

Against requirements: A is strong but needs key ceremonies and rotation; B reduces key-theft risk and adds a public transparency log but depends on an external service; C is simplest but gives Coastline no independent verification.

### 25.4 Prototype

The team prototypes B with synthetic artifacts in a test environment, measuring time added to builds (about 20 seconds).

### 25.5 Presentation

Ten minutes to Ingrid and two Coastline engineers, with the requirement table, risks and recommendation.

### 25.6 Peer review

Another studio team reviews the design and asks how verification works offline on buses with no signal; the team adds cached verification material.

### Team roles

Each studio team assigns a lead, a requirements owner, a prototype builder and a reviewer, rotating in the next studio. Roles make sure no part of the design is forgotten and give each student practice in different responsibilities. Kwame acts as requirements owner, keeping the table current as the design changes.

### Reflection

After the studio, each student writes one page on what they learned and would change.

### Worked example

The team recommends B combined with C: app-store signing for distribution plus keyless signing and provenance for Coastline's own verification. Ingrid accepts it for a pilot.

> **Synthetic case.** The studio brief and results are synthetic.

### Errors and limits

Studio prototypes are simplified; production adds monitoring and recovery.

### Exercises

- **EX073 — Three options.** Describe the three options. *Rubric:* 3 = HSM long-lived key; keyless short-lived; app store only; 2 = two; 1 = one; 0 = none.
- **EX074 — Option C weakness.** Why is option C weak alone? *Rubric:* 3 = no independent verification; 2 = partial; 1 = none; 0 = none.
- **EX075 — Offline question.** What did peer review raise and how was it addressed? *Rubric:* 3 = offline verification on buses; cached material; 2 = partial; 1 = none; 0 = none.

### Synthesis

Compare alternatives against requirements, prototype and accept critique.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Application and software supply chain security: architecture alternatives

### Learning outcomes

You will (1) compare architectural options for dependency management and build integrity; (2) evaluate trade-offs in cost, risk and usability; (3) use evidence from the literature to justify choices; (4) record decisions.

### 26.1 The question

How should ticket-web obtain dependencies? Option 1: fetch directly from the public registry with lockfile hashes. Option 2: an internal mirror that proxies and caches the registry. Option 3: a curated internal repository where each new package version is reviewed before use.

### 26.2 Risk trade-offs

Option 1 is simple but depends on the registry's availability and offers no central control point. Option 2 adds caching, logging and a place for checks, with modest cost. Option 3 gives the most control but slows updates, which can lengthen exposure to known flaws; Kula et al. (2018) showed that update friction already causes lag, and Decan et al. (2018) showed how lag spreads vulnerabilities.

### 26.3 Build options

For builds: self-hosted runners give control but must be maintained and isolated; hosted runners from the CI provider offer fresh, isolated environments and platform-generated provenance aligned with SLSA v1.0 Build Level 2 and above, but depend on the provider.

### 26.4 Reproducibility

Reproducible builds (Lamb and Zacchiroli, 2022) let an independent builder recreate the same bits, detecting tampering in the original build. Coastline evaluates making ticket-web's server build reproducible; it requires fixing timestamps and ordering in the build.

### 26.5 Usability

Developers need fast builds and simple upgrades. A design that slows them down will be worked around, echoing Johnson et al. (2013) on tool adoption.

### 26.6 Decision

Coastline chooses option 2 with automatic checks (name similarity, advisories, licence), hosted runners, and a pilot of reproducible server builds.

### Worked example

Kwame's decision record compares the three options in a table of control, cost, update speed and availability. He estimates option 3 would add about 5 days to the median time to adopt a fix, unacceptable given the 7-day critical target.

> **Synthetic case.** Options, estimates and decisions are synthetic.

### Errors and limits

Architecture choices depend on organisation size; a small team may not sustain a curated repository.

### Exercises

- **EX076 — Option 3 cost.** Why was the curated repository rejected? *Rubric:* 3 = slows updates; ~5 days; critical target; 2 = partial; 1 = none; 0 = none.
- **EX077 — Hosted runner benefit.** What do hosted runners provide? *Rubric:* 3 = fresh isolated environments; platform provenance; 2 = partial; 1 = none; 0 = none.
- **EX078 — Reproducibility need.** What does reproducibility require for ticket-web? *Rubric:* 3 = fix timestamps and ordering; 2 = partial; 1 = none; 0 = none.

### Synthesis

Choose architectures that balance control, update speed and usability, with recorded evidence.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Application and software supply chain security: control design

### Learning outcomes

You will (1) design specific controls for source, dependencies, build and deployment; (2) define policies as code; (3) specify failure behaviour of controls; (4) plan exceptions.

### 27.1 Source controls

Branch protection requires review by one engineer and passing checks; signed commits for release branches; no direct pushes to main.

### 27.2 Dependency controls

The CI dependency gate fails a build if: a lockfile hash does not match, a new name is within edit distance 1 of a popular name without an approved review, or a critical advisory applies without an exception.

### 27.3 Build controls

Builds run on hosted runners with pinned tool versions; production secrets are not available to builds from forks; the platform generates provenance.

### 27.4 Deployment controls

The deploy policy allows an artifact only if built by the approved builder from the approved repository from reviewed commits, with a valid signature and matching digest. Policies are written as code, version-controlled and reviewed like application code.

### 27.5 Failure behaviour

Controls fail closed: if the advisory service is unreachable, the build waits and retries rather than skipping the check; after one hour, the on-call engineer is paged.

### 27.6 Exceptions

Exceptions need an owner, a reason, an expiry date and approval by Ingrid. Expired exceptions block builds again.

### Policy testing

Policies are code, so they have tests: for each rule, a synthetic input that should pass and one that should fail. A change to the deploy policy that accidentally allowed any builder would fail the test suite before review.

### Worked example

In the first week, the dependency gate blocks 6 builds: 4 for a critical advisory in a test-only library (exception granted for 14 days because it never ships), 1 for a lookalike name (a typo, corrected) and 1 for a hash mismatch caused by a developer editing the lockfile by hand.

> **Synthetic case.** Policies and events are synthetic.

### Errors and limits

Strict controls create pressure for exceptions; track the exception count as a health signal.

### Exercises

- **EX079 — Fail closed.** What happens if the advisory service is down? *Rubric:* 3 = build waits/retries; page after 1 h; 2 = partial; 1 = none; 0 = none.
- **EX080 — Exception rules.** What does an exception need? *Rubric:* 3 = owner, reason, expiry, approval; 2 = three; 1 = one; 0 = none.
- **EX081 — Week one blocks.** Summarise the six blocks. *Rubric:* 3 = 4 test-only advisory (exception), 1 lookalike typo, 1 hand-edited lockfile; 2 = partial; 1 = one; 0 = none.

### Synthesis

Write controls as reviewed policy, make them fail closed and govern exceptions.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Application and software supply chain security: implementation I

### Learning outcomes

You will (1) implement output encoding and authorisation checks in the application; (2) fix the tmpl advisory safely; (3) implement the dependency gate; (4) review implementation for regressions.

### 28.1 Output encoding

Cross-site scripting (CWE-79) happens when untrusted data is placed into pages without encoding for its context. The fixed tmpl version escapes attributes by default. Kwame also adds a test that renders synthetic rider names with special characters and checks they appear as text, not markup.

### 28.2 Authorisation

Every endpoint calls a central authorisation function with the user's role and the resource owner. Checks happen on the server, aligned with OWASP Top 10:2021 A01 and ASVS access-control requirements.

### 28.3 Upgrading tmpl

The upgrade from 2.0.9 to 2.0.10 is small but changes one default. Tests catch two templates that relied on unescaped output for trusted icons; they are rewritten to use an explicit safe-markup helper reviewed by Ingrid.

### 28.4 Implementing the gate

The dependency gate is a small CI step reading the lockfile and SBOM, calling the advisory feed and the name-similarity check, and applying the policy. Its own code is reviewed and tested.

### 28.5 Regression review

After the changes, a reviewer compares rendered pages before and after and runs the authorisation test suite.

### 28.6 Rollback plan

Each release can be rolled back to the previous signed artifact within ten minutes.

### Code review focus

Reviewers check that new endpoints call the central authorisation function and that templates do not use the safe-markup helper without a comment explaining why the content is trusted. A simple search in CI lists every use of the helper for the reviewer.

### Worked example

The tmpl upgrade ships three days after the advisory, faster than the 11 days of the original incident, because the gate flagged it immediately and tests made the change safe.

> **Synthetic case.** Code changes and timings are synthetic.

### Errors and limits

Explicit safe-markup helpers can be misused; restrict and review their use.

### Exercises

- **EX082 — XSS defence.** What prevents cross-site scripting here? *Rubric:* 3 = context encoding by default; tests with special characters; 2 = partial; 1 = none; 0 = none.
- **EX083 — Upgrade issue.** What did the tmpl upgrade break and how was it fixed? *Rubric:* 3 = two templates relying on unescaped icons; safe-markup helper; 2 = partial; 1 = none; 0 = none.
- **EX084 — Speed gain.** Why was this fix faster than the original incident? *Rubric:* 3 = gate flagged at once; tests; 2 = partial; 1 = none; 0 = none.

### Synthesis

Implement defaults that encode and authorise, and upgrade with tests behind you.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Application and software supply chain security: measurement

### Learning outcomes

You will (1) define security metrics for application and supply chain; (2) compute remediation times against targets; (3) identify late items and causes; (4) report metrics without perverse incentives.

### 29.1 What to measure

Coastline measures time to remediate findings by severity, share of builds with valid provenance, number of active exceptions, and dependency freshness (how many versions behind the latest).

### Lab — Lab — remediation times

```python
"""Median days to remediate synthetic findings by severity against targets."""
from statistics import median
targets = {"critical": 7, "high": 30, "medium": 90}
found = {"critical": [2, 5, 9], "high": [12, 20, 41, 18, 33], "medium": [60, 75, 120, 44]}
for sev, days in found.items():
    late = sum(d > targets[sev] for d in days)
    print(f"{sev:8} n={len(days)} median={median(days)} target={targets[sev]} late={late}")
```

Run with `python3 lab_fixtime.py`. Verified output:

```text
critical n=3 median=5 target=7 late=1
high     n=5 median=20 target=30 late=2
medium   n=4 median=67.5 target=90 late=1
```

### 29.2 Lab result

Critical: three findings, median 5 days, one late (9 days against a 7-day target). High: five findings, median 20 days, two late (41 and 33 against 30). Medium: four findings, median 67.5 days, one late (120 against 90).

### 29.3 Late items

The late critical item waited for a vendor patch; the late highs needed a framework upgrade that took two sprints. Measuring lateness leads to the cause, not blame.

### 29.4 Perverse incentives

If teams are rewarded only for closing fast, they may downgrade severities. Coastline reviews severity changes monthly.

### 29.5 Freshness

The median dependency is one minor version behind; two are more than two major versions behind and planned for replacement.

### Reading the dashboard

The dashboard shows each metric as a trend over six months with targets as lines. Items behind target are listed by name with owners. Ingrid reviews it weekly with the team, asking about causes rather than people; the review takes 15 minutes and ends with at most three actions. Kwame finds that showing named items, not just numbers, gets them fixed faster because owners see their work.

### Sharing metrics

Monthly summaries go to Coastline's leadership with a short explanation of trends.

### Worked example

Kwame's dashboard shows provenance on 100% of server builds and 80% of mobile builds (the remaining 20% are older releases built before the CI move). Ingrid sets a goal to retire those releases.

> **Synthetic case.** All measurements are synthetic.

### Errors and limits

Small counts make medians unstable; show the individual items too.

### Exercises

- **EX085 — Lab late items.** How many items were late in each severity? *Rubric:* 3 = critical 1, high 2, medium 1; 2 = two; 1 = one; 0 = none.
- **EX086 — Critical cause.** Why was the critical item late? *Rubric:* 3 = waited for vendor patch; 2 = partial; 1 = none; 0 = none.
- **EX087 — Incentive control.** How are perverse incentives controlled? *Rubric:* 3 = monthly review of severity changes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure remediation, provenance and freshness, find causes and guard against gaming.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) write unit tests for security rules; (2) test boundaries and negative cases; (3) run tests in CI; (4) interpret test results.

### 30.1 Why test security rules

Security rules, such as who may issue a refund, are business logic that can break silently. Tests make the intended behaviour explicit and catch regressions.

### Lab — Lab — refund authorisation tests

```python
"""Authorisation unit tests for a synthetic fare-refund function."""
import io, unittest
def can_refund(role, amount):
    return role == "agent" and amount <= 50 or role == "supervisor"
class T(unittest.TestCase):
    def test_rider_cannot(self): self.assertFalse(can_refund("rider", 5))
    def test_agent_small(self): self.assertTrue(can_refund("agent", 50))
    def test_agent_large(self): self.assertFalse(can_refund("agent", 51))
    def test_supervisor(self): self.assertTrue(can_refund("supervisor", 500))
r = unittest.TextTestRunner(stream=io.StringIO()).run(unittest.defaultTestLoader.loadTestsFromTestCase(T))
print("tests run:", r.testsRun, "failures:", len(r.failures), "errors:", len(r.errors))
```

Run with `python3 lab_unittest.py`. Verified output:

```text
tests run: 4 failures: 0 errors: 0
```

### 30.2 Lab result

Four tests run and all pass: a rider cannot refund, an agent can refund 50 but not 51, a supervisor can refund 500. The 50/51 pair tests the boundary exactly.

### 30.3 Negative cases

Tests that check something is refused are as important as tests that check something is allowed. Two of the four lab tests are negative.

### 30.4 In CI

The tests run on every change; a failure blocks merging. Coverage reports show which authorisation branches are exercised.

### 30.5 Mutation thinking

Kwame changes "<= 50" to "< 50" in a scratch copy: the agent-small test fails, proving the test detects that mistake.

### Test naming

Each test name states the rule in plain words, such as test_agent_large. When a test fails, the name tells the developer which rule broke without opening the code. Kwame adds a short docstring to each test linking it to the ASVS access-control requirement it checks, so auditors can trace requirements to evidence and developers understand why the rule exists.

### Test data

Tests use synthetic riders and amounts only, never copies of real data. A small factory function creates test users with chosen roles, which keeps tests short and readable.

### Worked example

A later change adds a "senior agent" role with a 200 limit. The developer adds two tests (200 allowed, 201 refused) before writing the code, and the review checks that the old tests still pass.

> **Synthetic case.** Code and tests are synthetic.

### Errors and limits

Passing tests show the cases written work; they do not prove no other path exists.

### Exercises

- **EX088 — Lab results.** What did the lab report? *Rubric:* 3 = 4 run, 0 failures, 0 errors; 2 = partial; 1 = none; 0 = none.
- **EX089 — Boundary pair.** Which tests check the boundary? *Rubric:* 3 = agent 50 allowed, 51 refused; 2 = partial; 1 = none; 0 = none.
- **EX090 — Mutation check.** What did changing <= to < show? *Rubric:* 3 = test catches it; 2 = partial; 1 = none; 0 = none.

### Synthesis

Test allowed and refused cases at the boundaries, in CI, and check the tests can fail.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Application and software supply chain security: implementation II

### Learning outcomes

You will (1) implement build provenance and signing in CI; (2) implement deployment verification; (3) integrate SBOM storage with artifacts; (4) test the full path end to end.

### 31.1 Provenance in CI

The hosted CI platform generates provenance for each build: builder identity, source repository, commit digest, build steps and output digests. The record is signed by the platform, so a compromised build script cannot forge it, which is the key property of SLSA v1.0's higher build levels.

### 31.2 Signing

The artifact is signed with keyless signing tied to the CI workflow's identity, and the signature is recorded in a transparency log, following the Sigstore model (Newman et al., 2022). Anyone can later check when and by which identity the artifact was signed.

### 31.3 Storage

The artifact, its SBOM, provenance and signature are stored together and linked by the artifact digest. Retention is at least as long as the release is in use, plus one year.

### 31.4 Deployment verification

The deployment tool fetches the artifact and its records, verifies the signature, checks the provenance against policy (chapter 38's lab) and compares digests before installing. Any failure stops the deployment with a clear message.

### 31.5 End-to-end test

A staging pipeline deploys a known-good synthetic artifact and three deliberately flawed ones (wrong digest, wrong builder, missing signature). The test passes only if the first deploys and the others are refused.

### 31.6 Performance

Verification adds 12 seconds to deployment, acceptable for the team.

### Worked example

During the end-to-end test, the missing-signature case deploys successfully: a configuration flag left verification in "warn" mode. The flag is changed to "enforce", the test re-run, and a CI check added that fails if the flag is ever set to warn in production configuration.

> **Synthetic case.** Pipeline and tests are synthetic.

### Errors and limits

Verification proves origin and integrity, not that the source code itself is free of flaws.

### Exercises

- **EX091 — Provenance contents.** What does provenance record? *Rubric:* 3 = builder, repo, commit, steps, output digests; 2 = four; 1 = two; 0 = none.
- **EX092 — Platform signing.** Why must the platform sign provenance? *Rubric:* 3 = build script cannot forge it; 2 = partial; 1 = none; 0 = none.
- **EX093 — Warn mode.** What did the end-to-end test catch? *Rubric:* 3 = verification in warn mode; set enforce; CI check; 2 = partial; 1 = none; 0 = none.

### Synthesis

Generate, store and verify provenance and signatures end to end, and test that failures are refused.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Application and software supply chain security: reliability

### Learning outcomes

You will (1) make security controls reliable; (2) avoid single points of failure in the pipeline; (3) plan for outages of external services; (4) measure control availability.

### 32.1 Reliable controls

A control that often fails gets switched off. The dependency gate and deployment verification must be dependable, with clear errors and quick recovery.

### 32.2 External dependencies

The pipeline depends on the public registry, the advisory feed, the transparency log and the CI provider. Each can fail. The internal mirror covers registry outages; cached advisory data covers short feed outages; verification material is cached for transparency-log outages.

### 32.3 Fail closed, recover fast

Failing closed protects integrity, but long outages block releases. Coastline sets a recovery process: if a check is unavailable for more than four hours and a critical fix must ship, Ingrid can approve a documented manual verification with two engineers.

### 32.4 Measuring availability

The team logs every control failure: cause, duration and effect. Over a quarter the gate was unavailable for 3 hours in total, all due to the advisory feed.

### 32.5 Redundancy

A second advisory source is added, reducing dependence on one feed.

### 32.6 Testing failure

Every quarter the team simulates an outage of each external service in staging to check the fallback works.

### Error messages

When a control fails because of an outage, the message says so plainly and links to the status page, so developers do not waste time thinking their code is wrong. Clear outage messages reduced support questions during the advisory feed outage by more than half.

### Capacity

Build capacity is monitored so checks do not slow when many changes arrive at once.

### Worked example

The quarterly simulation of a transparency-log outage reveals that cached verification material expired after 24 hours. The cache period is extended to 7 days with monitoring of freshness.

> **Synthetic case.** Outages and timings are synthetic.

### Errors and limits

Fallbacks add complexity; keep them simple and tested.

### Exercises

- **EX094 — External dependencies.** List four external services the pipeline depends on. *Rubric:* 3 = registry, advisory feed, transparency log, CI provider; 2 = three; 1 = one; 0 = none.
- **EX095 — Manual path.** When can manual verification be used? *Rubric:* 3 = check down >4 h; critical fix; Ingrid approves; two engineers; 2 = partial; 1 = none; 0 = none.
- **EX096 — Simulation finding.** What did the outage simulation reveal? *Rubric:* 3 = cache expired after 24 h; extended to 7 days; 2 = partial; 1 = none; 0 = none.

### Synthesis

Controls must be reliable, with tested fallbacks that keep integrity.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Application and software supply chain security: safety and resilience

### Learning outcomes

You will (1) plan for compromise of a dependency or the pipeline; (2) design response and recovery for supply-chain incidents; (3) protect riders during incidents; (4) learn from exercises.

### 33.1 Assume compromise

Even with good controls, a dependency or build component may be compromised. Resilience means detecting quickly, limiting damage and recovering to a known-good state.

### 33.2 Response plan

The supply-chain playbook: identify affected artifacts using SBOMs and provenance; stop deployments; roll back to the last known-good signed release; rotate any credentials the compromised component could have reached; notify stakeholders.

### 33.3 Known-good state

Because every artifact is linked to its SBOM and provenance, the team can find the last release that did not include a compromised version and redeploy it.

### 33.4 Rider safety

Ticket sales must continue. A fallback paper-ticket process and the previous app version keep service running.

### 33.5 Exercise

Coastline runs a tabletop: "a widely used package in ticket-web is reported compromised; versions 1.4.2–1.4.3 contained malicious code". Using SBOM search, the team finds that only one release included 1.4.2 and that it was deployed for two days.

### 33.6 Lessons

The exercise shows that credential rotation would take a full day because tokens were scattered; the team consolidates them in the secrets manager.

### Communication

The playbook includes message templates for staff, riders and partners. Riders are told what happened, what Coastline did and whether they need to act. Messages avoid technical jargon and speculation; they are approved by the communications lead and Ingrid before release.

### After the incident

A review within two weeks records lessons, owners and dates.

### Worked example

Kwame times the SBOM search in the exercise: 4 minutes to list every affected release. Before SBOMs, the same question would have required inspecting builds by hand for hours.

> **Synthetic case.** The exercise is synthetic.

### Errors and limits

Rollback restores code but not data altered during compromise; check data integrity too.

### Exercises

- **EX097 — Playbook steps.** List the playbook steps. *Rubric:* 3 = identify via SBOM/provenance; stop deploys; rollback; rotate credentials; notify; 2 = four; 1 = two; 0 = none.
- **EX098 — Exercise finding.** What did SBOM search show in the exercise? *Rubric:* 3 = one release with 1.4.2, deployed two days; 4 minutes; 2 = partial; 1 = none; 0 = none.
- **EX099 — Rotation lesson.** What lesson came from credential rotation? *Rubric:* 3 = scattered tokens; consolidate in secrets manager; 2 = partial; 1 = none; 0 = none.

### Synthesis

Plan for compromise: find, stop, roll back, rotate and keep the service running.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Application and software supply chain security: integration

### Learning outcomes

You will (1) integrate application security and supply-chain controls into one workflow; (2) align teams and tools; (3) avoid duplicated or conflicting checks; (4) manage the developer experience.

### 34.1 One workflow

Developers see one pipeline: tests, static analysis, dependency gate, build with provenance, signing, staging deploy with verification, production deploy with verification. Results appear in one place in the pull request.

### 34.2 Aligning teams

The security team writes policies; the platform team runs the pipeline; product teams own fixes. A weekly meeting resolves conflicts.

### 34.3 Avoiding duplication

Two tools both scanned dependencies with different advisory data, producing contradictory results. The team keeps one as the gate and uses the other only for comparison reports.

### 34.4 Developer experience

Messages explain what failed, why it matters and how to fix it, with links. Median CI time is kept under 12 minutes.

### 34.5 Integration testing

Changes to any control are tested in a staging copy of the pipeline before rollout.

### 34.6 SAMM view

OWASP SAMM v2 (2020) maturity assessment shows Coastline rising in Implementation (secure build, secure deployment) and Verification after integration.

### Documentation

A single developer guide explains every pipeline check, what it protects against and how to fix common failures. The guide is versioned with the pipeline configuration, so it always matches the checks in force. New developers read it in their first week, and the platform team updates it whenever a check changes.

### Metrics for the pipeline

The platform team tracks CI duration, failure causes and flaky tests. Flaky tests are fixed or removed within a week, since they teach developers to ignore failures.

### Worked example

A developer survey after integration shows 78% find failure messages clear, up from 41%, and the number of "how do I fix this" questions in chat halves.

> **Synthetic case.** Survey figures are synthetic.

### Errors and limits

Integration concentrates risk: one pipeline misconfiguration affects all checks; protect pipeline configuration.

### Exercises

- **EX100 — Team roles.** Who owns policies, pipeline and fixes? *Rubric:* 3 = security, platform, product teams; 2 = two; 1 = one; 0 = none.
- **EX101 — Duplication fix.** How was scanner duplication resolved? *Rubric:* 3 = one gate, other comparison only; 2 = partial; 1 = none; 0 = none.
- **EX102 — Survey result.** What did the survey show? *Rubric:* 3 = 78% clear vs 41%; questions halved; 2 = partial; 1 = none; 0 = none.

### Synthesis

Integrate checks into one clear workflow owned by aligned teams.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design a supply-chain improvement for a third-party integration; (2) evaluate vendor software risk; (3) specify contractual and technical controls; (4) present to stakeholders.

### 35.1 The brief

Coastline plans to add a vendor's journey-planning widget to ticket-web. Kwame's team must design how to integrate it safely.

### 35.2 Vendor risk

Questions to the vendor: Do you follow the SSDF? Do you provide SBOMs and signed releases? How fast do you fix vulnerabilities? Do you have a disclosure process?

### 35.3 Technical isolation

Options: include the vendor's script directly in ticket-web pages; host a pinned copy with an integrity hash; or load the widget in a sandboxed frame on a separate domain. The sandboxed frame limits the widget's access to rider data.

### 35.4 Contractual controls

The contract requires notification of security incidents within 48 hours, SBOM delivery with each release and fixing critical flaws within 14 days.

### 35.5 Monitoring

Coastline monitors the widget's domain and versions and alerts on unexpected changes.

### 35.6 Presentation

The team presents to Ingrid, procurement and legal.

### Exit planning

The design also covers removal: if the vendor fails or the relationship ends, the widget can be turned off with a configuration change and the page still works without it. Riders see a simple link to a timetable page instead. Planning exit at the start avoids being locked into a risky supplier.

### Stakeholder questions

Procurement asked about cost; the team showed that sandboxing added no licence fees and only two days of work.

### Approval

Ingrid signs off the design for a three-month pilot.

### Worked example

The team recommends the sandboxed frame with pinned versions plus contract terms. Legal adds a right to audit. The vendor agrees to provide SBOMs quarterly instead of per release; the team accepts this with monitoring as compensation.

> **Synthetic case.** The vendor and terms are synthetic.

### Errors and limits

Contracts help after incidents but do not prevent them; technical isolation is the first control.

### Exercises

- **EX103 — Vendor questions.** List three vendor questions. *Rubric:* 3 = SSDF, SBOM/signing, fix speed, disclosure (three); 2 = two; 1 = one; 0 = none.
- **EX104 — Isolation choice.** Why choose a sandboxed frame? *Rubric:* 3 = limits widget access to rider data; 2 = partial; 1 = none; 0 = none.
- **EX105 — Negotiated outcome.** What compromise was reached on SBOMs? *Rubric:* 3 = quarterly; monitoring compensates; 2 = partial; 1 = none; 0 = none.

### Synthesis

Third-party code needs technical isolation, contractual terms and monitoring.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Application and software supply chain security: performance and scale

### Learning outcomes

You will (1) keep security controls fast as the codebase and team grow; (2) scale SBOM and advisory checks; (3) cache safely; (4) measure the cost of controls.

### 36.1 Growth

Over two years ticket-web grows to 220 components and 30 developers, with 60 builds a day. Checks that took seconds now risk slowing everyone.

### 36.2 Incremental checks

The dependency gate checks only components that changed in a pull request, and a nightly job checks everything. This cut median gate time from 90 to 15 seconds.

### 36.3 Safe caching

Advisory data is cached for one hour; the cache key includes the feed's version so stale data is detected. Caches must never be shared between untrusted pull-request builds and release builds, or a poisoned cache could affect releases.

### 36.4 Parallelism

Tests and checks run in parallel jobs; provenance generation happens once at the end.

### 36.5 Measuring cost

Kwame measures each control's time: tests 6 minutes, static analysis 2, gate 15 seconds, signing 20 seconds, verification 12 seconds. Security controls are under 10% of CI time.

### 36.6 Scale of data

SBOMs for all releases are stored in a searchable index so a question like "which releases contain zipx 1.2.x?" answers in seconds.

### Planning for growth

Kwame projects build volume for the next two years using the growth rates from chapter 1 and sizes the CI capacity accordingly. He also sets a budget: security controls should stay under 10% of CI time. When a new check is proposed, its time cost is measured in staging first, and if it would break the budget, the team looks for ways to make it incremental before adding it.

### Worked example

When a new advisory affects zipx, the index search returns 14 releases in 2 seconds; only the current one is deployed. The team upgrades and confirms no other environments run older releases.

> **Synthetic case.** Sizes and timings are synthetic.

### Errors and limits

Speed optimisations can introduce gaps, such as skipped checks on unchanged components; the nightly full check covers this.

### Exercises

- **EX106 — Incremental check.** How was gate time reduced? *Rubric:* 3 = check changed components; nightly full; 2 = partial; 1 = none; 0 = none.
- **EX107 — Cache rule.** Which caches must never be shared? *Rubric:* 3 = untrusted PR builds and release builds; 2 = partial; 1 = none; 0 = none.
- **EX108 — Control cost.** What share of CI time do security controls take? *Rubric:* 3 = under 10%; 2 = partial; 1 = none; 0 = none.

### Synthesis

Scale checks with incremental work, safe caching and measured cost.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Application and software supply chain security: operations

### Learning outcomes

You will (1) operate the application securely in production; (2) monitor for security events from the app and pipeline; (3) manage patching and configuration; (4) run on-call for security issues.

### 37.1 Monitoring

ticket-web logs authentication events, authorisation failures, input validation rejections and admin actions; the pipeline logs builds, signing and deployments. OWASP Top 10:2021 A09 highlights logging and monitoring failures.

### 37.2 Alerts

Alerts fire on unusual patterns: many authorisation failures from one account, a deployment not from the approved pipeline, or a signature verification failure.

### 37.3 Patching

Servers rebuild weekly from updated base images; the application follows the remediation targets.

### 37.4 Configuration

Configuration is stored as code and compared nightly with running systems; drift is reported.

### 37.5 On-call

A rota covers security alerts outside office hours, with playbooks.

### 37.6 Working with operations

Security events are shared with Coastline's operations centre.

### Incident handover

When an alert needs more than a quick check, the on-call engineer opens an incident record with the timeline, actions and owner, and hands over to the day team with a short summary. Records are kept so patterns across incidents can be studied later. Kwame notices that three of the year's alerts came from manual changes, which supports removing direct server access entirely and making the pipeline the only route to production.

### Reviewing alerts

Every month the team reviews which alerts fired, which were real and which rules need tuning. Rules that never fire are tested to check they still work.

### Access reviews

Production access lists are reviewed every quarter and unused access removed.

### Worked example

An alert fires: a deployment to a staging server not from the pipeline. Investigation shows a developer copied files manually to debug. The server is rebuilt from the pipeline and the developer's direct access to staging servers is removed.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Logs can contain personal data; collect what is needed and protect it.

### Exercises

- **EX109 — Logged events.** List three app events logged for security. *Rubric:* 3 = authentication, authorisation failures, validation rejections, admin actions (three); 2 = two; 1 = one; 0 = none.
- **EX110 — Drift.** What is configuration drift and how is it found? *Rubric:* 3 = running differs from code; nightly comparison; 2 = partial; 1 = none; 0 = none.
- **EX111 — Manual deploy.** What happened with the manual deployment alert? *Rubric:* 3 = developer copied files; rebuilt; access removed; 2 = partial; 1 = none; 0 = none.

### Synthesis

Operate with logs, alerts, drift detection and on-call aligned to the pipeline.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Application and software supply chain security: validation

### Learning outcomes

You will (1) validate that deployed artifacts meet provenance policy; (2) check records against policy rules; (3) investigate denials; (4) show evidence to auditors.

### 38.1 What validation means

Validation checks the real system against requirements: are only artifacts built by the approved builder, from the approved repository, from reviewed commits, running?

### Lab — Lab — provenance policy

```python
"""Check synthetic build provenance records against a deployment policy."""
policy = {"builder": "ci.coastline.example/hosted-runner", "repo": "git.coastline.example/ticket-web"}
records = [{"artifact": "ticket-web-3.2.0", "builder": "ci.coastline.example/hosted-runner", "repo": "git.coastline.example/ticket-web", "commit_reviewed": True},
           {"artifact": "ticket-web-3.2.1", "builder": "laptop-kd", "repo": "git.coastline.example/ticket-web", "commit_reviewed": True},
           {"artifact": "ticket-web-3.2.2", "builder": "ci.coastline.example/hosted-runner", "repo": "git.coastline.example/ticket-web", "commit_reviewed": False}]
for r in records:
    issues = [k for k in policy if r[k] != policy[k]] + ([] if r["commit_reviewed"] else ["unreviewed commit"])
    print(f"{r['artifact']:16} {'ALLOW' if not issues else 'DENY: ' + ', '.join(issues)}")
```

Run with `python3 lab_provenance.py`. Verified output:

```text
ticket-web-3.2.0 ALLOW
ticket-web-3.2.1 DENY: builder
ticket-web-3.2.2 DENY: unreviewed commit
```

### 38.2 Lab result

ticket-web-3.2.0 is allowed. ticket-web-3.2.1 is denied because it was built on "laptop-kd", not the approved hosted runner. ticket-web-3.2.2 is denied because its commit was not reviewed.

### 38.3 Investigating denials

3.2.1 was built during the earlier period before all builds moved to CI; it is retired. 3.2.2 came from an emergency change whose after-the-fact review had not been recorded; the review is completed and the release rebuilt.

### 38.4 Evidence for auditors

A monthly report lists every running artifact and its policy result, with links to provenance. This supports SSDF PS.2 and PS.3 (archive and protect each release).

### 38.5 Continuous validation

The check runs hourly against running servers, not only at deployment.

### Validation coverage

Kwame checks that every production server is included in the hourly validation. A newly added server in a second region was missing because it was not yet in the inventory list. The check now reads the inventory from the same source the deployment tool uses, so new servers are covered automatically and no manual list can fall out of date.

### Exceptions in validation

Any running artifact that fails policy must have an approved exception or be replaced within a week.

### Worked example

The auditor asks how Coastline knows the hosted runner itself was not tampered with. Kwame explains the provider's attestations and Coastline's reliance on the provider's controls, and notes reproducible builds as a future independent check.

> **Synthetic case.** Records are synthetic.

### Errors and limits

Validation depends on trustworthy provenance; if the builder is compromised, records may be false.

### Exercises

- **EX112 — Lab results.** Give the lab's three results. *Rubric:* 3 = 3.2.0 ALLOW; 3.2.1 DENY builder; 3.2.2 DENY unreviewed; 2 = two; 1 = one; 0 = none.
- **EX113 — 3.2.2 fix.** How was 3.2.2 resolved? *Rubric:* 3 = review completed; rebuilt; 2 = partial; 1 = none; 0 = none.
- **EX114 — Auditor answer.** What future check did Kwame mention? *Rubric:* 3 = reproducible builds; 2 = partial; 1 = none; 0 = none.

### Synthesis

Validate continuously that what runs meets the provenance policy, and keep evidence.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Application and software supply chain security: maintainability

### Learning outcomes

You will (1) keep dependencies and controls maintainable over years; (2) plan replacement of abandoned components; (3) reduce dependency count; (4) document ownership.

### 39.1 Abandoned components

A component with no releases for two years and unanswered issues is a risk: flaws may never be fixed. Kwame finds four in ticket-web.

### 39.2 Replacement planning

For each, options are: replace with a maintained alternative, take over maintenance internally, or remove the feature. qr-make is replaced by a maintained library; one small helper is copied in and owned internally.

### 39.3 Reducing dependencies

Some packages are used for one tiny function. Removing them reduces attack surface and update work. Kwame removes 11 such packages.

### 39.4 Ownership

Each dependency has an owning team listed in a file in the repository.

### 39.5 Supporting upstream

Coastline sponsors two critical upstream projects and contributes fixes, recognising findings from Wermke et al. (2022) that open-source maintainers often lack resources.

### 39.6 Control maintenance

Policies and checks are reviewed yearly; obsolete rules are removed.

### Choosing new dependencies

Before adding a new dependency, developers check its maintenance activity, number of maintainers, security policy, licence and size. A short checklist in the pull-request template asks these questions. Small utilities are often better written in a few lines than imported, while complex functions such as cryptography should use well-maintained libraries rather than home-made code.

### Licence checks

Licences of new components are checked automatically, and unusual licences go to legal for review before the component is merged.

### Upgrade rhythm

A fixed weekly slot is reserved for dependency updates, so upgrades never pile up into risky large jumps.

### Worked example

After a year, the component count falls from 220 to 196 and the median versions-behind drops from 1 minor to 0. Update pull requests merge faster because fewer conflicts occur.

> **Synthetic case.** Counts are synthetic.

### Errors and limits

Copying code in means owning its flaws; only copy small, well-understood code.

### Exercises

- **EX115 — Abandoned test.** What marks a component as abandoned? *Rubric:* 3 = no releases 2 years; unanswered issues; 2 = partial; 1 = none; 0 = none.
- **EX116 — Options.** List the three options for abandoned components. *Rubric:* 3 = replace, maintain internally, remove feature; 2 = two; 1 = one; 0 = none.
- **EX117 — Year outcome.** What changed after a year? *Rubric:* 3 = 220 to 196; versions-behind to 0; 2 = partial; 1 = none; 0 = none.

### Synthesis

Maintainable supply chains have fewer, owned, maintained components and supported upstreams.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) plan an authorised security test of the application and pipeline; (2) use the OWASP WSTG to structure testing; (3) verify ASVS requirements with evidence; (4) report results responsibly.

### 40.1 Authorisation

Testing requires written authorisation stating scope (staging ticket-web and pipeline), time window and contacts. Kwame's team tests only within that scope.

### 40.2 WSTG structure

The OWASP Web Security Testing Guide v4.2 organises tests into areas such as configuration, identity, authentication, authorisation, session management, input validation and business logic. The team selects tests matching their ASVS Level 2 requirements.

### 40.3 Pipeline review

For the pipeline, the team reviews configuration: branch protection, secret exposure to forks, runner isolation, policy enforcement mode.

### 40.4 Evidence

Each ASVS requirement gets pass, fail or not applicable, with evidence such as screenshots of configuration or test logs.

### 40.5 Results

30 application requirements: 27 pass, 2 fail (session timeout too long; missing rate limit on password reset), 1 not applicable. 12 pipeline requirements: 11 pass, 1 fail (a self-hosted runner still used for a reporting job).

### 40.6 Reporting

Findings describe the weakness, its impact and the fix, without step-by-step misuse instructions, and go to owners with target dates.

### Retesting

Each fix is retested by someone other than the person who made it, using the same test as the original finding. Retest evidence is attached to the finding before it is closed. Kwame finds that one fix for the rate limit applied only to the web form and not the mobile API; the retest caught it and the fix was extended.

### Lessons for the course

The team notes which tests found real issues to plan next year's verification focus.

### Sharing results

Results are shared with developers in a short session.

### Worked example

All three failures are fixed within 30 days and retested. The verification report becomes evidence for Coastline's annual security review.

> **Synthetic case.** Tests and results are synthetic.

### Errors and limits

A test window samples the system at one time; continuous checks fill the gaps.

### Exercises

- **EX118 — Authorisation contents.** What must test authorisation state? *Rubric:* 3 = scope, time window, contacts; 2 = two; 1 = one; 0 = none.
- **EX119 — Results.** Summarise application and pipeline results. *Rubric:* 3 = app 27/2/1; pipeline 11/1; 2 = partial; 1 = one; 0 = none.
- **EX120 — Pipeline failure.** What pipeline failure was found? *Rubric:* 3 = self-hosted runner for reporting job; 2 = partial; 1 = none; 0 = none.

### Synthesis

Authorised, structured verification with evidence closes the loop on requirements.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Application and software supply chain security: system optimization

### Learning outcomes

You will (1) optimise the security system as a whole rather than individual controls; (2) find bottlenecks in remediation; (3) balance risk reduction against cost; (4) use data to choose the next improvement.

### 41.1 Whole-system view

Individual controls can each look good while the system performs poorly. Kwame maps the flow of an advisory from publication to deployed fix: detection (nightly check), triage (owner assigned), fix (code change), review, build, staging, production. He measures the median time in each step over six months of synthetic records.

### 41.2 Finding the bottleneck

Detection takes under a day, fix and review two days, but waiting for the next production release window takes a median of six days. The bottleneck is not security tooling; it is the release schedule.

### 41.3 Changing the system

Coastline introduces a fast lane: security fixes that pass all checks can deploy any weekday morning with one approver. The median time from advisory to deployed fix falls from 10 to 4 days.

### 41.4 Cost and risk

The fast lane adds some deployment risk, managed by automatic rollback and verification. Kwame compares expected exposure saved (6 days per advisory times about 20 relevant advisories a year) with the effort of extra deployments (about 30 minutes each).

### 41.5 Choosing next improvements

With data on each step, the team ranks improvements by days saved per hour of effort. Faster triage through automatic owner assignment ranks next.

### 41.6 Avoiding local optimisation

Speeding up scanning further would save hours, not days; the system view keeps attention on what matters.

### Worked example

Kwame presents a simple chart of median days per step before and after the fast lane. Ingrid notes that the original 11-day tmpl exposure from year one would now be about 4 days, and adopts automatic owner assignment as the next project.

> **Synthetic case.** Step times and counts are synthetic.

### Errors and limits

Medians hide variation; a few slow items may need separate attention.

### Exercises

- **EX121 — Bottleneck.** What was the bottleneck? *Rubric:* 3 = waiting for release window, median 6 days; 2 = partial; 1 = none; 0 = none.
- **EX122 — Fast lane effect.** What effect did the fast lane have? *Rubric:* 3 = 10 to 4 days median; 2 = partial; 1 = none; 0 = none.
- **EX123 — Next improvement.** What ranked next and why? *Rubric:* 3 = automatic owner assignment; days saved per effort; 2 = partial; 1 = none; 0 = none.

### Synthesis

Optimise the whole flow from advisory to deployment, guided by measured bottlenecks.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Application and software supply chain security: applied research

### Learning outcomes

You will (1) formulate an applied research question from engineering practice; (2) design a small study with synthetic or approved data; (3) analyse and interpret results; (4) report limitations.

### 42.1 The question

Kwame asks: does requiring a written justification for new dependencies reduce the number added without lowering developer satisfaction? This connects to findings that dependency growth spreads risk (Zimmermann et al., 2019; Decan et al., 2018).

### 42.2 Design

A before-and-after comparison over two six-month periods at Coastline, with dependency additions counted from the repository and satisfaction measured by a short anonymous survey. The study uses only repository metadata and anonymous survey answers, with Coastline's approval.

### 42.3 Results

New direct dependencies fell from 34 to 19. Survey satisfaction with the dependency process stayed similar (3.8 to 3.7 on a 5-point scale). Justifications most often cited "needed for a new feature" and "replacing an abandoned package".

### 42.4 Interpretation

The justification step seems to reduce casual additions without much frustration. But other changes happened at the same time, such as the new checklist and fewer new features in the second period.

### 42.5 Limitations

One company, two periods, no control group; survey response rate 60%. The findings are suggestive, not conclusive.

### 42.6 Reporting

Kwame writes a short paper for a student conference and a summary for Coastline's engineering blog, using synthetic examples.

### Ethics of the study

Developers were told about the survey's purpose, that it was anonymous and optional, and that results would not be used to judge individuals. Kwame reports only totals, so no developer's dependency choices can be identified.

### Data handling

Survey data are deleted after analysis.

### Worked example

Ingrid asks whether to roll the justification step out to other Coastline apps. Kwame suggests doing so in stages, measuring the same outcomes, which would turn the rollout into a stronger study.

> **Synthetic case.** Study data are synthetic.

### Errors and limits

Before-and-after studies are vulnerable to time trends; staged rollouts improve evidence.

### Exercises

- **EX124 — Research question.** State Kwame's research question. *Rubric:* 3 = justification reduces additions without lowering satisfaction; 2 = partial; 1 = none; 0 = none.
- **EX125 — Results.** Give the two main results. *Rubric:* 3 = 34 to 19 additions; satisfaction 3.8 to 3.7; 2 = one; 1 = none; 0 = none.
- **EX126 — Staged rollout.** Why roll out in stages? *Rubric:* 3 = stronger evidence; compare groups; 2 = partial; 1 = none; 0 = none.

### Synthesis

Applied research turns engineering changes into evidence, with honest limits.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work in a professional engineering team on security tasks; (2) apply course knowledge in a real organisation; (3) follow professional conduct and confidentiality; (4) reflect on practice.

### 43.1 The placement

Kwame spends twelve weeks at Coastline Transit as a placement engineer in Ingrid's platform team, working on the pipeline and the ticket-web application.

### 43.2 Tasks

He triages dependency advisories, writes authorisation tests, improves gate messages, joins on-call shadowing and helps prepare the annual security review.

### 43.3 Conduct

He signs confidentiality terms, uses only approved systems and data, and never tests outside authorised scope. When he finds an issue in a vendor's widget, he reports it to Ingrid, who handles it with the vendor under the contract.

### 43.4 Public service

As a public transport operator, Coastline's priority is safe, reliable service for riders. Kwame sees how security work is balanced with service continuity, such as timing upgrades away from peak travel.

### 43.5 Mentoring

Weekly meetings with Ingrid review his work and learning goals.

### 43.6 Reflection

Kwame keeps a journal of decisions and lessons, reviewed by his course tutor.

### Working with operations

Kwame spends two days with Coastline's operations centre to see how security alerts reach them and what information they need. He learns that alerts with clear next steps are handled faster, and he rewrites three pipeline alerts to include a short action and a link to the runbook. Seeing the work from the receiving side changes how he designs alerts.

### Feedback

At the end of the placement, Ingrid gives written feedback on strengths and areas to develop.

### Worked example

In week eight, Kwame's improved gate messages are rolled out. In the following month, the number of failed builds that are retried without changes drops by half, showing developers now understand and fix the issues instead of retrying.

> **Synthetic case.** The placement is synthetic.

### Errors and limits

Placements vary; learning goals should be agreed early.

### Exercises

- **EX127 — Placement tasks.** List three of Kwame's placement tasks. *Rubric:* 3 = triage advisories, write tests, improve messages, on-call shadowing, security review (three); 2 = two; 1 = one; 0 = none.
- **EX128 — Vendor issue.** How did Kwame handle the vendor widget issue? *Rubric:* 3 = reported to Ingrid; handled with vendor under contract; 2 = partial; 1 = none; 0 = none.
- **EX129 — Message outcome.** What showed the gate messages worked? *Rubric:* 3 = retries without changes halved; 2 = partial; 1 = none; 0 = none.

### Synthesis

Placements test course knowledge against real constraints and conduct.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define a capstone project addressing a real supply-chain need; (2) set requirements and success measures; (3) plan work and risks; (4) secure stakeholder agreement.

### 44.1 The need

Coastline's mobile app builds now run in CI, but the app has no independent check that what riders install matches the signed build. Kwame's capstone: design and build a verification service that checks published app versions against provenance and signatures, and alerts on mismatches.

### 44.2 Requirements

Check each new app store release within one hour; compare its digest with the signed build record; verify provenance policy; alert on mismatch; produce a monthly report.

### 44.3 Success measures

All releases checked within one hour; zero missed mismatches in a test set of 20 synthetic releases with 5 deliberate mismatches; false alerts under one per month.

### 44.4 Plan

Twelve weeks: design (2), build (5), test (3), report (2). Weekly reviews with Ingrid and a tutor.

### 44.5 Risks

App store APIs may change; mitigation: abstract the fetch step. Access to signing records needs approval; mitigation: request early.

### 44.6 Agreement

Ingrid and the course tutor sign the project plan.

### Scope control

Kwame lists what is out of scope: verifying third-party libraries inside the app, checking older releases, and blocking releases automatically. Keeping scope tight lets him deliver a working system in twelve weeks, and the list becomes the starting point for future work.

### Stakeholders

Stakeholders are the platform team, which will operate the verifier, the mobile team, whose releases it checks, and the security lead, who receives alerts. Kwame meets each group in the first week to learn their needs and constraints, and records them in the plan.

### Worked example

During planning, Kwame learns that app stores may re-sign or repackage apps, so digests may legitimately differ. He revises the requirement: compare the inner application files, not the outer package digest, and documents the reasoning.

> **Synthetic case.** The project is synthetic.

### Errors and limits

Capstones must fit time; plan a minimum viable version first.

### Exercises

- **EX130 — Capstone aim.** What does the capstone build? *Rubric:* 3 = service checking app store releases vs provenance/signatures; alerts; 2 = partial; 1 = none; 0 = none.
- **EX131 — Success test.** Describe the test set. *Rubric:* 3 = 20 synthetic releases, 5 mismatches, zero missed; 2 = partial; 1 = none; 0 = none.
- **EX132 — Revised requirement.** Why compare inner files? *Rubric:* 3 = stores may re-sign/repackage; 2 = partial; 1 = none; 0 = none.

### Synthesis

A good capstone starts from a real need with measurable success and managed risks.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) receive and respond to critique; (3) distinguish major from minor issues; (4) update the design with traceable changes.

### 45.1 Preparing

Kwame prepares a design document: purpose, requirements, architecture, data flows, threat model (STRIDE), controls and test plan.

### 45.2 Reviewers

A Coastline security engineer, an external engineer from another transit agency and a course tutor review it.

### 45.3 Findings

Major: the verification service itself holds credentials to the app store API; if compromised, it could hide mismatches. Minor: logging retention unspecified; alert channel single point of failure.

### 45.4 Responses

For the major issue, credentials are read-only and alerts are also sent to a separate system the service cannot modify. Minor issues are fixed with specific values and a second alert channel.

### 45.5 Traceability

Every review comment links to the design change it caused, or a reason for no change.

### 45.6 Value

Independent reviewers see assumptions the author cannot.

### Review meeting

The review takes two hours. Kwame presents for fifteen minutes, then reviewers discuss each section. He listens and records comments without arguing, asking only clarifying questions. Afterwards he sorts comments into major and minor, writes responses and circulates them within a week. Reviewers confirm the major issue is resolved before the build starts.

### Second round

After changes, two reviewers read the updated design and confirm their comments are addressed. The external reviewer adds one new question about how the verifier itself is updated; Kwame answers that it goes through the same pipeline, with signing and provenance checks, as any Coastline service.

### Lessons

Kwame notes that writing the threat model before review saved time.

### Worked example

The external engineer suggests sharing the verification approach with other transit agencies using the same app vendor. Coastline agrees to publish a summary after the capstone.

> **Synthetic case.** Reviews are synthetic.

### Errors and limits

Reviewers may disagree; the designer must weigh comments and justify choices.

### Exercises

- **EX133 — Major finding.** What was the major finding? *Rubric:* 3 = verifier credentials; compromise could hide mismatches; 2 = partial; 1 = none; 0 = none.
- **EX134 — Major fix.** How was the major finding addressed? *Rubric:* 3 = read-only credentials; alerts to separate system; 2 = partial; 1 = none; 0 = none.
- **EX135 — Traceability.** How are review comments tracked? *Rubric:* 3 = linked to change or reason; 2 = partial; 1 = none; 0 = none.

### Synthesis

Independent review finds what authors miss; respond traceably.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) build and test the capstone system; (2) measure against success criteria; (3) handle unexpected problems; (4) document the implementation.

### 46.1 Building

Kwame builds the verifier in a memory-safe language using standard libraries where possible, with its own CI, signing and provenance, so it meets the same rules it enforces.

### 46.2 Testing

The test set of 20 synthetic releases includes 5 mismatches: altered file, missing signature, wrong builder, unreviewed commit and an extra file. All 5 are detected; no false alerts on the 15 good releases.

### 46.3 Timing

Each release is checked in a median of 7 minutes after detection; the slowest takes 22 minutes, within the one-hour target.

### 46.4 Unexpected problem

App store metadata sometimes lags; the verifier now retries for up to 45 minutes before alerting "not yet available" rather than "mismatch".

### 46.5 Documentation

Operations guide, architecture notes, runbook for alerts and a test report.

### 46.6 Handover readiness

Coastline's platform team reviews the code and runs it in staging for two weeks.

### Code quality

The verifier's code is reviewed by two Coastline engineers. Its own tests cover each policy rule and the retry logic. Static analysis runs on every change, and dependencies are kept minimal: only the standard library and one well-maintained library for signature checking. Kwame applies every rule from the course to his own project, so it can be trusted as a security tool.

### Monitoring the verifier

The verifier reports its own health: last successful check, queue length and error counts. If it stops checking for more than two hours, an alert fires, so a silent failure of the checker cannot go unnoticed.

### Worked example

During staging, a real release triggers an alert: an extra configuration file. Investigation shows the vendor's build tool added it in a new version. It is harmless, but the release process is updated to include it in the signed build so future checks pass.

> **Synthetic case.** Results are synthetic.

### Errors and limits

A test set represents known mismatch types; unknown types may evade it.

### Exercises

- **EX136 — Mismatch types.** List the five mismatch types tested. *Rubric:* 3 = altered file, missing signature, wrong builder, unreviewed commit, extra file; 2 = four; 1 = two; 0 = none.
- **EX137 — Timing results.** Give the timing results. *Rubric:* 3 = median 7 min; slowest 22 min; 2 = one; 1 = none; 0 = none.
- **EX138 — Staging alert.** What did the staging alert reveal? *Rubric:* 3 = vendor tool added config file; added to signed build; 2 = partial; 1 = none; 0 = none.

### Synthesis

Build to the same standard you enforce and measure against agreed criteria.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) plan a controlled failure trial of the pipeline and verifier; (2) observe detection and recovery; (3) measure recovery time; (4) record and act on lessons.

### 47.1 The trial

With approval, Coastline runs a planned trial in staging: a synthetic tampered artifact is placed on the mirror, and the signing service is made unavailable for two hours.

### 47.2 Expectations

The deployment should refuse the tampered artifact; the verifier should alert; builds should wait during the signing outage and resume afterwards.

### 47.3 Observations

The tampered artifact is refused within seconds and the alert reaches on-call in 3 minutes. During the signing outage, builds queue as designed, but one team, unaware of the trial, tries to bypass signing with a manual flag; the policy blocks it.

### 47.4 Recovery

After the outage, queued builds complete within 25 minutes. The mirror is cleaned and its digests rechecked.

### 47.5 Lessons

Communication: teams need notice of trials and a status page during outages. The manual flag is removed entirely.

### 47.6 Measuring

Time to detect: 3 minutes; time to recover: 25 minutes after service return.

### Safety of the trial

The trial ran only in staging, with production untouched. A named trial lead could stop it at any time, and all affected teams except one were told in advance; that missed notice became the main lesson. The tampered artifact was synthetic and clearly labelled, and it was deleted and its removal verified after the trial.

### Follow-up

Actions from the trial are tracked to closure, with owners and dates, and reviewed one month later.

### Repeatability

The written procedure lists preparation, roles, steps, stop conditions and clean-up, so the platform team can repeat the trial each year.

### Worked example

Ingrid adds the trial to the yearly calendar and asks Kwame to write the procedure so others can repeat it after he leaves.

> **Synthetic case.** The trial is synthetic.

### Errors and limits

Staging trials may not reproduce production load or human behaviour exactly.

### Exercises

- **EX139 — Trial setup.** What two failures were introduced? *Rubric:* 3 = tampered artifact on mirror; signing service down 2 h; 2 = one; 1 = none; 0 = none.
- **EX140 — Bypass attempt.** What happened when a team tried to bypass signing? *Rubric:* 3 = policy blocked it; flag removed; 2 = partial; 1 = none; 0 = none.
- **EX141 — Measures.** Give detection and recovery times. *Rubric:* 3 = 3 min; 25 min; 2 = one; 1 = none; 0 = none.

### Synthesis

Planned failure trials prove that controls hold and recovery works.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble evidence that the system meets its requirements; (2) organise evidence by requirement; (3) include test results, reviews and trials; (4) make the dossier useful to assessors and operators.

### 48.1 Purpose

The dossier shows assessors and Coastline that the capstone and the pipeline controls meet their requirements.

### 48.2 Structure

For each requirement: statement, implementation, verification method, evidence links and status. Sections cover the verifier, the pipeline controls it relies on and the operational procedures.

### 48.3 Evidence types

Test reports (chapter 46), design review records (45), failure trial results (47), validation reports (38) and metrics (29).

### 48.4 Gaps

Two requirements are partly met: monthly reports exist but are not yet reviewed by management; alert response is tested in staging only. Both are stated with plans.

### 48.5 Usability

The dossier begins with a one-page summary table.

### 48.6 Maintenance

The dossier is versioned; after handover, the platform team updates it.

### Audience needs

Assessors want traceability; operators want procedures and contacts. The dossier therefore has two entry points: a requirement table for assessors and an operations section with runbooks, alert meanings and escalation contacts. Kwame tests each entry point with a real reader from that group and fixes the places where they got lost. He also adds a glossary for terms like provenance and transparency log, which operators found unfamiliar.

### Review of the dossier

Before submission, Ingrid and the tutor check that every link works and every claim matches its evidence. Two links point to outdated test reports and are updated. A second reader checks the summary table against the detailed sections, finding one status shown as met that was only partly met; it is corrected.

### Format

The dossier is plain text with links, readable without special tools.

### Worked example

The assessor samples three requirements and follows the links to evidence in under ten minutes. She notes the honest gap statements as a strength.

> **Synthetic case.** The dossier is synthetic.

### Errors and limits

Evidence ages; keep dates on everything.

### Exercises

- **EX142 — Requirement entry.** What does each requirement entry contain? *Rubric:* 3 = statement, implementation, method, evidence, status; 2 = four; 1 = two; 0 = none.
- **EX143 — Partial items.** Which two requirements were partly met? *Rubric:* 3 = management review of reports; production alert response; 2 = one; 1 = none; 0 = none.
- **EX144 — Assessor finding.** What did the assessor note? *Rubric:* 3 = traced in 10 min; honest gaps a strength; 2 = partial; 1 = none; 0 = none.

### Synthesis

An evidence dossier links each requirement to proof and states gaps openly.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis on the capstone; (2) connect design, implementation and evidence to the literature; (3) discuss limitations and future work; (4) meet academic standards.

### 49.1 Structure

Introduction (problem and need), background (supply chain, SLSA, SSDF, Sigstore, in-toto, reproducible builds), requirements, design, implementation, verification, trial, discussion, conclusion.

### 49.2 Literature connections

The thesis positions the verifier as a consumer-side check complementary to producer-side controls described in SLSA v1.0 and the SSDF, and relates its use of signing and transparency logs to Newman et al. (2022). It cites Ladisa et al. (2023) to show which attack classes the verifier addresses (distribution-stage tampering) and which it does not (malicious source commits by authorised maintainers).

### 49.3 Discussion

The verifier detects mismatches between built and published apps quickly, but relies on trustworthy build records; reproducible builds would add an independent check.

### 49.4 Limitations

One organisation, synthetic mismatches, short operating period.

### 49.5 Future work

Reproducible mobile builds; sharing verification results among transit agencies.

### 49.6 Academic standards

Citations are checked against sources; all case data are synthetic or approved.

### Writing process

Kwame writes the thesis in drafts over eight weeks, sharing each chapter with his tutor. He keeps a list of claims and the evidence for each, checking it before submission so every statement is supported. He also asks Ingrid to check the description of Coastline's systems for accuracy and confidentiality before the thesis is submitted.

### Abstract and summary

The abstract states the problem, approach, main results and limits in under 300 words, and a plain-language summary is written for Coastline staff.

### Submission

The thesis is submitted with the dossier and code archive.

### Worked example

Kwame's tutor asks him to cut the background chapter by a third and expand the discussion of limitations; the revised thesis is clearer about what the verifier does not protect against.

> **Synthetic case.** The thesis is synthetic.

### Errors and limits

Engineering theses must avoid overclaiming security from a single deployment.

### Exercises

- **EX145 — Positioning.** How is the verifier positioned? *Rubric:* 3 = consumer-side check complementing producer controls; 2 = partial; 1 = none; 0 = none.
- **EX146 — Not covered.** Which attack class does the verifier not address? *Rubric:* 3 = malicious commits by authorised maintainers; 2 = partial; 1 = none; 0 = none.
- **EX147 — Tutor change.** What did the tutor ask Kwame to change? *Rubric:* 3 = cut background; expand limitations; 2 = partial; 1 = none; 0 = none.

### Synthesis

An engineering thesis ties built systems to literature and states their limits.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) present and defend the capstone and thesis; (2) answer technical and ethical questions; (3) reflect on the five-year journey; (4) plan continued professional development.

### 50.1 Presentation

Twenty-five minutes: the original incidents, requirements, design, results, trial, limits and future work.

### 50.2 Technical questions

"What if an attacker compromises your CI provider?" Kwame explains that provenance would then be untrustworthy and reproducible builds or a second independent builder would be needed. "Why not verify every file on riders' phones?" He explains privacy and battery costs, and that store-level checks catch tampering before installation.

### 50.3 Ethical questions

"Could the verifier's data reveal riders?" No: it handles only app releases, not rider data.

### 50.4 Reflection

From calculus models of exposure to a deployed verifier, Kwame sees supply-chain security as an engineering discipline of requirements, design, measurement and verification.

### 50.5 Development

He plans a professional certification and joins an open-source supply-chain security working group.

### 50.6 Thanks

Ingrid and the Coastline team receive the final dossier and verifier.

### Preparing the defense

Kwame rehearses three times with classmates who play examiners. He prepares short backup slides on the threat model, test set and failure trial. He practises answering in under a minute, then offering more detail if asked. Rehearsal helps him stay calm and clear, especially on questions about what the verifier cannot do.

### Handover

After the defense, Kwame hands over the verifier code, documents and dossier to the platform team. He runs two sessions so they can operate and change it, and he remains available for questions for a month. A smooth handover ensures the work keeps protecting riders after the student project ends.

### Worked example

The panel passes Kwame with distinction. Coastline offers him a role on the platform team, and the verifier enters production with the platform team as owner.

> **Synthetic case.** The defense is synthetic.

### Errors and limits

A successful defense is the start of practice, not the end of learning.

### Exercises

- **EX148 — CI provider answer.** How did Kwame answer the CI-provider question? *Rubric:* 3 = provenance untrustworthy; reproducible builds/second builder; 2 = partial; 1 = none; 0 = none.
- **EX149 — Rider data.** Does the verifier handle rider data? *Rubric:* 3 = no, only releases; 2 = partial; 1 = none; 0 = none.
- **EX150 — Next steps.** Name Kwame's next steps. *Rubric:* 3 = certification; working group; platform role; 2 = partial; 1 = none; 0 = none.

### Synthesis

The defense shows engineering judgement across technology, evidence and ethics.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Kwame Asante, Ingrid Solberg, Coastline Transit, ticket-web and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** 30 components per year.

**EX002.** It shortens the time the risk rate is integrated over, shrinking the area.

**EX003.** Advisories arrive as fast as they are fixed.

**EX004.** Three direct and nine in total.

**EX005.** It is reached through two parents, so updates may need coordination.

**EX006.** tmpl came in transitively through the framework, so they did not know it was there.

**EX007.** Radiation and wear.

**EX008.** It changes completely.

**EX009.** A storage failure truncated the file; it was not tampered with.

**EX010.** Returning zero would make tickets free; raising an error fails safely.

**EX011.** A function's default skipped escaping for certain attributes.

**EX012.** To avoid echoing user input into the page in the error message.

**EX013.** Summary, context, findings, evidence, recommendations and limitations.

**EX014.** Because lack of evidence is not proof it was not used.

**EX015.** Step-by-step instructions for misuse.

**EX016.** Five, from the sum 1/(1 − 0.8).

**EX017.** About 35% after 10 days and 4% after 30.

**EX018.** Because the real tail was longer than predicted (7% versus 4% after 30 days).

**EX019.** Because malicious packages are rare, so even a small false-flag rate on legitimate ones dominates.

**EX020.** escape-htm1, qr-maker and requests.

**EX021.** 38 proposals, 4 flagged, 1 suspicious and blocked after review.

**EX022.** CWE-787 out-of-bounds write and CWE-416 use after free.

**EX023.** They make flaws harder to misuse but do not remove them.

**EX024.** In a separate process with limited permissions, no network access and a time limit.

**EX025.** A definition of exactly what is acceptable; everything else is rejected.

**EX026.** 12 passengers is out of range and "42a2" is not four digits.

**EX027.** Because browser checks can be bypassed.

**EX028.** He reported it to Ingrid without exploring what it could do.

**EX029.** Reporting privately to maintainers and waiting for a fix before public discussion.

**EX030.** He said he lacked authority to accept risk and escalated to Ingrid.

**EX031.** It authenticates the server and encrypts traffic.

**EX032.** HTTPS with certificate checks and verification against lockfile hashes.

**EX033.** The download was blocked and the team chose a different package.

**EX034.** So that a flaw gives an attacker only limited rights.

**EX035.** To stop one build leaving files that affect the next.

**EX036.** By using ephemeral agents and recording the image digest in each build record.

**EX037.** Only a token and the last four digits.

**EX038.** The parameterised query returned zone A; the string-built one failed on the apostrophe.

**EX039.** Because values can be altered before they reach the server.

**EX040.** Prepare the Organization, Protect the Software, Produce Well-Secured Software, Respond to Vulnerabilities.

**EX041.** Tests, static analysis, the dependency name check and the advisory check.

**EX042.** No training plan for secure coding, in the PO group.

**EX043.** Because they alter the code that is built or deployed.

**EX044.** tmpl: A06 Vulnerable and Outdated Components; mirror: A08 Software and Data Integrity Failures.

**EX045.** OWASP ASVS.

**EX046.** Source repository, CI, artifact storage, deployment and servers.

**EX047.** It is a gap: nothing enforces it.

**EX048.** A second approver and an after-the-fact review within 24 hours.

**EX049.** The SBOM-based advisory check is the sensor; engineering time is the actuator.

**EX050.** Problems are found late and fixes come in bursts.

**EX051.** Removing duplicate advisories reported by two sources.

**EX052.** Reviewed source, isolated builds, signed outputs, provenance records and verified deployment.

**EX053.** Long-lived signing keys that can leak.

**EX054.** Staging shared a database account with production; the accounts were split.

**EX055.** The release copy was verified; the mirror copy had a digest mismatch.

**EX056.** It binds the digest to the identity of the publisher.

**EX057.** An older build with a reused version label; label reuse was then forbidden.

**EX058.** Source, dependencies, build, artifact storage and distribution, deployment and update.

**EX059.** That producers provide a way to verify release integrity.

**EX060.** The mobile app was built on a laptop; it moved to hosted CI.

**EX061.** Deployment shall refuse any artifact whose digest does not match the signed build record.

**EX062.** Level 2, because ticket-web handles payments.

**EX063.** Attempt to deploy a mismatched synthetic artifact in staging and confirm it is refused.

**EX064.** External entities, processes, data stores and data flows.

**EX065.** Supplier, component name, version and dependency relationship.

**EX066.** CI build logs sent to a third-party log service; sensitive values were masked.

**EX067.** Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.

**EX068.** Elevation of privilege.

**EX069.** Expiry monitoring with 30 days' warning.

**EX070.** Because text comparison would wrongly rank 2.0.9 above 2.0.10.

**EX071.** ADV-101 for tmpl and ADV-103 for imgkit.

**EX072.** tmpl renders every page, while imgkit is isolated.

**EX073.** A long-lived key in a hardware module, keyless signing with short-lived certificates, and app-store signing only.

**EX074.** It gives Coastline no independent way to verify.

**EX075.** Offline verification; cached verification material was added.

**EX076.** It would slow fixes by about 5 days, threatening the 7-day critical target.

**EX077.** Fresh isolated environments and platform-generated provenance.

**EX078.** Fixing timestamps and file ordering in the build.

**EX079.** The build waits and retries; after an hour on-call is paged.

**EX080.** An owner, a reason, an expiry date and Ingrid's approval.

**EX081.** Four for a test-only advisory, one lookalike typo and one hand-edited lockfile.

**EX082.** Encoding output for its context by default, with tests using special characters.

**EX083.** Two templates relied on unescaped output; they now use a reviewed safe-markup helper.

**EX084.** The gate flagged it immediately and tests made the change safe.

**EX085.** One critical, two high and one medium.

**EX086.** It waited for a vendor patch.

**EX087.** By reviewing severity changes monthly.

**EX088.** Four tests run with no failures or errors.

**EX089.** Agent refund of 50 allowed and 51 refused.

**EX090.** The agent-small test failed, showing the test detects that mistake.

**EX091.** Builder identity, source repository, commit digest, build steps and output digests.

**EX092.** So a compromised build script cannot forge it.

**EX093.** Verification was in warn mode; it was set to enforce and guarded by a CI check.

**EX094.** The public registry, advisory feed, transparency log and CI provider.

**EX095.** When a check is down over four hours and a critical fix must ship, with Ingrid's approval and two engineers.

**EX096.** Cached verification material expired after 24 hours; it was extended to seven days.

**EX097.** Identify affected artifacts, stop deployments, roll back, rotate credentials and notify.

**EX098.** One release included 1.4.2, deployed for two days; found in four minutes.

**EX099.** Tokens were scattered, so they were consolidated in the secrets manager.

**EX100.** Security writes policies, platform runs the pipeline, product teams own fixes.

**EX101.** One scanner is the gate; the other is used only for comparison reports.

**EX102.** 78% found messages clear, up from 41%, and questions halved.

**EX103.** Do you follow the SSDF, provide SBOMs and signed releases, and how fast do you fix vulnerabilities?

**EX104.** It limits the widget's access to rider data.

**EX105.** Quarterly SBOMs, compensated by monitoring.

**EX106.** By checking only changed components per pull request, with a full nightly check.

**EX107.** Caches between untrusted pull-request builds and release builds.

**EX108.** Under 10%.

**EX109.** Authentication events, authorisation failures and admin actions.

**EX110.** A difference between running systems and configuration code, found by nightly comparison.

**EX111.** A developer copied files to debug; the server was rebuilt and direct access removed.

**EX112.** 3.2.0 allowed; 3.2.1 denied for builder; 3.2.2 denied for an unreviewed commit.

**EX113.** The missing review was completed and the release rebuilt.

**EX114.** Reproducible builds as an independent check.

**EX115.** No releases for two years and unanswered issues.

**EX116.** Replace, maintain internally or remove the feature.

**EX117.** Components fell from 220 to 196 and median versions-behind to zero.

**EX118.** Scope, time window and contacts.

**EX119.** Application: 27 pass, 2 fail, 1 not applicable; pipeline: 11 pass, 1 fail.

**EX120.** A self-hosted runner still used for a reporting job.

**EX121.** Waiting for the next production release window, a median of six days.

**EX122.** Median time to deployed fix fell from 10 to 4 days.

**EX123.** Automatic owner assignment for triage, ranked by days saved per hour of effort.

**EX124.** Whether requiring a written justification for new dependencies reduces additions without lowering developer satisfaction.

**EX125.** Additions fell from 34 to 19 and satisfaction stayed similar, 3.8 to 3.7.

**EX126.** To compare groups over the same time, giving stronger evidence.

**EX127.** Triage advisories, write authorisation tests and improve gate messages.

**EX128.** He reported it to Ingrid, who handled it with the vendor under the contract.

**EX129.** Builds retried without changes dropped by half.

**EX130.** A service that checks app store releases against provenance and signatures and alerts on mismatches.

**EX131.** 20 synthetic releases including 5 deliberate mismatches, with none missed.

**EX132.** Because app stores may re-sign or repackage, changing the outer digest legitimately.

**EX133.** The verifier's credentials meant a compromise could hide mismatches.

**EX134.** Read-only credentials and alerts sent to a separate system the service cannot modify.

**EX135.** Each links to a design change or a reason for no change.

**EX136.** Altered file, missing signature, wrong builder, unreviewed commit and extra file.

**EX137.** Median 7 minutes; slowest 22 minutes.

**EX138.** The vendor's tool added a configuration file; it was included in the signed build.

**EX139.** A tampered artifact on the mirror and a two-hour signing outage.

**EX140.** The policy blocked it and the manual flag was later removed.

**EX141.** Detection in 3 minutes; recovery 25 minutes after service return.

**EX142.** Statement, implementation, verification method, evidence links and status.

**EX143.** Management review of monthly reports and production alert response.

**EX144.** She traced three requirements quickly and praised the honest gap statements.

**EX145.** As a consumer-side check complementing producer-side controls in SLSA and the SSDF.

**EX146.** Malicious source commits by authorised maintainers.

**EX147.** Cut the background by a third and expand the limitations discussion.

**EX148.** Provenance would be untrustworthy; reproducible builds or a second independent builder would be needed.

**EX149.** No, only app releases.

**EX150.** A professional certification, an open-source working group and a role on the platform team.

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
