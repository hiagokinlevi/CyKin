"""Public hostnames for the nine book editions."""

from __future__ import annotations

from urllib.parse import urlsplit


LANGUAGES = ("en", "pt", "es", "he", "fr", "ru", "de", "zh", "ja")
ACTIVE_INTERFACES = {"en", "pt", "es"}
BASE_DOMAIN = "opencyber.academy"


def host_for_language(language: str) -> str:
    if language not in LANGUAGES:
        raise ValueError("Unknown language")
    return BASE_DOMAIN if language == "en" else f"{language}.{BASE_DOMAIN}"


def site_for_language(language: str) -> str:
    return "https://" + host_for_language(language)


def language_for_host(host: str) -> str | None:
    hostname = urlsplit("//" + host).hostname or ""
    if hostname in {BASE_DOMAIN, "www." + BASE_DOMAIN}:
        return "en"
    for language in LANGUAGES[1:]:
        if hostname == host_for_language(language):
            return language
    return None


def preferred_language(header: str) -> str:
    """Choose the highest-quality supported browser language; English is default."""
    values = []
    for order, item in enumerate(header.split(",")):
        code, *parameters = item.strip().split(";")
        code = code.split("-", 1)[0].lower()
        quality = 1.0
        for parameter in parameters:
            if parameter.strip().startswith("q="):
                try:
                    quality = float(parameter.strip()[2:])
                except ValueError:
                    quality = 0.0
        if code in LANGUAGES and quality > 0:
            values.append((-quality, order, code))
    return min(values)[2] if values else "en"
