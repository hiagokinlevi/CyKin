/* Public, aggregated, opt-in usage counts. No personal records are returned. */
(() => {
  if (!document.querySelector('[data-insight], [data-exercise-insight], [data-exercise-browsers]')) return;
  const language = document.documentElement.lang || 'en';
  const number = new Intl.NumberFormat(language);
  let pending = false;
  const refresh = async () => {
    if (pending) return;
    pending = true;
    try {
      const edition = new URLSearchParams(location.search).get('lang') || '';
      const params = new URLSearchParams({ path: location.pathname });
      if (/^[a-z]{2}$/.test(edition)) params.set('edition', edition);
      const response = await fetch(`/api/insights?${params}`, { cache: 'no-store' });
      if (!response.ok) throw new Error('Insights unavailable');
      const data = await response.json();
      for (const element of document.querySelectorAll('[data-insight]')) {
        const [scope, metric] = element.getAttribute('data-insight').split('.');
        const value = data[scope]?.[metric] ?? data[scope];
        if (typeof value === 'number') element.textContent = number.format(value);
      }
      for (const element of document.querySelectorAll('[data-exercise-insight]')) {
        const id = element.getAttribute('data-exercise-insight');
        const value = data.exercises_by_id?.[id]?.opens || 0;
        element.textContent = number.format(value);
      }
      for (const element of document.querySelectorAll('[data-exercise-browsers]')) {
        const id = element.getAttribute('data-exercise-browsers');
        const value = data.exercises_by_id?.[id]?.browsers || 0;
        element.textContent = number.format(value);
      }
      document.querySelectorAll('[data-insight-status]').forEach(element => { element.textContent = ''; });
    } catch {
      document.querySelectorAll('[data-insight-status]').forEach(element => {
        element.textContent = language === 'pt' ? 'Métricas indisponíveis no momento.' :
          language === 'es' ? 'Métricas no disponibles ahora.' : 'Usage counts are temporarily unavailable.';
      });
    } finally { pending = false; }
  };
  void refresh();
  window.addEventListener('oca-insights-updated', () => { void refresh(); });
})();
