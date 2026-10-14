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
  const lesson = location.pathname.match(/^\/courses\/([a-z0-9-]+)\/([a-z0-9-]+)\/(?:lessons|chapters)\/([a-z]{2})\/(\d+)\/?$/);
  if (lesson) {
    const payload = { level: lesson[1], area: lesson[2], language: lesson[3], chapter: Number(lesson[4]) };
    const send = (kind, seconds = 0) => fetch('/student/activity', {
      method: 'POST', credentials: 'same-origin', keepalive: true,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...payload, kind, seconds }),
    }).catch(() => {});
    fetch('/auth/me', { credentials: 'same-origin', cache: 'no-store' }).then(response => {
      if (!response.ok) return;
      void send('lesson_opened');
      const labels = lesson[3] === 'pt' ? ['Sua análise da aula', 'Salvar análise', 'Análise salva.']
        : lesson[3] === 'es' ? ['Tu análisis de la lección', 'Guardar análisis', 'Análisis guardado.']
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
    }).catch(() => {});
  }
})();
