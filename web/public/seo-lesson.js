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
})();
