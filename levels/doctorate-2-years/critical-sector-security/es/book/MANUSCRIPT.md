# Infraestructura crítica y seguridad sectorial: métodos de investigación doctoral y práctica de la tesis

- Idioma: español (`es`), edición en español neutro internacional; programa de investigación doctoral, dos años; aproximadamente 1600 horas de estudio planificado (curso 207 de 207, el último curso de la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador parcial en español**. El capítulo 1 de 8 está escrito en español, con los ejercicios EX001–EX007 y sus resultados resueltos, y su laboratorio produce una salida idéntica a la de la edición en inglés; los capítulos 2–8 (EX008–EX050) están, por ahora, solo en la [edición en inglés](../../en/book/MANUSCRIPT.md#ch-02) y se añadirán por lotes. Siguen abiertas la revisión independiente de la materia, la nueva verificación de las fuentes, la revisión de accesibilidad, la revisión lingüística y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
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
2. [Infraestructura crítica y seguridad sectorial: frontera de la investigación](../../en/book/MANUSCRIPT.md#ch-02): panorama de políticas y normas, familias de modelos de interdependencia, investigación sobre detección y bancos de pruebas, evidencia específica de cada sector y una brecha falsable.
3. [Propuesta de contribución original](../../en/book/MANUSCRIPT.md#ch-03): mecanismo, grafos de dependencias con reservas, hipótesis, líneas base, explicaciones rivales y condiciones de falla declaradas de antemano.
4. [Replicación de las líneas base y piloto](../../en/book/MANUSCRIPT.md#ch-04): reproducción de un modelo de inoperabilidad y de un banco de referencia de detección, trampas de la evaluación, verificación del modelo y un piloto acotado.
5. [Estudio principal y validación independiente](../../en/book/MANUSCRIPT.md#ch-05): experimentos de simulación con incertidumbre, estudios de mesa con operadores, validación frente a la historia y a expertos, y un segundo contexto.
6. [Crítica de pares y revisión](../../en/book/MANUSCRIPT.md#ch-06): circularidad modelo–política, condiciones de contorno, desajuste del modelo, resultados negativos, revisión de doble uso y acotación de las afirmaciones.
7. [Síntesis de la tesis y archivo de reproducibilidad](../../en/book/MANUSCRIPT.md#ch-07): estructura argumental, divulgación de artefactos por niveles según las reglas de información de infraestructura, datos sintéticos y documentación del modelo.
8. [Defensa y plan de publicación](../../en/book/MANUSCRIPT.md#ch-08): auditoría de las afirmaciones, preparación de la defensa, foros de publicación, divulgación coordinada, traducción a políticas y el programa de investigación posdoctoral.

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

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](../../en/book/MANUSCRIPT.md#ch-02)

Continúe con la siguiente lección escrita.
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
