# Cloud and Container Security: Master's Course

- Language: English (`en`); course 174, Master's course (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students who must compare competing explanations of cloud security failures with careful observational research.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only cloud accounts, clusters and workloads you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Misconfigurations are taught from the defender's side using synthetic configurations, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one master's student from a hand-made public storage bucket, through question and literature method, an access-control seminar, study design and ethics, competing explanations, proposal and pilot, analysis and writing, to independent review. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lucas Moreau** | Master's student | Invented |
| **Dr Mei Tanaka** | Supervisor | Invented |
| **Ashcombe University** | Fictional university | Invented |
| **Larkspur Retail** | Fictional online retailer | Invented |

### Core sources

NIST [SP 800-145](https://doi.org/10.6028/NIST.SP.800-145), [SP 800-210](https://doi.org/10.6028/NIST.SP.800-210), [SP 800-190](https://doi.org/10.6028/NIST.SP.800-190) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); CSA [Cloud Controls Matrix v4](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); the [AWS](https://aws.amazon.com/compliance/shared-responsibility-model/), [Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) and [Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) shared responsibility pages; Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn an operational problem into a master's research question; (2) search and screen literature systematically; (3) record the search so it can be repeated; (4) define key terms.

### 1.1 The opening case

Lucas Moreau is a master's student at the fictional Ashcombe University, supervised by Dr Mei Tanaka. His employer, the fictional online retailer Larkspur Retail, had a storage bucket of order exports left publicly readable for nine days. The bucket, tmp-export-0412, had been created by hand in the cloud console during a late-night data request. The security team believes manual console changes cause most exposures; the platform team believes infrastructure-as-code (IaC) templates with weak defaults are just as much to blame.

### 1.2 From problem to question

Lucas turns the argument into a question he can answer with Larkspur's change records: "Are configuration changes made through the console more likely to expose storage publicly than changes made through reviewed IaC, and what explains any difference?" The question compares two explanations rather than assuming one.

### 1.3 Search method

He searches two digital libraries and the NIST and CSA publication lists with recorded search strings, dates and result counts. Titles and abstracts are screened against written inclusion criteria: empirical or standards sources on cloud configuration error, IaC security or access control.

### 1.4 Key terms

"Exposure" means a storage resource readable without authentication. "Change origin" is console, IaC pipeline or provider API script. "Reviewed" means a second person approved the change.

### 1.5 Recording

The search log, screening decisions and reasons for exclusion are kept so another student could repeat the search and reach the same set.

### 1.6 Early sources

Mell and Grance (2011) define the service models; the shared responsibility pages of AWS, Microsoft and Google place storage access settings on the customer's side; Rahman et al. (2019) found security smells in IaC scripts, which supports the platform team's concern.

### Worked example

The first search returns 412 records; after screening 31 remain. Lucas notices that he had unconsciously excluded two papers arguing that IaC also spreads errors widely. Dr Tanaka asks him to reinstate them, because a review that only supports one explanation cannot judge between two.

> **Synthetic case.** Larkspur Retail, people and counts are synthetic.

### Errors and limits

Searching only for evidence that supports a favoured explanation is confirmation bias.

### Exercises

- **EX001 — Opening incident.** What happened at Larkspur? *Rubric:* 3 = console-made bucket public 9 days; 2 = partial; 1 = none; 0 = none.
- **EX002 — Two explanations.** What are the competing explanations? *Rubric:* 3 = console changes vs weak IaC defaults; 2 = partial; 1 = none; 0 = none.
- **EX003 — The question.** State Lucas's question. *Rubric:* 3 = console more likely to expose than reviewed IaC, and why; 2 = partial; 1 = none; 0 = none.
- **EX004 — Exposure term.** How is exposure defined? *Rubric:* 3 = readable without authentication; 2 = partial; 1 = none; 0 = none.
- **EX005 — Search record.** What is recorded about the search? *Rubric:* 3 = strings, dates, counts, decisions; 2 = three; 1 = one; 0 = none.
- **EX006 — Reinstated papers.** Why were two papers reinstated? *Rubric:* 3 = avoid confirmation bias; 2 = partial; 1 = none; 0 = none.
- **EX007 — Customer side.** Whose responsibility are storage access settings? *Rubric:* 3 = customer; 2 = partial; 1 = none; 0 = none.

### Synthesis

A fair question compares explanations, supported by a repeatable search.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Cloud and container security: advanced seminar

### Learning outcomes

You will (1) discuss access control, least privilege and configuration in depth; (2) analyse permission use; (3) connect identity to storage exposure; (4) present a seminar argument.

### 2.1 Access control models

Sandhu et al. (1996) formalised role-based access control, where permissions attach to roles rather than individuals. Cloud platforms implement roles and policies at large scale. NIST SP 800-210 gives guidance specific to cloud systems, including managing access across service models.

### 2.2 Least privilege in practice

A role that holds permissions it never uses widens what an error or stolen credential can do. Cloud providers offer access history that shows which permissions were used, which allows evidence-based trimming.

### Lab — Lab — permission use

```python
"""Compare granted and used permissions for synthetic cloud roles over 90 days (stdlib only)."""
roles = {
    "ci-deployer":   ({"storage.write", "storage.read", "compute.deploy", "iam.passRole", "logs.read"}, {"storage.write", "compute.deploy", "iam.passRole"}),
    "analytics-job": ({"storage.read", "storage.write", "db.read", "db.admin"}, {"storage.read", "db.read"}),
    "support-ro":    ({"logs.read", "compute.describe"}, {"logs.read", "compute.describe"}),
}
tg = tu = 0
for r, (granted, used) in roles.items():
    unused = sorted(granted - used)
    tg += len(granted); tu += len(unused)
    print(f"{r:14} granted {len(granted)}, used {len(used)}, unused: {', '.join(unused) or 'none'}")
print(f"unused share {tu}/{tg} = {100*tu/tg:.0f}%")
```

Run with `python3 lab_iam.py`. Verified output:

```text
ci-deployer    granted 5, used 3, unused: logs.read, storage.read
analytics-job  granted 4, used 2, unused: db.admin, storage.write
support-ro     granted 2, used 2, unused: none
unused share 4/11 = 36%
```

### 2.3 Lab result

Over 90 synthetic days, ci-deployer used 3 of 5 granted permissions (unused: logs.read, storage.read), analytics-job used 2 of 4 (unused: db.admin, storage.write) and support-ro used both of its 2. In total 4 of 11 granted permissions, 36%, went unused. The analytics job's unused storage.write matters for Lucas's question: a job that can write storage settings could also change them.

### 2.4 Zero trust

NIST SP 800-207 argues that access should be decided per request using identity and context, not network location. For storage, that means private by default, with access granted to named identities.

### 2.5 Seminar argument

Lucas argues that exposure is partly an identity problem: if few identities can change bucket access settings, fewer paths to exposure exist, regardless of console or IaC.

### Access history quality

Access history can omit some actions, so Lucas checks the provider documentation for gaps before relying on it.

### Worked example

Seminar peers challenge him: unused permissions over 90 days may still be needed for rare tasks such as quarterly reports. Lucas agrees to treat unused permissions as candidates for review with the owner, not automatic removal, and adds this nuance to his framework.

> **Synthetic case.** Roles and usage are synthetic.

### Errors and limits

Absence of use in a window is not proof a permission is unneeded.

### Exercises

- **EX008 — RBAC idea.** What is the core RBAC idea? *Rubric:* 3 = permissions attach to roles; 2 = partial; 1 = none; 0 = none.
- **EX009 — Lab share.** What share of permissions went unused? *Rubric:* 3 = 4/11, 36%; 2 = partial; 1 = none; 0 = none.
- **EX010 — analytics-job.** Which permissions did analytics-job not use? *Rubric:* 3 = db.admin, storage.write; 2 = partial; 1 = none; 0 = none.
- **EX011 — Why storage.write.** Why does analytics-job's unused storage.write matter? *Rubric:* 3 = could change bucket settings; 2 = partial; 1 = none; 0 = none.
- **EX012 — ZTA for storage.** What does zero trust mean for storage? *Rubric:* 3 = private by default, named identities; 2 = partial; 1 = none; 0 = none.
- **EX013 — Peer challenge.** What did peers challenge? *Rubric:* 3 = rare tasks need unused permissions; 2 = partial; 1 = none; 0 = none.
- **EX014 — Response.** How did Lucas respond? *Rubric:* 3 = review with owner, not auto-remove; 2 = partial; 1 = none; 0 = none.

### Synthesis

Identity and least privilege shape how exposures can happen.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) design an observational study of change records; (2) address confounding; (3) obtain ethics approval and data agreements; (4) plan reproducible analysis.

### 3.1 Design

The study uses one year of Larkspur's change records for storage resources. Each change has an origin (console or IaC), a time, a resource and whether it produced public exposure. An observational design is appropriate because Larkspur cannot randomly assign how teams make changes.

### 3.2 Confounding

Console changes may happen more often under time pressure, in data-science teams or at night. Lucas records team, hour and resource type so he can check whether the difference holds within these groups.

### 3.3 Ethics

Change records name engineers. The ethics application commits to pseudonymising engineer identities before analysis, reporting only by team and origin, and never using the study to assess individuals. Larkspur's data protection officer signs the data agreement.

### 3.4 Reproducibility

Analysis scripts are written before the full data arrive, tested on synthetic records with the same structure and kept under version control. The synthetic generator is released with the thesis.

### 3.5 Pre-registration

Lucas writes his hypotheses, primary comparison and planned subgroup checks in a dated document shared with Dr Tanaka before receiving the data.

### 3.6 Measures of association

The primary result is the proportion of changes causing exposure by origin, the risk ratio, and a chi-square test; subgroup results follow.

### Data management plan

The data management plan states where pseudonymised records are stored (a university-approved encrypted store), who can access them (Lucas and Dr Tanaka), how long they are kept (until the degree is awarded plus one year) and how they are deleted. Larkspur keeps the key linking pseudonyms to engineers and never shares it.

### Worked example

The ethics board asks how Lucas will avoid identifying an engineer in a small team. He agrees to merge teams with fewer than five engineers into an "other" group in all reports.

> **Synthetic case.** Records and approvals are synthetic.

### Errors and limits

Observational data show association; explanations need careful argument and subgroup checks.

### Exercises

- **EX015 — Why observational.** Why is the design observational? *Rubric:* 3 = cannot randomise change methods; 2 = partial; 1 = none; 0 = none.
- **EX016 — Confounders.** Name three possible confounders. *Rubric:* 3 = time pressure, team, hour, resource type; 2 = two; 1 = one; 0 = none.
- **EX017 — Pseudonymising.** What happens to engineer identities? *Rubric:* 3 = pseudonymised; team-level reports; 2 = partial; 1 = none; 0 = none.
- **EX018 — Pre-registration.** What was pre-registered? *Rubric:* 3 = hypotheses, primary comparison, subgroups; 2 = two; 1 = one; 0 = none.
- **EX019 — Primary result.** What is the primary result measure? *Rubric:* 3 = proportion exposing by origin, risk ratio, chi-square; 2 = two; 1 = one; 0 = none.
- **EX020 — Small teams.** How are small teams protected? *Rubric:* 3 = merge under 5 into other; 2 = partial; 1 = none; 0 = none.

### Synthesis

Design for confounders, protect people and fix the analysis in advance.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Cloud and container security: competing explanations

### Learning outcomes

You will (1) state each explanation as a testable mechanism; (2) derive predictions that differ; (3) identify evidence that would distinguish them; (4) avoid unfalsifiable explanations.

### 4.1 Explanation A: console error

Manual console changes skip review and templates, so mistakes such as ticking "public" are more likely and stay unnoticed. Prediction: higher exposure rate for console changes, persisting within teams and hours.

### 4.2 Explanation B: weak IaC defaults

Templates copied between projects carry permissive settings, and review focuses on application logic, not storage policy. Prediction: IaC exposures cluster in resources created from a small number of templates; fixing templates would cut many exposures at once.

### 4.3 Explanation C: identity breadth

Exposure depends on how many identities can change access settings, whatever the origin. Prediction: exposures concentrate where many identities hold storage administration rights.

### 4.4 Distinguishing evidence

A and B can both be true. The study measures rates by origin, clustering by template and the number of identities with storage admin rights per account.

### 4.5 Avoiding unfalsifiable claims

"Human error" alone explains everything and predicts nothing; each explanation must say what pattern would contradict it.

### 4.6 Literature link

Rahman et al. (2019) supports B's mechanism; provider guidance on blocking public access at account level addresses all three.

### Writing the table

Each row of Lucas's table lists the explanation, its mechanism, its prediction, the evidence that would contradict it and the data field that measures it. Writing the contradicting evidence is the hardest column and the most useful: it forces each explanation to risk being wrong. The table becomes the first figure of the thesis.

### Worked example

Lucas tables the three explanations with their predictions and contradicting patterns. Dr Tanaka points out that C could make A look stronger if console users also hold broad rights; Lucas adds identity breadth as a control variable.

> **Synthetic case.** Explanations are framed for the synthetic case.

### Errors and limits

Supporting one explanation does not rule out others; look for the pattern that would contradict each.

### Exercises

- **EX021 — Explanation A.** State explanation A's prediction. *Rubric:* 3 = higher console rate within teams and hours; 2 = partial; 1 = none; 0 = none.
- **EX022 — Explanation B.** What does explanation B predict? *Rubric:* 3 = clustering by template; 2 = partial; 1 = none; 0 = none.
- **EX023 — Explanation C.** What does C predict? *Rubric:* 3 = exposures where many identities have admin rights; 2 = partial; 1 = none; 0 = none.
- **EX024 — Human error.** Why is "human error" alone weak? *Rubric:* 3 = predicts nothing; 2 = partial; 1 = none; 0 = none.
- **EX025 — Control variable.** What control variable was added? *Rubric:* 3 = identity breadth; 2 = partial; 1 = none; 0 = none.
- **EX026 — Both true.** Can A and B both be true? *Rubric:* 3 = yes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Turn explanations into predictions that evidence could contradict.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write the research proposal; (2) pilot the data extraction on a small sample; (3) check measures work; (4) revise before the main collection.

### 5.1 The proposal

Twelve pages: background, question, explanations and predictions, design, data, ethics, analysis, risks and timeline. Each prediction maps to an analysis.

### 5.2 Pilot extraction

Lucas extracts one month of synthetic-format records from a test account and classifies current bucket settings to check that the classification works.

### Lab — Lab — bucket classification

```python
"""Classify synthetic storage bucket settings against a simple baseline (stdlib only)."""
buckets = [  # name, public, encrypted, access_logging, origin
    ("orders-archive", False, True, True, "iac"), ("marketing-assets", True, True, False, "console"),
    ("tmp-export-0412", True, False, False, "console"), ("ml-features", False, True, False, "iac"),
    ("receipts", False, True, True, "iac"), ("partner-drop", True, True, True, "iac"),
]
for n, pub, enc, log, origin in buckets:
    issues = [x for x, bad in (("public", pub), ("unencrypted", not enc), ("no access logs", not log)) if bad]
    print(f"{n:17} {origin:8} {', '.join(issues) or 'ok'}")
print("public buckets:", sum(b[1] for b in buckets), "of", len(buckets))
```

Run with `python3 lab_buckets.py`. Verified output:

```text
orders-archive    iac      ok
marketing-assets  console  public, no access logs
tmp-export-0412   console  public, unencrypted, no access logs
ml-features       iac      no access logs
receipts          iac      ok
partner-drop      iac      public
public buckets: 3 of 6
```

### 5.3 Lab result

Of six synthetic buckets, three are public: marketing-assets (console; also no access logs), tmp-export-0412 (console; also unencrypted and no access logs) and partner-drop (IaC; public by design for a partner). orders-archive and receipts are ok; ml-features lacks access logs. The pilot shows that "public" needs a field for intended public access: partner-drop's exposure was approved.

### 5.4 Revising measures

Exposure is now "unintended public access", with intended public resources recorded in an approved register. This change is made before the main data are seen and is noted in the pre-registration log.

### 5.5 CIS and CCM

The baseline checks align with CIS Benchmark recommendations for storage and with CSA CCM v4 control domains for data security, which helps relate findings to frameworks Larkspur already uses.

### Proposal feedback

The proposal reviewers ask for a power estimate. Using the pilot's rough rates, Lucas estimates that a year of records gives enough changes to detect a difference of about three percentage points between origins, and states that smaller differences may be missed.

### Worked example

The pilot also shows that console changes made through a provider's mobile app are logged with a different origin label. Lucas maps both to "console" and records the rule.

> **Synthetic case.** Buckets and labels are synthetic.

### Errors and limits

Changing measures after seeing main data is a source of bias; change them only after pilots, and log why.

### Exercises

- **EX027 — Lab public.** Which buckets were public? *Rubric:* 3 = marketing-assets, tmp-export-0412, partner-drop; 2 = two; 1 = one; 0 = none.
- **EX028 — tmp-export.** What issues did tmp-export-0412 have? *Rubric:* 3 = public, unencrypted, no logs; 2 = two; 1 = one; 0 = none.
- **EX029 — Revised measure.** How was exposure redefined? *Rubric:* 3 = unintended public access; 2 = partial; 1 = none; 0 = none.
- **EX030 — Mobile app.** What labelling issue was found? *Rubric:* 3 = mobile app console origin label; 2 = partial; 1 = none; 0 = none.
- **EX031 — Framework links.** Which frameworks do checks align with? *Rubric:* 3 = CIS Benchmarks, CSA CCM v4; 2 = partial; 1 = none; 0 = none.
- **EX032 — When to change measures.** When may measures change? *Rubric:* 3 = after pilots, before main data, logged; 2 = partial; 1 = none; 0 = none.

### Synthesis

Pilots refine measures before they can bias results.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) collect the full dataset under the agreed rules; (2) run the pre-registered analysis; (3) test subgroup patterns for each explanation; (4) interpret with care.

### 6.1 Collection

Larkspur exports one year of storage change records, pseudonymised, with origin, team group, hour, resource and template identifier. Lucas checks counts against Larkspur's monthly totals before analysis.

### Lab — Lab — exposure by origin

```python
"""Exposure events by change origin: rates and a chi-square test of independence (stdlib only)."""
import math
table = {"iac": (12, 1188), "console": (27, 573)}  # (exposing changes, other changes)
for k, (e, o) in table.items():
    print(f"{k:8} {e}/{e+o} changes exposing = {100*e/(e+o):.1f}%")
rows = list(table.values()); N = sum(sum(r) for r in rows)
cols = [sum(r[i] for r in rows) for i in (0, 1)]
chi = sum((rows[i][j] - sum(rows[i]) * cols[j] / N) ** 2 / (sum(rows[i]) * cols[j] / N) for i in (0, 1) for j in (0, 1))
p = math.erfc(math.sqrt(chi / 2))  # 1 degree of freedom
rr = (27/600) / (12/1200)
print(f"chi-square {chi:.1f} (df 1), p {p:.2g}; risk ratio console/iac {rr:.1f}")
```

Run with `python3 lab_origin.py`. Verified output:

```text
iac      12/1200 changes exposing = 1.0%
console  27/600 changes exposing = 4.5%
chi-square 23.1 (df 1), p 1.5e-06; risk ratio console/iac 4.5
```

### 6.2 Primary result

In the synthetic dataset, 12 of 1,200 IaC changes (1.0%) and 27 of 600 console changes (4.5%) caused unintended public exposure. The chi-square statistic is 23.1 with one degree of freedom, p about 1.5 × 10⁻⁶, and the risk ratio is 4.5: console changes were four and a half times as likely to expose storage.

### 6.3 Subgroups for A

The difference holds within daytime and night-time changes and within the three largest team groups, which supports explanation A beyond timing or team effects.

### 6.4 Clustering for B

Nine of the twelve IaC exposures come from two templates, supporting explanation B: weak defaults spread. Fixing those templates would address most IaC exposures.

### 6.5 Identity for C

Accounts where more than ten identities hold storage administration rights have higher exposure rates for both origins, supporting C as a contributing factor.

### Checking the data

Before analysis, Lucas checks for duplicate records, missing origins and impossible timestamps. He finds 14 records with no origin, all from an automation account; after checking with Larkspur, they are classed as IaC pipeline changes and the rule is logged. A sensitivity analysis excluding them gives the same conclusion.

### Worked example

Lucas's conclusion is that all three explanations contribute, with different remedies: guardrails for console changes, template fixes for IaC and fewer storage administrators. Dr Tanaka praises the result for replacing an argument between teams with evidence that both were partly right.

> **Synthetic case.** All counts are synthetic.

### Errors and limits

A small p-value shows the difference is unlikely by chance, not that it is large or causal.

### Exercises

- **EX033 — Rates.** What were the exposure rates? *Rubric:* 3 = IaC 1.0%, console 4.5%; 2 = partial; 1 = none; 0 = none.
- **EX034 — Statistics.** What were the chi-square and risk ratio? *Rubric:* 3 = 23.1, RR 4.5; 2 = partial; 1 = none; 0 = none.
- **EX035 — Template clustering.** How many IaC exposures came from two templates? *Rubric:* 3 = 9 of 12; 2 = partial; 1 = none; 0 = none.
- **EX036 — Identity finding.** What did identity breadth show? *Rubric:* 3 = >10 admins higher rates both origins; 2 = partial; 1 = none; 0 = none.
- **EX037 — Remedies.** Match each explanation to a remedy. *Rubric:* 3 = guardrails, template fixes, fewer admins; 2 = two; 1 = one; 0 = none.
- **EX038 — p-value meaning.** What does the small p-value show? *Rubric:* 3 = unlikely by chance, not size or cause; 2 = partial; 1 = none; 0 = none.

### Synthesis

Test each explanation's prediction and match remedies to causes.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) write the dissertation clearly; (2) present limitations honestly; (3) separate findings from recommendations; (4) prepare figures and appendices.

### 7.1 Structure

Introduction and question; literature review with the search method; design and ethics; results by explanation; discussion; limitations; recommendations; appendices with search log, analysis scripts and the synthetic generator.

### 7.2 Limitations

One organisation and one year; origin labels depend on logging accuracy; intended public resources depend on a register that may be incomplete; the study measures exposure, not whether data were accessed.

### 7.3 Findings versus recommendations

Findings say what the data show; recommendations say what Larkspur might do, labelled as Lucas's judgement. Mixing them would overstate the evidence.

### 7.4 Recommendations

Block public access at account level by default with approved exceptions, as provider guidance suggests; fix the two templates and add policy checks to IaC review; reduce storage administrators; route urgent data requests through a pre-approved, private export process.

### 7.5 Figures

One figure per explanation shows its prediction against the data, using the same scale.

### 7.6 Writing clearly

Short paragraphs, defined terms and one claim per paragraph.

### Appendices

The appendices let readers check everything without cluttering the main text. They contain the full search log with screening decisions, the pre-registration and its dated amendments, the analysis scripts with a short guide to rerunning them, the synthetic data generator and a table mapping each recommendation to the finding that supports it. Dr Tanaka asks Lucas to test the guide by having a classmate follow it; the classmate reproduces every figure on the first attempt.

### Word limits

Lucas keeps within the word limit by moving detail to appendices.

### Worked example

In draft review, Dr Tanaka marks a sentence claiming the recommendations "will prevent exposures". Lucas changes it to "are expected to reduce exposures, which Larkspur could test by repeating the measurement after a year".

> **Synthetic case.** Text and outcomes are synthetic.

### Errors and limits

Recommendations framed as findings mislead readers about certainty.

### Exercises

- **EX039 — Limitations.** Name three limitations. *Rubric:* 3 = one org/year, logging accuracy, register, no access data; 2 = two; 1 = one; 0 = none.
- **EX040 — Findings vs recommendations.** How do findings differ from recommendations? *Rubric:* 3 = data vs judgement; 2 = partial; 1 = none; 0 = none.
- **EX041 — Recommendations.** List two recommendations. *Rubric:* 3 = account-level block, template fixes, fewer admins, private export; 2 = one; 1 = none; 0 = none.
- **EX042 — Figures.** How are figures organised? *Rubric:* 3 = one per explanation, same scale; 2 = partial; 1 = none; 0 = none.
- **EX043 — Overclaiming.** How was the overclaim fixed? *Rubric:* 3 = expected to reduce; test later; 2 = partial; 1 = none; 0 = none.
- **EX044 — Exposure vs access.** Why is exposure not access? *Rubric:* 3 = data may not have been read; 2 = partial; 1 = none; 0 = none.

### Synthesis

Write clearly, limit claims and separate judgement from evidence.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) prepare for independent examination; (2) respond to examiner questions; (3) revise the dissertation; (4) share results responsibly.

### 8.1 Examination

An external examiner reads the dissertation and the archive. Lucas prepares by rerunning all scripts from the archive on a clean machine.

### 8.2 Questions expected

Could origin labels be wrong? He shows the logging checks and mobile-app rule. Is chi-square appropriate? Expected counts exceed five in all cells. Do findings generalise? Mechanisms may, rates may not.

### 8.3 The defence

In a 45-minute viva, the examiner asks why Lucas did not use multilevel models for team effects. Lucas explains the pre-registered approach and shows the subgroup checks, agreeing that multilevel models would be a good extension.

### 8.4 Revisions

Minor corrections: clarify the register definition, add the power estimate to the results chapter.

### 8.5 Sharing results

Larkspur receives a summary with the recommendations; a short paper is submitted with synthetic data and scripts; no engineer or team names are published.

### 8.6 Follow-through

Larkspur enables account-level public access blocking and fixes the two templates within a quarter.

### Lessons for practice

Lucas writes a two-page note for practitioners: measure exposure by change origin, look for template clustering, count identities with storage admin rights, and use provider account-level controls to make private the default. The note avoids naming Larkspur and links to the shared responsibility pages and CIS Benchmarks instead of recommending products. It is shared on the university's practitioner network and later used in a cloud governance workshop.

### Archive updates

After corrections, the archive gets a new version and manifest, recorded with the date.

### Worked example

Six months later Larkspur repeats the measurement with Lucas's scripts: console exposure has fallen to 1.2% and IaC to 0.3% in synthetic follow-up data, supporting the recommendations while Lucas notes the before-after design's limits.

> **Synthetic case.** Examination and outcomes are synthetic.

### Errors and limits

A before-after improvement may reflect other changes too; note them.

### Exercises

- **EX045 — Preparation.** How did Lucas prepare? *Rubric:* 3 = reran scripts on clean machine; 2 = partial; 1 = none; 0 = none.
- **EX046 — Chi-square check.** Why was chi-square appropriate? *Rubric:* 3 = expected counts over five; 2 = partial; 1 = none; 0 = none.
- **EX047 — Examiner suggestion.** What did the examiner suggest? *Rubric:* 3 = multilevel models; 2 = partial; 1 = none; 0 = none.
- **EX048 — Follow-up rates.** What were follow-up rates? *Rubric:* 3 = console 1.2%, IaC 0.3%; 2 = partial; 1 = none; 0 = none.
- **EX049 — Before-after limit.** What limits the follow-up? *Rubric:* 3 = other changes may explain; 2 = partial; 1 = none; 0 = none.
- **EX050 — Sharing.** What is never published? *Rubric:* 3 = engineer or team names; 2 = partial; 1 = none; 0 = none.

### Synthesis

Prepare reproducibly, answer openly and share responsibly.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Lucas Moreau, Dr Mei Tanaka, Ashcombe University, Larkspur Retail and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A console-created bucket of order exports was public for nine days.

**EX002.** Manual console changes versus weak IaC template defaults.

**EX003.** Whether console changes are more likely than reviewed IaC changes to expose storage, and what explains it.

**EX004.** A storage resource readable without authentication.

**EX005.** Search strings, dates, result counts, screening decisions and reasons.

**EX006.** A review supporting only one explanation cannot judge between two.

**EX007.** The customer's, under shared responsibility models.

**EX008.** Permissions attach to roles, not individuals.

**EX009.** 4 of 11, 36%.

**EX010.** db.admin and storage.write.

**EX011.** A job that can write storage settings could change them.

**EX012.** Private by default with access granted to named identities.

**EX013.** Unused permissions might be needed for rare tasks.

**EX014.** Treat them as review candidates with the owner, not automatic removals.

**EX015.** Larkspur cannot randomly assign how teams make changes.

**EX016.** Time pressure, team, hour and resource type.

**EX017.** They are pseudonymised and results are reported by team and origin.

**EX018.** Hypotheses, primary comparison and planned subgroup checks.

**EX019.** Proportion exposing by origin, risk ratio and chi-square test.

**EX020.** Teams under five engineers are merged into "other".

**EX021.** Higher exposure rate for console changes, persisting within teams and hours.

**EX022.** IaC exposures cluster in a few templates.

**EX023.** Exposures concentrate where many identities hold storage admin rights.

**EX024.** It explains everything and predicts nothing.

**EX025.** Identity breadth.

**EX026.** Yes, both can contribute.

**EX027.** marketing-assets, tmp-export-0412 and partner-drop.

**EX028.** Public, unencrypted and no access logs.

**EX029.** As unintended public access, with an approved register.

**EX030.** Mobile-app console changes had a different origin label.

**EX031.** CIS Benchmarks and CSA CCM v4.

**EX032.** After pilots and before main data, with the reason logged.

**EX033.** IaC 1.0% (12/1,200), console 4.5% (27/600).

**EX034.** Chi-square 23.1 (df 1), risk ratio 4.5.

**EX035.** Nine of twelve.

**EX036.** Accounts with over ten storage admins had higher rates for both origins.

**EX037.** Console: guardrails; IaC: template fixes; identity: fewer storage admins.

**EX038.** The difference is unlikely by chance, not that it is large or causal.

**EX039.** One organisation and year, logging accuracy, incomplete register, exposure not access.

**EX040.** Findings report data; recommendations are labelled judgement.

**EX041.** Account-level public access block, template fixes, fewer admins, a private export process.

**EX042.** One per explanation, on the same scale.

**EX043.** "Expected to reduce", with a suggestion to re-measure.

**EX044.** A public resource may or may not have been read.

**EX045.** He reran all scripts from the archive on a clean machine.

**EX046.** All expected cell counts exceeded five.

**EX047.** Multilevel models for team effects.

**EX048.** Console 1.2%, IaC 0.3%.

**EX049.** Other changes could explain the improvement.

**EX050.** Engineer or team names.

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
