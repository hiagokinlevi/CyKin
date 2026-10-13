# Seguridad de TO, IoT y sistemas ciberfísicos: métodos de investigación doctoral y práctica de la tesis

- Idioma: español (`es`), edición en español neutro internacional; programa de investigación doctoral, dos años; aproximadamente 1600 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–8 de 8 tienen texto didáctico escrito, los ejercicios EX001–EX050 y sus resultados resueltos correspondientes. Siguen abiertas la revisión independiente de la materia, la nueva verificación de las fuentes, la revisión de accesibilidad, la revisión lingüística y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no es un libro terminado.
- Público: investigadores avanzados con experiencia de investigación y una pregunta defendible sobre la seguridad de los sistemas de control industrial (ICS), la tecnología operacional (TO), el Internet industrial de las cosas (IIoT) u otros sistemas ciberfísicos (CPS). Conocimientos de entrada: el contenido previsto para el programa de [maestría](../../../../masters-2-years/ot-iot-security/en/book/PLAN.md) de esta área o experiencia equivalente, además de soltura práctica en teoría de control (modelos de espacio de estados, lazos de realimentación), probabilidad y estadística, y al menos un protocolo industrial como Modbus o DNP3.
- Relación con los cursos vecinos: el [curso doctoral de infraestructura crítica](../../../critical-sector-security/README.md) estudia servicios, sectores y cascadas intersectoriales; el [curso doctoral de respuesta a incidentes](../../../incident-response-resilience/README.md) estudia la detección y la respuesta organizacionales. **Este libro estudia el propio lazo de control**: sensores, actuadores, controladores, el proceso físico, los protocolos industriales y las funciones de seguridad que mantienen con vida a las personas cuando todo lo demás falla.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos.
- Límite educativo: este programa es un plan educativo independiente. No es un programa de doctorado acreditado, no otorga ningún título y no concede autorización para acceder, escanear, probar o estudiar ninguna planta, controlador, dispositivo, producto de fabricante o persona reales. Toda planta, organización, conjunto de datos, banco de pruebas, participante y resultado numérico de un ejemplo resuelto es **sintético**, salvo que una frase cite explícitamente una fuente pública. Nada de este libro es un procedimiento operativo para una instalación real.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Lea los ocho capítulos en orden; siguen el arco de un proyecto doctoral. El capítulo 1 fija los estándares de integridad y de seguridad física para una investigación en la que un experimento puede abrir una válvula. El capítulo 2 cartografía la frontera de la investigación en seguridad de TO y aísla una pregunta abierta. El capítulo 3 la convierte en una contribución falsable. El capítulo 4 replica las líneas de base y prueba el procedimiento en un modelo antes de tocar cualquier banco de pruebas. El capítulo 5 ejecuta el estudio principal y lo valida en un segundo banco de pruebas independiente. El capítulo 6 somete las afirmaciones a una crítica adversarial. El capítulo 7 ensambla la tesis y un archivo de reproducibilidad por niveles. El capítulo 8 prepara la defensa, la divulgación coordinada y un plan de publicación.

Cada capítulo contiene resultados de aprendizaje, secciones didácticas, un ejemplo resuelto, una actividad práctica con código sin conexión de la biblioteca estándar de Python 3, errores comunes y límites, ejercicios numerados con una rúbrica de 0–3, una síntesis y un bloque **Siga estudiando**. Intente cada ejercicio antes de abrir los [resultados resueltos](#worked-results).

Mantenga cinco etiquetas en cada nota de investigación: **observación** (lo que registró un instrumento o una fuente con nombre), **inferencia** (lo que usted concluye y bajo qué supuestos), **afirmación** (lo que defenderá, con su alcance), **decisión** (lo que alguien eligió a causa de ello) y **consecuencia física** (lo que le ocurre al proceso, a los equipos, a las personas o al entorno). La investigación en TO falla con mayor frecuencia cuando una observación de red se promueve en silencio a una afirmación sobre el proceso físico.

### El corpus de investigación sintético

El libro sigue un proyecto inventado, el **Setpoint Study** (Estudio del Punto de Consigna), que pregunta: *¿un detector que comprueba invariantes físicos entre sensores independientes (un residuo de balance de masa con una prueba de suma acumulada) detecta la manipulación por repetición de sensor en un lazo de control de nivel antes y con menos falsas alarmas que una alarma de proceso de banda fija, y bajo qué capacidades del atacante desaparece esa ventaja?*

| Elemento sintético | Función | Límite |
|---|---|---|
| **Kestrel Water Works, Plant A**: un tanque de almacenamiento, una bomba de entrada, un caudalímetro, un transmisor de nivel, un PLC y un enlace Modbus/TCP con un historiador SCADA | Contexto principal del modelo (capítulos 1, 3–5). | Empresa de servicios inventada; ninguna planta, personal o registro reales. |
| **Testbed T2, "Harrow Process Lab"**: una instalación de dos tanques de estilo universitario con un relé de seguridad separado | Contexto de validación independiente (capítulos 5–6). | Laboratorio inventado. |
| **TankBench-21** | Un banco de referencia sintético "publicado" cuya puntuación de detección declarada no puede reproducirse (capítulo 4). | Inventado; no lo busque. |
| Estudios sintéticos **S1–S8** | Artículos ficticios usados para practicar la evaluación crítica (capítulo 2). | Inventados. |
| Operadores **O01–O10** | Participantes ficticios de sala de control en una revisión ciega de alarmas (capítulo 5). | Inventados; no aparecen datos de sujetos humanos. |

Las salidas de los laboratorios provienen de los datos de prueba impresos en el texto y se ejecutan solo con la biblioteca estándar de Python 3. Demuestran métodos; no son hallazgos sobre ningún sistema real.

### Política de fuentes

Las afirmaciones fácticas sobre normas, incidentes públicos o investigaciones publicadas enlazan con fuentes que el autor consultó; vuelva a verificar las versiones antes de basarse en ellas. Referencias centrales usadas a lo largo del libro:

- NIST, [SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security*](https://csrc.nist.gov/pubs/sp/800/82/r3/final) (septiembre de 2023).
- ISA, [ISA/IEC 62443 series of standards](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) (página de presentación).
- MITRE, [ATT&CK for ICS matrix](https://attack.mitre.org/matrices/ics/).
- Modbus Organization, [*Modbus Application Protocol Specification V1.1b3*](https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf).
- J. Giraldo et al., ["A Survey of Physics-Based Attack Detection in Cyber-Physical Systems"](https://doi.org/10.1145/3203245), *ACM Computing Surveys* 51(4), 2018.
- D. Urbina et al., ["Limiting the Impact of Stealthy Attacks on Industrial Control Systems"](https://doi.org/10.1145/2976749.2978388), ACM CCS 2016.
- R. Sommer y V. Paxson, ["Outside the Closed World: On Using Machine Learning for Network Intrusion Detection"](https://doi.org/10.1109/SP.2010.25), IEEE S&P 2010.
- D. Arp et al., ["Dos and Don'ts of Machine Learning in Computer Security"](https://www.usenix.org/conference/usenixsecurity22/presentation/arp), USENIX Security 2022.
- E. S. Page, ["Continuous Inspection Schemes"](https://doi.org/10.1093/biomet/41.1-2.100), *Biometrika* 41, 1954 (la prueba CUSUM).
- U.S. DHS, [*The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research*](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) (2012).
- CISA, [Coordinated Vulnerability Disclosure Program](https://www.cisa.gov/coordinated-vulnerability-disclosure-process).
- ACM, [Artifact Review and Badging, Version 1.1](https://www.acm.org/publications/policies/artifact-review-and-badging-current).
- iTrust/SUTD, [Secure Water Treatment (SWaT) and related datasets](https://itrust.sutd.edu.sg/itrust-labs_datasets/), descrito solo al nivel de su página pública.

El vocabulario metodológico genérico (verificación frente a validación, números aleatorios comunes) se identifica como tal en lugar de recibir una cita inventada.

## Contenido

1. [Integridad y métodos avanzados de investigación](#ch-01)
2. [Seguridad de TO, IoT y sistemas ciberfísicos: frontera de la investigación](#ch-02)
3. [Propuesta de contribución original](../../en/book/MANUSCRIPT.md#ch-03)
4. [Replicación de la línea de base y piloto](../../en/book/MANUSCRIPT.md#ch-04)
5. [Estudio principal y validación independiente](../../en/book/MANUSCRIPT.md#ch-05)
6. [Crítica de pares y revisión](../../en/book/MANUSCRIPT.md#ch-06)
7. [Síntesis de la tesis y archivo de reproducibilidad](../../en/book/MANUSCRIPT.md#ch-07)
8. [Defensa y plan de publicación](../../en/book/MANUSCRIPT.md#ch-08)
9. [Resultados resueltos](#worked-results)

<a id="ch-01"></a>

## Capítulo 1 — Integridad y métodos avanzados de investigación

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá: (1) explicar por qué el proceso físico, y no el paquete, es el objeto de la investigación en seguridad de TO; (2) situar una afirmación de investigación en una escalera que va de la observación de red a la consecuencia física; (3) diseñar un experimento cuyo peor resultado creíble esté acotado por una capa de seguridad independiente; (4) aplicar los principios del Menlo Report a la investigación industrial; y (5) elegir métricas de detección que no puedan manipularse mediante convenciones de puntuación. El capítulo se apoya en sus conocimientos de entrada sobre diseño de investigación y prepara el mapeo de la frontera del capítulo 2.

### 1.1 El objeto de estudio: un lazo de control con consecuencias

Un sistema de información falla al revelar, corromper o retener datos. Un sistema de control industrial puede fallar de todas esas maneras, pero su falla definitoria es distinta: un **proceso físico** sale de su envolvente segura. Una bomba funciona en seco, un tanque se desborda, una dosis de cloro supera su límite, una turbina se embala. NIST SP 800-82 Rev. 3 describe la TO como sistemas que "interactúan con el entorno físico" y subraya que la seguridad física y la disponibilidad suelen dominar el orden de prioridades que en TI encabeza la confidencialidad. Esa diferencia transforma la investigación. Un método de detección que señala toda escritura Modbus maliciosa pero no puede decir si el proceso estuvo en peligro ha respondido una pregunta de TI en un entorno de TO.

Por eso el investigador doctoral modela el lazo de forma explícita. Un **sensor** mide una variable de proceso (nivel, presión, caudal). Un **controlador**, normalmente un controlador lógico programable (PLC), la compara con un **punto de consigna** y calcula una orden. Un **actuador** (bomba, válvula, interruptor) modifica el proceso. Una **capa de supervisión** (SCADA, HMI, historiador) observa y ajusta los puntos de consigna. Por debajo de todos ellos se encuentra un **sistema instrumentado de seguridad (SIS)** o un enclavamiento cableado diseñado para llevar el proceso a un estado seguro con independencia del sistema de control. Cada elemento es un posible punto de manipulación, y la honestidad de cada elemento es algo que su detector o bien supone o bien pone a prueba.

### 1.2 Una escalera de afirmaciones

Escriba cada afirmación en una escalera de cinco peldaños y niéguese a subir un peldaño sin evidencia que lo respalde:

1. **Observación de protocolo**: una trama con el código de función 6 (escribir un único registro) llegó a la unidad 1 (la especificación Modbus define los códigos de función).
2. **Inferencia de control**: el registro del punto de consigna cambió de 50 a 80.
3. **Inferencia de proceso**: la trayectoria del nivel del tanque fue coherente con el nuevo punto de consigna.
4. **Inferencia de seguridad**: la trayectoria cruzaría (o no) el disparo por nivel muy alto dentro del horizonte modelado.
5. **Afirmación de consecuencia**: se habrían producido (o no) daños a los equipos, una liberación o lesiones, dadas las capas de protección independientes.

La mayoría de los artículos publicados sobre detección en TO se detienen en el peldaño 1 o 2 y reportan exactitud; la mayor parte del valor práctico está en los peldaños 3–5. Una tesis no necesita llegar al peldaño 5, pero debe decir dónde se detiene.

### 1.3 La seguridad física antes que la integridad de los resultados

Un experimento de TI mal ejecutado pierde datos; un experimento de TO mal ejecutado puede herir a alguien. Las reglas de integridad de la investigación ordinaria (informar con honestidad, prerregistrar los análisis, conservar los datos brutos) se mantienen, pero una regla nueva tiene prioridad: **nunca pruebe en producción**. Los experimentos se ejecutan en simulaciones, en instalaciones de laboratorio aisladas cuyo peor caso es inofensivo o, de forma excepcional, en el sistema de un operador con su autorización escrita, su propia revisión de seguridad y una persona con nombre que tenga autoridad para detenerlo. Incluso en un laboratorio, el investigador debe enumerar el peor resultado físico creíble de cada experimento (por ejemplo, "el agua se derrama en el suelo del recinto de la instalación") y la capa independiente que lo acota (un interruptor de flotador mecánico, no el PLC sometido a prueba). Si la única protección es el sistema que usted está atacando, el experimento no está acotado.

### 1.4 Ética y doble uso

El Menlo Report adapta los principios del Informe Belmont a la investigación en TIC: respeto por las personas, beneficencia, justicia, y respeto por la ley y el interés público. En la investigación en TO domina la **beneficencia**: una técnica de evasión que derrota a todos los detectores publicados es una contribución real y también una receta. La respuesta ética no es el silencio, sino la proporción. Publique la *clase* de debilidad, la medición defensiva y la mitigación; retenga los detalles de explotación específicos de un fabricante hasta que se haya completado la divulgación coordinada (capítulo 8). El **respeto por las personas** se aplica a los operadores que usted entreviste u observe: pueden revelar prácticas inseguras que podrían costarles el empleo, por lo que los formularios de consentimiento deben indicar quién ve las notas brutas. El **respeto por la ley** abarca el control de exportaciones de algunas tecnologías industriales y los límites contractuales sobre los datos de los bancos de pruebas.

### 1.5 Los datos que describen una planta son sensibles

Las capturas de red, los programas de PLC, los diagramas de tuberías e instrumentación y los registros de alarmas forman en conjunto un mapa de cómo dañar una instalación. Trátelos como sensibles incluso cuando la instalación sea una instalación universitaria, porque estas reutilizan controladores comerciales y sus configuraciones revelan el comportamiento de los productos. Defina los niveles desde el principio: T0 público, T1 compartible con licencia, T2 compartible con investigadores verificados, T3 nunca sale del propietario. El capítulo 7 convierte estos niveles en un manifiesto de publicación.

Asigne un nivel a cada artefacto cuando se crea, no cuando se escribe la tesis, y registre qué propietario puede cambiarlo. Una captura tomada en el Testbed T2 empieza en T2 aunque parezca inofensiva. Bajar un nivel exige una razón escrita, como la eliminación de direcciones e identificadores de controladores, y una segunda persona que compruebe el resultado.

### 1.6 Métricas que resisten la manipulación

La investigación sobre detección en TO tiene un problema de medición. Los ataques en los conjuntos de datos de series temporales son segmentos largos y contiguos; una convención de puntuación muy usada, el *ajuste por puntos*, marca todo un segmento de ataque como detectado si cualquier punto dentro de él se señala. Como muestra el Laboratorio 1, puede convertir un detector que encuentra el 10 % de los puntos de ataque en uno que informa un F1 casi perfecto. Arp et al. enumeran esta familia de errores (medidas de rendimiento inadecuadas, desatención a la tasa de base, evaluación solo en laboratorio) para el aprendizaje automático en seguridad en general. Para la TO, el conjunto de métricas defendible es: **exhaustividad a nivel de evento** (fracción de episodios de ataque detectados), **tiempo hasta la detección** medido desde el inicio del ataque, **falsas alarmas por turno de operador** (porque las avalanchas de alarmas son en sí mismas un peligro para la seguridad) e **impacto físico en el momento de la detección** (cuánto se había desplazado el proceso cuando se disparó la alarma). Esta última métrica es específica de la TO y es la que se omite con más frecuencia.

### 1.7 Ejemplo resuelto: la primera revisión del protocolo del Setpoint Study

El primer protocolo del candidato proponía repetir ataques grabados en la red de historiador en producción de Kestrel Plant A en modo "solo lectura". El comité de revisión planteó tres problemas. Primero, *solo lectura es una afirmación, no una propiedad*: una herramienta de captura en un puerto espejo es pasiva, pero una herramienta que consulta al PLC es activa y añade carga a un controlador con un ciclo de escaneo fijo. Segundo, no se indicaba el peor resultado creíble. Tercero, la métrica era el F1 con ajuste por puntos. El protocolo revisado (a) traslada todos los experimentos de ataque a una simulación de Plant A y, más adelante, al Testbed T2 aislado; (b) establece como peor resultado en T2 "el tanque superior se desborda hacia la bandeja de goteo", acotado por una válvula de flotador mecánica independiente del PLC; (c) informa la exhaustividad por eventos, el retardo, las falsas alarmas por turno de 8 horas y el sobrellenado máximo; y (d) designa al responsable del laboratorio como autoridad de parada.

### 1.8 Actividad práctica — Laboratorio 1: el ajuste por puntos infla las puntuaciones

Ejecútelo sin conexión. Crea una secuencia sintética de etiquetas de 100 muestras con dos segmentos de ataque y un detector que señala cinco muestras.

```python
# Lab 1 (synthetic): how "point-adjusted" scoring inflates an OT anomaly detector.
labels = [0]*20 + [1]*30 + [0]*30 + [1]*10 + [0]*10      # two attack segments (100 samples)
alarms = [0]*100
for i in (5, 40, 85, 86, 87):    # detector flagged five samples
    alarms[i] = 1
def scores(lab, pred):
    tp = sum(l and p for l, p in zip(lab, pred)); fp = sum((not l) and p for l, p in zip(lab, pred))
    fn = sum(l and not p for l, p in zip(lab, pred))
    prec = tp/(tp+fp) if tp+fp else 0.0; rec = tp/(tp+fn) if tp+fn else 0.0
    return round(prec, 3), round(rec, 3), round(2*prec*rec/(prec+rec), 3) if prec+rec else 0.0
def point_adjust(lab, pred):
    out = pred[:]; i = 0
    while i < len(lab):
        if lab[i]:
            j = i
            while j < len(lab) and lab[j]: j += 1
            if any(pred[i:j]): out[i:j] = [1]*(j-i)
            i = j
        else: i += 1
    return out
def events(lab, pred):
    segs, i = [], 0
    while i < len(lab):
        if lab[i]:
            j = i
            while j < len(lab) and lab[j]: j += 1
            segs.append((i, j)); i = j
        else: i += 1
    return sum(any(pred[a:b]) for a, b in segs), len(segs)
print("pointwise P/R/F1 :", scores(labels, alarms))
print("point-adjust     :", scores(labels, point_adjust(labels, alarms)))
print("events detected  :", events(labels, alarms))
```

Salida esperada:

```text
pointwise P/R/F1 : (0.8, 0.1, 0.178)
point-adjust     : (0.976, 1.0, 0.988)
events detected  : (2, 2)
```

Interpretación: ambos episodios se detectaron (exhaustividad por eventos de 1,0), lo cual es realmente útil, pero el F1 con ajuste por puntos de 0,988 oculta que la primera alarma del segmento uno llegó 20 muestras después del inicio. Informe la exhaustividad por eventos *junto con* el retardo, nunca el F1 con ajuste por puntos por sí solo.

Las mismas cinco alarmas producen tres historias muy distintas. Punto a punto, el detector encontró cuatro de cuarenta muestras de ataque y generó una falsa alarma. Con ajuste por puntos, parece casi perfecto. Por eventos, encontró ambos episodios, uno de ellos tarde. Solo la tercera visión, acompañada del retardo, le dice a un operador lo que habría ocurrido en el tanque, y por eso es la que informa el Setpoint Study.

### 1.9 Errores comunes y límites

- Tratar una anomalía de protocolo como una anomalía de proceso (el peldaño 1 presentado como peldaño 3).
- Llamar "segura" a una captura pasiva mientras se ejecutan herramientas de consulta activa.
- Usar el PLC sometido a prueba como única cota de seguridad en un laboratorio.
- Informar una única puntuación agregada sin falsas alarmas por turno.
- Suponer que las instalaciones universitarias no son sensibles porque son pequeñas.

Cada error tiene una salvaguarda. Escriba el peldaño junto a cada afirmación en sus notas. Llame activa a cualquier herramienta que envíe solicitudes a un controlador, lea lo que lea. Nombre la capa independiente que acota cada ejecución de laboratorio, como la válvula de flotador de T2. Informe las falsas alarmas por turno de ocho horas junto a la exhaustividad. Clasifique los datos de una instalación universitaria como clasificaría los datos de una planta.

### Ejercicios — capítulo 1

Rúbrica para todos los ejercicios de este libro: **3** = correcto, con alcance definido, con la evidencia etiquetada y honesto sobre los límites; **2** = correcto con una laguna menor de alcance o de evidencia; **1** = parcialmente correcto o con afirmaciones sin etiquetar; **0** = ausente, inseguro o con afirmaciones excesivas.

- **EX001 — Afirmaciones en la escalera para el eslogan del desbordamiento.** *Objetivo:* clasificar afirmaciones. *Entrada:* la frase "Nuestro detector evita los desbordamientos de tanques". *Pasos:* reescríbala como una afirmación en cada uno de los peldaños 1–4 de la escalera para un ataque Modbus al punto de consigna. *Evidencia:* cuatro afirmaciones con alcance definido. *Restricción:* ninguna afirmación del peldaño 5 sin datos de las capas de protección. *Rúbrica:* 3 = cuatro peldaños con Modbus FC6/40001, punto de consigna 50→80, trayectoria, disparo modelado; nada del peldaño 5 sin datos de protección; 2 = cuatro peldaños pero con un vínculo débil con el proceso; 1 = omite un peldaño o inventa el peldaño 5; 0 = repite el eslogan.
- **EX002 — Acotar el experimento con la bomba de T2.** *Objetivo:* acotar un experimento. Para un ataque a la bomba del Testbed T2, indique el peor resultado creíble, la capa de protección independiente y la autoridad de parada. *Evidencia:* una tabla de tres filas. *Rúbrica:* 3 = desbordamiento≈2 L, válvula de flotador + bandeja de 10 L, responsable con nombre y parada de emergencia; una capa solo de PLC ≤1; 2 = tres filas pero con independencia débil; 1 = falta la autoridad de parada; 0 = sin acotar.
- **EX003 — Recolección pasiva frente a activa.** *Objetivo:* pasivo frente a activo. Clasifique cinco métodos de recolección de datos (captura en puerto espejo, consulta al PLC, exportación del historiador, carga del proyecto desde la estación de ingeniería, volcado de firmware) como pasivos o activos y dé un riesgo para cada uno. *Rúbrica:* 3 = cinco métodos con pasivo/activo y un riesgo cada uno (espejo, consulta, historiador, carga del proyecto, firmware); 2 = cuatro correctos; 1 = dos; 0 = ninguno.
- **EX004 — Revisión Menlo de la publicación de una evasión.** *Objetivo:* análisis Menlo. Aplique los cuatro principios a la publicación de una nueva técnica de evasión contra detectores basados en la física. *Evidencia:* un párrafo por principio y una decisión de publicación. *Rúbrica:* 3 = los cuatro principios de Menlo + publicar la clase y la defensa, retener los pasos específicos del producto; 2 = principios sin decisión; 1 = un principio; 0 = ninguno.
- **EX005 — Niveles desde el programa ladder hasta el simulador.** *Objetivo:* niveles de datos. Asigne T0–T3 a: un programa ladder de PLC, una tabla anonimizada de recuentos de alarmas, una captura de red con direcciones IP, un P&ID y un simulador sintético. Justifique cada uno. *Rúbrica:* 3 = ladder T2/T3, alarmas T1, captura con IP T2, P&ID T2/T3, simulador T0 con razones; 2 = cuatro correctos; 1 = dos; 0 = ninguno.
- **EX006 — Retardo por evento frente a ajuste por puntos.** *Objetivo:* métricas. Usando el Laboratorio 1, calcule el retardo de detección a nivel de evento para cada segmento y explique por qué el ajuste por puntos lo oculta. *Rúbrica:* 3 = retardos de 20 y 5 muestras + por qué el ajuste por puntos los oculta; 2 = solo los retardos; 1 = un retardo; 0 = ninguno.
- **EX007 — Encabezados del protocolo del Setpoint Study.** *Objetivo:* protocolo. Redacte los diez encabezados de un protocolo del Setpoint Study, incluidas las condiciones de parada y de abandono. *Rúbrica:* 3 = diez encabezados, incluida la parada (válvula de flotador, reinicio, pérdida de registros >1 %) y el abandono; 2 = encabezados sin parada/abandono; 1 = lista parcial; 0 = ninguno.

### Síntesis del capítulo

La investigación en TO estudia lazos de control cuya falla es física. Suba por la escalera de afirmaciones solo con evidencia, acote cada experimento con una capa de seguridad independiente, trate los datos de planta como sensibles y elija métricas (exhaustividad por eventos, retardo, falsas alarmas por turno, impacto físico en el momento de la detección) que una convención de puntuación no pueda inflar.

### Siga estudiando — capítulo 01 de 08

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Seguridad de TO, IoT y sistemas ciberfísicos: frontera de la investigación

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) organizar la literatura sobre seguridad de TO en familias de investigación, (2) leer las normas como hipótesis comprobables, (3) evaluar críticamente los artículos sobre detección frente a errores de evaluación conocidos, (4) usar los incidentes públicos solo al nivel en que sus analistas los publicaron y (5) enunciar una laguna falsable. Se apoya en la escalera de afirmaciones del capítulo 1 y alimenta la propuesta del capítulo 3.

### 2.1 Por qué la frontera es difícil de ver

La investigación en seguridad de TO está dispersa entre la ingeniería de control (detección de fallas, control resiliente), la seguridad informática (detección de intrusiones, análisis de protocolos), la ingeniería de seguridad física (análisis de peligros, seguridad funcional) y la práctica industrial (documentos técnicos de fabricantes, avisos gubernamentales). La misma idea aparece con nombres distintos: la *detección de fallas basada en residuos* de un ingeniero de control es la *detección de anomalías basada en la física* de un investigador de seguridad. Por eso, una búsqueda exploratoria debe usar sinónimos de cada comunidad y buscar tanto en bases de datos de ingeniería como en foros de seguridad.

Mantenga una tabla de sinónimos con una columna por comunidad y una fila por idea, y actualícela a medida que el cribado revele términos nuevos. Busque en las bases de datos de ingeniería con el vocabulario de control y en los foros de seguridad con el vocabulario de seguridad; después combine los resultados y elimine los duplicados. Registre de qué comunidad procede cada estudio incluido, para que un lector pueda ver si el mapa está equilibrado o se inclina hacia una tradición.

### 2.2 Familias de investigación

**Arquitectura y segmentación.** El modelo de referencia Purdue, descrito en NIST SP 800-82 Rev. 3, organiza en capas la empresa (niveles 4–5), la gestión de operaciones (3), el control de supervisión (2), el control básico (1) y el proceso físico (0), con una DMZ industrial entre TI y TO. ISA/IEC 62443-3-2 replantea la segmentación como *zonas y conductos* con niveles de seguridad objetivo. Entre las preguntas de investigación están si los diseños de segmentación reducen realmente las rutas de ataque alcanzables y cómo el IIoT conectado a la nube erosiona el modelo por capas.

**Seguridad de protocolos.** Los protocolos industriales clásicos, como Modbus, se diseñaron sin autenticación: la especificación del protocolo de aplicación Modbus define códigos de función y modelos de datos, pero ningún campo de seguridad. DNP3 añadió Secure Authentication; OPC UA incluye un modelo de seguridad. La investigación estudia la adopción, los fallos de implementación y el costo de incorporar seguridad a posteriori en redes deterministas.

**Detección.** La detección basada en la red modela el tráfico; la detección basada en el proceso (basada en la física) modela la planta. Giraldo et al. revisaron la detección basada en la física y encontraron que las evaluaciones rara vez consideran a un adversario que conoce el detector; Urbina et al. propusieron medir cuánto puede desplazar el proceso un atacante *sigiloso* sin superar el umbral del detector, la idea del impacto en el momento de la detección del capítulo 1.

**Coingeniería de seguridad física y ciberseguridad.** Los métodos de análisis de peligros (HAZOP, STPA) se están extendiendo a causas adversariales; IEC 62443 y las normas de seguridad funcional se están alineando. La investigación pregunta cómo una falla de ciberseguridad puede anular una función de seguridad y cómo certificar ambas.

**Evidencia de amenazas.** MITRE ATT&CK for ICS cataloga técnicas de adversarios como *Modify Parameter*, *Spoof Reporting Message* y *Manipulation of View*, cada una fundamentada en informes públicos. Los incidentes públicos (la manipulación por Stuxnet de los accionamientos de las centrifugadoras mientras mostraba valores normales, los cortes de distribución en Ucrania en 2015 y el malware dirigido a sistemas instrumentados de seguridad, TRITON/TRISIS) muestran que la *manipulación de la vista*, la repetición de valores normales ante los operadores, es un objetivo documentado de los adversarios, no uno especulativo.

### 2.3 Las normas como hipótesis

Una norma codifica una creencia experta: "las zonas con nivel de seguridad 2 resisten a los atacantes casuales". Trate tales enunciados como hipótesis. Una tesis puede medir si un diseño de zonas reduce la alcanzabilidad, si una práctica de alarmas recomendada reduce la sobrecarga de los operadores o si un nivel de seguridad es alcanzable dentro del presupuesto de tiempo de escaneo de un controlador. No cite una norma como evidencia de que sus recomendaciones funcionan; cítela como la afirmación que usted pone a prueba.

Escriba en la tesis cada enunciado puesto a prueba tal como lo formula la norma y, a continuación, como la hipótesis medible que usted derivó de él, para que los lectores puedan juzgar la traducción. Un resultado nulo es útil: si un diseño de zonas recomendado no reduce la alcanzabilidad en su topología, eso dice algo sobre el diseño o sobre la topología, y ambas cosas merecen informarse.

### 2.4 Evaluación crítica: qué hace creíble un artículo sobre detección en TO

Aplique la advertencia de Sommer y Paxson (la detección de anomalías funciona mal cuando el espacio "normal" es abierto y los ataques son raros) y la lista de verificación de Arp et al. Pregunte a cada artículo: ¿el conjunto de datos procedía de un banco de pruebas o de una planta? ¿Generaron los ataques las mismas personas que construyeron el detector? ¿Conoce el adversario el detector? ¿Se eligió el umbral sobre el conjunto de prueba? ¿Se informa el impacto en el momento de la detección? Los conjuntos de datos públicos como SWaT, de iTrust, proceden de un banco de pruebas real (a escala reducida) de tratamiento de agua, lo que los hace valiosos, pero cada conjunto de datos tiene un conjunto fijo de ataques y una planta fija; las afirmaciones de generalización más allá de ellos necesitan un segundo contexto.

### 2.5 Ejemplo resuelto: evaluación crítica de los estudios sintéticos S1–S8

| Estudio (sintético) | Datos | ¿Adversario consciente? | Origen del umbral | ¿Se informa el impacto? | Veredicto |
|---|---|---|---|---|---|
| S1 | un conjunto de datos público de banco de pruebas | no | conjunto de prueba | no | optimista |
| S2 | simulación | sí (acotado) | validación | sí | sólido pero de una sola planta |
| S3 | registros de planta, sin ataques | — | — | — | solo estudio de falsas alarmas |
| S4 | banco de pruebas | no | conjunto de prueba | no | F1 con ajuste por puntos |
| S5 | simulación + banco de pruebas | parcial | validación | parcial | prometedor |
| S6 | solo red | no | validación | no | solo peldaño 1 |
| S7 | banco de pruebas, falsificación de varios sensores | sí | validación | sí | muestra evasión por repetición + caudal |
| S8 | revisión | — | — | — | mapa |

El patrón es la laguna: ningún estudio combina (a) un adversario que conoce el detector, (b) umbrales fijados antes de la prueba, (c) el impacto en el momento de la detección y (d) la validación en una segunda planta independiente.

### 2.6 Actividad práctica — Laboratorio 2: codificar el mapa

Copie la tabla en un CSV y cuente, con el módulo `csv` de Python, cuántos estudios cumplen cada criterio. Recuentos esperados a partir de la tabla: adversario plenamente consciente = 2 (S2, S7), umbrales de validación = 4 (S2, S5, S6, S7), impacto plenamente informado = 2 (S2, S7), dos contextos = 1 (S5). Cambie una decisión de codificación y observe cómo cambia el enunciado de la laguna; registre esa sensibilidad en sus notas. Un cambio pequeño puede hacer que un estudio cruce la línea. Si la conciencia del adversario en S5 se codifica como plena en lugar de parcial, tres estudios cumplen ese criterio en lugar de dos, pero ninguno combina todavía las cuatro propiedades, de modo que la laguna se mantiene. Registre cada regla de codificación con un ejemplo y pida a un segundo codificador que codifique la tabla de forma independiente antes de basarse en ella.

### 2.7 Una laguna falsable

Laguna débil: "La detección basada en la física está poco estudiada". Laguna fuerte: "Ninguna evaluación informa a la vez el retardo de detección y la desviación máxima del proceso en el momento de la detección para ataques de repetición de sensor en un lazo de nivel, con umbrales fijados de antemano, en dos plantas independientes; predecimos que un residuo de balance de masa reduce el retardo respecto a una alarma de banda, y que la ventaja desaparece cuando el atacante controla también el sensor de caudal independiente". La versión fuerte nombra la condición bajo la cual la contribución falla.

La laguna fuerte predice su propia falla, que el Setpoint Study confirma más adelante como la clase B. Esa predicción es lo que permite a un comité juzgar la tesis con justicia: si el detector de residuos hubiera detectado también la clase B, habría que revisar la laguna, porque un detector no debería poder ver a través de una mentira coherente en ambos sensores sin alguna otra señal independiente.

### 2.8 Errores comunes y límites

Citar material de marketing de fabricantes como evidencia; tratar las técnicas de ATT&CK como frecuencias (son posibilidades documentadas, no tasas de base); reclamar novedad por el nombre de un conjunto de datos nuevo; describir incidentes más allá de lo que afirman los análisis públicos. Un documento de un fabricante puede señalar una pregunta, pero no puede responderla. ATT&CK le dice que se ha visto la manipulación de la vista, no con qué frecuencia. Un conjunto de datos nuevo solo es novedoso si le permite poner a prueba algo que antes no podía. Al describir Stuxnet, Ucrania o TRITON, diga lo que informaron los analistas citados y deténgase ahí.

### Ejercicios — capítulo 2

- **EX008 — Sinónimos para sensores manipulados.** Construya una tabla de sinónimos con al menos cuatro términos de la ingeniería de control y cuatro de la seguridad para el concepto "detectar datos de sensores manipulados". *Rúbrica:* 3 = ≥4 términos de control + ≥4 de seguridad para sensores manipulados; 2 = 3+3; 1 = solo un lado; 0 = ninguno.
- **EX009 — Mapa Purdue de Plant A.** Asigne los componentes de Plant A del Setpoint Study a los niveles Purdue 0–3 y nombre el conducto que atraviesa una consulta al historiador. *Rúbrica:* 3 = componentes L0–L3 + la consulta al historiador atraviesa la DMZ TI/TO (3.5) y 3–2; 2 = niveles sin conducto; 1 = parcial; 0 = ninguno.
- **EX010 — Hipótesis de zonas de 62443.** Reescriba una recomendación de zonas y conductos de IEC 62443 como una hipótesis medible. *Rúbrica:* 3 = hipótesis medible con un recorte ≥90 % de la alcanzabilidad de escritura y método de medición; 2 = hipótesis sin métrica; 1 = eslogan; 0 = ninguno.
- **EX011 — Evaluar el estudio S4.** Evalúe críticamente el estudio S4 con cinco preguntas de §2.4 e indique qué resultado puede respaldar. *Rúbrica:* 3 = cinco puntos de evaluación + techo de respaldo (señala algunas muestras; no retardo/impacto/generalización); 2 = evaluación sin techo; 1 = vago; 0 = ninguno.
- **EX012 — Dos técnicas de ATT&CK for ICS.** Elija dos técnicas de ATT&CK for ICS relevantes para el Setpoint Study y explique por qué su presencia en la matriz no es evidencia de frecuencia. *Rúbrica:* 3 = Spoof Reporting Message + Modify Parameter y ninguna afirmación de tasa de base; 2 = técnicas sin salvedad; 1 = una técnica; 0 = ninguno.
- **EX013 — Invertir la codificación del adversario en S5.** Ejecute el Laboratorio 2, cambie la codificación del adversario de S5 a "sí" e informe cómo cambia el enunciado de la laguna. *Rúbrica:* 3 = recuento de conscientes→3, eliminar el absoluto "ningún estudio consciente", mantener la laguna de combinación; 2 = solo el recuento; 1 = recuento erróneo; 0 = ninguno.
- **EX014 — Lagunas débil y fuerte sobre DNP3-SA.** Escriba un enunciado de laguna débil y uno fuerte para otro tema de TO (por ejemplo, la adopción de DNP3 Secure Authentication). *Rúbrica:* 3 = débil frente a fuerte con muestra pública + predicción de latencia; 2 = débil/fuerte sin números; 1 = un enunciado; 0 = ninguno.

### Síntesis del capítulo

La frontera se extiende entre comunidades; léala con sinónimos, trate las normas como hipótesis y evalúe los artículos sobre detección según la conciencia del adversario, la filtración del umbral, el informe del impacto y la validación en un segundo contexto. Una laguna solo es útil cuando dice cómo podría cerrarse y cómo podría fallar ese cierre.

### Siga estudiando — capítulo 02 de 08

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](../../en/book/MANUSCRIPT.md#ch-03)

<a id="worked-results"></a>

## Resultados resueltos

Cada respuesta muestra una respuesta defendible; las rúbricas de cada ejercicio premian alternativas que cumplan el mismo estándar de evidencia, alcance y honestidad. Todos los números provienen de los laboratorios sintéticos.

### Capítulo 1

**EX001.** Peldaño 1: "Se observó una escritura Modbus (código de función 6) en el registro de retención 40001 de la unidad 1". Peldaño 2: "El punto de consigna de nivel cambió de 50 a 80". Peldaño 3: "La trayectoria del nivel subió hacia 80, de forma coherente con el nuevo punto de consigna". Peldaño 4: "En el modelo, la trayectoria cruzaría el disparo por nivel muy alto en t+420 s sin intervención". El peldaño 5 se retiene: no hay datos sobre la capa mecánica de alivio. "Evita los desbordamientos" se sustituye por "generó una alarma N s antes del disparo modelado".
**EX002.** Peor resultado: el tanque superior se desborda hacia la bandeja de goteo (≈2 L de agua). Capa independiente: válvula de flotador mecánica que cierra la entrada, más una bandeja de goteo dimensionada para 10 L. Autoridad de parada: responsable del laboratorio con nombre y una parada de emergencia física que corta la alimentación de la bomba. Rúbrica: un enclavamiento del PLC como única capa obtiene ≤1.
**EX003.** Captura en puerto espejo: pasiva; riesgo = datos sensibles almacenados. Consulta al PLC: activa; añade carga al ciclo de escaneo. Exportación del historiador: pasiva para el PLC pero activa en el historiador; riesgo = carga del servidor y volumen de datos. Carga del proyecto desde la estación de ingeniería: activa; en algunos productos puede provocar cambios de modo del controlador. Volcado de firmware: activo y potencialmente disruptivo; puede exigir detener el controlador.
**EX004.** Respeto por las personas: no hay personas directamente implicadas; los clientes de los fabricantes se ven afectados de forma indirecta. Beneficencia: los defensores aprenden a exigir mediciones independientes; los atacantes ganan poco más allá de las tácticas documentadas de manipulación de la vista si se retienen los pasos específicos del producto. Justicia: las empresas de servicios pequeñas, las menos capaces de aplicar parches, soportan el riesgo; publique mitigaciones de bajo costo. Ley e interés público: compruebe las obligaciones de divulgación y las normas de exportación. Decisión: publicar la clase de capacidad y la defensa; retener las secuencias específicas del producto hasta que concluya la divulgación coordinada.
**EX005.** Programa ladder: T2/T3 (revela la lógica y los enclavamientos de seguridad). Recuentos de alarmas anonimizados: T1. Captura con IP: T2 (topología). P&ID: T3 para plantas reales, T2 para una instalación de laboratorio. Simulador sintético: T0.
**EX006.** El segmento 1 empieza en el índice 20; primera alarma en 40 → retardo de 20 muestras. El segmento 2 empieza en 80; primera alarma en 85 → retardo de 5. El ajuste por puntos acredita como detectados los 30 y los 10 puntos, lo que oculta el retardo de 20 muestras durante el cual el proceso se desplazó.
**EX007.** Título y pregunta; antecedentes y laguna; hipótesis H1–H4; modelo de atacante; sistemas (simulador, T2) y cotas de seguridad; niveles de datos y manejo; métricas; plan de análisis con umbrales congelados; condiciones de parada (se alcanza la válvula de flotador, reinicio no planificado, pérdida de registros >1 %) y condiciones de abandono (T2 no puede hacerse seguro; el simulador no supera la verificación); plan de ética y divulgación.

### Capítulo 2

**EX008.** Control: detección y aislamiento de fallas, generación de residuos, redundancia analítica, monitorización basada en observadores, validación de sensores. Seguridad: inyección de datos falsos, falsificación de sensores, manipulación de la vista, ataque de repetición, detección de anomalías basada en la física.
**EX009.** Nivel 0: tanque, bomba, transmisor de nivel, caudalímetro. Nivel 1: PLC. Nivel 2: SCADA/HMI. Nivel 3: historiador (operaciones). Una consulta al historiador desde la empresa atraviesa el conducto de la DMZ TI/TO (nivel 3.5) y el conducto entre los niveles 3 y 2.
**EX010.** "Las zonas entre el nivel 2 y el nivel 1 con un conducto limitado a códigos de función de lectura reducen en ≥90 % el número de hosts capaces de emitir escrituras Modbus a los PLC en comparación con una red plana, medido mediante un análisis de alcanzabilidad de la topología sintética".
**EX011.** S4: datos de banco de pruebas; adversario no consciente; umbral sobre el conjunto de prueba; sin impacto; F1 con ajuste por puntos. Respalda como máximo "el detector señala algunas muestras dentro de estos segmentos de ataque en este banco de pruebas"; no afirmaciones de generalización, retardo o impacto.
**EX012.** *Spoof Reporting Message* y *Modify Parameter*. La matriz documenta que los adversarios han usado o podrían usar una técnica, con base en informes públicos; no cuenta las ocurrencias en todas las plantas, así que no ofrece ninguna tasa de base.
**EX013.** El recuento de adversarios conscientes pasa a 3 (S2, S5, S7). El enunciado de la laguna debe eliminar "ningún estudio tiene un adversario que conozca el detector" y mantener la laguna de combinación (consciente + umbrales congelados + impacto + dos contextos), que ningún estudio individual cumple todavía: S5 informa el impacto solo de forma parcial.
**EX014.** Débil: "DNP3-SA se usa poco". Fuerte: "Ninguna medición informa la proporción de estaciones remotas DNP3 de una muestra pública definida que negocian Secure Authentication, ni la latencia que añade en enlaces serie; predecimos una adopción inferior al 10 % y una latencia superior al presupuesto de sondeo en enlaces de 9,6 kbit/s, y la predicción quedaría refutada por una adopción superior al 30 %".

<a id="glossary"></a>

## Glosario

**ATT&CK for ICS.** Base de conocimiento de MITRE sobre tácticas y técnicas de adversarios contra sistemas de control industrial; documenta posibilidades, no tasas de base.

**Atacante de clase A / clase B (Setpoint Study).** La clase A falsifica un único sensor (por ejemplo, el de nivel) mientras una medición independiente sigue siendo honesta; la clase B controla ambas mediciones de forma coherente, de modo que un residuo de balance de masa no ve ningún desacuerdo.

**CUSUM.** Prueba de suma acumulada (Page, 1954) usada aquí sobre un residuo de balance de masa entre mediciones cableadas de forma independiente.

**Niveles de datos T0–T3.** Etiquetas de manejo que van desde lo sintético o público (T0–T1) hasta artefactos identificables de la instalación de laboratorio o de la planta (T2–T3), usadas en las reglas de archivo del Setpoint Study.

**Retardo de detección a nivel de evento.** Muestras desde el inicio del segmento de ataque hasta la primera alarma verdadera; contrasta con las puntuaciones con ajuste por puntos, que acreditan segmentos enteros.

**Manipulación de la vista.** Objetivo del adversario de suministrar a operadores o detectores lecturas falsas del proceso mientras el estado de la planta diverge.

**Menlo Report.** Principios éticos del U.S. DHS (2012) para la investigación en TIC: respeto por las personas, beneficencia, justicia, y respeto por la ley y el interés público.

**Plant A.** Contexto sintético de un solo tanque en el Setpoint Study, usado para experimentos de simulación y ajuste de umbrales.

**Modelo Purdue / zonas y conductos.** Arquitectura ICS por capas (NIST SP 800-82) y marco de segmentación de ISA/IEC 62443-3-2.

**Setpoint Study.** Caso doctoral recurrente: medir cuándo un CUSUM sobre el residuo entre sensores detecta la repetición de nivel frente a una alarma de banda, y dónde la clase B lo derrota.

**Testbed T2.** Instalación aislada de laboratorio con tanques de agua, válvula de flotador mecánica, bandeja de goteo y una autoridad de parada de emergencia con nombre; usada para la validación con umbrales congelados.

**TankBench-21.** Banco de referencia publicado previamente cuyas puntuaciones con ajuste por puntos la tesis vuelve a implementar para exponer los efectos de la métrica.

<a id="references"></a>

## Referencias

Enlaces comprobados el 13 de octubre de 2026; vuelva a verificar las ediciones antes de citarlas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- ACM. Artifact Review and Badging, Version 1.1. <https://www.acm.org/publications/policies/artifact-review-and-badging-current>
- Arp, D. et al. Dos and Don'ts of Machine Learning in Computer Security. USENIX Security 2022. <https://www.usenix.org/conference/usenixsecurity22/presentation/arp>
- CISA. Coordinated Vulnerability Disclosure Program. <https://www.cisa.gov/coordinated-vulnerability-disclosure-process>
- Giraldo, J. et al. A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. *ACM Computing Surveys* 51(4), 2018. <https://doi.org/10.1145/3203245>
- IEC 62443-3-2. Security for industrial automation and control systems — Security risk assessment for system design. IEC.
- iTrust, SUTD. Secure Water Treatment (SWaT) and related datasets (public page). <https://itrust.sutd.edu.sg/itrust-labs_datasets/>
- MITRE. ATT&CK for Industrial Control Systems. <https://attack.mitre.org/matrices/ics/>
- NIST SP 800-82 Rev. 3. Guide to Operational Technology (OT) Security. <https://doi.org/10.6028/NIST.SP.800-82r3>
- Page, E. S. Continuous Inspection Schemes. *Biometrika* 41(1–2), 1954. <https://doi.org/10.1093/biomet/41.1-2.100>
- Urbina, D. et al. Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS 2016. <https://doi.org/10.1145/2976749.2978388>
- U.S. DHS. The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research (2012). <https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf>
