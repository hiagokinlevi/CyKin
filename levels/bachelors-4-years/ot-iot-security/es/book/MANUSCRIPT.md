# Seguridad de TO, IoT y sistemas ciberfísicos: fundamentos de grado y proyecto final

- Idioma: español neutro (`es`); curso de grado, cuatro años; aproximadamente 3.200 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–40 de 40 tienen texto didáctico escrito a mano; los ejercicios EX001–EX120 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no equivale a un libro terminado.
- Público: estudiantes de seguridad y computación en sentido amplio que necesitan fundamentos rigurosos en seguridad de TO, IoT y sistemas ciberfísicos, y que terminan con un proyecto final y una tesis de alcance acotado.
- Relación con los libros vecinos: el [libro de ingeniería](../../../../engineering-5-years/ot-iot-security/en/book/MANUSCRIPT.md) se centra en el diseño; el [libro de maestría](../../../../masters-2-years/ot-iot-security/en/book/MANUSCRIPT.md) está guiado por la investigación. **Este libro equilibra fundamentos, teoría, casos, métodos y habilidades de investigación.**
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado. No concede autorización para acceder a plantas reales. Todas las plantas, personas y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los capítulos 1–18 son fundamentos, cada uno aplicado a una planta desde su primera página. Los capítulos 19–32 forman el núcleo de TO, IoT y sistemas ciberfísicos, con el Laboratorio I (25) y el Laboratorio II (30). Los capítulos 33–40 tratan de métodos de investigación, un proyecto comparativo, el proyecto final y la tesis. Cada capítulo tiene resultados de aprendizaje, secciones didácticas, un ejemplo resuelto, un caso sintético etiquetado, errores y límites, tres ejercicios puntuados de 0 a 3, una síntesis y un bloque **Siga estudiando**. Los laboratorios se ejecutan sin conexión con `python3 file.py`; nunca los dirija contra un sistema real.

### Caso de estudio sintético

| Elemento | Función | Límite |
|---|---|---|
| **Lakeside District Heating Plant (LDHP)** — PLC de control de calderas PLC-H, disparo de seguridad SIS-H, HMI-1, historiador HIST-1, estación de ingeniería EWS-1, contadores de calor IoT y pasarelas de contadores | Sistema estudiado a lo largo del libro | Inventado |
| **Maya Chen** | Estudiante de grado en estancia en la oficina de ingeniería de LDHP | Inventada |

### Fuentes principales

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [serie ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); avisos de CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a) y [AA22-103A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-103a); ICS-CERT [IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). Lista completa en [Referencias](#references).

## Contenido

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](../../en/book/MANUSCRIPT.md#ch-07) · [8](../../en/book/MANUSCRIPT.md#ch-08) · [9](../../en/book/MANUSCRIPT.md#ch-09) · [10](../../en/book/MANUSCRIPT.md#ch-10) · [11](../../en/book/MANUSCRIPT.md#ch-11) · [12](../../en/book/MANUSCRIPT.md#ch-12) · [13](../../en/book/MANUSCRIPT.md#ch-13) · [14](../../en/book/MANUSCRIPT.md#ch-14) · [15](../../en/book/MANUSCRIPT.md#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) · [19](../../en/book/MANUSCRIPT.md#ch-19) · [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) · [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) · [31](../../en/book/MANUSCRIPT.md#ch-31) · [32](../../en/book/MANUSCRIPT.md#ch-32) · [33](../../en/book/MANUSCRIPT.md#ch-33) · [34](../../en/book/MANUSCRIPT.md#ch-34) · [35](../../en/book/MANUSCRIPT.md#ch-35) · [36](../../en/book/MANUSCRIPT.md#ch-36) · [37](../../en/book/MANUSCRIPT.md#ch-37) · [38](../../en/book/MANUSCRIPT.md#ch-38) · [39](../../en/book/MANUSCRIPT.md#ch-39) · [40](../../en/book/MANUSCRIPT.md#ch-40) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Razonamiento matemático

### Resultados de aprendizaje

Al terminar este capítulo usted podrá (1) convertir una frase sobre la planta en una magnitud con unidades; (2) estimar un orden de magnitud antes de calcular; (3) enunciar la hipótesis que hace válido un cálculo; y (4) reconocer cuándo un número de aspecto preciso esconde una conjetura. El caso de estudio es la planta sintética Lakeside District Heating Plant (LDHP).

### 1.1 Por qué un estudiante de TO necesita hábitos de demostración

Las afirmaciones de seguridad sobre una planta de calefacción son cuantitativas, lo admitamos o no. «El cambio de red es de bajo riesgo» significa en realidad «la probabilidad de perder el control de la temperatura de impulsión, multiplicada por el daño a los hogares, está por debajo de un umbral que aceptamos». El razonamiento matemático hace visibles los términos ocultos. El hábito es sencillo: escriba cada magnitud con su unidad, nombre la hipótesis que la vincula con la magnitud siguiente y contraste el resultado con una estimación aproximada hecha antes de tocar la calculadora.

### 1.2 Unidades y comprobaciones dimensionales

La calefacción urbana mezcla kilovatios, metros cúbicos por hora, grados Celsius y segundos. La potencia térmica entregada es aproximadamente P = ρ · c · Q · ΔT, con una densidad del agua ρ ≈ 1000 kg/m³ y un calor específico c ≈ 4,19 kJ/(kg·K). Si escribe Q en m³/h, debe dividir entre 3600 para obtener kg/s. Una comprobación dimensional detecta ese descuido antes de que se convierta en un argumento equivocado de dimensionamiento de calderas en un registro de riesgos. El primer memorando de Maya necesitaba exactamente esta comprobación: un error de 5 K en el punto de consigna es un ΔT, así que el déficit escala con el caudal, y un caudal expresado en m³/h da un número 3600 veces demasiado grande si no se convierte antes a kg/s.

### 1.3 Implicación, contrarrecíproco y contraejemplo

«Si el SIS es independiente, entonces un compromiso del SCADA no puede desactivar el disparo». El contrarrecíproco —«si un compromiso del SCADA puede desactivar el disparo, el SIS no es independiente»— es lógicamente equivalente y a menudo más fácil de probar. El recíproco no es equivalente: un disparo que supera una prueba no demuestra la independencia. Un único contraejemplo documentado, como una estación de ingeniería compartida que puede descargar lógica en ambos controladores, refuta una afirmación universal. En LDHP, el contraejemplo que hay que buscar es EWS-1: si una sola estación de ingeniería puede descargar lógica tanto en PLC-H como en SIS-H, la afirmación de que SIS-H es independiente de un compromiso de la zona de control es falsa, por muchas pruebas de disparo que SIS-H haya superado.

### Ejemplo resuelto (LDHP sintética)

LDHP bombea Q = 180 m³/h con ΔT = 30 K. Primero, la estimación: 0,05 m³/s × 1000 kg/m³ × 4,19 kJ/(kg·K) × 30 K ≈ 6.300 kW. Cálculo exacto: 180/3600 = 0,05 m³/s, así que P = 50 kg/s × 4,19 × 30 = 6.285 kW ≈ 6,3 MW. Si un atacante solo pudiera cambiar el punto de consigna de impulsión en 5 K, ΔT bajaría a 25 K y el calor entregado caería a 5.237,5 kW, un déficit de 1.047,5 kW. Ese déficit, no el paquete, es la consecuencia que un responsable del riesgo puede ponderar.

> **Caso sintético — Lakeside District Heating Plant.** La estudiante Maya Chen se incorpora a la oficina de ingeniería de LDHP. Su primer memorando debe expresar en kilovatios el déficit de calor causado por un error de 5 K en el punto de consigna, con todas las hipótesis enumeradas.

### Errores y límites

La fórmula del calor ignora las pérdidas en las tuberías y el hecho de que la densidad y la capacidad calorífica varían con la temperatura. Una respuesta con dos cifras significativas es honesta; seis dígitos sugieren un conocimiento que usted no tiene.

### Ejercicios — capítulo 1

- **EX001 — Calor con caudal reducido.** El caudal de LDHP baja a 150 m³/h mientras ΔT se mantiene en 30 K. Calcule la potencia entregada y muestre la conversión de unidades. *Rúbrica:* 3 = 5.237,5 kW con la conversión m³/h→kg/s mostrada; 2 = valor correcto, sin conversión; 1 = olvidó dividir entre 3600; 0 = sin intento.
- **EX002 — Contrarrecíproco de una afirmación de zonificación.** Escriba el contrarrecíproco de «si la pasarela de contadores no tiene ruta hacia la zona de control, no puede escribir en PLC-H». *Rúbrica:* 3 = contrarrecíproco correcto y por qué es comprobable; 2 = solo la forma correcta; 1 = da el recíproco; 0 = nada.
- **EX003 — Estimar antes de calcular.** Dé una estimación de orden de magnitud, en una línea, del calor diario entregado a 6,3 MW. *Rúbrica:* 3 = ≈150 MWh/día con el método; 2 = orden correcto; 1 = error de unidades; 0 = nada.

### Síntesis del capítulo

Magnitudes con unidades, hipótesis dichas en voz alta y contraejemplos buscados: estos tres hábitos convierten una opinión de seguridad sobre una planta en un argumento que otra persona puede comprobar.

### Siga estudiando — capítulo 01 de 40

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Sistemas de computación

### Resultados de aprendizaje

Usted podrá (1) describir las capas de un controlador lógico programable, desde la tarjeta de E/S hasta el ciclo de escaneo; (2) contrastar un PLC con un servidor de propósito general; (3) explicar por qué la temporización determinista es una propiedad de seguridad en TO; y (4) enumerar lo que contiene una imagen de firmware.

### 2.1 El ciclo de escaneo

Un PLC lee repetidamente las entradas, ejecuta la lógica, escribe las salidas y atiende las comunicaciones. En LDHP, el PLC de calderas PLC-H completa este bucle cada 20 ms. Si la gestión de comunicaciones crece —por ejemplo, porque un historiador mal configurado sondea 400 registros cada 50 ms—, el tiempo de escaneo se alarga y el temporizador de vigilancia (watchdog) puede llevar el controlador a una parada segura. Por eso, en TO una denegación de servicio puede llegar como tráfico ordinario que simplemente es demasiado.

Maya se encontró con esto en su segunda semana: un proyecto de panel de control pedía «todas las etiquetas, en cada escaneo». Convertida a tiempo de escaneo, esa petición habría cargado la gestión de comunicaciones de PLC-H en cada ciclo de 20 ms, así que recomendó leer del historiador.

### 2.2 PLC frente a servidor

Un servidor está diseñado para ejecutar muchos programas, aceptar actualizaciones y recuperarse reiniciando. Un PLC está diseñado para ejecutar un único programa durante años, a menudo sin cuentas de usuario, con un registro limitado y con un firmware que el fabricante firma (o, en modelos antiguos, no firma). Reiniciar un servidor es rutina; reiniciar un controlador en una sala de calderas en funcionamiento exige un permiso de trabajo, la presencia de operadores y un plan para mantener el proceso en estado seguro.

Para PLC-H esto significa que una corrección de firmware no puede aplicarse sin más un martes por la tarde: necesita la ventana mensual de cuatro horas, un permiso de trabajo y la presencia del jefe de turno.

### 2.3 Qué vive en el firmware

El firmware agrupa un sistema operativo de tiempo real, pilas de protocolos, el entorno de ejecución que ejecuta la lógica de escalera o el texto estructurado, y un cargador de arranque. De ahí se siguen consecuencias de seguridad: un fallo en una pila de protocolos puede afectar a todos los programas del dispositivo, y una vía de actualización sin firma permite a cualquiera que alcance el puerto de ingeniería sustituir el entorno de ejecución. NIST SP 800-82r3 trata la integridad del firmware y la descarga controlada de programas como prácticas centrales de TO.

Para PLC-H, la pregunta práctica es quién puede alcanzar el puerto de ingeniería: si EWS-1 es el único equipo que puede hacerlo, proteger EWS-1 protege el entorno de ejecución; si la VLAN de oficina también puede alcanzar el puerto 502, el comportamiento de firma del firmware se convierte en la última barrera.

### Ejemplo resuelto (LDHP sintética)

PLC-H tiene un escaneo objetivo de 20 ms y un watchdog de 100 ms. La lógica tarda 9 ms, la E/S 4 ms, y atender cada petición Modbus cuesta 0,6 ms. Con 10 peticiones por escaneo, el ciclo es 9 + 4 + 6 = 19 ms. Si un nuevo panel añade 30 peticiones por escaneo, el ciclo pasa a 37 ms: sigue por debajo del watchdog, pero se pierde la temporización de 20 ms que esperan los lazos ajustados y la calidad del control se degrada antes de que salte ninguna alarma.

> **Caso sintético — Lakeside District Heating Plant.** Maya encuentra un proyecto de panel que pide «todas las etiquetas, en cada escaneo». Convierte la petición en milisegundos de escaneo y recomienda sondear el historiador, no el controlador.

### Errores y límites

Los modelos de escaneo varían según el fabricante; algunos atienden las comunicaciones en una tarea separada. Nunca mida el impacto en el escaneo cargando un controlador de producción: use una unidad de banco o las cifras del fabricante.

### Ejercicios — capítulo 2

- **EX004 — Carga de comunicaciones y tiempo de escaneo.** Con 9 ms de lógica, 4 ms de E/S y 0,6 ms por petición, ¿cuántas peticiones por escaneo mantienen PLC-H en 20 ms o menos? *Rúbrica:* 3 = 11 peticiones, con el cálculo; 2 = número correcto, sin cálculo; 1 = ignora la E/S; 0 = nada.
- **EX005 — Hábitos de servidor que dañan a los controladores.** Nombre dos hábitos de administración de servidores que no son seguros en un PLC en funcionamiento y dé la alternativa de TO para cada uno. *Rúbrica:* 3 = dos hábitos con alternativas; 2 = un par; 1 = hábitos sin alternativas; 0 = nada.
- **EX006 — Capas del firmware y radio de impacto.** Explique por qué una vulnerabilidad en la pila de protocolos de un controlador tiene un impacto más amplio que un fallo en un escalón de la lógica de escalera. *Rúbrica:* 3 = la pila compartida sirve a todos los programas y es alcanzable antes de que se ejecute la lógica; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis del capítulo

Un controlador es primero una máquina temporizada y después un computador; su seguridad empieza por respetar el ciclo de escaneo y controlar qué puede cargarse en él.

### Siga estudiando — capítulo 02 de 40

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Programación I

### Resultados de aprendizaje

Usted podrá (1) leer datos estructurados con la biblioteca estándar de Python; (2) validar valores frente a rangos de ingeniería; (3) escribir salidas que un revisor pueda comprobar línea por línea; y (4) explicar por qué el código de validación es un artefacto relevante para la seguridad.

### 3.1 Etiquetas como registros

Una lista de etiquetas de TO es una tabla: nombre de la etiqueta, unidad de ingeniería, límites bajo y alto, valor actual. El módulo `csv` de Python lee estas tablas sin paquetes de terceros, lo que importa en portátiles de ingeniería bloqueados, donde instalar software requiere aprobación. Trate cada fila como un diccionario y mantenga el texto bruto separado de los números analizados, para que un fallo de análisis sea visible en lugar de convertirse silenciosamente en cero. En el laboratorio de etiquetas, conservar el texto bruto es lo que permite que la nota de Maya diga «FT-301 marcó −3,0 m³/h» en lugar de informar de un vacío o de un cero; el técnico de instrumentación puede entonces ver el valor exacto que envió el contador y decidir si el problema está en el escalado o en el cableado.

### 3.2 Validación de rangos

Una temperatura de 141 °C en una sonda calibrada para 20–130 °C es una desviación real, un sensor averiado o un valor manipulado. El código no puede saber cuál; puede marcar la fila e impedir que llegue a un informe etiquetado como «normal». Lo mismo vale para un caudal negativo, que es físicamente imposible en un contador unidireccional y, por tanto, siempre plantea una cuestión de calidad o de integridad de los datos. El laboratorio de etiquetas marca exactamente estas dos filas: TT-102 a 141,0 °C frente a un límite de 130 °C, y FT-301 a −3,0 m³/h. Maya envía la primera al operador de inmediato y la segunda a instrumentación como sospecha de fallo de cableado o de escalado.

### 3.3 Salida legible

Imprima una decisión por línea junto con la entrada que la causó. Los revisores de los comités de cambios de planta rara vez son programadores; confiarán en una salida que puedan rastrear hasta una fila.

```python
"""Lab 03: validate a synthetic LDHP tag list (no plant access)."""
import csv, io
RAW = """tag,unit,lo,hi,value
TT-101,degC,20,130,96.5
TT-102,degC,20,130,141.0
PT-201,bar,0,16,9.8
FT-301,m3/h,0,250,-3.0
LT-401,pct,0,100,57
"""
bad = []
for row in csv.DictReader(io.StringIO(RAW)):
    v, lo, hi = float(row["value"]), float(row["lo"]), float(row["hi"])
    ok = lo <= v <= hi
    print(f"{row['tag']:7} {v:7.1f} {row['unit']:5} {'ok' if ok else 'OUT-OF-RANGE'}")
    if not ok: bad.append(row["tag"])
print("flagged:", ", ".join(bad))
```

Ejecútelo con `python3 lab_tags.py`. Salida verificada:

```text
TT-101     96.5 degC  ok
TT-102    141.0 degC  OUT-OF-RANGE
PT-201      9.8 bar   ok
FT-301     -3.0 m3/h  OUT-OF-RANGE
LT-401     57.0 pct   ok
flagged: TT-102, FT-301
```

En LDHP, las dos filas marcadas se imprimen como `TT-102    141.0 degC  OUT-OF-RANGE` y `FT-301     -3.0 m3/h  OUT-OF-RANGE`, con el valor de entrada en la misma línea que la decisión; dirigir cada marca al operador o a instrumentación es el criterio de Maya en su nota, no algo que decida el script. Un revisor del comité de cambios que sea ingeniero de control, no programador, puede contrastar cada línea con el índice de instrumentos en un minuto y no necesita leer el script. Si una línea no puede rastrearse hasta una fila, el revisor no tiene motivos para confiar en ella, así que la salida nunca debería imprimir un recuento resumido sin las filas que lo respaldan.

### Ejemplo resuelto (LDHP sintética)

El laboratorio marca TT-102 (141,0 °C, por encima de 130) y FT-301 (−3,0 m³/h, por debajo de 0). La nota de Maya los separa: TT-102 podría ser una lectura alta genuina y va al operador de inmediato; FT-301 es físicamente imposible y va a instrumentación como sospecha de fallo de cableado o de escalado, con revisión de integridad si el fallo no puede explicarse.

> **Caso sintético — Lakeside District Heating Plant.** La lista de etiquetas del laboratorio es inventada; los límites reales de LDHP provendrían del índice de instrumentos que mantienen los ingenieros de control.

### Errores y límites

Las comprobaciones de rango detectan errores groseros, no una manipulación sutil dentro de la banda. La comparación en coma flotante en el límite necesita una regla explícita (aquí, inclusiva). El script lee una cadena, no un sistema en vivo.

### Ejercicios — capítulo 3

- **EX007 — Ampliar la tabla de etiquetas.** Añada la fila `TT-103,degC,20,130,130.0`. ¿Qué imprime el laboratorio para ella y por qué? *Rúbrica:* 3 = ok, porque los límites son inclusivos; 2 = ok sin motivo; 1 = dice fuera de rango; 0 = nada.
- **EX008 — Valores no analizables.** Describa qué hace el script si una celda de valor contiene `n/a` y proponga una corrección. *Rúbrica:* 3 = un ValueError detiene la ejecución; capturarlo y marcar BAD-VALUE; 2 = una de las dos cosas; 1 = dice que se convierte en cero; 0 = nada.
- **EX009 — Triaje de dos marcas.** Explique por qué TT-102 y FT-301 van a personas distintas. *Rúbrica:* 3 = desviación plausible frente a valor imposible, operador frente a instrumentación; 2 = parcial; 1 = trata ambas igual; 0 = nada.

### Síntesis del capítulo

Programas pequeños y legibles, con la biblioteca estándar, que marcan en lugar de corregir son la primera herramienta en la que un estudiante de seguridad de TO debería confiar y que debería poder defender.

### Siga estudiando — capítulo 03 de 40

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Escritura académica

### Resultados de aprendizaje

Usted podrá (1) estructurar un memorando técnico como afirmación, evidencia y limitación; (2) citar una norma por su identificador y edición exactos; (3) escribir para un operador, un ingeniero y un directivo sin cambiar los hechos; y (4) evitar el lenguaje inflado en los hallazgos de seguridad.

### 4.1 Afirmación, evidencia, limitación

Cada párrafo de un memorando de seguridad de TO debería permitir al lector encontrar tres cosas: qué afirma usted, qué observó que lo respalda y dónde termina la afirmación. «El puerto 502 de PLC-H es alcanzable desde la VLAN de oficina (observado en la exportación aprobada de reglas del cortafuegos del 3 de marzo); no probamos si las escrituras tienen éxito» es una frase mejor que «PLC-H está completamente expuesto», porque es comprobable y honesta sobre el alcance. El memorando de Maya usó esta frase casi palabra por palabra, y la única pregunta del jefe de turno, qué deberían hacer distinto los operadores esa noche, pudo responderse porque la limitación estaba enunciada.

### 4.2 Citar normas con precisión

Escriba «NIST SP 800-82 Rev. 3 (septiembre de 2023)», no «la guía del NIST». Para la familia 62443, nombre la parte: IEC 62443-3-3 trata los requisitos de seguridad del sistema y los niveles de seguridad; IEC 62443-2-1, el programa de seguridad del propietario del activo; IEC 62443-4-2, los requisitos de los componentes. El lector debe poder abrir el documento exacto. No cite un número de cláusula que no haya leído. La propuesta posterior de SL-T de Maya para LDHP cita IEC 62443-3-2 por su parte para el método de zonas e IEC 62443-3-3 para los requisitos, en lugar de «62443» para ambos. Un lector que quiera comprobar su SL-T 3 para la zona de control de calderas necesita abrir la parte que define los niveles de seguridad, no una familia de catorce documentos.

### 4.3 Un hecho, tres públicos

El operador necesita saber qué vigilar; el ingeniero necesita la ruta técnica; el directivo necesita el coste, el tiempo de inactividad y el riesgo residual. Mantenga los hechos idénticos en todas las versiones: solo cambian el énfasis y el vocabulario. Si las versiones discrepan en los hechos, una de ellas está equivocada. Para el hallazgo de PLC-H, el operador oye «si el punto de consigna de impulsión cambia sin una petición desde HMI-1, llame al jefe de turno»; el ingeniero oye «puerto 502 alcanzable desde la VLAN de oficina según la exportación de reglas del 3 de marzo; escrituras sin probar»; el directivo oye el coste del cambio en el cortafuegos y el riesgo residual hasta que se haga. Las tres versiones nombran el mismo puerto, la misma fecha y la misma pregunta sin probar.

### Ejemplo resuelto (LDHP sintética)

Versión débil: «Los hackers podrían tomar el control de la caldera, lo cual es extremadamente peligroso». Versión reescrita: «Un equipo de la VLAN de oficina puede abrir conexiones Modbus/TCP con PLC-H (regla 14 de la exportación del 3 de marzo). No hemos probado el acceso de escritura. El disparo por alta temperatura de SIS-H está cableado y no depende de esta ruta. Recomendación: eliminar la regla 14 y encaminar las lecturas del historiador a través de la DMZ». La versión reescrita da la ubicación, la evidencia, el alcance no probado, la salvaguarda independiente y una acción.

> **Caso sintético — Lakeside District Heating Plant.** El memorando de Maya lo revisa el jefe de turno de la planta, que hace una sola pregunta: «¿Qué deberían hacer distinto mis operadores esta noche?». El memorando debe responderla.

### Errores y límites

Evite «de grado militar», «totalmente seguro» y «riesgo cero». La voz pasiva que oculta quién observó qué debilita la evidencia. Una revisión de la literatura no sustituye a la observación propia.

### Ejercicios — capítulo 4

- **EX010 — Reescribir un hallazgo inflado.** Reescriba «el historiador es una puerta trasera enorme» como una frase de afirmación–evidencia–limitación para LDHP. *Rúbrica:* 3 = las tres partes con una observación concreta; 2 = dos partes; 1 = sigue inflada; 0 = nada.
- **EX011 — Elegir la parte correcta de 62443.** ¿Qué parte de IEC 62443 citaría para un requisito sobre la capacidad de autenticación propia de PLC-H, y cuál para el programa de gestión de parches de la planta? *Rúbrica:* 3 = 4-2 y 2-1 (2-3 también es aceptable para parches) con motivos; 2 = una correcta; 1 = cita solo «62443»; 0 = nada.
- **EX012 — Versión para el operador.** Escriba la versión para el operador, en dos frases, del hallazgo de la regla 14. *Rúbrica:* 3 = síntoma observable más acción; 2 = uno de los dos; 1 = solo jerga técnica; 0 = nada.

### Síntesis del capítulo

La buena escritura de TO es comprobable: fuentes exactas, evidencia observada y límites enunciados, con palabras sobre las que cada público pueda actuar.

### Siga estudiando — capítulo 04 de 40

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Alfabetización en seguridad

### Resultados de aprendizaje

Usted podrá (1) definir confidencialidad, integridad y disponibilidad para una planta de calefacción; (2) añadir la seguridad funcional y la fiabilidad como propiedades de primer orden; (3) separar amenaza, vulnerabilidad y consecuencia; y (4) relacionar una técnica pública de MITRE ATT&CK for ICS con un activo de LDHP.

### 5.1 El orden de preocupación en TO

En la TI de oficina, la confidencialidad suele ir primero. En una planta de calefacción urbana el orden suele invertirse: primero la seguridad de las personas y los equipos, después la disponibilidad y la integridad del control, y solo entonces la confidencialidad de los datos. Las tablas de recetas o las lecturas de los contadores de los clientes siguen importando —los datos de los contadores son datos personales—, pero una hoja de cálculo filtrada no quema a nadie, mientras que un punto de consigna manipulado sí puede hacerlo.

Maya lo aplicó cuando el director de la planta preguntó si debía cifrar primero la base de datos del historiador: ella dio más prioridad a separar la red de oficina de PLC-H, porque una escritura del punto de consigna puede cortar el calor a los hogares y una copia de la base de datos no.

### 5.2 Amenaza, vulnerabilidad, consecuencia

Una amenaza es un actor o un evento con intención o potencial de causar daño. Una vulnerabilidad es una debilidad que hace posible el daño. Una consecuencia es lo que realmente le ocurre al proceso. Los estudiantes suelen confundirlas: «Modbus no tiene autenticación» es una vulnerabilidad, «un contratista descontento» es una fuente de amenaza y «pérdida de calefacción en 4.000 hogares en enero» es una consecuencia. Los enunciados de riesgo necesitan las tres. El enunciado de riesgo de Maya para PLC-H las une: un contratista en la red de oficina (amenaza) puede escribir el registro 100 porque Modbus no tiene autenticación y el puerto 502 es alcanzable (vulnerabilidad), bajando el punto de consigna de impulsión a 30 °C y cortando el calor a 4.000 hogares (consecuencia).

### 5.3 ATT&CK for ICS como vocabulario

MITRE ATT&CK for ICS cataloga el comportamiento adversario observado contra sistemas industriales. La técnica T0836 *Modify Parameter* describe la modificación de parámetros del controlador, como puntos de consigna o límites, para causar un efecto; T0883 *Internet Accessible Device* describe el acceso a controladores expuestos directamente a internet. Use estos identificadores para describir el comportamiento con precisión, no como una lista de comprobación que pretenda ser completa. En LDHP, T0836 describe el escenario al que este libro vuelve con más frecuencia: una escritura en el registro de retención 100, el punto de consigna de la temperatura de impulsión. T0883 describe el controlador de calefacción «real» que un compañero de clase encuentra en un buscador en el capítulo 10. Nombrarlas permite a Maya vincular sus notas con avisos públicos sin dar a entender que la planta haya sufrido alguna de ellas.

### Ejemplo resuelto (LDHP sintética)

Enunciado: «Una parte no autorizada con acceso a la VLAN de oficina (amenaza) podría usar la ruta Modbus sin autenticación de la regla 14 (vulnerabilidad) para cambiar el punto de consigna de impulsión, comportamiento descrito por ATT&CK for ICS T0836 Modify Parameter, reduciendo el calor entregado en aproximadamente 1 MW (consecuencia, del capítulo 1); el SIS-H cableado limita el daño por sobretemperatura». Cada cláusula es separable y cada una puede cuestionarse.

> **Caso sintético — Lakeside District Heating Plant.** El director de la planta pregunta si cifrar la base de datos del historiador es la máxima prioridad. Maya la sitúa por debajo de separar la oficina de PLC-H y explica por qué usando el orden de preocupación de TO.

### Errores y límites

ATT&CK enumera comportamientos observados; la ausencia de una técnica no prueba que no pueda ocurrir. La seguridad funcional no es lo mismo que la ciberseguridad, y los controles de ciberseguridad nunca deben debilitar una función de seguridad funcional.

### Ejercicios — capítulo 5

- **EX013 — Clasificar amenaza, debilidad y daño.** Clasifique: (a) «contraseña por defecto en la pasarela de contadores», (b) «banda de ransomware», (c) «la caldera dispara y el distrito se queda sin calefacción durante seis horas». *Rúbrica:* 3 = vulnerabilidad, amenaza, consecuencia; 2 = dos correctas; 1 = una; 0 = nada.
- **EX014 — Priorizar en LDHP.** Justifique situar la integridad del punto de consigna por encima de la confidencialidad de los datos de los contadores en LDHP, sin decir que la confidencialidad no importa. *Rúbrica:* 3 = consecuencia física frente a daño a la privacidad, ambas conservadas; 2 = solo la priorización; 1 = desestima la privacidad; 0 = nada.
- **EX015 — Relacionar una pasarela expuesta.** ¿Qué identificador de técnica de ATT&CK for ICS describe que la pasarela de contadores sea alcanzable desde internet, y qué no demuestra esa relación? *Rúbrica:* 3 = T0883 y «no demuestra la explotación ni la completitud»; 2 = solo el identificador; 1 = identificador incorrecto; 0 = nada.

### Síntesis del capítulo

La alfabetización en seguridad en TO significa hablar con precisión de amenazas, debilidades y consecuencias físicas, con la seguridad funcional en primer lugar y con vocabularios compartidos usados con honestidad.

### Siga estudiando — capítulo 05 de 40

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Estructuras discretas

### Resultados de aprendizaje

Usted podrá (1) modelar zonas y conductos como un grafo dirigido; (2) calcular la alcanzabilidad con búsqueda en anchura; (3) razonar sobre qué eliminación de una sola arista desconecta un nodo crítico; y (4) usar conjuntos para expresar listas de permitidos.

### 6.1 Zonas y conductos como grafo

IEC 62443-3-2 pide a los propietarios de activos dividir un sistema en zonas (grupos de activos que comparten requisitos de seguridad) conectadas por conductos (los canales de comunicación entre zonas). Un grafo dirigido lo captura: los nodos son zonas y las aristas son conductos en el sentido en que puede abrirse una sesión. Una ruta desde la zona corporativa hasta la zona de seguridad funcional es una cuestión de alcanzabilidad en un grafo, que resulta mecánica una vez dibujado el grafo con honestidad.

En el grafo del laboratorio, Maya registra los conductos como pares ordenados, de modo que MeterGW→SCADA y Control→SIS son aristas visibles y no líneas en un dibujo.

### 6.2 Búsqueda en anchura

La búsqueda en anchura (BFS) visita un nodo de inicio, después todos sus vecinos, después los vecinos de estos, y marca cada nodo visitado una sola vez. Se ejecuta en un tiempo proporcional a los nodos más las aristas, así que incluso la lista de conductos de una gran refinería se comprueba al instante. El peligro no está en el algoritmo sino en la entrada: un módem de un proveedor olvidado o un portátil con doble conexión es una arista que el diagrama omite.

```python
"""Lab 06: reachability over a synthetic LDHP zone/conduit graph (BFS)."""
from collections import deque
CONDUITS = {"Enterprise": ["DMZ"], "DMZ": ["SCADA"], "SCADA": ["Control"],
            "Control": ["SIS"], "MeterCloud": ["MeterGW"], "MeterGW": ["SCADA"], "SIS": []}
def reach(src):
    seen, q = {src}, deque([src])
    while q:
        for n in CONDUITS.get(q.popleft(), []):
            if n not in seen: seen.add(n); q.append(n)
    return seen
for z in ["Enterprise", "MeterCloud", "SCADA"]:
    r = sorted(reach(z) - {z}); print(f"{z:10} -> {r}  SIS reachable: {'SIS' in r}")
CONDUITS["Control"] = []  # design change: SIS gets its own hardwired trip, no Control->SIS data conduit
print("after removing Control->SIS:", "SIS" in reach("Enterprise"))
```

Ejecútelo con `python3 lab_reach.py`. Salida verificada:

```text
Enterprise -> ['Control', 'DMZ', 'SCADA', 'SIS']  SIS reachable: True
MeterCloud -> ['Control', 'MeterGW', 'SCADA', 'SIS']  SIS reachable: True
SCADA      -> ['Control', 'SIS']  SIS reachable: True
after removing Control->SIS: False
```

En LDHP, un módem de proveedor que nadie registró o una EWS-1 conectada a la vez a la red de oficina y a la de control añadiría una arista que el laboratorio no puede conocer; la respuesta de la BFS solo es tan cierta como la lista de conductos.

### 6.3 Aristas de corte

Una arista cuya eliminación desconecta las zonas expuestas al atacante de la zona crítica es una arista de corte para ese par. En el laboratorio, Control→SIS es una de ellas: eliminarla hace que SIS sea inalcanzable desde Enterprise y desde MeterCloud. La ingeniería suele preferir eliminar por completo un conducto de datos hacia un sistema de seguridad funcional y confiar en disparos cableados, que es exactamente lo que representa el cambio de diseño del laboratorio. La nota de Maya añade el segundo paso: la arista MeterGW→SCADA existe solo para que facturación pueda leer los totales de caudal, así que sustituirla por una exportación unidireccional desde el historiador elimina la otra ruta de la nube de contadores hacia la zona de control.

### Ejemplo resuelto (LDHP sintética)

El laboratorio muestra que la nube de contadores alcanza SIS a través de MeterGW → SCADA → Control → SIS. Maya expresa la lista de conductos como un conjunto de pares ordenados y señala que la arista MeterGW→SCADA existe solo para que facturación pueda leer los totales de caudal. Sustituirla por una exportación unidireccional desde el historiador elimina una segunda ruta; eliminar Control→SIS elimina la última.

> **Caso sintético — Lakeside District Heating Plant.** Los nombres de las zonas y los conductos del laboratorio son inventados para que el grafo sea lo bastante pequeño como para comprobarlo a mano.

### Errores y límites

La alcanzabilidad indica que puede abrirse una sesión, no que vaya a tener éxito ni lo que puede hacer. Los dibujos no dirigidos ocultan la diferencia entre «el SCADA sondea la pasarela» y «la pasarela puede conectarse al SCADA».

### Ejercicios — capítulo 6

- **EX016 — Seguir una BFS a mano.** Enumere el orden en que la BFS desde MeterCloud visita los nodos del grafo original. *Rúbrica:* 3 = MeterCloud, MeterGW, SCADA, Control, SIS; 2 = conjunto correcto, orden incorrecto; 1 = falta un nodo; 0 = nada.
- **EX017 — Un módem de proveedor omitido.** Un módem de proveedor da a internet un conducto directo hacia Control. Tras el cambio de diseño del laboratorio, ¿es SIS alcanzable desde internet? *Rúbrica:* 3 = no, Control no tiene arista saliente hacia SIS tras el cambio, pero el propio Control queda ahora expuesto; 2 = solo «no»; 1 = «sí»; 0 = nada.
- **EX018 — Lista de permitidos como conjunto.** Exprese «HIST-1 puede leer de PLC-H; HMI-1 puede leer y escribir en PLC-H» como un conjunto de tuplas (origen, destino, acción). *Rúbrica:* 3 = tres tuplas, nada más; 2 = algún extra menor; 1 = usa rangos de equipos; 0 = nada.

### Síntesis del capítulo

Dibujar zonas y conductos como un grafo dirigido convierte los argumentos de segmentación en comprobaciones que cualquiera puede volver a ejecutar, siempre que el grafo incluya todas las aristas reales.

### Siga estudiando — capítulo 06 de 40

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](../../en/book/MANUSCRIPT.md#ch-07)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo para EX001–EX120. Lakeside District Heating Plant, Maya Chen y todos los números de la planta son sintéticos. Cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación.

**EX001.** 150/3600 = 0,04167 m³/s → 41,67 kg/s; P = 41,67 × 4,19 × 30 ≈ 5.237,5 kW (unos 5,2 MW), aproximadamente 1 MW por debajo del caso de 180 m³/h.

**EX002.** «Si la pasarela de contadores puede escribir en PLC-H, entonces tiene una ruta hacia la zona de control». Es comprobable porque encontrar cualquier ruta de escritura exitosa obliga a buscar la ruta, y no encontrar ninguna respalda (pero no demuestra) la afirmación original.

**EX003.** 6,3 MW × 24 h ≈ 151 MWh al día, es decir, «unos 150 MWh/día»; la estimación supone una carga constante, lo que un perfil de noche de invierno no cumpliría.

**EX004.** 9 + 4 = 13 ms deja 7 ms; 7 / 0,6 = 11,67, así que como máximo 11 peticiones por escaneo (11 × 0,6 = 6,6 ms → 19,6 ms).

**EX005.** (1) Reiniciar para eliminar un fallo → programar una parada controlada con los operadores manteniendo el proceso en estado seguro. (2) Instalar actualizaciones de inmediato → preparar el firmware en una unidad de banco y desplegarlo en una ventana de mantenimiento con plan de reversión. Desactivar servicios sobre la marcha o ejecutar escáneres también son ejemplos aceptables.

**EX006.** La pila de protocolos la comparte todo el dispositivo y analiza la entrada de red antes de que se ejecute ninguna lógica de usuario, así que un fallo en ella puede bloquear o controlar el controlador sea cual sea el programa cargado; un fallo de la lógica de escalera solo afecta a la función que implementa ese escalón.

**EX007.** `TT-103 130.0 degC ok`: la comparación `lo <= v <= hi` es inclusiva, así que una lectura exactamente en el límite alto pasa.

**EX008.** `float("n/a")` lanza un ValueError y el script se detiene con una traza antes de imprimir las filas restantes. Envuelva la conversión en try/except, imprima `BAD-VALUE` para esa etiqueta y añádala a la lista de marcadas, de modo que un valor ausente nunca se omita en silencio.

**EX009.** 141 °C es físicamente posible y puede ser un sobrecalentamiento real, así que el operador debe revisar el proceso ahora; −3 m³/h no puede darse en un contador unidireccional, así que apunta a cableado, escalado o manipulación y corresponde a instrumentación, con un seguimiento de integridad.

**EX010.** «HIST-1 acepta conexiones entrantes desde la VLAN de oficina en su puerto SQL (exportación del cortafuegos, 3 de marzo) y mantiene una sesión saliente hacia PLC-H; no probamos si la ruta desde la oficina puede alcanzar PLC-H a través de él».

**EX011.** IEC 62443-4-2 (requisitos de seguridad de los componentes, p. ej., autenticación de usuarios humanos en un dispositivo embebido) para la capacidad de PLC-H; IEC 62443-2-1 para el programa de seguridad del propietario del activo que incluye la gestión de parches, con IEC TR 62443-2-3 como el informe técnico específico de gestión de parches.

**EX012.** «Si ve en PLC-H un cambio de punto de consigna que nadie del turno ha hecho, llame al ingeniero de control y anote la hora. Hasta que se elimine la regla 14, no inicie sesión en el correo de la oficina desde el PC de la sala del HMI».

**EX013.** (a) vulnerabilidad; (b) fuente de amenaza; (c) consecuencia.

**EX014.** Un punto de consigna manipulado produce un daño físico inmediato —hogares fríos o esfuerzo sobre los equipos— y puede ser irreversible en cuestión de minutos, mientras que una filtración de datos de los contadores daña la privacidad y aun así debe prevenirse en virtud de los deberes de protección de datos; la integridad del control se sitúa primero porque su consecuencia es física y crítica en el tiempo, no porque pueda descuidarse la privacidad.

**EX015.** T0883 Internet Accessible Device. La relación muestra solo la exposición; no demuestra que nadie haya explotado la pasarela, ni que la lista de técnicas relacionadas cubra todas las formas en que LDHP podría ser atacada.

**EX016.** MeterCloud → MeterGW → SCADA → Control → SIS (cada nodo tiene una sola arista saliente, así que el orden de la cola es único).

**EX017.** No: tras el cambio, Control no tiene ningún conducto saliente, así que la nueva arista Internet→Control no alcanza SIS. Sin embargo, sí expone el control a nivel de PLC directamente a internet, lo que es un hallazgo grave por sí mismo.

**EX018.** {(HIST-1, PLC-H, read), (HMI-1, PLC-H, read), (HMI-1, PLC-H, write)}.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; las normas y los avisos se revisan, así que vuelva a verificar las ediciones antes de citarlas. Los DOI se comprobaron en Crossref. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Antonakakis, M., et al. (2017). Understanding the Mirai Botnet. 26th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis>
- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA, DOE, NSA, FBI (2022). AA22-103A: APT Cyber Tools Targeting ICS/SCADA Devices. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-103a>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ICS-CERT (2016). IR-ALERT-H-16-056-01: Cyber-Attack Against Ukrainian Critical Infrastructure. <https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01>
- ISA/IEC 62443 series of standards (overview; parts 2-1, 2-3, 3-2, 3-3, 4-1 and 4-2 are cited in the text). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS, including T0836 Modify Parameter, T0843 Program Download, T0883 Internet Accessible Device and T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- Modbus Organization. Modbus Application Protocol Specification V1.1b3. Listed at <https://www.modbus.org/modbus-specifications>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- NIST FIPS 198-1 (2008). The Keyed-Hash Message Authentication Code (HMAC). <https://csrc.nist.gov/pubs/fips/198-1/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
