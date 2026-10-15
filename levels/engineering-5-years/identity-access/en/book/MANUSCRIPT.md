# Identity and Access Management: Engineering Degree

- Language: English (`en`); course 125, Engineering degree (5 years).
- Editorial state: **published**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; Seven offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students and practitioners designing, implementing and verifying identity and access management for real organisations.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only identity systems and accounts you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic accounts, entitlements, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one engineering student replacing a borough council's fragmented local accounts with a central identity provider, from foundations in mathematics, hardware and programming through requirements, data models, threat analysis, architecture alternatives, control design, phased implementation, measurement, reliability, operations, validation, verification, an applied review study, a capstone, a failure trial, an evidence dossier, thesis and defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Sana Malik** | Engineering student | Invented |
| **Dr Owen Hale** | Supervisor | Invented |
| **Brackenford Institute of Technology** | Fictional institute | Invented |
| **Linmouth Borough Council** | Fictional partner (2,400 staff) | Invented |

### Core sources

NIST [SP 800-63-4](https://doi.org/10.6028/NIST.SP.800-63-4), [SP 800-63B-4](https://doi.org/10.6028/NIST.SP.800-63B-4), [SP 800-162](https://doi.org/10.6028/NIST.SP.800-162), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); IETF [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749) and [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700); [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html); W3C [WebAuthn Level 2](https://www.w3.org/TR/webauthn-2/); OASIS [SAML 2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf). Full list in [References](#references).

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

You will (1) use rates of change to describe sign-in load; (2) relate derivatives to capacity; (3) estimate peaks from smooth curves.

### 1.1 The case

Sana Malik is a five-year engineering student at the fictional Brackenford Institute of Technology, supervised by Dr Owen Hale. Her long project is with the fictional Linmouth Borough Council, whose 2,400 staff use about 140 applications, most with their own local accounts and passwords. Nobody removes accounts reliably when people leave, and auditors found former staff still able to sign in to several systems. The council wants a central identity provider with single sign-on, multi-factor authentication, role-based access and automated joiner, mover and leaver processes. This book follows Sana from foundations to a defended engineering thesis.

### 1.2 Rates of sign-in

Identity systems handle quantities that change over time: sign-in requests, token issuances and password checks. If the cumulative count of sign-ins during a morning is a smooth curve, its derivative is the sign-in rate at each moment. At Linmouth, the curve rises steeply between 08:30 and 09:00 as staff arrive. The slope at its steepest point tells Sana the peak rate the identity provider must handle, which matters far more for capacity than the daily total, because a provider that copes on average can still fail at the morning rush.

### 1.3 Derivatives and capacity

If the identity provider can process a fixed number of sign-ins per second, any period where the arrival rate exceeds that capacity creates a backlog. The backlog grows at a rate equal to the difference between arrivals and capacity, which is itself a derivative. When the rush ends, the backlog drains. Sana uses this reasoning to explain why staff experience slow sign-in for a few minutes each morning even though the system is idle most of the day, and why capacity planning must start from peak rates, not averages.

### 1.4 Why this matters for security

Capacity is a security property as well as a performance one. If sign-in slows badly, staff and administrators look for shortcuts, such as shared accounts or disabling multi-factor prompts. A provider that fails under load also blocks access to every federated application at once. Understanding rates lets Sana size the system so that strong controls remain usable at peak. It also helps her recognise abnormal patterns, such as a sudden rise in failed sign-ins at night, which can indicate password-guessing attempts that monitoring should flag for review.

### Worked example

Sana estimates the steepest slope of a synthetic cumulative sign-in curve at about 14 sign-ins per second between 08:40 and 08:50, and sizes the identity provider for at least twice that.

> **Synthetic case.** Sana Malik, Brackenford Institute of Technology, Linmouth Borough Council and all figures are synthetic.

### Errors and limits

Sizing an identity provider from daily averages ignores the morning peak, when failure would block every application at once.

### Exercises

- **EX001 — Peak rate.** Why does peak rate matter more than the daily total for sizing? *Rubric:* 3 = provider must cope at the rush or block all apps;; 2 = peak;; 1 = total;; 0 = none.
- **EX002 — Backlog growth.** At what rate does a sign-in backlog grow? *Rubric:* 3 = arrivals minus capacity;; 2 = difference;; 1 = capacity;; 0 = none.
- **EX003 — Night failures.** What might a sudden night-time rise in failed sign-ins indicate? *Rubric:* 3 = password-guessing attempts to flag;; 2 = attack;; 1 = vague;; 0 = none.

### Synthesis

Rates and derivatives turn sign-in curves into capacity requirements that keep strong controls usable at peak.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) model users, roles and permissions as sets and relations; (2) compose relations to find effective access; (3) count combinations that drive role growth.

### 2.1 Sets and relations

Access control is naturally described with sets. Users, roles and permissions are sets; assignments are relations between them. The user-to-role relation says who holds which role, and the role-to-permission relation says what each role grants. Composing them gives the user-to-permission relation: everything each person can actually do. Sandhu and colleagues (1996) built role-based access control models on exactly this structure. Writing access in this way lets Sana ask precise questions, such as which users can approve payments, rather than relying on the impression given by role names.

### 2.2 Composition and effective access

Effective access is often larger than anyone intended, because roles overlap. A person holding both a finance clerk role and a temporary project role may gain a permission that neither role was meant to provide in combination. By composing relations, Sana computes every user's effective permissions and compares them with what their job requires. The difference, permissions held but not needed, is excess access. Set difference is a simple operation, but applying it consistently across thousands of users reveals problems that manual review of role names would never find.

### 2.3 Counting and role explosion

With n permissions there are two to the power n possible permission sets. Even with thirty permissions, that is over a billion combinations. Organisations that create a new role whenever someone needs a slightly different set drift towards role explosion, with hundreds of roles that differ by one or two permissions. Counting shows why role design needs principles, such as roles based on job functions plus a small number of well-governed exceptions, rather than a role for every case. Linmouth's existing applications already show this pattern.

### 2.4 Partial orders and hierarchies

Role hierarchies let a senior role inherit the permissions of junior ones, forming a partial order. A finance manager role might inherit everything from finance clerk and add approval rights. Hierarchies reduce duplication, but inheritance also spreads permissions silently: adding a permission to a junior role grants it to every role above. Sana draws the hierarchy as a directed graph and checks that inheritance flows only in intended directions, and that no cycle exists, since a cycle would make two roles equivalent and confuse every later review.

### Worked example

For users {u1, u2}, roles {clerk, project} and permissions {raise, approve, view}, Sana composes assignments to show that u2, holding both roles, can raise and approve payments, a combination neither role intended alone.

> **Synthetic case.** Users, roles and permissions are synthetic.

### Errors and limits

Reviewing role names instead of computing effective permissions misses combinations that arise from overlapping roles.

### Exercises

- **EX004 — Effective access.** How is each user's effective access computed? *Rubric:* 3 = compose user-role with role-permission relations;; 2 = compose;; 1 = list roles;; 0 = none.
- **EX005 — Permission sets count.** How many possible permission sets exist with thirty permissions? *Rubric:* 3 = 2^30, over a billion;; 2 = 2^30;; 1 = 30;; 0 = none.
- **EX006 — Hierarchy cycle.** Why must a role hierarchy contain no cycle? *Rubric:* 3 = cycle makes roles equivalent and confuses review;; 2 = equivalence;; 1 = speed;; 0 = none.

### Synthesis

Sets, relations and counting make access precise, expose excess and explain why roles must follow principles.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical properties to authenticators; (2) explain why device-bound keys resist copying; (3) consider environmental limits on hardware.

### 3.1 Authenticators as physical objects

Many authenticators are physical: smart cards, security keys and phones with secure hardware. Their security rests partly on physics. A private key stored in a secure element is designed so that it cannot be read out through normal interfaces, and extracting it requires specialised equipment and time. NIST SP 800-63B-4 distinguishes authenticators by such properties, including whether a key can be exported. For Sana, the physical nature of authenticators means they can be lost, damaged or left at home, which the council's processes must handle as carefully as the cryptography itself.

### 3.2 Radio and proximity

Some authenticators communicate over short-range radio, such as near-field communication on staff badges or Bluetooth between a phone and a laptop. Signal strength falls rapidly with distance, which is why these methods require the device to be close. Proximity is useful: it suggests the person holding the device is physically present. But it is not proof, so designs should not treat a nearby signal as a substitute for user verification such as a PIN or fingerprint. Sana notes which council devices use radio and what each assumes about proximity.

### 3.3 Biometric sensing

Fingerprint and face sensors convert physical features into measurements and compare them with a stored template. Measurements vary with dirt, light, injury and age, so sensors accept matches within a tolerance. That tolerance creates two error rates: wrongly rejecting the right person and wrongly accepting someone else. In passkeys and device unlock, the biometric only unlocks a local key and never leaves the device. Sana explains this to council staff who worry that their fingerprints would be stored centrally, which is not how such systems are designed.

### 3.4 Environment and hardware life

Physical devices age and fail. Smart card readers wear out, security keys break when dropped and phone batteries die at the end of a shift. In cold depots, some touch sensors respond poorly to gloved hands. Sana lists the council's working environments, from offices to waste depots, and checks that each has an authenticator that works there, with a fallback that is still strong. Planning for physical conditions prevents staff from abandoning secure methods because they simply do not work where they need to sign in.

### Worked example

Sana maps four council environments to suitable authenticators: offices to passkeys on laptops, depots to security keys usable with gloves, reception to smart cards, and mobile staff to phone-based passkeys.

> **Synthetic case.** Environments and devices are synthetic.

### Errors and limits

Treating a nearby radio signal as proof of presence confuses proximity with verification.

### Exercises

- **EX007 — Secure element value.** Why does a secure element make key copying hard? *Rubric:* 3 = key cannot be read out through normal interfaces;; 2 = not exportable;; 1 = encryption;; 0 = none.
- **EX008 — Biometric errors.** Which two error rates does a biometric tolerance create? *Rubric:* 3 = false rejection and false acceptance;; 2 = two;; 1 = one;; 0 = none.
- **EX009 — Depot authenticator.** Which authenticator suits gloved depot staff in Sana's mapping? *Rubric:* 3 = security keys usable with gloves;; 2 = keys;; 1 = fingerprint;; 0 = none.

### Synthesis

Physical properties shape how authenticators protect keys, how they fail and where they can be used.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small scripts that read account lists; (2) compare sets of accounts; (3) produce clear, repeatable reports.

### 4.1 Why program

Comparing account lists by eye works for ten accounts but not for thousands across 140 applications. A short program reads each list, compares it with the HR record of current staff and reports accounts with no matching employee. It does the same check identically every time, and its output can be saved as evidence. Sana writes her first scripts in Python using only the standard library, so they run on any council machine without installing extra packages, which the council's change rules would otherwise require approval for.

### Lab — Leaver accounts

```python
"""Compare a synthetic HR staff list with an application's active accounts (stdlib only)."""
hr = {"aali", "bchen", "cdiaz", "dfox", "egray", "fhill", "gking", "mlee"}
app = ["aali", "BChen", "cdiaz ", "dfox", "egray", "fhill", "gking", "jdoe", "kpatel"]
norm = {a.strip().lower() for a in app}
print("active accounts:", len(norm), " current staff:", len(hr))
print("no current employee:", sorted(norm - hr))
print("employee without account:", sorted(hr - norm))
```

Run with `python3 lab_leavers.py`. Verified output:

```text
active accounts: 9  current staff: 8
no current employee: ['jdoe', 'kpatel']
employee without account: ['mlee']
```

### 4.2 Reading the output

The synthetic HR list contains eight current staff, and the application export contains nine active accounts. The script finds two accounts, jdoe and kpatel, with no matching current employee: likely leavers whose access was never removed. It also finds one employee, mlee, without an account, who may be new and still waiting. Sana does not disable anything herself; she reports the findings to the application owner, who checks each case, because a script can only show a mismatch, not explain it, and some mismatches have innocent causes such as name changes.

### 4.3 Structuring a script

Sana structures each script in three parts: reading inputs, computing results and printing a report. Each part is a small function with a clear name. Inputs are read from files named at the top, so the same script works on any export with the same format. Keeping computation separate from reading and printing makes it easy to test with small examples. This simple structure means a colleague can understand and rerun the script months later, when Sana has moved on to other parts of the project.

### 4.4 Testing

A test gives a function a small, known input and checks the output against an answer worked out by hand. For the leaver check, Sana tests an exact match, a case difference in usernames, an account with trailing spaces and an empty list. The case and spacing tests reveal that her first version treated JDoe and jdoe as different people. Fixing that before running the script on real exports prevents false alarms that would waste application owners' time and reduce their trust in the results.

### Worked example

The leaver script reports two active accounts with no current employee (jdoe, kpatel) and one employee without an account (mlee); owners confirm the first two are leavers.

> **Synthetic case.** Accounts and staff are synthetic.

### Errors and limits

Disabling accounts directly from a script's output, without owner checks, risks locking out staff whose records differ for innocent reasons.

### Exercises

- **EX010 — Orphan count.** Which accounts does the lab flag as having no current employee? *Rubric:* 3 = jdoe and kpatel;; 2 = two;; 1 = vague;; 0 = none.
- **EX011 — Missing account.** Which employee has no account in the lab? *Rubric:* 3 = mlee;; 2 = one;; 1 = vague;; 0 = none.
- **EX012 — Case bug.** What did the case test reveal? *Rubric:* 3 = JDoe and jdoe treated as different;; 2 = case;; 1 = vague;; 0 = none.

### Synthesis

Small, tested scripts make account comparisons repeatable and trustworthy across many applications.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write for different audiences; (2) draw identity architecture diagrams; (3) explain trade-offs in plain language.

### 5.1 Audiences

Different readers need different things from the same identity design. Council directors want risk, cost and disruption in plain terms; service desk staff need to know what changes for callers; application owners need integration steps; auditors want evidence that controls exist and are checked. Sana prepares a one-page summary for directors, a technical design for engineers, a short guide for the service desk and an evidence register for auditors. Writing one document for everyone would serve none of them well.

### 5.2 Diagrams

A good identity diagram shows users, the identity provider, applications and the trust relationships between them, with arrows for sign-in flows and labels for protocols such as SAML or OpenID Connect. It omits detail that does not help the reader's decision. Sana dates every diagram and keeps it with the design, so nobody trusts an outdated picture. She draws separate views for staff sign-in, administrator access and account lifecycle, because combining all three in one picture makes each harder to understand.

### 5.3 Trade-off tables

Choices such as which authenticator to use for depot staff involve trade-offs. Sana uses a table with options as rows and criteria as columns: security, cost, usability in the environment, support effort and resilience when a device is lost. Each cell has a short score and evidence. Readers can disagree with a specific cell rather than the whole recommendation, which makes discussions faster and fairer, and the table records why a choice was made for whoever maintains the system later.

### 5.4 Plain language

Instead of writing that the council will implement federated authentication with phishing-resistant authenticators, Sana writes that staff will sign in once each morning with a security key or their phone, and that fake sign-in pages will no longer be able to steal their access. She defines any necessary technical term at first use. She tests drafts on a colleague outside IT and rewrites anything they misread, because directors who misunderstand a design may refuse to fund it, however good it is.

### Worked example

Sana produces four documents from one design: a one-page director summary, a technical design, a service desk guide and an auditor evidence register.

> **Synthetic case.** Documents and readers are synthetic.

### Errors and limits

Writing one long technical document for all audiences leaves directors confused and auditors without evidence.

### Exercises

- **EX013 — Four documents.** Name Sana's four documents. *Rubric:* 3 = director summary, technical design, desk guide, evidence register;; 2 = three;; 1 = one;; 0 = none.
- **EX014 — Separate views.** Which three diagram views does Sana draw? *Rubric:* 3 = staff sign-in, administrator access, account lifecycle;; 2 = two;; 1 = one;; 0 = none.
- **EX015 — Plain rewrite.** How does Sana test plain-language drafts? *Rubric:* 3 = ask a colleague outside IT and rewrite misread parts;; 2 = test reader;; 1 = spellcheck;; 0 = none.

### Synthesis

Tailored documents, focused diagrams, trade-off tables and plain language get identity designs understood and approved.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) compute totals from rates; (2) model growth of accounts and logs; (3) estimate storage for audit records.

### 6.1 Totals from rates

If the identity provider records audit events at a known rate, the total stored over a period is the integral of that rate. When the rate varies through the day, the area under the curve gives the daily total. Sana uses this to estimate log storage: if events average 30 per second during working hours and 3 per second at night, she integrates the piecewise rate to find about 1.1 million events per day, assuming nine working hours. Multiplying by average record size gives storage needed before any compression.

### 6.2 Growth models

Some quantities grow in proportion to their size. If the number of cloud applications connected to the identity provider grows by five percent a month, the growth is exponential and doubles in about fourteen months. A straight-line forecast would underestimate future load. Other quantities decay: the share of staff still using old one-time-code methods may halve every few months during a passkey rollout. Choosing the right model, and checking it against measurements, prevents both overspending on capacity and running out unexpectedly.

### 6.3 Retention estimates

Audit records must be kept long enough to support investigations, which often start weeks after events. Sana multiplies daily volume by the retention period required by council policy, adds headroom for growth and for incident periods, when logging often increases, and estimates compressed storage. The required period comes from policy and legal duties, not from what fits on an existing disk. She documents each assumption so the estimate can be updated when real volumes are measured after rollout. Retention for each record type is reviewed annually.

### 6.4 Checking with data

Models are only useful if they match reality. During a pilot, Sana compares predicted log volume with measured volume. If measured volume is double the estimate, she traces which assumption was wrong, such as events per sign-in or record size, and corrects it. Recording each assumption separately makes this tracing straightforward. The corrected model then becomes the basis for the full design, which is far safer than discovering a shortfall when the storage fills during an investigation. The pilot thus validates both the model and the method.

### Worked example

Integrating a piecewise event rate gives about 1.1 million audit events per day; at 500 bytes each, a year's retention needs roughly 210 gigabytes before compression.

> **Synthetic case.** Rates, sizes and policies are synthetic.

### Errors and limits

Linear forecasts of exponential growth underestimate future identity provider load.

### Exercises

- **EX016 — Area meaning.** What does the area under an event-rate curve represent? *Rubric:* 3 = total events over the period;; 2 = total;; 1 = peak;; 0 = none.
- **EX017 — Doubling time.** At five percent monthly growth, roughly when does load double? *Rubric:* 3 = about fourteen months;; 2 = about a year;; 1 = five months;; 0 = none.
- **EX018 — Retention source.** Where should the required retention period come from? *Rubric:* 3 = policy and legal duties, not disk size;; 2 = policy;; 1 = disk;; 0 = none.

### Synthesis

Integrals turn rates into totals, and checked growth models keep capacity and retention plans realistic.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) model random events such as lockouts; (2) summarise sign-in times with medians and percentiles; (3) reason about rare events.

### 7.1 Random events

Account lockouts, forgotten security keys and authentication errors occur at random times but at fairly stable average rates. Modelling them as random events with a known rate lets Sana estimate, for example, how many lockouts the service desk should expect on a Monday morning. A Poisson model, which describes counts of independent events in a fixed period, is a reasonable first approximation. She checks the model against desk records, since events that cluster, such as many lockouts after a password policy change, break the independence assumption.

### 7.2 Summarising sign-in times

Sign-in duration varies. The mean can be pulled up by a few very slow sign-ins, so Sana reports the median as the typical experience and the 95th percentile to show how slow the worst common cases are. If the median is two seconds but the 95th percentile is twelve, one in twenty sign-ins is frustrating, which users will notice and complain about. She always reports the number of samples and the period, so readers can judge whether the summary reflects normal conditions or an unusual week.

### 7.3 Rare events and base rates

Suspicious sign-ins are rare among millions of legitimate ones. A detection rule that flags one percent of normal sign-ins would produce thousands of alerts daily, almost all false. This is the base-rate problem: even an accurate detector produces mostly false alarms when the event it looks for is rare. Sana uses it to explain why the council's sign-in monitoring must combine several signals, such as new device, impossible travel and failed second factors, rather than alerting on any single unusual feature.

### 7.4 Uncertainty in estimates

Estimates from samples carry uncertainty. If a pilot of 200 staff sees 6 lockouts in a week, the true weekly rate for that group is uncertain, and Sana reports an interval rather than a single number. Larger samples give narrower intervals. Reporting uncertainty helps managers decide wisely: a wide interval suggests waiting for more data before committing desk staff, while a narrow one supports a firm plan. Ignoring uncertainty leads to overconfident decisions that later look like mistakes. Intervals are recalculated as more weeks of data arrive.

### Worked example

With an average of four lockouts per Monday morning hour, a Poisson model gives about a 21 percent chance of six or more in one hour, which Sana uses to plan desk cover.

> **Synthetic case.** Rates and counts are synthetic.

### Errors and limits

Reporting only a mean sign-in time hides the slow tail that users actually experience.

### Exercises

- **EX019 — Poisson assumption.** What assumption does a Poisson lockout model rely on? *Rubric:* 3 = independent events at a stable rate;; 2 = independence;; 1 = normality;; 0 = none.
- **EX020 — Percentile meaning.** What does a 95th percentile of twelve seconds mean? *Rubric:* 3 = one in twenty sign-ins takes twelve seconds or more;; 2 = slow tail;; 1 = average;; 0 = none.
- **EX021 — Base-rate effect.** Why does a 1% false-alarm rate overwhelm monitoring? *Rubric:* 3 = legitimate sign-ins vastly outnumber suspicious ones;; 2 = base rate;; 1 = vague;; 0 = none.

### Synthesis

Simple probability models and robust summaries make identity operations measurable and plannable.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) explain how secure hardware stores keys; (2) relate processor and memory to cryptographic cost; (3) size identity servers sensibly.

### 8.1 Secure hardware

Identity systems rely on hardware that protects keys. Trusted platform modules in laptops, secure enclaves in phones and hardware security modules in data centres keep private keys inside protected boundaries and perform signing there, so software outside never sees the key. The identity provider's token-signing key is the most valuable secret in Sana's design, because anyone holding it could create tokens accepted by every application. She plans to keep it in a hardware security module or a managed key service with equivalent protection, with access tightly logged.

### 8.2 Cost of cryptography

Every sign-in involves cryptographic operations: verifying a passkey signature, signing an ID token and checking certificates. Each consumes processor time. Elliptic-curve signatures are much faster to create than older RSA signatures of similar strength, which affects how many tokens per second a server can issue. Sana measures signing time on representative hardware in the lab rather than trusting general figures, because actual cost depends on the processor, the library and whether a hardware module is involved. The results feed directly into the sizing estimate in this chapter.

### 8.3 Memory and sessions

The identity provider keeps session state for signed-in users, such as which authentication methods were used and when the session expires. With 2,400 staff and some on several devices, sessions number in the thousands, each using a small amount of memory or database storage. Sana estimates this and checks what happens when the store fills or a server restarts. If sessions are lost on restart, every user must sign in again at once, creating a sudden load spike that the capacity plan must allow for.

### 8.4 Sizing servers

Combining peak sign-in rate, cryptographic cost per sign-in and session storage gives a server sizing estimate. Sana adds headroom for growth and for one server failing, so the remaining servers can carry the whole load. She documents the estimate with its assumptions and plans a load test in the verification laboratory. Sizing from measured costs rather than vendor marketing figures avoids both waste and the far worse outcome of a provider that collapses at the morning peak. The load test then confirms or corrects these figures.

### Worked example

Measured signing at about 0.4 milliseconds per token and a peak of 28 sign-ins per second give modest processor load; Sana sizes for two servers, each able to carry the full peak alone.

> **Synthetic case.** Measurements and servers are synthetic.

### Errors and limits

Storing the token-signing key in an ordinary file on the server exposes the most valuable secret in the design.

### Exercises

- **EX022 — Signing key value.** Why is the token-signing key the most valuable secret? *Rubric:* 3 = anyone holding it can forge tokens every app accepts;; 2 = forge tokens;; 1 = encryption;; 0 = none.
- **EX023 — Restart spike.** What happens if sessions are lost on restart? *Rubric:* 3 = all users sign in again, causing a load spike;; 2 = spike;; 1 = vague;; 0 = none.
- **EX024 — Failure headroom.** How does Sana plan for one server failing? *Rubric:* 3 = each server can carry full peak alone;; 2 = headroom;; 1 = vague;; 0 = none.

### Synthesis

Secure hardware protects keys, and measured cryptographic and session costs drive realistic sizing.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) build larger, structured programs; (2) parse identity exports; (3) handle errors and keep results reproducible.

### 9.1 Larger programs

As Sana's checks grow, she splits code into modules: readers for each export format, a common account model, comparison logic and report writers. Each module is small enough to understand. Functions have clear names and short docstrings, and there are no global variables that would make one part depend invisibly on another. This structure lets a colleague review the code and lets Sana add a new application's export by writing one reader, without touching the comparison logic that has already been tested.

### 9.2 Parsing exports

Application exports arrive in different formats: comma-separated files, directory listings and JSON from cloud services. A parser turns each into a common structure: username, display name, status, last sign-in and roles. Sana writes parsers against synthetic samples first, and each parser reports lines it cannot understand rather than silently skipping them. A silently skipped line could hide exactly the stale administrator account the check exists to find, so visible errors are a safety feature, not an inconvenience. Each parser has its own tests using small synthetic files.

### Lab — Role summary

```python
"""Summarise synthetic role assignments: members per role and risky permission combinations (stdlib only)."""
from collections import defaultdict
roles = {"clerk": {"view", "payments-raise"}, "clerk-plus": {"view", "payments-raise", "export"}, "approver": {"view", "payments-approve"},
         "manager": {"view", "payments-approve", "reports"}, "manager-temp": {"view", "payments-approve", "reports", "export"},
         "auditor": {"view", "reports"}, "helpdesk": {"view", "reset"}}
assign = {"u01": ["clerk"], "u02": ["clerk"], "u03": ["clerk"], "u04": ["clerk-plus"], "u05": ["approver"], "u06": ["approver"],
          "u07": ["manager"], "u08": ["manager"], "u09": ["manager-temp"], "u10": ["auditor"], "u11": ["helpdesk"], "u12": ["clerk", "approver"]}
members = defaultdict(int)
for u, rs in assign.items():
    for r in rs: members[r] += 1
print(f"accounts={len(assign)} roles={len(roles)}")
for r in roles: print(f"  {r:13} members={members[r]}")
print("single-member roles:", sorted(r for r in roles if members[r] == 1))
for u, rs in sorted(assign.items()):
    p = set().union(*(roles[r] for r in rs))
    if {"payments-raise", "payments-approve"} <= p: print("raise+approve:", u, rs)
```

Run with `python3 lab_roles.py`. Verified output:

```text
accounts=12 roles=7
  clerk         members=4
  clerk-plus    members=1
  approver      members=3
  manager       members=2
  manager-temp  members=1
  auditor       members=1
  helpdesk      members=1
single-member roles: ['auditor', 'clerk-plus', 'helpdesk', 'manager-temp']
raise+approve: u12 ['clerk', 'approver']
```

### 9.3 Reading the role summary

The synthetic export lists twelve accounts across seven roles. Four roles have only one member each, and two of those differ from a larger role by a single permission. This is the early stage of role explosion described in chapter 2. The script also shows one account holding both payments-raise and payments-approve through different roles. Sana records these as findings for the role design work later in the project, noting that the data is synthetic and the real export must be checked with each application owner.

### 9.4 Reproducibility

A result is reproducible when someone else can run the same program on the same input and get the same output. Sana records the script version, the export file and its date, and avoids hidden dependencies such as the current date unless it is passed in explicitly. Reports include these details in a header. When an auditor later asks how a finding was produced, Sana can show exactly which script and data created it, which turns analysis into evidence the council can rely on.

### Worked example

The role summary finds seven roles for twelve accounts, four single-member roles and one account combining raise and approve permissions.

> **Synthetic case.** Exports, roles and accounts are synthetic.

### Errors and limits

Parsers that silently skip unreadable lines can hide the very accounts a check is meant to find.

### Exercises

- **EX025 — Single-member roles.** How many single-member roles does the lab find? *Rubric:* 3 = four, two differing by one permission;; 2 = four;; 1 = vague;; 0 = none.
- **EX026 — Combined permissions.** What risky combination does the lab find? *Rubric:* 3 = one account with payments-raise and payments-approve;; 2 = raise and approve;; 1 = vague;; 0 = none.
- **EX027 — Report header.** What does Sana put in each report header? *Rubric:* 3 = script version, export file and date;; 2 = version;; 1 = name;; 0 = none.

### Synthesis

Modular, error-reporting, reproducible programs make identity analysis dependable across many applications.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply professional duties to identity work; (2) obtain authorisation; (3) handle personal data and changes safely.

### 10.1 Professional duties

Identity systems decide who can reach records about residents, payments and staff. Engineers working on them owe duties to the public, not only to the client: honesty about risk, staying within competence and refusing to approve unsafe designs. Sana reads the code of conduct of her professional body and notes that it requires her to raise concerns even when that is uncomfortable, such as telling a director that former staff still have access. Professional duties exist precisely for moments when silence would be easier.

### 10.2 Authorisation

Any security work on council systems requires written permission from someone entitled to give it, stating scope, timing and methods. Sana's authorisation covers reading exports provided by application owners and working in a separate test environment. It does not cover signing in to production systems, testing passwords or trying to bypass controls. If she finds she needs something outside that scope, she stops and asks. Working without authorisation, even with good intentions, can be illegal and can damage trust in the whole project.

### 10.3 Data care

Account exports contain names, roles and last sign-in times, which are personal data about staff. Sana collects only the fields each check needs, stores files on an encrypted council share with access logged, and deletes them when the check is complete. Where possible, application owners pseudonymise usernames before export. For teaching and testing she uses synthetic data, as in this book. Treating colleagues' data with care is part of earning permission to work with it again. Access to these files is reviewed at the end of each check.

### 10.4 Change safety

Changes to identity systems can lock out many people at once: a faulty single sign-on setting can stop every user reaching an application. Safe practice is to plan each change, have it reviewed, schedule it for a low-impact time, keep a tested rollback and verify afterwards that sign-in still works for representative users. Sana also ensures that at least one emergency administrator account remains usable during changes, so a mistake cannot remove the ability to fix it. Every change and its outcome is recorded for later review.

### Worked example

Sana's authorisation letter lists permitted activities (reading owner-provided exports, test environment work) and excluded ones (production sign-in, password testing, bypass attempts).

> **Synthetic case.** The authorisation and data are synthetic.

### Errors and limits

Making identity changes without an emergency administrator path can turn a small mistake into a long outage.

### Exercises

- **EX028 — Uncomfortable duty.** What uncomfortable report does Sana's duty require? *Rubric:* 3 = telling a director former staff still have access;; 2 = raise concern;; 1 = stay silent;; 0 = none.
- **EX029 — Excluded activities.** Name two activities outside Sana's authorisation. *Rubric:* 3 = production sign-in, password testing, bypass attempts (two);; 2 = one;; 1 = vague;; 0 = none.
- **EX030 — Emergency account.** Why keep an emergency administrator account during changes? *Rubric:* 3 = so a mistake cannot remove the ability to fix it;; 2 = recovery;; 1 = convenience;; 0 = none.

### Synthesis

Professional duty, written authorisation, data care and safe change practice are the foundations of trustworthy identity engineering.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) trace how sign-in traffic crosses networks; (2) explain HTTPS redirects in federation; (3) identify where tokens travel.

### 11.1 Sign-in over the network

When a council employee opens an application, the browser is redirected to the identity provider, signs in there and is redirected back carrying proof of authentication. Every step travels over HTTPS, which protects the content with TLS. Sana traces this path for a typical application: browser to application, browser to provider, provider back to browser, browser to application. Understanding the path shows where tokens and codes appear, and therefore which links, logs and devices must protect them, since anything that captures a token may be able to replay it.

### 11.2 Redirects and codes

In OpenID Connect's authorisation code flow, the provider does not send the ID token through the browser directly. It sends a short-lived code, which the application exchanges with the provider over a direct back-channel connection for tokens. RFC 6749 defines this pattern for OAuth 2.0, and RFC 7636 adds Proof Key for Code Exchange so that a stolen code cannot be redeemed by someone else. RFC 9700 recommends these practices as current best practice. Sana requires them for every new integration at Linmouth.

Without PKCE, a malicious app that intercepted the code on the same device could exchange it for tokens itself.

### 11.3 Name resolution and trust

Browsers find the identity provider through DNS, then verify its TLS certificate. If DNS were tampered with and the certificate not checked, staff could be sent to a fake sign-in page. Proper certificate validation in browsers protects against this, and phishing-resistant authenticators add a second layer, because a passkey will not sign for a site whose origin differs from the one it was registered with. Sana documents the provider's domain names and certificate management as part of the identity design, not as a separate network matter.

### 11.4 Where tokens travel

Access tokens travel from applications to APIs on every request. If any hop uses plain HTTP, or if tokens are written to logs, they can be copied. Sana lists every place a token may appear: browser storage, application memory, API gateways, logs and monitoring tools. For each, she sets a rule, such as transport only over TLS and never logging full tokens. This inventory turns a vague worry about token theft into concrete checks that can be reviewed and tested in the verification laboratory.

### Worked example

Sana traces an OpenID Connect code flow at Linmouth through four hops and lists five places tokens may appear, each with a protection rule.

> **Synthetic case.** Hops, domains and applications are synthetic.

### Errors and limits

Logging full access tokens for debugging creates a store of reusable credentials.

### Exercises

- **EX031 — Code exchange.** How does an application turn an authorisation code into tokens? *Rubric:* 3 = direct back-channel exchange with the provider;; 2 = back-channel;; 1 = browser;; 0 = none.
- **EX032 — PKCE purpose.** What does Proof Key for Code Exchange prevent? *Rubric:* 3 = redemption of a stolen code by someone else;; 2 = stolen code use;; 1 = phishing;; 0 = none.
- **EX033 — Token log rule.** What logging rule protects tokens? *Rubric:* 3 = never log full tokens;; 2 = no tokens in logs;; 1 = log all;; 0 = none.

### Synthesis

Tracing sign-in across the network shows where codes and tokens travel and what must protect them.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) explain local accounts and privileges on hosts; (2) relate device sign-in to central identity; (3) protect administrator rights on endpoints.

### 12.1 Local accounts

Every laptop and server has local accounts managed by its operating system, alongside any central directory accounts. Local administrator accounts are powerful and often share the same password across many machines when built from one image. If one machine's local password is discovered, all others become exposed. Sana recommends unique, automatically rotated local administrator passwords stored centrally with access logged, so each machine's local account is different and its use is visible. Use of a local administrator account then becomes a rare, visible event that monitoring can flag, rather than routine background activity that hides misuse among normal work.

### 12.2 Privilege on endpoints

Operating systems separate ordinary users from administrators. Staff who work daily as administrators can install software and change security settings, which means any malicious file they open gains the same power. Least privilege on endpoints means staff use standard accounts, with elevation granted only when needed and logged. At Linmouth, about a third of staff hold local administrator rights for historical reasons; Sana proposes removing them in stages, with a request process for genuine needs such as specialist software installation.

### 12.3 Device sign-in and central identity

When staff sign in to a council laptop, the operating system can verify them against the central directory or identity provider, and may unlock a device-bound key that later serves as a passkey. Joining devices to central identity means a disabled account can no longer sign in to any council device. It also allows device health, such as encryption and updates, to inform access decisions. Sana maps which device types are joined, which are not, and what that means for leavers.

### 12.4 Service accounts on hosts

Services on servers often run under dedicated accounts. These accounts are rarely reviewed, frequently over-privileged and sometimes hold passwords that never change. Sana inventories service accounts on a sample of servers, recording owner, purpose, privileges and how credentials are managed. Where possible, she recommends managed service identities whose credentials rotate automatically. Service accounts are part of identity and access management too, and attackers often look for them precisely because organisations forget them. Each service account also gets a review date, so it is checked along with human accounts rather than forgotten.

### Worked example

A synthetic server sample shows 14 service accounts, 5 without a named owner and 3 with passwords unchanged for over two years; Sana records them as findings.

> **Synthetic case.** Servers and accounts are synthetic.

### Errors and limits

Building every laptop from one image with the same local administrator password exposes all machines when one is compromised.

### Exercises

- **EX034 — Shared local password.** Why is one shared local administrator password dangerous? *Rubric:* 3 = exposure of one machine exposes all;; 2 = all machines;; 1 = speed;; 0 = none.
- **EX035 — Endpoint least privilege.** How does Sana apply least privilege to staff laptops? *Rubric:* 3 = standard accounts, logged elevation on request;; 2 = standard accounts;; 1 = all admin;; 0 = none.
- **EX036 — Ownerless service accounts.** How many service accounts lack a named owner in the sample? *Rubric:* 3 = 5 of 14;; 2 = 5;; 1 = 14;; 0 = none.

### Synthesis

Unique local credentials, least privilege on endpoints, central device sign-in and reviewed service accounts extend IAM to every host.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) design a store for identity and audit data; (2) define a schema for sign-in events; (3) plan queries and retention.

### 13.1 Identity data sources

Identity data comes from several systems: the HR record of staff and roles, the directory of accounts and groups, the identity provider's sign-in logs, application access logs and the service desk's ticket system. Each answers different questions. HR says who should exist, the directory says who does, sign-in logs show who is active and tickets show who needed help. Sana lists each source with its owner, update frequency and clock, because combining them only works when identities and timestamps can be matched reliably.

### 13.2 Schema for sign-in events

Sana defines a schema for sign-in events: time in UTC, user identifier, application, authentication methods used, result, client device, network location and a correlation identifier linking related events. Agreeing the schema before collection allows events from different systems to be stored and queried together. Without it, one system's user field might hold an email address and another's an internal number, so queries silently miss matches. The schema is documented with examples and versioned as it changes. Fields that some sources cannot supply are marked as optional.

### 13.3 Queries

Good queries answer operational questions: how many sign-ins failed for each user yesterday, which accounts have not signed in for ninety days, and which administrators signed in from new devices this week. Sana writes each query with an explicit time window and filters, checks its result against a small sample read by hand, and saves it with a description. During an incident there is no time to write and debug new queries, so a tested library of common queries is part of being prepared.

### 13.4 Retention and access

Sign-in logs are personal data and also evidence. Sana sets retention by purpose: detailed events for a year to support investigations, summaries for longer for trend reporting. Access to the logs is restricted to named roles and logged in turn, because logs reveal staff working patterns. Deletion at the end of the period is automated so the rule is actually applied. She records these decisions in the data protection documentation, linking each to the policy that justifies it. Requests to extend retention need documented approval.

### Worked example

Sana's sign-in schema has eight fields, a tested query finds 61 synthetic accounts inactive for over ninety days, and retention is one year detailed, three years summarised.

> **Synthetic case.** Sources, counts and periods are synthetic.

### Errors and limits

Combining sources whose user identifiers or clocks differ produces queries that silently miss matches.

### Exercises

- **EX037 — HR role.** What question does the HR record answer? *Rubric:* 3 = who should exist;; 2 = staff;; 1 = who signed in;; 0 = none.
- **EX038 — Correlation identifier.** What is the correlation identifier for? *Rubric:* 3 = linking related events;; 2 = linking;; 1 = encryption;; 0 = none.
- **EX039 — Inactive query.** What does the tested inactivity query find? *Rubric:* 3 = 61 accounts inactive over ninety days;; 2 = 61;; 1 = vague;; 0 = none.

### Synthesis

A shared schema, tested queries and purposeful retention turn identity logs into reliable evidence.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) manage identity configuration as code; (2) review and test integration changes; (3) deploy safely in stages.

### 14.1 Configuration as code

Identity provider settings, application integrations, group rules and access policies can be kept as text files in version control rather than edited by hand in an administration console. Every change then records who made it, when and why, and earlier versions can be restored. Sana uses templates for application integrations, so each new application follows the same secure defaults, such as the code flow with PKCE and short token lifetimes. Consistency across 140 applications is only realistic when configuration is generated, not typed.

### 14.2 Review

Every proposed identity change is reviewed by a second engineer before it is applied. The reviewer checks that the change does what its description says, that it does not grant broader access than intended, that redirect addresses are exact rather than wildcards and that a rollback exists. Review comments stay with the change record, documenting reasoning for later engineers. Sana finds that the most common review finding is an over-broad group assignment, which would have given whole departments access meant for a single team.

### 14.3 Testing

Identity changes can be tested before deployment. Syntax checks confirm the configuration is valid. Policy tests confirm that representative synthetic users get the access expected and are refused access they should not have, using a table of expected outcomes. Integration tests in a test tenant confirm that sign-in works end to end. Sana runs these automatically on every proposed change, so a mistake that would lock out a department is found in minutes in the test environment rather than by staff on a Monday morning.

### 14.4 Staged deployment

Approved changes are deployed in stages: first to a test tenant, then to a pilot group of volunteers, then to everyone. At each stage Sana checks sign-in success rates and service desk calls before continuing. Each stage has a defined rollback, and the deployment record notes the exact configuration version. Automating deployment from version control removes manual retyping in consoles, which is a common source of errors, and guarantees that what runs in production is exactly what was reviewed and tested.

### Worked example

A proposed change assigning the whole finance department to a payroll application is caught in review; the corrected change targets the payroll team group and passes policy tests.

> **Synthetic case.** Changes, groups and tests are synthetic.

### Errors and limits

Wildcard redirect addresses in application integrations can let tokens be sent to unintended destinations.

### Exercises

- **EX040 — Template benefit.** Why use templates for application integrations? *Rubric:* 3 = consistent secure defaults across many apps;; 2 = consistency;; 1 = speed only;; 0 = none.
- **EX041 — Common finding.** What is the most common review finding at Linmouth? *Rubric:* 3 = over-broad group assignment;; 2 = broad group;; 1 = typos;; 0 = none.
- **EX042 — Policy test content.** What does a policy test check? *Rubric:* 3 = expected access granted and forbidden access refused for synthetic users;; 2 = access table;; 1 = syntax;; 0 = none.

### Synthesis

Version-controlled, reviewed, tested and staged identity changes are safer than console edits.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to identity; (2) use least privilege and separation of duties; (3) categorise identity threats.

### 15.1 CIA for identity

Confidentiality in identity means credentials, tokens and personal data are not exposed. Integrity means accounts, group memberships and policies change only through authorised processes. Availability means staff can sign in when they need to. The three can conflict: very strict sign-in rules protect confidentiality but may hurt availability if staff are locked out. Sana states which property each control supports and how it might harm another, so trade-offs are made consciously rather than discovered after rollout. Each conflict is recorded with the choice made and who accepted it.

### 15.2 Least privilege and separation of duties

Least privilege means each person and system has only the access needed for their role. Separation of duties means no single person can complete a sensitive task alone, such as raising and approving the same payment. Saltzer and Schroeder (1975) described related principles decades ago, and NIST SP 800-53 Rev. 5 includes both in its access control family. At Linmouth, Sana treats them as design requirements: roles are built from job functions, and conflicting permissions are prevented from being held together.

A role combining payment raising and approval, for example, is rejected at design time rather than discovered in a later review.

### 15.3 Defence in depth

No single identity control is enough. Strong authentication, least privilege, monitoring of sign-ins, regular access reviews and rapid leaver processing each address different failures. If an attacker obtains a session, least privilege limits what they can reach; if a review is skipped, the leaver process may still remove access; if monitoring misses an event, the review may catch the result later. Sana checks that layers fail independently, since two controls relying on the same data feed can fail together. Independence is checked during design review.

### 15.4 Identity threat categories

Sana groups identity threats to check her design systematically: credential theft through phishing or reuse; abuse of recovery and reset processes; excessive or stale privileges; misuse by authorised insiders; compromise of the identity provider or its signing keys; and failures of integration such as misconfigured redirects. For each category she lists the controls that reduce it and the evidence that they work. The categories prompt thinking but are not complete, so she also asks council staff about threats specific to their services.

### Worked example

Sana's threat table lists six identity threat categories, each linked to at least two controls and one verification method.

> **Synthetic case.** Threat entries and controls are synthetic.

### Errors and limits

Making sign-in so strict that staff are routinely locked out trades confidentiality for availability without saying so.

### Exercises

- **EX043 — CIA conflict.** How can strict sign-in harm availability? *Rubric:* 3 = lockouts stop staff working;; 2 = lockout;; 1 = it cannot;; 0 = none.
- **EX044 — Separation example.** Give an example of separation of duties. *Rubric:* 3 = raising and approving the same payment kept apart;; 2 = payments;; 1 = passwords;; 0 = none.
- **EX045 — Recovery threat.** Which threat category covers abuse of reset processes? *Rubric:* 3 = recovery and reset abuse;; 2 = recovery;; 1 = insider;; 0 = none.

### Synthesis

CIA, least privilege, separation of duties, defence in depth and threat categories give identity design its security foundations.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) apply the systems lifecycle to an identity programme; (2) write verifiable requirements; (3) maintain traceability and interfaces.

### 16.1 Lifecycle

Sana's project follows the systems engineering lifecycle: understanding needs, writing requirements, design, implementation, verification, operation and eventually retirement of old account stores. Each stage produces documents the next relies on. Security is considered throughout, because a flaw designed into the identity architecture, such as one shared administrator role across all applications, is far costlier to fix after 140 applications depend on it. Reviews between stages confirm that outputs are complete before work continues. Retiring old account stores is planned from the start, since leaving them running alongside the new provider keeps old weaknesses alive.

### 16.2 Requirements

A requirement states what the system must do or how well, in a way that can be checked. Leavers' access to all integrated applications must be removed within four working hours of their HR end date is a requirement; buy a particular identity product is a design decision. Each requirement has an identifier, a source such as an audit finding or council policy, and a planned verification method. Sana writes about sixty requirements, grouped into authentication, authorisation, lifecycle, audit and operations.

### 16.3 Traceability

A traceability matrix links each requirement to the design elements that satisfy it and the tests that verify it. Gaps become visible: a requirement with no test is unverified, and a design element linked to no requirement may be unnecessary. When the council changes a requirement, the links show what must be revisited. Auditors use the matrix to confirm that promises were kept. Sana keeps it in version control next to the configuration, so it changes together with the system it describes.

### 16.4 Interfaces

Many identity failures happen at interfaces: between HR and the directory, between the provider and each application, between the provider and the service desk tools. Each side assumes something about the other, such as when an HR end date becomes effective. Sana writes interface specifications recording what crosses each boundary, in which direction, in what format, how often and who owns each side. Agreeing them in writing prevents gaps, such as a leaver feed that runs weekly when the requirement assumes hours.

### Worked example

Requirement LC-03 (leaver removal within four working hours) traces to the HR-to-directory feed, the provisioning connector and test case T-LC-03.

> **Synthetic case.** Requirements, interfaces and tests are synthetic.

### Errors and limits

Writing product choices as requirements closes off design options before alternatives are compared.

### Exercises

- **EX046 — Requirement versus design.** Which is a requirement: leaver removal within four hours, or buying a product? *Rubric:* 3 = leaver removal within four hours;; 2 = first;; 1 = product;; 0 = none.
- **EX047 — Untested requirement.** What does a requirement without a linked test indicate? *Rubric:* 3 = it is unverified;; 2 = gap;; 1 = done;; 0 = none.
- **EX048 — Interface gap example.** What interface gap does Sana give as an example? *Rubric:* 3 = weekly leaver feed when hours required;; 2 = timing;; 1 = vague;; 0 = none.

### Synthesis

Lifecycle stages, verifiable requirements, traceability and written interfaces keep an identity programme coherent.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) view identity operations as feedback loops; (2) set thresholds for sign-in alerts; (3) avoid oscillating automated responses.

### 17.1 Feedback in identity operations

Identity operations form feedback loops. Monitoring measures sign-in failures, lockouts and risky events; people or automation compare them with expectations; and actions follow, such as requiring a second factor or locking an account. A good loop corrects problems quickly and steadily. A poor one reacts too slowly, letting an attack continue, or too aggressively, locking out legitimate staff. Seeing operations as feedback helps Sana design alerts and automated responses that keep the system stable. Measuring how long each loop takes to respond shows where it is too slow.

### 17.2 Thresholds

An account lockout threshold turns a count of failed sign-ins into a decision. Too low, and staff who mistype a few times are locked out, flooding the service desk; too high, and guessing attempts continue longer. NIST SP 800-63B-4 discusses limiting failed attempts as part of authenticator management. Sana sets thresholds from measured normal behaviour, uses a time window so old failures expire, and reviews thresholds after rollout, since passkeys change failure patterns substantially. Each threshold has a named owner who reviews it quarterly.

### 17.3 Oscillation and self-harm

Automated responses can oscillate or cause harm. If many failed sign-ins trigger lockouts, and lockouts generate reset requests that themselves fail, the loop amplifies a small problem. Worse, an attacker who knows a username can deliberately lock out that person by failing on purpose. Sana prefers responses that slow attempts progressively or require additional verification, rather than hard lockouts, so that the control limits guessing without handing anyone an easy way to deny service to colleagues. Alerts accompany these responses so analysts can see patterns.

### 17.4 Human in the loop

Many identity responses keep a person in the loop: an alert reaches an analyst, who decides whether a risky sign-in is genuine. People add judgement but also delay and fatigue. Sana designs alerts that include context, such as the user's usual locations and devices, and writes runbooks for common cases. She measures time from alert to decision, because a loop with a person in it is only as fast as that person can act, and alerts nobody reads provide no control at all.

### Worked example

Replacing a hard five-failure lockout with progressive delays cuts synthetic lockout tickets by about two thirds while keeping guessing attempts slow.

> **Synthetic case.** Thresholds, tickets and rates are synthetic.

### Errors and limits

Hard lockouts let anyone who knows a username deny that person access by failing on purpose.

### Exercises

- **EX049 — Low threshold effect.** What happens when a lockout threshold is too low? *Rubric:* 3 = staff locked out, desk flooded;; 2 = lockouts;; 1 = vague;; 0 = none.
- **EX050 — Lockout abuse.** How can hard lockouts be abused? *Rubric:* 3 = attacker fails deliberately to lock someone out;; 2 = deny service;; 1 = vague;; 0 = none.
- **EX051 — Progressive response.** What does Sana prefer to hard lockouts? *Rubric:* 3 = progressive slowing or extra verification;; 2 = delays;; 1 = no limit;; 0 = none.

### Synthesis

Identity controls are feedback loops; good thresholds, progressive responses and supported analysts keep them stable.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) place identity controls in an architecture; (2) centralise decisions sensibly; (3) keep the design simple.

### 18.1 Identity as the control plane

In Linmouth's target design, the identity provider becomes the central point where staff are authenticated and where many access decisions are made. Zero trust architecture, described in NIST SP 800-207, treats every access request as needing verification based on identity, device and context rather than network location. Sana does not adopt zero trust as a slogan; she uses its ideas to decide where policy decisions are made, where they are enforced and what information each decision needs. This keeps the design grounded in specific, testable decisions.

### 18.2 Decision and enforcement points

SP 800-207 separates the policy decision point, which decides whether access is allowed, from the policy enforcement point, which applies the decision. In Sana's design, the identity provider and its conditional access rules decide; applications and gateways enforce by accepting or rejecting tokens. Separating them means policy can change centrally without modifying each application. It also concentrates risk: if the decision point fails or is misconfigured, every application is affected, so it needs strong change control and resilience. The decision point is therefore deployed redundantly.

### 18.3 Placing controls

Sana places controls where they are most effective. Authentication strength is enforced at the provider, so all applications benefit. Fine-grained authorisation, such as which case records a social worker may view, stays in the application, which understands its own data. Lifecycle automation sits between HR and the directory. Monitoring collects events from all of these. Each placement is recorded on the architecture diagram with its purpose, so reviewers can see why a control lives where it does. Placement decisions are revisited if requirements change.

### 18.4 Simplicity

Every extra identity provider, exception policy or special sign-in path adds a place for errors. Sana prefers one provider for staff, a small number of conditional access policies and consistent integration templates. She justifies any added complexity by a specific requirement, such as a separate arrangement for external partners. Simple designs are easier to review, test and operate, and operators who understand the whole design are less likely to make dangerous changes under pressure. Simplicity also reduces training needs for the small identity team.

### Worked example

Sana's architecture places authentication at one provider, authorisation detail in applications, lifecycle between HR and directory, and monitoring across all, with decision and enforcement points labelled.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Pushing all fine-grained authorisation into the central provider ignores that applications best understand their own data.

### Exercises

- **EX052 — Decision versus enforcement.** What does the policy enforcement point do? *Rubric:* 3 = applies the decision by accepting or rejecting access;; 2 = enforce;; 1 = decide;; 0 = none.
- **EX053 — Central risk.** What risk comes with a central decision point? *Rubric:* 3 = its failure or misconfiguration affects every application;; 2 = single point;; 1 = vague;; 0 = none.
- **EX054 — Authorisation placement.** Where does fine-grained authorisation stay in Sana's design? *Rubric:* 3 = in the application, which knows its data;; 2 = application;; 1 = provider;; 0 = none.

### Synthesis

Clear decision and enforcement points, deliberate control placement and simplicity make identity architecture robust.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) explain keys, certificates and signatures in identity; (2) describe token formats and signing; (3) plan key lifecycle.

### 19.1 Signatures and trust

Identity federation relies on digital signatures. The identity provider signs assertions and tokens with its private key; applications verify them with the matching public key. If verification succeeds, the application knows the token came from the provider and was not altered. SAML 2.0, an OASIS standard, uses signed XML assertions; OpenID Connect uses signed JSON Web Tokens defined in RFC 7519. Sana explains that the whole system's trust rests on the secrecy of the provider's signing keys and on applications actually checking signatures.

### 19.2 Token contents

A JSON Web Token carries claims: who the user is, who issued the token, which application it is for, when it was issued and when it expires. Applications must check all of these, not only the signature. A valid token issued for a different application should be rejected, and an expired one refused. Sana lists the checks required of every integration and includes them in policy tests, because skipping the audience or expiry check is a common integration mistake that makes valid tokens dangerous.

### 19.3 Certificates

Certificates bind public keys to names and are used for TLS on the provider's sign-in pages and sometimes for signing keys. Each has an expiry date. An expired signing certificate can stop sign-in to every federated application at once, which has caused outages in many organisations. Sana inventories every certificate in the identity system with owner, expiry and renewal procedure, and sets alerts well in advance. Renewal is rehearsed in the test tenant so it is routine rather than an emergency.

### 19.4 Key lifecycle

Signing keys pass through generation, publication, use, rotation and retirement. Rotation limits damage if a key leaks and keeps the procedure practised. Providers usually publish their current public keys at a well-known address, so applications can fetch new ones automatically. Sana checks that each application does so, rather than having a key copied into its configuration by hand, because hand-copied keys break silently at rotation. Revocation is also planned, so a compromised key can be withdrawn quickly. Each step has a named owner and a rehearsed procedure.

### Worked example

Sana's integration checklist requires signature, issuer, audience and expiry checks; her certificate inventory shows two signing certificates expiring within ninety days, both scheduled for rehearsed renewal.

> **Synthetic case.** Certificates and checks are synthetic.

### Errors and limits

Checking only a token's signature, not its audience and expiry, accepts tokens meant for other applications or already expired.

### Exercises

- **EX055 — JWT standard.** Which RFC defines JSON Web Tokens? *Rubric:* 3 = RFC 7519;; 2 = 7519;; 1 = 6749;; 0 = none.
- **EX056 — Required checks.** Which four token checks does Sana require? *Rubric:* 3 = signature, issuer, audience, expiry;; 2 = three;; 1 = signature only;; 0 = none.
- **EX057 — Hand-copied keys.** Why avoid hand-copying signing keys into applications? *Rubric:* 3 = they break silently at rotation;; 2 = rotation;; 1 = size;; 0 = none.

### Synthesis

Signatures, complete token checks, managed certificates and automated key rotation keep federation trustworthy.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Identity and access management: engineering context

### Learning outcomes

You will (1) describe Linmouth's current identity state; (2) record constraints; (3) state the engineering problem and success measures.

### 20.1 Current state

Linmouth has an on-premises directory for laptop sign-in and email, plus about 140 applications. Around 60 use their own local accounts; 50 sync accounts from the directory; and 30 cloud services each have their own sign-up. HR sends a monthly leaver list by email to IT, who forward it to application owners. Multi-factor authentication covers email only. Sana records this state with dated evidence, including counts of accounts per system, so later improvements can be measured against a fair baseline rather than impressions.

The 60 applications with local accounts are where leavers are most likely to keep access, since the monthly email relies on each owner acting.

### 20.2 Constraints

Constraints shape what is possible: a limited budget, a small identity team of three, some legacy applications that cannot use modern federation, union agreements on monitoring of staff, and the need to keep council services running throughout. Some applications are supplied by vendors who must make changes themselves. Sana writes these down early and agrees them with the council, because a design that ignores constraints may look excellent and still fail when the team cannot operate it or the budget runs out halfway.

### 20.3 The engineering problem

Stated plainly, the problem is to give every member of staff one strong sign-in for all council applications they need, to grant access by role with exceptions governed, to remove access promptly when people move or leave, and to produce evidence that these things happen, all within the constraints and without disrupting services. A clear statement keeps later work focused. Sana tests each design option and each piece of work against it, asking whether it moves the council closer to that outcome.

### 20.4 Success measures

Sana agrees measures with the council before work starts: the share of applications integrated with single sign-on; the share of staff using phishing-resistant authentication; median time from HR leaver date to access removal; the number of accounts with no matching employee; and service desk password tickets per hundred staff. Each has a baseline, a target and a collection method. Agreeing them in advance prevents results being reinterpreted later to look better than they are. Results are reported to directors every quarter against these targets.

### Worked example

Baseline: 0 of 140 applications on single sign-on, multi-factor only for email, median leaver removal 19 days, 312 accounts with no matching employee across sampled systems.

> **Synthetic case.** Counts and timings are synthetic.

### Errors and limits

Starting design without a measured baseline makes it impossible to show improvement credibly.

### Exercises

- **EX058 — Leaver process today.** How are leavers communicated today? *Rubric:* 3 = monthly emailed list forwarded to app owners;; 2 = monthly email;; 1 = automated;; 0 = none.
- **EX059 — Constraint examples.** Name two constraints Sana records. *Rubric:* 3 = budget, small team, legacy apps, union agreements, service continuity (two);; 2 = one;; 1 = vague;; 0 = none.
- **EX060 — Baseline leaver time.** What is the baseline median leaver removal time? *Rubric:* 3 = 19 days;; 2 = weeks;; 1 = hours;; 0 = none.

### Synthesis

A documented baseline, written constraints, a clear problem statement and agreed measures frame the whole engineering effort.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Identity and access management: requirements

### Learning outcomes

You will (1) write security, lifecycle and operational requirements for identity; (2) prioritise them with the council; (3) choose a verification method for each.

### 21.1 Security requirements

Sana writes security requirements that can be tested. Examples: all staff sign-ins to integrated applications must use multi-factor authentication; administrators must use phishing-resistant authenticators as described in NIST SP 800-63B-4; tokens must expire within one hour and refresh only while the session is valid; no account may hold permissions that break a defined separation-of-duties rule. Each requirement names the threat it addresses from the threat table, so reviewers can see why it exists, and each avoids naming a product, leaving the design free to choose the best way to meet it.

### 21.2 Lifecycle requirements

Lifecycle requirements cover joiners, movers and leavers. A joiner must have access to their role's standard applications on their first day; a mover's old role access must be removed within five working days of the change; a leaver's access to every integrated application must be removed within four working hours of their HR end date. These numbers come from council policy and audit findings, discussed with HR and service owners. They are ambitious compared with the baseline of nineteen days, which is exactly why they need clear verification and regular measurement after rollout.

### 21.3 Operational requirements

Operational requirements describe what the identity team needs to run the system: monitoring of sign-in success and provider health, documented runbooks, backups of configuration, a test tenant that mirrors production, and a maintenance window for changes. They also cover the service desk: agents must be able to verify a caller's identity using a defined procedure before any reset or recovery. Operational requirements matter because a secure design the small team cannot operate will drift back to insecure habits within months of the project ending.

### 21.4 Prioritisation

Not everything can be delivered at once, so Sana and the council rank requirements as must, should or could, using risk reduction, legal duty and cost. Leaver removal and administrator authentication are musts, because audit findings and threat ranking put them highest. Self-service group requests are a could. Agreeing the ranking in a workshop with directors means that if time or budget runs short, the least important work is dropped first by decision, rather than whatever happens to be scheduled last being quietly abandoned.

### 21.5 Verification methods

Each requirement is verified by inspection, analysis, demonstration or test. Token lifetime is verified by inspecting configuration and testing a token after expiry; leaver removal by measuring time from HR date to removal across real cases; separation of duties by analysing all role assignments with a script. Choosing the method when writing the requirement makes sure it is checkable. The verification results become evidence in the dossier that Sana assembles at the end of the project for the council and her examiners.

### Worked example

Sana's 60 requirements are ranked 22 must, 26 should and 12 could, each with a threat link, a source and a verification method recorded in the traceability matrix.

> **Synthetic case.** Requirements and rankings are synthetic.

### Errors and limits

Requirements without numbers, such as remove leavers promptly, cannot be verified and invite disagreement later.

### Exercises

- **EX061 — Leaver target.** What is the leaver removal requirement? *Rubric:* 3 = all integrated apps within four working hours of HR end date;; 2 = four hours;; 1 = 19 days;; 0 = none.
- **EX062 — Must examples.** Which requirements are ranked must? *Rubric:* 3 = leaver removal and administrator authentication;; 2 = one;; 1 = self-service;; 0 = none.
- **EX063 — SoD verification.** How is separation of duties verified? *Rubric:* 3 = analysing all role assignments with a script;; 2 = analysis;; 1 = interview;; 0 = none.

### Synthesis

Testable, prioritised requirements with chosen verification methods turn audit findings into an achievable programme.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Identity and access management: system and data models

### Learning outcomes

You will (1) model identities, accounts, roles and entitlements; (2) distinguish identity from account; (3) build a role model from evidence.

### 22.1 Identity versus account

An identity is a person or system the council recognises; an account is a record in a particular system that the identity uses. One employee may have a directory account, a payroll account and accounts in several cloud services. Confusing the two causes errors: disabling one account does not remove the person's access elsewhere. Sana's data model has a single identity per person, keyed to the HR record, with every account linked to it. That link is what makes complete leaver removal possible and what the baseline lacks.

### 22.2 Entitlements and roles

An entitlement is one permission or group membership in one system. Roles bundle entitlements that a job function needs. Following the role-based models of Sandhu and colleagues (1996), Sana models users assigned to roles and roles granted entitlements, with a small set of governed exceptions for individual needs. She builds roles from evidence, grouping entitlements that people in the same job actually hold and use, rather than designing them in a meeting from job titles alone, which tends to produce roles that fit nobody exactly.

### Lab — Role summary revisited

```python
"""Summarise synthetic role assignments: members per role and risky permission combinations (stdlib only)."""
from collections import defaultdict
roles = {"clerk": {"view", "payments-raise"}, "clerk-plus": {"view", "payments-raise", "export"}, "approver": {"view", "payments-approve"},
         "manager": {"view", "payments-approve", "reports"}, "manager-temp": {"view", "payments-approve", "reports", "export"},
         "auditor": {"view", "reports"}, "helpdesk": {"view", "reset"}}
assign = {"u01": ["clerk"], "u02": ["clerk"], "u03": ["clerk"], "u04": ["clerk-plus"], "u05": ["approver"], "u06": ["approver"],
          "u07": ["manager"], "u08": ["manager"], "u09": ["manager-temp"], "u10": ["auditor"], "u11": ["helpdesk"], "u12": ["clerk", "approver"]}
members = defaultdict(int)
for u, rs in assign.items():
    for r in rs: members[r] += 1
print(f"accounts={len(assign)} roles={len(roles)}")
for r in roles: print(f"  {r:13} members={members[r]}")
print("single-member roles:", sorted(r for r in roles if members[r] == 1))
for u, rs in sorted(assign.items()):
    p = set().union(*(roles[r] for r in rs))
    if {"payments-raise", "payments-approve"} <= p: print("raise+approve:", u, rs)
```

Run with `python3 lab_roles.py`. Verified output:

```text
accounts=12 roles=7
  clerk         members=4
  clerk-plus    members=1
  approver      members=3
  manager       members=2
  manager-temp  members=1
  auditor       members=1
  helpdesk      members=1
single-member roles: ['auditor', 'clerk-plus', 'helpdesk', 'manager-temp']
raise+approve: u12 ['clerk', 'approver']
```

### 22.3 Reading the model

Revisiting the synthetic summary from chapter 9 with the data model in mind, Sana sees that clerk-plus and manager-temp are variants that exist only because single people needed one extra permission. In her model these become exceptions attached to the identity, with an owner and an expiry date, rather than new roles. The account holding clerk and approver together breaks a separation rule, so the model includes a constraint preventing that combination. The result is fewer roles, explicit exceptions and rules the system can check automatically.

### 22.4 Attributes

Some decisions are better expressed with attributes than roles, such as allowing access to a housing case only for staff in the housing department working in the same area office. NIST SP 800-162 describes attribute-based access control for such cases, and Kuhn, Coyne and Weil (2010) discussed combining attributes with roles. Sana's model keeps roles for coarse access to applications and uses attributes, such as department and location from HR, for finer rules inside applications that support them. Attributes are only as good as their source, so HR data quality becomes a security concern.

### Worked example

The data model links one identity to many accounts, replaces two variant roles with expiring exceptions, adds a raise-approve constraint and uses department and location attributes for case access.

> **Synthetic case.** The model, roles and attributes are synthetic.

### Errors and limits

Treating an account as the person means disabling one account leaves the person's other access untouched.

### Exercises

- **EX064 — Identity definition.** How does an identity differ from an account? *Rubric:* 3 = identity is the person; account is a record in one system;; 2 = person vs record;; 1 = same;; 0 = none.
- **EX065 — Variant role fix.** How are clerk-plus and manager-temp handled in the model? *Rubric:* 3 = replaced by owned, expiring exceptions;; 2 = exceptions;; 1 = kept;; 0 = none.
- **EX066 — Attribute source risk.** Why does HR data quality become a security concern? *Rubric:* 3 = attribute decisions depend on it;; 2 = attributes;; 1 = it does not;; 0 = none.

### Synthesis

Separating identities from accounts and combining evidence-based roles, governed exceptions and attributes gives a model the system can enforce.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Identity and access management: threat and failure analysis

### Learning outcomes

You will (1) analyse identity threats and failures; (2) rank them by likelihood and impact; (3) state residual risk.

### 23.1 Threat analysis

Sana analyses threats to each part of the design: staff credentials, the service desk, the identity provider, its signing keys, integrations and administrator accounts. For each she asks who might attack it, how, and what they would gain, drawing on the threat categories from chapter 15 and on interviews with council staff about past incidents. She records each threat with its likely source, the affected components and evidence for its likelihood, such as audit findings or published guidance, rather than relying only on intuition about what seems dangerous.

### 23.2 Failure analysis

Failures matter as much as attacks. Sana asks what happens when parts break: the identity provider is unreachable, the HR feed stops, a signing certificate expires, or a connector to an application fails silently. For each she records the effect, how it would be detected and the planned response. A provider outage blocks all integrated applications, so she plans emergency access for critical services. A silent connector failure is especially dangerous because leavers would keep access with no alarm raised.

### Lab — Ranking threats and failures

```python
"""Rank synthetic identity threats and failures by likelihood x impact (stdlib only)."""
items = [("Phished password reused at provider", 4, 5), ("Leaver keeps app access", 5, 3), ("Desk reset by impersonation", 3, 4),
         ("Signing certificate expires", 2, 5), ("Over-broad group grant", 4, 3), ("Provider outage at peak", 2, 4),
         ("Stale service account abused", 2, 4), ("Admin console reachable without MFA", 3, 5)]
for name, l, i in sorted(items, key=lambda x: -x[1]*x[2]):
    print(f"{l*i:2}  L={l} I={i}  {name}")
```

Run with `python3 lab_risk.py`. Verified output:

```text
20  L=4 I=5  Phished password reused at provider
15  L=5 I=3  Leaver keeps app access
15  L=3 I=5  Admin console reachable without MFA
12  L=3 I=4  Desk reset by impersonation
12  L=4 I=3  Over-broad group grant
10  L=2 I=5  Signing certificate expires
 8  L=2 I=4  Provider outage at peak
 8  L=2 I=4  Stale service account abused
```

### 23.3 Prioritisation

The synthetic ranking puts a phished password reused at the provider highest at 20, followed by a leaver keeping access and an administrator console reachable without multi-factor at 15. Desk impersonation and over-broad group grants score 12. Certificate expiry scores 10 because its impact is high even though it is unlikely. Sana uses the ranking to order work, but she treats scores as rough: a five-point scale hides uncertainty, and items with the same score may differ greatly. She records the evidence behind each score and revisits the ranking after each incident.

### 23.4 Residual risk

After controls are designed, some risk remains. Phishing-resistant authentication reduces credential theft but does not remove it for staff on legacy applications that cannot use the provider. Prompt leaver removal shrinks the window but does not close it for accounts in systems the connectors do not reach. Sana states each residual risk, why it is acceptable for now and who accepted it. The council's senior information risk owner signs the list, which is reviewed when circumstances change, such as a new application or an incident.

### Worked example

The ranking orders eight synthetic items from 20 down to 8; Sana's work plan tackles provider authentication, leaver removal and administrator protection first, with residual risks signed by the risk owner.

> **Synthetic case.** Scores, items and owners are synthetic.

### Errors and limits

Treating risk scores as precise measurements hides the uncertainty behind a simple scale.

### Exercises

- **EX067 — Top risk.** Which item ranks highest in the lab, with what score? *Rubric:* 3 = phished password reused at provider, 20;; 2 = phishing;; 1 = certificate;; 0 = none.
- **EX068 — Certificate score reason.** Why does certificate expiry score 10 despite being unlikely? *Rubric:* 3 = impact is very high;; 2 = impact 5;; 1 = likely;; 0 = none.
- **EX069 — Silent connector danger.** Why is a silent connector failure especially dangerous? *Rubric:* 3 = leavers keep access with no alarm;; 2 = no alarm;; 1 = speed;; 0 = none.

### Synthesis

Analysing threats and failures together, ranking with evidence and stating residual risk gives the design honest priorities.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Identity and access management: methods I

### Learning outcomes

You will (1) design joiner, mover and leaver processes; (2) design provisioning connectors; (3) plan secure service desk verification.

### 24.1 Joiner, mover, leaver

The lifecycle starts in HR. When HR records a new starter, a feed creates the identity, assigns roles from the job and sends provisioning requests to connected applications. When HR records a job change, the mover process adds the new role's access and schedules removal of the old after a short overlap. When HR records a leaver, every account is disabled at the end date and deleted after a retention period. Sana designs each flow with its triggers, steps, owners and timings, so nothing depends on someone remembering to send an email.

### 24.2 Provisioning connectors

Connectors carry lifecycle changes from the identity system to applications. Modern cloud services often support the SCIM protocol, defined in RFC 7644, which offers a standard way to create, update and disable users. Older applications need custom connectors or scripted exports and imports. Sana classifies each application by connector type and designs error handling: every failed operation is logged, retried and, if still failing, raised to the identity team. A connector that fails silently would undo the whole leaver requirement, so failures must always be visible.

### 24.3 Service desk verification

The service desk is a frequent attack target, because a caller who convinces an agent can get a reset or new authenticator. Sana designs a verification procedure: callers are verified through a method not controlled by the caller, such as a call-back to a number in HR records or a video check against the staff photo, and resets for administrators require a second agent's approval. NIST SP 800-63B-4 treats recovery as part of authenticator management. Agents are trained, and every reset is logged for review.

### 24.4 Exceptions

Some access does not fit roles: a project member who needs a system for three months, or a contractor supporting one application. Sana designs an exception process: the request names the entitlement, the reason, the approver and an expiry date. Exceptions are visible on the identity, reviewed in access reviews and removed automatically when they expire, with a reminder sent to the approver beforehand. Without expiry dates, exceptions become permanent and gradually recreate the excess access the role model was meant to remove.

### Worked example

Sana's lifecycle design has three HR-triggered flows, classifies 140 applications into SCIM, directory-synced, custom and manual connectors, and defines call-back or video verification for desk resets.

> **Synthetic case.** Flows, classifications and procedures are synthetic.

### Errors and limits

A connector that fails silently undoes the leaver requirement without anyone noticing.

### Exercises

- **EX070 — SCIM role.** What does SCIM (RFC 7644) provide? *Rubric:* 3 = standard way to create, update and disable users;; 2 = provisioning standard;; 1 = sign-in;; 0 = none.
- **EX071 — Desk verification method.** Name one caller verification method Sana designs. *Rubric:* 3 = call-back to HR number or video check against photo;; 2 = call-back;; 1 = security question;; 0 = none.
- **EX072 — Exception expiry.** What happens when an exception reaches its expiry date? *Rubric:* 3 = removed automatically after approver reminder;; 2 = removed;; 1 = kept;; 0 = none.

### Synthesis

HR-triggered lifecycle flows, visible connector errors, verified desk procedures and expiring exceptions make access follow employment.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) present an identity design for critique; (2) respond to critique with evidence; (3) record decisions and actions.

### 25.1 Studio work

A design studio is a structured session where Sana presents work in progress and invited peers question it. She brings the architecture diagram, data model, lifecycle flows, threat ranking and a list of open questions. Attendees include Dr Hale, two fellow students, a council application owner and a service desk team leader. Studios catch design problems while they are cheap to fix. Sana's goal is not to defend the design but to discover its weaknesses before staff and auditors do, so she asks attendees to focus on what would break.

### 25.2 Critique received

The service desk leader points out that call-back verification fails for new starters whose phone numbers are not yet in HR records. A fellow student asks what happens to access when HR records a leaver date in error. The application owner notes that some vendors take weeks to support SCIM. Each comment is a hypothesis about a weakness. Sana does not argue in the room; she records each comment, asks clarifying questions and later checks it against evidence, changing the design where the comment holds up.

### 25.3 Responses and trade-offs

For new starters, Sana adds in-person verification with photo identification on the first day. For erroneous leaver dates, she adds a short grace period for disabling, during which HR can reverse the change, balanced against the four-hour requirement by making the grace period one hour. For slow vendors, she accepts scripted daily exports as an interim connector, documented as residual risk. Each trade-off is recorded with the options considered and the reason for the choice, so it can be revisited if circumstances change.

### 25.4 Documentation

After the studio, Sana writes a short record: attendees, material presented, every comment, her response and actions with owners and dates. She sends it to participants to confirm accuracy. The record shows how the design evolved and why, which helps her examiners and anyone who later maintains the system and wonders why there is a one-hour grace period. Short, prompt records are far more useful than long ones written weeks later from fading memory. The record also feeds the decision log used in the thesis.

### Worked example

Three studio comments lead to first-day in-person verification for new starters, a one-hour leaver grace period and interim scripted connectors for slow vendors, all recorded with reasons.

> **Synthetic case.** Studio participants and comments are synthetic.

### Errors and limits

Defending a design in the studio instead of recording and testing comments wastes the session's value.

### Exercises

- **EX073 — New starter gap.** What gap did the service desk leader find? *Rubric:* 3 = call-back fails for new starters without HR phone numbers;; 2 = new starters;; 1 = vague;; 0 = none.
- **EX074 — Grace period.** What grace period does Sana add for leaver disabling? *Rubric:* 3 = one hour, reversible by HR;; 2 = one hour;; 1 = one day;; 0 = none.
- **EX075 — Slow vendor response.** How does Sana handle vendors slow to support SCIM? *Rubric:* 3 = interim scripted daily exports as residual risk;; 2 = scripts;; 1 = wait;; 0 = none.

### Synthesis

Studios expose design weaknesses early, and recorded responses and trade-offs show how the design improved.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Identity and access management: architecture alternatives

### Learning outcomes

You will (1) compare identity architecture alternatives; (2) agree criteria and weights; (3) justify the choice.

### 26.1 Alternatives

Sana compares three architectures. Option A extends the on-premises directory with federation services for applications. Option B moves staff identity to a cloud identity provider, synchronised from HR, with the on-premises directory retained for laptops and legacy systems. Option C, the do-minimum baseline, keeps local accounts but adds multi-factor authentication to the most sensitive applications and a manual monthly leaver check. Including the do-minimum option gives a fair baseline: every more ambitious option must show enough extra benefit to justify its cost and disruption.

### 26.2 Criteria

Criteria are agreed with the council before scoring: security benefit, support for phishing-resistant authentication, ability to meet the leaver requirement, cost over five years, operational effort for a three-person team, disruption during migration and fit with existing skills. Weights reflect council priorities, with security benefit and leaver capability weighted highest. Each criterion has a three-level scale with written descriptions of low, medium and high, so scores are consistent and can be challenged cell by cell rather than as a whole.

### 26.3 Evaluation

Each option is scored with evidence: vendor documentation, a small proof of concept in the test tenant, interviews with the identity team and cost estimates from procurement. Option B scores highest on security and leaver capability and medium on cost. Option A scores well on fit with skills but poorly on operational effort, because the team would maintain more infrastructure. Option C is cheapest but fails the leaver requirement entirely. Sana checks sensitivity: the ranking holds unless cost is weighted far above the council's stated priorities.

### 26.4 Justification

Sana recommends Option B. The justification explains why it best meets the agreed criteria, acknowledges its weaknesses, such as dependence on a cloud provider and the need for strong internet connectivity, and names the evidence that would change the decision, such as a large rise in subscription prices. Writing plainly lets directors understand and approve it, and future engineers can see whether the reasoning still holds if conditions change, rather than inheriting a decision whose basis is lost. Directors approve the recommendation in writing.

### Worked example

Weighted scores rank Option B first, Option A second and Option C last; the ranking survives all weight changes within the council's stated priorities.

> **Synthetic case.** Options, scores and costs are synthetic.

### Errors and limits

Comparing a preferred design only against an obviously weak alternative makes the evaluation unconvincing.

### Exercises

- **EX076 — Do-minimum purpose.** Why include a do-minimum option? *Rubric:* 3 = gives a fair baseline others must beat;; 2 = baseline;; 1 = cheapest;; 0 = none.
- **EX077 — Option C failure.** Which requirement does Option C fail? *Rubric:* 3 = leaver requirement;; 2 = leaver;; 1 = cost;; 0 = none.
- **EX078 — Decision change evidence.** What evidence would change Sana's recommendation? *Rubric:* 3 = e.g. large subscription price rise;; 2 = price;; 1 = vague;; 0 = none.

### Synthesis

Realistic alternatives, agreed criteria, evidence-based scoring and a plain justification produce a defensible architecture choice.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Identity and access management: control design

### Learning outcomes

You will (1) specify authentication, authorisation and session controls; (2) design separation-of-duties checks; (3) design administrator protections.

### 27.1 Authentication policy

Sana specifies authentication policy at the provider. All staff use multi-factor authentication; passkeys on council laptops and phones are the default; security keys serve shared and depot devices. Administrators must use phishing-resistant authenticators at all times. Conditional rules require stronger checks for unusual contexts, such as a new device. Following NIST SP 800-63B-4, she avoids periodic forced password changes, which encourage weak patterns, and instead requires changes when compromise is suspected. Each rule is written in a policy table that both people and test scripts can read.

### 27.2 Separation of duties checks

Separation-of-duties rules are listed as pairs of entitlements that must never be held by one identity, such as raising and approving payments, editing vendor details and approving payments, or editing staff records and running payroll. Sana designs two checks: a preventive check that blocks role assignments creating a conflict, and a detective check that scans all assignments nightly and reports any conflicts that slipped through, for example via exceptions or application-level grants outside the role model. Both checks use the same rule list, so they cannot drift apart.

### Lab — Conflict scan

```python
"""Check synthetic role assignments against separation-of-duties rules (stdlib only)."""
roles = {"clerk": {"pay-raise"}, "approver": {"pay-approve"}, "vendor-admin": {"vendor-edit"}, "payroll": {"payroll-run"},
         "hr-admin": {"staff-edit"}, "auditor": {"audit-read"}}
rules = [("pay-raise", "pay-approve"), ("vendor-edit", "pay-approve"), ("staff-edit", "payroll-run")]
users = {"s01": ["clerk"], "s02": ["clerk", "approver"], "s03": ["approver", "vendor-admin"], "s04": ["payroll"],
         "s05": ["hr-admin"], "s06": ["hr-admin", "payroll"], "s07": ["auditor"], "s08": ["approver"]}
bad = 0
for u, rs in sorted(users.items()):
    p = set().union(*(roles[r] for r in rs))
    for a, b in rules:
        if a in p and b in p: bad += 1; print(f"conflict {u}: {a} + {b} via {rs}")
print(f"users={len(users)} rules={len(rules)} conflicts={bad}")
```

Run with `python3 lab_sod.py`. Verified output:

```text
conflict s02: pay-raise + pay-approve via ['clerk', 'approver']
conflict s03: vendor-edit + pay-approve via ['approver', 'vendor-admin']
conflict s06: staff-edit + payroll-run via ['hr-admin', 'payroll']
users=8 rules=3 conflicts=3
```

### 27.3 Reading the conflicts

The synthetic scan of eight users and three rules finds three conflicts: s02 can raise and approve payments; s03 can edit vendor details and approve payments; s06 can edit staff records and run payroll. Each conflict goes to the relevant manager, who either removes one role or documents a compensating control, such as a second approver for that person's payments, with an expiry date. The detective scan matters because preventive checks only see assignments made through the identity system, not those granted directly inside applications.

### 27.4 Sessions and administrators

Session controls limit how long access lasts: tokens expire within an hour, sessions require re-authentication daily and immediately on sensitive actions, and disabling an identity revokes its sessions. Administrators use separate administrator accounts, not their everyday accounts, sign in only from managed administration workstations, and receive elevated rights just in time for a defined period. Every administrator action is logged to a store the administrators themselves cannot alter. These controls limit what a stolen session or a compromised administrator account can do.

### Worked example

The policy table defines default passkeys, phishing-resistant administrators and no periodic password changes; the conflict scan finds three synthetic conflicts, each resolved or covered by a documented compensating control.

> **Synthetic case.** Policies, users and conflicts are synthetic.

### Errors and limits

Relying only on preventive checks misses conflicts granted directly inside applications.

### Exercises

- **EX079 — Conflict count.** How many conflicts does the lab scan find? *Rubric:* 3 = three: s02, s03, s06;; 2 = three;; 1 = vague;; 0 = none.
- **EX080 — Detective need.** Why is a nightly detective scan needed? *Rubric:* 3 = preventive checks miss grants made inside applications;; 2 = app grants;; 1 = speed;; 0 = none.
- **EX081 — Admin separation.** How are administrator accounts separated? *Rubric:* 3 = separate admin accounts, managed workstations, just-in-time rights;; 2 = separate accounts;; 1 = shared;; 0 = none.

### Synthesis

Clear authentication policy, preventive and detective separation checks, and tight session and administrator controls form the core control design.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Identity and access management: implementation I

### Learning outcomes

You will (1) implement the identity provider in phases; (2) pilot single sign-on and passkeys; (3) enforce policies after monitoring.

### 28.1 Phasing

Sana's implementation plan has phases: build the provider and HR feed; integrate a pilot group of ten applications; enrol pilot staff in passkeys; then roll out by department and application group. Each phase has entry criteria, such as tests passed in the test tenant, and exit criteria, such as sign-in success above an agreed level with no unresolved critical tickets. Lessons from each phase change the next. Phasing limits the number of people affected by any mistake and builds the team's confidence step by step.

### 28.2 Pilot group

The pilot covers the IT department and the planning department, about 180 staff, chosen because IT can troubleshoot and planning uses a mix of old and new applications. Pilot staff agree to report problems through a dedicated channel. Sana holds a short daily check-in with the identity team during the first two weeks. Success criteria are set beforehand, so the decision to proceed rests on evidence rather than impressions, and the pilot's issues are recorded for every later department's preparation.

A failure that only appears in planning's older applications, for example, will surface with 180 staff rather than with the whole council.

### 28.3 Report-only policies

Conditional access policies are first deployed in report-only mode, where the provider records what it would have done without enforcing it. Reviewing these records reveals effects nobody predicted: a scanner that signs in with a shared account, staff who work from a partner building with unusual network addresses and an old mobile app that cannot handle multi-factor prompts. Each is investigated with its owner. Some lead to policy adjustments, while others reveal behaviour that should stop, such as the shared scanner account, which gets its own managed identity.

### 28.4 Enforcement

After report-only review, policies are enforced department by department, at quiet times, with staff informed and the service desk briefed. For the first days, Sana watches sign-in failures and desk tickets closely. Any unexpected block is investigated and fixed by correcting the policy or the device, not by adding a broad exception. Emergency access accounts, excluded from conditional policies but monitored closely, remain available in case a policy error locks out administrators, and their use triggers an immediate alert. Each department's enforcement is confirmed in writing.

### Worked example

The pilot of 180 staff and ten applications reaches 98.9 percent sign-in success; report-only mode exposes a shared scanner account, a partner building and an old mobile app, each resolved before enforcement.

> **Synthetic case.** Departments, applications and figures are synthetic.

### Errors and limits

Enforcing new access policies without a report-only period turns unpredicted effects into outages.

### Exercises

- **EX082 — Pilot departments.** Which departments form the pilot, and why? *Rubric:* 3 = IT and planning: troubleshooting plus mixed applications;; 2 = two;; 1 = all;; 0 = none.
- **EX083 — Report-only meaning.** What does report-only mode do? *Rubric:* 3 = records what would happen without enforcing;; 2 = log only;; 1 = blocks;; 0 = none.
- **EX084 — Emergency account handling.** How are emergency access accounts treated? *Rubric:* 3 = excluded from conditional policies, monitored, use alerts;; 2 = monitored;; 1 = deleted;; 0 = none.

### Synthesis

Phased implementation, a well-chosen pilot, report-only review and careful enforcement bring the design safely into use.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Identity and access management: measurement

### Learning outcomes

You will (1) measure lifecycle and authentication outcomes; (2) compare with baseline using robust summaries; (3) investigate outliers.

### 29.1 What to measure

Measurement follows the success measures agreed in chapter 20: share of applications on single sign-on, share of staff using phishing-resistant authentication, time from HR leaver date to access removal, accounts with no matching employee and password tickets per hundred staff. Each is collected the same way as the baseline, so differences reflect real change rather than a new counting method. Sana documents every query and script used, and stores results with dates, so the comparison can be repeated by the council after her project ends.

### Lab — Leaver removal times

```python
"""Measure synthetic leaver-removal times (hours) before and after automation: median and 90th percentile (stdlib only)."""
import statistics as st
before = [312, 456, 98, 720, 504, 240, 600, 168, 432, 288, 552, 384]
after = [1.5, 2.0, 0.8, 3.5, 1.2, 26.0, 2.2, 1.0, 1.8, 2.6, 0.9, 1.4]
def p90(v): s = sorted(v); return s[int(0.9*(len(s)-1))]
for n, v in [("before", before), ("after", after)]:
    print(f"{n:6} n={len(v)} median_h={st.median(v):.1f} p90_h={p90(v):.1f} over_4h={sum(x > 4 for x in v)}")
```

Run with `python3 lab_review.py`. Verified output:

```text
before n=12 median_h=408.0 p90_h=552.0 over_4h=12
after  n=12 median_h=1.6 p90_h=2.6 over_4h=1
```

### 29.2 Reading the result

In the synthetic sample of twelve leavers, the median time from HR end date to removal falls from 408 hours, about seventeen days, to 1.6 hours. The 90th percentile falls from 552 hours to 2.6 hours. Before automation, all twelve exceeded the four-hour requirement; after, only one did. Sana reports medians and percentiles rather than means because one slow case would distort an average heavily. She also notes the small sample and continues collecting, since twelve leavers cannot show how often rare delays occur.

### 29.3 Investigating the outlier

The one leaver taking twenty-six hours is investigated rather than ignored. Logs show that HR entered the leaver on a Friday evening, the connector to one legacy application failed on a locked account record, and the retry succeeded only on Saturday night. The failure was logged and alerted, but nobody was on call. Sana records two actions: fix the connector's handling of locked records and agree weekend alert handling for leaver failures. Outliers often reveal exactly the weaknesses that averages hide.

### 29.4 Honest reporting

Results go to directors with baseline, target and current value for each measure, plus a short explanation of uncertainty and the outlier. Sana avoids presenting the improvement as complete: some applications remain outside connectors, and accounts in those still depend on manual removal. Honest reporting builds trust, and when a later measurement looks worse, directors understand why instead of losing confidence. It also keeps attention on the remaining work rather than on celebrating the parts that went well. The same format is used every quarter.

### Worked example

Median leaver removal falls from 408 to 1.6 hours and the 90th percentile from 552 to 2.6 hours; one 26-hour outlier reveals a connector bug and a weekend alerting gap.

> **Synthetic case.** Leavers, times and logs are synthetic.

### Errors and limits

Reporting a mean removal time lets one slow case distort the picture in either direction.

### Exercises

- **EX085 — Median change.** How did the median removal time change in the lab? *Rubric:* 3 = 408 to 1.6 hours;; 2 = large fall;; 1 = vague;; 0 = none.
- **EX086 — Over-requirement count.** How many leavers exceeded four hours after automation? *Rubric:* 3 = one of twelve;; 2 = one;; 1 = vague;; 0 = none.
- **EX087 — Outlier causes.** What two actions came from the outlier? *Rubric:* 3 = fix locked-record handling; agree weekend alert handling;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Consistent measurement, robust summaries and investigated outliers show real improvement and the remaining gaps.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) build a test environment for identity; (2) write test cases with expected results; (3) record evidence linked to configuration versions.

### 30.1 Lab setup

The verification laboratory is a separate test tenant of the identity provider, with synthetic users, groups and a handful of test applications, plus a copy of the HR feed using synthetic records. It is isolated from production so tests cannot affect staff. Its configuration comes from the same version-controlled files as production, so tests exercise exactly what will be deployed. Sana documents how to rebuild the lab from scratch, which lets others repeat her tests and lets the council keep using it after she leaves.

### 30.2 Test cases

Each test case states its purpose, the requirement it verifies, the input and the expected result. Examples: a synthetic leaver is marked in HR, and within four hours every test application refuses sign-in; a synthetic clerk is assigned the approver role, and the preventive check blocks it; a token is presented after expiry and is rejected; a token issued for one application is presented to another and is rejected. Cases cover both access that must work and access that must fail, and expected results are written before running.

### 30.3 Evidence

Evidence records what each test did: date, configuration version, input, observed output and pass or fail, with logs attached. A reviewer can confirm a result without rerunning it. Evidence that cannot be linked to a specific configuration version is weak, because it may describe a setup that no longer exists. Sana stores evidence beside the traceability matrix, so each requirement points to its tests and each test to its evidence, forming the chain auditors and examiners will follow. Evidence is retained for the life of the system.

### 30.4 Results

Of 84 test cases in the first round, 79 pass. The five failures include an application that accepts tokens with the wrong audience, a mover whose old access was not removed because of an overlapping exception and a desk procedure step missing from the runbook. Each failure is fixed, retested and recorded. Sana reports failures openly in the results summary; reviewers trust a report that shows honest failures and fixes far more than one in which everything passed first time.

Seventy-nine of 84 is a 94 percent first-round pass rate.

### Worked example

The first verification round passes 79 of 84 tests; five failures, including a wrong-audience token acceptance, are fixed and retested with evidence linked to configuration versions.

> **Synthetic case.** Tests, failures and versions are synthetic.

### Errors and limits

Evidence not linked to a configuration version cannot show that the tested setup is the one in production.

### Exercises

- **EX088 — Lab isolation.** Why is the test tenant isolated from production? *Rubric:* 3 = tests cannot affect staff;; 2 = safety;; 1 = cost;; 0 = none.
- **EX089 — Audience failure.** Which serious failure did the first round find? *Rubric:* 3 = an application accepting wrong-audience tokens;; 2 = audience;; 1 = vague;; 0 = none.
- **EX090 — First round result.** How many tests passed in the first round? *Rubric:* 3 = 79 of 84;; 2 = 79;; 1 = 84;; 0 = none.

### Synthesis

A rebuildable test tenant, tests with expected results and versioned evidence make identity verification trustworthy.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Identity and access management: implementation II

### Learning outcomes

You will (1) extend single sign-on and lifecycle to remaining departments; (2) onboard legacy and supplier access; (3) communicate change to staff.

### 31.1 Department rollout

After the pilot, Sana and the identity team roll out department by department, starting with smaller teams where problems affect fewer people. Each department follows the same checklist: confirm its applications and roles, enrol staff in passkeys during a supported week, enable report-only policies, review findings, enforce, and verify sign-in success and leaver removal. Keeping the checklist identical across departments means any difference in outcome points to something particular to that department, such as unusual devices, rather than to a change in method.

### 31.2 Legacy applications

About twenty applications cannot use modern federation. For some, an application proxy in front of the legacy system lets staff sign in through the provider, while the application still sees a simple header or form login behind the proxy. For others, Sana accepts scripted daily account exports compared against HR, with mismatches sent to the owner. Each legacy application gets a documented plan: proxy, scripted check or replacement, with a date. These are recorded as residual risk until the plan is complete, so they are not forgotten once the main rollout feels finished.

### 31.3 Supplier access

Suppliers who support council systems need access, but only to their own systems. Sana gives each supplier person an individual guest identity linked to a sponsor at the council, requires phishing-resistant authentication or the supplier's own strong sign-in through federation, restricts access to named applications and sets an expiry date tied to the contract. Sponsors confirm continued need every quarter. Shared supplier accounts, which existed for several systems, are removed, because actions under a shared account cannot be traced to a person.

### 31.4 Communication

Staff need to know what changes, when and what to do if something goes wrong. Before each department's rollout, the council sends a short notice with the date, a two-minute video showing passkey enrolment and a contact for help. Floor walkers from the IT team visit on enrolment day. After rollout, a brief follow-up asks staff for feedback. Clear communication reduces desk calls, helps staff report genuine problems quickly and builds goodwill, so security improvements are seen as making work easier rather than as obstacles.

### Worked example

All departments are rolled out over five months with the same checklist; twenty legacy applications receive proxy, scripted-check or replacement plans; eleven shared supplier accounts are replaced by sponsored individual guest identities.

> **Synthetic case.** Departments, applications and suppliers are synthetic.

### Errors and limits

Leaving shared supplier accounts in place means supplier actions cannot be traced to individuals.

### Exercises

- **EX091 — Identical checklist value.** Why keep the rollout checklist identical across departments? *Rubric:* 3 = differences then point to department-specific causes;; 2 = comparability;; 1 = speed;; 0 = none.
- **EX092 — Legacy options.** Name the three plan types for legacy applications. *Rubric:* 3 = proxy, scripted check, replacement;; 2 = two;; 1 = one;; 0 = none.
- **EX093 — Supplier sponsor.** What does each supplier identity link to? *Rubric:* 3 = a council sponsor who confirms need quarterly;; 2 = sponsor;; 1 = contract only;; 0 = none.

### Synthesis

A repeatable rollout, explicit legacy plans, sponsored supplier identities and clear communication carry the design across the whole council.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Identity and access management: reliability

### Learning outcomes

You will (1) model availability of sign-in; (2) identify single points of failure; (3) check independence of redundant parts.

### 32.1 Availability model

When the identity provider sits in front of every application, its availability, and that of the paths to it, bounds the availability of everything. Sana models sign-in for a typical cloud application as components in series: the council's internet link, the provider's service region and the application itself. Components in series multiply their availabilities, so the chain is less available than any one part. Redundant parts in parallel improve availability, since both must fail together for the service to stop. The model shows where investment would reduce downtime most.

### Lab — Sign-in availability

```python
"""Availability of sign-in for a council application: components in series and in parallel (stdlib only)."""
hrs = 8760
comp = {"internet": 0.9990, "provider-region": 0.9995, "hr-feed": 0.9900, "app": 0.9980}
link2 = 0.9970
series = comp["internet"] * comp["provider-region"] * comp["app"]
dual = 1 - (1 - comp["internet"]) * (1 - link2)
with_dual = dual * comp["provider-region"] * comp["app"]
print(f"single link: A={series:.4f} downtime_h={hrs*(1-series):.1f}")
print(f"dual links:  A={with_dual:.4f} downtime_h={hrs*(1-with_dual):.1f}")
print("hr-feed is not in the sign-in path; its outage delays joiners/leavers, not sign-in")
```

Run with `python3 lab_avail.py`. Verified output:

```text
single link: A=0.9965 downtime_h=30.6
dual links:  A=0.9975 downtime_h=21.9
hr-feed is not in the sign-in path; its outage delays joiners/leavers, not sign-in
```

### 32.2 Reading the model

With a single internet link, the synthetic model gives availability of 0.9965, about thirty hours of sign-in downtime a year. Adding a second link from a different provider raises it to 0.9975, about twenty-two hours. The remaining downtime comes mostly from the application and the provider region, which the council does not control. The HR feed is not in the sign-in path at all: its outage delays joiners and leavers rather than stopping sign-in. Sana presents results as hours per year, which directors understand far more easily than percentages.

### 32.3 Independence

Redundancy only helps if failures are independent. Two internet links leaving the building through the same duct, or relying on the same upstream carrier, can fail together. Two provider regions might share a software release that fails everywhere at once. Sana checks for shared causes and records them, because the simple model overstates availability when parts share dependencies. Where independence cannot be achieved, she states the risk plainly in the report rather than letting an optimistic number speak for itself.

### 32.4 Emergency access

Even with redundancy, the provider may become unreachable. Sana designs emergency access for critical services: a small number of emergency administrator accounts with phishing-resistant keys stored in a safe, excluded from conditional policies, and local break-glass procedures for systems such as the emergency planning application. Use triggers alerts and a review. These arrangements are tested twice a year. Emergency access is a reliability control, but it is also a security risk, so it is kept minimal, monitored and documented. Each test result is recorded as evidence.

### Worked example

A second internet link reduces modelled sign-in downtime from about 30.6 to 21.9 hours a year; shared-duct risk is recorded, and emergency access is designed and tested twice yearly.

> **Synthetic case.** Availabilities, links and procedures are synthetic.

### Errors and limits

Assuming redundant links are independent when they share a duct or carrier overstates availability.

### Exercises

- **EX094 — Single-link downtime.** What annual downtime does the single-link model give? *Rubric:* 3 = about 30.6 hours, A=0.9965;; 2 = 30 hours;; 1 = 22;; 0 = none.
- **EX095 — HR feed placement.** Why does an HR feed outage not stop sign-in? *Rubric:* 3 = it is not in the sign-in path, only lifecycle;; 2 = not in path;; 1 = it does;; 0 = none.
- **EX096 — Emergency testing.** How often is emergency access tested? *Rubric:* 3 = twice a year;; 2 = regularly;; 1 = never;; 0 = none.

### Synthesis

Availability models, independence checks and minimal, tested emergency access keep central sign-in reliable.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Identity and access management: safety and resilience

### Learning outcomes

You will (1) identify services where sign-in failure endangers people; (2) design degraded modes; (3) plan recovery and exercises.

### 33.1 Critical services

Some council services affect people's safety: emergency planning, social care case records used during out-of-hours calls and housing repairs for vulnerable tenants. If staff cannot sign in to these, harm could follow. Sana lists critical services with their owners, acceptable outage times and dependencies on identity. Each owner agrees what must happen if sign-in fails. This list guides design choices, such as which applications keep cached access or offline procedures, and the order of recovery after a disruption. The list is reviewed with owners every year.

### 33.2 Degraded modes

A degraded mode is a planned way to continue with reduced function. For out-of-hours social care, staff carry a printed contact list and use a phone line to a duty manager who can access records through an emergency account. For emergency planning, a small set of pre-authorised laptops keep cached credentials valid for a limited time. Degraded modes are written down, rehearsed and still controlled: emergency use is logged and reviewed afterwards, so safety arrangements do not quietly become a permanent way around normal controls.

### 33.3 Recovery

Recovery restores normal sign-in after a disruption. The plan lists steps in order: confirm the cause, restore provider configuration from version control if needed, verify that critical services work first, then the rest, and finally check that monitoring and lifecycle connectors have resumed. Each step has an owner and expected time. Recovery is not complete until leavers processed during the outage have been checked, because a connector backlog could leave people with access they should have lost. Timings are compared with targets after each exercise or real event.

### 33.4 Exercises

Plans are tested through exercises. In a tabletop exercise, the identity team, service desk and two critical service owners walk through a scenario: the provider is unreachable at 08:00 on a Monday. Each participant describes their actions. The exercise reveals that the duty manager's emergency key is stored in a building that is locked at weekends, and that the desk script lacks wording for this case. Findings are recorded, plans updated and the exercise repeated in six months. Exercises are run without blame, so people report gaps honestly.

### Worked example

A tabletop exercise on a Monday-morning provider outage reveals an inaccessible emergency key and a missing desk script; both are fixed and the exercise is scheduled again in six months.

> **Synthetic case.** Services, scenario and findings are synthetic.

### Errors and limits

Degraded modes that are not logged and reviewed can become a permanent route around normal controls.

### Exercises

- **EX097 — Critical example.** Name one council service where sign-in failure could endanger people. *Rubric:* 3 = emergency planning, out-of-hours social care or vulnerable tenant repairs;; 2 = one;; 1 = payroll;; 0 = none.
- **EX098 — Recovery completion.** What must be checked before recovery is complete? *Rubric:* 3 = leavers processed during the outage;; 2 = leaver backlog;; 1 = vague;; 0 = none.
- **EX099 — Exercise finding.** What did the tabletop exercise reveal about the emergency key? *Rubric:* 3 = stored in a building locked at weekends;; 2 = inaccessible;; 1 = lost;; 0 = none.

### Synthesis

Knowing critical services, planning controlled degraded modes, ordered recovery and regular exercises keep people safe when sign-in fails.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Identity and access management: integration

### Learning outcomes

You will (1) integrate identity with logging, HR, the service desk and security monitoring; (2) agree team responsibilities; (3) hand over monitoring.

### 34.1 Logging integration

The provider's sign-in and audit logs must reach the council's central log store with consistent fields and UTC timestamps. Sana maps provider fields to the schema from chapter 13 and tests that synthetic events arrive complete and promptly. She checks that tokens and passwords never appear in logs, and that administrator actions are recorded in a store administrators cannot alter. Gaps found in testing, such as missing device information for some sign-ins, are fixed before the logs are relied on for monitoring or investigations.

### 34.2 HR and service desk integration

HR is the source of truth for joiners, movers and leavers, so the feed's reliability is critical. Sana agrees with HR when changes become effective, how errors are corrected and who is alerted when the feed fails. The service desk tool is integrated so agents can see an identity's status, recent sign-in failures and authenticator registrations without needing administrator rights. Resets and recoveries are logged as tickets linked to the identity, so patterns of repeated recovery, a possible sign of abuse, become visible.

### 34.3 Security monitoring

The council's security monitoring team receives alerts for high-risk identity events: sign-ins combining a new device and unusual location, repeated failed second factors, use of emergency accounts, administrator role activation outside change windows and leaver connector failures. Sana writes a runbook for each alert type with the context to check and the actions to take. Following the base-rate reasoning from chapter 7, alerts combine several signals, so analysts see fewer, more meaningful alerts rather than a flood they learn to ignore.

### 34.4 Teams and handover

Several teams share identity responsibilities: the identity team runs the provider, HR owns the feed, application owners approve access, the service desk handles resets and security monitoring handles alerts. Sana writes a responsibility table and reviews it with each team, so tasks do not fall between them. She runs handover sessions and pairs with identity team members on real changes, because the real test of integration is whether everything keeps working after her project ends and she is no longer there to answer questions.

### Worked example

Five identity alert types with runbooks are handed to security monitoring; the responsibility table assigns each of twelve identity tasks to one owning team.

> **Synthetic case.** Teams, alerts and tasks are synthetic.

### Errors and limits

Integrating alerts without runbooks leaves analysts unsure what to check or do.

### Exercises

- **EX100 — Repeated recovery signal.** Why link resets to identities as tickets? *Rubric:* 3 = patterns of repeated recovery become visible as possible abuse;; 2 = patterns;; 1 = billing;; 0 = none.
- **EX101 — Alert examples.** Name two identity alert types sent to monitoring. *Rubric:* 3 = new device plus unusual location, failed second factors, emergency account use, admin activation, connector failure (two);; 2 = one;; 1 = vague;; 0 = none.
- **EX102 — Integration test.** What is the real test of integration? *Rubric:* 3 = everything keeps working after Sana leaves;; 2 = handover;; 1 = go-live;; 0 = none.

### Synthesis

Clean log integration, a reliable HR feed, desk visibility, meaningful alerts and clear ownership make identity part of everyday operations.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) review what was built against the design; (2) present measured outcomes; (3) agree improvements for the second half of the project.

### 35.1 Reviewing what was built

Halfway through implementation, Sana runs a second design studio with Dr Hale, two council engineers and the service desk leader. The first studio reviewed plans; this one reviews what was actually built. She presents the deployed architecture, measured outcomes, divergences from the design and the exceptions that accumulated during rollout. Comparing the built system with the design shows where reality differed from intention, and those differences are where the most useful lessons for the second half of the project are found.

### 35.2 Divergences

Three divergences stand out. Exceptions grew faster than planned, with 140 active exceptions, a third without a clear business reason. Two legacy applications planned for proxies remain on scripted checks because a vendor upgrade slipped. And conditional access has eleven policies rather than the planned five, as special cases were added during rollout. Each divergence is presented with evidence and its cause, without blame, so the group can decide whether to accept it, correct it or change the design to reflect a better understanding.

### 35.3 Critique and decisions

The group agrees three decisions. Exceptions will be reviewed in a focused campaign, with approvers confirming or removing each within four weeks. Conditional access policies will be consolidated, with test cases written first so consolidation cannot silently change behaviour. The legacy applications remain on scripted checks with monthly owner sign-off until the vendor delivers. The service desk leader adds that recovery requests are rising, so Sana adds a second-passkey campaign to reduce lost-device recoveries. Each decision has a named owner and a date for completion, recorded in the studio notes.

### 35.4 Recording outcomes

Sana records the studio as before: attendees, material, divergences, decisions, owners and dates. She updates the design documents so they describe the system as built, not as originally imagined, and notes each change in the decision log. Keeping documentation in step with reality is easy to postpone and costly to neglect: an engineer who trusts an outdated design document during an incident may take exactly the wrong action under pressure. Participants confirm the record within a week, and it is filed with the earlier studio notes so the design's history stays in one place.

### Worked example

Studio II finds 140 exceptions (one third unexplained), eleven conditional policies and two delayed proxies; decisions include an exception campaign, policy consolidation with tests first and a second-passkey campaign.

> **Synthetic case.** Counts, decisions and participants are synthetic.

### Errors and limits

Leaving design documents describing the intended rather than the built system misleads engineers during incidents.

### Exercises

- **EX103 — Exception growth.** How many exceptions were active, and what share lacked a reason? *Rubric:* 3 = 140, about a third;; 2 = 140;; 1 = few;; 0 = none.
- **EX104 — Consolidation safeguard.** How is policy consolidation kept safe? *Rubric:* 3 = test cases written first;; 2 = tests first;; 1 = vague;; 0 = none.
- **EX105 — Recovery response.** What campaign addresses rising recovery requests? *Rubric:* 3 = second-passkey registration;; 2 = second passkey;; 1 = password reset;; 0 = none.

### Synthesis

Reviewing the built system honestly and updating documents keeps a programme aligned with reality.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Identity and access management: performance and scale

### Learning outcomes

You will (1) estimate provider load from sign-in and refresh rates; (2) plan for growth; (3) test performance safely.

### 36.1 Load components

Provider load has two main parts: interactive sign-ins and application token requests at the morning peak, and background token refreshes through the day as applications renew access. Sana estimates each from staff numbers, applications per person and arrival patterns measured during the pilot. Separating the components matters, because they respond differently to change: adding applications increases both, while lengthening token lifetimes reduces refreshes but increases the time a stolen token remains useful, which is a security trade-off. Both components are measured separately during the pilot.

### Lab — Peak load estimate

```python
"""Estimate identity provider load at the morning peak from synthetic rates (stdlib only)."""
staff, apps, arrive_share, window_s = 2400, 6, 0.60, 600
signin = staff * arrive_share * apps / window_s
refresh = staff * apps * 0.8 / 3600
cap_per_server = 60
for label, f in [("now", 1.0), ("+40% growth", 1.4)]:
    s, r = signin * f, refresh * f; t = s + r
    print(f"{label:12} app sign-ins/s={s:.1f} refresh/s={r:.1f} total/s={t:.1f} one-server utilisation={t/cap_per_server:.0%}")
```

Run with `python3 lab_load.py`. Verified output:

```text
now          app sign-ins/s=14.4 refresh/s=3.2 total/s=17.6 one-server utilisation=29%
+40% growth  app sign-ins/s=20.2 refresh/s=4.5 total/s=24.6 one-server utilisation=41%
```

### 36.2 Reading the estimate

With 2,400 staff, six applications each and sixty percent arriving within ten minutes, the synthetic model gives about 14.4 application sign-ins per second plus 3.2 refreshes, around 17.6 requests per second, or 29 percent of one server's tested capacity. With forty percent growth in staff or applications, load rises to about 24.6 per second, 41 percent. These figures match the earlier calculus estimate and leave room for one server to fail. Sana treats them as estimates to be confirmed by load testing, not as guarantees.

Even after growth, 24.6 requests per second would use 41 percent of one server, so a single surviving server could still carry the load.

### 36.3 Load testing safely

Load tests run only in the test tenant, with synthetic users and the provider's documented testing rules, because generating large volumes of sign-ins against a production cloud service may breach its terms and could affect real staff. Sana ramps load gradually, watching latency percentiles and error rates, and stops at defined limits. The test confirms capacity and reveals a slow group-membership lookup for users with many groups, which is fixed by trimming nested groups in the directory. Results are stored as evidence with the configuration version.

### 36.4 Growth planning

Sana writes a growth plan: review load estimates every six months, recalculate when a large application is integrated and watch the morning-peak 95th percentile latency as an early warning. For cloud providers, capacity is often handled by the vendor, but limits on requests per tenant still apply and must be known. The plan also covers the council's side, such as internet link capacity and the HR feed's processing time, which grow with staff numbers even when the provider itself scales automatically.

### Worked example

The model estimates about 17.6 requests per second now and 24.6 after 40 percent growth; test-tenant load testing confirms capacity and finds a slow lookup for users in many nested groups.

> **Synthetic case.** Rates, capacity and findings are synthetic.

### Errors and limits

Load testing against production cloud identity services can breach terms and affect real staff.

### Exercises

- **EX106 — Peak estimate.** What total peak load does the lab estimate now? *Rubric:* 3 = about 17.6 requests per second, 29%;; 2 = 17.6;; 1 = 4.4;; 0 = none.
- **EX107 — Lifetime trade-off.** What is the trade-off in lengthening token lifetimes? *Rubric:* 3 = fewer refreshes but stolen tokens useful longer;; 2 = security vs load;; 1 = vague;; 0 = none.
- **EX108 — Load test finding.** What did load testing reveal? *Rubric:* 3 = slow lookup for users with many nested groups;; 2 = nested groups;; 1 = vague;; 0 = none.

### Synthesis

Separating load components, confirming estimates in a test tenant and planning growth keep sign-in fast as the council grows.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Identity and access management: operations

### Learning outcomes

You will (1) run routine identity operations; (2) handle incidents involving identity; (3) manage changes and access reviews.

### 37.1 Routine operations

Daily identity operations include checking the HR feed and connector status, reviewing failed provisioning operations, handling exception requests and watching sign-in success and alert queues. Weekly tasks include reviewing emergency account use and administrator activations. Monthly tasks include certificate expiry checks and a report on success measures. Sana writes each task in a runbook with steps, expected results and escalation contacts, so the three-person team can share the work and cover absences without relying on memory. Runbooks are reviewed after every incident and at least yearly.

### 37.2 Identity incidents

When a staff account is suspected compromised, the response follows a runbook: confirm signals with the user through a trusted channel, revoke sessions and tokens, reset or re-register authenticators with verified identity, review recent activity for actions taken, and inform the security team. Revoking sessions matters because disabling a password alone does not end existing sessions. Each incident is recorded with timeline and lessons. Sana practises the runbook with synthetic scenarios in the test tenant so the team acts quickly when a real case arrives.

### 37.3 Change management

Identity changes follow the process designed in chapter 14: version control, review, automated tests and staged deployment. Operations adds a change calendar, so changes avoid busy periods such as payroll week, and a rule that conditional access changes require a second approver. Emergency changes are allowed but reviewed within two working days. Sana measures change failure rate, the share of changes needing rollback, as an indicator of whether the process is working or being bypassed under pressure. Trends in this rate are reviewed monthly.

### 37.4 Access reviews

Quarterly access reviews ask managers to confirm each team member's roles and exceptions. Drawing on lessons that approve-all reviews achieve little, Sana designs reviews that show plain-language descriptions, last-use dates and highlights for unused or conflicting access, and keep each manager's list short by excluding standard role access already governed by HR job data. Removals happen automatically when a manager rejects an item. Completion rates and removals are reported, so reviews are judged by what they change, not by how many clicks they collect.

### Worked example

Runbooks cover twelve daily, weekly and monthly tasks; a synthetic compromise drill completes session revocation in nine minutes; the first improved access review removes 7 percent of reviewed items.

> **Synthetic case.** Tasks, drills and figures are synthetic.

### Errors and limits

Disabling a password without revoking sessions leaves an attacker's existing session active.

### Exercises

- **EX109 — Session revocation reason.** Why must sessions be revoked in a compromise? *Rubric:* 3 = disabling password alone does not end existing sessions;; 2 = sessions persist;; 1 = speed;; 0 = none.
- **EX110 — Change failure rate.** What does change failure rate measure? *Rubric:* 3 = share of changes needing rollback;; 2 = rollbacks;; 1 = speed;; 0 = none.
- **EX111 — Review design.** Name two features of Sana's improved access reviews. *Rubric:* 3 = plain descriptions, last-use dates, highlights, short lists, automatic removal (two);; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Runbooks, practised incident response, disciplined change and meaningful access reviews keep identity secure day to day.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Identity and access management: validation

### Learning outcomes

You will (1) validate that the system meets stakeholders' real needs; (2) gather user evidence; (3) compare with original goals.

### 38.1 Verification versus validation

Verification asks whether the system meets its written requirements; validation asks whether it meets the real needs of the council and its staff. A system can pass every test and still fail people, for example if passkey enrolment works but depot staff find it impractical in their conditions. Sana plans validation separately: interviews with staff from different departments, observation of sign-in at a depot and in a social care office, and review of desk tickets for recurring frustrations that requirements did not anticipate.

### 38.2 User evidence

Sana interviews twenty staff across roles and observes sign-in in three locations. Most office staff find passkeys faster than passwords. Depot staff report that security keys work but are easily left in vans. Social care staff value single sign-on but dislike re-authentication before viewing sensitive records during visits. She records each finding with its source and frequency, distinguishing widespread issues from individual preferences, and treats interviews as evidence alongside numbers rather than as anecdotes to be dismissed. Findings are shared with participants for confirmation.

### 38.3 Comparing with goals

Returning to the problem statement in chapter 20, Sana checks each goal. One strong sign-in for all applications: met for 120 of 140 applications, with plans for the rest. Role-based access with governed exceptions: met, though exceptions need continued attention. Prompt removal of leavers: met for integrated applications. Evidence that these happen: met through measurement and the verification dossier. She states where goals are only partly met and why, which gives directors an accurate picture rather than a celebration. The comparison is repeated each year.

### 38.4 Acting on validation

Validation leads to changes. Depot staff receive key holders attached to their high-visibility jackets. Social care re-authentication is adjusted so a recent phishing-resistant sign-in on a managed device satisfies the sensitive-records check for a limited period, after a risk discussion with the service owner. Recurring desk tickets about enrolling new phones lead to a self-service guide. Each change goes through normal change control and is recorded, so validation produces improvements rather than just a report. Follow-up interviews check whether the changes helped.

### Worked example

Validation with twenty interviews and three observations leads to key holders for depot staff, adjusted social care re-authentication on managed devices and a self-service phone guide; 120 of 140 applications meet the single sign-on goal.

> **Synthetic case.** Interviews, findings and counts are synthetic.

### Errors and limits

Treating a system that passes all tests as finished ignores whether it serves people in their real conditions.

### Exercises

- **EX112 — Validation definition.** How does validation differ from verification? *Rubric:* 3 = validation checks real needs; verification checks written requirements;; 2 = needs vs requirements;; 1 = same;; 0 = none.
- **EX113 — Depot finding.** What did depot staff report about security keys? *Rubric:* 3 = they work but are left in vans;; 2 = forgotten;; 1 = broken;; 0 = none.
- **EX114 — SSO coverage.** How many applications meet the single sign-on goal? *Rubric:* 3 = 120 of 140;; 2 = 120;; 1 = 140;; 0 = none.

### Synthesis

Validation with real user evidence checks the system against actual needs and drives practical improvements.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Identity and access management: maintainability

### Learning outcomes

You will (1) keep identity configuration understandable over time; (2) control drift and sprawl; (3) plan documentation and knowledge transfer.

### 39.1 Configuration sprawl

Identity systems accumulate settings: groups, policies, application integrations and exceptions. Without care they become hard to understand, and nobody dares remove anything. Sana measures sprawl with simple counts tracked monthly: number of groups, groups without owners, conditional policies, applications without a named owner and active exceptions. Rising counts without matching business change signal that maintainability is slipping. Making sprawl visible lets the team decide deliberately what to clean up before it becomes unmanageable. The counts are shown in the monthly report to directors alongside the success measures.

### 39.2 Drift detection

Drift happens when production differs from version-controlled configuration, usually because someone made a quick change in the administration console. Sana schedules a nightly comparison between exported production settings and the repository. Differences raise a ticket: either the change is added to the repository through normal review, or it is reverted. Drift detection keeps the repository trustworthy as the single description of the system, which is essential for recovery, audits and anyone trying to understand why access behaves as it does.

### 39.3 Naming and ownership

Every group, role, policy and application integration follows a naming convention showing its purpose and owner, such as role-finance-clerk or app-payroll-users. Each has a named owning team and a review date. Objects without owners are flagged in the monthly report and either adopted or removed. Clear names and owners make reviews faster, because reviewers understand what they see, and they make cleanup safe, because someone can confirm whether an object is still needed before it is deleted. New objects cannot be created without both.

### 39.4 Knowledge transfer

Maintainability depends on people as much as configuration. Sana writes an operations guide explaining the architecture, the reasons behind key decisions, the runbooks and how to change things safely. She records short walkthrough videos of common tasks and pairs with each identity team member on real changes. The decision log from her studios explains why things are as they are. These materials matter because the identity team will change over the years, and new members must be able to work safely without her.

### Worked example

Monthly sprawl metrics track five counts; nightly drift detection finds four console changes in its first month, three added to the repository after review and one reverted.

> **Synthetic case.** Counts and drift events are synthetic.

### Errors and limits

Allowing console edits without drift detection makes the repository an unreliable description of production.

### Exercises

- **EX115 — Sprawl metrics.** Name three sprawl counts Sana tracks. *Rubric:* 3 = groups, ownerless groups, policies, ownerless apps, exceptions (three);; 2 = two;; 1 = one;; 0 = none.
- **EX116 — Drift outcome.** What happened to the four drift findings? *Rubric:* 3 = three added via review, one reverted;; 2 = resolved;; 1 = ignored;; 0 = none.
- **EX117 — Naming example.** Give an example of Sana's naming convention. *Rubric:* 3 = role-finance-clerk or app-payroll-users;; 2 = example;; 1 = vague;; 0 = none.

### Synthesis

Visible sprawl metrics, drift detection, clear naming and ownership, and good knowledge transfer keep identity maintainable.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) run a second, broader verification round; (2) test failure and recovery paths; (3) produce final verification evidence.

### 40.1 Broader scope

The second verification round extends beyond the first round's functional checks. It adds failure and recovery tests, such as HR feed interruption and connector failure, security regression tests for every earlier failure, tests of emergency access and tests of the improved access review. Sana updates the test catalogue from the traceability matrix so every must and should requirement has at least one test. The round runs in the test tenant using the current configuration version from the repository. Results are compared with the first round.

### 40.2 Failure path tests

Failure tests check that the system fails safely. When the HR feed stops, the system must raise an alert within an hour and must not treat missing staff as leavers and disable everyone. When a connector fails, failed operations must be retried and alerted. When a signing certificate is near expiry, alerts must fire at ninety, thirty and seven days. Sana designs each test with a synthetic trigger and an expected result, because failure handling that has never been tested usually does not work when needed.

### 40.3 Regression tests

Every failure from the first round becomes a permanent regression test. The wrong-audience token test runs against every integrated application, not only the one that failed, because the same mistake could exist elsewhere. The mover with an overlapping exception is turned into a family of tests covering different exception timings. Regression tests run automatically on each change, so a fix cannot silently be undone months later by an unrelated update to an application or policy. The regression suite grows with every fixed failure.

### 40.4 Final evidence

The second round runs 148 tests, and 146 pass. One failure is an alert that fires at thirty days but not at ninety; the other is an application that accepts a token two minutes after expiry because of clock tolerance set too generously. Both are fixed and retested. Evidence for every test is stored with its configuration version and linked from the traceability matrix. Sana summarises results by requirement, listing any residual risks accepted by the council, ready for the evidence dossier.

### Worked example

The second round passes 146 of 148 tests; the two failures, a missing ninety-day certificate alert and a too-generous clock tolerance, are fixed and retested.

> **Synthetic case.** Tests, failures and versions are synthetic.

### Errors and limits

Failure handling that has never been tested usually fails when it is needed.

### Exercises

- **EX118 — Feed failure rule.** What must not happen when the HR feed stops? *Rubric:* 3 = treating missing staff as leavers and disabling everyone;; 2 = mass disable;; 1 = alert;; 0 = none.
- **EX119 — Second round result.** How many tests passed in the second round? *Rubric:* 3 = 146 of 148;; 2 = 146;; 1 = 148;; 0 = none.
- **EX120 — Clock tolerance.** What did the clock tolerance failure allow? *Rubric:* 3 = tokens accepted two minutes after expiry;; 2 = late tokens;; 1 = vague;; 0 = none.

### Synthesis

Broader verification with failure paths and permanent regression tests produces final evidence the council can rely on.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Identity and access management: system optimization

### Learning outcomes

You will (1) reduce unnecessary roles, groups and exceptions; (2) streamline policies without weakening them; (3) measure the effect of optimisation.

### 41.1 What to optimise

After rollout, Sana looks for ways to make the system simpler and cheaper to run without weakening security. Candidates include roles that differ only slightly, groups with no members or owners, exceptions that have become routine and could be folded into a role, conditional policies that overlap, and application integrations still using older settings. Optimisation is guided by evidence from monthly sprawl metrics and access reviews, and every candidate is checked with its owner before any change is made. Candidates are ranked by expected effort saved.

### 41.2 Role consolidation

Using assignment and usage data, Sana finds roles whose members hold almost identical entitlements. Where two roles differ by one rarely used permission, she proposes merging them and handling that permission as an exception for the few who need it. Role mining research, such as Molloy and colleagues (2008), emphasises keeping roles meaningful to the business rather than purely statistical, so each proposed merge is discussed with the department that owns the roles. The finance roles shrink from fourteen to eight without changing anyone's needed access.

### 41.3 Policy streamlining

The eleven conditional access policies noted in studio II are consolidated to six. Before changing anything, Sana writes test cases capturing current intended behaviour for representative synthetic users and contexts. She then rewrites the policies and runs the tests, confirming that every intended outcome is preserved and that two unintended gaps, where certain devices escaped multi-factor prompts, are now closed. Writing tests first is what makes the optimisation safe, because simplification without tests can quietly weaken controls. The tests then join the permanent regression suite.

### 41.4 Measuring the effect

Sana measures the results: the number of roles, policies and exceptions; time spent on access reviews per manager; and identity team hours spent on routine tasks. Reviews take about a quarter less time because lists are shorter and clearer. She also checks that security measures have not worsened, such as leaver removal times and conflict counts. Optimisation is only a success if it reduces effort and complexity while keeping or improving security, so both sides are reported together. Results are compared with the baseline taken before optimisation.

### Worked example

Finance roles fall from fourteen to eight, conditional policies from eleven to six with two gaps closed, and access review time per manager drops by about a quarter, with security measures unchanged or improved.

> **Synthetic case.** Roles, policies and timings are synthetic.

### Errors and limits

Simplifying policies without first capturing intended behaviour in tests can quietly weaken controls.

### Exercises

- **EX121 — Finance roles.** How many finance roles remain after consolidation? *Rubric:* 3 = eight, down from fourteen;; 2 = eight;; 1 = fourteen;; 0 = none.
- **EX122 — Policy gaps closed.** What did policy consolidation also fix? *Rubric:* 3 = two gaps where devices escaped MFA prompts;; 2 = gaps;; 1 = vague;; 0 = none.
- **EX123 — Optimisation success test.** When is optimisation a success? *Rubric:* 3 = less effort and complexity with security kept or improved;; 2 = both;; 1 = cost only;; 0 = none.

### Synthesis

Evidence-based consolidation, tests written first and measurement of both effort and security make optimisation safe.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Identity and access management: applied research

### Learning outcomes

You will (1) frame a small applied research question from the project; (2) design a fair comparison; (3) report results with limits.

### 42.1 A research question

Sana's project raises a question worth studying carefully: does showing last-use dates in access reviews increase the share of unneeded access removed? Herley (2009) argued that people reject security effort whose cost exceeds its visible benefit, which suggests that making benefit visible might change reviewer behaviour. She frames the question narrowly, defines removal rate as the share of reviewed items removed and later confirmed as unneeded, and agrees with the council to use the next quarterly review as the setting.

Requiring confirmation that removed items were unneeded guards against a removal rate inflated by deleting access people still use.

### 42.2 Design

Departments are split into two groups at random: one sees last-use dates in its review, the other sees the review without them. Both use the same descriptions and list lengths. Removal decisions are checked afterwards by application owners, who do not know which group a department was in, to classify each removal as correct or wrong. Wrong removals, which must be reversed, are counted as harm. Ethical approval from the institute covers the study, and managers are told that review design is being evaluated.

### 42.3 Results

In the synthetic results, departments shown last-use dates remove 11 percent of reviewed items, against 5 percent without them, with a similar rate of wrong removals in both groups. With only twelve departments, the uncertainty is large, so Sana reports the difference with an interval and avoids claiming a precise effect. She also notes that managers in the dates group spent slightly longer per item, which matters for adoption. The finding supports showing last-use dates, but it should be confirmed in further review cycles.

### 42.4 Limits and use

Sana lists limits: one organisation, one cycle, small numbers, and the possibility that managers discussed the study across groups. Despite these, the result is useful: it supports a low-cost change and gives the council a method to keep testing review improvements. She writes the study as a chapter of her thesis and as a short practitioner note, distinguishing what the evidence shows from what it suggests, so readers do not take a promising early result for settled knowledge. A second cycle is planned to check the result.

### Worked example

A randomised comparison across twelve departments finds 11 percent versus 5 percent removal with similar wrong-removal rates; Sana reports it with an interval and clear limits.

> **Synthetic case.** Departments, rates and outcomes are synthetic.

### Errors and limits

Reporting a small study's difference without uncertainty presents a promising signal as an established effect.

### Exercises

- **EX124 — Removal rate definition.** How does Sana define removal rate? *Rubric:* 3 = share of reviewed items removed and confirmed unneeded;; 2 = removals;; 1 = clicks;; 0 = none.
- **EX125 — Blinded checkers.** Who checks removals without knowing the group? *Rubric:* 3 = application owners;; 2 = owners;; 1 = Sana;; 0 = none.
- **EX126 — Study result.** What removal rates does the study find? *Rubric:* 3 = 11% with dates vs 5% without;; 2 = both;; 1 = one;; 0 = none.

### Synthesis

Small, fair applied studies can improve identity practice when results are reported with honest uncertainty and limits.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a public-service organisation's governance; (2) manage stakeholders and procurement; (3) reflect on professional practice.

### 43.1 Public-service context

Working inside a council differs from a classroom exercise. Decisions pass through governance boards, budgets follow annual cycles, and services must keep running for residents throughout. Sana attends the council's digital board monthly, presenting progress against success measures and risks. She learns to frame proposals in terms of service outcomes, such as fewer locked-out care workers, and legal duties, such as protecting residents' personal data, rather than technical features, because those are the terms in which board members make decisions.

### 43.2 Stakeholders

Many people have a stake in identity changes: HR, service owners, unions, the service desk, auditors and staff themselves. Sana keeps a stakeholder map recording each group's interests and concerns. The union raised a worry that sign-in logs might be used to monitor productivity; Sana works with HR to write a clear statement limiting their use to security and operations, which the union accepts. Listening early to concerns avoids opposition later that could have stalled the whole programme. The map is updated as new concerns arise.

### 43.3 Procurement and suppliers

The identity provider and some connectors are bought services. Sana helps write requirements for procurement, focused on outcomes such as support for phishing-resistant authentication, standard protocols like OpenID Connect, SAML and SCIM, exportable logs and clear limits on the supplier's access to council data. She learns that procurement rules require fair comparison of bidders and documented scoring, much like her architecture evaluation. Contracts include security obligations, such as prompt notification of breaches, that the council can enforce. Scoring records are kept for audit.

### 43.4 Reflection on practice

Sana keeps a reflective log during her placement, noting situations where technical correctness was not enough: a well-designed policy delayed because a director was not briefed, a rollout smoothed by floor walkers more than by documentation. Professional practice combines technical skill with communication, patience and respect for the people affected. She also records ethical moments, such as declining to share an individual's sign-in history with a manager without proper authorisation, and how she handled them. The log becomes evidence of professional development in her thesis.

### Worked example

Sana presents monthly to the digital board, resolves a union concern with a written statement on log use, and helps procurement score bidders on standards support and data access limits.

> **Synthetic case.** Boards, stakeholders and suppliers are synthetic.

### Errors and limits

Presenting identity work to boards as technical features rather than service outcomes makes approval harder.

### Exercises

- **EX127 — Union concern.** What concern did the union raise? *Rubric:* 3 = logs used to monitor productivity;; 2 = monitoring;; 1 = pay;; 0 = none.
- **EX128 — Procurement outcomes.** Name two outcomes Sana's procurement requirements stress. *Rubric:* 3 = phishing-resistant auth, standard protocols, exportable logs, limited supplier data access (two);; 2 = one;; 1 = price;; 0 = none.
- **EX129 — Ethical refusal.** What request did Sana decline? *Rubric:* 3 = sharing an individual's sign-in history without authorisation;; 2 = sharing logs;; 1 = vague;; 0 = none.

### Synthesis

Public-service practice requires governance awareness, stakeholder care, sound procurement and reflective professionalism.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define the capstone scope from remaining gaps; (2) plan work and evidence; (3) begin delivery with clear milestones.

### 44.1 Choosing the scope

The capstone draws on everything so far. Sana chooses to close the largest remaining gap: the twenty applications outside full single sign-on and automated lifecycle. Her scope is to bring at least twelve of them under the provider with automated leaver removal and to put the rest on documented, monitored interim controls. The scope is agreed with Dr Hale and the council, with clear success criteria, because a capstone without boundaries tends to expand until nothing is finished well. The criteria are written into the plan.

### 44.2 Planning

Sana plans the work in milestones: classify each application and its options; build proxies or connectors in the test tenant; verify with tests; migrate users in small groups; and measure leaver removal for each. Each milestone has deliverables and evidence requirements, linked to the traceability matrix. She identifies dependencies, such as vendor support for SCIM and a proxy licence, and risks, such as a vendor delay, with planned responses. The plan is reviewed fortnightly with her supervisor and the identity team lead.

### 44.3 Early delivery

The first milestone classifies the twenty applications: seven can use the provider through a proxy, five have new vendor versions supporting standard federation and provisioning, four need scripted checks permanently and four are due for retirement within a year. Sana starts with two proxy applications in the test tenant, because they share a pattern and success there will speed the others. She records time spent per application, so later estimates are based on measured effort rather than guesses. Measured effort per application improves later estimates.

### 44.4 Managing risk

Two weeks in, a vendor announces that its federation-capable version is delayed by three months. Sana updates the plan: that application moves to the interim group with a monitored scripted check, and another application from the proxy group takes its place to keep the target achievable. She records the change, its reason and its effect on the capstone scope in the decision log, and informs the council. Adapting openly to risks is part of engineering; pretending the plan is unchanged is not.

### Worked example

Twenty applications are classified as 7 proxy, 5 modern federation, 4 permanent scripted check and 4 retiring; a vendor delay moves one application to interim controls without changing the target of twelve.

> **Synthetic case.** Applications, vendors and timings are synthetic.

### Errors and limits

Hiding a plan change caused by a supplier delay leaves stakeholders with false expectations.

### Exercises

- **EX130 — Capstone target.** What is the capstone's main target? *Rubric:* 3 = at least twelve of twenty apps under provider with automated leaver removal;; 2 = twelve;; 1 = all;; 0 = none.
- **EX131 — Classification counts.** How are the twenty applications classified? *Rubric:* 3 = 7 proxy, 5 modern, 4 scripted, 4 retiring;; 2 = four groups;; 1 = one;; 0 = none.
- **EX132 — Delay response.** How does Sana respond to the vendor delay? *Rubric:* 3 = move app to interim, substitute another, record and inform;; 2 = adapt;; 1 = wait;; 0 = none.

### Synthesis

A bounded capstone with milestones, evidence requirements and openly managed risks gives the final year a solid structure.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) obtain an independent review of the capstone design; (2) respond to findings; (3) strengthen the evidence.

### 45.1 Why independent review

An independent reviewer, not involved in the project, examines the capstone design and evidence. Sana arranges a review by an identity architect from another public body, under a confidentiality agreement and using redacted material. Independent eyes catch assumptions that people close to the work no longer notice. The reviewer is asked to judge whether the design meets its requirements, whether evidence supports the claims, and whether any significant risk has been missed or understated in the residual risk register. Its findings are recorded formally.

### 45.2 Findings

The reviewer raises four findings. Proxy applications rely on headers that the proxy adds, so the application must reject any request not coming through the proxy; this is not yet tested. Emergency access accounts are excluded from all conditional policies, including logging alerts for one policy. The residual risk for scripted checks understates the window during which a leaver retains access. And the decision log lacks the reason for one token lifetime choice. Each finding comes with evidence and a suggested severity.

### 45.3 Responses

Sana responds to each finding in a table: the finding, her assessment, the action and the evidence of completion. She adds tests confirming that proxied applications refuse direct requests, corrects the emergency account exclusion so alerts still fire, revises the residual risk statement with a measured window of up to twenty-four hours and adds the missing decision record. Where she disagrees with a severity, she explains why with evidence. The reviewer confirms the responses, and the record goes into the evidence dossier.

### 45.4 Learning from review

Sana reflects that two findings concerned assumptions she had stopped questioning: that nobody could reach a proxied application directly and that emergency account exclusions were harmless. Independent review is valuable precisely because it targets such blind spots. She recommends that the council arrange independent review for future major identity changes and adds a review step to the change process for high-risk changes, so the benefit continues after her project. She also adds both assumptions to the design checklist, so future engineers test them explicitly rather than relying on memory.

### Worked example

Four independent findings lead to direct-access tests for proxied applications, restored alerts for emergency accounts, a corrected residual risk window and a completed decision log.

> **Synthetic case.** Reviewer, findings and responses are synthetic.

### Errors and limits

Assuming that a proxied application cannot be reached directly leaves a path around the provider untested.

### Exercises

- **EX133 — Proxy finding.** What must a proxied application do according to the review? *Rubric:* 3 = reject requests not coming through the proxy;; 2 = reject direct;; 1 = vague;; 0 = none.
- **EX134 — Residual window.** What leaver window does the revised residual risk state for scripted checks? *Rubric:* 3 = up to twenty-four hours;; 2 = 24h;; 1 = vague;; 0 = none.
- **EX135 — Lasting change.** What lasting process change does Sana recommend? *Rubric:* 3 = independent review step for high-risk identity changes;; 2 = review step;; 1 = vague;; 0 = none.

### Synthesis

Independent review targets blind spots, and evidenced responses turn findings into stronger design and evidence.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) complete capstone delivery; (2) verify and measure outcomes; (3) hand over remaining work.

### 46.1 Completing migrations

Sana completes the capstone migrations in small groups, each with report-only checks first, a defined rollback and verification afterwards. By the end, thirteen of the twenty applications are under the provider with automated leaver removal, one more than the target. Each migration's evidence includes test results, the configuration version and a sample of leaver removals measured after go-live. Staff for each application receive notices beforehand and a contact for problems, following the communication pattern from earlier rollouts. Each completion is confirmed with the owner.

### 46.2 Measuring outcomes

Sana measures outcomes for the capstone applications: median leaver removal time falls from about a week under the old manual process to under two hours; the number of accounts with no matching employee in these applications drops from 47 to 2, both explained by pending HR corrections; and password tickets for these applications fall noticeably. She reports results with baselines, sample sizes and limits, such as the short measurement period for the last applications migrated. Measurement continues after handover, now run by the identity team.

### 46.3 Interim controls

The seven applications not migrated have documented interim controls: scripted daily checks against HR, alerts on mismatches, monthly owner sign-off and a planned date for migration or retirement. Sana tests that the scripted checks actually detect a synthetic leaver and that alerts reach the identity team. Interim controls are recorded in the residual risk register with owners. This ensures that applications outside the main design are still governed rather than silently forgotten once the project's attention moves on. Each control is reviewed monthly by its owner.

### 46.4 Handover

Sana hands over the capstone to the identity team with updated documentation, runbooks for proxies and new connectors, the test suite and evidence. She walks through each migrated application with the team lead and agrees who owns the remaining interim applications. A short handover checklist confirms that monitoring, alerts and access reviews cover the new integrations. The council's acceptance of the handover is recorded, closing the capstone formally and providing a clear end point for the thesis. Open questions are listed with owners.

### Worked example

Thirteen of twenty applications are migrated, one above target; median leaver removal falls from about a week to under two hours and ownerless accounts from 47 to 2; seven applications remain on tested interim controls.

> **Synthetic case.** Applications, counts and times are synthetic.

### Errors and limits

Declaring success at go-live without measuring leaver removal afterwards leaves the main requirement unverified.

### Exercises

- **EX136 — Migrated count.** How many applications were migrated in the capstone? *Rubric:* 3 = thirteen of twenty, one above target;; 2 = thirteen;; 1 = twelve;; 0 = none.
- **EX137 — Ownerless accounts change.** How did ownerless accounts change in capstone applications? *Rubric:* 3 = 47 to 2, both pending HR corrections;; 2 = 47 to 2;; 1 = vague;; 0 = none.
- **EX138 — Interim test.** How are interim scripted checks verified? *Rubric:* 3 = a synthetic leaver is detected and alerts reach the team;; 2 = synthetic test;; 1 = assumed;; 0 = none.

### Synthesis

Careful migration, measured outcomes, tested interim controls and a formal handover complete the capstone.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) run a controlled failure and recovery trial; (2) measure recovery against targets; (3) record lessons.

### 47.1 Trial design

Before the project ends, Sana runs a controlled trial of failure and recovery in the test tenant, mirroring production configuration. Scenarios include loss of the HR feed for a day, a connector outage during a busy leaver period, an expired signing certificate and an unreachable provider requiring emergency access. Each scenario has a trigger, expected behaviour, recovery steps and target times. The council's identity team runs the recovery while Sana observes, because the aim is to test whether the team, not just the technology, can recover.

### 47.2 Running the trial

The trial runs over two days. The HR feed loss raises an alert within forty minutes, and no staff are wrongly disabled. The connector outage queues twelve synthetic leaver operations, which complete within thirty minutes of restoration. The expired certificate stops sign-in in the test tenant; renewal and publication take fifty-five minutes against a target of one hour. Emergency access works, but the team takes twenty minutes to locate the correct runbook page, longer than expected under pressure. All timings are logged for later analysis.

### 47.3 Measuring against targets

Sana tabulates each scenario against its target time and expected behaviour. Three of four meet targets; the certificate renewal meets it narrowly. The emergency access scenario meets the functional goal but reveals a usability problem with the runbook. She reports these as measurements, not impressions, and links each to the requirement it tests. Narrow margins are treated as warnings: a renewal that takes fifty-five minutes in a calm trial may take longer during a real incident at night. Results are shared with the council.

### 47.4 Lessons

Lessons become actions: the runbook gets a one-page emergency card at the front; certificate renewal is automated further to shorten it; and the trial is scheduled annually. Sana also notes a positive lesson: the failure-safe design for the HR feed worked exactly as intended, justifying the effort spent designing it. Lessons are recorded in the decision log and the operations guide. Trials like this build confidence that the system and team can handle real failures, which is the purpose of resilience engineering.

### Worked example

Three of four failure scenarios meet targets; certificate renewal takes 55 of 60 minutes and emergency access takes twenty minutes to find the runbook, leading to automation and a one-page emergency card.

> **Synthetic case.** Scenarios, times and outcomes are synthetic.

### Errors and limits

Testing only the technology and not the team's ability to recover overstates resilience.

### Exercises

- **EX139 — Feed loss outcome.** What happened in the HR feed loss scenario? *Rubric:* 3 = alert within forty minutes, nobody wrongly disabled;; 2 = safe failure;; 1 = mass disable;; 0 = none.
- **EX140 — Certificate timing.** How long did certificate renewal take against its target? *Rubric:* 3 = 55 minutes vs 60;; 2 = under target;; 1 = over;; 0 = none.
- **EX141 — Runbook fix.** What fix addresses the slow runbook lookup? *Rubric:* 3 = one-page emergency card at the front;; 2 = card;; 1 = training only;; 0 = none.

### Synthesis

Controlled failure trials measure real recovery capability and turn narrow margins into improvements.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble verification and measurement evidence; (2) structure the dossier around requirements; (3) make it auditable.

### 48.1 Purpose

The evidence dossier gathers proof that the identity programme met its requirements. Its readers are Sana's examiners, the council's auditors and the identity team. It must let a reader check any claim without trusting Sana's word: each requirement links to tests, measurements and documents showing it was met, partly met or not met. A well-built dossier is also a lasting asset for the council, since future audits and changes can start from it rather than reconstructing evidence from scratch. It is kept under version control.

### 48.2 Structure

The dossier is organised by requirement group: authentication, authorisation, lifecycle, audit and operations. For each requirement it gives the statement, verification method, test results with configuration versions, measurement results with dates, and status. A summary table shows status across all sixty requirements. Separate sections hold the threat ranking, residual risk register, studio records, independent review and trial results. Consistent structure lets readers find evidence quickly and see gaps at a glance. Cross-references link related evidence across sections, and an index lists every evidence identifier.

### 48.3 Honest status

Of sixty requirements, fifty-three are met, five partly met and two not met. Partly met requirements include single sign-on coverage, which reaches 133 of 140 applications, and leaver removal for applications on interim scripted checks. Not met are a self-service group request feature, ranked could and deferred, and a reporting dashboard delayed by procurement. Sana records each with its reason and plan. Showing gaps plainly makes the dossier credible; a dossier claiming everything was met would invite suspicion. Status is reviewed by her supervisor.

### 48.4 Auditability

To make the dossier auditable, every evidence item has an identifier, date, source and storage location, and logs or screenshots are kept unaltered with checksums. Scripts used for measurements are included with their versions, and synthetic test data is stored alongside. An auditor can pick any requirement, follow its links and reach original evidence. Sana asks a council auditor to try this on three random requirements before submission; one broken link is found and fixed. Checksums are verified before submission.

### Worked example

The dossier reports 53 met, 5 partly met and 2 not met of 60 requirements, with evidence items carrying identifiers, dates, sources and checksums; an auditor's trial finds one broken link, now fixed.

> **Synthetic case.** Requirements, counts and evidence are synthetic.

### Errors and limits

A dossier that claims every requirement was fully met invites suspicion rather than trust.

### Exercises

- **EX142 — Requirement status.** How many requirements are met, partly met and not met? *Rubric:* 3 = 53, 5, 2;; 2 = 53 met;; 1 = all;; 0 = none.
- **EX143 — SSO coverage final.** What single sign-on coverage does the dossier report? *Rubric:* 3 = 133 of 140 applications;; 2 = 133;; 1 = 140;; 0 = none.
- **EX144 — Auditor trial.** What did the auditor's trial find? *Rubric:* 3 = one broken link among three requirements;; 2 = one issue;; 1 = vague;; 0 = none.

### Synthesis

A requirement-structured, honest and auditable dossier proves what was achieved and what remains.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write the engineering thesis; (2) present the argument from problem to evidence; (3) state contribution and limits.

### 49.1 Thesis structure

Sana's thesis follows the engineering story: problem and context, requirements, threat and failure analysis, architecture alternatives and choice, control design, implementation, verification, measurement, validation, applied research and conclusions. Each chapter opens with its purpose and ends by linking to the next. Tables carry key numbers, with references to dossier evidence. She writes the method and results chapters first, while details are fresh, and the introduction last, once she knows exactly what the thesis shows. Signposting helps examiners follow the argument across chapters.

### 49.2 The argument

The argument runs: Linmouth had fragmented identities, slow leaver removal and weak authentication; requirements were derived from audit findings and threats; a cloud identity provider with HR-driven lifecycle was chosen against agreed criteria; controls were designed, implemented in phases and verified; and measurements show leaver removal falling from weeks to hours and phishing-resistant authentication becoming the norm. Each step cites evidence. Sana avoids claiming more than the evidence shows, such as a reduction in attacks, which she did not measure.

### 49.3 Contribution

Sana states her contribution clearly: an engineered and verified identity programme for a mid-sized public body, a reusable requirements set and test catalogue, a measured lifecycle improvement, and a small randomised study suggesting that last-use dates improve access reviews. Saltzer and Schroeder's principles and the NIST guidance cited throughout provide the foundations; her contribution is showing how they can be applied, measured and evidenced in a real setting with limited staff and budget. Each part is linked to its evidence in the dossier.

### 49.4 Limits and future work

Limits include one organisation, a measurement period of under a year after rollout, and some applications still on interim controls. Future work includes measuring whether access drifts back over several years, extending the review study across more cycles, and evaluating supplier access patterns. Stating limits clearly helps examiners trust the thesis and helps the council decide what to do next. Sana also notes what she would do differently: involve HR earlier, since feed reliability became central. Each limit is linked to its likely effect.

### Worked example

The thesis follows the engineering story from problem to evidence, claims a verified programme, reusable artefacts, measured lifecycle improvement and a small review study, and states limits and future work.

> **Synthetic case.** The thesis and its claims are synthetic.

### Errors and limits

Claiming a reduction in attacks that was never measured overstates the evidence.

### Exercises

- **EX145 — Unmeasured claim.** Which claim does Sana avoid because she did not measure it? *Rubric:* 3 = a reduction in attacks;; 2 = attacks;; 1 = leaver time;; 0 = none.
- **EX146 — Contribution items.** Name two parts of Sana's stated contribution. *Rubric:* 3 = verified programme, reusable requirements and tests, measured improvement, review study (two);; 2 = one;; 1 = vague;; 0 = none.
- **EX147 — Hindsight change.** What would Sana do differently? *Rubric:* 3 = involve HR earlier;; 2 = HR;; 1 = vague;; 0 = none.

### Synthesis

A clear engineering thesis links problem, design, evidence and limits into one credible argument.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) prepare and deliver the final defense; (2) answer questions with evidence; (3) close the project responsibly.

### 50.1 Preparing

Sana prepares a twenty-minute presentation: the problem, the chosen design and why, key evidence, the applied study, limits and contribution. She rehearses with fellow students acting as examiners, who ask hard questions about choices she now takes for granted. She prepares short answers with page and dossier references for likely questions, such as why a cloud provider, how emergency access is controlled and what happens to legacy applications. Preparation means understanding her own work deeply, not memorising a script. She times each section of the talk.

### 50.2 Likely questions

Examiners are likely to probe weak points: the reliance on HR data quality, the residual risk from interim controls, the small applied study, the cloud provider dependency and the exclusions of emergency accounts. For each, Sana prepares an honest answer that names the evidence and the limit. She also prepares for broader questions, such as how the design would change for a much larger organisation, answering from principles and from evidence rather than speculation presented as fact. Answers are checked with her supervisor.

### 50.3 The defense

In the defense, Sana listens fully to each question and answers what was asked, referring to specific evidence. When asked whether attacks fell, she explains that the project did not measure attacks, what it did measure, and how attack-related outcomes could be studied. When asked about HR dependency, she cites the failure trial showing safe behaviour when the feed stopped. Examiners request minor corrections, including a clearer explanation of the availability model, which she notes and agrees to complete. She remains calm and concise.

### 50.4 Closing the project

After corrections, Sana submits the final thesis and closes her obligations to the council. Exports and working files containing staff data are deleted according to the data agreement, confirmed in writing. The council keeps the dossier, runbooks and test suite. She thanks the identity team, service desk and staff who took part in interviews and studies, and offers a short session summarising lessons. Her final reflection notes that the most lasting outcomes are the processes and evidence the council now owns, not the project itself.

### Worked example

Sana delivers a twenty-minute defense, answers questions on attacks, HR dependency and interim controls with evidence, completes minor corrections and closes the project with confirmed data deletion.

> **Synthetic case.** Examiners, questions and outcomes are synthetic.

### Errors and limits

Answering a question about an unmeasured outcome with guesses rather than stating what was measured undermines credibility.

### Exercises

- **EX148 — Attack question answer.** How does Sana answer whether attacks fell? *Rubric:* 3 = explains attacks were not measured, what was, and how to study it;; 2 = honest;; 1 = yes;; 0 = none.
- **EX149 — HR dependency evidence.** What evidence does Sana cite on HR dependency? *Rubric:* 3 = failure trial showing safe behaviour when feed stopped;; 2 = trial;; 1 = vague;; 0 = none.
- **EX150 — Lasting outcome.** What does Sana consider the most lasting outcome? *Rubric:* 3 = processes and evidence the council now owns;; 2 = processes;; 1 = thesis;; 0 = none.

### Synthesis

A well-prepared, evidence-based defense and a responsible close complete the engineering journey.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Sana Malik, Dr Owen Hale, Brackenford Institute of Technology, Linmouth Borough Council and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Because the provider must cope at the busiest moment, or every federated application is blocked.

**EX002.** At the difference between the arrival rate and capacity.

**EX003.** Possible password-guessing attempts that monitoring should flag.

**EX004.** By composing the user-to-role relation with the role-to-permission relation.

**EX005.** Two to the power thirty, over a billion.

**EX006.** A cycle would make the roles in it equivalent and confuse every review.

**EX007.** The private key is designed not to be readable through normal interfaces.

**EX008.** Wrongly rejecting the right person and wrongly accepting someone else.

**EX009.** Security keys that can be used while wearing gloves.

**EX010.** jdoe and kpatel.

**EX011.** mlee.

**EX012.** That the first version treated JDoe and jdoe as different people.

**EX013.** A director summary, a technical design, a service desk guide and an auditor evidence register.

**EX014.** Staff sign-in, administrator access and account lifecycle.

**EX015.** She tests drafts on a colleague outside IT and rewrites what they misread.

**EX016.** The total number of events over the period.

**EX017.** In about fourteen months.

**EX018.** From policy and legal duties, not from available disk space.

**EX019.** That events occur independently at a stable average rate.

**EX020.** About one in twenty sign-ins takes twelve seconds or longer.

**EX021.** Because legitimate sign-ins vastly outnumber suspicious ones, so most alerts are false.

**EX022.** Anyone holding it could create tokens accepted by every application.

**EX023.** Every user must sign in again at once, creating a load spike.

**EX024.** She sizes so remaining servers can carry the full peak load.

**EX025.** Four (auditor, clerk-plus, helpdesk, manager-temp).

**EX026.** One account holding both payments-raise and payments-approve.

**EX027.** The script version, the input export file and its date.

**EX028.** Telling a director that former staff still have access.

**EX029.** Signing in to production systems and testing passwords (also bypass attempts).

**EX030.** So a faulty change cannot remove the ability to fix it.

**EX031.** By exchanging it with the provider over a direct back-channel connection.

**EX032.** A stolen authorisation code being redeemed by someone else.

**EX033.** Never write full tokens to logs.

**EX034.** If it is discovered on one machine, every machine built from the image is exposed.

**EX035.** Staff use standard accounts, with elevation granted on request and logged.

**EX036.** Five of fourteen.

**EX037.** Who should exist, meaning current staff and their jobs.

**EX038.** Linking related events across systems.

**EX039.** 61 synthetic accounts inactive for over ninety days.

**EX040.** So every integration follows the same secure defaults across 140 applications.

**EX041.** Over-broad group assignments.

**EX042.** That synthetic users get expected access and are refused what they should not have.

**EX043.** Staff may be locked out and unable to work.

**EX044.** Preventing one person from both raising and approving the same payment.

**EX045.** Abuse of recovery and reset processes.

**EX046.** Leaver removal within four working hours; buying a product is a design decision.

**EX047.** That it is unverified.

**EX048.** A leaver feed that runs weekly when the requirement assumes hours.

**EX049.** Staff who mistype a few times are locked out and the service desk is flooded.

**EX050.** Someone who knows a username can lock that person out by failing on purpose.

**EX051.** Progressive slowing of attempts or additional verification.

**EX052.** It applies the decision, for example by accepting or rejecting tokens.

**EX053.** If it fails or is misconfigured, every application is affected.

**EX054.** In each application, which understands its own data.

**EX055.** RFC 7519.

**EX056.** Signature, issuer, audience and expiry.

**EX057.** Hand-copied keys break silently when the provider rotates them.

**EX058.** HR emails a monthly leaver list to IT, who forward it to application owners.

**EX059.** A limited budget and a three-person identity team (also legacy apps, union agreements, continuity).

**EX060.** 19 days.

**EX061.** Removal from all integrated applications within four working hours of the HR end date.

**EX062.** Leaver removal and administrator authentication.

**EX063.** By analysing all role assignments with a script.

**EX064.** An identity is the person or system; an account is its record in one particular system.

**EX065.** They become exceptions with an owner and expiry, not roles.

**EX066.** Because attribute-based decisions depend on HR data being correct.

**EX067.** A phished password reused at the provider, scoring 20.

**EX068.** Because its impact is very high (5) even though likelihood is low (2).

**EX069.** Leavers would keep access and no alarm would be raised.

**EX070.** A standard protocol for creating, updating and disabling user accounts in applications.

**EX071.** A call-back to the number in HR records (or a video check against the staff photo).

**EX072.** It is removed automatically, after a reminder to the approver.

**EX073.** Call-back verification fails for new starters whose numbers are not yet recorded.

**EX074.** A one-hour grace period during which HR can reverse an erroneous leaver date.

**EX075.** Interim scripted daily exports, documented as residual risk.

**EX076.** It gives a baseline that more ambitious options must justify themselves against.

**EX077.** The leaver removal requirement.

**EX078.** For example, a large rise in subscription prices.

**EX079.** Three, for s02, s03 and s06.

**EX080.** Preventive checks only see identity-system assignments, not grants made directly in applications.

**EX081.** Separate administrator accounts used from managed workstations with just-in-time elevation.

**EX082.** IT and planning, because IT can troubleshoot and planning uses mixed old and new applications.

**EX083.** It records what the policy would have done without enforcing it.

**EX084.** Excluded from conditional policies but closely monitored, with any use triggering an alert.

**EX085.** From 408 hours to 1.6 hours.

**EX086.** One of twelve.

**EX087.** Fix the connector's locked-record handling and agree weekend handling of leaver alerts.

**EX088.** So tests cannot affect real staff or services.

**EX089.** An application accepting tokens issued for a different audience.

**EX090.** 79 of 84.

**EX091.** So any difference in outcome points to something particular to that department.

**EX092.** An application proxy, a scripted daily check or replacement.

**EX093.** A council sponsor, who confirms continued need every quarter.

**EX094.** About 30.6 hours (availability 0.9965).

**EX095.** It is not in the sign-in path; it only delays joiner and leaver changes.

**EX096.** Twice a year.

**EX097.** Out-of-hours social care records (also emergency planning or repairs for vulnerable tenants).

**EX098.** That leavers processed during the outage actually lost their access.

**EX099.** It was stored in a building locked at weekends.

**EX100.** So patterns of repeated recovery, a possible sign of abuse, become visible.

**EX101.** Emergency account use and repeated failed second factors (others: new device with unusual location, admin activation, connector failure).

**EX102.** Whether everything keeps working after her project ends.

**EX103.** 140, about a third without a clear business reason.

**EX104.** By writing test cases first so behaviour cannot silently change.

**EX105.** A campaign encouraging staff to register a second passkey.

**EX106.** About 17.6 requests per second, 29 percent of one server.

**EX107.** Fewer refreshes, but a stolen token stays useful for longer.

**EX108.** A slow group-membership lookup for users with many nested groups.

**EX109.** Because disabling the password alone does not end existing sessions.

**EX110.** The share of changes that need to be rolled back.

**EX111.** Plain-language descriptions and last-use dates (also highlighted conflicts, short lists, automatic removal).

**EX112.** Verification checks written requirements; validation checks the real needs of people.

**EX113.** They work but are easily left in vans.

**EX114.** 120 of 140.

**EX115.** Groups, groups without owners and active exceptions (also policies, ownerless applications).

**EX116.** Three were added to the repository after review and one was reverted.

**EX117.** role-finance-clerk (or app-payroll-users).

**EX118.** The system must not treat missing staff as leavers and disable everyone.

**EX119.** 146 of 148.

**EX120.** An application accepted tokens two minutes after expiry.

**EX121.** Eight, down from fourteen.

**EX122.** Two gaps where certain devices escaped multi-factor prompts.

**EX123.** When it reduces effort and complexity while keeping or improving security.

**EX124.** The share of reviewed items removed and later confirmed as unneeded.

**EX125.** Application owners.

**EX126.** 11 percent with last-use dates versus 5 percent without.

**EX127.** That sign-in logs might be used to monitor productivity.

**EX128.** Phishing-resistant authentication support and standard protocols (also exportable logs, supplier access limits).

**EX129.** Sharing an individual's sign-in history with a manager without proper authorisation.

**EX130.** At least twelve of the twenty remaining applications under the provider with automated leaver removal.

**EX131.** Seven proxy, five modern federation, four permanent scripted check and four retiring.

**EX132.** She moves it to interim controls, substitutes another application and records and reports the change.

**EX133.** Reject any request that does not come through the proxy.

**EX134.** Up to twenty-four hours.

**EX135.** An independent review step for high-risk identity changes.

**EX136.** Thirteen of twenty, one above the target of twelve.

**EX137.** From 47 to 2, both explained by pending HR corrections.

**EX138.** By confirming that a synthetic leaver is detected and alerts reach the identity team.

**EX139.** An alert fired within forty minutes and no staff were wrongly disabled.

**EX140.** Fifty-five minutes against a sixty-minute target.

**EX141.** A one-page emergency card at the front of the runbook.

**EX142.** 53 met, 5 partly met and 2 not met.

**EX143.** 133 of 140 applications.

**EX144.** One broken evidence link, which was fixed.

**EX145.** A reduction in attacks.

**EX146.** A verified identity programme and a reusable requirements set and test catalogue (also measured improvement, review study).

**EX147.** Involve HR earlier, since feed reliability became central.

**EX148.** She explains attacks were not measured, states what was measured and how attack outcomes could be studied.

**EX149.** The failure trial showing safe behaviour when the HR feed stopped.

**EX150.** The processes and evidence the council now owns.

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
