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

Kwame compares yearly increments rather than the average alone. If the count rose by 15, 25, 35 and 45 in successive years, the average is still 30, but the increments themselves are growing, which means the review workload is accelerating. A team that plans for the average will fall further behind each year.

### 1.3 Accumulation

An integral adds up a rate over time. If a vulnerable component is present for t days at a risk rate r(t), the accumulated exposure is the area under r(t). Shortening the time to upgrade reduces this area directly; this is why later chapters measure remediation days.

The area grows with both height and width, so a severe flaw left for a few days can matter as much as a mild one left for weeks. Kwame treats time as the lever the team controls: it cannot choose when advisories appear, but it can choose how quickly fixes reach production.

### 1.4 Reading graphs

Kwame plots weekly open advisories for ticket-web. The slope after a big framework upgrade is negative for six weeks, then flattens. A flat line at a non-zero value means advisories arrive as fast as they are fixed.

The negative slope shows the upgrade cleared a backlog, because many old advisories were fixed at once. The flattening tells a different story: the team is now keeping pace but not gaining ground. To bring the line down further, Kwame suggests the team either fixes faster or reduces how many components can receive advisories in the first place, for example by removing dependencies nobody uses.

### 1.5 Limits

Calculus models assume smooth change; real advisories arrive in jumps. Models are guides for reasoning, not precise forecasts.

A single large advisory can arrive overnight, and a whole group of components can be fixed in one upgrade, so the real curve is a staircase rather than a smooth line. The models still help compare options, such as weekly versus monthly releases, as long as conclusions are stated as comparisons and not as predictions. Kwame labels every chart with its assumptions, so readers do not mistake a sketch for a measurement.

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

The direction of each arrow matters. If A depends on B, a flaw in B can affect A, but not the other way round. Drawing ticket-web this way shows at a glance which packages its own code calls and which arrive only because another package needs them.

### 2.2 Transitive closure

The set of all nodes reachable from ticket-web is its transitive dependency set. Every node in it is code that runs inside ticket-web, even if no Coastline developer chose it.

That last point changes how teams think about risk. Choosing three trusted packages does not mean trusting only three sets of maintainers; it means trusting everyone whose code those packages bring in. Kwame lists the transitive set alongside the direct one in every review, because advisories arrive for both, and the indirect ones are more likely to surprise the team.

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

The breadth-first search visits each package once, using the seen set, so zipx is counted once even though two arrows lead to it. The work grows only in proportion to the number of packages and arrows, which is why tools can compute closures for real applications with hundreds of packages in moments. Six of the nine arrive only indirectly.

### 2.4 Why it matters

Decan, Mens and Constantinou (2018) measured how vulnerabilities in npm spread through such transitive links; Zimmermann et al. (2019) showed that a few packages and maintainers reach a large share of an ecosystem. Graph structure explains why one flaw can affect thousands of applications.

For Coastline, the practical lesson is that watching only direct dependencies misses most of the code that runs. Advisory monitoring must cover the whole transitive set, and upgrade plans must consider who else depends on a shared package.

### 2.5 Cycles

Some ecosystems allow cycles; search must track visited nodes, as the lab's "seen" set does, or it will loop forever.

Without tracking, a search entering A → B → A would revisit the same nodes endlessly. With a visited set, each node is processed once, cycles or not. Cycles also complicate upgrades, since the packages in a cycle may need to move together, so Kwame's tooling reports any cycle it finds as a note for the team rather than silently handling it.

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

Error-correcting memory corrects single flips and detects double ones, but it does not cover every path a file takes. Data moving over networks, written to disks or held in ordinary memory on cheaper machines can still change. Engineers therefore check data at the points where it matters, such as before an artifact is deployed, rather than assuming the hardware kept it intact.

### 3.2 Storage reliability

Disks and flash wear out; silent corruption is rare but real at scale. Coastline's artifact mirror stores thousands of build files for years.

Over years, even small corruption rates add up across thousands of files. A file corrupted silently may not be read for months, and by then the backup may hold the same damaged copy. Regular verification finds problems while a good copy still exists. Kwame's estimate for Coastline's mirror shows that weekly checks of every file are affordable, since reading the whole store takes under an hour on the existing hardware.

### 3.3 Integrity checks

A cryptographic digest such as SHA-256 changes completely if any bit changes. Checking digests detects corruption and tampering alike; chapter 19 returns to this in the lab.

A digest cannot say which of the two happened, only that the bytes changed. Telling corruption from tampering needs other evidence, such as storage error logs or access records, which is why digests and logs are kept together. A digest is only as trustworthy as the place its expected value is kept: if an attacker can change both the file and the recorded digest, the check passes. Coastline stores expected digests in the build record, separate from the mirror.

### 3.4 Heat and performance

Hot servers slow down; build machines under heavy load can time out, producing incomplete artifacts. Monitoring temperature and build duration helps catch this.

An incomplete artifact is dangerous because it may still look plausible: a truncated archive can open and simply lack its last files. Build systems should fail loudly when a step times out rather than publishing whatever was produced. Recording each build's duration makes outliers visible; a build that suddenly takes twice as long deserves a look before its output is trusted.

### 3.5 The mirror mismatch

Investigation showed the mismatched mirror copy was truncated during a storage failure, not tampered with. But the team could not tell which until they compared logs.

Logs showed a disk error at the time the file was written and no unusual access, which pointed to corruption. Without those logs, the team would have had to treat the event as possible tampering and rebuild everything from source. Kwame's lesson is that detection is only half the job: the evidence to explain a mismatch must be collected before the mismatch happens.

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

Separating calculation from input handling means fare_for can be tested with plain values, without a browser or a web form, and the form code can be reviewed for validation on its own. If prices change, only one small function changes. If a flaw appears in form handling, the pricing logic is not involved. Kwame keeps each function short enough to read on one screen, which also makes the review comment he received easy to act on.

### 4.2 Explicit errors

If zone is unknown, the function raises an error instead of returning zero, which would make tickets free. Failing safely is a security property.

Returning zero looks harmless in a test that only checks valid zones, but in production it would quietly hand out free tickets to anyone who sent a strange zone code. An exception stops the request and leaves a log entry, so the problem is visible. The caller decides what the rider sees, usually a polite message, while the detail stays in the log for engineers.

### 4.3 Testing

Each function has small tests: valid zones, unknown zone, zero passengers. Tests run on every change.

The unknown-zone test is the most important of the three, because it checks the error path, which normal use rarely exercises. Running tests on every change means a later edit that breaks the error handling is caught within minutes. Kwame also adds a test with a negative passenger count, since a value nobody expects is exactly what an attacker or a buggy client might send.

### 4.4 Secure defaults

Defaults should be the safe choice: deny unless allowed, escape output unless told otherwise. The template flaw in tmpl arose when one function's default skipped escaping for certain attributes.

A safe default protects every caller who does not think about the issue, which is most of them. An unsafe default requires every caller to remember an extra step, and some will forget. In tmpl, developers who used the affected attributes got unescaped output without asking for it. The fix changed the default, so existing code became safe without any change by ticket-web's developers.

### 4.5 Readability

Clear names and short functions make review effective; reviewers miss flaws in long, tangled code.

Reviewers have limited attention. A function that fits on one screen and uses names like unescaped_title can be checked in minutes, while a long function with names like t2 hides mistakes. Readability is therefore a security property as well as a courtesy. Kwame's rule of thumb is that if he needs a comment to explain what a line does, the line should probably be rewritten with clearer names first.

### 4.6 CWE vocabulary

MITRE's CWE Top 25 lists weaknesses such as improper input validation (CWE-20) and cross-site scripting (CWE-79). Learning their names early helps read advisories.

The tmpl flaw is an example of CWE-79: output reached a page without proper escaping. Advisories name the CWE, and knowing it tells a reader at once what kind of mistake caused the flaw and where to look in their own code for the same pattern. Kwame keeps a short list of the CWEs relevant to ticket-web and checks new code against it during review.

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

For engineers: the tmpl version, the affected attributes and the upgrade path. For managers: the exposure period, whether data was affected and what the fix costs. For the public: that a flaw was found and fixed, and that no evidence of misuse was seen. The facts are the same in all three; only the detail and emphasis change. Kwame checks that none of the versions says anything another version contradicts.

### 5.2 Report structure

Summary, context, findings, evidence, recommendations, limitations. The summary fits in five lines.

The summary is written last but read first, and often it is the only part managers read. It must stand alone: what happened, what it means and what is recommended. The remaining parts support it for readers who need to check. Limitations come at the end but are never omitted, because a report that hides them loses credibility as soon as a reader finds one. Each finding links to its evidence, so a reviewer can follow any claim to its source without asking the author.

### 5.3 Diagrams

Kwame's dependency graph diagram made the tmpl surprise clear to managers in one glance.

The diagram showed tmpl two arrows away from ticket-web, which answered the question every manager asked: how did we not know? A diagram works when it shows one idea. Kwame removed packages unrelated to the finding, highlighted the path from ticket-web to tmpl, and labelled each arrow, so the picture could be understood without the report beside it. He also included the date of the graph, since dependencies change.

### 5.4 Uncertainty

"We have no evidence the flaw was used" is different from "the flaw was not used". Ingrid insists on accurate phrasing.

The first statement reports what was examined and what was found. The second claims knowledge the team does not have, since logs may not cover every request and an attacker may leave no trace. Readers make different decisions on each: the first may justify further monitoring, while the second suggests nothing more is needed. Accurate phrasing protects both the reader and the team.

### 5.5 Responsible detail

Reports about flaws avoid giving step-by-step misuse instructions; they describe the weakness, its effect and the fix.

Reports travel further than intended: they are forwarded, quoted and sometimes leaked. A description of the weakness and its fix lets readers act, while exploit steps help only attackers. Where engineers need technical detail to verify a fix, it goes in a restricted appendix with a list of who may read it. Kwame's reports describe the tmpl flaw as an escaping failure in certain attributes, without showing a working attack.

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

The series converges only when the average is below one; at one or above, each addition could bring an ever-growing tree, which in practice is limited only by the size of the ecosystem. Kwame uses the figure as a reminder, not a forecast: before adding a dependency, the team asks what it brings with it, and looks at the actual transitive list rather than the package's own size.

### 6.2 Decay models

After Coastline releases a fixed version of its mobile ticket app, users update gradually. If 10% of the remaining old installations update each day, the share still on the old version after t days is 0.9^t: about 35% after 10 days and 4% after 30. This exponential decay model helps plan how long old server-side support for the vulnerable version must continue.

The model assumes each remaining user is equally likely to update on any day, which is the assumption the next comparison tests. Real users do not behave that way.

### 6.3 Linear versus exponential

Kwame fits both models to the real update data from the last app release. The exponential model fits the first two weeks well but overestimates updating later, when the remaining users are those who rarely open the app. Neither model is perfect; he reports both and the range they imply.

A linear model, which assumes a fixed number of users update each day, fails in the opposite way: it predicts everyone will have updated by a certain date, which never happens. Reporting a range between the two models is more honest than choosing the one that gives the most convenient answer. The lingering tail of rare users is what security planning must cover.

### 6.4 Using the models

The models inform two decisions: whether to force updates for security fixes, and how long to keep compatibility code. A forced update shortens the tail but annoys riders whose phones are old.

The decision weighs exposure against cost. If a flaw lets someone tamper with tickets, a forced update after a few days may be justified; if the risk is minor, a prompt is enough. Compatibility code kept for old versions is itself a risk, since it preserves paths that the fix closed elsewhere, so its removal date is planned from the model's tail estimate.

### 6.5 Honest fit

A good fit on past data does not guarantee future behaviour; holidays, app store delays and phone models change patterns. Kwame states the model's assumptions in every chart caption.

Kwame also keeps the gap between prediction and outcome in view. If the model predicted 4% unpatched and reality showed 7%, he records the difference and adjusts the next forecast, rather than quietly refitting so the old prediction looks right. Captions such as 'assumes 10% of remaining users update daily; app-store review delays not modelled' tell readers when not to trust the chart.

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

Suppose 10,000 proposals arrive in a year: about 10 are malicious and about 500 legitimate ones are flagged. Even if every malicious one is caught, only about 2% of flags are real. The check is still worthwhile if reviewing a flag takes minutes, but not if each needs a long investigation, which is why Kwame designs the review to be quick.

### 7.2 Lookalike names

Ohm et al. (2020) documented malicious packages that used names close to popular ones (typosquatting). A defensive check compares each newly proposed dependency name with popular names and asks a human to look when they differ by a single character.

Attackers rely on hurried developers typing a name from memory or copying it from a forum post. The check cannot judge intent; it only notices similarity and passes the decision to a person who can look at the publisher, the package's age and its download history. Popular names are taken from the packages Coastline already uses, plus a list of widely used packages in the ecosystem.

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

The three flags show different edits: escape-htm1 swaps a letter for a digit, qr-maker adds one letter, and requests replaces the final letter. Edit distance 1 means exactly one such insertion, deletion or substitution.

### 7.4 Choosing a threshold

A distance of 1 catches most single typing errors with few flags; a distance of 2 would flag many more legitimate names. Kwame measures over a month: 38 new dependency proposals, 4 flagged at distance 1, of which 1 was suspicious and blocked after review.

One suspicious package out of four flags is a precision of about 25%, which is acceptable for a review that takes a few minutes each. At distance 2, Kwame's trial produced far more flags for the same single catch, so the extra review time bought nothing. The month's counts justify the choice better than intuition would, and they will be checked again as the dependency list grows.

### 7.5 Statistics for decisions

Kwame reports the flag rate and the reviewed outcomes, not just "the check works". Over time these counts estimate the check's precision.

Counts also show what the check cannot do. One catch in a month is too few to estimate how many malicious packages it misses, since those are never seen. Kwame states this limit and suggests a periodic manual review of a sample of unflagged additions to estimate the miss rate. Decisions about tightening or loosening the check then rest on data rather than on the memory of a single dramatic catch.

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

Privilege levels mean ordinary programs cannot touch hardware or other programs' memory directly; they must ask the operating system, which checks permissions first. Virtual memory gives each process its own view of addresses, so a pointer in the image worker cannot name a location inside the web server. When a flaw is exploited, these boundaries decide how far an attacker can move. That is why Coastline treats the process boundary, not the function boundary, as the line that contains damage.

### 8.2 Memory and weaknesses

In languages without automatic bounds checks, writing past the end of a buffer can corrupt nearby data. The CWE Top 25 includes out-of-bounds write (CWE-787) and use after free (CWE-416), both memory-safety weaknesses. ticket-web's image library imgkit is written in such a language and wrapped for the web app.

An out-of-bounds write lets a malformed input overwrite values the program relies on, such as a length or a return address. Use after free means code keeps using memory that has been handed back and possibly reused for something else. Both can turn a crafted image into code execution. Image decoders are a classic target because they parse complex, attacker-supplied formats at speed.

### 8.3 Hardware help

Features such as non-executable memory and address randomisation make memory flaws harder to misuse, but do not remove the flaw. Defence in depth combines them with safer code.

Non-executable memory stops injected bytes from being run directly from a data area, and address randomisation makes it hard to guess where useful code sits. Attackers have found ways around each, for example by reusing code already present in the program. The protections raise cost and reduce reliability of attacks; they buy time for patching rather than replacing it. Kwame checks that both are enabled on the image worker's build.

### 8.4 Language choice

Memory-safe languages prevent many of these weaknesses by design. Coastline writes new services in memory-safe languages and isolates imgkit in a separate process with limited permissions.

Rewriting imgkit would be costly and would introduce new bugs, so Coastline accepts it for now and contains it instead. The choice is made per component: new code gets the safer language, while trusted old code is wrapped. Each wrapped component is listed with its reason and a review date, so the exception is revisited rather than forgotten. Rust and modern managed languages are examples the team considers for replacements.

### 8.5 Isolation by design

Running risky parsing code in its own process, with no network access and a time limit, limits damage if a flaw is triggered by a malformed image.

The worker receives image bytes, returns a resized image or an error, and has nothing else to reach: no database credentials, no network and a small writable folder. A compromised worker could at worst return a wrong picture. Kwame's measurement test later confirmed the time limit stops runaway processing. Designing the boundary before an advisory arrives is far cheaper than adding it in a hurry afterwards.

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

A denylist for zones might reject quotes and angle brackets, but it would still accept 'E' or 'AA', and attackers keep finding characters the list forgot. The allowlist states the four valid letters and nothing else gets through. The rules in the lab are anchored at both ends, so extra characters before or after a valid value also fail.

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

Notice that form 3 reports both failing fields rather than stopping at the first. Users fix all problems in one attempt, and the log shows every rule that fired. Form 2 shows that a value can be well formed, a single capital letter, and still be wrong for the business: Z is a letter but not a zone. The output also confirms fullmatch is used, so partial matches are not accepted.

### 9.3 Where to validate

Validation happens on the server; browser checks improve user experience but can be bypassed. Validation is also not the only defence: output must still be escaped and queries parameterised (chapter 13).

Anyone can send requests straight to the server with a script, skipping the browser entirely, so the server-side rules are the ones that count. Keeping the rule list in one shared module stops the browser and server drifting apart. Validation narrows what reaches the rest of the code; escaping and parameterised queries still handle values that are valid but contain characters such as apostrophes in surnames.

### 9.4 Error handling

Rejected forms return a clear message naming the field, without echoing the raw input. Logs record the rejection without storing card data.

Echoing raw input back can turn an error page into a place where injected markup runs, so the message says 'zone must be A to D' instead of repeating what was sent. Messages also avoid revealing internal details such as stack traces or table names. The log line records the field and the rule that failed, which is enough to spot a pattern of probing without collecting card endings.

### 9.5 Testing rules

Each rule has tests for boundaries: zone A and D accepted, E rejected; 1 and 9 passengers accepted, 0 and 10 rejected.

Boundary tests catch the commonest mistakes, such as writing a range that excludes its last value or a pattern without anchors. Kwame adds empty strings, missing fields and very long values, since forms sent by scripts may contain any of them. When a business rule changes, the test changes in the same commit, so reviewers see the old and new limits side by side.

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

Duties can pull in different directions. An employer may want a feature shipped on time, while the public needs it to protect card data. The engineer's role is to make the risk visible to the people who decide, not to hide it or to decide alone. Ticket sales during disruptions matter because riders without tickets may be stranded, so availability is also a public duty.

### 10.2 Responsible handling

When Kwame notices that an old staff test account still works on the staging site, he reports it to Ingrid rather than exploring what it can do. Testing beyond what you are authorised to do is wrong even with good intentions.

Exploring the account could have exposed rider data, changed records or triggered alarms, and it would have been unauthorised access regardless of motive. Reporting promptly lets the owner disable the account and check its history. Kwame's report gives the account name, where it worked and when he noticed, and nothing he did beyond confirming the login page accepted it.

### 10.3 Disclosure

When the team finds a flaw in an open-source component, it reports privately to the maintainers and waits for a fix before discussing it publicly, a practice known as coordinated disclosure.

Publishing details before a fix exists gives attackers a head start while users cannot protect themselves. Waiting indefinitely is also wrong, so coordinated disclosure usually agrees a deadline with the maintainers, after which details are released. Coastline's reports go through the project's security contact, not its public issue tracker, and include enough detail to reproduce the problem.

### 10.4 Safety and availability

Security changes can break services. Forcing all riders to update the app during a storm, when ferries are cancelled and people need tickets for alternative buses, could cause real harm. Timing matters.

A forced update has value, closing a flaw quickly, and a cost, locking out riders who cannot update during a crisis. The team checks the weather and service status before scheduling disruptive changes and keeps a fallback, such as allowing older versions to show existing tickets. Timing decisions are recorded with their reasons so they can be reviewed later.

### 10.5 Conflicts of interest

Kwame's friend runs a company selling scanning tools. When Coastline evaluates scanners, Kwame declares the relationship and steps back from the decision.

Even if Kwame would judge the tools fairly, others cannot know that, and a hidden link would damage trust in the result if discovered. Declaring the relationship lets someone without the link make the choice. He can still answer factual questions about the tools if asked. The declaration is recorded in the evaluation notes, so later readers see it too.

### 10.6 Codes of conduct

Professional bodies' codes emphasise honesty, competence and public welfare. They help when pressure to ship conflicts with safety.

Citing a code turns a personal objection into a shared professional standard, which is easier for a manager to accept. Codes do not settle every case; they name the values to weigh. Kwame keeps notes of difficult choices and the reasons for them, which also helps him when similar situations arise and when colleagues ask why a decision was made. Recording the reasoning at the time is more honest than reconstructing it afterwards.

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

If DNS answers are forged, the phone may connect to the wrong server; TLS certificate checks catch that. If TLS is misconfigured, data may be readable in transit. If the application layer has a flaw, encryption does not help, because the attack arrives inside a valid connection. Each layer protects against different failures, so none can be skipped on the assumption that another covers it.

### 11.2 TLS

TLS lets the phone check that it is talking to Coastline's real server, using a certificate signed by a trusted authority, and then encrypts traffic. OWASP Top 10:2021 A02 Cryptographic Failures includes sending sensitive data without proper encryption.

The certificate binds the name of Coastline's server to a public key, and the trusted authority's signature vouches for that binding. If an attacker presents a certificate for another name, or one signed by an unknown party, the phone refuses. Encryption without authentication would be pointless, since the phone might be encrypting traffic to the attacker. Kwame checks that ticket-web redirects plain HTTP requests to HTTPS.

### 11.3 Package downloads

Build servers download dependencies over the network. If downloads used plain HTTP, or if certificate checks were disabled, an attacker on the network could substitute a different package. Coastline's builds use HTTPS only, with checks enabled, and verify each package against a lockfile hash.

The lockfile hash is a second, independent check. Even if a mirror or registry were compromised and served a different file over a valid HTTPS connection, the hash would not match and the build would stop. TLS protects the transfer; the hash protects the content. Together they mean a substituted package needs both a broken connection and a matching hash, which is far harder.

### 11.4 Restricting egress

Build machines are allowed to reach only the package registry mirror and source host. Unexpected outbound connections during a build are blocked and logged, which limits what a malicious install script could reach.

Malicious packages often send stolen environment variables to an attacker's server or fetch a second stage during installation. An egress allowlist blocks both unless the attacker's host happens to be on the list. The log of blocked attempts is itself useful: a new package that tries to reach an unknown host is investigated before anyone decides whether to allow it.

### 11.5 Internal mirror

Coastline uses an internal mirror of approved packages. It reduces dependence on the public registry's availability and gives one place to apply checks.

When a package is approved, its exact version is copied into the mirror; builds fetch only from there. If the public registry removes or replaces a version, Coastline's builds are unaffected. Checks such as malware scanning and licence review run once at the point of entry. The mirror must itself be protected and patched, since it becomes a single trusted source for every build.

### 11.6 Monitoring

Network logs from the build environment are kept, so the team can check what a build contacted.

Logs record the destination, time and build identifier for each connection, so an analyst can match unusual traffic to a specific job and commit. They are kept for long enough to cover the time it usually takes for a malicious package to be discovered and reported publicly. A weekly report highlights any new destination, which a reviewer either explains or investigates. Unexplained destinations are treated as possible incidents until shown otherwise.

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

Running as administrator would mean any flaw in ticket-web gave control of the whole server: installing software, reading other services' data and covering tracks. A dedicated user limits this to what the service needs. Separate services get separate users, so a problem in the image worker cannot read ticket-web's files. Each user's permissions are listed in configuration and reviewed when the service changes.

### 12.2 Least privilege

The service user can read its code and write only to its log and temporary folders. If a flaw lets an attacker run code inside ticket-web, they gain only these limited rights.

The code folder is read-only to the service, so an attacker who gains control cannot quietly modify the application to keep access after a restart. Write access is limited to places where nothing is executed. Kwame checks this by listing files the service user can write and comparing them with the intended list; the later monthly script automates the same comparison.

### 12.3 Build isolation

Each build runs in a fresh, short-lived container or virtual machine, destroyed afterwards. This prevents one build from leaving files that affect the next, an issue SLSA v1.0 addresses in its build requirements for isolated builds.

If a malicious dependency writes a modified compiler or cached file during one build, a reused machine would carry it into every later build, including ones for other projects. A fresh environment starts from a known image each time. Recording the image digest lets the team prove later which environment produced a release, which is the evidence auditors and incident responders ask for.

### 12.4 Secrets on the system

Build credentials are injected only for the steps that need them and never written to disk. A build that prints environment variables must not reveal tokens; the CI system masks them in logs.

A token written to disk could remain in a cache, a crash dump or a reused image. Injecting it only into the step that publishes a release means that test steps, which run third-party test code, never see it. Masking in logs is a backup measure, not the main defence, since masking can miss tokens that are encoded or split across lines.

### 12.5 OS logs

Operating systems record process starts, logins and permission changes. These logs help answer what happened during a build or on a server.

During an investigation the question is often when a process started, under which user and what it launched. OS logs answer that independently of the application's own logs, which an attacker with control of the application might alter. Coastline sends them to a central store that build and server accounts cannot modify, and keeps them long enough to cover a typical detection delay.

### 12.6 Patching the OS

Base images for servers and builds are rebuilt weekly with security updates, and a record shows which image each build used.

Weekly rebuilds keep the window for known OS flaws short without constant manual patching. Because each build records the image it used, the team can find every release built on an image that later turns out to contain a vulnerable library. Old images are kept for a limited time so past builds can still be reproduced, then removed. A failed weekly rebuild is fixed before the next week, so images do not quietly fall behind.

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

Data that is not stored cannot be stolen from Coastline's database. The payment token is useful only to Coastline's payment provider account, and the last four digits let riders recognise which card they used without exposing the full number. Each field is checked against a purpose: if no feature needs it, it is not collected. This keeps the impact of any breach smaller.

### 13.2 Queries and injection

When code builds database queries by joining strings with user input, characters in the input can change the query's meaning. This weakness, SQL injection (CWE-89), is part of OWASP Top 10:2021 A03 Injection. The defence is parameterised queries, which send the query and the data separately.

Parameterised queries work because the database receives the query structure first and the values afterwards, so a value can never become part of the structure. Escaping by hand is fragile, since each database has its own rules and one missed case is enough. Kwame's team uses the database library's placeholders everywhere, including in internal reports and scripts.

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

Ann's name contains nothing malicious, yet it broke the string-built query, which shows the flaw is in the code, not in her input. An attacker would use the same gap deliberately, adding text that changes the query instead of merely ending it. The fetchall result is a list of tuples, so the single tuple containing A confirms one matching rider.

### 13.4 Access to data

Staff access goes through roles: support sees tickets but not payment tokens; finance sees refunds. Database accounts used by the app have only the permissions it needs.

Roles reduce the harm a single compromised staff account can do, and they make access easy to review: listing a role's members shows who can see what. The app's database account cannot drop tables or read the audit log, so an injection flaw in ticket-web could not erase its tracks there. Role membership is reviewed each quarter and when staff change jobs.

### 13.5 Backups and retention

Backups are encrypted and tested; rider data is deleted after the legal retention period.

An untested backup may fail exactly when needed, so restores are practised on a schedule. Encryption protects copies stored away from the main system. Keeping rider data longer than the law requires adds risk without benefit, and deletion must reach backups too, which is why older backups expire on the same timetable as the live data they contain. Restore tests use a separate environment, so a practice restore never overwrites real rider records or exposes them to staff who would not normally see them.

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

Spreading security across the steps means problems are caught where they are cheapest to fix. In planning, the team asks who may use a feature; in design, which trust boundaries it crosses; in building, whether review covered input handling; in testing, whether abuse cases were tried. Maintenance includes watching advisories for components already released. Two-week iterations keep each change small enough to review properly, and a flaw found late in one iteration can be fixed early in the next.

### 14.2 The SSDF

NIST SP 800-218 (Souppaya et al., 2022) organises secure development practices into four groups: Prepare the Organization (PO), Protect the Software (PS), Produce Well-Secured Software (PW) and Respond to Vulnerabilities (RV). Kwame maps Coastline's activities to these groups to find gaps.

The four groups cover more than coding. PO asks whether people, roles and tools are in place; PS whether source and releases are protected from tampering; PW whether design, review and testing produce sound code; RV whether flaws found after release are handled. Coastline's signed releases fall under PS, its review checklist under PW and its advisory check under RV. Activities with no group, or groups with no activity, both prompt questions.

### 14.3 Code review

Every change is reviewed by another engineer. A checklist prompts reviewers to look at input handling, authorisation and new dependencies.

A second engineer catches mistakes the author cannot see because they know what the code is meant to do. The checklist keeps reviews from focusing only on style. New dependencies are listed explicitly, because a single line in a manifest can bring in dozens of transitive packages, as the graph lab showed. Reviews of security-sensitive files, such as authorisation rules and pipeline configuration, require a reviewer from a named group of experienced engineers.

### 14.4 Continuous integration

Each change runs tests, static analysis, the dependency name check (chapter 7) and an advisory check. Failures block merging.

Running checks automatically on every change means they cannot be forgotten under deadline pressure. Blocking merges makes the result binding rather than advisory. The cost is occasional false alarms, which slow work if they are frequent, so the team tracks how often a failure turns out to be wrong and tunes the checks. A check that is regularly overridden is either fixed or removed, since ignored alarms train people to ignore real ones.

### 14.5 Dependency policy

New dependencies need a reason, an owner and a check of maintenance activity. Kula et al. (2018) found that developers often do not update dependencies, so each dependency's owner is responsible for keeping it current.

Maintenance activity is checked because an abandoned package will not receive fixes when flaws are found. The reason is recorded so that, years later, the team can tell whether the dependency is still needed. Owners receive the advisory alerts for their packages and plan upgrades. When an owner leaves Coastline, their packages are reassigned during the handover, so no dependency ends up without anyone responsible for it.

### 14.6 Release

Releases are built by CI, signed, and recorded with their digests.

Building releases only in CI means no artifact comes from a developer's laptop, where unreviewed changes or local tools could slip in. The signature lets deployment confirm that the artifact came from Coastline's pipeline. The recorded digest ties the release to the exact bytes built, which is what the mirror check compares against. Each release record also lists the source commit and the SBOM, so anyone can trace a running version back to the code and components it contains. A release lacking any of these records is not deployed.

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

The three properties can conflict. Strict checks that stop every unsigned artifact protect integrity but may block an urgent release if signing is broken, harming availability. Teams decide in advance which property wins in which situation. For ticket-web, integrity of deployed code comes first, since a tampered release could harm every rider at once, while a short delay to a release affects nobody's safety.

### 15.2 Assets and threats

Assets: payment tokens, rider accounts, the build pipeline, signing keys. Threats: criminals seeking payment data, fraudsters seeking free tickets, attackers targeting the pipeline to reach many riders.

Listing assets first prevents the team from focusing only on threats they find interesting. The build pipeline and signing keys appear because they let an attacker reach every rider through one compromise. Each threat is linked to the assets it wants: criminals to payment tokens, fraudsters to ticket and price logic, pipeline attackers to signing keys. Motivation helps predict effort; fraudsters probing for free tickets are numerous but rarely sophisticated.

### 15.3 OWASP Top 10:2021

The ten categories are Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration, Vulnerable and Outdated Components, Identification and Authentication Failures, Software and Data Integrity Failures, Security Logging and Monitoring Failures, and Server-Side Request Forgery. The tmpl advisory relates to Vulnerable and Outdated Components (A06); the mirror mismatch to Software and Data Integrity Failures (A08).

The categories are ranked by data from many organisations and include both specific mistakes and broad design problems. They are useful for training and for sorting findings, as Kwame's classification later shows. Each category links to further guidance, and the matching ASVS chapters give testable requirements.

### 15.4 Controls

Preventive (validation, least privilege), detective (logs, advisory checks) and corrective (patching, rollback).

Each type answers a different question. Preventive controls stop something happening, such as validation rejecting a bad zone. Detective controls tell the team it happened, such as the advisory check spotting a vulnerable component already deployed. Corrective controls restore a good state, such as rolling back to the previous signed release. A plan with only preventive controls has no answer when prevention fails, which it eventually will. For the tmpl advisory, Coastline used all three: review rules for template use, the daily advisory check and a fast upgrade.

### 15.5 Defence in depth

No control is perfect; layers mean one failure does not lead to disaster.

For ticket-web, the template flaw shows the idea. Escaping in tmpl failed for some attributes, but validation had already limited what users could put in most fields, and the web application firewall at the edge blocked some common attack patterns. None of these layers alone was complete. Together they meant that the flaw, although real, was much harder to misuse. Layers should fail for different reasons; three copies of the same check add little, because one bypass defeats all of them.

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

Treating the system as a whole reveals risks that no single team sees. The developers may write careful code while the deployment tool accepts any artifact, or the servers may be hardened while the CI system holds production credentials. Kwame's diagram shows people as well as machines, since an engineer with deployment rights is part of the path from source to rider.

### 16.2 Boundaries

Kwame draws the system boundary: Coastline controls source, CI, mirror and servers; the payment provider and public registry are outside. Interfaces across the boundary (registry downloads, payment API calls) are where trust must be checked, because Coastline cannot inspect what happens beyond them.

Drawing the line makes ownership clear: inside it, Coastline can inspect, test and change things; outside it, Coastline must rely on contracts, checks and evidence supplied by others. The public registry is a good example: Coastline cannot audit every maintainer, so it checks hashes, mirrors approved versions and watches advisories.

### 16.3 Interfaces

Each interface has an owner and a contract: what is sent, how it is authenticated, what happens on failure. The registry interface's contract says downloads must match lockfile hashes; the payment interface's says requests are signed and responses verified.

The failure clause matters most and is often forgotten. If the payment API times out, ticket-web must not issue a ticket as if payment had succeeded. If a lockfile hash does not match, the build stops rather than continuing with a warning. Owners update contracts when either side changes and confirm that tests still exercise each clause.

### 16.4 Traceability

Requirements such as "only reviewed code is deployed" are traced to the components that enforce them (repository branch protection, CI policy, deployment check) and to tests that prove them. A requirement with no traced component is a gap.

The table runs in both directions. From a requirement, the team finds the controls and tests; from a component, it finds the requirements that depend on it, which shows what is at risk if that component is changed or removed. Auditors use the same table to pick samples, so keeping it current saves effort during reviews.

### 16.5 Change management

Changes to one part, such as a new CI runner, are checked for effects on others. A change board reviews changes to the pipeline itself, since a pipeline change can affect every future release.

The board does not slow ordinary code changes, which go through normal review. Pipeline changes get extra scrutiny because they change how every later change is checked: a mistake in the CI policy could let unreviewed code through for weeks before anyone notices. Each approved pipeline change has a rollback plan.

### 16.6 Interfaces as risk

Many supply-chain attacks in the Ladisa et al. (2023) taxonomy target interfaces between stages: source to build, build to distribution, distribution to install.

At each handover, one stage trusts what the previous stage produced. If source is altered after review, the build compiles the altered code faithfully. If a build is compromised, distribution publishes the result. If a distribution channel is hijacked, installers receive the substitute. Checks at each interface, such as signed commits, provenance and signature verification at install, break this chain of assumed trust. Coastline's traceability work focuses on these handovers first, since an unchecked interface lets one compromise pass silently into every later stage.

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

Every loop has four parts: a sensor that measures, a target, a comparison and an actuator that changes something. If any part is missing, the loop does not work. A dashboard nobody reads has a sensor without comparison; a target nobody acts on has comparison without an actuator. Kwame checks each security process for all four parts.

### 17.2 The advisory loop

Coastline's target: no critical advisory open more than 7 days. Each morning, the advisory check reports open items; the team adjusts priorities. The loop's sensor is the SBOM-based check (chapter 24); its actuator is engineering time.

The target is simple enough that everyone knows whether it is being met. The daily report is the comparison, and the morning stand-up is where effort is adjusted. If the SBOM is wrong, the sensor misreads, and the loop steers confidently in the wrong direction, so SBOM accuracy is checked as part of the loop.

### 17.3 Delays

Feedback with long delays causes trouble. If the advisory report were monthly, problems would be found late and fixes would come in bursts. Daily reports shorten the loop.

Delay hides problems and also makes responses overshoot. With a monthly report, a team sees many advisories at once and rushes to fix them all, then has little to do until the next report. Daily reports spread the work evenly. The delay that matters is the whole path from advisory publication to the team noticing, not just how often the report runs.

### 17.4 Oscillation

Overreacting causes swings: one week everyone drops features to fix low-severity items, the next week nothing gets fixed. Clear thresholds and steady capacity keep the loop stable.

Swings waste effort and erode trust in the process. A threshold such as 'criticals first, highs within 30 days' tells everyone what deserves immediate attention, and reserved capacity, for example one engineer-day per week, means the work does not depend on the mood of the week. Kwame compares weekly fix counts to see whether swings shrink.

### 17.5 Positive feedback

Some loops amplify: more noise leads to ignoring alerts, which leads to more unresolved items and more noise. Recognising such loops helps break them early.

The cure is to break the loop at its weakest point. Removing duplicate and irrelevant alerts lowers noise, which makes people more willing to read the rest, which leads to more items being resolved. Good loops can amplify too: quick fixes build confidence, which encourages people to report problems early. Spotting which direction a loop is turning is the first step to steering it.

### 17.6 Measuring the loop

The loop's performance is measured by time to remediate, studied in chapter 29.

Remediation time shows whether the loop as a whole works, combining detection, decision and fix. It is measured from when an advisory applies to Coastline until the fix is deployed, not merely merged, since riders are only protected once production changes. Coastline tracks the median and the slowest cases separately, because an average can look healthy while a few critical advisories wait for weeks. Breaking the time into stages, such as noticing, deciding and deploying, shows which part of the loop to improve next.

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

Each layer stops a different kind of attack. The firewall and rate limits slow automated probing; the application layer handles malicious input; the data layer limits what a successful attack can read; the pipeline layer protects against attackers who try to change the code itself. An attacker who passes one layer still faces the others.

### 18.2 Trust boundaries

Boundaries separate zones of different trust: internet to web tier, web tier to database, CI to production. Every boundary has checks. Secrets for production are never available to pull-request builds from untrusted branches.

Pull requests from untrusted branches may contain code written by anyone, and CI runs that code during tests. If production secrets were available, a single malicious pull request could steal them. Separating the build that tests contributions from the build that produces releases keeps secrets out of reach, at the cost of maintaining two pipeline configurations.

### 18.3 Pipeline architecture

Source changes are reviewed; builds run on hosted, isolated runners; outputs are signed; provenance records who built what from which source; deployment verifies signature and provenance. This follows the SLSA v1.0 model of build provenance and in-toto's idea (Torres-Arias et al., 2019) of recording and checking each step.

Each step produces evidence that the next step checks, so trust is not assumed at any handover. If someone bypasses review, the provenance shows source that did not pass branch protection, and deployment refuses it.

### 18.4 Signing

Signing proves who published an artifact. Sigstore (Newman et al., 2022) offers signing with short-lived certificates tied to identities, avoiding long-lived keys that can leak.

A signature also proves the artifact has not changed since signing. Long-lived signing keys are attractive targets: if one leaks, an attacker can sign malware that looks legitimate until the key is revoked. Short-lived certificates tied to the CI identity limit that window, and a public transparency log records each signing so unexpected signatures can be spotted.

### 18.5 Decisions

Each choice has a decision record: options, trade-offs, chosen design.

A decision record captures the context at the time: what problem was being solved, which options were considered, what each would cost, and why one was chosen. Coastline's record for signing compares long-lived keys with short-lived certificates and notes that the second was chosen to remove key-storage risk. When the context changes, for example a new regulation, the team reads the record before reopening the debate, which avoids repeating old arguments. Records are short, often one page, and are stored next to the code they affect.

### 18.6 Threat of the builder

Thompson (1984) reminds architects that build tools themselves must be trusted; Coastline pins its build tools by digest and rebuilds them from known sources where possible.

Thompson showed that a compiler could be altered to insert a backdoor into programs it compiled, including new copies of itself, so the source would look clean. Pinning tools by digest means a changed tool is noticed. Reproducible builds help further, because independent rebuilds that produce the same output make a hidden insertion in one toolchain visible.

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

Two properties make this useful. It is infeasible to find a different file with the same digest, so an attacker cannot craft a substitute that passes the check, and the digest is small enough to publish, store in a build record or paste into a lockfile. The digest says nothing about whether the file is good, only whether it is the same file the reference describes.

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

The tampered copy differs only by six bytes at the end, yet its digest bears no resemblance to the published one, which is why truncation in the mirror incident was detectable. An ordinary string comparison stops at the first differing character, and its timing can leak information when the compared value is secret.

### 19.3 Signatures

A digest proves the file matches a reference, but who published the reference? A digital signature binds the digest to an identity. Deployment checks both.

An attacker who can change both the artifact and the published digest on the same server defeats a digest check alone, which is the weakness the errors note at the end of this chapter warns about. The signature moves trust to a key or identity the attacker does not control. Deployment first verifies the signature on the build record, then compares the artifact's digest with the one in that record.

### 19.4 Keys and identities

Build signing uses short-lived credentials issued to the CI identity, not personal keys. Developers sign in with multi-factor authentication; OWASP Top 10:2021 A07 covers identification and authentication failures.

Personal keys travel with people: onto laptops, into backups and out of the company when someone leaves. A CI identity exists only inside the pipeline and receives credentials for minutes, so a leaked credential soon becomes useless. Multi-factor sign-in for developers protects the steps before CI, since a stolen password alone could otherwise push code that CI would build and sign faithfully.

### 19.5 Encryption

Encryption protects confidentiality, for example of backups and network traffic; it is not the same as integrity protection.

An encrypted file can still be replaced with a different encrypted file, or corrupted, without the reader noticing unless an integrity check is added. Modern authenticated encryption schemes combine both properties, but plain encryption does not. For artifacts, which are usually public, confidentiality matters little; integrity and authenticity are the goals, so signatures and digests do the work. Backups need both, since they hold rider data and must not be swapped for altered copies.

### 19.6 Key management

Keys are stored in a managed key service, rotated and access-logged.

A managed service keeps keys inside hardware or software that performs signing and decryption without exporting the key, so administrators use keys without being able to copy them. Rotation limits how long any single key is useful if it leaks unnoticed. Access logs show which identity used which key and when; Kwame reviews them monthly for use outside the CI jobs that should need them. Short-lived signing credentials still depend on longer-lived keys elsewhere, such as the key service's own root, so those are protected most carefully.

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

Listing actors shows how many parties outside Coastline influence what riders run. Maintainers write the dependencies, registries host them, the CI provider runs the builds, and Coastline's operators deploy. Each handover is a point where something can be swapped or altered, which is why the controls later in this chapter are arranged by stage.

### 20.2 Attack classes

Ohm et al. (2020) and Ladisa et al. (2023) describe attacks such as malicious packages, compromised maintainer accounts, tampering with build systems and substituting artifacts during distribution. This course stays defensive: it uses these classes to decide where controls belong, not to describe how to carry attacks out.

Grouping attacks by the stage they target is more useful to defenders than listing individual incidents. A compromised maintainer account and a malicious lookalike package both arrive through dependencies, so the same mirror, name check and review controls apply. Build tampering needs different controls, such as isolated runners and provenance, because the source and dependencies may be perfectly clean.

### 20.3 Coastline's controls

Source: branch protection and review. Dependencies: lockfiles, name checks, mirror, advisory checks. Build: isolated hosted runners, pinned tools. Artifacts: signing, provenance, digest checks. Deployment: verification policy. Operation: monitoring and update process.

Laying controls along the chain shows where coverage is thin. Operation has the fewest controls, which reflects that monitoring a running app for signs of a tampered component is hard. Each listed control has an owner and a test, so the team can show it works rather than simply claiming it exists. Kwame's diagram in the worked example applies this check.

### 20.4 Standards

SLSA v1.0 describes build track levels with increasing provenance and isolation guarantees; the SSDF (SP 800-218) practice PS.2 asks producers to provide a way to verify release integrity; ASVS includes requirements on components and configuration.

The three standards look at different parts of the problem. SLSA focuses on how artifacts are built and how their origin can be shown. The SSDF covers the organisation's development practices as a whole. ASVS tests the application itself. Using them together avoids the trap of a well-built artifact containing a poorly secured application, or the reverse.

### 20.5 Open source realities

Wermke et al. (2022) found that open-source projects vary widely in security practices and rely heavily on trust in contributors. Consumers like Coastline cannot assume upstream controls exist.

Many projects depend on a handful of volunteers with no security budget. Coastline therefore treats upstream security as a variable to check, not a given: it looks at maintenance activity, use of multi-factor authentication where registries show it, and whether a project publishes signatures. Where Coastline relies heavily on a project, it can also contribute fixes or funding.

### 20.6 Engineering context

Supply chain security is an engineering problem: it requires requirements, design, measurement and verification like any other system property.

Treating it this way means stating measurable goals, such as every deployed artifact having verified provenance, designing controls to meet them, and testing that they hold. It also means accepting trade-offs: stronger controls cost build time and engineering effort, and the team chooses where they bring the most risk reduction. Calling it engineering rather than a checklist exercise keeps attention on whether controls work, not on whether they exist on paper. The rest of the course follows this pattern from requirements to verification.

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

Each source catches things the others miss. Threats reflect Coastline's own situation, standards bring lessons from many organisations, contracts set obligations the company cannot ignore, and incidents show where its own controls already failed. A requirement records its source, which helps when deciding later whether it is still needed. The tmpl advisory, for instance, is the source of the requirement that advisory checks cover transitive components.

### 21.2 Writing them well

A good requirement is specific and testable: "Deployment shall refuse any artifact whose SHA-256 digest does not match the signed build record" rather than "artifacts shall be secure".

The good example names the actor, the action, the condition and the outcome, so a tester can design a check and anyone can tell whether it is met. Words such as 'secure', 'appropriate' or 'robust' give no test and invite argument. Kwame rewrites each vague requirement until he can describe the acceptance test that would prove it.

### 21.3 Application requirements

Using ASVS as a base, Coastline selects requirements for authentication, access control, validation, output encoding and logging. ASVS 4.0.3 offers three levels; Coastline targets Level 2 for ticket-web because it handles payments. ASVS 5.0.0 keeps the level idea with reorganised chapters, so Kwame records both identifiers.

Level 2 is meant for applications handling sensitive data such as payments, while Level 1 covers basic checks and Level 3 suits the most critical systems. Recording both versions protects the work as the standard evolves: auditors using either edition can find each requirement, and moving to the new edition later becomes a mapping exercise rather than a rewrite.

### 21.4 Pipeline requirements

From SLSA v1.0: builds on a hosted platform, provenance generated by the platform, provenance verified before deployment. From SSDF: PO.3 secure toolchains, PS.1 protect code from unauthorised changes, PS.2 provide verification mechanisms, RV.1 identify vulnerabilities continuously.

Each pipeline item answers a specific risk. Hosted builds remove developers' laptops from the release path. Platform-generated provenance cannot be forged by the build script itself. Verification at deployment ensures the evidence is actually checked. Without that last step, the other two produce records nobody reads.

### 21.5 Prioritising

Requirements are ranked by risk reduction and effort; must-haves cover the two incidents.

The two incidents rank first because they showed real gaps at Coastline, not hypothetical ones. Among the rest, items that close several threats at once, such as deployment verification, rank above those that close one. Effort matters too: a cheap requirement with moderate benefit may be done before an expensive one with slightly more. The ranking is written down with its reasoning, so deferred items are not mistaken for forgotten ones, and the list is revisited when a new incident or standard changes the picture. Must-haves are not traded away for convenience.

### 21.6 Acceptance tests

Each requirement has a test: e.g., deploy a deliberately mismatched synthetic artifact in staging and confirm refusal.

The staging test uses a synthetic artifact, so it proves the check works without risking production. Tests run automatically wherever possible and are repeated after changes to the deployment tool, because a later change could disable the check silently. A requirement whose test cannot be automated gets a manual procedure and a scheduled date for running it. The result of every test run is kept, so auditors and the team can see that the requirement held throughout the year, not only on the day it was first accepted.

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

The four element types make the diagram easy to read and to analyse systematically, because each type suggests particular questions. Data stores invite questions about who can read and change them; processes about what input they accept; external entities about how much they can be trusted.

### 22.2 Trust boundaries

Boundaries appear between rider and web app, web app and payment provider, CI and public registry, CI and production. Every flow crossing a boundary is a place to ask what could go wrong.

On the diagram, a boundary is a dashed line, and every flow that crosses it is checked for authentication, integrity and what happens if the other side misbehaves. The CI-to-registry crossing is where hash checks and the mirror apply; the CI-to-production crossing is where signature and provenance checks apply.

### 22.3 Software as data

An SBOM lists components and versions; NTIA (2021) defined minimum elements: supplier, component name, version, unique identifiers, dependency relationship, author of SBOM data and timestamp. Provenance records how an artifact was built. These are data models the pipeline produces and consumes.

Treating these records as data means they need the same care as other data: correct formats, validation, storage and access control. An SBOM that names the wrong version misleads the advisory check. Missing timestamps or authors make it impossible to tell how fresh the list is or who to ask about it.

### 22.4 Linking models

Each deployed artifact links to its SBOM and provenance by digest. Given a running server, the team can find exactly which components it contains.

The digest is the key that joins everything. From a running server, the team reads the artifact digest, finds the SBOM listing its components and the provenance naming the source commit and build. When an advisory names a component, the same links run backwards to every artifact and server containing it. Without these links, answering 'are we affected?' means searching by hand under pressure. Kwame tests the links each quarter by picking a random production server and tracing it back to source in under ten minutes.

### 22.5 Model upkeep

Models are stored with the code and updated in the same pull request as architecture changes.

Keeping models in the repository means changes are reviewed like code, and the history shows when each flow was added or removed. A reviewer who sees a new external call in the code but no matching change to the diagram asks for it. Outdated models are worse than none, because they give false confidence about which flows exist. Kwame adds a pull-request template question asking whether the change adds or removes a flow, so authors think about the model while the change is fresh.

### 22.6 Simplicity

Models should be just detailed enough to support decisions; a diagram nobody can read helps nobody.

A diagram covering every library call is unreadable and never kept current. Kwame's version shows a dozen processes and stores; detail goes into separate diagrams for areas that need it, such as payment handling. The test is whether a new engineer can explain the main flows after five minutes with the diagram. If a decision would not change with more detail, the detail is left out.

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

Each letter names a property being attacked: spoofing attacks authentication, tampering integrity, repudiation accountability, information disclosure confidentiality, denial of service availability and elevation of privilege authorisation. Walking through the letters for each diagram element gives a structured set of questions, which reduces the chance of forgetting whole categories. Not every letter applies to every element; noting 'not applicable' is still a recorded decision.

### 23.2 Examples

Spoofing: a fake package with a lookalike name. Tampering: an altered artifact on the mirror. Repudiation: a deployment without a record of who approved it. Information disclosure: secrets in build logs. Denial of service: registry outage stopping builds. Elevation of privilege: a pull request from an untrusted fork gaining access to production secrets.

Each example sits on a specific element of Kwame's diagram, which makes it actionable. The fork pull request is elevation of privilege because it crosses the trust boundary between untrusted contributors and CI secrets. The registry outage is accidental in many cases but is listed because the effect, builds stopped, is the same whether caused by failure or attack.

### 23.3 Failure modes

Failure mode and effects analysis asks how each component can fail without an attacker: mirror corruption, CI outage, expired signing certificates, clock errors breaking certificate checks.

Accidental failures matter because they cause many real outages and can mimic attacks, as the truncated mirror copy did. An expired signing certificate stops every release; a clock error can make valid certificates look expired. For each failure, the analysis records how it would be noticed and how the system behaves: safely stopping, or carrying on wrongly.

### 23.4 Ranking

Each threat or failure is rated for likelihood and impact on a 1–3 scale; the product ranks them.

A three-point scale is coarse but quick, and team members agree on it more easily than on finer scales. Multiplying likelihood by impact gives scores from 1 to 9; items scoring 6 or more get attention first. Ties are broken by discussion, with reasons recorded. The scale is not precise risk measurement; it is a way to agree an order of work. Ratings are revisited when controls change, since a new control lowers likelihood and therefore the rank, as the worked example's certificate monitoring will do.

### 23.5 Linking to controls

Each high-ranked item must have a control and a test. Untracked items are risks recorded for management.

Linking means naming the control that reduces each item and the test that shows it works, as in the requirements table. An item with a control but no test is treated as uncontrolled until tested. Lower-ranked items may be accepted without controls, but the acceptance is recorded with a reason and the name of the person who accepted it. This makes it clear who decided, and it lets the next review check whether the reasoning still holds.

### 23.6 Review

The analysis is revisited when the architecture changes and after incidents.

Architecture changes add new elements and flows that the old analysis never considered. Incidents show where the analysis was wrong, either missing a threat or misjudging its likelihood. Each review starts from the previous ranking and records what changed and why. Kwame also schedules a yearly review even without changes, since new attack classes appear and the team's own understanding improves. Lessons from the mirror mismatch, for example, raised the likelihood of storage failures in the next review.

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

Generating the SBOM inside CI, from the same lockfile the build used, means it describes what was actually built rather than what someone remembers adding. A standard format lets the advisory check and other tools read it without custom parsing. Storing it beside the artifact, linked by digest, means that months later the team can answer exactly which components shipped in any release, even if the lockfile has changed since. An SBOM written by hand after release would drift from reality almost at once.

### 24.2 Matching advisories

Advisories list affected version ranges and fixed versions. Matching must compare versions numerically, not as text: "2.0.9" is lower than "2.0.10".

Text comparison works character by character, so when it reaches the third part it compares '9' with '1' and wrongly ranks the older release higher. Splitting on dots and comparing each part as a number gives the right order. Real version schemes add complications, such as pre-release labels with a beta suffix, so production tools use the ecosystem's own comparison rules. Ranges are usually written with an inclusive lower bound and an exclusive upper bound at the fixed version, which is how the lab treats them.

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

The lab's v() function turns each version into a tuple of integers, which Python compares part by part. A package missing from the SBOM would give None and count as not affected, so the SBOM's completeness directly limits what the check can see.

### 24.4 Prioritising

Not every affected component is equally urgent. Kwame considers severity, whether the vulnerable function is reachable in ticket-web, and the exploitation likelihood estimated by EPSS (Jacobs et al., 2021). imgkit is isolated (chapter 8), which reduces its urgency; tmpl renders every page, so it goes first.

EPSS gives a probability that a flaw will be exploited soon, which complements severity: a severe flaw nobody is exploiting may wait behind a moderate one under active attack. Reachability needs knowledge of the code, which the component owner provides.

### 24.5 In CI

The check runs on every build and nightly against the current release, because new advisories appear for unchanged code.

Running at build time catches advisories for newly added components before they ship. The nightly run against the current release covers the other case: code that was clean when built but has since had a flaw published. Without the nightly check, a release could sit in production for weeks with a known flaw until the next build happened to run. Results from both runs feed the same list, so owners see one queue. The nightly run uses the stored SBOM for the release, so it needs no rebuild and finishes in minutes.

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

Moving the mobile build into CI, after the gap found in the chain diagram, solved where the app is built but not how users and Coastline can confirm what they received. The brief asks for signing, verification and updates together, because a design that signs well but updates poorly still leaves riders on old versions. Requirements from earlier work give the team a ready test for each option.

### 25.2 Alternatives

Option A: traditional long-lived signing key in a hardware module. Option B: keyless signing with short-lived certificates tied to the CI identity (the Sigstore model). Option C: platform app-store signing only.

Including a minimal option, C, gives a baseline to compare against: if A or B adds little over relying on the app stores, the extra effort is not justified. The three differ mainly in where trust sits: in a key Coastline guards, in an identity and a public log, or in the store operators.

### 25.3 Critique

Against requirements: A is strong but needs key ceremonies and rotation; B reduces key-theft risk and adds a public transparency log but depends on an external service; C is simplest but gives Coastline no independent verification.

The team scores each option against the requirement table rather than against general impressions. Dependence on an external service, for B, is weighed by asking what happens during an outage: builds would pause signing, which fails closed. For C, the lack of independent verification fails the requirement that Coastline can check what was built from its own records.

### 25.4 Prototype

The team prototypes B with synthetic artifacts in a test environment, measuring time added to builds (about 20 seconds).

The prototype tests the claims made in the critique. Twenty seconds per build is small compared with the test suite, so build time is not an objection. The team also confirms that verification fails when an artifact is altered and when the certificate identity is not Coastline's CI, and records any steps that were harder than expected. Synthetic artifacts mean no real signing identity or production system is involved, so mistakes during the prototype carry no risk. Measured numbers replace guesses in the final presentation.

### 25.5 Presentation

Ten minutes to Ingrid and two Coastline engineers, with the requirement table, risks and recommendation.

Ten minutes forces the team to lead with the recommendation and the evidence for it, leaving detail for questions. The requirement table lets Ingrid see at once which needs each option meets. Risks are stated plainly, including the dependence on an external service for B. Kwame, as requirements owner, answers questions about coverage. The engineers' questions are noted and answered in writing afterwards, so nothing raised in the meeting is lost.

### 25.6 Peer review

Another studio team reviews the design and asks how verification works offline on buses with no signal; the team adds cached verification material.

Reviewers from outside the team see assumptions the authors no longer notice. The team had assumed riders' phones are always online, but buses and ferries often lose signal, and a verification step that needed the network would block riders at the worst moment. Cached verification material lets the app check updates offline, with a refresh when signal returns. The review is recorded with the change it caused, so later readers understand why the design includes caching.

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

The three options represent increasing levels of control. Each moves the point where Coastline can inspect packages closer to its own boundary. The choice affects every build and every developer, so it is worth comparing carefully before committing. Kwame's team also asks which option a team of Coastline's size can keep running for years, not just set up.

### 26.2 Risk trade-offs

Option 1 is simple but depends on the registry's availability and offers no central control point. Option 2 adds caching, logging and a place for checks, with modest cost. Option 3 gives the most control but slows updates, which can lengthen exposure to known flaws; Kula et al. (2018) showed that update friction already causes lag, and Decan et al. (2018) showed how lag spreads vulnerabilities.

The tension is between control and speed. Every check added before a package can be used also delays the fixes that arrive as new versions, so tighter control can mean longer exposure. Option 2 sits in the middle: it inspects packages automatically as they pass through, without waiting for a person.

### 26.3 Build options

For builds: self-hosted runners give control but must be maintained and isolated; hosted runners from the CI provider offer fresh, isolated environments and platform-generated provenance aligned with SLSA v1.0 Build Level 2 and above, but depend on the provider.

Self-hosted runners require Coastline to patch, isolate and monitor them, which the old reused build agent showed is easy to get wrong. Hosted runners shift that work to the provider and produce provenance the build script cannot forge. The cost is dependence on the provider's availability and security, which Coastline checks through the provider's published assurances.

### 26.4 Reproducibility

Reproducible builds (Lamb and Zacchiroli, 2022) let an independent builder recreate the same bits, detecting tampering in the original build. Coastline evaluates making ticket-web's server build reproducible; it requires fixing timestamps and ordering in the build.

Timestamps embedded in files and the order in which files are archived are common reasons two builds of the same source differ. Fixing them lets an independent rebuild be compared with the release by digest. A match is strong evidence that the release came from the stated source. A mismatch is investigated before the release is trusted.

### 26.5 Usability

Developers need fast builds and simple upgrades. A design that slows them down will be worked around, echoing Johnson et al. (2013) on tool adoption.

Developers under deadline pressure find shortcuts: copying a package into the repository to avoid the mirror, or disabling a slow check. Each shortcut removes the control it avoided. Designs that are fast and simple to follow get used as intended, so usability is a security requirement, not a convenience. Coastline measures build times and the time to add a new dependency before and after each change to the design, and treats a significant slowdown as a defect to be fixed.

### 26.6 Decision

Coastline chooses option 2 with automatic checks (name similarity, advisories, licence), hosted runners, and a pilot of reproducible server builds.

The decision combines the option that balances control with update speed, a build platform that removes maintenance burden and provides provenance, and a limited pilot of reproducible builds to learn the cost before committing. The pilot covers only the server build, because the mobile build depends on store tooling that is harder to make reproducible. The record lists conditions that would reopen the choice, such as the registry suffering repeated outages or the curated option becoming cheaper through automation.

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

Review by one engineer prevents a single person from changing ticket-web alone. Passing checks ensures tests and the dependency gate ran. Signed commits on release branches tie each change to a verified author, so a stolen password alone cannot inject code. Blocking direct pushes means every change goes through the same path, including those from senior engineers and administrators, who could otherwise skip review in a hurry. The repository settings that enforce these rules are themselves protected, so changing them needs approval from two administrators.

### 27.2 Dependency controls

The CI dependency gate fails a build if: a lockfile hash does not match, a new name is within edit distance 1 of a popular name without an approved review, or a critical advisory applies without an exception.

Each condition corresponds to an earlier finding: hash mismatches to the mirror incident, lookalike names to the name-similarity lab and critical advisories to the tmpl case. The approved-review clause matters, because some legitimate packages have names close to popular ones; a reviewer can approve them once, and the gate then remembers the decision. Messages name the failing rule so developers can fix the cause quickly.

### 27.3 Build controls

Builds run on hosted runners with pinned tool versions; production secrets are not available to builds from forks; the platform generates provenance.

Pinned tool versions mean a build uses exactly the compiler and packaging tools the team tested, not whatever was latest that morning. Keeping secrets away from fork builds closes the threat ranked highest in the threat analysis. Platform-generated provenance records the builder, source and inputs in a way the build steps cannot alter, which the deployment policy then checks. Tool versions are updated deliberately in reviewed changes, so a new compiler is never introduced silently.

### 27.4 Deployment controls

The deploy policy allows an artifact only if built by the approved builder from the approved repository from reviewed commits, with a valid signature and matching digest. Policies are written as code, version-controlled and reviewed like application code.

Writing policy as code means a change to the rules is visible in a pull request, with a reviewer and history. Each condition in the policy maps to evidence produced earlier: the provenance names the builder and repository, branch protection records the review, and the signing log holds the signature. If any piece is missing, the artifact is refused, even when everything else looks correct.

### 27.5 Failure behaviour

Controls fail closed: if the advisory service is unreachable, the build waits and retries rather than skipping the check; after one hour, the on-call engineer is paged.

Failing open would mean an outage of the advisory service silently disables the check, which an attacker could exploit by causing the outage. Failing closed costs availability: releases wait until the service returns. Paging after an hour keeps that delay short. For a true emergency, the exception process allows a release with a recorded approval, so failing closed does not trap the team indefinitely.

### 27.6 Exceptions

Exceptions need an owner, a reason, an expiry date and approval by Ingrid. Expired exceptions block builds again.

An exception without an expiry tends to become permanent and forgotten. The owner is responsible for removing the cause before expiry or requesting renewal with a new reason. Requiring Ingrid's approval keeps exceptions visible to someone accountable for overall risk. A weekly list of active exceptions shows the trend; a rising count suggests a control is too strict or a team needs help. Each exception records exactly which check it suspends and for which component, so it cannot be stretched to cover other problems.

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

Context matters because the same character is dangerous in different ways in page text, attribute values and scripts. A quote mark is harmless in text but can end an attribute early; angle brackets matter in text but not inside a quoted attribute. Encoding for the right context, by default, removes the burden from each developer. The test with synthetic rider names checks that quotes and angle brackets in them arrive on the page as plain text.

### 28.2 Authorisation

Every endpoint calls a central authorisation function with the user's role and the resource owner. Checks happen on the server, aligned with OWASP Top 10:2021 A01 and ASVS access-control requirements.

A central function means one place to review and test instead of checks scattered through every handler. It compares the user's role and identity with the resource: a rider may view only their own tickets, support staff any ticket but no payment tokens. A handler that forgets to call the function is caught by a test that lists every endpoint and checks each one calls it. Server-side checks matter because hidden buttons in the browser do nothing to stop a scripted request.

### 28.3 Upgrading tmpl

The upgrade from 2.0.9 to 2.0.10 is small but changes one default. Tests catch two templates that relied on unescaped output for trusted icons; they are rewritten to use an explicit safe-markup helper reviewed by Ingrid.

The changed default was the fix, so templates relying on the old behaviour broke as intended. Rewriting them with an explicit helper makes the trust decision visible in the code. Ingrid's review confirms the icons come from Coastline's own files, not user input. Any future use of the helper needs the same check.

### 28.4 Implementing the gate

The dependency gate is a small CI step reading the lockfile and SBOM, calling the advisory feed and the name-similarity check, and applying the policy. Its own code is reviewed and tested.

Keeping the gate small makes it easy to read and test. It does not decide policy itself; it reads the policy file and reports which rule failed, so the error message tells developers exactly what to fix. Tests use synthetic lockfiles that should pass and fail. A bug in the gate could let flawed packages through silently, so it is treated as security-critical code.

### 28.5 Regression review

After the changes, a reviewer compares rendered pages before and after and runs the authorisation test suite.

Comparing rendered pages catches text that now appears escaped where it should be formatted, or markup that should be escaped but is not. The authorisation suite checks that each role still sees exactly what it should after the refactoring of handlers. Automated screenshots highlight differences, and the reviewer looks at each one rather than approving the whole set. Regressions found here are cheaper than complaints from riders, and the review is repeated for any change that touches templates or authorisation.

### 28.6 Rollback plan

Each release can be rolled back to the previous signed artifact within ten minutes.

Fast rollback lowers the cost of a mistaken release, which makes the team more willing to ship security fixes quickly. Because the previous artifact is already signed and its digest recorded, the deployment policy accepts it without a new build. Database changes are the hard part: migrations are written so the previous version still works with the new schema for at least one release. The rollback is practised in staging every month, so the ten-minute figure is measured rather than hoped for.

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

Each metric answers a different question. Remediation time shows how quickly known problems are fixed. Provenance coverage shows how much of what runs can be traced to reviewed source. The exception count shows how often controls are being bypassed. Freshness predicts future pain: a dependency far behind will need a large, risky upgrade when a flaw finally forces one. Metrics are chosen because someone will act on them; a number nobody can influence is dropped from the dashboard.

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

The medians all sit inside their targets, yet four of twelve findings were late. A report showing only medians would suggest everything is fine. Counting late items separately reveals the cases that need attention. With only three critical findings, one extra late item would move the median sharply, which is the instability the errors note warns about. For an even count, as with the four medium findings, the median is the average of the middle two values, 60 and 75, which gives 67.5.

### 29.3 Late items

The late critical item waited for a vendor patch; the late highs needed a framework upgrade that took two sprints. Measuring lateness leads to the cause, not blame.

The two causes call for different actions. A vendor delay may be handled by a temporary control, such as isolating the component or disabling the affected feature, while waiting. A slow framework upgrade points to too much deferred maintenance; regular small upgrades would make the next one easier. Asking 'what made this slow?' instead of 'who was slow?' gets honest answers, because people are not afraid to describe the delay.

### 29.4 Perverse incentives

If teams are rewarded only for closing fast, they may downgrade severities. Coastline reviews severity changes monthly.

A finding downgraded from high to medium gains sixty days under the targets, which makes the numbers look better without making riders any safer. The monthly review checks each change against its evidence; changes need a written reason and a second person's agreement. Coastline also avoids rewarding individuals on remediation numbers, since that invites gaming. Teams are praised for honest reporting, including when the numbers look bad, because hidden problems cannot be fixed.

### 29.5 Freshness

The median dependency is one minor version behind; two are more than two major versions behind and planned for replacement.

Being one minor version behind usually means the team is current enough to take a security fix quickly, often with no code changes. Being two major versions behind means a fix may only be released for newer versions, forcing a large upgrade under pressure. Replacement is planned for those two while there is time, rather than waiting for an advisory to force the work. The freshness figure is reviewed monthly alongside remediation time, since the two tend to move together.

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

Refund rules mix role and amount, and a small edit can change who gets money back. Without tests, nobody notices until a fraud report or an audit. With tests, the change fails in CI within minutes and the author sees exactly which rule they altered. Tests also document the rule in a form developers read: the test names say what is allowed far more precisely than a policy document.

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

The test runner's output is captured in a string buffer, so the lab prints only the summary line. A real CI run shows each test name, which helps when one fails. The function relies on Python's operator precedence, where 'and' binds more tightly than 'or'; the tests confirm that the expression means what the author intended. Adding parentheses would make that intent clearer to a reader.

### 30.3 Negative cases

Tests that check something is refused are as important as tests that check something is allowed. Two of the four lab tests are negative.

Many authorisation bugs are about allowing too much, and positive tests never catch them: a function that returns True for everyone passes every 'is allowed' test. The rider test and the agent-large test would both fail in that case. Kwame aims for at least one refused case for every allowed one, covering wrong role, wrong amount and missing values.

### 30.4 In CI

The tests run on every change; a failure blocks merging. Coverage reports show which authorisation branches are exercised.

Running on every change means a regression is caught by the person who caused it, while the change is fresh in their mind. Blocking merges keeps broken rules out of the main branch. Coverage reports show branches no test reaches; for refunds, an uncovered branch is a rule nobody has checked. Coverage alone does not prove tests are good, which is why mutation thinking follows.

### 30.5 Mutation thinking

Kwame changes "<= 50" to "< 50" in a scratch copy: the agent-small test fails, proving the test detects that mistake.

A test suite that still passes after a deliberate mistake would not have protected anyone. Changing the comparison is a small mutation, the kind of slip a developer might make while editing nearby code. If no test failed, Kwame would know the boundary was untested. Tools can automate this by making many small changes and reporting which ones survive the test suite; each survivor shows a gap. Kwame runs such a tool monthly on the authorisation module, because that is where a missed mistake would cost most.

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

Because the platform, not the build steps, writes the record, an attacker who changes the build script still cannot make the provenance claim a different source or builder. Deployment then checks those claims against policy before anything is installed.

### 31.2 Signing

The artifact is signed with keyless signing tied to the CI workflow's identity, and the signature is recorded in a transparency log, following the Sigstore model (Newman et al., 2022). Anyone can later check when and by which identity the artifact was signed.

The transparency log is public and append-only, so a signature made with Coastline's identity at an unexpected time, or for an unknown artifact, would be visible. Coastline monitors the log for its own identity and alerts on entries that do not match a CI run. No long-lived key exists to steal.

### 31.3 Storage

The artifact, its SBOM, provenance and signature are stored together and linked by the artifact digest. Retention is at least as long as the release is in use, plus one year.

Keeping the records together means one lookup by digest returns everything needed to verify or investigate a release. If records were stored separately, one might be deleted or overwritten while the others remain, leaving a release that cannot be checked. The extra year after a release leaves use covers investigations that start late, such as when a compromised component is discovered months after it shipped. Storage is write-once, so records cannot be altered after they are saved.

### 31.4 Deployment verification

The deployment tool fetches the artifact and its records, verifies the signature, checks the provenance against policy (chapter 38's lab) and compares digests before installing. Any failure stops the deployment with a clear message.

The order of checks matters little for security, since all must pass, but checking the signature first gives the clearest error for the commonest failure. The clear message names which check failed and for which artifact, so the person deploying can tell a configuration mistake from a possible tampering case and escalate the second at once.

### 31.5 End-to-end test

A staging pipeline deploys a known-good synthetic artifact and three deliberately flawed ones (wrong digest, wrong builder, missing signature). The test passes only if the first deploys and the others are refused.

Each flawed artifact tests one check in isolation, so a failure points to the broken part. Testing only the good case would prove nothing about the checks, since a tool that verifies nothing also deploys a good artifact. The test runs after every change to the deployment tool, its configuration or the policy, and weekly otherwise, because the worked example shows how a single flag can quietly disable a check.

### 31.6 Performance

Verification adds 12 seconds to deployment, acceptable for the team.

Twelve seconds is small next to the minutes a deployment already takes, and far less than the cost of investigating a tampered release. Measuring it matters anyway, because slow controls invite shortcuts: if verification took ten minutes, people would look for ways around it during urgent fixes. The team records the time for each deployment and investigates if it grows, since a sudden rise might signal a problem with the log service or cached verification material. Most of the time is spent fetching records, not checking signatures.

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

When a control fails often for reasons unrelated to security, developers learn to treat its failures as noise and press for an override. Each false or flaky failure therefore weakens the control. Coastline tracks failures by cause and fixes the commonest ones first, so the control mostly fails only when it has found something real. Recovery time matters as well: a failure that clears in a minute barely interrupts work, while one needing a support ticket costs hours and goodwill.

### 32.2 External dependencies

The pipeline depends on the public registry, the advisory feed, the transparency log and the CI provider. Each can fail. The internal mirror covers registry outages; cached advisory data covers short feed outages; verification material is cached for transparency-log outages.

Listing the dependencies makes their failures predictable. For each one, the team decides how long it can be unavailable before releases stop and what cache or fallback covers that period. A dependency with no fallback is a single point of failure and is listed as a risk until one is added.

### 32.3 Fail closed, recover fast

Failing closed protects integrity, but long outages block releases. Coastline sets a recovery process: if a check is unavailable for more than four hours and a critical fix must ship, Ingrid can approve a documented manual verification with two engineers.

The manual path is narrow on purpose: it needs a critical fix, a long outage and a named approver, and two engineers perform the checks by hand and record what they did. Every use is reviewed afterwards. Without this path, teams under pressure would invent their own bypasses, which would be less careful and leave no record.

### 32.4 Measuring availability

The team logs every control failure: cause, duration and effect. Over a quarter the gate was unavailable for 3 hours in total, all due to the advisory feed.

Three hours across a quarter is a small fraction of the time, but if it falls during an urgent release it matters a great deal. Logging the cause shows that all downtime came from one source, which makes the fix obvious. Without the log, the team would remember the outages vaguely and might blame the gate itself. The same log later shows whether the fix worked, by comparing the next quarter's downtime with this one.

### 32.5 Redundancy

A second advisory source is added, reducing dependence on one feed.

With two feeds, the gate keeps working if one is down, and advisories published by only one source are still seen. The sources sometimes disagree on version ranges; when they do, the gate uses the wider range and flags the difference for a person to check. Duplicates from the two feeds are merged by advisory identifier, so the earlier noise reduction is not undone. The added cost is small compared with releases blocked for hours during an outage of a single feed, and the team reviews both sources yearly to see whether each still adds value.

### 32.6 Testing failure

Every quarter the team simulates an outage of each external service in staging to check the fallback works.

A fallback that is never exercised may have broken without anyone knowing, as the expired cache in the worked example shows. Simulating outages in staging, by blocking access to each service in turn, proves the cache, mirror and second feed take over. Each test records how long builds and deployments continued normally and what errors appeared. Results feed into the control failure log, so planned tests and real outages can be compared over time.

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

Planning only for prevention leaves the team improvising when prevention fails. Assuming compromise changes the questions: how quickly would we notice, how many riders would be affected, and how fast could we return to a trusted release? The links between artifacts, SBOMs and provenance built in earlier chapters exist largely to answer those questions under pressure.

### 33.2 Response plan

The supply-chain playbook: identify affected artifacts using SBOMs and provenance; stop deployments; roll back to the last known-good signed release; rotate any credentials the compromised component could have reached; notify stakeholders.

The steps are ordered so that damage stops spreading before anything else. Finding affected artifacts first tells the team what to stop and what to roll back. Credentials are rotated because a malicious component may have read secrets available to its process, and rollback alone does not revoke stolen tokens. Each step has a named owner.

### 33.3 Known-good state

Because every artifact is linked to its SBOM and provenance, the team can find the last release that did not include a compromised version and redeploy it.

Rolling back to a release built before the compromise works only if that release is still stored, still signed and still compatible with the current database. Coastline's retention rules and migration practice make all three true. Without SBOMs, the team would have to guess which release is clean, and a wrong guess would leave the malicious code running while everyone believed it gone.

### 33.4 Rider safety

Ticket sales must continue. A fallback paper-ticket process and the previous app version keep service running.

During a supply-chain incident the safest technical step, stopping all releases, must not stop riders travelling. Riders who cannot buy a ticket may be stranded at a station or pier, which is a real harm. The paper process is tested twice a year so staff know how to use it. Keeping the previous app version available means riders whose phones have already updated can be moved back if needed, while people at stations follow the paper route. Customer messages explain the fallback in plain words.

### 33.5 Exercise

Coastline runs a tabletop: "a widely used package in ticket-web is reported compromised; versions 1.4.2–1.4.3 contained malicious code". Using SBOM search, the team finds that only one release included 1.4.2 and that it was deployed for two days.

A tabletop uses discussion rather than live systems, so no service is put at risk. The scenario is concrete enough that the team must run real queries against stored SBOMs. Finding that only one release was affected, and for only two days, narrows the response dramatically.

### 33.6 Lessons

The exercise shows that credential rotation would take a full day because tokens were scattered; the team consolidates them in the secrets manager.

Scattered tokens were invisible until the exercise asked the team to rotate them all at once. Consolidating them in the secrets manager gives one list of what exists, who uses it and how to rotate it, and makes rotation scriptable. The next exercise is planned to measure the new rotation time, so the improvement is shown with evidence rather than assumed. Exercises are worth running precisely because they find this kind of gap before a real incident does.

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

Before integration, developers checked several dashboards and often missed a failing scanner because it reported somewhere they rarely looked. A single sequence, shown in the pull request, means every result is seen at the moment a decision is made about merging. The order also matters: cheap checks run first, so a simple test failure is reported before slower steps start, and signing happens only for builds that passed everything earlier in the line.

### 34.2 Aligning teams

The security team writes policies; the platform team runs the pipeline; product teams own fixes. A weekly meeting resolves conflicts.

Clear roles stop each team assuming another handles a problem. The security team decides what the rules are, but does not run the CI servers; the platform team keeps the pipeline healthy, but does not decide which advisories matter; product teams fix their own code, since they know it best. Conflicts, such as a policy that slows a team's releases, are raised in the weekly meeting, where the people who can change each part are present. Decisions are written down so the same argument does not repeat.

### 34.3 Avoiding duplication

Two tools both scanned dependencies with different advisory data, producing contradictory results. The team keeps one as the gate and uses the other only for comparison reports.

Contradictory results waste time and erode trust: developers asked which tool to believe, and some ignored both. Choosing one gate gives a single answer for merging. Comparison reports from the second tool still catch advisories the first missed, and any difference is investigated by the security team rather than left for each developer to puzzle over.

### 34.4 Developer experience

Messages explain what failed, why it matters and how to fix it, with links. Median CI time is kept under 12 minutes.

A message such as 'blocked: ADV-101 affects tmpl 2.0.9, upgrade to 2.0.10, see guide' lets a developer fix the problem in minutes. A bare 'policy violation' sends them to ask in chat. Keeping CI time down matters for the same reason: when builds take too long, people batch changes, which makes review harder and each failure more confusing to diagnose. Links point to the developer guide.

### 34.5 Integration testing

Changes to any control are tested in a staging copy of the pipeline before rollout.

The pipeline is software, and changes to it can break every later build or, worse, silently stop a check from running. A staging copy with the same configuration lets the platform team try a change against sample repositories, including ones designed to fail each check. Only when the expected failures still occur is the change rolled out. The end-to-end deployment test with flawed artifacts is part of this suite.

### 34.6 SAMM view

OWASP SAMM v2 (2020) maturity assessment shows Coastline rising in Implementation (secure build, secure deployment) and Verification after integration.

SAMM groups practices into business functions, each assessed for maturity. Using it shows progress in a form leadership recognises and highlights functions that lag, such as governance or operations. Coastline repeats the assessment yearly, using the same assessors where possible, so changes reflect real improvement rather than differences in how the questions were interpreted. The score is a guide for where to invest next, not a goal in itself.

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

Third-party scripts run with the same rights as Coastline's own code when included directly in a page, so a compromised vendor could read rider data or change ticket prices shown to users. The brief therefore asks for more than a feature integration. It asks the team to decide how much the widget should be able to reach, how Coastline would notice a malicious change, and how it could be removed quickly.

### 35.2 Vendor risk

Questions to the vendor: Do you follow the SSDF? Do you provide SBOMs and signed releases? How fast do you fix vulnerabilities? Do you have a disclosure process?

The answers show whether the vendor's practices resemble the controls Coastline applies to itself. A vendor that follows the SSDF and signs releases makes verification possible; one that cannot say how fast it fixes flaws leaves Coastline guessing. The team scores answers against a short rubric and asks for evidence, such as a published disclosure policy, rather than accepting yes or no.

### 35.3 Technical isolation

Options: include the vendor's script directly in ticket-web pages; host a pinned copy with an integrity hash; or load the widget in a sandboxed frame on a separate domain. The sandboxed frame limits the widget's access to rider data.

Direct inclusion is easiest but gives the vendor the most power, and the vendor can change the script at any time. A pinned copy with an integrity hash stops silent changes but still runs with full page access. The sandboxed frame keeps the widget in a separate origin, so browser rules stop it reading ticket-web's pages or cookies.

### 35.4 Contractual controls

The contract requires notification of security incidents within 48 hours, SBOM delivery with each release and fixing critical flaws within 14 days.

Each term gives Coastline something to act on. Notification within 48 hours lets the team check exposure before attackers spread. SBOMs feed the same advisory check used for Coastline's own components. The 14-day fix commitment sets an expectation the team can measure and raise with the vendor if missed. Terms are kept specific so both sides can tell whether they are met.

### 35.5 Monitoring

Coastline monitors the widget's domain and versions and alerts on unexpected changes.

Because the widget sits on the vendor's domain, Coastline cannot control its content. It can, however, watch for changes in the script's version, size or the hosts it contacts, and compare them with the vendor's announced releases. An unannounced change triggers a check with the vendor and, if unexplained, use of the exit plan to switch the widget off. Monitoring results are reviewed monthly during the pilot, with any surprises raised at the vendor meeting.

### 35.6 Presentation

The team presents to Ingrid, procurement and legal.

Each audience has different questions. Ingrid cares about isolation and verification; procurement asks about cost and the vendor's terms; legal asks about liability, audit rights and data handling. The team prepares one slide for each concern and keeps the technical detail in an appendix. Presenting to all three together lets disagreements surface early, such as legal wanting stronger audit rights than procurement expected to negotiate. Questions that cannot be answered on the spot are recorded with an owner and a date for a written reply.

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

Growth multiplies the cost of every check, because each one now runs more often and covers more components. A check that adds a minute to each build costs an hour of waiting every day across the team. Slow checks also encourage developers to batch changes or seek exceptions, which weakens the controls they were meant to enforce. Kwame therefore treats speed as a design requirement.

### 36.2 Incremental checks

The dependency gate checks only components that changed in a pull request, and a nightly job checks everything. This cut median gate time from 90 to 15 seconds.

Most pull requests touch few or no dependencies, so checking only what changed avoids repeating work. The nightly full check ensures advisories published for unchanged components are still found, as the worked example on zipx will show. Together they cover everything with far less waiting during the day. If the nightly run finds something, the owner is alerted the next morning.

### 36.3 Safe caching

Advisory data is cached for one hour; the cache key includes the feed's version so stale data is detected. Caches must never be shared between untrusted pull-request builds and release builds, or a poisoned cache could affect releases.

Including the feed version in the cache key means a newer feed invalidates old entries automatically, so the cache cannot hide a fresh advisory for longer than an hour. Separating caches by build type matters because a pull request from a fork runs code nobody has reviewed; if that code could write into the cache used for releases, it could plant a fake 'no advisories' answer. Release builds therefore use their own cache.

### 36.4 Parallelism

Tests and checks run in parallel jobs; provenance generation happens once at the end.

Running independent jobs at the same time shortens the wall-clock time developers wait, without reducing what is checked. Provenance must come last because it describes the final outputs and the steps that produced them; generating it earlier would leave later steps unrecorded. Parallel jobs need separate workspaces, so one job cannot alter files another job is about to check. The pipeline runs each in its own container, which also keeps a failure in one job from leaving debris for the others.

### 36.5 Measuring cost

Kwame measures each control's time: tests 6 minutes, static analysis 2, gate 15 seconds, signing 20 seconds, verification 12 seconds. Security controls are under 10% of CI time.

These figures answer the common complaint that security slows builds: most CI time goes to tests, which the team would run anyway. Measuring each control separately also shows where effort would pay off. Speeding up the gate further would save little, while splitting the test suite would save minutes. Numbers end arguments that impressions start. Kwame repeats the measurement each quarter.

### 36.6 Scale of data

SBOMs for all releases are stored in a searchable index so a question like "which releases contain zipx 1.2.x?" answers in seconds.

Without an index, the same question would mean opening every stored SBOM in turn, which takes long enough to delay a response. The index stores component names and versions for each release, linked to the release digest, so a query returns both which releases contain a component and where those releases run. Wildcard searches over a minor series help when an advisory covers a range of versions.

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

The application logs show misuse of ticket-web itself, while pipeline logs show attempts to change what runs. Together they cover both ways an attacker might reach riders. Each log entry has a time, an account and an action, which lets investigators reconstruct events. Logs are sent to a central store that the application and pipeline accounts can write to but not edit or delete, so an intruder cannot erase evidence of their own actions.

### 37.2 Alerts

Alerts fire on unusual patterns: many authorisation failures from one account, a deployment not from the approved pipeline, or a signature verification failure.

Each alert matches a pattern that is rare in normal operation but common in attacks. Many authorisation failures suggest someone probing for other riders' tickets; a deployment not from the pipeline suggests someone bypassing controls; a verification failure may mean tampering. Alerts are tuned so that each one is worth a person's attention, because an on-call engineer woken often by noise starts to ignore real problems.

### 37.3 Patching

Servers rebuild weekly from updated base images; the application follows the remediation targets.

Weekly rebuilds mean server patches arrive steadily without anyone needing to remember them. Application fixes follow the same remediation targets as other findings: seven days for critical, thirty for high. Because servers are rebuilt rather than patched in place, every server matches its image exactly, and no server keeps an old library that a manual patch missed. The image used by each server is recorded, so the team can list every server still running an image with a known flaw.

### 37.4 Configuration

Configuration is stored as code and compared nightly with running systems; drift is reported.

Drift happens when someone changes a running system by hand, often to fix an urgent problem, and the change never reaches the code. The nightly comparison finds such changes within a day. Each one is either added to the code through review or reverted, so the stored configuration remains a true description of production. Repeated drift in one area suggests the pipeline is missing a needed feature.

### 37.5 On-call

A rota covers security alerts outside office hours, with playbooks.

Attacks do not keep office hours, and a deployment from outside the pipeline at night needs attention before the morning. The rota spreads the load so no one person is always on call, and each shift starts with a short handover. Playbooks give the first steps for each alert type, such as how to check a deployment's origin or freeze releases, so the engineer acts consistently even when tired. The rota is paid and limited in length to avoid burnout.

### 37.6 Working with operations

Security events are shared with Coastline's operations centre.

The operations centre watches network and server health for all Coastline services, and it may see the same event from another angle, such as unusual traffic during an alert on authorisation failures. Sharing events lets both teams join up the picture quickly. Coastline agrees which events go to which team, so nothing falls between them and nobody receives everything. A joint review each quarter checks whether the split still works and whether any events were missed or duplicated.

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

Validation differs from verification at deployment. Deployment checks each artifact once, as it goes out; validation looks at what is actually running at a given moment, which can differ if someone copied files by hand or if a server was missed. The question is answered from evidence, not from what the pipeline intended. That makes it a check on the pipeline itself as well.

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

The policy compares exact strings, so a builder name that differs by one character, such as a similar-looking hostname, is denied. Each denial lists every failing rule, so 3.2.2 would show both problems if it also had the wrong builder. The repository check passes for all three records, since each came from the approved repository.

### 38.3 Investigating denials

3.2.1 was built during the earlier period before all builds moved to CI; it is retired. 3.2.2 came from an emergency change whose after-the-fact review had not been recorded; the review is completed and the release rebuilt.

Both denials had innocent causes, but the investigation was still needed: the same output would appear if an attacker had built a release elsewhere or slipped in an unreviewed commit. Retiring 3.2.1 removes an artifact the team cannot vouch for. Rebuilding 3.2.2 after review produces a new artifact with provenance showing a reviewed commit.

### 38.4 Evidence for auditors

A monthly report lists every running artifact and its policy result, with links to provenance. This supports SSDF PS.2 and PS.3 (archive and protect each release).

Auditors want to see controls working over time, not on one day chosen by the team. A monthly report generated automatically gives that history without extra effort. Links to provenance let an auditor pick any artifact and follow it back to source, builder and review. Keeping the reports for several years supports later questions about past releases. PS.3 asks that releases be archived and protected, which the write-once storage from the implementation work covers.

### 38.5 Continuous validation

The check runs hourly against running servers, not only at deployment.

Checking only at deployment would miss changes made afterwards, such as the manual file copy found by the operations alert. Hourly checks narrow the window in which an unapproved artifact can run unnoticed. A failure raises an alert to the on-call engineer and is added to the monthly report. The check reads digests from running servers and looks them up in the artifact store, so it needs no access to the servers' data. Hourly was chosen as a balance between load on the servers and speed of detection.

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

Signs of abandonment include no recent releases, open security reports without response and maintainers who no longer reply. Not every quiet project is abandoned: a small, finished library may need no changes. Kwame distinguishes them by checking whether reported bugs are answered. The four found were all used in ticket-web's request path, so a flaw in any of them would reach riders with no fix coming.

### 39.2 Replacement planning

For each, options are: replace with a maintained alternative, take over maintenance internally, or remove the feature. qr-make is replaced by a maintained library; one small helper is copied in and owned internally.

The choice depends on size and importance. Replacing qr-make is practical because maintained alternatives exist and the interface is small. Copying the small helper in makes sense because its few lines are easy to understand and test. Taking over maintenance of a large component would cost too much for a team Coastline's size, and removing a feature is chosen only when riders do not need it.

### 39.3 Reducing dependencies

Some packages are used for one tiny function. Removing them reduces attack surface and update work. Kwame removes 11 such packages.

A package used for one tiny function still brings its own dependencies, advisories and update work. Writing the function directly, in a few reviewed lines, removes all of that. Kwame chooses packages to remove by comparing how much of each is actually used. Each removal is a small pull request with tests, so mistakes are easy to spot and revert.

### 39.4 Ownership

Each dependency has an owning team listed in a file in the repository.

An owner receives advisories for the dependency, decides on upgrades and reviews proposals to remove it. Listing owners in the repository means the information changes through review and is visible to everyone. A check fails if a new dependency is added without an owner, so no package arrives unclaimed. When teams reorganise, the file is updated in the same change as the team structure. The owner is a team, not a person, so ownership survives holidays and staff turnover.

### 39.5 Supporting upstream

Coastline sponsors two critical upstream projects and contributes fixes, recognising findings from Wermke et al. (2022) that open-source maintainers often lack resources.

Sponsoring maintainers helps fund the time that fixes, reviews and releases require. Contributing fixes means Coastline's own patches are reviewed by people who know the code and reach every other user. Both reduce the chance that a critical project falls silent. Coastline chooses projects by how much of ticket-web depends on them, using the dependency graph to find the ones with the widest reach. It also reports flaws privately to these projects, following coordinated disclosure, so fixes arrive before details are public.

### 39.6 Control maintenance

Policies and checks are reviewed yearly; obsolete rules are removed.

A rule that no longer matches the system adds noise or, worse, gives false confidence. For example, a check for a package that has been removed still runs and passes, suggesting coverage that does not exist. The yearly review asks of each rule what risk it addresses, whether that risk still exists and whether the rule has fired. Rules with no remaining purpose are removed, and new ones are added for risks found during the year. The review results are recorded so auditors can see why rules changed.

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

Written scope protects everyone. Without it, a test that slows the staging site or touches the wrong system could be treated as an attack, and the testers could face disciplinary or legal consequences. The time window lets operations recognise test traffic, and named contacts mean a problem can be stopped quickly. Production is excluded because riders depend on it. If the team finds something that seems to reach outside scope, such as a link to a vendor system, it stops and asks rather than following it.

### 40.2 WSTG structure

The OWASP Web Security Testing Guide v4.2 organises tests into areas such as configuration, identity, authentication, authorisation, session management, input validation and business logic. The team selects tests matching their ASVS Level 2 requirements.

Selecting tests from the WSTG by matching them to chosen requirements keeps the effort focused. A test for business logic, for example, checks refund limits that no generic scanner understands. Each selected test names the requirement it covers, so results feed straight into the pass or fail table. Areas with no matching requirement are noted, in case the requirement set itself has a gap.

### 40.3 Pipeline review

For the pipeline, the team reviews configuration: branch protection, secret exposure to forks, runner isolation, policy enforcement mode.

These settings decide whether the pipeline controls actually hold. Branch protection that administrators can bypass, secrets visible to fork builds or a policy left in warn mode would each undo much of the design. The review compares the live settings with the intended ones and records any differences. Configuration is read through the CI system's own settings pages and exports, so no change is made during review, and findings are confirmed by a second team member before being reported.

### 40.4 Evidence

Each ASVS requirement gets pass, fail or not applicable, with evidence such as screenshots of configuration or test logs.

Evidence lets someone else confirm the result without repeating the test. A pass with no evidence is a claim; a pass with a log showing the refused request is a fact. Not applicable is recorded with a reason, such as a feature ticket-web does not offer, so reviewers can challenge it if they disagree. Evidence is stored with the report and referenced by requirement identifier, so a later reader can find each item quickly. Screenshots are checked for personal data before being saved.

### 40.5 Results

30 application requirements: 27 pass, 2 fail (session timeout too long; missing rate limit on password reset), 1 not applicable. 12 pipeline requirements: 11 pass, 1 fail (a self-hosted runner still used for a reporting job).

The failures are specific and fixable. A long session timeout leaves accounts open on shared devices; a missing rate limit on password reset lets someone flood riders with reset messages or guess codes. The self-hosted runner breaks the requirement that builds use hosted, isolated runners, even though the job only produces reports.

### 40.6 Reporting

Findings describe the weakness, its impact and the fix, without step-by-step misuse instructions, and go to owners with target dates.

Detailed misuse steps help attackers if the report leaks and add nothing for owners, who need to know what to fix. Each finding states the requirement it fails, the evidence, the likely impact on riders or Coastline, and a suggested fix. Target dates follow the remediation targets by severity. Reports go to the named owners and Ingrid, not to a broad mailing list, and are stored with restricted access until every finding is fixed.

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

The point is to find where time actually goes, which intuition often gets wrong. Each record carries a timestamp for every step, so the medians come straight from the data. Steps owned by different teams are shown on the same chart, which makes handovers visible as well as work.

### 41.2 Finding the bottleneck

Detection takes under a day, fix and review two days, but waiting for the next production release window takes a median of six days. The bottleneck is not security tooling; it is the release schedule.

Without the measurements, the team would likely have bought a faster scanner, since tools are easy to blame. The data shows that a fix sits ready for most of its waiting time. Once the cause is the schedule, the fix is a change to how releases are planned, not a purchase.

### 41.3 Changing the system

Coastline introduces a fast lane: security fixes that pass all checks can deploy any weekday morning with one approver. The median time from advisory to deployed fix falls from 10 to 4 days.

The fast lane changes a policy rather than adding a tool. All the usual checks still apply: tests, gate, signing, provenance and verification. Only the waiting for a release window is removed. The six days saved come straight from the bottleneck measured earlier. Morning deployment keeps the team at hand if something goes wrong.

### 41.4 Cost and risk

The fast lane adds some deployment risk, managed by automatic rollback and verification. Kwame compares expected exposure saved (6 days per advisory times about 20 relevant advisories a year) with the effort of extra deployments (about 30 minutes each).

Six days times twenty advisories is 120 days of exposure avoided each year, while twenty extra deployments at thirty minutes each cost about ten hours of engineering time. The comparison is rough, but the gap is large enough that the decision does not depend on precise numbers.

### 41.5 Choosing next improvements

With data on each step, the team ranks improvements by days saved per hour of effort. Faster triage through automatic owner assignment ranks next.

Ranking by days saved per hour of effort favours small changes with big effects, which are often overlooked in favour of large projects. Automatic owner assignment uses the dependency ownership file to route each advisory immediately, removing the day or so currently spent finding the right person. The ranking is repeated after each change, since removing one bottleneck reveals the next.

### 41.6 Avoiding local optimisation

Speeding up scanning further would save hours, not days; the system view keeps attention on what matters.

Each team naturally improves the part it controls, which can make the overall flow look busy without becoming faster. A scanner that finishes in ten minutes instead of twenty makes no difference when a fix waits six days for release. Coastline asks every proposed improvement to state which step of the measured flow it shortens and by how much. Proposals that cannot answer are deferred until the measurement shows they matter. This keeps effort where riders feel the difference.

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

A good applied question is narrow enough to answer with available data and matters to the people who will use the answer. Kwame's question has two outcomes, so the study can show whether a benefit comes with a hidden cost to developers. Linking it to published research shows why the answer matters beyond Coastline.

### 42.2 Design

A before-and-after comparison over two six-month periods at Coastline, with dependency additions counted from the repository and satisfaction measured by a short anonymous survey. The study uses only repository metadata and anonymous survey answers, with Coastline's approval.

Comparing two periods is the simplest design possible inside one company. Counting additions from repository history gives objective data that cannot be skewed by memory. The survey captures how developers feel, which the counts cannot. Approval from Coastline and the use of metadata only keep the study within what developers agreed to.

### 42.3 Results

New direct dependencies fell from 34 to 19. Survey satisfaction with the dependency process stayed similar (3.8 to 3.7 on a 5-point scale). Justifications most often cited "needed for a new feature" and "replacing an abandoned package".

The fall from 34 to 19 is a drop of about 44%, while the satisfaction score barely changed. The common justifications show that most additions had a clear purpose, which suggests the step filtered out casual additions rather than blocking needed ones. Only direct dependencies are counted, since transitive ones follow from them.

### 42.4 Interpretation

The justification step seems to reduce casual additions without much frustration. But other changes happened at the same time, such as the new checklist and fewer new features in the second period.

Kwame states both explanations openly. The justification step could explain the fall, but so could fewer new features, which would reduce the need for dependencies regardless of the process. Without a comparison group, the data cannot separate these causes, so Kwame describes the result as consistent with a benefit rather than proof of one.

### 42.5 Limitations

One company, two periods, no control group; survey response rate 60%. The findings are suggestive, not conclusive.

Each limit weakens the conclusion in a specific way. A single company may not represent others; two periods may reflect seasonal work patterns; with no control group, other changes cannot be ruled out; and the forty percent who did not answer may feel differently from those who did. Stating these lets readers judge how far to trust the findings and suggests how a better study could be designed, such as the staged rollout Kwame proposes in the worked example.

### 42.6 Reporting

Kwame writes a short paper for a student conference and a summary for Coastline's engineering blog, using synthetic examples.

Different readers need different forms. The conference paper describes methods and limits in full so other researchers can judge or repeat the work. The blog summary tells engineers what was tried and what seemed to help, in plain language. Both use synthetic examples, so no real code, names or internal details from Coastline appear. Coastline reviews both before publication to check nothing confidential slipped through.

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

Twelve weeks is long enough to take on real responsibilities and see work through from start to finish. Working in the platform team gives Kwame direct contact with the pipeline controls he studied, while the application work keeps him close to the code riders use. Learning goals are agreed in the first week and written into his placement plan.

### 43.2 Tasks

He triages dependency advisories, writes authorisation tests, improves gate messages, joins on-call shadowing and helps prepare the annual security review.

The tasks mix routine and project work, which reflects real engineering. Advisory triage teaches him how to read advisories quickly and decide what matters. Writing tests and improving messages produces visible results. On-call shadowing shows how alerts feel at night. Preparing the review shows how evidence is gathered across the whole organisation, and why records kept during the year matter.

### 43.3 Conduct

He signs confidentiality terms, uses only approved systems and data, and never tests outside authorised scope. When he finds an issue in a vendor's widget, he reports it to Ingrid, who handles it with the vendor under the contract.

Reporting the vendor issue through Ingrid, rather than contacting the vendor directly, respects the contract and the relationship Coastline manages. It also follows the practice from earlier chapters of acting within authority. Confidentiality terms cover rider data, internal systems and unreleased plans, and they continue after the placement ends.

### 43.4 Public service

As a public transport operator, Coastline's priority is safe, reliable service for riders. Kwame sees how security work is balanced with service continuity, such as timing upgrades away from peak travel.

A private company might accept brief outages for faster changes, but a transit operator's riders depend on the service to reach work, hospitals and schools. Security work is planned around that need. Kwame notices that upgrades are often scheduled for late evenings on quiet days, and that emergency fixes go through extra checks to avoid breaking ticket sales during peak hours.

### 43.5 Mentoring

Weekly meetings with Ingrid review his work and learning goals.

The meetings follow a simple pattern: what Kwame did, what he learned, what he found hard and what comes next. Ingrid asks him to explain his reasoning on one decision each week, which builds the habit of justifying choices. Learning goals are adjusted as the placement goes on, for example adding on-call shadowing once he was comfortable with triage. Notes from each meeting are kept by Kwame and shared with his course tutor, so the course can see his progress and offer support if needed.

### 43.6 Reflection

Kwame keeps a journal of decisions and lessons, reviewed by his course tutor.

Writing decisions down while they are fresh records the reasons as they were at the time, before hindsight changes them. The tutor's review asks what he would do differently and which course ideas proved useful or needed changing in practice. Kwame notes, for example, that the threat model he learned was helpful, but that real systems had more undocumented flows than expected. Entries avoid confidential details, so the journal can be shared with the course without breaching his placement terms.

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

App stores add a step between Coastline's build and the rider's phone. If a release were altered there, or uploaded by someone who obtained store access, Coastline's own records would not show it. The service fills that gap by checking what the store actually distributes.

### 44.2 Requirements

Check each new app store release within one hour; compare its digest with the signed build record; verify provenance policy; alert on mismatch; produce a monthly report.

Each requirement is testable. One hour matches how quickly a released app spreads to riders' phones; comparing with the signed record checks integrity; the provenance check confirms the source and builder; alerts reach someone able to act, and the monthly report gives evidence over time. Kwame checks that none of them depends on a manual step, so the service keeps working when he is away.

### 44.3 Success measures

All releases checked within one hour; zero missed mismatches in a test set of 20 synthetic releases with 5 deliberate mismatches; false alerts under one per month.

The test set checks detection directly: five mismatches hidden among twenty releases, all of which must be found. The false alert limit protects the people who receive alerts, since a noisy verifier would be ignored. Measures are set before building, so they cannot be adjusted afterwards to fit the results. Ingrid agrees them in writing.

### 44.4 Plan

Twelve weeks: design (2), build (5), test (3), report (2). Weekly reviews with Ingrid and a tutor.

Building takes the largest share because it includes the store integration and the alerting. Three weeks of testing allows time for the test set and fixing what it reveals. Two weeks of reporting is planned rather than squeezed into the end. Weekly reviews catch delays early, while there is still time to adjust scope. Each phase ends with a short demonstration, so progress is shown rather than reported, and the plan states which features would be cut first if the schedule slipped.

### 44.5 Risks

App store APIs may change; mitigation: abstract the fetch step. Access to signing records needs approval; mitigation: request early.

Each risk has a mitigation the team can act on now. Wrapping store access in one module means an API change affects only that module. Requesting access to signing records early allows time for the approval process. Kwame reviews the risk list weekly and adds new ones, such as a reviewer's leave clashing with the testing phase, and records when each risk closes.

### 44.6 Agreement

Ingrid and the course tutor sign the project plan.

The signed plan records the scope, requirements, success measures and timeline that all parties accepted. It protects Kwame from requests that would expand the project beyond twelve weeks, and it gives Ingrid confidence that the result will be usable by the platform team. Changes later need agreement from both signers, with the reason recorded. The tutor's signature confirms the project meets the course's academic standards as well as Coastline's needs, so the work can be assessed fairly at the end.

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

A complete document lets reviewers judge the design without needing Kwame present. The threat model shows which risks he considered, so reviewers can focus on what he missed. The test plan shows how each requirement will be checked. He sends the document a week before the meeting, giving reviewers time to read it carefully. A short cover note lists the parts he is least sure of.

### 45.2 Reviewers

A Coastline security engineer, an external engineer from another transit agency and a course tutor review it.

Each reviewer brings a different view. The Coastline engineer knows the systems and constraints; the external engineer brings experience from another organisation and no attachment to Coastline's choices; the tutor checks the engineering method and the academic standard. Together they cover technical detail, outside perspective and rigour. Reviewers receive the design document a week ahead with a short list of questions Kwame is unsure about.

### 45.3 Findings

Major: the verification service itself holds credentials to the app store API; if compromised, it could hide mismatches. Minor: logging retention unspecified; alert channel single point of failure.

The major finding matters because a verifier that attackers can silence is worse than none: it gives false assurance. Minor findings would not break the design but leave gaps. Without a retention period, logs might be deleted before an investigation needs them or kept longer than necessary. With a single alert channel, one outage could hide every mismatch. Sorting findings by severity tells Kwame what must be resolved before building starts and what can be fixed alongside it.

### 45.4 Responses

For the major issue, credentials are read-only and alerts are also sent to a separate system the service cannot modify. Minor issues are fixed with specific values and a second alert channel.

Read-only credentials mean that even a compromised verifier cannot change app store releases. Sending alerts to a separate system means a compromised verifier could fail to raise an alert but could not delete one already sent, and a missing daily heartbeat from the verifier itself raises an alarm.

### 45.5 Traceability

Every review comment links to the design change it caused, or a reason for no change.

The link lets reviewers check that their comments were handled and see the reasoning when a suggestion was declined. A comment with no response is treated as unresolved. The table also helps future maintainers understand why the design looks as it does, so they do not undo a change made for a good reason. Kwame keeps it in the repository alongside the design document, versioned with each revision, so the history of decisions travels with the code and survives after he leaves.

### 45.6 Value

Independent reviewers see assumptions the author cannot.

Authors know what they meant, so they read their documents as they intended them, not as written. Kwame had not seen that the verifier's own credentials were a target, because he thought of it as a defender. A reviewer with no part in the design asked what an attacker would do with the verifier, and the major finding followed. The cost was two hours of meeting time and a week of revisions, far less than fixing the flaw after the service was running. Kwame now builds review time into every project plan.

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

A verifier that skipped the controls it checks would be an obvious weak point: an attacker who altered the verifier could make every mismatch look clean. Building it through the same pipeline means its own releases are signed, have provenance and pass the dependency gate. Using standard libraries keeps its dependency graph small, which reduces the chance that a third-party package undermines it.

### 46.2 Testing

The test set of 20 synthetic releases includes 5 mismatches: altered file, missing signature, wrong builder, unreviewed commit and an extra file. All 5 are detected; no false alerts on the 15 good releases.

Each mismatch type tests a different check: digest comparison, signature verification, builder policy, review status and file listing. Detecting all five shows every check works, and the absence of false alerts on good releases shows the checks are not over-sensitive. The test set is stored with the code and run on every change.

### 46.3 Timing

Each release is checked in a median of 7 minutes after detection; the slowest takes 22 minutes, within the one-hour target.

Reporting the median and the slowest case together shows both typical behaviour and the margin against the target. Most of the time is spent waiting for store metadata rather than computing. A slowest case of twenty-two minutes leaves plenty of room under the hour, even if store responses slow down. Kwame records the timing of every check, so a gradual slowdown is visible long before it threatens the target.

### 46.4 Unexpected problem

App store metadata sometimes lags; the verifier now retries for up to 45 minutes before alerting "not yet available" rather than "mismatch".

Reporting a mismatch when the data simply has not arrived would produce false alerts, which the success measures limit to fewer than one a month. The new status separates two situations that need different responses. If metadata is still missing after the retry window, the alert says so plainly, and on-call checks the store rather than starting a tampering investigation. Kwame adds this case to the test set, using a synthetic release whose metadata appears late.

### 46.5 Documentation

Operations guide, architecture notes, runbook for alerts and a test report.

Each document serves a different reader. The operations guide explains how to run and update the service. The architecture notes record design choices and their reasons. The runbook tells on-call engineers what each alert means and what to do first. The test report gives evidence that the success measures were met. All four are kept in the repository and reviewed with code changes, so they stay accurate after Kwame leaves.

### 46.6 Handover readiness

Coastline's platform team reviews the code and runs it in staging for two weeks.

Running in staging lets the platform team see the verifier under realistic conditions before relying on it. During the two weeks, its engineers handle any alerts themselves, with Kwame available to explain. Their code review checks that they can understand and change the service without him. Any issues found are fixed before the service moves to production, and the team signs off only when it is confident it can operate the verifier alone. That sign-off is the readiness test.

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

The two failures test different properties. The tampered artifact tests integrity controls: would anything bad reach a server? The signing outage tests failing closed and recovery: do builds stop safely, and do they resume cleanly? Approval names the trial lead, the time window and the systems involved, and only staging is touched.

### 47.2 Expectations

The deployment should refuse the tampered artifact; the verifier should alert; builds should wait during the signing outage and resume afterwards.

Writing expectations before the trial turns it into a test rather than a demonstration. Each expectation can be observed and timed, so the result is clearly pass or fail. If something unexpected happens, the gap between expectation and observation is the lesson. Expectations come from the requirements and the control design, so the trial also checks that the design was implemented as intended.

### 47.3 Observations

The tampered artifact is refused within seconds and the alert reaches on-call in 3 minutes. During the signing outage, builds queue as designed, but one team, unaware of the trial, tries to bypass signing with a manual flag; the policy blocks it.

The alert time comes from the moment the artifact was placed, not when someone noticed. Refusal in seconds shows the digest check ran before any installation step. The blocked manual flag is the surprise: the trial was not meant to test it, yet it showed that a bypass still existed in the configuration and that the policy caught its use. Observations are logged with timestamps by an observer who has no other role.

### 47.4 Recovery

After the outage, queued builds complete within 25 minutes. The mirror is cleaned and its digests rechecked.

Twenty-five minutes reflects the backlog of builds that piled up during two hours, processed with normal capacity. Rechecking every digest on the mirror confirms that only the synthetic artifact was affected and that cleaning it left nothing behind. Recovery counts as finished only when the system is back to a verified state, not when builds simply restart. The team also checks that no build skipped signing during the outage by comparing the build log with the transparency log.

### 47.5 Lessons

Communication: teams need notice of trials and a status page during outages. The manual flag is removed entirely.

The team that tried the manual flag was acting reasonably with the information it had: builds were stuck and nobody had said why. Telling all teams in advance and showing outages on a status page would have prevented the attempt. Removing the flag altogether means no one can try it in future, whether during a trial or a real outage. The emergency path described in earlier chapters, with named approval, remains the only route for urgent fixes.

### 47.6 Measuring

Time to detect: 3 minutes; time to recover: 25 minutes after service return.

These two numbers give the yearly trial a baseline. If detection takes longer next year, the team will look at alert routing; if recovery takes longer, at build capacity or queue handling. Measuring recovery from service return separates Coastline's response from the length of the outage, which Coastline did not control. Both figures are added to the evidence dossier, with the trial date beside them, so next year's result can be compared directly.

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

Assessors need to judge the capstone against academic criteria, while Coastline needs confidence to operate the verifier and rely on the controls around it. One dossier serves both, because both need the same thing: each claim backed by evidence that someone else can check. Without the dossier, the evidence would be spread across repositories, reports and emails, and nobody could easily confirm that everything had been tested.

### 48.2 Structure

For each requirement: statement, implementation, verification method, evidence links and status. Sections cover the verifier, the pipeline controls it relies on and the operational procedures.

Repeating the same fields for every requirement makes the dossier easy to scan and makes missing evidence obvious. The verification method says how the requirement was checked; the evidence links lead straight to the results. Grouping by system part follows how operators think about the service. A status of met, partly met or not met is chosen from evidence, never from intent.

### 48.3 Evidence types

Test reports (chapter 46), design review records (45), failure trial results (47), validation reports (38) and metrics (29).

Different kinds of evidence answer different questions. Tests show the verifier behaves correctly in controlled cases; review records show the design was challenged and improved; the trial shows behaviour under failure; validation reports show the controls hold on running systems; metrics show performance over time. Together they give a fuller picture than any one type could, and an assessor can follow whichever kind best answers their question. Each item carries a date, so readers can tell how recent it is.

### 48.4 Gaps

Two requirements are partly met: monthly reports exist but are not yet reviewed by management; alert response is tested in staging only. Both are stated with plans.

Stating gaps openly makes the rest of the dossier more credible, because readers can see the author is not hiding weaknesses. Each gap has an owner and a date, which turns it from an admission into a plan. Management review of the reports is scheduled for the next quarter; a production test of alert response needs an agreed window with operations.

### 48.5 Usability

The dossier begins with a one-page summary table.

The table lists each requirement with its status and a link to the detail, so a reader can see the overall picture in a minute and go deeper where they need to. Assessors usually sample a few requirements; the summary helps them choose. Operators use it to find the parts that matter to them. Partly met items are marked clearly in the table rather than buried in the detail. The table is generated from the detailed entries, so it cannot drift from them, and it shows the date of the last update at the top.

### 48.6 Maintenance

The dossier is versioned; after handover, the platform team updates it.

A dossier that stops being updated becomes misleading, since the system and its evidence change over time. Versioning lets readers see what changed and when. The platform team adds new test results, trial outcomes and validation reports as they arrive, and closes the two gaps when their plans are complete. A yearly review checks that every link still works and every status is still accurate, and the dossier is included in the material for Coastline's annual security review.

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

The structure follows the engineering work in the order it happened, which helps readers see how each choice led to the next. The background gives readers who do not know supply-chain security enough context to follow the design. Verification and trial chapters present evidence, and the discussion interprets it. Each chapter ends with a link to the next, so the argument reads as one piece. Kwame writes the conclusion last, after the discussion is settled, so it states only what the evidence supports.

### 49.2 Literature connections

The thesis positions the verifier as a consumer-side check complementary to producer-side controls described in SLSA v1.0 and the SSDF, and relates its use of signing and transparency logs to Newman et al. (2022). It cites Ladisa et al. (2023) to show which attack classes the verifier addresses (distribution-stage tampering) and which it does not (malicious source commits by authorised maintainers).

Naming what the verifier does not address is as important as naming what it does. A reader who assumed the verifier covered malicious commits would trust it for the wrong job. Mapping it onto a published taxonomy lets others compare it with their own controls.

### 49.3 Discussion

The verifier detects mismatches between built and published apps quickly, but relies on trustworthy build records; reproducible builds would add an independent check.

This dependency on build records is the verifier's main weakness. If the CI provider or build step were compromised, the records would describe the compromised build as legitimate, and the verifier would confirm a match. Reproducible builds would allow a second builder to produce the same output independently, so a mismatch between builders would reveal tampering in one of them. The discussion explains this honestly instead of presenting the verifier as a complete answer.

### 49.4 Limitations

One organisation, synthetic mismatches, short operating period.

Each limit restricts how far the results can be generalised. One organisation means other transit agencies or app stores might behave differently. Synthetic mismatches test the known types well but may not represent real attacks, which are designed to be hard to detect. A short operating period does not show how the verifier behaves over months of store changes and updates. Kwame explains how each limit affects his conclusions, and which future work would address it.

### 49.5 Future work

Reproducible mobile builds; sharing verification results among transit agencies.

Each item follows from a limitation. Reproducible mobile builds would address the dependence on trustworthy build records. Sharing results among agencies that use the same app vendor would test the approach in other organisations and could detect a problem affecting many of them at once, building on the external reviewer's suggestion. Kwame describes what each would need, so others can pick them up, including the data each would need and who might provide it.

### 49.6 Academic standards

Citations are checked against sources; all case data are synthetic or approved.

Checking citations means reading the source to confirm it says what the thesis claims, not copying references from other papers. Kwame finds one case where he had cited a paper for a broader claim than it makes, and he narrows his sentence. Case data are synthetic or approved by Coastline, and the thesis states this clearly, so readers know no confidential details are disclosed. The tutor checks the reference list and the data statement before submission, and any figures from Coastline are confirmed by Ingrid.

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

Starting with the original incidents reminds examiners why the work matters. The middle part moves quickly through requirements and design to the results, where most attention belongs. Limits and future work come before questions, so examiners see that Kwame knows what the verifier cannot do. He leaves time for questions rather than filling every minute with slides. A single results slide shows the five detected mismatches and timings.

### 50.2 Technical questions

"What if an attacker compromises your CI provider?" Kwame explains that provenance would then be untrustworthy and reproducible builds or a second independent builder would be needed. "Why not verify every file on riders' phones?" He explains privacy and battery costs, and that store-level checks catch tampering before installation.

Both answers show he understands the boundaries of his design. The first admits a real weakness and names a remedy instead of defending the design at all costs. The second explains a choice in terms of riders' interests, privacy and battery life, and shows that the chosen check sits at a point where it still catches the threat. Examiners look for this kind of reasoning more than for perfect designs.

### 50.3 Ethical questions

"Could the verifier's data reveal riders?" No: it handles only app releases, not rider data.

Kwame explains the answer further: the verifier reads release files and build records from the store and Coastline's systems, and it never touches riders' phones or accounts. Logs record releases and check results only. He adds that the verifier could still affect riders indirectly, for example if a false alert delayed a needed security update, which is why the false alert rate was a success measure. Examiners also ask about disclosure, and he describes how a real mismatch would be reported through Coastline's incident process.

### 50.4 Reflection

From calculus models of exposure to a deployed verifier, Kwame sees supply-chain security as an engineering discipline of requirements, design, measurement and verification.

Looking back, he notices how the first-year incidents shaped every later step. The template advisory led to SBOMs and advisory checks; the mirror mismatch led to digests, signing and provenance. Mathematics and physics courses that once seemed distant gave him ways to model exposure and reason about corruption. He ends with the view that controls are only as good as the evidence that they work.

### 50.5 Development

He plans a professional certification and joins an open-source supply-chain security working group.

A certification gives a structured way to keep his knowledge current and shows employers what he knows. The working group connects him with engineers who face similar problems in other organisations and lets him contribute to shared tools and standards. He also plans to keep reading new research, since attack classes and defences change quickly. Ingrid agrees to remain an informal mentor, meeting him monthly to review his goals.

### 50.6 Thanks

Ingrid and the Coastline team receive the final dossier and verifier.

The handover is a way of saying thanks in practice, since the work stays with the organisation that supported it. Kwame also thanks his tutor, the reviewers and his classmates who played examiners. He notes in his thesis acknowledgements that the external reviewer's suggestion changed his future work. Coastline's leadership thanks the platform team for hosting him, and the verifier is listed as a team project in the next annual security review, with Kwame named as its original author.

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
