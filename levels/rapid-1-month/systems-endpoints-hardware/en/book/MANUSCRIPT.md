# Systems, Endpoint and Hardware Security: Rapid Course

- Language: English (`en`); course 012, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; One offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: volunteers and staff in very small organisations who need to secure a handful of laptops in four weeks with no budget.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only servers, endpoints and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, inventories, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read one chapter per week: the chapters follow one volunteer IT lead at a fictional food bank after a stolen laptop, covering device lists and updates, accounts and settings, encryption and backups, and a monthly routine with simple incident steps. Run the lab in week one, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Leah Morgan** | Volunteer IT lead | Invented |
| **Northgate Learning** | Fictional course provider | Invented |
| **Fenwick Community Food Bank** | Fictional charity (12 laptops, 1 front desk PC) | Invented |

### Core sources

NIST [SP 800-123](https://doi.org/10.6028/NIST.SP.800-123), [SP 800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4), [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128), [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5) and [SP 800-193](https://doi.org/10.6028/NIST.SP.800-193); [CIS Controls v8](https://www.cisecurity.org/controls/v8) and [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); DISA [STIGs](https://public.cyber.mil/stigs/); Microsoft [Windows security baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines); Linux [kernel self-protection](https://www.kernel.org/doc/html/latest/security/self-protection.html). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Week 1: Know your devices and update them

### Learning outcomes

You will (1) list every device and who uses it; (2) run a five-point quick check; (3) get updates working everywhere.

### 1.1 The case

Leah Morgan volunteers as the IT lead at the fictional Fenwick Community Food Bank, which has twelve laptops used by staff and volunteers, a shared PC at the front desk and a cloud email and file service. Leah is taking the one-month rapid course from the fictional Northgate Learning. Last month a volunteer's laptop was stolen from a car, and nobody could say whether it was encrypted or what was on it. The trustees asked Leah to make sure that does not happen again, with no budget beyond what the food bank already pays for.

### 1.2 Start with a list

You cannot protect what you do not know about. CIS Controls v8 starts with an inventory of devices for this reason. Leah makes a simple spreadsheet with one row per device: a short name, who uses it, model, serial number and where it normally lives. She finds the twelve laptops, the front desk PC and an old laptop in a cupboard that nobody uses, which is wiped and recycled.

The serial number column answers the question the theft raised: with it, the food bank can tell the police and the insurer exactly which device was taken. The "where it lives" column matters for the same reason; a laptop that normally goes home in a volunteer's car carries more risk than one that stays in the office.

### 1.3 The quick check

Leah checks five things on every laptop, because together they cover the most common harms: updates installed within fourteen days, disk encryption on, the user working in a standard account rather than an administrator, a screen lock, and files backed up in the last week. Each is a yes or no.

Each check maps to a part of the stolen-laptop problem. Encryption decides whether a thief can read the disk. Backups decide whether the food bank loses work. Updates and a standard account make it harder for a harmful program to take over a laptop in the first place. A screen lock protects a laptop left open on the front desk. Recording yes or no keeps the check quick enough to repeat every month.

### Lab — Five-point quick check

```python
"""Five-point quick check across a small charity's laptops (synthetic, stdlib only)."""
checks = ["updates<=14d", "encrypted", "standard user", "screen lock", "backup<=7d"]
laptops = {"FB01": [1,1,1,1,1], "FB02": [1,0,0,1,1], "FB03": [0,1,1,1,0], "FB04": [1,1,0,1,1], "FB05": [1,1,1,0,1],
           "FB06": [1,0,1,1,1], "FB07": [0,0,0,1,0], "FB08": [1,1,1,1,1], "FB09": [1,1,0,1,1], "FB10": [1,1,1,1,0],
           "FB11": [1,0,1,1,1], "FB12": [1,1,1,1,1]}
for i, c in enumerate(checks):
    print(f"{c:14} {sum(v[i] for v in laptops.values()):2d}/{len(laptops)}")
full = [k for k, v in laptops.items() if all(v)]
print(f"laptops passing all five: {len(full)}/{len(laptops)}; worst: {min(laptops, key=lambda k: sum(laptops[k]))}")
```

Run with `python3 lab_quickcheck.py`. Verified output:

```text
updates<=14d   10/12
encrypted       8/12
standard user   8/12
screen lock    11/12
backup<=7d      9/12
laptops passing all five: 3/12; worst: FB07
```

### 1.4 Reading the result

Only three of twelve laptops pass all five. Encryption and standard accounts are weakest at eight of twelve each. FB07 fails four checks: it is an old laptop used by a weekend volunteer. Screen lock is nearly everywhere already. This tells Leah where to spend her four weeks.

The lab's per-laptop rows show where the gaps sit. FB02, FB06, FB07 and FB11 are not encrypted; FB02, FB04, FB07 and FB09 have users working as administrators; FB03 and FB07 are behind on updates; FB03, FB07 and FB10 have no recent backup; and only FB05 lacks a screen lock. FB01, FB08 and FB12 pass everything. Encryption comes first because it is exactly what nobody could confirm for the stolen laptop.

### 1.5 Getting updates working

Two laptops are behind on updates. One has a full disk; the other has updates paused. Leah frees space, removes the pause and sets updates to install automatically with a restart outside opening hours. She also checks that the browser and PDF reader update themselves. NIST SP 800-40 Rev. 4 describes patching as preventive maintenance; for a small charity, that means making automatic updates work and checking them monthly.

Both problems were invisible to the users: a laptop with paused updates keeps working normally until the day a known flaw is used against it. Fixing the cause matters more than installing the missing updates once. A full disk will fill again, so Leah moves old files to the cloud service as well as clearing space. By Friday all twelve laptops show updates within fourteen days.

### Worked example

Leah fills in the spreadsheet in an afternoon, runs the quick check over two days as volunteers come in, and fixes the two update problems the same week. By Friday, all twelve laptops show updates within fourteen days.

> **Synthetic case.** Fenwick Community Food Bank, Northgate Learning and all people and data are fictional; figures are synthetic.

### Errors and limits

Assuming a laptop is fine because it seems to work is how the stolen laptop's status went unknown. Check, record and date it.

### Exercises

- **EX001 — Inventory first.** Why does the course start with a device list? *Rubric:* 3 = cannot protect unknown devices, links to CIS; 2 = knowing devices; 1 = vague; 0 = none.
- **EX002 — Spreadsheet columns.** List the columns of Leah's device spreadsheet. *Rubric:* 3 = five columns; 2 = four; 1 = fewer; 0 = none.
- **EX003 — Cupboard laptop.** What should happen to an unused old laptop? *Rubric:* 3 = wipe and recycle with record; 2 = remove; 1 = keep; 0 = none.
- **EX004 — Five checks.** Name the five quick checks. *Rubric:* 3 = all five; 2 = four; 1 = fewer; 0 = none.
- **EX005 — Weakest checks.** Which checks scored lowest in the lab? *Rubric:* 3 = encryption and standard user, 8/12; 2 = one; 1 = wrong; 0 = none.
- **EX006 — All-five count.** How many laptops passed every check? *Rubric:* 3 = 3 of 12; 2 = three; 1 = wrong; 0 = none.
- **EX007 — Worst laptop.** Which laptop did worst and why might that be? *Rubric:* 3 = FB07, old weekend volunteer laptop; 2 = FB07; 1 = wrong; 0 = none.
- **EX008 — Full disk.** How can a full disk stop updates? *Rubric:* 3 = no space to download and install; 2 = blocks; 1 = vague; 0 = none.
- **EX009 — Paused updates.** What should Leah do about paused updates? *Rubric:* 3 = remove pause, set automatic; 2 = unpause; 1 = vague; 0 = none.
- **EX010 — Other software.** Besides Windows, what else needs updating? *Rubric:* 3 = browser and PDF reader with checking; 2 = apps; 1 = vague; 0 = none.
- **EX011 — Restart timing.** When should automatic restarts happen at a food bank? *Rubric:* 3 = outside opening hours; 2 = later; 1 = anytime; 0 = none.
- **EX012 — Recording dates.** Why write the date beside each check? *Rubric:* 3 = shows when status was true, enables comparison; 2 = tracking; 1 = vague; 0 = none.
- **EX013 — Stolen laptop lesson.** What did the stolen laptop reveal about the food bank? *Rubric:* 3 = unknown encryption and contents; 2 = no records; 1 = vague; 0 = none.

### Synthesis

In week one, Leah knows every device, has a clear picture of five basics, and has updates working everywhere.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Week 2: Accounts and safer settings

### Learning outcomes

You will (1) move everyone to standard accounts; (2) secure email sign-in with MFA; (3) apply a few key settings.

### 2.1 Standard accounts

Four laptops have users working as administrators. That means any harmful program they open can change anything on the laptop. Leah creates a separate admin account on each laptop, known only to her and the deputy manager and kept in the password manager, and changes the everyday accounts to standard users. Saltzer and Schroeder called this least privilege: give each user only the rights they need.

The four were FB02, FB04, FB07 and FB09. For the volunteers, little changes day to day: they open the same apps and save to the same places. What changes is that a harmful attachment opened in a standard account cannot install itself system-wide or turn off Defender, so it does far less damage. Leah made the change in two evenings and checked each laptop afterwards by signing in as the everyday user.

### 2.2 Getting software without admin

Volunteers sometimes need a new app. Instead of giving them admin rights, Leah installs approved apps herself, usually within a day. She keeps a short list of approved apps so requests are quick.

The approved list grows from real requests: a volunteer who needs a PDF editor for donation receipts asks once, Leah checks the app's publisher and source, installs it, and adds it to the list so the next request takes minutes. The monthly routine checks that nobody has become an administrator again, which is the usual way this arrangement erodes.

### 2.3 Passwords and MFA

The cloud email service holds client names and addresses. Leah turns on multi-factor authentication for every account, with an authenticator app on volunteers' phones and backup codes kept in the office safe. She asks everyone to use a long passphrase and a password manager. Shared logins, such as the front desk account, get their own strong password stored in a shared vault.

This matters even with encrypted laptops: a stolen password could open the cloud email from anywhere, and encryption does nothing about that. In the worked example, two volunteers needed help setting up the authenticator app, which Leah gave in person on their next shift. Keeping backup codes in the office safe means a volunteer who loses a phone can still sign in after Leah checks who they are.

### 2.4 Key settings

Leah applies a handful of settings from the CIS Benchmark that matter most: Windows firewall on, screen lock after five minutes of inactivity, guest account off, and Microsoft Defender with tamper protection on. She does this by hand on each laptop with a printed checklist, because twelve laptops do not justify a management system yet.

Each setting has a reason in this case. The firewall blocks unexpected connections when laptops are used on other networks. The five-minute lock protects laptops left open between clients. The guest account is off so nobody can sign in without an account. Tamper protection stops a harmful program from switching off Defender. The printed checklist also records which laptops have been done, so the next one picks up where the last stopped.

### 2.5 Front desk PC

The shared front desk PC is used by many volunteers. It gets a standard account that opens only the browser and the booking system, and the screen locks when unattended. Volunteers sign in to the booking system with their own accounts so actions are traceable.

The front desk PC is the device most likely to be used by someone Leah has never met, which is why it is the most limited. Because it opens only the browser and the booking system, a volunteer cannot install software or browse to unrelated sites by habit. Personal booking accounts mean a wrong entry can be traced to the person and corrected with them, not blamed on "front desk".

### Worked example

In two evenings Leah changes the four admin users to standard, turns on MFA for all fourteen email accounts, and applies the four key settings with her checklist. Two volunteers need help setting up the authenticator app, which she gives in person on their next shift.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Turning on MFA without backup codes can lock someone out if they lose their phone.

### Exercises

- **EX014 — Admin danger.** What can a harmful program do when its user is an administrator? *Rubric:* 3 = change anything, install, disable protection; 2 = more damage; 1 = vague; 0 = none.
- **EX015 — Admin password storage.** Where should the separate admin passwords be kept? *Rubric:* 3 = password manager, limited people; 2 = securely; 1 = note; 0 = none.
- **EX016 — App requests.** How do volunteers get new apps without admin rights? *Rubric:* 3 = Leah installs from approved list; 2 = ask; 1 = vague; 0 = none.
- **EX017 — MFA backup.** Why keep backup codes in the safe? *Rubric:* 3 = recovery if phone lost; 2 = backup; 1 = vague; 0 = none.
- **EX018 — Email sensitivity.** Why does email need MFA at a food bank? *Rubric:* 3 = client personal data; 2 = protection; 1 = vague; 0 = none.
- **EX019 — Shared login.** How should the front desk login be handled? *Rubric:* 3 = strong password in shared vault, personal booking accounts; 2 = vault; 1 = shared note; 0 = none.
- **EX020 — Four settings.** Name the four key settings applied. *Rubric:* 3 = all four; 2 = three; 1 = fewer; 0 = none.
- **EX021 — Tamper protection.** What does tamper protection prevent? *Rubric:* 3 = turning off Defender; 2 = disabling; 1 = vague; 0 = none.
- **EX022 — Checklist value.** Why use a printed checklist for settings? *Rubric:* 3 = consistency across laptops; 2 = reminder; 1 = vague; 0 = none.
- **EX023 — Traceability.** Why do volunteers use personal booking accounts? *Rubric:* 3 = traceable actions; 2 = accountability; 1 = vague; 0 = none.
- **EX024 — Passphrase advice.** What password advice did Leah give? *Rubric:* 3 = long passphrase with manager; 2 = long; 1 = vague; 0 = none.
- **EX025 — In-person help.** Why help volunteers with MFA in person? *Rubric:* 3 = reduces lockouts and confusion; 2 = support; 1 = vague; 0 = none.
- **EX026 — Week two result.** Summarise the state at the end of week two. *Rubric:* 3 = standard users, MFA, settings; 2 = two; 1 = one; 0 = none.

### Synthesis

By the end of week two, nobody works as an administrator, email is protected by MFA and every laptop has the key settings.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Week 3: Encryption and backups

### Learning outcomes

You will (1) turn on and verify disk encryption; (2) store recovery keys safely; (3) check and test backups.

### 3.1 Why encryption

If a laptop is stolen while switched off, disk encryption makes its contents unreadable. Had the stolen laptop been encrypted, the food bank could have said with confidence that client data were safe. Windows BitLocker or device encryption uses the laptop's TPM chip so users do not need an extra password at startup.

The limit matters: encryption protects a laptop that is off or at its sign-in screen after a restart. A laptop stolen while unlocked and in use is protected only by the screen lock, which is why both checks are in the quick check.

### 3.2 Turning it on

Four laptops are not encrypted. Leah checks that each has a TPM enabled, turns on BitLocker and saves the recovery key to the food bank's cloud account and a printed copy in the office safe. One older laptop has its TPM switched off in its firmware settings; with the volunteer's agreement, Leah enables it first.

The recovery key matters because a firmware update or hardware change can make BitLocker ask for it at startup. Without the key, the volunteer's files would be locked away from the food bank too. Keeping one copy in the cloud account and a printed one in the safe means it is available even when the cloud service cannot be reached. By Thursday, all twelve laptops are encrypted.

### 3.3 Checking it worked

Leah confirms each laptop shows encryption on and protection active, rather than assuming. She notes the date in the spreadsheet.

Starting encryption is not the same as finishing it: a laptop can show encryption "in progress" for hours, or have it suspended after an update. Leah checks each of the four laptops she changed and the eight that were already encrypted, because the original problem was a laptop nobody had checked. The spreadsheet row for each device now records encryption status with the date it was confirmed, and the monthly routine repeats that check. If a laptop is stolen next year, the answer to "was it encrypted?" is a dated line, not a guess.

### 3.4 Backups

Files are stored in the cloud file service, which keeps previous versions for thirty days. Three laptops still keep documents only on the desktop. Leah moves those folders into the cloud service so they are backed up, and shows volunteers where to save.

The three were FB03, FB07 and FB10, which failed the backup check in the lab. Desktop-only files are the ones lost with a stolen laptop, encrypted or not: encryption keeps them away from the thief but does not give them back to the food bank. With the folders moved, a stolen laptop would cost the device and nothing else.

### 3.5 Testing a restore

Leah deletes a test file and restores it from the cloud service's recycle bin, then restores an older version of a document. Both work. CIS Controls v8 Control 11 includes testing that data can be recovered, because backups that have never been restored may fail when needed.

The thirty-day version history sets a limit: a file damaged and not noticed for six weeks could not be recovered this way. Leah records that limit for the trustees rather than claiming backups cover everything. She chose a test file and an old document version because these are the two situations volunteers actually face: a deleted file and an overwritten one.

### Worked example

By Thursday, all twelve laptops are encrypted and verified, all documents live in the cloud service, and two restore tests have succeeded.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

A recovery key saved only on the laptop itself is useless if the laptop is locked; keep it elsewhere.

### Exercises

- **EX027 — Off versus on.** When does disk encryption protect a stolen laptop? *Rubric:* 3 = when switched off or locked at startup; 2 = when off; 1 = always; 0 = none.
- **EX028 — TPM role.** What does the TPM do for BitLocker? *Rubric:* 3 = holds keys, no extra startup password; 2 = keys; 1 = vague; 0 = none.
- **EX029 — Key locations.** Where did Leah store recovery keys? *Rubric:* 3 = cloud account and safe; 2 = one; 1 = laptop; 0 = none.
- **EX030 — Disabled TPM.** What did Leah do about a disabled TPM? *Rubric:* 3 = enabled in firmware with agreement; 2 = enabled; 1 = vague; 0 = none.
- **EX031 — Verify step.** Why verify encryption after turning it on? *Rubric:* 3 = confirm protection active; 2 = check; 1 = vague; 0 = none.
- **EX032 — Desktop files.** Why move desktop files into the cloud service? *Rubric:* 3 = backed up and versioned; 2 = backup; 1 = vague; 0 = none.
- **EX033 — Version history.** How long are previous versions kept? *Rubric:* 3 = 30 days; 2 = month; 1 = vague; 0 = none.
- **EX034 — Restore test.** Describe the two restore tests. *Rubric:* 3 = deleted file and older version; 2 = one; 1 = vague; 0 = none.
- **EX035 — CIS backup control.** Which CIS Control covers data recovery? *Rubric:* 3 = Control 11; 2 = 11; 1 = wrong; 0 = none.
- **EX036 — Key mistake.** What is wrong with saving the key only on the laptop? *Rubric:* 3 = inaccessible when locked; 2 = bad; 1 = vague; 0 = none.
- **EX037 — Answering trustees.** How would Leah now answer trustees after a theft? *Rubric:* 3 = encrypted, verified date, data safe; 2 = encrypted; 1 = vague; 0 = none.
- **EX038 — Week three result.** Summarise week three's result. *Rubric:* 3 = encrypted 12/12, cloud, restores; 2 = two; 1 = one; 0 = none.

### Synthesis

After week three, a stolen laptop would no longer expose client data, and files can be recovered.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Week 4: Keep it going and respond calmly

### Learning outcomes

You will (1) re-run the quick check; (2) set a monthly routine; (3) prepare simple incident steps.

### 4.1 Re-running the check

Leah repeats the five-point quick check with the same method. All twelve laptops now pass all five, compared with three of twelve at the start. She records the result with the date and shares a one-page summary with the trustees: what was found, what was changed and what it cost, which was only her time.

Using the same method matters: the before and after figures are comparable only because the five checks and their yes or no answers did not change. The summary also tells the trustees what the theft would mean now: an encrypted laptop with files in the cloud, a recovery key on record and a dated spreadsheet row.

### 4.2 A monthly routine

Improvements fade without routine. Leah writes a fifteen-minute monthly checklist: run the quick check on each laptop, confirm updates are current, check that no one has become an administrator, look at the cloud service's sign-in alerts, and restore one file. A second volunteer is trained to do it when Leah is away.

Each item checks that a fix has not quietly undone itself: updates paused again, a volunteer given admin rights in a hurry, a sign-in alert ignored, or a backup that no longer restores. Restoring one file a month keeps the skill fresh as well as testing the service. The trustees asked for a two-line update at each meeting, which the routine's record makes easy.

### 4.3 When something goes wrong

Leah writes four short responses on one page. Lost or stolen laptop: tell Leah, who confirms encryption, signs the user out everywhere and changes their password. Suspicious email clicked: change the password, check MFA prompts and tell Leah. Antivirus warning: disconnect from Wi-Fi and call Leah. Account locked out: Leah verifies the person by phone before resetting. NIST SP 800-61 describes incident handling in detail, but a small charity needs simple first steps that anyone can follow.

Each response is something a volunteer can do without IT knowledge, and each ends with Leah. For a stolen laptop, the first question is the one nobody could answer last month: was it encrypted? The spreadsheet now answers it at once.

### 4.4 Joiners and leavers

New volunteers get a standard account, MFA set up in person and a two-minute talk on saving files to the cloud. Leavers return laptops, and their accounts are disabled the same day.

The leavers step closes the gap the food bank had before: accounts that stay active after someone stops volunteering. Disabling the account on the same day means a returned laptop cannot be used to reach the email, and a laptop that is never returned is encrypted and has no working account behind it. Leah notes each joiner and leaver in the device spreadsheet against the laptop they used. The monthly routine checks the list of active accounts against current volunteers, so a missed leaver is caught within a month.

### 4.5 What remains

Some things are beyond a month: replacing the oldest laptop, which will soon stop receiving updates, and considering a free device management service for charities. Leah lists them for the trustees with rough timings.

FB07, the old laptop that failed four of the five checks at the start, is the kind of device this covers. Once the oldest laptop stops receiving updates, the quick check will fail it every month whatever Leah does, so replacing it is a budget decision for the trustees, not an IT task. A device management service would replace the printed checklist if the food bank grows beyond twelve laptops.

### Worked example

The trustees approve the monthly routine and ask for a two-line update at each meeting. Leah's final note shows 12 of 12 laptops passing all five checks, the date, and the two remaining items.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

A routine kept in one person's head stops when they leave; write it down and train a second person.

### Exercises

- **EX039 — Before and after.** State the quick check result before and after. *Rubric:* 3 = 3/12 to 12/12; 2 = one; 1 = vague; 0 = none.
- **EX040 — Routine length.** How long should the monthly routine take? *Rubric:* 3 = about fifteen minutes; 2 = short; 1 = vague; 0 = none.
- **EX041 — Routine items.** List the five monthly routine items. *Rubric:* 3 = all five; 2 = four; 1 = fewer; 0 = none.
- **EX042 — Second volunteer.** Why train a second volunteer? *Rubric:* 3 = continuity; 2 = backup; 1 = vague; 0 = none.
- **EX043 — Lost laptop steps.** What are the lost laptop steps? *Rubric:* 3 = confirm encryption, sign out, change password; 2 = two; 1 = one; 0 = none.
- **EX044 — Antivirus warning.** What should a volunteer do on an antivirus warning? *Rubric:* 3 = disconnect, call Leah; 2 = call; 1 = ignore; 0 = none.
- **EX045 — Lockout identity.** Before resetting a locked account, what does Leah do? *Rubric:* 3 = verify by phone; 2 = verify; 1 = vague; 0 = none.
- **EX046 — New volunteer setup.** How is a new volunteer set up? *Rubric:* 3 = standard account, MFA in person, saving guidance; 2 = account; 1 = vague; 0 = none.
- **EX047 — Leaver timing.** When are leaver accounts disabled? *Rubric:* 3 = same day; 2 = soon; 1 = later; 0 = none.
- **EX048 — Remaining items.** Name the two remaining items. *Rubric:* 3 = old laptop replacement and management service; 2 = one; 1 = vague; 0 = none.
- **EX049 — Trustee update.** What did trustees ask for? *Rubric:* 3 = two-line update each meeting; 2 = updates; 1 = vague; 0 = none.
- **EX050 — Main lesson.** In one sentence, what did the month achieve? *Rubric:* 3 = from unknown to known with routines; 2 = improvement; 1 = vague; 0 = none.

### Synthesis

In one month, Leah moved the food bank from not knowing to knowing, with simple routines that keep the basics in place.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Leah Morgan, Northgate Learning, Fenwick Community Food Bank and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** You cannot protect devices you do not know about; CIS Controls v8 starts with inventory.

**EX002.** Short name, user, model, serial number and usual location.

**EX003.** Wipe it securely, recycle it and record that it was disposed of.

**EX004.** Updates within 14 days, encryption, standard account, screen lock, recent backup.

**EX005.** Encryption and standard user accounts, eight of twelve each.

**EX006.** Three of twelve.

**EX007.** FB07, an old laptop used only by a weekend volunteer.

**EX008.** Updates need free space to download and install, so they fail.

**EX009.** Remove the pause and set updates to install automatically.

**EX010.** The browser, PDF reader and other installed apps.

**EX011.** Outside opening hours, so nobody loses work during sessions.

**EX012.** So it is clear when the result was true and later checks can be compared.

**EX013.** Nobody knew whether it was encrypted or what data it held.

**EX014.** It can change settings, install itself and switch off protection.

**EX015.** In the password manager, known only to Leah and the deputy manager.

**EX016.** They ask Leah, who installs approved apps within a day.

**EX017.** So a volunteer who loses their phone can still sign in.

**EX018.** It holds client names and addresses, which must be protected.

**EX019.** A strong password in a shared vault, with personal accounts in the booking system.

**EX020.** Firewall on, five-minute screen lock, guest off, Defender with tamper protection.

**EX021.** It prevents Defender from being turned off by users or programs.

**EX022.** So every laptop gets exactly the same settings.

**EX023.** So each action in the booking system can be traced to a person.

**EX024.** Use a long passphrase and store passwords in a password manager.

**EX025.** It avoids mistakes and lockouts during setup.

**EX026.** No admin users, MFA on all email and key settings on every laptop.

**EX027.** When the laptop is switched off, so the disk cannot be read without unlocking.

**EX028.** It stores the key and unlocks the disk at startup if nothing has changed.

**EX029.** In the food bank's cloud account and on paper in the office safe.

**EX030.** Enabled it in firmware settings with the volunteer's agreement before encrypting.

**EX031.** To confirm encryption finished and protection is active.

**EX032.** So they are backed up with previous versions kept.

**EX033.** Thirty days.

**EX034.** Restoring a deleted test file and an older version of a document.

**EX035.** Control 11, data recovery.

**EX036.** If the laptop is locked, the key on it cannot be reached.

**EX037.** The laptop was encrypted, verified on a recorded date, so client data are unreadable.

**EX038.** All twelve laptops encrypted, documents in the cloud, restores tested.

**EX039.** Three of twelve passing all five at the start, twelve of twelve at the end.

**EX040.** About fifteen minutes.

**EX041.** Quick check, updates current, no new admins, sign-in alerts, restore one file.

**EX042.** So the routine continues when Leah is away.

**EX043.** Confirm encryption, sign the user out everywhere and change their password.

**EX044.** Disconnect from Wi-Fi and call Leah.

**EX045.** Verifies the person by phone.

**EX046.** Standard account, MFA in person and guidance on saving to the cloud.

**EX047.** The same day they leave.

**EX048.** Replace the oldest laptop and consider a free device management service.

**EX049.** A two-line update at each meeting.

**EX050.** The food bank moved from not knowing its devices' state to knowing it, with routines to keep it so.

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
