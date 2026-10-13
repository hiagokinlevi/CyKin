# Infraestructura crítica y seguridad sectorial: diseño de investigación aplicada y la tesis de maestría

- Idioma: español (`es`), edición en español neutro internacional; curso de maestría, dos años; aproximadamente 1200 horas de estudio planificado (curso 184 de 207 de la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–8 de 8 tienen texto didáctico escrito, los ejercicios EX001–EX050 y sus resultados resueltos correspondientes. Siguen abiertas la revisión independiente de la materia, la nueva verificación de las fuentes, la revisión de accesibilidad, la revisión lingüística y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: investigadores principiantes que conocen el campo por la práctica o por estudios anteriores y que ahora necesitan responder una pregunta acotada sobre la seguridad y la resiliencia de la infraestructura crítica —salud, energía, agua, transporte, comunicaciones, finanzas y servicios públicos— con evidencia que otra persona pueda comprobar. Conocimientos de entrada: el contenido previsto para los programas de [ingeniería](../../../../engineering-5-years/critical-sector-security/en/book/PLAN.md) o de [grado](../../../../bachelors-4-years/critical-sector-security/en/book/PLAN.md) de esta área (todavía esquemas en el momento de redactar), o experiencia profesional equivalente, además de estadística introductoria (medias, varianza, intervalos de confianza, regresión lineal) y la capacidad de ejecutar un script breve de Python.
- Relación con el curso doctoral: el [libro doctoral de esta área](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) pide al investigador que haga y defienda una contribución *original*: un método nuevo, validado de forma independiente, con un programa de publicaciones. Este libro de maestría pide algo distinto y anterior: **diseñar, pilotar y ejecutar bien un estudio empírico con revisión ética**, informar exactamente lo que puede y lo que no puede mostrar y defenderlo ante un tribunal. Donde el libro doctoral construye simulaciones y replica líneas base, este libro trabaja sobre todo con datos observacionales, diseños cuasiexperimentales y entrevistas, porque eso es a lo que pueden acceder la mayoría de los proyectos de maestría de este campo.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este curso es un plan educativo independiente. No es un programa de maestría acreditado, no otorga ningún título y no concede autorización para acceder, escanear, probar o estudiar ninguna infraestructura, operador, conjunto de datos o persona reales. Toda organización, región, hospital, persona, registro, conjunto de datos y resultado numérico de un ejemplo resuelto es **sintético**, salvo que una frase cite explícitamente una fuente pública. Nada de este libro es un procedimiento operativo para un hospital, una empresa de servicios o un servicio de emergencias reales, y nada en él es asesoramiento jurídico o clínico.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Lea los ocho capítulos en orden; juntos siguen una tesis de maestría desde la primera idea hasta la evaluación. El capítulo 1 convierte un tema en una pregunta respondible y construye una búsqueda bibliográfica documentada. El capítulo 2 es el seminario avanzado: recorre en qué se diferencian los sectores, qué evidencia existe para cada uno y cómo leer críticamente un artículo sectorial. El capítulo 3 elige un diseño, redacta la solicitud ética y organiza un proyecto reproducible antes de que llegue ningún dato. El capítulo 4 enumera las explicaciones que podrían producir los mismos datos que la hipótesis y construye las pruebas que las separan. El capítulo 5 redacta la propuesta y ejecuta un piloto cuya tarea es poner a prueba la viabilidad, no encontrar un efecto. El capítulo 6 recoge y analiza los datos, cuantitativos y cualitativos. El capítulo 7 redacta la tesis y sus limitaciones. El capítulo 8 prepara la evaluación independiente, la defensa oral y la difusión responsable de los resultados.

Cada capítulo contiene secciones didácticas, definiciones, un ejemplo resuelto, una actividad práctica con un laboratorio de Python sin conexión, una lista de errores habituales y límites, ejercicios numerados y una síntesis. Los laboratorios usan solo la biblioteca estándar de Python 3; no se necesitan acceso a la red, paquetes ni datos reales. Escriba su respuesta a cada ejercicio antes de abrir los [resultados resueltos](#worked-results). Muchos ejercicios tienen más de una respuesta defendible; el resultado resuelto muestra una y la rúbrica muestra lo que un evaluador premiaría.

Mantenga cuatro etiquetas en cada nota de investigación que escriba mientras estudia: **observación** (lo que registró una fuente identificada), **inferencia** (lo que usted concluye, con qué supuestos), **afirmación** (lo que pretende defender, con su alcance) y **decisión** (lo que alguien decidió hacer a causa de ello). La investigación sobre infraestructura añade una quinta: **consecuencia**, el efecto sobre las personas que dependen de un servicio. El error más común a nivel de maestría no es un cálculo equivocado; es un cálculo correcto unido a una afirmación más amplia de lo que el diseño puede sostener.

### Qué significa «investigación aplicada» en este nivel

Una tesis de maestría en este campo suele juzgarse por cuatro cosas: si la pregunta es clara y merece respuesta; si el diseño se ajusta a la pregunta y a los datos realmente disponibles; si el análisis se realizó con competencia y de forma reproducible; y si las conclusiones se mantienen dentro de la evidencia. La originalidad es bienvenida, pero no se exige en el sentido doctoral. Una replicación bien ejecutada de un diseño publicado en una región nueva, un estudio descriptivo cuidadoso de algo que nadie ha medido o un estudio de métodos mixtos que explica *por qué* ocurrió un efecto observado son todas contribuciones legítimas de maestría. Lo que no es aceptable es una tesis cuyas afirmaciones no puedan comprobarse, cuyos datos se obtuvieron sin la aprobación adecuada o cuya sección de limitaciones enumera debilidades sin decir en qué dirección sesgan la respuesta.

### La tesis sintética usada en este libro

El libro sigue un proyecto de maestría inventado, el **Estudio de Desbordamiento** (*Spillover Study*). Su pregunta, refinada en el capítulo 1, es: *cuando un sistema hospitalario se ve interrumpido por un ataque de ransomware y desvía ambulancias, ¿cuánto aumentan las llegadas de ambulancias y los tiempos de espera en los hospitales vecinos, y disminuye ese aumento con la distancia?* La pregunta se inspira en una línea real de trabajos publicados —[Dameff et al. (2023)](https://doi.org/10.1001/jamanetworkopen.2023.12270) informaron de un aumento del volumen, de las llegadas de ambulancias y de los tiempos de espera en los servicios de urgencias adyacentes a un sistema de salud sometido a un ataque de ransomware de un mes de duración en 2021—, pero todo lugar, organización, persona y número del Estudio de Desbordamiento es ficticio.

| Elemento sintético | Papel en el libro | Límite |
|---|---|---|
| **Tamsin Valley** — Kestrel Health (dos hospitales, atacados), Alder Point Hospital (AP, a 6 km), Brookfield Community Hospital (BF, 14 km), Calloway General (CG, 38 km), Tamsin Valley EMS, despacho del condado, Tamsin Valley Healthcare Coalition | Región de estudio. El día 0 es el inicio de un desvío de ambulancias de 21 días en Kestrel (capítulos 3–8). | Región inventada; ningún hospital, organismo, personal, paciente o registro reales. |
| **Wexmoor** — Wexmoor General (W1) y St. Aldric (W2) | Región de comparación no afectada con un patrón estacional similar (capítulos 3, 4, 6 y 8). | Inventada. |
| Registros de búsqueda con DOI que empiezan por `10.9999/syn` | Una exportación de búsqueda sintética para practicar la deduplicación y el cribado (capítulo 1). | Registros inventados; el prefijo no es de ninguna editorial real y no debe buscarse. |
| Entrevistados **I01–I10** | Jefes de servicios de urgencias, supervisores de EMS y personal de la coalición (capítulos 3, 5 y 6). | Inventados; en este libro no aparece ningún dato de seres humanos. |
| El candidato y el director | Las personas cuyas decisiones siguen los ejemplos resueltos. | Papeles inventados, no personas reales. |

Los laboratorios generan todos los datos a partir de números aleatorios con semilla impresos en el texto. Como los datos son sintéticos, el libro puede decirle algo que un estudio real nunca sabe: el efecto **verdadero** incorporado en el generador. Las llegadas de Alder Point se generaron con un aumento del 22 % durante el desvío, las de Brookfield con un 10 % y las de Calloway sin ninguno. Varios capítulos usan este privilegio para mostrar con qué frecuencia métodos honestos no detectan o describen mal un efecto real. Nunca presente un número de laboratorio como hallazgo sobre hospitales reales.

### Política de fuentes

Cada enunciado factual sobre una ley, una norma, un incidente público o un estudio publicado enlaza con una fuente que el autor consultó en octubre de 2026. Las leyes y las normas cambian; cada una se cita con su versión y su fecha y debe verificarse de nuevo antes de basarse en ella. Cuando un enunciado es vocabulario metodológico estándar —por ejemplo, que un intervalo de confianza describe la incertidumbre muestral bajo un modelo—, el texto lo dice en lugar de inventar una referencia. Una fuente respalda el enunciado general junto al que aparece, nunca los detalles del caso sintético. Los incidentes públicos se describen solo con el nivel de detalle que divulgaron sus editores y, cuando una evidencia posterior revisó un primer relato, se citan ambos. En esta edición, las referencias se mantienen idénticas a las de la edición en inglés y los títulos de las obras se citan en su idioma original.

## Contenido

1. [Pregunta de investigación y método de revisión de la literatura](#ch-01) — del tema a una pregunta respondible, alcance de la afirmación, búsqueda documentada entre disciplinas y en la literatura gris, deduplicación, cribado doble y la matriz de conceptos.
2. [Infraestructura crítica y seguridad sectorial: seminario avanzado](#ch-02) — perfiles sectoriales y unidades de consecuencia, lo que los catálogos públicos de incidentes pueden y no pueden decirle, lectura y presentación de un artículo sectorial y casos documentados cuyo primer relato fue revisado.
3. [Diseño del estudio, ética y reproducibilidad](../../en/book/MANUSCRIPT.md#ch-03) — elección entre diseños cuasiexperimentales y cualitativos, análisis del diseño antes de los datos, revisión ética, protección de datos y sensibilidad de la información de infraestructura, y un proyecto reproducible.
4. [Infraestructura crítica y seguridad sectorial: explicaciones rivales](../../en/book/MANUSCRIPT.md#ch-04) — múltiples hipótesis de trabajo, diagramas causales, regiones de comparación, controles negativos, pruebas placebo y dosis-respuesta como evidencia discriminante.
5. [Propuesta y piloto](../../en/book/MANUSCRIPT.md#ch-05) — la propuesta como contrato, cronograma y registro de riesgos, acuerdos de acceso a datos, pilotos de viabilidad con criterios de continuar o no continuar declarados de antemano y una auditoría de los datos del piloto.
6. [Recogida y análisis de datos](../../en/book/MANUSCRIPT.md#ch-06) — series temporales interrumpidas controladas con intervalos robustos a la autocorrelación, ventanas placebo, entrevistas y análisis temático, acuerdo entre codificadores e integración de las dos vertientes.
7. [Redacción de la tesis y limitaciones](../../en/book/MANUSCRIPT.md#ch-07) — estructura y argumento, comunicación honesta de los resultados, procedencia de los números, guías de comunicación, limitaciones direccionales, figuras accesibles y disponibilidad de datos bajo sensibilidad.
8. [Revisión independiente y defensa](../../en/book/MANUSCRIPT.md#ch-08) — cómo leen los evaluadores, curvas de especificación para preguntas de «¿y si...?», la defensa oral, las correcciones y la difusión responsable de los resultados con el sector.

Los [resultados resueltos](#worked-results) contienen EX001–EX050. Un [glosario](#glossary) y las [referencias](#references) cierran el libro.

<a id="ch-01"></a>

## Capítulo 1 — Pregunta de investigación y método de revisión de la literatura

### Resultados de aprendizaje y conexión

Al final de este capítulo, el estudiante será capaz de:

1. Pasar de un tema («ransomware en hospitales») a un problema y de ahí a una única pregunta de investigación respondible, y ponerla a prueba con los criterios FINER y con una versión de PICOT para infraestructura.
2. Clasificar una pregunta como descriptiva, de asociación, causal, explicativa o evaluativa, y enunciar el tipo de diseño y de afirmación que permite cada una.
3. Definir la cantidad que el estudio estimará —su **estimando**— con palabras lo bastante precisas como para que dos analistas calculen lo mismo.
4. Elegir un tipo de revisión (narrativa, exploratoria, sistemática) adecuado para una tesis de maestría y justificarlo.
5. Construir, ejecutar y documentar una búsqueda interdisciplinaria que incluya literatura gris, ponerla a prueba con elementos conocidos y detenerla según una regla declarada de antemano.
6. Deduplicar registros, cribarlos con dos revisores, medir el acuerdo con la kappa de Cohen, reparar los criterios de elegibilidad donde se concentra el desacuerdo y comunicar un diagrama de flujo.
7. Organizar lo encontrado en una matriz de conceptos en lugar de un resumen autor por autor.

El capítulo fija la pregunta y el mapa de la evidencia que usan todos los capítulos posteriores. El capítulo 2 amplía el mapa a los demás sectores; el capítulo 3 elige un diseño para la pregunta fijada aquí; el capítulo 4 enumera las explicaciones rivales que la literatura ya ha planteado; el capítulo 7 redacta el capítulo de revisión de la literatura a partir de la matriz de conceptos construida aquí.

### 1.1 Del tema al problema y a la pregunta

#### 1.1.1 Tres cosas distintas

La mayoría de las tesis empiezan con un **tema**, que es un área de interés: «ciberataques contra hospitales». Un tema no puede responderse. Un **problema** es una brecha entre lo que se sabe y lo que alguien necesita saber para actuar: «los planificadores regionales de emergencias no saben cuánto sobrecarga a sus vecinos un desvío inducido por un ciberataque en un hospital, de modo que los acuerdos de ayuda mutua se redactan sin números». Una **pregunta de investigación** es la pregunta concreta cuya respuesta reduciría esa brecha: «Durante un desvío de ambulancias inducido por ransomware, ¿cuánto cambian las llegadas diarias de ambulancias a los hospitales situados a menos de 40 km, en relación con lo que se habría esperado sin el desvío?».

El paso del tema a la pregunta es un estrechamiento, y cada estrechamiento es una decisión que usted debe poder defender. Estrechar a las *llegadas de ambulancias* en lugar de al «daño a los pacientes» cambia importancia por mensurabilidad. Estrechar a *una región* cambia generalidad por profundidad y acceso a los datos. Estrechar al *desvío inducido por ransomware* en lugar de a los «incidentes cibernéticos» hace observable la exposición: un desvío tiene un inicio y un fin que registra un organismo de servicios médicos de emergencia (EMS), mientras que «un incidente cibernético» puede ser desconocido incluso para el hospital durante semanas.

#### 1.1.2 FINER y un PICOT para infraestructura

Los investigadores clínicos ponen a prueba las preguntas con los criterios FINER —factible, interesante, novedosa, ética y relevante— y las estructuran con PICOT: población, intervención, comparación, resultado (*outcome*) y tiempo ([Farrugia et al., 2010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2912019/), que resumen *Designing Clinical Research* de Hulley y colaboradores). Ambos se trasladan a la investigación sobre infraestructura con un cambio: la mayoría de los estudios de infraestructura observan una **exposición** que el investigador no asignó, de modo que la «I» se convierte en «E».

| Elemento | Significado en la investigación sobre infraestructura | Estudio de Desbordamiento (primera versión) |
|---|---|---|
| **P**oblación / unidades | Las unidades que prestan el servicio estudiado: hospitales, servicios de urgencias, alimentadores, sistemas de agua, procesadores de pagos. Indique la unidad de análisis y la unidad de observación (pueden diferir: la unidad puede ser un hospital-día). | Servicios de urgencias (SU) de Tamsin Valley distintos de los de Kestrel; unidad de observación: el SU-día. |
| **E**xposición | El evento o la condición cuya consecuencia se estudia, definido de modo que su inicio y su fin sean observables. | Desvío de ambulancias en Kestrel causado por un ataque de ransomware (días 0–20). |
| **C**omparación | Con qué se compara lo que vivieron los expuestos: las mismas unidades antes, unidades no expuestas en el mismo periodo, o ambas. | Los mismos SU en los 180 días anteriores; los SU de Wexmoor en los mismos días. |
| Resultado (**O**utcome) | Una consecuencia medida en unidades de servicio. Nombre el resultado primario y, como mucho, unos pocos secundarios. | Primario: llegadas diarias de ambulancias. Secundario: mediana de minutos desde la llegada hasta el primer clínico. |
| **T**iempo | Ventana, seguimiento y resolución (por hora, diaria, mensual). | Diaria, del día −180 al día +89. |

FINER es un filtro, no una puntuación. **Factible** significa que los datos existen, que usted puede obtenerlos legalmente dentro del plazo del curso y que el análisis está dentro de su competencia. **Interesante** significa que a alguien que debe tomar una decisión le importa la respuesta. **Novedosa**, a nivel de maestría, incluye «medido por primera vez en este contexto» y «replicado con un diseño más sólido». **Ética** significa que un comité de revisión podría aprobarla (capítulo 3). **Relevante** significa que la respuesta cambiaría un plan, una política o un estudio posterior.

#### 1.1.3 Tipos de pregunta y las afirmaciones que permiten

| Tipo | Forma | Ejemplo | Lo que debe aportar el diseño | Afirmación más fuerte |
|---|---|---|---|---|
| Descriptiva | ¿Cuánto, con qué frecuencia, qué? | ¿Cuántas horas de desvío de ambulancias registraron el año pasado los SU de Tamsin Valley, por causa? | Una población definida y registros completos. | Una cantidad medida en esa población. |
| De asociación | ¿Está X asociado con Y? | ¿Son mayores las horas de desvío en los SU más cercanos a un hospital que desvía? | Variación en X e Y; ajuste por los factores de confusión evidentes. | Una asociación, con su tamaño y su incertidumbre. |
| Causal | ¿Cuánto cambió X a Y? | ¿Cuánto aumentó el desvío de Kestrel las llegadas a Alder Point? | Un contrafáctico creíble: lo que habría ocurrido sin X (capítulos 3–4). | Una estimación del efecto bajo supuestos enunciados. |
| Explicativa | ¿Por qué o cómo cambió X a Y? | ¿Mediante qué decisiones redistribuyeron los despachadores a los pacientes? | Evidencia de proceso: entrevistas, documentos, registros. | Un mecanismo respaldado por relatos convergentes. |
| Evaluativa | ¿Funcionó una medida? | ¿Acortó los tiempos de espera el protocolo de desvío de la coalición? | Un diseño causal más una definición operativa de «funcionar». | Un efecto de la medida, bajo supuestos. |

La pregunta primaria del Estudio de Desbordamiento es causal, y su pregunta secundaria, explicativa. Esa combinación —una estimación cuantitativa más un relato del mecanismo— es típica de una tesis de maestría sólida y es la razón por la que este libro enseña ambas vertientes.

### 1.2 El estimando: diga exactamente qué número producirá

Una pregunta formulada con palabras todavía deja lugar a muchos números distintos. «¿Cuánto aumentan las llegadas?» podría significar el aumento del primer día, el aumento medio durante el desvío, el aumento respecto al año pasado, el aumento respecto a una región de comparación o el total de pacientes adicionales. Un **estimando** es la cantidad precisa que un estudio pretende estimar, definida antes de ver los datos. Una plantilla útil tiene cinco partes:

1. **Unidades:** qué unidades y qué días (SU de Alder Point, días 0–20).
2. **Resultado:** qué se cuenta y cómo (llegadas de ambulancias por día natural, según el registro de llegadas del SU).
3. **Contraste:** comparado con qué (las llegadas que se habrían producido en ausencia del desvío).
4. **Resumen:** la escala (razón entre la media observada y la contrafáctica, comunicada como cambio porcentual).
5. **Población de inferencia:** sobre quién trata la respuesta (este SU durante este evento, no «los hospitales en general»).

El estimando primario del Estudio de Desbordamiento es, por tanto: *para cada SU vecino, el cambio porcentual en la media diaria de llegadas de ambulancias durante los días 0–20, en relación con las llegadas esperadas a partir de la tendencia previa al evento de ese mismo SU y del cambio simultáneo en los SU no afectados de Wexmoor.* El contrafáctico «se habrían producido» nunca se observa; los capítulos 3 y 4 deciden cómo aproximarlo. Escribir primero el estimando evita un fallo común: elegir la comparación después de ver cuál da el número más impresionante.

#### 1.2.1 Alcance de la afirmación

El [libro doctoral de esta área](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md#ch-01) describe una escalera de cinco peldaños desde la observación hasta la afirmación de investigación. A nivel de maestría, la disciplina esencial es más simple: **escriba la afirmación que espera hacer y el alcance que tendrá antes de empezar**, y compruebe al final si la evidencia la alcanzó. El Estudio de Desbordamiento espera afirmar: *«En un evento regional sintético, las llegadas de ambulancias al SU vecino más cercano aumentaron durante el desvío en una cantidad que estimamos con una incertidumbre enunciada, y el aumento fue menor en los SU más distantes».* No espera afirmar que el ransomware daña a los pacientes, que todas las regiones se comportan así ni que las políticas de desvío deban cambiar, aunque la discusión pueda sugerir qué estudios podrían respaldar esas afirmaciones más amplias.

### 1.3 Para qué sirve una revisión de la literatura

A nivel de maestría, la revisión tiene cuatro tareas: mostrar que la pregunta está abierta o que merece volver a plantearse; encontrar los **métodos y las medidas** que otros han usado, para que usted no los reinvente; encontrar las **explicaciones rivales** ya planteadas (capítulo 4); y situar el resultado final en su contexto. No es una bibliografía anotada ni una demostración de cuánto ha leído usted.

| Tipo de revisión | Propósito | Requisitos de método | Encaja en un proyecto de maestría cuando |
|---|---|---|---|
| Narrativa (tradicional) | Síntesis y argumentación expertas | Pocas reglas formales; riesgo de citación selectiva | La revisión respalda un estudio empírico primario y el campo es pequeño |
| Exploratoria (*scoping*) | Trazar la extensión, el alcance y la naturaleza de la evidencia; aclarar conceptos | Marco de [Arksey y O'Malley (2005)](https://doi.org/10.1080/1364557032000119616); comunicación según [PRISMA-ScR (Tricco et al., 2018)](https://doi.org/10.7326/M18-0850) | La literatura está dispersa entre disciplinas y la pregunta todavía se está perfilando |
| Sistemática | Responder una pregunta focalizada con búsqueda y valoración exhaustivas | Protocolo, cribado doble, riesgo de sesgo, comunicación según [PRISMA 2020](https://doi.org/10.1136/bmj.n71) | La revisión *es* la tesis y hay suficiente literatura para sintetizar |
| Integradora / semisistemática | Combinar tipos de estudio diversos en una síntesis conceptual | Búsqueda documentada con síntesis flexible ([Snyder, 2019](https://doi.org/10.1016/j.jbusres.2019.07.039)) | El campo mezcla trabajo empírico, técnico y de políticas |

Para el Estudio de Desbordamiento, la revisión es una **revisión exploratoria estructurada** que respalda un estudio empírico: búsqueda documentada, elegibilidad explícita, dos revisores sobre una muestra, un diagrama de flujo y una matriz de conceptos, pero sin puntuación formal del riesgo de sesgo ni metaanálisis, porque el puñado de estudios pertinentes usa diseños no comparables. Enuncie esta elección y su motivo en el capítulo de métodos; un lector nunca debería tener que adivinar si una revisión pretendía ser exhaustiva.

### 1.4 Buscar entre disciplinas

#### 1.4.1 Por qué la literatura sobre infraestructura está dispersa

La evidencia sobre la pregunta del desbordamiento está repartida entre la medicina de urgencias, la investigación en servicios de salud, la economía de la salud, la medicina de desastres, la seguridad de la información, la administración pública y la auditoría gubernamental. La misma idea recibe nombres distintos: «desvío de ambulancias», «saturación del SU», «oleada regional», «redistribución de pacientes», «radio de impacto». Las bases de datos de seguridad rara vez indexan las operaciones hospitalarias; las bases de datos médicas rara vez indexan las ponencias de congresos de seguridad; y parte de la evidencia más informativa —informes de auditoría, declaraciones de reguladores, informes posteriores a la acción, informes de ejercicios de coaliciones sanitarias— es **literatura gris** que ninguna base de datos bibliográfica indexa.

#### 1.4.2 Bloques de conceptos

Construya la búsqueda a partir de bloques de conceptos combinados con AND; dentro de cada bloque, sinónimos combinados con OR:

- **Bloque A — exposición cibernética:** ransomware OR cyberattack OR "cyber attack" OR "cyber incident" OR "IT outage" OR "downtime" OR "information system failure".
- **Bloque B — contexto:** hospital OR "emergency department" OR "health system" OR "health care delivery organization" OR EMS OR ambulance.
- **Bloque C — consecuencia regional:** diversion OR crowding OR "neighbouring" OR "neighboring" OR adjacent OR regional OR spillover OR "surge".

Incluir «downtime» e «IT outage» en el bloque A es una elección deliberada: las interrupciones no maliciosas producen efectos operativos similares y pueden aportar métodos y rivales (capítulo 4). Registre la elección; amplía el trabajo de cribado y debe manejarse mediante los criterios de elegibilidad.

#### 1.4.3 Fuentes y la prueba de los elementos conocidos

Busque en al menos un índice biomédico, un índice académico general y un índice de informática, además de un plan para la literatura gris: oficinas gubernamentales de auditoría, ministerios y organismos de salud, órganos de coordinación sectorial, asociaciones de hospitales e informes de coaliciones. Antes de ejecutar la búsqueda completa, reúna un **conjunto de elementos conocidos** —estudios que ya sabe que son pertinentes— y compruebe que su búsqueda los encuentra. Para la pregunta del desbordamiento, un conjunto razonable de elementos conocidos es [Dameff et al. (2023)](https://doi.org/10.1001/jamanetworkopen.2023.12270), [Ghafur et al. (2019)](https://doi.org/10.1038/s41746-019-0161-6) sobre WannaCry en el NHS de Inglaterra y [Neprash et al. (2022)](https://doi.org/10.1001/jamahealthforum.2022.4873) sobre las tendencias del ransomware en las organizaciones prestadoras de atención sanitaria de EE. UU. Una búsqueda que no encuentra un elemento conocido es demasiado estrecha; revísela y registre la revisión.

#### 1.4.4 Encadenamiento de citas y detención

Las búsquedas en bases de datos no encuentran los artículos que usan un vocabulario inesperado. El **encadenamiento hacia atrás** lee las listas de referencias de los estudios incluidos; el **encadenamiento hacia delante** encuentra artículos posteriores que los citan. [Wohlin (2014)](https://doi.org/10.1145/2601248.2601268) ofrece pautas para esta «bola de nieve» y muestra que, en algunos campos, puede complementar o sustituir la búsqueda en bases de datos. Decida de antemano cuándo detenerse: por ejemplo, *tras dos rondas consecutivas de encadenamiento que no añadan ningún estudio incluido*. Anote cada búsqueda en un **registro de búsqueda**: fecha, fuente, cadena exacta, filtros, número de resultados y quién la ejecutó.

### 1.5 De los registros a los estudios incluidos

#### 1.5.1 Deduplicación

El mismo artículo aparece en varias bases de datos, con distintas mayúsculas, puntuación y guiones y, a veces, sin DOI. Deduplique antes del cribado, para que dos revisores no criben el mismo estudio dos veces y el diagrama de flujo sea honesto. Un procedimiento sólido en dos pasadas es: (1) emparejar los DOI exactos tras pasarlos a minúsculas; (2) emparejar, entre los restantes, títulos normalizados más el año: minúsculas, sin puntuación, espacios colapsados y variantes conocidas normalizadas (por ejemplo, «turn-around» y «turnaround»). En un proyecto pequeño, inspeccione a ojo cada coincidencia automática; las reglas automáticas pueden fusionar artículos distintos con títulos genéricos («Editorial», «Corrección»).

#### 1.5.2 Cribado en dos etapas y acuerdo

Cribe títulos y resúmenes según los criterios de elegibilidad y lea después el texto completo de todo lo que los supere. A nivel de maestría, a menudo dos revisores no pueden cribarlo todo; un compromiso defendible es que un segundo revisor (un compañero o el director) cribe de forma independiente una muestra, que se mida el acuerdo, que se reparen los criterios donde se concentra el desacuerdo y que el primer revisor cribe después el resto con los criterios reparados. El acuerdo se mide con la **kappa de Cohen** ([Cohen, 1960](https://doi.org/10.1177/001316446002000104)), que corrige el acuerdo observado *p*ₒ por el acuerdo *p*ₑ esperado por azar a partir de la tasa de inclusión de cada revisor: κ = (*p*ₒ − *p*ₑ) / (1 − *p*ₑ). Dos revisores que incluyen cada uno la mitad de los registros coincidirían la mitad de las veces solo por azar, de modo que un acuerdo bruto del 80 % puede ser poco impresionante. Las bandas de interpretación varían, y [McHugh (2012)](https://doi.org/10.11613/BM.2012.031) sostiene que las bandas que se citan habitualmente son demasiado indulgentes para la investigación en salud, donde un acuerdo bajo significa datos poco fiables. Trate la kappa como un diagnóstico: **dónde** discrepan los revisores le dice qué criterio no está claro.

#### 1.5.3 El diagrama de flujo

Comunique los registros identificados por fuente, los duplicados eliminados, los registros cribados, los registros excluidos, los textos completos evaluados, los textos completos excluidos *con sus motivos* y los estudios incluidos. PRISMA 2020 ofrece un diagrama de flujo estándar ([Page et al., 2021](https://doi.org/10.1136/bmj.n71)). Incluso una revisión no sistemática se beneficia de él, porque permite al evaluador ver el denominador que hay detrás de «la literatura muestra».

### 1.6 Síntesis por concepto, no por autor

[Webster y Watson (2002)](https://www.jstor.org/stable/4132319) recomendaron que las revisiones fueran **centradas en conceptos** y no en autores: en lugar de un párrafo por artículo («Smith encontró…; Jones encontró…»), organice la revisión en torno a los conceptos que necesita la pregunta y muestre qué estudios informan cada uno. Una **matriz de conceptos** tiene los estudios como filas y los conceptos como columnas. Para el Estudio de Desbordamiento, las columnas son: unidad de análisis; definición de la exposición; comparación; resultado; diseño; lo que el estudio puede respaldar; rivales que plantea.

| Estudio | Unidad | Exposición | Comparación | Resultados pertinentes para el desbordamiento | Diseño (según la publicación) | Lo que puede respaldar |
|---|---|---|---|---|---|---|
| [Dameff et al., 2023](https://doi.org/10.1001/jamanetworkopen.2023.12270) | Dos SU adyacentes a una organización atacada | Ataque de ransomware de un mes contra cuatro hospitales adyacentes (mayo de 2021) | Los mismos SU en las cuatro semanas anteriores y posteriores | Censo, llegadas de ambulancias, tiempos de espera, abandonos sin ser atendido, duración de la estancia, desvío de EMS del condado, indicadores de ictus | Cohorte antes-después | Una asociación entre el periodo del ataque y la carga en los SU vecinos de una región |
| [Ghafur et al., 2019](https://doi.org/10.1038/s41746-019-0161-6) | *Trusts* del NHS de Inglaterra | WannaCry (mayo de 2017) | Semanas de referencia; *trusts* infectados frente a no infectados | Ingresos, atenciones en urgencias (A&E), cancelaciones de consultas externas, muertes en A&E | Análisis retrospectivo de las Hospital Episode Statistics | Reducciones de actividad en los *trusts* infectados; ningún cambio detectable en las muertes en A&E (una medida tosca del daño, como señalan los autores) |
| [Neprash et al., 2022](https://doi.org/10.1001/jamahealthforum.2022.4873) | Organizaciones prestadoras de atención sanitaria de EE. UU. | Ataques de ransomware en una base de datos construida a partir de informes públicos, 2016–2021 | Tendencias temporales | Frecuencia, exposición de información sanitaria protegida (PHI), interrupción operativa, incluido el desvío de ambulancias | Cohorte de ataques reportados | Tendencias y características de los ataques *reportados* |

La matriz hace visible la brecha: un estudio antes-después de SU vecinos, ningún estudio con una región de comparación no afectada y ningún estudio sobre si la carga disminuye con la distancia. Esa es la justificación del Estudio de Desbordamiento.

### 1.7 Leer un estudio por su diseño, no solo por sus hallazgos

Cuando extraiga un estudio, registre no solo lo que encontró, sino lo que **podría** haber encontrado. Pregúntese: ¿cuál es la unidad? ¿Está definida la exposición por su inicio y su fin? ¿Cuál es la comparación y qué más cambió entre los periodos comparados? ¿Es el resultado una consecuencia (pacientes retrasados) o una actividad (visitas contadas)? ¿A qué población podría generalizarse el resultado? Una comparación antes-después dentro de las mismas unidades, por ejemplo, no puede separar la exposición de cualquier otra cosa que cambiara al mismo tiempo: la estación, una política, la dotación de personal, una epidemia simultánea. Decirlo no es una crítica a los autores; es la evidencia que su propio diseño debe mejorar.

### 1.8 Ejemplo resuelto: del tema a la pregunta del desbordamiento (sintético)

El primer párrafo de la propuesta del candidato decía: *«Esta tesis investigará el impacto de los ciberataques en los hospitales y mostrará que ponen en peligro a los pacientes en toda la región».* La revisión del director:

| Problema | Por qué falla | Revisión |
|---|---|---|
| «Investigar el impacto de los ciberataques en los hospitales» | Un tema, no una pregunta; «impacto» no está definido. | Nombrar el resultado: llegadas diarias de ambulancias y tiempo de espera en los SU vecinos. |
| «Mostrar que ponen en peligro a los pacientes» | Presupone la respuesta; un diseño para «mostrar» no puede fallar. | Preguntar «cuánto» y admitir el cero como respuesta. |
| «En toda la región» | Sin unidad ni límite. | SU situados a menos de 40 km del sistema atacado; la distancia como moderador. |
| «Ciberataques» | Exposición no observable ni fechada. | Desvío de ambulancias causado por un ataque de ransomware, con inicio y fin registrados por el EMS. |
| Sin comparación | Un antes-después por sí solo no puede separar el ataque de la estación. | Añadir una región de comparación no afectada. |
| Sin mecanismo | Incluso un número creíble no diría a los planificadores qué cambiar. | Pregunta explicativa secundaria con entrevistas al personal de los SU, del EMS y de la coalición. |
| «Se pone en peligro a los pacientes» | Los resultados en pacientes requieren datos clínicos y aprobaciones que exceden el calendario de una maestría. | Dejar los resultados en pacientes fuera del alcance; nombrarlos como trabajo futuro. |

Preguntas finales:

- **PI1 (causal):** Durante un desvío de ambulancias inducido por ransomware en un sistema hospitalario, ¿en qué porcentaje cambian las llegadas diarias de ambulancias a cada SU vecino en relación con el contrafáctico estimado a partir de su propia tendencia previa al evento y de una región de comparación no afectada?
- **PI2 (de asociación):** ¿Disminuye ese cambio con la distancia al sistema que desvía?
- **PI3 (explicativa):** Según los jefes de los SU, los supervisores del EMS y el personal de la coalición, ¿mediante qué decisiones y restricciones se redistribuyó la carga?

### 1.9 Actividad práctica: deduplicar, cribar y medir el acuerdo

El siguiente laboratorio contiene una exportación sintética de 20 registros procedentes de tres bases de datos y de una búsqueda de literatura gris. Los deduplica en dos pasadas, toma las decisiones de dos revisores sobre título y resumen para los registros restantes, calcula la kappa y enumera los desacuerdos. Ejecútelo con Python 3; no se necesitan paquetes.

```python
# Lab 1 - deduplicate a synthetic search export, measure screening agreement, count the flow (offline)
# Each record: (source, title, year, doi_or_empty). Decisions: reviewer A and B, I = include, X = exclude.
import re

RECORDS = [
    ("medline", "Ransomware and emergency department crowding at neighbouring hospitals", 2023, "10.9999/syn.001"),
    ("scopus",  "Ransomware and Emergency Department Crowding at Neighbouring Hospitals.", 2023, "10.9999/SYN.001"),
    ("ieee",    "Anomaly detection for water distribution SCADA", 2019, "10.9999/syn.002"),
    ("medline", "Hospital IT downtime and laboratory turnaround times", 2021, ""),
    ("scopus",  "Hospital IT downtime and laboratory turn-around times", 2021, "10.9999/syn.003"),
    ("grey",    "After-action report: regional EMS diversion during a hospital network outage", 2022, ""),
    ("scopus",  "Ambulance diversion policies and patient outcomes: a review", 2018, "10.9999/syn.004"),
    ("medline", "Ambulance diversion policies and patient outcomes - a review", 2018, ""),
    ("ieee",    "Cyber-physical attack graphs for substations", 2020, "10.9999/syn.005"),
    ("grey",    "State health department memo on downtime procedures", 2024, ""),
    ("scopus",  "Interrupted time series of ED arrivals after hospital closure", 2017, "10.9999/syn.006"),
    ("medline", "Mortality after hospital cyberattacks in Medicare beneficiaries", 2024, "10.9999/syn.007"),
    ("scopus",  "Mortality after hospital cyberattacks in Medicare beneficiaries", 2024, "10.9999/syn.007"),
    ("ieee",    "A survey of ransomware families 2015-2022", 2022, "10.9999/syn.008"),
    ("grey",    "Regional healthcare coalition cyber-incident exercise report", 2023, ""),
    ("medline", "Stroke care times during regional diversion", 2020, "10.9999/syn.009"),
    ("scopus",  "Electronic health record downtime: a scoping review", 2022, "10.9999/syn.010"),
    ("medline", "Electronic Health Record Downtime: A Scoping Review", 2022, "10.9999/syn.010"),
    ("ieee",    "Blockchain for hospital supply chains", 2021, "10.9999/syn.011"),
    ("grey",    "Vendor white paper: ransomware readiness in hospitals", 2023, ""),
]

def norm_title(t):
    t = t.lower().replace("turn-around", "turnaround")
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return " ".join(t.split())

def key(rec):
    _, title, year, doi = rec
    return ("doi", doi.lower()) if doi else ("ty", norm_title(title), year)

seen, unique, dup = {}, [], 0
for rec in RECORDS:                       # pass 1: DOI or title+year
    k = key(rec)
    if k in seen:
        dup += 1
        continue
    seen[k] = rec
    unique.append(rec)
by_title = {}
final = []
for rec in unique:                        # pass 2: same normalized title+year, one record lacks a DOI
    tk = (norm_title(rec[1]), rec[2])
    if tk in by_title:
        dup += 1
        continue
    by_title[tk] = rec
    final.append(rec)

# Title/abstract screening decisions by two reviewers, in the order of `final`
A = "I X I I I X X I I X I I I X X".split()
B = "I X I I I X I I I X X I I X I".split()

def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return po, pe, (po - pe) / (1 - pe)

po, pe, k = kappa(A, B)
both = sum(x == y == "I" for x, y in zip(A, B))
disagree = [final[i][1] for i in range(len(final)) if A[i] != B[i]]
print(f"records identified: {len(RECORDS)}  duplicates removed: {dup}  screened: {len(final)}")
print(f"agreement po={po:.3f} pe={pe:.3f} kappa={k:.3f}")
print(f"both include: {both}  disagreements: {len(disagree)}")
for t in disagree:
    print("  resolve:", t)
```

Salida esperada:

```text
records identified: 20  duplicates removed: 5  screened: 15
agreement po=0.800 pe=0.533 kappa=0.571
both include: 8  disagreements: 3
  resolve: State health department memo on downtime procedures
  resolve: Regional healthcare coalition cyber-incident exercise report
  resolve: Vendor white paper: ransomware readiness in hospitals
```

Se eliminaron cinco duplicados: tres por DOI (uno con un DOI escrito con otras mayúsculas) y dos por título normalizado y año, entre ellos un par que solo se diferenciaba por «turn-around» frente a «turnaround» y otro que solo se diferenciaba por una raya frente a dos puntos. El acuerdo bruto sobre los 15 registros cribados es del 80 %, pero el acuerdo por azar es del 53 %, de modo que κ = 0,571: moderado, en el mejor de los casos. El valor diagnóstico está en la lista: **los tres desacuerdos son literatura gris** (un memorando de un departamento de salud, un informe de ejercicio de una coalición y un libro blanco de un proveedor). Los criterios no decían nada sobre la literatura gris. Repárelos antes de continuar el cribado: por ejemplo, incluya los informes gubernamentales, de reguladores, de coaliciones y posteriores a la acción que describan los efectos operativos de un evento concreto; excluya el marketing de proveedores y los documentos que describen procedimientos sin comunicar efectos. Después, vuelva a cribar la muestra y recalcule la kappa.

### 1.10 Errores habituales y límites

- Empezar con una conclusión («mostrar que…») en lugar de con una pregunta cuya respuesta puede salir en cualquier sentido.
- Plantear una pregunta causal con un diseño que solo puede describir.
- Dejar el estimando sin definir hasta el análisis y elegir entonces la comparación que da el mayor efecto.
- Buscar en la base de datos de una sola disciplina y llamar al resultado «la literatura».
- Ignorar la literatura gris en un campo donde las auditorías, las declaraciones de reguladores y los informes posteriores a la acción contienen gran parte de la evidencia, o incluirla sin criterios.
- Comunicar el acuerdo bruto sin corregirlo por el azar, o comunicar la kappa sin examinar dónde está el desacuerdo.
- Redactar la revisión autor por autor en lugar de concepto por concepto.
- Tratar el hallazgo de un estudio como transferible sin registrar su unidad, su comparación y su contexto.

El límite de una revisión de maestría es el tiempo: no será exhaustiva y no debe fingir serlo. Su credibilidad proviene de una búsqueda documentada y repetible y de una declaración honesta de lo que no se buscó.

### Ejercicios — capítulo 1

**EX001 — Del tema a la pregunta.** *Objetivo:* estrechar un tema hasta una pregunta respondible. *Entradas:* el tema «incidentes cibernéticos en empresas de agua potable». *Restricciones:* una pregunta primaria; una exposición observable y fechada; un resultado en unidades de servicio. *Pasos:* (1) enuncie un problema al que se enfrenta quien toma decisiones; (2) escriba una pregunta en forma de PICOT para infraestructura; (3) póngala a prueba con cada criterio FINER en una frase; (4) enuncie la afirmación que espera hacer y su alcance. *Evidencia esperada:* un memorando de media página. *Rúbrica:* 3 = pregunta respondible con datos plausibles, exposición y resultado observables, FINER aplicado con honestidad (incluido lo que no es factible), afirmación acotada al diseño; 2 = un elemento vago; 1 = sigue siendo un tema; 0 = nada.

**EX002 — Tipos de pregunta.** *Objetivo:* asociar preguntas con diseños y afirmaciones. *Entradas:* (a) «¿Cuántas horas de desvío de ambulancias se registraron en el condado en 2024, por causa?» (b) «¿Tienen tiempos de espera más cortos durante las interrupciones informáticas los SU que adoptaron simulacros de funcionamiento sin sistemas?» (c) «¿Cuánto aumentó el desvío las llegadas a Alder Point?» (d) «¿Por qué los despachadores enviaron a los pacientes con ictus más allá del hospital abierto más cercano?» (e) «¿Redujo el nuevo protocolo de desvío de la coalición el tiempo en desvío?» *Restricciones:* use la tabla del §1.1.3. *Pasos:* clasifique cada una; nombre el diseño mínimo; nombre la afirmación más fuerte. *Evidencia esperada:* tabla. *Rúbrica:* 3 = todas clasificadas correctamente con diseños que realmente respaldarían las afirmaciones, y (b) reconocida como de asociación salvo que la adopción de simulacros pueda tratarse como una exposición con un contrafáctico creíble; 2 = un error; 1 = diseños genéricos; 0 = nada.

**EX003 — Estrategia de búsqueda y prueba de los elementos conocidos.** *Objetivo:* construir una búsqueda documentada e interdisciplinaria. *Entradas:* PI1–PI3 del §1.8. *Restricciones:* tres bloques de conceptos; al menos tres fuentes bibliográficas de disciplinas distintas y un plan de literatura gris con al menos cuatro tipos de fuente. *Pasos:* (1) escriba los bloques; (2) enumere las fuentes y justifique cada una; (3) defina un conjunto de tres elementos conocidos y describa cómo comprobaría que se recupera cada uno; (4) defina una regla de detención para el encadenamiento de citas; (5) diseñe una plantilla de registro de búsqueda. *Evidencia esperada:* protocolo de una página y plantilla de registro. *Rúbrica:* 3 = bloques con sinónimos de varias disciplinas, literatura gris especificada por tipo de fuente, prueba de elementos conocidos y regla de detención concretas; 2 = falta un elemento; 1 = búsqueda de una sola disciplina; 0 = nada.

**EX004 — Deduplicación y acuerdo.** *Objetivo:* comprobar si la deduplicación por título detecta un registro casi duplicado de literatura gris y ver cómo mueve la kappa de Cohen un único desacuerdo entre revisores. *Entradas:* el código del laboratorio 1. *Restricciones:* sin conexión. *Pasos:* (1) ejecute el laboratorio y anote la salida; (2) añada un registro `("grey", "Ransomware & emergency department crowding at neighbouring hospitals", 2023, "")` al final de `RECORDS`, agregue `I` a las cadenas de decisiones de ambos revisores (el registro solo llega al cribado si la deduplicación no lo detecta), vuelva a ejecutarlo e informe si el procedimiento de dos pasadas lo eliminó y por qué; (3) cambie la decisión del revisor B sobre «Cyber-physical attack graphs for substations» de X a I e informe la nueva kappa; (4) explique en 100 palabras por qué un desacuerdo adicional cambia la kappa más de lo que sugiere el acuerdo bruto. *Evidencia esperada:* salidas y explicación. *Rúbrica:* 3 = salidas correctas, fallo del signo «&» diagnosticado con una corrección propuesta, kappa recalculada correctamente, corrección por azar explicada; 2 = un error; 1 = no ejecutado; 0 = nada.

**EX005 — Reparar los criterios de elegibilidad.** *Objetivo:* convertir el desacuerdo en criterios más claros. *Entradas:* los tres desacuerdos del laboratorio 1. *Restricciones:* los criterios deben poder decidirse a partir de un título y un resumen o de la primera página de un informe. *Pasos:* (1) escriba criterios de inclusión y exclusión para la literatura gris; (2) aplíquelos a los tres registros; (3) indique qué haría con un registro que todavía no puede decidir. *Evidencia esperada:* criterios y decisiones. *Rúbrica:* 3 = criterios decidibles, decisiones coherentes, registros indecidibles enviados a revisión del texto completo en lugar de excluidos; 2 = una decisión incoherente; 1 = los criterios repiten el tema; 0 = nada.

**EX006 — Matriz de conceptos.** *Objetivo:* sintetizar por concepto. *Entradas:* los tres estudios del §1.6 más el [informe de la NAO sobre WannaCry y el NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/) (octubre de 2017). *Restricciones:* lea usted mismo el resumen de la NAO; cite los números con su fuente. *Pasos:* (1) añada el informe de la NAO como fila; (2) añada una columna «rivales que el estudio plantea o deja abiertos»; (3) escriba un párrafo de 200 palabras centrado en conceptos sobre «efectos regionales de los incidentes cibernéticos en hospitales». *Evidencia esperada:* matriz y párrafo. *Rúbrica:* 3 = fila de la NAO exacta (alcance de la interrupción y la distinción entre cancelaciones registradas y estimadas), rivales concretos, párrafo organizado por concepto; 2 = párrafo autor por autor; 1 = números sin fuente; 0 = nada.

**EX007 — Memorando de estimando y alcance.** *Objetivo:* definir exactamente lo que se estimará. *Entradas:* PI1 y PI2. *Restricciones:* la plantilla de cinco partes del §1.2. *Pasos:* (1) escriba el estimando de PI1; (2) escriba uno para PI2; (3) enumere dos estimandos que un analista descuidado podría calcular en su lugar y por qué difieren; (4) enuncie la afirmación que se espera hacer y las afirmaciones explícitamente fuera del alcance. *Evidencia esperada:* una página. *Rúbrica:* 3 = estimandos inequívocos con un contraste contrafáctico, alternativas realmente distintas (por ejemplo, aumento del primer día, aumento frente al año pasado), afirmaciones fuera del alcance explícitas; 2 = un estimando ambiguo; 1 = sin contraste; 0 = nada.

### Síntesis del capítulo

Una tesis se sostiene sobre su pregunta. Pase del tema al problema y a la pregunta de forma deliberada, haciendo defendible cada estrechamiento; ponga a prueba la pregunta con FINER y escríbala en una forma de PICOT para infraestructura con una exposición observable y un resultado de consecuencia. Clasifique la pregunta, porque su tipo decide el diseño y la afirmación más fuerte disponible. Defina el estimando antes de ver los datos. Elija un tipo de revisión que se ajuste al proyecto y dígalo. Busque entre disciplinas y en la literatura gris, ponga a prueba la búsqueda con elementos conocidos, encadene citas hasta un punto de detención declarado de antemano y regístrelo todo. Deduplique, cribe con un segundo revisor al menos sobre una muestra, use la kappa como diagnóstico de criterios poco claros y comunique el flujo. Sintetice por concepto: la matriz de conceptos muestra tanto lo que se sabe como la brecha que su estudio llenará.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 08

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Infraestructura crítica y seguridad sectorial: seminario avanzado

### Resultados de aprendizaje y conexión

Al final de este capítulo, el estudiante será capaz de:

1. Describir, para cada sector principal, su unidad de consecuencia característica, sus reservas, los instrumentos que lo rigen y la evidencia que un investigador de maestría puede obtener de forma realista.
2. Distinguir las **cascadas de dependencias** (un proveedor falla y sus dependientes fallan cuando se agotan sus reservas) del **desbordamiento por transferencia de carga** (los pares absorben la demanda de una unidad que falló), y reconocer cuál mide un estudio.
3. Tratar los catálogos públicos de incidentes como datos con un proceso de selección y cuantificar cómo una divulgación que aumenta con la gravedad infla la gravedad aparente y cómo un cambio en las reglas de notificación crea una tendencia espuria.
4. Codificar incidentes cuyo primer relato público se revisó después, sin repetir el primer relato ni borrarlo.
5. Leer un artículo sectorial con un protocolo crítico fijo y presentarlo en un seminario de modo que la discusión trate de la evidencia y no de opiniones.

Este capítulo amplía el mapa de la evidencia construido en el capítulo 1 de un sector al campo entero. El [capítulo sobre la frontera de la investigación](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md#ch-02) del libro doctoral recorre las normas como hipótesis y las familias de modelos de interdependencia; este seminario no repite ese recorrido. Se concentra en lo que necesita un investigador principiante: en qué se diferencian los sectores en las consecuencias que producen y en la evidencia que dejan, cómo leer la evidencia que existe y cómo discutirla con los pares.

### 2.1 Para qué sirve el seminario

Un seminario de investigación entrena tres hábitos que una tesis necesita y que las clases magistrales no entrenan: leer un artículo por lo que puede respaldar, presentar con justicia el trabajo de otra persona antes de criticarlo y aceptar la crítica de la propia lectura. Cada sesión de este curso sigue el mismo protocolo, que usted reutilizará al redactar la revisión de la literatura del capítulo 7:

1. **Afirmación.** ¿Qué afirma el artículo y con qué alcance? Cite la frase.
2. **Evidencia.** ¿Qué datos, de qué unidades y durante qué periodo?
3. **Garantía.** ¿Por qué esa evidencia respalda esa afirmación? ¿Qué lógica de diseño las conecta?
4. **Rivales.** ¿Qué otra cosa podría haber producido la misma evidencia? ¿Qué rivales aborda el artículo y cómo?
5. **Transferencia.** ¿A qué otras unidades, sectores o jurisdicciones podría aplicarse el resultado y en qué condiciones?
6. **Y qué.** ¿Qué decisión o estudio posterior informa?
7. **Siguiente estudio.** ¿Qué estudio reduciría más la incertidumbre restante?

El presentador responde las preguntas 1–3 y 5–6 en los términos del propio artículo y abre después la 4 y la 7 al grupo. La crítica de un artículo publicado no es un veredicto sobre sus autores; la mayoría de las limitaciones se derivan de los datos que existían.

### 2.2 Perfiles sectoriales

Los sectores se diferencian en lo que se pierde, con qué rapidez y para quién, en quién los regula y en qué evidencia llega al registro público. Los siguientes perfiles son un punto de partida; cada instrumento se cita con su versión y su fecha y debe verificarse de nuevo antes de basarse en él.

| Sector | Unidad de consecuencia típica | Reservas principales | Ejemplos de instrumentos que lo rigen | Evidencia que un estudiante de maestría suele poder obtener | Caso público tratado en este libro |
|---|---|---|---|---|---|
| Salud | Pacientes retrasados, desviados o dañados; procedimientos y citas aplazados | Procedimientos de funcionamiento sin sistemas, registros en papel, personal, ayuda mutua regional, capacidad de otros hospitales | Los [HPH Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html) de EE. UU. (voluntarios, enero de 2024); la salud es un sector de [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/) en la UE | Datos agregados de actividad (con aprobación), declaraciones públicas, auditorías, entrevistas | Dameff et al. (2023); WannaCry y el NHS; Synnovis (2024); Change Healthcare (2024) |
| Energía — electricidad | Clientes y horas-cliente sin suministro; cargas críticas perdidas | Generadores, almacenamiento, operación manual, maniobras de conmutación | [Normas NERC CIP](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx) (obligatorias para el sistema eléctrico de transmisión de América del Norte); sector energético de NIS2 | Estadísticas de interrupciones, informes públicos posteriores a la acción; rara vez datos operativos | Ucrania 2015 (véase el libro doctoral, capítulo 1) |
| Energía — petróleo y gas, oleoductos | Producto no entregado; escasez de suministro | Inventarios, transporte alternativo | Directivas de seguridad de oleoductos emitidas por la Transportation Security Administration de EE. UU. tras Colonial Pipeline, según describe [CISA (2023)](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years) | Cronologías públicas, informes de situación de organismos energéticos, datos de precios y suministro | Colonial Pipeline (2021) |
| Agua | Personas sin agua segura o sin presión; avisos emitidos | Almacenamiento, dosificación manual, interconexiones | La [America's Water Infrastructure Act of 2018](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans) de EE. UU., que exige a los sistemas comunitarios de agua que abastecen a más de 3300 personas completar evaluaciones de riesgo y resiliencia y planes de respuesta a emergencias | Avisos, resúmenes de reguladores, encuestas a empresas pequeñas | Oldsmar (2021) y su revisión posterior |
| Finanzas | Transacciones no procesadas; liquidación retrasada; clientes que no pueden pagar | Procesamiento manual, sitios de respaldo, canales de pago alternativos | El [Reglamento de Resiliencia Operativa Digital de la UE, Reglamento (UE) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj); la [guía CPMI–IOSCO](https://www.bis.org/cpmi/publ/d146.htm) (junio de 2016) para las infraestructuras del mercado financiero | Publicaciones de supervisión, estadísticas agregadas; casi nunca datos de empresas | La interrupción de pagos y reclamaciones de Change Healthcare (2024), donde se encuentran la salud y las finanzas |
| Comunicaciones y TI compartida | Usuarios u organizaciones sin servicio; servicios dependientes degradados | Enlaces redundantes, procedimientos de contingencia | Reglas de telecomunicaciones específicas del sector; los [CPG de CISA](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals), intersectoriales | Declaraciones de proveedores, informes de interrupciones | La actualización defectuosa de software de seguridad de julio de 2024 (no maliciosa) |
| Servicios públicos y de emergencia | Llamadas no atendidas, respuestas retrasadas | Centros de despacho vecinos, despacho manual | Reglas nacionales de comunicaciones de emergencia; [CER](https://eur-lex.europa.eu/eli/dir/2022/2557/oj) y NIS2 en la UE | Agregados de despacho y de EMS, informes posteriores a la acción | Desvío del EMS del condado comunicado por Dameff et al. (2023) |

Dos rasgos de la tabla importan para el diseño de la investigación. Primero, la **unidad de consecuencia** difiere según el sector, de modo que un estudio intersectorial que compara el «impacto» sin una unidad común está comparando cosas inconmensurables; elija una unidad funcional común (personas sin un servicio durante un tiempo enunciado) o manténgase dentro de un sector. Segundo, la **disponibilidad de la evidencia** está inversamente relacionada con la sensibilidad: los sectores cuyos datos operativos responderían a las mejores preguntas son los que tienen menos probabilidades de divulgarlos. Un proyecto de maestría realista elige una pregunta que puedan responder datos agregados, públicos o consentidos.

### 2.3 Cómo los incidentes sectoriales se vuelven regionales

#### 2.3.1 Dos mecanismos de propagación

El libro doctoral modela las **cascadas de dependencias**: un proveedor falla y cada dependiente falla cuando se agota su reserva; un hospital pierde la presión del agua horas después de que una planta de tratamiento pierda la electricidad. El Estudio de Desbordamiento mide un mecanismo distinto, el **desbordamiento por transferencia de carga**: una unidad falla o se retira y su demanda pasa a pares que no fallaron. Las ambulancias desviadas de Kestrel llegan a Alder Point; los pacientes que no pueden obtener un medicamento en una farmacia van a otra; los clientes de un procesador de pagos caído hacen cola en los bancos. La transferencia de carga suele ser más rápida que una cascada de dependencias (empieza en cuanto la unidad se retira) y está limitada por la **capacidad sobrante** de los pares y no por las reservas.

| Rasgo | Cascada de dependencias | Desbordamiento por transferencia de carga |
|---|---|---|
| Trayectoria | Proveedor → dependiente | Unidad que falló → pares |
| Momento | Después de agotarse la reserva del dependiente | Inmediatamente tras la retirada |
| Factor limitante | Tamaño de la reserva y tiempo de restablecimiento | Capacidad sobrante de los pares y distancia |
| Medición típica | Tiempo hasta el impacto, horas de servicio perdidas | Demanda excedente en los pares, tiempos de espera, rechazos |
| Ejemplo en fuentes públicas | La parada de Colonial Pipeline y sus efectos en la distribución de combustible ([Departamento de Energía de EE. UU.](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident)) | Aumento del volumen en los SU adyacentes a un sistema atacado ([Dameff et al., 2023](https://doi.org/10.1001/jamanetworkopen.2023.12270)) |

Los eventos reales suelen implicar ambos. Durante el ataque de ransomware contra el laboratorio de patología Synnovis en junio de 2024, la dependencia eran los servicios de laboratorio de los que dependían los hospitales; [NHS England informó](https://www.england.nhs.uk/london/2024/06/14/update-on-cyber-incident-clinical-impact-in-south-east-london-friday-14-june-2024/) de que en la primera semana (3–9 de junio) el King's College Hospital y Guy's and St Thomas' aplazaron 814 procedimientos programados y 861 citas ambulatorias hospitalarias y comunitarias, y el trabajo se redirigió a otros proveedores: transferencia de carga. Una tesis debe nombrar qué mecanismo mide, porque el diseño, el resultado y las implicaciones de política difieren.

#### 2.3.2 Concentración y servicios compartidos

Cuando muchas organizaciones dependen de un mismo proveedor de servicios, un incidente en el proveedor se vuelve simultáneo en todas ellas. La [encuesta de la AHA](https://www.aha.org/2024-03-15-aha-survey-change-healthcare-cyberattack-significantly-disrupts-patient-care-hospitals-finances) a casi 1000 hospitales en marzo de 2024 informó de que el 94 % sufrió un impacto financiero por el ciberataque contra Change Healthcare, que interrumpió el procesamiento de reclamaciones y pagos. Un ejemplo no malicioso ilustra el mismo punto estructural: Microsoft [estimó](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/) que una actualización defectuosa de software de seguridad en julio de 2024 afectó a 8,5 millones de dispositivos Windows —menos del uno por ciento de todas las máquinas Windows—, pero interrumpió servicios de forma generalizada porque las máquinas afectadas se concentraban en empresas que operan servicios críticos. Para los investigadores, los incidentes de concentración son experimentos naturales con muchas unidades expuestas simultáneamente, pero puede no existir un grupo de comparación no expuesto del mismo tipo.

### 2.4 Los catálogos públicos de incidentes son muestras, no poblaciones

La mayor parte de la evidencia intersectorial proviene de catálogos compilados a partir de informes públicos: noticias, notificaciones regulatorias de brechas, declaraciones de empresas y avisos de organismos. [Neprash et al. (2022)](https://doi.org/10.1001/jamahealthforum.2022.4873) construyeron una base de datos de este tipo para los ataques de ransomware contra organizaciones prestadoras de atención sanitaria de EE. UU. e informaron de 374 ataques entre 2016 y 2021, un recuento anual que más que se duplicó, de 43 a 91, y de interrupción operativa en el 44,4 % de los ataques, incluido el desvío de ambulancias en 16 (4,3 %). Los autores presentan sus recuentos como ataques que llegaron a conocerse públicamente. Ese encuadre importa, porque el contenido de un catálogo está moldeado por dos procesos que no tienen nada que ver con la incidencia verdadera:

1. **Divulgación dependiente de la gravedad.** Las interrupciones largas y visibles tienen más probabilidades de comunicarse que las cortas absorbidas internamente. La gravedad media del catálogo es, por tanto, mayor que la de la población.
2. **Cambios en las reglas de notificación y en la atención.** Una nueva obligación de notificar, un cambio en la práctica de publicación de un regulador o un aumento de la atención mediática incrementan la fracción de incidentes que se hacen públicos. Los recuentos suben aunque la incidencia no lo haga.

Ninguno de los dos procesos hace inútiles los catálogos. Los hacen adecuados para algunas preguntas (qué tipos de interrupción han ocurrido; qué características aparecen entre los eventos comunicados; cómo cambiaron los eventos comunicados tras una regla) e inadecuados para otras (con qué frecuencia ocurren los incidentes; qué gravedad tiene un incidente típico; si la incidencia está aumentando), salvo que se modele el proceso de divulgación. El laboratorio 2 muestra el tamaño de ambas distorsiones en una población sintética.

### 2.5 Cuando se revisa el primer relato

Los registros públicos de incidentes de infraestructura se revisan a medida que avanzan las investigaciones. Dos casos documentados muestran por qué un investigador debe registrar **qué se afirmó, quién lo afirmó, cuándo y cómo se revisó después**.

- **Oldsmar, Florida, febrero de 2021.** Las primeras declaraciones públicas describieron a un intruso remoto que elevaba el punto de consigna de hidróxido de sodio en una planta de tratamiento de agua, y CISA emitió un aviso conjunto, [AA21-042A, "Compromise of U.S. Water Treatment Facility"](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). En abril de 2023, quien era entonces administrador de la ciudad dijo que el FBI había concluido que el incidente probablemente lo causó un empleado, y un portavoz del FBI dijo que la investigación «no pudo confirmar que este incidente se iniciara por una intrusión cibernética dirigida» ([WUSF, 13 de abril de 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). El incidente sigue apareciendo en muchas listas de ciberataques contra el sector del agua.
- **Düsseldorf, Alemania, septiembre de 2020.** Un ataque de ransomware interrumpió el hospital universitario, una paciente fue trasladada a un hospital más distante y murió, y la fiscalía abrió una investigación por homicidio imprudente que atrajo la atención mundial como posiblemente la primera muerte causada por ransomware. En noviembre de 2020, la fiscalía concluyó que el retraso no fue decisivo para el desenlace ([MIT Technology Review, 12 de noviembre de 2020](https://www.technologyreview.com/2020/11/12/1012015/ransomware-did-not-kill-a-german-hospital-patient/)).

Ninguna de las dos revisiones muestra que el riesgo subyacente sea imaginario. Ambas muestran que un catálogo que codifica el primer relato como un hecho —«intrusión cibernética en una planta de agua», «muerte causada por ransomware»— contiene errores que se propagan a todo análisis que lo use. Un esquema de codificación sólido almacena, para cada incidente, la afirmación, su fuente, el tipo de fuente (oficial, empresa, medios), la fecha de la afirmación, el estado actual (confirmado, disputado, revisado, desconocido) y la fecha de la última comprobación. Una fuente secundaria que repite el primer relato no es una confirmación independiente de él.

### 2.6 Leer un artículo sectorial: un seminario resuelto

El protocolo del seminario (§2.1) aplicado a [Dameff et al. (2023)](https://doi.org/10.1001/jamanetworkopen.2023.12270), usando solo lo que afirman el resumen y el artículo publicados:

1. **Afirmación.** Los hospitales adyacentes a organizaciones prestadoras de atención sanitaria atacadas con ransomware «pueden ver aumentos del censo de pacientes y pueden sufrir limitaciones de recursos que afecten a la atención sensible al tiempo», y esos ataques deberían considerarse un desastre regional.
2. **Evidencia.** Dos SU urbanos académicos del condado de San Diego; 19 857 visitas a los SU; tres fases de cuatro semanas en torno a un ataque contra otra organización que empezó el 1 de mayo de 2021: antes (3–30 de abril), ataque y recuperación (1–28 de mayo), después (29 de mayo–25 de junio). La organización atacada representaba alrededor de una cuarta parte de las altas hospitalarias de la región.
3. **Garantía.** Si nada más cambió entre fases, las diferencias entre fases están asociadas con el ataque.
4. **Rivales (para el grupo).** El cambio estacional de abril a junio; la evolución de la situación de la COVID-19 en la primavera de 2021; otros eventos regionales; muchos resultados comparados, lo que aumenta la probabilidad de que algunas diferencias surjan por azar. El diseño compara fases dentro de los mismos SU; no incluye una región de comparación no afectada, que es la principal aportación que podría hacer un estudio de seguimiento.
5. **Transferencia.** A regiones donde una organización concentra una gran parte de la capacidad, de modo que su retirada desplaza una carga considerable; menos a regiones con muchos proveedores pequeños.
6. **Y qué.** La planificación regional ante ciberdesastres, la ayuda mutua y los protocolos de desvío del EMS —la conclusión del propio artículo— y el argumento para medir los efectos regionales en otros eventos.
7. **Siguiente estudio.** Un diseño controlado: los mismos resultados en SU comparables no afectados durante las mismas semanas, más un gradiente de distancia. Ese es el diseño del Estudio de Desbordamiento.

Fíjese en el tono. El artículo hizo la primera medición publicada de un efecto regional; la crítica del seminario identifica lo que puede añadir un estudio *siguiente*, no lo que los autores «hicieron mal».

### 2.7 Presentar en el seminario

Una presentación de diez minutos tiene una forma fija: una diapositiva para la pregunta y por qué importa; una para el diseño (unidades, exposición, comparación, resultado, periodo); una para el resultado principal en palabras de los autores, con su incertidumbre; una para lo que el diseño descarta y lo que deja abierto; una para el siguiente estudio. Ponga los rivales en la diapositiva como preguntas, no como acusaciones. Cuando le pregunten, separe tres tipos de respuesta: «el artículo dice…», «yo infiero…» y «no lo sé; haría falta…». Los mismos tres registros le servirán en la defensa oral (capítulo 8).

### 2.8 Ejemplo resuelto: una contradicción aparente (ejercicio de seminario)

En el seminario, un participante objeta: «Ghafur et al. encontraron que WannaCry *redujo* la actividad hospitalaria y el NHS no vio ningún aumento de las muertes; Dameff et al. encontraron que el ransomware *aumentó* la actividad. La evidencia se contradice». El seminario lo resuelve con la matriz de conceptos:

| Dimensión | [Ghafur et al., 2019](https://doi.org/10.1038/s41746-019-0161-6) | [Dameff et al., 2023](https://doi.org/10.1001/jamanetworkopen.2023.12270) |
|---|---|---|
| Unidades medidas | *Trusts* infectados (y todos los *trusts*) | SU no afectados adyacentes a la organización atacada |
| Dirección esperada | Las unidades infectadas hacen menos (citas canceladas, menos ingresos) | Los vecinos absorben la demanda desplazada |
| Sistema de salud | NHS de Inglaterra, mayo de 2017 | Condado de San Diego, mayo de 2021 |
| Duración | Una semana de interrupción aguda | Ataque y recuperación de un mes |
| Resultado de daño | Muertes en A&E: ningún cambio detectable, descrito por los autores como una medida tosca | Indicadores de atención del ictus y tiempos de proceso |

Los hallazgos son complementarios: la actividad de una unidad atacada cae y la de sus vecinos sube. Juntos sugieren el mecanismo del Estudio de Desbordamiento. El resultado de «ningún cambio en la mortalidad» tampoco es evidencia de ausencia de daño; es la ausencia de un cambio detectado en un resultado tosco durante una semana. La [investigación de la NAO](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/) añade alcance: al menos 81 de 236 *trusts* de Inglaterra se vieron afectados, junto con 603 organizaciones de atención primaria y otras del NHS, y NHS England registró 6912 citas canceladas, aunque estimó que se cancelaron más de 19 000 en total; un recordatorio de que los recuentos registrados y los totales estimados son cantidades distintas.

### 2.9 Actividad práctica: lo que un catálogo hace a la gravedad y a la tendencia

El laboratorio crea una población sintética de 2400 incidentes que interrumpen servicios, 400 por año durante seis años, de modo que la incidencia verdadera es constante. Las duraciones de las interrupciones son log-normales con una mediana de 6 horas. Cada incidente se divulga con una probabilidad que aumenta con la duración (50 % a las 24 horas), y una obligación de notificar a partir del año 4 multiplica la divulgación por 1,8.

```python
# Lab 2 - what a public incident catalogue does to severity and trend (offline, standard library only)
# Synthetic population of service-disrupting incidents over six years. Each has an outage duration (hours).
# Disclosure probability rises with duration; a reporting mandate raises disclosure from year 4.
import math, random

rng = random.Random(42)
TRUE_PER_YEAR = 400                      # constant true incidence: there is NO real trend

def p_report(hours, year):
    base = 1 / (1 + math.exp(-(math.log(hours) - math.log(24)) * 1.5))   # 50% at 24 h
    return min(1.0, base * (1.0 if year < 4 else 1.8))                   # mandate from year 4

pop = []
for year in range(1, 7):
    for _ in range(TRUE_PER_YEAR):
        hours = rng.lognormvariate(math.log(6), 1.2)                       # median 6 h
        pop.append((year, hours, rng.random() < p_report(hours, year)))

def summary(rows):
    h = sorted(r[1] for r in rows)
    n = len(h)
    med = h[n // 2] if n % 2 else (h[n // 2 - 1] + h[n // 2]) / 2
    return n, sum(h) / n, med, sum(x > 24 for x in h) / n

print("set           n     mean_h  median_h  share>24h")
for label, rows in (("population", pop), ("catalogue", [r for r in pop if r[2]])):
    n, mean, med, big = summary(rows)
    print(f"{label:12} {n:5d}  {mean:7.1f}  {med:8.1f}  {big:9.2f}")
print("year  true  catalogued")
for y in range(1, 7):
    print(f"{y:4d}  {sum(r[0] == y for r in pop):4d}  {sum(r[0] == y and r[2] for r in pop):10d}")
```

Salida esperada:

```text
set           n     mean_h  median_h  share>24h
population    2400     12.8       6.1       0.13
catalogue      646     29.2      18.4       0.40
year  true  catalogued
   1   400          99
   2   400          73
   3   400          90
   4   400         125
   5   400         133
   6   400         126
```

Lea ambas tablas. La interrupción media del catálogo (29,2 h) es más del doble de la de la población (12,8 h); su mediana es tres veces mayor; y la proporción de incidentes de más de 24 horas sube del 13 % al 40 %. Un estudio que describiera los incidentes «típicos» a partir del catálogo los exageraría mucho. Los recuentos anuales muestran un salto de unos 87 por año a unos 128 por año tras la obligación: un «aumento» del 47 % en una población cuya incidencia nunca cambió. Un análisis honesto de un catálogo se limita a preguntas que la selección no distorsiona, modela el proceso de divulgación con supuestos enunciados o usa un denominador externo (por ejemplo, todos los incidentes notificados en virtud de una obligación cuya exhaustividad se conoce).

### 2.10 Errores habituales y límites

- Comparar el «impacto» entre sectores sin una unidad de consecuencia común.
- Confundir las cascadas de dependencias con el desbordamiento por transferencia de carga y, por tanto, medir el resultado equivocado.
- Tratar los recuentos de un catálogo público como incidencia, o los promedios del catálogo como gravedad típica.
- Interpretar un aumento de los incidentes notificados tras una obligación como un aumento de los ataques.
- Codificar un relato público temprano como un hecho y no volver a revisarlo nunca.
- Tratar una fuente secundaria que repite un primer relato como confirmación independiente.
- Criticar un artículo por no hacer lo que sus datos nunca podrían respaldar, en lugar de identificar el siguiente estudio.
- Tratar «ningún cambio detectado» en un resultado tosco como evidencia de ausencia de efecto.

El límite de un seminario es que solo lee lo que se publicó. La evidencia no publicada —incidentes nunca divulgados, datos operativos nunca liberados— queda fuera de él, y el seminario debe decirlo en lugar de suponer que el registro publicado está completo.

### Ejercicios — capítulo 2

**EX008 — Perfil sectorial.** *Objetivo:* perfilar un sector como contexto de investigación. *Entradas:* la tabla del §2.2. *Restricciones:* elija un sector distinto de la salud; cite al menos dos fuentes primarias para sus instrumentos y un caso público documentado. *Pasos:* (1) defina la unidad de consecuencia; (2) enumere las reservas; (3) nombre los instrumentos que lo rigen con su versión y su fecha; (4) enumere la evidencia que un estudiante de maestría podría obtener legalmente; (5) proponga una pregunta respondible que esta evidencia pueda respaldar. *Evidencia esperada:* perfil de una página. *Rúbrica:* 3 = unidad de consecuencia precisa, instrumentos citados con exactitud, evidencia realista, pregunta ajustada a la evidencia; 2 = un elemento vago; 1 = sin citas; 0 = nada.

**EX009 — Distorsión del catálogo.** *Objetivo:* separar el sesgo de tendencia que crea una obligación de notificar del sesgo de gravedad que crea la divulgación selectiva en un catálogo de incidentes. *Entradas:* el código del laboratorio 2. *Restricciones:* sin conexión; no cambie la semilla. *Pasos:* (1) ejecute el laboratorio y anote la salida; (2) fije el multiplicador de la obligación en 1.0 e informe la media, la mediana, la proporción por encima de 24 horas y los recuentos anuales del catálogo; (3) explique por qué la distorsión de la gravedad persiste sin la obligación; (4) proponga una pregunta que este catálogo *sí* puede responder sin modelar la divulgación. *Evidencia esperada:* salidas y dos párrafos. *Rúbrica:* 3 = salidas correctas, distorsión de la gravedad atribuida a la divulgación dependiente de la gravedad, distorsión de la tendencia atribuida a la obligación, una pregunta respondible y defendible; 2 = falta una explicación; 1 = no ejecutado; 0 = nada.

**EX010 — Protocolo del seminario.** *Objetivo:* aplicar el protocolo de siete preguntas. *Entradas:* [Ghafur et al. (2019)](https://doi.org/10.1038/s41746-019-0161-6). *Restricciones:* use solo lo que afirma el artículo; cite su afirmación. *Pasos:* responda las siete preguntas del §2.1; señale qué rivales aborda el artículo y cómo. *Evidencia esperada:* una página. *Rúbrica:* 3 = afirmación citada, diseño descrito con exactitud (fuente de datos, comparación, resultados), rivales concretos, siguiente estudio factible; 2 = una pregunta pobre; 1 = opinión en lugar de evidencia; 0 = nada.

**EX011 — Clasificación de mecanismos.** *Objetivo:* distinguir los mecanismos de propagación. *Entradas:* (a) la parada de Colonial Pipeline y sus efectos en el suministro de combustible (página del DOE); (b) Synnovis y los procedimientos aplazados (NHS England); (c) Change Healthcare y la liquidez de los hospitales (AHA); (d) el desvío de Kestrel y las llegadas a Alder Point (sintético). *Restricciones:* use el §2.3.1. *Pasos:* clasifique cada uno como cascada de dependencias, desbordamiento por transferencia de carga o ambos; nombre la unidad de consecuencia; nombre el factor limitante. *Evidencia esperada:* tabla. *Rúbrica:* 3 = clasificaciones justificadas, «ambos» reconocido cuando la sustitución sigue a un fallo de dependencia, factores limitantes concretos; 2 = una clasificación errónea; 1 = sin justificación; 0 = nada.

**EX012 — Codificar un incidente revisado.** *Objetivo:* diseñar una entrada de catálogo que sobreviva a la revisión. *Entradas:* las fuentes sobre Oldsmar del §2.5. *Restricciones:* como mínimo, los campos del §2.5. *Pasos:* (1) escriba la entrada tal como habría quedado en marzo de 2021; (2) actualícela a abril de 2023; (3) indique cómo debería tratar la entrada un análisis que cuente «intrusiones confirmadas en empresas de agua»; (4) indique cómo comprobaría el estado de la entrada antes de usarla en 2026. *Evidencia esperada:* dos entradas y un párrafo. *Rúbrica:* 3 = ambas entradas conservan la fuente, la fecha y el estado, regla de análisis explícita, procedimiento de nueva comprobación concreto; 2 = historial perdido en la actualización; 1 = la entrada afirma una causa; 0 = nada.

**EX013 — Contradicción aparente.** *Objetivo:* resolver hallazgos que parecen contradictorios. *Entradas:* las afirmaciones «WannaCry redujo la actividad en los *trusts* infectados del NHS» y «el ransomware aumentó el volumen en los SU vecinos de San Diego». *Restricciones:* use una matriz de conceptos con al menos cinco dimensiones. *Pasos:* (1) construya la matriz; (2) indique si los hallazgos se contradicen; (3) indique qué estudio podría poner a prueba el mecanismo combinado. *Evidencia esperada:* matriz y párrafo. *Rúbrica:* 3 = unidades y dirección distinguidas, limitación de la medida de daño señalada, el estudio combinado mide tanto las unidades atacadas como las vecinas; 2 = falta una dimensión; 1 = afirma la contradicción; 0 = nada.

**EX014 — Presentación en el seminario.** *Objetivo:* presentar un artículo con justicia. *Entradas:* un artículo sectorial publicado de su elección con un resultado cuantitativo. *Restricciones:* cinco diapositivas como en el §2.7; rivales planteados como preguntas. *Pasos:* (1) prepare las diapositivas; (2) escriba tres preguntas que espera y sus respuestas en los tres registros («el artículo dice», «yo infiero», «no lo sé; haría falta»); (3) tras presentar ante sus pares, registre un punto en el que cambió su lectura. *Evidencia esperada:* esquema de las diapositivas, hoja de preguntas y reflexión. *Rúbrica:* 3 = resumen justo antes de la crítica, rivales precisos, registros usados correctamente, reflexión honesta; 2 = la crítica precede al resumen; 1 = basada en opiniones; 0 = nada.

### Síntesis del capítulo

Los sectores se diferencian en lo que pierden, con qué rapidez y para quién; en quién los rige; y en qué evidencia llega a la vista del público. Elija una unidad de consecuencia común o manténgase dentro de un sector. Distinga las cascadas de dependencias del desbordamiento por transferencia de carga y mida el mecanismo que afirma. Los catálogos públicos son muestras moldeadas por la divulgación dependiente de la gravedad y por los cambios en las reglas de notificación: sus promedios exageran la gravedad típica y sus tendencias pueden ser artefactos. Los primeros relatos públicos se revisan —Oldsmar y Düsseldorf son ejemplos documentados—, así que codifique las afirmaciones con su fuente, su fecha y su estado, y vuelva a comprobarlas antes de usarlas. Lea los artículos con un protocolo fijo, resuma con justicia antes de criticar y convierta la crítica en el diseño del siguiente estudio.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 08

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](../../en/book/MANUSCRIPT.md#ch-03)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Cada resultado resuelto muestra una respuesta defendible y explica lo que premia la rúbrica. Una respuesta distinta puede obtener la máxima calificación si cumple el mismo estándar de evidencia, alcance y honestidad sobre los límites. Los resultados numéricos provienen de los laboratorios sin conexión de este libro ejecutados con Python 3 (en este borrador se usó la versión 3.13) y solo con la biblioteca estándar; si su salida difiere, compruebe primero la versión de Python, la semilla y si cambió el orden de las extracciones aleatorias.

### Capítulo 1: EX001–EX007

**EX001 — Del tema a la pregunta.** *Problema:* los reguladores estatales del agua potable y las asociaciones de empresas de servicios no saben con qué frecuencia ni durante cuánto tiempo los incidentes cibernéticos en empresas pequeñas interrumpen el tratamiento o la vigilancia, de modo que los programas de apoyo no pueden focalizarse. *Pregunta (forma PICOT):* entre los sistemas comunitarios de agua que abastecen a 3300–50 000 personas en un estado (P), ¿con qué frecuencia coincidieron los incidentes cibernéticos notificados al organismo estatal competente (E) con una interrupción registrada del tratamiento o de la vigilancia, en comparación con las averías de equipos no cibernéticas (C), medida como el número y la duración de las interrupciones (O) a lo largo de cinco años (T)? *FINER:* factible solo si los registros de incidentes del organismo competente distinguen las causas y pueden compartirse de forma agregada, lo que debe comprobarse primero; interesante para el organismo y para las empresas; novedosa si no existe ninguna descripción a escala estatal; ética porque los registros agregados no involucran a individuos, aunque debe gestionarse el riesgo de identificar a empresas pequeñas (capítulo 3); relevante porque mostraría si las causas cibernéticas son una proporción significativa de las interrupciones. *Afirmación esperada:* «En un estado, a lo largo de cinco años, los incidentes cibernéticos registrados representaron una proporción enunciada de las interrupciones del tratamiento o de la vigilancia, con duraciones enunciadas». *Fuera del alcance:* la incidencia de los incidentes no notificados; los efectos sobre la salud. La máxima calificación exige honestidad sobre la viabilidad (puede que los registros no codifiquen la causa de forma fiable) y una afirmación limitada a los incidentes notificados.

**EX002 — Tipos de pregunta.**

| P | Tipo | Diseño mínimo | Afirmación más fuerte |
|---|---|---|---|
| (a) | Descriptiva | Registro completo de desvíos del condado en 2024 con códigos de causa | Horas de desvío por causa en ese condado y ese año |
| (b) | De asociación (causal solo con más) | Comparación transversal o de panel de SU con y sin simulacros, ajustada por tamaño y casuística | Una asociación entre la adopción de simulacros y los tiempos de espera durante las interrupciones; causal solo si puede aprovecharse el momento de la adopción (por ejemplo, una implantación escalonada) con comparaciones creíbles |
| (c) | Causal | ITS controlada o equivalente | Cambio porcentual respecto a un contrafáctico, bajo supuestos enunciados |
| (d) | Explicativa | Entrevistas con despachadores y tripulaciones, registros de despacho | Un mecanismo respaldado por relatos convergentes |
| (e) | Evaluativa (causal) | ITS en torno al inicio del protocolo, idealmente con una región de comparación | Efecto del protocolo sobre el tiempo en desvío, bajo supuestos |

El punto clave de la rúbrica es (b): la adopción de simulacros la eligen los hospitales, de modo que los hospitales mejor gestionados adoptan simulacros y a la vez tienen esperas más cortas; sin un diseño que maneje esto, la afirmación es de asociación.

**EX003 — Estrategia de búsqueda y prueba de los elementos conocidos.** Bloques como en el §1.4.2, con añadidos como "health information technology failure", "cyber incident" y "EHR outage" en el bloque A y "regional surge", "patient redistribution" y "mutual aid" en el bloque C. Fuentes: un índice biomédico (para la medicina de urgencias y los servicios de salud), un índice académico general (para la economía y la administración pública) y un índice de informática (para la seguridad), cada uno justificado por la disciplina que cubre. Literatura gris: oficinas de auditoría (por ejemplo, la NAO), organismos y ministerios de salud, declaraciones de reguladores, informes posteriores a la acción de coaliciones sanitarias y de EMS, encuestas de asociaciones de hospitales (por ejemplo, las de la AHA) y órganos de coordinación sectorial. Conjunto de elementos conocidos: Dameff et al. (2023), Ghafur et al. (2019), Neprash et al. (2022); se comprueba buscando en cada fuente y confirmando que el elemento aparece en los resultados, revisando la cadena si no aparece y registrando la revisión. Regla de detención: dos rondas consecutivas de encadenamiento sin ningún nuevo estudio incluido. Campos del registro: fecha, fuente, cadena exacta, filtros, resultados, nombre del archivo exportado, persona. La rúbrica premia una búsqueda que encontraría el informe de la NAO —imposible solo con bases de datos bibliográficas— y una comprobación de elementos conocidos que pueda ejecutarse realmente.

**EX004 — Deduplicación y acuerdo.** (1) La salida esperada es la del §1.9: 20 identificados, 5 duplicados, 15 cribados, κ = 0,571. (2) Con el registro del signo «&» añadido e `I` agregado para ambos revisores, la salida es `records identified: 21 duplicates removed: 5 screened: 16`, `po=0.812 pe=0.547 kappa=0.586`: el registro **no** se eliminó. El título normalizado "ransomware emergency department crowding at neighbouring hospitals" difiere de "ransomware and emergency department crowding…" porque el normalizador elimina «&», pero no lo convierte en «and». Corrección: sustituir «&» por " and " antes de eliminar la puntuación y añadir una revisión manual de las coincidencias aproximadas (por ejemplo, títulos cuyas formas normalizadas difieren en una palabra). (3) Partiendo del laboratorio original, cambiar a I la decisión de B sobre el artículo de las subestaciones da `po=0.733 pe=0.547 kappa=0.412`. (4) El acuerdo bruto bajó 6,7 puntos, pero la kappa bajó de 0,571 a 0,412, porque la kappa reescala el acuerdo por encima del azar sobre el intervalo restante: con un acuerdo por azar cercano a 0,55, solo 0,45 de la escala se «gana», de modo que un desacuerdo adicional entre 15 registros elimina una gran parte de ella.

**EX005 — Reparar los criterios de elegibilidad.** Criterios para la literatura gris: *incluir* los informes de organismos gubernamentales, reguladores, oficinas de auditoría, coaliciones sanitarias, organismos de EMS o asociaciones de hospitales que describan los efectos operativos (actividad, desvío, retrasos, cancelaciones) de un incidente cibernético o de una interrupción informática concretos sobre una o más organizaciones de atención sanitaria; *excluir* los documentos que describen procedimientos, orientaciones o productos sin comunicar los efectos de un evento, y el marketing de proveedores. Decisiones: el memorando del departamento estatal de salud sobre los procedimientos de funcionamiento sin sistemas → excluir (procedimiento sin efectos), salvo que el texto completo comunique los efectos de un evento; el informe de ejercicio de la coalición → excluir para PI1–2 (un ejercicio no es un evento), pero conservarlo en una lista aparte de «métodos y planificación» útil para PI3 y para la discusión; el libro blanco del proveedor → excluir. Un registro que sigue siendo indecidible a partir de su primera página pasa a revisión del texto completo en lugar de excluirse, para que la incertidumbre no reduzca en silencio la base de evidencia.

**EX006 — Matriz de conceptos.** Fila de la NAO: *unidad* — organizaciones del NHS en Inglaterra; *exposición* — WannaCry, mayo de 2017; *comparación* — ninguna en sentido estadístico; una investigación de lo que ocurrió y por qué; *resultados* — al menos 81 de 236 *trusts* afectados, más 603 organizaciones de atención primaria y otras del NHS (entre ellas 595 consultorios de medicina general); 6912 citas registradas como canceladas y más de 19 000 estimadas en total; *diseño* — investigación de auditoría; *respalda* — la escala de la interrupción y la brecha entre las cancelaciones registradas y las estimadas; *rivales planteados o abiertos* — registro incompleto; desconexión preventiva de organizaciones no afectadas. Párrafo modelo: «La evidencia sobre los efectos regionales proviene de tres tipos de estudio. Las investigaciones de auditoría (NAO, 2017) establecen la escala de la interrupción, pero se basan en recuentos registrados que subestiman los totales. Los análisis de datos administrativos (Ghafur et al., 2019) cuantifican la reducción de la actividad en los *trusts* infectados —alrededor de un 6 % menos de ingresos por hospital infectado y por día— y no encuentran diferencias en las muertes en A&E, una medida que los autores califican de tosca. Un estudio antes-después de SU vecinos (Dameff et al., 2023) asocia un periodo de ataque con un aumento del volumen en vecinos no afectados. Ningún estudio compara todavía a los vecinos con una región no afectada ni examina la distancia…». La rúbrica premia la distinción entre lo registrado y lo estimado y la organización por concepto.

**EX007 — Memorando de estimando y alcance.** Estimando de PI1: «Para cada uno de Alder Point, Brookfield y Calloway: exp(β₂) − 1, la diferencia porcentual entre la media diaria de llegadas de ambulancias durante los días 0–20 y las llegadas esperadas a partir de la tendencia previa al evento del SU ajustada por el cambio simultáneo en las llegadas agrupadas de Wexmoor». PI2: «el patrón de estas tres estimaciones frente a la distancia, resumido como la diferencia entre la estimación del SU más cercano y la media de las estimaciones de los dos SU más distantes, con intervalos». Estimandos alternativos que podría calcular un analista descuidado: el aumento del primer día (solo capta el choque inicial); el aumento respecto a los mismos días del año pasado (confundido por un año de tendencia y una estación distinta); el número total de pacientes adicionales en 21 días (otra escala, sensible al tamaño de la línea base). Afirmación esperada como en el §1.2.1; fuera del alcance: los resultados en pacientes, el efecto del ransomware como algo distinto del desvío, otras regiones.

### Capítulo 2: EX008–EX014

**EX008 — Perfil sectorial (ejemplo: agua).** Unidad de consecuencia: personas abastecidas por un sistema sin agua que cumpla un umbral enunciado de presión o de calidad, durante un tiempo enunciado, y el número y la duración de los avisos. Reservas: almacenamiento, dosificación y vigilancia manuales, interconexiones con sistemas vecinos, distribución de agua embotellada. Instrumentos: la America's Water Infrastructure Act of 2018 (evaluaciones de riesgo y resiliencia y planes de respuesta a emergencias para los sistemas comunitarios de agua que abastecen a más de 3300 personas, según la página de la EPA); en la UE, el agua potable es un sector de NIS2 y un sector de CER. Evidencia: avisos (públicos), resúmenes del organismo estatal competente, encuestas a empresas, entrevistas; rara vez datos operativos. Pregunta: «En un estado, ¿cuántos avisos de hervir el agua emitidos en cinco años atribuyó el organismo competente a fallos de equipos o de sistemas de control, y cuánto duraron?». Caso público: Oldsmar, codificado con su revisión (§2.5). La máxima calificación exige citas exactas de los instrumentos y una pregunta ajustada a evidencia pública o agregada.

**EX009 — Distorsión del catálogo.** (1) Salida como en el §2.9. (2) Con el multiplicador en 1.0: población sin cambios; catálogo `n=491, mean 31.8 h, median 18.9 h, share>24h 0.42`; recuentos anuales catalogados 99, 73, 90, 75, 77, 77. (3) La distorsión de la gravedad persiste porque la causa la divulgación dependiente de la gravedad, que actúa todos los años con independencia de la obligación; la obligación solo cambia cuántos incidentes se divulgan, no cuáles se ven favorecidos. (La media del catálogo sube ligeramente sin la obligación porque la obligación admite proporcionalmente más incidentes cortos). La tendencia desaparece: los años 4–6 se parecen ahora a los años 1–3, salvo por el ruido. (4) Pregunta respondible: «Entre los incidentes catalogados, ¿cambió tras la obligación la proporción que presenta una característica concreta (por ejemplo, el desvío de ambulancias)?»; sigue afectada si la obligación cambia *qué* incidentes se divulgan, así que las respuestas más seguras describen características dentro del catálogo y no tasas. La rúbrica premia atribuir cada distorsión a su mecanismo.

**EX010 — Protocolo del seminario sobre Ghafur et al. (2019).** *Afirmación (citada del resumen):* «Entre los hospitales infectados con el ransomware WannaCry, hubo una disminución significativa del número de atenciones e ingresos, que correspondió a 5,9 millones de libras en actividad hospitalaria perdida. No se informó de ningún aumento de la mortalidad, aunque esta es una medida tosca del daño a los pacientes». *Evidencia:* Hospital Episode Statistics de los *trusts* del NHS en Inglaterra, del 1 de abril al 30 de junio de 2017, agregadas a hospital-día; 34 *trusts* infectados comparados con *trusts* no infectados. *Diseño:* diferencias en diferencias por mínimos cuadrados ordinarios con efectos fijos de hospital y términos de día de la semana y de festivo, comparando la semana de WannaCry con semanas de referencia; los resultados fueron citas de consultas externas canceladas, ingresos programados y urgentes, atenciones en A&E y muertes en A&E. *Garantía:* los *trusts* no infectados muestran lo que habrían hecho los infectados esa semana. *Rivales que aborda el artículo:* la fluctuación nacional (se modelan las semanas anteriores y posteriores y se muestra que el cambio en todos los *trusts* está dentro de la volatilidad normal); las diferencias invariables en el tiempo entre hospitales (efectos fijos). *Rivales que plantea o deja abiertos:* el fallo de registro en los *trusts* infectados —los propios autores señalan que, si los sistemas usados para codificar los datos administrativos estaban caídos, puede que los datos no reflejen plenamente los hechos, un rival de medición propio de los estudios sobre interrupciones informáticas—; los *trusts* «afectados» pero no infectados que se desconectaron como precaución, que complican el grupo de comparación (el artículo los analiza por separado); y la transferencia de carga a los vecinos, que el artículo nombra como una laguna («no tenemos ninguna comprensión del efecto de red»). *Transferencia:* a sistemas de salud centralizados con datos comparables y ataques cortos. *Y qué:* incluso un ataque corto tuvo costos de actividad y financieros medibles. *Siguiente estudio:* la actividad de los hospitales vecinos durante cierres y desvíos, que es precisamente la pregunta del Estudio de Desbordamiento. La máxima calificación incluye el rival del fallo de registro y una descripción exacta de la comparación.

**EX011 — Clasificación de mecanismos.**

| Caso | Mecanismo | Unidad de consecuencia | Factor limitante |
|---|---|---|---|
| (a) Colonial Pipeline | Cascada de dependencias (la distribución de combustible depende del oleoducto), con transferencia de carga a rutas de suministro alternativas | Producto no entregado; déficits de suministro | Inventarios y capacidad de transporte alternativo |
| (b) Synnovis | Ambos: los hospitales dependían de los servicios de patología (cascada); el trabajo se redirigió a otros proveedores (transferencia de carga) | Procedimientos y citas aplazados | Capacidad de laboratorio en otros lugares |
| (c) Change Healthcare | Cascada de dependencias a través del procesamiento de reclamaciones y pagos | Interrupción de la liquidez; reclamaciones retrasadas | Procesadores alternativos y reservas de efectivo |
| (d) Desvío de Kestrel | Desbordamiento por transferencia de carga | Llegadas excedentes y tiempo de espera en los vecinos | Capacidad sobrante y rutas de los vecinos |

La rúbrica premia reconocer «ambos» cuando la sustitución sigue a un fallo de dependencia.

**EX012 — Codificar un incidente revisado.** Entrada de marzo de 2021: *afirmación* — «un usuario remoto no autorizado cambió el punto de consigna de hidróxido de sodio en la planta de tratamiento de agua de Oldsmar»; *fuente* — aviso de CISA AA21-042A y declaraciones públicas de las autoridades locales; *tipo de fuente* — oficial; *fecha de la afirmación* — febrero de 2021; *estado* — comunicado, en investigación; *última comprobación* — marzo de 2021. Actualización de abril de 2023: conservar la afirmación original y sus fuentes, añadir *revisión* — «el exadministrador de la ciudad declaró que el FBI concluyó que el evento probablemente lo causó un empleado; el FBI dijo que no pudo confirmar una intrusión dirigida» (WUSF, 13 de abril de 2023); *estado* — disputado (o «no confirmado»); *última comprobación* — abril de 2023. Regla de análisis: un análisis que cuente intrusiones confirmadas excluye la entrada, mientras que un análisis de sensibilidad que incluya las entradas disputadas comunica ambos recuentos. Procedimiento de nueva comprobación para 2026: buscar declaraciones oficiales posteriores a abril de 2023 (registros del FBI, actualizaciones del aviso de CISA) y registrar lo encontrado y la fecha.

**EX013 — Contradicción aparente.** Dimensiones de la matriz: unidades (*trusts* infectados frente a vecinos no afectados), dirección esperada (la actividad cae frente a sube), sistema de salud y año (NHS 2017 frente a San Diego 2021), duración (alrededor de una semana frente a un mes), resultados (ingresos, atenciones, cancelaciones, muertes en A&E frente a censo, llegadas, esperas, indicadores de ictus), diseño (datos administrativos con referencia y comparación infectados/no infectados frente a antes-después dentro de los vecinos). No se contradicen: miden extremos opuestos de la misma transferencia de carga. Un estudio combinado mediría tanto la actividad perdida por la organización atacada como la actividad ganada por los vecinos en el mismo evento, con una región de comparación no afectada, de modo que puedan estimarse juntos el efecto regional neto y su redistribución.

**EX014 — Presentación en el seminario.** Se evalúa con la rúbrica. Una entrega de máxima calificación resume el artículo en sus propios términos antes de la crítica; enuncia los rivales como preguntas («¿Podría el cambio de abril a mayo reflejar la estación?»); y usa los tres registros en las respuestas preparadas, por ejemplo: «El artículo dice que la organización atacada gestionaba alrededor de una cuarta parte de las altas de la región. Infiero que la retirada de una organización más pequeña desplazaría menos carga. No sé en qué diferiría el resultado en una región con muchos proveedores; haría falta una comparación entre varias regiones». La reflexión nombra un cambio concreto en la lectura provocado por los pares.

<a id="glossary"></a>

## Glosario

- **Análisis del diseño** — Simular un estudio planificado sobre datos generados con efectos conocidos para conocer su sesgo, su precisión y su probabilidad de detectar efectos de tamaño plausible antes de recoger datos reales.
- **Análisis temático** — Un método para identificar, analizar y comunicar patrones de significado en datos cualitativos, en seis fases.
- **Autocorrelación** — Correlación entre los valores de una serie (o los residuos de un modelo) en días cercanos; deja insesgadas las estimaciones por mínimos cuadrados, pero hace que sus errores estándar habituales sean incorrectos.
- **Cascada de dependencias** — Propagación de una perturbación desde un proveedor que falla hacia los servicios que dependen de él.
- **Conjunto de elementos conocidos** — Estudios que ya se sabe que son pertinentes, usados para comprobar que una estrategia de búsqueda los recupera.
- **Control negativo** — Un resultado o una población que la exposición no debería afectar, pero que comparte los factores de confusión del estudio; se usa para detectar sesgos.
- **Control sintético** — Una combinación ponderada de unidades no expuestas elegida para reproducir la trayectoria previa al evento de la unidad expuesta, usada como su contrafáctico.
- **Criterios de progresión** — Umbrales fijados antes de un piloto que deciden si el estudio principal continúa, continúa tras una modificación o se detiene.
- **Curva de especificación** — El conjunto de estimaciones obtenidas con todas las decisiones analíticas razonables, mostradas juntas para que ninguna decisión aislada sostenga la conclusión.
- **Desbordamiento por transferencia de carga** — Propagación de una perturbación por sustitución: la demanda que el proveedor perturbado no puede atender pasa a otros.
- **Desvío (desvío de ambulancias)** — La solicitud de un hospital de que las ambulancias lleven a los pacientes a otros hospitales; en este libro, la exposición del Estudio de Desbordamiento.
- **Diagrama acíclico dirigido (DAG)** — Un diagrama de las relaciones causales supuestas que se usa para identificar factores de confusión, mediadores y colisionadores.
- **Discordancia** — En los métodos mixtos, un resultado de una vertiente que entra en conflicto con la otra; se comunica y se explica en lugar de resolverse dejando que gane una vertiente.
- **Errores estándar de Newey–West (HAC)** — Errores estándar robustos a la heterocedasticidad y a la autocorrelación hasta un rezago elegido, que usan ponderaciones decrecientes de Bartlett.
- **Estimando** — La cantidad precisa que un estudio pretende estimar: unidad, resultado, contraste de exposición, ventana temporal y medida resumen.
- **Estudio piloto (de viabilidad)** — Un estudio pequeño que pone a prueba si el estudio principal puede hacerse según lo previsto —datos, instrumentos y procedimientos—, no si la hipótesis es verdadera.
- **FINER** — Factible, interesante, novedosa, ética y relevante (*feasible, interesting, novel, ethical, relevant*): criterios para una pregunta de investigación.
- **Kappa de Cohen (κ)** — Acuerdo entre dos evaluadores más allá del que producirían por azar sus frecuencias marginales: (observado − azar) / (1 − azar).
- **Limitación direccional** — Una limitación enunciada con la dirección probable y el tamaño aproximado de su sesgo, lo que se hizo al respecto y lo que la resolvería.
- **Literatura gris** — Informes y documentos producidos fuera de la edición académica comercial (auditorías, informes de organismos, revisiones posteriores a la acción).
- **Matriz de conceptos** — Una tabla que organiza los estudios según los conceptos de los que trata una revisión (unidades, exposición, comparación, resultados, diseño, rivales), de modo que la síntesis avance por concepto y no autor por autor.
- **Metainferencia** — La conclusión que se extrae al integrar dos vertientes: confirmación, ampliación o discordancia.
- **Múltiples hipótesis de trabajo** — Mantener varias explicaciones a la vez y diseñar evidencia que discrimine entre ellas.
- **PICOT (forma para infraestructura)** — Población o unidades, exposición, comparación, resultado y tiempo, usados para que una pregunta sea respondible.
- **Plan de análisis previo** — Una especificación registrada y fechada de estimandos, resultados, modelos y comprobaciones de robustez escrita antes de ver los datos de resultado.
- **Poder informativo** — La idea de que cuanto más información pertinente tiene cada participante para un objetivo acotado, menos entrevistas se necesitan.
- **Presentación conjunta** — Una tabla que empareja resultados cuantitativos con hallazgos cualitativos y enuncia una metainferencia para cada fila.
- **Procedencia (de un número)** — El camino rastreable desde un número del texto hasta el código y la salida que lo produjeron.
- **Prueba placebo en el tiempo** — Ajustar el modelo principal a ventanas anteriores al evento real, donde no debería existir ningún efecto, y situar la estimación real en el orden de las estimaciones placebo.
- **Rastro de auditoría** — El libro de códigos, los memorandos y las versiones de un análisis cualitativo que permiten a otra persona seguir cómo los códigos se convirtieron en temas.
- **Registro de desviaciones** — Un registro fechado de cada cambio en un plan registrado, su motivo y si se habían visto datos de resultado cuando se hizo.
- **Registro de resultados y afirmaciones** — Una tabla que vincula cada afirmación de la tesis con su resultado, la fuerza de la evidencia y el verbo que la evidencia permite.
- **Regresión a la media** — La tendencia de las mediciones inusualmente extremas a ir seguidas de otras menos extremas, que puede imitar un efecto cuando las unidades se seleccionan por valores extremos.
- **Regresión segmentada** — Regresión con términos de nivel y de pendiente que cambian en una interrupción; el modelo habitual para las series temporales interrumpidas.
- **Revisión exploratoria** (*scoping review*) — Una revisión que traza la extensión y los tipos de evidencia sobre una pregunta amplia en lugar de combinar efectos.
- **Ruta crítica** — La cadena de tareas cuyo retraso retrasa todo el proyecto; en una tesis de maestría suelen ser las aprobaciones y los acuerdos de datos.
- **Serie temporal interrumpida controlada (CITS)** — Una serie temporal interrumpida analizada en relación con una serie de comparación que no estuvo expuesta, de modo que se eliminen choques compartidos como la estación.
- **Sesgo de comunicación (sesgo de catálogo)** — Distorsión de los catálogos de incidentes porque los incidentes que se divulgan dependen de su gravedad, de las obligaciones y de la atención.
- **Tendencias paralelas** — El supuesto de que, sin la exposición, las series tratada y de comparación se habrían movido juntas.

<a id="references"></a>

## Referencias

Las leyes, las orientaciones y las páginas públicas sobre incidentes cambian. Las versiones y fechas que siguen son las consultadas para este borrador (octubre de 2026); vuelva a verificarlas antes de basarse en ellas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

**Política, derecho y normas**

- Bank for International Settlements, Committee on Payments and Market Infrastructures, and International Organization of Securities Commissions. [Guidance on Cyber Resilience for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d146.htm). June 2016.
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- European Union. [Regulation (EU) 2022/2554 on digital operational resilience for the financial sector (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Department of Health and Human Services. [Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html).
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).
- U.S. Government. [45 CFR Part 46 — Protection of Human Subjects](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46). Electronic Code of Federal Regulations.

**Incidentes y evidencia sectorial**

- American Hospital Association. [AHA Survey: Change Healthcare Cyberattack Significantly Disrupts Patient Care, Hospitals' Finances](https://www.aha.org/2024-03-15-aha-survey-change-healthcare-cyberattack-significantly-disrupts-patient-care-hospitals-finances). 15 March 2024.
- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Dameff, C., Tully, J., Chan, T. C., et al. [Ransomware Attack Associated With Disruptions at Adjacent Emergency Departments in the US](https://doi.org/10.1001/jamanetworkopen.2023.12270). *JAMA Network Open*, 6(5), e2312270, 2023.
- Ghafur, S., Kristensen, S., Honeyford, K., Martin, G., Darzi, A., and Aylin, P. [A Retrospective Impact Analysis of the WannaCry Cyberattack on the NHS](https://doi.org/10.1038/s41746-019-0161-6). *npj Digital Medicine*, 2, 98, 2019.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- MIT Technology Review. [Ransomware Did Not Kill a German Hospital Patient](https://www.technologyreview.com/2020/11/12/1012015/ransomware-did-not-kill-a-german-hospital-patient/). 12 November 2020.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Neprash, H. T., McGlave, C. C., Cross, D. A., et al. [Trends in Ransomware Attacks on US Hospitals, Clinics, and Other Health Care Delivery Organizations, 2016–2021](https://doi.org/10.1001/jamahealthforum.2022.4873). *JAMA Health Forum*, 3(12), e224873, 2022.
- NHS England (London). [Update on Cyber Incident: Clinical Impact in South East London — Friday 14 June 2024](https://www.england.nhs.uk/london/2024/06/14/update-on-cyber-incident-clinical-impact-in-south-east-london-friday-14-june-2024/). 14 June 2024.
- U.S. Department of Energy, Office of Cybersecurity, Energy Security, and Emergency Response. [Colonial Pipeline Cyber Incident](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident).
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

**Preguntas, revisiones y argumentación**

- Arksey, H., and O'Malley, L. [Scoping Studies: Towards a Methodological Framework](https://doi.org/10.1080/1364557032000119616). *International Journal of Social Research Methodology*, 8(1), 19–32, 2005.
- Chamberlin, T. C. [The Method of Multiple Working Hypotheses](https://doi.org/10.1126/science.148.3671.754). *Science*, 148(3671), 754–759, 1965 (reprint of the 1890 paper).
- Farrugia, P., Petrisor, B. A., Farrokhyar, F., and Bhandari, M. [Research Questions, Hypotheses and Objectives](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2912019/). *Canadian Journal of Surgery*, 53(4), 278–281, 2010.
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. [The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews](https://doi.org/10.1136/bmj.n71). *BMJ*, 372, n71, 2021.
- Platt, J. R. [Strong Inference](https://doi.org/10.1126/science.146.3642.347). *Science*, 146(3642), 347–353, 1964.
- Snyder, H. [Literature Review as a Research Methodology: An Overview and Guidelines](https://doi.org/10.1016/j.jbusres.2019.07.039). *Journal of Business Research*, 104, 333–339, 2019.
- Tricco, A. C., Lillie, E., Zarin, W., et al. [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/M18-0850). *Annals of Internal Medicine*, 169(7), 467–473, 2018.
- Webster, J., and Watson, R. T. [Analyzing the Past to Prepare for the Future: Writing a Literature Review](https://www.jstor.org/stable/4132319). *MIS Quarterly*, 26(2), xiii–xxiii, 2002.
- Wohlin, C. [Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering](https://doi.org/10.1145/2601248.2601268). *Proceedings of the 18th International Conference on Evaluation and Assessment in Software Engineering (EASE)*, 2014.

**Diseño y análisis cuantitativos**

- Abadie, A. [Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects](https://doi.org/10.1257/jel.20191450). *Journal of Economic Literature*, 59(2), 391–425, 2021.
- Barnett, A. G., van der Pols, J. C., and Dobson, A. J. [Regression to the Mean: What It Is and How to Deal With It](https://doi.org/10.1093/ije/dyh299). *International Journal of Epidemiology*, 34(1), 215–220, 2005.
- Durbin, J., and Watson, G. S. [Testing for Serial Correlation in Least Squares Regression. I](https://doi.org/10.1093/biomet/37.3-4.409). *Biometrika*, 37(3–4), 409–428, 1950.
- Gelman, A., and Loken, E. [The Statistical Crisis in Science](https://doi.org/10.1511/2014.111.460). *American Scientist*, 102(6), 460, 2014.
- Goodman-Bacon, A. [Difference-in-Differences with Variation in Treatment Timing](https://doi.org/10.1016/j.jeconom.2021.03.014). *Journal of Econometrics*, 225(2), 254–277, 2021.
- Greenland, S., Pearl, J., and Robins, J. M. [Causal Diagrams for Epidemiologic Research](https://doi.org/10.1097/00001648-199901000-00008). *Epidemiology*, 10(1), 37–48, 1999.
- Hategeka, C., Ruton, H., Karamouzian, M., Lynd, L. D., and Law, M. R. [Use of Interrupted Time Series Methods in the Evaluation of Health System Quality Improvement Interventions: A Methodological Systematic Review](https://doi.org/10.1136/bmjgh-2020-003567). *BMJ Global Health*, 5, e003567, 2020.
- Hernán, M. A., and Robins, J. M. [Causal Inference: What If](https://miguelhernan.org/whatifbook). Chapman & Hall/CRC, 2020 (open online edition).
- Lakens, D. [Sample Size Justification](https://doi.org/10.1525/collabra.33267). *Collabra: Psychology*, 8(1), 33267, 2022.
- Lipsitch, M., Tchetgen Tchetgen, E., and Cohen, T. [Negative Controls: A Tool for Detecting Confounding and Bias in Observational Studies](https://doi.org/10.1097/EDE.0b013e3181d61eeb). *Epidemiology*, 21(3), 383–388, 2010.
- Lopez Bernal, J., Cummins, S., and Gasparrini, A. [Interrupted Time Series Regression for the Evaluation of Public Health Interventions: A Tutorial](https://doi.org/10.1093/ije/dyw098). *International Journal of Epidemiology*, 46(1), 348–355, 2017.
- Newey, W. K., and West, K. D. [A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix](https://doi.org/10.2307/1913610). *Econometrica*, 55(3), 703–708, 1987.
- Roth, J., Sant'Anna, P. H. C., Bilinski, A., and Poe, J. [What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature](https://doi.org/10.1016/j.jeconom.2023.03.008). *Journal of Econometrics*, 235(2), 2218–2244, 2023.
- Simonsohn, U., Simmons, J. P., and Nelson, L. D. [Specification Curve Analysis](https://doi.org/10.1038/s41562-020-0912-z). *Nature Human Behaviour*, 4, 1208–1214, 2020.
- Steegen, S., Tuerlinckx, F., Gelman, A., and Vanpaemel, W. [Increasing Transparency Through a Multiverse Analysis](https://doi.org/10.1177/1745691616658637). *Perspectives on Psychological Science*, 11(5), 702–712, 2016.
- Wagner, A. K., Soumerai, S. B., Zhang, F., and Ross-Degnan, D. [Segmented Regression Analysis of Interrupted Time Series Studies in Medication Use Research](https://doi.org/10.1046/j.1365-2710.2002.00430.x). *Journal of Clinical Pharmacy and Therapeutics*, 27(4), 299–309, 2002.
- Wasserstein, R. L., and Lazar, N. A. [The ASA Statement on p-Values: Context, Process, and Purpose](https://doi.org/10.1080/00031305.2016.1154108). *The American Statistician*, 70(2), 129–133, 2016.

**Métodos cualitativos y mixtos**

- Braun, V., and Clarke, V. [Using Thematic Analysis in Psychology](https://doi.org/10.1191/1478088706qp063oa). *Qualitative Research in Psychology*, 3(2), 77–101, 2006.
- Cohen, J. [A Coefficient of Agreement for Nominal Scales](https://doi.org/10.1177/001316446002000104). *Educational and Psychological Measurement*, 20(1), 37–46, 1960.
- Fetters, M. D., Curry, L. A., and Creswell, J. W. [Achieving Integration in Mixed Methods Designs — Principles and Practices](https://doi.org/10.1111/1475-6773.12117). *Health Services Research*, 48(6 Pt 2), 2134–2156, 2013.
- Fischhoff, B. [Hindsight ≠ Foresight: The Effect of Outcome Knowledge on Judgment Under Uncertainty](https://doi.org/10.1037/0096-1523.1.3.288). *Journal of Experimental Psychology: Human Perception and Performance*, 1(3), 288–299, 1975.
- Guest, G., Bunce, A., and Johnson, L. [How Many Interviews Are Enough? An Experiment with Data Saturation and Variability](https://doi.org/10.1177/1525822X05279903). *Field Methods*, 18(1), 59–82, 2006.
- Malterud, K., Siersma, V. D., and Guassora, A. D. [Sample Size in Qualitative Interview Studies: Guided by Information Power](https://doi.org/10.1177/1049732315617444). *Qualitative Health Research*, 26(13), 1753–1760, 2016.
- McHugh, M. L. [Interrater Reliability: The Kappa Statistic](https://doi.org/10.11613/BM.2012.031). *Biochemia Medica*, 22(3), 276–282, 2012.
- O'Connor, C., and Joffe, H. [Intercoder Reliability in Qualitative Research: Debates and Practical Guidelines](https://doi.org/10.1177/1609406919899220). *International Journal of Qualitative Methods*, 19, 2020.

**Pilotos, comunicación, reproducibilidad y evaluación**

- Benchimol, E. I., Smeeth, L., Guttmann, A., et al. [The REporting of Studies Conducted Using Observational Routinely-Collected Health Data (RECORD) Statement](https://doi.org/10.1371/journal.pmed.1001885). *PLOS Medicine*, 12(10), e1001885, 2015.
- Eldridge, S. M., Chan, C. L., Campbell, M. J., et al. [CONSORT 2010 Statement: Extension to Randomised Pilot and Feasibility Trials](https://doi.org/10.1136/bmj.i5239). *BMJ*, 355, i5239, 2016.
- Lancaster, G. A., Dodd, S., and Williamson, P. R. [Design and Analysis of Pilot Studies: Recommendations for Good Practice](https://doi.org/10.1111/j..2002.384.doc.x). *Journal of Evaluation in Clinical Practice*, 10(2), 307–312, 2004.
- Leon, A. C., Davis, L. L., and Kraemer, H. C. [The Role and Interpretation of Pilot Studies in Clinical Research](https://doi.org/10.1016/j.jpsychires.2010.10.008). *Journal of Psychiatric Research*, 45(5), 626–629, 2011.
- Mullins, G., and Kiley, M. ['It's a PhD, Not a Nobel Prize': How Experienced Examiners Assess Research Theses](https://doi.org/10.1080/0307507022000011507). *Studies in Higher Education*, 27(4), 369–386, 2002.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606, 2018.
- O'Brien, B. C., Harris, I. B., Beckman, T. J., Reed, D. A., and Cook, D. A. [Standards for Reporting Qualitative Research: A Synthesis of Recommendations (SRQR)](https://doi.org/10.1097/ACM.0000000000000388). *Academic Medicine*, 89(9), 1245–1251, 2014.
- Open Science Framework. [OSF Registries](https://osf.io/registries).
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLOS Computational Biology*, 9(10), e1003285, 2013.
- Thabane, L., Ma, J., Chu, R., et al. [A Tutorial on Pilot Studies: The What, Why and How](https://doi.org/10.1186/1471-2288-10-1). *BMC Medical Research Methodology*, 10, 1, 2010.
- The Turing Way Community. [The Turing Way: A Handbook for Reproducible, Ethical and Collaborative Research](https://book.the-turing-way.org/).
- Tong, A., Sainsbury, P., and Craig, J. [Consolidated Criteria for Reporting Qualitative Research (COREQ): A 32-Item Checklist for Interviews and Focus Groups](https://doi.org/10.1093/intqhc/mzm042). *International Journal for Quality in Health Care*, 19(6), 349–357, 2007.
- von Elm, E., Altman, D. G., Egger, M., et al. [The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) Statement: Guidelines for Reporting Observational Studies](https://doi.org/10.1016/S0140-6736(07)61602-X). *The Lancet*, 370(9596), 1453–1457, 2007.
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. [The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18). *Scientific Data*, 3, 160018, 2016.

Material complementario de CyberABC: el [libro doctoral de infraestructura crítica](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md), que lleva los métodos de investigación de este libro a una contribución original basada en simulación.

**Límite del caso.** Tamsin Valley, Kestrel Health, Alder Point Hospital, Brookfield Community Hospital, Calloway General, Tamsin Valley EMS, el centro de despacho del condado, la Tamsin Valley Healthcare Coalition, la región de Wexmoor y sus hospitales, los entrevistados I01–I10, los registros con DOI que empiezan por 10.9999/syn, el Estudio de Desbordamiento y todos los números producidos por los laboratorios son inventados con fines didácticos. Las fuentes respaldan los enunciados generales junto a los que se citan, nunca los detalles sintéticos.

**Metadatos de la edición.** Edición en borrador, octubre de 2026. Revisor: pendiente. Verificación A4: todavía no renderizada.
