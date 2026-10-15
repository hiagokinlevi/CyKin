# Quantum and Post-Quantum Security: A First Introduction

- Language: English (`en`); rapid course, one month; approximately 80 hours of planned study.
- Editorial state: **published**. Chapters 1–4 of 4 have authored teaching text; exercises EX001–EX052 (thirteen per chapter) have matching worked results; offline labs use the Python 3 standard library with verified outputs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: new learners with no security role and basic digital literacy who want to understand what quantum computing means for everyday security and complete one guided task safely.
- Relation to neighbouring books: the [professional book](../../../../professional-6-months/quantum-post-quantum-security/en/book/MANUSCRIPT.md) teaches the full migration workflow; the [technical book](../../../../technical-18-months/quantum-post-quantum-security/en/book/MANUSCRIPT.md) teaches hands-on configuration. **This book is a short, careful introduction**: core ideas, safe practice, how to map what a small organization depends on, and one guided lab.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not a qualification. No authority to test real systems. All organizations, people and numbers in examples are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Four chapters, roughly one per week: foundations and decisions (1), scope, permission and safe practice (2), systems, data and dependencies (3), and a guided lab with a short final synthesis (4). Each chapter has learning outcomes, plain-language teaching, worked examples, practice activities, common mistakes, thirteen short exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs run offline with Python 3 and print their results so you can check your run; you do not need programming experience to read them.

### The running example: Bluebird Bakery Online

**Bluebird Bakery Online (BBO)** is a synthetic family bakery with two shops, an office and an online shop where customers order cakes. It uses a web shop hosted by a provider, card payments through a payment company, a staff portal, a file-transfer service to receive supplier price lists, cloud email and an office Wi-Fi network. The owner, Priya, has read a news story about quantum computers and asks you, her nephew who is learning about security, what it means for the bakery. Every number about BBO is invented.

### Source policy

Primary sources were checked on 12 October 2026: NIST [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) and [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (August 2024), [NIST IR 8547 (initial public draft)](https://doi.org/10.6028/NIST.IR.8547.ipd), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) and [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). Standards change; re-check before relying on them.

## Contents

| Week | Chapter |
|---|---|
| 1 | [1 Foundations and decisions](#ch-01) |
| 2 | [2 Scope, permission and safe practice](#ch-02) |
| 3 | [3 Systems, data and dependencies](#ch-03) |
| 4 | [4 Guided lab and applied synthesis](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Quantum and post-quantum security: foundations and decisions

### Learning outcomes

You will (1) explain in plain words what encryption and digital signatures do; (2) describe what a quantum computer is and what it could break; (3) explain "harvest now, decrypt later" and "forge later"; (4) name the new post-quantum standards; (5) explain hybrid protection; and (6) make a first, sensible decision for a small organization.

### 1.1 Locks and seals

When you visit a web shop, your browser and the shop agree on a secret key that nobody else knows, then use it to scramble (encrypt) everything you send. This is like two people agreeing on a combination for a lock box while strangers listen — and still keeping it secret. The method that lets them do this is called *public-key cryptography*. The same family of methods also makes *digital signatures*: seals that prove a message, a website or a software update really came from who it says. Today's public-key methods have names like RSA and elliptic curves. A different family, *symmetric* encryption such as AES, does the bulk scrambling once the key is agreed.

### 1.2 What a quantum computer is

Ordinary computers use bits that are 0 or 1. Quantum computers use *qubits*, which follow the rules of quantum physics and can be combined in ways that let certain calculations run very differently. They are not simply faster computers; for most tasks — spreadsheets, websites, games — they bring no benefit. But for a few special mathematical problems they could be dramatically faster. One of those problems is exactly what RSA and elliptic curves rely on. In 1994 Peter Shor described a quantum method (published in a journal in 1997) that would break them on a large enough, reliable quantum computer. Such a machine does not exist yet, and experts disagree about when, or whether, it will.

### 1.3 What would and would not break

If a large, reliable quantum computer were built, it could work out the secret keys behind RSA and elliptic-curve cryptography. That would let an attacker read traffic protected by those methods and forge signatures. Symmetric encryption such as AES-256 and fingerprints (hashes) such as SHA-256 would remain strong. So the problem is specific: the "agree a secret" and "sign" parts of today's systems need replacing; the bulk encryption does not.

For Bluebird Bakery Online this means the card payments, the online shop's connections and the staff portal logins could all be affected one day, because they rely on agreeing keys and on signatures. The files themselves, once encrypted with AES, would stay safe. That is why the bakery's later actions focus on providers' key-agreement and signature plans rather than on its stored files.

### 1.4 Two kinds of risk with different timing

*Harvest now, decrypt later*: someone records scrambled traffic today, stores it, and unlocks it years later once a quantum computer exists. This only matters for information that must stay private for many years — medical details, contracts, identity documents, payroll. *Forge later*: once a quantum computer exists, someone could fake digital seals — for example, a fake software update. This matters most for things that must be trusted for a long time.

At the bakery, payroll files and customer accounts are the information most exposed to the first risk, because they must stay private for many years. The second risk matters for things like software updates on the tills or the oven controller, which rely on signatures to prove they are genuine. Order confirmations are useful only for months, so neither risk matters much for them.

### 1.5 The new standards

In August 2024 the US National Institute of Standards and Technology (NIST) published three new standards designed to resist quantum computers: [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203) (ML-KEM, for agreeing secret keys), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) (ML-DSA, for signatures) and [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (SLH-DSA, also for signatures). They are called *post-quantum cryptography*: ordinary software designed to resist future quantum attacks. NIST has also published a *draft* plan, [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd), proposing that the old methods be phased out after 2030 and stopped after 2035; because it is a draft, those dates may change.

### 1.6 Hybrid protection

During the changeover, many systems use *both* an old and a new method together, so that an attacker would have to break both. This is called *hybrid* protection ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) defines the terms). Modern web browsers and many websites already use a hybrid method called X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) to agree keys. If you use an up-to-date browser, some of your connections are probably already protected this way.

### 1.7 Deciding how much it matters: Lab M

A simple rule from Michele Mosca (2018) helps decide what to worry about. Add how many years information must stay private (*x*) to how many years it takes to change systems (*y*). If that total is more than the number of years until a capable quantum computer exists (*z*), the information is already at risk. Nobody knows *z*, so try several guesses.

```python
# Lab M (ch 1): Mosca's inequality x + y > z for synthetic Bluebird Bakery Online data, sweeping z.
assets = [  # (name, shelf-life x in years, migration time y in years) - synthetic
    ("customer accounts", 10, 2), ("supplier contracts", 7, 1), ("order confirmations", 0.5, 1), ("staff payroll files", 12, 2)]
for z in (10, 15, 20):  # years until a cryptographically relevant quantum computer: an assumption, not a forecast
    late = [n for n, x, y in assets if x + y > z]
    print(f"z={z:>2}: at risk now -> {', '.join(late) if late else 'none'}")
```

Expected output:

```text
z=10: at risk now -> customer accounts, staff payroll files
z=15: at risk now -> none
z=20: at risk now -> none
```

With a guess of ten years, customer accounts and payroll files would be at risk; with fifteen or twenty, nothing at the bakery would be. The sensible conclusion is not panic, but: keep software and services up to date so the bakery benefits from new protections as providers adopt them, and ask the providers holding long-lived data what their plans are.

### 1.8 Worked example

Priya asks: "Should I buy a 'quantum-proof' security box I saw advertised?" Answer: "No. There is no such thing as 'quantum-proof', and the protection that matters for us comes from the software our providers run. The new standards are already appearing in browsers and web services. Our job is to keep devices updated, use reputable providers and ask the ones holding customer and payroll data about their post-quantum plans."

Notice what the answer avoids: it does not promise the bakery is safe, and it does not suggest spending money now. It names the two kinds of data that matter most and the people who control them. A good first decision for a small organization is usually about asking the right questions of providers, not about buying equipment.

### 1.9 Practice activities

1. Write a three-sentence explanation of quantum risk for a friend who is not technical. 2. Find one news article about quantum computers and underline any claim that sounds exaggerated. 3. Re-run Lab M in your head with *z* = 8: which items would be at risk?

For the first activity, test your explanation on the friend and note any word they did not understand. For the second, compare the article's claims with what you learned here: does it say all encryption breaks, or give one firm date? For the third, check each item by adding its two numbers and comparing the total with 8.

### 1.10 Common mistakes

- Saying quantum computers "break all encryption" — symmetric encryption and hashes remain strong.
- Quoting a single date for when quantum computers will arrive.
- Buying products marketed as "quantum-proof".
- Treating draft dates as final rules.

Each mistake has a short correction. Say which methods are at risk: key agreement and signatures, not bulk encryption. Give ranges for timing, and say they are guesses. Ask what a product actually does instead of trusting a label. And when you mention the 2030 and 2035 dates, say they come from a draft.

### Exercises

- **EX001 — Lock and seal.** In one sentence each, explain what encryption and a digital signature do. Rubric: 3 = both accurate and plain.
- **EX002 — Not a faster laptop.** Explain why a quantum computer would not make a bakery's spreadsheet faster. Rubric: 3 = only special problems benefit.
- **EX003 — What breaks.** Which of RSA, AES-256, elliptic curves and SHA-256 would a large quantum computer break? Rubric: 3 = RSA and elliptic curves only.
- **EX004 — Harvest now.** Describe harvest-now-decrypt-later in your own words. Rubric: 3 = record now, unlock later, matters for long-lived secrets.
- **EX005 — Forge later.** Give one example of forge-later risk. Rubric: 3 = fake signed update or website, explained.
- **EX006 — Which data.** Which bakery data needs protection for many years: order confirmations, payroll files, today's menu? Rubric: 3 = payroll files, with reason.
- **EX007 — Standards.** Name the three 2024 NIST post-quantum standards and what each is for. Rubric: 3 = FIPS 203 key agreement; 204 and 205 signatures.
- **EX008 — Draft.** Is IR 8547 a final rule? Explain in one sentence. Rubric: 3 = draft proposing dates.
- **EX009 — Hybrid.** Explain hybrid protection in one sentence. Rubric: 3 = old and new together, both must be broken.
- **EX010 — Mosca.** With *x* = 7 and *y* = 1 (supplier contracts), at which guesses of *z* would they be at risk? Rubric: 3 = *z* below 8 years.
- **EX011 — Myth.** Correct: "Quantum computers can already read all internet traffic." Rubric: 3 = no such machine yet; only some methods vulnerable.
- **EX012 — Advice.** Give Priya two sensible actions. Rubric: 3 = updates, ask providers (or similar).
- **EX013 — Quantum-proof.** Why should "quantum-proof" claims make you cautious? Rubric: 3 = undefined claim, no guarantees, marketing.

### Synthesis

Quantum computers, if built at scale, would break today's methods for agreeing keys and signing, but not bulk encryption. New NIST standards and hybrid protection are already rolling out. For most organizations, the sensible decision is calm: protect long-lived information first, keep systems updated and ask providers about their plans.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) explain why permission is essential before checking any system; (2) write a simple scope; (3) collect only the information you need; (4) handle what you find responsibly; (5) avoid unsafe "experiments"; and (6) report clearly.

### 2.1 Why permission matters

Looking at how a website or service protects its connections can feel harmless, and ordinary use — visiting a site in your browser — is fine. But deliberately probing systems, running scanning tools or trying to make a connection use weaker settings is different: without the owner's permission it may be illegal, it can disrupt the service, and it breaks trust. Professionals always have written permission that says what they may do. In this course you will only work with your own devices, the bakery's systems with Priya's written agreement, and lab examples on your own computer.

### 2.2 A simple scope

A scope answers five questions: *What* systems may I look at? *How* may I look (for example, read settings, read documents, use my browser normally)? *When*? *What* will I do with the information? *Who* do I call if something seems wrong? Example: "With Priya's agreement on 1 October, I may review the bakery's account settings pages, provider documentation and my own browser's connection details for the online shop between 1 and 31 October. I will keep notes in a shared folder only Priya and I can access. I will not run scanning tools or test anything on the payment system. If anything looks wrong, I will tell Priya and the provider's support team."

### 2.3 Collecting only what you need

To understand quantum readiness, you need facts such as which provider runs a service, which security settings or versions it uses, and how long data must be kept. You do not need customers' names, card numbers, passwords or message contents. Writing down less is safer: if your notes are lost, nothing sensitive leaks.

At the bakery, a useful note might read: online shop, run by the web-shop provider, customer accounts kept about ten years. It would not include any customer's name or address. If you need an example to explain something, make one up rather than copying real data.

### 2.4 Responsible handling

If you come across something sensitive or worrying — a password written on a sticky note, a shared folder open to everyone, an alert from a provider — do not explore further. Tell the owner (Priya) straight away and suggest contacting the provider. Never try to "test" whether a found password works. If you think you have found a weakness in a company's product, tell the company privately; do not post about it publicly.

Write down what you saw, where and when, without copying the sensitive item itself. A note such as sticky note with a password on the office monitor, 9 October, reported to Priya is enough. The owner and the provider decide what happens next; your job is to tell them quickly and to stop there.

### 2.5 Unsafe experiments

Some online guides show how to force a connection to use older, weaker settings ("downgrade") or how to capture other people's network traffic. These are only appropriate in isolated labs run by trained professionals with permission. In this course, labs run entirely on your own computer with made-up data.

If you see such a guide, you can still learn from reading it, but do not follow its steps on any network you use, including the bakery's Wi-Fi. If a classmate or friend suggests trying one, explain that it could break other people's connections and that permission from the network owner is needed first.

### 2.6 Reporting clearly

A good note says: what you looked at, when, how, what you found, why it matters and what you suggest. Example: "8 October, bakery account page of the email provider (read only): the provider's help page says connections use modern TLS and lists post-quantum key exchange as 'rolling out'. Matters because staff emails include payroll attachments. Suggest: ask the provider for a date."

Short notes are easier to act on than long ones. Write each note on the day you make the observation, and keep the date and source with it. If you later learn something that changes the note, add a dated correction rather than editing the original, so that Priya can see what was known when.

### 2.7 Worked example

A classmate says: "Let's scan the shopping centre's Wi-Fi to see whose devices are quantum-vulnerable." The safe answer: "We don't have permission and it could expose other people's data. Instead, let's look at our own phones' settings and read the Wi-Fi provider's public documentation."

The answer refuses politely and offers a safe alternative that still teaches something. It also explains why: other people's data and the lack of permission. If the classmate insists, the right move is to stop and talk to a teacher or the venue's owner rather than argue.

### 2.8 Practice activities

1. Write a scope for reviewing your own home router's settings. 2. List three pieces of information you would *not* write down during a review. 3. Rewrite a vague note ("email is fine I think") into a clear one.

For the first activity, use the five scope questions from earlier in this chapter. For the second, think of things that would cause harm if your notes were lost. For the third, add what, when, how and the source to the vague note, and remove the words I think.

### 2.9 Common mistakes

- Thinking "it's public, so I can test it".
- Writing down passwords or customer details.
- Investigating further after finding something sensitive.
- Posting about weaknesses publicly before the owner can fix them.

Each mistake has a simple correction. Public means anyone may visit, not that anyone may test. Notes should hold facts about settings and providers, never secrets. Finding something sensitive is the signal to stop and tell the owner. And weaknesses are reported privately so the owner can fix them first.

### Exercises

- **EX014 — Permission.** Why is permission needed before running a scanning tool on a website? Rubric: 3 = legality, disruption, trust.
- **EX015 — Normal use.** Is visiting a website in your browser and looking at its padlock details acceptable? Explain. Rubric: 3 = yes, ordinary use; contrast with probing.
- **EX016 — Five questions.** List the five questions a scope answers. Rubric: 3 = what, how, when, data use, who to call.
- **EX017 — Scope writing.** Write a scope for reviewing BBO's staff portal settings. Rubric: 3 = all five elements.
- **EX018 — Do not collect.** Name three things not to collect. Rubric: 3 = card numbers, passwords, message contents (or similar).
- **EX019 — Found password.** What do you do if you find a password on a sticky note? Rubric: 3 = don't use, tell owner, suggest change.
- **EX020 — Product weakness.** How should you report a weakness in a company's product? Rubric: 3 = privately to the company, no public post.
- **EX021 — Downgrade.** Why are downgrade experiments not for this course? Rubric: 3 = risk, need isolated lab and permission.
- **EX022 — Clear note.** Rewrite "web shop ok" as a clear note. Rubric: 3 = what, when, how, finding, why, suggestion.
- **EX023 — Classmate.** Respond to a classmate who wants to scan public Wi-Fi. Rubric: 3 = refuse, reason, safe alternative.
- **EX024 — Storage.** Where should review notes be stored? Rubric: 3 = shared private folder with owner, not public.
- **EX025 — Something wrong.** What do you do if, during your review, a service stops working? Rubric: 3 = stop, tell owner/provider, note time.
- **EX026 — Labelled examples.** Why does this book label examples "synthetic"? Rubric: 3 = avoid confusion with real organizations.

### Synthesis

Safe practice starts with permission and a clear scope, collects only what is needed, handles sensitive discoveries responsibly, avoids risky experiments and reports clearly.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Quantum and post-quantum security: systems, data and dependencies

### Learning outcomes

You will (1) list the services a small organization depends on; (2) note what data each holds and for how long; (3) identify who controls the security of each service; (4) record facts with their source; (5) treat unknowns as questions; and (6) choose priorities.

### 3.1 Listing services

Start with what the business uses every day: the online shop, card payments, email, the staff portal, supplier file transfers, office Wi-Fi, the shop tills and any connected equipment such as an oven controller. Write each down with a one-line description.

Include things that are easy to forget because they just work: the office router, the card readers at the tills, and the cloud drive where Priya keeps receipts. For each service write who provides it and what it is for. A list made in ten minutes with Priya is a good start; it can be corrected later.

### 3.2 Data and lifetimes

For each service, note the kind of data it handles and how long that data must stay private. At BBO: customer accounts (names, addresses, order history; kept about ten years for tax and loyalty records); payroll files (twelve years); supplier contracts (seven years); order confirmations (useful for months). Long lifetimes mean harvest-now-decrypt-later matters more.

Ask Priya or her accountant how long each kind of record must be kept, rather than guessing. Write the lifetime in years next to each service, as Lab M uses them. These numbers drive the priorities later in this chapter, so a wrong lifetime can push an important service down the list.

### 3.3 Who controls security

Small organizations rarely run their own servers. The web-shop provider controls the shop's connections; the payment company controls card security; the email provider controls email; the router maker controls Wi-Fi equipment updates. BBO controls choices like which providers to use, keeping devices updated, and asking questions. Writing down the controller tells you whom to ask.

For each service on the list, add one line: who controls its security, and how to contact them. At the bakery most entries name a provider, which means the main action is asking them questions. Where Priya does control something, such as updating the office router, note that too.

### 3.4 Recording facts with their source

Each fact should say where it came from: "Provider help page, 8 October", "Router settings page, version 2.1", "Asked Priya". Facts from documentation are less certain than facts you observed directly, such as your browser showing the connection details.

At the bakery, the online shop's hybrid key exchange was seen in your own browser's connection details, which is stronger evidence than a help page. The email provider's statement that post-quantum key exchange is rolling out is a claim from documentation and should be checked again later. Write the date beside each source, because pages change.

### 3.5 Unknowns are questions

If you do not know something — which security settings the oven controller uses — write "unknown" and turn it into a question for the right person. Unknown is not the same as safe.

Write each question to the person who can answer it: the oven-controller maker for its connections, the payroll provider for its post-quantum plans. Note when you sent the question and when you expect an answer. When an answer arrives, replace the unknown with the fact and its source.

### 3.6 Practical activity — Lab J

```python
# Lab J (ch 3): parse a synthetic JSON export of TLS endpoints and summarise key exchange by site.
import json, collections
export = json.loads("""[
 {"site": "shop", "host": "web-01", "group": "X25519MLKEM768"},
 {"site": "shop", "host": "till-02", "group": "secp256r1"},
 {"site": "bakery",  "host": "web-01", "group": "X25519"},
 {"site": "bakery",  "host": "oven-ctl", "group": null},
 {"site": "office","host": "web-01", "group": "X25519MLKEM768"}]""")
summary = collections.defaultdict(collections.Counter)
for e in export:
    g = e["group"]
    kind = "unknown" if g is None else ("hybrid" if "MLKEM" in g else "classical")
    summary[e["site"]][kind] += 1
for prop, c in sorted(summary.items()):
    print(f"{prop:9s} hybrid={c['hybrid']} classical={c['classical']} unknown={c['unknown']}")
```

Expected output:

```text
bakery    hybrid=0 classical=1 unknown=1
office    hybrid=1 classical=0 unknown=0
shop      hybrid=1 classical=1 unknown=0
```

The bakery's oven controller has no recorded information, so it shows as unknown. The till at the shop and the web server at the bakery use older classical methods. The web servers at the shop and office already use hybrid protection, probably because their provider updated them.

Lab J groups made-up connection records by site and counts each kind. A record with no group is counted as unknown, not as safe. Run it and check that your output matches; then change one entry to see how the counts move.

### 3.7 Choosing priorities

Combine lifetimes and control. First: services holding long-lived data that BBO can influence — ask the payroll and email providers about their post-quantum plans and keep accounts updated. Next: services with unknowns — ask the oven-controller maker. Last: short-lived data such as order confirmations.

Write the priorities as a short numbered list with an owner for each item, usually Priya, and a date to check back. Payroll and email come first because their data lasts longest and the bakery can ask their providers directly. The list should fit on one page.

### 3.8 Worked example

BBO's list (synthetic): online shop (provider; customer accounts 10 years; hybrid key exchange seen in your browser's connection details, 8 October); payroll service (provider; 12 years; unknown — ask); email (provider; payroll attachments; "rolling out" — ask for date); supplier file transfer (provider; contracts 7 years; classical — ask); oven controller (manufacturer; no personal data; unknown — ask about updates). Priorities: payroll and email questions first.

The list mixes facts and unknowns, and each unknown ends with ask, which turns it into a task. It also records where each fact came from, such as your browser's connection details for the online shop. Priya can read it in two minutes and see what to do first.

### 3.9 Practice activities

1. List the services your household or a club you belong to depends on. 2. For each, write the data held, lifetime and controller. 3. Turn two unknowns into questions.

Use the same columns as the bakery list: service, data held, lifetime, who controls it. For the unknowns, write a question addressed to a named person or company. Keep the result private if it includes information about other people. Ask someone in the household or club to check your lifetimes, since they may know rules you do not.

### 3.10 Common mistakes

- Forgetting equipment such as tills and controllers.
- Treating unknown as safe.
- Writing facts without sources.
- Assuming the provider has it handled without asking.

Each mistake has a simple remedy. Walk round the premises to find equipment such as tills and controllers. Write unknown and add a question. Put a source and date beside every fact. And ask providers directly; a short email is cheap and the answer is useful. Review the list with the owner once a year, or when a provider changes.

### Exercises

- **EX027 — Service list.** List six BBO services. Rubric: 3 = six plausible services.
- **EX028 — Lifetimes.** Give data and lifetime for three services. Rubric: 3 = plausible pairs.
- **EX029 — Controller.** Who controls the security of the online shop's connections? Rubric: 3 = web-shop provider.
- **EX030 — Source.** Rewrite "email is quantum-safe" with a source and date. Rubric: 3 = sourced, dated, accurate wording.
- **EX031 — Unknown.** Turn "oven controller: unknown" into a question for the manufacturer. Rubric: 3 = clear, answerable question.
- **EX032 — Lab J counts.** From Lab J, how many endpoints are hybrid, classical and unknown in total? Rubric: 3 = 2, 2, 1.
- **EX033 — Lab J reading.** Which site needs follow-up first and why? Rubric: 3 = bakery: classical web server and unknown controller.
- **EX034 — Priority.** Why ask the payroll provider first? Rubric: 3 = longest lifetime, provider-controlled.
- **EX035 — Observed vs documented.** Which is stronger evidence: your browser's connection details or a help page? Rubric: 3 = observed, with reason.
- **EX036 — Low priority.** Why are order confirmations low priority? Rubric: 3 = short lifetime.
- **EX037 — Equipment.** Why include the till and oven controller? Rubric: 3 = connected devices can hold or carry data, need updates.
- **EX038 — Question list.** Write two questions for the email provider. Rubric: 3 = PQ plans/dates and what customers should do.
- **EX039 — Household.** Name one long-lived household data type and its service. Rubric: 3 = e.g. tax records in cloud storage.

### Synthesis

Mapping services, data lifetimes and who controls each service, with sourced facts and unknowns turned into questions, shows a small organization where to focus.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Quantum and post-quantum security: guided lab and applied synthesis

### Learning outcomes

You will (1) read a simple configuration audit; (2) explain "offered" versus "used"; (3) check, with permission, whether your own browser uses hybrid protection; (4) write a short readiness note for an owner; (5) list questions for providers; and (6) plan your next learning steps.

### 4.1 The guided lab — Lab T

This lab checks made-up configurations for four BBO services. It asks two questions: does the service offer the new hybrid method, and does it prefer it?

```python
# Lab T (ch 4): audit synthetic TLS server configurations for post-quantum key exchange and preference order.
configs = {  # service: ordered list of offered groups (server preference) - synthetic
    "online-shop": ["X25519MLKEM768", "X25519", "secp256r1"],
    "staff-portal": ["X25519", "X25519MLKEM768", "secp256r1"],
    "supplier-sftp": ["ecdh-sha2-nistp256"],
    "till-dashboard": ["X25519", "secp384r1"]}
HYBRID = {"X25519MLKEM768", "SecP256r1MLKEM768", "SecP384r1MLKEM1024"}
for svc, groups in configs.items():
    offered = [g for g in groups if g in HYBRID]
    if not offered: verdict = "CLASSICAL ONLY"
    elif groups[0] in HYBRID: verdict = "OK (hybrid preferred)"
    else: verdict = "WARN hybrid offered but not preferred"
    print(f"{svc:17s} {verdict}")
```

Expected output:

```text
online-shop       OK (hybrid preferred)
staff-portal      WARN hybrid offered but not preferred
supplier-sftp     CLASSICAL ONLY
till-dashboard    CLASSICAL ONLY
```

The online shop offers and prefers hybrid. The staff portal offers hybrid but prefers the older method, so most connections will still use the older one — like having a new lock fitted but still using the old one by habit. The supplier file transfer and till dashboard use only older methods.

The lab looks only at the order of groups in each made-up configuration. It does not connect to anything, so it is safe to run on your own computer. Try moving X25519MLKEM768 to the front of the staff portal's list and run it again to see the verdict change.

### 4.2 Offered versus used

A setting that *offers* the new method is not the same as connections that *use* it. What matters is what happens when a connection is made. Technical staff check this with connection logs or tools; as a learner, you can see it for your own browser.

At the bakery the staff portal is the clear example: it offers the hybrid method but lists the older one first, so most connections will use the older method. Your note to Priya should say offered but not preferred, not protected.

### 4.3 Checking your own browser (with permission)

On your own computer, using a website you normally visit, you can look at the connection details. In some browsers the security panel or developer tools show the "key exchange" used, and you may see X25519MLKEM768 for sites that use hybrid protection. This is ordinary use of your own browser — you are not probing the site. Do not use scanning tools against websites.

Record what you saw with the date, the site and where in the browser you found it, and keep the note in the shared folder. A screenshot of your own connection details is fine. If the panel shows an older key exchange, simply note it; do not try other tools to find out more.

### 4.4 Writing a readiness note

A readiness note for an owner should be short and calm: what you looked at, what you found, what it means and what to do. Example for Priya:

"Quantum readiness note — Bluebird Bakery Online (synthetic), 30 October. What I reviewed: our list of services, provider documentation and my own browser's connection to our online shop. Findings: the online shop uses the new hybrid protection; our staff portal offers it but does not prefer it; supplier file transfers and the till dashboard use older methods; the payroll provider and oven controller are unknown. What it means: no immediate danger, but payroll and email hold information that must stay private for many years. Suggested actions: ask the staff-portal and file-transfer providers to prefer the new method; ask the payroll and email providers for their post-quantum plans and dates; keep all devices and accounts updated; review again in six months."

### 4.5 Questions for providers

Good questions are specific and answerable: "Do your connections use post-quantum or hybrid key exchange (for example X25519MLKEM768)? If not, when? Which of our data do you keep, and for how long? How will you tell us about changes?"

Send the questions by email so that the answer is written down, and save the reply with the date. If a provider does not reply, ask again after a few weeks. Keep the questions short so that a support team can answer them without escalating.

### 4.6 Applied synthesis

Putting the month together: you can now explain what quantum computers threaten and what they do not (Chapter 1), work safely with permission (Chapter 2), map a small organization's services, data and controllers (Chapter 3), read a simple audit and write an owner's note (this chapter). That is a complete, useful first task.

The month's work produces three things the bakery can keep: a service list with lifetimes and controllers, a readiness note, and a set of provider questions. Together they let Priya act without needing to understand the mathematics.

### 4.7 Next steps

If you want to go further: the professional course teaches the full migration workflow; the technical course teaches hands-on configuration and verification. Keep up with news from reliable sources such as NIST, and be sceptical of headlines.

Before moving on, check that you can explain to someone else what harvest now, decrypt later means and why AES-256 stays strong. Revisit any exercises you scored below 3. Keep the readiness note as an example for later courses. Note the date you finished.

### 4.8 Worked example

Priya reads the note and asks: "So do we need to spend money?" Answer: "Not now. Our main actions are emails to providers and keeping things updated. If the payroll provider has no plan, we can consider switching at the next contract renewal."

The answer keeps the decision small and specific: send emails, keep updating, and revisit at contract renewal. If a provider's answer later shows a real problem, the next readiness note will say so, and spending can be discussed then.

### 4.9 Practice activities

1. Rewrite the readiness note for your household or club. 2. Draft one provider email from the questions above. 3. Explain "offered versus used" to a friend using an everyday analogy.

For the first activity, use the same four parts as the bakery note: what you reviewed, findings, what it means and suggested actions. For the second, pick one question from the provider list and address it to a real service you use. For the third, test your analogy on a friend. Share your work only with people you trust.

### 4.10 Common mistakes

- Reporting "offered" as "used".
- Scanning websites instead of looking at your own browser.
- Alarmist notes that ask for spending without need.
- Forgetting to set a review date.

Each mistake has a simple correction. Write offered but not preferred when that is what a configuration shows. Use your own browser, never scanning tools. Keep the tone calm and spending suggestions small. Put a review date on every note. Ask the owner whether the note was clear, and improve the next one using their answer.

### Exercises

- **EX040 — Lab T reading.** Which service in Lab T offers hybrid but does not prefer it? Rubric: 3 = staff-portal.
- **EX041 — Classical only.** Which services in Lab T use only older methods? Rubric: 3 = supplier-sftp and till-dashboard.
- **EX042 — Analogy.** Give an everyday analogy for "offered versus used". Rubric: 3 = clear and accurate.
- **EX043 — Own browser.** Why is checking your own browser's connection details acceptable but scanning a site not? Rubric: 3 = ordinary use vs probing without permission.
- **EX044 — Note sections.** List the four parts of a readiness note. Rubric: 3 = reviewed, findings, meaning, actions.
- **EX045 — Calm tone.** Rewrite: "We are in huge danger from quantum hackers!" Rubric: 3 = calm, accurate.
- **EX046 — Provider question.** Write one specific question for the staff-portal provider. Rubric: 3 = asks to prefer hybrid/date.
- **EX047 — Review date.** Why include a review date? Rubric: 3 = standards and services change.
- **EX048 — Spending.** When might the bakery need to spend money? Rubric: 3 = provider has no plan → switch at renewal, or device replacement.
- **EX049 — Hybrid name.** What is the name of the hybrid method commonly used in browsers? Rubric: 3 = X25519MLKEM768.
- **EX050 — What it does not fix.** Name one thing hybrid key exchange does not fix. Rubric: 3 = signatures/certificates still classical (or data recorded earlier).
- **EX051 — Next course.** Which course would you take next to learn configuration, and which for workflow? Rubric: 3 = technical; professional.
- **EX052 — Final summary.** Summarise the month in three sentences. Rubric: 3 = threat, safe practice, mapping and action.

### Synthesis

The guided lab shows the difference between offering and using new protection; a short, calm readiness note and specific provider questions turn the month's learning into a useful first task for a real owner.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Bluebird Bakery Online is synthetic.

**EX001.** Encryption scrambles information so only someone with the key can read it. A digital signature is a seal that proves who created a message or update and that it was not changed.

**EX002.** Quantum computers only help with a few special mathematical problems; adding up columns in a spreadsheet is not one of them.

**EX003.** RSA and elliptic curves. AES-256 and SHA-256 remain strong.

**EX004.** Someone records scrambled traffic now and keeps it until a future quantum computer can unlock it; it matters for information that must stay private for many years.

**EX005.** Once a quantum computer exists, an attacker could fake the signature on a software update so a device installs malicious software.

**EX006.** Payroll files: they must stay private for many years. Order confirmations and today's menu do not.

**EX007.** FIPS 203 (ML-KEM) for agreeing secret keys; FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) for signatures.

**EX008.** No: it is a draft that proposes phasing old methods out after 2030 and stopping them after 2035; the dates may change.

**EX009.** Hybrid protection uses an old and a new method together, so an attacker would have to break both.

**EX010.** 7 + 1 = 8, so at risk for guesses of *z* below 8 years.

**EX011.** No such quantum computer exists yet, and even a future one would only break some methods (key agreement and signatures), not all encryption.

**EX012.** Keep devices and accounts updated; ask providers that hold long-lived data (payroll, email) about their post-quantum plans.

**EX013.** "Quantum-proof" has no agreed meaning, nothing is guaranteed against all future attacks, and the term is often marketing.

**EX014.** Scanning without permission may be illegal, can disrupt the service and breaks trust with the owner.

**EX015.** Yes: visiting a site and reading the padlock or connection details is ordinary use; probing or scanning the site is not.

**EX016.** What systems; how; when; what you will do with the information; who to call.

**EX017.** "With Priya's written agreement (date), I may view the staff-portal settings pages and provider documentation, 1–31 October, reading only. Notes go in our private shared folder. I will not change settings or run tools. Contact: Priya, then the provider's support."

**EX018.** Card numbers, passwords, contents of messages (or customers' personal details).

**EX019.** Don't try it; tell Priya straight away; suggest changing it and removing the note.

**EX020.** Privately to the company's security contact, with details; don't post publicly while they fix it.

**EX021.** They can weaken or break real connections and need an isolated lab, training and permission.

**EX022.** "8 October, my browser on the bakery's online shop (normal visit): connection details show hybrid key exchange X25519MLKEM768. Matters because customer accounts are kept ten years. Suggest: no action; recheck in six months."

**EX023.** "No — we don't have permission and it could expose strangers' data. Let's check our own phones and read the provider's public information instead."

**EX024.** In a private shared folder that only the owner and you can access, not on public or personal accounts.

**EX025.** Stop, note the time and what you were doing, and tell Priya and the provider.

**EX026.** So nobody mistakes teaching examples for facts about real organizations.

**EX027.** Online shop, card payments, email, staff portal, supplier file transfer, office Wi-Fi (also tills, oven controller).

**EX028.** Online shop: customer accounts, 10 years. Payroll: payroll files, 12 years. Supplier transfer: contracts, 7 years.

**EX029.** The web-shop provider.

**EX030.** "According to the email provider's help page (read 8 October), post-quantum key exchange is 'rolling out'; no date given."

**EX031.** "Which security methods does the oven controller use for its connections and updates, and will you provide updates that support the new NIST post-quantum standards?"

**EX032.** Hybrid 2, classical 2, unknown 1.

**EX033.** The bakery site: its web server uses only a classical method and its oven controller is unknown.

**EX034.** Payroll data has the longest lifetime (12 years) and is controlled by the provider, so asking is the main action.

**EX035.** Your browser's connection details (observed), because a help page may be out of date or general.

**EX036.** They are only useful for a few months, so recorded copies would not matter years later.

**EX037.** Connected devices may carry data and need security updates; they are easy to forget.

**EX038.** "Do you use post-quantum or hybrid key exchange for email connections, and from when?" "Is there anything we need to do on our side?"

**EX039.** Tax records stored in a cloud drive (kept many years).

**EX040.** staff-portal.

**EX041.** supplier-sftp and till-dashboard.

**EX042.** A new, stronger lock fitted to the door but the family still locks only the old one out of habit.

**EX043.** Looking at your own browser is ordinary use of your own device; scanning a site probes someone else's system without permission.

**EX044.** What I reviewed; findings; what it means; suggested actions (plus a review date).

**EX045.** "Future quantum computers could weaken some of today's protections. We are checking our providers' plans and keeping systems updated."

**EX046.** "Can you configure the staff portal to prefer the hybrid post-quantum key exchange (X25519MLKEM768) that it already offers, and when?"

**EX047.** Standards, providers and services change, so the note needs refreshing.

**EX048.** If a provider holding long-lived data has no plan, consider switching at contract renewal; or when old equipment must be replaced.

**EX049.** X25519MLKEM768.

**EX050.** Website certificates and signatures still use older methods (and data recorded before the change remains exposed).

**EX051.** Technical course for configuration; professional course for the workflow.

**EX052.** "Quantum computers could one day break today's key-agreement and signature methods, so long-lived secrets matter now. We work only with permission and collect little. Mapping the bakery's services, data and providers showed where to ask questions, and a short note gave Priya calm, practical actions."

## Four-subject teaching route

This is the **rapid** introductory course for new learners, following the synthetic **Bluebird Bakery Online (BBO)**: foundations and decisions, safe practice, mapping services and dependencies, and one guided lab with an owner's readiness note.

<a id="references"></a>

## References

Links checked 12 October 2026; standards status changes, so re-verify.

- IETF RFCs: 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST IR 8547 initial public draft (2024). <https://doi.org/10.6028/NIST.IR.8547.ipd>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
