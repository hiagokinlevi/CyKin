import { siteLanguage } from './i18n';

type Lesson = { level: string; area: string; language: string; chapter: number; status: string; updated_at: string };
type Exercise = Lesson & { exercise_id: string };

const copy = {
  en: {
    eyebrow: 'OPTIONAL STUDENT AREA', heading: 'Your learning, at your pace.', intro: 'Books and lessons are open without an account. Use an email code only to save progress and take chapter tests.', tests: 'Explore chapter tests →', identity: 'STUDENT ACCOUNT', email: 'Email address', send: 'Send code', code: 'Six-digit code', signin: 'Sign in', back: 'Use another email', signout: 'Sign out', benefits: 'YOUR STUDY AREA', benefitsTitle: 'What you can track', lessons: 'Completed lessons', lessonsDetail: 'Mark a lesson when you finish reading.', exercises: 'Exercise attempts', exercisesDetail: 'Save your answers and continue later.', media: 'Audio and video', mediaDetail: 'Planned for later; reading is already open.', history: 'MY HISTORY', historyTitle: 'Saved progress', continue: 'Continue learning →',
    checking: 'Checking your session…', noPassword: 'No password is required.', enterEmail: 'Sign in with your email', sent: 'If the address can receive mail, a six-digit code is on its way. It expires in 10 minutes.', enterCode: 'Enter the code from your email', sending: 'Sending a code…', verifying: 'Checking the code…', failed: 'Sign-in is unavailable right now. Please try again later.', limited: 'Too many requests. Please try again later.', invalid: 'The code is invalid or expired. Check it or request a new one.', active: 'Your progress belongs only to this account.', pending: 'Sign in to see your lessons and attempts.', empty: 'No lessons marked yet. Begin with a published lesson.', lesson: 'lesson', completed: 'Completed', inProgress: 'In progress', summary: (lessons: number, exercises: number) => `${lessons} lessons marked · ${exercises} exercise attempts saved.`,
  },
  pt: {
    eyebrow: 'ÁREA DO ESTUDANTE OPCIONAL', heading: 'Seu aprendizado, no seu ritmo.', intro: 'Livros e aulas são abertos sem cadastro. Use um código por email apenas para salvar o progresso ou fazer testes.', tests: 'Explorar testes por capítulo →', identity: 'CONTA DO ESTUDANTE', email: 'Endereço de email', send: 'Enviar código', code: 'Código de seis dígitos', signin: 'Entrar', back: 'Usar outro email', signout: 'Sair', benefits: 'SUA ÁREA DE ESTUDO', benefitsTitle: 'O que você pode acompanhar', lessons: 'Aulas concluídas', lessonsDetail: 'Marque uma aula ao terminar de lê-la.', exercises: 'Tentativas de exercícios', exercisesDetail: 'Salve suas respostas e continue depois.', media: 'Áudio e vídeo', mediaDetail: 'Planejados para depois; a leitura já está aberta.', history: 'MEU HISTÓRICO', historyTitle: 'Progresso salvo', continue: 'Continuar estudando →',
    checking: 'Verificando sua sessão…', noPassword: 'Não é necessária senha.', enterEmail: 'Entre com seu email', sent: 'Se o endereço receber mensagens, um código de seis dígitos está a caminho. Ele expira em 10 minutos.', enterCode: 'Digite o código enviado ao seu email', sending: 'Enviando código…', verifying: 'Verificando código…', failed: 'Não foi possível entrar agora. Tente novamente mais tarde.', limited: 'Muitas solicitações. Tente novamente mais tarde.', invalid: 'Código inválido ou expirado. Confira ou solicite outro.', active: 'Seu progresso pertence somente a esta conta.', pending: 'Entre para ver suas aulas e tentativas.', empty: 'Nenhuma aula marcada ainda. Comece por uma aula publicada.', lesson: 'aula', completed: 'Concluída', inProgress: 'Em andamento', summary: (lessons: number, exercises: number) => `${lessons} aulas marcadas · ${exercises} tentativas de exercícios salvas.`,
  },
  es: {
    eyebrow: 'ÁREA DE ESTUDIANTE OPCIONAL', heading: 'Aprende a tu ritmo.', intro: 'Los libros y las lecciones son abiertos sin cuenta. Usa un código por correo solo para guardar el progreso o hacer pruebas.', tests: 'Explorar pruebas por capítulo →', identity: 'CUENTA DE ESTUDIANTE', email: 'Correo electrónico', send: 'Enviar código', code: 'Código de seis dígitos', signin: 'Entrar', back: 'Usar otro correo', signout: 'Cerrar sesión', benefits: 'TU ÁREA DE ESTUDIO', benefitsTitle: 'Qué puedes seguir', lessons: 'Lecciones completadas', lessonsDetail: 'Marca una lección al terminar de leerla.', exercises: 'Intentos de ejercicios', exercisesDetail: 'Guarda tus respuestas y continúa después.', media: 'Audio y vídeo', mediaDetail: 'Previstos para más adelante; la lectura ya está abierta.', history: 'MI HISTORIAL', historyTitle: 'Progreso guardado', continue: 'Seguir aprendiendo →',
    checking: 'Comprobando tu sesión…', noPassword: 'No necesitas contraseña.', enterEmail: 'Accede con tu correo', sent: 'Si la dirección puede recibir mensajes, un código de seis dígitos está en camino. Caduca en 10 minutos.', enterCode: 'Introduce el código de tu correo', sending: 'Enviando código…', verifying: 'Comprobando código…', failed: 'No se puede acceder ahora. Inténtalo más tarde.', limited: 'Demasiadas solicitudes. Inténtalo más tarde.', invalid: 'Código inválido o caducado. Revísalo o solicita otro.', active: 'Tu progreso pertenece solo a esta cuenta.', pending: 'Inicia sesión para ver tus lecciones e intentos.', empty: 'Aún no has marcado lecciones. Empieza por una lección publicada.', lesson: 'lección', completed: 'Completada', inProgress: 'En curso', summary: (lessons: number, exercises: number) => `${lessons} lecciones marcadas · ${exercises} intentos de ejercicios guardados.`,
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
  const emailInput = document.getElementById('account-email') as HTMLInputElement;
  const codeInput = document.getElementById('account-code') as HTMLInputElement;
  const logout = document.getElementById('account-logout') as HTMLButtonElement;
  const next = new URLSearchParams(location.search).get('next');
  const safeNext = next && /^\/(?:tests|courses)\//.test(next) && !next.includes('\\') ? next : null;
  const post = (url: string, payload: unknown) => fetch(url, { method: 'POST', credentials: 'same-origin', cache: 'no-store', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  let flowId = '';

  function showEmail(): void {
    emailForm.hidden = false; codeForm.hidden = true; logout.hidden = true;
    title.textContent = t.enterEmail; description.textContent = t.noPassword;
  }
  function showCode(): void {
    emailForm.hidden = true; codeForm.hidden = false; logout.hidden = true;
    title.textContent = t.enterCode; description.textContent = t.sent; codeInput.focus();
  }
  async function showAccount(): Promise<void> {
    const me = await fetch('/auth/me', { credentials: 'same-origin', cache: 'no-store' });
    if (!me.ok) { showEmail(); return; }
    const user = await me.json() as { email: string };
    emailForm.hidden = true; codeForm.hidden = true; logout.hidden = false;
    title.textContent = user.email; description.textContent = t.active; message.textContent = '';
    const response = await fetch('/student/progress', { credentials: 'same-origin', cache: 'no-store' });
    if (!response.ok) { status.textContent = t.failed; return; }
    const data = await response.json() as { lessons: Lesson[]; exercises: Exercise[] };
    status.textContent = data.lessons.length ? t.summary(data.lessons.length, data.exercises.length) : t.empty;
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
  document.getElementById('code-back')!.addEventListener('click', () => {
    flowId = ''; codeInput.value = ''; message.textContent = ''; showEmail();
  });
  logout.addEventListener('click', async () => {
    logout.disabled = true;
    try {
      const response = await post('/auth/logout', {});
      if (!response.ok) throw new Error('logout');
      list.replaceChildren(); status.textContent = t.pending; showEmail(); message.textContent = '';
    } catch { message.textContent = t.failed; }
    finally { logout.disabled = false; }
  });
  status.textContent = t.pending; title.textContent = t.checking; description.textContent = t.noPassword;
  try { await showAccount(); } catch { showEmail(); message.textContent = t.failed; }
}
