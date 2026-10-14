import mermaid from 'mermaid';

const language = document.documentElement.lang;
const words = {
  en: { explore: 'Scroll to explore the diagram', source: 'View diagram source', full: 'Open full diagram', text: 'Text version', generic: 'Lesson diagram' },
  pt: { explore: 'Deslize para explorar o diagrama', source: 'Ver código do diagrama', full: 'Abrir diagrama completo', text: 'Versão em texto', generic: 'Diagrama da aula' },
  es: { explore: 'Desplázate para explorar el diagrama', source: 'Ver código del diagrama', full: 'Abrir diagrama completo', text: 'Versión en texto', generic: 'Diagrama de la lección' },
}[language] || { explore: 'Scroll to explore the diagram', source: 'View diagram source', full: 'Open full diagram', text: 'Text version', generic: 'Lesson diagram' };

const diagrams = [];
let serial = 0;

function disclosure(label, content) {
  const details = document.createElement('details');
  const summary = document.createElement('summary');
  summary.textContent = label;
  details.append(summary, content);
  return details;
}

async function renderDiagram(item) {
  try {
    const { svg } = await mermaid.render(`oca-diagram-${++serial}`, item.code);
    const url = URL.createObjectURL(new Blob([svg], { type: 'image/svg+xml' }));
    const image = document.createElement('img');
    image.src = url;
    image.alt = item.title;
    image.loading = 'lazy';
    const link = document.createElement('a');
    link.href = url;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.setAttribute('aria-label', `${words.full}: ${item.title}`);
    link.append(image);
    item.viewport.replaceChildren(link);
    if (item.url) URL.revokeObjectURL(item.url);
    item.url = url;
  } catch (_) {
    // Keep the authored Mermaid code available when a particular chart fails.
    if (!item.figure.isConnected) return;
    const alternative = item.figure.querySelector('details:nth-of-type(2)');
    item.figure.replaceWith(item.source);
    if (alternative) item.source.after(alternative);
  }
}

async function renderAll() {
  mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'strict',
    theme: document.documentElement.dataset.theme === 'light' ? 'default' : 'dark',
    flowchart: { htmlLabels: false, useMaxWidth: false },
    themeVariables: { fontFamily: 'Titillium Web, sans-serif' },
  });
  for (const item of diagrams) await renderDiagram(item);
}

for (const block of document.querySelectorAll('.prose pre code.language-mermaid')) {
  const source = block.parentElement;
  const code = block.textContent || '';
  const title = source.previousElementSibling?.matches('h2,h3,h4')
    ? source.previousElementSibling.textContent.trim() : words.generic;
  const figure = document.createElement('figure');
  figure.className = 'diagram';
  const viewport = document.createElement('div');
  viewport.className = 'diagram-viewport';
  viewport.setAttribute('role', 'region');
  viewport.setAttribute('aria-label', title);
  viewport.tabIndex = 0;
  const caption = document.createElement('figcaption');
  caption.textContent = words.explore;
  figure.append(viewport, caption);
  source.replaceWith(figure);
  figure.append(disclosure(words.source, source));

  const alternative = figure.nextElementSibling;
  if (alternative?.matches('pre') && alternative.querySelector('code.language-text')) {
    figure.append(disclosure(words.text, alternative));
  }
  diagrams.push({ code, title, figure, viewport, source, url: null });
}

if (diagrams.length) {
  renderAll();
  window.addEventListener('oca-theme-change', renderAll);
  window.addEventListener('pagehide', () => {
    for (const item of diagrams) if (item.url) URL.revokeObjectURL(item.url);
  }, { once: true });
}
