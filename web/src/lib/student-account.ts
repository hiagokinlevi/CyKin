import { siteLanguage } from './i18n';

type Lesson = { level: string; area: string; language: string; chapter: number; status: string; updated_at: string };
type Exercise = Lesson & { exercise_id: string };
type CoursePerformance = { level: string; area: string; language: string; lesson_visits: number; read_seconds: number;
  lessons_completed: number; exercises_saved: number; analyses_saved: number; chapters_tested: number;
  best_correct: number; best_possible: number };
type CatalogCourse = { level: string; area: string; title: string; titles: Record<string, string> };

const copy = {
  en: {
    eyebrow: 'STUDENT AREA', heading: 'Your learning, at your pace.', intro: 'Every book and lesson is free to read. Sign in to save your progress and take chapter tests.', tests: 'Explore chapter tests →', identity: 'STUDENT ACCOUNT', email: 'Email address', send: 'Send code', code: 'Six-digit code', signin: 'Sign in', back: 'Use another email', signout: 'Sign out', benefits: 'YOUR STUDY AREA', benefitsTitle: 'What you can track', lessons: 'Completed lessons', lessonsDetail: 'Mark a lesson when you finish reading.', exercises: 'Exercise attempts', exercisesDetail: 'Save your answers and continue later.', media: 'Audio and video', mediaDetail: 'Planned for later; reading is already open.', history: 'MY HISTORY', historyTitle: 'Saved progress', continue: 'Continue learning →', returnAfterSignIn: 'After signing in, you will return to your test or lesson.',
    checking: 'Checking your session…', noPassword: 'Email sign-in uses a one-time code.', enterEmail: 'Sign in with your email', sent: 'If the address can receive mail, a six-digit code is on its way. It expires in 10 minutes.', enterCode: 'Enter the code from your email', sending: 'Sending a code…', verifying: 'Checking the code…', failed: 'Sign-in is unavailable right now. Please try again later.', limited: 'Too many requests. Please try again later.', invalid: 'The code is invalid or expired. Check it or request a new one.', active: 'Your progress belongs only to this account.', pending: 'Sign in to see your lessons and attempts.', empty: 'No lessons marked yet. Begin with a published lesson.', lesson: 'lesson', completed: 'Completed', inProgress: 'In progress', summary: (lessons: number, exercises: number) => `${lessons} lessons marked · ${exercises} exercise attempts saved.`, username: 'Username', password: 'Password', passwordMethod: 'Use username and password', emailMethod: 'Use email code', enterPassword: 'Sign in with username', invalidPassword: 'Invalid username or password.', stats: (opens: number, seconds: number, analyses: number, tests: number) => `${opens} lesson visits · ${Math.floor(seconds / 60)} reading minutes · ${analyses} analyses · ${tests} completed tests.`, performanceTitle: 'Performance by course', performance: (row: CoursePerformance) => `${row.lessons_completed} lessons completed · ${row.exercises_saved} exercises · ${row.analyses_saved} analyses · ${row.chapters_tested} chapter tests · best answers ${row.best_correct}/${row.best_possible} · ${Math.floor(row.read_seconds / 60)} reading minutes`,
  },
  pt: {
    eyebrow: 'ÁREA DO ESTUDANTE', heading: 'Seu aprendizado, no seu ritmo.', intro: 'Todos os livros e aulas são gratuitos e abertos. Entre para salvar seu progresso e fazer testes.', tests: 'Explorar testes por capítulo →', identity: 'CONTA DO ESTUDANTE', email: 'Endereço de email', send: 'Enviar código', code: 'Código de seis dígitos', signin: 'Entrar', back: 'Usar outro email', signout: 'Sair', benefits: 'SUA ÁREA DE ESTUDO', benefitsTitle: 'O que você pode acompanhar', lessons: 'Aulas concluídas', lessonsDetail: 'Marque uma aula ao terminar de lê-la.', exercises: 'Tentativas de exercícios', exercisesDetail: 'Salve suas respostas e continue depois.', media: 'Áudio e vídeo', mediaDetail: 'Planejados para depois; a leitura já está aberta.', history: 'MEU HISTÓRICO', historyTitle: 'Progresso salvo', continue: 'Continuar estudando →', returnAfterSignIn: 'Após entrar, você voltará ao teste ou à aula.',
    checking: 'Verificando sua sessão…', noPassword: 'O acesso por email usa um código único.', enterEmail: 'Entre com seu email', sent: 'Se o endereço receber mensagens, um código de seis dígitos está a caminho. Ele expira em 10 minutos.', enterCode: 'Digite o código enviado ao seu email', sending: 'Enviando código…', verifying: 'Verificando código…', failed: 'Não foi possível entrar agora. Tente novamente mais tarde.', limited: 'Muitas solicitações. Tente novamente mais tarde.', invalid: 'Código inválido ou expirado. Confira ou solicite outro.', active: 'Seu progresso pertence somente a esta conta.', pending: 'Entre para ver suas aulas e tentativas.', empty: 'Nenhuma aula marcada ainda. Comece por uma aula publicada.', lesson: 'aula', completed: 'Concluída', inProgress: 'Em andamento', summary: (lessons: number, exercises: number) => `${lessons} aulas marcadas · ${exercises} tentativas de exercícios salvas.`, username: 'Usuário', password: 'Senha', passwordMethod: 'Usar usuário e senha', emailMethod: 'Usar código por email', enterPassword: 'Entrar com usuário', invalidPassword: 'Usuário ou senha inválidos.', stats: (opens: number, seconds: number, analyses: number, tests: number) => `${opens} visitas a aulas · ${Math.floor(seconds / 60)} minutos de leitura · ${analyses} análises · ${tests} testes concluídos.`, performanceTitle: 'Rendimento por curso', performance: (row: CoursePerformance) => `${row.lessons_completed} aulas concluídas · ${row.exercises_saved} exercícios · ${row.analyses_saved} análises · ${row.chapters_tested} testes · melhores respostas ${row.best_correct}/${row.best_possible} · ${Math.floor(row.read_seconds / 60)} minutos de leitura`,
  },
  es: {
    eyebrow: 'ÁREA DEL ESTUDIANTE', heading: 'Aprende a tu ritmo.', intro: 'Todos los libros y lecciones son gratuitos y abiertos. Accede para guardar tu progreso y hacer pruebas.', tests: 'Explorar pruebas por capítulo →', identity: 'CUENTA DE ESTUDIANTE', email: 'Correo electrónico', send: 'Enviar código', code: 'Código de seis dígitos', signin: 'Entrar', back: 'Usar otro correo', signout: 'Cerrar sesión', benefits: 'TU ÁREA DE ESTUDIO', benefitsTitle: 'Qué puedes seguir', lessons: 'Lecciones completadas', lessonsDetail: 'Marca una lección al terminar de leerla.', exercises: 'Intentos de ejercicios', exercisesDetail: 'Guarda tus respuestas y continúa después.', media: 'Audio y vídeo', mediaDetail: 'Previstos para más adelante; la lectura ya está abierta.', history: 'MI HISTORIAL', historyTitle: 'Progreso guardado', continue: 'Seguir aprendiendo →', returnAfterSignIn: 'Después de acceder, volverás a la prueba o lección.',
    checking: 'Comprobando tu sesión…', noPassword: 'El acceso por correo usa un código único.', enterEmail: 'Accede con tu correo', sent: 'Si la dirección puede recibir mensajes, un código de seis dígitos está en camino. Caduca en 10 minutos.', enterCode: 'Introduce el código de tu correo', sending: 'Enviando código…', verifying: 'Comprobando código…', failed: 'No se puede acceder ahora. Inténtalo más tarde.', limited: 'Demasiadas solicitudes. Inténtalo más tarde.', invalid: 'Código inválido o caducado. Revísalo o solicita otro.', active: 'Tu progreso pertenece solo a esta cuenta.', pending: 'Inicia sesión para ver tus lecciones e intentos.', empty: 'Aún no has marcado lecciones. Empieza por una lección publicada.', lesson: 'lección', completed: 'Completada', inProgress: 'En curso', summary: (lessons: number, exercises: number) => `${lessons} lecciones marcadas · ${exercises} intentos de ejercicios guardados.`, username: 'Usuario', password: 'Contraseña', passwordMethod: 'Usar usuario y contraseña', emailMethod: 'Usar código por correo', enterPassword: 'Acceder con usuario', invalidPassword: 'Usuario o contraseña incorrectos.', stats: (opens: number, seconds: number, analyses: number, tests: number) => `${opens} visitas a lecciones · ${Math.floor(seconds / 60)} minutos de lectura · ${analyses} análisis · ${tests} pruebas completadas.`, performanceTitle: 'Rendimiento por curso', performance: (row: CoursePerformance) => `${row.lessons_completed} lecciones completadas · ${row.exercises_saved} ejercicios · ${row.analyses_saved} análisis · ${row.chapters_tested} pruebas · mejores respuestas ${row.best_correct}/${row.best_possible} · ${Math.floor(row.read_seconds / 60)} minutos de lectura`,
  },
};

export async function initializeStudentAccount(): Promise<void> {
  const t = copy[siteLanguage()];
  for (const element of document.querySelectorAll<HTMLElement>('[data-account]')) {
    const key = element.dataset.account as keyof typeof t;
    const value = t[key];
    if (typeof value === 'string') element.textContent = value;
  }
  const title = document.getElementById('profile-title')!;
  const description = document.getElementById('profile-description')!;
  const message = document.getElementById('account-message')!;
  const status = document.getElementById('records-status')!;
  const list = document.getElementById('records-list')!;
  const emailForm = document.getElementById('email-form') as HTMLFormElement;
  const codeForm = document.getElementById('code-form') as HTMLFormElement;
  const passwordForm = document.getElementById('password-form') as HTMLFormElement;
  const methodToggle = document.getElementById('method-toggle') as HTMLButtonElement;
  const emailInput = document.getElementById('account-email') as HTMLInputElement;
  const codeInput = document.getElementById('account-code') as HTMLInputElement;
  const usernameInput = document.getElementById('account-username') as HTMLInputElement;
  const passwordInput = document.getElementById('account-password') as HTMLInputElement;
  const logout = document.getElementById('account-logout') as HTMLButtonElement;
  const stats = document.getElementById('account-stats')!;
  const courseStats = document.getElementById('account-courses')!;
  const courseStatsTitle = document.getElementById('account-courses-title')!;
  const next = new URLSearchParams(location.search).get('next');
  const safeNext = next && /^\/(?:tests|courses)\//.test(next) && !next.includes('\\') ? next : null;
  const returnNotice = document.getElementById('return-after-signin')!;
  if (safeNext) { returnNotice.textContent = t.returnAfterSignIn; returnNotice.hidden = false; }
  const post = (url: string, payload: unknown) => fetch(url, { method: 'POST', credentials: 'same-origin', cache: 'no-store', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  let flowId = '';

  function showEmail(): void {
    emailForm.hidden = false; codeForm.hidden = true; passwordForm.hidden = true;
    methodToggle.hidden = false; methodToggle.textContent = t.passwordMethod; logout.hidden = true;
    title.textContent = t.enterEmail; description.textContent = t.noPassword;
  }
  function showCode(): void {
    emailForm.hidden = true; codeForm.hidden = false; passwordForm.hidden = true; methodToggle.hidden = true; logout.hidden = true;
    title.textContent = t.enterCode; description.textContent = t.sent; codeInput.focus();
  }
  function showPassword(): void {
    emailForm.hidden = true; codeForm.hidden = true; passwordForm.hidden = false;
    methodToggle.hidden = false; methodToggle.textContent = t.emailMethod; logout.hidden = true;
    title.textContent = t.enterPassword; description.textContent = t.active; usernameInput.focus();
  }
  async function showAccount(): Promise<void> {
    const me = await fetch('/auth/me', { credentials: 'same-origin', cache: 'no-store' });
    if (!me.ok) { showEmail(); return; }
    if (safeNext) { location.assign(safeNext); return; }
    const user = await me.json() as { email: string | null; username: string | null };
    emailForm.hidden = true; codeForm.hidden = true; passwordForm.hidden = true; methodToggle.hidden = true; logout.hidden = false;
    title.textContent = user.username || user.email || t.identity; description.textContent = t.active; message.textContent = '';
    const response = await fetch('/student/progress', { credentials: 'same-origin', cache: 'no-store' });
    if (!response.ok) { status.textContent = t.failed; return; }
    const data = await response.json() as { lessons: Lesson[]; exercises: Exercise[] };
    status.textContent = data.lessons.length ? t.summary(data.lessons.length, data.exercises.length) : t.empty;
    const activity = await fetch('/student/stats', { credentials: 'same-origin', cache: 'no-store' });
    if (activity.ok) {
      const report = await activity.json() as { summary: { activity: Record<string, { events: number; seconds: number }>; analyses_saved: number; tests_completed: number }; courses: CoursePerformance[] };
      stats.textContent = t.stats(report.summary.activity.lesson_opened?.events || 0,
        report.summary.activity.lesson_read?.seconds || 0, report.summary.analyses_saved, report.summary.tests_completed);
      courseStats.replaceChildren(); courseStatsTitle.hidden = report.courses.length === 0;
      let titles = new Map<string, string>();
      try {
        const catalog = await fetch('/api/catalog', { cache: 'no-store' });
        if (catalog.ok) {
          const data = await catalog.json() as { courses: CatalogCourse[] };
          titles = new Map(data.courses.map(item => [`${item.level}/${item.area}`, item.titles?.[siteLanguage()] || item.title]));
        }
      } catch { /* The course slug still identifies it if the catalog is unavailable. */ }
      for (const item of report.courses) {
        const anchor = document.createElement('a'); anchor.className = 'record';
        anchor.href = `/courses/${encodeURIComponent(item.level)}/${encodeURIComponent(item.area)}/?lang=${encodeURIComponent(item.language)}`;
        const heading = document.createElement('strong');
        heading.textContent = `${titles.get(`${item.level}/${item.area}`) || item.area.replaceAll('-', ' ')} · ${item.language.toUpperCase()}`;
        const detail = document.createElement('span'); detail.textContent = t.performance(item);
        anchor.append(heading, detail); courseStats.append(anchor);
      }
    }
    list.replaceChildren();
    for (const item of data.lessons) {
      const anchor = document.createElement('a'); anchor.className = 'record';
      anchor.href = `/courses/${encodeURIComponent(item.level)}/${encodeURIComponent(item.area)}/?lang=${encodeURIComponent(item.language)}&chapter=${item.chapter}`;
      const heading = document.createElement('strong');
      heading.textContent = `${item.area.replaceAll('-', ' ')} · ${t.lesson} ${String(item.chapter).padStart(2, '0')}`;
      const detail = document.createElement('span');
      detail.textContent = `${item.language.toUpperCase()} · ${item.status === 'completed' ? t.completed : t.inProgress} · ${item.updated_at}`;
      anchor.append(heading, detail); list.append(anchor);
    }
  }
  emailForm.addEventListener('submit', async event => {
    event.preventDefault(); if (!emailForm.reportValidity()) return;
    const button = emailForm.querySelector<HTMLButtonElement>('button[type="submit"]')!;
    button.disabled = true; message.textContent = t.sending;
    try {
      const response = await post('/auth/request-code', { email: emailInput.value.trim(), language: siteLanguage() });
      if (response.status === 429) throw new Error('limited');
      if (!response.ok) throw new Error('send');
      flowId = (await response.json() as { flow_id: string }).flow_id;
      message.textContent = ''; showCode();
    } catch (error) { message.textContent = error instanceof Error && error.message === 'limited' ? t.limited : t.failed; }
    finally { button.disabled = false; }
  });
  codeForm.addEventListener('submit', async event => {
    event.preventDefault(); if (!codeForm.reportValidity()) return;
    const button = codeForm.querySelector<HTMLButtonElement>('button[type="submit"]')!;
    button.disabled = true; message.textContent = t.verifying;
    try {
      const response = await post('/auth/verify-code', { flow_id: flowId, code: codeInput.value.trim() });
      if (!response.ok) throw new Error('code');
      if (safeNext) { location.assign(safeNext); return; }
      await showAccount();
    } catch { message.textContent = t.invalid; }
    finally { button.disabled = false; }
  });
  methodToggle.addEventListener('click', () => {
    message.textContent = '';
    if (passwordForm.hidden) showPassword(); else showEmail();
  });
  passwordForm.addEventListener('submit', async event => {
    event.preventDefault(); if (!passwordForm.reportValidity()) return;
    const button = passwordForm.querySelector<HTMLButtonElement>('button[type="submit"]')!;
    button.disabled = true; message.textContent = t.verifying;
    try {
      const response = await post('/auth/password-login', { username: usernameInput.value.trim(), password: passwordInput.value });
      passwordInput.value = '';
      if (response.status === 429) throw new Error('limited');
      if (!response.ok) throw new Error('invalid');
      if (safeNext) { location.assign(safeNext); return; }
      await showAccount();
    } catch (error) { message.textContent = error instanceof Error && error.message === 'limited' ? t.limited : t.invalidPassword; }
    finally { button.disabled = false; }
  });
  document.getElementById('code-back')!.addEventListener('click', () => {
    flowId = ''; codeInput.value = ''; message.textContent = ''; showEmail();
  });
  logout.addEventListener('click', async () => {
    logout.disabled = true;
    try {
      const response = await post('/auth/logout', {});
      if (!response.ok) throw new Error('logout');
      list.replaceChildren(); courseStats.replaceChildren(); courseStatsTitle.hidden = true;
      status.textContent = t.pending; stats.textContent = ''; showEmail(); message.textContent = '';
    } catch { message.textContent = t.failed; }
    finally { logout.disabled = false; }
  });
  status.textContent = t.pending; title.textContent = t.checking; description.textContent = t.noPassword;
  try { await showAccount(); } catch { showEmail(); message.textContent = t.failed; }
}
