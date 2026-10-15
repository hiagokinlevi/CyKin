"""The ten public tabletop cases must stay complete, localized and navigable."""

import json
import re
import xml.etree.ElementTree as ET
from html import escape
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import app
from tabletop import TEAM_PREFIXES, validate_catalog


ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "web/tabletop/scenarios.json").read_text(encoding="utf-8"))
CASES = validate_catalog(DATA)
HOSTS = {"en": "opencyber.academy", "pt": "pt.opencyber.academy", "es": "es.opencyber.academy"}


@pytest.fixture
def client():
    async def source(path):
        file = ROOT / path
        return file.read_text(encoding="utf-8") if file.is_file() else None

    app.state.source_override = source
    try:
        yield TestClient(app)
    finally:
        del app.state.source_override


@pytest.mark.parametrize("language", HOSTS)
def test_index_has_ten_distinct_cases_and_localized_search_metadata(client, language):
    response = client.get("/tabletop/", headers={"host": HOSTS[language]})
    assert response.status_code == 200
    assert response.headers["content-language"] == language
    assert response.headers["cache-control"] == "no-store"
    page = response.text
    assert f'<html lang="{language}">' in page
    assert f'<link rel="canonical" href="https://{HOSTS[language]}/tabletop/">' in page
    assert '<meta name="robots" content="index,follow' in page
    assert page.count('class="tabletop-card"') == 10
    assert 'https://csrc.nist.gov/pubs/sp/800/61/r3/final' in page
    for case in CASES:
        assert f'href="/tabletop/{case["id"]}/"' in page
        assert case["title"][language] in page


@pytest.mark.parametrize("language", HOSTS)
@pytest.mark.parametrize("number", range(10))
def test_case_has_five_nist_stages_and_three_named_teams_per_stage(client, language, number):
    case = CASES[number]
    response = client.get(f'/tabletop/{case["id"]}/', headers={"host": HOSTS[language]})
    assert response.status_code == 200
    page = response.text
    assert page.count('class="tabletop-stage"') == 5
    assert page.count('<tbody>') == 5
    assert page.count('<tr><th scope="row">') == 15
    assert page.count('<details>') == 5
    assert all(f'id="stage-{stage}"' in page for stage in range(1, 6))
    assert all(code in page for code in ("GV · ID · PR", "DE", "RS", "RC", "ID.IM"))
    assert len(set(TEAM_PREFIXES[number])) == 3
    for prefix in TEAM_PREFIXES[number]:
        assert page.count(f'>{prefix} ') == 5
    assert escape(case["guardrail"][language], quote=True) in page
    assert escape(case["acceptance"][language], quote=True) in page
    assert escape(case["improvement"][language], quote=True) in page
    structured = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S).group(1))
    assert structured["inLanguage"] == language
    assert structured["isAccessibleForFree"] is True


def test_missing_case_and_untranslated_host_are_explicit(client):
    assert client.get("/tabletop/unknown-case/").status_code == 404
    response = client.get("/tabletop/", headers={"host": "fr.opencyber.academy"}, follow_redirects=False)
    assert response.status_code == 302
    assert response.headers["location"] == "https://opencyber.academy/tabletop/"


def test_sitemaps_advertise_only_authored_language_pages():
    for language, host in HOSTS.items():
        root = ET.fromstring((ROOT / f"web/public/sitemap-{language}-pages.xml").read_text())
        urls = {loc.text for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
        assert f"https://{host}/tabletop/" in urls
        assert all(f"https://{host}/tabletop/{case['id']}/" in urls for case in CASES)
    root = ET.fromstring((ROOT / "web/public/sitemap-fr-pages.xml").read_text())
    assert not any("tabletop" in (loc.text or "") for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"))
