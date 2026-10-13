# Seguridad de TO, IoT y sistemas ciberfísicos: métodos de investigación de maestría y práctica del trabajo de fin de máster

- Idioma: español (`es`), edición en español neutro internacional; curso de maestría, dos años; aproximadamente 1200 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–8 de 8 tienen texto didáctico escrito, los ejercicios EX001–EX050 y sus resultados resueltos correspondientes. Siguen abiertas la revisión independiente y la verificación de 300 páginas A4.
- Público: investigadores principiantes con sólidos fundamentos en el dominio y alfabetización en métodos de investigación que formularán una pregunta, evaluarán trabajos previos y producirán hallazgos reproducibles en seguridad de TO, IoT y sistemas ciberfísicos.
- Relación con los cursos vecinos: el [curso de maestría de infraestructura crítica](../../../critical-sector-security/README.md) estudia sectores y cascadas; el [curso doctoral de TO](../../../../doctorate-2-years/ot-iot-security/README.md) profundiza en la integridad de la investigación y la práctica de la tesis. **Este libro** lo prepara para diseñar y completar un trabajo de fin de máster sobre la capa del sistema de control: PLC, protocolos industriales, detección basada en la física, coingeniería de seguridad funcional (safety) y seguridad de la información (security) y la arquitectura Purdue/ISA-62443.
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado. No concede autorización para acceder a plantas reales. Todas las organizaciones, conjuntos de datos, bancos de pruebas y números de los ejemplos resueltos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Ocho capítulos siguen un único proyecto de maestría, el **Harbor Loop Study** (Estudio del Lazo Harbor): *¿detecta un CUSUM sobre el residuo del balance de masa la repetición (replay) de un único sensor de nivel en un lazo sintético de almacenamiento de agua antes y con menos falsas alarmas que una alarma de proceso de banda fija, y bajo qué capacidad del atacante desaparece la ventaja?* Los capítulos cubren el método de revisión de la literatura, el seminario de TO, el diseño y la ética, las explicaciones rivales, la propuesta y el piloto, el análisis, la redacción y la defensa.

Mantenga cinco etiquetas en cada nota: observación, inferencia, afirmación, decisión, consecuencia física. Los laboratorios usan solo la biblioteca estándar de Python 3.

### Corpus sintético

| Elemento | Función | Límite |
|---|---|---|
| Harbor Municipal Water, lazo L1 | Modelo principal: tanque, bomba, caudalímetro, transmisor de nivel, PLC, Modbus/TCP | Inventado |
| Campus Rig R2 | Piloto y validación: instalación de laboratorio de dos tanques con válvula de flotador independiente | Inventado |
| Estudios L1–L12 | Literatura ficticia para valoración crítica | Inventado |
| Operadores Q01–Q08 | Participantes ficticios de entrevistas | Inventado |

### Fuentes principales

- NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) (2023).
- [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/).
- Modbus [*Application Protocol V1.1b3*](https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf).
- Giraldo et al., [ACM CSUR 2018](https://doi.org/10.1145/3203245); Urbina et al., [CCS 2016](https://doi.org/10.1145/2976749.2978388).
- Sommer & Paxson [IEEE S&P 2010](https://doi.org/10.1109/SP.2010.25); Arp et al. [USENIX Security 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp).
- Page, [CUSUM, Biometrika 1954](https://doi.org/10.1093/biomet/41.1-2.100).
- [Menlo Report](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf); CISA [CVD](https://www.cisa.gov/coordinated-vulnerability-disclosure-process).
- iTrust [conjuntos de datos SWaT](https://itrust.sutd.edu.sg/itrust-labs_datasets/) (solo la página pública).

## Contenido

1. [Pregunta de investigación y método de revisión de la literatura](#ch-01)
2. [Seguridad de TO, IoT y sistemas ciberfísicos: seminario avanzado](#ch-02)
3. [Diseño del estudio, ética y reproducibilidad](../../en/book/MANUSCRIPT.md#ch-03)
4. [Explicaciones rivales](../../en/book/MANUSCRIPT.md#ch-04)
5. [Propuesta y piloto](../../en/book/MANUSCRIPT.md#ch-05)
6. [Recolección y análisis de datos](../../en/book/MANUSCRIPT.md#ch-06)
7. [Redacción del trabajo de fin de máster y limitaciones](../../en/book/MANUSCRIPT.md#ch-07)
8. [Revisión independiente y defensa](../../en/book/MANUSCRIPT.md#ch-08)
9. [Resultados resueltos](#worked-results)

<a id="ch-01"></a>

## Capítulo 1 — Pregunta de investigación y método de revisión de la literatura

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) convertir un interés vago en una pregunta investigable sobre un lazo de control, (2) buscar con sinónimos en publicaciones de ingeniería de control y de seguridad, (3) deduplicar y cribar con métricas de concordancia y (4) redactar un protocolo de revisión de alcance. Prepara el seminario del capítulo 2.

### 1.1 Del interés a la pregunta

"Seguridad de TO" es un campo, no una pregunta. Una pregunta investigable nombra un **sistema**, un **fenómeno**, una **comparación** y un **alcance**. Ejemplo de Harbor Loop: *en un lazo sintético de nivel de un solo tanque, ¿detecta un CUSUM sobre el residuo que usa un caudalímetro cableado de forma independiente la repetición de un único sensor con mayor exhaustividad por eventos y menor tasa de falsas alarmas que una alarma de banda de ±1.5, y desaparece la ventaja cuando también se suplanta el caudalímetro?* La pregunta ya codifica la condición de fracaso, un hábito propio del nivel de maestría que ahorra meses de afirmaciones exageradas.

### 1.2 Buscar en dos comunidades

La detección basada en la física aparece como "redundancia analítica" y "generación de residuos" en las revistas de control, y como "inyección de datos falsos" y "suplantación de sensores" en las publicaciones de seguridad. Construya una tabla de sinónimos antes de buscar en IEEE Xplore, ACM DL, Scopus y arXiv. Incluya la literatura gris (documentos técnicos de la IEC, avisos de CISA) como una corriente separada con sus propias reglas de elegibilidad, porque no se revisa por pares de la misma manera.

Ejecute cada cadena de búsqueda en cada base de datos y guarde las exportaciones con la fecha, la consulta exacta y el número de resultados, para que un examinador pueda repetir la búsqueda. Espere que las dos comunidades describan el mismo detector con palabras distintas y espere duplicados entre publicaciones; el laboratorio 1 muestra con qué rapidez aparecen cuando una misma revisión está indexada tanto en IEEE como en ACM.

### 1.3 Cribado y concordancia

Dos revisores criban títulos y resúmenes de forma independiente; informe el kappa de Cohen. El laboratorio 1 muestra una exportación sintética con deduplicación por DOI y por título y año, y un kappa de 0.462: una concordancia moderada debida al desacuerdo sobre un documento técnico de un fabricante y un artículo de mediciones de DNP3. Una concordancia baja es una señal para reparar los criterios de elegibilidad, no para forzar el consenso. Redacte las reglas de elegibilidad como enunciados comprobables antes del cribado: ¿evalúa el estudio un detector en un lazo de control?, ¿nombra su modelo de atacante?, ¿informa una métrica más allá de la exactitud? Criben juntos un pequeño lote de calibración, discutan cada desacuerdo y solo después criben el resto de forma independiente. Registre cada regla modificada y la fecha en que cambió.

### 1.4 Ejemplo resuelto y laboratorio 1

```python
# Lab 1 (masters OT, synthetic): deduplicate a search export and compute Cohen's kappa for two screeners.
import re
RECORDS=[
 ("ieee","Physics-based anomaly detection for ICS: a survey",2018,"10.1145/3203245"),
 ("acm","Physics-Based Anomaly Detection for ICS: A Survey",2018,"10.1145/3203245"),
 ("ieee","Modbus security: a survey of attacks and defenses",2020,""),
 ("arxiv","Sensor replay attacks on water treatment testbeds",2021,""),
 ("ieee","Sensor Replay Attacks on Water Treatment Testbeds",2021,""),
 ("grey","Vendor white paper: securing SCADA with AI",2022,""),
 ("ieee","DNP3 Secure Authentication field measurements",2019,""),
 ("acm","Zone and conduit design for IEC 62443",2020,""),
 ("ieee","False data injection in power systems: a survey",2011,"10.1109/TSG.2011.2129544"),
 ("arxiv","False Data Injection Attacks against State Estimation in Electric Power Grids",2011,"10.1109/TSG.2011.2129544"),
]
def key(r):
    doi=r[3].strip().lower();
    if doi: return ("doi",doi)
    t=re.sub(r"[^a-z0-9]","",r[1].lower()); return ("title",t,r[2])
seen={}; kept=[]
for r in RECORDS:
    k=key(r)
    if k in seen: continue
    seen[k]=True; kept.append(r)
# two reviewers: I=include X=exclude; disagreements on grey and DNP3
A="IIXIXIIXIX"[:len(kept)]; B="IIXIXXXIIX"[:len(kept)]
def kappa(a,b):
    n=len(a); agree=sum(x==y for x,y in zip(a,b))/n
    pa=sum(x=="I" for x in a)/n; pb=sum(x=="I" for x in b)/n
    pe=pa*pb+(1-pa)*(1-pb)
    return round(agree,3), round((agree-pe)/(1-pe) if pe!=1 else 1.0,3)
print("raw",len(RECORDS),"kept",len(kept),"dropped",len(RECORDS)-len(kept))
print("agree,kappa",kappa(A,B))
print("kept titles:",[r[1][:40] for r in kept])

```

Salida esperada:

```text
raw 10 kept 7 dropped 3
agree,kappa (0.714, 0.462)
kept titles: ['Physics-based anomaly detection for ICS:', 'Modbus security: a survey of attacks and', 'Sensor replay attacks on water treatment', 'Vendor white paper: securing SCADA with ', 'DNP3 Secure Authentication field measure', 'Zone and conduit design for IEC 62443', 'False data injection in power systems: a']
```

Se eliminan tres duplicados por DOI o por título normalizado. Un kappa de 0.462 con una concordancia bruta del 71.4 % muestra la corrección por azar en acción.

El laboratorio conserva el primer registro de cada par duplicado, de modo que se queda la versión de IEEE de la revisión basada en la física y se elimina la copia de ACM. Dos registros sin DOI se fusionan solo porque sus títulos normalizados y sus años coinciden exactamente; un pequeño cambio de redacción dejaría pasar un duplicado. Revise a ojo la lista conservada antes del cribado e informe en el protocolo el recuento bruto, el conservado y el eliminado, tal como los imprime el laboratorio.

### 1.5 Errores comunes y límites

Buscar solo en publicaciones de seguridad; tratar los artículos de fabricantes como evidencia revisada por pares; informar la concordancia bruta sin kappa; redactar una pregunta sin condición de fracaso. Una pregunta sin condición de fracaso invita a un trabajo de fin de máster que solo puede tener éxito. La pregunta de Harbor Loop lo evita al preguntar cuándo desaparece la ventaja del CUSUM. La búsqueda tiene un límite parecido: las bases de datos cambian su indexación, de modo que una búsqueda ejecutada en marzo puede no devolver el mismo conjunto en septiembre. Registre la fecha de cada ejecución y trate el corpus como una instantánea.

### Ejercicios — capítulo 1

- **EX001 — Pregunta investigable sobre Modbus.** Reescriba "Quiero estudiar la seguridad de Modbus" como una pregunta investigable con sistema, fenómeno, comparación y alcance. *Rúbrica:* 3 = sistema, fenómeno, comparación y alcance con métrica de ≥90 %; 2 = falta un elemento; 1 = interés vago por Modbus; 0 = nada.
- **EX002 — Tabla de sinónimos para la manipulación de sensores.** Construya una tabla de sinónimos (≥4 términos de control + ≥4 de seguridad) para la detección de datos de sensores manipulados. *Rúbrica:* 3 = ≥4 términos de control + ≥4 de seguridad; 2 = 3+3; 1 = una sola comunidad; 0 = nada.
- **EX003 — Incluir o excluir el documento técnico y el de DNP3.** Redacte criterios de inclusión y exclusión que decidan sobre el documento técnico del fabricante y el artículo de DNP3 del laboratorio 1. *Rúbrica:* 3 = los criterios excluyen el marketing de fabricantes e incluyen la medición de campo de DNP3; 2 = decisiones sin criterios; 1 = una decisión; 0 = nada.
- **EX004 — Registro gris con ampersand y kappa.** Ejecute el laboratorio 1; añada un registro gris con un ampersand en el título; muestre si su key() lo detecta; recalcule kappa tras cambiar una decisión. *Rúbrica:* 3 = la clave normalizada detecta el ampersand + se explica el movimiento de kappa; 2 = clave sin kappa; 1 = solo kappa; 0 = nada.
- **EX005 — Protocolo de revisión de alcance de una página.** Redacte un protocolo de revisión de alcance de una página (bases de datos, fechas, sinónimos, reglas de cribado, objetivo de kappa). *Rúbrica:* 3 = bases de datos/fechas/sinónimos/cribado/κ≥0.6; 2 = falta un campo; 1 = lista de viñetas; 0 = nada.
- **EX006 — Clave DOI antes que clave de título.** Explique por qué, en la deduplicación, una clave DOI debe preceder a una clave de título. *Rúbrica:* 3 = identidad del DOI entre variantes del título + modo de fallo de la clave de título; 2 = DOI primero sin modo de fallo; 1 = eslogan; 0 = nada.
- **EX007 — Niveles de evidencia para tres fuentes.** Clasifique tres fuentes (la revisión de Giraldo, un aviso de CISA, un blog de un fabricante) por nivel de evidencia para un trabajo de fin de máster. *Rúbrica:* 3 = Giraldo alto, CISA medio, blog del fabricante bajo, con razones; 2 = niveles sin razones; 1 = una fuente; 0 = nada.

### Síntesis del capítulo

Un proyecto de maestría empieza con una pregunta que ya nombra su condición de fracaso, una búsqueda que abarca varias comunidades y un proceso de cribado cuyos desacuerdos reparan los criterios.

### Siga estudiando — capítulo 01 de 08

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Seguridad de TO, IoT y sistemas ciberfísicos: seminario avanzado

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) explicar los niveles Purdue y las zonas de ISA/IEC 62443, (2) describir por qué los protocolos industriales clásicos carecen de autenticación, (3) contrastar la detección en red con la detección basada en la física, (4) leer ATT&CK for ICS como evidencia de capacidad y no como evidencia de frecuencia, y (5) extraer una laguna falsable de un mapa de la literatura.

### 2.1 Arquitectura: Purdue y zonas

NIST SP 800-82 Rev. 3 presenta el modelo Purdue: niveles 0–1 (proceso y control básico), 2 (supervisión), 3 (operaciones), 4–5 (empresa), con una DMZ industrial. ISA/IEC 62443-3-2 le pide particionar en **zonas** con un nivel de seguridad objetivo y controlar los **conductos** entre ellas. Un trabajo de fin de máster puede tratar un diseño de zonas como una hipótesis: ¿reduce un conducto que solo permite lecturas Modbus del nivel 2 al nivel 1 la alcanzabilidad de escritura en una fracción medida dentro de una topología sintética? En Harbor Loop la frontera pertinente se sitúa entre el nivel de supervisión y el PLC, donde Modbus/TCP transporta tanto lecturas como escrituras. Dibuje esa frontera en el trabajo aunque el estudio mida la detección y no la segmentación, porque el lector necesita saber qué posiciones del atacante supone la repetición. Un conducto que bloquea las escrituras no detiene las lecturas repetidas, y por eso la detección sigue importando.

### 2.2 Protocolos

El Modbus Application Protocol define códigos de función (entre ellos los de escritura de uno o varios registros) y un modelo de datos, pero ningún campo de autenticación ni de integridad. DNP3 Secure Authentication y los modelos de seguridad de OPC UA muestran que la industria ha añadido opciones; su adopción y la calidad de su implementación siguen siendo cuestiones empíricas. Nunca presente "Modbus es inseguro" como un hallazgo: es una propiedad de diseño de la especificación. Para el Harbor Loop Study la propiedad pertinente es que una respuesta que transporta un valor de nivel no tiene ningún campo que demuestre que procede del transmisor. Por eso la repetición es posible y por eso el trabajo mide la detección y no la prevención. Nombre los códigos de función que usa su modelo de atacante, para que el lector vea de qué partes de la especificación dependen los resultados.

### 2.3 Familias de detección

Los detectores de red observan paquetes; los detectores basados en la física observan si los valores de sensores y actuadores obedecen las leyes del proceso. Giraldo et al. revisaron estos últimos; Urbina et al. defendieron medir el impacto frente a un adversario sigiloso. Sommer y Paxson advirtieron que la detección de anomalías falla cuando lo "normal" es abierto; Arp et al. enumeraron errores de evaluación, entre ellos la puntuación con ajuste por puntos. Harbor Loop pertenece a la segunda familia: su CUSUM sobre el residuo compara la lectura de nivel con una estimación impulsada por el caudalímetro. Las advertencias de ambos artículos se aplican directamente. La operación normal de un lazo de agua es bastante cerrada, lo que ayuda, pero la puntuación debe usar episodios de ataque y no puntos, y la evaluación debe preguntar qué podría seguir haciendo un adversario sigiloso. La clase B es esa pregunta.

### 2.4 Evidencia de amenazas

MITRE ATT&CK for ICS enumera técnicas como *Modify Parameter* y *Spoof Reporting Message*. Los informes públicos sobre Stuxnet, los apagones de Ucrania de 2015 y TRITON/TRISIS muestran que la manipulación de la vista y el ataque a los sistemas de seguridad funcional son objetivos documentados de los adversarios. Úselos al nivel de los análisis públicos citados; no invente detalles operativos. Para el trabajo de fin de máster esta evidencia respalda una sola frase: manipular lo que ven los operadores es un objetivo documentado de los adversarios, de modo que probar la detección de una lectura de nivel repetida es pertinente. No respalda afirmaciones sobre la frecuencia con que las empresas de agua sufren repeticiones. Limite la cita a la técnica y al análisis público, y deje fuera del capítulo de antecedentes las afirmaciones de frecuencia.

### 2.5 Ejemplo resuelto: codificar una laguna

De doce estudios sintéticos L1–L12, solo dos informan el impacto en el momento de la detección, solo uno congela los umbrales antes de un segundo contexto y ninguno combina adversario consciente del detector + umbrales congelados + impacto + segunda planta. Laguna: *ninguna evaluación de la detección por residuos frente a la repetición de sensores informa la exhaustividad por eventos, el retardo y el sobrellenado en el momento de la alarma con umbrales congelados en dos contextos y una clase de atacante explícita de dos sensores.*

Escriba la laguna como una sola frase que nombre lo que falta y luego contraste cada palabra con la tabla codificada. Si un estudio sí combinara umbrales congelados y una segunda planta, la laguna se reduce y la frase debe cambiar. Una laguna construida a partir de una tabla de codificación puede auditarse; una laguna construida a partir de impresiones sobre el campo, no.

### 2.6 Errores comunes y límites

Citar normas como evidencia de que funcionan; tratar ATT&CK como tasas de base; reivindicar novedad a partir del nombre de un conjunto de datos nuevo. Estos errores comparten un patrón: confunden la existencia de un documento con la evidencia de un efecto. Una norma dice lo que debería hacerse; no demuestra que hacerlo reduzca el daño. ATT&CK enumera lo que se ha visto hacer a los adversarios, no con qué frecuencia. Un conjunto de datos nuevo es útil, pero la novedad debe venir de la pregunta que permite responder.

### Ejercicios — capítulo 2

- **EX008 — Mapa Purdue de Harbor Loop L1.** Asigne los componentes de Harbor Loop L1 a los niveles Purdue 0–3 y nombre dos conductos. *Rúbrica:* 3 = componentes L0–L3 + dos conductos (SCADA↔PLC, historiador↔SCADA); 2 = solo niveles; 1 = parcial; 0 = nada.
- **EX009 — Zona 62443 como hipótesis medible.** Reescriba una recomendación de zonas de 62443 como una hipótesis medible. *Rúbrica:* 3 = hipótesis medible de conducto de solo lectura con métrica de ≥90 %; 2 = hipótesis sin métrica; 1 = eslogan; 0 = nada.
- **EX010 — Autenticación en Modbus frente a DNP3-SA.** Compare Modbus y DNP3 Secure Authentication en cuanto a la presencia de autenticación usando solo las especificaciones públicas. *Rúbrica:* 3 = Modbus sin autenticación frente a los desafíos de DNP3-SA; presencia, no adopción; 2 = solo presencia; 1 = afirmación sobre adopción; 0 = nada.
- **EX011 — Techo para un estudio con F1 con ajuste por puntos.** Valore un estudio ficticio que informa un F1 con ajuste por puntos = 0.99 en un banco de pruebas; indique qué puede respaldar. *Rúbrica:* 3 = techo de respaldo solo para marcas de segmento; excluye retardo/impacto/generalización/adversario consciente; 2 = techo sin exclusiones; 1 = acepta el 0.99; 0 = nada.
- **EX012 — Dos técnicas de ATT&CK para Harbor Loop.** Seleccione dos técnicas de ATT&CK for ICS para Harbor Loop; explique por qué no son evidencia de frecuencia. *Rúbrica:* 3 = Spoof Reporting Message + Modify Parameter + no son frecuencia; 2 = técnicas sin salvedad; 1 = una; 0 = nada.
- **EX013 — Lagunas débil y fuerte de la detección por residuos.** Redacte enunciados de laguna débil y fuerte para la detección por residuos de la repetición de sensores. *Rúbrica:* 3 = laguna débil frente a fuerte que coincide en sustancia con §2.5; 2 = débil/fuerte sin detalle de TO; 1 = una; 0 = nada.
- **EX014 — Errores de Arp más un error de TO.** Enumere tres errores de evaluación de Arp et al. que se aplican a los detectores de TO y un error específico de TO. *Rúbrica:* 3 = tres errores de Arp + error de impacto en el momento de la detección de TO; 2 = solo Arp; 1 = un error; 0 = nada.

### Síntesis del capítulo

El seminario le da arquitectura, protocolos, familias de detección y evidencia de amenazas, y la disciplina para convertirlos en hipótesis y lagunas en lugar de eslóganes.

### Siga estudiando — capítulo 02 de 08

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](../../en/book/MANUSCRIPT.md#ch-03)

<a id="worked-results"></a>

## Resultados resueltos

### Capítulo 1
**EX001.** "En un lazo sintético de nivel Modbus/TCP, ¿reduce la activación de la protección contra escritura en los registros de punto de consigna los cambios no autorizados exitosos del punto de consigna en ≥90 % frente a una línea de base sin protección bajo una tormenta de escrituras guionizada, y rompe la protección la disponibilidad cuando la estación de ingeniería necesita escrituras legítimas?"
**EX002.** Control: generación de residuos, redundancia analítica, FDI basada en observadores, validación de sensores. Seguridad: inyección de datos falsos, suplantación de sensores, repetición (replay), manipulación de la vista, ADS basados en la física.
**EX003.** Incluir mediciones o revisiones revisadas por pares sobre detección o protocolos de ICS de 2010–2026; excluir el marketing de fabricantes sin método. Documento técnico del fabricante → excluir; medición de campo de DNP3 → incluir.
**EX004.** Ampersand: key() elimina los caracteres no alfanuméricos, de modo que un registro gris titulado "Sensor replay attacks on water-treatment testbeds" (2021) se colapsa con el registro de arXiv, pero "Modbus security: a survey of attacks & defenses" no coincide con el registro de IEEE, porque la palabra "and" sobrevive a la normalización mientras que "&" desaparece; convierta "&" en "and" antes de eliminar caracteres. Kappa se mueve cuando cambia una decisión porque la concordancia por azar depende de las tasas marginales.
**EX005.** Protocolo: IEEE/ACM/Scopus/arXiv 2010–2026; sinónimos del EX002; dos revisores; objetivo κ≥0.6 tras reparar los criterios; corriente gris separada.
**EX006.** El DOI identifica la misma obra entre variantes del título; la clave de título por sí sola conserva ambos duplicados "Survey" y "survey" cuando la puntuación difiere, salvo que se normalice: poner el DOI primero es más estricto.
**EX007.** Giraldo: revisión revisada por pares (alto para el encuadre). Aviso de CISA: evidencia de profesionales (medio para la existencia de problemas). Blog del fabricante: marketing (bajo; solo hipótesis).

### Capítulo 2
**EX008.** L0: tanque/bomba/sensores; L1: PLC; L2: SCADA; L3: historiador. Conductos: SCADA↔PLC (Modbus), historiador↔SCADA.
**EX009.** "Un conducto que solo permite los códigos de función Modbus 3/4 (lecturas) de L2 a L1 reduce en ≥90 % los equipos capaces de escribir puntos de consigna frente a una red plana, medido por alcanzabilidad sobre un inventario sintético."
**EX010.** Modbus Application Protocol: sin campos de autenticación. DNP3-SA: define desafíos de autenticación para las solicitudes críticas. La comparación trata de la presencia de un mecanismo, no de su adopción.
**EX011.** Respalda como máximo "el detector marcó ≥1 punto en estos segmentos en este banco de pruebas"; no el retardo, el impacto, la generalización ni el rendimiento frente a un adversario consciente.
**EX012.** Spoof Reporting Message; Modify Parameter. La matriz documenta técnicas, no tasas.
**EX013.** Débil: "La detección basada en la física necesita más estudio". Fuerte: el párrafo de la laguna de §2.5.
**EX014.** Arp: métricas inapropiadas, evaluación solo en laboratorio, fuga entre entrenamiento y prueba. Específico de TO: ignorar el impacto físico en el momento de la detección.

<a id="glossary"></a>

## Glosario

**ATT&CK for ICS.** Base de conocimiento de técnicas de MITRE sobre adversarios de control industrial; no es una distribución de frecuencias.

**Clase A / clase B (Harbor Loop).** La clase A suplanta un sensor mientras una medición independiente sigue siendo honesta; la clase B controla ambas de forma coherente y derrota un residuo de balance de masa.

**CUSUM.** Suma acumulada de Page (1954) aplicada a un residuo entre mediciones cableadas de forma independiente.

**Harbor Loop.** Caso conductor de la maestría: lazo de nivel Modbus/TCP sintético usado para delimitar el alcance, para los experimentos y para las afirmaciones dirigidas a los operadores.

**Manipulación de la vista.** Inyectar lecturas falsas para que los operadores o los detectores no perciban un estado del proceso que diverge.

**Menlo Report.** Principios de ética de la investigación en TIC del DHS (2012), usados al decidir qué detalle de evasión publicar.

**Rig R2.** Instalación de laboratorio aislada de bomba y tanque con válvula de flotador mecánica, bandeja de goteo y parada de emergencia con responsable designado; se usa como T2 para las comprobaciones con umbrales congelados.

**Niveles Purdue / zonas IEC 62443.** Vocabulario de arquitectura y segmentación para enunciar hipótesis medibles sobre conductos.

**F1 con ajuste por puntos.** Puntuación que acredita todo un segmento de ataque tras una sola alarma; oculta el retardo de detección.

**Residuo / detección basada en la física.** Detectores que comparan las mediciones del proceso con una relación física (por ejemplo, el balance de masa).

<a id="references"></a>

## Referencias

Enlaces comprobados el 13 de octubre de 2026; vuelva a verificar las ediciones antes de citarlas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- ACM. Artifact Review and Badging, Version 1.1. <https://www.acm.org/publications/policies/artifact-review-and-badging-current>
- Arp, D. et al. Dos and Don'ts of Machine Learning in Computer Security. USENIX Security 2022. <https://www.usenix.org/conference/usenixsecurity22/presentation/arp>
- CISA. Coordinated Vulnerability Disclosure Program. <https://www.cisa.gov/coordinated-vulnerability-disclosure-process>
- Giraldo, J. et al. A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. *ACM Computing Surveys* 51(4), 2018. <https://doi.org/10.1145/3203245>
- ISA. ISA/IEC 62443 series of standards (overview). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- iTrust, SUTD. Secure Water Treatment (SWaT) and related datasets (public page). <https://itrust.sutd.edu.sg/itrust-labs_datasets/>
- MITRE. ATT&CK for Industrial Control Systems. <https://attack.mitre.org/matrices/ics/>
- Modbus Organization. Modbus Application Protocol Specification V1.1b3. <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
- NIST SP 800-82 Rev. 3. Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Page, E. S. Continuous Inspection Schemes. *Biometrika* 41, 1954. <https://doi.org/10.1093/biomet/41.1-2.100>
- Sommer, R. and Paxson, V. Outside the Closed World: On Using Machine Learning for Network Intrusion Detection. IEEE S&P 2010. <https://doi.org/10.1109/SP.2010.25>
- Urbina, D. et al. Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS 2016. <https://doi.org/10.1145/2976749.2978388>
- U.S. DHS. The Menlo Report: Ethical Principles Guiding ICT Research (2012). <https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf>
