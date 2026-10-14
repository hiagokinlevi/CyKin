"""The public course route must never confuse an outline with a lesson."""

import json
import hashlib
import html
import re
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import app, chapter_sections, worked_answers


ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def client():
    app.state.catalog_override = json.loads((ROOT / "web/public/catalog.json").read_text())

    async def local_source(path):
        target = ROOT / path
        return target.read_text(encoding="utf-8") if target.is_file() else None

    app.state.source_override = local_source
    try:
        yield TestClient(app)
    finally:
        del app.state.catalog_override
        del app.state.source_override


def test_public_guide_and_lesson(client):
    catalog = client.get("/api/catalog")
    assert catalog.status_code == 200
    assert len(catalog.json()["courses"]) == 207
    rapid = next(course for course in catalog.json()["courses"] if course["level"] == "rapid-1-month")
    engineering = next(course for course in catalog.json()["courses"] if course["level"] == "engineering-5-years")
    assert (rapid["instructional_weeks"], rapid["daily_lesson_target"]) == (4, 20)
    assert (engineering["instructional_weeks"], engineering["daily_lesson_target"]) == (260, 1300)
    assert "minimum_a4_pages" not in rapid
    assert "minimum_exercises" not in rapid

    guide = client.get("/api/courses/rapid-1-month/incident-response-resilience/en")
    assert guide.status_code == 200
    assert guide.json()["planned_chapters"] == 4
    assert guide.json()["published_chapters"] == 4
    assert guide.json()["planned_lessons"] == guide.json()["published_lessons"] == 20
    assert [lesson["chapter"] for lesson in guide.json()["lessons"]] == list(range(1, 21))
    assert [(module["kind"], module["number"], module["chapters"]) for module in guide.json()["modules"]] == [
        ("Chapter", number, list(range((number - 1) * 5 + 1, number * 5 + 1))) for number in range(1, 5)
    ]
    assert guide.json()["lessons"][0]["subject"] == "Incident readiness, roles and authorized scope"
    assert guide.json()["daily_schedule_ready"] is True
    assert len(guide.json()["legacy_chapters"]) == 4
    assert guide.json()["legacy_chapters"][0]["published"] is True

    lesson = client.get("/api/lessons/rapid-1-month/incident-response-resilience/en/1")
    assert lesson.status_code == 200
    assert lesson.json()["title"] == "Evidence readiness and the first case question"
    assert lesson.json()["next"] == 2
    assert lesson.json()["week_chapter"] == 1
    assert lesson.json()["exercise_ids"] == ["001"]
    assert "EX001" in lesson.json()["worked_answers"]
    assert "EX002" not in lesson.json()["worked_answers"]
    assert "W1-R1 — Worked answer" in lesson.json()["worked_answers"]
    assert "W1-R2 — Worked answer" not in lesson.json()["worked_answers"]
    second = client.get("/api/lessons/rapid-1-month/incident-response-resilience/en/2").json()
    assert "W1-R2 — Worked answer" in second["worked_answers"]
    assert client.get("/api/chapters/rapid-1-month/incident-response-resilience/en/1").status_code == 200


def test_unwritten_chapter_is_not_served_as_lesson(client):
    guide = client.get("/api/courses/rapid-1-month/cybersecurity/en").json()
    assert guide["planned_chapters"] == 20
    assert guide["published_chapters"] == 20
    assert guide["lessons"][3]["published"] is True
    assert guide["lessons"][11]["published"] is True
    assert guide["lessons"][19]["published"] is True
    missing = client.get("/api/lessons/rapid-1-month/cybersecurity/en/21")
    assert missing.status_code == 404
    assert missing.json()["detail"] == "This chapter is still a plan"

    info = client.get("/api/courses/rapid-1-month/information-security/en").json()
    assert info["planned_chapters"] == 20
    assert info["published_chapters"] == 20
    assert info["lessons"][8]["published"] is True
    assert info["lessons"][19]["published"] is True
    missing_info = client.get("/api/lessons/rapid-1-month/information-security/en/21")
    assert missing_info.status_code == 404
    assert missing_info.json()["detail"] == "This chapter is still a plan"

    governance = client.get("/api/courses/rapid-1-month/data-governance/en").json()
    assert governance["planned_chapters"] == 20
    assert governance["published_chapters"] == 20
    assert governance["lessons"][4]["published"] is True
    assert governance["lessons"][19]["published"] is True
    missing_governance = client.get("/api/lessons/rapid-1-month/data-governance/en/21")
    assert missing_governance.status_code == 404
    assert missing_governance.json()["detail"] == "This chapter is still a plan"

    privacy = client.get("/api/courses/rapid-1-month/privacy-data-protection/en").json()
    assert privacy["planned_chapters"] == 20
    assert privacy["published_chapters"] == 20
    assert privacy["lessons"][4]["published"] is True
    assert privacy["lessons"][19]["published"] is True
    missing_privacy = client.get("/api/lessons/rapid-1-month/privacy-data-protection/en/21")
    assert missing_privacy.status_code == 404
    assert missing_privacy.json()["detail"] == "This chapter is still a plan"

    grc = client.get("/api/courses/rapid-1-month/security-governance-risk-compliance/en").json()
    assert grc["planned_chapters"] == 20
    assert grc["published_chapters"] == 20
    assert grc["lessons"][4]["published"] is True
    assert grc["lessons"][19]["published"] is True
    assert grc["lessons"][19]["title"] == "What the strategy page can say"
    missing_grc = client.get("/api/lessons/rapid-1-month/security-governance-risk-compliance/en/21")
    assert missing_grc.status_code == 404
    assert missing_grc.json()["detail"] == "This chapter is still a plan"

    human = client.get("/api/courses/rapid-1-month/human-factors-policy/en").json()
    assert human["planned_chapters"] == 20
    assert human["published_chapters"] == 20
    assert human["lessons"][4]["published"] is True
    assert human["lessons"][19]["published"] is True
    assert human["lessons"][19]["title"] == "What the charity note can say"
    missing_human = client.get("/api/lessons/rapid-1-month/human-factors-policy/en/21")
    assert missing_human.status_code == 404
    assert missing_human.json()["detail"] == "This chapter is still a plan"

    architecture = client.get("/api/courses/rapid-1-month/security-architecture/en").json()
    assert architecture["planned_chapters"] == 20
    assert architecture["published_chapters"] == 20
    assert architecture["lessons"][4]["published"] is True
    assert architecture["lessons"][19]["published"] is True
    assert architecture["lessons"][19]["title"] == "What the architecture note can say"
    missing_architecture = client.get("/api/lessons/rapid-1-month/security-architecture/en/21")
    assert missing_architecture.status_code == 404
    assert missing_architecture.json()["detail"] == "This chapter is still a plan"

    cryptography = client.get("/api/courses/rapid-1-month/cryptography-trust/en").json()
    assert cryptography["planned_chapters"] == 20
    assert cryptography["published_chapters"] == 20
    assert cryptography["lessons"][4]["published"] is True
    assert cryptography["lessons"][19]["published"] is True
    assert cryptography["lessons"][19]["title"] == "What the library note can say"
    missing_cryptography = client.get("/api/lessons/rapid-1-month/cryptography-trust/en/21")
    assert missing_cryptography.status_code == 404
    assert missing_cryptography.json()["detail"] == "This chapter is still a plan"

    web3 = client.get("/api/courses/rapid-1-month/web3-blockchain-security/en").json()
    assert web3["planned_chapters"] == 20
    assert web3["published_chapters"] == 20
    assert web3["lessons"][4]["published"] is True
    assert web3["lessons"][19]["published"] is True
    assert web3["lessons"][19]["title"] == "What the loyalty note can say"
    missing_web3 = client.get("/api/lessons/rapid-1-month/web3-blockchain-security/en/21")
    assert missing_web3.status_code == 404
    assert missing_web3.json()["detail"] == "This chapter is still a plan"
    portuguese_web3 = client.get("/api/lessons/rapid-1-month/web3-blockchain-security/pt/1")
    assert portuguese_web3.status_code == 404
    assert portuguese_web3.json()["detail"] == "This edition has no authored manuscript yet"

    identity = client.get("/api/courses/rapid-1-month/identity-access/en").json()
    assert identity["planned_chapters"] == 20
    assert identity["published_chapters"] == 20
    assert identity["lessons"][4]["published"] is True
    assert identity["lessons"][19]["published"] is True
    assert identity["lessons"][19]["title"] == "What the florist note can say"
    missing_identity = client.get("/api/lessons/rapid-1-month/identity-access/en/21")
    assert missing_identity.status_code == 404
    assert missing_identity.json()["detail"] == "This chapter is still a plan"
    portuguese_identity = client.get("/api/lessons/rapid-1-month/identity-access/pt/1")
    assert portuguese_identity.status_code == 404
    assert portuguese_identity.json()["detail"] == "This edition has no authored manuscript yet"

    network = client.get("/api/courses/rapid-1-month/network-communications/en").json()
    assert network["planned_chapters"] == 20
    assert network["published_chapters"] == 20
    assert network["lessons"][4]["published"] is True
    assert network["lessons"][19]["published"] is True
    assert network["lessons"][19]["title"] == "What the bakery note can say"
    missing_network = client.get("/api/lessons/rapid-1-month/network-communications/en/21")
    assert missing_network.status_code == 404
    assert missing_network.json()["detail"] == "This chapter is still a plan"
    portuguese_network = client.get("/api/lessons/rapid-1-month/network-communications/pt/1")
    assert portuguese_network.status_code == 404
    assert portuguese_network.json()["detail"] == "This edition has no authored manuscript yet"

    systems = client.get("/api/courses/rapid-1-month/systems-endpoints-hardware/en").json()
    assert systems["planned_chapters"] == 20
    assert systems["published_chapters"] == 20
    assert systems["lessons"][4]["published"] is True
    assert systems["lessons"][19]["published"] is True
    assert systems["lessons"][19]["title"] == "What the food-bank note can say"
    missing_systems = client.get("/api/lessons/rapid-1-month/systems-endpoints-hardware/en/21")
    assert missing_systems.status_code == 404
    assert missing_systems.json()["detail"] == "This chapter is still a plan"
    portuguese_systems = client.get("/api/lessons/rapid-1-month/systems-endpoints-hardware/pt/1")
    assert portuguese_systems.status_code == 404
    assert portuguese_systems.json()["detail"] == "This edition has no authored manuscript yet"

    cloud = client.get("/api/courses/rapid-1-month/cloud-containers/en").json()
    assert cloud["planned_chapters"] == 20
    assert cloud["published_chapters"] == 20
    assert cloud["lessons"][4]["published"] is True
    assert cloud["lessons"][19]["published"] is True
    assert cloud["lessons"][19]["title"] == "What the clinic note can say"
    missing_cloud = client.get("/api/lessons/rapid-1-month/cloud-containers/en/21")
    assert missing_cloud.status_code == 404
    assert missing_cloud.json()["detail"] == "This chapter is still a plan"
    portuguese_cloud = client.get("/api/lessons/rapid-1-month/cloud-containers/pt/1")
    assert portuguese_cloud.status_code == 404
    assert portuguese_cloud.json()["detail"] == "This edition has no authored manuscript yet"

    supply = client.get("/api/courses/rapid-1-month/application-supply-chain/en").json()
    assert supply["planned_chapters"] == 20
    assert supply["published_chapters"] == 20
    assert supply["lessons"][4]["published"] is True
    assert supply["lessons"][19]["published"] is True
    assert supply["lessons"][19]["title"] == "What the charity note can say"
    missing_supply = client.get("/api/lessons/rapid-1-month/application-supply-chain/en/21")
    assert missing_supply.status_code == 404
    assert missing_supply.json()["detail"] == "This chapter is still a plan"
    portuguese_supply = client.get("/api/lessons/rapid-1-month/application-supply-chain/pt/1")
    assert portuguese_supply.status_code == 404
    assert portuguese_supply.json()["detail"] == "This edition has no authored manuscript yet"

    operations = client.get("/api/courses/rapid-1-month/security-operations-blue-team/en").json()
    assert operations["planned_chapters"] == 20
    assert operations["published_chapters"] == 20
    assert operations["lessons"][4]["published"] is True
    assert operations["lessons"][19]["published"] is True
    assert operations["lessons"][19]["title"] == "What the firm note can say"
    missing_operations = client.get("/api/lessons/rapid-1-month/security-operations-blue-team/en/21")
    assert missing_operations.status_code == 404
    assert missing_operations.json()["detail"] == "This chapter is still a plan"
    portuguese_operations = client.get("/api/lessons/rapid-1-month/security-operations-blue-team/pt/1")
    assert portuguese_operations.status_code == 404
    assert portuguese_operations.json()["detail"] == "This edition has no authored manuscript yet"

    forensics = client.get("/api/courses/rapid-1-month/digital-forensics-malware/en").json()
    assert forensics["planned_chapters"] == 20
    assert forensics["published_chapters"] == 20
    assert forensics["lessons"][4]["published"] is True
    assert forensics["lessons"][19]["published"] is True
    assert forensics["lessons"][19]["title"] == "What the food bank note can say"
    missing_forensics = client.get("/api/lessons/rapid-1-month/digital-forensics-malware/en/21")
    assert missing_forensics.status_code == 404
    assert missing_forensics.json()["detail"] == "This chapter is still a plan"
    portuguese_forensics = client.get("/api/courses/rapid-1-month/digital-forensics-malware/pt").json()
    assert portuguese_forensics["published_chapters"] == 4
    portuguese_forensics_lesson = client.get("/api/lessons/rapid-1-month/digital-forensics-malware/pt/1")
    assert portuguese_forensics_lesson.status_code == 200

    intelligence = client.get("/api/courses/rapid-1-month/threat-intelligence-osint/en").json()
    assert intelligence["planned_chapters"] == 20
    assert intelligence["published_chapters"] == 20
    assert intelligence["lessons"][4]["published"] is True
    assert intelligence["lessons"][19]["published"] is True
    assert intelligence["lessons"][19]["title"] == "What the Elmfield note can say"
    missing_intelligence = client.get("/api/lessons/rapid-1-month/threat-intelligence-osint/en/21")
    assert missing_intelligence.status_code == 404
    assert missing_intelligence.json()["detail"] == "This chapter is still a plan"
    portuguese_intelligence = client.get("/api/lessons/rapid-1-month/threat-intelligence-osint/pt/1")
    assert portuguese_intelligence.status_code == 404
    assert portuguese_intelligence.json()["detail"] == "This edition has no authored manuscript yet"

    offensive = client.get("/api/courses/rapid-1-month/offensive-security-red-team/en").json()
    assert offensive["planned_chapters"] == 20
    assert offensive["published_chapters"] == 20
    assert offensive["lessons"][4]["published"] is True
    assert offensive["lessons"][19]["published"] is True
    assert offensive["lessons"][19]["title"] == "What the college note can say"
    missing_offensive = client.get("/api/lessons/rapid-1-month/offensive-security-red-team/en/21")
    assert missing_offensive.status_code == 404
    assert missing_offensive.json()["detail"] == "This chapter is still a plan"
    portuguese_offensive = client.get("/api/courses/rapid-1-month/offensive-security-red-team/pt").json()
    assert portuguese_offensive["published_chapters"] == 4
    portuguese_offensive_lesson = client.get("/api/lessons/rapid-1-month/offensive-security-red-team/pt/1")
    assert portuguese_offensive_lesson.status_code == 200

    ai_security = client.get("/api/courses/rapid-1-month/ai-security/en").json()
    assert ai_security["planned_chapters"] == 20
    assert ai_security["published_chapters"] == 20
    assert ai_security["lessons"][4]["published"] is True
    assert ai_security["lessons"][19]["published"] is True
    assert ai_security["lessons"][19]["title"] == "What the Tallis note can say"
    missing_ai = client.get("/api/lessons/rapid-1-month/ai-security/en/21")
    assert missing_ai.status_code == 404
    assert missing_ai.json()["detail"] == "This chapter is still a plan"
    portuguese_ai = client.get("/api/courses/rapid-1-month/ai-security/pt").json()
    assert portuguese_ai["published_chapters"] == 4
    portuguese_ai_lesson = client.get("/api/lessons/rapid-1-month/ai-security/pt/1")
    assert portuguese_ai_lesson.status_code == 200
    assert portuguese_ai["book_url"] is not None
    assert portuguese_ai["chapter_lessons"] is False


def test_information_security_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/information-security/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the month's log can say"
    assert guide['lessons'][19]['title'] == "What the month's log can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/information-security/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/information-security/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/information-security/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/information-security/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex074"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/information-security/pt').json()
    assert portuguese['chapter_lessons'] is True
    assert portuguese['published_lessons'] == portuguese['published_chapters'] == 20
    assert portuguese['lessons'][19]['title'] == "O que o registro do mês pode afirmar"


def test_data_governance_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/data-governance/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the notebook can say"
    assert guide['lessons'][19]['title'] == "What the notebook can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/data-governance/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/data-governance/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/data-governance/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/data-governance/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex074"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/data-governance/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0


def test_privacy_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/privacy-data-protection/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the review file can say"
    assert guide['lessons'][19]['title'] == "What the review file can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/privacy-data-protection/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/privacy-data-protection/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/privacy-data-protection/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/privacy-data-protection/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex074"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/privacy-data-protection/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0


def test_grc_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/security-governance-risk-compliance/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the strategy page can say"
    assert guide['lessons'][19]['title'] == "What the strategy page can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/security-governance-risk-compliance/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/security-governance-risk-compliance/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/security-governance-risk-compliance/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/security-governance-risk-compliance/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex074"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/security-governance-risk-compliance/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 4


def test_human_factors_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/human-factors-policy/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the charity note can say"
    assert guide['lessons'][19]['title'] == "What the charity note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/human-factors-policy/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/human-factors-policy/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/human-factors-policy/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/human-factors-policy/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/human-factors-policy/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 4


def test_security_architecture_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/security-architecture/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the architecture note can say"
    assert guide['lessons'][19]['title'] == "What the architecture note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/security-architecture/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/security-architecture/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/security-architecture/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/security-architecture/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/security-architecture/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 4


def test_cryptography_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/cryptography-trust/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the library note can say"
    assert guide['lessons'][19]['title'] == "What the library note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/cryptography-trust/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/cryptography-trust/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/cryptography-trust/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/cryptography-trust/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/cryptography-trust/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 4


def test_web3_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/web3-blockchain-security/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the loyalty note can say"
    assert guide['lessons'][19]['title'] == "What the loyalty note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/web3-blockchain-security/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/web3-blockchain-security/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/web3-blockchain-security/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/web3-blockchain-security/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/web3-blockchain-security/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 0
    assert portuguese['book_url'] is None


def test_identity_access_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/identity-access/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the florist note can say"
    assert guide['lessons'][19]['title'] == "What the florist note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/identity-access/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/identity-access/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/identity-access/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/identity-access/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/identity-access/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 0
    assert portuguese['book_url'] is None


def test_network_communications_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/network-communications/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the bakery note can say"
    assert guide['lessons'][19]['title'] == "What the bakery note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/network-communications/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/network-communications/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/network-communications/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/network-communications/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/network-communications/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 0
    assert portuguese['book_url'] is None


def test_systems_endpoints_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/systems-endpoints-hardware/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the food-bank note can say"
    assert guide['lessons'][19]['title'] == "What the food-bank note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/systems-endpoints-hardware/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/systems-endpoints-hardware/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/systems-endpoints-hardware/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/systems-endpoints-hardware/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/systems-endpoints-hardware/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 0
    assert portuguese['book_url'] is None


def test_cloud_containers_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/cloud-containers/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the clinic note can say"
    assert guide['lessons'][19]['title'] == "What the clinic note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/cloud-containers/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/cloud-containers/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/cloud-containers/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/cloud-containers/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/cloud-containers/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 0
    assert portuguese['book_url'] is None


def test_application_supply_chain_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/application-supply-chain/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the charity note can say"
    assert guide['lessons'][19]['title'] == "What the charity note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/application-supply-chain/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/application-supply-chain/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/application-supply-chain/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/application-supply-chain/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/application-supply-chain/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 0
    assert portuguese['book_url'] is None


def test_security_operations_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/security-operations-blue-team/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the firm note can say"
    assert guide['lessons'][19]['title'] == "What the firm note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/security-operations-blue-team/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/security-operations-blue-team/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/security-operations-blue-team/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/security-operations-blue-team/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/security-operations-blue-team/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 0
    assert portuguese['book_url'] is None


def test_digital_forensics_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/digital-forensics-malware/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the food bank note can say"
    assert guide['lessons'][19]['title'] == "What the food bank note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/digital-forensics-malware/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/digital-forensics-malware/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/digital-forensics-malware/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/digital-forensics-malware/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/digital-forensics-malware/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 4
    assert portuguese['book_url'] is not None


def test_threat_intelligence_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/threat-intelligence-osint/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the Elmfield note can say"
    assert guide['lessons'][19]['title'] == "What the Elmfield note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/threat-intelligence-osint/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/threat-intelligence-osint/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/threat-intelligence-osint/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/threat-intelligence-osint/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/threat-intelligence-osint/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 0
    assert portuguese['book_url'] is None


def test_offensive_security_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/offensive-security-red-team/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the college note can say"
    assert guide['lessons'][19]['title'] == "What the college note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/offensive-security-red-team/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/offensive-security-red-team/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/offensive-security-red-team/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/offensive-security-red-team/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/offensive-security-red-team/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 4
    assert portuguese['book_url'] is not None


def test_ai_security_chapter_lessons_use_one_canonical_page_each(client):
    guide = client.get('/api/courses/rapid-1-month/ai-security/en').json()
    assert guide['chapter_lessons'] is True
    assert guide['has_daily_lessons'] is True
    assert guide['daily_schedule_ready'] is True
    assert guide['published_lessons'] == guide['published_chapters'] == 20
    assert len(guide['daily_slots']) == 20
    assert [entry['module'] for entry in guide['daily_slots']] == [week for week in range(1, 5) for _ in range(5)]
    assert all(entry['published'] for entry in guide['daily_slots'])
    assert [module['chapters'] for module in guide['modules']] == [list(range(first, first + 5)) for first in (1, 6, 11, 16)]
    assert guide['daily_slots'][19]['source_url'].endswith('#ch-20')
    assert guide['daily_slots'][19]['title'] == "What the Tallis note can say"
    assert guide['lessons'][19]['title'] == "What the Tallis note can say"

    for number in range(1, 21):
        unit = client.get(f'/api/lessons/rapid-1-month/ai-security/en/{number}').json()
        assert unit['exercise_ids']
        assert {f'<a id="answer-ex{digits}"></a>' for digits in unit['exercise_ids']} <= set(
            re.findall(r'<a id="answer-ex\d{3,4}"></a>', unit['worked_answers'])
        )

    lesson = client.get('/api/lessons/rapid-1-month/ai-security/en/20').json()
    assert lesson['content_kind'] == 'chapter_lesson'
    assert lesson['source_url'].endswith('#ch-20')
    assert lesson['worked_answers']
    canonical = client.get('/courses/rapid-1-month/ai-security/lessons/en/20/', follow_redirects=False)
    assert canonical.status_code == 308
    assert canonical.headers['location'] == '/courses/rapid-1-month/ai-security/chapters/en/20/'
    page = client.get(canonical.headers['location'])
    assert page.status_code == 200
    assert 'Lesson 20' in page.text
    assert f"<h1 id=\"ch-20\">{html.escape(guide['lessons'][19]['title'])}</h1>" in page.text
    assert 'id="answer-ex066"' in page.text

    portuguese = client.get('/api/courses/rapid-1-month/ai-security/pt').json()
    assert portuguese['chapter_lessons'] is False
    assert portuguese['published_lessons'] == 0
    assert portuguese['published_chapters'] == 4
    assert portuguese['book_url'] is not None


def test_full_book_and_internal_reference_source(client):
    book = client.get('/api/books/rapid-1-month/incident-response-resilience/en')
    assert book.status_code == 200
    assert '<a id="ch-01"></a>' in book.text
    assert '<a id="answers"></a>' in book.text
    assert book.headers['x-opencyberacademy-source-sha256'] == hashlib.sha256(book.content).hexdigest()

    plan = client.get('/api/source', params={
        'path': 'levels/rapid-1-month/incident-response-resilience/en/book/PLAN.md',
    })
    assert plan.status_code == 200
    assert '<a id="ch-01"></a>' in plan.text
    for forbidden in ('../README.md', '/README.md', 'levels//README.md', 'missing.md'):
        assert client.get('/api/source', params={'path': forbidden}).status_code == 404


def test_stateless_mcp_public_and_progress_private(client):
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    initialize = client.post("/mcp", headers=headers, json={"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
    assert initialize.status_code == 200
    assert initialize.json()["result"]["protocolVersion"] == "2025-06-18"
    tools = client.post("/mcp", headers=headers, json={"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    assert {"get_editorial_policy", "list_courses", "list_lessons", "read_lesson", "read_chapter", "search_course",
            "student_sign_in", "student_read_lesson", "student_get_stats", "student_get_progress",
            "student_save_analysis", "student_save_lesson", "student_save_exercise"} <= {
                tool["name"] for tool in tools.json()["result"]["tools"]}
    resources = client.post("/mcp", headers=headers, json={"jsonrpc": "2.0", "id": 4, "method": "resources/list"})
    assert "open-cyber-academy://editorial-policy" in {item["uri"] for item in resources.json()["result"]["resources"]}
    policy = client.post("/mcp", headers=headers, json={"jsonrpc": "2.0", "id": 5, "method": "resources/read", "params": {"uri": "open-cyber-academy://editorial-policy"}})
    assert "all 207 course editions" in policy.json()["result"]["contents"][0]["text"]
    policy_tool = client.post("/mcp", headers=headers, json={"jsonrpc": "2.0", "id": 6, "method": "tools/call", "params": {"name": "get_editorial_policy", "arguments": {}}})
    assert "English → Portuguese → Spanish" in json.loads(policy_tool.json()["result"]["content"][0]["text"])["markdown"]
    lesson = client.post("/mcp", headers=headers, json={"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "read_lesson", "arguments": {"level": "rapid-1-month", "area": "incident-response-resilience", "language": "en", "chapter": 1}}})
    mcp_lesson = json.loads(lesson.json()["result"]["content"][0]["text"])
    assert "W1-R1 — Worked answer" in mcp_lesson["worked_answers"]
    assert "W1-R2 — Worked answer" not in mcp_lesson["worked_answers"]
    assert client.post("/mcp", headers={**headers, "Origin": "https://evil.example"}, json={"jsonrpc": "2.0", "id": 3, "method": "ping"}).status_code == 403
    assert client.get("/private/me").status_code == 503
    assert client.post("/private/progress/lesson", json={"level": "rapid-1-month", "area": "cybersecurity", "language": "en", "chapter": 1, "status": "completed"}).status_code == 403


def test_long_course_chapter_and_exercise_numbers():
    book = '<a id="ch-1300"></a>\n## Lesson 1300\n\n### Exercise EX1300\nSolve it.\n\n## Worked answers\n\n### EX1300\nA worked answer.\n'
    chapter = chapter_sections(book)[1300]["markdown"]
    assert "EX1300" in chapter
    assert "A worked answer" in worked_answers(book, chapter)


def test_weekly_chapters_group_130_daily_lessons_into_26_weeks(client):
    plan = "\n\n".join(
        f'<a id="ch-{week:02d}"></a>\n## Chapter {week}\n' +
        "\n".join(f'<a id="lesson-{n:02d}"></a>\n### Lesson {n}' for n in range((week - 1) * 5 + 1, week * 5 + 1))
        for week in range(1, 27)
    )
    book = '<a id="ch-20"></a>\n## Chapter 20\n<a id="lesson-100"></a>\n### Lesson 100\n\n#### Practice\n\n##### EX1000 — Test\nSolve it.\n\n## Worked answers\n\n### EX1000\nWorked result.\n'

    async def source(path):
        if path.endswith('/book/PLAN.md'):
            return plan
        if path.endswith('/book/MANUSCRIPT.md'):
            return book
        return None

    original_source = app.state.source_override
    app.state.source_override = source
    try:
        guide = client.get('/api/courses/professional-6-months/incident-response-resilience/en').json()
        assert guide['daily_schedule_ready'] is True
        assert len(guide['modules']) == 26
        assert guide['modules'][19]['chapters'] == [96, 97, 98, 99, 100]
        assert guide['published_chapters'] == 1
        assert guide['published_lessons'] == 1
        assert guide['planned_lessons'] == 130
        lesson = client.get('/api/lessons/professional-6-months/incident-response-resilience/en/100').json()
        assert lesson['exercise_ids'] == ['1000']
        assert lesson['week_chapter'] == 20
        assert 'Worked result' in lesson['worked_answers']
    finally:
        app.state.source_override = original_source


def test_partial_daily_conversion_keeps_chapters_and_reads_new_public_text(client):
    path = 'levels/professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md'
    original_source = app.state.source_override
    revised = None

    async def source(filename):
        text = await original_source(filename)
        if filename == path and revised is not None:
            return revised
        return text

    app.state.source_override = source
    try:
        guide = client.get('/api/courses/professional-6-months/incident-response-resilience/en').json()
        assert guide['planned_lessons'] == 130
        assert guide['published_lessons'] == 10
        assert guide['published_chapters'] == 12
        assert [day['published'] for day in guide['daily_slots'][:11]] == [True] * 10 + [False]
        assert len(guide['legacy_chapters']) == 12

        day = client.get('/api/lessons/professional-6-months/incident-response-resilience/en/1')
        assert day.status_code == 200
        assert day.headers['cache-control'] == 'no-store'
        assert day.json()['content_kind'] == 'daily_lesson'
        assert day.json()['source_sha256'] == hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        assert '#week-01-day-01' in day.json()['source_url']
        assert '<a id="exercise-ex001"></a>' in day.json()['markdown']
        assert '<a id="answer-ex001"></a>' in day.json()['worked_answers']
        assert 'answer-ex002' not in day.json()['worked_answers']

        chapter = client.get('/api/chapters/professional-6-months/incident-response-resilience/en/2')
        assert chapter.status_code == 200
        assert chapter.json()['content_kind'] == 'legacy_chapter'
        assert 'EX006' in chapter.json()['markdown']
        second_week = client.get('/api/lessons/professional-6-months/incident-response-resilience/en/6')
        assert second_week.status_code == 200
        assert second_week.json()['content_kind'] == 'daily_lesson'
        assert '#week-02-day-01' in second_week.json()['source_url']
        assert '<a id="exercise-ex006"></a>' in second_week.json()['markdown']
        assert '<a id="answer-ex006"></a>' in second_week.json()['worked_answers']
        assert client.get('/api/lessons/professional-6-months/incident-response-resilience/en/11').status_code == 404

        original = (ROOT / path).read_text(encoding='utf-8')
        revised = original.replace('The write path and the observation path have different failure points:', 'The updated write path and observation path have different failure points:', 1)
        assert revised != original
        updated = client.get('/api/lessons/professional-6-months/incident-response-resilience/en/1').json()
        assert 'updated write path' in updated['markdown']
        assert updated['content_sha256'] != day.json()['content_sha256']
    finally:
        app.state.source_override = original_source
