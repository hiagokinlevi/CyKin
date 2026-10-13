# Security Operations and Blue Team: Rapid Course

- Language: English (`en`); course 015, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; One offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: managers and staff in small organisations who need basic security operations habits in one month.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: monitor and respond only on systems you are authorised to defend; no exploit code, no payloads, no attack procedures and no instructions for evading detection. Detections are taught from the defender's side using synthetic telemetry. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one office manager at a small accountancy from an invoice-fraud email through spotting signs, acting fast and keeping watch. Run the lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Leo Barros** | Office manager | Invented |
| **Elaine Finch** | Partner whose mailbox was compromised | Invented |
| **Marlow & Finch** | Fictional 12-person accountancy | Invented |
| **BrightPath IT** | Fictional outside IT support | Invented |

### Core sources

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker and Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security operations in one month: seeing what matters

### Learning outcomes

You will (1) explain what security operations means for a small organisation; (2) identify the few signals worth watching; (3) set up who watches and who acts; (4) introduce the case.

### 1.1 The case

Leo Barros is office manager at the fictional Marlow & Finch, a 12-person accountancy. IT is handled by a small outside support company, BrightPath IT. On a Monday morning, a client phones to ask why partner Elaine Finch emailed asking them to pay an invoice into a new bank account. Elaine sent no such email. Leo has one month, with this rapid course, to set up basic security operations so the firm notices such things itself.

The client's phone call is the only reason anyone found out. Nothing at the firm raised an alarm: no one watched sign-ins, and a hidden mailbox rule kept the clients' replies away from Elaine.

### 1.2 What security operations means

Security operations is the routine of watching for signs of attack, deciding what matters and acting quickly. Large firms run a security operations centre (SOC); small firms need the same habits on a small scale. MITRE's "11 Strategies of a World-Class Cybersecurity Operations Center" (Knerler, Parker and Zimmerman, 2022) starts with knowing what you protect and who has authority, which applies to a 12-person firm as much as to a bank.

For Leo, "knowing what you protect" means the client data and mailboxes, and "authority" means deciding in advance who may lock an account at 10 on a Monday morning without waiting for a partners' meeting. In this case that delay would have mattered: one client paid £4,800 into the criminal's account that morning.

### 1.3 What to protect

For Marlow & Finch: client financial data, email accounts (because criminals use them for invoice fraud) and the accounts software. Email matters most because it is how money is requested.

Leo ranks email first because of what happened to Elaine: one mailbox, accessed with one stolen password, was enough to send a fake invoice to two clients and hide the replies. The client data and accounts software matter too, but an attack on them would most likely start with a mailbox like hers. So most of the plan protects and watches the email accounts.

### 1.4 A few good signals

A small firm cannot watch everything. Leo picks four signals: sign-ins from unusual countries or at night, new mailbox forwarding rules, multi-factor authentication (MFA) changes, and staff reports of odd emails. These cover the most common ways small firms are attacked.

Each signal matches part of Elaine's incident. The criminal signed in at night from Brazil, set up a forwarding rule four minutes later, and worked on an account without MFA. The fraud was spotted only because a client phoned with an odd email. With these four signals in place, the forwarding rule alone would have produced an alert on Friday night, before any client paid.

### 1.5 Who watches, who acts

BrightPath IT receives security alerts from the email service and calls Leo for anything urgent. Leo can ask BrightPath to reset passwords and block sign-ins at any hour; partners are told afterwards. This is written on one page and signed by both partners.

The page also answers the question that slows small firms down: who may lock a partner out of her own mailbox? Leo may, and the partners learn afterwards. On the Monday of the fraud, Leo approved the actions at 10:05, and BrightPath had revoked Elaine's sessions three minutes later. Without the signed page, Leo would have needed to reach both partners first.

### 1.6 Frameworks in plain words

NIST CSF 2.0 (CSWP 29, 2024) groups security work into Govern, Identify, Protect, Detect, Respond and Recover. Leo's plan touches each: a signed page (Govern), knowing what matters (Identify), MFA (Protect), the four signals (Detect), the call list (Respond) and backups (Recover).

The framework does not add work; it checks for gaps. Before the incident, Marlow & Finch had no MFA, no alerts and no call list, so Protect, Detect and Respond were empty. Using the six words as a checklist showed Leo that his plan needed something in each, and that backups, for Recover, were the only part already in place.

### Worked example

Leo's one-page plan: protect email, client data and accounts software; watch four signals; BrightPath watches and calls Leo; Leo may approve resets and blocks at any time; the partners review monthly. Elaine signs it and asks for the fraud to be investigated first.

> **Synthetic case.** Marlow & Finch, BrightPath IT and all events are invented.

### Errors and limits

Four signals will not catch everything; they target the most likely problems.

### Exercises

- **EX001 — Monday call.** What did the client's call reveal? *Rubric:* 3 = email from Elaine asking payment to new bank account; she did not send it; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Security operations meaning.** Define security operations in one sentence. *Rubric:* 3 = watch, decide, act quickly; 2 = partial; 1 = vague; 0 = none.
- **EX003 — Most important asset.** Why does email matter most here? *Rubric:* 3 = criminals use it to request money; 2 = partial; 1 = vague; 0 = none.
- **EX004 — Four signals.** List Leo's four signals. *Rubric:* 3 = unusual sign-ins; forwarding rules; MFA changes; staff reports; 2 = three; 1 = one; 0 = none.
- **EX005 — Watcher.** Who watches alerts and who approves actions? *Rubric:* 3 = BrightPath watches; Leo approves; 2 = partial; 1 = vague; 0 = none.
- **EX006 — Night authority.** Can Leo act before telling partners? *Rubric:* 3 = yes; partners told afterwards; 2 = partial; 1 = vague; 0 = none.
- **EX007 — CSF mapping.** Map MFA and backups to CSF functions. *Rubric:* 3 = MFA Protect; backups Recover; 2 = one; 1 = vague; 0 = none.
- **EX008 — Plan length.** Why keep the plan to one page? *Rubric:* 3 = people read and use it; 2 = partial; 1 = vague; 0 = none.
- **EX009 — Signal limits.** What is the limit of four signals? *Rubric:* 3 = won't catch everything; 2 = partial; 1 = vague; 0 = none.
- **EX010 — Partner review.** How often do the partners review? *Rubric:* 3 = monthly; 2 = one; 1 = vague; 0 = none.
- **EX011 — 11 Strategies lesson.** Which idea from the 11 Strategies applies to a small firm? *Rubric:* 3 = know what you protect and who has authority; 2 = partial; 1 = vague; 0 = none.
- **EX012 — First task.** What did Elaine ask to be done first? *Rubric:* 3 = investigate the fraud; 2 = partial; 1 = vague; 0 = none.
- **EX013 — Protected items.** Name the three things to protect. *Rubric:* 3 = client data, email, accounts software; 2 = two; 1 = one; 0 = none.

### Synthesis

Small firms need the same habits as a SOC: know what matters, watch a few good signals and agree who acts.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Spotting the signs

### Learning outcomes

You will (1) read sign-in records for unusual country and time; (2) find mailbox forwarding rules; (3) connect signals into a story; (4) avoid jumping to conclusions.

### 2.1 Sign-in records

The email service records each sign-in with user, time and approximate country. NIST SP 800-92 (Kent and Souppaya, 2006) explains why such logs must be kept and checked; Leo asks BrightPath to keep 90 days.

Ninety days matters here. Elaine entered her password on the fake page on Thursday, and the client phoned on Monday, so the records needed went back only a few days. In many cases a stolen password is used weeks later, and if BrightPath kept only a week of sign-ins, the first criminal sign-in could already be gone by the time anyone looked.

### Lab — unusual sign-ins

```python
"""Flag synthetic mailbox sign-ins from unusual countries or at unusual hours."""
usual = {"UK"}
signins = [("e.finch", "Fri 08:52", "UK"), ("e.finch", "Fri 13:05", "UK"), ("e.finch", "Fri 23:47", "BR"),
           ("s.marlow", "Fri 09:10", "UK"), ("l.barros", "Fri 08:30", "UK"), ("e.finch", "Sat 00:02", "BR")]
for user, when, country in signins:
    hour = int(when.split()[1][:2])
    flags = [f for f, bad in (("new country", country not in usual), ("night", hour < 6 or hour >= 22)) if bad]
    print(f"{user:9} {when} {country} {'CHECK: ' + ', '.join(flags) if flags else 'ok'}")
```

Run with `python3 lab_signins.py`. Verified output:

```text
e.finch   Fri 08:52 UK ok
e.finch   Fri 13:05 UK ok
e.finch   Fri 23:47 BR CHECK: new country, night
s.marlow  Fri 09:10 UK ok
l.barros  Fri 08:30 UK ok
e.finch   Sat 00:02 BR CHECK: new country, night
```

### 2.2 Lab result

Two of Elaine's sign-ins are flagged: Friday 23:47 and Saturday 00:02, both from Brazil (BR) and both at night. Her daytime sign-ins from the UK, and other staff's, are normal.

The lab flags each sign-in for two separate reasons, a country not on the usual list and a time between 22:00 and 06:00, and prints both when both apply. Both of Elaine's Brazil sign-ins carry both flags, which makes them stronger leads than a sign-in with only one. Elaine's Friday 08:52 and 13:05 sign-ins from the UK show her own normal pattern.

### 2.3 Forwarding rules

BrightPath checks Elaine's mailbox: at 23:51 on Friday a rule was created that forwards any email containing "invoice" or "payment" to an outside address and deletes the copy. This hid the fraud from Elaine.

The rule explains the timeline: the criminal signed in from Brazil at 23:47 and set up the rule four minutes later. Forwarding then deleting means Elaine never saw clients' replies about the new bank account. That is why no one at the firm noticed, and why the fraud came to light only when a client phoned.

### 2.4 The story

Thursday: Elaine entered her password on a fake "document shared with you" page. Friday night: a criminal signed in, created the rule and sent the fake invoice to two clients. MFA was not enabled on her account.

Each step has evidence. The fake page appears in Elaine's browser history. The two Brazil sign-ins appear in the sign-in records. The 23:51 forwarding rule appears in her mailbox settings. The two fake invoices appear in her sent items. Because each step has its own source, Leo can tell the partners what happened without guessing, and BrightPath knows what to undo.

### 2.5 Not jumping to conclusions

A new country can be travel; Leo checks Elaine was at home. Night sign-ins can be a phone syncing; the country rules this out.

Here both checks point the same way. Elaine was at home in the UK that weekend, so the Brazil sign-ins were not her travelling; and a phone syncing at night would sign in from the UK, not from Brazil. With travel and syncing ruled out, the two sign-ins become strong evidence that someone else used her password.

### 2.6 ATT&CK

MITRE ATT&CK (Strom et al., 2018) lists email forwarding rules as a known collection technique; BrightPath uses this to check for similar rules on other mailboxes.

The ATT&CK entry gives BrightPath a name to search for. It searched all 12 mailboxes for rules forwarding to outside addresses, found that only Elaine's had one, and checked that no other staff member had unusual sign-ins. That is how the firm knows the problem was limited to one account, not just assumed so.
### Worked example

Before relying on Elaine's account of the weekend, Leo phones her rather than emailing, since her mailbox may still be controlled by the criminal. She confirms she was at home in the UK that weekend, the fact 2.5 needs to rule out travel as the reason for the Brazil sign-ins.

> **Synthetic case.** Sign-ins and rules are synthetic.

### Errors and limits

Country information is approximate and can be hidden by services that route traffic.

### Exercises

- **EX014 — Lab flags.** Which sign-ins did the lab flag? *Rubric:* 3 = Elaine Fri 23:47 and Sat 00:02 BR night; 2 = partial; 1 = vague; 0 = none.
- **EX015 — Rule details.** Describe the forwarding rule. *Rubric:* 3 = 23:51; forwards invoice/payment emails outside; deletes copy; 2 = partial; 1 = vague; 0 = none.
- **EX016 — Password theft.** How was the password stolen? *Rubric:* 3 = fake document-shared page Thursday; 2 = partial; 1 = vague; 0 = none.
- **EX017 — Missing protection.** Which protection was missing? *Rubric:* 3 = MFA; 2 = one; 1 = vague; 0 = none.
- **EX018 — Travel check.** Why check whether Elaine travelled? *Rubric:* 3 = new country could be travel; 2 = partial; 1 = vague; 0 = none.
- **EX019 — Phone syncing.** Why might a night sign-in be innocent? *Rubric:* 3 = phone syncing; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Scope check.** Were other mailboxes affected? *Rubric:* 3 = no rules or unusual sign-ins elsewhere; 2 = partial; 1 = vague; 0 = none.
- **EX021 — Log retention.** How long are sign-in logs kept? *Rubric:* 3 = 90 days; 2 = one; 1 = vague; 0 = none.
- **EX022 — Hiding effect.** Why did the rule delete copies? *Rubric:* 3 = to hide replies from Elaine; 2 = partial; 1 = vague; 0 = none.
- **EX023 — Clients targeted.** How many clients got the fake invoice? *Rubric:* 3 = two; 2 = one; 1 = vague; 0 = none.
- **EX024 — Technique source.** Which framework lists forwarding rules as a technique? *Rubric:* 3 = MITRE ATT&CK; 2 = one; 1 = vague; 0 = none.
- **EX025 — Country limits.** Give one limit of country data. *Rubric:* 3 = approximate; hidden by routing services; 2 = partial; 1 = vague; 0 = none.
- **EX026 — Night threshold.** What hours count as night in the lab? *Rubric:* 3 = before 06:00 or from 22:00; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Unusual sign-ins plus a hidden forwarding rule told the story; check innocent explanations first.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Acting fast and calmly

### Learning outcomes

You will (1) contain a compromised email account in the right order; (2) warn clients without causing panic; (3) check whether money was lost; (4) record actions and times.

### 3.1 Order of actions

BrightPath's playbook for a compromised mailbox, following the response ideas in NIST SP 800-61r3 (Nelson et al., 2025): sign out all sessions, reset the password, remove the forwarding rule, turn on MFA, then review sent items and rules. Doing the reset before signing out sessions can leave the criminal connected.

Turning on MFA comes after the reset because Elaine must set up the authenticator app on her phone, and that takes a few minutes. The rule is removed before the sent-items review so that no more client replies are forwarded while BrightPath works out which clients received the fake invoice.

### 3.2 Timing

Leo approves at 10:05 on Monday. Sessions are revoked at 10:08, the password reset at 10:09, the rule removed at 10:11 and MFA enabled at 10:20 once Elaine sets up the app on her phone.

Signing out all sessions at 10:08, before the reset at 10:09, follows the playbook's order, so the criminal could not stay connected with an old session. The full sequence took fifteen minutes from approval to MFA. In the eleven minutes between revoking sessions and enabling MFA, the account was protected by the new password only, which is why Elaine set up the app straight away.

### 3.3 Checking the money

Leo calls both clients who received the fake invoice. One had not paid; the other had paid £4,800 that morning. Leo tells that client to call their bank immediately; the bank attempts a recall.

Speed matters more than anything else here: a bank recall works best before the money is moved on. The client who had paid that morning called their bank at once, and the bank later recovered £3,100 of the £4,800. Leo also tells the client who had not paid to ignore the email and use the firm's known bank details.

### 3.4 Warning clients

A short email from the firm's main address to all clients, approved by the partners: "We will never change our bank details by email. If you receive such a request, phone us on our usual number." No technical details, no blame.

The message works because it gives clients a simple rule they can apply without understanding the attack: bank detail changes never come by email, and a phone call to a known number settles any doubt. Leo uses the firm's usual address, not Elaine's, and sends it after the forwarding rule has been removed, so the criminal cannot see or answer replies.

### 3.5 Reporting

The firm reports the fraud to the national fraud reporting service and, since client contact details in Elaine's mailbox may have been viewed, asks its data protection adviser whether the regulator must be told.

The data protection adviser decided the breach had to be reported because client financial details were in the mailbox, and the report was filed within the deadline. Leo's incident log, with the 23:47 sign-in, the 23:51 rule and the times of each fix, made the report quick to write.

### 3.6 Recording

Leo records each action with its time in a simple incident log.

Leo's log for the Monday reads: approval at 10:05, sessions revoked at 10:08, password reset at 10:09, forwarding rule removed at 10:11, MFA on at 10:20, and then each client call with its time. Each line names who did it: Leo or BrightPath. The data protection adviser used the log to write the breach report, and the lessons review used it to see which steps were quick and which were slow. Without it, both would have relied on memory a week later.

### Telling staff

Staff get a short briefing the same day so they know what happened and what to watch for.

### Worked example

The bank recovers £3,100 of the £4,800. The data protection adviser decides the breach must be reported because client financial details were in the mailbox; the report is filed within the deadline. Leo's incident log makes the report quick to write.

> **Synthetic case.** Amounts and times are invented.

### Errors and limits

Recovery of paid money is uncertain; speed is the best help.

### Exercises

- **EX027 — Correct order.** Give the containment order. *Rubric:* 3 = sign out sessions, reset, remove rule, MFA, review; 2 = four; 1 = two; 0 = none.
- **EX028 — Why sessions first.** Why revoke sessions before reset? *Rubric:* 3 = otherwise criminal stays connected; 2 = partial; 1 = vague; 0 = none.
- **EX029 — Containment times.** When were sessions revoked and MFA enabled? *Rubric:* 3 = 10:08 and 10:20; 2 = one; 1 = vague; 0 = none.
- **EX030 — Paying client.** What happened with the client who paid? *Rubric:* 3 = paid £4,800; bank recall; £3,100 recovered; 2 = partial; 1 = vague; 0 = none.
- **EX031 — Client email.** Summarise the client warning. *Rubric:* 3 = never change bank details by email; phone usual number; 2 = partial; 1 = vague; 0 = none.
- **EX032 — No blame.** Why avoid technical detail and blame? *Rubric:* 3 = keeps message clear and calm; 2 = partial; 1 = vague; 0 = none.
- **EX033 — Fraud report.** Where was the fraud reported? *Rubric:* 3 = national fraud reporting service; 2 = partial; 1 = vague; 0 = none.
- **EX034 — Regulator decision.** Why was the regulator told? *Rubric:* 3 = client financial details in mailbox; 2 = partial; 1 = vague; 0 = none.
- **EX035 — Incident log value.** How did the log help? *Rubric:* 3 = made report quick; 2 = partial; 1 = vague; 0 = none.
- **EX036 — Approval time.** When did Leo approve action? *Rubric:* 3 = 10:05 Monday; 2 = one; 1 = vague; 0 = none.
- **EX037 — Speed matters.** What helps most with recovering money? *Rubric:* 3 = speed; 2 = one; 1 = vague; 0 = none.
- **EX038 — Review step.** What is reviewed after MFA? *Rubric:* 3 = sent items and rules; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Contain in the right order, chase the money quickly, warn calmly and record everything.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Keeping watch and getting better

### Learning outcomes

You will (1) set up simple ongoing monitoring with a provider; (2) measure whether alerts are useful; (3) run a short lessons review; (4) plan the next month and beyond.

### 4.1 Ongoing alerts

BrightPath turns on alerts in the email service for the four signals from chapter 1 and sends Leo a weekly summary. Shared detection ideas such as SigmaHQ rules inspire the alert choices, though BrightPath uses the email service's built-in alerts.

The alert for new forwarding rules matters most, because it would have caught Elaine's 23:51 rule on Friday night, long before the client's Monday phone call. Built-in alerts suit a firm with no security staff: BrightPath does not have to write or maintain its own rules, only check what the email service sends.

### 4.2 Measuring usefulness

In the first month, there are 11 alerts: 8 for sign-ins abroad (6 were Leo's colleague on holiday in Spain, 2 a partner's phone using a roaming network), 2 MFA changes (new phones), 1 forwarding rule (a staff member forwarding to her own personal email, against policy). None were attacks, but the forwarding rule found a policy issue.

Every alert was checked against a simple question, "is there an innocent explanation we can confirm?", and the answer took minutes: a holiday in Spain, a roaming phone, two new phones. The forwarding rule shows the value of the signal even without an attack: a staff member was sending firm email, possibly including client data, to a personal account.

### 4.3 Reducing noise

Staff tell Leo before travelling; BrightPath adds the trip to a list so alerts are checked quickly. Axelsson (2000) explains why rare attacks make most alerts false; the aim is quick checks, not zero alerts.

In the first month, 8 of the 11 alerts were sign-ins abroad and all had innocent explanations. With the travel list, a sign-in from Spain during a colleague's known holiday can be checked in a minute. The forwarding-rule and MFA alerts stay unchanged, because they are rare and each one needs a look.

### 4.4 Lessons review

A 30-minute meeting asks what happened, what worked and what to change. Actions: MFA for all staff (done), phone-check rule for bank detail changes (done), staff phishing training (booked), and a twice-yearly check of who has admin rights.

Each action ties to a gap the incident exposed. MFA for all staff, because Elaine's account had none. A phone-check rule, because a client paid £4,800 on the strength of an email alone. Phishing training, because Elaine entered her password on a fake page. The admin-rights check, because a mailbox with admin rights could have done far more harm.

### 4.5 Continuous monitoring

NIST SP 800-137 (Dempsey et al., 2011) describes monitoring as continuous, feeding decisions over time. For Leo this means the weekly summary, the monthly partner review and yearly checks of the plan.

Each of the three timescales has a job. The weekly summary shows Leo the alerts and how each was explained. The monthly review lets the partners see trends, such as the report button being used more. The yearly check asks whether the four signals and the call list still fit the firm, for example after new staff or a change of IT provider.

### 4.6 Next steps

Leo plans to learn more about incident response and resilience.

Each topic builds on this month's work. Incident response would turn BrightPath's mailbox playbook into a short set of playbooks for other events, such as a lost laptop or a ransomware note. Resilience starts from the firm's backups, the one part of the plan that existed before Elaine's incident, and asks whether the accounts software and client files could be restored quickly after an attack. Leo would test that by restoring one client folder.

### Worked example

Two months later, a staff member reports a fake "invoice overdue" email. BrightPath confirms no one entered a password; the sender is blocked. The report button is used three more times that month. Leo counts this as success: people are watching too.

> **Synthetic case.** Alerts and reports are invented.

### Errors and limits

A small firm relies heavily on its provider; check the provider's work through the weekly summaries.

### Exercises

- **EX039 — Alert count.** How many alerts in the first month and how many attacks? *Rubric:* 3 = 11; none; 2 = one; 1 = vague; 0 = none.
- **EX040 — Sign-in alerts.** Explain the 8 sign-in alerts. *Rubric:* 3 = 6 holiday in Spain; 2 roaming phone; 2 = partial; 1 = vague; 0 = none.
- **EX041 — Policy finding.** What did the forwarding alert find? *Rubric:* 3 = staff forwarding to personal email; policy issue; 2 = partial; 1 = vague; 0 = none.
- **EX042 — Travel list.** How was travel noise reduced? *Rubric:* 3 = staff tell Leo; trip list for BrightPath; 2 = partial; 1 = vague; 0 = none.
- **EX043 — Realistic aim.** What is the aim with alerts? *Rubric:* 3 = quick checks, not zero alerts; 2 = partial; 1 = vague; 0 = none.
- **EX044 — Lessons actions.** List three actions from the lessons review. *Rubric:* 3 = MFA all; phone-check bank changes; training; admin check (three); 2 = two; 1 = one; 0 = none.
- **EX045 — Review length.** How long was the lessons meeting? *Rubric:* 3 = 30 minutes; 2 = one; 1 = vague; 0 = none.
- **EX046 — Continuous meaning.** What does continuous monitoring mean for Leo? *Rubric:* 3 = weekly summary, monthly review, yearly plan check; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Later report.** What happened with the later phishing report? *Rubric:* 3 = no password entered; sender blocked; 2 = partial; 1 = vague; 0 = none.
- **EX048 — Success measure.** Why did Leo count reports as success? *Rubric:* 3 = people watching too; 2 = partial; 1 = vague; 0 = none.
- **EX049 — Provider check.** How does Leo check the provider? *Rubric:* 3 = weekly summaries; 2 = partial; 1 = vague; 0 = none.
- **EX050 — Admin rights.** How often are admin rights checked? *Rubric:* 3 = twice a year; 2 = one; 1 = vague; 0 = none.

### Synthesis

Keep watching a few signals, measure them, learn from each event and keep people involved.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Leo Barros, Elaine Finch, Marlow & Finch, BrightPath IT and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A client received an email from Elaine's account asking for payment into a new bank account, which she had not sent.

**EX002.** The routine of watching for signs of attack, deciding what matters and acting quickly.

**EX003.** Because it is how money is requested, so criminals use it for invoice fraud.

**EX004.** Unusual sign-ins, new forwarding rules, MFA changes and staff reports of odd emails.

**EX005.** BrightPath IT watches and calls; Leo approves resets and blocks.

**EX006.** Yes; he may approve resets and blocks at any hour and inform partners afterwards.

**EX007.** MFA is Protect; backups are Recover.

**EX008.** So everyone reads and uses it.

**EX009.** They will not catch everything, only the most likely problems.

**EX010.** Monthly.

**EX011.** Knowing what you protect and who has authority.

**EX012.** Investigate the fraud email.

**EX013.** Client financial data, email accounts and the accounts software.

**EX014.** Elaine's Friday 23:47 and Saturday 00:02 sign-ins from Brazil at night.

**EX015.** Created at 23:51, it forwarded emails mentioning invoice or payment to an outside address and deleted the copy.

**EX016.** Elaine entered it on a fake "document shared" page on Thursday.

**EX017.** MFA.

**EX018.** A new country could be genuine travel.

**EX019.** A phone syncing mail at night.

**EX020.** No; no other forwarding rules or unusual sign-ins were found.

**EX021.** 90 days.

**EX022.** To hide the fraud and replies from Elaine.

**EX023.** Two.

**EX024.** MITRE ATT&CK.

**EX025.** It is approximate and can be hidden by services that route traffic.

**EX026.** Before 06:00 or from 22:00.

**EX027.** Sign out sessions, reset password, remove rule, enable MFA, then review.

**EX028.** Otherwise the criminal may stay connected.

**EX029.** Sessions at 10:08 and MFA at 10:20.

**EX030.** They had paid £4,800; the bank recalled £3,100.

**EX031.** The firm never changes bank details by email; phone on the usual number if asked.

**EX032.** To keep the message clear and calm.

**EX033.** To the national fraud reporting service.

**EX034.** Because client financial details were in the mailbox.

**EX035.** It made the regulator report quick to write.

**EX036.** 10:05 on Monday.

**EX037.** Speed of contacting the bank.

**EX038.** Sent items and mailbox rules.

**EX039.** Eleven alerts; none were attacks.

**EX040.** Six from a colleague on holiday in Spain and two from a partner's roaming phone.

**EX041.** A staff member forwarding work email to personal email, against policy.

**EX042.** Staff tell Leo before travel and BrightPath keeps a trip list.

**EX043.** Quick checks, not zero alerts.

**EX044.** MFA for all staff, phone checks for bank detail changes and phishing training.

**EX045.** Thirty minutes.

**EX046.** Weekly summaries, monthly partner reviews and yearly plan checks.

**EX047.** Nobody entered a password and the sender was blocked.

**EX048.** Because staff were watching and reporting.

**EX049.** Through the weekly summaries.

**EX050.** Twice a year.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and telemetry in this book are synthetic unless a sentence cites a public source.


- Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. *31st USENIX Security Symposium*, 2783–2800. <https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi>
- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations* (NIST SP 800-137). <https://doi.org/10.6028/NIST.SP.800-137>
- Hassan, W. U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., & Bates, A. (2019). NoDoze: Combatting threat alert fatigue with automated provenance triage. *NDSS Symposium*. <https://doi.org/10.14722/ndss.2019.23349>
- Kaloroumakis, P. E., & Smith, M. J. (2021). *Toward a Knowledge Graph of Cybersecurity Countermeasures* (MITRE D3FEND). The MITRE Corporation. <https://d3fend.mitre.org/resources/D3FEND.pdf>
- Kent, K., & Souppaya, M. (2006). *Guide to Computer Security Log Management* (NIST SP 800-92). <https://doi.org/10.6028/NIST.SP.800-92>
- Knerler, K., Parker, I., & Zimmerman, C. (2022). *11 Strategies of a World-Class Cybersecurity Operations Center* (2nd ed.). The MITRE Corporation. <https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center>
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., & Ahn, G.-J. (2019). Matched and mismatched SOCs: A qualitative study on security operations center issues. *ACM CCS 2019*, 1955–1970. <https://doi.org/10.1145/3319535.3354239>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (NIST SP 800-61 Rev. 3). <https://doi.org/10.6028/NIST.SP.800-61r3>
- SigmaHQ. *Sigma: Generic signature format for SIEM systems* (rule specification and repository). <https://github.com/SigmaHQ/sigma>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018, rev. 2020). *MITRE ATT&CK: Design and Philosophy* (MP180360R1). The MITRE Corporation. <https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf>
- Sundaramurthy, S. C., Case, J., Truong, T., Zomlot, L., & Hoffmann, M. (2014). A tale of three security operation centers. *ACM Workshop on Security Information Workers (SIW '14)*, 43–50. <https://doi.org/10.1145/2663887.2663904>
- van Os, R. (2016). *SOC-CMM: Designing and Evaluating a Tool for Measurement of Capability Maturity in Security Operations Centers* (Master's thesis). Luleå University of Technology. <https://ltu.diva-portal.org/smash/get/diva2:1031560/FULLTEXT02>
- Vielberth, M., Böhm, F., Fichtinger, I., & Pernul, G. (2020). Security operations center: A systematic study and open challenges. *IEEE Access*, 8, 227756–227779. <https://doi.org/10.1109/ACCESS.2020.3045514>
- Zimmerman, C. (2014). *Ten Strategies of a World-Class Cybersecurity Operations Center*. The MITRE Corporation. ISBN 978-0-692-24310-7. <https://www.mitre.org/sites/default/files/publications/pr-13-1028-mitre-10-strategies-cyber-ops-center.pdf>
