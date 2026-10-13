"""Read-only daily planner contract tests. Synthetic fixtures, no production data."""
import copy
import importlib.util
import json
from datetime import date, timedelta
from pathlib import Path

import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

MODULE = Path(__file__).resolve().parents[1] / 'api' / 'daily_study.py'
spec = importlib.util.spec_from_file_location('daily_study', MODULE)
daily = importlib.util.module_from_spec(spec)
spec.loader.exec_module(daily)
ROOT = Path(__file__).resolve().parents[2]
POLICY = (ROOT / 'DAILY_STUDY_STANDARD.md').read_text()
LEVELS = daily.json_block(POLICY, 'daily-policy')['levels']
BOOK = '''# Test book
<a id="ch-01"></a>
## Chapter 1
### Foundations
Original synthetic teaching, not an operational incident finding.
#### Worked example
A recorded request does not prove that an operator performed it.
### Practice
#### EX001 — Independent task
Classify the specified request and identify the missing execution evidence.
<a id="answers"></a>
## Worked results
### EX001 — Worked result
A request is not an execution receipt; ask for the scoped operator record.
'''
PLAN = dict(schema=1, level='rapid-1-month', area='incident-response-resilience', language='en',
            state='mapped-draft', source_blob_sha=daily.git_blob_sha(BOOK), lessons=[dict(
                id='D0001', chapter=1, title='Separate request from execution',
                start='### Foundations', end='### Practice', example='#### Worked example',
                exercises=['EX001'])])


def block(value):
    return '<!-- cykin:daily-plan:start -->\n```json\n' + json.dumps(value) + '\n```\n<!-- cykin:daily-plan:end -->'


def parse(plan=None, book=BOOK):
    return daily.mapped_units(block(plan or PLAN), book, level=PLAN['level'], area=PLAN['area'], language='en', chapters=4)


@pytest.mark.parametrize('level', LEVELS)
def test_reference_formula(level):
    p = daily.policy_level(POLICY, level)
    assert p['reference_lessons'] == (p['months'] * 260 + 11) // 12


@pytest.mark.parametrize('start', ['2026-10-13', '2026-10-17', '2028-02-29', '2027-01-29', '2026-12-31'])
@pytest.mark.parametrize('level', LEVELS)
def test_calendar_independent_enumeration(start, level):
    p = LEVELS[level]
    result = daily.calendar_plan(start, p['months'], p['reference_lessons'])
    first, end = date.fromisoformat(result['first_study_date']), date.fromisoformat(result['period_end_exclusive'])
    count = sum((first + timedelta(days=n)).isoweekday() <= 5 for n in range((end-first).days))
    assert count == result['calendar_weekdays']
    dates = list(map(date.fromisoformat, result['dates']))
    assert len(dates) == p['reference_lessons'] == len(set(dates))
    assert dates == sorted(dates) and all(d.weekday() < 5 for d in dates)
    assert result['difference_days'] == count - len(dates)
    assert (result['alignment'] == 'aligned') == (count == len(dates))


@pytest.mark.parametrize('start', ['2026-02-30', '26-01-01', '2026-1-01', '2099-01-01', 'not-a-date'])
def test_bad_calendar(start):
    with pytest.raises(ValueError):
        daily.calendar_plan(start, 6, 130)


def test_clamp_and_weekend():
    assert daily.calendar_plan('2026-10-17', 1, 22)['first_study_date'] == '2026-10-19'
    assert daily.calendar_plan('2027-01-29', 1, 22)['period_end_exclusive'] == '2027-02-28'
    assert daily.calendar_plan('2028-02-29', 12, 260)['period_end_exclusive'] == '2029-02-28'
    assert daily.calendar_plan(None, 60, 1300)['alignment'] == 'undated'


def test_mapping_has_teaching_example_prompt_answer_and_revision():
    plan, units = parse()
    assert len(units) == 1 and units[0]['state'] == 'mapped-draft'
    assert 'Original synthetic teaching' in units[0]['markdown']
    assert 'operator performed' in units[0]['example']
    assert units[0]['exercises'][0]['id'] == 'EX001'
    assert 'ask for the scoped' in units[0]['exercises'][0]['answer']
    assert plan['source_blob_sha'] == daily.git_blob_sha(BOOK)


@pytest.mark.parametrize('change', [
    {'language': 'pt'}, {'area': 'different'}, {'source_blob_sha': '0'*40},
    {'state': 'complete'}, {'lessons': []}, {'schema': True},
])
def test_invalid_manifest(change):
    value = copy.deepcopy(PLAN); value.update(change)
    with pytest.raises(ValueError): parse(value)


@pytest.mark.parametrize('change', [
    {'id': 'D0002'}, {'chapter': True}, {'title': ''},
    {'start': '### Missing'}, {'end': '### Foundations'},
    {'example': '#### No example'}, {'exercises': []},
    {'exercises': ['EX001', 'EX001']}, {'exercises': ['EX0001']}, {'exercises': ['EX000']},
])
def test_invalid_daily_unit(change):
    value = copy.deepcopy(PLAN); value['lessons'][0].update(change)
    with pytest.raises(ValueError): parse(value)


@pytest.mark.parametrize('changed', [
    BOOK.replace('### EX001 — Worked result', '### EX002 — Worked result'),
    BOOK + '\n### Foundations\nDuplicate heading.\n',
    BOOK.replace('A request is not an execution receipt; ask for the scoped operator record.', ''),
    BOOK.replace('<a id="answers"></a>', ''),
    BOOK + '\n```python\n',
])
def test_source_defects_with_refreshed_fingerprint_still_block(changed):
    value = copy.deepcopy(PLAN); value['source_blob_sha'] = daily.git_blob_sha(changed)
    with pytest.raises(ValueError): parse(value, changed)


def test_fenced_heading_is_not_evidence():
    changed = BOOK.replace('Original synthetic teaching,', '```text\n### Foundations\n```\nOriginal synthetic teaching,')
    value = copy.deepcopy(PLAN); value['source_blob_sha'] = daily.git_blob_sha(changed)
    assert len(parse(value, changed)[1]) == 1


def test_four_digit_exercises_not_truncated():
    changed = BOOK.replace('EX001', 'EX1000')
    value = copy.deepcopy(PLAN); value['source_blob_sha'] = daily.git_blob_sha(changed)
    value['lessons'][0]['exercises'] = ['EX1000']
    assert parse(value, changed)[1][0]['exercises'][0]['id'] == 'EX1000'


def test_duplicate_json_key_rejected():
    text = block(PLAN).replace('"schema": 1', '"schema": 1, "schema": 1')
    with pytest.raises(ValueError): daily.json_block(text, 'daily-plan')


def client(sources=None, fail=False):
    app = FastAPI()
    async def catalog(request): return {}
    def get_course(data, level, area, language):
        if level not in LEVELS or area != 'incident-response-resilience' or language not in daily.LANGUAGES:
            raise HTTPException(404, 'Unknown course or language')
        return {}
    async def source_text(request, path):
        if fail: raise HTTPException(502, 'Upstream unavailable')
        if path == daily.POLICY_PATH: return POLICY
        return (sources or {}).get(path)
    daily.install_daily_routes(app, catalog=catalog, get_course=get_course, source_text=source_text)
    @app.get('/{path:path}')
    def fallback(path): return {'fallback': True}
    return TestClient(app)


BASE_URL = '/api/daily/rapid-1-month/incident-response-resilience/en'
SOURCES = {
    'levels/rapid-1-month/incident-response-resilience/en/DAILY_PLAN.md': block(PLAN),
    'levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md': BOOK,
}


@pytest.mark.parametrize('language', daily.LANGUAGES)
@pytest.mark.parametrize('level', LEVELS)
def test_all_level_language_combinations_remain_plans_without_manifests(level, language):
    response = client().get(f'/api/daily/{level}/incident-response-resilience/{language}')
    assert response.status_code == 200
    data = response.json()
    assert data['planned_daily_positions'] == LEVELS[level]['reference_lessons']
    assert data['mapped_draft_readings'] == data['native_daily_lessons'] == data['reviewed_daily_lessons'] == 0
    assert all(d['state'] == 'planned' and d['exercise_ids'] == [] for d in data['days'])


def test_api_mapping_navigation_and_partial_week():
    c = client(SOURCES)
    result = c.get(BASE_URL + '?start=2026-10-14').json()
    assert result['mapped_draft_readings'] == 1
    assert [d['study_day'] for d in result['days'][:4]] == [3, 4, 5, 1]
    assert result['days'][3]['week'] == 2
    lesson = c.get(BASE_URL + '/1')
    assert lesson.status_code == 200 and lesson.json()['next'] == 2 and lesson.json()['previous'] is None
    assert c.get(BASE_URL + '/2').status_code == 404
    assert c.get(BASE_URL + '/0').status_code == 404
    assert c.get(BASE_URL.replace('/en', '/pt') + '/1').status_code == 404
    assert c.get(BASE_URL + '?start=2026-02-30').status_code == 422


def test_source_change_blocks_available_day_without_fallback():
    sources = dict(SOURCES)
    sources['levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md'] += '\nSource changed.'
    c = client(sources)
    assert c.get(BASE_URL).json()['mapping_state'] == 'blocked'
    assert c.get(BASE_URL + '/1').status_code == 409


def test_network_error_not_zero_authored():
    assert client(fail=True).get(BASE_URL).status_code == 502


def test_unknown_language_and_course():
    c = client()
    assert c.get(BASE_URL.replace('/en', '/xx')).status_code == 404
    assert c.get(BASE_URL.replace('rapid-1-month', 'unknown')).status_code == 404


def test_public_ir_allocation_metadata_only():
    # Structural metadata test only: this does NOT inspect the complete source book.
    path = ROOT / 'levels/rapid-1-month/incident-response-resilience/en/DAILY_PLAN.md'
    plan = daily.json_block(path.read_text(), 'daily-plan')
    assert [d['id'] for d in plan['lessons']] == [f'D{n:04d}' for n in range(1, 23)]
    ids = [ex for d in plan['lessons'] for ex in d['exercises']]
    assert len(ids) == len(set(ids)) == 50
    assert set(ids) == {f'EX{n:03d}' for n in range(1, 51)}
