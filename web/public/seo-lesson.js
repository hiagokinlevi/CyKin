(() => {
  document.getElementById('theme-toggle')?.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('open-cyber-academy-theme', next); } catch (_) { /* Private mode. */ }
    window.dispatchEvent(new Event('oca-theme-change'));
  });
  const revealAnswer = () => {
    if (/^#(?:answer-ex\d{3,4}|w\d+-answer-\d{2})$/.test(location.hash)) {
      const target = document.querySelector(location.hash);
      target?.closest('details')?.setAttribute('open', '');
    }
  };
  addEventListener('hashchange', revealAnswer);
  revealAnswer();

  // Record only signed-in study activity. Anonymous reading never reaches D1.
  const lesson = location.pathname.match(/^\/courses\/([a-z0-9-]+)\/([a-z0-9-]+)\/(lessons|chapters)\/([a-z]{2})\/(\d+)\/?$/);
  if (lesson) {
    const payload = { level: lesson[1], area: lesson[2], language: lesson[4], chapter: Number(lesson[5]) };
    const unitKind = lesson[3] === 'chapters' ? 'chapter' : 'lesson';
    const panel = document.querySelector('.progress-sidebar');
    const panelStatus = document.getElementById('progress-status');
    const signIn = document.getElementById('progress-signin');
    const dashboard = document.getElementById('progress-dashboard');
    const markButton = document.getElementById('mark-lesson-complete');
    const ui = lesson[4] === 'pt'
      ? { count: (n, total) => `${n} de ${total} aulas publicadas concluídas.`, unavailable: 'O progresso está indisponível agora.', marked: 'Aula concluída.', saved: 'Resposta salva na sua conta.', signIn: 'Entre para salvar sua resposta.', failed: 'Não foi possível salvar a resposta.' }
      : lesson[4] === 'es'
      ? { count: (n, total) => `${n} de ${total} lecciones publicadas completadas.`, unavailable: 'El progreso no está disponible ahora.', marked: 'Lección completada.', saved: 'Respuesta guardada en tu cuenta.', signIn: 'Inicia sesión para guardar tu respuesta.', failed: 'No se pudo guardar la respuesta.' }
      : { count: (n, total) => `${n} of ${total} published lessons completed.`, unavailable: 'Progress is unavailable right now.', marked: 'Lesson completed.', saved: 'Answer saved to your account.', signIn: 'Sign in to save your answer.', failed: 'Could not save the answer.' };
    for (const form of document.querySelectorAll('.exercise-attempt')) {
      form.addEventListener('submit', async event => {
        event.preventDefault();
        const answer = form.querySelector('textarea');
        const button = form.querySelector('button[type="submit"]');
        const status = form.querySelector('.exercise-attempt-status');
        if (!answer?.value.trim() || !button || !status) return;
        button.disabled = true;
        try {
          const response = await fetch('/student/progress/exercise', { method: 'POST', credentials: 'same-origin',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...payload, unit_kind: unitKind, exercise_id: form.dataset.exerciseId, answer: answer.value, status: 'attempted' }),
          });
          status.textContent = response.ok ? ui.saved : [401, 403].includes(response.status) ? ui.signIn : ui.failed;
          if (response.ok) void loadProgress();
          if ([401, 403].includes(response.status) && signIn) signIn.hidden = false;
        } catch { status.textContent = ui.failed; }
        finally { button.disabled = false; }
      });
    }
    const showGuest = () => { if (panelStatus) panelStatus.textContent = ''; if (signIn) signIn.hidden = false; };
    const loadProgress = async () => {
      if (!panel || !panelStatus) return;
      try {
        const [statsResponse, progressResponse] = await Promise.all([
          fetch('/student/stats', { credentials: 'same-origin', cache: 'no-store' }),
          fetch('/student/progress', { credentials: 'same-origin', cache: 'no-store' }),
        ]);
        if (!statsResponse.ok || !progressResponse.ok) throw new Error('Study record is unavailable');
        const [stats, progress] = await Promise.all([statsResponse.json(), progressResponse.json()]);
        const course = stats.courses.find(item => item.level === payload.level && item.area === payload.area && item.language === payload.language);
        const completed = Number(course?.lessons_completed || 0);
        const published = Number(panel.dataset.published || 0);
        document.getElementById('progress-completed').textContent = `${completed}/${published}`;
        document.getElementById('progress-exercises').textContent = String(course?.exercises_saved || 0);
        document.getElementById('progress-correct').textContent = `${course?.best_correct || 0}/${course?.best_possible || 0}`;
        document.getElementById('progress-metrics').hidden = false;
        panelStatus.textContent = ui.count(completed, published);
        if (dashboard) dashboard.hidden = false;
        const current = progress.lessons.find(item => item.level === payload.level && item.area === payload.area
          && item.language === payload.language && Number(item.chapter) === payload.chapter);
        if (markButton) markButton.hidden = current?.status === 'completed';
      } catch { panelStatus.textContent = ui.unavailable; }
    };
    markButton?.addEventListener('click', async () => {
      markButton.disabled = true;
      try {
        const response = await fetch('/student/progress/lesson', { method: 'POST', credentials: 'same-origin',
          headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ...payload, status: 'completed' }) });
        if (!response.ok) throw new Error('Could not save progress');
        panelStatus.textContent = ui.marked;
        markButton.hidden = true;
        await loadProgress();
      } catch { panelStatus.textContent = ui.unavailable; }
      finally { markButton.disabled = false; }
    });
    const send = (kind, seconds = 0) => fetch('/student/activity', {
      method: 'POST', credentials: 'same-origin', keepalive: true,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...payload, kind, seconds }),
    }).catch(() => {});
    fetch('/auth/me', { credentials: 'same-origin', cache: 'no-store' }).then(response => {
      if (!response.ok) { showGuest(); return; }
      void loadProgress();
      void send('lesson_opened');
      const labels = lesson[4] === 'pt' ? ['Sua análise da aula', 'Salvar análise', 'Análise salva.']
        : lesson[4] === 'es' ? ['Tu análisis de la lección', 'Guardar análisis', 'Análisis guardado.']
        : ['Your lesson analysis', 'Save analysis', 'Analysis saved.'];
      const section = document.createElement('section'); section.className = 'student-analysis';
      const heading = document.createElement('h2'); heading.textContent = labels[0];
      const form = document.createElement('form');
      const textarea = document.createElement('textarea'); textarea.rows = 6; textarea.maxLength = 10_000;
      textarea.setAttribute('aria-label', labels[0]);
      const button = document.createElement('button'); button.type = 'submit'; button.textContent = labels[1];
      const status = document.createElement('p'); status.setAttribute('role', 'status');
      form.append(textarea, button, status); section.append(heading, form);
      document.querySelector('article.prose')?.after(section);
      const query = new URLSearchParams({ ...payload, chapter: String(payload.chapter) });
      fetch(`/student/analysis?${query}`, { credentials: 'same-origin', cache: 'no-store' }).then(async result => {
        if (result.ok) textarea.value = (await result.json()).analysis?.note || '';
      }).catch(() => {});
      form.addEventListener('submit', async event => {
        event.preventDefault(); button.disabled = true;
        try {
          const result = await fetch('/student/analysis', { method: 'POST', credentials: 'same-origin',
            headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ...payload, note: textarea.value }) });
          status.textContent = result.ok ? labels[2] : '';
        } finally { button.disabled = false; }
      });
      let started = document.visibilityState === 'visible' ? Date.now() : 0;
      const flush = () => {
        if (!started) return;
        const seconds = Math.min(3600, Math.floor((Date.now() - started) / 1000));
        started = document.visibilityState === 'visible' ? Date.now() : 0;
        if (seconds > 0) void send('lesson_read', seconds);
      };
      document.addEventListener('visibilitychange', () => {
        flush();
        if (document.visibilityState === 'visible') started = Date.now();
      });
      window.addEventListener('pagehide', flush);
      window.setInterval(flush, 60_000);
    }).catch(showGuest);
  }
})();
