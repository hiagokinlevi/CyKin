/* Optional page-view analytics. Nothing is recorded before a positive choice. */
(() => {
  const measurementId = 'G-7KDGFR12FS';
  const language = location.hostname.split('.')[0];
  const labels = {
    pt: { prompt: 'O ensino é gratuito e não exige cadastro. Você permite o uso do Google Analytics para estatísticas agregadas de visualização? A ferramenta só será carregada com sua autorização.', no: 'Não, obrigado', yes: 'Permitir analytics', privacy: 'Detalhes de privacidade', settings: 'Preferências de analytics' },
    es: { prompt: 'El aprendizaje es gratuito y no requiere registro. ¿Permites usar Google Analytics para estadísticas agregadas de visitas? La herramienta solo se carga con tu autorización.', no: 'No, gracias', yes: 'Permitir analytics', privacy: 'Detalles de privacidad', settings: 'Preferencias de analytics' },
    he: { prompt: 'הלימוד חינם ואינו דורש הרשמה. האם לאפשר ל-Google Analytics לאסוף נתוני צפייה מצטברים? הכלי ייטען רק לאחר הסכמתך.', no: 'לא תודה', yes: 'אישור נתונים', privacy: 'פרטי פרטיות', settings: 'העדפות נתונים' },
    fr: { prompt: 'Les cours sont gratuits et sans inscription. Autorisez-vous Google Analytics à recueillir des statistiques de consultation agrégées ? Le service ne se charge qu’avec votre accord.', no: 'Non merci', yes: 'Autoriser', privacy: 'Confidentialité', settings: 'Préférences statistiques' },
    ru: { prompt: 'Обучение бесплатно и не требует регистрации. Разрешить Google Analytics собирать сводную статистику посещений? Сервис загрузится только с вашего согласия.', no: 'Нет, спасибо', yes: 'Разрешить', privacy: 'Конфиденциальность', settings: 'Настройки аналитики' },
    de: { prompt: 'Das Lernen ist kostenlos und ohne Anmeldung möglich. Dürfen wir Google Analytics für zusammengefasste Seitenstatistiken verwenden? Der Dienst lädt nur mit Ihrer Einwilligung.', no: 'Nein, danke', yes: 'Zulassen', privacy: 'Datenschutz', settings: 'Analyse-Einstellungen' },
    zh: { prompt: '学习免费且无需注册。是否允许 Google Analytics 收集汇总访问统计？只有在您同意后才会加载该工具。', no: '不用，谢谢', yes: '允许', privacy: '隐私说明', settings: '分析偏好' },
    ja: { prompt: '学習は無料で登録も不要です。Google Analytics による集計閲覧統計を許可しますか？同意した場合にのみ読み込まれます。', no: '許可しない', yes: '許可する', privacy: 'プライバシー', settings: '解析設定' },
  }[language] || { prompt: 'Learning is free without an account. May we use Google Analytics for aggregate page-view statistics? The tag loads only if you agree.', no: 'No thanks', yes: 'Allow analytics', privacy: 'Privacy details', settings: 'Analytics preferences' };
  const counterNote = {
    pt: ' Com sua permissão, a Academy também mostrará contadores públicos de visualizações, leituras e exercícios. Um identificador aleatório do navegador é resumido por hash e os eventos expiram em 30 dias.',
    es: ' Con tu permiso, la Academy también mostrará contadores públicos de visualizaciones, lecturas y ejercicios. Un identificador aleatorio del navegador se guarda como hash y los eventos vencen en 30 días.',
    he: ' בהסכמתכם, האקדמיה תציג גם מוני צפיות, קריאה ותרגילים. מזהה דפדפן אקראי נשמר כ-hash והאירועים נמחקים כעבור 30 יום.',
    fr: ' Avec votre accord, l’Academy affichera aussi les consultations, lectures et exercices. Un identifiant de navigateur aléatoire est haché et les événements expirent après 30 jours.',
    ru: ' С вашего согласия Academy также покажет просмотры, чтения и открытия упражнений. Случайный идентификатор браузера хранится в виде хеша; события удаляются через 30 дней.',
    de: ' Mit Ihrer Einwilligung zeigt die Academy auch Aufrufe, Lesevorgänge und geöffnete Übungen. Eine zufällige Browser-ID wird gehasht; Ereignisse verfallen nach 30 Tagen.',
    zh: ' 经您同意，Academy 还将显示页面浏览、阅读和练习打开次数。随机浏览器标识符仅以哈希保存，事件将在 30 天后删除。',
    ja: ' 同意された場合、Academy は閲覧・読書・演習の公開件数も表示します。ランダムなブラウザー識別子はハッシュ化され、記録は30日後に削除されます。',
  }[language] || ' With your permission, the Academy also displays public counts of views, reading sessions and exercise opens. A random browser identifier is hashed and events expire after 30 days.';
  // Public counters expand the purpose of the earlier Google-only preference.
  // Ask existing visitors again before collecting first-party events.
  const key = 'open-cyber-academy-analytics-choice-v2';
  const restricted = navigator.globalPrivacyControl === true || navigator.doNotTrack === '1';
  let choice = null;
  try { choice = localStorage.getItem(key); } catch (_) { /* Storage can be unavailable. */ }

  const visitKey = 'open-cyber-academy-visitor';
  let visitor = null;
  function participant() {
    if (visitor) return visitor;
    try { visitor = localStorage.getItem(visitKey); } catch (_) { /* Private mode. */ }
    if (!/^[a-f0-9]{32}$/.test(visitor || '')) {
      const bytes = new Uint8Array(16); crypto.getRandomValues(bytes);
      visitor = [...bytes].map(byte => byte.toString(16).padStart(2, '0')).join('');
      try { localStorage.setItem(visitKey, visitor); } catch (_) { /* Session only. */ }
    }
    return visitor;
  }
  function record(event, exerciseId = '') {
    if (restricted || choice !== 'yes') return;
    const edition = new URLSearchParams(location.search).get('lang') || '';
    fetch('/api/insights/collect', { method: 'POST', credentials: 'same-origin', keepalive: true,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ visitor: participant(), event, path: location.pathname,
        exercise_id: exerciseId, edition: /^[a-z]{2}$/.test(edition) ? edition : '' }),
    }).then(() => window.dispatchEvent(new Event('oca-insights-updated'))).catch(() => {});
  }
  function startFirstParty() {
    record('view');
    if (/^\/courses\/[^/]+\/[^/]+\/(?:lessons|chapters)\/[a-z]{2}\/\d+\/?$/.test(location.pathname)) {
      let visible = 0; let completed = false;
      const timer = setInterval(() => {
        if (!document.hidden) visible += 1;
        if (visible >= 30) { clearInterval(timer); completed = true; record('read'); }
      }, 1000);
      addEventListener('pagehide', () => { if (!completed) clearInterval(timer); }, { once: true });
      document.addEventListener('click', event => {
        const target = event.target instanceof Element ? event.target : null;
        const link = target?.closest('a[href^="#exercise-ex"],a[href^="#answer-ex"]');
        const card = target?.closest('.exercise-attempt');
        const id = card?.getAttribute('data-exercise-id') ||
          link?.getAttribute('href')?.match(/ex(\d{3,4})$/)?.[1];
        if (id) record('exercise', id.startsWith('EX') ? id : `EX${id}`);
      });
    }
  }

  function startAnalytics() {
    if (restricted || window.__openCyberAnalyticsStarted) return;
    window.__openCyberAnalyticsStarted = true;
    startFirstParty();
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', measurementId, { send_page_view: false });
    window.gtag('event', 'page_view', { page_location: location.origin + location.pathname, page_title: document.title });
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + measurementId;
    document.head.append(script);
  }

  function store(next) {
    const wasRunning = Boolean(window.__openCyberAnalyticsStarted);
    choice = next;
    try { localStorage.setItem(key, next); } catch (_) { /* Session-only choice. */ }
    document.getElementById('analytics-consent')?.remove();
    if (next === 'yes') startAnalytics();
    else {
      visitor = null;
      try { localStorage.removeItem(visitKey); } catch (_) { /* Private mode. */ }
      if (wasRunning) location.reload();
    }
  }

  function showChoice() {
    document.getElementById('analytics-consent')?.remove();
    const box = document.createElement('aside');
    box.id = 'analytics-consent';
    box.setAttribute('aria-label', 'Optional analytics preference');
    const text = document.createElement('p');
    text.textContent = labels.prompt + counterNote;
    const actions = document.createElement('div');
    const decline = document.createElement('button'); decline.type = 'button'; decline.textContent = labels.no;
    const accept = document.createElement('button'); accept.type = 'button'; accept.textContent = labels.yes;
    decline.addEventListener('click', () => store('no'));
    accept.addEventListener('click', () => store('yes'));
    const privacy = document.createElement('a'); privacy.href = '/privacy/'; privacy.textContent = labels.privacy;
    actions.append(decline, accept, privacy); box.append(text, actions); document.body.append(box);
  }

  const settings = document.createElement('button');
  settings.id = 'analytics-settings';
  settings.type = 'button';
  settings.textContent = labels.settings;
  settings.addEventListener('click', showChoice);
  document.querySelector('.footer .shell, .footer-inner')?.append(settings);
  if (restricted) return;
  if (choice === 'yes') startAnalytics();
  else if (choice !== 'no') showChoice();
})();
