import test from 'node:test';
import assert from 'node:assert/strict';
import { buildCalendar, firstStudyDate, calendarMonthEnd, dailyIndex, MONTHS } from '../src/lib/study-calendar.mjs';

const BASELINES = [20, 130, 390, 780, 1040, 1300, 520, 520, 520];
const LEVELS = Object.keys(MONTHS);
const D = 86400000;
const source = (ids, published = true) => ids.map(chapter => ({chapter, title: `Synthetic ${chapter}`, published}));

// Independent reference uses weekday arithmetic over each civil date.
for (const [i, level] of LEVELS.entries()) {
  for (const start of ['2026-10-13','2026-10-17','2027-01-29','2028-02-29','2026-12-31']) {
    test(`${level}: weekday conservation from ${start}`, () => {
      const p = buildCalendar({start, level, baseline: BASELINES[i]});
      const first = Date.parse(p.first_study_date), end = Date.parse(p.end_exclusive);
      const expected = [];
      for (let t = first; t < end; t += D) {
        const day = ((Math.floor(t / D) + 3) % 7 + 7) % 7; // Monday=0
        if (day < 5) expected.push(new Date(t).toISOString().slice(0,10));
      }
      assert.deepEqual(p.days.filter(d=>d.within_nominal_period).map(d=>d.date), expected);
      assert.equal(p.nominal_weekdays, expected.length);
      assert.equal(new Set(p.days.map(d=>d.date)).size, p.days.length);
      assert.equal(p.baseline_difference, expected.length - BASELINES[i]);
      assert.ok(p.days.every(d=>d.weekday>=1&&d.weekday<=5));
      assert.deepEqual(p.days.map(d=>d.day), p.days.map((_,n)=>n+1));
      assert.equal(p.source_indexed_lessons, null);
      assert.ok(p.days.every(d=>d.state==='unknown'));
    });
  }
}

test('weekend starts Monday; month and leap-day anniversaries clamp explicitly',()=>{
  assert.equal(firstStudyDate('2026-10-17').toISOString().slice(0,10),'2026-10-19');
  assert.equal(calendarMonthEnd(firstStudyDate('2027-01-29'),1).toISOString().slice(0,10),'2027-02-28');
  assert.equal(calendarMonthEnd(firstStudyDate('2028-02-29'),12).toISOString().slice(0,10),'2029-02-28');
});

test('20 instructional days do not silently fill an actual calendar month',()=>{
  const p=buildCalendar({start:'2026-10-13',level:LEVELS[0],baseline:20,availabilityKnown:true,hasDailyLessons:true,lessons:source(Array.from({length:20},(_,n)=>n+1))});
  assert.equal(p.nominal_weekdays,23);
  assert.equal(p.days.length,23);
  assert.equal(p.source_indexed_lessons,20);
  assert.equal(p.missing_within_nominal_period,3);
  assert.equal(p.first_unavailable_day,21);
  assert.equal(p.days[20].state,'unallocated');
});

test('missing lesson 2 is a gap, not a reason to move lesson 3 to day 2',()=>{
  const p=buildCalendar({start:'2026-10-14',level:LEVELS[0],baseline:20,availabilityKnown:true,hasDailyLessons:true,lessons:source([3,1])});
  assert.equal(p.days[1].state,'unallocated');
  assert.equal(p.days[2].title,'Synthetic 3');
  assert.equal(p.first_unavailable_day,2);
  assert.deepEqual(p.days.slice(0,4).map(d=>d.weekday),[3,4,5,1]);
  assert.equal(p.days[3].calendar_week,2);
  assert.equal(p.days[3].reference_study_week,1);
});

test('extra authored/indexed positions remain after the nominal end',()=>{
  const p=buildCalendar({start:'2026-10-13',level:LEVELS[0],baseline:20,availabilityKnown:true,hasDailyLessons:true,lessons:source([1,25])});
  assert.equal(p.days.length,25);
  assert.equal(p.days[24].within_nominal_period,false);
  assert.equal(p.days[24].state,'source_indexed');
  assert.equal(p.alignment,'allocation_review_required');
});

test('legacy chapters are not daily lessons and planned teaching is not available',()=>{
  assert.equal(dailyIndex(false,source([1,2,3,4])).size,0);
  const p=buildCalendar({start:'2026-10-13',level:LEVELS[0],baseline:20,availabilityKnown:true,hasDailyLessons:true,lessons:source([1],false)});
  assert.equal(p.days[0].state,'planned');
  assert.equal(p.source_indexed_lessons,0);
});

for (const start of ['2026-02-30','2026-2-01','bad','2028-13-01','1899-01-01','2091-01-01','2026-10-13T00:00Z']) {
  test(`reject invalid start ${start}`,()=>assert.throws(()=>buildCalendar({start,level:LEVELS[0],baseline:20})));
}
for (const baseline of [0,-1,2.5,'20',true,10000,NaN]) {
  test(`reject invalid baseline ${String(baseline)}`,()=>assert.throws(()=>buildCalendar({start:'2026-10-13',level:LEVELS[0],baseline})));
}
for (const entries of [source([1,1]),source([0]),source([1.5]),source([10000]),[{chapter:1,title:'',published:true}],[{chapter:1,title:'Bad flag',published:'false'}]]) {
  test(`reject malformed source index ${JSON.stringify(entries)}`,()=>assert.throws(()=>dailyIndex(true,entries)));
}

test('unknown level and missing API evidence never imply zero authored lessons',()=>{
  assert.throws(()=>buildCalendar({start:'2026-10-13',level:'not-a-level',baseline:20}));
  const p=buildCalendar({start:'2026-10-13',level:LEVELS[0],baseline:20});
  assert.equal(p.first_unavailable_day,null);
  assert.equal(p.missing_within_nominal_period,null);
});

test('long books retain lesson 1000 and reject an unknown Boolean type',()=>{
  const p=buildCalendar({start:'2026-10-13',level:'engineering-5-years',baseline:1300,availabilityKnown:true,hasDailyLessons:true,lessons:source([1,1000,1300])});
  assert.equal(p.days[999].title,'Synthetic 1000');
  assert.throws(()=>dailyIndex('true',source([1])));
  assert.throws(()=>buildCalendar({start:'2026-10-13',level:LEVELS[0],baseline:20,availabilityKnown:'false'}));
});
