<!-- local-deploy-policy-2026-10-12 -->
## Política de deploy local e GitHub Actions (12/10/2026)

- Não usar GitHub Actions neste repositório para CI, deploy, agendamentos ou qualquer outra automação. Não criar, habilitar ou executar workflows em `.github/workflows`.
- Fazer deploy diretamente de um computador local autorizado para AWS, Cloudflare ou outro provedor do projeto, usando os scripts e as credenciais locais aprovadas.
- Antes de publicar, confirmar a conta, o ambiente e o destino, executar as validações locais adequadas e identificar a versão a implantar. Depois, verificar o resultado no provedor.
- Se faltar um procedimento local de deploy, implementá-lo e documentá-lo antes da próxima publicação. Não reativar GitHub Actions para contornar essa falta.
- Referências antigas a GitHub Actions em outros arquivos são legado e não anulam esta política.
<!-- /local-deploy-policy-2026-10-12 -->

# CyKin reader guidance for AI agents

Start at [home](README.md), then read the [daily-study standard](DAILY_STUDY_STANDARD.md), [AI guide](AI_GUIDE.md), [study path](STUDY_PATH.md), [book standard](BOOK_STANDARD.md), [course progress](COURSE_WRITING_PROGRESS.md), [rights](RIGHTS.md) and the selected course's current files. Use the repository's present revision, not a remembered conversation state. The course route remains 001–207; the level index also supports independent browsing.

## Daily instruction is the required unit of study

**Effective 2026-10-13, one subject is a chapter containing multiple daily lessons, not one lesson for the whole subject.** Retain one principal `book/MANUSCRIPT.md` per area/level/language and one `skill/SKILL.md` per course. Every Monday–Friday study day needs substantive teaching, an explained example and a distinct primary exercise with a reasoned answer in the final appendix of that same book. Do not create books or skills per day.

Use the [curriculum grid](CURRICULUM_GRID.md) for the nine duration-based reference allocations. The six-month existing track is professional; rapid remains one month. A dated calendar counts actual weekdays across its calendar-month span, not a fixed four-week month. No holiday, vacation, repeated task or missing day may be silently hidden. Longer courses require genuinely greater learning depth and volume, not copied prose or padding.

Read `<language>/DAILY_PLAN.md` alongside `SUBJECTS.md` and `book/PLAN.md`. A daily manifest is navigation, not student-facing content outside the book. Existing text may be exposed as **mapped draft readings** with exact source selectors and exercise-answer pointers, but must not be claimed as newly authored or workload-reviewed daily lessons. A changed source requires revalidation; missing or ambiguous references stop publication of the affected daily view. Preserve old chapter anchors, exercise IDs and learner history.

## Tutoring and progression

Keep `{language, course_number, chapter_number, daily_id, source_revision, source_state, exercises_attempted, feedback, next_step}`. Teach from the selected edition's actual manuscript. Read objectives and prerequisites, explain the assigned source portion and worked example, let the learner attempt the distinct task, then compare its final-book answer. Preserve synthetic-case release boundaries: later source cards cannot justify an earlier decision. Follow each native day's previous/index/next navigation and retain subject-chapter navigation for whole-book reading. Stop completion at the first unwritten required unit; a next link is not evidence of learning.

A plan is not authored teaching; a draft is not a reviewed edition; a course page or calendar is not an accredited program. A complete book requires at least 300 verified qualifying A4 pages, at least `max(50, required daily lessons)` substantive distinct exercises with paired answers, full daily coverage and the remaining technical, linguistic, source, rights and accessibility gates. `EX1000` and later IDs must remain intact in longer courses.

Keep legacy English ≥300-word subject-chapter coverage separate from planned days, mapped readings, native daily drafts, reviewed daily lessons, learner attempts and complete books. Never convert a completed chapter into many completed days or a high bookshelf percentage into finished translations.

## Production and provenance

Write and review the English collection first, starting with Incident Response and its levels, then the other areas. Continue Portuguese, Spanish, Hebrew, French, Russian, German, Chinese and Japanese one language at a time. Preserve valid existing translations and inspect each independently. An English outline or translated interface is not a translated lesson. Do not silently substitute another language when teaching is absent.

Work in sequential batches of five to ten daily units or substantive daily revisions within the existing chapters. Check learning progression, examples, unique primary tasks, answer reasoning, sources, links, safety and actual workload before claiming review. Update daily allocation, course skill, indexes and progress with precise scope and the next required day. Do not let reference page/hour budgets become content ceilings or measured results.

Cite exact files and primary factual sources; label fictional cases and teaching inferences. Preserve third-party rights and relative repository links. Books lead study; [playbooks](playbooks/README.md) remain supplementary. All teaching content—including drafts, examples, labs, exercises, answers and course skills—belongs in this **public** repository. The private Engine contains construction tools, measurements and operational records only. Temporary chapter drafts must be consolidated into the sole manuscript.

Before a write, check the current source SHA and authenticated account. Publish only under hiagokinlevi's actual account; do not falsify authorship or erase history. Preserve parallel changes and read back the result. Distinguish committed website code from a verified live deployment and follow the local policy above. The [daily migration status](DAILY_STUDY_PROGRESS.md) identifies implementation and editorial work still pending.
