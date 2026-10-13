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
3. [Propuesta de contribución original](#ch-03)
4. [Replicación de la línea de base y piloto](#ch-04)
5. [Estudio principal y validación independiente](#ch-05)
6. [Crítica de pares y revisión](#ch-06)
7. [Síntesis de la tesis y archivo de reproducibilidad](#ch-07)
8. [Defensa y plan de publicación](#ch-08)
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

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Propuesta de contribución original

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) elegir el tipo de contribución que hace su tesis, (2) expresar un mecanismo de detección como un invariante físico, (3) definir un modelo de atacante explícito, (4) enunciar hipótesis con umbrales y explicaciones rivales y (5) declarar de antemano las condiciones en las que su contribución falla. Convierte la laguna del capítulo 2 en un estudio que el capítulo 4 puede pilotar.

### 3.1 Tipos de contribución

Una tesis de seguridad de TO puede aportar un **mecanismo** (un nuevo detector o protección), una **medición** (una forma de cuantificar el impacto o la exposición), un **hallazgo empírico** (cómo se comportan realmente los operadores o las plantas) o un **principio validado** (una regla de diseño que se mantiene en distintos contextos). El Setpoint Study aporta una comparación respaldada por mediciones: no inventa la prueba CUSUM (Page, 1954) ni la detección basada en residuos (revisada por Giraldo et al.); comprueba cuándo un invariante entre sensores ayuda frente a un objetivo adversario específico y documentado —la manipulación de la vista— y cuantifica dónde deja de ayudar. Un posicionamiento honesto de este tipo es una fortaleza en una defensa, no una debilidad.

### 3.2 El mecanismo como invariante físico

El tanque de la planta A obedece un balance de masa discreto: nivel siguiente = nivel + caudal de entrada − caudal de salida, con un caudal de salida ≈ 0,02 × nivel a través de un orificio fijo en el modelo sintético (equilibrio de 50 unidades cuando el caudal de entrada es 1,0). Un transmisor de nivel y un caudalímetro miden magnitudes distintas producidas por la misma física. Si un atacante repite lecturas antiguas de nivel mientras fuerza la bomba, la estimación de nivel predicha a partir del caudalímetro diverge del nivel informado. El **residuo** r = nivel informado − nivel predicho debería estar cerca de cero en operación normal y alejarse bajo ese ataque. Un **CUSUM** acumula la magnitud del residuo por encima de una holgura k y alarma cuando la suma supera un umbral h; está diseñado para captar desplazamientos pequeños y persistentes que una banda fija no detecta.

El invariante lleva una suposición incorporada: el caudalímetro es honesto. Si el atacante controla ambos sensores (o el PLC que los informa), el invariante puede satisfacerse con una mentira coherente. Enunciar esta suposición es el comienzo del modelo de atacante.

### 3.3 Modelo de atacante

Escriba el modelo como capacidades, conocimiento y objetivo:

| Elemento | Suposición del Setpoint Study |
|---|---|
| Capacidades | Acceso de escritura al comando de la bomba y a la lectura de nivel en el enlace SCADA (coherente con *Modify Parameter* y *Spoof Reporting Message* de ATT&CK for ICS); **clase A**: solo el sensor de nivel; **clase B**: sensores de nivel y de caudal. |
| Conocimiento | Conoce los límites de alarma de la banda; la clase B también conoce el detector. |
| Objetivo | Elevar el nivel real manteniendo normales los valores mostrados (manipulación de la vista). |
| Fuera de alcance | Compromiso de la válvula mecánica de flotador; manipulación física. |

### 3.4 Hipótesis y umbrales

- **H1 (detección):** frente a la repetición de clase A, el CUSUM de residuos detecta ≥95 % de los episodios con un retardo medio ≤ 60 pasos, mientras que la alarma de banda detecta ≤ 10 %.
- **H2 (falsas alarmas):** en 100 ejecuciones nominales, el CUSUM de residuos no produce más ejecuciones con falsa alarma que la alarma de banda.
- **H3 (impacto):** el sobrellenado real máximo en el momento de la detección es menor con CUSUM que con la alarma de banda.
- **H4 (condición de fallo):** frente a la clase B, la detección del CUSUM cae a ≤ 10 %, la frontera prevista de la contribución.

Los umbrales se justifican, no son decorativos: 60 pasos corresponden, en la base de tiempo sintética, al tiempo que tarda el sobrellenado en alcanzar la mitad del margen hasta el disparo por nivel muy alto. H4 es una hipótesis que usted *quiere* poder confirmar: un método cuyos límites se han medido es más útil que uno cuyos límites se desconocen.

### 3.5 Líneas de base y rivales

Las líneas de base son (a) la **alarma de banda** que la planta ya tiene, (b) un **detector de red** que señala cualquier escritura en el registro de nivel —trivialmente eficaz si las escrituras son raras, inútil si el atacante repite en el sensor— y (c) un **oráculo** con acceso al nivel real, que da el mejor retardo posible. Las explicaciones rivales de cualquier ventaja del CUSUM incluyen el ajuste del umbral con datos de prueba, un simulador demasiado limpio y magnitudes de ataque elegidas a la medida del método. Cada rival recibe una prueba en el capítulo 4 o 5.

### 3.6 Ejemplo resuelto y laboratorio 3

El laboratorio 3 implementa el modelo y ambos detectores en 100 ejecuciones con semilla por condición.

```python
# Lab 3 - Setpoint Study (synthetic): fixed-band alarm vs. physics-residual CUSUM on one tank.
# Python 3 standard library only. Attack: pump forced to over-fill while the level sensor replays
# nominal values ("replay"); variant "replay+flow" also spoofs the inflow meter.
import random

def run(seed, attack, detector, steps=600, onset=300):
    rng = random.Random(seed)
    true_level, s, first_alarm, max_dev = 50.0, 0.0, None, 0.0
    est = 50.0
    for t in range(steps):
        inflow = 1.0 + rng.gauss(0, 0.05)
        if attack and t >= onset:
            inflow += 0.05                      # forced pump: hidden extra inflow
        true_level += inflow - 0.02 * true_level
        level_meas = true_level + rng.gauss(0, 0.3)
        flow_meas = inflow + rng.gauss(0, 0.02)
        if attack and t >= onset:
            level_meas = 50.0 + rng.gauss(0, 0.3)   # replayed nominal level
            if attack == "replay+flow":
                flow_meas = 1.0 + rng.gauss(0, 0.02)
        est = est + flow_meas - 0.02 * est      # mass-balance prediction from flow meter
        if detector == "band":
            hit = abs(level_meas - 50.0) > 1.5
        else:
            s = max(0.0, s + abs(level_meas - est) - 0.6)
            hit = s > 6.0
        if hit and first_alarm is None:
            first_alarm = t
        if t >= onset:
            max_dev = max(max_dev, true_level - 50.0)
    return first_alarm, max_dev

for det in ("band", "cusum"):
    fa = sum(run(k, None, det)[0] is not None for k in range(100))
    for atk in ("replay", "replay+flow"):
        res = [run(k, atk, det) for k in range(100)]
        hits = [a - 300 for a, _ in res if a is not None and a >= 300]
        delay = f"{sum(hits)/len(hits):.1f}" if hits else "n/a"
        print(f"{det:5s} {atk:11s} false_alarm_runs={fa}/100 detected={len(hits)}/100 "
              f"mean_delay={delay} worst_true_overfill={max(d for _, d in res):.2f}")
```

Salida esperada:

```text
band  replay      false_alarm_runs=9/100 detected=0/100 mean_delay=n/a worst_true_overfill=3.36
band  replay+flow false_alarm_runs=9/100 detected=0/100 mean_delay=n/a worst_true_overfill=3.26
cusum replay      false_alarm_runs=0/100 detected=100/100 mean_delay=31.8 worst_true_overfill=3.36
cusum replay+flow false_alarm_runs=0/100 detected=0/100 mean_delay=n/a worst_true_overfill=3.26
```

Lectura de la salida frente a las hipótesis: H1 queda respaldada en el modelo (100/100, retardo 31,8 frente a 0/100); H2 queda respaldada (0 frente a 9 ejecuciones con falsa alarma: la banda estrecha de ±1,5 se dispara con el ruido); H4 se confirma (la clase B evade por completo). El «peor sobrellenado real» es el máximo sobre *toda* la ventana de ataque, así que H3 requiere una medición aparte del sobrellenado en el momento de la alarma, un ejercicio más abajo. Todas las cifras son propiedades de un modelo sintético, no de ninguna planta.

### 3.7 Errores comunes y límites

Afirmar que un mecanismo es novedoso cuando solo lo es su aplicación; omitir la suposición del sensor honesto; elegir las magnitudes de ataque después de ver el comportamiento del detector; no tener ninguna condición en la que la hipótesis falle. Cada uno de estos errores tiene un síntoma visible en una propuesta: una frase de contribución que afirma inventar el CUSUM, un modelo de atacante sin clase B, una ganancia de ataque cambiada después de ejecutar el laboratorio 3 o una lista de hipótesis sin H4. Lea la propuesta buscando esos síntomas antes de enviarla al comité y corríjalos mientras el estudio todavía es barato de cambiar.

### Ejercicios — capítulo 3

- **EX015 — Posicione la contribución del Setpoint Study.** Clasifique el tipo de contribución del Setpoint Study y escriba una declaración de posicionamiento de dos frases que cite el trabajo previo. *Rúbrica:* 3 = comparación respaldada por mediciones + cita Page 1954 y Giraldo et al. 2018; 2 = tipo sin citas; 1 = afirma inventar el CUSUM; 0 = nada.
- **EX016 — Nivel de equilibrio con caudal de entrada adicional.** Derive el nivel de equilibrio del tanque del laboratorio 3 cuando el caudal de entrada es 1,05 y explique qué significa para el objetivo del atacante. *Rúbrica:* 3 = L*=52,5 y el atacante necesita un forzamiento mayor/salida bloqueada; 2 = solo 52,5; 1 = equilibrio erróneo; 0 = nada.
- **EX017 — Atacante de clase C frente a los detectores.** Amplíe la tabla del modelo de atacante con un atacante de clase C que controla la propia lógica del PLC; prediga el resultado para cada detector. *Rúbrica:* 3 = la clase C evade la banda/CUSUM dentro del PLC; un CUSUM externo independiente sigue detectando; 2 = evasión sin el caso externo; 1 = vago; 0 = nada.
- **EX018 — Sobrellenado en el momento de la alarma para H3.** Modifique el laboratorio 3 para registrar el sobrellenado real *en el momento de la alarma* y pruebe H3. *Rúbrica:* 3 = sobrellenado≈1,22 de media/1,60 máximo en la alarma del CUSUM; la banda nunca se dispara; H3 respaldada en esa configuración; 2 = cifras sin H3; 1 = solo cualitativo; 0 = nada.
- **EX019 — Justifique un umbral de retardo para H1.** Justifique un umbral de retardo distinto para H1 usando un nivel de disparo por nivel muy alto declarado y la tasa de sobrellenado. *Rúbrica:* 3 = disparo/margen/tasa → umbral ≈60 pasos con razonamiento; 2 = umbral sin derivación; 1 = número arbitrario; 0 = nada.
- **EX020 — Tres rivales para una ventaja del CUSUM.** Enumere tres explicaciones rivales de una ventaja del CUSUM y la prueba que descartaría cada una. *Rúbrica:* 3 = tres rivales (ajuste, simulación limpia, elección de ganancia) cada uno con una prueba que lo descarta; 2 = rivales sin pruebas; 1 = un rival; 0 = nada.

### Síntesis del capítulo

Una propuesta sólida se posiciona con honestidad, expresa el mecanismo como un invariante físico, hace explícita la suposición del sensor honesto mediante un modelo de atacante y declara de antemano sus hipótesis, incluida la que marca dónde falla la contribución.

### Siga estudiando — capítulo 03 de 08

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Replicación de la línea de base y piloto

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) distinguir reproducción, replicación y reimplementación, (2) diagnosticar por qué no puede reproducirse un resultado publicado de detección en TO, (3) verificar un simulador de procesos antes de confiar en él, (4) diseñar un piloto acotado en una instalación aislada y (5) tomar una decisión de continuar o no continuar declarada de antemano. Toma las hipótesis del capítulo 3 y prepara el estudio principal del capítulo 5.

### 4.1 Términos

La política de distintivos de artefactos de la ACM distingue la **repetibilidad** (mismo equipo, misma configuración), la **reproducibilidad** (otro equipo, mismos artefactos) y la **replicabilidad** (otro equipo, artefactos propios). En TO difieren mucho porque las plantas, los controladores y los conjuntos de datos rara vez pueden compartirse. Fije su vocabulario antes de afirmar cualquiera de ellas. En el Setpoint Study, volver a ejecutar el laboratorio 3 con el mismo código y las mismas semillas es repetibilidad. Un colega que ejecuta el código archivado es reproducibilidad. El trabajo sobre TankBench-21 es una reimplementación a partir de la descripción del artículo, más cercana a la replicación. Decirlo con precisión evita que un revisor lea una nueva puntuación como una confirmación independiente del resultado original.

### 4.2 Diagnóstico de una reproducción fallida: TankBench-21

El banco de pruebas sintético TankBench-21 informa un F1 de 0,96 para una alarma de banda más tasa de cambio. La reimplementación del candidato obtiene 0,31. Un diagnóstico disciplinado enumera hipótesis y prueba cada una: (a) **convención de puntuación**: el artículo usó ajuste por puntos (el laboratorio 1 muestra que esto solo puede explicar una diferencia de este tamaño); (b) **filtración del umbral**: los umbrales se eligieron con la partición de prueba; (c) **alineación de etiquetas**: las etiquetas de ataque empiezan cuando se lanzó el script de ataque, no cuando el proceso se desvió por primera vez; (d) **muestreo**: el artículo submuestreó a 10 s, lo que suaviza el ruido. Volver a puntuar con ajuste por puntos da 0,94, dentro de una tolerancia declarada de antemano de ±0,05, así que la reproducción «tiene éxito», pero tiene éxito en reproducir una métrica inflada. La tesis registra ambas cifras y adopta la exhaustividad por eventos más el retardo.

### 4.3 Verificación del simulador

La verificación pregunta si el modelo está bien construido; la validación pregunta si es el modelo correcto (vocabulario estándar de modelado). Las pruebas de verificación del tanque del laboratorio 3 incluyen: equilibrio en 50,0 con el caudal de entrada nominal (comprobación analítica); conservación de la masa durante 1.000 pasos sin ruido; media del residuo cercana a cero sin ataque; y semillas que producen trazas idénticas en dos máquinas. Un detector evaluado en un simulador no verificado se evalúa en un sistema desconocido. Escriba cada prueba de verificación como código que falle de forma ruidosa y ejecute el conjunto antes de cada lote de experimentos. Si la comprobación del equilibrio falla tras un cambio en el término de caudal de salida, ningún resultado de detector de esa versión es utilizable hasta que la prueba pase. Conserve la salida de las pruebas con los registros de las ejecuciones para que un examinador pueda ver que la verificación precedió a los resultados que respalda.

### 4.4 Ajuste sin filtración: laboratorio 6

El CUSUM tiene dos parámetros, la holgura k y el umbral h. Ajústelos con semillas separadas de las semillas de evaluación y examine la robustez frente al error del modelo. El laboratorio 6 barre k y añade un sesgo constante de calibración del sensor de nivel de 0,4 unidades, un desajuste realista entre el modelo y el instrumento.

```python
# Lab 6 (synthetic): CUSUM drift k vs. false alarms and detection delay - the tuning trade-off reviewers ask about.
import random
def first_alarm(seed, attack, k, h=6.0, steps=600, onset=300, bias=0.0):
    rng = random.Random(seed); true, est, s = 50.0, 50.0, 0.0
    for t in range(steps):
        inflow = 1.0 + rng.gauss(0, 0.05) + (0.05 if attack and t >= onset else 0.0)
        true += inflow - 0.02*true
        lvl = true + rng.gauss(0, 0.3) + bias
        if attack and t >= onset: lvl = 50.0 + rng.gauss(0, 0.3) + bias
        est += inflow + rng.gauss(0, 0.02) - 0.02*est
        s = max(0.0, s + abs(lvl - est) - k)
        if s > h: return t
    return None
for bias in (0.0, 0.4):
    for k in (0.4, 0.6, 0.8, 1.0):
        fa = sum(first_alarm(i, False, k, bias=bias) is not None for i in range(100))
        d = [a-300 for a in (first_alarm(i, True, k, bias=bias) for i in range(100)) if a is not None and a >= 300]
        print(f"bias={bias} k={k} false_alarm_runs={fa}/100 detected={len(d)}/100 mean_delay={sum(d)/len(d) if d else float('nan'):.1f}")
```

Salida esperada:

```text
bias=0.0 k=0.4 false_alarm_runs=0/100 detected=100/100 mean_delay=25.6
bias=0.0 k=0.6 false_alarm_runs=0/100 detected=100/100 mean_delay=30.9
bias=0.0 k=0.8 false_alarm_runs=0/100 detected=100/100 mean_delay=38.0
bias=0.0 k=1.0 false_alarm_runs=0/100 detected=100/100 mean_delay=46.1
bias=0.4 k=0.4 false_alarm_runs=97/100 detected=19/100 mean_delay=35.4
bias=0.4 k=0.6 false_alarm_runs=4/100 detected=99/100 mean_delay=46.1
bias=0.4 k=0.8 false_alarm_runs=0/100 detected=100/100 mean_delay=55.6
bias=0.4 k=1.0 false_alarm_runs=0/100 detected=100/100 mean_delay=66.5
```

Con un modelo perfecto, la k más pequeña parece la mejor. Un pequeño sesgo de calibración vuelve inútil k = 0,4: 97 ejecuciones alarman antes de que empiece el ataque y solo 19 alarmas caen después del inicio. La elección defendible es k = 0,8, que cambia unos 7 pasos de retardo (frente a k = 0,6 sin sesgo) por robustez. Este es el tipo de resultado que los revisores esperan ver *antes* del estudio principal.

### 4.5 Un piloto acotado en el banco de pruebas T2

El piloto responde solo preguntas de viabilidad: ¿puede la instalación ejecutar el escenario de repetición de forma segura?, ¿puede el historiador registrar a 1 Hz? y ¿detiene la válvula de flotador el desbordamiento? Los datos del piloto no se usan para pruebas de hipótesis. Los criterios de continuar o no continuar se escriben de antemano: continuar si tres ejecuciones consecutivas se completan sin que nunca se alcance la válvula de flotador, con una pérdida de registros inferior al 1 % y sin ningún reinicio no planificado del controlador; en caso contrario, revisar. El plan del piloto también registra quién puede detener una ejecución y cómo (una parada de emergencia física que corta la alimentación de la bomba, independiente del PLC).

### 4.6 Errores comunes y límites

Llamar replicación a una nueva puntuación; confiar en un simulador porque «parece correcto»; ajustar con semillas de evaluación; usar datos del piloto para probar hipótesis; carecer de una parada de emergencia independiente. Cada error permite que un resultado parezca mejor de lo que es. Una nueva puntuación con ajuste por puntos solo confirma que se usó la convención original. Una traza de aspecto plausible no es una prueba de verificación superada. Las semillas compartidas entre el ajuste y la evaluación filtran información. Las ejecuciones piloto responden a la viabilidad, no a las hipótesis. Y sin una parada física que corte la alimentación de la bomba de forma independiente del PLC, el piloto no está acotado.

### Ejercicios — capítulo 4

- **EX021 — Términos de repetibilidad de la ACM.** Clasifique tres actividades (volver a ejecutar su propio laboratorio 3, un colega que ejecuta su archivo, un colega que construye su propio modelo de tanque) según los términos de la ACM. *Rúbrica:* 3 = repetibilidad / reproducibilidad / replicabilidad asignadas correctamente; 2 = dos correctas; 1 = una; 0 = nada.
- **EX022 — Registro de reproducción de TankBench-21.** Escriba una entrada del registro de reproducción de TankBench-21 con las cuatro hipótesis, pruebas y resultados. *Rúbrica:* 3 = cuatro hipótesis con pruebas/resultados, incluido ajuste por puntos→0,94; 2 = hipótesis sin resultados; 1 = parcial; 0 = nada.
- **EX023 — Prueba de verificación de la conservación de la masa.** Escriba y ejecute una prueba de verificación de la conservación de la masa en el modelo sin ruido del laboratorio 3. *Rúbrica:* 3 = equilibrio sin ruido≈50 y comprobación de la identidad entrada−salida; 2 = solo el equilibrio; 1 = vago; 0 = nada.
- **EX024 — Elija k con sesgo de calibración.** Usando el laboratorio 6, elija k para una planta en la que se espera un sesgo de calibración de hasta 0,4 y justifíquelo con dos cifras. *Rúbrica:* 3 = k=0,8 con 0/100 FA frente a k=0,6 con 4/100 FA y el compromiso de retardo; 2 = elección de k sin ambas cifras; 1 = solo k; 0 = nada.
- **EX025 — Criterios de continuar o no continuar del piloto en T2.** Escriba criterios de continuar o no continuar para un piloto en T2 que incluyan un criterio de seguridad y uno de calidad de datos. *Rúbrica:* 3 = seguridad (válvula de flotador), datos (<1 % de pérdida), reinicio, prueba previa de la parada de emergencia; 2 = falta uno; 1 = continuar vago; 0 = nada.
- **EX026 — Por qué el 0,94 reproducido no indica calidad.** Explique por qué el 0,94 reproducido no es evidencia de que el detector de TankBench-21 sea bueno. *Rúbrica:* 3 = puntuación con ajuste por puntos ≠ rendimiento en retardo/FA/turno + posible ajuste con el conjunto de prueba; 2 = una razón; 1 = «demasiado alto»; 0 = nada.

### Síntesis del capítulo

Reproduzca las líneas de base con una tolerancia declarada de antemano y diagnostique las diferencias de forma sistemática; verifique el simulador; ajuste con semillas separadas y someta el resultado a pruebas de estrés frente al error del modelo; y pilote solo para la viabilidad, con una autoridad de parada física independiente.

### Siga estudiando — capítulo 04 de 08

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Estudio principal y validación independiente

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) diseñar un experimento pareado con números aleatorios comunes, (2) informar una incertidumbre que separe el ruido de la simulación de la incertidumbre del modelo, (3) validar en un segundo contexto independiente, (4) incorporar una revisión ciega por parte de operadores y (5) escribir un párrafo de resultados honesto, incluidos los resultados mixtos. Ejecuta el plan pilotado en el capítulo 4 y produce las afirmaciones que el capítulo 6 atacará.

### 5.1 Diseño pareado

Al comparar dos configuraciones de detector, ejecute ambas con las **mismas** semillas aleatorias (números aleatorios comunes, que es una técnica de simulación estándar). La diferencia por semilla elimina el ruido compartido y estrecha los intervalos de confianza. El laboratorio 5 compara k = 0,8 con k = 0,6 en dos variantes de planta: la planta A, con una ganancia de caudal de entrada del ataque de 0,05, y la planta B, un tanque mayor en el que la misma manipulación de la bomba produce solo 0,02 unidades por paso.

```python
# Lab 5 (synthetic): paired comparison of detection delay on two plant models with common random numbers + bootstrap CI.
import random
def delay(seed, k, gain):
    rng = random.Random(seed); true, est, s = 50.0, 50.0, 0.0
    for t in range(700):
        inflow = 1.0 + rng.gauss(0, 0.05) + (gain if t >= 300 else 0.0)
        true += inflow - 0.02*true
        lvl = 50.0 + rng.gauss(0, 0.3) if t >= 300 else true + rng.gauss(0, 0.3)
        est += inflow + rng.gauss(0, 0.02) - 0.02*est
        s = max(0.0, s + abs(lvl - est) - k)
        if s > 6.0 and t >= 300: return t - 300
    return 400
for plant, gain in (("A", 0.05), ("B", 0.02)):
    diffs = [delay(i, 0.8, gain) - delay(i, 0.6, gain) for i in range(200)]
    rng = random.Random(7); boots = sorted(sum(rng.choice(diffs) for _ in diffs)/len(diffs) for _ in range(2000))
    print(f"plant {plant}: mean delay(k=0.8)-delay(k=0.6)={sum(diffs)/len(diffs):.1f} steps, 95% CI [{boots[50]:.1f}, {boots[1949]:.1f}]")
```

Salida esperada:

```text
plant A: mean delay(k=0.8)-delay(k=0.6)=6.9 steps, 95% CI [6.5, 7.4]
plant B: mean delay(k=0.8)-delay(k=0.6)=45.4 steps, 95% CI [38.4, 53.0]
```

La robustez elegida en el capítulo 4 cuesta unos 7 pasos en la planta A, pero unos 45 pasos en la planta B, donde la señal del ataque es más débil. Las ejecuciones no detectadas se limitan a 400 pasos (censura por la derecha); por tanto, la media de la planta B es una cota inferior del coste real. El intervalo bootstrap describe solo el ruido de la simulación: no dice nada sobre si el modelo del tanque representa alguna planta real.

### 5.2 Tres tipos de incertidumbre

Separe la incertidumbre **estocástica** (variación de una semilla a otra, recogida por el intervalo), la incertidumbre **paramétrica** (coeficiente del orificio, niveles de ruido, sesgo de calibración, explorada mediante análisis de sensibilidad como en el laboratorio 6) y la incertidumbre **estructural** (¿es un balance de masa de un solo tanque el modelo correcto?). Solo el segundo banco de pruebas aborda la tercera. En el Setpoint Study, el intervalo del laboratorio 5 cubre solo el primer tipo. El laboratorio 6 cubre parte del segundo, mediante el sesgo de calibración y la holgura. El banco de pruebas T2 es la primera evidencia sobre el tercero, y su menor exhaustividad muestra que el caudalímetro honesto y sin retardo del modelo era demasiado simple. Informe cada tipo en su propio lugar para que los lectores no confundan uno con otro.

### 5.3 Validación independiente en el banco de pruebas T2

T2 difiere del modelo de la planta A en aspectos que importan: dos tanques acoplados, un caudalímetro distinto con su propio retardo y un ciclo de barrido del PLC de 100 ms. Los umbrales se congelan a partir del ajuste en la planta A antes de examinar cualquier dato de T2; de lo contrario, la validación sería otro ejercicio de ajuste. Resultados sintéticos de T2: la repetición de clase A se detectó en 18 de 20 episodios (dos no detectados porque el retardo del caudalímetro ocultó manipulaciones pequeñas), una mediana de retardo mayor que en la simulación, cero falsas alarmas en 40 horas nominales y la evasión de clase B confirmada en los 10 ensayos. El estudio respalda así H1 con una salvedad (menor exhaustividad con un instrumento con retardo) y confirma H4.

### 5.4 La revisión ciega por parte de operadores

Diez operadores sintéticos (O01–O10) revisaron cronologías de alarmas sin saber qué detector las había producido. Ocho prefirieron la alarma del CUSUM porque llegaba con una tendencia del residuo que podían interpretar; dos encontraron abstracto un «residuo» y querían que se mostrara en la HMI el nivel predicho. El hallazgo trata de la interpretabilidad, no de la exactitud de la detección, y cambia el diseño: la tesis recomienda mostrar el nivel predicho frente al informado. Diez participantes no pueden respaldar una afirmación estadística sobre poblaciones de operadores, y el estudio no la hace. La revisión muestra que la interpretabilidad es una cuestión de diseño que vale la pena medir más adelante con personal real de salas de control que dé su consentimiento. Registre el protocolo, el método de cegamiento y la razón declarada por cada operador, de modo que la recomendación pueda rastrearse hasta lo que se dijo y no hasta un recuento.

### 5.5 Redacción honesta de resultados mixtos

«En el modelo sintético de la planta A y en el banco de pruebas sintético T2, un CUSUM de residuos de balance de masa detectó ataques de repetición de sensores de clase A que una alarma de banda de ±1,5 no detectó, sin ejecuciones con falsa alarma en operación nominal. La exhaustividad cayó del 100 % en la simulación al 90 % en T2 debido al retardo del caudalímetro. La robustez frente a un sesgo de calibración de 0,4 unidades exigió una holgura mayor, que alargó el retardo de detección unos 7 pasos en la planta A y al menos 45 en la planta B, de señal más débil. Cuando el atacante controlaba también el caudalímetro (clase B), la detección falló en todos los ensayos, como se había predicho».

### 5.6 Errores comunes y límites

Semillas independientes en comparaciones pareadas; ajuste en el banco de pruebas de validación; ocultar ejecuciones censuradas; presentar los intervalos como incertidumbre del mundo real; omitir la condición de fallo en el resumen. Cada punto tiene una comprobación concreta en este estudio: el laboratorio 5 usa números aleatorios comunes, los umbrales de T2 se congelan a partir del ajuste en la planta A, las ejecuciones limitadas se informan como censuradas en 400 pasos, el intervalo bootstrap se etiqueta como ruido de la simulación y el resumen indica que la clase B evadió la detección en todos los ensayos. Un revisor debería poder confirmar cada comprobación a partir del archivo.

### Ejercicios — capítulo 5

- **EX027 — Semillas independientes frente a pareadas.** Vuelva a ejecutar el laboratorio 5 con semillas independientes para las dos configuraciones y compare la anchura de los intervalos con la versión pareada. *Rúbrica:* 3 = anchura no pareada en la planta A≈3,2 frente a pareada≈0,9 y comparación de la planta B; 2 = solo la dirección; 1 = dirección errónea; 0 = nada.
- **EX028 — Seis fuentes de incertidumbre clasificadas.** Clasifique seis fuentes de incertidumbre del Setpoint Study como estocásticas, paramétricas o estructurales. *Rúbrica:* 3 = estocástica/paramétrica/estructural con dos ejemplos de cada clase; 2 = clases sin ejemplos; 1 = una clase; 0 = nada.
- **EX029 — Regla de congelación antes de la validación en T2.** Escriba la regla de congelación de los umbrales antes de la validación en T2 y explique qué invalidaría la validación. *Rúbrica:* 3 = congelar k=0,8 h=6 con hash antes de cargar T2 + qué invalida; 2 = congelación sin invalidación; 1 = vago; 0 = nada.
- **EX030 — Censura por la derecha en la planta B.** Explique cómo sesga la censura por la derecha la media de la planta B y proponga un resumen mejor. *Rúbrica:* 3 = media como cota inferior + informar la proporción de detección/mediana entre los detectados o estilo KM; 2 = sesgo sin resumen mejor; 1 = vago; 0 = nada.
- **EX031 — De la revisión de operadores a diseño y límite.** Convierta el hallazgo de la revisión de operadores en una recomendación de diseño y una limitación. *Rúbrica:* 3 = mostrar predicho frente a informado en la HMI + límite de operadores sintéticos; 2 = una de las dos; 1 = vago; 0 = nada.
- **EX032 — Párrafo de resultados cuando H1 falla en T2.** Escriba un párrafo de resultados de 120 palabras para un estudio en el que H1 falló en T2. *Rúbrica:* 3 = ~120 palabras con T2 9/20 frente a simulación 100/100 y explicación de retardo/holgura; 2 = cifras sin el retardo; 1 = breve nota de fallo; 0 = nada.

### Síntesis del capítulo

Los diseños pareados afinan las comparaciones; la incertidumbre tiene tres tipos y los intervalos recogen solo uno; validar significa umbrales congelados en un contexto independiente; y un párrafo de resultados honesto lleva consigo sus salvedades y su condición de fallo.

### Siga estudiando — capítulo 05 de 08

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Crítica de pares y revisión

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) organizar una revisión interna de equipo rojo de sus propias afirmaciones, (2) convertir objeciones en hipótesis comprobables, (3) caracterizar las condiciones límite en lugar de ocultarlas, (4) realizar una revisión de doble uso de un artículo antes de enviarlo y (5) escribir una carta de respuesta a los revisores que responda de verdad. Ataca los resultados del capítulo 5 y alimenta el argumento de la tesis del capítulo 7.

### 6.1 Las objeciones como hipótesis

Invite a dos colegas —idealmente un ingeniero de control y un investigador de seguridad ofensiva— a atacar las afirmaciones. Registre cada objeción como una hipótesis con una prueba:

| Objeción (equipo rojo) | Hipótesis | Prueba | Resultado (sintético) |
|---|---|---|---|
| «Su atacante es ingenuo: un atacante inteligente sube lentamente». | Una rampa lenta por debajo de la holgura del CUSUM evade la detección y aun así provoca sobrellenado. | Barrer la ganancia del ataque de 0,005 a 0,05. | La ganancia 0,005 se detecta solo en 14/100 ejecuciones y la de 0,01 en 55/100, pero el peor sobrellenado en la ventana de 300 pasos se queda en 1,12 y 1,37 unidades, frente a 3,36 con ganancia 0,05: el argumento de acotación del impacto de Urbina et al. |
| «El caudalímetro es solo otra entrada del PLC». | Si el medidor está cableado al mismo PLC que el sensor de nivel, la clase B es tan fácil como la clase A. | Inspeccionar el cableado de T2 y el diseño de la planta A. | En T2 ambos pasan por un mismo PLC; la suposición del sensor honesto solo se cumple con un medidor cableado por separado. |
| «Los operadores notarían que la bomba está en marcha». | La visualización del estado de la bomba revela el ataque. | Revisar el diseño de la HMI. | Solo si el estado de la bomba procede de un contacto independiente, no del valor comandado. |
| «Los resultados dependen del nivel de ruido». | Un mayor ruido del sensor aumenta las falsas alarmas con k fija. | Laboratorio 6 con el ruido duplicado. | Requiere reajuste; se informa como sensibilidad paramétrica. |

La segunda objeción es la más importante: revela que la fortaleza de la defensa es una propiedad **arquitectónica** (rutas de medición independientes), no algorítmica. La afirmación de la tesis se revisa en consecuencia.

### 6.2 Condiciones límite

Una buena tesis traza dónde funciona el método. En el Setpoint Study los límites son: (1) debe existir una segunda medición independiente de la misma física y estar fuera del control del atacante; (2) el error del modelo debe ser menor que la señal del ataque; (3) los ataques más lentos que la holgura pueden evadir, pero su impacto dentro de un horizonte declarado está acotado (en el modelo, ≤1,37 unidades de sobrellenado en 300 pasos para ganancias ≤0,01). Se enuncian en el resumen, no se entierran en una sección de limitaciones.

Cada límite debe enunciarse con la evidencia que lo mide: la inspección del cableado de T2 para el primero, el barrido del sesgo de calibración del laboratorio 6 para el segundo y el barrido de la ganancia del ataque de la revisión de equipo rojo para el tercero.

### 6.3 La afirmación acotada

Antes: «El CUSUM basado en la física detecta la manipulación de sensores en plantas de agua». Después: «Donde un sensor cableado de forma independiente mide una magnitud vinculada por un balance de masa conocido, un CUSUM de residuos con una holgura ajustada al error de calibración esperado detecta ataques de repetición sobre un solo sensor que las alarmas de banda no detectan, y acota el sobrellenado alcanzable por ataques más lentos; no ofrece protección cuando el atacante controla ambas rutas de medición». La afirmación acotada es más débil en alcance y mucho más sólida en evidencia.

Conserve en la tesis las versiones de antes y de después, para que los lectores vean cómo la crítica cambió el argumento. Contraste cada frase posterior con la afirmación acotada: un resumen o una conclusión que vuelva a derivar hacia las plantas de agua en general deshace el trabajo. La afirmación acotada también da a los operadores una prueba directa sobre su propio sitio: ¿está la segunda medición cableada de forma independiente?

### 6.4 Revisión de doble uso

Antes de enviar el artículo, pregunte: ¿ofrece el artículo una receta para la evasión de clase B contra un producto concreto? (No: describe la clase de capacidad, que ya está documentada como manipulación de la vista). ¿Revela la configuración de T2? (Solo la estructura genérica). ¿Ganaría más un defensor que un atacante? (Sí: la recomendación arquitectónica —rutas de medición independientes— es aplicable para los defensores y bien conocida por los atacantes capaces). Registre las respuestas en el apéndice de la tesis. Pida a un revisor ajeno al proyecto que responda las mismas preguntas sin ver sus respuestas y registre cualquier desacuerdo y cómo se resolvió. Si un trabajo posterior encuentra un fallo específico de un producto, como un PLC que acepta escrituras que debería rechazar, la revisión se repite y la divulgación se gestiona mediante el proceso coordinado antes de publicar.

### 6.5 Respuesta a los revisores

Responda a cada punto, cítelo, indique qué cambió y dónde, y discrepe con evidencia cuando deba hacerlo. Ejemplo: «El revisor 2 afirma que el CUSUM no es novedoso. Estamos de acuerdo y hemos revisado el §1 para posicionar la contribución como una medición de cuándo los invariantes entre sensores ayudan frente a la manipulación de la vista, citando a Page (1954) y Giraldo et al. (2018). La nueva declaración de contribución está en la p. 3». Mantenga una tabla con una fila por cada punto del revisor: la cita, su respuesta, el cambio realizado y su ubicación. Cuando discrepe, cite el resultado medido, como que la clase B evadió la detección en todos los ensayos, en lugar de reafirmar su opinión. Envíe la tabla con el manuscrito revisado para que el editor pueda comprobar cada cambio.

### 6.6 Errores comunes y límites

Defender en lugar de probar; ocultar el fallo frente a la clase B; afirmar generalidad entre plantas después de dos contextos; responder a los revisores sin indicar los cambios. Cada error convierte la crítica en defensa. Responda a la objeción de la rampa lenta con el barrido de ganancias, no con palabras tranquilizadoras. Ponga la clase B en el resumen. Limite la generalidad a los dos contextos medidos, el modelo de la planta A y el banco de pruebas T2. En las cartas a los revisores, indique qué cambió y dónde, para que un lector pueda verificar la revisión en lugar de confiar en la afirmación. Conserve la tabla de objeciones en la tesis.

### Ejercicios — capítulo 6

- **EX033 — La objeción del sobreajuste como prueba.** Convierta la objeción «su umbral está sobreajustado» en una hipótesis y una prueba. *Rúbrica:* 3 = hipótesis de caída con semillas no vistas/T2 + ajustar con 0–99 / evaluar con 1000–1099 y T2; 2 = hipótesis sin protocolo; 1 = reformula la objeción; 0 = nada.
- **EX034 — Barrido de la ganancia del ataque para el CUSUM.** Modifique el laboratorio 3 para barrer la ganancia del ataque (0,005, 0,01, 0,02, 0,05) para el CUSUM e informe la detección y el peor sobrellenado. *Rúbrica:* 3 = cuatro ganancias con recuentos de detección, retardos y peor sobrellenado coincidentes con el barrido del laboratorio; 2 = dos ganancias; 1 = cualitativo; 0 = nada.
- **EX035 — Párrafo de límites para el resumen.** Escriba el párrafo de condiciones límite para el resumen en ≤ 80 palabras. *Rúbrica:* 3 = ≤80 palabras: segunda medición independiente, error del modelo < ataque, ataques lentos ≤1,37 de sobrellenado; 2 = límites sin cifras; 1 = afirmación excesiva; 0 = nada.
- **EX036 — Acote la afirmación sobre los servicios de agua.** Reescriba la afirmación «el método protege los servicios de agua» como una afirmación acotada. *Rúbrica:* 3 = dos contextos sintéticos + caudal independiente + fallo frente a la clase B; 2 = acotada, pero todavía «servicios»; 1 = edición menor; 0 = afirmación original.
- **EX037 — Doble uso de la secuencia exacta de falsificación en T2.** Realice una revisión de doble uso sobre la publicación de la secuencia exacta de falsificación del caudalímetro usada en T2. *Rúbrica:* 3 = publicar clase+defensa; secuencia exacta de T2 solo mediante divulgación coordinada/fabricante; 2 = retener sin vía; 1 = publicar todo; 0 = nada.
- **EX038 — Respuesta sobre la representatividad del banco de pruebas.** Escriba una respuesta a un revisor ante «Los resultados del banco de pruebas no son representativos de plantas reales». *Rúbrica:* 3 = acepta la diferencia, remite a las afirmaciones acotadas + umbrales congelados en T2 + riesgo residual; 2 = acepta sin remitir a la evidencia; 1 = desestima; 0 = nada.

### Síntesis del capítulo

La crítica es un dato: convierta las objeciones en pruebas, deje que acoten la afirmación, publique las condiciones límite en un lugar destacado y revise el doble uso antes de enviar. La objeción más valiosa aquí convirtió una afirmación algorítmica en una arquitectónica.

### Siga estudiando — capítulo 06 de 08

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Síntesis de la tesis y archivo de reproducibilidad

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) trazar el argumento de la tesis desde la evidencia hasta la afirmación, (2) elegir un formato de tesis, (3) construir un archivo por niveles, verificado con hashes, que falle de forma cerrada, (4) documentar datos y modelos sintéticos y (5) escribir limitaciones que digan en qué dirección empuja cada sesgo. Reúne los capítulos 1–6 y prepara la defensa.

### 7.1 Mapa del argumento

Use una estructura de Toulmin: **afirmación** (la afirmación acotada del §6.3), **datos** (resultados del laboratorio 3, del laboratorio 5 y de T2), **garantía** (el balance de masa vincula caudal y nivel; un atacante que controla solo uno no puede mantener ambos coherentes), **respaldo** (pruebas de verificación, propiedades del CUSUM de Page), **calificador** («en dos contextos sintéticos») y **refutación** (clase B, rampas lentas, instrumentos con retardo). Cada elemento remite a un capítulo y a un artefacto. Dibuje el mapa en una página y compruebe cada flecha: ¿respaldan realmente los datos citados la garantía, y enumera la refutación todos los límites del capítulo de crítica? Un elemento sin ningún artefacto detrás es una laguna que debe cerrarse antes de la defensa. Mantenga el mapa actualizado a medida que cambie la redacción, porque los examinadores suelen preguntar cómo se conecta una sola frase con la evidencia.

### 7.2 Formato

Una monografía se adapta a un único argumento integrado; una tesis por compendio de publicaciones se adapta a artículos independientes con un capítulo de enlace. En cualquier caso, el archivo de reproducibilidad pertenece a la tesis, no a un artículo. En el Setpoint Study, una tesis por compendio de publicaciones se corresponde de forma natural con los tres artículos previstos, y el capítulo de enlace lleva la afirmación acotada y las condiciones límite. Una monografía situaría el mismo material en un argumento continuo. Elija pronto con su comité, porque la elección cambia cuánta repetición es aceptable y cómo se acredita el trabajo en coautoría.

### 7.3 Archivo por niveles

Los artefactos de TO conllevan riesgos distintos entre sí. El código y el simulador sintético son T0 (públicos). Las trazas sintéticas son T1. Las configuraciones del banco de pruebas son T2 (solo para investigadores verificados). Los mapas derivados de plantas son T3 y nunca se publican. Una publicación debe **fallar de forma cerrada**: si el hash de cualquier archivo difiere del manifiesto, no se publica nada; los archivos por encima del nivel de publicación se excluyen automáticamente. El laboratorio 7 demuestra esta lógica.

```python
# Lab 7: fail-closed reproducibility manifest check (stdlib). Creates synthetic files in ./archive_demo.
import hashlib, json, os
os.makedirs("archive_demo", exist_ok=True)
files = {"lab3.py": "print('model')\n", "traces_T1.csv": "t,level\n0,50.0\n", "plant_map_T3.txt": "RESTRICTED\n"}
for n, c in files.items():
    open(os.path.join("archive_demo", n), "w").write(c)
manifest = [{"path": n, "tier": "T3" if n.startswith("plant_map") else "T1",
             "sha256": hashlib.sha256(c.encode()).hexdigest()} for n, c in files.items()]
manifest[1]["sha256"] = "0"*64          # simulate a stale hash after an edit
def check(release_tier_max="T1"):
    ok = True
    for e in manifest:
        h = hashlib.sha256(open(os.path.join("archive_demo", e["path"]), "rb").read()).hexdigest()
        if e["tier"] > release_tier_max:
            print("EXCLUDE (tier)", e["path"], e["tier"]); continue
        if h != e["sha256"]:
            print("FAIL (hash)   ", e["path"]); ok = False
        else:
            print("OK            ", e["path"])
    return ok
print("release allowed:", check())
```

Salida esperada:

```text
OK             lab3.py
FAIL (hash)    traces_T1.csv
EXCLUDE (tier) plant_map_T3.txt T3
release allowed: False
```

El hash desactualizado bloquea la publicación y el archivo T3 nunca se considera. La comparación `e["tier"] > release_tier_max` funciona porque los nombres de nivel se ordenan lexicográficamente T0 < T1 < T2 < T3, una comodidad que dejaría de funcionar con un nivel llamado "T10", lo cual se anota en el README del archivo.

### 7.4 Documentación de datos y modelos sintéticos

Indique para cada conjunto de datos sintético si es **inventado** (parámetros elegidos para la enseñanza) o **calibrado** (ajustado a las estadísticas de un sistema real). El tanque del Setpoint Study es inventado. Registre los parámetros, las semillas, la versión del código generador y el uso previsto; advierta contra su uso para hacer afirmaciones sobre plantas reales. Escriba esta documentación como una ficha de datos breve almacenada con el código generador, e incluya el equilibrio, el coeficiente del orificio de 0,02, los niveles de ruido y las ganancias del ataque. Nombre los laboratorios que usaron cada configuración. Cualquiera que reutilice las trazas debería ver de inmediato que describen un modelo didáctico, no mediciones de Kestrel ni de ninguna otra planta.

### 7.5 Limitaciones con dirección

Una tabla de limitaciones útil indica la dirección de cada sesgo: caudalímetro sin ruido en la simulación (*sobrestima* la exhaustividad, confirmado por T2), modelo de un solo lazo (dirección *desconocida* para plantas de varios lazos), operadores sintéticos (*desconocida*), escala del banco de pruebas (*probablemente sobrestima* la relación señal/ruido), censura en 400 pasos (*subestima* el coste en retardo de la planta B). La dirección importa porque indica al lector cómo ajustar su confianza. Si un sesgo sobrestima la exhaustividad, la cifra del mundo real probablemente es menor; si es desconocida, el lector no debe suponer nada en ningún sentido. Mantenga la tabla junto a los resultados y no al final, y actualícela cuando una nueva evidencia, como la menor exhaustividad de T2, determine una dirección.

### 7.6 Errores comunes y límites

Archivos que publican todo o nada; manifiestos sin comprobar; llamar «realistas» a datos inventados; limitaciones sin dirección. Un archivo que publica todo filtra detalles de nivel de planta; uno que no publica nada no puede comprobarse. Un manifiesto que nunca se verifica da una falsa tranquilidad, y por eso el laboratorio 7 falla de forma cerrada. Los datos sintéticos deben llamarse inventados o calibrados, nunca realistas. Y cada limitación debe decir si empuja los resultados hacia arriba, hacia abajo o en una dirección desconocida. Ejecute la comprobación del manifiesto sobre la copia de publicación, nunca solo sobre el directorio de trabajo.

### Ejercicios — capítulo 7

- **EX039 — Mapa de Toulmin de la afirmación acotada.** Dibuje (como tabla) el mapa de Toulmin de la afirmación acotada con referencias a los capítulos. *Rúbrica:* 3 = afirmación/datos/garantía/respaldo/calificador/refutación con referencias a capítulos; 2 = falta un elemento en el mapa; 1 = solo la afirmación; 0 = nada.
- **EX040 — Corrija la comparación de niveles del laboratorio 7.** Corrija el laboratorio 7 para que los niveles se comparen numéricamente y añada un caso de prueba T10. *Rúbrica:* 3 = comparación con int(tier[1:]) + T10 frente a T1 se excluye; 2 = corrección con int sin T10; 1 = nota sobre la ordenación de cadenas; 0 = nada.
- **EX041 — Niveles de ocho artefactos del Setpoint Study.** Asigne niveles a ocho artefactos del Setpoint Study y justifique dos elecciones dudosas. *Rúbrica:* 3 = ocho artefactos con niveles + dos justificaciones de casos dudosos; 2 = niveles sin casos dudosos; 1 = cuatro artefactos; 0 = nada.
- **EX042 — Ficha del conjunto de datos del simulador del laboratorio 3.** Escriba una ficha del conjunto de datos para el simulador del laboratorio 3 (propósito, parámetros, inventado/calibrado, usos prohibidos). *Rúbrica:* 3 = propósito, parámetros, condición de inventado, usos prohibidos; 2 = falta un campo; 1 = solo el propósito; 0 = nada.
- **EX043 — Dos limitaciones con dirección más.** Añada dos filas a la tabla de limitaciones con dirección. *Rúbrica:* 3 = dos filas con dirección (*desconocida*/*sobrestima*, etc.); 2 = una fila; 1 = sin dirección; 0 = nada.
- **EX044 — Monografía frente a compendio de publicaciones.** Argumente a favor del formato de monografía o de compendio de publicaciones para el Setpoint Study. *Rúbrica:* 3 = elige formato con la razón de la correspondencia con tres artículos o del argumento integrado; 2 = elección sin razón; 1 = vago; 0 = nada.

### Síntesis del capítulo

La tesis es un argumento en el que cada elemento remite a evidencia; el archivo publica solo lo que es seguro y está verificado, fallando de forma cerrada; los datos sintéticos se etiquetan como inventados o calibrados; y las limitaciones dicen en qué sentido sesgan el resultado.

### Siga estudiando — capítulo 07 de 08

[← Capítulo 06 (borrador)](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 (borrador) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Defensa y plan de publicación

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) auditar un registro de afirmaciones antes de la defensa, (2) prepararse para las familias de preguntas de los examinadores, (3) secuenciar las publicaciones, (4) canalizar las vulnerabilidades de productos mediante la divulgación coordinada y (5) traducir los hallazgos para los operadores y los organismos de normalización. Completa el proyecto iniciado en el capítulo 1.

### 8.1 Auditoría del registro de afirmaciones

Cada afirmación de la tesis necesita evidencia, alcance y un falsador, y debe evitar una redacción excesiva. El laboratorio 8 automatiza la primera pasada.

```python
# Lab 8: audit a thesis claim register (synthetic). Every claim needs evidence, scope and a falsifier.
claims = [
 {"id": "C1", "text": "Residual CUSUM detects replay on Plant A tank model", "evidence": "Lab3 100/100", "scope": "simulated tank, single-sensor replay", "falsifier": "replay+flow"},
 {"id": "C2", "text": "Method secures water utilities", "evidence": "", "scope": "", "falsifier": ""},
 {"id": "C3", "text": "Band alarms miss replay", "evidence": "Lab3 0/100", "scope": "band +/-1.5", "falsifier": ""},
 {"id": "C4", "text": "Detection holds on testbed T2", "evidence": "Ch5 table 5.2", "scope": "T2, class A replay", "falsifier": "class B: flow meter also spoofed"},
]
overreach = ("secures", "prevents all", "guarantees", "real-world")
for c in claims:
    issues = [f for f in ("evidence", "scope", "falsifier") if not c[f]]
    if any(w in c["text"].lower() for w in overreach): issues.append("overreach wording")
    print(c["id"], "PASS" if not issues else "REVISE: " + ", ".join(issues))
```

Salida esperada:

```text
C1 PASS
C2 REVISE: evidence, scope, falsifier, overreach wording
C3 REVISE: falsifier
C4 PASS
```

C2 debe eliminarse o acotarse; C3 necesita un falsador (por ejemplo, «una banda lo bastante estrecha para captar la repetición superaría el presupuesto de falsas alarmas por turno»). Una lista de palabras clave es una comprobación tosca; la auditoría humana sigue leyendo cada afirmación.

La lista de palabras clave del laboratorio 8 es deliberadamente corta, así que superarla demuestra poco. Una auditoría humana debería contrastar igualmente C4 con los resultados de T2: su alcance es la repetición de clase A porque la clase B evadió la detección en T2, y la exhaustividad de 18 de 20 debe figurar junto a la afirmación, no solo en el capítulo de resultados. Repita la auditoría después de cada revisión del resumen o de la conclusión, y conserve la salida de cada ejecución en el historial del registro de afirmaciones para que los examinadores puedan ver cómo se acotaron las afirmaciones.

### 8.2 Familias de preguntas de los examinadores

Prepare respuestas para: **posicionamiento** («¿qué hay de nuevo más allá de Page y Giraldo?»), **validez** («¿por qué debería generalizarse un banco de pruebas?»), **adversario** («¿qué hace un atacante más fuerte?»), **seguridad física** («¿cómo acotó los experimentos en T2?»), **ética** («¿qué retuvo y por qué?») e **impacto** («¿qué debería cambiar un operador el lunes?»). La respuesta a la última es arquitectónica: disponer de una segunda medición cableada de forma independiente de las magnitudes clave del proceso y mostrar los valores predichos frente a los informados.

Ensaye cada familia en voz alta con un colega que interrumpa, y mantenga una hoja con una respuesta breve y una referencia a la figura o tabla que la respalda. Cuando no sepa algo, diga qué evidencia respondería a la pregunta y qué tiene realmente. Responda a la pregunta formulada y luego deténgase.

### 8.3 Secuenciación de las publicaciones

Artículo 1: la contribución de metodología de evaluación (impacto en el momento de la detección y métricas por eventos, con la lección de la reproducción al estilo de TankBench-21 contada de forma genérica). Artículo 2: la comparación del Setpoint Study con las condiciones límite. Artículo 3: el hallazgo sobre la interpretabilidad para los operadores, con colaboradores de factores humanos. Publique el archivo T0/T1 con el artículo 2. Planifique cada artículo de modo que no contradiga la tesis ni los demás artículos, y registre qué afirmaciones y figuras reutiliza cada uno. Si el artículo sobre operadores se retrasa por la revisión de factores humanos, los otros dos pueden aparecer igualmente; el archivo se publica con el artículo 2 porque es el artículo cuyas cifras reproduce. Acuerde la autoría con los colaboradores antes de empezar a escribir.

### 8.4 Divulgación coordinada

Si la investigación revela una vulnerabilidad en un producto comercial —por ejemplo, un PLC que acepta escrituras no autenticadas en un registro que debería ser de solo lectura—, comuníquela al fabricante y, cuando corresponda, a un coordinador como el programa de divulgación coordinada de vulnerabilidades de CISA, acuerde un calendario y publique los detalles técnicos solo cuando haya mitigaciones disponibles. Una propiedad de diseño documentada en una especificación pública (la falta de autenticación de Modbus) no es una divulgación de vulnerabilidad; un fallo de implementación sí lo es.

Registre el calendario de divulgación en el apéndice de la tesis con las fechas del primer contacto, del acuse de recibo del fabricante y de la publicación. Si el fabricante no responde, siga el proceso del coordinador en lugar de publicar antes de tiempo. La tesis puede describir igualmente la clase de debilidad mientras retiene los nombres de los productos y los pasos hasta que existan mitigaciones.

### 8.5 Traducción para la práctica

Escriba un informe de dos páginas para los operadores con niveles de confianza: «Confianza alta (modelo + banco de pruebas): las alarmas de banda por sí solas no detectan lecturas de nivel repetidas. Confianza media (dos contextos): una medición de caudal independiente más una comprobación de residuos detecta la repetición sobre un solo sensor. Sin protección: si un solo dispositivo o PLC controla ambas mediciones». Sugiera a los grupos de trabajo de normalización que se consideren rutas de medición independientes al evaluar los niveles de seguridad de las zonas, como propuesta y no como hallazgo de cumplimiento.

Pruebe el informe con uno o dos operadores antes de publicarlo: ¿pueden decir qué comprobar el lunes? Si no pueden, hay que reformular los niveles de confianza o la recomendación. Mantenga el informe coherente con la afirmación acotada y no permita que un formato más corto omita el caso en que un solo dispositivo controla ambas mediciones.

### 8.6 Programa posdoctoral

Extender el trabajo a plantas de varios lazos, probar modelos calibrados en lugar de inventados, medir el tiempo de respuesta de los operadores con personal real de salas de control (que dé su consentimiento) y estudiar atacantes de clase C que modifican la lógica del PLC. Cada extensión prueba un límite que la tesis midió pero no pudo cruzar. Las plantas de varios lazos prueban si los residuos siguen siendo interpretables cuando los lazos interactúan. Los modelos calibrados prueban si los parámetros inventados sobrestimaron la separación. Los operadores reales prueban la interpretabilidad a escala. Los atacantes de clase C, que pueden reescribir la lógica del controlador, prueban si algún invariante sobrevive cuando el propio controlador miente; los mismos límites de seguridad y la misma revisión ética se aplican a las cuatro extensiones.

### Ejercicios — capítulo 8

- **EX045 — Audite tres afirmaciones del capítulo 5.** Audite tres afirmaciones de su propio párrafo de resultados del capítulo 5 con los criterios del laboratorio 8. *Rúbrica:* 3 = tres afirmaciones etiquetadas PASS/REVISE con correcciones de alcance; 2 = dos afirmaciones; 1 = una; 0 = nada.
- **EX046 — Respuestas de defensa sobre posicionamiento y seguridad.** Escriba respuestas modelo a las preguntas de los examinadores sobre posicionamiento y seguridad física. *Rúbrica:* 3 = posicionamiento más allá de Page/Giraldo + respuesta de seguridad con los límites de T2/parada de emergencia; 2 = una familia; 1 = vago; 0 = nada.
- **EX047 — Secuencie tres artículos por tipo de foro.** Secuencie tres artículos con foros del tipo adecuado (seguridad, control, factores humanos) y justifique el orden. *Rúbrica:* 3 = orden seguridad→control/CPS→FH con razón de dependencia; 2 = tres foros en orden erróneo; 1 = un artículo; 0 = nada.
- **EX048 — Tres decisiones de divulgación.** Decida si cada uno de tres hallazgos es un caso de divulgación: Modbus carece de autenticación; un firmware de PLC acepta escrituras en un registro protegido; el PLC de T2 comparte cableado para ambos sensores. *Rúbrica:* 3 = Modbus=documentado; escritura en registro protegido=divulgación coordinada; cableado compartido de T2=responsable del laboratorio, no divulgación de producto; 2 = dos correctas; 1 = una; 0 = nada.
- **EX049 — Declaraciones de confianza sin clase B.** Escriba las tres declaraciones de confianza del informe para operadores de un estudio en el que no se probó la clase B. *Rúbrica:* 3 = alta/media/desconocida con la clase B no probada explícita; 2 = falta desconocida; 1 = un nivel; 0 = nada.
- **EX050 — Posdoctorado de dos años con dos hipótesis.** Esboce un programa posdoctoral de dos años con dos hipótesis falsables. *Rúbrica:* 3 = plan de dos años con dos H falsables, incluidas métricas/límites de FA; 2 = plan sin H falsables; 1 = solo temas; 0 = nada.

### Síntesis del capítulo

Audite cada afirmación, prepárese para las seis familias de preguntas, publique en un orden que genere credibilidad, divulgue los fallos de implementación mediante coordinación y traduzca los hallazgos con una confianza explícita. La contribución doctoral es un método medido *y* sus límites medidos.

### Siga estudiando — capítulo 08 de 08

[← Capítulo 07 (borrador)](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Resultados resueltos ↓](#worked-results) · [Siguiente curso: Infraestructura crítica y seguridad sectorial, doctorado (curso 207) →](../../../critical-sector-security/es/SUBJECTS.md)

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

### Capítulo 3

**EX015.** Tipo de contribución: comparación respaldada por mediciones con límites caracterizados. «No proponemos un detector nuevo; a partir del CUSUM (Page, 1954) y de la detección basada en residuos (Giraldo et al., 2018), medimos cuándo un invariante de balance de masa entre sensores detecta la manipulación de la vista y la capacidad del atacante con la que falla».
**EX016.** Equilibrio L* = caudal de entrada/0,02 = 1,05/0,02 = 52,5 unidades. Un caudal de entrada adicional persistente de 0,05 eleva el nivel solo 2,5 unidades en régimen estacionario; el atacante necesita un forzamiento mayor (o una salida bloqueada) para llegar a un disparo, lo que afecta a qué ganancias son realistas en el capítulo 6.
**EX017.** La clase C modifica la lógica del PLC, así que puede falsificar ambos valores informados de forma coherente y suprimir las alarmas calculadas en el PLC. Alarma de banda: evadida. CUSUM en el PLC: evadido. CUSUM calculado fuera del PLC sobre sensores cableados de forma independiente: sigue detectando. Conclusión: la ubicación del detector importa tanto como el algoritmo.
**EX018.** Registrar `true_level − 50` en la primera alarma da, para el CUSUM y una ganancia de 0,05, un sobrellenado medio de 1,22 unidades y un máximo de 1,60 en el momento de la alarma; la alarma de banda nunca se dispara después del inicio, así que su sobrellenado crece hasta el máximo de la ventana, 3,36. H3 queda respaldada en el modelo.
**EX019.** Suponga que el disparo por nivel muy alto está en 56 (margen 6) y que el ataque eleva el nivel inicialmente hasta ≈0,05 unidades/paso. La mitad del margen (3 unidades) se alcanzaría en unos 60–80 pasos una vez considerada la aproximación exponencial; un umbral de 60 pasos es conservador. Un nivel de disparo distinto justifica un umbral distinto con la misma aritmética.
**EX020.** (1) Ajuste del umbral con datos de prueba → ajustar con semillas separadas (laboratorio 6) y congelar. (2) Simulador demasiado limpio → añadir sesgo de calibración y validar en T2. (3) Magnitud de ataque elegida a la medida del método → barrer las ganancias (EX034) e informar la curva completa.

### Capítulo 4

**EX021.** Volver a ejecutar su propio laboratorio 3: repetibilidad. Un colega que ejecuta su archivo: reproducibilidad. Un colega que construye su propio modelo de tanque: replicabilidad.
**EX022.** Hipótesis: convención de puntuación, filtración del umbral, alineación de etiquetas, muestreo. Pruebas: volver a puntuar con ajuste por puntos (→0,94, dentro de ±0,05: explica la diferencia); reajustar con la partición de entrenamiento (sin cambios adicionales); desplazar las etiquetas a la primera desviación del proceso (cambio pequeño); submuestrear (cambio pequeño). Resultado: la reproducción de la cifra informada solo tiene éxito con ajuste por puntos; se adoptan métricas por eventos.
**EX023.** Ejecute el modelo sin ruido `true += 1.0 - 0.02*true` durante 1.000 pasos desde 50,0; el resultado es 50,000000, lo que confirma el equilibrio; una prueba más estricta calcula el caudal de entrada acumulado menos el de salida y comprueba que es igual al nivel final menos el inicial dentro de la tolerancia de coma flotante.
**EX024.** k = 0,8: con un sesgo de 0,4 tiene 0/100 ejecuciones con falsa alarma y 100/100 detecciones (retardo 55,6), mientras que k = 0,6 tiene 4/100 ejecuciones con falsa alarma. Se acepta el coste de 7–10 pasos de retardo a cambio de cero falsas alarmas.
**EX025.** Continuar si: tres ejecuciones consecutivas se completan sin que se alcance la válvula de flotador (seguridad); pérdida de registros del historiador <1 % a 1 Hz (datos); ningún reinicio no planificado del PLC (estabilidad); parada de emergencia probada antes de cada sesión. En caso contrario, no continuar y revisar.
**EX026.** Porque 0,94 reproduce una puntuación con ajuste por puntos que acredita segmentos enteros por una sola alarma; no dice nada sobre el retardo ni sobre las falsas alarmas por turno, y los umbrales pueden haberse ajustado con datos de prueba.

### Capítulo 5

**EX027.** Sustituir la semilla pareada de k = 0,6 por la semilla i+1000 da en la planta A 6,9 pasos, IC [5,3, 8,5] (anchura 3,2), frente a [6,5, 7,4] pareado (anchura 0,9); en la planta B 47,3, IC [36,5, 58,6], frente a [38,4, 53,0]. El emparejamiento estrecha los intervalos porque el ruido compartido se cancela.
**EX028.** Estocásticas: extracciones del ruido del sensor, ruido del caudal de entrada. Paramétricas: coeficiente del orificio, sesgo de calibración. Estructurales: modelo de un solo tanque, ignorar el retardo del caudalímetro.
**EX029.** «La holgura k = 0,8 y el umbral h = 6,0 se fijan, se les calcula un hash y se registran antes de cargar cualquier dato de ataque de T2». Inspeccionar datos de ataque de T2 antes de congelar, o cambiar k después de ver los resultados de T2, invalida la validación.
**EX030.** Las ejecuciones no detectadas fijadas en 400 convierten la media en una cota inferior. Informe por separado la proporción de detección y la mediana del retardo entre los detectados, o una curva de tiempo hasta la detección de estilo Kaplan–Meier.
**EX031.** Recomendación: mostrar en la HMI el nivel predicho frente al informado. Limitación: operadores sintéticos; sus preferencias pueden no predecir tiempos de respuesta reales.
**EX032.** Ejemplo: «H1 no quedó respaldada en T2: el CUSUM de residuos detectó 9 de 20 episodios de clase A, frente a 100 de 100 en la simulación. Un retardo del caudalímetro de varios segundos produjo transitorios del residuo que exigieron una holgura mayor, la cual ocultó después manipulaciones pequeñas. Las falsas alarmas siguieron en cero. Concluimos que el simulador sobrestimó la relación señal/ruido y que la dinámica de los instrumentos debe modelarse antes de hacer afirmaciones de despliegue».

### Capítulo 6

**EX033.** Hipótesis: el rendimiento cae cuando los umbrales se evalúan con semillas o bancos de pruebas no vistos durante el ajuste. Prueba: ajustar con las semillas 0–99 y evaluar con 1000–1099 y en T2 con valores congelados; comparar la detección y las falsas alarmas.
**EX034.** Resultado del barrido: ganancia 0,005 → 14/100 detectados, retardo medio 186,0, peor sobrellenado 1,12; 0,01 → 55/100, 168,3, 1,37; 0,02 → 100/100, 90,4, 1,87; 0,05 → 100/100, 31,8, 3,36. Los ataques lentos evaden, pero logran un sobrellenado limitado en la ventana.
**EX035.** «El método requiere una segunda medición cableada de forma independiente y vinculada a la atacada por un balance de masa conocido; el error del modelo debe ser menor que la señal del ataque. Los ataques más lentos que la holgura pueden evadir, pero lograron ≤1,37 unidades de sobrellenado modelado en 300 pasos. No ofrece protección cuando un atacante controla ambas mediciones».
**EX036.** «En dos contextos sintéticos, un CUSUM de residuos que usa un caudalímetro cableado de forma independiente detectó la repetición del nivel sobre un solo sensor que una alarma de banda no detectó; no protege frente a un atacante que controla ambas mediciones».
**EX037.** Publicar la secuencia exacta de T2 da a los atacantes una receta lista para una configuración de producto concreta, mientras que los defensores solo necesitan la clase de capacidad y la corrección arquitectónica. Decisión: publicar la clase y la defensa; compartir las secuencias exactas solo con el fabricante mediante divulgación coordinada, si hay un fallo de producto implicado.
**EX038.** «Estamos de acuerdo en que los bancos de pruebas difieren de las plantas y hemos acotado nuestras afirmaciones a los dos contextos estudiados (§6.3). Probamos la incertidumbre estructural validando en un banco de pruebas independiente, con instrumentos distintos, umbrales congelados a partir de la simulación (§5.3), informamos la pérdida de exhaustividad resultante y enumeramos la validación a escala de planta como trabajo futuro (§8.6)».

### Capítulo 7

**EX039.** Afirmación: afirmación acotada (cap. 6.3). Datos: laboratorio 3, laboratorio 5, T2 (cap. 3, 5). Garantía: el balance de masa vincula caudal y nivel (cap. 3.2). Respaldo: pruebas de verificación, teoría del CUSUM (cap. 4.3). Calificador: dos contextos sintéticos (cap. 5). Refutación: clase B, rampas lentas, retardo (cap. 5–6).
**EX040.** Almacene los niveles como enteros (`int(e["tier"][1:])`) y compare números; así, una entrada T10 con un máximo de publicación T1 se excluye en lugar de pasar erróneamente como "T10" < "T2".
**EX041.** Código del simulador T0; trazas sintéticas T1; cuadernos de laboratorio T1; diagrama de cableado de la instalación T2 T2; programa del PLC de T2 T2; notas de la revisión de operadores T2; configuraciones reales al estilo de la planta A T3; vídeos del piloto T2. Casos dudosos: diagrama de cableado (T2 porque revela la debilidad del PLC compartido); notas de los operadores (T2 porque contienen citas identificables).
**EX042.** Propósito: enseñanza y demostración del método. Parámetros: caudal de entrada 1,0±0,05, caudal de salida 0,02×nivel, ruido del nivel σ = 0,3, ruido del caudal σ = 0,02, ganancia del ataque 0,05 en el paso 300. Condición: inventado, no calibrado. Usos prohibidos: afirmaciones sobre plantas reales, evaluación comparativa de productos.
**EX043.** Inicio fijo del ataque en el paso 300 (*desconocida*; puede favorecer a los detectores con calentamiento). Un único objetivo del atacante (*sobrestima* la generalidad).
**EX044.** El compendio de publicaciones encaja: tres contribuciones separables (métricas, comparación, estudio con operadores) con un capítulo de enlace; una monografía es defendible si la institución prefiere un único argumento integrado.

### Capítulo 8

**EX045.** Usando el párrafo de EX032 o del §5.5: «detectó la repetición de clase A en la simulación» → PASS con alcance; «robusto frente al sesgo de calibración» → REVISE: añadir alcance (≤0,4 unidades); «funciona en plantas reales» → REVISE: redacción excesiva.
**EX046.** Posicionamiento: «El CUSUM y los residuos están establecidos; nuestra contribución es medir el retardo y el impacto en el momento de la detección para la manipulación de la vista en dos contextos e identificar la capacidad del atacante con la que el método falla». Seguridad física: «Todos los ataques se ejecutaron en simulación o en T2 con una válvula mecánica de flotador independiente del PLC, una bandeja de goteo, una parada de emergencia física y una autoridad de parada designada; no se tocó ningún sistema de producción».
**EX047.** 1: artículo de metodología en un foro de seguridad (establece las métricas); 2: comparación en un foro de seguridad de control/CPS (usa esas métricas); 3: estudio con operadores en un foro de factores humanos. El orden construye el vocabulario del que dependen los artículos posteriores.
**EX048.** Modbus carece de autenticación: propiedad de diseño documentada, no una divulgación. Un PLC acepta escrituras en un registro protegido: fallo de implementación → divulgación coordinada. Cableado compartido en T2: problema de configuración del laboratorio → informar al responsable del laboratorio; no es una vulnerabilidad de producto.
**EX049.** Alta: las alarmas de banda por sí solas no detectan lecturas de nivel repetidas. Media: una medición de caudal independiente más un residuo detecta la repetición sobre un solo sensor. Desconocida: no se probó la protección frente a un atacante que controla ambas mediciones; no la dé por supuesta.
**EX050.** Año 1: modelo calibrado de varios lazos; H: exhaustividad de la detección por residuos ≥80 % con falsas alarmas ≤1 por turno cuando los lazos se acoplan. Año 2: estudio con operadores que dan su consentimiento; H: mostrar los valores predichos frente a los informados reduce el tiempo hasta el diagnóstico correcto en ≥20 %. Ambos con umbrales congelados y criterios de refutación.

**Fin de los resultados resueltos.** Vuelva al [índice de capítulos del curso](../SUBJECTS.md).

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
