/* Optional page-view analytics. The Google tag is never requested without consent. */
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
  const key = 'open-cyber-academy-analytics-choice';
  const restricted = navigator.globalPrivacyControl === true || navigator.doNotTrack === '1';
  let choice = null;
  try { choice = localStorage.getItem(key); } catch (_) { /* Storage can be unavailable. */ }

  function startAnalytics() {
    if (restricted || window.__openCyberAnalyticsStarted) return;
    window.__openCyberAnalyticsStarted = true;
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
    else if (wasRunning) location.reload();
  }

  function showChoice() {
    document.getElementById('analytics-consent')?.remove();
    const box = document.createElement('aside');
    box.id = 'analytics-consent';
    box.setAttribute('aria-label', 'Optional analytics preference');
    const text = document.createElement('p');
    text.textContent = labels.prompt;
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
