# Systems, Endpoint and Hardware Security: Technical Course

- Language: English (`en`); course 058, Technical course (18 months).
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; Two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
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

Support technicians set up PCs, install software, reset passwords and fix problems. Every one of those tasks affects security. A PC set up with weak settings stays weak for years; a password reset done without checking identity can hand an account to the wrong person; software installed carelessly can bring unwanted programs. Good support work and good security work are largely the same work done carefully.

### 1.3 What this course covers

The course moves from the parts of a PC and Windows administration to accounts, updates, protection software, encryption, backups and safe support habits. In the final chapters Nadia carries out a small improvement project at Harlow & Pike, measuring local administrator rights and update status before and after her changes.

### 1.4 Working within limits

Nadia works only on systems she is asked to support, with a placement agreement signed by her supervisor at the firm, office manager Lena Brooks. She never uses tools that probe or attack systems. Client financial data are confidential, so she does not open client files, and all examples in this book use synthetic data.

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

A PC contains a processor, memory, a storage drive, network adapters and a motherboard with firmware. Knowing these helps diagnose faults and plan upgrades. For security, the storage drive matters because it holds data that must be protected if the PC is stolen or disposed of, and the firmware matters because it starts everything else.

### 2.2 UEFI settings

The firmware, usually UEFI, has settings for boot order, Secure Boot and the TPM. Secure Boot checks that the startup software is signed by a trusted publisher. The TPM is a chip that stores keys used by BitLocker. Nadia checks these settings on three PCs using the firmware setup screen and the Windows System Information tool, only looking, not changing.

### 2.3 Firmware passwords

A firmware administrator password stops someone from changing boot settings, for example to start the PC from a USB stick and bypass Windows. Harlow & Pike's PCs have none. Lena agrees that the IT supplier will set one, stored in the password manager.

### 2.4 Recording details

Nadia records for each PC: model, serial number, TPM present and enabled, Secure Boot on or off, and firmware version. This takes ten minutes per PC and gives a clear picture of which PCs are ready for encryption.

### Firmware updates

PC makers release firmware updates that fix security flaws. The supplier enables firmware updates through Windows Update for supported models, so firmware stays current without visiting each desk.

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

Windows accounts are either standard users or administrators. Standard users run programs and save their own work. Administrators can install software, change settings and read any file. At Harlow & Pike, staff were given admin rights years ago so they could install printer drivers, and nobody took them away.

### 3.2 Separate admin accounts

The IT supplier and Nadia use separate accounts for admin work. Day-to-day email and browsing happen in a standard account, so a malicious email attachment opened by mistake runs without admin rights. This is the principle of least privilege described by Saltzer and Schroeder in 1975.

### 3.3 User Account Control

User Account Control, or UAC, asks for confirmation or credentials before a program gets admin rights. For a standard user, UAC asks for an admin password, which they do not have, so the installation stops. For an administrator, UAC only asks for a click, which people approve without thinking.

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

In a sample of ten PCs, four have extra administrators, five accounts in total, including a leftover account called temp. Each must be checked with the user and removed, with an alternative way to get software they need.

### Leftover accounts

The temp account found on PC04 was created years ago for a contractor. Leftover local accounts like this are easy to forget and may have weak passwords, so they are removed rather than just stripped of rights.

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

Long passphrases are easier to remember and harder to guess than short complex passwords. NIST guidance on digital identity recommends checking new passwords against lists of known breached passwords rather than forcing frequent changes. Harlow & Pike sets a minimum of fourteen characters and blocks common and breached passwords.

### 4.2 Password manager

Staff use many systems: email, accounting software, tax portals and client portals. A password manager lets them use a different strong password for each. The firm adopts a business password manager with shared vaults for team accounts.

### 4.3 Multi-factor authentication

Multi-factor authentication asks for something more than a password, such as approval in an app. Even if a password is phished, the attacker cannot sign in without the second factor. The firm turns it on for email and remote access first.

### 4.4 Safe resets

Password resets are a common route for impersonation. Nadia follows a procedure: confirm identity by calling the staff member back on their known number or in person, then set a temporary password that must be changed at first sign-in. She never resets a password based only on an email request.

### Shared mailboxes

The firm's shared mailbox for client enquiries is opened through each user's own account with delegated access, not by signing in with a shared password. This keeps MFA in place and shows who did what.

### Account lockout

Repeated wrong passwords lock the account for fifteen minutes, slowing guessing without locking staff out for long.

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

Microsoft releases security updates monthly. The firm's PCs receive them through Windows Update for Business, managed by the IT supplier. Updates install automatically, with restarts outside working hours and a deadline so that PCs cannot postpone forever. NIST SP 800-40 Rev. 4 describes patching as routine maintenance rather than emergency work.

### 5.2 Applications

Browsers usually update themselves. Other applications, such as PDF readers and the accounting software, need managing. The supplier deploys these through its management tool so they update centrally.

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

Twenty-five of thirty PCs updated within fourteen days. Five are late, the oldest by sixty days. Nadia checks each: two are rarely used spare PCs, one is a partner's laptop that is often off, one has a full disk and one has a broken update service.

### 5.4 Fixing failures

Spare PCs are switched on weekly to update. The full disk is cleaned. The broken update service is repaired by the supplier using the standard repair steps. The partner's laptop is set to update when it connects.

### Feature updates

Besides monthly security updates, Windows receives a larger feature update each year. Each version is supported for a fixed period. The supplier plans feature updates with a pilot group first, because they can affect older applications, and makes sure no PC stays on a version past its support date.

### Pausing updates

During month-end, the supplier may pause feature updates, but security updates continue. Any pause has an end date recorded in the ticket, so it cannot be forgotten.

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

Microsoft Defender Antivirus is built into Windows and is enough for many small offices when kept updated and managed centrally. It scans files, watches behaviour and checks downloads. The firm's supplier manages it from a cloud console showing every PC's status.

### 6.2 Checking status

Nadia compares the console's list with the PC inventory and finds two PCs missing. One was rebuilt and never enrolled; the other had Defender turned off when a staff member installed a different free antivirus. Both are fixed and the free product removed.

### 6.3 Tamper protection

Tamper protection stops users and programs from turning off Defender. The supplier enables it across all PCs.

### 6.4 Responding to alerts

When Defender blocks something, the alert appears in the console. Most are routine. If an alert says a threat was found but not removed, Nadia disconnects the PC from the network and tells the supplier immediately.

### Scans and performance

Staff sometimes complain that antivirus slows their PC. The supplier schedules full scans for lunchtime and relies on real-time protection the rest of the day. Explaining this to staff removes the reason they turned protection off in the first place, which is better than relying only on tamper protection.

Nadia also checks that protection updates arrive daily; a PC with old definitions is flagged in the console.

### Quarantine

Blocked files go to quarantine, where they cannot run. Only the supplier may restore a quarantined file, after confirming it is safe, so staff cannot release something harmful by accident.

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

Software should come from the vendor's official site, the Microsoft Store or the supplier's managed catalogue. Free tools from download sites often bundle unwanted programs, which is how the adware arrived.

### 7.2 Verifying downloads

Many vendors publish a checksum for each download. Nadia shows staff how the supplier checks a downloaded installer's SHA-256 hash against the vendor's published value before adding it to the catalogue. A matching hash shows the file was not corrupted or replaced.

### 7.3 Approving software

New software requests go to Lena, who checks the business need, and to the supplier, who checks the source and licence. Approved software goes into the catalogue.

### 7.4 Recording

The supplier keeps a list of approved software and versions. CIS Controls v8 Control 2 asks organisations to keep a software inventory and allow only authorised software.

### Browser extensions

Browser extensions are software too. Some read every page a user visits, including client portals. The supplier sets a policy allowing only approved extensions, such as the password manager. Staff who want another extension request it through the same process as other software.

Nadia explains to staff that free extensions which promise coupons or downloads often collect browsing data, which matters for a firm handling client finances.

### Uninstalling unused software

Software nobody uses still needs updates. Nadia lists programs not opened in six months; with users' agreement, the supplier removes them, reducing what must be patched.

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

Nadia and the supplier choose ten settings from the CIS Benchmark and Microsoft security baseline: firewall on, screen lock after ten minutes, guest account off, autorun off, SMBv1 off, Defender PUA blocking, macros from the internet blocked, LAPS, remote desktop off and PowerShell logging.

### 8.2 Applying

The supplier applies them through its management tool to a pilot group of three PCs for a week. One accountant's old tax tool needs a macro from an internet-downloaded template; the template is saved to a trusted location instead.

### 8.3 Checking

The management tool reports compliance. Nadia spot-checks two PCs by opening the settings directly.

### 8.4 Exceptions

Any PC that cannot take a setting gets a recorded exception with a reason and review date.

### Explaining settings to staff

Nadia writes a one-page note for staff describing what will change and why: the screen locks after ten minutes, USB sticks do not run anything automatically, and macros in documents from the internet are blocked. Each line has a short reason.

She also explains what to do if something stops working: raise a ticket rather than looking for a way around it. Two tickets arrive in the first week, both resolved within a day.

### Local Administrator Password Solution

LAPS gives every PC a unique, random local administrator password stored in the directory. If one PC's password leaked, it would not open any other PC, and the supplier can read the password when needed for repairs.

### Reviewing the settings list

The ten settings are reviewed each year against the latest CIS Benchmark and Microsoft baseline, since recommendations change with new Windows versions.

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

Accountants carry laptops to clients. If one is stolen, BitLocker makes the drive unreadable without the key. Client financial data are confidential, so encryption is essential.

### 9.2 Enabling

The supplier enables BitLocker with TPM protection through the management tool, storing recovery keys in the directory. The PC with a disabled TPM from chapter 2 has it enabled first.

### 9.3 Verifying

Nadia checks encryption status in the console and with the manage-bde status command on two PCs. All laptops show fully encrypted with protection on.

### 9.4 Recovery keys

If BitLocker asks for a recovery key, the user calls IT, who verifies identity before reading out the key. Retrieval is logged.

### Desktops too

Office desktops are encrypted as well. A break-in could take desktops as easily as laptops, and encryption costs nothing extra on PCs with a TPM. The supplier enables BitLocker on all thirty PCs, not just laptops, in a second wave a week after the laptops.

Nadia also checks USB sticks used to carry client files to meetings. The firm buys encrypted sticks and asks staff to stop using personal ones.

### Encryption during repair

When a PC goes for repair, BitLocker may need suspending for a firmware update. The supplier resumes protection afterwards and Nadia checks the status the same day.

### Checking new PCs

Every new PC's encryption status is checked on its first day, before it receives client data, and noted on the joiner checklist.

### Reporting

Lena receives a monthly line: PCs encrypted out of thirty.

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

The file server holds client files and is backed up nightly to the network storage box, with a weekly copy to cloud storage. PCs store work on the file server, so they need little backing up.

### 10.2 Why separation matters

Ransomware can encrypt anything it can reach, including the backup box if it is mapped as a drive. The supplier sets the box so that backups are written by the backup software only, and the cloud copy keeps older versions that cannot be changed for thirty days.

### 10.3 Checking

Each morning, the backup software emails a report. Nadia sets up a rule to flag failures and checks the report weekly with the supplier.

### 10.4 Restore tests

Once a month, she restores one folder to a test location and confirms the files open. CIS Controls v8 Control 11 includes testing recovery.

### Recovery time

Lena asks how long recovery would take. Nadia times a restore of a large client folder: forty minutes from the backup box, three hours from the cloud copy. Lena decides this is acceptable but asks that the most active folders are restored first in any real event.

This conversation turns backup from a technical task into a business decision, which is where it belongs.

### Retention

The firm must keep some records for several years. The supplier sets backup retention to match, keeping monthly copies for seven years in cloud storage, and Lena confirms the period with the firm's compliance adviser.

### Backup box updates

The storage box's own firmware is updated quarterly, since it holds every copy.

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

The router connects the office to the internet. Its firmware needs updates and its admin password must be known and strong. With the old supplier's help, the admin password is reset, firmware updated and remote management from the internet turned off.

### 11.2 Wi-Fi

Staff Wi-Fi uses WPA2 or WPA3 with a strong password. Clients visiting the office use a separate guest network that cannot reach the file server.

### 11.3 Host firewalls

Windows Defender Firewall stays on for all profiles, so PCs are protected on hotel or client networks.

### 11.4 Printers

Network printers also have admin pages and firmware; their default passwords are changed.

### Router firmware routine

Router firmware is easy to forget. Nadia adds a quarterly check to the supplier's routine: confirm the router's firmware version against the maker's site and update if needed, during an evening.

She also checks the router's port forwarding list and finds an old rule forwarding a port to a PC that no longer exists. The rule is removed, since an open forward is an unnecessary entry point.

### DNS filtering

The supplier points office DNS to a filtering service that blocks known malicious sites. This adds a cheap layer of protection for all devices, including printers.

### Default router settings

Features such as UPnP, which lets devices open ports automatically, are turned off on the router unless something genuinely needs them.

### Network inventory

Nadia lists every device on the office network from the router's client table and matches each to the inventory; two unknown entries turn out to be staff phones on the wrong Wi-Fi.

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

Partners reach the file server through the supplier's VPN with MFA. Each user has their own account.

### 12.2 Remote desktop

Remote desktop to office PCs is only available through the VPN, never directly from the internet.

### 12.3 Home networks

Staff are asked to keep their home router updated and not to share work laptops with family.

### 12.4 Remote support

When Nadia helps a remote user, she uses the supplier's remote support tool, which asks the user to accept each session.

### Supporting remote users safely

Remote users can be impersonated as easily as office users. Before starting a remote session, Nadia confirms the caller by phoning back on their known number. During the session, she explains what she is doing and ends it as soon as the task is complete.

She never asks users for their passwords; if she needs to sign in as an administrator, she uses her own admin account.

### Lost laptop away from the office

If a laptop is lost at a client site, the user phones the office. Nadia checks encryption status, signs the user out of all sessions, resets the password and records the event for Lena, who decides whether clients need to be told.

### Home printers

Staff printing client documents at home are asked to collect printouts immediately and shred them, since paper leaks are as real as digital ones.

### VPN disconnection

The VPN disconnects after a period of inactivity, so an unattended laptop does not stay connected to the office network.

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

Staff forward suspicious emails to a report address. Nadia checks headers and links without opening attachments, and the supplier blocks the sender if malicious.

### 13.2 When someone clicks

If a staff member entered their password on a fake page, Nadia resets the password, checks for new email forwarding rules and confirms MFA was not approved by mistake.

### 13.3 Awareness

Short monthly tips cover tax-season phishing, which targets accountants with fake revenue authority messages.

### 13.4 Blame-free reporting

Staff who report a click quickly get thanks, not blame, so they keep reporting.

### Checking a reported email

When an email is reported, Nadia looks at the sender's real address, the reply-to address and where links point by hovering over them. Messages that pretend to be from the tax authority but come from unrelated domains are blocked. She records each report briefly, building a picture of what the firm receives.

She never forwards suspicious attachments to colleagues; the supplier handles analysis in its own safe environment.

### Payment change requests

Accountants are targeted with emails asking to change a client's bank details. The firm's rule is that any change to payment details is confirmed by phone using a number already on file, never one in the email. Nadia includes this rule in the monthly tip.

This is a process control, not a technical one, and it stops a fraud that no filter can fully catch.

### Measuring reports

Monthly report counts help Lena see whether awareness is working; more reports with fewer clicks is a good sign.

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

New PCs are enrolled in the management tool on first start, receiving settings, apps and encryption automatically.

### 14.2 Reassigning

When a PC moves to a new user, it is reset and re-enrolled rather than just handed over.

### 14.3 Leavers

A leaver's account is disabled on their last day and their PC is collected.

### 14.4 Disposal

Old drives are wiped using the manufacturer's secure erase or destroyed, with a certificate, following NIST SP 800-88.

### Joiner setup

A joiner's PC is prepared before their first day: enrolled, encrypted and updated, with their standard account created. On day one Nadia helps them set up MFA and the password manager. Doing this in person avoids rushed setups that skip steps.

The joiner checklist is a single page and is signed off by Nadia and the new starter.

### Lost or broken devices

Broken PCs under warranty are sent for repair only after the drive is removed or encryption confirmed. Lost devices are reported and recorded as in chapter 12.

### Inventory updates

Every joiner, move and leaver updates the PC inventory: who has the PC, its serial and its status. The monthly comparison with the management tool catches missed updates.

At the end of the placement, the inventory matches the management tool exactly for all thirty PCs.

### Mobile phones

Phones that read work email are enrolled in app protection, so work data can be removed from a lost phone without wiping personal photos.

### Leaver data

Before a leaver's account is disabled, their manager confirms which files should move to shared folders, so client work is not lost.

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

Each system has a short page: what it is, how it is set up, who looks after it and where passwords are stored.

### 15.2 Change records

Every change is noted with date, who, what and why.

### 15.3 Tickets

Good tickets describe the problem, steps taken and outcome, so others can learn.

### 15.4 Standards

NIST SP 800-128 links configuration management with documentation and change control.

### Where passwords live

System pages record where a password is stored, never the password itself. Router, printer and firmware passwords are kept in the password manager's IT vault, which only Nadia and the supplier can open.

This replaces a paper notebook in Lena's drawer, which is shredded once its contents are moved.

### Knowledge base

Common fixes become short knowledge base articles: how to reset MFA, how to reconnect the VPN, how to request software. Staff can solve simple problems themselves, and new technicians learn faster.

Nadia writes eight articles during the placement, each reviewed by the supplier for accuracy.

### Reviewing documents

Documentation drifts like settings. Nadia adds a yearly review date to every system page, and the supplier checks pages after any major change. Out-of-date documentation can mislead someone during an outage, when accuracy matters most.

### Change review

Each Friday, Nadia and the supplier review the week's change records together for five minutes to spot anything unexpected or unrecorded.

### Templates

Nadia creates templates for system pages, tickets and change records, so every entry has the same fields and nothing important is left out. Templates also make reviews faster, because reviewers know where to look for each detail.

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

Nadia's project measures local admin rights and update status across all thirty PCs, then reduces both.

### 16.2 Measuring

Using exports and the labs, she finds 12 of 30 PCs with extra admins and 25 of 30 within 14 days of updates.

### 16.3 Method

She records the export date and steps so she can repeat them.

### 16.4 Agreement

Lena approves the plan and measures.

### Why these two measures

Nadia chose local admin rights and update status because both relate directly to the adware incident and both can be measured from existing exports. Admin rights let staff install software; out-of-date PCs give that software more weaknesses to use. Fixing both addresses the cause of the incident rather than just its symptoms.

She avoided measures needing new tools, so the project fits the placement time.

### Validating the data

Before relying on exports, she checks three PCs by hand: the local administrators group and the update history match the exports. She records these checks.

She also notes that two PCs were switched off during measurement; they are counted separately and checked when switched on.

### Timeline

Measuring takes one week, changes four weeks and re-measuring one week, with a buffer for month-end, when accountants are busiest and changes are paused.

### Baseline table

The baseline table shows each measure, the count, the total, the date and the export used, with offline PCs listed separately.

### Measuring with care

Exports are taken at the same time of day on a Tuesday, avoiding Monday when PCs that were off over the weekend are still catching up. This small choice makes the before and after numbers comparable.

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

Extra admin rights are removed after talking to each user, and the self-service catalogue is introduced. Update failures are fixed as in chapter 5.

### 17.2 Results

Extra admins fall from 12 to 0 PCs; updates within 14 days rise from 25 to 29 of 30.

### 17.3 Remaining

One PC stays late because it is a partner's laptop often off; a reminder is set.

### 17.4 Staff reaction

Most staff did not notice the change; two asked for software via the catalogue.

### Talking to each user

Before removing admin rights, Nadia speaks to each of the affected staff. She asks what they use admin rights for, checks those tools are in the catalogue and explains the change. Most used rights only for printer drivers, which the supplier now deploys automatically.

One partner asks to keep rights; Lena decides that partners follow the same rule, and the partner is given a separate admin account held by the supplier for rare needs.

### Checking results honestly

Nadia re-measures with the same exports and steps. She notes that update results can vary month to month, so she will check again next month. She also notes that admin rights could creep back if the supplier grants them for quick fixes, which is why the quarterly check matters.

The report shows both measures with counts, dates and a short explanation of the remaining late PC.

### Cost

The project used about twelve hours of Nadia's time and four of the supplier's.

### Follow-up check

One month later, Nadia repeats both measures. Admin rights remain at zero extra and updates at twenty-nine of thirty, suggesting the changes are holding.

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

Nadia learned that security work is mostly careful support.

### 18.2 Recommendations

Quarterly admin and update checks, MFA for all systems, and router firmware checks.

### 18.3 Handover

Scripts and notes are handed to the supplier.

### 18.4 Assessment

Sam assesses the report and Lena's feedback.

### What worked

Three things worked well: measuring before changing, talking to staff before removing rights, and fixing update failures by cause rather than one by one. Each made changes smoother and results clearer.

What worked less well was timing. Month-end slowed progress, and Nadia would plan around it from the start next time.

### Skills gained

Nadia lists the skills she practised: reading firmware settings, managing accounts and rights, checking updates, verifying encryption, testing restores, handling phishing reports and writing documentation. Sam notes that these map directly to entry-level support roles.

She also reflects on soft skills: explaining changes simply, listening to staff concerns and asking permission before acting.

### Further study

She plans to study Linux administration next, since many small firms now use cloud services built on it, and to read the CIS Controls v8 implementation group 1 guide in full.

### Thanks

Nadia thanks Lena, the supplier and the staff of Harlow & Pike.

### Feedback from the firm

Lena's feedback notes fewer support calls about slow PCs and no new unwanted software since the changes. She asks the institute for another placement student next year.

### Advice to the next student

Nadia leaves a short note for next year's student: read the system pages first, ask Lena before changing anything visible, and avoid month-end for changes.

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
