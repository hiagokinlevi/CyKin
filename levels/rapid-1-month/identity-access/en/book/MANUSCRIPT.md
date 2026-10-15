# Identity and Access Management: Rapid Course

- Language: English (`en`); course 010, Rapid course (1 month).
- Editorial state: **published**. Chapters 1–20 have hand-written teaching text; exercises EX001–EX066 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. The rapid planning minimum is 20 lessons and there is no maximum. These twenty lessons meet that minimum. Independent review remains open. Page count is not the writing target. This is not a finished qualification.
- Audience: newcomers and small-business staff who need safe, practical identity and access basics in one month.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only identity systems and accounts you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic accounts, entitlements, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

<!-- open-cyber-academy:chapter-lessons -->

## How to use this book

Read the chapters in order. This English edition publishes twenty lessons, and each numbered chapter is that lesson. Five chapters in a row can be one study week; the grouping does not make a second copy of the text. Mia Clarke's first four lessons cover what the florist accounts protect, the written permission and safe habits, the seven-row account list, and the checklist with the short report. Lessons 5–20 each take one later florist question and leave both laboratory prints where the files already have them. Twenty lessons meet the planning minimum. They do not close this review, and they do not award a qualification. Run each lab where its chapter shows it, try each exercise before the worked result, and score the rubric yourself.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Mia Clarke** | Rapid-course learner | Invented |
| **Joseph Mensah** | Coach | Invented |
| **Eastgate Skills Centre** | Fictional training centre | Invented |
| **Willow Lane Florist** | Fictional partner (one shop, six staff) | Invented |

### Core sources

NIST [SP 800-63-4](https://doi.org/10.6028/NIST.SP.800-63-4), [SP 800-63B-4](https://doi.org/10.6028/NIST.SP.800-63B-4), [SP 800-162](https://doi.org/10.6028/NIST.SP.800-162), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); IETF [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749) and [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700); [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html); W3C [WebAuthn Level 2](https://www.w3.org/TR/webauthn-2/); OASIS [SAML 2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Identity and access: foundations and first decisions

### Learning outcomes

You will (1) explain what identity and access control protect; (2) describe a small shop's accounts; (3) choose first steps with limited time.

### 1.1 Why this course

Mia Clarke works part-time at the fictional Willow Lane Florist, a single shop with six staff run by its owner, Rosa. Mia joins a one-month rapid course at the fictional Eastgate Skills Centre to learn the basics of identity and access, coached by Joseph Mensah. Rosa has asked her to help make the shop's online accounts safer. Everything in this book, including the shop, staff and accounts, is synthetic, and every change Mia makes is agreed with Rosa first. She keeps a short diary of each week.

### 1.2 What access control protects

Identity and access control decide who can sign in to each account and what they can do once inside. At the florist, accounts protect customer orders and addresses, card payment records, the online shop, supplier orders, the accounts package and the shop's social media page. If someone else got into the online shop admin, they could change prices or redirect payments. If they got into email, they could reset passwords for every other account. Access control protects money, customers and reputation.

### 1.3 Three simple ideas

Joseph teaches three ideas. Identification is saying who you are, such as a username. Authentication is proving it, with a password and ideally a second step. Authorisation is what you may do once signed in. Mia sees that a shared login breaks identification, because nobody knows who made a change; a weak password breaks authentication; and giving everyone admin rights breaks authorisation. Knowing which idea a problem belongs to helps her pick the right fix. She writes the three ideas on a card to use all month.

### 1.4 Why email comes first

Email matters most, because most services send password reset links there. Whoever controls the shop's email can take over the online shop, social media and supplier accounts. Joseph explains that protecting email with a strong password and a second step is usually the single most valuable action for a small business. Mia notes that the shop has two email accounts: Rosa's own and a shared orders mailbox that all staff use. She marks both mailboxes at the top of her priority list, and she notes that the shared one is used by all six staff.

### 1.5 Choosing first steps

Mia has four weeks and little budget, so she learns to rank steps by three questions: how much harm does it prevent, what does it cost, and could it disrupt the shop? Turning on a second sign-in step for email prevents much harm, is free and causes little disruption, so it comes first. Buying new software would come later, if at all. Ranking keeps a short course focused on actions that remove the most risk quickly. Rosa agrees the ranking before work starts.

### 1.6 Guidance worth knowing

Good guidance exists even for small shops. NIST SP 800-63B, a US government guide to digital identity, recommends long passwords checked against lists of known-leaked ones and favours stronger second steps such as passkeys. Passkeys use the W3C WebAuthn standard and only work on the genuine website, which protects against fake sign-in pages. Mia does not need to read whole standards; Joseph summarises the key points so her advice rests on recognised sources rather than guesswork. Joseph gives her the source names so she can cite them.

### 1.7 The plan for the month

Joseph and Mia agree a plan with Rosa. In week one, understand the accounts and choose priorities. In week two, agree what Mia may do and learn safe habits. In week three, list every account, who uses it and whether it has a second step. In week four, make the agreed changes, check them against a checklist and write a short report. A clear plan helps Rosa know what to expect and when. Rosa agrees the dates and adds them to the shop calendar.

### Worked example

Mia's notes list seven accounts and two email mailboxes; her first priority is a second sign-in step on email, because it controls password resets.

> **Synthetic case.** Willow Lane Florist, Mia Clarke, Rosa, Joseph Mensah, Eastgate Skills Centre and all data are synthetic; NIST SP 800-63B and W3C WebAuthn are real sources.

### Errors and limits

Spending the first week comparing paid products delays free steps that remove most risk.

### Exercises

- **EX001 — Shop size.** How many staff does the florist have? *Rubric:* 3 = six, one shop;; 2 = six;; 1 = sixty;; 0 = none.
- **EX002 — Admin takeover harm.** What could someone do in the online shop admin? *Rubric:* 3 = change prices or redirect payments;; 2 = payments;; 1 = vague;; 0 = none.
- **EX003 — Authentication meaning.** What is authentication? *Rubric:* 3 = proving who you are;; 2 = proof;; 1 = username;; 0 = none.
- **EX004 — Authorisation meaning.** What is authorisation? *Rubric:* 3 = what you may do once signed in;; 2 = permissions;; 1 = password;; 0 = none.
- **EX005 — Shared login problem.** Which idea does a shared login break? *Rubric:* 3 = identification;; 2 = who did it;; 1 = speed;; 0 = none.
- **EX006 — Email importance.** Why protect email first? *Rubric:* 3 = password resets go there;; 2 = resets;; 1 = it is free;; 0 = none.
- **EX007 — Mailboxes.** Which two email accounts does the shop have? *Rubric:* 3 = Rosa's own and shared orders mailbox;; 2 = two;; 1 = one;; 0 = none.
- **EX008 — Ranking questions.** What three questions rank each step? *Rubric:* 3 = harm prevented, cost, disruption;; 2 = three;; 1 = one;; 0 = none.
- **EX009 — Top step.** Why does a second step on email come first? *Rubric:* 3 = high harm prevented, free, little disruption;; 2 = cheap;; 1 = required;; 0 = none.
- **EX010 — Password guidance.** What does NIST SP 800-63B recommend for passwords? *Rubric:* 3 = long and checked against leaked lists;; 2 = long;; 1 = symbols;; 0 = none.
- **EX011 — Passkey benefit.** Why do passkeys resist fake sign-in pages? *Rubric:* 3 = only work on the genuine site;; 2 = genuine site;; 1 = longer;; 0 = none.
- **EX012 — Week three.** What happens in week three? *Rubric:* 3 = list accounts, users and second steps;; 2 = listing;; 1 = report;; 0 = none.
- **EX013 — Plan benefit.** How does the plan help Rosa? *Rubric:* 3 = she knows what to expect and when;; 2 = clarity;; 1 = vague;; 0 = none.

### Synthesis

Knowing what accounts protect and taking high-value, low-cost steps first is the basis of practical access control.

### Continue studying — lesson 01 (chapter 01 of 20)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) agree what Mia may do; (2) handle passwords safely; (3) learn everyday habits that protect accounts.

### 2.1 Getting permission

Before changing anything, Mia writes a short note listing the accounts she may look at, the changes she may make, such as turning on second steps, and the changes Rosa must do herself, such as anything involving payments. Rosa signs it. Joseph explains that permission protects everyone: the shop knows what Mia is doing, and Mia can show she acted as asked. Working without permission, even with good intentions, can cause confusion and harm. Mia keeps the signed note with her course notes.

### 2.2 Handling passwords safely

Mia must never ask staff to tell her their passwords, write them on paper or send them by message. Where she needs to set something up, the account holder signs in themselves while she guides them. Rosa uses a password manager, an app that stores passwords securely, so Mia helps her move the shop's passwords into it. Handling passwords safely means the review itself never exposes them, which is the first rule of helping with access. Joseph checks that she follows this rule.

### 2.3 Shared accounts

The shop's orders mailbox, online shop admin and social media page are shared: everyone uses the same password, kept on a note by the till. Mia learns why this matters: anyone who sees the note can sign in, former staff still know the password, and nobody can tell who made a change. Where a service allows separate accounts for each person, she plans to use them. Where it does not, the shared password moves into the password manager and is changed when anyone leaves.

### 2.4 Recognising fake messages

Joseph shows Mia how fake messages try to get people to sign in on look-alike pages. Signs include urgent language, unexpected requests to confirm a password and links whose address does not match the real site. The safest habit is never to sign in from an email link; instead open the website directly or use a saved bookmark. Mia makes a short note for staff explaining this, because the best technical protection can still be undone by one rushed click.

### 2.5 Everyday habits

Mia lists habits for staff: lock the till computer when stepping away; use a different password for work than for personal accounts; turn on a second step wherever offered; tell Rosa when you receive something suspicious; and tell Rosa when someone joins or leaves so their access can be added or removed. She keeps the list short and puts it by the till. Simple, repeated habits protect a small shop more than rules nobody remembers. Rosa reminds staff of the list at the weekly team chat.

### 2.6 When to ask for help

Some situations are beyond Mia's role: a suspected break-in to an account, a payment that looks wrong or a message threatening the shop. Joseph and Rosa agree that in these cases Mia stops, tells Rosa straight away and does not try to investigate alone. Rosa contacts the service provider or her bank. Knowing when to stop and ask is part of safe practice, because acting beyond your skills can make a problem worse. Mia writes the stop cases into her notes for quick reference.

### Worked example

Rosa signs a one-page permission note; shared passwords move from the note by the till into the password manager; a staff habits sheet is posted.

> **Synthetic case.** Notes, accounts and events are synthetic.

### Errors and limits

Collecting staff passwords to "check" them exposes them and breaks trust.

### Exercises

- **EX014 — Rosa's changes.** Which changes must Rosa make herself? *Rubric:* 3 = anything involving payments;; 2 = payments;; 1 = vague;; 0 = none.
- **EX015 — Permission value.** Why does permission protect Mia? *Rubric:* 3 = she can show she acted as asked;; 2 = proof;; 1 = vague;; 0 = none.
- **EX016 — Password rule.** What must Mia never ask staff? *Rubric:* 3 = to tell her their passwords;; 2 = passwords;; 1 = names;; 0 = none.
- **EX017 — Manager meaning.** What is a password manager? *Rubric:* 3 = an app that stores passwords securely;; 2 = app;; 1 = notebook;; 0 = none.
- **EX018 — Till note risk.** Why is a password note by the till risky? *Rubric:* 3 = anyone who sees it can sign in;; 2 = visible;; 1 = messy;; 0 = none.
- **EX019 — Shared fallback.** What if a service cannot give separate accounts? *Rubric:* 3 = store in manager, change when anyone leaves;; 2 = change on leave;; 1 = vague;; 0 = none.
- **EX020 — Fake signs.** Name one sign of a fake message. *Rubric:* 3 = urgent language;; 2 = mismatched link;; 1 = greeting;; 0 = none.
- **EX021 — Safest habit.** What is the safest sign-in habit? *Rubric:* 3 = open the site directly, not from email links;; 2 = bookmark;; 1 = click links;; 0 = none.
- **EX022 — Leaver habit.** Why tell Rosa when someone leaves? *Rubric:* 3 = so their access can be removed;; 2 = removal;; 1 = party;; 0 = none.
- **EX023 — Lock habit.** What should staff do when stepping away from the till? *Rubric:* 3 = lock the computer;; 2 = lock;; 1 = vague;; 0 = none.
- **EX024 — Stop cases.** Name one situation where Mia stops and tells Rosa. *Rubric:* 3 = suspected account break-in;; 2 = wrong payment;; 1 = lunch;; 0 = none.
- **EX025 — Who escalates.** Who contacts the provider or bank? *Rubric:* 3 = Rosa;; 2 = owner;; 1 = Mia;; 0 = none.
- **EX026 — Habit length.** Why keep the habits list short? *Rubric:* 3 = so staff remember it;; 2 = memorable;; 1 = cheap;; 0 = none.

### Synthesis

Written permission, careful password handling and simple habits make access work safe for everyone.

### Continue studying — lesson 02 (chapter 02 of 20)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Listing accounts and who uses them

### Learning outcomes

You will (1) list every account; (2) record users, owners and second steps; (3) find the riskiest gaps.

### 3.1 Why list accounts

You cannot protect accounts you have forgotten. Mia sits with Rosa and lists every online account the shop uses: email, the online shop, card payments, social media, the supplier portal and the accounting package. For each she records the account name, who uses it, who owns it and whether a second sign-in step is turned on. She does not record passwords. The list becomes the shop's map of where access lives, and she saves it in the password manager's notes.

### 3.2 Finding accounts

Some accounts are easy to forget. Mia looks through the shop's email for welcome messages and invoices from online services, checks the browser's saved sites on the shop computer with Rosa present, and asks staff which websites they use for work. She finds a supplier portal nobody had mentioned. Searching in several places catches accounts that were set up years ago by former staff and never written down anywhere. She adds each new find to the list with Rosa's confirmation, and she notes where she found it so the search can be repeated.

### 3.3 Owners and users

Every account needs an owner, the person responsible for deciding who may use it, and a list of users. At the florist, Rosa owns every account, but several are used by all staff. Mia notes where the users are more than needed: the online shop admin is used by Rosa and Mia, but the others only need to view orders, which the shop software can allow with a separate staff role. Fewer people with admin rights means fewer ways for mistakes or misuse to happen.

### 3.4 The account check

Mia writes a short Python script, using only the standard library, that reads the synthetic account list and reports accounts without a second step and accounts that are shared. It only reads the list and prints results, so nothing in the shop's accounts is touched. Joseph checks her script with her and confirms the output matches the list by hand. She tests it first on a tiny list where she already knows the answers. The output is saved with the date, so the check can be repeated in three months and the results compared. Rosa sees the output before any change is planned.

### Lab — Account check

```python
"""Account list check for a small shop (synthetic, read-only)."""
# service, account, used by, MFA on?, shared?
ACCOUNTS = [
    ("email", "owner@shop", "Rosa", True, False),
    ("email", "orders@shop", "all staff", False, True),
    ("online shop", "admin", "Rosa, Mia", False, True),
    ("card payments", "rosa.m", "Rosa", True, False),
    ("social media", "shop-page", "all staff", False, True),
    ("supplier portal", "willowlane", "Rosa", False, False),
    ("accounting", "rosa.m", "Rosa", True, False),
]

def main():
    no_mfa = [a for a in ACCOUNTS if not a[3]]
    shared = [a for a in ACCOUNTS if a[4]]
    print(f"accounts {len(ACCOUNTS)}, MFA on {len(ACCOUNTS) - len(no_mfa)}")
    for s, acct, _, _, sh in no_mfa:
        print(f"no MFA: {s} ({acct}){' - shared' if sh else ''}")
    print(f"shared accounts: {len(shared)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_accounts.py`. Verified output:

```text
accounts 7, MFA on 3
no MFA: email (orders@shop) - shared
no MFA: online shop (admin) - shared
no MFA: social media (shop-page) - shared
no MFA: supplier portal (willowlane)
shared accounts: 3
```

### 3.5 Reading the results

The script reads seven accounts. Three have a second step turned on: Rosa's email, card payments and accounting. Four do not: the shared orders mailbox, the shared online shop admin, the shared social media page and the supplier portal. Three accounts are shared. Mia notices that every shared account also lacks a second step, which makes them the riskiest: a password known by many people, with nothing else needed to sign in. Mia confirms these results by hand against the list before sharing them.

### 3.6 Ranking the gaps

Mia ranks the gaps with her three questions. The orders mailbox comes first, because it receives password resets for the online shop. The online shop admin is second, because it controls prices and payments. Social media is third, because a takeover would harm the shop's reputation. The supplier portal is fourth. She agrees the order with Rosa, who asks her to complete the first three in week four, with the supplier portal following if time allows. She records the order in her notes.

### Worked example

The account check shows 7 accounts, 3 with a second step and 3 shared; the four gaps are ranked orders mailbox, shop admin, social media and supplier portal.

> **Synthetic case.** Accounts, the script and results are synthetic.

### Errors and limits

Listing only the accounts people remember misses forgotten services set up by former staff.

### Exercises

- **EX027 — Not recorded.** What does Mia not record in the list? *Rubric:* 3 = passwords;; 2 = secrets;; 1 = owners;; 0 = none.
- **EX028 — Forgotten account.** Which forgotten account did Mia find? *Rubric:* 3 = a supplier portal;; 2 = supplier;; 1 = email;; 0 = none.
- **EX029 — Search places.** Name one place Mia looked for accounts. *Rubric:* 3 = welcome emails and invoices;; 2 = browser saved sites;; 1 = bins;; 0 = none.
- **EX030 — Owner role.** What does an account owner do? *Rubric:* 3 = decides who may use it;; 2 = decides;; 1 = pays;; 0 = none.
- **EX031 — Staff view role.** What do most staff need in the online shop? *Rubric:* 3 = only to view orders;; 2 = view;; 1 = admin;; 0 = none.
- **EX032 — Second-step count.** How many accounts had a second step on? *Rubric:* 3 = three of seven;; 2 = 3;; 1 = seven;; 0 = none.
- **EX033 — Shared count.** How many accounts were shared? *Rubric:* 3 = three;; 2 = 3 shared;; 1 = one;; 0 = none.
- **EX034 — Riskiest pattern.** Why are the shared accounts riskiest? *Rubric:* 3 = known by many and no second step;; 2 = both;; 1 = old;; 0 = none.
- **EX035 — First gap.** Which gap comes first? *Rubric:* 3 = orders mailbox;; 2 = mailbox;; 1 = supplier;; 0 = none.
- **EX036 — Social media rank.** Why is social media third? *Rubric:* 3 = takeover harms reputation;; 2 = reputation;; 1 = cost;; 0 = none.
- **EX037 — Script safety.** Why is the account script safe to run? *Rubric:* 3 = it only reads the list and prints;; 2 = read-only;; 1 = it is short;; 0 = none.
- **EX038 — Rosa's request.** What did Rosa ask for week four? *Rubric:* 3 = complete the first three gaps;; 2 = three;; 1 = all;; 0 = none.

### Synthesis

A complete account list with owners, users and second-step status shows exactly where to act first.

### Continue studying — lesson 03 (chapter 03 of 20)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Making changes, checking them and reporting

### Learning outcomes

You will (1) make agreed access changes; (2) check them against a checklist; (3) write a short report for the owner.

### 4.1 Turning on second steps

In week four Mia helps make the agreed changes, with Rosa signing in herself. For the orders mailbox, the email service allows separate staff accounts with access to a shared mailbox, so each staff member gets their own sign-in with an authenticator app, and the old shared password is retired. For Rosa's admin accounts, Rosa sets up a passkey on her phone. Mia checks each sign-in works before moving on, so nobody is locked out during a busy day. Each change is noted.

### 4.2 Fixing shared logins

For the online shop, Mia and Rosa create a staff role that can view and pack orders but not change prices or payment settings, and give each staff member their own login. Only Rosa and Mia keep admin rights, both with a second step. The social media service allows people to be added as page helpers using their own accounts, so the shared login is removed. The note by the till is shredded once the old passwords no longer work.

### 4.3 Removing former staff

Mia asks Rosa who has left in the past two years. Two former staff are still listed as helpers on the social media page, and one still has a login to the online shop. Rosa removes them. Mia explains that when shared passwords were in use, former staff might also have remembered them, which is why changing shared passwords and moving to personal logins matters. She adds leaving to the staff habits list. She records each removal and the date.

### 4.4 The checklist

Mia writes a standard-library script that compares a before-and-after checklist of eight items, such as every account listed with an owner, a second step on key accounts, no written shared passwords, a password manager in use, former staff removed and recovery details up to date. The script reads only the synthetic checklist and prints the scores, so it changes nothing. Mia fills in the before list during week one and the after list at the end of week four, with Rosa confirming each item. She tests the script on a small known example first, and saves both outputs with the report.

### Lab — Checklist score

```python
"""Before/after access checklist score for a small shop (synthetic, read-only)."""
ITEMS = [
    "every account listed with an owner",
    "MFA on email",
    "MFA on online shop admin",
    "MFA on social media",
    "no shared passwords written down",
    "password manager in use",
    "former staff removed",
    "recovery details up to date",
]
BEFORE = {0, 1}
AFTER = {0, 1, 2, 3, 4, 5, 6}

def main():
    for name, done in (("before", BEFORE), ("after", AFTER)):
        print(f"{name}: {len(done)}/{len(ITEMS)}")
    for i, item in enumerate(ITEMS):
        if i not in AFTER:
            print("still to do:", item)

if __name__ == "__main__":
    main()
```

Run with `python3 lab_checklist.py`. Verified output:

```text
before: 2/8
after: 7/8
still to do: recovery details up to date
```

### 4.5 Reading the score

Before the course, the shop met 2 of 8 items; afterwards it meets 7 of 8. The one remaining item is keeping recovery details up to date: some accounts still list a former staff member's phone number for account recovery. Mia explains that recovery details are how an account is regained if a password or phone is lost, so wrong details could let someone else reset an account or lock Rosa out. Rosa agrees to update them the following week.

Moving from 2 to 7 of 8 within the course shows how far a small shop can get with short, concrete steps.

### 4.6 The short report

Mia writes Rosa a one-page report in plain words: what was found, what was changed, the checklist score from 2 to 7 of 8, what remains and three habits to keep: add and remove people promptly, keep a second step on every account, and check the account list every three months. She adds the supplier portal as the next account to secure. Joseph reviews the report, and Rosa keeps it with the account list in the password manager. Rosa signs it.

Keeping it beside the account list means whoever next checks the list also sees what was agreed.

### Worked example

Personal logins replace three shared accounts, three former staff lose access and the checklist rises from 2 to 7 of 8; recovery details remain.

> **Synthetic case.** Changes, scores and people are synthetic.

### Errors and limits

Turning on second steps for everyone in the middle of a busy day without checking each sign-in risks locking staff out.

### Exercises

- **EX039 — Rosa's method.** What second step does Rosa use for admin accounts? *Rubric:* 3 = a passkey on her phone;; 2 = passkey;; 1 = text;; 0 = none.
- **EX040 — Mailbox fix.** How was the shared orders mailbox fixed? *Rubric:* 3 = personal sign-ins with access to the shared mailbox;; 2 = personal;; 1 = new password;; 0 = none.
- **EX041 — Staff role.** What can the shop staff role do? *Rubric:* 3 = view and pack orders, not change prices;; 2 = view;; 1 = everything;; 0 = none.
- **EX042 — Till note fate.** What happened to the till password note? *Rubric:* 3 = shredded after old passwords stopped working;; 2 = shredded;; 1 = kept;; 0 = none.
- **EX043 — Former staff found.** How many former staff still had access? *Rubric:* 3 = three;; 2 = 3;; 1 = vague;; 0 = none.
- **EX044 — Score change.** How did the checklist score change? *Rubric:* 3 = 2 to 7 of 8;; 2 = improved;; 1 = fell;; 0 = none.
- **EX045 — Remaining item.** Which item remains? *Rubric:* 3 = recovery details up to date;; 2 = recovery;; 1 = MFA;; 0 = none.
- **EX046 — Recovery risk.** Why do wrong recovery details matter? *Rubric:* 3 = could let someone else reset or lock Rosa out;; 2 = reset;; 1 = vague;; 0 = none.
- **EX047 — Report habits.** Name one habit in the report. *Rubric:* 3 = check the account list every three months;; 2 = add/remove promptly;; 1 = vague;; 0 = none.
- **EX048 — Next account.** Which account is next to secure? *Rubric:* 3 = supplier portal;; 2 = supplier;; 1 = email;; 0 = none.
- **EX049 — Report storage.** Where does Rosa keep the report? *Rubric:* 3 = in the password manager with the account list;; 2 = manager;; 1 = desk;; 0 = none.
- **EX050 — Checking sign-in.** Why check each sign-in before moving on? *Rubric:* 3 = so nobody is locked out on a busy day;; 2 = lockout;; 1 = speed;; 0 = none.

### Synthesis

Agreed changes, a simple checklist and a short report leave a small business safer and able to keep going alone.

### Continue studying — lesson 04 (chapter 04 of 20)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — The account print is not the checklist

### Learning outcomes

After this chapter, you should be able to:

1. Say which question each script answers.
2. Keep both prints.
3. Refuse a note that folds them into one score.

### 5.1 Two reads, taken at two moments.

The account script walks the seven-row list and prints how many rows have a second step, which rows do not, and how many are shared. Its embedded run says `accounts 7, MFA on 3`, then four `no MFA` lines, then `shared accounts: 3`. Chapter 3 says Rosa sees that output before any change is planned, and Joseph checks it against the list by hand. The checklist script does not read those rows. It compares two sets of eight yes-or-no items and prints `before: 2/8`, `after: 7/8`, and `still to do: recovery details up to date`. Week four's changes are described in prose and then scored by that second script. A classmate who copies 7/8 onto the account print, or who deletes the four `no MFA` lines because the checklist improved, is answering a question the first script never asked. Leave `lab_accounts.py` and `lab_checklist.py` as the runs that produced these two blocks.

### 5.2 Worked example

Match the sentence to the script that printed it.

| Cited line | Script | Decision |
|---|---|---|
| `accounts 7, MFA on 3` | Account list | Keep it on that print |
| `shared accounts: 3` | Account list | Keep it on that print |
| `before: 2/8` and `after: 7/8` | Checklist | Keep both counts |
| "So the account list now scores 7 of 8." | Neither script | Refuse |

> **Synthetic case.** Both prints belong to Willow Lane Florist. Neither is a re-run of the other.

### Errors and limits

A later improvement can be real and still leave the earlier print untouched. The two files are not drafts of one score.

### Apply

- **EX051 — Which print?** The account run says 7 accounts and MFA on 3. The checklist run says before 2/8 and after 7/8, with recovery still to do. May the checklist score replace the account print? *Rubric:* 3 = no; both prints stay; the account lines stay 7 accounts, MFA on 3 and shared 3; the checklist stays 2/8 then 7/8 with recovery still to do; do not edit either script;; 2 = the two prints stay different;; 1 = one print;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue studying — lesson 05 (chapter 05 of 20)

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Three with a second step is not seven

### Learning outcomes

After this chapter, you should be able to:

1. Name the three rows that already have a second step on the account print.
2. Keep the four `no MFA` lines.
3. Refuse to read 3 as 7.

### 6.1 The column counts flags, not wishes.

On the account list, the second-step flag is true for Rosa's own mailbox `owner@shop`, for card payments `rosa.m`, and for accounting `rosa.m`. Those are the three. The print therefore says `MFA on 3` out of `accounts 7`. The other four rows are printed, not implied: the orders mailbox, the online shop admin, the social page, and the supplier portal. Card payments and accounting share the label `rosa.m` and still are two services, both already flagged on, both used by Rosa alone. Nothing in that arithmetic says the four printed gaps grew a second step. The checklist's `after: 7/8` counts checklist items, not these seven rows, so it cannot be substituted for `MFA on 3`. Turning the four false flags to true would be a different list. This run does not contain that list.

### 6.2 Worked example

Say "three rows" when you mean the account column, and "seven items" only for the checklist.

| Claim | What the account print supports | Decision |
|---|---|---|
| "Three rows already have a second step." | `MFA on 3` | May stay |
| "Four named rows are printed without one." | The `no MFA` lines | May stay |
| "3 of 7 means the same as 7 of 8." | Different denominators | Refuse |
| "Flip the four flags." | No second run | Refuse |

> **Synthetic case.** The flags are synthetic columns. No second step is being switched on in this lesson.

### Errors and limits

A small numerator is easy to round upward. Here the printed gaps are the point of the count.

### Apply

- **EX052 — What does 3 count?** A classmate says MFA on 3 means every account now has a second step, because the checklist later reached 7 of 8. Which rows does 3 actually count, and which lines stay? *Rubric:* 3 = three rows only, owner email, card payments and accounting; the four no-MFA lines stay; 3 is not 7; the checklist 7/8 does not rewrite the account column;; 2 = keep MFA on 3 and the four lines;; 1 = the count only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue studying — lesson 06 (chapter 06 of 20)

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — The three shared lines stay on the account print

### Learning outcomes

After this chapter, you should be able to:

1. Name the three rows the account print marks shared.
2. Keep `shared accounts: 3`.
3. Leave week four's personal logins in the prose, not in a rewritten tuple.

### 7.1 Shared means one password for many people, on this list.

The account script prints `shared accounts: 3`. The rows with that flag are the orders mailbox used by all staff, the online shop admin used by Rosa and Mia, and the social page used by all staff. Chapter 3 says every one of those three also lacks a second step, which is why they were called the riskiest pattern: a password known by many people, and nothing further required to sign in. The supplier portal is not in that trio. Its shared flag is false, and only Rosa is listed as the user. Chapter 4 later describes personal sign-ins, a staff role, and removal of the shared social login. Those sentences sit in the narrative. They do not replace the tuples the first script reads, and they do not change the line `shared accounts: 3`. A note that prints `shared accounts: 0` because the prose moved on has edited a result the file still shows.

### 7.2 Worked example

Use the shared flag, not the later story, when you quote the account print.

| Row | Shared flag on the print | Decision |
|---|---|---|
| Orders mailbox, shop admin, social page | True | Keep them in the three |
| Supplier portal | False | Do not call it shared |
| `shared accounts: 3` | The tally | Keep the tally |
| "Week four set the tally to zero." | No new account run | Refuse |

> **Synthetic case.** The shared flags are fields in a synthetic list. No live password is shared in this chapter.

### Errors and limits

Describing a fix is not the same artifact as the list that justified the fix. Both can stand.

### Apply

- **EX053 — How many are shared?** Chapter 4 describes personal logins. The account print still says `shared accounts: 3`. What is the shared count on that print, and which row is not part of it? *Rubric:* 3 = the print stays at 3; the three are the orders mailbox, the shop admin and the social page; the supplier portal stays not shared; week-four prose does not rewrite the tally;; 2 = the tally stays 3;; 1 = the prose only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue studying — lesson 07 (chapter 07 of 20)

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — The orders mailbox line stays no-MFA and shared

### Learning outcomes

After this chapter, you should be able to:

1. Quote the orders-mailbox line from the account print.
2. Keep it apart from the checklist item "MFA on email".
3. Leave the week-four authenticator story as prose.

### 8.1 The reset mailbox is one row. "MFA on email" is another sentence.

Whoever holds the shop's email can ask other services to reset their passwords. That is why chapter 3 ranks the orders mailbox first: it receives those reset links, and on the account list it is shared by all staff with the second-step flag false. The print says `no MFA: email (orders@shop) - shared`. Rosa's own mailbox is a different row, `owner@shop`, and that row's second-step flag is already true. The checklist's before pair includes the single item "MFA on email". That item does not name `orders@shop`, and it does not erase the printed gap. In week four the narrative says each staff member received a personal sign-in with access to the shared mailbox, plus an authenticator app, and that the old shared password was retired. The account script was not run again. The password itself is never written. Until a new embedded run replaces the line, the gap on this print stays a gap.

### 8.2 Worked example

Point at the address in the line before you decide what the line claims.

| Sentence | Ground | Decision |
|---|---|---|
| "`orders@shop` is printed no-MFA and shared." | The account run | May stay |
| "`owner@shop` already has a second step." | The same list | May stay |
| "MFA on email was a before-item." | The checklist source | May stay, as that item |
| "So `orders@shop` dropped off the print." | No new run | Refuse |

> **Synthetic case.** The mailbox addresses are labels in the synthetic list. No message is opened.

### Errors and limits

One true flag on Rosa's mailbox does not cover the mailbox the whole staff share. The authenticator story does not back-fill the print.

### Apply

- **EX054 — Which mailbox changed on the print?** Week four gives staff their own sign-ins and an authenticator for the orders mailbox. What does the account print still say about `orders@shop`? *Rubric:* 3 = the line stays `no MFA: email (orders@shop) - shared`; the week-four story stays prose; "MFA on email" stays a separate checklist item; do not edit the script;; 2 = the printed line stays;; 1 = the story only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue studying — lesson 08 (chapter 08 of 20)

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — The shop admin line stays the week-three row

### Learning outcomes

After this chapter, you should be able to:

1. Read the shop-admin tuple as printed.
2. Keep the staff role in the narrative.
3. Refuse to add a name to the row.

### 9.1 The tuple names two people. The role does not add a third.

The account row says the online shop admin is used by Rosa and Mia, the second-step flag is false, and the shared flag is true. The print says `no MFA: online shop (admin) - shared`. That row is why a takeover could change prices or redirect payments, which is the harm chapter 1 names, and why chapter 3 ranks this gap second, after the orders mailbox. Week four describes a staff role that can view and pack orders and cannot change prices or payment settings, with each staff member given a personal login. Only Rosa and Mia keep admin, both with a second step in that narrative. The account list does not gain a row for the staff role, and it does not gain a personal name. Six staff remain an unnamed group. Writing another name into "Rosa, Mia" would invent a user the synthetic list does not contain. The checklist item "MFA on online shop admin" belongs to the other script's after set. It does not delete this `no MFA` line.

### 9.2 Worked example

Quote the users who are written. Stop before the users who are only described as "staff".

| Statement | In the account tuple? | Decision |
|---|---|---|
| Users are Rosa and Mia | Yes | May stay |
| The row is shared and has no second step | Yes, on the print | May stay |
| A staff role views and packs, not prices | Chapter 4 prose | May stay as prose |
| A named colleague was added to the tuple | No name | Refuse |

> **Synthetic case.** The admin row is a synthetic tuple. No shop price is changed.

### Errors and limits

A narrower role is a good design and still not a new laboratory line. Unnamed staff stay unnamed.

### Apply

- **EX055 — Who is on the admin row?** Week four creates a view-and-pack role. The account print still has one online-shop line. Who does that line name, and what must you not add? *Rubric:* 3 = the printed users stay Rosa and Mia; the row stays no-MFA and shared; the staff role stays prose; no new name is added;; 2 = Rosa and Mia stay the printed users;; 1 = the role only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue studying — lesson 09 (chapter 09 of 20)

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — The social page line stays no-MFA and shared

### Learning outcomes

After this chapter, you should be able to:

1. Quote the social-page line.
2. Keep the helper change in the narrative.
3. Leave the former helpers unnamed.

### 10.1 A takeover of the page harms reputation. The print still shows the old row.

Chapter 3 ranks social media third because a takeover would harm the shop's reputation. On the list the row is `shop-page`, used by all staff, second step false, shared true. The print says `no MFA: social media (shop-page) - shared`. Week four says the service lets people be added as page helpers with their own accounts, and that the shared login is then removed. Two former staff are still listed as helpers in that chapter, and Rosa removes them. The account script does not print those two people, does not print the removal, and does not drop the `no MFA` line. "All staff" stays the user field. Calling the former helpers by name, or printing `shared accounts` without this row, would add facts the run does not contain. The checklist item "MFA on social media" is an after-item on the other script. It is not a rewrite of `shop-page`.

### 10.2 Worked example

Keep the page's risk and the page's printed row in separate sentences.

| What someone says | Where it lives | Decision |
|---|---|---|
| "The print shows `shop-page` with no second step, shared." | Account run | May stay |
| "A takeover would harm reputation." | Chapter 3 | May stay |
| "Helpers moved to their own accounts." | Chapter 4 prose | May stay as prose |
| "The two former helpers are named on the print." | No names | Refuse |

> **Synthetic case.** The page is a synthetic row. No post is published from this lesson.

### Errors and limits

Removing a shared login in the story does not rename `all staff` on the list. The former helpers stay an unnamed pair.

### Apply

- **EX056 — What does the social line still say?** The narrative removes the shared social login. What user, second-step flag and shared flag does the account print still show for `shop-page`? *Rubric:* 3 = all staff, no MFA, shared; the helper change stays prose; the former helpers stay unnamed;; 2 = the printed line stays;; 1 = the narrative only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue studying — lesson 10 (chapter 10 of 20)

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — The supplier portal stays the next account

### Learning outcomes

After this chapter, you should be able to:

1. Say how the supplier portal entered the list.
2. Keep its printed flags.
3. Leave it as the next account, not a secured one.

### 11.1 A forgotten service is on the list. It is not in the finished set.

Mia finds the supplier portal by looking beyond what people remember: welcome mail and invoices, the browser's saved sites with Rosa present, and questions to staff. Nobody had mentioned it. She adds it with Rosa's confirmation. The row says the account label is `willowlane`, the user is Rosa, the second-step flag is false, and the shared flag is false. The print says `no MFA: supplier portal (willowlane)` and does not add `- shared`. Chapter 3 ranks it fourth. Rosa asks Mia to finish the first three gaps in week four, and the portal only if time allows. Chapter 4's report then names the supplier portal as the next account to secure. "Next" means it is still ahead. The checklist has no supplier line to flip, and the account script does not show a later true flag. Time allowing is not a sentence that the work was done. The label `willowlane` is this portal's account name. It does not become a second shop, and it does not collect a password.

### 11.2 Worked example

Call it next only while the file still calls it next.

| Fact | Status | Decision |
|---|---|---|
| Forgotten, then added with Rosa's confirmation | Chapter 3 | May stay |
| Rosa, no second step, not shared | The print | May stay |
| Next account in the report | Chapter 4 | May stay |
| "The portal now has a second step." | Not printed | Refuse |

> **Synthetic case.** The portal is a synthetic find. No supplier order is placed.

### Errors and limits

Finding an account is the start of the record. It is not the second step the row still lacks.

### Apply

- **EX057 — Is the portal finished?** The report lists the supplier portal as the next account. The account print shows `willowlane` with no second step, used by Rosa, not shared. Has that row been secured? *Rubric:* 3 = no; it stays the next account; the printed flags stay Rosa, no MFA and not shared; "if time allows" is not a completed change;; 2 = it stays next and the flags stay;; 1 = the rank only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue studying — lesson 11 (chapter 11 of 20)

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Recovery details stay the remaining item

### Learning outcomes

After this chapter, you should be able to:

1. Say which checklist item remains.
2. Keep `after: 7/8`.
3. Leave the phone number and the following week unprinted.

### 12.1 Recovery is how a lost sign-in is regained. Wrong details point at the wrong person.

The checklist prints `after: 7/8` and then one remainder: `still to do: recovery details up to date`. Recovery details are the way an account is regained if a password or a phone is lost. Chapter 4 says some accounts still list a former staff member's phone number, so the wrong person might reset an account or lock Rosa out. Rosa agrees to update them the following week. The agreement is a plan. The following week is not described as having happened, and no phone number is written anywhere in the book. The script's after set simply does not include that item, which is why the remainder line exists. Adding the item by hand, printing 8 of 8, or inventing the number would close a gap the file left open on purpose. The other seven checklist items can stand as the after score without this one. A former staff member's number is not the same fact as the three people whose access Rosa removes. Those removals are a different item, and this lesson does not merge them.

### 12.2 Worked example

Quote the remainder line. Do not finish it.

| Sentence | In the file? | Decision |
|---|---|---|
| "`after: 7/8`" | The checklist print | May stay |
| "Recovery details are still to do." | The same print | May stay |
| "Rosa agrees to update them the following week." | Chapter 4 | May stay as a plan |
| "The number was changed and the score is 8 of 8." | No | Refuse |

> **Synthetic case.** No recovery number is hidden elsewhere in the chapter. The blank is the evidence.

### Errors and limits

An agreed update is still future. Seven of eight is the score because the eighth item is the one named underneath it.

### Apply

- **EX058 — What remains?** The checklist prints after 7/8 and names recovery details. Rosa says she will update them the following week. What do you print as the phone number, and what is the after score? *Rubric:* 3 = no phone number; the after score stays 7/8; recovery stays still to do; the following week is not shown as done;; 2 = 7/8 stays and no number is added;; 1 = the agreement only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue studying — lesson 12 (chapter 12 of 20)

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — The before line stays two of eight

### Learning outcomes

After this chapter, you should be able to:

1. Keep `before: 2/8`.
2. Name the two items the source marks as already done.
3. Refuse to slide the week-four gains backward.

### 13.1 Week one records a short start. Week four must not be pasted over it.

Mia fills the before list during week one and the after list at the end of week four, with Rosa confirming each item. The print says `before: 2/8`. In the script the before set contains only the first two items: every account listed with an owner, and MFA on email. The other six items are absent from that set. Some of them appear in the after set, and recovery does not appear even there. Moving "former staff removed" or "password manager in use" into the before count would pretend the shop started where it finished. It would also hide the work week four describes. "MFA on email" as a before item still does not cancel the account print's `orders@shop` line. One checklist phrase and one mailbox row are different records, and chapter 8 keeps them apart. The before line stays 2. The after line stays 7. Neither number is a monthly average, and neither is printed as 8.

### 13.2 Worked example

Ask which week the item belongs to before you count it.

| Item | Before set | Decision |
|---|---|---|
| Every account listed with an owner | Included | Counts toward 2 |
| MFA on email | Included | Counts toward 2 |
| Former staff removed | Not included | Do not move it backward |
| `before: 2/8` | The print | Keep it |

> **Synthetic case.** The before list is a synthetic week-one page. It is not the report Rosa signs later.

### Errors and limits

A strong after score can tempt a reader to improve the start. The start is what made the change visible.

### Apply

- **EX059 — What was already true?** The print says `before: 2/8`. Which two items does the source count, and may "former staff removed" join them? *Rubric:* 3 = only every account listed with an owner, and MFA on email; the before line stays 2/8; later items stay out of the before set;; 2 = the before count stays 2 and the two items stay those two;; 1 = the count only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue studying — lesson 13 (chapter 13 of 20)

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — Three former staff, and no removal date is printed

### Learning outcomes

After this chapter, you should be able to:

1. Count the former staff who still had access.
2. Keep their names and the removal dates unprinted.
3. Leave "former staff removed" as a checklist item, not a calendar entry.

### 14.1 The count is three roles, not three named people.

Mia asks Rosa who has left in the past two years. Two former staff are still helpers on the social page, and one still has a login to the online shop. Rosa removes them. That is three people, matching the worked result in chapter 4. Mia records each removal and the date, and she adds leaving to the habits list so the next departure is reported. The manuscript never prints the date and never prints a name. The account rows still say "all staff" or "Rosa, Mia". They do not list the people who left. The checklist's after set includes "former staff removed", which is why that item is not on the `still to do` line. A ticked item is not a dated register. Shared passwords, while they existed, might also have been remembered by people who had left. That is why the move to personal logins matters. It does not add a fourth leaver, and it does not fill in the blank date. Two years is the question Mia asked. It is not a pair of calendar years written on the page.

### 14.2 Worked example

Count the access that was still open. Do not invent the diary entry.

| Record | What is shown | Decision |
|---|---|---|
| Two social helpers and one shop login | Chapter 4 | May stay |
| Rosa removes them | The same chapter | May stay |
| A removal date | Recorded, not printed | Do not invent it |
| A fourth leaver | Not in the count | Refuse |

> **Synthetic case.** The former staff stay unnamed. No diary page is reproduced.

### Errors and limits

Recording a date in a note the book does not show is not the same as the date being available to copy. Three stays three.

### Apply

- **EX060 — What do you date?** Rosa removes two social helpers and one shop login. Mia records the dates. Which date do you print, and how many people were removed? *Rubric:* 3 = three people, and no date is printed; no name is added; "former staff removed" stays a checklist item rather than a calendar line;; 2 = the count stays three and the date stays blank;; 1 = the count only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue studying — lesson 14 (chapter 14 of 20)

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — No password is written, and the till note is not restored

### Learning outcomes

After this chapter, you should be able to:

1. State the rule that Mia never asks for a password.
2. Keep the till note shredded in the story and absent as text.
3. Refuse to type a password into the lesson.

### 15.1 The manager stores secrets. This book does not repeat them.

Mia must never ask staff for their passwords, write them on paper, or send them by message. When something must be set up, the account holder signs in while she guides them. Rosa already uses a password manager. Mia helps move the shop's passwords into it. Where a service cannot give separate accounts, the shared password goes into that manager and is changed when anyone leaves. The till note, which held the shared passwords where anyone could see it, is shredded once those old passwords no longer work. None of those passwords is printed. The checklist before set does not include "no shared passwords written down"; the after set does. That shift records the habit. It does not reveal a secret, and it does not put the note back by the till. A classmate who types an example password so the shredding "makes sense" breaks the rule the chapter is teaching. Joseph checks that Mia follows the rule. The check does not produce a password either.

### 15.2 Worked example

Describe the container. Do not open it.

| Object | What the file shows | Decision |
|---|---|---|
| Staff asked for their passwords | Never | Keep that ban |
| Shop passwords | Moved into the manager | Do not quote them |
| Till note | Shredded after the old passwords failed | Do not restore it |
| An example password | Not in the book | Do not add one |

> **Synthetic case.** No practice password is supplied. The manager is named only as an app.

### Errors and limits

Shredding is told, not dated. A missing date does not mean the note is still beside the till.

### Apply

- **EX061 — What do you type?** The till note was shredded after the old passwords stopped working, and Mia never collects staff passwords. Which password do you add so a classmate can see the idea? *Rubric:* 3 = none; no password is written; the till note stays shredded in the story and is not restored; the manager stays the store;; 2 = no secret is typed and the note stays gone;; 1 = the rule only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue studying — lesson 15 (chapter 15 of 20)

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — The permission dates stay off the page

### Learning outcomes

After this chapter, you should be able to:

1. Say what the permission note allows and what it reserves.
2. Keep the stop cases with Rosa.
3. Leave the shop-calendar dates unprinted.

### 16.1 Permission is a signed limit. The calendar entry is not copied here.

Before any change, Mia writes a short note: which accounts she may look at, which changes she may make, such as turning on second steps, and which changes Rosa must do herself, such as anything involving payments. Rosa signs it. Mia keeps the signed note with her course notes. The signature lets Mia show she acted as asked. It does not let her cross into payments or into an investigation. If she suspects a break-in, sees a payment that looks wrong, or meets a message that threatens the shop, she stops, tells Rosa, and does not investigate alone. Rosa contacts the provider or the bank. Chapter 1 says Rosa agrees the week's dates and adds them to the shop calendar. Those dates are not printed. "Dates" as something a plan can have does not invent a day, a month, or a year for this shop. Finishing the checklist does not widen the note, and it does not move a stop case onto Mia's list of jobs. Working without the signature, even with good intentions, can cause confusion and harm. The file shows the signature. It does not show the calendar.

### 16.2 Worked example

Copy the boundary. Leave the unpublished days unpublished.

| Element | Shown? | Decision |
|---|---|---|
| Rosa's signature | Yes | Keep it |
| Payments reserved to Rosa | Yes | Keep the reserve |
| Stop, then Rosa calls the provider or bank | Yes | Keep the stop |
| A calendar date | Not printed | Do not invent one |

> **Synthetic case.** The permission note is not reproduced as a filled form. The shop calendar stays off the page.

### Errors and limits

An undated signature can still limit the work. Missing days do not make a payment change into Mia's task.

### Apply

- **EX062 — What do you add to the note?** Rosa has signed. A payment looks wrong, and the checklist is finished. Which date do you write, and who contacts the bank? *Rubric:* 3 = no date is printed; Rosa stays the person who contacts the provider or the bank; payments stay hers; Mia stops and does not investigate; finishing the checklist does not widen the note;; 2 = no date and Rosa keeps the escalation;; 1 = the signature only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue studying — lesson 16 (chapter 16 of 20)

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — The three-month check is a habit, not a second run

### Learning outcomes

After this chapter, you should be able to:

1. List what the one-page report is allowed to say.
2. Keep the three-month check as a habit.
3. Leave the supplier portal as the next account.

### 17.1 The report points at the prints. It does not replace them.

Mia's one-page report uses plain words: what was found, what was changed, the checklist score from 2 to 7 of 8, what remains, and three habits. The habits are to add and remove people promptly, to keep a second step on every account, and to check the account list every three months. Joseph reviews the report. Rosa signs it and keeps it in the password manager beside the account list, so the next person who opens the list also sees what was agreed. Chapter 3 saved the account output with a date so a later check could be compared. That date is not printed, and the comparison is not shown. "Every three months" is an instruction in the report. It is not a second embedded run, and it does not change `accounts 7, MFA on 3` or `shared accounts: 3`. The supplier portal remains the next account inside that same report. Storing the page does not secure the portal, and signing it does not complete the recovery update. Whoever next reads the list should still see the open items.

### 17.2 Worked example

Let the report cite the score it was given. Do not let it improve the score.

| Report line | Standing | Decision |
|---|---|---|
| Score from 2 of 8 to 7 of 8 | Matches the checklist print | May stay |
| Three habits, including a three-month look | Written as habits | May stay |
| Supplier portal next | Still next | May stay |
| "The three-month check has already been run." | No second print | Refuse |

> **Synthetic case.** The report is a synthetic page in a synthetic manager. It is not a notice to customers.

### Errors and limits

A signed page can still contain future work. Storage beside the list makes the open items easier to find. It does not close them.

### Apply

- **EX063 — Has the later check happened?** The report says to check the account list every three months, and Rosa signs it. The supplier portal is named as next. Which later run do you attach, and is the portal finished? *Rubric:* 3 = no later run is in the file; the habit stays a habit; the portal stays next; the stored report does not change either print;; 2 = no second run and the portal stays next;; 1 = the signature only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue studying — lesson 17 (chapter 17 of 20)

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — Six staff and one shop stay the size

### Learning outcomes

After this chapter, you should be able to:

1. State the shop's size as the book states it.
2. Keep "all staff" where the list says "all staff".
3. Refuse a named roster or a second shop.

### 18.1 Headcount is a boundary. It is not a roll call.

Willow Lane Florist is one shop with six staff, run by its owner, Rosa. Mia works there part-time and is on the rapid course. The account list never spells the six names. Where a row is used by the whole group, the user field says "all staff": the orders mailbox and the social page. Inventing five colleagues, splitting six into Rosa plus six, or adding a second shop because the supplier label says `willowlane` would change the case. Mia's part-time work does not print an hour count and does not add a seventh person. The three former staff are people who had left. They are not a revision of the six. Rosa remains the owner who signs the permission note and the report. Joseph remains the coach at Eastgate Skills Centre, not a member of the shop staff. A leaving note may repeat "six" and "one shop". It may not turn either figure into a roster.

### 18.2 Worked example

Repeat the size. Do not staff it with new people.

| Figure | Meaning | Decision |
|---|---|---|
| Six staff, one shop | The business | May stay |
| "all staff" on two rows | The printed user field | May stay |
| Mia works part-time | Her role | Do not convert it into hours or a seventh head |
| A second shop, or six names | Not written | Refuse |

> **Synthetic case.** No staff rota is attached. The shop has no street address in this book.

### Errors and limits

A small number is not an invitation to fill seats. Unnamed people stay an unnamed group.

### Apply

- **EX064 — How big is the shop?** The case says one shop and six staff. A classmate adds a second branch and names the six. What size do you keep, and what do you refuse to write? *Rubric:* 3 = one shop and six staff stay; no second shop; no names for the six; "all staff" stays the user field where the list uses it; part-time does not add a person;; 2 = the size stays and no names are added;; 1 = the size only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue studying — lesson 18 (chapter 18 of 20)

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-19"></a>

## Chapter 19 — Admin stays with Rosa and Mia

### Learning outcomes

After this chapter, you should be able to:

1. Separate the staff role from admin.
2. Keep Rosa and Mia as the admin pair.
3. Leave payments with Rosa, and leave any lockout unrecorded.

### 19.1 Fewer admins is the control. The pair is named, and the day is not.

Authorisation is what a person may do after signing in. Giving everyone admin breaks that idea, which is why most staff need only to view orders. Week four makes the limit concrete: the staff role can view and pack, and it cannot change prices or payment settings. Only Rosa and Mia keep admin, and the narrative says both have a second step. The account tuple still reads "Rosa, Mia". Dropping Mia because she is a learner, or adding the other staff because they now have logins, would rewrite either the tuple or the role. Payment settings stay inside the changes Rosa must do herself. Mia checks each sign-in before she moves on, so a busy day does not become a lockout. The book does not say that anyone was locked out, and it does not name the day. The check is a precaution that was followed. It is not an incident report. A note that grants the staff role the right to change prices, or that says the busy day ended in a lockout, adds an event the file does not contain.

### 19.2 Worked example

Say what the role can do, then stop at the boundary the chapter drew.

| Power | Who has it | Decision |
|---|---|---|
| View and pack orders | Staff role | May stay |
| Change prices or payment settings | Not the staff role | Keep it off that role |
| Admin | Rosa and Mia | Keep the pair |
| A recorded lockout | Not in the file | Do not add one |

> **Synthetic case.** No order is packed in this lesson. The busy day stays undated.

### Errors and limits

A careful sequence can still be told without a casualty. The absence of a lockout is not permission to skip the check.

### Apply

- **EX065 — Who may change a price?** The staff role views and packs orders. Admin stays with Rosa and Mia, and Mia checks each sign-in before moving on. May the staff role change prices, and was anyone locked out? *Rubric:* 3 = the staff role may not change prices or payment settings; admin stays Rosa and Mia; no lockout is recorded; payments stay Rosa's;; 2 = the role stays narrow and no lockout is added;; 1 = the pair only;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Continue studying — lesson 19 (chapter 19 of 20)

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-20"></a>

## Chapter 20 — What the florist note can say

### Learning outcomes

After this chapter, you should be able to:

1. Repeat both laboratory prints and the open items.
2. Reject a note that replaces a print or closes an open item.
3. Name the following subject while this review stays open.

### 20.1 A note may quote the file. It may not improve the file.

A leaving note may say what was already written. From the account run, keep `accounts 7, MFA on 3`, the four `no MFA` lines, and `shared accounts: 3`. From the checklist run, keep `before: 2/8`, `after: 7/8`, and `still to do: recovery details up to date`. The before pair stays the owner line and "MFA on email". The orders mailbox, the shop admin, and the social page stay shared on the account print even though week four tells a later story about personal logins. The supplier portal stays Rosa's, without a second step, and stays the next account. No recovery number, removal date, permission date, or password is available to copy. Six staff and one shop stay the size. Admin in the narrative stays with Rosa and Mia, and the staff role still cannot change prices or payments. No lockout is filed. Chapter 4's synthesis still says the agreed changes, the checklist, and the short report leave a small business safer and able to keep going alone. That sentence stays. It does not finish the recovery item, and it does not call the shop secure.

### 20.2 Worked example

| Leaving-note sentence | Why it fails or stands | Decision |
|---|---|---|
| "The account print shows 7 accounts, MFA on 3, and 3 shared." | The first script | May stay |
| "The checklist moved from 2 of 8 to 7 of 8, and recovery remains." | The second script | May stay |
| "The account list was re-run and every row has a second step." | No second account run | Reject |
| "Recovery was updated, the portal is done, and the score is 8 of 8." | All three are still open or unprinted | Reject |
| "A password, a second shop, and a lockout belong in the note." | None of those is filed | Reject |
| "Twenty lessons make the florist secure." | The review is still open | Reject |

> **Synthetic case.** The note is a classroom page about Willow Lane Florist. It is not a notice to customers.

### Errors and limits

Twenty English lessons meet Willow Lane Florist's planning minimum and leave this review open. A fresh florist question can still earn its own later Willow Lane Florist lesson. These English chapters do not publish another language edition. Identity and access management stays this course. Network and communications security is the learner's following subject. Open items at the shop stay open on that turn. These chapters do not call the florist secure, and they do not hand anyone a qualification.

### Apply

- **EX066 — Four claims.** A classmate's leaving note says the account print now shows MFA on 7 and shared accounts 0, that the checklist after line is 8/8 and the recovery phone number was updated, that the supplier portal has a second step and a shop password was copied into the note, and that twenty lessons make the florist secure. Which claims do you reject, and what do twenty lessons meet? *Rubric:* 3 = reject the rewritten account print, the 8/8 line, the updated phone number, the finished portal, and the copied password; keep accounts 7, MFA on 3, shared 3, before 2/8, after 7/8, and recovery still to do; twenty lessons meet the planning minimum and leave review open; do not call the florist secure;; 2 = reject the closings and keep both prints;; 1 = one claim;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Continue studying — lesson 20 (chapter 20 of 20)

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX066. Mia Clarke, Joseph Mensah, Eastgate Skills Centre, Willow Lane Florist and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Six staff in one shop.

**EX002.** Change prices or redirect payments.

**EX003.** Proving who you are, for example with a password and second step.

**EX004.** What you are allowed to do once signed in.

**EX005.** Identification, because nobody knows who made a change.

**EX006.** Most password reset links are sent to email.

**EX007.** Rosa's own mailbox and the shared orders mailbox.

**EX008.** How much harm it prevents, what it costs and whether it could disrupt the shop.

**EX009.** It prevents much harm, is free and causes little disruption.

**EX010.** Long passwords checked against lists of known-leaked ones.

**EX011.** They only work on the genuine website.

**EX012.** Listing every account, who uses it and whether it has a second step.

**EX013.** She knows what to expect and when.

**EX014.** Anything involving payments.

**EX015.** She can show she acted as asked.

**EX016.** To tell her their passwords.

**EX017.** An app that stores passwords securely.

**EX018.** Anyone who sees it can sign in, including former staff who remember it.

**EX019.** Keep the shared password in the manager and change it when anyone leaves.

**EX020.** Urgent language, an unexpected password request or a mismatched link address.

**EX021.** Open the website directly or use a bookmark instead of an email link.

**EX022.** So their access can be removed.

**EX023.** Lock the till computer.

**EX024.** A suspected account break-in, a wrong-looking payment or a threatening message.

**EX025.** Rosa.

**EX026.** Short lists are remembered and repeated.

**EX027.** Passwords.

**EX028.** A supplier portal nobody had mentioned.

**EX029.** Welcome emails and invoices, the browser's saved sites or asking staff.

**EX030.** Decides who may use the account.

**EX031.** Only to view orders, through a separate staff role.

**EX032.** Three of seven.

**EX033.** Three.

**EX034.** Their passwords are known by many people and they have no second step.

**EX035.** The orders mailbox, because it receives password resets.

**EX036.** A takeover would harm the shop's reputation.

**EX037.** It only reads the synthetic list and prints results.

**EX038.** Complete the first three gaps, with the supplier portal if time allows.

**EX039.** A passkey on her phone.

**EX040.** Each staff member got their own sign-in with access to the shared mailbox.

**EX041.** View and pack orders, but not change prices or payment settings.

**EX042.** It was shredded once the old passwords no longer worked.

**EX043.** Three: two social media helpers and one online shop login.

**EX044.** From 2 of 8 to 7 of 8.

**EX045.** Keeping recovery details up to date.

**EX046.** They could let someone else reset an account or lock Rosa out.

**EX047.** Add and remove people promptly, keep second steps, or check the list every three months.

**EX048.** The supplier portal.

**EX049.** In the password manager with the account list.

**EX050.** So nobody is locked out during a busy day.

**EX051.** No. Both prints stay. The account lines stay 7 accounts, MFA on 3, and shared 3. The checklist stays before 2/8 and after 7/8, with recovery still to do. Do not edit either script.

**EX052.** Three rows only: the owner email, card payments, and accounting. The four no-MFA lines stay. 3 is not 7. The checklist score of 7/8 does not rewrite the account column.

**EX053.** The print stays at 3: the orders mailbox, the shop admin, and the social page. The supplier portal stays not shared. Week-four prose does not rewrite the tally.

**EX054.** The line stays `no MFA: email (orders@shop) - shared`. The week-four story stays prose. "MFA on email" stays a separate checklist item. Do not edit the script.

**EX055.** The printed users stay Rosa and Mia. The row stays no-MFA and shared. The staff role stays prose. No new name is added.

**EX056.** All staff, no MFA, and shared. The helper change stays prose. The former helpers stay unnamed.

**EX057.** No. It stays the next account. The printed flags stay Rosa, no MFA, and not shared. "If time allows" is not a completed change.

**EX058.** No phone number. The after score stays 7/8. Recovery stays still to do. The following week is not shown as done.

**EX059.** Only "every account listed with an owner" and "MFA on email." The before line stays 2/8. Later items stay out of the before set.

**EX060.** Three people, and no date is printed. No name is added. "Former staff removed" stays a checklist item rather than a calendar line.

**EX061.** None. No password is written. The till note stays shredded in the story and is not restored. The manager stays the store.

**EX062.** No date is printed. Rosa stays the person who contacts the provider or the bank. Payments stay hers. Mia stops and does not investigate. Finishing the checklist does not widen the note.

**EX063.** No later run is in the file. The habit stays a habit. The portal stays next. The stored report does not change either print.

**EX064.** One shop and six staff stay. No second shop. No names for the six. "All staff" stays the user field where the list uses it. Part-time does not add a person.

**EX065.** The staff role may not change prices or payment settings. Admin stays Rosa and Mia. No lockout is recorded. Payments stay Rosa's.

**EX066.** Reject the rewritten account print, the 8/8 line, the updated phone number, the finished portal, and the copied password. Keep accounts 7, MFA on 3, shared 3, before 2/8, after 7/8, and recovery still to do. Twenty lessons meet the planning minimum and leave review open. Do not call the florist secure.

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
