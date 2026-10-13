# Cloud and Container Security: Engineering Course

- Language: English (`en`); course 128, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; Nine offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students learning to design, implement, verify and operate security controls for cloud and containerised platforms.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only cloud accounts, clusters and workloads you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Misconfigurations are taught from the defender's side using synthetic configurations, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one engineering student on an industry project with an energy co-operative whose smart-meter platform leaked a cloud key in a public image and ran without network policies. They move from mathematics, computing and security foundations through requirements, models, threat analysis, control design, implementation, measurement, verification labs, reliability, operations, validation and optimisation to a capstone, a failure trial, an evidence dossier, a thesis and a defence. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Elena Petrova** | Engineering student | Invented |
| **Rosa Delgado** | Industry supervisor | Invented |
| **Dr Felix Wagner** | Academic tutor | Invented |
| **Brackenridge Institute of Technology** | Fictional institute | Invented |
| **Solent Energy Co-op** | Fictional energy co-operative running meterhub | Invented |

### Core sources

NIST [SP 800-145](https://doi.org/10.6028/NIST.SP.800-145), [SP 800-210](https://doi.org/10.6028/NIST.SP.800-210), [SP 800-190](https://doi.org/10.6028/NIST.SP.800-190) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); CSA [Cloud Controls Matrix v4](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); the [AWS](https://aws.amazon.com/compliance/shared-responsibility-model/), [Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) and [Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) shared responsibility pages; Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation. Full list in [References](#references).

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

You will (1) use rates of change to describe how cloud resources and risks grow; (2) interpret derivatives as rates in operational data; (3) reason about accumulation; (4) connect calculus to the opening case.

### 1.1 The opening case

Elena Petrova is a fifth-year engineering student at the fictional Brackenridge Institute of Technology, on an industry project with the fictional Solent Energy Co-op under industry supervisor Rosa Delgado and academic tutor Dr Felix Wagner. Solent runs meterhub, a Kubernetes-hosted platform that ingests smart-meter readings from 80,000 homes. Last spring a container image for meterhub with a cloud access key built into one layer was pushed to a public registry by mistake, and the meterhub namespace had no network policies, so any pod could reach the readings database. The key was revoked within hours and no misuse was found, but the review asked for an engineered approach rather than patches.

The leak and the missing network policies give the course two threads to follow: how secrets end up where they should not, and how traffic inside a cluster is controlled. Elena's project brief asks her to understand both, design fixes that the small platform team can operate, and show with evidence that the fixes work. Each later chapter adds a tool she uses on that brief.

### 1.2 Rates of change

Engineers describe systems by how quantities change. If the number of running pods P changes over time t, dP/dt is the rate of scaling. When meterhub's ingest rate rises in the evening, the derivative of request volume tells the autoscaler how quickly capacity must grow.

The derivative matters because capacity cannot appear instantly: a new pod needs time to start, pull its image and pass its health checks. If demand rises faster than pods can start, requests queue or fail. Knowing the steepest evening rise lets Elena check whether the autoscaler's settings react quickly enough, or whether a small buffer of spare pods should run before the peak arrives.

### 1.3 Accumulation

The integral of a rate gives a total. The integral of exposure over time, for example the number of reachable sensitive services multiplied by hours, gives a measure of accumulated risk. Elena uses this idea later to compare designs: a short, wide exposure can matter as much as a long, narrow one.

Consider a database port accidentally reachable from the internet for two hours, against an internal admin service reachable from every pod for a month. The first is wide but brief; the second is narrow but long. Multiplying reach by time puts both on one scale, so the team can compare them honestly instead of reacting only to whichever sounds more alarming.

### 1.4 Growth of configuration

Each new microservice adds configuration. If services grow linearly but permissions per service grow too, total permissions grow faster than linearly, which explains why manual review stops scaling.

If each of ten services needs five permissions, a reviewer checks fifty entries; if forty services each need twelve, the count is 480, and many of them interact. Reviews that once took an afternoon now take a week and are done less carefully. This growth is the main argument for checking configuration with programs and policies rather than by reading every line by hand.

### 1.5 Approximation

Small steps approximate continuous change: sampling metrics every 30 seconds approximates the true curve, and the sampling interval limits how fast a change can be seen.

A spike lasting ten seconds may fall entirely between two 30-second samples and never appear in the graph. Shorter intervals reveal more but cost storage and processing. Elena checks the sampling interval of each metric she plans to use for alerts, because an alert can only fire on changes the samples actually capture. Alert rules state their interval.

### 1.6 Why maths first

Later chapters use rates for autoscaling, statistics for alert latency and logic for policy evaluation. The foundations make those designs analysable rather than guessed.

Guessed designs are hard to defend when someone asks why a threshold is five rather than ten, or why one design is safer than another. With rates, distributions and logic, Elena can show the reasoning and let others check it. The maths in these first chapters is kept to what the later engineering work actually uses.

### Worked example

Elena estimates the accumulated exposure of the leaked key: one credential reachable publicly for 5 hours with access to 3 storage buckets gives 15 bucket-hours. She compares this with the namespace's missing network policies: 12 reachable pod pairs for an estimated 400 days, a much larger accumulated exposure, though of a different kind. The comparison helps Rosa explain why both issues need engineering fixes.

> **Synthetic case.** Brackenridge, Solent Energy Co-op, meterhub and all figures are synthetic.

### Errors and limits

Accumulated exposure is a simplified measure; it ignores how likely each exposure was to be used.

### Exercises

- **EX001 — Derivative meaning.** What does dP/dt describe for pods? *Rubric:* 3 = rate of scaling; 2 = partial; 1 = none; 0 = none.
- **EX002 — Integral use.** How can an integral measure risk? *Rubric:* 3 = exposure accumulated over time; 2 = partial; 1 = none; 0 = none.
- **EX003 — Leak estimate.** What was the leaked key's accumulated exposure? *Rubric:* 3 = 15 bucket-hours; 2 = partial; 1 = none; 0 = none.

### Synthesis

Rates and accumulation give engineers a language for growth and exposure.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) express access policies as logic and sets; (2) evaluate requests with default deny and explicit deny; (3) reason about policy combinations; (4) test a small evaluator.

### 2.1 Policies as logic

An access policy is a set of rules, each matching a principal, an action and a resource. A request is allowed if some allow rule matches and no deny rule matches; otherwise it is denied by default. This is a logical formula: allowed = (exists allow match) and not (exists deny match).

Writing the rule as a formula makes its behaviour predictable. Two results follow directly: a request that matches nothing is denied, and a single matching deny beats any number of allows. Elena uses the formula to explain to the platform team why adding another allow rule did not fix a denied request, because a deny elsewhere was still matching it.

### 2.2 Sets and wildcards

Wildcards describe sets: storage:Get* is the set of all get actions; readings/* is all objects under readings. Reasoning about overlaps between sets explains surprising results, such as a broad allow being overridden by a narrow deny.

Wildcards are convenient but easy to over-grant: storage:* includes deletes and permission changes that the writer may never have intended. Thinking of each pattern as a set, and asking what is inside it, helps spot such over-reach. Overlaps also explain conflicts, since two rules with overlapping sets both match some requests and the combining rule decides the outcome.

### Lab — Lab — policy evaluation

```python
"""Evaluate synthetic access requests: default deny, explicit deny overrides allow (stdlib only)."""
from fnmatch import fnmatch
policies = [
    ("allow", "meter-reader", "storage:Get*", "readings/*"),
    ("allow", "meter-reader", "storage:*", "readings/raw/*"),
    ("deny",  "*",            "storage:Delete*", "readings/*"),
    ("allow", "ops-admin",    "storage:*", "*"),
]
requests = [
    ("meter-reader", "storage:GetObject", "readings/2026/10.csv"),
    ("meter-reader", "storage:PutObject", "readings/raw/a.csv"),
    ("meter-reader", "storage:DeleteObject", "readings/raw/a.csv"),
    ("ops-admin", "storage:DeleteObject", "readings/old.csv"),
    ("billing-job", "storage:GetObject", "readings/2026/10.csv"),
]
for who, act, res in requests:
    m = [e for e, p, a, r in policies if fnmatch(who, p) and fnmatch(act, a) and fnmatch(res, r)]
    d = "DENY (explicit)" if "deny" in m else ("ALLOW" if "allow" in m else "DENY (default)")
    print(f"{who:13} {act:21} {res:22} {d}")
```

Run with `python3 lab_policy.py`. Verified output:

```text
meter-reader  storage:GetObject     readings/2026/10.csv   ALLOW
meter-reader  storage:PutObject     readings/raw/a.csv     ALLOW
meter-reader  storage:DeleteObject  readings/raw/a.csv     DENY (explicit)
ops-admin     storage:DeleteObject  readings/old.csv       DENY (explicit)
billing-job   storage:GetObject     readings/2026/10.csv   DENY (default)
```

### 2.3 Lab result

meter-reader may get readings/2026/10.csv and put readings/raw/a.csv (ALLOW). meter-reader's delete of readings/raw/a.csv is DENY (explicit) because the deny on storage:Delete* for readings/* matches, overriding the broader allow. ops-admin's delete of readings/old.csv is also DENY (explicit): the deny rule applies to everyone. billing-job has no matching allow, so it is DENY (default).

The lab's value is in the reasons as much as the outcomes. Two denials look the same to the caller but come from different causes: one from an explicit guardrail, one from a missing allow. Fixing them needs different actions. For billing-job, an allow must be added if the access is legitimate; for the delete guardrail, the team must decide whether any exception is justified at all.

### 2.4 Why this structure

Default deny means forgotten cases fail safe. Explicit deny lets a security team set guardrails that application teams cannot override with broad allows. NIST SP 800-210 discusses such policy combination in cloud access control.

Without default deny, a new resource created without a policy would be open until someone noticed. Without explicit deny, any team with permission to write allow rules could widen access beyond what the security team intended. Together they give a predictable floor and ceiling, within which application teams can grant what they need.

### 2.5 Proving properties

With the formula, Elena can argue properties such as "no principal can delete readings" by showing the deny rule covers every delete action on readings, regardless of allows.

A test checks a few cases; an argument from the formula covers all cases at once. If every delete on readings matches a deny, no allow can change the result, whatever principals or rules are added later. Elena still writes tests for a sample of cases, so a mistake in her reasoning or a change in the rules would be caught.

### Worked example

Rosa asks whether ops-admin should be able to delete old readings for retention. Elena shows that, as written, nobody can; a retention job would need a narrower exception, such as excluding a retention prefix from the deny. They decide retention will use storage lifecycle rules instead, keeping the deny absolute.

> **Synthetic case.** Policies and requests are synthetic.

### Errors and limits

Real cloud policy languages have more conditions; check the provider's documented evaluation logic.

### Exercises

- **EX004 — Formula.** Write the allow formula. *Rubric:* 3 = allow match and not deny match; 2 = partial; 1 = none; 0 = none.
- **EX005 — Lab deny reasons.** Why were the two deletes denied? *Rubric:* 3 = explicit deny on Delete* for readings/*; 2 = partial; 1 = none; 0 = none.
- **EX006 — billing-job.** Why was billing-job denied? *Rubric:* 3 = no allow, default deny; 2 = partial; 1 = none; 0 = none.

### Synthesis

Logic makes policy behaviour predictable and provable.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical limits to cloud systems; (2) reason about latency, energy and failure in data centres; (3) understand why regions and zones exist; (4) connect physical location to data protection.

### 3.1 Distance and latency

Signals in fibre travel at roughly two-thirds the speed of light, about 200 km per millisecond. A round trip between regions 1,000 km apart costs at least 10 ms before any processing. meterhub keeps its database in the same region as ingest for this reason.

Ten milliseconds sounds small, but an application that makes twenty sequential database calls per request would add 200 ms if the database sat in another region. Users notice delays of that size. Physics sets a floor that no amount of engineering removes, which is why data placement is decided early in a design rather than adjusted later.

### 3.2 Zones and regions

Providers group data centres into availability zones (separate power and cooling) within regions. Spreading workloads across zones protects against a single facility failure; regions protect against wider events.

A zone failure might come from a power fault or a cooling problem in one facility; a regional event might be a major network outage or a natural disaster affecting several facilities. Spreading across zones is relatively cheap and handles the common case. Spreading across regions costs more, adds latency and complicates data protection, so it is reserved for services that truly need it.

### 3.3 Energy and heat

Computing turns electrical energy into heat. Data-centre capacity is limited by power and cooling, which is why providers price resources and why idle over-provisioned clusters waste money and energy.

Every idle node draws power and needs cooling even when it does no useful work. A cluster sized for the evening peak all day long wastes most of that energy in quiet hours. Autoscaling and right-sizing reduce both the cost and the energy used, which matters to an energy co-operative whose members care about efficiency.

### 3.4 Hardware failure

Disks, memory and power supplies fail at measurable rates. At scale, failures are routine, so cloud systems are designed to replace failed parts automatically. Verma et al. (2015) describe how Google's Borg handled machine failures as normal events.

At the scale of a large cloud, disks fail daily somewhere, so systems that treat failure as an emergency would be in permanent crisis. Borg's approach of rescheduling work automatically when a machine fails became a model for Kubernetes. For meterhub, it means pods should be written so that losing one and starting another elsewhere does no harm.

### 3.5 Location and data protection

Meter readings are personal data about household behaviour. Where data are physically stored affects which laws apply; Solent keeps readings in one jurisdiction, recorded in its data register.

Readings taken every half hour can reveal when a household wakes, leaves and returns, so they are personal data under most data protection laws. Storing them in one jurisdiction keeps the legal picture simple. The data register records where each data set lives, which lets Solent answer regulators and members accurately. Backups stay in-jurisdiction too.

### 3.6 Shared hardware

Workloads from different customers may share physical machines. Ristenpart et al. (2009) showed that co-residence could leak information, which drove providers to strengthen isolation; customers handle the rest through their own configuration choices.

Co-residence research showed that, under some conditions, one virtual machine could learn information about another on the same physical host. Providers responded with stronger isolation and placement controls. What remains for customers is their own configuration: who can reach their services, which secrets their workloads hold, and how their data are protected.

### Worked example

Elena checks meterhub's zones: all ingest pods run in one zone. A zone outage would stop ingestion for 80,000 meters. She proposes spreading pods across three zones and estimates the extra cross-zone latency at under 2 ms, acceptable for ingest.

> **Synthetic case.** Figures are synthetic and approximate.

### Errors and limits

Physical estimates give lower bounds; real latency includes processing and queuing.

### Exercises

- **EX007 — Latency bound.** What is the minimum round trip for 1,000 km? *Rubric:* 3 = about 10 ms; 2 = partial; 1 = none; 0 = none.
- **EX008 — Zones.** What does spreading across zones protect against? *Rubric:* 3 = single facility failure; 2 = partial; 1 = none; 0 = none.
- **EX009 — Zone finding.** What did Elena find in meterhub? *Rubric:* 3 = all ingest in one zone; spread to three; 2 = partial; 1 = none; 0 = none.

### Synthesis

Physical limits shape cloud architecture and resilience.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small, safe Python programs that read configuration data; (2) use functions, loops and data structures; (3) test programs with synthetic inputs; (4) follow stdlib-only lab rules.

### 4.1 Why programming

Cloud and container configuration is data: YAML, JSON and key-value settings. Engineers who can read and check that data with programs can review hundreds of resources reliably.

A cluster with forty services may have hundreds of manifests and thousands of settings. Reading them by eye invites mistakes, especially late in a review. A short program can check every manifest for the same issues in seconds and produce a consistent list, which a human then examines with fresh attention. Rosa reviews each script's output.

### 4.2 Core structures

Dictionaries map names to settings, lists hold resources, sets hold permissions. Elena represents each pod's security settings as a dictionary, which makes comparisons simple.

Representing settings as dictionaries means a check like 'is privileged true?' is a single lookup. Lists of resources can be filtered and counted. Sets of permissions can be compared with set operations, such as finding permissions one role has that another lacks. Choosing the right structure keeps the code short and clear. Elena keeps each structure small.

### 4.3 Functions and tests

A function such as check_pod(spec) returns a list of issues. Small tests with synthetic specs confirm it flags privileged pods and passes compliant ones.

Returning a list of issues, rather than printing them, lets other code count, sort or filter the results. Synthetic specs give known answers: a pod with privileged set should produce exactly one issue, a compliant pod none. When the function is changed later, the tests show immediately if it still behaves correctly. Edge cases get their own tests.

### 4.4 Reading files safely

Programs only read configuration exports; they never call cloud APIs to change anything. Inputs are treated as untrusted: missing fields are reported, not assumed.

Reading exports avoids any chance of a script changing a live system by mistake, and it means the scripts need no cloud credentials. Treating inputs as untrusted guards against odd or malformed exports. A missing field reported as missing is honest; one silently treated as false could hide a real problem. Each script states which export it expects.

### 4.5 Stdlib only

Labs use only Python's standard library (json, csv, hashlib, statistics, re), so they run anywhere without installing packages, and their behaviour is easy to review.

Each external package is code from outside that may change, break or be compromised. The standard library covers parsing, hashing, statistics and pattern matching, which is enough for these labs. Students can run them on any machine with Python and review every line without needing to understand third-party code. The labs record the Python version used.

### 4.6 Clear output

Output names the resource, the issue and the reason, so non-programmers can act on it.

An output line such as 'ingest-7f9: privileged=true; privileged containers can access the host' tells a manager what is wrong and why it matters. Listing only a rule identifier would force them to look it up. Clear output also helps engineers fix issues quickly, because the resource and the reason are given together. Elena also sorts issues by severity, so the most serious appear first.

### Reading exports

The pod export is a JSON list. Elena's program loops over each pod, then each container, and checks whether a resources.limits field exists with both cpu and memory. Pods are reported by namespace and name so owners can find them. She keeps the input file name and its hash in the output so the result can be traced to the exact export. Writing the program also teaches her how Kubernetes nests settings, which helps in later chapters on pod security.

### Worked example

Elena writes a 40-line program that reads a JSON export of meterhub pods and lists those without resource limits. It finds 6 of 22 pods missing limits. A colleague reviews the code and adds a test for pods with limits on only one container.

> **Synthetic case.** Exports and counts are synthetic.

### Errors and limits

A program is only as good as its tests; check edge cases.

### Exercises

- **EX010 — Config as data.** Why can programs help with configuration? *Rubric:* 3 = configuration is data; scale; 2 = partial; 1 = none; 0 = none.
- **EX011 — Stdlib reason.** Why use only the standard library? *Rubric:* 3 = runs anywhere, easy to review; 2 = partial; 1 = none; 0 = none.
- **EX012 — Limits program.** What did Elena's program find? *Rubric:* 3 = 6/22 pods missing limits; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small, tested programs make configuration review reliable.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write clear technical documents for different audiences; (2) structure design notes and incident summaries; (3) use diagrams effectively; (4) present trade-offs honestly.

### 5.1 Audiences

Rosa's platform team needs exact configuration changes; Solent's managers need risk and cost; the regulator needs evidence of controls. Elena writes one design note with a short summary for managers and detailed sections for engineers.

Each audience reads for a different purpose. Engineers need to know exactly what to change and how to test it; managers need to decide whether to fund and approve; regulators need confidence that controls exist and work. Writing one document with layered sections serves all three without forcing anyone to read what they do not need.

### 5.2 Structure

Context, problem, options, decision, consequences, open questions. This structure, common in architecture decision records, makes reasoning visible.

A fixed structure helps readers find what they want and helps writers spot what they forgot. Writing options before the decision shows the choice was considered, not assumed. Consequences include costs and risks, not only benefits. Open questions show what is still uncertain, so readers know where judgement may change later. Elena's first note runs to two pages, with the manager summary in the first paragraph.

### 5.3 Diagrams

A diagram of meterhub shows ingest, API, database and metrics pods, with arrows for allowed traffic. Trust boundaries are drawn as dashed lines. One diagram per question avoids clutter.

Arrows for allowed traffic make it obvious what should and should not talk. Dashed trust boundaries show where checks must happen. A diagram trying to show deployment, data flow and permissions at once becomes unreadable, so Elena draws separate diagrams for each question and labels each one with its purpose. Each diagram is dated.

### 5.4 Incident summaries

The key-leak summary states timeline, impact, cause, fixes and lessons, without blame and without guessing.

Blame shuts down honest discussion; people who fear blame hide details. Guessing replaces evidence with stories that may be wrong. The summary sticks to what is known, says what is not, and focuses on fixes that change the system, such as scanning images for secrets before they are published. Elena drafts the summary from the recorded timeline and asks the engineers involved to correct any errors before it circulates.

### 5.5 Trade-offs

Every option has costs. Elena writes "default-deny network policies will block undocumented traffic; we expect some breakage during rollout" rather than hiding it.

Admitting expected breakage builds trust and helps planning. If teams know default-deny policies will block undocumented traffic, they can prepare by documenting flows and watching closely during rollout. Hiding the cost would only mean surprise and frustration later, and a design that loses support at the first problem. Rosa agrees with Elena on a rollback plan for each expected problem.

### 5.6 Review

Documents are reviewed by an engineer and a non-engineer to check both clarity and accuracy.

An engineer checks that the technical content is correct; a non-engineer checks that the summary and reasoning make sense to someone outside the field. Each catches different problems. Elena asks a Solent operations manager to read her design note and rewrites two paragraphs that the manager found confusing. Reviewers' comments and Elena's responses are kept with the note, so later readers can see what changed and why.

### Writing incident summaries

For the key-leak summary Elena writes short dated entries: when the image was built, when it was pushed, when the key was found, when it was revoked. Each entry cites a log or ticket. Readers can then check the facts, and the summary stays useful months later.

### Presenting

Elena presents the design note to the platform team in ten minutes: one slide for the problem, one for each option with its cost, and one for the recommendation. Questions are recorded and answered in the next version of the note.

### Worked example

Elena's first design note proposes three fixes. Rosa's manager reads only the summary and asks which fix matters most. Elena revises the summary to rank them with one sentence each on risk reduced and effort required.

> **Synthetic case.** Documents are synthetic.

### Errors and limits

Long documents without a summary are rarely read.

### Exercises

- **EX013 — Note structure.** List the design note sections. *Rubric:* 3 = context, problem, options, decision, consequences, questions; 2 = four; 1 = two; 0 = none.
- **EX014 — Trade-off honesty.** How did Elena state a trade-off? *Rubric:* 3 = expect breakage during rollout; 2 = partial; 1 = none; 0 = none.
- **EX015 — Summary revision.** What did the manager need? *Rubric:* 3 = ranked fixes with risk and effort; 2 = partial; 1 = none; 0 = none.

### Synthesis

Write for the reader and show trade-offs openly.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) model growth and decay in cloud systems with exponential functions; (2) use series for approximations; (3) analyse queue build-up; (4) apply models to capacity and backlog.

### 6.1 Exponential growth

If meterhub's number of meters grows 3% a month, the count after n months is N0 × 1.03^n. In two years it roughly doubles. Planning capacity on linear assumptions would leave the platform short.

Starting from 80,000 meters, 3% monthly growth gives about 114,000 after a year and roughly 163,000 after two. A linear plan adding 2,400 meters a month, the first month's increase, would predict only about 137,600 at two years, leaving a gap of some 25,000 meters' worth of ingest capacity. Elena puts both curves on one chart so Solent's managers can see where the plans diverge and when.

### 6.2 Decay

Old log data loses value over time and storage costs accumulate; retention policies model value decaying while cost grows linearly. The crossing point suggests how long to keep detailed logs.

Detailed request logs are most useful in the days after an event, when incidents are investigated; months later they are rarely read, yet each month kept adds to the storage bill. Plotting falling value against rising cumulative cost shows where keeping more stops paying off. Summaries can be kept longer than raw detail, so value is not lost entirely when the detailed copy expires.

### 6.3 Queues

If readings arrive faster than they are processed, the backlog grows at the difference of the rates. Integrating the difference over an evening peak gives the backlog size, which sets queue capacity.

In the evening, meters report while households cook and heat, so arrivals exceed processing for a while and the queue grows. After the peak, processing catches up and the queue drains. Integrating the excess gives the largest backlog, and the queue must hold at least that many readings, plus a margin, or readings will be dropped at the busiest time.

### 6.4 Series approximations

For small rates, (1 + r)^n ≈ 1 + nr, a quick estimate. Engineers use such approximations to check whether a detailed model's answer is plausible.

For a 2% rise over five months, the shortcut gives 10% and the exact figure is about 10.4%, close enough to confirm a spreadsheet is sane. Over thirty months the shortcut says 60% while the true growth is about 81%, so the approximation is only for quick checks, never for the final plan. Elena uses it to catch typing mistakes in her capacity model.

### 6.5 Sensitivity

Derivatives of a model with respect to its inputs show which assumptions matter most. For backlog, the processing rate matters more than the arrival rate near saturation.

Near saturation, a small drop in processing speed sends the backlog climbing steeply, while a similar change in arrivals has a gentler effect. This tells Elena where to spend effort: making ingest pods faster or adding one more replica has a bigger payoff than trying to smooth meter reporting times. Sensitivity also shows which estimates need the most careful measurement.

### 6.6 Security link

Security events also accumulate: unreviewed alerts, unrotated keys. Modelling backlogs shows when manual processes will fall behind.

If twenty keys need rotating each month but the team only manages fifteen, the overdue count grows by five every month and never recovers on its own. The same arithmetic applies to unreviewed alerts or pending access requests. Seeing the growth early justifies automating rotation or adding time, before the backlog becomes an audit finding or a breach. Elena charts the overdue count monthly.

### Checking with data

Elena compares her growth model with twelve months of synthetic meter counts. The model fits within 4%, which gives confidence for planning the next year. Where it diverges, in a month when a new housing estate joined, she notes that step changes need separate planning.

### Worked example

Elena models the evening peak: arrivals of 1,500 readings per second for two hours against processing of 1,200 per second. The backlog reaches about 2.2 million readings, which the current queue cannot hold. The team raises processing capacity rather than queue size, because a long queue also delays fraud and tamper alerts.

> **Synthetic case.** Rates are synthetic.

### Errors and limits

Models simplify; real arrivals are bursty, so add margin.

### Exercises

- **EX016 — Doubling.** How does 3% monthly growth behave over two years? *Rubric:* 3 = roughly doubles; 2 = partial; 1 = none; 0 = none.
- **EX017 — Backlog.** What was the evening backlog? *Rubric:* 3 = about 2.2 million; 2 = partial; 1 = none; 0 = none.
- **EX018 — Decision.** Why raise processing not queue size? *Rubric:* 3 = long queue delays alerts; 2 = partial; 1 = none; 0 = none.

### Synthesis

Growth and queue models show when systems and processes fall behind.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) summarise operational measurements with appropriate statistics; (2) understand skewed distributions; (3) use percentiles for service objectives; (4) avoid misleading averages.

### 7.1 Distributions

Many cloud measurements, such as response times and alert delays, are skewed: most are small, a few are very large. The mean is pulled by large values; the median describes the typical case; high percentiles describe the worst common cases.

An average response time of 300 ms could hide that most requests take 100 ms while a few take several seconds. Users who hit those slow requests have a poor experience, and for alerts, a slow delivery could mean a late response to an incident. Reporting median and high percentiles together gives a truer picture than any single number.

### Lab — Lab — alert latency

```python
"""Summarise synthetic alert latencies (minutes): mean, median, 95th percentile (stdlib only)."""
import statistics
lat = [2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 9, 10, 12, 15, 21, 38, 95]
q = statistics.quantiles(lat, n=20, method="inclusive")
print(f"n {len(lat)}, mean {statistics.mean(lat):.1f}, median {statistics.median(lat)}, p95 {q[18]:.1f}, max {max(lat)}")
```

Run with `python3 lab_latency.py`. Verified output:

```text
n 20, mean 13.2, median 6.5, p95 40.9, max 95
```

### 7.2 Lab result

Twenty synthetic alert latencies have mean 13.2 minutes, median 6.5, 95th percentile 40.9 and maximum 95. The mean is twice the median because of a few long delays; the p95 shows that about one alert in twenty takes over 40 minutes, which matters for incidents such as a leaked key.

The maximum of 95 minutes is one alert that took over an hour and a half to reach anyone, which in a key-leak scenario could mean the key was used in that time. The mean alone would suggest a moderate delay; the p95 shows the real risk lies in the tail. Elena follows up the slowest cases to find out why they took so long.

### 7.3 Objectives

Solent sets an objective that 95% of critical alerts reach the on-call engineer within 15 minutes. The current p95 of 40.9 minutes misses it, and the long tail becomes an engineering problem to solve.

An objective turns a vague wish into a measurable target. Fifteen minutes is chosen because a leaked key or exposed service can be abused quickly once found. Missing the target by a wide margin shows the alert path needs redesign, such as paging directly rather than through a shared mailbox, and the same measure later shows whether the fix worked.

### 7.4 Sampling

Twenty values are a small sample; percentiles from small samples are uncertain. Elena collects a month of data before drawing conclusions.

With twenty values, the 95th percentile rests on just one or two observations, so a single unusual alert can move it dramatically. A month gives hundreds of values and a much steadier estimate. Elena reports the sample size alongside each percentile, so readers know how much weight to place on it. She also checks whether the month was typical, since a holiday period could make alert traffic unusually light.

### 7.5 Probability of events

If a control fails independently with probability 0.01 per day, the chance of at least one failure in a year is 1 − 0.99^365, about 97%. Rare daily events become near certain over time.

The calculation uses the complement: the chance of no failures in a year is 0.99 multiplied by itself 365 times, about 2.6%, so at least one failure is about 97% likely. This explains why systems that 'almost never' fail still fail regularly at scale. It argues for monitoring every control and designing for recovery, not assuming success.

### Choosing the objective

The 15-minute objective is chosen with the on-call team, based on how fast a leaked key must be revoked to limit harm. Objectives set without the people who must meet them tend to be ignored. Elena records the reasoning beside the objective so it can be revisited when the alert system changes. She also proposes measuring it monthly and reporting misses with their causes, not just the percentage.

### Worked example

Looking at the longest delays, Elena finds they all come from alerts routed through a shared email list checked only in working hours. Routing critical alerts to the paging system is expected to remove the tail.

> **Synthetic case.** Latencies are synthetic.

### Errors and limits

Percentiles from small samples are unstable; report sample size.

### Exercises

- **EX019 — Lab stats.** What were mean, median and p95? *Rubric:* 3 = 13.2, 6.5, 40.9; 2 = two; 1 = one; 0 = none.
- **EX020 — Yearly chance.** What is the chance of at least one failure in a year at 0.01/day? *Rubric:* 3 = about 97%; 2 = partial; 1 = none; 0 = none.
- **EX021 — Tail cause.** What caused the long delays? *Rubric:* 3 = email list checked in working hours; 2 = partial; 1 = none; 0 = none.

### Synthesis

Use medians and percentiles for skewed operational data.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) describe CPUs, memory and storage as they appear in virtual machines and containers; (2) understand virtualisation's hardware support; (3) relate architecture to isolation; (4) reason about resource limits.

### 8.1 Processors and memory

Virtual machines run on physical CPUs with hardware virtualisation support, which lets a hypervisor isolate guests. Containers share the host kernel and are isolated by kernel features instead.

Hardware virtualisation gives each guest its own virtual processors and memory, with the hypervisor enforcing boundaries. Containers are lighter because they share one kernel, but that also means a kernel flaw can affect every container on the host. For meterhub, the choice affects how strongly workloads from different teams are separated on the same node.

### 8.2 Memory and isolation

Each process has its own virtual address space. Hardware memory management enforces separation; flaws in this area, such as speculative execution issues, are why providers patch hosts and why sensitive workloads may use dedicated hosts.

Speculative execution flaws showed that even hardware-enforced separation can leak information through subtle timing effects. Providers responded with microcode updates, kernel patches and options for dedicated hosts. Customers handling highly sensitive data can choose such hosts to avoid sharing hardware with unknown tenants, at higher cost.

### 8.3 Storage hierarchy

Caches, memory, local disks and network storage differ in speed by orders of magnitude. meterhub keeps recent readings in memory and older ones on network storage.

Memory is thousands of times faster than network storage, so keeping the most recent readings there lets dashboards respond quickly. Older readings are needed less often and can tolerate slower access. Choosing what lives where balances speed against cost, and the boundary moves as usage patterns change. Elena checks how often older readings are actually requested before moving the boundary.

### 8.4 Resource limits

Kubernetes requests and limits map to kernel controls (cgroups) on CPU time and memory. Without limits, one pod can starve others on the node, an availability risk.

A request tells the scheduler how much a pod needs; a limit caps what it may use. A pod with a memory leak and no limit could consume the node's memory, causing other pods to be killed. Setting limits keeps one faulty workload from taking down its neighbours, which is a security concern as well as a reliability one.

### 8.5 Architecture and responsibility

The provider secures physical hardware and hypervisors; the customer chooses instance types, node images and pod settings.

The split is called the shared responsibility model. Solent cannot patch the provider's hypervisors, but it chooses node images and must keep them updated. Pod settings, such as running as non-root, are entirely Solent's responsibility. Knowing where the line falls prevents gaps where each side assumes the other is handling something. Elena lists each layer of meterhub with its owner in a single table, which Rosa's team reviews and keeps with the platform documentation.

### 8.6 Measuring

Node metrics show CPU, memory and I/O pressure, which help size limits correctly.

Without measurements, limits are guesses: too low and pods are throttled or killed, too high and nodes are underused. Watching metrics over a week of normal use, including evening peaks, shows how much each pod actually needs. Elena sets limits at the observed peak plus a margin, and reviews them as load grows. Throttling events are watched too, since they show a limit set too low even when averages look fine.

### Node images

Nodes run a minimal operating system image maintained by the provider. Elena checks that automatic node upgrades are enabled, since kernel fixes for isolation flaws arrive through those images.

### Dedicated hosts

For the most sensitive workloads, providers offer dedicated hosts that are not shared with other customers. Solent decides meterhub does not need them, but records the reasoning.

### Worked example

Elena finds that the 6 pods without limits from chapter 4 include a report generator that occasionally uses 12 GB of memory, evicting meterhub ingest pods on the same node. Setting a limit and moving reports to a separate node pool fixes the evictions.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Limits set too low cause their own failures; base them on measured use.

### Exercises

- **EX022 — VM vs container.** How do VM and container isolation differ? *Rubric:* 3 = hypervisor vs shared kernel features; 2 = partial; 1 = none; 0 = none.
- **EX023 — Limits mechanism.** What enforces pod limits? *Rubric:* 3 = cgroups; 2 = partial; 1 = none; 0 = none.
- **EX024 — Eviction fix.** How were evictions fixed? *Rubric:* 3 = limit and separate node pool; 2 = partial; 1 = none; 0 = none.

### Synthesis

Architecture explains isolation and resource behaviour.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure larger programs into modules; (2) parse YAML-like and JSON configuration; (3) handle errors robustly; (4) write tests and review code.

### 9.1 Modules

Elena organises her configuration checker into modules: loading, checks, reporting. Each check is a function with one responsibility, so new checks can be added without changing others.

Separating loading from checks means a new export format needs only a new loader. Separating reporting means output can change from text to CSV without touching the checks. One function per check keeps each easy to test and read, and lets the team turn individual checks on or off for different clusters. Rosa adds one check herself.

### 9.2 Parsing

Kubernetes manifests are YAML; Python's standard library has no YAML parser, so labs use JSON exports, which Kubernetes tools can produce. Parsing errors are reported with the file and line.

Using JSON keeps the labs within the standard library while still working with real Kubernetes data. Reporting the file and line of a parse error lets the user find and fix the problem quickly. Elena's loader also checks that each document has the expected top-level fields before passing it to the checks.

### 9.3 Error handling

Missing fields default to the least safe interpretation for reporting: a missing runAsNonRoot is reported as "not set", because Kubernetes would not enforce it.

Treating a missing setting as safe would hide real exposure, since Kubernetes applies its own default, which may be less strict. Reporting it as not set makes the gap visible. The report distinguishes 'explicitly false' from 'not set', because the fixes and the reasons differ slightly. Elena documents each default the checker assumes, citing the Kubernetes behaviour behind it, so reviewers can confirm the assumptions are correct.

### 9.4 Testing

Each check has tests with compliant and non-compliant synthetic manifests. Tests run on every change in the course repository.

Each test pairs a synthetic manifest with the expected result, such as one issue for a pod that runs as root. Testing both compliant and non-compliant cases checks that the function flags problems and does not raise false alarms. Running tests on every change catches mistakes before they reach users. A new check cannot be merged without both kinds of test, and the test data live beside the check in the repository.

### 9.5 Code review

A reviewer checks correctness, clarity and that the program only reads data.

Correctness asks whether the checks match the policy; clarity asks whether others can maintain them. Confirming the program only reads data protects production systems from accidental changes. The reviewer also checks that test cases cover the edge cases Elena described in her design note. Rosa reviews Elena's first three checks herself. Her comments become a short checklist that Elena applies to every later check before asking for review, so reviews get quicker as the project goes on.

### 9.6 Performance

The checker processes 3,000 manifests in under two seconds, fast enough to run in a build pipeline.

Fast checks can run on every change without slowing developers. If the checker took minutes, teams would be tempted to skip it. Elena measures run time on the full set of exported manifests and records it, so later changes that slow the checker are noticed. The time is printed at the end of each run. If the manifest count doubles as meterhub grows, the checker should still finish quickly, since each manifest is checked independently and the work grows only in proportion to the count.

### Packaging the checker

The checker is packaged with a short README, example inputs and expected outputs, so others can run it and confirm it works. Version numbers are recorded in each report, which matters when results change after an update. Elena also writes a list of checks with the reason and source for each one, linking to the Kubernetes Pod Security Standards and NIST SP 800-190. That list becomes the basis of later control design, so each check traces back to published guidance.

### Logging decisions

Each check logs why it flagged a resource, making false alarms easier to trace.

### Worked example

A review finds Elena's checker treats a container-level setting as overriding the pod-level one in the wrong direction. A new test reproduces it, the fix is one line, and the test stays to prevent regression.

> **Synthetic case.** Code and counts are synthetic.

### Errors and limits

Defaults matter: know how the platform interprets missing settings.

### Exercises

- **EX025 — Missing fields.** How are missing security fields reported? *Rubric:* 3 = as not set, least safe; 2 = partial; 1 = none; 0 = none.
- **EX026 — JSON choice.** Why use JSON exports in labs? *Rubric:* 3 = stdlib lacks YAML parser; 2 = partial; 1 = none; 0 = none.
- **EX027 — Review catch.** What did review catch? *Rubric:* 3 = override direction wrong; 2 = partial; 1 = none; 0 = none.

### Synthesis

Structured, tested programs scale to real configuration sets.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering ethics to cloud work; (2) consider safety and privacy of households; (3) act within authorisation; (4) raise concerns responsibly.

### 10.1 Duties

Engineers owe duties to the public, clients and the profession. For meterhub, the public includes 80,000 households whose readings reveal when they are home.

The public's interest is not abstract here: a careless design could expose patterns of daily life for tens of thousands of families. Clients expect competent work within agreed scope. The profession expects honesty and continued learning. When these duties conflict, the public interest comes first. Elena writes these duties into her project plan so they guide daily choices, not only difficult moments.

### 10.2 Privacy

Meter readings at fine intervals can reveal occupancy and habits. Elena's project uses synthetic readings; real data stays in production under Solent's controls.

Synthetic readings let Elena build and test without touching personal data, which removes a whole class of risk from the project. Real data stays where Solent's access controls, logging and retention rules apply. If a test truly needs real data, it goes through Solent's approval process first. Elena's synthetic generator mimics evening peaks and holiday dips without copying any real household's pattern.

### 10.3 Authorisation

Elena's access is limited to read-only exports and a test cluster. She does not test production systems without written approval from Rosa.

Read-only exports and a test cluster give Elena enough to do her work without risking production. Written approval for any production test makes the decision explicit and traceable. If something goes wrong during an approved test, the record shows it was sanctioned and by whom. She keeps copies of each approval with the test records. Approvals state the date, scope and stop conditions, and expire after the test window ends.

### 10.4 Safety

Changes to network policies could stop ingestion, which affects billing and grid planning. Safety means staged rollout, monitoring and rollback plans.

Ingestion stopping means readings are lost or delayed, which affects bills and the grid operator's planning. Staged rollout limits the impact to a few services first; monitoring shows problems quickly; rollback restores service if needed. Elena writes these steps into every change plan. She also checks each change against the evening peak and avoids rolling out during it, when readings are most valuable.

### 10.5 Raising concerns

If Elena found that readings were exposed, she would report to Rosa and Solent's data protection lead immediately rather than investigate alone.

Investigating alone could destroy evidence, alert an attacker or breach rules on handling personal data. Reporting immediately lets people with authority and expertise take over. The data protection lead also judges whether a regulator must be notified, which has its own deadlines. Solent's incident procedure lists who to call and how quickly, and Elena keeps a copy handy.

### 10.6 Honesty

Reports state uncertainty and do not overstate the effect of controls.

Saying a control 'prevents' an attack when it only makes one harder misleads decision-makers. Elena uses measured results where possible and states what was not tested. Honest reports build trust and help Solent decide where further work is needed. When results are mixed, the report gives both sides and the evidence for each. Elena also lists known limitations at the start of each results chapter, not just at the end, so readers meet them before forming conclusions. Rosa checks reports for overclaiming before they reach managers.

### Professional codes

Elena reads her engineering institution's code of conduct and notes three duties relevant to her project: protect public safety and privacy, work only within competence, and report concerns. Her project plan has a short ethics section that names these duties and how she meets them: synthetic data, read-only access, staged changes and clear escalation contacts. Dr Wagner signs the section at the start of the project.

### Ethics in design

Ethics also shapes design choices: Elena prefers controls that fail safely and are visible to teams, rather than hidden controls that could surprise people and cause outages.

### Worked example

During the project, Elena notices a test dataset in the shared cluster that looks like real readings with addresses. She reports it; Solent confirms it was a copy made against policy, deletes it and reminds teams of the synthetic-data rule.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Good intentions do not replace authorisation.

### Exercises

- **EX028 — Public duty.** Who is the public for meterhub? *Rubric:* 3 = 80,000 households; 2 = partial; 1 = none; 0 = none.
- **EX029 — Privacy risk.** What can fine-grained readings reveal? *Rubric:* 3 = occupancy and habits; 2 = partial; 1 = none; 0 = none.
- **EX030 — Real data found.** What did Elena do on finding real-looking data? *Rubric:* 3 = reported to Rosa; 2 = partial; 1 = none; 0 = none.

### Synthesis

Ethics guides how engineers handle data and changes.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) explain cloud virtual networks, subnets and security groups; (2) describe Kubernetes pod and service networking; (3) reason about traffic paths; (4) identify where traffic can be controlled.

### 11.1 Virtual networks

A cloud virtual network is a private address space divided into subnets. Route tables decide where traffic goes, and security groups or firewall rules decide which connections are allowed. Solent's meterhub cluster runs in private subnets; only a load balancer sits in a public subnet.

Keeping nodes in private subnets means they have no public addresses at all, so nothing on the internet can open a connection to them directly. The load balancer becomes the single front door, where TLS, request limits and logging are applied. Elena draws the subnets and route tables for meterhub and confirms that no route sends internet traffic straight to a node, which would undo the separation without anyone noticing.

### 11.2 Kubernetes networking

Every pod gets its own IP address and, by default, can reach every other pod in the cluster. Services give stable names and addresses in front of groups of pods. This flat model is convenient, but it is why meterhub's missing network policies let any pod reach the database.

In practice, the metrics pod, the report API and a forgotten debugging pod could all open connections to the database, though only the ingest and API services ever needed to. Nothing in the default model distinguishes them. Network policies add that distinction by selecting pods with labels and listing which other pods may connect, turning a flat network into one where each path must be stated.

### 11.3 Control points

Traffic can be controlled at the cloud level (security groups between nodes and external services), at the cluster level (network policies between pods, enforced by the network plugin) and at the application level (authentication between services). Each catches different mistakes.

Security groups stop a node from reaching services it never should, such as another team's database. Network policies stop one pod from reaching another inside the same cluster. Service authentication stops a request that arrives on an allowed path but from the wrong caller. A mistake at one layer, such as an over-broad policy, is then caught by another, which is why Solent uses all three.

### 11.4 Encryption in transit

External traffic uses TLS at the load balancer. Internal service-to-service traffic is also encrypted in Solent's design so that a compromised node cannot read readings in transit.

Without internal encryption, anyone able to capture traffic on a node, whether an attacker who has compromised it or a misconfigured monitoring tool, could read meter readings as they pass. Encrypting service-to-service traffic, often with mutual TLS, also lets each side check the other's identity. The cost is certificate management, which Solent automates so that certificates rotate without manual work.

### 11.5 DNS

Cluster DNS resolves service names; egress to external DNS is limited so pods cannot reach arbitrary internet hosts.

DNS is also a channel for data: a compromised pod could encode readings in lookups for names under a domain an attacker controls. Restricting pods to the cluster resolver, and letting that resolver forward only to approved upstream servers, closes that path. Elena checks that the resolver logs queries, so unusual lookups can be investigated. Blocked lookups are logged as well, since repeated attempts to reach outside resolvers may show a misbehaving pod.

### 11.6 Egress

By default pods can usually reach the internet. Limiting egress reduces what a compromised or misconfigured workload can send out, which would also have limited the use of a leaked key from inside the cluster.

A pod that pulls images or calls one external weather service needs only those destinations. Allowing everything means a compromised pod could upload readings anywhere or download further tools. Listing allowed destinations, often through an egress gateway or proxy, keeps outbound traffic visible and limited. A leaked key used from inside the cluster would have had nowhere to send its results.

### 11.7 Mapping traffic

Before writing rules, engineers need to know which traffic is legitimate. Elena uses flow logs from the test cluster to list observed connections.

Writing rules from memory or diagrams misses flows that were never documented, such as a nightly export job. Flow logs show what actually happens over days of normal use, including peaks. Elena groups the observed connections by source and destination service, marks each as expected or unexplained, and asks service owners about the unexplained ones before any rule is written.

### Worked example

Flow logs for meterhub's test cluster show 14 distinct pod-to-pod flows in a week, but only 4 are documented in the architecture diagram. Ten undocumented flows are investigated: eight are legitimate (health checks and metrics) and two come from a debugging tool left running, which is removed.

> **Synthetic case.** Networks and flows are synthetic.

### Errors and limits

A week of flow logs can miss monthly jobs; check schedules before blocking.

### Exercises

- **EX031 — Default pod reachability.** What is Kubernetes' default pod reachability? *Rubric:* 3 = every pod can reach every pod; 2 = partial; 1 = none; 0 = none.
- **EX032 — Three control points.** Name the three levels of traffic control. *Rubric:* 3 = cloud, cluster, application; 2 = two; 1 = one; 0 = none.
- **EX033 — Flow findings.** What did the flow logs show? *Rubric:* 3 = 14 flows, 4 documented; 2 from debug tool; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know the traffic paths before controlling them.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) explain how containers use Linux kernel features; (2) describe capabilities, namespaces and control groups; (3) apply least privilege to containers; (4) check capability sets.

### 12.1 Namespaces

Containers are processes isolated by Linux namespaces: each sees its own process list, network interfaces, mount points and hostname. Isolation comes from the shared kernel, so kernel settings matter.

A container's process list shows only its own processes because of the PID namespace; its network namespace gives it a separate interface and routing table. These are views provided by the kernel, not separate machines. A flaw in the kernel, or a setting that grants access to the host's namespaces, breaks the illusion, which is why host-level settings such as hostNetwork are checked closely.

### 12.2 Capabilities

Linux splits root privileges into capabilities such as NET_BIND_SERVICE (bind low ports), CHOWN (change file owners) and SYS_ADMIN (a very broad set of administrative powers). A container should drop all and add only what it needs; NIST SP 800-190 recommends limiting container privileges.

Running as root inside a container used to mean holding every capability, including powerful ones like loading kernel modules. Splitting them lets a web server bind to port 443 without also being able to reconfigure the network. Dropping all and adding back only what is needed makes each container's power explicit and reviewable.

### Lab — Lab — container capabilities

```python
"""Compare synthetic container capability sets with a drop-all-add-needed baseline (stdlib only)."""
needed = {"meter-ingest": {"NET_BIND_SERVICE"}, "report-api": set(), "node-agent": {"SYS_PTRACE"}}
actual = {"meter-ingest": {"NET_BIND_SERVICE", "CHOWN", "SETUID"}, "report-api": set(),
          "node-agent": {"SYS_ADMIN", "SYS_PTRACE", "NET_ADMIN"}}
for c in actual:
    extra = sorted(actual[c] - needed[c])
    print(f"{c:13} extra capabilities: {', '.join(extra) or 'none'}")
```

Run with `python3 lab_caps.py`. Verified output:

```text
meter-ingest  extra capabilities: CHOWN, SETUID
report-api    extra capabilities: none
node-agent    extra capabilities: NET_ADMIN, SYS_ADMIN
```

### 12.3 Lab result

meter-ingest has two extra capabilities, CHOWN and SETUID, beyond the NET_BIND_SERVICE it needs. report-api has none extra. node-agent has NET_ADMIN and SYS_ADMIN beyond the SYS_PTRACE it needs. SYS_ADMIN is the most serious because it grants broad control close to full root.

CHOWN and SETUID on meter-ingest are probably leftovers from a base image or an old setup step; removing them should be tested but is unlikely to break anything. node-agent's case needs more care, since it monitors the node and genuinely needs some power, but SYS_ADMIN is far more than tracing requires. Elena raises it as the top finding with a suggested reduced set.

### 12.4 Running as non-root

Containers should run as a non-root user with a read-only root filesystem where possible. The Restricted profile of the Pod Security Standards requires runAsNonRoot and disallows privilege escalation.

A process running as root inside a container is one kernel flaw away from root on the host. Running as an ordinary user removes that step. A read-only root filesystem stops an attacker from writing tools or changing binaries inside the container; writable space is given only where needed, through specific volumes.

### 12.5 Seccomp

Seccomp profiles limit which system calls a container may make. The runtime default profile blocks many rarely needed calls and is required by the Restricted profile.

Many system calls exist for rare administrative tasks that ordinary applications never use. Each one is a possible path into the kernel if it contains a bug. Blocking unused calls shrinks that attack surface. The runtime default suits most applications; where a workload needs an unusual call, a custom profile adds it explicitly. Profiles are kept in version control.

### 12.6 Checking in practice

Capability sets come from pod specifications; Elena's checker compares them with a documented "needed" list per workload.

The 'needed' list is written by each workload's owner with a short reason for every capability. Elena's checker then reports any capability in the spec that is not on the list, and any listed capability that the spec no longer uses. Both kinds of difference prompt a review, keeping the list and the deployment in step. The list is reviewed when a workload's owner changes, so knowledge of why each capability exists is not lost.

### Worked example

The node-agent's owners explain that SYS_ADMIN was copied from an old example. Testing on the test cluster shows the agent works with only SYS_PTRACE. NET_ADMIN is removed too, and meter-ingest drops CHOWN and SETUID after its image is rebuilt to set file ownership at build time.

> **Synthetic case.** Workloads and capabilities are synthetic.

### Errors and limits

Removing capabilities can break software in rare code paths; test thoroughly.

### Exercises

- **EX034 — Lab extras.** What extra capabilities did node-agent have? *Rubric:* 3 = NET_ADMIN, SYS_ADMIN; 2 = partial; 1 = none; 0 = none.
- **EX035 — Most serious.** Why is SYS_ADMIN most serious? *Rubric:* 3 = broad, close to full root; 2 = partial; 1 = none; 0 = none.
- **EX036 — meter-ingest fix.** How did meter-ingest drop CHOWN and SETUID? *Rubric:* 3 = set ownership at build time; 2 = partial; 1 = none; 0 = none.

### Synthesis

Containers should drop capabilities and run as non-root.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) design storage for meter readings with security in mind; (2) apply encryption, access control and retention; (3) separate personal data; (4) plan backups and restores.

### 13.1 Data model

meterhub stores readings (meter ID, timestamp, value) in a time-series database and customer details (name, address) in a separate customer system. Linking requires a lookup the API controls, reducing what a database leak reveals.

If the readings database leaked alone, an attacker would see meter IDs and values but not names or addresses. Linking them requires the customer system, which holds different credentials and is accessed only through the API's controlled lookup. Separation does not make readings harmless, but it raises the effort needed to identify households.

### 13.2 Encryption at rest

Cloud storage and databases encrypt data at rest by default with provider-managed keys. Solent uses customer-managed keys for readings so it can control and audit key use, as CSA CCM v4's cryptography domain describes.

Provider-managed keys protect against stolen disks but are used automatically, so their use reveals little. Customer-managed keys let Solent set who can use them and see every use in audit logs. Disabling the key makes the data unreadable, which is a strong control in an emergency but also a risk if done by mistake.

### 13.3 Access control

Only the ingest service writes readings; the API reads them; analysts get aggregated views without meter IDs. Database credentials are short-lived and issued per service.

Each service gets the narrowest access that its job requires: ingest can write but not read customer details; the API can read but not write. Aggregated views for analysts remove meter IDs, so analysis does not expose individuals. Short-lived credentials limit how long a stolen credential stays useful. Each grant is recorded with its owner and reviewed twice a year.

### 13.4 Retention

Fine-grained readings are kept 13 months for billing disputes, then aggregated to daily values. Retention is enforced by lifecycle rules, not manual deletion.

Thirteen months covers a full billing year plus time for disputes. After that, daily aggregates still support long-term planning while revealing much less about daily household routines. Lifecycle rules apply automatically and consistently, whereas manual deletion is easily forgotten or done unevenly. Elena checks that aggregation runs before deletion, so no month is lost if a job fails, and that failures raise an alert.

### 13.5 Backups

Daily snapshots are copied to a separate account so that a compromised production account cannot delete them. Restores are tested quarterly.

An attacker who gains control of the production account might try to delete backups before encrypting or destroying data. Copies in a separate account, with different credentials, survive that. Quarterly restore tests prove the copies are usable and show how long recovery takes, which matters for planning. The backup account allows writes from production but no deletes, and its own administrators use separate credentials and MFA.

### 13.6 Data in logs

Logs must not contain readings linked to addresses; Elena adds a check for meter IDs in application logs.

Developers often log request details while debugging and forget to remove them. A log line containing a meter ID and an address would recreate the link the data model was designed to prevent. Elena's check searches log samples for patterns matching meter IDs and raises an issue for the owning team. Teams fix findings at the source by changing log statements, not by filtering logs afterwards, which could fail silently.

### Restore tests

A quarterly restore test brings back one day of synthetic readings from the separate backup account into a test database and compares counts and checksums with the source. The first test reveals that restores need a permission nobody on call held; the runbook and access are fixed.

### Worked example

The log check finds that the API logs full query parameters, including meter IDs, at debug level, and debug logging was left on in one environment. Debug logging is turned off and the logger is changed to redact meter IDs at every level.

> **Synthetic case.** Data and findings are synthetic.

### Errors and limits

Encryption at rest does not protect against an authorised service misusing its access.

### Exercises

- **EX037 — Separation.** Why separate readings from customer details? *Rubric:* 3 = leak reveals less; 2 = partial; 1 = none; 0 = none.
- **EX038 — Backup protection.** How are backups protected from a compromised account? *Rubric:* 3 = copied to separate account; 2 = partial; 1 = none; 0 = none.
- **EX039 — Log finding.** What did the log check find? *Rubric:* 3 = meter IDs in debug logs; 2 = partial; 1 = none; 0 = none.

### Synthesis

Design data storage so each part reveals and allows as little as possible.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) apply software engineering practices to infrastructure and platform code; (2) use version control, review and pipelines; (3) manage configuration as code; (4) reduce change risk.

### 14.1 Infrastructure as code

Solent defines its cloud networks, clusters and storage in code templates, and Kubernetes workloads in manifests, all in version control. Every change is a reviewed pull request, giving history and accountability.

Defining infrastructure in code means the same template produces the same network or cluster every time, unlike manual console changes that drift. Reviews catch mistakes before they reach production. History shows who changed what and when, which helps investigations and audits. Console changes are blocked in production except through an emergency procedure that is logged and reviewed.

### 14.2 Security smells

Rahman et al. (2019) identified recurring security smells in infrastructure-as-code: hard-coded secrets, admin by default, empty passwords, unrestricted IP addresses, use of HTTP and weak cryptography. Elena adds checks for several of these to the pipeline.

A smell is a pattern that often indicates a problem, not proof of one. A hard-coded secret in a template is visible to anyone with repository access; an unrestricted address range opens a service to the world. Automated checks find these patterns quickly so reviewers can focus on design.

### 14.3 Pipelines

A pipeline validates templates, runs policy checks, builds and scans images, and deploys to test before production. Failures stop the change.

Each stage catches a different kind of problem: template validation finds syntax errors, policy checks find insecure settings, image scans find known vulnerabilities and embedded secrets. Deploying to test first shows whether the change works. Stopping on failure keeps unsafe changes out of production. Each failure message names the stage and the rule that failed, so developers can fix problems without asking the platform team for help.

### 14.4 Small changes

Small, frequent changes are easier to review and roll back than large ones.

A change touching one service and two settings can be reviewed in minutes, and if it breaks something the cause is obvious. A change touching twenty services makes review superficial and diagnosis slow. Small changes also make rollback safer, since undoing one does not undo unrelated work. Solent's guideline asks for changes that a reviewer can understand in fifteen minutes; larger work is split into a series of steps, each deployable on its own.

### 14.5 Environments

Test, staging and production are separate accounts with separate credentials; promotion uses the same artifacts.

Separate accounts mean a mistake or compromise in test cannot reach production data. Promoting the same artifacts, rather than rebuilding them, ensures that what was tested is what runs in production. Credentials for each environment are held by different people or systems. Configuration that differs between environments, such as hostnames and sizes, lives in separate parameter files reviewed like code, so the differences are visible and deliberate rather than hidden in manual steps.

### 14.6 Peer review

Reviewers check intent, security settings and blast radius: what else could this change affect?

Intent asks whether the change does what its description says. Security settings are checked against policy. Blast radius asks what else could break, such as a network rule that also affects a monitoring service. Reviewers who ask these questions consistently catch problems that tests alone miss. Solent requires one reviewer for routine changes and two for changes to network policies, access rules or the pipeline itself, since mistakes there have the widest effect.

### 14.7 Documentation

README files in each repository explain how to deploy and roll back.

A deployment that only one person knows how to run or undo is a risk when that person is away. README files give the steps, prerequisites and how to check success. Rollback instructions are tested, so they work when needed under pressure. Each README also lists the owner and an escalation contact. Elena tests two READMEs by following them on the test cluster without help, and fixes the steps that were missing or out of date.

### Console changes

Because console changes bypass the pipeline, Solent limits console write access in production to a break-glass role used only in emergencies, with alerts on use. Normal changes go through code.

### Rollback design

Each deployment keeps the previous version ready, so rollback is one reviewed command; Elena tests rollback in staging monthly.

### Merge rules

Main branches require one approval and passing checks before merge.

### Worked example

The new IaC checks flag a storage template that allows access from any IP address, used by three projects. The template is fixed once and the three projects pick up the fix on their next deployment, an example of why fixing shared templates is efficient.

> **Synthetic case.** Templates and findings are synthetic.

### Errors and limits

Pipeline checks only see what passes through the pipeline; console changes bypass them.

### Exercises

- **EX040 — Smells.** Name three IaC security smells. *Rubric:* 3 = hard-coded secrets, admin default, unrestricted IP, HTTP, weak crypto; 2 = two; 1 = one; 0 = none.
- **EX041 — Blast radius.** What does blast radius mean in review? *Rubric:* 3 = what else a change affects; 2 = partial; 1 = none; 0 = none.
- **EX042 — Template fix.** Why was the template fix efficient? *Rubric:* 3 = three projects fixed at once; 2 = partial; 1 = none; 0 = none.

### Synthesis

Treat infrastructure like software: reviewed, versioned and tested.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to meterhub; (2) identify assets and threats; (3) use defence in depth; (4) understand shared responsibility.

### 15.1 CIA for meterhub

Confidentiality: readings and customer details stay private. Integrity: readings are not altered, since bills and grid planning depend on them. Availability: ingest keeps up so data are not lost.

Each property has concrete consequences. A confidentiality breach exposes households' routines; an integrity failure could produce wrong bills or mislead grid planning; an availability failure loses readings that cannot be recollected. Elena uses these to rank risks during design. She also notes that integrity failures may go unnoticed longer than outages, since wrong values look normal.

### 15.2 Assets

Readings, customer data, cloud credentials, container images, cluster configuration and the deployment pipeline. The leaked key showed that credentials and images are assets as important as data.

Listing assets broadly avoids focusing only on the database. A cloud credential can unlock many resources at once; a container image can carry secrets or vulnerabilities into production; the pipeline can deploy anything. Protecting these is as important as protecting the data itself. Each asset has a named owner in Solent's register, together with its sensitivity and where it is stored.

### 15.3 Threats

Credential leaks, misconfigured access, vulnerable images, compromised dependencies, insider misuse and outages. Each threat maps to controls.

Mapping each threat to controls shows where defences are strong and where they are thin. Credential leaks map to secret scanning and short-lived keys; vulnerable images to scanning and patching; outages to redundancy and backups. Threats with no mapped control become priorities. Insider misuse is easy to overlook in a small co-operative where everyone knows each other, but access logs and separation of duties still apply. Outages are included because availability failures can lose readings permanently.

### 15.4 Defence in depth

The key leak could have been prevented (no secrets in images), detected (secret scanning before push), limited (key with narrow permissions, egress limits) and recovered from (fast revocation). Several layers each reduce risk.

Any one of these layers might have stopped the leak from causing harm. Together they make it much less likely that a single mistake leads to a breach. Elena uses the key leak as a worked example when explaining layered controls to Solent's managers. She shows how each layer applies to other threats too.

### 15.5 Shared responsibility

The AWS, Azure and Google Cloud shared responsibility documents agree that customers secure identities, data, configurations and workloads; providers secure the physical infrastructure and managed service internals. Managed Kubernetes moves the control plane to the provider but leaves workloads to the customer.

Misunderstanding the split is a common cause of cloud incidents: customers assume the provider secures their storage permissions, which it does not. Managed Kubernetes relieves Solent of patching the control plane but not of configuring pods, network policies and access. Elena lists Solent's responsibilities explicitly in the design note.

### 15.6 Zero trust

NIST SP 800-207 recommends authenticating and authorising every request; network location alone is not trusted. This principle drives meterhub's service authentication and network policies.

In meterhub, being inside the cluster no longer grants access by itself: each service proves its identity and is authorised for specific actions. Network policies limit who can even attempt a connection. If one pod is compromised, it cannot freely reach everything else simply because it shares a network. Every connection decision is logged, so denied attempts become evidence for investigation.

### Workload identity

Workload identity lets a pod obtain short-lived cloud credentials tied to its Kubernetes service account, instead of a long-lived key stored in a file or image. If such a credential leaked it would expire within an hour and could only be used with the narrow permissions of that service. This removes the class of problem behind the opening case.

### Worked example

Elena maps the key leak to the four layers and finds Solent had only the last one (revocation). The project plan adds the other three: build-time secret checks, pre-push scanning, and narrow, short-lived credentials from a workload identity service.

> **Synthetic case.** Assets and events are synthetic.

### Errors and limits

Defence in depth fails if every layer depends on the same assumption.

### Exercises

- **EX043 — Integrity importance.** Why does integrity matter for readings? *Rubric:* 3 = bills and grid planning; 2 = partial; 1 = none; 0 = none.
- **EX044 — Four layers.** Name the four layers for the key leak. *Rubric:* 3 = prevent, detect, limit, recover; 2 = three; 1 = one; 0 = none.
- **EX045 — Managed Kubernetes.** What does managed Kubernetes leave to the customer? *Rubric:* 3 = workloads; 2 = partial; 1 = none; 0 = none.

### Synthesis

Layered controls and clear responsibility protect cloud systems.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) treat meterhub as a system of interacting parts; (2) define requirements, interfaces and life cycle; (3) trace requirements to verification; (4) manage trade-offs across subsystems.

### 16.1 Systems view

meterhub is not just a cluster: it includes meters, the network operator, the ingest service, storage, billing, analysts, the cloud provider and the people who operate it. Security properties emerge from how these parts interact, not from any single control.

### 16.2 Life cycle

Systems engineering follows concept, requirements, design, implementation, verification, operation and retirement. Security must appear at each stage; retirement matters too, since old clusters and buckets left running were a source of exposure in many organisations.

### 16.3 Interfaces

Each interface is specified: what data crosses it, in what format, authenticated how and with what limits. The interface between ingest and storage, for example, carries readings over TLS with a workload identity and a maximum batch size.

### 16.4 Traceability

Every security requirement has an identifier, a source (standard, regulation or risk), a design element that meets it and a verification method. A traceability matrix shows gaps: requirements with no test, tests with no requirement.

### 16.5 Trade-offs

Stronger isolation (separate clusters per service) costs more and adds operational work; Solent chooses separate namespaces with strict policies and a separate cluster only for the payment-related service.

### 16.6 Configuration management

The system's configuration baseline is the set of reviewed templates and manifests in version control; changes go through change control.

### Worked example

Elena builds the first traceability matrix with 24 security requirements. Five have no verification method, including "backups cannot be deleted from production". She adds a test that attempts a deletion from a production test role in a controlled way and expects it to be refused, and records the result.

> **Synthetic case.** Requirements and tests are synthetic.

### Errors and limits

A matrix can look complete while tests are weak; review test quality too.

### Exercises

- **EX046 — Emergent security.** Why is security emergent in systems? *Rubric:* 3 = arises from interactions; 2 = partial; 1 = none; 0 = none.
- **EX047 — Retirement.** Why does retirement matter? *Rubric:* 3 = old resources left running expose data; 2 = partial; 1 = none; 0 = none.
- **EX048 — Matrix gaps.** What gaps did the first matrix show? *Rubric:* 3 = 5 requirements without verification; 2 = partial; 1 = none; 0 = none.

### Synthesis

Systems engineering traces security from requirements to tests across the life cycle.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) describe feedback loops in cloud systems; (2) analyse an autoscaling rule; (3) reason about stability, limits and oscillation; (4) relate reconciliation loops to security.

### 17.1 Feedback loops

A controller measures an output, compares it with a target and adjusts an input. Kubernetes is built from such loops: controllers continually reconcile the actual state toward the declared desired state, as Burns et al. (2016) describe.

### 17.2 Autoscaling rule

The horizontal pod autoscaler sets desired replicas = ceil(current replicas × current metric ÷ target metric), within minimum and maximum bounds.

### Lab — Lab — autoscaling loop

```python
"""Replica feedback rule desired = ceil(current * metric / target), with min/max bounds (stdlib only)."""
import math
target, lo, hi = 60, 2, 10   # target CPU %, min and max replicas
replicas = 2
for load in [50, 90, 150, 200, 120, 40]:   # synthetic CPU % per replica at current size
    desired = max(lo, min(hi, math.ceil(replicas * load / target)))
    print(f"util {load:3}% at {replicas:2} replicas -> desired {desired}")
    replicas = desired
```

Run with `python3 lab_autoscale.py`. Verified output:

```text
util  50% at  2 replicas -> desired 2
util  90% at  2 replicas -> desired 3
util 150% at  3 replicas -> desired 8
util 200% at  8 replicas -> desired 10
util 120% at 10 replicas -> desired 10
util  40% at 10 replicas -> desired 7
```

### 17.3 Lab result

With a 60% CPU target and bounds of 2 to 10: at 50% on 2 replicas it stays at 2; at 90% it scales to 3; at 150% on 3 to 8; at 200% on 8 it would want 27 but is capped at 10; at 120% on 10 it stays at the cap of 10; at 40% on 10 it scales down to 7. The cap protects cost and downstream systems but means sustained overload is possible.

### 17.4 Stability

Loops that react too fast oscillate; real autoscalers add stabilisation windows so scale-down waits. Measurement delay makes oscillation more likely.

### 17.5 Security and feedback

Reconciliation also restores security settings: if someone edits a live object by hand, a GitOps controller changes it back to the declared state. Security alerts and responses form a loop too; slow detection is like measurement delay.

### 17.6 Limits as safety

Maximum replicas also limit the cost of a flood of fake traffic, a simple availability safeguard.

### Tuning

Stabilisation windows are tuned using load-test data rather than guesses.

### Worked example

In a load test, ingest hits the 10-replica cap for 40 minutes and the queue grows. Elena recommends raising the cap to 14 after checking the database can handle the extra connections, and adding an alert when the cap is reached for more than 10 minutes.

> **Synthetic case.** Loads and replicas are synthetic.

### Errors and limits

A capped autoscaler hides overload unless the cap itself is monitored.

### Exercises

- **EX049 — Formula.** Write the autoscaling formula. *Rubric:* 3 = ceil(current × metric / target) within bounds; 2 = partial; 1 = none; 0 = none.
- **EX050 — Capped step.** What happened at 200% on 8 replicas? *Rubric:* 3 = wanted 27, capped at 10; 2 = partial; 1 = none; 0 = none.
- **EX051 — Reconciliation security.** How does reconciliation help security? *Rubric:* 3 = reverts manual edits to declared state; 2 = partial; 1 = none; 0 = none.

### Synthesis

Feedback loops scale systems and restore declared security state.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) design a layered security architecture for meterhub; (2) place trust boundaries; (3) choose isolation levels; (4) document architecture decisions.

### 18.1 Layers

Account level: separate accounts for production, test and backups; organisation policies that block public storage and restrict regions. Cluster level: private control plane endpoint, workload identity, Pod Security admission at Restricted, default-deny network policies. Workload level: signed images, non-root, minimal capabilities. Data level: customer-managed keys, separation of readings and customer details.

### 18.2 Trust boundaries

Internet to load balancer; load balancer to ingest; ingest to storage; cluster to cloud APIs; pipeline to cluster; production to backup account. Each boundary has authentication and a policy check.

### 18.3 Isolation choices

Namespaces with strict policies for most services; a separate cluster for the payment service; separate accounts for backups. NIST SP 800-190 discusses grouping containers by sensitivity on hosts.

### 18.4 Zero trust alignment

Every service call is authenticated with workload identity, following NIST SP 800-207, and authorised by policy.

### 18.5 Architecture decision records

Each choice is recorded with context, options and consequences, so future engineers know why the payment service is separate.

### 18.6 Guardrails versus gates

Guardrails (organisation policies) prevent classes of mistakes everywhere; gates (pipeline checks) stop specific changes. Both are used.

### Reviewing the architecture

Architecture reviews happen when a new service is added or a boundary changes. The reviewer walks each trust boundary and asks what authenticates the caller, what policy decides access and what is logged. Gaps become tickets. Elena keeps a one-page architecture diagram current in the repository, with links from each boundary to the decision record that explains it.

### Worked example

Reviewing the architecture with Rosa, Elena finds that the pipeline can deploy to both test and production with the same credential. A separate production deployer identity is created, usable only from the main branch after approval.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Architecture on paper must be verified against what is actually deployed.

### Exercises

- **EX052 — Account layer.** Name two account-level controls. *Rubric:* 3 = separate accounts; block public storage; restrict regions; 2 = one; 1 = none; 0 = none.
- **EX053 — Guardrails vs gates.** How do guardrails differ from gates? *Rubric:* 3 = prevent everywhere vs stop specific changes; 2 = partial; 1 = none; 0 = none.
- **EX054 — Pipeline finding.** What pipeline weakness was found? *Rubric:* 3 = same credential test and prod; 2 = partial; 1 = none; 0 = none.

### Synthesis

Layer controls and document why each boundary exists.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) manage cloud and workload identities; (2) apply cryptography for data and images; (3) detect secrets in images; (4) prefer short-lived credentials.

### 19.1 Identities

Humans sign in through the organisation's identity provider with multi-factor authentication; workloads use workload identity; pipelines use federated identity from the build system. Long-lived access keys are avoided.

### 19.2 Secrets in images

Image layers are archives; anything copied in remains even if deleted in a later layer. The opening case's key sat in layer 3 of the image. Shu, Gu and Enck (2017) found widespread vulnerabilities in public container images, a reminder that what is pushed publicly is visible to anyone.

### Lab — Lab — secrets in image layers

```python
"""Flag key-like strings in synthetic image layer files using pattern and entropy (stdlib only)."""
import math, re
from collections import Counter
layers = {
    "layer3/app/config.env": "LOG_LEVEL=info\nCLOUD_ACCESS_KEY=SYNTHKEY7Qx9Lp2Vw8Rt4Zm6\n",
    "layer4/app/settings.py": "TIMEOUT = 30\nEXAMPLE_TOKEN = 'xxxxxxxxxxxxxxxxxxxx'\n",
    "layer5/app/readme.txt": "Meter data platform.\n",
}
def H(s):
    c = Counter(s); return -sum(v/len(s) * math.log2(v/len(s)) for v in c.values())
for path, text in layers.items():
    for m in re.finditer(r"([A-Z_]*(?:KEY|TOKEN|SECRET)[A-Z_]*)\s*=\s*'?([A-Za-z0-9]{16,})", text):
        h = H(m.group(2))
        print(f"{path:24} {m.group(1):17} entropy {abs(h):.2f} {'LIKELY SECRET' if h > 3.5 else 'placeholder'}")
```

Run with `python3 lab_secrets.py`. Verified output:

```text
layer3/app/config.env    CLOUD_ACCESS_KEY  entropy 4.50 LIKELY SECRET
layer4/app/settings.py   EXAMPLE_TOKEN     entropy 0.00 placeholder
```

### 19.3 Lab result

The scan finds CLOUD_ACCESS_KEY in layer3/app/config.env with character entropy 4.50, above the 3.5 threshold: LIKELY SECRET. EXAMPLE_TOKEN in layer4/app/settings.py is twenty repeated characters with entropy 0.00: a placeholder. Entropy helps separate real-looking keys from obvious placeholders, but a reviewer confirms each finding.

### 19.4 Cryptography for integrity

Images are signed after build and verified at admission, so only images built by Solent's pipeline can run. Keys for signing are held in a managed key service.

### 19.5 Secrets management

Runtime secrets come from a secret manager or Kubernetes Secrets with encryption at rest, never from images; the Kubernetes good-practice guidance for Secrets recommends least-privilege access to them.

### 19.6 Rotation

Remaining long-lived secrets are rotated on a schedule and immediately after exposure.

### Human access

Engineers' production access is granted just in time for a ticket and expires automatically after a few hours.

### Worked example

Elena adds the layer scan to the pipeline before any push. In the first month it blocks two builds containing test credentials, both caught before leaving the build system.

> **Synthetic case.** Keys and images are synthetic.

### Errors and limits

Entropy checks miss low-entropy secrets such as simple passwords; combine with pattern rules.

### Exercises

- **EX055 — Deleted files.** Why does deleting a file in a later layer not help? *Rubric:* 3 = earlier layer still contains it; 2 = partial; 1 = none; 0 = none.
- **EX056 — Lab result.** What did the scan report? *Rubric:* 3 = CLOUD_ACCESS_KEY 4.50 likely secret; EXAMPLE_TOKEN 0.00 placeholder; 2 = one; 1 = none; 0 = none.
- **EX057 — Image signing.** What does image signing achieve? *Rubric:* 3 = only pipeline-built images run; 2 = partial; 1 = none; 0 = none.

### Synthesis

Short-lived identities and secret-free images remove whole classes of leaks.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Cloud and container security: engineering context

### Learning outcomes

You will (1) frame cloud and container security as an engineering discipline; (2) identify stakeholders and constraints; (3) relate standards to Solent's context; (4) define project goals.

### 20.1 The discipline

Cloud and container security engineering designs, builds and verifies controls for systems built on shared infrastructure, declarative configuration and fast change. Mell and Grance (2011) define the cloud's essential characteristics; each creates security work, such as self-service creating many configuration changes.

### 20.2 Stakeholders

Solent's platform team, service developers, the data protection officer, the energy regulator, customers and the cloud provider. Each has constraints: uptime for billing, privacy law, audit requirements.

### 20.3 Standards

NIST SP 800-190 for containers; SP 800-210 for cloud access control; SP 800-207 for zero trust; CSA CCM v4 for a control catalogue mapped to many frameworks; CIS Benchmarks for Kubernetes and cloud account settings; Kubernetes Pod Security Standards for workloads.

### 20.4 Constraints

The platform team has four engineers; changes must not disrupt ingestion; budgets limit new tools; the regulator expects evidence.

### 20.5 Project goals

No long-lived credentials in workloads; default-deny networking in all production namespaces; Restricted pod security everywhere except documented exceptions; signed images only; measurable detection within objectives.

### 20.6 Success measures

Each goal has a measure, such as percentage of namespaces with default-deny, tracked monthly.

### Mapping to CCM

Elena maps the five goals to CSA CCM v4 domains, such as identity and access management, infrastructure and virtualization security, and cryptography, encryption and key management. The mapping helps the regulator see that Solent's plan covers recognised control areas, and shows a gap in logging and monitoring, which Elena adds as a sixth goal: alert on high-risk configuration changes within fifteen minutes.

### Worked example

Elena presents the goals to Solent's leadership with a one-year plan. The finance director asks for the cost; Elena estimates mainly engineering time, about 30% of the platform team for two quarters, and no new paid tools.

> **Synthetic case.** Goals and estimates are synthetic.

### Errors and limits

Goals without measures cannot be verified.

### Exercises

- **EX058 — Characteristic link.** Give an example of a cloud characteristic creating security work. *Rubric:* 3 = self-service causes many changes; 2 = partial; 1 = none; 0 = none.
- **EX059 — Five goals.** List the five project goals. *Rubric:* 3 = no long-lived creds, default-deny, restricted, signed images, detection; 2 = three; 1 = one; 0 = none.
- **EX060 — Cost.** What was the cost estimate? *Rubric:* 3 = ~30% team for two quarters; 2 = partial; 1 = none; 0 = none.

### Synthesis

Engineering goals need context, standards and measures.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Cloud and container security: requirements

### Learning outcomes

You will (1) write testable security requirements for meterhub; (2) derive them from risks, standards and regulation; (3) prioritise them; (4) link each to verification.

### 21.1 Good requirements

A requirement says what the system must do in a way that can be tested: "Pods in production namespaces must not run as root" is testable; "the cluster must be secure" is not. Each requirement names its scope, condition and expected behaviour.

### 21.2 Sources

Risks from the key-leak review, the Kubernetes Pod Security Standards, CIS Benchmark recommendations for managed Kubernetes, CSA CCM v4 controls and the energy regulator's data rules. Each requirement cites its source so its purpose is clear.

### 21.3 Examples

R1: workloads obtain cloud credentials only through workload identity with lifetimes under one hour. R2: every production namespace has a default-deny ingress and egress network policy. R3: production namespaces enforce the Restricted Pod Security profile. R4: only images signed by the pipeline are admitted. R5: storage holding readings cannot be made public. R6: high-risk configuration changes raise an alert within 15 minutes.

### 21.4 Prioritising

Requirements are ranked by risk reduced and effort. R1 and R5 directly address the opening case; R2 addresses the missing network policies.

### 21.5 Exceptions

Some workloads, such as the node agent, need privileges. Requirements allow documented, time-limited exceptions approved by the platform lead.

### 21.6 Verification link

Each requirement has a verification: an admission test, a configuration query, or an alert test with synthetic events.

### 21.7 Change control

Requirements change only through review, with the reason recorded.

### Ownership

Each requirement has an owning team responsible for meeting and evidencing it.

### Worked example

Developers object that R3 will break two services that write to their root filesystem. Elena and the developers agree a two-month exception while the services are changed to write to a mounted volume; the exception expires automatically.

> **Synthetic case.** Requirements and services are synthetic.

### Errors and limits

Requirements that nobody can meet get ignored; plan exceptions and timelines.

### Exercises

- **EX061 — Testable.** Make "the cluster must be secure" testable. *Rubric:* 3 = specific condition e.g. pods not root; 2 = partial; 1 = none; 0 = none.
- **EX062 — R1.** State R1. *Rubric:* 3 = workload identity, under one hour; 2 = partial; 1 = none; 0 = none.
- **EX063 — Exception handling.** How was the R3 objection handled? *Rubric:* 3 = two-month expiring exception; 2 = partial; 1 = none; 0 = none.

### Synthesis

Testable, sourced requirements anchor the engineering work.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Cloud and container security: system and data models

### Learning outcomes

You will (1) model meterhub's components, identities and data flows; (2) classify data; (3) mark trust boundaries; (4) use the model to find missing controls.

### 22.1 Component model

Components: load balancer, ingest service, message queue, time-series database, API, billing export job, analytics workspace, metrics stack, pipeline, image registry, secret manager, backup account.

### 22.2 Identity model

Each component has an identity: Kubernetes service accounts mapped to cloud roles, pipeline federated identity, human roles. The model lists what each identity can do, which reveals over-broad roles.

### 22.3 Data model

Data classes: readings (personal, high), customer details (personal, high), aggregated statistics (internal), logs (may contain personal data), images (internal, may contain secrets). Each class has storage, retention and access rules.

### 22.4 Data flows

Meters to load balancer to ingest to queue to database; database to API to customer portal; database to billing export to billing system; database to analytics as aggregates.

### 22.5 Trust boundaries

Marked where data crosses between identities, networks or accounts. Shostack-style questions are asked at each: what can go wrong here?

### 22.6 Using the model

For each flow, Elena checks: is it authenticated, authorised, encrypted, logged? Missing marks become work items.

### Generating the model

Elena writes a script that builds the identity part of the model from exported role bindings and cloud role policies, so it can be regenerated monthly instead of drawn by hand. Differences from the previous month are highlighted for review. The first regeneration finds two new role bindings added during an incident and never removed.

### Worked example

The model shows the billing export job reads the full readings table with an identity that can also write to it. Reducing it to read-only, and to a view with only billing-period totals, removes write access and most personal detail from that path.

> **Synthetic case.** Components and flows are synthetic.

### Errors and limits

Models drift from reality; regenerate parts from live configuration where possible.

### Exercises

- **EX064 — Data classes.** Name three data classes. *Rubric:* 3 = readings, customer details, aggregates, logs, images; 2 = two; 1 = one; 0 = none.
- **EX065 — Flow checks.** What four checks are made per flow? *Rubric:* 3 = authenticated, authorised, encrypted, logged; 2 = three; 1 = one; 0 = none.
- **EX066 — Billing fix.** What changed for the billing export? *Rubric:* 3 = read-only view of totals; 2 = partial; 1 = none; 0 = none.

### Synthesis

Models of components, identities and data reveal missing controls.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Cloud and container security: threat and failure analysis

### Learning outcomes

You will (1) analyse threats and failures for meterhub systematically; (2) use STRIDE-style categories; (3) consider accidental failures; (4) rank scenarios and link controls.

### 23.1 Threat categories

Using the STRIDE categories Shostack (2014) teaches: spoofing (a fake meter or service), tampering (altered readings or images), repudiation (unlogged admin changes), information disclosure (public buckets, leaked keys), denial of service (ingest floods), elevation of privilege (privileged pods reaching the node).

### 23.2 Failure analysis

Not all problems are attacks. Failures include expired certificates stopping ingest, a policy change blocking legitimate traffic, a node pool upgrade evicting pods and a misconfigured lifecycle rule deleting data early.

### 23.3 Scenarios

Each scenario names a cause, a path and an impact: "A developer pushes an image with an embedded key to a public registry; the key allows reading three buckets; readings could be exposed." Scenarios stay at outcome level, without procedures.

### 23.4 Ranking

Likelihood and impact are rated with evidence such as past incidents and exposure.

### 23.5 Linking controls

Each scenario lists preventive, detective and recovery controls and their requirement IDs.

### 23.6 Review

The analysis is repeated when the architecture changes.

### Using the ranking

The top five scenarios get named owners and dates. Lower-ranked scenarios are reviewed quarterly. Elena notes that the analysis took two workshops of two hours each with platform engineers and developers; involving developers surfaced two failure modes the platform team had not considered, including the lifecycle rule risk.

### Scenario register

Scenarios live in a register with owner, controls and review date.

### Worked example

The analysis ranks "privileged pod gains node access and reads other pods' data" as high impact; it links to R3 and the node-agent exception. Elena adds a requirement that excepted privileged workloads run on a dedicated node pool, limiting what they could reach.

> **Synthetic case.** Scenarios are synthetic.

### Errors and limits

Threat lists can grow endlessly; focus on scenarios that change decisions.

### Exercises

- **EX067 — STRIDE example.** Give an information disclosure example. *Rubric:* 3 = public bucket or leaked key; 2 = partial; 1 = none; 0 = none.
- **EX068 — Failure example.** Name an accidental failure. *Rubric:* 3 = expired certificate, blocking policy, eviction, lifecycle rule; 2 = one; 1 = none; 0 = none.
- **EX069 — New requirement.** What requirement followed the privileged-pod scenario? *Rubric:* 3 = dedicated node pool for exceptions; 2 = partial; 1 = none; 0 = none.

### Synthesis

Analyse attacks and accidents, then link scenarios to controls.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Cloud and container security: methods I

### Learning outcomes

You will (1) design default-deny network policies; (2) compute reachability before and after; (3) allow only documented flows; (4) test policies safely.

### 24.1 The method

Start from the documented and observed flows (chapter 11), apply a default-deny policy to the namespace, then add allow rules for each legitimate flow. The Kubernetes network policy documentation explains that once a pod is selected by a policy, traffic not allowed by some policy is denied.

### Lab — Lab — network reachability

```python
"""Reachability between synthetic pods: no policy vs default-deny with allow rules (stdlib only)."""
pods = ["web", "api", "db", "metrics"]
allow = {("web", "api"), ("api", "db"), ("metrics", "api"), ("metrics", "db")}
total = len(pods) * (len(pods) - 1)
print(f"no policies: {total}/{total} pod pairs reachable")
ok = sorted(f"{a}->{b}" for a in pods for b in pods if a != b and (a, b) in allow)
print(f"default deny + allows: {len(ok)}/{total} reachable: {', '.join(ok)}")
print("web->db reachable:", ("web", "db") in allow)
```

Run with `python3 lab_netpol.py`. Verified output:

```text
no policies: 12/12 pod pairs reachable
default deny + allows: 4/12 reachable: api->db, metrics->api, metrics->db, web->api
web->db reachable: False
```

### 24.2 Lab result

With no policies, all 12 directed pod pairs among web, api, db and metrics are reachable. With default deny plus four allows, only 4 of 12 are: api->db, metrics->api, metrics->db and web->api. web->db is no longer reachable, so a flaw in the web pod could not reach the database directly.

### 24.3 Egress too

Default deny should cover egress as well as ingress; DNS egress must be allowed explicitly or name resolution fails.

### 24.4 Testing safely

Policies are applied first in the test cluster, with connection tests for every allowed and a sample of denied pairs. Some network plugins offer audit modes; otherwise staged rollout by namespace is used.

### 24.5 Labels

Policies select pods by labels; inconsistent labels cause surprises, so label standards are enforced in the pipeline.

### 24.6 Monitoring

Denied connection logs show legitimate traffic that was missed.

### Rollout order

Namespaces are rolled out from least to most critical, so lessons from simple services improve the policies for meterhub ingest, which goes last.

### Worked example

In meterhub's test cluster, the first default-deny rollout breaks metrics collection because the metrics stack scrapes through a port not in the documented flows. The denied-connection log shows it within minutes; an allow rule is added and the test repeated before production rollout.

> **Synthetic case.** Pods and flows are synthetic.

### Errors and limits

Network policies depend on the network plugin enforcing them; confirm the cluster's plugin supports them.

### Exercises

- **EX070 — Lab counts.** How many pairs were reachable before and after? *Rubric:* 3 = 12/12 then 4/12; 2 = partial; 1 = none; 0 = none.
- **EX071 — web->db.** Why does blocking web->db matter? *Rubric:* 3 = web flaw cannot reach database directly; 2 = partial; 1 = none; 0 = none.
- **EX072 — Metrics breakage.** What broke and how was it found? *Rubric:* 3 = metrics scraping; denied log; 2 = partial; 1 = none; 0 = none.

### Synthesis

Default deny plus documented allows shrinks reachability sharply.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) design an end-to-end secure deployment path for meterhub in a team; (2) critique alternatives; (3) produce a design review package; (4) incorporate feedback.

### 25.1 The brief

Teams design how code becomes a running meterhub workload: build, scan, sign, store, admit, deploy and observe, meeting requirements R1 to R6.

### 25.2 Alternatives

Team A proposes push-based deployment from the pipeline with a production deployer identity. Team B proposes pull-based GitOps, where a controller in the cluster pulls approved manifests. Elena's team compares them on credentials exposed, auditability and recovery.

### 25.3 Comparison

Pull-based deployment means the pipeline never holds cluster credentials, and the cluster's state is always reconciled to the repository. Push-based is simpler to adopt. Both can verify signatures at admission.

### 25.4 Review package

Diagram, requirement trace, threat scenarios addressed, open risks and a test plan.

### 25.5 Critique

Studio critics ask how emergency fixes work if the repository is unavailable, and who can change the GitOps controller itself.

### 25.6 Revision

The design adds a documented break-glass path with alerts, and restricts controller changes to a separate reviewed repository.

### Studio process

Each team has two weeks: one for design, one for review and revision. Critics are platform engineers from another energy company, invited under a confidentiality agreement and shown only synthetic diagrams. Their outside view is valuable: they point out that GitOps controllers themselves need updates and monitoring. Teams are assessed on clarity, trace to requirements, honesty about open risks and response to critique, not on choosing a particular design.

### Package format

Review packages are limited to ten pages so critics can read them fully.

### Worked example

The panel selects the pull-based design for production with the break-glass addition. Elena's team notes that it also addresses the console-change problem: manual edits are reverted by reconciliation.

> **Synthetic case.** Designs are synthetic.

### Errors and limits

Studio designs skip operational details; plan pilots before committing.

### Exercises

- **EX073 — Brief stages.** List the deployment path stages. *Rubric:* 3 = build, scan, sign, store, admit, deploy, observe; 2 = four; 1 = two; 0 = none.
- **EX074 — Pull advantage.** What is pull-based deployment's credential advantage? *Rubric:* 3 = pipeline holds no cluster credentials; 2 = partial; 1 = none; 0 = none.
- **EX075 — Critique.** What did critics ask? *Rubric:* 3 = emergency path; who changes controller; 2 = two; 1 = one; 0 = none.

### Synthesis

Compare designs on credentials, auditability and recovery.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Cloud and container security: architecture alternatives

### Learning outcomes

You will (1) compare isolation and tenancy architectures for meterhub; (2) evaluate cost, risk and operations; (3) choose with explicit criteria; (4) record the decision.

### 26.1 The options

Option 1: one shared cluster with namespaces per service and strict policies. Option 2: one cluster per environment and sensitivity tier. Option 3: one cluster per service. Each gives a different balance of isolation, cost and operational effort.

### 26.2 Criteria

Blast radius if a workload is compromised; cost of control planes and nodes; operational effort for upgrades; consistency of policy; regulator expectations for separation of payment data.

### 26.3 Evaluation

Option 1 is cheapest but relies on Kubernetes isolation between namespaces; NIST SP 800-190 suggests grouping containers by sensitivity. Option 3 isolates best but multiplies upgrade work by the number of services. Option 2 balances them: a high-sensitivity cluster for readings and payments, a standard cluster for other services.

### 26.4 Hybrid with nodes

Within a cluster, dedicated node pools for sensitive or privileged workloads add separation at the host level.

### 26.5 Decision

Option 2 with dedicated node pools, recorded in an architecture decision record with criteria scores.

### 26.6 Revisit triggers

The decision is revisited if the number of services doubles, the regulator changes rules or a namespace isolation weakness is published.

### Scoring the options

Each criterion is scored 1 to 5 by three engineers independently, then discussed. Disagreements on operational effort lead to a quick estimate of upgrade hours per cluster, which settles the scores. The scored table goes into the decision record.

### Exit path

The decision notes how to merge clusters later if needs change.

### Worked example

The finance team questions the extra cluster's cost. Elena shows that it is about 8% of platform spending and that it lets audits of the payment service cover one small cluster instead of the whole estate, saving auditor time each year.

> **Synthetic case.** Options and costs are synthetic.

### Errors and limits

Strong isolation can create false confidence if identities span clusters; check identity boundaries too.

### Exercises

- **EX076 — Three options.** Name the three options. *Rubric:* 3 = shared, per tier, per service; 2 = two; 1 = one; 0 = none.
- **EX077 — Chosen option.** Which option was chosen? *Rubric:* 3 = per tier with dedicated node pools; 2 = partial; 1 = none; 0 = none.
- **EX078 — Cost argument.** How was the extra cost justified? *Rubric:* 3 = ~8%, simpler audits; 2 = partial; 1 = none; 0 = none.

### Synthesis

Choose isolation with explicit criteria and revisit triggers.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Cloud and container security: control design

### Learning outcomes

You will (1) design admission, identity and storage controls in detail; (2) specify behaviour, exceptions and failure modes; (3) make controls observable; (4) avoid single points of failure.

### 27.1 Admission control

Pod Security admission enforces the Restricted profile on production namespaces; a policy engine adds checks for image signatures, resource limits and allowed registries. Policies are code, reviewed and tested.

### 27.2 Failure mode

If the policy engine is unavailable, should deployments fail closed (blocked) or open (allowed)? Solent chooses fail closed for production with a monitored, highly available engine, and fail open with alerts for test clusters.

### 27.3 Identity controls

Workload identity bindings map each service account to one cloud role with minimal permissions. Organisation policy disallows creating long-lived keys for service accounts.

### 27.4 Storage controls

Account-level settings block public access to storage; bucket policies require encrypted connections; customer-managed keys protect readings.

### 27.5 Exceptions

Exceptions are labels on namespaces or workloads that reference a ticket and expiry date; the policy engine checks expiry.

### 27.6 Observability

Every denial is logged with the rule and reason and counted on a dashboard; repeated denials for the same team prompt help, not punishment.

### Policy testing

Policies are code, so they have unit tests: each rule is tested with a compliant and a non-compliant synthetic object. Tests run in the pipeline before a policy change reaches any cluster. A policy change that breaks a test cannot merge, which prevents a typo from blocking every deployment in production or, worse, silently allowing what it should block.

### Worked example

Elena tests the fail-closed design by stopping one of three policy engine replicas in staging; deployments continue. Stopping all three blocks deployments as intended, and an alert fires within a minute, confirming the failure mode is visible.

> **Synthetic case.** Controls and tests are synthetic.

### Errors and limits

Fail-closed controls become availability risks; invest in their reliability.

### Exercises

- **EX079 — Fail mode.** What failure mode was chosen for production? *Rubric:* 3 = fail closed with HA engine; 2 = partial; 1 = none; 0 = none.
- **EX080 — Key prevention.** How are long-lived keys prevented? *Rubric:* 3 = org policy disallows creation; 2 = partial; 1 = none; 0 = none.
- **EX081 — Engine test.** What did the replica test show? *Rubric:* 3 = continues with one down; blocks and alerts when all down; 2 = partial; 1 = none; 0 = none.

### Synthesis

Specify how controls behave, fail and are observed.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Cloud and container security: implementation I

### Learning outcomes

You will (1) implement workload identity and storage guardrails; (2) migrate services off long-lived keys; (3) verify each step; (4) manage rollout risk.

### 28.1 Plan

Migrate services one at a time from long-lived keys to workload identity: create the role binding, deploy the service using it, confirm it works, then disable and delete the old key.

### 28.2 Inventory

A query lists all service account keys in Solent's cloud accounts: 23 keys, of which 9 had not been used in 90 days.

### 28.3 Unused keys

Unused keys are disabled first, not deleted, for two weeks. If nothing breaks, they are deleted.

### 28.4 Active keys

Active keys are migrated service by service, with each service owner present.

### 28.5 Storage guardrail

Account-level public access blocking is enabled on test accounts first, then production. A query beforehand lists buckets with public access and their documented reasons: none in production after chapter 13's fixes.

### 28.6 Verification

After each migration, a check confirms the service has no keys and that its role has only the expected permissions.

### Communicating the migration

Each service owner receives a short note before their migration: what changes, when, how to tell if it worked and who to contact. After migration, they confirm their service's health. Clear communication keeps trust high, and owners volunteer their services for earlier slots once the first migrations go smoothly. Elena keeps a migration log with each service, date, result and any issues, which becomes evidence for the regulator.

### Rollback plan

Each migration keeps the old key disabled, not deleted, for a week as a rollback path.

### Worked example

Migration takes six weeks. One legacy import job cannot use workload identity because it runs outside the cluster on a scheduled VM; it receives a VM-attached identity instead, also short-lived, and the last long-lived key is deleted. Elena records "long-lived workload keys: 0" as evidence for R1.

> **Synthetic case.** Keys and services are synthetic.

### Errors and limits

Disabling before deleting avoids irreversible mistakes.

### Exercises

- **EX082 — Key inventory.** How many keys were found and unused? *Rubric:* 3 = 23; 9 unused; 2 = partial; 1 = none; 0 = none.
- **EX083 — Disable first.** Why disable before deleting? *Rubric:* 3 = avoid irreversible breakage; 2 = partial; 1 = none; 0 = none.
- **EX084 — Legacy job.** How was the legacy job handled? *Rubric:* 3 = VM-attached short-lived identity; 2 = partial; 1 = none; 0 = none.

### Synthesis

Migrate carefully, verify each step and record evidence.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Cloud and container security: measurement

### Learning outcomes

You will (1) define control coverage measures; (2) compute coverage per namespace; (3) track progress; (4) interpret measures carefully.

### 29.1 Coverage measures

For each production namespace, Elena records whether four controls are in place: default-deny network policy, Restricted pod security, image signature enforcement and resource limits on all pods.

### Lab — Lab — control coverage

```python
"""Control coverage per namespace for four controls (stdlib only)."""
ctrl = ["netpol-default-deny", "pod-security-restricted", "image-signature", "resource-limits"]
ns = {"meterhub": [1, 1, 1, 1], "billing": [1, 1, 0, 1], "reports": [0, 1, 0, 1], "legacy-import": [0, 0, 0, 1]}
for n, v in ns.items():
    miss = [c for c, x in zip(ctrl, v) if not x]
    print(f"{n:14} {sum(v)}/4 {'missing: ' + ', '.join(miss) if miss else ''}")
allv = [x for v in ns.values() for x in v]
print(f"overall coverage {sum(allv)}/{len(allv)} = {100*sum(allv)/len(allv):.0f}%")
```

Run with `python3 lab_coverage.py`. Verified output:

```text
meterhub       4/4 
billing        3/4 missing: image-signature
reports        2/4 missing: netpol-default-deny, image-signature
legacy-import  1/4 missing: netpol-default-deny, pod-security-restricted, image-signature
overall coverage 10/16 = 62%
```

### 29.2 Lab result

meterhub has 4 of 4 controls. billing has 3 of 4 (missing image-signature). reports has 2 of 4 (missing netpol-default-deny and image-signature). legacy-import has 1 of 4 (missing netpol-default-deny, pod-security-restricted and image-signature). Overall coverage is 10 of 16 controls, 62%.

### 29.3 Interpreting

Coverage says a control is configured, not that it is effective; an allow-all policy would count as a policy. Elena's checker therefore requires a default-deny policy specifically, and verification tests (later chapters) check behaviour.

### 29.4 Weighting

Namespaces differ in sensitivity; a missing control in billing matters more than in reports. The dashboard shows both raw and sensitivity-weighted coverage.

### 29.5 Trends

Monthly coverage is plotted; a drop signals new namespaces without controls or removed controls.

### Sensitivity weighting

Weights are set with the data protection officer: namespaces handling readings or payments count three times, others once. Weighted coverage starts at 58%, lower than raw coverage, because the biggest gaps are in billing. This helps focus effort where data are most sensitive. Elena reports both numbers so neither hides the other.

### Reporting cadence

Coverage is reported monthly to the platform lead and quarterly to Solent's risk committee, with the causes of gaps and the plan for each. Reports show trend lines rather than single numbers.

### Worked example

The image-signature gap across three namespaces traces to one cause: their images were built by an older pipeline without signing. Moving them to the standard pipeline closes all three gaps in a sprint, raising coverage to 13 of 16.

> **Synthetic case.** Namespaces and figures are synthetic.

### Errors and limits

Measures can be gamed; check what each one counts.

### Exercises

- **EX085 — Lab overall.** What was overall coverage? *Rubric:* 3 = 10/16, 62%; 2 = partial; 1 = none; 0 = none.
- **EX086 — legacy-import.** What was legacy-import missing? *Rubric:* 3 = netpol, pod security, image signature; 2 = two; 1 = one; 0 = none.
- **EX087 — Signature cause.** Why were signatures missing? *Rubric:* 3 = older pipeline without signing; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure coverage, then check effectiveness.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify controls with safe, synthetic tests; (2) check admission, network and identity controls behave as specified; (3) record evidence; (4) handle failures.

### 30.1 Lab setup

A test cluster mirrors production policies. Tests use synthetic workloads designed to violate one rule each, so a correct control rejects them. No production systems are touched.

### 30.2 Admission tests

A synthetic pod requesting privileged mode must be rejected; one without runAsNonRoot must be rejected; an unsigned image must be rejected; a compliant pod must be admitted.

### 30.3 Network tests

From a test pod labelled web, a connection to db must fail and a connection to api must succeed, matching the chapter 24 design.

### 30.4 Identity tests

A test service with workload identity can read its allowed bucket and is refused writing to another; no keys exist for the service account.

### 30.5 Recording

Each test records requirement, input, expected and actual result, time and cluster version.

### 30.6 Failures

A failed test is a defect with an owner, not a test to rewrite.

### Parity checks

Before each verification run, a script compares policy versions, namespace labels and admission configuration between the test cluster and production, and stops the run if they differ. This ensures results describe production. The first parity check finds the test cluster one policy version behind, which is corrected before testing.

### Evidence storage

Results are stored in the repository, versioned with the policies they tested, so auditors can see exactly which policy version passed which test and when.

### Worked example

One test fails: a pod with allowPrivilegeEscalation unset is admitted. Investigation shows the namespace label set the profile to Baseline, not Restricted, after a copy-paste error. The label is fixed, the test passes, and a pipeline check is added for namespace labels.

> **Synthetic case.** Tests and results are synthetic.

### Errors and limits

Verification in a test cluster assumes it matches production; check configuration parity.

### Exercises

- **EX088 — Test design.** How are admission tests designed? *Rubric:* 3 = synthetic workloads violating one rule each; 2 = partial; 1 = none; 0 = none.
- **EX089 — Network test.** What network results are expected? *Rubric:* 3 = web->db fails; web->api succeeds; 2 = partial; 1 = none; 0 = none.
- **EX090 — Failure cause.** Why was the escalation test admitted? *Rubric:* 3 = namespace label set Baseline; 2 = partial; 1 = none; 0 = none.

### Synthesis

Safe synthetic tests prove controls behave as designed.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Cloud and container security: implementation II

### Learning outcomes

You will (1) implement image signing, admission verification and default-deny networking across production; (2) sequence the rollout; (3) manage exceptions; (4) confirm results.

### 31.1 Image signing

The standard pipeline signs every image after build and scanning, and records the image digest. Admission verifies the signature and that the image comes from Solent's registry. Images are referenced by digest, not mutable tags, so what was verified is what runs.

### 31.2 Rollout sequence

Signature verification starts in audit mode, logging unsigned images without blocking, for two weeks. The log shows which teams still use old pipelines. Enforcement follows namespace by namespace once each is clean.

### 31.3 Network policies

Default-deny policies roll out in the order from chapter 24, with denied-connection logs watched for a day after each namespace.

### 31.4 Exceptions

The node agent keeps its exception on a dedicated node pool; the two services writing to their root filesystem complete their changes and their exception expires on time.

### 31.5 Communication

A shared calendar shows each namespace's enforcement date. Teams can ask for a delay with a reason, approved by the platform lead.

### 31.6 Confirming

After each step, verification tests from chapter 30 run again in production using synthetic test workloads in a dedicated test namespace.

### 31.7 Cleanup

Old pipeline jobs that cannot sign images are archived so they cannot be used by mistake.

### Signing keys

Signing keys live in a managed key service; the pipeline can request signatures but cannot export the key.

### Worked example

Audit mode reveals a third-party monitoring image pulled directly from a public registry. Instead of an exception, the platform team mirrors it into Solent's registry after checking its published digest and signs it with a separate key marked "third-party, verified", keeping one admission rule for all images.

> **Synthetic case.** Images and timelines are synthetic.

### Errors and limits

Audit periods that never end become permanent gaps; set an end date.

### Exercises

- **EX091 — Digest use.** Why reference images by digest? *Rubric:* 3 = what was verified is what runs; 2 = partial; 1 = none; 0 = none.
- **EX092 — Audit mode.** What did audit mode achieve? *Rubric:* 3 = found teams on old pipelines without blocking; 2 = partial; 1 = none; 0 = none.
- **EX093 — Third-party image.** How was the monitoring image handled? *Rubric:* 3 = mirrored, digest-checked, signed as third-party; 2 = partial; 1 = none; 0 = none.

### Synthesis

Roll out enforcement after audit periods and keep one rule for all images.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Cloud and container security: reliability

### Learning outcomes

You will (1) ensure security controls do not reduce reliability; (2) design highly available control components; (3) plan for certificate and key expiry; (4) measure control-induced incidents.

### 32.1 Controls as dependencies

Admission controllers, policy engines, secret managers and identity services are now on the critical path for deployments and running services. If they fail, so does meterhub.

### 32.2 High availability

The policy engine runs three replicas across zones with a disruption budget so upgrades never remove more than one. The secret manager is a managed cloud service with regional redundancy.

### 32.3 Expiry

Certificates and signing keys expire. Elena lists every certificate and key with expiry dates and adds alerts at 30 and 7 days. An expired webhook certificate would block all deployments.

### 32.4 Timeouts

Admission webhooks have short timeouts so a slow engine causes a clear failure rather than hanging deployments.

### 32.5 Measuring

Incidents caused by security controls are tracked separately; the goal is fewer than one per quarter after rollout.

### 32.6 Error budgets

Solent's site reliability practice gives each service an error budget; control-induced outages count against it, which gives the platform team a reason to make controls reliable.

### 32.7 Game days

Planned exercises simulate control failures in staging to practise recovery.

### Disruption budgets

A pod disruption budget tells Kubernetes how many replicas of a component may be unavailable during voluntary disruptions such as node upgrades. For the policy engine it is set to allow at most one unavailable replica. Elena tests it by draining a node in staging and confirming the engine keeps serving admission requests throughout. Similar budgets are set for ingest, so upgrades never drop it below the capacity needed for the evening peak.

### Worked example

A game day simulates the signing key's certificate expiring. Deployments are blocked as designed; the runbook for emergency rotation takes 25 minutes, longer than the 10-minute target. Steps are scripted and the next exercise completes in 8 minutes.

> **Synthetic case.** Components and timings are synthetic.

### Errors and limits

Reliability work on controls is often skipped because controls are seen as "security", not "service"; they are both.

### Exercises

- **EX094 — Critical path.** Why are controls on the critical path? *Rubric:* 3 = deployments and services depend on them; 2 = partial; 1 = none; 0 = none.
- **EX095 — Expiry alerts.** When do expiry alerts fire? *Rubric:* 3 = 30 and 7 days; 2 = partial; 1 = none; 0 = none.
- **EX096 — Game day result.** What did the game day show? *Rubric:* 3 = rotation 25 min, then 8 after scripting; 2 = partial; 1 = none; 0 = none.

### Synthesis

Make security controls as reliable as the services they protect.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Cloud and container security: safety and resilience

### Learning outcomes

You will (1) design meterhub to keep essential functions during incidents; (2) separate safety-relevant data paths; (3) plan recovery from compromise; (4) test resilience.

### 33.1 Essential functions

For an energy co-op, essential functions are ingesting readings (data must not be lost), billing accuracy and tamper alerts. Customer portal features are less critical.

### 33.2 Graceful degradation

If the API is attacked or overloaded, ingest continues on separate infrastructure. Queues buffer readings if the database is unavailable.

### 33.3 Recovery from compromise

If a cluster is suspected compromised, the plan is to rebuild from code in a clean account rather than clean it in place: declarative configuration and signed images make rebuilds repeatable.

### 33.4 Backups and immutability

Backups in a separate account with deletion protection allow recovery even if production credentials are misused.

### 33.5 Isolation of blast radius

Separate clusters and accounts (chapter 26) limit how far a compromise spreads.

### 33.6 Exercises

Resilience exercises rebuild the standard cluster from code in a fresh account and measure the time to restore ingest.

### 33.7 Communication

Incident plans include messages to customers and the regulator.

### Tamper alerts

Tamper alerts from meters are routed through a separate, small service with its own queue, so they keep flowing even if the main ingest path is degraded. Elena includes this path in the rebuild exercise and confirms alerts resume within 20 minutes in a fresh account. She also notes that tamper alerts have a regulatory reporting duty, so their path is documented for the regulator.

### Recording lessons

Each exercise ends with a short review listing what slowed recovery and the fix.

### Worked example

The first rebuild exercise takes 6 hours, mainly waiting for manual approvals to create new accounts. Pre-approved account templates cut the next exercise to 2.5 hours, within the 4-hour objective for restoring ingest.

> **Synthetic case.** Exercises and timings are synthetic.

### Errors and limits

Rebuild plans fail if secrets or configuration live outside version control; inventory them.

### Exercises

- **EX097 — Essential functions.** List meterhub's essential functions. *Rubric:* 3 = ingest, billing accuracy, tamper alerts; 2 = two; 1 = one; 0 = none.
- **EX098 — Rebuild reason.** Why rebuild rather than clean a compromised cluster? *Rubric:* 3 = repeatable from code and signed images; 2 = partial; 1 = none; 0 = none.
- **EX099 — Exercise time.** How long did rebuilds take? *Rubric:* 3 = 6 h then 2.5 h; 2 = partial; 1 = none; 0 = none.

### Synthesis

Plan to keep essential functions and rebuild cleanly.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Cloud and container security: integration

### Learning outcomes

You will (1) integrate cloud controls with logging, incident response, change management and the wider organisation; (2) connect alerts to people; (3) align with governance.

### 34.1 Logging

Cloud audit logs, Kubernetes audit logs, admission decisions and network denials flow to Solent's central log platform, kept for a year in a separate account.

### 34.2 Alerting

High-risk events (public access settings changed, new keys created, policy engine disabled, privileged pod admitted under exception) raise alerts routed to the on-call engineer, meeting the 15-minute objective from chapter 7.

### 34.3 Incident response

Runbooks describe first steps for each alert type, including revoking credentials and isolating namespaces.

### 34.4 Change management

Policy changes follow the normal change process with security review; emergency changes are reviewed afterwards.

### 34.5 Governance

Monthly coverage and incidents feed Solent's risk committee; CSA CCM v4 mapping supports the regulator's annual review.

### 34.6 People

Developers get training on the new controls and a help channel; the platform team runs office hours.

### 34.7 Integration testing

Synthetic events are injected monthly to check each alert reaches the on-call engineer.

### Training developers

Training is short and practical: a one-hour session showing how admission messages explain a rejection, how to request an exception and how to read denied-connection logs. Rejection messages link to a page with the rule, the reason and an example fix. After training, help-channel questions about rejections fall by half, and most remaining ones lead to clearer messages.

### Ownership of alerts

Every alert rule has an owning team and a runbook link, checked quarterly so that rules without owners are fixed or removed.

### Worked example

An injected "public access setting changed" event takes 31 minutes to reach on-call because the alert rule's severity was set to low. The rule is corrected, and the monthly injection is added to the verification schedule.

> **Synthetic case.** Systems and events are synthetic.

### Errors and limits

Alerts nobody receives are equivalent to no alerts.

### Exercises

- **EX100 — Alert examples.** Name three high-risk alerts. *Rubric:* 3 = public access, new keys, engine disabled, privileged pod; 2 = two; 1 = one; 0 = none.
- **EX101 — Log retention.** Where and how long are logs kept? *Rubric:* 3 = separate account, one year; 2 = partial; 1 = none; 0 = none.
- **EX102 — Injection finding.** What did the injection test find? *Rubric:* 3 = 31 min due to low severity; 2 = partial; 1 = none; 0 = none.

### Synthesis

Controls work only when integrated with people and processes.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design monitoring and response for configuration drift and policy exceptions; (2) critique designs in teams; (3) produce an operational design package.

### 35.1 The brief

Design how Solent detects and responds to differences between declared and running configuration, and manages exceptions through their life.

### 35.2 Alternatives

Team A proposes relying on GitOps reconciliation to revert drift silently. Team B proposes reconciliation plus alerts for security-relevant drift. Elena's team proposes B plus a weekly drift report covering resources outside GitOps, such as cloud accounts.

### 35.3 Trade-offs

Silent reversion hides useful signals: someone made a manual change, perhaps during an incident. Alerts on every drift create noise. Elena's team limits alerts to security-relevant fields.

### 35.4 Exceptions life cycle

Request, review, approval, labelled implementation, expiry reminder, renewal or removal, all logged.

### 35.5 Package

Diagrams, alert list with severities, exception workflow and test plan.

### 35.6 Critique

Critics ask what happens to drift in resources the GitOps controller does not manage; Elena's weekly report addresses this.

### Assessment

Teams are assessed on whether their design meets the brief, the quality of trade-off reasoning, the test plan and the response to critique. Elena's team loses a point for an alert list without clear owners, which they fix in the final package. The studio reinforces that operational design deserves the same rigour as building controls. Each team also writes a one-paragraph reflection on what they would change after critique, which the tutor reads alongside the package.

### Prototype

Elena's team builds a small prototype of the weekly report on synthetic data to show it is feasible before the panel.

### Worked example

The panel adopts Elena's team's design, noting that the weekly report would have caught the opening case's missing network policies, since they were declared in a design document but never in code.

> **Synthetic case.** Designs are synthetic.

### Errors and limits

Drift detection needs a trustworthy declared state; keep the repository protected.

### Exercises

- **EX103 — Silent reversion.** What is the problem with silent reversion? *Rubric:* 3 = hides manual change signals; 2 = partial; 1 = none; 0 = none.
- **EX104 — Exception steps.** List the exception life cycle steps. *Rubric:* 3 = request, review, approve, implement, remind, renew/remove; 2 = four; 1 = two; 0 = none.
- **EX105 — Opening case link.** How would the design have caught the opening case? *Rubric:* 3 = weekly report vs declared design; 2 = partial; 1 = none; 0 = none.

### Synthesis

Detect drift, alert on what matters and manage exceptions through their life.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Cloud and container security: performance and scale

### Learning outcomes

You will (1) measure the performance cost of security controls; (2) analyse latency percentiles; (3) plan controls for growth; (4) optimise without weakening protection.

### 36.1 Why measure

Developers worry that admission checks and signature verification slow deployments. Measurement replaces worry with data and shows where optimisation is needed.

### Lab — Lab — admission overhead

```python
"""Admission check overhead on synthetic deployment latencies (ms): median and p95 with and without (stdlib only)."""
import statistics
base = [180, 190, 200, 205, 210, 215, 220, 230, 240, 260, 270, 300, 310, 330, 350, 400, 420, 450, 500, 610]
withc = [b + d for b, d in zip(base, [12, 14, 15, 15, 16, 16, 17, 18, 18, 19, 20, 20, 21, 22, 24, 25, 28, 30, 35, 60])]
def p95(x): return statistics.quantiles(x, n=20, method="inclusive")[18]
print(f"median {statistics.median(base)} -> {statistics.median(withc)} ms; p95 {p95(base):.1f} -> {p95(withc):.1f} ms")
```

Run with `python3 lab_overhead.py`. Verified output:

```text
median 265.0 -> 284.5 ms; p95 505.5 -> 541.8 ms
```

### 36.2 Lab result

Across 20 synthetic deployments, median admission latency rises from 265.0 ms without the policy checks to 284.5 ms with them, about 20 ms. The 95th percentile rises from 505.5 to 541.8 ms, about 36 ms. Deployments take minutes overall, so the overhead is negligible; the tail grows more than the median because signature lookups occasionally miss the cache.

### 36.3 Scaling

As meters grow (chapter 6), ingest pods and deployments increase. Policy checks are per admission, not per request, so they scale with deployment frequency, not traffic.

### 36.4 Network policy cost

Network policy enforcement happens in the node's data path; Elena measures ingest throughput with and without policies and sees under 2% difference.

### 36.5 Optimisation

Caching signature verification results by digest cuts repeated lookups; the policy engine's replicas scale with admission load.

### 36.6 Never trading away protection

Optimisations must not skip checks; caching by digest is safe because the digest identifies exact content.

### Measurement method

Elena measures admission latency from the API server's own metrics in staging, running the same synthetic deployments with the policy checks enabled and disabled in alternating batches. Alternating reduces the effect of background load changing over the test. She records cluster version, node sizes and policy version with the results so the test can be repeated.

### Worked example

After adding a digest cache, the synthetic p95 overhead drops to about 15 ms in a repeat test. Elena publishes the measurements to developers, which ends a long-running debate about whether the controls "slow everything down".

> **Synthetic case.** Latencies are synthetic.

### Errors and limits

Small samples give noisy percentiles; repeat measurements before deciding.

### Exercises

- **EX106 — Lab medians.** What were the medians? *Rubric:* 3 = 265.0 to 284.5 ms; 2 = partial; 1 = none; 0 = none.
- **EX107 — Tail growth.** Why did the tail grow more? *Rubric:* 3 = cache misses on signature lookups; 2 = partial; 1 = none; 0 = none.
- **EX108 — Safe cache.** Why is caching by digest safe? *Rubric:* 3 = digest identifies exact content; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure control costs and optimise without weakening checks.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Cloud and container security: operations

### Learning outcomes

You will (1) run the secured platform day to day; (2) handle alerts, exceptions and upgrades; (3) keep runbooks current; (4) measure operational load.

### 37.1 Daily operations

The on-call engineer reviews overnight alerts, the exception expiry list and the drift report. Most days take under 30 minutes.

### 37.2 Upgrades

Kubernetes minor versions are upgraded within the provider's support window. Each upgrade is tested in staging with the verification suite, since admission behaviour can change between versions.

### 37.3 Exception handling

Weekly, the platform lead reviews new requests and upcoming expiries. Exceptions near expiry trigger a message to owners.

### 37.4 Runbooks

Each alert has a runbook with first steps, escalation and communication. Runbooks are tested in game days and updated after incidents.

### 37.5 Operational load

Elena tracks time spent on security operations: in the first quarter after rollout, about 6 engineer-hours a week, falling to 3 as tooling improves.

### 37.6 Incident example

A developer accidentally creates a public test bucket in a sandbox account. The account-level block prevents public access; an alert still fires for the attempted change, and a short note reminds the developer of the sandbox rules.

### 37.7 Continuous improvement

Each month the team picks one source of repetitive work and automates or removes it.

### Handover between shifts

On-call handover includes a short written note: open alerts, exceptions expiring that week, upgrades planned and anything unusual. The note lives in the team channel so others can see the platform's state at a glance. Missed handovers were a cause of two slow responses before this practice started.

### Calm operations

A quiet platform is the goal.

### Worked example

Exception reviews show three services renewing the same exception repeatedly. The platform team works with them to remove the underlying need, a log path written to the root filesystem, and the exceptions end.

> **Synthetic case.** Operations data are synthetic.

### Errors and limits

Operational load that grows unnoticed leads to controls being weakened; track it.

### Exercises

- **EX109 — Daily tasks.** What does on-call review daily? *Rubric:* 3 = alerts, exception expiries, drift report; 2 = two; 1 = one; 0 = none.
- **EX110 — Upgrade testing.** Why test upgrades with the verification suite? *Rubric:* 3 = admission behaviour can change; 2 = partial; 1 = none; 0 = none.
- **EX111 — Repeated exceptions.** How were repeated exceptions ended? *Rubric:* 3 = removed underlying need; 2 = partial; 1 = none; 0 = none.

### Synthesis

Steady operations keep controls effective without exhausting teams.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Cloud and container security: validation

### Learning outcomes

You will (1) validate that the engineered system meets stakeholder needs, not just requirements; (2) gather evidence from users, auditors and incidents; (3) compare with goals.

### 38.1 Verification versus validation

Verification asks "did we build it right?" (requirements met). Validation asks "did we build the right thing?" (stakeholders' needs met). A system could pass every test yet frustrate developers so much that they bypass it.

### 38.2 Goals review

Elena compares results with chapter 20's goals: no long-lived workload keys (achieved), default-deny in all production namespaces (achieved), Restricted profile with documented exceptions (achieved, one exception), signed images only (achieved), detection within objectives (achieved after alert fixes).

### 38.3 Developer validation

A survey of 30 developers asks about deployment friction and clarity of rejections. 70% find rejection messages clear; complaints focus on exception request time.

### 38.4 Auditor validation

An internal auditor reviews evidence against CSA CCM v4 mappings and finds evidence sufficient for identity and infrastructure domains, asking for more on key rotation records.

### 38.5 Incident validation

Six months without a credential or exposure incident is encouraging but short; Elena reports it with that caveat.

### 38.6 Adjustments

Exception requests get a 2-day service level; key rotation records are generated automatically.

### Acting on validation

Validation results become backlog items with owners. The exception service level and automatic rotation records are delivered within a month, and the next survey shows exception complaints falling. Elena repeats validation every six months, because needs change as the platform and teams grow. She reports validation alongside verification so leadership sees both whether controls work and whether people can live with them.

### Worked example

The survey also reveals that developers no longer remember why the network policies exist. Elena adds short "why" notes to each policy file linking to the opening case and the threat analysis, so the reasons survive staff changes.

> **Synthetic case.** Survey and audit results are synthetic.

### Errors and limits

Absence of incidents in a short period is weak evidence of effectiveness.

### Exercises

- **EX112 — Ver vs val.** Distinguish verification and validation. *Rubric:* 3 = built it right vs right thing; 2 = partial; 1 = none; 0 = none.
- **EX113 — Survey result.** What did developers report? *Rubric:* 3 = 70% clear; exception time complaints; 2 = partial; 1 = none; 0 = none.
- **EX114 — Audit request.** What did the auditor ask for? *Rubric:* 3 = key rotation records; 2 = partial; 1 = none; 0 = none.

### Synthesis

Validate with the people who use and audit the system.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Cloud and container security: maintainability

### Learning outcomes

You will (1) keep the security platform maintainable; (2) reduce custom code; (3) document decisions; (4) plan for staff changes and technology change.

### 39.1 Prefer standard features

Built-in Pod Security admission is used instead of custom rules where possible; custom policies cover only what the standard does not. Less custom code means less to maintain.

### 39.2 Policy as code quality

Policies follow a style guide, have tests and comments explaining intent. Dead rules are removed.

### 39.3 Documentation

Decision records, runbooks and "why" notes live with the code. A new engineer can understand the platform in a week.

### 39.4 Dependencies

The policy engine, GitOps controller and signing tools have upgrade schedules and owners, like any dependency.

### 39.5 Staff changes

Two engineers know each component; knowledge is shared through pairing and rotation.

### 39.6 Technology change

If Solent changes cloud provider or Kubernetes distribution, controls defined in standard terms (Pod Security Standards, network policies) move more easily than provider-specific ones.

### 39.7 Technical debt

A list of known shortcuts with dates for removal is reviewed quarterly.

### Retiring controls

Controls are retired when they are replaced or no longer needed, with the reason recorded. For example, a custom rule blocking privileged pods is retired when built-in Pod Security admission covers it, after tests show identical behaviour. Retiring controls carefully keeps the policy set small and understandable. Each retirement goes through the same review as a new control, so nothing is removed by accident.

### Review rhythm

Each quarter the team spends one day on maintainability work: removing dead rules, updating docs and upgrading tools.

### Worked example

An onboarding test asks a new platform engineer to add a policy for a new requirement using only the documentation. She completes it in two days and suggests three documentation fixes, which are made.

> **Synthetic case.** Platform details are synthetic.

### Errors and limits

Maintainability erodes slowly; schedule time for it.

### Exercises

- **EX115 — Standard features.** Why prefer built-in Pod Security admission? *Rubric:* 3 = less custom code to maintain; 2 = partial; 1 = none; 0 = none.
- **EX116 — Portability.** Which controls move more easily between platforms? *Rubric:* 3 = standard Kubernetes terms; 2 = partial; 1 = none; 0 = none.
- **EX117 — Onboarding test.** What did the onboarding test show? *Rubric:* 3 = 2 days, 3 doc fixes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Maintainable controls outlast the people who built them.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify declared versus live configuration across the estate; (2) detect drift; (3) classify and respond to drift; (4) record evidence.

### 40.1 Drift

Drift is any difference between the declared configuration in version control and what is live. It may be harmless (an autoscaler changed replicas) or serious (a network policy deleted).

### Lab — Lab — configuration drift

```python
"""Compare desired (declared) settings with live synthetic settings and report drift (stdlib only)."""
desired = {"meterhub/replicas": 3, "meterhub/image": "meterhub@sha256:aa11", "meterhub/runAsNonRoot": True,
           "billing/replicas": 2, "billing/netpol": "default-deny", "reports/limits.cpu": "500m"}
live = {"meterhub/replicas": 3, "meterhub/image": "meterhub@sha256:bb22", "meterhub/runAsNonRoot": True,
        "billing/replicas": 4, "billing/netpol": None, "reports/limits.cpu": "500m"}
drift = [(k, desired[k], live.get(k)) for k in desired if live.get(k) != desired[k]]
for k, d, l in drift:
    print(f"DRIFT {k:22} desired {d}  live {l}")
print(f"{len(drift)}/{len(desired)} settings drifted")
```

Run with `python3 lab_drift.py`. Verified output:

```text
DRIFT meterhub/image         desired meterhub@sha256:aa11  live meterhub@sha256:bb22
DRIFT billing/replicas       desired 2  live 4
DRIFT billing/netpol         desired default-deny  live None
3/6 settings drifted
```

### 40.2 Lab result

Three of six synthetic settings have drifted. meterhub/image runs digest bb22 instead of the declared aa11. billing/replicas is 4 instead of 2. billing/netpol is missing instead of default-deny. The missing network policy is serious and urgent; the image digest needs investigation (an unapproved image?); the replica count is likely the autoscaler and should be excluded from declared state.

### 40.3 Classification

Security-relevant drift (policies, images, identities, privileges) alerts immediately; operational drift is reported weekly.

### 40.4 Response

Serious drift is reverted by reconciliation and investigated: who changed it, why, and was anything exposed in the meantime?

### 40.5 Evidence

Each drift event is recorded with timestamps, cause and resolution.

### Weekly drift report

The weekly report covers resources outside GitOps, such as cloud account settings, comparing them with templates in version control. It lists each difference, its classification and an owner.

### Investigating drift

For each serious drift, the investigation records who changed it, through which path, and whether anything was exposed while it lasted.

### Lab rerun

The lab is rerun after each fix to confirm drift is cleared.

### Worked example

In the lab scenario, the image digest change traces to an emergency hotfix built correctly by the pipeline but deployed by hand; the declared state is updated through a pull request. The missing network policy traces to a namespace recreated during troubleshooting; reconciliation restores it, and a rule now prevents namespace deletion without approval.

> **Synthetic case.** Settings and events are synthetic.

### Errors and limits

Fields that legitimately change, like replica counts, must be excluded or drift reports become noise.

### Exercises

- **EX118 — Lab drift.** What three drifts did the lab find? *Rubric:* 3 = image digest, replicas, missing netpol; 2 = two; 1 = one; 0 = none.
- **EX119 — Replicas.** Why is the replica drift likely harmless? *Rubric:* 3 = autoscaler; 2 = partial; 1 = none; 0 = none.
- **EX120 — Netpol cause.** What caused the missing policy? *Rubric:* 3 = namespace recreated during troubleshooting; 2 = partial; 1 = none; 0 = none.

### Synthesis

Detect, classify and investigate drift from declared state.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Cloud and container security: system optimization

### Learning outcomes

You will (1) optimise the secured platform for cost, effort and risk together; (2) identify waste; (3) remove redundant controls; (4) prioritise improvements by value.

### 41.1 Finding waste

Elena reviews where time and money go: duplicate scanners checking the same images, alerts that never lead to action, idle node pools reserved for exceptions that ended.

### 41.2 Redundant controls

Two image scanners ran in the pipeline with overlapping results. Comparing six months of findings shows one found everything the other did plus more; the weaker one is retired, saving pipeline time.

### 41.3 Noisy alerts

Alerts are ranked by how often they led to action. Three alert rules with no action in six months are reviewed: two are tuned, one removed with the reason recorded.

### 41.4 Cost

The dedicated node pool for privileged workloads now hosts only the node agent; it is right-sized to the smallest suitable machines.

### 41.5 Risk value

Each improvement candidate is scored on risk reduced per engineer-day. Top items: automate key rotation records, add egress limits to two namespaces, shorten exception approval time.

### 41.6 Guarding against over-optimisation

Removing a control requires evidence it is redundant, not just inconvenient.

### 41.7 Results

Optimisation saves about 15% of platform security spending and four engineer-hours a week.

### Sharing savings

Elena reports savings alongside the risk measures, showing that coverage and detection stayed the same or improved while cost fell. This reassures leadership that optimisation did not quietly weaken security.

### Next review

The optimisation review repeats yearly, using the same scoring method so results can be compared.

### Owner sign-off

Each removal is signed off by the control owner.

### Worked example

One proposal is to drop the weekly drift report because GitOps reverts most drift. Elena checks: in six months, the report found four security-relevant drifts outside GitOps-managed resources. The report stays.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Optimisation that removes controls without evidence trades visible savings for invisible risk.

### Exercises

- **EX121 — Redundant scanner.** How was the redundant scanner identified? *Rubric:* 3 = six months comparison, one superset; 2 = partial; 1 = none; 0 = none.
- **EX122 — Score.** How are improvements prioritised? *Rubric:* 3 = risk reduced per engineer-day; 2 = partial; 1 = none; 0 = none.
- **EX123 — Drift report.** Why did the drift report stay? *Rubric:* 3 = found 4 drifts outside GitOps; 2 = partial; 1 = none; 0 = none.

### Synthesis

Optimise with evidence, keeping controls that still find problems.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Cloud and container security: applied research

### Learning outcomes

You will (1) run a small applied study on the platform; (2) frame a question; (3) collect and analyse data; (4) report limits.

### 42.1 The question

Elena asks: "Since admission enforcement began, has the time from a risky workload configuration being proposed to being fixed fallen?" Before enforcement, risky settings were found by weekly scans after deployment.

### 42.2 Data

Pipeline and admission logs give the time a risky configuration first appeared in a pull request or admission request, and when a compliant version replaced it. Six months before and after are compared.

### 42.3 Analysis

Median time to fix falls from 9 days (found after deployment) to 4 hours (rejected at admission, fixed before deployment). Most fixes now happen before anything runs.

### 42.4 Limits

The before period relied on weekly scans, so measured times include detection delay; teams also improved through training; one organisation.

### 42.5 Ethics

Data are aggregated by namespace; no individual developer is identified.

### 42.6 Reporting

A four-page report with method, results, limits and recommendations is shared internally and summarised for the regulator.

### Data quality

Before analysis, Elena checks that pipeline and admission timestamps use the same clock and time zone, and removes 11 records from a test namespace. She keeps the cleaning steps in a script with the analysis, so the results can be reproduced. A second engineer reruns the script and gets the same medians, which goes into the report as a reproducibility check. Elena also lists the fields she could not use, such as fix effort, which would make a useful follow-up study.

### Worked example

The study's most useful finding is unexpected: 40% of admission rejections occur in the first week of a new service. Solent adds a secure service template so new services start compliant, which reduces first-week rejections by half in the following quarter.

> **Synthetic case.** Data and results are synthetic.

### Errors and limits

Before-after comparisons cannot isolate one cause; describe other changes.

### Exercises

- **EX124 — Question.** What did the study ask? *Rubric:* 3 = did time to fix fall after enforcement; 2 = partial; 1 = none; 0 = none.
- **EX125 — Result.** What were the medians? *Rubric:* 3 = 9 days to 4 hours; 2 = partial; 1 = none; 0 = none.
- **EX126 — Unexpected finding.** What unexpected finding led to action? *Rubric:* 3 = 40% rejections in first week; template; 2 = partial; 1 = none; 0 = none.

### Synthesis

Applied studies show what controls change and where to improve next.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a real-style operations team; (2) apply course methods to live-style tasks under supervision; (3) reflect on professional practice.

### 43.1 Placement

Elena spends eight weeks embedded in Solent's platform team, joining on-call shadowing, change reviews and planning.

### 43.2 Change reviews

She reviews 40 infrastructure pull requests, commenting on security-relevant settings. Twelve comments lead to changes; she learns to phrase comments as questions with references.

### 43.3 Shadowing on-call

Elena observes alert handling and drafts runbook improvements, approved by the team.

### 43.4 Working with developers

A developer team asks for help moving a service to Restricted pod security. Elena pairs with them; the service is compliant in two days.

### 43.5 Professional lessons

Security engineers succeed by making the secure path easy: templates, clear messages, help when stuck.

### 43.6 Supervision

Rosa reviews Elena's work weekly; all production changes are made by team members.

### Reflection log

Each week Elena writes a short reflection: what she did, what she learned and what she would do differently. Reading them back at the end shows a shift from focusing on controls to focusing on how teams experience them. Rosa uses the reflections to plan Elena's final weeks, giving her more pairing with developers. The log also supplies material for the evidence dossier later in the course, since each entry links to the reviews and runbooks she worked on.

### Supervisor feedback

Rosa's final feedback praises Elena's review comments for offering fixes with references, and suggests she practise saying no to scope creep.

### Worked example

In week six, Elena notices a pull request adding a cloud role with wildcard storage permissions for a new analytics job. Her review comment proposes the specific actions and buckets needed, with a link to the least-privilege requirement; the author updates the role before merge.

> **Synthetic case.** Placement details are synthetic.

### Errors and limits

Reviewers who only block changes lose influence; offer the fix.

### Exercises

- **EX127 — Review outcome.** How many review comments led to changes? *Rubric:* 3 = 12 of 40 PRs commented; 2 = partial; 1 = none; 0 = none.
- **EX128 — Lesson.** What is the main professional lesson? *Rubric:* 3 = make secure path easy; 2 = partial; 1 = none; 0 = none.
- **EX129 — Wildcard role.** How was the wildcard role handled? *Rubric:* 3 = proposed specific actions and buckets; 2 = partial; 1 = none; 0 = none.

### Synthesis

Practice teaches how security works with teams, not around them.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define the capstone project scope; (2) plan design, implementation and verification; (3) identify risks; (4) agree success criteria.

### 44.1 Capstone choice

Elena's capstone is an automated "secure namespace" service: a request creates a namespace with default-deny network policies, Restricted pod security, workload identity binding, resource quotas and monitoring, all from reviewed templates.

### 44.2 Why

The applied study showed new services generate most rejections. A secure-by-default namespace removes that friction and closes gaps like the opening case's missing policies.

### 44.3 Scope

Templates, a small request workflow, verification tests and documentation. Out of scope: changes to existing namespaces.

### 44.4 Success criteria

New namespaces pass all chapter 30 verification tests at creation; creation takes under 10 minutes; developers rate the process at least 4 of 5.

### 44.5 Risks

Templates could become too rigid; the workflow could become a bottleneck; template errors would spread to every new namespace.

### 44.6 Mitigations

Template tests in the pipeline; staged release; a documented way to request variations.

### 44.7 Plan

Eight weeks: design (2), implementation (3), verification (2), documentation and handover (1).

### Stakeholder check

Before starting, Elena shows the plan to three developer teams who will use the service. They ask for a way to request larger quotas and for the service to create a starter alert dashboard. The quota request becomes part of scope; the dashboard is noted as a later improvement to keep the eight-week plan realistic. Elena also agrees with Rosa which platform engineer will own the service after handover, so design choices suit the people who will maintain it.

### Timeline buffer

The plan keeps one week of buffer inside the eight weeks for problems found in verification.

### Worked example

Dr Wagner asks how template errors will be caught before they spread. Elena adds a canary step: each template change first creates a test namespace and runs the verification suite before any real namespace uses it.

> **Synthetic case.** Capstone details are synthetic.

### Errors and limits

Capstones grow; protect scope with a written out-of-scope list.

### Exercises

- **EX130 — Capstone.** What is the capstone? *Rubric:* 3 = automated secure namespace service; 2 = partial; 1 = none; 0 = none.
- **EX131 — Criteria.** State the success criteria. *Rubric:* 3 = pass tests, under 10 min, rating ≥4; 2 = two; 1 = one; 0 = none.
- **EX132 — Canary.** What did the canary step add? *Rubric:* 3 = test namespace verification before use; 2 = partial; 1 = none; 0 = none.

### Synthesis

A clear scope and criteria set up the capstone for success.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) submit the capstone design for independent review; (2) respond to findings; (3) revise; (4) record decisions.

### 45.1 Reviewers

A platform engineer from another team and a security architect from a partner university review the design package.

### 45.2 Findings

The reviewers raise four points: quotas may be too small for data jobs; the workflow's own permissions are broad (it can create any namespace); monitoring setup assumes one log destination; templates lack versioning for rollback.

### 45.3 Responses

Quotas become size options; the workflow's identity is limited to creating namespaces with an approved label prefix and applying templates; log destination is a parameter; templates are versioned and namespaces record which version created them.

### 45.4 Disagreement

One reviewer suggests separate clusters per team. Elena explains the chapter 26 decision and criteria; the reviewer accepts, noting it as a future option.

### 45.5 Record

A review log captures each finding, response and change.

### 45.6 Learning

Independent review catches issues the designer cannot see.

### Second round

After revisions, Elena sends the updated package back to both reviewers. They confirm the changes address their findings, and one adds a minor note about naming conventions for the label prefix, which Elena adopts. The two-round process takes three weeks but avoids rework later in implementation, when changes would cost more. Elena notes in her dossier that the review found a serious permission issue no internal test had covered.

### Reviewer selection

Reviewers are chosen from outside the project so they bring fresh assumptions, and they receive the requirements and threat analysis with the design.

### Worked example

The workflow permission finding is the most important: as first designed, a bug could have let the workflow modify system namespaces. The fix narrows its role, and a verification test confirms it cannot touch namespaces without the prefix.

> **Synthetic case.** Review details are synthetic.

### Errors and limits

Reviews only help if findings are acted on and verified.

### Exercises

- **EX133 — Four findings.** List the four findings. *Rubric:* 3 = quotas, workflow permissions, log destination, template versioning; 2 = three; 1 = one; 0 = none.
- **EX134 — Most important.** Which finding mattered most and why? *Rubric:* 3 = workflow permissions; could modify system namespaces; 2 = partial; 1 = none; 0 = none.
- **EX135 — Disagreement.** How was the disagreement handled? *Rubric:* 3 = explained decision criteria; noted future option; 2 = partial; 1 = none; 0 = none.

### Synthesis

Independent review strengthens designs when findings are verified.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) implement and verify the secure namespace service; (2) run it in staging and production; (3) measure against success criteria; (4) document and hand over.

### 46.1 Implementation

Templates are written as versioned manifests; the request workflow is a reviewed pull request to a namespaces repository, processed by the GitOps controller with a narrowly scoped identity. A canary namespace verifies each template version.

### 46.2 Verification

Each new namespace automatically runs the chapter 30 tests: privileged pod rejected, unsigned image rejected, web-to-db connection blocked, workload identity limited, quotas applied, alerts flowing. Results are attached to the request.

### 46.3 Staging trial

Twelve namespaces are created in staging over two weeks; all pass verification. One template error, a missing DNS egress rule, is caught by the canary before any real namespace uses it.

### 46.4 Production

Eight new production namespaces are created in the following month, all passing at creation. Median creation time is 6 minutes.

### 46.5 Developer feedback

Developers rate the process 4.4 of 5; the main request is clearer documentation on quota options.

### 46.6 Handover

The platform team takes ownership with runbooks, template tests and a maintenance schedule.

### 46.7 Criteria check

All three success criteria are met.

### Documentation

The service has a short user guide: how to request a namespace, what is included, how to choose quota sizes and how to request a variation. Following developer feedback, quota options are explained with examples of typical workloads. The platform team's guide covers template changes, canary checks and how to roll back a template version.

### Ownership

The platform team now owns the service.

### Worked example

Rosa compares the first eight production namespaces with the previous eight created by hand: the hand-made ones averaged 2.5 missing controls at creation, the new ones none. The comparison goes into the evidence dossier as the clearest result of the capstone.

> **Synthetic case.** Namespaces and figures are synthetic.

### Errors and limits

Early success can fade if templates are not maintained; schedule reviews.

### Exercises

- **EX136 — Canary catch.** What did the canary catch? *Rubric:* 3 = missing DNS egress rule; 2 = partial; 1 = none; 0 = none.
- **EX137 — Results.** What were creation time and rating? *Rubric:* 3 = 6 minutes; 4.4/5; 2 = partial; 1 = none; 0 = none.
- **EX138 — Comparison.** How did new namespaces compare with hand-made ones? *Rubric:* 3 = 0 vs 2.5 missing controls; 2 = partial; 1 = none; 0 = none.

### Synthesis

Secure defaults, verified at creation, prevent gaps rather than finding them later.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) plan and run a controlled failure and recovery trial; (2) test controls and recovery under realistic stress; (3) measure recovery; (4) learn from results.

### 47.1 Trial plan

With approval from Solent's operations director, Elena and the platform team run a staged trial in a production-like environment: simulate a leaked workload credential, a deleted network policy and an unavailable policy engine, then measure detection and recovery.

### 47.2 Safety

The trial uses a dedicated environment with synthetic meter data. Abort criteria and a rollback plan are agreed; observers are named.

### 47.3 Leaked credential scenario

A synthetic credential event is injected. Detection takes 4 minutes; the credential is revoked in 9 minutes. Because workload identity tokens expire within an hour, the scenario also confirms that no long-lived key exists to revoke.

### 47.4 Deleted policy scenario

A network policy is deleted. GitOps restores it in 3 minutes; a drift alert fires in 2.

### 47.5 Engine failure scenario

All policy engine replicas are stopped. Deployments fail closed; an alert fires in 1 minute; recovery takes 6 minutes following the runbook.

### 47.6 Results

All objectives met; two runbook steps clarified.

### Debrief

The trial ends with a debrief within 24 hours: what went well, what surprised the team and what changes follow. Findings are tracked like incidents, with owners and dates. The two runbook clarifications are made the same week, and the fail-open rule is added to on-call training. The team agrees to run a similar trial each year with new scenarios chosen from the threat register.

### Approval

The trial plan was approved in writing a week ahead.

### Worked example

An observer notes that during the engine failure, an engineer considered switching admission to fail open to unblock a deployment. The runbook now states explicitly that fail-open in production requires the platform lead's approval and an incident record.

> **Synthetic case.** Trial and timings are synthetic.

### Errors and limits

Trials are only as realistic as their scenarios; vary them each year.

### Exercises

- **EX139 — Safety measures.** How was the trial kept safe? *Rubric:* 3 = dedicated environment, synthetic data, abort criteria, observers; 2 = two; 1 = one; 0 = none.
- **EX140 — Credential times.** What were detection and revocation times? *Rubric:* 3 = 4 and 9 minutes; 2 = partial; 1 = none; 0 = none.
- **EX141 — Runbook change.** What runbook change followed? *Rubric:* 3 = fail-open needs approval and incident; 2 = partial; 1 = none; 0 = none.

### Synthesis

Controlled trials prove recovery works under stress.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) compile an evidence dossier for the engineering work; (2) trace requirements to evidence; (3) include limitations; (4) prepare it for assessment and audit.

### 48.1 Structure

The dossier follows the requirement trace: for each of R1 to R6 and the capstone criteria, the design element, verification evidence, operational evidence and remaining risk.

### 48.2 Evidence types

Test results with dates and policy versions, configuration queries, measurement reports (coverage, latency, applied study), trial results, review logs, survey results and decision records.

### 48.3 Integrity

Evidence files are stored in a repository with a manifest of SHA-256 hashes so assessors can confirm nothing changed after submission.

### 48.4 Mapping

A table maps evidence to CSA CCM v4 domains and to the Pod Security Standards and CIS Benchmark sections used.

### 48.5 Limitations

One organisation; synthetic data in trials; short post-rollout period; some controls depend on provider features that could change.

### 48.6 Readability

A two-page summary leads, with links into detail.

### Failures included

The dossier includes the failures found along the way: the Baseline label error, the alert severity mistake, the canary-caught template error and the workflow permission issue found in review. Each shows how it was found and fixed. Assessors value these because they show the verification process works. Elena also includes a short section listing evidence she could not obtain, such as long-term incident data, and why.

### Assessor access

Assessors receive read-only access to the evidence repository and the manifest, so they can check any file against its hash themselves. Elena walks one assessor through the trace for R2 in a short meeting.

### Worked example

An assessor test-reads the dossier and asks for evidence that exceptions expire. Elena adds the exception log extract and a test showing an expired exception causing rejection, closing the gap.

> **Synthetic case.** Dossier contents are synthetic.

### Errors and limits

A dossier that only shows successes is less credible; include failures and fixes.

### Exercises

- **EX142 — Per-requirement content.** What does the dossier show for each requirement? *Rubric:* 3 = design, verification, operation, remaining risk; 2 = three; 1 = one; 0 = none.
- **EX143 — Integrity.** How is dossier integrity protected? *Rubric:* 3 = SHA-256 manifest; 2 = partial; 1 = none; 0 = none.
- **EX144 — Added evidence.** What evidence did the assessor request? *Rubric:* 3 = exceptions expire; 2 = partial; 1 = none; 0 = none.

### Synthesis

Trace every claim to evidence and show the failures too.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write the engineering thesis; (2) present problem, design, implementation, verification and evaluation; (3) discuss contributions and limits; (4) propose future work.

### 49.1 Problem

Configuration and credential weaknesses in a containerised energy-data platform, shown by the leaked key and missing network policies.

### 49.2 Approach

Requirements from risks and standards; layered architecture; implemented controls (workload identity, default-deny networking, Restricted pod security, signed images, guardrails, drift detection); secure namespace service.

### 49.3 Evaluation

Coverage rose from 62% to 100% of production namespaces; long-lived workload keys from 23 to 0; time to fix risky configurations fell from 9 days to 4 hours; admission overhead about 20 ms median; trial objectives met.

### 49.4 Contributions

An engineering method combining standards, traceability and verification for small platform teams; the secure namespace service; measurement scripts reusable by others.

### 49.5 Limits

Single organisation, short observation, synthetic trial data, dependence on provider features.

### 49.6 Future work

Extend the namespace service to cloud accounts; measure developer productivity effects; study multi-organisation adoption.

### Writing process

Elena writes the thesis chapter by chapter alongside the work, reusing design notes, decision records and test reports rather than writing from memory at the end. Each chapter is reviewed by Dr Wagner within a week. This keeps the thesis accurate and reduces the final writing load. The final document is about 60 pages plus appendices containing the dossier summary, the requirement trace and the scripts. A short reading guide at the start tells practitioners which chapters to read if they only want the method or the results.

### Abstract

The abstract states the problem, method, main results with figures and limits in 250 words.

### Final check

Every figure is checked against its source file before submission.

### Worked example

Dr Wagner's main comment on the draft is that the evaluation chapter lists results but not their uncertainty. Elena adds sample sizes and notes where figures come from single measurements.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Engineering theses must show evidence, not only describe systems.

### Exercises

- **EX145 — Coverage result.** How did coverage change? *Rubric:* 3 = 62% to 100%; 2 = partial; 1 = none; 0 = none.
- **EX146 — Contributions.** List the contributions. *Rubric:* 3 = method, namespace service, scripts; 2 = two; 1 = one; 0 = none.
- **EX147 — Draft comment.** What did Dr Wagner ask to add? *Rubric:* 3 = uncertainty, sample sizes; 2 = partial; 1 = none; 0 = none.

### Synthesis

The thesis connects problem, design and evidence into one argument.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend the engineering thesis before a panel; (2) answer technical and professional questions; (3) reflect on learning; (4) plan next steps.

### 50.1 The panel

Dr Wagner, Rosa Delgado and an external examiner from industry.

### 50.2 Technical questions

Why fail closed? Because production safety outweighs deployment convenience, backed by a reliable engine. Why namespaces rather than clusters per service? The scored decision record. How do controls handle a provider outage? Rebuild and degradation plans.

### 50.3 Professional questions

How did you handle developer resistance? Through exceptions with expiry, clear messages and making the secure path easy. What would you do differently? Involve developers earlier in requirements.

### 50.4 Reflection

Elena writes that the most valuable skill was turning standards into testable requirements and then into evidence.

### 50.5 Outcome

The thesis passes; Solent offers Elena a platform security engineer role.

### 50.6 Next steps

Lead the extension of secure defaults to cloud accounts, mentor next year's student.

### Mentoring

As part of her new role, Elena prepares a short guide for next year's student: how to find data, which stakeholders to meet first and how to use synthetic data for labs. The guide shows the project's methods becoming part of Solent's practice, the outcome Dr Wagner hoped for. She also hands over her lab scripts with tests, so next year's student starts from working tools rather than from scratch.

### Closing reflection

Elena closes by thanking the platform team, noting that every control in the thesis exists because they run it daily.

### Worked example

The external examiner asks whether the approach would work at a much larger company. Elena answers that the method would, but the tooling would need more automation and the exception process would need delegation; she cites the Borg and Kubernetes experience (Burns et al., 2016) of declarative, reconciled configuration at scale as supporting the core idea.

> **Synthetic case.** Panel and outcomes are synthetic.

### Errors and limits

Answer within the evidence; say where it runs out.

### Exercises

- **EX148 — Fail closed defence.** How did Elena justify fail closed? *Rubric:* 3 = safety over convenience, reliable engine; 2 = partial; 1 = none; 0 = none.
- **EX149 — Do differently.** What would she do differently? *Rubric:* 3 = involve developers earlier; 2 = partial; 1 = none; 0 = none.
- **EX150 — Scale answer.** How did she answer the scale question? *Rubric:* 3 = method scales; more automation, delegation; 2 = partial; 1 = none; 0 = none.

### Synthesis

Defend with evidence and know where it ends.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Elena Petrova, Rosa Delgado, Dr Felix Wagner, Brackenridge Institute of Technology, Solent Energy Co-op and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The rate at which the number of pods changes.

**EX002.** By integrating exposure over time, such as reachable services multiplied by hours.

**EX003.** One key for 5 hours on 3 buckets: 15 bucket-hours.

**EX004.** Allowed if some allow rule matches and no deny rule matches.

**EX005.** The explicit deny on storage:Delete* for readings/* overrides allows.

**EX006.** No allow rule matched, so default deny applied.

**EX007.** About 10 ms at roughly 200 km per ms each way.

**EX008.** The failure of a single facility.

**EX009.** All ingest pods were in one zone; she proposed three zones.

**EX010.** Configuration is structured data that programs can check at scale.

**EX011.** Labs run anywhere and are easy to review.

**EX012.** Six of 22 pods lacked resource limits.

**EX013.** Context, problem, options, decision, consequences, open questions.

**EX014.** That default-deny policies would block undocumented traffic during rollout.

**EX015.** A ranked list with risk reduced and effort for each fix.

**EX016.** It roughly doubles.

**EX017.** About 2.2 million readings.

**EX018.** A long queue would also delay tamper alerts.

**EX019.** Mean 13.2, median 6.5, p95 40.9 minutes.

**EX020.** About 97%.

**EX021.** Alerts routed through an email list checked only in working hours.

**EX022.** VMs are isolated by a hypervisor; containers share the kernel and use kernel features.

**EX023.** Kernel control groups (cgroups).

**EX024.** A memory limit and a separate node pool for reports.

**EX025.** As "not set", the least safe interpretation.

**EX026.** The standard library has no YAML parser.

**EX027.** Container-level settings overriding pod-level in the wrong direction.

**EX028.** The 80,000 households whose readings are processed.

**EX029.** When people are home and their habits.

**EX030.** She reported it; it was deleted.

**EX031.** Every pod can reach every other pod.

**EX032.** Cloud security groups, cluster network policies and application authentication.

**EX033.** 14 flows, only 4 documented; two came from a leftover debugging tool.

**EX034.** NET_ADMIN and SYS_ADMIN.

**EX035.** It grants broad administrative power close to full root.

**EX036.** By setting file ownership when the image is built.

**EX037.** A leak of one store reveals less.

**EX038.** They are copied to a separate account.

**EX039.** Meter IDs in debug-level query logging.

**EX040.** Hard-coded secrets, admin by default, unrestricted IP addresses, HTTP, weak cryptography.

**EX041.** What else a change could affect.

**EX042.** One fix reached three projects.

**EX043.** Bills and grid planning depend on accurate readings.

**EX044.** Prevent, detect, limit and recover.

**EX045.** Workloads and their configuration.

**EX046.** It arises from how parts interact, not any single control.

**EX047.** Old clusters and buckets left running can expose data.

**EX048.** Five requirements had no verification method.

**EX049.** desired = ceil(current × metric ÷ target), bounded by min and max.

**EX050.** It would want 27 but was capped at 10.

**EX051.** It reverts manual edits back to the declared configuration.

**EX052.** Separate accounts and organisation policies blocking public storage and restricting regions.

**EX053.** Guardrails prevent mistake classes everywhere; gates stop specific changes.

**EX054.** One credential could deploy to both test and production.

**EX055.** The earlier layer still contains the file.

**EX056.** CLOUD_ACCESS_KEY entropy 4.50 likely secret; EXAMPLE_TOKEN 0.00 placeholder.

**EX057.** Only images built and signed by the pipeline can run.

**EX058.** Self-service creates many configuration changes to secure.

**EX059.** No long-lived credentials, default-deny networking, Restricted pod security, signed images, measured detection.

**EX060.** About 30% of the platform team for two quarters.

**EX061.** For example, "pods in production namespaces must not run as root".

**EX062.** Workloads get cloud credentials only via workload identity with lifetimes under one hour.

**EX063.** A two-month exception that expires automatically while services change.

**EX064.** Readings, customer details, aggregated statistics, logs and images.

**EX065.** Authenticated, authorised, encrypted and logged.

**EX066.** Read-only access to a view of billing-period totals.

**EX067.** A public bucket or a leaked key.

**EX068.** An expired certificate, a blocking policy change, an upgrade eviction or a bad lifecycle rule.

**EX069.** Excepted privileged workloads run on a dedicated node pool.

**EX070.** 12 of 12 before; 4 of 12 after.

**EX071.** A flaw in web cannot reach the database directly.

**EX072.** Metrics scraping, found through denied-connection logs.

**EX073.** Build, scan, sign, store, admit, deploy and observe.

**EX074.** The pipeline never holds cluster credentials.

**EX075.** How emergencies work and who can change the controller.

**EX076.** One shared cluster, clusters per environment and tier, one cluster per service.

**EX077.** Clusters per sensitivity tier with dedicated node pools.

**EX078.** About 8% of spend, and audits cover one small cluster.

**EX079.** Fail closed, with a highly available engine.

**EX080.** An organisation policy disallows creating them.

**EX081.** Deployments continued with one replica down; with all down they blocked and alerted.

**EX082.** 23 keys; 9 unused in 90 days.

**EX083.** To detect breakage before an irreversible step.

**EX084.** With a short-lived identity attached to its VM.

**EX085.** 10 of 16, 62%.

**EX086.** Default-deny network policy, Restricted pod security and image signature.

**EX087.** Images came from an older pipeline that did not sign.

**EX088.** Synthetic workloads each violating one rule.

**EX089.** web to db fails and web to api succeeds.

**EX090.** The namespace label set Baseline instead of Restricted.

**EX091.** So the image that was verified is exactly what runs.

**EX092.** It showed unsigned images and old pipelines without blocking.

**EX093.** Mirrored after checking its digest and signed with a third-party key.

**EX094.** Deployments and running services depend on them.

**EX095.** At 30 and 7 days before expiry.

**EX096.** Rotation took 25 minutes, reduced to 8 after scripting.

**EX097.** Ingesting readings, billing accuracy and tamper alerts.

**EX098.** Declarative code and signed images make clean rebuilds repeatable and trustworthy.

**EX099.** 6 hours, then 2.5 hours with pre-approved templates.

**EX100.** Public access changes, new keys, policy engine disabled and privileged pods admitted.

**EX101.** In a separate account for one year.

**EX102.** A 31-minute delay because severity was set to low.

**EX103.** It hides that someone made a manual change.

**EX104.** Request, review, approval, labelled implementation, expiry reminder, renewal or removal.

**EX105.** The weekly report compares declared and running state, revealing missing policies.

**EX106.** 265.0 ms to 284.5 ms.

**EX107.** Occasional cache misses on signature lookups.

**EX108.** The digest identifies exact image content.

**EX109.** Overnight alerts, exception expiries and the drift report.

**EX110.** Admission behaviour can change between versions.

**EX111.** By removing the underlying need, a root filesystem log path.

**EX112.** Verification: built it right; validation: built the right thing.

**EX113.** 70% found messages clear; complaints were about exception request time.

**EX114.** More evidence on key rotation.

**EX115.** It reduces custom code to maintain.

**EX116.** Controls defined in standard Kubernetes terms.

**EX117.** A new engineer added a policy in two days and suggested three doc fixes.

**EX118.** meterhub image digest, billing replicas and missing billing network policy.

**EX119.** The autoscaler likely changed it.

**EX120.** The namespace was recreated during troubleshooting.

**EX121.** Six months of findings showed one scanner found everything the other did and more.

**EX122.** By risk reduced per engineer-day.

**EX123.** It found four security-relevant drifts outside GitOps.

**EX124.** Whether time from proposing to fixing a risky configuration fell.

**EX125.** 9 days before; 4 hours after.

**EX126.** 40% of rejections came in a service's first week; a secure template was added.

**EX127.** Twelve comments led to changes across 40 reviews.

**EX128.** Make the secure path easy.

**EX129.** Elena proposed specific actions and buckets and the author updated it.

**EX130.** An automated secure namespace service.

**EX131.** Pass verification at creation, under 10 minutes, developer rating at least 4/5.

**EX132.** Each template change is verified on a test namespace first.

**EX133.** Small quotas, broad workflow permissions, single log destination, no template versioning.

**EX134.** Workflow permissions, because a bug could modify system namespaces.

**EX135.** Elena explained the earlier decision; the reviewer accepted it as a future option.

**EX136.** A missing DNS egress rule.

**EX137.** Median 6 minutes; rating 4.4 of 5.

**EX138.** None missing versus an average of 2.5 missing controls.

**EX139.** Dedicated environment, synthetic data, abort criteria and named observers.

**EX140.** Detection 4 minutes; revocation 9 minutes.

**EX141.** Fail-open in production needs the platform lead's approval and an incident record.

**EX142.** Design element, verification evidence, operational evidence and remaining risk.

**EX143.** With a manifest of SHA-256 hashes.

**EX144.** Evidence that exceptions expire.

**EX145.** From 62% to 100%.

**EX146.** The method, the secure namespace service and reusable measurement scripts.

**EX147.** Uncertainty and sample sizes for results.

**EX148.** Production safety outweighs convenience, supported by a reliable engine.

**EX149.** Involve developers earlier in requirements.

**EX150.** The method scales; tooling needs automation and exceptions need delegation.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Amazon Web Services. (n.d.). *Shared responsibility model*. <https://aws.amazon.com/compliance/shared-responsibility-model/>
- Armbrust, M., Fox, A., Griffith, R., Joseph, A. D., Katz, R., Konwinski, A., Lee, G., Patterson, D., Rabkin, A., Stoica, I., & Zaharia, M. (2010). A view of cloud computing. *Communications of the ACM*, 53(4), 50–58. <https://doi.org/10.1145/1721654.1721672>
- Burns, B., Grant, B., Oppenheimer, D., Brewer, E., & Wilkes, J. (2016). Borg, Omega, and Kubernetes. *Communications of the ACM*, 59(5), 50–57. <https://doi.org/10.1145/2890784>
- Center for Internet Security. (n.d.). *CIS Benchmarks*. <https://www.cisecurity.org/cis-benchmarks>
- Cloud Security Alliance. (2021). *Cloud Controls Matrix (CCM) v4*. <https://cloudsecurityalliance.org/research/cloud-controls-matrix>
- Google Cloud. (n.d.). *Shared responsibilities and shared fate on Google Cloud*. <https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate>
- Hu, V. C., Iorga, M., Bao, W., Li, A., Li, Q., & Gouglidis, A. (2020). *General access control guidance for cloud systems* (NIST SP 800-210). NIST. <https://doi.org/10.6028/NIST.SP.800-210>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Kubernetes Authors. (n.d.). *Pod Security Standards*. <https://kubernetes.io/docs/concepts/security/pod-security-standards/>
- Kubernetes Authors. (n.d.). *Using RBAC authorization*. <https://kubernetes.io/docs/reference/access-authn-authz/rbac/>
- Kubernetes Authors. (n.d.). *Network policies*. <https://kubernetes.io/docs/concepts/services-networking/network-policies/>
- Kubernetes Authors. (n.d.). *Good practices for Kubernetes Secrets*. <https://kubernetes.io/docs/concepts/security/secrets-good-practices/>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Mell, P., & Grance, T. (2011). *The NIST definition of cloud computing* (NIST SP 800-145). NIST. <https://doi.org/10.6028/NIST.SP.800-145>
- Microsoft. (n.d.). *Shared responsibility in the cloud*. <https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility>
- Rahman, A., Parnin, C., & Williams, L. (2019). The seven sins: Security smells in infrastructure as code scripts. *41st International Conference on Software Engineering (ICSE)*, 164–175. <https://doi.org/10.1109/ICSE.2019.00033>
- Ristenpart, T., Tromer, E., Shacham, H., & Savage, S. (2009). Hey, you, get off of my cloud: Exploring information leakage in third-party compute clouds. *16th ACM Conference on Computer and Communications Security (CCS '09)*, 199–212. <https://doi.org/10.1145/1653662.1653687>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Sandhu, R. S., Coyne, E. J., Feinstein, H. L., & Youman, C. E. (1996). Role-based access control models. *Computer*, 29(2), 38–47. <https://doi.org/10.1109/2.485845>
- Shu, R., Gu, X., & Enck, W. (2017). A study of security vulnerabilities on Docker Hub. *7th ACM Conference on Data and Application Security and Privacy (CODASPY '17)*, 269–280. <https://doi.org/10.1145/3029806.3029832>
- Souppaya, M., Morello, J., & Scarfone, K. (2017). *Application container security guide* (NIST SP 800-190). NIST. <https://doi.org/10.6028/NIST.SP.800-190>
- Verma, A., Pedrosa, L., Korupolu, M., Oppenheimer, D., Tune, E., & Wilkes, J. (2015). Large-scale cluster management at Google with Borg. *10th European Conference on Computer Systems (EuroSys '15)*, 1–17. <https://doi.org/10.1145/2741948.2741964>
