# Infraestructura crítica y seguridad sectorial: práctica especializada avanzada

- Idioma: español neutro (`es`); curso de posgrado de especialización, dos años; aproximadamente 600 horas de estudio planificado (curso 161 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–12 de 12 tienen texto didáctico escrito, doce laboratorios sin conexión, los ejercicios EX001–EX060 y sus resultados resueltos correspondientes. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: profesionales con experiencia (ingenieros de seguridad, responsables de TO y de TI, responsables de riesgo y resiliencia, auditores, personal técnico de los reguladores y consultores) que ya trabajan en un servicio esencial o cerca de él y ahora tienen que **liderar** las decisiones de seguridad de toda una organización o de un grupo de operadores interdependientes. Conocimientos de entrada: un primer título universitario o una experiencia profesional equivalente en el campo; conocimientos prácticos de redes, identidad, gestión de incidentes y al menos un sector operativo; soltura con proporciones, valores esperados e intervalos de confianza; y la capacidad de ejecutar un script breve de Python.
- En qué se diferencia este curso de sus vecinos. El [libro de grado](../../../../bachelors-4-years/critical-sector-security/es/book/MANUSCRIPT.md) construye los fundamentos asignatura por asignatura. El [libro de ingeniería](../../../../engineering-5-years/critical-sector-security/es/book/MANUSCRIPT.md) diseña, construye y verifica sistemas. El [libro de maestría](../../../../masters-2-years/critical-sector-security/es/book/MANUSCRIPT.md) diseña y defiende un estudio empírico; el [libro de doctorado](../../../../doctorate-2-years/critical-sector-security/es/book/MANUSCRIPT.md) hace una contribución original a la investigación. **Este libro de posgrado trata del juicio profesional avanzado**: tomar, justificar, evaluar y asumir decisiones a escala de la organización en condiciones de incertidumbre, con evidencias lo bastante buenas para un consejo de administración, un regulador y las personas que dependen del servicio. Lee investigación para usarla, no para producirla, y construye sistemas solo lo necesario para comparar y probar opciones de diseño.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este curso es un proyecto educativo independiente. No es un programa de posgrado acreditado, no otorga ninguna titulación y no concede autorización para acceder, escanear, probar o estudiar ninguna infraestructura, operador, conjunto de datos o persona reales. Toda organización, lugar, persona, registro, coste, probabilidad y resultado numérico de un ejemplo resuelto es **sintético**, salvo que una frase cite explícitamente una fuente pública. Nada de lo que aparece en este libro es un procedimiento operativo para una empresa de servicios, un hospital, un puerto o una red eléctrica reales, y nada constituye asesoramiento jurídico, clínico o regulatorio.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los doce capítulos siguen el trabajo de un especialista a lo largo de dos años. La etapa 1 (capítulos 1–3) construye los tres hábitos en los que descansa todo lo demás: decidir bien en condiciones de incertidumbre, saber qué exige realmente la buena práctica actual en cada sector y producir evidencias especializadas que resistan el escrutinio. La etapa 2 (capítulos 4–6) los aplica a las partes más difíciles del trabajo: el riesgo cuantificado con su distribución ética, la elección entre arquitecturas y la evaluación de los controles antes de confiar en ellos. La etapa 3 (capítulos 7–9) pasa a la organización: integrar la seguridad en las operaciones, los proveedores y los dispositivos regionales de emergencia; gestionar casos en los que todas las opciones perjudican a alguien; y liderar y asegurar una función de seguridad. La etapa 4 (capítulos 10–12) cierra el ciclo: leer de forma crítica la investigación y las afirmaciones de los proveedores, realizar un proyecto aplicado con una evaluación honesta y transferir lo aprendido a otro sector.

Cada capítulo tiene resultados de aprendizaje, secciones didácticas con definiciones, un ejemplo resuelto, una actividad práctica con un laboratorio en Python, una lista de errores comunes y límites, cinco ejercicios numerados y una síntesis. Los laboratorios usan solo la biblioteca estándar de Python 3 (las salidas de este borrador se produjeron con Python 3.13); no necesitan red, paquetes ni datos reales, y cada salida está impresa en el texto para que pueda comprobar su ejecución. Escriba su respuesta a cada ejercicio antes de abrir los [resultados resueltos](#worked-results). Muchos ejercicios tienen más de una respuesta defendible: el resultado resuelto muestra una, y la rúbrica muestra lo que premiaría un evaluador con experiencia.

Mantenga cinco etiquetas en cada nota de trabajo: **observación** (lo que registró una fuente identificada), **inferencia** (lo que usted concluye y con qué supuestos), **juicio** (lo que usted sopesa cuando se agota la evidencia), **decisión** (lo que alguien eligió, con autoridad para elegirlo) y **consecuencia** (el efecto sobre las personas que dependen del servicio). El fallo más común en el nivel de especialista no es desconocer un control; es una recomendación segura de sí misma cuyas evidencias, supuestos y responsable no pueden encontrarse después.

### El escenario sintético de este libro

| Elemento sintético | Papel en el libro | Límite |
|---|---|---|
| **Merrow Bay**: una región costera de unas 230.000 personas | Escenario de todos los ejemplos resueltos. | Región inventada. |
| **Merrow Water (MW)**: agua potable y aguas residuales; plantas de tratamiento en Hollin, Fenley, Upper Merrow, Kettle Ford, Ashby, Saltings y seis emplazamientos más pequeños | La organización en la que el lector es **especialista principal de seguridad**, depende del director de Operaciones y tiene una línea de dependencia funcional con el responsable de seguridad de la información (CISO). | Inventada; ninguna empresa de servicios, personal ni sistema reales. |
| **Merrow Health (MH)**, **Merrow Energy Networks (ME)**, **Port of Merrow (PoM)** | Operadores vecinos que comparten proveedores, energía y telecomunicaciones con MW. | Inventados. |
| **Merrow Bay Resilience Forum (MBRF)** | Grupo regional multiagencia de planificación de emergencias. | Inventado. |
| Proveedores **Corvane Systems**, **Lumen Watch**, **BayTel**, **Halden Cloud** | Integrador de SCADA, proveedor de detección gestionada, operador de telecomunicaciones, alojamiento en la nube. | Empresas inventadas; cualquier parecido con empresas reales es casual. |
| El consejo de administración, los reguladores, la cuenta «vendor-svc», cada coste, probabilidad, línea de registro y tiempo de simulacro | Contexto de decisión de los ejercicios. | Valores inventados, elegidos con fines didácticos. |

Como los datos son sintéticos, el libro puede decirle a veces lo que un operador real nunca sabe; por ejemplo, cuál de dos explicaciones generó un registro. Use ese privilegio para aprender cómo fallan los métodos, nunca como evidencia sobre organizaciones reales.

### Política de fuentes

Toda afirmación factual sobre una ley, una norma, un incidente público o un estudio publicado enlaza con una fuente consultada en octubre de 2026. Las leyes, las normas y las orientaciones cambian: cada una se cita con su versión o fecha y debe volver a verificarse antes de basarse en ella, y nada de lo que aquí aparece interpreta una ley para una organización concreta. Cuando una afirmación es vocabulario profesional o estadístico estándar (por ejemplo, que el valor esperado pondera cada resultado por su probabilidad), el texto lo indica en lugar de inventar una referencia. Una cita respalda la afirmación general que la acompaña, nunca los detalles sintéticos. Los incidentes públicos se describen solo con el nivel de detalle que publicaron sus autores y, cuando un primer relato se revisó después, se citan ambos.

## Contenido

1. [Toma de decisiones de seguridad avanzada](#ch-01): plantear decisiones, objetivos en unidades de servicio, valor esperado, arrepentimiento y robustez, valor de la información, sesgos y el registro de decisión.
2. [Infraestructura crítica y seguridad sectorial: práctica actual](#ch-02): qué exigen las líneas base y los regímenes en los distintos sectores, cobertura declarada frente a verificada y priorización por consecuencias.
3. [Infraestructura crítica y seguridad sectorial: evidencia especializada](../../en/book/MANUSCRIPT.md#ch-03): evidencia en entornos de TO y mixtos, relojes y cronologías, preservación sin perturbar el proceso y hallazgos que separan la observación de la inferencia.
4. [Riesgo y ética avanzados](../../en/book/MANUSCRIPT.md#ch-04): riesgo cuantificado con incertidumbre, excedencia de pérdidas, apetito de riesgo en unidades de servicio y quién soporta el riesgo residual.
5. [Infraestructura crítica y seguridad sectorial: alternativas de diseño](../../en/book/MANUSCRIPT.md#ch-05): comparar arquitecturas como grafos de ataque y como sistemas operables, modos de fallo de los controles y registros de decisiones de arquitectura.
6. [Infraestructura crítica y seguridad sectorial: evaluación controlada](../../en/book/MANUSCRIPT.md#ch-06): probar las detecciones y los simulacros antes de confiar en ellos, intervalos, carga de falsas alarmas y diseño seguro de las pruebas.
7. [Infraestructura crítica y seguridad sectorial: integración organizativa](../../en/book/MANUSCRIPT.md#ch-07): modelos operativos, propiedad, concentración de proveedores e integración con la gestión de emergencias.
8. [Infraestructura crítica y seguridad sectorial: casos difíciles](../../en/book/MANUSCRIPT.md#ch-08): cascadas, prioridades de restablecimiento, actualizaciones de confianza defectuosas, internos ambiguos y obligaciones en conflicto.
9. [Infraestructura crítica y seguridad sectorial: liderazgo y aseguramiento](../../en/book/MANUSCRIPT.md#ch-09): liderar una función, informes al consejo, casos de aseguramiento, frescura de la evidencia y distinguir la señal del ruido.
10. [Lectura y crítica de la investigación](../../en/book/MANUSCRIPT.md#ch-10): leer estudios, avisos y afirmaciones de proveedores para decidir; denominadores, confusión y transferencia.
11. [Proyecto aplicado](../../en/book/MANUSCRIPT.md#ch-11): delimitar, ejecutar y evaluar con honestidad una mejora a escala de la organización.
12. [Revisión final y transferencia](../../en/book/MANUSCRIPT.md#ch-12): integrar el curso, transferir decisiones entre sectores y planificar la práctica continuada.

Apéndices: [Resultados resueltos y notas de evaluación](#worked-results) · [Glosario](#glossary) · [Referencias](#references).

<a id="ch-01"></a>

## Capítulo 1 — Toma de decisiones de seguridad avanzada

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Plantear una decisión de seguridad a escala de la organización: quién decide, para cuándo, entre qué opciones y frente a qué objetivos.
2. Expresar los objetivos en unidades del servicio esencial (horas de suministro perdidas, pacientes derivados, hogares afectados) y no solo en dinero o en número de controles.
3. Comparar opciones con el valor esperado, el peor caso y el minimax del arrepentimiento, y explicar cuándo es adecuada cada regla.
4. Comprobar cuán sensible es una recomendación a las probabilidades de las que estaba menos seguro e indicar el umbral en el que cambia.
5. Estimar el valor de obtener más información antes de comprarla.
6. Reconocer los errores de juicio que con más frecuencia distorsionan las decisiones de seguridad en los servicios esenciales.
7. Redactar un registro de decisión que un sucesor, un auditor o un regulador puedan seguir.

Este capítulo establece los hábitos de decisión que usan todos los capítulos posteriores. El capítulo 4 añade el riesgo cuantificado y su distribución entre las personas; el capítulo 5 aplica el mismo razonamiento a las arquitecturas; el capítulo 9 convierte los registros de decisión en aseguramiento.

### 1.1 Qué hace que una decisión sea «a escala de la organización»

En etapas anteriores, un profesional elige configuraciones, herramientas y procedimientos. Un especialista que lidera la seguridad de un servicio esencial elige **carteras sujetas a restricciones**: cuál de varios programas valiosos financiar este año, qué riesgo aceptar, qué proveedor mantener, cuándo desconectar una planta de una red. Estas decisiones comparten cinco rasgos. Son **irreversibles o caras de revertir**: un contrato de servicio gestionado a tres años, una red de control rediseñada. Sus resultados son **inciertos y raros**, de modo que la experiencia por sí sola da una retroalimentación pobre: una empresa de servicios puede pasar una década sin el suceso para el que compró un control. Tienen **varios objetivos** que no pueden reducirse honestamente a un solo número: continuidad del suministro, seguridad del personal y del público, coste, cumplimiento legal, privacidad y reputación. Tienen **varias partes interesadas** con intereses legítimos pero distintos: el consejo de administración, los operadores, el regulador, los clientes, los operadores vecinos. Y las **toma alguien con autoridad**, que después debe explicarlas.

El trabajo del especialista rara vez consiste en tomar la decisión solo. Consiste en **estructurarla** para que la persona con autoridad pueda decidir bien, y en hacer que esa estructura pueda inspeccionarse. Esa distinción importa para la rendición de cuentas (capítulo 7) y para la ética (capítulo 4): un analista que elige en silencio los pesos ha tomado la decisión aparentando solo asesorar.

### 1.2 Plantear la decisión: el enunciado de la decisión

La mayoría de las malas decisiones de seguridad son respuestas bien analizadas a preguntas mal planteadas. Un **enunciado de la decisión** fija seis cosas antes de cualquier análisis:

| Elemento | Pregunta | Ejemplo de Merrow Water (sintético) |
|---|---|---|
| Quien decide | ¿Quién tiene autoridad para elegir y para aceptar el riesgo residual? | El director de Operaciones, con aprobación del consejo por encima de 500.000 £ al año |
| Decisión | ¿Qué se elige exactamente? | Qué programa de seguridad financiar el próximo ejercicio con una dotación fija |
| Opciones | ¿Qué alternativas realmente distintas hay sobre la mesa, incluida «aplazar»? | A bastionado del acceso remoto; B capacidad de operación manual; C la mitad de cada una; D aplazar |
| Objetivos | ¿Qué intentamos proteger o lograr, y en qué unidades? | Minimizar el coste esperado y el del peor caso de la pérdida del suministro de agua tratada, incluido el coste del programa; mantener a salvo al público; cumplir las obligaciones regulatorias |
| Horizonte y plazo | ¿En qué periodo se juzgan los resultados y cuándo debemos elegir? | Un año presupuestario; decisión en el consejo de marzo |
| Restricciones | ¿Qué no puede vulnerarse, diga lo que diga el análisis? | Ninguna opción puede reducir la capacidad de los operadores de hacer funcionar las plantas a mano; ninguna plantilla adicional no presupuestada |

La **opción «aplazar»** merece una atención explícita. Siempre está disponible, es lo que ocurre cuando nadie decide y, en los servicios esenciales, a menudo es peor de lo que parece, porque sus pérdidas se concentran en escenarios raros y graves. Escribirla obliga al análisis a mostrar su coste.

Las buenas opciones son **realmente distintas**, no una opción favorita acompañada de dos hombres de paja. Una prueba útil: ¿podría una persona razonable e informada preferir cada una de ellas con alguna visión plausible del mundo? Si no, el conjunto de opciones es un ejercicio de justificación.

### 1.3 Objetivos en unidades de servicio

El NIST Cybersecurity Framework 2.0 sitúa «Govern» (gobernar) en el centro de la gestión de la seguridad y pide a las organizaciones que comprendan su misión, sus partes interesadas y su apetito de riesgo antes de elegir controles ([NIST, CSF 2.0, 2024](https://doi.org/10.6028/NIST.CSWP.29)). En un servicio esencial, la misión se presta en **unidades de servicio**: litros de agua conforme, megavatios-hora entregados, pacientes atendidos dentro de los plazos clínicos, contenedores movidos, pagos liquidados. Un objetivo expresado en unidades de servicio hace tres cosas que un objetivo monetario no puede hacer. Mantiene visibles a las personas que dependen del servicio; permite que los operadores, que piensan en unidades de servicio, comprueben el análisis; y deja al descubierto los casos en los que el dinero y el daño divergen, por ejemplo cuando una interrupción barata recae sobre personas que no pueden afrontarla (capítulo 4).

En la práctica usará ambos: unidades de servicio para la consecuencia y dinero para el coste. Manténgalos en columnas separadas hasta que quien decide acuerde un tipo de cambio, y registre ese tipo como un juicio, no como un hecho. El Cyber Assessment Framework del National Cyber Security Centre del Reino Unido hace algo similar al organizar sus objetivos en torno a la función esencial y no en torno a los activos de TI ([NCSC, Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf)).

### 1.4 Tres reglas de decisión

Suponga que tiene una tabla de opciones por escenarios, con el coste anual total (coste del programa más pérdida) en cada celda. Tres reglas de decisión leen esa tabla de forma distinta.

**Valor esperado (VE).** Pondere el resultado de cada escenario por su probabilidad y sume. Elija la opción con el menor coste esperado. El VE es la regla adecuada cuando afronta muchas decisiones similares e independientes y puede absorber la variación, porque a lo largo de muchas repeticiones lo que paga es la media. Es la regla por defecto en el pensamiento de los seguros y de las carteras. Sus debilidades: depende de probabilidades que, para los sucesos ciberfísicos raros, nadie conoce bien; y trata una pequeña probabilidad de catástrofe como intercambiable con una pequeña pérdida segura.

**Minimax (peor caso).** Elija la opción cuyo peor resultado sea el menos malo. El minimax es adecuado cuando un resultado sería inaceptable con independencia de su probabilidad: la pérdida de vidas, la desaparición de la organización, la pérdida de la confianza pública en el agua potable. Su debilidad es que ignora por completo las probabilidades y puede comprar una protección cara frente a un escenario casi imposible.

**Minimax del arrepentimiento.** Para cada escenario, encuentre la mejor opción; el **arrepentimiento** de una opción en ese escenario es cuánto peor es que esa mejor opción. Elija la opción cuyo mayor arrepentimiento sea el menor ([Savage, 1951](https://doi.org/10.1080/01621459.1951.10500768)). El arrepentimiento recoge cómo se verá una decisión a posteriori («deberíamos haber hecho X») y tiende a favorecer las opciones equilibradas cuando ningún escenario domina. Su debilidad es que añadir o quitar una opción irrelevante puede cambiar la respuesta.

Ninguna de estas reglas es «la correcta». Un especialista informa de lo que recomienda cada regla, explica por qué difieren y ayuda a quien decide a elegir una regla *antes* de ver qué opción favorece. Cuando las tres coinciden, la decisión es robusta. Cuando discrepan, la discrepancia es lo más útil que puede mostrar a un consejo de administración.

### 1.5 Probabilidades que no conoce: sensibilidad y umbrales

Las probabilidades de los escenarios de seguridad raros son juicios, no mediciones. Tres prácticas las mantienen honestas. Primero, **obténgalas con cuidado**: pida rangos, pregunte a varias personas de forma independiente y pregunte por las tasas base antes que por el caso concreto ([O'Hagan et al., 2006](https://doi.org/10.1002/0470033312)). Segundo, **muestre varios conjuntos de creencias** (el del analista, el de un pesimista, la visión implícita del regulador) en lugar de uno solo. Tercero, y lo más útil, **encuentre el umbral**: la probabilidad en la que cambia la recomendación. A un consejo de administración no le resulta fácil decir si la probabilidad de un compromiso del acceso remoto de TO es del 3 % o del 6 % anual, pero a menudo sí puede decir si está por encima o por debajo de un umbral dado, sobre todo si se le muestra la evidencia que sustenta cada visión; por ejemplo, los avisos públicos que describen el preposicionamiento en redes de infraestructura ([CISA, AA24-038A, 2024](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)).

### 1.6 Valor de la información

Antes de encargar una evaluación, una prueba de penetración o un estudio de consultoría, pregúntese qué podría cambiar. El **valor esperado de la información perfecta (EVPI)** es la diferencia entre el coste esperado de la mejor opción ahora y el coste esperado si pudiera saber qué escenario ocurrirá antes de elegir. Es una cota superior de lo que vale cualquier estudio para esta decisión: si el EVPI es de 50.000 £, un estudio de 200.000 £ no puede amortizarse solo con esta decisión. Los estudios reales dan información imperfecta, por lo que valen menos que el EVPI; si un estudio no puede, de forma plausible, mover una probabilidad al otro lado del umbral hallado en el §1.5, vale poco para la decisión, por interesante que sea. Este es el razonamiento estándar del análisis de decisiones; lo importante para la práctica es escribir, antes de comprar información, qué resultado cambiaría qué elección.

### 1.7 Errores de juicio que distorsionan las decisiones de seguridad

La investigación clásica sobre el juicio en condiciones de incertidumbre describe heurísticos (disponibilidad, representatividad, anclaje) que conducen a errores sistemáticos ([Tversky and Kahneman, 1974](https://doi.org/10.1126/science.185.4157.1124)). En la seguridad de los servicios esenciales aparecen de formas reconocibles:

- **Disponibilidad tras un titular.** Un incidente de amplia difusión en otro sector eleva la probabilidad percibida de ese escenario y desplaza a otros más discretos y más probables.
- **Anclaje en el presupuesto del año anterior o en el primer presupuesto de un proveedor.**
- **Sustitución por el cumplimiento.** Tratar «el regulador exige X» como si respondiera a «X es el mejor uso de la próxima libra». El cumplimiento es una restricción (§1.2), no un objetivo.
- **Recuento de controles.** Preferir la opción que cierra más hallazgos de auditoría en lugar de la que más reduce la consecuencia.
- **Optimismo sobre el respaldo manual.** Suponer que los operadores pueden hacer funcionar una planta a mano porque una vez pudieron, sin un simulacro reciente (capítulo 6).
- **Pensamiento de grupo y deferencia.** La persona de mayor rango habla primero y el resto se ancla en ella.

Los remedios estructurales funcionan mejor que las exhortaciones: estimaciones independientes antes de la discusión; un escéptico designado; un **pre mortem**, en el que el grupo imagina que la decisión ha fracasado y escribe por qué ([Klein, 2007](https://hbr.org/2007/09/performing-a-project-premortem)); y un registro escrito del disenso.

### 1.8 El registro de decisión

Un **registro de decisión** es un documento breve redactado en el momento de la decisión, que contiene: el enunciado de la decisión; las opciones y por qué se consideró cada una; las evidencias utilizadas, con sus fuentes; los juicios de probabilidad y de peso y quién los hizo; lo que recomendó cada regla de decisión; el análisis de umbrales; la elección hecha, por quién y con qué regla; el riesgo residual aceptado y su responsable; el disenso; y el **desencadenante de revisión**, la observación que reabriría la decisión (por ejemplo, «un aviso creíble que informe del compromiso de dispositivos de acceso remoto del tipo que usamos»). El registro protege a quienes deciden bien cuando un suceso raro ocurre de todos modos, y es la forma en que las organizaciones aprenden: sin él, la retrospectiva reescribe lo que se sabía.

### 1.9 Ejemplo resuelto: la elección de programa de Merrow Water (sintético)

La dotación de Merrow Water permite una de cuatro opciones para el próximo año. El especialista y el equipo de operaciones construyeron la tabla siguiente (miles de libras al año, incluido el coste propio de cada opción; menos es mejor). La opción A bastiona el acceso remoto (sesiones de proveedores intermediadas, MFA resistente al phishing, eliminación de las cuentas permanentes). La opción B construye capacidad de operación manual (procedimientos, instrumentación local, simulacros, cobertura de personal) para que las plantas sigan produciendo agua segura cuando se pierden los sistemas de control. La opción C hace la mitad de cada una. La opción D aplaza.

| Opción | Ransomware de TI | Compromiso del acceso remoto de TO | Interrupción de proveedor/nube | Año tranquilo |
|---|---:|---:|---:|---:|
| A bastionado del acceso remoto | 700 | 240 | 650 | 170 |
| B capacidad de operación manual | 450 | 900 | 330 | 230 |
| C la mitad de cada una | 560 | 520 | 470 | 200 |
| D aplazar | 1.300 | 2.600 | 780 | 0 |

El razonamiento que hay detrás de algunas celdas importa más que los números. B funciona bien siempre que los sistemas de control se *pierden* (ransomware, interrupción), porque la planta sigue funcionando a mano, pero mal cuando un intruso los *usa indebidamente*, porque la capacidad manual no detiene las órdenes maliciosas antes de que se adviertan. A funciona bien frente al intruso, pero no frente a la pérdida. D es la más barata en un año tranquilo y catastrófica en el escenario de TO, cuyo coste incluye un aviso de hervir el agua que afecta a toda la zona de suministro de Hollin.

El equipo registró tres conjuntos de creencias sobre las probabilidades de los escenarios: el del analista (15 % / 3 % / 10 % / 72 %), el de un pesimista (25 % / 10 % / 15 % / 50 %) y una visión implícita del regulador con más peso en el compromiso de TO (10 % / 8 % / 5 % / 77 %). El Lab 1 calcula los resultados.

### 1.10 Actividad práctica: una decisión, tres reglas

Ejecute el laboratorio y después lea la interpretación.

```python
# Lab 1 - one decision, three decision rules (offline, standard library only)
# Synthetic: Merrow Water's annual security investment choice. Figures are invented, in GBP thousands per year,
# and already include each option's own annual cost. Lower is better (cost + expected/realized loss).
OPTIONS = ["A remote-access hardening", "B manual-operations capability", "C half of each", "D defer"]
SCEN = ["IT ransomware", "OT remote-access compromise", "vendor/cloud outage", "quiet year"]
COST = {  # option -> loss in each scenario (k GBP)
    "A remote-access hardening":      [ 700,  240,  650, 170],
    "B manual-operations capability": [ 450,  900,  330, 230],
    "C half of each":                 [ 560,  520,  470, 200],
    "D defer":                        [1300, 2600,  780,   0],
}
BELIEFS = {
    "analyst":    [0.15, 0.03, 0.10, 0.72],
    "pessimist":  [0.25, 0.10, 0.15, 0.50],
    "regulator":  [0.10, 0.08, 0.05, 0.77],
}
def ev(o, p): return sum(c * q for c, q in zip(COST[o], p))
for name, p in BELIEFS.items():
    assert abs(sum(p) - 1) < 1e-9
    ranked = sorted(OPTIONS, key=lambda o: ev(o, p))
    print(f"{name:10s}", "  ".join(f"{o[0]}={ev(o, p):7.1f}" for o in OPTIONS), " best:", ranked[0][0])
best_in = [min(COST[o][s] for o in OPTIONS) for s in range(len(SCEN))]
regret = {o: max(COST[o][s] - best_in[s] for s in range(len(SCEN))) for o in OPTIONS}
worst = {o: max(COST[o]) for o in OPTIONS}
print("max regret:", "  ".join(f"{o[0]}={regret[o]}" for o in OPTIONS), " minimax-regret:", min(OPTIONS, key=regret.get)[0])
print("worst case:", "  ".join(f"{o[0]}={worst[o]}" for o in OPTIONS), " minimax:", min(OPTIONS, key=worst.get)[0])
# Robustness: sweep P(OT compromise) from 0 to 0.30, keeping the analyst's other ratios, and report the EV winner.
base = BELIEFS["analyst"]
prev = None
for k in range(0, 31):
    q = k / 100
    rest = [base[0], base[2], base[3]]; s = sum(rest)
    p = [rest[0] / s * (1 - q), q, rest[1] / s * (1 - q), rest[2] / s * (1 - q)]
    win = min(OPTIONS, key=lambda o: ev(o, p))[0]
    if win != prev:
        print(f"P(OT compromise)={q:.2f}: EV winner {win}")
        prev = win
```

Salida esperada:

```text
analyst    A=  299.6  B=  293.1  C=  290.6  D=  351.0  best: C
pessimist  A=  381.5  B=  367.0  C=  362.5  D=  702.0  best: C
regulator  A=  252.6  B=  310.6  C=  275.1  D=  377.0  best: A
max regret: A=320  B=660  C=280  D=2360  minimax-regret: C
worst case: A=700  B=900  C=560  D=2600  minimax: C
P(OT compromise)=0.00: EV winner B
P(OT compromise)=0.03: EV winner C
P(OT compromise)=0.07: EV winner A
```

**Interpretación.** Con las creencias del analista y del pesimista, C tiene el menor coste esperado, pero solo por poco: 290,6 frente a 293,1 de B y 299,6 de A con la visión del analista. Diferencias de 3.000–9.000 £ sobre estimaciones tan aproximadas no son, por sí solas, una base para decidir. Con las creencias del regulador gana A. El barrido de umbrales hace visible la estructura: B gana solo si la probabilidad de compromiso de TO es inferior a un 3 % aproximadamente; C, entre un 3 % y un 7 % aproximadamente; A, por encima de un 7 % aproximadamente. El minimax y el minimax del arrepentimiento eligen ambos C, porque C nunca sale muy mal parada. **C es, por tanto, la recomendación robusta**: es la mejor o casi la mejor con todos los conjuntos de creencias y todas las reglas. El registro de decisión debe decir exactamente eso y añadir el desencadenante de revisión: una evidencia que eleve la probabilidad de compromiso de TO por encima del 7 % (por ejemplo, informes creíbles de explotación de los productos de acceso remoto que usa Merrow) desplaza la recomendación a A. Observe también lo que la tabla no puede mostrar: el valor de C supone que «la mitad de cada una» aporta más de la mitad del beneficio de cada una, lo cual es un juicio que debe confirmar el director de Operaciones.

### 1.11 Errores comunes y límites

- Presentar una única «puntuación de riesgo» por opción, que oculta si la puntuación procede de la frecuencia, de la gravedad o de una ponderación arbitraria.
- Omitir la opción de aplazar, o asignarle un coste cero.
- Elegir la regla de decisión después de ver qué opción favorece.
- Informar de valores esperados a la libra cuando las entradas son juicios aproximados; informe, en cambio, de las diferencias que importan y de los umbrales.
- Tratar estadísticas de proveedores o de encuestas de apariencia precisa como probabilidades para su organización sin preguntar cómo se obtuvieron (capítulo 10).
- Dejar que los pesos del analista se conviertan en silencio en la decisión.
- Redactar el registro de decisión a posteriori, cuando la retrospectiva ya lo ha moldeado.

El principal límite del análisis formal de decisiones es que solo es tan bueno como el conjunto de opciones y el modelo de consecuencias. Su valor no está en producir automáticamente la respuesta correcta, sino en hacer que las razones de una respuesta sean **inspeccionables** y **revisables** cuando llegan nuevas evidencias.

### Ejercicios — capítulo 1

**EX001 — Plantee una decisión hospitalaria.** *Objetivo:* redactar el enunciado de una decisión para una elección verosímil. *Entradas:* Merrow Health debe decidir si sustituye este año su sistema de laboratorio de anatomía patológica sin soporte o lo aísla y lo sustituye dentro de dos años. *Restricciones:* use los seis elementos del §1.2; al menos tres opciones realmente distintas, incluida aplazar; objetivos en unidades de servicio. *Pasos:* (1) redacte el enunciado; (2) aplique a cada opción la prueba de «una persona razonable podría preferirla»; (3) enumere dos restricciones que no sean objetivos. *Evidencia esperada:* enunciado de la decisión de una página. *Rúbrica:* 3 = los seis elementos, opciones realmente distintas, objetivos en unidades de servicio (por ejemplo, el tiempo de respuesta de los resultados urgentes), restricciones diferenciadas de los objetivos; 2 = un elemento débil; 1 = las opciones son hombres de paja o los objetivos solo están en dinero; 0 = falta.

**EX002 — Cambie una celda.** *Objetivo:* ver cómo responden las reglas de decisión a una estimación de consecuencias revisada. *Entradas:* el Lab 1. *Restricciones:* cambie solo el coste de D en el escenario de TO de 2.600 a 1.200 (los ingenieros creen que un aviso de hervir el agua podría limitarse a una zona). *Pasos:* (1) vuelva a ejecutarlo; (2) informe del ganador por VE con cada conjunto de creencias, del arrepentimiento máximo de cada opción y de la elección por minimax del arrepentimiento; (3) explique por qué D sigue sin ganar. *Evidencia esperada:* salidas y explicación de 150 palabras. *Rúbrica:* 3 = números correctos y una explicación que vincula el arrepentimiento de D con el escenario de ransomware, no solo con el de TO; 2 = números correctos, explicación pobre; 1 = no ejecutado; 0 = nada.

**EX003 — Valor de la información perfecta.** *Objetivo:* acotar lo que vale un estudio adicional. *Entradas:* la tabla del Lab 1 y las creencias del analista. *Restricciones:* calcúlelo a mano o con un breve añadido al laboratorio. *Pasos:* (1) calcule el coste esperado de la mejor opción ahora; (2) calcule el coste esperado si conociera el escenario antes de elegir; (3) informe del EVPI; (4) un consultor ofrece una evaluación de amenazas de TO por 60.000 £: explique en qué condición podría merecer la pena comprarla para esta decisión. *Evidencia esperada:* cálculo y párrafo. *Rúbrica:* 3 = EVPI correcto y la compra vinculada a si el estudio podría mover la probabilidad de TO al otro lado de los umbrales del 3 % o del 7 %; 2 = EVPI correcto, vínculo débil; 1 = errores aritméticos; 0 = nada.

**EX004 — Registro de decisión con disenso.** *Objetivo:* producir un registro inspeccionable. *Entradas:* el ejemplo resuelto y la salida del Lab 1. *Restricciones:* una página; todos los elementos del §1.8. *Pasos:* (1) redacte el registro de la elección de C; (2) incluya un disenso realista del jefe de operaciones, que prefiere B; (3) indique el desencadenante de revisión y el responsable del riesgo residual. *Evidencia esperada:* registro de decisión. *Rúbrica:* 3 = completo, honesto sobre los estrechos márgenes de VE, disenso expuesto con justicia, desencadenante medible; 2 = falta un elemento; 1 = se lee como un alegato; 0 = nada.

**EX005 — Auditoría de sesgos.** *Objetivo:* reconocer errores de juicio en una reunión. *Entradas:* acta sintética: «El presidente abrió la sesión mencionando el reciente caso de ransomware en el oleoducto y dijo que la seguridad de TO es ahora la máxima prioridad. La propuesta de 400.000 £ del proveedor se tomó como punto de partida. El jefe de operaciones dijo que el funcionamiento manual "no es problema: lo hicimos en 2009". La responsable de auditoría interna señaló que la opción A cierra nueve de los once hallazgos abiertos. No se registraron otras opiniones». *Restricciones:* nombre como máximo cinco errores del §1.7 y proponga un remedio estructural para cada uno. *Pasos:* identifique, explique, proponga un remedio. *Evidencia esperada:* tabla. *Rúbrica:* 3 = disponibilidad, anclaje, optimismo sobre el respaldo manual, recuento de controles y deferencia/pensamiento de grupo identificados con remedios estructurales (estimaciones independientes, pre mortem, evidencia de simulacros, puntuación basada en consecuencias, disenso registrado); 2 = tres o cuatro; 1 = consejos genéricos; 0 = nada.

### Síntesis del capítulo

Las decisiones de seguridad a escala de la organización son irreversibles, de sucesos raros, con varios objetivos y varias partes interesadas, y pertenecen a alguien con autoridad. La contribución del especialista es la estructura: un enunciado de la decisión con opciones realmente distintas, incluida aplazar; objetivos en unidades de servicio; varias reglas de decisión presentadas una junto a otra; conjuntos de creencias en lugar de una única probabilidad; umbrales en los que cambia la recomendación; el valor de obtener más información; defensas estructurales contra el juicio sesgado; y un registro de decisión redactado en el momento. Una recomendación robusta es la que sobrevive a los cambios de regla y de creencias; cuando no lo hace, muestre el umbral y deje que la persona que rinde cuentas decida con conocimiento de causa.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 12

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Infraestructura crítica y seguridad sectorial: práctica actual

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Describir las principales líneas base y regímenes, transversales y sectoriales, con los que probablemente se encontrará un operador de servicios esenciales, y qué tipo de obligación crea cada uno.
2. Explicar por qué los sectores que comparten tecnología siguen necesitando prácticas distintas: difieren la consecuencia, la física, la regulación y la plantilla.
3. Distinguir la implantación declarada, documentada y verificada de una práctica, y medir la diferencia.
4. Priorizar las carencias por su consecuencia para el servicio esencial y no por su número.
5. Criticar una práctica común y proponer una alternativa mejor fundamentada en evidencias.

El capítulo 1 le dio una forma de elegir entre opciones. Este capítulo aporta las opciones que se espera que conozca un especialista competente y el estándar de evidencia para afirmar que están implantadas. El capítulo 3 se pregunta después qué cuenta como evidencia cuando algo sale mal.

### 2.1 Qué significa «práctica actual» para un especialista

La «práctica actual» no es una única lista. Es la intersección de tres cosas: lo que **exigen los reguladores y las normas** en su jurisdicción y su sector; lo que recomiendan las **orientaciones autorizadas** a partir de los ataques observados; y lo que **los operadores comparables realmente hacen** y pueden demostrar. Un especialista debe conocer las tres y debe poder decir de qué fuente procede cada afirmación de un programa de seguridad, porque tienen un peso distinto. Una obligación legal es una restricción; un requisito de una norma puede ser contractual o certificable; una orientación es un consejo que debe sopesarse frente a su propio análisis de consecuencias.

La práctica también envejece. Los avisos sobre el preposicionamiento en redes de infraestructura por parte de actores patrocinados por Estados que usan herramientas de administración legítimas ([CISA, AA24-038A, 2024](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)) cambiaron lo que significan un «registro adecuado» y una «higiene de credenciales adecuada» para los operadores que los habían tratado como tareas domésticas de TI. Una línea base que era actual hace tres años puede ser hoy un mínimo.

### 2.2 Líneas base transversales

Cuatro familias de documentos se repiten en todos los sectores:

- **Marcos de resultados.** El NIST CSF 2.0 organiza los resultados en Govern, Identify, Protect, Detect, Respond y Recover (gobernar, identificar, proteger, detectar, responder y recuperar) ([NIST, 2024](https://doi.org/10.6028/NIST.CSWP.29)). El Cyber Assessment Framework del NCSC del Reino Unido fija cuatro objetivos (gestionar el riesgo de seguridad, protegerse frente a los ciberataques, detectar los eventos de ciberseguridad y minimizar el impacto de los incidentes), con indicadores de buena práctica para cada principio, y está diseñado en torno a las funciones esenciales ([NCSC, CAF](https://www.ncsc.gov.uk/collection/caf)). Los marcos de resultados dicen *qué* debe lograrse, no *cómo*; son buenos para estructurar un programa y malos como guiones de prueba.
- **Líneas base priorizadas.** Los Cross-Sector Cybersecurity Performance Goals de CISA enumeran un pequeño conjunto de prácticas con un alto valor de reducción del riesgo para organizaciones de cualquier tamaño ([CISA, CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)); el Departamento de Salud y Servicios Humanos de EE. UU. publicó, con el mismo espíritu, objetivos de desempeño específicos para la atención sanitaria ([HHS, HPH CPGs, 2024](https://hphcyber.hhs.gov/performance-goals.html)). Son útiles precisamente porque son breves; no son un programa completo.
- **Catálogos de controles.** La NIST SP 800-53 Rev. 5 es un catálogo exhaustivo de controles de seguridad y privacidad ([NIST](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)); la NIST SP 800-82 Rev. 3 adapta las orientaciones a la tecnología operativa, incluidas superposiciones (*overlays*) y las restricciones particulares de los sistemas de control ([NIST, 2023](https://doi.org/10.6028/NIST.SP.800-82r3)).
- **Normas industriales.** La serie ISA/IEC 62443 aborda la seguridad de los sistemas de automatización y control industrial para propietarios de activos, integradores y proveedores de productos, incluidas las zonas y los conductos, los niveles de seguridad y el desarrollo seguro de productos ([ISA overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). Su parte de evaluación de riesgos para el diseño de sistemas, la IEC 62443-3-2, es el punto de partida habitual de una revisión de arquitectura de TO ([IEC catalogue page](https://webstore.iec.ch/en/publication/30727)).

### 2.3 Los regímenes sectoriales crean distintos tipos de obligación

A escala de la organización, la pregunta no es «qué marco es el mejor», sino «qué obligaciones se nos aplican y qué evidencias esperará cada regulador». Ejemplos, que deben volver a verificarse para su jurisdicción y su fecha:

| Régimen | Ámbito (resumen) | Tipo de obligación | Evidencia típica esperada |
|---|---|---|---|
| [NIS2 Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/) | Entidades esenciales e importantes de los sectores enumerados, transpuesta al derecho nacional | Medidas de gestión de riesgos y notificación de incidentes por etapas (alerta temprana, notificación, informe final) | Medidas aprobadas por el órgano de dirección, informes de incidentes dentro de los plazos nacionales |
| [CER Directive (EU) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj) | Resiliencia de las entidades críticas frente a todo tipo de amenazas | Evaluación de riesgos y medidas de resiliencia, no solo cibernéticas | Planes de resiliencia, cooperación con las autoridades |
| [DORA, Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) | Entidades financieras y sus proveedores terceros críticos de TIC | Normas directamente aplicables sobre riesgo de TIC, pruebas, incidentes y terceros | Registros de los acuerdos con terceros de TIC, resultados de las pruebas |
| [NERC CIP standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx) | Sistema eléctrico de transporte en Norteamérica | Requisitos obligatorios y auditables según la categoría de impacto del activo | Evidencia de auditoría por requisito, a menudo muy prescriptiva |
| [America's Water Infrastructure Act 2018, s.2013](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans) | Sistemas comunitarios de agua de EE. UU. por encima de un umbral de tamaño | Evaluación de riesgos y resiliencia y plan de respuesta a emergencias, con certificación | Evaluaciones y planes certificados de forma cíclica |

De ahí se derivan dos lecciones. Primera: un operador que abarca varios sectores (una empresa multiservicios, un puerto con su propia red eléctrica) puede estar sujeto a varios regímenes con plazos de notificación y estilos de evidencia distintos; armonizarlos en un único conjunto interno de controles con correspondencias es una tarea central del especialista. Segunda: **el cumplimiento es un mínimo y una restricción**, como sostuvo el capítulo 1: dos operadores que cumplen plenamente el mismo régimen pueden tener una resiliencia muy distinta.

### 2.4 Por qué difiere la práctica entre sectores

La tecnología compartida tienta a copiar prácticas de un sector a otro. Cuatro diferencias hacen que eso no sea seguro:

1. **Consecuencia y tiempo.** Los sistemas clínicos de un hospital fallan hacia daños en minutos u horas; un sistema de agua con almacenamiento puede tener de horas a días; el daño de un sistema de pagos se acumula en las ventanas de liquidación; el de un puerto, en el tiempo de permanencia de la carga y en las cadenas de suministro. El tiempo hasta el daño determina cuánto respaldo manual se necesita y con qué rapidez debe darse la respuesta.
2. **Física y seguridad funcional.** En la TO, una acción de seguridad puede causar daño por sí misma: un escaneo agresivo puede bloquear un controlador; aislar una red puede dejar ciegos a los operadores. La NIST SP 800-82 subraya que las restricciones de disponibilidad y de seguridad funcional determinan qué controles de seguridad son aceptables ([NIST, 2023](https://doi.org/10.6028/NIST.SP.800-82r3)).
3. **Regulación y cultura de la evidencia.** La electricidad en Norteamérica trabaja con requisitos auditables y prescriptivos; muchas empresas de agua trabajan con evaluaciones certificadas periódicas; la atención sanitaria trabaja bajo la legislación de privacidad y la gobernanza de la seguridad clínica, además de las normas de seguridad.
4. **Plantilla y proveedores.** Las pequeñas empresas de servicios pueden no tener personal de seguridad; los hospitales dependen de los fabricantes de dispositivos médicos para los parches; los puertos dependen de los proveedores del sistema operativo de la terminal y de las navieras. Quién puede implantar realmente una práctica determina si es real.

### 2.5 Declarado, documentado y verificado

La mayoría de las evaluaciones de líneas base son autoevaluaciones. Son útiles, pero un especialista debe saber qué parte de un «sí» está **verificada**. Use tres grados de evidencia:

- **Verificado (V):** se observó que la práctica funciona mediante prueba, inspección o conciliación: se realizó y cronometró una restauración; se exportó y comprobó la configuración del proveedor de identidad; se conciliaron los registros del intermediario con las sesiones del cortafuegos.
- **Documentado (D):** existe una política, un diseño o un procedimiento que dice que la práctica está implantada, pero nadie comprobó que la realidad coincida.
- **Afirmación (S):** alguien lo dijo.

Los métodos de evaluación del catálogo del NIST distinguen entre examinar, entrevistar y probar por la misma razón ([NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)). La diferencia entre la cobertura declarada y la verificada es a menudo la cifra más importante de un informe de línea base, y la que más a menudo se omite. También es donde viven los incidentes: copias de seguridad sin conexión que «existen» pero nunca se han restaurado; un acceso de proveedores que está «intermediado» salvo por aquel módem heredado.

### 2.6 Priorizar por consecuencias

La importancia de una práctica depende de cuánto limita la pérdida del servicio esencial. Pondere las prácticas por su consecuencia (no por cuántas referencias de marcos les corresponden) y priorice las carencias en las que el peso es alto y la puntuación verificada es baja. Los pesos son juicios; registre quién los fijó (capítulo 1). En Merrow Bay, el foro acordó que la MFA en el acceso remoto, la segmentación entre TI y TO, las copias de seguridad sin conexión probadas y el acceso de proveedores intermediado tienen el mayor peso, porque cada una limita directamente una vía hacia la pérdida del suministro observada en incidentes públicos: el compromiso del acceso remoto de un sistema de tratamiento de agua fue objeto de un aviso conjunto en 2021 ([CISA, AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)), aunque el relato de ese suceso concreto se cuestionó después ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)); la debilidad del acceso remoto que describía el aviso sigue siendo, en cualquier caso, una preocupación de diseño válida.

### 2.7 Ejemplo resuelto: las autoevaluaciones de cuatro operadores (sintético)

El Merrow Bay Resilience Forum pidió a cuatro operadores que autoevaluaran ocho prácticas, con una puntuación de 0 (ausente), 1 (parcial) o 2 (implantada), y que calificaran la evidencia como V, D o S. La tarea del especialista es convertir las respuestas en una imagen regional sin ofender a nadie ni creérselo todo. En lugar de «rechazar» las afirmaciones, el Lab 2 les da un crédito **provisional** de cero hasta que se prueben y medio crédito a los documentos. Esos créditos son una elección de política; el EX007 pone a prueba su efecto.

Dos convenciones determinan los resultados. Los pesos de cada práctica los acordó el foro, de modo que la imagen regional refleja su juicio sobre qué prácticas limitan la pérdida del suministro. Y los operadores aparecen con su nombre en este ejemplo solo porque es sintético; un informe real del foro mostraría normalmente a cada operador su propia fila y daría a los demás solo el resumen regional. El especialista debería enviar a cada operador su resultado en privado antes de la reunión del foro, para que nadie descubra una carencia incómoda delante de sus homólogos.

### 2.8 Actividad práctica: cobertura declarada frente a verificada

```python
# Lab 2 - claimed versus verified baseline coverage, weighted by consequence (offline, standard library only)
# Synthetic: four Merrow Bay operators self-assess eight baseline practices (0 = absent, 1 = partial, 2 = in place)
# and say what evidence backs each answer: V = verified by test or inspection, D = document only, S = statement only.
PRACTICES = {  # practice -> consequence weight (how much it limits loss of the essential service; invented)
    "MFA on remote access": 3, "asset inventory incl. OT": 2, "IT/OT segmentation": 3,
    "offline backups restored in test": 3, "central logging retained 90d": 1,
    "incident plan exercised in 12 months": 2, "vendor access brokered and recorded": 3,
    "default credentials removed": 2,
}
ANSWERS = {  # operator -> list of (score, evidence) in PRACTICES order
    "Merrow Water":     [(2,"V"),(1,"D"),(2,"D"),(2,"S"),(1,"V"),(2,"V"),(1,"S"),(2,"S")],
    "Merrow Health":    [(2,"V"),(1,"D"),(1,"D"),(2,"V"),(2,"V"),(2,"D"),(1,"D"),(1,"S")],
    "Merrow Energy":    [(2,"V"),(2,"V"),(2,"V"),(1,"D"),(2,"V"),(2,"V"),(2,"D"),(2,"D")],
    "Port of Merrow":   [(2,"S"),(0,"S"),(1,"S"),(2,"S"),(1,"D"),(1,"S"),(0,"S"),(2,"S")],
}
CREDIT = {"V": 1.0, "D": 0.5, "S": 0.0}  # how much of a claimed score we accept without further testing
W = list(PRACTICES.values()); maxw = 2 * sum(W)
print(f"{'operator':16s} claimed  verified  gap(weighted points)")
gaps = []
for op, ans in ANSWERS.items():
    claimed = sum(w * s for w, (s, e) in zip(W, ans))
    verified = sum(w * s * CREDIT[e] for w, (s, e) in zip(W, ans))
    print(f"{op:16s} {claimed/maxw:6.0%}   {verified/maxw:6.0%}   {maxw-verified:5.1f}")
    for (name, w), (s, e) in zip(PRACTICES.items(), ans):
        unverified = w * (2 - s * CREDIT[e])
        if w == 3 and unverified >= 3:
            gaps.append((unverified, op, name, s, e))
print("\nHigh-consequence practices with >= 3 unverified weighted points:")
for u, op, name, s, e in sorted(gaps, reverse=True):
    print(f"  {u:4.1f}  {op:16s} {name}  (claimed {s}, evidence {e})")
```

Salida esperada:

```text
operator         claimed  verified  gap(weighted points)
Merrow Water        84%      39%    23.0
Merrow Health       74%      53%    18.0
Merrow Energy       92%      75%     9.5
Port of Merrow      58%       1%    37.5

High-consequence practices with >= 3 unverified weighted points:
   6.0  Port of Merrow   vendor access brokered and recorded  (claimed 0, evidence S)
   6.0  Port of Merrow   offline backups restored in test  (claimed 2, evidence S)
   6.0  Port of Merrow   MFA on remote access  (claimed 2, evidence S)
   6.0  Port of Merrow   IT/OT segmentation  (claimed 1, evidence S)
   6.0  Merrow Water     vendor access brokered and recorded  (claimed 1, evidence S)
   6.0  Merrow Water     offline backups restored in test  (claimed 2, evidence S)
   4.5  Merrow Health    vendor access brokered and recorded  (claimed 1, evidence D)
   4.5  Merrow Health    IT/OT segmentation  (claimed 1, evidence D)
   4.5  Merrow Energy    offline backups restored in test  (claimed 1, evidence D)
   3.0  Merrow Water     IT/OT segmentation  (claimed 2, evidence D)
   3.0  Merrow Energy    vendor access brokered and recorded  (claimed 2, evidence D)
```

**Interpretación.** La cobertura declarada va del 58 % al 92 %; la verificada, del 1 % al 75 %. La posición de la propia Merrow Water (84 % declarada, 39 % verificada) resulta incómoda para su especialista: las dos carencias de mayor peso son afirmaciones de que las copias de seguridad sin conexión pueden restaurarse y de que el acceso de proveedores está intermediado. El 1 % de Port of Merrow no significa que el puerto no tenga seguridad; significa que no se ha demostrado nada. La lista priorizada es un **plan de verificación** antes que un plan de corrección: cada uno de los once elementos se basa en una afirmación o en un documento, de modo que la primera acción en cada caso es poner a prueba la afirmación, algo barato en comparación con comprar controles y, a veces, suficiente para cerrar la carencia. Merrow Energy, con evidencias mayoritariamente verificadas, es la mejor fuente de método práctico de la región: un activo para el foro, no solo una puntuación.

### 2.9 Criticar una práctica común

Se espera que los especialistas cuestionen las prácticas que persisten por costumbre. Tome la «prueba de penetración de TO» anual que figura en muchos contratos. A menudo produce una lista de hallazgos sobre una muestra de sistemas en una ventana corta, con técnicas que deben atenuarse para no perturbar el proceso, y suele delimitarse de modo que se evitan los activos de mayor consecuencia. Entre las alternativas con mejor valor como evidencia figuran: una revisión guiada por las consecuencias que parte del peor resultado físico creíble y retrocede hasta las rutas digitales que podrían causarlo ([Idaho National Laboratory, CCE](https://inl.gov/national-security/cce/)); la conciliación continua de los registros de acceso remoto y de cambios; y las pruebas en una instalación representativa en lugar de en la planta en producción (capítulo 6). La crítica no es «no pruebe nunca»; es «elija el método de evidencia que responde a la pregunta que de verdad hace el consejo de administración».

### 2.10 Errores comunes y límites

- Tratar una correspondencia con un marco como evidencia de implantación.
- Informar solo de la cobertura declarada, o promediar la declarada y la verificada en una sola cifra.
- Copiar la práctica de otro sector sin comprobar el tiempo hasta el daño y las restricciones de seguridad funcional.
- Tratar la línea base más breve como el programa completo, o el catálogo más largo como una lista de tareas.
- Suponer que el regulador de un sector aceptará evidencias diseñadas para otro.
- Ponderar las prácticas por cuántas normas las mencionan y no por su consecuencia.

El límite de cualquier línea base es que describe defensas que son comunes porque los ataques eran comunes. Dice poco sobre las rutas raras, dirigidas o nuevas, y por eso los capítulos 4 y 5 añaden el análisis guiado por las consecuencias.

### Ejercicios — capítulo 2

**EX006 — Haga corresponder una práctica con varios marcos.** *Objetivo:* vincular una práctica con obligaciones y orientaciones sin confundirlas. *Entradas:* «acceso de proveedores intermediado y registrado» en Merrow Water. *Restricciones:* use solo las fuentes citadas en los §2.2–2.3; no cite texto de normas de pago. *Pasos:* (1) identifique la función o funciones del CSF 2.0 y el objetivo del CAF a los que contribuye; (2) indique si aparece como objetivo transversal de CISA; (3) explique cómo la encuadra la idea de zonas y conductos de la IEC 62443; (4) indique, sin dar asesoramiento jurídico, si es una obligación legal para una empresa de agua en su jurisdicción y cómo lo verificaría. *Evidencia esperada:* una tabla breve de correspondencias y un párrafo. *Rúbrica:* 3 = correspondencias correctas a nivel de función y objetivo, obligaciones separadas de las orientaciones, una vía de verificación con asesoramiento jurídico indicada; 2 = una correspondencia errónea; 1 = trata las orientaciones como ley; 0 = nada.

**EX007 — Cambie la política de evidencias.** *Objetivo:* comprobar cómo cambia la imagen una política de puntuación. *Entradas:* el Lab 2. *Restricciones:* cambie el crédito de una afirmación de 0.0 a 0.25 y no cambie nada más. *Pasos:* (1) vuelva a ejecutarlo e informe de la cobertura verificada de cada operador; (2) diga qué conclusiones del §2.8 se mantienen; (3) defienda una política de créditos para el informe del foro. *Evidencia esperada:* salidas y un argumento de 200 palabras. *Rúbrica:* 3 = números correctos, reconocimiento de que se mantienen el orden y la prioridad de probar las afirmaciones, una política defendida a partir del uso del informe; 2 = números correctos, argumento débil; 1 = no ejecutado; 0 = nada.

**EX008 — Plan de verificación.** *Objetivo:* convertir las principales carencias en pruebas. *Entradas:* los tres elementos de Merrow Water de mayor peso en la lista del Lab 2. *Restricciones:* las pruebas deben ser seguras para la planta en funcionamiento; nombre la evidencia que contaría como V. *Pasos:* para cada elemento, indique el método (prueba, inspección, conciliación), el responsable, las condiciones de seguridad, el criterio de aceptación y el coste esperado en días-persona. *Evidencia esperada:* tabla. *Rúbrica:* 3 = los métodos ponen realmente a prueba la realidad (por ejemplo, una restauración cronometrada de un sistema identificado a un servidor aislado; la conciliación de los registros del intermediario con las sesiones del cortafuegos durante 30 días), condiciones de seguridad explícitas, criterios de aceptación medibles; 2 = un método solo documental; 1 = «revisar la política»; 0 = nada.

**EX009 — Operador sujeto a varios regímenes.** *Objetivo:* planificar las evidencias para regímenes superpuestos. *Entradas:* una empresa multiservicios sintética de la UE que suministra agua, opera una pequeña red de distribución eléctrica y tiene una filial de pagos. *Restricciones:* identifique los regímenes del §2.3 que podrían aplicarse, sin decidir su ámbito jurídico. *Pasos:* (1) enumere los regímenes candidatos y por qué podría aplicarse cada uno; (2) diseñe un único conjunto interno de controles con correspondencias; (3) identifique los plazos de notificación de incidentes que deben conciliarse; (4) indique qué preguntaría a los asesores jurídicos. *Evidencia esperada:* plan de una página. *Rúbrica:* 3 = regímenes candidatos plausibles, un único conjunto de controles con correspondencias, plazos de notificación identificados como problema de diseño, preguntas jurídicas específicas; 2 = correspondencias vagas; 1 = presenta conclusiones jurídicas como hechos; 0 = nada.

**EX010 — Critique una práctica.** *Objetivo:* defender un método de evidencia mejor. *Entradas:* el contrato de Merrow Health exige una «prueba de penetración externa anual de la red clínica». *Restricciones:* 300 palabras; respete la seguridad de los pacientes. *Pasos:* (1) enuncie la pregunta que el consejo quiere responder; (2) diga qué responde y qué no responde la prueba anual; (3) proponga una cartera alternativa de evidencias; (4) indique sus límites. *Evidencia esperada:* memorando. *Rúbrica:* 3 = pregunta explícita, límites de las pruebas puntuales identificados (muestra, ventana, atenuación, dispositivos excluidos), alternativas ajustadas a la pregunta, límites honestos; 2 = crítica sin alternativa; 1 = rechaza de plano las pruebas; 0 = nada.

### Síntesis del capítulo

La práctica actual es la intersección de la obligación, la orientación y la práctica demostrada de los homólogos, y cada una tiene un peso distinto. Conozca los marcos de resultados, las líneas base priorizadas, los catálogos de controles y las normas industriales, y sepa qué regímenes obligan a su organización y qué evidencias espera cada uno. No copie prácticas entre sectores sin comprobar el tiempo hasta el daño, la física, la regulación y la plantilla. Califique la evidencia como verificada, documentada o afirmación, informe con honestidad de la diferencia, pondere las prácticas por su consecuencia y convierta las mayores carencias en verificación antes que en corrección. Cuestione las prácticas habituales preguntando a qué pregunta responden sus evidencias.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](../../en/book/MANUSCRIPT.md#ch-03)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Cada resultado resuelto muestra una respuesta defendible y explica lo que premia la rúbrica. Una respuesta distinta puede obtener la máxima puntuación si cumple el mismo nivel de evidencia, de alcance y de honestidad sobre los límites. Los resultados numéricos proceden de los laboratorios sin conexión de este libro, ejecutados con Python 3 (para este borrador se usó la 3.13) y solo con la biblioteca estándar; si su salida difiere, compruebe primero la versión de Python, la semilla cuando se use una y si cambió el orden de las extracciones aleatorias. Todas las cifras describen datos sintéticos; nunca las presente como hallazgos sobre operadores reales.

### Capítulo 1: EX001–EX005

**EX001 — Plantee una decisión hospitalaria.** *Quien decide:* el director de Operaciones (COO) de Merrow Health, con aprobación del consejo por encima de un umbral de capital establecido. *Decisión:* si sustituir, y cuándo, el sistema de información del laboratorio de anatomía patológica sin soporte. *Opciones:* (A) sustituirlo este año por un producto con soporte; (B) aislar el sistema actual, restringir sus interfaces y sustituirlo dentro de dos años; (C) sustituirlo dentro de dos años sin más aislamiento (una opción débil que una persona razonable solo preferiría con una presión presupuestaria extrema; es mejor reemplazarla por una tercera opción genuina, como trasladar el trabajo urgente al sistema de otro centro); (D) aplazar indefinidamente. *Objetivos (unidades de servicio):* maximizar los resultados urgentes entregados dentro de los plazos clínicos; minimizar las intervenciones programadas canceladas; minimizar la exposición de datos que identifican a pacientes. *Horizonte:* decisión este trimestre; consecuencias a tres años. *Restricciones:* ninguna plantilla adicional no presupuestada; se exige la aprobación de seguridad clínica; obligaciones de protección de datos. La máxima puntuación exige una tercera opción genuina (no un hombre de paja), objetivos en unidades de servicio y restricciones diferenciadas de los objetivos.

**EX002 — Cambie una celda.** Con el coste de TO de D en 1.200: arrepentimientos máximos A=320, B=660, C=280, D=960; el minimax del arrepentimiento sigue eligiendo C. Valores esperados: analista A 299,6, B 293,1, C 290,6, D 309,0 (gana C); pesimista A 381,5, B 367,0, C 362,5, D 562,0 (gana C); regulador A 252,6, B 310,6, C 275,1, D 265,0 (sigue ganando A, ahora con D en segundo lugar). D no gana porque sus celdas de ransomware y de proveedor/nube siguen siendo caras: aunque se ignorara el escenario de TO, su arrepentimiento en el escenario de ransomware sería 1.300 − 450 = 850 (frente a B), muy por encima del arrepentimiento máximo de C, 280; con la celda revisada, su mayor arrepentimiento es 960, en el escenario de TO, frente a los 240 de A. La idea: una sola celda revisada rara vez invierte una recomendación robusta cuando contribuyen varios escenarios.

**EX003 — Valor de la información perfecta.** La mejor opción ahora es C, con un coste esperado de 290,6. Con información perfecta, el coste esperado es 0.15×450 + 0.03×240 + 0.10×330 + 0.72×0 = 107.7. EVPI ≈ 182,9 (miles de libras). Una evaluación de 60.000 £ merece la pena para esta decisión solo si puede mover la probabilidad de compromiso de TO al otro lado de los umbrales del 3 % o del 7 % que cambian la recomendación, y si su valor esperado de la información *imperfecta* se acerca a su coste. Una evaluación que no puede cambiar la elección tiene poco valor para la decisión, sea cual sea su calidad.

**EX004 — Registro de decisión con disenso.** Un registro con la máxima puntuación incluye el enunciado, la tabla, los tres conjuntos de creencias, el umbral (B por debajo de ~3 %, C entre ~3–7 %, A por encima de ~7 %), las tres reglas prefiriendo C, la elección de C por el director de Operaciones, el riesgo residual (exposición parcial del acceso remoto y capacidad manual parcial) asumido por ese director, el disenso del jefe de operaciones, que prefiere B porque «podemos perder el SCADA mañana», y un desencadenante de revisión como «un aviso creíble que informe del compromiso de nuestros productos de acceso remoto, o un incidente de TO en una empresa de servicios homóloga».

**EX005 — Auditoría de sesgos.** Disponibilidad (el ransomware del oleoducto), anclaje (el presupuesto de 400.000 £), optimismo sobre el respaldo manual (2009), recuento de controles (nueve de once hallazgos), deferencia/pensamiento de grupo (el presidente habló primero, no hubo otras opiniones). Remedios: estimaciones independientes antes de la discusión; pre mortem; exigir evidencia de simulacros recientes; puntuar las opciones por consecuencias; registrar el disenso y rotar quién habla primero.

### Capítulo 2: EX006–EX010

**EX006 — Haga corresponder una práctica.** El acceso de proveedores intermediado contribuye a las funciones Protect y Detect del CSF y a los principios del CAF relativos a la protección frente a los ciberataques y a la detección de eventos; aparece en los CPG de CISA en los temas de cuentas y acceso; la IEC 62443 lo encuadra como un conducto controlado hacia una zona. Que sea una obligación legal para una empresa de agua depende de la jurisdicción y de la transposición: verifíquelo con los asesores jurídicos frente al régimen aplicable (por ejemplo, las medidas de NIS2) en lugar de afirmarlo. La máxima puntuación mantiene la obligación separada de la orientación.

**EX007 — Cambie la política de evidencias.** Con un crédito de 0.25 para las afirmaciones: Merrow Water, 48 % verificado; Health, 54 %; Energy, 75 %; Port, 15 %. Se mantienen el orden y la prioridad de probar las afirmaciones; solo la cifra absoluta del puerto parece menos catastrófica. Una política defendible para un informe del foro: las afirmaciones reciben un crédito provisional de cero (para motivar las pruebas), con una nota que indique que algunas afirmaciones pueden ser ciertas, porque el propósito del informe es impulsar la verificación.

**EX008 — Plan de verificación.** Copias de seguridad sin conexión: restauración cronometrada de una copia identificada del SCADA a un servidor aislado; aceptación = restauración satisfactoria dentro de un tiempo establecido; ~2 días-persona. Acceso de proveedores: conciliar los registros del intermediario con las sesiones VPN del cortafuegos durante 30 días; aceptación = todas las sesiones emparejadas y aprobadas; ~1 día-persona. Segmentación entre TI y TO: inspeccionar las reglas del cortafuegos e intentar, con unas reglas de enfrentamiento, una ruta permitida frente a otra denegada desde la red corporativa hasta un equipo de control no productivo; aceptación = ninguna ruta inesperada; ~3 días-persona. La máxima puntuación exige pruebas de la realidad, no revisiones de políticas.

**EX009 — Operador sujeto a varios regímenes.** Regímenes candidatos: NIS2 (agua y electricidad como sectores esenciales), CER (resiliencia de las entidades críticas), DORA (filial de pagos) y, posiblemente, los códigos nacionales del sector eléctrico. Un único conjunto interno de controles con correspondencias con cada uno; los plazos de notificación de incidentes (alerta temprana / notificación / informe final según NIS2; notificación de incidentes de TIC según DORA; cualquier plazo específico del sector eléctrico) conciliados en un único procedimiento. Preguntas específicas para los asesores jurídicos: qué entidades están designadas; qué plazos vinculan a qué filial; si un solo informe puede satisfacer varios regímenes.

**EX010 — Critique una práctica.** El consejo quiere saber si un atacante puede perturbar la atención clínica. Una prueba externa anual sobre una muestra de la red clínica responde a una pregunta estrecha sobre esa muestra en esa ventana, con técnicas atenuadas por seguridad y, a menudo, excluyendo los dispositivos médicos. Una cartera mejor: una revisión guiada por las consecuencias de los peores resultados clínicos; monitorización continua y pruebas de restauración; pruebas en un entorno no productivo representativo; y una evaluación centrada en las rutas de los dispositivos médicos y de los proveedores. Límites: ninguna cartera elimina el riesgo residual; cada método necesita el consentimiento de operaciones.

<a id="glossary"></a>

## Glosario

**Registro de decisiones de arquitectura (ADR).** Registro breve de una elección de arquitectura: contexto, alternativas, decisión, consecuencias, verificación y desencadenante de revisión.

**Caso de aseguramiento.** Argumento estructurado de que una afirmación es cierta, con subafirmaciones, evidencias y refutaciones consideradas.

**Reloj de respaldo.** Cuánto tiempo puede un emplazamiento mantener su función esencial tras el fallo de una dependencia, usando su propio almacenamiento, combustible, batería o solución manual.

**Acceso de emergencia (*break-glass*).** Vía de acceso de emergencia que se usa cuando los controles de seguridad principales no están disponibles; debe tener alarma, quedar registrada y probarse, y no debe convertirse en rutina.

**Declarado / documentado / verificado.** Grados de evidencia de una práctica: afirmación, documento u observación mediante prueba o inspección.

**Conjunto de estrangulamiento.** El conjunto más pequeño de nodos cuya eliminación (o defensa perfecta) corta todas las rutas desde los puntos de entrada hasta un objetivo en un grafo de arquitectura.

**Diseño guiado por las consecuencias.** Diseñar la seguridad partiendo del resultado físico o de servicio intolerable y retrocediendo hasta las rutas digitales que podrían causarlo.

**Registro de decisión.** Registro contemporáneo de una decisión: enunciado, opciones, evidencias, juicios, reglas aplicadas, elección, riesgo residual, disenso y desencadenante de revisión.

**Diferencias en diferencias (DiD).** Estimación del efecto de un proyecto: el cambio en el grupo piloto menos el cambio en un grupo de comparación durante el mismo periodo.

**Valor esperado de la información perfecta (EVPI).** Lo máximo que quien decide debería pagar por una información que revele, antes de elegir, qué escenario ocurrirá.

**Índice de Herfindahl–Hirschman (HHI).** Suma de las cuotas porcentuales al cuadrado; medida de concentración que va de casi 0 a 10.000 (monopolio).

**Curva de excedencia de pérdidas (LEC).** La probabilidad de que la pérdida anual supere cada nivel; una forma de leer el riesgo que muestra la cola.

**Minimax.** Elegir la opción cuyo peor resultado sea el menos malo.

**Minimax del arrepentimiento.** Elegir la opción cuyo mayor arrepentimiento (coste adicional frente a la mejor opción en cada escenario) sea el menor.

**Tendencias paralelas.** El supuesto, en diferencias en diferencias, de que los grupos piloto y de comparación habrían cambiado en la misma medida sin el proyecto.

**Comprobación por permutación.** Evaluar una estimación preguntando cuán inusual es entre todas las formas de asignar las unidades a los grupos.

**Gráfico de comportamiento del proceso (XmR).** Gráfico que usa la propia historia de un indicador para separar la variación rutinaria de las señales de cambio.

**RACI.** Matriz que asigna los papeles de responsable de ejecutar (*Responsible*), responsable último (*Accountable*), consultado (*Consulted*) e informado (*Informed*) en las actividades; cada actividad crítica debe tener exactamente un responsable último.

**Desencadenante de revisión.** Observación declarada de antemano que reabre una decisión o una afirmación de aseguramiento.

**Apetito / tolerancia al riesgo.** Cuánto riesgo, y de qué tipo, retendrá una organización, y los límites de la variación aceptable; idealmente expresados en unidades de servicio con límites para la cola y la distribución.

**Unidades de servicio.** Unidades de la función esencial: horas-hogar de suministro, pacientes derivados, megavatios-hora entregados y similares.

**Paradoja de Simpson.** Patrón en el que una comparación agregada apunta en sentido contrario a todas las comparaciones dentro de los grupos, normalmente por un factor de confusión como el tamaño.

**Modelo de las Tres Líneas.** Modelo del IIA sobre los papeles: la dirección es dueña del riesgo (primera línea), las funciones especializadas de riesgo y cumplimiento (segunda) y el aseguramiento independiente (tercera).

**Intervalo de puntuación de Wilson.** Intervalo de confianza para una proporción que se comporta bien con muestras pequeñas y con tasas cercanas a 0 o a 1.

**Zonas y conductos.** Conceptos de la IEC 62443: grupos de activos con requisitos de seguridad comunes y las comunicaciones controladas entre ellos.

<a id="references"></a>

## Referencias

Las leyes, las orientaciones y las páginas públicas cambian. Las versiones y fechas que siguen son las consultadas para este borrador (octubre de 2026); vuelva a verificarlas antes de basarse en ellas. Una cita respalda la afirmación general que la acompaña en el texto, nunca los detalles del caso sintético. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

### Política, derecho y normas

- Bank for International Settlements, Committee on Payments and Market Infrastructures, and International Organization of Securities Commissions. [Guidance on Cyber Resilience for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d146.htm). June 2016.
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [National Security Memorandum on Critical Infrastructure Security and Resilience (overview)](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- European Union. [Regulation (EU) 2022/2554 on digital operational resilience for the financial sector (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- International Electrotechnical Commission. [IEC 62443-3-2:2020, Security for industrial automation and control systems — Part 3-2: Security risk assessment for system design](https://webstore.iec.ch/en/publication/30727). Catalogue page.
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final).
- National Institute of Standards and Technology. [SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://doi.org/10.6028/NIST.SP.800-82r3).
- National Institute of Standards and Technology. [SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1).
- National Institute of Standards and Technology. [SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final).
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29).
- National Institute of Standards and Technology. [NIST Privacy Framework](https://www.nist.gov/privacy-framework).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).
- U.S. Department of Justice. [Herfindahl-Hirschman Index](https://www.justice.gov/atr/herfindahl-hirschman-index).

### Incidentes y evidencia sectorial

- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01).
- Cybersecurity and Infrastructure Security Agency. [PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a). February 2024.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Dameff, C., Tully, J., Chan, T. C., et al. [Ransomware Attack Associated With Disruptions at Adjacent Emergency Departments in the US](https://doi.org/10.1001/jamanetworkopen.2023.12270). *JAMA Network Open*, 6(5), e2312270, 2023.
- Ghafur, S., Kristensen, S., Honeyford, K., Martin, G., Darzi, A., and Aylin, P. [A Retrospective Impact Analysis of the WannaCry Cyberattack on the NHS](https://doi.org/10.1038/s41746-019-0161-6). *npj Digital Medicine*, 2, 98, 2019.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Neprash, H. T., McGlave, C. C., Cross, D. A., et al. [Trends in Ransomware Attacks on US Hospitals, Clinics, and Other Health Care Delivery Organizations, 2016–2021](https://doi.org/10.1001/jamahealthforum.2022.4873). *JAMA Health Forum*, 3(12), e224873, 2022.
- U.S. Department of Energy, Office of Cybersecurity, Energy Security, and Emergency Response. [Colonial Pipeline Cyber Incident](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident).
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

### Métodos, análisis de decisiones y ética

- Association for Computing Machinery. [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics).
- Arp, D., Quiring, E., Pendlebury, F., et al. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). *USENIX Security*, 2022.
- Bochman, A., and Freeman, S. [Countering Cyber Sabotage: Introducing Consequence-Driven, Cyber-Informed Engineering (CCE)](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710). CRC Press, 2021.
- Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., and Havlin, S. [Catastrophic Cascade of Failures in Interdependent Networks](https://doi.org/10.1038/nature08932). *Nature*, 464, 1025–1028, 2010.
- Card, D., and Krueger, A. B. [Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania](https://www.jstor.org/stable/2118030). *American Economic Review*, 84(4), 772–793, 1994.
- Chamberlin, T. C. [The Method of Multiple Working Hypotheses](https://doi.org/10.1126/science.148.3671.754). *Science*, 148(3671), 754–759, 1965 (reprint of the 1890 paper).
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- Institute of Internal Auditors. [The IIA's Three Lines Model: An Update of the Three Lines of Defense](https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/). 2020.
- Kerr, N. L. [HARKing: Hypothesizing After the Results Are Known](https://doi.org/10.1207/s15327957pspr0203_4). *Personality and Social Psychology Review*, 2(3), 196–217, 1998.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *AAAI*, 2022.
- Klein, G. [Performing a Project Premortem](https://hbr.org/2007/09/performing-a-project-premortem). *Harvard Business Review*, September 2007.
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- National Society of Professional Engineers. [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics).
- NIST/SEMATECH. [e-Handbook of Statistical Methods, 6.3.2 What are Variables Control Charts?](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm).
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., and Mellor, D. T. [The Preregistration Revolution](https://doi.org/10.1073/pnas.1708274114). *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606, 2018.
- O'Hagan, A., Buck, C. E., Daneshkhah, A., et al. [Uncertain Judgements: Eliciting Experts' Probabilities](https://doi.org/10.1002/0470033312). Wiley, 2006.
- Pearl, J., and Bareinboim, E. [External Validity: From Do-Calculus to Transportability Across Populations](https://doi.org/10.1214/14-STS486). *Statistical Science*, 29(4), 579–595, 2014.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320, 768–770, 2000.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine*, 21(6), 11–25, 2001.
- Saltelli, A., Ratto, M., Andres, T., et al. [Global Sensitivity Analysis: The Primer](https://doi.org/10.1002/9780470725184). Wiley, 2008.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.
- Savage, L. J. [The Theory of Statistical Decision](https://doi.org/10.1080/01621459.1951.10500768). *Journal of the American Statistical Association*, 46(253), 55–67, 1951.
- Simpson, E. H. [The Interpretation of Interaction in Contingency Tables](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x). *Journal of the Royal Statistical Society Series B*, 13(2), 238–241, 1951.
- Smith, W. E. [Various Optimizers for Single-Stage Production](https://doi.org/10.1002/nav.3800030106). *Naval Research Logistics Quarterly*, 3(1–2), 59–66, 1956.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). *IEEE Symposium on Security and Privacy*, 2010.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003.
- Tversky, A., and Kahneman, D. [Judgment under Uncertainty: Heuristics and Biases](https://doi.org/10.1126/science.185.4157.1124). *Science*, 185(4157), 1124–1131, 1974.
- Wilson, E. B. [Probable Inference, the Law of Succession, and Statistical Inference](https://doi.org/10.1080/01621459.1927.10502953). *Journal of the American Statistical Association*, 22(158), 209–212, 1927.
