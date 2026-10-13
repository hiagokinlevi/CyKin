# Systems, Endpoint and Hardware Security: Technical Course

- Language: English (`en`); course 058, Technical course (18 months).
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical students preparing for IT support roles who need to set up, maintain and support Windows PCs securely in a small office.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only servers, endpoints and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, inventories, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one support student at a fictional accountancy firm from an adware incident through hardware, accounts, updates, protection, safe installation, settings, encryption, backups, networks, remote work, phishing, lifecycle and documentation to a measured placement project. Run each lab where it appears, attempt the four exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Nadia Petrova** | Technical student | Invented |
| **Sam Adeyinka** | Instructor | Invented |
| **Lena Brooks** | Office manager at the partner | Invented |
| **Brookfield Technical Institute** | Fictional institute | Invented |
| **Harlow & Pike** | Fictional accountancy firm (25 staff, 30 PCs) | Invented |

### Core sources

NIST [SP 800-123](https://doi.org/10.6028/NIST.SP.800-123), [SP 800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4), [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128), [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5) and [SP 800-193](https://doi.org/10.6028/NIST.SP.800-193); [CIS Controls v8](https://www.cisecurity.org/controls/v8) and [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); DISA [STIGs](https://public.cyber.mil/stigs/); Microsoft [Windows security baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines); Linux [kernel self-protection](https://www.kernel.org/doc/html/latest/security/self-protection.html). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — The support technician's view of security

### Learning outcomes

You will (1) describe a small office's endpoints; (2) explain the technician's security role; (3) introduce the case.

### 1.1 The case

Nadia Petrova is on an eighteen-month technical programme at the fictional Brookfield Technical Institute, taught by Sam Adeyinka. Her work placement is at the fictional Harlow & Pike, a firm of accountants with twenty-five staff, thirty Windows PCs, a file server and a network storage box for backups. Before she arrived, a staff member installed a free PDF tool using administrator rights, and the PC filled with adverts and slowed down. It was cleaned, but the partners asked how to stop it happening again.

### 1.2 The technician's role

Support technicians set up PCs, install software, reset passwords and fix problems. Every one of those tasks affects security. A PC set up with weak settings stays weak for years; a password reset done without checking identity can hand an account to the wrong person; software installed carelessly can bring unwanted programs. Good support work and good security work are largely the same work done carefully. At Harlow & Pike, Nadia sees this on her first day: staff hold admin rights given years ago for printer drivers, and an adware infection came from a free tool.

### 1.3 What this course covers

The course moves from the parts of a PC and Windows administration to accounts, updates, protection software, encryption, backups and safe support habits. In the final chapters Nadia carries out a small improvement project at Harlow & Pike, measuring local administrator rights and update status before and after her changes. Each chapter gives her a skill she uses at the firm, so by the project she can explain why each change matters, not only how to make it. Sam Adeyinka asks her to keep notes as she goes, because the project report will draw on them.

### 1.4 Working within limits

Nadia works only on systems she is asked to support, with a placement agreement signed by her supervisor at the firm, office manager Lena Brooks. She never uses tools that probe or attack systems. Client financial data are confidential, so she does not open client files, and all examples in this book use synthetic data. These limits protect the firm's clients as well as Nadia. If she needs to do something outside her agreement, such as changing the router, she asks Lena first and records the answer. The IT supplier remains responsible for systems, and Nadia works alongside it.

### Worked example

Nadia lists the office's devices: thirty PCs, one file server, one network storage box, two printers and the internet router. For each she notes who set it up and who looks after it now. The list shows that the router was set up by a previous supplier and nobody has its admin password, which becomes an early task.

> **Synthetic case.** Harlow & Pike, Brookfield Technical Institute and all people and figures are fictional.

### Errors and limits

Treating security as a separate job from support leads to setups that must later be redone.

### Exercises

- **EX001 — Support tasks and security.** Pick two support tasks and explain how each affects security. *Rubric:* 3 = two tasks with clear effects;; 2 = two tasks;; 1 = one;; 0 = none.
- **EX002 — Case trigger.** What event started the placement project and what did it reveal? *Rubric:* 3 = adware install via admin rights, revealing broad admin access;; 2 = adware;; 1 = vague;; 0 = none.
- **EX003 — Placement boundaries.** State two limits on Nadia's work. *Rubric:* 3 = no client files, no probing tools;; 2 = one;; 1 = none;; 0 = none.
- **EX004 — Unknown router password.** Why is the missing router admin password a security concern? *Rubric:* 3 = cannot update or check settings, previous supplier control;; 2 = concern;; 1 = none;; 0 = none.

### Synthesis

Careful everyday support is the foundation of endpoint security in a small office.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — PC hardware and firmware

### Learning outcomes

You will (1) identify PC components; (2) check firmware settings; (3) record hardware details.

### 2.1 Components

A PC contains a processor, memory, a storage drive, network adapters and a motherboard with firmware. Knowing these helps diagnose faults and plan upgrades. For security, the storage drive matters because it holds data that must be protected if the PC is stolen or disposed of, and the firmware matters because it starts everything else. At Harlow & Pike, the drive matters because accountants' laptops carry client financial records, which BitLocker will later protect. Nadia notes each PC's components in the inventory, which also helps when the supplier plans replacements for the oldest models.

### 2.2 UEFI settings

The firmware, usually UEFI, has settings for boot order, Secure Boot and the TPM. Secure Boot checks that the startup software is signed by a trusted publisher. The TPM is a chip that stores keys used by BitLocker. Nadia checks these settings on three PCs using the firmware setup screen and the Windows System Information tool, only looking, not changing. Only looking means she cannot break a PC or lock a user out while learning. The results go into the inventory and tell her which PCs are ready for BitLocker, since the oldest has its TPM disabled.

### 2.3 Firmware passwords

A firmware administrator password stops someone from changing boot settings, for example to start the PC from a USB stick and bypass Windows. Harlow & Pike's PCs have none. Lena agrees that the IT supplier will set one, stored in the password manager. Without a firmware password, anyone with a few minutes alone with a PC could change boot settings and get around Windows protections. Storing the password in the manager means the supplier can still change settings when needed. Nadia records which PCs have the password set and checks the list again after the supplier finishes.

### 2.4 Recording details

Nadia records for each PC: model, serial number, TPM present and enabled, Secure Boot on or off, and firmware version. This takes ten minutes per PC and gives a clear picture of which PCs are ready for encryption. Recording the firmware version also shows which PCs need updates from the manufacturer. Nadia stores the details in the office inventory, so they are available when the supplier enables BitLocker. She repeats the check on the remaining PCs over the following weeks, a few at a time, so office work is not disrupted.

### Firmware updates

PC makers release firmware updates that fix security flaws in the code that runs before Windows starts. Because firmware sits below the operating system, a flaw there can survive a Windows reinstall, which makes these updates more important than their low profile suggests. NIST SP 800-147 describes how firmware updates should be authenticated so that only the maker's signed updates are accepted. The supplier enables firmware updates through Windows Update for supported models, so firmware stays current without visiting each desk. Updates are applied only when the PC is on mains power, since an interrupted firmware update can leave a PC unable to start, and the firmware version is recorded in the inventory.

### Worked example

Of the three PCs checked, two have TPM 2.0 enabled and Secure Boot on; the oldest has the TPM disabled in firmware, noted for the encryption chapter.

> **Synthetic case.** Details are synthetic.

### Errors and limits

Changing firmware settings without a plan can stop a PC starting; Nadia only records them.

### Exercises

- **EX005 — Secure Boot purpose.** What does Secure Boot check? *Rubric:* 3 = signed trusted startup software;; 2 = startup;; 1 = none;; 0 = none.
- **EX006 — Firmware password value.** Explain why a firmware password helps. *Rubric:* 3 = prevents changing boot settings to bypass Windows;; 2 = protection;; 1 = none;; 0 = none.
- **EX007 — Hardware record.** List five details to record per PC. *Rubric:* 3 = all five;; 2 = four;; 1 = fewer;; 0 = none.
- **EX008 — Disabled TPM.** What should happen with a PC whose TPM is disabled? *Rubric:* 3 = plan to enable before encryption, by IT;; 2 = enable;; 1 = ignore;; 0 = none.

### Synthesis

Firmware settings are part of a PC's security and belong in its record.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Windows accounts and rights

### Learning outcomes

You will (1) explain standard and administrator accounts; (2) use separate admin accounts; (3) understand UAC.

### 3.1 Two kinds of account

Windows accounts are either standard users or administrators. Standard users run programs and save their own work. Administrators can install software, change settings and read any file. At Harlow & Pike, staff were given admin rights years ago so they could install printer drivers, and nobody took them away. Admin rights mean any program a staff member runs, including a malicious attachment, can do the same. Nadia's checks later show how widespread the problem is, which shapes her project. She lists each extra administrator account by PC and user, which becomes the starting list for her project.

### 3.2 Separate admin accounts

The IT supplier and Nadia use separate accounts for admin work. Day-to-day email and browsing happen in a standard account, so a malicious email attachment opened by mistake runs without admin rights. This is the principle of least privilege described by Saltzer and Schroeder in 1975. At Harlow & Pike, the supplier's staff had been doing admin work from their everyday accounts. Nadia shows Lena how separate accounts reduce what an attack through email could do, and the supplier agrees to change its practice. Admin accounts are not used for email or browsing.

### 3.3 User Account Control

User Account Control, or UAC, asks for confirmation or credentials before a program gets admin rights. For a standard user, UAC asks for an admin password, which they do not have, so the installation stops. For an administrator, UAC only asks for a click, which people approve without thinking. This is why removing admin rights from staff matters at the firm: with admin rights, UAC becomes a click that people approve without reading, including for software from download sites. As standard users, staff cannot install software by accident.

### Lab — Finding extra administrators

```python
"""List PCs where users other than the IT admin account hold local admin rights (synthetic, stdlib only)."""
pcs = {"PC01": ["itadmin"], "PC02": ["itadmin", "j.hale"], "PC03": ["itadmin"], "PC04": ["itadmin", "r.cole", "temp"],
       "PC05": ["itadmin"], "PC06": ["itadmin", "s.iqbal"], "PC07": ["itadmin"], "PC08": ["itadmin"],
       "PC09": ["itadmin", "m.fry"], "PC10": ["itadmin"]}
extra = {pc: [u for u in us if u != "itadmin"] for pc, us in pcs.items() if len(us) > 1}
for pc, us in extra.items(): print(f"{pc} extra admins: {', '.join(us)}")
print(f"PCs with extra admins: {len(extra)} of {len(pcs)}; extra accounts: {sum(len(v) for v in extra.values())}")
```

Run with `python3 lab_admins.py`. Verified output:

```text
PC02 extra admins: j.hale
PC04 extra admins: r.cole, temp
PC06 extra admins: s.iqbal
PC09 extra admins: m.fry
PCs with extra admins: 4 of 10; extra accounts: 5
```

### 3.4 Reading the result

In a sample of ten PCs, four have extra administrators, five accounts in total, including a leftover account called temp. Each must be checked with the user and removed, with an alternative way to get software they need. Each extra administrator is a decision someone made years ago and never reviewed. The temp account is the most concerning, because nobody knows who uses it. Nadia lists the accounts with the PCs and users, and Lena agrees to remove them once each user has another way to install the software they need.

### Leftover accounts

The temp account found on PC04 was created years ago for a contractor and never removed. Leftover local accounts like this are easy to forget: they do not appear in the directory, nobody signs in with them and their passwords are often weak or shared. Because temp was also an administrator, anyone who knew its password could take full control of the PC. Removing its admin rights is not enough; the account itself is deleted after checking that no files or scheduled tasks depend on it. Nadia adds a check for unexpected local accounts to the quarterly routine, using the same export as the admin rights lab.

### Worked example

Lena approves removing the extra rights; the supplier sets up a self-service software list so staff can install approved tools without admin rights.

> **Synthetic case.** Accounts are synthetic.

### Errors and limits

Removing admin rights without offering an alternative leads to frustration and requests to restore them.

### Exercises

- **EX009 — Daily account choice.** Why should IT staff browse the web from a standard account? *Rubric:* 3 = malicious content runs without admin rights;; 2 = safer;; 1 = none;; 0 = none.
- **EX010 — UAC difference.** How does UAC behave differently for standard users and administrators? *Rubric:* 3 = password required vs click;; 2 = different;; 1 = none;; 0 = none.
- **EX011 — Lab reading.** Summarise the lab result. *Rubric:* 3 = 4 of 10 PCs, 5 accounts, names temp;; 2 = counts;; 1 = wrong;; 0 = none.
- **EX012 — Alternative to admin.** What alternative lets staff install approved tools? *Rubric:* 3 = self-service catalogue;; 2 = IT installs;; 1 = none;; 0 = none.

### Synthesis

Standard accounts for daily work limit the damage of mistakes and malicious files.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Passwords, MFA and password resets

### Learning outcomes

You will (1) explain good password practice; (2) set up multi-factor authentication; (3) reset passwords safely.

### 4.1 Password practice

Long passphrases are easier to remember and harder to guess than short complex passwords. NIST guidance on digital identity recommends checking new passwords against lists of known breached passwords rather than forcing frequent changes. Harlow & Pike sets a minimum of fourteen characters and blocks common and breached passwords. Fourteen characters is long enough to resist guessing but short enough for a passphrase staff can remember. Blocking breached passwords stops staff choosing ones attackers already have. Nadia explains the change at a staff meeting, with examples of good passphrases.

### 4.2 Password manager

Staff use many systems: email, accounting software, tax portals and client portals. A password manager lets them use a different strong password for each. The firm adopts a business password manager with shared vaults for team accounts. Reusing passwords means one breached site could expose the firm's tax portal or client portal. Shared vaults let teams use accounts such as a client portal without sending passwords by email. Nadia helps staff set up the manager and import passwords from their browsers.

### 4.3 Multi-factor authentication

Multi-factor authentication asks for something more than a password, such as approval in an app. Even if a password is phished, the attacker cannot sign in without the second factor. The firm turns it on for email and remote access first. Email comes first because it is the main target of phishing, and remote access because it lets someone reach the file server from outside. The firm plans to extend MFA to the accounting software and portals once staff are used to it. Nadia helps each person set up the app and records who has enrolled.

### 4.4 Safe resets

Password resets are a common route for impersonation. Nadia follows a procedure: confirm identity by calling the staff member back on their known number or in person, then set a temporary password that must be changed at first sign-in. She never resets a password based only on an email request. The callback works because an attacker who sends an email asking for a reset cannot answer the staff member's desk phone. A temporary password that must be changed means even Nadia does not know the final password. Each reset is logged with the date, user and how identity was confirmed.

### Shared mailboxes and lockout

The firm's shared mailbox for client enquiries used to be opened by signing in with a shared password. Now each user opens it through their own account with delegated access, which keeps MFA in place and shows who sent each reply. The shared mailbox's own sign-in is disabled. To slow password guessing, repeated wrong passwords lock an account for fifteen minutes. This is long enough to make guessing slow, but short enough that a staff member who mistypes a few times is not stuck until IT is free. Lockout events appear in the sign-in log, so a pattern of lockouts on one account can be noticed and investigated.

### Worked example

A staff member emails asking for a reset; Nadia calls their desk phone, confirms, and sets a temporary password, logging the request.

> **Synthetic case.** The request is synthetic.

### Errors and limits

Resetting passwords from unverified requests is one of the easiest ways for someone to take over an account.

### Exercises

- **EX013 — Passphrase reasoning.** Why is a long passphrase better than a short complex password? *Rubric:* 3 = harder to guess, easier to remember;; 2 = longer;; 1 = none;; 0 = none.
- **EX014 — MFA protection.** What does MFA protect against when a password is phished? *Rubric:* 3 = attacker lacks second factor;; 2 = protection;; 1 = none;; 0 = none.
- **EX015 — Reset steps.** List the steps of a safe password reset. *Rubric:* 3 = verify by known channel, temporary password, forced change, log;; 2 = three;; 1 = fewer;; 0 = none.
- **EX016 — Shared accounts.** How should a shared team login be stored? *Rubric:* 3 = shared vault with access control;; 2 = password manager;; 1 = spreadsheet;; 0 = none.

### Synthesis

Strong passphrases, a password manager, MFA and careful resets protect accounts together.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Updating Windows and applications

### Learning outcomes

You will (1) configure updates; (2) check update status; (3) handle failed updates.

### 5.1 Windows updates

Microsoft releases security updates monthly. The firm's PCs receive them through Windows Update for Business, managed by the IT supplier. Updates install automatically, with restarts outside working hours and a deadline so that PCs cannot postpone forever. NIST SP 800-40 Rev. 4 describes patching as routine maintenance rather than emergency work. Before the supplier set deadlines, some staff postponed restarts for weeks, leaving their PCs behind. Restarts outside working hours avoid interrupting client work, which matters in tax season. Nadia checks the update status in the supplier's console each week.

### 5.2 Applications

Browsers usually update themselves. Other applications, such as PDF readers and the accounting software, need managing. The supplier deploys these through its management tool so they update centrally. The accounting software matters most, because it holds client data and is used every day. Central updates mean the supplier can roll out a fix to all thirty PCs at once, rather than waiting for each staff member to accept it. Nadia includes these applications when she checks update status, so the figure covers more than Windows alone. She notes which applications cannot update centrally, so they can be checked by hand.

### Lab — Checking update status

```python
"""Summarise days since last successful update per PC against a 14-day target (synthetic, stdlib only)."""
days = [3, 5, 2, 41, 6, 9, 15, 4, 2, 60, 7, 3, 11, 5, 19, 2, 8, 4, 6, 3, 30, 5, 2, 9, 4, 6, 3, 12, 5, 7]
late = [i + 1 for i, d in enumerate(days) if d > 14]
print(f"PCs {len(days)}; within 14 days {len(days)-len(late)}; late {len(late)}: {['PC%02d' % i for i in late]}")
print(f"oldest {max(days)} days")
```

Run with `python3 lab_updates.py`. Verified output:

```text
PCs 30; within 14 days 25; late 5: ['PC04', 'PC07', 'PC10', 'PC15', 'PC21']
oldest 60 days
```

### 5.3 Reading the result

Twenty-five of thirty PCs updated within fourteen days. Five are late, the oldest by sixty days. Nadia checks each: two are rarely used spare PCs, one is a partner's laptop that is often off, one has a full disk and one has a broken update service. Each late PC has a different cause, and each cause needs a different fix. Without checking, Nadia might have assumed the five were careless users. The full disk and broken service are technical problems the supplier can fix, while the spare PCs and the partner's laptop need a change in routine. Nadia records each cause in her notes.

### 5.4 Fixing failures

Spare PCs are switched on weekly to update. The full disk is cleaned. The broken update service is repaired by the supplier using the standard repair steps. The partner's laptop is set to update when it connects. Each fix is checked a week later to confirm it worked. Nadia's ticket for the broken update service records the error, repair steps and result, so the supplier can fix the same problem faster next time. Weekly start-ups for the spares become part of her routine.

### Feature updates and pauses

Besides monthly security updates, Windows receives a larger feature update each year, and each version is supported for a fixed period. Feature updates can affect older applications such as the tax software, so the supplier installs them first on a pilot group and makes sure no PC stays on a version past its support date. During month-end, the busiest time for accountants, the supplier may pause feature updates, but security updates continue. Any pause is recorded in a ticket with an end date, so it cannot be forgotten. An expired pause is one of the commonest reasons small offices drift behind on updates.

### Worked example

A month later, twenty-nine of thirty PCs are within fourteen days.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

A PC reported as late may not be faulty; it may just be switched off. Check before escalating.

### Exercises

- **EX017 — Deadline purpose.** Why set an update restart deadline? *Rubric:* 3 = prevents indefinite postponement;; 2 = forces;; 1 = none;; 0 = none.
- **EX018 — Late PC causes.** Name three reasons a PC might be late on updates. *Rubric:* 3 = three distinct;; 2 = two;; 1 = one;; 0 = none.
- **EX019 — Lab reading.** What does the lab show? *Rubric:* 3 = 25 of 30, five late, oldest 60;; 2 = counts;; 1 = wrong;; 0 = none.
- **EX020 — Spare PCs.** How should spare PCs be kept updated? *Rubric:* 3 = switched on regularly to update;; 2 = update;; 1 = none;; 0 = none.

### Synthesis

Automatic updates with deadlines plus a check for late PCs keep the office current.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Protection software

### Learning outcomes

You will (1) check antivirus status; (2) understand tamper protection; (3) respond to alerts.

### 6.1 Built-in protection

Microsoft Defender Antivirus is built into Windows and is enough for many small offices when kept updated and managed centrally. It scans files, watches behaviour and checks downloads. The firm's supplier manages it from a cloud console showing every PC's status. For a firm of thirty PCs, a built-in, centrally managed product avoids the cost and complexity of another tool. The console lets the supplier see when a PC stops reporting or finds a threat. Nadia's job is to check that every PC actually appears there.

### 6.2 Checking status

Nadia compares the console's list with the PC inventory and finds two PCs missing. One was rebuilt and never enrolled; the other had Defender turned off when a staff member installed a different free antivirus. Both are fixed and the free product removed. Comparing the console with the inventory finds PCs the console cannot show: one that never enrolled, and one whose protection was off. Running two antivirus products together can cause problems, which is another reason to remove the free product. Nadia records both fixes.

### 6.3 Tamper protection

Tamper protection stops users and programs from turning off Defender. The supplier enables it across all PCs. At Harlow & Pike, tamper protection would have stopped Defender being turned off when the free antivirus was installed. It also stops malware disabling protection after it arrives. Nadia confirms in the console that the setting is on for every PC, including the one that was rebuilt and never enrolled, which the supplier has now added. She adds tamper protection to the monthly check list.

### 6.4 Responding to alerts

When Defender blocks something, the alert appears in the console. Most are routine. If an alert says a threat was found but not removed, Nadia disconnects the PC from the network and tells the supplier immediately. Disconnecting first stops a threat spreading to the file server while the supplier investigates. Nadia records each serious alert with what she did and when. Routine alerts, such as a blocked download, are reviewed weekly with the supplier to check for patterns. Lena is phoned about any threat that was found but not removed, because she decides whether client work on that PC must stop.

### Scans, performance and quarantine

Staff sometimes complain that antivirus slows their PC, which is why one turned it off before Nadia arrived. The supplier now schedules full scans for lunchtime and relies on real-time protection the rest of the day. Explaining this to staff removes the reason they turned protection off, which works better than relying only on tamper protection. Nadia also checks that protection updates arrive daily; a PC with old definitions is flagged. Blocked files go to quarantine, where they cannot run. Only the supplier may restore a quarantined file, after confirming it is safe, so a worried staff member cannot release something harmful by accident.

### Worked example

The adware incident would now show as a blocked potentially unwanted application, because the supplier enables that protection setting.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Installing a second antivirus usually causes conflicts and can disable the managed one.

### Exercises

- **EX021 — Coverage check.** How do you find PCs without protection? *Rubric:* 3 = compare console with inventory;; 2 = console;; 1 = none;; 0 = none.
- **EX022 — Second antivirus.** Why avoid installing a second antivirus? *Rubric:* 3 = conflicts, disables managed one;; 2 = conflicts;; 1 = none;; 0 = none.
- **EX023 — Unremoved threat.** What do you do when a threat is not removed? *Rubric:* 3 = disconnect and tell supplier;; 2 = tell supplier;; 1 = ignore;; 0 = none.
- **EX024 — PUA setting.** Which Defender setting would have stopped the adware? *Rubric:* 3 = potentially unwanted application protection;; 2 = a setting;; 1 = none;; 0 = none.

### Synthesis

Managed, tamper-protected antivirus with a checked coverage list is a solid base.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Safe software installation

### Learning outcomes

You will (1) choose trusted sources; (2) verify downloads; (3) record installed software.

### 7.1 Trusted sources

Software should come from the vendor's official site, the Microsoft Store or the supplier's managed catalogue. Free tools from download sites often bundle unwanted programs, which is how the adware arrived. At Harlow & Pike, a staff member downloaded a free PDF tool from a download site, and adware came with it. Using official sources reduces that risk. Nadia explains the change in a short note to staff, with the catalogue as the easy alternative. The supplier removed the adware and the PDF tool it came with, and replaced the tool with the vendor's official reader from the catalogue.

### 7.2 Verifying downloads

Many vendors publish a checksum for each download. Nadia shows staff how the supplier checks a downloaded installer's SHA-256 hash against the vendor's published value before adding it to the catalogue. A matching hash shows the file was not corrupted or replaced. The hash check confirms that the installer is the one the vendor published, not a copy changed on the way. Staff do not need to check hashes themselves, since the supplier does it before adding software to the catalogue. Nadia records the hash with each catalogue entry, so the check can be repeated if needed.

### 7.3 Approving software

New software requests go to Lena, who checks the business need, and to the supplier, who checks the source and licence. Approved software goes into the catalogue. Two checks mean software is both needed and safe to install. Lena knows what work staff do, while the supplier knows where software comes from and whether the firm may use it. Approved software appears in the self-service catalogue, so staff can install it without admin rights. Requests are logged with the decision and date, and a refused request receives a reason and, where possible, an approved alternative.

### 7.4 Recording

The supplier keeps a list of approved software and versions. CIS Controls v8 Control 2 asks organisations to keep a software inventory and allow only authorised software. The list lets the supplier and Nadia spot software that should not be there, such as the free antivirus she found. Each entry records the version, source and who approved it. Nadia compares the list with what is installed on a few PCs each month, and anything unexpected is checked with the user and Lena. The list also helps the supplier know what to update when a vendor releases a fix.

### Browser extensions and unused software

Browser extensions can read every page a user visits, including client portals. The supplier allows only approved extensions, such as the password manager, and other requests follow the normal software process. Nadia explains that free coupon or download extensions often collect browsing data, which matters for a firm handling client finances. Unused software is another quiet risk: every installed program needs updates even if nobody opens it. Nadia lists programs not opened in six months and, with each user's agreement, the supplier removes them. Fewer programs mean fewer updates to track and fewer places for flaws to hide.

### Worked example

A request for a screen-capture tool is approved, the installer's hash is checked against the vendor's page, and it appears in the catalogue the next day.

> **Synthetic case.** Events are synthetic.

### Errors and limits

A hash only helps if it comes from the vendor's official page, not the same download site.

### Exercises

- **EX025 — Bundled software.** Why are third-party download sites risky? *Rubric:* 3 = bundled unwanted programs;; 2 = risky;; 1 = none;; 0 = none.
- **EX026 — Hash check.** What does a matching SHA-256 hash show? *Rubric:* 3 = file unchanged from vendor's;; 2 = integrity;; 1 = none;; 0 = none.
- **EX027 — Approval roles.** Who approves software, and what does each check? *Rubric:* 3 = manager need, supplier source/licence;; 2 = both;; 1 = one;; 0 = none.
- **EX028 — CIS link.** Which CIS Control covers software inventory? *Rubric:* 3 = Control 2 with description;; 2 = 2;; 1 = wrong;; 0 = none.

### Synthesis

Trusted sources, verification and approval keep unwanted software out.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Windows security settings

### Learning outcomes

You will (1) apply key settings; (2) check them; (3) record exceptions.

### 8.1 Key settings

Nadia and the supplier choose ten settings from the CIS Benchmark and Microsoft security baseline: firewall on, screen lock after ten minutes, guest account off, autorun off, SMBv1 off, Defender PUA blocking, macros from the internet blocked, LAPS, remote desktop off and PowerShell logging. Ten settings are enough to make a real difference without overwhelming a small office. Each one closes a common gap: autorun stops programs starting from USB sticks, macro blocking stops a common route for malware in documents, and LAPS gives each PC its own local admin password. Nadia records the reason for each choice and the reference it came from.

### 8.2 Applying

The supplier applies them through its management tool to a pilot group of three PCs for a week. One accountant's old tax tool needs a macro from an internet-downloaded template; the template is saved to a trusted location instead. The pilot finds problems before they reach every PC. A trusted location keeps the macro protection on for everything else while letting the old tax tool work. Nadia records the change with its reason, so the next person who sees the trusted location knows why it exists.

### 8.3 Checking

The management tool reports compliance. Nadia spot-checks two PCs by opening the settings directly. Spot checks confirm that the management tool's report matches the PCs. If a setting appears compliant in the tool but not on the PC, the report cannot be trusted. Nadia records which settings she checked and what she found. Both PCs matched, so the report is used for the monthly compliance figure. She repeats the spot check each quarter on different PCs. The monthly compliance figure and the spot-check notes are filed together, so a later reader can see that the report was checked by hand.

### 8.4 Exceptions

Any PC that cannot take a setting gets a recorded exception with a reason and review date. After rollout, one PC has an exception for remote desktop, used by a partner working from home through the VPN. The exception records the reason, the compensating control that remote desktop works only through the VPN, and a review date. Nadia keeps the exceptions in a short list with the baseline, and Lena approves each one. At each review date Lena either renews the exception with a fresh reason or closes it once the PC can take the setting.

### Explaining settings to staff

Nadia writes a one-page note for staff describing what will change and why: the screen locks after ten minutes, USB sticks do not run anything automatically, and macros in documents from the internet are blocked. Each line has a short reason.

She also explains what to do if something stops working: raise a ticket rather than looking for a way around it. Two tickets arrive in the first week, both resolved within a day.

The note is kept on the shared drive and linked from the knowledge base, so new starters read the same explanation.

### Local admin passwords and reviewing settings

Every Windows PC has a built-in local administrator account. If all thirty share one password, a single leaked password opens every PC. Microsoft's Local Administrator Password Solution, LAPS, gives each PC a unique random password stored in the directory, readable only by the supplier for repairs, and changes it regularly. The ten-setting list itself is also reviewed each year against the latest CIS Benchmark and Microsoft security baseline, because recommendations change as Windows changes. The review is short: compare the list, note any new recommendations that matter for the firm, pilot them and update the one-page staff note.

### Worked example

After rollout, 29 of 30 PCs comply; one has an exception for remote desktop used by a partner working from home through the VPN.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Turning off remote desktop everywhere without asking would have stopped one partner working.

### Exercises

- **EX029 — Setting choice.** Name four of the ten settings. *Rubric:* 3 = four correct;; 2 = three;; 1 = fewer;; 0 = none.
- **EX030 — Macro conflict.** How was the macro conflict solved without weakening the setting? *Rubric:* 3 = trusted location;; 2 = solved;; 1 = none;; 0 = none.
- **EX031 — Exception record.** What does an exception record contain? *Rubric:* 3 = PC, setting, reason, review date;; 2 = three;; 1 = fewer;; 0 = none.
- **EX032 — Spot checks.** Why spot-check settings directly? *Rubric:* 3 = confirm tool reports;; 2 = check;; 1 = none;; 0 = none.

### Synthesis

A short list of important settings, piloted and checked, makes PCs consistently safer.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Disk encryption with BitLocker

### Learning outcomes

You will (1) enable BitLocker; (2) store recovery keys; (3) verify encryption.

### 9.1 Purpose

Accountants carry laptops to clients. If one is stolen, BitLocker makes the drive unreadable without the key. Client financial data are confidential, so encryption is essential. A stolen laptop without encryption would expose client records, and the firm may have to tell clients and the regulator. With BitLocker and a protected key, the data cannot be read, which greatly reduces the harm. Nadia checks that every laptop leaving the office is encrypted. Lena tells the partners before rollout that their laptops will restart once during encryption, so nobody is caught out before a client visit.

### 9.2 Enabling

The supplier enables BitLocker with TPM protection through the management tool, storing recovery keys in the directory. The PC with a disabled TPM from chapter 2 has it enabled first. Using the management tool means every PC is encrypted in the same way, with keys stored centrally rather than on paper. Enabling the TPM first was necessary because BitLocker uses it to protect the key. Nadia checks the oldest PC after the change to confirm it encrypted successfully. Lena is told when encryption finishes on each laptop, so she knows which ones are safe to take to clients.

### 9.3 Verifying

Nadia checks encryption status in the console and with the manage-bde status command on two PCs. All laptops show fully encrypted with protection on. Checking two PCs directly confirms the console report. A drive can show as encrypted while protection is suspended, for example after a firmware update, so Nadia looks for protection on as well as encryption. She records the results with the date in her notes, and repeats the check after the next round of firmware updates. Both direct checks matched the console, so Nadia records the console report as reliable for the monthly figure.

### 9.4 Recovery keys

If BitLocker asks for a recovery key, the user calls IT, who verifies identity before reading out the key. Retrieval is logged. Verifying identity before reading out the key stops someone posing as a staff member from unlocking a stolen laptop. Nadia uses the same callback method as for password resets. Each retrieval is logged with the user, date and reason, and the supplier reviews the log monthly. Recovery keys are only readable by the supplier and Nadia. Staff are told about the callback step in advance, so a request to confirm identity is expected rather than taken as distrust.

### Desktops too

Office desktops are encrypted as well. A break-in could take desktops as easily as laptops, and encryption costs nothing extra on PCs with a TPM. The supplier enables BitLocker on all thirty PCs, not just laptops, in a second wave a week after the laptops.

Nadia also checks USB sticks used to carry client files to meetings. The firm buys encrypted sticks and asks staff to stop using personal ones.

Desktops are verified the same way as laptops, with the encryption status and date recorded in the inventory for each machine.

### Encryption checks over the PC's life

Encryption needs checking at several points, not just once. When a PC goes for repair, BitLocker may be suspended for a firmware update; the supplier resumes protection afterwards and Nadia checks the status the same day. Every new PC's encryption is checked on its first day, before it receives client data, and noted on the joiner checklist. Lena receives a monthly line in the IT report giving the number of PCs encrypted out of thirty. These three checks cover the moments when encryption most often goes wrong: after maintenance, at setup and through slow drift, and together they give the partners steady evidence.

### Worked example

A laptop asks for its recovery key after a firmware update; Nadia verifies the user by callback and reads the key from the directory.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Keys stored on a sticky note in the laptop bag defeat encryption.

### Exercises

- **EX033 — Why laptops first.** Why prioritise laptops for encryption? *Rubric:* 3 = leave office, theft risk;; 2 = travel;; 1 = none;; 0 = none.
- **EX034 — Status command.** Which command shows BitLocker status? *Rubric:* 3 = manage-bde -status;; 2 = manage-bde;; 1 = none;; 0 = none.
- **EX035 — Key request.** How should a recovery key request be handled? *Rubric:* 3 = verify identity, read key, log;; 2 = verify;; 1 = none;; 0 = none.
- **EX036 — Bad storage.** Why is a written key in the laptop bag a problem? *Rubric:* 3 = thief gets both;; 2 = insecure;; 1 = none;; 0 = none.

### Synthesis

Encryption with protected recovery keys keeps client data safe if devices are lost.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Backups

### Learning outcomes

You will (1) explain backup types; (2) check backups; (3) test restores.

### 10.1 What is backed up

The file server holds client files and is backed up nightly to the network storage box, with a weekly copy to cloud storage. PCs store work on the file server, so they need little backing up. The weekly cloud copy protects against a problem that destroys the office, such as fire or theft. Because PCs store work on the file server, rebuilding a failed PC does not lose client files. Nadia confirms with staff that they save work to the server and not to their desktops.

### 10.2 Why separation matters

Ransomware can encrypt anything it can reach, including the backup box if it is mapped as a drive. The supplier sets the box so that backups are written by the backup software only, and the cloud copy keeps older versions that cannot be changed for thirty days. Without these settings, ransomware that reached a staff member's PC could also encrypt the backups, leaving nothing to restore. Thirty days of unchangeable versions gives the firm time to notice an attack and restore from before it began. Nadia checks with the supplier that the settings are in place.

### 10.3 Checking

Each morning, the backup software emails a report. Nadia sets up a rule to flag failures and checks the report weekly with the supplier. A failed backup that nobody notices is the same as no backup. Flagging failures means Nadia sees them the same day. The weekly check with the supplier also looks at backup size and duration, which can show problems before they cause failures. Each failure is recorded with its cause and fix. Nadia keeps the reports for three months, so patterns over time can be seen.

### 10.4 Restore tests

Once a month, she restores one folder to a test location and confirms the files open. CIS Controls v8 Control 11 includes testing recovery. A backup that has never been restored might not work when needed. Opening the files proves they can be read, not only that the job completed. A monthly test once found that a shared folder was missing from the backup job, and the supplier added it. Nadia records each test with the folder, date and result, and chooses a different folder each month.

### Recovery time

Lena asks how long recovery would take. Nadia times a restore of a large client folder: forty minutes from the backup box, three hours from the cloud copy. Lena decides this is acceptable but asks that the most active folders are restored first in any real event.

This conversation turns backup from a technical task into a business decision, which is where it belongs.

The timings are written into the recovery plan, so in a real event everyone knows roughly how long each restore should take and can spot one that is going wrong.

### Retention and the backup box

The firm must keep some records for several years. The supplier sets backup retention to match, keeping monthly copies for seven years in cloud storage, and Lena confirms the period with the firm's compliance adviser rather than guessing. The network storage box that holds the nightly backups is itself a computer with firmware and an admin page. Because it holds every copy of the firm's files, it is an attractive target. Its firmware is updated quarterly, its admin password is unique and stored in the password manager, and its admin page is reachable only from the supplier's management PC.

### Worked example

A monthly test reveals that one shared folder was excluded from the backup job; the supplier adds it.

> **Synthetic case.** Events are synthetic.

### Errors and limits

A backup that has never been restored may not work.

### Exercises

- **EX037 — Ransomware risk.** Why should backups not be mapped as drives on PCs? *Rubric:* 3 = ransomware can reach them;; 2 = risk;; 1 = none;; 0 = none.
- **EX038 — Immutable copy.** What does keeping unchangeable versions for 30 days give? *Rubric:* 3 = recovery after ransomware;; 2 = safety;; 1 = none;; 0 = none.
- **EX039 — Test finding.** What did the monthly restore test reveal? *Rubric:* 3 = excluded folder;; 2 = problem;; 1 = none;; 0 = none.
- **EX040 — Report check.** How are backup failures noticed? *Rubric:* 3 = flagged report email and weekly review;; 2 = email;; 1 = none;; 0 = none.

### Synthesis

Separated backups, checked daily and restored monthly, make recovery possible.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Network basics for technicians

### Learning outcomes

You will (1) check router and Wi-Fi settings; (2) separate guest access; (3) use host firewalls.

### 11.1 The router

The router connects the office to the internet. Its firmware needs updates and its admin password must be known and strong. With the old supplier's help, the admin password is reset, firmware updated and remote management from the internet turned off. Nobody at the firm had the router's admin password, which meant nobody could update it or check its settings. Turning off remote management stops anyone on the internet trying to log in to it. Nadia stores the new password in the password manager and records the firmware version.

### 11.2 Wi-Fi

Staff Wi-Fi uses WPA2 or WPA3 with a strong password. Clients visiting the office use a separate guest network that cannot reach the file server. WPA2 or WPA3 encrypts traffic on the staff network, so visitors cannot read it. The guest network lets clients use the internet without reaching the file server, which holds client files. After the change, Nadia confirms with a guest device that the file server does not appear in its network list. The staff Wi-Fi password is changed when someone leaves.

### 11.3 Host firewalls

Windows Defender Firewall stays on for all profiles, so PCs are protected on hotel or client networks. Accountants work at client offices and hotels, where other devices on the same network could try to connect to their laptops. Keeping the firewall on for every profile means the laptop is protected wherever it is. Nadia checks the setting on a sample of laptops, and it is part of the baseline, so the management tool reports any PC where it is turned off.

### 11.4 Printers

Network printers also have admin pages and firmware; their default passwords are changed. A printer with a default password could be changed by anyone on the network, for example to send copies of scanned documents elsewhere. Nadia checks both printers' admin pages, changes the passwords and stores them in the manager. She also checks for firmware updates and asks the supplier to apply them, and records the printers in the inventory with their firmware versions. Each printer now has a system page listing its model, firmware version and where its admin password is stored.

### Router firmware routine

Router firmware is easy to forget. Nadia adds a quarterly check to the supplier's routine: confirm the router's firmware version against the maker's site and update if needed, during an evening.

She also checks the router's port forwarding list and finds an old rule forwarding a port to a PC that no longer exists. The rule is removed, since an open forward is an unnecessary entry point.

Each check is noted on the router's system page with the version found and any update applied, so the next technician can see the history at a glance.

### DNS filtering and router defaults

The supplier points the office's DNS to a filtering service that blocks known malicious sites. This adds a cheap layer of protection for every device, including printers and phones that cannot run antivirus. On the router, convenience features are turned off unless needed. UPnP, which lets devices open ports through the router automatically, is disabled, because any program on any device could otherwise expose services to the internet without anyone noticing. Wi-Fi Protected Setup is also off. Each disabled feature is noted on the router's system page, so a future technician knows it was a deliberate choice.

### Network inventory

A network can only be checked if its devices are known. Nadia lists every device in the router's client table and matches each to the inventory. Two unknown entries turn out to be staff phones that had joined the office Wi-Fi instead of the guest network; the staff are shown how to switch, and the office Wi-Fi password is changed. She also finds a smart TV in the meeting room on the office network, which is moved to the guest network because it does not need to reach the file server. The comparison becomes a quarterly routine, since unknown devices tend to accumulate quietly.

### Worked example

After the changes, a guest device on the guest network cannot see the file server, which Nadia confirms by checking that the server does not appear in its network list.

> **Synthetic case.** Settings are synthetic.

### Errors and limits

Leaving router remote management open to the internet exposes the office's front door.

### Exercises

- **EX041 — Router actions.** List three router actions taken. *Rubric:* 3 = password, firmware, remote management off;; 2 = two;; 1 = one;; 0 = none.
- **EX042 — Guest network.** Why separate guest Wi-Fi? *Rubric:* 3 = guests cannot reach server;; 2 = separation;; 1 = none;; 0 = none.
- **EX043 — Printer defaults.** Why change printer admin passwords? *Rubric:* 3 = defaults are public;; 2 = security;; 1 = none;; 0 = none.
- **EX044 — Firewall profiles.** Why keep the public firewall profile on? *Rubric:* 3 = protection on untrusted networks;; 2 = safety;; 1 = none;; 0 = none.

### Synthesis

Simple network settings keep guests and outsiders away from office systems.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Remote access and working from home

### Learning outcomes

You will (1) provide secure remote access; (2) protect home working; (3) support remote users.

### 12.1 VPN

Partners reach the file server through the supplier's VPN with MFA. Each user has their own account. MFA on the VPN means a stolen password alone cannot reach the file server. Individual accounts mean each connection can be traced to a person, and a leaver's account can be disabled without affecting anyone else. A partner's slow VPN was traced to an old client version, which Nadia updated. VPN accounts are disabled the same day someone leaves, as part of the leaver steps.

### 12.2 Remote desktop

Remote desktop to office PCs is only available through the VPN, never directly from the internet. Remote desktop exposed directly to the internet is a common target for attackers guessing passwords. Requiring the VPN means only users who have passed MFA can reach it. Nadia confirms with the supplier that no direct access is open on the router. The one exception for a partner working from home uses this route and is recorded with a review date. Because remote desktop off is one of the ten baseline settings, the management tool reports any PC where it has been turned on outside the recorded exception.

### 12.3 Home networks

Staff are asked to keep their home router updated and not to share work laptops with family. Home networks are outside the firm's control, but a work laptop used by family members could pick up unwanted software. The firm cannot check staff routers, so it relies on advice and on the laptop's own protection, including the firewall, Defender and encryption. Nadia gives staff a short guide on updating their home router and keeping work devices for work. Lena sends the home-network guide to staff with a note that the firm will help anyone who is unsure how to update their router.

### 12.4 Remote support

When Nadia helps a remote user, she uses the supplier's remote support tool, which asks the user to accept each session. Asking the user to accept each session means nobody can connect to their laptop without their knowledge. Nadia explains what she is doing during the session and ends it when finished. The tool records each session, so the supplier can see who connected and when. She never asks a user to install a different remote tool, which is a common trick in support scams.

### Supporting remote users safely

Remote users can be impersonated as easily as office users. Before starting a remote session, Nadia confirms the caller by phoning back on their known number. During the session, she explains what she is doing and ends it as soon as the task is complete.

She never asks users for their passwords; if she needs to sign in as an administrator, she uses her own admin account.

Each remote session is recorded in the ticket with its start and end time, so there is a trail of who accessed which PC and why.

### Lost laptops, VPN timeouts and home printing

If a laptop is lost at a client site, the user phones the office. Nadia checks encryption status, signs the user out of all sessions, resets the password and records the event for Lena, who decides whether clients need to be told. The VPN also disconnects after a period of inactivity, so an unattended laptop does not stay connected to the office network. Finally, staff printing client documents at home are asked to collect printouts immediately and shred them when finished. Paper leaks are as real as digital ones, and a remote working guide that ignores printing leaves a gap.

### Worked example

A partner reports slow VPN; Nadia finds their laptop is on an old VPN client version and updates it.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Remote support tools that connect without user approval can be misused.

### Exercises

- **EX045 — RDP exposure.** Why never expose remote desktop directly to the internet? *Rubric:* 3 = attacked constantly;; 2 = risky;; 1 = none;; 0 = none.
- **EX046 — Session consent.** Why should users accept each remote support session? *Rubric:* 3 = prevents unseen access;; 2 = consent;; 1 = none;; 0 = none.
- **EX047 — Family use.** Why not share work laptops with family? *Rubric:* 3 = data exposure and unwanted software;; 2 = risk;; 1 = none;; 0 = none.
- **EX048 — Old VPN client.** Why update the VPN client? *Rubric:* 3 = fixes and performance;; 2 = update;; 1 = none;; 0 = none.

### Synthesis

Individual VPN accounts with MFA and approved support sessions keep remote work safe.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Phishing and the help desk

### Learning outcomes

You will (1) recognise phishing reports; (2) respond to clicks; (3) support staff awareness.

### 13.1 Reports

Staff forward suspicious emails to a report address. Nadia checks headers and links without opening attachments, and the supplier blocks the sender if malicious. Checking headers and links without opening attachments lets Nadia judge a message safely. If it is malicious, the supplier blocks the sender and searches for similar messages in other mailboxes. Nadia thanks the reporter and records the message and outcome, so patterns, such as a wave of fake revenue authority emails, become visible. Lena receives a monthly count of reported messages and how many were malicious, which shows whether the tax-season tips are working.

### 13.2 When someone clicks

If a staff member entered their password on a fake page, Nadia resets the password, checks for new email forwarding rules and confirms MFA was not approved by mistake. Speed matters, because an attacker with the password could read email or set up rules to forward it. In one case, a staff member reported entering their password on a fake page, and within twenty minutes the password was reset and a new forwarding rule found and removed. Nadia records what happened and checks the account again a week later.

### 13.3 Awareness

Short monthly tips cover tax-season phishing, which targets accountants with fake revenue authority messages. Tax season is when accountants expect messages from the revenue authority, so fake ones are more convincing. Monthly tips keep staff alert without overwhelming them. Each tip includes a real-looking example and what to check, such as the sender's address. Nadia writes the tips and Lena sends them. Staff can reply with questions, which help Nadia choose the next tip. Each tip fits in a few lines, because busy accountants in tax season are unlikely to read a long security email.

### 13.4 Blame-free reporting

Staff who report a click quickly get thanks, not blame, so they keep reporting. If staff fear blame, they may hide a click, giving an attacker more time. Thanking people who report quickly encourages others to do the same. Lena states this clearly at a staff meeting. The staff member who reported entering their password on a fake page was thanked, and their quick report meant the attacker's forwarding rule was found and removed within twenty minutes. Nadia's records of reported clicks describe what happened and what was done, without naming the staff member, so reports cannot be used against anyone.

### Checking a reported email

When an email is reported, Nadia looks at the sender's real address, the reply-to address and where links point by hovering over them. Messages that pretend to be from the tax authority but come from unrelated domains are blocked. She records each report briefly, building a picture of what the firm receives.

She never forwards suspicious attachments to colleagues; the supplier handles analysis in its own safe environment.

She replies to every reporter with a short thank-you and the outcome, which teaches staff what to look for next time.

### Payment change requests

Accountants are targeted with emails asking to change a client's bank details. The firm's rule is that any change to payment details is confirmed by phone using a number already on file, never one in the email. Nadia includes this rule in the monthly tip.

This is a process control, not a technical one, and it stops a fraud that no filter can fully catch.

Staff are encouraged to call back even when the request seems to come from a known client, because compromised client mailboxes are common.

### Measuring reports

Monthly counts help Lena see whether awareness is working. Nadia records the number of reported emails, how many were genuinely malicious and how many clicks were reported. More reports with fewer clicks is a good sign; fewer reports might mean less phishing or might mean people have stopped bothering, so the count is read alongside the quality of reports. She avoids naming individuals in the figures, because the aim is to encourage reporting. After three months, reports have doubled and the time from a click to its report has fallen from hours to minutes, which limits damage.

### Worked example

A staff member reports entering their password on a fake login page; within twenty minutes the password is reset and a new forwarding rule found and removed.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Blaming staff discourages reporting, so problems are found later.

### Exercises

- **EX049 — After a click.** List three actions after a password is entered on a fake page. *Rubric:* 3 = reset, check forwarding rules, check MFA;; 2 = two;; 1 = one;; 0 = none.
- **EX050 — Safe inspection.** How should Nadia inspect a reported email safely? *Rubric:* 3 = headers and links, no attachments;; 2 = carefully;; 1 = open;; 0 = none.
- **EX051 — Seasonal risk.** Why mention tax season in awareness tips? *Rubric:* 3 = targeted phishing then;; 2 = relevance;; 1 = none;; 0 = none.
- **EX052 — Blame effect.** Why thank people who report clicks? *Rubric:* 3 = encourages fast reporting;; 2 = nice;; 1 = none;; 0 = none.

### Synthesis

Fast, blame-free reporting limits the damage of phishing.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Device lifecycle

### Learning outcomes

You will (1) set up new PCs consistently; (2) reassign PCs; (3) dispose securely.

### 14.1 New PCs

New PCs are enrolled in the management tool on first start, receiving settings, apps and encryption automatically. Enrolling on first start means a new PC receives the baseline settings, Defender, BitLocker and approved software before anyone uses it. This avoids the old pattern of PCs set up by hand with whatever settings the person chose. Nadia checks each new PC in the console after enrolment and adds it to the inventory with its serial number and user. Lena receives a monthly list of newly enrolled PCs, so she can confirm that each one belongs to a current member of staff.

### 14.2 Reassigning

When a PC moves to a new user, it is reset and re-enrolled rather than just handed over. Handing over a PC without resetting it can leave the previous user's files, saved passwords and permissions on it. Resetting and re-enrolling gives the new user a clean PC with the current baseline. Nadia updates the inventory with the new user's name. The previous user's files are kept on the file server, so nothing is lost. Because settings and software arrive automatically, a reset PC is ready for its new user the same day, with no setup done by hand.

### 14.3 Leavers

A leaver's account is disabled on their last day and their PC is collected. Disabling the account on the last day stops a former employee from reaching email or files afterwards. Collecting the PC ensures client data does not leave with them. Nadia also checks shared vaults in the password manager and changes any passwords the leaver knew, such as for a client portal. Lena tells Nadia about leavers in advance. The supplier confirms each leaver step on a short checklist, and Lena signs it, so a missed account or portal password is noticed straight away.

### 14.4 Disposal

Old drives are wiped using the manufacturer's secure erase or destroyed, with a certificate, following NIST SP 800-88. Old drives can hold client records for years after a PC stops working. Secure erase or destruction makes the data unrecoverable, and the certificate shows auditors what happened to each drive. When two old PCs were disposed of, the recycler's certificate listed their serial numbers, which Nadia matched against the inventory before closing their records. The certificates are filed with the inventory records of the disposed PCs, so an auditor can trace each drive from purchase to destruction.

### Joiner setup

A joiner's PC is prepared before their first day: enrolled, encrypted and updated, with their standard account created. On day one Nadia helps them set up MFA and the password manager. Doing this in person avoids rushed setups that skip steps.

The joiner checklist is a single page and is signed off by Nadia and the new starter.

The checklist also confirms that the joiner has read the short security note and knows how to report a suspicious email, so good habits start on day one rather than after the first mistake.

### Broken, lost and mobile devices

Broken PCs under warranty are sent for repair only after the drive is removed or encryption confirmed, since repair shops handle many devices. Lost devices are reported and recorded as in chapter 12. Phones that read work email are enrolled in app protection: work email and files live inside managed apps that can be wiped without touching personal photos or messages. This lets staff use their own phones while giving the firm control of its data. Before a leaver's account is disabled, their manager confirms which files should move to shared folders, so client work is not lost with the account.

### Inventory updates

Every joiner, move and leaver changes the inventory: who has a PC, its serial number and its status. If these updates are missed, the inventory slowly stops matching reality, and checks based on it give wrong answers. Nadia adds the inventory update to the joiner and leaver checklists so it happens at the same time as the account change. A monthly comparison with the management tool catches anything missed. At the end of the placement, the inventory matches the management tool exactly for all thirty PCs, which Nadia records with the date as evidence.

### Worked example

Two old PCs are disposed of; the recycler's certificate lists their serial numbers.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Handing a PC to a new user without reset leaves the previous user's files and settings.

### Exercises

- **EX053 — Enrolment benefit.** What does automatic enrolment give? *Rubric:* 3 = consistent settings and encryption;; 2 = consistency;; 1 = none;; 0 = none.
- **EX054 — Reassignment.** Why reset a PC before reassigning? *Rubric:* 3 = remove previous data;; 2 = clean;; 1 = none;; 0 = none.
- **EX055 — Disposal proof.** What proves secure disposal? *Rubric:* 3 = certificate with serials;; 2 = certificate;; 1 = none;; 0 = none.
- **EX056 — Leaver timing.** When should a leaver's account be disabled? *Rubric:* 3 = last day;; 2 = soon;; 1 = later;; 0 = none.

### Synthesis

Consistent setup, reset and disposal keep data safe through a device's life.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Documentation and change records

### Learning outcomes

You will (1) document setups; (2) record changes; (3) write useful tickets.

### 15.1 Documentation

Each system has a short page: what it is, how it is set up, who looks after it and where passwords are stored. Short pages mean someone new, such as a different supplier technician, can understand a system quickly. Before Nadia's work, nobody knew who had set up the router or where its password was. Each page is stored in a shared folder that the supplier and Lena can reach. Passwords themselves stay in the password manager, and the page says only where to find them.

### 15.2 Change records

Every change is noted with date, who, what and why. A change record lets someone trace a problem back to the change that caused it. For example, if a setting stops the old tax tool working, the record shows when the setting changed and why. Nadia and the supplier keep records in the same place, using a short template. Changes made in an emergency are recorded afterwards. Lena reviews the change records monthly to see what has changed in the office.

### 15.3 Tickets

Good tickets describe the problem, steps taken and outcome, so others can learn. A ticket that only says "fixed" teaches nothing. Nadia's ticket on the broken update service listed the error, the repair steps and the result, so the next technician facing the same problem can follow it. Good tickets also show patterns, such as repeated problems with one PC. The supplier reviews tickets monthly with Nadia, and recurring problems become tasks. Nadia uses a short template with fields for problem, steps and outcome, and Sam reviews a sample of her tickets to check they would let another technician repeat the fix.

### 15.4 Standards

NIST SP 800-128 links configuration management with documentation and change control. The guidance explains why configuration, documentation and change records belong together: a setting that is not documented cannot be checked, and a change that is not recorded cannot be traced. Nadia uses it to explain to Lena why the firm keeps system pages and change records. The supplier's own processes follow the same ideas, so they fit easily with the firm's records. Nadia cites SP 800-128 in her project report and gives Lena a one-paragraph summary explaining why the firm keeps system pages and change records.

### Where passwords live

System pages record where a password is stored, never the password itself. Router, printer, firmware and storage box passwords are kept in the password manager's IT vault, which only Nadia and the supplier can open, and access is logged. This replaces a paper notebook in Lena's drawer that held every admin password in one place. Once its contents are moved and the passwords changed, the notebook is shredded. Changing the passwords matters, because anyone who had seen the notebook could still know them. The vault also records when each password was last changed, which helps plan rotations.

### Knowledge base and templates

Common fixes become short knowledge base articles: how to reset MFA, reconnect the VPN or request software. Staff can solve simple problems themselves and new technicians learn faster; Nadia writes eight articles, each checked by the supplier. She also creates templates for system pages, tickets and change records, so every entry has the same fields and nothing important is left out. Templates make reviews faster, because reviewers know where to look for each detail, and they make gaps obvious: an empty field in a change record stands out in a way that a missing sentence in free text does not.

### Reviewing documents and changes

Documentation drifts like settings, and out-of-date documentation can mislead someone during an outage, when accuracy matters most. Nadia adds a yearly review date to every system page, and the supplier checks pages after any major change. Changes themselves get a lighter weekly review: each Friday, Nadia and the supplier spend five minutes going through the week's change records together. The aim is to spot anything unexpected, such as a change with no reason recorded, or a change that should have triggered a documentation update. NIST SP 800-128 links configuration management with exactly this kind of change review.

### Worked example

Nadia's ticket on the broken update service lists the error, the repair steps and the result.

> **Synthetic case.** Tickets are synthetic.

### Errors and limits

Undocumented fixes are repeated from scratch next time.

### Exercises

- **EX057 — System page.** What goes on a system page? *Rubric:* 3 = four items;; 2 = three;; 1 = fewer;; 0 = none.
- **EX058 — Ticket quality.** What makes a ticket useful later? *Rubric:* 3 = problem, steps, outcome;; 2 = detail;; 1 = none;; 0 = none.
- **EX059 — Change fields.** List change record fields. *Rubric:* 3 = date, who, what, why;; 2 = three;; 1 = fewer;; 0 = none.
- **EX060 — Standard reference.** Which NIST publication covers configuration change control? *Rubric:* 3 = SP 800-128;; 2 = NIST;; 1 = wrong;; 0 = none.

### Synthesis

Clear documentation saves time and supports security.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Placement project: measuring

### Learning outcomes

You will (1) plan a small project; (2) measure admin rights and updates; (3) record method.

### 16.1 Plan

Nadia's project measures local admin rights and update status across all thirty PCs, then reduces both. These two measures were chosen because they matter for security and can be counted from exports: extra admin rights let malware do more, and late updates leave known flaws open. Measuring all thirty PCs, not just a sample, gives a complete picture. Nadia agrees the plan with Sam and Lena, and the supplier provides the exports. The project runs over several weeks so changes can be made carefully.

### 16.2 Measuring

Using exports and the labs, she finds 12 of 30 PCs with extra admins and 25 of 30 within 14 days of updates. The admin figure is higher than in the earlier sample of ten PCs, which shows why measuring every PC matters. The update figure matches the earlier check. Nadia records both as the starting point for her project. She notes the date of each export and checks a few results by hand to confirm the exports are accurate. Lena receives both starting figures with the export dates, so she can compare them with the results after the changes.

### 16.3 Method

She records the export date and steps so she can repeat them. Recording the steps means she can measure again after the changes using exactly the same method, so the comparison is fair. It also means the supplier can repeat the measurement after she leaves. Her notes include which export was used, which filter and which lab script. Sam checks the notes to see whether someone else could follow them without help. Sam follows the notes himself on one PC to confirm someone else could repeat the measurement, and they later go into the handover.

### 16.4 Agreement

Lena approves the plan and measures. Lena's approval confirms that removing admin rights and fixing update failures are business decisions, not just technical ones. She agrees the two measures and the method, and asks to see results before and after. Nadia records the approval with the date, and Sam receives a copy for the course records. Lena also agrees to announce the change to staff before it begins. Sam also reviews the plan, checking that the measures can be repeated and that the changes stay within her placement agreement.

### Why these two measures

Nadia chose local admin rights and update status because both relate directly to the adware incident and both can be measured from existing exports. Admin rights let staff install software; out-of-date PCs give that software more weaknesses to use. Fixing both addresses the cause of the incident rather than just its symptoms.

She avoided measures needing new tools, so the project fits the placement time.

Each measure also has a clear direction: fewer extra admins and more PCs updated are both unambiguously better, which keeps the report easy to read.

### Validating and timing the measurement

Before relying on exports, Nadia checks three PCs by hand: the local administrators group and update history match the exports, and she records these checks. Two PCs switched off during measurement are counted separately and checked when switched on. Exports are taken at the same time of day on a Tuesday, avoiding Monday, when PCs that were off over the weekend are still catching up; this makes before and after figures comparable. The plan allows one week to measure, four to change and one to re-measure, with a buffer for month-end, when accountants are busiest and changes are paused.

### Baseline table

The baseline table is short on purpose. Each row shows a measure, the count, the total, the date and the export used: 12 of 30 PCs with extra administrators and 25 of 30 updated within fourteen days. Offline PCs are listed underneath rather than counted as passing or failing. Lena can read it in a minute, and Sam can check that each number has a source. Keeping the export file alongside the table means anyone can recompute the figures later, which is what makes a baseline evidence rather than a claim, and it lets the end measurement follow exactly the same steps.

### Worked example

The baseline table has two rows with counts and dates.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Measuring without recording the method makes comparison unreliable.

### Exercises

- **EX061 — Project measures.** What two measures did Nadia use? *Rubric:* 3 = admin rights and update status;; 2 = one;; 1 = none;; 0 = none.
- **EX062 — Baseline values.** State the baseline values. *Rubric:* 3 = 12/30 and 25/30;; 2 = one;; 1 = none;; 0 = none.
- **EX063 — Method record.** Why record export steps? *Rubric:* 3 = repeatability;; 2 = repeat;; 1 = none;; 0 = none.
- **EX064 — Approval.** Who approved the plan? *Rubric:* 3 = Lena;; 2 = manager;; 1 = none;; 0 = none.

### Synthesis

A short measured baseline gives the project a clear starting point.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Placement project: changes and results

### Learning outcomes

You will (1) make changes safely; (2) re-measure; (3) report.

### 17.1 Changes

Extra admin rights are removed after talking to each user, and the self-service catalogue is introduced. Update failures are fixed as in chapter 5. Talking to each user first means nobody loses software they need without warning. The self-service catalogue gives them a way to install approved tools without admin rights. Fixing update failures follows the causes found earlier: spares started weekly, disks cleaned, the broken service repaired and the partner's laptop set to update when it connects. Nadia records each change in the change log.

### 17.2 Results

Extra admins fall from 12 to 0 PCs; updates within 14 days rise from 25 to 29 of 30. Nadia measures again with the same exports and method as before, so the figures can be compared directly. The admin result is complete, since every extra administrator was removed after checking with the user. The update result is close to complete; the one remaining PC is explained. She presents both with the before figures in a simple table, with the export dates. Lena signs the results table, which confirms that the firm accepts the figures as its own record of the change.

### 17.3 Remaining

One PC stays late because it is a partner's laptop often off; a reminder is set. The partner's laptop is often off for days, so it misses update deadlines even with automatic updates set. A reminder asks the partner to leave it connected overnight once a week. Nadia records the laptop as a known gap rather than a failure of the project, and the supplier checks its status each month. If the reminder does not work, the supplier will contact the partner directly.

### 17.4 Staff reaction

Most staff did not notice the change; two asked for software via the catalogue. The quiet reaction suggests the change caused little disruption, which matters for keeping it in place. The two catalogue requests show staff found the new way to get software. Nadia asked a few staff directly whether anything had become harder, and nobody reported a problem. She records the reaction in her report, without names, and notes that it covers only the first weeks. Lena agrees, adding that she had expected complaints about losing admin rights and received none in the first weeks.

### Talking to each user

Before removing admin rights, Nadia speaks to each of the affected staff. She asks what they use admin rights for, checks those tools are in the catalogue and explains the change. Most used rights only for printer drivers, which the supplier now deploys automatically.

One partner asks to keep rights; Lena decides that partners follow the same rule, and the partner is given a separate admin account held by the supplier for rare needs.

These conversations took about fifteen minutes each and avoided every complaint that Lena had expected.

### Checking results honestly

Nadia re-measures with the same exports and steps. She notes that update results can vary month to month, so she will check again next month. She also notes that admin rights could creep back if the supplier grants them for quick fixes, which is why the quarterly check matters.

The report shows both measures with counts, dates and a short explanation of the remaining late PC.

She sends the report to Sam and Lena together, so both readers see the same numbers and caveats.

### Follow-up check and cost

One month after the changes, Nadia repeats both measures with the same exports and steps. Extra admin rights remain at zero and updates at twenty-nine of thirty, which suggests the changes are holding rather than being a one-off result. She also records the effort: about twelve hours of her time and four of the supplier's. Recording cost matters for a small firm, because partners decide whether to continue a practice by comparing effort with benefit. Here the effort was modest, and the ongoing quarterly check takes under an hour, which makes the case for continuing it straightforward.

### Worked example

The report table shows before and after values.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Removing rights before the catalogue was ready would have caused complaints.

### Exercises

- **EX065 — Results.** State both results. *Rubric:* 3 = 12→0 and 25→29;; 2 = one;; 1 = none;; 0 = none.
- **EX066 — Ordering.** Why set up the catalogue first? *Rubric:* 3 = alternative before removal;; 2 = smoother;; 1 = none;; 0 = none.
- **EX067 — Remaining PC.** How is the remaining late PC handled? *Rubric:* 3 = reminder;; 2 = followed;; 1 = ignored;; 0 = none.
- **EX068 — Reaction.** What did staff reaction suggest? *Rubric:* 3 = low disruption;; 2 = fine;; 1 = none;; 0 = none.

### Synthesis

Small careful changes produced clear measured improvements.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Reflection and next steps

### Learning outcomes

You will (1) reflect on learning; (2) recommend next steps; (3) hand over.

### 18.1 Reflection

Nadia learned that security work is mostly careful support. Checking identity before a reset, reading a backup report, comparing the inventory with the console, testing a restore: each is an ordinary support task done with care. Nadia writes that most of the improvements at Harlow & Pike came from such tasks rather than from new tools. She also notes what she found hardest: explaining changes to staff without technical words. Sam asks her to keep that reflection for her next placement.

### 18.2 Recommendations

Quarterly admin and update checks, MFA for all systems, and router firmware checks. Each recommendation keeps an improvement from slipping back. Quarterly checks catch new admin rights or late updates before they become normal again. Extending MFA to the accounting software and portals closes remaining gaps. Router firmware checks stop the router being forgotten again. Nadia writes each recommendation with an owner and frequency, and Lena agrees them. The supplier adds the quarterly checks to its contract. Each recommendation includes an estimate of the supplier's time, so Lena can see what keeping the improvements in place will cost.

### 18.3 Handover

Scripts and notes are handed to the supplier. The handover includes the export steps, lab scripts, inventory, exceptions list and system pages, so the supplier can repeat Nadia's measurements and keep records current. She walks through them with the supplier's technician and answers questions. Lena receives a copy, and the notes are stored in the shared folder with the system pages. The supplier confirms it can run the scripts, and Nadia stays available for questions by email during the first quarterly check.

### 18.4 Assessment

Sam assesses the report and Lena's feedback. Sam looks at whether the report explains what was measured, what changed and why, with evidence. Lena's feedback describes Nadia's work from the firm's view: whether changes were explained well and whether staff were disrupted. Together they give a picture of both technical and professional skills. Nadia receives written comments from both, which she uses for her next placement. Sam marks the report as meeting the course outcomes and suggests she practise writing shorter executive summaries.

### What worked and what the firm said

Three things worked well: measuring before changing, talking to staff before removing rights and fixing update failures by cause rather than one by one. Each made changes smoother and results clearer. What worked less well was timing; month-end slowed progress, and Nadia would plan around it from the start. Lena's feedback notes fewer support calls about slow PCs and no new unwanted software since the changes, and she asks the institute for another placement student next year. Nadia thanks Lena, the supplier and the staff, whose cooperation made every change possible.

### Skills gained and next steps

Nadia lists the skills she practised: reading firmware settings, managing accounts and rights, checking updates, verifying encryption, testing restores, handling phishing reports and writing documentation. Sam notes that these map directly to entry-level support roles. She also reflects on soft skills: explaining changes simply, listening to concerns and asking before acting. She plans to study Linux administration next and read the CIS Controls v8 implementation group 1 guide in full. For next year's student she leaves a short note: read the system pages first, ask Lena before changing anything visible and avoid month-end for changes.

Sam asks her to keep a short learning log during her first job, recording each new problem and how it was solved, since that habit is what turns experience into skill.

### Worked example

The supplier adds the quarterly checks to its contract.

> **Synthetic case.** The case is synthetic.

### Errors and limits

Without a handover, checks stop when the student leaves.

### Exercises

- **EX069 — Lesson.** State Nadia's main lesson. *Rubric:* 3 = support equals security, explained;; 2 = stated;; 1 = none;; 0 = none.
- **EX070 — Recommendation.** Give one recommendation with reason. *Rubric:* 3 = justified;; 2 = unjustified;; 1 = none;; 0 = none.
- **EX071 — Handover target.** Who receives the handover? *Rubric:* 3 = supplier;; 2 = IT;; 1 = none;; 0 = none.
- **EX072 — Contract.** Why put checks in the supplier contract? *Rubric:* 3 = ensures they happen;; 2 = formal;; 1 = none;; 0 = none.

### Synthesis

The placement leaves routines that keep the office safer.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Nadia Petrova, Sam Adeyinka, Lena Brooks, Brookfield Technical Institute, Harlow & Pike and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** PC setup decides baseline settings; password resets can give an account to the wrong person if identity is not checked.

**EX002.** A staff member installed a free tool with admin rights and got adware, revealing that users could install anything.

**EX003.** She does not open client files, and she does not use tools that probe or attack systems.

**EX004.** Nobody can update or review the router, and a former supplier may still have access.

**EX005.** That each piece of startup software is signed by a trusted publisher.

**EX006.** It stops someone changing boot order to start another system and bypass Windows protections.

**EX007.** Model, serial number, TPM state, Secure Boot state and firmware version.

**EX008.** Record it and plan for IT to enable it in firmware before turning on BitLocker.

**EX009.** Anything malicious opened by mistake runs without admin rights and can do less damage.

**EX010.** Standard users must enter an admin password; administrators only click to confirm.

**EX011.** Four of ten PCs have extra admins, five accounts in total, including a leftover temp account.

**EX012.** A self-service list of approved software that installs without admin rights.

**EX013.** Length makes it harder to guess while staying memorable.

**EX014.** The attacker still cannot sign in without the second factor.

**EX015.** Verify identity by a known channel, set a temporary password, force change at sign-in, log the request.

**EX016.** In a shared vault in the business password manager with access limited to the team.

**EX017.** Without a deadline, users can postpone restarts and updates never complete.

**EX018.** Switched off, full disk, broken update service.

**EX019.** 25 of 30 within 14 days; five late (PC04, PC07, PC10, PC15, PC21); oldest 60 days.

**EX020.** Switch them on weekly so they install updates before being given to anyone.

**EX021.** Compare the console's device list with the PC inventory.

**EX022.** It can conflict and switch off the centrally managed protection.

**EX023.** Disconnect the PC from the network and contact the supplier straight away.

**EX024.** Potentially unwanted application blocking.

**EX025.** They often bundle adware or other unwanted programs with the tool.

**EX026.** The file matches what the vendor published and was not corrupted or replaced.

**EX027.** Lena checks business need; the supplier checks source and licence.

**EX028.** Control 2, inventory and control of software assets.

**EX029.** Firewall on, screen lock, autorun off, SMBv1 off.

**EX030.** The template was saved to a trusted location so the block on internet macros stayed.

**EX031.** PC, setting, reason and review date.

**EX032.** To confirm the management tool's reports match the PCs.

**EX033.** They travel to clients and are more likely to be lost or stolen.

**EX034.** manage-bde -status.

**EX035.** Verify the caller by a known channel, read the key and log the retrieval.

**EX036.** A thief who takes the bag gets both the laptop and its key.

**EX037.** Ransomware on a PC could encrypt the backups too.

**EX038.** Clean copies remain even if newer files are encrypted.

**EX039.** One shared folder was missing from the backup job.

**EX040.** A rule flags failure reports, and Nadia reviews them weekly.

**EX041.** Reset admin password, update firmware, turn off internet remote management.

**EX042.** So visitors' devices cannot reach the file server.

**EX043.** Default passwords are published and anyone could change printer settings.

**EX044.** It protects laptops on hotel and client networks.

**EX045.** It is constantly targeted by password guessing and known flaws.

**EX046.** So nobody can connect to their PC without their knowledge.

**EX047.** Family members could install unwanted software or see client data.

**EX048.** Old clients miss security fixes and can perform poorly.

**EX049.** Reset the password, check for new forwarding rules, review MFA approvals.

**EX050.** Look at headers and link targets without opening attachments.

**EX051.** Phishing pretending to be the tax authority rises then.

**EX052.** Quick reports limit damage, and thanks keep people reporting.

**EX053.** Every new PC gets the same settings, apps and encryption.

**EX054.** To remove the previous user's files and settings.

**EX055.** A certificate listing serial numbers.

**EX056.** On their last working day.

**EX057.** What it is, setup, owner and password location.

**EX058.** It records the problem, steps taken and outcome.

**EX059.** Date, who, what and why.

**EX060.** SP 800-128.

**EX061.** PCs with extra admins and PCs updated within 14 days.

**EX062.** 12 of 30 with extra admins; 25 of 30 updated within 14 days.

**EX063.** So the end measurement uses identical steps.

**EX064.** Lena Brooks, the office manager.

**EX065.** Extra admins 12 to 0; updates 25 to 29 of 30.

**EX066.** Staff had a way to get software before losing admin rights.

**EX067.** A reminder prompts the partner to connect the laptop for updates.

**EX068.** The change caused little disruption.

**EX069.** Careful everyday support work is most of endpoint security.

**EX070.** Quarterly admin checks, because rights tend to creep back.

**EX071.** The IT supplier.

**EX072.** It makes the checks a contracted duty, so they continue.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Center for Internet Security. (n.d.). *CIS Benchmarks*. <https://www.cisecurity.org/cis-benchmarks>
- Center for Internet Security. (2021). *CIS Critical Security Controls v8*. <https://www.cisecurity.org/controls/v8>
- Cooper, D., Polk, W., Regenscheid, A., & Souppaya, M. (2011). *BIOS protection guidelines* (NIST SP 800-147). NIST. <https://doi.org/10.6028/NIST.SP.800-147>
- Defense Information Systems Agency. (n.d.). *Security Technical Implementation Guides (STIGs)*. <https://public.cyber.mil/stigs/>
- Dietrich, C., Krombholz, K., Borgolte, K., & Fiebig, T. (2018). Investigating system operators' perspective on security misconfigurations. *2018 ACM SIGSAC Conference on Computer and Communications Security (CCS '18)*, 1272–1289. <https://doi.org/10.1145/3243734.3243794>
- Forrest, S., Hofmeyr, S. A., Somayaji, A., & Longstaff, T. A. (1996). A sense of self for Unix processes. *1996 IEEE Symposium on Security and Privacy*, 120–128. <https://doi.org/10.1109/SECPRI.1996.502675>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Johnson, A., Dempsey, K., Ross, R., Gupta, S., & Bailey, D. (2011, updated 2019). *Guide for security-focused configuration management of information systems* (NIST SP 800-128). NIST. <https://doi.org/10.6028/NIST.SP.800-128>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Kent, K., & Souppaya, M. (2006). *Guide to computer security log management* (NIST SP 800-92). NIST. <https://doi.org/10.6028/NIST.SP.800-92>
- Kernel development community. (n.d.). *Kernel self-protection*. <https://www.kernel.org/doc/html/latest/security/self-protection.html>
- Kim, Y., Daly, R., Kim, J., Fallin, C., Lee, J. H., Lee, D., Wilkerson, C., Lai, K., & Mutlu, O. (2014). Flipping bits in memory without accessing them: An experimental study of DRAM disturbance errors. *41st International Symposium on Computer Architecture (ISCA)*, 361–372. <https://doi.org/10.1109/ISCA.2014.6853210>
- Kocher, P., Horn, J., Fogh, A., Genkin, D., Gruss, D., Haas, W., Hamburg, M., Lipp, M., Mangard, S., Prescher, T., Schwarz, M., & Yarom, Y. (2019). Spectre attacks: Exploiting speculative execution. *2019 IEEE Symposium on Security and Privacy*, 1–19. <https://doi.org/10.1109/SP.2019.00002>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Li, F., & Paxson, V. (2017). A large-scale empirical study of security patches. *2017 ACM SIGSAC Conference on Computer and Communications Security (CCS '17)*, 2201–2215. <https://doi.org/10.1145/3133956.3134072>
- Microsoft. (n.d.). *Windows security baselines*. <https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines>
- Microsoft. (n.d.). *BitLocker overview*. <https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/>
- Microsoft. (n.d.). *Application Control for Windows*. <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol>
- Nappa, A., Johnson, R., Bilge, L., Caballero, J., & Dumitraș, T. (2015). The attack of the clones: A study of the impact of shared code on vulnerability patching. *2015 IEEE Symposium on Security and Privacy*, 692–708. <https://doi.org/10.1109/SP.2015.48>
- Regenscheid, A. (2018). *Platform firmware resiliency guidelines* (NIST SP 800-193). NIST. <https://doi.org/10.6028/NIST.SP.800-193>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Scarfone, K., Jansen, W., & Tracy, M. (2008). *Guide to general server security* (NIST SP 800-123). NIST. <https://doi.org/10.6028/NIST.SP.800-123>
- Souppaya, M., & Scarfone, K. (2013). *Guide to malware incident prevention and handling for desktops and laptops* (NIST SP 800-83 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-83r1>
- Souppaya, M., & Scarfone, K. (2022). *Guide to enterprise patch management planning: Preventive maintenance for technology* (NIST SP 800-40 Rev. 4). NIST. <https://doi.org/10.6028/NIST.SP.800-40r4>
