# Cryptography and Trust Services: Rapid Course

- Language: English (`en`); course 008, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: new learners with no prior security role.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: labs compute SHA-256 fingerprints and call hashlib's scrypt on synthetic data; they implement no cipher. Real systems use vetted libraries and products; never roll your own cryptography. All people, organisations and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. Four chapters follow one new learner helping a small community library: what cryptography protects, permission and safe practice, the library's systems and suppliers, and a guided task checking a download fingerprint. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Leo Fernandes** | New learner and volunteer | Invented |
| **Inês Hartley** | Volunteer IT guide | Invented |
| **Willow Lane Community Library** | Fictional small library | Invented |

### Core sources

[RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280); [RFC 7914](https://www.rfc-editor.org/rfc/rfc7914); [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4); Menezes, van Oorschot and Vanstone, [Handbook of Applied Cryptography](https://cacr.uwaterloo.ca/hac/). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Cryptography and trust services: foundations and decisions

### Learning outcomes

You will (1) explain in plain words what cryptography protects; (2) tell encoding, hashing, encryption and signatures apart; (3) see what a padlock and a certificate do and do not promise; (4) make simple, safe decisions about cryptographic tools.

### 1.1 The case

Leo Fernandes has no security background. He signs up for a one-month introductory course and, as practice, helps the fictional Willow Lane Community Library, a small library with a public website, a members' e-book account system, two staff laptops, a public Wi-Fi network and an email newsletter. His guide is Inês Hartley, the volunteer who looks after the library's IT. Every person, place and number in this book is synthetic. Leo's goal is to understand the core risks well enough to explain them to the library team and to complete one guided task safely. He will use cryptography, never invent it.

### 1.2 What cryptography protects

Inês explains three promises. Confidentiality means only the right people can read something, such as a member's address. Integrity means changes are noticed, such as a website file altered by an intruder. Authenticity means you can tell who sent or published something, such as an email from the library. Cryptography delivers these promises with mathematics and keys, which are secret values. It does not stop someone guessing a weak password, clicking a fake link or leaving a laptop unlocked. Leo writes the three words on a card and asks of every tool which promise it keeps, because each tool keeps different promises.

### 1.3 Four kinds of transformation

Leo meets four things that look like scrambled text. Encoding, such as Base64, just changes how data is written; anyone can reverse it, so it hides nothing. Hashing, such as SHA-256, turns any data into a short fingerprint that cannot be turned back, and a tiny change gives a completely different fingerprint. Encryption, such as AES, hides data so only someone with the key can read it. A digital signature lets anyone check who signed something using a public key. The lab below shows the hash behaviour on synthetic text: one changed letter produces an unrelated fingerprint.

### Lab — One letter changes the fingerprint

```python
# SHA-256 fingerprints of synthetic text (FIPS 180-4 via hashlib).
import hashlib
a = "Willow Lane opening hours: 9-17"
b = "Willow Lane opening hours: 9-18"
ha, hb = hashlib.sha256(a.encode()).hexdigest(), hashlib.sha256(b.encode()).hexdigest()
print("A:", ha[:32] + "...")
print("B:", hb[:32] + "...")
print("match:", ha == hb)
```

Run with `python3 lab_fingerprint.py`. Verified output:

```text
A: 7a5d91566f93af7abf7fc2c33d868004...
B: c029501271e71ec3fc765840b69dfabd...
match: False
```

### 1.4 The padlock and the certificate

When Leo opens the library website, the browser shows a padlock. Inês explains that it means the connection uses TLS, the protocol in RFC 8446, so people on the same Wi-Fi cannot read or change what passes between Leo and the site. The site proves its name with a certificate, defined in RFC 5280, issued by an authority the browser trusts. The padlock does not mean the site is honest, free of bugs or the one Leo meant to visit; a fake site with a similar name can have its own padlock. So Leo checks the address carefully, not just the padlock.

### 1.5 Simple safe decisions

Inês gives Leo four rules for decisions he can make himself. Use well-known tools and settings rather than home-made tricks. Never click through a browser certificate warning on a site that should be trusted; report it instead. Keep secrets such as passwords and keys out of emails, chats and shared documents. When unsure, ask before changing anything. Leo notices the rules are about behaviour, not mathematics. Most real problems at small organisations come from settings and habits, and a beginner who follows these rules already avoids the commonest mistakes made by people who know far more theory.

### Worked example

Leo maps the library's website, e-book accounts and newsletter to the three promises, runs the fingerprint lab and explains to a staff member why the padlock alone is not enough.

> **Synthetic case.** Willow Lane Community Library, Leo and Inês are invented; RFC 8446 and RFC 5280 are real.

### Errors and limits

These are first approximations; real systems combine several mechanisms. A padlock on a fake site still looks like a padlock.

### Exercises

- **EX001 — Leo's goal.** What is Leo trying to achieve in this course? *Rubric:* 3 = understand core risks, explain them and complete one guided task safely;; 2 = part;; 1 = design cryptography;; 0 = none.
- **EX002 — Integrity in a library.** Give a library example of integrity. *Rubric:* 3 = noticing that a website file was altered by an intruder;; 2 = example;; 1 = confidentiality example;; 0 = none.
- **EX003 — Things cryptography cannot stop.** Name two things cryptography cannot prevent. *Rubric:* 3 = weak password guessing, clicking fake links, unlocked laptops (two);; 2 = one;; 1 = says it prevents all;; 0 = none.
- **EX004 — Base64 secrecy.** Does Base64 hide a password? Explain. *Rubric:* 3 = no; it is encoding anyone can reverse without a key;; 2 = no;; 1 = yes;; 0 = none.
- **EX005 — One-letter change.** In the lab, what happened when one letter changed? *Rubric:* 3 = the SHA-256 fingerprint changed completely, match False;; 2 = changed;; 1 = same;; 0 = none.
- **EX006 — Reversing a hash.** Can a SHA-256 fingerprint be turned back into the original text? *Rubric:* 3 = no, hashing is one-way;; 2 = no;; 1 = yes;; 0 = none.
- **EX007 — Who reads encrypted data.** Who can read data encrypted with AES? *Rubric:* 3 = only someone holding the right key;; 2 = key holder;; 1 = anyone;; 0 = none.
- **EX008 — Signature check.** What does a digital signature let anyone check? *Rubric:* 3 = who signed it and that it was not changed, using a public key;; 2 = who signed;; 1 = hides content;; 0 = none.
- **EX009 — Padlock promise.** What does the browser padlock actually promise? *Rubric:* 3 = the connection is protected by TLS to the site named in the certificate;; 2 = TLS connection;; 1 = site is honest;; 0 = none.
- **EX010 — Fake site padlock.** Why can a fake library site still show a padlock? *Rubric:* 3 = it can get its own certificate for a look-alike name;; 2 = own certificate;; 1 = impossible;; 0 = none.
- **EX011 — Certificate warning.** What should Leo do if the library site shows a certificate warning? *Rubric:* 3 = not click through; report it;; 2 = report;; 1 = click through;; 0 = none.
- **EX012 — Secrets in chat.** Where should passwords and keys never be shared? *Rubric:* 3 = email, chat or shared documents;; 2 = one place;; 1 = anywhere fine;; 0 = none.
- **EX013 — Rules focus.** What do Inês's four rules mostly concern? *Rubric:* 3 = behaviour and settings rather than mathematics;; 2 = behaviour;; 1 = maths;; 0 = none.

### Synthesis

Cryptography keeps promises of confidentiality, integrity and authenticity through keys, and beginners stay safe by matching tools to promises and following simple rules.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) explain why permission comes before any check; (2) define a small, safe scope; (3) handle personal data and secrets with care; (4) report problems responsibly.

### 2.1 Permission first

Leo is curious and wants to scan the library's network to see what is there. Inês stops him: checking systems without permission can be illegal, can break fragile devices like the old self-service kiosk and can upset partners whose systems sit on the same network. Even with good intentions, testing needs written permission from the person responsible. For Leo, that is the library manager, who signs a short note. Leo learns that asking first is not a formality; it protects the library, its members and Leo himself, and it builds the trust that lets him help again later.

### 2.2 A small, safe scope

The signed note lists exactly what Leo may do: read the library website's certificate details in his browser, check that staff laptops have disk encryption turned on, and review whether the e-book account page uses a strong password policy. It lists what he may not do: scan the network, try passwords, touch the book supplier's systems or the council's Wi-Fi equipment. It also names the week and Inês as his contact. A small scope keeps a beginner's first task safe and finishable. Leo writes the scope at the top of his notes and checks each step against it before starting.

### 2.3 Personal data and secrets

Libraries hold personal data: names, addresses, borrowing history. While checking a laptop, Leo might see member records on screen. Inês teaches him to look only at what the task needs, close anything else and never copy personal data into his notes. If he finds a password written on a sticky note or saved in a text file, he records where it was and what kind of secret it is, but not the password itself, and tells Inês the same day so it can be changed. Writing a secret down in a report would only spread the problem further.

### 2.4 Reporting responsibly

When Leo finds something wrong, he reports it to Inês and the manager, not to friends or social media. His report says what he saw, where, when and why it matters, in plain words, with a suggested next step. If he ever spotted a weakness in a product many libraries use, such as the e-book platform, the right path would be to tell the supplier privately through the library so they can fix it before details become public. This is called coordinated disclosure. Responsible reporting turns a discovery into a fix instead of a new risk.

### Worked example

Leo gets a signed scope note, checks two laptops for disk encryption within it, finds a password sticky note, records only its location and reports it to Inês.

> **Synthetic case.** The scope note, laptops and sticky note are synthetic.

### Errors and limits

Permission does not make careless work safe. Rules on personal data vary by country; follow the library's policy.

### Exercises

- **EX014 — Scan refusal.** Why did Inês stop Leo scanning the network? *Rubric:* 3 = no permission; could be illegal, break devices or affect partners;; 2 = one reason;; 1 = fine to scan;; 0 = none.
- **EX015 — Who grants permission.** Who signs Leo's permission note? *Rubric:* 3 = the library manager;; 2 = manager;; 1 = Leo;; 0 = none.
- **EX016 — Allowed checks.** List two checks Leo may do. *Rubric:* 3 = two of read website certificate, check laptop disk encryption, review password policy;; 2 = one;; 1 = scan network;; 0 = none.
- **EX017 — Forbidden actions.** Name two actions outside Leo's scope. *Rubric:* 3 = two of scanning, trying passwords, supplier systems, council Wi-Fi equipment;; 2 = one;; 1 = none;; 0 = none.
- **EX018 — Small scope benefit.** What does a small scope give a beginner? *Rubric:* 3 = a safe, finishable first task;; 2 = safe;; 1 = none;; 0 = none.
- **EX019 — Member record seen.** What should Leo do if a member's record appears on screen? *Rubric:* 3 = look only at what the task needs, close it and not copy it;; 2 = close it;; 1 = copy it;; 0 = none.
- **EX020 — Sticky note.** How should Leo record a password found on a sticky note? *Rubric:* 3 = location and type only, then tell Inês to change it;; 2 = location;; 1 = writes password;; 0 = none.
- **EX021 — Report contents.** What should Leo's report include? *Rubric:* 3 = what, where, when, why it matters and a next step;; 2 = three;; 1 = vague;; 0 = none.
- **EX022 — Wrong audience.** Who should not hear about a weakness first? *Rubric:* 3 = friends or social media;; 2 = names;; 1 = the manager;; 0 = none.
- **EX023 — Platform weakness.** How should a weakness in the e-book platform be handled? *Rubric:* 3 = coordinated disclosure to the supplier through the library;; 2 = supplier;; 1 = post online;; 0 = none.
- **EX024 — Coordinated disclosure name.** What is the private-first reporting path called? *Rubric:* 3 = coordinated disclosure;; 2 = named;; 1 = none;; 0 = none.
- **EX025 — Kiosk risk.** Which fragile device could an unapproved scan disrupt? *Rubric:* 3 = the old self-service kiosk;; 2 = kiosk;; 1 = none;; 0 = none.
- **EX026 — Protection of asking.** Whom does asking permission protect? *Rubric:* 3 = the library, its members and Leo;; 2 = two;; 1 = nobody;; 0 = none.

### Synthesis

Safe practice means getting permission, keeping a small scope, handling personal data and secrets carefully and reporting through the right people.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Cryptography and trust services: systems, data and dependencies

### Learning outcomes

You will (1) list the library's systems and where cryptography is used; (2) explain how passwords should be stored; (3) recognise dependencies on outside suppliers; (4) understand why keys and certificates expire.

### 3.1 Systems and their cryptography

With Inês, Leo lists the library's systems. The website uses TLS so visitors' connections are private. The e-book account system stores members' passwords and is run by an outside supplier. Staff laptops use built-in disk encryption, so a stolen laptop does not expose files. Public Wi-Fi uses a shared password, which keeps out casual neighbours but does not protect users from each other. The newsletter platform signs outgoing email so receivers can tell it really comes from the library. Leo is surprised how many places use cryptography quietly, without anyone at the library thinking about it.

### 3.2 How passwords should be stored

Leo asks how a website remembers his password. Inês explains that a good system never stores the password itself. It stores the result of a slow, salted password-hashing function such as scrypt, described in RFC 7914, or Argon2id, described in RFC 9106. The salt is a random value per user, so two members with the same password get different stored results. When you log in, the system repeats the calculation and compares. If thieves steal the database, slow hashing makes guessing expensive. The lab below shows salted storage on synthetic accounts using Python's standard library.

### Lab — Salted password storage

```python
# Salted scrypt storage for synthetic members. Teaching only; real systems use maintained libraries.
import hashlib, hmac, secrets
P = dict(n=2**14, r=8, p=1, dklen=32)
def store(pw):
    s = secrets.token_bytes(16); return s, hashlib.scrypt(pw, salt=s, **P)
def check(pw, rec): return hmac.compare_digest(hashlib.scrypt(pw, salt=rec[0], **P), rec[1])
m1, m2 = store(b"ReadMore2026"), store(b"ReadMore2026")
print("same password, same stored value?", m1[1] == m2[1])
print("member 1 right password:", check(b"ReadMore2026", m1))
print("member 2 right password:", check(b"ReadMore2026", m2))
print("member 1 wrong password:", check(b"ReadLess2026", m1))
```

Run with `python3 lab_salted.py`. Verified output:

```text
same password, same stored value? False
member 1 right password: True
member 2 right password: True
member 1 wrong password: False
```

### 3.3 Depending on suppliers

Many of the library's protections are run by others. The e-book supplier stores members' password hashes; the newsletter platform holds the email signing key; the web host renews the website certificate. The library cannot change these settings directly, but it depends on them. Inês shows Leo how to check what the supplier promises, for example in its security page or contract, and who to contact if something goes wrong. Knowing the dependency list means that when a supplier announces a problem, the library knows at once whether members are affected and what to tell them.

### 3.4 Why things expire

Certificates and some keys have end dates. A certificate that expires makes browsers show warnings, which happened to the library website last year when the web host's automatic renewal failed silently. Expiry exists so that a key cannot be used forever if it was quietly stolen, and so that settings get refreshed. Inês now keeps a simple calendar of expiry dates with reminders a month ahead, even for items suppliers renew automatically. Leo learns that cryptography is not set-and-forget: someone must watch dates, renewals and suppliers, or the protection itself can cause an outage.

### Worked example

Leo builds a five-row table of library systems, their cryptographic use and who controls them, runs the salted storage lab and adds the website certificate to the expiry calendar.

> **Synthetic case.** Systems, suppliers and the past outage are synthetic; RFC 7914 and RFC 9106 are real.

### Errors and limits

A shared Wi-Fi password gives limited protection between users. Supplier promises still need checking over time.

### Exercises

- **EX027 — Laptop encryption purpose.** What does laptop disk encryption protect against? *Rubric:* 3 = a stolen laptop exposing its files;; 2 = theft;; 1 = network attacks;; 0 = none.
- **EX028 — Shared Wi-Fi limit.** What does the shared Wi-Fi password not do? *Rubric:* 3 = protect users on the network from each other;; 2 = limit;; 1 = protects everything;; 0 = none.
- **EX029 — Newsletter signing.** Why does the newsletter platform sign emails? *Rubric:* 3 = so receivers can tell mail really comes from the library;; 2 = authenticity;; 1 = secrecy;; 0 = none.
- **EX030 — Never stored.** What should a good login system never store? *Rubric:* 3 = the password itself;; 2 = password;; 1 = the hash;; 0 = none.
- **EX031 — Salt meaning.** What is a salt in password storage? *Rubric:* 3 = a random value per user so equal passwords give different results;; 2 = random value;; 1 = secret key;; 0 = none.
- **EX032 — Lab result.** In the salted lab, did two members with the same password get the same stored value? *Rubric:* 3 = no, they differed; both verified with the right password;; 2 = no;; 1 = yes;; 0 = none.
- **EX033 — Slow hashing value.** Why is slow hashing useful if a database is stolen? *Rubric:* 3 = it makes each guess expensive for thieves;; 2 = expensive;; 1 = faster;; 0 = none.
- **EX034 — Supplier key.** Who holds the email signing key? *Rubric:* 3 = the newsletter platform;; 2 = platform;; 1 = library;; 0 = none.
- **EX035 — Checking a supplier.** Where can the library check a supplier's promises? *Rubric:* 3 = its security page or contract;; 2 = one place;; 1 = nowhere;; 0 = none.
- **EX036 — Past outage cause.** Why did the library website show warnings last year? *Rubric:* 3 = the host's automatic renewal failed silently and the certificate expired;; 2 = expired;; 1 = hacked;; 0 = none.
- **EX037 — Purpose of expiry.** Give one reason certificates expire. *Rubric:* 3 = limits use of a stolen key or forces refresh of settings;; 2 = one;; 1 = none;; 0 = none.
- **EX038 — Calendar reminders.** How far ahead does Inês set expiry reminders? *Rubric:* 3 = a month;; 2 = month;; 1 = none;; 0 = none.

### Synthesis

Small organisations depend on cryptography in many systems and suppliers, so they must know where it is used and watch passwords, keys and expiry dates.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Cryptography and trust services: guided lab and applied synthesis

### Learning outcomes

You will (1) complete a guided task verifying a downloaded file with a published fingerprint; (2) interpret the result correctly; (3) write a short plain-language summary for the library team; (4) plan your next learning steps.

### 4.1 The guided task

The library wants to install a free catalogue tool on a staff laptop. The project's website publishes a SHA-256 fingerprint for each download. Inês asks Leo to check that the file he downloaded matches. The idea is simple: if even one byte of the file was damaged or swapped, the fingerprint will differ. Leo does the task in a safe way, using a synthetic file in the lab below, then repeats the steps with the real download under Inês's supervision. The lab compares a correct file and a tampered file against the published value and prints match or mismatch for each.

### Lab — Checking a download fingerprint

```python
# Compare synthetic downloads with a published SHA-256 fingerprint.
import hashlib
original = b"catalogue-tool v2.1 synthetic installer bytes " * 50
published = hashlib.sha256(original).hexdigest()
tampered = original[:-1] + b"!"
print("published:", published[:24] + "...")
for name, data in [("download_ok.bin", original), ("download_bad.bin", tampered)]:
    print(name, "MATCH" if hashlib.sha256(data).hexdigest() == published else "MISMATCH")
```

Run with `python3 lab_checkfile.py`. Verified output:

```text
published: 215e60edb672063786f8bb92...
download_ok.bin MATCH
download_bad.bin MISMATCH
```

### 4.2 Reading the result

A match tells Leo the file is identical to the one whose fingerprint was published. It does not tell him the software is safe or free of bugs, and if an attacker had changed both the file and the fingerprint on the same website, the check would still match. That is why some projects also sign their releases with a digital signature, which needs the project's private key to forge. Leo writes down both points. A mismatch means stop: do not install, download again from the official site and tell Inês if it still fails.

### 4.3 Summarising for the team

Leo writes a five-sentence summary for library staff. The catalogue tool download was checked against the fingerprint published by the project and matched. This shows the file was not damaged or swapped on the way. It does not prove the software is safe, so it is installed only on one laptop first. If a check ever fails, the file must not be installed. Leo also lists the three findings from earlier chapters: the password sticky note, the expiry calendar and the warning about clicking through certificate errors, each with who will act.

### 4.4 What comes next

The course ends with a short reflection. Leo can now explain the three promises, tell encoding from encryption, ask for permission and scope, store nothing secret in notes and check a download fingerprint. He knows what he does not know: how TLS negotiates keys, how certificates are issued, and how organisations manage keys over years. Inês recommends next steps: the Professional course, and reading accessible chapters of the Handbook of Applied Cryptography by Menezes, van Oorschot and Vanstone, whose chapters are free online. Leo leaves with a clear picture of the core risks and one safe task completed.

### Worked example

Leo runs the fingerprint lab, verifies the real download under supervision, writes a five-sentence staff summary and lists three earlier findings with owners.

> **Synthetic case.** The catalogue tool, files and fingerprints are synthetic; the Handbook of Applied Cryptography is real.

### Errors and limits

A fingerprint from the same website as the file proves only that the two match. Signatures need the signer's key to be trusted correctly.

### Exercises

- **EX039 — Published fingerprint.** What does the catalogue project publish for each download? *Rubric:* 3 = a SHA-256 fingerprint;; 2 = fingerprint;; 1 = password;; 0 = none.
- **EX040 — Lab outcomes.** What did the lab print for the correct and tampered files? *Rubric:* 3 = MATCH for the correct file, MISMATCH for the tampered one;; 2 = one;; 1 = both match;; 0 = none.
- **EX041 — Meaning of a match.** What does a matching fingerprint prove? *Rubric:* 3 = the file is identical to the published one;; 2 = identical;; 1 = software is safe;; 0 = none.
- **EX042 — Match is not safety.** What does a match not prove? *Rubric:* 3 = that the software is safe or bug-free;; 2 = safety;; 1 = proves all;; 0 = none.
- **EX043 — Same-site weakness.** When could a fingerprint check be fooled? *Rubric:* 3 = if an attacker changed both file and fingerprint on the same site;; 2 = both changed;; 1 = never;; 0 = none.
- **EX044 — Signed releases.** Why do some projects also sign releases? *Rubric:* 3 = forging a signature needs the project's private key;; 2 = private key;; 1 = no reason;; 0 = none.
- **EX045 — Mismatch action.** What should Leo do after a mismatch? *Rubric:* 3 = stop, do not install, download again from the official site, tell Inês if it fails again;; 2 = stop;; 1 = install anyway;; 0 = none.
- **EX046 — Staged install.** Why is the tool installed on one laptop first? *Rubric:* 3 = a match does not prove the software is safe;; 2 = caution;; 1 = none;; 0 = none.
- **EX047 — Earlier findings.** List the three earlier findings in Leo's summary. *Rubric:* 3 = sticky note password, expiry calendar, certificate warning advice;; 2 = two;; 1 = none;; 0 = none.
- **EX048 — Admitted unknowns.** Name two topics Leo knows he has not learnt yet. *Rubric:* 3 = two of TLS key negotiation, certificate issuance, long-term key management;; 2 = one;; 1 = none;; 0 = none.
- **EX049 — Free reading.** Which reference does Inês recommend with free chapters online? *Rubric:* 3 = Handbook of Applied Cryptography by Menezes, van Oorschot and Vanstone;; 2 = title;; 1 = none;; 0 = none.
- **EX050 — Next course.** What course does Inês suggest next? *Rubric:* 3 = the Professional course;; 2 = named;; 1 = none;; 0 = none.

### Synthesis

Checking a published fingerprint is a small, real cryptographic task, and understanding what it does and does not prove is the course's final lesson.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Leo Fernandes, Inês Hartley, Willow Lane Community Library and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** To understand the core risks, explain them to the library team and safely complete one guided task.

**EX002.** Noticing that a page on the library website has been changed by someone who should not have changed it.

**EX003.** It cannot stop a weak password being guessed or a person clicking a fake link.

**EX004.** No. Base64 is only a way of writing data, and anyone can turn it back without any key.

**EX005.** The fingerprint was completely different and the match check printed False.

**EX006.** No. Hashing is one-way; you can only check a guess by hashing it and comparing.

**EX007.** Only someone who has the correct secret key.

**EX008.** Who signed the item and that it has not been altered, using the signer's public key.

**EX009.** That the connection is protected by TLS and the site holds a certificate for the name shown.

**EX010.** Because it can obtain a valid certificate for its own look-alike name, so the padlock appears.

**EX011.** Stop, do not click through, and report the warning to Inês.

**EX012.** Never in emails, chat messages or shared documents.

**EX013.** They concern behaviour and settings, which is where most real problems come from.

**EX014.** Because without permission it could be illegal, could break fragile devices like the kiosk and could affect partners' systems.

**EX015.** The library manager, who is responsible for the library's systems.

**EX016.** Reading the website's certificate details and checking that laptops have disk encryption on.

**EX017.** Scanning the network and trying passwords are both outside his scope.

**EX018.** It makes the first task safe and possible to finish.

**EX019.** Look away from what the task does not need, close it and never copy it into notes.

**EX020.** He notes where it was and that it is a password, without writing it down, and tells Inês so it can be changed.

**EX021.** What he saw, where and when, why it matters and a suggested next step.

**EX022.** Friends and social media; findings go to Inês and the manager.

**EX023.** Tell the supplier privately through the library so it can be fixed before details are public.

**EX024.** Coordinated disclosure.

**EX025.** The library's old self-service kiosk, which might crash under scanning.

**EX026.** It protects the library, its members and Leo himself.

**EX027.** It stops files being read if a laptop is lost or stolen.

**EX028.** It does not protect people on the network from one another.

**EX029.** So that receiving mail systems can check that the newsletter really comes from the library.

**EX030.** The actual password; it keeps only a slow, salted hash.

**EX031.** A random value stored with each user's hash so that identical passwords produce different stored results.

**EX032.** No. Their stored values were different, and both still verified with the correct password.

**EX033.** It makes every password guess costly, slowing down thieves trying to recover passwords.

**EX034.** The newsletter platform supplier.

**EX035.** In the supplier's published security page or in the contract.

**EX036.** The certificate expired because the web host's automatic renewal failed without anyone noticing.

**EX037.** So that a quietly stolen key cannot be used forever.

**EX038.** One month before each expiry date.

**EX039.** A SHA-256 fingerprint of each file.

**EX040.** The correct file printed MATCH and the tampered file printed MISMATCH.

**EX041.** That the downloaded file is exactly the file whose fingerprint was published.

**EX042.** It does not prove the software is safe or free of bugs.

**EX043.** If an attacker replaced both the file and the published fingerprint on the same website.

**EX044.** Because forging a digital signature requires the project's private key, which an attacker on the website lacks.

**EX045.** Stop, not install, download again from the official site and tell Inês if it still fails.

**EX046.** Because the match does not prove safety, so trying it on one laptop limits harm if something is wrong.

**EX047.** The password sticky note, the expiry calendar and the advice not to click through certificate warnings.

**EX048.** How TLS negotiates keys and how certificates are issued.

**EX049.** The Handbook of Applied Cryptography by Menezes, van Oorschot and Vanstone.

**EX050.** The Professional course in cryptography and trust services.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, keys and data in this book are synthetic unless a sentence cites a public source.

- Biryukov, A., Dinu, D., Khovratovich, D., & Josefsson, S. (2021). *Argon2 memory-hard function for password hashing and proof-of-work applications* (RFC 9106). IETF. <https://www.rfc-editor.org/rfc/rfc9106>
- Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 public key infrastructure certificate and CRL profile* (RFC 5280). IETF. <https://www.rfc-editor.org/rfc/rfc5280>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- National Institute of Standards and Technology. (2001, updated 2023). *Advanced Encryption Standard (AES)* (FIPS 197). <https://doi.org/10.6028/NIST.FIPS.197-upd1>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
