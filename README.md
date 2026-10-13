# CyKin — Cybersecurity Academic Books Collection

~~~text
  +------------------------------------------------------------------+
  |         CYKIN / CYBERSECURITY ACADEMIC BOOKS COLLECTION          |
  +------------------------------------------------------------------+
  |     ________    ________    ________    ________    ________     |
  |    |   IR   |  |  CYBR  |  |  INFO  |  |  DATA  |  |  PRIV  |    |
  |    | 100.0% |  |  1.6%  |  | 100.0% |  | 100.0% |  | 100.0% |    |
  |    |________|  |________|  |________|  |________|  |________|    |
  |==================================================================|
  |     ________    ________    ________    ________    ________     |
  |    |  GRC   |  | HUMAN  |  |  ARCH  |  | CRYPT  |  |  WEB3  |    |
  |    | 100.0% |  | 100.0% |  | 100.0% |  | 100.0% |  | 100.0% |    |
  |    |________|  |________|  |________|  |________|  |________|    |
  |==================================================================|
  |     ________    ________    ________    ________    ________     |
  |    |  IAM   |  |  NET   |  |  SYS   |  | CLOUD  |  |  APP   |    |
  |    | 100.0% |  | 100.0% |  | 100.0% |  | 100.0% |  | 100.0% |    |
  |    |________|  |________|  |________|  |________|  |________|    |
  |==================================================================|
  |     ________    ________    ________    ________    ________     |
  |    |  SOC   |  |  DFIR  |  |  CTI   |  |  RED   |  |   AI   |    |
  |    | 100.0% |  | 100.0% |  | 100.0% |  | 100.0% |  | 100.0% |    |
  |    |________|  |________|  |________|  |________|  |________|    |
  |==================================================================|
  |                 ________    ________    ________                 |
  |                |  PQC   |  |   OT   |  |  CRIT  |                |
  |                | 100.0% |  | 100.0% |  | 100.0% |                |
  |                |________|  |________|  |________|                |
  |==================================================================|
  |            ENGLISH DRAFT CHAPTERS / 23 ACADEMIC AREAS            |
  +------------------------------------------------------------------+
~~~

<!-- cykin:onboarding:start -->

## Start here

[Open the CyKin study site](https://cykin.org/) and browse [by level](https://cykin.org/levels/) or [by subject](https://cykin.org/subjects/). Each level and subject leads to separate course pages, and each course has its own lesson guide and book. Subjects organize modules. The weekday calendar sets a minimum number of lessons and no maximum: one chapter, a worked example and an exercise. If an idea needs more lessons, the course grows. English is written first. Existing manuscripts are being expanded from their older subject-chapter structure. Public reading requires no account.

**Route 1 — one course:** 1. language → 2. subject area → 3. level → the complete lesson guide for that course.

**Route 2 — one level:** 1. language → 2. level → 3. all 23 subject areas at that level, with courses and lessons in study order.

The site reads book text from this repository's `main` branch; the links below provide a GitHub-only route through the same curriculum.

| Language | Route 1: choose an area | Route 2: choose a level |
|---|---|---|
| English | [Area → level](onboarding/en/themes.md) | [Level → all areas](onboarding/en/levels.md) |
| Português | [Area → level](onboarding/pt/themes.md) | [Level → all areas](onboarding/pt/levels.md) |
| Español | [Area → level](onboarding/es/themes.md) | [Level → all areas](onboarding/es/levels.md) |
| עברית | [Area → level](onboarding/he/themes.md) | [Level → all areas](onboarding/he/levels.md) |
| Français | [Area → level](onboarding/fr/themes.md) | [Level → all areas](onboarding/fr/levels.md) |
| Русский | [Area → level](onboarding/ru/themes.md) | [Level → all areas](onboarding/ru/levels.md) |
| Deutsch | [Area → level](onboarding/de/themes.md) | [Level → all areas](onboarding/de/levels.md) |
| 中文 | [Area → level](onboarding/zh/themes.md) | [Level → all areas](onboarding/zh/levels.md) |
| 日本語 | [Area → level](onboarding/ja/themes.md) | [Level → all areas](onboarding/ja/levels.md) |

**How to study:** open a course's lesson index (`SUBJECTS.md`), read each available chapter in `MANUSCRIPT.md`, attempt the exercises, compare the worked answers, and follow the links at the end of each chapter. A `PLAN.md` chapter is an outline rather than a written lesson. Hebrew, French, Russian, German, Chinese and Japanese currently have indexes and plans only. The bookshelf above measures initial English chapter coverage; it does not certify finished books or translations. [See coverage by language](LANGUAGE_LESSON_PROGRESS.md).
<!-- cykin:onboarding:end -->

## How the study site works

The [CyKin website](https://cykin.org/) is an in-site reader for this public curriculum. Students choose a language and browse **by level** or **by subject**, then open one separate course page for a level–area combination. The course page shows its current modules, published chapters, exercises, worked answers and previous/index/next navigation; the full principal book is also readable on the site. The planning minimum is shown separately from the chapters actually published, and it is not a maximum. A plan or an untranslated outline is never a completed lesson. The site interface starts in English, detects supported browser languages, and lets readers switch among English, Portuguese and Spanish; each book's actual language and editorial state remain independent of that interface choice.

| Layer | Responsibility | Source in this repository |
|---|---|---|
| Public books | One Markdown `MANUSCRIPT.md` per course and language; `SUBJECTS.md` and `PLAN.md` describe the current curriculum and migration to daily lessons | [`levels/`](levels/README.md) and [book standard](BOOK_STANDARD.md) |
| Frontend | Astro builds the home page, level and subject directories, 207 separate course pages, book reader and account page; the reader renders Markdown and Mermaid diagrams inside the site | [`web/src/`](web/src/) |
| Course catalog | A local build extracts 207 courses, language availability and weekday targets into a static JSON catalog; structural changes need a site deploy | [`web/scripts/build_catalog.py`](web/scripts/build_catalog.py) |
| Public learning API | FastAPI reads the selected public manuscript from this repository's `main` branch and serves the course guide, chapter, book, search and read-only MCP endpoint; new book text becomes available without a frontend build | [`web/api/`](web/api/) and [API guide](web/README.md#public-ai-interface) |
| Optional progress | Cloudflare Access protects only student progress routes; D1 stores completed lessons and exercise attempts. Books, lessons, API and MCP require no registration | [site operations](web/README.md#student-sign-in-and-progress) |
| Hosting and publication | One Cloudflare Python Worker serves FastAPI and Astro static assets at `cykin.org`. The maintainer validates and deploys directly from an authorized local computer; GitHub Actions are not used | [`web/scripts/deploy-local.sh`](web/scripts/deploy-local.sh) and [deployment guide](web/README.md#publish-from-an-authorized-local-computer) |

This architecture keeps the Markdown books as the canonical public source while giving human readers and AI clients stable site routes. The [web application README](web/README.md) contains local development, deployment and endpoint details. The [daily curriculum grid](CURRICULUM_GRID.md) sets a planning minimum of 20 weekday lessons for the rapid month, 130 for six months and 1,300 for five-year engineering, with **no maximum**. These counts are not current completion. English lessons are written first.

**English writing progress:** each percentage is the share of that area's planned English chapters with at least 300 words of authored teaching in a manuscript draft. The bookshelf is refreshed from the manuscripts on each local publication; it does not indicate a finished book or an A4 page count. [Sigil key, exact counts and method](WRITING_PROGRESS.md).

**Public lessons in three languages:** [open the English, Portuguese and Spanish lesson coverage table](LANGUAGE_LESSON_PROGRESS.md). It links each existing book or its plan and counts authored chapters, explicit examples, exercises, navigation and diagrams separately. A public manuscript is readable now; books with pending technical, language or A4 review are identified by the [publication gate](BOOK_STANDARD.md).

**Incident Response book-length checkpoints:** [Rapid](levels/rapid-1-month/incident-response-resilience/README.md): A4 stale after the CyKin rename; last verified 353 pages for prior manuscript SHA-256 a7b0fb3cc2ef0ee5f3433bdbd6b00ecd70bbd528ad31b5d97fc63f4a42724049 · [Professional](levels/professional-6-months/incident-response-resilience/README.md): A4 stale; last verified 132 pages for prior manuscript SHA-256 66783cb9490293ffbdfd573f30f82b45aa24fa6a12ffbebf57ae9f93c8b87790 · [Technical](levels/technical-18-months/incident-response-resilience/README.md): A4 stale after the rename; previous render 124 pages · [Doctoral](levels/doctorate-2-years/incident-response-resilience/README.md): A4 stale after the rename; previous render 122 pages. Recompute the A4 measurements for the new source hashes before claiming a current page floor. These length checkpoints are not completion percentages; the writing queue runs from rapid to doctoral level.

**Published integration — 2026-10-13:** The six early Chapter 2 correction units are part of the [single public English rapid Incident Response manuscript](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md#ch-02). The subsequent [HOLD2 review](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md#ir-rapid-ch02-hold2-binding) adds request-bound authorization, two-sided scope checking, complete lifecycle validation and matching worked explanations. Its program preserves the previous 19 output lines and adds 14 acceptance controls; 114 additional regression assertions were run locally. The former correction-file path remains navigation only. This is publication of scoped teaching improvements, not approval of the complete book or validation of all courses and translations. The next scoped editorial review starts at [Chapter 2, section 2.10](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md#ir-rapid-ch02-vq2-lab), within the still-open full-volume review.

**Q1-S learning expansion — 2026-10-13:** Section 2.9 now includes [qualified identifiers and clock sensitivity](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md#ir-rapid-ch02-q1-scope): a namespace drawing, a minute-scaled interval diagram, a decision flow, an eleven-case offline program and [worked answers](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md#ir-rapid-ch02-q1-scope-result). The original four Q1 outputs remain unchanged. Local checks cover the new eleven-line transcript, four practice variations, 153 event ranges, six row-order permutations and twelve additional malformed inputs. This changes learning depth, not the chapter or numbered-exercise count; the current manuscript needs a fresh word recount and A4 render. Other levels and language editions were not revised in this scoped pass.

**A public, free Markdown learning library for cybersecurity, information security, data governance and digital defense.** Its long-term vision is an online university-style curriculum from first practice to advanced research.

**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned text is dedicated under [CC0 1.0](LICENSE); factual sources are cited and third-party works retain their own rights. Course titles are educational plans, not accredited degrees.

[**Follow the complete 207-course study path**](STUDY_PATH.md) · [**Browse by formation level**](levels/README.md) · [**Start Incident Response**](levels/rapid-1-month/incident-response-resilience/README.md) · [**View all 23 areas**](AREA_MAP.md) · [**Find a skill**](SKILLS.md)

**Start at lesson 01:** [Cybersecurity / rapid / English](levels/rapid-1-month/cybersecurity/en/book/MANUSCRIPT.md#ch-01). At each chapter's end, follow **Continue studying** to the previous chapter, course index or next chapter. The same navigation is present in every book plan. Follow each [course's chapter index](levels/rapid-1-month/cybersecurity/en/SUBJECTS.md) into the next course until the last doctoral chapter. Unwritten chapters are labeled as plans, not lessons.

## How this library is organized

1. **Formation level** — choose one of nine pathways below.
2. **Academic area** — every level has all 23 areas, each represented by one course home.
3. **Language edition** — every course has one planned principal book per language. English is authored and reviewed first.
4. **Subjects and chapters** — subjects are modules; the new schedule calls for one chapter per instructional weekday, each with teaching, a worked example, an exercise and a final worked-answer appendix. Existing editions retain their earlier subject-chapter structure until expanded.
5. **One course skill** — a single `SKILL.md` guides AI clients through the whole course and its chapters. Playbooks are supplementary.

~~~text
levels/<level>/<area>/
├── README.md               course home: objectives, all languages and links
├── skill/SKILL.md          one skill for this course
└── <language>/
    ├── README.md           edition and editorial status
    ├── SUBJECTS.md         all subjects and chapter links
    ├── MATERIALS.md        labs, cases, exercises and references
    └── book/
        ├── PLAN.md          chapter summaries and learning sequence
        └── MANUSCRIPT.md    authored draft, only when present
~~~

**Current structure:** 9 levels × 23 areas = **207 courses and course skills**. With 9 language editions, **1,863 books are planned**. The English plans contain **4,186 legacy subject-chapters**; the new weekday-lesson target is larger and is measured separately. These are plans, not finished books. 199 English manuscripts contain public work in progress; **zero books have passed the complete-book gate**.

**Progress, measured separately:** the folders and course/book plans cover 100% of the current 23-area catalog. Only 336 of 4,186 English chapter briefs have a manually tailored teaching outline so far; the other summaries are template-based working plans. Authored English chapter drafts: **4,007 of 4,186 (95.7%)**, with the area-by-area method in the [writing progress table](WRITING_PROGRESS.md) and [percentages for all 207 courses](COURSE_WRITING_PROGRESS.md). Completed book editions: **0 of 1,863 (0%)**. All 1,863 editions still need to pass the publication gate; see the [progress review](STRUCTURE_REVIEW.md).

A finished book must meet its level's **verified A4 page floor**, have **an exercise and worked answer for every weekday lesson** (at least 50 per book), and pass technical, source, rights, language and accessibility review. The [book standard](BOOK_STANDARD.md) explains the gate.

## 1. Choose a formation level

| Level | Duration | Existing subject modules | Weekday lessons / book target | Open all 23 areas |
|---|---:|---:|---:|---|
| Rapid course | 1 month | 4 | 20 | [Open level](levels/rapid-1-month/README.md) |
| Professional course | 6 months | 12 | 130 | [Open level](levels/professional-6-months/README.md) |
| Technical course | 18 months | 18 | 390 | [Open level](levels/technical-18-months/README.md) |
| Technologist course | 3 years | 30 | 780 | [Open level](levels/technologist-3-years/README.md) |
| Bachelor's course | 4 years | 40 | 1,040 | [Open level](levels/bachelors-4-years/README.md) |
| Engineering course | 5 years | 50 | 1,300 | [Open level](levels/engineering-5-years/README.md) |
| Postgraduate course | 2 years | 12 | 520 | [Open level](levels/postgraduate-2-years/README.md) |
| Master's course | 2 years | 8 | 520 | [Open level](levels/masters-2-years/README.md) |
| Doctoral research track | 2 years | 8 | 520 | [Open level](levels/doctorate-2-years/README.md) |

## 2. English draft progress for every course

Each linked percentage opens one course page with its nine language editions, one skill, book, chapter index, materials, related project and practice playbooks. The percentage is **authored English chapters with at least 300 words of teaching ÷ planned chapters**. It updates when manuscripts and this README are published from the maintainer's machine. **100% means every chapter has a draft start; it does not mean the book or any translation is complete.** All 207 courses are shown here. See [course counts, manuscript words and A4 measurements](COURSE_WRITING_PROGRESS.md) and the [book completion gate](BOOK_STANDARD.md). The five schools are descriptive groupings; the folder hierarchy begins with formation level.

| School / area | Rapid | Professional | Technical | Technologist | Bachelor's | Engineering | Postgraduate | Master's | Doctorate |
|---|---|---|---|---|---|---|---|---|---|
| **Cybersecurity** (School of Cybersecurity Foundations) | [75.0%](levels/rapid-1-month/cybersecurity/README.md) | [0.0%](levels/professional-6-months/cybersecurity/README.md) | [0.0%](levels/technical-18-months/cybersecurity/README.md) | [0.0%](levels/technologist-3-years/cybersecurity/README.md) | [0.0%](levels/bachelors-4-years/cybersecurity/README.md) | [0.0%](levels/engineering-5-years/cybersecurity/README.md) | [0.0%](levels/postgraduate-2-years/cybersecurity/README.md) | [0.0%](levels/masters-2-years/cybersecurity/README.md) | [0.0%](levels/doctorate-2-years/cybersecurity/README.md) |
| **Information security** (School of Cybersecurity Foundations) | [100.0%](levels/rapid-1-month/information-security/README.md) | [100.0%](levels/professional-6-months/information-security/README.md) | [100.0%](levels/technical-18-months/information-security/README.md) | [100.0%](levels/technologist-3-years/information-security/README.md) | [100.0%](levels/bachelors-4-years/information-security/README.md) | [100.0%](levels/engineering-5-years/information-security/README.md) | [100.0%](levels/postgraduate-2-years/information-security/README.md) | [100.0%](levels/masters-2-years/information-security/README.md) | [100.0%](levels/doctorate-2-years/information-security/README.md) |
| **Data governance** (School of Data and Security Governance) | [100.0%](levels/rapid-1-month/data-governance/README.md) | [100.0%](levels/professional-6-months/data-governance/README.md) | [100.0%](levels/technical-18-months/data-governance/README.md) | [100.0%](levels/technologist-3-years/data-governance/README.md) | [100.0%](levels/bachelors-4-years/data-governance/README.md) | [100.0%](levels/engineering-5-years/data-governance/README.md) | [100.0%](levels/postgraduate-2-years/data-governance/README.md) | [100.0%](levels/masters-2-years/data-governance/README.md) | [100.0%](levels/doctorate-2-years/data-governance/README.md) |
| **Privacy and data protection** (School of Data and Security Governance) | [100.0%](levels/rapid-1-month/privacy-data-protection/README.md) | [100.0%](levels/professional-6-months/privacy-data-protection/README.md) | [100.0%](levels/technical-18-months/privacy-data-protection/README.md) | [100.0%](levels/technologist-3-years/privacy-data-protection/README.md) | [100.0%](levels/bachelors-4-years/privacy-data-protection/README.md) | [100.0%](levels/engineering-5-years/privacy-data-protection/README.md) | [100.0%](levels/postgraduate-2-years/privacy-data-protection/README.md) | [100.0%](levels/masters-2-years/privacy-data-protection/README.md) | [100.0%](levels/doctorate-2-years/privacy-data-protection/README.md) |
| **Security governance, risk and compliance** (School of Data and Security Governance) | [100.0%](levels/rapid-1-month/security-governance-risk-compliance/README.md) | [100.0%](levels/professional-6-months/security-governance-risk-compliance/README.md) | [100.0%](levels/technical-18-months/security-governance-risk-compliance/README.md) | [100.0%](levels/technologist-3-years/security-governance-risk-compliance/README.md) | [100.0%](levels/bachelors-4-years/security-governance-risk-compliance/README.md) | [100.0%](levels/engineering-5-years/security-governance-risk-compliance/README.md) | [100.0%](levels/postgraduate-2-years/security-governance-risk-compliance/README.md) | [100.0%](levels/masters-2-years/security-governance-risk-compliance/README.md) | [100.0%](levels/doctorate-2-years/security-governance-risk-compliance/README.md) |
| **Human factors and cyber policy** (School of Data and Security Governance) | [100.0%](levels/rapid-1-month/human-factors-policy/README.md) | [100.0%](levels/professional-6-months/human-factors-policy/README.md) | [100.0%](levels/technical-18-months/human-factors-policy/README.md) | [100.0%](levels/technologist-3-years/human-factors-policy/README.md) | [100.0%](levels/bachelors-4-years/human-factors-policy/README.md) | [100.0%](levels/engineering-5-years/human-factors-policy/README.md) | [100.0%](levels/postgraduate-2-years/human-factors-policy/README.md) | [100.0%](levels/masters-2-years/human-factors-policy/README.md) | [100.0%](levels/doctorate-2-years/human-factors-policy/README.md) |
| **Security architecture and engineering** (School of Secure Engineering) | [100.0%](levels/rapid-1-month/security-architecture/README.md) | [100.0%](levels/professional-6-months/security-architecture/README.md) | [100.0%](levels/technical-18-months/security-architecture/README.md) | [100.0%](levels/technologist-3-years/security-architecture/README.md) | [100.0%](levels/bachelors-4-years/security-architecture/README.md) | [100.0%](levels/engineering-5-years/security-architecture/README.md) | [100.0%](levels/postgraduate-2-years/security-architecture/README.md) | [100.0%](levels/masters-2-years/security-architecture/README.md) | [100.0%](levels/doctorate-2-years/security-architecture/README.md) |
| **Cryptography and trust services** (School of Secure Engineering) | [100.0%](levels/rapid-1-month/cryptography-trust/README.md) | [100.0%](levels/professional-6-months/cryptography-trust/README.md) | [100.0%](levels/technical-18-months/cryptography-trust/README.md) | [100.0%](levels/technologist-3-years/cryptography-trust/README.md) | [100.0%](levels/bachelors-4-years/cryptography-trust/README.md) | [100.0%](levels/engineering-5-years/cryptography-trust/README.md) | [100.0%](levels/postgraduate-2-years/cryptography-trust/README.md) | [100.0%](levels/masters-2-years/cryptography-trust/README.md) | [100.0%](levels/doctorate-2-years/cryptography-trust/README.md) |
| **Web3, blockchain and cryptoasset security** (School of Secure Engineering) | [100.0%](levels/rapid-1-month/web3-blockchain-security/README.md) | [100.0%](levels/professional-6-months/web3-blockchain-security/README.md) | [100.0%](levels/technical-18-months/web3-blockchain-security/README.md) | [100.0%](levels/technologist-3-years/web3-blockchain-security/README.md) | [100.0%](levels/bachelors-4-years/web3-blockchain-security/README.md) | [100.0%](levels/engineering-5-years/web3-blockchain-security/README.md) | [100.0%](levels/postgraduate-2-years/web3-blockchain-security/README.md) | [100.0%](levels/masters-2-years/web3-blockchain-security/README.md) | [100.0%](levels/doctorate-2-years/web3-blockchain-security/README.md) |
| **Identity and access management** (School of Secure Engineering) | [100.0%](levels/rapid-1-month/identity-access/README.md) | [100.0%](levels/professional-6-months/identity-access/README.md) | [100.0%](levels/technical-18-months/identity-access/README.md) | [100.0%](levels/technologist-3-years/identity-access/README.md) | [100.0%](levels/bachelors-4-years/identity-access/README.md) | [100.0%](levels/engineering-5-years/identity-access/README.md) | [100.0%](levels/postgraduate-2-years/identity-access/README.md) | [100.0%](levels/masters-2-years/identity-access/README.md) | [100.0%](levels/doctorate-2-years/identity-access/README.md) |
| **Network and communications security** (School of Secure Engineering) | [100.0%](levels/rapid-1-month/network-communications/README.md) | [100.0%](levels/professional-6-months/network-communications/README.md) | [100.0%](levels/technical-18-months/network-communications/README.md) | [100.0%](levels/technologist-3-years/network-communications/README.md) | [100.0%](levels/bachelors-4-years/network-communications/README.md) | [100.0%](levels/engineering-5-years/network-communications/README.md) | [100.0%](levels/postgraduate-2-years/network-communications/README.md) | [100.0%](levels/masters-2-years/network-communications/README.md) | [100.0%](levels/doctorate-2-years/network-communications/README.md) |
| **Systems, endpoints and hardware security** (School of Secure Engineering) | [100.0%](levels/rapid-1-month/systems-endpoints-hardware/README.md) | [100.0%](levels/professional-6-months/systems-endpoints-hardware/README.md) | [100.0%](levels/technical-18-months/systems-endpoints-hardware/README.md) | [100.0%](levels/technologist-3-years/systems-endpoints-hardware/README.md) | [100.0%](levels/bachelors-4-years/systems-endpoints-hardware/README.md) | [100.0%](levels/engineering-5-years/systems-endpoints-hardware/README.md) | [100.0%](levels/postgraduate-2-years/systems-endpoints-hardware/README.md) | [100.0%](levels/masters-2-years/systems-endpoints-hardware/README.md) | [100.0%](levels/doctorate-2-years/systems-endpoints-hardware/README.md) |
| **Cloud and container security** (School of Secure Engineering) | [100.0%](levels/rapid-1-month/cloud-containers/README.md) | [100.0%](levels/professional-6-months/cloud-containers/README.md) | [100.0%](levels/technical-18-months/cloud-containers/README.md) | [100.0%](levels/technologist-3-years/cloud-containers/README.md) | [100.0%](levels/bachelors-4-years/cloud-containers/README.md) | [100.0%](levels/engineering-5-years/cloud-containers/README.md) | [100.0%](levels/postgraduate-2-years/cloud-containers/README.md) | [100.0%](levels/masters-2-years/cloud-containers/README.md) | [100.0%](levels/doctorate-2-years/cloud-containers/README.md) |
| **Application and software supply chain security** (School of Secure Engineering) | [100.0%](levels/rapid-1-month/application-supply-chain/README.md) | [100.0%](levels/professional-6-months/application-supply-chain/README.md) | [100.0%](levels/technical-18-months/application-supply-chain/README.md) | [100.0%](levels/technologist-3-years/application-supply-chain/README.md) | [100.0%](levels/bachelors-4-years/application-supply-chain/README.md) | [100.0%](levels/engineering-5-years/application-supply-chain/README.md) | [100.0%](levels/postgraduate-2-years/application-supply-chain/README.md) | [100.0%](levels/masters-2-years/application-supply-chain/README.md) | [100.0%](levels/doctorate-2-years/application-supply-chain/README.md) |
| **Security operations and blue team** (School of Cyber Defense and Operations) | [100.0%](levels/rapid-1-month/security-operations-blue-team/README.md) | [100.0%](levels/professional-6-months/security-operations-blue-team/README.md) | [100.0%](levels/technical-18-months/security-operations-blue-team/README.md) | [100.0%](levels/technologist-3-years/security-operations-blue-team/README.md) | [100.0%](levels/bachelors-4-years/security-operations-blue-team/README.md) | [100.0%](levels/engineering-5-years/security-operations-blue-team/README.md) | [100.0%](levels/postgraduate-2-years/security-operations-blue-team/README.md) | [100.0%](levels/masters-2-years/security-operations-blue-team/README.md) | [100.0%](levels/doctorate-2-years/security-operations-blue-team/README.md) |
| **Incident response and cyber resilience** (School of Cyber Defense and Operations) | [100.0%](levels/rapid-1-month/incident-response-resilience/README.md) | [100.0%](levels/professional-6-months/incident-response-resilience/README.md) | [100.0%](levels/technical-18-months/incident-response-resilience/README.md) | [100.0%](levels/technologist-3-years/incident-response-resilience/README.md) | [100.0%](levels/bachelors-4-years/incident-response-resilience/README.md) | [100.0%](levels/engineering-5-years/incident-response-resilience/README.md) | [100.0%](levels/postgraduate-2-years/incident-response-resilience/README.md) | [100.0%](levels/masters-2-years/incident-response-resilience/README.md) | [100.0%](levels/doctorate-2-years/incident-response-resilience/README.md) |
| **Digital forensics and malware analysis** (School of Cyber Defense and Operations) | [100.0%](levels/rapid-1-month/digital-forensics-malware/README.md) | [100.0%](levels/professional-6-months/digital-forensics-malware/README.md) | [100.0%](levels/technical-18-months/digital-forensics-malware/README.md) | [100.0%](levels/technologist-3-years/digital-forensics-malware/README.md) | [100.0%](levels/bachelors-4-years/digital-forensics-malware/README.md) | [100.0%](levels/engineering-5-years/digital-forensics-malware/README.md) | [100.0%](levels/postgraduate-2-years/digital-forensics-malware/README.md) | [100.0%](levels/masters-2-years/digital-forensics-malware/README.md) | [100.0%](levels/doctorate-2-years/digital-forensics-malware/README.md) |
| **Threat intelligence and OSINT** (School of Cyber Defense and Operations) | [100.0%](levels/rapid-1-month/threat-intelligence-osint/README.md) | [100.0%](levels/professional-6-months/threat-intelligence-osint/README.md) | [100.0%](levels/technical-18-months/threat-intelligence-osint/README.md) | [100.0%](levels/technologist-3-years/threat-intelligence-osint/README.md) | [100.0%](levels/bachelors-4-years/threat-intelligence-osint/README.md) | [100.0%](levels/engineering-5-years/threat-intelligence-osint/README.md) | [100.0%](levels/postgraduate-2-years/threat-intelligence-osint/README.md) | [100.0%](levels/masters-2-years/threat-intelligence-osint/README.md) | [100.0%](levels/doctorate-2-years/threat-intelligence-osint/README.md) |
| **Authorized offensive security and red team** (School of Cyber Defense and Operations) | [100.0%](levels/rapid-1-month/offensive-security-red-team/README.md) | [100.0%](levels/professional-6-months/offensive-security-red-team/README.md) | [100.0%](levels/technical-18-months/offensive-security-red-team/README.md) | [100.0%](levels/technologist-3-years/offensive-security-red-team/README.md) | [100.0%](levels/bachelors-4-years/offensive-security-red-team/README.md) | [100.0%](levels/engineering-5-years/offensive-security-red-team/README.md) | [100.0%](levels/postgraduate-2-years/offensive-security-red-team/README.md) | [100.0%](levels/masters-2-years/offensive-security-red-team/README.md) | [100.0%](levels/doctorate-2-years/offensive-security-red-team/README.md) |
| **AI and machine-learning security** (School of Emerging and Critical Systems) | [100.0%](levels/rapid-1-month/ai-security/README.md) | [100.0%](levels/professional-6-months/ai-security/README.md) | [100.0%](levels/technical-18-months/ai-security/README.md) | [100.0%](levels/technologist-3-years/ai-security/README.md) | [100.0%](levels/bachelors-4-years/ai-security/README.md) | [100.0%](levels/engineering-5-years/ai-security/README.md) | [100.0%](levels/postgraduate-2-years/ai-security/README.md) | [100.0%](levels/masters-2-years/ai-security/README.md) | [100.0%](levels/doctorate-2-years/ai-security/README.md) |
| **Quantum and post-quantum security** (School of Emerging and Critical Systems) | [100.0%](levels/rapid-1-month/quantum-post-quantum-security/README.md) | [100.0%](levels/professional-6-months/quantum-post-quantum-security/README.md) | [100.0%](levels/technical-18-months/quantum-post-quantum-security/README.md) | [100.0%](levels/technologist-3-years/quantum-post-quantum-security/README.md) | [100.0%](levels/bachelors-4-years/quantum-post-quantum-security/README.md) | [100.0%](levels/engineering-5-years/quantum-post-quantum-security/README.md) | [100.0%](levels/postgraduate-2-years/quantum-post-quantum-security/README.md) | [100.0%](levels/masters-2-years/quantum-post-quantum-security/README.md) | [100.0%](levels/doctorate-2-years/quantum-post-quantum-security/README.md) |
| **OT, IoT and cyber-physical security** (School of Emerging and Critical Systems) | [100.0%](levels/rapid-1-month/ot-iot-security/README.md) | [100.0%](levels/professional-6-months/ot-iot-security/README.md) | [100.0%](levels/technical-18-months/ot-iot-security/README.md) | [100.0%](levels/technologist-3-years/ot-iot-security/README.md) | [100.0%](levels/bachelors-4-years/ot-iot-security/README.md) | [100.0%](levels/engineering-5-years/ot-iot-security/README.md) | [100.0%](levels/postgraduate-2-years/ot-iot-security/README.md) | [100.0%](levels/masters-2-years/ot-iot-security/README.md) | [100.0%](levels/doctorate-2-years/ot-iot-security/README.md) |
| **Critical infrastructure and sector security** (School of Emerging and Critical Systems) | [100.0%](levels/rapid-1-month/critical-sector-security/README.md) | [100.0%](levels/professional-6-months/critical-sector-security/README.md) | [100.0%](levels/technical-18-months/critical-sector-security/README.md) | [100.0%](levels/technologist-3-years/critical-sector-security/README.md) | [100.0%](levels/bachelors-4-years/critical-sector-security/README.md) | [100.0%](levels/engineering-5-years/critical-sector-security/README.md) | [100.0%](levels/postgraduate-2-years/critical-sector-security/README.md) | [100.0%](levels/masters-2-years/critical-sector-security/README.md) | [100.0%](levels/doctorate-2-years/critical-sector-security/README.md) |

[Detailed area map](mapa-areas-ciberseguranca.md) · [All course and book links](COURSE_GUIDE.md) · [English subject counts](CURRICULUM_GRID.md)

## First English book in progress

The [Incident Response rapid-course draft](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md) has four authored chapter drafts, 50 numbered exercises and a final worked-answer appendix. Chapter 1 develops readiness, booking behavior, source boundaries, the AR1 pre-incident authority-rehearsal lab and the separate PATH1 service-function/degraded-mode lab. Chapter 2 develops TRI2 evidence-bounded priority reassessment, preservation, query coverage, impact measurement, the MIN2 privacy-aware reviewer-view lab and the separate HOLD2 source-hold lifecycle laboratory. Chapter 3 adds RB3 containment-reversal readiness, G3-DG decision gates and MQ3 queue reconciliation: failed checks outrank missing checks, duplicate receipts and conflicting keys are held, and a 09:52 planning review is distinct from fifteen minutes of verified protection. RTE3 measures evidence-bounded recovery: service interruption to owner acceptance, copy age versus proved missing writes, and explicit unknown states. Chapter 4 adds BH4 blind handoff reconstruction: a new responder locates sources, distinguishes proposal from reported action, preserves failed gates and chooses an authorized next request. These synthetic outputs and exercise extensions remain distinct from canonical case evidence. The principal manuscript now contains **146,069 whitespace-separated words** across teaching, exercises, answers and references, with R1X–R4X and the integrated CH04 release, receipt and worked-answer corrections. An earlier source rendered to **353 A4 pages** for SHA-256 `a7b0fb3cc2ef0ee5f3433bdbd6b00ecd70bbd528ad31b5d97fc63f4a42724049`; the CyKin rename changed the source hash, so this page count requires a fresh render. It remains a **draft** pending comprehensive specialist, technical, source, rights, language and accessibility review. Other English Incident Response manuscripts and their actual chapter coverage appear in the [207-course writing table](COURSE_WRITING_PROGRESS.md); a draft or 100% chapter coverage is not a completed book. All 182 Incident Response chapter briefs and 154 Cybersecurity briefs have individual teaching plans; the remaining English chapters are on the editorial queue. The [study path](STUDY_PATH.md) and each chapter's previous/index/next navigation guide the learner. All language editions still need their own writing and review.

**A4 length check:** The prior rapid Incident Response manuscript (SHA-256 `a7b0fb3cc2ef0ee5f3433bdbd6b00ecd70bbd528ad31b5d97fc63f4a42724049`) rendered to **353 A4 pages** with the local Engine preview method on 13 October 2026. All pages contained extractable text; three code-heavy pages were sparse and need layout review. This historical measurement applies to that exact source and layout only. Rerender the renamed manuscript before reporting a current page count. The book remains a draft until the [complete editorial gate](BOOK_STANDARD.md) passes.

## Language sequence

**English → Portuguese → Spanish → Hebrew → French → Russian → German → Chinese → Japanese.** Complete and review the English collection before translating; each later language receives its own technical and linguistic review. Some non-English folders already contain partial manuscripts alongside working outlines; no translation is verified complete.

## Existing projects

**27 curated active repositories from the [hiagokinlevi account](https://github.com/hiagokinlevi?tab=repositories), checked 11 October 2026.** This inventory includes the current learning platform, 13 original security projects, two research repositories, nine forks, and two profile or website repositories. It is a project index, separate from the **23 CyKin academic areas**. Each linked repository has its own scope, state, authorship history, and license; inclusion here does not make its contents part of a completed CyKin course.

### Learning platform · 1

- [CyKin](https://github.com/hiagokinlevi/CyKin) — public curriculum, study plans, books, and learner materials.

### Original security software · 13

| Focus | Repositories |
|---|---|
| Detection and response | [honeypot-foundry](https://github.com/hiagokinlevi/honeypot-foundry) · [dfir-attack-lab](https://github.com/hiagokinlevi/dfir-attack-lab) · [ir-playbooks-automation](https://github.com/hiagokinlevi/ir-playbooks-automation) |
| Applications and delivery | [waf-defense-rulepacks](https://github.com/hiagokinlevi/waf-defense-rulepacks) · [secure-pipeline-blueprints](https://github.com/hiagokinlevi/secure-pipeline-blueprints) · [offensive-gvuln](https://github.com/hiagokinlevi/offensive-gvuln) |
| Cloud and infrastructure | [cloud-posture-watch](https://github.com/hiagokinlevi/cloud-posture-watch) · [iam-audit-lab](https://github.com/hiagokinlevi/iam-audit-lab) · [container-defense-stack](https://github.com/hiagokinlevi/container-defense-stack) |
| Secrets and exposure | [secret-leak-sentinel](https://github.com/hiagokinlevi/secret-leak-sentinel) · [phishing-surface-monitor](https://github.com/hiagokinlevi/phishing-surface-monitor) |
| AI and cryptography | [ai-security-guardrails](https://github.com/hiagokinlevi/ai-security-guardrails) · [cryptologik](https://github.com/hiagokinlevi/cryptologik) |

### Study routes from the original projects

Each original project links to a related CyKin course. The course home links its nine editions, principal book, chapter index, one skill and supplementary playbooks.

| Project | Related course |
|---|---|
| [honeypot-foundry](https://github.com/hiagokinlevi/honeypot-foundry) | [Security operations and blue team](levels/rapid-1-month/security-operations-blue-team/README.md) |
| [dfir-attack-lab](https://github.com/hiagokinlevi/dfir-attack-lab) | [Digital forensics and malware analysis](levels/rapid-1-month/digital-forensics-malware/README.md) |
| [ir-playbooks-automation](https://github.com/hiagokinlevi/ir-playbooks-automation) | [Incident response and cyber resilience](levels/rapid-1-month/incident-response-resilience/README.md) |
| [waf-defense-rulepacks](https://github.com/hiagokinlevi/waf-defense-rulepacks) | [Network and communications security](levels/rapid-1-month/network-communications/README.md) |
| [secure-pipeline-blueprints](https://github.com/hiagokinlevi/secure-pipeline-blueprints) | [Application and software supply chain security](levels/rapid-1-month/application-supply-chain/README.md) |
| [offensive-gvuln](https://github.com/hiagokinlevi/offensive-gvuln) | [Authorized offensive security and red team](levels/rapid-1-month/offensive-security-red-team/README.md) |
| [cloud-posture-watch](https://github.com/hiagokinlevi/cloud-posture-watch) | [Cloud and container security](levels/rapid-1-month/cloud-containers/README.md) |
| [iam-audit-lab](https://github.com/hiagokinlevi/iam-audit-lab) | [Identity and access management](levels/rapid-1-month/identity-access/README.md) |
| [container-defense-stack](https://github.com/hiagokinlevi/container-defense-stack) | [Cloud and container security](levels/rapid-1-month/cloud-containers/README.md) |
| [secret-leak-sentinel](https://github.com/hiagokinlevi/secret-leak-sentinel) | [Information security](levels/rapid-1-month/information-security/README.md) |
| [phishing-surface-monitor](https://github.com/hiagokinlevi/phishing-surface-monitor) | [Threat intelligence and OSINT](levels/rapid-1-month/threat-intelligence-osint/README.md) |
| [ai-security-guardrails](https://github.com/hiagokinlevi/ai-security-guardrails) | [AI and machine-learning security](levels/rapid-1-month/ai-security/README.md) |
| [cryptologik](https://github.com/hiagokinlevi/cryptologik) | [Cryptography and trust services](levels/rapid-1-month/cryptography-trust/README.md) |

### Original research · 2

- [ADAI-Autonomous-Defensive-Artificial-Intelligence](https://github.com/hiagokinlevi/ADAI-Autonomous-Defensive-Artificial-Intelligence) — research on governed autonomous defensive AI.
- [DAI-Decripte-Artificial-Intelligence-LLM](https://github.com/hiagokinlevi/DAI-Decripte-Artificial-Intelligence-LLM) — research on a security-focused language model and verifiable authority.

For related learning, open the [AI and machine-learning security course](levels/rapid-1-month/ai-security/README.md) and choose a formation level from the [complete level index](levels/README.md). The research repositories remain independent sources.

### Forked reference collections · 9

These are **forks of other projects**. Their upstream authorship and license terms remain with their respective sources; check each repository before reuse.

- [AwesomeResponsibleAI](https://github.com/hiagokinlevi/AwesomeResponsibleAI) · [awesome-llm-security-alignment](https://github.com/hiagokinlevi/awesome-llm-security-alignment) · [Awesome-LLM4SecOps](https://github.com/hiagokinlevi/Awesome-LLM4SecOps)
- [LLM-security-and-privacy](https://github.com/hiagokinlevi/LLM-security-and-privacy) · [prompt-injection-defenses](https://github.com/hiagokinlevi/prompt-injection-defenses) · [awesome-agentic-hardening](https://github.com/hiagokinlevi/awesome-agentic-hardening)
- [awesome-ai-agent-governance](https://github.com/hiagokinlevi/awesome-ai-agent-governance) · [awesome-ai-security](https://github.com/hiagokinlevi/awesome-ai-security) · [awesome-llm-security](https://github.com/hiagokinlevi/awesome-llm-security)

### Public profile and website · 2

- [hiagokinlevi](https://github.com/hiagokinlevi/hiagokinlevi) — GitHub profile repository.
- [hiagokinlevi.github.io](https://github.com/hiagokinlevi/hiagokinlevi.github.io) — public portfolio website.

The [project categories](CATEGORIES.md) give context for the original security software. New public repositories can be added to this index without changing the academic taxonomy.

## Rights, progress and navigation

Original maintainer-owned content is public and dedicated to the public domain under [CC0 1.0](LICENSE). Accurate citation of factual sources remains an editorial requirement. Linked repositories and third-party works retain their own licenses.

[Level index](levels/README.md) · [Area map](AREA_MAP.md) · [Book guide](guia-geral-cursos-e-livros.md) · [Course skills](SKILLS.md) · [Playbooks](playbooks/README.md) · [AI navigation](AI_GUIDE.md) · [Writing by area](WRITING_PROGRESS.md) · [Writing by course](COURSE_WRITING_PROGRESS.md) · [Progress](STRUCTURE_REVIEW.md) · [Roadmap](ROADMAP.md) · [Sources](SOURCE_AUDIT.md) · [Rights](RIGHTS.md) · [Project categories](CATEGORIES.md)

Construction scripts, tests, measurements and operational records stay in a separate private editorial workspace. All teaching Markdown, including unfinished chapter drafts, belongs in this public repository and is published directly from the maintainer's machine. Separate chapter drafts are temporary and will be consolidated into the course's single principal book.
