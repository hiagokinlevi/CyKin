import { siteLanguage } from './i18n';

export type Lesson = { level: string; area: string; language: string; chapter: number; status: string; updated_at: string };
export type Exercise = Lesson & { exercise_id: string; answer: string };
export type CoursePerformance = { level: string; area: string; language: string; lesson_visits: number; read_seconds: number;
  lessons_completed: number; exercises_saved: number; analyses_saved: number; chapters_tested: number;
  best_correct: number; best_possible: number };
type Activity = { kind: string; level: string; area: string; language: string; chapter: number;
  exercise_id: string | null; seconds: number; score: number | null; occurred_at: string };
type Summary = { activity: Record<string, { events: number; seconds: number }>; lessons_marked: number;
  lessons_completed: number; exercises_saved: number; tests_completed: number; test_answers_correct: number;
  analyses_saved: number };
export type StudentReport = { summary: Summary; courses: CoursePerformance[]; recent: Activity[] };
export type StudentProgress = { lessons: Lesson[]; exercises: Exercise[] };
type CatalogCourse = { level: string; area: string; title: string; titles: Record<string, string> };

export const dashboardCopy = {
  en: {
    dashboardTitle: 'Your study dashboard', recentTitle: 'Recent activity', savedLessonsTitle: 'Latest lessons',
    savedExercisesTitle: 'Exercise answers', exercisePrivacy: 'Your saved answers are private. Open a course for its details.',
    courseEyebrow: 'COURSE DETAIL', courseHint: 'Open a course to see lessons, exercises and test results.',
    connectAiEyebrow: 'PRIVATE MCP ACCESS', connectAi: 'Connect your AI',
    connectAiIntro: 'Create a personal key to let your AI study with your account, save answers and track progress. Public reading stays open without a key.',
    keySafety: "Keep the key in your AI client's private credential field. It is shown only once. Revoke it here at any time.",
    aiGuide: 'How the MCP connection works →', keyName: 'Key name', createKey: 'Create key',
    keyPlaceholder: 'My AI on my computer', keyLimit: 'You can have five active keys. Revoke one to create another.',
    jumpNav: 'Dashboard sections', metricsLabel: 'Study totals',
    keyOnce: 'Copy this key now. It will not be shown again.', copyKey: 'Copy key', dismissKey: 'Done', yourKeys: 'Your keys',
    keyCopied: 'Key copied. Store it only in your AI client.', keyCreated: 'Key created. Copy it before closing this page.',
    keyRevoked: 'Key revoked.', revokeKey: 'Revoke', keyError: 'Could not manage keys right now. Try again.',
    noKeys: 'No personal AI keys yet.', keyExpired: 'Expired', keyRevokedLabel: 'Revoked', keyActive: 'Active',
    keyUses: 'uses', keyLastUsed: 'Last used', keyExpires: 'Expires',
    overview: (courses: number, lessons: number, exercises: number) => `${courses} courses studied · ${lessons} lessons completed · ${exercises} saved exercise answers.`,
    noActivity: 'No study activity yet. Open a published lesson to begin.', noLessons: 'No saved lessons yet.',
    noExercises: 'No exercise answers saved yet.', noTests: 'No completed chapter tests for this course.',
    loadingTests: 'Loading chapter-test results…', testError: 'Could not load test results.',
    older: 'Show more', lesson: 'Lesson', completed: 'Completed', inProgress: 'In progress',
    readingVisit: 'Opened a lesson', readingTime: 'Read a lesson', finishedLesson: 'Completed a lesson',
    answeredExercise: 'Answered an exercise', startedTest: 'Started a chapter test',
    answeredTest: 'Answered a test question', savedAnalysis: 'Saved an analysis',
    courseLessons: 'Saved lessons', courseExercises: 'Saved exercises', courseTests: 'Chapter-test results',
    metricVisits: 'Lesson visits', metricMinutes: 'Reading minutes', metricCompleted: 'Lessons completed',
    metricAnswers: 'Exercise submissions', metricTests: 'Tests completed', metricCorrect: 'Correct test answers',
    metricAnalyses: 'Saved analyses', metricSaved: 'Distinct exercises saved',
    bestScore: 'Best score', visits: 'visits', minutes: 'reading minutes', exercises: 'exercises', tests: 'tests',
  },
  pt: {
    dashboardTitle: 'Seu painel de estudos', recentTitle: 'Atividade recente', savedLessonsTitle: 'Últimas aulas',
    savedExercisesTitle: 'Respostas de exercícios', exercisePrivacy: 'Suas respostas salvas são privadas. Abra um curso para ver os detalhes.',
    courseEyebrow: 'DETALHES DO CURSO', courseHint: 'Abra um curso para ver aulas, exercícios e resultados dos testes.',
    connectAiEyebrow: 'ACESSO MCP PRIVADO', connectAi: 'Conecte sua IA',
    connectAiIntro: 'Crie uma chave pessoal para sua IA estudar com sua conta, salvar respostas e acompanhar o progresso. A leitura pública continua aberta sem chave.',
    keySafety: 'Guarde a chave no campo privado de credenciais do cliente de IA. Ela aparece uma única vez. Você pode revogá-la aqui.',
    aiGuide: 'Como funciona a conexão MCP →', keyName: 'Nome da chave', createKey: 'Criar chave',
    keyPlaceholder: 'Minha IA no computador', keyLimit: 'Você pode ter cinco chaves ativas. Revogue uma para criar outra.',
    jumpNav: 'Seções do painel', metricsLabel: 'Totais de estudo',
    keyOnce: 'Copie esta chave agora. Ela não será exibida novamente.', copyKey: 'Copiar chave', dismissKey: 'Concluído', yourKeys: 'Suas chaves',
    keyCopied: 'Chave copiada. Guarde-a apenas no cliente de IA.', keyCreated: 'Chave criada. Copie-a antes de fechar a página.',
    keyRevoked: 'Chave revogada.', revokeKey: 'Revogar', keyError: 'Não foi possível gerenciar as chaves agora. Tente novamente.',
    noKeys: 'Nenhuma chave pessoal de IA ainda.', keyExpired: 'Expirada', keyRevokedLabel: 'Revogada', keyActive: 'Ativa',
    keyUses: 'usos', keyLastUsed: 'Último uso', keyExpires: 'Expira em',
    overview: (courses: number, lessons: number, exercises: number) => `${courses} cursos estudados · ${lessons} aulas concluídas · ${exercises} respostas distintas salvas.`,
    noActivity: 'Nenhuma atividade ainda. Abra uma aula publicada para começar.', noLessons: 'Nenhuma aula salva ainda.',
    noExercises: 'Nenhuma resposta de exercício salva ainda.', noTests: 'Nenhum teste concluído neste curso.',
    loadingTests: 'Carregando resultados dos testes…', testError: 'Não foi possível carregar os resultados.',
    older: 'Mostrar mais', lesson: 'Aula', completed: 'Concluída', inProgress: 'Em andamento',
    readingVisit: 'Abriu uma aula', readingTime: 'Leu uma aula', finishedLesson: 'Concluiu uma aula',
    answeredExercise: 'Respondeu um exercício', startedTest: 'Iniciou um teste',
    answeredTest: 'Respondeu uma questão', savedAnalysis: 'Salvou uma análise',
    courseLessons: 'Aulas salvas', courseExercises: 'Exercícios salvos', courseTests: 'Resultados dos testes',
    metricVisits: 'Visitas a aulas', metricMinutes: 'Minutos de leitura', metricCompleted: 'Aulas concluídas',
    metricAnswers: 'Respostas enviadas', metricTests: 'Testes concluídos', metricCorrect: 'Acertos nos testes',
    metricAnalyses: 'Análises salvas', metricSaved: 'Exercícios distintos salvos',
    bestScore: 'Melhor nota', visits: 'visitas', minutes: 'minutos de leitura', exercises: 'exercícios', tests: 'testes',
  },
  es: {
    dashboardTitle: 'Tu panel de estudios', recentTitle: 'Actividad reciente', savedLessonsTitle: 'Últimas lecciones',
    savedExercisesTitle: 'Respuestas de ejercicios', exercisePrivacy: 'Tus respuestas guardadas son privadas. Abre un curso para ver los detalles.',
    courseEyebrow: 'DETALLE DEL CURSO', courseHint: 'Abre un curso para ver lecciones, ejercicios y resultados de pruebas.',
    connectAiEyebrow: 'ACCESO MCP PRIVADO', connectAi: 'Conecta tu IA',
    connectAiIntro: 'Crea una clave personal para que tu IA estudie con tu cuenta, guarde respuestas y siga tu progreso. La lectura pública sigue abierta sin clave.',
    keySafety: 'Guarda la clave en el campo privado de credenciales de tu cliente de IA. Se muestra una sola vez. Puedes revocarla aquí.',
    aiGuide: 'Cómo funciona la conexión MCP →', keyName: 'Nombre de la clave', createKey: 'Crear clave',
    keyPlaceholder: 'Mi IA en el ordenador', keyLimit: 'Puedes tener cinco claves activas. Revoca una para crear otra.',
    jumpNav: 'Secciones del panel', metricsLabel: 'Totales de estudio',
    keyOnce: 'Copia esta clave ahora. No volverá a mostrarse.', copyKey: 'Copiar clave', dismissKey: 'Listo', yourKeys: 'Tus claves',
    keyCopied: 'Clave copiada. Guárdala solo en tu cliente de IA.', keyCreated: 'Clave creada. Cópiala antes de cerrar la página.',
    keyRevoked: 'Clave revocada.', revokeKey: 'Revocar', keyError: 'No se pueden gestionar las claves ahora. Inténtalo de nuevo.',
    noKeys: 'Todavía no tienes claves personales de IA.', keyExpired: 'Caducada', keyRevokedLabel: 'Revocada', keyActive: 'Activa',
    keyUses: 'usos', keyLastUsed: 'Último uso', keyExpires: 'Caduca el',
    overview: (courses: number, lessons: number, exercises: number) => `${courses} cursos estudiados · ${lessons} lecciones completadas · ${exercises} respuestas distintas guardadas.`,
    noActivity: 'Todavía no hay actividad. Abre una lección publicada para empezar.', noLessons: 'Todavía no hay lecciones guardadas.',
    noExercises: 'Todavía no hay respuestas de ejercicios guardadas.', noTests: 'No hay pruebas completadas en este curso.',
    loadingTests: 'Cargando resultados de las pruebas…', testError: 'No se pueden cargar los resultados.',
    older: 'Mostrar más', lesson: 'Lección', completed: 'Completada', inProgress: 'En curso',
    readingVisit: 'Abrió una lección', readingTime: 'Leyó una lección', finishedLesson: 'Completó una lección',
    answeredExercise: 'Respondió un ejercicio', startedTest: 'Empezó una prueba',
    answeredTest: 'Respondió una pregunta', savedAnalysis: 'Guardó un análisis',
    courseLessons: 'Lecciones guardadas', courseExercises: 'Ejercicios guardados', courseTests: 'Resultados de pruebas',
    metricVisits: 'Visitas a lecciones', metricMinutes: 'Minutos de lectura', metricCompleted: 'Lecciones completadas',
    metricAnswers: 'Respuestas enviadas', metricTests: 'Pruebas completadas', metricCorrect: 'Aciertos en pruebas',
    metricAnalyses: 'Análisis guardados', metricSaved: 'Ejercicios distintos guardados',
    bestScore: 'Mejor puntuación', visits: 'visitas', minutes: 'minutos de lectura', exercises: 'ejercicios', tests: 'pruebas',
  },
};

type Copy = typeof dashboardCopy.en;
const locale = { en: 'en-US', pt: 'pt-BR', es: 'es-ES' };

function dateLabel(value: string | number | null | undefined, language: 'en' | 'pt' | 'es'): string {
  if (!value) return '—';
  const date = typeof value === 'number' ? new Date(value * 1000) : new Date(value.replace(' ', 'T') + (value.includes('Z') ? '' : 'Z'));
  return Number.isNaN(date.getTime()) ? String(value) : new Intl.DateTimeFormat(locale[language], { dateStyle: 'medium', timeStyle: 'short' }).format(date);
}

function courseUrl(level: string, area: string, language: string, chapter?: number): string {
  const base = `/courses/${encodeURIComponent(level)}/${encodeURIComponent(area)}/`;
  return chapter ? `${base}lessons/${encodeURIComponent(language)}/${chapter}/` : `${base}?lang=${encodeURIComponent(language)}`;
}

function record(href: string, heading: string, detail: string): HTMLAnchorElement {
  const anchor = document.createElement('a'); anchor.className = 'record'; anchor.href = href;
  const title = document.createElement('strong'); title.textContent = heading;
  const caption = document.createElement('span'); caption.textContent = detail;
  anchor.append(title, caption);
  return anchor;
}

function appendLimited(container: HTMLElement, items: HTMLElement[], empty: string, more: string, limit = 8): void {
  container.replaceChildren(...items.slice(0, limit));
  if (!items.length) { const note = document.createElement('p'); note.className = 'empty-note'; note.textContent = empty; container.append(note); }
  if (items.length > limit) {
    const disclosure = document.createElement('details');
    const summary = document.createElement('summary'); summary.textContent = `${more} (${items.length - limit})`;
    const rest = document.createElement('div'); rest.className = 'dashboard-list'; rest.append(...items.slice(limit));
    disclosure.append(summary, rest); container.append(disclosure);
  }
}

function activityLabel(item: Activity, t: Copy): string {
  const labels: Record<string, string> = {
    lesson_opened: t.readingVisit, lesson_read: t.readingTime, lesson_completed: t.finishedLesson,
    exercise_answered: t.answeredExercise, test_started: t.startedTest, test_answered: t.answeredTest,
    analysis_saved: t.savedAnalysis,
  };
  return `${labels[item.kind] || item.kind}${item.exercise_id ? ` · ${item.exercise_id}` : ''}`;
}

export async function renderStudentDashboard(progress: StudentProgress, report: StudentReport): Promise<void> {
  const language = siteLanguage();
  const t = dashboardCopy[language];
  const summary = report.summary;
  const event = (kind: string) => Number(summary.activity[kind]?.events || 0);
  const minutes = Math.floor(Number(summary.activity.lesson_read?.seconds || 0) / 60);
  document.getElementById('records-status')!.textContent = report.courses.length || summary.lessons_marked
    ? t.overview(report.courses.length, Number(summary.lessons_completed), Number(summary.exercises_saved)) : t.noActivity;

  const metrics: [string, number | string, string, string][] = [
    [t.metricVisits, event('lesson_opened'), '#account-recent', t.visits],
    [t.metricMinutes, minutes, '#account-recent', t.minutes],
    [t.metricCompleted, Number(summary.lessons_completed), '#account-lessons', t.lesson],
    [t.metricAnswers, event('exercise_answered'), '#account-exercises', `${summary.exercises_saved} ${t.metricSaved.toLowerCase()}`],
    [t.metricTests, Number(summary.tests_completed), '#account-course-section', t.tests],
    [t.metricCorrect, `${summary.test_answers_correct}/${Number(summary.tests_completed) * 10}`, '#account-course-section', t.bestScore],
    [t.metricAnalyses, Number(summary.analyses_saved), '#account-course-section', t.metricAnalyses],
  ];
  const tiles = document.getElementById('account-metrics')!; tiles.replaceChildren();
  for (const [label, value, href, detail] of metrics) {
    const link = document.createElement('a'); link.className = 'metric'; link.href = href;
    const number = document.createElement('span'); number.className = 'metric-value'; number.textContent = String(value);
    const name = document.createElement('span'); name.className = 'metric-label'; name.textContent = label;
    const caption = document.createElement('span'); caption.className = 'metric-detail'; caption.textContent = detail;
    link.append(number, name, caption); tiles.append(link);
  }

  const catalogTitles = new Map<string, string>();
  try {
    const response = await fetch('/api/catalog', { cache: 'no-store' });
    if (response.ok) {
      const catalog = await response.json() as { courses: CatalogCourse[] };
      for (const course of catalog.courses) catalogTitles.set(`${course.level}/${course.area}`, course.titles?.[language] || course.title);
    }
  } catch { /* Slugs remain usable when the public catalog is unavailable. */ }
  const titleFor = (level: string, area: string) => catalogTitles.get(`${level}/${area}`) || area.replaceAll('-', ' ');
  const latest = document.getElementById('records-list')!;
  const lessonItems = progress.lessons.map(item => record(
    courseUrl(item.level, item.area, item.language, item.chapter),
    `${titleFor(item.level, item.area)} · ${t.lesson} ${item.chapter}`,
    `${item.language.toUpperCase()} · ${item.status === 'completed' ? t.completed : t.inProgress} · ${dateLabel(item.updated_at, language)}`));
  appendLimited(latest, lessonItems, t.noLessons, t.older);

  const exerciseItems = progress.exercises.map(item => record(
    courseUrl(item.level, item.area, item.language, item.chapter),
    `${item.exercise_id} · ${titleFor(item.level, item.area)}`,
    `${t.lesson} ${item.chapter} · ${item.language.toUpperCase()} · ${dateLabel(item.updated_at, language)}`));
  appendLimited(document.getElementById('account-exercise-list')!, exerciseItems, t.noExercises, t.older);

  const recentItems = report.recent.map(item => record(
    courseUrl(item.level, item.area, item.language, item.chapter),
    activityLabel(item, t),
    `${titleFor(item.level, item.area)} · ${t.lesson} ${item.chapter} · ${dateLabel(item.occurred_at, language)}`));
  appendLimited(document.getElementById('account-recent-list')!, recentItems, t.noActivity, t.older);

  const courses = document.getElementById('account-courses')!; courses.replaceChildren();
  for (const item of report.courses) {
    const disclosure = document.createElement('details'); disclosure.className = 'course-detail';
    const heading = document.createElement('summary');
    const name = document.createElement('strong'); name.textContent = `${titleFor(item.level, item.area)} · ${item.language.toUpperCase()}`;
    const facts = document.createElement('span'); facts.className = 'muted';
    facts.textContent = `${item.lessons_completed} ${t.courseLessons.toLowerCase()} · ${item.exercises_saved} ${t.exercises} · ${item.chapters_tested} ${t.tests}${item.chapters_tested ? ` · ${t.bestScore} ${item.best_correct}/${item.best_possible}` : ''} · ${Math.floor(item.read_seconds / 60)} ${t.minutes}`;
    heading.append(name, facts);
    const body = document.createElement('div'); body.className = 'course-detail-body';
    const scoped = (title: string, elements: HTMLElement[], empty: string) => {
      const section = document.createElement('section'); const h3 = document.createElement('h3'); h3.textContent = title;
      const content = document.createElement('div'); content.className = 'dashboard-list';
      appendLimited(content, elements, empty, t.older, 5); section.append(h3, content); return section;
    };
    const matches = (row: Lesson | Exercise) => row.level === item.level && row.area === item.area && row.language === item.language;
    const lessons = progress.lessons.filter(matches).map(row => record(courseUrl(row.level, row.area, row.language, row.chapter),
      `${t.lesson} ${row.chapter}`, `${row.status === 'completed' ? t.completed : t.inProgress} · ${dateLabel(row.updated_at, language)}`));
    const exercises = progress.exercises.filter(matches).map(row => record(courseUrl(row.level, row.area, row.language, row.chapter),
      row.exercise_id, `${t.lesson} ${row.chapter} · ${dateLabel(row.updated_at, language)}`));
    const tests = document.createElement('section'); const h3 = document.createElement('h3'); h3.textContent = t.courseTests;
    const results = document.createElement('div'); results.className = 'dashboard-list';
    const note = document.createElement('p'); note.className = 'empty-note'; note.textContent = t.loadingTests;
    results.append(note); tests.append(h3, results);
    body.append(scoped(t.courseLessons, lessons, t.noLessons), scoped(t.courseExercises, exercises, t.noExercises), tests);
    disclosure.append(heading, body); courses.append(disclosure);
    disclosure.addEventListener('toggle', async () => {
      if (!disclosure.open || disclosure.dataset.loaded) return;
      disclosure.dataset.loaded = 'true';
      try {
        const query = new URLSearchParams({ level: item.level, area: item.area, language: item.language });
        const response = await fetch(`/student/tests/results?${query}`, { credentials: 'same-origin', cache: 'no-store' });
        if (!response.ok) throw new Error('tests');
        const data = await response.json() as { results: { chapter: number; best_score: number; last_attempt: string }[] };
        const entries = data.results.map(row => record(`/tests/?${new URLSearchParams({ level: item.level, area: item.area, lang: item.language, chapter: String(row.chapter) })}`,
          `${t.lesson} ${row.chapter} · ${t.bestScore} ${row.best_score}/10`, dateLabel(row.last_attempt, language)));
        appendLimited(results, entries, t.noTests, t.older, 12);
      } catch { results.textContent = t.testError; delete disclosure.dataset.loaded; }
    });
  }
  if (!report.courses.length) { const note = document.createElement('p'); note.className = 'empty-note'; note.textContent = t.noActivity; courses.append(note); }
}
