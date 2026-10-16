import catalog from '../../public/catalog.json';
import testIndex from '../../public/test-index.json';
import approvals from '../../public/approved-books.json';
import { siteLanguage } from './i18n';

type Chapter = { chapter: number; bank_sha256: string; source_sha256: string };
type Question = { number: number; total: number; id: string; prompt: string; options: { id: string; text: string }[]; deadline_ms: number; server_now_ms: number; seconds: number };
type Review = { id: string; selected: string | null; correct: boolean; timed_out: boolean; answer: string; explanation: string; source: string };
type QuizResponse = { attempt_id: string; question?: Question; complete?: boolean; score?: number; perfect?: boolean; review?: Review; feedback?: Review[] };
type Course = (typeof catalog.courses)[number];

const names: Record<string, string> = { en: 'English', pt: 'Português', es: 'Español', he: 'עברית', fr: 'Français', ru: 'Русский', de: 'Deutsch', zh: '中文', ja: '日本語' };
const activeLanguages = ['en', 'pt', 'es', 'he', 'fr', 'ru', 'de', 'zh', 'ja'];
type PublishedUnit = { chapter: number; title: string; published: boolean };
type PublishedGuide = { daily_slots: PublishedUnit[]; legacy_chapters: PublishedUnit[]; chapter_lessons: boolean };
const copy = {
  en: { choose: 'Select a language, subject and level.', none: 'No reviewed chapter tests have been published for this edition yet.', count: (done: number, total: number) => `${done} of ${total} chapters have published tests.`, read: 'Read chapter', take: 'Take test', open: 'Open assessment', chapter: 'Chapter', best: (score: number) => `Best score: ${score}/10`, question: (n: number) => `Question ${n} of 10`, submit: 'Submit answer →', starting: 'Starting your test…', sending: 'Saving your answer…', signin: 'Sign in to take this test →', setup: 'Student sign-in is being configured. Public reading remains open.', failed: 'The test could not be loaded. Please try again.', result: (score: number) => `${score} / 10 correct`, perfect: 'Perfect score for this chapter. Your result was saved.', retry: 'Review the chapter and try again to reach 10/10.', timed: 'Time expired', selected: 'You chose', correct: 'Correct answer', previous: (correct: boolean) => `Previous question: ${correct ? 'correct' : 'incorrect'}. Full explanations appear after the test.`, certificate: 'View your certificate', pending: 'A course certificate requires 10/10 on every chapter and a fully reviewed book.', practiceNone: 'No authored lessons or exercises are available in this edition yet.', practiceCount: (n: number) => `${n} authored units with book exercises available for practice.`, practiceOpen: 'Open exercises', lesson: 'Lesson' },
  pt: { choose: 'Escolha idioma, tema e nível.', none: 'Ainda não há testes revisados publicados para esta edição.', count: (done: number, total: number) => `${done} de ${total} capítulos têm testes publicados.`, read: 'Ler capítulo', take: 'Fazer teste', open: 'Abrir avaliação', chapter: 'Capítulo', best: (score: number) => `Melhor nota: ${score}/10`, question: (n: number) => `Pergunta ${n} de 10`, submit: 'Enviar resposta →', starting: 'Iniciando seu teste…', sending: 'Salvando sua resposta…', signin: 'Entre para fazer este teste →', setup: 'O cadastro de estudantes está sendo configurado. A leitura pública continua aberta.', failed: 'Não foi possível carregar o teste. Tente novamente.', result: (score: number) => `${score} / 10 corretas`, perfect: 'Aproveitamento integral neste capítulo. Seu resultado foi salvo.', retry: 'Revise o capítulo e tente novamente até obter 10/10.', timed: 'Tempo esgotado', selected: 'Sua escolha', correct: 'Resposta correta', previous: (correct: boolean) => `Pergunta anterior: ${correct ? 'correta' : 'incorreta'}. As explicações completas aparecem ao final do teste.`, certificate: 'Ver seu certificado', pending: 'O certificado do curso exige 10/10 em todos os capítulos e um livro integralmente revisado.', practiceNone: 'Ainda não há aulas e exercícios escritos nesta edição.', practiceCount: (n: number) => `${n} unidades escritas com exercícios do livro para praticar.`, practiceOpen: 'Abrir exercícios', lesson: 'Aula' },
  es: { choose: 'Elige idioma, tema y nivel.', none: 'Todavía no hay pruebas revisadas publicadas para esta edición.', count: (done: number, total: number) => `${done} de ${total} capítulos tienen pruebas publicadas.`, read: 'Leer capítulo', take: 'Hacer prueba', open: 'Abrir evaluación', chapter: 'Capítulo', best: (score: number) => `Mejor nota: ${score}/10`, question: (n: number) => `Pregunta ${n} de 10`, submit: 'Enviar respuesta →', starting: 'Iniciando la prueba…', sending: 'Guardando la respuesta…', signin: 'Inicia sesión para hacer esta prueba →', setup: 'El registro de estudiantes está en preparación. La lectura pública sigue abierta.', failed: 'No se pudo cargar la prueba. Inténtalo de nuevo.', result: (score: number) => `${score} / 10 correctas`, perfect: 'Puntuación perfecta en este capítulo. El resultado se guardó.', retry: 'Repasa el capítulo e inténtalo de nuevo hasta lograr 10/10.', timed: 'Tiempo agotado', selected: 'Tu elección', correct: 'Respuesta correcta', previous: (correct: boolean) => `Pregunta anterior: ${correct ? 'correcta' : 'incorrecta'}. Las explicaciones completas aparecen al terminar la prueba.`, certificate: 'Ver tu certificado', pending: 'El certificado del curso exige 10/10 en todos los capítulos y un libro totalmente revisado.', practiceNone: 'Esta edición todavía no tiene lecciones ni ejercicios redactados.', practiceCount: (n: number) => `${n} unidades redactadas con ejercicios del libro para practicar.`, practiceOpen: 'Abrir ejercicios', lesson: 'Lección' },
};
const practiceFallback = {
  en: { failed: 'The exercise list is temporarily unavailable.', guide: 'Open the course guide →' },
  pt: { failed: 'A lista de exercícios está temporariamente indisponível.', guide: 'Abrir guia do curso →' },
  es: { failed: 'La lista de ejercicios no está disponible en este momento.', guide: 'Abrir guía del curso →' },
};
const readyCopy = {
  en: { note: 'Ten questions, with ten seconds for each answer. The clock starts when you begin. Explanations appear after the last question.', start: 'Start timed test →' },
  pt: { note: 'Dez perguntas, com dez segundos para cada resposta. O cronômetro começa quando você iniciar. As explicações aparecem ao final.', start: 'Iniciar teste cronometrado →' },
  es: { note: 'Diez preguntas, con diez segundos para cada respuesta. El reloj comienza al iniciar. Las explicaciones aparecen al final.', start: 'Iniciar prueba cronometrada →' },
};

const el = (id: string): HTMLElement => document.getElementById(id)!;
const chapterTitle = (title: string, chapter: number): string => {
  const prefix = new RegExp(`^(?:Chapter|Capítulo)\\s+0*${chapter}\\s*[—–-]\\s*`, 'i');
  return title.replace(prefix, '').trim();
};
const button = (label: string, pressed: boolean, onClick: () => void): HTMLButtonElement => {
  const result = document.createElement('button'); result.type = 'button'; result.textContent = label;
  result.setAttribute('aria-pressed', String(pressed)); result.addEventListener('click', onClick); return result;
};
const actionButton = (label: string, onClick: () => void): HTMLButtonElement => {
  const result = document.createElement('button'); result.type = 'button'; result.textContent = label;
  result.addEventListener('click', onClick); return result;
};

export function initChapterTests(): void {
  const ui = copy[siteLanguage()];
  const params = new URLSearchParams(location.search);
  let language = activeLanguages.includes(params.get('lang') || '') ? params.get('lang')! : siteLanguage();
  let area = catalog.courses.some(course => course.area === params.get('area')) ? params.get('area')! : '';
  let level = catalog.level_order.includes(params.get('level') || '') ? params.get('level')! : '';
  let selectedChapter = Number(params.get('chapter')) || 0;
  (el('test-manual-selection') as HTMLDetailsElement).open = !(area && level);
  let active: QuizResponse | null = null;
  let timer: ReturnType<typeof setInterval> | undefined;
  let deadline = 0;
  let busy = false;
  let resultsRequest = 0;
  let practiceRequest = 0;
  let chaptersByCourse = testIndex.courses as Record<string, Chapter[]>;
  const renderPublishedCards = () => {
    const publishedCards: HTMLElement[] = [];
    for (const [key, chapters] of Object.entries(chaptersByCourse)) {
    const [courseLevel, courseArea, courseLanguage] = key.split('/');
    if (!activeLanguages.includes(courseLanguage)) continue;
    const course = catalog.courses.find(item => item.level === courseLevel && item.area === courseArea);
    if (!course) continue;
    if (!chapters.length) continue;
    const card = document.createElement('article'); card.className = 'test-chapter test-course-card';
    const heading = document.createElement('strong');
    heading.textContent = course.titles[courseLanguage as keyof typeof course.titles] || course.title;
    const detail = document.createElement('p'); detail.className = 'muted';
    detail.textContent = `${names[courseLanguage]} · ${catalog.level_names[courseLevel as keyof typeof catalog.level_names][siteLanguage()]}`;
    const coverage = document.createElement('span'); coverage.className = 'test-coverage';
    coverage.textContent = ui.count(chapters.length, course.planned_chapters);
    const link = document.createElement('a');
    const url = new URL('/tests/', location.href);
    if (location.hostname.endsWith('opencyber.academy')) url.hostname = courseLanguage === 'en' ? 'opencyber.academy' : `${courseLanguage}.opencyber.academy`;
    url.search = new URLSearchParams({ lang: courseLanguage, area: courseArea, level: courseLevel }).toString();
    url.hash = 'published-chapters';
    link.href = url.href; link.textContent = `${ui.open} →`;
    card.append(heading, detail, coverage, link); publishedCards.push(card);
    }
    el('test-available').replaceChildren(...publishedCards);
  };
  renderPublishedCards();
  void fetch('/api/tests/catalog', { cache: 'no-store' }).then(async response => {
    if (!response.ok) throw new Error('Catalog unavailable');
    const latest = await response.json() as { courses: Record<string, Chapter[]>; live_sync?: string };
    if (!latest.courses || typeof latest.courses !== 'object') throw new Error('Invalid catalog');
    chaptersByCourse = latest.courses;
    renderPublishedCards();
    if (!active) render();
    el('test-catalog-sync').textContent = latest.live_sync === 'github'
      ? siteLanguage() === 'pt' ? 'Sincronizado com o GitHub atual.' : siteLanguage() === 'es' ? 'Sincronizado con el GitHub actual.' : 'Synced with current GitHub main.'
      : siteLanguage() === 'pt' ? 'Exibindo o catálogo incluído nesta versão do site.' : siteLanguage() === 'es' ? 'Mostrando el catálogo incluido en esta versión del sitio.' : 'Showing the catalog included in this site release.';
  }).catch(() => {
    el('test-catalog-sync').textContent = siteLanguage() === 'pt' ? 'Exibindo o catálogo incluído nesta versão do site.' :
      siteLanguage() === 'es' ? 'Mostrando el catálogo incluido en esta versión del sitio.' : 'Showing the catalog included in this site release.';
  });
  const clearAttempt = () => {
    resultsRequest++;
    if (timer) clearInterval(timer);
    timer = undefined; active = null; selectedChapter = 0;
    el('test-ready').hidden = true; el('test-player').hidden = true; el('test-result').hidden = true;
    (el('test-practice-disclosure') as HTMLDetailsElement).open = false;
  };

  const chosenCourse = (): Course | undefined => catalog.courses.find(course => course.area === area && course.level === level);
  const courseKey = (): string => `${level}/${area}/${language}`;
  const available = (): Chapter[] => chaptersByCourse[courseKey()] || [];
  const updateUrl = () => {
    const next = new URL(location.href);
    for (const [key, value] of [['lang', language], ['area', area], ['level', level], ['chapter', String(selectedChapter)]]) {
      if (value && value !== '0') next.searchParams.set(key, value); else next.searchParams.delete(key);
    }
    history.replaceState(null, '', next);
  };
  const chooseLanguage = (next: string) => {
    clearAttempt(); language = next;
    const targetHost = next === 'en' ? 'opencyber.academy' : `${next}.opencyber.academy`;
    if (location.hostname.endsWith('opencyber.academy') && location.hostname !== targetHost) {
      const url = new URL(location.href); url.hostname = targetHost; url.searchParams.set('lang', next); url.searchParams.delete('chapter'); location.assign(url.href); return;
    }
    render();
  };
  const render = () => {
    updateUrl();
    el('test-languages').replaceChildren(...activeLanguages.map(code => button(names[code], language === code, () => chooseLanguage(code))));
    const subjects = catalog.courses.filter(course => course.level === catalog.level_order[0]);
    el('test-subjects').replaceChildren(...subjects.map(course => button(
      course.titles[siteLanguage()] || course.title, area === course.area, () => { clearAttempt(); area = course.area; render(); }
    )));
    el('test-levels').replaceChildren(...catalog.level_order.map(code => button(
      catalog.level_names[code as keyof typeof catalog.level_names][siteLanguage()], level === code,
      () => { clearAttempt(); level = code; render(); }
    )));
    const status = el('test-course-status'); const list = el('test-chapters'); list.replaceChildren();
    const course = chosenCourse();
    if (!course) { status.textContent = ui.choose; el('test-practice-status').textContent = ui.choose; el('test-practice').replaceChildren(); el('test-practice-fallback').hidden = true; return; }
    const chapters = available();
    status.textContent = chapters.length ? ui.count(chapters.length, course.planned_chapters) : ui.none;
    for (const item of chapters) {
      const card = document.createElement('article'); card.className = 'test-chapter';
      card.dataset.chapter = String(item.chapter);
      const heading = document.createElement('strong'); heading.textContent = `${ui.chapter} ${item.chapter.toString().padStart(2, '0')}`;
      const best = document.createElement('small'); best.className = 'test-best';
      const link = document.createElement('a'); link.href = `/courses/${level}/${area}/chapters/${language}/${item.chapter}/`; link.textContent = ui.read;
      const start = actionButton(ui.take, () => prepareTest(item.chapter));
      card.append(heading, best, link, start); list.append(card);
    }
    void loadResults(courseKey());
    void renderPractice(courseKey());
  };

  const renderPractice = async (key: string) => {
    const requestId = ++practiceRequest;
    const status = el('test-practice-status'); const list = el('test-practice');
    const fallback = el('test-practice-fallback'); fallback.hidden = true; fallback.replaceChildren();
    list.replaceChildren(); status.textContent = '';
    try {
      const response = await fetch(`/api/courses/${level}/${area}/${language}`, { cache: 'no-store' });
      if (!response.ok) throw new Error('The published course guide is unavailable');
      const edition = await response.json() as PublishedGuide;
      if (requestId !== practiceRequest || key !== courseKey()) return;
      const units = edition.chapter_lessons
        ? edition.legacy_chapters.filter(unit => unit.published).map(unit => ({ ...unit, route: 'chapters', label: ui.lesson }))
        : [
          ...edition.daily_slots.filter(unit => unit.published).map(unit => ({ ...unit, route: 'lessons', label: ui.lesson })),
          ...edition.legacy_chapters.filter(unit => unit.published).map(unit => ({ ...unit, route: 'chapters', label: ui.chapter })),
        ];
      for (const chapter of edition.legacy_chapters) {
        if (!chapter.published) continue;
        const heading = el('test-chapters').querySelector<HTMLElement>(`[data-chapter="${chapter.chapter}"] strong`);
        if (heading) heading.textContent = `${ui.chapter} ${String(chapter.chapter).padStart(2, '0')} · ${chapterTitle(chapter.title, chapter.chapter)}`;
      }
      status.textContent = units.length ? ui.practiceCount(units.length) : ui.practiceNone;
      for (const unit of units) {
        const card = document.createElement('article'); card.className = 'test-chapter';
        const title = document.createElement('strong'); title.textContent = `${unit.label} ${String(unit.chapter).padStart(2, '0')} · ${chapterTitle(unit.title, unit.chapter)}`;
        const link = document.createElement('a'); link.href = `/courses/${level}/${area}/${unit.route}/${language}/${unit.chapter}/#lesson-practice`;
        link.textContent = `${ui.practiceOpen} →`;
        card.append(title, link); list.append(card);
      }
    } catch {
      if (requestId !== practiceRequest || key !== courseKey()) return;
      const message = practiceFallback[siteLanguage()];
      status.textContent = message.failed;
      const link = document.createElement('a'); link.href = `/courses/${level}/${area}/?lang=${language}`;
      link.textContent = message.guide; fallback.replaceChildren(link); fallback.hidden = false;
    }
  };

  const loadResults = async (key: string) => {
    const requestId = ++resultsRequest;
    try {
      const me = await fetch('/auth/me', { credentials: 'same-origin', cache: 'no-store', redirect: 'manual' });
      if (!me.ok || !(me.headers.get('content-type') || '').includes('application/json')) return;
      const query = new URLSearchParams({ level, area, language });
      const response = await fetch(`/student/tests/results?${query}`, { credentials: 'same-origin', cache: 'no-store' });
      if (!response.ok) return;
      const rows = (await response.json()).results as { chapter: number; bank_sha256: string; best_score: number }[];
      if (requestId !== resultsRequest || key !== courseKey()) return;
      for (const item of available()) {
        const score = rows.find(row => row.chapter === item.chapter && row.bank_sha256 === item.bank_sha256)?.best_score;
        const label = el('test-chapters').querySelector<HTMLElement>(`[data-chapter="${item.chapter}"] .test-best`);
        if (label && typeof score === 'number') label.textContent = ui.best(score);
      }
    } catch { /* Tests remain browsable while sign-in or progress is unavailable. */ }
  };

  const signInLink = () => {
    const link = document.createElement('a'); link.className = 'button gold';
    link.href = `/account/?next=${encodeURIComponent(location.pathname + location.search)}`;
    link.textContent = ui.signin; return link;
  };
  const post = async (path: string, payload: unknown): Promise<Response> => fetch(path, {
    method: 'POST', credentials: 'same-origin', cache: 'no-store',
    headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(payload),
  });
  const prepareTest = (chapter: number) => {
    if (busy) return;
    if (timer) clearInterval(timer);
    timer = undefined; active = null; selectedChapter = chapter; updateUrl();
    el('test-player').hidden = true; el('test-result').hidden = true;
    const ready = readyCopy[siteLanguage()];
    el('test-ready-heading').textContent = `${ui.chapter} ${String(chapter).padStart(2, '0')} · ${ui.take}`;
    el('test-ready-note').textContent = ready.note;
    el('test-ready-start').textContent = ready.start;
    el('test-ready').hidden = false;
    el('test-ready').scrollIntoView({ behavior: 'auto', block: 'start' });
    el('test-ready-heading').focus({ preventScroll: true });
  };
  const startTest = async (chapter: number) => {
    if (busy) return; busy = true; selectedChapter = chapter; updateUrl();
    const status = el('test-course-status'); status.textContent = ui.starting;
    try {
      const me = await fetch('/auth/me', { credentials: 'same-origin', cache: 'no-store', redirect: 'manual' });
      if (!me.ok || !(me.headers.get('content-type') || '').includes('application/json')) {
        if (me.status === 503) status.textContent = ui.setup;
        else status.replaceChildren(signInLink());
        return;
      }
      const response = await post('/student/tests/start', { level, area, language, chapter });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || ui.failed);
      active = data as QuizResponse;
      el('test-ready').hidden = true; el('test-result').hidden = true; el('test-player').hidden = false;
      el('test-live-feedback').hidden = true;
      el('test-player').scrollIntoView({ behavior: 'auto', block: 'start' });
      showQuestion(active.question!);
      status.textContent = ui.count(available().length, chosenCourse()!.planned_chapters);
    } catch (error) { status.textContent = error instanceof Error ? error.message : ui.failed; }
    finally { busy = false; }
  };
  const showQuestion = (question: Question) => {
    el('test-question-number').textContent = ui.question(question.number);
    (el('test-progress') as HTMLProgressElement).value = question.number;
    el('test-live-feedback').textContent = '';
    el('test-live-feedback').hidden = true;
    el('test-prompt').textContent = question.prompt;
    const options = el('test-options'); options.replaceChildren();
    for (const option of question.options) {
      const label = document.createElement('label'); label.className = 'test-option';
      const radio = document.createElement('input'); radio.type = 'radio'; radio.name = 'test-option'; radio.value = option.id;
      const text = document.createElement('span'); text.textContent = `${option.id.toUpperCase()}. ${option.text}`;
      label.append(radio, text); options.append(label);
    }
    (el('test-submit') as HTMLButtonElement).disabled = false; el('test-submit').textContent = ui.submit;
    el('test-feedback-status').textContent = '';
    el('test-question-number').focus({ preventScroll: true });
    if (timer) clearInterval(timer);
    deadline = performance.now() + Math.min(10_000, question.deadline_ms - question.server_now_ms - 250);
    const tick = () => {
      const remaining = Math.max(0, deadline - performance.now()); const clock = el('test-timer');
      clock.textContent = String(Math.ceil(remaining / 1000)); clock.classList.toggle('low', remaining <= 3000);
      if (remaining <= 0) { if (timer) clearInterval(timer); timer = undefined; void submitAnswer(null); }
    };
    tick(); timer = setInterval(tick, 100);
  };
  const submitAnswer = async (selected: string | null) => {
    if (busy || !active?.question) return; busy = true;
    if (timer) clearInterval(timer); timer = undefined;
    (el('test-submit') as HTMLButtonElement).disabled = true; el('test-feedback-status').textContent = ui.sending;
    try {
      const response = await post('/student/tests/answer', { attempt_id: active.attempt_id, index: active.question.number - 1, selected });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || ui.failed);
      active = data as QuizResponse;
      if (active.question) {
        showQuestion(active.question);
        if (active.review) {
          const notice = el('test-live-feedback');
          notice.textContent = ui.previous(active.review.correct);
          notice.hidden = false;
        }
      }
      else if (active.complete) showResult(active);
    } catch (error) {
      try {
        const state = await fetch(`/student/tests/state?attempt_id=${encodeURIComponent(active.attempt_id)}`, { credentials: 'same-origin', cache: 'no-store' });
        if (!state.ok) throw error;
        active = await state.json() as QuizResponse;
        if (active.question) showQuestion(active.question);
        else if (active.complete) showResult(active);
      } catch {
        el('test-feedback-status').textContent = error instanceof Error ? error.message : ui.failed;
        (el('test-submit') as HTMLButtonElement).disabled = false;
      }
    }
    finally { busy = false; }
  };
  const showResult = (result: QuizResponse) => {
    el('test-player').hidden = true; el('test-result').hidden = false;
    el('test-score').textContent = ui.result(result.score || 0);
    el('test-result-note').textContent = result.perfect ? ui.perfect : ui.retry;
    const reviewLink = el('test-review-chapter') as HTMLAnchorElement;
    reviewLink.href = `/courses/${level}/${area}/chapters/${language}/${selectedChapter}/`;
    reviewLink.textContent = `${ui.read} →`;
    void loadResults(courseKey());
    const explanations = el('test-explanations'); explanations.replaceChildren();
    for (const item of result.feedback || []) {
      const row = document.createElement('div'); row.className = 'test-explanation';
      const heading = document.createElement('strong'); heading.textContent = `${item.id} · ${item.correct ? '✓' : '×'}${item.timed_out ? ` · ${ui.timed}` : ''}`;
      const answer = document.createElement('p'); answer.textContent = `${ui.selected}: ${item.selected?.toUpperCase() || '—'} · ${ui.correct}: ${item.answer.toUpperCase()}`;
      const reason = document.createElement('p'); reason.textContent = item.explanation;
      const source = document.createElement('small'); source.textContent = item.source;
      row.append(heading, answer, reason, source); explanations.append(row);
    }
    const course = chosenCourse(); const certificate = el('test-certificate') as HTMLButtonElement;
    const approved = (approvals.books as { level: string; area: string; language: string }[]).some(item => item.level === level && item.area === area && item.language === language);
    certificate.hidden = !(approved && course && available().length === course.planned_chapters);
    el('test-certificate-status').textContent = certificate.hidden ? ui.pending : '';
    el('test-result').scrollIntoView({ behavior: 'auto', block: 'start' });
    el('test-score').focus({ preventScroll: true });
  };
  el('test-answer-form').addEventListener('submit', event => {
    event.preventDefault();
    const selected = (document.querySelector<HTMLInputElement>('input[name="test-option"]:checked'))?.value || null;
    void submitAnswer(selected);
  });
  el('test-ready-start').addEventListener('click', () => { if (selectedChapter) void startTest(selectedChapter); });
  el('test-retry').addEventListener('click', () => { if (selectedChapter) prepareTest(selectedChapter); });
  el('test-certificate').addEventListener('click', async () => {
    const status = el('test-certificate-status'); status.textContent = ui.sending;
    try {
      const response = await post('/student/tests/certificate', { level, area, language });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || ui.failed);
      const link = document.createElement('a'); link.href = data.certificate_url; link.textContent = `${ui.certificate} →`;
      status.replaceChildren(link);
    } catch (error) { status.textContent = error instanceof Error ? error.message : ui.failed; }
  });
  render();
  if (location.hash === '#published-chapters' && area && level) {
    requestAnimationFrame(() => el('published-chapters').scrollIntoView({ block: 'start' }));
  }
}
