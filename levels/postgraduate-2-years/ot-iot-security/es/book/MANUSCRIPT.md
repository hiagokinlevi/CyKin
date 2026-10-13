# Seguridad de TO, IoT y sistemas ciberfísicos: práctica y liderazgo de posgrado

- Idioma: español neutro (`es`); curso de posgrado, dos años a tiempo parcial; aproximadamente 600 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–12 de 12 tienen texto didáctico escrito a mano; los ejercicios EX001–EX060 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no equivale a un libro terminado.
- Público: profesionales con experiencia que lideran decisiones de seguridad de TO, IoT y sistemas ciberfísicos a escala de toda la organización.
- Relación con los libros vecinos: el [libro de grado](../../../../bachelors-4-years/ot-iot-security/es/book/MANUSCRIPT.md) construye los fundamentos; el [libro de maestría](../../../../masters-2-years/ot-iot-security/es/book/MANUSCRIPT.md) enseña el ciclo de investigación. **Este libro está guiado por la práctica**: decidir, evaluar, integrar y asegurar.
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado. No concede autorización para acceder a plantas reales. Todas las organizaciones, personas y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Cada capítulo tiene resultados de aprendizaje, secciones didácticas, un ejemplo resuelto, un caso sintético etiquetado, errores y límites, cinco ejercicios puntuados de 0 a 3, una síntesis y un bloque **Siga estudiando**. Los laboratorios (capítulos 1, 4, 6 y 9) se ejecutan sin conexión con `python3 file.py` sobre datos sintéticos con semilla fija.

### Caso de estudio sintético

| Elemento | Función | Límite |
|---|---|---|
| **Bayside Water Reclamation Plant (BWRP)** — controlador de dosificación PLC-D, SCADA, historiador, 23 estaciones de bombeo con RTU celulares, acceso remoto de proveedores | Organización estudiada a lo largo del libro | Inventada |
| **Daniel Osei** | Responsable de seguridad de TO, que reporta al director de la planta | Inventado |

### Fuentes principales

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [serie ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); [avisos de ciberseguridad](https://www.cisa.gov/news-events/cybersecurity-advisories) de CISA; Giraldo et al. 2018; Urbina et al. 2016. Lista completa en [Referencias](#references).

## Contenido

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](../../en/book/MANUSCRIPT.md#ch-07) · [8](../../en/book/MANUSCRIPT.md#ch-08) · [9](../../en/book/MANUSCRIPT.md#ch-09) · [10](../../en/book/MANUSCRIPT.md#ch-10) · [11](../../en/book/MANUSCRIPT.md#ch-11) · [12](../../en/book/MANUSCRIPT.md#ch-12) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Toma de decisiones avanzada en seguridad

### Resultados de aprendizaje

Usted será capaz de (1) plantear una decisión de seguridad de TO con opciones, criterios, incertidumbre y un responsable de la decisión; (2) comparar opciones por pérdida esperada y por peor caso creíble a la vez; (3) registrar una decisión de modo que pueda auditarse más adelante; y (4) reconocer cuándo conviene aplazar una decisión para reunir información.

### 1.1 Decisiones, no hallazgos

En el nivel de posgrado, el entregable rara vez es una lista de vulnerabilidades; es una decisión que alguien con presupuesto y responsabilidad debe tomar. En la planta sintética Bayside Water Reclamation Plant (BWRP), el responsable de seguridad de TO, Daniel Osei, debe decidir cómo acceden los proveedores al controlador de dosificación química PLC-D. Un marco de decisión nombra al responsable (el director de la planta), las opciones, los criterios, lo que es incierto y la fecha en la que debe tomarse la decisión.

Para la decisión sobre el acceso de proveedores, el marco también necesita el plazo que la fuerza, como el vencimiento del contrato de VPN actual, y las personas a las que hay que consultar: operación, el gestor de proveedores e ingeniería. Escribir el marco antes del análisis evita que Daniel elija los criterios después de saber qué opción favorecen.

### 1.2 La pérdida esperada es necesaria pero no suficiente

La pérdida anual esperada (probabilidad por pérdida, sumada sobre los escenarios) permite comparar en una sola escala opciones con costes distintos. Pero los servicios públicos no son neutrales al riesgo: un evento raro que contamine el vertido a una bahía, desencadene una actuación regulatoria y erosione la confianza pública puede ser inaceptable con cualquier probabilidad por encima de un umbral. Por eso los líderes informan de la pérdida esperada junto con el peor caso creíble y cualquier restricción regulatoria o de seguridad funcional que sea vinculante con independencia de la aritmética.

```python
"""Lab 01: compare three synthetic BWRP options by expected annual loss and worst credible case."""
options = {  # name: (annual cost, [(probability per year, loss if it happens)])
    "A keep vendor VPN":        (10_000, [(0.10, 400_000), (0.02, 2_500_000)]),
    "B brokered sessions":      (35_000, [(0.03, 400_000), (0.005, 2_500_000)]),
    "C no remote access":       (90_000, [(0.01, 400_000), (0.004, 2_500_000)]),
}
for name, (cost, events) in options.items():
    eal = sum(p * l for p, l in events)
    worst = max(l for _, l in events)
    print(f"{name:20} cost={cost:>7,} expected_loss={eal:>9,.0f} total={cost+eal:>9,.0f} worst_case={worst:,}")
```

Ejecútelo con `python3 lab_decide.py`. Salida verificada:

```text
A keep vendor VPN    cost= 10,000 expected_loss=   90,000 total=  100,000 worst_case=2,500,000
B brokered sessions  cost= 35,000 expected_loss=   24,500 total=   59,500 worst_case=2,500,000
C no remote access   cost= 90,000 expected_loss=   14,000 total=  104,000 worst_case=2,500,000
```

### 1.3 Cómo leer la comparación

La opción B tiene el total más bajo (59.500) porque su coste de control compra una gran reducción de la probabilidad de incidente. La opción C elimina más riesgo, pero con estas estimaciones cuesta más de lo que ahorra. Las tres comparten el mismo peor caso porque el escenario catastrófico sigue siendo posible por otras rutas; ninguna elección de acceso remoto lo elimina. Esa observación lleva al líder a buscar salvaguardas independientes, no más gasto en acceso remoto. Los números también muestran lo sensible que es la clasificación. La opción A pierde por sus probabilidades de incidente; si ambas estimaciones se redujeran a la mitad, el total de A bajaría a 55.000 y superaría a los 59.500 de B. Por eso el registro de Daniel nombra un disparador de revisión ligado a la estimación de incidentes, y por eso la siguiente pregunta es qué solidez tienen realmente esas probabilidades.

### 1.4 Valor de la información

Si las estimaciones de probabilidad se discuten (y para los ataques dirigidos siempre se discuten), pregúntese si la decisión cambiaría al moverlas dentro de su rango plausible. Si B gana en todo ese rango, decida ahora. Si la clasificación se invierte, un estudio breve (revisión de registros de proveedores, un ejercicio de mesa) puede valer más que una compra inmediata. Para BWRP, la pregunta es si B sigue ganando cuando la probabilidad de incidente de proveedor de la opción A es menor que la estimada. Daniel puede comprobarlo en el laboratorio cambiando un número cada vez y anotando dónde se invierte la clasificación. Si la inversión exige una estimación fuera de lo que informan otras organizaciones del sector, la decisión se mantiene; si no, dos semanas de revisión de los registros de proveedores pueden ser el mejor primer gasto.

### Ejemplo resuelto (BWRP sintética)

Registro de decisión de Daniel: «D-2026-14. Responsable: director de la planta. Decisión: adoptar sesiones de proveedor intermediadas (B). Fundamento: menor coste esperado total con las estimaciones del anexo 1; el peor caso es igual en todas las opciones, así que una acción separada (D-2026-15) revisa el enclavamiento de límite alto de dosificación. Revisar si la estimación de frecuencia de incidentes de proveedor supera 0,06 al año o tras cualquier incidente de acceso remoto».

> **Caso sintético — Bayside Water Reclamation Plant.** BWRP, Daniel Osei y todos los costes y probabilidades son inventados.

### Errores y límites

Las estimaciones puntuales de probabilidades adversarias transmiten una precisión falsa; presente rangos. La aritmética de la pérdida esperada no recoge el daño a las personas aguas abajo, que debe argumentarse por separado.

### Ejercicios — capítulo 1

- **EX001 — Coste total de la opción A con una probabilidad menor.** Si el escenario de 400.000 de A baja a 0,05 al año, recalcule el total de A. *Rúbrica:* 3 = 10.000 + 20.000 + 50.000 = 80.000, todavía por encima de B; 2 = solo el número; 1 = error aritmético; 0 = nada.
- **EX002 — Por qué el peor caso es idéntico.** Explique qué implica para el líder el peor caso compartido de 2,5 millones. *Rúbrica:* 3 = la elección de acceso remoto no elimina la ruta catastrófica; invertir en una salvaguarda independiente; 2 = parcial; 1 = «todas iguales»; 0 = nada.
- **EX003 — Redactar un disparador de revisión.** Añada un disparador de revisión más a D-2026-14. *Rúbrica:* 3 = disparador observable y específico; 2 = vago pero pertinente; 1 = «si las cosas cambian»; 0 = nada.
- **EX004 — ¿Se invierte la clasificación?** Halle la probabilidad del escenario de 400.000 de B con la que el total de B iguala los 100.000 de A. *Rúbrica:* 3 = (100.000 − 35.000 − 12.500)/400.000 ≈ 0,131; 2 = método; 1 = ignora el otro término; 0 = nada.
- **EX005 — Cuándo no decidir todavía.** Describa una situación en la que Daniel debería aplazar D-2026-14 para reunir información. *Rúbrica:* 3 = la clasificación se invierte dentro del rango plausible y un estudio barato puede acotarlo antes del plazo; 2 = parcial; 1 = «cuando haya dudas»; 0 = nada.

### Síntesis del capítulo

Los líderes deciden con la pérdida esperada, el peor caso creíble, responsables explícitos y disparadores de revisión, y compran información cuando esta podría cambiar la elección.

### Siga estudiando — capítulo 01 de 12

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Seguridad de TO, IoT y sistemas ciberfísicos: práctica actual

### Resultados de aprendizaje

Usted será capaz de (1) comparar el programa de seguridad de TO de una organización con los temas de NIST SP 800-82r3 e IEC 62443-2-1; (2) distinguir la práctica documentada de la práctica realizada; (3) elaborar una lista de brechas con evidencia; y (4) priorizar las brechas para la dirección.

### 2.1 Qué espera la orientación actual

NIST SP 800-82r3 organiza un programa de seguridad de TO en torno a la gobernanza, la gestión de riesgos, la arquitectura y las capacidades de seguridad aplicadas a los sistemas de TO, y relaciona las consideraciones de TO con las funciones del NIST Cybersecurity Framework. IEC 62443-2-1 especifica requisitos para el programa de seguridad de un propietario de activos. Ninguno de los dos es una lista de casillas por marcar; ambos describen capacidades que un programa maduro demuestra. En una revisión, use cada documento para generar preguntas y no una puntuación. En BWRP eso significa preguntar, por ejemplo, cómo se gobierna el acceso remoto, cómo se inventarían los activos y cómo se gestionarían los incidentes en el sistema de dosificación. Las respuestas pasan después a la lista de brechas con su evidencia, de modo que la revisión informa de lo que la planta puede demostrar y no de cuántas cláusulas afirma cumplir.

### 2.2 Documentado frente a realizado

Una política que dice «el acceso remoto se revisa mensualmente» es práctica documentada. Un registro que muestra las tres últimas revisiones mensuales, con los hallazgos cerrados, es práctica realizada. Los evaluadores de posgrado buscan lo segundo. En BWRP, Daniel muestrea evidencia de cada práctica declarada en lugar de aceptar las respuestas de las entrevistas. La muestra tiene que elegirse antes de mirar, o deriva hacia los casos que quedan bien. Daniel elige cinco prácticas situadas en rutas hacia consecuencias y pide, para cada una, el artefacto más reciente que demuestre que se hizo. Una respuesta de entrevista puede señalar la evidencia, pero nunca la sustituye en la lista de brechas.

### 2.3 Construir la lista de brechas

Para cada capacidad: lo que espera la orientación, lo que BWRP documenta, lo que la evidencia muestra que se realiza, la brecha, la consecuencia de la brecha y un responsable propuesto. Las estaciones de bombeo remotas conectadas mediante RTU celulares son un punto ciego habitual: aparecen en el registro de activos como «estaciones de bombeo», pero no como puntos finales de red. Cada fila debe ser lo bastante específica como para que su responsable pueda actuar. Para la brecha de inventario de BWRP, eso significa nombrar las nueve RTU de estaciones de bombeo que aún no figuran, la consecuencia de que no pueden supervisarse ni parchearse, y la persona que las añadirá. Una fila que solo dice «inventario incompleto» no da una tarea a nadie.

### 2.4 Priorizar

Priorice las brechas situadas en rutas hacia consecuencias (dosificación, calidad del vertido) y las que son baratas de cerrar. La falta de inventario de las RTU celulares bloquea varias otras capacidades (supervisión, aplicación de parches, delimitación del alcance de incidentes), así que ocupa un puesto alto aunque sea «solo documentación». Escriba la clasificación con su motivo, para que el director de la planta vea por qué una tarea de inventario supera a una herramienta nueva. En BWRP, la revisión del acceso remoto va a continuación, porque no se realiza desde marzo y los proveedores pueden llegar a PLC-D. Después viene la prueba de restauración de la lógica del PLC, ya que unas copias de seguridad cuya restauración nunca se ha probado pueden fallar cuando se necesiten.

### Ejemplo resuelto (BWRP sintética)

Muestra de cinco prácticas de Daniel: inventario de activos (documentado, realizado en parte: 14 de 23 RTU de estaciones de bombeo registradas); revisión del acceso remoto (documentada, no realizada desde marzo); copia de seguridad de la lógica del PLC (realizada, restauración nunca probada); plan de respuesta a incidentes (documentado, sin guía de actuación específica de TO); aplicación de parches (realizada en las HMI Windows, no en el firmware de las RTU).

> **Caso sintético — Bayside Water Reclamation Plant.** Los recuentos y las fechas son inventados.

### Errores y límites

Una comparación con un solo documento puede pasar por alto la regulación sectorial. Muestrear cinco prácticas da una visión, no una opinión de auditoría.

### Ejercicios — capítulo 2

- **EX006 — Clasificar una práctica declarada.** Se afirma «probamos las restauraciones anualmente», pero no existe ningún registro. ¿Documentada o realizada? *Rúbrica:* 3 = solo documentada; pedir evidencia; 2 = solo la etiqueta; 1 = realizada; 0 = nada.
- **EX007 — Clasificar la brecha de inventario de RTU.** Justifique por qué la brecha de inventario de RTU está por encima de la guía de actuación que falta. *Rúbrica:* 3 = bloquea la supervisión, los parches y la delimitación del alcance; habilitadora; 2 = parcial; 1 = «más importante»; 0 = nada.
- **EX008 — Una fila de la lista de brechas.** Escriba la fila completa de la lista de brechas para «restauración nunca probada». *Rúbrica:* 3 = expectativa, documentado, realizado, brecha, consecuencia, responsable; 2 = cuatro campos; 1 = solo la brecha; 0 = nada.
- **EX009 — Elegir el documento de referencia.** ¿Cuándo sería IEC 62443-2-1 una mejor referencia que SP 800-82r3 para BWRP? *Rúbrica:* 3 = cuando se aplican requisitos de certificación o contractuales sobre el programa del propietario de activos; 2 = parcial; 1 = «es mejor»; 0 = nada.
- **EX010 — Cobertura de la muestra.** ¿Qué se puede y qué no se puede concluir de muestrear cinco prácticas? *Rúbrica:* 3 = brechas indicativas; no es una opinión de aseguramiento completa; sesgo de muestreo; 2 = un solo lado; 1 = afirma de más; 0 = nada.

### Síntesis del capítulo

Las revisiones de la práctica actual comparan la evidencia de lo que se hace, no de lo que está escrito, y clasifican las brechas por su efecto en las consecuencias y en otras capacidades.

### Siga estudiando — capítulo 02 de 12

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Seguridad de TO, IoT y sistemas ciberfísicos: evidencia especializada

### Resultados de aprendizaje

Usted será capaz de (1) valorar la calidad de las fuentes de evidencia de seguridad de TO; (2) conciliar evidencia contradictoria procedente de datos de red, de equipos y de proceso; (3) evaluar con sentido crítico las afirmaciones de proveedores y avisos; y (4) redactar una valoración de la evidencia que indique niveles de confianza.

### 3.1 Fuentes y sus puntos ciegos

Las capturas pasivas de red muestran quién habló con quién, pero no ven los enlaces serie ni el significado de las cargas útiles cifradas. Los registros de eventos del controlador, cuando existen, muestran los cambios de programa, pero a menudo se sobrescriben tras unos cientos de entradas. Los datos de proceso del historiador muestran el efecto físico, pero no la causa. Los registros de auditoría de la HMI muestran las acciones del operador, pero no las sesiones de la herramienta de ingeniería. El trabajo con evidencia especializada las combina porque a cada una se le escapa algo.

Antes de confiar en cualquier fuente, escriba qué puede y qué no puede ver en BWRP. La captura cubre la red de la planta, pero no a un técnico ante el panel de dosificación. El registro de eventos de PLC-D puede haberse sobrescrito desde el evento. El historiador registra el punto de consigna, pero no quién lo cambió. Esa lista le dice a Daniel qué segunda fuente consultar para cada pregunta.

### 3.2 Los conflictos son información

Si el historiador muestra un cambio del punto de consigna de dosificación a las 14:02, pero ni el registro de auditoría de la HMI ni la captura de red muestran una escritura, las posibilidades son una captura incompleta, un desfase de reloj, un cambio local en el panel o una lógica que cambia el punto de consigna internamente. Cada hipótesis predice algo comprobable: los registros del interruptor de llave del panel, una comparación del programa del PLC, los contadores de pérdida de paquetes de la captura.

Escriba cada hipótesis con la comprobación que la descartaría y haga primero las comprobaciones más baratas. Un desfase de reloj puede probarse en minutos comparando las marcas de tiempo de un evento conocido en varios sistemas. Registre el resultado de cada comprobación, incluidas las que solo eliminan una posibilidad, porque son las que hacen creíble la conclusión final.

### 3.3 Valorar afirmaciones externas

Los avisos ICS de CISA describen los productos y versiones afectados, las puntuaciones CVSS y las mitigaciones coordinadas con los proveedores; son una evidencia sólida de la existencia de una vulnerabilidad y más débil de si es explotable en su configuración. Las declaraciones de un proveedor de que un producto «no está afectado» merecen que se le pida el razonamiento. Los estudios de medición revisados por pares, como el análisis de Mirai de Antonakakis et al. (USENIX Security 2017), incluyen secciones de método que usted puede evaluar.

Para BWRP, un aviso que afecte a un producto usado en PLC-D debería llevar a dos preguntas: si la versión afectada está instalada y si la función vulnerable es alcanzable desde donde podría estar un atacante. Registre las respuestas junto al aviso en el inventario. Cuando un proveedor diga que no está afectado, archive su razonamiento con la fecha, para poder comprobar la afirmación más adelante.

### 3.4 Declaraciones de confianza

Declare la confianza de forma explícita: alta (varias fuentes independientes coinciden), moderada (una fuente sólida, sin contradicción), baja (inferencia a partir de datos indirectos). Los líderes actúan de manera distinta en cada caso. Asigne el nivel a cada conclusión, no al informe en su conjunto, y diga qué fuentes la respaldan. El hallazgo de las 14:02 de Daniel tiene confianza alta porque la captura, la comparación del programa y el registro del interruptor de llave coinciden. Una conclusión basada solo en el registro del interruptor de llave sería moderada, y una conjetura sobre quién estaba en la planta, antes de comprobar los cuadrantes de turnos, sería baja.

### Ejemplo resuelto (BWRP sintética)

A las 14:02, el historiador muestra que el punto de consigna de dosificación de hipoclorito en PLC-D pasa de 4,0 a 6,5 mg/L. No hay entrada de auditoría en la HMI ni escritura Modbus en la captura. Daniel comprueba: los contadores de pérdida de la captura muestran 0 paquetes descartados; la comparación del programa del PLC muestra un programa sin cambios; el registro del interruptor de llave del panel local muestra «modo local 14:01–14:05». Valoración: confianza alta en que el cambio se hizo localmente en el panel; siguiente paso, identificar quién estaba en la planta.

> **Caso sintético — Bayside Water Reclamation Plant.** Las horas, etiquetas y valores son inventados.

### Errores y límites

La ausencia de evidencia en una captura solo tiene significado si se conocen la cobertura y la pérdida de la captura. Un intruso capaz puede alterar los registros.

### Ejercicios — capítulo 3

- **EX011 — Predicciones a partir de hipótesis.** Para la hipótesis «desfase de reloj», indique qué evidencia la confirmaría. *Rúbrica:* 3 = escritura correspondiente encontrada en la captura o en el registro de la HMI en la hora desplazada, con el desfase medido; 2 = parcial; 1 = vago; 0 = nada.
- **EX012 — Confianza con evidencia de una sola fuente.** La única evidencia de un inicio de sesión remoto es una línea del registro de la VPN. ¿Qué confianza y por qué? *Rúbrica:* 3 = moderada como mucho, una sola fuente, podría estar alterada o mal atribuida; 2 = solo el nivel; 1 = alta; 0 = nada.
- **EX013 — Interpretar una afirmación de «no afectado».** Un proveedor dice que su RTU no está afectada por el fallo de biblioteca de un aviso. ¿Qué pregunta usted? *Rúbrica:* 3 = qué versión/componente, por qué no es alcanzable, evidencia (SBOM, análisis); 2 = una; 1 = aceptarlo; 0 = nada.
- **EX014 — Qué demuestran los contadores de pérdida de la captura.** ¿Por qué comprobó Daniel los contadores de pérdida de paquetes antes de confiar en «no se ve ninguna escritura»? *Rúbrica:* 3 = la ausencia solo tiene significado si la captura está completa; 2 = parcial; 1 = vago; 0 = nada.
- **EX015 — Punto ciego de los datos de proceso.** Nombre una cosa que el historiador nunca puede decirle sobre el cambio de las 14:02. *Rúbrica:* 3 = quién o qué lo inició (causa/identidad); 2 = vago; 1 = incorrecto; 0 = nada.

### Síntesis del capítulo

El trabajo con evidencia especializada triangula fuentes con puntos ciegos conocidos, trata los conflictos como hipótesis que hay que probar y asigna una confianza a cada conclusión.

### Siga estudiando — capítulo 03 de 12

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Riesgo y ética avanzados

### Resultados de aprendizaje

Usted será capaz de (1) modelar distribuciones de pérdidas en lugar de cifras únicas; (2) leer las pérdidas media, del percentil 95 y del percentil 99 de una simulación con semilla fija; (3) decidir quién soporta el riesgo residual y si ha dado su consentimiento; y (4) gestionar la tensión ética entre transparencia y seguridad en un servicio público.

### 4.1 Distribuciones en lugar de estimaciones puntuales

La pérdida anual por interrupciones de TO es casi siempre cero y, de vez en cuando, grande. Una simulación de Monte Carlo sortea, muchos miles de veces, si ocurre un incidente y cuánto dura, y produce una distribución cuya cola es lo que interesa a los consejos de administración y a las aseguradoras.

```python
"""Lab 04: Monte Carlo of annual outage loss for BWRP with and without a control (seeded, synthetic)."""
import random, statistics
def year(rnd, p_incident, hours_lo, hours_hi, cost_per_hour=12_000):
    if rnd.random() >= p_incident: return 0.0
    return rnd.uniform(hours_lo, hours_hi) * cost_per_hour
for label, p, lo, hi in [("baseline", 0.15, 4, 72), ("with segmentation", 0.06, 4, 48)]:
    rnd = random.Random(2026)
    losses = sorted(year(rnd, p, lo, hi) for _ in range(20_000))
    print(f"{label:18} mean={statistics.mean(losses):>8,.0f} p95={losses[int(0.95*len(losses))]:>9,.0f} p99={losses[int(0.99*len(losses))]:>9,.0f} P(loss>0)={sum(l>0 for l in losses)/len(losses):.3f}")
```

Ejecútelo con `python3 lab_mc.py`. Salida verificada:

```text
baseline           mean=  68,613 p95=  592,662 p99=  814,425 P(loss>0)=0.151
with segmentation  mean=  18,590 p95=  129,339 p99=  493,624 P(loss>0)=0.059
```

La simulación solo necesita unas pocas entradas: la probabilidad de que ocurra un incidente en un año, cuánto dura y cuánto cuesta cada hora. Cada una debe acompañarse de su fuente y de un rango plausible. El laboratorio 4 usa una semilla fija para que el consejo vea los mismos números cuando se repite la ejecución, y para que un cambio en el resultado pueda atribuirse a un cambio en las hipótesis.

### 4.2 Cómo leer la cola

La segmentación reduce la pérdida media de unos 68.600 a 18.600, y la probabilidad de cualquier pérdida del 15,1 % al 5,9 %. El percentil 99 baja de forma menos marcada (de 814.000 a 494.000) porque, cuando un incidente sí ocurre, todavía puede durar dos días. Si la tolerancia del consejo es «no más de un 1 % de probabilidad de perder más de 600.000 en un año», con estas hipótesis solo el diseño segmentado la cumple. Estas cifras dependen de hipótesis que merecen su propia línea en la diapositiva: las probabilidades de incidente, los rangos de duración y un único coste por hora. Cambiar la duración máxima del diseño segmentado de 48 a 72 horas elevaría su cola. El consejo debería ver qué hipótesis determina el resultado de la tolerancia antes de dar por cumplido el umbral de 600.000.

### 4.3 Quién soporta el riesgo

En una planta de regeneración de aguas, el riesgo residual no lo soporta solo la empresa de servicios. Los residentes cercanos a los puntos de vertido y el ecosistema de la bahía soportan el riesgo de calidad del vertido; los abonados soportan el riesgo de costes. Desde el punto de vista ético, un líder debería identificar a estas partes, preguntar si el regulador o el órgano electo ha aceptado el riesgo en su nombre y evitar aceptar en nombre de otros lo que la organización no tiene mandato para aceptar.

En BWRP, el acta del consejo lo hizo explícito al dejar constancia de que el riesgo de calidad del vertido para los residentes se rige por las condiciones de la autorización del regulador. El papel de Daniel es hacer visibles a las partes afectadas en el registro de riesgos e indicar quién ha aceptado el riesgo en su nombre. Cuando nadie tiene ese mandato, el riesgo se escala en lugar de aceptarse en silencio.

### 4.4 Transparencia frente a exposición

Publicar una evaluación de seguridad detallada genera confianza pública, pero puede dar un mapa a los atacantes. Una práctica defendible es la divulgación por capas: publicar la gobernanza, las decisiones de aceptación de riesgos y las métricas de avance; compartir el detalle técnico con los reguladores y los organismos sectoriales de intercambio de información bajo confidencialidad; y divulgar los incidentes según el deber legal y con prontitud a las personas afectadas. Para BWRP, eso podría significar publicar la decisión de adoptar sesiones de proveedor intermediadas y las cifras de avance de la segmentación, mientras que el diseño de la red de las estaciones de bombeo se comparte solo con el regulador y con el grupo sectorial de intercambio. La decisión sobre qué va a cada sitio debe registrarse y revisarse, para que las solicitudes posteriores de periodistas o residentes reciban una respuesta coherente.

### Ejemplo resuelto (BWRP sintética)

Daniel presenta la simulación con sus hipótesis en una sola diapositiva: probabilidad anual de incidente de referencia del 15 % (de organizaciones del sector, rango 8–25 %), duración uniforme de 4–72 horas, coste de 12.000 por hora, semilla 2026. El consejo acepta la segmentación y hace constar en el acta que el riesgo de calidad del vertido para los residentes está cubierto por las condiciones de la autorización del regulador, y no solo por el apetito de riesgo del consejo.

> **Caso sintético — Bayside Water Reclamation Plant.** Todos los parámetros de la simulación son inventados.

### Errores y límites

Las duraciones uniformes son una simplificación; las distribuciones de cola pesada elevarían el percentil 99. Una simulación con semilla fija es reproducible, no correcta.

### Ejercicios — capítulo 4

- **EX016 — Interpretar el cambio de p99.** Explique por qué, con la segmentación, p99 baja proporcionalmente menos que la media. *Rúbrica:* 3 = la segmentación reduce sobre todo la probabilidad de incidente; la cola condicional de la duración sigue siendo larga; 2 = parcial; 1 = vago; 0 = nada.
- **EX017 — Comprobar una tolerancia.** ¿Cumple la situación de referencia «P(pérdida > 600.000) ≤ 1 %»? Use la salida. *Rúbrica:* 3 = no, p99 = 814.425 > 600.000, así que más del 1 % la supera; 2 = solo la conclusión; 1 = sí; 0 = nada.
- **EX018 — Nombrar a las partes afectadas.** Enumere tres partes, además de la empresa de servicios, que soportan el riesgo residual de TO de BWRP. *Rúbrica:* 3 = tres partes pertinentes; 2 = dos; 1 = una; 0 = nada.
- **EX019 — Un plan de divulgación por capas.** Asigne cada elemento a público, solo regulador o interno: (a) declaración de apetito de riesgo, (b) conjunto de reglas del cortafuegos, (c) recuento anual de incidentes de TO. *Rúbrica:* 3 = público, interno (o regulador), público; 2 = dos; 1 = uno; 0 = nada.
- **EX020 — Sensibilidad al modelo de duración.** Prediga cómo cambian la media y p99 al sustituir la duración uniforme de 4–72 h por una distribución de cola más pesada. *Rúbrica:* 3 = p99 sube más que la media; determinado por la cola; 2 = solo la dirección; 1 = sin cambio; 0 = nada.

### Síntesis del capítulo

El trabajo avanzado de riesgos informa de distribuciones y colas, nombra a quién soporta el riesgo residual y equilibra de forma deliberada la transparencia y la exposición.

### Siga estudiando — capítulo 04 de 12

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Seguridad de TO, IoT y sistemas ciberfísicos: alternativas de diseño

### Resultados de aprendizaje

Usted será capaz de (1) generar alternativas de diseño realmente distintas para proteger estaciones de bombeo remotas; (2) evaluarlas con criterios operativos, de seguridad y de ciclo de vida; (3) usar los conceptos de zona y conducto de IEC 62443 para describir cada una; y (4) documentar por qué se rechazaron las alternativas rechazadas.

### 5.1 El problema

Las 23 estaciones de bombeo de BWRP impulsan las aguas residuales hasta la planta. Cada una tiene una RTU con un módem celular que informa de los niveles y del estado de las bombas al SCADA y acepta órdenes de arranque y parada. Algunos módems tienen direcciones IP públicas, lo que los sitúa en la categoría de exposición que ATT&CK for ICS denomina T0883 *Internet Accessible Device*. Lo que más importa son las órdenes. Una lectura de nivel falsa podría ocultar un desbordamiento, pero una parada remota enviada a una bomba durante una tormenta podría provocarlo. Por eso cualquier diseño tiene que responder a dos preguntas: quién puede llegar a las RTU y si las órdenes remotas son necesarias en absoluto. Las respuestas difieren según la estación, y por eso las alternativas se comparan estación por estación.

### 5.2 Tres alternativas

Alternativa 1, APN privado: el operador de telecomunicaciones proporciona un nombre de punto de acceso privado para que los módems no tengan direcciones públicas; el tráfico llega a BWRP a través de un túnel gestionado por el operador. Alternativa 2, VPN en el lado de la RTU: cada RTU (o un pequeño router junto a ella) establece un túnel IPsec con un concentrador de BWRP en la DMZ. Alternativa 3, enlace de solo supervisión con control local: se eliminan las órdenes remotas; las RTU ejecutan el control local de nivel y solo informan, y los operadores envían cuadrillas ante las excepciones.

Cada alternativa cambia una cosa distinta. La primera elimina las direcciones públicas, pero mantiene la confianza en el operador. La segunda añade el cifrado y la autenticación propios de BWRP a costa de más equipos. La tercera elimina la capacidad más arriesgada, las órdenes remotas, y acepta una respuesta más lenta. Son realmente distintas, y eso es lo que hace útil compararlas.

### 5.3 Evaluarlas

La alternativa 1 es rápida y barata, pero confía en el aislamiento del operador. La alternativa 2 da a BWRP su propia frontera criptográfica, pero añade 23 dispositivos que parchear y certificados que gestionar. La alternativa 3 es la que más reduce la superficie de ataque (sin órdenes remotas no hay manipulación remota de las bombas), pero alarga la respuesta a algunas averías, algo que operación debe aceptar. En términos de 62443, cada alternativa define un conducto distinto entre las zonas de las estaciones de bombeo y la zona SCADA, con capacidades de seguridad distintas.

Ponga la evaluación en una tabla con los mismos criterios para cada alternativa, como el plazo de despliegue, el coste a cinco años, el efecto en la respuesta a los desbordamientos y la exposición que queda. Puntúe cada clase de estación por separado, porque una estación junto a la playa con una consecuencia de desbordamiento alta justifica más que una estación de interior cuyo desbordamiento queda contenido.

### 5.4 Registrar los rechazos

Un registro de diseño enumera las alternativas rechazadas y el motivo. De lo contrario, los revisores futuros las vuelven a proponer sin conocer la historia. Para BWRP, el registro anota que la alternativa 3 se rechazó porque los arranques remotos de bombas evitaron tres desbordamientos el año pasado. Si la operación cambia más adelante, por ejemplo al añadir almacenamiento local o control automático en las estaciones de consecuencia alta, el motivo puede dejar de ser válido, y el registro le dice al siguiente revisor exactamente qué condición comprobar. Feche el registro y nombre a quién aceptó el rechazo.

### Ejemplo resuelto (BWRP sintética)

Daniel recomienda la alternativa 1 de inmediato (elimina la exposición pública en un mes) y la alternativa 2 para las seis estaciones con mayor consecuencia de desbordamiento (cerca de las playas), y rechaza la alternativa 3 porque operación demostró que los arranques remotos de bombas evitaron tres desbordamientos el año pasado.

> **Caso sintético — Bayside Water Reclamation Plant.** Los recuentos de estaciones y el historial de desbordamientos son inventados.

### Errores y límites

Un APN privado no es cifrado; las redes internas del operador quedan fuera del control de BWRP. Hay que probar el efecto de latencia de las alternativas sobre la telemetría.

### Ejercicios — capítulo 5

- **EX021 — El registro de la opción rechazada.** Escriba la entrada de rechazo de la alternativa 3. *Rúbrica:* 3 = motivo con evidencia y condiciones para reconsiderarla; 2 = solo el motivo; 1 = «no elegida»; 0 = nada.
- **EX022 — Hipótesis de confianza de un APN privado.** Indique la hipótesis de confianza de la que depende la alternativa 1. *Rúbrica:* 3 = el operador aísla el tráfico del APN y gestiona el acceso correctamente; 2 = vago; 1 = intento mínimo; 0 = nada.
- **EX023 — Coste de ciclo de vida de las VPN en las RTU.** Enumere dos tareas recurrentes que añade la alternativa 2. *Rúbrica:* 3 = renovación/rotación de certificados, parches del firmware de los routers (o mantenimiento del concentrador); 2 = una; 1 = tareas puntuales; 0 = nada.
- **EX024 — Justificar un híbrido.** Justifique aplicar la alternativa 2 solo a seis estaciones. *Rúbrica:* 3 = niveles según la consecuencia, coste proporcional al riesgo; 2 = parcial; 1 = solo el coste; 0 = nada.
- **EX025 — Descripción del conducto.** Describa el conducto de la alternativa 2 con el lenguaje de zonas y conductos. *Rúbrica:* 3 = conducto desde cada zona de estación de bombeo por un túnel IPsec hasta el concentrador de la DMZ y de ahí a la zona SCADA, con los controles indicados; 2 = parcial; 1 = «VPN»; 0 = nada.

### Síntesis del capítulo

Un buen trabajo de diseño produce alternativas reales, las evalúa a lo largo de su ciclo de vida, escalona la protección según la consecuencia y recuerda por qué se rechazaron las opciones.

### Siga estudiando — capítulo 05 de 12

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Seguridad de TO, IoT y sistemas ciberfísicos: evaluación controlada

### Resultados de aprendizaje

Usted será capaz de (1) diseñar una comparación controlada de dos conjuntos de reglas de alerta sobre la misma reproducción etiquetada; (2) estimar la exhaustividad y la tasa de falsas alertas de cada uno; (3) calcular un intervalo de confianza bootstrap para la diferencia; y (4) decidir si la evidencia justifica un cambio en producción.

### 6.1 Mismos datos, dos tratamientos

Comparar el conjunto de reglas A (actual) con el conjunto de reglas B (propuesto) sobre semanas de datos distintas confunde las reglas con las semanas. Una evaluación controlada pasa las mismas ventanas etiquetadas por ambos. Las etiquetas proceden de un plan de pruebas: 40 ventanas contienen comportamiento de ataque inyectado en la reproducción y 160 son de operación normal.

```python
"""Lab 06: controlled evaluation of two alerting rule sets on the same synthetic replay, with bootstrap CI."""
import random
rnd = random.Random(6)
# 200 labelled replay windows: (is_attack, alert_by_A, alert_by_B)
data = []
for i in range(200):
    att = i < 40
    a = rnd.random() < (0.70 if att else 0.08)
    b = rnd.random() < (0.85 if att else 0.05)
    data.append((att, a, b))
def recall(rows, k): at = [r for r in rows if r[0]]; return sum(r[k] for r in at) / len(at)
def far(rows, k): be = [r for r in rows if not r[0]]; return sum(r[k] for r in be) / len(be)
print(f"A recall={recall(data,1):.3f} false-alert rate={far(data,1):.3f}")
print(f"B recall={recall(data,2):.3f} false-alert rate={far(data,2):.3f}")
diffs = []
for _ in range(2000):
    s = [rnd.choice(data) for _ in data]
    if any(r[0] for r in s): diffs.append(recall(s, 2) - recall(s, 1))
diffs.sort()
print(f"recall difference B-A 95% bootstrap CI: [{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Ejecútelo con `python3 lab_ab.py`. Salida verificada:

```text
A recall=0.650 false-alert rate=0.069
B recall=0.850 false-alert rate=0.037
recall difference B-A 95% bootstrap CI: [0.000, 0.388]
```

El plan de pruebas debe escribirse antes de construir la reproducción, nombrando los comportamientos de ataque, cuántas ventanas recibe cada uno y quién las etiqueta. Lo ideal es que la persona que inyecta los ataques no haya diseñado ninguno de los dos conjuntos de reglas. El laboratorio 6 sustituye esto por resultados aleatorios con semilla fija, así que sus números muestran el método y no el rendimiento real de las reglas de BWRP.

### 6.2 Cómo leer el resultado

La exhaustividad de B es 0,85 frente a 0,65 de A, y su tasa de falsas alertas es menor (3,7 % frente a 6,9 %). El intervalo bootstrap para la diferencia de exhaustividad va de 0,000 a 0,388: el extremo inferior toca el cero. Con solo 40 ventanas de ataque, no podemos descartar que B no sea mejor que A en exhaustividad, aunque la estimación puntual lo favorece claramente. Cada ventana remuestreada lleva los resultados de ambos conjuntos de reglas, así que el bootstrap anterior ya conserva el emparejamiento; una prueba exacta sobre las ventanas en las que A y B discrepan sería la comprobación cruzada natural.

Informe de los recuentos junto a las tasas para que el lector pueda juzgar la evidencia: 34 de 40 frente a 26 de 40 ventanas de ataque, y 6 frente a 11 de 160 ventanas normales. Con tan pocas ventanas de ataque, un puñado de resultados distintos cambiaría el panorama. Esa es la razón principal por la que Daniel pide una reproducción más grande y construida de forma independiente antes de la siguiente revisión.

### 6.3 Tomar la decisión

Los líderes rara vez necesitan certeza estadística para actuar; necesitan conocer el riesgo de cada opción. B es más barato en falsas alertas y probablemente mejor en exhaustividad. El inconveniente de cambiar (si B en realidad no fuera mejor) es pequeño. Daniel recomienda cambiar, ampliando a la vez el conjunto de ventanas de ataque a 120 antes de la siguiente revisión. La decisión es más fácil porque B también produce menos falsas alertas, algo que los operadores notan en cada turno. Daniel registra la recomendación con su incertidumbre, fija la fecha de la siguiente revisión y nombra al colega que construirá las 120 ventanas de ataque. Si la reproducción más grande no muestra ninguna ventaja en exhaustividad, la decisión se revisa en lugar de defenderse.

### 6.4 Amenazas a la validez

Los ataques inyectados reflejan la imaginación del autor de las pruebas; los adversarios reales pueden ser distintos. La reproducción omite la reacción de los operadores. El conjunto de reglas B se diseñó después de ver algunos de estos tipos de ataque, lo que lo favorece. Cada amenaza tiene un remedio parcial. Pida a un colega que no diseñó B que escriba ventanas de ataque nuevas. Deje constancia de que la reproducción mide alertas, no si los operadores actúan sobre ellas. Registre qué tipos de ataque influyeron en el diseño de B e informe de los resultados de B sobre ellos por separado del resto, para que el lector pueda ver si su ventaja se mantiene con comportamientos no vistos.

### Ejemplo resuelto (BWRP sintética)

Nota de evaluación de Daniel: «Reproducción R-6 (200 ventanas, 40 de ataque, semilla 6). B: exhaustividad 34/40, falsas alertas 6/160. A: exhaustividad 26/40, falsas alertas 11/160. Diferencia de exhaustividad, IC bootstrap del 95 % [0,000; 0,388]. Recomendación: adoptar B; ampliar a 120 ventanas de ataque construidas por un colega que no diseñó B».

> **Caso sintético — Bayside Water Reclamation Plant.** Las etiquetas de la reproducción y los resultados de las alertas los genera el script con semilla fija.

### Errores y límites

Los intervalos bootstrap con pocos positivos son inestables. Los resultados de alerta del laboratorio son sorteos aleatorios que sustituyen al comportamiento real de las reglas.

### Ejercicios — capítulo 6

- **EX026 — Los recuentos detrás de las tasas.** Convierta la tasa de falsas alertas de A, 0,069, en un recuento sobre las 160 ventanas normales. *Rúbrica:* 3 = 11 de 160; 2 = ≈11; 1 = 0,069 × 200; 0 = nada.
- **EX027 — Interpretar un IC que toca el cero.** ¿Qué le dice a quien decide un límite inferior de 0,000? *Rúbrica:* 3 = datos compatibles con ninguna mejora de la exhaustividad; incertidumbre por tener 40 positivos; 2 = parcial; 1 = «B es mejor»; 0 = nada.
- **EX028 — ¿Por qué reproducir las mismas ventanas?** Explique la ventaja de un diseño emparejado en este caso. *Rúbrica:* 3 = elimina la variación de una semana a otra; las diferencias se deben a las reglas; 2 = parcial; 1 = vago; 0 = nada.
- **EX029 — Autoría independiente de los ataques.** ¿Por qué debería un colega construir las nuevas ventanas de ataque? *Rúbrica:* 3 = evita un sesgo de diseño a favor de B; 2 = parcial; 1 = carga de trabajo; 0 = nada.
- **EX030 — Inconveniente asimétrico.** Argumente por qué cambiar a B es razonable a pesar del intervalo. *Rúbrica:* 3 = menos falsas alertas y probablemente mejor exhaustividad; coste pequeño si son iguales; reversible; 2 = parcial; 1 = «estadísticamente demostrado»; 0 = nada.

### Síntesis del capítulo

Una evaluación controlada empareja los tratamientos sobre datos etiquetados idénticos, informa de recuentos e intervalos, y permite a los líderes actuar de forma proporcionada a partir de evidencia incierta pero útil.

### Siga estudiando — capítulo 06 de 12

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](../../en/book/MANUSCRIPT.md#ch-07)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo para EX001–EX060. Bayside Water Reclamation Plant, Daniel Osei y todas las cifras son sintéticos. Cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación.

**EX001.** 10.000 + 0,05 × 400.000 + 0,02 × 2.500.000 = 10.000 + 20.000 + 50.000 = 80.000, todavía más que los 59.500 de B.

**EX002.** El escenario catastrófico puede producirse por rutas que ninguna opción de acceso remoto cierra, así que más gasto en acceso remoto no puede reducir el peor caso; el líder debería financiar una salvaguarda independiente (por ejemplo, un límite alto de dosificación cableado) para cambiar la cola.

**EX003.** «Revisar si el proveedor del intermediario notifica un incidente de seguridad que afecte a su servicio de sesiones, o si el informe de atestación del intermediario tiene más de 12 meses».

**EX004.** Total de B = 35.000 + 400.000p + 0,005 × 2.500.000 = 47.500 + 400.000p. Igualarlo a 100.000 da p = 52.500 / 400.000 ≈ 0,131 al año.

**EX005.** Si las estimaciones creíbles de la probabilidad de incidente de A van de 0,01 a 0,10 y la clasificación entre A y B se invierte dentro de ese rango, mientras que una revisión de dos semanas de los registros de acceso de proveedores podría acotar la estimación antes del plazo del contrato, aplazar para hacer el estudio es mejor que decidir ahora.

**EX006.** Solo documentada. Sin un registro de restauración no puede contarse como realizada; pida el último registro de restauración o programe una prueba.

**EX007.** Nueve RTU no registradas no pueden supervisarse, parchearse ni incluirse en la delimitación del alcance de un incidente, así que la brecha de inventario debilita varias capacidades a la vez, mientras que la falta de una guía de actuación afecta a una; corregir primero la capacidad habilitadora aumenta el valor de todos los controles posteriores.

**EX008.** Expectativa: las copias de seguridad de TO son restaurables y se prueban. Documentado: existe un procedimiento de copias de seguridad. Realizado: copias semanales de la lógica, sin prueba de restauración. Brecha: la restauración nunca se ha demostrado. Consecuencia: tras un ransomware o una corrupción de la lógica, el tiempo de recuperación es desconocido y puede ser de días. Responsable: ingeniero de sistemas de control, prueba antes del fin del trimestre.

**EX009.** Cuando BWRP deba demostrar conformidad con un requisito contractual o regulatorio formulado sobre IEC 62443 (por ejemplo, un esquema de certificación del programa de seguridad del propietario de activos), o cuando los integradores y proveedores ya usen la terminología de 62443, la parte 2-1 alinea la comparación con esas obligaciones.

**EX010.** Indica dónde es probable que haya brechas y da ejemplos concretos a la dirección, pero no es una opinión de aseguramiento sobre todo el programa: las cinco prácticas las eligió Daniel, pueden no ser representativas, y las prácticas no muestreadas podrían ser más débiles o más sólidas.

**EX011.** En la captura o en el registro de auditoría de la HMI aparece una escritura del punto de consigna en PLC-D a las 14:02 menos (o más) un desfase de reloj medido, y ese mismo desfase explica otros pares de eventos a lo largo de la mañana.

**EX012.** Moderada como mucho: una sola fuente de registro respalda un inicio de sesión, pero podría estar mal atribuido (cuenta compartida), alterado por un intruso o equivocado en la hora; la corroboración del servidor de salto o de la grabación de la sesión aumentaría la confianza.

**EX013.** Pregunte qué versiones exactas de firmware se analizaron, si contienen la biblioteca afectada (y en qué versión, según la SBOM) y por qué la función vulnerable no es alcanzable, pidiendo el análisis o la evidencia de las pruebas y no solo la conclusión.

**EX014.** «Ninguna escritura en la captura» solo respalda «ninguna escritura por la red» si la captura vio todos los paquetes; cero paquetes descartados en el puerto de supervisión muestran que la ausencia tiene significado y no es un hueco en la recogida.

**EX015.** Quién o qué causó el cambio: el historiador registra el valor y la hora, no el usuario, el equipo o la acción en el panel que lo inició.

**EX016.** La segmentación reduce sobre todo la frecuencia de los incidentes (15 % → 6 %), pero cuando uno ocurre su duración todavía puede ser larga (hasta 48 h), así que la cola condicional se reduce menos que la media, que está dominada por la frecuencia de incidentes.

**EX017.** No. El percentil 99 de referencia es 814.425, así que más del 1 % de los años simulados superan 600.000: la tolerancia se incumple.

**EX018.** Los residentes cercanos al punto de vertido, los abonados que financian los costes de recuperación y el ecosistema de la bahía (y los negocios que dependen de él, como los mariscadores); también son aceptables el regulador y los usuarios del agua aguas abajo.

**EX019.** (a) Público: muestra la gobernanza. (b) Solo interno (compartido con el regulador bajo confidencialidad si lo solicita): es un mapa para el atacante. (c) Público: un recuento agregado favorece la rendición de cuentas sin revelar técnicas.

**EX020.** Una cola más pesada añade interrupciones muy largas y raras: la media sube algo, pero el percentil 99 sube mucho más, porque los años extremos que definen p99 se vuelven más extremos.

**EX021.** «Rechazada: alternativa 3 (solo supervisión). Motivo: los registros de operación muestran que los arranques remotos de bombas evitaron tres desbordamientos el último año; eliminar las órdenes remotas aumentaría el riesgo de desbordamiento en las estaciones de consecuencia alta. Reconsiderar si el tiempo de respuesta de las cuadrillas baja de 20 minutos o si el control local de nivel se mejora con sensores redundantes».

**EX022.** Que el operador mantiene el tráfico del APN privado de BWRP aislado de otros clientes y de internet, controla qué SIM pueden unirse a él, y que su personal y sus sistemas no están ellos mismos comprometidos.

**EX023.** Renovar y revocar los certificados de dispositivo de 23 extremos de túnel, y aplicar parches al firmware de los routers del lado de las RTU y del concentrador de la DMZ.

**EX024.** Las seis estaciones junto a la playa tienen la peor consecuencia de desbordamiento (salud pública, cierres), así que justifican el mayor coste y la mayor carga de gestión del cifrado controlado por BWRP, mientras que el APN privado ofrece una reducción de riesgo suficiente para las estaciones de consecuencia menor.

**EX025.** Cada estación de bombeo es su propia zona; su conducto es un túnel IPsec desde el router de la estación hasta un concentrador en la zona DMZ de BWRP, con autenticación mutua por certificados y un cortafuegos que solo deja pasar el protocolo de sondeo del SCADA hacia la zona SCADA.

**EX026.** 0,069 × 160 ≈ 11, así que A dio 11 falsas alertas en las 160 ventanas normales (11/160 = 0,06875).

**EX027.** Los datos son compatibles con que B no sea mejor que A en exhaustividad: 40 ventanas de ataque son demasiado pocas para excluir una mejora nula, aunque la mejor estimación sea 0,20 superior.

**EX028.** Ambos conjuntos de reglas ven exactamente el mismo tráfico, así que las diferencias en las alertas proceden de las reglas y no de semanas, condiciones meteorológicas o modos de operación distintos; la comparación emparejada también permite que el bootstrap remuestree ventanas con ambos resultados asociados.

**EX029.** Daniel diseñó B en parte pensando en estos tipos de ataque; las ventanas escritas por otra persona reducen la probabilidad de que el conjunto de pruebas se adapte, sin querer, a los puntos fuertes de B.

**EX030.** B produce menos falsas alertas con los mismos datos y muy probablemente detecta más ataques; si en realidad es igual en exhaustividad, la organización pierde poco y puede revertir el cambio, así que el valor esperado de cambiar es positivo mientras se reúnen más datos.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; las normas y los avisos se revisan, así que vuelva a verificar las ediciones antes de citarlas. Los DOI se comprobaron en Crossref. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Antonakakis, M., et al. (2017). Understanding the Mirai Botnet. 26th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis>
- CISA. Cybersecurity advisories (ICS advisories are filterable). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series of standards (overview; part 2-1 and the zone and conduit concepts of part 3-2 are cited in the text). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS, including T0883 Internet Accessible Device. <https://attack.mitre.org/matrices/ics/>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
