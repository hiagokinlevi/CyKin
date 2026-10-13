# Application and Software Supply Chain Security: Technical Course

- Language: English (`en`); course 060, Technical course (18 months).
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical course students learning to install, verify, configure and monitor third-party web components safely in a hosting support role.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: test and review only software you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic code and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one support technician at a hosting company from a plugin installed from an unverified mirror, through foundations, the supply chain model, telemetry, failure modes, inventory, configuration, verification, contained labs, troubleshooting, automation, dependencies and documentation, to a supervised project. Run each lab where it appears, attempt the four exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Tomás Rivera** | Technical course student and support technician | Invented |
| **Grace Okafor** | Support supervisor | Invented |
| **Pinecrest Hosting** | Fictional hosting company | Invented |
| **Eastbank Technical College** | Fictional college | Invented |
| **Ferncroft Books** | Fictional customer shop | Invented |

### Core sources

[OWASP Top 10:2021](https://owasp.org/Top10/); OWASP [ASVS](https://owasp.org/www-project-application-security-verification-standard/) 4.0.3 and 5.0.0; OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/) and [SAMM](https://owaspsamm.org/); NIST [SP 800-218 (SSDF)](https://doi.org/10.6028/NIST.SP.800-218); [CWE Top 25](https://cwe.mitre.org/top25/); [SLSA v1.0](https://slsa.dev/spec/v1.0/); Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) describe how a hosted customer website is built from servers, web software, databases and plugins; (2) identify who is responsible for each part; (3) place the opening case in that picture; (4) name the supply chain behind a site.

### 1.1 The opening case

Tomás Rivera is a technical course student at the fictional Eastbank Technical College, working part-time as a support technician at the fictional Pinecrest Hosting under supervisor Grace Okafor. A customer, Ferncroft Books, asked support to install an image-resize plugin. A previous technician had downloaded it from a mirror site because the vendor's page was slow. Weeks later the shop began showing strange redirects. The mirror copy turned out to differ from the official release. The case gives every later chapter its starting point and its first piece of evidence.

### 1.2 Parts of a hosted site

A customer site runs on a server managed by Pinecrest. Web server software receives requests, the shop application builds pages, a database stores products and orders, and plugins add features such as image resizing, contact forms and galleries. Each part comes from somewhere: an operating system vendor, a web server project, the shop application's maintainers and plugin authors. For Ferncroft Books, the resize plugin is the part that touched product images, which is why its source later matters so much.

### 1.3 Shared responsibility

Pinecrest is responsible for servers, operating system updates and the hosting control panel. Customers choose plugins and content. Support staff who install plugins for customers take on part of that responsibility, which is why their installation steps matter. In Ferncroft's case, the customer chose the resize plugin, but a Pinecrest technician downloaded and installed it. That split makes the mirror download a support problem, not only a customer choice. Grace treats it that way, which is why the later rules on sources and hashes apply to every plugin support installs, whoever requested it.

### 1.4 The supply chain behind a site

Everything a site runs was written by someone else and delivered through downloads, updates and registries. NIST SP 800-218 (SSDF) and SLSA v1.0 describe how software producers should protect that chain; consumers like Pinecrest must check what they receive. Ferncroft's site shows how short the gap can be between a producer's good practice and a consumer's mistake. The resize plugin's vendor published an official release, yet the copy installed came from a mirror. No producer practice can help a consumer who never fetches the producer's file or compares it with the published hash.

### 1.5 Requests and responses

A visitor's browser sends a request; the web server passes it to the application, which may call plugins and the database, then returns a page. Problems in any plugin can affect every page it touches. At Ferncroft, the resize plugin runs whenever a product image page is requested, so a change in that plugin shows up on exactly those pages. That is why customers saw redirects on image pages while other pages loaded normally. Tracing a request through its parts tells Tomás which component to suspect first.

### 1.6 Why this course

The course teaches Tomás to check what is installed, where it came from, how it is configured and how to notice when something goes wrong. Each of those four questions became a gap in the Ferncroft case: nobody had a list of installed plugins, the source was a mirror, the plugin folder was writable, and redirects ran for weeks before anyone noticed. The chapters that follow take those gaps one at a time and turn each into a routine.

### Worked example

Tomás draws Ferncroft's site as boxes: server, web server, shop application, database, and four plugins with their sources. Only the resize plugin's source is marked "mirror, unverified". Grace pins the drawing above the support desk as a reminder that every box has a source worth checking.

> **Synthetic case.** Ferncroft Books, Pinecrest Hosting and all events are synthetic.

### Errors and limits

A diagram simplifies; real sites often hide extra parts such as scheduled tasks or old plugins.

### Exercises

- **EX001 — Site parts.** List the main parts of a hosted customer site. *Rubric:* 3 = server, web server, application, database, plugins; 2 = three; 1 = one; 0 = none.
- **EX002 — Pinecrest's share.** What is Pinecrest responsible for? *Rubric:* 3 = servers, OS updates, control panel; 2 = two; 1 = one; 0 = none.
- **EX003 — Support's share.** Why do support staff's installation steps matter? *Rubric:* 3 = they take on part of responsibility for plugins; 2 = partial; 1 = none; 0 = none.
- **EX004 — Unverified box.** Which box in Tomás's drawing was marked unverified? *Rubric:* 3 = the resize plugin from a mirror; 2 = partial; 1 = none; 0 = none.

### Synthesis

Every part of a site has a source; know them all.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) explain how visitors reach a site over HTTPS; (2) describe DNS, ports and certificates at a practical level; (3) recognise redirects and their risks; (4) read basic request details in support cases.

### 2.1 Reaching a site

The visitor's device asks DNS for the site's address, connects to port 443, checks the site's certificate and then exchanges encrypted HTTP requests. Each step can fail or be misused, and support technicians often need to tell which step a problem belongs to. Ferncroft's problem sat at the last step, inside the HTTP response, but Tomás still checks the earlier steps. A changed DNS record or a broken certificate can also send visitors somewhere unexpected. Knowing the order lets him rule out each step quickly before blaming the plugin.

### 2.2 Certificates

A certificate proves the server holds the site's name. Pinecrest renews certificates automatically; expired certificates cause browser warnings that customers report as "the site is broken". Because renewal is automatic, an expired certificate usually means the renewal job failed rather than that someone forgot. Tomás checks the certificate's expiry date in the browser before anything else when a customer reports warnings. A valid certificate also rules out one explanation for strange behaviour, which helped narrow the Ferncroft redirects to the site itself.

### 2.3 HTTP basics

Requests have a method (GET, POST), a path and headers; responses have a status code: 200 success, 301/302 redirect, 401 needs sign-in, 404 not found, 500 server error. Knowing these codes lets Tomás read logs and customer screenshots quickly. In the Ferncroft screenshots, the status code 302 on image pages was the first technical clue. In the log lab later, the 401 lines on /admin and the 500 lines on /shop tell two different stories from the same file. A 302 alone is normal for http-to-https moves, so the destination domain is what Tomás reads next.

### 2.4 Redirects

Redirects are normal, for example from http to https. Unexpected redirects to other domains, as Ferncroft's visitors saw, usually mean something on the site has been changed and must be investigated rather than worked around. Working around an unexpected redirect, for example by clearing a cache and closing the ticket, would hide the evidence and leave visitors exposed. At Ferncroft, the 302 from image pages to an unknown domain was the visible effect of the changed mirror copy, and only investigation found that cause.

### 2.5 Ports and firewalls

Customer servers accept only web traffic publicly; administration uses Pinecrest's private network and multi-factor sign-in. Keeping administration off the public internet means a visitor can reach the shop but not the server's management interfaces. For Ferncroft, this limited what an outsider could do directly. The redirect came from code the site itself was running, installed by support, rather than from someone breaking into the server's administration. Multi-factor sign-in on the private network means a stolen staff password alone does not open a customer server's administration.

### 2.6 Customer conversations

Tomás learns to ask precise questions: which page, which time, what the browser showed, and whether others see it too. Precise questions save time and avoid guessing. 'The site is broken' could mean an expired certificate, a slow page or a redirect. For Ferncroft, asking which page and what the browser showed produced three screenshots, all of a 302 redirect from product image pages, which pointed straight at image handling. He writes the answers into the ticket, so the security team sees the same facts without asking the customer again.

### DNS checks

When redirects appear, Tomás also confirms the site's DNS records still point at Pinecrest, ruling out a changed domain setting.

### Worked example

For the Ferncroft case, Tomás collects three customer screenshots. All show a 302 redirect from the product image page to an unknown domain, while other pages load normally. That narrows the problem to image handling, the resize plugin's job, and Grace escalates it to the security team.

> **Synthetic case.** Domains and screenshots are synthetic.

### Errors and limits

A redirect can also come from DNS or caching changes; check those too before concluding.

### Exercises

- **EX005 — Connection steps.** What steps happen before an HTTPS page loads? *Rubric:* 3 = DNS, connect 443, certificate check, encrypted requests; 2 = three; 1 = one; 0 = none.
- **EX006 — Status codes.** What do 302, 401 and 500 mean? *Rubric:* 3 = redirect, needs sign-in, server error; 2 = two; 1 = one; 0 = none.
- **EX007 — Unexpected redirect.** Why are unexpected redirects investigated? *Rubric:* 3 = usually mean site was changed; 2 = partial; 1 = none; 0 = none.
- **EX008 — Narrowing.** How did screenshots narrow the Ferncroft problem? *Rubric:* 3 = only image page redirected; resize plugin; 2 = partial; 1 = none; 0 = none.

### Synthesis

Knowing protocols lets support narrow problems fast.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) describe user accounts and file permissions on a web server; (2) apply least privilege to sites and staff; (3) manage support access safely; (4) recognise risky permission settings.

### 3.1 Accounts on the server

Each customer site runs under its own operating system user, so one site cannot read another's files. The web server process can read site files and write only to upload and cache folders. Separate users mean the Ferncroft problem stayed inside Ferncroft's site rather than spreading to other customers on the same server. The web server's write access is limited to uploads and cache, so normal visitors cannot change code. When that limit is broken, as it was at Ferncroft, the protection weakens.

### 3.2 File permissions

Plugin and application code should not be writable by the web server process. If it is, a flaw in any plugin could let changed code be written into the site, which is one way unexpected redirects appear. At Ferncroft, the plugin folder was writable by the web server, a leftover from the mirror installation. That setting did not cause the redirect by itself, since the mirror copy already carried it. It did mean that any plugin flaw could have let further changes be written to the site.

### 3.3 Staff identities

Support technicians sign in with personal accounts and multi-factor authentication. They have temporary access to a customer site only while a ticket is open, granted by the ticket system and removed when it closes. Tying access to an open ticket means Tomás could work on Ferncroft's site only while the redirect ticket was open. When the ticket closed, the access ended without anyone having to remember to remove it. The session log then shows exactly who worked on the site and when.

### 3.4 Customer identities

Customers manage their own shop administrators. Pinecrest advises unique accounts for each staff member and removing accounts when staff leave. OWASP Top 10:2021 A07 covers authentication failures. Shared administrator accounts make it impossible to tell who did what. At Ferncroft, Tomás found two administrator accounts belonging to former shop staff, which were removed with the customer's agreement. Pinecrest cannot know who has left a customer's business, so the yearly reminder asks customers to check their own lists. OWASP A07 lists weak and shared credentials among authentication failures, which matches what Pinecrest asks customers to avoid.

### 3.5 Checking permissions

A support script lists files writable by the web server outside the permitted folders. The script reads permissions and prints a list; it changes nothing. On Ferncroft's site it found the plugin folder writable by the web server. Running it weekly through the nightly job later turns a one-off discovery into a routine check that catches the same mistake on other sites before it causes harm. The permitted folders, uploads and cache, are listed in the script itself so reviewers can check them.

### 3.6 Records

Every support session is logged with the technician, ticket and time. Each log entry names the technician, the ticket and the time, so any change on a customer site can be traced to a person and a reason. For Ferncroft, the logs would show which technician installed the resize plugin and when, which mattered when the cause of the redirects was being reconstructed. Grace samples these logs during her monthly reviews to confirm that each session matched an open ticket.

### Removing old accounts

Tomás also lists shop administrator accounts on Ferncroft's site and finds two belonging to former shop staff. With the customer's agreement, they are removed. Grace adds a yearly reminder to customers to review their own administrator lists, since Pinecrest cannot know who has left a customer's business.

### Worked example

Running the permission check on Ferncroft's site shows the plugin folder writable by the web server, a leftover from the mirror installation. Tomás reports it; the security team restores correct permissions after taking a copy for investigation.

> **Synthetic case.** Accounts and findings are synthetic.

### Errors and limits

Correct permissions limit damage but do not fix a flawed plugin.

### Exercises

- **EX009 — Site isolation.** How are customer sites kept apart? *Rubric:* 3 = own OS user each; 2 = partial; 1 = none; 0 = none.
- **EX010 — Writable code.** Why should code not be writable by the web server? *Rubric:* 3 = a flaw could write changed code; 2 = partial; 1 = none; 0 = none.
- **EX011 — Support access.** How is support access limited? *Rubric:* 3 = temporary, per open ticket; 2 = partial; 1 = none; 0 = none.
- **EX012 — Ferncroft permission.** What permission problem was found? *Rubric:* 3 = plugin folder writable by web server; 2 = partial; 1 = none; 0 = none.

### Synthesis

Least privilege for sites and staff limits harm.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) compute and compare file hashes; (2) read simple JSON and CSV records; (3) write small safe stdlib scripts; (4) verify downloads before installing.

### 4.1 Hashes

A cryptographic hash such as SHA-256 is a short fingerprint of a file. Any change to the file, even one byte, produces a completely different hash. Vendors publish hashes so users can check a download is exactly the released file. For Ferncroft, the vendor's published hash for resize-plugin 2.4.1 would have differed from the mirror copy's hash. Checking takes less than a minute, while the redirects ran for weeks. The vendor's hash for resize-plugin 2.4.1 is exactly what the lab below compares against each downloaded copy.

### Lab — download verification

```python
"""Verify synthetic downloaded files against a published SHA-256 manifest (stdlib only)."""
import hashlib
files = {  # synthetic file contents
    "resize-plugin-2.4.1.zip": b"synthetic resize plugin 2.4.1 official",
    "gallery-plugin-1.8.0.zip": b"synthetic gallery plugin 1.8.0 official",
    "resize-plugin-2.4.1-mirror.zip": b"synthetic resize plugin 2.4.1 modified",
}
manifest = {  # published by the synthetic vendor
    "resize-plugin-2.4.1": hashlib.sha256(files["resize-plugin-2.4.1.zip"]).hexdigest(),
    "gallery-plugin-1.8.0": hashlib.sha256(files["gallery-plugin-1.8.0.zip"]).hexdigest(),
}
for name, data in files.items():
    key = name.replace("-mirror", "").removesuffix(".zip")
    got = hashlib.sha256(data).hexdigest()
    status = "MATCH" if manifest.get(key) == got else "MISMATCH - do not install"
    print(f"{name:32} {got[:12]}  {status}")
```

Run with `python3 lab_hash.py`. Verified output:

```text
resize-plugin-2.4.1.zip          e85dc388d054  MATCH
gallery-plugin-1.8.0.zip         80324825a8be  MATCH
resize-plugin-2.4.1-mirror.zip   5af89d46d94f  MISMATCH - do not install
```

### 4.2 Lab result

The official resize-plugin-2.4.1.zip and gallery-plugin-1.8.0.zip match the vendor manifest. resize-plugin-2.4.1-mirror.zip has a different hash (beginning 5af89d46d94f) and is reported as MISMATCH - do not install. This is exactly the check that would have stopped the Ferncroft installation. The lab compares full hashes even though it prints only the first twelve characters. A mismatch is never a judgment call: the file is not the released one, whatever the mirror claims about it. Grace's new ticket field later records this result for every installation that support performs.

### 4.3 Where hashes come from

A hash is only useful if it comes from a trusted source, such as the vendor's own site over HTTPS or a signed release. A hash published next to a file on the same mirror proves nothing, because whoever changed the file could change the hash too. For the resize plugin, the trusted source is the vendor's release page reached over HTTPS, not the mirror where the previous technician downloaded the file. Grace's new ticket field records where the hash came from, so a reviewer can check that the source was the vendor's own page.

### 4.4 Data formats

Manifests and advisories are often JSON or CSV. Python's json and csv modules read them safely without extra packages. Reading these formats with the standard library avoids installing extra packages on support machines. The same json and csv modules later read the advisory feeds and the nightly inventory CSV, so Tomás learns one set of tools that he uses throughout the course and in the nightly job. Reading a file never runs code from it, which keeps these scripts safe on support machines.

### 4.5 Safe scripts

Support scripts only read data and print results; any change to a customer site goes through a ticket. A read-only script cannot damage a customer site even if it contains a bug. The download-verification lab follows this rule: it computes hashes and prints MATCH or MISMATCH, but installing or rejecting the file is a decision recorded in the ticket. The nightly job built in Chapter 14 later keeps exactly the same read-only rule. Separating reading from changing also lets new technicians run the scripts without extra permissions.

### Reading the script

The lab computes each file's SHA-256 with hashlib and compares it to the manifest entry for the release name. It prints only the first twelve characters for readability, but compares the full value.

### Worked example

Grace makes hash verification a required step: the support ticket for a plugin installation now has a field for the vendor hash source and the computed hash. In the first month, the step catches one more mismatched download from a slow mirror.

> **Synthetic case.** Files and hashes are synthetic.

### Errors and limits

A matching hash proves the file is the released one, not that the release is free of flaws.

### Exercises

- **EX013 — Lab result.** Which file failed and what does the lab advise? *Rubric:* 3 = mirror zip; do not install; 2 = partial; 1 = none; 0 = none.
- **EX014 — Hash source.** Why must the hash come from a trusted source? *Rubric:* 3 = attacker could change both; 2 = partial; 1 = none; 0 = none.
- **EX015 — What a match proves.** What does a matching hash prove? *Rubric:* 3 = file is the released one, not flawless; 2 = partial; 1 = none; 0 = none.
- **EX016 — New step.** What did Grace add to the ticket? *Rubric:* 3 = hash source and computed hash fields; 2 = partial; 1 = none; 0 = none.

### Synthesis

Verify downloads against trusted hashes before installing.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) define the scope of a support or security task; (2) collect evidence carefully; (3) record the chain of handling; (4) stay within authorisation.

### 5.1 Scope

Every task has a scope: which customer, which systems, what actions are allowed. Tomás works only on systems named in the ticket, with the customer's consent recorded. For Ferncroft, the ticket named the customer's site, the resize plugin and its files, the server logs and the permission check. Looking at other customers' sites that ran the same plugin needed a separate ticket and approval, even though the risk seemed similar. The consent recorded in the ticket is what lets Tomás copy Ferncroft's logs and files at all.

### 5.2 Evidence

In the Ferncroft case, evidence includes the plugin files, their hashes, server logs, the permission listing and customer screenshots. Evidence is copied before anything is changed. Copying first matters because the security team restored correct permissions on the plugin folder. Had they done so before taking a copy, the evidence that the folder was writable would have been lost. Grace's review counted seven evidence items for Ferncroft, each with its hash and the time it was collected. Screenshots from customers count as evidence too, so they are saved with their dates.

### 5.3 Recording handling

Each item has a note: what it is, who collected it, when, and its hash. This lets others trust that the evidence was not altered. The hash in the note is what makes later trust possible. If the security team computes the same hash on the plugin copy weeks later, they know it is the file Tomás collected. A missing time or collector name would leave a gap that a customer or reviewer could reasonably question. The notes travel with the files, so a copy without its note is treated as unverified.

### 5.4 Authorisation

Investigating beyond scope, such as looking at another customer's site "just in case", needs a new ticket and approval. The temptation is real when the same resize plugin might be installed elsewhere. Yet another customer's site belongs to that customer, and their consent is not in the Ferncroft ticket. A new ticket records the reason and approval, and the inventory built in Chapter 9 later makes such searches routine and authorised. Approval comes from Grace or the security team, not from the technician's own judgement of risk.

### 5.5 Privacy

Logs contain visitors' addresses; they are kept only as long as needed and shared only within the investigation. Ferncroft's server logs include addresses of shoppers who never did anything wrong. Tomás copies only the lines needed for the redirect investigation and keeps them with the evidence. The 30-day retention used for web logs at Pinecrest sets the default, and training examples use documentation addresses instead of real ones. Lines kept as evidence follow the case's retention period and are deleted with the rest of it.

### 5.6 Handing over

Tomás passes evidence to the security team with the notes, and keeps working on customer communication. Handing over with the notes means the security team does not need to ask Tomás what each file is. His continued role in customer communication keeps one person responsible for what Ferncroft hears. The split also keeps the investigation separate from support work that must continue meanwhile. Tomás's customer messages are reviewed by Grace before they are sent to Ferncroft's owner.

### Customer communication

Evidence also supports what Pinecrest tells the customer. Tomás drafts a plain message for Grace to review: what visitors saw, what was found, what has been fixed, and what Ferncroft should do, such as changing administrator passwords as a precaution. The message avoids guesses and states only what the evidence shows. When the investigation later confirms the cause, a short follow-up explains it, and the customer thanks support for the clear updates.

### Retention

Evidence is kept for the agreed period, then deleted.

### Worked example

Grace reviews Tomás's evidence notes for Ferncroft: seven items, each with hash and time. The security team later confirms from the files that the mirror version added a redirect, and the notes support Pinecrest's message to the customer.

> **Synthetic case.** Evidence is synthetic.

### Errors and limits

Changing a system before copying evidence can destroy the facts needed later.

### Exercises

- **EX017 — Scope parts.** What defines a task's scope? *Rubric:* 3 = customer, systems, allowed actions; 2 = two; 1 = one; 0 = none.
- **EX018 — Evidence note.** What does each evidence note record? *Rubric:* 3 = what, who, when, hash; 2 = three; 1 = one; 0 = none.
- **EX019 — Beyond scope.** What is needed to look at another site? *Rubric:* 3 = new ticket and approval; 2 = partial; 1 = none; 0 = none.
- **EX020 — Before changing.** Why copy evidence before changing anything? *Rubric:* 3 = changes can destroy facts; 2 = partial; 1 = none; 0 = none.

### Synthesis

Stay in scope and handle evidence carefully.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Application and software supply chain security: system model

### Learning outcomes

You will (1) model a customer site's supply chain from vendor to running site; (2) mark where checks belong; (3) compare to SSDF and SLSA ideas; (4) use the model in support work.

### 6.1 The model

Vendor writes plugin → vendor builds and publishes release with hash → download source (vendor site, registry or mirror) → Pinecrest support downloads → verification → installation on site → updates over time. Each arrow is a place where the software could change. At Ferncroft, the change happened at the download source arrow: the mirror served a modified copy. The vendor's release and hash were fine, but nobody compared them. Drawing the arrows lets support see that a check at the verification step would have caught the problem before installation.

### 6.2 Checks on the model

At download: use official sources. At verification: compare trusted hash or signature. At installation: correct permissions. Over time: track versions against advisories and watch for unexpected changes. Applied to Ferncroft, each check matches one gap: the mirror was not an official source, nothing was verified, the code folder was writable, and no inventory existed to track the plugin over time. The model turns a single incident into four separate controls, each owned and checked later in the course. Each check later gains its own verification test, scheduled in Tomás's calendar.

### 6.3 Producer practices

The SSDF asks producers to protect code and publish integrity information; SLSA v1.0 build levels describe provenance, a record of how a release was built. When vendors provide these, consumers can verify more. Pinecrest does not build plugins, so these practices describe what it can hope to receive from vendors. A published hash, as the resize plugin's vendor provided, is the simplest form. Signatures and provenance records go further, which is why the next steps in Chapter 18 include vendor signature checks.

### 6.4 Consumer practices

Pinecrest cannot change how vendors build, but it can prefer vendors that publish hashes or signatures and keep an inventory of what is installed where. The inventory is the consumer's main tool, because Pinecrest cannot react to an advisory about a plugin it does not know it runs. Preferring verifiable vendors costs little when customers ask for a plugin, since support can suggest an equivalent with published hashes when two plugins do the same job. These two consumer practices cost little and apply to every customer site Pinecrest hosts.

### 6.5 Using the model

Support uses the model when customers ask for plugins: is the source official, can it be verified, who updates it. For each request, support asks where the official download is, whether a hash or signature is published, and who will apply updates. A plugin that fails these questions is not automatically refused, but the customer is told the risk and the reason is recorded. The Ferncroft resize plugin would have passed if downloaded officially. The answers go into the installation ticket, so later reviews can see why a plugin was accepted.

### 6.6 Gaps found

The model shows Pinecrest had no inventory of plugins across customers. Without an inventory, nobody could say which other sites ran the resize plugin, or which version, when the Ferncroft case came to light. That gap made the case harder to scope and is why the nightly inventory becomes the centre of the later chapters, starting with Chapter 9. Scoping the Ferncroft case therefore relied on asking customers one by one, which is slow and incomplete across hundreds of hosted sites.

### Model for updates

Updates follow the same path as first installations, so they need the same checks. Automatic plugin updates from the vendor's official channel are acceptable when that channel verifies integrity; manual updates repeat the hash check. The model also reminds support that removing unused plugins removes whole paths from the chain.

### Worked example

Using the model, Grace and Tomás list the Ferncroft gaps: unofficial source, no verification, writable code folder, no inventory. Each becomes a control in later chapters.

> **Synthetic case.** The model is synthetic.

### Errors and limits

A model is only useful if updated when processes change.

### Exercises

- **EX021 — Model steps.** List the model's steps. *Rubric:* 3 = vendor, publish, source, download, verify, install, update; 2 = four; 1 = two; 0 = none.
- **EX022 — Download check.** What check belongs at download? *Rubric:* 3 = official sources; 2 = partial; 1 = none; 0 = none.
- **EX023 — Consumer role.** What can Pinecrest do as a consumer? *Rubric:* 3 = prefer verifiable vendors; inventory; 2 = partial; 1 = none; 0 = none.
- **EX024 — Four gaps.** Name the four Ferncroft gaps. *Rubric:* 3 = unofficial source, no verification, writable folder, no inventory; 2 = three; 1 = one; 0 = none.

### Synthesis

Model the chain and place a check on each step.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Application and software supply chain security: data and telemetry

### Learning outcomes

You will (1) read web access logs for signs of problems; (2) summarise errors and failed sign-ins; (3) choose useful telemetry; (4) respect privacy in logs.

### 7.1 What logs show

Each request leaves a log line: time, source address, method, path and status code. Patterns in these lines show problems: bursts of errors after an update, repeated failed sign-ins to the admin page, or requests for pages that should not exist. In the lab log, the five 401 responses on /admin from one address show one pattern, and the two 500 errors on /shop show another. Reading lines one at a time misses both; counting them by hour and by source makes them visible.

### Lab — log summary

```python
"""Summarise a synthetic web access log: errors per hour and admin-page requests by source (stdlib only)."""
from collections import Counter
log = """10:02 203.0.113.5 GET /shop 200
10:05 203.0.113.9 GET /admin 302
10:07 198.51.100.7 GET /admin 401
10:07 198.51.100.7 GET /admin 401
10:08 198.51.100.7 GET /admin 401
10:08 198.51.100.7 GET /admin 401
10:09 198.51.100.7 GET /admin 401
10:15 203.0.113.5 GET /cart 200
11:01 203.0.113.12 GET /shop 500
11:02 203.0.113.12 GET /shop 500
11:20 203.0.113.5 GET /shop 200""".splitlines()
errors, admin = Counter(), Counter()
for line in log:
    t, ip, _, path, code = line.split()
    if code.startswith(("4", "5")):
        errors[t[:2]] += 1
    if path == "/admin" and code == "401":
        admin[ip] += 1
for hour, n in sorted(errors.items()):
    print(f"hour {hour}: {n} error responses")
for ip, n in admin.items():
    print(f"{ip}: {n} failed admin sign-ins" + ("  REVIEW" if n >= 5 else ""))
```

Run with `python3 lab_logs.py`. Verified output:

```text
hour 10: 5 error responses
hour 11: 2 error responses
198.51.100.7: 5 failed admin sign-ins  REVIEW
```

### 7.2 Lab result

The synthetic Ferncroft log shows 5 error responses in hour 10 and 2 in hour 11. All five hour-10 errors are failed sign-ins (401) to /admin from 198.51.100.7, which reaches the review threshold of 5. The two hour-11 errors are 500 server errors on /shop from another address, which point to an application fault rather than sign-in attempts. The summary does not say who was behind 198.51.100.7, only that it crossed the threshold. Tomás still checks with the customer before treating the address as hostile, because a staff member who forgot a password would produce the same count.

### 7.3 Choosing telemetry

Useful records for supply chain work include plugin installation and update events, file changes in code folders, error rates after updates and admin sign-ins. Pinecrest adds file-change monitoring for code folders after the Ferncroft case. File-change monitoring would have flagged Ferncroft's plugin folder had anything been written into it, and installation events would have recorded the mirror download. Error rates measured just after updates show a broken release within hours rather than days. Each record answers a question support actually asks, which keeps telemetry focused rather than collecting everything.

### 7.4 Privacy

Logs contain visitor addresses, which are personal data. They are kept for 30 days, access is limited to support and security staff, and examples in training use documentation addresses. Thirty days covers most support investigations, including the Ferncroft redirects once they were reported. Restricting access to support and security staff keeps visitor addresses away from people who do not need them. Using documentation addresses such as 198.51.100.7 in labs means training material never exposes a real visitor. Evidence copies taken for a case follow the case's retention instead.

### 7.5 From summary to action

A REVIEW line is a prompt to look further, not proof of an attack; repeated failures may be a customer who forgot a password. In the worked example, the REVIEW line for 198.51.100.7 led Tomás to ask Ferncroft whether any staff were working then; none were. That answer, not the count alone, made the failures worth acting on. A forgetful staff member would have produced the same five lines in the summary. The decision and the customer's answer are recorded in the ticket with the summary.

### Error bursts after updates

When errors rise just after a plugin update, support first suspects the update and can roll back.

### Worked example

Tomás checks the 198.51.100.7 failures with Ferncroft: no staff were working at that time. The customer turns on multi-factor sign-in for shop administrators, and the failures stop mattering because a password alone no longer signs in.

> **Synthetic case.** Logs and addresses are synthetic documentation values.

### Errors and limits

Logs only show what was recorded; missing logs leave blind spots.

### Exercises

- **EX025 — Lab hour 10.** What did hour 10 show? *Rubric:* 3 = 5 failed admin sign-ins from one address; 2 = partial; 1 = none; 0 = none.
- **EX026 — Hour 11.** What did the hour-11 errors suggest? *Rubric:* 3 = application fault, 500s; 2 = partial; 1 = none; 0 = none.
- **EX027 — New telemetry.** What monitoring did Pinecrest add? *Rubric:* 3 = file-change monitoring for code folders; 2 = partial; 1 = none; 0 = none.
- **EX028 — REVIEW meaning.** What does a REVIEW line mean? *Rubric:* 3 = prompt to look further, not proof; 2 = partial; 1 = none; 0 = none.

### Synthesis

Logs turn into useful signals when summarised and checked.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Application and software supply chain security: failure modes

### Learning outcomes

You will (1) list the ways the supply chain to a customer site can fail; (2) link each to a check; (3) recognise them in support tickets; (4) avoid blaming individuals.

### 8.1 Changed downloads

A file from an unofficial source differs from the release, as in the Ferncroft case. Check: official sources and hash verification. The Ferncroft mirror copy is this failure exactly: the file looked like resize-plugin 2.4.1 but its hash began 5af89d46d94f instead of matching the vendor's. The two checks address different moments, since an official source reduces the chance of a bad file and the hash proves the file received is the released one. Both checks now sit in the installation procedure as mandatory steps.

### 8.2 Outdated components

A plugin version with a published advisory stays installed because nobody tracks versions. Kula et al. (2018) found that developers often leave dependencies outdated. Check: inventory and advisory comparison. Without the inventory, Pinecrest could not compare installed versions with advisories at all. The advisory lab later finds alder-dental and quayside-gym running contact-form versions older than the fixed 5.1.0. Those are the kind of outdated installations that stay unnoticed when nobody tracks versions across sites. The nightly inventory makes this comparison routine instead of a rare manual task.

### 8.3 Abandoned components

A plugin's author stops maintaining it; future flaws will never be fixed. Check: review maintenance activity yearly and replace abandoned plugins. An abandoned plugin can look fine for years, then a flaw is published and no fix ever arrives. The yearly maintenance review catches this before an advisory forces a rushed replacement. The yearly review looks at recent release dates, open issues and whether security notices are answered, and replacement plugins go through the normal installation procedure with hash checks.

### 8.4 Compromised publishers

A legitimate vendor's account or build is misused to publish a harmful update. Ladisa et al. (2023) catalogue such attacks on open-source supply chains, and Ohm et al. (2020) describe harmful packages. Check: watch for unexpected changes after updates and follow vendor security notices. This failure mode differs from Ferncroft's because the harmful file would come from the vendor itself, with a matching hash. File-change monitoring and error rates after updates are the main signals support has. Following vendor security notices also tells support when a release has been withdrawn.

### 8.5 Misconfiguration

Correct software configured badly, such as writable code folders or missing security headers. Check: baseline checks. At Ferncroft the writable plugin folder was this kind of failure, and in the header lab alder-dental and quayside-gym miss baseline headers. The software itself may be correct while its settings leave it exposed. Baseline checks compare every site against the same written standard, so drift shows up as a named finding rather than a vague doubt. Fixes go through the server template where possible, so all sites benefit at once.

### 8.6 Blame-free review

Failures are treated as process problems; the technician who used the mirror followed no rule because none existed. The previous technician used the mirror because the vendor's page was slow and no rule required an official source or a hash check. Blaming that person would teach staff to hide shortcuts rather than report them. In Grace's review, the technician helps write the new rules, which also makes them more practical. The review notes also record the rules that were missing, not the person involved.

### Using the list in tickets

Tomás keeps the failure-mode list beside the ticket queue. When a ticket mentions strange redirects, new admin users or pages changing on their own, he checks for changed files and recent plugin updates first. When a ticket asks for a plugin installation, he checks source, hash and maintenance before agreeing. The list turns vague worries into specific questions with specific checks.

### Worked example

Grace runs a short review of the Ferncroft case using these failure modes. Three applied: changed download, misconfiguration and, initially, no inventory to detect outdated components. The review results in new rules, not blame, and the technician involved helps write them.

> **Synthetic case.** Cases are synthetic.

### Errors and limits

Some failures cannot be prevented by a consumer, only detected quickly.

### Exercises

- **EX029 — Changed download check.** What checks prevent changed downloads? *Rubric:* 3 = official sources, hash verification; 2 = partial; 1 = none; 0 = none.
- **EX030 — Abandoned plugins.** How are abandoned plugins handled? *Rubric:* 3 = review yearly; replace; 2 = partial; 1 = none; 0 = none.
- **EX031 — Compromised publisher.** Why can't consumers fully prevent publisher compromise? *Rubric:* 3 = legitimate channel; detect quickly; 2 = partial; 1 = none; 0 = none.
- **EX032 — Blame-free.** Why was the review blame-free? *Rubric:* 3 = no rule existed; process problem; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know the failure modes and link each to a check.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Application and software supply chain security: tools and methods

### Learning outcomes

You will (1) build and use a plugin inventory; (2) compare versions with advisories; (3) choose simple, reliable tools; (4) keep results current.

### 9.1 The inventory

A nightly script lists, for every customer site, each installed plugin and version from the application's own records. The output is a CSV kept by Pinecrest and visible to support. Using the application's own records makes the list quick and consistent across hundreds of sites. The CSV gives support a single place to answer 'which sites run resize-plugin 2.4.1?', a question nobody could answer during the Ferncroft case. The monthly spot check against plugin folders catches anything the records miss. The CSV is read-only to support, so nobody edits inventory rows by hand.

### 9.2 Advisories

Vendors and security databases publish advisories naming the affected component, the fixed version and severity. Pinecrest subscribes to advisory feeds for the shop application and its popular plugins. An advisory gives exactly what the comparison script needs: the component name, the version that fixes the flaw and the severity. Subscribing to feeds for the shop application and popular plugins covers most of Pinecrest's installations, since seven plugins account for over 80% of them. Each feed's entries are checked against the advisory text before a ticket is raised.

### 9.3 Comparing

A script compares installed versions with the fixed version: anything lower is affected. Version strings must be compared as numbers, not text, or 2.10 would sort before 2.9. The lab in Chapter 12 does this with number tuples, so 2.4.1 is correctly lower than 2.4.3 and 4.9.9 lower than 5.1.0. Labels such as 2.4.1-beta would break a simple conversion, which is why Tomás adds a test for them when he checks the inventory. An incorrect comparison could miss affected sites or flag fixed ones, so the script is tested with known pairs.

### 9.4 Prioritising

High severity on public pages comes first. EPSS scores (Jacobs et al., 2021) can help judge how likely exploitation is when many advisories arrive at once, alongside CWE categories such as those in MITRE's CWE Top 25 to understand the kind of weakness. Severity alone can mislead when dozens of advisories arrive at once, so these signals help order the work. Pinecrest uses EPSS only as one input, and Tomás records which advisories were moved up or down because of it, so the order can be reviewed.

### 9.5 Simple tools

Stdlib scripts with clear output are easy to review and run anywhere. A short standard-library script can be read by a supervisor in minutes and run on any support machine without installing anything. The four labs in this course follow that pattern, and the nightly job grows from scripts written the same way, so reviewers can check exactly what each step does before trusting its results. Clear output, one line per finding, makes the results easy to paste into tickets.

### 9.6 Keeping current

The inventory runs nightly, so it reflects updates made the day before. A nightly run means an advisory published today can be compared with yesterday's installed versions by tomorrow morning. Updates applied during the day appear in the next run, so a fixed site drops out of the findings without anyone editing a list by hand. Stale inventory data would send technicians to sites that had already been updated the day before. If a nightly run fails, the coverage alert from Chapter 14 makes the gap visible.

### Checking the inventory

Once a month Tomás picks five sites and compares the inventory with a direct listing of plugin folders. The first check finds one site with a plugin folder copied by hand that the application did not list; it is added to the inventory process. He also checks that version strings with extra labels, such as 2.4.1-beta, are handled correctly by the comparison script and adds a test for them.

### Worked example

The first inventory shows 412 customer sites with 1,960 plugin installations and 38 distinct plugins. Seven plugins account for over 80% of installations, so advisories for those seven are watched most closely.

> **Synthetic case.** Counts are synthetic.

### Errors and limits

An inventory from the application's own records may miss files added by hand; compare with file listings occasionally.

### Exercises

- **EX033 — Inventory content.** What does the inventory list? *Rubric:* 3 = site, plugin, version; 2 = two; 1 = one; 0 = none.
- **EX034 — Version compare.** Why compare versions as numbers? *Rubric:* 3 = text puts 2.10 before 2.9; 2 = partial; 1 = none; 0 = none.
- **EX035 — Priority.** What comes first? *Rubric:* 3 = high severity on public pages; 2 = partial; 1 = none; 0 = none.
- **EX036 — Seven plugins.** Why watch seven plugins closely? *Rubric:* 3 = over 80% of installations; 2 = partial; 1 = none; 0 = none.

### Synthesis

Inventory and advisory comparison find what needs updating.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Application and software supply chain security: control configuration

### Learning outcomes

You will (1) configure a baseline of security headers and settings for customer sites; (2) check sites against it; (3) fix gaps safely; (4) record exceptions.

### 10.1 The baseline

Pinecrest's baseline for customer sites: HTTPS only with Strict-Transport-Security; a Content-Security-Policy limiting where scripts load from; X-Content-Type-Options set to nosniff; a Referrer-Policy; and no server header revealing software versions. OWASP ASVS 4.0.3 section V14 covers such configuration requirements. Each item has a specific job on a shop site. HSTS keeps browsers on HTTPS, CSP limits script sources, nosniff stops browsers guessing file types, Referrer-Policy limits what leaves in links, and hiding the version removes an easy clue for anyone scanning for old software.

### 10.2 Why headers matter for the supply chain

A Content-Security-Policy limits which outside sources a page will load scripts from. If a plugin is changed to load a script from an unknown domain, the browser blocks it. Headers do not replace verification, but they reduce what a changed component can do. For Ferncroft, the changed plugin sent visitors elsewhere through a redirect, which CSP does not stop, so verification remained essential there. Headers therefore work beside hash verification, each catching what the other misses on a hosted shop.

### Lab — header baseline

```python
"""Check synthetic site response headers against a baseline (stdlib only)."""
baseline = ["Strict-Transport-Security", "Content-Security-Policy", "X-Content-Type-Options", "Referrer-Policy"]
sites = {
    "ferncroft-books": {"Strict-Transport-Security": "max-age=31536000", "Content-Security-Policy": "default-src 'self'",
                        "X-Content-Type-Options": "nosniff", "Referrer-Policy": "strict-origin-when-cross-origin"},
    "alder-dental": {"Strict-Transport-Security": "max-age=31536000", "X-Content-Type-Options": "nosniff"},
    "quayside-gym": {"Content-Security-Policy": "default-src 'self'", "X-Content-Type-Options": "nosniff",
                     "Referrer-Policy": "no-referrer", "Server": "webserver/2.4.29"},
}
for site, h in sites.items():
    missing = [x for x in baseline if x not in h]
    extra = ["Server header reveals version"] if "Server" in h and any(c.isdigit() for c in h["Server"]) else []
    issues = [f"missing {m}" for m in missing] + extra
    print(f"{site:16} {'OK' if not issues else '; '.join(issues)}")
```

Run with `python3 lab_headers.py`. Verified output:

```text
ferncroft-books  OK
alder-dental     missing Content-Security-Policy; missing Referrer-Policy
quayside-gym     missing Strict-Transport-Security; Server header reveals version
```

### 10.3 Lab result

ferncroft-books meets the baseline (OK). alder-dental is missing Content-Security-Policy and Referrer-Policy. quayside-gym is missing Strict-Transport-Security and its Server header reveals a version, webserver/2.4.29. ferncroft-books passing shows the baseline can be met on a real shop configuration. The other two sites fail for different reasons, so one generic fix would not do. alder-dental needs a policy written for its own scripts, while quayside-gym's gaps are fixed in the shared server template for all sites. The lab output becomes three tickets: two site-specific fixes and one template change.

### 10.4 Fixing safely

A new Content-Security-Policy can break pages that load scripts from legitimate outside services, such as a booking widget. Pinecrest first applies it in report-only mode, reviews reports for a week, adjusts, then enforces. Report-only mode lets the browser report what a policy would block without actually blocking it. For alder-dental, the week of reports showed one legitimate outside script, the appointment widget, whose domain was then added. Enforcing without this step could have broken bookings and turned the customer against the change.

### 10.5 Exceptions

If a customer needs a weaker setting, the reason and review date are recorded. An exception without a review date tends to become permanent and forgotten. Recording the reason lets a later technician judge whether it still applies, for example whether a customer still uses the outside service that needed a looser Content-Security-Policy. Expired exceptions go back to the baseline unless the customer renews the request with a reason. The exception record also names the customer contact who requested it, so renewal questions reach the right person at the right time.

### Applying through templates

Headers are set in the shared server template, so fixes reach every site and new sites start compliant. Customer-specific additions live in a small override file reviewed by support.

### Recording changes

Every baseline change is logged with its reason and date.

### Worked example

Applying report-only mode to alder-dental shows one legitimate outside script, an appointment widget. Its domain is added, the policy enforced, and the site shows no errors. quayside-gym's missing header and version banner are fixed in the server template for all sites.

> **Synthetic case.** Sites and headers are synthetic.

### Errors and limits

Headers depend on browsers enforcing them; they are a layer, not a guarantee.

### Exercises

- **EX037 — Baseline items.** List the baseline headers. *Rubric:* 3 = HSTS, CSP, nosniff, Referrer-Policy, no version banner; 2 = three; 1 = one; 0 = none.
- **EX038 — Lab gaps.** What did the lab find for alder-dental and quayside-gym? *Rubric:* 3 = alder missing CSP, Referrer; quayside missing HSTS, version banner; 2 = one; 1 = none; 0 = none.
- **EX039 — Report-only.** Why use report-only mode first? *Rubric:* 3 = avoid breaking legitimate scripts; 2 = partial; 1 = none; 0 = none.
- **EX040 — CSP benefit.** How does CSP help with supply chain problems? *Rubric:* 3 = blocks scripts from unknown domains; 2 = partial; 1 = none; 0 = none.

### Synthesis

Baselines limit what a changed component can do.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Application and software supply chain security: verification

### Learning outcomes

You will (1) verify that controls work as intended; (2) test with synthetic cases; (3) record results; (4) re-verify after changes.

### 11.1 Verification versus configuration

Configuring a control is not the same as knowing it works. Verification checks the result: the header is actually sent, the hash check actually stops a mismatched file, the permission check actually finds writable folders. At Pinecrest this difference showed up when a template update silently dropped Referrer-Policy from 40 sites. The configuration had once been correct, but only the quarterly verification found that it no longer was. Verification asks 'does it work now?', not 'did we set it up once?'.

### 11.2 Synthetic test cases

For each control, Tomás prepares safe synthetic cases: a deliberately mismatched test file for the hash step, a test site with a writable code folder, and a test page loading a script from an unlisted domain to confirm CSP reports it. OWASP WSTG v4.2 describes structured testing of configuration and deployment management. Each case is harmless by design: the test file is synthetic, the writable folder sits on a test site, and the unlisted script only checks reporting. Each case has an expected result written down before the test runs.

### 11.3 Recording results

Each verification records control, test case, expected result, actual result, date and tester. Recording the expected result before the test prevents reading success into whatever happens. A record for the hash step might show a mismatched test file, expected MISMATCH, actual MISMATCH, with date and tester. Over six months these records added up to 31 verifications with three failures, which became Grace's evidence of maintained controls. Records are kept with the control's documentation, so anyone can see its test history at once.

### 11.4 Re-verification

Controls are re-verified after server template changes, application upgrades and every quarter. Template changes and application upgrades are exactly when settings tend to drift, as the dropped Referrer-Policy on 40 sites showed. Quarterly runs catch slower changes that no single event announces. The calendar Tomás keeps lists each re-verification, so another technician can run them when he is away. Each re-verification uses the same synthetic cases, so results can be compared over time and a change in outcome stands out clearly.

### 11.5 Failures

A failed verification is a finding with an owner and due date, like any other issue. Treating a failed verification as a finding means it enters the ticket queue with the same visibility as any other problem. The three failures in six months were each fixed within a week this way. Without an owner and due date, a failed test risks being noted and then forgotten. The failure record also notes which test found it, which helps judge whether tests are sufficient.

### 11.6 Customer evidence

Verification records let Pinecrest answer customer security questionnaires with evidence. When a customer's questionnaire asks whether file integrity is checked before installation, Pinecrest can point to dated verification records rather than a policy statement. The records show the hash step actually rejecting a mismatched file, which is stronger evidence than a procedure that only says what should happen. Answers cite dates and results without exposing other customers' details, and Grace reviews each questionnaire answer before it goes back to the customer.

### Verification schedule

Tomás keeps a simple calendar: hash-step test monthly, permission check weekly through the nightly job, header check after every template change and quarterly in full. Each test takes minutes. The calendar is shared, so if Tomás is away another technician runs the tests and records the results. After six months the records show 31 verifications with three failures, all fixed within a week, which Grace uses as evidence that the controls are being maintained, not just configured once.

### Worked example

Quarterly verification finds that the server template update had dropped Referrer-Policy from 40 sites. The test catches it within days, the template is fixed, and a check is added to the template's own tests.

> **Synthetic case.** Tests and results are synthetic.

### Errors and limits

Tests only cover cases you thought of; vary them over time.

### Exercises

- **EX041 — Difference.** How does verification differ from configuration? *Rubric:* 3 = checks the result works; 2 = partial; 1 = none; 0 = none.
- **EX042 — Test cases.** Name two synthetic test cases. *Rubric:* 3 = mismatched file, writable folder, unlisted script; 2 = one; 1 = none; 0 = none.
- **EX043 — When to re-verify.** When are controls re-verified? *Rubric:* 3 = template changes, upgrades, quarterly; 2 = two; 1 = one; 0 = none.
- **EX044 — Quarterly catch.** What did the quarterly check catch? *Rubric:* 3 = Referrer-Policy dropped from 40 sites; 2 = partial; 1 = none; 0 = none.

### Synthesis

Verify controls with safe tests and repeat after change.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) run an advisory comparison in a contained lab; (2) interpret results; (3) plan updates by severity; (4) practise safe lab habits.

### 12.1 The lab setting

The contained lab uses synthetic customer records only. No real sites are touched; results are discussed, not acted on, until the real process runs with tickets. This rule protects Pinecrest's customers from mistakes made while learning in the lab. A script under development might have a bug, and pointing it at a live site could produce wrong findings or, for a script that writes, real damage. Discussing results first and acting only through tickets keeps the lab a rehearsal rather than a change. Lab records are labelled as synthetic so they are never filed as real findings.

### 12.2 The task

Compare installed plugin versions for three synthetic sites with two advisories: resize-plugin fixed in 2.4.3 (high) and contact-form fixed in 5.1.0 (medium). The two advisories differ in severity, which is what makes the task useful for practising priorities. The three synthetic sites also include two installations that are already fixed, so the script must show that it can tell affected versions from safe ones rather than flagging every installation of a named plugin. The fixed versions and severities come from the synthetic advisories only.

### Lab — advisory comparison

```python
"""Compare installed synthetic plugin versions with advisory fixed versions (stdlib only)."""
def v(s): return tuple(int(x) for x in s.split("."))
advisories = {"resize-plugin": ("2.4.3", "high"), "contact-form": ("5.1.0", "medium")}
installed = {
    "ferncroft-books": {"resize-plugin": "2.4.1", "contact-form": "5.2.0"},
    "alder-dental": {"contact-form": "5.0.4"},
    "quayside-gym": {"resize-plugin": "2.5.0", "contact-form": "4.9.9"},
}
count = {"high": 0, "medium": 0}
for site, plugins in installed.items():
    for p, ver in plugins.items():
        if p in advisories and v(ver) < v(advisories[p][0]):
            fixed, sev = advisories[p]
            count[sev] += 1
            print(f"{site:16} {p:14} {ver:6} -> update to {fixed} ({sev})")
print("totals:", count)
```

Run with `python3 lab_versions.py`. Verified output:

```text
ferncroft-books  resize-plugin  2.4.1  -> update to 2.4.3 (high)
alder-dental     contact-form   5.0.4  -> update to 5.1.0 (medium)
quayside-gym     contact-form   4.9.9  -> update to 5.1.0 (medium)
totals: {'high': 1, 'medium': 2}
```

### 12.3 Lab result

ferncroft-books must update resize-plugin from 2.4.1 to 2.4.3 (high). alder-dental must update contact-form from 5.0.4 to 5.1.0 (medium), and quayside-gym contact-form from 4.9.9 to 5.1.0 (medium). Totals: high 1, medium 2. quayside-gym's resize-plugin 2.5.0 and ferncroft's contact-form 5.2.0 are already fixed. The totals depend on comparing number tuples, so 4.9.9 is correctly lower than 5.1.0. Changing alder-dental to 5.1.0 drops the medium count to 1. Tomás records both the original totals and the changed run, so the check of the script's behaviour is visible to Grace. The two already fixed installations show the script does not flag every copy of a named plugin.

### 12.4 Planning

High within 7 days, medium within 30. Customers are told before updates that could change how their site looks. For the lab results, that means ferncroft-books' resize-plugin update is due within 7 days, and the two contact-form updates within 30. Telling customers first matters for updates such as contact-form, where alder-dental's later update broke the form until a renamed setting was applied. The deadlines run from when the advisory arrives, not from when someone notices it. Customers who cannot accept an update in time are recorded with a reason and a new date.

### 12.5 Lab habits

Keep lab data synthetic, label outputs as lab results, and never point lab scripts at real systems. Labelling outputs as lab results prevents a synthetic finding, such as ferncroft-books needing resize-plugin 2.4.3, from being mistaken for a real ticket. Pointing scripts only at synthetic records keeps the contained lab contained. The same habits apply when Tomás later reuses the scripts in the rehearsal in Chapter 17. Lab scripts are stored apart from production tools so nobody runs them against live sites.

### Reading the lab

The script converts versions to number tuples, compares each installed plugin with the fixed version, and counts results by severity. Tomás changes one input in the lab, setting alder-dental to 5.1.0, and confirms the medium count drops to 1, a quick way to check the script behaves as expected. He also notes that the lab's advisory list is tiny; the real process reads a feed with hundreds of entries, which is why matching must be automatic.

### Lab record

Lab outputs are saved with the date and labelled as synthetic results.

### Worked example

Tomás presents the lab plan to Grace: one high update today with a hash-verified official download, two medium updates in the weekly maintenance window. Grace asks what happens if an update breaks a site; Tomás adds a backup and rollback step to the plan.

> **Synthetic case.** The lab is synthetic.

### Errors and limits

A version comparison depends on accurate advisories; check the advisory text.

### Exercises

- **EX045 — Lab totals.** What totals did the lab give? *Rubric:* 3 = high 1, medium 2; 2 = partial; 1 = none; 0 = none.
- **EX046 — Already fixed.** Which installations were already fixed? *Rubric:* 3 = quayside resize 2.5.0; ferncroft contact-form 5.2.0; 2 = one; 1 = none; 0 = none.
- **EX047 — Due dates.** What due dates apply? *Rubric:* 3 = high 7 days, medium 30; 2 = partial; 1 = none; 0 = none.
- **EX048 — Added step.** What did Tomás add after Grace's question? *Rubric:* 3 = backup and rollback; 2 = partial; 1 = none; 0 = none.

### Synthesis

Practise in a contained lab before acting on real systems.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Application and software supply chain security: troubleshooting

### Learning outcomes

You will (1) diagnose problems after plugin updates and control changes; (2) roll back safely; (3) find root causes; (4) keep notes.

### 13.1 Typical problems

After updates: pages break, layouts change, error rates rise. After control changes: a new Content-Security-Policy blocks a legitimate widget, the hash step rejects a file because the vendor republished a release, or the permission fix stops a legitimate cache folder from working. Each of these problems has appeared in the course: the appointment widget at alder-dental, the vendor republishing case, and the contact-form update that broke a form. Knowing these typical cases helps Tomás recognise a familiar pattern quickly.

### 13.2 Method

Tomás reads the error, checks what changed most recently, reproduces it on a test copy of the site with synthetic data, and changes one thing at a time. This method found the alder-dental fault: the most recent change was the contact-form update, and the test copy showed the new version needed a renamed setting. Changing one thing at a time on the test copy shows which change fixed the fault, so the live fix can be applied once and correctly.

### 13.3 Rolling back

Every update has a backup. If a customer's site is broken, rollback restores service first; diagnosis continues on the test copy. At alder-dental, Tomás rolled back the contact-form update within ten minutes, so the customer's form worked again while he diagnosed. The backup taken before every update is what makes this possible. Rollback is a service decision, not a fix, which is why a deadline to fix forward follows it. The rollback is recorded in the ticket with the time it was performed.

### 13.4 Not weakening controls

Rolling back an update is acceptable; turning off a control to make an error disappear is not. If a control must change, the change is reviewed. Turning off a Content-Security-Policy to make a widget work would remove protection against changed components on that site. The right response is to find the legitimate domain, as with alder-dental's appointment widget, and add it after review. Any reviewed change to a control is recorded with its reason, so an exception never happens silently.

### 13.5 Vendor republishing

When a vendor's hash changes, support asks the vendor through an official channel why before installing. A changed hash may have an innocent explanation, such as a vendor rebuilding a release, but it may also mean a compromised publisher. Asking through the vendor's official channel, not the mirror or a forum, gets an answer Pinecrest can trust. Until then, the file is treated like the Ferncroft mirror copy and not installed. The vendor's answer is saved in the ticket with the new hash.

### 13.6 Notes

Each fix is recorded with symptom, cause and fix in the support knowledge base. The alder-dental note records the symptom, a broken contact form after the update, the cause, a renamed setting, and the fix. The next technician who sees the same symptom on another site can apply the fix in minutes. Notes also show recurring causes that may justify a procedure change. Grace reviews the new knowledge-base notes every week so that wrong fixes are corrected before others copy them.

### Test copies

Each customer site can be copied to a private test area with customer data replaced by synthetic records. Problems are reproduced there so that diagnosis never risks the live shop or its customers' details.

### Deadlines after rollback

A rollback to a version with a known advisory gets a ticket with a fix-forward deadline.

### Worked example

A contact-form update breaks alder-dental's form. Tomás rolls back within ten minutes, reproduces the problem on a test copy, and finds the new version requires a setting renamed. He applies the update with the setting on the test copy, then on the live site, and writes a knowledge-base note.

> **Synthetic case.** Problems are synthetic.

### Errors and limits

Rolling back to a vulnerable version is temporary; set a deadline to fix forward.

### Exercises

- **EX049 — Method.** What is Tomás's method? *Rubric:* 3 = read, check recent change, reproduce, one change; 2 = three; 1 = one; 0 = none.
- **EX050 — Rollback rule.** What comes first when a site is broken? *Rubric:* 3 = restore service by rollback; 2 = partial; 1 = none; 0 = none.
- **EX051 — Republished hash.** What happens when a vendor's hash changes? *Rubric:* 3 = ask vendor officially first; 2 = partial; 1 = none; 0 = none.
- **EX052 — Alder fix.** What fixed the alder-dental form? *Rubric:* 3 = renamed setting applied; 2 = partial; 1 = none; 0 = none.

### Synthesis

Restore service, diagnose safely and keep controls on.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Application and software supply chain security: automation

### Learning outcomes

You will (1) automate inventory, advisory comparison and baseline checks; (2) route results to tickets; (3) limit automation's permissions; (4) watch for silent failures.

### 14.1 The nightly job

Each night a job builds the plugin inventory, compares it with advisories, checks headers and permissions for every site, and writes a report. Combining the checks into one job means every site is checked the same way every night. The job reuses the logic from the course labs: the inventory, the version comparison, the header baseline and the permission listing. Its report replaces the manual weekly checks that previously took a full day. The report lists coverage first, then new findings by severity.

### 14.2 Routing

Each finding becomes a ticket for the support queue with severity and due date. Highs also notify the duty supervisor. Turning findings into tickets uses the queue support already watches, so nothing needs a separate dashboard. Due dates follow the planning rule of high within 7 days and medium within 30. Notifying the duty supervisor for highs ensures an advisory like the resize-plugin one is not left waiting until morning. Each ticket links back to the nightly report line that produced it.

### 14.3 Permissions

The job reads site data and opens tickets; it cannot change sites. Updates are applied by technicians through the normal process. A read-only job limits the harm a bug or a stolen credential can do. The expired read credential in the worked example shows the job does depend on credentials, which is another reason they grant only reading. Updates still follow the procedure, with backups, hash checks and customer notice. The job's credential is also scoped to reading site data only.

### 14.4 Silent failures

If the report is missing or covers fewer sites than expected, an alert fires. A job that silently checks nothing is worse than no job, because it looks like good news. The coverage alert caught exactly this: zero findings for a cluster, together with 60 fewer sites than expected. Comparing sites checked against sites expected turns that silence into a visible alert. The alert goes to the duty supervisor, who checks the job before trusting the next report. The expected site count comes from Pinecrest's hosting records, not from the job itself.

### 14.5 Reviewing the job

The job's code is reviewed and tested with synthetic sites before each change. Testing on synthetic sites first means a change cannot break the real nightly report unnoticed. When the job's scripts first ran beside the manual checks, two differences were found, both bugs in the scripts. The same comparison approach is used whenever the job's checks change, with a second technician reviewing. A second technician signs off each change, and the review is recorded with the job's code in version control.

### 14.6 Time saved

Weekly manual checks that took a day now take an hour of reading tickets. The saved day goes into fixing findings rather than finding them. Grace reads only the summary each morning, and technicians work from the tickets, so the job's output is read by the people who act on it. The comparison is rough, since the old manual checks covered fewer sites, but the direction is clear. Tomás records the estimate in his project evidence as an approximate figure rather than a measured result.

### Building in steps

The job started as Tomás's manual checks turned into scripts one at a time. Each script ran beside the manual check for two weeks, and results were compared before the manual step stopped. Two differences were found, both bugs in the scripts, and fixed before anyone relied on them. The report starts with counts by severity and coverage (sites checked versus sites expected), then lists new findings. Coverage at the top makes gaps hard to miss. Grace reads only the summary each morning; technicians work from the tickets.

### Change control

Any change to the job's checks is reviewed by a second technician before it runs nightly.

### Worked example

In its third week, the nightly job reports 0 findings for a whole hosting cluster. Because the site count also dropped by 60, the missing-coverage alert fires; the cause is an expired read credential for that cluster, which is renewed the same morning.

> **Synthetic case.** Jobs and events are synthetic.

### Errors and limits

Automation that can change sites needs far stronger review; keep it read-only where possible.

### Exercises

- **EX053 — Job tasks.** What does the nightly job do? *Rubric:* 3 = inventory, advisory compare, headers and permissions, report; 2 = three; 1 = one; 0 = none.
- **EX054 — Job permissions.** Why can't the job change sites? *Rubric:* 3 = limits harm; changes by technicians; 2 = partial; 1 = none; 0 = none.
- **EX055 — Zero findings.** Why was zero findings suspicious? *Rubric:* 3 = site count dropped too; 2 = partial; 1 = none; 0 = none.
- **EX056 — Cause.** What caused the gap? *Rubric:* 3 = expired read credential; 2 = partial; 1 = none; 0 = none.

### Synthesis

Automate checks read-only and watch coverage.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Application and software supply chain security: integration and dependencies

### Learning outcomes

You will (1) understand how plugins depend on other components; (2) check third-party scripts and services; (3) manage dependency chains; (4) reduce unneeded dependencies.

### 15.1 Dependency chains

Plugins often bundle libraries, and the shop application depends on the language runtime and its packages. Decan et al. (2018) showed how dependency networks grow across ecosystems, and Zimmermann et al. (2019) showed how a few maintainers can reach many projects. A flaw deep in the chain can affect sites that never chose that library. For Pinecrest, this means an advisory may name a library that no customer ever chose, bundled inside a plugin such as the resize plugin. The bundled libraries are recorded in the inventory where vendors report them.

### 15.2 Third-party scripts

Many sites load scripts from outside services: analytics, chat widgets, payment forms. Each is a dependency outside Pinecrest's control, and CSP lists them explicitly. These scripts run in visitors' browsers even though Pinecrest never installs them on its servers. Listing them in each site's CSP makes each one a visible decision rather than a silent addition. The review of outside scripts later finds several sites still loading scripts from services they had stopped using. Payment forms in particular are reviewed carefully, since they handle card details.

### 15.3 Recording dependencies

The inventory adds bundled libraries reported by plugins and outside script domains from each site's CSP. Adding bundled libraries means an advisory naming a library can be matched to sites, not only advisories naming plugins. Reading outside script domains from each CSP turns the policy into an inventory source as well as a control. The customer's owner for each remaining script is recorded alongside it, so questions go to the right person. The dependency data is refreshed by the same nightly job as the plugin list.

### 15.4 Reducing dependencies

Unused plugins and scripts are removed with customer agreement; every removal shrinks the chain. The worked example shows the scale: 61 sites had plugins installed but disabled, and customers agreed to remove them from 54 sites, cutting 140 installations. Each removed installation is one less entry to compare with advisories, one less folder to check for permissions and one less path for changed code. Removal follows the normal procedure, with a backup taken first. The remaining seven sites kept their disabled plugins at the customers' request, and that decision is recorded.

### 15.5 SBOMs

Some vendors publish a software bill of materials listing components; NTIA (2021) describes minimum elements. Where available, Pinecrest uses SBOMs to see bundled libraries. An SBOM lists components by name and version, so Pinecrest can match bundled libraries against advisories without unpacking each plugin. Few plugin vendors publish one yet, which is why extending the inventory through SBOMs appears in Tomás's next steps rather than in his completed work. SBOM data is checked against installed files on a sample of sites first.

### 15.6 Updates and compatibility

Updating one component may require others; updates are tested together on a test copy. Updating a plugin may require a newer shop application or library, and updating the application may break an older plugin. Testing the set together on a test copy with synthetic data shows such conflicts before they reach a customer's live shop. The rollback plan covers the whole set, not each part. Results from the combined test are recorded in the ticket before any live update is scheduled.

### Reviewing outside scripts

For each outside script domain, Tomás asks the customer what it is for. Several sites still load scripts from services they stopped using years ago. Removing them shortens the CSP and removes code that runs in visitors' browsers without any benefit. For scripts that remain, the inventory records the service and its owner at the customer.

### Yearly dependency review

Once a year, support reviews each popular plugin's maintenance activity and bundled libraries.

### Worked example

Reviewing dependencies, Tomás finds 61 sites with plugins installed but disabled. Customers agree to remove them from 54 sites, cutting 140 installations that would otherwise need tracking and updating.

> **Synthetic case.** Counts are synthetic.

### Errors and limits

Disabled plugins still have files on the server; remove, do not just disable.

### Exercises

- **EX057 — Chain risk.** Why can deep dependencies affect sites? *Rubric:* 3 = bundled libraries not chosen directly; 2 = partial; 1 = none; 0 = none.
- **EX058 — Outside scripts.** How are outside scripts tracked? *Rubric:* 3 = listed in CSP; inventory; 2 = partial; 1 = none; 0 = none.
- **EX059 — Disabled plugins.** Why remove disabled plugins? *Rubric:* 3 = files remain on server; 2 = partial; 1 = none; 0 = none.
- **EX060 — Removal result.** What did removal achieve? *Rubric:* 3 = 140 installations removed from 54 sites; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know and shrink the dependency chain.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) write clear procedures for plugin installation and updates; (2) document safety rules; (3) keep documents current; (4) make them easy to follow.

### 16.1 The installation procedure

One page: confirm the request in a ticket; check the plugin is maintained; download from the official source only; verify the hash or signature from the vendor's site; take a backup; install with correct permissions; check headers and error logs; record version and hash in the ticket. Each step answers one Ferncroft gap: the official source and hash replace the mirror, the permissions step prevents a writable plugin folder, and recording the version feeds the inventory. The backup step comes from Grace's question about broken updates in the contained lab, so every installation can be rolled back.

### 16.2 The update procedure

Similar steps, plus checking change notes for breaking changes and a rollback plan. Change notes reveal breaking changes such as the renamed setting that broke alder-dental's contact form. Reading them before updating lets the technician apply the setting at once rather than discovering it through a customer complaint. The rollback plan names the backup to restore and who decides to restore it. The update procedure also repeats the hash or signature check, exactly as for a first installation of the same plugin.

### 16.3 Safety rules

Work only within ticket scope; never install from mirrors; never disable a control to fix an error; use synthetic data in tests; report anything unexpected to the duty supervisor. Each of these safety rules comes from a case met earlier in this course. Scope comes from the Ferncroft ticket, the mirror ban from the changed download, and the rule against disabling controls from troubleshooting. The rule on synthetic test data comes from the contained labs and the test copies. Reporting to the duty supervisor covers anything unexpected that no rule describes.

### 16.4 Writing clearly

Numbered steps, one action per step, and the reason for important steps in a short note. New technicians test the procedure by following it exactly. One action per step makes it obvious where a technician stopped or skipped. The short reasons help with judgement when something unexpected happens, such as the vendor publishing a signature instead of a hash. Testing by a new technician finds places where experienced staff fill gaps without noticing. Edits from those tests are recorded in the procedure's history.

### 16.5 Keeping current

Each document has an owner and review date; incidents and verification failures trigger updates. The signature gap found by a new technician shows how incidents and tests feed updates: the procedure gained a short part on checking vendor signatures. A named owner makes sure updates happen, and the review date catches documents that no incident has touched. The change history at the bottom of the procedure shows each update with its date and reason. Verification failures also trigger a check of whether the procedure missed a step.

### 16.6 Where documents live

Procedures sit in the support knowledge base linked from the ticket templates. Linking procedures from ticket templates puts them in front of technicians at the moment they need them. A technician opening an installation ticket sees the installation procedure and the mandatory fields for version, hash source and computed hash. Documents kept elsewhere are easily forgotten when a technician is working under time pressure. The knowledge base keeps one current version of each procedure, so technicians never follow a superseded copy saved locally on a desktop.

### Checking tickets

Each month Grace samples ten installation tickets to see whether the version, hash source and computed hash were recorded. The first sample finds two tickets missing the hash source. The fields are made mandatory in the ticket form, and the next sample is complete.

### Version history

Each procedure keeps a short change history at the bottom, showing what changed, when and why, so technicians can see recent updates.

### Worked example

A new technician follows the installation procedure for the first time and stops at "verify the hash": the vendor publishes a signature, not a hash. Tomás adds a short section on checking vendor signatures and links the vendor's instructions.

> **Synthetic case.** Procedures are synthetic.

### Errors and limits

A procedure nobody follows is a false comfort; check tickets show the steps were done.

### Exercises

- **EX061 — Install steps.** List four installation steps. *Rubric:* 3 = ticket, official source, verify, backup, permissions, record; 2 = three; 1 = one; 0 = none.
- **EX062 — Safety rule.** Name two safety rules. *Rubric:* 3 = scope; no mirrors; no disabling; synthetic tests; 2 = one; 1 = none; 0 = none.
- **EX063 — Testing documents.** How is a procedure tested? *Rubric:* 3 = new technician follows it exactly; 2 = partial; 1 = none; 0 = none.
- **EX064 — Signature gap.** What gap did the new technician find? *Rubric:* 3 = vendor uses signature not hash; 2 = partial; 1 = none; 0 = none.

### Synthesis

Clear, tested procedures make safe work routine.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) rehearse a full plugin advisory response in a contained lab; (2) combine inventory, verification, logs and headers; (3) produce a short report.

### 17.1 The scenario

A synthetic high-severity advisory for resize-plugin is published. In the lab, Tomás uses the earlier scripts together on synthetic records. Choosing resize-plugin connects the rehearsal to the Ferncroft case and lets each earlier lab play its part. The advisory comparison, hash check, header check and log summary all run on the same synthetic records. Using existing scripts tests whether they work together, not only alone. Tomás runs the rehearsal on a timer to measure how long a full response takes.

### 17.2 Steps

Run the advisory comparison to find affected sites (ferncroft-books, high). Verify the fixed release's hash against the vendor manifest (official file MATCH; mirror file MISMATCH, rejected). Check headers on affected sites (ferncroft-books OK). Summarise logs for signs of problems (failed admin sign-ins from one address reaching REVIEW). Each step reuses a lab output unchanged, so results can be checked against the earlier chapters. The results agree with each lab's verified output, which shows the scripts combine without changing each other's behaviour. Any disagreement would have pointed to a bug in combining them.

### 17.3 Report

The lab report lists affected sites, verified files, configuration status, log observations and the update plan with due dates. For the rehearsal, the report lists ferncroft-books as affected (high), the official file as verified and the mirror file as rejected. It records headers as OK, the REVIEW line for 198.51.100.7, and the update due within 7 days. Grace later uses this report as the template for real advisory responses. The report fits on one page, with an appendix holding the raw outputs of all four scripts.

### 17.4 Timing

The rehearsal is timed: from advisory to complete plan in 35 minutes. Timing gives a baseline for later rehearsals and for real responses. The 35 minutes include finding the vendor's official hash, the step that took longest because the vendor's download page had moved. A month later, the contact-form advisory is handled with the same steps in under an hour, including real-style checks. Grace records the 35 minutes with the rehearsal scores, so the next rehearsal six months later can be compared against the same steps.

### 17.5 Lab safety

All data synthetic; no real sites contacted. The rehearsal combines four scripts but still reads only synthetic files. No vendor site, customer site or log server is contacted, so a mistake cannot affect anyone. The advisory, sites and addresses are invented, and documentation addresses such as 198.51.100.7 keep the log step safe for training material. The outputs are labelled as rehearsal results and stored with the lab scripts. Grace checks those labels herself before the report is used as a template.

### 17.6 Lessons

The rehearsal shows the log summary needs the site name in its output for multi-site use. The log lab was written for one site, so its output names addresses but not sites. When the rehearsal combines results across sites, a REVIEW line without a site name cannot be routed to the right ticket. Adding the site name is a small change with a clear test. The fix is tested with the same synthetic log well before the next rehearsal runs.

### Debrief

After the rehearsal, Tomás and Grace discuss what went well and what slowed them. Finding the vendor's official hash took longest, because the vendor's download page moved. They add each major vendor's official release page to the procedure. They also agree to rerun the rehearsal every six months with new synthetic advisories, so new technicians practise before facing a real one. The debrief notes are filed with the lab report so the next rehearsal starts from them.

### Scoring the rehearsal

Grace scores the rehearsal on completeness, accuracy and time, and records the scores for comparison.

### Files kept

The lab scripts and synthetic inputs are stored together for reuse.

### Worked example

Grace reviews the lab report and uses it as the template for real advisory responses. A month later, a real-style synthetic advisory for contact-form is handled with the same steps in under an hour.

> **Synthetic case.** The lab is synthetic.

### Errors and limits

Rehearsals cannot include every real-world complication.

### Exercises

- **EX065 — Steps.** List the four lab steps. *Rubric:* 3 = compare, verify, headers, logs; 2 = three; 1 = one; 0 = none.
- **EX066 — Rejected file.** Which file was rejected and why? *Rubric:* 3 = mirror file; hash mismatch; 2 = partial; 1 = none; 0 = none.
- **EX067 — Timing.** How long did the rehearsal take? *Rubric:* 3 = 35 minutes; 2 = partial; 1 = none; 0 = none.
- **EX068 — Lesson.** What improvement did the rehearsal show? *Rubric:* 3 = site name in log output; 2 = partial; 1 = none; 0 = none.

### Synthesis

Rehearse the full response with the tools together.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) deliver a supervised improvement project; (2) apply the course; (3) measure the result; (4) present it with limits.

### 18.1 The project

Tomás's project is to reduce the time from advisory publication to all affected customer sites being updated. Before the course, Pinecrest had no inventory; the Ferncroft-type cases were found by customer complaints. The goal is measurable and comes directly from the opening case, where weeks passed before customer complaints revealed the Ferncroft redirects. Reducing the time from advisory to update tests the whole course: inventory, verification, procedures and automation must all work for the figure to improve. Grace supervises the project at Pinecrest and his college tutor assesses it for the course.

### 18.2 Work done

The nightly inventory and advisory comparison, the installation and update procedures with hash or signature verification, the header baseline, file-change monitoring and the removal of unused plugins. Each item answers one of the four Ferncroft gaps: procedures with verification replace mirror downloads, the baseline and permission checks address misconfiguration, and the nightly inventory makes outdated components visible. Removing unused plugins shrinks what the inventory and advisory comparison must track each night. None of the items changes customer sites automatically, keeping the read-only rule intact. Each item is documented in the support knowledge base with its owner.

### 18.3 Measurement

Over three months, Tomás measures median time from advisory to update for high advisories: 5 days across 24 high advisories. Before the project there was no reliable record, so he compares with the Ferncroft case, where weeks passed before anyone noticed. A median of 5 days sits inside the 7-day target for high advisories. Tomás reports the median rather than the average, so a few slow updates do not hide the typical result. All 24 advisories and their update dates come from tickets, which Grace can check.

### 18.4 Limits

The before figure is weak evidence; customer-chosen plugins outside the advisory feeds are not covered; vendor compromises can only be detected, not prevented. Stating these three limits openly keeps the presentation honest about what the figures show. The Ferncroft comparison is one case, not a measured baseline, so it shows the direction of change but not its size. Plugins outside the feeds can only be covered by adding sources, and vendor compromise still depends on detection such as file-change monitoring. The tutor asks Tomás to state these limits in the written report as well.

### 18.5 Presentation

Tomás presents to Grace and his college tutor with evidence from tickets and nightly reports, mapping the work to the SSDF practice groups for responding to vulnerabilities and protecting software. Mapping the work to SSDF practice groups shows that a consumer's routine can follow the same framework producers use, adapted to Pinecrest's role. Evidence from tickets and nightly reports lets Grace and the tutor check each claim, such as the 5-day median, against records rather than Tomás's description of them.

### 18.6 Next steps

Add vendor signature checks where offered and extend the inventory to bundled libraries via SBOMs. Both of these next steps extend checks that the project already performs every night. Signature checks strengthen the verification step for vendors that publish signatures, as the new technician found, and SBOMs extend the inventory beyond plugins to the libraries bundled inside them. Each will need the same synthetic tests and procedure updates before use. Both are scheduled with owners and dates in Pinecrest's plan for the next year.

### Training others

Training the two new technicians tests the documents again: each follows the procedures on the test copies while Tomás watches without helping. Their questions lead to three small edits. By the end of the week both complete an installation and an update correctly, and Grace signs them off for live work.

### Reflection

Tomás writes that the most useful habit was checking sources before installing anything.

### Worked example

The project is assessed as complete. Pinecrest keeps the nightly job and procedures in service, and Grace asks Tomás to train two new technicians on them.

> **Synthetic case.** People and results are synthetic.

### Errors and limits

Report weak comparisons honestly rather than overstating improvement.

### Exercises

- **EX069 — Project goal.** What was the project goal? *Rubric:* 3 = reduce advisory-to-update time; 2 = partial; 1 = none; 0 = none.
- **EX070 — Measure.** What was measured? *Rubric:* 3 = median 5 days for 24 highs; 2 = partial; 1 = none; 0 = none.
- **EX071 — Limits.** Name two limits. *Rubric:* 3 = weak before figure; plugins outside feeds; vendor compromise; 2 = one; 1 = none; 0 = none.
- **EX072 — Next steps.** What are the next steps? *Rubric:* 3 = signatures; SBOMs for bundled libraries; 2 = partial; 1 = none; 0 = none.

### Synthesis

Deliver, measure and present with honest limits.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Tomás Rivera, Grace Okafor, Pinecrest Hosting, Eastbank Technical College, Ferncroft Books and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Server, web server software, application, database and plugins.

**EX002.** Servers, operating system updates and the control panel.

**EX003.** Installing plugins for customers makes support responsible for checking them.

**EX004.** The resize plugin downloaded from a mirror.

**EX005.** DNS lookup, connection to port 443, certificate check, then encrypted HTTP.

**EX006.** Redirect, sign-in required, server error.

**EX007.** They usually mean something on the site was changed.

**EX008.** Only image pages redirected, pointing at the resize plugin.

**EX009.** Each site runs under its own operating system user.

**EX010.** A flaw in any plugin could then change the site's code.

**EX011.** Temporary access only while a ticket is open.

**EX012.** The plugin folder was writable by the web server.

**EX013.** resize-plugin-2.4.1-mirror.zip; do not install.

**EX014.** Whoever changed the file could change a hash stored beside it.

**EX015.** That the file is exactly the released one, not that it has no flaws.

**EX016.** Fields for the vendor hash source and computed hash.

**EX017.** The customer, systems and allowed actions.

**EX018.** What it is, who collected it, when, and its hash.

**EX019.** A new ticket and approval.

**EX020.** Changes can destroy facts needed later.

**EX021.** Vendor writes, publishes with hash, download source, download, verify, install, update.

**EX022.** Use official sources.

**EX023.** Prefer vendors with hashes or signatures and keep an inventory.

**EX024.** Unofficial source, no verification, writable code folder, no inventory.

**EX025.** Five failed admin sign-ins from 198.51.100.7.

**EX026.** An application fault, shown by 500 errors on /shop.

**EX027.** File-change monitoring for code folders.

**EX028.** A prompt to look further, not proof of an attack.

**EX029.** Official sources and hash verification.

**EX030.** Review maintenance yearly and replace abandoned ones.

**EX031.** The update arrives through the legitimate channel; consumers can only detect it quickly.

**EX032.** No rule existed, so it was a process problem.

**EX033.** Each customer site's installed plugins and versions.

**EX034.** As text, 2.10 would sort before 2.9.

**EX035.** High-severity issues on public pages.

**EX036.** They account for over 80% of installations.

**EX037.** Strict-Transport-Security, Content-Security-Policy, X-Content-Type-Options nosniff, Referrer-Policy, and no version-revealing server header.

**EX038.** alder-dental lacked CSP and Referrer-Policy; quayside-gym lacked HSTS and revealed its version.

**EX039.** To find legitimate outside scripts before enforcing.

**EX040.** It blocks scripts loaded from unknown domains by a changed component.

**EX041.** Verification checks that the configured control actually works.

**EX042.** A mismatched test file, a test site with a writable folder, or a page loading an unlisted script.

**EX043.** After template changes, application upgrades, and quarterly.

**EX044.** A template update had dropped Referrer-Policy from 40 sites.

**EX045.** High 1, medium 2.

**EX046.** quayside-gym's resize-plugin 2.5.0 and ferncroft-books' contact-form 5.2.0.

**EX047.** High within 7 days, medium within 30.

**EX048.** A backup and rollback step.

**EX049.** Read the error, check recent changes, reproduce on a test copy, change one thing at a time.

**EX050.** Restore service by rolling back, then diagnose.

**EX051.** Ask the vendor through an official channel before installing.

**EX052.** Applying the update with a renamed setting.

**EX053.** Builds the inventory, compares advisories, checks headers and permissions, and reports.

**EX054.** To limit harm; changes go through technicians.

**EX055.** The site count also dropped, showing missing coverage.

**EX056.** An expired read credential for one cluster.

**EX057.** Plugins bundle libraries the site never chose directly.

**EX058.** Listed explicitly in each site's CSP and recorded in the inventory.

**EX059.** Their files remain on the server.

**EX060.** 140 fewer installations to track across 54 sites.

**EX061.** Confirm ticket, download from official source, verify hash or signature, back up, install with correct permissions, record version and hash.

**EX062.** Work within scope, never install from mirrors, never disable controls, use synthetic test data.

**EX063.** A new technician follows it exactly.

**EX064.** The vendor published a signature, not a hash.

**EX065.** Advisory comparison, hash verification, header check and log summary.

**EX066.** The mirror file, because its hash did not match.

**EX067.** 35 minutes from advisory to plan.

**EX068.** The log summary needed the site name in its output.

**EX069.** Reduce time from advisory to updated sites.

**EX070.** A median of 5 days across 24 high advisories.

**EX071.** Weak before figure, plugins outside feeds, vendor compromise only detectable.

**EX072.** Vendor signature checks and SBOM-based tracking of bundled libraries.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Decan, A., Mens, T., & Constantinou, E. (2018). On the impact of security vulnerabilities in the npm package dependency network. *Proceedings of the 15th International Conference on Mining Software Repositories (MSR '18)*, 181–191. <https://doi.org/10.1145/3196398.3196401>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Johnson, B., Song, Y., Murphy-Hill, E., & Bowdidge, R. (2013). Why don't software developers use static analysis tools to find bugs? *35th International Conference on Software Engineering (ICSE)*, 672–681. <https://doi.org/10.1109/ICSE.2013.6606613>
- Kula, R. G., German, D. M., Ouni, A., Ishio, T., & Inoue, K. (2018). Do developers update their library dependencies? *Empirical Software Engineering*, 23(1), 384–417. <https://doi.org/10.1007/s10664-017-9521-5>
- Ladisa, P., Plate, H., Martinez, M., & Barais, O. (2023). SoK: Taxonomy of attacks on open-source software supply chains. *IEEE Symposium on Security and Privacy*, 1509–1526. <https://doi.org/10.1109/SP46215.2023.10179304>
- Lamb, C., & Zacchiroli, S. (2022). Reproducible builds: Increasing the integrity of software supply chains. *IEEE Software*, 39(2), 62–70. <https://doi.org/10.1109/MS.2021.3073045>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- MITRE. (2024). *CWE Top 25 Most Dangerous Software Weaknesses*. <https://cwe.mitre.org/top25/>
- Newman, Z., Meyers, J. S., & Torres-Arias, S. (2022). Sigstore: Software signing for everybody. *ACM SIGSAC Conference on Computer and Communications Security (CCS '22)*, 2353–2367. <https://doi.org/10.1145/3548606.3560596>
- NTIA. (2021). *The minimum elements for a software bill of materials (SBOM)*. U.S. Department of Commerce. <https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom>
- Ohm, M., Plate, H., Sykosch, A., & Meier, M. (2020). Backstabber's knife collection: A review of open source software supply chain attacks. *DIMVA 2020*, LNCS 12223, 23–43. <https://doi.org/10.1007/978-3-030-52683-2_2>
- OpenSSF. (2023). *SLSA: Supply-chain Levels for Software Artifacts, version 1.0*. <https://slsa.dev/spec/v1.0/>
- OWASP Foundation. (2020). *Software Assurance Maturity Model (SAMM) v2.0*. <https://owaspsamm.org/model/>
- OWASP Foundation. (2020). *Web Security Testing Guide v4.2*. <https://owasp.org/www-project-web-security-testing-guide/>
- OWASP Foundation. (2021). *Application Security Verification Standard 4.0.3*. <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP Foundation. (2021). *OWASP Top 10:2021*. <https://owasp.org/Top10/>
- OWASP Foundation. (2025). *Application Security Verification Standard 5.0.0*. <https://owasp.org/www-project-application-security-verification-standard/>
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley. ISBN 978-1-118-80999-0.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure Software Development Framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
- Thompson, K. (1984). Reflections on trusting trust. *Communications of the ACM*, 27(8), 761–763. <https://doi.org/10.1145/358198.358210>
- Torres-Arias, S., Afzali, H., Kuppusamy, T. K., Curtmola, R., & Cappos, J. (2019). in-toto: Providing farm-to-table guarantees for bits and bytes. *28th USENIX Security Symposium*, 1393–1410. <https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias>
- Wermke, D., Wöhler, N., Klemmer, J. H., Fourné, M., Acar, Y., & Fahl, S. (2022). Committed to trust: A qualitative study on security & trust in open source software projects. *IEEE Symposium on Security and Privacy*, 1880–1896. <https://doi.org/10.1109/SP46214.2022.9833686>
- Zimmermann, M., Staicu, C.-A., Tenny, C., & Pradel, M. (2019). Small world with high risks: A study of security threats in the npm ecosystem. *28th USENIX Security Symposium*, 995–1010. <https://www.usenix.org/conference/usenixsecurity19/presentation/zimmerman>
