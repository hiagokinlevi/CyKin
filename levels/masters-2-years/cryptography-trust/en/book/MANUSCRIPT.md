# Cryptography and Trust Services: Master's Course

- Language: English (`en`); course 169, Master's course (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; five offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students who will run a reproducible study on how organisations operate certificates and public-key trust.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the book studies how vetted TLS, X.509 and ACME tooling is operated. It never teaches building cryptographic primitives for production; labs compute dates, counts, rates and keyed pseudonyms on synthetic data. All people, organisations and hosts are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one master's student asking why TLS certificates expire unnoticed in a hospital network, and whether automated renewal with ACME (RFC 8555) reduces expiry incidents compared with manual renewal. The route runs from literature method, through a seminar on X.509 and TLS 1.3, ethical study design, competing explanations, a pilot, data analysis, writing and an independent review. Attempt the exercises before the worked results and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Felipe Arantes** | Master's student | Invented |
| **Dr. Ingrid Solberg** | Supervisor | Invented |
| **Coldwater Polytechnic** | Fictional university | Invented |
| **Briarwood Health Network** | Fictional partner with about 1,400 certificates | Invented |

### Core sources

[RFC 5280](https://www.rfc-editor.org/rfc/rfc5280) (X.509 profile); [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) (TLS 1.3); [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555) (ACME); [RFC 6962](https://www.rfc-editor.org/rfc/rfc6962) (Certificate Transparency); NIST [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5); Boneh and Shoup, [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/); Katz and Lindell (3rd ed.). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn an operational pain into a researchable question about certificate lifecycles; (2) run a documented literature search with a screening funnel; (3) record why each source was kept or dropped.

### 1.1 The case

Felipe Arantes is a master's student at the fictional Coldwater Polytechnic, supervised by Dr. Ingrid Solberg. The fictional Briarwood Health Network runs about 1,400 TLS certificates across patient portals, laboratory systems and internal APIs. Last year several expired unnoticed, and clinicians briefly lost access to results. Some certificates renew automatically through an ACME client, as defined in RFC 8555, while others are renewed by hand from a spreadsheet. Felipe's working question is whether automated renewal is associated with fewer expiry incidents per certificate-year than manual renewal, and what else explains the incidents that still happen. All hosts and figures in this book are synthetic.

### 1.2 Sharpening the question

A good master's question is narrow enough to answer in a year and clear about its unit. Felipe defines an expiry incident as a user-visible failure caused by a certificate past its notAfter date, the validity field defined in RFC 5280. His unit is the certificate-year, so a service with many short-lived certificates is not unfairly counted. He writes one primary question about renewal mode and one secondary question about other causes, and he explicitly excludes revocation failures and algorithm weaknesses, which are real problems but would need different data. Dr. Solberg asks him to write the excluded topics down so the scope does not creep later.

### 1.3 A documented search

Felipe searches three academic databases plus the RFC index and NIST publications, using a written string combining certificate terms (certificate, X.509, TLS, PKI) with lifecycle terms (expiry, renewal, ACME, outage). He keeps the exact strings, dates and hit counts in a log so another student could rerun the search. Standards are searched separately because they rarely appear in academic indexes but define the vocabulary. The screening stages follow a common systematic-review pattern: remove duplicates, screen titles and abstracts against inclusion rules, read full texts, and keep only studies that report an outage or expiry outcome.

### Lab — Screening funnel

```python
"""Literature screening funnel for a synthetic review of certificate-lifecycle studies."""
STAGES = [("records found (3 databases + RFC/NIST search)", 412), ("after duplicate removal", 297),
          ("after title/abstract screen", 64), ("after full-text eligibility", 21),
          ("included with outage or expiry outcome", 9)]

def main():
    prev = None
    for name, n in STAGES:
        drop = "" if prev is None else f"  (-{prev - n})"
        print(f"{n:>4}  {name}{drop}")
        prev = n
    print(f"inclusion rate from deduplicated pool: {100 * STAGES[-1][1] / STAGES[1][1]:.1f}%")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_screen.py`. Verified output:

```text
 412  records found (3 databases + RFC/NIST search)
 297  after duplicate removal  (-115)
  64  after title/abstract screen  (-233)
  21  after full-text eligibility  (-43)
   9  included with outage or expiry outcome  (-12)
inclusion rate from deduplicated pool: 3.0%
```

### 1.4 Reading the funnel

The search finds 412 records, 297 remain after duplicates are removed, 64 pass title and abstract screening, 21 pass full-text eligibility and 9 report an expiry or outage outcome. Only 3.0 percent of the deduplicated pool is finally included, which is normal for a narrow question. The largest drop, 233 records, happens at title and abstract screening, mostly papers on certificate validation bugs rather than lifecycle management. Felipe reports every number, because a reader who sees only the nine included studies cannot judge whether relevant work was missed or excluded for weak reasons.

### 1.5 Recording decisions

For each full-text paper Felipe writes one line: citation, population, outcome measure, whether renewal was automated, and the reason for inclusion or exclusion. Twelve papers are dropped at full text, most because they measured certificate misissuance by authorities rather than expiry at operators. He separately records grey literature such as vendor outage reports, flagged as non-peer-reviewed, because they describe real failures but rarely state their methods. That log becomes an appendix of the dissertation and lets examiners test whether his conclusions follow from the evidence he actually read.

### Worked example

Felipe writes the question with a certificate-year unit, logs the search strings, and reports a 412 to 9 funnel with reasons for every full-text exclusion.

> **Synthetic case.** Coldwater, Briarwood and every host are invented; RFC 5280 and RFC 8555 are real.

### Errors and limits

Searches miss work indexed under other words, and grey literature is uneven. A funnel shows diligence, not completeness, so state the search date and limits.

### Exercises

- **EX001 — Working question.** State Felipe's primary question with its unit. *Rubric:* 3 = is ACME automated renewal associated with fewer expiry incidents per certificate-year than manual renewal;; 2 = without unit;; 1 = "fix expiry";; 0 = none.
- **EX002 — Incident definition.** How is an expiry incident defined, and which field marks expiry? *Rubric:* 3 = user-visible failure from a certificate past notAfter (RFC 5280);; 2 = definition without field;; 1 = any warning;; 0 = none.
- **EX003 — Excluded topics.** Which two topics did Felipe exclude and why? *Rubric:* 3 = revocation failures and algorithm weaknesses; need different data;; 2 = topics only;; 1 = one;; 0 = none.
- **EX004 — Funnel numbers.** Give the counts at each of the five stages. *Rubric:* 3 = 412, 297, 64, 21, 9;; 2 = four right;; 1 = ends only;; 0 = none.
- **EX005 — Largest drop.** Where was the biggest drop and what caused most of it? *Rubric:* 3 = title/abstract, 233 records, mostly validation-bug papers;; 2 = stage only;; 1 = duplicates;; 0 = none.
- **EX006 — Full-text exclusions.** Why were most full-text papers excluded? *Rubric:* 3 = they studied CA misissuance rather than operator expiry;; 2 = off-topic;; 1 = quality;; 0 = none.
- **EX007 — Grey literature.** How does Felipe handle vendor outage reports? *Rubric:* 3 = records them separately, flagged non-peer-reviewed, as methods are rarely stated;; 2 = flags them;; 1 = ignores;; 0 = none.

### Synthesis

A narrow question with a fair unit, a replayable search and a full decision log are the foundation of a credible master's study.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Cryptography and trust services: advanced seminar

### Learning outcomes

You will (1) explain how an X.509 certificate binds a public key to a name; (2) describe where certificates enter the TLS 1.3 handshake; (3) read a certificate inventory and spot lifecycle risk.

### 2.1 What a certificate asserts

A certificate is a signed statement by an issuing authority that a public key belongs to a subject, valid between notBefore and notAfter. RFC 5280 profiles the fields: subject and subject alternative names, issuer, serial number, validity, key usage and extensions. The signature, made with an algorithm such as ECDSA or RSA from FIPS 186-5, lets a client check the statement using the issuer's public key, up a chain to a root it already trusts. Katz and Lindell describe this as moving trust from many keys to a few roots. The validity window is part of the signed statement, so an expired certificate cannot be extended without a new signature.

### 2.2 Certificates in TLS 1.3

In a TLS 1.3 handshake, defined in RFC 8446, client and server first agree on key shares, typically using X25519 from RFC 7748, and derive handshake keys with HKDF from RFC 5869. The server then sends its certificate chain and a CertificateVerify message, a signature over the handshake transcript made with the certificate's private key. The client validates the chain, the names and the validity period. If the certificate has expired, a correctly configured client aborts the handshake. That is the behaviour Briarwood clinicians experienced: the cryptography worked exactly as designed and refused an out-of-date assertion.

### 2.3 Why lifetimes keep shrinking

Short lifetimes limit how long a stolen key or a mistaken certificate remains useful, and they reduce dependence on revocation, which clients check unevenly. The cost is operational: more renewals, each a chance to fail. Certificate Transparency, specified in RFC 6962, adds public logs so that domain owners can see every certificate issued for their names. SP 800-57 Part 1 frames the same tension for all keys: cryptoperiods should be limited, but every rotation must be planned. Felipe's seminar paper argues that automation is the only scalable answer to shrinking lifetimes, which his study will test rather than assume.

### Lab — Inventory read

```python
"""Days to expiry for a synthetic certificate inventory, as of a fixed audit date."""
from datetime import date
AUDIT = date(2026, 3, 1)
CERTS = [("h-portal", "acme", date(2026, 4, 20)), ("h-labres", "manual", date(2026, 3, 9)),
         ("h-pacs", "manual", date(2026, 2, 25)), ("h-api", "acme", date(2026, 4, 2)),
         ("h-vpn", "manual", date(2027, 1, 15)), ("h-mail", "manual", date(2026, 3, 20)),
         ("h-sched", "acme", date(2026, 5, 1)), ("h-hr", "manual", date(2026, 3, 27))]

def main():
    for name, how, exp in sorted(CERTS, key=lambda c: c[2]):
        d = (exp - AUDIT).days
        flag = "EXPIRED" if d < 0 else ("<30d" if d < 30 else "")
        print(f"{name:<9} {how:<7} {exp}  {d:>4} d  {flag}")
    urgent = [c for c in CERTS if (c[2] - AUDIT).days < 30]
    print(f"urgent {len(urgent)}/{len(CERTS)}, all manual: {all(c[1] == 'manual' for c in urgent)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_inventory.py`. Verified output:

```text
h-pacs    manual  2026-02-25    -4 d  EXPIRED
h-labres  manual  2026-03-09     8 d  <30d
h-mail    manual  2026-03-20    19 d  <30d
h-hr      manual  2026-03-27    26 d  <30d
h-api     acme    2026-04-02    32 d  
h-portal  acme    2026-04-20    50 d  
h-sched   acme    2026-05-01    61 d  
h-vpn     manual  2027-01-15   320 d  
urgent 4/8, all manual: True
```

### 2.4 Reading the inventory

On the synthetic audit date of 1 March 2026, one of eight sampled certificates, h-pacs, has already expired by four days, and three more expire within thirty days: h-labres in 8 days, h-mail in 19 and h-hr in 26. All four urgent certificates are renewed manually, while the three ACME certificates sit at 32 to 61 days, consistent with clients that renew around a third of the lifetime before expiry. One manual certificate, h-vpn, has 320 days left. Felipe notes that a long-lived manual certificate is not safe either: it will expire long after the person who installed it has moved roles.

### 2.5 From seminar to study

The seminar leaves Felipe with three operational hypotheses. Manual certificates cluster near expiry because renewal depends on a person remembering. Automated certificates can still fail when the ACME client breaks silently, for instance after a firewall change blocks the validation challenge. And certificates without a recorded owner fail whichever renewal method they use, because nobody receives or acts on warnings. The third hypothesis competes with his main question and will return in Chapter 4. He writes them down now so that later analysis tests ideas he had before seeing outcome data.

### Worked example

Felipe explains how an expired certificate makes a TLS 1.3 client abort, then reads an eight-certificate sample in which all four urgent items are manual.

> **Synthetic note.** The eight hosts and dates are invented; RFC 5280, RFC 8446 and RFC 6962 are real.

### Errors and limits

An eight-row sample illustrates; it does not estimate a rate. Validity dates alone cannot show whether an ACME client is actually healthy.

### Exercises

- **EX008 — Certificate claim.** What does an X.509 certificate assert, and what makes it checkable? *Rubric:* 3 = issuer-signed binding of public key to subject within validity window; verified with issuer key up a chain to a trusted root;; 2 = binding only;; 1 = "encrypts traffic";; 0 = none.
- **EX009 — Handshake role.** At which point in TLS 1.3 does the server prove possession of its certificate key? *Rubric:* 3 = CertificateVerify, a signature over the transcript;; 2 = "during certificate message";; 1 = key share;; 0 = none.
- **EX010 — Short lifetimes.** Give one benefit and one cost of shorter certificate lifetimes. *Rubric:* 3 = limits stolen-key window/less reliance on revocation; more renewals that can fail;; 2 = one side;; 1 = vague;; 0 = none.
- **EX011 — Urgent certificates.** Which sampled certificates were expired or under 30 days, and how were they renewed? *Rubric:* 3 = h-pacs expired, h-labres, h-mail, h-hr under 30 days, all manual;; 2 = count and mode;; 1 = count only;; 0 = none.
- **EX012 — Long manual certificate.** Why is h-vpn with 320 days still a risk? *Rubric:* 3 = it expires after its installer may have left, so nobody remembers;; 2 = still manual;; 1 = safe;; 0 = none.
- **EX013 — Silent ACME failure.** How can an automated certificate still expire? *Rubric:* 3 = ACME client breaks silently, e.g. firewall blocks validation challenge;; 2 = client failure;; 1 = never;; 0 = none.
- **EX014 — Competing hypothesis.** Which seminar hypothesis competes with the main question? *Rubric:* 3 = certificates without a recorded owner fail whatever the renewal mode;; 2 = ownership;; 1 = algorithm;; 0 = none.

### Synthesis

Certificates are signed, time-bounded assertions that TLS enforces strictly; lifecycle operations, not cryptography, decide whether they stay valid.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) choose an observational design suited to existing certificate records; (2) pseudonymise hostnames with a keyed function; (3) plan for a study others can reproduce.

### 3.1 Choosing an observational design

Felipe cannot randomise certificates to renewal modes; Briarwood decided those years ago. He chooses a retrospective cohort design: every certificate active during the past two years is a member, its renewal mode is the exposure, and expiry incidents from the ticketing system are the outcome. He measures exposure time in certificate-years, so a certificate that existed for six months contributes half a year. He accepts the main weakness openly: services chosen for automation may differ from manual ones in age, team or importance, so differences may reflect those traits, not renewal mode.

### 3.2 Ethics and approval

The study touches no patient data, but the ethics committee still reviews it because hostnames and tickets can reveal Briarwood's internal architecture and staff names. Felipe's protocol says ticket text is read only on Briarwood premises, staff names are removed before export, and the exported dataset contains only pseudonymised host identifiers, renewal mode, dates and incident counts. Any currently expired or soon-expiring certificate he notices is reported to the Briarwood infrastructure lead on the same day, because a study of outages must not knowingly let one happen.

### 3.3 Keyed pseudonyms

Felipe needs stable pseudonyms: the same hostname must map to the same identifier across files, but outsiders must not be able to reverse it. A plain hash fails, because anyone can hash a guessed hostname such as portal.briarwood.example and compare. A keyed hash, HMAC from RFC 2104 with SHA-256, fixes this: only holders of the secret key can compute the mapping. Briarwood generates and keeps the key; Felipe receives only pseudonymised data. The lab uses a fixed demonstration key purely so the output is reproducible, and shows that a fresh random key from the secrets module produces unrelated pseudonyms.

### Lab — Keyed pseudonyms

```python
"""Keyed pseudonyms for hostnames with HMAC-SHA256 (RFC 2104); synthetic names, demo key only."""
import hmac, hashlib, secrets
HOSTS = ["portal.briarwood.example", "lab-results.briarwood.example", "portal.briarwood.example"]

def pseud(key, host):
    return "h-" + hmac.new(key, host.encode(), hashlib.sha256).hexdigest()[:10]

def main():
    fixed = b"study-demo-key-not-for-production"  # fixed so output is reproducible
    for h in HOSTS:
        print(f"{h:<33} -> {pseud(fixed, h)}")
    plain = "h-" + hashlib.sha256(HOSTS[0].encode()).hexdigest()[:10]
    print(f"unkeyed SHA-256 of first host -> {plain} (anyone can recompute)")
    fresh = secrets.token_bytes(32)
    print(f"fresh random key gives same pseudonym as demo key: {pseud(fresh, HOSTS[0]) == pseud(fixed, HOSTS[0])}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_pseudo.py`. Verified output:

```text
portal.briarwood.example          -> h-6f292159ff
lab-results.briarwood.example     -> h-915f39cfa2
portal.briarwood.example          -> h-6f292159ff
unkeyed SHA-256 of first host -> h-80926435c3 (anyone can recompute)
fresh random key gives same pseudonym as demo key: False
```

### 3.4 Reading the pseudonyms

Both appearances of portal.briarwood.example map to h-6f292159ff, so records join correctly, while lab-results maps to h-915f39cfa2. The unkeyed SHA-256 of the first host yields h-80926435c3, which any outsider who guesses the name can recompute; that is why plain hashing is not pseudonymisation. With a fresh 32-byte key the pseudonym differs, confirming that the mapping depends on the secret. Felipe notes that truncating to ten hexadecimal characters is acceptable for 1,400 hosts, giving about a trillion possible values, but must be checked for collisions before joining tables.

### 3.5 Reproducibility plan

Felipe's plan lists what another researcher would need: the data dictionary, extraction queries run against Briarwood's inventory and ticketing systems, the analysis scripts with random seeds, the pseudonymised dataset and a log of every manual coding decision. Briarwood cannot publish the extraction queries, so he documents them in prose detailed enough to adapt elsewhere. He fixes the software environment to the Python standard library to avoid dependency drift. Dr. Solberg asks for a dry run: a classmate repeats the analysis from the package alone and reproduces every table.

### Worked example

Felipe registers a retrospective cohort design measured in certificate-years, obtains ethics approval with same-day reporting of live expiries, and exports data with HMAC-SHA256 pseudonyms whose key stays at Briarwood.

> **Synthetic note.** The hosts and demonstration key are invented; HMAC (RFC 2104) is real, and real keys must come from a managed secret store.

### Errors and limits

Observational cohorts cannot rule out confounding; they can only measure and adjust for what was recorded. Pseudonyms protect against outsiders, not against anyone who obtains the key.

### Exercises

- **EX015 — Design choice.** Why a retrospective cohort instead of a trial? *Rubric:* 3 = renewal mode already assigned and cannot be randomised; cohort uses existing records;; 2 = no randomising;; 1 = cheaper;; 0 = none.
- **EX016 — Exposure time.** How does a six-month certificate contribute to the denominator? *Rubric:* 3 = half a certificate-year;; 2 = partial;; 1 = one;; 0 = none.
- **EX017 — Live-risk duty.** What must Felipe do on noticing an expiring certificate? *Rubric:* 3 = report it to the infrastructure lead that same day;; 2 = report;; 1 = record it;; 0 = none.
- **EX018 — Plain hash weakness.** Why is unkeyed SHA-256 unsuitable for hostname pseudonyms? *Rubric:* 3 = anyone can hash guessed hostnames and match;; 2 = reversible-ish;; 1 = too slow;; 0 = none.
- **EX019 — Lab pseudonyms.** Which pseudonym did portal.briarwood.example receive, and what did the fresh-key test print? *Rubric:* 3 = h-6f292159ff both times; False;; 2 = one;; 1 = unkeyed value;; 0 = none.
- **EX020 — Dry run.** What did Dr. Solberg's dry run check? *Rubric:* 3 = a classmate reproduced all tables from the package alone;; 2 = reproducibility;; 1 = code style;; 0 = none.

### Synthesis

An honest observational design, keyed pseudonyms held by the partner and a tested reproducibility package make a field study both ethical and checkable.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Cryptography and trust services: competing explanations

### Learning outcomes

You will (1) set rival explanations for certificate expiry against each other; (2) read a cross-tabulation for confounding; (3) decide which explanation the data can and cannot distinguish.

### 4.1 Three rival explanations

Felipe states three explanations for expiry incidents. The renewal-mode explanation says manual renewal fails because people forget. The ownership explanation says certificates without a named owner fail because warnings reach nobody, whatever the renewal method. The change-collision explanation says renewals fail when network or firewall changes break validation or deployment, affecting automated renewals in particular. Each predicts a different pattern. If renewal mode dominates, manual incidents should outnumber automated ones even among owned certificates. If ownership dominates, owner-missing incidents should be common in both modes.

### Lab — Explanation cross-tab

```python
"""Cross-tab of 30 synthetic expiry incidents against two competing explanations."""
from collections import Counter
# (renewal mode, owner recorded?) for each incident
INC = ([("manual", False)] * 14 + [("manual", True)] * 9 + [("acme", False)] * 5 + [("acme", True)] * 2)

def main():
    c = Counter(INC)
    print("            owner-missing  owner-known")
    for mode in ("manual", "acme"):
        print(f"{mode:<10} {c[(mode, False)]:>10} {c[(mode, True)]:>12}")
    for mode in ("manual", "acme"):
        tot = c[(mode, False)] + c[(mode, True)]
        print(f"{mode}: {tot} incidents, owner missing in {100 * c[(mode, False)] / tot:.0f}%")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_explain.py`. Verified output:

```text
            owner-missing  owner-known
manual             14            9
acme                5            2
manual: 23 incidents, owner missing in 61%
acme: 7 incidents, owner missing in 71%
```

### 4.2 Reading the cross-tab

Among thirty synthetic incidents, twenty-three involve manual certificates and seven ACME certificates. Owner-missing certificates account for 61 percent of manual incidents and 71 percent of ACME incidents. Felipe sees two things. Manual renewal is clearly over-represented, which supports the renewal-mode explanation. Yet the owner-missing share is high in both modes, which supports the ownership explanation too. Raw counts alone cannot separate them, because he has not yet divided by the number of certificates in each cell; a high count might just reflect many owner-missing certificates.

### 4.3 Confounding in plain terms

A confounder is a factor linked to both exposure and outcome. If Briarwood automated mostly well-owned, modern services and left orphaned legacy hosts on manual renewal, ownership would make automation look better than it is. Felipe checks the inventory and finds that 38 percent of manual certificates lack an owner compared with 21 percent of ACME certificates. Ownership is therefore a plausible confounder, and his analysis must compare like with like: manual and ACME certificates within the owner-known group, and separately within the owner-missing group.

### 4.4 Where change collision fits

The change-collision explanation needs different evidence: change tickets linked to renewal dates. Felipe finds that five of the seven ACME incidents followed a firewall or proxy change within the preceding week, where the ACME client could no longer complete its challenge and logged errors nobody watched. RFC 8555 defines challenge types such as HTTP-01 and DNS-01, and each depends on infrastructure outside the client. This explanation does not compete with automation so much as qualify it: automation removes forgetting but adds a monitored dependency.

### 4.5 What the data can decide

Felipe writes a decision table. The data can estimate incident rates by renewal mode within ownership strata, which addresses confounding by ownership. The data can describe how often automated failures follow changes, but with seven incidents only descriptively. The data cannot rule out unmeasured confounders such as service criticality, because Briarwood does not record it consistently. He states that his conclusion will be about association, adjusted for ownership, and that any causal language must be qualified. Naming the limits now prevents an overclaim later.

### Worked example

Felipe's cross-tab shows manual renewal over-represented but owner-missing shares high in both modes; he adopts stratification by ownership and treats change collision as a qualifier of automation.

> **Synthetic note.** The thirty incidents and ownership percentages are invented; RFC 8555 challenge types are real.

### Errors and limits

Counts without denominators mislead; always convert to rates. Stratifying on one confounder leaves others uncontrolled.

### Exercises

- **EX021 — Three explanations.** Name the three rival explanations. *Rubric:* 3 = renewal mode, ownership, change collision;; 2 = two;; 1 = one;; 0 = none.
- **EX022 — Cross-tab shares.** What owner-missing shares did the lab report for each mode? *Rubric:* 3 = 61 percent manual, 71 percent ACME;; 2 = one;; 1 = counts only;; 0 = none.
- **EX023 — Why counts fail.** Why can raw incident counts not separate the explanations? *Rubric:* 3 = no denominators; counts may reflect how many certificates each cell holds;; 2 = need rates;; 1 = small sample;; 0 = none.
- **EX024 — Confounder evidence.** What inventory figures make ownership a confounder? *Rubric:* 3 = 38 percent manual vs 21 percent ACME lack owners;; 2 = direction;; 1 = none;; 0 = none.
- **EX025 — Change collisions.** How many ACME incidents followed infrastructure changes, and why? *Rubric:* 3 = five of seven; client could not complete challenge, errors unwatched;; 2 = number;; 1 = reason;; 0 = none.
- **EX026 — Unmeasured confounder.** Which confounder can the data not address? *Rubric:* 3 = service criticality, not consistently recorded;; 2 = "unmeasured";; 1 = ownership;; 0 = none.

### Synthesis

Rival explanations predict different patterns; testing them requires rates, stratification on measured confounders and candour about what remains unmeasured.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write a proposal that commits to outcomes, strata and analysis; (2) pilot data extraction on a small slice; (3) fix extraction errors before full collection.

### 5.1 The proposal

Felipe's proposal states the primary outcome, expiry incidents per 100 certificate-years, compared between manual and ACME renewal, overall and within owner-known and owner-missing strata. The secondary outcome is the share of ACME incidents preceded by an infrastructure change within seven days. The analysis plan uses rate ratios with bootstrap intervals, because incidents are few and their distribution is far from normal. He records the planned seed and resample count, and he lists in advance the inventory fields he will use, so that he cannot later search the dataset for a favourable split.

### 5.2 Linking certificates to incidents

The hardest technical step is linking tickets to certificates. Tickets mention hostnames in free text, sometimes misspelt, while the inventory uses fully qualified names. Felipe writes matching rules in advance: exact match on the subject alternative name first, then a documented list of known aliases, then manual review by two people for anything left. Each ticket must also mention certificate expiry or a browser or client error about validity; tickets that merely mention a certificate during an unrelated outage are excluded. The rules go into the proposal appendix.

### 5.3 Running the pilot

The pilot extracts three months of tickets and the matching inventory slice: 118 certificates and 11 candidate tickets. Two people apply the linking rules independently. They agree on nine tickets and disagree on two. One disagreement involves a ticket naming a load balancer that terminates TLS for several hosts; the other involves an expired intermediate certificate in a chain rather than the server certificate itself. Felipe also finds that 14 inventory rows lack a renewal-mode value, because older spreadsheets never recorded it. He treats these as instrument faults to fix, not as results to interpret.

### 5.4 Fixing the instruments

Felipe makes three rule changes. Load-balancer tickets are attributed to the certificate actually presented to clients, checked against the inventory's endpoint field. Expired intermediates are coded as expiry incidents attributed to the chain owner, because RFC 5280 path validation fails on any expired certificate in the path, not just the leaf. Rows without renewal mode are filled from the ACME client's own account records where possible, and otherwise marked unknown and reported as a separate group, not silently dropped. Each change is logged with a date before full extraction begins.

### 5.5 What the pilot does not tell

The pilot covers only three months, so Felipe does not compute or report incident rates from it. He uses it to estimate effort: linking took about four minutes per ticket, so a two-year extraction of roughly 120 tickets is feasible within a month. He also confirms that pseudonymisation runs at Briarwood before export and that the HMAC key never leaves their secret store. Dr. Solberg approves the revised proposal, and Felipe schedules full extraction for a quiet period so that infrastructure staff can answer questions about ambiguous tickets.

### Worked example

Felipe commits to rates per 100 certificate-years with ownership strata, pilots linking on 118 certificates and 11 tickets, and fixes rules for load balancers, intermediates and missing renewal modes.

> **Synthetic note.** The pilot counts and timings are invented; RFC 5280 path validation is real.

### Errors and limits

A pilot that is too short cannot estimate rates and should not try. Changing rules after seeing outcome data, rather than during a pilot, becomes outcome-driven analysis.

### Exercises

- **EX027 — Primary outcome.** State the primary outcome and its comparison. *Rubric:* 3 = incidents per 100 certificate-years, manual vs ACME, overall and by ownership stratum;; 2 = no strata;; 1 = counts;; 0 = none.
- **EX028 — Linking order.** In what order are tickets matched to certificates? *Rubric:* 3 = exact SAN match, known aliases list, then two-person manual review;; 2 = two steps;; 1 = manual only;; 0 = none.
- **EX029 — Pilot disagreements.** What were the two pilot disagreements about? *Rubric:* 3 = load balancer terminating several hosts; expired intermediate certificate;; 2 = one;; 1 = typo;; 0 = none.
- **EX030 — Intermediate rule.** How are expired intermediates coded, and why? *Rubric:* 3 = as expiry incidents for the chain owner, since RFC 5280 path validation fails on any expired certificate;; 2 = coding only;; 1 = excluded;; 0 = none.
- **EX031 — Missing renewal mode.** What happens to rows without renewal mode? *Rubric:* 3 = fill from ACME account records, else mark unknown and report separately;; 2 = mark unknown;; 1 = drop;; 0 = none.
- **EX032 — Effort estimate.** What effort estimate did the pilot produce? *Rubric:* 3 = about four minutes per ticket, about 120 tickets feasible within a month;; 2 = minutes only;; 1 = vague;; 0 = none.

### Synthesis

A specific proposal plus a pilot aimed at extraction faults makes the full dataset consistent before any rate is computed.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) compute incident rates per certificate-year; (2) express uncertainty for a rate ratio with a bootstrap; (3) compare overall and stratified estimates.

### 6.1 The assembled dataset

Full extraction covers two years. Manual certificates contribute 540 certificate-years and 23 linked expiry incidents; ACME certificates contribute 900 certificate-years and 7 incidents. Forty-one rows remain with unknown renewal mode and two incidents; Felipe reports them separately and runs a check showing that assigning them all to either group changes no conclusion. Every number traces back to a query and a coding log entry. Before running any comparison he re-reads the proposal to confirm that the analysis matches what he registered, including the seed and the resample count.

### 6.2 Rates and the rate ratio

A rate divides events by exposure. Manual renewal shows 4.26 incidents per 100 certificate-years and ACME 0.78, giving a rate ratio of 5.48: manual certificates failed about five and a half times as often per unit of exposure. A ratio alone hides uncertainty, and seven ACME incidents is a small number. The bootstrap estimates uncertainty by resampling certificate-years with replacement thousands of times and recomputing the ratio, then reading the middle 95 percent of the resulting values. It makes few assumptions, which suits sparse event data.

### Lab — Rate ratio with bootstrap

```python
"""Expiry incidents per 100 certificate-years with a bootstrap interval for the rate ratio (synthetic)."""
import random
MANUAL = [1] * 23 + [0] * 517   # 540 manual certificate-years, 23 incidents
ACME = [1] * 7 + [0] * 893      # 900 ACME certificate-years, 7 incidents

def rate(x): return 100 * sum(x) / len(x)

def main():
    rr = rate(MANUAL) / rate(ACME)
    rng = random.Random(7); boots = []
    for _ in range(5000):
        m = [rng.choice(MANUAL) for _ in MANUAL]; a = [rng.choice(ACME) for _ in ACME]
        if sum(a): boots.append(rate(m) / rate(a))
    boots.sort()
    lo, hi = boots[int(0.025 * len(boots))], boots[int(0.975 * len(boots))]
    print(f"manual {rate(MANUAL):.2f} per 100 cert-years, acme {rate(ACME):.2f}")
    print(f"rate ratio {rr:.2f}, bootstrap 95% interval {lo:.2f}-{hi:.2f} (seed 7, 5000 resamples)")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_rate.py`. Verified output:

```text
manual 4.26 per 100 cert-years, acme 0.78
rate ratio 5.48, bootstrap 95% interval 2.50-17.50 (seed 7, 5000 resamples)
```

### 6.3 Reading the interval

The bootstrap interval runs from 2.50 to 17.50 with seed 7 and 5,000 resamples. The lower bound well above 1 means the data are hard to reconcile with equal rates, but the interval is wide and asymmetric because a handful of ACME incidents dominate the denominator of the ratio. Felipe reports the interval in his abstract next to the point estimate, writing "about 2.5 to 17.5 times higher" rather than "5.48 times higher", because the single number would suggest more precision than seven events can give. A reader can then judge for themselves how much weight the finding deserves.

### 6.4 Stratifying by ownership

Within owner-known certificates, manual renewal shows 9 incidents in 335 certificate-years, 2.69 per 100, and ACME 2 in 711, 0.28 per 100, a ratio near 9.6. Within owner-missing certificates, manual shows 14 in 205, 6.83 per 100, and ACME 5 in 189, 2.65 per 100, a ratio near 2.6. Two lessons follow. Automation is associated with lower rates in both strata, so ownership does not explain the effect away. And owner-missing certificates fail more often whatever their mode: an orphaned ACME certificate fails about as often as an owned manual one. Ownership therefore matters on its own, and Felipe flags it as a second lever for the discussion chapter.

### 6.5 The change-collision description

Five of seven ACME incidents followed an infrastructure change within seven days, matching the pilot impression. Felipe reports this descriptively, as the proposal required, and adds one concrete observation from logs: in four of those five cases the ACME client had logged renewal errors for more than a week before expiry, but logs were not forwarded to monitoring. That finding is directly actionable: alerting on renewal failures, which SP 800-57 Part 1 would treat as part of planned key transition, closes a gap automation alone leaves open.

### Worked example

Felipe reports 4.26 versus 0.78 incidents per 100 certificate-years, a rate ratio of 5.48 with a bootstrap interval of 2.50 to 17.50, a lower ACME rate in both ownership strata, and unmonitored renewal errors before most ACME incidents.

> **Synthetic note.** Exposure, incidents and strata are invented teaching data.

### Errors and limits

Bootstrap intervals from very few events are unstable; with seven events, report them as rough. Stratification controls ownership only.

### Exercises

- **EX033 — Rates.** Report both renewal-mode rates per 100 certificate-years. *Rubric:* 3 = manual 4.26, ACME 0.78;; 2 = one;; 1 = counts;; 0 = none.
- **EX034 — Bootstrap interval.** Give the rate ratio and its interval with the seed. *Rubric:* 3 = 5.48, 2.50–17.50, seed 7, 5000 resamples;; 2 = ratio and interval;; 1 = ratio only;; 0 = none.
- **EX035 — Wide interval.** Why is the interval wide and asymmetric? *Rubric:* 3 = only seven ACME incidents dominate the ratio's denominator;; 2 = small sample;; 1 = bad code;; 0 = none.
- **EX036 — Stratum ratios.** Give the rate ratio within each ownership stratum. *Rubric:* 3 = about 9.6 owner-known, about 2.6 owner-missing;; 2 = one;; 1 = rates only;; 0 = none.
- **EX037 — Orphan comparison.** How does an orphaned ACME certificate compare with an owned manual one? *Rubric:* 3 = roughly the same rate (2.65 vs 2.69 per 100);; 2 = similar;; 1 = much lower;; 0 = none.
- **EX038 — Log finding.** What did logs show before ACME incidents, and what fix follows? *Rubric:* 3 = renewal errors logged over a week in 4 of 5 but not monitored; alert on renewal failures;; 2 = finding only;; 1 = fix only;; 0 = none.

### Synthesis

Rates, intervals and strata together show a robust association between automation and fewer expiries, and expose ownership and monitoring as independent levers.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure a dissertation so each chapter serves the main claim; (2) write limitations that are specific and useful; (3) turn findings into recommendations that respect evidence strength.

### 7.1 Structure around the claim

Felipe's dissertation opens with one claim: at Briarwood, ACME renewal was associated with substantially fewer expiry incidents per certificate-year than manual renewal, within both ownership strata, and most remaining ACME incidents followed unmonitored renewal failures after infrastructure changes. The literature chapter explains why this question was open; the methods chapter defines units, linking rules and pseudonymisation; the results chapter reports rates, intervals and strata; the discussion interprets them. Dr. Solberg's test for every paragraph is whether removing it would weaken the claim. Paragraphs that fail the test move to appendices or disappear.

### 7.2 Writing results plainly

The results chapter leads with the primary analysis exactly as registered, then the stratified analysis, then the descriptive change-collision finding. Each table states the unit, the exposure, the number of events and the interval method. Felipe avoids adjectives such as "dramatic" and instead writes numbers with intervals. Where an analysis was added after the pilot, such as the unknown-mode sensitivity check, he labels it. He includes the eight-certificate inventory from Chapter 2 only as an illustration in the background section, explicitly not as evidence.

### 7.3 Specific limitations

Weak limitations sections list generic caveats. Felipe writes specific ones, each with its likely direction of bias. Tickets under-record short outages fixed before anyone filed a report, which probably under-counts manual incidents more, because manual renewals are often fixed by hand within minutes. Service criticality was not measured, so automated services may be the better-maintained ones, which would exaggerate the ACME advantage. The study covers one health network with one ACME client; organisations using DNS-01 challenges with different infrastructure may see different failure patterns.

### 7.4 Recommendations proportional to evidence

From strong evidence Felipe recommends automating renewal for certificates that can use it and assigning a named owner to every certificate, because both associations held across strata. From weaker, descriptive evidence he recommends alerting on ACME renewal failures and reviewing certificate dependencies during firewall changes, framed as low-cost measures consistent with the findings rather than proven effects. He also recommends monitoring Certificate Transparency logs, defined in RFC 6962, to discover certificates missing from the inventory, framed as a hypothesis for future work, since his study never measured it.

### 7.5 Writing about cryptography responsibly

Because readers may skim, Felipe adds a short box clarifying what the study does not say. It does not say certificates or TLS are weak; the failures were operational, and the cryptography behaved as RFC 8446 and RFC 5280 require. It does not recommend extending lifetimes to reduce renewals, which would trade operational convenience for a longer exposure window for compromised keys. And it does not recommend building custom renewal scripts in place of maintained ACME clients, because home-grown tooling would reintroduce exactly the silent failures the study observed.

### Worked example

Felipe writes a claim-led dissertation, specific limitations with directions of bias, and recommendations graded by evidence strength, plus a box on what the study does not imply about cryptography.

> **Synthetic note.** Briarwood's findings are invented; RFC 6962, RFC 8446 and RFC 5280 are real.

### Errors and limits

Recommending more than the evidence supports is the most common dissertation flaw. Limitations without a direction of bias give readers little help.

### Exercises

- **EX039 — Paragraph test.** What test did Dr. Solberg apply to every paragraph? *Rubric:* 3 = would removing it weaken the main claim; if not, move or cut;; 2 = relevance;; 1 = length;; 0 = none.
- **EX040 — Table contents.** What must each results table state? *Rubric:* 3 = unit, exposure, number of events, interval method;; 2 = three;; 1 = one;; 0 = none.
- **EX041 — Ticket bias.** Which direction does ticket under-recording probably bias results, and why? *Rubric:* 3 = under-counts manual incidents more, as hand fixes happen in minutes without tickets;; 2 = direction;; 1 = none;; 0 = none.
- **EX042 — Strong versus weak recommendations.** Which recommendations rest on strong evidence and which on weak? *Rubric:* 3 = automate renewal and assign owners strong; alerting and change reviews weaker;; 2 = partial;; 1 = all strong;; 0 = none.
- **EX043 — CT recommendation.** How is Certificate Transparency monitoring framed and why? *Rubric:* 3 = as a future-work hypothesis because the study did not measure it;; 2 = framed cautiously;; 1 = proven;; 0 = none.
- **EX044 — What it does not say.** Give two things the clarification box says the study does not imply. *Rubric:* 3 = two of: TLS is weak, extend lifetimes, write custom renewal scripts;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

A claim-led structure, specific limitations and evidence-graded recommendations turn analysis into a dissertation readers can trust and act on.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) prepare for independent examination of a cryptography operations study; (2) answer challenges with evidence from the package; (3) plan dissemination to practitioners.

### 8.1 External examination

Coldwater appoints an external examiner who works on public-key infrastructure at another university. She receives the dissertation, the pseudonymised dataset and the reproducibility package, and reruns the analysis before the defense. Her pre-defense report agrees with the rate ratio and interval but questions two choices: coding expired intermediates as expiry incidents, and the decision to report unknown renewal modes separately. Felipe prepares a short response to each, pointing to the pilot log, the RFC 5280 path-validation rule and the sensitivity check, rather than restating his conclusions.

### 8.2 Answering the intermediate question

The examiner argues that an expired intermediate is the issuing authority's fault, not Briarwood's. Felipe answers that clients experienced the same failure either way, that Briarwood chose to serve that chain and was responsible for updating it, and that RFC 5280 path validation rejects any expired certificate in the path. He then shows the sensitivity result: removing the two intermediate cases changes the overall rate ratio from 5.48 to about 5.2, so the conclusion does not depend on the choice. Showing the alternative calmly answers the objection better than defending the original rule.

### 8.3 Questions about the cryptography

A committee member asks whether moving to post-quantum certificates would change the findings. Felipe answers that ML-DSA from FIPS 204 and SLH-DSA from FIPS 205 bring larger keys and signatures, and possibly hybrid chains during transition, but renewal remains an operational process. If anything, migration adds risk: new client versions, new certificate profiles and more changes, each a chance for the change collisions his study observed. He suggests that the ownership and monitoring recommendations become more, not less, important during migration. He declines to predict incident rates for migration, since his data contain none.

### 8.4 Dissemination to practitioners

After the defense Felipe writes a four-page practitioner summary for Briarwood and similar hospitals. It gives the rates and interval in plain language, a checklist of three actions (automate where possible, name an owner for every certificate, alert on renewal failures), and the clarification box on what the study does not imply. Briarwood's infrastructure lead reviews it to ensure no internal hostnames or architecture appear. Felipe also offers the anonymised codebook and linking rules for reuse, so other organisations can measure their own expiry rates in the same units.

### 8.5 Closing the study

Felipe closes the study formally. The ethics committee receives a final report, and Briarwood destroys the HMAC pseudonymisation key according to its own key-destruction procedure, consistent with SP 800-57 Part 1's lifecycle phases, so that even Felipe's dataset can no longer be linked back to hostnames. The reproducibility package stays available with a note that re-linking is impossible by design. Dr. Solberg reminds him that destroying the key is part of the study's ethics, not an inconvenience: a pseudonym is only as strong as the protection of its key.

### Worked example

Felipe answers the examiner's intermediate-certificate objection with a sensitivity result (5.48 to about 5.2), relates post-quantum migration to change-collision risk, and closes the study by having Briarwood destroy the pseudonymisation key.

> **Synthetic note.** The examiner, committee and figures are invented; FIPS 204, FIPS 205 and SP 800-57 are real.

### Errors and limits

Defensive answers that repeat conclusions convince no one; show alternatives and their effect. Never retain a pseudonymisation key past the study's need.

### Exercises

- **EX045 — Examiner's preparation.** What did the external examiner do before the defense? *Rubric:* 3 = reran the analysis from the package and wrote a report querying two choices;; 2 = reran analysis;; 1 = read it;; 0 = none.
- **EX046 — Intermediate sensitivity.** How did removing intermediate cases affect the result? *Rubric:* 3 = rate ratio from 5.48 to about 5.2, conclusion unchanged;; 2 = unchanged;; 1 = reversed;; 0 = none.
- **EX047 — Responsibility argument.** Give two reasons Felipe kept intermediates as Briarwood incidents. *Rubric:* 3 = two of: same client failure, Briarwood served the chain, path validation rejects any expired certificate;; 2 = one;; 1 = authority's fault;; 0 = none.
- **EX048 — Post-quantum effect.** How might PQ migration affect expiry risk? *Rubric:* 3 = FIPS 204/205 larger keys, hybrid chains, more changes raise change-collision risk; ownership and monitoring matter more;; 2 = partial;; 1 = no effect;; 0 = none.
- **EX049 — Practitioner checklist.** List the three actions in the practitioner summary. *Rubric:* 3 = automate where possible, name an owner, alert on renewal failures;; 2 = two;; 1 = one;; 0 = none.
- **EX050 — Key destruction.** Why does Briarwood destroy the HMAC key at closure? *Rubric:* 3 = so data can never be re-linked; pseudonym strength depends on key protection; SP 800-57 lifecycle;; 2 = privacy;; 1 = disk space;; 0 = none.

### Synthesis

Independent rerun, calm sensitivity answers, practitioner dissemination and a deliberate key destruction complete a master's study that others can verify and use.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Felipe Arantes, Dr. Ingrid Solberg, Coldwater Polytechnic, Briarwood Health Network and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Is automated ACME renewal associated with fewer expiry incidents per certificate-year than manual renewal at Briarwood?

**EX002.** A user-visible failure caused by a certificate used after its notAfter date, the validity field of RFC 5280.

**EX003.** Revocation failures and weak algorithms, because answering them would require different data from lifecycle records.

**EX004.** 412 found, 297 deduplicated, 64 after screening, 21 eligible, 9 included.

**EX005.** Title and abstract screening removed 233 records, largely papers about certificate validation bugs.

**EX006.** Most measured misissuance by certificate authorities, not expiry at operating organisations.

**EX007.** Kept in a separate list and marked as not peer reviewed, because such reports describe failures without clear methods.

**EX008.** That the issuer vouches for a public key belonging to the named subject between notBefore and notAfter; clients verify the issuer's signature along a chain to a root they trust.

**EX009.** In the CertificateVerify message, where the server signs the handshake transcript with the certificate's private key.

**EX010.** Benefit: a compromised key or wrong certificate stays useful for less time and revocation matters less. Cost: many more renewals, each of which can fail.

**EX011.** h-pacs had expired four days earlier and h-labres, h-mail and h-hr expired within 30 days; all four were manual.

**EX012.** Its renewal falls far in the future, likely after the person who installed it has changed roles, so no one remembers it.

**EX013.** If the ACME client stops working unnoticed, for example because a firewall change blocks its validation challenge.

**EX014.** That certificates lacking a recorded owner fail regardless of whether they renew manually or automatically.

**EX015.** Briarwood had already chosen each certificate's renewal mode, so it cannot be randomised; a cohort uses the existing history.

**EX016.** It adds 0.5 certificate-years of exposure.

**EX017.** Tell Briarwood's infrastructure lead on the same day.

**EX018.** An outsider can hash likely hostnames and compare results, recovering the real names.

**EX019.** h-6f292159ff in both rows, and the fresh-key comparison printed False.

**EX020.** Whether a classmate, using only the package, could regenerate every table in the dissertation.

**EX021.** Manual renewal causing forgetting, missing ownership so warnings reach nobody, and infrastructure changes breaking renewal.

**EX022.** Owner-missing in 61 percent of manual incidents and 71 percent of ACME incidents.

**EX023.** They lack denominators, so a large count may just reflect many certificates in that group rather than a higher risk.

**EX024.** Thirty-eight percent of manual certificates have no owner, compared with twenty-one percent of ACME certificates.

**EX025.** Five of seven, because a firewall or proxy change blocked the ACME challenge and the client's error logs went unwatched.

**EX026.** How critical each service is, which Briarwood does not record consistently.

**EX027.** Expiry incidents per 100 certificate-years, comparing manual with ACME renewal overall and inside the owner-known and owner-missing groups.

**EX028.** First exact subject-alternative-name matches, then the documented alias list, then independent review by two people.

**EX029.** A load balancer terminating TLS for several hosts, and an expired intermediate rather than leaf certificate.

**EX030.** As expiry incidents of the chain owner, because path validation under RFC 5280 rejects any expired certificate in the chain.

**EX031.** Filled from the ACME client's account records when possible; otherwise labelled unknown and reported as their own group.

**EX032.** Roughly four minutes per ticket, so linking about 120 tickets over two years fits in one month.

**EX033.** Manual 4.26 and ACME 0.78 incidents per 100 certificate-years.

**EX034.** Rate ratio 5.48 with bootstrap 95 percent interval 2.50 to 17.50 (seed 7, 5,000 resamples).

**EX035.** The ratio's denominator rests on just seven ACME incidents, so resamples with very few of them inflate the upper tail.

**EX036.** Roughly 9.6 among owner-known certificates and roughly 2.6 among owner-missing ones.

**EX037.** About the same: orphaned ACME certificates fail at 2.65 per 100 versus 2.69 for owned manual ones.

**EX038.** In four of five cases the ACME client logged errors for over a week unnoticed; forward renewal failures to monitoring with alerts.

**EX039.** Whether deleting the paragraph would weaken the central claim; paragraphs that would not are moved to appendices or cut.

**EX040.** The unit, the exposure measured, how many events occurred and how the interval was computed.

**EX041.** It likely under-counts manual incidents more, because staff often fix manual renewals within minutes without filing a ticket, which makes the study conservative.

**EX042.** Automating renewal and naming owners rest on associations seen in both strata; alerting on renewal failures and reviewing dependencies during changes rest on descriptive evidence.

**EX043.** As a hypothesis for future research, since the study never measured whether CT monitoring finds missing certificates.

**EX044.** For example, that TLS itself is weak and that lifetimes should be lengthened (also that custom scripts should replace maintained clients).

**EX045.** She reran the analysis from the reproducibility package and sent a report challenging the intermediate rule and the handling of unknown renewal modes.

**EX046.** The overall rate ratio moved from 5.48 to roughly 5.2, leaving the conclusion intact.

**EX047.** Clients saw the same failure, and Briarwood chose and maintained the chain it served (also, path validation rejects any expired certificate in the path).

**EX048.** Larger ML-DSA or SLH-DSA certificates, hybrid chains and many client changes increase opportunities for change collisions, making ownership and monitoring even more important.

**EX049.** Automate renewal where possible, give every certificate a named owner, and alert on renewal failures.

**EX050.** Destroying the key makes re-linking impossible, since pseudonyms are only as safe as their key, following the key-lifecycle phases in SP 800-57.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, keys and data in this book are synthetic unless a sentence cites a public source.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barker, E., & Kelsey, J. (2015). *Recommendation for random number generation using deterministic random bit generators* (NIST SP 800-90A Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-90Ar1>
- Barnes, R., Bhargavan, K., Lipp, B., & Wood, C. (2022). *Hybrid public key encryption* (RFC 9180). IETF. <https://www.rfc-editor.org/rfc/rfc9180>
- Barnes, R., Hoffman-Andrews, J., McCarney, D., & Kasten, J. (2019). *Automatic certificate management environment (ACME)* (RFC 8555). IETF. <https://www.rfc-editor.org/rfc/rfc8555>
- Biryukov, A., Dinu, D., Khovratovich, D., & Josefsson, S. (2021). *Argon2 memory-hard function for password hashing and proof-of-work applications* (RFC 9106). IETF. <https://www.rfc-editor.org/rfc/rfc9106>
- Boneh, D., & Shoup, V. (2023). *A graduate course in applied cryptography* (version 0.6, draft). <https://toc.cryptobook.us/>
- Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 public key infrastructure certificate and CRL profile* (RFC 5280). IETF. <https://www.rfc-editor.org/rfc/rfc5280>
- Dworkin, M. (2007). *Recommendation for block cipher modes of operation: Galois/Counter Mode (GCM) and GMAC* (NIST SP 800-38D). NIST. <https://doi.org/10.6028/NIST.SP.800-38D>
- Josefsson, S., & Liusvaara, I. (2017). *Edwards-curve digital signature algorithm (EdDSA)* (RFC 8032). IETF. <https://www.rfc-editor.org/rfc/rfc8032>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Krawczyk, H., & Eronen, P. (2010). *HMAC-based extract-and-expand key derivation function (HKDF)* (RFC 5869). IETF. <https://www.rfc-editor.org/rfc/rfc5869>
- Krawczyk, H., Bellare, M., & Canetti, R. (1997). *HMAC: Keyed-hashing for message authentication* (RFC 2104). IETF. <https://www.rfc-editor.org/rfc/rfc2104>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Langley, A., Hamburg, M., & Turner, S. (2016). *Elliptic curves for security* (RFC 7748). IETF. <https://www.rfc-editor.org/rfc/rfc7748>
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate transparency* (RFC 6962). IETF. <https://www.rfc-editor.org/rfc/rfc6962>
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- Moriarty, K., Kaliski, B., Jonsson, J., & Rusch, A. (2016). *PKCS #1: RSA cryptography specifications version 2.2* (RFC 8017). IETF. <https://www.rfc-editor.org/rfc/rfc8017>
- National Institute of Standards and Technology. (2001, updated 2023). *Advanced Encryption Standard (AES)* (FIPS 197). <https://doi.org/10.6028/NIST.FIPS.197-upd1>
- National Institute of Standards and Technology. (2008). *The keyed-hash message authentication code (HMAC)* (FIPS 198-1). <https://doi.org/10.6028/NIST.FIPS.198-1>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2023). *Digital signature standard (DSS)* (FIPS 186-5). <https://doi.org/10.6028/NIST.FIPS.186-5>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Shoup, V. (2004). *Sequences of games: A tool for taming complexity in security proofs* (Cryptology ePrint Archive, Paper 2004/332). <https://eprint.iacr.org/2004/332>
