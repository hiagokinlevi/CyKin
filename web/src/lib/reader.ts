import { marked } from 'marked';
import DOMPurify from 'dompurify';

const REPO_VIEW = 'https://github.com/hiagokinlevi/CyKin/blob/main/';
const REPO_RAW = 'https://raw.githubusercontent.com/hiagokinlevi/CyKin/main/';

function sourcePath(url: URL): string | null {
  if (url.hostname === 'github.com') {
    const match = url.pathname.match(/^\/hiagokinlevi\/CyKin\/(?:blob|tree)\/main\/(.+)$/i);
    return match ? decodeURIComponent(match[1]) : null;
  }
  if (url.hostname === 'raw.githubusercontent.com') {
    const match = url.pathname.match(/^\/hiagokinlevi\/CyKin\/main\/(.+)$/i);
    return match ? decodeURIComponent(match[1]) : null;
  }
  return null;
}

export function internalSourceLink(href: string, sourceUrl: string, language: string, mode: 'book' | 'lesson' | 'reference' = 'lesson'): string | null {
  if (href.startsWith('#') && (mode !== 'lesson' || !/^#(?:ch-\d{2,4}|lesson-\d{2,4}|week-\d{2,4}-day-\d{2})$/i.test(href))) return href;
  let url: URL;
  try { url = new URL(href, sourceUrl); } catch { return null; }
  const path = sourcePath(url);
  if (!path) return null;
  if (path === 'README.md') return url.hash ? '/read/?path=README.md' + url.hash : '/';
  const course = path.match(/^levels\/([^/]+)\/([^/]+)\/(?:([a-z]{2})\/)?(.+)$/);
  if (course) {
    const [, level, area, edition, file] = course;
    const lang = edition || language;
    const query = new URLSearchParams({ lang });
    const coursePage = `/courses/${level}/${area}/`;
    if (file === 'book/MANUSCRIPT.md') {
      if (mode === 'book' && sourcePath(new URL(sourceUrl)) === path && url.hash) return url.hash;
      const lesson = url.hash.match(/^#lesson-(\d{2,4})$/i);
      if (lesson) { query.set('unit', 'daily'); query.set('chapter', String(Number(lesson[1]))); return coursePage + '?' + query; }
      const weekday = url.hash.match(/^#week-(\d{2,4})-day-(\d{2})$/i);
      if (weekday) { query.set('unit', 'daily'); query.set('chapter', String((Number(weekday[1]) - 1) * 5 + Number(weekday[2]))); return coursePage + '?' + query; }
      const chapter = url.hash.match(/^#ch-(\d{2,4})$/i);
      if (chapter && mode === 'lesson') { query.set('unit', 'chapter'); query.set('chapter', String(Number(chapter[1]))); return coursePage + '?' + query; }
      return '/book/?' + new URLSearchParams({ level, area, lang }) + url.hash;
    }
    if (file === 'SUBJECTS.md' || file === 'README.md') {
      const lesson = url.hash.match(/^#lesson-(\d{2,4})$/i);
      const weekday = url.hash.match(/^#week-(\d{2,4})-day-(\d{2})$/i);
      const chapter = url.hash.match(/^#ch-(\d{2,4})$/i);
      if (chapter) { query.set('unit', 'chapter'); query.set('chapter', String(Number(chapter[1]))); return coursePage + '?' + query; }
      if (lesson) { query.set('unit', 'daily'); query.set('chapter', String(Number(lesson[1]))); }
      if (weekday) { query.set('unit', 'daily'); query.set('chapter', String((Number(weekday[1]) - 1) * 5 + Number(weekday[2]))); }
      return coursePage + '?' + query;
    }
  }
  if (path.toLowerCase().endsWith('.md')) return '/read/?' + new URLSearchParams({ path }).toString() + url.hash;
  return null;
}

export async function renderMarkdown(target: HTMLElement, markdown: string, sourceUrl: string, language: string, mode: 'book' | 'lesson' | 'reference' = 'lesson'): Promise<void> {
  target.lang = language;
  target.dir = language === 'he' ? 'rtl' : 'ltr';
  for (const old of target.querySelectorAll<HTMLImageElement>('img[data-mermaid-url]')) URL.revokeObjectURL(old.dataset.mermaidUrl!);
  target.innerHTML = DOMPurify.sanitize(await marked.parse(markdown, { gfm: true }), { ADD_TAGS: ['input'], ADD_ATTR: ['class', 'id'] });
  const directory = sourceUrl.split('#')[0].replace(/[^/]+$/, '');
  for (const link of target.querySelectorAll<HTMLAnchorElement>('a[href]')) {
    const original = link.getAttribute('href') || '';
    const local = internalSourceLink(original, sourceUrl, language, mode);
    if (local) { link.href = local; link.removeAttribute('target'); continue; }
    try { link.href = new URL(original, sourceUrl).href; } catch { continue; }
    if (link.protocol === 'http:' || link.protocol === 'https:') { link.target = '_blank'; link.rel = 'noopener noreferrer'; }
  }
  for (const image of target.querySelectorAll<HTMLImageElement>('img[src]')) {
    const src = image.getAttribute('src') || '';
    try {
      const url = new URL(src, directory);
      const path = sourcePath(url);
      image.src = path ? REPO_RAW + path : url.href;
    } catch { /* Keep sanitized source. */ }
    image.loading = 'lazy';
  }
  const diagrams = target.querySelectorAll<HTMLElement>('pre code.language-mermaid');
  if (!diagrams.length) return;
  const mermaid = (await import('mermaid')).default;
  mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', flowchart: { htmlLabels: false }, themeVariables: { fontFamily: 'Titillium Web, sans-serif' }, theme: document.documentElement.dataset.theme === 'light' ? 'default' : 'dark' });
  for (const block of diagrams) {
    const parent = block.parentElement!; const code = block.textContent || '';
    const container = document.createElement('figure'); container.className = 'diagram';
    try {
      const rendered = await mermaid.render('mermaid-' + Math.random().toString(36).slice(2), code);
      const url = URL.createObjectURL(new Blob([rendered.svg], { type: 'image/svg+xml' }));
      const viewport = document.createElement('div'); viewport.className = 'diagram-viewport';
      const picture = document.createElement('img'); picture.src = url; picture.dataset.mermaidUrl = url; picture.alt = 'Technical diagram from this lesson';
      picture.addEventListener('load', () => {
        const ratio = picture.naturalWidth / picture.naturalHeight;
        if (ratio > 5) picture.classList.add('diagram-wide');
        if (ratio < .5) picture.classList.add('diagram-tall');
      }, { once: true });
      viewport.append(picture);
      const full = document.createElement('a'); full.href = url; full.target = '_blank'; full.rel = 'noopener noreferrer'; full.textContent = 'Open full diagram ↗';
      const source = document.createElement('details'); const summary = document.createElement('summary'); summary.textContent = 'View diagram source';
      const raw = document.createElement('pre'); raw.textContent = code; source.append(summary, raw);
      container.append(viewport, full, source); parent.replaceWith(container);
    } catch { /* Keep the original source when a diagram is invalid. */ }
  }
}

export const sourceUrlFor = (path: string) => REPO_VIEW + path;
