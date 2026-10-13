# Cloud and Container Security: Technical Course

- Language: English (`en`); course 059, Technical course (18 months).
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; Four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical students learning to configure, verify and maintain cloud storage and container security in a small IT team.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only cloud accounts, clusters and workloads you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Misconfigurations are taught from the defender's side using synthetic configurations, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one apprentice from a storage bucket left public for nearly three days, through services, networks, identities, scripting, scope and evidence, to a timeline, causes, policy, configuration, verification, secrets, troubleshooting, automation, partner integration, documentation, drift and a supervised project. Run each lab where it appears, attempt the four exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Tomás Reyes** | Technical student and apprentice | Invented |
| **Grace Mensah** | Supervisor | Invented |
| **Hollins Technical College** | Fictional college | Invented |
| **Fairway Logistics** | Fictional courier | Invented |

### Core sources

NIST [SP 800-145](https://doi.org/10.6028/NIST.SP.800-145), [SP 800-210](https://doi.org/10.6028/NIST.SP.800-210), [SP 800-190](https://doi.org/10.6028/NIST.SP.800-190) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); CSA [Cloud Controls Matrix v4](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); the [AWS](https://aws.amazon.com/compliance/shared-responsibility-model/), [Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) and [Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) shared responsibility pages; Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) describe how a small company's services are built from cloud components; (2) explain service models from NIST SP 800-145; (3) identify who runs each part.

### 1.1 The trigger

Tomás Reyes is a technical-course student at the fictional Hollins Technical College, working as an apprentice in the small IT team of the fictional Fairway Logistics, a regional courier. His supervisor is Grace Mensah. In March a developer made the storage bucket holding delivery manifests public so that a partner could download a file. It stayed public for nearly three days. Grace asks Tomás to help find out what happened and to make sure it does not happen again. The course follows that work.

### 1.2 Fairway's services

Fairway runs a parcel tracking site in containers on a managed Kubernetes cluster, stores manifests and driver photos in cloud storage buckets, keeps backups in another bucket, and uses a managed database. Its website images sit in a separate assets bucket.

Section one point two develops computing and service architecture with a Fairway Logistics note Tomás Reyes can demo offline.

Under section one point two, Grace Mensah expects computing claims to carry owners and dates.

Section one point two treats the trigger fairway's services as testable only when evidence and ticket IDs are recorded.

### 1.3 Service models

NIST SP 800-145 defines infrastructure, platform and software as a service. Fairway's cluster is close to platform as a service, because the provider runs the control plane; its storage and database are managed services; its email is software as a service.

Section one point three develops computing and service architecture with a Fairway Logistics note Tomás Reyes can demo offline.

Under section one point three, Grace Mensah expects computing claims to carry owners and dates.

Section one point three treats the trigger fairway's services as testable only when evidence and ticket IDs are recorded.

### 1.4 Who runs what

For each component Tomás records whether the provider, Fairway's IT team or a vendor operates it. This tells him where Fairway must configure security itself.

Section one point four develops computing and service architecture with a Fairway Logistics note Tomás Reyes can demo offline.

Under section one point four, Grace Mensah expects computing claims to carry owners and dates.

Section one point four treats the trigger fairway's services as testable only when evidence and ticket IDs are recorded.

For section one point four, Fairway Logistics will not accept computing work without a written trail.

### 1.5 Components and connections

He sketches how the tracking site reads from the database, writes manifests to storage and sends emails, so later chapters can follow data through the system.

Section one point five develops computing and service architecture with a Fairway Logistics note Tomás Reyes can demo offline.

Under section one point five, Grace Mensah expects computing claims to carry owners and dates.

Section one point five treats the trigger fairway's services as testable only when evidence and ticket IDs are recorded.

For section one point five, Fairway Logistics will not accept computing work without a written trail.

### Worked example

Tomás lists six components with their service model and operator. Grace adds one he missed: the partner's file transfer, which the developer replaced with the public bucket. Tomás realises that the incident began when a missing service was improvised.

> **Synthetic case.** Fairway, Tomás and Grace are synthetic.

### Errors and limits

Service model labels are approximate; record actual responsibilities rather than arguing about categories.

### Exercises

- **EX001 — Incident summary.** Describe the March incident in one sentence. *Rubric:* 3 = manifests bucket made public for partner, about three days; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Service models.** Which NIST service model best fits Fairway's managed cluster, and why? *Rubric:* 3 = platform-like; provider runs control plane; 2 = partial; 1 = none; 0 = none.
- **EX003 — Operator record.** Why record who operates each component? *Rubric:* 3 = shows where Fairway must configure security; 2 = partial; 1 = none; 0 = none.
- **EX004 — Missing component.** What component did Grace add and why did it matter? *Rubric:* 3 = partner file transfer; its absence led to improvising; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know each component, its service model and who runs it.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) explain HTTPS, DNS and private endpoints; (2) describe how storage is reached over the internet; (3) recognise public exposure.

### 2.1 HTTPS and TLS

Browsers and partners reach Fairway's services over HTTPS, which uses TLS to encrypt traffic and authenticate the server. Encryption protects data on the way, but it does not decide who is allowed to read it.

Section two point one develops networks and protocols with a Fairway Logistics note Tomás Reyes can demo offline.

Under section two point one, Grace Mensah expects networks claims to carry owners and dates.

Section two point one treats https and tls dns as testable only when evidence and ticket IDs are recorded.

### 2.2 DNS

DNS maps names such as tracking.fairway.example to addresses. Storage buckets also have names reachable over the internet, which is why a public setting exposes them to anyone who knows or guesses the name.

Section two point two develops networks and protocols with a Fairway Logistics note Tomás Reyes can demo offline.

Under section two point two, Grace Mensah expects networks claims to carry owners and dates.

Section two point two treats https and tls dns as testable only when evidence and ticket IDs are recorded.

### 2.3 Private endpoints

Cloud providers allow services to be reached through private network endpoints, so traffic stays inside a private network. Fairway's database uses one; its buckets do not yet.

Section two point three develops networks and protocols with a Fairway Logistics note Tomás Reyes can demo offline.

Under section two point three, Grace Mensah expects networks claims to carry owners and dates.

Section two point three treats https and tls dns as testable only when evidence and ticket IDs are recorded.

For section two point three, Fairway Logistics will not accept networks work without a written trail.

### 2.4 Exposure

A service is exposed when it can be reached from the internet without authentication. The manifests bucket was exposed for nearly three days because its policy allowed public reads.

Section two point four develops networks and protocols with a Fairway Logistics note Tomás Reyes can demo offline.

Under section two point four, Grace Mensah expects networks claims to carry owners and dates.

Section two point four treats https and tls dns as testable only when evidence and ticket IDs are recorded.

### 2.5 Ports and firewalls

Firewalls limit which addresses can reach which ports, but storage services are reached through the provider's shared endpoints, so access policy, not firewalls, is the main control.

Section two point five develops networks and protocols with a Fairway Logistics note Tomás Reyes can demo offline.

Under section two point five, Grace Mensah expects networks claims to carry owners and dates.

Section two point five treats https and tls dns as testable only when evidence and ticket IDs are recorded.

For section two point five, Fairway Logistics will not accept networks work without a written trail.

### Checking exposure

Tomás learns a simple habit: for every service, ask who can reach it from the internet and what proves they are allowed. For the tracking site, users reach it and the application checks their login. For the database, nobody outside the private network can reach it. For the manifests bucket during the incident, anyone could reach it and nothing checked them. Writing the answer for each service makes exposure visible before it becomes an incident.

### Worked example

Tomás asks why the firewall did not stop the downloads. Grace explains that the bucket was reached through the provider's public storage endpoint over HTTPS, which Fairway's firewall does not control. Access policy is the only gate.

> **Synthetic case.** Names are synthetic.

### Errors and limits

Assuming firewalls protect managed services leads to false confidence.

### Exercises

- **EX005 — Encryption limit.** What does HTTPS not decide? *Rubric:* 3 = who may read the data; 2 = partial; 1 = none; 0 = none.
- **EX006 — Bucket names.** Why do bucket names matter for exposure? *Rubric:* 3 = reachable by name over internet; 2 = partial; 1 = none; 0 = none.
- **EX007 — Firewall gap.** Why did Fairway's firewall not prevent the downloads? *Rubric:* 3 = provider's public endpoint; policy is the gate; 2 = partial; 1 = none; 0 = none.
- **EX008 — Private endpoint.** Which Fairway service already uses a private endpoint? *Rubric:* 3 = database; 2 = partial; 1 = none; 0 = none.

### Synthesis

For managed services, access policy is the main network control.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) explain users, groups and service identities; (2) describe cloud identity and access management; (3) apply least privilege to storage.

### 3.1 Users and groups

Operating systems grant permissions to users and groups. Cloud platforms do the same with identities, roles and policies, but over the internet and across many services.

Section three point one develops operating systems and identities with a Fairway Logistics note Tomás Reyes can demo offline.

Under section three point one, Grace Mensah expects operating claims to carry owners and dates.

Section three point one treats users and groups cloud as testable only when evidence and ticket IDs are recorded.

For section three point one, Fairway Logistics will not accept operating work without a written trail.

### 3.2 Cloud IAM

Each provider's identity and access management service decides which identity may perform which action on which resource. The developer, dev-sam, had permission to change bucket policies, which is why he could make the bucket public.

Section three point two develops operating systems and identities with a Fairway Logistics note Tomás Reyes can demo offline.

Under section three point two, Grace Mensah expects operating claims to carry owners and dates.

Section three point two treats users and groups cloud as testable only when evidence and ticket IDs are recorded.

### 3.3 Least privilege

Developers need to upload objects, not change bucket policies. Removing that permission would have prevented the incident.

Section three point three develops operating systems and identities with a Fairway Logistics note Tomás Reyes can demo offline.

Under section three point three, Grace Mensah expects operating claims to carry owners and dates.

Section three point three treats users and groups cloud as testable only when evidence and ticket IDs are recorded.

For section three point three, Fairway Logistics will not accept operating work without a written trail.

### 3.4 Service identities

The CI deploy pipeline uses its own identity to upload website assets. It should be limited to the assets bucket.

Section three point four develops operating systems and identities with a Fairway Logistics note Tomás Reyes can demo offline.

Under section three point four, Grace Mensah expects operating claims to carry owners and dates.

Section three point four treats users and groups cloud as testable only when evidence and ticket IDs are recorded.

For section three point four, Fairway Logistics will not accept operating work without a written trail.

### 3.5 Role-based access

Sandhu et al. (1996) describe role-based access control. Fairway defines roles such as developer, operator and auditor with set permissions.

Section three point five develops operating systems and identities with a Fairway Logistics note Tomás Reyes can demo offline.

Under section three point five, Grace Mensah expects operating claims to carry owners and dates.

Section three point five treats users and groups cloud as testable only when evidence and ticket IDs are recorded.

For section three point five, Fairway Logistics will not accept operating work without a written trail.

### Reviewing permissions

Permission reviews compare what each identity is allowed to do with what it actually does. Provider tools can list unused permissions, and Fairway's own audit logs show which actions were used in the last ninety days. dev-sam had never changed a bucket policy before March, which supports removing the permission: it was not needed for normal work. Tomás schedules a quarterly review using the same method.

He also checks that Grace's administrator account uses multi-factor authentication and is used only for administrative tasks, not daily work.

### Leavers

Accounts of staff who leave are disabled on their last day.

### Worked example

Tomás lists permissions for three identities. Developer: upload, read and change policies on all buckets. CI deploy: write to all buckets. Grace: administrator. He proposes removing policy changes from developers and limiting CI deploy to site-assets.

> **Synthetic case.** Identities are synthetic.

### Errors and limits

Removing permissions can break workflows; agree changes with the people affected.

### Exercises

- **EX009 — Root permission.** Which permission let dev-sam make the bucket public? *Rubric:* 3 = change bucket policies; 2 = partial; 1 = none; 0 = none.
- **EX010 — Developer need.** What do developers actually need on storage? *Rubric:* 3 = upload and read objects; 2 = partial; 1 = none; 0 = none.
- **EX011 — CI scope.** How should CI deploy be limited? *Rubric:* 3 = site-assets bucket only; 2 = partial; 1 = none; 0 = none.
- **EX012 — Roles.** Name Fairway's three roles. *Rubric:* 3 = developer, operator, auditor; 2 = two; 1 = one; 0 = none.

### Synthesis

Give identities only what their work requires.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) read JSON, YAML and environment files; (2) write small Python checks; (3) avoid printing secrets.

### 4.1 Formats

Cloud settings arrive as JSON, Kubernetes manifests as YAML, and application settings as environment files with KEY=value lines. Tomás learns to recognise each.

Section four point one develops scripting and data formats with a Fairway Logistics note Tomás Reyes can demo offline.

Under section four point one, Grace Mensah expects scripting claims to carry owners and dates.

Section four point one treats formats reading with python as testable only when evidence and ticket IDs are recorded.

For section four point one, Fairway Logistics will not accept scripting work without a written trail.

### 4.2 Reading with Python

Python's standard library reads JSON directly, and simple line-based formats with string methods. The labs in this course use these, with no extra packages.

Section four point two develops scripting and data formats with a Fairway Logistics note Tomás Reyes can demo offline.

Under section four point two, Grace Mensah expects scripting claims to carry owners and dates.

Section four point two treats formats reading with python as testable only when evidence and ticket IDs are recorded.

For section four point two, Fairway Logistics will not accept scripting work without a written trail.

### 4.3 Small checks

A check loads records, compares each with an expected value and prints differences. Counts come first, then details.

Section four point three develops scripting and data formats with a Fairway Logistics note Tomás Reyes can demo offline.

Under section four point three, Grace Mensah expects scripting claims to carry owners and dates.

Section four point three treats formats reading with python as testable only when evidence and ticket IDs are recorded.

For section four point three, Fairway Logistics will not accept scripting work without a written trail.

### 4.4 Never print secrets

When a check looks for secrets, it reports the key name and file, never the value. Printed secrets end up in logs and screenshots.

Section four point four develops scripting and data formats with a Fairway Logistics note Tomás Reyes can demo offline.

Under section four point four, Grace Mensah expects scripting claims to carry owners and dates.

Section four point four treats formats reading with python as testable only when evidence and ticket IDs are recorded.

For section four point four, Fairway Logistics will not accept scripting work without a written trail.

### 4.5 Synthetic data

All labs use synthetic records; values that look like secrets are written as <redacted>.

Section four point five develops scripting and data formats with a Fairway Logistics note Tomás Reyes can demo offline.

Under section four point five, Grace Mensah expects scripting claims to carry owners and dates.

Section four point five treats formats reading with python as testable only when evidence and ticket IDs are recorded.

For section four point five, Fairway Logistics will not accept scripting work without a written trail.

### A worked check

Tomás's first check has four parts: load the export, define the expected value, compare each record and print counts then details. He keeps the expected values at the top of the script so that anyone reviewing can see the policy without reading the loop. When the policy changes, only that block changes.

He tests the check on a small synthetic file where he knows the answer, including one bucket that should pass and one that should fail. Only after both behave as expected does he run it on the full synthetic export. Testing with known answers is a habit he keeps for every lab in the course.

### Handling errors

If a record is missing a field, the check reports it rather than crashing or silently skipping it, because a missing setting is itself a finding.

### Worked example

Tomás writes a check that reads a JSON export of bucket settings and prints buckets without encryption. Grace reviews it and asks him to add a count at the top and a comment explaining the expected value.

> **Synthetic case.** Data is synthetic.

### Errors and limits

Simple parsers may mis-read complex YAML; use them only on simple synthetic examples.

### Exercises

- **EX013 — Formats.** Which format do Kubernetes manifests usually use? *Rubric:* 3 = YAML; 2 = partial; 1 = none; 0 = none.
- **EX014 — Library.** Why use only the standard library? *Rubric:* 3 = runs anywhere, no unreviewed packages; 2 = partial; 1 = none; 0 = none.
- **EX015 — Secret output.** What should a secret check print? *Rubric:* 3 = key name and file, not value; 2 = partial; 1 = none; 0 = none.
- **EX016 — Review request.** What did Grace ask Tomás to add? *Rubric:* 3 = count at top, comment on expected value; 2 = partial; 1 = none; 0 = none.

### Synthesis

Read common formats safely and print results, not secrets.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) define the scope of a security review; (2) collect evidence with time and source; (3) respect authorisation.

### 5.1 Scope

Grace defines Tomás's scope: Fairway's storage buckets, identities and cluster settings, using read-only access and synthetic copies where possible. Partner systems are out of scope.

Section five point one develops security scope and evidence with a Fairway Logistics note Tomás Reyes can demo offline.

Under section five point one, Grace Mensah expects security claims to carry owners and dates.

Section five point one treats scope authorisation evidence preserving as testable only when evidence and ticket IDs are recorded.

For section five point one, Fairway Logistics will not accept security work without a written trail.

### 5.2 Authorisation

The scope is written and signed by Grace and the IT manager. Tomás does not test anything outside it.

Section five point two develops security scope and evidence with a Fairway Logistics note Tomás Reyes can demo offline.

Under section five point two, Grace Mensah expects security claims to carry owners and dates.

Section five point two treats scope authorisation evidence preserving as testable only when evidence and ticket IDs are recorded.

For section five point two, Fairway Logistics will not accept security work without a written trail.

### 5.3 Evidence

Evidence includes exported audit events, settings and permission lists, each saved with collection time and source.

Section five point three develops security scope and evidence with a Fairway Logistics note Tomás Reyes can demo offline.

Under section five point three, Grace Mensah expects security claims to carry owners and dates.

Section five point three treats scope authorisation evidence preserving as testable only when evidence and ticket IDs are recorded.

For section five point three, Fairway Logistics will not accept security work without a written trail.

### 5.4 Preserving evidence

Copies are stored read-only so they cannot be altered.

Section five point four develops security scope and evidence with a Fairway Logistics note Tomás Reyes can demo offline.

Under section five point four, Grace Mensah expects security claims to carry owners and dates.

Section five point four treats scope authorisation evidence preserving as testable only when evidence and ticket IDs are recorded.

For section five point four, Fairway Logistics will not accept security work without a written trail.

Section five point four fails closed if security evidence is missing rather than guessing.

### 5.5 Facts and judgements

Tomás separates what records show from what he concludes.

Section five point five develops security scope and evidence with a Fairway Logistics note Tomás Reyes can demo offline.

Under section five point five, Grace Mensah expects security claims to carry owners and dates.

Section five point five treats scope authorisation evidence preserving as testable only when evidence and ticket IDs are recorded.

For section five point five, Fairway Logistics will not accept security work without a written trail.

Section five point five fails closed if security evidence is missing rather than guessing.

### Evidence register

Tomás keeps an evidence register listing each item, its source, collection time, who collected it and where it is stored. When the timeline is written later, each statement points to a register entry. This lets Grace or an auditor trace any claim back to its record.

The register also records what was not available. For example, data access logs were enabled only on the manifests bucket, so reads of other buckets during the period cannot be checked. Recording gaps prevents later readers from assuming more coverage than existed.

### Confidentiality

The manifests contain customer addresses. Tomás works with synthetic copies for analysis and does not open real manifests; the decision about customer impact is made by the data protection lead using the evidence he provides.

### Keeping time

All times are recorded in one time zone, stated at the top of the register, to avoid confusion when comparing provider logs with staff notes.

### Worked example

Tomás exports the storage audit events for March and saves them with a note of who exported them, when and from which account. Grace checks the note before analysis begins.

> **Synthetic case.** Scope is synthetic.

### Errors and limits

Working outside scope, even with good intentions, can break trust and rules.

### Exercises

- **EX017 — Out of scope.** What was out of scope? *Rubric:* 3 = partner systems; 2 = partial; 1 = none; 0 = none.
- **EX018 — Authorisation.** Who signed the scope? *Rubric:* 3 = Grace and IT manager; 2 = partial; 1 = none; 0 = none.
- **EX019 — Evidence note.** What did Tomás record with the export? *Rubric:* 3 = who, when, which account; 2 = two; 1 = one; 0 = none.
- **EX020 — Fact versus judgement.** Why separate facts from conclusions? *Rubric:* 3 = others can check reasoning; 2 = partial; 1 = none; 0 = none.

### Synthesis

Work inside written scope with recorded evidence.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Cloud and container security: system model

### Learning outcomes

You will (1) model Fairway's cloud system with components, data and trust boundaries; (2) identify where controls belong.

### 6.1 Model

Tomás draws Fairway's system: users and partners on the internet; the tracking site in the cluster; buckets for manifests, assets, backups and driver photos; the database.

Section six point one develops cloud and container security system with a Fairway Logistics note Tomás Reyes can demo offline.

Under section six point one, Grace Mensah expects cloud claims to carry owners and dates.

Section six point one treats model data boundaries where as testable only when evidence and ticket IDs are recorded.

### 6.2 Data

He labels data by sensitivity: manifests contain customer names and addresses; driver photos are personal data; assets are public by design; backups contain everything.

Section six point two develops cloud and container security system with a Fairway Logistics note Tomás Reyes can demo offline.

Under section six point two, Grace Mensah expects cloud claims to carry owners and dates.

Section six point two treats model data boundaries where as testable only when evidence and ticket IDs are recorded.

For section six point two, Fairway Logistics will not accept cloud work without a written trail.

### 6.3 Boundaries

Boundaries lie between the internet and the cluster, the cluster and storage, and storage and the internet.

Section six point three develops cloud and container security system with a Fairway Logistics note Tomás Reyes can demo offline.

Under section six point three, Grace Mensah expects cloud claims to carry owners and dates.

Section six point three treats model data boundaries where as testable only when evidence and ticket IDs are recorded.

For section six point three, Fairway Logistics will not accept cloud work without a written trail.

### 6.4 Where controls belong

Public access blocks on sensitive buckets, least-privilege identities, encryption and logging belong at the storage boundary.

Section six point four develops cloud and container security system with a Fairway Logistics note Tomás Reyes can demo offline.

Under section six point four, Grace Mensah expects cloud claims to carry owners and dates.

Section six point four treats model data boundaries where as testable only when evidence and ticket IDs are recorded.

For section six point four, Fairway Logistics will not accept cloud work without a written trail.

### 6.5 Shared responsibility

The provider secures storage infrastructure; Fairway configures access, as the providers' shared responsibility pages explain.

Section six point five develops cloud and container security system with a Fairway Logistics note Tomás Reyes can demo offline.

Under section six point five, Grace Mensah expects cloud claims to carry owners and dates.

Section six point five treats model data boundaries where as testable only when evidence and ticket IDs are recorded.

For section six point five, Fairway Logistics will not accept cloud work without a written trail.

### Checking the model

Tomás compares the model with the provider's list of buckets and finds driver-photos, created by a mobile app project, which was not on his diagram. He adds it and labels its data as personal. The comparison shows why models must be checked against real inventories: the bucket nobody remembered turns out, in chapter 11, to be the worst configured.

He also confirms the database endpoint is private by checking its network settings, not just the diagram.

### Using the model

The model becomes the reference for later chapters: every check, alert and policy rule points back to a component and boundary on it. When a new service is added, the model is updated first.

### Data owners

Each data type gets an owner: operations for manifests, HR for driver photos and IT for backups.

### Worked example

The model shows that only the assets bucket should ever be public. Tomás marks the others as never public, which becomes a policy rule.

> **Synthetic case.** Model is synthetic.

### Errors and limits

A model is a simplification; check it against real settings.

### Exercises

- **EX021 — Sensitive data.** Which data is most sensitive? *Rubric:* 3 = backups, manifests, driver photos; 2 = two; 1 = one; 0 = none.
- **EX022 — Public bucket.** Which bucket should be public? *Rubric:* 3 = assets only; 2 = partial; 1 = none; 0 = none.
- **EX023 — Storage controls.** Which controls belong at the storage boundary? *Rubric:* 3 = public block, least privilege, encryption, logging; 2 = three; 1 = two; 0 = none.
- **EX024 — Provider duty.** What does the provider secure? *Rubric:* 3 = storage infrastructure; 2 = partial; 1 = none; 0 = none.

### Synthesis

Model data sensitivity and boundaries to place controls.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Cloud and container security: data and telemetry

### Learning outcomes

You will (1) read cloud storage audit events; (2) reconstruct a timeline; (3) count exposure and access.

### 7.1 Audit events

Cloud providers can record management actions, such as policy changes, and data access, such as object reads. Fairway had data access logging enabled on the manifests bucket, which makes the timeline possible.

Section seven point one develops cloud and container security data with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seven point one, Grace Mensah expects cloud claims to carry owners and dates.

Section seven point one treats audit events reading the as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — storage events

```python
"""Summarise synthetic cloud storage audit events and flag public-access changes (stdlib only)."""
events = [("2026-03-02 09:14", "dev-sam", "PutObject", "manifests"), ("2026-03-02 09:20", "dev-sam", "PutObject", "manifests"),
          ("2026-03-03 16:41", "dev-sam", "PutBucketPolicy:public-read", "manifests"),
          ("2026-03-04 08:05", "ci-deploy", "PutObject", "site-assets"), ("2026-03-05 11:30", "anonymous", "GetObject", "manifests"),
          ("2026-03-05 11:31", "anonymous", "GetObject", "manifests"), ("2026-03-06 10:02", "grace", "PutBucketPolicy:private", "manifests"),
          ("2026-03-06 10:05", "ci-deploy", "PutObject", "site-assets")]
print(f"events {len(events)}")
for t, who, act, b in events:
    if "PutBucketPolicy" in act or who == "anonymous":
        print(f"  {t} {who:10} {act:28} {b}")
pub = [e for e in events if e[2].endswith("public-read")][0][0]; fix = [e for e in events if e[2].endswith("private")][0][0]
print(f"public from {pub} to {fix}; anonymous reads {sum(1 for e in events if e[1]=='anonymous')}")
```

Run with `python3 lab_events.py`. Verified output:

```text
events 8
  2026-03-03 16:41 dev-sam    PutBucketPolicy:public-read  manifests
  2026-03-05 11:30 anonymous  GetObject                    manifests
  2026-03-05 11:31 anonymous  GetObject                    manifests
  2026-03-06 10:02 grace      PutBucketPolicy:private      manifests
public from 2026-03-03 16:41 to 2026-03-06 10:02; anonymous reads 2
```

### 7.2 Reading the result

Of 8 events, 4 matter. dev-sam set the bucket policy to public-read on 3 March at 16:41. Two anonymous reads followed on 5 March at 11:30 and 11:31. Grace set the policy back to private on 6 March at 10:02. The bucket was public for about two days and seventeen hours.

Section seven point two develops cloud and container security data with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seven point two, Grace Mensah expects cloud claims to carry owners and dates.

Section seven point two treats audit events reading the as testable only when evidence and ticket IDs are recorded.

### 7.3 Interpreting the reads

The two anonymous reads could be the partner, who was sent the link, or someone else. The records show the source network for each request; Tomás compares them with the partner's published address range and finds they match the partner.

Section seven point three develops cloud and container security data with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seven point three, Grace Mensah expects cloud claims to carry owners and dates.

Section seven point three treats audit events reading the as testable only when evidence and ticket IDs are recorded.

### 7.4 Limits

Logs show requests that reached the service. They do not prove that no other copies exist, for example if the partner forwarded the file.

Section seven point four develops cloud and container security data with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seven point four, Grace Mensah expects cloud claims to carry owners and dates.

Section seven point four treats audit events reading the as testable only when evidence and ticket IDs are recorded.

For section seven point four, Fairway Logistics will not accept cloud work without a written trail.

### 7.5 Reporting

The timeline is written in plain words with times, sources and the limit stated.

Section seven point five develops cloud and container security data with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seven point five, Grace Mensah expects cloud claims to carry owners and dates.

Section seven point five treats audit events reading the as testable only when evidence and ticket IDs are recorded.

For section seven point five, Fairway Logistics will not accept cloud work without a written trail.

### Preserving the timeline

The exported events and timeline are kept read-only with the evidence register.

### Clock alignment

Provider log times are in UTC; Tomás converts them to local time and states both in the timeline, so readers comparing staff notes are not confused.

### Worked example

Grace asks whether customers must be told. Tomás presents the timeline and the partner match. Grace consults Fairway's data protection lead, who decides, based on the evidence, that the exposure was limited to an authorised partner and records the decision.

> **Synthetic case.** Events and times are synthetic.

### Errors and limits

Without data access logs, the reads would have been invisible; the absence of logs is not evidence of no access.

### Exercises

- **EX025 — Lab timeline.** Give the start and end of exposure. *Rubric:* 3 = 3 March 16:41 to 6 March 10:02; 2 = partial; 1 = none; 0 = none.
- **EX026 — Anonymous reads.** How many anonymous reads occurred and who made them? *Rubric:* 3 = two; matched partner range; 2 = partial; 1 = none; 0 = none.
- **EX027 — Log limit.** What can the logs not prove? *Rubric:* 3 = no other copies; 2 = partial; 1 = none; 0 = none.
- **EX028 — Decision owner.** Who decided on notification? *Rubric:* 3 = data protection lead; 2 = partial; 1 = none; 0 = none.

### Synthesis

Logs turn guesses into a timeline; state what they cannot show.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Cloud and container security: failure modes

### Learning outcomes

You will (1) explain how cloud misconfigurations happen; (2) classify causes; (3) connect causes to controls.

### 8.1 How it happened

The developer needed to share a file, had permission to change the policy, and no check stopped him. Three conditions combined: a missing service, broad permission and no guardrail.

Section eight point one develops cloud and container security failure with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eight point one, Grace Mensah expects cloud claims to carry owners and dates.

Section eight point one treats how it happened common as testable only when evidence and ticket IDs are recorded.

### 8.2 Common causes

Cloud failures often come from manual console changes, copied examples with insecure defaults, permissions broader than needed and lack of review.

Section eight point two develops cloud and container security failure with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eight point two, Grace Mensah expects cloud claims to carry owners and dates.

Section eight point two treats how it happened common as testable only when evidence and ticket IDs are recorded.

For section eight point two, Fairway Logistics will not accept cloud work without a written trail.

### 8.3 Classifying

Tomás groups causes as process (no partner transfer service), access (broad permissions) and technical (no public access block).

Section eight point three develops cloud and container security failure with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eight point three, Grace Mensah expects cloud claims to carry owners and dates.

Section eight point three treats how it happened common as testable only when evidence and ticket IDs are recorded.

For section eight point three, Fairway Logistics will not accept cloud work without a written trail.

### 8.4 Matching controls

Process: provide a secure way to share files. Access: remove policy permissions from developers. Technical: enable account-level public access blocking.

Section eight point four develops cloud and container security failure with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eight point four, Grace Mensah expects cloud claims to carry owners and dates.

Section eight point four treats how it happened common as testable only when evidence and ticket IDs are recorded.

For section eight point four, Fairway Logistics will not accept cloud work without a written trail.

### 8.5 Blameless review

The review focuses on conditions, not the developer.

Section eight point five develops cloud and container security failure with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eight point five, Grace Mensah expects cloud claims to carry owners and dates.

Section eight point five treats how it happened common as testable only when evidence and ticket IDs are recorded.

For section eight point five, Fairway Logistics will not accept cloud work without a written trail.

Section eight point five fails closed if cloud evidence is missing rather than guessing.

### Lessons from research

Cloud misconfiguration is widely reported. Armbrust et al. (2010) noted early that cloud computing shifts operational work to customers in new ways; the shared responsibility pages from AWS, Azure and Google Cloud all place access configuration with the customer. Fairway's incident fits this pattern: the provider's storage worked as designed, and the exposure came from configuration.

Tomás uses this to explain to the team that the fix is about Fairway's own practices, not about changing providers.

### Recording causes

Each cause is recorded with its matching control and an owner, so the review leads to actions rather than only understanding.

### Follow-up date

Grace sets a review date one month later to check that every action was completed.

### Sharing lessons

A short summary of causes is shared with all developers.

### Worked example

dev-sam joins the review and explains he believed the link was hard to guess. Grace thanks him for being open, and the team notes that obscurity is not access control.

> **Synthetic case.** Synthetic.

### Errors and limits

Fixing only one cause leaves the others to combine again.

### Exercises

- **EX029 — Three conditions.** Which three conditions combined? *Rubric:* 3 = missing service, broad permission, no guardrail; 2 = two; 1 = one; 0 = none.
- **EX030 — Cause groups.** Name the three cause groups. *Rubric:* 3 = process, access, technical; 2 = two; 1 = one; 0 = none.
- **EX031 — Technical control.** Which technical control matches? *Rubric:* 3 = account-level public access block; 2 = partial; 1 = none; 0 = none.
- **EX032 — Obscurity.** Why is a hard-to-guess link not enough? *Rubric:* 3 = obscurity is not access control; 2 = partial; 1 = none; 0 = none.

### Synthesis

Fix every contributing condition, not just one.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Cloud and container security: tools and methods

### Learning outcomes

You will (1) choose methods for checking cloud configuration; (2) use benchmarks; (3) plan regular checks.

### 9.1 Methods

Settings can be checked by reading exports, by provider policy tools, or by scanners. Tomás starts with exports and a simple script.

Section nine point one develops cloud and container security tools with a Fairway Logistics note Tomás Reyes can demo offline.

Under section nine point one, Grace Mensah expects cloud claims to carry owners and dates.

Section nine point one treats methods benchmarks fairway's policy as testable only when evidence and ticket IDs are recorded.

For section nine point one, Fairway Logistics will not accept cloud work without a written trail.

### 9.2 Benchmarks

The CIS Benchmarks for cloud providers include storage recommendations such as blocking public access and enabling logging. CSA CCM v4 lists matching controls.

Section nine point two develops cloud and container security tools with a Fairway Logistics note Tomás Reyes can demo offline.

Under section nine point two, Grace Mensah expects cloud claims to carry owners and dates.

Section nine point two treats methods benchmarks fairway's policy as testable only when evidence and ticket IDs are recorded.

For section nine point two, Fairway Logistics will not accept cloud work without a written trail.

### 9.3 Fairway's policy

Grace and Tomás write a storage policy with four rules: block public access, encrypt, version and log access, except for the assets bucket's public read.

Section nine point three develops cloud and container security tools with a Fairway Logistics note Tomás Reyes can demo offline.

Under section nine point three, Grace Mensah expects cloud claims to carry owners and dates.

Section nine point three treats methods benchmarks fairway's policy as testable only when evidence and ticket IDs are recorded.

For section nine point three, Fairway Logistics will not accept cloud work without a written trail.

### 9.4 Frequency

Checks run daily; changes between runs are caught by the alert from chapter 14.

Section nine point four develops cloud and container security tools with a Fairway Logistics note Tomás Reyes can demo offline.

Under section nine point four, Grace Mensah expects cloud claims to carry owners and dates.

Section nine point four treats methods benchmarks fairway's policy as testable only when evidence and ticket IDs are recorded.

For section nine point four, Fairway Logistics will not accept cloud work without a written trail.

### 9.5 Reviewing tools

They test a provider tool but keep their script, because it is simple and understood.

Section nine point five develops cloud and container security tools with a Fairway Logistics note Tomás Reyes can demo offline.

Under section nine point five, Grace Mensah expects cloud claims to carry owners and dates.

Section nine point five treats methods benchmarks fairway's policy as testable only when evidence and ticket IDs are recorded.

For section nine point five, Fairway Logistics will not accept cloud work without a written trail.

### Comparing tools

Tomás tests the provider's policy tool on a staging account. It finds the same issues as his script plus two settings he had not considered, such as object ownership controls. He adds these to the policy as future rules. The comparison shows that a simple script and a richer tool can complement each other: the script is easy to explain, and the tool reveals what the script misses.

He records results in a short note: what each method found, how long it took and how easy the output was to read.

### Starting small

Grace prefers four well-enforced rules over forty ignored ones.

### Evidence from checks

Each daily run saves its output with a date, building a history auditors can review.

### Budget

The script approach costs only staff time.

### Review cycle

The policy is reviewed yearly.

### Worked example

Tomás maps each of the four rules to a benchmark recommendation and a CCM v4 control area, which helps Grace explain the policy to auditors.

> **Synthetic case.** Synthetic.

### Errors and limits

A benchmark is a starting point; adapt it to the system.

### Exercises

- **EX033 — Methods.** Name three ways to check settings. *Rubric:* 3 = exports, provider tools, scanners; 2 = two; 1 = one; 0 = none.
- **EX034 — Policy rules.** List the four storage rules. *Rubric:* 3 = block public, encrypt, version, log; 2 = three; 1 = two; 0 = none.
- **EX035 — Exception.** Which exception applies? *Rubric:* 3 = assets bucket public read; 2 = partial; 1 = none; 0 = none.
- **EX036 — Mapping value.** Why map rules to benchmarks? *Rubric:* 3 = explain to auditors; 2 = partial; 1 = none; 0 = none.

### Synthesis

Write a short policy grounded in benchmarks and check it often.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Cloud and container security: control configuration

### Learning outcomes

You will (1) configure storage controls; (2) apply them safely; (3) record changes.

### 10.1 Account-level block

Providers offer a setting that blocks public access for all buckets in an account. Fairway enables it, with the assets bucket moved to a separate account where public reads are allowed.

Section ten point one develops cloud and container security control with a Fairway Logistics note Tomás Reyes can demo offline.

Under section ten point one, Grace Mensah expects cloud claims to carry owners and dates.

Section ten point one treats account-level block encryption versioning as testable only when evidence and ticket IDs are recorded.

### 10.2 Encryption

Default encryption ensures new objects are encrypted at rest.

Section ten point two develops cloud and container security control with a Fairway Logistics note Tomás Reyes can demo offline.

Under section ten point two, Grace Mensah expects cloud claims to carry owners and dates.

Section ten point two treats account-level block encryption versioning as testable only when evidence and ticket IDs are recorded.

For section ten point two, Fairway Logistics will not accept cloud work without a written trail.

Section ten point two fails closed if cloud evidence is missing rather than guessing.

### 10.3 Versioning

Versioning keeps earlier copies so deleted or overwritten files can be restored.

Section ten point three develops cloud and container security control with a Fairway Logistics note Tomás Reyes can demo offline.

Under section ten point three, Grace Mensah expects cloud claims to carry owners and dates.

Section ten point three treats account-level block encryption versioning as testable only when evidence and ticket IDs are recorded.

For section ten point three, Fairway Logistics will not accept cloud work without a written trail.

### 10.4 Logging

Access logging records reads and writes for investigation.

Section ten point four develops cloud and container security control with a Fairway Logistics note Tomás Reyes can demo offline.

Under section ten point four, Grace Mensah expects cloud claims to carry owners and dates.

Section ten point four treats account-level block encryption versioning as testable only when evidence and ticket IDs are recorded.

For section ten point four, Fairway Logistics will not accept cloud work without a written trail.

Section ten point four fails closed if cloud evidence is missing rather than guessing.

### 10.5 Change records

Each change is made through the configuration repository with review, not in the console.

Section ten point five develops cloud and container security control with a Fairway Logistics note Tomás Reyes can demo offline.

Under section ten point five, Grace Mensah expects cloud claims to carry owners and dates.

Section ten point five treats account-level block encryption versioning as testable only when evidence and ticket IDs are recorded.

For section ten point five, Fairway Logistics will not accept cloud work without a written trail.

### 10.6 Testing

Each change is tested on a staging bucket first.

Section ten point six develops cloud and container security control with a Fairway Logistics note Tomás Reyes can demo offline.

Under section ten point six, Grace Mensah expects cloud claims to carry owners and dates.

Section ten point six treats account-level block encryption versioning as testable only when evidence and ticket IDs are recorded.

For section ten point six, Fairway Logistics will not accept cloud work without a written trail.

Section ten point six fails closed if cloud evidence is missing rather than guessing.

### Order of changes

Tomás applies changes in an order that reduces risk. First, the account-level public block, because it prevents the incident pattern immediately. Second, removing developer policy permissions. Third, default encryption, then versioning and logging. Each step is small, tested and recorded, so if something breaks, the cause is obvious.

He informs developers before each change through the team channel, explaining what changes and whom to ask if something stops working.

### Costs

Versioning and logging add storage cost. Tomás estimates them with Grace: logs and old versions for Fairway's volumes cost a small monthly amount, and a lifecycle rule deletes old versions after ninety days to keep costs predictable.

### Recording

Each change record links to the review, the test result and the date applied.

### Rollback plan

Each change has a written rollback step, tested in staging, so it can be undone quickly if needed.

### Sign-off

Grace signs off each change.

### Worked example

Moving the assets bucket to its own account takes a day of testing because the website must keep loading images. Tomás tests the new address in staging before switching.

> **Synthetic case.** Synthetic.

### Errors and limits

Account-wide settings can break legitimate uses; plan exceptions before enabling them.

### Exercises

- **EX037 — Account block.** Why move assets to another account? *Rubric:* 3 = so account-wide block can apply elsewhere; 2 = partial; 1 = none; 0 = none.
- **EX038 — Versioning.** What does versioning allow? *Rubric:* 3 = restoring deleted or overwritten files; 2 = partial; 1 = none; 0 = none.
- **EX039 — Change route.** How are changes made? *Rubric:* 3 = repository with review; 2 = partial; 1 = none; 0 = none.
- **EX040 — Testing.** Where were changes tested first? *Rubric:* 3 = staging bucket; 2 = partial; 1 = none; 0 = none.

### Synthesis

Configure controls through reviewed, tested changes.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Cloud and container security: verification

### Learning outcomes

You will (1) verify that controls are in place; (2) compare bucket settings with policy; (3) report differences.

### 11.1 Why verify

Configuring is not the same as confirming. Tomás verifies each bucket against the policy.

Section eleven point one develops cloud and container security verification with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eleven point one, Grace Mensah expects cloud claims to carry owners and dates.

Section eleven point one treats why verify reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point one, Fairway Logistics will not accept cloud work without a written trail.

### Lab — Lab — bucket verification

```python
"""Verify synthetic bucket settings against Fairway's storage policy (stdlib only)."""
policy = {"block_public_access": True, "encryption": True, "versioning": True, "access_logging": True}
buckets = {"manifests": {"block_public_access": True, "encryption": True, "versioning": False, "access_logging": True},
           "site-assets": {"block_public_access": False, "encryption": True, "versioning": True, "access_logging": False},
           "backups": {"block_public_access": True, "encryption": True, "versioning": True, "access_logging": True},
           "driver-photos": {"block_public_access": True, "encryption": False, "versioning": False, "access_logging": False}}
total = 0
for b, s in buckets.items():
    f = [k for k in policy if s[k] != policy[k]]; total += len(f)
    print(f"{b}: {'OK' if not f else 'differs: ' + ', '.join(f)}")
print(f"{total} differences across {len(buckets)} buckets")
```

Run with `python3 lab_verify.py`. Verified output:

```text
manifests: differs: versioning
site-assets: differs: block_public_access, access_logging
backups: OK
driver-photos: differs: encryption, versioning, access_logging
6 differences across 4 buckets
```

### 11.2 Reading the result

Six differences across four buckets. Manifests lacks versioning. Site-assets has no public block, which is expected under its exception, and no access logging. Backups passes. Driver-photos lacks encryption, versioning and logging.

Section eleven point two develops cloud and container security verification with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eleven point two, Grace Mensah expects cloud claims to carry owners and dates.

Section eleven point two treats why verify reading the as testable only when evidence and ticket IDs are recorded.

### 11.3 Acting

Driver-photos is the most serious because it holds personal data unencrypted. It is fixed first. Site-assets logging is added; its public access is recorded as the approved exception.

Section eleven point three develops cloud and container security verification with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eleven point three, Grace Mensah expects cloud claims to carry owners and dates.

Section eleven point three treats why verify reading the as testable only when evidence and ticket IDs are recorded.

### 11.4 Re-check

After fixes, the check shows only the approved exception.

Section eleven point four develops cloud and container security verification with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eleven point four, Grace Mensah expects cloud claims to carry owners and dates.

Section eleven point four treats why verify reading the as testable only when evidence and ticket IDs are recorded.

For section eleven point four, Fairway Logistics will not accept cloud work without a written trail.

Section eleven point four fails closed if cloud evidence is missing rather than guessing.

### Why verification found more

The original incident concerned only manifests, but verification across all buckets found problems elsewhere. This is common: one incident reveals a pattern. Checking every bucket against the same policy finds similar gaps before they cause their own incidents.

Tomás reports the findings in order of data sensitivity, not in the order the script prints them, so readers see the most important first.

### Evidence of fixes

After fixes, the check output is saved as evidence, alongside the change records.

### Exceptions register

The site-assets exception is recorded with owner, reason and annual review date.

### Next run

The check is scheduled daily so new buckets are covered automatically.

### Owner sign-off

Each bucket owner confirms the fixes for their bucket, and the confirmation is stored with the evidence.

### Lessons

Verification across all buckets, not just the one in the incident, found the most serious problem. Tomás recommends checking every similar resource after any incident.

### Worked example

Grace asks why driver-photos was missed. Tomás finds it was created by a mobile app project using a copied example with no encryption setting.

> **Synthetic case.** Synthetic.

### Errors and limits

Verification checks settings, not that data was never exposed.

### Exercises

- **EX041 — Lab total.** How many differences, across how many buckets? *Rubric:* 3 = 6 across 4; 2 = partial; 1 = none; 0 = none.
- **EX042 — Worst bucket.** Which bucket was fixed first and why? *Rubric:* 3 = driver-photos; personal data unencrypted; 2 = partial; 1 = none; 0 = none.
- **EX043 — Approved exception.** Which difference is acceptable? *Rubric:* 3 = site-assets public access; 2 = partial; 1 = none; 0 = none.
- **EX044 — Root cause.** Why was driver-photos misconfigured? *Rubric:* 3 = copied example; 2 = partial; 1 = none; 0 = none.

### Synthesis

Verify after configuring, and fix the worst first.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) search synthetic configuration files for secret-like keys; (2) handle findings safely; (3) move secrets to a vault.

### 12.1 Purpose

During verification Tomás saw a note mentioning a storage key. He checks whether secrets sit in configuration files.

Section twelve point one develops contained laboratory with a Fairway Logistics note Tomás Reyes can demo offline.

Under section twelve point one, Grace Mensah expects contained claims to carry owners and dates.

Section twelve point one treats purpose reading the result as testable only when evidence and ticket IDs are recorded.

For section twelve point one, Fairway Logistics will not accept contained work without a written trail.

### Lab — Lab — secret-like keys

```python
"""Find secret-like key names in synthetic config files without printing values (stdlib only)."""
import re
files = {"app.env": "DB_HOST=db.internal\nDB_PASSWORD=<redacted>\nLOG_LEVEL=info",
         "deploy.yaml": "image: registry.fairway.example/tracker:4.2\nreplicas: 2",
         "notes.txt": "storage key moved to vault on 03-06",
         "worker.env": "QUEUE=jobs\nAPI_TOKEN=<redacted>\nCLOUD_SECRET_KEY=<redacted>"}
pat = re.compile(r"^([A-Z_]*(PASSWORD|TOKEN|SECRET)[A-Z_]*)=", re.M)
hits = {f: [m.group(1) for m in pat.finditer(t)] for f, t in files.items()}
for f, h in hits.items():
    if h: print(f"{f}: {', '.join(h)}")
print(f"{sum(len(h) for h in hits.values())} secret-like keys in {sum(1 for h in hits.values() if h)} of {len(files)} files")
```

Run with `python3 lab_secrets.py`. Verified output:

```text
app.env: DB_PASSWORD
worker.env: API_TOKEN, CLOUD_SECRET_KEY
3 secret-like keys in 2 of 4 files
```

### 12.2 Reading the result

Three secret-like keys appear in two of four files: DB_PASSWORD in app.env, API_TOKEN and CLOUD_SECRET_KEY in worker.env. Values are not printed.

Section twelve point two develops contained laboratory with a Fairway Logistics note Tomás Reyes can demo offline.

Under section twelve point two, Grace Mensah expects contained claims to carry owners and dates.

Section twelve point two treats purpose reading the result as testable only when evidence and ticket IDs are recorded.

For section twelve point two, Fairway Logistics will not accept contained work without a written trail.

### 12.3 Handling

Each secret is moved to the provider's secret manager and the old values are rotated, since anyone who saw the files could have copied them.

Section twelve point three develops contained laboratory with a Fairway Logistics note Tomás Reyes can demo offline.

Under section twelve point three, Grace Mensah expects contained claims to carry owners and dates.

Section twelve point three treats purpose reading the result as testable only when evidence and ticket IDs are recorded.

For section twelve point three, Fairway Logistics will not accept contained work without a written trail.

### 12.4 Kubernetes secrets

The Kubernetes good-practice guide advises encrypting secrets at rest and limiting who can read them.

Section twelve point four develops contained laboratory with a Fairway Logistics note Tomás Reyes can demo offline.

Under section twelve point four, Grace Mensah expects contained claims to carry owners and dates.

Section twelve point four treats purpose reading the result as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Fairway Logistics will not accept contained work without a written trail.

### 12.5 Containment

The lab uses synthetic files; the real search is run read-only by Grace.

Section twelve point five develops contained laboratory with a Fairway Logistics note Tomás Reyes can demo offline.

Under section twelve point five, Grace Mensah expects contained claims to carry owners and dates.

Section twelve point five treats purpose reading the result as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Fairway Logistics will not accept contained work without a written trail.

Section twelve point five fails closed if contained evidence is missing rather than guessing.

### Why secrets end up in files

Developers often put credentials in environment files during testing and forget to remove them. Rahman et al. (2019) identified hard-coded secrets as a common security smell in infrastructure scripts. Fairway's files matched this pattern: the worker file was copied from a test setup.

Tomás adds a pipeline check that blocks commits containing secret-like key names with values, giving developers a message pointing to the secret manager instructions.

### Access to the secret manager

Only the workloads that need each secret can read it, using their own identities.

### Recording rotation

Each rotation is recorded with date, owner and confirmation that the old value no longer works.

### False matches

A key named TOKEN_COUNT would match the pattern without being a secret; reviewers check each hit.

### Worked example

Rotating CLOUD_SECRET_KEY breaks the worker until its new reference is deployed. Tomás schedules rotation for a quiet hour with the developer present.

> **Synthetic case.** Synthetic.

### Errors and limits

Name-based search misses secrets with unusual names; it is a first pass.

### Exercises

- **EX045 — Lab hits.** Which keys were found? *Rubric:* 3 = DB_PASSWORD, API_TOKEN, CLOUD_SECRET_KEY; 2 = two; 1 = one; 0 = none.
- **EX046 — Rotation.** Why rotate after moving? *Rubric:* 3 = values may have been copied; 2 = partial; 1 = none; 0 = none.
- **EX047 — Search limit.** What can name-based search miss? *Rubric:* 3 = unusual names; 2 = partial; 1 = none; 0 = none.
- **EX048 — Rotation plan.** How was the worker breakage managed? *Rubric:* 3 = quiet hour, developer present; 2 = partial; 1 = none; 0 = none.

### Synthesis

Find secrets by name, move them, and rotate.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Cloud and container security: troubleshooting

### Learning outcomes

You will (1) diagnose failures after security changes; (2) fix the specific cause; (3) keep services running.

### 13.1 After the block

Once the account-level public block is on, a marketing tool fails to load a brochure from the manifests account. Tomás reads the error: access denied.

Section thirteen point one develops cloud and container security troubleshooting with a Fairway Logistics note Tomás Reyes can demo offline.

Under section thirteen point one, Grace Mensah expects cloud claims to carry owners and dates.

Section thirteen point one treats after the block method as testable only when evidence and ticket IDs are recorded.

For section thirteen point one, Fairway Logistics will not accept cloud work without a written trail.

### 13.2 Method

Read the error, list recent changes, reproduce in staging, find the smallest correct fix, record it.

Section thirteen point two develops cloud and container security troubleshooting with a Fairway Logistics note Tomás Reyes can demo offline.

Under section thirteen point two, Grace Mensah expects cloud claims to carry owners and dates.

Section thirteen point two treats after the block method as testable only when evidence and ticket IDs are recorded.

For section thirteen point two, Fairway Logistics will not accept cloud work without a written trail.

### 13.3 Finding

The brochure was stored in the wrong bucket. Moving it to the assets account fixes the problem without weakening the block.

Section thirteen point three develops cloud and container security troubleshooting with a Fairway Logistics note Tomás Reyes can demo offline.

Under section thirteen point three, Grace Mensah expects cloud claims to carry owners and dates.

Section thirteen point three treats after the block method as testable only when evidence and ticket IDs are recorded.

For section thirteen point three, Fairway Logistics will not accept cloud work without a written trail.

### 13.4 Another case

The CI deploy pipeline fails after its permissions are narrowed: it needs to clear a cache path in site-assets. A single extra permission solves it.

Section thirteen point four develops cloud and container security troubleshooting with a Fairway Logistics note Tomás Reyes can demo offline.

Under section thirteen point four, Grace Mensah expects cloud claims to carry owners and dates.

Section thirteen point four treats after the block method as testable only when evidence and ticket IDs are recorded.

For section thirteen point four, Fairway Logistics will not accept cloud work without a written trail.

### 13.5 Rollback rule

If a fix is not found within an hour during business hours, the change is reversed and retried later.

Section thirteen point five develops cloud and container security troubleshooting with a Fairway Logistics note Tomás Reyes can demo offline.

Under section thirteen point five, Grace Mensah expects cloud claims to carry owners and dates.

Section thirteen point five treats after the block method as testable only when evidence and ticket IDs are recorded.

For section thirteen point five, Fairway Logistics will not accept cloud work without a written trail.

### 13.6 Guide

Each case goes into a short troubleshooting guide.

Section thirteen point six develops cloud and container security troubleshooting with a Fairway Logistics note Tomás Reyes can demo offline.

Under section thirteen point six, Grace Mensah expects cloud claims to carry owners and dates.

Section thirteen point six treats after the block method as testable only when evidence and ticket IDs are recorded.

For section thirteen point six, Fairway Logistics will not accept cloud work without a written trail.

Section thirteen point six fails closed if cloud evidence is missing rather than guessing.

### Communicating breakages

When a security change breaks something, Tomás posts in the team channel what broke, why, and the fix. Being open about breakages builds trust; teams learn that security changes are handled carefully and that reporting problems gets them fixed quickly.

He also records how long each breakage lasted. Both cases in March were fixed within thirty minutes.

### Testing before changes

Most breakages could have been found in staging if staging had matched production. Tomás adds the marketing tool to staging tests.

### Guide format

The guide uses symptom, cause, fix and a link to the change.

### After action

Each breakage gets a short note in the guide within a day.

### Metrics

Breakage counts are tracked monthly.

### Worked example

A colleague suggests turning the block off "just for today". Tomás explains the risk and finds the misplaced brochure within twenty minutes.

> **Synthetic case.** Synthetic.

### Errors and limits

Disabling a control to fix a symptom often reintroduces the original risk.

### Exercises

- **EX049 — Brochure fix.** What fixed the brochure error? *Rubric:* 3 = moving it to assets account; 2 = partial; 1 = none; 0 = none.
- **EX050 — CI need.** What did CI deploy need? *Rubric:* 3 = clear a cache path in site-assets; 2 = partial; 1 = none; 0 = none.
- **EX051 — Rollback rule.** State the rollback rule. *Rubric:* 3 = reverse if no fix in an hour; 2 = partial; 1 = none; 0 = none.
- **EX052 — Colleague suggestion.** Why not turn the block off for a day? *Rubric:* 3 = reintroduces the risk; 2 = partial; 1 = none; 0 = none.

### Synthesis

Fix the specific cause and keep controls on.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Cloud and container security: automation

### Learning outcomes

You will (1) automate checks and alerts; (2) alert on public access changes; (3) keep automation reviewable.

### 14.1 Daily check

The verification script runs daily in the pipeline and posts results to the team channel.

Section fourteen point one develops cloud and container security automation with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fourteen point one, Grace Mensah expects cloud claims to carry owners and dates.

Section fourteen point one treats daily check change alert as testable only when evidence and ticket IDs are recorded.

For section fourteen point one, Fairway Logistics will not accept cloud work without a written trail.

### 14.2 Change alert

An alert fires within minutes if any bucket policy changes to public, using the provider's event notifications.

Section fourteen point two develops cloud and container security automation with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fourteen point two, Grace Mensah expects cloud claims to carry owners and dates.

Section fourteen point two treats daily check change alert as testable only when evidence and ticket IDs are recorded.

For section fourteen point two, Fairway Logistics will not accept cloud work without a written trail.

### 14.3 Pipeline rules

Infrastructure code that sets public access or disables encryption is blocked before merge, with a clear message. Rahman et al. (2019) found such smells recur in infrastructure code.

Section fourteen point three develops cloud and container security automation with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fourteen point three, Grace Mensah expects cloud claims to carry owners and dates.

Section fourteen point three treats daily check change alert as testable only when evidence and ticket IDs are recorded.

### 14.4 Review

Automation scripts are reviewed like application code.

Section fourteen point four develops cloud and container security automation with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fourteen point four, Grace Mensah expects cloud claims to carry owners and dates.

Section fourteen point four treats daily check change alert as testable only when evidence and ticket IDs are recorded.

For section fourteen point four, Fairway Logistics will not accept cloud work without a written trail.

Section fourteen point four fails closed if cloud evidence is missing rather than guessing.

### 14.5 Noise

Alerts must lead to action; the assets account is excluded to avoid constant alerts.

Section fourteen point five develops cloud and container security automation with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fourteen point five, Grace Mensah expects cloud claims to carry owners and dates.

Section fourteen point five treats daily check change alert as testable only when evidence and ticket IDs are recorded.

For section fourteen point five, Fairway Logistics will not accept cloud work without a written trail.

### 14.6 Ownership

Grace owns the alert; Tomás maintains the scripts.

Section fourteen point six develops cloud and container security automation with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fourteen point six, Grace Mensah expects cloud claims to carry owners and dates.

Section fourteen point six treats daily check change alert as testable only when evidence and ticket IDs are recorded.

For section fourteen point six, Fairway Logistics will not accept cloud work without a written trail.

Section fourteen point six fails closed if cloud evidence is missing rather than guessing.

### Testing the automation

Every alert and check is tested with a synthetic change in staging when first created and then every quarter. A drill confirms that the alert fires, reaches the right channel and that the runbook is followed. Without drills, a broken alert could stay silent for months.

Tomás records drill results with the time to alert and the time to response.

### Event sources

The alert uses the provider's management events for policy changes, which are recorded even without data access logging.

### Failure of automation

If the daily check fails to run, it posts a failure message rather than staying silent.

### Change control

Changes to alert rules go through review, so nobody can quietly disable them; the history shows who changed what and when.

### Documentation

Each automated check links to its runbook in the alert message, so responders know what to do immediately.

### Worked example

A test change in staging sets a bucket public. The alert arrives in four minutes, the on-call engineer checks the change, and the test is recorded as a successful drill.

> **Synthetic case.** Synthetic.

### Errors and limits

Automation catches known patterns; new services may need new checks.

### Exercises

- **EX053 — Alert speed.** How fast did the drill alert arrive? *Rubric:* 3 = four minutes; 2 = partial; 1 = none; 0 = none.
- **EX054 — Pipeline block.** What infrastructure changes are blocked? *Rubric:* 3 = public access, disabled encryption; 2 = partial; 1 = none; 0 = none.
- **EX055 — Exclusion.** Why exclude the assets account? *Rubric:* 3 = avoid constant alerts; 2 = partial; 1 = none; 0 = none.
- **EX056 — Owners.** Who owns the alert and scripts? *Rubric:* 3 = Grace; Tomás; 2 = partial; 1 = none; 0 = none.

### Synthesis

Automate checks and alerts with clear owners.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Cloud and container security: integration and dependencies

### Learning outcomes

You will (1) provide a secure partner file service; (2) manage dependencies on external services; (3) review images used in the cluster.

### 15.1 The missing service

The incident began because there was no approved way to share files with partners. Fairway sets up time-limited signed links that expire after 24 hours.

Section fifteen point one develops cloud and container security integration with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fifteen point one, Grace Mensah expects cloud claims to carry owners and dates.

Section fifteen point one treats the missing service partner as testable only when evidence and ticket IDs are recorded.

For section fifteen point one, Fairway Logistics will not accept cloud work without a written trail.

### 15.2 Partner agreement

The partner agrees to download promptly and delete copies after processing.

Section fifteen point two develops cloud and container security integration with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fifteen point two, Grace Mensah expects cloud claims to carry owners and dates.

Section fifteen point two treats the missing service partner as testable only when evidence and ticket IDs are recorded.

For section fifteen point two, Fairway Logistics will not accept cloud work without a written trail.

### 15.3 Dependencies

The tracking site depends on a base image, a mapping service and the email provider. Each dependency is listed with an owner.

Section fifteen point three develops cloud and container security integration with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fifteen point three, Grace Mensah expects cloud claims to carry owners and dates.

Section fifteen point three treats the missing service partner as testable only when evidence and ticket IDs are recorded.

For section fifteen point three, Fairway Logistics will not accept cloud work without a written trail.

### 15.4 Images

Shu et al. (2017) found many public images contained vulnerabilities; Fairway builds its images from a maintained base in its own registry.

Section fifteen point four develops cloud and container security integration with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fifteen point four, Grace Mensah expects cloud claims to carry owners and dates.

Section fifteen point four treats the missing service partner as testable only when evidence and ticket IDs are recorded.

For section fifteen point four, Fairway Logistics will not accept cloud work without a written trail.

### 15.5 Container guidance

NIST SP 800-190 advises using trusted registries and monitoring images for vulnerabilities.

Section fifteen point five develops cloud and container security integration with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fifteen point five, Grace Mensah expects cloud claims to carry owners and dates.

Section fifteen point five treats the missing service partner as testable only when evidence and ticket IDs are recorded.

For section fifteen point five, Fairway Logistics will not accept cloud work without a written trail.

### 15.6 Reviews

New dependencies require a short review.

Section fifteen point six develops cloud and container security integration with a Fairway Logistics note Tomás Reyes can demo offline.

Under section fifteen point six, Grace Mensah expects cloud claims to carry owners and dates.

Section fifteen point six treats the missing service partner as testable only when evidence and ticket IDs are recorded.

For section fifteen point six, Fairway Logistics will not accept cloud work without a written trail.

Section fifteen point six fails closed if cloud evidence is missing rather than guessing.

### Managing the partner relationship

The partner is asked to confirm in writing how they store and delete files, and Fairway records the answer in its supplier register. Each year the account manager checks that nothing has changed. This reflects the shared responsibility idea beyond cloud providers: once a file leaves Fairway, the partner's practices matter.

Tomás also asks whether the partner needs full manifests. They need only parcel identifiers and postcodes, so the export is reduced.

### Dependency list

The dependency list records each external service, data it receives, owner and review date.

### Image updates

Base images are rebuilt monthly, and the inventory confirms the cluster runs the new version.

### Approval

New partners must use signed links; any other method needs Grace's written approval.

### Review of reduced export

The partner confirms the reduced export meets their needs, and the change is recorded.

### Worked example

The partner tests a signed link. It works, expires as planned, and the partner confirms the process is easier than before.

> **Synthetic case.** Synthetic.

### Errors and limits

Signed links can still be forwarded; keep expiry short.

### Exercises

- **EX057 — Sharing method.** What sharing method replaced the public bucket? *Rubric:* 3 = signed links expiring in 24h; 2 = partial; 1 = none; 0 = none.
- **EX058 — Partner duties.** What did the partner agree? *Rubric:* 3 = download promptly, delete after; 2 = partial; 1 = none; 0 = none.
- **EX059 — Image source.** Where does Fairway build images from? *Rubric:* 3 = maintained base in own registry; 2 = partial; 1 = none; 0 = none.
- **EX060 — Link risk.** What risk remains with signed links? *Rubric:* 3 = forwarding; 2 = partial; 1 = none; 0 = none.

### Synthesis

Provide safe ways to do needed work so people need not improvise.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) document configurations and procedures; (2) write for the next person; (3) keep safety boundaries.

### 16.1 What to document

Storage policy, exceptions, check scripts, alert runbook, partner sharing procedure.

Section sixteen point one develops technical documentation and safety with a Fairway Logistics note Tomás Reyes can demo offline.

Under section sixteen point one, Grace Mensah expects technical claims to carry owners and dates.

Section sixteen point one treats what to document runbooks as testable only when evidence and ticket IDs are recorded.

For section sixteen point one, Fairway Logistics will not accept technical work without a written trail.

Section sixteen point one fails closed if technical evidence is missing rather than guessing.

### 16.2 Runbooks

The alert runbook says what the alert means, how to check, how to revert and who to tell.

Section sixteen point two develops technical documentation and safety with a Fairway Logistics note Tomás Reyes can demo offline.

Under section sixteen point two, Grace Mensah expects technical claims to carry owners and dates.

Section sixteen point two treats what to document runbooks as testable only when evidence and ticket IDs are recorded.

For section sixteen point two, Fairway Logistics will not accept technical work without a written trail.

### 16.3 Plain writing

Short sentences, numbered steps and no unexplained acronyms.

Section sixteen point three develops technical documentation and safety with a Fairway Logistics note Tomás Reyes can demo offline.

Under section sixteen point three, Grace Mensah expects technical claims to carry owners and dates.

Section sixteen point three treats what to document runbooks as testable only when evidence and ticket IDs are recorded.

For section sixteen point three, Fairway Logistics will not accept technical work without a written trail.

Section sixteen point three fails closed if technical evidence is missing rather than guessing.

### 16.4 Safety

Documents never include secret values or customer data.

Section sixteen point four develops technical documentation and safety with a Fairway Logistics note Tomás Reyes can demo offline.

Under section sixteen point four, Grace Mensah expects technical claims to carry owners and dates.

Section sixteen point four treats what to document runbooks as testable only when evidence and ticket IDs are recorded.

For section sixteen point four, Fairway Logistics will not accept technical work without a written trail.

Section sixteen point four fails closed if technical evidence is missing rather than guessing.

### 16.5 Review

Grace reviews every document; a colleague follows each runbook once.

Section sixteen point five develops technical documentation and safety with a Fairway Logistics note Tomás Reyes can demo offline.

Under section sixteen point five, Grace Mensah expects technical claims to carry owners and dates.

Section sixteen point five treats what to document runbooks as testable only when evidence and ticket IDs are recorded.

For section sixteen point five, Fairway Logistics will not accept technical work without a written trail.

Section sixteen point five fails closed if technical evidence is missing rather than guessing.

### 16.6 Location

Documents live beside the code they describe.

Section sixteen point six develops technical documentation and safety with a Fairway Logistics note Tomás Reyes can demo offline.

Under section sixteen point six, Grace Mensah expects technical claims to carry owners and dates.

Section sixteen point six treats what to document runbooks as testable only when evidence and ticket IDs are recorded.

For section sixteen point six, Fairway Logistics will not accept technical work without a written trail.

Section sixteen point six fails closed if technical evidence is missing rather than guessing.

### Documentation for auditors

Auditors want to see policy, evidence that controls run and records of exceptions. Tomás organises the documentation so each policy rule links to its check, latest output and any exception. When Fairway's insurer asks about cloud storage controls after the incident, Grace answers with links in under an hour.

The documentation also records the incident review and actions, showing that lessons led to changes.

### Writing style

Tomás uses headings that match questions readers ask, such as "What do I do when the alert fires?"

### Versioning documents

Documents are versioned with the code, so the history shows when procedures changed.

### Diagrams

A single diagram shows where checks run and where alerts go.

### Safety boundaries

The documents describe defensive checks only and state that testing outside scope is not permitted.

### Ownership

Each document names an owner responsible for keeping it accurate and a review date six months ahead. Owners receive a reminder when the date arrives.

### Feedback loop

Readers can comment on any document, and the owner responds within a week. Comments often reveal steps that seemed obvious to the writer but not to readers.

### Worked example

A colleague following the runbook gets stuck on "revert via IaC". Tomás adds the exact command and the file path.

> **Synthetic case.** Synthetic.

### Errors and limits

Documents decay; give each a review date.

### Exercises

- **EX061 — Runbook contents.** What does the alert runbook cover? *Rubric:* 3 = meaning, check, revert, tell; 2 = three; 1 = two; 0 = none.
- **EX062 — Safety rule.** What must documents never include? *Rubric:* 3 = secret values, customer data; 2 = partial; 1 = none; 0 = none.
- **EX063 — Test.** How is each runbook tested? *Rubric:* 3 = colleague follows it; 2 = partial; 1 = none; 0 = none.
- **EX064 — Fix.** What did the stuck colleague's test lead to? *Rubric:* 3 = exact command and path added; 2 = partial; 1 = none; 0 = none.

### Synthesis

Write for the next person and test the writing.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) detect drift between declared and live settings; (2) decide which drift to fix; (3) prevent recurrence.

### 17.1 Drift

Drift is a difference between what the repository declares and what is live, usually from manual changes.

Section seventeen point one develops contained laboratory ii with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seventeen point one, Grace Mensah expects contained claims to carry owners and dates.

Section seventeen point one treats drift reading the result as testable only when evidence and ticket IDs are recorded.

For section seventeen point one, Fairway Logistics will not accept contained work without a written trail.

### Lab — Lab — drift check

```python
"""Compare declared (repository) settings with live settings to find drift (synthetic, stdlib only)."""
declared = {"manifests.block_public_access": True, "manifests.versioning": True, "site-assets.access_logging": True,
            "cluster.audit_logging": True, "cluster.public_endpoint": False, "tracker.replicas": 2, "tracker.run_as_root": False}
live = dict(declared, **{"site-assets.access_logging": False, "cluster.public_endpoint": True, "tracker.replicas": 3})
drift = [(k, declared[k], live[k]) for k in declared if declared[k] != live[k]]
print(f"settings {len(declared)}, drifted {len(drift)}")
for k, d, l in drift: print(f"  {k}: declared {d}, live {l}")
```

Run with `python3 lab_drift.py`. Verified output:

```text
settings 7, drifted 3
  site-assets.access_logging: declared True, live False
  cluster.public_endpoint: declared False, live True
  tracker.replicas: declared 2, live 3
```

### 17.2 Reading the result

Three of seven settings drifted: site-assets access logging is off, the cluster public endpoint is on, and tracker replicas are 3 instead of 2.

Section seventeen point two develops contained laboratory ii with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seventeen point two, Grace Mensah expects contained claims to carry owners and dates.

Section seventeen point two treats drift reading the result as testable only when evidence and ticket IDs are recorded.

For section seventeen point two, Fairway Logistics will not accept contained work without a written trail.

### 17.3 Judging

The public endpoint matters most; logging next; replicas were raised during a busy week and are harmless but should be declared.

Section seventeen point three develops contained laboratory ii with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seventeen point three, Grace Mensah expects contained claims to carry owners and dates.

Section seventeen point three treats drift reading the result as testable only when evidence and ticket IDs are recorded.

For section seventeen point three, Fairway Logistics will not accept contained work without a written trail.

### 17.4 Fixing

The endpoint is restored to private through the repository; logging re-enabled; replicas updated in the repository to match.

Section seventeen point four develops contained laboratory ii with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seventeen point four, Grace Mensah expects contained claims to carry owners and dates.

Section seventeen point four treats drift reading the result as testable only when evidence and ticket IDs are recorded.

For section seventeen point four, Fairway Logistics will not accept contained work without a written trail.

### 17.5 Prevention

The drift check runs nightly.

Section seventeen point five develops contained laboratory ii with a Fairway Logistics note Tomás Reyes can demo offline.

Under section seventeen point five, Grace Mensah expects contained claims to carry owners and dates.

Section seventeen point five treats drift reading the result as testable only when evidence and ticket IDs are recorded.

For section seventeen point five, Fairway Logistics will not accept contained work without a written trail.

Section seventeen point five fails closed if contained evidence is missing rather than guessing.

### Fix live or update the declaration

For each drift item, Tomás asks: was the live change needed and safe? If yes, update the repository so it becomes declared. If no, restore the live setting from the repository. The replicas change was needed and safe; the endpoint change was unsafe; logging being off was an accident. Writing the decision for each item keeps the repository as the single source of truth.

He adds a rule: urgent manual changes must be recorded in the repository within one working day.

### Vendor access

Vendor access now uses a temporary account on the private network that expires after the session.

### Nightly results

Nightly drift results are posted with a count, so a rising number is noticed.

### Trend

After a month, nightly drift averages under one item.

### Recording

Each drift decision is logged with reasons and date.

### Worked example

Tomás finds that the endpoint was opened during a support call to let a vendor connect. Grace arranges vendor access through the private network instead.

> **Synthetic case.** Synthetic.

### Errors and limits

Not all drift is bad; decide whether to fix live or update the declaration.

### Exercises

- **EX065 — Lab result.** Which settings drifted? *Rubric:* 3 = logging, endpoint, replicas; 2 = two; 1 = one; 0 = none.
- **EX066 — Priority.** Which drift mattered most? *Rubric:* 3 = public endpoint; 2 = partial; 1 = none; 0 = none.
- **EX067 — Replicas.** How was the replicas drift handled? *Rubric:* 3 = declaration updated; 2 = partial; 1 = none; 0 = none.
- **EX068 — Endpoint cause.** Why had the endpoint been opened? *Rubric:* 3 = vendor support call; 2 = partial; 1 = none; 0 = none.

### Synthesis

Compare declared and live often and decide each difference deliberately.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) complete a supervised project; (2) show measured results; (3) reflect.

### 18.1 Project

Tomás's project: a storage guardrail pack with policy, verification, alerts, drift check, sharing procedure and runbooks.

Section eighteen point one develops supervised technical project with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eighteen point one, Grace Mensah expects supervised claims to carry owners and dates.

Section eighteen point one treats project results limits presentation as testable only when evidence and ticket IDs are recorded.

For section eighteen point one, Fairway Logistics will not accept supervised work without a written trail.

### 18.2 Results

Bucket differences fell from 6 to 1 approved exception; drift fell from 3 to 0; public change alert tested at four minutes.

Section eighteen point two develops supervised technical project with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eighteen point two, Grace Mensah expects supervised claims to carry owners and dates.

Section eighteen point two treats project results limits presentation as testable only when evidence and ticket IDs are recorded.

For section eighteen point two, Fairway Logistics will not accept supervised work without a written trail.

### 18.3 Limits

Results cover one company and a few months.

Section eighteen point three develops supervised technical project with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eighteen point three, Grace Mensah expects supervised claims to carry owners and dates.

Section eighteen point three treats project results limits presentation as testable only when evidence and ticket IDs are recorded.

For section eighteen point three, Fairway Logistics will not accept supervised work without a written trail.

Section eighteen point three fails closed if supervised evidence is missing rather than guessing.

### 18.4 Presentation

He presents to Hollins tutors and Fairway's IT manager.

Section eighteen point four develops supervised technical project with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eighteen point four, Grace Mensah expects supervised claims to carry owners and dates.

Section eighteen point four treats project results limits presentation as testable only when evidence and ticket IDs are recorded.

For section eighteen point four, Fairway Logistics will not accept supervised work without a written trail.

Section eighteen point four fails closed if supervised evidence is missing rather than guessing.

### 18.5 Reflection

He learned that the incident was a process gap as much as a technical one.

Section eighteen point five develops supervised technical project with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eighteen point five, Grace Mensah expects supervised claims to carry owners and dates.

Section eighteen point five treats project results limits presentation as testable only when evidence and ticket IDs are recorded.

For section eighteen point five, Fairway Logistics will not accept supervised work without a written trail.

### 18.6 Next

He plans to study application security next.

Section eighteen point six develops supervised technical project with a Fairway Logistics note Tomás Reyes can demo offline.

Under section eighteen point six, Grace Mensah expects supervised claims to carry owners and dates.

Section eighteen point six treats project results limits presentation as testable only when evidence and ticket IDs are recorded.

For section eighteen point six, Fairway Logistics will not accept supervised work without a written trail.

Section eighteen point six fails closed if supervised evidence is missing rather than guessing.

### Assessment

Tutors assess the project against criteria agreed at the start: working checks, measured results, documentation tested by another person and honest limits. Tomás meets all four. The tutors note that his timeline in chapter 7 was clear and well evidenced, and suggest that future work could include cost tracking for logging and versioning.

Grace's feedback highlights his habit of testing on synthetic data with known answers before running checks.

### Course review

The course moved from understanding Fairway's services, networks and identities, through scope and evidence, to the timeline, causes, policy, configuration, verification, secrets, troubleshooting, automation, partner integration, documentation and drift.

### Handover

Before finishing, Tomás hands the scripts and runbooks to the IT team with a short walkthrough.

### Safety

All work used synthetic data or read-only access under supervision.

### Thanks

He thanks Grace and the developers who joined the reviews.

### Future work

Next steps are cost tracking and a check for new accounts.

### Closing

The project closes with all actions done.

### Worked example

The IT manager asks what would happen if another team opened a new cloud account. Tomás explains that the account-level block and alerts must be applied to new accounts as part of setup, and adds it to the checklist.

> **Synthetic case.** Synthetic.

### Errors and limits

Projects judged only on tools miss process changes.

### Exercises

- **EX069 — Pack contents.** What is in the guardrail pack? *Rubric:* 3 = policy, verification, alerts, drift, sharing, runbooks; 2 = four; 1 = two; 0 = none.
- **EX070 — Results.** Give the measured results. *Rubric:* 3 = 6→1 differences, 3→0 drift, 4-minute alert; 2 = two; 1 = one; 0 = none.
- **EX071 — New accounts.** What was added for new accounts? *Rubric:* 3 = block and alerts at setup; 2 = partial; 1 = none; 0 = none.
- **EX072 — Lesson.** What did Tomás learn about the incident? *Rubric:* 3 = process gap as well as technical; 2 = partial; 1 = none; 0 = none.

### Synthesis

Show measured results and the process changes behind them.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Tomás Reyes, Grace Mensah, Hollins Technical College, Fairway Logistics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A developer made the manifests bucket public for a partner and it stayed public about three days.

**EX002.** Close to platform as a service, because the provider runs the control plane.

**EX003.** It shows where Fairway itself must configure security.

**EX004.** The partner file transfer; its absence led to the improvised public bucket.

**EX005.** Who is allowed to read the data.

**EX006.** Buckets are reachable over the internet by name.

**EX007.** The bucket was reached via the provider's endpoint, so only access policy controls it.

**EX008.** The managed database.

**EX009.** Permission to change bucket policies.

**EX010.** To upload and read objects, not change policies.

**EX011.** To the site-assets bucket only.

**EX012.** Developer, operator and auditor.

**EX013.** YAML.

**EX014.** It runs anywhere without unreviewed packages.

**EX015.** The key name and file, never the value.

**EX016.** A count at the top and a comment on the expected value.

**EX017.** Partner systems.

**EX018.** Grace and the IT manager.

**EX019.** Who exported it, when and from which account.

**EX020.** So others can check the reasoning.

**EX021.** Backups, manifests with addresses and driver photos.

**EX022.** Only the assets bucket.

**EX023.** Public access blocks, least privilege, encryption and logging.

**EX024.** The storage infrastructure.

**EX025.** From 3 March 16:41 to 6 March 10:02.

**EX026.** Two, from addresses matching the partner.

**EX027.** That no other copies exist.

**EX028.** Fairway's data protection lead.

**EX029.** Missing sharing service, broad permission, no guardrail.

**EX030.** Process, access, technical.

**EX031.** Account-level public access blocking.

**EX032.** Obscurity is not access control; links get shared.

**EX033.** Reading exports, provider policy tools, scanners.

**EX034.** Block public access, encrypt, version, log access.

**EX035.** The assets bucket may be publicly readable.

**EX036.** To explain the policy to auditors.

**EX037.** So the account-wide public block can apply to all other buckets.

**EX038.** Restoring deleted or overwritten files.

**EX039.** Through the configuration repository with review.

**EX040.** On a staging bucket.

**EX041.** Six across four buckets.

**EX042.** Driver-photos, because personal data was unencrypted.

**EX043.** Site-assets public access, under its exception.

**EX044.** It was created from a copied example without encryption.

**EX045.** DB_PASSWORD, API_TOKEN and CLOUD_SECRET_KEY.

**EX046.** Anyone who saw the files could have copied them.

**EX047.** Secrets with unusual key names.

**EX048.** Rotation at a quiet hour with the developer present.

**EX049.** Moving the brochure to the assets account.

**EX050.** Permission to clear one cache path in site-assets.

**EX051.** Reverse the change if no fix is found within an hour.

**EX052.** It reintroduces the original exposure risk.

**EX053.** Within four minutes.

**EX054.** Setting public access or disabling encryption.

**EX055.** To avoid alerts on intended public access.

**EX056.** Grace owns the alert; Tomás maintains scripts.

**EX057.** Time-limited signed links expiring after 24 hours.

**EX058.** To download promptly and delete copies after processing.

**EX059.** A maintained base in its own registry.

**EX060.** They can be forwarded before expiry.

**EX061.** Meaning, how to check, how to revert, who to tell.

**EX062.** Secret values or customer data.

**EX063.** A colleague follows it once.

**EX064.** Adding the exact command and file path.

**EX065.** Site-assets logging, cluster public endpoint, tracker replicas.

**EX066.** The cluster public endpoint.

**EX067.** The repository was updated to match.

**EX068.** For a vendor during a support call.

**EX069.** Policy, verification, alerts, drift check, sharing procedure and runbooks.

**EX070.** Differences 6→1 (approved), drift 3→0, alert in four minutes.

**EX071.** Applying the block and alerts during setup.

**EX072.** It was a process gap as much as technical.

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
