# Cloud and Container Security: Technologist Course

- Language: English (`en`); course 082, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; Seven offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students learning to build, run and improve practical cloud and container security at a small hosting company.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only cloud accounts, clusters and workloads you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Misconfigurations are taught from the defender's side using synthetic configurations, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one student on placement at a hosting company, from a six-hour search for workloads affected by an image advisory, through foundations, inventory, data flows, baselines, workload controls, monitoring, automation and evaluation, to a handoff, a field response and a capstone. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Priya Nair** | Technologist student on placement | Invented |
| **Kwame Asante** | Placement mentor | Invented |
| **Cobalt Hosting** | Fictional hosting company | Invented |
| **Northgate Polytechnic** | Fictional polytechnic | Invented |
| **Riverside Dental Group** | Fictional client | Invented |

### Core sources

NIST [SP 800-145](https://doi.org/10.6028/NIST.SP.800-145), [SP 800-210](https://doi.org/10.6028/NIST.SP.800-210), [SP 800-190](https://doi.org/10.6028/NIST.SP.800-190) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); CSA [Cloud Controls Matrix v4](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); the [AWS](https://aws.amazon.com/compliance/shared-responsibility-model/), [Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) and [Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) shared responsibility pages; Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing systems

### Learning outcomes

You will (1) describe the parts of a computer that a cloud service still depends on; (2) explain processes, memory and storage in plain terms; (3) connect these ideas to the hosting work Priya will see on placement.

### 1.1 Starting the placement

Priya Nair is a technologist student at the fictional Northgate Polytechnic. In her second week on placement at the fictional Cobalt Hosting, a small company that runs websites and booking systems for local businesses, a security advisory arrives about an old Node.js base image. Her mentor, Kwame Asante, asks which client workloads use it. Answering takes the team six hours of searching. This course follows Priya as she learns why that question was hard and how to make it easy.

### 1.2 Hardware under the cloud

Cloud computing, as defined in NIST SP 800-145, lets customers use pooled computing resources on demand. The resources are still physical machines with processors, memory, disks and network cards, owned and operated by a provider. Knowing this helps Priya understand that a cloud server is a share of real hardware, not something abstract.

### 1.3 Processes and programs

A program is a file of instructions; a process is a running copy of it, with its own memory and permissions. A web server, a database and a backup job are separate processes. Security questions often start with which process is running, as which user, and with what access.

### 1.4 Memory and storage

Memory holds working data and disappears when power is lost. Storage keeps data on disk. In cloud systems, a container's own disk is often temporary, so anything worth keeping must go to separate storage, such as a managed database or a storage bucket.

### 1.5 Files and permissions

Operating systems record who owns each file and who may read, write or run it. Mistakes here, such as a configuration file readable by everyone, are common causes of exposure.

### Worked example

Kwame shows Priya a client's web server. She lists its processes and sees a web server, a scheduled report job and a log shipper. For each she records the user it runs as and what files it reads. The report job runs as an administrator account, which Kwame notes as something to fix later.

> **Synthetic case.** Priya, Kwame, Cobalt Hosting and its clients are synthetic.

### Errors and limits

Calling something "the cloud" can hide that it runs on real machines with real limits and owners.

### Exercises

- **EX001 — Placement trigger.** What question took the Cobalt team six hours to answer? *Rubric:* 3 = which client workloads used the old Node.js image; 2 = names the advisory only; 1 = vague; 0 = none.
- **EX002 — Process versus program.** Explain the difference between a program and a process. *Rubric:* 3 = file of instructions vs running copy with memory and permissions; 2 = one correct; 1 = vague; 0 = none.
- **EX003 — Temporary disks.** Why should data worth keeping not stay on a container's own disk? *Rubric:* 3 = it is often temporary; use separate storage; 2 = partial; 1 = none; 0 = none.

### Synthesis

Cloud services still run on processes, memory, storage and permissions; security starts with knowing what runs and as whom.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) explain addresses, ports and protocols; (2) describe how a web request reaches a hosted service; (3) identify where encryption protects traffic.

### 2.1 Addresses and ports

Each machine on a network has an address. A port number identifies a particular service on that machine, such as 443 for HTTPS. When a firewall rule allows a port, it allows anyone who can reach that address to talk to the service behind it.

### 2.2 A web request

When a dental patient opens Riverside Dental Group's booking page, their browser looks up the name using DNS, connects to Cobalt's proxy on port 443, and the proxy forwards the request to the web container. The response travels back the same way.

### 2.3 Encryption in transit

TLS encrypts traffic between browser and proxy so others on the network cannot read it. Traffic between services inside a cluster may or may not be encrypted; Priya learns to check rather than assume.

### 2.4 Private and public networks

Some services, such as databases, should only be reachable from inside a private network. Exposing them to the internet without need increases risk greatly.

### 2.5 Load balancers and proxies

A proxy or load balancer receives traffic and passes it on. It is a natural place to enforce TLS, limit request sizes and log requests.

### 2.6 Network diagrams

Kwame keeps a simple diagram for each client showing which parts face the internet. Priya notices that two diagrams are out of date.

### Worked example

Priya traces a request to the booking page step by step and writes each hop with its port and whether it is encrypted. She finds that the hop from proxy to web container uses TLS, but the hop from web to API inside the cluster does not. Kwame says this is acceptable for now inside the cluster, but it should be recorded as a known limit.

> **Synthetic case.** The booking system is synthetic.

### Errors and limits

A diagram is only useful if it is updated when the system changes.

### Exercises

- **EX004 — Port meaning.** What does allowing a port in a firewall rule permit? *Rubric:* 3 = anyone who can reach the address can use the service; 2 = partial; 1 = none; 0 = none.
- **EX005 — Request path.** Trace the booking page request from browser to container. *Rubric:* 3 = DNS, proxy on 443, forwarded to web container; 2 = two steps; 1 = one; 0 = none.
- **EX006 — Inside the cluster.** Which hop was not encrypted and how was it treated? *Rubric:* 3 = web to API; recorded as known limit; 2 = partial; 1 = none; 0 = none.

### Synthesis

Follow each request hop by hop and check encryption rather than assuming it.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) read short Python scripts; (2) use lists and dictionaries to hold records; (3) write small checks that print clear results.

### 3.1 Why scripting helps

The six-hour search happened because staff checked each client by hand. A short script that reads a list of workloads and prints which images they use could answer the same question in seconds.

### 3.2 Values, lists and dictionaries

A list holds items in order. A dictionary maps names to values, such as workload name to image. Most of the labs in this course use these two structures with synthetic data.

### 3.3 Loops and conditions

A loop goes through each item; a condition decides what to do with it. Together they let a script find every workload whose image is not on an approved list.

### 3.4 Clear output

A good check prints counts first and then the details, so a reader sees the size of the problem before the list. Priya adopts this habit.

### 3.5 Standard library only

The course labs use only Python's standard library, so they run anywhere without installing packages. This also avoids bringing in code that Cobalt has not reviewed.

### 3.6 Reading before running

Priya reads every script before running it, even one written by a colleague. Kwame says this is good practice for any code that touches client systems.

### Comments and names

Clear variable names such as approved_images and short comments make a script readable months later by someone else.

### Worked example

Priya writes a few lines that loop over a dictionary of workloads and print those whose image name starts with docker.io. It finds two workloads on its first run. She adds a count at the top of the output and a comment explaining what the script does.

> **Synthetic case.** Scripts and data are synthetic.

### Errors and limits

Scripts reflect the data they are given; if the list of workloads is incomplete, the answer is incomplete.

### Exercises

- **EX007 — Structure choice.** Which data structure maps workload names to images? *Rubric:* 3 = dictionary; 2 = list; 1 = none; 0 = none.
- **EX008 — Output order.** Why print counts before details? *Rubric:* 3 = reader sees size first; 2 = partial; 1 = none; 0 = none.
- **EX009 — Incomplete data.** What limits the accuracy of any inventory script? *Rubric:* 3 = completeness of input data; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small, readable scripts turn slow manual searches into quick, repeatable checks.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) model hosting assets as records; (2) choose fields that answer security questions; (3) keep records consistent.

### 4.1 What to record

To answer "which clients use this image?", Cobalt needs records linking client, cluster, workload and image. Priya drafts a simple model with those four fields plus an owner.

### 4.2 Consistent names

Two staff wrote the same image as "node14" and "node:14". Inconsistent names break searches. Priya proposes always recording the full image reference, including registry and tag.

### 4.3 Identifiers

Each record needs a unique identifier, so updates change the right row. Workload names alone are not unique because two clients both have a workload called web.

### 4.4 Tables and files

Records can live in a spreadsheet, a CSV file or a database. For now Cobalt uses a CSV file kept in its configuration repository, so changes are reviewed.

### 4.5 Keeping data current

A model is useful only if it is updated. Priya suggests generating the records from the clusters automatically each night rather than typing them.

### 4.6 Sensitive fields

The model avoids storing secrets or patient data; it describes systems, not people.

### Checking the model

Priya tests her model by asking it three real questions: which clients use a given image, which workloads belong to one owner, and which clusters hold a client's systems. If a question cannot be answered from the fields, the model needs another field. The test shows that she also needs the namespace, because two clients share one cluster, so she adds it.

### Worked example

Priya builds the CSV for three clients and finds that the same name "web" appears twice. She adds a client prefix to make identifiers unique, then re-runs her script, which now reports each client's images correctly.

> **Synthetic case.** Records are synthetic.

### Errors and limits

A model that tries to capture everything becomes too hard to maintain; start with fields that answer real questions.

### Exercises

- **EX010 — Model fields.** List the fields in Priya's first model. *Rubric:* 3 = client, cluster, workload, image, owner; 2 = three or four; 1 = fewer; 0 = none.
- **EX011 — Naming problem.** What naming problem did Priya find? *Rubric:* 3 = node14 vs node:14; use full image reference; 2 = partial; 1 = none; 0 = none.
- **EX012 — Unique ids.** How were duplicate workload names resolved? *Rubric:* 3 = client prefix; 2 = partial; 1 = none; 0 = none.

### Synthesis

Model only what answers real questions, and keep names and identifiers consistent.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain confidentiality, integrity and availability; (2) describe the shared responsibility model; (3) recognise common cloud security failures.

### 5.1 Three goals

Confidentiality keeps data from the wrong people, integrity keeps it accurate, and availability keeps it usable when needed. A booking system needs all three: patient details must stay private, appointments must be correct, and the site must be up.

### 5.2 Shared responsibility

AWS, Azure and Google Cloud each publish a shared responsibility model: the provider secures the underlying infrastructure, and the customer secures what they configure and run. Cobalt, as a hosting company, adds a third layer: it manages clusters for clients, who still own their data and users.

### 5.3 Common failures

Public storage buckets, overly broad permissions, unpatched images and missing logs appear again and again in cloud incidents. None requires a clever attacker; all are configuration problems.

### 5.4 Threats and vulnerabilities

A threat is something that could cause harm; a vulnerability is a weakness it could use. The old Node image is a vulnerability; whether it matters depends on how the workload is exposed.

### 5.5 Risk

Risk combines how likely harm is and how bad it would be. Priya learns to describe risk in words before using numbers.

### 5.6 Ethics of access

Placement students see client systems. Priya signs Cobalt's confidentiality agreement and only accesses what her tasks require.

### Words to use

Priya keeps a short glossary for client conversations, defining terms such as vulnerability and patch in one sentence each.

### Worked example

Kwame asks Priya who is responsible if a client's storage bucket is made public. She answers that the provider secures storage infrastructure, Cobalt is responsible if it configured the bucket, and the client is responsible for deciding which data goes there. Kwame agrees and adds that the contract should say this clearly.

> **Synthetic case.** Cobalt and its clients are synthetic.

### Errors and limits

The shared responsibility model divides duties; it does not remove any.

### Exercises

- **EX013 — Three goals.** Apply confidentiality, integrity and availability to the booking system. *Rubric:* 3 = private details, correct appointments, site up; 2 = two; 1 = one; 0 = none.
- **EX014 — Responsibility layers.** Describe the three responsibility layers at Cobalt. *Rubric:* 3 = provider infra, Cobalt config, client data/users; 2 = two; 1 = one; 0 = none.
- **EX015 — Configuration failures.** Name three common cloud failures that are configuration problems. *Rubric:* 3 = public buckets, broad permissions, unpatched images, missing logs; 2 = two; 1 = one; 0 = none.

### Synthesis

Security goals and responsibilities must be clear before controls make sense.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) explain virtual machines and containers; (2) compare their isolation; (3) describe what a container image contains.

### 6.1 Virtual machines

A virtual machine runs a full operating system on shared hardware, separated by a hypervisor. Cloud providers use this to run many customers on the same physical machine.

### 6.2 Containers

A container packages an application with the files it needs and runs it as an isolated process on a shared kernel. Containers start quickly and are small, which is why Cobalt uses them.

### 6.3 Isolation differences

Containers share the host kernel, so their isolation is weaker than separate virtual machines. NIST SP 800-190 advises grouping containers of similar sensitivity on the same hosts and keeping the host operating system minimal.

### 6.4 Images

An image is a layered file bundle from which containers start. It includes a base layer, often a small operating system, plus the application. The advisory affected the base layer, so every image built on it was affected.

### 6.5 Tags and digests

A tag such as node:14 is a label that can be moved; a digest identifies exact content. Recording digests gives a reliable answer to "what exactly is running?"

### 6.6 Running as root

Containers that run as root give more power to anyone who compromises them. Kubernetes Pod Security Standards discourage it in the Restricted profile.

### Hosts and nodes

In Kubernetes, the machines that run containers are called nodes. Keeping nodes updated matters because a kernel flaw affects every container on that node.

### Worked example

Priya inspects the booking workload's image record and sees it uses node:14 by tag. She looks up the digest from the registry and records both. Kwame explains that because the tag could have been moved, only the digest proves which content was running on the day of the advisory.

> **Synthetic case.** Image names are synthetic.

### Errors and limits

Container isolation is useful but not equal to virtual machine isolation.

### Exercises

- **EX016 — Shared kernel.** Why is container isolation weaker than VM isolation? *Rubric:* 3 = containers share the host kernel; 2 = partial; 1 = none; 0 = none.
- **EX017 — Base layer impact.** Why were many images affected by one advisory? *Rubric:* 3 = shared base layer; 2 = partial; 1 = none; 0 = none.
- **EX018 — Digest value.** What does a digest prove that a tag does not? *Rubric:* 3 = exact content; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know what is inside an image and pin it by digest when evidence matters.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) explain authentication and authorisation; (2) apply least privilege; (3) describe roles in cloud and Kubernetes.

### 7.1 Who and what

Authentication confirms who someone is; authorisation decides what they may do. In cloud systems, identities include people, services and automation such as the CI bot.

### 7.2 Least privilege

Each identity should have only the access it needs. Sandhu et al. (1996) describe role-based access control, where permissions are grouped into roles and roles assigned to users, making least privilege easier to manage.

### 7.3 Kubernetes RBAC

Kubernetes uses Roles and ClusterRoles to grant actions on resources, bound to users or service accounts. A ClusterRoleBinding to cluster-admin grants everything and should be rare.

### 7.4 Service accounts

Workloads run with service accounts. The default service account should have no extra permissions; each workload that needs API access gets its own account.

### 7.5 Leavers

When staff leave, their access must be removed. Priya finds an account called old-admin still active on one cluster.

### 7.6 Multi-factor authentication

Console access for staff requires a second factor, which greatly reduces the impact of stolen passwords.

### Reviewing access regularly

Kwame's team now reviews cluster-admin holders every month. The review takes ten minutes: export the bindings, compare with the staff list, and remove anything unexplained. Priya automates the export so the review only needs a person for the judgement, not the collection of data.

### Shared accounts

Shared logins hide who did what. Each person at Cobalt now has an individual account, so audit logs name a real person.

### Worked example

Priya lists who has cluster-admin on the client-b cluster: Kwame, the CI bot and old-admin. Kwame confirms old-admin belonged to a former employee. They remove it the same day, and Priya notes that the CI bot needs only deployment rights, not cluster-admin.

> **Synthetic case.** Accounts are synthetic.

### Errors and limits

Removing access can break automation that silently used it; test after changes.

### Exercises

- **EX019 — Authn versus authz.** Distinguish authentication from authorisation. *Rubric:* 3 = who you are vs what you may do; 2 = partial; 1 = none; 0 = none.
- **EX020 — Old account.** What did Priya find on client-b and what was done? *Rubric:* 3 = old-admin with cluster-admin; removed; 2 = partial; 1 = none; 0 = none.
- **EX021 — CI bot rights.** Which access does the CI bot actually need? *Rubric:* 3 = deployment rights only; 2 = partial; 1 = none; 0 = none.

### Synthesis

Give each identity only what it needs and remove what is no longer used.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) describe defence in depth; (2) place controls at layers of a hosting platform; (3) explain trust boundaries.

### 8.1 Layers

Defence in depth means several controls so one failure does not expose everything. For a client site: network rules, TLS at the proxy, admission rules in the cluster, least-privilege service accounts and logs.

### 8.2 Trust boundaries

A trust boundary is where data passes between areas with different levels of trust, such as internet to proxy or cluster to managed database. Controls cluster at boundaries.

### 8.3 Zero trust ideas

NIST SP 800-207 describes zero trust: no implicit trust based on network location; each request is authenticated and authorised. Cobalt does not need a full programme, but the idea supports checking service identities inside clusters.

### 8.4 Separation of clients

Cobalt runs each large client in its own cluster and smaller clients in separate namespaces of a shared cluster with network policies between them.

### 8.5 Simplicity

A design staff understand is more secure in practice than a complex one they work around.

### 8.6 Architecture records

Each client has a one-page architecture record with layers and boundaries.

### Architecture and clients

Small clients often assume that being hosted means being protected. The architecture record lets Cobalt show clients which layers it manages and which remain theirs, such as choosing strong passwords for their own staff accounts on the booking system.

### Reviewing the design

Kwame reviews each architecture record with the client once a year, checking whether new services added boundaries.

### Worked example

Priya draws Riverside Dental's architecture with four boundaries: internet to proxy, proxy to cluster, cluster to database, cluster to monitoring service. For each she lists the controls present and one that is missing: no network policy between the booking and reports workloads.

> **Synthetic case.** Architecture is synthetic.

### Errors and limits

Layers help only if each is maintained; an unmonitored control can fail silently.

### Exercises

- **EX022 — Defence in depth.** Give four layers protecting a client site. *Rubric:* 3 = network, TLS, admission, service accounts, logs; 2 = three; 1 = two; 0 = none.
- **EX023 — Boundary definition.** What makes a point in the system a trust boundary? *Rubric:* 3 = data moves between different trust levels; 2 = partial; 1 = none; 0 = none.
- **EX024 — Missing control.** Which control was missing at Riverside Dental? *Rubric:* 3 = network policy between booking and reports; 2 = partial; 1 = none; 0 = none.

### Synthesis

Put controls at each boundary and keep the design simple enough to maintain.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) collect evidence about system state; (2) define simple measures; (3) avoid misleading numbers.

### 9.1 What counts as evidence

Evidence is a record that shows the state of a system at a time: a configuration export, a log entry, an inventory file. A colleague saying "it is fine" is not evidence.

### 9.2 Timestamps and sources

Each piece of evidence needs when it was collected and from where, so others can check it.

### 9.3 Simple measures

Useful measures for Cobalt: share of workloads using approved images, number of baseline failures per cluster, and time to answer an advisory.

### 9.4 Baselines and trends

A single number means little; comparing it over time shows whether things improve.

### 9.5 Misleading numbers

A percentage hides small totals. "50% of clusters failing" may mean one of two. Priya always shows counts alongside percentages.

### 9.6 Storing evidence

Evidence is kept in the configuration repository with read-only history so it cannot be quietly changed.

### Measurement plan

Priya writes a measurement plan stating each measure, how it is collected, how often and by whom. Writing it down before collecting stops her from changing the definition later to make results look better. Kwame reviews the plan and suggests one change: measure the advisory time with a question the team has not seen before, so preparation cannot inflate the result. Priya adds that rule to the plan.

### Evidence quality

Priya rates evidence as strong when it is exported directly from a system, and weaker when it is a manual note. Strong evidence is preferred for audits and comparisons.

### Worked example

Priya records the six-hour advisory search as the first measurement, with date and method. She proposes measuring the same question again after the inventory work, so improvement can be shown with numbers.

> **Synthetic case.** Measures are synthetic.

### Errors and limits

Measuring what is easy rather than what matters creates false comfort.

### Exercises

- **EX025 — Evidence test.** Why is "it is fine" not evidence? *Rubric:* 3 = no record of state, time or source; 2 = partial; 1 = none; 0 = none.
- **EX026 — Three measures.** Name Cobalt's three proposed measures. *Rubric:* 3 = approved images share, baseline failures, advisory time; 2 = two; 1 = one; 0 = none.
- **EX027 — Small totals.** How does Priya avoid misleading percentages? *Rubric:* 3 = shows counts too; 2 = partial; 1 = none; 0 = none.

### Synthesis

Collect timed, sourced evidence and measure trends with counts.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Cloud and container security: orientation

### Learning outcomes

You will (1) map the cloud and container security field; (2) locate Cobalt's problem within it; (3) plan the rest of the course.

### 10.1 The field

Cloud and container security covers configuring cloud services, building and running images, managing identities, protecting data and monitoring. Standards include NIST SP 800-190 for containers, CSA CCM v4 for cloud controls and the CIS Benchmarks for configuration.

### 10.2 Cobalt's problem

The six-hour search showed that Cobalt lacked an inventory of images. Without it, advisories, audits and incidents all start slowly.

### 10.3 Main areas

Priya groups the work into inventory, configuration baselines, identity, data flows, pipeline checks and monitoring.

### 10.4 Kubernetes security docs

The Kubernetes project documents Pod Security Standards, RBAC, network policies and good practices for secrets. These are free and written for operators.

### 10.5 Plan

Over the next chapters Priya will build an inventory, check data flows, apply a baseline, review logs, add pipeline checks and evaluate the result.

### 10.6 Agreement

Kwame and Northgate agree on her placement objectives and confirm she works only on synthetic copies or with supervision.

### Learning resources

Priya builds a reading list: the NIST definitions in SP 800-145, the container guidance in SP 800-190, the CSA CCM v4 control list, the CIS Kubernetes Benchmark and the Kubernetes security documentation. For each she notes which chapters of her placement it supports, so she reads with a purpose rather than trying to absorb everything at once. Kwame adds the shared responsibility pages from the three main providers, because Cobalt's clients use different providers.

### Boundaries of the placement

Priya does not test client systems for weaknesses.

### Worked example

Priya writes a one-page plan linking each area to a deliverable: inventory script, flow list, baseline check, log summary, pipeline rule set, evaluation and handoff pack. Kwame approves it.

> **Synthetic case.** Plan is synthetic.

### Errors and limits

Trying to cover every area at once spreads effort too thin.

### Exercises

- **EX028 — Field sources.** Name three sources for cloud and container security guidance. *Rubric:* 3 = SP 800-190, CCM v4, CIS, Kubernetes docs; 2 = two; 1 = one; 0 = none.
- **EX029 — Root gap.** What gap did the six-hour search reveal? *Rubric:* 3 = no image inventory; 2 = partial; 1 = none; 0 = none.
- **EX030 — Deliverables.** List Priya's planned deliverables. *Rubric:* 3 = inventory, flows, baseline, logs, pipeline, evaluation, handoff; 2 = five; 1 = three; 0 = none.

### Synthesis

Locate a concrete problem in the field before choosing tools.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Cloud and container security: assets and context

### Learning outcomes

You will (1) build an inventory of running workloads and their images; (2) compare it with an approved list; (3) explain why unapproved images matter.

### 11.1 From model to inventory

Using the data model from chapter 4, Priya exports the workloads from the shared client cluster into a synthetic list. Each entry links a workload to the full image reference it runs. This is the asset list that was missing during the advisory search.

### 11.2 Approved images

Cobalt keeps an approved list: images built by its own pipeline, scanned and stored in its private registry. Anything else is unapproved, either pulled straight from a public registry or built outside the pipeline. Shu et al. (2017) found that many public images contained known vulnerabilities, which is why Cobalt prefers its own builds.

### Lab — Lab — image inventory

```python
"""Match running container images to the approved registry list (synthetic, stdlib only)."""
running = {"web-1": "registry.cobalt.example/web:2.4", "web-2": "registry.cobalt.example/web:2.4",
           "api-1": "registry.cobalt.example/api:1.9", "booking": "docker.io/library/node:14",
           "reports": "registry.cobalt.example/reports:0.7", "cron": "docker.io/library/python:3.6",
           "proxy": "registry.cobalt.example/proxy:3.1", "metrics": "registry.cobalt.example/metrics:5.0"}
approved = {"registry.cobalt.example/web:2.4", "registry.cobalt.example/api:1.9",
            "registry.cobalt.example/proxy:3.1", "registry.cobalt.example/metrics:5.0"}
unknown = {w: i for w, i in running.items() if i not in approved}
print(f"workloads {len(running)}, approved {len(running)-len(unknown)}, not approved {len(unknown)}")
for w, i in sorted(unknown.items()):
    print(f"  {w}: {i} ({'public registry' if i.startswith('docker.io') else 'internal, not on list'})")
```

Run with `python3 lab_inventory.py`. Verified output:

```text
workloads 8, approved 5, not approved 3
  booking: docker.io/library/node:14 (public registry)
  cron: docker.io/library/python:3.6 (public registry)
  reports: registry.cobalt.example/reports:0.7 (internal, not on list)
```

### 11.3 Reading the result

Of 8 workloads, 5 run approved images and 3 do not. Two, booking and cron, pull node:14 and python:3.6 directly from a public registry; both are old versions. One, reports, uses an internal image that was never added to the approved list.

### 11.4 Context for each finding

Priya adds context: booking faces the internet and handles appointments, so it matters most; cron sends files to a partner; reports is internal. Context decides the order of fixes.

### 11.5 Owners

Each unapproved image is assigned to the team that deploys it, with a target date.

### Regenerating

Priya schedules the export to run nightly so the inventory always reflects what runs.

### Worked example

The booking team says node:14 "works fine". Priya explains that it no longer receives security updates and that the advisory applies to it. They agree to rebuild on a supported base through the pipeline within two weeks.

> **Synthetic case.** Workloads and images are synthetic.

### Errors and limits

An inventory taken once goes stale; it must be regenerated regularly.

### Exercises

- **EX031 — Lab counts.** How many workloads ran unapproved images, and which? *Rubric:* 3 = 3: booking, cron, reports; 2 = two named; 1 = count only; 0 = none.
- **EX032 — Fix order.** Which unapproved workload should be fixed first and why? *Rubric:* 3 = booking; internet-facing, appointments; 2 = partial; 1 = none; 0 = none.
- **EX033 — Public image risk.** What did Shu et al. (2017) find that supports private builds? *Rubric:* 3 = many public images had known vulnerabilities; 2 = partial; 1 = none; 0 = none.

### Synthesis

An inventory linked to an approved list turns advisories into quick lookups.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Cloud and container security: data flows

### Learning outcomes

You will (1) list data flows for a client system; (2) mark trust boundaries; (3) flag flows needing review.

### 12.1 Why flows matter

Knowing what runs is half the picture; knowing where data goes is the other. Patient contact details move from browser to booking to email service; reports go to a storage bucket; files go to a partner.

### 12.2 Recording flows

Priya records each flow as source, destination, zone and whether it is encrypted. The zone shows whether the flow stays inside the cluster, goes to a managed service or crosses the internet.

### Lab — Lab — data flows

```python
"""List data flows and flag ones that cross a trust boundary without encryption (synthetic)."""
flows = [("browser", "proxy", "internet", True), ("proxy", "web", "cluster", True),
         ("web", "api", "cluster", False), ("api", "database", "managed service", True),
         ("reports", "storage bucket", "managed service", True), ("cron", "partner sftp", "internet", True),
         ("metrics", "monitoring saas", "internet", True), ("booking", "email api", "internet", False)]
cross = [f for f in flows if f[2] != "cluster"]
print(f"flows {len(flows)}, crossing a boundary {len(cross)}")
for s, d, z, enc in flows:
    if z != "cluster" and not enc: print(f"  REVIEW {s} -> {d} ({z}) not encrypted")
    elif z == "cluster" and not enc: print(f"  note {s} -> {d} inside cluster, not encrypted")
```

Run with `python3 lab_flows.py`. Verified output:

```text
flows 8, crossing a boundary 6
  note web -> api inside cluster, not encrypted
  REVIEW booking -> email api (internet) not encrypted
```

### 12.3 Reading the result

Of 8 flows, 6 cross a boundary. One, booking to the email API over the internet, is not encrypted and is flagged for review. One inside the cluster, web to API, is also unencrypted and noted as a known limit.

### 12.4 Following up

Priya checks the booking configuration and finds the email library set to a plain connection. Switching to the encrypted endpoint is a one-line configuration change, tested in staging first.

### 12.5 Data minimisation

She also asks whether the email needs the patient's full details. It needs only a name and time, so the flow is reduced.

### 12.6 Keeping the list current

The flow list is reviewed whenever a new integration is added.

### Partner flows

The cron workload sends files to a partner over SFTP. Priya confirms the partner's address and key are recorded.

### Review

Kwame signs off the flow list.

### Worked example

Kwame asks why the internal flow is acceptable. Priya explains that the cluster network is private, both workloads belong to the same client, and the risk is recorded with a plan to add mutual TLS when the service mesh is introduced.

> **Synthetic case.** Flows are synthetic.

### Errors and limits

A flow list from documentation may miss integrations added quietly; compare with observed traffic where possible.

### Exercises

- **EX034 — Lab flag.** Which flow was flagged for review and why? *Rubric:* 3 = booking to email API; internet, unencrypted; 2 = partial; 1 = none; 0 = none.
- **EX035 — Minimisation.** How was the email flow reduced? *Rubric:* 3 = only name and time sent; 2 = partial; 1 = none; 0 = none.
- **EX036 — Internal limit.** Why was the internal unencrypted flow accepted for now? *Rubric:* 3 = private network, same client, recorded with plan; 2 = two; 1 = one; 0 = none.

### Synthesis

Map where data goes and fix flows that leave unprotected.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Cloud and container security: risk scenarios

### Learning outcomes

You will (1) write plain risk scenarios; (2) rate likelihood and impact; (3) prioritise fixes.

### 13.1 Writing scenarios

A scenario states what could go wrong, how, and what the result would be, without describing attack steps. For example: an outdated booking image contains a known flaw; if exploited, patient contact details could be exposed.

### 13.2 Four scenarios

Priya writes four: outdated public images in booking; the client-b cluster without audit logs, so misuse would go unseen; a leftover admin account; and the unencrypted email flow.

### 13.3 Rating

She rates likelihood and impact as low, medium or high, recording a sentence of reasoning for each.

### 13.4 Prioritising

High impact and medium or high likelihood come first: outdated booking image and missing audit logs. The admin account was already removed; the email flow is fixed.

### 13.5 Residual risk

After fixes, some risk remains; the scenario record notes it.

### 13.6 Sharing

Scenarios are shared with clients in plain language as part of Cobalt's service review.

### Scenario register

Scenarios are stored in a register with an owner, rating, reasoning, linked controls and review date. When a control is added, the register shows which scenarios it addresses. When an incident or advisory occurs, the team checks whether it matches an existing scenario or reveals a new one. This keeps the register alive instead of becoming a document written once and forgotten.

Priya also notes that likelihood ratings change: once the booking image is rebuilt, its scenario's likelihood drops, and the register is updated.

### Worked example

Riverside Dental's practice manager reads the scenarios and asks what "audit logs" means. Priya explains they are records of who did what in the cluster, needed to investigate any problem. The manager agrees to the change window for enabling them.

> **Synthetic case.** Scenarios are synthetic.

### Errors and limits

Ratings are judgements; record the reasons so others can challenge them.

### Exercises

- **EX037 — Scenario parts.** What three parts does a scenario state? *Rubric:* 3 = what, how in general, result; 2 = two; 1 = one; 0 = none.
- **EX038 — Top priorities.** Which two scenarios came first? *Rubric:* 3 = outdated booking image, missing audit logs; 2 = one; 1 = none; 0 = none.
- **EX039 — Client explanation.** How did Priya explain audit logs to the client? *Rubric:* 3 = records of who did what; 2 = partial; 1 = none; 0 = none.

### Synthesis

Plain scenarios with reasons help clients and staff agree on priorities.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Cloud and container security: methods I

### Learning outcomes

You will (1) use benchmarks to define a configuration baseline; (2) select checks suitable for small clusters; (3) document the baseline.

### 14.1 Benchmarks

The CIS Benchmarks give consensus configuration recommendations for platforms including Kubernetes and the main cloud providers. They are long; small teams choose the checks that matter most for their risks.

### 14.2 Choosing checks

Priya picks six checks linked to her scenarios: audit logging on, anonymous access off, a Restricted default for pod security, encryption of secrets at rest, no public API endpoint, and automatic node upgrades.

### 14.3 Why each matters

Audit logging supports investigation; anonymous access off prevents unauthenticated requests; the Restricted default blocks risky pods; secrets encryption protects stored credentials; a private endpoint reduces exposure; auto-upgrades keep nodes patched.

### 14.4 Writing it down

The baseline is a small file with each setting and its expected value, kept in the repository with a short reason for each.

### 14.5 Managed services

Some settings are controlled by the provider in managed Kubernetes; the baseline notes which ones Cobalt sets and which it relies on the provider for, citing the provider's shared responsibility page.

### 14.6 Exceptions

Where a client needs a different value, the exception is recorded with owner and expiry.

### Version control for the baseline

Keeping the baseline in the repository means every change to it is reviewed and recorded. If someone wants to relax a setting, the change appears in review with a reason, and Kwame can approve or question it. The history also shows auditors when the baseline was introduced and how it has evolved.

### Worked example

Kwame asks why Priya did not include all benchmark items. She shows that her six cover the top scenarios and can be checked automatically today; more will be added once these pass.

> **Synthetic case.** Baseline is synthetic.

### Errors and limits

A baseline copied without understanding is followed reluctantly and dropped quickly.

### Exercises

- **EX040 — Six checks.** List Priya's six baseline checks. *Rubric:* 3 = audit, anonymous off, restricted default, secrets encryption, private endpoint, auto-upgrade; 2 = five; 1 = three; 0 = none.
- **EX041 — Selection reason.** Why not include every benchmark item at first? *Rubric:* 3 = focus on top scenarios, automatable now; 2 = partial; 1 = none; 0 = none.
- **EX042 — Provider settings.** How are provider-controlled settings handled? *Rubric:* 3 = noted as relied on, citing shared responsibility; 2 = partial; 1 = none; 0 = none.

### Synthesis

Choose a small, justified baseline and grow it.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Cloud and container security: guided lab

### Learning outcomes

You will (1) run a baseline check against synthetic cluster settings; (2) interpret failures; (3) plan fixes.

### 15.1 Setup

Priya exports settings for three clusters into synthetic records: client-a, client-b and Cobalt's internal cluster. The lab compares each with the baseline.

### Lab — Lab — baseline check

```python
"""Check synthetic cluster settings against a small benchmark-style baseline (stdlib only)."""
baseline = {"audit_logging": True, "anonymous_auth": False, "pod_security_default": "restricted",
            "secrets_encryption": True, "public_endpoint": False, "node_auto_upgrade": True}
clusters = {
 "client-a": {"audit_logging": True, "anonymous_auth": False, "pod_security_default": "restricted",
              "secrets_encryption": True, "public_endpoint": True, "node_auto_upgrade": True},
 "client-b": {"audit_logging": False, "anonymous_auth": False, "pod_security_default": "privileged",
              "secrets_encryption": False, "public_endpoint": True, "node_auto_upgrade": False},
 "internal": {"audit_logging": True, "anonymous_auth": False, "pod_security_default": "baseline",
              "secrets_encryption": True, "public_endpoint": False, "node_auto_upgrade": True}}
for c, s in clusters.items():
    fails = [k for k, v in baseline.items() if s[k] != v]
    print(f"{c}: {len(baseline)-len(fails)}/{len(baseline)} pass; fails: {', '.join(fails) or 'none'}")
```

Run with `python3 lab_baseline.py`. Verified output:

```text
client-a: 5/6 pass; fails: public_endpoint
client-b: 1/6 pass; fails: audit_logging, pod_security_default, secrets_encryption, public_endpoint, node_auto_upgrade
internal: 5/6 pass; fails: pod_security_default
```

### 15.2 Reading the result

Client-a passes 5 of 6, failing only on a public endpoint. Client-b passes 1 of 6: audit logging, pod security default, secrets encryption, public endpoint and node auto-upgrade all fail. The internal cluster passes 5 of 6, with a Baseline rather than Restricted default.

### 15.3 Why client-b differs

Client-b was set up years ago by a contractor and never reviewed. It explains why the old admin account was found there too.

### 15.4 Plan

Client-b gets a planned rebuild; client-a's endpoint is restricted to Cobalt's office addresses; the internal cluster moves to Restricted after checking its workloads.

### 15.5 Total

Seven failures across three clusters form the starting count for later comparison.

### Running safely

The lab reads settings records only; it changes nothing. Running real checks against client clusters also uses read-only access, granted for that purpose. Priya confirms with Kwame that her account has read rights only before running the check against production settings exports.

### What the check cannot see

The baseline check reads settings, so it cannot tell whether workloads inside a cluster behave safely, whether staff passwords are strong or whether the provider's own systems are secure. Priya lists these limits next to the results, so nobody reads a pass as a statement that the cluster is safe overall. She also notes that settings exports are a snapshot: a change made an hour after the export would not appear until the next run, which is one reason to schedule the check daily.

### Worked example

Before changing client-b, Priya checks with the client and schedules a window. She tests the new settings on a copy first. The rebuild passes 6 of 6.

> **Synthetic case.** Settings are synthetic.

### Errors and limits

A passing check confirms settings, not that workloads behave safely.

### Exercises

- **EX043 — Lab totals.** Give each cluster's result. *Rubric:* 3 = a 5/6, b 1/6, internal 5/6; 2 = two; 1 = one; 0 = none.
- **EX044 — Client-b cause.** Why was client-b so far from baseline? *Rubric:* 3 = contractor setup never reviewed; 2 = partial; 1 = none; 0 = none.
- **EX045 — Total failures.** How many failures were counted in total? *Rubric:* 3 = 7; 2 = partial; 1 = none; 0 = none.

### Synthesis

Run the baseline, explain each failure, and fix with care.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Cloud and container security: methods II

### Learning outcomes

You will (1) apply Pod Security Standards; (2) use network policies; (3) handle secrets safely.

### 16.1 Pod Security Standards

Kubernetes defines three profiles: Privileged, Baseline and Restricted. Restricted requires, among other things, running as non-root and dropping extra capabilities. Namespaces are labelled with the level to enforce.

### 16.2 Network policies

By default pods can talk to all other pods. A network policy limits this, for example allowing booking to reach only the API and email service.

### 16.3 Secrets

The Kubernetes good-practice guide for secrets advises encryption at rest, least-privilege access to secrets and avoiding secrets in images or source code.

### 16.4 Starting with warn

Pod Security admission supports warn and audit modes, which report violations without blocking. Priya uses these first.

### 16.5 Fixing workloads

Most failures are fixed by setting a non-root user in the image and adding a security context.

### 16.6 Recording progress

Each namespace's level is tracked in the inventory.

### Namespaces and labels

Labels are applied through the configuration repository, so a forgotten label shows up in review. Priya adds a check that every namespace has an enforce label, which catches new namespaces created without one. This idea comes from a known failure: after Kubernetes removed PodSecurityPolicy in version 1.25, clusters without replacement labels lost enforcement silently.

For network policies, she starts with a default deny for each client namespace and then adds allow rules for the flows on her list, linking the two pieces of work.

### Checking support

Priya confirms the shared cluster's network plugin enforces policies before relying on them.

### Order

Warn, then audit, then enforce, namespace by namespace.

### Worked example

Warn mode on the shared cluster shows that reports runs as root. The team changes its image to use a non-root user, tests, and the namespace moves to enforce Restricted.

> **Synthetic case.** Workloads are synthetic.

### Errors and limits

Network policies only work if the cluster's network plugin supports them; check first.

### Exercises

- **EX046 — Profiles.** Name the three Pod Security Standards profiles. *Rubric:* 3 = privileged, baseline, restricted; 2 = two; 1 = one; 0 = none.
- **EX047 — Default traffic.** What happens between pods without network policies? *Rubric:* 3 = all can talk; 2 = partial; 1 = none; 0 = none.
- **EX048 — Warn first.** Why start Pod Security admission in warn mode? *Rubric:* 3 = see violations without blocking; 2 = partial; 1 = none; 0 = none.

### Synthesis

Apply workload controls gradually, observing before enforcing.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cloud and container security: tooling

### Learning outcomes

You will (1) choose tools for inventory, scanning and checks; (2) prefer simple and reviewable tools; (3) avoid tool sprawl.

### 17.1 Needs first

Priya lists needs: export workloads, scan images for known vulnerabilities, check baselines, check code before merge.

### 17.2 Options

Scanners and checkers exist from providers, open-source projects and vendors. The course labs show the logic with stdlib Python so it is understood before a tool is chosen.

### 17.3 Criteria

Cobalt chooses tools that are maintained, produce readable output, run in the pipeline and do not need wide permissions.

### 17.4 Scanner limits

Image scanners match packages against vulnerability databases; they miss custom code flaws and can report vulnerabilities that are not reachable.

### 17.5 Prioritising findings

Jacobs et al. (2021) describe EPSS, which estimates the likelihood a vulnerability will be exploited. Cobalt uses it alongside severity to order fixes.

### 17.6 Sprawl

Each tool adds maintenance. Priya recommends two tools rather than five.

### Testing a tool

Before adopting the scanner, Priya runs it on three known images: one current, one old and one custom. She checks whether its findings match published advisories and notes false alarms. The test takes an afternoon and gives the team confidence in what the tool reports and where it falls short.

### Output handling

Scanner reports can include internal image names and versions. They are stored in the repository, not shared publicly.

### Writing the decision

The tool decision is written up with needs, options, test results and reasons, so it can be revisited.

### Licences

Priya checks each tool's licence allows commercial use at Cobalt before adoption, with Kwame's help.

### Worked example

A vendor offers a dashboard with hundreds of checks. Priya compares it to needs and finds most checks irrelevant to Cobalt's services; the team stays with a smaller open-source scanner plus their own checks.

> **Synthetic case.** Tool choices are synthetic.

### Errors and limits

A tool's output needs a person who understands it.

### Exercises

- **EX049 — Tool criteria.** What criteria did Cobalt use for tools? *Rubric:* 3 = maintained, readable, pipeline, low permissions; 2 = three; 1 = two; 0 = none.
- **EX050 — Scanner limits.** What do image scanners miss? *Rubric:* 3 = custom code flaws, reachability; 2 = partial; 1 = none; 0 = none.
- **EX051 — EPSS use.** How does EPSS help? *Rubric:* 3 = exploit likelihood to order fixes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Pick few, understood tools that fit real needs.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Cloud and container security: controls

### Learning outcomes

You will (1) describe preventive, detective and corrective controls; (2) map Cobalt's controls; (3) check coverage against a framework.

### 18.1 Control types

Preventive controls stop problems (admission rules); detective controls find them (logs and scans); corrective controls fix them (rebuild and redeploy).

### 18.2 Cobalt's controls

Approved registry, baseline checks, Pod Security admission, network policies, pipeline checks, audit logs and an advisory process.

### 18.3 Framework mapping

Priya maps each to CSA CCM v4 domains, such as identity and access management, and to NIST SP 800-190 recommendations on images and registries.

### 18.4 Gaps

The mapping shows no tested restore of client data, which becomes a new task.

### 18.5 Owners and evidence

Each control has an owner and a source of evidence.

### 18.6 Clients

The control list goes into each client's service description.

### Testing controls

Each control is tested at least once a year: an admission rule is tested by submitting a synthetic non-compliant pod in staging; a log alert by generating a matching synthetic event; the restore by actually restoring. Test results become evidence in the control record, showing not only that a control exists but that it worked recently.

Priya notes that preventive controls are cheapest when they work, but detective and corrective controls are still needed for what prevention misses, such as console changes.

### Control owners

Without owners, controls decay. Each control's owner reviews its evidence quarterly.

### Client copy

Clients receive a short version of the control list, written without internal detail, describing what Cobalt does for them.

### Keeping the map current

When a control changes, its mapping entry and evidence source are updated in the same review.

### Worked example

An auditor for Riverside Dental asks how Cobalt prevents unapproved images. Priya shows the admission rule, the pipeline and the inventory check, each with evidence.

> **Synthetic case.** Mapping is synthetic.

### Errors and limits

Mapping to a framework shows coverage on paper; testing shows it works.

### Exercises

- **EX052 — Control types.** Give one example each of preventive, detective, corrective. *Rubric:* 3 = admission; logs/scans; rebuild; 2 = two; 1 = one; 0 = none.
- **EX053 — Mapping gap.** What gap did mapping reveal? *Rubric:* 3 = no tested restore; 2 = partial; 1 = none; 0 = none.
- **EX054 — Auditor answer.** How did Priya show unapproved images are prevented? *Rubric:* 3 = admission rule, pipeline, inventory with evidence; 2 = two; 1 = one; 0 = none.

### Synthesis

Combine control types, map them and test them.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Cloud and container security: monitoring

### Learning outcomes

You will (1) summarise audit events; (2) identify events needing review; (3) set simple alerts.

### 19.1 Audit logs

Kubernetes audit logs record requests to the API: who, what action, which resource. With client-b now logging, Priya has data to review.

### Lab — Lab — audit summary

```python
"""Summarise synthetic Kubernetes-style audit events and flag ones worth review (stdlib only)."""
import collections
events = [("ci-bot", "create", "deployments"), ("ci-bot", "update", "deployments")] * 20 + \
         [("kwame", "get", "pods")] * 12 + [("priya", "get", "pods")] * 8 + \
         [("ci-bot", "get", "secrets")] * 3 + [("old-admin", "create", "clusterrolebindings"),
          ("old-admin", "get", "secrets"), ("system:anonymous", "get", "pods")]
watch = {"secrets", "clusterrolebindings"}
print(f"events {len(events)}")
for (u, v, r), n in sorted(collections.Counter(events).items()):
    flag = " <- review" if r in watch or u.startswith("system:anon") or u == "old-admin" else ""
    print(f"  {u:17} {v:6} {r:20} {n:3}{flag}")
```

Run with `python3 lab_logs.py`. Verified output:

```text
events 66
  ci-bot            create deployments           20
  ci-bot            get    secrets                3 <- review
  ci-bot            update deployments           20
  kwame             get    pods                  12
  old-admin         create clusterrolebindings    1 <- review
  old-admin         get    secrets                1 <- review
  priya             get    pods                   8
  system:anonymous  get    pods                   1 <- review
```

### 19.2 Reading the result

Of 66 events, most are routine: the CI bot creating and updating deployments, staff reading pods. Four lines need review: the CI bot reading secrets three times, old-admin creating a cluster role binding and reading a secret, and an anonymous request.

### 19.3 Investigating

The CI bot reads a secret it needs for deployment, which is expected but its access can be narrowed. The old-admin events predate removal. The anonymous request came before anonymous access was turned off.

### 19.4 Alerts

Priya proposes alerts for new cluster role bindings, secret reads by people and any anonymous request.

### 19.5 Noise

Alerts that fire constantly are ignored; each must lead to an action.

### Retention

Audit logs are kept for one year in a separate storage account where cluster administrators cannot delete them. Retention lets investigators look back, and separation protects logs from being changed by someone trying to hide activity. Priya checks the storage cost with Kwame: for small clusters, it is a few pounds a month, much less than the value of being able to answer questions after an incident.

She also checks that logs do not contain patient data; audit logs record API requests, not application data, so this is acceptable.

### Review rhythm

Flagged events are reviewed each morning by the on-call engineer, with outcomes noted beside each line.

### Worked example

Kwame asks whether old-admin's events mean misuse. Priya checks the timestamps: they occurred on the former employee's last day, during a handover. Kwame records this with the client and keeps the log extract.

> **Synthetic case.** Events are synthetic.

### Errors and limits

A summary hides detail; investigate flagged lines in full.

### Exercises

- **EX055 — Lab flags.** How many lines were flagged and for what? *Rubric:* 3 = 4: ci-bot secrets, old-admin binding and secret, anonymous; 2 = three; 1 = two; 0 = none.
- **EX056 — Old-admin finding.** What explained the old-admin events? *Rubric:* 3 = last day handover; 2 = partial; 1 = none; 0 = none.
- **EX057 — Alerts.** Which alerts did Priya propose? *Rubric:* 3 = new bindings, people reading secrets, anonymous; 2 = two; 1 = one; 0 = none.

### Synthesis

Summarise logs, investigate flags, and alert only on actionable events.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Cloud and container security: troubleshooting

### Learning outcomes

You will (1) diagnose failures caused by security controls; (2) restore service safely; (3) learn from incidents.

### 20.1 Common breakages

New controls can break workloads: Restricted rejects a pod, a network policy blocks a needed connection, or a narrowed role stops the CI bot.

### 20.2 Method

Priya follows a method: read the error, check recent changes, reproduce in staging, fix the smallest thing, record it.

### 20.3 Example one

After enforcing Restricted, the cron job fails to start because it writes to a root-owned folder. The fix is a writable volume, not relaxing the policy.

### 20.4 Example two

A network policy blocks reports from reaching the storage service. Adding the specific egress rule fixes it.

### 20.5 Rolling back

If a fix takes too long, the change is rolled back and retried later, keeping the client service up.

### 20.6 Learning

Each breakage is added to a short guide for teams.

### A shared guide

The troubleshooting guide lists symptoms, likely causes and fixes, such as "pod rejected: runs as root" and its solution. Teams consult it before asking for help, and Priya updates it whenever a new case appears. After a month, questions to the platform team about security controls drop noticeably, and teams start contributing their own entries.

### Change windows

Enforcement changes are made during agreed windows so clients know when breakage is possible.

### Post-change review

After each enforcement change, the team checks error rates for a day to catch slower failures, such as a nightly job.

### Escalation

If a breakage affects a client's live service for more than fifteen minutes, the on-call engineer escalates to Kwame.

### Worked example

The CI bot fails after its role is narrowed. Priya reads the error: it needs to read one config map. She adds that permission only, rather than restoring cluster-admin.

> **Synthetic case.** Failures are synthetic.

### Errors and limits

Relaxing a control to fix a breakage is tempting; find the specific need.

### Exercises

- **EX058 — Method.** List the troubleshooting steps. *Rubric:* 3 = error, changes, reproduce, smallest fix, record; 2 = four; 1 = two; 0 = none.
- **EX059 — Cron fix.** How was the cron failure fixed? *Rubric:* 3 = writable volume; 2 = partial; 1 = none; 0 = none.
- **EX060 — CI bot.** What did the CI bot actually need? *Rubric:* 3 = read one config map; 2 = partial; 1 = none; 0 = none.

### Synthesis

Fix the specific need instead of weakening the control.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Cloud and container security: service integration

### Learning outcomes

You will (1) connect cluster workloads to managed cloud services securely; (2) use workload identities instead of stored keys; (3) review integrations.

### 21.1 Managed services

Client systems use managed databases, storage buckets and email services. Each connection needs an identity and permissions, and each is a place where data leaves the cluster.

### 21.2 Stored keys

Older Cobalt setups stored long-lived cloud access keys as Kubernetes secrets. If leaked, these keys work from anywhere until someone revokes them.

### 21.3 Workload identity

Major providers let a Kubernetes service account be linked to a cloud identity, issuing short-lived credentials automatically. This removes stored keys and makes access traceable to a workload.

### 21.4 Least privilege for services

The reports workload needs to write to one bucket path, not read every bucket. Priya narrows its policy accordingly.

### 21.5 Storage exposure

Buckets are private by default; any public access must be an approved exception. A weekly check lists bucket access settings across client accounts.

### 21.6 Reviewing integrations

When a new integration is added, the flow list, inventory and permissions are updated together, using a short checklist.

### Integration checklist

Priya's checklist for new integrations asks: what data is sent, which identity is used, what permissions it has, whether traffic is encrypted, and who owns the integration. Each answer is recorded before the integration goes live. The checklist takes ten minutes and prevents the most common mistakes, such as broad storage permissions or a forgotten stored key.

She tests the checklist on two past integrations and finds that one would have been caught: a monitoring service with read access to every bucket.

### Worked example

Priya migrates the reports workload from a stored key to workload identity in staging. After testing, she removes the old key and records the date. A search for other stored keys finds two more, scheduled for migration.

> **Synthetic case.** Integrations are synthetic.

### Errors and limits

Short-lived credentials reduce but do not remove risk; broad permissions are still dangerous.

### Exercises

- **EX061 — Stored key risk.** What is risky about long-lived keys stored as secrets? *Rubric:* 3 = work anywhere until revoked; 2 = partial; 1 = none; 0 = none.
- **EX062 — Workload identity.** What does workload identity provide? *Rubric:* 3 = short-lived credentials linked to service account; 2 = partial; 1 = none; 0 = none.
- **EX063 — Reports access.** How was the reports workload's access narrowed? *Rubric:* 3 = write to one bucket path only; 2 = partial; 1 = none; 0 = none.

### Synthesis

Replace stored keys with workload identities and narrow each integration.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Cloud and container security: automation

### Learning outcomes

You will (1) add security checks to the deployment pipeline; (2) block risky changes before merge; (3) keep checks explainable.

### 22.1 Shift checks earlier

Finding a public bucket after deployment means it was exposed for a time. Checking infrastructure code before merge stops it reaching production.

### 22.2 IaC smells

Rahman et al. (2019) studied infrastructure-as-code scripts and found recurring security smells, such as hard-coded secrets and admin by default. Cobalt's rules target similar patterns.

### Lab — Lab — pipeline checks

```python
"""Flag risky settings in synthetic infrastructure-as-code records before merge (stdlib only)."""
changes = [
 {"id": "PR-41", "bucket_public": False, "image_tag": "2.5", "run_as_root": False, "secret_in_file": False},
 {"id": "PR-42", "bucket_public": True, "image_tag": "2.5", "run_as_root": False, "secret_in_file": False},
 {"id": "PR-43", "bucket_public": False, "image_tag": "latest", "run_as_root": True, "secret_in_file": False},
 {"id": "PR-44", "bucket_public": False, "image_tag": "1.2", "run_as_root": False, "secret_in_file": True},
 {"id": "PR-45", "bucket_public": False, "image_tag": "3.0", "run_as_root": False, "secret_in_file": False}]
rules = {"bucket_public": lambda c: c["bucket_public"], "mutable tag": lambda c: c["image_tag"] == "latest",
         "run_as_root": lambda c: c["run_as_root"], "secret_in_file": lambda c: c["secret_in_file"]}
blocked = 0
for c in changes:
    hits = [n for n, f in rules.items() if f(c)]
    blocked += bool(hits); print(f"{c['id']}: {'BLOCK ' + ', '.join(hits) if hits else 'pass'}")
print(f"{blocked}/{len(changes)} changes blocked")
```

Run with `python3 lab_iac.py`. Verified output:

```text
PR-41: pass
PR-42: BLOCK bucket_public
PR-43: BLOCK mutable tag, run_as_root
PR-44: BLOCK secret_in_file
PR-45: pass
3/5 changes blocked
```

### 22.3 Reading the result

Of 5 proposed changes, 3 are blocked: PR-42 makes a bucket public, PR-43 uses the mutable latest tag and runs as root, and PR-44 puts a secret in a file. PR-41 and PR-45 pass.

### 22.4 Explaining blocks

Each blocked change gets a message stating the rule, why it matters and how to fix it. Developers fix most within the day.

### 22.5 Exceptions

A rare legitimate need, such as a public bucket for website images, uses an approved exception label reviewed by Kwame.

### Measuring the checks

Priya tracks how many changes are blocked each week and how long fixes take. Early on, many changes are blocked; after a month the number falls as developers learn the rules. A rule that blocks often without finding real problems is reviewed, because false blocks make developers resent the checks.

She also confirms that checks run quickly, under a minute, so they do not slow the pipeline.

### Detecting console changes

A nightly comparison of live settings with the repository flags any change made outside the pipeline.

### Worked example

The developer of PR-43 asks why latest is blocked. Priya explains that latest can point to different content over time, so the inventory could not say what is running; pinning a version or digest fixes this.

> **Synthetic case.** Changes are synthetic.

### Errors and limits

Pipeline checks only cover changes made through the pipeline; console changes need detection too.

### Exercises

- **EX064 — Lab blocks.** Which changes were blocked and why? *Rubric:* 3 = 42 public bucket; 43 latest and root; 44 secret; 2 = three; 1 = two; 0 = none.
- **EX065 — Latest tag.** Why is the latest tag blocked? *Rubric:* 3 = content changes; inventory cannot say what runs; 2 = partial; 1 = none; 0 = none.
- **EX066 — Pipeline limit.** Which changes do pipeline checks miss? *Rubric:* 3 = console changes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Block risky changes early with clear explanations and keep detection for the rest.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Cloud and container security: evaluation

### Learning outcomes

You will (1) compare measures before and after improvements; (2) judge whether changes worked; (3) state limits honestly.

### 23.1 What to compare

Priya returns to her measures from chapter 9: unapproved images, baseline failures and time to answer an advisory.

### Lab — Lab — before and after

```python
"""Compare unapproved images and baseline failures before and after the new checks (synthetic)."""
before = {"unapproved_images": 3, "baseline_fails": 7, "hours_to_answer_advisory": 6.0}
after = {"unapproved_images": 1, "baseline_fails": 2, "hours_to_answer_advisory": 0.5}
for k in before:
    b, a = before[k], after[k]
    print(f"{k}: {b} -> {a} ({(b-a)/b*100:.0f}% lower)")
```

Run with `python3 lab_compare.py`. Verified output:

```text
unapproved_images: 3 -> 1 (67% lower)
baseline_fails: 7 -> 2 (71% lower)
hours_to_answer_advisory: 6.0 -> 0.5 (92% lower)
```

### 23.2 Reading the result

Unapproved images fall from 3 to 1 (67% lower), baseline failures from 7 to 2 (71% lower), and the time to answer an advisory from 6 hours to half an hour (92% lower).

### 23.3 Checking the advisory time

To measure fairly, Kwame gives Priya a new synthetic advisory without warning. She answers it from the inventory in about 30 minutes, including checking two edge cases.

### 23.4 Limits

The counts are small and come from one placement period. Other changes, such as staff leaving, also affected results.

### 23.5 Remaining items

One unapproved image (cron, waiting for the partner's new format) and two baseline failures (internal cluster default and client-a endpoint during change window) remain, each with an owner and date.

### Sharing results

The results are shared with Riverside Dental in plain words: we can now tell within half an hour whether a new advisory affects you, and the remaining items have dates. The practice manager says this is the first time a provider has shown them evidence rather than assurances.

Priya also adds a note to the measurement plan to repeat the comparison every quarter, so improvement or slippage is visible over time.

### Honest framing

She avoids claiming the changes made clients safe; she claims measured improvements in specific areas.

### Cost

The checks cost about two staff days to build and run cheaply.

### Worked example

Kwame asks Priya to present the results to the Cobalt team. She shows counts first, then percentages, then limits, and ends with remaining items.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Before-and-after comparisons do not prove cause; describe other changes.

### Exercises

- **EX067 — Lab results.** Give the three before-and-after figures. *Rubric:* 3 = 3→1, 7→2, 6h→0.5h; 2 = two; 1 = one; 0 = none.
- **EX068 — Fair test.** How was the advisory time measured fairly? *Rubric:* 3 = unannounced synthetic advisory; 2 = partial; 1 = none; 0 = none.
- **EX069 — Limits.** What limits did Priya state? *Rubric:* 3 = small counts, one period, other changes; 2 = two; 1 = one; 0 = none.

### Synthesis

Measure again, compare fairly, and state limits.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) ask a focused practical question; (2) collect and analyse data carefully; (3) read relevant research.

### 24.1 A question from practice

Priya asks: how often do Cobalt's clusters drift from baseline between checks? It is answerable with data Cobalt already has.

### 24.2 Method

She runs the baseline check daily for four weeks on synthetic copies of the settings history and counts new failures.

### 24.3 Reading research

Armbrust et al. (2010) describe the cloud computing model and its obstacles, including configuration complexity. Verma et al. (2015) describe Borg, Google's cluster manager, explaining how large clusters are managed by automation, which supports Cobalt's move to automated checks.

### 24.4 Analysis

She counts drift events per cluster and notes causes, such as manual console changes.

### 24.5 Ethics

Data describes systems, not individual performance; names are removed from change records.

### 24.6 Writing up

A two-page report states question, method, results and limits.

### Choosing method

A survey of staff might have shown opinions about drift; daily checks show actual drift. Priya chooses the method that answers her question with the least guesswork. She also considers sample size: three clusters over four weeks gives 84 cluster-days, enough to see patterns but not to compare clusters precisely.

She writes these limitations into the report before showing results, so readers interpret the findings with care.

### Next study

She suggests repeating the study after the nightly comparison is introduced to see if drift falls.

### Sharing findings

Priya presents the study to the team in fifteen minutes, focusing on the recommendation and its evidence.

### Data handling

The settings history copies were stored only in the placement workspace and deleted after the report.

### Worked example

The study finds most drift came from manual changes during urgent fixes. Priya recommends recording urgent fixes in the pipeline afterwards so the baseline catches up.

> **Synthetic case.** Study data is synthetic.

### Errors and limits

Four weeks is short; seasonal work might differ.

### Exercises

- **EX070 — Question.** What practical question did Priya ask? *Rubric:* 3 = how often clusters drift from baseline; 2 = partial; 1 = none; 0 = none.
- **EX071 — Research use.** How does Verma 2015 support Cobalt's direction? *Rubric:* 3 = large clusters managed by automation; 2 = partial; 1 = none; 0 = none.
- **EX072 — Finding.** What caused most drift? *Rubric:* 3 = manual changes during urgent fixes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small focused studies can guide practical decisions.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) work in a team on a shared security improvement; (2) divide work; (3) review each other's output.

### 25.1 The project

Priya joins two other placement students to build a client-ready security summary page generated from the inventory and baseline results.

### 25.2 Dividing work

One builds the data export, one the page, and Priya the checks and wording.

### 25.3 Reviews

Each change is reviewed by another student and Kwame before merge.

### 25.4 Communication

A short daily note lists progress and blockers.

### 25.5 Client voice

They show a draft to Riverside Dental's practice manager, who asks for plain words and fewer numbers.

### 25.6 Result

The final page shows status in three colours with a one-line explanation each.

### Working agreement

At the start, the team agrees on working hours, how to raise problems and how decisions are made. When two members disagree about page colours, they follow the agreement: try both with the client and pick the clearer one. The agreement prevents small disputes from slowing the project.

Kwame reviews progress weekly and helps when a blocker needs someone with more access.

### Accessibility

The page uses text labels as well as colours, so it works for readers who cannot distinguish colours.

### Security of the page

The summary page is only available to logged-in client staff, since it describes the client's systems.

### Retrospective

At the end, the team lists what worked, such as daily notes, and what did not, such as late client feedback. They agree that showing a draft to the client in the first week would have saved rework.

### Final demo

The team demonstrates the page to Kwame and the account managers, who adopt it.

### Worked example

A teammate's draft says "CIS non-compliant". The manager does not understand it. Priya rewrites it as "two settings differ from our standard; fixes are scheduled for next week".

> **Synthetic case.** Project is synthetic.

### Errors and limits

Team projects slow down without clear ownership.

### Exercises

- **EX073 — Roles.** How was the work divided? *Rubric:* 3 = export, page, checks and wording; 2 = two; 1 = one; 0 = none.
- **EX074 — Client feedback.** What did the practice manager ask for? *Rubric:* 3 = plain words, fewer numbers; 2 = partial; 1 = none; 0 = none.
- **EX075 — Rewrite.** How was "CIS non-compliant" rewritten? *Rubric:* 3 = two settings differ; fixes scheduled; 2 = partial; 1 = none; 0 = none.

### Synthesis

Shared work needs owners, reviews and the reader's language.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Cloud and container security: operational handoff

### Learning outcomes

You will (1) prepare work for others to run; (2) write runbooks; (3) identify ownership after placement.

### 26.1 Why handoff

Priya's placement ends in two months. Her checks must keep running without her.

### 26.2 Runbooks

Each check has a runbook: what it does, how to run it, what to do with results, who to contact.

### 26.3 Owners

The platform team owns the checks; client account managers own client communication.

### 26.4 Alert routes

Alerts go to the on-call channel with a link to the runbook.

### 26.5 Known limits

The handoff states what the checks do not cover.

### 26.6 Practice

A colleague runs each check from the runbook alone while Priya watches.

### Knowledge transfer sessions

Priya runs two short sessions for the platform team: one on the inventory and baseline, one on the pipeline rules and alerts. Each session includes a live run of the check and time for questions. She records the questions and adds answers to the runbooks.

The sessions reveal that some staff did not know the checks existed. A short note in the team channel now announces any new check with a link to its runbook.

### Ownership agreement

The platform team lead signs off ownership in writing, so responsibilities are clear after Priya leaves.

### Review date

Each runbook has a review date six months ahead.

### Handoff timeline

The handoff starts six weeks before the placement ends, leaving time to fix gaps found in practice runs. Starting late is a common reason handoffs fail.

### Contacts

The runbooks list Kwame as the escalation contact after Priya leaves, with a backup engineer named for holidays.

### Leaving well

Priya's last week is kept free of new work.

### Worked example

During practice, a colleague cannot find where the baseline file lives. Priya adds the path and a link to the runbook.

> **Synthetic case.** Handoff is synthetic.

### Errors and limits

Handoffs fail when knowledge stays in one person's head.

### Exercises

- **EX076 — Runbook contents.** What does each runbook include? *Rubric:* 3 = what, how, results, contact; 2 = three; 1 = two; 0 = none.
- **EX077 — Owners.** Who owns the checks after placement? *Rubric:* 3 = platform team; 2 = partial; 1 = none; 0 = none.
- **EX078 — Practice gap.** What did practice reveal? *Rubric:* 3 = baseline file path missing; 2 = partial; 1 = none; 0 = none.

### Synthesis

Hand off with runbooks, owners and practice.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) check a handoff pack for completeness; (2) validate controls in production; (3) close gaps.

### 27.1 Handoff checklist

Kwame provides a list of eight required items for any handoff.

### Lab — Lab — handoff check

```python
"""Check a synthetic handoff pack for required items (stdlib only)."""
required = ["runbook", "owner list", "alert routes", "baseline file", "exception register",
            "restore test record", "contact for client", "known limits"]
pack = {"runbook", "owner list", "alert routes", "baseline file", "exception register", "known limits"}
missing = [r for r in required if r not in pack]
print(f"handoff items {len(required)-len(missing)}/{len(required)} present")
for m in missing: print("  missing:", m)
```

Run with `python3 lab_handoff.py`. Verified output:

```text
handoff items 6/8 present
  missing: restore test record
  missing: contact for client
```

### 27.2 Reading the result

Six of eight items are present. Missing: the restore test record and the client contact.

### 27.3 Restore test

Priya and the platform team restore a synthetic copy of Riverside Dental's database in a test account and time it at 40 minutes.

### 27.4 Client contact

The account manager adds the named client contact.

### 27.5 Validation in production

Each check is run in production once with Kwame watching, results compared with staging.

### Why a checklist

Handoffs at Cobalt had previously missed items, such as restore tests. A fixed checklist makes gaps visible and avoids relying on memory. The lab automates the check, but the important part is the list itself, agreed by the team.

After the gaps are closed, the pack is re-checked and passes 8 of 8.

### Restore lessons

The restore test showed one undocumented step: re-creating a database user. It is now in the runbook.

### Validation records

Each production validation is recorded with date, result and who observed it.

### Second look

After closing the gaps, a colleague who had not seen the pack reviews it and confirms it is understandable without Priya. The colleague suggests adding a diagram of where each check runs, which Priya adds.

### Sign-off

Kwame signs off the pack.

### Final state

With all eight items present and production validated, the checks are formally owned by the platform team.

### Archive

The validated pack is archived with its date.

### Worked example

Production validation shows the inventory script misses a workload in a newly added namespace. Priya changes it to read all namespaces, re-runs and confirms the count.

> **Synthetic case.** Pack is synthetic.

### Errors and limits

Staging does not always match production; validate in both.

### Exercises

- **EX079 — Lab gaps.** Which handoff items were missing? *Rubric:* 3 = restore test record, client contact; 2 = one; 1 = none; 0 = none.
- **EX080 — Restore time.** How long did the restore take? *Rubric:* 3 = 40 minutes; 2 = partial; 1 = none; 0 = none.
- **EX081 — Production finding.** What did production validation reveal? *Rubric:* 3 = new namespace missed; 2 = partial; 1 = none; 0 = none.

### Synthesis

Check the pack, validate in production and close gaps.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) respond to a real-style advisory using the new tools; (2) communicate with clients; (3) record the response.

### 28.1 The advisory

A synthetic advisory names a flaw in a common Python base image version.

### 28.2 Response

Priya runs the inventory and finds one internal workload using it, plus none in client clusters.

### 28.3 Prioritising

Using severity and EPSS, she rates it medium and schedules a rebuild within a week.

### 28.4 Communication

Clients receive a short note: assessed, not affected, internal fix scheduled.

### 28.5 Record

The response is recorded with times, decisions and evidence.

### 28.6 Comparison

The response took 25 minutes compared with six hours before.

### Using severity and EPSS

Severity describes how bad a flaw could be; EPSS, described by Jacobs et al. (2021), estimates how likely exploitation is soon. A flaw with high severity but low EPSS score in an internal, non-internet-facing workload can wait a week; the same flaw in an internet-facing booking system would be fixed faster. Priya records both values and her reasoning.

She checks the internal workload's exposure: it has no internet ingress and runs as non-root under Restricted, which supports the medium rating.

### Follow-up

After the rebuild, she re-runs the inventory to confirm the old image is gone and closes the record.

### Lessons recorded

The record notes that the inventory answered the question quickly and that EPSS lookup should be added to the runbook.

### Why it was fast

The speed came from the inventory, runbook and practice, not from heroic effort.

### Client trust

Two clients reply thanking Cobalt for the quick, clear note, and one asks to receive such notes routinely. The account manager adds advisory notes to the service description.

### Worked example

One client asks if they are safe. Priya replies with the note and offers the inventory extract for their workloads.

> **Synthetic case.** Advisory is synthetic.

### Errors and limits

"Not affected" is only as good as the inventory's completeness.

### Exercises

- **EX082 — Inventory result.** What did the inventory show? *Rubric:* 3 = one internal workload; no clients; 2 = partial; 1 = none; 0 = none.
- **EX083 — Client note.** What did the client note say? *Rubric:* 3 = assessed, not affected, fix scheduled; 2 = partial; 1 = none; 0 = none.
- **EX084 — Time.** How long did the response take? *Rubric:* 3 = 25 minutes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Good preparation makes advisories routine.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) combine course work into a capstone; (2) define success criteria; (3) build and test.

### 29.1 Capstone

Priya's capstone is a "client security baseline kit": inventory, baseline, pipeline rules, log alerts, runbooks.

### 29.2 Criteria

Success: runs on all clusters, under one hour to answer an advisory, runbooks tested by another person.

### 29.3 Build

She packages the scripts and documents in one repository folder with a readme.

### 29.4 Testing

A colleague installs the kit for a new synthetic client from the readme alone.

### 29.5 Fixes

Two unclear steps are rewritten.

### 29.6 Safety

The kit reads settings only and changes nothing.

### Repository layout

The kit folder contains scripts, the baseline file, pipeline rule definitions, alert definitions and runbooks, each in its own subfolder with a short readme. A top-level readme explains the order of installation and the access needed. Keeping everything together makes reviews easy and lets Cobalt version the kit as a whole.

Priya also adds a changelog so future changes are traceable.

### Limits of the kit

The kit does not cover application code, client staff accounts or provider control planes. These are listed in the readme.

### Synthetic test client

The test client is built from synthetic data, so no real client systems are touched during the test.

### Maintenance

The platform team agrees to review the kit each quarter and after any Kubernetes version upgrade.

### Peer review

Before the install test, a teammate reviews the scripts for clarity and confirms they only read data.

### Time budget

Priya keeps a log of hours spent, useful for estimating similar kits for other clients.

### Acceptance

Kwame accepts the kit after the install test meets all three success criteria.

### Versioning

The first release is tagged version one.

### Worked example

The colleague's install takes 50 minutes and passes all checks on the new client.

> **Synthetic case.** Kit is synthetic.

### Errors and limits

A kit tested only by its author may hide assumptions.

### Exercises

- **EX085 — Kit parts.** What does the kit contain? *Rubric:* 3 = inventory, baseline, pipeline rules, alerts, runbooks; 2 = four; 1 = two; 0 = none.
- **EX086 — Criteria.** State the success criteria. *Rubric:* 3 = all clusters, <1h advisory, runbooks tested; 2 = two; 1 = one; 0 = none.
- **EX087 — Install test.** What was the install result? *Rubric:* 3 = 50 minutes, all checks passed; 2 = partial; 1 = none; 0 = none.

### Synthesis

Build, test with others and fix assumptions.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) present the capstone; (2) reflect on learning; (3) plan next steps.

### 30.1 Presentation

Priya presents to Northgate and Cobalt: problem, approach, results, limits.

### 30.2 Assessment

Examiners check criteria, evidence and reflection.

### 30.3 Reflection

She notes strengths in inventory and automation, weaker in client communication early on.

### 30.4 Next steps

Cobalt offers her a junior role; she plans to study for a cloud certification.

### 30.5 Lessons

Know what runs, check it often, explain plainly.

### 30.6 Thanks

She credits Kwame and the team.

### Examiner feedback

The examiners praise the clear link between the original problem and the measured result: an advisory that took six hours now takes under half an hour. They note that the kit's limits are stated honestly and that the handoff was tested by others. One suggests that a future version could include cost tracking for the checks, so Cobalt can see their running cost.

Kwame's feedback focuses on habits: Priya reads code before running it, asks before acting on client systems and writes things down.

### Course review

Looking back, the course moved from computing basics through identity, architecture and evidence to inventory, flows, baselines, monitoring, automation, evaluation and handoff. Each step built on the last, and each lab produced evidence used later.

### Continuing learning

Priya plans to follow Kubernetes release notes, especially for removed features, and to revisit the CIS Benchmark when new versions appear.

### Safety reminder

All work in the course used synthetic data or read-only access with supervision. That boundary remains in her new role.

### Final reflection

The placement showed Priya that small, reliable habits matter more than impressive tools.

### Next course

Priya intends to continue studying security for the applications her clients run.

### Worked example

An examiner asks what she would do differently. Priya says she would talk to clients earlier.

> **Synthetic case.** Assessment is synthetic.

### Errors and limits

Reflection is most useful when specific.

### Exercises

- **EX088 — Structure.** What structure did the presentation follow? *Rubric:* 3 = problem, approach, results, limits; 2 = three; 1 = two; 0 = none.
- **EX089 — Weakness.** What weakness did Priya identify? *Rubric:* 3 = early client communication; 2 = partial; 1 = none; 0 = none.
- **EX090 — Lesson.** Summarise the three lessons. *Rubric:* 3 = know what runs, check often, explain plainly; 2 = two; 1 = one; 0 = none.

### Synthesis

Close by reflecting honestly and planning ahead.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Priya Nair, Kwame Asante, Cobalt Hosting, Northgate Polytechnic, Riverside Dental Group and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Which client workloads used the advisory's old Node.js base image.

**EX002.** A program is a file of instructions; a process is a running copy with its own memory and permissions.

**EX003.** A container's disk is often temporary, so data belongs in separate storage such as a database or bucket.

**EX004.** Anyone able to reach that address can talk to the service on that port.

**EX005.** DNS lookup, connection to the proxy on 443, forwarding to the web container.

**EX006.** Web to API inside the cluster; recorded as a known limit.

**EX007.** A dictionary.

**EX008.** So the reader sees the size of the problem before the list.

**EX009.** The script is only as complete as the data it reads.

**EX010.** Client, cluster, workload, image and owner.

**EX011.** The same image written differently; she proposed full references with registry and tag.

**EX012.** By adding a client prefix to identifiers.

**EX013.** Patient details private, appointments correct, site available.

**EX014.** Provider infrastructure, Cobalt's configuration, client data and users.

**EX015.** Public buckets, broad permissions, unpatched images, missing logs.

**EX016.** Containers share the host kernel.

**EX017.** They were built on the same affected base layer.

**EX018.** The exact content that was running.

**EX019.** Authentication confirms identity; authorisation decides permitted actions.

**EX020.** A former employee's old-admin account with cluster-admin; it was removed.

**EX021.** Only rights to manage deployments.

**EX022.** Network rules, TLS, admission rules, least-privilege accounts, logs.

**EX023.** Data passes between areas with different trust levels.

**EX024.** A network policy between booking and reports workloads.

**EX025.** It is not a record of system state with time and source.

**EX026.** Approved-image share, baseline failures per cluster, time to answer an advisory.

**EX027.** She shows counts alongside percentages.

**EX028.** NIST SP 800-190, CSA CCM v4, CIS Benchmarks, Kubernetes documentation.

**EX029.** The lack of an image inventory.

**EX030.** Inventory script, flow list, baseline check, log summary, pipeline rules, evaluation, handoff pack.

**EX031.** Three: booking (node:14), cron (python:3.6) and reports (internal, not listed).

**EX032.** Booking, because it faces the internet and handles appointments.

**EX033.** Many public images contained known vulnerabilities.

**EX034.** Booking to the email API: it crosses the internet unencrypted.

**EX035.** Only name and appointment time are sent.

**EX036.** Private network, same client, and recorded with a plan for mutual TLS.

**EX037.** What could go wrong, how in general terms, and the result.

**EX038.** Outdated booking image and missing audit logs on client-b.

**EX039.** Records of who did what in the cluster.

**EX040.** Audit logging, anonymous auth off, Restricted default, secrets encryption, private endpoint, node auto-upgrade.

**EX041.** The six cover the top scenarios and are checkable now.

**EX042.** Noted as provider-controlled, citing the shared responsibility page.

**EX043.** client-a 5/6, client-b 1/6, internal 5/6.

**EX044.** Set up by a contractor years ago and never reviewed.

**EX045.** Seven.

**EX046.** Privileged, Baseline, Restricted.

**EX047.** All pods can reach each other.

**EX048.** To see violations without blocking deployments.

**EX049.** Maintained, readable output, pipeline-ready, low permissions.

**EX050.** Custom code flaws; they may also flag unreachable issues.

**EX051.** It estimates exploitation likelihood to help order fixes.

**EX052.** Admission rules; logs and scans; rebuild and redeploy.

**EX053.** No tested restore of client data.

**EX054.** Admission rule, pipeline and inventory check with evidence.

**EX055.** Four: CI bot secret reads, old-admin binding and secret read, anonymous request.

**EX056.** A handover on the employee's last day.

**EX057.** New cluster role bindings, secret reads by people, anonymous requests.

**EX058.** Read error, check changes, reproduce in staging, smallest fix, record.

**EX059.** With a writable volume rather than relaxing policy.

**EX060.** Read access to one config map.

**EX061.** If leaked they work from anywhere until revoked.

**EX062.** Short-lived credentials tied to a service account.

**EX063.** To writing one bucket path only.

**EX064.** PR-42 public bucket, PR-43 latest tag and root, PR-44 secret in file.

**EX065.** It can point to different content, so the inventory loses accuracy.

**EX066.** Changes made outside the pipeline, such as in the console.

**EX067.** Unapproved images 3→1, baseline failures 7→2, advisory time 6h→0.5h.

**EX068.** With an unannounced synthetic advisory.

**EX069.** Small counts, one period, and other changes affecting results.

**EX070.** How often clusters drift from baseline between checks.

**EX071.** It shows large clusters are managed through automation.

**EX072.** Manual changes during urgent fixes.

**EX073.** Data export, page, checks and wording.

**EX074.** Plain words and fewer numbers.

**EX075.** Two settings differ from our standard; fixes are scheduled.

**EX076.** What it does, how to run it, what to do with results, who to contact.

**EX077.** The platform team.

**EX078.** The baseline file location was missing.

**EX079.** Restore test record and client contact.

**EX080.** 40 minutes.

**EX081.** The inventory missed a new namespace.

**EX082.** One internal workload; no client workloads.

**EX083.** Assessed, not affected, internal fix scheduled.

**EX084.** 25 minutes.

**EX085.** Inventory, baseline, pipeline rules, log alerts, runbooks.

**EX086.** Runs on all clusters, under one hour per advisory, runbooks tested.

**EX087.** 50 minutes with all checks passing.

**EX088.** Problem, approach, results, limits.

**EX089.** Client communication early on.

**EX090.** Know what runs, check it often, explain plainly.

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
