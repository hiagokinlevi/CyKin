# Cloud and Container Security: Professional Course

- Language: English (`en`); course 036, Professional course (6 months).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working practitioners, such as experienced administrators, moving into cloud and container security roles.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only cloud accounts, clusters and workloads you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Misconfigurations are taught from the defender's side using synthetic configurations, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one experienced administrator from an internal audit about broad cloud roles and unprioritised image vulnerabilities, through foundations, context, authority and methods, to role analysis, triage, verification, case analysis, reporting, quality, a supervised rehearsal and a portfolio. Run each lab where it appears, attempt the five exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Hannah Kowalski** | Practitioner moving into cloud security | Invented |
| **Dev Patel** | Supervisor, head of infrastructure | Invented |
| **Elmstead Council** | Fictional local council | Invented |
| **Kingsbridge Professional Institute** | Fictional training provider | Invented |

### Core sources

NIST [SP 800-145](https://doi.org/10.6028/NIST.SP.800-145), [SP 800-210](https://doi.org/10.6028/NIST.SP.800-210), [SP 800-190](https://doi.org/10.6028/NIST.SP.800-190) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); CSA [Cloud Controls Matrix v4](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); the [AWS](https://aws.amazon.com/compliance/shared-responsibility-model/), [Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) and [Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) shared responsibility pages; Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) frame cloud security for an experienced administrator; (2) apply confidentiality, integrity and availability to a public service; (3) use the shared responsibility model in daily decisions.

### 1.1 The starting point

Hannah Kowalski has run servers for the fictional Elmstead Council for twelve years. The council has moved its parking-permit service to containers on a managed Kubernetes cluster, and Hannah is taking a six-month professional course at the fictional Kingsbridge Professional Institute while moving into a cloud security role. Her supervisor is Dev Patel, the council's head of infrastructure. An internal audit has just reported two concerns about the permit service: cloud roles with far more access than needed, and container images with known vulnerabilities that nobody had prioritised.

### 1.2 What changes in the cloud

Hannah's experience still applies: least privilege, patching, logging and change control. What changes is that infrastructure is configured through APIs, identities are numerous and often belong to automation, and the provider runs part of the stack. NIST SP 800-145 describes the on-demand, self-service nature of cloud, which makes it easy to grant access quickly and hard to notice when it is too much. For the permit service, this means a deploy bot and background jobs hold as many permissions as staff do, and nobody reviews them unless someone asks.

### 1.3 Security goals for permits

Residents' names, addresses and vehicle registrations must stay confidential; permit records must be accurate so enforcement officers act on correct data; and the service must stay available because residents need permits to park legally. Each goal points to a different part of the audit. Excess permissions threaten confidentiality and accuracy, because a compromised workload could read or alter records. Unpatched images threaten all three. Hannah writes the goals at the top of her method note, so every later decision about what to fix first can be checked against them.

### 1.4 Shared responsibility

The provider secures the hardware, the managed control plane and its own services. The council configures identities, network rules, workloads and data protection, as each major provider's shared responsibility page explains. The audit findings fall entirely on the council's side. This matters for how the work is framed: the council cannot wait for the provider to fix its roles or images, and it cannot blame the provider for findings in its own configuration. Hannah notes which parts the provider runs, so her evidence covers only what the council controls and can change.

### 1.5 Working as a professional

Hannah's course expects her to apply methods at work, with evidence, under her organisation's authority, and to stay within agreed scope. At Elmstead this means working under a written brief signed by Dev and the information security officer, keeping evidence for each step, and proposing changes through the council's normal change process rather than making them directly. When something falls outside her brief, she reports it instead of acting on it. Her portfolio for Kingsbridge assessors is built from the same evidence she produces for the council, so the course and the job reinforce each other.

### Worked example

Dev asks Hannah where the audit findings sit in the shared responsibility model. She explains that both roles and images are configured by the council: the provider supplies the identity service and registry, but the council decides who gets which permissions and which images it runs. Dev agrees that this frames the work as the council's own improvement.

> **Synthetic case.** Hannah, Dev, Elmstead Council and Kingsbridge are synthetic.

### Errors and limits

Experienced administrators can over-trust familiar habits; cloud identities and automation need fresh attention.

### Exercises

- **EX001 — Audit concerns.** Name the two audit concerns. *Rubric:* 3 = broad roles; unprioritised vulnerable images; 2 = one; 1 = none; 0 = none.
- **EX002 — What stays the same.** Which of Hannah's existing practices still apply? *Rubric:* 3 = least privilege, patching, logging, change control; 2 = three; 1 = two; 0 = none.
- **EX003 — Permit goals.** Apply the three security goals to permits. *Rubric:* 3 = resident data private, records accurate, service available; 2 = two; 1 = one; 0 = none.
- **EX004 — Responsibility placement.** Where do the audit findings sit in shared responsibility? *Rubric:* 3 = council side; 2 = partial; 1 = none; 0 = none.
- **EX005 — Self-service risk.** Why does self-service make excessive access common? *Rubric:* 3 = easy to grant, hard to notice; 2 = partial; 1 = none; 0 = none.

### Synthesis

Bring existing discipline, but pay fresh attention to identities and automation.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Cloud and container security: service and stakeholder context

### Learning outcomes

You will (1) describe the permit service and its components; (2) identify stakeholders and their concerns; (3) agree priorities.

### 2.1 The service

The permit service has a public web front end (permits-web), a background worker that issues permits (permits-worker), a reporting job used by the parking team, a managed database and a storage bucket for uploaded documents such as proof of address. A deployment bot builds and deploys images. Each part has its own identity, and the audit found excess permissions on several of them. The worker and web front end share the permits-app role, which matters because a weakness in the internet-facing front end would give an attacker the worker's permissions too. Hannah draws a simple diagram of the parts, roles and data flows before collecting evidence.

### 2.2 Stakeholders

Residents want a working, private service. The parking team wants accurate reports. The digital team builds the application. Internal audit wants findings closed with evidence. The data protection officer cares about uploaded documents. Dev cares about stability. Each stakeholder judges the project by a different result, so Hannah writes their interests down at the start. Residents never attend meetings, so she represents their interest through the security goals. The data protection officer reviews anything touching the document bucket, and audit receives evidence in the form it asked for. Dev's concern for stability shapes the decision to change one thing at a time.

### 2.3 Concerns

Developers worry that removing permissions will break deployments. Audit wants dates. The parking team fears losing reports during changes. Each concern is reasonable and points to a safeguard. Developers' fear of breakage leads to testing every permission removal in staging first. Audit's need for dates leads to a timeline with a deadline for each finding. The parking team's worry about reports leads Hannah to schedule changes to the reporting job outside the times when reports are run. She records each concern with the safeguard that answers it, so stakeholders can see that their worries shaped the plan.

### 2.4 Agreeing priorities

Hannah holds a short meeting where each stakeholder states their main concern. They agree: protect resident data first, keep the service available, close audit findings within three months. The order matters when concerns conflict: if a fix risks breaking the service, it is tested and scheduled carefully rather than rushed, but resident data still comes first. Hannah writes the agreed priorities into her method note, so later decisions can refer to them. The three-month target becomes the deadline in the audit plan, and each finding is given an owner and a date.

### 2.5 Communication plan

A fortnightly update goes to all stakeholders, in plain language, showing progress and planned changes. The update lists what changed since the last one, what is planned before the next, and any decisions needed. Writing in plain language matters because the parking team and data protection officer are not cloud specialists. Hannah keeps each update to one page and sends it on the same day each fortnight, so stakeholders know when to expect it. Questions raised in replies are answered in the next update for everyone to see.

### Mapping data

Hannah lists what data each component handles. Permits-web and the worker handle names, addresses and vehicle registrations. The bucket holds uploaded proof-of-address documents, the most sensitive data in the service. Reporting reads aggregated counts for the parking team and needs no personal details. This map tells her which roles and images matter most: anything touching the bucket or the database comes first.

She confirms the map with the data protection officer, who adds that uploaded documents must be deleted after twelve months.

### Worked example

The digital team lead asks whether security changes will slow releases. Hannah proposes that each permission removal is tested in staging with the team, and that she will be available on change days. The lead agrees to a trial.

> **Synthetic case.** Synthetic.

### Errors and limits

Ignoring a stakeholder's concern often turns them into an obstacle later.

### Exercises

- **EX006 — Components.** List the permit service components. *Rubric:* 3 = web, worker, reporting, database, bucket, deploy bot; 2 = five; 1 = three; 0 = none.
- **EX007 — Developer worry.** What do developers worry about? *Rubric:* 3 = removals breaking deployments; 2 = partial; 1 = none; 0 = none.
- **EX008 — Agreed priorities.** What priorities were agreed? *Rubric:* 3 = protect data, availability, close findings in 3 months; 2 = two; 1 = one; 0 = none.
- **EX009 — Update cadence.** How often are stakeholders updated? *Rubric:* 3 = fortnightly; 2 = partial; 1 = none; 0 = none.
- **EX010 — Trial terms.** What did Hannah offer the digital team? *Rubric:* 3 = staging tests together, availability on change days; 2 = partial; 1 = none; 0 = none.

### Synthesis

Understand the service and its people before changing it.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) work within written authority; (2) handle evidence with care; (3) respect resident data.

### 3.1 Authority

Dev and the council's information security officer sign a brief giving Hannah read access to identity and registry settings, read access to cluster configuration, and the right to propose changes through the normal change process. The brief protects both Hannah and the council: she cannot be accused of acting beyond her role, and the council knows exactly what access she holds. Read access is enough to collect evidence, while every change goes through the same approval as any other production change. The brief has a start and end date, and Hannah's access is removed when it ends.

### 3.2 Limits

Hannah does not access resident data, does not test the service for weaknesses, and does not change production without approval. These limits keep the project to configuration review. Testing the service for weaknesses would need a separate authorisation and a different kind of plan, and resident data is not needed to analyse roles or images. The limits are written in the brief, so if anyone asks Hannah to go further, she can point to them and ask Dev for a decision.

### 3.3 Evidence

She exports role definitions, 90 days of permission usage from the provider's access logs, and image scan results. Each export is saved with time, source and her name. Ninety days covers most routine tasks the workloads perform, but may miss rare ones, so unused permissions are only candidates for removal until owners confirm them. If a finding is challenged, Hannah can show where the evidence came from and when. Scan results are exported weekly in the same way, so the permits-web, permits-worker and reporting findings can be compared from one week to the next.

### 3.4 Integrity

Exports are stored in a restricted folder with read-only copies; a short register lists each item. Keeping read-only copies means the original exports cannot be altered, even accidentally, while Hannah works on her own copies. The register records each export's name, date, source, size and where it is stored, so auditors can check that the evidence behind a finding is the evidence collected. Access to the folder is limited to Hannah and Dev. The register itself is part of her portfolio for Kingsbridge.

### 3.5 Privacy

Access logs contain staff names and resident-facing service activity but not resident records. Hannah removes staff names from shared summaries. Staff names are not needed to show that a permission was unused, so they appear only in the original exports, which stay in the restricted folder. Summaries for stakeholders refer to roles and workloads instead. Hannah checks with the data protection officer that this handling is acceptable, and records the answer. The approach also supports the later decision to report findings about systems and processes, not individuals.

### 3.6 Professional duty

If she sees something outside scope that worries her, she reports it to Dev rather than investigating alone. Investigating alone could take her outside her authority and might disturb evidence that someone else needs. Reporting to Dev means the issue is handled by people with the right access and responsibility. When she found the former contractor's role, she reported it the same day and Dev had it removed through the normal process. She records what she found and when she reported it, without investigating further herself.

### Why written authority matters

Written authority protects Hannah, the council and residents. If something breaks or an auditor asks why she viewed certain logs, the brief shows she acted within agreed limits. It also forces a conversation about scope at the start, so nobody is surprised later. The Kingsbridge course treats this as a core professional practice: competence includes knowing what one is allowed to do and keeping records that show it.

### Retention

Evidence is kept for the audit period and then deleted according to the council's retention schedule.

### Worked example

While exporting logs, Hannah notices a role belonging to a former contractor. It is outside her brief to remove it, so she reports it to Dev, who has it removed the same day through the normal process.

> **Synthetic case.** Synthetic.

### Errors and limits

Acting outside authority, even helpfully, can undermine evidence and trust.

### Exercises

- **EX011 — Granted access.** What access does the brief grant? *Rubric:* 3 = read identity, registry, cluster; propose changes; 2 = three; 1 = two; 0 = none.
- **EX012 — Prohibited actions.** Name the three limits. *Rubric:* 3 = no resident data, no testing, no unapproved production change; 2 = two; 1 = one; 0 = none.
- **EX013 — Evidence set.** What evidence did Hannah export? *Rubric:* 3 = roles, 90 days usage, scan results; 2 = two; 1 = one; 0 = none.
- **EX014 — Privacy step.** How is staff privacy protected in summaries? *Rubric:* 3 = names removed; 2 = partial; 1 = none; 0 = none.
- **EX015 — Contractor role.** How was the contractor role handled? *Rubric:* 3 = reported to Dev, removed via process; 2 = partial; 1 = none; 0 = none.

### Synthesis

Work within written authority and handle evidence carefully.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Cloud and container security: core methods

### Learning outcomes

You will (1) apply least privilege analysis; (2) use vulnerability prioritisation; (3) apply workload controls.

### 4.1 Least privilege analysis

Compare what each identity is allowed to do with what it has done over a representative period. Unused permissions are candidates for removal, after checking with owners for rare tasks. At Elmstead the representative period is ninety days of access logs, and the owners are the digital team and Dev. A permission can be unused because it is not needed, or because the task that needs it runs rarely, such as a yearly archive. Checking with owners separates the two, so removing a permission does not break a legitimate task.

### 4.2 Role design

Role-based access control, described by Sandhu et al. (1996), groups permissions into roles. Hannah aims for one role per workload with only needed permissions. At Elmstead, the permits-app role is shared by the web front end and the worker, which gives the internet-facing front end the worker's permissions too. Splitting roles by workload limits what a compromise of one part could reach. Hannah notes this as a later improvement, since the audit concerns unused permissions first. Rarely used permissions, such as those for a yearly archive job, are placed in separate roles that are granted only when needed.

### 4.3 Vulnerability prioritisation

Severity scores describe potential impact; the EPSS model of Jacobs et al. (2021) estimates the likelihood of exploitation activity; exposure describes whether the workload faces the internet. Combining them gives a fair order. Severity alone would put CVE-C in the internal worker ahead of a finding in the internet-facing front end, even though exploitation is much less likely. Combining all three factors gives an order that matches the council's real risk. Hannah writes the method down so that others can apply it the same way, and she records the scores used for each finding with their sources and the date each score was checked.

### 4.4 Workload controls

Kubernetes Pod Security Standards define Baseline and Restricted profiles; enforcing Restricted makes containers run as non-root and with fewer privileges, reducing the impact of a vulnerability. For Elmstead, enforcing Restricted in the permits namespace means that a container running as root or requesting extra privileges is rejected before it starts. A vulnerability in permits-web would then give an attacker less power inside the container. Hannah tests enforcement in staging with a synthetic pod that breaks the rules, so the evidence shows the profile works rather than only that it is configured. The digital team confirms that its workloads run under the profile.

### 4.5 Container guidance

NIST SP 800-190 recommends trusted images, regular rebuilding and limiting container privileges. Hannah's plan applies each recommendation to the permit service. Trusted images come from the council's registry, built by the pipeline from approved base images. Regular rebuilding is what fixes the scanner's findings, since a rebuilt image picks up an updated base. Limiting privileges is achieved through the Restricted profile in the permits namespace. She cites the guidance in her method note, so auditors can see where each practice comes from and judge whether it was applied.

### Choosing the period

Hannah chooses 90 days because it covers monthly reporting cycles and two releases. She checks the calendar for less frequent tasks, such as the yearly permit renewal campaign and archive job, and asks owners directly about them.

She also notes that the method depends on the provider's access logs being complete. She confirms that logging was enabled for the whole period before relying on it.

### Simple first

The method avoids complex scoring; tiers are easy to explain to developers and auditors, and can be refined later if needed.

### Owners

Each role has a named owner who confirms removals.

### Worked example

Hannah writes a one-page method note combining these approaches. Dev asks why not just fix everything at once. She explains that the team has limited time, and an order based on evidence fixes the most important items first.

> **Synthetic case.** Synthetic.

### Errors and limits

90 days may miss yearly tasks; confirm with owners.

### Exercises

- **EX016 — Least privilege method.** Describe the least privilege analysis method. *Rubric:* 3 = compare allowed vs used over a period; confirm with owners; 2 = partial; 1 = none; 0 = none.
- **EX017 — Role aim.** What role design does Hannah aim for? *Rubric:* 3 = one role per workload with needed permissions; 2 = partial; 1 = none; 0 = none.
- **EX018 — Three factors.** Which three factors order vulnerabilities? *Rubric:* 3 = severity, EPSS likelihood, exposure; 2 = two; 1 = one; 0 = none.
- **EX019 — Restricted effect.** How does Restricted reduce impact? *Rubric:* 3 = non-root, fewer privileges; 2 = partial; 1 = none; 0 = none.
- **EX020 — Period limit.** What can a 90-day window miss? *Rubric:* 3 = yearly tasks; 2 = partial; 1 = none; 0 = none.

### Synthesis

Combine usage evidence, likelihood and exposure to decide what to fix.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Cloud and container security: tools and interpretation

### Learning outcomes

You will (1) interpret permission usage data; (2) identify unused permissions; (3) plan safe removals.

### 5.1 The data

Hannah prepares a synthetic summary of three roles: permits-app (used by web and worker), reporting and deploy-bot, with permissions granted and used over 90 days. The synthetic summary mirrors the shape of the real exports without exposing them, so the course lab can be shared with Kingsbridge assessors. Each role lists the permissions it was granted and those that appear in the usage logs. Comparing the two sets for each role shows which permissions were never used during the ninety days.

### Lab — role usage

```python
"""Compare granted and used permissions for synthetic cloud roles over 90 days (stdlib only)."""
roles = {"permits-app": ({"db.read", "db.write", "storage.read", "storage.write", "storage.admin", "queue.send"},
                         {"db.read", "db.write", "storage.read", "queue.send"}),
         "reporting": ({"db.read", "storage.read", "iam.admin"}, {"db.read"}),
         "deploy-bot": ({"cluster.deploy", "registry.push", "registry.delete", "iam.admin"}, {"cluster.deploy", "registry.push"})}
tg = tu = 0
for r, (g, u) in roles.items():
    tg += len(g); tu += len(g & u)
    print(f"{r}: used {len(g & u)}/{len(g)}; unused: {', '.join(sorted(g - u))}")
print(f"overall unused {tg-tu}/{tg} ({(tg-tu)/tg*100:.0f}%)")
```

Run with `python3 lab_roles.py`. Verified output:

```text
permits-app: used 4/6; unused: storage.admin, storage.write
reporting: used 1/3; unused: iam.admin, storage.read
deploy-bot: used 2/4; unused: iam.admin, registry.delete
overall unused 6/13 (46%)
```

### 5.2 Reading the result

Six of thirteen permissions (46%) were unused. Permits-app never used storage.admin or storage.write; reporting never used iam.admin or storage.read; deploy-bot never used iam.admin or registry.delete. The lab counts permissions granted but not used; it does not show whether they are needed for rare tasks. Hannah treats each unused permission as a candidate for removal and lists them by role, ready to check with the owners. The two iam.admin grants stand out, because they belong to roles that have no reason to manage permissions.

### 5.3 Interpreting

The two iam.admin grants are the most dangerous: they allow changing permissions, which could let a compromised workload give itself more access. Storage.admin could change bucket policies. Storage.admin is a concern because the bucket holds residents' proof-of-address documents, so a change to its policy could expose them. Registry.delete could let a compromised deploy bot remove images the service depends on. Hannah ranks the removals by what each permission could do if misused, which puts the iam.admin grants first.

### 5.4 Checking with owners

The digital team confirms storage.write is needed only for a yearly archive job; it is moved to a separate, rarely used role. Registry.delete is used manually by Dev for clean-ups and can be removed from the bot. The reporting team confirms that neither iam.admin nor storage.read is needed, since the job reads only from the database. Checking with owners turns the unused list into decisions each owner has agreed. Hannah records each owner's answer with the date, so audit can see that every removal was confirmed before it happened.

### Removal plan

Removals are scheduled one role at a time, each on a weekday morning with the owning team available. Each change is tested in staging first with the team running their normal tasks. If anything fails, the permission is restored immediately and the failure is analysed before trying again.

Hannah records each removal with the evidence used, the owner's confirmation and the test result.

### Reading the numbers

46% unused is high but common for roles that grew during early development. The aim is not zero for its own sake, but no unused high-risk permissions.

### Sharing

The role summary is shared with each owning team before any change.

### Worked example

The reporting team asks why iam.admin was there. History shows it was added during an early test and never removed. They agree to remove it.

> **Synthetic case.** Synthetic.

### Errors and limits

Usage data shows what happened, not what is needed; confirm with owners.

### Exercises

- **EX021 — Lab total.** What share of permissions was unused? *Rubric:* 3 = 6/13 (46%); 2 = partial; 1 = none; 0 = none.
- **EX022 — Most dangerous.** Which unused permissions were most dangerous and why? *Rubric:* 3 = iam.admin; can change permissions; 2 = partial; 1 = none; 0 = none.
- **EX023 — Yearly job.** How was storage.write handled? *Rubric:* 3 = moved to separate rarely used role; 2 = partial; 1 = none; 0 = none.
- **EX024 — Registry delete.** Why could registry.delete be removed from the bot? *Rubric:* 3 = Dev does clean-ups manually; 2 = partial; 1 = none; 0 = none.
- **EX025 — Origin.** Why was iam.admin on reporting? *Rubric:* 3 = early test, never removed; 2 = partial; 1 = none; 0 = none.

### Synthesis

Read usage data, then confirm with owners before removing.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Cloud and container security: operational workflow

### Learning outcomes

You will (1) prioritise image vulnerabilities; (2) build a repeatable workflow; (3) integrate it with change management.

### 6.1 The findings

The scanner reports six synthetic findings across three images. Hannah orders them with the method from chapter 4. The findings come from the weekly scan of permits-web, permits-worker and reporting images, exported with the date and scanner version. Hannah does not tier them by severity alone. For each finding she adds the likelihood score and whether the workload faces the internet, then applies the agreed method. The method and the inputs are recorded together, so the digital team can check her ordering and apply the same method to future scans without her.

### Lab — vulnerability triage

```python
"""Order synthetic image findings by exposure, EPSS-style likelihood and severity (stdlib only)."""
findings = [("permits-web", "CVE-A", 9.8, 0.62, True), ("permits-web", "CVE-B", 5.3, 0.01, True),
            ("permits-worker", "CVE-C", 9.1, 0.03, False), ("reporting", "CVE-D", 7.5, 0.40, False),
            ("permits-web", "CVE-E", 7.2, 0.002, True), ("reporting", "CVE-F", 4.0, 0.001, False)]
def tier(f):
    _, _, sev, p, internet = f
    if internet and (p >= 0.1 or sev >= 9): return 1
    if p >= 0.1 or sev >= 9: return 2
    return 3
for f in sorted(findings, key=lambda f: (tier(f), -f[3], -f[2])):
    print(f"tier {tier(f)}  {f[0]:15} {f[1]}  severity {f[2]:4}  likelihood {f[3]:.3f}  {'internet' if f[4] else 'internal'}")
```

Run with `python3 lab_triage.py`. Verified output:

```text
tier 1  permits-web     CVE-A  severity  9.8  likelihood 0.620  internet
tier 2  reporting       CVE-D  severity  7.5  likelihood 0.400  internal
tier 2  permits-worker  CVE-C  severity  9.1  likelihood 0.030  internal
tier 3  permits-web     CVE-B  severity  5.3  likelihood 0.010  internet
tier 3  permits-web     CVE-E  severity  7.2  likelihood 0.002  internet
tier 3  reporting       CVE-F  severity  4.0  likelihood 0.001  internal
```

### 6.2 Reading the result

Tier 1: CVE-A in permits-web, severity 9.8, likelihood 0.62, internet-facing. Tier 2: CVE-D in reporting (7.5, 0.40) and CVE-C in permits-worker (9.1 but likelihood 0.03), both internal. Tier 3: three low-likelihood findings. The internet-facing finding with high likelihood comes first, even though CVE-C has a higher severity score. CVE-C is tier 2 because exploitation is unlikely and the worker is internal, but it is still fixed within a month, not ignored. The tier 3 findings wait for the next routine rebuild. Hannah records the inputs for each finding, so the order can be explained to the digital team, as it was when they asked about CVE-C.

### 6.3 Workflow

Tier 1 is fixed within a week, tier 2 within a month, tier 3 in the next routine rebuild. Each fix is a rebuild from an updated base image through the pipeline, then deployment through the change process. Fixing by rebuilding rather than patching running containers keeps images consistent and means the fix is part of the code that builds them. The change process gives Dev and the digital team a chance to review each deployment. Hannah tracks each finding from scan to deployment, so audit can see that tier deadlines were met. A new scan after deployment confirms the finding has gone.

### 6.4 Repetition

The scanner runs weekly; new findings are tiered automatically and appear in the team's queue. Weekly scans catch new vulnerabilities in images already running, not only in new builds. Automatic tiering means each finding arrives in the digital team's queue with its tier and deadline, so nobody has to sort results by hand. This answers one of the process causes Hannah later identifies: scan results had gone to an inbox nobody watched. The digital team reviews the queue in its weekly planning meeting.

### 6.5 Exceptions

If a fix is impossible in time, an exception records the reason and compensating controls. An exception is not a way to ignore a finding. It names the finding, why it cannot be fixed by the deadline, the controls that reduce risk meanwhile, the owner and the new date. Dev approves each exception. The reporting rebuild became the first exception, because an old library did not work with the new base image. Audit receives exceptions with the closed findings, so it can see what remains open and why. Each exception is reviewed when its date arrives, as the reporting rebuild was after the library update two weeks later.

### Why exposure matters

An internet-facing service can be reached by anyone, so a likely-exploited flaw there is urgent. The same flaw in an internal job is reachable only by those already inside the network. Exposure does not make internal findings unimportant, but it orders them sensibly when time is limited.

Hannah documents the tier rule so that developers can predict deadlines themselves.

### Rebuild habits

Images are rebuilt monthly even without findings, so base updates arrive routinely and urgent rebuilds are rarer and less risky.

### Queue

Each finding enters the work queue with tier, deadline, owner and a link to the scan record.

### Review

Tiers are reviewed monthly.

### Worked example

Permits-web is rebuilt within three days. The digital team asks why CVE-C, with severity 9.1, is only tier 2. Hannah explains that it is internal and its likelihood is low, so it waits behind the internet-facing finding, but still within a month.

> **Synthetic case.** Synthetic findings; CVE labels are placeholders.

### Errors and limits

Likelihood scores change; re-check before deferring.

### Exercises

- **EX026 — Tier 1.** Which finding was tier 1 and why? *Rubric:* 3 = CVE-A; internet, high severity and likelihood; 2 = partial; 1 = none; 0 = none.
- **EX027 — Severity 9.1.** Why was CVE-C not tier 1? *Rubric:* 3 = internal, low likelihood; 2 = partial; 1 = none; 0 = none.
- **EX028 — Deadlines.** State the tier deadlines. *Rubric:* 3 = week, month, next routine rebuild; 2 = two; 1 = one; 0 = none.
- **EX029 — Fix route.** How is each fix made? *Rubric:* 3 = rebuild from updated base via pipeline, change process; 2 = partial; 1 = none; 0 = none.
- **EX030 — Re-checking.** Why re-check before deferring? *Rubric:* 3 = likelihood scores change; 2 = partial; 1 = none; 0 = none.

### Synthesis

Tier by exposure and likelihood, then fix through normal change.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Cloud and container security: controls and verification

### Learning outcomes

You will (1) apply role and workload changes; (2) verify each remediation with fresh evidence; (3) report status.

### 7.1 Changes

Hannah's plan has six items: remove storage.admin from permits-app, remove iam.admin and storage.read from reporting, remove iam.admin and registry.delete from deploy-bot, rebuild permits-web, rebuild reporting, and enforce Restricted in the permits namespace. Each item corresponds to a finding and has a named owner and a planned date. The permission removals go first in staging, tested with the digital team, then to production through the change process one at a time, so a problem can be traced to a single change. The rebuilds follow the tier deadlines, and enforcing Restricted comes last, after the workloads have been checked against it.

### 7.2 Verification

Each item is confirmed with fresh evidence: a new role export, a new scan, and the namespace label plus a test deployment of a synthetic non-compliant pod in staging that should be rejected. Fresh evidence shows that the change took effect in production, not only that it was approved. The new role export shows that each removed permission is gone, the new scan shows that rebuilt images no longer carry the finding, and the rejected test pod shows that Restricted is enforced. Hannah saves each piece with its time and source in the evidence register, as she did for the original exports.

### Lab — remediation confirmation

```python
"""Confirm remediation items against fresh synthetic evidence (stdlib only)."""
items = {"remove storage.admin from permits-app": True, "remove iam.admin from reporting": True,
         "remove iam.admin and registry.delete from deploy-bot": True, "rebuild permits-web (CVE-A)": True,
         "rebuild reporting (CVE-D)": False, "enforce Restricted in permits namespace": True}
done = sum(items.values())
print(f"confirmed {done}/{len(items)}")
for k, v in items.items():
    if not v: print("  open:", k)
```

Run with `python3 lab_confirm.py`. Verified output:

```text
confirmed 5/6
  open: rebuild reporting (CVE-D)
```

### 7.3 Reading the result

Five of six items are confirmed. The reporting rebuild is open because the reporting job uses an old library that does not work with the new base image. The open item is reported as open, with its reason, rather than counted as done because the change was planned. Hannah records which items are confirmed and the evidence for each, and lists the reporting rebuild separately with the digital team's explanation. This is the information audit receives, so its picture matches what is actually running.

### 7.4 Handling the open item

The digital team needs two weeks to update the library. Hannah records an exception with compensating controls: reporting runs internally with no internet access and its role is now read-only. The controls reduce risk while the library is updated: without internet access, the vulnerability in the reporting image is harder to reach, and with a read-only role, even a compromised job could not change permissions or records. Dev approves the exception with a review date of two weeks, and it is included in the update to audit.

### 7.5 Reporting

Audit receives the status with evidence for each closed item and the exception for the open one. For each closed item, audit sees the original finding, the change made, the date and the fresh evidence confirming it. The exception shows the reason the reporting rebuild is open, the compensating controls, the owner and the expected date. Hannah presents the status in a short table, so audit can check each finding quickly. She also includes the two process recommendations, since audit asked how the findings arose.

### Test pod

The synthetic non-compliant pod requests to run as root. It is used only in staging and is rejected as expected, proving the admission rule works without harming anything. The test is part of the verification record and repeated after any cluster upgrade, because upgrades have removed security features before, as when PodSecurityPolicy was removed in Kubernetes 1.25.

### Status table

The audit status table lists each item, evidence, date and owner.

### Sign-off

Dev signs off each verified item.

### Archive

Evidence is archived.

### Worked example

Audit asks how Hannah knows Restricted is enforced. She shows the namespace label and the staging rejection of the synthetic test pod, with timestamps.

> **Synthetic case.** Synthetic.

### Errors and limits

A ticket marked done is not verification; check the system itself.

### Exercises

- **EX031 — Lab result.** How many items were confirmed, and which was open? *Rubric:* 3 = 5/6; reporting rebuild; 2 = partial; 1 = none; 0 = none.
- **EX032 — Restricted evidence.** What evidence showed Restricted was enforced? *Rubric:* 3 = label and staging rejection of test pod; 2 = partial; 1 = none; 0 = none.
- **EX033 — Open item cause.** Why was the reporting rebuild delayed? *Rubric:* 3 = old library incompatible; 2 = partial; 1 = none; 0 = none.
- **EX034 — Compensating controls.** What compensating controls applied? *Rubric:* 3 = internal only, no internet, read-only role; 2 = two; 1 = one; 0 = none.
- **EX035 — Done versus verified.** Why is a closed ticket not verification? *Rubric:* 3 = must check the system; 2 = partial; 1 = none; 0 = none.

### Synthesis

Verify each fix with fresh evidence and record honest exceptions.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Cloud and container security: supervised case analysis

### Learning outcomes

You will (1) analyse how the audit findings arose; (2) identify process causes; (3) recommend lasting changes.

### 8.1 How roles grew

Permissions were added during early testing and urgent fixes, with no review afterwards. Nobody owned role hygiene. Hannah traces the history of the permissions she removed. Reporting's iam.admin was added during an early test and never taken away; storage.admin on permits-app was added during an urgent fix. In each case, a permission granted for a short-term need stayed because nobody was responsible for reviewing roles. She finds no evidence that any permission was added carelessly; the problem was the absence of a routine to remove them later.

### 8.2 How vulnerabilities piled up

The scanner existed, but results went to an inbox nobody watched, and there was no rule for what to fix first. The council had invested in scanning but not in what happens after a scan. Without a rule for ordering findings, the long list looked unmanageable, so nothing was fixed systematically. Without an owner, nobody was asked why findings remained. Hannah notes that tiering and a named owner address both gaps, and that the tool itself was never the problem.

### 8.3 Process causes

Missing ownership, missing review cadence and missing prioritisation method. Each cause is a gap in process rather than a technical failure. Nobody owned role hygiene or scan results, so nobody reviewed them. There was no review cadence, so permissions granted for short-term needs stayed indefinitely. There was no prioritisation method, so a long list of findings had no clear starting point. Hannah's recommendations answer each cause directly, so the same problems should not build up again after the project ends. She shows the link in her report to Dev as a short table pairing each cause with the routine and owner that answers it.

### 8.4 Recommendations

Quarterly role reviews owned by the platform team; weekly scan triage owned by the digital team; temporary permissions that expire; findings tracked in the normal work queue. Each recommendation names an owner and a frequency, so it can be checked later. Quarterly role reviews give unused permissions a regular chance to be removed. Weekly triage keeps findings from piling up. Expiring permissions stop short-term grants from becoming permanent. Tracking findings in the normal work queue puts them where developers already plan work, as the digital team later suggested.

### 8.5 Supervision

Dev reviews the analysis and challenges one point: whether expiry for temporary permissions is practical. They agree to pilot it. Dev's concern is that developers might need a permission longer than expected, and that expiry could interrupt their work. Hannah suggests a pilot with a clear process for requesting more time. In the pilot, a developer's temporary storage.write for a migration expired after 48 hours as planned, and nothing lingered. They record the pilot's result and decide to continue using expiry for temporary grants.

### Comparing with guidance

Hannah compares the process causes with CSA CCM v4, which includes controls for regular access reviews and vulnerability management. The council's policies referred to these in general terms, but nobody had turned them into scheduled tasks with owners. Mapping recommendations to CCM v4 controls helps audit see that the changes meet a recognised framework.

She also checks the CIS Benchmark for the council's cloud provider, which recommends reviewing unused credentials and permissions; the quarterly review satisfies this.

### Tracking actions

Each recommendation becomes a tracked action with an owner and due date.

### Follow-up

Dev reviews progress on the actions monthly until all are complete.

### Lesson

Problems grew slowly because nothing prompted anyone to look. Scheduled reviews with owners provide that prompt and make neglect visible.

### Pilot review

After a month, the expiry pilot is reviewed: no grants lingered and no work was delayed.

### Worked example

In the pilot, a developer requests temporary storage.write for a migration. It is granted for 48 hours and expires automatically; the developer finishes in time and nothing lingers.

> **Synthetic case.** Synthetic.

### Errors and limits

Recommendations without owners rarely happen.

### Exercises

- **EX036 — Role growth.** How did roles grow too broad? *Rubric:* 3 = added in testing and fixes, never reviewed; 2 = partial; 1 = none; 0 = none.
- **EX037 — Inbox problem.** Why did vulnerabilities pile up? *Rubric:* 3 = results to unwatched inbox, no priority rule; 2 = two; 1 = one; 0 = none.
- **EX038 — Process causes.** Name the three process causes. *Rubric:* 3 = ownership, review cadence, prioritisation; 2 = two; 1 = one; 0 = none.
- **EX039 — Pilot result.** What happened in the expiry pilot? *Rubric:* 3 = 48h grant expired automatically; 2 = partial; 1 = none; 0 = none.
- **EX040 — Owners.** Who owns role reviews and scan triage? *Rubric:* 3 = platform team; digital team; 2 = partial; 1 = none; 0 = none.

### Synthesis

Fix the process that let problems grow, with named owners.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) report findings clearly to different audiences; (2) handle sensitive information ethically; (3) avoid blame.

### 9.1 Audiences

Councillors want risk and cost in plain words; audit wants evidence; developers want technical detail. Each audience needs different information to make its decisions. Councillors decide on budget and accept risk on behalf of residents, so they need to know what was found, what was fixed and what remains. Audit decides whether findings can be closed, so it needs evidence for each. Developers carry out the changes, so they need exact permissions, images and versions. Hannah plans her reporting around these needs rather than writing one report and hoping it suits all three groups.

### 9.2 One message, three forms

Hannah writes a one-paragraph summary for councillors, an evidence table for audit and a technical note for developers. The three documents carry the same facts at different depths, so they never contradict each other. The summary for councillors states the risk and what was done in plain words. The evidence table for audit lists each finding, change, date and evidence. The technical note gives developers the details of removed permissions and rebuilt images. Hannah checks all three against the same source data before sending them, and Dev reviews them first.

### 9.3 Ethics

Findings describe systems and processes, not individuals. The contractor's leftover role is reported without naming the contractor. Leftover roles and excess permissions came from missing processes, not from individual carelessness. Naming people would not fix the causes, and could discourage staff from reporting problems in future. Hannah describes the contractor's role by its permissions and when it was last used, which is enough for audit to understand the finding. The same approach applies to the staff names in access logs, which are removed from shared summaries.

### 9.4 Honesty

Hannah reports the open reporting rebuild and the limits of 90 days of data rather than presenting a perfect picture. Ninety days of usage may miss rare tasks, so she states that unused permissions were confirmed with owners rather than inferred from logs alone. The open rebuild is reported with its exception and expected date. Hannah notes that presenting a perfect picture would undermine trust if the gap were discovered later. Being clear about limits also helps the council decide whether a longer review period is needed for future role reviews.

### 9.5 Sensitive details

Detailed vulnerability information is shared only with those who need it until fixed. Until a vulnerability is fixed, details such as the affected image, version and exposure could help someone exploit it. Hannah shares this information with the digital team and Dev, who need it to fix the finding. The summary for councillors describes the risk in general terms without technical details. Once a fix is confirmed, the details can be shared more widely, for example with audit as part of the evidence for closing the finding.

### Writing the summary

The councillors' summary has four sentences: what audit found, what has been fixed, what remains and when, and the cost in staff time. It avoids technical terms. Hannah tests it on a colleague from another department, who suggests replacing "permissions" with "access rights", which councillors understand better.

The evidence table for audit lists each finding, action, evidence reference and date. The developer note includes role names, permissions and image versions.

### Timing

Reports go out after fixes for the most serious issues, so sensitive details are not circulated while still exploitable.

### Feedback

Hannah asks each audience whether the report met their needs and adjusts the format for the next one.

### Language

Hannah avoids words like "critical" unless the evidence supports them, so readers trust her ratings.

### Questions

Each report ends with a named contact for questions, so readers know whom to ask and do not guess at meanings.

### Worked example

A councillor asks whether residents' data was at risk. Hannah answers that no evidence shows misuse, the most serious issues are fixed, and one internal item has compensating controls until fixed in two weeks.

> **Synthetic case.** Synthetic.

### Errors and limits

Reassuring without evidence damages trust when problems appear later.

### Exercises

- **EX041 — Audiences.** What does each audience want? *Rubric:* 3 = councillors risk/cost, audit evidence, developers detail; 2 = two; 1 = one; 0 = none.
- **EX042 — Blame.** How was the contractor's role reported? *Rubric:* 3 = without naming; 2 = partial; 1 = none; 0 = none.
- **EX043 — Honest limits.** Which limits did Hannah report? *Rubric:* 3 = open rebuild, 90-day data; 2 = partial; 1 = none; 0 = none.
- **EX044 — Detail sharing.** Who receives detailed vulnerability information? *Rubric:* 3 = need to know until fixed; 2 = partial; 1 = none; 0 = none.
- **EX045 — Councillor answer.** How did Hannah answer the councillor? *Rubric:* 3 = no evidence of misuse, serious fixed, one item controlled; 2 = partial; 1 = none; 0 = none.

### Synthesis

Tailor reports to audiences while staying honest and blameless.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Cloud and container security: quality and troubleshooting

### Learning outcomes

You will (1) check the quality of security work; (2) troubleshoot problems after changes; (3) improve the workflow.

### 10.1 Quality checks

Hannah asks a colleague to repeat her role analysis on one role from raw exports. Their results match. Repeating the analysis from raw exports tests both Hannah's method and her work. If a colleague following the method note reaches the same result, the method can be applied by others. The colleague chose the reporting role and checked which permissions appeared in the usage logs. Hannah records the check, the role chosen and the result in her portfolio. Dev signs the record as reviewer, which gives Kingsbridge assessors independent evidence that the method note is usable by someone else.

### 10.2 Breakage

After removing storage.admin, the worker fails to set an object's metadata. The error shows it needs a narrower metadata permission, which is added. The failure happened in staging, as planned, so the service was not affected. Rather than restoring storage.admin, Hannah and the digital team find the specific permission needed and add only that, keeping the role narrow. The change is recorded and the staging test repeated before production. Hannah adds the failure and its fix to the evidence register, so audit sees the full history of the change.

### 10.3 Root cause

The usage log had recorded the action under a different name; Hannah updates her method to map action names carefully. The worker had been using the metadata action all along, but the log recorded it under a name that did not match the permission, so it looked unused. Hannah adds a mapping step to her method note: for each permission, list the action names that may appear in logs. She also rechecks the other removals with the new mapping and finds no further mismatches. She describes the missed mapping in her Kingsbridge reflection as the main technical lesson of the project.

### 10.4 Workflow improvements

Scan triage now takes 15 minutes weekly; role reviews take an hour quarterly. Fifteen minutes a week is enough because the scanner tiers findings automatically and the digital team only needs to check new tier 1 and 2 findings. An hour a quarter for role reviews works because the core roles are now narrow and the analysis method is written down. Hannah records these times so Dev can plan the work. Keeping both routines short makes it more likely they continue after the project.

### 10.5 Measures

Unused permissions fell from 6 of 13 to 0 in the core roles; tier 1 findings were fixed in three days. Hannah reports these figures with their sources: the new role exports for permissions and the deployment records for the tier 1 fix. She states that the figures cover the three core roles and the three images in scope, not the council's other cloud services. The open reporting rebuild is reported with its exception rather than left out of the figures. Dev checks the figures against the new role exports and scan results before they go to audit.

### Independent review value

The colleague's repetition found no errors in results, but found that one step in Hannah's notes was unclear: how she excluded the yearly archive job. She rewrites the step. Independent repetition tests both results and method description.

After the breakage, Hannah adds a rule to her method: before removing a broad permission, list the specific actions recorded under it and check for narrower equivalents.

### Monitoring after changes

For a week after each change, error rates and failed requests are checked daily to catch slower problems, such as a job that runs weekly.

### Lessons log

Each problem and fix goes into a lessons log shared with the platform team.

### Time saved

Triage time fell from an unplanned afternoon to fifteen minutes, freeing developer time.

### Peer check cadence

A colleague repeats one analysis every quarter to keep the method honest.

### Worked example

The digital team suggests adding the triage output to their sprint board directly. Hannah agrees; findings now appear where developers already work.

> **Synthetic case.** Synthetic.

### Errors and limits

Repeated checks by another person catch errors the author cannot see.

### Exercises

- **EX046 — Quality check.** How was the role analysis quality-checked? *Rubric:* 3 = colleague repeated one role from raw exports; 2 = partial; 1 = none; 0 = none.
- **EX047 — Breakage fix.** What fixed the worker failure? *Rubric:* 3 = narrow metadata permission; 2 = partial; 1 = none; 0 = none.
- **EX048 — Method lesson.** What did the breakage teach? *Rubric:* 3 = map action names carefully; 2 = partial; 1 = none; 0 = none.
- **EX049 — Measures.** Give two improvement measures. *Rubric:* 3 = unused 6/13→0; tier 1 fixed in 3 days; 2 = partial; 1 = none; 0 = none.
- **EX050 — Sprint board.** Why put triage on the sprint board? *Rubric:* 3 = where developers work; 2 = partial; 1 = none; 0 = none.

### Synthesis

Check work independently and improve the workflow from experience.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) rehearse the full workflow on synthetic data; (2) time each step; (3) identify weak points.

### 11.1 Rehearsal

Dev gives Hannah a synthetic new service with two roles and four image findings. She runs the full workflow: usage analysis, triage, plan, staging changes, verification, report. The rehearsal tests whether Hannah can apply the whole method on a service she has not seen, without the help of familiar evidence. The synthetic service runs in a separate staging account, so nothing affects the council's real systems. Dev watches but does not help, noting where she pauses or checks her method note. Each step produces the same kind of evidence as the real project, so the result can go into her portfolio.

### 11.2 Timing

The rehearsal takes three hours: one for analysis, one for staging changes, one for verification and report. Splitting the time by stage shows where the method takes longest. Analysis was quick because the method note gives clear steps. Staging changes took an hour because each removal had to be tested. Verification and report took another hour, mostly spent on workload controls. Hannah records the timings so she can compare them with a second rehearsal and see whether her improvements help.

### 11.3 Weak points

Verification of workload controls took longest because staging lacked a test pod template. Hannah adds one. Without a template, Hannah had to write a non-compliant test pod from scratch to check that Restricted was enforced. Adding a template to staging means future verification only needs the template applied and the rejection recorded. She also writes a short note explaining how to use it. Dev reviews the template to make sure it tests the profile without doing anything harmful, and it is stored with the method note.

### 11.4 Re-run

A second rehearsal on another synthetic service takes two hours. The shorter time shows that the test pod template and familiarity with the method helped. The second service also had different roles and findings, so the speed did not come from repeating the same answers. Hannah records the timings for both rehearsals in her portfolio. Dev notes that a colleague could run the method too, which was later shown when a colleague completed it from her notes. Dev signs off both rehearsal records, which go into her portfolio as evidence that the workflow can be repeated on unfamiliar services.

### 11.5 Safety

The rehearsal used synthetic services in a separate staging account. Using a separate account means a mistake during rehearsal cannot affect the permit service or residents' data. The synthetic services contain no real records, and their roles and images were designed for the exercise. Dev approved the rehearsal account and its access in writing. Hannah deletes the rehearsal services afterwards and records that the account was cleaned up, so nothing is left running. The cleanup is checked by Dev, who confirms the account is empty.

### What the rehearsal tests

The rehearsal tests whether the method works end to end, whether notes are clear enough for others and how long each step takes. Timing helps Dev plan staff time for future services: about two hours for a small service once the method is practised.

The synthetic services include deliberate traps, such as a permission used only once in 90 days, to check that Hannah confirms with owners rather than removing it automatically. She catches it and asks the synthetic owner, as the method requires.

### Recording

Each rehearsal produces the same records as real work, so the portfolio can show them.

### Improvements

After the rehearsals, the method note gains a checklist at the top summarising each step and its evidence.

### Repetition

Dev schedules rehearsals twice a year so skills stay fresh in the team.

### Debrief

Each rehearsal ends with a short debrief on what to improve.

### Outcome

Dev approves the method for use on other services.

### Worked example

Dev asks what would happen if Hannah were away. A colleague runs the rehearsal from her notes in three and a half hours, showing the method is transferable.

> **Synthetic case.** Synthetic.

### Errors and limits

Rehearsals with synthetic data may hide complications of real services.

### Exercises

- **EX051 — Rehearsal steps.** List the rehearsal steps. *Rubric:* 3 = analysis, triage, plan, staging, verify, report; 2 = five; 1 = three; 0 = none.
- **EX052 — Duration.** How long did the rehearsals take? *Rubric:* 3 = 3h then 2h; 2 = partial; 1 = none; 0 = none.
- **EX053 — Weak point.** What slowed verification? *Rubric:* 3 = no test pod template; 2 = partial; 1 = none; 0 = none.
- **EX054 — Transfer.** How was transferability shown? *Rubric:* 3 = colleague ran it in 3.5h; 2 = partial; 1 = none; 0 = none.
- **EX055 — Account.** Where did the rehearsal run? *Rubric:* 3 = separate staging account; 2 = partial; 1 = none; 0 = none.

### Synthesis

Rehearse the workflow and fix its weak points.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a portfolio of evidence; (2) reflect on growth; (3) plan continued practice.

### 12.1 Portfolio

Hannah's portfolio includes her authority brief, method note, role analysis, triage, verification evidence, the exception, reports and rehearsal records. Each item shows a different competence: the brief shows working within authority, the method note shows planning, the analyses show technical skill, the verification evidence shows care, and the reports show communication. Hannah arranges the portfolio in the order of the work, so assessors can follow the project from start to finish. Each item is dated and linked to the evidence register.

### 12.2 Assessment

Kingsbridge assessors check that each item shows applied competence with evidence. Assessors look for evidence that the method was applied at work, not just described. They check that the role analysis matches the exports, that verification used fresh evidence and that the exception was handled properly. They may ask Hannah to explain any item. The assessment criteria are published by Kingsbridge, and Hannah maps each portfolio item to the criteria before submitting it, so assessors can find the evidence for each one.

### 12.3 Reflection

Hannah notes her strength in careful verification and her growth in stakeholder communication. Her careful verification showed in the fresh evidence for every change and in the colleague's repeat of the role analysis. Her growth in communication came from meeting stakeholders, writing three versions of the report and answering councillors' questions. She also notes a mistake she learned from: relying on action names in logs without mapping them to permissions. Writing the reflection helps her plan what to develop next.

### 12.4 Next steps

She plans to extend role reviews to the council's other cloud services. Elmstead runs other services on the same cloud platform, and their roles have probably grown in the same way as the permit service's. Hannah proposes starting with the service that holds the most sensitive data, using the method note and the quarterly review routine. Dev agrees to include the proposal in the platform team's plan for the next year. She also plans to share the method with the digital team so they can run reviews themselves.

### 12.5 Closing the audit

The reporting rebuild closes after two weeks; audit closes both findings. Once the library was updated, the reporting image was rebuilt and scanned again, and the exception was closed. Audit received the final evidence and closed both findings within the three-month target agreed at the start. Hannah records the closure in her portfolio and in the final fortnightly update, so every stakeholder knows the project is complete. Dev thanks the digital team and the parking team for their patience during changes, and the quarterly role review and weekly triage continue as normal work.

### Assessor feedback

The assessors note that Hannah's portfolio links every claim to evidence and that her exception for the reporting rebuild shows honest judgement rather than forcing a closure. They suggest she write a short guide for other councils, anonymised, as a contribution to the profession.

Dev's feedback highlights that the stakeholder meetings prevented resistance and that the digital team now asks Hannah for advice before adding permissions.

### Course review

The course moved from foundations and context, through authority and methods, to tools, workflow, verification, case analysis, communication, quality, rehearsal and portfolio. Each step used evidence from the previous one.

### Continuing practice

Hannah will keep the quarterly role reviews and weekly triage, track Kubernetes release notes for changes to security features, and revisit the CIS Benchmark when new versions appear.

### Boundaries

All work stayed within written authority, using synthetic data for the course labs and read-only access for evidence.

### Thanks

She thanks Dev, the digital team and audit.

### Final note

Hannah begins her new cloud security role with the method, the evidence habits and a team that trusts the process.

### Next

She starts with housing.

### Worked example

An assessor asks which habit mattered most. Hannah says confirming with owners before removing anything.

> **Synthetic case.** Synthetic.

### Errors and limits

A portfolio shows evidence; reflection explains it.

### Exercises

- **EX056 — Portfolio items.** List four portfolio items. *Rubric:* 3 = brief, method, analysis, triage, verification, exception, reports, rehearsal; 2 = four; 1 = two; 0 = none.
- **EX057 — Strength.** What strength did Hannah identify? *Rubric:* 3 = careful verification; 2 = partial; 1 = none; 0 = none.
- **EX058 — Growth.** Where did she grow? *Rubric:* 3 = stakeholder communication; 2 = partial; 1 = none; 0 = none.
- **EX059 — Audit closure.** When did audit close the findings? *Rubric:* 3 = after reporting rebuild; 2 = partial; 1 = none; 0 = none.
- **EX060 — Key habit.** Which habit mattered most? *Rubric:* 3 = confirm with owners before removing; 2 = partial; 1 = none; 0 = none.

### Synthesis

Evidence plus reflection shows professional competence.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Hannah Kowalski, Dev Patel, Elmstead Council, Kingsbridge Professional Institute and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Cloud roles with excessive access and vulnerable images not prioritised.

**EX002.** Least privilege, patching, logging and change control.

**EX003.** Resident data confidential, permit records accurate, service available.

**EX004.** On the council's side: it configures identities and chooses images.

**EX005.** Access is quick to grant and hard to notice when excessive.

**EX006.** permits-web, permits-worker, reporting, database, document bucket, deployment bot.

**EX007.** That removing permissions will break deployments.

**EX008.** Protect resident data, keep service available, close findings within three months.

**EX009.** Fortnightly.

**EX010.** Joint staging tests and her presence on change days.

**EX011.** Read identity, registry and cluster settings, and propose changes.

**EX012.** No resident data access, no weakness testing, no unapproved production changes.

**EX013.** Role definitions, 90 days of usage and image scan results.

**EX014.** Staff names are removed.

**EX015.** Reported to Dev and removed through the normal process.

**EX016.** Compare allowed and used permissions over a period, then confirm with owners.

**EX017.** One role per workload with only needed permissions.

**EX018.** Severity, exploitation likelihood (EPSS) and exposure.

**EX019.** Containers run non-root with fewer privileges.

**EX020.** Tasks that happen less often, such as yearly jobs.

**EX021.** Six of thirteen, 46%.

**EX022.** The iam.admin grants, because they allow changing permissions.

**EX023.** Moved to a separate role for the yearly archive job.

**EX024.** Dev performs clean-ups manually.

**EX025.** Added in an early test and never removed.

**EX026.** CVE-A in permits-web: internet-facing, severity 9.8, likelihood 0.62.

**EX027.** It is internal with low likelihood.

**EX028.** One week, one month, next routine rebuild.

**EX029.** Rebuild from an updated base through the pipeline and change process.

**EX030.** Likelihood scores change over time.

**EX031.** Five of six; the reporting rebuild was open.

**EX032.** The namespace label and a staging rejection of a synthetic non-compliant pod.

**EX033.** An old library did not work with the new base image.

**EX034.** Internal only, no internet access and a read-only role.

**EX035.** Verification requires checking the system itself.

**EX036.** Permissions were added during testing and fixes without later review.

**EX037.** Results went to an unwatched inbox and there was no prioritisation rule.

**EX038.** Missing ownership, review cadence and prioritisation method.

**EX039.** A 48-hour grant expired automatically after the work was done.

**EX040.** Platform team for roles; digital team for scans.

**EX041.** Councillors: risk and cost; audit: evidence; developers: technical detail.

**EX042.** Without naming the contractor.

**EX043.** The open reporting rebuild and the 90-day data limit.

**EX044.** Only those who need it, until fixed.

**EX045.** No evidence of misuse, serious items fixed, one internal item controlled until fixed.

**EX046.** A colleague repeated one role's analysis from raw exports.

**EX047.** Adding a narrow metadata permission.

**EX048.** To map action names carefully in usage logs.

**EX049.** Unused permissions 6/13 to 0; tier 1 fixed in three days.

**EX050.** Findings appear where developers already work.

**EX051.** Usage analysis, triage, plan, staging changes, verification, report.

**EX052.** Three hours, then two hours.

**EX053.** No test pod template in staging.

**EX054.** A colleague ran it from notes in three and a half hours.

**EX055.** A separate staging account.

**EX056.** Authority brief, method note, role analysis, triage, verification evidence, exception, reports, rehearsals.

**EX057.** Careful verification.

**EX058.** Stakeholder communication.

**EX059.** After the reporting rebuild closed two weeks later.

**EX060.** Confirming with owners before removing anything.

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
