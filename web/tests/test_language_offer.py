"""The English home remains the default; browser locale is a user choice."""

from fastapi.testclient import TestClient

from app import app


def test_english_home_does_not_auto_redirect_for_portuguese_browser():
    with TestClient(app, base_url="https://opencyber.academy") as client:
        response = client.get("/", headers={"Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"}, follow_redirects=False)
    assert response.status_code == 200
    assert "<html lang=\"en\">" in response.text
    assert "id=\"language-offer\"" in response.text
    assert "Continue in English" in response.text


def test_spanish_subdomain_serves_spanish_home_without_language_offer_redirect():
    with TestClient(app, base_url="https://es.opencyber.academy") as client:
        response = client.get("/", headers={"Accept-Language": "es-ES,es;q=0.9"}, follow_redirects=False)
    assert response.status_code == 200
    assert "<html lang=\"es\">" in response.text
