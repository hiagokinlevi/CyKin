"""Public, source-backed NIST-aligned tabletop exercises.

The scenarios are fictional educational cases. SP 800-61r3 supplies the
incident-response framework; these team decisions are authored applications,
not NIST-prescribed playbooks or evidence of a real incident.
"""

from __future__ import annotations

import html
import json
from typing import Any

from locales import site_for_language


SOURCE = "https://csrc.nist.gov/pubs/sp/800/61/r3/final"
TEAM_PREFIXES = (
    ("Aster", "Birch", "Cobalt"), ("Delta", "Elm", "Faro"),
    ("Granite", "Harbor", "Iris"), ("Juniper", "Kestrel", "Lumen"),
    ("Maple", "Nimbus", "Orion"), ("Pine", "Quartz", "River"),
    ("Sable", "Tamar", "Umber"), ("Vale", "Willow", "Xenon"),
    ("Yarrow", "Zenith", "Amber"), ("Beacon", "Cedar", "Dawn"),
)
ROLES = {
    "en": ("Evidence team", "Service team", "Decision team"),
    "pt": ("Equipe de evidências", "Equipe de serviço", "Equipe de decisão"),
    "es": ("Equipo de evidencias", "Equipo de servicio", "Equipo de decisiones"),
}
UI = {
    "en": {
        "skip": "Skip to exercise", "nav": "Main navigation", "courses": "Courses", "tests": "Tests", "account": "My area", "toc": "Scenario stages",
        "title": "TableTop", "intro": "Ten guided, fictional incident-response exercises. Choose a case, make each decision before opening the worked team response, and compare what, how and why.",
        "index": "All scenarios", "case": "Scenario", "fiction": "Fictional training scenario; no real system or person is described.",
        "framework": "NIST SP 800-61 Rev. 3 aligns incident response with CSF 2.0. Govern, Identify and Protect support preparation; Detect, Respond and Recover form the response cycle; Identify/Improvement captures lessons. The decisions below are an educational application of this framework.",
        "guardrail": "Safety and authority boundary", "challenge": "Your decision", "reveal": "Reveal the worked team response",
        "what": "What", "how": "How", "why": "Why", "team": "Team",
        "prompt": "Before opening the response, decide what each named team should do, how it would do it, why, whose approval is needed, and what evidence would change the decision.",
        "accept": "Recovery acceptance test", "learn": "Improvement to verify", "previous": "Previous scenario", "next": "Next scenario",
        "source": "NIST framework source", "note": "A tabletop result is practice, not an accredited assessment or permission to act on a real system.",
        "fallback": "This scenario has not yet been translated into your selected language; open the English edition.",
    },
    "pt": {
        "skip": "Pular para o exercício", "nav": "Navegação principal", "courses": "Cursos", "tests": "Testes", "account": "Minha área", "toc": "Etapas do cenário",
        "title": "TableTop", "intro": "Dez exercícios guiados e fictícios de resposta a incidentes. Escolha um caso, tome cada decisão antes de abrir a resposta das equipes e compare o quê, como e por quê.",
        "index": "Todos os cenários", "case": "Cenário", "fiction": "Cenário fictício para estudo; nenhuma pessoa ou sistema real é descrito.",
        "framework": "O NIST SP 800-61 Rev. 3 integra a resposta a incidentes ao CSF 2.0. Governar, Identificar e Proteger apoiam a preparação; Detectar, Responder e Recuperar compõem o ciclo de resposta; Identificar/Melhoria registra as lições. As decisões abaixo são uma aplicação didática desse modelo.",
        "guardrail": "Limite de segurança e autoridade", "challenge": "Sua decisão", "reveal": "Mostrar a resposta comentada das equipes",
        "what": "O que fez", "how": "Como fez", "why": "Por que fez", "team": "Equipe",
        "prompt": "Antes de abrir a resposta, decida o que cada equipe nomeada deve fazer, como, por quê, quem aprova e qual evidência mudaria a decisão.",
        "accept": "Critério de aceitação da recuperação", "learn": "Melhoria a verificar", "previous": "Cenário anterior", "next": "Próximo cenário",
        "source": "Fonte do modelo NIST", "note": "O resultado da simulação é prática, não uma avaliação credenciada nem autorização para agir em sistema real.",
        "fallback": "Este cenário ainda não foi traduzido para o idioma escolhido; abra a edição em inglês.",
    },
    "es": {
        "skip": "Saltar al ejercicio", "nav": "Navegación principal", "courses": "Cursos", "tests": "Pruebas", "account": "Mi área", "toc": "Etapas del escenario",
        "title": "TableTop", "intro": "Diez ejercicios guiados y ficticios de respuesta a incidentes. Elija un caso, tome cada decisión antes de abrir la respuesta de los equipos y compare qué, cómo y por qué.",
        "index": "Todos los escenarios", "case": "Escenario", "fiction": "Escenario ficticio para estudiar; no describe personas ni sistemas reales.",
        "framework": "NIST SP 800-61 Rev. 3 integra la respuesta a incidentes con CSF 2.0. Gobernar, Identificar y Proteger apoyan la preparación; Detectar, Responder y Recuperar forman el ciclo de respuesta; Identificar/Mejora recoge lo aprendido. Las decisiones siguientes son una aplicación educativa de este modelo.",
        "guardrail": "Límite de seguridad y autoridad", "challenge": "Su decisión", "reveal": "Mostrar la respuesta desarrollada de los equipos",
        "what": "Qué hizo", "how": "Cómo lo hizo", "why": "Por qué lo hizo", "team": "Equipo",
        "prompt": "Antes de abrir la respuesta, decida qué debe hacer cada equipo nombrado, cómo, por qué, quién lo aprueba y qué evidencia cambiaría la decisión.",
        "accept": "Criterio de aceptación de la recuperación", "learn": "Mejora que debe verificarse", "previous": "Escenario anterior", "next": "Siguiente escenario",
        "source": "Fuente del modelo NIST", "note": "El resultado de la simulación es práctica, no una evaluación acreditada ni permiso para actuar sobre un sistema real.",
        "fallback": "Este escenario aún no se ha traducido al idioma elegido; abra la edición en inglés.",
    },
}
STAGES = {
    "en": (
        ("Preparation", "GV · ID · PR", "situation"),
        ("Detection and analysis", "DE", "signal"),
        ("Response and containment", "RS", "guardrail"),
        ("Recovery", "RC", "recovery"),
        ("Improvement", "ID.IM", "improvement"),
    ),
    "pt": (
        ("Preparação", "GV · ID · PR", "situation"),
        ("Detecção e análise", "DE", "signal"),
        ("Resposta e contenção", "RS", "guardrail"),
        ("Recuperação", "RC", "recovery"),
        ("Melhoria", "ID.IM", "improvement"),
    ),
    "es": (
        ("Preparación", "GV · ID · PR", "situation"),
        ("Detección y análisis", "DE", "signal"),
        ("Respuesta y contención", "RS", "guardrail"),
        ("Recuperación", "RC", "recovery"),
        ("Mejora", "ID.IM", "improvement"),
    ),
}

# Each row is what the team did, the method, and the rationale. The case fields
# make the plan specific; every phase names all three distinct teams.
ACTIONS = {
    "en": (
        (
            ("Prepared an evidence route", "Named read-only sources and custodians for: {signal}", "The first alert needs a verifiable provenance and time."),
            ("Rehearsed safe continuity", "Tested an isolated version of: {recovery}", "A rushed recovery can worsen the service impact."),
            ("Set authority and escalation", "Assigned owners and approval conditions around: {guardrail}", "Safety, privacy and communications need accountable decisions."),
        ),
        (
            ("Triaged the signal", "Preserved source, UTC time and a second independent check for: {signal}", "One alert is a lead, not proof of cause or scope."),
            ("Measured user impact", "Compared the actual service with the scenario baseline: {situation}", "Technical alerts alone do not establish operational impact."),
            ("Declared a bounded case", "Recorded confirmed facts, unknowns, owner and next review time.", "The teams can coordinate without overstating the evidence."),
        ),
        (
            ("Preserved and scoped evidence", "Saved the original records and defined a bounded path for: {containment}", "Containment must not destroy the basis for later review."),
            ("Applied the approved control", "Implemented: {containment}", "A reversible, owner-approved change reduces harm without expanding scope."),
            ("Authorized and communicated", "Logged the approver, affected users and constraint: {guardrail}", "Response actions need clear authority and proportional notice."),
        ),
        (
            ("Checked for persistence", "Compared new telemetry against: {acceptance}", "An apparently healthy service can still be compromised."),
            ("Restored in stages", "Executed: {recovery}", "A staged return tests dependencies before widening access."),
            ("Accepted the business outcome", "Requested owner sign-off only after: {acceptance}", "Recovery is a service decision, not merely a green dashboard."),
        ),
        (
            ("Turned uncertainty into a test", "Documented the evidence gap and proposed: {improvement}", "A lesson needs a measurable future check."),
            ("Rehearsed the changed control", "Assigned an owner and date to test: {improvement}", "An untested action item is not a verified improvement."),
            ("Closed the decision record", "Approved resources, tracked the owner and checked the new control later.", "Learning must feed Govern, Identify and Protect."),
        ),
    ),
    "pt": (
        (
            ("Preparou a rota de evidências", "Nomeou fontes somente de leitura e responsáveis para: {signal}", "O primeiro alerta precisa de origem e horário verificáveis."),
            ("Ensaiou a continuidade segura", "Testou em isolamento uma versão de: {recovery}", "Recuperação apressada pode agravar o impacto no serviço."),
            ("Definiu autoridade e escalonamento", "Atribuiu responsáveis e condições de aprovação para: {guardrail}", "Segurança, privacidade e comunicação exigem decisão atribuída."),
        ),
        (
            ("Avaliou o sinal", "Preservou origem, horário UTC e confirmação independente de: {signal}", "Um alerta é pista, não prova de causa ou abrangência."),
            ("Mediu impacto nos usuários", "Comparou o serviço real com a linha de base: {situation}", "Alertas técnicos sozinhos não comprovam impacto operacional."),
            ("Abriu caso delimitado", "Registrou fatos confirmados, incógnitas, responsável e horário da próxima revisão.", "As equipes se coordenam sem exagerar as evidências."),
        ),
        (
            ("Preservou e delimitou evidências", "Guardou registros originais e definiu caminho limitado para: {containment}", "A contenção não deve destruir a base da revisão posterior."),
            ("Aplicou o controle aprovado", "Executou: {containment}", "Mudança reversível e aprovada reduz danos sem ampliar o escopo."),
            ("Autorizou e comunicou", "Registrou aprovador, pessoas afetadas e limite: {guardrail}", "Ações exigem autoridade clara e aviso proporcional."),
        ),
        (
            ("Verificou persistência", "Comparou nova telemetria com: {acceptance}", "Serviço aparentemente saudável ainda pode estar comprometido."),
            ("Restaurou em etapas", "Executou: {recovery}", "O retorno gradual testa dependências antes de ampliar o acesso."),
            ("Aceitou o resultado operacional", "Pediu aprovação do responsável somente após: {acceptance}", "Recuperação é decisão de serviço, não apenas painel verde."),
        ),
        (
            ("Transformou incerteza em teste", "Documentou lacuna de evidência e propôs: {improvement}", "Uma lição exige verificação futura mensurável."),
            ("Ensaiou o controle alterado", "Atribuiu responsável e data para testar: {improvement}", "Item não testado não é melhoria verificada."),
            ("Fechou registro de decisões", "Aprovou recursos, acompanhou o responsável e verificou depois o controle.", "O aprendizado deve alimentar Governar, Identificar e Proteger."),
        ),
    ),
    "es": (
        (
            ("Preparó la ruta de evidencia", "Nombró fuentes de solo lectura y responsables para: {signal}", "La primera alerta necesita origen y hora verificables."),
            ("Ensayó la continuidad segura", "Probó de forma aislada una versión de: {recovery}", "Una recuperación precipitada puede agravar el impacto."),
            ("Definió autoridad y escalamiento", "Asignó responsables y condiciones de aprobación para: {guardrail}", "Seguridad, privacidad y comunicación requieren decisiones responsables."),
        ),
        (
            ("Evaluó la señal", "Conservó origen, hora UTC y comprobación independiente de: {signal}", "Una alerta es una pista, no prueba de causa o alcance."),
            ("Midió el impacto en usuarios", "Comparó el servicio real con la línea base: {situation}", "Las alertas técnicas solas no demuestran impacto operativo."),
            ("Abrió un caso delimitado", "Registró hechos confirmados, incógnitas, responsable y próxima revisión.", "Los equipos se coordinan sin exagerar la evidencia."),
        ),
        (
            ("Conservó y delimitó evidencia", "Guardó los registros originales y definió una ruta limitada para: {containment}", "La contención no debe destruir la base de la revisión posterior."),
            ("Aplicó el control aprobado", "Ejecutó: {containment}", "Un cambio reversible y aprobado reduce daños sin ampliar el alcance."),
            ("Autorizó y comunicó", "Registró aprobador, personas afectadas y límite: {guardrail}", "Las acciones exigen autoridad clara y aviso proporcional."),
        ),
        (
            ("Comprobó la persistencia", "Comparó nueva telemetría con: {acceptance}", "Un servicio aparentemente sano todavía puede estar comprometido."),
            ("Restauró por etapas", "Ejecutó: {recovery}", "El retorno gradual prueba dependencias antes de ampliar el acceso."),
            ("Aceptó el resultado operativo", "Pidió aprobación del responsable solo después de: {acceptance}", "Recuperar es una decisión de servicio, no solo un panel verde."),
        ),
        (
            ("Convirtió incertidumbre en prueba", "Documentó la laguna de evidencia y propuso: {improvement}", "Una lección requiere una comprobación futura medible."),
            ("Ensayó el control modificado", "Asignó responsable y fecha para probar: {improvement}", "Una tarea no probada no es una mejora verificada."),
            ("Cerró el registro de decisiones", "Aprobó recursos, siguió al responsable y comprobó el nuevo control.", "El aprendizaje debe alimentar Gobernar, Identificar y Proteger."),
        ),
    ),
}


def _esc(value: str) -> str:
    return html.escape(value, quote=True)


def _value(case: dict[str, Any], key: str, language: str) -> str:
    return str(case[key][language])


def validate_catalog(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Reject missing or duplicate scenarios before rendering them."""
    if data.get("version") != 1 or data.get("source") != SOURCE:
        raise ValueError("Unsupported tabletop source")
    cases = data.get("scenarios")
    if not isinstance(cases, list) or len(cases) != 10:
        raise ValueError("The TableTop collection requires ten scenarios")
    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)) or any(not isinstance(value, str) or not value.replace("-", "").isalnum() for value in ids):
        raise ValueError("Invalid scenario identity")
    for case in cases:
        for field in ("title", "situation", "signal", "guardrail", "containment", "recovery", "acceptance", "improvement"):
            if not isinstance(case.get(field), dict) or any(
                not isinstance(case[field].get(language), str) or len(case[field][language].strip()) < 12
                for language in ("en", "pt", "es")
            ):
                raise ValueError(f"Incomplete scenario translation: {case['id']} {field}")
    return cases


def _document(language: str, title: str, description: str, path: str, body: str) -> str:
    ui = UI[language]
    usage = {
        "en": ("Page views", "Participating browsers", "Last 30 days · optional analytics"),
        "pt": ("Visualizações", "Navegadores participantes", "Últimos 30 dias · análise opcional"),
        "es": ("Visualizaciones", "Navegadores participantes", "Últimos 30 días · análisis opcional"),
    }[language]
    origin = site_for_language(language)
    canonical = origin + path
    alternates = "".join(
        f'<link rel="alternate" hreflang="{lang}" href="{_esc(site_for_language(lang) + path)}">'
        for lang in ("en", "pt", "es")
    )
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "LearningResource", "name": title,
        "description": description, "inLanguage": language, "isAccessibleForFree": True,
        "url": canonical, "citation": SOURCE,
    }, ensure_ascii=False).replace("<", "\\u003c")
    return f'''<!doctype html><html lang="{language}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{_esc(title)} · OpenCyber Academy</title><meta name="description" content="{_esc(description)}">
<meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{_esc(canonical)}">
{alternates}<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{_esc(title)}"><meta property="og:description" content="{_esc(description)}">
<meta property="og:url" content="{_esc(canonical)}"><meta name="twitter:card" content="summary">
<script type="application/ld+json">{schema}</script>
<link rel="stylesheet" href="/seo-lesson.css"><link rel="stylesheet" href="/tabletop.css">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem('open-cyber-academy-theme')||'dark'}}catch(_){{document.documentElement.dataset.theme='dark'}}</script>
<script src="/analytics.js" defer></script><script src="/insights.js" defer></script></head><body>
<a class="skip" href="#tabletop-main">{_esc(ui["skip"])}</a>
<header class="header"><div class="shell header-row"><a class="brand" href="/"><img src="/favicon.svg" alt="" width="28" height="28">OpenCyber Academy</a>
<nav aria-label="{_esc(ui["nav"])}"><a href="/levels/">{_esc(ui["courses"])}</a><a href="/tests/">{_esc(ui["tests"])}</a><a href="/tabletop/" aria-current="page">TableTop</a><a href="/account/">{_esc(ui["account"])}</a></nav></div></header>
<main id="tabletop-main" class="shell tabletop-main"><div class="tabletop-usage" aria-label="{_esc(usage[2])}"><span>{_esc(usage[2])}</span><strong data-insight="page.views">—</strong> {_esc(usage[0])}<strong data-insight="page.browsers">—</strong> {_esc(usage[1])}<small data-insight-status role="status"></small></div>{body}</main>
<footer class="footer"><div class="shell">© OpenCyber Academy · {_esc(ui["note"])} · <a href="{SOURCE}">{_esc(ui["source"])}</a></div></footer>
</body></html>'''


def render_index(data: dict[str, Any], language: str) -> str:
    cases = validate_catalog(data)
    ui = UI[language]
    cards = "".join(
        f'<li><a class="tabletop-card" href="/tabletop/{_esc(case["id"])}/">'
        f'<span class="tabletop-count">{number:02d}</span><strong>{_esc(_value(case, "title", language))}</strong>'
        f'<span>{_esc(_value(case, "situation", language))}</span><span class="tabletop-arrow" aria-hidden="true">→</span>'
        f'</a></li>'
        for number, case in enumerate(cases, 1)
    )
    body = (f'<div class="eyebrow">NIST SP 800-61 REV. 3 · CSF 2.0</div><h1>{_esc(ui["title"])}</h1>'
            f'<p class="tabletop-lead">{_esc(ui["intro"])}</p><p class="tabletop-framework">{_esc(ui["framework"])}</p>'
            f'<p class="tabletop-note">{_esc(ui["fiction"])}</p><ol class="tabletop-grid">{cards}</ol>')
    return _document(language, ui["title"], ui["intro"], "/tabletop/", body)


def render_case(data: dict[str, Any], language: str, slug: str) -> str | None:
    cases = validate_catalog(data)
    match = next(((index, case) for index, case in enumerate(cases) if case["id"] == slug), None)
    if match is None:
        return None
    index, case = match
    ui = UI[language]
    title = _value(case, "title", language)
    names = [f"{prefix} {role}" for prefix, role in zip(TEAM_PREFIXES[index], ROLES[language])]
    stages = []
    for stage_index, (heading, code, field) in enumerate(STAGES[language]):
        rows = []
        for team_index, templates in enumerate(ACTIONS[language][stage_index]):
            what, how, why = (template.format(**{key: _value(case, key, language) for key in (
                "situation", "signal", "guardrail", "containment", "recovery", "acceptance", "improvement"
            )}) for template in templates)
            rows.append(f'<tr><th scope="row">{_esc(names[team_index])}</th>'
                        f'<td>{_esc(what)}</td><td>{_esc(how)}</td><td>{_esc(why)}</td></tr>')
        stages.append(
            f'<section class="tabletop-stage" id="stage-{stage_index + 1}">'
            f'<div class="tabletop-stage-head"><span>{stage_index + 1:02d} / 05</span><div><h2>{_esc(heading)}</h2><small>{code}</small></div></div>'
            f'<p class="tabletop-inject">{_esc(_value(case, field, language))}</p>'
            f'<p class="tabletop-prompt"><strong>{_esc(ui["challenge"])}.</strong> {_esc(ui["prompt"])}</p>'
            f'<details><summary>{_esc(ui["reveal"])}</summary><div class="tabletop-scroll">'
            f'<table><thead><tr><th>{_esc(ui["team"])}</th><th>{_esc(ui["what"])}</th>'
            f'<th>{_esc(ui["how"])}</th><th>{_esc(ui["why"])}</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div></details></section>'
        )
    previous = f'<a href="/tabletop/{cases[index - 1]["id"]}/">← {_esc(ui["previous"])}</a>' if index else ""
    following = f'<a href="/tabletop/{cases[index + 1]["id"]}/">{_esc(ui["next"])} →</a>' if index + 1 < len(cases) else ""
    body = (
        f'<nav class="tabletop-back"><a href="/tabletop/">← {_esc(ui["index"])}</a></nav>'
        f'<div class="eyebrow">{_esc(ui["case"])} {index + 1:02d} / 10 · NIST SP 800-61 REV. 3</div>'
        f'<h1>{_esc(title)}</h1><p class="tabletop-lead">{_esc(_value(case, "situation", language))}</p>'
        f'<p class="tabletop-note">{_esc(ui["fiction"])}</p><section class="tabletop-boundary">'
        f'<h2>{_esc(ui["guardrail"])}</h2><p>{_esc(_value(case, "guardrail", language))}</p></section>'
        f'<nav class="tabletop-toc" aria-label="{_esc(ui["toc"])}">'
        + "".join(f'<a href="#stage-{n + 1}">{_esc(stage[0])}</a>' for n, stage in enumerate(STAGES[language])) +
        f'</nav>{"".join(stages)}<section class="tabletop-outcome"><h2>{_esc(ui["accept"])}</h2>'
        f'<p>{_esc(_value(case, "acceptance", language))}</p><h2>{_esc(ui["learn"])}</h2>'
        f'<p>{_esc(_value(case, "improvement", language))}</p></section>'
        f'<nav class="tabletop-prevnext">{previous}<a href="/tabletop/">{_esc(ui["index"])}</a>{following}</nav>'
    )
    return _document(language, title, _value(case, "situation", language), f"/tabletop/{slug}/", body)
