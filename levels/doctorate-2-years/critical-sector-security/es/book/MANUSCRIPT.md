# Infraestructura crítica y seguridad sectorial: métodos de investigación doctoral y práctica de la tesis

- Idioma: español (`es`), edición en español neutro internacional; programa de investigación doctoral, dos años; aproximadamente 1600 horas de estudio planificado (curso 207 de 207, el último curso de la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–8 de 8 tienen texto didáctico escrito en español, los ejercicios EX001–EX050 y sus resultados resueltos correspondientes, y sus laboratorios producen una salida idéntica a la de la edición en inglés. Siguen abiertas la revisión independiente de la materia, la nueva verificación de las fuentes, la revisión de accesibilidad, la revisión lingüística y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: investigadores avanzados que ya tienen experiencia de investigación y una pregunta defendible sobre la seguridad y la resiliencia de la infraestructura crítica: energía, agua, salud, transporte, comunicaciones, finanzas y servicios públicos. Conocimientos de entrada: el contenido previsto para los programas de [maestría](../../../../masters-2-years/critical-sector-security/en/book/PLAN.md) y de [posgrado](../../../../postgraduate-2-years/critical-sector-security/en/book/PLAN.md) de esta área (todavía esquemas en el momento de redactar), o experiencia profesional equivalente, además de soltura práctica en probabilidad, teoría básica de grafos, simulación y entrevistas cualitativas. El [curso doctoral complementario de seguridad de TO, IoT y sistemas ciberfísicos](../../../ot-iot-security/README.md) estudia en profundidad la capa de los sistemas de control; este libro estudia la capa *sectorial e intersectorial* que se sitúa por encima.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este programa es un plan educativo independiente. No es un programa de doctorado acreditado, no otorga ningún título y no concede autorización para acceder, escanear, probar o estudiar ninguna infraestructura, operador, conjunto de datos o persona reales. Toda organización, región, activo, persona, registro, conjunto de datos, banco de referencia y resultado numérico de un ejemplo resuelto es **sintético**, salvo que una frase cite explícitamente una fuente pública. Nada de este libro es un procedimiento operativo para una empresa de servicios real.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Lea los ocho capítulos en orden. Siguen el arco de un único proyecto doctoral. El capítulo 1 fija los estándares de integridad, seguridad y método que todo paso posterior debe cumplir en un ámbito donde un experimento descuidado puede dañar a las personas. El capítulo 2 traza la frontera de la investigación y encuentra una pregunta abierta genuina. El capítulo 3 la convierte en una contribución falsable. El capítulo 4 replica las líneas base que la contribución debe superar y pone a prueba el procedimiento del estudio en un piloto. El capítulo 5 ejecuta el estudio principal y lo valida de forma independiente. El capítulo 6 somete las afirmaciones a una crítica adversarial de pares y las revisa. El capítulo 7 ensambla la tesis y su archivo de reproducibilidad según las reglas de protección de la información que rigen los datos de infraestructura. El capítulo 8 prepara la defensa y un plan de publicación responsable.

Cada capítulo contiene secciones didácticas, definiciones, un ejemplo resuelto, una actividad práctica con código sin conexión, una lista de errores habituales y límites, ejercicios numerados y una síntesis. Escriba su propia respuesta a cada ejercicio antes de abrir los [resultados resueltos](#worked-results). A este nivel, la mayoría de los ejercicios tienen más de una respuesta defendible; los resultados resueltos muestran una y la rúbrica muestra lo que un revisor premiaría o rechazaría.

Mantenga cuatro etiquetas en cada nota de investigación que escriba mientras estudia este libro: **observación** (lo que registró una fuente identificada), **inferencia** (lo que usted concluye a partir de las observaciones y con qué supuestos), **afirmación** (el enunciado que pretende defender, con su alcance) y **decisión** (lo que alguien decidió hacer a causa de ello). En la investigación sobre infraestructura es indispensable una quinta etiqueta: **consecuencia**, el efecto físico, sanitario, económico o social sobre las personas que dependen de un servicio. La mayoría de los errores de este campo provienen de confundir una observación cibernética con una afirmación sobre consecuencias.

### Por qué un curso doctoral aparte sobre infraestructura crítica

La seguridad de la tecnología operativa (TO) pregunta cómo puede atacarse y defenderse un sistema de control. La seguridad de la infraestructura crítica (IC) plantea otro conjunto de preguntas: qué *funciones* no puede perder una sociedad, durante cuánto tiempo puede perderlas, cómo la pérdida de una se propaga a otras, quién es responsable de cada eslabón, qué reglas se aplican y cómo puede reunirse evidencia sobre todo ello sin poner en peligro los servicios estudiados. La unidad de análisis pasa del dispositivo y la planta al **servicio, el sector y el sistema de sistemas**. Una contribución doctoral en este campo puede ser un modelo, un método de medición, una evaluación de políticas, un estudio empírico de operadores o un principio de diseño validado; rara vez es un nuevo *exploit*, y casi nunca debería serlo.

### El corpus de investigación sintético usado en este libro

El libro sigue un proyecto doctoral inventado, el **Estudio Cascada** (*Cascade Study*), que pregunta si un *orden de restablecimiento consciente de las dependencias* —restablecer los alimentadores eléctricos en el orden en que los servicios críticos que sostienen agotarían de otro modo sus reservas— reduce la pérdida de servicios críticos tras una interrupción de la distribución inducida por un ciberataque, en comparación con un orden convencional que maximiza los clientes restablecidos, y a qué costo para los clientes ordinarios. Sus escenarios ficticios son:

| Elemento sintético | Papel en el libro | Límite |
|---|---|---|
| **Región de Riverbend** — Riverbend Electric Cooperative (REC), Riverbend Water Authority (RWA), St. Calder Hospital, central de Meridian Telecom, despacho de emergencias del condado de Riverbend | Contexto principal del estudio, con cuatro alimentadores de distribución F1–F4 (capítulos 1, 3 y 5). | Región inventada; ninguna empresa eléctrica, hospital, operador, personal, activo o registro reales. |
| **Port Halvard** | Segundo contexto, costero, con otra topología de alimentadores, dos cuadrillas de restablecimiento y contratos de reabastecimiento de combustible (validación independiente del capítulo 5, capítulo 6). | Región inventada. |
| **GridWater-Sim** | Un banco de referencia de cosimulación «publicado» y sintético cuya línea base no puede reproducirse al principio (capítulo 4). | Banco de referencia inventado; no es una herramienta ni un conjunto de datos reales y no debe buscarse. |
| Estudios sintéticos **P1–P8** | Artículos ficticios usados para practicar la evaluación crítica y el mapeo de la literatura (capítulo 2). | Inventados; representan tipos de estudio, no autores reales. |
| Participantes operadores **P01–P12** | Entrevistados y participantes ficticios en ejercicios de mesa (capítulos 1, 5 y 6). | Inventados; en este libro no aparece ningún dato de seres humanos. |

Todos los números que producen los laboratorios provienen de datos sintéticos impresos en el texto y se ejecutan solo con la biblioteca estándar de Python 3. Demuestran un método; no son hallazgos sobre ninguna infraestructura real.

### Política de fuentes

Cada enunciado factual sobre una norma, un reglamento, un incidente público o un estudio publicado enlaza con una fuente que el autor consultó. Las normas y los reglamentos cambian; cada uno se cita con su versión y su fecha y debe verificarse de nuevo antes de basarse en él. Cuando un concepto es vocabulario metodológico estándar (por ejemplo, la distinción entre verificación y validación de un modelo), el texto lo dice en lugar de inventar una referencia. Una fuente respalda el enunciado general junto al que aparece, nunca los detalles del caso sintético. Los informes públicos de incidentes se usan solo con el nivel de detalle que divulgaron sus editores, y no se reproduce ninguna instrucción operativa de ataque. En esta edición, las referencias se mantienen idénticas a las de la edición en inglés y los títulos de las obras se citan en su idioma original.

## Contenido

1. [Integridad y métodos avanzados de investigación](#ch-01): la consecuencia como objeto de estudio, la evidencia en la investigación sobre infraestructura, la ética de la seguridad y del doble uso, la información protegida, las métricas de resiliencia y el protocolo defendible.
2. [Infraestructura crítica y seguridad sectorial: frontera de la investigación](#ch-02): panorama de políticas y normas, familias de modelos de interdependencia, investigación sobre detección y bancos de pruebas, evidencia específica de cada sector y una brecha falsable.
3. [Propuesta de contribución original](#ch-03): mecanismo, grafos de dependencias con reservas, hipótesis, líneas base, explicaciones rivales y condiciones de falla declaradas de antemano.
4. [Replicación de las líneas base y piloto](#ch-04): reproducción de un modelo de inoperabilidad y de un banco de referencia de detección, trampas de la evaluación, verificación del modelo y un piloto acotado.
5. [Estudio principal y validación independiente](#ch-05): experimentos de simulación con incertidumbre, estudios de mesa con operadores, validación frente a la historia y a expertos, y un segundo contexto.
6. [Crítica de pares y revisión](#ch-06): circularidad modelo–política, condiciones de contorno, desajuste del modelo, resultados negativos, revisión de doble uso y acotación de las afirmaciones.
7. [Síntesis de la tesis y archivo de reproducibilidad](#ch-07): estructura argumental, divulgación de artefactos por niveles según las reglas de información de infraestructura, datos sintéticos y documentación del modelo.
8. [Defensa y plan de publicación](#ch-08): auditoría de las afirmaciones, preparación de la defensa, foros de publicación, divulgación coordinada, traducción a políticas y el programa de investigación posdoctoral.

Los [resultados resueltos](#worked-results) contienen EX001–EX050. Un [glosario](#glossary) y las [referencias](#references) cierran el libro.

<a id="ch-01"></a>

## Capítulo 1 — Integridad y métodos avanzados de investigación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, el estudiante será capaz de:

1. Definir infraestructura crítica, función crítica, dependencia, interdependencia y resiliencia con la precisión suficiente para asociar una medición a cada término, y explicar por qué las definiciones que usan distintos gobiernos no son intercambiables.
2. Distinguir las observaciones cibernéticas de las afirmaciones sobre consecuencias y precisar qué evidencia se necesita para pasar de unas a otras.
3. Aplicar salvaguardas de integridad de la investigación —preespecificación, registros de desviaciones, separación entre trabajo exploratorio y confirmatorio, declaración de conflictos de interés— a estudios cuyos socios son operadores regulados.
4. Identificar los riesgos de seguridad física, de doble uso, jurídicos y de protección de la información propios de la investigación sobre infraestructura y diseñar salvaguardas proporcionadas, usando los principios del Informe Menlo como estructura de trabajo.
5. Elegir y defender métricas de resiliencia y de consecuencia, reconociendo que la elección de la métrica puede invertir la clasificación de los escenarios y que las ventanas de observación censuran las interrupciones no recuperadas.
6. Redactar un protocolo de investigación que un revisor hostil pero justo —y el responsable de seguridad de una empresa de servicios— pueda auditar, incluidas las condiciones de detención.

El capítulo es el contrato metodológico del resto del libro. El capítulo 2 lee la literatura con su vocabulario de evidencia; el capítulo 3 usa su plantilla de protocolo; los capítulos 4 y 5 usan sus métricas y sus herramientas de validez; los capítulos 6 a 8 usan sus estándares de integridad, seguridad y protección de la información para juzgar el trabajo terminado.

### 1.1 Qué se estudia: servicios, funciones y consecuencias



#### 1.1.1 Definiciones que tienen peso

«Infraestructura crítica» es un término jurídico y de política pública antes que técnico, y su definición decide hacia qué puede generalizar un estudio. En los Estados Unidos, la definición legal de la USA PATRIOT Act (42 U.S.C. § 5195c(e)) describe sistemas y activos «so vital to the United States that the incapacity or destruction of such systems and assets would have a debilitating impact on security, national economic security, national public health or safety». La política estadounidense organiza esos activos en sectores; el [National Security Memorandum on Critical Infrastructure Security and Resilience (NSM-22)](https://www.govinfo.gov/content/pkg/DCPD-202400358/html/DCPD-202400358.htm), emitido el 30 de abril de 2024, derogó y sustituyó la Presidential Policy Directive 21 (2013), mantuvo la estructura sectorial, designó a la Cybersecurity and Infrastructure Security Agency (CISA) como coordinadora nacional y asignó las Sector Risk Management Agencies ([resumen de CISA](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience); [resumen del Congressional Research Service](https://www.congress.gov/crs-product/IF12716)). El resumen del CRS señala que una administración posterior puede derogar o modificar el NSM-22 sin intervención del Congreso, de modo que una tesis debe citar el instrumento vigente en una fecha declarada.

La Unión Europea usa dos instrumentos coordinados: la [Directiva (UE) 2022/2557 relativa a la resiliencia de las entidades críticas (CER)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj), para la resiliencia frente a todos los peligros de las entidades críticas designadas, y la [Directiva (UE) 2022/2555 (NIS2)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/), para la ciberseguridad de las entidades esenciales e importantes. Un estudio que llama a un hospital «infraestructura crítica» en el sentido estadounidense y «entidad esencial» en el sentido de NIS2 no está usando sinónimos: las poblaciones difieren, las obligaciones difieren y los umbrales de notificación difieren.

Una perspectiva complementaria es la **función** en lugar del activo. El [National Critical Functions set](https://www.cisa.gov/national-critical-functions-set) de CISA, publicado en abril de 2019, enumera 55 funciones agrupadas en *Connect*, *Distribute*, *Manage* y *Supply*; por ejemplo, «Distribute electricity» o «Supply water». Las funciones atraviesan sectores y organizaciones. Para la investigación, la perspectiva funcional tiene una ventaja decisiva: nombra algo cuya *pérdida* puede medirse (servicio prestado, personas afectadas, duración) y no algo cuyo *compromiso* puede observarse (un equipo, una credencial, un controlador).

Definiciones de trabajo usadas en este libro:

| Término | Definición de trabajo | Qué hay que medir para usarlo |
|---|---|---|
| **Servicio crítico** | Un servicio cuya interrupción más allá de una duración declarada causa daño a la salud, la seguridad, la protección o la actividad económica esencial de una población declarada. | Población atendida, umbral de daño, duración tolerable de la interrupción. |
| **Dependencia** | Una relación unidireccional en la que el estado del servicio *B* depende del servicio *A* ([Rinaldi, Peerenboom y Kelly, 2001](https://doi.org/10.1109/37.969131)). | Dirección, tipo, reserva, intensidad del acoplamiento. |
| **Interdependencia** | Una relación bidireccional: el estado de cada servicio depende del otro, directamente o a través de una cadena (misma fuente). | El ciclo y su temporización. |
| **Reserva** | Capacidad almacenada que permite a un dependiente seguir operando después de perder a un proveedor: combustible, baterías, almacenamiento de agua, inventario, procedimientos manuales. | Duración con una carga declarada y cómo se agota. |
| **Consecuencia** | El efecto sobre las personas y sobre las funciones de las que dependen, medido en unidades de servicio (clientes-hora, derivaciones de pacientes, litros no suministrados). | Una unidad, una población, una ventana temporal. |
| **Resiliencia** | La capacidad de un sistema para resistir, absorber, recuperarse y adaptarse ante una perturbación; se operacionaliza mediante métricas sobre una curva de desempeño (§1.6). | Una medida de desempeño en el tiempo y un resumen elegido. |

Rinaldi, Peerenboom y Kelly clasifican las interdependencias como **físicas** (un producto material de una es insumo de otra), **cibernéticas** (dependencia de información transmitida por una infraestructura de información), **geográficas** (un evento local afecta a componentes ubicados en el mismo lugar) y **lógicas** (cualquier otro mecanismo, como los mercados o las políticas). Sus seis «dimensiones» —entorno, acoplamiento y comportamiento de respuesta, tipo de falla (en cascada, escalonada, de causa común), características de la infraestructura, estado de operación y tipo de interdependencia— siguen siendo una lista de verificación útil de lo que un modelo ignora. Un estudio doctoral debe declarar cuáles de esas dimensiones modela y cuáles mantiene fijas.

#### 1.1.2 La observación cibernética no es la consecuencia

El problema epistémico que define el campo es la distancia entre lo que puede observarse de un evento cibernético y lo que les ocurrió a las personas. Consideremos tres ejemplos públicos, descritos solo con el nivel de detalle que divulgaron sus editores:

- El ataque de diciembre de 2015 contra tres empresas distribuidoras de electricidad de Ucrania interrumpió el suministro a unos 225 000 clientes durante varias horas; el [caso de uso de defensa conjunto de E-ISAC y SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and) (marzo de 2016) describe el robo de credenciales, la operación remota de sistemas de gestión de la distribución, malware destructivo y una denegación de servicio telefónica contra los centros de atención al cliente. La *consecuencia* (clientes sin electricidad, durante horas) dependió de la capacidad de los operadores para restablecer el servicio manualmente, una reserva que era organizativa y no técnica.
- El malware que CISA describe como [CrashOverride](https://www.cisa.gov/news-events/alerts/2017/06/12/crashoverride-malware) (alerta TA17-163A, junio de 2017) atacó subestaciones eléctricas de Ucrania en 2016. Un análisis de capacidades de un malware dice qué *podría* ordenarse; por sí solo no dice qué *se perdió*.
- El análisis de CISA sobre [HatMan (también conocido como TRITON o TRISIS)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf) describe un malware dirigido a un sistema instrumentado de seguridad. Aquí la consecuencia más importante es una que no ocurrió, y las afirmaciones de investigación sobre «cuasi accidentes» requieren un cuidado especial porque el contrafáctico no es observable.

Cada caso vincula una observación cibernética (malware, acceso, comandos) con una consecuencia (interrupción, disparo, daño evitado) a través de una cadena de mecanismos físicos y organizativos. Una afirmación de investigación que salta la cadena —«los ataques contra subestaciones causan apagones»— no es tanto falsa como infundada. Escriba la cadena de forma explícita; cada eslabón es un punto donde una reserva, un procedimiento manual, un sistema de protección o una decisión humana pueden romperla.

#### 1.1.3 La escalera de afirmaciones para la investigación sobre infraestructura

El libro doctoral de respuesta a incidentes de esta serie introdujo una escalera de afirmaciones ([observación, inferencia, afirmación de caso, afirmación de investigación](../../../incident-response-resilience/en/book/MANUSCRIPT.md#ch-01)). La investigación sobre infraestructura necesita un peldaño más, porque las afirmaciones centrales del campo tratan de consecuencias en sistemas físicos que el investigador normalmente no puede observar de forma directa:

| Nivel | Tipo de enunciado | Ejemplo (sintético) | Evidencia típica |
|---|---|---|---|
| L1 Observación | Una fuente identificada registró algo. | «El sistema de gestión de interrupciones de REC registró el alimentador F3 abierto a las 02:10». | Registro preservado con el estado del reloj. |
| L2 Inferencia | Una conclusión a partir de observaciones bajo supuestos declarados. | «F3 fue abierto por un comando remoto, no por la protección». | Registros de comandos, registros de eventos de relés, supuestos declarados. |
| L3 Afirmación de caso | Un enunciado sobre lo que ocurrió en un evento. | «La planta de tratamiento funcionó con generador durante 7 h y luego perdió presión en la zona alta». | Registros convergentes de varios propietarios. |
| L4 Afirmación de consecuencia | Un enunciado sobre efectos en personas o funciones. | «Unos 2500 clientes carecieron de presión de agua potable durante unas 5 h». | Registros de servicio, reportes de clientes, verificación en campo. |
| L5 Afirmación de investigación | Un enunciado general sobre una población de sistemas o eventos. | «El restablecimiento consciente de las dependencias reduce la pérdida de servicios críticos en las interrupciones de distribución». | Muchos casos, un modelo validado o un estudio diseñado. |

Subir un peldaño siempre añade supuestos. El protocolo de §1.8 exige que cada afirmación de una tesis lleve la etiqueta de su peldaño y de sus supuestos.

### 1.2 La evidencia en la investigación sobre infraestructura



#### 1.2.1 Cinco fuentes de evidencia y sus sesgos característicos

1. **Registros de incidentes e informes públicos.** Escasos, divulgados de forma selectiva, escritos con fines distintos de la investigación y moldeados por la exposición jurídica. El sesgo de publicación es extremo: se reportan los eventos con consecuencias dramáticas o adversarios atribuibles; las perturbaciones absorbidas en silencio, no. La *población* de incidentes es desconocida.
2. **Datos operativos de los socios.** Historiadores SCADA, registros de gestión de interrupciones, órdenes de trabajo, registros de alarmas. Alta fidelidad, pero son propiedad del operador, a menudo están protegidos por ley o por contrato y los producen sistemas ajustados para la operación y no para la medición. El muestreo lo decide la disposición del socio, que se correlaciona con su madurez.
3. **Bancos de pruebas.** Plantas de laboratorio físicas o híbridas, como el banco de pruebas Secure Water Treatment (SWaT) descrito por [Goh, Adepu, Junejo y Mathur (2016)](https://doi.org/10.1007/978-3-319-71368-7_8). Permiten ataques controlados y datos etiquetados, a costa de escala, antigüedad y realismo: una planta didáctica de seis etapas no es el sistema de agua de una ciudad.
4. **Modelos y simulaciones.** Modelos de redes, de flujos, de insumo-producto, basados en agentes, de dinámica de sistemas y de cosimulación (capítulo 2). Permiten contrafácticos y escala, pero solo prueban lo que su estructura y sus parámetros permiten; su validez debe establecerse, no suponerse ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)).
5. **Personas.** Entrevistas, encuestas, ejercicios de mesa y observación de operadores, gestores de emergencias y reguladores. Revelan reservas que solo existen como práctica —soluciones manuales, ayuda mutua informal— y también revelan lo que las personas *dicen* que harían, que no es lo que hacen bajo estrés.

El trabajo doctoral sólido **triangula**: la predicción de un modelo se contrasta con un registro histórico, un experimento en banco de pruebas y el juicio de los operadores, y la tesis explica qué puede y qué no puede respaldar cada fuente.

#### 1.2.2 El problema de la tasa base y del denominador

Los incidentes de infraestructura con consecuencias físicas son raros. Un estudio que recopila «incidentes cibernéticos que afectan a empresas de servicios» a partir de fuentes públicas tiene un numerador sin denominador: no puede decir con qué frecuencia ocurren esos incidentes, solo con qué frecuencia se *reportan*. Las tasas requieren una población definida (todas las empresas de servicios de un tipo en una jurisdicción), un período definido y un mecanismo de notificación de completitud conocida. Los regímenes de notificación obligatoria podrían ayudar con el tiempo: la Cyber Incident Reporting for Critical Infrastructure Act de 2022 (CIRCIA) de los Estados Unidos obliga a CISA a dictar normas; la propuesta de norma de CISA de 2024 exigiría notificar los incidentes cubiertos en un plazo de 72 horas y los pagos de rescate en 24 horas, y la norma final se envió a revisión interinstitucional el 1 de octubre de 2026 tras incumplir plazos anteriores ([Inside Privacy, 2026](https://www.insideprivacy.com/critical-infrastructure/cisa-submits-final-circia-rule-for-omb-review/)). Mientras no se publique y entre en vigor una norma final, y mientras sus datos no se pongan a disposición de los investigadores bajo algún régimen de acceso, ninguna tesis debe tratar las obligaciones de notificación como datos.

#### 1.2.3 Retrospectiva, contrafácticos y «cuasi accidentes»

Las afirmaciones sobre consecuencias en este campo suelen ser contrafácticas: «si los operadores no hubieran pasado al control manual, la interrupción habría durado días». Los contrafácticos son objetos de investigación legítimos solo cuando los produce un modelo explícito cuyos supuestos se divulgan y cuya sensibilidad se reporta. La retrospectiva hace que el camino real parezca inevitable y que las alternativas parezcan obvias; el diseño del ejercicio de mesa del capítulo 5 muestra cómo presentar escenarios a los participantes sin que conozcan el desenlace.

### 1.3 Integridad cuando los socios son operadores regulados



#### 1.3.1 Presiones específicas del campo

Las prácticas de investigación cuestionables —reporte selectivo, análisis flexible, formular hipótesis después de conocer los resultados— son generales ([Simmons, Nelson y Simonsohn, 2011](https://doi.org/10.1177/0956797611417632); [Kerr, 1998](https://doi.org/10.1207/s15327957pspr0203_4)). La investigación sobre infraestructura añade cuatro presiones:

- **Exposición regulatoria.** Un operador socio puede temer que un hallazgo se lea como incumplimiento. La presión para suavizar o retrasar resultados es previsible y debe gestionarse con un acuerdo de publicación escrito *antes* del acceso a los datos (§1.5.3).
- **Financiación por partes interesadas.** Los proveedores de productos de detección, las asociaciones sectoriales y las agencias financian investigación. La financiación no es corrupción, pero la financiación no declarada es una falla de integridad, y presentar de forma favorable el producto de un financiador es un riesgo conocido.
- **Clasificación y sensibilidad.** Algunos resultados no pueden publicarse completos. La tentación es publicar la parte favorable. La regla de este libro: si un resultado no puede publicarse, la *existencia* del análisis retenido y su dirección deben comunicarse a los examinadores en el marco del acuerdo de acceso, y el texto público no debe afirmar más de lo que respalda la evidencia pública.
- **Flexibilidad de la simulación.** Un modelo tiene muchos parámetros libres. Ajustarlos hasta que un método propuesto gane es el equivalente en simulación del *p-hacking*. La salvaguarda consiste en fijar las distribuciones de parámetros, los conjuntos de escenarios y las métricas antes de comparar métodos (capítulo 3), y en reportar todas las familias de escenarios, no solo aquellas en las que el método gana.

#### 1.3.2 Preespecificación para estudios de simulación y de métodos mixtos

El prerregistro no es solo para experimentos con participantes humanos ([Nosek et al., 2018](https://doi.org/10.1073/pnas.1708274114)). En un estudio de simulación, preespecifique: la versión del modelo y sus pruebas de verificación; las distribuciones de parámetros y sus fuentes; las familias de escenarios y cuántas extracciones de cada una; las políticas de comparación, incluida la línea base más fuerte disponible; la métrica primaria, la métrica secundaria o de seguridad y cualquier margen de no inferioridad; las semillas; y el análisis (diferencias pareadas, método de intervalos). En entrevistas y ejercicios de mesa, preespecifique el marco muestral, el protocolo, las categorías iniciales del marco de codificación y la regla para añadir categorías. Un **registro de desviaciones** anota cada cambio con fecha, motivo y si ya se habían visto los resultados.

#### 1.3.3 Originalidad y procedencia

La literatura sobre infraestructura está repartida entre la ingeniería, la investigación de operaciones, la economía, las políticas públicas y la seguridad informática, y la misma idea se redescubre a menudo con otros nombres: «restablecimiento consciente de las dependencias» en ingeniería eléctrica, «priorización del restablecimiento» en gestión de emergencias, «criticidad a nivel de servicio» en TI. Por eso, una afirmación doctoral de originalidad necesita una búsqueda entre disciplinas (capítulo 2) y una declaración honesta de qué es nuevo: el método, la aplicación, la evidencia o la síntesis.

### 1.4 Seguridad, doble uso y ética



#### 1.4.1 Por qué la investigación sobre infraestructura necesita su propio análisis ético

El [Informe Menlo](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) (Dittrich y Kenneally, 2012) adaptó los principios de Belmont —respeto por las personas, beneficencia, justicia— a la investigación en tecnologías de la información y la comunicación y añadió el **respeto por la ley y el interés público**. Aplicarlo a la investigación sobre infraestructura revela partes interesadas ausentes en la mayoría de los estudios de seguridad: la población atendida por la infraestructura, que nunca dio su consentimiento y puede salir perjudicada por un experimento que sale mal; el personal del operador, que puede quedar expuesto a culpas; y los terceros conectados por interdependencia.

| Principio de Menlo | Aplicación específica a la infraestructura |
|---|---|
| Respeto por las personas | Consentimiento informado del personal entrevistado u observado; protección frente al uso disciplinario de los datos de investigación; consentimiento separado para la grabación de audio. La población atendida no puede consentir, de modo que sus intereses deben representarse mediante la minimización del riesgo. |
| Beneficencia | Ningún experimento sobre sistemas de control en producción. Revisión de seguridad física para cualquier laboratorio que energice equipos. Ponderar el beneficio de publicar una vulnerabilidad o un patrón de debilidad frente a la ventaja que da a un adversario. |
| Justicia | No concentrar la carga de la investigación (y el riesgo de exposición) en empresas de servicios pequeñas y con pocos recursos que no pueden decir que no a un financiador; no diseñar métodos de restablecimiento que perjudiquen sistemáticamente a una población sin decirlo (el margen de no inferioridad del capítulo 3). |
| Respeto por la ley y el interés público | Cumplir los regímenes de protección de la información (§1.5), los controles de exportación cuando corresponda, la legislación sobre uso indebido de sistemas informáticos y los contratos con los socios; ser transparente sobre los métodos para servir al interés público en una investigación que rinda cuentas. |

#### 1.4.2 Reglas estrictas usadas en este libro

1. **Nunca pruebe en producción.** Ningún escaneo, sondeo, *fuzzing* ni inyección de comandos contra ningún sistema operativo en funcionamiento, incluido el «solo leer» con protocolos industriales, sin una autorización escrita del propietario del activo que indique alcance, horario, controles de seguridad y una autoridad de detención. La [Guide to Operational Technology Security, SP 800-82 Rev. 3](https://doi.org/10.6028/NIST.SP.800-82r3) del NIST (septiembre de 2023) explica por qué la TO difiere de la TI: predominan la disponibilidad y la seguridad física, los dispositivos pueden fallar con un tráfico que los sistemas de TI toleran y los cambios requieren revisión de ingeniería. El NIST publicó un borrador público inicial de la Revisión 4 en septiembre de 2026, con comentarios hasta el 30 de noviembre de 2026 ([página del CSRC](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); cite la revisión que usó.
2. **Simule o emule primero.** Use modelos, cosimulación, gemelos digitales o bancos de pruebas aislados. Cuando se usa un banco de pruebas físico, este necesita su propio caso de seguridad (presión, tensión, dosificación química) revisado por un ingeniero calificado.
3. **Separe la capacidad de la consecuencia al publicar.** Una tesis puede publicar cómo se propaga una clase de falla y qué reservas la detienen; no debe publicar una lista de objetivos específicos por activo ni un camino paso a paso hacia un efecto físico.
4. **Tenga una autoridad de detención.** Todo estudio que involucre al personal o a los sistemas de un socio nombra a una persona del lado del socio que puede detenerlo de inmediato, y el protocolo dice qué pasa con los datos recogidos antes de la detención.

#### 1.4.3 Revisión de doble uso

Una revisión de doble uso plantea tres preguntas antes de cualquier publicación: *Ventaja*: ¿este resultado facilita de forma sustancial que un adversario cause daño, en comparación con lo que ya es público? *Valor defensivo*: ¿ayuda más a los defensores que a los atacantes, y tienen los defensores los medios para actuar en consecuencia? *Mitigación*: ¿puede generalizarse la parte dañina, retrasarse (hasta que existan correcciones) o pasarse a acceso controlado sin perder valor científico? El capítulo 6 realiza una revisión completa de doble uso de los resultados del Estudio Cascada; el capítulo 8 la sitúa en un calendario de divulgación coordinada.

### 1.5 Información protegida y acuerdos de datos



#### 1.5.1 Regímenes que encontrará el investigador

Los datos de infraestructura suelen estar sujetos a regímenes jurídicos de protección distintos de la legislación sobre datos personales. En los Estados Unidos, algunos ejemplos son la Protected Critical Infrastructure Information (PCII), la Chemical-terrorism Vulnerability Information (CVI), la Sensitive Security Information (SSI) en el transporte y la Critical Energy/Electric Infrastructure Information (CEII) en la Federal Energy Regulatory Commission. Su alcance y sus reglas de tratamiento los definen leyes y reglamentos, y cambian con el tiempo; lea la regla vigente y la interpretación del socio antes de aceptar datos. En la UE, la CER y NIS2 imponen confidencialidad sobre la información intercambiada con las autoridades. Los datos personales de notas de entrevistas, listas de turnos y grabaciones de llamadas están sujetos a la legislación ordinaria de privacidad (por ejemplo, el RGPD en la UE). *Nota para el lector hispanohablante:* en España, el RGPD se complementa con la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales; en América Latina rige la ley de cada país, por ejemplo la Ley 25.326 en Argentina o la Ley 1581 de 2012 en Colombia. Este libro no da asesoramiento jurídico. Exige que el protocolo (§1.8) nombre cada régimen que pueda aplicarse, a la persona que decidió si se aplica y la consecuencia para el tratamiento.

#### 1.5.2 La prueba de sensibilidad de la información

Incluso sin un régimen formal, aplique una prueba de sensibilidad a cada artefacto: *¿identifica un activo específico, su ubicación, su vulnerabilidad o su dependencia de una manera que ayudaría a alguien a dañarlo?* Los mapas de alimentador a instalación, las capacidades de combustible de los generadores, las rutas de comunicación de respaldo y las prioridades de restablecimiento son exactamente lo que busca un adversario que planifica un efecto en cascada. Los datos centrales del Estudio Cascada —qué alimentador abastece a qué instalación crítica y cuánto dura su reserva— son, por tanto, sensibles *aunque cada número sea aproximado*. El capítulo 7 construye los niveles de divulgación que se derivan de esto.

#### 1.5.3 Acuerdos antes del acceso

Negocie antes de recoger nada: un acuerdo de uso de datos (alcance, almacenamiento, conservación, destrucción, notificación de brechas); un acuerdo de publicación (el socio puede revisar en busca de información protegida y de errores de hecho dentro de un plazo fijo, pero no puede vetar los hallazgos que no le gusten); una política de autoría y agradecimientos; y una cláusula de protección del personal (los datos de investigación no se usarán con fines disciplinarios). Registre los acuerdos en el apéndice del protocolo. Un estudio sin acuerdo de publicación ha concedido, en la práctica, un veto a su socio.

### 1.6 Medición: métricas de resiliencia y de consecuencia



#### 1.6.1 La curva de desempeño

La mayoría de las métricas cuantitativas de resiliencia resumen una **curva de desempeño** *Q(t)*: la fracción del servicio normal prestada a lo largo del tiempo, antes, durante y después de una perturbación. [Bruneau et al. (2003)](https://doi.org/10.1193/1.1623497) plantearon la resiliencia sísmica de las comunidades en términos de menor probabilidad de falla, menores consecuencias y menor tiempo de recuperación, y su muy reproducido «triángulo de resiliencia» mide la pérdida como el área entre el servicio pleno y *Q(t)* durante el período de recuperación. [Haimes (2009)](https://doi.org/10.1111/j.1539-6924.2009.01216.x) sostuvo que la resiliencia es función de la amenaza específica y del estado del sistema, no una propiedad única. La [SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1) del NIST (diciembre de 2021) define la ciberresiliencia como la capacidad de anticipar, resistir, recuperarse y adaptarse ante condiciones adversas, tensiones o ataques contra sistemas que usan recursos cibernéticos o dependen de ellos.

Resúmenes habituales de *Q(t)*:

| Métrica | Definición | Sensible a | Ciega a |
|---|---|---|---|
| Pérdida de resiliencia (área) | ∫ (1 − Q(t)) dt en la ventana | Profundidad × duración | Si una pérdida breve y profunda es peor para las personas que una larga y superficial |
| Peor desempeño | 1 − min Q(t) | Profundidad | Duración |
| Tiempo hasta la recuperación | Primer instante de servicio pleno menos el inicio de la perturbación | Duración | Profundidad |
| Clientes-hora perdidos | Σ clientes × horas sin servicio | Población y duración | Criticidad de los clientes |
| Pérdida ponderada de servicios críticos | Σ peso × horas en que un servicio crítico no está disponible | Prioridades declaradas de antemano | Clientes ordinarios, salvo que se incluyan |

Ninguna métrica es neutral. Cada una incorpora un juicio de valor sobre qué pérdidas cuentan y cómo se compensa la profundidad con la duración. Un estudio doctoral debe justificar su métrica primaria por la decisión que informa, reportar al menos una alternativa y mostrar si las conclusiones cambian.

#### 1.6.2 Censura

Si un servicio no se ha recuperado cuando se cierra la ventana de observación, su tiempo hasta la recuperación está **censurado**: el valor verdadero es al menos el valor observado. Promediar duraciones censuradas como si fueran completas sesga los resultados hacia una recuperación más rápida. Reporte el número de casos censurados, use métodos de supervivencia cuando la muestra lo permita o amplíe la ventana. En las simulaciones, la ventana es una decisión de diseño; elíjala de modo que la censura sea rara con todas las políticas comparadas, o repórtela.

#### 1.6.3 Validez de constructo de los pesos de consecuencia

Una métrica de consecuencia ponderada necesita pesos. Los pesos obtenidos de operadores, gestores de emergencias o marcos de criticidad publicados son juicios de valor, no mediciones. Declárelos de antemano, cite de dónde provienen y realice el análisis con conjuntos de pesos alternativos (capítulo 6). Si la conclusión depende de un único conjunto de pesos, la afirmación debe decirlo.

### 1.7 Modos de falla habituales en las afirmaciones de investigación sobre infraestructura

- **Salto de lo cibernético a la consecuencia.** Tratar el acceso o la capacidad de un malware como evidencia de consecuencia física.
- **La topología como realidad.** Usar un diagrama de red como si capturara flujos, reservas, protecciones y operadores humanos.
- **Generalización desde el banco de pruebas.** Reportar la exactitud de detección en un banco de pruebas pequeño como exactitud «para sistemas de agua».
- **Simulación no validada.** Presentar salidas de un modelo sin verificación, sin comparación con ningún evento histórico y sin análisis de sensibilidad.
- **Búsqueda de la métrica conveniente.** Reportar la métrica de resiliencia que favorezca al método propuesto.
- **Muestrear por el desenlace dramático.** Construir teoría solo a partir de incidentes famosos.
- **Ignorar la reserva humana.** Omitir la operación manual, la ayuda mutua y la improvisación, que los informes públicos señalan repetidamente como decisivas en el restablecimiento.
- **Sensibilidad silenciosa.** Publicar datos que permiten seleccionar objetivos porque cada número «parecía inofensivo».

### 1.8 Redactar un protocolo de investigación defendible

Un protocolo para un estudio de infraestructura contiene, como mínimo:

1. **Pregunta y peldaño de la afirmación.** La pregunta de investigación, la afirmación buscada, su peldaño (L1–L5) y su alcance (sistemas, sectores, jurisdicciones, peligros).
2. **Definiciones y métricas.** Cada constructo, su operacionalización, las métricas primaria y secundaria, la ventana y la regla de censura.
3. **Fuentes de evidencia.** Cuáles de las cinco fuentes (§1.2.1), por qué y qué no puede respaldar cada una.
4. **Diseño.** Condiciones de comparación, líneas base, familias de escenarios, muestreo, asignación.
5. **Preespecificación.** Qué se fija antes de los resultados; el registro de desviaciones.
6. **Seguridad y ética.** Análisis de Menlo, reglas estrictas (§1.4.2), revisión de seguridad física, autoridad de detención, aprobación para investigación con seres humanos cuando corresponda.
7. **Protección de la información.** Regímenes aplicables, prueba de sensibilidad, almacenamiento, niveles de divulgación.
8. **Acuerdos.** Uso de datos, publicación, autoría, protección del personal.
9. **Plan de análisis.** Estimadores, incertidumbre, análisis de sensibilidad, métricas y pesos alternativos.
10. **Condiciones de detención y de abandono.** Cuándo se detiene el estudio (seguridad, retirada del socio, brecha de datos) y cuándo se abandona o se acota la afirmación (condiciones de falla declaradas de antemano, capítulo 3).
11. **Conflictos de interés y financiación.**
12. **Plan de reproducibilidad.** Qué se divulgará y en qué nivel (capítulo 7).

### 1.9 Ejemplo resuelto: la primera revisión del protocolo del Estudio Cascada

El doctorando (sintético) propone estudiar el orden de restablecimiento en la Región de Riverbend. El primer borrador dice: *«Obtendremos los registros de interrupciones y los registros SCADA de REC de los últimos cinco años, identificaremos las interrupciones relacionadas con incidentes cibernéticos y mostraremos que restablecer primero a los clientes críticos habría reducido el daño».* Una revisión del protocolo encuentra:

| Problema | Por qué falla | Revisión |
|---|---|---|
| «Interrupciones relacionadas con incidentes cibernéticos» en cinco años de una sola cooperativa | Probablemente cero o un evento; sin denominador; sin variación que estudiar. | Usar las interrupciones históricas de distribución *por cualquier causa* para calibrar las duraciones de restablecimiento, y una cosimulación para los escenarios cibernéticos. |
| «Habría reducido el daño» | Contrafáctico sin modelo; retrospectiva. | Modelo explícito con parámetros declarados de antemano; ejercicio de mesa con operadores que desconocen el desenlace. |
| «Primero los clientes críticos» | Indefinido; confunde el número de clientes con la criticidad. | Definir los servicios críticos (central de telecomunicaciones, tratamiento de agua, hospital, despacho de emergencias), sus reservas y pesos declarados de antemano. |
| Se solicitan registros SCADA | Alta sensibilidad; no se necesitan para la pregunta. | Solicitar resúmenes de gestión de interrupciones a nivel de alimentador, agregados; ningún dato de red ni de protocolo. |
| Sin acuerdo con el socio | Veto del socio por defecto. | Acuerdos de uso de datos y de publicación con una revisión de hechos de 30 días y sin veto sobre los hallazgos. |
| Sin métrica de seguridad | Un método que ayuda a los hospitales pero deja a miles de hogares a oscuras durante más tiempo es una decisión de política. | Métrica secundaria: clientes-hora perdidos, con un margen de no inferioridad justificado junto con el socio (capítulo 3). |
| El mapa alimentador–instalación aparecería en la tesis | Valor para seleccionar objetivos. | Región sintética en el texto público; el mapeo real, solo en un apéndice de acceso controlado, si acaso. |

La pregunta revisada pasa a ser: *En las interrupciones de distribución que exigen un restablecimiento manual y secuencial de los alimentadores, ¿ordenar el restablecimiento según el tiempo hasta el impacto de los servicios críticos reduce la pérdida ponderada de servicios críticos en comparación con ordenarlo según los clientes restablecidos, y en cuánto aumenta los clientes-hora perdidos?* Es respondible, medible, segura de estudiar y honesta sobre su compromiso.

### 1.10 Actividad práctica: las métricas de resiliencia pueden invertir las clasificaciones

El siguiente laboratorio sin conexión calcula tres resúmenes de tres curvas de desempeño sintéticas y señala si cada una está censurada. Ejecútelo con Python 3; no se necesitan paquetes.

```python
# Lab 1 - resilience metrics on three synthetic performance curves (offline, standard library only)
# Q(t) = delivered fraction of normal service (1.0 = full), sampled hourly over a 48-hour window.
def curve(drop_at, depth, hold, recover_hours, window=48):
    q = []
    for t in range(window + 1):
        if t < drop_at:
            q.append(1.0)
        elif t < drop_at + hold:
            q.append(1.0 - depth)
        elif t < drop_at + hold + recover_hours:
            frac = (t - drop_at - hold) / recover_hours
            q.append(round(1.0 - depth * (1 - frac), 4))
        else:
            q.append(1.0)
    return q

def metrics(q):
    loss = sum((1.0 - a) + (1.0 - b) for a, b in zip(q, q[1:])) / 2  # trapezoid, hour units
    worst = 1.0 - min(q)
    down = [t for t, v in enumerate(q) if v < 1.0]
    if not down:
        return round(loss, 2), worst, 0, False
    recovered = q[-1] >= 1.0
    ttr = (max(down) + 1 - min(down)) if recovered else None
    return round(loss, 2), round(worst, 2), ttr, not recovered

scenarios = {
    "A_deep_short": curve(drop_at=2, depth=0.90, hold=3, recover_hours=4),
    "B_shallow_long": curve(drop_at=2, depth=0.25, hold=20, recover_hours=10),
    "C_unrecovered": curve(drop_at=30, depth=0.40, hold=30, recover_hours=6),
}
print("scenario        loss_h  worst  ttr_h  censored")
for name, q in scenarios.items():
    loss, worst, ttr, cens = metrics(q)
    print(f"{name:15} {loss:6.2f}  {worst:5.2f}  {str(ttr):5}  {cens}")
```

Salida esperada:

```text
scenario        loss_h  worst  ttr_h  censored
A_deep_short      4.95   0.90  7      False
B_shallow_long    6.38   0.25  30     False
C_unrecovered     7.40   0.40  None   True
```

Lea la salida con atención. Según el *peor desempeño*, A es mucho peor que B; según la *pérdida de área* y el *tiempo hasta la recuperación*, B es peor que A. El escenario C tiene la mayor pérdida de área dentro de la ventana, pero su pérdida queda truncada en la hora 48: la pérdida verdadera es mayor y su tiempo hasta la recuperación es desconocido. El laboratorio demuestra tres puntos de §1.6: las clasificaciones dependen de la métrica; la censura oculta los peores casos; y una única «puntuación de resiliencia» oculta un juicio de valor. Si A es una pérdida de presión de agua que obliga a emitir un aviso de hervir el agua y B es un período de presión reducida sin efecto sobre la salud, ni el área ni la duración captan la diferencia decisiva; un umbral sobre la profundidad, sí.

### 1.11 Errores habituales y límites

- Tratar una etiqueta sectorial como definición de población.
- Afirmar consecuencias a partir de observaciones cibernéticas sin la cadena física y organizativa.
- Usar un recuento de activos o una centralidad de red como medida de consecuencia.
- Reportar una única métrica de resiliencia sin justificarla ni probar una alternativa.
- Promediar tiempos de recuperación censurados.
- Solicitar datos operativos que la pregunta no necesita.
- Empezar la recogida de datos antes de que exista un acuerdo de publicación.
- Tratar lo «sintético» como motivo para omitir la prueba de sensibilidad: los datos sintéticos calibrados con un lugar real todavía pueden identificarlo.

El límite de este capítulo es que las salvaguardas de integridad reducen, pero no eliminan, el riesgo de resultados engañosos. Su propósito es que otros puedan *detectar* los errores.

### Ejercicios — capítulo 1

**EX001 — Auditoría con la escalera de afirmaciones.** *Objetivo:* separar observaciones de afirmaciones sobre consecuencias. *Entradas:* el enunciado sintético «Los registros muestran que el atacante accedió al sistema de gestión de la distribución de REC a las 01:52; la interrupción resultante dejó al hospital sin electricidad y puso en peligro a los pacientes; esto demuestra que las cooperativas rurales son el punto más débil de la red». *Restricciones:* use los cinco peldaños de §1.1.3. *Pasos:* (1) divida el enunciado en las aserciones que lo componen; (2) asigne a cada una un peldaño; (3) nombre el supuesto oculto detrás de cada una; (4) nombre una observación que refutaría cada una; (5) reescriba el enunciado para que afirme solo lo que la evidencia podría respaldar. *Evidencia esperada:* tabla y reescritura. *Rúbrica:* 3 = cada aserción ubicada correctamente en la escalera, la reserva del generador del hospital y la generalización señaladas, reescritura bien acotada; 2 = una aserción mal ubicada; 1 = la reescritura sigue afirmando de más; 0 = nada.

**EX002 — Definición y población.** *Objetivo:* ver cómo las definiciones legales cambian la población de un estudio. *Entradas:* el NSM-22 (a través de la página de CISA), la Directiva CER y NIS2, tal como se citan en §1.1.1. *Restricciones:* no parafrasee de memoria; cite el texto definitorio en que se apoya, con artículo o sección. *Pasos:* (1) para un hospital regional, una pequeña empresa de agua potable y un procesador de pagos, indique si cada uno está dentro del alcance de cada instrumento y en qué categoría; (2) nombre una consecuencia de las diferencias para un estudio comparativo entre jurisdicciones. *Evidencia esperada:* tabla de 3 × 3 con citas y un párrafo. *Rúbrica:* 3 = exacta, con citas precisas y una consecuencia de diseño sólida; 2 = un error de categoría; 1 = sin citas; 0 = nada.

**EX003 — Tipificación de interdependencias.** *Objetivo:* aplicar los tipos de Rinaldi et al. *Entradas:* las dependencias de Riverbend: TEL de F2; HOSP de F2 y de WATER; WATER de F3; el SCADA del agua de TEL; la facturación de la cooperativa eléctrica del procesador de pagos; las entregas de combustible para generadores del acceso por carretera. *Restricciones:* un tipo principal por relación, justificado. *Pasos:* clasifique cada una como física, cibernética, geográfica o lógica; identifique cualquier ciclo; indique qué dependencia omitiría un modelo puro de flujo de potencia. *Evidencia esperada:* tabla y un párrafo. *Rúbrica:* 3 = tipos justificados, se señala la ausencia de ciclo entre los servicios enumerados, combustible/carretera y facturación identificados como fuera de un modelo de flujo de potencia; 2 = una clasificación errónea; 1 = sin justificación; 0 = nada.

**EX004 — Análisis de Menlo.** *Objetivo:* identificar partes interesadas y salvaguardas. *Entradas:* la pregunta revisada del Estudio Cascada en §1.9, que incluye entrevistas con despachadores de REC y un ejercicio de mesa. *Restricciones:* use los cuatro principios; al menos seis partes interesadas. *Pasos:* enumere las partes interesadas; para cada principio, nombre el riesgo principal y una salvaguarda; nombre la autoridad de detención y los datos que se destruyen si el socio se retira. *Evidencia esperada:* tabla de partes interesadas y tabla de salvaguardas. *Rúbrica:* 3 = población atendida, riesgo disciplinario para el personal, sensibilidad de la información y presión del socio tratados con salvaguardas concretas; 2 = un principio poco desarrollado; 1 = genérico; 0 = nada.

**EX005 — Prueba de sensibilidad.** *Objetivo:* decidir qué puede publicarse. *Entradas:* cinco artefactos: (a) duraciones de restablecimiento agregadas por clase de alimentador; (b) una lista de hospitales con los días de combustible de sus generadores; (c) el código del modelo; (d) el marco de codificación de las entrevistas; (e) un mapa de qué alimentador abastece a la planta regional de tratamiento de agua. *Restricciones:* aplique §1.5.2; proponga un nivel: público, controlado, retenido. *Pasos:* (1) decida si cada artefacto identifica un activo, una ubicación, una vulnerabilidad o una dependencia específicos; (2) asigne un nivel; (3) justifique el nivel; (4) proponga una transformación que permita una divulgación más amplia. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (b) y (e) retenidos o transformados, (a) y (c) públicos, (d) público si no tiene citas textuales, con transformaciones; 2 = uno mal juzgado; 1 = todo público o todo retenido; 0 = nada.

**EX006 — Inversión de métricas.** *Objetivo:* usar el laboratorio 1. *Entradas:* el código del laboratorio. *Restricciones:* sin conexión. *Pasos:* (1) ejecute el laboratorio y registre la salida; (2) añada una cuarta métrica, «horas por debajo de 0,5», y repórtela para todos los escenarios; (3) cambie la ventana a 72 horas y reporte qué le ocurre a C; (4) escriba 150 palabras sobre qué métrica elegiría como primaria para un servicio de agua potable y por qué. *Evidencia esperada:* cambio en el código, salidas, párrafo. *Rúbrica:* 3 = valores correctos, C deja de estar censurado y con mayor pérdida, elección de la métrica justificada por un umbral sanitario; 2 = un valor erróneo; 1 = sin justificación; 0 = no ejecutado.

**EX007 — Esqueleto de protocolo.** *Objetivo:* redactar un protocolo auditable. *Entradas:* la pregunta revisada de §1.9. *Restricciones:* los doce elementos de §1.8; como máximo tres páginas. *Pasos:* (1) redacte en orden cada uno de los doce elementos del protocolo de §1.8; (2) marque cada elemento como fijo o abierto; (3) escriba dos condiciones de detención y dos condiciones de abandono; (4) enumere lo que un revisor hostil atacaría primero. *Evidencia esperada:* borrador del protocolo. *Rúbrica:* 3 = todos los elementos concretos, condiciones de detención y de abandono distintas, protección de la información específica; 2 = uno o dos elementos vagos; 1 = falta la seguridad o los acuerdos; 0 = nada.

### Síntesis del capítulo

La investigación sobre infraestructura estudia las consecuencias para las personas a través de cadenas de mecanismos físicos, cibernéticos y organizativos que el investigador rara vez observa directamente. Su evidencia proviene de incidentes raros y reportados de forma selectiva, de datos operativos protegidos, de bancos de pruebas pequeños, de modelos y de personas; cada fuente tiene sesgos característicos y debe triangularse. Las salvaguardas de integridad —preespecificación, registros de desviaciones, declaración— son necesarias porque los socios están regulados, los financiadores tienen intereses y las simulaciones son flexibles. Los riesgos de seguridad y de doble uso son reales: nunca pruebe en producción, simule primero, separe la capacidad de la consecuencia al publicar y nombre una autoridad de detención. La información sobre dependencias y reservas es sensible aunque sea aproximada. Las métricas de resiliencia incorporan juicios de valor; elíjalas según la decisión que se va a tomar y muestre si las conclusiones resisten las alternativas. El protocolo es el contrato que hace auditable todo esto.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 08

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Infraestructura crítica y seguridad sectorial: frontera de investigación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, el estudiante será capaz de:

1. Buscar, con un protocolo documentado y repetible, la literatura dispersa sobre seguridad y resiliencia de la infraestructura en ingeniería, investigación operativa, economía, políticas públicas y seguridad informática.
2. Explicar las principales familias de modelos de interdependencia, qué supone cada una y qué tipo de afirmación puede sustentar cada una.
3. Leer normas y regulaciones —NIST CSF 2.0, NIST SP 800-82, IEC 62443, NERC CIP, NIS2, CER y la orientación sectorial— como *objetos de investigación* cuya eficacia es en sí misma una pregunta abierta.
4. Evaluar la investigación sobre detección y bancos de pruebas a la luz de los errores de evaluación documentados en la literatura de seguridad y de series temporales.
5. Clasificar un vacío de evidencia (ausente, débil, contradictorio, no transferido) y convertir un tema en un enunciado de contribución falsable.

El capítulo 1 aportó la escalera de afirmaciones y las fuentes de evidencia; este capítulo las usa para leer el campo. El capítulo 3 convertirá el vacío elegido aquí en una propuesta de contribución.

### 2.1 Por qué cuesta encontrar la literatura

Un doctorando en seguridad de la infraestructura hereda al menos cinco literaturas que rara vez se citan entre sí:

| Comunidad | Preguntas típicas | Publicaciones y vocabulario típicos |
|---|---|---|
| Ingeniería de confiabilidad y de riesgo | Propagación de fallas, restablecimiento, métricas de riesgo, curvas de resiliencia | *Reliability Engineering & System Safety*, *Risk Analysis*; «inoperabilidad», «triángulo de resiliencia», «fragilidad». |
| Ingeniería eléctrica, hidráulica y de transporte | Física de redes, protección, secuenciación del restablecimiento | Revistas IEEE de potencia y redes inteligentes, revistas de recursos hídricos; «restablecimiento del servicio», «arranque en negro», «zona de presión». |
| Investigación operativa | Programación, diseño de redes, interdicción | Revistas de investigación operativa; «tiempo de finalización ponderado», «interdicción», «programa estocástico». |
| Seguridad informática y de OT | Ataques, detección, bancos de pruebas, protocolos | Conferencias de seguridad y talleres de seguridad de sistemas ciberfísicos; «detección de anomalías», «banco de pruebas», «modelo de amenazas». |
| Políticas públicas, derecho y gestión | Regulación, colaboración, incentivos, notificación | Revistas de políticas públicas e informes gubernamentales; «gestión de riesgos sectoriales», «colaboración público-privada», «entidad crítica». |

Publicaciones especializadas como el *International Journal of Critical Infrastructure Protection* y la serie de conferencias CRITIS tienden puentes entre algunas de ellas, pero una búsqueda limitada a publicaciones de seguridad pasará por alto la mayor parte del trabajo sobre restablecimiento e interdependencias, y una limitada a la ingeniería pasará por alto el trabajo informado por las amenazas. El marco de Rinaldi, Peerenboom y Kelly ([2001](https://doi.org/10.1109/37.969131)) es el ancestro común más habitual y una buena semilla para el encadenamiento de citas en ambas direcciones.

### 2.2 Delimitación sistemática entre disciplinas

#### 2.2.1 Elegir el tipo de revisión

Una **revisión sistemática** responde a una pregunta acotada con una búsqueda exhaustiva y una evaluación formal; una **revisión de alcance** (*scoping review*) cartografía la extensión y la naturaleza de un cuerpo de trabajo; una **revisión narrativa** es una síntesis experta sin búsqueda reproducible. Para un capítulo doctoral de frontera, lo adecuado suele ser una revisión de alcance con protocolo documentado: es reproducible, muestra la forma del campo e identifica dónde una revisión sistemática sería prematura. Repórtela con los ítems pertinentes de [PRISMA 2020](https://doi.org/10.1136/bmj.n71) —fuentes de búsqueda, fechas, cadenas, cribado, motivos de exclusión y diagrama de flujo— aunque la lista de verificación completa no se aplique.

#### 2.2.2 Un protocolo de búsqueda para el Estudio Cascada

1. **Pregunta.** ¿Qué se sabe sobre el efecto del orden de restablecimiento, informado por las dependencias entre sectores, en las consecuencias de las interrupciones de la infraestructura, incluidas las provocadas por ciberataques?
2. **Bloques conceptuales.** (restoration OR recovery OR "service restoration" OR prioritization) AND (interdependen* OR dependen* OR cascad*) AND (infrastructure OR utility OR "distribution system" OR "lifeline").
3. **Fuentes.** Al menos un índice de ingeniería, un índice académico general y una fuente de políticas (informes gubernamentales, informes posteriores a la acción), más encadenamiento de citas hacia atrás y hacia adelante a partir de dos artículos semilla.
4. **Elegibilidad.** Estudios que comparen al menos dos órdenes de restablecimiento o que cuantifiquen la consecuencia causada por dependencias; se excluyen las clasificaciones de vulnerabilidad puramente topológicas que no modelan el servicio.
5. **Cribado.** Dos revisores sobre una muestra de títulos y resúmenes, con el acuerdo medido antes de repartir el trabajo; los desacuerdos se resuelven por discusión y se registran.
6. **Marco de codificación.** Familia de modelo; tipo de validación (ninguna, aparente, histórica, de campo); fuente de datos; si los autores también construyeron el banco de pruebas o el modelo que evalúan; métrica de resultado; tipo de amenaza (natural, accidental, ciber); línea de base de comparación.
7. **Regla de parada.** Detener el encadenamiento cuando dos rondas consecutivas no añadan ningún estudio elegible.

#### 2.2.3 Evaluación de modelos y simulaciones

Las herramientas de evaluación clínica encajan mal. Para los artículos basados en modelos, evalúe: ¿la estructura del modelo está justificada por el mecanismo que representa? ¿Tienen fuente los parámetros? ¿Se verificó la implementación (hace el código lo que dice el artículo)? ¿Se validó el modelo, y frente a qué —validez aparente, eventos históricos, datos de campo ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20))? ¿Hay análisis de sensibilidad? ¿Es fuerte la línea de base de comparación? ¿Están disponibles el código y los datos de entrada? Un artículo de modelado que no puede responder a las preguntas de verificación y validación sustenta, como mucho, una afirmación sobre el modelo, no sobre la infraestructura.

### 2.3 El panorama de políticas y normas como objeto de investigación

Las normas y regulaciones no son solo contexto; saber si funcionan es una de las mayores preguntas abiertas del campo. El panorama actual (verifique las versiones antes de citarlas):

- **NIST Cybersecurity Framework 2.0** ([CSWP 29, febrero de 2024](https://doi.org/10.6028/NIST.CSWP.29)) añadió una función *Govern* (Gobernar) a Identify, Protect, Detect, Respond y Recover. Se basa en resultados y es voluntario en la mayoría de los sectores; pregunta de investigación: ¿sufren menos interrupciones, o interrupciones de menor consecuencia, las organizaciones que lo adoptan, y cómo se sabría?
- **NIST SP 800-82 Rev. 3** ([septiembre de 2023](https://doi.org/10.6028/NIST.SP.800-82r3)) amplió el alcance de los sistemas de control industrial a la tecnología operativa y añadió una superposición de OT para los controles de SP 800-53 Rev. 5. En septiembre de 2026 se publicó un borrador público inicial de la Rev. 4 ([CSRC](https://csrc.nist.gov/pubs/sp/800/82/r3/final)).
- **ISA/IEC 62443** es una serie de normas para la seguridad de los sistemas de automatización y control industrial. La parte 3-2 define el sistema bajo consideración, lo divide en **zonas** y **conductos**, evalúa el riesgo y asigna un **nivel de seguridad objetivo (SL-T)**; la parte 3-3 establece los requisitos del sistema bajo siete requisitos fundamentales —control de identificación y autenticación, control de uso, integridad del sistema, confidencialidad de los datos, flujo de datos restringido, respuesta oportuna a los eventos y disponibilidad de los recursos ([página de catálogo de IEC 62443-3-2](https://webstore.iec.ch/en/publication/30727)). Pregunta de investigación: ¿predice un SL-T asignado la resistencia ante adversarios realistas, y cómo se pueden medir los niveles de seguridad alcanzados en lugar de afirmarlos?
- Las normas de confiabilidad **NERC CIP** son obligatorias para el sistema eléctrico de gran escala de América del Norte. En junio de 2025, la FERC aprobó la [CIP-015-1 sobre monitoreo de la seguridad de la red interna](https://www.federalregister.gov/documents/2025/07/02/2025-12309/critical-infrastructure-protection-reliability-standard-cip-015-1-cyber-security-internal-network) (Order No. 907), con una implementación escalonada a lo largo de varios años ([página de la norma en NERC](https://www.nerc.com/standards/reliability-standards/cip/cip-015-1)). Una norma obligatoria con despliegue escalonado es un experimento natural, si los investigadores logran obtener datos de resultados, lo que rara vez ocurre.
- **NIS2 y CER de la UE** (ambas de 2022) imponen obligaciones de gestión de riesgos y de notificación a las entidades esenciales e importantes, y obligaciones de resiliencia a las entidades críticas; la transposición nacional varía, lo que crea una variación entre países de interés para la investigación.
- **Finanzas.** La [Guidance on cyber resilience for financial market infrastructures](https://www.bis.org/cpmi/publ/d146.htm) del CPMI–IOSCO (junio de 2016) complementa los Principles for Financial Market Infrastructures; es el origen de la expectativa, muy debatida, de que las operaciones críticas se diseñen para reanudarse rápidamente tras una interrupción, lo que crea una tensión entre la rapidez de la reanudación y la integridad de los datos, un problema de investigación sin respuesta establecida.
- La **ingeniería ciberinformada orientada a consecuencias (CCE)**, desarrollada en el Idaho National Laboratory, avanza en cuatro fases —priorización de consecuencias, análisis de sistema de sistemas, selección de objetivos basada en consecuencias, y mitigaciones y protecciones ([página de CCE del INL](https://inl.gov/national-security/cce/); [Bochman y Freeman, 2021](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710)). Parte de las consecuencias y no de las vulnerabilidades, lo que concuerda con el énfasis de este libro; si produce mejores decisiones de mitigación que los métodos guiados por vulnerabilidades no se ha probado, hasta donde sabe el autor, con diseños comparativos.

El vacío de investigación común a todo el panorama es la **evidencia de resultados**: los marcos se justifican por consenso experto y por las lecciones de incidentes, pero los estudios comparativos que vinculan su adopción con las consecuencias son escasos, porque los datos de resultados son escasos, están protegidos y se confunden con la madurez de la organización.

### 2.4 Familias de modelos de interdependencia

[Ouyang (2014)](https://doi.org/10.1016/j.ress.2013.06.040) revisó el modelado y la simulación de sistemas de infraestructura interdependientes y agrupó los enfoques en empíricos, basados en agentes, basados en dinámica de sistemas, basados en teoría económica, basados en redes y otros. Cada familia sustenta un tipo distinto de afirmación.

| Familia | Idea central | Sustenta afirmaciones sobre | Límites principales |
|---|---|---|---|
| Empírica | Analizar registros de interrupciones pasadas y de su propagación | Lo que ha ocurrido; frecuencia de los tipos de dependencia en los informes | Sesgo de notificación; pocos eventos; sin contrafácticos |
| Basada en agentes | Simular decisores y activos autónomos | Comportamiento emergente, decisiones de los operadores | Muchos parámetros; validación difícil |
| Dinámica de sistemas | Existencias, flujos y bucles de retroalimentación en el tiempo | Dinámica agregada, retroalimentación de políticas | Gruesa; estructura supuesta |
| Económica (insumo-producto) | Propagación al estilo de Leontief de la inoperabilidad o de la pérdida de producción entre sectores ([Haimes y Jiang, 2001](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1))) | Pérdida económica y clasificación a nivel sectorial | Lineal, estática o cuasiestática; la agregación sectorial oculta las instalaciones |
| Red — topología | Grafos y percolación | Fragilidad estructural; regímenes cualitativos de cascada | Sin flujos, reservas ni operadores |
| Red — flujo | Flujos físicos (flujo de potencia, hidráulica) sobre redes | Consecuencias de ingeniería dentro de un sector | Exige muchos datos; acoplamiento entre sectores difícil |
| Cosimulación | Acoplar simuladores de dominio (electricidad, agua, comunicaciones) | Tiempos entre sectores con fidelidad física | Error de integración; sincronización; pesada |

**Cascadas topológicas.** [Buldyrev et al. (2010)](https://doi.org/10.1038/nature08932) mostraron, en un modelo de percolación de dos redes interdependientes, que el acoplamiento puede producir un colapso abrupto y catastrófico y que, a diferencia de lo que ocurre en redes aisladas, distribuciones de grado más amplias pueden aumentar la vulnerabilidad ante fallas aleatorias. El resultado es un hito de comprensión estructural. También es una fuente frecuente de afirmaciones exageradas: el modelo supone una dependencia de todo o nada, sin reservas, sin restablecimiento y con patrones de acoplamiento específicos. Citarlo como prueba de que la electricidad y las comunicaciones de una ciudad concreta colapsarán abruptamente es un error de categoría: una comprensión estructural L5 presentada como una afirmación de consecuencia L4.

**Inoperabilidad insumo-producto.** El modelo insumo-producto de inoperabilidad (IIM) escribe el vector de inoperabilidad de equilibrio *q* como *q* = *A\*q* + *c\**, de modo que *q* = (*I* − *A\**)⁻¹ *c\**, donde *A\** contiene los coeficientes de interdependencia y *c\** una perturbación inicial. El capítulo 4 replica un cálculo IIM y muestra cómo un error en la convención de la matriz cambia los resultados sin dar aviso.

**Dónde están las reservas.** Un tema común a las familias es que el momento de la consecuencia lo gobiernan las **reservas** —combustible de generadores, autonomía de baterías, almacenamiento, inventario, procedimientos manuales— que la topología ignora y que los modelos de flujo suelen mantener constantes. La investigación sobre restablecimiento en ingeniería eléctrica sí modela la secuenciación, pero a menudo dentro de un solo sector y con el objetivo de clientes o carga restablecidos. El Estudio Cascada se sitúa en esta junta: el tiempo de las reservas entre sectores como motor del *orden de restablecimiento*.

### 2.5 Investigación sobre detección y bancos de pruebas: la evaluación como frontera

Gran parte de la literatura del lado de la seguridad estudia la detección de ataques en procesos industriales. Sus problemas están cada vez mejor documentados:

- **Evaluación de mundo cerrado.** [Sommer y Paxson (2010)](https://doi.org/10.1109/SP.2010.25) argumentaron que la detección de intrusiones con aprendizaje automático encaja mal con el mundo abierto y cambiante de las redes reales, y que las evaluaciones a menudo no captan el costo de los errores ni la brecha semántica entre una anomalía y un ataque.
- **Errores en la investigación de seguridad con aprendizaje automático.** [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) identificaron diez errores —entre ellos sesgo de muestreo, fisgoneo de datos, correlaciones espurias, líneas de base y métricas inadecuadas, la falacia de la tasa base, la evaluación solo en laboratorio y modelos de amenaza inadecuados— y encontraron varios en cada uno de los 30 artículos de publicaciones de primer nivel que revisaron.
- **Métricas de series temporales infladas.** [Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) mostraron que el protocolo de *ajuste por punto* (*point adjustment*), habitual en la detección de anomalías en series temporales, que marca como detectado todo un segmento anómalo si se señala cualquier punto de él, puede hacer que incluso puntuaciones aleatorias parezcan el estado del arte; propusieron PA%K. El capítulo 4 reproduce el efecto.
- **Bancos de pruebas pequeños, antiguos y construidos por los autores.** Los conjuntos de datos públicos de bancos de pruebas como SWaT ([Goh et al., 2016](https://doi.org/10.1007/978-3-319-71368-7_8)) y la competencia de distribución de agua BATADAL ([Taormina et al., 2018](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969)) permitieron la comparación, lo que es una contribución importante. También concentran el campo en unos pocos sistemas con conjuntos de ataques específicos; los resultados se transfieren a otras plantas solo mediante argumentos.

Para una tesis sobre IC, la detección es relevante sobre todo como **reserva frente a la consecuencia**: una detección que llega después de que se agotó la reserva de un servicio no cambia nada para las personas atendidas. Plantear la detección por el tiempo hasta la consecuencia y no por el F1 es un puente poco explorado entre las dos literaturas.

### 2.6 Evidencia sectorial y sobre amenazas

- **Energía.** El ataque de 2015 a la distribución en Ucrania, documentado por [E-ISAC y SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and), es el caso público más citado de un ciberataque que causó cortes a los clientes; también es un solo caso, con el restablecimiento logrado mediante operación manual.
- **Agua.** Los sistemas de agua son numerosos, a menudo pequeños y con pocos recursos, lo que dificulta reunir evidencia de todo el sector; gran parte del trabajo cuantitativo usa redes de distribución simuladas como la de BATADAL.
- **Salud.** [Neprash et al. (2022)](https://doi.org/10.1001/jamahealthforum.2022.4873) documentaron un número creciente de ataques de *ransomware* contra organizaciones prestadoras de atención de salud de EE. UU. entre 2016 y 2021 y sus efectos en las operaciones; este tipo de trabajo vincula un evento cibernético con la prestación de atención —el peldaño de la consecuencia— usando datos públicos y regulatorios.
- **Cambio del modelo de amenazas.** El aviso conjunto [AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a) de CISA (febrero de 2024) evaluó que un actor patrocinado por un Estado, conocido como Volt Typhoon, se había preposicionado en redes de TI de organizaciones de comunicaciones, energía, transporte y agua para posibilitar una eventual interrupción, usando cuentas válidas y técnicas que aprovechan herramientas legítimas del sistema (*living off the land*). Para la investigación, el preposicionamiento significa que el escenario pertinente es una interrupción *simultánea, multisectorial y sincronizada por el adversario*, justo donde las reglas de restablecimiento de un solo sector pueden fallar.
- **Precedente ciberfísico.** El [análisis de Stuxnet de Langner de 2013](https://archive.org/details/to-kill-a-centrifuge) es un relato clásico de un ataque ciberfísico diseñado a partir del conocimiento del proceso. Su lección para la investigación en IC es que los ataques con consecuencias se diseñan contra procesos físicos y sus márgenes de seguridad, razón por la cual existen métodos que parten de la consecuencia, como CCE.

### 2.7 Clasificar el vacío

El libro doctoral de IR distingue cuatro tipos de vacío de evidencia; aquí se aplican sin cambios:

| Tipo de vacío | Significado | Ejemplo en infraestructura | Siguiente estudio adecuado |
|---|---|---|---|
| Ausente | Ningún estudio aborda la pregunta | No hay prueba comparativa de CCE frente a la priorización guiada por vulnerabilidades | Primer diseño comparativo, aunque sea pequeño |
| Débil | Hay estudios, pero no pueden sustentar la afirmación | Beneficios del orden de restablecimiento mostrados solo en modelos no validados construidos por quienes los proponen | Validación independiente; líneas de base más fuertes |
| Contradictorio | Estudios creíbles discrepan | Los modelos topológicos y de flujo clasifican los mismos activos de forma distinta | Estudio que discrimine entre mecanismos |
| No transferido | Existe evidencia en otro dominio | La evidencia sobre planificación de sobrecarga hospitalaria no se ha aplicado al orden de restablecimiento | Prueba de transferencia con condiciones de contorno explícitas |

### 2.8 Ejemplo resuelto: evaluación de la literatura sobre orden de restablecimiento (sintético)

La revisión de alcance del Estudio Cascada (sintética) encontró ocho artículos elegibles, P1–P8:

| ID | Familia | Validación | ¿Independiente del modelo o banco de pruebas de los propios autores? | Afirmación sustentada |
|---|---|---|---|---|
| P1 | Topología de red | Ninguna | No | C1 la centralidad identifica los activos de mayor consecuencia |
| P2 | Topología de red | Aparente (revisión experta) | No | C1 |
| P3 | Insumo-producto | Histórica (interrupción regional) | Sí | C2 el IIM clasifica los sectores por pérdida económica |
| P4 | Basado en agentes | Aparente | No | C3 el restablecimiento consciente de las dependencias reduce la pérdida crítica |
| P5 | Cosimulación | Histórica | No | C3 |
| P6 | Insumo-producto | Histórica | Sí | C2 |
| P7 | Cosimulación | De campo (ejercicio de la empresa de servicios) | Sí | C3 |
| P8 | Empírico | De campo (registros posteriores a la acción) | Sí | C4 la duración de la energía de respaldo domina el tiempo de la cascada |

Evaluación: C1 solo tiene evidencia topológica autovalidada; es *débil*. C2 tiene dos validaciones históricas independientes, la afirmación más fuerte del conjunto, aunque sobre pérdida económica y no sobre el servicio. C3 tiene tres estudios, pero solo uno independiente y con validación fuerte; P4 y P5 se evaluaron en los modelos de sus propios autores, lo que invita a la circularidad modelo-política (capítulo 6). C4 descansa en un solo estudio empírico. Por tanto, la frontera es C3: plausible, *propuesta* repetidamente, *probada* débilmente.

### 2.9 Actividad práctica: codificar el mapa de la literatura

```python
# Lab 2 - coding a synthetic literature map for interdependency-modelling claims (offline)
# Fields: id, model family, validation, independent of authors' own testbed?, claim supported
studies = [
    ("P1", "network-topology", "none",       False, "C1"),
    ("P2", "network-topology", "face",       False, "C1"),
    ("P3", "input-output",     "historical", True,  "C2"),
    ("P4", "agent-based",      "face",       False, "C3"),
    ("P5", "co-simulation",    "historical", False, "C3"),
    ("P6", "input-output",     "historical", True,  "C2"),
    ("P7", "co-simulation",    "field",      True,  "C3"),
    ("P8", "empirical",        "field",      True,  "C4"),
]
claims = {
    "C1": "Topological centrality identifies the assets whose loss causes the largest service cascade",
    "C2": "Input-output inoperability ranks sectors by economic loss after a regional outage",
    "C3": "Dependency-aware restoration lowers critical-service loss compared with siloed restoration",
    "C4": "Backup-power duration is the dominant buffer controlling cascade timing",
}
STRONG = {"historical", "field"}
for cid, text in claims.items():
    rows = [s for s in studies if s[4] == cid]
    strong_indep = [s[0] for s in rows if s[2] in STRONG and s[3]]
    if len(strong_indep) >= 2:
        state = "supported (>=2 independent strong validations)"
    elif strong_indep:
        state = "single-source; needs replication"
    else:
        state = "open: no independent strong validation"
    print(f"{cid}: {state}; evidence={[s[0] for s in rows]}; strong+independent={strong_indep}")
```

Salida esperada:

```text
C1: open: no independent strong validation; evidence=['P1', 'P2']; strong+independent=[]
C2: supported (>=2 independent strong validations); evidence=['P3', 'P6']; strong+independent=['P3', 'P6']
C3: single-source; needs replication; evidence=['P4', 'P5', 'P7']; strong+independent=['P7']
C4: single-source; needs replication; evidence=['P8']; strong+independent=['P8']
```

Registre la salida exacta en su bitácora de reproducción, no una paráfrasis.

La regla codificada en `STRONG` y en el indicador de independencia es una *elección*. Cambiarla cambia qué afirmaciones quedan «sustentadas». Un mapa de la literatura debe publicar su regla de codificación para que los lectores puedan discrepar de ella explícitamente.

Antes de confiar en el mapa conviene hacer dos comprobaciones. Primero, ejecútelo sin el indicador de independencia: C3 cuenta entonces P5 como validación fuerte y se reporta como sustentada, lo que muestra cuánto del veredicto depende de esa única decisión de codificación. Segundo, pida a un segundo codificador que clasifique la validación y la independencia de los ocho artículos sin ver la hoja del primero, y registre dónde discrepan. Un desacuerdo sobre si un ejercicio de la empresa de servicios cuenta como validación de campo, como en P7, es un hallazgo sobre el marco de codificación, y el marco debe ajustarse antes de usar el mapa para elegir un vacío.

### 2.10 Del mapa a la frontera: la prueba de contribución

Un vacío se convierte en contribución doctoral cuando supera cuatro pruebas: **Abierto** — la búsqueda documentada muestra que aún no tiene respuesta; **Importante** — una respuesta cambiaría una decisión que alguien toma realmente (aquí, el orden de restablecimiento en operaciones de emergencia); **Factible** — los datos, los modelos, los socios y la ética lo permiten dentro del programa; **Falsable** — una observación enunciada mostraría que la afirmación es falsa. Formato de redacción: *«En [población/contexto], [intervención], comparada con [la línea de base más fuerte], cambiará [métrica principal] en al menos [efecto mínimo de interés] sin empeorar [métrica de seguridad] más allá de [margen]; esto quedará refutado si [observación]»*.

El enunciado del Estudio Cascada (que se refinará en el capítulo 3): *En interrupciones de distribución que requieren el restablecimiento manual secuencial de alimentadores, ordenar por el tiempo hasta el impacto de los servicios críticos, en comparación con ordenar por clientes restablecidos, reduce la pérdida ponderada de servicios críticos, declarada de antemano, en al menos un 20 %, mientras aumenta las horas-cliente perdidas en no más de un 15 %; esto queda refutado si la reducción es inferior al 20 % en un modelo construido de forma independiente para una segunda región, o si los operadores, en un ejercicio de mesa a ciegas, no eligen ese orden cuando se les da la misma información.*

### 2.11 Errores habituales y límites

- Buscar solo en publicaciones de seguridad y declarar un vacío que la ingeniería ya ha llenado.
- Citar resultados de percolación como predicciones de consecuencias para lugares concretos.
- Tratar las normas como evidencia de eficacia y no como hipótesis sobre ella.
- Comparar artículos de detección por el F1 de titular sin revisar el protocolo de evaluación.
- Contar estudios en lugar de evaluar su independencia y su validación.
- Redactar un vacío como un tema («interdependencias en ciudades inteligentes») en lugar de como un enunciado falsable.

- Tratar una publicación especializada, como la serie CRITIS, como si cubriera todo el campo, cuando la mayor parte del trabajo sobre restablecimiento aparece en publicaciones de ingeniería y de investigación operativa.
- Leer la adopción generalizada de un marco como evidencia de resultados; la adopción muestra que la gente lo eligió, no que las consecuencias disminuyeron.
- Codificar un artículo como independiente porque sus autores son distintos de quienes proponen, sin comprobar si reutiliza el modelo o el banco de pruebas de estos.
- Detener el encadenamiento de citas antes de tiempo porque las primeras rondas confirmaron el vacío esperado.

### Ejercicios — capítulo 2

**EX008 — Protocolo de búsqueda.** *Objetivo:* redactar una búsqueda interdisciplinaria reproducible. *Entradas:* una pregunta de su elección sobre seguridad o resiliencia de la infraestructura. *Restricciones:* al menos tres tipos de fuente (índice de ingeniería, índice general, fuente de políticas); encadenamiento de citas. *Pasos:* (1) enuncie la pregunta; (2) construya los bloques conceptuales y las cadenas; (3) defina la elegibilidad y los motivos de exclusión; (4) defina el cribado, el acuerdo y la regla de parada. *Evidencia esperada:* protocolo (≤ 2 páginas). *Rúbrica:* 3 = repetible, interdisciplinario, acuerdo medido, regla de parada explícita; 2 = un elemento vago; 1 = solo una lista de palabras clave; 0 = nada.

**EX009 — Evaluación de un artículo de modelado.** *Objetivo:* evaluar un artículo de simulación según la afirmación que puede sustentar. *Entradas:* estudio sintético P5 (cosimulación, validación histórica, modelo de los propios autores). *Restricciones:* use el §2.2.3. *Pasos:* enumere lo que comprobaría sobre estructura, parámetros, verificación, validación, sensibilidad, línea de base y disponibilidad; enuncie la afirmación más fuerte que P5 puede sustentar y su peldaño. *Evidencia esperada:* formulario de evaluación y afirmación de una oración. *Rúbrica:* 3 = identifica como decisivos el modelo construido por los autores, la verificación desconocida, el único evento histórico y la fuerza de la línea de base, y limita la afirmación al modelo; 2 = se omite un problema; 1 = acepta la afirmación como L5; 0 = nada.

**EX010 — Ajuste de la familia de modelos.** *Objetivo:* emparejar preguntas con familias de modelado. *Entradas:* cuatro preguntas: (a) ¿Qué sectores pierden más producción tras una semana de pérdida regional de electricidad? (b) ¿Cuánto tarda un hospital en perder la presión de agua tras la interrupción de un alimentador? (c) ¿Comparten los operadores combustible de manera informal entre empresas de servicios durante interrupciones largas? (d) ¿Es propenso a un colapso abrupto un sistema de dos redes con acoplamiento aleatorio? *Restricciones:* una familia principal por pregunta, con una razón y un límite. *Pasos:* (1) reformule qué le pide predecir o explicar cada pregunta; (2) elija la familia de modelado principal del §2.4; (3) justifique la elección por la afirmación que sustenta; (4) nombre el límite más importante de la familia para esa pregunta. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (a) insumo-producto, (b) flujo/cosimulación o modelo de reservas, (c) empírico/cualitativo o basado en agentes informado por entrevistas, (d) topología/percolación, cada uno con límites sólidos; 2 = un desajuste; 1 = dos o más; 0 = nada.

**EX011 — La norma como hipótesis.** *Objetivo:* convertir una norma en una afirmación comprobable. *Entradas:* zonas, conductos y SL-T de IEC 62443-3-2 (§2.3). *Restricciones:* una hipótesis comprobable; nombre la medida de resultado y un diseño factible. *Pasos:* enuncie la afirmación causal implícita de la norma; redacte una hipótesis; proponga un diseño (por ejemplo, ejercicios de *red team* sobre zonas de un banco de pruebas con distintos SL-T); nombre dos factores de confusión. *Evidencia esperada:* una página. *Rúbrica:* 3 = hipótesis observable, diseño seguro y factible, factores de confusión reales (habilidad del evaluador, antigüedad de los activos); 2 = diseño vago; 1 = repite la norma; 0 = nada.

**EX012 — Reparar el mapa de la literatura.** *Objetivo:* hacer que una regla de codificación coincida con un criterio enunciado. *Entradas:* Laboratorio 2. *Restricciones:* sin conexión; conservar todas las filas. *Pasos:* (1) añada un campo `hazard` (P5 y P7 "cyber", todos los demás "all-hazards"); (2) cambie la regla para que una afirmación sobre interrupciones *provocadas por ciberataques* solo quede sustentada por validaciones fuertes e independientes con hazard "cyber"; (3) ejecute y registre la salida exacta para C3; (4) explique en 100 palabras qué cambió y por qué importa. *Evidencia esperada:* código modificado, salida exacta, explicación. *Rúbrica:* 3 = código correcto; C3 sigue con una sola fuente (solo P7), y el estudiante observa que C1, C2 y C4 ya no tienen sustento fuerte e independiente para interrupciones *provocadas por ciberataques*, con una explicación clara de la transferencia entre amenazas; 2 = salida correcta, explicación pobre; 1 = regla equivocada; 0 = no se ejecutó.

**EX013 — Clasificar el vacío.** *Objetivo:* distinguir los tipos de vacío. *Entradas:* cuatro enunciados sintéticos: (a) «Dos estudios con modelos de flujo discrepan sobre si el almacenamiento de agua o el combustible del generador domina el tiempo de interrupción del hospital»; (b) «Existe investigación sobre la capacidad de sobrecarga hospitalaria, pero ningún estudio la vincula con el orden de restablecimiento»; (c) «Tres documentos técnicos de proveedores afirman que su plataforma reduce a la mitad el tiempo de restablecimiento»; (d) «Ningún estudio de nuestra búsqueda documentada compara CCE con la priorización guiada por vulnerabilidades». *Restricciones:* un tipo para cada uno, justificado; proponga el siguiente estudio. *Pasos:* (1) reformule cada uno como pregunta; (2) enumere la evidencia correspondiente; (3) asigne un tipo de vacío; (4) nombre el estudio que lo cerraría. *Evidencia esperada:* cuatro párrafos. *Rúbrica:* 3 = contradictorio, no transferido, débil, ausente, con siguientes pasos sólidos; 2 = un error; 1 = dos errores; 0 = nada.

**EX014 — Enunciado falsable y memorando de frontera.** *Objetivo:* convertir un tema en una contribución. *Entradas:* el tema «resiliencia de los sistemas de pago durante interrupciones eléctricas regionales». *Restricciones:* use el formato de redacción del §2.10; la observación refutadora debe ser factible; 400–600 palabras; cite solo fuentes que haya leído. *Pasos:* (1) redacte el enunciado; (2) aplique las cuatro pruebas; (3) revíselo una vez; (4) explique qué pregunta adyacente debe responderse primero y por qué. *Evidencia esperada:* enunciado, notas de las pruebas, revisión, memorando. *Rúbrica:* 3 = supera todas las pruebas con un refutador factible y un orden de preguntas justificado; 2 = una prueba débil; 1 = sigue siendo un tema; 0 = nada.

### Síntesis del capítulo

La frontera de la seguridad de la infraestructura está repartida en cinco literaturas con vocabularios distintos; una búsqueda doctoral debe cruzarlas deliberadamente y documentar cómo lo hace. Las normas y regulaciones son hipótesis sobre lo que reduce la consecuencia, y la evidencia de resultados sobre ellas es escasa. Los modelos de interdependencia se agrupan en familias que sustentan afirmaciones distintas; los resultados topológicos dan comprensión estructural, los modelos insumo-producto dan economía a nivel sectorial y los modelos de flujo o de cosimulación dan tiempos de ingeniería, y ninguno sustituye a la validación. La investigación sobre detección está mejorando su práctica de evaluación; para la IC, la detección importa como reserva medida frente al tiempo hasta la consecuencia. Evalúe la independencia y la validación, no los recuentos. El vacío del Estudio Cascada —el orden de restablecimiento consciente de las dependencias se propone a menudo y se prueba débilmente— está abierto, es importante, es factible y puede hacerse falsable.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 08

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Propuesta de contribución original

### Resultados de aprendizaje y conexión

Al terminar este capítulo, el estudiante será capaz de:

1. Tipificar una contribución doctoral (artefacto, método, medición, hallazgo empírico, teoría) y enunciar la evidencia que exige cada tipo.
2. Especificar un mecanismo como una cadena de eslabones que predice un *patrón* de resultados, incluido dónde la intervención no debería ayudar.
3. Representar las dependencias entre sectores como un grafo con reservas, calcular el tiempo hasta el impacto y explicar qué deja fuera la representación.
4. Relacionar el orden de restablecimiento con la teoría clásica de la programación de tareas y usar esa relación para elegir líneas de base y predecir compensaciones.
5. Redactar hipótesis principales, de mecanismo, de contribución sobre la mejor práctica y de no inferioridad con un efecto mínimo de interés justificado.
6. Construir una tabla de explicaciones rivales y un conjunto de condiciones de fracaso declaradas de antemano que acotarían o harían abandonar la afirmación.

El capítulo 2 identificó el vacío: el orden de restablecimiento consciente de las dependencias se propone a menudo y se prueba débilmente. Este capítulo lo convierte en una propuesta que podría ser errónea. El capítulo 4 replicará las líneas de base y pondrá a prueba el procedimiento en un piloto.

### 3.1 ¿Qué tipo de contribución?

| Tipo | Ejemplo en seguridad de IC | Evidencia mínima |
|---|---|---|
| Artefacto | Una cosimulación abierta de distribución eléctrica, agua y telecomunicaciones | Pruebas de verificación; documentación; evidencia de uso por terceros |
| Método | Un procedimiento para calcular prioridades de restablecimiento a partir de datos de dependencias | Comparación con la práctica actual más fuerte en métricas enunciadas, en más de un contexto |
| Medición | Un instrumento validado para la duración de las reservas o la exactitud del mapa de dependencias | Evidencia de confiabilidad y validez |
| Hallazgo empírico | «Los operadores ya priorizan las instalaciones críticas, pero no usan el tiempo de las reservas» | Un estudio muestreado y documentado de operadores |
| Teoría | Un mecanismo que explica cuándo ayuda el orden consciente de las dependencias | Predicciones que lo distinguen de los rivales, puestas a prueba |

La contribución que busca el Estudio Cascada es un **método con un mecanismo**: una regla para ordenar el restablecimiento (el artefacto es accesorio) y una explicación de *cuándo* supera a la práctica actual. Decirlo pronto importa, porque «construimos un simulador y nuestro método ganó» es una demostración de artefacto, no una contribución de método.

### 3.2 El orden de restablecimiento como problema de programación

Cuando una sola cuadrilla de restablecimiento debe restablecer los alimentadores de uno en uno, el orden de restablecimiento es un **problema de programación en una sola máquina**: cada alimentador *j* es una tarea con tiempo de procesamiento *p_j* (maniobras manuales, inspección, reenergización) y el objetivo depende de lo que se minimice.

- Si el objetivo son las **horas-cliente perdidas**, cada alimentador aporta (clientes en *j*) × (tiempo de finalización *C_j*). Minimizar Σ *w_j C_j* en una máquina se resuelve de forma exacta ordenando las tareas por *w_j / p_j* de mayor a menor —la **regla de Smith** ([Smith, 1956](https://doi.org/10.1002/nav.3800030106)). Con tiempos de restablecimiento esperados iguales, esto equivale simplemente a «más clientes primero». El orden convencional que este libro usa como línea de base no es, por tanto, ingenuo: es *óptimo para las horas-cliente* en este escenario idealizado.
- Si el objetivo es la **pérdida de servicios críticos**, un servicio *s* alimentado por el alimentador *j* solo se pierde desde el momento en que se agota su reserva *b_s* hasta que se restablece el alimentador: loss_s = *w_s* × max(0, *C_j* + lag − *b_s*). La reserva actúa como una fecha de vencimiento, y el objetivo se parece al **retraso ponderado** (*weighted tardiness*). El retraso ponderado total en una sola máquina es NP-difícil en sentido fuerte ([Lenstra, Rinnooy Kan y Brucker, 1977](https://doi.org/10.1016/S0167-5060(08)70743-X)), de modo que las reglas prácticas son heurísticas. Ordenar por la fecha de vencimiento más temprana —aquí, el tiempo hasta el impacto más temprano— es una heurística clásica que ignora los pesos.

Esta relación le da al estudio tres cosas que un planteamiento puramente de seguridad pasaría por alto. Primero, una **predicción teórica de la compensación**: cualquier orden que se aparte de la regla de Smith debe aumentar las horas-cliente esperadas, de modo que un margen de no inferioridad sobre las horas-cliente no es opcional. Segundo, una **cota superior del beneficio alcanzable**: con pocos alimentadores, la enumeración exhaustiva da un orden oráculo para cada extracción de escenario, lo que muestra cuánto margen deja cualquier heurística. Tercero, **un modo de falla conocido de la heurística propuesta**: una regla de tiempo hasta el impacto más temprano ignora los pesos y la ramificación, de modo que puede perder frente a una regla que restablece el alimentador que protege más servicios ponderados, aunque el primer impacto de ese alimentador sea algo más tardío. El capítulo 6 muestra exactamente esto.

### 3.3 Grafos de dependencias con reservas

#### 3.3.1 Representación

Represente cada relación proveedor → dependiente como una arista dirigida etiquetada con la reserva que tiene el dependiente para ese proveedor. Si el proveedor *A* falla en el instante *t_A*, el dependiente *B* falla en *t_A* + *b_AB* salvo que se lo restablezca antes. Si *B* falla cuando falla *cualquiera* de sus proveedores (un «O» de fallas, sin redundancia), el instante de falla de *B* es el mínimo sobre los caminos entrantes, lo que es un cálculo de camino más corto con las reservas como pesos de las aristas.

#### 3.3.2 Laboratorio de tiempo hasta el impacto

```python
# Lab 3 - time-to-impact on a synthetic Riverbend dependency graph (offline, standard library only)
# Edge (supplier -> dependant, buffer_hours): the dependant fails `buffer_hours` after it loses that supplier.
import heapq
edges = [
    ("F2", "TEL", 8),     # telecom central office: batteries plus generator fuel on hand
    ("F2", "HOSP", 26),   # hospital: generator fuel on hand
    ("F3", "WATER", 9),   # treatment plant generator + clearwell storage
    ("F3", "WSCADA", 2),  # water SCADA server UPS
    ("TEL", "WSCADA", 0), # remote telemetry needs the carrier circuit
    ("WATER", "HOSP", 4), # hospital on-site water storage
    ("TEL", "DISPATCH", 1),  # emergency dispatch: ring-down backup lasts 1 h
    ("F1", "RES", 0), ("F4", "COM", 0),
]
def time_to_impact(initial):  # initial: {node: failure time}
    graph = {}
    for s, d, b in edges:
        graph.setdefault(s, []).append((d, b))
    best = dict(initial)
    pq = [(t, n) for n, t in initial.items()]
    heapq.heapify(pq)
    while pq:
        t, n = heapq.heappop(pq)
        if t > best.get(n, float("inf")):
            continue
        for d, b in graph.get(n, []):
            if t + b < best.get(d, float("inf")):
                best[d] = t + b
                heapq.heappush(pq, (t + b, d))
    return best
tti = time_to_impact({"F1": 0, "F2": 0, "F3": 0, "F4": 0})
for node in sorted(tti, key=lambda n: (tti[n], n)):
    print(f"{node:9} fails at t={tti[node]:>3} h")
degree = {}
for s, d, _ in edges:
    degree[s] = degree.get(s, 0) + 1
    degree[d] = degree.get(d, 0) + 1
print("degree ranking:", sorted(degree, key=lambda n: (-degree[n], n))[:4])
```

Salida esperada:

```text
COM       fails at t=  0 h
F1        fails at t=  0 h
F2        fails at t=  0 h
F3        fails at t=  0 h
F4        fails at t=  0 h
RES       fails at t=  0 h
WSCADA    fails at t=  2 h
TEL       fails at t=  8 h
DISPATCH  fails at t=  9 h
WATER     fails at t=  9 h
HOSP      fails at t= 13 h
degree ranking: ['TEL', 'F2', 'F3', 'HOSP']
```

Tres lecciones. **Dominan los caminos indirectos:** el generador propio del hospital da 26 horas, pero el hospital falla en la hora 13 por el camino del agua (9 + 4). Un estudio que registrara solo la reserva eléctrica directa de cada instalación juzgaría mal su prioridad por medio día. **El grado no es la consecuencia:** la centralidad de grado pone TEL en primer lugar, lo que aquí es razonable, pero pone HOSP por encima de WATER y no dice nada sobre los tiempos. **El supuesto del «O» es fuerte:** el SCADA del agua falla en la hora 0 + 0 a través de TEL *solo* si la telemetría no tiene un camino alternativo; en muchas empresas de servicios, los operadores pueden hacer funcionar la planta localmente sin SCADA, de modo que la falla de WSCADA puede no tener consecuencia para el servicio. El grafo debe distinguir la *pérdida de una función* de la *pérdida de un servicio*.

#### 3.3.3 Lo que la representación deja fuera

Las aristas con reservas fijas omiten: la **dinámica de agotamiento** (el combustible de un generador dura más a carga parcial); la **redundancia** (lógica «Y»: un hospital con dos alimentaciones independientes solo falla cuando fallan ambas); las **dependencias del restablecimiento** (un alimentador no puede reenergizarse sin comunicaciones con las cuadrillas de campo, una dependencia en la dirección de la *recuperación*); las **reservas humanas** (operación manual, ayuda mutua, entregas de combustible que amplían las reservas si las carreteras y las telecomunicaciones funcionan); y la **adaptación del adversario** (un adversario que conoce la lista de prioridades puede atacar su primer puesto). Una propuesta debe enumerar qué omisiones podrían invertir sus conclusiones y cómo las pondrá a prueba el estudio (§3.7).

### 3.4 El mecanismo

Un mecanismo es una cadena de eslabones, cada uno de los cuales podría fallar, que predice un *patrón* y no solo un efecto medio:

1. Los servicios críticos dependen de reservas cuyas duraciones difieren mucho (horas para las baterías de telecomunicaciones y los respaldos de despacho, días para el combustible de los hospitales).
2. En una interrupción de varios alimentadores que requiere restablecimiento manual secuencial, el orden de restablecimiento determina qué reservas se agotan.
3. La práctica convencional o bien maximiza los clientes restablecidos (regla de Smith), o bien restablece primero a los «clientes críticos» en un orden que no usa el tiempo de las reservas.
4. Ordenar por tiempo hasta el impacto restablece primero los alimentadores cuyos servicios críticos fallarían antes, de modo que se agotan menos reservas.
5. Por tanto, la pérdida ponderada de servicios críticos disminuye.

El mecanismo predice un patrón:

- **Beneficio frente al orden de clientes primero** siempre que los servicios críticos estén en alimentadores con pocos clientes.
- **Beneficio frente al orden por indicador crítico solo cuando discrepan**: cuando el orden por tiempo de las reservas entre los alimentadores críticos difiere del orden por número de clientes entre ellos. Cuando los órdenes coinciden, las dos reglas son idénticas y el beneficio debe ser cero.
- **Ningún beneficio cuando las reservas superan el tiempo total de restablecimiento**: si todas las reservas duran más que la interrupción, el orden no puede importar para los servicios críticos.
- **Un costo en horas-cliente** respecto de la regla de Smith, mayor cuando los servicios críticos están en alimentadores pequeños.
- **Fragilidad ante errores del mapa**: si el mapa de dependencias o las reservas son erróneos, el orden puede ser peor que una simple lista de indicadores.

Un mecanismo que predice dónde falla la intervención vale más que uno que solo predice el éxito, porque son las fallas las que lo distinguen de los rivales.

### 3.5 Hipótesis, métricas y efecto mínimo de interés

Métrica principal: **pérdida ponderada de servicios críticos** en una ventana de 72 horas, con pesos declarados de antemano (hospital 5, agua 4, telecomunicaciones 3, despacho de emergencias 4 por hora de servicio), obtenidos del personal de gestión de emergencias de los socios antes de cualquier simulación (capítulo 1, §1.6.3). Métrica secundaria (de seguridad): **horas-cliente perdidas** (miles).

- **H1 (beneficio frente a clientes primero).** DEP reduce la pérdida ponderada media de servicios críticos en al menos un 20 % en comparación con SILO.
- **H2 (contribución sobre la mejor práctica).** DEP reduce la pérdida ponderada media de servicios críticos en al menos un 10 % en comparación con CRITFLAG (lista de indicadores de clientes críticos ordenada por clientes), en cada región de estudio.
- **H3 (patrón del mecanismo).** La diferencia DEP − CRITFLAG es cero cuando los dos órdenes coinciden y crece con el número de posiciones en que difieren; se reduce hacia cero a medida que las reservas crecen en relación con el tiempo de restablecimiento.
- **H4a/H4b (no inferioridad).** DEP aumenta las horas-cliente perdidas medias en no más de un 15 % en comparación con SILO (H4a) y con CRITFLAG (H4b).

**Efectos mínimos de interés.** Los umbrales del 20 % y del 10 % y el margen del 15 % son juicios *prácticos*, no convenciones estadísticas: los socios declararon (sintético) que un cambio en la práctica de restablecimiento exige reentrenamiento, revisión de procedimientos y explicaciones al regulador, que solo emprenderían por una reducción de al menos un 10 % en la pérdida de servicios críticos respecto de su práctica actual de indicadores críticos; y el consejo de la cooperativa no aceptaría más de un 15 % de horas-cliente adicionales sin consulta pública. Registre quién fijó cada umbral y cuándo; un umbral elegido después de ver los resultados no vale nada.

Obsérvese que la teoría de la programación predice que H4a *fallará* siempre que los servicios críticos estén en alimentadores pequeños. Declararla de antemano de todos modos es lo correcto: el estudio debe reportar con honestidad el tamaño de la compensación en lugar de ocultarlo, y una prueba de no inferioridad fallida es un hallazgo para los responsables de las políticas.

### 3.6 Líneas de base

Una contribución es tan fuerte como la línea de base que supera.

| Línea de base | Por qué incluirla | Qué mostraría superarla |
|---|---|---|
| **SILO** — más clientes primero | Óptima para las horas-cliente con duraciones iguales (regla de Smith); opción predeterminada habitual | Que el orden consciente de la criticidad protege los servicios críticos: esperable y débil como contribución |
| **CRITFLAG** — primero los alimentadores con alguna instalación crítica de la lista, por clientes | Representa la práctica extendida de mantener listas de clientes críticos | La contribución real: que la información de *tiempos* aporta valor más allá de una lista |
| **ORACLE** — el mejor de todos los órdenes para cada extracción (calculable para ≤ 6–7 alimentadores) | Cota superior de cualquier regla | Cuánto margen queda; si DEP está cerca del óptimo |
| **RANDOM** (opcional) | Comprobación de sensatez | Que la métrica no es degenerada |

Superar a SILO es necesario pero no suficiente; la afirmación vive o muere frente a CRITFLAG. El ejemplo resuelto del §3.9 muestra cómo una propuesta que omitía CRITFLAG habría parecido impresionante y habría sido errónea.

### 3.7 Explicaciones rivales

| Rival | Predicción que la sustentaría | Elemento del diseño que la pone a prueba |
|---|---|---|
| Cualquier lista de criticidad explica la ganancia, no los tiempos | DEP ≈ CRITFLAG | Línea de base CRITFLAG; H2 |
| La ganancia es un artefacto de los pesos | La ganancia desaparece con pesos iguales o alternativos | Sensibilidad a los pesos (capítulo 6) |
| La ganancia es un artefacto de las reservas cortas de la región elegida | La ganancia se desvanece con reservas más largas y realistas | Análisis de escalado de reservas; segunda región con contratos de combustible |
| El modelo se construyó para favorecer a DEP (circularidad) | La ganancia se reduce en un modelo construido de forma independiente o con un mapa erróneo | Segunda región construida por otro modelador a partir de datos de los socios; prueba de error del mapa |
| Los operadores no seguirían el orden | Las elecciones en el ejercicio de mesa difieren de DEP incluso mostrando el tiempo hasta el impacto | Ejercicio de mesa a ciegas con operadores (capítulo 5) |
| El supuesto de una sola cuadrilla determina el resultado | La ganancia desaparece con varias cuadrillas | Port Halvard con dos cuadrillas |
| Error de discretización o de implementación | Los resultados cambian con el paso temporal o la implementación | Verificación frente a una implementación independiente basada en eventos (capítulo 4) |

### 3.8 Condiciones de fracaso y registro de riesgos

**Condiciones de fracaso declaradas de antemano** (cada una corresponde a un cambio en la afirmación):

| Condición | Consecuencia para la afirmación |
|---|---|
| H2 falla en ambas regiones | Abandonar la contribución de método; reportar que los tiempos no añaden nada medible sobre las listas de indicadores críticos; conservar el análisis de programación como contribución teórica. |
| H2 falla en una región y se cumple en la otra | Acotar a las condiciones que las distinguen; poner a prueba H3 para ver si el mecanismo explica la diferencia. |
| Patrón de H3 ausente (ganancia sin relación con la divergencia de órdenes) | Mecanismo sin sustento; cualquier ganancia queda sin explicar y no debe generalizarse. |
| H4b falla | Reportar una compensación; el método no es «gratuito» respecto de la práctica actual. |
| La ganancia se desploma con errores plausibles del mapa | Afirmación condicionada a la exactitud del mapa; añadir una auditoría del mapa como requisito previo. |
| Los operadores rechazan el orden en el ejercicio de mesa | Afirmación limitada a «una ayuda a la decisión cuya adopción no está demostrada»; estudiar las barreras a la adopción. |

**Registro de riesgos** (selección): retirada de un socio (mitigación: diseño de región sintética que no dependa de los datos de un solo socio); exposición de datos sensibles (almacenamiento por niveles, ningún mapa real en el texto público); error del simulador (reimplementación independiente y pruebas unitarias); participantes del ejercicio de mesa identificables (reporte agregado, ninguna combinación de función y empresa de servicios en el texto público); presión del financiador (acuerdo de publicación firmado antes de empezar el trabajo).

### 3.9 Ejemplo resuelto: la propuesta que casi omitió la línea de base real

El primer borrador del candidato comparaba DEP solo con SILO y reportaba, en una ejecución piloto, una reducción de casi el 90 % en la pérdida ponderada de servicios críticos. El comité de supervisión hizo dos preguntas: *¿Qué hacen hoy realmente las empresas de servicios?* y *¿Qué lograría un orden perfecto?* Entrevistas (sintéticas) con tres despachadores revelaron que las tres empresas de servicios mantienen una lista de clientes críticos y restablecen pronto esos alimentadores. El candidato añadió CRITFLAG y ORACLE. El piloto mostró entonces que DEP y CRITFLAG eran casi indistinguibles en Riverbend, y ambos estaban lejos de ORACLE. El veredicto del comité: la cifra del 90 % medía el valor de *tener una lista de clientes críticos*, que no es nuevo; la pregunta abierta es si los *tiempos* añaden valor, y Riverbend por sí sola —con solo dos alimentadores críticos, que la mayoría de las reglas ordenan igual— no puede responderla. La propuesta se revisó para declarar de antemano H2 y H3, para elegir una segunda región según criterios de diseño enunciados (más alimentadores críticos, órdenes divergentes por reservas y por clientes, dos cuadrillas, contratos de combustible) *antes* de cualquier simulación en ella, y para realizar un análisis de muchas regiones en el que la divergencia entre órdenes varíe sistemáticamente.

Esta es la decisión de diseño más importante del libro: **elija la comparación que representa la mejor práctica actual, no la que hace que el método se vea mejor.**

### 3.10 Errores habituales y límites

- Comparar con una línea de base de paja (ninguna priorización, o aleatoria).
- Omitir el lado del costo de una compensación que la teoría de la programación predice.
- Definir «crítico» después de ver qué instalaciones se benefician.
- Codificar las reservas como valores puntuales sin incertidumbre.
- Tratar un grafo con semántica «O» como si modelara la redundancia.
- Redactar un mecanismo que solo predice el éxito.
- Fijar el efecto mínimo de interés por convención estadística en lugar de por consecuencia práctica.

- Elegir el segundo contexto después de ver qué tipo de región favorece al método, en lugar de fijar de antemano los criterios de selección.
- Tratar una regla de tiempo hasta el impacto más temprano como óptima cuando la teoría de la programación muestra que el problema ponderado es difícil y que la regla ignora los pesos y la ramificación.
- Registrar solo la reserva eléctrica directa de cada instalación, de modo que se pierden caminos indirectos como la dependencia del hospital respecto del agua.
- Dejar que el socio que aporta los datos también elija los umbrales sin registrar quién los fijó y cuándo.

### Ejercicios — capítulo 3

**EX015 — Tipificación de contribuciones.** *Objetivo:* emparejar afirmaciones con evidencia. *Entradas:* cuatro afirmaciones sintéticas de tesis: (a) «Publicamos GridWater-Sim 2.0»; (b) «Nuestro instrumento de encuesta sobre la duración de las reservas es confiable»; (c) «Las empresas de servicios rara vez usan el tiempo de las reservas al ordenar el restablecimiento»; (d) «El orden por tiempo hasta el impacto reduce la pérdida de servicios críticos». *Restricciones:* use el §3.1. *Pasos:* (1) asigne a cada afirmación un tipo de contribución; (2) enuncie la evidencia mínima que exige ese tipo; (3) indique qué afirmación depende de otra; (4) diga qué afirmación no debe hacer el Estudio Cascada a partir de (a) solamente. *Evidencia esperada:* tabla. *Rúbrica:* 3 = tipos y evidencia correctos, (d) depende de (a) solo como instrumento, (c) necesita un estudio empírico muestreado; 2 = un error; 1 = evidencia genérica; 0 = nada.

**EX016 — Comprobación con la teoría de la programación.** *Objetivo:* aplicar la regla de Smith. *Entradas:* clientes de Riverbend F1 9000, F2 1200, F3 2500, F4 6000; duraciones de restablecimiento de 4, 3, 5 y 4 horas respectivamente; una cuadrilla. *Restricciones:* muestre los cálculos. *Pasos:* (1) calcule w/p para cada alimentador; (2) dé el orden de Smith; (3) calcule las horas-cliente (miles) para el orden de Smith y para el orden F2, F3, F1, F4; (4) indique el aumento porcentual. *Evidencia esperada:* cálculos. *Rúbrica:* 3 = orden F1, F4, F3, F2 (cocientes 2250, 1500, 500, 400), totales de 135,7 y 227,6 miles de horas-cliente, un aumento del 67,7 %; 2 = desliz aritmético; 1 = regla equivocada; 0 = nada.

**EX017 — Ampliación del tiempo hasta el impacto.** *Objetivo:* ampliar el Laboratorio 3. *Entradas:* Laboratorio 3. *Restricciones:* sin conexión. *Pasos:* (1) añada una dependencia de entrega de combustible: la reserva del generador del hospital pasa a ser de 60 h si TEL está disponible para pedir combustible, modelado sustituyendo la reserva F2 → HOSP por 60 y añadiendo TEL → HOSP con reserva 30; (2) ejecute y registre el instante de falla de HOSP; (3) explique por qué el resultado no cambió; (4) indique qué no puede expresar el grafo con semántica «O» sobre este acuerdo de combustible. *Evidencia esperada:* código, salida, explicación. *Rúbrica:* 3 = HOSP sigue en 13 h por el agua; explica que una *ampliación de la reserva condicionada a otro servicio* es una relación Y/condicional que el grafo «O» no puede expresar; 2 = salida correcta, explicación parcial; 1 = salida errónea; 0 = no se ejecutó.

**EX018 — Conjunto de hipótesis.** *Objetivo:* operacionalizar hipótesis. *Entradas:* el mecanismo del §3.4, aplicado a otro dominio de su elección (por ejemplo, restablecer sitios de telecomunicaciones tras un incidente cibernético en un operador, con hospitales y despacho como dependientes). *Restricciones:* una hipótesis de beneficio, una de contribución sobre la mejor práctica, una de patrón del mecanismo y una de no inferioridad; umbrales justificados. *Pasos:* (1) redacte cada hipótesis con población, intervención, comparador, resultado y dirección; (2) defina operacionalmente cada resultado; (3) justifique cada umbral por una consecuencia práctica. *Evidencia esperada:* bloque de hipótesis. *Rúbrica:* 3 = completo y operacional, comparador de mejor práctica nombrado, umbrales justificados por consecuencias y responsables; 2 = un elemento vago; 1 = umbrales arbitrarios; 0 = nada.

**EX019 — Tabla de explicaciones rivales.** *Objetivo:* diseñar frente a alternativas. *Entradas:* sus hipótesis del EX018. *Restricciones:* al menos seis rivales. *Pasos:* (1) enumere al menos seis explicaciones rivales de un resultado positivo; (2) para cada una, enuncie la predicción que la sustentaría; (3) nombre el elemento del diseño que la pone a prueba. *Evidencia esperada:* tabla. *Rúbrica:* 3 = seis o más rivales plausibles, incluidos la adecuación de la línea de base, los pesos, la circularidad y la adopción, cada uno con un elemento de diseño concreto; 2 = cuatro o cinco; 1 = genéricos; 0 = nada.

**EX020 — Condiciones de fracaso y criterios del segundo contexto.** *Objetivo:* hacer falsable la contribución y evitar elegir a conveniencia el contexto de validación. *Entradas:* su propuesta. *Restricciones:* al menos cinco condiciones de fracaso con sus consecuencias; criterios de selección de un segundo contexto redactados *antes* de modelarlo. *Pasos:* (1) redacte condiciones de fracaso asociadas a cambios en la afirmación; (2) redacte de tres a cinco criterios de selección del contexto derivados del mecanismo; (3) explique cómo podría verificar un revisor que los criterios se fijaron de antemano. *Evidencia esperada:* dos listas y un párrafo. *Rúbrica:* 3 = cada condición cambia una afirmación específica, criterios derivados del mecanismo (divergencia de órdenes, número de cuadrillas, rango de reservas), prerregistro con marca de tiempo nombrado; 2 = criterios no derivados del mecanismo; 1 = vago; 0 = nada.

### Síntesis del capítulo

Una contribución doctoral debe decir de qué tipo es y debe superar a la práctica actual más fuerte, no a un hombre de paja. El orden de restablecimiento es un problema de programación: la regla de Smith hace que «más clientes primero» sea óptimo para las horas-cliente, mientras que los servicios críticos limitados por reservas crean un objetivo de retraso ponderado para el cual las reglas simples son heurísticas. Esa teoría predice la compensación, aporta una cota oráculo y expone la debilidad de la regla propuesta. Los grafos de dependencias con reservas revelan caminos indirectos que dominan los tiempos, pero hay que nombrar su semántica «O», sus reservas fijas y las dependencias humanas y de la dirección de la recuperación que les faltan. El mecanismo predice un patrón —beneficio solo donde los tiempos y el número de clientes discrepan, ninguno cuando las reservas son largas, un costo en horas-cliente y fragilidad ante errores del mapa— y las hipótesis, las líneas de base, los rivales y las condiciones de fracaso se redactan para que cada parte de ese patrón pueda demostrarse falsa.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 08

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Replicación de líneas de base y piloto

### Resultados de aprendizaje y conexión

Al terminar este capítulo, el estudiante será capaz de:

1. Distinguir la reproducción, la replicación y las comprobaciones de robustez, y elegir cuál necesita una línea de base.
2. Reproducir un cálculo de modelo publicado, declarar de antemano una tolerancia, diagnosticar una discrepancia y redactar una bitácora de reproducción.
3. Verificar un simulador con invariantes, pruebas unitarias y una implementación independiente antes de confiar en cualquier comparación que produzca.
4. Reconocer los artefactos de los protocolos de evaluación —ajuste por punto, fuga temporal, características propias del banco de pruebas— que inflan las líneas de base de detección.
5. Obtener de expertos y documentar los parámetros del modelo con incertidumbre explícita.
6. Diseñar un piloto acotado cuyo propósito sea la factibilidad, con criterios de continuar o detener, y explicar por qué un piloto no debe usarse para estimar el tamaño del efecto.

El capítulo 3 fijó las hipótesis, las líneas de base y las condiciones de fracaso. Antes de que el estudio principal pueda comparar DEP con SILO, CRITFLAG y ORACLE, hay que demostrar que cada número del que dependen esas comparaciones significa lo que afirma.

### 4.1 Reproducción, replicación, robustez

Las [National Academies (2019)](https://doi.org/10.17226/25303) distinguen la **reproducibilidad** —obtener resultados coherentes con los mismos datos de entrada, pasos computacionales, métodos y condiciones de análisis— de la **replicabilidad** —obtener resultados coherentes entre estudios dirigidos a la misma pregunta, cada uno con sus propios datos—. Una tercera actividad, a menudo llamada comprobación de **robustez**, varía las decisiones analíticas sobre los mismos datos. Las tesis sobre infraestructura necesitan las tres:

| Actividad | Ejemplo del Estudio Cascada | Contra qué protege |
|---|---|---|
| Reproducción | Volver a ejecutar un cálculo de inoperabilidad publicado con la matriz publicada | Malinterpretar convenciones; errores de programación en la línea de base |
| Replicación | Construir Port Halvard de forma independiente y comprobar si se mantiene el resultado de Riverbend | Hallazgos propios de un contexto o de un modelo |
| Robustez | Variar pesos, reservas, paso temporal, horizonte | Resultados que dependen de una sola elección arbitraria |

### 4.2 Reproducir un cálculo de modelo: el modelo insumo-producto de inoperabilidad

#### 4.2.1 El modelo

El modelo insumo-producto de inoperabilidad de Haimes y Jiang ([2001](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1))) adapta la economía insumo-producto de Leontief a la infraestructura. Cada sector *i* tiene una inoperabilidad *q_i* entre 0 (plenamente operable) y 1 (plenamente inoperable). El equilibrio tras una perturbación inicial *c\** es *q* = *A\*q* + *c\**, de donde *q* = (*I* − *A\**)⁻¹ *c\**. El elemento *A\*_ij* es la inoperabilidad que aporta al sector *i* cada unidad de inoperabilidad del sector *j*. La convención importa: la fila es el sector *receptor* y la columna el sector *proveedor*. Los artículos y el software difieren en la notación, y algunos derivan *A\** de tablas económicas de insumo-producto mediante pasos de normalización en los que es fácil equivocarse de forma sutil.

#### 4.2.2 Laboratorio de reproducción

Un artículo «publicado» sintético informa que, tras una perturbación que deja la electricidad inoperable en un 50 %, el agua alcanza una inoperabilidad de equilibrio de 0,236 en un modelo de tres sectores. Declare de antemano una tolerancia de ± 0,005 (el redondeo de la publicación) y luego reproduzca:

```python
# Lab 4a - reproducing an inoperability input-output (IIM) result (offline, standard library only)
# q = (I - A*)^-1 c*. Convention: A*[i][j] = inoperability contributed to sector i per unit inoperability of sector j.
def solve(a, c):
    n = len(c)
    m = [[(1.0 if i == j else 0.0) - a[i][j] for j in range(n)] + [c[i]] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[piv] = m[piv], m[col]
        for r in range(n):
            if r != col:
                f = m[r][col] / m[col][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[col])]
    return [m[i][n] / m[i][i] for i in range(n)]
sectors = ["power", "water", "telecom"]
A = [[0.00, 0.05, 0.10],   # power depends a little on water (cooling) and telecom (SCADA comms)
     [0.40, 0.00, 0.15],   # water depends strongly on power
     [0.30, 0.02, 0.00]]   # telecom depends on power
c = [0.50, 0.00, 0.00]    # initial perturbation: power 50% inoperable
q = solve(A, c)
print("convention A* (row = receiving sector):", [round(x, 3) for x in q])
At = [list(r) for r in zip(*A)]
qt = solve(At, c)
print("transposed by mistake:               ", [round(x, 3) for x in qt])
```

Salida esperada:

```text
convention A* (row = receiving sector): [0.528, 0.236, 0.163]
transposed by mistake:                [0.528, 0.028, 0.057]
```

Con la convención correcta, la reproducción coincide (agua 0,236). Con la matriz traspuesta —un error que no produce ninguna advertencia, ningún fallo y un vector de aspecto plausible—, la inoperabilidad del agua cae casi un orden de magnitud y la *clasificación* de los sectores cambia: las telecomunicaciones aparecen ahora más afectadas que el agua. El valor de la propia electricidad coincide casualmente en ambos casos, y eso es exactamente lo que vuelve peligroso el error: quien replique comprobando solo el sector perturbado declararía el éxito.

#### 4.2.3 La bitácora de reproducción

Una bitácora de reproducción registra: el valor objetivo y su fuente (página, tabla); la tolerancia, fijada *antes* de ejecutar; el entorno de software (versión del lenguaje, sistema operativo); las entradas y su procedencia; la salida exacta; las discrepancias y su diagnóstico; y la decisión (reproducido, reproducido tras una corrección, no reproducido). Cuando la convención de los autores originales es ambigua, escríbales; registre la correspondencia. Una no reproducción es un resultado, no una vergüenza, y pertenece a la tesis.

#### 4.2.4 Lo que un IIM reproducido puede sustentar y lo que no

Reproducir el cálculo solo muestra que se entiende la aritmética. El IIM sigue siendo lineal y basado en el equilibrio: no modela reservas, tiempos ni orden de restablecimiento, y sus coeficientes suelen derivarse de flujos económicos y no de dependencias de ingeniería. En el Estudio Cascada sirve como **contraste a nivel sectorial** —¿coinciden los sectores que el IIM clasifica como más afectados con los servicios que el modelo de reservas muestra fallando?— y no como competidor del modelo de restablecimiento.

### 4.3 La discrepancia de GridWater-Sim (sintética)

El banco de referencia sintético GridWater-Sim reporta, para una configuración similar a Riverbend, una pérdida ponderada media de servicios críticos con restablecimiento de clientes primero que la reimplementación del candidato no pudo igualar dentro de la tolerancia declarada de antemano. El diagnóstico siguió el orden que con más frecuencia encuentra la causa:

1. **Entradas.** ¿Se usaron las mismas distribuciones de parámetros? La documentación del banco de referencia daba las distribuciones triangulares como (mínimo, moda, máximo); `random.triangular` de Python recibe (mínimo, máximo, moda). Intercambiar la moda y el máximo desplaza la media sin dar aviso.
2. **Semántica.** ¿«Restablecido» significa reenergizado o servicio reanudado? GridWater-Sim aplicaba un retardo de rearranque de una hora solo al agua; la reimplementación lo aplicaba a todos los servicios.
3. **Numérica.** El banco de referencia avanzaba el tiempo en pasos fijos; la reimplementación calculaba intervalos de interrupción exactos. Los pasos fijos introducen un error de discretización que depende del paso y de dónde caen los vencimientos de las reservas dentro de un paso.
4. **Aleatoriedad.** ¿Eran idénticos las semillas y el orden de las extracciones? El orden importa: extraer las duraciones antes que las reservas en una implementación y después en otra produce conjuntos de escenarios distintos a partir de la misma semilla.

Tras alinear (1) y (2), la diferencia restante quedó dentro de la tolerancia y se redujo con pasos temporales más pequeños, lo que confirmó (3). La tesis registra el banco de referencia como *reproducido tras corregir una ambigüedad en el orden de los parámetros*, reporta los valores originales y corregidos, y adopta la implementación de intervalos exactos, conservando la versión de pasos temporales como comprobación independiente.

### 4.4 Verificar un simulador

La verificación pregunta si el modelo está implementado correctamente; la validación pregunta si representa el sistema real de forma adecuada para su propósito ([Sargent, 2013](https://doi.org/10.1057/jos.2012.20)). La verificación va primero, porque validar una implementación con errores no tiene sentido. **Invariantes** que debe cumplir cualquier simulador de restablecimiento correcto:

- Si todas las reservas superan el horizonte, la pérdida ponderada de servicios críticos es cero con cualquier orden.
- Dos políticas que producen el mismo orden producen resultados idénticos con extracciones idénticas.
- La pérdida del oráculo es menor o igual que la de cada política en cada extracción.
- Aumentar una reserva, con todo lo demás fijo, nunca aumenta la pérdida.
- Las horas-cliente con la regla de Smith son menores o iguales que con cualquier otro orden cuando las duraciones de restablecimiento son iguales.
- La pérdida y las horas-cliente no son negativas y están acotadas por peso × horizonte y clientes × horizonte.

Las **pruebas unitarias** comprueban los componentes más pequeños: la aritmética de intervalos de un solo servicio; el efecto de una dependencia con reserva en el sitio; la asignación de cuadrillas con dos cuadrillas. Las **pruebas entre implementaciones** comparan dos implementaciones escritas de forma independiente con extracciones fijas. Las **pruebas de condiciones extremas** usan reservas nulas, duraciones nulas y un solo alimentador. Conserve las pruebas en el archivo (capítulo 7); un revisor que puede ejecutarlas confía más en las comparaciones que uno que debe aceptarlas por fe.

### 4.5 Replicar una línea de base de detección: artefactos de evaluación

Aunque el Estudio Cascada no propone un detector, su análisis del tiempo hasta el impacto depende de cuándo se reconoce una interrupción, y el candidato debe ser capaz de juzgar las líneas de base de detección reportadas para la infraestructura. Los mecanismos habituales de inflación son decisiones de evaluación, no propiedades del modelo.

#### 4.5.1 Ajuste por punto

[Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) mostraron que el ajuste por punto (PA) —contar como detectado todo un segmento anómalo cuando se señala cualquier punto de él— puede hacer que puntuaciones aleatorias parezcan excelentes. El siguiente laboratorio reproduce el efecto con etiquetas sintéticas:

```python
# Lab 4b - how point adjustment (PA) inflates detection scores (offline, standard library only)
import random
random.seed(42)
N = 2000
labels = [0] * N
for start, length in [(300, 60), (900, 120), (1500, 80)]:
    for t in range(start, start + length):
        labels[t] = 1
scores = [random.random() for _ in range(N)]          # a detector that knows nothing
thr = sorted(scores)[int(0.97 * N)]                    # alarm on the top 3% of scores
pred = [1 if s > thr else 0 for s in scores]
def f1(p, y):
    tp = sum(1 for a, b in zip(p, y) if a and b)
    fp = sum(1 for a, b in zip(p, y) if a and not b)
    fn = sum(1 for a, b in zip(p, y) if b and not a)
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    return round(2 * prec * rec / (prec + rec), 3) if prec + rec else 0.0
def segments(y):
    segs, t = [], 0
    while t < len(y):
        if y[t]:
            s = t
            while t < len(y) and y[t]:
                t += 1
            segs.append((s, t))
        else:
            t += 1
    return segs
def adjust(p, y, k=0.0):
    q = list(p)
    for s, e in segments(y):
        hit = sum(p[s:e]) / (e - s)
        if hit > k:
            for t in range(s, e):
                q[t] = 1
    return q
print("point-wise F1           :", f1(pred, labels))
print("F1 after PA             :", f1(adjust(pred, labels), labels))
print("F1 after PA%K (K = 0.20):", f1(adjust(pred, labels, 0.20), labels))
print("segments hit by >=1 alarm:", sum(1 for s, e in segments(labels) if any(pred[s:e])), "of", len(segments(labels)))
```

Salida esperada:

```text
point-wise F1           : 0.05
F1 after PA             : 0.911
F1 after PA%K (K = 0.20): 0.05
segments hit by >=1 alarm: 3 of 3
```

Un detector sin ninguna información obtiene 0,911 tras el PA porque cada segmento largo contiene, por azar, al menos una de las alarmas aleatorias del 3 %. PA%K con K = 20 % elimina aquí la inflación. Para la investigación en IC, la lección va más allá: ninguna de las dos métricas dice *cuándo* se produjo la primera alarma verdadera respecto del inicio del segmento, que es lo que importa para las reservas. Una métrica relevante para la consecuencia es la **latencia de detección relativa al tiempo hasta el impacto**: la fracción de incidentes detectados antes de que se agote la reserva del primer servicio dependiente.

#### 4.5.2 Otros artefactos

- **Fuga temporal.** Las divisiones aleatorias de series temporales en entrenamiento y prueba permiten que un modelo aprenda del futuro. Use divisiones ordenadas en el tiempo que imiten el despliegue.
- **Características propias del banco de pruebas.** Un detector puede aprender firmas de las herramientas de inyección de ataques del banco de pruebas o de sus sensores específicos en lugar de los ataques.
- **Cobertura del conjunto de ataques.** Los ataques de un conjunto de datos los eligieron quienes lo construyeron; el rendimiento frente a ellos dice poco sobre otras clases de ataque ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)).
- **Tasas base.** Una tasa de falsos positivos que parece pequeña en un conjunto de datos equilibrado puede desbordar a los operadores con tasas base realistas ([Sommer y Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 4.6 Obtención de parámetros

Las reservas, las duraciones de restablecimiento y los pesos del modelo provienen de personas. La obtención estructurada del juicio experto —preparar a los expertos, pedir cuantiles en lugar de valores únicos, devolverles las distribuciones implícitas y registrar sus razones— reduce el anclaje y el exceso de confianza ([O'Hagan et al., 2006](https://doi.org/10.1002/0470033312)). Para el Estudio Cascada (sintético):

| Parámetro | Obtenido de | Forma | Documentación |
|---|---|---|---|
| Duración del restablecimiento de un alimentador | Tres despachadores de la REC | Mínimo, más probable y máximo para maniobras manuales sin SCADA | Razón de cada valor; desacuerdos registrados |
| Reserva de telecomunicaciones | Ingeniero de instalaciones del operador | Autonomía de baterías con la carga medida, horas de combustible del generador | Supuesto de carga enunciado |
| Reserva de agua | Gerente de operaciones de la RWA | Autonomía del generador más vaciado del almacenamiento hasta la presión mínima | Supuesto de demanda (estación) enunciado |
| Reserva del hospital | Director de instalaciones | Combustible disponible con la carga típica; horas de agua en el sitio | Se distinguen los requisitos normativos del inventario real |
| Pesos | Panel de gestión de emergencias | Comparaciones por pares convertidas en pesos | Obtenidos antes de cualquier simulación; firmados y fechados |

Las distribuciones triangulares son una elección pragmática para obtenciones de tres puntos; no se derivan de la física. El capítulo 6 pone a prueba si las conclusiones dependen de la familia de distribuciones.

### 4.7 El piloto

#### 4.7.1 Para qué sirve un piloto

Un piloto pone a prueba la **factibilidad**: si funcionan los procedimientos, los materiales, los tiempos, los flujos de datos y los instrumentos. No es un estudio principal pequeño. Los tamaños del efecto estimados a partir de pilotos son demasiado imprecisos para planificar tamaños de muestra o para sustentar afirmaciones ([Leon, Davis y Kraemer, 2011](https://doi.org/10.1016/j.jpsychires.2010.10.008)). El piloto del Estudio Cascada tuvo dos vertientes:

1. **Piloto de simulación.** Ejecutar las cuatro políticas con 50 extracciones para comprobar que funcionan el código, el registro y los invariantes, que el tiempo de ejecución permite el número de extracciones previsto y que la censura a las 72 horas es poco frecuente. Los *resultados* del piloto (diferencias entre políticas) se registran como exploratorios y no se interpretan.
2. **Piloto de ejercicio de mesa.** Tres operadores (participantes sintéticos P01–P03, no elegibles para el estudio principal) trabajaron un escenario de 40 minutos con y sin una visualización del tiempo hasta el impacto. Preguntas: ¿entienden la visualización? ¿Revela el escenario el resultado demasiado pronto? ¿Cuánto tarda cada decisión? ¿Funciona el proceso de consentimiento y de cierre informativo?

#### 4.7.2 Criterios de continuar o detener (declarados de antemano)

| Criterio | Umbral | Resultado del piloto (sintético) | Decisión |
|---|---|---|---|
| Pasan las pruebas de invariantes | Todas | Todas | Continuar |
| Censura a las 72 h | < 1 % de las combinaciones servicio-extracción | 0 % | Continuar |
| Tiempo de ejecución para 500 extracciones, incluido el oráculo | < 1 hora | Minutos | Continuar |
| Los participantes leen correctamente la visualización | ≥ 2 de 3 | 3 de 3 tras un cambio de redacción | Continuar con revisión |
| El escenario revela el resultado prematuramente | No | Sí: una inyección mencionaba el «desvío hospitalario» | Revisar la inyección; repetir el piloto con un participante |
| Duración de la sesión | ≤ 60 min | 55 min | Continuar |

Cada revisión se registra en la bitácora de desviaciones con la fecha y la confirmación de que no existían datos del estudio principal.

### 4.8 Ejemplo resuelto: el piloto que cambió el escenario

En el piloto del ejercicio de mesa, P02 preguntó por qué la reserva del generador del hospital se mostraba como 26 horas cuando «todo el mundo sabe que el agua se va primero». El candidato solo había mostrado las reservas eléctricas directas. La visualización se revisó para mostrar el **tiempo efectivo hasta el impacto** (el mínimo sobre todos los caminos, como en el Laboratorio 3) junto a las reservas directas, con el camino indicado. Esto cambió el instrumento —un resultado legítimo de un piloto— y planteó una cuestión metodológica para el estudio principal: la comparación entre «con visualización» y «sin visualización» ponía a prueba ahora la visualización del tiempo efectivo hasta el impacto, y no simplemente cualquier información de criticidad. Las hipótesis del ejercicio de mesa se refinaron en consecuencia, *antes* del estudio principal, y el cambio se prerregistró como enmienda.

### 4.9 Errores habituales y límites

- Declarar exitosa una reproducción tras comprobar una sola salida.
- Fijar las tolerancias después de ver la discrepancia.
- Tratar el código del banco de referencia como la especificación cuando discrepa de su artículo, o viceversa, sin registrar cuál se siguió.
- Validar un simulador antes de verificarlo.
- Reportar el F1 con ajuste por punto para la detección en infraestructura sin la latencia relativa a la consecuencia.
- Pedir a los expertos números únicos y tratarlos como ciertos.
- Usar los tamaños del efecto del piloto para planificar o para afirmar.

- Comprobar solo el sector perturbado en una reproducción, como con la electricidad en la matriz de inoperabilidad traspuesta, que coincide con ambas convenciones.
- Suponer que el orden de los parámetros de una biblioteca coincide con la notación del artículo, como con la distribución triangular en el caso de GridWater-Sim.
- Interpretar las diferencias entre políticas en un piloto, cuando el propósito del piloto es la factibilidad y sus resultados se registran como exploratorios.
- Cambiar un instrumento del ejercicio de mesa tras el piloto sin registrar el cambio en la bitácora de desviaciones.

### Ejercicios — capítulo 4

**EX021 — Bitácora de reproducción.** *Objetivo:* documentar un intento de reproducción. *Entradas:* Laboratorio 4a. *Restricciones:* ejecutar sin conexión; tolerancia de ± 0,005 fijada antes de ejecutar. *Pasos:* (1) registre el objetivo (agua 0,236); (2) ejecute primero la matriz traspuesta y registre la discrepancia; (3) diagnostique usando la convención de la matriz; (4) ejecute la convención correcta; (5) redacte la entrada de la bitácora con los detalles del entorno. *Evidencia esperada:* bitácora de reproducción. *Rúbrica:* 3 = salidas exactas, diagnóstico de la convención, entorno registrado, observa que la electricidad coincide en ambas ejecuciones; 2 = falta un elemento; 1 = sin diagnóstico; 0 = no se ejecutó.

**EX022 — Análisis de perturbaciones con el IIM.** *Objetivo:* usar un modelo reproducido para una afirmación acotada. *Entradas:* Laboratorio 4a con la convención correcta. *Restricciones:* sin conexión. *Pasos:* (1) calcule *q* para las perturbaciones de electricidad 0,5 y de telecomunicaciones 0,5 por separado; (2) calcule *q* para ambas juntas; (3) compruebe si el resultado conjunto es igual a la suma de los resultados separados y explique por qué; (4) enuncie una afirmación que el modelo sustenta y otra que no puede sustentar. *Evidencia esperada:* tres vectores y un párrafo. *Rúbrica:* 3 = vectores correctos, linealidad (superposición) explicada, afirmación limitada a la inoperabilidad de equilibrio sin tiempos; 2 = vectores correctos, explicación pobre; 1 = errores; 0 = nada.

**EX023 — La trampa del orden de los parámetros.** *Objetivo:* detectar un error de entrada silencioso. *Entradas:* una distribución documentada como (low = 4, mode = 8, high = 12). *Restricciones:* use `random.triangular(low, high, mode)` de Python. *Pasos:* (1) calcule la media teórica, (low + mode + high) / 3, para la llamada correcta `triangular(4, 12, 8)`; (2) estime la media de la llamada errónea `triangular(4, 8, 12)` a partir de 100 000 extracciones con semilla y registre el mínimo y el máximo; explique qué muestrea realmente la llamada errónea; indique qué prueba lo habría detectado. *Evidencia esperada:* dos medias y una explicación. *Rúbrica:* 3 = media correcta 8,0; la llamada errónea trata 8 como *high* y 12 como *mode*, de modo que la fórmula de CPython devuelve 4 + 4·√(2u) para una *u* uniforme —valores en [4, ≈ 9,66] con media ≈ 7,77, que no forman en absoluto una distribución triangular—; una comprobación de la media por sí sola es débil, mientras que comprobar que el máximo de la muestra se acerca a 12 y trazar un histograma lo detectan; 2 = error identificado, prueba débil; 1 = error no detectado; 0 = nada.

**EX024 — Pruebas de invariantes.** *Objetivo:* redactar pruebas de verificación. *Entradas:* los invariantes del §4.4 y el simulador que encontrará en el capítulo 5 (Laboratorio 5), o uno propio. *Restricciones:* al menos cuatro invariantes como aserciones ejecutables. *Pasos:* (1) elija al menos cuatro invariantes del §4.4; (2) escriba cada uno como aserción ejecutable; (3) ejecute las aserciones con extracciones fijas; (4) introduzca deliberadamente un error, como eliminar el retardo de rearranque de un servicio, y muestre qué prueba falla. *Evidencia esperada:* código de las pruebas y salida antes y después del error. *Rúbrica:* 3 = cuatro o más invariantes significativos, el error detectado, explicación de por qué; 2 = las pruebas se ejecutan pero el error no se detecta; 1 = pruebas triviales; 0 = nada.

**EX025 — Métrica de detección relativa a la latencia.** *Objetivo:* definir una métrica de detección relevante para la consecuencia. *Entradas:* Laboratorio 4b y los valores de tiempo hasta el impacto del Laboratorio 3 (el primer impacto crítico a las 2 h para el SCADA del agua, 8 h para las telecomunicaciones). *Restricciones:* defina la métrica formalmente. *Pasos:* (1) defina «detectado antes del impacto» para un segmento con inicio conocido y tiempo hasta el impacto conocido; (2) calcúlela para el detector aleatorio, tratando cada paso temporal como 6 minutos y tomando un tiempo hasta el impacto de 2 h para cada segmento; (3) compárela con los valores de F1. *Evidencia esperada:* definición, fracción calculada, párrafo. *Rúbrica:* 3 = definición sólida y cálculo correcto a partir del índice de la primera alarma de cada segmento, con el contraste con el PA explicado; 2 = definición correcta, error de cálculo; 1 = vago; 0 = nada.

**EX026 — Plan del piloto.** *Objetivo:* diseñar un piloto de factibilidad. *Entradas:* su propio estudio de los ejercicios anteriores. *Restricciones:* al menos seis criterios de continuar o detener con umbrales; enunciado explícito de lo que no se estimará. *Pasos:* (1) enumere las preguntas de factibilidad del piloto; (2) fije umbrales declarados de antemano; (3) defina qué ocurre ante un «detener» en cada una; (4) defina quién puede participar y por qué los participantes del piloto quedan excluidos del estudio principal. *Evidencia esperada:* plan del piloto. *Rúbrica:* 3 = criterios medibles, solo de factibilidad, exclusión justificada, proceso de revisión registrado; 2 = un criterio vago; 1 = piloto usado para estimar el efecto; 0 = nada.

### Síntesis del capítulo

Antes de comparar métodos, asegúrese de que los números significan lo que afirman. Reproduzca las líneas de base con una tolerancia fijada de antemano, compruebe más de una salida y registre las convenciones: una matriz traspuesta produjo una respuesta plausible y errónea que coincidía en el único valor que comprobaría quien replica con prisa. Diagnostique las discrepancias por entradas, semántica, numérica y aleatoriedad. Verifique los simuladores con invariantes, pruebas unitarias y una implementación independiente antes de validarlos. Trate con suspicacia las líneas de base de detección que dependen del ajuste por punto, de divisiones aleatorias o de un solo banco de pruebas, y prefiera para la infraestructura la latencia relativa al tiempo hasta el impacto. Obtenga los parámetros con su incertidumbre y su procedencia. Use el piloto para ajustar procedimientos e instrumentos, nunca para estimar efectos.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 08

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Estudio principal y validación independiente

### Resultados de aprendizaje y conexión

Al terminar este capítulo, el estudiante será capaz de:

1. Diseñar un experimento de simulación pareado con números aleatorios comunes, un número justificado de extracciones y una cota oráculo.
2. Distinguir la incertidumbre de Monte Carlo de la incertidumbre de los parámetros y de la incertidumbre estructural, y decir cuál describe un intervalo reportado.
3. Interpretar un patrón mixto de hipótesis sustentadas y no sustentadas sin rescatar las favorables.
4. Diseñar y analizar un ejercicio de mesa a ciegas con operadores cuyo resultado sea la *consecuencia* de las elecciones realizadas, no la preferencia declarada.
5. Validar un modelo con evidencia de validez aparente, histórica, de condiciones extremas y operacional, y enunciar qué establece cada una.
6. Realizar una validación independiente en un segundo contexto seleccionado según criterios declarados de antemano y razonar sobre la transportabilidad.

El capítulo 4 verificó el simulador, reprodujo las líneas de base y puso a prueba los procedimientos en un piloto. Este capítulo ejecuta el estudio confirmatorio exactamente como se prerregistró y luego comprueba si su resultado se traslada a otro contexto.

### 5.1 Diseño del experimento de simulación

#### 5.1.1 Comparaciones pareadas y números aleatorios comunes

Cada extracción de la simulación muestrea un escenario: duraciones de restablecimiento para cada alimentador y reservas para cada servicio. Cada política se evalúa sobre *la misma* extracción. Este diseño de **números aleatorios comunes** elimina de la comparación la varianza compartida entre escenarios: la cantidad de interés es la diferencia por extracción entre dos políticas, cuya varianza es Var(A) + Var(B) − 2 Cov(A, B). El pareo ayuda exactamente en la medida en que las pérdidas de las dos políticas están correlacionadas positivamente entre extracciones. Cuando dos políticas se compensan —una protege el agua en una extracción en la que la otra protege las telecomunicaciones—, la correlación es débil y el pareo ayuda poco; el EX028 muestra que esto ocurre en Riverbend. Analice de todos modos las diferencias pareadas, porque son el estimando correcto, pero no suponga que el pareo garantiza precisión.

#### 5.1.2 ¿Cuántas extracciones?

El error estándar de Monte Carlo de una diferencia de medias es *s_d* / √*n*, donde *s_d* es la desviación estándar de las diferencias por extracción. En el piloto (capítulo 4), la desviación estándar de las diferencias DEP − CRITFLAG en Riverbend fue de unas 7 horas-servicio ponderadas, de modo que 500 extracciones dan una semiamplitud del 95 % de alrededor de 1,96 × 7 / √500 ≈ 0,6. El efecto mínimo de interés para H2 es el 10 % de la pérdida de CRITFLAG; como la pérdida de CRITFLAG en Riverbend es pequeña (alrededor de 4), ese umbral es de alrededor de 0,4, menor que la semiamplitud. Por eso el prerregistro fijó una **regla de decisión** de tres vías: H2 queda *sustentada* si el intervalo está completamente por debajo de −10 % de la pérdida media de CRITFLAG, *rechazada* si está completamente por encima de ese umbral (se descarta una reducción de al menos el 10 %), e *inconclusa* en otro caso, situación en la que el remedio previsto eran 2000 extracciones adicionales sin el oráculo. Registre el cálculo y la regla; no aumente *n* tras ver un resultado «casi significativo» fuera de la regla que redactó.

#### 5.1.3 Qué significa un intervalo de Monte Carlo

Un intervalo *bootstrap* o normal sobre extracciones de la simulación describe la **incertidumbre de Monte Carlo**: cuánto se movería la estimación con más extracciones *de este modelo con estas distribuciones de parámetros*. No dice nada sobre la **incertidumbre de los parámetros** (si las distribuciones obtenidas son correctas) ni sobre la **incertidumbre estructural** (si la forma del modelo es correcta). Con suficientes extracciones, cualquier diferencia se vuelve «estadísticamente significativa» dentro de un modelo. Reporte los intervalos de Monte Carlo para completar, pero base las afirmaciones en los tamaños del efecto respecto del efecto mínimo de interés, y aborde la incertidumbre de los parámetros y la estructural con análisis de sensibilidad y validación (§5.4 y capítulo 6).

### 5.2 El estudio confirmatorio de simulación

#### 5.2.1 El simulador

El simulador basado en eventos que sigue implementa el diseño prerregistrado. Un servicio no está disponible mientras su alimentador está desenergizado más allá de su reserva, o mientras un servicio del que depende no está disponible más allá de su reserva en el sitio; tras el restablecimiento hay un retardo de rearranque de una hora. Las cuadrillas toman el siguiente alimentador en el orden de la política en cuanto quedan libres. Las horas-cliente se calculan por alimentador. ORACLE enumera todos los órdenes posibles para cada extracción. Guarde el código como `lab5_mc.py`; el capítulo 6 lo importa.

```python
# Lab 5 - paired Monte Carlo comparison of restoration orderings (offline, standard library only)
# Event-based: a service is unavailable while its feeder is down beyond its buffer, or while a
# service it depends on is unavailable beyond its on-site buffer; restart lag applies after restoration.
import itertools, random, statistics

RIVERBEND = {
    "customers": {"F1": 9000, "F2": 1200, "F3": 2500, "F4": 6000},
    "crews": 1, "dur": (2, 6, 4),          # triangular(low, high, mode) hours per feeder
    "services": {  # name: (feeder, buffer triangular, weight, (depends_on, on-site hours) or None)
        "WATER": ("F3", (4, 14, 8), 4.0, None),
        "TEL":   ("F2", (4, 12, 8), 3.0, None),
        "HOSP":  ("F2", (8, 48, 24), 5.0, ("WATER", 4.0)),
    },
}
PORT_HALVARD = {
    "customers": {"H1": 7000, "H2": 3000, "H3": 1500, "H4": 4000, "H5": 800, "H6": 5000},
    "crews": 2, "dur": (1.5, 5, 3),
    "services": {
        "WATER2":   ("H4", (10, 30, 20), 4.0, None),
        "HOSP2":    ("H2", (48, 96, 72), 5.0, ("WATER2", 6.0)),
        "TEL2":     ("H3", (2, 6, 4), 3.0, None),
        "DISPATCH": ("H5", (1, 3, 2), 4.0, None),
    },
}
H, LAG = 72.0, 1.0

def draw(region, rng, buffer_scale=1.0):
    dur = {f: rng.triangular(*region["dur"]) for f in sorted(region["customers"])}
    buf = {s: rng.triangular(*v[1]) * buffer_scale for s, v in sorted(region["services"].items())}
    return dur, buf

def restore_times(order, dur, crews):
    free, done = [0.0] * crews, {}
    for f in order:
        i = min(range(crews), key=lambda k: free[k])
        free[i] += dur[f]
        done[f] = free[i]
    return done

def outage(region, done, buf):
    """Return {service: (start, end)} of unavailability, clipped to [0, H]."""
    out = {}
    def solve(s):
        if s in out:
            return out[s]
        feeder, _, _, dep = region["services"][s]
        ivs = []
        if buf[s] < done[feeder]:
            ivs.append((buf[s], done[feeder] + LAG))
        if dep:
            d = solve(dep[0])
            if d and d[0] + dep[1] < d[1]:
                ivs.append((d[0] + dep[1], d[1]))
        out[s] = (min(a for a, _ in ivs), max(b for _, b in ivs)) if ivs else None
        return out[s]
    for s in region["services"]:
        solve(s)
    return {s: (max(0.0, iv[0]), min(H, iv[1])) for s, iv in out.items() if iv}

def evaluate(region, order, dur, buf):
    done = restore_times(order, dur, region["crews"])
    loss = sum(region["services"][s][2] * (e - b) for s, (b, e) in outage(region, done, buf).items() if e > b)
    cust_h = sum(c * min(H, done[f]) for f, c in region["customers"].items()) / 1000.0
    return loss, cust_h

def silo(region):
    return sorted(region["customers"], key=lambda f: -region["customers"][f])

def critflag(region, believed_feeder=None):
    feeder_of = {s: v[0] for s, v in region["services"].items()}
    feeder_of.update(believed_feeder or {})   # the critical-customer list may also be out of date
    crit = set(feeder_of.values())
    return sorted(region["customers"], key=lambda f: (f not in crit, -region["customers"][f]))

def dep(region, believed_feeder=None):
    svc = dict(region["services"])
    if believed_feeder:                       # planner's (possibly wrong) dependency map
        for s, f in believed_feeder.items():
            svc[s] = (f,) + svc[s][1:]
    mean = {s: sum(v[1]) / 3 for s, v in svc.items()}
    tti = {}
    def t(s):
        if s not in tti:
            dep_ = svc[s][3]
            tti[s] = min(mean[s], t(dep_[0]) + dep_[1]) if dep_ else mean[s]
        return tti[s]
    key = {f: min([t(s) for s, v in svc.items() if v[0] == f], default=float("inf")) for f in region["customers"]}
    return sorted(region["customers"], key=lambda f: (key[f], -region["customers"][f]))

def experiment(region, n=500, seed=7, buffer_scale=1.0, believed_feeder=None, oracle=True):
    rng = random.Random(seed)
    policies = {"SILO": silo(region), "CRITFLAG": critflag(region, believed_feeder), "DEP": dep(region, believed_feeder)}
    res = {k: [] for k in list(policies) + (["ORACLE"] if oracle else [])}
    cust = {k: [] for k in policies}
    perms = list(itertools.permutations(region["customers"]))
    for _ in range(n):
        dur, buf = draw(region, rng, buffer_scale)
        for k, order in policies.items():
            l, c = evaluate(region, order, dur, buf)
            res[k].append(l)
            cust[k].append(c)
        if oracle:
            res["ORACLE"].append(min(evaluate(region, list(p), dur, buf)[0] for p in perms))
    return policies, res, cust

def boot_ci(x, seed=11, b=1000):
    rng = random.Random(seed)
    means = sorted(statistics.fmean(rng.choices(x, k=len(x))) for _ in range(b))
    return round(means[int(0.025 * b)], 2), round(means[int(0.975 * b)], 2)

if __name__ == "__main__":
    for name, region in (("Riverbend", RIVERBEND), ("Port Halvard", PORT_HALVARD)):
        policies, res, cust = experiment(region)
        print(f"== {name}: orders {policies}")
        for k, v in res.items():
            extra = f"  customer-hours(k) {statistics.fmean(cust[k]):7.1f}" if k in cust else ""
            print(f"  {k:8} weighted critical loss {statistics.fmean(v):6.2f}{extra}")
        d = [a - b for a, b in zip(res["DEP"], res["CRITFLAG"])]
        print("  DEP - CRITFLAG loss: mean", round(statistics.fmean(d), 2), "95% CI", boot_ci(d))
        r = statistics.fmean(cust["DEP"]) / statistics.fmean(cust["SILO"]) - 1
        r2 = statistics.fmean(cust["DEP"]) / statistics.fmean(cust["CRITFLAG"]) - 1
        print("  DEP customer-hours vs SILO:", f"{r:+.1%}", "| vs CRITFLAG:", f"{r2:+.1%}")
```

Salida esperada:

```text
== Riverbend: orders {'SILO': ['F1', 'F4', 'F3', 'F2'], 'CRITFLAG': ['F3', 'F2', 'F1', 'F4'], 'DEP': ['F2', 'F3', 'F1', 'F4']}
  SILO     weighted critical loss  52.75  customer-hours(k)   133.0
  CRITFLAG weighted critical loss   3.97  customer-hours(k)   222.5
  DEP      weighted critical loss   4.32  customer-hours(k)   227.6
  ORACLE   weighted critical loss   1.79
  DEP - CRITFLAG loss: mean 0.35 95% CI (-0.23, 0.97)
  DEP customer-hours vs SILO: +71.2% | vs CRITFLAG: +2.3%
== Port Halvard: orders {'SILO': ['H1', 'H6', 'H4', 'H2', 'H3', 'H5'], 'CRITFLAG': ['H4', 'H2', 'H3', 'H5', 'H1', 'H6'], 'DEP': ['H5', 'H3', 'H4', 'H2', 'H1', 'H6']}
  SILO     weighted critical loss  53.93  customer-hours(k)   103.2
  CRITFLAG weighted critical loss  31.63  customer-hours(k)   148.5
  DEP      weighted critical loss   9.61  customer-hours(k)   163.2
  ORACLE   weighted critical loss   9.61
  DEP - CRITFLAG loss: mean -22.01 95% CI (-22.4, -21.59)
  DEP customer-hours vs SILO: +58.2% | vs CRITFLAG: +9.9%
```

#### 5.2.2 Leer los resultados frente a las hipótesis

| Hipótesis | Riverbend (principal) | Port Halvard (validación independiente) | Veredicto |
|---|---|---|---|
| H1: DEP reduce la pérdida ≥ 20 % frente a SILO | 52,75 → 4,32 (−92 %) | 53,93 → 9,61 (−82 %) | Sustentada en ambas |
| H2: DEP reduce la pérdida ≥ 10 % frente a CRITFLAG | +0,35 (intervalo de MC del 95 %: −0,23 a 0,97), completamente por encima del umbral de −0,40: se descarta una reducción del 10 % | −22,01 de 31,63 (−70 %) | **No sustentada** en Riverbend; sustentada en Port Halvard |
| H3: la ganancia crece con la divergencia de órdenes | Los órdenes difieren en 2 posiciones (F2/F3 intercambiados) y, sin embargo, no hay ganancia | Los órdenes difieren en las 4 posiciones críticas; gran ganancia | En parte; Riverbend es una anomalía que hay que explicar (§5.2.3) |
| H4a: horas-cliente ≤ +15 % frente a SILO | +71,2 % | +58,2 % | **Falla** en ambas |
| H4b: horas-cliente ≤ +15 % frente a CRITFLAG | +2,3 % | +9,9 % | Se cumple en ambas |
| Brecha con ORACLE | DEP 4,32 frente a ORACLE 1,79 | DEP 9,61 = ORACLE 9,61 | DEP lejos del óptimo en Riverbend; óptimo en Port Halvard |

El resumen honesto es mixto. Un orden consciente de la criticidad, de *cualquier* tipo, protege los servicios críticos de manera drástica en comparación con el orden de clientes primero, con un gran costo en horas-cliente que la teoría de la programación había predicho (capítulo 3). Que los *tiempos* aporten valor sobre una lista de clientes críticos depende de la región: ninguno en Riverbend, mucho en Port Halvard. Se aplica la condición de fracaso prerregistrada «H2 falla en una región y se cumple en la otra»: acotar la afirmación a las condiciones que distinguen las regiones y poner a prueba el mecanismo.

#### 5.2.3 Explicar la anomalía de Riverbend sin rescatar la hipótesis

En Riverbend, DEP restablece F2 (telecomunicaciones y hospital) antes que F3 (agua), porque el tiempo esperado hasta el impacto de las telecomunicaciones (8 h) es ligeramente anterior al del agua (8,7 h). CRITFLAG restablece primero F3 porque tiene más clientes. Pero F3 protege *dos* servicios ponderados —el agua directamente y el hospital a través de su dependencia del agua—, mientras que restablecer primero F2 protege las telecomunicaciones y solo el camino eléctrico del hospital, que tiene una reserva larga. Una regla de tiempo hasta el impacto más temprano ignora los **pesos y la ramificación**; el capítulo 3 lo señaló como la debilidad conocida de la heurística. La pérdida mucho menor de ORACLE confirma que ninguna de las dos reglas está cerca del óptimo en Riverbend.

Esta explicación es *post hoc*. Es legítimo reportarla como una *hipótesis generada por el estudio confirmatorio*, que debe ponerse a prueba con datos nuevos (el capítulo 6 la pone a prueba en muchas regiones sintéticas); no es legítimo volver a ejecutar el estudio principal con una regla revisada y reportarlo como confirmatorio.

### 5.3 El ejercicio de mesa con operadores

#### 5.3.1 Por qué personas, y no solo modelos

Una regla de restablecimiento que los operadores no seguirán no tiene consecuencia alguna. El ejercicio de mesa pregunta si, con la visualización del tiempo efectivo hasta el impacto probada en el piloto del capítulo 4, operadores experimentados eligen órdenes que el modelo califica como de menor consecuencia, y por qué sí o por qué no.

#### 5.3.2 Diseño (sintético)

- **Participantes.** Doce operadores y gestores de emergencias (P01–P12) de tres empresas de servicios sintéticas, reclutados a través de los socios con consentimiento individual, ninguno del piloto. La participación fue voluntaria y sin pago más allá de los gastos; los gerentes no supieron quién participó.
- **Cruce intrasujeto.** Cada participante ordenó el restablecimiento en dos escenarios isomorfos —topología similar a Port Halvard con alimentadores renombrados y posiciones mezcladas—, una vez con una visualización convencional (número de clientes e indicadores de clientes críticos) y otra con la visualización del tiempo efectivo hasta el impacto añadida. El orden de las visualizaciones y de las versiones del escenario se contrabalanceó.
- **Cegamiento.** Los escenarios no contenían información sobre el resultado; en el piloto se revisaron las inyecciones en busca de pistas prematuras. Los analistas que puntuaron las justificaciones en texto libre no sabían qué condición de visualización las había producido.
- **Resultado.** El *orden elegido*, evaluado en el simulador sobre las mismas 500 extracciones que el estudio principal, de modo que el resultado es la consecuencia estimada por el modelo de la decisión del participante, no su preferencia declarada. Secundarios: tiempo de decisión; códigos de justificación.
- **Análisis.** Comparación pareada de si cada participante eligió el orden DEP con cada visualización; prueba exacta de McNemar sobre los pares discordantes; diferencias descriptivas de consecuencia; análisis temático de las justificaciones.

#### 5.3.3 Resultados (sintéticos)

| Visualización convencional → visualización del tiempo hasta el impacto | Participantes |
|---|---|
| No DEP → DEP | 7 |
| No DEP → no DEP | 5 |
| DEP → no DEP | 0 |
| DEP → DEP | 0 |

Los siete pares discordantes se movieron hacia DEP. Bajo la hipótesis nula de que un cambio en cualquiera de las dos direcciones es igualmente probable, la probabilidad exacta bilateral de siete o más cambios en una dirección de siete es 2 × 0,5⁷ = 0,0156. Con doce participantes de tres empresas de servicios, esto es evidencia de que la visualización *puede* cambiar las elecciones en un ejercicio de mesa, no una estimación de con qué frecuencia los operadores cambiarían su práctica. De los cinco que no adoptaron DEP, cuatro mantuvieron un orden similar a CRITFLAG. Los códigos de justificación (dos codificadores, desacuerdos resueltos y registrados) incluyeron: *expectativa institucional* («el consejo nos mide por clientes restablecidos»; 4 participantes), *desconfianza de las cifras de reserva* («he visto los registros de combustible de los hospitales: nunca coinciden con lo que dice el papel»; 3) y *logística de campo* («las cuadrillas ya están cerca del alimentador grande»; 3). El último tema identifica una variable que el modelo omite: el tiempo de desplazamiento entre alimentadores, que hace que las duraciones de restablecimiento dependan del orden.

#### 5.3.4 Lo que el ejercicio de mesa puede sustentar y lo que no

Sustenta: que la visualización es comprensible; que desplaza las elecciones del ejercicio de mesa hacia una menor consecuencia modelada; que los operadores plantean objeciones específicas que el modelo debe abordar. No puede sustentar: la adopción en el mundo real; los efectos bajo estrés, fatiga e información incompleta; ni los efectos en empresas de servicios distintas de las tres muestreadas. Los ejercicios de mesa son además actuaciones —los participantes saben que se les observa—, lo que empuja hacia respuestas que «parecen correctas».

### 5.4 Validar el modelo

Siguiendo a [Sargent (2013)](https://doi.org/10.1057/jos.2012.20), la validación es evidencia de que un modelo es adecuado *para su propósito previsto* —aquí, clasificar los órdenes de restablecimiento por la consecuencia sobre los servicios críticos—, no de que sea «verdadero».

| Tipo de validación | Evidencia del Estudio Cascada (sintética) | Qué establece | Qué no establece |
|---|---|---|---|
| Validez aparente | Doce participantes del ejercicio de mesa y dos ingenieros de los socios revisaron la estructura y las salidas del modelo | La estructura es reconocible para los profesionales; no hay omisiones flagrantes salvo el tiempo de desplazamiento | Que los parámetros sean correctos |
| Validación histórica | Interrupción por la tormenta de hielo de 2019 en Riverbend (todas las causas, registro sintético): el modelo, con los tiempos de restablecimiento de los alimentadores registrados, predijo pérdida de presión de agua a las 9 h y desvío hospitalario a las 13 h; los registros muestran 11 h y ninguno (el hospital recibió agua en camiones a las 10 h) | El momento de la falla del agua está en el rango correcto; el modelo omite la ayuda mutua (agua en camiones), una reserva humana | La exactitud para escenarios provocados por ciberataques; cualquier generalización a partir de un evento |
| Pruebas de condiciones extremas | Reservas nulas, reservas infinitas, un solo alimentador, un servicio | El comportamiento en los límites es sensato (invariantes del capítulo 4) | El comportamiento en el interior |
| Variabilidad de los parámetros | Escalado de reservas y conjuntos de pesos (capítulo 6) | Qué conclusiones dependen de qué parámetros | La adecuación estructural |
| Validez operacional | Acuerdo entre la clasificación de órdenes del modelo y la clasificación experta de los operadores en seis escenarios: coinciden 5 de 6 primeras opciones | El modelo clasifica los órdenes de forma muy parecida a los expertos en casos conocidos | Si alguno de los dos acierta en casos desconocidos |

La validación histórica produjo una corrección importante: el modelo trata las reservas como fijas, pero los operadores reales las amplían —agua en camiones, entregas de combustible, deslastre de carga en el hospital—. Un modelo sin estas reservas humanas es **conservador respecto de la consecuencia** y puede **exagerar el beneficio de reordenar**, porque ignora alternativas que los operadores usarían de todos modos. La tesis debe decirlo.

### 5.5 Validación independiente en un segundo contexto

#### 5.5.1 Selección según criterios declarados de antemano

Port Halvard se eligió *antes* de la simulación, según criterios derivados del mecanismo y registrados en la enmienda del prerregistro del capítulo 3: más alimentadores críticos (cuatro), divergencia entre el orden por reservas y el orden por clientes entre los alimentadores críticos, dos cuadrillas y reservas hospitalarias largas respaldadas por contratos de combustible. Un modelador distinto construyó la configuración de Port Halvard a partir de la documentación de los socios, sin acceso a los resultados de Riverbend. Estos pasos reducen, pero no eliminan, el riesgo de un contexto de validación que favorezca al método: los propios criterios se eligieron para dar al mecanismo la oportunidad de actuar. Eso es aceptable para una prueba del mecanismo, *no* para estimar con qué frecuencia ayuda el método en regiones reales. El capítulo 6 aborda la segunda pregunta con muchas regiones generadas aleatoriamente.

#### 5.5.2 Transportabilidad

Un resultado se transporta de un contexto a otro cuando la estructura causal pertinente es compartida y las diferencias se miden. [Pearl y Bareinboim (2014)](https://doi.org/10.1214/14-STS486) formalizan cuándo los hallazgos experimentales pueden transportarse entre poblaciones. De manera informal, para el Estudio Cascada: el mecanismo (reservas, restablecimiento secuencial, consecuencia ponderada) es compartido; los *moderadores* que difieren —número de alimentadores críticos, divergencia de órdenes, número de cuadrillas, duración de las reservas— deben medirse en cualquier región de destino antes de aplicar el resultado. Una empresa de servicios que conoce estas cuatro cosas sobre sí misma puede estimar si es probable que DEP supere a su lista actual; una que no las conoce, no puede.

### 5.6 Reportar el estudio principal

Reporte, como mínimo: el prerregistro y todas las enmiendas con sus fechas; la bitácora de desviaciones; cada hipótesis con su veredicto, incluidos los fracasos; los tamaños del efecto respecto de los efectos mínimos de interés; los intervalos de Monte Carlo etiquetados como tales; las brechas con ORACLE; el diseño del ejercicio de mesa, el consentimiento, el abandono y los resultados con pruebas exactas y temas cualitativos; cada tipo de validación con lo que establece; y la configuración de las dos regiones *con el nivel de detalle que permitan los niveles de protección de la información* (capítulo 7). Siga una estructura de reporte reconocida para estudios de simulación cuando exista una en la publicación de destino, y para el ejercicio de mesa siga las expectativas de transparencia de la investigación con seres humanos de su campo.

### 5.7 Errores habituales y límites

- Analizar por separado las medias de dos políticas en lugar de las diferencias pareadas.
- Aumentar el número de extracciones hasta que una diferencia sea «significativa».
- Presentar un intervalo de Monte Carlo como incertidumbre sobre el mundo.
- Volver a ejecutar el estudio confirmatorio con una regla revisada tras ver los resultados y llamarlo confirmatorio.
- Elegir un contexto de validación porque el método funcionará bien en él, sin decirlo.
- Medir las preferencias declaradas de los operadores en lugar de las consecuencias de sus elecciones.
- Tratar la validez aparente como validación de los parámetros.

- Leer el fracaso de H2 en Riverbend como una razón para revisar DEP y volver a ejecutar el estudio principal con el mismo prerregistro.
- Reportar un desplazamiento estadísticamente significativo en el ejercicio de mesa como evidencia de adopción, cuando doce participantes de tres empresas de servicios solo muestran que una visualización puede cambiar las elecciones.
- Tratar un único evento histórico, como la tormenta de hielo de 2019, como validación para escenarios provocados por ciberataques.
- Omitir la brecha con ORACLE, que muestra lo lejos que está cualquier regla del mejor orden.

### Ejercicios — capítulo 5

**EX027 — Ejecutar e interpretar el estudio principal.** *Objetivo:* reproducir e interpretar el Laboratorio 5. *Entradas:* el código del §5.2.1. *Restricciones:* sin conexión; registre la salida exacta. *Pasos:* (1) ejecute el laboratorio; (2) complete la tabla de hipótesis del §5.2.2 a partir de su salida; (3) calcule el cambio relativo de DEP frente a CRITFLAG en cada región; (4) redacte un párrafo de resultados de 150 palabras que un revisor hostil aceptaría. *Evidencia esperada:* salida, tabla, párrafo. *Rúbrica:* 3 = salida exacta, H2 reportada como fallida en Riverbend y sustentada en Port Halvard, fracaso de H4a reportado, sin rescate; 2 = números correctos, el párrafo exagera; 1 = errores; 0 = no se ejecutó.

**EX028 — Pareado frente a no pareado.** *Objetivo:* ver por qué importan los números aleatorios comunes. *Entradas:* Laboratorio 5. *Restricciones:* sin conexión. *Pasos:* (1) para Riverbend, calcule la desviación estándar de las pérdidas de DEP, de las de CRITFLAG y de las diferencias por extracción; (2) calcule un intervalo no pareado del 95 % para la diferencia de medias con la aproximación normal; (3) compárelo con el intervalo pareado; (4) explique la diferencia en 100 palabras. *Evidencia esperada:* tres desviaciones estándar, dos intervalos, explicación. *Rúbrica:* 3 = DE de alrededor de 6,36 (DEP), 4,57 (CRITFLAG) y 6,79 (diferencias); intervalo no pareado de alrededor de −0,34 a 1,04 frente al pareado de −0,24 a 0,95; explica que el pareo ayudó solo modestamente porque las pérdidas de las políticas están débilmente correlacionadas —se compensan en cuanto a qué servicio falla en una extracción dada— y que la DE de las diferencias puede superar la DE de cada política sin dejar de ser inferior a √(Var A + Var B); 2 = números correctos, la explicación supone que el pareo siempre reduce la varianza; 1 = error; 0 = nada.

**EX029 — Taxonomía de la incertidumbre.** *Objetivo:* clasificar la incertidumbre. *Entradas:* cinco enunciados: (a) «con 5000 extracciones el intervalo se estrecharía»; (b) «el combustible del hospital puede ser menor de lo que dijo el director de instalaciones»; (c) «el tiempo de desplazamiento entre alimentadores no está modelado»; (d) «los pesos reflejan los valores de un solo panel»; (e) «las reservas pueden no ser triangulares». *Restricciones:* clasifique cada uno como incertidumbre de Monte Carlo, de parámetros, estructural o de valores y nombre el método que la aborda. *Pasos:* (1) clasifique cada enunciado; (2) justifique la clase en una oración; (3) nombre el método que reduce o expone esa incertidumbre. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (a) Monte Carlo, (b) parámetros, (c) estructural, (d) valores, (e) parámetros o estructural con justificación, con métodos adecuados; 2 = un error; 1 = dos o más; 0 = nada.

**EX030 — Crítica del diseño del ejercicio de mesa.** *Objetivo:* reforzar un diseño con seres humanos. *Entradas:* §5.3.2. *Restricciones:* proponga al menos cinco mejoras dentro de los límites éticos y prácticos. *Pasos:* (1) identifique las amenazas —características de la demanda, muestra pequeña, tres empresas de servicios, ausencia de presión de tiempo, reconocimiento de escenarios isomorfos—; (2) proponga un cambio de diseño para cada una; (3) indique lo que cuesta cada cambio. *Evidencia esperada:* tabla. *Rúbrica:* 3 = cinco o más amenazas reales con cambios factibles y costos honestos; 2 = tres o cuatro; 1 = genérico; 0 = nada.

**EX031 — Matriz de evidencia de validación.** *Objetivo:* planificar la validación de su propio modelo. *Entradas:* un modelo de su investigación o el del Estudio Cascada. *Restricciones:* al menos cuatro tipos de validación; para cada uno, la evidencia, lo que establece y lo que no. *Pasos:* (1) elija al menos cuatro tipos de validación del §5.4; (2) para cada uno, indique la evidencia que reuniría; (3) indique lo que esa evidencia establece y lo que no; (4) identifique qué validación sería más perjudicial para su afirmación si fallara. *Evidencia esperada:* matriz y párrafo. *Rúbrica:* 3 = tipos bien elegidos, límites honestos, prueba más perjudicial identificada y planificada pronto; 2 = límites pobres; 1 = solo validez aparente; 0 = nada.

**EX032 — Memorando de transportabilidad.** *Objetivo:* asesorar a una tercera empresa de servicios. *Entradas:* una empresa de servicios sintética con cinco alimentadores, tres de ellos con servicios críticos cuyo orden por reservas coincide con su orden por clientes, y una cuadrilla. *Restricciones:* 300 palabras; use los moderadores del §5.5.2. *Pasos:* (1) mida los cuatro moderadores para esta empresa de servicios; (2) prediga la ganancia de DEP sobre CRITFLAG; (3) indique qué datos necesitaría para cambiar su predicción. *Evidencia esperada:* memorando. *Rúbrica:* 3 = predice ninguna ganancia porque los órdenes coinciden, explica los moderadores y observa que los pesos o la ramificación podrían seguir importando; 2 = predicción correcta, razonamiento pobre; 1 = predice una ganancia; 0 = nada.

### Síntesis del capítulo

El estudio principal comparó cuatro órdenes sobre extracciones pareadas con una cota oráculo. El orden consciente de la criticidad, de cualquier tipo, protegió los servicios críticos de manera drástica en comparación con el restablecimiento de clientes primero y costó muchas más horas-cliente que el margen declarado de antemano: una compensación para las políticas, no una ganancia gratuita. La información de tiempos no añadió nada sobre una lista de clientes críticos en Riverbend y añadió mucho en Port Halvard; la explicación *post hoc* (pesos y ramificación ignorados por una regla de tiempo más temprano) es una hipótesis nueva, no un rescate. Un ejercicio de mesa a ciegas mostró que una visualización del tiempo hasta el impacto puede desplazar las elecciones de los operadores hacia una menor consecuencia modelada y sacó a la luz variables omitidas, como el tiempo de desplazamiento de las cuadrillas. La validación estableció que el modelo es adecuado para clasificar órdenes en casos conocidos y que es conservador porque omite las reservas humanas. Los intervalos de Monte Carlo describieron solo el ruido de la simulación; la incertidumbre de los parámetros, la estructural y la de valores quedan para el capítulo 6.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 08

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Crítica entre pares y revisión

### Resultados de aprendizaje y conexión

Al terminar este capítulo, el estudiante será capaz de:

1. Organizar la crítica adversarial de la propia tesis —*red team* interno, revisión externa estructurada y colaboración adversarial— y registrarla.
2. Detectar la circularidad modelo-política y ponerla a prueba con un desajuste deliberado del modelo.
3. Cartografiar las condiciones de contorno con análisis de sensibilidad y con muchos contextos generados, reconociendo que el generador es en sí mismo un modelo.
4. Distinguir una revisión confirmatoria de una exploratoria y etiquetar cada una.
5. Redactar resultados negativos y acotados de modo que sean útiles para otros.
6. Realizar una revisión de doble uso de los hallazgos de investigación y decidir qué publicar, generalizar, aplazar o restringir.
7. Redactar una respuesta a los revisores que cambie las afirmaciones en lugar de defenderlas.

El capítulo 5 produjo un resultado mixto: un fuerte beneficio frente al orden de clientes primero, una compensación que no cumplió su margen, ningún beneficio frente a las listas de indicadores críticos en una región y un gran beneficio en otra. En este capítulo la tesis se gana sus afirmaciones intentando destruirlas.

### 6.1 La crítica como método

La revisión por pares en el momento de la publicación llega demasiado tarde y es demasiado superficial para ser el principal control de calidad de un proyecto doctoral. Integre la crítica en el proyecto:

- **Red team interno.** Antes del envío, se pide a un colega que no trabajó en el estudio que rompa la afirmación principal, con acceso al código, a los datos y al prerregistro. Su informe se responde por escrito.
- **Revisión externa estructurada.** Los socios y expertos del dominio revisan la estructura del modelo y las afirmaciones con un formulario que pide la objeción *más fuerte*, no una impresión general.
- **Colaboración adversarial.** Cuando un investigador creíble sostiene una opinión opuesta (por ejemplo, que la priorización basada en la topología es suficiente), diseñe una prueba conjunta cuyos resultados, según acuerdan ambas partes de antemano, les harían cambiar de opinión.
- **Pre-mortem.** Imagine que la tesis fue rechazada en la defensa; escriba las razones del examinador. Luego ponga a prueba cada razón.

Toda la crítica y las respuestas pasan al registro de revisiones de la tesis. Los examinadores confían en un trabajo cuyas debilidades han sido atacadas de forma visible.

### 6.2 El informe del red team sobre el Estudio Cascada (sintético)

Un *red team* interno produjo cinco objeciones principales:

1. **Circularidad.** «DEP se calcula a partir de las reservas y del mapa de dependencias del propio modelo y luego se evalúa en el mismo modelo. Es lógico que salga bien. En la realidad, el mapa del planificador está equivocado».
2. **Artefacto de reservas cortas.** «Las reservas de Riverbend son cortas en relación con los tiempos de restablecimiento. Con contratos de combustible realistas, nada de lo que se haga importa».
3. **Selección del contexto.** «Port Halvard se eligió para que el mecanismo actuara. Dos regiones, una elegida para el método, no pueden estimar con qué frecuencia ayuda DEP».
4. **Debilidad de la heurística.** «Su propio oráculo muestra que DEP está lejos del óptimo en Riverbend. ¿Por qué debería alguien adoptar una regla que usted sabe que es subóptima?».
5. **Doble uso.** «Ha mostrado que la pérdida de servicios críticos depende de qué alimentador se restablece primero y de si el mapa del planificador es correcto. Eso le dice a un adversario qué atacar: los datos de prioridad de restablecimiento».

Cada objeción es una hipótesis sobre el resultado. El resto del capítulo las pone a prueba.

### 6.3 Actividad práctica: condiciones de contorno, desajuste y muchas regiones

El laboratorio importa el simulador del Laboratorio 5 (guárdelo como `lab5_mc.py` en la misma carpeta).

```python
# Lab 6 - boundary conditions, model mismatch and many synthetic regions (offline)
# Save Lab 5 as lab5_mc.py in the same folder first.
import random, statistics
import lab5_mc as m

def mean_gain(region, **kw):
    _, res, cust = m.experiment(region, n=300, oracle=False, **kw)
    return (statistics.fmean(res["DEP"]) - statistics.fmean(res["CRITFLAG"]),
            statistics.fmean(res["DEP"]) - statistics.fmean(res["SILO"]))

print("1) Riverbend buffer scaling: (DEP-CRITFLAG, DEP-SILO) mean loss")
for s in (0.5, 1.0, 2.0, 4.0):
    a, b = mean_gain(m.RIVERBEND, buffer_scale=s)
    print(f"   scale {s:3.1f}: {a:7.2f} {b:7.2f}")

print("2) Model mismatch: water plant truly on F1, planner believes F3")
true = {**m.RIVERBEND, "services": {**m.RIVERBEND["services"], "WATER": ("F1",) + m.RIVERBEND["services"]["WATER"][1:]}}
_, res, _ = m.experiment(true, n=300, oracle=False, believed_feeder={"WATER": "F3"})
print("   mean loss SILO %.2f CRITFLAG %.2f DEP %.2f" % tuple(statistics.fmean(res[k]) for k in ("SILO", "CRITFLAG", "DEP")))

print("3) 200 random synthetic regions: gain of DEP over CRITFLAG vs rank divergence")
def random_region(rng):
    feeders = [f"G{i}" for i in range(1, 6)]
    cust = {f: rng.choice([500, 1000, 2000, 4000, 8000]) for f in feeders}
    crit = rng.sample(feeders, 3)
    services = {}
    for i, f in enumerate(crit):
        lo = rng.choice([1, 4, 12, 36])
        services[f"S{i}"] = (f, (lo, lo * 3, lo * 2), rng.choice([3.0, 4.0, 5.0]), None)
    return {"customers": cust, "crews": 1, "dur": (2, 6, 4), "services": services}
def divergence(region):
    flag = [f for f in m.critflag(region) if f in {v[0] for v in region["services"].values()}]
    depo = [f for f in m.dep(region) if f in flag]
    return sum(1 for a, b in zip(flag, depo) if a != b)
rng = random.Random(2026)
rows = []
for _ in range(200):
    r = random_region(rng)
    _, res, _ = m.experiment(r, n=60, oracle=False)
    rows.append((divergence(r), statistics.fmean(res["DEP"]) - statistics.fmean(res["CRITFLAG"])))
for d in sorted({d for d, _ in rows}):
    g = [x for dd, x in rows if dd == d]
    print(f"   positions differing={d}: regions={len(g):3d} mean gain={statistics.fmean(g):7.2f} share DEP worse={sum(x > 0 for x in g)/len(g):.2f}")
```

Salida esperada:

```text
1) Riverbend buffer scaling: (DEP-CRITFLAG, DEP-SILO) mean loss
   scale 0.5:    6.10  -86.14
   scale 1.0:    0.38  -47.57
   scale 2.0:    0.02   -7.25
   scale 4.0:    0.00    0.00
2) Model mismatch: water plant truly on F1, planner believes F3
   mean loss SILO 29.41 CRITFLAG 26.21 DEP 22.29
3) 200 random synthetic regions: gain of DEP over CRITFLAG vs rank divergence
   positions differing=0: regions= 69 mean gain=   0.00 share DEP worse=0.00
   positions differing=2: regions= 77 mean gain= -11.21 share DEP worse=0.01
   positions differing=3: regions= 54 mean gain= -23.97 share DEP worse=0.00
```

#### 6.3.1 Objeción 1: circularidad

En la parte 2, la planta de agua real está en F1, pero tanto la lista de clientes críticos como el planificador DEP creen que está en F3. Todas las políticas conscientes de la criticidad se degradan bruscamente: DEP de 4,32 a 22,29, CRITFLAG de 3,97 a 26,21. SILO incluso mejora (52,75 → 29,41) porque restablece primero F1 por razones de clientes y, con ello, restablece casualmente el agua. La objeción queda **sostenida en una forma más fuerte de la que planteó el red team**: el valor de *cualquier* orden consciente de la criticidad depende de la exactitud del mapa de dependencias. La revisión consiste en convertir la exactitud del mapa en una condición previa enunciada de la afirmación, añadir al método un procedimiento de auditoría del mapa y recomendar medir el error del mapa en cualquier aplicación de campo. Esto convierte una debilidad en una contribución: un requisito previo *medible* que las empresas de servicios pueden comprobar.

#### 6.3.2 Objeción 2: reservas cortas

La parte 1 escala todas las reservas. Al duplicarse las reservas, la ventaja de DEP sobre SILO cae de 47,57 a 7,25 horas-servicio ponderadas y desaparece con cuatro veces las reservas obtenidas. La objeción queda **sostenida como condición de contorno**: cuando las reservas superan holgadamente el tiempo total de restablecimiento, el orden no importa para los servicios críticos. Es exactamente la predicción del mecanismo en el capítulo 3, de modo que el resultado sustenta el mecanismo a la vez que limita el alcance de la afirmación. También revela algo que el red team no planteó: con la *mitad* de las reservas obtenidas, DEP es **peor** que CRITFLAG en 6,10; la debilidad heurística de la objeción 4 crece cuando las reservas son cortas, porque los errores sobre qué alimentador protege más servicios ponderados cuestan más.

#### 6.3.3 Objeción 3: selección del contexto

La parte 3 genera 200 regiones sintéticas con cinco alimentadores, tres servicios críticos, número de clientes, rangos de reservas y pesos aleatorios, y las clasifica según cuántas posiciones difieren entre los órdenes de CRITFLAG y DEP entre los alimentadores críticos. Donde los órdenes coinciden (69 regiones), la ganancia es exactamente cero, como debe ser. Donde difieren en dos posiciones (77 regiones), DEP reduce la pérdida media en 11,21 y es peor en alrededor del 1 % de las regiones; donde difieren en tres (54 regiones), en 23,97, sin ser nunca peor en esta muestra. El patrón predicho por H3 se mantiene en contextos que no se eligieron para el método.

Aun así, la objeción del red team queda **sostenida en parte**: el generador extrae el número de clientes y las reservas de forma independiente, y ese supuesto fija la frecuencia con que se produce la divergencia. Las regiones reales pueden tener correlaciones en cualquiera de las dos direcciones. Si los alimentadores grandes tienden a albergar instalaciones con reservas largas (grandes hospitales con grandes depósitos de combustible), el orden de CRITFLAG, de mayor a menor, va en sentido opuesto al orden de DEP, de la reserva más corta a la más larga, y la divergencia se vuelve *más* frecuente; si los alimentadores grandes tienden a albergar servicios de reserva corta (nodos de telecomunicaciones de zonas densas con baterías), los dos órdenes coinciden y la divergencia se vuelve menos frecuente. La frecuencia de la divergencia en regiones reales es una pregunta *empírica* que la tesis no puede responder con generadores sintéticos; la afirmación debe quedar condicionada a la divergencia, que una empresa de servicios puede medir sobre sí misma.

#### 6.3.4 Objeción 4: una heurística que se sabe subóptima

Sostenida. La cota del oráculo muestra que una regla que use los pesos y la ramificación —por ejemplo, ordenar los alimentadores por el valor ponderado de los servicios que protegen por hora de restablecimiento, teniendo en cuenta las dependencias— podría hacerlo mejor. El candidato puede desarrollar una regla así, pero debe etiquetarla como **exploratoria**: se diseñaría después de ver los resultados confirmatorios y debe confirmarse en configuraciones nuevas (regiones nuevas, semillas nuevas, prerregistrada) antes de hacer ninguna afirmación. La tesis puede presentarla legítimamente como el siguiente paso más prometedor.

### 6.4 Análisis de sensibilidad más allá de un factor cada vez

Variar un factor cada vez (las reservas, luego los pesos, luego las duraciones) pasa por alto las interacciones: el resultado del escalado de reservas muestra que la debilidad de la heurística interactúa con la duración de las reservas. El **análisis de sensibilidad global** varía a la vez todas las entradas inciertas y reparte la varianza de la salida entre las entradas y sus interacciones; [Saltelli et al. (2008)](https://doi.org/10.1002/9780470725184) es una introducción de referencia. Para una tesis, una secuencia práctica es: un cribado de un factor cada vez para encontrar las entradas que importan; un diseño estructurado (por ejemplo, un factorial sobre las pocas que importan); y luego, si los recursos lo permiten, índices basados en la varianza. Reporte de qué depende la conclusión, en los términos del lector: *«La ventaja de DEP sobre el orden por indicador crítico requiere divergencia entre los órdenes por reservas y por clientes, un mapa de dependencias sin errores de alimentador y reservas más cortas que alrededor del doble del tiempo de restablecimiento esperado»*.

La sensibilidad a los valores es distinta de la sensibilidad a los parámetros. Los pesos declarados de antemano codifican las prioridades de un panel. Vuelva a ejecutar con conjuntos de pesos alternativos —pesos iguales, pesos de un segundo panel, pesos que incluyan a los clientes ordinarios— y reporte si las conclusiones cambian (EX034).

### 6.5 Resultados negativos y acotación

El Estudio Cascada tiene ahora una afirmación acotada:

> En escenarios sintéticos de interrupción de la distribución que requieren restablecimiento manual secuencial, ordenar por el tiempo hasta el impacto de los servicios críticos reduce la pérdida ponderada de servicios críticos, declarada de antemano, respecto del orden por indicador de cliente crítico **solo** cuando los dos órdenes difieren, el mapa de dependencias es exacto y las reservas son cortas en relación con el tiempo de restablecimiento; donde se cumplen estas condiciones, la reducción es grande y las horas-cliente adicionales respecto del orden por indicadores quedan dentro de un margen del 15 %. Cualquier orden consciente de la criticidad protege los servicios críticos mucho mejor que el orden de clientes primero, con un costo en horas-cliente de aproximadamente el 60–70 % en las regiones estudiadas, que supera el margen declarado de antemano y es una compensación de política más que una mejora técnica. La heurística del tiempo hasta el impacto más temprano puede rendir menos que el orden por indicadores cuando las reservas son muy cortas, porque ignora los pesos y la ramificación.

Observe lo que hace la afirmación acotada: enuncia condiciones que una empresa de servicios puede medir; reporta el margen incumplido; reporta dónde pierde el método; y separa el hallazgo robusto (orden consciente de la criticidad frente a clientes primero) de la contribución condicional (tiempos frente a listas). Un resultado negativo sobre H2 en Riverbend no se oculta; es la evidencia que define el contorno.

**Publique los resultados negativos de forma útil.** Enuncie la hipótesis, el diseño, el tamaño del efecto con su intervalo y el efecto mínimo de interés que descarta. «Ninguna diferencia significativa» no sirve; «en Riverbend se descarta una reducción del 10 % o más respecto del orden por indicadores» sí sirve.

### 6.6 Revisión de doble uso de los hallazgos

Aplicando las tres preguntas del capítulo 1 (§1.4.3):

| Hallazgo | Ventaja para un adversario | Valor defensivo | Decisión |
|---|---|---|---|
| El orden consciente de la criticidad protege los servicios críticos; costo en horas-cliente | Despreciable: ampliamente conocido | Sustenta el debate de políticas sobre las prioridades de restablecimiento | Publicar |
| El valor depende de la exactitud del mapa de dependencias | Moderada: sugiere que corromper o robar los datos de prioridad de restablecimiento y las listas de clientes críticos podría amplificar un ataque | Alto: indica a las empresas de servicios que protejan la integridad y la confidencialidad de los datos de prioridad de restablecimiento y que auditen los mapas | Publicar a nivel general con la recomendación defensiva; sin ejemplos de cómo alterar esos datos |
| Regiones sintéticas, código y parámetros | Baja: lugares inventados | Alto: reproducibilidad | Publicar (capítulo 7, nivel T0) |
| Rangos de reservas y relaciones alimentador-instalación derivados de los socios | Alta: información para seleccionar objetivos | Bajo más allá del socio | Retener; describir solo rangos agregados |
| Justificaciones del ejercicio de mesa | Baja | Moderado | Publicar los temas sin identificadores de función y empresa de servicios |

La segunda fila ilustra un patrón recurrente en la investigación sobre infraestructura: un hallazgo de resiliencia suele ser también un hallazgo sobre la superficie de ataque. El contexto de amenazas pertinente es público —el [AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a) de CISA describe el preposicionamiento en las redes de TI de la infraestructura, donde suelen residir los datos de planificación—, de modo que la recomendación defensiva (protección de la integridad y auditoría de los datos de prioridad de restablecimiento) tiene un valor claro. Coordine con los socios y, cuando corresponda, con el organismo sectorial de intercambio de información pertinente antes de publicar (capítulo 8).

### 6.7 Responder a los revisores

Una buena carta de respuesta cita cada comentario, indica si se acepta, se acepta en parte o no se acepta, describe el cambio (con su ubicación) y, cuando no se acepta, aporta evidencia y no opinión. Sobre todo, **cambia las afirmaciones**, no solo la redacción. Compare:

- *Defensiva:* «Agradecemos al revisor. Port Halvard se seleccionó según criterios declarados de antemano, por lo que el sesgo de selección no es un problema».
- *Receptiva:* «Aceptado en parte. Port Halvard se seleccionó según criterios declarados de antemano y derivados del mecanismo, lo que lo convierte en una prueba justa del mecanismo, pero no en una estimación de con qué frecuencia ayuda DEP. Añadimos un análisis de 200 regiones (§6.3.3), acotamos la afirmación a las regiones con divergencia de órdenes y declaramos que la frecuencia de la divergencia en regiones reales es desconocida (Limitaciones, punto 4)».

### 6.8 Errores habituales y límites

- Tratar la revisión por pares como un obstáculo en lugar de como un método.
- Evaluar una política solo en el modelo usado para derivarla.
- Reportar solo la sensibilidad de un factor cada vez.
- Tratar un generador de contextos aleatorios como una muestra de la realidad.
- Presentar una revisión exploratoria como confirmatoria.
- Redactar los resultados negativos como «no significativos».
- Omitir la revisión de doble uso porque los resultados son «solo simulaciones».

- Aceptar una objeción del red team en su forma original sin comprobar si se sostiene una versión más fuerte, como ocurrió con la circularidad.
- Tratar una condición de contorno como una derrota y no como una predicción confirmada del mecanismo que acota la afirmación.
- Suponer que los supuestos de independencia de un generador de regiones aleatorias coinciden con las regiones reales, donde el número de clientes y las reservas pueden estar correlacionados.
- Redactar una carta de respuesta que agradece a los revisores y defiende la afirmación original en lugar de cambiarla donde la evidencia lo exige.
- Publicar rangos de reservas derivados de los socios porque parecen inofensivos en forma agregada.

### Ejercicios — capítulo 6

**EX033 — Informe del red team.** *Objetivo:* atacar su propia afirmación. *Entradas:* la afirmación del Estudio Cascada antes de acotarla (resumen del capítulo 5) o la suya. *Restricciones:* al menos cinco objeciones, cada una enunciada como hipótesis comprobable. *Pasos:* (1) redacte cada objeción; (2) diga qué evidencia la sostendría o la descartaría; (3) diseñe la prueba; (4) prediga el resultado antes de ejecutar nada. *Evidencia esperada:* informe. *Rúbrica:* 3 = objeciones específicas y comprobables, incluidas la circularidad y la selección del contexto, con predicciones registradas antes de las pruebas; 2 = una o dos no comprobables; 1 = genéricas; 0 = nada.

**EX034 — Sensibilidad a los pesos.** *Objetivo:* poner a prueba la sensibilidad a los valores. *Entradas:* Laboratorio 5 y Laboratorio 6. *Restricciones:* sin conexión. *Pasos:* (1) fije todos los pesos de los servicios en 1,0 en ambas regiones; (2) vuelva a ejecutar la comparación principal; (3) registre las pérdidas de DEP, CRITFLAG y SILO; (4) indique si cambia cada veredicto de la tabla de hipótesis; (5) explique por qué. *Evidencia esperada:* código modificado, salidas, párrafo. *Rúbrica:* 3 = salidas exactas, análisis correcto de los veredictos, explicación vinculada a la ramificación y los pesos; 2 = salidas correctas, explicación pobre; 1 = errores; 0 = no se ejecutó.

**EX035 — Experimento de error del mapa.** *Objetivo:* cuantificar la fragilidad ante errores del mapa. *Entradas:* Laboratorio 6, parte 2. *Restricciones:* sin conexión. *Pasos:* (1) repita el desajuste con la central de telecomunicaciones realmente en F4 mientras los planificadores creen que está en F2; (2) registre las pérdidas; (3) compárelas con la parte 2; (4) proponga un procedimiento de auditoría del mapa con un objetivo de exactitud medible. *Evidencia esperada:* salidas y procedimiento. *Rúbrica:* 3 = salidas correctas, comparación con el desajuste del agua, procedimiento de auditoría medible (verificación de campo por muestreo, tasa de exactitud, aprobación del responsable); 2 = procedimiento vago; 1 = no se ejecutó correctamente; 0 = nada.

**EX036 — Crítica del generador.** *Objetivo:* reconocer el generador como un modelo. *Entradas:* `random_region` del Laboratorio 6. *Restricciones:* proponga un cambio que codifique una correlación plausible del mundo real. *Pasos:* (1) modifique el generador para que los alimentadores más grandes tiendan a albergar servicios críticos con reservas más largas; (2) vuelva a ejecutar la parte 3; (3) compare la distribución de la divergencia y de las ganancias con la parte 3 original; (4) prediga, y luego compruebe, qué haría la correlación opuesta; (5) explique qué significa esto para la afirmación. *Evidencia esperada:* código, salida, párrafo. *Rúbrica:* 3 = correlación implementada con sensatez; el estudiante advierte que esta correlación hace que los órdenes de CRITFLAG y DEP vayan en sentidos opuestos, de modo que la divergencia se vuelve *más* frecuente (las regiones sin divergencia caen bruscamente), y explica que la correlación opuesta la haría menos frecuente, por lo que la afirmación debe seguir condicionada a la divergencia medida; 2 = implementación sólida, pero se interpreta mal la dirección del efecto; 1 = sin comparación; 0 = nada.

**EX037 — Decisión de doble uso.** *Objetivo:* decidir el tratamiento de publicación. *Entradas:* cuatro hallazgos de su propia investigación o: (a) una lista de empresas de agua cuyo SCADA es accesible a través del producto de acceso remoto de un proveedor específico; (b) la observación de que los productos de acceso remoto son un punto de entrada habitual en todos los sectores; (c) un método para estimar el tiempo hasta el impacto a partir de datos públicos de instalaciones; (d) las estimaciones del tiempo hasta el impacto para hospitales con nombre de una ciudad. *Restricciones:* las tres preguntas del §1.4.3. *Pasos:* (1) evalúe la ventaja de cada hallazgo; (2) evalúe el valor defensivo; (3) decida entre publicar, generalizar, aplazar y restringir; (4) indique a quién se debe notificar antes de la publicación. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (a) restringir y notificar mediante divulgación coordinada, (b) publicar, (c) publicar con cuidado, (d) retener o restringir, con razonamiento sólido; 2 = uno mal juzgado; 1 = dos o más; 0 = nada.

**EX038 — Carta de respuesta.** *Objetivo:* cambiar las afirmaciones en respuesta a la crítica. *Entradas:* las cinco objeciones del red team del §6.2. *Restricciones:* una respuesta por objeción; al menos dos deben llevar a una afirmación cambiada. *Pasos:* (1) cite cada objeción; (2) márquela como aceptada, aceptada en parte o no aceptada; (3) describa el cambio y su ubicación; (4) aporte evidencia para cualquier no aceptación. *Evidencia esperada:* carta de respuesta. *Rúbrica:* 3 = receptiva y no defensiva, afirmaciones cambiadas donde corresponde, trabajo exploratorio etiquetado; 2 = mayormente receptiva; 1 = defensiva; 0 = nada.

### Síntesis del capítulo

La crítica forma parte del método. Las objeciones del red team se convirtieron en hipótesis y pruebas. La circularidad se sostuvo en una forma más fuerte —toda política consciente de la criticidad depende de un mapa de dependencias exacto—, que se convirtió en una condición previa medible y en una recomendación defensiva. Las reservas cortas se confirmaron como una condición de contorno predicha por el mecanismo, y las reservas muy cortas expusieron la debilidad de la heurística. Un análisis de 200 regiones sustentó el mecanismo en contextos no elegidos para él, a la vez que recordó que un generador es un modelo. La afirmación acotada enuncia condiciones medibles, reporta el margen incumplido y separa el hallazgo robusto de la contribución condicional. La revisión de doble uso mostró que un hallazgo de resiliencia también puede ser un hallazgo sobre la superficie de ataque y decidió qué publicar y con qué nivel de detalle.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 08

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Síntesis de la tesis y archivo de reproducibilidad

### Resultados de aprendizaje y conexión

Al terminar este capítulo, el estudiante será capaz de:

1. Estructurar una tesis como un argumento en el que cada afirmación está vinculada a evidencia, garantía, alcance y limitación.
2. Decidir entre una monografía y una tesis por compendio de publicaciones e integrar cualquiera de las dos en un único argumento coherente.
3. Diseñar un archivo de reproducibilidad por niveles que publique tanto como sea lícito y seguro, bajo la protección de la información de infraestructura.
4. Distinguir los datos sintéticos inventados de los datos sintéticos calibrados con lugares reales, y evaluar el riesgo residual de divulgación.
5. Documentar modelos, conjuntos de datos y estudios de simulación con estructuras reconocidas.
6. Redactar una sección de limitaciones que informe en lugar de disculparse.

El capítulo 6 produjo la afirmación acotada. Este capítulo arma la tesis en torno a ella y construye el archivo que permite a otros comprobarla sin exponer la infraestructura que estudia.

### 7.1 La tesis como argumento

Una tesis no es un informe de todo lo realizado; es un argumento a favor de una contribución. Un andamiaje útil es el análisis de los argumentos de Toulmin ([Toulmin, 1958/2003](https://doi.org/10.1017/CBO9780511840005)): una **afirmación** sustentada por **datos** (evidencia) mediante una **garantía** (la razón por la que la evidencia sustenta la afirmación), con un **respaldo** para la garantía, un **cualificador** (con qué fuerza) y **refutaciones** (condiciones en las que la afirmación falla). Aplicado a la investigación sobre infraestructura:

| Elemento | Ejemplo del Estudio Cascada |
|---|---|
| Afirmación | El orden por tiempo hasta el impacto reduce la pérdida ponderada de servicios críticos respecto del orden por indicador crítico cuando los órdenes divergen, los mapas son exactos y las reservas son cortas. |
| Datos | Simulaciones pareadas de Riverbend y Port Halvard; análisis de 200 regiones; pruebas de error del mapa y de escalado de reservas. |
| Garantía | El simulador representa el agotamiento de las reservas y el restablecimiento secuencial de forma adecuada para clasificar órdenes. |
| Respaldo | Pruebas de verificación; reproducción de las líneas de base; validación histórica del tiempo del agua; validez operacional frente a clasificaciones expertas. |
| Cualificador | En regiones sintéticas, una sola clase de escenario (interrupciones de distribución que requieren restablecimiento manual secuencial), pesos declarados de antemano. |
| Refutaciones | Errores del mapa; reservas largas; conjuntos de pesos que favorecen la ramificación; reservas humanas y tiempo de desplazamiento omitidos; frecuencia de la divergencia en el mundo real desconocida. |

Cada capítulo de la tesis debe aportar un elemento identificable. Un capítulo que no aporta ninguno es candidato a apéndice.

### 7.2 Monografía o tesis por compendio de publicaciones

Una **monografía** presenta un único argumento integrado; una **tesis por compendio de publicaciones** reúne artículos con una introducción y una conclusión integradoras. Las tesis sobre infraestructura suelen mezclar géneros —un artículo de modelado, un estudio empírico de operadores, un análisis de políticas—, lo que se adapta bien a las tesis por compendio, pero los capítulos integradores deben hacer un trabajo real: enunciar la afirmación general, mostrar cómo aporta cada artículo datos o respaldo, conciliar las diferencias de alcance entre los artículos y presentar las limitaciones del conjunto. Las normas sobre formato, declaraciones de coautoría y publicación previa difieren entre instituciones; este itinerario educativo no otorga títulos y no puede asesorar sobre las normas de ninguna institución más allá de señalar que deben comprobarse pronto.

### 7.3 Estructura de la tesis del Estudio Cascada

1. **Introducción.** Problema, vacío, tipos de contribución, afirmación general y su alcance.
2. **Marco de referencia.** Definiciones, literatura sobre interdependencia y resiliencia, práctica de restablecimiento, teoría de la programación (capítulos 1–2 de este libro).
3. **Método.** Mecanismo, hipótesis, líneas de base, protocolo, ética y protección de la información (capítulo 3).
4. **Verificación y líneas de base.** Reproducciones, pruebas de verificación, obtención de parámetros y piloto (capítulo 4).
5. **Estudio principal y validación.** Simulaciones, ejercicio de mesa, validación, segunda región (capítulo 5).
6. **Crítica y contornos.** Pruebas del red team, sensibilidad, análisis de muchas regiones, afirmación acotada, revisión de doble uso (capítulo 6).
7. **Discusión.** Qué pueden hacer los profesionales y los responsables de las políticas con la afirmación acotada; qué sigue sin conocerse.
8. **Limitaciones.**
9. **Conclusión.**
10. **Apéndices.** Prerregistro y enmiendas, bitácora de desviaciones, listado de pruebas de verificación, protocolos de obtención, materiales del ejercicio de mesa, manifiesto del archivo.

### 7.4 El archivo de reproducibilidad

#### 7.4.1 Objetivos y restricciones

La reproducibilidad en este campo debe cumplir dos objetivos que tiran en direcciones opuestas: permitir que otros comprueben el trabajo y no publicar información que ayude a alguien a dañar la infraestructura o que identifique a personas. Los [principios FAIR](https://doi.org/10.1038/sdata.2016.18) —localizable, accesible, interoperable, reutilizable— ayudan aquí porque FAIR no significa abierto: los datos pueden ser localizables y tener sus condiciones de acceso claramente descritas mientras el acceso en sí está controlado.

#### 7.4.2 Niveles de publicación

| Nivel | Quién puede acceder | Qué contiene en el Estudio Cascada | Condiciones |
|---|---|---|---|
| T0 Público | Cualquier persona | Código del simulador, pruebas, definiciones de regiones sintéticas, semillas, salidas, scripts de análisis, materiales del ejercicio de mesa sin identificadores | Licencia indicada; identificador persistente |
| T1 Registrado | Investigadores que se registran y aceptan las condiciones | Rangos de obtención agregados sin la identidad de los socios; conjuntos de escenarios ampliados | Las condiciones de uso prohíben la reidentificación y la selección de objetivos |
| T2 Controlado | Investigadores aprobados bajo un acuerdo y, cuando corresponda, con aprobación ética | Transcripciones seudonimizadas del ejercicio de mesa y justificaciones codificadas | Acuerdo de uso de datos; entorno seguro; auditoría |
| T3 Retenido | No se publica; solo se describe | Relaciones alimentador-instalación derivadas de los socios, inventarios reales de reservas, mapas | Su existencia y naturaleza se describen en la tesis para que los examinadores sepan qué falta y por qué |

El **manifiesto** del archivo enumera cada archivo con un *hash* criptográfico y su nivel, de modo que cualquiera puede verificar que los archivos públicos son los que se usaron, y los examinadores pueden ver qué existe en los niveles superiores.

#### 7.4.3 Actividad práctica: construir un manifiesto por niveles

```python
# Lab 7 - build a tiered reproducibility manifest for a synthetic thesis archive (offline)
import hashlib, json, os, tempfile
files = {
    "code/lab5_mc.py": b"# simulation code\n",
    "data/synthetic_riverbend_params.csv": b"feeder,customers\nF1,9000\nF2,1200\nF3,2500\nF4,6000\n",
    "data/partner_feeder_map.csv": b"feeder,substation,gps\nF2,SUB-7,redacted\n",
    "results/mc_summary.json": b'{"mean_dloss": -46.86}\n',
    "docs/operator_interview_notes.txt": b"P03: we restore by customer count\n",
}
RULES = [  # first matching rule wins; order matters
    ("partner_", "T3-withheld: partner-owned infrastructure detail; describe, do not release"),
    ("interview", "T2-controlled: human-subjects data; release only under approved access agreement"),
    ("synthetic_", "T0-public"),
    ("code/", "T0-public"),
    ("results/", "T0-public"),
]
def tier(path):
    for key, label in RULES:
        if key in path:
            return label
    return "UNCLASSIFIED: stop and review"
with tempfile.TemporaryDirectory() as root:
    manifest = []
    for rel, content in sorted(files.items()):
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(content)
        manifest.append({"path": rel, "sha256": hashlib.sha256(content).hexdigest()[:16], "tier": tier(rel)})
    print(json.dumps(manifest, indent=1))
    print("public files:", sum(m["tier"].startswith("T0") for m in manifest), "of", len(manifest))
```

Salida esperada:

```text
[
 {
  "path": "code/lab5_mc.py",
  "sha256": "e9db014f8aeb90da",
  "tier": "T0-public"
 },
 {
  "path": "data/partner_feeder_map.csv",
  "sha256": "160cefe894e75af9",
  "tier": "T3-withheld: partner-owned infrastructure detail; describe, do not release"
 },
 {
  "path": "data/synthetic_riverbend_params.csv",
  "sha256": "66bd4b5c8f37d273",
  "tier": "T0-public"
 },
 {
  "path": "docs/operator_interview_notes.txt",
  "sha256": "35c6e20265ce92c5",
  "tier": "T2-controlled: human-subjects data; release only under approved access agreement"
 },
 {
  "path": "results/mc_summary.json",
  "sha256": "7bde71d2f02e64ad",
  "tier": "T0-public"
 }
]
public files: 3 of 5
```

Dos decisiones de diseño merecen atención. Primero, las reglas están **ordenadas** y gana la primera coincidencia: si la regla «synthetic» se colocara antes que la regla «partner», un archivo llamado `synthetic_partner_feeders.csv` se publicaría. Ordene primero las reglas más restrictivas. Segundo, un archivo sin coincidencia devuelve **"UNCLASSIFIED: stop and review"** en lugar de un nivel predeterminado; un flujo de publicación debe fallar de forma cerrada. Los flujos reales también analizarían el *contenido* de los archivos (coordenadas, identificadores de activos, nombres), no solo las rutas.

### 7.5 Datos sintéticos: inventados frente a calibrados

Las regiones de este libro son **inventadas**: sus números se eligieron para enseñar y no corresponden a ningún lugar. Una tesis basada en un socio real produciría más probablemente datos sintéticos **calibrados**, generados para reproducir propiedades estadísticas de datos reales. La calibración preserva el valor para la investigación y también preserva cierto riesgo de divulgación: si la región real tiene un único hospital en un alimentador pequeño con una planta de agua de reserva corta, una región sintética calibrada que preserve esas relaciones todavía puede señalarla. Evalúe explícitamente el riesgo residual: ¿podría una persona informada hacer corresponder la configuración sintética con una real? ¿Revelaría esa correspondencia algo que no sea ya público? Generalizar (rangos en lugar de valores), perturbar y mezclar varias configuraciones reales reducen el riesgo; la evaluación y las medidas elegidas pertenecen a la documentación del archivo.

### 7.6 Documentar modelos, datos y estudios

- **Modelos.** Para los componentes basados en agentes, el protocolo ODD —visión general, conceptos de diseño, detalles— da una estructura estándar ([Grimm et al., 2006](https://doi.org/10.1016/j.ecolmodel.2006.04.023)). Para cualquier simulador, documente el propósito, las entidades y las variables de estado, los procesos y su programación, las entradas y sus fuentes, las pruebas de verificación y las limitaciones conocidas.
- **Conjuntos de datos.** Las fichas de datos (*datasheets*) registran la motivación, la composición, el proceso de recopilación, el preprocesamiento, los usos, la distribución y el mantenimiento ([Gebru et al., 2021](https://doi.org/10.1145/3458723)).
- **Componentes aprendidos.** Si el estudio incluye un modelo aprendido (por ejemplo, un detector), una ficha de modelo (*model card*) registra el uso previsto, las condiciones de evaluación y las limitaciones ([Mitchell et al., 2019](https://doi.org/10.1145/3287560.3287596)).
- **Cómputo.** Fije las versiones del lenguaje y de las bibliotecas, registre las semillas, proporcione una única orden que regenere cada tabla y cada figura, e incluya las pruebas de verificación. [Sandve et al. (2013)](https://doi.org/10.1371/journal.pcbi.1003285) dan diez reglas prácticas.

### 7.7 Redactar las limitaciones

Una sección de limitaciones forma parte del argumento: enuncia las condiciones de refutación y su dirección probable. Las secciones de limitaciones débiles enumeran salvedades genéricas («se necesita más investigación»). Las fuertes dicen, para cada limitación, *qué* es, *cómo* podría cambiar el resultado y *en qué dirección*, y *qué estudio* la resolvería. Para el Estudio Cascada:

| Limitación | Efecto posible | Dirección | Estudio que la resolvería |
|---|---|---|---|
| Se omiten las reservas humanas (agua en camiones, entregas de combustible, deslastre de carga) | El modelo exagera la consecuencia de todos los órdenes y el beneficio de reordenar | Hacia un beneficio menor | Modelar la ampliación de las reservas como condicionada a las telecomunicaciones y las carreteras; validar frente a registros posteriores a la acción |
| Se omite el tiempo de desplazamiento entre alimentadores | Los órdenes que saltan entre alimentadores distantes cuestan más de lo modelado | Hacia un beneficio menor de DEP cuando los alimentadores críticos están dispersos | Añadir una matriz de tiempos de desplazamiento; volver a ejecutar |
| Solo regiones sintéticas | Frecuencia de la divergencia en regiones reales desconocida | Desconocida | Encuesta a empresas de servicios que mida la divergencia, con protección T3 |
| Pesos de un solo panel | Los veredictos cambian con los pesos (EX034) | Cualquiera | Varios paneles; reportar los veredictos por conjunto de pesos |
| Muestra del ejercicio de mesa de 12 personas de 3 empresas de servicios | Evidencia de adopción débil | Hacia una exageración de la adoptabilidad | Estudio más amplio y estratificado; piloto de campo durante ejercicios |
| Clase de escenario cibernético limitada a interrupciones de distribución que requieren restablecimiento manual | No cubre ataques contra las herramientas de restablecimiento ni contra los datos de prioridad | Desconocida | Familia de escenarios que incluya ataques a la integridad de los datos de planificación (motivada por el §6.6) |

### 7.8 Ejemplo resuelto: armar el archivo

El primer plan de archivo del candidato colocaba todo en T2 «por seguridad». El comité lo rechazó: la restricción excesiva impide la verificación y no es segura, solo hace el trabajo imposible de auditar. El plan revisado usó la tabla de niveles del §7.4.2, publicó todo el código y las configuraciones sintéticas en T0 con una única orden de regeneración, colocó las transcripciones del ejercicio de mesa en T2 según las condiciones de consentimiento que firmaron los participantes, y registró el material T3 de los socios en una descripción que indicaba a los examinadores exactamente qué análisis dependían de él: ninguno de los resultados confirmatorios, por diseño, porque el estudio usó regiones inventadas para todas las afirmaciones públicas y usó los datos de los socios solo para los rangos de obtención y la validez aparente. Esa decisión de diseño, tomada en el capítulo 1, es la que hizo posible un archivo en gran parte público.

### 7.9 Errores habituales y límites

- Redactar la tesis como un cuaderno de laboratorio cronológico en lugar de como un argumento.
- Restringirlo todo, o publicarlo todo, en lugar de establecer niveles.
- Equiparar FAIR con abierto.
- Tratar los datos sintéticos calibrados como automáticamente seguros.
- Scripts de publicación que fallan de forma abierta.
- Secciones de limitaciones sin dirección ni estudios que las resuelvan.

- Colocar todo en un nivel restrictivo por seguridad, lo que impide la verificación y hace el trabajo imposible de auditar en lugar de seguro.
- Ordenar las reglas de publicación de modo que un patrón permisivo como synthetic coincida antes que uno restrictivo como partner.
- Clasificar los archivos solo por su nombre, sin analizar su contenido en busca de coordenadas, identificadores de activos o nombres.
- Dejar que los resultados confirmatorios dependan de material retenido de los socios, de modo que los examinadores no puedan comprobarlos.
- Omitir una única orden que regenere cada tabla y cada figura a partir de los archivos públicos.

### Ejercicios — capítulo 7

**EX039 — Mapa del argumento.** *Objetivo:* exponer el argumento de la tesis. *Entradas:* la afirmación acotada del §6.5. *Restricciones:* use los seis elementos de Toulmin. *Pasos:* (1) cartografíe la afirmación; (2) marque qué capítulo de la tesis aporta cada elemento; (3) identifique la garantía más débil y la evidencia que la reforzaría. *Evidencia esperada:* mapa y párrafo. *Rúbrica:* 3 = mapa completo, garantía más débil correctamente identificada (adecuación del modelo para regiones reales, o reservas humanas omitidas) con un estudio específico para reforzarla; 2 = un elemento pobre; 1 = solo afirmación y datos; 0 = nada.

**EX040 — Asignación de niveles.** *Objetivo:* asignar niveles a un archivo realista. *Entradas:* diez artefactos: código del simulador; pruebas de verificación; configuración de Riverbend; formularios de obtención con nombres de socios; rangos de obtención agregados; audio del ejercicio de mesa; justificaciones codificadas; formularios de consentimiento; un procedimiento de restablecimiento de un socio; figuras finales. *Restricciones:* use los cuatro niveles; justifique cada uno. *Pasos:* (1) asigne un nivel a cada artefacto; (2) justifique el nivel en una línea; (3) proponga una transformación que llevaría cada elemento restringido a un nivel más abierto. *Evidencia esperada:* tabla. *Rúbrica:* 3 = niveles sensatos (código, pruebas, configuraciones y figuras T0; rangos agregados T1; justificaciones codificadas T2, o T1 si se desidentifican; audio, formularios de consentimiento y formularios de obtención con nombres T2 o T3; procedimiento del socio T3) con transformaciones; 2 = uno o dos mal juzgados; 1 = niveles uniformes; 0 = nada.

**EX041 — Manifiesto que falla de forma cerrada.** *Objetivo:* mejorar el Laboratorio 7. *Entradas:* Laboratorio 7. *Restricciones:* sin conexión. *Pasos:* (1) añada un archivo `data/synthetic_partner_feeders.csv`; (2) muestre que el orden actual de las reglas lo clasifica correctamente y explique por qué; (3) mueva la regla `synthetic_` al primer lugar, vuelva a ejecutar y registre el fallo; (4) añada una comprobación de contenido que niegue el nivel público a cualquier archivo que contenga la cadena `SUB-`. *Evidencia esperada:* código, salidas, explicación. *Rúbrica:* 3 = demuestra el peligro del orden, la comprobación de contenido funciona, la explicación se vincula al diseño que falla de forma cerrada; 2 = parcial; 1 = no se ejecutó; 0 = nada.

**EX042 — Evaluación del riesgo residual de divulgación.** *Objetivo:* evaluar datos sintéticos calibrados. *Entradas:* una región sintética calibrada con un condado real con un hospital, dos plantas de agua y cinco alimentadores, que preserva qué alimentador alberga el hospital. *Restricciones:* use las preguntas del §7.5. *Pasos:* (1) evalúe el riesgo de reidentificación; (2) evalúe qué revelaría una correspondencia; (3) proponga transformaciones y evalúe su costo para el valor de la investigación. *Evidencia esperada:* evaluación de una página. *Rúbrica:* 3 = reconoce la reidentificación a través de una estructura única, propone mezcla o generalización, sopesa con honestidad el valor para la investigación; 2 = evaluación superficial; 1 = declara seguro lo sintético; 0 = nada.

**EX043 — Documentación del modelo.** *Objetivo:* documentar el simulador del Laboratorio 5. *Entradas:* código del Laboratorio 5. *Restricciones:* siga los elementos del modelo del §7.6; como máximo dos páginas. *Pasos:* (1) redacte el propósito, las entidades, los procesos y su programación; (2) enumere las entradas y sus fuentes; (3) enumere las pruebas de verificación; (4) enumere las limitaciones conocidas, incluidas al menos tres del §7.7. *Evidencia esperada:* documento. *Rúbrica:* 3 = fiel al código (intervalos basados en eventos, retardo de rearranque, asignación de cuadrillas, semántica «O» para las dependencias), limitaciones específicas; 2 = inexactitudes menores; 1 = genérico; 0 = nada.

**EX044 — Sección de limitaciones.** *Objetivo:* redactar limitaciones que informen. *Entradas:* su propio estudio o el Estudio Cascada. *Restricciones:* al menos cinco limitaciones, cada una con su efecto, su dirección y el estudio que la resolvería. *Pasos:* (1) enumere las limitaciones; (2) indique el efecto y la dirección de cada una; (3) nombre el estudio que resolvería cada una; (4) ordénelas según cuánto podrían cambiar la afirmación principal. *Evidencia esperada:* tabla y párrafo de ordenación. *Rúbrica:* 3 = específicas, con dirección, con estudios que las resuelvan y una ordenación justificada; 2 = faltan direcciones en algunas; 1 = salvedades genéricas; 0 = nada.

### Síntesis del capítulo

La tesis es un argumento: afirmación, datos, garantía, respaldo, cualificador y refutaciones, cada uno aportado por una parte identificable del trabajo. La investigación sobre infraestructura debe conciliar la reproducibilidad con la protección de la infraestructura estudiada y de las personas implicadas; los archivos por niveles con manifiestos con *hash* lo logran, y los principios FAIR describen el acceso sin implicar apertura. Las herramientas de publicación deben fallar de forma cerrada y comprobar el contenido, no solo los nombres. Los datos sintéticos inventados conllevan poco riesgo de divulgación; los datos sintéticos calibrados necesitan una evaluación explícita del riesgo residual. Documente los modelos, los datos y el cómputo con estructuras reconocidas. Las limitaciones enuncian la dirección y los estudios que las resolverían, lo que las convierte en la siguiente agenda de investigación.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 08

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Defensa y plan de publicación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, el estudiante será capaz de:

1. Auditar el registro de afirmaciones de una tesis en busca de afirmaciones sin sustento, sin alcance definido o generalizadas en exceso antes de la defensa.
2. Prepararse para una defensa anticipando las preguntas más fuertes de los examinadores y respondiendo con evidencia, alcance y límites.
3. Planificar una secuencia de publicaciones para distintas comunidades que preserve la integridad del argumento general.
4. Integrar la divulgación coordinada y la coordinación sectorial en el calendario de publicación cuando los hallazgos afectan a vulnerabilidades o superficies de ataque.
5. Traducir una afirmación de investigación acotada en recomendaciones de política y práctica sin inflarla.
6. Convertir las limitaciones de la tesis en un programa de investigación posdoctoral creíble.

El capítulo 7 armó la tesis y su archivo. Este capítulo prepara al candidato para defenderla y para publicarla de forma responsable: el último paso del libro y del itinerario de estudio de 207 cursos.

### 8.1 La auditoría de las afirmaciones

Antes de la defensa, cada afirmación de la tesis —en el resumen, la introducción, las conclusiones de los capítulos y la conclusión general— pasa a un **registro de afirmaciones** con su evidencia, su alcance y sus limitaciones. Los resúmenes y las conclusiones son donde se acumulan las afirmaciones exageradas, porque se redactan al final, con prisa y buscando impacto.

#### 8.1.1 Actividad práctica: una primera revisión automatizada

```python
# Lab 8 - audit a thesis claim register before the defense (offline)
claims = [
    {"id": "K1", "text": "Dependency-aware restoration reduced weighted critical-service loss in the Riverbend model",
     "evidence": ["Ch5-MC"], "scope": "synthetic model, single crew, 4 feeders", "limits": ["model-policy circularity"], "status": "supported"},
    {"id": "K2", "text": "The benefit persists when generator fuel buffers double",
     "evidence": ["Ch6-boundary"], "scope": "gen_scale 2-4", "limits": [], "status": "supported"},
    {"id": "K3", "text": "Operators would adopt the dependency-aware ordering",
     "evidence": [], "scope": "", "limits": [], "status": "supported"},
    {"id": "K4", "text": "Dependency-aware restoration improves resilience of US utilities",
     "evidence": ["Ch5-MC", "Ch6-PortHalvard"], "scope": "two synthetic regions", "limits": ["no field data"], "status": "supported"},
]
OVERREACH = ("US utilities", "all utilities", "proves", "always")
for c in claims:
    problems = []
    if c["status"] == "supported" and not c["evidence"]:
        problems.append("no evidence for a supported claim")
    if not c["scope"]:
        problems.append("scope missing")
    if not c["limits"]:
        problems.append("no stated limitation")
    if any(w in c["text"] for w in OVERREACH) and "synthetic" in c["scope"]:
        problems.append("text generalizes beyond its synthetic scope")
    print(c["id"], "OK" if not problems else "; ".join(problems))
```

Salida esperada:

```text
K1 OK
K2 no stated limitation
K3 no evidence for a supported claim; scope missing; no stated limitation
K4 text generalizes beyond its synthetic scope
```

El script detecta tres fallos clásicos. K2 está sustentada, pero no enuncia ninguna limitación; sin embargo, el capítulo 6 mostró que el beneficio frente a SILO se reduce bruscamente a medida que crecen las reservas, de modo que «persiste cuando las reservas se duplican» necesita el cualificador de que el beneficio cae alrededor de un 85 % con el doble de reservas. K3 está marcada como sustentada sin evidencia: el ejercicio de mesa mostró que una visualización *puede desplazar las elecciones en un ejercicio de mesa*, lo que no es adopción. K4 generaliza de dos regiones sintéticas a «US utilities». Un filtro de palabras clave es tosco —pasaría por alto «nationwide» o «the grid»—, de modo que el script es una primera revisión; la auditoría decisiva es una persona que lea cada afirmación frente al registro.

#### 8.1.2 Afirmaciones corregidas

| ID | Texto corregido |
|---|---|
| K1 | En el modelo sintético de Riverbend, todos los órdenes conscientes de la criticidad redujeron la pérdida ponderada de servicios críticos en alrededor de un 90 % respecto del orden de clientes primero, con alrededor de un 70 % más de horas-cliente; allí, el orden por tiempo hasta el impacto no mejoró el orden por indicador crítico. |
| K2 | La ventaja del orden consciente de la criticidad sobre el orden de clientes primero cayó alrededor de un 85 % al duplicar las reservas y desapareció con cuatro veces las reservas obtenidas. |
| K3 | En un ejercicio de mesa con doce participantes de tres empresas de servicios sintéticas, una visualización del tiempo hasta el impacto desplazó los órdenes elegidos por siete participantes hacia el orden de menor consecuencia; no se estudió la adopción en la práctica. |
| K4 | En dos regiones sintéticas y 200 regiones generadas, el orden por tiempo hasta el impacto mejoró el orden por indicador crítico solo donde sus órdenes divergían; se desconoce con qué frecuencia ocurre esto en regiones reales. |

### 8.2 Preparar la defensa

#### 8.2.1 Qué ponen a prueba los examinadores

Los examinadores ponen a prueba si el candidato es un investigador independiente: si entiende los límites de su contribución mejor que nadie, si puede defender sus decisiones de diseño frente a alternativas y si conoce la literatura lo suficiente como para situar el trabajo. Espere preguntas de seis familias:

| Familia | Pregunta de ejemplo para el Estudio Cascada | Qué contiene una respuesta sólida |
|---|---|---|
| Contribución | «¿Qué hay de nuevo aquí, si las empresas de servicios ya mantienen listas de clientes críticos?» | La afirmación acotada; las condiciones en que los tiempos aportan valor; las condiciones previas medibles (divergencia, exactitud del mapa); el planteamiento desde la teoría de la programación. |
| Diseño | «¿Por qué una simulación y un ejercicio de mesa en lugar de un estudio de campo?» | Seguridad y ética (nunca probar en producción); rareza de los eventos reales; el uso de la validación histórica; lo que añadiría a continuación un piloto de campo durante ejercicios. |
| Validez | «¿No es circular el resultado?» | La prueba de desajuste; un modelador independiente para Port Halvard; el análisis del generador; lo que sigue siendo circular. |
| Valores | «¿Quién decidió que los hospitales importan cinco veces más que una central de telecomunicaciones, y por qué debería aceptarlo alguien?» | Proceso de obtención, panel, fecha, sensibilidad de los veredictos a los pesos (EX034), declaración explícita de que los pesos son una decisión de política. |
| Ética y doble uso | «¿No acaba de decirles a los adversarios que ataquen los datos de prioridad de restablecimiento?» | La revisión de doble uso; publicación a nivel general; recomendación defensiva; coordinación antes de publicar. |
| Conocimiento del campo | «¿Cómo se relaciona su trabajo con los enfoques de ingeniería orientados a consecuencias?» | La lógica de CCE de partir de la consecuencia; la tesis como contribución al lado de la *recuperación*; diferencias en la unidad de análisis. |

#### 8.2.2 Defensas simuladas

Realice al menos dos defensas simuladas: una con expertos del dominio favorables y otra con un metodólogo hostil ajeno a él. Registre las preguntas que no pudo responder bien; cada una es un vacío de la tesis (corríjalo), un vacío de su preparación (estúdielo) o una pregunta realmente abierta (dígalo en la defensa: «no lo sé, y así es como lo averiguaría» es una respuesta sólida).

#### 8.2.3 Responder

Responda a la pregunta formulada, luego aporte la evidencia y después enuncie el límite. Evite tres hábitos: defender una afirmación más fuerte que la que hace la tesis; conceder, por nervios, un punto que la tesis sí aborda; y llenar el silencio con especulaciones. Cuando un examinador propone una explicación alternativa que usted no puso a prueba, la mejor respuesta describe la prueba que la distinguiría y lo que significaría cada resultado.

### 8.3 Plan de publicación

#### 8.3.1 Secuenciar los artículos

El Estudio Cascada se divide de forma natural en artículos para distintas comunidades:

1. **Artículo de métodos / investigación operativa.** El orden de restablecimiento con servicios críticos limitados por reservas: el planteamiento de programación, la cota del oráculo, la heurística y sus modos de falla, el análisis de 200 regiones. Público: publicaciones de confiabilidad, riesgo e investigación operativa.
2. **Artículo de seguridad de la infraestructura.** La integridad del mapa de dependencias como condición previa del restablecimiento consciente de la criticidad, con los resultados del desajuste y la recomendación defensiva sometida a revisión de doble uso. Público: publicaciones de protección de infraestructuras críticas y talleres de seguridad de sistemas ciberfísicos.
3. **Artículo de factores humanos.** El ejercicio de mesa: visualización, elecciones, justificaciones y variables omitidas. Público: factores humanos y gestión de emergencias.
4. **Nota de replicación.** La reproducción de GridWater-Sim tras corregir una ambigüedad en el orden de los parámetros, con las pruebas de verificación. Público: la comunidad del banco de referencia; también es valiosa como artículo de datos o de software.

Publique los componentes T0 del archivo con identificadores persistentes junto con el primer artículo, para que los artículos posteriores citen los mismos artefactos versionados. Cada artículo debe enunciar el alcance de la afirmación general y no debe citar otro artículo de la tesis como evidencia más fuerte de lo que es.

#### 8.3.2 Preprints, embargos y resultados sensibles

Los *preprints* aceleran la retroalimentación y establecen la prioridad. Para los resultados que afectan a superficies de ataque, decida *antes* del preprint si se necesita coordinación (§8.4); un preprint es una publicación. Los financiadores y los socios pueden tener plazos de preaviso en sus acuerdos (capítulo 1, §1.5.3); respételos y rechace cualquier solicitud que equivalga a un veto sobre los hallazgos.

### 8.4 Divulgación coordinada y coordinación sectorial

La investigación sobre infraestructura puede producir tres tipos de hallazgo sensible, cada uno con su propia vía:

| Hallazgo | Ejemplo | Vía |
|---|---|---|
| Una vulnerabilidad de un producto | Una falla en el software de gestión de interrupciones de un proveedor encontrada al construir el simulador | Divulgación coordinada de vulnerabilidades al proveedor, directamente o a través de un coordinador como el [programa CVD de CISA](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program); la práctica internacional se describe en ISO/IEC 29147 (divulgación) e ISO/IEC 30111 (gestión). |
| Una debilidad propia de una organización | La lista de clientes críticos de un socio tiene asignaciones de alimentadores erróneas | Informe privado al socio según el acuerdo de uso de datos; nunca se publica de forma identificable. |
| Una superficie de ataque a nivel sectorial | Los datos de prioridad de restablecimiento y los mapas de dependencias son objetivos de alto valor cuya corrupción amplifica las interrupciones | Coordinar con los socios y, cuando corresponda, con la organización sectorial de intercambio de información pertinente antes de publicar; publicar a nivel general con recomendaciones defensivas. |

Incorpore el periodo de coordinación al calendario. CISA describe su proceso como uno que abarca el contacto con el proveedor, el análisis, la coordinación de la remediación y la publicación del aviso, y señala que puede divulgar tras un periodo si un proveedor no responde; lea la política vigente en lugar de confiar en un resumen. La tesis registra qué se divulgó, a quién, cuándo y qué se retuvo.

### 8.5 Traducir a política y práctica

Los públicos de políticas necesitan recomendaciones que se deriven de la evidencia y que digan con qué confianza se formulan. A partir de la afirmación acotada del Estudio Cascada, las recomendaciones defendibles son:

1. **Hacer explícita la compensación.** Priorizar los servicios críticos en el restablecimiento cuesta a los clientes ordinarios tiempo sin electricidad; el tamaño de ese costo debe estimarse y discutirse en los planes de emergencia y, cuando corresponda, en consulta pública. (Evidencia fuerte dentro del modelo; la dirección es un resultado de la teoría de la programación).
2. **Auditar los mapas de dependencias.** El restablecimiento consciente de la criticidad es tan bueno como el mapa alimentador-instalación y los datos de reservas que lo sustentan; las empresas de servicios y sus socios deben verificarlos con regularidad. (Evidencia fuerte de fragilidad dentro del modelo).
3. **Proteger los datos de prioridad de restablecimiento.** Tratar las listas de clientes críticos, los mapas de dependencias y los inventarios de reservas como sensibles y críticos para la integridad. (Inferencia a partir de los resultados del desajuste y de los informes públicos de amenazas; confianza moderada).
4. **Medir la divergencia antes de cambiar la práctica.** Una empresa de servicios puede determinar si el orden por tiempo hasta el impacto cambiaría el orden de su lista crítica actual; si no lo cambia, no gana nada adoptándolo. (Condicionado al modelo; bajo costo de comprobación).

Estas recomendaciones encajan de forma natural en procesos de gestión de riesgos que ya existen —la gestión de riesgos sectoriales del NSM-22 en Estados Unidos, las evaluaciones de riesgos de las entidades críticas de la Directiva CER en la UE— sin afirmar que ninguna autoridad deba imponerlas. Un resumen de políticas ocupa dos páginas, enuncia su base de evidencia y sus límites, y enlaza con la tesis y el archivo.

### 8.6 El programa posdoctoral

La tabla de limitaciones del capítulo 7 es una agenda de investigación. Un programa creíble de tres estudios:

1. **Encuesta sobre la divergencia en regiones reales** (empírica, protegida): medir, con protección T3, con qué frecuencia divergen los órdenes por tiempo hasta el impacto y por lista crítica en una muestra de empresas de servicios. Esto responde a la pregunta que los generadores sintéticos no pudieron responder.
2. **Modelado de las reservas humanas** (modelo + validación): representar la ampliación de las reservas (entregas de combustible, agua en camiones) como condicionada al acceso a las telecomunicaciones y a las carreteras, validarla frente a registros posteriores a la acción y volver a poner a prueba las afirmaciones sobre el restablecimiento.
3. **Ataques a la integridad de los datos de planificación** (seguridad + simulación): modelar la corrupción adversarial de los mapas de dependencias y de las listas de prioridades, evaluar estrategias de detección y auditoría, y estimar su valor en términos de consecuencia; una continuación directa del hallazgo de doble uso, realizada con socios sectoriales.

Cada estudio tiene una afirmación falsable, un diseño seguro y un modelo de colaboración con socios, y cada uno cambiaría una decisión que alguien toma.

### 8.7 Ejemplo resuelto: un intercambio en la defensa (sintético)

*Examinador:* «Su región de Port Halvard se diseñó para que su método ganara. ¿Por qué debería creer algo más allá de Riverbend, donde fracasó?».

*Candidato:* «Tiene razón en que Port Halvard se seleccionó para que el mecanismo pudiera actuar; los criterios de selección se prerregistraron antes de la simulación y la construyó otro modelador, pero es una prueba del mecanismo, no una estimación de con qué frecuencia ayuda el método. Por eso ejecuté el análisis de 200 regiones, en el que la ganancia sobre el orden por indicadores es exactamente cero siempre que los dos órdenes coinciden y crece con la divergencia, y por eso la tesis no afirma nada sobre la frecuencia de la divergencia en regiones reales. El fracaso de Riverbend forma parte de la afirmación: muestra que el método no aporta nada donde los órdenes coinciden o donde los pesos y la ramificación favorecen otro orden. Si quiere una estimación para empresas de servicios reales, el estudio que haría primero es la encuesta sobre la divergencia que describo en la conclusión».

La respuesta concede lo que es cierto, cita la evidencia específica, reformula la afirmación acotada y nombra el siguiente estudio. No defiende la afirmación original, más amplia.

### 8.8 Errores habituales y límites

- Resúmenes y conclusiones que afirman más que los capítulos.
- Tratar la defensa como una presentación y no como un examen de independencia.
- Publicar artículos cuyas afirmaciones se desvían más allá del alcance de la tesis.
- Publicar preprints antes de decidir si se necesita coordinación.
- Recomendaciones de política sin niveles de confianza ni vínculos con la evidencia.
- Planes posdoctorales que repiten la tesis en lugar de abordar sus limitaciones.

- Mantener un registro de afirmaciones, pero auditarlo solo por palabras clave, lo que pasa por alto las extralimitaciones formuladas como «nationwide» o «the grid».
- Responder a la explicación alternativa de un examinador defendiendo la afirmación original en lugar de describir la prueba que las distinguiría.
- Publicar el artículo de seguridad de la infraestructura antes de haber consultado a los socios y al organismo sectorial de intercambio de información sobre el hallazgo de la integridad de los mapas.
- Citar un artículo de la tesis como evidencia más fuerte de lo que es en el artículo siguiente.
- Redactar recomendaciones de política que implican una obligación que la evidencia no sustenta.

### Ejercicios — capítulo 8

**EX045 — Auditoría de las afirmaciones.** *Objetivo:* auditar un registro de afirmaciones. *Entradas:* Laboratorio 8. *Restricciones:* sin conexión. *Pasos:* (1) ejecute el laboratorio y registre la salida; (2) añada una afirmación K5, "Our method makes the grid resilient to cyber attacks", con evidencia `["Ch5-MC"]`, alcance "synthetic model" y límites `["no field data"]`; (3) muestre que el script no la detecta; (4) mejore la comprobación y vuelva a ejecutar; (5) redacte un texto corregido para K5. *Evidencia esperada:* código, salidas, afirmación corregida. *Rúbrica:* 3 = demuestra la omisión, una comprobación mejorada sensata (por ejemplo, términos como "the grid" o "resilient to" combinados con un alcance sintético), afirmación corregida debidamente acotada; 2 = comprobación mejorada, pero la afirmación sigue inflada; 1 = no se ejecutó; 0 = nada.

**EX046 — Banco de preguntas de los examinadores.** *Objetivo:* prepararse para la defensa. *Entradas:* su tesis o el Estudio Cascada. *Restricciones:* al menos dos preguntas de cada una de las seis familias del §8.2.1; una respuesta modelo de 120 palabras como máximo para las tres más difíciles. *Pasos:* (1) redacte al menos dos preguntas de cada familia; (2) marque las tres más difíciles; (3) redacte una respuesta modelo de 120 palabras como máximo para cada una; (4) identifique cualquier pregunta que revele un vacío de la tesis y no de su preparación. *Evidencia esperada:* banco de preguntas y respuestas. *Rúbrica:* 3 = preguntas agudas y específicas, respuestas que siguen el patrón pregunta-evidencia-límite, al menos un vacío real identificado; 2 = respuestas defensivas; 1 = preguntas genéricas; 0 = nada.

**EX047 — Plan de publicación.** *Objetivo:* secuenciar los artículos con integridad. *Entradas:* el Estudio Cascada o su tesis. *Restricciones:* de tres a cinco artículos; público, afirmación y evidencia de cada uno; versionado del archivo; puntos de control de la coordinación. *Pasos:* (1) enumere los artículos con sus públicos; (2) enuncie la afirmación de cada artículo y la evidencia que usa; (3) cartografíe los artefactos compartidos y sus versiones; (4) marque dónde deben producirse la coordinación o la revisión de doble uso antes de la publicación. *Evidencia esperada:* plan con calendario. *Rúbrica:* 3 = artículos distintos y sin solapamiento en sus afirmaciones, artefactos compartidos versionados, coordinación situada antes de cualquier preprint que afecte a superficies de ataque; 2 = solapamientos o puntos de control ausentes; 1 = solo una lista de títulos; 0 = nada.

**EX048 — Enrutamiento de la divulgación.** *Objetivo:* encaminar hallazgos sensibles. *Entradas:* cuatro hallazgos sintéticos: (a) la empresa de servicios socia del simulador exporta su lista de clientes críticos a una página web interna sin autenticación; (b) un producto comercial de gestión de interrupciones acepta importaciones de configuración sin firmar; (c) en tres socios, los inventarios de reservas en papel superan en un 20–40 % a los inventarios físicos; (d) los procedimientos de radio de las cuadrillas de restablecimiento dependen de un único sitio repetidor. *Restricciones:* vías del §8.4; indique el momento y lo que se publica. *Pasos:* (1) clasifique cada hallazgo por tipo; (2) elija la vía; (3) indique a quién se notifica y cuándo; (4) indique qué se publica finalmente y a qué nivel. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (a) informe privado al socio, (b) CVD con el proveedor o un coordinador, (c) informes privados más la publicación general de la brecha entre los inventarios en papel y los físicos, (d) informe privado y un hallazgo general sobre los puntos únicos de falla en las comunicaciones de restablecimiento, con un calendario sólido; 2 = uno mal encaminado; 1 = dos o más; 0 = nada.

**EX049 — Resumen de políticas.** *Objetivo:* traducir sin inflar. *Entradas:* la afirmación acotada del §6.5 y las recomendaciones del §8.5. *Restricciones:* dos páginas; nivel de confianza y vínculo con la evidencia para cada recomendación; un párrafo sobre lo que la investigación no muestra. *Pasos:* (1) redacte el resumen; (2) marque cada oración como evidencia, inferencia o recomendación; (3) elimine cualquier oración que no pueda rastrearse hasta la tesis. *Evidencia esperada:* resumen con marcas. *Rúbrica:* 3 = recomendaciones rastreables y matizadas, lo no hallado explícito, lenguaje accesible; 2 = algunas oraciones no rastreables; 1 = defensa de una postura sin evidencia; 0 = nada.

**EX050 — Programa de investigación posdoctoral.** *Objetivo:* convertir las limitaciones en investigación. *Entradas:* su tabla de limitaciones del EX044 o el §7.7. *Restricciones:* tres estudios; cada uno con una afirmación falsable, un diseño seguro, un modelo de colaboración con socios y la decisión que cambiaría. *Pasos:* (1) elija tres limitaciones; (2) diseñe un estudio para cada una; (3) ordene los estudios por dependencia y valor; (4) indique qué resultado pondría fin al programa. *Evidencia esperada:* programa de dos páginas. *Rúbrica:* 3 = los estudios abordan directamente las limitaciones de mayor consecuencia, son falsables y seguros, y están ordenados por dependencia, con un resultado de parada honesto; 2 = un estudio débil; 1 = repite la tesis; 0 = nada.

### Síntesis del capítulo

La defensa examina la independencia: el candidato debe conocer los límites de la contribución mejor que nadie. Un registro de afirmaciones, auditado con un script y con lectura, elimina las afirmaciones exageradas que se acumulan en los resúmenes y las conclusiones. Las preguntas de los examinadores se agrupan en familias previsibles; responda con evidencia y límites, y nombre el estudio que resolvería lo que no sabe. Publique en secuencia para distintas comunidades con artefactos compartidos versionados, y decida sobre la coordinación antes de que cualquier preprint afecte a una superficie de ataque. Encamine de forma distinta las vulnerabilidades, las debilidades propias de una organización y las superficies de ataque a nivel sectorial. Traduzca las afirmaciones acotadas en recomendaciones con niveles de confianza. Las limitaciones se convierten en el siguiente programa de investigación: el final natural de un curso doctoral y de este itinerario de estudio.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 08

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Termine el itinerario de 207 cursos →](../SUBJECTS.md)

Este es el último capítulo de este curso y del itinerario de estudio de 207 cursos.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Cada resultado resuelto muestra una respuesta defendible y explica qué premia la rúbrica. Las respuestas alternativas pueden obtener la puntuación completa cuando cumplen el mismo estándar de evidencia, alcance y honestidad sobre los límites. Los resultados numéricos provienen de los laboratorios sin conexión de este libro ejecutados con la biblioteca estándar de Python 3; si su salida difiere, compruebe primero la versión de Python, la semilla y si cambió el orden de las extracciones aleatorias.

### Capítulo 1: EX001–EX007

**EX001 — Auditoría con la escalera de afirmaciones.**

| # | Aserción | Peldaño | Supuesto oculto | Observación que la refuta |
|---|---|---|---|---|
| 1 | Los registros muestran un acceso al sistema de gestión de la distribución (DMS) a las 01:52. | L1 si el registro se preserva con el estado del reloj; si no, L2 | La fuente del registro está íntegra y su reloj es correcto; «atacante» ya es una inferencia | El registro muestra una sesión programada de un proveedor; desfase del reloj |
| 2 | El acceso lo realizó un atacante. | L2 | La sesión no estaba autorizada | La sesión coincide con una orden de mantenimiento autorizada |
| 3 | El acceso causó la interrupción. | L3 afirmación causal de caso | Se emitieron comandos y el alimentador se abrió por ellos, no por la protección | Los registros de relés muestran un disparo de protección; ningún comando en los registros del DMS |
| 4 | El hospital se quedó sin electricidad. | L4 consecuencia | El generador del hospital no arrancó o se quedó sin combustible | Los registros del generador muestran una transferencia sin cortes |
| 5 | Se puso en peligro a los pacientes. | L4 consecuencia, fuerte | Los servicios clínicos se vieron afectados | El hospital no reporta ningún cambio en el servicio |
| 6 | Las cooperativas rurales son el punto más débil de la red. | L5 afirmación de investigación a partir de un caso | Un caso representa a una población; comparación con otros tipos de empresas de servicios | Cualquier comparación con la tasa base |

Reescritura: «En este caso sintético, el DMS registró una sesión a las 01:52 (reloj del DMS) cuya autorización todavía no se ha establecido. Un alimentador que abastece al hospital se abrió en algún momento posterior; no se ha establecido si lo causó un comando, ni si el hospital se quedó sin electricidad en lugar de transferir la carga a su generador. De un solo caso no se deduce ninguna conclusión sobre las cooperativas en general». La puntuación completa exige señalar la reserva del generador (la razón más probable por la que la afirmación de consecuencia es falsa) y la generalización.

**EX002 — Definición y población.** Una respuesta defendible cita: la definición legal que usa la política estadounidense (42 U.S.C. § 5195c(e)) y la estructura sectorial del NSM-22 a través de la página de CISA; las definiciones de «entidad crítica» del artículo 2 de la CER y su anexo de sectores; el artículo 3 de NIS2 con los anexos I y II (entidades esenciales e importantes). Clasificación típica: el hospital regional pertenece al sector estadounidense Healthcare and Public Health, es probablemente una entidad de NIS2 en el sector sanitario según su tamaño y las normas nacionales, y solo puede ser designado entidad crítica con arreglo a la CER si el Estado miembro lo identifica; la pequeña empresa de agua pertenece al sector estadounidense Water, puede quedar por debajo de los umbrales de tamaño de NIS2 salvo que un Estado miembro le aplique las normas, y está en el sector de agua potable de la CER si se la designa; el procesador de pagos pertenece al sector estadounidense Financial Services, está sujeto en la UE a las normas del sector financiero (NIS2 contiene disposiciones de *lex specialis* en relación con actos sectoriales como DORA) y a los sectores bancario o de infraestructuras de los mercados financieros de la CER si se lo designa. Consecuencia de diseño: una comparación entre jurisdicciones debe definir su población por un criterio funcional común (por ejemplo, población atendida y función) y no por categoría jurídica, y reportar la situación jurídica de cada unidad como covariable. La rúbrica premia las citas exactas y trata los casos que dependen de una designación como condicionales y no como seguros.

**EX003 — Tipificación de interdependencias.**

| Relación | Tipo | Justificación |
|---|---|---|
| TEL de F2 | Física | La electricidad es un insumo material |
| HOSP de F2 | Física | Igual |
| HOSP de WATER | Física | El agua es un insumo material |
| WATER de F3 | Física | Igual |
| SCADA del agua de TEL | Cibernética | Dependencia de información transportada por la red de telecomunicaciones |
| Facturación del procesador de pagos | Lógica (o cibernética) | Mecanismo financiero y contractual; afecta a las operaciones solo al cabo de días, no a la prestación del servicio |
| Combustible de los generadores del acceso por carretera | Física, con un componente geográfico si las carreteras y los alimentadores comparten peligros | El combustible es un insumo material; el acceso puede fallar por el mismo evento local |

No existe ningún ciclo entre los servicios enumerados (ningún servicio de la lista depende a su vez de HOSP, WATER o TEL). Un modelo puro de flujo de potencia omitiría la dependencia combustible–carretera, la dependencia de facturación y la dependencia del SCADA del agua respecto de TEL. La puntuación completa señala que la ausencia de ciclo es una propiedad de esta lista, no de la región: las telecomunicaciones suelen necesitar agua para refrigeración y las empresas eléctricas necesitan telecomunicaciones para el restablecimiento, lo que crearía ciclos.

**EX004 — Análisis de Menlo.** Partes interesadas: los despachadores entrevistados; los gestores de emergencias del ejercicio de mesa; REC, RWA, el hospital y el operador de telecomunicaciones como organizaciones; la población atendida; los reguladores; el financiador; el equipo de investigación. Principio por principio: *respeto por las personas*: consentimiento individual separado del permiso del empleador, audio opcional, retirada sin penalización, ningún dato para los superiores; *beneficencia*: ningún contacto con sistemas en funcionamiento, solo simulación, prueba de sensibilidad sobre todos los artefactos, revisión de seguridad física no requerida porque no se energiza nada; *justicia*: no cargar solo a la empresa de servicios más pequeña; reportar el compromiso en clientes-hora para que no se oculte la pérdida de ninguna población; *ley e interés público*: acuerdos de uso de datos y de publicación, regímenes de protección de la información aplicables identificados, métodos transparentes. Autoridad de detención: un responsable designado del socio y el investigador principal. Si el socio se retira: se destruyen los datos identificables de las entrevistas; las contribuciones agregadas y desidentificadas se conservan solo si los formularios de consentimiento lo preveían. La rúbrica premia las salvaguardas concretas, en especial la protección del personal frente al uso disciplinario y el tratamiento de la población atendida como parte interesada.

**EX005 — Prueba de sensibilidad.**

| Artefacto | Nivel | Razonamiento y transformación |
|---|---|---|
| (a) Duraciones de restablecimiento agregadas por clase de alimentador | Público | Ningún activo ni ubicación específicos; mantener clases amplias |
| (b) Hospitales con los días de combustible de sus generadores | Retenido | Identifica instalaciones específicas y su reserva: datos para seleccionar objetivos. Si hace falta, transformar en una distribución anónima de días de combustible por tipo de instalación |
| (c) Código del modelo | Público | No contiene datos de infraestructura; comprobar que los valores por defecto sean sintéticos |
| (d) Marco de codificación de las entrevistas | Público | Sin citas textuales ni identificadores; las citas van al nivel controlado |
| (e) Mapa del alimentador que abastece a la planta regional de agua | Retenido | Dependencia específica de un activo específico. Describirlo en la tesis como «mapeo proporcionado por el socio, usado solo para la obtención de juicios» |

**EX006 — Inversión de métricas.** Salida con la métrica añadida (muestras horarias con Q < 0,5): A 5 h, B 0 h, C 0 h. Con una ventana de 72 horas, la pérdida de C sube de 7,40 a 13,40 unidades-hora, su tiempo hasta la recuperación pasa a ser de 36 h y deja de estar censurado; A y B no cambian. Para el agua potable, una métrica primaria defendible son las **horas por debajo de un umbral de presión o de calidad asociado a un aviso de hervir el agua o a la pérdida del caudal contra incendios**, porque la consecuencia sanitaria depende de umbrales; la pérdida de área y el tiempo hasta la recuperación son secundarios. La puntuación completa nombra la fuente del umbral (la regulación de la empresa de servicios o la orientación de salud pública de la jurisdicción) en lugar de inventar un valor, y señala que el umbral de 0,5 del laboratorio es ilustrativo.

**EX007 — Esqueleto de protocolo.** Un protocolo sólido fija la pregunta y el peldaño de la afirmación (L5 condicional, dentro de una clase de escenarios); define la pérdida ponderada de servicios críticos y los clientes-hora, una ventana de 72 horas y una regla de censura; nombra el modelo, la obtención de juicios, el ejercicio de mesa y los registros históricos como fuentes de evidencia, con sus límites; especifica las cuatro políticas y las dos regiones; preespecifica parámetros, semillas, métricas, el margen de no inferioridad y la regla de decisión; contiene el análisis de Menlo, la regla «nunca pruebe en producción» y la aprobación para investigación con seres humanos para las entrevistas y el ejercicio de mesa; nombra los regímenes de protección de la información y el almacenamiento; adjunta los acuerdos de uso de datos y de publicación; y enumera condiciones de detención (petición del socio; cualquier brecha de datos; cualquier malestar de un participante) distintas de las condiciones de abandono (H2 falla en ambas regiones; el modelo falla la validación histórica por más de un margen declarado de antemano). El revisor hostil atacaría primero los pesos, la circularidad y la selección de contextos.

### Capítulo 2: EX008–EX014

**EX008 — Protocolo de búsqueda.** Un protocolo modelo para «¿Afectan los incidentes de *ransomware* en hospitales a los resultados de los pacientes en hospitales vecinos?»: bloques conceptuales (ransomware OR cyberattack OR "cyber incident") AND (hospital OR "health system") AND (diversion OR spillover OR "neighboring" OR "nearby") AND (outcome OR mortality OR "length of stay"); fuentes: un índice biomédico, un índice académico general e informes gubernamentales y sectoriales; encadenamiento a partir de dos estudios semilla; elegibilidad: estudios con grupo de comparación o serie temporal; cribado por dos revisores sobre una muestra del 10 % con el acuerdo reportado antes de repartir el trabajo; parar cuando dos rondas consecutivas de encadenamiento no añadan nada. La rúbrica premia las fuentes interdisciplinarias y el acuerdo medido.

**EX009 — Evaluación de un artículo de modelado.** Estructura: ¿representa la cosimulación las reservas y el restablecimiento? Parámetros: ¿con fuente o supuestos? Verificación: la descripción no aporta evidencia de pruebas; desconocida. Validación: un evento histórico, con el modelo de los propios autores; buena, pero única. Sensibilidad: desconocida. Línea de base: si la comparación es solo con «clientes primero», es una línea de base débil (capítulo 3). Disponibilidad: desconocida. Afirmación más fuerte que puede sustentar: «En la cosimulación de los autores, calibrada con un evento histórico, el restablecimiento consciente de las dependencias redujo la pérdida de servicios críticos en comparación con [su línea de base]», una afirmación sobre el modelo (L2–L3), no sobre la infraestructura en general.

**EX010 — Ajuste de la familia de modelos.** (a) Insumo-producto (IIM o insumo-producto económico): estima la pérdida de producción a nivel sectorial; límite: lineal, sin tiempos, el detalle de las instalaciones desaparece en la agregación. (b) Flujo o cosimulación, o un modelo de tiempo de reservas como el Laboratorio 3: límite: necesita datos a nivel de instalación y reservas validadas. (c) Estudio empírico cualitativo (entrevistas, registros posteriores a la acción), que puede informar un modelo basado en agentes: límite: autodeclaración y muestras pequeñas. (d) Percolación topológica: límite: abstracta; sin reservas ni flujos; solo comprensión estructural.

**EX011 — La norma como hipótesis.** Afirmación implícita: asignar e implementar un SL-T por zona reduce la probabilidad de que un adversario de la capacidad correspondiente logre un efecto con consecuencias. Hipótesis: «En zonas de un banco de pruebas implementadas según los requisitos de SL 3, equipos rojos de capacidad fija logran un efecto predefinido a nivel de proceso con menos frecuencia, o tardan más, que en zonas por lo demás idénticas implementadas según SL 1». Diseño: banco de pruebas aislado, varias zonas equivalentes, equipos rojos independientes que desconocen el SL, efectos predefinidos simulados y no físicos. Factores de confusión: habilidad y fatiga del equipo rojo; calidad de la implementación independiente del SL nominal; aprendizaje entre ensayos. La rúbrica premia la seguridad (solo banco de pruebas) y medir la seguridad alcanzada y no la afirmada.

**EX012 — Reparar el mapa de la literatura.** Añada un sexto campo y filtre por `s[5] == "cyber"`. Salida para C3: `single-source; needs replication; strong+independent=['P7']`. El estado de C3 no cambia porque P7 es a la vez independiente y ciber, pero C1, C2 y C4 ya no tienen sustento que cumpla los requisitos para afirmaciones sobre interrupciones *provocadas por ciberataques*. Explicación: la evidencia de interrupciones por todo tipo de amenazas se transfiere a las provocadas por ciberataques solo mediante un argumento —los escenarios cibernéticos pueden ser simultáneos, sincronizados por el adversario y pueden corromper las herramientas de restablecimiento—, de modo que una afirmación cibernética necesita una validación específica para lo cibernético o un argumento de transferencia explícito.

**EX013 — Clasificar el vacío.** (a) *Contradictorio*: el siguiente estudio discrimina mecanismos midiendo ambas reservas y su agotamiento en las mismas instalaciones. (b) *No transferido*: el siguiente estudio prueba si las variables de planificación de la capacidad de sobrecarga predicen el orden óptimo de restablecimiento. (c) *Débil*: documentos técnicos de proveedores con conflictos de interés; el siguiente estudio es una comparación independiente con una línea de base fuerte. (d) *Ausente*: el siguiente estudio es un primer diseño comparativo, aunque sea una pequeña comparación de mesa entre CCE y la priorización guiada por vulnerabilidades.

**EX014 — Enunciado falsable y memorando de frontera.** Enunciado de ejemplo: «En interrupciones eléctricas regionales de más de ocho horas, la aceptación de pagos con tarjeta en tiendas de alimentación y farmacias cae por debajo del 50 % de lo normal en las primeras cuatro horas debido a la dependencia del enlace de retorno de telecomunicaciones y de la alimentación del punto de venta, salvo que los comercios dispongan de autorización sin conexión; esto queda refutado si los registros de transacciones de dos regiones independientes muestran una aceptación superior al 50 % a las cuatro horas entre los comercios sin capacidad sin conexión». Notas de las pruebas: abierto (ningún estudio regional encontrado en la búsqueda documentada, hipotéticamente), importante (acceso a alimentos y medicamentos durante las interrupciones), factible (datos de transacciones agregados mediante un socio de la red de pagos), falsable (observación enunciada). El memorando argumenta que primero debe cartografiarse la dependencia de los comercios respecto del enlace de retorno, porque sin ello la aceptación no puede atribuirse a las telecomunicaciones o a la electricidad. La rúbrica premia un refutador factible y un orden razonado de las preguntas.

### Capítulo 3: EX015–EX020

**EX015 — Tipificación de contribuciones.** (a) Artefacto: necesita documentación, pruebas de verificación y evidencia de uso. (b) Medición: necesita evidencia de confiabilidad (test-retest, entre evaluadores) y de validez. (c) Hallazgo empírico: necesita un estudio muestreado y documentado de empresas de servicios, con marco muestral y tasas de respuesta. (d) Método: necesita una comparación con la práctica actual más fuerte en métricas enunciadas, en más de un contexto. (d) usa (a) como instrumento; (a) por sí sola no puede sustentar (d), porque la existencia del simulador no dice nada sobre si el método supera a la práctica actual. (c) es una condición previa para saber si (d) es novedoso en la práctica.

**EX016 — Comprobación con la teoría de la programación.** Cocientes *w/p*: F1 9000/4 = 2250; F2 1200/3 = 400; F3 2500/5 = 500; F4 6000/4 = 1500. Orden de Smith: F1, F4, F3, F2. Tiempos de finalización 4, 8, 13, 16 h → horas-cliente = 9000·4 + 6000·8 + 2500·13 + 1200·16 = 135 700 → 135,7 miles. Orden F2, F3, F1, F4: finalizaciones 3, 8, 12, 16 → 1200·3 + 2500·8 + 9000·12 + 6000·16 = 227 600 → 227,6 miles. Aumento del 67,7 %. (En los laboratorios de este libro, las horas-cliente también se cuentan por alimentador hasta el restablecimiento; el retardo de rearranque se aplica solo a los servicios críticos).

**EX017 — Ampliación del tiempo hasta el impacto.** Con F2 → HOSP = 60 y TEL → HOSP = 30, el instante de falla del hospital por la vía eléctrica es min(60, 8 + 30 = 38) = 38 h, pero por el agua es 9 + 4 = 13 h, de modo que HOSP sigue fallando a las 13 h. El resultado no cambia porque el camino determinante es el del agua. Más en el fondo, el acuerdo «el generador dura 60 h *si* las telecomunicaciones funcionan para pedir combustible; si no, 26 h» es una *reserva condicional*, una combinación Y/O que un grafo de caminos más cortos con pesos fijos en las aristas no puede expresar. Modelarlo exige reservas dependientes del estado (como los intervalos de dependencia del Laboratorio 5, ampliados) o una simulación en la que las entregas de combustible sean eventos que requieren TEL.

**EX018 — Conjunto de hipótesis.** Ejemplo para el restablecimiento de sitios de telecomunicaciones tras un incidente cibernético en un operador: *Beneficio* — «Restablecer los sitios celulares en orden del tiempo hasta el impacto de los servicios dependientes reduce la pérdida ponderada de capacidad de llamadas de emergencia y de conectividad hospitalaria en ≥ 20 % en comparación con restablecer por abonados atendidos». *Mejor práctica* — «…en ≥ 10 % en comparación con la lista de sitios prioritarios existente del operador». *Mecanismo* — «La ganancia es cero donde el orden de la lista y el orden por tiempo hasta el impacto coinciden y crece con la divergencia; se desvanece cuando la autonomía de las baterías de los sitios supera el tiempo total de restablecimiento». *No inferioridad* — «Las horas-abonado perdidas aumentan en ≤ 15 % en comparación con la lista de sitios prioritarios». Resultados definidos operacionalmente (por ejemplo, intentos de llamada de emergencia fallidos por hora, a partir de contadores de red en una simulación). Umbrales justificados por el costo de cambio declarado por el operador y las expectativas de calidad del servicio del regulador, con responsables y fechas.

**EX019 — Tabla de explicaciones rivales.** Rivales: cualquier lista de prioridades explica la ganancia (prueba: línea de base de lista); pesos (prueba: pesos alternativos); baterías cortas en la red elegida (prueba: escalado de baterías, segunda red); circularidad (prueba: modelo independiente, error del mapa); adopción (prueba: ejercicio de mesa con ingenieros); una sola cuadrilla o desplazamientos ignorados (prueba: cuadrillas y matriz de desplazamientos); el desvío del tráfico a sitios vecinos hace irrelevante el orden (prueba: modelo con cobertura de vecinos). La puntuación completa incluye al menos circularidad, adecuación de la línea de base, pesos y adopción.

**EX020 — Condiciones de fracaso y criterios del segundo contexto.** Condiciones de fracaso: como en el §3.8, adaptadas. Criterios del segundo contexto derivados del mecanismo: al menos tres sitios de servicios críticos; divergencia entre el orden de la lista y el orden por tiempo hasta el impacto en al menos dos posiciones; rango de reservas que se solapa con el tiempo total de restablecimiento; un modelo de cuadrillas distinto del primer contexto. Verificación por los revisores: una enmienda del prerregistro con marca de tiempo (en un registro público o un *commit* de repositorio con una etiqueta firmada) fechada antes de cualquier simulación del segundo contexto, más la declaración del modelador de que no tuvo acceso a los resultados del primer contexto.

### Capítulo 4: EX021–EX026

**EX021 — Bitácora de reproducción.** Objetivo: agua 0,236 (artículo sintético, tabla 2). Tolerancia de ± 0,005 fijada antes de ejecutar. Ejecución 1 (matriz traspuesta): `[0.528, 0.028, 0.057]`; el agua difiere en 0,208, fuera de la tolerancia; la electricidad coincide. Diagnóstico: el artículo define *A\*_ij* como el efecto de *j* sobre *i*; el archivo de entrada se leyó por columnas. Ejecución 2 (convención correcta): `[0.528, 0.236, 0.163]`; reproducido. Entorno: versión de Python, sistema operativo, fecha. Decisión: reproducido tras corregir un error de convención en nuestro manejo de las entradas. Nota: que la electricidad coincida en ambas ejecuciones muestra por qué comprobar una sola salida es insuficiente.

**EX022 — Análisis de perturbaciones con el IIM.** Solo electricidad 0,5: `[0.528, 0.236, 0.163]`. Solo telecomunicaciones 0,5: `[0.057, 0.101, 0.519]`. Ambas: `[0.585, 0.336, 0.682]`, que es igual a la suma de los dos vectores separados (salvo redondeo), porque el IIM es lineal: *q* = (*I* − *A\**)⁻¹ *c\** y la inversa se distribuye sobre la suma de las perturbaciones. Afirmación sustentada: «en este modelo lineal de equilibrio, una perturbación combinada de electricidad y telecomunicaciones eleva la inoperabilidad del agua a alrededor de 0,34». No sustentada: nada sobre tiempos, reservas, umbrales u orden de restablecimiento, ni ninguna afirmación de que una inoperabilidad superior a 1 tenga sentido (los modelos lineales pueden superar los límites físicos con perturbaciones grandes).

**EX023 — La trampa del orden de los parámetros.** Llamada correcta `triangular(4, 12, 8)`: media (4 + 8 + 12) / 3 = 8,0. La llamada errónea `triangular(4, 8, 12)` pasa high = 8 y mode = 12; CPython calcula *c* = (12 − 4)/(8 − 4) = 2 y devuelve 4 + 4·√(2*u*), de modo que los valores van de 4 a unos 9,66 y la media es de unos 7,77 (una ejecución con semilla de 100 000 extracciones dio mínimo 4,02, máximo 9,66, media 7,77). La salida no es una distribución triangular y supera el «high» documentado de 8 sin llegar nunca a 12. Una comprobación de la media por sí sola (7,77 frente a 8,0) se descarta fácilmente como ruido; una comprobación del rango frente a los límites documentados y un histograma revelan el error de inmediato.

**EX024 — Pruebas de invariantes.** Aserciones de ejemplo con el Laboratorio 5: (1) con todas las reservas por encima de 72 h, la pérdida de cada política es 0; (2) `evaluate` con órdenes idénticos da resultados idénticos; (3) ORACLE ≤ cada política en cada extracción; (4) aumentar en 1 h la reserva de un servicio nunca aumenta la pérdida con extracciones fijas; (5) con duraciones iguales, las horas-cliente de SILO ≤ las de cada permutación. Eliminar el retardo de rearranque de un servicio *no* lo detecta ninguno de estos invariantes: reduce de forma coherente las pérdidas de todas las políticas. Lo detecta una **prueba unitaria** sobre un solo servicio: alimentador restablecido a las 5 h, reserva de 2 h → intervalo de interrupción esperado (2, 6). La puntuación completa extrae la lección: los invariantes prueban la estructura y las pruebas unitarias prueban la semántica; se necesitan ambos.

**EX025 — Métrica de detección relativa a la latencia.** Definición: para cada segmento anómalo *k* con inicio *s_k*, primera alarma *a_k* (el primer índice señalado en el segmento) y tiempo hasta el impacto *T_k*, el segmento queda «detectado antes del impacto» si *a_k* existe y (*a_k* − *s_k*) × Δ*t* < *T_k*. Con Δ*t* = 6 min y *T* = 2 h (20 pasos): la primera alarma del segmento 1 está en el desplazamiento de 21 pasos (2,1 h) → no; la del segmento 2 en el desplazamiento 0 → sí; la del segmento 3 en el desplazamiento de 29 pasos (2,9 h) → no. Fracción detectada antes del impacto = 1/3. Contraste: PA-F1 0,911, F1 puntual 0,05, PA%K 0,05. La métrica de latencia muestra que un detector sin información se adelanta a la reserva solo por azar, información que el PA-F1 oculta por completo.

**EX026 — Plan del piloto.** Un plan sólido enumera preguntas de factibilidad (tasa de reclutamiento, comprensión de los materiales, duración de las sesiones, captura de datos, tiempo de ejecución, pruebas de invariantes), fija umbrales como en el §4.7.2, especifica las respuestas ante un «detener» (revisar y repetir el piloto; cambiar la vía de reclutamiento; reducir el alcance), excluye a los participantes del piloto del estudio principal porque han visto los materiales y sus elecciones estarían contaminadas, y declara explícitamente que no se estimará ni se reportará como evidencia ningún tamaño del efecto.

### Capítulo 5: EX027–EX032

**EX027 — Ejecutar e interpretar el estudio principal.** La salida exacta está impresa en el §5.2.1. Cambio relativo de DEP frente a CRITFLAG: Riverbend 4,32 / 3,97 − 1 = +8,8 % (DEP ligeramente peor); Port Halvard 9,61 / 31,63 − 1 = −69,6 %. Párrafo modelo: «Respecto del orden de clientes primero, ambos órdenes conscientes de la criticidad redujeron la pérdida ponderada de servicios críticos en más del 80 % en las dos regiones sintéticas, mientras aumentaron las horas-cliente entre un 58 % y un 71 %, lo que supera el margen del 15 % declarado de antemano (H4a no se cumple). Respecto del orden por indicador crítico, el orden por tiempo hasta el impacto no produjo ninguna reducción en Riverbend (diferencia media +0,35, intervalo de Monte Carlo del 95 % de −0,23 a 0,97; se descarta una reducción del 10 %) y produjo una reducción del 70 % en Port Halvard, donde igualó al oráculo; las horas-cliente aumentaron un 2,3 % y un 9,9 % respectivamente, dentro del margen (H4b se cumple). Los intervalos reflejan solo el ruido de la simulación».

**EX028 — Pareado frente a no pareado.** Riverbend, 500 extracciones: DE de las pérdidas de DEP ≈ 6,36, de CRITFLAG ≈ 4,57, de las diferencias por extracción ≈ 6,79. Intervalo no pareado del 95 % para la diferencia de medias ≈ 0,35 ± 1,96 × √((6,36² + 4,57²)/500) ≈ −0,34 a 1,04; pareado ≈ −0,24 a 0,95. El pareo ayudó solo modestamente. Las pérdidas de las dos políticas están débilmente correlacionadas de forma positiva: en muchas extracciones una protege el agua y la otra las telecomunicaciones, de modo que sus pérdidas se mueven en direcciones distintas. La varianza de las diferencias, Var(A) + Var(B) − 2 Cov(A, B), puede por tanto superar la varianza de cualquiera de las políticas sin dejar de ser inferior a la suma no pareada. Los números aleatorios comunes siguen siendo correctos; su ganancia de precisión es una cuestión empírica.

**EX029 — Taxonomía de la incertidumbre.** (a) Monte Carlo: más extracciones. (b) Parámetros: obtención con incertidumbre, verificación de inventarios, análisis de sensibilidad. (c) Estructural: ampliación del modelo (tiempos de desplazamiento), comparación de estructuras de modelo. (d) Valores: conjuntos de pesos alternativos, reporte transparente de los veredictos por conjunto, deliberación con las partes interesadas. (e) Parámetros (familia de distribuciones) o estructural (si la forma refleja un mecanismo como el agotamiento): poner a prueba familias alternativas y reportar la sensibilidad.

**EX030 — Crítica del diseño del ejercicio de mesa.**

| Amenaza | Cambio | Costo |
|---|---|---|
| Características de la demanda (los participantes adivinan la respuesta «correcta») | Incluir escenarios de relleno en los que DEP no sea óptimo; planteamiento neutral | Sesiones más largas |
| Muestra pequeña, tres empresas de servicios | Reclutar en más empresas de servicios, estratificadas por tamaño | Esfuerzo de reclutamiento; más acuerdos |
| Sin presión de tiempo ni fatiga | Decisiones cronometradas dentro de un ejercicio más largo; integrarlo en un simulacro programado de la empresa de servicios | Realismo frente a carga; consentimiento de los responsables del simulacro |
| Reconocimiento de escenarios isomorfos | Variar más los rasgos superficiales; separar las sesiones por días | Logística; abandono |
| Visualización probada solo combinada con información de tiempos | Añadir un tercer brazo: lista de indicadores con caminos mostrados pero sin tiempos | Se necesitan más participantes |
| Resultado puntuado con el mismo modelo usado para diseñar DEP | Puntuar las elecciones también con un panel experto independiente | Tiempo del panel |

**EX031 — Matriz de evidencia de validación.** Una respuesta sólida elige validez aparente, histórica, de condiciones extremas, de variabilidad de parámetros y operacional; reconoce con honestidad que la validación histórica de eventos cibernéticos poco frecuentes es imposible y la sustituye por eventos de todas las causas con un argumento de transferencia; e identifica la prueba más perjudicial —para el Estudio Cascada, la validación histórica del tiempo de las reservas, porque si las reservas son sistemáticamente erróneas, cambian todos los resultados de orden— y la programa antes del estudio principal.

**EX032 — Memorando de transportabilidad.** La empresa de servicios tiene tres alimentadores críticos cuyo orden por reservas coincide con su orden por clientes y una cuadrilla. Moderadores: divergencia nula; una cuadrilla; reservas desconocidas en relación con el tiempo de restablecimiento; exactitud del mapa desconocida. Predicción: el orden por tiempo hasta el impacto producirá el mismo orden que la lista crítica, de modo que la ganancia es nula. Salvedades: si los pesos o la ramificación (un alimentador que protege varios servicios ponderados) difieren, una regla consciente de los pesos podría seguir ayudando; eso queda fuera de la afirmación probada. Datos que cambiarían la predicción: reservas corregidas (que podrían cambiar el orden), evidencia de errores en el mapa o dependencias que no figuran en la lista.

### Capítulo 6: EX033–EX038

**EX033 — Informe del red team.** Las objeciones modelo son las del §6.2, más, por ejemplo, «el horizonte de 72 horas censura las interrupciones largas» (prueba: ampliar a 120 h y contar los servicios censurados) y «las distribuciones triangulares subestiman las colas» (prueba: reservas lognormales con medianas iguales). Cada objeción enuncia su predicción antes de la prueba; por ejemplo, «si la circularidad determina el resultado, un mapa erróneo eliminará la ventaja de DEP sobre SILO»: el capítulo 6 encontró que redujo la ventaja de pérdida de DEP sobre SILO de unas 48 a unas 7 horas-servicio ponderadas, mientras todas las políticas conscientes de la criticidad se degradaban.

**EX034 — Sensibilidad a los pesos.** Con todos los pesos fijados en 1,0 (500 extracciones, semilla 7): Riverbend SILO 15,00, CRITFLAG 1,32, DEP 1,07, ORACLE 0,54; DEP − CRITFLAG −0,25 (intervalo de Monte Carlo del 95 % de −0,41 a −0,08). Port Halvard SILO 14,95, CRITFLAG 8,61, DEP 2,49, ORACLE 2,49; DEP − CRITFLAG −6,12 (−6,24 a −6,00). Veredictos: H1 sin cambios (sustentada); H2 en Riverbend pasa de *rechazada* a *inconclusa* según la regla prerregistrada: la estimación puntual es una reducción del 19 %, pero el extremo superior del intervalo (−0,08) no queda completamente por debajo del umbral (−0,13); H2 en Port Halvard sin cambios (sustentada); H4 no se ve afectada (las horas-cliente no dependen de los pesos). Explicación: con los pesos declarados de antemano, restablecer primero F3 protege dos servicios con pesos altos (agua 4 y el hospital a través del agua 5), lo que favorece el orden de CRITFLAG; con pesos iguales, restablecer pronto las telecomunicaciones importa relativamente más y la regla de DEP del tiempo hasta el impacto más temprano sale ganando. Conclusión: el veredicto de Riverbend depende de los valores; la tesis debe reportar los veredictos por conjunto de pesos.

**EX035 — Experimento de error del mapa.** Telecomunicaciones realmente en F4, los planificadores creen que en F2 (300 extracciones, semilla 7, sin oráculo): SILO 29,01, CRITFLAG 26,82, DEP 31,11. Con un mapa correcto, CRITFLAG y DEP eligen ambos F4, F3, F2, F1 y llegan a 4,90. En comparación con el desajuste del agua (§6.3.1), el error de las telecomunicaciones perjudica todavía más a DEP: DEP pasa a ser la peor de las tres políticas, porque restablece con confianza primero F2 para una central de telecomunicaciones que no está allí. Procedimiento de auditoría: para cada instalación crítica de la lista, verificación de campo por muestreo del alimentador que la abastece cada año y tras cualquier reconfiguración de la red; objetivo de exactitud ≥ 98 % en una muestra aleatoria de al menos 50 pares instalación-alimentador (o todos, si hay menos); aprobación del responsable; discrepancias corregidas en 30 días; resultados de la auditoría almacenados en un nivel controlado.

**EX036 — Crítica del generador.** Implementando «los alimentadores más grandes albergan servicios con reservas más largas» (asignar los niveles de reserva ordenados a los alimentadores críticos ordenados por clientes, la reserva más pequeña al alimentador más pequeño; 200 regiones, semilla 2026): las regiones sin divergencia caen de 69 a 9; divergencia en dos posiciones, 77 regiones, ganancia media −24,85; divergencia en tres posiciones, 114 regiones, ganancia media −19,02. La correlación opuesta (la reserva más corta en el alimentador más grande) da 162 regiones sin divergencia, 35 con dos posiciones (ganancia media −8,65) y 3 con tres (−17,24). Interpretación: es el supuesto de correlación del generador, y no el método, el que controla con qué frecuencia ayuda DEP. La afirmación debe seguir condicionada a la divergencia medida, y la frecuencia en regiones reales debe medirse, no simularse.

**EX037 — Decisión de doble uso.** (a) *Restringir y notificar*: específico, accionable, gran ventaja para el adversario; divulgación coordinada a través del proveedor y de un coordinador; notificar a las empresas de servicios afectadas por los canales adecuados; publicar solo hallazgos agregados tras la remediación. (b) *Publicar*: patrón general ampliamente tratado en avisos públicos; valor defensivo alto. (c) *Publicar con cuidado*: el método ayuda a los planificadores; evite publicar flujos listos para usar que ingieran datos públicos de instalaciones de lugares con nombre. (d) *Retener o restringir*: las estimaciones para hospitales con nombre son datos para seleccionar objetivos, con poco valor defensivo más allá de esos hospitales; compártalas en privado con ellos si son exactas.

**EX038 — Carta de respuesta.** Respuestas modelo: (1) circularidad: *aceptada en parte*; se añaden pruebas de desajuste, la afirmación se condiciona a la exactitud del mapa y se recomienda una auditoría del mapa. (2) Reservas cortas: *aceptada como condición de contorno*; se añade el escalado de reservas y la afirmación se limita a reservas más cortas que alrededor del doble del tiempo de restablecimiento. (3) Selección del contexto: *aceptada en parte*; se añade el análisis de 200 regiones, la afirmación se limita a la divergencia medida y la frecuencia en regiones reales figura como desconocida. (4) Debilidad de la heurística: *aceptada*; la regla consciente de los pesos se presenta como trabajo futuro exploratorio, no como resultado. (5) Doble uso: *aceptada*; se añade la revisión de doble uso; la recomendación sobre los datos de prioridad de restablecimiento se publica a nivel general tras la coordinación. Cada respuesta cita la sección modificada.

### Capítulo 7: EX039–EX044

**EX039 — Mapa del argumento.** Afirmación, datos, garantía, respaldo, cualificador y refutaciones como en el §7.1, con los capítulos: datos (capítulos 5–6), garantía (verificación del capítulo 4 y validación del capítulo 5), respaldo (reproducciones y pruebas del capítulo 4), cualificador (alcance del capítulo 3 más las condiciones del capítulo 6), refutaciones (capítulo 6 y Limitaciones). Garantía más débil: que el modelo clasifica los órdenes de forma adecuada para regiones *reales*, ya que la validación histórica cubre un solo evento de todas las causas y omite las reservas humanas. Refuerzo: validación del tiempo de las reservas frente a varios registros posteriores a la acción, con las reservas humanas modeladas explícitamente.

**EX040 — Asignación de niveles.** Código del simulador T0; pruebas de verificación T0; configuración de Riverbend T0 (inventada); formularios de obtención con nombres de socios T3 (o T2 si los socios consienten el acceso controlado): transformarlos eliminando las identidades y agregando para llevarlos a T1; rangos de obtención agregados T1 (T0 si los socios están de acuerdo y no queda ninguna estructura única); audio del ejercicio de mesa T2: destruirlo tras la transcripción si el consentimiento así lo indica; justificaciones codificadas T2, o T1 tras la desidentificación y la eliminación de las combinaciones de función y empresa de servicios; formularios de consentimiento T2 (administrativos, nunca se publican); procedimiento de restablecimiento del socio T3: describir solo su existencia y su función; figuras finales T0.

**EX041 — Manifiesto que falla de forma cerrada.** Con el orden original de las reglas, `data/synthetic_partner_feeders.csv` coincide primero con `partner_` y se clasifica como T3 (correcto). Mover la regla `synthetic_` al primer lugar lo clasifica como T0-public (incorrecto): un peligro de orden. Una comprobación de contenido: antes de asignar T0, leer los bytes y negar T0 si aparece `b"SUB-"` (o cualquier patrón de una lista de formatos de identificadores de activos), devolviendo "UNCLASSIFIED: stop and review". Lección: ponga primero las reglas más restrictivas, falle de forma cerrada cuando no haya coincidencia y compruebe el contenido además de los nombres.

**EX042 — Evaluación del riesgo residual de divulgación.** Riesgo: la configuración (un hospital, dos plantas de agua, cinco alimentadores, el hospital en un alimentador concreto) es una huella estructural casi única del condado; alguien con conocimiento local podría hacerla corresponder. Una correspondencia revelaría qué alimentador abastece al hospital y las reservas obtenidas: información para seleccionar objetivos. Transformaciones: mezclar estructuras de varios condados; generalizar a rangos; eliminar el vínculo alimentador-hospital y sustituirlo por una asignación aleatoria que preserve solo el estadístico de interés (por ejemplo, la distribución de la divergencia). Costo: vínculo más débil con el caso real; la tesis debe indicar qué resultados dependen de la estructura preservada.

**EX043 — Documentación del modelo.** Propósito: clasificar los órdenes de restablecimiento por la pérdida ponderada de servicios críticos y las horas-cliente en interrupciones de distribución que requieren restablecimiento manual secuencial. Entidades: alimentadores (clientes, duración del restablecimiento), servicios (alimentador, reserva, peso, dependencia opcional con reserva en el sitio), cuadrillas. Procesos y programación: las cuadrillas toman los alimentadores en el orden de la política en cuanto quedan libres; los intervalos de interrupción de los servicios se calculan de forma exacta desde el vencimiento de la reserva hasta el restablecimiento más un retardo de rearranque de una hora; los intervalos de dependencia empiezan en el inicio de la interrupción del proveedor más la reserva en el sitio y terminan con el restablecimiento del proveedor; los intervalos se recortan a 72 h; las dependencias tienen semántica «O». Entradas: distribuciones triangulares procedentes de la obtención; pesos del panel de gestión de emergencias. Verificación: los invariantes y las pruebas unitarias del EX024. Limitaciones: sin tiempo de desplazamiento; sin ampliación humana de las reservas; solo semántica «O»; reservas fijas (sin dinámica de agotamiento); una sola clase de escenario.

**EX044 — Sección de limitaciones.** Una respuesta sólida se parece al §7.7, con cinco o más limitaciones, cada una con su efecto, su dirección y el estudio que la resolvería, y las ordena: (1) reservas humanas omitidas (podrían reducir todos los beneficios de reordenar), (2) regiones sintéticas (frecuencia de la divergencia desconocida), (3) pesos (los veredictos cambian), (4) tiempo de desplazamiento (reduce el beneficio de DEP donde los alimentadores críticos están dispersos), (5) escala del ejercicio de mesa (adopción no demostrada).

### Capítulo 8: EX045–EX050

**EX045 — Auditoría de las afirmaciones.** La salida original señala K2, K3 y K4 (véase el §8.1.1). K5 se reporta como "OK" porque no aparece ninguna de las palabras clave. Comprobación mejorada: ampliar `OVERREACH` con expresiones como "the grid", "resilient to", "makes", "secure", o, mejor aún, exigir una expresión de alcance explícita («en el modelo sintético…») en el texto de cualquier afirmación cuyo campo de alcance contenga "synthetic". K5 corregida: «En dos regiones sintéticas, el orden de restablecimiento por tiempo hasta el impacto redujo la pérdida modelada de servicios críticos tras interrupciones de distribución en condiciones enunciadas; no previene ciberataques, y su efecto en redes reales no se ha probado».

**EX046 — Banco de preguntas de los examinadores.** Las tres más difíciles para el Estudio Cascada, con respuestas modelo: (1) «¿No es circular el resultado?»: responda con la evidencia del desajuste y del modelador independiente, y admita lo que sigue siendo circular (ORACLE y DEP siguen compartiendo el modelo). (2) «¿Por qué debería alguien aceptar sus pesos?»: no debería hacerlo sin examinarlos; describa la obtención y la tabla de veredictos por conjunto de pesos; los pesos son una entrada de política que el método hace explícita. (3) «Sin un estudio de campo, ¿qué sabe usted de las empresas de servicios reales?»: que las condiciones del beneficio son medibles; que la encuesta sobre la divergencia es el siguiente estudio; que no se hace ninguna afirmación de campo. Un vacío real revelado: la tesis no tiene evidencia sobre si las cuadrillas pueden seguir un plan reordenado dados los tiempos de desplazamiento; es un vacío del trabajo, que debe enunciarse como limitación.

**EX047 — Plan de publicación.** Como en el §8.3.1, con: el archivo T0 v1.0 publicado con el artículo 1; los artículos 2–4 citando versiones del archivo; la revisión de doble uso y la coordinación sectorial completadas antes de cualquier preprint del artículo 2; los plazos de preaviso de los socios respetados para los artículos que usan rangos de obtención; y una declaración en cada artículo de su alcance respecto de la afirmación general de la tesis.

**EX048 — Enrutamiento de la divulgación.**

| Hallazgo | Tipo | Vía y momento | Publicado |
|---|---|---|---|
| (a) El socio expone su lista de clientes críticos | Propio de una organización | Informe privado inmediato según el acuerdo de uso de datos; confirmar la corrección | Nunca de forma identificable; quizá una nota general de que las listas de prioridades necesitan control de acceso |
| (b) Importaciones de configuración sin firmar en un producto comercial | Vulnerabilidad de un producto | CVD con el proveedor, directamente o mediante un coordinador; publicación tras la remediación o según la política del coordinador | Descripción a nivel de aviso tras la coordinación |
| (c) Inventarios de reservas en papel frente a físicos | Propio de una organización y a nivel sectorial | Informes privados a cada socio; después, publicación general de la brecha | Hallazgo agregado sin identidades |
| (d) Un único sitio repetidor para las radios de las cuadrillas | Propio de una organización con relevancia sectorial | Informe privado a la empresa de servicios; hallazgo general sobre los puntos únicos de falla en las comunicaciones de restablecimiento tras la coordinación | Solo el hallazgo general |

**EX049 — Resumen de políticas.** Un resumen sólido abre con el problema (el orden de restablecimiento determina qué servicios críticos fallan), enuncia cuatro recomendaciones con niveles de confianza y vínculos con la evidencia (§8.5), incluye un párrafo «Lo que esta investigación no muestra» (efectos en empresas de servicios reales, frecuencia de la divergencia, adopción bajo estrés, cualquier efecto de prevención de ciberataques), usa un lenguaje llano y enlaza con la tesis y con el archivo T0. Cada oración está marcada; las oraciones que no pueden rastrearse hasta la tesis se eliminan.

**EX050 — Programa de investigación posdoctoral.** Como en el §8.6: (1) encuesta sobre la divergencia: afirmación «la divergencia ocurre en al menos una cuarta parte de las empresas de servicios encuestadas», diseño con protección T3, colaboración con socios a través de asociaciones sectoriales, decisión que cambia: si promover o no el orden por tiempo hasta el impacto; (2) modelado de las reservas humanas: afirmación «incluir las entregas de combustible y de agua reduce el beneficio modelado de reordenar en menos de la mitad», validada frente a registros posteriores a la acción; (3) ataques a la integridad de los datos de planificación: afirmación «las auditorías de mapas con un 98 % de exactitud limitan a una cota enunciada la amplificación de la consecuencia de los datos de prioridad corrompidos». Orden: (1) primero, porque si la divergencia es poco frecuente, (2) y (3) importan más que seguir trabajando en el método. Resultado de parada: si la encuesta encuentra divergencia en muy pocas empresas de servicios y los errores de los mapas son poco frecuentes, el programa debería reorientarse de los métodos de ordenación a la verificación de las reservas.

<a id="glossary"></a>

## Glosario

- **Ajuste por punto (PA)** — Un protocolo de evaluación que cuenta como detectado todo un segmento anómalo si cualquiera de sus puntos se marca; se sabe que infla las puntuaciones (Kim et al., 2022).
- **Censura** — Observación incompleta de una duración porque la ventana de observación se cerró antes de que ocurriera el evento (por ejemplo, la recuperación).
- **Circularidad modelo–política** — Evaluar una política en el mismo modelo del que se derivó, de modo que los errores del modelo no pueden aparecer como fallas de la política.
- **Consecuencia** — El efecto de una perturbación sobre las personas y las funciones de las que dependen, medido en unidades de servicio dentro de una ventana temporal.
- **Curva de desempeño** — La fracción del servicio normal prestada a lo largo del tiempo antes, durante y después de una perturbación.
- **Dependencia / interdependencia** — Una relación unidireccional / bidireccional en la que el estado de un servicio depende del de otro (Rinaldi, Peerenboom y Kelly, 2001).
- **Divergencia** — El número de posiciones en que dos órdenes de restablecimiento difieren entre los alimentadores críticos; en este libro, el moderador de la ventaja de DEP sobre CRITFLAG.
- **Función crítica** — Una función del gobierno o del sector privado cuya interrupción tendría un efecto debilitante sobre la seguridad, la economía, la salud pública o la seguridad física; el National Critical Functions set de CISA enumera 55.
- **Margen de no inferioridad** — El mayor empeoramiento de una métrica secundaria o de seguridad que se acepta a cambio de un beneficio en la métrica primaria, fijado de antemano.
- **Menor efecto de interés** — El menor efecto que cambiaría una decisión real, justificado por su consecuencia práctica y fijado antes del análisis.
- **Modelo de insumo-producto de inoperabilidad (IIM)** — Un modelo lineal basado en Leontief de la propagación de la inoperabilidad de equilibrio entre sectores (Haimes y Jiang, 2001).
- **Nivel de divulgación** — El nivel de acceso (público, registrado, controlado, retenido) con el que se pone a disposición un artefacto del archivo.
- **Nivel de seguridad objetivo (SL-T)** — En IEC 62443-3-2, el nivel de seguridad deseado para una zona o un conducto, determinado mediante la evaluación de riesgos.
- **Números aleatorios comunes** — Evaluar cada política comparada con las mismas extracciones simuladas, de modo que las comparaciones sean pareadas.
- **Orden consciente de las dependencias (DEP)** — En este libro, restablecer los alimentadores en orden creciente del tiempo hasta el impacto esperado más temprano de los servicios críticos que sostienen.
- **Orden oráculo** — El mejor orden para una extracción dada, hallado por enumeración exhaustiva; una cota superior de lo que cualquier regla podría lograr.
- **Orden por clientes (SILO)** — En este libro, restablecer los alimentadores en orden decreciente de clientes atendidos; óptimo para los clientes-hora con duraciones iguales (regla de Smith).
- **Orden por indicador crítico (CRITFLAG)** — En este libro, restablecer primero los alimentadores que abastecen instalaciones críticas enumeradas, ordenados entre sí por clientes atendidos.
- **Pérdida de resiliencia** — El área entre el servicio pleno y la curva de desempeño dentro de una ventana.
- **Reproducción / replicación** — Obtener resultados coherentes con los mismos datos y métodos / con datos nuevos que abordan la misma pregunta (National Academies, 2019).
- **Reserva** — Capacidad almacenada (combustible, baterías, almacenamiento de agua, inventario, procedimientos manuales) que permite a un dependiente seguir operando después de perder a un proveedor, durante un tiempo que depende de la carga.
- **Revisión de doble uso** — Evaluación, antes de publicar, de la ventaja que un resultado de investigación da a los adversarios, su valor defensivo y las mitigaciones posibles.
- **Servicio crítico** — Un servicio cuya interrupción más allá de una duración declarada daña la salud, la seguridad, la protección o la actividad económica esencial de una población declarada.
- **Tiempo hasta el impacto** — El tiempo, después de una falla inicial, en que falla un servicio dependiente, calculado sobre todas las rutas de dependencia.
- **Verificación / validación** — Demostrar que un modelo está implementado correctamente / que es adecuado para su propósito previsto (Sargent, 2013).
- **Zonas y conductos** — En IEC 62443, agrupaciones de activos con requisitos de seguridad comunes y de los canales de comunicación entre ellos.

<a id="references"></a>

## Referencias

Las normas, los reglamentos y los instrumentos de política cambian. Las versiones y fechas que siguen son las consultadas para este borrador (octubre de 2026); vuelva a verificarlas antes de basarse en ellas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

**Política, derecho y normas**

- Bank for International Settlements, Committee on Payments and Market Infrastructures, and International Organization of Securities Commissions. [Guidance on Cyber Resilience for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d146.htm). June 2016.
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set). April 2019.
- Cybersecurity and Infrastructure Security Agency. [National Security Memorandum on Critical Infrastructure Security and Resilience (overview)](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Congressional Research Service. [The 2024 National Security Memorandum on Critical Infrastructure Security and Resilience](https://www.congress.gov/crs-product/IF12716). IF12716.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- Federal Energy Regulatory Commission. [Critical Infrastructure Protection Reliability Standard CIP-015-1 — Cyber Security — Internal Network Security Monitoring](https://www.federalregister.gov/documents/2025/07/02/2025-12309/critical-infrastructure-protection-reliability-standard-cip-015-1-cyber-security-internal-network). Order No. 907, *Federal Register*, 2 July 2025.
- International Electrotechnical Commission. [IEC 62443-3-2:2020, Security for industrial automation and control systems — Part 3-2: Security risk assessment for system design](https://webstore.iec.ch/en/publication/30727).
- Inside Privacy (Covington & Burling). [CISA Submits Final CIRCIA Rule for OMB Review](https://www.insideprivacy.com/critical-infrastructure/cisa-submits-final-circia-rule-for-omb-review/). October 2026. (Secondary source on regulatory status.)
- NERC. [CIP-015-1 standard page](https://www.nerc.com/standards/reliability-standards/cip/cip-015-1).
- NIST. [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29). NIST CSWP 29, February 2024.
- NIST. Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST SP 800-160 Vol. 2 Rev. 1, December 2021.
- NIST. Stouffer, K., Pease, M., Tang, C., Zimmerman, T., Pillitteri, V., Lightman, S., Hahn, A., Saravia, S., Sherule, A., and Thompson, M. [Guide to Operational Technology (OT) Security](https://doi.org/10.6028/NIST.SP.800-82r3). NIST SP 800-82 Rev. 3, September 2023. [CSRC page with Rev. 4 draft note](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- The White House. [National Security Memorandum on Critical Infrastructure Security and Resilience (NSM-22)](https://www.govinfo.gov/content/pkg/DCPD-202400358/html/DCPD-202400358.htm). 30 April 2024.

**Informes de incidentes y amenazas**

- CISA. [CrashOverride Malware (TA17-163A)](https://www.cisa.gov/news-events/alerts/2017/06/12/crashoverride-malware). June 2017.
- CISA. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf).
- CISA and partners. [PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a). February 2024.
- E-ISAC and SANS ICS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). 18 March 2016 (archived copy at the National Security Archive).
- Langner, R. [To Kill a Centrifuge: A Technical Analysis of What Stuxnet's Creators Tried to Achieve](https://archive.org/details/to-kill-a-centrifuge). The Langner Group, November 2013 (Internet Archive copy).

**Infraestructura, resiliencia y modelización**

- Bochman, A. A., and Freeman, S. [Countering Cyber Sabotage: Introducing Consequence-Driven, Cyber-Informed Engineering (CCE)](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710). CRC Press, 2021.
- Bruneau, M., Chang, S. E., Eguchi, R. T., Lee, G. C., O'Rourke, T. D., Reinhorn, A. M., Shinozuka, M., Tierney, K., Wallace, W. A., and von Winterfeldt, D. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra* 19(4), 2003.
- Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., and Havlin, S. [Catastrophic Cascade of Failures in Interdependent Networks](https://doi.org/10.1038/nature08932). *Nature* 464, 2010.
- Goh, J., Adepu, S., Junejo, K. N., and Mathur, A. [A Dataset to Support Research in the Design of Secure Water Treatment Systems](https://doi.org/10.1007/978-3-319-71368-7_8). CRITIS 2016, LNCS 10242.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis* 29(4), 2009.
- Haimes, Y. Y., and Jiang, P. [Leontief-Based Model of Risk in Complex Interconnected Infrastructures](https://doi.org/10.1061/(ASCE)1076-0342(2001)7:1(1)). *Journal of Infrastructure Systems* 7(1), 2001.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- Lenstra, J. K., Rinnooy Kan, A. H. G., and Brucker, P. [Complexity of Machine Scheduling Problems](https://doi.org/10.1016/S0167-5060(08)70743-X). *Annals of Discrete Mathematics* 1, 1977.
- Neprash, H. T., McGlave, C. C., et al. [Trends in Ransomware Attacks on US Hospitals, Clinics, and Other Health Care Delivery Organizations, 2016–2021](https://doi.org/10.1001/jamahealthforum.2022.4873). *JAMA Health Forum* 3(12), 2022.
- Ouyang, M. [Review on Modeling and Simulation of Interdependent Critical Infrastructure Systems](https://doi.org/10.1016/j.ress.2013.06.040). *Reliability Engineering & System Safety* 121, 2014.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine* 21(6), 2001.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation* 7(1), 2013.
- Smith, W. E. [Various Optimizers for Single-Stage Production](https://doi.org/10.1002/nav.3800030106). *Naval Research Logistics Quarterly* 3(1–2), 1956.
- Taormina, R., et al. [Battle of the Attack Detection Algorithms: Disclosing Cyber Attacks on Water Distribution Networks](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969). *Journal of Water Resources Planning and Management* 144(8), 2018.

**Métodos de investigación, evaluación e integridad**

- Arp, D., Quiring, E., Pendlebury, F., Warnecke, A., Pierazzi, F., Wressnegger, C., Cavallaro, L., and Rieck, K. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). USENIX Security Symposium, 2022.
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- Gebru, T., Morgenstern, J., Vecchione, B., Wortman Vaughan, J., Wallach, H., Daumé III, H., and Crawford, K. [Datasheets for Datasets](https://doi.org/10.1145/3458723). *Communications of the ACM* 64(12), 2021.
- Grimm, V., et al. [A Standard Protocol for Describing Individual-Based and Agent-Based Models](https://doi.org/10.1016/j.ecolmodel.2006.04.023). *Ecological Modelling* 198(1–2), 2006.
- Kerr, N. L. [HARKing: Hypothesizing After the Results Are Known](https://doi.org/10.1207/s15327957pspr0203_4). *Personality and Social Psychology Review*, 1998.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *Proceedings of the AAAI Conference on Artificial Intelligence* 36(7), 2022.
- Leon, A. C., Davis, L. L., and Kraemer, H. C. [The Role and Interpretation of Pilot Studies in Clinical Research](https://doi.org/10.1016/j.jpsychires.2010.10.008). *Journal of Psychiatric Research* 45(5), 2011.
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., and Gebru, T. [Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596). FAT* 2019.
- National Academies of Sciences, Engineering, and Medicine. [Reproducibility and Replicability in Science](https://doi.org/10.17226/25303). 2019.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *PNAS*, 2018.
- O'Hagan, A., Buck, C. E., Daneshkhah, A., Eiser, J. R., Garthwaite, P. H., Jenkinson, D. J., Oakley, J. E., and Rakow, T. [Uncertain Judgements: Eliciting Experts' Probabilities](https://doi.org/10.1002/0470033312). Wiley, 2006.
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. [The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews](https://doi.org/10.1136/bmj.n71). *BMJ*, 2021.
- Pearl, J., and Bareinboim, E. [External Validity: From Do-Calculus to Transportability Across Populations](https://doi.org/10.1214/14-STS486). *Statistical Science* 29(4), 2014.
- Saltelli, A., Ratto, M., Andres, T., Campolongo, F., Cariboni, J., Gatelli, D., Saisana, M., and Tarantola, S. [Global Sensitivity Analysis: The Primer](https://doi.org/10.1002/9780470725184). Wiley, 2008.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology* 9(10), 2013.
- Simmons, J. P., Nelson, L. D., and Simonsohn, U. [False-Positive Psychology](https://doi.org/10.1177/0956797611417632). *Psychological Science*, 2011.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). IEEE Symposium on Security and Privacy, 2010.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. [The FAIR Guiding Principles for Scientific Data Management and Stewardship](https://doi.org/10.1038/sdata.2016.18). *Scientific Data*, 2016.

Material complementario de CyberABC: el [libro doctoral de respuesta a incidentes](../../../incident-response-resilience/en/book/MANUSCRIPT.md) (la escalera de afirmaciones y los métodos de integridad de la investigación que reutiliza el capítulo 1) y el [curso doctoral de seguridad de TO, IoT y sistemas ciberfísicos](../../../ot-iot-security/README.md) (la capa de los sistemas de control).

**Límite del caso.** La Región de Riverbend, Port Halvard, Riverbend Electric Cooperative, Riverbend Water Authority, St. Calder Hospital, Meridian Telecom, GridWater-Sim, los estudios P1–P8, los participantes P01–P12, el Estudio Cascada y todos los números que producen los laboratorios son inventados con fines didácticos. Las fuentes respaldan los enunciados generales junto a los que se citan, nunca los detalles sintéticos.

**Metadatos de la edición.** Edición en borrador en español, octubre de 2026, traducida de la edición de referencia en inglés. Revisor: pendiente. Verificación A4 para publicación: pendiente; una comprobación preliminar de maquetación consta en [la revisión de avance](../../../../../STRUCTURE_REVIEW.md#a4-preflight).
