<!-- local-deploy-policy-2026-10-12 -->
## Política de deploy local e GitHub Actions (12/10/2026)

- Não usar GitHub Actions neste repositório para CI, deploy, agendamentos ou qualquer outra automação. Não criar, habilitar ou executar workflows em `.github/workflows`.
- Fazer deploy diretamente de um computador local autorizado para AWS, Cloudflare ou outro provedor do projeto, usando os scripts e as credenciais locais aprovadas.
- Antes de publicar, confirmar a conta, o ambiente e o destino, executar as validações locais adequadas e identificar a versão a implantar. Depois, verificar o resultado no provedor.
- Se faltar um procedimento local de deploy, implementá-lo e documentá-lo antes da próxima publicação. Não reativar GitHub Actions para contornar essa falta.
- Referências antigas a GitHub Actions em outros arquivos são legado e não anulam esta política.
<!-- /local-deploy-policy-2026-10-12 -->

# CyKin reader guidance for AI agents

Start at the [home page](README.md). For a complete sequential curriculum, follow the [study path](STUDY_PATH.md): courses 001–207, then each course's `SUBJECTS.md` rows from chapter 01 to the last, following **Next step** into the next course in the same language. The [level index](levels/README.md) supports browsing, and the [AI guide](AI_GUIDE.md) explains the route. Each course links its nine language editions, one [course skill index](SKILLS.md), chapter index, book plan, authored draft when present, and [supplementary playbooks](playbooks/README.md).

- There is **one course skill per course**, in `levels/<level>/<area>/skill/SKILL.md`. Subjects are curriculum modules, with no separate skills. The new authoring target is one distinct book chapter per instructional weekday; see [the curriculum grid](CURRICULUM_GRID.md). Existing subject-chapters are legacy content blocks until expanded, not completed daily lessons.
- Each course has one principal book per language. Read `book/PLAN.md` as an outline and `book/MANUSCRIPT.md` as authored text only where that file exists. A plan is never a finished book.
- At the end of every authored chapter and every `PLAN.md` chapter summary, use its **Continue studying** block to go to the previous chapter, the course chapter index or the next chapter. If it links a plan, state clearly that teaching is not yet authored. Return to `SUBJECTS.md` after the final chapter to reach the next course.
- Keep a learner checkpoint with language, course number, chapter number, source state and exercises attempted. A planned next-step link is navigation, not proof of completion; stop at the first unwritten required lesson and identify any added explanation as supplementary.
- A completed book needs all daily chapters for its level, one worked example and exercise with answer per chapter, at least 50 exercises overall, its verified level-specific A4 floor (at least 300 pages), and editorial review. Check the [book standard](BOOK_STANDARD.md) and [progress review](STRUCTURE_REVIEW.md) before claiming completion.
- The README bookshelf's percentages are generated English **legacy draft-chapter coverage** by area. Its linked matrix shows the same measure for all 207 courses. Read the [sigil key and method](WRITING_PROGRESS.md); do not call these percentages daily-lesson coverage, completed books or progress in other languages.
- The [course writing table](COURSE_WRITING_PROGRESS.md) adds chapter counts, manuscript words and hash-checked A4 measurements for all 207 individual English courses. A course with 100% draft coverage can still have an incomplete book.
- English is the current reference. Other language folders may contain English working outlines pending translation and review; identify that state accurately.
- Cite the exact file and original factual sources. Label fictional cases, preserve third-party rights, and do not claim academic accreditation.
- Books lead the learning path; linked playbooks support practice.
- All teaching content, including unfinished chapter drafts, examples, labs, exercises, worked answers and course skills, belongs in this public repository. The private Engine contains only construction tools, measurements and operational records. A separate public draft is temporary and must be consolidated into the course's one `book/MANUSCRIPT.md`; do not count it as an additional book or lesson.

This public file guides readers and AI clients. Construction tools and operational procedures remain in a separate private editorial workspace.
