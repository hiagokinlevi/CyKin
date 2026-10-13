# Identity and Access Management: Postgraduate Specialisation

- Language: English (`en`); course 148, Postgraduate specialisation (2 years).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: practitioners and postgraduates who lead privileged access and identity decisions in organisations.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only identity systems and accounts you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic accounts, entitlements, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one postgraduate engineer redesigning privileged access at a fictional logistics company, from framing the decision and current practice through measuring standing privilege, risk and ethics of monitoring, scored design alternatives, a controlled pilot, organisational integration, difficult cases, board assurance, research critique, rollout and final transfer. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Marta Kowalczyk** | Postgraduate student and engineer | Invented |
| **Prof. Leila Haddad** | Supervisor | Invented |
| **Ashdown Graduate School** | Fictional school | Invented |
| **Corran Logistics** | Fictional employer (600 staff) | Invented |

### Core sources

NIST [SP 800-63-4](https://doi.org/10.6028/NIST.SP.800-63-4), [SP 800-63B-4](https://doi.org/10.6028/NIST.SP.800-63B-4), [SP 800-162](https://doi.org/10.6028/NIST.SP.800-162), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); IETF [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749) and [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700); [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html); W3C [WebAuthn Level 2](https://www.w3.org/TR/webauthn-2/); OASIS [SAML 2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame a privileged access decision for senior leaders; (2) weigh risk, cost and disruption; (3) document decisions with their reasoning.

### 1.1 The case

Marta Kowalczyk is a postgraduate student at the fictional Ashdown Graduate School, supervised by Prof. Leila Haddad. She also works part-time as an infrastructure engineer at the fictional Corran Logistics, a distribution company with 600 staff and three warehouses. Corran has eight administrator accounts with permanent, full rights to its cloud directory, servers and warehouse systems; two are shared by the night shift. An insurer's questionnaire asked how privileged access is controlled, and nobody could answer well. Marta's postgraduate project asks how Corran should manage privileged access, and whether the chosen approach actually reduces risk without slowing operations.

### 1.2 Decisions under uncertainty

Senior leaders rarely have complete information. Marta frames the decision as a choice among options, each with uncertain benefits and costs. She lists what is known, such as the number of administrators and how often they need full rights, and what is uncertain, such as how likely an administrator account is to be compromised. Instead of pretending to precision, she uses ranges and scenarios: what happens if a shared night-shift account is misused, and how quickly would anyone notice? This framing helps leaders see the decision clearly without a false sense of certainty.

### 1.3 Weighing risk, cost and disruption

Every option has three faces. Risk reduction is the security benefit. Cost includes licences, staff time and training. Disruption is the effect on operations, such as a warehouse system update delayed because an administrator must request access first. Marta agrees with Corran's operations director that disruption matters as much as cost, because a missed delivery window has real financial and reputational consequences. Stating these weights openly lets leaders see the trade-offs they are making, and prevents security work from being judged on security benefit alone.

### 1.4 Recording the reasoning

Marta keeps a decision record for each significant choice: the question, options, criteria, evidence, decision, who made it and what would trigger a review. NIST SP 800-53 Rev. 5 includes controls for privileged accounts within its access control family, which she cites when explaining why the decision matters, but the record focuses on Corran's own reasoning. Months later, when an auditor or new director asks why Corran chose a particular approach, the record answers with evidence rather than recollection, and shows that the decision was made deliberately rather than by default.

### Worked example

Marta frames the privileged access decision with three options, three weighted faces and a decision record template agreed with the operations director.

> **Synthetic case.** Marta Kowalczyk, Ashdown Graduate School, Corran Logistics and all figures are synthetic; NIST SP 800-53 Rev. 5 is a real source.

### Errors and limits

Presenting a security decision with false precision hides uncertainty that leaders need to understand.

### Exercises

- **EX001 — Corran admins.** How many administrator accounts does Corran have, and how many are shared? *Rubric:* 3 = eight, two shared by night shift;; 2 = eight;; 1 = two;; 0 = none.
- **EX002 — Uncertainty handling.** How does Marta handle uncertain likelihoods? *Rubric:* 3 = ranges and scenarios, not false precision;; 2 = scenarios;; 1 = exact numbers;; 0 = none.
- **EX003 — Three faces.** What are the three faces of every option? *Rubric:* 3 = risk reduction, cost, disruption;; 2 = two;; 1 = one;; 0 = none.
- **EX004 — Disruption example.** Give an example of disruption from privileged access controls. *Rubric:* 3 = warehouse update delayed by an access request;; 2 = delay;; 1 = vague;; 0 = none.
- **EX005 — Decision record fields.** Name four fields in Marta's decision record. *Rubric:* 3 = question, options, criteria, evidence, decision, owner, review trigger (four);; 2 = three;; 1 = one;; 0 = none.

### Synthesis

Good security decisions name options, weigh risk, cost and disruption openly and record their reasoning.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Identity and access management: current practice

### Learning outcomes

You will (1) describe current practice in privileged access management; (2) relate it to published guidance; (3) assess Corran against it.

### 2.1 What privileged access means

Privileged accounts can change systems, read any data or create other accounts. They include directory administrators, server administrators, database owners and service accounts with broad rights. Misuse of one, whether by an attacker or by mistake, can affect the whole organisation. Current practice treats privileged access as a distinct problem from ordinary access, with stronger authentication, tighter control over when privilege is held and closer monitoring. Marta begins by listing every privileged identity at Corran, including service accounts, finding fourteen in total rather than the eight that staff first mentioned.

### 2.2 Common practices

Several practices are now widespread. Administrators use separate administrator accounts, not their everyday accounts. Strong, phishing-resistant authentication, as described in NIST SP 800-63B-4, protects those accounts. Just-in-time elevation grants full rights only when needed, for a limited time, with a recorded reason. Credentials for shared or emergency accounts are kept in a vault and released with logging. Sessions on critical systems may be recorded. And privileged activity is monitored for unusual patterns. Zero trust guidance in NIST SP 800-207 reinforces the idea that standing trust should be minimised.

### 2.3 Corran against practice

Marta compares Corran with these practices. Administrators use their everyday accounts with administrator rights attached. Multi-factor authentication uses text message codes. Rights are permanent. Two night-shift administrators share an account whose password is on a sticky note in a locked office. No vault exists. Monitoring alerts only on failed sign-ins. She presents this gap analysis factually, noting that Corran's practices are common for its size and history, which helps leaders accept the findings without defensiveness. Each gap is linked to the risk it creates and the practice that would close it.

### 2.4 Limits of best practice

Published practice describes what many organisations do, not what every organisation must do. Some practices, such as full session recording, need tools and staff time Corran may not have. Marta distinguishes practices that address Corran's main risks cheaply, such as separate administrator accounts and phishing-resistant keys, from those whose value depends on scale. This avoids recommending an expensive suite simply because it appears in vendor material, and focuses Corran's limited budget on the controls that matter most for its situation.

### Worked example

Marta's gap analysis finds fourteen privileged identities, everyday accounts used for administration, text-code multi-factor, permanent rights, a shared night-shift account and no vault.

> **Synthetic case.** Identities, practices and findings are synthetic; NIST SP 800-63B-4 and SP 800-207 are real sources.

### Errors and limits

Recommending every published practice regardless of scale wastes a small organisation's budget.

### Exercises

- **EX006 — Privileged count.** How many privileged identities did Marta find? *Rubric:* 3 = fourteen, including service accounts;; 2 = 14;; 1 = 8;; 0 = none.
- **EX007 — JIT meaning.** What is just-in-time elevation? *Rubric:* 3 = full rights only when needed, time-limited, with reason;; 2 = temporary rights;; 1 = permanent;; 0 = none.
- **EX008 — Night shift account.** How is the night-shift account's password kept? *Rubric:* 3 = on a sticky note in a locked office;; 2 = written;; 1 = vault;; 0 = none.
- **EX009 — Gap tone.** Why present the gap analysis factually and as common practice? *Rubric:* 3 = helps leaders accept findings without defensiveness;; 2 = acceptance;; 1 = style;; 0 = none.
- **EX010 — Scale-dependent practice.** Which practice's value depends on scale? *Rubric:* 3 = full session recording;; 2 = recording;; 1 = separate accounts;; 0 = none.

### Synthesis

Current practice separates, strengthens, limits and monitors privileged access; organisations adopt what fits their risks.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Identity and access management: specialist evidence

### Learning outcomes

You will (1) measure standing privilege; (2) gather evidence on how administrators actually work; (3) interpret specialist data carefully.

### 3.1 Measuring standing privilege

Standing privilege means rights held all the time, whether or not they are being used. Marta measures it as privilege-hours: the number of administrators multiplied by hours in a week during which they hold full rights. With eight permanent administrators, that is 1,344 privilege-hours every week. She then asks how many hours administrators actually need full rights, using change records and interviews. The difference between held and needed privilege is exposure that serves no purpose, and it becomes a central measure in her project.

### Lab — Standing versus just-in-time

```python
"""Standing versus just-in-time administrator privilege-hours per week for synthetic admins (stdlib only)."""
admins = {"adm01": 3.0, "adm02": 6.5, "adm03": 1.0, "adm04": 0.5, "adm05": 4.0, "adm06": 2.0, "adm07": 0.0, "adm08": 1.5}
standing = len(admins) * 168
jit = sum(admins.values())
print(f"admins={len(admins)} standing_priv_hours={standing} jit_priv_hours={jit:.1f} reduction={100*(1-jit/standing):.1f}%")
print("never activated:", [a for a, h in admins.items() if h == 0])
```

Run with `python3 lab_standing.py`. Verified output:

```text
admins=8 standing_priv_hours=1344 jit_priv_hours=18.5 reduction=98.6%
never activated: ['adm07']
```

### 3.2 Reading the result

In the synthetic data, the eight administrators actually needed full rights for 18.5 hours in a typical week. Under just-in-time elevation, privilege-hours would fall from 1,344 to 18.5, a reduction of about 98.6 percent. One administrator, adm07, needed full rights not at all, which raises the question of whether that account is needed. Marta treats the figure carefully: it assumes elevation would match need exactly, and emergencies may add hours. Still, the scale of the difference shows how much exposure permanent rights create.

The 1,344 figure is simply eight administrators holding full rights for all 168 hours of the week.

### 3.3 Interpreting carefully

Specialist data can mislead. Change records may miss urgent fixes made without tickets, so needed hours may be underestimated. Interviews may reflect what administrators think they do rather than what they do. Marta compares change records, interviews and directory logs, and where they disagree she investigates. For example, logs show adm02 using administrator rights late on several evenings, which change records do not explain; it turns out to be a scheduled report that could run under a service account with much narrower rights.

### Worked example

Standing privilege of 1,344 hours per week compares with 18.5 hours needed; adm07 never needs full rights and adm02's evening use is moved to a narrow service account.

> **Synthetic case.** Administrators, hours and logs are synthetic.

### Errors and limits

Assuming change records capture every administrator action underestimates the real need for elevation.

### Exercises

- **EX011 — Standing hours.** What standing privilege-hours does the lab compute? *Rubric:* 3 = 1,344 per week;; 2 = 1344;; 1 = 18.5;; 0 = none.
- **EX012 — JIT reduction.** What reduction would just-in-time give in the lab? *Rubric:* 3 = about 98.6%, to 18.5 hours;; 2 = 98.6%;; 1 = 50%;; 0 = none.
- **EX013 — Unused admin.** Which administrator never needed full rights? *Rubric:* 3 = adm07;; 2 = one;; 1 = adm02;; 0 = none.
- **EX014 — Triangulation sources.** Which three sources does Marta compare? *Rubric:* 3 = change records, interviews, directory logs;; 2 = two;; 1 = one;; 0 = none.
- **EX015 — Evening use fix.** How is adm02's evening administrator use addressed? *Rubric:* 3 = scheduled report moved to narrow service account;; 2 = service account;; 1 = ignored;; 0 = none.

### Synthesis

Measuring standing versus needed privilege reveals exposure that serves no purpose, and careful triangulation keeps the measure honest.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) assess privileged access risk with evidence; (2) consider ethical issues in monitoring administrators; (3) balance accountability with trust.

### 4.1 Risk assessment

Marta assesses privileged access risks using likelihood and impact, supported by evidence. A shared night-shift account has high impact, because its actions cannot be traced, and moderate likelihood of misuse, given the written password. Text-code multi-factor on administrator accounts has high impact if bypassed through a fake sign-in page. Permanent rights increase the window in which a stolen session can do harm. She ranks these risks, explains the evidence behind each rating and avoids treating her scores as precise measurements.

### 4.2 Monitoring administrators

Stronger monitoring of administrators raises ethical questions. Administrators are trusted colleagues, and constant scrutiny can feel like an accusation. Yet their access is powerful, and accountability protects them too: clear records can show they did not cause a problem. Marta proposes monitoring focused on actions, such as elevation outside change windows and changes to security settings, rather than on keystrokes or screen recording of all work. Administrators are told exactly what is monitored and why, and the monitoring policy is agreed with their manager and HR.

### 4.3 Accountability and trust

Accountability and trust are not opposites. Individual named accounts make every action attributable, which allows trust to be based on evidence rather than assumption. Marta explains to the night-shift administrators that ending the shared account protects them: if something goes wrong at 03:00, the records will show who did what, rather than casting suspicion on everyone who knew the password. Framing controls as protection for honest staff, not suspicion of them, makes adoption smoother and more respectful. Both night administrators agree to the change.

### 4.4 Data protection

Privileged activity logs are personal data about administrators. Marta applies purpose limitation: logs are used for security and troubleshooting, not for judging productivity. Retention is set at one year, matching investigation needs, and access to the logs is limited to the security lead and auditors, with each access recorded. She documents these decisions in Corran's data protection records. Applying privacy principles to monitoring of administrators shows that security and respect for staff can be designed together. The policy is reviewed each year with HR.

### Worked example

Marta ranks the shared night-shift account and text-code administrator authentication highest, and proposes action-focused monitoring agreed with HR and explained to administrators.

> **Synthetic case.** Risks, ratings and policies are synthetic.

### Errors and limits

Recording all administrator screens by default damages trust and collects far more personal data than security needs.

### Exercises

- **EX016 — Shared account impact.** Why is the shared night-shift account high impact? *Rubric:* 3 = actions cannot be traced to a person;; 2 = untraceable;; 1 = cost;; 0 = none.
- **EX017 — Monitoring focus.** What does Marta's monitoring focus on? *Rubric:* 3 = actions such as off-window elevation and security setting changes;; 2 = actions;; 1 = keystrokes;; 0 = none.
- **EX018 — Protection framing.** How does ending the shared account protect honest staff? *Rubric:* 3 = records show who did what, avoiding suspicion on all;; 2 = attribution;; 1 = vague;; 0 = none.
- **EX019 — Log retention.** How long are privileged activity logs kept? *Rubric:* 3 = one year;; 2 = year;; 1 = forever;; 0 = none.
- **EX020 — Log access.** Who may access privileged activity logs? *Rubric:* 3 = security lead and auditors, with access recorded;; 2 = limited;; 1 = everyone;; 0 = none.

### Synthesis

Evidence-based risk rating and transparent, purpose-limited monitoring balance accountability with trust.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Identity and access management: design alternatives

### Learning outcomes

You will (1) define realistic privileged access designs; (2) score them against agreed weighted criteria; (3) test the sensitivity of the ranking.

### 5.1 Three designs

Marta defines three designs. Design A keeps existing administrator accounts but adds a password vault for shared and emergency credentials and phishing-resistant keys. Design B replaces everyday-account administration with named administrator accounts, security keys and just-in-time elevation through the cloud directory's built-in features, with a vault only for emergency accounts. Design C buys a full privileged access management suite with session recording, credential rotation and approval workflows. Each design is described in enough detail to estimate cost and disruption. Costs are estimated over three years.

### 5.2 Criteria and weights

Criteria are agreed with Corran's IT manager and operations director before scoring: risk reduction weighted 35 percent, operability for a small team 25 percent, cost 20 percent and disruption 20 percent. Each design is scored from one to three on each criterion, with written evidence such as vendor documentation, a two-week trial of built-in elevation and staff estimates. Agreeing weights before scoring prevents the analysis being bent towards a favourite option after the numbers are known. The agreed weights are signed off in writing.

### Lab — Weighted scoring

```python
"""Weighted scoring of three privileged-access designs on agreed criteria (scores 1-3; stdlib only)."""
w = {"risk reduction": 0.35, "operability": 0.25, "cost": 0.20, "disruption": 0.20}
opts = {"A: vault + shared admin": {"risk reduction": 1, "operability": 3, "cost": 3, "disruption": 3},
        "B: named admin + JIT": {"risk reduction": 3, "operability": 2, "cost": 2, "disruption": 2},
        "C: full PAM suite": {"risk reduction": 3, "operability": 1, "cost": 1, "disruption": 1}}
for o, s in sorted(opts.items(), key=lambda kv: -sum(w[c]*kv[1][c] for c in w)):
    print(f"{o:26} weighted={sum(w[c]*s[c] for c in w):.2f}")
```

Run with `python3 lab_score.py`. Verified output:

```text
B: named admin + JIT       weighted=2.35
A: vault + shared admin    weighted=2.30
C: full PAM suite          weighted=1.70
```

### 5.3 Reading the scores

Design B scores 2.35, Design A 2.30 and Design C 1.70. B leads, but only narrowly ahead of A, so Marta tests sensitivity. If risk reduction is weighted slightly less, A overtakes B; if risk reduction is weighted more, B's lead grows. Because Corran's insurer and board have stressed privileged access risk, the agreed weighting is defensible, but she reports the closeness openly. C ranks last because its operability and disruption scores are poor for a small team, despite strong risk reduction.

A lead of 0.05 is smaller than the swing from a modest change in weights, so the result is a narrow preference rather than a clear win.

### Worked example

Weighted scores rank B (2.35) narrowly ahead of A (2.30) and well ahead of C (1.70); sensitivity analysis shows the B–A order depends on keeping risk reduction weighted highly.

> **Synthetic case.** Designs, weights and scores are synthetic.

### Errors and limits

Presenting a narrow scoring lead as decisive hides how sensitive the ranking is to the weights chosen.

### Exercises

- **EX021 — Design B content.** What does Design B include? *Rubric:* 3 = named admin accounts, keys, JIT via built-in features, vault for emergencies;; 2 = JIT;; 1 = suite;; 0 = none.
- **EX022 — Top score.** Which design scores highest in the lab, and with what? *Rubric:* 3 = B, 2.35;; 2 = B;; 1 = C;; 0 = none.
- **EX023 — Narrow margin.** How large is B's lead over A? *Rubric:* 3 = 0.05;; 2 = narrow;; 1 = large;; 0 = none.
- **EX024 — Sensitivity finding.** What changes the B–A order? *Rubric:* 3 = weighting risk reduction lower;; 2 = weights;; 1 = nothing;; 0 = none.
- **EX025 — Suite weakness.** Why does Design C rank last? *Rubric:* 3 = poor operability and disruption for small team;; 2 = operability;; 1 = security;; 0 = none.

### Synthesis

Realistic alternatives, agreed weights and sensitivity analysis make design choices transparent.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Identity and access management: controlled evaluation

### Learning outcomes

You will (1) pilot the chosen design with a controlled comparison; (2) measure outcomes against a baseline; (3) review out-of-window activations.

### 6.1 Pilot design

Corran approves Design B. Marta pilots it for six weeks with four of the eight administrators, chosen to cover day and night shifts, while the other four continue as before. Both groups' activity is measured over the same weeks. The comparison is not randomised, since shift patterns made that impractical, so Marta records differences between the groups, such as workload, that could affect results. Measures include privilege-hours, elevation requests, time to obtain elevation and any operational delays reported by warehouse managers.

### 6.2 Results

The pilot group's privilege-hours fall from 672 a week to about 9, while the comparison group stays at 672. Median time to obtain elevation is under two minutes, because the built-in workflow approves standard requests automatically during change windows. Warehouse managers report one delay, when an administrator's security key was left at home; a second key, registered and kept in the office safe, solves this. These results suggest Design B reduces exposure greatly with little disruption, though a six-week pilot cannot show long-term effects.

### Lab — Out-of-window activations

```python
"""Flag administrator activations outside approved change windows in synthetic logs (stdlib only)."""
acts = [("adm01", "Tue", 19), ("adm02", "Wed", 10), ("adm05", "Sat", 2), ("adm02", "Thu", 22), ("adm06", "Mon", 9),
        ("adm03", "Sun", 14), ("adm01", "Fri", 11), ("adm04", "Tue", 20), ("adm02", "Fri", 16), ("adm05", "Wed", 13)]
def in_window(day, h): return (day in ("Mon", "Tue", "Wed", "Thu", "Fri") and 8 <= h < 18) or (day == "Tue" and 18 <= h < 22)
out = [a for a in acts if not in_window(a[1], a[2])]
print(f"activations={len(acts)} outside_window={len(out)}")
for a in out: print("  review:", a)
```

Run with `python3 lab_window.py`. Verified output:

```text
activations=10 outside_window=3
  review: ('adm05', 'Sat', 2)
  review: ('adm02', 'Thu', 22)
  review: ('adm03', 'Sun', 14)
```

### 6.3 Reviewing activations

Of ten synthetic activations, three fall outside approved windows: adm05 at 02:00 on Saturday, adm02 at 22:00 on Thursday and adm03 on Sunday afternoon. Each is reviewed with the administrator. Two are genuine emergencies with incident tickets; one is a routine task done at a convenient time, which is not wrong but should be scheduled. Marta reports this as evidence that monitoring works and that most out-of-window use has legitimate reasons, which reassures administrators that monitoring is about understanding, not catching people out.

### Worked example

The pilot cuts privilege-hours from 672 to about 9 a week with two-minute elevation; three of ten activations fall outside windows, two of them documented emergencies.

> **Synthetic case.** Groups, hours and activations are synthetic.

### Errors and limits

Treating every out-of-window activation as misconduct ignores genuine emergencies and damages trust.

### Exercises

- **EX026 — Pilot comparison.** How is the pilot comparison structured? *Rubric:* 3 = four admins on Design B, four unchanged, same weeks;; 2 = two groups;; 1 = vague;; 0 = none.
- **EX027 — Elevation time.** What is the median time to obtain elevation? *Rubric:* 3 = under two minutes;; 2 = minutes;; 1 = hours;; 0 = none.
- **EX028 — Key fix.** How was the forgotten key problem solved? *Rubric:* 3 = second key kept in the office safe;; 2 = spare key;; 1 = password;; 0 = none.
- **EX029 — Off-window count.** How many activations fall outside windows in the lab? *Rubric:* 3 = three of ten;; 2 = three;; 1 = vague;; 0 = none.
- **EX030 — Off-window outcomes.** What did review find about the out-of-window activations? *Rubric:* 3 = two emergencies, one routine task to schedule;; 2 = mostly legitimate;; 1 = misconduct;; 0 = none.

### Synthesis

A controlled pilot with a comparison group and reviewed activations shows both the benefit and the practical effects of the design.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access management: organizational integration

### Learning outcomes

You will (1) integrate the privileged access design with change management, HR and incident response; (2) assign ownership; (3) train staff.

### 7.1 Change management

Just-in-time elevation works best when tied to change management. Marta links elevation requests to change tickets, so each request names the change it supports, and approved change windows define when standard requests are automatically approved. Emergency elevation outside windows needs a reason and is reviewed the next working day. This integration means privileged activity can be traced from the change that justified it to the actions taken, which helps both auditors and engineers investigating problems after a change. Auditors can follow this trail easily.

### 7.2 HR and lifecycle

Administrator status must follow employment. When HR records that an administrator moves role or leaves, their administrator account is disabled and their keys revoked the same day. New administrators receive access only after their manager's approval and completion of a short training module. Marta works with HR to add administrator status to the leaver checklist and to the six-monthly access review, so privileged accounts are never left behind when the people who held them have gone. The training module takes about thirty minutes.

### 7.3 Incident response

The incident response plan is updated so that suspected misuse of privileged access has a clear procedure: revoke active elevations, disable the account, preserve logs, inform the security lead and investigate. Emergency accounts in the vault are documented for use if normal administrator access fails during an incident. Marta runs a tabletop exercise with the IT team, discovering that nobody knew the vault's emergency release procedure at night. The procedure is simplified and printed in the incident pack. The exercise is repeated yearly.

### 7.4 Ownership and training

Each part of the design has an owner: the IT manager owns administrator policy, the security lead owns monitoring, HR owns lifecycle triggers and the operations director approves change windows. Marta runs short training for administrators covering why the changes matter, how to request elevation, what is monitored and what to do if a key is lost. Training is practical and brief, and administrators leave with a one-page guide. Clear ownership and training keep the design working after the project ends.

### Worked example

Elevation links to change tickets, HR triggers disable administrator accounts on the same day, a tabletop exercise simplifies night-time vault release, and four owners are named.

> **Synthetic case.** Processes, owners and exercises are synthetic.

### Errors and limits

Introducing just-in-time elevation without linking it to change management loses the reason behind each elevation.

### Exercises

- **EX031 — Change link.** How is elevation linked to change management? *Rubric:* 3 = requests name the change ticket; windows auto-approve;; 2 = tickets;; 1 = vague;; 0 = none.
- **EX032 — Leaver admin.** When are a leaving administrator's account and keys removed? *Rubric:* 3 = same day as HR records it;; 2 = same day;; 1 = month;; 0 = none.
- **EX033 — Tabletop finding.** What did the tabletop exercise reveal? *Rubric:* 3 = nobody knew night-time vault release procedure;; 2 = vault;; 1 = nothing;; 0 = none.
- **EX034 — Owners named.** Name two owners in the design. *Rubric:* 3 = IT manager, security lead, HR, operations director (two);; 2 = one;; 1 = vague;; 0 = none.
- **EX035 — Training contents.** Name two topics in administrator training. *Rubric:* 3 = why, how to request, what is monitored, lost keys (two);; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Linking privileged access to change, HR, incident response and clear owners embeds it in how the organisation works.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Identity and access management: difficult cases

### Learning outcomes

You will (1) handle service accounts, third-party administrators and legacy systems; (2) manage exceptions; (3) accept residual risk explicitly.

### 8.1 Service accounts

Six of Corran's fourteen privileged identities are service accounts used by software, such as backup jobs and the warehouse management interface. They cannot use security keys or just-in-time elevation in the same way as people. Marta documents each with owner, purpose and permissions, reduces permissions to what the task needs, moves credentials into the vault with automatic rotation where the software supports it, and sets alerts for interactive sign-ins, which a service account should never perform. Two accounts turn out to be unused and are disabled after owner confirmation.

### 8.2 Third-party administrators

The warehouse system supplier administers its software remotely. Previously it used a shared account with permanent access. Marta designs named accounts for each supplier engineer, linked to a Corran sponsor, with access enabled only when a support ticket is open and automatically removed afterwards. Supplier engineers authenticate with strong methods agreed in the contract. Activity is logged and reviewed. This brings third parties into the same principles as staff: named, limited in time and accountable. The contract is updated to require these terms at renewal.

### 8.3 Legacy systems

One warehouse control system cannot integrate with the cloud directory and has a single local administrator account. Replacement is planned in eighteen months. Meanwhile, the account password is held in the vault, released only through a logged request, and rotated after each use. Physical access to the console is limited. Marta records this as an exception with its compensating controls, its owner and its end date, rather than pretending the system meets the new design. The exception is reviewed every quarter until replacement.

### 8.4 Residual risk

After the design and exceptions, some risk remains: the legacy system, the supplier's own security practices and the possibility of an administrator's key and device both being stolen. Marta states each residual risk, its likely impact, the compensating controls and who accepts it. Corran's finance director, as risk owner, signs the list. Reviewing it every six months, or after any incident, ensures that accepted risks remain conscious decisions rather than forgotten gaps. Each entry also records the date of the next review and any trigger that would bring it forward.

### Worked example

Six service accounts are documented and reduced, two disabled; supplier access becomes ticket-linked named accounts; the legacy controller is a time-limited exception with vault rotation.

> **Synthetic case.** Accounts, suppliers and systems are synthetic.

### Errors and limits

Pretending a legacy system meets the new design, instead of recording an exception, hides a known gap.

### Exercises

- **EX036 — Service account alert.** Which activity should alert for a service account? *Rubric:* 3 = interactive sign-in;; 2 = interactive;; 1 = any;; 0 = none.
- **EX037 — Unused service accounts.** How many service accounts were found unused? *Rubric:* 3 = two;; 2 = 2;; 1 = vague;; 0 = none.
- **EX038 — Supplier access window.** When is supplier engineer access enabled? *Rubric:* 3 = only while a support ticket is open;; 2 = ticket;; 1 = always;; 0 = none.
- **EX039 — Legacy controls.** What compensating controls protect the legacy controller? *Rubric:* 3 = vault, logged release, rotation after use, physical limits;; 2 = vault;; 1 = vague;; 0 = none.
- **EX040 — Risk owner.** Who signs the residual risk list? *Rubric:* 3 = finance director as risk owner;; 2 = director;; 1 = Marta;; 0 = none.

### Synthesis

Service accounts, suppliers and legacy systems need tailored controls, explicit exceptions and signed residual risk.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Identity and access management: leadership and assurance

### Learning outcomes

You will (1) report privileged access status to the board; (2) provide assurance with evidence; (3) answer an insurer's questions.

### 9.1 Reporting to the board

Marta prepares a one-page board report: the problem, the chosen design, results from the pilot and rollout, remaining risks and next steps. Figures include privilege-hours before and after, the share of administrator accounts with phishing-resistant keys, out-of-window activations reviewed and residual risks accepted. She uses plain language and one chart. Board members ask whether the changes slowed operations; she answers with the pilot's two-minute median elevation time and the single delay, now fixed. Board members receive the full assurance pack on request.

### 9.2 Assurance

Assurance means giving confidence, based on evidence, that controls work. Marta assembles an assurance pack: configuration exports showing settings, test results from the verification exercises, samples of elevation requests linked to change tickets, activation reviews and the residual risk register. Each item is dated and traceable. Corran's external auditor reviews a sample and confirms the evidence supports the claims, adding a recommendation to test vault emergency release twice a year. Marta adds the recommendation to the sustaining plan, with the security lead named as owner of the tests and their results.

### 9.3 Answering the insurer

The insurer's questionnaire, which started the project, asks how privileged access is controlled. Corran can now answer precisely: named administrator accounts, phishing-resistant authentication, just-in-time elevation linked to change, vaulted emergency and legacy credentials, monitored activity and documented exceptions. Each answer references evidence. Marta cautions against overclaiming, such as saying all privileged access is just-in-time when service accounts and the legacy system are exceptions, because inaccurate answers to insurers can cause problems if a claim is ever made. The answers are reviewed by the finance director.

### 9.4 Leadership lessons

Marta reflects on leading change without formal authority. Progress came from explaining risks in business terms, involving administrators early, piloting before committing and reporting honestly. The board supported the work because it saw evidence and understood trade-offs. She also learned that assurance is ongoing: controls drift, people change and new systems arrive, so evidence must be refreshed regularly rather than assembled once and filed away. She notes these lessons in her dissertation as practical guidance for engineers who must lead change from within a team rather than from a management position, which is common in smaller organisations.

### Worked example

The board report shows privilege-hours falling by about 98 percent with minimal delay; an auditor confirms the assurance pack; the insurer receives precise, evidenced answers with exceptions stated.

> **Synthetic case.** Reports, auditors and insurers are synthetic.

### Errors and limits

Overclaiming to an insurer, such as saying all privileged access is just-in-time, can cause problems if a claim is made.

### Exercises

- **EX041 — Board figures.** Name two figures in the board report. *Rubric:* 3 = privilege-hours, key coverage, off-window reviews, residual risks (two);; 2 = one;; 1 = vague;; 0 = none.
- **EX042 — Assurance meaning.** What is assurance? *Rubric:* 3 = confidence, based on evidence, that controls work;; 2 = evidence;; 1 = hope;; 0 = none.
- **EX043 — Auditor recommendation.** What did the auditor recommend? *Rubric:* 3 = test vault emergency release twice a year;; 2 = testing;; 1 = nothing;; 0 = none.
- **EX044 — Overclaim example.** What overclaim does Marta warn against? *Rubric:* 3 = saying all privileged access is just-in-time;; 2 = all JIT;; 1 = vague;; 0 = none.
- **EX045 — Ongoing assurance.** Why must assurance evidence be refreshed? *Rubric:* 3 = controls drift, people change, new systems arrive;; 2 = drift;; 1 = rules;; 0 = none.

### Synthesis

Plain board reporting, evidenced assurance and accurate external answers make privileged access management credible.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) read research on access control and authentication critically; (2) assess evidence quality; (3) connect findings to practice.

### 10.1 Reading critically

Marta reads published research to inform her work and to place it in context. She reads Sandhu and colleagues (1996) on role-based access control, Bonneau and colleagues (2012) on comparing authentication schemes and Herley (2009) on why users reject security advice. For each, she asks what question was studied, what method was used, what evidence supports the conclusions and how far they apply to Corran. Reading critically means neither accepting conclusions because they are published nor dismissing them because the setting differs.

Herley's argument concerns ordinary users weighing security advice, so Marta asks whether it fits Corran's administrators, who face different incentives.

### 10.2 Evidence quality

Evidence varies in strength. A formal model, like the role-based access control family, shows what is logically possible but not how organisations behave. A comparative framework, like Bonneau and colleagues', structures judgement but depends on the evaluators' ratings. A large measurement study, like Florêncio and Herley (2007) on password habits, shows real behaviour at scale but in a consumer setting. Marta notes the kind of evidence each provides, so she uses each for what it can support and no more.

### 10.3 Connecting to practice

Herley's argument that people rationally reject costly security advice helps explain why Corran's administrators had resisted earlier controls that added friction without visible benefit. Design B's fast, automatic elevation reduced friction, which may explain its smoother adoption. Bonneau and colleagues' framework helped Marta compare authenticators for administrators systematically. Connecting research to practice in this way strengthens her recommendations, while she remains careful not to claim that published findings prove what happened at Corran. She marks these links as interpretations, not findings, and invites readers to weigh them against Corran's own evidence.

### 10.4 Writing a critique

Marta writes a short critique of one paper for her course, summarising its question, method and findings, then assessing strengths, limitations and relevance. She avoids attacking the authors and focuses on what the evidence can and cannot show. She also notes what further research would help, such as studies of privileged access practices in small and medium organisations, where published evidence is thin. Good critique advances understanding by being fair, specific and constructive. Her lecturer's feedback praises the balance and suggests one further limitation about sampling.

### Worked example

Marta's critique of a password-habits study praises its scale, notes its consumer setting and suggests workplace studies of administrators as further research.

> **Synthetic case.** Marta's critique is synthetic; the cited papers are real.

### Errors and limits

Treating a formal model as evidence of how organisations behave confuses logical possibility with observed practice.

### Exercises

- **EX046 — Critical questions.** What four questions does Marta ask of each paper? *Rubric:* 3 = question, method, evidence, applicability;; 2 = three;; 1 = one;; 0 = none.
- **EX047 — Model limitation.** What can a formal model not show? *Rubric:* 3 = how organisations actually behave;; 2 = behaviour;; 1 = logic;; 0 = none.
- **EX048 — Herley relevance.** How does Herley's argument help explain Corran? *Rubric:* 3 = admins resisted costly controls without visible benefit;; 2 = friction;; 1 = vague;; 0 = none.
- **EX049 — Research gap.** What further research does Marta suggest? *Rubric:* 3 = privileged access practices in small and medium organisations;; 2 = SMEs;; 1 = vague;; 0 = none.
- **EX050 — Critique tone.** What should a good critique focus on? *Rubric:* 3 = what evidence can and cannot show, fairly and constructively;; 2 = evidence;; 1 = authors;; 0 = none.

### Synthesis

Critical reading matches each kind of evidence to what it can support and connects research to practice carefully.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) roll out the design across Corran; (2) measure outcomes against the baseline; (3) document lessons.

### 11.1 Rollout

After the pilot, Design B is rolled out to all administrators over four weeks. Each administrator receives two security keys, a named administrator account and training. The shared night-shift account is disabled after both night administrators have individual accounts and have used them successfully for a week. Supplier access moves to ticket-linked named accounts. Each step has a rollback plan and is verified afterwards. Marta tracks progress weekly with the IT manager and records issues as they arise. No operational incidents occur during rollout.

### 11.2 Outcomes

After eight weeks, Marta measures outcomes using the same definitions as the baseline. Standing privilege-hours fall from 1,344 to about 22 per week, slightly higher than the pilot estimate because of two incident weeks. All human administrators use phishing-resistant keys. Shared administrator accounts fall from one to none. Out-of-window activations average three a week, all reviewed within one working day. Service accounts are documented, with two removed. She reports each with counts and dates. Results are presented to the IT manager and filed with the assurance pack.

### 11.3 Unexpected effects

Some effects were not planned. Administrators report that requesting elevation made them think twice before changes, catching two mistakes. Conversely, a warehouse manager complained that an overnight fix took ten minutes longer while the administrator located a key. Marta records both. Unexpected effects, good and bad, are part of an honest evaluation and often point to the next improvement, such as storing spare keys at each warehouse for night shifts. She also asks administrators for further suggestions, gathering three more small ideas that the IT manager adopts over the following month.

### 11.4 Documenting lessons

Marta writes lessons for Corran and for her dissertation: pilot before rollout, involve night shifts early, provide two keys per administrator, link elevation to change tickets and review out-of-window activity kindly. She also notes what she would change, such as starting the service account work earlier. Lessons are written with evidence from the project, so they can guide Corran's next identity projects and help other organisations of similar size. Each lesson names the evidence behind it and the situation in which it applies, so readers can judge whether it fits their own organisation before adopting it.

### Worked example

Rollout cuts standing privilege-hours from 1,344 to about 22 per week, removes the shared account and brings all human administrators onto keys; spare warehouse keys address night-shift delays.

> **Synthetic case.** Rollout, outcomes and lessons are synthetic.

### Errors and limits

Reporting only intended outcomes hides side effects that point to the next improvement.

### Exercises

- **EX051 — Rollout privilege-hours.** What were standing privilege-hours after rollout? *Rubric:* 3 = about 22 per week, from 1,344;; 2 = 22;; 1 = 18.5;; 0 = none.
- **EX052 — Higher than pilot.** Why were rollout hours higher than the pilot estimate? *Rubric:* 3 = two incident weeks;; 2 = incidents;; 1 = error;; 0 = none.
- **EX053 — Positive side effect.** What positive side effect did administrators report? *Rubric:* 3 = thinking twice caught two mistakes;; 2 = fewer mistakes;; 1 = vague;; 0 = none.
- **EX054 — Night-shift fix.** What addresses night-shift key delays? *Rubric:* 3 = spare keys at each warehouse;; 2 = spare keys;; 1 = passwords;; 0 = none.
- **EX055 — Hindsight.** What would Marta start earlier? *Rubric:* 3 = service account work;; 2 = service accounts;; 1 = nothing;; 0 = none.

### Synthesis

A careful rollout with consistent measurement, honest side effects and evidenced lessons completes the applied project.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) review the whole project; (2) transfer ownership to Corran; (3) reflect on professional development.

### 12.1 Final review

Marta and Prof. Haddad review the project against its aims. Corran now has named, key-protected administrators, just-in-time elevation, vaulted emergency and legacy credentials, monitored activity, documented service accounts and a signed residual risk register. Standing privilege has fallen by about 98 percent with small operational cost. Limits remain: eight weeks of post-rollout data, one organisation and a legacy system awaiting replacement. Marta's dissertation reports these honestly with evidence. Prof. Haddad agrees the conclusions match the evidence, and suggests making the limits section more prominent so readers see it before the recommendations.

### 12.2 Transfer to Corran

Ownership transfers formally. The IT manager owns the administrator policy and elevation configuration; the security lead owns monitoring and activation reviews; HR owns lifecycle triggers; the finance director owns the residual risk register. Marta hands over runbooks, the assurance pack, training materials and test cases. A handover meeting walks through each item, and owners confirm they can run their parts. The transfer is recorded, so responsibility is clear after Marta's project role ends. A copy of every handed-over item is stored in Corran's document system.

### 12.3 Sustaining the change

Marta proposes a sustaining plan: quarterly review of privileged identities, six-monthly vault emergency release tests, yearly training refreshers and a check whenever a new system is added. Measures continue in the monthly IT report. She warns that without such routines, standing privilege tends to creep back as quick fixes accumulate. Sustaining change is harder than making it, and naming routines and owners is the best protection against gradual decline. The IT manager adds each routine to the team calendar with a named owner, and the first quarterly review is scheduled before Marta leaves.

### 12.4 Professional reflection

Marta reflects on her development: from engineer to someone who frames decisions for leaders, measures outcomes and communicates evidence. She learned that technical controls succeed only when people understand and accept them, and that honest reporting of limits builds more trust than polished claims. She plans to share an anonymised summary with a regional practitioner group, contributing to the thin evidence base on privileged access in mid-sized organisations. Prof. Haddad encourages her to present at the group's next meeting, and Corran agrees, provided the summary is reviewed for identifying details first.

### Worked example

The final review confirms a 98 percent reduction in standing privilege with stated limits; four owners accept formal transfer and a sustaining plan sets quarterly, six-monthly and yearly routines.

> **Synthetic case.** Reviews, owners and plans are synthetic.

### Errors and limits

Ending a project without sustaining routines lets standing privilege creep back through quick fixes.

### Exercises

- **EX056 — Post-rollout limit.** Name one limit Marta states in the final review. *Rubric:* 3 = eight weeks of data, one organisation, legacy system (one);; 2 = one;; 1 = vague;; 0 = none.
- **EX057 — Register owner.** Who owns the residual risk register after transfer? *Rubric:* 3 = finance director;; 2 = director;; 1 = Marta;; 0 = none.
- **EX058 — Sustaining routines.** Name two sustaining routines. *Rubric:* 3 = quarterly identity review, six-monthly vault test, yearly training, new-system check (two);; 2 = one;; 1 = vague;; 0 = none.
- **EX059 — Creep warning.** What happens without sustaining routines? *Rubric:* 3 = standing privilege creeps back;; 2 = drift;; 1 = nothing;; 0 = none.
- **EX060 — Sharing plan.** How will Marta share her findings beyond Corran? *Rubric:* 3 = anonymised summary to a regional practitioner group;; 2 = practitioners;; 1 = vague;; 0 = none.

### Synthesis

Honest review, formal transfer and named sustaining routines turn a project into lasting practice.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Marta Kowalczyk, Prof. Leila Haddad, Ashdown Graduate School, Corran Logistics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Eight, two of which are shared by the night shift.

**EX002.** With ranges and scenarios rather than false precision.

**EX003.** Risk reduction, cost and disruption.

**EX004.** A warehouse system update delayed because an administrator must request access first.

**EX005.** Question, options, evidence and review trigger (also criteria, decision and decision-maker).

**EX006.** Fourteen, including service accounts.

**EX007.** Granting full rights only when needed, for a limited time, with a recorded reason.

**EX008.** On a sticky note in a locked office.

**EX009.** So leaders accept the findings without becoming defensive.

**EX010.** Full session recording.

**EX011.** 1,344 privilege-hours per week.

**EX012.** About 98.6 percent, from 1,344 to 18.5 privilege-hours.

**EX013.** adm07.

**EX014.** Change records, interviews and directory logs.

**EX015.** The scheduled report is moved to a service account with much narrower rights.

**EX016.** Its actions cannot be traced to an individual.

**EX017.** Actions such as elevation outside change windows and changes to security settings.

**EX018.** Records show exactly who did what, so suspicion does not fall on everyone.

**EX019.** One year.

**EX020.** The security lead and auditors, with each access recorded.

**EX021.** Named administrator accounts, security keys and built-in just-in-time elevation, with a vault for emergency accounts.

**EX022.** Design B, with 2.35.

**EX023.** 0.05 (2.35 versus 2.30).

**EX024.** Weighting risk reduction lower lets A overtake B.

**EX025.** Its operability and disruption scores are poor for a small team.

**EX026.** Four administrators use Design B while four continue unchanged over the same weeks.

**EX027.** Under two minutes.

**EX028.** A second registered key kept in the office safe.

**EX029.** Three of ten.

**EX030.** Two were genuine emergencies; one was a routine task that should be scheduled.

**EX031.** Each request names its change ticket, and approved windows auto-approve standard requests.

**EX032.** The same day HR records the move or departure.

**EX033.** Nobody knew the vault's emergency release procedure at night.

**EX034.** The IT manager (policy) and the security lead (monitoring); also HR and the operations director.

**EX035.** How to request elevation and what is monitored (also why changes matter and lost keys).

**EX036.** An interactive sign-in, which a service account should never perform.

**EX037.** Two, disabled after owner confirmation.

**EX038.** Only while a support ticket is open.

**EX039.** Vaulted password with logged release, rotation after each use and limited physical access.

**EX040.** Corran's finance director, as risk owner.

**EX041.** Privilege-hours before and after and the share of administrators with phishing-resistant keys.

**EX042.** Confidence, based on evidence, that controls work.

**EX043.** Testing vault emergency release twice a year.

**EX044.** Saying all privileged access is just-in-time when exceptions exist.

**EX045.** Because controls drift, people change and new systems arrive.

**EX046.** What was studied, how, what evidence supports it and how far it applies to Corran.

**EX047.** How organisations actually behave.

**EX048.** It explains why administrators resisted earlier controls that added friction without visible benefit.

**EX049.** Studies of privileged access practices in small and medium organisations.

**EX050.** What the evidence can and cannot show, fairly and constructively.

**EX051.** About 22 per week, down from 1,344.

**EX052.** Because of two weeks with incidents.

**EX053.** Requesting elevation made them think twice, catching two mistakes.

**EX054.** Storing spare keys at each warehouse.

**EX055.** The service account work.

**EX056.** Only eight weeks of post-rollout data (also one organisation or the legacy system).

**EX057.** The finance director.

**EX058.** Quarterly privileged identity reviews and six-monthly vault release tests (also yearly training).

**EX059.** Standing privilege tends to creep back as quick fixes accumulate.

**EX060.** By sharing an anonymised summary with a regional practitioner group.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Bonneau, J., Herley, C., van Oorschot, P. C., & Stajano, F. (2012). The quest to replace passwords: A framework for comparative evaluation of web authentication schemes. *2012 IEEE Symposium on Security and Privacy*, 553–567. <https://doi.org/10.1109/SP.2012.44>
- Ferraiolo, D. F., Sandhu, R., Gavrila, S., Kuhn, D. R., & Chandramouli, R. (2001). Proposed NIST standard for role-based access control. *ACM Transactions on Information and System Security*, 4(3), 224–274. <https://doi.org/10.1145/501978.501980>
- Florêncio, D., & Herley, C. (2007). A large-scale study of web password habits. *Proceedings of the 16th International Conference on World Wide Web*, 657–666. <https://doi.org/10.1145/1242572.1242661>
- Hardt, D. (Ed.). (2012). *The OAuth 2.0 authorization framework* (RFC 6749). IETF. <https://www.rfc-editor.org/rfc/rfc6749>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- Hu, V. C., Ferraiolo, D., Kuhn, R., Schnitzer, A., Sandlin, K., Miller, R., & Scarfone, K. (2014). *Guide to attribute based access control (ABAC) definition and considerations* (NIST SP 800-162). NIST. <https://doi.org/10.6028/NIST.SP.800-162>
- Hunt, P. (Ed.), Grizzle, K., Ansari, M., Wahlstroem, E., & Mortimore, C. (2015). *System for Cross-domain Identity Management: Protocol* (RFC 7644). IETF. <https://www.rfc-editor.org/rfc/rfc7644>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Jones, M., Bradley, J., & Sakimura, N. (2015). *JSON Web Token (JWT)* (RFC 7519). IETF. <https://www.rfc-editor.org/rfc/rfc7519>
- Kuhn, D. R., Coyne, E. J., & Weil, T. R. (2010). Adding attributes to role-based access control. *Computer*, 43(6), 79–81. <https://doi.org/10.1109/MC.2010.155>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Lodderstedt, T., Bradley, J., Labunets, A., & Fett, D. (2025). *Best current practice for OAuth 2.0 security* (RFC 9700, BCP 240). IETF. <https://www.rfc-editor.org/rfc/rfc9700>
- Molloy, I., Chen, H., Li, T., Wang, Q., Li, N., Bertino, E., Calo, S., & Lobo, J. (2008). Mining roles with semantic meanings. *Proceedings of the 13th ACM Symposium on Access Control Models and Technologies*, 21–30. <https://doi.org/10.1145/1377836.1377840>
- OASIS. (2005). *Assertions and protocols for the OASIS Security Assertion Markup Language (SAML) V2.0*. OASIS Standard. <https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Sakimura, N., Bradley, J., & Agarwal, N. (2015). *Proof Key for Code Exchange by OAuth public clients* (RFC 7636). IETF. <https://www.rfc-editor.org/rfc/rfc7636>
- Sakimura, N., Bradley, J., Jones, M., de Medeiros, B., & Mortimore, C. (2014). *OpenID Connect Core 1.0*. OpenID Foundation. <https://openid.net/specs/openid-connect-core-1_0.html>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sandhu, R. S., Coyne, E. J., Feinstein, H. L., & Youman, C. E. (1996). Role-based access control models. *Computer*, 29(2), 38–47. <https://doi.org/10.1109/2.485845>
- Temoshok, D., Proud-Madruga, D., Choong, Y.-Y., Galluzzo, R., Gupta, S., LaSalle, C., Lefkovitz, N., & Regenscheid, A. (2025). *Digital identity guidelines* (NIST SP 800-63-4). NIST. <https://doi.org/10.6028/NIST.SP.800-63-4>
- Temoshok, D., Fenton, J. L., Choong, Y.-Y., Lefkovitz, N., Regenscheid, A., Galluzzo, R., & Richer, J. P. (2025). *Digital identity guidelines: Authentication and authenticator management* (NIST SP 800-63B-4). NIST. <https://doi.org/10.6028/NIST.SP.800-63B-4>
- W3C. (2021). *Web Authentication: An API for accessing public key credentials, Level 2*. W3C Recommendation. <https://www.w3.org/TR/webauthn-2/>
