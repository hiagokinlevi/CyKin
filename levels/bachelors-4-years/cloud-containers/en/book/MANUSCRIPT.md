# Cloud and Container Security: Bachelor's Course

- Language: English (`en`); course 105, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; Nine offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: bachelor's students learning to review, design, verify and operate security for cloud accounts and containerised platforms.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only cloud accounts, clusters and workloads you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Misconfigurations are taught from the defender's side using synthetic configurations, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one student working with a university cloud team after a container registry was found allowing anonymous pulls of an image with a database connection string, while audit logging was off in one account. They move from foundations (reasoning, computing, programming, writing, networks, data, identity, privacy, evidence, architecture and cryptography) through research methods, system models, registry and benchmark reviews, controls, verification, failure analysis and operations, to labs, studies, community practice and a posture-report capstone. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Samuel Osei** | Bachelor's student | Invented |
| **Dr Clara Jensen** | Academic supervisor | Invented |
| **Tom Becker** | University cloud team lead | Invented |
| **Westmere University** | Fictional university running StudyHub | Invented |
| **Harbourside Youth Trust** | Fictional charity in the community placement | Invented |

### Core sources

NIST [SP 800-145](https://doi.org/10.6028/NIST.SP.800-145), [SP 800-210](https://doi.org/10.6028/NIST.SP.800-210), [SP 800-190](https://doi.org/10.6028/NIST.SP.800-190) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); CSA [Cloud Controls Matrix v4](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); the [AWS](https://aws.amazon.com/compliance/shared-responsibility-model/), [Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) and [Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) shared responsibility pages; Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) use precise reasoning to state and check claims about cloud systems; (2) distinguish necessary and sufficient conditions; (3) use counterexamples; (4) set up the course case.

### 1.1 The opening case

Samuel Osei is a bachelor's student at the fictional Westmere University. His final-year project is with the university's own cloud team, led by Tom Becker, and supervised by Dr Clara Jensen from the computing department. Westmere runs StudyHub, its student services platform, as containers on a managed Kubernetes service. Last term an internal review found that the container registry allowed anonymous pulls of two repositories. One image, records-api, contained a connection string for the student records test database. The test database held synthetic records only, and no unusual access was logged, but nobody could say how long the registry had been open, because audit logging was off in one account.

### 1.2 Precise claims

"StudyHub is secure" cannot be checked. "No registry repository allows anonymous pull" can be checked by listing repositories and their settings. The course trains Samuel to turn vague worries into precise, checkable statements, because only checkable statements lead to fixes and evidence.

Section one point two develops mathematical reasoning with a Westmere University note Samuel Osei can demo offline.

Under section one point two, Tom Becker expects mathematical claims to carry owners and dates.

Section one point two treats the opening case precise as testable only when evidence and ticket IDs are recorded.

### 1.3 Necessary and sufficient

Turning off anonymous pull is necessary to stop outsiders downloading images, but not sufficient to protect secrets: anyone with internal access could still read a secret baked into an image. Removing secrets from images and using a secret manager is also needed. Mixing up necessary and sufficient conditions leads to fixes that feel complete but are not.

Section one point three develops mathematical reasoning with a Westmere University note Samuel Osei can demo offline.

Under section one point three, Tom Becker expects mathematical claims to carry owners and dates.

### 1.4 Counterexamples

One counterexample disproves a universal claim. The claim "all our images are private" was disproved by a single anonymous pull test on records-api. Engineers look for counterexamples deliberately rather than waiting for them to appear in an incident.

Section one point four develops mathematical reasoning with a Westmere University note Samuel Osei can demo offline.

Under section one point four, Tom Becker expects mathematical claims to carry owners and dates.

Section one point four treats the opening case precise as testable only when evidence and ticket IDs are recorded.

### 1.5 Quantities and units

Exposure is measured in days and resources; costs in money and engineer-hours. Keeping units explicit avoids comparing unlike things.

Section one point five develops mathematical reasoning with a Westmere University note Samuel Osei can demo offline.

Under section one point five, Tom Becker expects mathematical claims to carry owners and dates.

Section one point five treats the opening case precise as testable only when evidence and ticket IDs are recorded.

For section one point five, Westmere University will not accept mathematical work without a written trail.

### 1.6 Logical structure

Claims are combined with and, or and not; access policies, later in the course, follow the same logic.

Section one point six develops mathematical reasoning with a Westmere University note Samuel Osei can demo offline.

Under section one point six, Tom Becker expects mathematical claims to carry owners and dates.

Section one point six treats the opening case precise as testable only when evidence and ticket IDs are recorded.

For section one point six, Westmere University will not accept mathematical work without a written trail.

### Worked example

Samuel writes the review's findings as four precise statements: two repositories allowed anonymous pull; one image contained a database connection string; audit logging was off in one account; therefore the duration of exposure is unknown. Tom notes that the last statement follows logically from the third, and that fixing logging is necessary before any future exposure can be measured.

> **Synthetic case.** Westmere University, StudyHub, people and events are synthetic.

### Errors and limits

Precise statements can still rest on wrong data; check the data source too.

### Exercises

- **EX001 — Checkable claim.** Rewrite "StudyHub is secure" as a checkable claim. *Rubric:* 3 = e.g. no repo allows anonymous pull; 2 = partial; 1 = none; 0 = none.
- **EX002 — Not sufficient.** Why is disabling anonymous pull not sufficient? *Rubric:* 3 = internal users could still read baked-in secret; 2 = partial; 1 = none; 0 = none.
- **EX003 — Unknown duration.** Why was exposure duration unknown? *Rubric:* 3 = audit logging off; 2 = partial; 1 = none; 0 = none.

### Synthesis

Precise, checkable statements turn worries into work.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the layers of a cloud-hosted application; (2) explain virtual machines, containers and managed services; (3) identify who manages each layer; (4) relate layers to the opening case.

### 2.1 Layers

StudyHub runs on physical servers in the provider's data centres, virtualised into machines that form the Kubernetes worker nodes. Containers run on those nodes, each packaged from an image stored in a registry. Managed services provide the database, storage and identity.

Section two point one develops computing systems with a Westmere University note Samuel Osei can demo offline.

Under section two point one, Tom Becker expects computing claims to carry owners and dates.

Section two point one treats layers service models images as testable only when evidence and ticket IDs are recorded.

### 2.2 Service models

NIST SP 800-145 (Mell & Grance, 2011) defines infrastructure, platform and software as a service. Managed Kubernetes sits between infrastructure and platform: the provider runs the control plane; Westmere runs the workloads and their configuration.

Section two point two develops computing systems with a Westmere University note Samuel Osei can demo offline.

Under section two point two, Tom Becker expects computing claims to carry owners and dates.

Section two point two treats layers service models images as testable only when evidence and ticket IDs are recorded.

### 2.3 Images and registries

An image is a stack of file-system layers plus metadata. The registry stores images and controls who may pull or push them. Whatever goes into a layer stays there, which is why a connection string in records-api remained readable even after the application stopped using it.

Section two point three develops computing systems with a Westmere University note Samuel Osei can demo offline.

Under section two point three, Tom Becker expects computing claims to carry owners and dates.

Section two point three treats layers service models images as testable only when evidence and ticket IDs are recorded.

### 2.4 Shared responsibility

The AWS, Microsoft and Google shared responsibility pages agree that customers configure access to registries, storage and identities. The open registry was on Westmere's side.

Section two point four develops computing systems with a Westmere University note Samuel Osei can demo offline.

Under section two point four, Tom Becker expects computing claims to carry owners and dates.

Section two point four treats layers service models images as testable only when evidence and ticket IDs are recorded.

For section two point four, Westmere University will not accept computing work without a written trail.

### 2.5 Managed services

Using a managed database removes patching work but leaves access rules, backups and encryption choices to the customer.

Section two point five develops computing systems with a Westmere University note Samuel Osei can demo offline.

Under section two point five, Tom Becker expects computing claims to carry owners and dates.

Section two point five treats layers service models images as testable only when evidence and ticket IDs are recorded.

For section two point five, Westmere University will not accept computing work without a written trail.

### 2.6 Mapping the case

Samuel draws StudyHub's layers and marks who manages each, then marks where the opening findings sat: registry settings, image content and account logging, all customer-managed.

Section two point six develops computing systems with a Westmere University note Samuel Osei can demo offline.

Under section two point six, Tom Becker expects computing claims to carry owners and dates.

Section two point six treats layers service models images as testable only when evidence and ticket IDs are recorded.

For section two point six, Westmere University will not accept computing work without a written trail.

### Containers versus virtual machines

A virtual machine includes a whole operating system, while a container shares the node's kernel and packages only the application and its libraries. Containers start quickly and pack densely, which suits StudyHub's many small services, but their isolation depends on kernel features and careful settings.

### Worked example

The layer drawing surprises some university managers, who assumed the cloud provider handled registry security. Tom uses it in a briefing to explain why Westmere's cloud team must own these settings.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

Responsibility boundaries differ between services; check each service's documentation.

### Exercises

- **EX004 — Service models.** Name the three NIST service models. *Rubric:* 3 = IaaS, PaaS, SaaS; 2 = two; 1 = one; 0 = none.
- **EX005 — Layer persistence.** Why did the connection string remain readable? *Rubric:* 3 = stays in image layer; 2 = partial; 1 = none; 0 = none.
- **EX006 — Briefing use.** How did the drawing help managers? *Rubric:* 3 = showed customer owns registry settings; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know the layers and who manages each.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write small Python programs to read and check configuration data; (2) use variables, conditions, loops and functions; (3) test with synthetic data; (4) produce clear output.

### 3.1 Why code

The cloud team manages hundreds of resources. Reading each one by hand is slow and error-prone; a short program can check every resource the same way every time.

Section three point one develops programming with a Westmere University note Samuel Osei can demo offline.

Under section three point one, Tom Becker expects programming claims to carry owners and dates.

Section three point one treats why code basics functions as testable only when evidence and ticket IDs are recorded.

For section three point one, Westmere University will not accept programming work without a written trail.

### 3.2 Basics

Variables hold values; lists hold many items; dictionaries map names to settings. A loop visits each repository; an if statement checks a setting; print shows the result.

Section three point two develops programming with a Westmere University note Samuel Osei can demo offline.

Under section three point two, Tom Becker expects programming claims to carry owners and dates.

Section three point two treats why code basics functions as testable only when evidence and ticket IDs are recorded.

For section three point two, Westmere University will not accept programming work without a written trail.

### 3.3 Functions

A function such as check_repo(repo) returns a list of problems. Functions make programs easier to test and reuse.

Section three point three develops programming with a Westmere University note Samuel Osei can demo offline.

Under section three point three, Tom Becker expects programming claims to carry owners and dates.

Section three point three treats why code basics functions as testable only when evidence and ticket IDs are recorded.

For section three point three, Westmere University will not accept programming work without a written trail.

### 3.4 Synthetic data

Samuel writes his first programs against a small, made-up list of repositories, so mistakes cannot affect real systems and anyone can rerun them.

Section three point four develops programming with a Westmere University note Samuel Osei can demo offline.

Under section three point four, Tom Becker expects programming claims to carry owners and dates.

Section three point four treats why code basics functions as testable only when evidence and ticket IDs are recorded.

For section three point four, Westmere University will not accept programming work without a written trail.

### 3.5 Clear output

Each line names the resource and the problem in plain words, so non-programmers can act.

Section three point five develops programming with a Westmere University note Samuel Osei can demo offline.

Under section three point five, Tom Becker expects programming claims to carry owners and dates.

Section three point five treats why code basics functions as testable only when evidence and ticket IDs are recorded.

For section three point five, Westmere University will not accept programming work without a written trail.

Section three point five fails closed if programming evidence is missing rather than guessing.

### 3.6 Standard library

Labs use only Python's standard library, so they run on any machine and are easy to read.

Section three point six develops programming with a Westmere University note Samuel Osei can demo offline.

Under section three point six, Tom Becker expects programming claims to carry owners and dates.

Section three point six treats why code basics functions as testable only when evidence and ticket IDs are recorded.

For section three point six, Westmere University will not accept programming work without a written trail.

### 3.7 Testing

For each check, Samuel writes one example that should pass and one that should fail, and confirms the output.

Section three point seven develops programming with a Westmere University note Samuel Osei can demo offline.

Under section three point seven, Tom Becker expects programming claims to carry owners and dates.

Section three point seven treats why code basics functions as testable only when evidence and ticket IDs are recorded.

For section three point seven, Westmere University will not accept programming work without a written trail.

### Reading exports

The cloud team can export registry settings as JSON. Samuel's program opens the file with the json module, loops over the repositories and prints any problems. He records the export date in the output so readers know how current the result is. Later in the course, the same pattern checks accounts, identities and logs, so this first program becomes a template he reuses many times.

### Worked example

Samuel's first program lists repositories with anonymous pull enabled from a synthetic export. Dr Jensen asks what happens if a repository record has no "anonymous" field. Samuel adds a rule to report "setting missing" instead of assuming it is off.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Programs that assume missing settings are safe can hide problems.

### Exercises

- **EX007 — Why programs.** Why use programs for configuration checks? *Rubric:* 3 = consistent, fast, many resources; 2 = partial; 1 = none; 0 = none.
- **EX008 — Function benefit.** Why write checks as functions? *Rubric:* 3 = testable and reusable; 2 = partial; 1 = none; 0 = none.
- **EX009 — Missing field.** How does Samuel handle a missing field? *Rubric:* 3 = report setting missing; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small tested programs make checks reliable.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write clear academic and technical prose about cloud security; (2) cite sources correctly; (3) structure arguments; (4) avoid overstatement.

### 4.1 Purpose

Samuel's thesis and reports must persuade careful readers with evidence. Academic writing states claims, supports them with sources or data, and acknowledges limits.

Section four point one develops academic writing with a Westmere University note Samuel Osei can demo offline.

Under section four point one, Tom Becker expects academic claims to carry owners and dates.

Section four point one treats purpose structure citing precision as testable only when evidence and ticket IDs are recorded.

For section four point one, Westmere University will not accept academic work without a written trail.

### 4.2 Structure

Each paragraph makes one point: a topic sentence, evidence, and a link to the argument. Sections follow a logical order from problem to conclusion.

Section four point two develops academic writing with a Westmere University note Samuel Osei can demo offline.

Under section four point two, Tom Becker expects academic claims to carry owners and dates.

Section four point two treats purpose structure citing precision as testable only when evidence and ticket IDs are recorded.

For section four point two, Westmere University will not accept academic work without a written trail.

### 4.3 Citing

Standards and papers are cited in a consistent style with links or DOIs. Samuel cites NIST SP 800-190 when discussing container image risks and the Kubernetes documentation when describing Pod Security Standards.

Section four point three develops academic writing with a Westmere University note Samuel Osei can demo offline.

Under section four point three, Tom Becker expects academic claims to carry owners and dates.

Section four point three treats purpose structure citing precision as testable only when evidence and ticket IDs are recorded.

### 4.4 Precision

"Anonymous pull was enabled on two of four repositories" is better than "the registry was insecure".

Section four point four develops academic writing with a Westmere University note Samuel Osei can demo offline.

Under section four point four, Tom Becker expects academic claims to carry owners and dates.

Section four point four treats purpose structure citing precision as testable only when evidence and ticket IDs are recorded.

For section four point four, Westmere University will not accept academic work without a written trail.

### 4.5 Overstatement

"No evidence of misuse was found in available logs" is accurate; "no misuse occurred" is not, since logging was missing.

Section four point five develops academic writing with a Westmere University note Samuel Osei can demo offline.

Under section four point five, Tom Becker expects academic claims to carry owners and dates.

Section four point five treats purpose structure citing precision as testable only when evidence and ticket IDs are recorded.

For section four point five, Westmere University will not accept academic work without a written trail.

### 4.6 Revising

Samuel reads drafts aloud, removes unnecessary words and checks every number against its source.

Section four point six develops academic writing with a Westmere University note Samuel Osei can demo offline.

Under section four point six, Tom Becker expects academic claims to carry owners and dates.

Section four point six treats purpose structure citing precision as testable only when evidence and ticket IDs are recorded.

For section four point six, Westmere University will not accept academic work without a written trail.

Section four point six fails closed if academic evidence is missing rather than guessing.

### 4.7 Feedback

Dr Jensen comments on drafts within a week; Samuel keeps a list of recurring feedback to avoid repeating mistakes.

Section four point seven develops academic writing with a Westmere University note Samuel Osei can demo offline.

Under section four point seven, Tom Becker expects academic claims to carry owners and dates.

Section four point seven treats purpose structure citing precision as testable only when evidence and ticket IDs are recorded.

For section four point seven, Westmere University will not accept academic work without a written trail.

### Using sources well

Samuel learns to prefer primary sources: the standard itself, not a blog summary of it. When a secondary source is useful, he checks its claims against the original. He also records the version and access date for web documents, since cloud documentation changes often. A short source log beside each essay lists each source, why it was used and where in the text it supports a claim.

### Worked example

In his first essay, Samuel writes that the registry exposure "had no impact". Dr Jensen asks how he knows. He revises to "no unusual access was found in the logs that existed; the period without logs cannot be assessed", a statement the evidence supports.

> **Synthetic case.** Essays are synthetic.

### Errors and limits

Absence of evidence is not evidence of absence when logging was missing.

### Exercises

- **EX010 — Paragraph structure.** Describe a good paragraph. *Rubric:* 3 = topic sentence, evidence, link; 2 = two; 1 = one; 0 = none.
- **EX011 — Accurate phrasing.** Why is "no misuse occurred" an overstatement? *Rubric:* 3 = logs missing for part of the period; 2 = partial; 1 = none; 0 = none.
- **EX012 — Revision habit.** Name a revision habit. *Rubric:* 3 = read aloud, cut words, check numbers; 2 = one; 1 = none; 0 = none.

### Synthesis

Clear, sourced and modest writing persuades careful readers.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain core security ideas in cloud terms; (2) recognise common cloud risks; (3) understand defence in depth and least privilege; (4) read security guidance critically.

### 5.1 Core ideas

Confidentiality, integrity and availability; authentication and authorisation; least privilege; defence in depth; logging and accountability. Each has a cloud form: identity policies, encryption settings, multi-zone deployment, audit logs.

Section five point one develops security literacy with a Westmere University note Samuel Osei can demo offline.

Under section five point one, Tom Becker expects security claims to carry owners and dates.

Section five point one treats core ideas common cloud as testable only when evidence and ticket IDs are recorded.

For section five point one, Westmere University will not accept security work without a written trail.

### 5.2 Common cloud risks

Misconfigured storage and registries, over-broad identities, leaked credentials, unpatched images, missing logs. Most are configuration choices on the customer's side.

Section five point two develops security literacy with a Westmere University note Samuel Osei can demo offline.

Under section five point two, Tom Becker expects security claims to carry owners and dates.

Section five point two treats core ideas common cloud as testable only when evidence and ticket IDs are recorded.

For section five point two, Westmere University will not accept security work without a written trail.

### 5.3 Least privilege

Each person and service gets only the access it needs. If records-api had used a short-lived identity instead of a connection string, there would have been no secret to leak.

Section five point three develops security literacy with a Westmere University note Samuel Osei can demo offline.

Under section five point three, Tom Becker expects security claims to carry owners and dates.

Section five point three treats core ideas common cloud as testable only when evidence and ticket IDs are recorded.

For section five point three, Westmere University will not accept security work without a written trail.

### 5.4 Defence in depth

Several layers: private registry, no secrets in images, scanning before push, limited database permissions, logging. Any one could have reduced the opening case's risk.

Section five point four develops security literacy with a Westmere University note Samuel Osei can demo offline.

Under section five point four, Tom Becker expects security claims to carry owners and dates.

Section five point four treats core ideas common cloud as testable only when evidence and ticket IDs are recorded.

For section five point four, Westmere University will not accept security work without a written trail.

### 5.5 Guidance

CIS Benchmarks give configuration checklists; CSA CCM v4 lists cloud controls; NIST SP 800-190 covers containers. Samuel learns to check the date and scope of guidance before using it.

Section five point five develops security literacy with a Westmere University note Samuel Osei can demo offline.

Under section five point five, Tom Becker expects security claims to carry owners and dates.

Section five point five treats core ideas common cloud as testable only when evidence and ticket IDs are recorded.

For section five point five, Westmere University will not accept security work without a written trail.

### 5.6 Thinking like a defender

Ask what could go wrong, how it would be noticed and how it would be fixed.

Section five point six develops security literacy with a Westmere University note Samuel Osei can demo offline.

Under section five point six, Tom Becker expects security claims to carry owners and dates.

Section five point six treats core ideas common cloud as testable only when evidence and ticket IDs are recorded.

For section five point six, Westmere University will not accept security work without a written trail.

### Reading guidance critically

For each piece of guidance, Samuel asks who wrote it, for which systems, how recent it is and what evidence supports it. A CIS Benchmark for a specific managed Kubernetes version is more useful to StudyHub than a general blog post. Vendor guidance may favour the vendor's products; it is still useful for configuration details, but recommendations about which tools to buy need independent checking.

### Worked example

Samuel maps the opening case to defence-in-depth layers and finds that only one layer, network restrictions on the test database, was working. That layer probably prevented harm, which shows why multiple layers matter.

> **Synthetic case.** Case details are synthetic.

### Errors and limits

Guidance can be outdated; check versions.

### Exercises

- **EX013 — Common risks.** Name three common cloud risks. *Rubric:* 3 = storage/registry misconfig, broad identities, leaked creds, unpatched images, missing logs; 2 = two; 1 = one; 0 = none.
- **EX014 — Least privilege example.** How would least privilege have helped records-api? *Rubric:* 3 = short-lived identity, no secret; 2 = partial; 1 = none; 0 = none.
- **EX015 — Working layer.** Which layer worked? *Rubric:* 3 = network restrictions on test DB; 2 = partial; 1 = none; 0 = none.

### Synthesis

Core security ideas take specific forms in the cloud.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) model identities and roles as a graph; (2) find paths to privileged roles; (3) reason about reachability; (4) use graph results to reduce privilege.

### 6.1 Graphs for access

In the cloud, identities can often assume other roles. Treat each identity and role as a node and each "may assume" permission as a directed edge. A path from a person to an administrator role means that person can become an administrator, even if no single permission says so directly.

Section six point one develops discrete structures with a Westmere University note Samuel Osei can demo offline.

Under section six point one, Tom Becker expects discrete claims to carry owners and dates.

### 6.2 Breadth-first search

Breadth-first search explores neighbours level by level and finds the shortest path. It is simple to implement with a queue and a set of visited nodes, and it always terminates on a finite graph.

Section six point two develops discrete structures with a Westmere University note Samuel Osei can demo offline.

Under section six point two, Tom Becker expects discrete claims to carry owners and dates.

Section six point two treats graphs for access breadth-first as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — role paths

```python
"""Find which identities can reach an admin role through role-assumption chains (BFS, stdlib only)."""
from collections import deque
can_assume = {  # identity -> roles it may assume
    "dev-alice": ["ci-runner"], "ci-runner": ["deployer"], "deployer": ["cluster-admin"],
    "analyst-bo": ["reports-reader"], "reports-reader": [], "support-cy": ["ticket-bot"],
    "ticket-bot": ["deployer"], "cluster-admin": [],
}
def path(start, goal="cluster-admin"):
    q, seen = deque([[start]]), {start}
    while q:
        p = q.popleft()
        if p[-1] == goal: return p
        for n in can_assume.get(p[-1], []):
            if n not in seen: seen.add(n); q.append(p + [n])
for who in ["dev-alice", "analyst-bo", "support-cy"]:
    p = path(who)
    print(f"{who:11} {'REACHES admin: ' + ' -> '.join(p) if p else 'cannot reach admin'}")
```

Run with `python3 lab_graph.py`. Verified output:

```text
dev-alice   REACHES admin: dev-alice -> ci-runner -> deployer -> cluster-admin
analyst-bo  cannot reach admin
support-cy  REACHES admin: support-cy -> ticket-bot -> deployer -> cluster-admin
```

### 6.3 Lab result

dev-alice reaches cluster-admin through dev-alice -> ci-runner -> deployer -> cluster-admin. support-cy also reaches it through support-cy -> ticket-bot -> deployer -> cluster-admin. analyst-bo cannot reach admin. The surprise is support-cy: a helpdesk account can become cluster administrator through a ticket automation bot.

Section six point three develops discrete structures with a Westmere University note Samuel Osei can demo offline.

Under section six point three, Tom Becker expects discrete claims to carry owners and dates.

Section six point three treats graphs for access breadth-first as testable only when evidence and ticket IDs are recorded.

### 6.4 Why chains appear

Roles are added one at a time for convenience. Each edge looks reasonable alone; the risky path only appears when they are combined. NIST SP 800-210 discusses the difficulty of reasoning about combined access rules in cloud systems.

Section six point four develops discrete structures with a Westmere University note Samuel Osei can demo offline.

Under section six point four, Tom Becker expects discrete claims to carry owners and dates.

Section six point four treats graphs for access breadth-first as testable only when evidence and ticket IDs are recorded.

### 6.5 Using results

Breaking one edge breaks a path. The best edge to remove is one used by many risky paths and needed by few legitimate tasks.

Section six point five develops discrete structures with a Westmere University note Samuel Osei can demo offline.

Under section six point five, Tom Becker expects discrete claims to carry owners and dates.

Section six point five treats graphs for access breadth-first as testable only when evidence and ticket IDs are recorded.

For section six point five, Westmere University will not accept discrete work without a written trail.

### Repeating the analysis

The graph is rebuilt monthly from exports so new risky paths are found early.

### Worked example

Tom's team finds the ticket-bot needed to restart pods, not deploy. They replace its link to deployer with a narrow restart role. Rerunning the analysis shows only dev-alice's pipeline path remains, which is expected and protected by review rules.

> **Synthetic case.** Identities and roles are synthetic.

### Errors and limits

Graphs built from exports miss conditions such as time limits; check details for each path.

### Exercises

- **EX016 — Edge meaning.** What does an edge represent? *Rubric:* 3 = may assume permission; 2 = partial; 1 = none; 0 = none.
- **EX017 — Surprise path.** Which path was surprising and why? *Rubric:* 3 = support-cy via ticket-bot; 2 = partial; 1 = none; 0 = none.
- **EX018 — Fix.** How was it fixed? *Rubric:* 3 = ticket-bot given narrow restart role; 2 = partial; 1 = none; 0 = none.

### Synthesis

Graphs reveal privilege paths that single permissions hide.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain cloud networking for StudyHub; (2) describe security groups, private endpoints and Kubernetes services; (3) reason about exposure; (4) plan network restrictions.

### 7.1 Virtual networks

StudyHub's cluster runs in a private network with subnets for nodes and databases. Only the load balancer is public. The test database accepted connections only from the cluster's subnet, which is why the leaked connection string could not be used from outside.

Section seven point one develops networks and protocols with a Westmere University note Samuel Osei can demo offline.

Under section seven point one, Tom Becker expects networks claims to carry owners and dates.

Section seven point one treats virtual networks security groups as testable only when evidence and ticket IDs are recorded.

### 7.2 Security groups and firewalls

Rules list allowed sources, destinations and ports. Default-deny with specific allows is safer than broad allows with exceptions.

Section seven point two develops networks and protocols with a Westmere University note Samuel Osei can demo offline.

Under section seven point two, Tom Becker expects networks claims to carry owners and dates.

Section seven point two treats virtual networks security groups as testable only when evidence and ticket IDs are recorded.

For section seven point two, Westmere University will not accept networks work without a written trail.

### 7.3 Private endpoints

Managed services such as the registry and storage can be reached through private endpoints inside the network, so traffic need not cross the internet and public access can be disabled.

Section seven point three develops networks and protocols with a Westmere University note Samuel Osei can demo offline.

Under section seven point three, Tom Becker expects networks claims to carry owners and dates.

Section seven point three treats virtual networks security groups as testable only when evidence and ticket IDs are recorded.

### 7.4 Kubernetes networking

Pods can talk to each other freely unless network policies restrict them. Services provide stable names; ingress controllers route external requests.

Section seven point four develops networks and protocols with a Westmere University note Samuel Osei can demo offline.

Under section seven point four, Tom Becker expects networks claims to carry owners and dates.

Section seven point four treats virtual networks security groups as testable only when evidence and ticket IDs are recorded.

For section seven point four, Westmere University will not accept networks work without a written trail.

### 7.5 TLS

Traffic is encrypted with TLS. Certificates are managed automatically and monitored for expiry.

Section seven point five develops networks and protocols with a Westmere University note Samuel Osei can demo offline.

Under section seven point five, Tom Becker expects networks claims to carry owners and dates.

Section seven point five treats virtual networks security groups as testable only when evidence and ticket IDs are recorded.

For section seven point five, Westmere University will not accept networks work without a written trail.

Section seven point five fails closed if networks evidence is missing rather than guessing.

### 7.6 Exposure analysis

For each component, Samuel lists what can reach it: internet, campus network, cluster or specific services.

Section seven point six develops networks and protocols with a Westmere University note Samuel Osei can demo offline.

Under section seven point six, Tom Becker expects networks claims to carry owners and dates.

Section seven point six treats virtual networks security groups as testable only when evidence and ticket IDs are recorded.

For section seven point six, Westmere University will not accept networks work without a written trail.

### 7.7 Change risk

Network changes can break services, so they are tested in the test environment and rolled out gradually.

Section seven point seven develops networks and protocols with a Westmere University note Samuel Osei can demo offline.

Under section seven point seven, Tom Becker expects networks claims to carry owners and dates.

Section seven point seven treats virtual networks security groups as testable only when evidence and ticket IDs are recorded.

For section seven point seven, Westmere University will not accept networks work without a written trail.

### Documenting flows

Samuel writes a short table of every allowed network flow with its purpose and owner. When a rule is proposed, reviewers check it against the table. Flows without a known purpose are investigated and, if unused, removed. The table also helps new team members understand StudyHub quickly, and it becomes the basis for Kubernetes network policies later in the course.

### Worked example

The exposure analysis shows the registry is reachable from the internet, needed only because a build server outside the network pushes images. Moving the build to a runner inside the network lets the team disable public registry access entirely.

> **Synthetic case.** Networks are synthetic.

### Errors and limits

Network controls reduce reach but do not replace authentication.

### Exercises

- **EX019 — Why string unusable.** Why couldn't the leaked string be used from outside? *Rubric:* 3 = DB only accepted cluster subnet; 2 = partial; 1 = none; 0 = none.
- **EX020 — Private endpoint.** What does a private endpoint provide? *Rubric:* 3 = access inside network; public off; 2 = partial; 1 = none; 0 = none.
- **EX021 — Registry fix.** How was public registry access removed? *Rubric:* 3 = build runner inside network; 2 = partial; 1 = none; 0 = none.

### Synthesis

Limit what can reach each component.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) build a larger configuration checker with modules and tests; (2) parse JSON exports; (3) handle errors; (4) produce reports for different readers.

### 8.1 Design

Samuel's checker has three parts: loaders for each export type, a set of check functions and a report writer. Adding a new check means adding one function and its tests.

Section eight point one develops programming ii with a Westmere University note Samuel Osei can demo offline.

Under section eight point one, Tom Becker expects programming claims to carry owners and dates.

Section eight point one treats design parsing errors tests as testable only when evidence and ticket IDs are recorded.

For section eight point one, Westmere University will not accept programming work without a written trail.

### 8.2 Parsing

Exports from the cloud console and Kubernetes are JSON. Each loader validates required fields and reports malformed records with their position.

Section eight point two develops programming ii with a Westmere University note Samuel Osei can demo offline.

Under section eight point two, Tom Becker expects programming claims to carry owners and dates.

Section eight point two treats design parsing errors tests as testable only when evidence and ticket IDs are recorded.

For section eight point two, Westmere University will not accept programming work without a written trail.

### 8.3 Errors

A check that cannot run reports "unable to check" rather than silently passing.

Section eight point three develops programming ii with a Westmere University note Samuel Osei can demo offline.

Under section eight point three, Tom Becker expects programming claims to carry owners and dates.

Section eight point three treats design parsing errors tests as testable only when evidence and ticket IDs are recorded.

For section eight point three, Westmere University will not accept programming work without a written trail.

Section eight point three fails closed if programming evidence is missing rather than guessing.

### 8.4 Tests

Each check has tests with synthetic records: one compliant, one non-compliant, one with missing fields. Tests run automatically on every change.

Section eight point four develops programming ii with a Westmere University note Samuel Osei can demo offline.

Under section eight point four, Tom Becker expects programming claims to carry owners and dates.

Section eight point four treats design parsing errors tests as testable only when evidence and ticket IDs are recorded.

For section eight point four, Westmere University will not accept programming work without a written trail.

### 8.5 Reports

A detailed report for the cloud team lists every finding; a summary for managers counts findings by severity and account.

Section eight point five develops programming ii with a Westmere University note Samuel Osei can demo offline.

Under section eight point five, Tom Becker expects programming claims to carry owners and dates.

Section eight point five treats design parsing errors tests as testable only when evidence and ticket IDs are recorded.

For section eight point five, Westmere University will not accept programming work without a written trail.

### 8.6 Review

Tom's team reviews the code before it runs against real exports, checking that it only reads files.

Section eight point six develops programming ii with a Westmere University note Samuel Osei can demo offline.

Under section eight point six, Tom Becker expects programming claims to carry owners and dates.

Section eight point six treats design parsing errors tests as testable only when evidence and ticket IDs are recorded.

For section eight point six, Westmere University will not accept programming work without a written trail.

### 8.7 Version control

The checker lives in a repository with a changelog, so results can be linked to the code version.

Section eight point seven develops programming ii with a Westmere University note Samuel Osei can demo offline.

Under section eight point seven, Tom Becker expects programming claims to carry owners and dates.

Section eight point seven treats design parsing errors tests as testable only when evidence and ticket IDs are recorded.

For section eight point seven, Westmere University will not accept programming work without a written trail.

### Running regularly

The checker runs weekly against fresh exports, and its reports are saved with the export date and code version. Comparing weekly reports shows whether findings are being fixed or new ones appearing. Samuel adds a short section at the top of each report listing what changed since the previous week, which is what the cloud team reads first. Over the term, weekly reports show findings falling from 41 to 12, with the remaining ones assigned to owners and dates.

### Sharing

The checker is shared with other university teams.

### Worked example

During review, a team member notices that the checker treats repository names case-sensitively while the registry does not. A test with mixed-case names is added and the comparison fixed.

> **Synthetic case.** Code and data are synthetic.

### Errors and limits

Checkers need the same care as production code.

### Exercises

- **EX022 — Three parts.** Name the checker's parts. *Rubric:* 3 = loaders, checks, report writer; 2 = two; 1 = one; 0 = none.
- **EX023 — Unable to check.** Why report "unable to check"? *Rubric:* 3 = avoid silent passing; 2 = partial; 1 = none; 0 = none.
- **EX024 — Case bug.** What bug did review find? *Rubric:* 3 = case-sensitive names; 2 = partial; 1 = none; 0 = none.

### Synthesis

Structured, reviewed checkers scale to many resources.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) classify StudyHub's data; (2) apply access, encryption and retention; (3) separate test and production data; (4) check retention with a lab.

### 9.1 Data classes

Student records (personal, high), coursework uploads (personal, medium), logs (may contain personal data), test data (should be synthetic). Classification guides controls.

Section nine point one develops data and databases with a Westmere University note Samuel Osei can demo offline.

Under section nine point one, Tom Becker expects data claims to carry owners and dates.

Section nine point one treats data classes test data as testable only when evidence and ticket IDs are recorded.

For section nine point one, Westmere University will not accept data work without a written trail.

### 9.2 Test data

Test databases should never hold real student data. The opening case's test database held synthetic records only, which limited the impact; Samuel confirms with a check against known synthetic markers.

Section nine point two develops data and databases with a Westmere University note Samuel Osei can demo offline.

Under section nine point two, Tom Becker expects data claims to carry owners and dates.

Section nine point two treats data classes test data as testable only when evidence and ticket IDs are recorded.

### 9.3 Access

Applications use database roles with only the needed permissions; administrators use separate, audited accounts.

Section nine point three develops data and databases with a Westmere University note Samuel Osei can demo offline.

Under section nine point three, Tom Becker expects data claims to carry owners and dates.

Section nine point three treats data classes test data as testable only when evidence and ticket IDs are recorded.

For section nine point three, Westmere University will not accept data work without a written trail.

### 9.4 Encryption

Managed databases and storage encrypt at rest; connections require TLS.

Section nine point four develops data and databases with a Westmere University note Samuel Osei can demo offline.

Under section nine point four, Tom Becker expects data claims to carry owners and dates.

Section nine point four treats data classes test data as testable only when evidence and ticket IDs are recorded.

For section nine point four, Westmere University will not accept data work without a written trail.

Section nine point four fails closed if data evidence is missing rather than guessing.

### 9.5 Retention

Keeping data longer than needed increases risk. Westmere's rules: app logs 90 days, audit logs 365, exam uploads 400, test snapshots 30.

Section nine point five develops data and databases with a Westmere University note Samuel Osei can demo offline.

Under section nine point five, Tom Becker expects data claims to carry owners and dates.

Section nine point five treats data classes test data as testable only when evidence and ticket IDs are recorded.

For section nine point five, Westmere University will not accept data work without a written trail.

### Lab — Lab — retention check

```python
"""Compare synthetic data store ages with retention rules (stdlib only)."""
rules = {"app-logs": 90, "audit-logs": 365, "exam-uploads": 400, "test-db-snapshots": 30}
stores = [("app-logs", 120), ("audit-logs", 200), ("exam-uploads", 380), ("test-db-snapshots", 210), ("test-db-snapshots", 12)]
for kind, age in stores:
    print(f"{kind:18} age {age:3} d, limit {rules[kind]:3} d  {'OVER RETENTION' if age > rules[kind] else 'ok'}")
```

Run with `python3 lab_retention.py`. Verified output:

```text
app-logs           age 120 d, limit  90 d  OVER RETENTION
audit-logs         age 200 d, limit 365 d  ok
exam-uploads       age 380 d, limit 400 d  ok
test-db-snapshots  age 210 d, limit  30 d  OVER RETENTION
test-db-snapshots  age  12 d, limit  30 d  ok
```

### 9.6 Lab result

app-logs at 120 days exceed the 90-day limit. One test-db-snapshot at 210 days exceeds its 30-day limit; another at 12 days is fine. audit-logs (200 of 365) and exam-uploads (380 of 400) are within limits. The 210-day snapshot is a forgotten copy that should have been deleted automatically.

Section nine point six develops data and databases with a Westmere University note Samuel Osei can demo offline.

Under section nine point six, Tom Becker expects data claims to carry owners and dates.

Section nine point six treats data classes test data as testable only when evidence and ticket IDs are recorded.

### Lifecycle rules

Cloud storage and snapshot services support lifecycle rules that delete or archive data after a set age. Rules are defined in code, reviewed and tested on synthetic objects. They are better than manual deletion because they never forget. Samuel checks each rule against Westmere's retention policy and finds that app logs had no rule at all, which explains why they exceeded 90 days.

### Owner review

Data owners confirm retention periods yearly with the records office.

### Worked example

The forgotten snapshot was made manually during a migration and was outside the lifecycle rules. The team deletes it after confirming nobody needs it, and adds a rule that manual snapshots carry an expiry tag enforced by automation.

> **Synthetic case.** Data stores are synthetic.

### Errors and limits

Deleting data is irreversible; confirm before deleting.

### Exercises

- **EX025 — Test data rule.** What should test databases contain? *Rubric:* 3 = synthetic data only; 2 = partial; 1 = none; 0 = none.
- **EX026 — Lab over.** Which stores were over retention? *Rubric:* 3 = app-logs 120; snapshot 210; 2 = one; 1 = none; 0 = none.
- **EX027 — Snapshot fix.** What rule followed? *Rubric:* 3 = expiry tags on manual snapshots; 2 = partial; 1 = none; 0 = none.

### Synthesis

Classify data, separate test data and enforce retention.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) work within authorisation in cloud projects; (2) respect student privacy; (3) handle findings responsibly; (4) know when to stop and escalate.

### 10.1 Authorisation

Samuel's project agreement lists what he may access: read-only exports, a test account and documentation. He may not access production data or test production systems.

Section ten point one develops ethics and authorized practice with a Westmere University note Samuel Osei can demo offline.

Under section ten point one, Tom Becker expects ethics claims to carry owners and dates.

Section ten point one treats authorisation privacy responsible findings as testable only when evidence and ticket IDs are recorded.

For section ten point one, Westmere University will not accept ethics work without a written trail.

### 10.2 Privacy

Student records are personal data. Samuel's labs use synthetic data. If he encounters real data by mistake, he stops and reports it.

Section ten point two develops ethics and authorized practice with a Westmere University note Samuel Osei can demo offline.

Under section ten point two, Tom Becker expects ethics claims to carry owners and dates.

Section ten point two treats authorisation privacy responsible findings as testable only when evidence and ticket IDs are recorded.

For section ten point two, Westmere University will not accept ethics work without a written trail.

### 10.3 Responsible findings

Findings go to Tom and Dr Jensen, not to classmates or public forums. Reports avoid details that would help misuse before fixes are made.

Section ten point three develops ethics and authorized practice with a Westmere University note Samuel Osei can demo offline.

Under section ten point three, Tom Becker expects ethics claims to carry owners and dates.

Section ten point three treats authorisation privacy responsible findings as testable only when evidence and ticket IDs are recorded.

For section ten point three, Westmere University will not accept ethics work without a written trail.

### 10.4 Defensive purpose

The project checks and improves configurations; it does not attempt to break in. Testing that could affect availability needs explicit approval.

Section ten point four develops ethics and authorized practice with a Westmere University note Samuel Osei can demo offline.

Under section ten point four, Tom Becker expects ethics claims to carry owners and dates.

Section ten point four treats authorisation privacy responsible findings as testable only when evidence and ticket IDs are recorded.

For section ten point four, Westmere University will not accept ethics work without a written trail.

### 10.5 Conflicts of interest

If a finding concerns a colleague's work, it is reported factually, without blame.

Section ten point five develops ethics and authorized practice with a Westmere University note Samuel Osei can demo offline.

Under section ten point five, Tom Becker expects ethics claims to carry owners and dates.

Section ten point five treats authorisation privacy responsible findings as testable only when evidence and ticket IDs are recorded.

For section ten point five, Westmere University will not accept ethics work without a written trail.

### 10.6 Escalation

Signs of active misuse go immediately to Westmere's security team.

Section ten point six develops ethics and authorized practice with a Westmere University note Samuel Osei can demo offline.

Under section ten point six, Tom Becker expects ethics claims to carry owners and dates.

Section ten point six treats authorisation privacy responsible findings as testable only when evidence and ticket IDs are recorded.

For section ten point six, Westmere University will not accept ethics work without a written trail.

Section ten point six fails closed if ethics evidence is missing rather than guessing.

### Writing it down

Samuel's project agreement is signed by Tom, Dr Jensen and Westmere's data protection officer before he receives any exports. It lists permitted data, storage location, retention and contacts for reporting concerns. Having it in writing protects Samuel as well as the university: if a question arises about what he accessed, the agreement and access logs answer it. He keeps a short access diary recording each export he receives and when he deleted local copies.

### Supervisor role

Dr Jensen checks quarterly that the project stays within its agreement and signs the access diary.

### Worked example

While reviewing exports, Samuel sees an access key printed in a build log. He does not use or test it; he reports it to Tom, who revokes it within an hour and adds log masking to the build system.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Testing a found credential, even to check it works, is using it without authorisation.

### Exercises

- **EX028 — Allowed access.** What may Samuel access? *Rubric:* 3 = read-only exports, test account, documentation; 2 = two; 1 = one; 0 = none.
- **EX029 — Found key.** What did Samuel do with the found key? *Rubric:* 3 = reported, did not use; 2 = partial; 1 = none; 0 = none.
- **EX030 — Testing a credential.** Why not test a found credential? *Rubric:* 3 = that is unauthorised use; 2 = partial; 1 = none; 0 = none.

### Synthesis

Stay within authorisation and report findings responsibly.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain how containers rely on Linux features; (2) describe users, permissions and capabilities in containers; (3) apply secure defaults to StudyHub pods; (4) recognise risky settings.

### 11.1 Containers are processes

A container is a group of processes isolated by Linux namespaces and limited by control groups. It shares the node's kernel, so settings that weaken isolation affect the whole node.

Section eleven point one develops operating systems with a Westmere University note Samuel Osei can demo offline.

Under section eleven point one, Tom Becker expects operating claims to carry owners and dates.

Section eleven point one treats containers are processes users as testable only when evidence and ticket IDs are recorded.

For section eleven point one, Westmere University will not accept operating work without a written trail.

### 11.2 Users

Many images run as root by default. Running as a non-root user means that a flaw in the application gives less power inside the container and less chance to affect the node.

Section eleven point two develops operating systems with a Westmere University note Samuel Osei can demo offline.

Under section eleven point two, Tom Becker expects operating claims to carry owners and dates.

Section eleven point two treats containers are processes users as testable only when evidence and ticket IDs are recorded.

### 11.3 Capabilities

Root powers are split into capabilities. Most web services need none; dropping all and adding only what is required is the secure default recommended by NIST SP 800-190.

Section eleven point three develops operating systems with a Westmere University note Samuel Osei can demo offline.

Under section eleven point three, Tom Becker expects operating claims to carry owners and dates.

Section eleven point three treats containers are processes users as testable only when evidence and ticket IDs are recorded.

For section eleven point three, Westmere University will not accept operating work without a written trail.

### 11.4 File systems

A read-only root file system prevents changes to the application files at run time; temporary data goes to mounted volumes.

Section eleven point four develops operating systems with a Westmere University note Samuel Osei can demo offline.

Under section eleven point four, Tom Becker expects operating claims to carry owners and dates.

Section eleven point four treats containers are processes users as testable only when evidence and ticket IDs are recorded.

For section eleven point four, Westmere University will not accept operating work without a written trail.

### 11.5 Pod Security Standards

Kubernetes defines Privileged, Baseline and Restricted profiles. Restricted requires non-root, no privilege escalation, dropped capabilities and a seccomp profile. StudyHub targets Restricted for all application namespaces.

Section eleven point five develops operating systems with a Westmere University note Samuel Osei can demo offline.

Under section eleven point five, Tom Becker expects operating claims to carry owners and dates.

Section eleven point five treats containers are processes users as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Westmere University will not accept operating work without a written trail.

### 11.6 Patching

Base images include operating system packages that need updates; images are rebuilt regularly from patched bases.

Section eleven point six develops operating systems with a Westmere University note Samuel Osei can demo offline.

Under section eleven point six, Tom Becker expects operating claims to carry owners and dates.

Section eleven point six treats containers are processes users as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Westmere University will not accept operating work without a written trail.

### 11.7 Checking

Samuel's checker reads pod specifications and reports settings that violate Restricted.

Section eleven point seven develops operating systems with a Westmere University note Samuel Osei can demo offline.

Under section eleven point seven, Tom Becker expects operating claims to carry owners and dates.

Section eleven point seven treats containers are processes users as testable only when evidence and ticket IDs are recorded.

For section eleven point seven, Westmere University will not accept operating work without a written trail.

Section eleven point seven fails closed if operating evidence is missing rather than guessing.

### Admission enforcement

Once pods comply, the Restricted profile is enforced at admission for application namespaces, so new non-compliant pods are rejected with a clear message. System namespaces keep documented exceptions with an owner and review date.

### Worked example

The check finds that 9 of 31 StudyHub pods run as root, mostly because their images never set a user. Rebuilding the images with a non-root user and testing them in the test cluster takes two sprints; afterwards all application pods meet Restricted.

> **Synthetic case.** Pods and counts are synthetic.

### Errors and limits

Some system components need more privileges; isolate them rather than weakening the profile everywhere.

### Exercises

- **EX031 — Shared kernel.** Why do isolation-weakening settings affect the node? *Rubric:* 3 = containers share kernel; 2 = partial; 1 = none; 0 = none.
- **EX032 — Restricted requirements.** Name three Restricted requirements. *Rubric:* 3 = non-root, no escalation, dropped caps, seccomp; 2 = two; 1 = one; 0 = none.
- **EX033 — Root pods.** How many pods ran as root and why? *Rubric:* 3 = 9 of 31; no user set; 2 = partial; 1 = none; 0 = none.

### Synthesis

Containers should run with minimal privileges by default.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) summarise remediation times; (2) distinguish mean and median; (3) estimate a proportion with an interval; (4) interpret uncertainty.

### 12.1 Skewed data

Times to fix findings are skewed: most are quick, a few take months. The median describes the typical case; the mean is pulled up by long delays.

Section twelve point one develops probability and statistics with a Westmere University note Samuel Osei can demo offline.

Under section twelve point one, Tom Becker expects probability claims to carry owners and dates.

Section twelve point one treats skewed data lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point one, Westmere University will not accept probability work without a written trail.

### Lab — Lab — remediation statistics

```python
"""Remediation times and a 95% interval for the share fixed within 14 days (stdlib only)."""
import math, statistics
days = [2, 3, 3, 5, 6, 7, 8, 9, 10, 12, 13, 15, 18, 21, 25, 30, 33, 41, 55, 70]
k = sum(d <= 14 for d in days); n = len(days); p = k / n
se = math.sqrt(p * (1 - p) / n)
print(f"n {n}, mean {statistics.mean(days):.1f}, median {statistics.median(days)}, within 14 days {k}/{n} = {p:.2f}")
print(f"approx 95% interval {max(0,p-1.96*se):.2f}-{min(1,p+1.96*se):.2f}")
```

Run with `python3 lab_stats.py`. Verified output:

```text
n 20, mean 19.3, median 12.5, within 14 days 11/20 = 0.55
approx 95% interval 0.33-0.77
```

### 12.2 Lab result

Across 20 synthetic findings, the mean time to fix is 19.3 days and the median 12.5. Eleven of 20 (0.55) were fixed within the 14-day target. An approximate 95% interval for that proportion is 0.33 to 0.77.

Section twelve point two develops probability and statistics with a Westmere University note Samuel Osei can demo offline.

Under section twelve point two, Tom Becker expects probability claims to carry owners and dates.

Section twelve point two treats skewed data lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point two, Westmere University will not accept probability work without a written trail.

### 12.3 Interpreting the interval

With only 20 findings, the true on-time rate could plausibly be anywhere from about a third to three quarters. Claims like "we fix 55% on time" should carry this uncertainty.

Section twelve point three develops probability and statistics with a Westmere University note Samuel Osei can demo offline.

Under section twelve point three, Tom Becker expects probability claims to carry owners and dates.

Section twelve point three treats skewed data lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point three, Westmere University will not accept probability work without a written trail.

### 12.4 Sample size

Quadrupling the sample roughly halves the interval width. Samuel plans to report quarterly once more findings accumulate.

Section twelve point four develops probability and statistics with a Westmere University note Samuel Osei can demo offline.

Under section twelve point four, Tom Becker expects probability claims to carry owners and dates.

Section twelve point four treats skewed data lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Westmere University will not accept probability work without a written trail.

### 12.5 Comparing periods

Differences between periods need intervals too; a rise from 55% to 65% on small samples may be noise.

Section twelve point five develops probability and statistics with a Westmere University note Samuel Osei can demo offline.

Under section twelve point five, Tom Becker expects probability claims to carry owners and dates.

Section twelve point five treats skewed data lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Westmere University will not accept probability work without a written trail.

### 12.6 Presenting

Charts show medians and percentiles, with sample sizes labelled.

Section twelve point six develops probability and statistics with a Westmere University note Samuel Osei can demo offline.

Under section twelve point six, Tom Becker expects probability claims to carry owners and dates.

Section twelve point six treats skewed data lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point six, Westmere University will not accept probability work without a written trail.

Section twelve point six fails closed if probability evidence is missing rather than guessing.

### Why the median matters here

The median of 12.5 days says a typical finding is fixed within target. The mean of 19.3 days is pulled up by four findings that took 33 to 70 days. Looking at those four, Samuel finds two waited for a vendor patch and two had no clear owner. Fixing ownership is cheap and addresses half the tail. This kind of analysis is more useful to the team than a single average, because it points to causes they can act on.

### Worked example

The cloud team had planned to report "45% of findings late" as a crisis. Samuel shows the wide interval and the median of 12.5 days, below target. The team reframes the report around the long tail of findings over 30 days, which have specific causes.

> **Synthetic case.** Data are synthetic.

### Errors and limits

The simple interval used here is approximate; for small samples better methods exist.

### Exercises

- **EX034 — Lab figures.** What were mean, median and on-time share? *Rubric:* 3 = 19.3, 12.5, 0.55; 2 = two; 1 = one; 0 = none.
- **EX035 — Interval.** What was the interval? *Rubric:* 3 = 0.33-0.77; 2 = partial; 1 = none; 0 = none.
- **EX036 — Reframing.** How was the report reframed? *Rubric:* 3 = focus on long tail over 30 days; 2 = partial; 1 = none; 0 = none.

### Synthesis

Report typical values and uncertainty honestly.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) review cloud user accounts and keys; (2) enforce multi-factor authentication; (3) remove stale access; (4) prefer federated and short-lived identities.

### 13.1 Human identities

Staff sign in through the university's identity provider with multi-factor authentication. Separate cloud console users should not exist except for documented break-glass accounts.

Section thirteen point one develops identity and access with a Westmere University note Samuel Osei can demo offline.

Under section thirteen point one, Tom Becker expects identity claims to carry owners and dates.

Section thirteen point one treats human identities service identities as testable only when evidence and ticket IDs are recorded.

For section thirteen point one, Westmere University will not accept identity work without a written trail.

### 13.2 Service identities

Services should use workload identity or managed identities that issue short-lived credentials, not long-lived access keys.

Section thirteen point two develops identity and access with a Westmere University note Samuel Osei can demo offline.

Under section thirteen point two, Tom Becker expects identity claims to carry owners and dates.

Section thirteen point two treats human identities service identities as testable only when evidence and ticket IDs are recorded.

For section thirteen point two, Westmere University will not accept identity work without a written trail.

### Lab — Lab — account review

```python
"""Review synthetic cloud console users: MFA, key age and last sign-in (stdlib only)."""
users = [("c.jensen", True, None, 2), ("t.becker", True, 45, 1), ("svc-backup", False, 610, None),
         ("old-contractor", False, 400, 220), ("s.osei", True, None, 5)]
for u, mfa, key_age, last in users:
    f = []
    if last is not None and not mfa: f.append("console user without MFA")
    if key_age and key_age > 90: f.append(f"access key {key_age} d old")
    if last and last > 90: f.append(f"inactive {last} d")
    print(f"{u:15} {'; '.join(f) or 'ok'}")
```

Run with `python3 lab_mfa.py`. Verified output:

```text
c.jensen        ok
t.becker        ok
svc-backup      access key 610 d old
old-contractor  console user without MFA; access key 400 d old; inactive 220 d
s.osei          ok
```

### 13.3 Lab result

c.jensen, t.becker and s.osei are ok. svc-backup has an access key 610 days old. old-contractor is a console user without MFA, with a 400-day-old key, inactive for 220 days. old-contractor should be removed; svc-backup should move to a managed identity.

Section thirteen point three develops identity and access with a Westmere University note Samuel Osei can demo offline.

Under section thirteen point three, Tom Becker expects identity claims to carry owners and dates.

Section thirteen point three treats human identities service identities as testable only when evidence and ticket IDs are recorded.

### 13.4 Stale access

Accounts inactive for 90 days are disabled after confirming with owners. Leavers' access is removed through the identity provider, which removes cloud access too when federation is used.

Section thirteen point four develops identity and access with a Westmere University note Samuel Osei can demo offline.

Under section thirteen point four, Tom Becker expects identity claims to carry owners and dates.

Section thirteen point four treats human identities service identities as testable only when evidence and ticket IDs are recorded.

For section thirteen point four, Westmere University will not accept identity work without a written trail.

### 13.5 Keys

Keys older than 90 days are rotated or, better, replaced by short-lived credentials.

Section thirteen point five develops identity and access with a Westmere University note Samuel Osei can demo offline.

Under section thirteen point five, Tom Becker expects identity claims to carry owners and dates.

Section thirteen point five treats human identities service identities as testable only when evidence and ticket IDs are recorded.

For section thirteen point five, Westmere University will not accept identity work without a written trail.

Section thirteen point five fails closed if identity evidence is missing rather than guessing.

### 13.6 Reviews

Quarterly access reviews list who has which roles; owners confirm each.

Section thirteen point six develops identity and access with a Westmere University note Samuel Osei can demo offline.

Under section thirteen point six, Tom Becker expects identity claims to carry owners and dates.

Section thirteen point six treats human identities service identities as testable only when evidence and ticket IDs are recorded.

For section thirteen point six, Westmere University will not accept identity work without a written trail.

Section thirteen point six fails closed if identity evidence is missing rather than guessing.

### Break-glass accounts

Two break-glass accounts exist for emergencies when the identity provider is unavailable. Their credentials are sealed, use hardware MFA, and any sign-in raises an immediate alert to the security team. They are tested twice a year. The access review checks they have not been used outside tests, and each test is recorded with who performed it and why.

### Role design

Roles are designed per task, such as read-only support, deployer and database administrator, and reviewed when tasks change.

### Worked example

Removing old-contractor reveals that a scheduled report used that account's key. The report is moved to a service identity with read-only access to one bucket, and the account is deleted. The incident shows why personal accounts must never run automation.

> **Synthetic case.** Accounts are synthetic.

### Errors and limits

Disabling accounts can break hidden dependencies; disable before deleting and watch for failures.

### Exercises

- **EX037 — Lab findings.** What did the lab find for old-contractor? *Rubric:* 3 = no MFA, 400 d key, inactive 220 d; 2 = two; 1 = one; 0 = none.
- **EX038 — svc-backup.** What should happen to svc-backup? *Rubric:* 3 = move to managed identity; 2 = partial; 1 = none; 0 = none.
- **EX039 — Hidden dependency.** What hidden dependency was found? *Rubric:* 3 = scheduled report used contractor key; 2 = partial; 1 = none; 0 = none.

### Synthesis

Federated, short-lived identities and regular reviews keep access tidy.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) apply privacy principles to StudyHub; (2) minimise and protect student data; (3) understand lawful basis and rights; (4) build privacy into cloud designs.

### 14.1 Principles

Collect only what is needed, use it only for stated purposes, keep it only as long as needed, keep it accurate and secure, and be transparent with students.

Section fourteen point one develops privacy foundations with a Westmere University note Samuel Osei can demo offline.

Under section fourteen point one, Tom Becker expects privacy claims to carry owners and dates.

Section fourteen point one treats principles data location minimisation as testable only when evidence and ticket IDs are recorded.

For section fourteen point one, Westmere University will not accept privacy work without a written trail.

### 14.2 Data location

Where cloud data is stored affects which laws apply. Westmere keeps student data in its home region and records this in its data register.

Section fourteen point two develops privacy foundations with a Westmere University note Samuel Osei can demo offline.

Under section fourteen point two, Tom Becker expects privacy claims to carry owners and dates.

Section fourteen point two treats principles data location minimisation as testable only when evidence and ticket IDs are recorded.

For section fourteen point two, Westmere University will not accept privacy work without a written trail.

### 14.3 Minimisation in design

StudyHub's analytics use aggregated data; individual records stay in the records system. Logs mask student IDs.

Section fourteen point three develops privacy foundations with a Westmere University note Samuel Osei can demo offline.

Under section fourteen point three, Tom Becker expects privacy claims to carry owners and dates.

Section fourteen point three treats principles data location minimisation as testable only when evidence and ticket IDs are recorded.

For section fourteen point three, Westmere University will not accept privacy work without a written trail.

### 14.4 Rights

Students can ask for their data; systems need a way to find and export it. Knowing where data lives (chapter 9) makes this possible.

Section fourteen point four develops privacy foundations with a Westmere University note Samuel Osei can demo offline.

Under section fourteen point four, Tom Becker expects privacy claims to carry owners and dates.

Section fourteen point four treats principles data location minimisation as testable only when evidence and ticket IDs are recorded.

For section fourteen point four, Westmere University will not accept privacy work without a written trail.

### 14.5 Breach duties

Exposure of personal data may need reporting to a regulator and students within strict time limits. Good logging lets Westmere determine what was exposed.

Section fourteen point five develops privacy foundations with a Westmere University note Samuel Osei can demo offline.

Under section fourteen point five, Tom Becker expects privacy claims to carry owners and dates.

Section fourteen point five treats principles data location minimisation as testable only when evidence and ticket IDs are recorded.

For section fourteen point five, Westmere University will not accept privacy work without a written trail.

### 14.6 Privacy and security

Security controls protect privacy, but privacy also asks whether data should be collected at all.

Section fourteen point six develops privacy foundations with a Westmere University note Samuel Osei can demo offline.

Under section fourteen point six, Tom Becker expects privacy claims to carry owners and dates.

Section fourteen point six treats principles data location minimisation as testable only when evidence and ticket IDs are recorded.

For section fourteen point six, Westmere University will not accept privacy work without a written trail.

### 14.7 Test data

Synthetic test data avoids privacy risk in testing entirely.

Section fourteen point seven develops privacy foundations with a Westmere University note Samuel Osei can demo offline.

Under section fourteen point seven, Tom Becker expects privacy claims to carry owners and dates.

Section fourteen point seven treats principles data location minimisation as testable only when evidence and ticket IDs are recorded.

For section fourteen point seven, Westmere University will not accept privacy work without a written trail.

Section fourteen point seven fails closed if privacy evidence is missing rather than guessing.

### Privacy reviews

New StudyHub features go through a short privacy review: what data, why, for how long, who can access it and whether a smaller set would do. The review takes under an hour for most features and is recorded. Samuel helps redesign the review form so developers answer in plain language. In its first term, the review stops one feature from collecting date of birth where age band was enough.

### Worked example

Samuel finds that an old analytics job copies full student records nightly into a reporting bucket, though the reports only need counts per course. The job is changed to produce counts directly, and the bucket's old copies are deleted after approval.

> **Synthetic case.** Data and jobs are synthetic.

### Errors and limits

Aggregated data can still identify people in small groups; suppress small counts.

### Exercises

- **EX040 — Principles.** List three privacy principles. *Rubric:* 3 = minimise, purpose, retention, accuracy, security, transparency; 2 = two; 1 = one; 0 = none.
- **EX041 — Logging and breach.** How does logging help with breach duties? *Rubric:* 3 = determine what was exposed; 2 = partial; 1 = none; 0 = none.
- **EX042 — Analytics change.** How was the analytics job changed? *Rubric:* 3 = counts instead of full records; 2 = partial; 1 = none; 0 = none.

### Synthesis

Privacy asks whether data is needed, not only how to protect it.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) gather evidence about cloud controls; (2) check audit logging coverage; (3) measure gaps; (4) keep evidence trustworthy.

### 15.1 Why logs matter

The opening case could not measure how long the registry was open because logging was off. Audit logs record who changed what and when, and are the main evidence for investigations.

Section fifteen point one develops evidence and measurement with a Westmere University note Samuel Osei can demo offline.

Under section fifteen point one, Tom Becker expects evidence claims to carry owners and dates.

Section fifteen point one treats why logs matter lab as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — logging coverage

```python
"""Check audit logging per synthetic account and region (stdlib only)."""
accounts = {"studyhub-prod": {"eu-west": True, "eu-central": True}, "studyhub-test": {"eu-west": True, "eu-central": False},
            "research-sandbox": {"eu-west": False, "eu-central": False}}
gaps = [(a, r) for a, regs in accounts.items() for r, on in regs.items() if not on]
for a, r in gaps: print(f"NO AUDIT LOG: {a} / {r}")
total = sum(len(r) for r in accounts.values())
print(f"logging coverage {total-len(gaps)}/{total}")
```

Run with `python3 lab_logging.py`. Verified output:

```text
NO AUDIT LOG: studyhub-test / eu-central
NO AUDIT LOG: research-sandbox / eu-west
NO AUDIT LOG: research-sandbox / eu-central
logging coverage 3/6
```

### 15.2 Lab result

Audit logging is missing in studyhub-test / eu-central and in both regions of research-sandbox. Coverage is 3 of 6 account-region pairs. studyhub-prod is fully covered; the gaps are in test and research accounts, which are exactly where mistakes are often made.

Section fifteen point two develops evidence and measurement with a Westmere University note Samuel Osei can demo offline.

Under section fifteen point two, Tom Becker expects evidence claims to carry owners and dates.

Section fifteen point two treats why logs matter lab as testable only when evidence and ticket IDs are recorded.

### 15.3 Fixing gaps

An organisation-wide logging configuration turns on audit logs for every account and region, sending them to a separate log account that individual accounts cannot alter.

Section fifteen point three develops evidence and measurement with a Westmere University note Samuel Osei can demo offline.

Under section fifteen point three, Tom Becker expects evidence claims to carry owners and dates.

Section fifteen point three treats why logs matter lab as testable only when evidence and ticket IDs are recorded.

For section fifteen point three, Westmere University will not accept evidence work without a written trail.

### 15.4 Trustworthy evidence

Logs are stored with integrity protection and restricted access. Evidence collected for reports records source, time and hash.

Section fifteen point four develops evidence and measurement with a Westmere University note Samuel Osei can demo offline.

Under section fifteen point four, Tom Becker expects evidence claims to carry owners and dates.

Section fifteen point four treats why logs matter lab as testable only when evidence and ticket IDs are recorded.

For section fifteen point four, Westmere University will not accept evidence work without a written trail.

### 15.5 Measures

Logging coverage, time to fix findings and number of high-risk configurations are tracked monthly.

Section fifteen point five develops evidence and measurement with a Westmere University note Samuel Osei can demo offline.

Under section fifteen point five, Tom Becker expects evidence claims to carry owners and dates.

Section fifteen point five treats why logs matter lab as testable only when evidence and ticket IDs are recorded.

For section fifteen point five, Westmere University will not accept evidence work without a written trail.

### 15.6 Limits

Logs show actions, not intentions; missing data must be stated in reports.

Section fifteen point six develops evidence and measurement with a Westmere University note Samuel Osei can demo offline.

Under section fifteen point six, Tom Becker expects evidence claims to carry owners and dates.

Section fifteen point six treats why logs matter lab as testable only when evidence and ticket IDs are recorded.

For section fifteen point six, Westmere University will not accept evidence work without a written trail.

Section fifteen point six fails closed if evidence evidence is missing rather than guessing.

### Evidence log

Samuel keeps an evidence log for his project: each export or log extract received, its date, source, hash and where it is stored. When he quotes a figure in a report, the log shows where it came from. Tom later adopts the same format for the cloud team's audit preparation, because auditors ask exactly these questions.

### Report gaps

Reports state gaps openly.

### Worked example

After organisation-wide logging is enabled, coverage reaches 6 of 6. A month later, logs show a researcher creating a public bucket in the sandbox; the account-level block prevents it, and the log provides clear evidence for a friendly reminder rather than a guess.

> **Synthetic case.** Accounts and events are synthetic.

### Errors and limits

Logging only per account can be switched off by that account's administrators; central configuration is stronger.

### Exercises

- **EX043 — Lab coverage.** What was coverage and where were gaps? *Rubric:* 3 = 3/6; test eu-central and research both; 2 = two; 1 = one; 0 = none.
- **EX044 — Central logging.** Why send logs to a separate account? *Rubric:* 3 = cannot be altered by individual accounts; 2 = partial; 1 = none; 0 = none.
- **EX045 — Sandbox event.** What did logs show a month later? *Rubric:* 3 = attempted public bucket, blocked; 2 = partial; 1 = none; 0 = none.

### Synthesis

Logs are evidence; make coverage complete and tamper-resistant.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) design a layered architecture for StudyHub; (2) separate accounts and environments; (3) place trust boundaries; (4) use guardrails at organisation level.

### 16.1 Account structure

Westmere uses separate cloud accounts for production, test, research sandboxes, shared tooling and logs. Accounts are strong boundaries: a mistake in a sandbox cannot change production resources.

Section sixteen point one develops security architecture with a Westmere University note Samuel Osei can demo offline.

Under section sixteen point one, Tom Becker expects security claims to carry owners and dates.

Section sixteen point one treats account structure organisation guardrails as testable only when evidence and ticket IDs are recorded.

For section sixteen point one, Westmere University will not accept security work without a written trail.

### 16.2 Organisation guardrails

Policies at the organisation level block public storage, restrict regions to the home region and prevent disabling audit logs. Guardrails apply to every account, including ones created in the future.

Section sixteen point two develops security architecture with a Westmere University note Samuel Osei can demo offline.

Under section sixteen point two, Tom Becker expects security claims to carry owners and dates.

Section sixteen point two treats account structure organisation guardrails as testable only when evidence and ticket IDs are recorded.

For section sixteen point two, Westmere University will not accept security work without a written trail.

### 16.3 Cluster design

Production and test clusters are separate. Within production, namespaces separate services, with default-deny network policies and Restricted pod security.

Section sixteen point three develops security architecture with a Westmere University note Samuel Osei can demo offline.

Under section sixteen point three, Tom Becker expects security claims to carry owners and dates.

Section sixteen point three treats account structure organisation guardrails as testable only when evidence and ticket IDs are recorded.

For section sixteen point three, Westmere University will not accept security work without a written trail.

### 16.4 Trust boundaries

Internet to load balancer; cluster to managed database; build system to registry; registry to cluster; accounts to log account. Each boundary has authentication and logging.

Section sixteen point four develops security architecture with a Westmere University note Samuel Osei can demo offline.

Under section sixteen point four, Tom Becker expects security claims to carry owners and dates.

Section sixteen point four treats account structure organisation guardrails as testable only when evidence and ticket IDs are recorded.

For section sixteen point four, Westmere University will not accept security work without a written trail.

### 16.5 Zero trust

Following NIST SP 800-207, services authenticate each other and every request is authorised, rather than trusting anything inside the network.

Section sixteen point five develops security architecture with a Westmere University note Samuel Osei can demo offline.

Under section sixteen point five, Tom Becker expects security claims to carry owners and dates.

Section sixteen point five treats account structure organisation guardrails as testable only when evidence and ticket IDs are recorded.

For section sixteen point five, Westmere University will not accept security work without a written trail.

### 16.6 Documentation

An architecture diagram and decision records explain each choice.

Section sixteen point six develops security architecture with a Westmere University note Samuel Osei can demo offline.

Under section sixteen point six, Tom Becker expects security claims to carry owners and dates.

Section sixteen point six treats account structure organisation guardrails as testable only when evidence and ticket IDs are recorded.

For section sixteen point six, Westmere University will not accept security work without a written trail.

Section sixteen point six fails closed if security evidence is missing rather than guessing.

### 16.7 Review

Architecture changes are reviewed by the cloud team and a security reviewer.

Section sixteen point seven develops security architecture with a Westmere University note Samuel Osei can demo offline.

Under section sixteen point seven, Tom Becker expects security claims to carry owners and dates.

Section sixteen point seven treats account structure organisation guardrails as testable only when evidence and ticket IDs are recorded.

For section sixteen point seven, Westmere University will not accept security work without a written trail.

Section sixteen point seven fails closed if security evidence is missing rather than guessing.

### Account creation

New accounts are created only through an automated process that applies guardrails, logging and baseline roles from the start. Manual account creation is disabled. This means that a research group requesting a sandbox gets one that already blocks public storage and sends logs centrally, without anyone having to remember. Samuel tests the process with a synthetic request and confirms the new account passes all baseline checks on its first day.

### Worked example

Applying the account structure reveals that the research sandbox shared the production registry, which is how a research image could be pushed alongside StudyHub images. A separate sandbox registry is created, and production accepts images only from its own registry.

> **Synthetic case.** Architecture is synthetic.

### Errors and limits

Guardrails can block legitimate needs; provide a documented exception route.

### Exercises

- **EX046 — Account benefit.** Why use separate accounts? *Rubric:* 3 = strong boundary for mistakes; 2 = partial; 1 = none; 0 = none.
- **EX047 — Guardrails.** Name two organisation guardrails. *Rubric:* 3 = block public storage, restrict regions, keep audit logs; 2 = one; 1 = none; 0 = none.
- **EX048 — Shared registry.** What was found and fixed? *Rubric:* 3 = sandbox shared prod registry; separated; 2 = partial; 1 = none; 0 = none.

### Synthesis

Use accounts, guardrails and boundaries as layered architecture.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain encryption at rest and in transit; (2) describe key management in the cloud; (3) use hashes and signatures for images; (4) avoid common cryptographic mistakes.

### 17.1 Encryption in transit

TLS protects traffic between users and StudyHub and between services. Certificates are issued and renewed automatically.

Section seventeen point one develops cryptography concepts with a Westmere University note Samuel Osei can demo offline.

Under section seventeen point one, Tom Becker expects cryptography claims to carry owners and dates.

Section seventeen point one treats encryption in transit encryption as testable only when evidence and ticket IDs are recorded.

For section seventeen point one, Westmere University will not accept cryptography work without a written trail.

### 17.2 Encryption at rest

Managed storage and databases encrypt data at rest. Provider-managed keys are simplest; customer-managed keys in a key service add control over use and rotation, with audit logs of each use.

Section seventeen point two develops cryptography concepts with a Westmere University note Samuel Osei can demo offline.

Under section seventeen point two, Tom Becker expects cryptography claims to carry owners and dates.

Section seventeen point two treats encryption in transit encryption as testable only when evidence and ticket IDs are recorded.

For section seventeen point two, Westmere University will not accept cryptography work without a written trail.

### 17.3 Key management

Keys live in a managed key service, never in code or images. Access to use a key is granted to specific identities.

Section seventeen point three develops cryptography concepts with a Westmere University note Samuel Osei can demo offline.

Under section seventeen point three, Tom Becker expects cryptography claims to carry owners and dates.

Section seventeen point three treats encryption in transit encryption as testable only when evidence and ticket IDs are recorded.

For section seventeen point three, Westmere University will not accept cryptography work without a written trail.

### 17.4 Hashes

An image digest is a hash of its content. Deploying by digest guarantees the exact image tested is the one running.

Section seventeen point four develops cryptography concepts with a Westmere University note Samuel Osei can demo offline.

Under section seventeen point four, Tom Becker expects cryptography claims to carry owners and dates.

Section seventeen point four treats encryption in transit encryption as testable only when evidence and ticket IDs are recorded.

For section seventeen point four, Westmere University will not accept cryptography work without a written trail.

### 17.5 Signatures

The build system signs images; the cluster verifies signatures before running them, so images from elsewhere are refused.

Section seventeen point five develops cryptography concepts with a Westmere University note Samuel Osei can demo offline.

Under section seventeen point five, Tom Becker expects cryptography claims to carry owners and dates.

Section seventeen point five treats encryption in transit encryption as testable only when evidence and ticket IDs are recorded.

For section seventeen point five, Westmere University will not accept cryptography work without a written trail.

### 17.6 Mistakes

Hard-coded keys, home-made encryption schemes and disabled certificate checks. All are avoided by using platform services.

Section seventeen point six develops cryptography concepts with a Westmere University note Samuel Osei can demo offline.

Under section seventeen point six, Tom Becker expects cryptography claims to carry owners and dates.

Section seventeen point six treats encryption in transit encryption as testable only when evidence and ticket IDs are recorded.

For section seventeen point six, Westmere University will not accept cryptography work without a written trail.

### 17.7 Secrets

Connection strings and passwords belong in a secret manager, delivered to pods at run time, never baked into images like the one in the opening case.

Section seventeen point seven develops cryptography concepts with a Westmere University note Samuel Osei can demo offline.

Under section seventeen point seven, Tom Becker expects cryptography claims to carry owners and dates.

Section seventeen point seven treats encryption in transit encryption as testable only when evidence and ticket IDs are recorded.

For section seventeen point seven, Westmere University will not accept cryptography work without a written trail.

### Rotation

Customer-managed keys are rotated automatically each year; data encrypted with older key versions remains readable because the key service keeps previous versions for decryption. TLS certificates renew automatically weeks before expiry, and an alert fires if renewal fails. Samuel lists every certificate and key with its owner and renewal method so nothing depends on memory.

### Key access reviews

Who can use each key is reviewed quarterly alongside role reviews.

### Worked example

Samuel finds that records-api checked TLS certificates with verification disabled, a leftover from development. Enabling verification in the test cluster reveals no issues, and the setting is fixed in all environments.

> **Synthetic case.** Settings are synthetic.

### Errors and limits

Encryption protects data from some threats but not from authorised identities misusing access.

### Exercises

- **EX049 — Customer-managed keys.** What do customer-managed keys add? *Rubric:* 3 = control and audit of key use; 2 = partial; 1 = none; 0 = none.
- **EX050 — Digest benefit.** Why deploy by digest? *Rubric:* 3 = exact tested image runs; 2 = partial; 1 = none; 0 = none.
- **EX051 — TLS finding.** What TLS issue was found? *Rubric:* 3 = certificate verification disabled; 2 = partial; 1 = none; 0 = none.

### Synthesis

Use platform cryptography services and never bake secrets into images.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) design a small study of StudyHub's configuration; (2) form a question and hypothesis; (3) collect data ethically; (4) analyse and report.

### 18.1 Question

Samuel asks: "Are StudyHub images built from the shared base image less likely to contain high-severity vulnerabilities than images built from public bases?"

Section eighteen point one develops research methods with a Westmere University note Samuel Osei can demo offline.

Under section eighteen point one, Tom Becker expects research claims to carry owners and dates.

Section eighteen point one treats question hypothesis data analysis as testable only when evidence and ticket IDs are recorded.

For section eighteen point one, Westmere University will not accept research work without a written trail.

### 18.2 Hypothesis

Images from the shared base, rebuilt weekly, have fewer high-severity findings.

Section eighteen point two develops research methods with a Westmere University note Samuel Osei can demo offline.

Under section eighteen point two, Tom Becker expects research claims to carry owners and dates.

Section eighteen point two treats question hypothesis data analysis as testable only when evidence and ticket IDs are recorded.

For section eighteen point two, Westmere University will not accept research work without a written trail.

Section eighteen point two fails closed if research evidence is missing rather than guessing.

### 18.3 Data

Scan reports for 40 images over one month: 22 from the shared base, 18 from public bases.

Section eighteen point three develops research methods with a Westmere University note Samuel Osei can demo offline.

Under section eighteen point three, Tom Becker expects research claims to carry owners and dates.

Section eighteen point three treats question hypothesis data analysis as testable only when evidence and ticket IDs are recorded.

For section eighteen point three, Westmere University will not accept research work without a written trail.

Section eighteen point three fails closed if research evidence is missing rather than guessing.

### 18.4 Analysis

Median high-severity findings: 0 for shared-base images, 3 for public-base images. Of public-base images, 12 of 18 had at least one high finding versus 3 of 22 shared-base images.

Section eighteen point four develops research methods with a Westmere University note Samuel Osei can demo offline.

Under section eighteen point four, Tom Becker expects research claims to carry owners and dates.

Section eighteen point four treats question hypothesis data analysis as testable only when evidence and ticket IDs are recorded.

For section eighteen point four, Westmere University will not accept research work without a written trail.

### 18.5 Limits

Images were not randomly assigned to bases; teams using public bases may maintain their images less. Shu, Gu and Enck (2017) also found many vulnerable images on public registries, which is consistent but does not prove cause here.

Section eighteen point five develops research methods with a Westmere University note Samuel Osei can demo offline.

Under section eighteen point five, Tom Becker expects research claims to carry owners and dates.

Section eighteen point five treats question hypothesis data analysis as testable only when evidence and ticket IDs are recorded.

### 18.6 Ethics

Data are scan reports about images, not people; team names are not reported.

Section eighteen point six develops research methods with a Westmere University note Samuel Osei can demo offline.

Under section eighteen point six, Tom Becker expects research claims to carry owners and dates.

Section eighteen point six treats question hypothesis data analysis as testable only when evidence and ticket IDs are recorded.

For section eighteen point six, Westmere University will not accept research work without a written trail.

Section eighteen point six fails closed if research evidence is missing rather than guessing.

### 18.7 Report

A three-page report with method, results, limits and recommendation: move all images to the shared base.

Section eighteen point seven develops research methods with a Westmere University note Samuel Osei can demo offline.

Under section eighteen point seven, Tom Becker expects research claims to carry owners and dates.

Section eighteen point seven treats question hypothesis data analysis as testable only when evidence and ticket IDs are recorded.

For section eighteen point seven, Westmere University will not accept research work without a written trail.

### Planning the study

Before collecting data, Samuel writes a one-page plan: question, hypothesis, data source, measures, analysis and limits. Dr Jensen approves it. Writing the plan first prevents changing the question after seeing the results. He also decides in advance to report all images, including the ones that do not fit the hypothesis, and to describe how scan tool versions were kept the same through the month.

### Sharing results

Results are presented to the cloud team in ten minutes, with the limits shown on the same slide as the main finding.

### Worked example

Tom accepts the recommendation and adds a pipeline check that warns when an image uses a non-approved base. Within two months, 34 of 40 images use the shared base.

> **Synthetic case.** Data are synthetic.

### Errors and limits

A correlation in observational data suggests but does not prove that the base causes the difference.

### Exercises

- **EX052 — Hypothesis.** State the hypothesis. *Rubric:* 3 = shared base images have fewer high findings; 2 = partial; 1 = none; 0 = none.
- **EX053 — Results.** What were the shares with high findings? *Rubric:* 3 = 12/18 public vs 3/22 shared; 2 = partial; 1 = none; 0 = none.
- **EX054 — Limit.** Why can't the study prove cause? *Rubric:* 3 = not randomly assigned; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small, careful studies guide practical decisions.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Cloud and container security: scope and theory

### Learning outcomes

You will (1) define cloud and container security; (2) explain the theories behind isolation, least privilege and declarative configuration; (3) set the scope of the subject.

### 19.1 Definition

Cloud and container security protects workloads, data and identities on shared, on-demand infrastructure and in containerised platforms. NIST SP 800-145 defines the cloud; NIST SP 800-190 sets out container risks: image, registry, orchestrator, container and host.

Section nineteen point one develops cloud and container security scope with a Westmere University note Samuel Osei can demo offline.

Under section nineteen point one, Tom Becker expects cloud claims to carry owners and dates.

Section nineteen point one treats definition isolation theory least as testable only when evidence and ticket IDs are recorded.

### 19.2 Isolation theory

Security depends on separating tenants, workloads and privileges. Clouds use hypervisors and accounts; containers use kernel features; Kubernetes uses namespaces and policies.

Section nineteen point two develops cloud and container security scope with a Westmere University note Samuel Osei can demo offline.

Under section nineteen point two, Tom Becker expects cloud claims to carry owners and dates.

Section nineteen point two treats definition isolation theory least as testable only when evidence and ticket IDs are recorded.

For section nineteen point two, Westmere University will not accept cloud work without a written trail.

### 19.3 Least privilege

Every identity has only needed permissions. Sandhu et al. (1996) formalised role-based access control, which cloud identity systems implement at scale.

Section nineteen point three develops cloud and container security scope with a Westmere University note Samuel Osei can demo offline.

Under section nineteen point three, Tom Becker expects cloud claims to carry owners and dates.

Section nineteen point three treats definition isolation theory least as testable only when evidence and ticket IDs are recorded.

For section nineteen point three, Westmere University will not accept cloud work without a written trail.

### 19.4 Declarative configuration

Kubernetes and infrastructure-as-code describe the desired state; controllers make reality match. Burns et al. (2016) explain this design. Declarative configuration can be reviewed and checked before it is applied.

Section nineteen point four develops cloud and container security scope with a Westmere University note Samuel Osei can demo offline.

Under section nineteen point four, Tom Becker expects cloud claims to carry owners and dates.

Section nineteen point four treats definition isolation theory least as testable only when evidence and ticket IDs are recorded.

### 19.5 Shared responsibility

Provider and customer responsibilities differ by service model, as provider documentation explains.

Section nineteen point five develops cloud and container security scope with a Westmere University note Samuel Osei can demo offline.

Under section nineteen point five, Tom Becker expects cloud claims to carry owners and dates.

Section nineteen point five treats definition isolation theory least as testable only when evidence and ticket IDs are recorded.

For section nineteen point five, Westmere University will not accept cloud work without a written trail.

### 19.6 Scope for the course

Accounts and identity, networks, registries and images, clusters and workloads, data and logging, operations.

Section nineteen point six develops cloud and container security scope with a Westmere University note Samuel Osei can demo offline.

Under section nineteen point six, Tom Becker expects cloud claims to carry owners and dates.

Section nineteen point six treats definition isolation theory least as testable only when evidence and ticket IDs are recorded.

For section nineteen point six, Westmere University will not accept cloud work without a written trail.

### Why theory matters

Theory explains why controls work, which helps when a new service appears that no checklist covers. For example, knowing that isolation in containers depends on the shared kernel tells Samuel to be cautious about any setting that gives a pod access to the host, even if a checklist does not mention that specific setting. Theory also helps him explain decisions to colleagues who ask why a rule exists.

### Worked example

Samuel maps the opening case to NIST SP 800-190's risk areas: the anonymous registry is a registry risk, the connection string is an image risk and missing logs is an orchestration and operations gap. The mapping organises the rest of his project.

> **Synthetic case.** Mapping is for the synthetic case.

### Errors and limits

Theories describe ideals; real systems need verification.

### Exercises

- **EX055 — SP 800-190 areas.** Name the five SP 800-190 risk areas. *Rubric:* 3 = image, registry, orchestrator, container, host; 2 = three; 1 = one; 0 = none.
- **EX056 — Declarative benefit.** Why is declarative configuration helpful for security? *Rubric:* 3 = reviewable and checkable before applied; 2 = partial; 1 = none; 0 = none.
- **EX057 — Case mapping.** Map the connection string to an SP 800-190 area. *Rubric:* 3 = image risk; 2 = partial; 1 = none; 0 = none.

### Synthesis

Theory gives structure; practice must verify it.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Cloud and container security: foundational cases

### Learning outcomes

You will (1) study representative cloud security cases; (2) extract causes and lessons; (3) compare them with Westmere; (4) avoid hindsight bias.

### 20.1 Case types

Common patterns in published incident reviews and research include public storage, leaked credentials in code or images, over-privileged identities and unpatched images. Samuel studies synthetic cases modelled on these patterns.

Section twenty point one develops cloud and container security foundational with a Westmere University note Samuel Osei can demo offline.

Under section twenty point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty point one treats case types case public as testable only when evidence and ticket IDs are recorded.

### 20.2 Case A: public storage

A synthetic company's bucket of backups was public for months. Cause: a test setting copied to production. Lesson: account-level blocks and checks before deployment.

Section twenty point two develops cloud and container security foundational with a Westmere University note Samuel Osei can demo offline.

Under section twenty point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty point two treats case types case public as testable only when evidence and ticket IDs are recorded.

For section twenty point two, Westmere University will not accept cloud work without a written trail.

### 20.3 Case B: credential in image

A synthetic startup pushed an image with a cloud key to a public registry; the key was used to start costly machines. Cause: no secret scanning and long-lived keys. Lesson: short-lived identities and pre-push scanning.

Section twenty point three develops cloud and container security foundational with a Westmere University note Samuel Osei can demo offline.

Under section twenty point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty point three treats case types case public as testable only when evidence and ticket IDs are recorded.

### 20.4 Case C: over-privileged pipeline

A build system with administrator rights was misused after its token leaked. Lesson: narrow pipeline permissions.

Section twenty point four develops cloud and container security foundational with a Westmere University note Samuel Osei can demo offline.

Under section twenty point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty point four treats case types case public as testable only when evidence and ticket IDs are recorded.

For section twenty point four, Westmere University will not accept cloud work without a written trail.

### 20.5 Comparing

Westmere's opening case resembles Case B, without misuse, partly because of network restrictions on the database.

Section twenty point five develops cloud and container security foundational with a Westmere University note Samuel Osei can demo offline.

Under section twenty point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty point five treats case types case public as testable only when evidence and ticket IDs are recorded.

For section twenty point five, Westmere University will not accept cloud work without a written trail.

### 20.6 Hindsight

Decisions that look wrong afterwards may have been reasonable with what was known. Reviews focus on systems, not blame.

Section twenty point six develops cloud and container security foundational with a Westmere University note Samuel Osei can demo offline.

Under section twenty point six, Tom Becker expects cloud claims to carry owners and dates.

Section twenty point six treats case types case public as testable only when evidence and ticket IDs are recorded.

For section twenty point six, Westmere University will not accept cloud work without a written trail.

### Sources of cases

Good case sources include published incident reviews, regulator reports and academic studies. Samuel prefers sources that describe causes and fixes, not just headlines. For each case, he notes which details are confirmed and which are speculation, and only uses confirmed causes when drawing lessons. Using synthetic composites in teaching avoids naming real organisations while keeping the patterns accurate.

### Case discussions

Each case is discussed in a seminar.

### Worked example

Samuel builds a table mapping each case's causes to Westmere's controls: Westmere now has account-level storage blocks (A), pre-push scanning in progress (B) and a pipeline role review scheduled (C). The table guides priorities.

> **Synthetic case.** Cases are synthetic composites.

### Errors and limits

Cases are selected because they went wrong; they do not show how common problems are.

### Exercises

- **EX058 — Case B lesson.** What is Case B's lesson? *Rubric:* 3 = short-lived identities, pre-push scanning; 2 = partial; 1 = none; 0 = none.
- **EX059 — Hindsight.** What is hindsight bias? *Rubric:* 3 = judging past decisions with later knowledge; 2 = partial; 1 = none; 0 = none.
- **EX060 — Westmere comparison.** Which case resembles Westmere's? *Rubric:* 3 = Case B; 2 = partial; 1 = none; 0 = none.

### Synthesis

Cases teach patterns; compare them carefully with your own system.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Cloud and container security: system models

### Learning outcomes

You will (1) model StudyHub's components, identities and data flows; (2) identify trust boundaries; (3) find missing controls from the model; (4) keep the model current.

### 21.1 Components

Load balancer, web front end, records-api, coursework service, message queue, managed database, storage buckets, registry, build system, identity provider, log account.

Section twenty-one point one develops cloud and container security system with a Westmere University note Samuel Osei can demo offline.

Under section twenty-one point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-one point one treats components identities data flows as testable only when evidence and ticket IDs are recorded.

For section twenty-one point one, Westmere University will not accept cloud work without a written trail.

### 21.2 Identities

Each service has a Kubernetes service account mapped to a cloud identity; people sign in through the identity provider; the build system has its own identity.

Section twenty-one point two develops cloud and container security system with a Westmere University note Samuel Osei can demo offline.

Under section twenty-one point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-one point two treats components identities data flows as testable only when evidence and ticket IDs are recorded.

For section twenty-one point two, Westmere University will not accept cloud work without a written trail.

### 21.3 Data flows

Students to web; web to records-api; records-api to database; coursework service to storage; build to registry; registry to cluster; all accounts to logs.

Section twenty-one point three develops cloud and container security system with a Westmere University note Samuel Osei can demo offline.

Under section twenty-one point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-one point three treats components identities data flows as testable only when evidence and ticket IDs are recorded.

For section twenty-one point three, Westmere University will not accept cloud work without a written trail.

### 21.4 Trust boundaries

Marked where flows cross networks, accounts or identity domains. Shostack's (2014) question "what can go wrong?" is asked at each boundary.

Section twenty-one point four develops cloud and container security system with a Westmere University note Samuel Osei can demo offline.

Under section twenty-one point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-one point four treats components identities data flows as testable only when evidence and ticket IDs are recorded.

For section twenty-one point four, Westmere University will not accept cloud work without a written trail.

### 21.5 Finding gaps

For each flow, Samuel checks authentication, authorisation, encryption and logging. Gaps become backlog items.

Section twenty-one point five develops cloud and container security system with a Westmere University note Samuel Osei can demo offline.

Under section twenty-one point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-one point five treats components identities data flows as testable only when evidence and ticket IDs are recorded.

For section twenty-one point five, Westmere University will not accept cloud work without a written trail.

### 21.6 Keeping current

The model is stored with the infrastructure code and updated in the same pull request as architecture changes.

Section twenty-one point six develops cloud and container security system with a Westmere University note Samuel Osei can demo offline.

Under section twenty-one point six, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-one point six treats components identities data flows as testable only when evidence and ticket IDs are recorded.

For section twenty-one point six, Westmere University will not accept cloud work without a written trail.

### 21.7 Model limits

The model shows intended flows; flow logs show actual flows. Comparing them finds surprises.

Section twenty-one point seven develops cloud and container security system with a Westmere University note Samuel Osei can demo offline.

Under section twenty-one point seven, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-one point seven treats components identities data flows as testable only when evidence and ticket IDs are recorded.

For section twenty-one point seven, Westmere University will not accept cloud work without a written trail.

### Drawing the model

Samuel draws the model in a simple text-based diagram format stored in the repository, so changes appear in pull request diffs like code. Each box has an owner and a link to its configuration. Reviewers can see when a new flow is added without a matching update to authentication or logging. The format is also easy for screen readers, which matters for one colleague on the team.

### Worked example

The model shows the coursework service writes to storage using a role that can also delete any object in the bucket. Students' submissions could be deleted by a bug. The role is narrowed to write-only for new objects, and deletion is reserved for a retention job.

> **Synthetic case.** The model is synthetic.

### Errors and limits

Models omit details; verify important assumptions with real configuration.

### Exercises

- **EX061 — Per-flow checks.** What is checked for each flow? *Rubric:* 3 = authn, authz, encryption, logging; 2 = three; 1 = one; 0 = none.
- **EX062 — Model vs reality.** How are surprises found? *Rubric:* 3 = compare model with flow logs; 2 = partial; 1 = none; 0 = none.
- **EX063 — Coursework role.** What was wrong with the coursework role? *Rubric:* 3 = could delete any object; 2 = partial; 1 = none; 0 = none.

### Synthesis

Models of flows and identities reveal missing controls.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Cloud and container security: data and dependencies

### Learning outcomes

You will (1) track images, base layers and library dependencies; (2) understand supply chain risk for containers; (3) manage third-party services; (4) plan updates.

### 22.1 Image dependencies

Each image depends on a base image, operating system packages and application libraries. A vulnerability in any of them is a vulnerability in the image.

Section twenty-two point one develops cloud and container security data with a Westmere University note Samuel Osei can demo offline.

Under section twenty-two point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-two point one treats image dependencies base images as testable only when evidence and ticket IDs are recorded.

For section twenty-two point one, Westmere University will not accept cloud work without a written trail.

### 22.2 Base images

A shared, regularly rebuilt base image (chapter 18) reduces vulnerabilities and gives one place to apply fixes.

Section twenty-two point two develops cloud and container security data with a Westmere University note Samuel Osei can demo offline.

Under section twenty-two point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-two point two treats image dependencies base images as testable only when evidence and ticket IDs are recorded.

For section twenty-two point two, Westmere University will not accept cloud work without a written trail.

### 22.3 Inventories

A software bill of materials lists components in each image, so Westmere can answer "which images contain this library?" quickly when an advisory appears.

Section twenty-two point three develops cloud and container security data with a Westmere University note Samuel Osei can demo offline.

Under section twenty-two point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-two point three treats image dependencies base images as testable only when evidence and ticket IDs are recorded.

For section twenty-two point three, Westmere University will not accept cloud work without a written trail.

### 22.4 Third-party images

Images from public registries are mirrored into Westmere's registry after checking their digest and scanning them; the cluster runs only images from the internal registry.

Section twenty-two point four develops cloud and container security data with a Westmere University note Samuel Osei can demo offline.

Under section twenty-two point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-two point four treats image dependencies base images as testable only when evidence and ticket IDs are recorded.

For section twenty-two point four, Westmere University will not accept cloud work without a written trail.

### 22.5 Managed service dependencies

StudyHub depends on the managed database, identity provider and storage. Their availability and security notices are monitored.

Section twenty-two point five develops cloud and container security data with a Westmere University note Samuel Osei can demo offline.

Under section twenty-two point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-two point five treats image dependencies base images as testable only when evidence and ticket IDs are recorded.

For section twenty-two point five, Westmere University will not accept cloud work without a written trail.

### 22.6 Update plan

Base images rebuild weekly; application images rebuild when their base changes; critical advisories trigger immediate rebuilds.

Section twenty-two point six develops cloud and container security data with a Westmere University note Samuel Osei can demo offline.

Under section twenty-two point six, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-two point six treats image dependencies base images as testable only when evidence and ticket IDs are recorded.

For section twenty-two point six, Westmere University will not accept cloud work without a written trail.

### 22.7 Removing dependencies

Unused libraries and services are removed to shrink what must be tracked.

Section twenty-two point seven develops cloud and container security data with a Westmere University note Samuel Osei can demo offline.

Under section twenty-two point seven, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-two point seven treats image dependencies base images as testable only when evidence and ticket IDs are recorded.

For section twenty-two point seven, Westmere University will not accept cloud work without a written trail.

### Generating inventories

The build pipeline generates a component list for every image automatically and stores it with the image digest in the registry. A small script searches all lists for a given library name and version. Samuel tests the script against a synthetic advisory before relying on it, and checks that images built before the pipeline change are rebuilt so they also have lists.

### Worked example

An advisory for a widely used compression library arrives. Using the inventory, Samuel finds it in 7 images within minutes; all are rebuilt from the patched base and deployed within two days. Without the inventory, the team estimates it would have taken a week to find them.

> **Synthetic case.** Images and advisories are synthetic.

### Errors and limits

Inventories must be generated automatically or they go stale.

### Exercises

- **EX064 — Image dependencies.** What does an image depend on? *Rubric:* 3 = base image, OS packages, libraries; 2 = two; 1 = one; 0 = none.
- **EX065 — Third-party images.** How are third-party images handled? *Rubric:* 3 = mirrored, digest-checked, scanned; 2 = partial; 1 = none; 0 = none.
- **EX066 — Advisory response.** How quickly were affected images found? *Rubric:* 3 = minutes via inventory; 7 images; 2 = partial; 1 = none; 0 = none.

### Synthesis

Track what goes into images so fixes reach every one.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Cloud and container security: methods I

### Learning outcomes

You will (1) review registry configuration systematically; (2) check anonymous access, image age and scanning; (3) prioritise fixes; (4) verify results.

### 23.1 Method

For each repository: is anonymous pull enabled? How old is the newest image? Has it ever been scanned? Who owns it?

Section twenty-three point one develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-three point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-three point one treats method lab result prioritising as testable only when evidence and ticket IDs are recorded.

For section twenty-three point one, Westmere University will not accept cloud work without a written trail.

### Lab — Lab — registry review

```python
"""Review synthetic container registry repositories: anonymous pull, image age, scan status (stdlib only)."""
repos = [("studyhub/web", False, 12, "scanned"), ("studyhub/records-api", True, 30, "scanned"),
         ("studyhub/legacy-import", True, 540, "never"), ("tools/base-python", False, 200, "scanned")]
for name, anon, age, scan in repos:
    f = [x for x, bad in (("anonymous pull enabled", anon), (f"newest image {age} d old", age > 180), ("never scanned", scan == "never")) if bad]
    print(f"{name:24} {'; '.join(f) or 'ok'}")
```

Run with `python3 lab_registry.py`. Verified output:

```text
studyhub/web             ok
studyhub/records-api     anonymous pull enabled
studyhub/legacy-import   anonymous pull enabled; newest image 540 d old; never scanned
tools/base-python        newest image 200 d old
```

### 23.2 Lab result

studyhub/web is ok. studyhub/records-api has anonymous pull enabled. studyhub/legacy-import has anonymous pull enabled, its newest image is 540 days old and it was never scanned. tools/base-python's newest image is 200 days old, which matters because many services build on it.

Section twenty-three point two develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-three point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-three point two treats method lab result prioritising as testable only when evidence and ticket IDs are recorded.

### 23.3 Prioritising

Anonymous pull is fixed first because it exposes images to anyone. The stale base image is next because its age spreads to dependent images. legacy-import is checked for use; unused repositories are archived.

Section twenty-three point three develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-three point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-three point three treats method lab result prioritising as testable only when evidence and ticket IDs are recorded.

### 23.4 Verifying fixes

After changes, an anonymous pull test from outside the network must be refused, and the review is rerun.

Section twenty-three point four develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-three point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-three point four treats method lab result prioritising as testable only when evidence and ticket IDs are recorded.

For section twenty-three point four, Westmere University will not accept cloud work without a written trail.

### 23.5 Prevention

Registry settings are defined in infrastructure code with private access by default; the organisation guardrail rejects public registry settings.

Section twenty-three point five develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-three point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-three point five treats method lab result prioritising as testable only when evidence and ticket IDs are recorded.

For section twenty-three point five, Westmere University will not accept cloud work without a written trail.

### Writing the review up

For each finding, the review records repository, setting, evidence (an export line or test result), owner and recommended action. Owners receive their findings directly with a deadline. Samuel follows up after a week and records the outcome. The written record lets the team show auditors that the registry was reviewed and fixed, and becomes the template for later reviews of other services.

### Repeat schedule

The review repeats quarterly, with results compared to the previous round.

### Worked example

Checking legacy-import shows it was last used by a migration finished a year earlier. The repository is archived and deleted after confirming with its owner, removing an unscanned, publicly pullable image entirely.

> **Synthetic case.** Repositories are synthetic.

### Errors and limits

Disabling anonymous access can break external consumers; check who pulls before changing.

### Exercises

- **EX067 — Lab findings.** What did the lab find for legacy-import? *Rubric:* 3 = anonymous, 540 d, never scanned; 2 = two; 1 = one; 0 = none.
- **EX068 — Priority.** Why fix anonymous pull first? *Rubric:* 3 = exposes images to anyone; 2 = partial; 1 = none; 0 = none.
- **EX069 — legacy-import outcome.** What happened to legacy-import? *Rubric:* 3 = archived and deleted; 2 = partial; 1 = none; 0 = none.

### Synthesis

Review registries systematically and fix exposure first.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Cloud and container security: controls

### Learning outcomes

You will (1) select and implement controls for StudyHub; (2) cover prevention, detection and response; (3) map controls to frameworks; (4) record them in a register.

### 24.1 Preventive controls

Organisation guardrails, private registry, admission control for signed images and Restricted pods, default-deny network policies, short-lived identities.

Section twenty-four point one develops cloud and container security controls with a Westmere University note Samuel Osei can demo offline.

Under section twenty-four point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-four point one treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point one, Westmere University will not accept cloud work without a written trail.

### 24.2 Detective controls

Central audit logs, alerts on high-risk changes, weekly configuration checks, image scanning.

Section twenty-four point two develops cloud and container security controls with a Westmere University note Samuel Osei can demo offline.

Under section twenty-four point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-four point two treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point two, Westmere University will not accept cloud work without a written trail.

### 24.3 Response controls

Runbooks for credential exposure, public resources and suspicious activity; ability to revoke credentials and isolate namespaces quickly.

Section twenty-four point three develops cloud and container security controls with a Westmere University note Samuel Osei can demo offline.

Under section twenty-four point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-four point three treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point three, Westmere University will not accept cloud work without a written trail.

### 24.4 Mapping

Each control maps to CSA CCM v4 domains and relevant CIS Benchmark sections, which helps auditors and shows coverage.

Section twenty-four point four develops cloud and container security controls with a Westmere University note Samuel Osei can demo offline.

Under section twenty-four point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-four point four treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point four, Westmere University will not accept cloud work without a written trail.

### 24.5 Control register

A register lists each control, owner, evidence source, test method and last test date.

Section twenty-four point five develops cloud and container security controls with a Westmere University note Samuel Osei can demo offline.

Under section twenty-four point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-four point five treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point five, Westmere University will not accept cloud work without a written trail.

### 24.6 Prioritising

Controls addressing the opening case (registry access, secrets in images, logging) come first.

Section twenty-four point six develops cloud and container security controls with a Westmere University note Samuel Osei can demo offline.

Under section twenty-four point six, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-four point six treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point six, Westmere University will not accept cloud work without a written trail.

### 24.7 Cost and effort

Most controls use built-in platform features, keeping cost low.

Section twenty-four point seven develops cloud and container security controls with a Westmere University note Samuel Osei can demo offline.

Under section twenty-four point seven, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-four point seven treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point seven, Westmere University will not accept cloud work without a written trail.

Section twenty-four point seven fails closed if cloud evidence is missing rather than guessing.

### Testing controls

Each control in the register has a test that can be run safely: a synthetic unsigned image must be refused, a public bucket request must be blocked, a synthetic high-risk change must raise an alert. Tests run monthly and results update the register. Failed tests become findings with owners. In the first round, 17 of 19 tests pass; the two failures are an alert routed to an old mailbox and a test namespace missing its network policy, both fixed within a week.

### Register owner

The register is owned by Tom, who reviews it monthly with the team.

### Retiring

Obsolete controls are retired with a reason.

### Worked example

The register shows that no control detects secrets in images before push. Samuel proposes a scan in the build pipeline that fails builds containing key-like strings, with a reviewed allow list for test placeholders. The cloud team adopts it.

> **Synthetic case.** Controls are synthetic.

### Errors and limits

A register is only useful if tests are actually run and dates updated.

### Exercises

- **EX070 — Control types.** Name the three control types with an example each. *Rubric:* 3 = preventive guardrail, detective alerts, response runbooks; 2 = two; 1 = one; 0 = none.
- **EX071 — Register fields.** What does the register record? *Rubric:* 3 = control, owner, evidence, test, last test; 2 = three; 1 = one; 0 = none.
- **EX072 — Missing control.** What gap did the register show? *Rubric:* 3 = no pre-push secret detection; 2 = partial; 1 = none; 0 = none.

### Synthesis

Choose controls across prevention, detection and response, and track them.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) practise configuration review on a synthetic environment; (2) apply registry, identity and logging checks together; (3) write a short lab report.

### 25.1 Lab environment

A synthetic export set models a small university platform: three accounts, a registry, a cluster and identities. No real systems are involved.

Section twenty-five point one develops laboratory with a Westmere University note Samuel Osei can demo offline.

Under section twenty-five point one, Tom Becker expects laboratory claims to carry owners and dates.

Section twenty-five point one treats lab environment tasks findings as testable only when evidence and ticket IDs are recorded.

For section twenty-five point one, Westmere University will not accept laboratory work without a written trail.

### 25.2 Tasks

Run the registry review, the account review and the logging coverage check; build the role graph; list findings by severity.

Section twenty-five point two develops laboratory with a Westmere University note Samuel Osei can demo offline.

Under section twenty-five point two, Tom Becker expects laboratory claims to carry owners and dates.

Section twenty-five point two treats lab environment tasks findings as testable only when evidence and ticket IDs are recorded.

For section twenty-five point two, Westmere University will not accept laboratory work without a written trail.

### 25.3 Findings expected

Students should find an anonymous repository, an account without MFA, missing logging in one region and a role path from a support account to an admin role.

Section twenty-five point three develops laboratory with a Westmere University note Samuel Osei can demo offline.

Under section twenty-five point three, Tom Becker expects laboratory claims to carry owners and dates.

Section twenty-five point three treats lab environment tasks findings as testable only when evidence and ticket IDs are recorded.

For section twenty-five point three, Westmere University will not accept laboratory work without a written trail.

### 25.4 Report

One page: summary, findings with evidence, recommended fixes and order.

Section twenty-five point four develops laboratory with a Westmere University note Samuel Osei can demo offline.

Under section twenty-five point four, Tom Becker expects laboratory claims to carry owners and dates.

Section twenty-five point four treats lab environment tasks findings as testable only when evidence and ticket IDs are recorded.

For section twenty-five point four, Westmere University will not accept laboratory work without a written trail.

Section twenty-five point four fails closed if laboratory evidence is missing rather than guessing.

### 25.5 Assessment

Completeness, accuracy, prioritisation and clarity.

Section twenty-five point five develops laboratory with a Westmere University note Samuel Osei can demo offline.

Under section twenty-five point five, Tom Becker expects laboratory claims to carry owners and dates.

Section twenty-five point five treats lab environment tasks findings as testable only when evidence and ticket IDs are recorded.

For section twenty-five point five, Westmere University will not accept laboratory work without a written trail.

Section twenty-five point five fails closed if laboratory evidence is missing rather than guessing.

### 25.6 Safety

All data synthetic; scripts read files only.

Section twenty-five point six develops laboratory with a Westmere University note Samuel Osei can demo offline.

Under section twenty-five point six, Tom Becker expects laboratory claims to carry owners and dates.

Section twenty-five point six treats lab environment tasks findings as testable only when evidence and ticket IDs are recorded.

For section twenty-five point six, Westmere University will not accept laboratory work without a written trail.

Section twenty-five point six fails closed if laboratory evidence is missing rather than guessing.

### 25.7 Debrief

Students compare reports and discuss differences in prioritisation.

Section twenty-five point seven develops laboratory with a Westmere University note Samuel Osei can demo offline.

Under section twenty-five point seven, Tom Becker expects laboratory claims to carry owners and dates.

Section twenty-five point seven treats lab environment tasks findings as testable only when evidence and ticket IDs are recorded.

For section twenty-five point seven, Westmere University will not accept laboratory work without a written trail.

Section twenty-five point seven fails closed if laboratory evidence is missing rather than guessing.

### Lab preparation

Before the lab, students review the scripts from earlier chapters and read the synthetic environment description. Dr Jensen provides a short guide on how findings will be assessed, including that a clear statement of assumptions earns credit even when rankings differ. Students work in pairs, which mirrors real practice where reviews are checked by a second person. Each pair keeps a log of commands run and files read, which is submitted with the report as evidence of method.

### After the lab

Feedback is returned within a week with comments on evidence, ranking reasons and clarity, and each pair revises one section.

### Marks

Marks are shared with each pair.

### Worked example

Samuel's report ranks the support-to-admin path first, ahead of the anonymous repository, because it could give someone full control. Dr Jensen accepts the reasoning but notes that the anonymous repository is easier to exploit by outsiders; the debrief agrees both belong at the top, fixed in parallel.

> **Synthetic case.** The lab is synthetic.

### Errors and limits

Ranking depends on assumptions; state them.

### Exercises

- **EX073 — Lab tasks.** List the lab tasks. *Rubric:* 3 = registry, accounts, logging, role graph; 2 = three; 1 = one; 0 = none.
- **EX074 — Expected findings.** Name two expected findings. *Rubric:* 3 = anonymous repo, no-MFA account, missing log region, support-admin path; 2 = one; 1 = none; 0 = none.
- **EX075 — Ranking debate.** How was the ranking debate resolved? *Rubric:* 3 = both top, fixed in parallel; 2 = partial; 1 = none; 0 = none.

### Synthesis

Combine checks and justify priorities.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Cloud and container security: methods II

### Learning outcomes

You will (1) assess cloud accounts against a benchmark-style checklist; (2) interpret pass and fail results; (3) prioritise by risk; (4) track improvement.

### 26.1 Benchmarks

The CIS Benchmarks provide consensus configuration recommendations for cloud accounts and Kubernetes. Samuel uses a small subset adapted for Westmere, keeping each item's reason.

Section twenty-six point one develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-six point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-six point one treats benchmarks lab result interpreting as testable only when evidence and ticket IDs are recorded.

For section twenty-six point one, Westmere University will not accept cloud work without a written trail.

### Lab — Lab — account checklist

```python
"""Score synthetic account settings against a small CIS-style checklist (stdlib only)."""
checks = {"root/owner account has MFA": True, "no root access keys": True, "audit logging all regions": False,
          "storage public access blocked": True, "password policy length >= 14": False,
          "default network has no open admin ports": False, "log files encrypted": True}
passed = sum(checks.values())
for c, ok in checks.items(): print(f"[{'PASS' if ok else 'FAIL'}] {c}")
print(f"score {passed}/{len(checks)} = {100*passed/len(checks):.0f}%")
```

Run with `python3 lab_cis.py`. Verified output:

```text
[PASS] root/owner account has MFA
[PASS] no root access keys
[FAIL] audit logging all regions
[PASS] storage public access blocked
[FAIL] password policy length >= 14
[FAIL] default network has no open admin ports
[PASS] log files encrypted
score 4/7 = 57%
```

### 26.2 Lab result

Four of seven checks pass: owner account MFA, no owner access keys, storage public access blocked and log files encrypted. Three fail: audit logging in all regions, password policy length at least 14, and the default network having no open administration ports. The score is 57%.

Section twenty-six point two develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-six point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-six point two treats benchmarks lab result interpreting as testable only when evidence and ticket IDs are recorded.

### 26.3 Interpreting

A percentage hides differences in importance. Open administration ports and missing logging matter more than password length, since staff sign in through the identity provider rather than local passwords.

Section twenty-six point three develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-six point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-six point three treats benchmarks lab result interpreting as testable only when evidence and ticket IDs are recorded.

### 26.4 Prioritising

Fix open ports first, then logging (already planned centrally), then password policy for the few local accounts.

Section twenty-six point four develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-six point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-six point four treats benchmarks lab result interpreting as testable only when evidence and ticket IDs are recorded.

For section twenty-six point four, Westmere University will not accept cloud work without a written trail.

### 26.5 Tracking

The checklist runs monthly; results are charted per account.

Section twenty-six point five develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-six point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-six point five treats benchmarks lab result interpreting as testable only when evidence and ticket IDs are recorded.

For section twenty-six point five, Westmere University will not accept cloud work without a written trail.

Section twenty-six point five fails closed if cloud evidence is missing rather than guessing.

### 26.6 Limits

Benchmarks cover common settings, not Westmere-specific risks such as role paths.

Section twenty-six point six develops cloud and container security methods with a Westmere University note Samuel Osei can demo offline.

Under section twenty-six point six, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-six point six treats benchmarks lab result interpreting as testable only when evidence and ticket IDs are recorded.

For section twenty-six point six, Westmere University will not accept cloud work without a written trail.

Section twenty-six point six fails closed if cloud evidence is missing rather than guessing.

### Adapting the benchmark

Samuel selects benchmark items relevant to Westmere's services and records why others were left out, for example items for services the university does not use. Each selected item keeps its benchmark reference so auditors can trace it. He also adds two Westmere-specific checks that no benchmark covers: no role path from support accounts to administrator roles, and no repository with anonymous pull. The checklist is reviewed every year when new benchmark versions are published, and changes are noted in its history.

### Worked example

The open administration ports belong to a default network created with the account and never used. Deleting the default network in all accounts removes the issue and simplifies the environment; the guardrail now prevents default networks in new accounts.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Passing a benchmark is not the same as being secure.

### Exercises

- **EX076 — Lab score.** What was the score and which checks failed? *Rubric:* 3 = 4/7; logging, password, open ports; 2 = two; 1 = one; 0 = none.
- **EX077 — Weighting.** Why does password length matter less here? *Rubric:* 3 = staff use identity provider; 2 = partial; 1 = none; 0 = none.
- **EX078 — Ports fix.** How were the open ports fixed? *Rubric:* 3 = deleted unused default networks; 2 = partial; 1 = none; 0 = none.

### Synthesis

Use benchmarks as a baseline and prioritise by real risk.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Cloud and container security: verification

### Learning outcomes

You will (1) verify that controls behave as intended with safe tests; (2) compare expected and observed results; (3) investigate failures; (4) record evidence.

### 27.1 Why verify

Configuration can say a control is on while it does not work, for example because of a wrong label or an old version. Verification observes behaviour.

Section twenty-seven point one develops cloud and container security verification with a Westmere University note Samuel Osei can demo offline.

Under section twenty-seven point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-seven point one treats why verify lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point one, Westmere University will not accept cloud work without a written trail.

### Lab — Lab — control verification

```python
"""Compare expected and observed results of synthetic control tests (stdlib only)."""
tests = [("anonymous pull refused", "refused", "refused"), ("public bucket blocked", "blocked", "blocked"),
         ("privileged pod rejected", "rejected", "admitted"), ("MFA required for console", "required", "required"),
         ("audit log written", "written", "written")]
fails = [t for t in tests if t[1] != t[2]]
for name, exp, obs in tests: print(f"{'PASS' if exp == obs else 'FAIL'}  {name:26} expected {exp:9} observed {obs}")
print(f"{len(tests)-len(fails)}/{len(tests)} passed")
```

Run with `python3 lab_verify.py`. Verified output:

```text
PASS  anonymous pull refused     expected refused   observed refused
PASS  public bucket blocked      expected blocked   observed blocked
FAIL  privileged pod rejected    expected rejected  observed admitted
PASS  MFA required for console   expected required  observed required
PASS  audit log written          expected written   observed written
4/5 passed
```

### 27.2 Lab result

Four of five tests pass: anonymous pull refused, public bucket blocked, MFA required for console and audit log written. One fails: a privileged test pod was admitted when it should have been rejected.

Section twenty-seven point two develops cloud and container security verification with a Westmere University note Samuel Osei can demo offline.

Under section twenty-seven point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-seven point two treats why verify lab result as testable only when evidence and ticket IDs are recorded.

### 27.3 Investigating

The failure traces to the test namespace lacking the label that enforces the Restricted profile. The label is added and the test passes; a check now ensures every application namespace carries it.

Section twenty-seven point three develops cloud and container security verification with a Westmere University note Samuel Osei can demo offline.

Under section twenty-seven point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-seven point three treats why verify lab result as testable only when evidence and ticket IDs are recorded.

### 27.4 Safe tests

Tests use synthetic pods and objects in a test namespace or account; they never touch student data.

Section twenty-seven point four develops cloud and container security verification with a Westmere University note Samuel Osei can demo offline.

Under section twenty-seven point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-seven point four treats why verify lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point four, Westmere University will not accept cloud work without a written trail.

### 27.5 Evidence

Each test run records date, environment, expected and observed results and the configuration version.

Section twenty-seven point five develops cloud and container security verification with a Westmere University note Samuel Osei can demo offline.

Under section twenty-seven point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-seven point five treats why verify lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point five, Westmere University will not accept cloud work without a written trail.

### 27.6 Regular runs

Tests run after changes and monthly.

Section twenty-seven point six develops cloud and container security verification with a Westmere University note Samuel Osei can demo offline.

Under section twenty-seven point six, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-seven point six treats why verify lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point six, Westmere University will not accept cloud work without a written trail.

Section twenty-seven point six fails closed if cloud evidence is missing rather than guessing.

### Writing good tests

A good verification test checks one behaviour, uses synthetic inputs, has a clear expected result and cleans up after itself. Tests that leave objects behind can confuse later checks. Samuel writes each test with a name that says what it proves, so a failure message is immediately understandable. He also includes one positive test for each control, checking that compliant actions still succeed, because a control that blocks everything would pass the negative tests while breaking the service.

### Worked example

Running the same tests in production's dedicated test namespace, all five pass. Samuel notes that verification in one namespace does not prove every namespace is labelled correctly, which is why the label check across namespaces was added.

> **Synthetic case.** Tests are synthetic.

### Errors and limits

A passing test shows one case works; coverage of cases matters.

### Exercises

- **EX079 — Lab result.** Which test failed? *Rubric:* 3 = privileged pod admitted; 2 = partial; 1 = none; 0 = none.
- **EX080 — Cause.** What caused the failure? *Rubric:* 3 = namespace missing Restricted label; 2 = partial; 1 = none; 0 = none.
- **EX081 — Coverage point.** Why add a label check across namespaces? *Rubric:* 3 = one namespace test doesn't prove all; 2 = partial; 1 = none; 0 = none.

### Synthesis

Observe behaviour, not just configuration.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Cloud and container security: failure analysis

### Learning outcomes

You will (1) analyse how StudyHub controls could fail; (2) consider technical and human failures; (3) plan detection and recovery for each; (4) prioritise improvements.

### 28.1 Approach

For each important control, ask how it could fail, how failure would be noticed and how service would recover.

Section twenty-eight point one develops cloud and container security failure with a Westmere University note Samuel Osei can demo offline.

Under section twenty-eight point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-eight point one treats approach admission control failure as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point one, Westmere University will not accept cloud work without a written trail.

### 28.2 Admission control failure

If the admission service is down, deployments may be blocked (fail closed) or allowed without checks (fail open). Westmere chooses fail closed for production with alerts and a runbook.

Section twenty-eight point two develops cloud and container security failure with a Westmere University note Samuel Osei can demo offline.

Under section twenty-eight point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-eight point two treats approach admission control failure as testable only when evidence and ticket IDs are recorded.

### 28.3 Identity provider outage

Staff cannot sign in; break-glass accounts allow emergency access.

Section twenty-eight point three develops cloud and container security failure with a Westmere University note Samuel Osei can demo offline.

Under section twenty-eight point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-eight point three treats approach admission control failure as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point three, Westmere University will not accept cloud work without a written trail.

Section twenty-eight point three fails closed if cloud evidence is missing rather than guessing.

### 28.4 Logging failure

If log delivery stops, an alert fires when no logs arrive for 30 minutes.

Section twenty-eight point four develops cloud and container security failure with a Westmere University note Samuel Osei can demo offline.

Under section twenty-eight point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-eight point four treats approach admission control failure as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point four, Westmere University will not accept cloud work without a written trail.

### 28.5 Human failures

A rushed console change during an incident; a mistaken guardrail exception. Controls: changes through code where possible, exceptions with expiry.

Section twenty-eight point five develops cloud and container security failure with a Westmere University note Samuel Osei can demo offline.

Under section twenty-eight point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-eight point five treats approach admission control failure as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point five, Westmere University will not accept cloud work without a written trail.

### 28.6 Prioritising

Failures that would be silent rank highest, because they can last long unnoticed, as in the opening case.

Section twenty-eight point six develops cloud and container security failure with a Westmere University note Samuel Osei can demo offline.

Under section twenty-eight point six, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-eight point six treats approach admission control failure as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point six, Westmere University will not accept cloud work without a written trail.

### 28.7 Exercises

Failure scenarios are rehearsed in the test environment each term.

Section twenty-eight point seven develops cloud and container security failure with a Westmere University note Samuel Osei can demo offline.

Under section twenty-eight point seven, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-eight point seven treats approach admission control failure as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point seven, Westmere University will not accept cloud work without a written trail.

Section twenty-eight point seven fails closed if cloud evidence is missing rather than guessing.

### Failure table

The analysis is kept as a table: control, failure mode, how it would be noticed, recovery steps and owner. Silent failure modes are highlighted. The table is reviewed each term and after incidents, and rehearsals pick scenarios from it. Samuel finds that writing the 'how would we notice' column was the most revealing part, because for four failure modes the honest answer was 'we would not', and each of those became an improvement item with a date.

### Owners

Each failure mode has an owner who checks its detection works.

### Worked example

The analysis finds that if the secret scanner in the pipeline crashed, builds would continue without scanning and nobody would notice. The pipeline is changed so that a scanner error fails the build, and a weekly report shows scan counts.

> **Synthetic case.** Scenarios are synthetic.

### Errors and limits

Fail-closed choices create availability risks; make the control itself reliable.

### Exercises

- **EX082 — Fail closed.** What does fail closed mean for admission? *Rubric:* 3 = deployments blocked if service down; 2 = partial; 1 = none; 0 = none.
- **EX083 — Silent failures.** Why do silent failures rank highest? *Rubric:* 3 = last long unnoticed; 2 = partial; 1 = none; 0 = none.
- **EX084 — Scanner fix.** How was the scanner failure addressed? *Rubric:* 3 = scanner error fails build; weekly counts; 2 = partial; 1 = none; 0 = none.

### Synthesis

Plan for controls failing, especially silently.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Cloud and container security: operations

### Learning outcomes

You will (1) run day-to-day cloud security operations; (2) measure alert quality and response time; (3) tune alerts; (4) keep runbooks current.

### 29.1 Daily work

The cloud team reviews alerts, check results and exception expiries daily.

Section twenty-nine point one develops cloud and container security operations with a Westmere University note Samuel Osei can demo offline.

Under section twenty-nine point one, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-nine point one treats daily work lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point one, Westmere University will not accept cloud work without a written trail.

Section twenty-nine point one fails closed if cloud evidence is missing rather than guessing.

### Lab — Lab — alert handling

```python
"""Summarise synthetic alert handling: count, actionable share and median minutes to acknowledge (stdlib only)."""
import statistics
alerts = [("public-access-change", True, 6), ("public-access-change", True, 9), ("new-access-key", True, 14),
          ("new-access-key", False, 30), ("login-new-country", False, 45), ("login-new-country", False, 60),
          ("login-new-country", False, 38), ("logging-disabled", True, 4)]
rules = sorted({a[0] for a in alerts})
for r in rules:
    x = [a for a in alerts if a[0] == r]
    print(f"{r:21} n {len(x)}, actionable {sum(a[1] for a in x)}/{len(x)}, median ack {statistics.median(a[2] for a in x)} min")
```

Run with `python3 lab_alerts.py`. Verified output:

```text
logging-disabled      n 1, actionable 1/1, median ack 4 min
login-new-country     n 3, actionable 0/3, median ack 45 min
new-access-key        n 2, actionable 1/2, median ack 22.0 min
public-access-change  n 2, actionable 2/2, median ack 7.5 min
```

### 29.2 Lab result

logging-disabled: 1 alert, 1 actionable, median 4 minutes to acknowledge. public-access-change: 2 alerts, both actionable, median 7.5 minutes. new-access-key: 2 alerts, 1 actionable, median 22.0 minutes. login-new-country: 3 alerts, none actionable, median 45 minutes. Alerts that are never actionable get slow responses, which risks slow responses to real ones too.

Section twenty-nine point two develops cloud and container security operations with a Westmere University note Samuel Osei can demo offline.

Under section twenty-nine point two, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-nine point two treats daily work lab result as testable only when evidence and ticket IDs are recorded.

### 29.3 Tuning

login-new-country fires for staff at conferences; it is tuned to exclude known travel from the identity provider's records and to raise severity only for administrator roles.

Section twenty-nine point three develops cloud and container security operations with a Westmere University note Samuel Osei can demo offline.

Under section twenty-nine point three, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-nine point three treats daily work lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point three, Westmere University will not accept cloud work without a written trail.

### 29.4 Runbooks

Each alert links to a runbook; runbooks are updated after each real alert.

Section twenty-nine point four develops cloud and container security operations with a Westmere University note Samuel Osei can demo offline.

Under section twenty-nine point four, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-nine point four treats daily work lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point four, Westmere University will not accept cloud work without a written trail.

### 29.5 Measuring

Monthly: alerts by rule, actionable share and acknowledgement time.

Section twenty-nine point five develops cloud and container security operations with a Westmere University note Samuel Osei can demo offline.

Under section twenty-nine point five, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-nine point five treats daily work lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point five, Westmere University will not accept cloud work without a written trail.

Section twenty-nine point five fails closed if cloud evidence is missing rather than guessing.

### 29.6 Workload

Tuning keeps total alerts manageable for a small team.

Section twenty-nine point six develops cloud and container security operations with a Westmere University note Samuel Osei can demo offline.

Under section twenty-nine point six, Tom Becker expects cloud claims to carry owners and dates.

Section twenty-nine point six treats daily work lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point six, Westmere University will not accept cloud work without a written trail.

Section twenty-nine point six fails closed if cloud evidence is missing rather than guessing.

### Runbook quality

A runbook states what the alert means, how to check whether it is real, what to do first, who to tell and how to close it. Runbooks are short enough to read during an incident. After each real alert, the responder notes what was unclear, and the runbook is updated within a week. Samuel reviews all runbooks once and finds three still referring to an old ticket system, which are corrected. He also adds a 'last tested' date to each runbook, so stale ones are easy to spot.

### Handover notes

At the end of each day, the person on duty writes a short note of open alerts and actions so the next person starts with full context. Notes are kept for a month.

### Worked example

After tuning, login-new-country alerts drop from about 40 a month to 3, and median acknowledgement for all alerts falls below 10 minutes.

> **Synthetic case.** Alerts are synthetic.

### Errors and limits

Tuning can hide real events; review tuned rules periodically.

### Exercises

- **EX085 — Lab worst rule.** Which rule was least actionable? *Rubric:* 3 = login-new-country 0/3; 2 = partial; 1 = none; 0 = none.
- **EX086 — Why it matters.** Why do non-actionable alerts matter? *Rubric:* 3 = slow responses spread; 2 = partial; 1 = none; 0 = none.
- **EX087 — Tuning result.** What did tuning achieve? *Rubric:* 3 = 40 to 3 a month; ack under 10 min; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure alert quality and tune for action.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) run a combined verification and operations lab; (2) inject synthetic events; (3) observe detection and response; (4) report results.

### 30.1 Setup

In the test account, the lab injects synthetic events: a public access change, a new access key, a privileged pod request and a logging disablement attempt.

Section thirty point one develops laboratory ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty point one, Tom Becker expects laboratory claims to carry owners and dates.

Section thirty point one treats setup expectations observing results as testable only when evidence and ticket IDs are recorded.

For section thirty point one, Westmere University will not accept laboratory work without a written trail.

### 30.2 Expectations

The guardrail blocks the public change and logging disablement; admission rejects the privileged pod; alerts fire for the key and the attempts.

Section thirty point two develops laboratory ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty point two, Tom Becker expects laboratory claims to carry owners and dates.

Section thirty point two treats setup expectations observing results as testable only when evidence and ticket IDs are recorded.

For section thirty point two, Westmere University will not accept laboratory work without a written trail.

### 30.3 Observing

Students record when each event happened, whether it was blocked, when alerts arrived and whether the runbook worked.

Section thirty point three develops laboratory ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty point three, Tom Becker expects laboratory claims to carry owners and dates.

Section thirty point three treats setup expectations observing results as testable only when evidence and ticket IDs are recorded.

For section thirty point three, Westmere University will not accept laboratory work without a written trail.

### 30.4 Results

All events are blocked or detected; the new-key alert takes 18 minutes, slower than the 15-minute target, because it waits for a batch log export.

Section thirty point four develops laboratory ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty point four, Tom Becker expects laboratory claims to carry owners and dates.

Section thirty point four treats setup expectations observing results as testable only when evidence and ticket IDs are recorded.

For section thirty point four, Westmere University will not accept laboratory work without a written trail.

### 30.5 Report

A short report with timings, a comparison with targets and recommendations.

Section thirty point five develops laboratory ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty point five, Tom Becker expects laboratory claims to carry owners and dates.

Section thirty point five treats setup expectations observing results as testable only when evidence and ticket IDs are recorded.

For section thirty point five, Westmere University will not accept laboratory work without a written trail.

Section thirty point five fails closed if laboratory evidence is missing rather than guessing.

### 30.6 Safety

Synthetic events only, in a test account, with the cloud team present.

Section thirty point six develops laboratory ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty point six, Tom Becker expects laboratory claims to carry owners and dates.

Section thirty point six treats setup expectations observing results as testable only when evidence and ticket IDs are recorded.

For section thirty point six, Westmere University will not accept laboratory work without a written trail.

Section thirty point six fails closed if laboratory evidence is missing rather than guessing.

### 30.7 Reflection

Students discuss which detections they would trust in production.

Section thirty point seven develops laboratory ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty point seven, Tom Becker expects laboratory claims to carry owners and dates.

Section thirty point seven treats setup expectations observing results as testable only when evidence and ticket IDs are recorded.

For section thirty point seven, Westmere University will not accept laboratory work without a written trail.

Section thirty point seven fails closed if laboratory evidence is missing rather than guessing.

### Lab roles

Each group has a coordinator who injects events, an observer who records timings and a responder who follows the runbooks. Roles rotate between rounds so everyone experiences each. Having a separate observer makes the timings reliable, because the responder is busy. The cloud team sits in to answer questions about the platform and to make sure no injected event touches anything outside the test account.

### Comparing groups

Groups compare their timings and runbook notes afterwards. Differences in how quickly groups confirmed alerts lead to a clearer first step in two runbooks.

### Clean-up

After the lab, injected objects are removed and the test account is checked for leftovers.

### Worked example

Samuel's group recommends moving key-creation alerts to the real-time event stream instead of batch export. Tom tests it the following week; alerts now arrive in under 2 minutes.

> **Synthetic case.** Lab events are synthetic.

### Errors and limits

Test accounts may differ from production in log delivery; check both.

### Exercises

- **EX088 — Injected events.** List the injected events. *Rubric:* 3 = public change, new key, privileged pod, logging disable; 2 = three; 1 = one; 0 = none.
- **EX089 — Slow alert.** Which alert was slow and why? *Rubric:* 3 = new key, 18 min, batch export; 2 = partial; 1 = none; 0 = none.
- **EX090 — Fix.** What fixed it? *Rubric:* 3 = real-time event stream; 2 = partial; 1 = none; 0 = none.

### Synthesis

Inject safe events to test detection and response end to end.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Cloud and container security: advanced cases

### Learning outcomes

You will (1) analyse complex cloud and container scenarios involving several weaknesses; (2) trace how small issues combine; (3) design layered fixes; (4) communicate complex findings.

### 31.1 Combining weaknesses

Serious incidents often combine several small issues. In a synthetic case, a developer's laptop token with broad rights, a pipeline role that can assume an administrator role and missing alerting on role assumptions together allow an unreviewed change to production.

Section thirty-one point one develops cloud and container security advanced with a Westmere University note Samuel Osei can demo offline.

Under section thirty-one point one, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-one point one treats combining weaknesses tracing chains as testable only when evidence and ticket IDs are recorded.

### 31.2 Tracing chains

Samuel uses the role graph (chapter 6), the model (chapter 21) and logs to trace each step. Each link is a separate fix opportunity.

Section thirty-one point two develops cloud and container security advanced with a Westmere University note Samuel Osei can demo offline.

Under section thirty-one point two, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-one point two treats combining weaknesses tracing chains as testable only when evidence and ticket IDs are recorded.

For section thirty-one point two, Westmere University will not accept cloud work without a written trail.

### 31.3 Layered fixes

Short-lived developer tokens; narrowed pipeline role; alerts on administrator role assumption; required review for production changes. Any one breaks the chain; all together make it robust.

Section thirty-one point three develops cloud and container security advanced with a Westmere University note Samuel Osei can demo offline.

Under section thirty-one point three, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-one point three treats combining weaknesses tracing chains as testable only when evidence and ticket IDs are recorded.

For section thirty-one point three, Westmere University will not accept cloud work without a written trail.

### 31.4 Container case

A second synthetic case: a privileged debug pod left running with a host path mount, plus no network policies, plus a service account token mounted by default. Fixes: Restricted pod security, default-deny policies, no automatic token mounting where not needed.

Section thirty-one point four develops cloud and container security advanced with a Westmere University note Samuel Osei can demo offline.

Under section thirty-one point four, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-one point four treats combining weaknesses tracing chains as testable only when evidence and ticket IDs are recorded.

### 31.5 Communicating

Complex findings are explained as a short story with a diagram, then a table of fixes with owners.

Section thirty-one point five develops cloud and container security advanced with a Westmere University note Samuel Osei can demo offline.

Under section thirty-one point five, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-one point five treats combining weaknesses tracing chains as testable only when evidence and ticket IDs are recorded.

For section thirty-one point five, Westmere University will not accept cloud work without a written trail.

### 31.6 Avoiding blame

The cases show system weaknesses, not individual failure.

Section thirty-one point six develops cloud and container security advanced with a Westmere University note Samuel Osei can demo offline.

Under section thirty-one point six, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-one point six treats combining weaknesses tracing chains as testable only when evidence and ticket IDs are recorded.

For section thirty-one point six, Westmere University will not accept cloud work without a written trail.

Section thirty-one point six fails closed if cloud evidence is missing rather than guessing.

### Teaching through cases

Samuel presents both cases to the cloud team as short stories, then asks the team to find the links in StudyHub. Working on their own system makes the lessons concrete, and the team finds the unused token mounts themselves with his script. The session takes an hour and produces four backlog items.

### Worked example

Applying the container case to StudyHub, Samuel finds 14 pods that mount service account tokens they never use. Turning off automatic mounting for those pods removes credentials that could have been misused if any pod were compromised.

> **Synthetic case.** Cases are synthetic.

### Errors and limits

Fixing one link is good; fixing several protects against unknown links.

### Exercises

- **EX091 — Chain parts.** List the three weaknesses in the first case. *Rubric:* 3 = broad laptop token, pipeline role to admin, no alerting; 2 = two; 1 = one; 0 = none.
- **EX092 — Container fixes.** Name two fixes for the container case. *Rubric:* 3 = Restricted, default-deny, no auto token; 2 = one; 1 = none; 0 = none.
- **EX093 — StudyHub finding.** What did Samuel find in StudyHub? *Rubric:* 3 = 14 pods mounting unused tokens; 2 = partial; 1 = none; 0 = none.

### Synthesis

Trace chains of weaknesses and break several links.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Cloud and container security: interdisciplinary interfaces

### Learning outcomes

You will (1) work with law, finance, teaching staff and students on cloud security decisions; (2) translate between disciplines; (3) balance competing needs.

### 32.1 Legal and privacy

The data protection officer needs to know where student data is stored and how breaches would be detected. Samuel provides the data map and logging coverage.

Section thirty-two point one develops cloud and container security interdisciplinary with a Westmere University note Samuel Osei can demo offline.

Under section thirty-two point one, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-two point one treats legal and privacy finance as testable only when evidence and ticket IDs are recorded.

For section thirty-two point one, Westmere University will not accept cloud work without a written trail.

### 32.2 Finance

Cloud costs are visible per account. Security controls such as logging have costs; Samuel estimates log storage cost and shows retention choices that balance cost and evidence.

Section thirty-two point two develops cloud and container security interdisciplinary with a Westmere University note Samuel Osei can demo offline.

Under section thirty-two point two, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-two point two treats legal and privacy finance as testable only when evidence and ticket IDs are recorded.

For section thirty-two point two, Westmere University will not accept cloud work without a written trail.

### 32.3 Teaching staff

Lecturers want research sandboxes with freedom to experiment. Guardrails protect against public data exposure without blocking experiments.

Section thirty-two point three develops cloud and container security interdisciplinary with a Westmere University note Samuel Osei can demo offline.

Under section thirty-two point three, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-two point three treats legal and privacy finance as testable only when evidence and ticket IDs are recorded.

For section thirty-two point three, Westmere University will not accept cloud work without a written trail.

### 32.4 Students

Students expect StudyHub to be available during deadlines. Changes are scheduled away from submission peaks.

Section thirty-two point four develops cloud and container security interdisciplinary with a Westmere University note Samuel Osei can demo offline.

Under section thirty-two point four, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-two point four treats legal and privacy finance as testable only when evidence and ticket IDs are recorded.

For section thirty-two point four, Westmere University will not accept cloud work without a written trail.

### 32.5 Translating

Each audience gets the same facts in its own terms: risk to students, legal duty, cost, teaching impact.

Section thirty-two point five develops cloud and container security interdisciplinary with a Westmere University note Samuel Osei can demo offline.

Under section thirty-two point five, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-two point five treats legal and privacy finance as testable only when evidence and ticket IDs are recorded.

For section thirty-two point five, Westmere University will not accept cloud work without a written trail.

### 32.6 Decisions

Conflicts, such as a research group wanting public datasets, go to a small governance group with a documented decision.

Section thirty-two point six develops cloud and container security interdisciplinary with a Westmere University note Samuel Osei can demo offline.

Under section thirty-two point six, Tom Becker expects cloud claims to carry owners and dates.

Section thirty-two point six treats legal and privacy finance as testable only when evidence and ticket IDs are recorded.

For section thirty-two point six, Westmere University will not accept cloud work without a written trail.

### Governance group

The governance group meets monthly with the cloud lead, the data protection officer, a finance representative, an academic and a student representative. It decides exceptions and trade-offs that cross disciplines, records each decision with its reasons, and reviews earlier decisions when circumstances change. Samuel attends as an observer and drafts the papers for two meetings, learning how to present technical options to non-technical members in plain terms with clear choices.

### Plain language

Papers use plain language, with technical terms defined once.

### Worked example

A research group asks for a public bucket to share an open dataset. The governance group approves a dedicated account for public data, with only the open dataset in it and a review of contents before publishing, keeping public data separate from everything else.

> **Synthetic case.** People and decisions are synthetic.

### Errors and limits

Translating risk across disciplines can lose nuance; check understanding.

### Exercises

- **EX094 — DPO needs.** What does the DPO need? *Rubric:* 3 = data location and breach detection; 2 = partial; 1 = none; 0 = none.
- **EX095 — Scheduling.** How are student needs respected? *Rubric:* 3 = changes away from deadline peaks; 2 = partial; 1 = none; 0 = none.
- **EX096 — Public dataset.** How was the public dataset request handled? *Rubric:* 3 = dedicated public-data account with review; 2 = partial; 1 = none; 0 = none.

### Synthesis

Cloud security decisions involve many disciplines; translate carefully.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) plan a more rigorous study; (2) compare groups fairly; (3) use reliable labels; (4) consider validity threats.

### 33.1 Question

Samuel asks whether teams that adopted the shared namespace template had fewer configuration findings per service than teams that did not, over one term.

Section thirty-three point one develops research methods ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty-three point one, Tom Becker expects research claims to carry owners and dates.

Section thirty-three point one treats question design labels results as testable only when evidence and ticket IDs are recorded.

For section thirty-three point one, Westmere University will not accept research work without a written trail.

### 33.2 Design

Compare 12 adopting services with 12 non-adopting services of similar size and age, matching pairs to reduce confounding.

Section thirty-three point two develops research methods ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty-three point two, Tom Becker expects research claims to carry owners and dates.

Section thirty-three point two treats question design labels results as testable only when evidence and ticket IDs are recorded.

For section thirty-three point two, Westmere University will not accept research work without a written trail.

### 33.3 Labels

Findings are labelled real or not by two reviewers independently; agreement is checked with Cohen's kappa, interpreted with Landis and Koch's (1977) bands.

Section thirty-three point three develops research methods ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty-three point three, Tom Becker expects research claims to carry owners and dates.

Section thirty-three point three treats question design labels results as testable only when evidence and ticket IDs are recorded.

For section thirty-three point three, Westmere University will not accept research work without a written trail.

### 33.4 Results

Median findings per service: 1 for adopters, 4 for non-adopters. Reviewer kappa is 0.82, almost perfect agreement.

Section thirty-three point four develops research methods ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty-three point four, Tom Becker expects research claims to carry owners and dates.

Section thirty-three point four treats question design labels results as testable only when evidence and ticket IDs are recorded.

For section thirty-three point four, Westmere University will not accept research work without a written trail.

### 33.5 Validity

Teams chose whether to adopt; more careful teams may adopt first. Matching helps but cannot remove this. One term is short.

Section thirty-three point five develops research methods ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty-three point five, Tom Becker expects research claims to carry owners and dates.

Section thirty-three point five treats question design labels results as testable only when evidence and ticket IDs are recorded.

For section thirty-three point five, Westmere University will not accept research work without a written trail.

### 33.6 Reporting

Results with limits, plus a recommendation to offer the template to all teams and re-measure.

Section thirty-three point six develops research methods ii with a Westmere University note Samuel Osei can demo offline.

Under section thirty-three point six, Tom Becker expects research claims to carry owners and dates.

Section thirty-three point six treats question design labels results as testable only when evidence and ticket IDs are recorded.

For section thirty-three point six, Westmere University will not accept research work without a written trail.

### Choosing pairs

Pairs are matched on number of containers, age of the service and team size, using records from the cloud team. Samuel writes the matching rules before looking at findings so the choice of pairs cannot be influenced by results. Two services have no good match and are excluded, which he reports. He also checks that both groups had similar numbers of deployments over the term, since more changes could mean more findings regardless of the template, and finds the counts close.

### Sharing data

The matched-pair table and labels are kept with the analysis script so another student could rerun the comparison and check the result.

### Ethics note

Findings are reported by service pair, never by person or team name.

### Worked example

Dr Jensen asks whether reviewers knew which services used the template. They did; Samuel repeats the labelling on a sample with service names hidden and gets the same kappa, reducing concern about bias.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Matching reduces some differences but not unmeasured ones.

### Exercises

- **EX097 — Design.** How were groups compared? *Rubric:* 3 = 12 vs 12 matched pairs; 2 = partial; 1 = none; 0 = none.
- **EX098 — Results.** What were medians and kappa? *Rubric:* 3 = 1 vs 4; kappa 0.82; 2 = partial; 1 = none; 0 = none.
- **EX099 — Blind check.** How was reviewer bias checked? *Rubric:* 3 = relabel with names hidden; 2 = partial; 1 = none; 0 = none.

### Synthesis

Fair comparisons and reliable labels make findings credible.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two approaches to a cloud security problem; (2) define criteria; (3) test both on synthetic data; (4) recommend with evidence.

### 34.1 The problem

How should Westmere detect public storage and registry exposure: periodic scanning of configuration, or real-time alerts on configuration change events?

Section thirty-four point one develops comparative project with a Westmere University note Samuel Osei can demo offline.

Under section thirty-four point one, Tom Becker expects comparative claims to carry owners and dates.

Section thirty-four point one treats the problem criteria testing as testable only when evidence and ticket IDs are recorded.

For section thirty-four point one, Westmere University will not accept comparative work without a written trail.

### 34.2 Criteria

Time to detect, false alerts, cost, coverage of resources created outside code, and effort to maintain.

Section thirty-four point two develops comparative project with a Westmere University note Samuel Osei can demo offline.

Under section thirty-four point two, Tom Becker expects comparative claims to carry owners and dates.

Section thirty-four point two treats the problem criteria testing as testable only when evidence and ticket IDs are recorded.

For section thirty-four point two, Westmere University will not accept comparative work without a written trail.

### 34.3 Testing

In a test account, Samuel creates 20 synthetic exposure events at random times. Periodic scanning every 24 hours detects all 20 with a median delay of 11 hours. Event-based alerts detect 19 with a median delay of 2 minutes; one is missed because that resource type does not emit the event used.

Section thirty-four point three develops comparative project with a Westmere University note Samuel Osei can demo offline.

Under section thirty-four point three, Tom Becker expects comparative claims to carry owners and dates.

Section thirty-four point three treats the problem criteria testing as testable only when evidence and ticket IDs are recorded.

### 34.4 Comparison

Event alerts are much faster but miss some types; scanning is complete but slow.

Section thirty-four point four develops comparative project with a Westmere University note Samuel Osei can demo offline.

Under section thirty-four point four, Tom Becker expects comparative claims to carry owners and dates.

Section thirty-four point four treats the problem criteria testing as testable only when evidence and ticket IDs are recorded.

For section thirty-four point four, Westmere University will not accept comparative work without a written trail.

Section thirty-four point four fails closed if comparative evidence is missing rather than guessing.

### 34.5 Recommendation

Use both: event alerts for speed, daily scanning as a safety net, plus prevention through guardrails so most events never happen.

Section thirty-four point five develops comparative project with a Westmere University note Samuel Osei can demo offline.

Under section thirty-four point five, Tom Becker expects comparative claims to carry owners and dates.

Section thirty-four point five treats the problem criteria testing as testable only when evidence and ticket IDs are recorded.

For section thirty-four point five, Westmere University will not accept comparative work without a written trail.

### 34.6 Cost

Both use built-in services; cost is mainly setup time.

Section thirty-four point six develops comparative project with a Westmere University note Samuel Osei can demo offline.

Under section thirty-four point six, Tom Becker expects comparative claims to carry owners and dates.

Section thirty-four point six treats the problem criteria testing as testable only when evidence and ticket IDs are recorded.

For section thirty-four point six, Westmere University will not accept comparative work without a written trail.

Section thirty-four point six fails closed if comparative evidence is missing rather than guessing.

### Writing the comparison

The report presents a table of criteria with results for each approach and a short paragraph on each criterion. Samuel avoids declaring an overall winner, since the approaches complement each other; instead he shows what each contributes. Tom finds this more useful than a single recommendation, because it explains why both are kept and which one to rely on for each kind of risk. The test scripts and synthetic events are kept so the comparison can be repeated after platform changes.

### Repeat plan

The comparison will be repeated after any change to logging or event sources.

### Limits noted

The test account lacked some production services.

### Worked example

The missed event type is reported to the cloud team, who add a second event source for it. A rerun detects all 20 events in under 5 minutes.

> **Synthetic case.** Tests and figures are synthetic.

### Errors and limits

Test accounts may not represent all production behaviours.

### Exercises

- **EX100 — Two approaches.** What two approaches were compared? *Rubric:* 3 = periodic scanning vs event alerts; 2 = partial; 1 = none; 0 = none.
- **EX101 — Results.** Give the median delays. *Rubric:* 3 = scan 11 h; events 2 min; 2 = partial; 1 = none; 0 = none.
- **EX102 — Recommendation.** What was recommended? *Rubric:* 3 = both, plus guardrails; 2 = partial; 1 = none; 0 = none.

### Synthesis

Compare approaches on clear criteria with tests.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) propose a capstone that improves StudyHub's cloud security; (2) define scope, method and success criteria; (3) identify risks; (4) obtain approval.

### 35.1 Proposal

Samuel proposes a "cloud posture report" for StudyHub: a weekly automated report combining registry, identity, logging, benchmark and pod security checks, with trends and owners, plus a secret scan in the build pipeline.

Section thirty-five point one develops capstone proposal with a Westmere University note Samuel Osei can demo offline.

Under section thirty-five point one, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-five point one treats proposal motivation scope success as testable only when evidence and ticket IDs are recorded.

### 35.2 Motivation

The opening case showed that no single view existed; the report gives one, and the scan addresses the root cause.

Section thirty-five point two develops capstone proposal with a Westmere University note Samuel Osei can demo offline.

Under section thirty-five point two, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-five point two treats proposal motivation scope success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point two, Westmere University will not accept capstone work without a written trail.

### 35.3 Scope

Read-only checks over exports; pipeline scan; report generation. Out of scope: automatic fixing.

Section thirty-five point three develops capstone proposal with a Westmere University note Samuel Osei can demo offline.

Under section thirty-five point three, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-five point three treats proposal motivation scope success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point three, Westmere University will not accept capstone work without a written trail.

Section thirty-five point three fails closed if capstone evidence is missing rather than guessing.

### 35.4 Success criteria

All five check families running weekly; zero anonymous repositories; logging 6 of 6; findings median age under 14 days by term end; scan blocking any key-like string except allowed placeholders.

Section thirty-five point four develops capstone proposal with a Westmere University note Samuel Osei can demo offline.

Under section thirty-five point four, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-five point four treats proposal motivation scope success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point four, Westmere University will not accept capstone work without a written trail.

### 35.5 Risks

Noise leading to ignored reports; scanner false positives blocking builds.

Section thirty-five point five develops capstone proposal with a Westmere University note Samuel Osei can demo offline.

Under section thirty-five point five, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-five point five treats proposal motivation scope success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point five, Westmere University will not accept capstone work without a written trail.

Section thirty-five point five fails closed if capstone evidence is missing rather than guessing.

### 35.6 Mitigations

Owners and severity in the report; reviewed allow list for test placeholders.

Section thirty-five point six develops capstone proposal with a Westmere University note Samuel Osei can demo offline.

Under section thirty-five point six, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-five point six treats proposal motivation scope success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point six, Westmere University will not accept capstone work without a written trail.

Section thirty-five point six fails closed if capstone evidence is missing rather than guessing.

### 35.7 Approval

Tom and Dr Jensen approve, with Tom's team owning the report afterwards.

Section thirty-five point seven develops capstone proposal with a Westmere University note Samuel Osei can demo offline.

Under section thirty-five point seven, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-five point seven treats proposal motivation scope success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point seven, Westmere University will not accept capstone work without a written trail.

Section thirty-five point seven fails closed if capstone evidence is missing rather than guessing.

### Plan and timeline

The capstone runs over ten weeks: two weeks design, four implementation, two verification, two documentation and handover. Weekly check-ins with Tom keep it aligned with the cloud team's priorities. A risk log tracks issues such as delays in getting exports. Samuel builds in a buffer week, which he later needs when an export format changes. He also schedules a mid-point demonstration to developers to collect feedback while there is still time to act on it.

### Supervision

Dr Jensen reviews progress fortnightly against the plan.

### Handover owner

Tom's team names an owner for the report before work begins.

### Worked example

Dr Jensen asks Samuel to state what he will not claim: the report shows configuration state, not that StudyHub cannot be attacked. Samuel adds this to the proposal's limits section.

> **Synthetic case.** Proposal is synthetic.

### Errors and limits

Capstones should solve a real problem, not showcase tools.

### Exercises

- **EX103 — Capstone.** What is the capstone? *Rubric:* 3 = weekly posture report plus pipeline secret scan; 2 = partial; 1 = none; 0 = none.
- **EX104 — Criteria.** Name two success criteria. *Rubric:* 3 = weekly checks, no anonymous repos, logging 6/6, median <14 d, scan blocks keys; 2 = one; 1 = none; 0 = none.
- **EX105 — Limit stated.** What will Samuel not claim? *Rubric:* 3 = that StudyHub cannot be attacked; 2 = partial; 1 = none; 0 = none.

### Synthesis

A good capstone solves a real problem with clear criteria and limits.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) apply cloud security skills in a community setting; (2) adapt methods for small organisations; (3) communicate with non-specialists; (4) reflect on practice.

### 36.1 The placement

Samuel volunteers for four weeks with a fictional local charity, Harbourside Youth Trust, which runs a small booking app on a cloud platform with one part-time IT volunteer.

Section thirty-six point one develops field or community practice with a Westmere University note Samuel Osei can demo offline.

Under section thirty-six point one, Tom Becker expects field claims to carry owners and dates.

Section thirty-six point one treats the placement adapting methods as testable only when evidence and ticket IDs are recorded.

For section thirty-six point one, Westmere University will not accept field work without a written trail.

### 36.2 Adapting methods

The full university checklist is too much. Samuel picks five checks that matter most for a small account: owner MFA, no owner keys, storage public access blocked, audit logging on, and budget alerts.

Section thirty-six point two develops field or community practice with a Westmere University note Samuel Osei can demo offline.

Under section thirty-six point two, Tom Becker expects field claims to carry owners and dates.

Section thirty-six point two treats the placement adapting methods as testable only when evidence and ticket IDs are recorded.

### 36.3 Findings

Owner MFA was off; a storage bucket of event photos was public; logging was off. Keys and budgets were fine.

Section thirty-six point three develops field or community practice with a Westmere University note Samuel Osei can demo offline.

Under section thirty-six point three, Tom Becker expects field claims to carry owners and dates.

Section thirty-six point three treats the placement adapting methods as testable only when evidence and ticket IDs are recorded.

For section thirty-six point three, Westmere University will not accept field work without a written trail.

### 36.4 Fixes

With the trustees' written permission, the volunteer turns on MFA, blocks public access after moving the intended public photos to the website, and enables logging. Samuel guides; the volunteer makes the changes.

Section thirty-six point four develops field or community practice with a Westmere University note Samuel Osei can demo offline.

Under section thirty-six point four, Tom Becker expects field claims to carry owners and dates.

Section thirty-six point four treats the placement adapting methods as testable only when evidence and ticket IDs are recorded.

### 36.5 Communication

Samuel explains risks in terms of children's photos and the charity's reputation, not technical jargon.

Section thirty-six point five develops field or community practice with a Westmere University note Samuel Osei can demo offline.

Under section thirty-six point five, Tom Becker expects field claims to carry owners and dates.

Section thirty-six point five treats the placement adapting methods as testable only when evidence and ticket IDs are recorded.

For section thirty-six point five, Westmere University will not accept field work without a written trail.

### 36.6 Reflection

Small organisations need short, prioritised advice and someone to help them act on it.

Section thirty-six point six develops field or community practice with a Westmere University note Samuel Osei can demo offline.

Under section thirty-six point six, Tom Becker expects field claims to carry owners and dates.

Section thirty-six point six treats the placement adapting methods as testable only when evidence and ticket IDs are recorded.

For section thirty-six point six, Westmere University will not accept field work without a written trail.

### Leaving it sustainable

Before leaving, Samuel writes a one-page guide for the charity volunteer: the five checks, how to do each in the console, and how often. He also sets a calendar reminder for the trustees to review who has owner access every six months. The guide uses screenshots described in words so it survives interface changes. The volunteer tries every step while Samuel watches, so the guide is proven to work for the person who will use it.

### Worked example

Three months later the volunteer emails that a budget alert caught an accidentally left-running test machine, saving a month's costs. The charity asks Westmere for a yearly check, which becomes a student volunteering scheme.

> **Synthetic case.** The charity and events are synthetic.

### Errors and limits

Advice must match the organisation's capacity or it will not be followed.

### Exercises

- **EX106 — Five checks.** List the five checks. *Rubric:* 3 = owner MFA, no owner keys, public access blocked, logging, budget alerts; 2 = four; 1 = two; 0 = none.
- **EX107 — Findings.** What did Samuel find? *Rubric:* 3 = MFA off, public bucket, logging off; 2 = two; 1 = one; 0 = none.
- **EX108 — Who changes.** Who made the changes? *Rubric:* 3 = the volunteer, with permission; 2 = partial; 1 = none; 0 = none.

### Synthesis

Adapt methods to the organisation's size and capacity.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critically review evidence used in cloud security claims; (2) assess vendor reports, studies and internal data; (3) present a critique.

### 37.1 Purpose

Students bring a claim from a source and assess its evidence: who made it, what data, what method, what limits.

Section thirty-seven point one develops evidence review seminar with a Westmere University note Samuel Osei can demo offline.

Under section thirty-seven point one, Tom Becker expects evidence claims to carry owners and dates.

Section thirty-seven point one treats purpose example claim research as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point one, Westmere University will not accept evidence work without a written trail.

### 37.2 Example claim

A vendor report states that "most cloud breaches are caused by misconfiguration". Samuel checks: the report's data come from the vendor's customers, the definition of breach is broad and the method is not described. The claim is plausible and consistent with research on configuration errors (Rahman et al., 2019), but the specific percentage is weakly supported.

Section thirty-seven point two develops evidence review seminar with a Westmere University note Samuel Osei can demo offline.

Under section thirty-seven point two, Tom Becker expects evidence claims to carry owners and dates.

### 37.3 Research example

Shu, Gu and Enck (2017) analysed real Docker Hub images with a described method; their findings are stronger evidence for image vulnerability prevalence at that time.

Section thirty-seven point three develops evidence review seminar with a Westmere University note Samuel Osei can demo offline.

Under section thirty-seven point three, Tom Becker expects evidence claims to carry owners and dates.

Section thirty-seven point three treats purpose example claim research as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point three, Westmere University will not accept evidence work without a written trail.

### 37.4 Internal data

Samuel's own studies are reviewed by classmates, who point out the short time frames.

Section thirty-seven point four develops evidence review seminar with a Westmere University note Samuel Osei can demo offline.

Under section thirty-seven point four, Tom Becker expects evidence claims to carry owners and dates.

Section thirty-seven point four treats purpose example claim research as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point four, Westmere University will not accept evidence work without a written trail.

### 37.5 Presenting

Each student gives a ten-minute critique with a verdict: strong, moderate or weak support.

Section thirty-seven point five develops evidence review seminar with a Westmere University note Samuel Osei can demo offline.

Under section thirty-seven point five, Tom Becker expects evidence claims to carry owners and dates.

Section thirty-seven point five treats purpose example claim research as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point five, Westmere University will not accept evidence work without a written trail.

### 37.6 Using evidence

Weak evidence can still guide action if the action is cheap and sensible; it should not be quoted as fact.

Section thirty-seven point six develops evidence review seminar with a Westmere University note Samuel Osei can demo offline.

Under section thirty-seven point six, Tom Becker expects evidence claims to carry owners and dates.

Section thirty-seven point six treats purpose example claim research as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point six, Westmere University will not accept evidence work without a written trail.

### Grading evidence

The seminar uses a simple grid: source type, data described, method described, sample size, conflicts of interest and age. Each criterion scores 0 to 2. The grid does not replace judgement but makes it explicit and comparable. Samuel's grid for the vendor report scores 4 of 12, for Shu et al. 10 of 12 (losing points mainly for age), which matches the seminar's verdicts.

### Reflection

Samuel notes his own studies would score about 7 of 12, mainly for short time frames.

### Worked example

The seminar agrees that the vendor claim should be cited as "a vendor survey reported" rather than as fact. Samuel updates his thesis wording accordingly.

> **Synthetic case.** Seminar content is synthetic; cited papers are real.

### Errors and limits

Even peer-reviewed studies age quickly in fast-changing cloud environments.

### Exercises

- **EX109 — Evidence questions.** What four questions assess evidence? *Rubric:* 3 = who, what data, what method, what limits; 2 = three; 1 = one; 0 = none.
- **EX110 — Vendor claim.** How was the vendor claim judged? *Rubric:* 3 = plausible but weakly supported percentage; 2 = partial; 1 = none; 0 = none.
- **EX111 — Wording.** How was the thesis wording changed? *Rubric:* 3 = "a vendor survey reported"; 2 = partial; 1 = none; 0 = none.

### Synthesis

Judge claims by their evidence, not their confidence.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) build the posture report and pipeline secret scan; (2) test with synthetic data; (3) deploy with the cloud team; (4) handle problems.

### 38.1 Building the report

The report combines the registry, account, logging, benchmark and pod security checks into one weekly document with trends and owners. Each section links to evidence files.

Section thirty-eight point one develops capstone implementation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-eight point one, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-eight point one treats building the report pipeline as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point one, Westmere University will not accept capstone work without a written trail.

### 38.2 Pipeline scan

The build pipeline scans image layers for key-like strings using pattern and entropy rules, failing the build on a match unless the string is in a reviewed placeholder allow list.

Section thirty-eight point two develops capstone implementation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-eight point two, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-eight point two treats building the report pipeline as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point two, Westmere University will not accept capstone work without a written trail.

### 38.3 Testing

Synthetic exports and images with known problems confirm each check works; compliant inputs confirm no false failures.

Section thirty-eight point three develops capstone implementation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-eight point three, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-eight point three treats building the report pipeline as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point three, Westmere University will not accept capstone work without a written trail.

### 38.4 Deployment

The report runs in the shared tooling account with read-only access to exports. The scan is added to the pipeline in warning mode for two weeks, then blocking.

Section thirty-eight point four develops capstone implementation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-eight point four, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-eight point four treats building the report pipeline as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point four, Westmere University will not accept capstone work without a written trail.

### 38.5 Problems

An export format changed mid-project, breaking the identity check; a loader update and test fixed it. Warning mode revealed three test fixtures with realistic-looking fake keys, which were replaced by obvious placeholders.

Section thirty-eight point five develops capstone implementation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-eight point five, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-eight point five treats building the report pipeline as testable only when evidence and ticket IDs are recorded.

### 38.6 Documentation

A guide explains how to read the report and how to request allow-list entries.

Section thirty-eight point six develops capstone implementation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-eight point six, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-eight point six treats building the report pipeline as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point six, Westmere University will not accept capstone work without a written trail.

Section thirty-eight point six fails closed if capstone evidence is missing rather than guessing.

### Code review

Tom's team reviews the report code before it runs in the tooling account, checking that it only reads exports and writes reports, and that no credentials are stored in it. The reviewer suggests separating each check into its own module with tests, which Samuel does. Review also catches that the report printed full resource identifiers that included a student project name; these are shortened to avoid exposing project details in a widely shared document.

### Worked example

In its first blocking week, the scan stops a build containing a real storage access key copied from a developer's notes. The developer removes it and the key is rotated, exactly the kind of event that caused the opening case.

> **Synthetic case.** Implementation details are synthetic.

### Errors and limits

Warning modes that never end become ignored; set a date.

### Exercises

- **EX112 — Report sources.** Which checks feed the report? *Rubric:* 3 = registry, account, logging, benchmark, pod security; 2 = three; 1 = one; 0 = none.
- **EX113 — Warning mode.** What did warning mode reveal? *Rubric:* 3 = realistic fake keys in fixtures; 2 = partial; 1 = none; 0 = none.
- **EX114 — First block.** What did the scan block? *Rubric:* 3 = real key from developer's notes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Build, test and roll out gradually; expect problems.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate the capstone against success criteria; (2) measure outcomes; (3) gather user feedback; (4) state limits honestly.

### 39.1 Criteria results

All five check families run weekly (met). Anonymous repositories: 0 (met). Logging coverage 6 of 6 (met). Median findings age 9 days at term end (met). Scan blocking key-like strings (met, one real key blocked).

Section thirty-nine point one develops capstone evaluation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-nine point one, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-nine point one treats criteria results trend feedback as testable only when evidence and ticket IDs are recorded.

### 39.2 Trend

Total open findings fell from 41 at the start of term to 9.

Section thirty-nine point two develops capstone evaluation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-nine point two, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-nine point two treats criteria results trend feedback as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point two, Westmere University will not accept capstone work without a written trail.

Section thirty-nine point two fails closed if capstone evidence is missing rather than guessing.

### 39.3 Feedback

The cloud team rates the report useful; they ask for a shorter summary at the top, which Samuel adds.

Section thirty-nine point three develops capstone evaluation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-nine point three, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-nine point three treats criteria results trend feedback as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point three, Westmere University will not accept capstone work without a written trail.

### 39.4 Limits

One term of data; configuration state only, not attack resistance; scan may miss secrets that do not look random.

Section thirty-nine point four develops capstone evaluation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-nine point four, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-nine point four treats criteria results trend feedback as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point four, Westmere University will not accept capstone work without a written trail.

### 39.5 Independent check

A cloud team member reruns the report from scratch using the guide and gets the same results.

Section thirty-nine point five develops capstone evaluation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-nine point five, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-nine point five treats criteria results trend feedback as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point five, Westmere University will not accept capstone work without a written trail.

### 39.6 What next

Add Kubernetes role-binding analysis to the report; extend the scan to infrastructure code.

Section thirty-nine point six develops capstone evaluation with a Westmere University note Samuel Osei can demo offline.

Under section thirty-nine point six, Tom Becker expects capstone claims to carry owners and dates.

Section thirty-nine point six treats criteria results trend feedback as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point six, Westmere University will not accept capstone work without a written trail.

Section thirty-nine point six fails closed if capstone evidence is missing rather than guessing.

### Measuring user value

Beyond criteria, Samuel asks how the report is used. The cloud team says they read the summary every Monday and assign new findings in their planning meeting. Two developers say the report helped them find their own issues before reviews. Usage is the best sign the report will continue after the project. Samuel also checks how many findings were closed by owners without prompting: 22 of 32, which suggests the owner column works.

### Survey

A short survey of the cloud team rates the report's clarity 4.2 of 5 and suggests adding links from each finding to its runbook.

### Next owner

Tom names the report owner.

### Worked example

Tom presents the evaluation to Westmere's IT leadership, who fund continuing the report and the student volunteering scheme. Samuel's limits section is quoted in the presentation, which Tom says increased leadership trust.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Meeting criteria shows the project did what it set out to do; it does not show the criteria were the right ones.

### Exercises

- **EX115 — Findings trend.** How did open findings change? *Rubric:* 3 = 41 to 9; 2 = partial; 1 = none; 0 = none.
- **EX116 — Median age.** What was the median findings age? *Rubric:* 3 = 9 days; 2 = partial; 1 = none; 0 = none.
- **EX117 — Limits.** Name two limits. *Rubric:* 3 = one term, config only, scan misses non-random secrets; 2 = one; 1 = none; 0 = none.

### Synthesis

Evaluate honestly against criteria and say what remains unknown.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write and present the bachelor's thesis; (2) integrate the course's work into one argument; (3) answer questions; (4) reflect on learning.

### 40.1 Structure

Introduction with the opening case; background on cloud and container security; methods; studies from chapters 18, 33 and 34; capstone design, implementation and evaluation; discussion; limits; conclusion.

Section forty point one develops thesis and presentation with a Westmere University note Samuel Osei can demo offline.

Under section forty point one, Tom Becker expects thesis claims to carry owners and dates.

Section forty point one treats structure argument presentation questions as testable only when evidence and ticket IDs are recorded.

For section forty point one, Westmere University will not accept thesis work without a written trail.

### 40.2 Argument

Westmere's exposure came from missing visibility and secrets in images; combining guardrails, pipeline scanning and a weekly posture report closes these gaps measurably.

Section forty point two develops thesis and presentation with a Westmere University note Samuel Osei can demo offline.

Under section forty point two, Tom Becker expects thesis claims to carry owners and dates.

Section forty point two treats structure argument presentation questions as testable only when evidence and ticket IDs are recorded.

For section forty point two, Westmere University will not accept thesis work without a written trail.

### 40.3 Presentation

A 20-minute talk with the opening case, three key results and the limits, followed by questions.

Section forty point three develops thesis and presentation with a Westmere University note Samuel Osei can demo offline.

Under section forty point three, Tom Becker expects thesis claims to carry owners and dates.

Section forty point three treats structure argument presentation questions as testable only when evidence and ticket IDs are recorded.

For section forty point three, Westmere University will not accept thesis work without a written trail.

### 40.4 Questions

Examiners ask why not buy a commercial posture tool. Samuel answers that built-in services and a small script met the needs, but a tool could be reconsidered if the estate grows. They ask how the report avoids becoming noise; he shows owner assignment and the falling findings trend.

Section forty point four develops thesis and presentation with a Westmere University note Samuel Osei can demo offline.

Under section forty point four, Tom Becker expects thesis claims to carry owners and dates.

Section forty point four treats structure argument presentation questions as testable only when evidence and ticket IDs are recorded.

### 40.5 Reflection

Samuel writes that the most important skill was turning a vague worry into checkable statements and evidence.

Section forty point five develops thesis and presentation with a Westmere University note Samuel Osei can demo offline.

Under section forty point five, Tom Becker expects thesis claims to carry owners and dates.

Section forty point five treats structure argument presentation questions as testable only when evidence and ticket IDs are recorded.

For section forty point five, Westmere University will not accept thesis work without a written trail.

### 40.6 Outcome

The thesis passes with a high mark; Westmere's cloud team offers Samuel a graduate role.

Section forty point six develops thesis and presentation with a Westmere University note Samuel Osei can demo offline.

Under section forty point six, Tom Becker expects thesis claims to carry owners and dates.

Section forty point six treats structure argument presentation questions as testable only when evidence and ticket IDs are recorded.

For section forty point six, Westmere University will not accept thesis work without a written trail.

### Preparing the talk

Samuel rehearses three times with classmates, cutting slides each time until the talk fits comfortably in 20 minutes. He prepares backup slides with detailed results for likely questions. The opening slide shows the anonymous registry finding in one sentence; the closing slide shows the three layers now in place. Classmates' questions in rehearsal match two of the examiners' questions, so he is ready for them.

### Thanks

The thesis acknowledges the cloud team.

### Worked example

In his final reflection, Samuel notes that the anonymous registry from the opening case would now be blocked by a guardrail, detected by an event alert in minutes and listed in the weekly report, three independent layers where there had been none.

> **Synthetic case.** People and outcomes are synthetic.

### Errors and limits

Presentations should match the thesis claims, not exaggerate them.

### Exercises

- **EX118 — Argument.** State the thesis argument. *Rubric:* 3 = guardrails, scanning, posture report close gaps; 2 = partial; 1 = none; 0 = none.
- **EX119 — Commercial tool.** How did Samuel answer the tool question? *Rubric:* 3 = built-ins met needs; reconsider if estate grows; 2 = partial; 1 = none; 0 = none.
- **EX120 — Three layers.** What three layers now cover the registry case? *Rubric:* 3 = guardrail, event alert, weekly report; 2 = two; 1 = one; 0 = none.

### Synthesis

The thesis ties the course together into one evidenced argument.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Samuel Osei, Dr Clara Jensen, Tom Becker, Westmere University, Harbourside Youth Trust and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** For example, "no registry repository allows anonymous pull".

**EX002.** Internal users could still read a secret baked into an image.

**EX003.** Audit logging was off in one account.

**EX004.** Infrastructure, platform and software as a service.

**EX005.** Content in an image layer stays there.

**EX006.** It showed registry security is Westmere's responsibility.

**EX007.** They check many resources consistently and quickly.

**EX008.** They are easier to test and reuse.

**EX009.** Report "setting missing" rather than assume it is off.

**EX010.** A topic sentence, evidence and a link to the argument.

**EX011.** Logs were missing, so misuse cannot be ruled out.

**EX012.** Reading aloud, cutting words or checking numbers against sources.

**EX013.** Misconfigured storage, over-broad identities, leaked credentials, unpatched images, missing logs.

**EX014.** A short-lived identity would mean no secret in the image.

**EX015.** Network restrictions on the test database.

**EX016.** A "may assume" permission from one identity to a role.

**EX017.** support-cy reached cluster-admin via the ticket bot.

**EX018.** The ticket bot got a narrow restart role instead of deployer.

**EX019.** The database only accepted connections from the cluster subnet.

**EX020.** Access from inside the network so public access can be disabled.

**EX021.** The build moved to a runner inside the network.

**EX022.** Loaders, check functions and report writer.

**EX023.** To avoid silently passing when a check cannot run.

**EX024.** Repository names were compared case-sensitively.

**EX025.** Synthetic data only.

**EX026.** app-logs at 120 days and a test snapshot at 210 days.

**EX027.** Manual snapshots must carry an enforced expiry tag.

**EX028.** Read-only exports, a test account and documentation.

**EX029.** Reported it without using or testing it.

**EX030.** Testing it is using it without authorisation.

**EX031.** Containers share the node's kernel.

**EX032.** Non-root, no privilege escalation, dropped capabilities and a seccomp profile.

**EX033.** Nine of 31, because their images never set a user.

**EX034.** Mean 19.3 days, median 12.5, 11/20 = 0.55 on time.

**EX035.** About 0.33 to 0.77.

**EX036.** Around the long tail of findings over 30 days.

**EX037.** No MFA, a 400-day-old key and 220 days inactive.

**EX038.** Move to a managed identity with short-lived credentials.

**EX039.** A scheduled report used the contractor's key.

**EX040.** Minimisation, purpose limitation, retention limits, accuracy, security and transparency.

**EX041.** It shows what was exposed.

**EX042.** It produces counts per course instead of copying full records.

**EX043.** 3 of 6; gaps in studyhub-test eu-central and both research-sandbox regions.

**EX044.** Individual accounts cannot alter or delete them.

**EX045.** A researcher's attempt to create a public bucket, which was blocked.

**EX046.** A mistake in one account cannot change another's resources.

**EX047.** Block public storage, restrict regions, prevent disabling audit logs.

**EX048.** The sandbox shared the production registry; it was separated.

**EX049.** Control over key use and rotation, with audit logs.

**EX050.** The exact tested image is the one that runs.

**EX051.** Certificate verification was disabled in records-api.

**EX052.** Images from the shared base have fewer high-severity findings.

**EX053.** 12 of 18 public-base versus 3 of 22 shared-base images.

**EX054.** Images were not randomly assigned to bases.

**EX055.** Image, registry, orchestrator, container and host.

**EX056.** It can be reviewed and checked before being applied.

**EX057.** An image risk.

**EX058.** Use short-lived identities and scan before pushing.

**EX059.** Judging past decisions using knowledge not available then.

**EX060.** Case B, the credential in an image.

**EX061.** Authentication, authorisation, encryption and logging.

**EX062.** By comparing the model with flow logs.

**EX063.** It could delete any object in the bucket.

**EX064.** A base image, operating system packages and application libraries.

**EX065.** Mirrored internally after digest checking and scanning.

**EX066.** Within minutes, 7 images, using the inventory.

**EX067.** Anonymous pull, 540-day-old image and never scanned.

**EX068.** It exposes images to anyone.

**EX069.** It was archived and deleted after confirming with its owner.

**EX070.** Preventive (guardrails), detective (alerts), response (runbooks).

**EX071.** Control, owner, evidence source, test method and last test date.

**EX072.** No detection of secrets in images before push.

**EX073.** Registry review, account review, logging coverage and role graph.

**EX074.** An anonymous repository, an account without MFA, a missing logging region, a support-to-admin path.

**EX075.** Both were placed at the top and fixed in parallel.

**EX076.** 57%; audit logging, password length and open admin ports failed.

**EX077.** Staff sign in through the identity provider, not local passwords.

**EX078.** The unused default networks were deleted.

**EX079.** The privileged pod was admitted.

**EX080.** The test namespace lacked the Restricted enforcement label.

**EX081.** A test in one namespace does not prove all are labelled.

**EX082.** Deployments are blocked if the admission service is down.

**EX083.** They can last a long time without anyone noticing.

**EX084.** A scanner error now fails the build, with weekly scan counts reported.

**EX085.** login-new-country, 0 of 3 actionable.

**EX086.** They train slow responses that may affect real alerts.

**EX087.** From about 40 to 3 a month; median acknowledgement under 10 minutes.

**EX088.** A public access change, a new access key, a privileged pod request and a logging disablement attempt.

**EX089.** The new-key alert, 18 minutes, due to batch export.

**EX090.** Using the real-time event stream, bringing it under 2 minutes.

**EX091.** A broad developer token, a pipeline role that can assume admin, and no alerting on role assumption.

**EX092.** Restricted pod security, default-deny policies, no automatic token mounting.

**EX093.** 14 pods mounting service account tokens they did not use.

**EX094.** Where student data is stored and how breaches would be detected.

**EX095.** Changes are scheduled away from submission peaks.

**EX096.** A dedicated account for public data with content review.

**EX097.** 12 adopting and 12 non-adopting services in matched pairs.

**EX098.** 1 versus 4 findings; kappa 0.82.

**EX099.** Relabelling a sample with service names hidden.

**EX100.** Periodic configuration scanning and real-time change alerts.

**EX101.** Scanning 11 hours; event alerts 2 minutes.

**EX102.** Both, plus prevention through guardrails.

**EX103.** A weekly cloud posture report and a pipeline secret scan.

**EX104.** Weekly checks, zero anonymous repositories, full logging, median findings age under 14 days, scan blocking keys.

**EX105.** That the report proves StudyHub cannot be attacked.

**EX106.** Owner MFA, no owner keys, public storage blocked, audit logging, budget alerts.

**EX107.** Owner MFA off, a public bucket and logging off.

**EX108.** The charity's volunteer, with trustees' permission, guided by Samuel.

**EX109.** Who made the claim, what data, what method, what limits.

**EX110.** Plausible, but the specific percentage is weakly supported.

**EX111.** To "a vendor survey reported" rather than stating it as fact.

**EX112.** Registry, account, logging, benchmark and pod security checks.

**EX113.** Three test fixtures with realistic-looking fake keys.

**EX114.** A build with a real storage key copied from notes.

**EX115.** From 41 to 9.

**EX116.** 9 days.

**EX117.** One term of data, configuration only, scan may miss non-random secrets.

**EX118.** Guardrails, pipeline scanning and a weekly posture report close the visibility and secret gaps.

**EX119.** Built-in services met needs; a tool could be reconsidered as the estate grows.

**EX120.** A guardrail, an event alert and the weekly report.

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
