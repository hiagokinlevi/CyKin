import type { Catalog, Course } from './catalog';
import { editionLanguage, siteLanguage, ui } from './i18n';

export function initializeCourseMenus(): void {
  const menus = [...document.querySelectorAll<HTMLDetailsElement>('.catalog-menu')];
  let catalogPromise: Promise<Catalog> | null = null;
  const catalog = () => catalogPromise ||= fetch('/api/catalog').then(response => {
    if (!response.ok) throw new Error('Catalog unavailable');
    return response.json() as Promise<Catalog>;
  });

  for (const menu of menus) {
    menu.addEventListener('toggle', async () => {
      if (!menu.open) return;
      for (const other of menus) if (other !== menu) other.open = false;
      const choices = menu.querySelector<HTMLElement>('.catalog-menu-choices')!;
      const results = menu.querySelector<HTMLElement>('.catalog-menu-courses')!;
      if (choices.childElementCount) return;
      try {
        const data = await catalog();
        if (!menu.open) return;
        const mode = menu.dataset.mode;
        const options = mode === 'level'
          ? data.level_order.map(key => ({ key, label: data.level_names[key][siteLanguage()] || data.level_names[key].en }))
          : data.courses.filter(course => course.level === data.level_order[0]).map(course => ({ key: course.area, label: ui(course.title) }));
        const courseRoute = location.pathname.match(/^\/courses\/([^/]+)\/([^/]+)\//);
        const directoryRoute = location.pathname.match(mode === 'level' ? /^\/levels\/([^/]+)\// : /^\/subjects\/([^/]+)\//);
        const currentKey = courseRoute ? courseRoute[mode === 'level' ? 1 : 2] : directoryRoute?.[1];
        const selectedIndex = Math.max(0, options.findIndex(option => option.key === currentKey));
        const renderCourses = (key: string) => {
          results.replaceChildren();
          const directory = document.createElement('a');
          directory.className = 'catalog-menu-directory';
          directory.href = `${mode === 'level' ? '/levels/' : '/subjects/'}${key}/?lang=${editionLanguage()}&ui=${siteLanguage()}`;
          directory.textContent = ui('View this group →');
          results.append(directory);
          const courses: Course[] = data.courses.filter(course => mode === 'level' ? course.level === key : course.area === key);
          for (const course of courses) {
            const item = document.createElement('a'); item.className = 'catalog-menu-course';
            item.href = `/courses/${course.level}/${course.area}/?lang=${editionLanguage()}&ui=${siteLanguage()}`;
            const number = document.createElement('span'); number.textContent = String(course.number).padStart(3, '0');
            const label = document.createElement('span'); label.textContent = mode === 'level' ? ui(course.title) : data.level_names[course.level][siteLanguage()] || data.level_names[course.level].en;
            item.append(number, label); results.append(item);
          }
        };
        options.forEach(({ key, label }, index) => {
          const button = document.createElement('button'); button.type = 'button'; button.textContent = label;
          button.setAttribute('aria-pressed', index === selectedIndex ? 'true' : 'false');
          button.addEventListener('click', () => {
            for (const sibling of choices.querySelectorAll('button')) sibling.setAttribute('aria-pressed', sibling === button ? 'true' : 'false');
            renderCourses(key);
          });
          choices.append(button);
        });
        if (options[selectedIndex]) renderCourses(options[selectedIndex].key);
      } catch { results.textContent = ui('The catalog is temporarily unavailable.'); }
    });
  }
  document.addEventListener('keydown', event => { if (event.key === 'Escape') for (const menu of menus) menu.open = false; });
  document.addEventListener('click', event => {
    const target = event.target as Node;
    if (!menus.some(menu => menu.contains(target))) for (const menu of menus) menu.open = false;
  });
}
