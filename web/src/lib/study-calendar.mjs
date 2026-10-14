/** Civil-date planning, not source authentication or learner completion.
 * Editorial responsibility: hiagokinlevi.
 * Weekly chapter/daily baselines come from the current catalog, not this module.
 */
export const MONTHS = Object.freeze({
  'rapid-1-month': 1, 'professional-6-months': 6,
  'technical-18-months': 18, 'technologist-3-years': 36,
  'bachelors-4-years': 48, 'engineering-5-years': 60,
  'postgraduate-2-years': 24, 'masters-2-years': 24,
  'doctorate-2-years': 24,
});
const DAY = 86400000;
const iso = value => value.toISOString().slice(0, 10);
const weekday = value => value.getUTCDay() !== 0 && value.getUTCDay() !== 6;
const next = value => new Date(value.getTime() + DAY);

function positiveInteger(value, name, maximum = 9999) {
  if (!Number.isInteger(value) || value < 1 || value > maximum) {
    throw new Error(`Invalid ${name}`);
  }
}

export function firstStudyDate(text) {
  if (typeof text !== 'string' || !/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(text)) {
    throw new Error('Use a YYYY-MM-DD start date');
  }
  let value = new Date(text + 'T00:00:00Z');
  if (!Number.isFinite(value.getTime()) || iso(value) !== text ||
      value.getUTCFullYear() < 1900 || value.getUTCFullYear() > 2090) {
    throw new Error('Use a valid date between 1900 and 2090');
  }
  while (!weekday(value)) value = next(value);
  return value;
}

export function calendarMonthEnd(first, months) {
  positiveInteger(months, 'duration', 120);
  const absoluteMonth = first.getUTCFullYear() * 12 + first.getUTCMonth() + months;
  const year = Math.floor(absoluteMonth / 12), month = absoluteMonth % 12;
  const lastDay = new Date(Date.UTC(year, month + 1, 0)).getUTCDate();
  return new Date(Date.UTC(year, month, Math.min(first.getUTCDate(), lastDay)));
}

/** API metadata only: a source-indexed lesson is not independently reviewed. */
export function dailyIndex(hasDailyLessons, lessons) {
  if (typeof hasDailyLessons !== 'boolean' || !Array.isArray(lessons)) {
    throw new Error('Invalid daily-source metadata');
  }
  const result = new Map();
  // Only explicit daily anchors or a source-marked chapter-lesson edition can set this flag.
  if (!hasDailyLessons) return result;
  for (const item of lessons) {
    if (!item || typeof item !== 'object') throw new Error('Invalid daily-source entry');
    positiveInteger(item.chapter, 'lesson ID');
    if (typeof item.published !== 'boolean' || typeof item.title !== 'string' || !item.title.trim()) {
      throw new Error('Invalid lesson title or publication flag');
    }
    if (result.has(item.chapter)) throw new Error('Duplicate daily lesson ID');
    result.set(item.chapter, { title: item.title, published: item.published });
  }
  return result;
}

/**
 * Keep every Monday-Friday date in the stated civil-month interval, and retain
 * extra indexed/baseline days after it. Never repeat, drop or renumber a lesson.
 * Missing source metadata means unknown, not zero authored content.
 */
export function buildCalendar({start, level, baseline, availabilityKnown = false,
                               hasDailyLessons = false, lessons = []}) {
  if (!Object.hasOwn(MONTHS, level)) throw new Error('Unknown level');
  positiveInteger(baseline, 'catalog baseline');
  if (typeof availabilityKnown !== 'boolean') throw new Error('Invalid availability state');
  const indexed = availabilityKnown ? dailyIndex(hasDailyLessons, lessons) : new Map();
  const first = firstStudyDate(start), end = calendarMonthEnd(first, MONTHS[level]);
  const periodDates = [];
  for (let cursor = first; cursor < end; cursor = next(cursor)) {
    if (weekday(cursor)) periodDates.push(iso(cursor));
  }
  const lastIndexed = indexed.size ? Math.max(...indexed.keys()) : 0;
  const sequenceLength = Math.max(baseline, lastIndexed);
  const total = Math.max(periodDates.length, sequenceLength);
  const monday = new Date(first.getTime() - ((first.getUTCDay() + 6) % 7) * DAY);
  const days = [];
  for (let cursor = first; days.length < total; cursor = next(cursor)) {
    if (!weekday(cursor)) continue;
    const ordinal = days.length + 1, record = indexed.get(ordinal);
    days.push({
      day: ordinal, date: iso(cursor),
      calendar_week: Math.floor((cursor.getTime() - monday.getTime()) / DAY / 7) + 1,
      weekday: cursor.getUTCDay(),
      // A calendar week starting Wednesday is not necessarily a book chapter.
      reference_study_week: Math.floor((ordinal - 1) / 5) + 1,
      within_nominal_period: cursor < end,
      beyond_baseline: ordinal > baseline,
      state: !availabilityKnown ? 'unknown' : !record ? 'unallocated' : record.published ? 'source_indexed' : 'planned',
      title: record?.title ?? null,
    });
  }
  return {
    level, months: MONTHS[level], requested_start: start,
    first_study_date: iso(first), end_exclusive: iso(end),
    baseline, nominal_weekdays: periodDates.length,
    baseline_difference: periodDates.length - baseline,
    sequence_length: sequenceLength, sequence_end: days[sequenceLength - 1].date,
    alignment: sequenceLength === periodDates.length ? 'date_counts_align' : 'allocation_review_required',
    availability_known: availabilityKnown,
    source_indexed_lessons: availabilityKnown ? [...indexed.values()].filter(x => x.published).length : null,
    first_unavailable_day: availabilityKnown ? (days.find(d => d.state !== 'source_indexed')?.day ?? null) : null,
    missing_within_nominal_period: availabilityKnown ? days.filter(d => d.within_nominal_period && d.state !== 'source_indexed').length : null,
    days,
  };
}
