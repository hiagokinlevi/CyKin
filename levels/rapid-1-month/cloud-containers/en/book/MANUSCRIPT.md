# Cloud and Container Security: Rapid Course

- Language: English (`en`); course 013, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: people who look after a small organisation's cloud services and need practical, proportionate cloud and container security in one month.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only cloud accounts, clusters and workloads you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Misconfigurations are taught from the defender's side using synthetic configurations, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow the only IT person at a small clinic from a patient letter that opened without a login, through foundations and decisions, permission and safe practice, and systems, data and dependencies, to a guided routine lab and synthesis. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Leila Ahmadi** | Rapid course student and practice manager | Invented |
| **Ben Hartley** | Course tutor | Invented |
| **Oakfield Physiotherapy** | Fictional clinic | Invented |
| **Westbrook Community College** | Fictional college | Invented |

### Core sources

NIST [SP 800-145](https://doi.org/10.6028/NIST.SP.800-145), [SP 800-210](https://doi.org/10.6028/NIST.SP.800-210), [SP 800-190](https://doi.org/10.6028/NIST.SP.800-190) and [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207); CSA [Cloud Controls Matrix v4](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); the [AWS](https://aws.amazon.com/compliance/shared-responsibility-model/), [Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) and [Google Cloud](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) shared responsibility pages; Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) and [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) documentation. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Cloud and container security: foundations and decisions

### Learning outcomes

You will (1) explain what cloud and container services a small clinic relies on; (2) use the shared responsibility model to see what the clinic must do; (3) make proportionate first decisions.

### 1.1 The trigger

Leila Ahmadi is the practice manager and only IT person at the fictional Oakfield Physiotherapy, a clinic with eight staff. The clinic stores letters, referrals and invoices in a cloud storage service and runs an online booking app that a local developer packaged as a container on a small hosted platform. In April a patient mentions that a link to her own treatment letter, forwarded by mistake, opened without any login. Leila realises the patient letters folder is shared with "anyone with the link". She joins a one-month rapid course at the fictional Westbrook Community College, with tutor Ben Hartley, to fix this and set up sensible routines.

### 1.2 What cloud means here

NIST SP 800-145 describes cloud computing as on-demand access to shared computing resources managed by a provider. For Oakfield, that means the storage service, the email service and the hosted platform running the booking container. The clinic owns no servers.

### 1.3 Containers in plain terms

A container is a packaged application with everything it needs to run. The booking app container was built by the developer from a base image; if the base image is old, the app inherits its flaws even if the clinic never touches the code.

### 1.4 Who does what

Each provider's shared responsibility page explains that the provider secures its infrastructure while the customer controls accounts, sharing settings, data and what it runs. Oakfield's sharing mistake sits entirely on the clinic's side.

### 1.5 Proportionate decisions

A small clinic cannot do everything at once. Ben suggests three first decisions: fix sharing on sensitive folders today, turn on multi-factor authentication for every account this week, and agree with the developer how the booking container will be kept updated.

### 1.6 Recording decisions

Leila writes each decision with date, reason and owner in a one-page log.

### Worked example

Leila changes the patient letters folder to staff-only that afternoon. She then asks Ben whether she must tell patients. Ben says this depends on what was exposed and for how long, and that she should gather evidence first and consult the clinic's data protection guidance, which chapter 2 covers.

> **Synthetic case.** Leila, Ben, Oakfield and Westbrook are synthetic.

### Errors and limits

Fixing the visible problem quickly is right, but the review must still look for similar problems elsewhere.

### Exercises

- **EX001 — Trigger.** What made Leila notice the sharing problem? *Rubric:* 3 = patient's letter opened without login via forwarded link; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Services used.** Name three cloud services Oakfield relies on. *Rubric:* 3 = storage, email, hosted booking platform; 2 = two; 1 = one; 0 = none.
- **EX003 — Container inheritance.** Why can an old base image affect the booking app? *Rubric:* 3 = app inherits its flaws; 2 = partial; 1 = none; 0 = none.
- **EX004 — Responsibility side.** On which side of shared responsibility does the sharing mistake sit? *Rubric:* 3 = clinic's side; 2 = partial; 1 = none; 0 = none.
- **EX005 — First decisions.** List Ben's three first decisions. *Rubric:* 3 = fix sharing, MFA, container update agreement; 2 = two; 1 = one; 0 = none.
- **EX006 — Decision log.** What does each decision log entry contain? *Rubric:* 3 = date, reason, owner; 2 = two; 1 = one; 0 = none.
- **EX007 — Notification question.** What did Ben advise about telling patients? *Rubric:* 3 = gather evidence, consult guidance; 2 = partial; 1 = none; 0 = none.
- **EX008 — Ownership of servers.** Does Oakfield own any servers? *Rubric:* 3 = no; 2 = partial; 1 = none; 0 = none.
- **EX009 — Definition source.** Which standard defines cloud computing used here? *Rubric:* 3 = NIST SP 800-145; 2 = partial; 1 = none; 0 = none.
- **EX010 — Clinic size effect.** Why make proportionate rather than complete changes? *Rubric:* 3 = small clinic cannot do everything; 2 = partial; 1 = none; 0 = none.
- **EX011 — Visible fix limit.** What must follow the quick fix? *Rubric:* 3 = look for similar problems; 2 = partial; 1 = none; 0 = none.
- **EX012 — Provider duty.** What does the provider secure? *Rubric:* 3 = its infrastructure; 2 = partial; 1 = none; 0 = none.
- **EX013 — Folder change.** What did Leila change on the first afternoon? *Rubric:* 3 = patient letters to staff-only; 2 = partial; 1 = none; 0 = none.

### Synthesis

Understand what the clinic controls and fix the most important things first.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) work within the clinic's authority and data protection duties; (2) collect evidence safely; (3) avoid risky shortcuts.

### 2.1 Authority

As practice manager, Leila is authorised by the clinic's owner, physiotherapist Mark Ellis, to manage accounts and settings. She confirms this in writing for the course and agrees she will only review Oakfield's own services.

### 2.2 Evidence first

Before changing more settings, Leila exports the storage service's sharing report and the activity log for the patient letters folder. She saves them with date and time in a restricted folder.

### 2.3 What the log shows

The activity log shows the folder was set to anyone-with-link in January when a colleague shared one letter with a hospital. The log records four views from outside the clinic: three match the hospital's domain, one is the patient's own forwarded view.

### 2.4 Data protection

Leila follows the regulator's guidance for small organisations, recording what happened, who was affected and why she judges the risk low. Mark, as data controller, makes the final decision and records it.

### 2.5 Safe practice

Leila does not try to "test" whether other links work by guessing addresses or using outside tools. She uses the provider's own reports and settings pages.

### 2.6 Accounts

Each staff member has their own account; the shared reception login is replaced, so the logs show who did what.

### 2.7 Multi-factor authentication

All accounts get a second factor. Two staff without smartphones receive hardware keys.

### Leavers

When staff leave, Leila removes their accounts on their last day and checks whether they owned any shared links, which are moved to a current staff member.

### Worked example

A colleague suggests deleting the activity log to "tidy up". Leila explains that the log is evidence and must be kept, and that tidying would remove the clinic's proof of what happened.

> **Synthetic case.** Synthetic.

### Errors and limits

Changing settings before exporting evidence can erase the record of what was exposed.

### Exercises

- **EX014 — Authority source.** Who authorises Leila's work? *Rubric:* 3 = Mark Ellis, clinic owner; 2 = partial; 1 = none; 0 = none.
- **EX015 — Evidence exports.** What did Leila export first? *Rubric:* 3 = sharing report and activity log; 2 = partial; 1 = none; 0 = none.
- **EX016 — Origin of link.** How did the folder become shared with anyone? *Rubric:* 3 = January share with hospital; 2 = partial; 1 = none; 0 = none.
- **EX017 — Outside views.** What did the outside views show? *Rubric:* 3 = four: three hospital, one patient; 2 = partial; 1 = none; 0 = none.
- **EX018 — Decision maker.** Who makes the final notification decision? *Rubric:* 3 = Mark as data controller; 2 = partial; 1 = none; 0 = none.
- **EX019 — Unsafe testing.** What did Leila avoid doing? *Rubric:* 3 = guessing links or outside tools; 2 = partial; 1 = none; 0 = none.
- **EX020 — Shared login.** Why replace the reception login? *Rubric:* 3 = logs show who did what; 2 = partial; 1 = none; 0 = none.
- **EX021 — Hardware keys.** How were staff without smartphones handled? *Rubric:* 3 = hardware keys; 2 = partial; 1 = none; 0 = none.
- **EX022 — Log deletion.** Why must the log be kept? *Rubric:* 3 = it is evidence; 2 = partial; 1 = none; 0 = none.
- **EX023 — Order of work.** Why export before changing more settings? *Rubric:* 3 = changes can erase the record; 2 = partial; 1 = none; 0 = none.
- **EX024 — Scope limit.** Which services does Leila review? *Rubric:* 3 = Oakfield's own only; 2 = partial; 1 = none; 0 = none.
- **EX025 — Risk record.** What does Leila record for data protection? *Rubric:* 3 = what happened, who affected, why low risk; 2 = two; 1 = one; 0 = none.
- **EX026 — Written confirmation.** Why confirm authority in writing? *Rubric:* 3 = clear limits, protection; 2 = partial; 1 = none; 0 = none.

### Synthesis

Work within authority, keep evidence, and avoid risky shortcuts.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Cloud and container security: systems, data and dependencies

### Learning outcomes

You will (1) list the clinic's data and where it is shared; (2) check sharing against a simple policy; (3) understand the booking container's dependencies.

### 3.1 A simple policy

Leila writes a one-line rule: sensitive items may be shared only with staff or administrators; non-sensitive items may also be public. Patient letters, referrals, invoices, backups and the booking app configuration count as sensitive.

### 3.2 Checking every item

The April problem might not be the only one, so she checks every top-level item in storage against the rule.

### Lab — Lab — sharing check

```python
"""List synthetic cloud storage items shared more widely than policy allows (stdlib only)."""
items = [("patient-letters/", "anyone-with-link", True), ("rota.xlsx", "staff", False), ("price-list.pdf", "public", False),
         ("referrals/", "staff", True), ("invoices/", "anyone-with-link", True), ("logo.png", "public", False),
         ("old-backup.zip", "anyone-with-link", True), ("booking-app-config", "admins", True)]
allowed = {True: {"staff", "admins"}, False: {"staff", "admins", "public"}}
bad = [(n, s) for n, s, sens in items if s not in allowed[sens]]
print(f"items {len(items)}, sensitive {sum(1 for i in items if i[2])}, shared too widely {len(bad)}")
for n, s in bad: print(f"  {n}: {s}")
```

Run with `python3 lab_sharing.py`. Verified output:

```text
items 8, sensitive 5, shared too widely 3
  patient-letters/: anyone-with-link
  invoices/: anyone-with-link
  old-backup.zip: anyone-with-link
```

### 3.3 Reading the result

Of 8 items, 5 are sensitive and 3 are shared too widely: patient-letters (already fixed in chapter 1, still in the April export), invoices and old-backup.zip, all set to anyone-with-link.

### 3.4 Acting

Invoices are set to staff-only. The old backup, from a previous system, is no longer needed; after checking with Mark and noting the clinic's retention rules, Leila deletes it. Fewer copies mean less to protect.

### 3.5 The booking container

Leila asks the developer which base image the booking app uses and how often it is rebuilt. The answer is an older image last rebuilt a year ago. NIST SP 800-190 advises rebuilding images regularly from maintained bases and using trusted registries; Shu et al. (2017) found many public images carried known vulnerabilities.

### 3.6 Agreement with the developer

They agree on a monthly rebuild from a maintained base, with the developer sending a one-line confirmation each time.

### 3.7 Secrets

The booking app's configuration contains a database password. The developer moves it into the platform's secret settings, following the Kubernetes good-practice idea of keeping secrets out of images and files.

### Worked example

Leila asks whether the booking app must run on Kubernetes. The developer explains it runs on a simpler hosted platform, but the same ideas apply: trusted images, regular rebuilds, secrets kept separately and least privilege.

> **Synthetic case.** Synthetic.

### Errors and limits

A one-off check finds today's problems; only a routine finds tomorrow's.

### Exercises

- **EX027 — Policy rule.** State Leila's sharing rule. *Rubric:* 3 = sensitive only staff/admins; non-sensitive may be public; 2 = partial; 1 = none; 0 = none.
- **EX028 — Lab result.** Which items were shared too widely? *Rubric:* 3 = patient-letters, invoices, old-backup; 2 = two; 1 = one; 0 = none.
- **EX029 — Sensitive count.** How many items were sensitive? *Rubric:* 3 = 5; 2 = partial; 1 = none; 0 = none.
- **EX030 — Backup decision.** What was done with the old backup and why? *Rubric:* 3 = deleted after checking retention; fewer copies; 2 = partial; 1 = none; 0 = none.
- **EX031 — Image age.** What did the developer reveal about the image? *Rubric:* 3 = old, rebuilt a year ago; 2 = partial; 1 = none; 0 = none.
- **EX032 — Rebuild agreement.** What rebuild schedule was agreed? *Rubric:* 3 = monthly with confirmation; 2 = partial; 1 = none; 0 = none.
- **EX033 — Password move.** Where did the database password go? *Rubric:* 3 = platform secret settings; 2 = partial; 1 = none; 0 = none.
- **EX034 — Public images.** What did Shu et al. (2017) find? *Rubric:* 3 = many public images had known vulnerabilities; 2 = partial; 1 = none; 0 = none.
- **EX035 — Platform question.** Do the ideas apply without Kubernetes? *Rubric:* 3 = yes: images, rebuilds, secrets, least privilege; 2 = partial; 1 = none; 0 = none.
- **EX036 — Why check all.** Why check every item, not just the reported folder? *Rubric:* 3 = other problems may exist; 2 = partial; 1 = none; 0 = none.
- **EX037 — One-off limit.** What can a one-off check not do? *Rubric:* 3 = find future problems; 2 = partial; 1 = none; 0 = none.
- **EX038 — Container guidance.** Which NIST publication covers container images? *Rubric:* 3 = SP 800-190; 2 = partial; 1 = none; 0 = none.

### Synthesis

Check every item against a simple rule and agree how dependencies stay current.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Cloud and container security: guided lab and applied synthesis

### Learning outcomes

You will (1) set up a monthly routine; (2) measure it over three months; (3) bring the course together.

### 4.1 The routine

Ben helps Leila write six monthly tasks: review sharing links, check admin accounts and multi-factor authentication, check that a backup can be restored, confirm the booking app image was rebuilt, review leavers' access, and read the providers' security notices.

### 4.2 Why these six

Each task matches something that went wrong or nearly did: sharing, accounts, backups, the old image, leavers and changes announced by providers.

### Lab — Lab — routine record

```python
"""Score a synthetic monthly cloud security routine over three months (stdlib only)."""
tasks = ["review sharing links", "check admin accounts and MFA", "check backups restored", "update booking app image",
         "review access of leavers", "read provider security notices"]
months = {"May": [1, 1, 0, 0, 1, 0], "June": [1, 1, 1, 0, 1, 1], "July": [1, 1, 1, 1, 1, 1]}
for m, done in months.items():
    miss = [t for t, d in zip(tasks, done) if not d]
    print(f"{m}: {sum(done)}/{len(tasks)} done" + (f"; missed: {', '.join(miss)}" if miss else ""))
```

Run with `python3 lab_routine.py`. Verified output:

```text
May: 3/6 done; missed: check backups restored, update booking app image, read provider security notices
June: 5/6 done; missed: update booking app image
July: 6/6 done
```

### 4.3 Reading the result

May: 3 of 6 tasks done; missed backup restore, image update and reading notices. June: 5 of 6; the image update was still missing. July: 6 of 6.

### 4.4 Fixing the gaps

The backup restore was missed in May because nobody knew how; Leila practises in June with a test folder. The image update was late because the developer was on holiday; they agree a backup contact.

### 4.5 Keeping it light

The routine takes about an hour a month. Leila books it in the calendar for the first Monday.

### 4.6 Course synthesis

In one month Leila moved from a forwarded link to a working routine: understand what the clinic controls, work within authority, keep evidence, check everything against a simple rule, keep dependencies current and repeat monthly.

### 4.7 Further steps

The CIS Benchmarks and CSA CCM v4 are more detailed than a small clinic needs now, but Leila keeps them as references if Oakfield grows.

### Recording

Each month's results are kept on the one-page log.

### Worked example

Mark asks how he will know the routine continues if Leila is on leave. She writes the six tasks with instructions on one page and trains the deputy manager, who completes August's routine with Leila watching.

> **Synthetic case.** Synthetic.

### Errors and limits

Routines decay when one person holds them; share and record them.

### Exercises

- **EX039 — Six tasks.** List the six monthly tasks. *Rubric:* 3 = sharing, admin/MFA, backup restore, image update, leavers, notices; 2 = five; 1 = three; 0 = none.
- **EX040 — Task origins.** Why were these six tasks chosen? *Rubric:* 3 = each matches a real or near problem; 2 = partial; 1 = none; 0 = none.
- **EX041 — Lab trend.** Give the three monthly results. *Rubric:* 3 = 3/6, 5/6, 6/6; 2 = partial; 1 = none; 0 = none.
- **EX042 — May gap.** Why was the restore missed in May? *Rubric:* 3 = nobody knew how; 2 = partial; 1 = none; 0 = none.
- **EX043 — Image delay.** What caused the late image update and the fix? *Rubric:* 3 = developer holiday; backup contact; 2 = partial; 1 = none; 0 = none.
- **EX044 — Time cost.** How long does the routine take? *Rubric:* 3 = about an hour a month; 2 = partial; 1 = none; 0 = none.
- **EX045 — Scheduling.** When is the routine done? *Rubric:* 3 = first Monday; 2 = partial; 1 = none; 0 = none.
- **EX046 — Course arc.** Summarise the course in one sentence. *Rubric:* 3 = understand, authority, evidence, check, dependencies, repeat; 2 = partial; 1 = none; 0 = none.
- **EX047 — References.** Why keep CIS and CCM v4 as references? *Rubric:* 3 = for growth later; 2 = partial; 1 = none; 0 = none.
- **EX048 — Continuity.** How was continuity ensured? *Rubric:* 3 = one-page instructions, trained deputy; 2 = partial; 1 = none; 0 = none.
- **EX049 — Deputy result.** What did the deputy do in August? *Rubric:* 3 = completed routine with Leila watching; 2 = partial; 1 = none; 0 = none.
- **EX050 — Decay risk.** Why do routines decay? *Rubric:* 3 = one person holds them; 2 = partial; 1 = none; 0 = none.

### Synthesis

A light, shared monthly routine keeps a small organisation's cloud security from drifting.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Leila Ahmadi, Ben Hartley, Oakfield Physiotherapy, Westbrook Community College and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A forwarded link to a patient's letter opened without any login.

**EX002.** Cloud storage, email and the hosted platform running the booking app.

**EX003.** The app inherits flaws in the base image it was built on.

**EX004.** The clinic's side: it controls sharing settings.

**EX005.** Fix sensitive sharing today, MFA this week, agree container updates with the developer.

**EX006.** Date, reason and owner.

**EX007.** Gather evidence first and consult data protection guidance.

**EX008.** No; all services are provider-managed.

**EX009.** NIST SP 800-145.

**EX010.** A small clinic must start with the most important changes.

**EX011.** A review looking for similar problems elsewhere.

**EX012.** Its own infrastructure.

**EX013.** The patient letters folder to staff-only.

**EX014.** Mark Ellis, the clinic owner.

**EX015.** The sharing report and the folder's activity log.

**EX016.** A colleague shared a letter with a hospital in January.

**EX017.** Four views: three from the hospital, one the patient's forwarded view.

**EX018.** Mark, as data controller.

**EX019.** Guessing addresses or using outside tools to test links.

**EX020.** So logs show which person did what.

**EX021.** They received hardware keys.

**EX022.** It is the evidence of what happened.

**EX023.** Changes can erase the record of exposure.

**EX024.** Only Oakfield's own services.

**EX025.** What happened, who was affected and why she judges the risk low.

**EX026.** It makes limits clear and protects everyone.

**EX027.** Sensitive items only to staff or administrators; non-sensitive may also be public.

**EX028.** Patient-letters, invoices and old-backup.zip.

**EX029.** Five.

**EX030.** Deleted after checking retention rules, since fewer copies mean less to protect.

**EX031.** An older base image last rebuilt a year ago.

**EX032.** Monthly rebuilds with a one-line confirmation.

**EX033.** Into the platform's secret settings.

**EX034.** Many public images carried known vulnerabilities.

**EX035.** Yes: trusted images, rebuilds, separate secrets and least privilege.

**EX036.** Other items might have the same problem.

**EX037.** Find problems that appear later.

**EX038.** NIST SP 800-190.

**EX039.** Sharing review, admin and MFA check, backup restore, image update, leavers' access, provider notices.

**EX040.** Each matches something that went wrong or nearly did.

**EX041.** May 3/6, June 5/6, July 6/6.

**EX042.** Nobody knew how to do it.

**EX043.** The developer's holiday; a backup contact was agreed.

**EX044.** About an hour a month.

**EX045.** The first Monday of each month.

**EX046.** Understand control, work within authority, keep evidence, check against a rule, keep dependencies current, repeat monthly.

**EX047.** They are more detailed than needed now but useful if Oakfield grows.

**EX048.** One-page instructions and a trained deputy manager.

**EX049.** Completed the routine with Leila watching.

**EX050.** When only one person holds them.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Amazon Web Services. (n.d.). *Shared responsibility model*. <https://aws.amazon.com/compliance/shared-responsibility-model/>
- Armbrust, M., Fox, A., Griffith, R., Joseph, A. D., Katz, R., Konwinski, A., Lee, G., Patterson, D., Rabkin, A., Stoica, I., & Zaharia, M. (2010). A view of cloud computing. *Communications of the ACM*, 53(4), 50–58. <https://doi.org/10.1145/1721654.1721672>
- Burns, B., Grant, B., Oppenheimer, D., Brewer, E., & Wilkes, J. (2016). Borg, Omega, and Kubernetes. *Communications of the ACM*, 59(5), 50–57. <https://doi.org/10.1145/2890784>
- Center for Internet Security. (n.d.). *CIS Benchmarks*. <https://www.cisecurity.org/cis-benchmarks>
- Cloud Security Alliance. (2021). *Cloud Controls Matrix (CCM) v4*. <https://cloudsecurityalliance.org/research/cloud-controls-matrix>
- Google Cloud. (n.d.). *Shared responsibilities and shared fate on Google Cloud*. <https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate>
- Hu, V. C., Iorga, M., Bao, W., Li, A., Li, Q., & Gouglidis, A. (2020). *General access control guidance for cloud systems* (NIST SP 800-210). NIST. <https://doi.org/10.6028/NIST.SP.800-210>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Kubernetes Authors. (n.d.). *Pod Security Standards*. <https://kubernetes.io/docs/concepts/security/pod-security-standards/>
- Kubernetes Authors. (n.d.). *Using RBAC authorization*. <https://kubernetes.io/docs/reference/access-authn-authz/rbac/>
- Kubernetes Authors. (n.d.). *Network policies*. <https://kubernetes.io/docs/concepts/services-networking/network-policies/>
- Kubernetes Authors. (n.d.). *Good practices for Kubernetes Secrets*. <https://kubernetes.io/docs/concepts/security/secrets-good-practices/>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Mell, P., & Grance, T. (2011). *The NIST definition of cloud computing* (NIST SP 800-145). NIST. <https://doi.org/10.6028/NIST.SP.800-145>
- Microsoft. (n.d.). *Shared responsibility in the cloud*. <https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility>
- Rahman, A., Parnin, C., & Williams, L. (2019). The seven sins: Security smells in infrastructure as code scripts. *41st International Conference on Software Engineering (ICSE)*, 164–175. <https://doi.org/10.1109/ICSE.2019.00033>
- Ristenpart, T., Tromer, E., Shacham, H., & Savage, S. (2009). Hey, you, get off of my cloud: Exploring information leakage in third-party compute clouds. *16th ACM Conference on Computer and Communications Security (CCS '09)*, 199–212. <https://doi.org/10.1145/1653662.1653687>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Sandhu, R. S., Coyne, E. J., Feinstein, H. L., & Youman, C. E. (1996). Role-based access control models. *Computer*, 29(2), 38–47. <https://doi.org/10.1109/2.485845>
- Shu, R., Gu, X., & Enck, W. (2017). A study of security vulnerabilities on Docker Hub. *7th ACM Conference on Data and Application Security and Privacy (CODASPY '17)*, 269–280. <https://doi.org/10.1145/3029806.3029832>
- Souppaya, M., Morello, J., & Scarfone, K. (2017). *Application container security guide* (NIST SP 800-190). NIST. <https://doi.org/10.6028/NIST.SP.800-190>
- Verma, A., Pedrosa, L., Korupolu, M., Oppenheimer, D., Tune, E., & Wilkes, J. (2015). Large-scale cluster management at Google with Borg. *10th European Conference on Computer Systems (EuroSys '15)*, 1–17. <https://doi.org/10.1145/2741948.2741964>
