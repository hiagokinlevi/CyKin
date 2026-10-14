"""Search pages must expose real authored lessons and safe, stable metadata."""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import app, worked_answers
from seo_pages import render_lesson_page


ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def client():
    app.state.catalog_override = json.loads((ROOT / "web/public/catalog.json").read_text())

    async def local_source(path):
        file = ROOT / path
        return file.read_text(encoding="utf-8") if file.is_file() else None

    app.state.source_override = local_source
    try:
        yield TestClient(app)
    finally:
        del app.state.catalog_override
        del app.state.source_override


def test_authored_lesson_has_indexable_html_and_stable_navigation(client):
    path = "/courses/rapid-1-month/incident-response-resilience/lessons/en/1/"
    response = client.get(path)
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert response.headers["content-language"] == "en"
    assert response.headers["cache-control"] == "no-store"
    assert f'<link rel="canonical" href="https://opencyber.academy{path}">' in response.text
    assert '<meta name="robots" content="index,follow' in response.text
    assert '"@type":"LearningResource"' in response.text
    assert '"@type":"BreadcrumbList"' in response.text
    assert '"isAccessibleForFree":true' in response.text
    structured = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', response.text, re.S).group(1))
    assert structured[0]["url"] == f"https://opencyber.academy{path}"
    assert structured[1]["itemListElement"][-1]["item"] == f"https://opencyber.academy{path}"
    assert '<article class="prose" lang="en">' in response.text
    assert "An incident response team does more than react" in response.text
    assert 'id="exercise-ex001"' in response.text
    assert 'id="answer-ex001"' in response.text
    assert 'href="#answer-ex001"' in response.text
    assert '/lessons/en/2/' in response.text
    assert 'src="/analytics.js"' in response.text
    assert client.get("/courses/rapid-1-month/incident-response-resilience/lessons/en/21/").status_code == 404
    chapter_only = client.get("/courses/rapid-1-month/information-security/lessons/en/1/", follow_redirects=False)
    assert chapter_only.status_code == 308
    assert chapter_only.headers["location"] == "/courses/rapid-1-month/information-security/chapters/en/1/"


def test_translated_chapters_use_localized_course_names_in_search_and_navigation(client):
    cases = (
        ("pt", "quantum-post-quantum-security", "Profissionalizante", "Segurança quântica e pós-quântica", "Navegação entre aulas"),
        ("es", "ot-iot-security", "Profesional", "Seguridad de OT, IoT y sistemas ciberfísicos", "Navegación entre lecciones"),
    )
    for language, area, level_name, course_name, navigation in cases:
        path = f"/courses/professional-6-months/{area}/chapters/{language}/1/"
        response = client.get(path, headers={"host": f"{language}.opencyber.academy"})
        assert response.status_code == 200
        assert f'<html lang="{language}"' in response.text
        assert f"{level_name} {course_name} | OpenCyber Academy</title>" in response.text
        assert f'aria-label="{navigation}"' in response.text
        structured = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', response.text, re.S).group(1))
        assert structured[0]["isPartOf"]["name"] == course_name
        assert structured[0]["educationalLevel"] == level_name


def test_sitemap_lists_only_routes_that_resolve_to_authored_sections(client):
    sitemaps = {language: (ROOT / f"web/public/sitemap-{language}.xml").read_text()
                for language in ("en", "pt", "es", "he", "fr", "ru", "de", "zh", "ja")}
    sitemap = sitemaps["en"]
    index = json.loads((ROOT / "web/public/lesson-index.json").read_text())
    assert "https://opencyber.academy/courses/rapid-1-month/incident-response-resilience/lessons/en/1/" in sitemap
    assert "https://opencyber.academy/courses/rapid-1-month/incident-response-resilience/lessons/en/21/" not in sitemap
    assert index["rapid-1-month/incident-response-resilience/en"]["lessons"][0]["number"] == 1
    info = index["rapid-1-month/information-security/en"]
    assert info["chapter_lessons"] is True
    assert len(info["chapters"]) == 20 and not info["lessons"]
    assert "https://opencyber.academy/courses/rapid-1-month/information-security/chapters/en/20/" in sitemap
    assert "https://opencyber.academy/courses/rapid-1-month/information-security/lessons/en/20/" not in sitemap
    assert "https://pt.opencyber.academy/courses/professional-6-months/quantum-post-quantum-security/chapters/pt/1/" in sitemaps["pt"]
    assert "https://es.opencyber.academy/courses/professional-6-months/ot-iot-security/chapters/es/1/" in sitemaps["es"]
    for language, xml in sitemaps.items():
        urls = [node.text for node in ET.fromstring(xml).iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        assert len(urls) == len(set(urls))
        assert all(url.startswith(f"https://{language + '.' if language != 'en' else ''}opencyber.academy/") for url in urls)
        if language not in {"en", "pt", "es"}:
            assert not urls  # No translated manuscripts exist yet.
    assert sum(len(re.findall(r"<url><loc>", xml)) for xml in sitemaps.values()) > 7000
    assert client.get("/sitemap.xml", headers={"host": "pt.opencyber.academy"}).text == sitemaps["pt"]
    assert "https://es.opencyber.academy/sitemap.xml" in client.get("/robots.txt", headers={"host": "es.opencyber.academy"}).text
    assert client.get("/api/catalog").headers["x-robots-tag"] == "noindex"


def test_sitemap_language_alternates_are_reciprocal_and_authored():
    sitemap_ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    xhtml_link = "{http://www.w3.org/1999/xhtml}link"
    pages = {}
    for language in ("en", "pt", "es"):
        root = ET.fromstring((ROOT / f"web/public/sitemap-{language}.xml").read_text())
        for page in root.findall(f"{sitemap_ns}url"):
            pages[page.findtext(f"{sitemap_ns}loc")] = {
                alternate.attrib["hreflang"]: alternate.attrib["href"]
                for alternate in page.findall(xhtml_link)
            }

    base = "/courses/professional-6-months/ot-iot-security/chapters/"
    variants = {
        "en": f"https://opencyber.academy{base}en/1/",
        "pt": f"https://pt.opencyber.academy{base}pt/1/",
        "es": f"https://es.opencyber.academy{base}es/1/",
    }
    assert all(pages[url] == variants for url in variants.values())
    english_only = "https://opencyber.academy/courses/rapid-1-month/incident-response-resilience/lessons/en/1/"
    assert pages[english_only] == {}
    assert all(
        target in pages and pages[target] == alternates
        for alternates in pages.values() for target in alternates.values()
    )


def test_language_hosts_and_unwritten_study_slots_are_honest(client):
    english_offer = client.get("/", headers={"host": "opencyber.academy", "accept-language": "pt-BR,pt;q=0.9,en;q=0.8"}, follow_redirects=False)
    assert english_offer.status_code == 200
    assert '<html lang="en">' in english_offer.text
    assert 'id="language-offer"' in english_offer.text
    assert client.get("/", headers={"host": "opencyber.academy", "accept-language": "en-US"}).status_code == 200
    for language in ("pt", "es"):
        host = f"{language}.opencyber.academy"
        home = client.get("/", headers={"host": host})
        about = client.get("/about/", headers={"host": host})
        assert home.status_code == about.status_code == 200
        assert f'<html lang="{language}">' in home.text
        assert f'https://{host}/about/' in about.text
        assert 'name="robots" content="index,follow' in home.text
        assert "Hiago Kin Levi" in about.text
    french = client.get("/", headers={"host": "fr.opencyber.academy"})
    assert french.status_code == 200 and 'content="noindex,follow"' in french.text
    planned = client.get("/courses/professional-6-months/incident-response-resilience/lessons/en/11/", headers={"host": "opencyber.academy"})
    assert planned.status_code == 200
    assert planned.headers["x-robots-tag"] == "noindex, follow"
    assert "have not been published yet" in planned.text
    assert "/lessons/en/12/" in planned.text
    assert client.get("/courses/professional-6-months/incident-response-resilience/lessons/en/131/").status_code == 404
    cross_host = client.get("/courses/rapid-1-month/incident-response-resilience/lessons/pt/1/", headers={"host": "opencyber.academy"}, follow_redirects=False)
    assert cross_host.status_code == 308
    assert cross_host.headers["location"].startswith("https://pt.opencyber.academy/")


def test_chapter_with_final_appendix_exposes_its_own_worked_answer(client):
    path = "/courses/rapid-1-month/cybersecurity/chapters/en/20/"
    response = client.get(path)
    assert response.status_code == 200
    assert 'id="exercise-ex036"' in response.text
    assert 'id="answer-ex036"' in response.text
    assert "The outage cause is still not established" in response.text
    assert 'id="answer-ex035"' not in response.text
    assert 'href="https://opencyber.academy' + path + '"' in response.text
    assert "respuesta" in worked_answers(
        "## Resultados resueltos\n\n### EX001 — Respuesta\n\nUna respuesta.",
        "### EX001 — Ejercicio",
        ["001"],
    ).lower()


def test_authored_markdown_cannot_inject_script_or_foreign_click_target():
    lesson = {
        "course": {"level": "rapid-1-month", "area": "incident-response-resilience", "language": "en"},
        "chapter": 1, "title": "A lesson </script><script>alert(1)</script>",
        "markdown": "### A lesson\n\nTeaching text. <script>alert(1)</script> [bad](javascript:alert(1)) [next](#lesson-02)",
        "worked_answers": "", "previous": None, "next": 2,
        "source_url": "https://github.com/hiagokinlevi/OpenCyberAcademy/blob/main/levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md#lesson-01",
    }
    page = render_lesson_page(lesson, {"title": "Incident response"}, "Rapid course")
    assert "<script>alert(1)</script>" not in page
    assert 'href="javascript:' not in page
    assert 'href="/courses/rapid-1-month/incident-response-resilience/lessons/en/2/"' in page
    assert "\\u003c/script>" in page
