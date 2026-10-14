/* Optional page-view analytics. The Google tag is never requested without consent. */
(() => {
  const measurementId = 'G-7KDGFR12FS';
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
    text.textContent = 'Learning is free without an account. May we use Google Analytics for aggregate page-view statistics? The tag loads only if you agree.';
    const actions = document.createElement('div');
    const decline = document.createElement('button'); decline.type = 'button'; decline.textContent = 'No thanks';
    const accept = document.createElement('button'); accept.type = 'button'; accept.textContent = 'Allow analytics';
    decline.addEventListener('click', () => store('no'));
    accept.addEventListener('click', () => store('yes'));
    const privacy = document.createElement('a'); privacy.href = '/privacy/'; privacy.textContent = 'Privacy details';
    actions.append(decline, accept, privacy); box.append(text, actions); document.body.append(box);
  }

  const settings = document.createElement('button');
  settings.id = 'analytics-settings';
  settings.type = 'button';
  settings.textContent = 'Analytics preferences';
  settings.addEventListener('click', showChoice);
  document.querySelector('.footer .shell, .footer-inner')?.append(settings);
  if (restricted) return;
  if (choice === 'yes') startAnalytics();
  else if (choice !== 'no') showChoice();
})();
