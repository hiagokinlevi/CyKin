# Identity and Access Management: Master's Research Track

- Language: English (`en`); course 171, Master's research track (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students and practitioners researching authentication and account recovery in identity and access management.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only identity systems and accounts you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic accounts, entitlements, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one master's student measuring whether passkey enrolment at a fictional insurer reduces password resets without lowering sign-in success, from question and literature method through an advanced seminar on assurance and phishing resistance, study design and ethics, competing explanations, proposal and pilot, data analysis, dissertation writing and an independent review and viva. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Jonah Reyes** | Master's student | Invented |
| **Dr Ingrid Solberg** | Supervisor | Invented |
| **Marlow Bay University** | Fictional university | Invented |
| **Halyard Insurance** | Fictional industry partner | Invented |

### Core sources

NIST [SP 800-63-4](https://doi.org/10.6028/NIST.SP.800-63-4), [SP 800-63B-4](https://doi.org/10.6028/NIST.SP.800-63B-4), [SP 800-162](https://doi.org/10.6028/NIST.SP.800-162), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); IETF [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749) and [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700); [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html); W3C [WebAuthn Level 2](https://www.w3.org/TR/webauthn-2/); OASIS [SAML 2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) frame a master's question about passkey adoption and account recovery; (2) search and screen literature systematically; (3) define measures before collecting data.

### 1.1 The case

Jonah Reyes is a master's student at the fictional Marlow Bay University, supervised by Dr Ingrid Solberg. His industry partner is the fictional Halyard Insurance, about nine hundred staff, whose service desk handles around forty password reset requests a week. Each reset takes staff time, interrupts work and is a known target for social engineering, because a caller who convinces the desk can take over an account. Halyard plans to enrol staff in passkeys, a phishing-resistant sign-in method based on the W3C Web Authentication standard. Jonah's dissertation asks a focused question: does passkey enrolment reduce password reset requests without lowering sign-in success?

### 1.2 Why the question matters

Passwords are forgotten, reused and phished; Florêncio and Herley (2007) showed in a large study that users hold many accounts and reuse a small number of passwords across them. Resets are the visible cost of that burden. NIST SP 800-63B-4 describes phishing-resistant authenticators and explains why they resist attacks that trick users into revealing secrets. If passkeys remove most reasons to reset a password, the service desk saves time and an attack path narrows. But if passkeys cause sign-in failures, staff may be locked out more often, which would simply move the burden elsewhere. Both outcomes must be measured.

### 1.3 Searching systematically

Jonah plans his literature search before running it. He lists databases, search terms such as passkey, WebAuthn, FIDO2, password reset and help desk, and a date range. He records every search string, the date and the number of results, so another student could repeat the search exactly. Inclusion criteria are written in advance: published from 2015, reporting empirical or survey evidence rather than opinion, and set in workplaces rather than consumer websites or student samples. Applying criteria written beforehand stops him unconsciously including papers that agree with what he hopes to find.

### Lab — Screening records

```python
"""Screen synthetic literature records against inclusion criteria and count each stage (stdlib only)."""
recs = [("R01", 2019, "empirical", "workplace"), ("R02", 2012, "empirical", "web"), ("R03", 2021, "opinion", "workplace"),
        ("R04", 2022, "empirical", "workplace"), ("R05", 2016, "empirical", "student"), ("R06", 2023, "empirical", "workplace"),
        ("R07", 2020, "survey", "workplace"), ("R08", 2018, "empirical", "web"), ("R09", 2024, "empirical", "workplace"),
        ("R10", 2017, "opinion", "web"), ("R11", 2023, "empirical", "student"), ("R12", 2021, "empirical", "workplace")]
s1 = [r for r in recs if r[1] >= 2015]; s2 = [r for r in s1 if r[2] in ("empirical", "survey")]; s3 = [r for r in s2 if r[3] == "workplace"]
print(f"found={len(recs)} year>=2015={len(s1)} evidence={len(s2)} workplace={len(s3)}")
print("included:", [r[0] for r in s3])
```

Run with `python3 lab_screen.py`. Verified output:

```text
found=12 year>=2015=11 evidence=9 workplace=6
included: ['R01', 'R04', 'R06', 'R07', 'R09', 'R12']
```

### 1.4 Reading the screen

Of twelve synthetic records, one is excluded for its date, two for being opinion pieces and three for studying web users or students rather than workplaces, leaving six. Jonah records the reason for every exclusion in a table, which forms the basis of a flow diagram in his literature chapter. Six included studies is a small base, so he notes that his review will be narrative rather than statistical. He also keeps excluded consumer studies in a separate list, because they may still help explain mechanisms, even though they do not answer his workplace question directly.

### 1.5 Defining measures

Jonah defines two primary measures before collecting data. The first is password reset requests per hundred active staff per week, normalised because headcount changes. The second is sign-in success rate: successful sign-ins divided by all attempts, from the identity provider's synthetic-style aggregate logs. A secondary measure is the number of lockouts needing desk help. Each measure has a written definition, a data source and a known weakness: reset counts depend on how desk staff categorise tickets, so he checks a sample of tickets by hand to confirm categories are applied consistently.

### Worked example

Jonah frames the question, writes inclusion criteria, screens twelve synthetic records to six workplace studies and defines reset rate per hundred staff and sign-in success as primary measures.

> **Synthetic case.** Jonah Reyes, Marlow Bay University, Halyard Insurance and all records and figures are synthetic.

### Errors and limits

Screening without criteria written in advance invites selection of studies that confirm the hoped-for answer.

### Exercises

- **EX001 — Reset risk.** Why are password resets a security concern as well as a cost? *Rubric:* 3 = social engineering can take over accounts via the desk;; 2 = social engineering;; 1 = cost only;; 0 = none.
- **EX002 — Passkey basis.** Which standard are passkeys based on? *Rubric:* 3 = W3C Web Authentication;; 2 = WebAuthn;; 1 = SAML;; 0 = none.
- **EX003 — Search record.** What must Jonah record for each search? *Rubric:* 3 = string, date and result count;; 2 = two;; 1 = vague;; 0 = none.
- **EX004 — Screen counts.** How many records remain after screening in the lab? *Rubric:* 3 = 6 of 12, with stage counts 11, 9, 6;; 2 = 6;; 1 = 12;; 0 = none.
- **EX005 — Exclusion reasons.** Why were three records excluded at the last stage? *Rubric:* 3 = they studied web users or students, not workplaces;; 2 = setting;; 1 = date;; 0 = none.
- **EX006 — Normalisation reason.** Why normalise resets per hundred staff? *Rubric:* 3 = headcount changes over time;; 2 = headcount;; 1 = vague;; 0 = none.
- **EX007 — Ticket check.** How does Jonah check reset-count reliability? *Rubric:* 3 = hand-check a sample of ticket categories;; 2 = sample;; 1 = trust;; 0 = none.

### Synthesis

A focused question, a repeatable search with fixed criteria and measures defined in advance give a master's study a solid start.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Identity and access management: advanced seminar

### Learning outcomes

You will (1) explain authentication assurance and phishing resistance; (2) describe how passkeys and federation work; (3) relate research findings to Halyard's plan.

### 2.1 Authentication assurance

NIST SP 800-63B-4 describes authentication assurance levels, which express how confident a system can be that the person signing in controls the authenticator bound to the account. Higher levels require multiple factors and stronger protections. The guidelines also describe phishing resistance: an authenticator resists phishing when it will not release a usable secret to a site that is impersonating the real one. One-time codes typed by the user do not have this property, because a user can be tricked into typing them into a fake page that relays them. Jonah uses these definitions to describe Halyard's current and planned methods precisely.

### 2.2 How passkeys work

With WebAuthn, a device or security key creates a key pair for each site. The private key stays on the device; the site stores only the public key. To sign in, the site sends a challenge, and the device signs it after the user unlocks it, often with a fingerprint or device PIN. The signature is bound to the site's origin, so a look-alike site receives nothing it can use at the real one. There is no shared secret for the user to forget or reveal, which is why passkeys may remove many reasons for password resets.

### 2.3 Federation and single sign-on

Halyard staff sign in once to an identity provider, which then vouches for them to many applications. Older applications use SAML 2.0, an OASIS standard in which the provider sends signed assertions; newer ones use OpenID Connect, built on OAuth 2.0, in which the provider issues signed ID tokens. Because applications trust the provider, strengthening sign-in at the provider strengthens it everywhere at once. That makes the provider the right place to introduce passkeys, and it also means a fault there affects every application, which Jonah must consider when measuring sign-in success.

### 2.4 What research says

Bonneau, Herley, van Oorschot and Stajano (2012) evaluated many alternatives to passwords against usability, deployability and security benefits and found that none dominated passwords on all of them. Their framework helps Jonah ask which benefits passkeys offer Halyard and which costs remain, such as device loss and recovery. Herley (2009) warned that security advice users find costly will be rationally ignored. Passkeys may succeed partly because they reduce effort rather than adding it. Jonah notes that most published evidence comes from consumer settings, so workplace evidence such as his is a useful addition.

### 2.5 Recovery remains

Passkeys do not eliminate account recovery. Staff lose phones, replace laptops and forget device PINs. If recovery falls back to a weak method, such as a desk agent resetting access after a phone call, attackers will target that path instead. NIST SP 800-63B-4 discusses authenticator loss and recovery as part of the lifecycle. Jonah therefore records recovery requests separately from password resets, and notes Halyard's recovery procedure, which requires an in-person or video identity check. Measuring only password resets could show an improvement while hiding a shift of risk into recovery.

### Worked example

Jonah describes Halyard's move from password plus one-time code to passkeys at the identity provider, using assurance levels, phishing resistance and the federation path, and plans to track recovery separately.

> **Synthetic case.** Halyard's systems are synthetic; the standards and papers cited are real.

### Errors and limits

Treating any multi-factor method as phishing-resistant ignores that typed one-time codes can be relayed by a fake site.

### Exercises

- **EX008 — Assurance meaning.** What does an authentication assurance level express? *Rubric:* 3 = confidence the person controls the bound authenticator;; 2 = confidence;; 1 = speed;; 0 = none.
- **EX009 — OTP weakness.** Why are typed one-time codes not phishing-resistant? *Rubric:* 3 = users can type them into a fake page that relays them;; 2 = relay;; 1 = they are;; 0 = none.
- **EX010 — Private key location.** Where does the passkey private key stay? *Rubric:* 3 = on the user's device or security key;; 2 = device;; 1 = server;; 0 = none.
- **EX011 — Origin binding.** What does origin binding prevent? *Rubric:* 3 = a look-alike site getting a usable signature;; 2 = phishing;; 1 = vague;; 0 = none.
- **EX012 — Federation leverage.** Why introduce passkeys at the identity provider? *Rubric:* 3 = strengthens sign-in for every federated application at once;; 2 = everywhere;; 1 = cheaper;; 0 = none.
- **EX013 — Comparative framework.** What did Bonneau and colleagues find when comparing password alternatives? *Rubric:* 3 = none dominated passwords on all benefits;; 2 = no winner;; 1 = passkeys best;; 0 = no answer.
- **EX014 — Recovery tracking.** Why track recovery requests separately? *Rubric:* 3 = risk may shift from resets to recovery;; 2 = shift;; 1 = no reason;; 0 = none.

### Synthesis

Passkeys bind sign-in to the real site and remove shared secrets, but recovery must be measured, because risk can move there.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) design a before-and-after study with comparison; (2) handle staff data ethically; (3) make the analysis reproducible.

### 3.1 Design

Halyard enrols departments in passkeys over three months, so Jonah uses a staggered design. He compares each department's reset rate in six weeks before enrolment with six weeks after, and uses departments not yet enrolled as a comparison over the same calendar weeks. If reset rates fall only in enrolled departments, passkeys are a more plausible cause than a general trend. The order of departments is set by Halyard's IT team for practical reasons, not chosen by Jonah, and he records that order in advance, because it cannot be randomised.

### 3.2 Ethics and data

Sign-in and ticket data reveal individuals' working patterns. Jonah's data agreement gives him only weekly aggregates per department, never individual sign-ins or names, prepared by Halyard's identity team. Departments with fewer than ten staff are merged so no individual can be singled out. Data stays on a university server with access logged and is deleted after the degree is awarded. Ethics approval covers short interviews with desk staff, who can withdraw. Jonah never accesses Halyard's systems himself, and the examples in this book use synthetic data with the same structure.

### 3.3 Analysis plan

Before seeing data, Jonah writes his analysis plan. The main comparison is the change in reset rate per hundred staff in enrolled departments minus the change in not-yet-enrolled departments over the same weeks. Sign-in success is compared with an interval for each method. He specifies what would count against his hypothesis, a reset reduction similar in both groups or a fall in sign-in success, and how he will handle missing weeks. Writing this first prevents him from choosing, after the fact, whichever analysis gives the most attractive result.

### 3.4 Reproducibility

Jonah keeps every script, the analysis plan, data dictionary and version history in a repository. Scripts use only the Python standard library and read a single aggregate file whose format is documented, so anyone with a file of the same structure can rerun them. A synthetic file with that structure is published with the dissertation. He records the exact export date and query used by Halyard's team. When the dissertation reports a number, a reader can trace it to the script and input that produced it, which is what reproducible means in practice.

### 3.5 Change control

Because Halyard's rollout is a real change, Jonah has no say over its pace and must not influence it to suit his study. He agrees with the IT team that any change to the rollout plan, such as pausing a department after problems, will be shared with him and recorded. Such events become part of the data, not something to hide. Separating the organisation's operational decisions from the researcher's analysis protects both: Halyard runs its rollout safely, and Jonah's results honestly describe what actually happened.

### Worked example

Jonah fixes a staggered before-and-after design with not-yet-enrolled departments as comparison, aggregate-only data, a written analysis plan and a reproducible script repository.

> **Synthetic case.** Departments, data and agreements are synthetic.

### Errors and limits

A simple before-and-after comparison without a comparison group cannot separate the effect of passkeys from seasonal or organisation-wide trends.

### Exercises

- **EX015 — Comparison group.** What serves as the comparison group? *Rubric:* 3 = departments not yet enrolled, same calendar weeks;; 2 = not enrolled;; 1 = vague;; 0 = none.
- **EX016 — Small-group rule.** How are small departments handled? *Rubric:* 3 = merged if fewer than ten staff;; 2 = merged;; 1 = excluded;; 0 = none.
- **EX017 — Main comparison.** What is the main comparison in the analysis plan? *Rubric:* 3 = enrolled change minus not-yet-enrolled change in reset rate;; 2 = difference of changes;; 1 = before/after;; 0 = none.
- **EX018 — Falsifying result.** What result would count against the hypothesis? *Rubric:* 3 = similar reduction in both groups or lower sign-in success;; 2 = one;; 1 = vague;; 0 = none.
- **EX019 — Traceable numbers.** What makes a reported number reproducible here? *Rubric:* 3 = traceable to script and input, synthetic file published;; 2 = traceable;; 1 = vague;; 0 = none.
- **EX020 — Rollout changes.** How are changes to Halyard's rollout treated? *Rubric:* 3 = shared, recorded and included as data;; 2 = recorded;; 1 = hidden;; 0 = none.

### Synthesis

A staggered design, aggregate data, a written plan and reproducible scripts make a workplace study both ethical and credible.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Identity and access management: competing explanations

### Learning outcomes

You will (1) identify alternative explanations for a fall in resets; (2) normalise for headcount; (3) test each explanation against evidence.

### 4.1 Why alternatives matter

A fall in password resets after passkey enrolment could have other causes. Headcount changes alter raw counts. A new self-service reset portal launched at the same time would cut desk tickets regardless of passkeys. Holidays reduce sign-ins and therefore resets. Desk staff might categorise tickets differently after training. And the password expiry policy, if changed, would remove a common trigger for resets. Jonah lists every plausible alternative, then checks each against evidence, because a dissertation that claims a cause without ruling out rivals will not convince examiners or Halyard's managers.

### Lab — Normalised reset rate

```python
"""Normalise synthetic weekly password-reset tickets per 100 active staff, before and after passkey enrolment (stdlib only)."""
import statistics as st
before = [(41, 880), (38, 884), (44, 890), (40, 893), (39, 895), (43, 899)]
after = [(27, 930), (24, 936), (22, 941), (23, 946), (21, 950), (20, 955)]
rb = [100*t/s for t, s in before]; ra = [100*t/s for t, s in after]
print("before per100:", [f"{r:.2f}" for r in rb]); print("after  per100:", [f"{r:.2f}" for r in ra])
print(f"raw mean {st.mean(t for t,_ in before):.1f} -> {st.mean(t for t,_ in after):.1f}; rate mean {st.mean(rb):.2f} -> {st.mean(ra):.2f}; change {100*(st.mean(ra)/st.mean(rb)-1):.0f}%")
```

Run with `python3 lab_rate.py`. Verified output:

```text
before per100: ['4.66', '4.30', '4.94', '4.48', '4.36', '4.78']
after  per100: ['2.90', '2.56', '2.34', '2.43', '2.21', '2.09']
raw mean 40.8 -> 22.8; rate mean 4.59 -> 2.42; change -47%
```

### 4.2 Reading the normalised series

In the synthetic data, raw weekly resets fall from a mean of 40.8 to 22.8. But headcount also rose, from about 880 to 955 staff, so Jonah normalises: the rate per hundred staff falls from 4.59 to 2.42, a reduction of about 47 percent. Normalisation actually strengthens the finding here, since more staff would be expected to generate more resets. The weekly values are also stable within each period, with no single unusual week driving the change, which reduces the chance that one holiday or outage explains the result.

### 4.3 Testing other explanations

Jonah checks the alternatives one by one. Halyard's change calendar shows no self-service portal launch during the study. Password expiry policy was unchanged, having been removed years earlier in line with current NIST guidance. Ticket categories were checked by hand on a sample from each period and applied consistently. Holidays fell in both periods. Finally, not-yet-enrolled departments show only a small fall over the same weeks. With each rival explanation examined and found weak, passkey enrolment becomes the most plausible explanation, though Jonah still describes it as an association supported by a comparison design, not a proof.

### 4.4 Where risk moved

Jonah also checks whether work simply moved elsewhere. Recovery requests for lost or replaced devices rose from almost none to about three a week. Each takes longer than a password reset, because it needs a video identity check. He reports this honestly: the desk handles fewer requests in total, but each recovery is more involved. From a security view the shift is positive, since the recovery path is harder to abuse than a phone reset, but Halyard should plan desk capacity for recovery and encourage staff to register a second passkey to reduce lost-device cases.

### Worked example

Normalised reset rate falls 47 percent while headcount rises; rival explanations such as a portal launch, policy change and recategorisation are checked and found weak; recovery requests rise modestly.

> **Synthetic case.** Rates, headcount and calendar entries are synthetic.

### Errors and limits

Reporting raw counts when headcount changes can exaggerate or hide real effects.

### Exercises

- **EX021 — Rival list.** Name three rival explanations for fewer resets. *Rubric:* 3 = headcount, self-service portal, holidays, recategorisation, policy change (three);; 2 = two;; 1 = one;; 0 = none.
- **EX022 — Normalised means.** What are the normalised reset rates before and after? *Rubric:* 3 = 4.59 to 2.42 per hundred, about 47% fall;; 2 = both;; 1 = raw;; 0 = none.
- **EX023 — Headcount direction.** Why does normalisation strengthen the finding here? *Rubric:* 3 = headcount rose, which would increase resets;; 2 = headcount rose;; 1 = it weakens;; 0 = none.
- **EX024 — Portal check.** How was the self-service portal explanation tested? *Rubric:* 3 = change calendar showed no launch;; 2 = calendar;; 1 = assumed;; 0 = none.
- **EX025 — Recovery rise.** How did recovery requests change? *Rubric:* 3 = rose to about three a week, each more involved;; 2 = rose;; 1 = fell;; 0 = none.
- **EX026 — Second passkey advice.** What advice reduces lost-device recovery? *Rubric:* 3 = register a second passkey;; 2 = backup;; 1 = vague;; 0 = none.

### Synthesis

Normalising and testing rival explanations one by one turns a raw drop in tickets into a credible, bounded claim.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write and agree a proposal; (2) run a pilot in one department; (3) record and apply lessons.

### 5.1 Proposal

Jonah's proposal sets out the question, the literature gap, the staggered design, measures, analysis plan, data agreement, ethics approval, timeline and risks. Risks include delays to Halyard's rollout, missing log weeks and low interview participation, each with a planned response. Dr Solberg and Halyard's IT manager approve it before data collection begins. The proposal becomes the reference point for the rest of the project: any later change is compared with it, recorded with a reason and reported in the dissertation, so readers can see how the study evolved and why.

### 5.2 Pilot department

Before the full rollout, Halyard enrols one department of about forty staff, the claims team. Jonah uses this pilot to test his data pipeline rather than to estimate effects. He checks that weekly aggregates arrive on time, that ticket categories map correctly to his measures and that sign-in logs separate passkey and password attempts. He also interviews two desk staff about how enrolment questions reach them. The pilot is small enough that problems affect few people, yet real enough to reveal issues that synthetic testing missed.

### 5.3 Pilot findings

Three issues appear. Sign-in logs counted a cancelled passkey prompt as a failure, inflating failures; the identity team adds a separate outcome code. Some reset tickets were logged as general access issues, so desk staff agree a clearer category. And several staff enrolled only on a laptop, then could not sign in on a shared terminal in the claims office. Halyard responds by offering a hardware security key for shared terminals. Jonah records each issue with evidence and the fix, and notes which fixes change his measures.

### 5.4 Applying lessons

Lessons from the pilot are applied before the main rollout. The new outcome code means sign-in success must be defined again, so Jonah updates the data dictionary and reruns the pilot numbers under both definitions to show the effect of the change. The ticket category change applies to all departments from the same date, so it does not favour one group. The security key option becomes part of standard enrolment. Each change is recorded against the proposal, ensuring that the main study begins with a cleaner pipeline and a documented history of why it differs.

### Worked example

The pilot in the claims team reveals cancelled prompts counted as failures, inconsistent ticket categories and shared-terminal problems; fixes are applied before the main rollout and recorded against the proposal.

> **Synthetic case.** The claims team, issues and fixes are synthetic.

### Errors and limits

Treating pilot results as the main finding mistakes a pipeline test for an effect estimate.

### Exercises

- **EX027 — Proposal risks.** Name two risks listed in the proposal. *Rubric:* 3 = rollout delay, missing log weeks, low interview participation (two);; 2 = one;; 1 = vague;; 0 = none.
- **EX028 — Pilot aim.** What is the pilot mainly testing? *Rubric:* 3 = the data pipeline, not the effect;; 2 = pipeline;; 1 = effect;; 0 = none.
- **EX029 — Cancelled prompts.** How were cancelled passkey prompts mishandled? *Rubric:* 3 = counted as failures, inflating failure rate;; 2 = failures;; 1 = ignored;; 0 = none.
- **EX030 — Shared terminal fix.** What fixed the shared-terminal problem? *Rubric:* 3 = hardware security keys offered;; 2 = security key;; 1 = passwords;; 0 = none.
- **EX031 — Definition change.** How does Jonah handle the changed success definition? *Rubric:* 3 = update dictionary, rerun pilot under both definitions;; 2 = update;; 1 = ignore;; 0 = none.
- **EX032 — Category fairness.** Why apply the ticket category change to all departments at once? *Rubric:* 3 = avoids favouring one group;; 2 = fairness;; 1 = speed;; 0 = none.

### Synthesis

A clear proposal and a small pilot reveal pipeline and practical problems early, and recording fixes keeps the study honest.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) collect aggregate data across the rollout; (2) estimate sign-in success with intervals; (3) examine the cases where passkeys failed.

### 6.1 Collecting data

Over three months, Halyard enrols seven departments in turn. Each week, the identity team exports aggregates: sign-in attempts and successes by method and department, reset and recovery tickets, and headcount. Jonah checks every file on arrival for completeness, comparing totals with the previous week and flagging gaps. Two weeks of one department's data are missing after a log storage fault; he records the gap and handles it as his analysis plan specified, by excluding those weeks from both groups rather than estimating values that were never measured.

### Lab — Sign-in success

```python
"""Sign-in success rate with a Wilson 95% interval for synthetic pilot and rollout groups (stdlib only)."""
import math
def wilson(k, n, z=1.96):
    p = k/n; c = (p + z*z/(2*n)) / (1 + z*z/n); h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / (1 + z*z/n)
    return p, c-h, c+h
for name, k, n in [("password+OTP", 9412, 9640), ("passkey", 9581, 9655)]:
    p, lo, hi = wilson(k, n); print(f"{name:13} success={k}/{n} rate={p:.3f} 95%CI=({lo:.3f}, {hi:.3f}) fails={n-k}")
```

Run with `python3 lab_success.py`. Verified output:

```text
password+OTP  success=9412/9640 rate=0.976 95%CI=(0.973, 0.979) fails=228
passkey       success=9581/9655 rate=0.992 95%CI=(0.990, 0.994) fails=74
```

### 6.2 Reading the result

In the synthetic data, password plus one-time code sign-ins succeed 97.6 percent of the time, with a 95 percent interval of 97.3 to 97.9, while passkey sign-ins succeed 99.2 percent, interval 99.0 to 99.4. The intervals do not overlap, so passkeys are very likely more reliable for these staff. Failures fall from 228 to 74 in similar numbers of attempts. Jonah uses Wilson intervals because they behave well when rates are close to one. He reports the counts beside the percentages, so readers can judge the precision for themselves.

### 6.3 Examining the failures

The seventy-four passkey failures deserve attention. Jonah groups them by cause using the outcome codes: most are biometric retries that exceed a limit, some are devices without a registered passkey being used for the first time, and a handful are on an older browser that does not support the standard. None involves an attacker. Each cause suggests a fix: guidance on registering more than one device and a browser upgrade for the remaining machines. Examining failures turns an aggregate rate into practical improvements that Halyard can act on.

### 6.4 The difference-in-differences

The main analysis compares changes. In enrolled departments, the reset rate falls by about 2.2 per hundred staff per week; in not-yet-enrolled departments over the same weeks it falls by about 0.2. The difference, about 2.0, is Jonah's estimate of the effect attributable to passkeys, under the assumption that both groups would otherwise have followed similar trends. He checks that assumption by comparing their trends before any enrolment and finds them close. He reports the estimate with an interval and states the assumption openly.

### Worked example

Passkey sign-in success is 99.2 percent against 97.6 percent for password plus code, with non-overlapping intervals; failures are grouped by cause and the difference-in-differences estimate is about 2.0 fewer resets per hundred staff per week.

> **Synthetic case.** Departments, logs and results are synthetic.

### Errors and limits

Filling missing weeks with guessed values hides the gap and can bias both groups.

### Exercises

- **EX033 — Success rates.** What are the two sign-in success rates and intervals? *Rubric:* 3 = 97.6% (97.3–97.9) and 99.2% (99.0–99.4);; 2 = rates;; 1 = one;; 0 = none.
- **EX034 — Failure counts.** How many failures does each method have in the lab? *Rubric:* 3 = 228 and 74;; 2 = both;; 1 = one;; 0 = none.
- **EX035 — Wilson choice.** Why use Wilson intervals here? *Rubric:* 3 = they behave well for rates near one;; 2 = near 1;; 1 = simpler;; 0 = none.
- **EX036 — Missing weeks.** How are the two missing weeks handled? *Rubric:* 3 = excluded from both groups per plan, not imputed;; 2 = excluded;; 1 = estimated;; 0 = none.
- **EX037 — Failure causes.** Name two causes of passkey failures. *Rubric:* 3 = biometric retry limit, unregistered device, old browser (two);; 2 = one;; 1 = attacker;; 0 = none.
- **EX038 — DiD estimate.** What is the difference-in-differences estimate? *Rubric:* 3 = about 2.0 fewer resets per hundred staff per week;; 2 = 2.0;; 1 = 2.2;; 0 = none.

### Synthesis

Careful collection, intervals around rates, cause analysis of failures and a comparison of changes give an honest picture of the effect.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure the dissertation; (2) state limitations honestly; (3) write recommendations and a practitioner summary.

### 7.1 Structure

Jonah structures the dissertation as introduction and question, literature review, method, results, discussion, limitations and recommendations. Each chapter opens by stating its purpose and ends by linking to the next, so the argument flows from question to evidence to conclusion. Tables carry the key numbers, with the script that produced each named in a note. He writes the method chapter first, while details are fresh, and the introduction last, once he knows exactly what the dissertation shows. Clear signposting helps examiners follow the argument and helps busy readers find what they need.

### 7.2 Limitations

Jonah states his limitations plainly. The study covers one organisation over three months, so long-term effects, such as whether recovery requests keep rising, are unknown. Department order was not randomised. Aggregate data cannot show individual experiences, such as whether some staff struggled repeatedly. Ticket categories depend on desk staff judgement, though sampling found them consistent. For each limitation he explains its likely effect on the results and how future work could address it, which shows examiners that he understands the boundaries of his evidence rather than overselling it.

### 7.3 Recommendations

Recommendations follow directly from the evidence. Continue passkey enrolment, since it reduced resets and improved sign-in success. Encourage every staff member to register a second passkey or security key, reducing lost-device recovery. Keep the strong identity check for recovery, because the recovery path is now the more attractive target. Upgrade the remaining old browsers. And keep measuring resets, recovery and sign-in success monthly. Each recommendation names its cost, an owner and how success will be measured, so Halyard can act on it rather than file it away.

### 7.4 Writing for practitioners

Jonah also writes a two-page summary for Halyard's managers and desk staff. It explains in plain language what passkeys are, what changed, the main numbers, the shift towards recovery and the recommended next steps, with one simple chart of the reset rate. Technical details and statistical methods stay in the dissertation. The summary is reviewed by a desk team leader for clarity. Practitioners make the decisions that turn research into practice, so writing for them is as important as writing for examiners.

### Worked example

Jonah writes a signposted dissertation with honest limitations, five evidence-based recommendations with owners, and a two-page practitioner summary reviewed by a desk team leader.

> **Synthetic case.** The dissertation, recommendations and reviewers are synthetic.

### Errors and limits

Hiding limitations to make results look stronger undermines trust when examiners find them anyway.

### Exercises

- **EX039 — Chapter order.** List the dissertation's main chapters in order. *Rubric:* 3 = introduction, literature, method, results, discussion, limitations, recommendations;; 2 = most;; 1 = few;; 0 = none.
- **EX040 — Writing order.** Which chapters are written first and last? *Rubric:* 3 = method first, introduction last;; 2 = one;; 1 = vague;; 0 = none.
- **EX041 — Long-term gap.** Which long-term question remains unknown? *Rubric:* 3 = whether recovery requests keep rising;; 2 = long-term effects;; 1 = vague;; 0 = none.
- **EX042 — Recovery recommendation.** Why keep the strong recovery check? *Rubric:* 3 = recovery is now the more attractive target;; 2 = target;; 1 = cost;; 0 = none.
- **EX043 — Recommendation parts.** What does each recommendation name? *Rubric:* 3 = cost, owner and success measure;; 2 = two;; 1 = one;; 0 = none.
- **EX044 — Summary reviewer.** Who reviews the practitioner summary? *Rubric:* 3 = a desk team leader, for clarity;; 2 = desk lead;; 1 = examiner;; 0 = none.

### Synthesis

Clear structure, honest limitations and practical recommendations make research useful to both examiners and practitioners.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) obtain an independent review; (2) prepare for the viva; (3) close the project responsibly.

### 8.1 Independent review

Before submission, a reviewer from another research group, who was not involved in the study, reads the dissertation and checks whether conclusions follow from evidence. She questions whether the difference-in-differences assumption holds for the last departments enrolled, which had shorter comparison periods. Jonah records every comment and his response, adds a sensitivity analysis excluding those departments and finds the estimate similar with a wider interval. Independent review catches blind spots that close involvement makes hard to see, and prepares the candidate for the questions examiners are likely to ask.

### 8.2 Viva preparation

Jonah rereads the dissertation and lists likely viva questions: why passkeys rather than another method, why aggregates, how the comparison group was chosen, what the recovery rise means, and what he would do differently. For each he notes the page and evidence. He practises summarising his contribution in three sentences. A mock viva with two colleagues helps him answer concisely and admit uncertainty where it exists. Examiners respect a candidate who knows the limits of the evidence more than one who claims too much.

### 8.3 The viva

In the viva, Jonah listens to each question fully, answers what was asked and refers to specific tables and pages. When asked whether the result would hold in a hospital with shared terminals, he explains what his pilot found about shared terminals and why the effect might be smaller there, without overclaiming. He notes the corrections requested, a clearer explanation of the trend assumption and one extra reference, and agrees a date for submission. Calm, evidence-based answers show he understands both the strengths and the boundaries of his work.

### 8.4 Closing the project

After corrections, Jonah submits the final dissertation and closes the partnership. He sends Halyard the practitioner summary and a short briefing for the desk team. University-held aggregate data is deleted on the agreed date, and deletion is confirmed in writing. The scripts and synthetic data remain public. He thanks the desk staff who took part in interviews. Finally, he considers a short paper with Halyard's agreement, so other organisations planning passkey rollouts can learn from the measured effects, including the shift towards recovery.

### Worked example

An independent reviewer prompts a sensitivity analysis; Jonah prepares and passes the viva with minor corrections, then closes the project with confirmed deletion and practitioner briefings.

> **Synthetic case.** Reviewer, examiners and outcomes are synthetic.

### Errors and limits

Skipping independent review leaves unexamined assumptions for examiners to find.

### Exercises

- **EX045 — Reviewer concern.** What did the independent reviewer question? *Rubric:* 3 = DiD assumption for late departments with short comparison periods;; 2 = assumption;; 1 = vague;; 0 = none.
- **EX046 — Sensitivity outcome.** What did excluding late departments show? *Rubric:* 3 = similar estimate, wider interval;; 2 = similar;; 1 = reversed;; 0 = none.
- **EX047 — Contribution summary.** How many sentences does Jonah practise for his contribution? *Rubric:* 3 = three;; 2 = few;; 1 = one;; 0 = none.
- **EX048 — Hospital question.** How does Jonah answer the hospital question? *Rubric:* 3 = cites shared-terminal pilot findings, effect may be smaller, no overclaim;; 2 = cautious;; 1 = yes;; 0 = none.
- **EX049 — Corrections requested.** What corrections were requested? *Rubric:* 3 = clearer trend assumption, one extra reference;; 2 = one;; 1 = vague;; 0 = none.
- **EX050 — Data closure.** What happens to university-held data at the end? *Rubric:* 3 = deleted on agreed date, confirmed in writing;; 2 = deleted;; 1 = published;; 0 = none.

### Synthesis

Independent review, careful preparation and a responsible close complete a master's study well.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Jonah Reyes, Dr Ingrid Solberg, Marlow Bay University, Halyard Insurance and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A convincing caller can trick the desk into resetting someone else's account.

**EX002.** The W3C Web Authentication (WebAuthn) standard.

**EX003.** The search string, the date and the number of results.

**EX004.** Six of twelve (11 after date, 9 after evidence type, 6 workplace).

**EX005.** They studied web users or students rather than workplaces.

**EX006.** Because headcount changes, raw counts would mislead.

**EX007.** By hand-checking a sample of tickets to confirm categories are applied consistently.

**EX008.** How confident the system can be that the person signing in controls the authenticator bound to the account.

**EX009.** A user can be tricked into typing them into a fake site, which relays them.

**EX010.** On the user's device or security key; the site holds only the public key.

**EX011.** A look-alike site receiving anything usable at the real site.

**EX012.** Because applications trust the provider, it strengthens sign-in everywhere at once.

**EX013.** No scheme dominated passwords across usability, deployability and security.

**EX014.** Because risk and workload may move from password resets into recovery.

**EX015.** Departments not yet enrolled, over the same calendar weeks.

**EX016.** Departments with fewer than ten staff are merged to protect individuals.

**EX017.** The change in reset rate for enrolled departments minus the change for not-yet-enrolled ones.

**EX018.** A similar reset fall in both groups, or a fall in sign-in success.

**EX019.** Each number can be traced to the script and input that produced it.

**EX020.** They are shared with Jonah, recorded and treated as part of the data.

**EX021.** Headcount changes, a self-service portal and holidays (also recategorisation or policy change).

**EX022.** 4.59 to 2.42 per hundred staff, about a 47 percent fall.

**EX023.** Headcount rose, which would be expected to increase resets, yet the rate fell.

**EX024.** Halyard's change calendar showed no portal launch during the study.

**EX025.** They rose from almost none to about three a week, each needing a video identity check.

**EX026.** Encourage staff to register a second passkey.

**EX027.** Rollout delays and missing log weeks (also low interview participation).

**EX028.** The data pipeline and practical issues, not the size of the effect.

**EX029.** They were counted as sign-in failures, inflating the failure rate.

**EX030.** Offering hardware security keys for shared terminals.

**EX031.** He updates the data dictionary and reruns pilot numbers under both definitions.

**EX032.** So the change does not favour enrolled or not-yet-enrolled departments.

**EX033.** Password plus code 97.6% (97.3–97.9); passkey 99.2% (99.0–99.4).

**EX034.** 228 for password plus code and 74 for passkeys.

**EX035.** They behave well when rates are close to one.

**EX036.** Excluded from both groups as the plan specified, not estimated.

**EX037.** Biometric retry limits and unregistered devices (also an old browser).

**EX038.** About 2.0 fewer resets per hundred staff per week.

**EX039.** Introduction, literature, method, results, discussion, limitations and recommendations.

**EX040.** Method first, introduction last.

**EX041.** Whether recovery requests keep rising beyond three months.

**EX042.** Because the recovery path has become the more attractive target for attackers.

**EX043.** Its cost, an owner and how success will be measured.

**EX044.** A service desk team leader, for clarity.

**EX045.** Whether the trend assumption held for late-enrolled departments with short comparison periods.

**EX046.** A similar estimate with a wider interval.

**EX047.** Three sentences.

**EX048.** He cites the shared-terminal pilot findings and says the effect may be smaller, without overclaiming.

**EX049.** A clearer explanation of the trend assumption and one extra reference.

**EX050.** It is deleted on the agreed date, with deletion confirmed in writing.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Bonneau, J., Herley, C., van Oorschot, P. C., & Stajano, F. (2012). The quest to replace passwords: A framework for comparative evaluation of web authentication schemes. *2012 IEEE Symposium on Security and Privacy*, 553–567. <https://doi.org/10.1109/SP.2012.44>
- Ferraiolo, D. F., Sandhu, R., Gavrila, S., Kuhn, D. R., & Chandramouli, R. (2001). Proposed NIST standard for role-based access control. *ACM Transactions on Information and System Security*, 4(3), 224–274. <https://doi.org/10.1145/501978.501980>
- Florêncio, D., & Herley, C. (2007). A large-scale study of web password habits. *Proceedings of the 16th International Conference on World Wide Web*, 657–666. <https://doi.org/10.1145/1242572.1242661>
- Hardt, D. (Ed.). (2012). *The OAuth 2.0 authorization framework* (RFC 6749). IETF. <https://www.rfc-editor.org/rfc/rfc6749>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- Hu, V. C., Ferraiolo, D., Kuhn, R., Schnitzer, A., Sandlin, K., Miller, R., & Scarfone, K. (2014). *Guide to attribute based access control (ABAC) definition and considerations* (NIST SP 800-162). NIST. <https://doi.org/10.6028/NIST.SP.800-162>
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
