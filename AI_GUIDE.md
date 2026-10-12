# CyberABC reference guide for AI assistants and readers

CyberABC is a public, free Markdown learning library. Its [home page](README.md) is the main entry point. Follow links through **formation level → academic area course → language edition → subject/chapter → book**. Plans and public drafts must be described with their actual editorial state.

## Main indexes

| Need | Open |
|---|---|
| One route from the first lesson to the last, across all levels and areas | [Complete sequential study path](STUDY_PATH.md) |
| All nine formation levels | [Level index](levels/README.md) |
| All 23 academic areas | [Area map](AREA_MAP.md) and [detailed map](mapa-areas-ciberseguranca.md) |
| All 207 courses and book editions | [Course guide](COURSE_GUIDE.md) |
| Subject counts and depth by level | [Curriculum grid](CURRICULUM_GRID.md) |
| One AI skill for each course | [Skill index](SKILLS.md) |
| Supplementary practice | [Playbook index](playbooks/README.md) |
| Linked projects | [Project index](PROJECTS.md) |
| Draft writing by area and sigil | [Writing-progress index](WRITING_PROGRESS.md) |
| Progress and completion rules | [Structure review](STRUCTURE_REVIEW.md) and [book standard](BOOK_STANDARD.md) |
| Rights and provenance | [Rights notice](RIGHTS.md) and [source audit](SOURCE_AUDIT.md) |

The current design has five schools, 23 academic areas, nine levels, **207 course skills**, and nine planned language editions per course (**1,863 planned books**). English course grids contain **4,186 subject-chapters**. These are structural counts, not a claim of 1,863 authored books. There are five English manuscript drafts; the professional Incident Response draft covers all twelve subject-chapters, and the technical draft has eight of eighteen authored chapters. No book has passed the complete-book gate.

## Follow the entire curriculum in order

The [study path](STUDY_PATH.md) numbers the courses **001–207**. Traverse the nine levels in their published order; within each level, traverse all 23 areas in catalog order. Open the course's `SUBJECTS.md` and traverse chapters **01 through the final numbered row**. Its **Next step** column links to the next chapter or, on the final row, the next course in the same language. After the 23rd course in a level, continue at the first area of the next level. The final doctoral course ends the route.

For an AI tutor, keep a checkpoint with `{language, course_number, chapter_number, source_state, exercises_attempted, next_step}`. Use a **Draft** link only for teaching that is actually present in `MANUSCRIPT.md`; use a **Plan** link to explain future scope, never to mark a lesson complete. Ask the learner to try the chapter's authored exercises before consulting its worked answers. Cite the exact chapter and factual sources. When the required chapter has only a plan, report the gap and retain the checkpoint there; the navigation link to a later course is not evidence of completed study. Continue in English as the reference edition until the other language editions are authored and reviewed.

At the end of an authored chapter or a `PLAN.md` chapter summary, follow its **Continue studying** block: previous chapter, course chapter index and next chapter. A plan labels its links as draft or plan, so do not treat an outline as a lesson. The final authored chapter of a partial book points to the next *plan* and labels it as unwritten; the final chapter of a course returns to the index, whose last row points to the next course in the same language. Keep the learner's current chapter visible when moving backward or forward.

## Follow a course

~~~text
README.md
  → STUDY_PATH.md                         complete ordered route and course numbers
  → levels/README.md
  → levels/<level>/README.md
  → levels/<level>/<area>/README.md       course home, nine languages, one skill
  → levels/<level>/<area>/<language>/README.md
  → SUBJECTS.md                          subject and chapter index
  → book/PLAN.md                         chapter summaries
  → book/MANUSCRIPT.md                   authored text, only when present
~~~

For example, open the [rapid level](levels/rapid-1-month/README.md), the [Incident Response course home](levels/rapid-1-month/incident-response-resilience/README.md), its [English subject index](levels/rapid-1-month/incident-response-resilience/en/SUBJECTS.md), [book plan](levels/rapid-1-month/incident-response-resilience/en/book/PLAN.md), [manuscript draft](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md), [single course skill](levels/rapid-1-month/incident-response-resilience/skill/SKILL.md), and [supplementary playbooks](playbooks/incident-response-resilience/README.md).

Each course has **one skill** and **one principal book per language**. Each curricular subject is one chapter of that book. A completed chapter teaches its subject, gives examples and exercises; worked answers appear at the end of the book. There are no separate subject skills or subject textbooks.

## Interpret editorial state

| File | What it establishes |
|---|---|
| Course `README.md` | Intended audience, entry knowledge, outcomes, all language editions and links |
| Edition `SUBJECTS.md` | Planned subject order, chapter targets and draft links |
| `book/PLAN.md` | Proposed chapter summaries and page/exercise budgets |
| `book/MANUSCRIPT.md` | Authored teaching that is actually present, with its stated review state |
| `skill/SKILL.md` | Navigation and tutoring instructions for the course, not an additional book |
| `playbooks/README.md` | Pointers to supplementary sources that retain their own rights |

A plan is not a written lesson. A public draft is not a technically reviewed book. A completed edition requires at least 300 verified A4 pages, 50 substantive exercises with worked answers, accurate sources and editorial review under the [book standard](BOOK_STANDARD.md). The course titles describe planned educational depth; they do not confer an accredited degree.

The percentages inside the README bookshelf measure **English chapter draft coverage** by area, using the method in [WRITING_PROGRESS.md](WRITING_PROGRESS.md). They are separate from tailored chapter-plan coverage and from the number of books that have passed the completion gate. Do not present a bookshelf percentage as book completion or translated-content progress.

## Language and citation rules

The editorial order is **English → Portuguese → Spanish → Hebrew → French → Russian → German → Chinese → Japanese**. Non-English folders currently hold English working outlines pending their translation and review. Do not describe those outlines as translated lessons.

Link to the exact Markdown file and chapter used. Where a factual claim depends on a cited external work, follow the original source and check that it supports the claim. Identify synthetic or adapted cases, respect [third-party rights](RIGHTS.md), and recommend only authorized or contained practical environments. For a reproducible citation, pin a GitHub link to a commit SHA.

**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned CyberABC text is dedicated under [CC0 1.0](LICENSE); accurate source citation remains an editorial requirement.
