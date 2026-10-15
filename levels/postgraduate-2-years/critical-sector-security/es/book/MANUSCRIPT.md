# Infraestructura crítica y seguridad sectorial: práctica especializada avanzada

- Idioma: español neutro (`es`); curso de posgrado de especialización, dos años; aproximadamente 600 horas de estudio planificado (curso 161 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Los capítulos 1–12 de 12 tienen texto didáctico escrito, doce laboratorios sin conexión, los ejercicios EX001–EX060 y sus resultados resueltos correspondientes. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
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
3. [Infraestructura crítica y seguridad sectorial: evidencia especializada](#ch-03): evidencia en entornos de TO y mixtos, relojes y cronologías, preservación sin perturbar el proceso y hallazgos que separan la observación de la inferencia.
4. [Riesgo y ética avanzados](#ch-04): riesgo cuantificado con incertidumbre, excedencia de pérdidas, apetito de riesgo en unidades de servicio y quién soporta el riesgo residual.
5. [Infraestructura crítica y seguridad sectorial: alternativas de diseño](#ch-05): comparar arquitecturas como grafos de ataque y como sistemas operables, modos de fallo de los controles y registros de decisiones de arquitectura.
6. [Infraestructura crítica y seguridad sectorial: evaluación controlada](#ch-06): probar las detecciones y los simulacros antes de confiar en ellos, intervalos, carga de falsas alarmas y diseño seguro de las pruebas.
7. [Infraestructura crítica y seguridad sectorial: integración organizativa](#ch-07): modelos operativos, propiedad, concentración de proveedores e integración con la gestión de emergencias.
8. [Infraestructura crítica y seguridad sectorial: casos difíciles](#ch-08): cascadas, prioridades de restablecimiento, actualizaciones de confianza defectuosas, internos ambiguos y obligaciones en conflicto.
9. [Infraestructura crítica y seguridad sectorial: liderazgo y aseguramiento](#ch-09): liderar una función, informes al consejo, casos de aseguramiento, frescura de la evidencia y distinguir la señal del ruido.
10. [Lectura y crítica de la investigación](#ch-10): leer estudios, avisos y afirmaciones de proveedores para decidir; denominadores, confusión y transferencia.
11. [Proyecto aplicado](#ch-11): delimitar, ejecutar y evaluar con honestidad una mejora a escala de la organización.
12. [Revisión final y transferencia](#ch-12): integrar el curso, transferir decisiones entre sectores y planificar la práctica continuada.

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

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 12

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 12

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Infraestructura crítica y seguridad sectorial: evidencia especializada

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Identificar las fuentes de evidencia disponibles en un entorno mixto de TI y TO y lo que cada una puede y no puede mostrar.
2. Reconstruir una cronología a partir de fuentes cuyos relojes discrepan, usando eventos ancla, e indicar la incertidumbre restante.
3. Planificar una preservación de evidencias que no ponga en peligro el proceso físico.
4. Generar explicaciones alternativas e identificar la evidencia que permitiría discriminar entre ellas.
5. Redactar hallazgos que separen la observación, la inferencia y el juicio, con un nivel de confianza que la evidencia respalde.
6. Cumplir las obligaciones de notificación sin exagerar lo que se sabe.

El capítulo 2 calificó la evidencia de que los controles están implantados. Este capítulo trata de la evidencia sobre **lo que ocurrió**: el material que un especialista aporta a una revisión de incidentes, a un regulador, a una aseguradora o a un tribunal. El capítulo 6 aplica la misma disciplina a las pruebas planificadas.

### 3.1 El deber probatorio del especialista

Cuando ocurre algo inexplicado en un servicio esencial, muchas personas se forman rápidamente un relato: el proveedor, los operadores, la prensa, el regulador. El deber del especialista es establecer qué respalda la evidencia, con qué confianza, y qué sigue sin conocerse, y mantener esas cosas separadas bajo presión. Las recomendaciones del NIST sobre respuesta a incidentes enmarcan la respuesta como parte de la gestión global del riesgo, con la preparación, la detección, el análisis y la mejora vinculados a la gobernanza ([NIST SP 800-61 Rev. 3, 2025](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). Para la TO, la NIST SP 800-82 Rev. 3 añade que la respuesta debe proteger primero la seguridad funcional y el proceso ([NIST, 2023](https://doi.org/10.6028/NIST.SP.800-82r3)).

El caso del sector del agua del capítulo 2 muestra por qué esto importa. En febrero de 2021, un aviso describió el compromiso del sistema de control de una instalación de tratamiento de agua de EE. UU. mediante software de acceso remoto ([CISA, AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a)). En 2023 se informó de que el antiguo gerente municipal había dicho que el suceso fue probablemente un error de un empleado y no una intrusión externa ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)). Sea cual sea la verdad, el episodio muestra cómo un primer relato público puede endurecerse antes de que la evidencia esté completa, y cuánto depende el análisis posterior de lo que se preservó en su momento.

### 3.2 Fuentes de evidencia en un entorno mixto

| Fuente | Qué puede mostrar | Debilidades típicas |
|---|---|---|
| Registros del cortafuegos y de la VPN | Sesiones, cuentas, direcciones y horas en el perímetro | Retención corta; la NAT oculta los equipos; sin contenido |
| Registros del proveedor de identidad y del servidor de salto | Quién se autenticó, desde dónde, qué sesiones | Las cuentas compartidas o de servicio impiden la atribución |
| Registros de sistema Windows/Linux en HMI y estaciones de ingeniería | Inicios de sesión, procesos, cambios en archivos | A menudo desactivados en equipos de TO; los pequeños búferes locales se sobrescriben |
| Historiador del SCADA | Valores del proceso y órdenes de los operadores con etiquetas de origen | Hora tomada del reloj del servidor del historiador; la compresión puede descartar eventos breves; el «origen» puede ser una estación, no una persona |
| Estado y archivos de proyecto de los controladores (PLC) | Lógica y configuración actuales; a veces, contadores de cambios | La lectura puede requerir herramientas del proveedor; la interacción en línea entraña riesgo para el proceso |
| Capturas de red en la zona de control | Exactamente qué órdenes de protocolo se enviaron | Rara vez se recogen de forma continua; voluminosas |
| Cuadernos de los operadores y relevos de turno | Observaciones y decisiones humanas | Resolución de minutos o peor; escritos a posteriori; relojes de pared sin sincronizar |
| Entrevistas | Intención, contexto, acciones no registradas | La memoria reconstruye; los incentivos moldean los relatos |
| Registros de proveedores y suministradores | Sesiones remotas, mantenimiento, actualizaciones | En poder de un tercero; el acceso requiere cláusulas contractuales |

Un especialista conoce estas fuentes **antes** de un incidente y corrige las debilidades que más importan: hora sincronizada, retención más larga para los registros del perímetro y de identidad, cuentas nominativas y acceso contractual a los registros de los proveedores. El catálogo de controles del NIST incluye requisitos sobre el contenido, la retención y las marcas de tiempo de los registros de auditoría precisamente por esta razón ([NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)).

### 3.3 El tiempo es evidencia

El orden de los eventos suele decidir la explicación: ¿la sesión remota empezó antes o después de que cambiara el punto de consigna? Cada fuente registra la hora con su propio reloj, y los relojes de TO están con frecuencia sin sincronizar, desviados o ajustados a mano. Tres prácticas hacen defendibles las cronologías:

1. **Elija un reloj de referencia** cuya sincronización pueda verificar (por ejemplo, un cortafuegos sincronizado con una fuente horaria conocida y comprobado) y exprese en él todos los eventos.
2. **Estime el desfase de cada fuente a partir de eventos ancla**: un único momento real registrado por dos fuentes, como los dos extremos de la misma sesión de red o una consulta de sincronización que atraviesa un cortafuegos. Dos anclas independientes por fuente son mejores que una; la discrepancia entre ellas revela la deriva.
3. **Indique la incertidumbre residual** de cada fuente (la precisión del propio ancla, la resolución, pues un registro manuscrito puede tener solo minutos, y la deriva a lo largo del intervalo) y compruebe si alguna conclusión depende de una ordenación más ajustada que esa incertidumbre.

### 3.4 Preservar sin causar daño

La preservación de evidencias en la TO no debe crear el daño que investiga. Principios:

- **Primero la seguridad funcional y el proceso.** El responsable de operaciones decide si un sistema puede tocarse. Los pasos de preservación se planifican con él, no se imponen.
- **Recoja primero de la fuente menos intrusiva.** Los registros del perímetro, los registros de identidad, las exportaciones del historiador y las copias de seguridad suelen poder recogerse sin tocar la red de control. El estado de los controladores debe leerse con las herramientas soportadas por el proveedor y bajo control de cambios, o no leerse hasta que el proceso sea seguro.
- **Preserve la evidencia volátil cuando sea seguro.** La memoria y el estado de las conexiones activas en las HMI basadas en Windows y en los servidores de salto desaparecen al reiniciar; captúrelos si se puede prescindir del equipo.
- **Registre la cadena de custodia.** Quién recogió qué, cuándo, cómo y con qué hashes: la misma disciplina que en cualquier trabajo forense. Un hash criptográfico como SHA-256 ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)) demuestra después que un archivo exportado no se alteró.
- **Pregunte pronto a los proveedores.** Los registros de sesiones de los proveedores y de soporte remoto a menudo se sobrescriben según el calendario del propio proveedor.

### 3.5 Explicaciones alternativas

Un cambio del punto de consigna con una sesión remota cercana invita al relato «lo hizo un atacante». Un especialista enumera todas las explicaciones que podrían producir la misma evidencia y se pregunta qué las distinguiría: el método de las hipótesis de trabajo múltiples ([Chamberlin, 1965 reprint](https://doi.org/10.1126/science.148.3671.754)). Para un cambio inexplicado de la dosificación, las candidatas incluyen un intruso externo que usa una credencial robada, un ingeniero legítimo del proveedor que hace un cambio no registrado, un error de un operador en una HMI local, un script o una receta automatizados, un error de etiquetado del historiador y un fallo de un instrumento que el operador corrigió a mano. Cada una predice rastros distintos: el cambio de un intruso debería proceder de la estación remota después del inicio de sesión remoto; el trabajo planificado de un proveedor debería coincidir con un tique y con un patrón observado en otros emplazamientos; un error de un operador debería proceder de una estación local; una receta debería repetirse según un calendario; un error de etiquetado debería discrepar del registro propio del controlador.

### 3.6 Redactar hallazgos

Un hallazgo tiene cuatro partes: la **observación** con su fuente; la **inferencia** con sus supuestos; la **confianza**, en palabras que correspondan a rangos explícitos si su organización los usa; y la **consecuencia** para las decisiones. Por ejemplo: «El historiador registra un cambio del punto de consigna de dosificación de 1,8 a 2,6 mg/L atribuido a la estación HMI-JH2 a las 02:23:03 (hora del cortafuegos, ±10 s). La estación HMI-JH2 es el cliente de HMI del servidor de salto JH-2. La única sesión interactiva en JH-2 en ese momento era la de la cuenta vendor-svc, que se conectó a través de la VPN desde las 02:11:40. Evaluamos con confianza moderada que el cambio se hizo dentro de la sesión de vendor-svc; todavía no podemos decir quién usó esa cuenta. La cuenta la comparten cuatro ingenieros de Corvane». Esto es mucho más útil para quien decide que «la cuenta del proveedor fue comprometida».

### 3.7 Notificar por obligación

Muchos regímenes exigen ahora notificar pronto y por etapas los incidentes significativos. NIS2, por ejemplo, prevé una alerta temprana, una notificación más completa y un informe final en plazos fijos ([Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/)); NERC CIP y otras normas sectoriales tienen sus propios plazos. Las notificaciones tempranas deben hacerse antes de conocer los hechos. La contribución del especialista es hacer que sean **exactas sobre la incertidumbre**: decir qué se ha observado, qué se está investigando y qué no se sabe todavía, y evitar una atribución que la evidencia posterior pueda revocar. Haga un seguimiento de cada declaración externa para que los informes posteriores puedan corregir explícitamente los anteriores.

### 3.8 Ejemplo resuelto: una noche en Hollin (sintético)

En la planta de tratamiento de Hollin, el punto de consigna de dosificación de cloro subió brevemente de 1,8 a 2,6 mg/L y volvió a su valor en menos de un minuto. El cuaderno manuscrito del operador dice que el operador advirtió una alarma a las «02:20» y restableció el punto de consigna. El especialista reunió los registros del cortafuegos, del servidor de salto y del historiador. Con una lectura ingenua, el historiador muestra el cambio a las 02:06, *antes* de que comenzara la sesión VPN de vendor-svc a las 02:11, lo que exculparía a la sesión remota. Pero se sabe que el reloj del servidor del historiador no está sincronizado. Existen dos anclas: el inicio de una sesión TCP visto tanto por el cortafuegos como por el servidor de salto, y la propia consulta de sincronización del historiador que atraviesa el cortafuegos.

### 3.9 Actividad práctica: una cronología con relojes que discrepan

```python
# Lab 3 - reconstructing a timeline from sources whose clocks disagree (offline, standard library only)
# Synthetic: Merrow Water, Hollin treatment works, night of an unexplained chlorine dosing setpoint change.
# Each source records time in its own clock. Anchor events were seen by two sources at the same real moment.
from datetime import datetime, timedelta
T = lambda s: datetime.strptime(s, "%H:%M:%S")
EVENTS = [  # (source, local clock time, description)
    ("firewall",  "02:11:40", "VPN session opened for account vendor-svc"),
    ("firewall",  "02:13:05", "RDP from VPN pool to jump host JH-2 allowed"),
    ("jumphost",  "02:20:31", "interactive logon vendor-svc on JH-2"),
    ("jumphost",  "02:22:58", "HMI client launched on JH-2"),
    ("historian", "02:06:12", "dosing setpoint changed 1.8 -> 2.6 mg/L, source HMI-JH2"),
    ("historian", "02:06:50", "dosing setpoint restored 2.6 -> 1.8 mg/L, source HMI-OPS1"),
    ("ops-log",   "02:20",    "operator notices dosing alarm, restores setpoint (handwritten, minute only)"),
    ("firewall",  "02:31:10", "VPN session closed for vendor-svc"),
]
ANCHORS = [  # the same real moment seen by two sources: (source_a, time_a, source_b, time_b)
    ("firewall", "02:13:07", "jumphost", "02:20:33"),   # TCP session start seen at both ends
    ("firewall", "02:14:30", "historian", "01:57:39"),  # historian's NTP query passing the firewall
]
offset = {"firewall": timedelta(0)}  # firewall is the reference clock (NTP-synchronized, checked)
for a, ta, b, tb in ANCHORS:
    offset[b] = (T(ta) - T(tb)) + offset[a]
offset["ops-log"] = timedelta(0)  # a handwritten log has no known offset, only minute resolution
def show(title, rows):
    print(title)
    for t, src, d in rows: print(f"  {t.strftime('%H:%M:%S')}  {src:9s} {d}")
naive = sorted((T(t) if len(t) > 5 else T(t + ':00'), s, d) for s, t, d in EVENTS)
show("Naive order (raw clocks):", naive)
fixed = sorted(((T(t) if len(t) > 5 else T(t + ':00')) + offset[s], s, d) for s, t, d in EVENTS)
show("Corrected to firewall time:", fixed)
print("offsets:", {k: int(v.total_seconds()) for k, v in offset.items()}, "seconds")
```

Salida esperada:

```text
Naive order (raw clocks):
  02:06:12  historian dosing setpoint changed 1.8 -> 2.6 mg/L, source HMI-JH2
  02:06:50  historian dosing setpoint restored 2.6 -> 1.8 mg/L, source HMI-OPS1
  02:11:40  firewall  VPN session opened for account vendor-svc
  02:13:05  firewall  RDP from VPN pool to jump host JH-2 allowed
  02:20:00  ops-log   operator notices dosing alarm, restores setpoint (handwritten, minute only)
  02:20:31  jumphost  interactive logon vendor-svc on JH-2
  02:22:58  jumphost  HMI client launched on JH-2
  02:31:10  firewall  VPN session closed for vendor-svc
Corrected to firewall time:
  02:11:40  firewall  VPN session opened for account vendor-svc
  02:13:05  firewall  RDP from VPN pool to jump host JH-2 allowed
  02:13:05  jumphost  interactive logon vendor-svc on JH-2
  02:15:32  jumphost  HMI client launched on JH-2
  02:20:00  ops-log   operator notices dosing alarm, restores setpoint (handwritten, minute only)
  02:23:03  historian dosing setpoint changed 1.8 -> 2.6 mg/L, source HMI-JH2
  02:23:41  historian dosing setpoint restored 2.6 -> 1.8 mg/L, source HMI-OPS1
  02:31:10  firewall  VPN session closed for vendor-svc
offsets: {'firewall': 0, 'jumphost': -446, 'historian': 1011, 'ops-log': 0} seconds
```

**Interpretación.** El servidor de salto va 446 segundos (7 min 26 s) adelantado respecto del cortafuegos; el historiador va 1.011 segundos (16 min 51 s) atrasado. Una vez corregido, el orden se invierte: la sesión de vendor-svc se abre a las 02:11:40, el inicio de sesión en el servidor de salto sigue a la conexión RDP permitida dentro del mismo segundo (una comprobación de coherencia que respalda la primera ancla), el cliente de HMI arranca a las 02:15:32 y el cambio del punto de consigna desde la estación HMI-JH2 se produce a las 02:23:03, con un restablecimiento desde la estación de los operadores 38 segundos después. La cronología ingenua habría exculpado a la sesión remota; la corregida sitúa el cambio dentro de ella. Observe la incoherencia que queda: las «02:20» del registro manuscrito son tres minutos *antes* del cambio que describen. La explicación probable es que el reloj de pared de la sala de control va atrasado, pero eso es una inferencia; debe comprobarse contra el reloj de pared y registrarse, no «arreglarse» en silencio. El hallazgo sigue refiriéndose a la **sesión**, no a una persona, y las explicaciones alternativas (§3.5), un cambio legítimo pero no registrado de un ingeniero del proveedor frente al uso indebido de la cuenta compartida, siguen abiertas.

### 3.10 Errores comunes y límites

- Ordenar los eventos de distintas fuentes por sus marcas de tiempo sin corregir.
- Corregir los relojes con una sola ancla y no contrastarla nunca con una segunda.
- Tratar la etiqueta de «origen» del historiador como una persona.
- Tocar los controladores para recoger evidencias sin la decisión del responsable de operaciones.
- Dejar que el primer relato plausible defina qué evidencias se recogen.
- Escribir «comprometido» o «ataque» en las notificaciones tempranas cuando la evidencia solo respalda «cambio inexplicado durante una sesión remota».
- Olvidar que los registros de los proveedores caducan.

El límite es que la evidencia puede reducir las explicaciones, pero rara vez las elimina todas menos una. Un especialista informa de qué explicaciones siguen en pie y de qué las separaría; la decisión de actuar (por ejemplo, suspender el acceso de un proveedor) puede, y a menudo debe, tomarse antes de que se resuelva la atribución.

### Ejercicios — capítulo 3

**EX011 — Robustez del orden.** *Objetivo:* cuantificar cuánto depende una conclusión cronológica de una sola ancla. *Entradas:* el Lab 3. *Restricciones:* considere errores solo en el ancla del historiador. *Pasos:* (1) calcule cuántos segundos antes tendría que estar el cambio corregido del punto de consigna para preceder al arranque del cliente de HMI en JH-2; (2) cambie en un minuto la hora del cortafuegos del ancla del historiador (02:14:30 → 02:15:30), vuelva a ejecutarlo e informe de si cambia el orden; (3) indique qué evidencia independiente confirmaría el desfase del historiador. *Evidencia esperada:* cálculo, salida de la nueva ejecución y un párrafo. *Rúbrica:* 3 = margen calculado (451 s), la nueva ejecución muestra que el orden no cambia, se propone una segunda ancla independiente; 2 = falta una parte; 1 = no ejecutado; 0 = nada.

**EX012 — Plan de preservación.** *Objetivo:* planificar una recogida segura de evidencias. *Entradas:* el suceso de Hollin. *Restricciones:* la planta debe seguir produciendo agua; el responsable de operaciones tiene autoridad sobre los sistemas de control. *Pasos:* enumere las fuentes en orden de recogida con el método, quién lo aprueba, la volatilidad y el riesgo para el proceso; incluya la cadena de custodia y las solicitudes a los proveedores. *Evidencia esperada:* tabla y una justificación de un párrafo. *Rúbrica:* 3 = lo menos intrusivo primero, captura volátil de JH-2 antes de cualquier reinicio, lecturas de los controladores con aprobación de operaciones y herramientas del proveedor, hashes y custodia, registros de sesiones de Corvane solicitados de inmediato; 2 = orden parcialmente erróneo; 1 = pone en peligro el proceso; 0 = nada.

**EX013 — Redacte el hallazgo.** *Objetivo:* separar la observación, la inferencia, la confianza y la consecuencia. *Entradas:* la salida del Lab 3. *Restricciones:* 200 palabras; ninguna atribución a una persona. *Pasos:* redacte el hallazgo para el consejo y una versión de una frase para la notificación temprana al regulador. *Evidencia esperada:* ambos textos. *Rúbrica:* 3 = observaciones con su fuente, su base horaria y su incertidumbre, inferencia explícita, confianza indicada, consecuencia clara para las decisiones (por ejemplo, suspender la cuenta compartida), frase para el regulador exacta sobre lo desconocido; 2 = un elemento mezclado; 1 = afirma el compromiso como un hecho; 0 = nada.

**EX014 — Evidencia que discrimina.** *Objetivo:* aplicar las hipótesis de trabajo múltiples. *Entradas:* las seis explicaciones candidatas del §3.5. *Restricciones:* para cada una, una predicción que las demás no compartan. *Pasos:* construya una tabla con la explicación, la predicción distintiva, la fuente de evidencia y el estado actual (respaldada, contradicha, abierta). *Evidencia esperada:* tabla. *Rúbrica:* 3 = predicciones realmente discriminantes, estados coherentes con el Lab 3 (error del operador en una estación local contradicho para el propio cambio; uso legítimo del proveedor frente a uso indebido, abierto), siguiente evidencia identificada; 2 = algunas predicciones compartidas; 1 = solo una lista; 0 = nada.

**EX015 — Notificación por etapas.** *Objetivo:* redactar declaraciones externas que resistan la evidencia posterior. *Entradas:* el suceso de Hollin; suponga que Merrow Water está sujeta a un régimen de notificación de incidentes por etapas similar al del artículo 23 de NIS2. *Restricciones:* no interprete la legislación real para una entidad real; use marcadores para los plazos. *Pasos:* redacte la alerta temprana, la notificación y el esquema del informe final, mostrando cómo cada uno corrige o amplía el anterior. *Evidencia esperada:* tres textos breves. *Rúbrica:* 3 = alerta temprana factual y explícita sobre la incertidumbre, la notificación añade la cronología corregida y las acciones, el esquema del informe final incluye la causa raíz, las correcciones y las lecciones; 2 = el texto temprano exagera; 1 = afirma la atribución; 0 = nada.

### Síntesis del capítulo

La evidencia especializada es el material sobre el que descansan las decisiones y la rendición de cuentas. Conozca sus fuentes antes de un incidente y corrija las debilidades que importan: la hora, la retención, las cuentas nominativas y el acceso a los proveedores. Trate el tiempo como evidencia: elija un reloj de referencia, estime los desfases a partir de anclas e indique la incertidumbre residual. Preserve sin dañar el proceso, lo menos intrusivo primero y con cadena de custodia. Genere explicaciones alternativas y busque la evidencia que discrimine entre ellas. Redacte hallazgos que mantengan separadas la observación, la inferencia, la confianza y la consecuencia, y notifique pronto de un modo que la evidencia posterior amplíe en lugar de contradecir.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 12

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Riesgo y ética avanzados

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Construir una estimación cuantificada del riesgo con una incertidumbre explícita sobre la frecuencia y la gravedad, y leerla como una curva de excedencia de pérdidas en lugar de como un único número.
2. Expresar el apetito y la tolerancia al riesgo en unidades de servicio, con límites sobre la cola y no solo sobre la media.
3. Obtener y documentar el juicio experto de forma que pueda cuestionarse.
4. Analizar quién soporta el riesgo residual y reconocer cuándo una opción que es mejor en promedio es peor para un grupo concreto.
5. Aplicar principios éticos reconocidos a las decisiones de seguridad, a las pruebas y a la divulgación en los servicios esenciales.

El capítulo 1 comparó opciones con una tabla de escenarios. Este capítulo sustituye la tabla por distribuciones y añade la pregunta que las tablas de decisión ocultan: ¿*para quién* es mejor una opción? El capítulo 8 aplica ambas cosas a casos en los que cualquier elección perjudica a alguien.

### 4.1 Por qué engañan las estimaciones puntuales

Una entrada de un registro de riesgos como «probabilidad 3, impacto 4, puntuación 12» oculta tres cosas que una decisión necesita: con qué frecuencia, con qué gravedad y con cuánta incertidumbre. Las recomendaciones del NIST sobre evaluación de riesgos describen el riesgo como una función de la amenaza, la vulnerabilidad, la probabilidad y el impacto, y advierten de que las evaluaciones deben indicar sus supuestos y su incertidumbre ([NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)). Además, multiplicar puntuaciones ordinales hace aritmética con números que son solo etiquetas.

Un modelo mínimo mejor tiene dos partes: una distribución de **frecuencia** del número de eventos de pérdida que ocurren en un año y una distribución de **gravedad** de lo grave que es cada uno. En las infraestructuras, la gravedad suele tener asimetría a la derecha: la mayoría de las interrupciones son cortas y unas pocas son muy largas. La distribución lognormal es una elección habitual y sencilla para estas magnitudes; sus parámetros deben anclarse en la evidencia (duraciones de interrupciones pasadas, resultados de ejercicios, incidentes de organizaciones similares) y la propia elección debe registrarse como un supuesto. Simular muchos años da una distribución de la pérdida anual, que puede resumirse de tres maneras: la **media** (lo que se paga en promedio), la **probabilidad de superar** los umbrales que importan y un **percentil alto** como el 99 (un año malo de uno entre cien). Representar la probabilidad de excedencia frente a la pérdida da la **curva de excedencia de pérdidas** (LEC, por sus siglas en inglés).

### 4.2 Apetito y tolerancia en unidades de servicio

El **apetito de riesgo** es la cantidad y el tipo de riesgo que una organización está dispuesta a buscar o retener; la **tolerancia** fija los límites de la variación aceptable. El NIST CSF 2.0 sitúa ambos dentro de la gobernanza ([NIST, 2024](https://doi.org/10.6028/NIST.CSWP.29)). En un servicio esencial, las declaraciones de apetito deben formularse en unidades de servicio y deben acotar la cola. Por ejemplo (sintético): «Merrow Water no aceptará una probabilidad anual superior al 2 % de una interrupción relacionada con ciberincidentes que supere un millón de horas-hogar de suministro, ni ningún escenario creíble en el que los hogares de un solo distrito se queden sin suministro durante más de 48 horas sin una provisión alternativa». La primera cláusula acota la LEC; la segunda acota la *distribución*, un tema al que volvemos en el §4.5.

### 4.3 El juicio experto como evidencia

Cuando los datos escasean, los parámetros de frecuencia y gravedad proceden de personas. La obtención estructurada (definir las magnitudes con precisión, formar a los expertos en calibración, pedir cuantiles en lugar de valores únicos, agregar a varios expertos y registrar la justificación) hace que el juicio sea inspeccionable ([O'Hagan et al., 2006](https://doi.org/10.1002/0470033312)). Reglas prácticas para el especialista: pregunte por magnitudes observables («¿cuántas horas se tardaría en restablecer el suministro a Upper Merrow tras una pérdida total del SCADA?») en lugar de por probabilidades abstractas; pida primero un intervalo del 90 % y después una mediana; pida tasas base de operadores comparables; y registre la persona, la fecha, la pregunta y la justificación, para poder revisar la estimación cuando llegue evidencia.

### 4.4 La ética en la seguridad de los servicios esenciales

Las decisiones de seguridad en las infraestructuras distribuyen el daño. Varios marcos consolidados ayudan a razonar sobre ellas:

- El **Informe Menlo** adaptó los principios de la ética de la investigación (respeto por las personas, beneficencia, justicia) a la investigación en tecnologías de la información y la comunicación, y añadió el respeto por la ley y el interés público ([Dittrich and Kenneally, 2012](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf)). Sus principios se aplican directamente a las pruebas y a la recogida de datos en entornos operativos.
- Los códigos profesionales, como el [ACM Code of Ethics](https://www.acm.org/code-of-ethics) y el [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics), sitúan el bienestar y la seguridad del público por encima del interés del empleador o del cliente, y exigen honestidad sobre los límites de la propia competencia y de la seguridad de un sistema.
- La legislación de protección de datos impone deberes al tratamiento de datos personales en la monitorización de seguridad y la gestión de incidentes ([GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)); los marcos de privacidad, como el [NIST Privacy Framework](https://www.nist.gov/privacy-framework), ayudan a gestionar esos deberes en el diseño. *Nota para el lector hispanohablante:* en España, el RGPD se complementa con la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales; en América Latina rige la ley de cada país, por ejemplo la Ley 25.326 en Argentina o la Ley 1581 de 2012 en Colombia.

Para un especialista hay cuatro preguntas éticas recurrentes. **Distribución:** ¿quién soporta el riesgo residual de la opción elegida y tuvo voz en la decisión? **Proporcionalidad:** ¿es la intrusión de una medida de seguridad (la monitorización del personal, la restricción del acceso de pacientes o clientes) proporcionada al daño que evita? **Honestidad:** ¿se comunican los riesgos y las incertidumbres con veracidad a quienes deciden y, cuando procede, al público? **Divulgación:** cuando descubre una debilidad que también afecta a otros (un producto de un proveedor usado por otras empresas de servicios), ¿cómo los protege sin armar a los atacantes? Los procesos de divulgación coordinada de vulnerabilidades existen exactamente para este caso ([CISA, CVD Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program)).

### 4.5 Quién soporta el riesgo residual

Las medidas agregadas (el total de horas-hogar perdidas, la pérdida esperada) pueden favorecer opciones que protegen zonas densas y bien servidas, porque proteger un poco a muchas personas puntúa más que proteger mucho a pocas. Por eso un especialista debe informar, junto a los totales, de la **carga per cápita por grupo** (distrito, tipo de cliente) y de la carga sobre las **personas con menos capacidad para afrontarla**, como los hogares con dependencia médica del agua o de la electricidad. Ni los totales ni las medidas per cápita zanjan la cuestión; elegir entre ellos es un juicio de valor que corresponde a quien decide y rinde cuentas, informado por los deberes legales (por ejemplo, los deberes hacia los clientes vulnerables) y por el apetito declarado de la organización. El deber ético del especialista es hacer visible la distribución para que el compromiso se elija con conocimiento de causa.

### 4.6 Ejemplo resuelto: dos opciones con el mismo presupuesto (sintético)

Merrow Water abastece a tres distritos. Harbour es urbano (60.000 hogares); Fenley, periurbano (25.000); Upper Merrow, rural (6.000 hogares en una única tubería troncal, con una telemetría lenta de restablecer y largos tiempos de desplazamiento de las cuadrillas). Las interrupciones del suministro relacionadas con ciberincidentes se modelan como eventos de Poisson con una duración lognormal (mediana de 8 horas). Actualmente, el restablecimiento en Upper Merrow tarda el triple. Dos opciones cuestan lo mismo:

- **X: reforzar el SCADA central**: reduce la frecuencia de eventos de 0,30 a 0,20 al año en todas partes; no hace nada por el largo restablecimiento de Upper Merrow.
- **Y: segunda alimentación y control local para Upper Merrow**: deja la frecuencia en 0,30, pero reduce el restablecimiento de Upper Merrow a 0,75 de la duración base.

Los hogares vulnerables (con necesidades médicas o de cuidados registradas) se cuentan por separado: 900 en Harbour, 500 en Fenley y 400 en Upper Merrow.

### 4.7 Actividad práctica: excedencia de pérdidas y distribución

```python
# Lab 4 - same budget, different people: loss exceedance and the distribution of harm (offline, stdlib only)
# Synthetic: Merrow Water supply interruptions caused by cyber events. Two options cost the same.
import random, math
random.seed(4)
YEARS = 20000
DISTRICTS = {  # name: (households, share of interruption events that hit this district, vulnerable households)
    "Harbour (urban)":  (60000, 0.40, 900),
    "Fenley (suburban)": (25000, 0.25, 500),
    "Upper Merrow (rural, single main)": (6000, 0.35, 400),
}
def poisson(lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= random.random()
        if p < L: return k
        k += 1
def simulate(freq, hours_mu, hours_sigma, rural_hours_factor):
    annual_hh_hours = []; per_district = {d: 0.0 for d in DISTRICTS}; vuln = {d: 0.0 for d in DISTRICTS}
    for _ in range(YEARS):
        total = 0.0
        for _ in range(poisson(freq)):
            hours = random.lognormvariate(hours_mu, hours_sigma)
            r = random.random(); acc = 0
            for d, (hh, share, v) in DISTRICTS.items():
                acc += share
                if r < acc:
                    h = hours * (rural_hours_factor if d.startswith("Upper") else 1.0)
                    per_district[d] += hh * h; vuln[d] += v * h; total += hh * h
                    break
        annual_hh_hours.append(total)
    return annual_hh_hours, per_district, vuln
OPTIONS = {
    "X: harden central SCADA (fewer events)":      (0.20, math.log(8), 0.9, 3.0),
    "Y: second feed + local control Upper Merrow": (0.30, math.log(8), 0.9, 0.75),
}
for name, args in OPTIONS.items():
    loss, per, vul = simulate(*args)
    loss.sort()
    mean = sum(loss) / YEARS
    p_any = sum(1 for x in loss if x > 0) / YEARS
    p_big = sum(1 for x in loss if x > 1_000_000) / YEARS
    p99 = loss[int(0.99 * YEARS)]
    print(name)
    print(f"  mean household-hours/yr {mean:9.0f}  P(any)={p_any:.3f}  P(>1M hh-h)={p_big:.4f}  99th pct {p99:9.0f}")
    for d, (hh, share, v) in DISTRICTS.items():
        print(f"  {d:34s} hours per household/yr {per[d]/YEARS/hh:5.2f}   vulnerable-household-hours/yr {vul[d]/YEARS:7.0f}")
```

Salida esperada:

```text
X: harden central SCADA (fewer events)
  mean household-hours/yr     88346  P(any)=0.183  P(>1M hh-h)=0.0204  99th pct   1498603
  Harbour (urban)                    hours per household/yr  0.97   vulnerable-household-hours/yr     872
  Fenley (suburban)                  hours per household/yr  0.64   vulnerable-household-hours/yr     318
  Upper Merrow (rural, single main)  hours per household/yr  2.39   vulnerable-household-hours/yr     956
Y: second feed + local control Upper Merrow
  mean household-hours/yr    117262  P(any)=0.261  P(>1M hh-h)=0.0305  99th pct   1920694
  Harbour (urban)                    hours per household/yr  1.48   vulnerable-household-hours/yr    1332
  Fenley (suburban)                  hours per household/yr  0.91   vulnerable-household-hours/yr     453
  Upper Merrow (rural, single main)  hours per household/yr  0.96   vulnerable-household-hours/yr     386
```

**Interpretación.** En todas las medidas agregadas X es mejor: una pérdida media de 88.346 frente a 117.262 horas-hogar al año; una probabilidad anual del 2,0 % frente al 3,1 % de superar un millón de horas-hogar; un percentil 99 más bajo. Frente al apetito del §4.2, X se sitúa en el límite del 2 % para la cola (0,0204, dentro del error de simulación del límite) e Y lo incumple claramente. Pero la **distribución** invierte el panorama. Con X, un hogar de Upper Merrow pierde en promedio 2,39 horas al año (más del doble que un hogar urbano y casi cuatro veces lo que pierde uno periurbano), y los 400 hogares vulnerables de Upper Merrow soportan 956 horas-hogar vulnerable al año, más que los 900 hogares de Harbour. Y reduce la carga rural a 0,96 horas por hogar y las horas-hogar vulnerable rurales a 386, a costa de cargas mayores en otros lugares. El total de horas-hogar vulnerable es casi idéntico (unas 2.146 con X y 2.171 con Y): las opciones apenas difieren en cuánto daño recae sobre las personas vulnerables en conjunto, pero sí, y mucho, en *qué* personas vulnerables lo soportan. La segunda cláusula del apetito (ningún distrito sin suministro más de 48 horas) exigiría examinar la cola de Upper Merrow, que el resumen no muestra; esa es la ampliación del EX016.

El análisis no decide entre X e Y. Muestra que «X es mejor» solo es cierto desde una perspectiva utilitarista agregada y que la elección concentra el riesgo en una pequeña población rural. Una recomendación defendible podría combinar X con medidas no técnicas más baratas para Upper Merrow (agua embotellada preposicionada, un registro prioritario de hogares vulnerables), y debe dejar constancia del juicio de valor.

### 4.8 Errores comunes y límites

- Multiplicar puntuaciones ordinales y tratar el producto como una magnitud.
- Informar solo de la pérdida anual media de un riesgo de cola pesada.
- Expresar el apetito de riesgo como un color o un adjetivo en lugar de como un límite en unidades de servicio.
- Tratar las cifras obtenidas de expertos como datos y descartar el registro de la obtención.
- Informar solo del beneficio agregado, de modo que el daño concentrado en grupos pequeños resulta invisible.
- Presentar un juicio de valor (agregado frente a distribución) como un resultado técnico.
- Guardar silencio sobre una vulnerabilidad que afecta a otros operadores porque divulgarla resulta incómodo.

Los límites del modelo son los de sus supuestos: la independencia de Poisson ignora las campañas que golpean varios emplazamientos a la vez; la lognormal puede subestimar las interrupciones más largas; los repartos entre distritos son juicios. Si se cambian, los números se mueven; el *método* de mostrar la distribución junto a los totales, no.

### Ejercicios — capítulo 4

**EX016 — Mejora rural parcial.** *Objetivo:* ver cómo responde la distribución a una opción más débil. *Entradas:* el Lab 4. *Restricciones:* cambie el factor de duración rural de Y de 0,75 a 1,5 (la segunda alimentación se retrasa; solo se entrega el control local). *Pasos:* (1) vuelva a ejecutarlo; (2) informe de las horas por hogar de Upper Merrow y de las horas-hogar vulnerable con la Y modificada; (3) compárelas con X y con la Y original; (4) amplíe el laboratorio para que informe de la probabilidad de que Upper Merrow sufra en un año una única interrupción de más de 48 horas con X y con Y. *Evidencia esperada:* salidas y un párrafo. *Rúbrica:* 3 = cifras de la Y modificada correctas (1,93 horas; 771 horas-hogar vulnerable), todavía mejor para Upper Merrow que X pero mucho menos que la Y original, ampliación de 48 horas implementada con una comprobación correcta por evento; 2 = falta la ampliación; 1 = no ejecutado; 0 = nada.

**EX017 — Memorando de análisis ético.** *Objetivo:* aplicar principios éticos a la elección entre X e Y. *Entradas:* §4.4–4.7. *Restricciones:* 400 palabras; principios del Informe Menlo y de un código profesional. *Pasos:* (1) identifique los grupos afectados y su voz; (2) analice la beneficencia y la justicia; (3) indique el juicio de valor que debe hacer el consejo; (4) recomiende una opción combinada con medidas no técnicas. *Evidencia esperada:* memorando. *Rúbrica:* 3 = grupos concretos, el compromiso entre la perspectiva agregada y la distributiva se nombra como un juicio, recomendación combinada concreta, se respeta el deber de honestidad hacia el consejo; 2 = principios enumerados pero no aplicados; 1 = afirma que X o Y es técnicamente correcta; 0 = nada.

**EX018 — Protocolo de obtención.** *Objetivo:* obtener parámetros de gravedad defendibles. *Entradas:* la pregunta «¿cuánto se tardaría en restablecer el suministro a Upper Merrow tras la pérdida total del SCADA?». *Restricciones:* tres expertos; magnitud observable; cuantiles. *Pasos:* (1) defina la magnitud con precisión; (2) redacte el guion de obtención, incluida una pregunta de calibración; (3) explique cómo agregaría y registraría las respuestas. *Evidencia esperada:* protocolo. *Rúbrica:* 3 = magnitud inequívoca (eventos de inicio y fin definidos), se piden los cuantiles 5, 50 y 95, obtención independiente antes de la discusión, calibración y registro conservados; 2 = se piden valores únicos; 1 = probabilidad de un evento vago; 0 = nada.

**EX019 — Declaración de apetito.** *Objetivo:* formular el apetito y la tolerancia en unidades de servicio. *Entradas:* Merrow Health (tres hospitales, dependencia de un servicio de ambulancias). *Restricciones:* al menos un límite sobre la cola y uno sobre la distribución; medibles con los datos propios de la organización. *Pasos:* redáctela; después pruébela con un escenario plausible e indique si se incumple. *Evidencia esperada:* declaración y prueba. *Rúbrica:* 3 = unidades de servicio (por ejemplo, horas de desvío del servicio de urgencias, tratamientos urgentes retrasados), límites de cola y de distribución medibles, prueba honesta; 2 = solo promedios; 1 = adjetivos; 0 = nada.

**EX020 — Dilema de divulgación.** *Objetivo:* gestionar una debilidad que afecta a otros. *Entradas:* durante una revisión, Merrow Water descubre que la herramienta de soporte remoto de Corvane acepta una credencial por defecto en un puerto de mantenimiento; Corvane da soporte a otras empresas de servicios de la región. *Restricciones:* ninguna prueba fuera de los propios sistemas de Merrow; ninguna divulgación pública antes de un proceso coordinado. *Pasos:* (1) acciones de protección inmediatas para Merrow; (2) vía de notificación a Corvane y, si hace falta, a un coordinador; (3) qué decir al foro de resiliencia y cuándo; (4) justificación ética. *Evidencia esperada:* plan. *Rúbrica:* 3 = primero se protegen los sistemas propios, notificación privada al proveedor con evidencia, uso de un proceso de divulgación coordinada si el proveedor no actúa, el foro se informa de un modo que protege a los demás sin publicar detalles de explotación, principios citados; 2 = falta un paso; 1 = prueba sistemas de otras empresas de servicios o publica; 0 = nada.

### Síntesis del capítulo

Cuantifique el riesgo como frecuencia y gravedad con una incertidumbre explícita, y léalo a través de la curva de excedencia de pérdidas, no de una única puntuación. Formule el apetito y la tolerancia en unidades de servicio, con límites sobre la cola y sobre la distribución. Trate el juicio experto como evidencia que debe obtenerse con cuidado y registrarse. Muestre quién soporta el riesgo residual (per cápita y entre quienes tienen menos capacidad para afrontarlo), porque las opciones que son mejores en promedio pueden concentrar el daño. Aplique principios éticos reconocidos a las elecciones, las pruebas y la divulgación, y mantenga visibles los juicios de valor como juicios que corresponden a quien decide y rinde cuentas.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 12

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Infraestructura crítica y seguridad sectorial: alternativas de diseño

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Generar alternativas de arquitectura realmente distintas para un problema de seguridad en un servicio esencial, partiendo de las consecuencias y no de los productos.
2. Representar las alternativas como grafos de rutas permitidas y compararlas por sus rutas, sus puntos de estrangulamiento y las barreras de cada ruta.
3. Evaluar cada alternativa como un sistema operable: los modos de fallo de los propios controles de seguridad, el acceso de emergencia, la mantenibilidad y el personal que debe operarlo.
4. Combinar la evidencia de seguridad, operabilidad y coste en una recomendación, usando los métodos de decisión de los capítulos 1 y 4.
5. Dejar constancia de la elección en un registro de decisión de arquitectura.

El capítulo 4 cuantificó el riesgo; este capítulo muestra dónde lo cambian las decisiones de diseño. Después, el capítulo 6 comprueba si un diseño elegido funciona como se afirma.

### 5.1 Partir de la consecuencia

Las revisiones de arquitectura suelen partir de un producto («¿deberíamos comprar un diodo de datos?») o de un patrón («necesitamos confianza cero»). Un especialista parte de la **consecuencia que debe evitarse** y trabaja hacia atrás hasta las rutas digitales que podrían causarla. La ingeniería impulsada por las consecuencias e informada por la ciberseguridad, desarrollada en el Idaho National Laboratory, formaliza este enfoque: identificar las funciones cuyo fallo sería intolerable, mapear los sistemas y las dependencias que podrían causarlo y elegir mitigaciones de ingeniería (incluidas las no digitales, como los límites mecánicos) que eliminen o acoten la consecuencia ([INL, CCE](https://inl.gov/national-security/cce/); [Bochman and Freeman, 2021](https://www.routledge.com/Countering-Cyber-Sabotage-Introducing-Consequence-Driven-Cyber-Informed-Engineering-CCE/Bochman-Freeman/p/book/9780367673710)). En la planta de Hollin de Merrow Water, la consecuencia intolerable es que una dosis de cloro no segura llegue a los clientes; la pregunta de diseño es cómo debería funcionar el acceso remoto al controlador de dosificación, si es que debe existir.

La mitigación no digital merece el primer lugar en el conjunto de opciones. Una bomba dosificadora dimensionada de modo que físicamente no pueda superar una dosis segura, o un analizador independiente que dispare la dosificación en un límite estricto, acota la consecuencia pase lo que pase en la red. Después se eligen los controles digitales para reducir la frecuencia de los intentos sobre lo que queda.

### 5.2 Principios que generan alternativas

Los principios de diseño clásicos siguen generando buenas alternativas: economía del mecanismo, valores por defecto a prueba de fallos, mediación completa y mínimo privilegio ([Saltzer and Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939)). La IEC 62443 los aplica a los sistemas de control mediante **zonas** (grupos de activos con requisitos de seguridad comunes) y **conductos** (la comunicación controlada entre zonas) ([ISA overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). La arquitectura de confianza cero traslada la aplicación de las políticas de la ubicación en la red a decisiones por sesión basadas en la identidad, el dispositivo y el contexto ([NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)). La ingeniería de ciberresiliencia añade técnicas (segmentación, no persistencia, diversidad, redundancia, integridad fundamentada) orientadas a seguir operando a pesar del compromiso, y no solo a evitarlo ([NIST SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1)). Cada principio apunta a un diseño distinto; usar varios de forma deliberada produce alternativas que difieren en su naturaleza.

### 5.3 Los diseños como grafos

Una representación sencilla y potente: los nodos son sistemas, las aristas dirigidas son conexiones permitidas y cada arista lleva la barrera que un intruso debe superar para usarla. Tres medidas permiten entonces comparar diseños:

- **Número de rutas** desde puntos de entrada plausibles hasta el activo que soporta la consecuencia. Menos es mejor, pero solo junto con la siguiente medida.
- **Conjunto mínimo de puntos de estrangulamiento**: el menor número de nodos cuya eliminación (o defensa perfecta) corta todas las rutas. Un único punto de estrangulamiento fuerte es más fácil de defender, monitorizar y evidenciar que varios débiles; también es un punto único de fallo para las operaciones legítimas (§5.4).
- **Fuerza de las barreras a lo largo de cada ruta**: una ruta cuyas aristas posteriores a la entrada inicial no llevan ninguna barrera ("none") permite que un punto de apoyo se convierta en control.

El grafo debe incluir las **rutas inesperadas** que contienen los entornos reales: conexiones del historiador, enlaces de copia de seguridad, módems de proveedores, agentes de monitorización en la nube. Muchas debilidades de arquitectura no están en el diseño previsto, sino en la ruta que alguien añadió después por comodidad. El análisis de grafos no demuestra la seguridad; hace explícitos y contables los supuestos.

### 5.4 Los diseños como sistemas operables

Un diseño seguro sobre el papel puede hacer fracasar las operaciones. Para cada alternativa, pregunte:

1. **¿Qué ocurre cuando falla el control de seguridad?** Si el intermediario de acceso está caído durante una emergencia nocturna, ¿cómo llega un ingeniero al controlador? Debe existir y probarse una ruta de **acceso de emergencia** (credenciales selladas, presencia física, una vía de emergencia grabada y con alarma); si no, los operadores construirán la suya.
2. **¿Quién lo opera?** Un diseño que necesita competencias que la organización no tiene, o un proveedor al que no puede exigir responsabilidades, se degradará.
3. **¿Cómo se modifica?** Cada excepción a una regla es una arista nueva en el grafo; los diseños que facilitan el trabajo legítimo reducen la presión para crear excepciones.
4. **¿Cuánto cuesta a lo largo de su vida?** Licencias, personal, pruebas, renovaciones.
5. **¿Qué efecto tiene sobre la monitorización?** Los flujos de datos unidireccionales pueden proteger una red de control y, aun así, permitir que el negocio vea los datos del proceso; también limitan el diagnóstico remoto.

### 5.5 Ejemplo resuelto: tres diseños de acceso remoto en Hollin (sintético)

Merrow Water tiene tres diseños candidatos para el acceso remoto a la red de control de Hollin:

- **D1 VPN plana**: la configuración actual; la VPN de proveedores y personal llega directamente a la red de control; el historiador es accesible desde la red corporativa.
- **D2 VPN más servidor de salto**: MFA en la VPN; todo el acceso interactivo a través de un servidor de salto bastionado; el historiador se traslada a una DMZ.
- **D3 acceso intermediado con historiador unidireccional**: acceso remoto solo a través de un intermediario de acceso que exige MFA y aprobación por sesión, con sesiones grabadas y limitadas en el tiempo, que llegan a una única estación de trabajo de ingeniería; el historiador se replica hacia la DMZ a través de un enlace unidireccional; el interruptor de llave del controlador de dosificación se deja en RUN, lo que (en este controlador sintético) bloquea las descargas de programas.

Se modelan dos puntos de entrada: internet y un correo de *phishing* que llega a un PC corporativo.

### 5.6 Actividad práctica: rutas y puntos de estrangulamiento

```python
# Lab 5 - comparing three remote-access architectures as graphs (offline, standard library only)
# Synthetic: paths from the internet to the dosing PLC at Merrow Water's Hollin works under three designs.
# An edge is a permitted connection; its label is what an intruder must defeat to use it.
from itertools import combinations
DESIGNS = {
 "D1 flat VPN": {
   "internet": [("vpn", "password")],
   "vpn": [("hmi", "none"), ("eng-ws", "none"), ("historian", "none")],
   "corp-pc": [("vpn", "none"), ("historian", "password")],
   "eng-ws": [("plc", "none")], "hmi": [("plc", "none")], "historian": [("hmi", "none")],
   "email": [("corp-pc", "user click")], "plc": []},
 "D2 VPN + jump host": {
   "internet": [("vpn", "MFA")],
   "vpn": [("jump", "password")], "corp-pc": [("jump", "password"), ("historian-dmz", "password")],
   "jump": [("hmi", "password"), ("eng-ws", "password")],
   "historian-dmz": [("historian", "none")], "historian": [("hmi", "none")],
   "eng-ws": [("plc", "none")], "hmi": [("plc", "none")], "email": [("corp-pc", "user click")], "plc": []},
 "D3 brokered access + one-way historian": {
   "internet": [("broker", "MFA + per-session approval")],
   "broker": [("eng-ws", "recorded session, time-boxed")],
   "corp-pc": [("broker", "MFA + per-session approval")],
   "historian": [("historian-dmz", "one-way")],  # data leaves OT only; nothing flows back
   "eng-ws": [("plc", "PLC key switch in RUN blocks writes")], "hmi": [("plc", "none")],
   "email": [("corp-pc", "user click")], "historian-dmz": [], "plc": []},
}
ENTRY, TARGET = ["internet", "email"], "plc"
def paths(g, node, seen):
    if node == TARGET: yield [node]; return
    for nxt, _ in g.get(node, []):
        if nxt not in seen:
            for rest in paths(g, nxt, seen | {nxt}): yield [node] + rest
def reachable(g, removed):
    stack = [e for e in ENTRY if e not in removed]; seen = set(stack)
    while stack:
        n = stack.pop()
        for nxt, _ in g.get(n, []):
            if nxt not in seen and nxt not in removed: seen.add(nxt); stack.append(nxt)
    return TARGET in seen
for name, g in DESIGNS.items():
    ps = [p for e in ENTRY for p in paths(g, e, {e})]
    inner = sorted({n for n in g if n not in ENTRY + [TARGET]})
    cut = next(c for k in range(1, len(inner) + 1) for c in combinations(inner, k) if not reachable(g, set(c)))
    free = [p for p in ps if all(lbl == "none" for a, b in zip(p, p[1:]) for nxt, lbl in g[a] if nxt == b and a not in ENTRY)]
    print(f"{name}: {len(ps)} paths; smallest chokepoint set {list(cut)}; "
          f"paths with no barrier after the first hop: {len(free)}")
    for p in ps:
        bars = [lbl for a, b in zip(p, p[1:]) for nxt, lbl in g[a] if nxt == b]
        print("   ", " -> ".join(p), "|", ", ".join(bars))
```

Salida esperada:

```text
D1 flat VPN: 7 paths; smallest chokepoint set ['corp-pc', 'vpn']; paths with no barrier after the first hop: 6
    internet -> vpn -> hmi -> plc | password, none, none
    internet -> vpn -> eng-ws -> plc | password, none, none
    internet -> vpn -> historian -> hmi -> plc | password, none, none, none
    email -> corp-pc -> vpn -> hmi -> plc | user click, none, none, none
    email -> corp-pc -> vpn -> eng-ws -> plc | user click, none, none, none
    email -> corp-pc -> vpn -> historian -> hmi -> plc | user click, none, none, none, none
    email -> corp-pc -> historian -> hmi -> plc | user click, password, none, none
D2 VPN + jump host: 5 paths; smallest chokepoint set ['corp-pc', 'jump']; paths with no barrier after the first hop: 0
    internet -> vpn -> jump -> hmi -> plc | MFA, password, password, none
    internet -> vpn -> jump -> eng-ws -> plc | MFA, password, password, none
    email -> corp-pc -> jump -> hmi -> plc | user click, password, password, none
    email -> corp-pc -> jump -> eng-ws -> plc | user click, password, password, none
    email -> corp-pc -> historian-dmz -> historian -> hmi -> plc | user click, password, none, none, none
D3 brokered access + one-way historian: 2 paths; smallest chokepoint set ['broker']; paths with no barrier after the first hop: 0
    internet -> broker -> eng-ws -> plc | MFA + per-session approval, recorded session, time-boxed, PLC key switch in RUN blocks writes
    email -> corp-pc -> broker -> eng-ws -> plc | user click, MFA + per-session approval, recorded session, time-boxed, PLC key switch in RUN blocks writes
```

**Interpretación.** D1 tiene siete rutas; en seis de ellas nada se interpone entre el primer punto de apoyo y el controlador. Su conjunto mínimo de puntos de estrangulamiento es de dos nodos. D2 elimina todas las rutas sin barreras y añade MFA, pero el grafo revela un defecto que el documento de diseño no mencionaba: la ruta `corp-pc → historian-dmz → historian → hmi → plc`. Trasladar el historiador a una DMZ dejando una conexión *desde la DMZ hacia* el historiador de la zona de control recrea una ruta que rodea el servidor de salto. Es exactamente el tipo de arista de conveniencia contra el que advertía el §5.3; el EX021 lo corrige. D3 tiene dos rutas, ambas a través de un único punto de estrangulamiento (el intermediario), y cada una cruza varias barreras fuertes. Por motivos de seguridad, D3 es claramente la mejor.

Por motivos de operabilidad, el único punto de estrangulamiento de D3 es también su debilidad. Si el intermediario o su proveedor de identidad fallan durante una emergencia, no existe ninguna ruta remota; por tanto, el diseño necesita una ruta de acceso de emergencia probada, que es a su vez una arista nueva que hay que modelar y proteger. La barrera del interruptor de llave solo es real si los procedimientos operativos mantienen los interruptores en RUN y si una visita al emplazamiento es aceptable para los cambios de programa. Una recomendación completa añadiría estos elementos al coste y al grafo.

### 5.7 Elegir y registrar

Reúna la evidencia con los métodos del capítulo 1: una tabla de escenarios para cada diseño (incidentes evitados, costes operativos de un acceso más lento, escenarios de caída del intermediario) y la comprobación distributiva del capítulo 4 (¿hace un diseño más difícil dar soporte a los emplazamientos remotos?). Después, redacte un **registro de decisión de arquitectura (ADR)**: el contexto, la consecuencia que se aborda, las alternativas consideradas con sus grafos, la decisión, las consecuencias (incluidos los riesgos nuevos, como la dependencia del intermediario), el diseño del acceso de emergencia, la evidencia que mostrará que el diseño funciona (capítulo 6) y un desencadenante de revisión. Un ADR es un registro de decisión (§1.8) especializado en diseños; su valor está en que el próximo ingeniero que quiera añadir una arista cómoda pueda ver por qué no estaba ahí.

### 5.8 Errores comunes y límites

- Partir de un producto o de un eslogan en lugar de la consecuencia.
- Omitir las mitigaciones no digitales que acotan directamente la consecuencia.
- Dibujar el diseño previsto y pasar por alto las rutas añadidas después.
- Contar controles en lugar de examinar las barreras a lo largo de cada ruta.
- Celebrar un único punto de estrangulamiento sin diseñar para su fallo.
- Ignorar quién operará el diseño y cómo se gestionarán las excepciones.
- No redactar ningún registro de decisión, de modo que el siguiente cambio deshace el diseño sin que nadie lo note.

Los grafos solo son tan completos como el inventario que los sustenta, y las etiquetas de las barreras son juicios sobre su fuerza, no mediciones. Úselos para comparar diseños y exponer supuestos, y después pruebe el diseño elegido (capítulo 6).

### Ejercicios — capítulo 5

**EX021 — Corrija D2.** *Objetivo:* eliminar una ruta no prevista y volver a evaluar. *Entradas:* el Lab 5. *Restricciones:* cambie solo los enlaces del historiador en D2, de modo que los datos fluyan en un solo sentido desde el historiador de la zona de control hacia la copia de la DMZ, como en D3. *Pasos:* (1) edítelo y vuelva a ejecutarlo; (2) informe de las rutas y del conjunto mínimo de puntos de estrangulamiento de D2; (3) compare D2 corregida con D3 en dos frases. *Evidencia esperada:* edición, salida y comparación. *Rúbrica:* 3 = edición correcta, D2 tiene ahora cuatro rutas con el punto de estrangulamiento `jump`, la comparación señala los saltos de D2 que siguen dependiendo solo de contraseñas frente a la aprobación por sesión y la grabación de D3; 2 = números correctos, comparación pobre; 1 = no ejecutado; 0 = nada.

**EX022 — Una arista nueva.** *Objetivo:* evaluar una propuesta de conveniencia. *Entradas:* D3; Corvane propone un agente de monitorización en la nube en la estación de trabajo de ingeniería que mantiene una conexión saliente con la nube de Corvane «para diagnósticos». *Restricciones:* modélelo como una arista `internet → eng-ws` con la barrera "vendor cloud account". *Pasos:* (1) añada la arista y vuelva a ejecutarlo; (2) informe de las rutas y de los puntos de estrangulamiento; (3) proponga una alternativa que cubra la necesidad de diagnóstico. *Evidencia esperada:* salida y propuesta. *Rúbrica:* 3 = reconoce que el conjunto de puntos de estrangulamiento cambia porque ahora una ruta elude el intermediario, propone una alternativa (por ejemplo, diagnósticos exportados a través del historiador unidireccional, o el agente en un equipo de la DMZ), indica el riesgo residual; 2 = salida correcta, alternativa débil; 1 = acepta la arista porque, al ser solo saliente, sería segura; 0 = nada.

**EX023 — Diseño del acceso de emergencia.** *Objetivo:* diseñar para el fallo del punto de estrangulamiento. *Entradas:* D3. *Restricciones:* debe funcionar cuando el intermediario y el proveedor de identidad están caídos; no debe convertirse en una ruta habitual. *Pasos:* (1) diseñe la ruta de acceso de emergencia; (2) añádala al grafo; (3) especifique las alarmas, los registros y la frecuencia de las pruebas. *Evidencia esperada:* diseño y lista de rutas actualizada. *Rúbrica:* 3 = ruta física o con credenciales selladas, con alarmas y revisión tras cada uso, modelada como una arista con su barrera, probada según un calendario; 2 = sin pruebas; 1 = contraseña compartida permanente; 0 = nada.

**EX024 — Elija con evidencia.** *Objetivo:* combinar la seguridad y la operabilidad. *Entradas:* D1, D2 corregida y D3 con acceso de emergencia; costes anuales sintéticos de 20.000 £, 70.000 £ y 110.000 £; su juicio sobre las pérdidas de cada escenario con el formato del capítulo 1. *Restricciones:* al menos tres escenarios, incluida una caída del intermediario durante una emergencia. *Pasos:* (1) construya la tabla; (2) aplique el VE y el minimax del arrepentimiento; (3) indique el umbral que cambiaría su recomendación. *Evidencia esperada:* tabla y recomendación. *Rúbrica:* 3 = escenarios plausibles que incluyen los inconvenientes operativos de D3, ambas reglas aplicadas correctamente, umbral explícito; 2 = solo una regla; 1 = solo seguridad; 0 = nada.

**EX025 — Registro de decisión de arquitectura.** *Objetivo:* dejar constancia de la elección de diseño. *Entradas:* su recomendación del EX024. *Restricciones:* una página; todos los elementos del §5.7. *Pasos:* redacte el ADR. *Evidencia esperada:* ADR. *Rúbrica:* 3 = contexto que parte de la consecuencia, alternativas con evidencia de los grafos, riesgos nuevos y acceso de emergencia, evidencia de verificación y desencadenante de revisión; 2 = falta un elemento; 1 = descripción de un producto; 0 = nada.

### Síntesis del capítulo

Diseñe hacia atrás desde la consecuencia y ponga primero los límites no digitales. Use principios consolidados (mínimo privilegio, mediación completa, zonas y conductos, decisiones por sesión, técnicas de resiliencia) para generar alternativas que difieran en su naturaleza. Represente los diseños como grafos de rutas permitidas y compare las rutas, los puntos de estrangulamiento y las barreras, incluidas las aristas de conveniencia que acumulan los entornos reales. Evalúe cada diseño como un sistema operable y diseñe para el fallo de sus propios controles. Elija con los métodos de decisión de los capítulos anteriores y deje constancia de la elección en un ADR para que sobreviva a la próxima solicitud de cambio.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 12

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Infraestructura crítica y seguridad sectorial: evaluación controlada

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Planificar una evaluación controlada de un control de seguridad (una regla de detección, un diseño, un procedimiento de recuperación) que responda de forma segura a una pregunta formulada.
2. Informar de las tasas de detección y de éxito con intervalos, y calcular cuántos ensayos necesita una afirmación.
3. Medir la carga de falsas alarmas en las unidades que experimentan los operadores.
4. Evaluar simulacros y ejercicios con comparaciones pareadas y reconocer las amenazas a su validez.
5. Redactar reglas de enfrentamiento y condiciones de seguridad para las pruebas cerca de una planta en funcionamiento.

El capítulo 5 eligió diseños; el capítulo 2 calificó la evidencia de que los controles existen. Este capítulo pregunta si **funcionan**, en qué medida y con cuánta seguridad podemos afirmarlo, antes de que un incidente real responda por nosotros. El capítulo 11 amplía el método a la evaluación de un proyecto completo.

### 6.1 Por qué evaluar en condiciones controladas

Los controles de seguridad de los servicios esenciales rara vez se ven puestos a prueba por ataques reales, así que su eficacia suele darse por supuesta. La evaluación controlada crea la evidencia de forma deliberada: inyectar eventos conocidos y ver si se detectan; ejecutar una recuperación y cronometrarla; hacer un simulacro y observar si el personal puede operar en modo manual. La palabra *controlada* importa por partida doble. Científicamente, significa que el evaluador controla lo que se inyecta, de modo que las detecciones y los fallos pueden contarse frente a una verdad conocida. Operativamente, significa que la prueba está controlada para que no pueda dañar el proceso: las instalaciones de prueba, los simuladores, los gemelos digitales, los destinos de restauración aislados y los ejercicios de mesa soportan la mayor parte de la carga, y las pruebas en vivo solo se hacen con la autorización de operaciones y con condiciones de seguridad.

### 6.2 Detección: tasas, familias e intervalos

Una evaluación de la detección cuenta cuántos de los escenarios inyectados se detectaron. Una tasa única oculta dos cosas. La primera son las **familias**: una regla que detecta todas las escrituras directas desde la HMI pero solo la mitad de las manipulaciones de deriva lenta tiene un perfil de riesgo distinto del de otra que detecta el 85 % de todo. Informe por familia de técnicas; para la TO, las familias de MITRE ATT&CK for ICS son un buen vocabulario ([MITRE, ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)). La segunda es la **incertidumbre**: 17 detecciones en 20 ensayos son compatibles con una amplia gama de tasas reales. El intervalo de puntuación de Wilson ([Wilson, 1927](https://doi.org/10.1080/01621459.1927.10502953)) se comporta bien con muestras pequeñas y con tasas próximas a 0 o 1; úselo en lugar de la aproximación normal simple.

De ello se sigue una consecuencia práctica: **las afirmaciones necesitan tamaños de muestra**. Para afirmar «al menos un 90 % de detección» con un límite inferior de Wilson al 95 %, se necesitan decenas de ensayos con éxito, no unos pocos; cada fallo eleva aún más la cifra. Planifique el número de ensayos antes de probar e indique qué afirmación puede respaldar el número previsto.

La investigación sobre la evaluación de sistemas de detección aporta dos advertencias más. Los datos de prueba deben parecerse al entorno operativo (la tasa base de ataques reales, la variedad del comportamiento benigno), o los resultados no serán transferibles ([Sommer and Paxson, 2010](https://doi.org/10.1109/SP.2010.25); [Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)). Y, en la detección de anomalías en series temporales, algunas convenciones de puntuación populares inflan el rendimiento; la evaluación debe definirse con cuidado ([Kim et al., 2022](https://ojs.aaai.org/index.php/AAAI/article/view/20680)).

### 6.3 Carga de falsas alarmas

Una detección solo es útil si los operadores pueden actuar a partir de sus alertas. Mida las falsas alarmas reproduciendo tráfico benigno representativo durante un periodo suficientemente largo y contando las alertas; después, exprese la tasa **por turno o por operador** y con un intervalo; para recuentos de eventos raros es adecuado el intervalo exacto de Poisson. Combínela con la tasa base de eventos reales: cuando los ataques reales son raros, incluso una tasa baja de falsas alarmas significa que la mayoría de las alertas son falsas. Acuerde con operaciones una carga aceptable *antes* de la prueba (por ejemplo, «no más de una investigación por turno de noche»), para que el resultado pueda aprobar o suspender.

### 6.4 Simulacros y ejercicios

Los simulacros de operación manual, los ejercicios de recuperación y los ejercicios de mesa ponen a prueba a las personas y los procedimientos. Las recomendaciones del NIST sobre planificación de contingencias tratan las pruebas, la formación y los ejercicios como un ciclo con objetivos documentados y resultados posteriores a la acción ([NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)). Para evaluar si la formación mejoró el desempeño, compare a **las mismas personas** antes y después (un diseño pareado), informe de la mejora media con un intervalo y examine las diferencias individuales: una mejora media puede ocultar a un operador que no mejoró nada. Las amenazas a la validez son serias en los simulacros: los participantes aprenden el escenario (efecto de la práctica), saben que se les observa y suelen ser el personal más dispuesto. Varíe los escenarios, incluya turnos de noche y personal con menos experiencia, y no trate un buen simulacro como prueba de preparación.

### 6.5 Diseño seguro de las pruebas y reglas de enfrentamiento

Toda prueba cerca de una planta en funcionamiento necesita **reglas de enfrentamiento** escritas: el alcance (sistemas, horarios), los sistemas excluidos, las técnicas permitidas, las condiciones de parada (cualquier cambio inesperado del proceso, cualquier alarma que los operadores no puedan explicar), la autoridad designada para detenerla, las comunicaciones, la vuelta atrás y el tratamiento de la evidencia. El responsable de operaciones las firma. Las pruebas que inyectan órdenes deben usar instalaciones de prueba o simuladores siempre que sea posible; las pruebas en la planta en vivo deben ser de solo lectura o usar marcadores benignos acordados previamente. Se aplican los principios éticos del capítulo 4: la prueba no debe trasladar riesgo a los clientes sin protegerlos.

### 6.6 Ejemplo resuelto: una regla de detección nueva y un simulacro (sintético)

El proveedor de detección gestionada de Merrow Water propone una regla para detectar escrituras no autorizadas de puntos de consigna. El especialista diseña una evaluación en la instalación de prueba: 20 escenarios inyectados en tres familias, 336 horas de tráfico benigno de Hollin reproducido y un simulacro de dosificación manual con seis operadores antes y después de un nuevo módulo de formación. El responsable de operaciones acordó de antemano los criterios de aceptación: un límite inferior de detección de al menos 0,80 en conjunto, sin ninguna familia por debajo de 0,50 como estimación puntual; no más de una falsa alarma por turno de noche en promedio; y una mejora del tiempo de dosificación manual cuyo intervalo excluya el cero.

### 6.7 Actividad práctica: qué muestra la evaluación

```python
# Lab 6 - what a controlled evaluation can and cannot show (offline, standard library only)
# Synthetic: Merrow Water tests a new detection rule for unauthorised setpoint writes on a test rig,
# replays two weeks of benign plant traffic, and times a manual-operation drill before and after training.
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
def pois_cdf(k, mu): return sum(math.exp(-mu) * mu**i / math.factorial(i) for i in range(k + 1))
def pois_ci(k, a=0.05):  # exact (Garwood) interval by bisection
    def solve(f, lo, hi):
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid): lo = mid
            else: hi = mid
        return (lo + hi) / 2
    lower = 0.0 if k == 0 else solve(lambda m: 1 - pois_cdf(k - 1, m) < a/2, 0, 10*k + 10)
    upper = solve(lambda m: pois_cdf(k, m) > a/2, 0, 10*k + 10)
    return lower, upper
# 1. Detection on injected scenarios, split by technique family
RESULTS = {"direct HMI write": (9, 9), "engineering-workstation download": (6, 7), "slow drift via historian tag": (2, 4)}
k = sum(a for a, b in RESULTS.values()); n = sum(b for a, b in RESULTS.values())
lo, hi = wilson(k, n); print(f"overall detected {k}/{n} = {k/n:.2f}, 95% Wilson [{lo:.2f}, {hi:.2f}]")
for fam, (a, b) in RESULTS.items():
    lo, hi = wilson(a, b); print(f"  {fam:34s} {a}/{b}  [{lo:.2f}, {hi:.2f}]")
# 2. How many trials, all detected, before the lower bound clears 0.90?
n = 1
while wilson(n, n)[0] < 0.90: n += 1
print(f"perfect runs needed for Wilson lower bound >= 0.90: {n}")
# 3. False alarms in 336 hours of benign replay
fa, hours = 9, 336
lo, hi = pois_ci(fa); print(f"false alarms {fa} in {hours} h = {fa/hours*24:.2f}/day, 95% CI [{lo/hours*24:.2f}, {hi/hours*24:.2f}]/day")
# 4. Drill: minutes to stable manual dosing, same six operators before and after training (paired)
before = [34, 41, 29, 52, 38, 45]; after = [22, 30, 27, 31, 25, 44]
diffs = [b - a for b, a in zip(before, after)]
md = sum(diffs) / len(diffs); sd = math.sqrt(sum((d - md)**2 for d in diffs) / (len(diffs) - 1))
t = 2.571  # two-sided 95% t quantile, 5 degrees of freedom
print(f"paired improvement mean {md:.1f} min, 95% CI [{md - t*sd/math.sqrt(6):.1f}, {md + t*sd/math.sqrt(6):.1f}]; diffs {diffs}")
```

Salida esperada:

```text
overall detected 17/20 = 0.85, 95% Wilson [0.64, 0.95]
  direct HMI write                   9/9  [0.70, 1.00]
  engineering-workstation download   6/7  [0.49, 0.97]
  slow drift via historian tag       2/4  [0.15, 0.85]
perfect runs needed for Wilson lower bound >= 0.90: 35
false alarms 9 in 336 h = 0.64/day, 95% CI [0.29, 1.22]/day
paired improvement mean 10.0 min, 95% CI [2.1, 17.9]; diffs [12, 11, 2, 21, 13, 1]
```

**Interpretación.** La detección global es 17/20 = 0,85, pero el intervalo de Wilson al 95 % [0,64, 0,95] no supera el límite inferior de 0,80 acordado previamente. Por familias, se detectaron todas las escrituras directas desde la HMI, seis de siete descargas desde la estación de trabajo de ingeniería y solo dos de cuatro derivas lentas a través de una etiqueta del historiador: la estimación puntual cumple el mínimo de 0,50, pero su intervalo va de 0,15 a 0,85, así que la evaluación no puede decir si la deriva lenta se detecta de forma fiable en absoluto. Para afirmar un 90 % de detección con todos los ensayos con éxito harían falta 35 éxitos consecutivos. Las falsas alarmas se producen a razón de 0,64 al día (intervalo 0,29–1,22), unas 0,21 por turno de ocho horas, holgadamente dentro del criterio de carga. El simulacro muestra una mejora media de 10,0 minutos con un intervalo del 95 % de 2,1 a 17,9 minutos (el intervalo excluye el cero, así que se cumple el criterio), pero dos operadores mejoraron solo uno y dos minutos; merece la pena entender su experiencia antes del despliegue.

Por tanto, el resultado honesto es mixto: **adoptar la regla para las escrituras directas y las descargas, con monitorización de su rendimiento, no confiar en ella para la deriva lenta y diseñar más ensayos para esa familia**. Es una respuesta más útil que «un 85 % de detección».

### 6.8 Errores comunes y límites

- Informar de una única tasa de detección sin familias ni intervalos.
- Hacer demasiado pocos ensayos para respaldar la afirmación y, aun así, hacer la afirmación.
- Probar con escenarios diseñados por el autor de la regla, y solo con ellos.
- Medir las falsas alarmas con una reproducción corta o poco representativa.
- Expresar las falsas alarmas por día para toda una red en lugar de por turno o por operador.
- Tratar un simulacro con éxito como prueba de preparación.
- Probar en la planta en vivo sin reglas de enfrentamiento firmadas ni condiciones de parada.

El límite de la evaluación controlada es la transferencia: una instalación de prueba no es una planta y los escenarios inyectados no son adversarios. Use la evaluación para acotar las afirmaciones y encontrar debilidades, siga midiendo durante la operación y repítala cuando cambie el entorno.

### Ejercicios — capítulo 6

**EX026 — Intervalos y tamaño de muestra.** *Objetivo:* relacionar las afirmaciones con el número de ensayos. *Entradas:* las funciones del Lab 6. *Restricciones:* intervalos de Wilson al 95 %. *Pasos:* (1) calcule el intervalo para 19/20; (2) halle el número de éxitos consecutivos necesarios para un límite inferior de 0,80; (3) halle los ensayos necesarios para un límite inferior de 0,90 si se produce exactamente un fallo; (4) explique a un directivo por qué «lo probamos 20 veces» no basta para afirmar un 90 %. *Evidencia esperada:* cifras y un párrafo. *Rúbrica:* 3 = 19/20 → [0,76, 0,99], 16 éxitos, 53 ensayos con un fallo, explicación en lenguaje claro; 2 = una cifra errónea; 1 = aproximación normal usada sin comentarios; 0 = nada.

**EX027 — Plan de pruebas para la deriva lenta.** *Objetivo:* diseñar ensayos para la familia más débil. *Entradas:* el resultado de la deriva lenta. *Restricciones:* solo en la instalación de prueba; los escenarios deben variar la velocidad, la duración y la etiqueta objetivo; incluya escenarios no escritos por el autor de la regla. *Pasos:* (1) defina la afirmación que se va a probar; (2) elija el número de ensayos; (3) enumere las variaciones de los escenarios; (4) defina el criterio de aprobado o suspenso y qué hará si no se cumple. *Evidencia esperada:* plan. *Rúbrica:* 3 = afirmación explícita y número de ensayos justificado con un cálculo de intervalos, autoría independiente de los escenarios, variaciones realistas, decisión acordada previamente; 2 = número no justificado; 1 = reutiliza los cuatro escenarios; 0 = nada.

**EX028 — Carga de alarmas.** *Objetivo:* expresar las falsas alarmas en las unidades de los operadores y combinarlas con las tasas base. *Entradas:* 0,64 falsas alarmas al día; suponga que las escrituras no autorizadas reales ocurren aproximadamente una vez cada dos años; detección de 0,85. *Restricciones:* tres turnos de ocho horas al día. *Pasos:* (1) falsas alarmas por turno y por año; (2) alertas verdaderas esperadas por año; (3) proporción de alertas que son verdaderas; (4) qué significa esto para el procedimiento de respuesta. *Evidencia esperada:* cálculo y un párrafo. *Rúbrica:* 3 = unas 0,21 por turno y 234 al año, unas 0,43 alertas verdaderas al año, alrededor del 0,2 % de alertas verdaderas, un procedimiento que haga cada investigación rápida y barata; 2 = aritmética correcta, falta la implicación; 1 = confunde las tasas; 0 = nada.

**EX029 — Validez del simulacro.** *Objetivo:* criticar la evaluación de un simulacro. *Entradas:* el resultado pareado de los seis operadores. *Restricciones:* nombre al menos cuatro amenazas a la validez. *Pasos:* enumere las amenazas, el sentido en que cada una sesgaría el resultado y un cambio de diseño para cada una. *Evidencia esperada:* tabla. *Rúbrica:* 3 = efecto de la práctica, efecto de la observación, selección del personal dispuesto, mismo escenario, muestra pequeña, día frente a noche; sentidos indicados; cambios concretos; 2 = amenazas sin sentidos; 1 = genérico; 0 = nada.

**EX030 — Reglas de enfrentamiento.** *Objetivo:* redactar condiciones de prueba seguras. *Entradas:* una propuesta de verificar en la planta en vivo de Fenley que la nueva regla alerta ante una escritura de punto de consigna inocua y acordada previamente (de 1,80 a 1,81 mg/L). *Restricciones:* operaciones tiene la autoridad; los clientes no deben verse afectados. *Pasos:* redacte el alcance, el momento, los roles, las condiciones de parada, las comunicaciones, la vuelta atrás y el tratamiento de la evidencia. *Evidencia esperada:* reglas de enfrentamiento de una página. *Rúbrica:* 3 = aprobación de operaciones, momento de baja demanda, condiciones de parada y autoridad explícitas, verificación independiente de la dosis, vuelta atrás, equipo de gestión de alertas avisado sin informar a los analistas de detección si la detección a ciegas forma parte de la prueba, evidencia registrada; 2 = falta un elemento; 1 = sin condiciones de parada; 0 = nada.

### Síntesis del capítulo

La evaluación controlada convierte los controles supuestos en controles medidos. Inyecte eventos conocidos en instalaciones de prueba y simuladores, informe de la detección por familia con intervalos de Wilson y planifique el número de ensayos según las afirmaciones que quiera hacer. Mida las falsas alarmas durante periodos representativos y expréselas en las unidades de los operadores junto a las tasas base. Evalúe los simulacros con comparaciones pareadas, examine a las personas individualmente y diseñe contra los efectos de la práctica y de la selección. Pruebe cerca de la planta en vivo solo con reglas de enfrentamiento escritas y firmadas. El resultado honesto de una evaluación suele ser mixto; indique exactamente para qué usos es adecuado un control.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 12

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Infraestructura crítica y seguridad sectorial: integración organizativa

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Comparar modelos operativos para la seguridad de la TO y de la TI en una organización de servicios esenciales y elegir uno de forma razonada.
2. Asignar la titularidad de modo que cada actividad de seguridad crítica tenga exactamente un rol que rinda cuentas y que los conflictos de funciones sean visibles.
3. Medir la concentración de proveedores dentro de una organización y en una región, y planificar para un fallo de modo común de un proveedor.
4. Integrar la respuesta a ciberincidentes con la gestión de emergencias, la continuidad del negocio y los mecanismos regionales de resiliencia.
5. Diseñar un intercambio de información entre operadores que sea útil, lícito y de confianza.

Los capítulos 1 a 6 dotaron al especialista de herramientas para decidir, aportar evidencia y evaluar. Este capítulo sitúa ese trabajo dentro de una organización y de una región, porque la mayoría de los fallos en los servicios esenciales son fallos de integración: entre la TI y las operaciones, entre un operador y sus proveedores, entre un equipo de ciberincidentes y las personas que dirigen la respuesta a emergencias. El capítulo 8 pone a prueba la integración en los casos más difíciles; el capítulo 9 la dirige y la asegura.

### 7.1 Modelos operativos

Tres modelos habituales para la seguridad en una organización que gestiona tanto TI como TO:

| Modelo | Descripción | Fortalezas | Debilidades |
|---|---|---|---|
| Central | El equipo del CISO es titular de la seguridad de la TI y de la TO | Un solo estándar, una sola visión del riesgo, herramientas eficientes | Distancia respecto de la planta; controles diseñados para la TI; las operaciones pueden sortearlos |
| Federado | Operaciones es titular de la seguridad de la TO con sus propios especialistas; el CISO fija la política y la asegura | Cerca del proceso; cultura de seguridad funcional; creíble para los operadores | Estándares incoherentes; herramientas duplicadas; lagunas en la frontera entre TI y TO |
| Integrado | Una función conjunta de seguridad de la TO que depende de operaciones con una línea formal hacia el CISO, estándares compartidos y un proceso de incidentes compartido | Combina el conocimiento del proceso con la profundidad en seguridad | Necesita una titularidad explícita y una resolución de conflictos; depende de las personas |

No existe un modelo correcto universal. La NIST SP 800-82 recomienda formar un equipo multifuncional que incluya a ingenieros de control, operadores, personal de seguridad de la TI y de seguridad funcional ([NIST, 2023](https://doi.org/10.6028/NIST.SP.800-82r3)); el NIST CSF 2.0 sitúa los roles, las responsabilidades y las autoridades dentro de la gobernanza ([NIST, 2024](https://doi.org/10.6028/NIST.CSWP.29)). La elección del modelo integrado por parte de Merrow Water (un especialista principal de seguridad que depende del director de operaciones con una línea de puntos hacia el CISO) se deriva de su tamaño y del peso que da a la confianza de los operadores. Después, el modelo debe hacerse realidad mediante la titularidad, el presupuesto y el proceso de incidentes; un organigrama por sí solo no integra nada.

### 7.2 Titularidad: RACI y segregación de funciones

Para cada actividad crítica, un rol **rinde cuentas** (*Accountable*: es titular del resultado y lo aprueba), uno o más son **responsables** (*Responsible*: hacen el trabajo) y otros son **consultados** (*Consulted*) o **informados** (*Informed*). Dos reglas detectan la mayoría de los fallos de titularidad: cada actividad crítica tiene **exactamente un** rol que rinde cuentas; y, cuando un mismo rol ejecuta y aprueba una actividad con consecuencias de seguridad (un cambio de emergencia en un cortafuegos, un pago, la concesión de un acceso a un proveedor), el conflicto se elimina o se cubre con un control compensatorio, como una revisión a posteriori de cada caso. La segregación de funciones es un principio de control de larga tradición en el catálogo del NIST ([NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)). Dos roles que rinden cuentas de «declarar un ciberincidente» suena a seguridad adicional; en la práctica, crea una laguna a las 3 de la madrugada, cuando cada uno supone que el otro ya ha decidido.

### 7.3 Proveedores y concentración

Los servicios esenciales dependen de proveedores para el soporte de los sistemas de control, la detección gestionada, las telecomunicaciones y el alojamiento en la nube. La concentración tiene dos niveles:

- **Dentro de un operador.** Si un proveedor presta toda una función crítica, su fallo (técnico, comercial o por compromiso) es el fallo del operador. Una medida estándar de la concentración es el índice de Herfindahl-Hirschman (HHI): la suma de los cuadrados de las cuotas porcentuales, desde casi 0 (muchos proveedores pequeños) hasta 10.000 (un solo proveedor) ([U.S. Department of Justice, HHI](https://www.justice.gov/atr/herfindahl-hirschman-index)). Es una señal tosca pero útil.
- **En una región.** Si un proveedor es una dependencia mayoritaria de varios operadores, un único evento se convierte en un evento regional. La caída mundial de julio de 2024 causada por una actualización defectuosa de un software de seguridad, que afectó a unos 8,5 millones de dispositivos Windows según Microsoft ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)), mostró cómo un proveedor de confianza puede convertirse en un fallo de modo común entre sectores. La regulación financiera es la que más ha avanzado en esto: DORA exige registros de los acuerdos con terceros proveedores de TIC y establece la supervisión de los terceros proveedores críticos de servicios TIC ([Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)).

La concentración no es automáticamente mala: un proveedor bien gestionado puede ser más seguro que tres mal gestionados. La tarea del especialista es hacerla visible, decidir qué concentraciones son aceptables y preparar **planes de salida y de continuidad**: ¿qué haríamos si este proveedor no estuviera disponible durante una semana, o estuviera comprometido? Los contratos deben otorgar derechos de acceso a los registros, la notificación de incidentes, requisitos de seguridad y soporte durante los incidentes del propio proveedor. Las prácticas de la cadena de suministro de software (listas de materiales de software, SBOM ([CISA, SBOM](https://www.cisa.gov/sbom)); desarrollo seguro ([NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)); y compromisos de seguridad desde el diseño ([CISA, Secure by Design](https://www.cisa.gov/securebydesign))) ayudan en la vertiente del producto.

### 7.4 Integración con la gestión de emergencias

Un ciberincidente grave en un servicio esencial es también una emergencia: avisos de hervir el agua, desvíos hospitalarios, cierres portuarios. Por eso, el equipo de ciberincidentes debe encajar en el **mando de emergencias y de continuidad del negocio** de la organización en lugar de funcionar en paralelo. Puntos prácticos de integración:

- Una **clasificación de incidentes** compartida que relacione la gravedad cibernética con el impacto en el servicio, para que el responsable de guardia pueda escalar sin que haya un especialista en seguridad presente.
- Representación cibernética en la estructura de mando de emergencias y representación de la gestión de emergencias en los ciberejercicios.
- **Planes de operación manual y de continuidad** cuya titularidad sea de operaciones y que se prueben con escenarios de seguridad (capítulo 6).
- **Mecanismos regionales** acordados previamente: quién informa a los operadores vecinos, a los servicios de salud y a las autoridades locales; cómo funciona la ayuda mutua; cómo se coordinan los mensajes públicos. La Directiva CER de la UE enmarca la resiliencia de las entidades críticas como multirriesgo e intersectorial ([Directive (EU) 2022/2557](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)); de forma similar, la política estadounidense sobre seguridad y resiliencia de las infraestructuras críticas hace hincapié en la coordinación sectorial ([NSM-22 overview, CISA](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-security-memorandum-critical-infrastructure-security-and-resilience)).

### 7.5 Intercambio de información

Los operadores aprenden más rápido juntos, pero compartir conlleva riesgos jurídicos, comerciales y de seguridad. El intercambio útil es **específico** (indicadores, técnicas, versiones de productos afectadas, mitigaciones que funcionaron), **oportuno**, **protegido** (reglas de tratamiento acordadas, como las etiquetas del semáforo) y **recíproco**. Un acuerdo de intercambio para un foro regional debe cubrir: qué se comparte y en qué formato; las reglas de tratamiento y de difusión posterior; los datos personales (minimizarlos; comprobar la base jurídica, [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)); la cautela en materia de defensa de la competencia con la información comercialmente sensible; la responsabilidad; y cómo puede llegar la información compartida a los reguladores. *Nota para el lector hispanohablante:* en España, el RGPD se complementa con la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales; en América Latina rige la ley de cada país, por ejemplo la Ley 25.326 en Argentina o la Ley 1581 de 2012 en Colombia. La confianza se construye sobre todo con el comportamiento: compartir primero, proteger lo que comparten los demás y reconocer el mérito ajeno.

### 7.6 Ejemplo resuelto: las dependencias de Merrow Bay y un borrador de RACI (sintético)

El foro de resiliencia preguntó a cada operador qué proveedores prestan servicio a sus funciones esenciales y qué cuota aportan. Al mismo tiempo, el especialista de Merrow Water redactó un RACI para cinco actividades de seguridad críticas, que debía acordarse con operaciones y con el CISO. El Lab 7 analiza ambas cosas. Las preguntas eran deliberadamente sencillas: qué proveedor presta servicio a cada función esencial y, aproximadamente, con qué cuota. Los operadores respondieron a partir de los contratos y de los registros de activos, no de memoria, y el foro acordó de antemano que las respuestas solo se usarían para el análisis regional. El borrador de RACI cubre la aprobación y la ejecución de cambios de emergencia en los cortafuegos de la TO, la concesión de sesiones remotas a proveedores, la declaración de un ciberincidente y la restauración desde copias de seguridad fuera de línea, cada una elegida porque un error de titularidad en ella retrasaría la respuesta o debilitaría el control.

### 7.7 Actividad práctica: comprobaciones de concentración y de titularidad

```python
# Lab 7 - concentration and ownership checks for an integrated security function (offline, stdlib only)
# Synthetic: which suppliers Merrow Bay operators depend on for essential functions, and a draft RACI.
from collections import defaultdict
DEPENDS = [  # (operator, function, supplier, share of that operator's function served by the supplier)
    ("Merrow Water", "SCADA support", "Corvane Systems", 1.0),
    ("Merrow Water", "managed detection", "Lumen Watch", 1.0),
    ("Merrow Water", "telemetry links", "BayTel", 0.7), ("Merrow Water", "telemetry links", "radio (own)", 0.3),
    ("Merrow Health", "EPR hosting", "Halden Cloud", 1.0),
    ("Merrow Health", "managed detection", "Lumen Watch", 1.0),
    ("Merrow Health", "pathology LIMS", "Corvane Systems", 1.0),
    ("Merrow Energy", "SCADA support", "Corvane Systems", 0.6), ("Merrow Energy", "SCADA support", "in-house", 0.4),
    ("Merrow Energy", "telemetry links", "BayTel", 0.5), ("Merrow Energy", "telemetry links", "private fibre", 0.5),
    ("Port of Merrow", "terminal OS hosting", "Halden Cloud", 1.0),
    ("Port of Merrow", "managed detection", "Lumen Watch", 1.0),
]
by_op_fn = defaultdict(list)
for op, fn, sup, share in DEPENDS: by_op_fn[(op, fn)].append((sup, share))
print("Herfindahl-Hirschman index per operator function (10000 = single supplier):")
for (op, fn), lst in by_op_fn.items():
    hhi = sum((100 * s) ** 2 for _, s in lst)
    print(f"  {op:15s} {fn:20s} HHI {hhi:6.0f}")
reach = defaultdict(set)
for op, fn, sup, share in DEPENDS:
    if sup not in ("in-house", "radio (own)", "private fibre") and share >= 0.5: reach[sup].add(op)
print("Suppliers that are a majority dependency for 2+ operators (regional common mode):")
for sup, ops in sorted(reach.items(), key=lambda x: -len(x[1])):
    if len(ops) >= 2: print(f"  {sup:16s} {len(ops)} operators: {', '.join(sorted(ops))}")
RACI = {  # activity -> {role: letters}
    "approve OT firewall change":   {"OT engineer": "R", "OT manager": "A", "CISO": "C"},
    "emergency OT firewall change": {"OT engineer": "RA", "OT manager": "I"},
    "grant vendor remote session":  {"OT engineer": "R", "Service desk": "R"},
    "declare cyber incident":       {"CISO": "A", "Duty manager": "A", "OT manager": "C"},
    "restore from offline backup":  {"OT engineer": "R", "OT manager": "A", "IT ops": "R"},
}
print("RACI findings:")
for act, roles in RACI.items():
    a = [r for r, l in roles.items() if "A" in l]
    if len(a) != 1: print(f"  {act}: {len(a)} accountable roles {a}")
    for r, l in roles.items():
        if "R" in l and "A" in l: print(f"  {act}: {r} both does and approves (needs compensating control or record)")
```

Salida esperada:

```text
Herfindahl-Hirschman index per operator function (10000 = single supplier):
  Merrow Water    SCADA support        HHI  10000
  Merrow Water    managed detection    HHI  10000
  Merrow Water    telemetry links      HHI   5800
  Merrow Health   EPR hosting          HHI  10000
  Merrow Health   managed detection    HHI  10000
  Merrow Health   pathology LIMS       HHI  10000
  Merrow Energy   SCADA support        HHI   5200
  Merrow Energy   telemetry links      HHI   5000
  Port of Merrow  terminal OS hosting  HHI  10000
  Port of Merrow  managed detection    HHI  10000
Suppliers that are a majority dependency for 2+ operators (regional common mode):
  Corvane Systems  3 operators: Merrow Energy, Merrow Health, Merrow Water
  Lumen Watch      3 operators: Merrow Health, Merrow Water, Port of Merrow
  BayTel           2 operators: Merrow Energy, Merrow Water
  Halden Cloud     2 operators: Merrow Health, Port of Merrow
RACI findings:
  emergency OT firewall change: OT engineer both does and approves (needs compensating control or record)
  grant vendor remote session: 0 accountable roles []
  declare cyber incident: 2 accountable roles ['CISO', 'Duty manager']
```

**Interpretación.** Dentro de los operadores, siete de los diez pares función-operador tienen un HHI de 10.000 (un único proveedor), algo habitual y no alarmante en sí mismo. La visión regional es más importante: Corvane Systems es una dependencia mayoritaria de tres operadores (soporte del SCADA en el agua y la energía, sistemas de anatomía patológica en la salud), Lumen Watch presta detección gestionada a tres, y BayTel y Halden Cloud, a dos cada uno. Un compromiso de Lumen Watch dejaría ciega a la vez la detección de tres operadores; un compromiso del soporte remoto de Corvane podría alcanzar los sistemas operativos de tres sectores. Son riesgos del nivel del foro que no mostrará el registro de ningún operador aislado. La comprobación del RACI encuentra tres problemas: en el cambio de emergencia del cortafuegos, el ingeniero de TO ejecuta y aprueba a la vez, lo que puede ser aceptable de noche si cada caso se revisa el siguiente día laborable; la concesión de sesiones remotas a proveedores **no** tiene ningún rol que rinda cuentas, el hallazgo más peligroso dado el suceso de Hollin del capítulo 3; y la declaración de un ciberincidente tiene dos roles que rinden cuentas, que deberían quedar en uno (el responsable de guardia, que siempre está disponible), con el CISO como consultado.

### 7.8 Errores comunes y límites

- Elegir un modelo operativo copiando a otra organización en lugar de atender al tamaño, el riesgo y la cultura.
- Dibujar un organigrama y llamarlo integración.
- Dejar actividades críticas sin ningún titular que rinda cuentas, o con dos.
- Evaluar el riesgo de los proveedores contrato a contrato y pasar por alto la concentración regional.
- Tratar la certificación de un proveedor como evidencia de resiliencia durante el propio incidente del proveedor.
- Llevar la respuesta a ciberincidentes en paralelo al mando de emergencias.
- Compartir información sin reglas de tratamiento, o no compartirla nunca porque las reglas no están claras.

El límite del análisis estructural es que la integración depende, en última instancia, de las relaciones y de la práctica. Las tablas RACI y los valores del HHI indican dónde mirar; los ejercicios y los incidentes reales muestran si la integración funciona.

### Ejercicios — capítulo 7

**EX031 — Repare el RACI.** *Objetivo:* corregir los defectos de titularidad y verificarlo. *Entradas:* el Lab 7. *Restricciones:* cada actividad, exactamente una A; cualquier conflicto R+A se elimina o se documenta con un control compensatorio. *Pasos:* (1) edite el RACI; (2) vuelva a ejecutarlo y muestre que no quedan hallazgos sin tratar; (3) redacte el control compensatorio de cualquier conflicto que mantenga. *Evidencia esperada:* tabla editada, salida, texto del control. *Rúbrica:* 3 = la concesión de sesiones a proveedores tiene un rol que rinde cuentas (el responsable de TO) con el centro de servicios y el ingeniero de TO como responsables, la declaración de incidentes tiene un único rol que rinde cuentas, el conflicto del cambio de emergencia se elimina o se mantiene con una revisión al día siguiente de cada caso; 2 = salida limpia pero falta el control; 1 = no se vuelve a ejecutar; 0 = nada.

**EX032 — Modo común regional.** *Objetivo:* planificar para un proveedor concentrado. *Entradas:* Lumen Watch presta servicio a tres operadores. *Restricciones:* el foro no tiene autoridad sobre los contratos; los operadores mantienen sus propias elecciones. *Pasos:* (1) describa dos escenarios de fallo (caída; compromiso del proveedor); (2) proponga acciones para cada operador y para el foro; (3) defina las cláusulas contractuales que se pedirán en la renovación. *Evidencia esperada:* plan. *Rúbrica:* 3 = escenarios distintos (ceguera frente al proveedor como vía de ataque), las acciones incluyen una detección o un registro mínimos locales conservados por cada operador, un ejercicio conjunto, cláusulas de notificación, acceso a los registros y un plan de salida; 2 = un escenario; 1 = «cambiar de proveedor»; 0 = nada.

**EX033 — Elija un modelo operativo.** *Objetivo:* justificar un modelo para otra organización. *Entradas:* Port of Merrow: 600 empleados, un equipo de seguridad de la TI de dos personas, la TO de la terminal gestionada por un contratista y un centro de operaciones del capitán de puerto. *Restricciones:* use el §7.1. *Pasos:* compare los modelos; elija uno; indique las tres condiciones que harían fracasar su elección. *Evidencia esperada:* recomendación de una página. *Rúbrica:* 3 = elección argumentada a partir del tamaño, la dependencia del contratista y la cultura de operaciones, condiciones de fracaso concretas; 2 = ventajas e inconvenientes genéricos; 1 = sin elección; 0 = nada.

**EX034 — Lo cibernético dentro del mando de emergencias.** *Objetivo:* integrar las estructuras de respuesta. *Entradas:* el plan de emergencias vigente de Merrow Water (hervir el agua, pérdida de suministro) y su procedimiento de ciberincidentes, que actualmente no se mencionan entre sí. *Restricciones:* una sola clasificación compartida; ningún mando duplicado. *Pasos:* (1) redacte una tabla de clasificación combinada a partir del impacto en el servicio; (2) defina el lugar del responsable cibernético en el mando de emergencias; (3) enumere las notificaciones regionales y quién las hace. *Evidencia esperada:* tabla y descripción de un diagrama. *Rúbrica:* 3 = clasificación por impacto en el servicio utilizable por un responsable de guardia, el responsable cibernético asesora al director del incidente en lugar de dirigir una estructura paralela, notificaciones regionales asignadas; 2 = se mantienen estructuras paralelas; 1 = gravedad solo cibernética; 0 = nada.

**EX035 — Aritmética y juicio sobre la concentración.** *Objetivo:* calcular e interpretar el HHI. *Entradas:* los servicios de telemetría y de red de Merrow Health se reparten un 40 % / 40 % / 20 % entre tres operadores de telecomunicaciones, dos de los cuales comparten la misma canalización a lo largo de la carretera del puerto. *Restricciones:* muestre el cálculo. *Pasos:* (1) calcule el HHI; (2) explique por qué la cifra subestima la concentración real; (3) proponga cómo representar las rutas físicas compartidas. *Evidencia esperada:* cálculo y un párrafo. *Rúbrica:* 3 = HHI de 3.600, se reconoce que el 80 % del servicio comparte una ruta física, de modo que la concentración efectiva es muy superior, se propone calcular la concentración por rutas físicas o dominios de fallo; 2 = solo la cifra; 1 = aritmética errónea; 0 = nada.

### Síntesis del capítulo

La integración es donde suele fallar la seguridad de los servicios esenciales. Elija un modelo operativo adecuado a su tamaño, su riesgo y su cultura, y hágalo realidad con la titularidad: exactamente un rol que rinda cuentas por cada actividad crítica y un tratamiento visible de los conflictos de funciones. Mida la concentración de proveedores dentro de la organización y en la región, y prepare planes de salida y de continuidad para un fallo de modo común de un proveedor. Sitúe la respuesta cibernética dentro del mando de emergencias y de continuidad, con una clasificación compartida basada en el servicio. Comparta información de forma específica, con reglas de tratamiento acordadas, y construya la confianza con el comportamiento.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 12

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Infraestructura crítica y seguridad sectorial: casos difíciles

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Reconocer los rasgos que hacen difícil un caso: la interdependencia, la presión del tiempo, los deberes en conflicto, la evidencia incompleta y el daño en todas las opciones.
2. Analizar los fallos en cascada entre sectores y fijar prioridades de restablecimiento con pesos explícitos.
3. Estructurar las decisiones sobre fallos de proveedores de confianza, extorsiones y sucesos internos ambiguos.
4. Gestionar obligaciones en conflicto con reguladores, clientes, socios y fuerzas del orden sin engañar a ninguno de ellos.
5. Comunicar en condiciones de incertidumbre de forma que la evidencia posterior no lo desacredite.

Este capítulo reúne las reglas de decisión del capítulo 1, la disciplina probatoria del capítulo 3, la ética del capítulo 4 y la integración del capítulo 7, y las aplica allí donde se tensan. Después, el capítulo 9 pregunta cómo prepara un líder a una organización para estos casos.

### 8.1 Qué hace difícil un caso

Los casos fáciles tienen una respuesta correcta que es difícil de ejecutar. Los casos difíciles **no tienen ninguna opción sin daño**, y el especialista debe ayudar a elegir qué daño, con rapidez, con evidencia incompleta y bajo escrutinio. Se repiten cinco rasgos: la **interdependencia**, de modo que una decisión sobre un servicio cambia los resultados en otros; la **presión del tiempo**, porque los suministros de respaldo, el almacenamiento y la paciencia se agotan; los **deberes en conflicto** con distintas partes interesadas; la **evidencia ambigua**, sobre todo en cuanto a la causa y la intención; y la **irreversibilidad**, porque algunas acciones (pagar, desconectar, anunciar) no pueden deshacerse. Las disciplinas de los capítulos anteriores siguen siendo válidas; lo que cambia es que deben prepararse de antemano, porque no habrá tiempo para inventarlas.

### 8.2 Cascadas y relojes de respaldo

Las infraestructuras dependen unas de otras de forma física (electricidad para las bombas), digital (telemetría a través de las telecomunicaciones), geográfica (canalizaciones y emplazamientos compartidos) y lógica (mercados, dotación de personal) ([Rinaldi, Peerenboom and Kelly, 2001](https://doi.org/10.1109/37.969131)). Los estudios de redes muestran que los sistemas interdependientes pueden fallar de forma más abrupta que cualquiera de ellos por separado ([Buldyrev et al., 2010](https://doi.org/10.1038/nature08932)). Para un especialista, la herramienta práctica es el **reloj de respaldo**: para cada emplazamiento esencial, cuánto dura su propio respaldo (combustible del generador, almacenamiento, batería, solución manual) tras el fallo de una dependencia. El daño empieza cuando un reloj se agota. Las decisiones de restablecimiento (qué alimentador volver a energizar, qué emplazamiento visitar primero) son elecciones sobre qué relojes detener.

Las intrusiones de diciembre de 2015 en tres empresas ucranianas de distribución eléctrica, descritas en una alerta sobre sistemas de control industrial, causaron cortes que afectaron a unos 225.000 clientes; después de restablecerse el suministro, las empresas siguieron funcionando con operaciones restringidas ([CISA, IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01)). El caso recuerda que el final de un corte no es el final de un incidente inducido por un ciberataque: puede que durante un tiempo no se pueda confiar en los sistemas de control, y el restablecimiento y la operación continuada pueden depender del trabajo manual.

### 8.3 Las prioridades de restablecimiento necesitan pesos explícitos

El orden de restablecimiento suele fijarse por costumbre: primero la carga mayor, o primero el trabajo más rápido. Ninguna de las dos reglas está diseñada para minimizar el daño. Ordenar los trabajos para minimizar el tiempo total ponderado de finalización es un resultado clásico de la teoría de la planificación ([Smith, 1956](https://doi.org/10.1002/nav.3800030106)); en cuanto los relojes de respaldo actúan como fechas límite, el problema pasa a ser de retraso ponderado, mucho más difícil en general, pero con un puñado de alimentadores pueden enumerarse simplemente todos los órdenes. La parte más difícil son los **pesos**. ¿Vale lo mismo una hora sin electricidad en un hospital que una hora sin electricidad en una vivienda? Tratar todas las horas-persona por igual es en sí un juicio de valor, y normalmente uno malo cuando algunos emplazamientos albergan funciones vitales. Los pesos deben acordarse de antemano con la gestión de emergencias y registrarse; el análisis muestra entonces el orden que implican esos pesos y lo sensible que es al fallo de un respaldo.

### 8.4 Cuando la causa es un proveedor de confianza

Los fallos de los proveedores son difíciles porque los propios procesos de la organización confían en el proveedor. La caída de julio de 2024 causada por una actualización defectuosa obligó a las organizaciones afectadas a recuperar a mano muchos equipos finales ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)). Las decisiones en un caso así incluyen: si desconectar el canal del proveedor antes de saber si la causa es un error o un compromiso; qué sistemas recuperar primero (la lógica de restablecimiento del §8.3 se aplica tanto a los equipos finales como a los alimentadores); si retrasar las actualizaciones en el futuro y aceptar el coste de seguridad de una protección más lenta; y cómo mantener la detección cuando el problema es la propia herramienta de detección. Prepararse para este caso significa anillos de actualización escalonados para los sistemas críticos, soportes de recuperación independientes y una capacidad mínima que no dependa del proveedor.

### 8.5 Extorsión

Los casos de *ransomware* y de extorsión con datos obligan a decidir sobre el pago mientras los servicios están degradados. Un especialista no decide si se paga (eso corresponde a la dirección, asesorada por los abogados), pero estructura la decisión: el tiempo de recuperación realista con y sin descifrado (los descifradores suelen ser lentos e imperfectos); las consecuencias para el servicio y la seguridad de cada calendario; la posición jurídica, incluidos los riesgos de sanciones, que debe comprobarse con los abogados; las condiciones de la aseguradora; las consecuencias éticas y estratégicas de financiar actividades delictivas; y la evidencia que cambiaría la evaluación. En mayo de 2021, Colonial Pipeline Company detuvo de forma proactiva su sistema de oleoductos en respuesta a un ataque de *ransomware* y lo reinició seis días después ([U.S. Department of Energy](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident); véase también [CISA, 2023](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years)), lo que ilustra que la decisión de detener un servicio esencial puede ser en sí misma una precaución tomada en condiciones de incertidumbre, con grandes consecuencias para otros. La preparación para la recuperación (copias de seguridad probadas, operación manual, capacidad de reconstrucción limpia) es lo que da a una organización libertad en esta decisión; debe existir antes de que surja el caso.

### 8.6 Sucesos internos ambiguos

El suceso de Hollin (capítulo 3) podría ser un uso indebido de una cuenta compartida de un proveedor, un cambio legítimo no registrado de un ingeniero del proveedor u otra cosa. Los casos internos son difíciles porque las personas implicadas son compañeros o socios, la evidencia es ambigua y una acusación prematura es dañina y a veces ilícita. El caso del sector del agua tratado en los capítulos 2 y 3, cuyo primer relato se discutió después ([WUSF, 2023](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021)), muestra cómo los relatos públicos pueden adelantarse a la evidencia. En la práctica: **actúe sobre el acceso, no sobre la persona** (suspenda la cuenta compartida, exija cuentas nominativas), preserve la evidencia, implique pronto a recursos humanos y a los servicios jurídicos, mantenga las acusaciones fuera de las comunicaciones y recuerde que el error humano suele ser un síntoma del diseño del sistema ([Reason, 2000](https://doi.org/10.1136/bmj.320.7237.768)).

### 8.7 Obligaciones en conflicto

En un incidente significativo, un especialista puede enfrentarse a la vez a: el plazo de notificación de un regulador; las fuerzas del orden, que piden que algunos detalles sigan siendo confidenciales; un operador socio que pregunta si está expuesto; clientes que necesitan información de seguridad; un proveedor que pide un aplazamiento antes de que se diga nada sobre su producto; y las condiciones de las aseguradoras. Los principios para resolverlo son: **no engañar nunca** a nadie; **separar lo que se dice de lo que se omite**, y omitir solo con una razón defendible; dar **primero la información de seguridad**; cumplir los **deberes legales**, consultando a los abogados cuando los deberes entren en conflicto; y **registrar** cada decisión y su motivo. La divulgación coordinada de vulnerabilidades (capítulo 4) es una forma estructurada de gestionar el conflicto con el proveedor.

### 8.8 Ejemplo resuelto: restablecimiento tras un corte regional (sintético)

Un ciberincidente en el centro de control de Merrow Energy ha dejado sin tensión cuatro alimentadores. Los operadores pueden restablecer con seguridad un alimentador cada vez, de forma manual. Cada alimentador abastece a emplazamientos esenciales con relojes de respaldo: la planta de agua de Hollin tiene seis horas de almacenamiento; el bombeo de Fenley, cuatro horas; el hospital de Harbour, 48 horas de combustible para el generador; la terminal de contenedores, dos horas de batería; un depósito de combustible, ocho horas. Las viviendas no tienen respaldo. La célula de emergencias del foro regional debe recomendar un orden. El Lab 8 enumera todos los órdenes, primero ponderando por igual cada hora-persona.

### 8.9 Actividad práctica: orden de restablecimiento

```python
# Lab 8 - restoration order after a regional outage, with backup clocks running (offline, stdlib only)
# Synthetic: after a cyber-induced distribution outage, Merrow Energy can re-energize one feeder at a time.
# Each feeder carries essential sites whose backup lasts a fixed number of hours; after that, people lose service.
from itertools import permutations
FEEDERS = {  # feeder: (hours to restore safely, [(site, people served, backup hours)])
    "F1 Harbour":  (4, [("homes", 40000, 0), ("Harbour hospital", 3000, 48)]),
    "F2 Hollin":   (3, [("Hollin water works", 70000, 6)]),
    "F3 Fenley":   (2, [("homes", 18000, 0), ("Fenley pumping", 25000, 4)]),
    "F4 Port":     (5, [("container terminal", 2000, 2), ("fuel depot", 15000, 8)]),
}
def harm(order):
    t, total = 0, 0
    for f in order:
        t += FEEDERS[f][0]
        for site, people, backup in FEEDERS[f][1]:
            total += people * max(0, t - backup)
    return total
res = sorted((harm(o), o) for o in permutations(FEEDERS))
print("best five orders (person-hours without service):")
for h, o in res[:5]: print(f"  {h:9,d}  {' > '.join(o)}")
print(f"worst: {res[-1][0]:,d}  {' > '.join(res[-1][1])}")
largest = sorted(FEEDERS, key=lambda f: -sum(p for _, p, _ in FEEDERS[f][1]))
print(f"'largest load first' {' > '.join(largest)}: {harm(largest):,d}")
shortest = sorted(FEEDERS, key=lambda f: FEEDERS[f][0])
print(f"'quickest job first' {' > '.join(shortest)}: {harm(shortest):,d}")
# What if the hospital generator fails at hour 2 (backup 48 -> 2)? Re-solve.
FEEDERS["F1 Harbour"][1][1] = ("Harbour hospital", 3000, 2)
res2 = sorted((harm(o), o) for o in permutations(FEEDERS))
print(f"after hospital generator failure, best: {res2[0][0]:,d}  {' > '.join(res2[0][1])}")
```

Salida esperada:

```text
best five orders (person-hours without service):
    510,000  F3 Fenley > F2 Hollin > F1 Harbour > F4 Port
    589,000  F2 Hollin > F3 Fenley > F1 Harbour > F4 Port
    600,000  F3 Fenley > F1 Harbour > F2 Hollin > F4 Port
    631,000  F1 Harbour > F2 Hollin > F3 Fenley > F4 Port
    642,000  F1 Harbour > F3 Fenley > F2 Hollin > F4 Port
worst: 1,299,000  F4 Port > F1 Harbour > F3 Fenley > F2 Hollin
'largest load first' F2 Hollin > F1 Harbour > F3 Fenley > F4 Port: 681,000
'quickest job first' F3 Fenley > F2 Hollin > F1 Harbour > F4 Port: 510,000
after hospital generator failure, best: 531,000  F3 Fenley > F2 Hollin > F1 Harbour > F4 Port
```

**Interpretación.** Con pesos iguales, el mejor orden (Fenley, Hollin, Harbour, Port) pierde 510.000 horas-persona de servicio; el peor pierde 1.299.000. La costumbre de «primero la carga mayor» cuesta 681.000, un tercio más que el mejor; «primero el trabajo más rápido» coincide aquí con el mejor, pero solo porque los trabajos cortos coinciden con los relojes de respaldo cortos (el reloj del bombeo de Fenley es de cuatro horas). Llama la atención que, cuando falla el generador del hospital, el mejor orden con pesos iguales no cambia: 3.000 usuarios del hospital son pocos en comparación con 70.000 clientes del agua, así que los pesos iguales mantienen al hospital en tercer lugar. Ese resultado es el análisis diciéndole que sus pesos son erróneos para este propósito. El EX036 le pide ponderar más las horas-persona del hospital; con una ponderación plausible, el hospital pasa al primer lugar en cuanto falla su generador. La decisión corresponde a la célula de emergencias; la contribución del especialista es mostrar el orden que implica cada conjunto defendible de pesos y cómo lo cambia el fallo de un respaldo.

### 8.10 Errores comunes y límites

- Tratar un caso difícil como si tuviera una opción inocua y buscarla mientras se agotan los relojes.
- Restablecer por costumbre en lugar de con pesos explícitos acordados de antemano.
- Ponderar por igual todas las horas-persona y llamarlo neutral.
- Confiar en el canal del proveedor durante un incidente causado por el proveedor.
- Dejar que decida sobre el pago de una extorsión un especialista en lugar de la persona de la dirección que rinde cuentas.
- Acusar a personas antes de que la evidencia lo respalde.
- Hacer declaraciones a una parte interesada que contradicen las hechas a otra.

El límite del análisis en los casos difíciles es el tiempo. La enumeración del Lab 8 tarda milisegundos; acordar los pesos lleva semanas de planificación. Haga ese trabajo antes del suceso, ensáyelo y acepte que durante el suceso estará eligiendo entre opciones imperfectas con información incompleta.

### Ejercicios — capítulo 8

**EX036 — Los pesos cambian el orden.** *Objetivo:* ver cómo los pesos de valor determinan el restablecimiento. *Entradas:* el Lab 8. *Restricciones:* pondere cada hora-persona del hospital 20 veces más que una hora-persona de una vivienda; deje los demás en 1. *Pasos:* (1) modifique la función de daño; (2) informe del mejor orden con el generador de 48 horas y después de que el generador falle a las 2 horas; (3) explique el cambio y quién debería fijar el peso. *Evidencia esperada:* cambio en el código, salidas y un párrafo. *Rúbrica:* 3 = con el generador funcionando, el mejor orden no cambia (510.000); tras el fallo, Harbour pasa al primer lugar (mejor: 751.000 horas-persona ponderadas, Harbour > Hollin > Fenley > Port); la explicación identifica el peso como un juicio de la gestión de emergencias acordado de antemano; 2 = cifras correctas, explicación pobre; 1 = no ejecutado; 0 = nada.

**EX037 — Estructure una decisión de extorsión.** *Objetivo:* apoyar una decisión de la dirección sin tomarla. *Entradas:* el sistema de administración de pacientes de Merrow Health está cifrado; las copias de seguridad están intactas, pero una reconstrucción limpia se estima en 9 días; los atacantes afirman tener datos de pacientes y ofrecen un descifrador. *Restricciones:* ninguna conclusión jurídica; la seguridad de los pacientes, primero. *Pasos:* (1) enumere las opciones; (2) para cada una, el calendario de recuperación, las consecuencias para la seguridad y el servicio, las cuestiones jurídicas para los abogados, las consideraciones éticas y las incertidumbres; (3) indique qué evidencia cambiaría el análisis. *Evidencia esperada:* informe para la decisión. *Rúbrica:* 3 = las opciones incluyen la reconstrucción sin pago y medidas parciales, la fiabilidad del descifrador se trata como incierta, la extorsión con datos se separa de la recuperación, cuestiones de sanciones y de notificación para los abogados, medidas de seguridad independientes de la elección; 2 = falta una consideración; 1 = recomienda pagar o negarse como un hecho técnico; 0 = nada.

**EX038 — Caída causada por un proveedor.** *Objetivo:* decidir ante el fallo de un proveedor de confianza. *Entradas:* una actualización del proveedor de seguridad de equipos finales de Merrow Water bloquea durante la noche las HMI de cuatro plantas; el proveedor dice que es un defecto. *Restricciones:* las plantas deben seguir produciendo agua segura. *Pasos:* (1) acciones inmediatas; (2) orden de recuperación entre los emplazamientos; (3) si bloquear las actualizaciones siguientes y cómo; (4) cambios posteriores en la política de actualizaciones, con su coste de seguridad. *Evidencia esperada:* plan. *Rúbrica:* 3 = primero la operación manual, canal del proveedor en pausa hasta su verificación, recuperación ordenada por los relojes de respaldo, después anillos de actualización escalonados con una aceptación explícita de una protección más lenta; 2 = sin cambio de política; 1 = espera al proveedor; 0 = nada.

**EX039 — Comunicaciones sobre un suceso interno.** *Objetivo:* comunicar un caso interno ambiguo. *Entradas:* el suceso de Hollin con la cronología corregida. *Restricciones:* no se nombra a ninguna persona; se respetan los procesos laborales y contractuales. *Pasos:* redacte (1) un mensaje interno al personal; (2) un mensaje a Corvane; (3) una declaración para el foro de resiliencia. *Evidencia esperada:* tres textos breves. *Rúbrica:* 3 = factuales, sin acusaciones, se indican las acciones sobre el acceso (cuentas nominativas, cuenta compartida suspendida), se piden a Corvane los registros de sesiones conforme al contrato, el foro recibe información de protección útil; 2 = un texto exagera; 1 = acusatorio; 0 = nada.

**EX040 — Obligaciones en conflicto.** *Objetivo:* conciliar demandas sin engaño. *Entradas:* durante la investigación de Hollin, la policía pide a Merrow Water que no divulgue el detalle de la cuenta del proveedor; llega el plazo de notificación al regulador; Merrow Energy pregunta si debería suspender el acceso de Corvane; un periodista pregunta si el agua no era segura. *Restricciones:* siga los principios del §8.7; consulte a los abogados cuando sea necesario. *Pasos:* para cada parte, qué dice, qué omite y por qué, y quién lo aprueba. *Evidencia esperada:* tabla. *Rúbrica:* 3 = respuesta de seguridad dada con veracidad (la dosis volvió a la normalidad en menos de un minuto y se verificó), regulador informado por completo bajo confidencialidad, Merrow Energy recibe consejos de protección sin incumplir la petición de la policía (por ejemplo, el consejo de revisar todas las cuentas compartidas de proveedores), el periodista no es inducido a error, aprobaciones registradas; 2 = una parte mal gestionada; 1 = declaración engañosa; 0 = nada.

### Síntesis del capítulo

Los casos difíciles tienen daño en todas las opciones, con presión del tiempo, evidencia ambigua y deberes en conflicto. Prepárese para ellos: mapee las dependencias y los relojes de respaldo; acuerde de antemano con la gestión de emergencias los pesos del restablecimiento; planifique para los fallos causados por proveedores con anillos de actualización y una recuperación independiente; estructure las decisiones de extorsión para la persona de la dirección que rinde cuentas; actúe sobre el acceso y no sobre las personas en los casos internos; y resuelva las obligaciones en conflicto sin engañar nunca, poniendo la seguridad primero, omitiendo solo con razones defendibles y registrando cada decisión. El análisis es rápido; el acuerdo es lento: haga la parte lenta antes del suceso.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 12

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Infraestructura crítica y seguridad sectorial: liderazgo y aseguramiento

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Dirigir una función de seguridad en un servicio esencial: fijar la dirección, desarrollar la capacidad y conservar la confianza de operaciones y del consejo.
2. Informar al consejo en unidades de servicio con un pequeño conjunto de indicadores que sirvan para decidir.
3. Distinguir un cambio real del ruido en un indicador de seguridad mediante un gráfico de comportamiento del proceso (XmR).
4. Construir un caso de aseguramiento para una afirmación sobre resiliencia y mantener la vigencia de su evidencia.
5. Usar el modelo de las tres líneas y la revisión independiente sin convertir el aseguramiento en papeleo.

Los capítulos 7 y 8 integraron la seguridad en la organización y la pusieron a prueba en casos difíciles. Este capítulo trata de la persona responsable de ella a lo largo de los años: de qué informa, cómo sabe si las cosas mejoran y cómo demuestra a otros que las afirmaciones son ciertas. Después, el capítulo 10 se ocupa de la evidencia externa que un líder debe leer.

### 9.1 Dirigir una función especializada

Un líder de seguridad en un servicio esencial dirige a personas escasas, a menudo sobrecargadas, que trabajan entre culturas distintas: ingenieros de control, personal de TI, operadores, proveedores. Predominan cuatro responsabilidades. **Dirección:** un número reducido de prioridades vinculadas al servicio y a su consecuencia, revisadas cuando cambia la evidencia (los desencadenantes de revisión del capítulo 1). **Capacidad:** las competencias, las herramientas y el tiempo para hacer el trabajo, incluida la sucesión, para que el conocimiento de un sistema crítico no resida en una sola cabeza. **Confianza:** operaciones debe creer que seguridad entiende la planta y no la pondrá en peligro; el consejo debe creer que los informes son francos. **Rendición de cuentas:** una titularidad clara (capítulo 7) y un registro de las decisiones (capítulo 1). Los códigos profesionales exigen honestidad sobre los límites ([ACM Code of Ethics](https://www.acm.org/code-of-ethics)); para un líder, eso incluye decir al consejo lo que no se sabe.

Desarrollar la capacidad en seguridad de la TO es, en parte, una cuestión de mezclar trayectorias: ingenieros de control que aprenden seguridad y especialistas en seguridad que aprenden el proceso. Las rotaciones, los ejercicios conjuntos (capítulo 6) y las revisiones compartidas de incidentes (capítulo 3) aportan más que los cursos por sí solos.

### 9.2 Informes al consejo

Los consejos deben tomar decisiones sobre el apetito, la inversión y la rendición de cuentas. Un buen informe es breve y responde a cuatro preguntas: **¿Estamos dentro del apetito?** (los límites de cola y de distribución del capítulo 4, en unidades de servicio); **¿Qué ha cambiado?** (amenazas nuevas, incidentes, supuestos); **¿Funcionan nuestros controles?** (evidencia verificada, capítulo 2; rendimiento evaluado, capítulo 6); **¿Qué tienen que decidir ustedes?** Los indicadores deben ser pocos, estar definidos y estar vinculados a la consecuencia: la cobertura verificada de las prácticas de mayor peso; el tiempo de corrección de las vulnerabilidades explotadas conocidas en los sistemas expuestos, usando una lista de referencia como el catálogo de CISA ([CISA, KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)); el último simulacro de operación manual superado en cada emplazamiento principal; el tiempo de recuperación demostrado para los sistemas críticos; y las decisiones pendientes con sus responsables. Evite los recuentos que miden la actividad en lugar del resultado: número de alertas, formaciones impartidas, hallazgos cerrados.

### 9.3 ¿Señal o ruido?

Todo indicador varía de un mes a otro. Reaccionar a cada subida malgasta la atención; ignorar un cambio real malgasta el tiempo. Un **gráfico de comportamiento del proceso** (también llamado gráfico de valores individuales y rango móvil, o XmR) separa ambas cosas usando la propia historia del indicador. A partir de un periodo de referencia, calcule la media y la diferencia absoluta media entre valores consecutivos (el rango móvil medio); los límites naturales del proceso son la media más o menos 2,66 veces el rango móvil medio. Los puntos fuera de los límites, o las rachas largas a un lado de la media, señalan un cambio que merece investigarse; los puntos dentro son variación rutinaria ([NIST/SEMATECH e-Handbook, control charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm)). Dos reglas prácticas: elija la referencia de un periodo que se considere estable y **no incluya el periodo que está poniendo a prueba**; y trate una señal como un aviso para investigar, no como la prueba de una causa.

### 9.4 Casos de aseguramiento

Un **caso de aseguramiento** es un argumento estructurado de que una afirmación es cierta, respaldado por evidencia. Sigue la estructura general de la argumentación (afirmación, fundamentos, garantía, refutación) ([Toulmin, 2003](https://doi.org/10.1017/CBO9780511840005)) aplicada a los sistemas. Por ejemplo: *Afirmación:* «Hollin puede suministrar agua segura durante 72 horas sin su sistema de control». *Subafirmaciones:* la dosificación manual puede mantenerse con el personal de cualquier turno; las existencias de productos químicos duran 72 horas; los analizadores funcionan sin SCADA; el personal puede ser relevado. *Evidencia:* informes de simulacros con tiempos y participantes; registros de existencias; pruebas de los analizadores; cuadrante de turnos. *Refutaciones consideradas:* turno de noche con personal mínimo; pérdida de alimentación de los analizadores; incidente simultáneo en Fenley. Un caso de aseguramiento hace visible de qué evidencia depende cada afirmación, de modo que, cuando la evidencia envejece o falla, se sabe qué afirmaciones quedan afectadas.

### 9.5 Vigencia de la evidencia

La evidencia caduca. Una restauración probada hace dieciocho meses dice poco de las copias de seguridad de hoy; una revisión del cortafuegos anterior a un cambio de red dice poco después de él. Para cada afirmación de aseguramiento, fije una **antigüedad máxima de la evidencia** relacionada con la rapidez con que cambia el sistema subyacente, e informe de la evidencia caducada como una laguna, aunque no se sepa que algo esté mal. Un tipo de evidencia de grado bajo (una declaración) con una antigüedad permitida larga merece un escrutinio especial: puede estar «vigente» según la regla, pero es débil por naturaleza (los grados del capítulo 2).

### 9.6 Las tres líneas y la revisión independiente

El modelo de las tres líneas del Institute of Internal Auditors describe los roles de la dirección (primera línea: ser titular del riesgo y gestionarlo), de las funciones especializadas de riesgos y cumplimiento (segunda línea: conocimiento experto, apoyo y cuestionamiento) y de la auditoría interna (tercera línea: aseguramiento independiente), todos ellos responsables ante un órgano de gobierno ([IIA, 2020](https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/)). En la seguridad de los servicios esenciales, el valor del modelo es la claridad: operaciones es titular del riesgo de su planta; la función de seguridad fija estándares, cuestiona y ayuda; la auditoría interna o un revisor externo comprueba que el sistema funciona. El modelo falla cuando la segunda línea hace el trabajo de la primera (de modo que nadie en operaciones es titular del riesgo) o cuando la auditoría pone a prueba documentos en lugar de la realidad.

### 9.7 Ejemplo resuelto: el dosier del consejo de Merrow Water (sintético)

El consejo de Merrow Water recibe cada mes la mediana de días para corregir las vulnerabilidades explotadas conocidas en los sistemas expuestos a internet. Tras una lectura de 24 días en diciembre, una consejera no ejecutiva preguntó si las cosas iban a peor o si diciembre había sido un mal mes. En la misma reunión, el especialista presentó la evidencia en que se apoyan seis afirmaciones de aseguramiento. El Lab 9 examina ambas cosas. La pregunta de la consejera es la correcta, y no puede responderse comparando solo diciembre con noviembre. El especialista necesita una referencia de meses en los que no se sepa que ocurriera nada inusual, así que el gráfico usa los once primeros meses y deja fuera las lecturas posteriores. Las seis afirmaciones se eligieron porque cada una respalda la declaración del consejo de que Merrow Water puede recuperarse con seguridad de un ciberincidente; cada una tiene un tipo de evidencia designado, una fecha y una antigüedad máxima aceptable acordada con la auditoría interna.

### 9.8 Actividad práctica: gráfico XmR y vigencia de la evidencia

```python
# Lab 9 - is the assurance signal a change or noise? An XmR chart and evidence freshness (offline, stdlib only)
# Synthetic: Merrow Water's monthly median days to remediate known-exploited vulnerabilities on internet-facing
# systems, reported to the board, and the age of the evidence behind six assurance claims.
from datetime import date
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan2","Feb2","Mar2"]
DAYS =   [  12,   9,  14,  11,  13,  10,   12,  15,   11,   9,   13,   24,   21,    23,    25]
BASE = 11  # first 11 months form the baseline
x = DAYS[:BASE]; mean = sum(x) / BASE
mr = [abs(b - a) for a, b in zip(x, x[1:])]; mrbar = sum(mr) / len(mr)
ucl, lcl = mean + 2.66 * mrbar, max(0, mean - 2.66 * mrbar)
print(f"baseline mean {mean:.2f} days, mean moving range {mrbar:.2f}, limits [{lcl:.2f}, {ucl:.2f}]")
run = 0
for m, d in zip(MONTHS, DAYS):
    flag = []
    if d > ucl or d < lcl: flag.append("outside limits")
    run = run + 1 if d > mean else 0
    if run >= 4: flag.append(f"{run} in a row above mean")
    print(f"  {m:5s} {d:3d} {'; '.join(flag)}")
TODAY = date(2026, 10, 12)
CLAIMS = [  # (claim, evidence type, date of evidence, maximum acceptable age in days)
    ("offline backups restorable", "restore test record", date(2026, 3, 2), 180),
    ("vendor sessions all brokered", "broker log reconciliation", date(2026, 9, 20), 31),
    ("no default credentials on PLCs", "engineer attestation", date(2025, 11, 5), 365),
    ("manual dosing drill passed", "drill report", date(2026, 6, 18), 365),
    ("IT/OT firewall rules reviewed", "rule review sign-off", date(2026, 1, 9), 180),
    ("MFA on all remote access", "IdP configuration export", date(2026, 10, 1), 90),
]
print("evidence freshness:")
for c, ev, d, mx in CLAIMS:
    age = (TODAY - d).days
    print(f"  {'STALE' if age > mx else 'ok   '} {age:4d}d / {mx:3d}d  {c} ({ev})")
```

Salida esperada:

```text
baseline mean 11.73 days, mean moving range 3.10, limits [3.48, 19.97]
  Jan    12 
  Feb     9 
  Mar    14 
  Apr    11 
  May    13 
  Jun    10 
  Jul    12 
  Aug    15 
  Sep    11 
  Oct     9 
  Nov    13 
  Dec    24 outside limits
  Jan2   21 outside limits
  Feb2   23 outside limits; 4 in a row above mean
  Mar2   25 outside limits; 5 in a row above mean
evidence freshness:
  STALE  224d / 180d  offline backups restorable (restore test record)
  ok      22d /  31d  vendor sessions all brokered (broker log reconciliation)
  ok     341d / 365d  no default credentials on PLCs (engineer attestation)
  ok     116d / 365d  manual dosing drill passed (drill report)
  STALE  276d / 180d  IT/OT firewall rules reviewed (rule review sign-off)
  ok      11d /  90d  MFA on all remote access (IdP configuration export)
```

**Interpretación.** Durante los once meses de referencia, el indicador promedió 11,7 días con unos límites naturales de aproximadamente 3,5 a 20,0 días. Los 24 días de diciembre están fuera de los límites (una señal, no solo un mal mes), y los tres meses siguientes también, con una racha por encima de la media. Algo cambió en diciembre; entre las causas candidatas están la marcha de un miembro del personal, un cambio en el contenido del catálogo de vulnerabilidades, una nueva clase de sistemas expuestos a internet o un cambio en la forma de calcular el indicador. El gráfico dice al consejo *que* debe preguntar, no *cuál* es la respuesta correcta. En cuanto a la evidencia, dos de las seis afirmaciones están caducadas: la prueba de restauración de las copias de seguridad fuera de línea (224 días frente a un límite de 180) y la revisión del cortafuegos entre TI y TO (276 días frente a 180). La afirmación sobre las credenciales por defecto de los PLC está dentro de su límite de antigüedad, pero se apoya en la declaración de un ingeniero, el grado de evidencia más débil, y caduca en menos de un mes. El consejo debe oír tres cosas: un deterioro real del tiempo de corrección desde diciembre, con una investigación en curso; dos afirmaciones de aseguramiento caducadas, con fechas de renovación; y una afirmación que necesita evidencia más fuerte, no solo más reciente.

### 9.9 Errores comunes y límites

- Informar de recuentos de actividad en lugar de indicadores relacionados con la consecuencia.
- Reaccionar a cada subida mensual, o atribuir al ruido un cambio real.
- Incluir el periodo sospechoso en la referencia, lo que ensancha los límites y oculta la señal.
- Redactar afirmaciones de aseguramiento sin evidencia designada, o evidencia sin fecha.
- Tratar una evidencia reciente pero débil como fuerte.
- Dejar que la función de seguridad sea titular del riesgo operativo en nombre de operaciones.
- Presentar al consejo solo las buenas noticias.

El límite de los indicadores y los gráficos es que resumen. Indican a un líder dónde mirar; mirar (conversar con los operadores, visitar los emplazamientos, leer las revisiones de incidentes) sigue siendo trabajo del líder.

### Ejercicios — capítulo 9

**EX041 — Una referencia contaminada.** *Objetivo:* ver cómo afecta la elección de la referencia a las señales. *Entradas:* el Lab 9. *Restricciones:* cambie la referencia a los doce primeros meses (incluido diciembre). *Pasos:* (1) vuelva a ejecutarlo; (2) informe de la nueva media, del rango móvil y de los límites; (3) informe de qué meses posteriores quedan ahora fuera de los límites; (4) explique la lección. *Evidencia esperada:* salida y un párrafo. *Rúbrica:* 3 = media de 12,75, rango móvil medio de unos 3,82, límites de aproximadamente [2,6, 22,9]; diciembre sigue fuera, pero enero (21) queda ahora dentro; lección: incluir el periodo puesto a prueba ensancha los límites y puede ocultar un cambio; 2 = cifras correctas, falta la lección; 1 = no ejecutado; 0 = nada.

**EX042 — Informe al consejo de una página.** *Objetivo:* informar en unidades de servicio para decidir. *Entradas:* las salidas del Lab 9, la cobertura verificada de Merrow Water del capítulo 2 (39 %), la evaluación del capítulo 6 y los hallazgos del RACI del capítulo 7. *Restricciones:* una página; seis indicadores como máximo; termine con las decisiones solicitadas. *Pasos:* redacte el informe. *Evidencia esperada:* informe. *Rúbrica:* 3 = estado del apetito en unidades de servicio, señal comunicada con la incertidumbre sobre su causa, evidencia caducada y débil identificada, decisiones concretas con responsables; 2 = incluye métricas de actividad; 1 = tranquilización sin evidencia; 0 = nada.

**EX043 — Caso de aseguramiento.** *Objetivo:* construir un argumento estructurado. *Entradas:* la afirmación «Hollin puede suministrar agua segura durante 72 horas sin su sistema de control». *Restricciones:* al menos cuatro subafirmaciones, cada una con el tipo de evidencia, la antigüedad máxima y el estado actual; al menos tres refutaciones. *Pasos:* construya el caso como una tabla o un árbol. *Evidencia esperada:* caso de aseguramiento. *Rúbrica:* 3 = las subafirmaciones cubren las personas, los materiales, los instrumentos y la duración; evidencia de grado verificado cuando es posible, con su antigüedad; refutaciones realistas (turno de noche, alimentación de los analizadores, incidente concurrente) con respuestas; 2 = evidencia sin fecha; 1 = repite la afirmación; 0 = nada.

**EX044 — Las tres líneas en la práctica.** *Objetivo:* asignar los roles de aseguramiento. *Entradas:* las seis afirmaciones de aseguramiento del Lab 9. *Restricciones:* use el modelo de las tres líneas. *Pasos:* para cada afirmación, asigne el titular de la primera línea, la actividad de cuestionamiento de la segunda línea y el método de prueba de la tercera línea; identifique una afirmación en la que la segunda línea esté haciendo actualmente trabajo de la primera. *Evidencia esperada:* tabla y un párrafo. *Rúbrica:* 3 = los titulares son roles operativos, los métodos de cuestionamiento y de prueba son distintos, ejemplo creíble de confusión de roles (por ejemplo, el equipo de seguridad ejecutando pruebas de restauración que debería ejecutar operaciones); 2 = líneas confundidas en una fila; 1 = genérico; 0 = nada.

**EX045 — Capacidad y sucesión.** *Objetivo:* reducir la dependencia de una sola persona. *Entradas:* el único ingeniero de Merrow Water que entiende la lógica del controlador de dosificación de Hollin prevé jubilarse dentro de 18 meses. *Restricciones:* presupuesto para un puesto adicional; las operaciones no deben verse alteradas. *Pasos:* (1) identifique qué conocimiento está en riesgo y cómo capturarlo; (2) diseñe un plan de desarrollo para dos sucesores; (3) defina la evidencia de que la sucesión ha funcionado. *Evidencia esperada:* plan. *Rúbrica:* 3 = conocimiento capturado como artefactos verificados (lógica anotada, procedimientos de prueba, recorridos grabados), trabajo en pareja y cambios supervisados, evidencia como un cambio dirigido por un sucesor y un simulacro sin el ingeniero que se jubila; 2 = solo cursos de formación; 1 = solo documentación; 0 = nada.

### Síntesis del capítulo

Dirigir la seguridad de un servicio esencial significa fijar una dirección vinculada a la consecuencia, desarrollar una capacidad que sobreviva a las marchas y conservar la confianza de operaciones y del consejo. Informe al consejo en unidades de servicio con pocos indicadores y decisiones explícitas. Use gráficos de comportamiento del proceso para distinguir el cambio del ruido, con una referencia limpia. Construya casos de aseguramiento que vinculen cada afirmación con evidencia fechada de grado conocido, e informe de la evidencia caducada o débil como lagunas. Use las tres líneas para mantener la titularidad en operaciones, el cuestionamiento en los especialistas y las pruebas independientes en la auditoría.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Siga estudiando — capítulo 09 de 12

[← Capítulo 08](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Lectura y crítica de la investigación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Leer un estudio publicado, un aviso oficial y una afirmación de un proveedor por lo que cada uno puede aportar a una decisión práctica.
2. Identificar el diseño de un estudio y la afirmación más fuerte que ese diseño respalda.
3. Comprobar los denominadores, las comparaciones y las definiciones de los resultados, y detectar factores de confusión como la paradoja de Simpson.
4. Juzgar si un hallazgo es transferible a su organización y a su sector.
5. Redactar una ficha de evidencia breve que indique qué muestra una fuente, qué no muestra y qué hará usted con ella.

Un especialista no necesita producir investigación, pero sí debe usarla: para elegir controles, para fijar probabilidades (capítulos 1 y 4), para discutir con los proveedores y para informar a los consejos. Este capítulo enseña a leer para decidir. Después, el capítulo 11 aplica la misma mirada crítica a la evaluación de su propio proyecto.

### 10.1 Tres tipos de fuente

| Tipo de fuente | Fortaleza | Debilidad típica | Cómo usarla |
|---|---|---|---|
| Estudio revisado por pares | Método explícito, revisado, citable | Contexto estrecho; retraso; puede no medir lo que a usted le importa | Conocer tamaños del efecto y mecanismos; comprobar la transferencia |
| Aviso o informe oficial | Oportuno, detalle operativo, autoridad | Escrito para actuar, no para inferir; selección de casos | Conocer técnicas y mitigaciones; no inferir frecuencias |
| Informe de proveedor o encuesta | Muestras grandes, actual | Interés comercial; denominadores no definidos; selección de los encuestados | Usarlo para generar hipótesis; verificar antes de actuar |

Ninguno es automáticamente fiable ni carece de valor. Cada uno responde bien a algunas preguntas y mal a otras. Su trabajo es emparejar la fuente con la pregunta.

### 10.2 Leer un estudio: primero el diseño

Antes de leer los resultados, identifique el diseño, porque limita la afirmación. Una comparación antes y después en un solo emplazamiento puede mostrar que algo cambió, pero difícilmente por qué. Una comparación con un grupo de control no afectado, o una serie temporal interrumpida, respalda un lenguaje causal más fuerte. Una encuesta a víctimas no puede estimar con qué frecuencia se producen ataques en el conjunto de la población. Después compruebe: la **unidad** (hospital, paciente, día), el **resultado** y cómo se midió, la **comparación** (qué habría ocurrido en otro caso), la **ventana temporal** y el **contexto**.

Considere dos estudios reales del sector sanitario. Ghafur y sus colegas analizaron los datos nacionales de actividad hospitalaria en torno al ataque WannaCry de 2017 y no encontraron un cambio significativo en la actividad total del conjunto de los *trusts* ingleses, pero sí alrededor de un 6 % menos de ingresos al día en los hospitales infectados, una actividad perdida estimada en 5,9 millones de libras y ninguna diferencia detectada en la mortalidad, aunque señalaron que la mortalidad es una medida tosca del daño a los pacientes ([Ghafur et al., 2019](https://doi.org/10.1038/s41746-019-0161-6)). Dameff y sus colegas compararon los volúmenes de los servicios de urgencias de dos hospitales vecinos de un sistema sanitario sometido a un ataque de *ransomware* de un mes de duración en 2021, antes, durante y después del ataque, e informaron de aumentos significativos de la ocupación, las llegadas en ambulancia y otras medidas durante el ataque ([Dameff et al., 2023](https://doi.org/10.1001/jamanetworkopen.2023.12270)). Ambos son valiosos; ambos están acotados por su diseño. El primero usa datos nacionales con comparación entre *trusts*; el segundo es un estudio antes y después en una sola institución, por lo que no pueden excluirse por completo los cambios estacionales o locales. Ninguno dice a Merrow Health qué probabilidad hay de un ataque; ambos informan sobre lo graves y lo regionales que pueden ser las consecuencias.

Los conjuntos de datos de ámbito poblacional responden a preguntas distintas. Neprash y sus colegas usaron una base de datos de ataques de *ransomware* comunicados públicamente contra organizaciones prestadoras de atención sanitaria de EE. UU. y encontraron que los ataques anuales se habían más que duplicado entre 2016 y 2021 y que casi la mitad interrumpieron la prestación de la atención ([Neprash et al., 2022](https://doi.org/10.1001/jamahealthforum.2022.4873)). Como los datos son ataques *comunicados públicamente*, las tendencias combinan los cambios en los ataques con los cambios en la comunicación, una limitación que el diseño de los autores hace explícita y que el lector debe tener presente.

### 10.3 Leer un aviso

Los avisos como el aviso conjunto de CISA sobre el preposicionamiento patrocinado por Estados en las infraestructuras críticas de EE. UU. ([AA24-038A, 2024](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)) ofrecen técnicas, indicadores y mitigaciones de casos investigados. Léalos buscando: **qué se observó** (técnicas, sectores atacados, vectores de entrada); **qué se recomienda** (mitigaciones, a menudo priorizadas); y **qué se infiere** (intención, escala). Traduzca las técnicas observadas en preguntas sobre su propio entorno («¿lo veríamos?») en lugar de en una probabilidad. Un aviso es evidencia de que una amenaza existe y de cómo opera, no una estimación de con qué frecuencia tiene éxito.

### 10.4 Leer la afirmación de un proveedor

Las afirmaciones de los proveedores merecen la misma disciplina de lectura. Pregunte: ¿cuál es el **resultado** (¿incidentes comunicados?, ¿incidentes detectados?, ¿pérdidas?); cuál es el **denominador** (¿clientes, emplazamientos, años-operador?); **quién está en cada grupo** y por qué (autoselección, tamaño, sector); y **qué efecto tendría un producto de detección sobre el resultado** (más monitorización encuentra más incidentes). La investigación sobre el aprendizaje automático en seguridad enumera trampas (sesgo de muestreo, fisgoneo de datos, referencias de comparación inadecuadas, falacia de la tasa base, modelos de amenaza poco realistas) que se aplican a muchas evaluaciones de productos ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)).

### 10.5 Confusión y paradoja de Simpson

Cuando los grupos difieren en un factor que también afecta al resultado, una comparación agregada puede apuntar en sentido contrario al de todas las comparaciones dentro de cada grupo. Es la **paradoja de Simpson** ([Simpson, 1951](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x)). En los datos de seguridad, el tamaño es un factor de confusión frecuente: los operadores grandes tienen más sistemas, más obligaciones de notificación y más incidentes, y compran productos en proporciones distintas de las de los pequeños. El remedio es **estratificar** (comparar dentro de franjas de tamaño) o **estandarizar** (reponderar los grupos para que tengan la misma composición) y preguntarse si el resultado mide el daño o la detección.

### 10.6 Transferencia

Un hallazgo es transferible a su contexto solo si el mecanismo que lo produjo opera allí. La literatura formal sobre la transportabilidad pregunta qué diferencias entre poblaciones cambian el efecto ([Pearl and Bareinboim, 2014](https://doi.org/10.1214/14-STS486)); en la práctica, enumere las condiciones de las que dependía el hallazgo (tamaño, sector, notificación regulatoria, tecnología, dotación de personal) y compruebe cada una para su organización. Un hallazgo sobre la mortalidad procedente de un sistema sanitario nacional con mecanismos de desvío en toda la red puede no ser transferible a una región rural con un solo hospital.

Para el folleto del proveedor de este capítulo, la transferencia es una cuestión adicional tras la confusión: incluso una comparación bien diseñada entre otros operadores solo se aplicaría a Merrow Bay si su tamaño, su práctica de notificación y su planta se parecieran a los de los miembros del foro. Anote las condiciones y marque cada una como comprobada, desconocida o distinta.

### 10.7 La ficha de evidencia

Resuma cada fuente importante para quienes deciden en una breve **ficha de evidencia**: la pregunta a la que ayuda a responder; el diseño y el contexto; el hallazgo principal con su tamaño y su incertidumbre; la afirmación más fuerte que respalda; las limitaciones clave y su sentido probable; la transferencia a nuestro contexto; y qué haremos con ella. Guarde las fichas en una biblioteca para que las decisiones posteriores puedan citarlas (los registros de decisiones del capítulo 1). Una ficha es breve por diseño, normalmente de una página, para que un directivo pueda leerla antes de una reunión. La afirmación más fuerte respaldada debe redactarse con las palabras que usted estaría dispuesto a defender ante los autores; si la conclusión de la propia fuente es más fuerte, dígalo y explique la diferencia. Feche cada ficha e indique cuándo debe revisarse, porque los avisos y los datos de los proveedores envejecen rápido.

### 10.8 Ejemplo resuelto: el folleto de un proveedor de monitorización (sintético)

Un proveedor de monitorización de TO dice al foro de resiliencia: «Los clientes que usan nuestra monitorización tuvieron un 40 % menos de incidentes comunicados». Cuando se le piden datos, el proveedor facilita recuentos por tamaño del operador. El Lab 10 los vuelve a leer. El primer paso del especialista es preguntar qué hay detrás de la cifra antes de discutirla: qué cuenta como incidente, a lo largo de cuántos años-operador y en qué se diferencian los clientes de los no clientes. La disposición del proveedor a facilitar recuentos por tamaño es útil en sí misma; un proveedor que se niega a compartir cualquier denominador ha dado al foro un motivo para tratar la afirmación como publicidad. El foro acuerda revisar los datos conjuntamente en lugar de responder al folleto.

### 10.9 Actividad práctica: agregación, denominadores y detección

```python
# Lab 10 - re-reading a vendor claim: aggregation, denominators and survivorship (offline, stdlib only)
# Synthetic: a vendor brochure says "customers using our OT monitoring had 40% fewer reported incidents".
# Below are the (invented) counts behind such a claim, split by operator size.
DATA = {  # stratum: {group: (operators, operator-years observed, incidents reported)}
    "small (<50 staff)": {"monitoring": (240, 720, 54), "none": (100, 300, 15)},
    "large (>=50 staff)": {"monitoring": (20, 60, 18),   "none": (100, 300, 75)},
}
def rate(g):
    oy = sum(DATA[s][g][1] for s in DATA); inc = sum(DATA[s][g][2] for s in DATA)
    return inc / oy, inc, oy
for g in ("monitoring", "none"):
    r, inc, oy = rate(g); print(f"pooled {g:10s} {inc:3d} incidents / {oy:4d} operator-years = {r:.3f}")
rm, rn = rate("monitoring")[0], rate("none")[0]
print(f"pooled relative difference: {(rm - rn) / rn:+.0%}")
for s, grp in DATA.items():
    a = grp["monitoring"][2] / grp["monitoring"][1]; b = grp["none"][2] / grp["none"][1]
    print(f"{s:20s} monitoring {a:.3f}  none {b:.3f}  ratio {a/b:.2f}")
# Standardize both groups to the same size mix (the 'none' group's operator-years) - direct standardization
w = {s: DATA[s]["none"][1] for s in DATA}; W = sum(w.values())
std = {g: sum(w[s] / W * DATA[s][g][2] / DATA[s][g][1] for s in DATA) for g in ("monitoring", "none")}
print(f"size-standardized: monitoring {std['monitoring']:.3f}  none {std['none']:.3f}  ratio {std['monitoring']/std['none']:.2f}")
```

Salida esperada:

```text
pooled monitoring  72 incidents /  780 operator-years = 0.092
pooled none        90 incidents /  600 operator-years = 0.150
pooled relative difference: -38%
small (<50 staff)    monitoring 0.075  none 0.050  ratio 1.50
large (>=50 staff)   monitoring 0.300  none 0.250  ratio 1.20
size-standardized: monitoring 0.188  none 0.150  ratio 1.25
```

**Interpretación.** En el agregado, los operadores monitorizados comunican 0,092 incidentes por año-operador frente a 0,150 de los no monitorizados, una diferencia del 38 %: la afirmación del folleto. Pero dentro de cada franja de tamaño, los operadores monitorizados comunican **más** incidentes: 1,5 veces más entre los operadores pequeños y 1,2 veces más entre los grandes. La comparación agregada se invierte porque la mayoría de los operadores monitorizados son pequeños, y los operadores pequeños comunican menos incidentes usen lo que usen. Estandarizados a la misma composición por tamaños, los operadores monitorizados comunican 1,25 veces más incidentes. Además, «incidentes comunicados» es un resultado de detección: un producto de monitorización que funcione debería *aumentar* los incidentes comunicados al encontrar lo que pasaba desapercibido. Ni las cifras agregadas ni las estratificadas dicen nada sobre el daño evitado. La respuesta correcta al proveedor no es «su producto es malo», sino «su afirmación no se desprende de estos datos; muéstrennos resultados en unidades de servicio, emparejados por tamaño y sector, a lo largo del tiempo».

### 10.10 Errores comunes y límites

- Leer los resultados antes de identificar el diseño.
- Tratar la lista de casos de un aviso como una estimación de frecuencia.
- Comparar grupos que difieren en tamaño o sector sin estratificar.
- Tratar los incidentes comunicados como una medida del daño o de la seguridad.
- Aceptar un hallazgo sin comprobar si su mecanismo opera en su contexto.
- Descartar por completo una fuente porque tiene una debilidad.
- Citar una fuente para más de lo que mostró.

El límite de la lectura crítica es el tiempo. Priorice las fuentes que podrían cambiar una decisión (el valor de la información del capítulo 1), léalas con cuidado y acepte una lectura más ligera para el resto.

### Ejercicios — capítulo 10

**EX046 — Vuelva a leer el folleto.** *Objetivo:* reproducir y explicar una inversión. *Entradas:* el Lab 10. *Restricciones:* 250 palabras para la explicación. *Pasos:* (1) ejecute el laboratorio; (2) explique la inversión al foro en lenguaje claro; (3) proponga dos medidas de resultado que mostrarían mejor el valor del producto. *Evidencia esperada:* salida y explicación. *Rúbrica:* 3 = inversión explicada mediante la composición por tamaños y el efecto de la detección, se cita la razón estandarizada, medidas de resultado vinculadas al daño (por ejemplo, horas de interrupción del servicio, tiempo hasta detectar pruebas inyectadas); 2 = inversión explicada, medidas débiles; 1 = repite el folleto; 0 = nada.

**EX047 — Ficha de evidencia: hospitales vecinos.** *Objetivo:* resumir un estudio para Merrow Health. *Entradas:* el resumen de Dameff et al. (2023). *Restricciones:* use la estructura del §10.7; cite cifras solo de la fuente. *Pasos:* redacte la ficha. *Evidencia esperada:* ficha de una página. *Rúbrica:* 3 = diseño identificado como antes y después en una sola institución, hallazgos expresados con sus medidas, limitaciones (un solo emplazamiento, estacionalidad, ninguna región de control) con su sentido, se discute la transferencia al sistema de tres hospitales de Merrow Bay, se indica una acción (por ejemplo, la planificación regional de desvíos); 2 = limitaciones sin sentido; 1 = exagera la causalidad; 0 = nada.

**EX048 — Ficha de evidencia: WannaCry.** *Objetivo:* resumir un estudio nacional. *Entradas:* Ghafur et al. (2019) y la investigación de la NAO. *Restricciones:* distinga los propósitos de las dos fuentes. *Pasos:* redacte una ficha que responda a «¿qué dice WannaCry a Merrow Health sobre las consecuencias de un evento de *ransomware* a gran escala?». *Evidencia esperada:* ficha. *Rúbrica:* 3 = se distinguen los hallazgos del estudio (alrededor de un 6 % menos de ingresos al día en los hospitales infectados; ninguna diferencia detectada en la mortalidad, con la cautela de los autores) y el propósito de auditoría de la NAO, se indican las cuestiones de transferencia, se indica una acción; 2 = fuentes mezcladas; 1 = «no hubo muertes, así que el riesgo es bajo»; 0 = nada.

**EX049 — Del aviso a las preguntas.** *Objetivo:* usar bien un aviso. *Entradas:* el AA24-038A de CISA. *Restricciones:* no estime probabilidades a partir de él. *Pasos:* (1) extraiga cinco técnicas o comportamientos observados; (2) para cada uno, redacte la pregunta «¿lo veríamos en Merrow Water?» y la fuente de evidencia que la respondería; (3) elija dos mitigaciones recomendadas y relaciónelas con las prácticas del capítulo 2. *Evidencia esperada:* tabla. *Rúbrica:* 3 = comportamientos observados resumidos con exactitud (por ejemplo, el uso de cuentas válidas y las técnicas que aprovechan herramientas legítimas del propio sistema), preguntas de detección vinculadas a registros concretos, mitigaciones relacionadas; 2 = mezcla observación e inferencia; 1 = solo un resumen; 0 = nada.

**EX050 — Comprobación de trampas.** *Objetivo:* aplicar una lista de comprobación de investigación a la evaluación de un producto. *Entradas:* un proveedor afirma que su detector de anomalías basado en aprendizaje automático «alcanzó una exactitud del 99 % con un conjunto de datos público de un banco de pruebas de tratamiento de agua». *Restricciones:* use las trampas de Arp et al. (2022). *Pasos:* enumere cinco preguntas que haría y por qué importa cada una. *Evidencia esperada:* lista. *Rúbrica:* 3 = la tasa base y la cuestión de la exactitud frente a la precisión, la fuga entre entrenamiento y prueba (fisgoneo de datos), la transferencia del banco de pruebas a la planta, la comparación con una referencia, el realismo del modelo de amenaza; 2 = tres; 1 = escepticismo genérico; 0 = nada.

### Síntesis del capítulo

Lea para decidir. Empareje la fuente con la pregunta: los estudios para los tamaños del efecto y los mecanismos, los avisos para las técnicas y las mitigaciones, los informes de proveedores para hipótesis que hay que verificar. Identifique el diseño antes que los resultados y limite las afirmaciones a lo que el diseño respalda. Compruebe el resultado, el denominador, la comparación y los factores de confusión; estratifique o estandarice cuando los grupos difieran, y recuerde que los incidentes comunicados miden tanto la detección como el daño. Pregúntese si el mecanismo es transferible a su contexto. Registre lo que aprenda en fichas de evidencia que los registros de decisiones puedan citar.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Siga estudiando — capítulo 10 de 12

[← Capítulo 09](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Proyecto aplicado

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Delimitar una mejora de seguridad a escala de la organización como un proyecto con una persona que decide, un objetivo basado en la consecuencia y unos beneficios medibles.
2. Planificar la ejecución con las partes interesadas, los riesgos, las condiciones de seguridad y los puntos de control.
3. Evaluar el resultado con honestidad mediante un grupo de comparación, una estimación de diferencias en diferencias y una comprobación por permutación.
4. Poner a prueba la robustez del resultado de un proyecto e informar de sus límites.
5. Presentar el proyecto para su evaluación según una rúbrica explícita.

El proyecto aplicado es donde el curso se convierte en práctica. Usa todos los capítulos anteriores: el planteamiento y los registros de decisiones (1), la práctica actual y la verificación (2), la evidencia (3), el riesgo y la ética (4), el diseño (5), la evaluación controlada (6), la integración (7), el razonamiento sobre casos difíciles (8), el aseguramiento (9) y la lectura crítica (10). A diferencia de un trabajo de fin de máster, su propósito no es responder a una pregunta de investigación para otros; es **mejorar un servicio real y mostrar de forma creíble si se consiguió**. Después, el capítulo 12 repasa el curso y lo transfiere.

### 11.1 Elegir el proyecto

Un buen proyecto aplicado de posgrado es: **trascendente** (cambia la exposición de un servicio esencial, no solo un documento); **acotado** (realizable en unos dos semestres de trabajo a tiempo parcial); **con titular** (un patrocinador designado con autoridad y unos titulares operativos que lo quieren); **medible** (un beneficio que pueda observarse, preferiblemente en unidades de servicio); **seguro y autorizado** (no crea ningún riesgo no aprobado para las operaciones, las personas o los datos); y **evaluable** (existe una forma de compararlo con lo que habría ocurrido sin él). Proyectos típicos: la preparación para la operación manual de un grupo de emplazamientos; el acceso intermediado de proveedores para un sistema de control; una capacidad de restauración para los sistemas clínicos; un plan regional de concentración de proveedores. Si usted no trabaja en el sector, el proyecto puede llevarse a cabo sobre un caso sintético realista como Merrow Bay, con los mismos entregables.

### 11.2 El acta de constitución del proyecto

Un **acta de constitución** de una página fija: el problema y su consecuencia; el patrocinador y los derechos de decisión; los objetivos y los beneficios, con medidas y líneas base; el alcance y las exclusiones; los entregables; las partes interesadas; las restricciones (seguridad, presupuesto, regulación); los riesgos; el diseño de la evaluación; los hitos y los puntos de control; y la rúbrica de evaluación. Escribir el diseño de la evaluación en el acta antes de la ejecución es el equivalente en un proyecto del prerregistro ([Nosek et al., 2018](https://doi.org/10.1073/pnas.1708274114)): protege al especialista de la tentación de elegir después la medida que mejor queda ([Kerr, 1998](https://doi.org/10.1207/s15327957pspr0203_4)).

### 11.3 Ejecutar a través de las personas

La mayoría de los proyectos de seguridad en los servicios esenciales fracasan por la adopción, no por la tecnología. Mapee a las partes interesadas según su influencia y su interés; acuerde con operaciones cómo y cuándo los cambios afectan a la planta; planifique la formación y la práctica supervisada; y anticipe quién pierde algo (comodidad, autonomía, presupuesto). Un **pre mortem** al inicio ([Klein, 2007](https://hbr.org/2007/09/performing-a-project-premortem)) saca a la luz pronto los riesgos de adopción. Lleve un registro de decisiones del proyecto con el formato del capítulo 1 para que los revisores posteriores puedan ver por qué cambió el plan.

En Merrow Water, las personas más afectadas por el proyecto del manual de operación son los operadores de turno, que deben practicar la operación manual en simulacros trimestrales además de su trabajo habitual. Acordar los horarios de los simulacros con los jefes de turno y usar sus comentarios para revisar el manual hace mucho más probable la adopción que emitirlo desde la sede central.

### 11.4 Evaluar el resultado

Las comparaciones antes y después son seductoras y débiles: puede que el resultado hubiera mejorado de todos modos por la estación, la práctica, el personal nuevo u otros proyectos. Un diseño más fuerte y práctico es el de **diferencias en diferencias (DiD)**: comparar el cambio en los emplazamientos que recibieron el proyecto (piloto) con el cambio en emplazamientos similares que no lo recibieron (comparación) durante el mismo periodo. La estimación es (piloto después − piloto antes) − (comparación después − comparación antes). Su supuesto clave es el de las **tendencias paralelas**: sin el proyecto, los emplazamientos piloto y los de comparación habrían cambiado en la misma medida. El diseño se popularizó en economía gracias a un conocido estudio que comparaba el empleo en estados vecinos ([Card and Krueger, 1994](https://www.jstor.org/stable/2118030)); se aplica igual a los tiempos de los simulacros o a los tiempos de recuperación entre emplazamientos.

Con pocos emplazamientos, los errores estándar ordinarios no son fiables. Una **comprobación por permutación** es sencilla y honesta: calcule la DiD para cada forma posible de elegir qué emplazamientos fueron «piloto» y pregúntese lo inusual que es la estimación de la asignación real. Si muchas asignaciones aleatorias producen estimaciones igual de grandes, el resultado podría deberse al azar. Por último, ponga a prueba la **robustez**: elimine el emplazamiento más influyente, use otra definición del resultado o compruebe si los emplazamientos piloto y los de comparación ya divergían antes del proyecto.

### 11.5 Informar del proyecto

El informe final indica el problema, lo que se hizo, lo que cambió, con cuánta seguridad lo sabemos y lo que queda pendiente. Informa primero de la medida especificada de antemano; los análisis adicionales se etiquetan como exploratorios. Las limitaciones se redactan con su **sentido** (¿haría esta debilidad que el efecto pareciera mayor o menor?) para que los lectores puedan juzgar el resultado. Los beneficios que no pudieron medirse se describen, no se inventan. El informe termina con el traspaso: los titulares, el mantenimiento, la evidencia de aseguramiento que mantendrá vigente la afirmación (capítulo 9) y el desencadenante de revisión.

### 11.6 Rúbrica de evaluación

Los proyectos se evalúan según cinco criterios, cada uno puntuado de 0 a 3:

| Criterio | 3 (excelente) | 1 (débil) |
|---|---|---|
| Planteamiento | Problema basado en la consecuencia, patrocinador, beneficio medible, evaluación especificada de antemano | Problema vago; medida elegida después de los resultados |
| Ejecución | Segura, autorizada, adoptada por operaciones; decisiones registradas | Ejecutado solo sobre el papel; operaciones esquivada |
| Evaluación | Grupo de comparación, DiD o equivalente, incertidumbre y robustez comunicadas | Solo antes y después, sin incertidumbre |
| Ética y seguridad | Riesgos para las personas y el servicio evaluados; distribución considerada | No considerados |
| Comunicación y traspaso | Informe claro, limitaciones con su sentido, titulares y evidencia de aseguramiento | Defensa de parte; sin traspaso |

### 11.7 Ejemplo resuelto: el proyecto del manual de operación manual (sintético)

El especialista de Merrow Water dirigió un proyecto para introducir un manual de operación manual y simulacros trimestrales en seis plantas (piloto), elegidas porque tenían los sistemas de control más antiguos; otras seis plantas siguieron como antes (comparación). El resultado especificado de antemano era la media de minutos hasta lograr una operación manual estable en los simulacros trimestrales, promediada en dos trimestres anteriores y dos posteriores. El acta especificó de antemano una DiD con una comprobación por permutación y una comprobación de robustez que eliminaba el emplazamiento más influyente.

Elegir los emplazamientos piloto por sus sistemas de control antiguos era sensato para el servicio, porque esas plantas eran las que más necesitaban el manual, pero significa que los grupos piloto y de comparación no eran iguales al principio. Por eso el acta exigía diferencias en diferencias en lugar de una comparación solo posterior, y por eso las tendencias paralelas deben argumentarse en lugar de suponerse. Está previsto que las seis plantas de comparación reciban el manual en la siguiente fase, lo que ofrece una oportunidad posterior de poner a prueba el resultado.

### 11.8 Actividad práctica: ¿funcionó?

```python
# Lab 11 - did the project work? Difference-in-differences with a permutation check (offline, stdlib only)
# Synthetic: Merrow Water piloted a manual-operation runbook and drills at six works (pilot) and not at six others.
# Outcome: mean minutes to stable manual operation in quarterly drills, two quarters before and two after.
from itertools import combinations
SITES = {  # site: (pilot?, mean minutes before, mean minutes after)
    "Hollin": (1, 41, 27), "Fenley": (1, 38, 29), "Upper Merrow": (1, 55, 36), "Kettle Ford": (1, 33, 28),
    "Ashby": (1, 47, 35), "Saltings": (1, 36, 30),
    "Brack": (0, 39, 35), "Dunmere": (0, 44, 40), "Orrin": (0, 35, 34), "Pelling": (0, 50, 43),
    "Quarry Lane": (0, 31, 30), "Rook": (0, 42, 36),
}
def did(treated):
    t = [SITES[s][2] - SITES[s][1] for s in SITES if s in treated]
    c = [SITES[s][2] - SITES[s][1] for s in SITES if s not in treated]
    return sum(t) / len(t) - sum(c) / len(c), sum(t) / len(t), sum(c) / len(c)
pilot = {s for s, v in SITES.items() if v[0]}
est, dt, dc = did(pilot)
print(f"pilot change {dt:+.2f} min, comparison change {dc:+.2f} min, difference-in-differences {est:+.2f} min")
naive = sum(SITES[s][2] for s in pilot) / 6 - sum(SITES[s][2] for s in SITES if s not in pilot) / 6
print(f"naive after-only difference {naive:+.2f} min")
allc = [did(set(c))[0] for c in combinations(SITES, 6)]
p = sum(1 for d in allc if d <= est) / len(allc)
print(f"permutation: {len(allc)} assignments; share with DiD <= observed = {p:.4f}")
# Sensitivity: drop the site with the largest pilot improvement
big = min(pilot, key=lambda s: SITES[s][2] - SITES[s][1])
rest = {s: SITES[s] for s in SITES if s != big}
t = [v[2]-v[1] for s, v in rest.items() if v[0]]; c = [v[2]-v[1] for s, v in rest.items() if not v[0]]
print(f"without {big}: DiD {sum(t)/len(t) - sum(c)/len(c):+.2f} min")
```

Salida esperada:

```text
pilot change -10.83 min, comparison change -3.83 min, difference-in-differences -7.00 min
naive after-only difference -5.50 min
permutation: 924 assignments; share with DiD <= observed = 0.0087
without Upper Merrow: DiD -5.37 min
```

**Interpretación.** Los emplazamientos piloto mejoraron 10,8 minutos en promedio; los de comparación, 3,8 minutos, probablemente por la práctica y la concienciación generales. La estimación DiD es una mejora de 7,0 minutos atribuible al proyecto bajo el supuesto de tendencias paralelas. Una comparación ingenua solo posterior (5,5 minutos) la subestimaría, porque los emplazamientos piloto partían de tiempos más lentos: se eligieron por sus sistemas antiguos. De las 924 asignaciones posibles de seis emplazamientos «piloto», menos del 1 % produce una mejora tan grande como la real, así que el azar es una explicación improbable. Eliminar Upper Merrow, el emplazamiento con la mayor mejora, reduce la estimación a 5,4 minutos: el resultado es robusto en su sentido, pero sensible en su tamaño a un solo emplazamiento. El informe debería decir «entre 5 y 7 minutos más rápido, principalmente, aunque no solo, por Upper Merrow», señalar que los emplazamientos piloto se seleccionaron por sus sistemas antiguos (de modo que las tendencias paralelas son un supuesto que hay que defender) y recomendar extender el manual a los emplazamientos de comparación con la misma evaluación.

### 11.9 Errores comunes y límites

- Elegir un proyecto por su interés y no por su consecuencia.
- Empezar sin un patrocinador que pueda tomar decisiones.
- Definir la medida del éxito después de ver los resultados.
- Evaluar solo con una comparación antes y después.
- Informar de una única estimación sin comprobar el azar ni la robustez.
- Enumerar las limitaciones sin su sentido.
- Terminar sin traspaso, de modo que el beneficio se degrada.

Con una docena de emplazamientos, ninguna evaluación es definitiva. La evaluación del proyecto debe ser honesta al respecto y estar diseñada para que la siguiente fase (por ejemplo, el despliegue escalonado en los emplazamientos de comparación) aporte más evidencia.

### Ejercicios — capítulo 11

**EX051 — Acta de constitución del proyecto.** *Objetivo:* delimitar su propio proyecto aplicado. *Entradas:* su organización, o Merrow Bay. *Restricciones:* una página; todos los elementos del acta del §11.2; evaluación especificada de antemano. *Pasos:* redacte el acta. *Evidencia esperada:* acta. *Rúbrica:* use los criterios «Planteamiento» y «Ética y seguridad» del §11.6; 3 = trascendente, acotado, con titular, medible, seguro y evaluable, con una comparación designada; 2 = evaluación vaga; 1 = actividad en lugar de resultado; 0 = nada.

**EX052 — Robustez del resultado de la permutación.** *Objetivo:* comprobar la sensibilidad a un solo emplazamiento. *Entradas:* el Lab 11. *Restricciones:* elimine por completo Upper Merrow de los datos (11 emplazamientos, 5 piloto). *Pasos:* (1) vuelva a calcular la DiD; (2) vuelva a calcular la proporción de la permutación sobre todas las asignaciones de 5 pilotos entre 11 emplazamientos; (3) interprételo. *Evidencia esperada:* cifras y un párrafo. *Rúbrica:* 3 = DiD de −5,37 minutos, 462 asignaciones, proporción de aproximadamente 0,017; interpretación de que el resultado sigue siendo improbable por azar pero es más débil, con el sentido de la limitación de selección; 2 = cifras correctas, interpretación pobre; 1 = no ejecutado; 0 = nada.

**EX053 — Plan de partes interesadas y de adopción.** *Objetivo:* planificar la ejecución a través de las personas. *Entradas:* el proyecto del manual. *Restricciones:* incluya los turnos de noche y a los contratistas. *Pasos:* mapee a las partes interesadas; identifique quién pierde qué; planifique la formación, la práctica supervisada y la retroalimentación; haga un breve pre mortem y enumere tres historias de fracaso con sus mitigaciones. *Evidencia esperada:* plan. *Rúbrica:* 3 = partes interesadas concretas, pérdidas reconocidas, formación basada en la práctica, historias de pre mortem creíbles; 2 = sin pre mortem; 1 = solo un plan de comunicación; 0 = nada.

**EX054 — Limitaciones con su sentido.** *Objetivo:* redactar limitaciones que ayuden a los lectores a juzgar. *Entradas:* el resultado del Lab 11. *Restricciones:* al menos cinco limitaciones, cada una con su sentido y con cómo podría abordarla una fase posterior. *Pasos:* redáctelas. *Evidencia esperada:* lista. *Rúbrica:* 3 = selección de los emplazamientos piloto, regresión a la media (los emplazamientos lentos mejoran más de todos modos; inflaría), efectos de la práctica, muestra pequeña, realismo de los simulacros frente a los sucesos reales, contaminación de los emplazamientos de comparación; sentidos correctos; 2 = faltan los sentidos; 1 = genérico; 0 = nada.

**EX055 — Traspaso y beneficios.** *Objetivo:* hacer que los beneficios perduren. *Entradas:* el proyecto del manual a su término. *Restricciones:* use las ideas de caso de aseguramiento y de vigencia del capítulo 9. *Pasos:* (1) designe a los titulares; (2) defina la afirmación de aseguramiento y la evidencia, con sus antigüedades máximas; (3) defina un indicador para el consejo con una referencia XmR; (4) defina el desencadenante de revisión. *Evidencia esperada:* nota de traspaso. *Rúbrica:* 3 = titulares operativos, evidencia de grado verificado con su antigüedad, indicador con el periodo de referencia indicado, desencadenante concreto; 2 = falta un elemento; 1 = «proyecto cerrado»; 0 = nada.

### Síntesis del capítulo

Un proyecto aplicado mejora un servicio real y muestra de forma creíble si lo consiguió. Elija algo trascendente, acotado, con titular, medible, seguro y evaluable; fije la evaluación en un acta antes de la ejecución; ejecútelo a través de las personas, con el consentimiento de operaciones y un pre mortem; evalúelo con un grupo de comparación, diferencias en diferencias, una comprobación por permutación y pruebas de robustez; informe de las limitaciones con su sentido; y haga el traspaso con titulares, evidencia de aseguramiento y un desencadenante de revisión.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Siga estudiando — capítulo 11 de 12

[← Capítulo 10](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Revisión final y transferencia

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted debería ser capaz de:

1. Integrar los métodos del curso en un enfoque coherente de las decisiones de seguridad a escala de la organización.
2. Transferir una decisión de un sector a otro reexaminando los supuestos y volviendo a obtener los pesos.
3. Hallar el peso con el que se invierte una recomendación multicriterio y usarlo para centrar la discusión.
4. Evaluar su propia competencia frente al resultado del curso con evidencia y planificar su desarrollo continuo.
5. Completar un análisis de caso avanzado que se apoye en todos los capítulos.

Este capítulo final repasa el curso como un único método, practica su transferencia a un sector nuevo y prepara la evaluación final. Su último ejercicio es el caso integrador del curso.

### 12.1 El curso como un único método

Leído de principio a fin, el curso describe un ciclo que un especialista ejecuta de forma continua:

1. **Plantear** la decisión: titular, opciones (incluida la de aplazar), objetivos en unidades de servicio (capítulo 1).
2. **Conocer la línea base**: obligaciones, orientaciones y práctica verificada (capítulo 2).
3. **Establecer los hechos**: evidencia que separe la observación de la inferencia (capítulo 3).
4. **Cuantificar y distribuir el riesgo**: frecuencia, gravedad, cola y quién lo soporta (capítulo 4).
5. **Diseñar alternativas**: primero la consecuencia, comparadas como grafos y como sistemas operables (capítulo 5).
6. **Evaluar antes de confiar**: pruebas controladas con intervalos (capítulo 6).
7. **Integrar**: titularidad, proveedores, mando de emergencias e intercambio de información (capítulo 7).
8. **Prepararse para los casos difíciles**: pesos, relojes y obligaciones acordados de antemano (capítulo 8).
9. **Dirigir y asegurar**: indicadores, casos de aseguramiento, evidencia vigente (capítulo 9).
10. **Leer con sentido crítico**: estudios, avisos y afirmaciones, con vistas a su transferencia (capítulo 10).
11. **Ejecutar y evaluar proyectos** con honestidad (capítulo 11).

Cada paso produce un artefacto que otros pueden inspeccionar: un registro de decisión, un plan de verificación, un hallazgo, una curva de excedencia de pérdidas con una tabla de distribución, un ADR, un informe de evaluación, un RACI, un acuerdo sobre los pesos del restablecimiento, un caso de aseguramiento, una ficha de evidencia, un informe de proyecto. La credibilidad de un especialista descansa en esos artefactos más que en cualquier juicio aislado.

### 12.2 Transferencia entre sectores

Los especialistas cambian de sector, y el trabajo regional exige razonar sobre varios a la vez. La transferencia fracasa de dos maneras características: copiando **conclusiones** que dependían de las condiciones del primer sector; y copiando **pesos** que reflejaban los valores del primer sector. La transferencia tiene éxito cuando se copia el **método** y se reexamina cada supuesto. Una lista de comprobación práctica para la transferencia:

- **Consecuencia y tiempo:** ¿cuál es la función esencial y con qué rapidez llega el daño cuando falla? (Los minutos de un hospital, las horas de un sistema de agua, los días de un puerto).
- **Física y seguridad funcional:** ¿qué modos de fallo puede causar la propia acción de seguridad?
- **Regulación:** ¿qué regímenes y plazos de notificación se aplican, y qué evidencia esperan?
- **Personas y proveedores:** ¿quién implantará y operará la medida? ¿Qué proveedores concentran el riesgo?
- **Datos y privacidad:** ¿qué datos personales o sensibles están implicados y qué deberes se derivan de ello? La seguridad sanitaria, por ejemplo, está sujeta a deberes de protección de datos y de privacidad sanitaria a los que una empresa de agua rara vez se enfrenta ([GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj); [HHS, HPH CPGs](https://hphcyber.hhs.gov/performance-goals.html)). *Nota para el lector hispanohablante:* en España, el RGPD se complementa con la Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales; en América Latina rige la ley de cada país, por ejemplo la Ley 25.326 en Argentina o la Ley 1581 de 2012 en Colombia.
- **Valores:** ¿a qué dan más peso los líderes de este sector y las personas a las que sirve, y quién debería fijar los pesos?

### 12.3 Decisiones multicriterio y puntos de inversión

Cuando las opciones se comparan según varios criterios con pesos (un modelo sencillo de suma ponderada), la recomendación depende de los pesos. En lugar de defender un único conjunto de pesos, halle el **punto de inversión**: el peso con el que cambia la recomendación. Si el punto de inversión está lejos de cualquier peso plausible, la recomendación es robusta; si está cerca, la discusión debe centrarse en ese peso. El análisis de sensibilidad sistemático de los modelos es un campo en sí mismo ([Saltelli et al., 2008](https://doi.org/10.1002/9780470725184)); para una decisión con tres opciones, suele bastar un barrido unidimensional. Es el equivalente multicriterio de los umbrales de probabilidad del capítulo 1.

### 12.4 Autoevaluación y práctica continuada

El resultado del curso es **dirigir la aplicación avanzada y justificar las elecciones a escala de la organización** en infraestructura crítica y seguridad sectorial. Evalúese frente a él con evidencia, no con sensaciones: para cada capítulo, ¿qué artefacto ha producido, con qué nivel (las rúbricas de los ejercicios) y qué retroalimentación ha recibido? Las carencias se convierten en un plan de desarrollo continuo con práctica concreta, no solo con cursos: dirija un simulacro; redacte un registro de decisión para una decisión real; revise el contrato de un proveedor; informe a un consejo; presente una ficha de evidencia a sus colegas. Los códigos profesionales esperan que los profesionales mantengan su competencia y trabajen dentro de ella ([ACM Code of Ethics](https://www.acm.org/code-of-ethics); [NSPE Code of Ethics](https://www.nspe.org/resources/ethics/code-ethics)). Las leyes, los estándares y las amenazas cambiarán a lo largo de su carrera; los hábitos de plantear bien, aportar evidencia, ser honesto con la incertidumbre y registrar el juicio, no.

### 12.5 Ejemplo resuelto: transferir la elección de un programa a Merrow Health (sintético)

El panel de Merrow Water puntuó tres programas de seguridad según cuatro criterios (0–10): continuidad del servicio esencial, seguridad de las personas, asequibilidad y privacidad. La dirección de Merrow Water ponderó mucho la continuidad y poco la privacidad. Merrow Health quiere reutilizar el análisis. El especialista copia las puntuaciones solo después de comprobar cada una con colegas clínicos y de gobernanza de la información (en este ejemplo se confirman) y pide a la dirección de Merrow Health que fije sus propios pesos. El Lab 12 compara los resultados y halla el punto de inversión.

Copiar las puntuaciones es en sí un juicio. Las puntuaciones de continuidad y de seguridad podrían ser distintas en un hospital, donde los sistemas clínicos que fallan causan daño en minutos y la privacidad conlleva deberes legales a los que una empresa de agua rara vez se enfrenta. Registrar que cada puntuación se comprobó, y quién lo hizo, permite al lector ver que la transferencia descansa en datos de entrada verificados y no solo en el panel de Merrow Water.

### 12.6 Actividad práctica: mismas opciones, pesos distintos

```python
# Lab 12 - transferring a decision to another sector: same options, different weights (offline, stdlib only)
# Synthetic: three security programmes scored 0-10 on four criteria by Merrow Water's panel, then reused
# by Merrow Health. Scores are invented; the weights are what each sector's leadership agreed.
OPTIONS = {  # option: scores on (continuity of essential service, safety of people, cost-affordability, privacy)
    "P1 manual-operation readiness":     (9, 7, 6, 4),
    "P2 identity and remote-access":     (6, 6, 7, 8),
    "P3 network monitoring and response": (7, 5, 4, 6),
}
CRIT = ["continuity", "safety", "affordability", "privacy"]
WEIGHTS = {
    "water":  (0.45, 0.30, 0.20, 0.05),
    "health": (0.25, 0.30, 0.15, 0.30),
}
for sector, w in WEIGHTS.items():
    assert abs(sum(w) - 1) < 1e-9
    scores = {o: sum(a * b for a, b in zip(s, w)) for o, s in OPTIONS.items()}
    print(sector, " ".join(f"{o.split()[0]}={v:.2f}" for o, v in scores.items()), " best:", max(scores, key=scores.get).split()[0])
# Sweep the privacy weight, taking it proportionally from the other water weights, to find the reversal point
w0 = WEIGHTS["water"]; prev = None
for k in range(0, 61):
    p = k / 100; rest = sum(w0[:3])
    w = tuple(x / rest * (1 - p) for x in w0[:3]) + (p,)
    best = max(OPTIONS, key=lambda o: sum(a * b for a, b in zip(OPTIONS[o], w))).split()[0]
    if best != prev: print(f"privacy weight {p:.2f}: best {best}"); prev = best
```

Salida esperada:

```text
water P1=7.55 P2=6.30 P3=5.75  best: P1
health P1=6.45 P2=6.75 P3=5.65  best: P2
privacy weight 0.00: best P1
privacy weight 0.28: best P2
```

**Interpretación.** Con los pesos del agua, la preparación para la operación manual (P1) obtiene 7,55 y es claramente la preferida. Con los pesos de la salud (la privacidad pesa ahora 0,30 porque están en juego datos de pacientes), gana la identidad y el acceso remoto (P2), con 6,75 frente a 6,45. El barrido sobre los pesos del agua muestra que P2 supera a P1 en cuanto el peso de la privacidad pasa de aproximadamente 0,28; para la salud, el barrido inverso (EX056) muestra que P1 recupera el primer lugar en cuanto el peso de la continuidad supera aproximadamente 0,32. La lección sobre la transferencia es que **las puntuaciones viajaron, la conclusión no**: la misma evidencia, ponderada según los valores legítimos de otro sector, recomienda un programa distinto. El trabajo del especialista es hacerlo visible, no convencer a un sector de que adopte los pesos del otro. Los puntos de inversión indican además a cada dirección exactamente qué juicio debe debatir.

### 12.7 Errores comunes y límites

- Copiar una conclusión de un sector sin reexaminar sus condiciones.
- Reutilizar los pesos de otra organización como si fueran hechos.
- Defender un único conjunto de pesos en lugar de informar de los puntos de inversión.
- Tratar la finalización del curso como competencia sin evidencia.
- Planificar el desarrollo solo como cursos, no como práctica con retroalimentación.
- Suponer que las leyes, los estándares y el panorama de amenazas de hoy se mantendrán.

Los modelos de suma ponderada suponen que los criterios pueden compensarse linealmente y que las puntuaciones están en escalas comparables; ninguna de las dos cosas es del todo cierta. Son herramientas para una conversación estructurada, que se usan mejor junto con los puntos de inversión y el registro de decisión.

### Ejercicios — capítulo 12

**EX056 — El punto de inversión de la salud.** *Objetivo:* hallar dónde cambia la recomendación. *Entradas:* el Lab 12. *Restricciones:* haga un barrido del peso de la continuidad para la salud, tomando el resto proporcionalmente de los otros tres criterios. *Pasos:* (1) modifique el barrido; (2) informe del peso con el que P1 supera a P2; (3) obtenga el mismo punto algebraicamente; (4) explique qué debería debatir la dirección de Merrow Health. *Evidencia esperada:* código, salida, derivación y un párrafo. *Rúbrica:* 3 = inversión entre 0,31 y 0,32 con el barrido y 0,318 algebraicamente (4,4c − 1,4 = 0), discusión centrada en la continuidad frente a la privacidad para los servicios clínicos; 2 = solo el barrido; 1 = no ejecutado; 0 = nada.

**EX057 — Lista de comprobación de la transferencia.** *Objetivo:* transferir una conclusión del sector del agua a un puerto. *Entradas:* la recomendación robusta C del capítulo 1 (la mitad para el bastionado del acceso remoto, la mitad para la capacidad de operación manual) para Merrow Water. *Restricciones:* use la lista de comprobación del §12.2 para Port of Merrow. *Pasos:* para cada elemento, indique qué difiere y si cambia la conclusión; después, indique qué volvería a obtener. *Evidencia esperada:* tabla y conclusión. *Rúbrica:* 3 = diferencias concretas (tiempo hasta el daño en días; TO de la terminal gestionada por un contratista; regímenes distintos; concentración de proveedores en Halden Cloud y Lumen Watch; consecuencias comerciales en lugar de sanitarias), conclusión derivada de nuevo en lugar de copiada, nueva obtención enumerada; 2 = algunos elementos genéricos; 1 = copia la conclusión; 0 = nada.

**EX058 — Autoevaluación con evidencia.** *Objetivo:* evaluar la competencia frente al resultado del curso. *Entradas:* sus respuestas a los ejercicios y la retroalimentación recibida. *Restricciones:* evidencia para cada afirmación. *Pasos:* (1) para cada capítulo, enumere su artefacto y su puntuación en la rúbrica; (2) identifique sus tres áreas más débiles; (3) redacte un plan de desarrollo a 12 meses con actividades prácticas y evidencia del progreso. *Evidencia esperada:* tabla y plan. *Rúbrica:* 3 = puntuaciones honestas con evidencia, debilidades concretas, plan basado en la práctica con evidencia medible; 2 = plan solo de cursos; 1 = sin evidencia; 0 = nada.

**EX059 — Caso integrador: compromiso de un proveedor en Merrow Bay.** *Objetivo:* aplicar el curso completo a un caso avanzado. *Entradas:* escenario sintético: Corvane Systems informa de que un atacante accedió a su plataforma de soporte remoto durante once días; Corvane da soporte al SCADA de Merrow Water y de Merrow Energy y a los sistemas de anatomía patológica de Merrow Health. Los registros de Merrow Water muestran tres sesiones de Corvane en ese periodo, una de ellas de noche y sin ningún tique asociado. *Restricciones:* 3.000 palabras como máximo; solo datos sintéticos; cite los capítulos de los métodos. *Pasos:* (1) plantee las decisiones inmediatas y las estratégicas (cap. 1); (2) indique el plan probatorio y los hallazgos iniciales (cap. 3); (3) fije las prioridades de restablecimiento y de protección entre los tres operadores con pesos explícitos (cap. 4, 8); (4) evalúe los cambios de diseño en el acceso de los proveedores (cap. 5, 6); (5) aborde la titularidad, la concentración de proveedores y la coordinación del foro (cap. 7); (6) redacte las comunicaciones al consejo y al regulador (cap. 3, 9); (7) evalúe con sentido crítico las declaraciones de Corvane (cap. 10); (8) proponga un proyecto de continuación con un diseño de evaluación (cap. 11). *Evidencia esperada:* informe del caso. *Rúbrica:* de 0 a 3 en cada una de las ocho partes (máximo 24); 20 o más = excelente, 14–19 = competente, menos de 14 = todavía no competente. La máxima puntuación exige incertidumbre explícita, juicios de valor registrados y ningún engaño en las comunicaciones.

**EX060 — Práctica continuada y desencadenantes de revisión.** *Objetivo:* mantener actualizado el curso. *Entradas:* las referencias de este libro. *Restricciones:* identifique las fuentes que probablemente cambiarán. *Pasos:* (1) enumere cinco fuentes (leyes, estándares, orientaciones) que deba volver a verificar, con el modo en que las vigilará; (2) fije desencadenantes de revisión para su propia práctica (por ejemplo, un nuevo aviso que afecte a sus productos de acceso remoto); (3) indique cómo registrará los cambios en sus registros de decisiones. *Evidencia esperada:* plan de una página. *Rúbrica:* 3 = fuentes realmente volátiles (por ejemplo, la transposición de NIS2, las revisiones de NERC CIP, la revisión de la SP 800-82, las actualizaciones de los CPG, las orientaciones sectoriales), vigilancia concreta, desencadenantes concretos, método de registro de los cambios; 2 = vigilancia genérica; 1 = solo una lista; 0 = nada.

### Síntesis del capítulo

El curso es un único método: plantear, conocer la línea base, aportar evidencia, cuantificar el riesgo y su distribución, diseñar, evaluar, integrar, prepararse para los casos difíciles, dirigir y asegurar, leer con sentido crítico y ejecutar proyectos con honestidad, y cada paso produce un artefacto inspeccionable. Transfiera el método, no la conclusión: reexamine la consecuencia, la física, la regulación, las personas, los datos y los valores, y deje que cada sector fije sus propios pesos. Informe de los puntos de inversión para que los líderes debatan el juicio que importa. Evalúese con evidencia, planifique la práctica con retroalimentación y mantenga en revisión las fuentes y las decisiones a medida que cambia el campo.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Siga estudiando — capítulo 12 de 12

[← Capítulo 11](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Siguiente curso desde el índice de capítulos →](../SUBJECTS.md)

Este es el último capítulo de este curso; el índice enlaza con el siguiente curso del itinerario completo de estudio.
<!-- open-cyber-academy:chapter-navigation:end -->

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

### Capítulo 3: EX011–EX015

**EX011 — Robustez del orden.** El cambio corregido es a las 02:23:03 y el arranque del cliente de HMI a las 02:15:32: un margen de 451 segundos. Desplazar un minuto el ancla del historiador mueve el cambio a las 02:24:03; el orden no cambia. Confirme el desfase con una segunda ancla independiente (por ejemplo, un evento del proceso registrado tanto por el historiador como por un analizador con un reloj conocido, o una segunda consulta NTP).

**EX012 — Plan de preservación.** Orden: registros del cortafuegos y de la VPN (exportación, hash); registros de identidad y del servidor de salto; captura volátil de JH-2 si es seguro; exportación del historiador para la ventana; cuadernos de los operadores; registros de sesiones de Corvane (solicitud contractual inmediata); estado de los controladores solo con aprobación de operaciones y con herramientas del proveedor. Cadena de custodia para cada elemento. Ninguna interacción en línea con los controladores sin el responsable de operaciones.

**EX013 — Redacte el hallazgo.** Observación: cronología corregida con desfases e incertidumbre de ±10 s; cambio atribuido a HMI-JH2 durante la sesión de vendor-svc. Inferencia: el cambio se hizo dentro de esa sesión; la persona es desconocida porque la cuenta es compartida. Confianza: moderada. Consecuencia: suspender la cuenta compartida; exigir cuentas nominativas; pedir a Corvane los registros de sesiones. Frase para el regulador: «Se produjo un cambio inexplicado del punto de consigna de dosificación durante una sesión remota de un proveedor; el punto de consigna se restableció en menos de un minuto; la investigación continúa; no hay evidencia de que saliera de la planta agua no segura».

**EX014 — Evidencia que discrimina.** Un intruso externo predice una IP de origen desconocida y técnicas nuevas: abierta. Un cambio legítimo del proveedor predice un tique y un patrón en otros emplazamientos: contradicho por la ausencia de tique; patrón abierto. Un error local del operador predice una estación local como origen: contradicho para el cambio (HMI-JH2). Una receta automatizada predice un calendario: abierta, compruébese el historiador. Un error de etiquetado predice una discrepancia con el controlador: abierta. El uso indebido de la cuenta compartida predice una sesión sin tique correspondiente: respaldada hasta ahora. Siguiente: registros de sesiones de Corvane y comparación con cuentas nominativas.

**EX015 — Notificación por etapas.** Alerta temprana: el hecho del suceso, el impacto en el servicio (ninguno duradero), investigación abierta. Notificación: cronología corregida, acciones (cuenta suspendida, cuentas nominativas exigidas), preguntas abiertas. Esquema final: causa raíz, correcciones a las declaraciones anteriores, lecciones, riesgo residual. La máxima puntuación nunca afirma pronto un «ataque» ni nombra a una persona.

### Capítulo 4: EX016–EX020

**EX016 — Mejora rural parcial.** Y modificada: Upper Merrow 1,93 horas por hogar y año y 771 horas-hogar vulnerable, mejor que X (2,39; 956) pero mucho peor que la Y original (0,96; 386). Ampliar el laboratorio para que informe de P(alguna interrupción de Upper Merrow > 48 h) da aproximadamente 0,015 con X, 0,001 con la Y original y 0,007 con la Y modificada (semilla 4). La máxima puntuación implementa una comprobación de la duración por evento para Upper Merrow.

**EX017 — Memorando de análisis ético.** Grupos afectados: los hogares de Harbour y Fenley, los hogares de Upper Merrow (incluidos los vulnerables) y el personal. Beneficencia y justicia (Menlo; primacía del bienestar público en ACM/NSPE): X reduce el daño total y cumple el apetito sobre la cola; Y reduce el daño rural concentrado. El consejo debe elegir el juicio de valor; una recomendación combinada (X más medidas rurales no técnicas) es honesta sobre la concentración residual.

**EX018 — Protocolo de obtención.** Magnitud: horas desde «SCADA declarado no disponible en Upper Merrow» hasta «agua tratada fluyendo a la zona según un procedimiento manual documentado». Pida a tres expertos, de forma independiente y tras una pregunta de calibración, los percentiles 5, 50 y 95; discútalos; agréguelos (por ejemplo, la mediana de las medianas con igual peso y las envolventes de los intervalos); registre la persona, la fecha y la justificación.

**EX019 — Declaración de apetito.** Ejemplo: «Merrow Health no aceptará una probabilidad anual superior al 5 % de un desvío del servicio de urgencias relacionado con ciberincidentes que supere 24 horas continuas en cualquier hospital, ni ningún escenario creíble en el que la atención urgente con tiempo crítico no esté disponible en los tres hospitales a la vez». Pruébela con un escenario de *ransomware* que afecte a los sistemas clínicos de dos hospitales.

**EX020 — Dilema de divulgación.** Inmediato: eliminar o cambiar la credencial por defecto en los sistemas de Merrow; bloquear el puerto; monitorizar. Notificación privada a Corvane con evidencia; si Corvane no actúa, recurrir a un proceso de divulgación coordinada (CVD de CISA). Informar al foro de que una clase de herramientas de soporte remoto necesita una revisión de credenciales, sin publicar detalles de explotación. Justificarlo con la beneficencia y la justicia del Informe Menlo y con los deberes profesionales hacia el público.

### Capítulo 5: EX021–EX025

**EX021 — Corrija D2.** Hacer que el historiador sea unidireccional hacia fuera de la zona de control deja a D2 con cuatro rutas y un único punto de estrangulamiento, `jump`. En comparación con D3: D2 sigue dependiendo de saltos con contraseña tras la MFA; D3 añade la aprobación por sesión y la grabación. D3 sigue siendo más fuerte en seguridad; D2 corregida es una clara mejora respecto de D2.

**EX022 — Una arista nueva.** Añadir `internet → eng-ws` con la barrera "vendor cloud account" da a D3 tres rutas y desplaza el punto de estrangulamiento a `eng-ws`, eludiendo el intermediario. Alternativa: exportar los diagnósticos a través del historiador unidireccional a un equipo de la DMZ que el proveedor pueda ver, o un agente del proveedor solo en ese equipo de la DMZ. Riesgo residual: uso indebido del canal saliente; monitorícelo y use una lista de permitidos.

**EX023 — Diseño del acceso de emergencia.** Presencia física con un sobre de credenciales sellado, o una cuenta local de emergencia con alarma y revisada tras cada uso; probado trimestralmente; modelado como una arista con una barrera fuerte y detección. Nunca una contraseña compartida permanente.

**EX024 — Elija con evidencia.** Una tabla de máxima puntuación incluye el compromiso de la TO, el *ransomware*, una caída del proveedor, una caída del intermediario durante una emergencia y un año tranquilo; aplica el VE y el minimax del arrepentimiento; indica un umbral (por ejemplo, una probabilidad de caída del intermediario superior al X % → preferir D2 corregida). Los números pueden variar; lo que puntúa es la estructura.

**EX025 — Registro de decisión de arquitectura.** Contexto: la consecuencia de una dosis no segura. Alternativas con la evidencia de rutas y puntos de estrangulamiento. Decisión (indique la suya). Consecuencias, incluida la dependencia del intermediario. Acceso de emergencia. Evidencia de verificación (capítulo 6). Desencadenante de revisión (por ejemplo, la propuesta de un agente del proveedor).

### Capítulo 6: EX026–EX030

**EX026 — Intervalos y tamaño de muestra.** 19/20 → Wilson [0,76, 0,99]. Éxitos consecutivos para un límite inferior ≥ 0,80: 16. Con un fallo, ensayos para un límite inferior ≥ 0,90: 53. Explicación en lenguaje claro: las muestras pequeñas dejan margen para que la tasa real sea mucho más baja que la observada; los directivos oyen «85 %» y no lo perciben.

**EX027 — Plan de pruebas para la deriva lenta.** Afirmación: «la manipulación de puntos de consigna por deriva lenta se detecta con un límite inferior de Wilson ≥ 0,70». Número de ensayos justificado con un cálculo de intervalos (por ejemplo, al menos 20 ensayos si se esperan pocos fallos). Los escenarios varían la velocidad, la duración, la etiqueta objetivo y el origen, tanto desde la ruta de la HMI como desde la del historiador; los redacta alguien distinto del autor de la regla. Criterio de aprobado o suspenso y decisión en caso de suspenso (no confiar en la regla para esta familia) acordados previamente.

**EX028 — Carga de alarmas.** Unas 0,21 falsas alarmas por turno; unas 234 al año. Alertas verdaderas esperadas: unas 0,43 al año. Proporción de alertas verdaderas: alrededor del 0,2 %. La respuesta debe ser rápida y barata (una lista de comprobación breve, no una investigación completa cada vez), o la regla acabará ignorándose.

**EX029 — Validez del simulacro.** Efecto de la práctica (infla la mejora); efecto de la observación (infla); selección del personal dispuesto (infla); mismo escenario (infla); muestra pequeña (incertidumbre amplia); simulacros solo de día (no captan el desempeño del turno de noche). Cambios de diseño: variar los escenarios, incluir turnos de noche y personal con menos experiencia, muestras más grandes, simulacros sin previo aviso cuando sea seguro.

**EX030 — Reglas de enfrentamiento.** Alcance: dosificación de Fenley, una escritura de 1,80→1,81 mg/L; momento: baja demanda; roles: el responsable de operaciones puede detenerla; condiciones de parada: cualquier cambio inesperado del proceso o alarma inexplicada; verificación independiente de la dosis; analistas de detección a ciegas si el objetivo es la detección a ciegas; gestores de alertas avisados; plan de vuelta atrás; evidencia registrada. Firmadas por operaciones.

### Capítulo 7: EX031–EX035

**EX031 — Repare el RACI.** Concesión de sesiones a proveedores: el responsable de TO rinde cuentas; el ingeniero de TO y el centro de servicios son responsables. Declaración de incidentes: el responsable de guardia rinde cuentas; el CISO es consultado. Cambio de emergencia: mantener al ingeniero de TO como responsable y como quien rinde cuentas solo con una revisión documentada al día siguiente de cada caso (o hacer que el responsable de TO rinda cuentas, con el ingeniero como responsable). La nueva ejecución no muestra hallazgos sin tratar.

**EX032 — Modo común regional.** Caída: ceguera temporal; conservar el registro local y una detección mínima, y ejercitar conjuntamente el estado degradado. Compromiso: el proveedor como vía de ataque; aislar el acceso del proveedor, búsqueda conjunta de amenazas, cláusulas de notificación, plan de salida. Cláusulas contractuales: notificación de incidentes en cuestión de horas, acceso a los registros, derecho de auditoría, asistencia en la salida.

**EX033 — Elija un modelo operativo.** Para el puerto: federado o integrado, con un responsable de seguridad de la TO designado en la organización del capitán de puerto y una línea formal hacia el pequeño equipo del CISO; el modelo central por sí solo corre el riesgo de quedar lejos de una TO gestionada por un contratista. Condiciones de fracaso: el contratista rechaza el modelo; no hay presupuesto para el responsable de TO; el equipo del CISO absorbe la TO sin titularidad de operaciones.

**EX034 — Lo cibernético dentro del mando de emergencias.** Clasificación por impacto en el servicio (pérdida de suministro por zonas, aviso de hervir el agua, etc.) utilizable por el responsable de guardia. El responsable cibernético asesora al director del incidente; ninguna estructura paralela de niveles estratégico y táctico. Notificaciones regionales asignadas (salud, autoridad local, foro, regulador) a roles designados.

**EX035 — Aritmética de la concentración.** HHI = 40² + 40² + 20² = 3.600. Subestima la concentración porque dos operadores de telecomunicaciones comparten una canalización: un 80 % del tráfico comparte un mismo dominio de fallo físico. Represente la concentración por rutas físicas o dominios de fallo, no solo por operadores contractuales.

### Capítulo 8: EX036–EX040

**EX036 — Los pesos cambian el orden.** Con un peso de 20 para el hospital y el generador funcionando, el mejor orden sigue siendo Fenley → Hollin → Harbour → Port con 510.000 (la contribución del hospital sigue siendo cero). Tras el fallo del generador (respaldo de 2 h), el mejor pasa a ser Harbour → Hollin → Fenley → Port con 751.000 horas-persona ponderadas. El peso es un juicio de la gestión de emergencias acordado de antemano, no un juicio técnico.

**EX037 — Estructure una decisión de extorsión.** Opciones: reconstruir desde las copias de seguridad sin pagar; negociar; restablecimiento parcial. Para cada una: calendario (descifrador incierto), seguridad (soluciones manuales para los procesos clínicos), cuestiones jurídicas para los abogados (sanciones, notificación, aseguradora), ética (financiar la delincuencia; datos de pacientes) y evidencia que cambiaría el análisis (pruebas de fiabilidad del descifrador; confirmación de la posesión de los datos). El pago es una decisión de la dirección.

**EX038 — Caída causada por un proveedor.** Inmediato: confirmar que las plantas pueden funcionar en modo manual; poner en pausa el canal de actualizaciones del proveedor; recuperar las HMI en el orden de los emplazamientos con los relojes de respaldo más cortos. Después: anillos de actualización escalonados para los equipos finales de la TO, aceptando una protección más lenta como coste de seguridad de la resiliencia.

**EX039 — Comunicaciones sobre un suceso interno.** Personal: el suceso factual, sin nombres, los cambios de acceso. Corvane: pedir los registros de sesiones conforme al contrato, suspender la cuenta compartida, exigir cuentas nominativas. Foro: consejo de protección para revisar las cuentas compartidas de proveedores, sin acusar a Corvane de mala fe.

**EX040 — Obligaciones en conflicto.** Periodista: el agua volvió a la dosis correcta en menos de un minuto y se verificó; veraz, sin especulaciones. Regulador: notificación completa bajo confidencialidad. Merrow Energy: consejo de protección para revisar las cuentas compartidas de proveedores y la política de cuentas nominativas, sin divulgar el detalle sensible para la policía si los abogados así lo aconsejan. Registre cada decisión; no engañe nunca.

### Capítulo 9: EX041–EX045

**EX041 — Una referencia contaminada.** Referencia de 12 meses: media de 12,75, rango móvil medio ≈ 3,82, límites ≈ [2,59, 22,91]. Diciembre (24) sigue fuera; enero (21) queda ahora dentro. Lección: incluir el periodo sospechoso en la referencia ensancha los límites y puede ocultar un cambio.

**EX042 — Informe al consejo de una página.** Estado del apetito; señal en el tiempo de corrección desde diciembre, con una investigación en curso; cobertura verificada del 39 % con las dos lagunas de mayor peso; evaluación de la regla de detección (adoptarla para algunas familias, no para la deriva lenta); evidencia caducada de las copias de seguridad y del cortafuegos; laguna del RACI en las sesiones de proveedores; decisiones solicitadas con responsables. Ningún recuento de actividad como indicador principal.

**EX043 — Caso de aseguramiento.** Subafirmaciones: personas (dotación de cualquier turno), materiales (existencias de productos químicos), instrumentos (analizadores sin SCADA), duración (72 h). Evidencia: informes de simulacros, registros de existencias, pruebas de los analizadores, cuadrantes de turnos, con su antigüedad y su grado. Refutaciones: turno de noche, pérdida de alimentación de los analizadores, incidente concurrente en Fenley, cada una con una respuesta o un riesgo residual.

**EX044 — Las tres líneas.** Ejemplo: copias de seguridad fuera de línea. Primera línea: operaciones de TO es titular de las restauraciones; segunda línea: seguridad cuestiona la vigencia de la evidencia; tercera línea: la auditoría interna observa una restauración. Confusión de roles: el equipo de seguridad ejecuta actualmente restauraciones que debería ejecutar operaciones.

**EX045 — Capacidad y sucesión.** Capturar la lógica anotada, los procedimientos de prueba y los recorridos grabados. Formar a dos sucesores mediante trabajo en pareja y cambios supervisados durante 18 meses. Evidencia: un cambio dirigido por un sucesor y un simulacro sin el ingeniero que se jubila.

### Capítulo 10: EX046–EX050

**EX046 — Vuelva a leer el folleto.** Véase el §10.9. Mejores resultados: horas de interrupción del servicio; tiempo hasta detectar pruebas inyectadas en una instalación de prueba; verificados frente a operadores de comparación emparejados.

**EX047 — Ficha de evidencia: hospitales vecinos.** Diseño: antes y después en una sola institución durante un ataque cercano. Hallazgos: aumentos significativos de la ocupación de urgencias, de las llegadas de los servicios de emergencias médicas y de medidas relacionadas (cítense del artículo). Limitaciones: un solo emplazamiento, estacionalidad, ninguna región de control no afectada; probablemente inflan el efecto si la estación o sucesos locales contribuyeron. Transferencia: los tres hospitales de Merrow Bay y los servicios de emergencias médicas compartidos; planificar el desvío regional. Acción: hacer un ejercicio de mesa del escenario de desvío con Merrow Health y los servicios de emergencias médicas.

**EX048 — Ficha de evidencia: WannaCry.** Estudio: alrededor de un 6 % menos de ingresos al día en los hospitales infectados; 5,9 millones de libras de actividad perdida estimada; ninguna diferencia detectada en la mortalidad, con la cautela de los autores de que la mortalidad es una medida tosca. NAO: investigación de auditoría del ataque y de la respuesta del NHS. Transferencia: Merrow Health es más pequeña; los efectos de red difieren. Acción: no tomar la «ausencia de diferencia en la mortalidad» como un riesgo clínico bajo; centrarse en medidas de continuidad asistencial.

**EX049 — Del aviso a las preguntas.** Extraiga técnicas del AA24-038A (por ejemplo, el uso de cuentas válidas, los binarios legítimos del propio sistema aprovechados por el atacante, el ataque a entornos operativos; contrástelo con el texto del aviso). Preguntas: ¿mostrarían nuestros registros de identidad un uso anómalo de las cuentas de servicio? ¿Conservaríamos los registros de los equipos pertinentes? Las mitigaciones se relacionan con la MFA, las cuentas nominativas, la conservación de registros y la segmentación.

**EX050 — Comprobación de trampas.** Preguntas: ¿cuál era la tasa base y cómo se definió la exactitud (precisión/exhaustividad)? ¿Estaba el conjunto de prueba separado del de entrenamiento en el tiempo y por entidades? ¿En qué se diferencia el banco de pruebas de nuestra planta? ¿Con qué detector de referencia se comparó? ¿Qué modelo de adversario se supuso? Cada una corresponde a una trampa conocida de Arp et al. (2022).

### Capítulo 11: EX051–EX055

**EX051 — Acta de constitución del proyecto.** Evalúela según los criterios de Planteamiento y Ética del §11.6. Un acta de máxima puntuación para un proyecto en Merrow Bay (o real) tiene un patrocinador designado, un objetivo basado en la consecuencia, una medida y una comparación especificadas de antemano, condiciones de seguridad y exclusiones.

**EX052 — Robustez del resultado de la permutación.** DiD de −5,37 minutos; 462 asignaciones de 5 pilotos entre 11; proporción con DiD ≤ la observada ≈ 0,017. Sigue siendo improbable por azar, pero más débil; la selección del emplazamiento que más mejoró inflaba la estimación original.

**EX053 — Plan de partes interesadas y de adopción.** Partes interesadas: los operadores (incluidos los de noche), los ingenieros de TO, Corvane, el CISO, el patrocinador del consejo. Pérdidas: tiempo, autonomía. Formación: práctica supervisada, no diapositivas. Historias de pre mortem: el turno de noche ignora el manual; el contratista nunca recibe formación; el simulacro se cancela por «presión operativa»; cada una con sus mitigaciones.

**EX054 — Limitaciones con su sentido.** Selección de pilotos con sistemas antiguos (puede inflar si tenían más margen de mejora); regresión a la media (infla); efectos de la práctica (inflan); muestra pequeña (incertidumbre amplia); simulacros ≠ sucesos reales (sentido incierto); contaminación si los emplazamientos de comparación oyeron hablar del manual (reduce). Fase posterior: despliegue escalonado comprobando las tendencias previas.

**EX055 — Traspaso y beneficios.** Titulares: operaciones de TO para los simulacros, el especialista para el caso de aseguramiento. Afirmación: «las plantas piloto pueden lograr una operación manual estable en X minutos». Evidencia: informes trimestrales de simulacros, antigüedad máxima de 365 días. Indicador: mediana del tiempo de los simulacros, referencia XmR de los ocho primeros trimestres. Desencadenante: un simulacro que supere el límite superior, o un cambio de personal en un emplazamiento piloto.

### Capítulo 12: EX056–EX060

**EX056 — El punto de inversión de la salud.** Barrido: P1 supera a P2 cuando el peso de la continuidad llega a aproximadamente 0,32. Álgebra: sean las puntuaciones P1 = (9,7,6,4) y P2 = (6,6,7,8); con los pesos (c, 0,30/0,75·(1−c), 0,15/0,75·(1−c), 0,30/0,75·(1−c)), la diferencia P1−P2 = 0 en c ≈ 0,318. La dirección debería debatir cuánto pesa más la continuidad que la privacidad en los servicios clínicos.

**EX057 — Lista de comprobación de la transferencia.** Diferencias del puerto: tiempo hasta el daño más lento; TO gestionada por un contratista; regímenes distintos; concentración en Halden Cloud y Lumen Watch; consecuencias comerciales. La mitad dedicada a la operación manual puede importar menos que la resiliencia de la identidad y de la nube; vuelva a obtener los escenarios, las probabilidades y los pesos con el capitán de puerto y el contratista.

**EX058 — Autoevaluación con evidencia.** La máxima puntuación exige artefactos capítulo a capítulo con sus puntuaciones en las rúbricas, tres debilidades concretas y un plan a 12 meses basado en la práctica con evidencia del progreso (por ejemplo, «dirigir dos simulacros; redactar tres registros de decisión revisados por un colega»).

**EX059 — Caso integrador.** Evalúe de 0 a 3 cada una de las ocho partes del ejercicio (máximo 24). Una respuesta sólida plantea las decisiones inmediatas (¿suspender el acceso de Corvane?, ¿notificar?) y las estratégicas (rediseñar el acceso de los proveedores); planifica la evidencia en los tres operadores; fija los pesos del restablecimiento con el foro; propone un acceso similar a D3 con evaluación; repara la titularidad y aborda la concentración en Corvane; comunica sin engaños; lee con sentido crítico las declaraciones de Corvane; y propone un proyecto de continuación con DiD o un diseño equivalente. La incertidumbre y los juicios de valor son explícitos en todo momento.

**EX060 — Práctica continuada y desencadenantes de revisión.** Fuentes volátiles: la transposición nacional de NIS2 y sus orientaciones; las revisiones de NERC CIP; las actualizaciones de la NIST SP 800-82 y del CSF; los CPG y el KEV de CISA; las orientaciones sectoriales (HPH CPGs, sector del agua). Vigilancia: listas de correo de los estándares, páginas de los reguladores, suscripciones a avisos. Desencadenantes: un aviso nuevo que afecte a los productos de acceso remoto; un incidente en una organización similar; un cambio en la concentración de proveedores. Registre los cambios como actualizaciones fechadas de los registros de decisiones.

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
