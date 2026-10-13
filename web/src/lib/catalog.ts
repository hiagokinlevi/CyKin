import catalogData from '../../public/catalog.json';

export type Edition = { authored_at_build: number; planned: number };
export type Course = {
  number: number;
  level: string;
  area: string;
  title: string;
  planned_chapters: number;
  instructional_weeks: number;
  study_days_per_week: number;
  daily_lesson_target: number;
  editions: Record<string, Edition>;
};
export type Catalog = {
  courses: Course[];
  level_order: string[];
  level_names: Record<string, Record<string, string>>;
  languages: string[];
};

export const catalog = catalogData as Catalog;
export const coursePath = (level: string, area: string) => `/courses/${level}/${area}/`;
export const levelPath = (level: string) => `/levels/${level}/`;
export const subjectPath = (area: string) => `/subjects/${area}/`;
export const subjects = catalog.courses.filter(course => course.level === catalog.level_order[0]);
