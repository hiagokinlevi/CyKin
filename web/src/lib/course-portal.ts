import { renderMarkdown } from './reader';
import { siteLanguage } from './i18n';

type Unit = { kind: 'daily' | 'chapter'; number: number };
type Entry = { chapter: number; title: string; module: number; published: boolean; source_url: string | null };
type Module = { number: number; kind: string; title: string; chapters: number[] };
type CourseDetails = {
  course: { instructional_weeks: number; daily_lesson_target: number };
  lessons: Entry[]; modules: Module[]; daily_slots: Entry[]; legacy_chapters: Entry[];
  published_chapters: number; published_lessons: number; planned_lessons: number;
  has_daily_lessons: boolean; book_url: string | null;
};
type LessonData = {
  chapter: number; title: string; markdown: string; worked_answers: string;
  exercise_ids: string[]; source_url: string; content_kind: string;
};

export async function initCoursePortal(): Promise<void> {
  const el = (id: string) => document.getElementById(id)!;
  const root = el('course-root');
  const level = root.dataset.level!, area = root.dataset.area!, courseNumber = Number(root.dataset.number);
  const firstQuery = new URLSearchParams(location.search);
  const selector = el('course-language') as HTMLSelectElement;
  let language = firstQuery.get('lang') || siteLanguage();
  if (!['en', 'pt', 'es', 'he', 'fr', 'ru', 'de', 'zh', 'ja'].includes(language)) language = 'en';
  selector.value = language;
  let details: CourseDetails;
  let current: Unit | null = null;
  let requestId = 0;
  let indexMode: Unit['kind'] = 'daily';
  let selectedWeek = 1;

  function entries(kind: Unit['kind']): Entry[] {
    return kind === 'daily' ? details.daily_slots : details.legacy_chapters;
  }
  function entry(unit: Unit): Entry | undefined {
    return entries(unit.kind).find(item => item.chapter === unit.number);
  }
  function url(unit: Unit | null): string {
    const params = new URLSearchParams({ lang: language });
    if (firstQuery.has('ui')) params.set('ui', firstQuery.get('ui')!);
    if (unit) { params.set('unit', unit.kind); params.set('chapter', String(unit.number)); }
    return location.pathname + '?' + params;
  }
  function bookUrl(anchor?: string): string {
    const params = new URLSearchParams({ level, area, lang: language });
    if (firstQuery.has('ui')) params.set('ui', firstQuery.get('ui')!);
    return '/book/?' + params + (anchor || '');
  }
  function link(label: string, href: string, className = 'button secondary'): HTMLAnchorElement {
    const node = document.createElement('a'); node.href = href; node.className = className; node.textContent = label; return node;
  }
  function unitLink(unit: Unit, item: Entry, className: string): HTMLElement {
    const node = item.published ? link('', url(unit), className) : document.createElement('div');
    if (!item.published) node.className = `${className} is-planned`;
    const number = document.createElement('span'); number.className = 'lesson-number'; number.textContent = String(unit.number).padStart(2, '0');
    const title = document.createElement('span'); title.className = 'lesson-subject'; title.textContent = item.title;
    const state = document.createElement('span'); state.className = 'lesson-state'; state.textContent = item.published ? 'Read on OpenCyber Academy →' : 'Planned · teaching pending';
    node.append(number, title, state);
    if (current?.kind === unit.kind && current.number === unit.number) { node.classList.add('active'); node.setAttribute('aria-current', 'page'); }
    if (item.published) node.addEventListener('click', event => { event.preventDefault(); void openUnit(unit, true); });
    return node;
  }
  function weekLabel(week: number): string {
    const module = details.modules.find(item => item.number === week);
    return module && details.has_daily_lessons ? `Week ${String(week).padStart(2, '0')} · ${module.title}` : `Week ${String(week).padStart(2, '0')}`;
  }
  function renderIndex(): void {
    const nav = el('course-lessons');
    nav.replaceChildren();
    const switches = document.createElement('div'); switches.className = 'course-index-switch';
    for (const [kind, label] of [['daily', 'Daily lessons'], ['chapter', 'Full chapters']] as const) {
      const button = document.createElement('button'); button.type = 'button'; button.textContent = label;
      button.setAttribute('aria-pressed', String(indexMode === kind));
      button.addEventListener('click', () => { indexMode = kind; renderIndex(); });
      switches.append(button);
    }
    nav.append(switches);
    if (indexMode === 'daily' && details.daily_slots.length) {
      const weeks = Math.ceil(details.daily_slots.length / 5);
      selectedWeek = Math.max(1, Math.min(weeks, selectedWeek));
      const picker = document.createElement('div'); picker.className = 'course-week-picker';
      const previous = document.createElement('button'); previous.type = 'button'; previous.textContent = '←'; previous.setAttribute('aria-label', 'Previous week'); previous.disabled = selectedWeek === 1;
      const next = document.createElement('button'); next.type = 'button'; next.textContent = '→'; next.setAttribute('aria-label', 'Next week'); next.disabled = selectedWeek === weeks;
      const selector = document.createElement('select'); selector.setAttribute('aria-label', 'Choose study week');
      for (let week = 1; week <= weeks; week++) {
        const days = details.daily_slots.slice((week - 1) * 5, week * 5);
        const option = document.createElement('option'); option.value = String(week);
        option.textContent = `Week ${String(week).padStart(2, '0')} · ${days.filter(day => day.published).length}/${days.length} written`;
        selector.append(option);
      }
      selector.value = String(selectedWeek);
      selector.addEventListener('change', () => { selectedWeek = Number(selector.value); renderIndex(); });
      previous.addEventListener('click', () => { selectedWeek--; renderIndex(); });
      next.addEventListener('click', () => { selectedWeek++; renderIndex(); });
      picker.append(previous, selector, next); nav.append(picker);
      const heading = document.createElement('h3'); heading.className = 'course-index-heading'; heading.textContent = weekLabel(selectedWeek); nav.append(heading);
      const days = details.daily_slots.slice((selectedWeek - 1) * 5, selectedWeek * 5);
      for (const day of days) nav.append(unitLink({ kind: 'daily', number: day.chapter }, day, 'course-lesson'));
      const note = document.createElement('p'); note.className = 'course-index-note'; note.textContent = 'Study one written lesson at a time. Planned lessons have no teaching text yet.'; nav.append(note);
    } else {
      const heading = document.createElement('h3'); heading.className = 'course-index-heading'; heading.textContent = 'Complete chapters'; nav.append(heading);
      const note = document.createElement('p'); note.className = 'course-index-note'; note.textContent = 'Read the full subject chapters in this course book.'; nav.append(note);
      for (const chapter of details.legacy_chapters) nav.append(unitLink({ kind: 'chapter', number: chapter.chapter }, chapter, 'course-lesson'));
    }
  }
  function renderOverview(): void {
    const overview = el('course-overview'); overview.replaceChildren();
    const cadence = document.createElement('section'); cadence.className = 'course-cadence';
    const eyebrow = document.createElement('div'); eyebrow.className = 'eyebrow'; eyebrow.textContent = 'MONDAY–FRIDAY STUDY PLAN';
    const title = document.createElement('h3'); title.textContent = `${details.course.instructional_weeks} weeks · ${details.course.daily_lesson_target} planned daily lessons`;
    const copy = document.createElement('p'); copy.textContent = 'One weekday lesson at a time. Read the explanation and worked example, solve the exercise, then compare the answer. A planned slot opens only after its teaching has been written.';
    const weekdays = document.createElement('div'); weekdays.className = 'course-weekdays';
    for (const day of ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']) { const chip = document.createElement('span'); chip.textContent = day; weekdays.append(chip); }
    const availability = document.createElement('p'); availability.className = 'course-availability';
    availability.textContent = `${details.published_lessons} of ${details.planned_lessons} daily lessons written · ${details.published_chapters} existing subject chapters readable`;
    cadence.append(eyebrow, title, copy, weekdays, availability); overview.append(cadence);

    const firstDaily = details.daily_slots.find(item => item.published);
    const firstChapter = details.legacy_chapters.find(item => item.published);
    if (firstDaily || firstChapter) {
      const start = firstDaily ? { kind: 'daily' as const, number: firstDaily.chapter } : { kind: 'chapter' as const, number: firstChapter!.chapter };
      const action = link(firstDaily ? 'Begin with Day 1 →' : 'Begin with Chapter 1 →', url(start), 'button gold');
      action.classList.add('course-start-action');
      action.addEventListener('click', event => { event.preventDefault(); void openUnit(start, true); });
      cadence.append(action);
    }

    const heading = document.createElement('h3'); heading.textContent = details.has_daily_lessons ? 'This course, week by week' : 'Published course chapters'; overview.append(heading);
    const grid = document.createElement('div'); grid.className = 'course-module-grid';
    const weeksWithTeaching = new Set(details.daily_slots.filter(item => item.published).map(item => Math.ceil(item.chapter / 5)));
    const visibleWeeks = new Set([...weeksWithTeaching, ...Array.from({ length: Math.min(3, details.course.instructional_weeks) }, (_, index) => index + 1)]);
    for (const week of [...visibleWeeks].sort((a, b) => a - b)) {
      const days = details.daily_slots.slice((week - 1) * 5, week * 5);
      if (!days.length) continue;
      const card = document.createElement('section'); card.className = 'course-module-card';
      const title = document.createElement('h4'); title.textContent = weekLabel(week);
      const count = document.createElement('p'); count.textContent = `${days.filter(item => item.published).length} of ${days.length} daily lessons written`;
      const list = document.createElement('div'); list.className = 'course-module-list';
      for (const day of days) list.append(unitLink({ kind: 'daily', number: day.chapter }, day, 'course-overview-lesson'));
      card.append(title, count, list); grid.append(card);
    }
    overview.append(grid);
    if (details.legacy_chapters.some(chapter => chapter.published)) {
      const chapters = document.createElement('details'); chapters.className = 'course-chapter-browse';
      if (!details.has_daily_lessons) chapters.open = true;
      const summary = document.createElement('summary'); summary.textContent = `Browse all ${details.published_chapters} full chapters`;
      const list = document.createElement('div'); list.className = 'course-chapter-list';
      for (const chapter of details.legacy_chapters.filter(item => item.published)) list.append(unitLink({ kind: 'chapter', number: chapter.chapter }, chapter, 'course-overview-lesson'));
      chapters.append(summary, list); overview.append(chapters);
    }
    const help = document.createElement('p'); help.className = 'course-index-note'; help.textContent = 'Use the guide at left to choose any week or chapter.'; overview.append(help);
  }
  function renderFacts(): void {
    const facts = el('course-facts'); facts.replaceChildren(); facts.hidden = false;
    for (const value of [`${details.course.instructional_weeks} study weeks`, `${details.published_lessons}/${details.planned_lessons} daily lessons written`, `${details.published_chapters} chapters readable`]) {
      const fact = document.createElement('span'); fact.textContent = value; facts.append(fact);
    }
  }
  function renderNavigation(unit: Unit | null): void {
    for (const nav of [el('course-lesson-nav-top'), el('course-lesson-nav')]) {
      nav.replaceChildren(); nav.hidden = nav.id === 'course-lesson-nav-top' && unit === null;
      if (unit === null) {
        const first = details.daily_slots.find(item => item.published);
        const chapter = details.legacy_chapters.find(item => item.published);
        if (first) nav.append(link('Start first daily lesson →', url({ kind: 'daily', number: first.chapter }), 'button gold'));
        else if (chapter) nav.append(link('Start first chapter →', url({ kind: 'chapter', number: chapter.chapter }), 'button gold'));
      } else {
        const published = entries(unit.kind).filter(item => item.published);
        const before = published.filter(item => item.chapter < unit.number).at(-1);
        const after = published.find(item => item.chapter > unit.number);
        if (before) nav.append(link(`← Previous ${unit.kind === 'daily' ? 'lesson' : 'chapter'}`, url({ kind: unit.kind, number: before.chapter })));
        nav.append(link('Course overview', url(null)));
        if (after) nav.append(link(`Next ${unit.kind === 'daily' ? 'lesson' : 'chapter'} →`, url({ kind: unit.kind, number: after.chapter })));
        if (unit.kind === 'daily' && !after) {
          const chapter = details.legacy_chapters.find(item => item.published && item.chapter === Math.ceil(unit.number / 5));
          if (chapter) nav.append(link('Read full chapter →', url({ kind: 'chapter', number: chapter.chapter })));
        }
      }
      for (const anchor of nav.querySelectorAll<HTMLAnchorElement>('a')) {
        anchor.addEventListener('click', event => {
          event.preventDefault(); void openUnit(readUnit(new URL(anchor.href).searchParams), true);
        });
      }
    }
  }
  function readUnit(params: URLSearchParams): Unit | null {
    const number = Number(params.get('chapter'));
    if (!Number.isInteger(number) || number < 1) return null;
    const requested = params.get('unit');
    if (requested === 'daily' || requested === 'chapter') return { kind: requested, number };
    if (details.daily_slots.some(item => item.chapter === number && item.published)) return { kind: 'daily', number };
    if (details.legacy_chapters.some(item => item.chapter === number && item.published)) return { kind: 'chapter', number };
    return { kind: details.has_daily_lessons ? 'daily' : 'chapter', number };
  }
  async function showProgress(lesson: LessonData): Promise<void> {
    const tools = el('course-progress'), action = el('course-progress-action'), forms = el('course-exercise-forms');
    tools.hidden = false; action.replaceChildren(); forms.replaceChildren(); el('course-progress-status').textContent = '';
    try {
      const me = await fetch('/private/me', { credentials: 'same-origin', cache: 'no-store', redirect: 'manual' });
      if (!me.ok) throw new Error('Sign-in unavailable');
    } catch { action.append(link('Sign in to save progress →', '/account/')); return; }
    const base = { level, area, language, chapter: lesson.chapter };
    const mark = document.createElement('button'); mark.className = 'button gold'; mark.type = 'button'; mark.textContent = 'Mark lesson complete ✓';
    mark.addEventListener('click', async () => {
      const response = await fetch('/private/progress/lesson', { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ...base, status: 'completed' }) });
      el('course-progress-status').textContent = response.ok ? 'Lesson completed and saved to your account.' : 'Could not save right now.';
    }); action.append(mark);
    for (const digits of lesson.exercise_ids) {
      const exerciseId = `EX${digits}`, form = document.createElement('form'); form.className = 'exercise-form';
      const label = document.createElement('label'); label.textContent = `Your answer for ${exerciseId}`; label.htmlFor = `answer-${exerciseId}`;
      const input = document.createElement('textarea'); input.id = `answer-${exerciseId}`; input.maxLength = 20_000; input.rows = 4; input.placeholder = 'Save your attempt, then compare the worked answer.';
      const save = document.createElement('button'); save.type = 'submit'; save.className = 'button secondary'; save.textContent = 'Save attempt';
      form.append(label, input, save);
      form.addEventListener('submit', async event => {
        event.preventDefault(); save.disabled = true;
        try {
          const response = await fetch('/private/progress/exercise', { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ...base, exercise_id: exerciseId, answer: input.value, status: 'attempted' }) });
          el('course-progress-status').textContent = response.ok ? `${exerciseId} saved to your account.` : `Could not save ${exerciseId}.`;
        } catch { el('course-progress-status').textContent = `Could not save ${exerciseId}.`; }
        finally { save.disabled = false; }
      }); forms.append(form);
    }
  }
  async function openUnit(unit: Unit | null, push = false): Promise<void> {
    const id = ++requestId;
    const item = unit ? entry(unit) : undefined;
    if (unit && !item) unit = null;
    current = unit;
    if (unit) { indexMode = unit.kind; if (unit.kind === 'daily') selectedWeek = Math.ceil(unit.number / 5); }
    const target = url(unit);
    if (location.pathname + location.search !== target) history[push ? 'pushState' : 'replaceState'](null, '', target);
    renderIndex(); renderNavigation(unit);
    el('course-markdown').hidden = true; el('course-answers').hidden = true; el('course-progress').hidden = true;
    el('course-overview').hidden = unit !== null; el('course-lesson-top').hidden = unit === null;
    el('course-reader-title').hidden = false;
    const source = el('course-source'); source.replaceChildren();
    if (push) el('course-reader-title').scrollIntoView({ behavior: 'smooth', block: 'start' });
    if (!unit || !item) {
      el('course-kicker').textContent = `COURSE ${String(courseNumber).padStart(3, '0')}`;
      el('course-reader-title').textContent = root.querySelector('h1')?.textContent || '';
      el('course-intro').textContent = `${details.published_lessons} daily lessons and ${details.published_chapters} chapters are published in this edition.`;
      if (details.book_url) source.append(link('Read the complete book →', bookUrl()));
      renderOverview(); return;
    }
    el('course-position').textContent = unit.kind === 'daily' ? `${weekLabel(Math.ceil(unit.number / 5))} · Day ${(unit.number - 1) % 5 + 1}` : `Chapter ${unit.number} of ${details.legacy_chapters.length}`;
    el('course-kicker').textContent = `${unit.kind === 'daily' ? 'LESSON' : 'CHAPTER'} ${String(unit.number).padStart(2, '0')} · COURSE ${String(courseNumber).padStart(3, '0')}`;
    el('course-reader-title').textContent = item.title;
    if (item.published && item.source_url) source.append(link('Read in the complete book →', bookUrl(new URL(item.source_url).hash)));
    if (!item.published) { el('course-intro').textContent = 'This study slot is planned. Its teaching has not been published yet. Choose a written lesson or chapter from the syllabus.'; return; }
    el('course-intro').textContent = 'Loading the current published text…';
    try {
      const endpoint = unit.kind === 'daily' ? 'lessons' : 'chapters';
      const response = await fetch(`/api/${endpoint}/${level}/${area}/${language}/${unit.number}`, { cache: 'no-store' });
      if (!response.ok) throw new Error('This text is temporarily unavailable.');
      const lesson = await response.json() as LessonData;
      if (id !== requestId) return;
      el('course-intro').textContent = `${lesson.exercise_ids.length} linked exercises · ${lesson.worked_answers ? 'Worked answers available' : 'Worked answer pending'}`;
      await renderMarkdown(el('course-markdown'), lesson.markdown, lesson.source_url, language);
      if (id !== requestId) return;
      el('course-markdown').hidden = false;
      const firstExercise = lesson.exercise_ids[0];
      if (firstExercise && el('course-markdown').querySelector(`#exercise-ex${firstExercise}`)) source.append(link('Jump to exercise ↓', `#exercise-ex${firstExercise}`));
      if (lesson.worked_answers) {
        await renderMarkdown(el('course-answer-markdown'), lesson.worked_answers, lesson.source_url, language);
        el('course-answers').hidden = false;
      }
      if (unit.kind === 'daily' || !details.has_daily_lessons) void showProgress(lesson);
      el('course-status').textContent = `${unit.kind === 'daily' ? 'Lesson' : 'Chapter'} ${unit.number} loaded from the current public book.`;
    } catch (error) { if (id === requestId) el('course-intro').textContent = String(error); }
  }

  el('course-markdown').addEventListener('click', event => {
    const link = (event.target as HTMLElement).closest('a[href^="#answer-ex"]');
    if (link) (el('course-answers').querySelector('details') as HTMLDetailsElement).open = true;
  });
  selector.addEventListener('change', () => {
    try { localStorage.setItem('open-cyber-academy-language', selector.value); } catch { /* private mode */ }
    const target = new URLSearchParams({ lang: selector.value });
    if (firstQuery.has('ui')) target.set('ui', firstQuery.get('ui')!);
    if (current) { target.set('unit', current.kind); target.set('chapter', String(current.number)); }
    location.href = location.pathname + '?' + target;
  });
  for (const anchor of [el('course-overview-link'), el('course-top-overview')] as HTMLAnchorElement[]) {
    anchor.href = url(null);
    anchor.addEventListener('click', event => { event.preventDefault(); void openUnit(null, true); });
  }
  window.addEventListener('popstate', () => { void openUnit(readUnit(new URLSearchParams(location.search))); });
  try {
    const response = await fetch(`/api/courses/${level}/${area}/${language}`, { cache: 'no-store' });
    if (!response.ok) throw new Error('The course guide could not be loaded.');
    details = await response.json() as CourseDetails;
    el('course-status').textContent = 'Current public syllabus loaded.';
    renderFacts();
    await openUnit(readUnit(new URLSearchParams(location.search)));
  } catch (error) {
    el('course-status').textContent = String(error);
    el('course-intro').textContent = 'This course is temporarily unavailable. Please try again shortly.';
  }
}
