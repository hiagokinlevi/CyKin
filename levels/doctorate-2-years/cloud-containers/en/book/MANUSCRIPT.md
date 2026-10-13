# Cloud and Container Security: A Doctoral Research Book

- Language: English (`en`); course 197, Doctoral research track (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: doctoral candidates designing an original, measurable contribution to cloud and container security.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only cloud accounts, clusters and workloads you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Misconfigurations are taught from the defender's side using synthetic configurations, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one doctoral candidate from a privileged workload that stayed live for months despite daily scanning, through integrity and method, the research frontier, a testable proposal with reliable labels, baseline replication, a stepped main study with independent validation, critique and a verified archive, to the defence. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Amara Okoye** | Doctoral candidate | Invented |
| **Prof. Henrik Lund** | Supervisor | Invented |
| **Thornfield University** | Fictional university | Invented |
| **Meridian Health Cloud** | Fictional industry partner running Kubernetes clusters | Invented |

### Core sources

NIST [SP 800-145](https://doi.org/10.6028/NIST.SP.800-145), [SP 800-210](https://doi.org/10.6028/NIST.SP.800-210), [SP 800-190](https://doi.org/10.6028/NIST.SP.800-190) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); CSA [Cloud Controls Matrix v4](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); the [AWS](https://aws.amazon.com/compliance/shared-responsibility-model/), [Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) and [Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) shared responsibility pages; Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes

You will (1) frame a doctoral question about cloud and container configuration risk; (2) apply research integrity to studies using operational data; (3) choose methods that fit the question; (4) plan for reproducibility from the start.

### 1.1 The opening case

Amara Okoye is a doctoral candidate at the fictional Thornfield University, supervised by Prof. Henrik Lund. Her industry partner, the fictional Meridian Health Cloud, runs about forty Kubernetes clusters for clinical scheduling services. A review the year before found a log-collection workload running as privileged with host filesystem access for eleven months; the daily configuration scan had reported it, but the report was one line among hundreds. Amara asks whether checking configurations at admission, before workloads start, shortens the time risky configurations stay live compared with daily scanning.

### 1.2 The research question

A doctoral question must be specific, answerable and new. Amara's working form: "In managed Kubernetes clusters, does admission-time enforcement of Pod Security Standards reduce the exposure window of risky workload configurations, compared with daily scanning, without unacceptable deployment failures?" Each phrase sets a boundary: managed clusters, a named standard, a measurable outcome and a cost that must also be measured.

### 1.3 Integrity with operational data

Configuration and audit data come from a partner's production systems. Amara agrees in writing what may be collected (configuration metadata and timestamps, never patient data or secrets), how it is stored and who sees it. The university ethics board reviews the plan because staff behaviour is indirectly observed through deployment records.

### 1.4 Choosing methods

The question compares two control designs, so it needs measurement of the same outcome under each, with attention to confounders: teams that adopt admission control early may already be more careful. Amara plans a stepped rollout across clusters, which gives comparison periods without withholding the control from anyone permanently.

### 1.5 Reproducibility from the start

Every analysis will be a script under version control, every dataset a synthetic or de-identified export with a hash, and every decision a dated note. Most of the course's labs rebuild small, synthetic versions of these steps so that readers can repeat them.

### 1.6 Grounding in sources

NIST SP 800-190 describes container risks and countermeasures, including limiting privileges; the Kubernetes Pod Security Standards define Privileged, Baseline and Restricted profiles; Burns et al. (2016) describe how Kubernetes grew from Google's Borg and Omega, which explains why configuration is declarative and checkable before workloads run.

### Worked example

Amara's first supervision meeting produces a one-page plan: question, outcome (hours between a risky configuration becoming live and being removed or blocked), comparison (daily scan versus admission enforcement), cost measure (deployment rejections and override requests), data rules and an archive plan. Prof. Lund asks her to state now what result would count as no effect; she writes "a median difference under two hours or an interval including zero".

> **Synthetic case.** Thornfield University, Meridian Health Cloud, people and data are synthetic.

### Errors and limits

Defining "no effect" after seeing results invites bias; write it down first.

### Exercises

- **EX001 — Question parts.** Which boundaries does Amara's question set? *Rubric:* 3 = clusters, standard, outcome, cost; 2 = three; 1 = one; 0 = none.
- **EX002 — Opening finding.** What did the earlier review find? *Rubric:* 3 = privileged log collector live 11 months despite scan; 2 = partial; 1 = none; 0 = none.
- **EX003 — Data agreement.** What may and may not be collected? *Rubric:* 3 = metadata and timestamps; no patient data or secrets; 2 = partial; 1 = none; 0 = none.
- **EX004 — Ethics review.** Why does the ethics board review the plan? *Rubric:* 3 = staff behaviour observed indirectly; 2 = partial; 1 = none; 0 = none.
- **EX005 — Stepped rollout.** Why use a stepped rollout? *Rubric:* 3 = comparison without withholding permanently; 2 = partial; 1 = none; 0 = none.
- **EX006 — No-effect rule.** How did Amara define no effect? *Rubric:* 3 = median difference under 2 h or interval including zero; 2 = partial; 1 = none; 0 = none.
- **EX007 — Declarative config.** Why does Kubernetes' history matter here? *Rubric:* 3 = declarative config checkable before running; 2 = partial; 1 = none; 0 = none.

### Synthesis

A precise question, written integrity rules and early reproducibility shape the whole study.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Cloud and container security: research frontier

### Learning outcomes

You will (1) map current research and practice on cloud configuration risk; (2) separate established findings from open problems; (3) locate the gap the study fills; (4) read sources critically.

### 2.1 Foundations

Mell and Grance (2011) define cloud computing by on-demand self-service, broad network access, resource pooling, rapid elasticity and measured service. Self-service and elasticity are why configuration changes are frequent and why errors spread quickly. Armbrust et al. (2010) described the economics that made this model dominant.

### 2.2 Shared responsibility

AWS, Microsoft and Google all publish shared responsibility models: the provider secures the underlying infrastructure, the customer secures what they configure, including identities, network rules and workloads. Google's "shared fate" framing adds that providers should offer secure defaults and guidance. Most incidents studied in practice involve the customer's side.

### 2.3 Configuration as code

Rahman, Parnin and Williams (2019) found recurring security smells in infrastructure-as-code scripts, such as hard-coded secrets and overly permissive settings, showing that configuration errors are common and detectable by static checks. Shu, Gu and Enck (2017) found that many container images on a public registry contained known vulnerabilities, so what runs inside containers also matters.

### 2.4 Isolation and multi-tenancy

Ristenpart et al. (2009) showed that co-residence in shared clouds raised information-leakage concerns, which pushed providers to strengthen isolation. For Amara's study it is a reminder that some risks sit with providers and are outside a customer's configuration choices.

### 2.5 Access control and zero trust

NIST SP 800-210 gives access control guidance for cloud systems and SP 800-207 describes zero trust architecture, where every request is evaluated by policy. Admission control is a policy enforcement point in this sense.

### 2.6 The gap

Studies show misconfigurations are common and detectable; guidance recommends preventive controls; but there is little published measurement of how much admission-time enforcement shortens exposure in real clusters, or what it costs in failed deployments. That is the gap.

### Worked example

Amara builds a literature matrix of 34 sources with columns for claim, method, data, setting and limitation. Only four report any measured exposure time, and none compares admission control with scanning in the same organisation. Prof. Lund accepts the gap statement after she removes one claim that rested on a vendor blog without data.

> **Synthetic case.** The matrix counts are synthetic.

### Errors and limits

Vendor reports can be useful leads but are not evidence unless methods and data are shown.

### Exercises

- **EX008 — Essential characteristics.** Name three NIST essential characteristics. *Rubric:* 3 = self-service, network access, pooling, elasticity, measured; 2 = two; 1 = one; 0 = none.
- **EX009 — Customer side.** What does the customer secure under shared responsibility? *Rubric:* 3 = identities, network rules, workloads, configs; 2 = partial; 1 = none; 0 = none.
- **EX010 — Shared fate.** What does Google's shared fate add? *Rubric:* 3 = provider secure defaults and guidance; 2 = partial; 1 = none; 0 = none.
- **EX011 — IaC finding.** What did Rahman et al. find? *Rubric:* 3 = recurring security smells in IaC; 2 = partial; 1 = none; 0 = none.
- **EX012 — Admission and ZTA.** How does admission control relate to SP 800-207? *Rubric:* 3 = policy enforcement point; 2 = partial; 1 = none; 0 = none.
- **EX013 — Gap statement.** State the gap. *Rubric:* 3 = no measurement of exposure reduction and cost; 2 = partial; 1 = none; 0 = none.
- **EX014 — Removed claim.** Why was one claim removed? *Rubric:* 3 = vendor blog without data; 2 = partial; 1 = none; 0 = none.

### Synthesis

Map what is known, what is claimed and what is missing.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Original contribution proposal

### Learning outcomes

You will (1) state a testable contribution; (2) define measures and labels; (3) establish reliable labelling of risky configurations; (4) set decision rules before data collection.

### 3.1 The contribution

Amara proposes two contributions: a measured comparison of exposure windows under scanning and admission enforcement in one organisation, and an open, reusable method for measuring exposure from audit records and configuration history.

### 3.2 Defining risky

A configuration is "risky" if it violates selected Baseline or Restricted checks of the Kubernetes Pod Security Standards: privileged containers, host path volumes, running without runAsNonRoot, or allowing privilege escalation. Using a public standard makes the definition checkable by others.

### 3.3 Labelling and agreement

Automated checks can misfire, so two reviewers independently label a sample of findings as real (R) or not real (N). Agreement is measured with Cohen's kappa, interpreted with the bands of Landis and Koch (1977), where values above 0.80 are "almost perfect".

### Lab — Lab — labelling agreement

```python
"""Cohen's kappa for two raters labelling synthetic misconfiguration findings (stdlib only)."""
a = "RRRRRRRRRRRRNNNNNNNNRRRNNNRRRRNNNNRRRRRRNNNNNNRRRR"
b = "RRRRRRRRRRRNNNNNNNNNRRRNNRRRRRNNNNRRRRRNNNNNNNRRRR"
n = len(a)
po = sum(x == y for x, y in zip(a, b)) / n
pe = sum((a.count(c) / n) * (b.count(c) / n) for c in "RN")
k = (po - pe) / (1 - pe)
print(f"items {n}, observed agreement {po:.2f}, chance {pe:.2f}, kappa {k:.2f}")
```

Run with `python3 lab_kappa.py`. Verified output:

```text
items 50, observed agreement 0.94, chance 0.51, kappa 0.88
```

### 3.4 Lab result

Across 50 synthetic findings the reviewers agree on 94%, against 51% expected by chance, giving kappa 0.88, almost perfect agreement. The three disagreements are discussed and the label guide is clarified for workloads that need host access for a documented reason.

### 3.5 Decision rules

Written before collection: primary outcome median exposure hours; comparison by bootstrap interval; no-effect rule from chapter 1; cost measured as rejection rate with a ceiling of 5% of deployments after the first fortnight.

### Sampling hard cases

Half the labelled sample is drawn from workloads with documented host-access needs, the hardest cases.

### Worked example

The proposal panel asks why kappa rather than raw agreement. Amara shows that with an uneven mix of labels, chance agreement is high, so raw agreement flatters the labels; kappa corrects for that. The panel approves the proposal with one condition: report the exception workloads separately.

> **Synthetic case.** Labels and panel are synthetic.

### Errors and limits

High agreement on an easy sample can hide disagreement on hard cases; sample deliberately.

### Exercises

- **EX015 — Contributions.** State the two contributions. *Rubric:* 3 = measured comparison; reusable method; 2 = partial; 1 = none; 0 = none.
- **EX016 — Risky definition.** What makes a configuration risky? *Rubric:* 3 = selected Pod Security Standards violations; 2 = partial; 1 = none; 0 = none.
- **EX017 — Lab kappa.** What did the lab report? *Rubric:* 3 = 0.94 agreement, 0.51 chance, kappa 0.88; 2 = one; 1 = none; 0 = none.
- **EX018 — Why kappa.** Why use kappa over raw agreement? *Rubric:* 3 = corrects for chance; 2 = partial; 1 = none; 0 = none.
- **EX019 — Cost ceiling.** What cost ceiling was set? *Rubric:* 3 = 5% rejections after fortnight; 2 = partial; 1 = none; 0 = none.
- **EX020 — Panel condition.** What condition did the panel set? *Rubric:* 3 = report exceptions separately; 2 = partial; 1 = none; 0 = none.

### Synthesis

Testable claims need public definitions, reliable labels and rules set in advance.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Baseline replication and pilot

### Learning outcomes

You will (1) replicate the existing daily scan on synthetic workloads; (2) confirm the checks behave as specified; (3) pilot data collection; (4) adjust the protocol.

### 4.1 Why replicate first

Before comparing designs, Amara checks that the measurement tool reproduces what the existing scanner reports. If the checks disagree with the scanner, any later difference could come from the tool, not the control.

### Lab — Lab — workload checks

```python
"""Check synthetic pod specs against selected Pod Security Standards checks (Baseline and Restricted profiles) (stdlib only)."""
pods = {
    "billing-api":  {"privileged": False, "hostPath": False, "runAsNonRoot": True,  "allowPrivilegeEscalation": False},
    "report-job":   {"privileged": False, "hostPath": True,  "runAsNonRoot": True,  "allowPrivilegeEscalation": False},
    "log-agent":    {"privileged": True,  "hostPath": True,  "runAsNonRoot": False, "allowPrivilegeEscalation": True},
    "web-frontend": {"privileged": False, "hostPath": False, "runAsNonRoot": False, "allowPrivilegeEscalation": False},
    "scheduler":    {"privileged": False, "hostPath": False, "runAsNonRoot": True,  "allowPrivilegeEscalation": True},
}
total = 0
for name, s in pods.items():
    v = []
    if s["privileged"]: v.append("privileged")
    if s["hostPath"]: v.append("hostPath volume")
    if not s["runAsNonRoot"]: v.append("runAsNonRoot not set")
    if s["allowPrivilegeEscalation"]: v.append("privilege escalation allowed")
    total += len(v)
    print(f"{name:13} {len(v)} {', '.join(v) or 'compliant'}")
print(f"violations {total}; compliant pods {sum(1 for s in pods.values() if not any([s['privileged'], s['hostPath'], not s['runAsNonRoot'], s['allowPrivilegeEscalation']]))}/{len(pods)}")
```

Run with `python3 lab_baseline.py`. Verified output:

```text
billing-api   0 compliant
report-job    1 hostPath volume
log-agent     4 privileged, hostPath volume, runAsNonRoot not set, privilege escalation allowed
web-frontend  1 runAsNonRoot not set
scheduler     1 privilege escalation allowed
violations 7; compliant pods 1/5
```

### 4.2 Lab result

Five synthetic pod specifications are checked. billing-api is compliant. report-job has one violation (host path volume), web-frontend one (runAsNonRoot not set) and scheduler one (privilege escalation allowed). log-agent has four: privileged, host path volume, runAsNonRoot not set and privilege escalation allowed. In total seven violations; one of five pods is compliant. The existing scanner's synthetic report gives the same seven.

### 4.3 The pilot

For two weeks on two non-production clusters, Amara records each risky configuration's start time from the audit log and its end time from removal or block. The pilot tests whether timestamps are complete and whether the measurement script handles restarts and redeployments.

### 4.4 Protocol changes

The pilot shows that redeploying the same workload creates new pods, which would be counted as new exposures. The protocol now groups pods by owning workload, so exposure is measured per workload configuration.

### 4.5 CIS and provider benchmarks

The CIS Benchmarks for Kubernetes include similar checks; Amara notes overlaps so results can be related to them.

### Recording the replication

The replication record lists both outputs side by side, with the tool version and input hashes.

### Worked example

The pilot also reveals that one cluster's audit logs were retained for only 24 hours, too short to measure long exposures. Meridian's platform team extends retention to 30 days for the study clusters, with the change recorded.

> **Synthetic case.** Pods, logs and counts are synthetic.

### Errors and limits

A pilot is for finding problems in the method, not for estimating the effect.

### Exercises

- **EX021 — Purpose.** Why replicate the scanner first? *Rubric:* 3 = differences must come from control not tool; 2 = partial; 1 = none; 0 = none.
- **EX022 — Lab totals.** What totals did the lab give? *Rubric:* 3 = 7 violations; 1/5 compliant; 2 = partial; 1 = none; 0 = none.
- **EX023 — log-agent.** What violations did log-agent have? *Rubric:* 3 = all four; 2 = one; 1 = none; 0 = none.
- **EX024 — Pod grouping.** What protocol change followed the pilot? *Rubric:* 3 = group pods by owning workload; 2 = partial; 1 = none; 0 = none.
- **EX025 — Retention.** What logging problem was found? *Rubric:* 3 = 24h retention too short; 2 = partial; 1 = none; 0 = none.
- **EX026 — Pilot purpose.** What is a pilot for? *Rubric:* 3 = finding method problems; 2 = partial; 1 = none; 0 = none.

### Synthesis

Replicate the baseline and pilot the method before the main study.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Main study and independent validation

### Learning outcomes

You will (1) run the main comparison; (2) estimate the effect with an interval; (3) measure cost; (4) have results validated independently.

### 5.1 Design

Eight production clusters move from daily scanning to admission enforcement in four steps of two clusters, one step a month. Each cluster contributes exposure measurements before and after its switch.

### 5.2 Exposure outcome

For each risky workload configuration, exposure is hours from becoming live to removal (scanning) or to an approved exception (admission, where a blocked deployment has zero exposure unless an exception is granted).

### Lab — Lab — exposure window

```python
"""Exposure window of risky configs: daily scan vs admission check, with a bootstrap interval (stdlib only)."""
import random, statistics
random.seed(7)
daily = [3, 9, 14, 18, 21, 22, 23, 11, 6, 17, 20, 13, 8, 19, 24, 5, 16, 12, 10, 15]  # hours exposed
admission = [0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0]          # hours exposed (exceptions)
d = statistics.median(daily) - statistics.median(admission)
boots = []
for _ in range(2000):
    s1 = [random.choice(daily) for _ in daily]
    s2 = [random.choice(admission) for _ in admission]
    boots.append(statistics.median(s1) - statistics.median(s2))
boots.sort()
print(f"median daily {statistics.median(daily)} h, admission {statistics.median(admission)} h, difference {d}")
print(f"95% bootstrap interval {boots[49]}-{boots[1949]} h (seed 7, 2000 resamples)")
```

Run with `python3 lab_window.py`. Verified output:

```text
median daily 14.5 h, admission 0.0 h, difference 14.5
95% bootstrap interval 10.5-18.5 h (seed 7, 2000 resamples)
```

### 5.3 Lab result

On the synthetic sample of 20 configurations per arm, the median exposure under daily scanning is 14.5 hours and under admission 0.0 hours, a difference of 14.5 hours. The 95% bootstrap interval is 10.5 to 18.5 hours (seed 7, 2000 resamples), well clear of the no-effect rule.

### 5.4 Cost

Deployment rejections fall from 7% in the first fortnight to 3% after, below the 5% ceiling; exception requests total 11, of which 9 are approved with reasons.

### 5.5 Independent validation

A researcher outside the project reruns the scripts on the archived synthetic and de-identified data and reproduces the medians and interval exactly.

### Threats to validity

Amara lists the main threats. Teams knew the switch dates, so they may have tidied configurations beforehand; she checks the month before each switch and finds no drop in new risky configurations. Some workloads moved between clusters, which she handles by following workload identity. The study covers one organisation, so external validity is limited; the method, not the size of the effect, is what she claims transfers. Writing these threats down alongside the result lets readers judge it fairly.

### Worked example

In the step-two clusters, exposure is higher than expected because exceptions were approved without end dates. Amara reports this separately, as the panel required, and Meridian adds 30-day expiry to exceptions.

> **Synthetic case.** All figures are synthetic.

### Errors and limits

A stepped design reduces but does not remove time effects; report calendar-time checks.

### Exercises

- **EX027 — Design.** Describe the rollout design. *Rubric:* 3 = 8 clusters, 4 steps of 2, monthly; 2 = partial; 1 = none; 0 = none.
- **EX028 — Lab medians.** What were the medians and difference? *Rubric:* 3 = 14.5 vs 0.0; 14.5; 2 = partial; 1 = none; 0 = none.
- **EX029 — Interval.** What was the interval? *Rubric:* 3 = 10.5-18.5 h; 2 = partial; 1 = none; 0 = none.
- **EX030 — Cost result.** Was the cost ceiling met? *Rubric:* 3 = yes, 3% after fortnight; 2 = partial; 1 = none; 0 = none.
- **EX031 — Validation.** How were results validated? *Rubric:* 3 = outside researcher reran scripts; 2 = partial; 1 = none; 0 = none.
- **EX032 — Exceptions.** What raised step-two exposure? *Rubric:* 3 = exceptions without end dates; 2 = partial; 1 = none; 0 = none.

### Synthesis

Estimate with intervals, measure costs and invite independent reruns.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Peer critique and revision

### Learning outcomes

You will (1) invite structured critique of the study; (2) separate valid objections from preferences; (3) revise claims and analyses; (4) record changes transparently.

### 6.1 Seeking critique

Amara presents to the research group and sends the draft paper to two external reviewers: a platform engineer and a measurement researcher. She asks each to identify the weakest claim and the weakest analysis.

### 6.2 Objections received

The platform engineer argues that blocking deployments may push teams to request broad exceptions, moving risk rather than removing it. The measurement researcher notes that blocked deployments counted as zero exposure could hide workarounds such as running the same workload in an unenforced namespace.

### 6.3 Responding

Amara checks both. Exception scope is analysed: 9 approved exceptions, all narrow to one workload. For workarounds, she searches the configuration history for workloads that were blocked and appeared within a day in another namespace; she finds two, both in a development namespace outside the study, and adds a sensitivity analysis counting them as exposed. The median difference stays 14.5 hours in the synthetic data.

### 6.4 Claim revision

The original claim "admission control eliminates exposure" becomes "admission enforcement reduced median exposure by about 14 hours, with a small number of exceptions and possible workarounds measured separately".

### 6.5 Recording changes

A revision log lists each critique, the response and any change in text or analysis, kept in the archive.

### Group critique

The research group meeting adds a practical point: the exception process itself needs measuring, since slow approvals push teams toward workarounds.

### Worked example

One reviewer prefers a different statistical test. Amara explains why the bootstrap fits a skewed, small sample and adds the alternative test as a supplementary result; both agree. The disagreement is recorded as a matter of preference, not a flaw.

> **Synthetic case.** Reviewers and results are synthetic.

### Errors and limits

Absorbing every suggestion can blur the paper; respond to all, change only what improves validity.

### Exercises

- **EX033 — Reviewers asked.** What did Amara ask reviewers for? *Rubric:* 3 = weakest claim and analysis; 2 = partial; 1 = none; 0 = none.
- **EX034 — Workaround objection.** What was the measurement objection? *Rubric:* 3 = zero exposure may hide workarounds; 2 = partial; 1 = none; 0 = none.
- **EX035 — Workarounds found.** How many workarounds were found? *Rubric:* 3 = two in development namespace; 2 = partial; 1 = none; 0 = none.
- **EX036 — Revised claim.** How was the claim revised? *Rubric:* 3 = reduced median ~14h with exceptions noted; 2 = partial; 1 = none; 0 = none.
- **EX037 — Test preference.** How was the test preference handled? *Rubric:* 3 = alternative as supplementary; 2 = partial; 1 = none; 0 = none.
- **EX038 — Revision log.** What does the revision log contain? *Rubric:* 3 = critique, response, change; 2 = two; 1 = one; 0 = none.

### Synthesis

Critique strengthens claims when answered with evidence.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Thesis synthesis and reproducibility archive

### Learning outcomes

You will (1) assemble the thesis argument; (2) package data, code and configuration for reproduction; (3) verify the archive's integrity; (4) document how to rerun.

### 7.1 The argument

The thesis connects the frontier gap (chapter 2), the defined measures (chapter 3), the replicated baseline (chapter 4), the main result (chapter 5) and the revisions (chapter 6) into one argument, with limits stated in each chapter, not saved for the end.

### 7.2 The archive

The archive contains synthetic and de-identified datasets, analysis scripts, policy configurations used in the study, the label guide, the revision log and a README explaining how to rerun every figure.

### 7.3 Integrity manifest

A SHA-256 manifest lists every file. Before submission, the archive is verified against it so examiners can trust that results come from the archived files.

### Lab — Lab — archive verification

```python
"""Build and verify a SHA-256 manifest for a synthetic reproducibility archive (stdlib only)."""
import hashlib
files = {"data/findings.csv": b"id,label\n1,R\n2,N\n", "code/lab_window.py": b"# analysis\n",
         "config/policies.yaml": b"restricted: true\n", "README.md": b"How to rerun the study\n"}
manifest = {p: hashlib.sha256(c).hexdigest() for p, c in files.items()}
files["config/policies.yaml"] = b"restricted: false\n"   # simulate an unrecorded change
bad = [p for p, c in files.items() if hashlib.sha256(c).hexdigest() != manifest[p]]
print(f"files {len(files)}, verified {len(files)-len(bad)}, changed: {', '.join(bad) or 'none'}")
```

Run with `python3 lab_archive.py`. Verified output:

```text
files 4, verified 3, changed: config/policies.yaml
```

### 7.4 Lab result

Of four synthetic files, three verify; config/policies.yaml has changed since the manifest was made. In the lab the change is simulated, flipping restricted to false; in Amara's real check, a late edit to a policy file had not been recorded. She restores the recorded version and reruns the analysis, confirming no result changes.

### 7.5 What cannot be archived

Raw audit logs from Meridian cannot leave the partner; the archive explains how equivalent data can be generated synthetically using the provided generator.

### Writing for examiners

Each results chapter opens with the question it answers and closes with what the result does and does not show. Figures carry their data file names, so examiners can trace any number back to the archive. Amara keeps the main text focused on the argument and moves long tables to appendices, with references from the text. Her supervisor reads each chapter for the single sentence a busy examiner would remember, and asks her to make that sentence explicit.

### Worked example

An examiner later downloads the archive, verifies the manifest and reruns all figures in under an hour on a laptop, noting this in the examination report as a strength.

> **Synthetic case.** Archive contents are synthetic.

### Errors and limits

A manifest proves files are unchanged, not that the analysis is correct.

### Exercises

- **EX039 — Argument links.** Which chapters does the argument connect? *Rubric:* 3 = gap, measures, baseline, result, revisions; 2 = three; 1 = one; 0 = none.
- **EX040 — Archive contents.** List four archive items. *Rubric:* 3 = data, scripts, policies, label guide, log, README; 2 = three; 1 = one; 0 = none.
- **EX041 — Lab result.** What did the archive lab find? *Rubric:* 3 = 3/4 verified; policies.yaml changed; 2 = partial; 1 = none; 0 = none.
- **EX042 — Real change.** What happened in the real check? *Rubric:* 3 = unrecorded late edit restored; 2 = partial; 1 = none; 0 = none.
- **EX043 — Raw logs.** How are raw logs handled? *Rubric:* 3 = stay with partner; synthetic generator; 2 = partial; 1 = none; 0 = none.
- **EX044 — Manifest limit.** What does a manifest not prove? *Rubric:* 3 = analysis correctness; 2 = partial; 1 = none; 0 = none.

### Synthesis

A verified archive lets others rerun the thesis.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Defense and publication plan

### Learning outcomes

You will (1) prepare for the defence; (2) anticipate examiner questions; (3) plan publications and data release; (4) plan responsible communication to practitioners.

### 8.1 Preparing

Amara rehearses a 30-minute talk: problem, gap, method, result, limits and contribution. Mock examiners ask about generalisation, measurement validity and ethics.

### 8.2 Expected questions

Would results hold in unmanaged clusters? Possibly not; managed clusters standardise many settings. Is exposure the right outcome? It is a proxy for risk; the thesis argues it is the variable a control can change. Were staff harmed by blocked deployments? Rejection rates and exception handling are reported, and no individual performance data were used.

### 8.3 Publications

Paper 1: the measurement method and archive, at a software engineering venue. Paper 2: the comparison results, at a security venue. A practitioner article explains the findings without partner details.

### 8.4 Data release

Synthetic data, scripts and policies are released under open licences; partner data are not released, as agreed.

### 8.5 Communicating with practitioners

The guidance stresses gradual rollout, exception expiry and measurement, not blanket blocking. It links to the Kubernetes Pod Security Standards and NIST SP 800-190 rather than prescribing a product.

### 8.6 Future work

Extending the method to infrastructure-as-code checks before deployment and to multiple organisations.

### After the defence

Amara makes the corrections within a month, updates the archive with a new manifest and version number, and records the change in the revision log. She presents the practitioner article at an internal Meridian session, where platform engineers ask for the measurement scripts so they can track exposure themselves. Sharing the scripts turns the thesis method into ongoing practice, which she counts as the clearest sign that the contribution was useful.

### Worked example

At the defence, the examiners ask whether the effect could be due to teams improving over time. Amara shows the calendar-time check and the stepped design. The thesis passes with minor corrections, and Meridian adopts exception expiry across all clusters.

> **Synthetic case.** Defence and outcomes are synthetic.

### Errors and limits

Practitioner summaries tend to drop caveats; keep the key limit in the first paragraph.

### Exercises

- **EX045 — Talk structure.** What is the talk structure? *Rubric:* 3 = problem, gap, method, result, limits, contribution; 2 = four; 1 = two; 0 = none.
- **EX046 — Exposure proxy.** Why use exposure as the outcome? *Rubric:* 3 = variable the control changes; 2 = partial; 1 = none; 0 = none.
- **EX047 — Two papers.** What are the two papers? *Rubric:* 3 = method and archive; comparison results; 2 = partial; 1 = none; 0 = none.
- **EX048 — Data release.** What is released? *Rubric:* 3 = synthetic data, scripts, policies; 2 = partial; 1 = none; 0 = none.
- **EX049 — Practitioner guidance.** What does the guidance stress? *Rubric:* 3 = gradual rollout, exception expiry, measurement; 2 = two; 1 = one; 0 = none.
- **EX050 — Time question.** How did Amara answer the time-effect question? *Rubric:* 3 = calendar-time check and stepped design; 2 = partial; 1 = none; 0 = none.

### Synthesis

Defend with evidence, publish openly and communicate carefully.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Amara Okoye, Prof. Henrik Lund, Thornfield University, Meridian Health Cloud and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Managed clusters, Pod Security Standards, exposure window as outcome, and deployment failures as cost.

**EX002.** A privileged workload with host access ran for eleven months although the daily scan reported it.

**EX003.** Configuration metadata and timestamps only; never patient data or secrets.

**EX004.** Deployment records indirectly reveal staff behaviour.

**EX005.** It gives comparison periods without withholding the control permanently.

**EX006.** A median difference under two hours or an interval including zero.

**EX007.** Configuration is declarative, so it can be checked before workloads run.

**EX008.** On-demand self-service, broad network access, resource pooling, rapid elasticity and measured service.

**EX009.** What they configure: identities, network rules and workloads.

**EX010.** Providers should offer secure defaults and guidance.

**EX011.** Recurring security smells such as hard-coded secrets in infrastructure-as-code scripts.

**EX012.** It acts as a policy enforcement point evaluating each request.

**EX013.** Little measurement of how much admission enforcement shortens exposure and what it costs.

**EX014.** It rested on a vendor blog with no data.

**EX015.** A measured comparison of exposure windows and a reusable measurement method.

**EX016.** Violating selected Baseline or Restricted Pod Security Standards checks.

**EX017.** Observed agreement 0.94, chance 0.51, kappa 0.88.

**EX018.** It corrects for agreement expected by chance.

**EX019.** Rejections under 5% of deployments after the first fortnight.

**EX020.** Report exception workloads separately.

**EX021.** So later differences reflect the control, not the measurement tool.

**EX022.** Seven violations; one of five pods compliant.

**EX023.** Privileged, host path volume, runAsNonRoot not set and privilege escalation allowed.

**EX024.** Exposure measured per owning workload, not per pod.

**EX025.** Audit logs were kept only 24 hours.

**EX026.** Finding problems in the method, not estimating the effect.

**EX027.** Eight clusters switched in four monthly steps of two.

**EX028.** 14.5 hours vs 0.0 hours; difference 14.5.

**EX029.** 10.5 to 18.5 hours.

**EX030.** Yes; rejections fell to 3%.

**EX031.** An outside researcher reran the scripts and reproduced them.

**EX032.** Exceptions approved without end dates.

**EX033.** The weakest claim and the weakest analysis.

**EX034.** Counting blocked deployments as zero could hide workarounds elsewhere.

**EX035.** Two, both in a development namespace.

**EX036.** Admission enforcement reduced median exposure by about 14 hours, with exceptions and workarounds measured separately.

**EX037.** The alternative test was added as a supplementary result.

**EX038.** Each critique, the response and any change made.

**EX039.** The gap, measures, replicated baseline, main result and revisions.

**EX040.** Datasets, scripts, policy configurations, label guide, revision log and README.

**EX041.** Three of four verified; config/policies.yaml had changed.

**EX042.** An unrecorded policy edit was found, restored and the analysis rerun.

**EX043.** They stay with the partner; a synthetic generator is provided.

**EX044.** That the analysis is correct.

**EX045.** Problem, gap, method, result, limits and contribution.

**EX046.** It is a risk proxy that the control can change.

**EX047.** One on the method and archive, one on comparison results.

**EX048.** Synthetic data, scripts and policies, not partner data.

**EX049.** Gradual rollout, exception expiry and measurement.

**EX050.** With the calendar-time check and stepped design.

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
