import catalog from '../../public/catalog.json';
import testIndex from '../../public/test-index.json';
import approvals from '../../public/approved-books.json';
import { siteLanguage } from './i18n';

type Chapter = { chapter: number; bank_sha256: string; source_sha256: string };
type Question = { number: number; total: number; id: string; prompt: string; options: { id: string; text: string }[]; deadline_ms: number; server_now_ms: number; seconds: number };
type QuizResponse = { attempt_id: string; question?: Question; complete?: boolean; score?: number; perfect?: boolean; feedback?: { id: string; selected: string | null; correct: boolean; timed_out: boolean; answer: string; explanation: string; source: string }[] };
type Course = (typeof catalog.courses)[number];

const names: Record<string, string> = { en: 'English', pt: 'Português', es: 'Español', he: 'עברית', fr: 'Français', ru: 'Русский', de: 'Deutsch', zh: '中文', ja: '日本語' };
const copy = {
  en: { choose: 'Select a language, subject and level.', none: 'No reviewed chapter tests have been published for this edition yet.', count: (done: number, total: number) => `${done} of ${total} chapters have published tests.`, read: 'Read chapter', take: 'Take test', best: (score: number) => `Best score: ${score}/10`, question: (n: number) => `Question ${n} of 10`, submit: 'Submit answer →', sending: 'Saving your answer…', signin: 'Sign in to take this test →', setup: 'Student sign-in is being configured. Public reading remains open.', failed: 'The test could not be loaded. Please try again.', result: (score: number) => `${score} / 10 correct`, perfect: 'Perfect score for this chapter. Your result was saved.', retry: 'Review the chapter and try again to reach 10/10.', timed: 'Time expired', selected: 'You chose', correct: 'Correct answer', certificate: 'View your certificate', pending: 'A course certificate requires 10/10 on every chapter and a fully reviewed book.' },
  pt: { choose: 'Escolha idioma, tema e nível.', none: 'Ainda não há testes revisados publicados para esta edição.', count: (done: number, total: number) => `${done} de ${total} capítulos têm testes publicados.`, read: 'Ler capítulo', take: 'Fazer teste', best: (score: number) => `Melhor nota: ${score}/10`, question: (n: number) => `Pergunta ${n} de 10`, submit: 'Enviar resposta →', sending: 'Salvando sua resposta…', signin: 'Entre para fazer este teste →', setup: 'O cadastro de estudantes está sendo configurado. A leitura pública continua aberta.', failed: 'Não foi possível carregar o teste. Tente novamente.', result: (score: number) => `${score} / 10 corretas`, perfect: 'Aproveitamento integral neste capítulo. Seu resultado foi salvo.', retry: 'Revise o capítulo e tente novamente até obter 10/10.', timed: 'Tempo esgotado', selected: 'Sua escolha', correct: 'Resposta correta', certificate: 'Ver seu certificado', pending: 'O certificado do curso exige 10/10 em todos os capítulos e um livro integralmente revisado.' },
  es: { choose: 'Elige idioma, tema y nivel.', none: 'Todavía no hay pruebas revisadas publicadas para esta edición.', count: (done: number, total: number) => `${done} de ${total} capítulos tienen pruebas publicadas.`, read: 'Leer capítulo', take: 'Hacer prueba', best: (score: number) => `Mejor nota: ${score}/10`, question: (n: number) => `Pregunta ${n} de 10`, submit: 'Enviar respuesta →', sending: 'Guardando la respuesta…', signin: 'Inicia sesión para hacer esta prueba →', setup: 'El registro de estudiantes está en preparación. La lectura pública sigue abierta.', failed: 'No se pudo cargar la prueba. Inténtalo de nuevo.', result: (score: number) => `${score} / 10 correctas`, perfect: 'Puntuación perfecta en este capítulo. El resultado se guardó.', retry: 'Repasa el capítulo e inténtalo de nuevo hasta lograr 10/10.', timed: 'Tiempo agotado', selected: 'Tu elección', correct: 'Respuesta correcta', certificate: 'Ver tu certificado', pending: 'El certificado del curso exige 10/10 en todos los capítulos y un libro totalmente revisado.' },
};

const el = (id: string): HTMLElement => document.getElementById(id)!;
const button = (label: string, pressed: boolean, onClick: () => void): HTMLButtonElement => {
  const result = document.createElement('button'); result.type = 'button'; result.textContent = label;
  result.setAttribute('aria-pressed', String(pressed)); result.addEventListener('click', onClick); return result;
};

export function initChapterTests(): void {
  const ui = copy[siteLanguage()];
  const params = new URLSearchParams(location.search);
  let language = catalog.languages.includes(params.get('lang') || '') ? params.get('lang')! : siteLanguage();
  let area = catalog.courses.some(course => course.area === params.get('area')) ? params.get('area')! : '';
  let level = catalog.level_order.includes(params.get('level') || '') ? params.get('level')! : '';
  let selectedChapter = Number(params.get('chapter')) || 0;
  let active: QuizResponse | null = null;
  let timer: ReturnType<typeof setInterval> | undefined;
  let deadline = 0;
  let busy = false;
  let resultsRequest = 0;
  const chaptersByCourse = testIndex.courses as Record<string, Chapter[]>;
  const clearAttempt = () => {
    resultsRequest++;
    if (timer) clearInterval(timer);
    timer = undefined; active = null; selectedChapter = 0;
    el('test-player').hidden = true; el('test-result').hidden = true;
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
    el('test-languages').replaceChildren(...catalog.languages.map(code => button(names[code], language === code, () => chooseLanguage(code))));
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
    if (!course) { status.textContent = ui.choose; return; }
    const chapters = available();
    status.textContent = chapters.length ? ui.count(chapters.length, course.planned_chapters) : ui.none;
    for (const item of chapters) {
      const card = document.createElement('article'); card.className = 'test-chapter';
      card.dataset.chapter = String(item.chapter);
      const heading = document.createElement('strong'); heading.textContent = `${course.title} · ${item.chapter.toString().padStart(2, '0')}`;
      const best = document.createElement('small'); best.className = 'test-best';
      const link = document.createElement('a'); link.href = `/courses/${level}/${area}/chapters/${language}/${item.chapter}/`; link.textContent = ui.read;
      const start = button(ui.take, false, () => { void startTest(item.chapter); });
      card.append(heading, best, link, start); list.append(card);
    }
    void loadResults(courseKey());
  };

  const loadResults = async (key: string) => {
    const requestId = ++resultsRequest;
    try {
      const me = await fetch('/private/me', { credentials: 'same-origin', cache: 'no-store', redirect: 'manual' });
      if (!me.ok || !(me.headers.get('content-type') || '').includes('application/json')) return;
      const query = new URLSearchParams({ level, area, language });
      const response = await fetch(`/private/tests/results?${query}`, { credentials: 'same-origin', cache: 'no-store' });
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
    link.href = `/private/login?next=${encodeURIComponent(location.pathname + location.search)}`;
    link.textContent = ui.signin; return link;
  };
  const post = async (path: string, payload: unknown): Promise<Response> => fetch(path, {
    method: 'POST', credentials: 'same-origin', cache: 'no-store',
    headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(payload),
  });
  const startTest = async (chapter: number) => {
    if (busy) return; busy = true; selectedChapter = chapter; updateUrl();
    const status = el('test-course-status'); status.textContent = ui.sending;
    try {
      const me = await fetch('/private/me', { credentials: 'same-origin', cache: 'no-store', redirect: 'manual' });
      if (!me.ok || !(me.headers.get('content-type') || '').includes('application/json')) {
        if (me.status === 503) status.textContent = ui.setup;
        else status.replaceChildren(signInLink());
        return;
      }
      const response = await post('/private/tests/start', { level, area, language, chapter });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || ui.failed);
      active = data as QuizResponse;
      el('test-result').hidden = true; el('test-player').hidden = false;
      showQuestion(active.question!); el('test-player').scrollIntoView({ behavior: 'smooth', block: 'start' });
      status.textContent = ui.count(available().length, chosenCourse()!.planned_chapters);
    } catch (error) { status.textContent = error instanceof Error ? error.message : ui.failed; }
    finally { busy = false; }
  };
  const showQuestion = (question: Question) => {
    el('test-question-number').textContent = ui.question(question.number);
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
      const response = await post('/private/tests/answer', { attempt_id: active.attempt_id, index: active.question.number - 1, selected });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || ui.failed);
      active = data as QuizResponse;
      if (active.question) showQuestion(active.question);
      else if (active.complete) showResult(active);
    } catch (error) {
      try {
        const state = await fetch(`/private/tests/state?attempt_id=${encodeURIComponent(active.attempt_id)}`, { credentials: 'same-origin', cache: 'no-store' });
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
    el('test-result').scrollIntoView({ behavior: 'smooth', block: 'start' });
  };
  el('test-answer-form').addEventListener('submit', event => {
    event.preventDefault();
    const selected = (document.querySelector<HTMLInputElement>('input[name="test-option"]:checked'))?.value || null;
    void submitAnswer(selected);
  });
  el('test-retry').addEventListener('click', () => { if (selectedChapter) void startTest(selectedChapter); });
  el('test-certificate').addEventListener('click', async () => {
    const status = el('test-certificate-status'); status.textContent = ui.sending;
    try {
      const response = await post('/private/tests/certificate', { level, area, language });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || ui.failed);
      const link = document.createElement('a'); link.href = data.certificate_url; link.textContent = `${ui.certificate} →`;
      status.replaceChildren(link);
    } catch (error) { status.textContent = error instanceof Error ? error.message : ui.failed; }
  });
  render();
}
