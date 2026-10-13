# Cryptography and Trust Services: Technologist Course

- Language: English (`en`); course 077, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; six offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technology implementers and administrators.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: labs parse logs, plan renewals, verify HMACs and call hashlib's scrypt against a published vector; they implement no cipher. Production systems use vetted libraries, ACME clients, HSMs and supplier products; never roll your own cryptography. All people, organisations and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one technologist student through foundations, a council placement and a capstone: encoding versus encryption, TLS and certificates, inventories, data flows, risk, webhook verification, a lab certificate authority, password storage, tooling, controls, monitoring, troubleshooting, integration, automation, evaluation, research, teamwork, handoff, deployment, field practice and the capstone. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Rosa Delgado** | Technologist student | Invented |
| **Owen Pryce** | Placement mentor, council IT | Invented |
| **Dr Imogen Hale** | Tutor | Invented |
| **Pinecrest Polytechnic** | Fictional school | Invented |
| **Harbourview City Council** | Fictional local government | Invented |

### Core sources

[RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280); [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555); [RFC 2104](https://www.rfc-editor.org/rfc/rfc2104); [RFC 7914](https://www.rfc-editor.org/rfc/rfc7914); NIST [SP 800-52 Rev. 2](https://doi.org/10.6028/NIST.SP.800-52r2) and [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing systems

### Learning outcomes

You will (1) describe the systems a city runs and where cryptography appears in them; (2) distinguish hardware, software and services; (3) identify cryptographic dependencies in everyday services.

### 1.1 The case

Rosa Delgado is a first-year student in the three-year technologist programme at the fictional Pinecrest Polytechnic. Her work placement, which runs through all three years, is with the IT department of the fictional Harbourview City Council, under senior engineer Owen Pryce. The council runs a parking-permit portal, a document service for signed council decisions, a staff VPN, a geographic information system and payment integrations. Every system, person and figure in this book is synthetic. A technologist builds and runs integrated services, so Rosa's goal is to make these services trustworthy in daily operation, not to invent new cryptography.

### 1.2 Hardware, software and services

Rosa sorts the council's systems into hardware, such as servers, laptops and network appliances; software, such as operating systems, web servers and databases; and services bought from outside, such as the payment provider and the email platform. Cryptography shows up in each: laptops encrypt disks, web servers terminate TLS, databases encrypt backups and the payment provider signs notifications. Owen asks her to note for each item who controls the keys. She finds that for outside services the provider holds the keys, which means the council must rely on contracts and the provider's controls rather than its own configuration.

### 1.3 Everyday dependencies

Rosa traces one citizen action, buying a parking permit, from start to finish. The browser connects to the portal over TLS; the portal checks the citizen's password against a stored hash; it calls the payment provider, which later sends a signed notification back; and the permit record is stored in an encrypted database with nightly encrypted backups. Five separate cryptographic mechanisms support one simple task. If any one fails, for example an expired certificate or a wrong webhook secret, citizens see errors. This exercise shows Rosa why service integration and operations are central to applied cryptography.

### Worked example

Rosa maps the permit purchase through TLS, password hashing, a signed payment notification and encrypted storage, and notes who holds each key.

> **Synthetic case.** Harbourview, Pinecrest and all systems are invented.

### Errors and limits

Diagrams of one transaction miss background processes such as backups and logging. Outside services move key control to providers, so contracts matter.

### Exercises

- **EX001 — Placement setting.** Where does Rosa's placement take place and what does a technologist focus on? *Rubric:* 3 = Harbourview City Council IT; making integrated services trustworthy in operation;; 2 = setting only;; 1 = inventing cryptography;; 0 = none.
- **EX002 — Provider keys.** Who holds the keys for outside services, and what follows? *Rubric:* 3 = the provider; council relies on contracts and provider controls;; 2 = provider;; 1 = council;; 0 = none.
- **EX003 — Permit mechanisms.** Name four cryptographic mechanisms in a permit purchase. *Rubric:* 3 = four of TLS, password hash, signed notification, database encryption, backup encryption;; 2 = three;; 1 = one;; 0 = none.

### Synthesis

Even simple public services depend on several cryptographic mechanisms whose keys and owners must be known.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) explain DNS, HTTP and TLS in a city web service; (2) describe what TLS certificates prove; (3) recognise common network-level failures.

### 2.1 How a request travels

When a citizen types permits.harbourview.example, the browser asks DNS for the server's address, opens a TCP connection and starts a TLS handshake before sending any HTTP request. Rosa learns the order matters: DNS answers are not protected by TLS, so an attacker who poisons DNS could direct the browser elsewhere, but TLS certificate checks would then fail because the attacker cannot present a valid certificate for the council's name. This is why certificate validation is the anchor of web security: it detects redirection that lower layers cannot stop. She practises tracing these steps in a lab with test domains.

### 2.2 What a certificate proves

A TLS certificate binds the name permits.harbourview.example to a public key, signed by a certificate authority the browser trusts. RFC 5280 defines the fields, including subject alternative names and validity dates. The certificate proves that whoever completes the handshake holds the private key for that name; it does not prove the site is safe or that the council's code is bug-free. Rosa explains this to the council's communications team, who had told citizens that "the padlock means your data is safe", and suggests more accurate wording about the connection being private.

### 2.3 Common failures

Rosa lists network failures she will meet: expired certificates, certificates missing a needed name, incomplete chains where the server does not send the intermediate certificate, clocks set wrong on clients and old clients that cannot negotiate modern TLS versions defined in RFC 8446. Each produces a different browser error. She builds a one-page guide mapping error messages to likely causes for the service desk, so that first-line staff can collect the right details before escalating. The guide later reduces time spent diagnosing simple certificate problems.

### Worked example

Rosa traces DNS, TCP and TLS for the permit site, corrects the "padlock means safe" wording and writes an error-to-cause guide for the service desk.

> **Synthetic case.** Domains and teams are invented; RFC 5280 and RFC 8446 are real.

### Errors and limits

TLS does not protect DNS lookups by itself. A valid certificate says nothing about application security.

### Exercises

- **EX004 — DNS and TLS.** Why does certificate validation still protect a citizen if DNS is poisoned? *Rubric:* 3 = attacker cannot present a valid certificate for the council's name;; 2 = valid cert;; 1 = it doesn't;; 0 = none.
- **EX005 — Padlock wording.** What did Rosa suggest instead of "the padlock means your data is safe"? *Rubric:* 3 = wording that the connection is private, not that the site or data is safe;; 2 = accurate;; 1 = unchanged;; 0 = none.
- **EX006 — Incomplete chain.** What is an incomplete chain failure? *Rubric:* 3 = the server does not send the intermediate certificate;; 2 = missing intermediate;; 1 = expired;; 0 = none.

### Synthesis

Web security rests on certificate validation over layers that are otherwise unprotected; knowing failure patterns speeds diagnosis.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write simple Python scripts for operations; (2) distinguish encoding from encryption; (3) handle secrets in scripts safely.

### 3.1 Scripts for operations

Technologists automate routine work with scripts. Rosa's first scripts read CSV exports of the council's certificate list and print those expiring within thirty days. She learns to use the standard library: csv for reading files, datetime for date arithmetic and argparse for command-line options. She writes small functions with clear names and tests each with sample data before running against real exports. Owen reviews her code and asks her to handle bad rows gracefully, since exports from older systems sometimes contain blank dates that would otherwise crash the script.

### Lab — Encoding is not encryption

```python
"""Encoding is not encryption: Base64 and hex are reversible by anyone (synthetic permit record)."""
import base64
REC = b"permit=PK-2291;plate=HRV-447;zone=4"

def main():
    b64 = base64.b64encode(REC).decode()
    print("base64:", b64)
    print("decoded without any key:", base64.b64decode(b64).decode())
    print("hex:", REC.hex()[:32], "...")
    print("length grows by", len(b64) - len(REC), "chars; secrecy added: none")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_encoding.py`. Verified output:

```text
base64: cGVybWl0PVBLLTIyOTE7cGxhdGU9SFJWLTQ0Nzt6b25lPTQ=
decoded without any key: permit=PK-2291;plate=HRV-447;zone=4
hex: 7065726d69743d504b2d323239313b70 ...
length grows by 13 chars; secrecy added: none
```

### 3.2 Reading the encoding lab

The lab Base64-encodes a synthetic permit record. The output looks scrambled, but decoding it needs no key and prints the original record exactly. Hex encoding likewise only changes representation. Base64 makes the text thirteen characters longer and adds no secrecy. Rosa finds a council integration that "protected" permit data in transit by Base64-encoding it inside an unencrypted HTTP request. She reports it, and the integration is moved to HTTPS with TLS. The lesson is simple but important: encoding is for transport and storage formats, while confidentiality needs encryption with a key.

### 3.3 Secrets in scripts

Rosa's next script calls an internal API that needs a token. Her first version writes the token directly in the code, which Owen rejects: code gets copied, shared and committed to repositories. She moves the token to an environment variable populated by the council's secret store and makes the script fail clearly if it is missing. She also avoids printing tokens in logs and uses the secrets module when a script must generate a random value, never the random module. These habits apply to every script she writes afterward.

### Worked example

Rosa writes a certificate-expiry script with tolerant parsing, shows Base64 adds no secrecy, gets a Base64-over-HTTP integration moved to TLS and moves an API token out of code.

> **Synthetic case.** The permit record and integration are invented.

### Errors and limits

Obfuscation such as Base64 misleads people into thinking data is protected. Environment variables are better than code but still need a secret store behind them.

### Exercises

- **EX007 — Bad rows.** What did Owen ask Rosa to handle in her expiry script? *Rubric:* 3 = blank or bad rows from older exports without crashing;; 2 = bad rows;; 1 = speed;; 0 = none.
- **EX008 — Base64 finding.** What did Rosa find and what fixed it? *Rubric:* 3 = permit data Base64-encoded over plain HTTP; moved to HTTPS;; 2 = finding and fix;; 1 = one;; 0 = none.
- **EX009 — Token handling.** Where did Rosa move the API token, and why? *Rubric:* 3 = to an environment variable from the secret store, since code is copied and committed;; 2 = env var;; 1 = left in code;; 0 = none.

### Synthesis

Operational scripting needs clean data handling, a clear grasp that encoding is not encryption and disciplined handling of secrets.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) model certificates, keys and owners as data; (2) design a simple inventory table; (3) keep sensitive values out of inventories.

### 4.1 Modelling trust objects

Rosa designs a data model for the council's certificates and keys. A certificate record holds the host name, issuer, serial number, expiry date, renewal method and owner. A key record holds its purpose, algorithm, location, creation date and owner. Each record has a unique identifier, and certificates link to the key they use. She deliberately stores no private keys or secrets in the model: the inventory describes keys, it never contains them. SP 800-57 Part 1 stresses that organisations must know their keys, and a well-designed model is the first step to that knowledge.

### 4.2 Designing the table

Using a lightweight database, Rosa creates tables for certificates, keys, owners and services, with relationships between them. She adds constraints: every certificate must have an owner and an expiry date; renewal method must be one of acme, internal-ca or manual. Constraints catch errors at entry time rather than during an outage. She imports existing spreadsheets and finds thirty rows with no owner, which she flags for follow-up. Owen notes that the act of loading data into a stricter model often reveals more than any report.

### 4.3 Keeping secrets out

A colleague asks whether the inventory could also store the passwords for service accounts "to keep everything in one place". Rosa explains why not: the inventory is read by many people, exported to reports and backed up widely, so storing secrets there would expose them. Secrets belong in a dedicated secret store with access control and audit logs. The inventory can record where a secret is stored and who owns it. Separating description from secret is a pattern she will reuse in every system she designs.

### Worked example

Rosa's inventory model links certificates, keys, owners and services with constraints, finds thirty ownerless rows and refuses to store service passwords in it.

> **Synthetic case.** The inventory is invented; SP 800-57 Part 1 is real.

### Errors and limits

Inventories decay without updates from automation. Mixing secrets into descriptive data exposes them widely.

### Exercises

- **EX010 — Certificate fields.** List four fields of a certificate record. *Rubric:* 3 = four of host, issuer, serial, expiry, renewal method, owner;; 2 = three;; 1 = one;; 0 = none.
- **EX011 — Constraint benefit.** Why add constraints such as requiring an owner? *Rubric:* 3 = catch errors at entry rather than during outages;; 2 = early errors;; 1 = slower;; 0 = none.
- **EX012 — Passwords request.** Why must service passwords not go into the inventory? *Rubric:* 3 = widely read, exported and backed up; secrets belong in a secret store;; 2 = exposure;; 1 = fine;; 0 = none.

### Synthesis

A clear data model for trust objects, enforced with constraints and kept free of secrets, makes keys and certificates manageable.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain core cryptographic goals in council terms; (2) match tools to goals; (3) correct common staff misunderstandings.

### 5.1 Goals in council terms

Rosa explains cryptographic goals using council examples. Confidentiality keeps citizens' addresses and payment references private. Integrity ensures a signed council decision has not been altered after approval. Authentication confirms that a payment notification really came from the payment provider. Availability, though not provided by cryptography, can be harmed by it when certificates expire or keys are lost. Framing goals around real services helps non-technical colleagues see why each control exists, and helps Rosa decide which tool fits each need rather than reaching for encryption by habit.

### 5.2 Matching tools

Rosa builds a simple table. Encryption, such as AES-GCM from SP 800-38D, provides confidentiality and, being authenticated, integrity for stored or transmitted data. Hashing with SHA-256 from FIPS 180-4 provides fingerprints for integrity checks when the expected hash is trusted. HMAC from RFC 2104 authenticates messages between parties sharing a secret, such as payment webhooks. Digital signatures, such as Ed25519 from RFC 8032, let anyone verify signed council decisions with a public key. She adds a column for who holds keys in each case, connecting tools to operations.

### 5.3 Correcting misunderstandings

Rosa collects misunderstandings from colleagues: "We encrypt passwords so we can email them back if people forget"; "the PDF is signed, so it's confidential"; and "our VPN means internal websites don't need TLS". She corrects each gently: passwords should be hashed, not reversibly encrypted, so nobody can recover them; signatures prove origin and integrity but do not hide content; and internal traffic still benefits from TLS because insiders and compromised devices exist. She turns the list into a short quiz for new staff.

### Worked example

Rosa maps four goals to council services, builds a tool table with key holders and corrects three staff misunderstandings in a quiz.

> **Synthetic case.** Colleague quotes are invented.

### Errors and limits

Tables oversimplify; authenticated encryption, for example, provides more than one goal. Availability depends on operations, not on algorithms.

### Exercises

- **EX013 — Integrity example.** Which council example illustrates integrity? *Rubric:* 3 = a signed council decision not altered after approval;; 2 = example;; 1 = confidentiality example;; 0 = none.
- **EX014 — Webhook tool.** Which tool suits payment webhooks, and why? *Rubric:* 3 = HMAC, as both parties share a secret and need message authentication;; 2 = HMAC;; 1 = encryption;; 0 = none.
- **EX015 — Password misconception.** Correct "we encrypt passwords so we can email them back". *Rubric:* 3 = passwords should be hashed so nobody can recover them; use reset instead;; 2 = hash;; 1 = agree;; 0 = none.

### Synthesis

Security literacy means matching each cryptographic tool to a concrete goal and correcting misconceptions in plain language.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) protect keys on Linux servers and virtual machines; (2) understand risks of cloning and snapshots; (3) use the operating system's secure randomness.

### 6.1 Keys on servers

The council's web servers hold TLS private keys. Rosa checks their storage: keys should be readable only by the web server's account, never by all users, and should not sit in home directories or shared folders. She finds one server where the key file is readable by every account, a leftover from troubleshooting. She corrects the permissions, records the change and adds a weekly check that reports key files with loose permissions. Operating-system permissions are a basic but powerful key control.

### 6.2 Cloning and snapshots

Virtual machines can be cloned and snapshotted, which is convenient but risky for cryptography. A cloned server carries the same private keys as the original, so two machines now hold one identity. Snapshots may capture keys and random generator state in memory. Rosa learns that the council's template image included a pre-generated SSH host key, so every new virtual machine had the same key. She fixes the template to generate keys on first boot and replaces the duplicated keys, documenting how many machines were affected.

### 6.3 Randomness in virtual machines

Freshly started virtual machines may have little entropy, and cloned machines might start with identical generator states. Modern operating systems handle this better by seeding from the hypervisor and hardware sources, and NIST SP 800-90A describes the generator designs they use. Rosa checks that the council's Linux images use the kernel's getrandom interface, which blocks until the generator is seeded, and that applications use it, for example through Python's secrets module. She notes that applications should never maintain their own homemade random generators.

### Worked example

Rosa fixes a world-readable TLS key, removes a duplicated SSH host key from the VM template and confirms images use properly seeded system randomness.

> **Synthetic case.** Servers and images are invented; SP 800-90A is real.

### Errors and limits

Snapshots and backups can contain keys; protect them like keys. Fixing a template does not fix machines already cloned from it.

### Exercises

- **EX016 — Key permissions.** What permission problem did Rosa find? *Rubric:* 3 = a TLS key file readable by every account;; 2 = readable;; 1 = vague;; 0 = none.
- **EX017 — Template flaw.** What was wrong with the VM template? *Rubric:* 3 = it contained a pre-generated SSH host key shared by all clones;; 2 = shared key;; 1 = vague;; 0 = none.
- **EX018 — getrandom.** Why use getrandom on new VMs? *Rubric:* 3 = it blocks until the generator is seeded, avoiding weak early randomness;; 2 = seeded;; 1 = faster;; 0 = none.

### Synthesis

Operating systems and virtualization shape key safety through permissions, templates and seeded randomness.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) explain how certificates and tokens identify users and devices; (2) configure multi-factor authentication for staff; (3) manage access changes when staff move or leave.

### 7.1 Identities and credentials

Rosa learns that identities can be proven with passwords, one-time codes, security keys and certificates. The council's staff VPN uses device certificates issued by an internal certificate authority plus a staff password and one-time code. The certificate shows the device is council-managed; the password and code show the person is authorised. Rosa explains to new staff that losing a laptop therefore requires both revoking the device certificate and checking the account, because the two credentials prove different things. Rosa also notes that each credential type has a different lifetime and revocation path, which must be written beside it in the inventory.

### 7.2 Multi-factor rollout

Owen asks Rosa to help roll out phishing-resistant security keys for administrators. Security keys sign a challenge that includes the website's origin, so a fake login page cannot reuse the response. Rosa prepares instructions, registers two keys per administrator so a lost key does not lock anyone out and tests recovery. She keeps one-time codes as a fallback for staff without security keys. She tracks adoption weekly and reaches all administrators within a month. She tracks enrolment weekly, chasing the last few teams personally, because a rollout that stalls at ninety percent leaves the weakest accounts unprotected.

### 7.3 Joiners, movers and leavers

Access must change when staff join, change roles or leave. Rosa reviews the council's process and finds that device certificates for leavers were sometimes not revoked for weeks. She adds a step to the leaver checklist that revokes the certificate and disables tokens on the last working day, and a monthly report comparing active certificates with the staff directory. She learns that cryptographic credentials are only as good as the processes that issue and withdraw them. Leaver processing is checked monthly against the human resources list, and any certificate still valid for a departed person is revoked the same day.

### Worked example

Rosa explains device certificates versus personal credentials, rolls out two security keys per administrator, and adds certificate revocation to the leaver checklist with a monthly reconciliation.

> **Synthetic case.** Processes and figures are invented.

### Errors and limits

Strong authentication does not limit what an authenticated user may do. Spare security keys must themselves be stored securely.

### Exercises

- **EX019 — Two credentials.** What do the device certificate and the password-plus-code each prove? *Rubric:* 3 = certificate: council-managed device; password and code: authorised person;; 2 = both;; 1 = one;; 0 = none.
- **EX020 — Two keys.** Why register two security keys per administrator? *Rubric:* 3 = so a lost key does not lock them out;; 2 = backup;; 1 = security;; 0 = none.
- **EX021 — Leaver gap.** What gap did Rosa find in the leaver process? *Rubric:* 3 = device certificates not revoked for weeks;; 2 = delay;; 1 = vague;; 0 = none.

### Synthesis

Certificates and tokens identify devices and people, but issuance and revocation processes decide their real strength.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) draw trust boundaries for council services; (2) place TLS, signatures and encryption at the right boundaries; (3) identify single points of failure in trust infrastructure.

### 8.1 Trust boundaries

Rosa draws the permit service architecture with trust boundaries: between the internet and the web gateway, between the gateway and application servers, between applications and the database, and between the council and the payment provider. She marks which data crosses each boundary and how it is protected. The diagram shows that the gateway terminates TLS and forwards traffic to applications over plain HTTP inside the data centre, a design chosen years ago for simplicity. She records it as a gap.

### 8.2 Placing controls

Rosa proposes controls at each boundary: TLS from citizens to the gateway, TLS with mutual authentication from gateway to applications, database connections over TLS with certificate checks, HMAC-signed webhooks from the payment provider, and signed PDFs for council decisions. Owen reviews the proposal and agrees, but asks her to estimate the operational load of the extra certificates. She answers that automated issuance from the internal authority will keep the load small, which leads to the automation work in later chapters.

### 8.3 Single points of failure

The diagram also reveals that the internal certificate authority runs on one virtual machine without a backup of its signing key, and that the same administrator account manages it and the gateway. If the machine failed, no new internal certificates could be issued; if the account were compromised, an attacker could issue certificates and redirect traffic. Rosa recommends an encrypted backup of the authority's key held under dual control and separate administrator accounts. Both recommendations are added to the council's risk register.

### Worked example

Rosa's architecture diagram reveals plain HTTP behind the gateway and a single, unbacked internal CA, and she proposes boundary controls and dual-controlled backups.

> **Synthetic case.** The architecture is invented.

### Errors and limits

Internal networks are not automatically trustworthy. More certificates mean more operations unless issuance is automated.

### Exercises

- **EX022 — Internal gap.** What gap did the diagram reveal behind the gateway? *Rubric:* 3 = traffic forwarded to applications over plain HTTP;; 2 = plain HTTP;; 1 = vague;; 0 = none.
- **EX023 — Webhook control.** Which control protects payment webhooks? *Rubric:* 3 = HMAC signatures from the payment provider;; 2 = HMAC;; 1 = TLS only;; 0 = none.
- **EX024 — CA weakness.** Why is the internal CA a single point of failure? *Rubric:* 3 = one VM without key backup, managed by the same account as the gateway;; 2 = both;; 1 = one;; 0 = none.

### Synthesis

Drawing trust boundaries places cryptographic controls where they matter and exposes fragile trust infrastructure.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) read TLS failure logs to find causes; (2) count and classify events reliably; (3) report evidence clearly to engineers and managers.

### 9.1 Logs as evidence

When citizens report "the site is broken", logs tell what actually happened. The council's web gateway records failed TLS handshakes with a client address, a reason code and the target host. Rosa learns to read these logs before guessing. Reason codes such as certificate_expired, protocol_version, unknown_ca and handshake_timeout point to different fixes. She writes a small parser using only the standard library to summarise a morning's failures, working on a synthetic sample with addresses from a private range.

### Lab — Handshake failure summary

```python
"""Count reasons in a synthetic TLS handshake-failure log from a city web gateway."""
from collections import Counter
LOG = """\
2026-03-02T08:01Z fail client=10.2.0.14 reason=certificate_expired host=permits
2026-03-02T08:03Z fail client=10.2.0.31 reason=protocol_version host=legacy-gis
2026-03-02T08:07Z fail client=10.2.0.14 reason=certificate_expired host=permits
2026-03-02T08:11Z fail client=10.2.7.90 reason=unknown_ca host=staff-vpn
2026-03-02T08:12Z fail client=10.2.0.55 reason=certificate_expired host=permits
2026-03-02T08:20Z fail client=10.2.0.31 reason=protocol_version host=legacy-gis
2026-03-02T08:24Z fail client=10.2.3.12 reason=handshake_timeout host=permits"""

def main():
    rows = [dict(kv.split("=") for kv in ln.split()[2:]) for ln in LOG.splitlines()]
    for (r, h), n in Counter((x["reason"], x["host"]) for x in rows).most_common():
        print(f"{n}  {r:<20} {h}")
    print("distinct clients hitting expired cert:", len({x["client"] for x in rows if x["reason"] == "certificate_expired"}))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_tlslog.py`. Verified output:

```text
3  certificate_expired  permits
2  protocol_version     legacy-gis
1  unknown_ca           staff-vpn
1  handshake_timeout    permits
distinct clients hitting expired cert: 2
```

### 9.2 Reading the summary

Of seven failures, three are certificate_expired on the permits host from two distinct clients, two are protocol_version on legacy-gis from one old client, one is unknown_ca on staff-vpn and one is a timeout on permits. Rosa concludes that the permits certificate is the urgent problem, affecting citizens; the legacy GIS failures come from one outdated client that cannot negotiate a modern TLS version; and the unknown CA error suggests a staff device missing the internal root. She separates each into its own ticket with the evidence attached, rather than one vague "TLS problem" ticket.

### 9.3 Reporting clearly

For engineers Rosa reports counts, hosts, reason codes and time ranges. For managers she writes two sentences: citizens could not renew permits for about twenty minutes because a certificate expired, and it was renewed at 08:30; two minor issues affect a GIS client and one staff device. She avoids exaggerating and includes when evidence is incomplete, such as failures not logged when the gateway was overloaded. Clear, audience-appropriate reporting helps the council act quickly and builds trust in IT's information. She closes each report with one recommended next step, so readers who skim still know exactly what to do.

### Worked example

Rosa parses a synthetic failure log, identifies the expired permits certificate as urgent, splits three issues into tickets and writes separate summaries for engineers and managers.

> **Synthetic case.** The log is invented.

### Errors and limits

Logs may miss events during overload. Reason codes depend on server software and can be ambiguous.

### Exercises

- **EX025 — Reason codes.** Name three TLS failure reason codes and what they suggest. *Rubric:* 3 = e.g. certificate_expired (renew), protocol_version (old client), unknown_ca (missing root);; 2 = two;; 1 = one;; 0 = none.
- **EX026 — Urgent issue.** Which issue did Rosa rank most urgent and why? *Rubric:* 3 = expired permits certificate, affecting citizens (3 failures, 2 clients);; 2 = issue;; 1 = other;; 0 = none.
- **EX027 — Manager summary.** What did the manager summary say? *Rubric:* 3 = citizens blocked about twenty minutes by expired certificate, renewed 08:30; two minor issues;; 2 = partial;; 1 = technical detail;; 0 = none.

### Synthesis

Reading logs carefully, classifying events and reporting to each audience turns cryptographic failures into actionable evidence.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Cryptography and trust services: orientation

### Learning outcomes

You will (1) define the trust services a council relies on; (2) explain who trusts whom in each; (3) identify the council's roles as consumer and provider of trust.

### 10.1 Trust services around the council

Rosa lists the trust services Harbourview uses: a public certificate authority for its websites; an internal certificate authority for staff devices and internal services; a document-signing service for council decisions; a timestamping service that proves when documents were signed; and the payment provider's webhook signatures. Each is a service whose assertions others rely on. She notes that the council is both a consumer of trust, relying on the public authority, and a provider, since citizens and partners rely on its signed decisions.

### 10.2 Who trusts whom

For each service Rosa writes who trusts whom. Browsers trust the public authority, which vouches for the council's websites. Council servers trust the internal authority, which vouches for devices. Citizens and courts trust the council's signing certificate, which vouches for decisions. The council trusts the payment provider's webhook key, which vouches for payment notices. RFC 5280 explains how certificate chains express such delegations. Writing these relations makes clear that a failure at one link, such as a stolen signing key, harms all who rely on it.

### 10.3 The council as a provider

Because the council signs decisions that citizens and courts may rely on years later, it carries a provider's responsibilities: protecting the signing key, documenting how signatures are made, keeping evidence for long-term validation and revoking promptly if a key is compromised. Rosa compares this with its consumer role, where it mainly configures and monitors. The distinction helps her explain to managers why the document-signing service deserves stronger controls than an ordinary web certificate. Rosa realises that partners judge the council by these details, and a single expired certificate on a public form erodes trust that took years to build.

### Worked example

Rosa lists five trust services, maps who trusts whom and explains why the council's signing role carries provider responsibilities.

> **Synthetic case.** The council's services are invented; RFC 5280 is real.

### Errors and limits

Trust relations change when suppliers change; review them. Providers of trust need evidence that lasts as long as reliance does.

### Exercises

- **EX028 — Five services.** Name the five trust services the council uses. *Rubric:* 3 = public CA, internal CA, document signing, timestamping, payment webhook signatures;; 2 = four;; 1 = two;; 0 = none.
- **EX029 — Webhook trust.** Who trusts whom for payment notices? *Rubric:* 3 = the council trusts the payment provider's webhook key;; 2 = partly correct;; 1 = reversed;; 0 = none.
- **EX030 — Provider duties.** List three provider responsibilities for signed decisions. *Rubric:* 3 = three of protect key, document process, keep evidence for long-term validation, revoke promptly;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

Trust services define who relies on whom; the council's role as signer brings duties beyond those of a consumer.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Cryptography and trust services: assets and context

### Learning outcomes

You will (1) inventory cryptographic assets across council services; (2) rate each asset's importance; (3) record context such as legal retention and suppliers.

### 11.1 Building the asset list

Using her Chapter 4 model, Rosa populates the inventory: 58 certificates, 14 keys in the key service, the internal CA signing key, the document-signing key and two webhook secrets. She gathers data from scanning authorised hosts, exports from the key service and interviews with service owners. Each asset gets an owner and a service link. She discovers a certificate for an old events website that was retired years ago but still renewed automatically, wasting effort and widening the attack surface. It is removed after the owner confirms.

### 11.2 Rating importance

Rosa rates assets by the harm their compromise or loss would cause. The document-signing key is rated critical because forged decisions could have legal effect. The internal CA key is critical because it could mint any internal identity. Public website certificates are high: compromise would allow impersonation, but they are short-lived and replaceable. Webhook secrets are high because forged payment notices could issue permits without payment. Ratings determine which controls, such as hardware protection and dual control, each asset receives.

### 11.3 Recording context

Some context changes requirements. Signed decisions must remain verifiable for at least ten years under the council's records policy, so the signing process needs timestamps and archived validation data. The payment webhook secret is shared with a supplier under a contract that requires rotation on request. Certain staff certificates are issued to contractors whose access ends with their contracts. Rosa records such context in the inventory, because a key's handling depends not only on its algorithm but on legal, contractual and organisational facts.

### Worked example

Rosa inventories 58 certificates and other keys, removes a stale events certificate, rates the signing and CA keys critical and records a ten-year verification requirement.

> **Synthetic case.** Counts and policies are invented.

### Errors and limits

Ratings are judgements and should be reviewed. Inventories built once and never updated soon mislead.

### Exercises

- **EX031 — Stale certificate.** What wasteful asset did Rosa discover? *Rubric:* 3 = certificate for a retired events website still auto-renewing;; 2 = stale cert;; 1 = vague;; 0 = none.
- **EX032 — Critical assets.** Which two assets were rated critical and why? *Rubric:* 3 = document-signing key (forged decisions) and internal CA key (mint any identity);; 2 = one;; 1 = vague;; 0 = none.
- **EX033 — Ten-year context.** What does the ten-year requirement imply for signing? *Rubric:* 3 = need timestamps and archived validation data for long-term verification;; 2 = timestamps;; 1 = vague;; 0 = none.

### Synthesis

An inventory rated by harm and enriched with legal and contractual context tells each asset what protection it deserves.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Cryptography and trust services: data flows

### Learning outcomes

You will (1) trace data flows between council services and partners; (2) identify protection gaps in each flow; (3) prioritise fixes by sensitivity and exposure.

### 12.1 Tracing flows

Rosa traces data flows for the permit and document services: citizen to gateway, gateway to application, application to database, application to payment provider, provider back to application by webhook, application to document-signing service, signed documents to the archive and backups to off-site storage. For each flow she records data type, protocol, protection and who controls the keys. She uses a simple table rather than an elaborate diagram, because the table can be sorted and filtered when planning fixes. She also records the frequency of each flow, since a nightly batch and a constant stream call for different monitoring.

### 12.2 Finding gaps

The table shows gaps: plain HTTP between gateway and applications, noted earlier; backups encrypted with a key stored on the backup server itself, so anyone stealing the server gets both; and signed documents archived without the timestamp and certificate status data needed for long-term validation. One flow, the export of permit data to a parking-enforcement contractor, travels as an emailed spreadsheet. Rosa flags it as the most exposed because it leaves the council's control entirely and has no encryption. She also notices that nobody could say who owned the export, which explains why it was never reviewed.

### 12.3 Prioritising fixes

Rosa ranks fixes by sensitivity of the data and exposure of the flow. The emailed export ranks first: personal data leaves the council unprotected. Next comes the backup key stored with backups, then the internal HTTP hop, then archive validation data. For the export she proposes a secure file transfer with TLS and per-file encryption to the contractor's public key, using a vetted tool. Owen approves the ranking and asks her to write the change requests, which she does with rollback plans.

### Worked example

Rosa's flow table finds four gaps and ranks an emailed permit export first, proposing secure transfer with encryption to the contractor's key.

> **Synthetic case.** Flows and contractor are invented.

### Errors and limits

Flow tables omit undocumented "shadow" flows; ask owners. Encrypting backups with a key stored beside them gives little protection.

### Exercises

- **EX034 — Table choice.** Why does Rosa use a table for flows? *Rubric:* 3 = it can be sorted and filtered when planning fixes;; 2 = sortable;; 1 = prettier;; 0 = none.
- **EX035 — Backup gap.** What was wrong with backup encryption? *Rubric:* 3 = key stored on the backup server itself;; 2 = key beside data;; 1 = vague;; 0 = none.
- **EX036 — Top fix.** Which flow ranked first and what fix was proposed? *Rubric:* 3 = emailed permit export; secure transfer with TLS and per-file encryption to contractor's key;; 2 = flow;; 1 = fix;; 0 = none.

### Synthesis

Tracing data flows with key ownership exposes gaps that diagrams miss, and ranking by sensitivity and exposure focuses effort.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Cryptography and trust services: risk scenarios

### Learning outcomes

You will (1) write risk scenarios for trust services; (2) estimate likelihood and impact; (3) choose treatments and owners.

### 13.1 Writing scenarios

Rosa writes scenarios in a consistent form: cause, event, consequence. A contractor laptop with a staff device certificate is stolen, the certificate is used to reach the VPN, and internal systems are exposed. The webhook secret leaks from a developer's notes, forged payment notices are accepted, and permits are issued without payment. The public website certificate expires during a holiday weekend, citizens cannot renew permits and the call centre is overwhelmed. Writing scenarios this way keeps them concrete enough to discuss and estimate.

### 13.2 Estimating risk

For each scenario Rosa estimates likelihood and impact on a three-level scale, with written reasons. The certificate expiry scenario is likely, given past incidents, with moderate impact. The webhook leak is possible with moderate financial impact. The stolen laptop scenario is possible with high impact because VPN access reaches many systems. She resists precise numbers she cannot justify, but she records evidence for each estimate, such as two expiry incidents last year, so others can challenge them. Where colleagues disagree with an estimate, she records both views rather than forcing consensus, and revisits the question once more data arrives.

### 13.3 Treatments and owners

Rosa proposes treatments. Certificate expiry: automate renewal and add alerts. Webhook leak: store secrets in the secret store, rotate them twice a year and verify timestamps to limit replay. Stolen laptop: require the person's password and one-time code in addition to the device certificate, and revoke certificates promptly. Each treatment gets an owner and a date. Owen presents the scenarios to the council's risk committee, which accepts the treatments and asks for quarterly progress reports. Rosa schedules the first progress report before the meeting ends, so the committee's acceptance turns into dated commitments rather than goodwill.

### Worked example

Rosa writes three cause-event-consequence scenarios, estimates them with evidence and assigns treatments, which the risk committee accepts.

> **Synthetic case.** Scenarios and estimates are invented.

### Errors and limits

Scenario lists are never complete; revisit after incidents. Three-level scales hide nuance, so record reasons.

### Exercises

- **EX037 — Scenario form.** What three parts does each scenario have? *Rubric:* 3 = cause, event, consequence;; 2 = two;; 1 = one;; 0 = none.
- **EX038 — Expiry estimate.** How was the expiry scenario rated, and on what evidence? *Rubric:* 3 = likely, moderate impact; two expiry incidents last year;; 2 = rating;; 1 = evidence;; 0 = none.
- **EX039 — Webhook treatment.** What treatments address the webhook leak scenario? *Rubric:* 3 = secret store, twice-yearly rotation, timestamp verification against replay;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

Concrete scenarios with justified estimates and owned treatments make trust-service risks manageable.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Cryptography and trust services: methods I

### Learning outcomes

You will (1) verify signed webhooks with HMAC; (2) limit replay with timestamps; (3) combine checks correctly in code.

### 14.1 Signed webhooks

The payment provider notifies the council when a permit is paid by sending an HTTP request containing a JSON body, a timestamp header and a signature header. The signature is an HMAC-SHA256, as in RFC 2104, computed over the timestamp and body with a secret shared between the provider and the council. The council recomputes the HMAC and compares. Rosa learns that the comparison must use a constant-time function, hmac.compare_digest in Python, so attackers cannot learn the correct signature byte by byte from timing.

### Lab — Webhook verification

```python
"""Verify a signed webhook with HMAC-SHA256 plus a 300-second timestamp window (synthetic payment notice)."""
import hmac, hashlib
SECRET = b"demo-webhook-secret-not-for-production"
WINDOW = 300

def sign(ts, body): return hmac.new(SECRET, f"{ts}.".encode() + body, hashlib.sha256).hexdigest()

def verify(ts, body, sig, now):
    return abs(now - ts) <= WINDOW and hmac.compare_digest(sig, sign(ts, body))

def main():
    body, ts = b'{"permit":"PK-2291","paid":45.00}', 1767225600
    sig = sign(ts, body)
    print("fresh, intact:", verify(ts, body, sig, now=ts + 20))
    print("amount edited:", verify(ts, body.replace(b"45.00", b"4.50"), sig, now=ts + 20))
    print("replayed after 1 hour:", verify(ts, body, sig, now=ts + 3600))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_webhook.py`. Verified output:

```text
fresh, intact: True
amount edited: False
replayed after 1 hour: False
```

### 14.2 Reading the webhook run

A fresh, intact notification verifies as True. When the paid amount is edited from 45.00 to 4.50, verification fails because the HMAC no longer matches. When the same valid notification is replayed an hour later, verification fails because the timestamp falls outside the 300-second window. Rosa notes that the window limits replay to five minutes but does not prevent it entirely; the council also records processed notification identifiers and rejects duplicates. The demonstration secret is fixed only for reproducible output; the real secret lives in the secret store.

### 14.3 Combining checks

Rosa writes the verification order: read the raw body exactly as received, before any JSON parsing that might change spacing; check the timestamp window; recompute and compare the HMAC; check the notification identifier has not been processed; and only then act on the content. She also logs failures with reasons for operations, but returns a generic error to the caller. Owen reviews the code and asks her to add tests for each failure path, mirroring the lab cases. Each test sends a crafted request and asserts both the response code and the log line, so silent acceptance cannot slip through.

### Worked example

Rosa verifies webhooks with HMAC and a 300-second window, adds duplicate-identifier checks, and orders the checks so raw bytes are verified before parsing.

> **Synthetic case.** The secret and notification are invented; RFC 2104 is real.

### Errors and limits

Verifying after JSON parsing can fail on harmless formatting changes. A timestamp window alone does not stop all replays.

### Exercises

- **EX040 — Signature input.** What does the provider's HMAC cover? *Rubric:* 3 = the timestamp and the body;; 2 = both;; 1 = body only;; 0 = none.
- **EX041 — Lab outcomes.** What did the lab print for edited and replayed notifications? *Rubric:* 3 = False for edited amount and False for replay after one hour;; 2 = both;; 1 = one;; 0 = none.
- **EX042 — Raw body.** Why verify the raw body before parsing JSON? *Rubric:* 3 = parsing can change bytes such as spacing, breaking verification;; 2 = bytes;; 1 = speed;; 0 = none.

### Synthesis

Webhook security combines HMAC over raw bytes, constant-time comparison, a timestamp window and duplicate detection.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Cryptography and trust services: guided lab

### Learning outcomes

You will (1) set up a test certificate authority in a lab; (2) issue and validate server certificates; (3) observe common validation failures safely.

### 15.1 Lab setup

In a guided lab, Rosa builds an isolated test network with a private certificate authority created with standard open-source tooling, a test web server and a client. The lab uses only test domains and throwaway keys. She creates a root certificate kept offline in the lab, an intermediate for issuing, and a server certificate for test.harbourview.example. She records each command and its purpose in her lab notebook, so the procedure can be repeated and reviewed. The lab network has no route to council systems, so nothing done there can affect real services or real citizens.

### 15.2 Issuing and validating

Rosa configures the test server with its certificate and the intermediate, and installs only the lab root on the client. Connections succeed with TLS 1.3. She then examines the certificate fields against RFC 5280: subject alternative name, key usage, extended key usage for server authentication and validity dates. She learns that browsers rely on subject alternative names rather than the older common name field, and fixes a certificate she initially generated with only a common name. She also checks that key usage permits digital signatures only, so the server certificate cannot be misused to sign other certificates.

### 15.3 Observing failures

Rosa deliberately breaks the setup, one change at a time: removing the intermediate from the server, letting a short-lived certificate expire, requesting a different host name and removing the root from the client. Each produces a distinct error, which she records next to the error-to-cause guide from Chapter 2. Seeing failures in a safe lab makes them recognisable in production. Owen stresses that this lab teaches operation of standard tools; it does not teach building a production authority, which requires careful policy, hardware and audit.

### Worked example

Rosa builds a lab CA with offline root and intermediate, fixes a certificate lacking subject alternative names, and records four induced failures.

> **Synthetic case.** The lab is invented; RFC 5280 is real.

### Errors and limits

Lab authorities lack the controls of production ones. Never install lab roots on production machines.

### Exercises

- **EX043 — Lab hierarchy.** What hierarchy does the lab authority use? *Rubric:* 3 = offline root, issuing intermediate, server certificate;; 2 = three levels;; 1 = one;; 0 = none.
- **EX044 — Name field.** Which certificate field do browsers rely on for host names? *Rubric:* 3 = subject alternative name, not common name;; 2 = SAN;; 1 = CN;; 0 = none.
- **EX045 — Induced failures.** List three failures Rosa induced. *Rubric:* 3 = three of missing intermediate, expired certificate, wrong host name, missing root;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

A safe lab authority makes certificate structure and failures familiar before they appear in production.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Cryptography and trust services: methods II

### Learning outcomes

You will (1) store passwords with memory-hard hashing; (2) verify an implementation call against a published test vector; (3) plan migration from weak password storage.

### 16.1 Memory-hard hashing

The permit portal's citizen accounts need safe password storage. Rosa learns that fast hashes let attackers test billions of guesses per second after stealing a database, while memory-hard functions make each guess costly in memory as well as time, slowing specialised hardware. Argon2id from RFC 9106 is the preferred choice; scrypt from RFC 7914 is an established alternative available in Python's hashlib. Production code uses a vetted password-hashing library with tuned parameters; the lab uses hashlib.scrypt to show the idea.

### Lab — scrypt with a test vector

```python
"""Check hashlib.scrypt against an RFC 7914 test vector, then store a synthetic password."""
import hashlib, hmac
WANT = ("fdbabe1c9d3472007856e7190d01e9fe7c6ad7cbc8237830e77376634b3731622eaf30d92e22a3886ff109279d9830dac727afb94a83ee6d8360cbdfa2cc0640")

def main():
    got = hashlib.scrypt(b"password", salt=b"NaCl", n=1024, r=8, p=16, dklen=64).hex()
    print("RFC 7914 vector matches:", got == WANT)
    salt = bytes.fromhex("5e" * 16)  # fixed demo salt for repeatable output
    stored = hashlib.scrypt(b"Permit-Desk-2026!", salt=salt, n=2**14, r=8, p=1, dklen=32)
    ok = hmac.compare_digest(stored, hashlib.scrypt(b"Permit-Desk-2026!", salt=salt, n=2**14, r=8, p=1, dklen=32))
    print("stored:", stored.hex()[:24], "... verify:", ok)

if __name__ == "__main__":
    main()
```

Run with `python3 lab_scrypt.py`. Verified output:

```text
RFC 7914 vector matches: True
stored: ddb1b7d5e7566125ab501de6 ... verify: True
```

### 16.2 Reading the scrypt run

The lab first checks hashlib.scrypt against a published test vector from RFC 7914 with password "password", salt "NaCl", N 1024, r 8 and p 16; the 64-byte output matches. Matching the vector confirms the function is called with the right parameter meanings. It then stores a synthetic staff password with a salt and N of 2^14, and verification with compare_digest returns True. The fixed salt only makes the output repeatable; real salts are random per user. Rosa records the parameters next to the stored hash so they can be raised later.

### 16.3 Planning migration

The portal currently stores passwords with salted SHA-256, which is too fast. Rosa plans a migration: when a citizen logs in successfully, the portal verifies against the old hash and immediately stores a new memory-hard hash; accounts that never log in are wrapped by hashing the old hash with the new function, so no weak hashes remain at rest. After a set period, unused accounts are asked to reset. The plan avoids forcing millions of password resets at once. She estimates server load for the new hash at peak login times before scheduling the change.

### Worked example

Rosa confirms hashlib.scrypt against RFC 7914, stores a synthetic password and plans migration from salted SHA-256 by rehash-on-login plus wrapping.

> **Synthetic case.** The portal and passwords are invented; RFC 7914 and RFC 9106 are real.

### Errors and limits

Memory-hard parameters must be tuned to server capacity. Wrapping old hashes must be done carefully to avoid lockouts.

### Exercises

- **EX046 — Why memory-hard.** Why are memory-hard functions better for passwords than fast hashes? *Rubric:* 3 = each guess costs memory and time, slowing specialised hardware;; 2 = slower;; 1 = same;; 0 = none.
- **EX047 — Vector purpose.** What does matching the RFC 7914 vector confirm? *Rubric:* 3 = the function is called with correct parameter meanings;; 2 = correct use;; 1 = security;; 0 = none.
- **EX048 — Migration method.** How are accounts that never log in protected during migration? *Rubric:* 3 = old hash wrapped with the new memory-hard function;; 2 = wrapping;; 1 = ignored;; 0 = none.

### Synthesis

Memory-hard hashing, verified against test vectors and introduced through careful migration, protects citizen passwords.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography and trust services: tooling

### Learning outcomes

You will (1) choose tools for certificate discovery, renewal and secret storage; (2) evaluate tools against requirements; (3) document tool usage safely.

### 17.1 Tool categories

Rosa surveys tools the council uses or could use: scanners that discover certificates on authorised hosts; ACME clients that renew certificates automatically under RFC 8555; a secret store that holds webhook secrets and API tokens with access control; the key service for encryption keys; and monitoring that tracks expiry and failures. She notes that tools should be mature, maintained and widely used, and that the council should prefer configuring proven tools over writing its own replacements. For each category she notes which team owns it today, revealing that nobody owned discovery scanning until she raised it.

### 17.2 Evaluating tools

Rosa evaluates two ACME clients against requirements: support for the council's web servers, renewal hooks to reload services, clear logs, alerting on failure and active maintenance with security updates. She tests each in the lab from Chapter 15, forcing renewals and failures. One client renews reliably but logs failures only locally, so she adds a hook that sends failures to monitoring. She writes a short evaluation report recommending the other client, which already integrates with the council's monitoring. Her report states the tests performed and their results, so the decision can be checked rather than taken on trust.

### 17.3 Documenting usage

For each tool Rosa writes a usage page: purpose, owner, installation, configuration, common tasks, failure modes and where its secrets are stored. She avoids including any secret values or full configuration files containing keys. Pages link to the inventory entries they affect. When a new team member renews a certificate manually during an outage, the page lets them do it correctly in minutes. Documentation is part of the tool, since a tool nobody knows how to run safely is a risk.

### Worked example

Rosa surveys tooling, evaluates two ACME clients in the lab, recommends the one integrated with monitoring and writes secret-free usage pages.

> **Synthetic case.** Tools are described generically; RFC 8555 is real.

### Errors and limits

Tools that log failures only locally create silent failures. Documentation that includes secrets becomes a leak.

### Exercises

- **EX049 — Tool preference.** What principle guides tool choice? *Rubric:* 3 = configure mature maintained tools rather than writing replacements;; 2 = mature;; 1 = custom;; 0 = none.
- **EX050 — ACME requirement.** Name three requirements Rosa used to evaluate ACME clients. *Rubric:* 3 = three of server support, reload hooks, clear logs, failure alerting, active maintenance;; 2 = two;; 1 = one;; 0 = none.
- **EX051 — Usage page.** What must a usage page never include? *Rubric:* 3 = secret values or configs containing keys;; 2 = secrets;; 1 = owner;; 0 = none.

### Synthesis

Mature tools, evaluated against requirements and documented without secrets, make trust operations reliable.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Cryptography and trust services: controls

### Learning outcomes

You will (1) define controls for the document-signing key; (2) apply least privilege and dual control; (3) collect evidence that controls operate.

### 18.1 Protecting the signing key

The document-signing key is critical, so Rosa helps design its controls. The key is generated inside a hardware security module and marked non-exportable. Signing requests come from the document workflow system, which submits a document digest, not the document itself, and only after a council officer approves the decision in the workflow. The HSM logs each signing operation. Signatures use a standard algorithm from FIPS 186-5 through the HSM's vetted interface, never through custom code. Backups of the HSM's encrypted key material follow the vendor's documented procedure and are tested by restoring into a spare module once a year.

### 18.2 Least privilege and dual control

Only the workflow service account can request signatures, and only for approved documents. Administrators can manage the HSM but cannot sign. Changing the signing configuration, such as replacing the key, requires two administrators and a change ticket approved by the records manager. Rosa explains to colleagues that these rules protect them too: no single person could be accused of forging a decision because no single person could do it. Rosa documents these roles in a short matrix listing each account, what it may do and who approves changes to it. Auditors later use the matrix as their starting point when sampling permissions.

### 18.3 Evidence

Rosa defines evidence for each control: HSM logs showing signatures match approved workflow items; quarterly access reviews of who can administer the HSM; change tickets with two approvers for key changes; and a yearly test that an unapproved document cannot be signed. She builds a small report that compares HSM signing logs with workflow approvals and flags mismatches. The first run finds none, which is itself useful evidence for auditors. She schedules the yearly negative test with the records manager present, since a witness strengthens the evidence. Each piece of evidence is filed with its date and reviewer, so missing reviews become visible rather than silently skipped.

### Worked example

Rosa designs HSM-based, workflow-gated signing with least privilege and dual control, and builds a report comparing signing logs with approvals.

> **Synthetic case.** The controls are invented; FIPS 186-5 is real.

### Errors and limits

HSMs protect keys, not the decisions behind signing requests; workflow controls matter. Evidence must be reviewed, not just collected.

### Exercises

- **EX052 — Signing input.** What does the workflow submit to the HSM? *Rubric:* 3 = a document digest after officer approval;; 2 = digest;; 1 = whole document;; 0 = none.
- **EX053 — Admin limits.** What can HSM administrators not do? *Rubric:* 3 = sign documents;; 2 = sign;; 1 = manage;; 0 = none.
- **EX054 — Mismatch report.** What does Rosa's report compare? *Rubric:* 3 = HSM signing logs against workflow approvals;; 2 = both;; 1 = one;; 0 = none.

### Synthesis

Critical keys need hardware protection, workflow gating, least privilege, dual control and evidence that controls work.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Cryptography and trust services: monitoring

### Learning outcomes

You will (1) choose metrics for TLS and certificate health; (2) set alert thresholds that avoid noise; (3) respond to alerts with runbooks.

### 19.1 What to monitor

Rosa sets up monitoring for trust services: days until each certificate expires, ACME renewal successes and failures, TLS handshake failure rates on the gateway, webhook verification failures and HSM availability. Each metric has an owner and a runbook. She focuses on signals that predict problems, such as renewal failures, rather than only measuring outages after they happen. Monitoring is how the council learns of a problem before citizens do. Before setting thresholds she records two weeks of baseline values, so alerts reflect what is unusual for the council rather than numbers copied from elsewhere. She sends alerts to the on-call rota, never to personal inboxes that go unread on leave.

### Lab — Failure-rate alert

```python
"""Flag hours where TLS failure rate exceeds 2% for three consecutive hours (synthetic gateway counts)."""
HOURS = [(1200, 6), (1350, 9), (1500, 41), (1480, 44), (1420, 39), (1300, 12), (1250, 7)]  # (handshakes, failures)

def main():
    rates = [f / h for h, f in HOURS]
    for i, r in enumerate(rates):
        print(f"hour {i}: {100 * r:.2f}%")
    run = 0
    for i, r in enumerate(rates):
        run = run + 1 if r > 0.02 else 0
        if run == 3:
            print(f"ALERT at hour {i} (3 consecutive hours above 2%)")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_monitor.py`. Verified output:

```text
hour 0: 0.50%
hour 1: 0.67%
hour 2: 2.73%
hour 3: 2.97%
hour 4: 2.75%
hour 5: 0.92%
hour 6: 0.56%
ALERT at hour 4 (3 consecutive hours above 2%)
```

### 19.2 Reading the alert

The lab computes hourly TLS failure rates at the gateway. Normal hours sit below one percent. Hours 2, 3 and 4 rise to 2.73, 2.97 and 2.75 percent, and the rule, more than two percent for three consecutive hours, fires at hour 4. Requiring three hours avoids alerting on a brief spike. Rosa notes the trade-off: a citizen-facing certificate expiry would justify a faster alert, so expiry gets its own direct check thirty and seven days ahead rather than waiting for failures to rise. She also checks that the alert clears once rates return below the threshold, so stale alerts do not pile up.

### 19.3 Responding to alerts

Each alert links to a runbook. For a failure-rate alert, the runbook says to check the gateway log summary from Chapter 9, identify the dominant reason code and host, check recent changes and escalate if a certificate or configuration is wrong. Rosa practises the runbook on the synthetic spike and finds the cause in the scenario's change log: a configuration push removed a cipher suite needed by an older payment terminal. She also records alert volumes monthly and tunes thresholds that never lead to action.

### Worked example

Rosa's monitoring fires a failure-rate alert at hour 4 after three hours above two percent, and her runbook traces it to a configuration push.

> **Synthetic case.** Counts and causes are invented.

### Errors and limits

Thresholds without baselines create noise or miss problems. Monitoring failures, not just outages, catches silent issues.

### Exercises

- **EX055 — Monitored signals.** List four signals Rosa monitors. *Rubric:* 3 = four of expiry days, renewal results, handshake failure rate, webhook failures, HSM availability;; 2 = three;; 1 = one;; 0 = none.
- **EX056 — Alert hour.** When did the lab alert fire and why? *Rubric:* 3 = hour 4, after three consecutive hours above two percent;; 2 = hour;; 1 = wrong;; 0 = none.
- **EX057 — Spike cause.** What caused the synthetic spike? *Rubric:* 3 = configuration push removed a cipher suite needed by an older payment terminal;; 2 = cause;; 1 = vague;; 0 = none.

### Synthesis

Monitoring predictive signals with tuned thresholds and runbooks lets operators fix trust problems before citizens notice.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Cryptography and trust services: troubleshooting

### Learning outcomes

You will (1) troubleshoot certificate and TLS problems systematically; (2) use evidence rather than guesses; (3) fix root causes, not just symptoms.

### 20.1 A method

Rosa adopts a troubleshooting method: define the symptom precisely, collect evidence, form one hypothesis at a time, test it, fix and verify, then record. For a ticket saying "staff can't reach the wiki", she first asks which staff, which devices and what error. The error is "unknown certificate authority" on new laptops only. Evidence narrows the problem quickly: the new laptop image lacks the council's internal root certificate. Guessing, such as restarting the wiki server, would have wasted time. She tests one change at a time, so each result can be attributed to a single cause.

### 20.2 Common root causes

Rosa compiles root causes from past tickets: missing intermediates on servers; internal roots missing from new images; clocks wrong on devices, making valid certificates appear not yet valid; old clients lacking TLS 1.2 support; certificates missing a host name; and expired certificates renewed but not reloaded by the web server. The last one is subtle: the new certificate sits on disk, but the server still uses the old one in memory until reload. She adds reload verification to the renewal runbook.

### 20.3 Fixing root causes

For the wiki ticket, Rosa installs the internal root through device management for affected laptops, but also fixes the laptop image so future devices include it, and adds a test to the image build. For the reload issue, she configures renewal hooks to reload services and checks the served certificate's expiry after renewal. Fixing root causes prevents repeats and frees time. She records each case in a knowledge base with symptom, evidence, cause and fix. Each knowledge base entry is tagged with the affected service, so the next person searching finds it quickly.

### Worked example

Rosa traces an unknown-CA error to a laptop image missing the internal root, fixes the image and adds post-renewal reload checks to prevent stale certificates in memory.

> **Synthetic case.** Tickets are invented.

### Errors and limits

Fixing symptoms leaves the cause to return. Multiple simultaneous changes make results impossible to interpret.

### Exercises

- **EX058 — Wiki diagnosis.** What evidence revealed the wiki problem's cause? *Rubric:* 3 = unknown CA error on new laptops only; image lacked internal root;; 2 = evidence;; 1 = guess;; 0 = none.
- **EX059 — Reload issue.** Why can a renewed certificate still appear expired? *Rubric:* 3 = server keeps old certificate in memory until reloaded;; 2 = reload;; 1 = not renewed;; 0 = none.
- **EX060 — Root-cause fix.** What root-cause fix did Rosa apply for the wiki? *Rubric:* 3 = fixed laptop image and added image build test, besides installing root on affected devices;; 2 = image;; 1 = device only;; 0 = none.

### Synthesis

Systematic, evidence-led troubleshooting finds root causes such as missing roots and unreloaded certificates and prevents repeats.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Cryptography and trust services: service integration

### Learning outcomes

You will (1) integrate a new service with council trust services; (2) define an onboarding checklist; (3) verify integration before go-live.

### 21.1 A new service arrives

The council buys a hosted booking system for community halls. It must use council single sign-on, present a valid certificate on a council subdomain, receive payment webhooks and store citizens' contact details. Rosa is asked to integrate it with the council's trust services. She starts by listing what the service needs from the council, such as a certificate and a webhook secret, and what the council needs from the supplier, such as TLS 1.2 or later, encryption at rest and a named security contact.

### 21.2 Onboarding checklist

Rosa turns her work into a reusable checklist: inventory entry with owner; certificate issued through ACME with monitoring; TLS configuration checked against the council baseline; webhook secret created in the secret store and shared with the supplier through a secure channel, never email; single sign-on configured with signed assertions validated by the supplier; data-at-rest encryption confirmed in the contract; and a rollback plan. Each item has a person who confirms it. The checklist means the next service onboards faster and more consistently.

### 21.3 Verifying before go-live

Before launch Rosa verifies each item with evidence rather than the supplier's word: she connects and records the TLS version and certificate chain, sends a test webhook with a deliberately wrong signature to confirm it is rejected, checks expiry monitoring shows the new certificate, and confirms sign-on fails when assertions are tampered with in the supplier's test environment. One check fails: the supplier accepted the wrong webhook signature. Go-live waits until the supplier fixes verification and Rosa retests successfully. She records the retest output in the change record before approving launch.

### Worked example

Rosa integrates a hall-booking service using a checklist and blocks go-live when a negative webhook test shows the supplier accepted a bad signature.

> **Synthetic case.** The service and supplier are invented.

### Errors and limits

Checklists can become box-ticking; require evidence. Supplier test environments may differ from production.

### Exercises

- **EX061 — Secret sharing.** How must the webhook secret be shared with the supplier? *Rubric:* 3 = through a secure channel from the secret store, never email;; 2 = secure;; 1 = email;; 0 = none.
- **EX062 — Failed check.** Which go-live check failed? *Rubric:* 3 = supplier accepted a webhook with a wrong signature;; 2 = webhook;; 1 = vague;; 0 = none.
- **EX063 — Evidence.** Why test with negative cases rather than trusting supplier statements? *Rubric:* 3 = statements can be wrong; negative tests prove rejection actually happens;; 2 = proof;; 1 = trust;; 0 = none.

### Synthesis

Integrating a service means a checklist of trust requirements, each verified by evidence including negative tests, before go-live.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Cryptography and trust services: automation

### Learning outcomes

You will (1) automate renewal planning from inventory data; (2) separate automatic and manual paths; (3) keep humans in control of exceptions.

### 22.1 Why automate

Manual renewal caused the council's past outages. Rosa writes a planner that reads the inventory and decides, for each certificate, whether to renew now, skip or escalate. Automation repeats the same correct decision every day, which people forget to do during holidays. Still, automation must be observable and must hand exceptions to people, because some certificates cannot be renewed automatically and some decisions need judgement. Rosa writes down what the planner must never do, such as deleting certificates or changing keys, and makes those actions impossible in its code. She also stores each day's plan, so anyone can later see what was decided and why. The inventory becomes the single source the planner trusts, which gives teams a reason to keep it accurate.

### Lab — Renewal planner

```python
"""Dry-run renewal planner: which certificates an automation job would renew (renew at <= 30 days)."""
from datetime import date
TODAY = date(2026, 5, 1)
CERTS = [("permits", date(2026, 5, 20), "acme"), ("council-docs", date(2026, 9, 2), "acme"),
         ("staff-vpn", date(2026, 5, 9), "internal-ca"), ("legacy-gis", date(2026, 4, 28), "manual")]

def main():
    for name, exp, how in CERTS:
        left = (exp - TODAY).days
        act = "RENEW" if left <= 30 and how != "manual" else ("ESCALATE (manual)" if left <= 30 else "skip")
        print(f"{name:<13} {left:>4} d {how:<12} {act}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_renewplan.py`. Verified output:

```text
permits         19 d acme         RENEW
council-docs   124 d acme         skip
staff-vpn        8 d internal-ca  RENEW
legacy-gis      -3 d manual       ESCALATE (manual)
```

### 22.2 Reading the planner

The planner renews certificates within thirty days of expiry. The permit site at 19 days is renewed automatically. Council-docs at 124 days is skipped. Staff-vpn at 8 days is renewed. Legacy-gis has already expired, at minus three days, and is managed manually because its old appliance cannot run an ACME client, so the planner escalates it to a person rather than attempting anything. Rosa likes that the planner's output is a readable plan, which can be reviewed before actions run. She adds a summary line counting each decision type for quick daily review.

### 22.3 Humans and exceptions

Rosa adds safeguards: the planner runs in a dry-run mode first and posts its plan to the operations channel; actual renewals run only through the vetted ACME client; any escalation creates a ticket with the owner; and failures alert monitoring. The legacy-gis appliance gets a replacement project, since an expired certificate on an unsupported device is a recurring risk. Owen notes that the best automation removes routine work so people can focus on the exceptions it reports. She reviews the dry-run plans for two weeks before allowing real renewals, comparing them with what she would have decided by hand.

### Worked example

Rosa's planner renews two certificates, skips one and escalates an expired manual one, running dry first and opening tickets for exceptions.

> **Synthetic case.** Inventory values are invented.

### Errors and limits

Automation that fails silently is worse than manual work. Thresholds must suit certificate lifetimes.

### Exercises

- **EX064 — Planner outcome.** What did the planner decide for legacy-gis and why? *Rubric:* 3 = escalate; expired at -3 days and managed manually;; 2 = escalate;; 1 = renew;; 0 = none.
- **EX065 — Threshold.** What threshold triggers automatic renewal? *Rubric:* 3 = within thirty days of expiry;; 2 = 30;; 1 = vague;; 0 = none.
- **EX066 — Safeguards.** Name two safeguards around the planner. *Rubric:* 3 = two of dry run posted, vetted ACME client, tickets for escalations, failure alerts;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Automation should make routine renewals reliable, stay observable and hand exceptions to accountable people.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Cryptography and trust services: evaluation

### Learning outcomes

You will (1) evaluate whether trust-service changes worked; (2) choose before-and-after measures; (3) report results honestly.

### 23.1 Did it work

After six months of changes, Owen asks Rosa to evaluate them. She returns to the goals set in the risk scenarios: fewer certificate outages, no weak TLS on public services, safer password storage and verified webhooks. Evaluation compares outcomes with those goals rather than listing completed tasks. Finishing a migration is an activity; reducing outages is an outcome. Rosa writes this distinction at the top of her report so readers know what she measured. She also lists the original goals verbatim, so nobody can quietly redefine success after the fact.

### 23.2 Measures

Rosa picks measures available before and after: certificate-related outage hours fell from nine in the previous half-year to zero; public endpoints offering TLS 1.0 fell from three to zero; the share of citizen accounts with memory-hard hashes rose to 71 percent through rehash-on-login and wrapping; and webhook verification failures are now logged and reviewed. She notes confounders: a quieter period for changes may have helped outage numbers, and six months is short for rare events. Each figure links to the query that produced it, so the committee can rerun it next half-year.

### 23.3 Honest reporting

Rosa reports what improved, what did not and what is unknown. The legacy-gis appliance remains a gap; one supplier still needs a retest; and outage figures need another year to be convincing. She includes the data sources and how numbers were computed so others can check them. Owen tells her that honest limitations make the report more credible to the risk committee, which has seen too many reports claiming complete success. She closes with three recommendations ranked by risk reduction, each with an owner and a proposed date, so the evaluation leads directly to next steps.

### Worked example

Rosa evaluates six months of work, reporting outage hours from nine to zero and TLS 1.0 endpoints from three to zero, with confounders and remaining gaps.

> **Synthetic case.** Figures are invented.

### Errors and limits

Before-and-after comparisons can mislead when other factors changed. Activity counts are not outcomes.

### Exercises

- **EX067 — Activity vs outcome.** Give an example of an activity and an outcome from the chapter. *Rubric:* 3 = activity: finishing migration; outcome: fewer outages;; 2 = both;; 1 = one;; 0 = none.
- **EX068 — Outage figures.** How did certificate outage hours change? *Rubric:* 3 = from nine to zero over the half-year;; 2 = numbers;; 1 = vague;; 0 = none.
- **EX069 — Confounder.** Name one confounder Rosa noted. *Rubric:* 3 = quieter change period or short six-month window;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Evaluation compares outcomes with goals, notes confounders and reports gaps honestly.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) frame a small applied research question; (2) collect data ethically from systems you are authorised to use; (3) draw cautious conclusions.

### 24.1 Framing a question

Rosa's programme requires a small applied study. She asks: how long do council certificates take to renew after alerts, and which factors predict delays? The question is answerable with data she can access, useful to the council and narrow enough for one term. Her tutor, Dr Imogen Hale, helps her rewrite vague aims such as "study PKI" into a question with measurable variables: alert-to-renewal time, certificate type, owner team and whether renewal is automated. She also writes down what result would surprise her, which helps her notice if she is only looking for confirmation. Dr Hale asks her to list the data she cannot obtain, so the limits are known from the start.

### 24.2 Ethical data collection

Rosa obtains written permission from Owen to use ticket and monitoring data. She removes staff names, replacing them with team labels, and stores data on council systems only. She collects no citizen data, since it is not needed. Her tutor checks the plan against the polytechnic's research ethics guidance. Rosa learns that even operational data about colleagues deserves care, because results could embarrass individuals if published carelessly. She agrees with Owen that the council may review the report before submission, to catch anything that could identify individuals or reveal sensitive configuration. Raw data is deleted at the end of term, as the plan promised.

### 24.3 Cautious conclusions

Across 41 renewals, automated ones completed within a day after alerts, while manual ones took a median of six days. Rosa concludes that automation is associated with faster renewal, but cautions that teams with automation may also be better resourced, so the study shows association, not proof of cause. She reports how many cases were excluded for missing data and why. Her tutor praises the restraint and suggests a follow-up comparing teams before and after automation. She also publishes her analysis script with synthetic sample data, so others can repeat the method.

### Worked example

Rosa studies 41 renewals, finds automated renewals finish within a day versus a six-day manual median, and reports association rather than cause.

> **Synthetic case.** The study and figures are invented.

### Errors and limits

Small samples give unstable results. Observational data cannot prove cause without careful design.

### Exercises

- **EX070 — Research question.** What was Rosa's research question? *Rubric:* 3 = how long renewals take after alerts and which factors predict delay;; 2 = question;; 1 = topic only;; 0 = none.
- **EX071 — Ethics step.** Name two ethical steps Rosa took. *Rubric:* 3 = two of written permission, staff names replaced, data kept on council systems, no citizen data, ethics check;; 2 = one;; 1 = vague;; 0 = none.
- **EX072 — Conclusion limit.** Why can't Rosa claim automation causes faster renewal? *Rubric:* 3 = automated teams may also be better resourced; association only;; 2 = confounder;; 1 = can claim;; 0 = none.

### Synthesis

Applied research needs a narrow question, ethical data handling and conclusions limited by design.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) plan a team project on trust services; (2) divide roles and track work; (3) review each other's work for security.

### 25.1 The project

Rosa's studio team of four is assigned to build an internal dashboard showing certificate health for the council, using inventory and monitoring data. The team agrees on scope: read-only views of expiry, renewal status and TLS findings; no ability to change systems. Restricting scope reduces risk, since a dashboard that could trigger actions would need far stronger controls. They write a one-page project charter with goals, scope, roles and a schedule of four two-week iterations. The charter also lists what is out of scope, so requests for new features can be declined politely by pointing to it.

### 25.2 Roles and tracking

Roles rotate: one person leads data integration, one the interface, one testing and one documentation and security review. They track tasks on a shared board and hold short weekly check-ins. When one teammate falls behind due to exams, the team reassigns tasks openly rather than letting work silently slip. Rosa finds that writing down decisions, such as which data sources are trusted, avoids repeated debates later. Each iteration ends with a short demo to Owen, whose comments shape the next plan. When disagreements arise, the team records options and the reason for the choice in a decision log, which later helps new members understand why the dashboard works as it does.

### 25.3 Security review

Each change gets a review by another teammate using a checklist: authentication required, data sources read with least privilege, no secrets in code, dependencies pinned and output that does not leak internal hostnames publicly. Reviewers find a hard-coded API token in an early commit; the team rotates the token and rewrites the history in the private repository, then adds a secret scanner. They learn that rotating the exposed secret matters more than hiding it. The scanner now runs on every push, and the team adds a short note to their charter about handling any future leak.

### Worked example

Rosa's team builds a read-only certificate dashboard over four iterations and, after finding a hard-coded token, rotates it and adds secret scanning.

> **Synthetic case.** The team and project are invented.

### Errors and limits

Removing a leaked secret from history does not make it safe; rotate it. Rotating roles needs handover notes.

### Exercises

- **EX073 — Scope choice.** Why was the dashboard kept read-only? *Rubric:* 3 = actions would require far stronger controls; reduces risk;; 2 = risk;; 1 = easier;; 0 = none.
- **EX074 — Token finding.** What did the team do after finding a hard-coded token? *Rubric:* 3 = rotated it, cleaned history, added secret scanner;; 2 = rotate;; 1 = delete only;; 0 = none.
- **EX075 — Lesson.** What matters most after a secret leaks? *Rubric:* 3 = rotating the secret;; 2 = rotate;; 1 = hide;; 0 = none.

### Synthesis

Team projects succeed with limited scope, open tracking and peer security reviews that act on findings.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Cryptography and trust services: operational handoff

### Learning outcomes

You will (1) prepare a service for handoff to operations; (2) write runbooks and ownership records; (3) run a handoff rehearsal.

### 26.1 What handoff means

When Rosa's placement project, automated renewal and the planner, is ready, it must pass to the council's operations team, who will run it after she leaves. Handoff means operations can run, monitor, troubleshoot and change the service without her. Owen reminds her that many council systems became fragile because their builders left without handing over knowledge, leaving undocumented scripts nobody dared touch. Rosa lists everything she does by habit, which reveals tasks she had never written down, such as checking the planner's disk space weekly. She also lists open problems honestly, so operations do not inherit hidden surprises. The handoff plan sets a date after which she answers questions only by improving documentation.

### 26.2 Runbooks and ownership

Rosa writes runbooks for routine tasks and failures: reading the daily plan, handling an escalation, renewing manually when ACME fails, restoring the planner after a server rebuild and rotating the ACME account key. Each runbook lists prerequisites, steps, verification and rollback. She updates the inventory to name the operations team as owner and records where credentials live in the secret store, without including the credentials themselves. Runbooks live in the operations wiki beside the inventory, with a review date and named maintainer, so they do not quietly go stale once Rosa leaves the council.

### 26.3 Rehearsal

Rosa runs a rehearsal: an operations colleague, with no help from her, handles a simulated failed renewal using only the runbook. The colleague gets stuck because the runbook assumes knowledge of where logs are stored. Rosa adds the missing step and repeats the rehearsal with another colleague, who succeeds. Handoff is signed off by the operations lead. Rosa learns that runbooks are only proven when someone else uses them. After sign-off, Rosa schedules a check-in one month later to collect questions, which become further runbook improvements. The operations lead adds the rehearsal to their yearly exercise calendar.

### Worked example

Rosa hands off renewal automation with runbooks, ownership records and a rehearsal that exposes a missing log-location step.

> **Synthetic case.** The handoff is invented.

### Errors and limits

Runbooks written by experts often skip steps they find obvious. Credentials must transfer through the secret store, not documents.

### Exercises

- **EX076 — Handoff meaning.** What does handoff mean in this chapter? *Rubric:* 3 = operations can run, monitor, troubleshoot and change without the builder;; 2 = full;; 1 = partial;; 0 = none.
- **EX077 — Rehearsal finding.** What did the first rehearsal reveal? *Rubric:* 3 = runbook assumed knowledge of log location;; 2 = gap;; 1 = vague;; 0 = none.
- **EX078 — Credentials.** How are credentials handed over? *Rubric:* 3 = via the secret store with location recorded, never in documents;; 2 = store;; 1 = docs;; 0 = none.

### Synthesis

A handoff is complete when others, using only runbooks and records, can operate the service.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) plan a safe deployment of TLS configuration changes; (2) validate changes against requirements; (3) roll back when validation fails.

### 27.1 Planning deployment

The council plans to remove TLS 1.0 and 1.1 from all public endpoints and enable TLS 1.3 where missing, following NIST SP 800-52 Rev. 2. Rosa plans a staged deployment: first the test environment, then a low-traffic endpoint, then the rest in batches. Each stage has a validation step and a rollback trigger. She also notifies partners whose old systems might break, including the parking terminals identified earlier through monitoring. Each batch is scheduled outside peak permit hours, and the service desk receives a short note explaining what citizens might report. She writes rollback commands into the plan in advance, tested in the lab.

### 27.2 Validation

For each endpoint Rosa validates by connecting with clients that offer only old versions to confirm rejection, and with modern clients to confirm TLS 1.2 and 1.3 work. She checks the certificate chain and that the monitoring failure rate stays near baseline for a day. Validation is written as a checklist with expected results, so results are compared, not interpreted loosely. She saves outputs as evidence for the change record. Any unexpected result stops the batch until it is explained, even if users have not complained. Results are attached to the change ticket for auditors.

### 27.3 Rollback

On the third batch, the failure rate on one endpoint rises above two percent within an hour. Logs show an older payment kiosk using TLS 1.0. Rosa rolls back that endpoint as planned, notifies the kiosk supplier and sets a deadline for their upgrade, with the risk accepted temporarily by the service owner. The other endpoints stay changed. She records that rollback worked within ten minutes, which is itself evidence that the plan was sound. The kiosk supplier's deadline is tracked in the risk register, with automatic reminders to the service owner.

### Worked example

Rosa deploys TLS changes in stages, validates with old and new clients, and rolls back one endpoint when a TLS 1.0 kiosk fails.

> **Synthetic case.** The deployment is invented; SP 800-52 Rev. 2 is real.

### Errors and limits

Big-bang changes make failures hard to isolate. Temporary risk acceptance needs a deadline.

### Exercises

- **EX079 — Staging.** What stages did the deployment use? *Rubric:* 3 = test, low-traffic endpoint, then batches;; 2 = three;; 1 = one;; 0 = none.
- **EX080 — Validation test.** How did Rosa confirm old versions were rejected? *Rubric:* 3 = connecting with clients offering only old versions;; 2 = test;; 1 = assume;; 0 = none.
- **EX081 — Rollback cause.** Why was one endpoint rolled back? *Rubric:* 3 = failure rate above two percent from an older TLS 1.0 payment kiosk;; 2 = cause;; 1 = vague;; 0 = none.

### Synthesis

Staged deployment with written validation and rehearsed rollback lets trust improvements proceed safely.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) apply skills during a supervised placement; (2) keep a professional log; (3) reflect on feedback.

### 28.1 Placement work

In her final year Rosa spends a supervised placement at Harbourview City Council. Her tasks include handling certificate tickets, reviewing TLS findings and supporting a supplier's integration. Owen assigns work with increasing responsibility, but she never holds administrator rights to the HSM or the internal CA, which remain with permanent staff. Rosa learns that professional practice includes knowing which actions belong to her role and asking before stepping outside it. She checks with Owen before any task that touches production during business hours, and records his decision. Her placement agreement lists permitted systems, which she rereads when unsure.

### 28.2 Professional log

Rosa keeps a daily log: tasks, decisions, evidence and questions. When a ticket asks her to "just disable certificate checking" for a broken integration, she logs the request, explains why disabling verification would expose the connection to interception and proposes installing the correct intermediate instead. The log becomes evidence for her placement assessment and a record if decisions are later questioned. It contains no secrets or citizen personal data. When she is uncertain, she writes the question in the log and raises it at the next daily check-in. Owen reviews the log weekly, initialling entries that involved production changes.

### 28.3 Reflecting on feedback

At mid-placement review, Owen praises Rosa's troubleshooting but notes that her change requests are too long for busy approvers. She rewrites them with a three-line summary at the top. Her tutor asks her to reflect on one mistake: she once restarted a service during business hours without telling the service desk. She writes what happened, its effect and what she now does. Reflection turns experience into lasting skill. She now posts a notice to the service desk before any restart, and her later change requests are approved faster. Her tutor notes that reflective writing is graded on honesty and specific changes, not on presenting a flawless placement.

### Worked example

Rosa works under supervision without HSM or CA admin rights, refuses to disable certificate checking and reflects on feedback about change requests and communication.

> **Synthetic case.** The placement is invented.

### Errors and limits

Logs that include sensitive data become liabilities. Feedback without reflection rarely changes practice.

### Exercises

- **EX082 — Role limits.** What rights did Rosa not hold during placement? *Rubric:* 3 = HSM and internal CA administrator rights;; 2 = both;; 1 = one;; 0 = none.
- **EX083 — Disable checking.** How did Rosa respond to a request to disable certificate checking? *Rubric:* 3 = explained interception risk and proposed installing correct intermediate;; 2 = both;; 1 = complied;; 0 = none.
- **EX084 — Feedback change.** What did Rosa change after Owen's feedback? *Rubric:* 3 = added a three-line summary to change requests;; 2 = summary;; 1 = vague;; 0 = none.

### Synthesis

Field practice builds judgement about roles, records and communication, strengthened by honest reflection.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) build a capstone deliverable integrating course skills; (2) apply quality and security checks; (3) document it for others.

### 29.1 Capstone scope

Rosa's capstone is a trust-service health toolkit for small councils: an inventory template, the renewal planner, the log summariser, the monitoring rule and runbooks. All tools use standard libraries or vetted clients and call established cryptographic functions; none implement cryptography. The toolkit ships with synthetic sample data only. Her tutor approves the scope because it integrates inventory, automation, monitoring and handoff, the core themes of the course. She sets a feature freeze two weeks before submission, leaving time for testing and documentation rather than last-minute features.

### 29.2 Quality and security checks

Rosa writes tests for each script with expected outputs from the sample data, mirroring the lab results she recorded earlier. She runs a secret scanner, pins dependencies and asks a classmate to review the code using the team studio checklist. The review finds that the log summariser would crash on unexpected lines; she makes it count and report unparseable lines instead. She also checks that documentation never suggests disabling verification as a fix. Every test runs automatically on each commit, and a failing test blocks merging. She records review comments and her responses in the repository, so assessors can see how feedback shaped the final toolkit.

### 29.3 Documentation

The toolkit's guide explains purpose, installation, configuration, each tool's inputs and outputs, limits and the references used, including RFC 8555, RFC 5280 and NIST SP 800-57. It marks all sample data as synthetic. A section called "What this toolkit does not do" states that it does not replace a certificate authority, an HSM or professional review. Rosa believes that clearly stating limits protects users from relying on the toolkit for more than it can do. The guide includes a quick-start using the sample data, so a reader can see each tool work in under fifteen minutes. It also explains how to report problems and suggest improvements.

### Worked example

Rosa builds a tested, reviewed toolkit of planner, summariser, monitor rule and runbooks, documenting references and stating its limits.

> **Synthetic case.** The toolkit is invented; cited standards are real.

### Errors and limits

Toolkits used outside their intended context can mislead. Tests on synthetic data do not prove behaviour on real data.

### Exercises

- **EX085 — Capstone contents.** List three components of Rosa's toolkit. *Rubric:* 3 = three of inventory template, renewal planner, log summariser, monitoring rule, runbooks;; 2 = two;; 1 = one;; 0 = none.
- **EX086 — Review fix.** What problem did review find and how was it fixed? *Rubric:* 3 = summariser crashed on unexpected lines; now counts and reports them;; 2 = both;; 1 = one;; 0 = none.
- **EX087 — Limits section.** What does the limits section say? *Rubric:* 3 = toolkit does not replace a CA, an HSM or professional review;; 2 = statement;; 1 = vague;; 0 = none.

### Synthesis

A capstone integrates skills into tested, reviewed and honestly documented tools.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) present a capstone to assessors; (2) defend design choices with evidence; (3) plan continued professional development.

### 30.1 Presentation

Rosa presents her toolkit to a panel of her tutor, Owen and an external assessor. She demonstrates the planner on synthetic data, shows the monitoring alert firing at hour 4 and walks through a runbook. She keeps the demonstration short and focused on the problems the toolkit solves: outages from expiry, silent failures and lost knowledge. The panel asks her to show evidence that the toolkit would have prevented a real past incident. To answer, she replays last year's expiry outage data through the planner, which would have flagged the certificate twenty-nine days before it expired.

### 30.2 Defending choices

The external assessor asks why she did not write her own certificate checking code. Rosa answers that standard libraries and clients implement verification carefully and receive security fixes, while custom code would likely miss edge cases from RFC 5280. Asked why the monitoring rule waits three hours, she explains the trade-off between noise and speed and points to the separate expiry checks. She admits that the toolkit was tested only on synthetic data, and proposes a pilot at another council. She thanks the assessor for the question about testing and adds the pilot to her plan.

### 30.3 Continuing development

The panel passes the capstone with a recommendation to publish the toolkit openly after review. Rosa writes a development plan: gain a recognised certificate in security operations, learn more about hardware security modules and signing services, follow post-quantum migration guidance in FIPS 203 and 204, and keep contributing to council operations. She reflects that the course taught her to keep cryptographic systems healthy using vetted tools, evidence and clear communication. She schedules quarterly reviews of the plan with Owen, who agrees to mentor her for her first year in a permanent role. The plan lists resources and dates, not just intentions.

### Worked example

Rosa presents her toolkit, defends using vetted libraries and the three-hour rule, admits synthetic-only testing and plans further study.

> **Synthetic case.** The assessment is invented; standards cited are real.

### Errors and limits

Demos can hide weaknesses; assessors should ask for evidence. Development plans need concrete steps.

### Exercises

- **EX088 — Panel request.** What evidence did the panel request? *Rubric:* 3 = that the toolkit would have prevented a real past incident;; 2 = incident;; 1 = vague;; 0 = none.
- **EX089 — Own code.** Why did Rosa avoid writing her own certificate checking? *Rubric:* 3 = vetted libraries handle RFC 5280 edge cases and get security fixes;; 2 = reason;; 1 = vague;; 0 = none.
- **EX090 — Development plan.** Name two items in Rosa's development plan. *Rubric:* 3 = two of security operations certificate, HSM and signing study, post-quantum guidance, continued council work;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Capstone assessment tests whether a learner can explain, defend and limit their work with evidence.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Rosa Delgado, Owen Pryce, Dr Imogen Hale, Pinecrest Polytechnic, Harbourview City Council and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** At the council's IT department, focusing on building and running integrated services reliably and securely.

**EX002.** The provider holds them, so the council must rely on contracts and the provider's own controls.

**EX003.** TLS to the portal, a password hash check, a signed payment notification and an encrypted database.

**EX004.** Because the impostor server cannot show a trusted certificate for the council's name, so the browser rejects it.

**EX005.** Wording explaining that the connection is private, without claiming the site or data are safe.

**EX006.** The server omits the intermediate certificate, so clients cannot build a path to a trusted root.

**EX007.** Rows with blank or malformed dates from older exports, so the script does not crash.

**EX008.** An integration sent Base64-encoded permit data over unencrypted HTTP; it was moved to HTTPS.

**EX009.** Into an environment variable filled from the secret store, because source code gets shared and committed.

**EX010.** Host name, issuer, expiry date and owner.

**EX011.** They stop incomplete records at entry time, before missing data causes an outage.

**EX012.** The inventory is widely read, exported and backed up, so secrets would be exposed; they belong in a secret store.

**EX013.** A signed council decision that must not change after approval.

**EX014.** HMAC, because the provider and council share a secret and need to authenticate messages.

**EX015.** Passwords should be stored as one-way hashes so nobody can recover them; forgotten passwords are reset, not emailed.

**EX016.** A TLS private key readable by all accounts on a server.

**EX017.** It shipped a pre-generated SSH host key, so every new machine had the same key.

**EX018.** Because it waits until the kernel generator is properly seeded before returning random bytes.

**EX019.** The certificate proves the device is council-managed; the password and code prove the person is authorised.

**EX020.** So that losing one key does not lock the administrator out.

**EX021.** Leavers' device certificates sometimes stayed valid for weeks.

**EX022.** The gateway forwarded traffic to application servers over unencrypted HTTP.

**EX023.** HMAC signatures on notifications from the payment provider.

**EX024.** It runs on one machine with no key backup, and the same account controls it and the gateway.

**EX025.** certificate_expired points to renewal, protocol_version to an outdated client and unknown_ca to a missing trusted root.

**EX026.** The expired permits certificate, since it blocked citizens: three failures from two clients.

**EX027.** That citizens could not renew permits for about twenty minutes due to an expired certificate, fixed at 08:30, with two minor separate issues.

**EX028.** A public CA, an internal CA, document signing, timestamping and payment webhook signatures.

**EX029.** The council trusts the payment provider's webhook key to vouch for payment notices.

**EX030.** Protect the signing key, keep evidence for long-term validation and revoke promptly after compromise.

**EX031.** A certificate for a long-retired events website that was still being renewed.

**EX032.** The document-signing key, since forged decisions could have legal effect, and the internal CA key, which could create any internal identity.

**EX033.** Signatures need trusted timestamps and archived validation data so they can be verified for ten years.

**EX034.** Because a table can be sorted and filtered when prioritising fixes.

**EX035.** The encryption key sat on the same backup server as the data.

**EX036.** The emailed spreadsheet export to the contractor, replaced by secure transfer with per-file encryption to the contractor's public key.

**EX037.** A cause, an event and a consequence.

**EX038.** Likely with moderate impact, based on two expiry incidents in the previous year.

**EX039.** Keep the secret in the secret store, rotate it twice a year and check timestamps to limit replay.

**EX040.** The timestamp together with the request body.

**EX041.** Both returned False: the edited amount failed the HMAC and the replay fell outside the window.

**EX042.** Because parsing and re-serialising can alter bytes such as spacing, so the HMAC would no longer match.

**EX043.** An offline root, an intermediate that issues, and the server certificate.

**EX044.** The subject alternative name extension rather than the common name.

**EX045.** Removing the intermediate, letting a certificate expire and requesting the wrong host name.

**EX046.** They make each guess expensive in both memory and time, which slows attackers' specialised hardware.

**EX047.** That hashlib.scrypt is being called with the right meanings for its parameters.

**EX048.** Their existing hashes are wrapped by hashing them again with the new memory-hard function.

**EX049.** Prefer configuring mature, maintained tools to writing the council's own replacements.

**EX050.** Support for council servers, hooks to reload services and alerting on failures.

**EX051.** Secret values or configuration files that contain keys.

**EX052.** A digest of the approved document, only after an officer approves it.

**EX053.** They cannot create signatures.

**EX054.** It compares HSM signing logs with workflow approvals and flags any mismatch.

**EX055.** Days to certificate expiry, renewal outcomes, handshake failure rates and webhook verification failures.

**EX056.** At hour 4, after three straight hours above two percent.

**EX057.** A configuration change removed a cipher suite that an older payment terminal still needed.

**EX058.** The error was "unknown certificate authority" only on new laptops, whose image lacked the internal root.

**EX059.** Because the web server keeps using the old certificate in memory until it is reloaded.

**EX060.** She corrected the laptop image and added a build test, in addition to fixing the affected laptops.

**EX061.** Through a secure channel from the secret store, never by email.

**EX062.** The supplier's system accepted a test webhook with a deliberately wrong signature.

**EX063.** Because only a deliberately bad input shows that rejection really happens, whatever the supplier says.

**EX064.** It escalated to a person because the certificate had expired and the appliance needs manual renewal.

**EX065.** Any automatically managed certificate within thirty days of expiry.

**EX066.** A dry-run plan posted for review and tickets with owners for every escalation.

**EX067.** Completing a migration is an activity; reducing certificate outages is an outcome.

**EX068.** They fell from nine hours in the previous half-year to zero.

**EX069.** A quieter period for changes might explain part of the outage reduction.

**EX070.** How long council certificate renewals take after alerts and which factors predict delays.

**EX071.** She obtained written permission and replaced staff names with team labels.

**EX072.** Because teams that automate may also differ in resources, so the data show association, not cause.

**EX073.** Because a dashboard able to change systems would need much stronger controls, so read-only reduced risk.

**EX074.** They rotated the token, cleaned the repository history and added a secret scanner.

**EX075.** Rotating the exposed secret, since copies may already exist.

**EX076.** Operations can run, monitor, troubleshoot and change the service without Rosa.

**EX077.** The runbook assumed the reader knew where logs were stored.

**EX078.** Through the secret store, with only their location recorded in documentation.

**EX079.** The test environment, then a low-traffic endpoint, then batches of the rest.

**EX080.** By connecting with clients that offered only old protocol versions and confirming rejection.

**EX081.** Its failure rate rose above two percent because an old payment kiosk still used TLS 1.0.

**EX082.** Administrator rights to the HSM and the internal certificate authority.

**EX083.** She explained that it would allow interception and proposed fixing the missing intermediate instead.

**EX084.** She added a three-line summary at the top of her change requests.

**EX085.** An inventory template, the renewal planner and the log summariser.

**EX086.** The log summariser crashed on unexpected lines, so it now counts and reports them instead.

**EX087.** That the toolkit does not replace a certificate authority, a hardware security module or professional review.

**EX088.** Evidence that the toolkit would have prevented a real incident from the past.

**EX089.** Because vetted libraries implement verification carefully, handle edge cases and receive security fixes.

**EX090.** Earning a security operations certificate and following post-quantum migration guidance.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, keys and data in this book are synthetic unless a sentence cites a public source.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barker, E., & Kelsey, J. (2015). *Recommendation for random number generation using deterministic random bit generators* (NIST SP 800-90A Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-90Ar1>
- Barker, E., & Roginsky, A. (2019). *Transitioning the use of cryptographic algorithms and key lengths* (NIST SP 800-131A Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-131Ar2>
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
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- Moriarty, K., Kaliski, B., Jonsson, J., & Rusch, A. (2016). *PKCS #1: RSA cryptography specifications version 2.2* (RFC 8017). IETF. <https://www.rfc-editor.org/rfc/rfc8017>
- National Institute of Standards and Technology. (2001, updated 2023). *Advanced Encryption Standard (AES)* (FIPS 197). <https://doi.org/10.6028/NIST.FIPS.197-upd1>
- National Institute of Standards and Technology. (2008). *The keyed-hash message authentication code (HMAC)* (FIPS 198-1). <https://doi.org/10.6028/NIST.FIPS.198-1>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2023). *Digital signature standard (DSS)* (FIPS 186-5). <https://doi.org/10.6028/NIST.FIPS.186-5>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- Nystrom, M. (2005). *Identifiers and test vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512* (RFC 4231). IETF. <https://www.rfc-editor.org/rfc/rfc4231>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Shoup, V. (2004). *Sequences of games: A tool for taming complexity in security proofs* (Cryptology ePrint Archive, Paper 2004/332). <https://eprint.iacr.org/2004/332>
