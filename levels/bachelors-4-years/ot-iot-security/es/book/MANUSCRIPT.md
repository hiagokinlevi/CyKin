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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](../../en/book/MANUSCRIPT.md#ch-19) · [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) · [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) · [31](../../en/book/MANUSCRIPT.md#ch-31) · [32](../../en/book/MANUSCRIPT.md#ch-32) · [33](../../en/book/MANUSCRIPT.md#ch-33) · [34](../../en/book/MANUSCRIPT.md#ch-34) · [35](../../en/book/MANUSCRIPT.md#ch-35) · [36](../../en/book/MANUSCRIPT.md#ch-36) · [37](../../en/book/MANUSCRIPT.md#ch-37) · [38](../../en/book/MANUSCRIPT.md#ch-38) · [39](../../en/book/MANUSCRIPT.md#ch-39) · [40](../../en/book/MANUSCRIPT.md#ch-40) |

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

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Redes y protocolos

### Resultados de aprendizaje

Usted podrá (1) decodificar la cabecera MBAP de Modbus/TCP y el código de función a partir de bytes en bruto; (2) distinguir los códigos de función de lectura y de escritura; (3) explicar por qué Modbus no ofrece autenticación; y (4) enunciar lo que un decodificador de protocolos puede y no puede decirle a un analista.

### 7.1 Modbus/TCP en una trama

Modbus/TCP lleva una cabecera MBAP de siete bytes —identificador de transacción (2 bytes), identificador de protocolo (2, siempre cero), longitud (2) e identificador de unidad (1)— seguida de la unidad de datos del protocolo, que empieza con un código de función de un byte. La Modbus Application Protocol Specification V1.1b3 define los códigos: el 3 lee registros de retención, el 6 escribe un único registro y el 16 escribe varios registros. En el laboratorio del decodificador, la trama 2 lleva el código de función 6 y la trama 3 el código de función 16; ambas son escrituras, y por eso la lista de permitidos del capítulo 27 se fija en el código de función antes que en la dirección.

### 7.2 Sin identidad en el protocolo

Nada en la trama dice quién la envió. Cualquier equipo que pueda abrir el puerto TCP 502 de un controlador puede emitir una escritura si el dispositivo la acepta. La seguridad debe venir, por tanto, de la red (segmentación, listas de permitidos) o de una variante protegida como Modbus/TCP Security, que envuelve el protocolo en TLS con roles basados en certificados.

```python
"""Lab 07: decode synthetic Modbus/TCP request headers (offline bytes only)."""
import struct
FC = {1: "read coils", 3: "read holding registers", 4: "read input registers",
      5: "write single coil", 6: "write single register", 16: "write multiple registers"}
frames = ["000100000006010300640002", "00020000000601060064012c", "000300000006011000c80001"]
for h in frames:
    b = bytes.fromhex(h)
    tid, pid, length, unit, fc = struct.unpack(">HHHBB", b[:8])
    addr, val = struct.unpack(">HH", b[8:12])
    kind = "WRITE" if fc in (5, 6, 15, 16) else "read"
    print(f"tid={tid} unit={unit} fc={fc} ({FC[fc]}) addr={addr} arg={val} -> {kind}")
```

Ejecútelo con `python3 lab_modbus.py`. Salida verificada:

```text
tid=1 unit=1 fc=3 (read holding registers) addr=100 arg=2 -> read
tid=2 unit=1 fc=6 (write single register) addr=100 arg=300 -> WRITE
tid=3 unit=1 fc=16 (write multiple registers) addr=200 arg=1 -> WRITE
```

Para PLC-H, que no puede autenticar a los clientes Modbus, este es todo el argumento de los controles compensatorios del capítulo 24: la lista de permitidos del cortafuegos que nombra a HMI-1 y HIST-1 como únicos orígenes autorizados es la comprobación de identidad que le falta al protocolo. Un equipo de la VLAN de oficina que alcanza el puerto 502 es, para PLC-H, indistinguible de HMI-1.

### 7.3 Leer la salida

La trama 2 escribe el valor 300 en el registro 100; la trama 3 es una escritura de varios registros que empieza en el 200. Observe que el decodificador imprime la dirección inicial y el primer argumento, pero no sabe qué *significa* el registro 100: eso proviene del mapa de registros del PLC, que es documentación de la planta, no del protocolo. En el mapa de registros de LDHP, el registro 100 contiene el punto de consigna de la temperatura de impulsión en décimas de grado, así que el valor 300 significa 30,0 °C, muy por debajo del punto de funcionamiento de 90 °C. Esa es la diferencia entre «escribir un único registro» y «posible pérdida de calefacción». La nota de Maya añade una columna del mapa de registros precisamente por esta razón, y marca la escritura de varios registros de la trama 3 en el 200 como no explicada hasta que el mapa diga qué controlan los registros a partir del 200.

### Ejemplo resuelto (LDHP sintética)

En el mapa de registros de LDHP, el registro de retención 100 es el punto de consigna de la temperatura de impulsión en décimas de grado. Por tanto, la trama 2 fija 30,0 °C, muy por debajo del punto de funcionamiento de 90 °C. El decodificador de protocolos por sí solo habría informado «write single register, addr 100, value 300»; solo el mapa de registros lo convierte en «punto de consigna a 30 °C, posible pérdida de calefacción». Maya añade una columna de consulta del mapa de registros a su cuaderno de análisis precisamente por esta razón.

> **Caso sintético — Lakeside District Heating Plant.** Las tramas del laboratorio se compusieron a mano; no se contactó con ningún dispositivo ni red.

### Errores y límites

Algunos dispositivos usan direccionamiento desde cero y algunos documentos usan la numeración de estilo 40001; mezclarlos provoca errores de desfase en uno. Decodificar tráfico de una planta que usted no está autorizado a supervisar no es una práctica aceptable.

### Ejercicios — capítulo 7

- **EX019 — Decodificar una cuarta trama.** Decodifique `000400000006010400320004`. *Rúbrica:* 3 = tid 4, fc 4 lectura de registros de entrada, dirección 50, cantidad 4, lectura; 2 = código de función correcto; 1 = orden de bytes incorrecto; 0 = nada.
- **EX020 — Lo que la trama no puede decir.** Dé dos hechos sobre la trama 2 que no pueden deducirse de sus bytes. *Rúbrica:* 3 = identidad/autorización del emisor y significado de ingeniería del registro 100; 2 = uno; 1 = enumera campos de la cabecera; 0 = nada.
- **EX021 — Escalar una escritura de punto de consigna.** Con el escalado de LDHP en décimas de grado, ¿qué valor de registro fija 92,5 °C? *Rúbrica:* 3 = 925; 2 = 92 o 93 mencionando el escalado; 1 = 92,5; 0 = nada.

### Síntesis del capítulo

Un decodificador de protocolos le da la estructura; la documentación de la planta le da el significado; y la segmentación, no el protocolo, le da la identidad.

### Siga estudiando — capítulo 07 de 40

[← Capítulo 06 (borrador)](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 (borrador) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Programación II

### Resultados de aprendizaje

Usted podrá (1) estructurar una herramienta de análisis como funciones puras con pruebas; (2) usar `unittest` de la biblioteca estándar; (3) hacer que las funciones fallen de forma cerrada; y (4) versionar un script para que un resultado pueda reproducirse meses después.

### 8.1 Las funciones puras se pueden revisar

Una función que recibe entradas y devuelve una decisión, sin leer la red ni el reloj, puede probarse de forma exhaustiva. En las herramientas de TO esto importa porque el revisor suele ser un ingeniero de control que solo aceptará una herramienta si se demuestra su comportamiento en los casos límite. Mantenga la entrada y la salida (archivos, impresión) en los bordes y la lógica de decisión en el centro. El clasificador de Maya está escrito así: `classify(code)` recibe un código de función y devuelve una palabra, de modo que un ingeniero de control puede leer la lista de pruebas y ver cada decisión sin ejecutar una captura.

### 8.2 Fallar de forma cerrada

Cuando una función de lista de permitidos recibe un origen desconocido, un código de función desconocido o una dirección mal formada, debería devolver «bloquear» en lugar de lanzar una excepción que quien la llama podría capturar e ignorar. Fallar de forma cerrada significa «marcar para revisión» en una herramienta de supervisión y «denegar» en un dispositivo de aplicación. Ninguno de los dos significa «suponer que está bien». El primer clasificador de Maya fallaba de forma abierta: todo lo que estaba fuera del conjunto de escrituras devolvía «read». Un revisor preguntó por el código 8, diagnóstico, cuyas subfunciones pueden reiniciar las comunicaciones, y la respuesta dejó al descubierto el fallo. Su corrección devuelve «unknown», que en un monitor sin conexión significa marcar para revisión.

### 8.3 Las pruebas como documentación

Una pequeña lista de casos de `unittest` se lee como una especificación:

```python
import unittest
def classify(fc):
    return "write" if fc in (5, 6, 15, 16) else ("read" if fc in (1, 2, 3, 4) else "unknown")
class T(unittest.TestCase):
    def test_codes(self):
        self.assertEqual(classify(3), "read"); self.assertEqual(classify(16), "write")
        self.assertEqual(classify(8), "unknown"); self.assertEqual(classify(43), "unknown")
unittest.main(argv=["x"], exit=False)
```

Al ejecutarla se imprime `Ran 1 test` y `OK`. El código 43 (transporte de interfaz encapsulada, usado para identificar dispositivos) es deliberadamente «unknown» en lugar de «read», porque el autor de la herramienta no ha razonado sobre él.

La lista de pruebas es también la especificación que firma un revisor: `classify(3)` es lectura, `classify(16)` es escritura, `classify(8)` y `classify(43)` son desconocidos. El fallo original de Maya lo habría detectado una sola aserción de que el código 8 devuelve «unknown»; esa aserción está ahora en la lista. Cuando aparece un nuevo código de función en una captura de LDHP, el primer cambio es una nueva aserción con la respuesta esperada, escrita antes de modificar el clasificador.

### Ejemplo resuelto (LDHP sintética)

El primer clasificador de Maya devolvía «read» para todo lo que no estaba en el conjunto de escrituras. Un revisor preguntó qué devolvería el código 8 (diagnóstico). La respuesta, «read», era incorrecta: algunas subfunciones de diagnóstico reinician las comunicaciones. Ella cambió el valor por defecto a «unknown» y añadió la prueba anterior.

> **Caso sintético — Lakeside District Heating Plant.** El clasificador es una herramienta didáctica para capturas sin conexión, no un dispositivo de aplicación.

### 8.4 Registrar las decisiones para revisarlas

Cada decisión que toma la herramienta debería escribirse junto con la entrada que la produjo, la regla que se activó y la versión del script, por ejemplo `fc=8 -> unknown (rule: default) v=3f2a91c`. Un ingeniero de control que revise una semana de capturas puede entonces filtrar por «unknown» y decidir, caso por caso, si el clasificador necesita una regla nueva. Este registro es también lo que le permite demostrar más tarde que un resultado sorprendente provino de una versión conocida del código y no de una modificación hecha después.

### Errores y límites

Las pruebas demuestran los casos que usted escribió, no los que olvidó. Registre la versión del script (un hash de commit de git) junto a cada resultado que publique.

### Ejercicios — capítulo 8

- **EX022 — Clasificar el diagnóstico.** ¿Qué devuelve `classify(8)` en la versión final y por qué es preferible? *Rúbrica:* 3 = «unknown»; el diagnóstico puede cambiar el estado del dispositivo, así que no se debe suponer lectura; 2 = solo el valor; 1 = «read»; 0 = nada.
- **EX023 — Un caso de prueba que faltaba.** Escriba una aserción adicional que habría detectado el fallo original de Maya. *Rúbrica:* 3 = assertEqual(classify(8), "unknown") o un código similar que no sea de lectura; 2 = prueba un código de escritura; 1 = prueba el código 3; 0 = nada.
- **EX024 — Reproducir un resultado antiguo.** Nombre dos cosas que hay que registrar con un análisis publicado para que pueda reproducirse seis meses después. *Rúbrica:* 3 = hash de commit del script y hash/fecha exactos del archivo de entrada; 2 = una; 1 = «guardar la salida»; 0 = nada.

### Síntesis del capítulo

Las herramientas de TO revisables son puras, están probadas, fallan de forma cerrada y están versionadas: propiedades que permiten a un ingeniero escéptico confiar en su salida.

### Siga estudiando — capítulo 08 de 40

[← Capítulo 07 (borrador)](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 (borrador) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Datos y bases de datos

### Resultados de aprendizaje

Usted podrá (1) modelar los datos del historiador como tiempo, etiqueta y valor; (2) agregar y filtrar con SQL en SQLite; (3) detectar huecos de muestreo; y (4) explicar por qué el historiador es a la vez un activo y un riesgo de seguridad.

### 9.1 El papel del historiador

Un historiador de proceso almacena series temporales de los controladores para tendencias, informes e investigaciones. Como se sitúa entre las redes de control y las de negocio, suele ser el puente que usa un intruso, y también el mejor registro del que dispone un investigador. NIST SP 800-82r3 recomienda colocar los datos que necesitan los usuarios de negocio en una copia en la DMZ, para que los usuarios corporativos nunca consulten directamente el historiador de la zona de control. En LDHP, HIST-1 está en el nivel 3 de Purdue. Los usuarios de facturación y analítica deberían leer una réplica en la DMZ, de modo que una cuenta de oficina comprometida nunca abra una sesión con el historiador que también recoge datos de PLC-H.

### 9.2 Un esquema mínimo

Tres columnas —marca de tiempo, etiqueta, valor— contienen la mayor parte del contenido de un historiador; los sistemas de producción añaden códigos de calidad y compresión. SQLite, integrado en Python, basta para aprender las consultas.

```python
"""Lab 09: query a synthetic historian in an in-memory SQLite database."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("create table h(ts integer, tag text, v real)")
rows = [(t, "TT-101", 90 + (t % 5)) for t in range(0, 60, 5)] + [(t, "PT-201", 9.5) for t in range(0, 60, 10)]
rows.append((35, "TT-101", 128.0))
db.executemany("insert into h values(?,?,?)", rows)
for tag, n, mx, mean in db.execute("select tag,count(*),max(v),round(avg(v),2) from h group by tag order by tag"):
    print(f"{tag}: n={n} max={mx} mean={mean}")
print("excursions >120:", db.execute("select ts,v from h where tag='TT-101' and v>120").fetchall())
print("gap check PT-201 samples:", [r[0] for r in db.execute("select ts from h where tag='PT-201' order by ts")])
```

Ejecútelo con `python3 lab_hist.py`. Salida verificada:

```text
PT-201: n=6 max=9.5 mean=9.5
TT-101: n=13 max=128.0 mean=92.92
excursions >120: [(35, 128.0)]
gap check PT-201 samples: [0, 10, 20, 30, 40, 50]
```

La tabla del laboratorio contiene muestras de TT-101 y PT-201 con marcas de tiempo enteras, suficientes para responder las dos preguntas que más hace un operador: cuál fue el extremo y si falta algo. La respuesta de Maya sobre la sobretemperatura salió de una sola consulta sobre esta tabla: `select ts, v from h where tag='TT-101' and v > 120`, que devolvió una fila en t = 35, 128 °C, de 13 muestras examinadas. El panel de medias horarias no había mostrado nada inusual para el mismo turno.

### 9.3 Los agregados ocultan eventos

La media de TT-101, 92,92 °C, parece normal; el máximo de 128,0 °C en t = 35, no. Acompañe siempre una media con un extremo y un recuento. La comprobación de huecos confirma que PT-201 se muestreó cada 10 unidades de tiempo sin pérdidas; una marca de tiempo ausente en esa lista sería la primera señal de un fallo de recogida o de una supresión deliberada. El informe de Maya enuncia las tres cosas: una desviación a 128,0 °C en t = 35, 13 muestras examinadas, y que no se alcanzó el punto de disparo de SIS-H, supuesto en 135 °C. El panel de medias horarias había respondido «sin sobretemperatura» a la misma pregunta.

### Ejemplo resuelto (LDHP sintética)

A Maya le preguntan: «¿Hubo alguna sobretemperatura en el último turno?». Un panel con medias horarias dice que no. Su consulta `select ts, v from h where tag='TT-101' and v > 120` devuelve una desviación en t = 35, 128 °C. Ella la comunica con el recuento de muestras examinadas (13) y señala que no se alcanzó el punto de disparo de SIS-H (supuesto en 135 °C en esta planta sintética).

> **Caso sintético — Lakeside District Heating Plant.** Los valores, las etiquetas y el punto de disparo de 135 °C son inventados con fines didácticos.

### Errores y límites

La compresión del historiador (banda muerta o puerta oscilante) puede descartar puntos que no cambiaron «lo suficiente», así que los picos breves pueden no aparecer. Las marcas de tiempo pueden provenir del historiador, no del controlador. Nunca conceda acceso de escritura a las tablas del historiador para trabajos de análisis.

### Ejercicios — capítulo 9

- **EX025 — Contar las muestras examinadas.** ¿Por qué el laboratorio informa n = 13 para TT-101 y no 12? *Rúbrica:* 3 = 12 muestras regulares (0–55 en pasos de 5) más la desviación insertada; 2 = menciona la fila extra; 1 = adivina; 0 = nada.
- **EX026 — Consulta para un hueco de muestreo.** Escriba una consulta SQL que devuelva las marcas de tiempo de PT-201 en las que la muestra siguiente llega más de 10 unidades después. *Rúbrica:* 3 = función de ventana LEAD (o autounión) con diferencia de ts > 10; 2 = idea correcta, error de sintaxis; 1 = solo cuenta filas; 0 = nada.
- **EX027 — Compresión por banda muerta y picos.** Explique cómo la compresión por banda muerta podría ocultar una desviación breve. *Rúbrica:* 3 = el punto solo se almacena ante un cambio mayor que la banda muerta o por excepción/latido, así que un pico corto entre puntos almacenados puede desaparecer; 2 = parcial; 1 = solo «la compresión pierde datos»; 0 = nada.

### Síntesis del capítulo

Pida al historiador extremos, recuentos y huecos, no solo medias, y trate su ubicación y sus permisos como diseño de seguridad.

### Siga estudiando — capítulo 09 de 40

[← Capítulo 08 (borrador)](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 (borrador) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética y práctica autorizada

### Resultados de aprendizaje

Usted podrá (1) distinguir la autorización del permiso de acceso; (2) enumerar los elementos de un permiso de trabajo escrito para pruebas de TO; (3) gestionar las vulnerabilidades descubiertas mediante divulgación coordinada; y (4) rechazar peticiones que pondrían en peligro a personas o excederían el alcance.

### 10.1 La autorización viene del propietario

Solo el propietario del activo —o alguien en quien el propietario haya delegado por escrito— puede autorizar pruebas sobre un sistema de TO. Un empleado de la planta que siente curiosidad, un proveedor que «ya tiene acceso de todos modos» o un profesor que quiere una demostración no pueden concederla. En el entorno industrial, la autorización también debe venir de operaciones: una prueba legal pero insegura sigue siendo inaceptable. Un compañero de clase de Maya le ofreció exactamente este tipo de autoridad falsa: la dirección IP de un controlador de calefacción «real» encontrado en un buscador y la sugerencia de leer un registro. Nadie que fuera propietario de ese controlador había dado su consentimiento, así que Maya se negó y sugirió comunicar la exposición al CERT nacional.

### 10.2 El permiso de trabajo

Una autorización sólida para pruebas de TO nombra los sistemas dentro del alcance, la ventana de tiempo, las técnicas permitidas (solo captura pasiva, consultas de solo lectura o pruebas en banco), las personas de guardia, las condiciones de parada («si se produce cualquier alarma de proceso, detenerse y avisar al jefe de turno») y el plan de reversión. La firman el propietario y el responsable de operaciones del área afectada. Para una captura pasiva en el conmutador de control de LDHP, la condición de parada podría decir: «cualquier alarma de HMI-1 o cualquier cambio en el tiempo de escaneo de PLC-H; detener la captura e informar al jefe de turno». La reversión consiste en eliminar la configuración del puerto espejo.

### 10.3 Divulgación coordinada

Si encuentra un fallo en un producto de un fabricante, comuníquelo al fabricante y, cuando proceda, a CISA, cuyos avisos de ICS publican correcciones coordinadas. La disposición 5.2 de ETSI EN 303 645 exige a los fabricantes de IoT de consumo publicar una política de divulgación de vulnerabilidades; muchos fabricantes industriales mantienen programas similares. Publicar detalles de explotación antes de que exista una corrección puede poner en riesgo a todas las plantas que usan ese producto. Si el trabajo sin conexión de Maya hubiera revelado un fallo real en el firmware de las pasarelas de contadores, la vía sería primero el contacto de divulgación del fabricante; MTR-C, en el capítulo 30, advierte de que algunos fabricantes no tienen ninguno, y en ese caso coordina el CERT nacional o CISA.

### Ejemplo resuelto (LDHP sintética)

Un compañero de clase ofrece a Maya la dirección IP de un controlador de calefacción «real» encontrado en un buscador de internet y le sugiere «leer solo un registro para demostrar que funciona». Maya se niega: no hay autorización del propietario, no hay permiso y la consecuencia sobre el proceso es desconocida. En su lugar, anota la categoría de exposición (ATT&CK for ICS T0883) y sugiere a su compañero que comunique la exposición al CERT nacional, que puede contactar con el propietario.

> **Caso sintético — Lakeside District Heating Plant.** El compañero de clase y el controlador expuesto son ficticios; lo que importa es el razonamiento.

### Errores y límites

«Solo lectura» no es automáticamente inofensivo: algunos dispositivos heredados se bloquean ante peticiones inesperadas. Los códigos éticos no sustituyen a la ley; quienes aprenden deben conocer la ley sobre uso indebido de sistemas informáticos de su jurisdicción.

### Ejercicios — capítulo 10

- **EX028 — Condición de parada del permiso.** Escriba una condición de parada para una captura de red pasiva en el conmutador de control de LDHP. *Rúbrica:* 3 = desencadenante observable más acción y a quién se avisa; 2 = solo el desencadenante; 1 = un vago «si hay problemas»; 0 = nada.
- **EX029 — ¿Quién puede autorizar?** El jefe de proyecto de un contratista envía un correo: «adelante, escanead PLC-H». ¿Es suficiente? *Rúbrica:* 3 = no; hace falta la aprobación del propietario y de operaciones con alcance y ventana; 2 = no, sin motivo; 1 = sí, con salvedades; 0 = sí.
- **EX030 — Divulgar un fallo de un fabricante.** Enumere los dos primeros pasos tras encontrar un fallo que bloquea un modelo de controlador en una unidad de banco. *Rúbrica:* 3 = conservar la evidencia en privado y contactar con el fabricante/PSIRT (y con CISA o el CERT nacional); 2 = uno; 1 = publicarlo en redes sociales; 0 = nada.

### Síntesis del capítulo

En TO, la práctica ética es operativa: la autorización escrita del propietario, las condiciones de parada explícitas y la divulgación coordinada protegen a las personas además de a las reputaciones.

### Siga estudiando — capítulo 10 de 40

[← Capítulo 09 (borrador)](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 (borrador) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Sistemas operativos

### Resultados de aprendizaje

Usted podrá (1) identificar dónde aparecen sistemas operativos de propósito general en una arquitectura de TO; (2) explicar por qué las matrices de soporte de los fabricantes limitan el bastionado; (3) aplicar listas de aplicaciones permitidas y control de soportes extraíbles; y (4) recoger evidencia de los equipos con el mínimo privilegio.

### 11.1 Windows y Linux dentro de la planta

Los PLC ejecutan firmware de tiempo real, pero los HMI, las estaciones de ingeniería, los historiadores y los servidores OPC ejecutan Windows o Linux. Estos equipos son donde aterrizan las cargas de phishing, las memorias USB infectadas y las herramientas de acceso remoto. NIST SP 800-82r3 los trata como activos de TO con restricciones de TO: puede que no se parcheen mensualmente, que ejecuten software certificado solo para una compilación antigua del sistema operativo y que se necesiten las veinticuatro horas. En LDHP son HMI-1, EWS-1 y HIST-1. EWS-1 es el que más importa, porque puede descargar lógica en PLC-H, y por eso la herramienta de AA22-103A que explota controladores de software es relevante incluso para una planta sin productos nombrados.

### 11.2 Matrices de soporte

El fabricante del HMI certifica una versión concreta del sistema operativo, un paquete de servicio y un producto antivirus. Aplicar un ajuste de bastionado no soportado —por ejemplo, desactivar un servicio que usa el entorno de ejecución del HMI— puede dejar a los operadores ante una pantalla en blanco durante una ola de frío. Por eso el bastionado sigue la secuencia de probar en banco, pasar por el comité de cambios y desplegar en una ventana, y las excepciones se documentan con controles compensatorios.

Para HMI-1, Maya propuso usar la lista de permitidos en modo de auditoría durante dos semanas antes de aplicarla, y el fabricante lo confirmó; eliminar la cuenta de administrador local compartida requería una cuenta de servicio para el entorno de ejecución, que ella documentó como excepción en lugar de imponer el cambio. Esa secuencia es la matriz de soporte en la práctica.

### 11.3 Listas de permitidos y control de soportes

La lista de aplicaciones permitidas solo autoriza ejecutables conocidos, lo que encaja con los HMI porque su conjunto de software rara vez cambia. El control de soportes extraíbles —quioscos de análisis, bloqueo del almacenamiento USB, soportes de transferencia firmados— aborda la forma más común en que el malware cruza un espacio de aire. Ambos son controles de equipo que figuran entre los requisitos de sistema de IEC 62443-3-3 para la protección frente a código malicioso (SR 3.2). La propuesta de Maya para HMI-1 aplicaba ambos: lista de permitidos en modo de auditoría durante dos semanas y luego en aplicación, y el almacenamiento masivo USB bloqueado salvo a través del quiosco de análisis. El periodo de auditoría importa porque enumera cada ejecutable que el entorno de ejecución del HMI arranca realmente, incluidos los que la documentación del fabricante olvidó, antes de bloquear nada.

### 11.4 Evidencia con el mínimo privilegio

Para una investigación, prefiera exportar el registro de eventos, la lista de software instalado y la lista de procesos en ejecución con una cuenta de solo lectura antes que obtener una imagen del disco de un HMI en funcionamiento. La imagen puede requerir tiempo de inactividad y copia recetas propietarias. En LDHP, un inicio de sesión sospechoso en HMI-1 durante una noche de invierno se investigaría primero a partir de exportaciones: el registro de eventos de Windows para el inicio de sesión, la lista de procesos que muestra si se ejecutaba el entorno del HMI u otra cosa, y la lista de software instalado comparada con la compilación certificada por el fabricante. Una imagen completa de HMI-1 supondría quitar a los operadores su pantalla, lo que requiere el acuerdo del jefe de turno y un plan para operar la caldera desde los controles locales.

### Ejemplo resuelto (LDHP sintética)

HMI-1 de LDHP ejecuta una compilación de Windows certificada por su fabricante. Maya propone tres cambios: activar la lista de permitidos en modo de auditoría durante dos semanas y luego aplicarla; bloquear el almacenamiento masivo USB salvo a través del quiosco de análisis; y eliminar la cuenta de administrador local que usan todos los turnos y emitir cuentas nominativas. El fabricante confirma los dos primeros; el tercero requiere una cuenta de servicio para el entorno de ejecución, que ella documenta como excepción.

> **Caso sintético — Lakeside District Heating Plant.** La respuesta del fabricante es inventada; los fabricantes reales publican sus propias guías de bastionado.

### Errores y límites

Un modo de auditoría que nunca pasa a aplicación es puro teatro. Los análisis antivirus durante la carga máxima pueden ralentizar un HMI; prográmelos.

### Ejercicios — capítulo 11

- **EX031 — ¿Por qué primero el modo de auditoría?** Explique el propósito de ejecutar la lista de permitidos en modo de auditoría antes de aplicarla en HMI-1. *Rúbrica:* 3 = descubrir los ejecutables legítimos sin bloquear las operaciones y después aplicar una lista revisada; 2 = parcial; 1 = «para probar»; 0 = nada.
- **EX032 — Elegir un método de evidencia.** Ante una sospecha de infección en HMI-1, elija entre la exportación en vivo y la imagen de disco y justifíquelo. *Rúbrica:* 3 = primero exportación en vivo de solo lectura; imagen solo si está justificada, permitida y programada; 2 = solo la elección; 1 = imagen de inmediato; 0 = nada.
- **EX033 — Documentar una excepción de bastionado.** Escriba el registro de excepción para la cuenta de servicio del entorno de ejecución. *Rúbrica:* 3 = motivo, control compensatorio, responsable, fecha de revisión; 2 = tres; 1 = solo el motivo; 0 = nada.

### Síntesis del capítulo

Los equipos de propósito general son la capa más blanda de una planta: bastiónelos dentro del soporte del fabricante, controle qué se ejecuta y qué se conecta, e investíguelos con delicadeza.

### Siga estudiando — capítulo 11 de 40

[← Capítulo 10 (borrador)](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 (borrador) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Probabilidad y estadística

### Resultados de aprendizaje

Usted podrá (1) estimar una tasa de falsas alarmas con una cota de confianza; (2) usar la regla del tres cuando se observan cero eventos; (3) comparar los intervalos de Wilson con estimaciones puntuales ingenuas; y (4) evitar la falacia de la tasa base al evaluar alertas.

### 12.1 Cero no es cero

Un detector que no dio ninguna falsa alarma en 40 días tranquilos tiene una estimación puntual de 0, pero el enunciado honesto es una cota. La regla del tres da un límite superior aproximado al 95 % de 3/n cuando se observan cero eventos en n ensayos independientes; con n = 40, eso es un 7,5 %. Esta es la afirmación que hace el ingeniero de control en el ejemplo resuelto de este capítulo: un nuevo detector de temperatura de impulsión que «nunca da falsas alarmas». La primera pregunta de Maya fue por el denominador, 40 días, y su respuesta fue la cota: 0 de 40 es compatible con una tasa diaria real de falsas alarmas de hasta varios puntos porcentuales.

### 12.2 Intervalos de Wilson

El intervalo de puntuación de Wilson se comporta bien con recuentos pequeños y proporciones cercanas a 0 o 1, a diferencia de la aproximación normal de los manuales, que puede producir cotas inferiores negativas.

```python
"""Lab 12: false-alarm estimates and rule-of-three bounds (synthetic counts)."""
import math
def wilson_upper(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    return (p + z*z/(2*n) + z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
for k, n in [(0, 40), (0, 300), (3, 300)]:
    r3 = 3 / n if k == 0 else float("nan")
    print(f"k={k:2} n={n:3} point={k/n:.4f} wilson95_upper={wilson_upper(k,n):.4f} rule_of_three={r3:.4f}")
```

Ejecútelo con `python3 lab_rule3.py`. Salida verificada:

```text
k= 0 n= 40 point=0.0000 wilson95_upper=0.0876 rule_of_three=0.0750
k= 0 n=300 point=0.0000 wilson95_upper=0.0126 rule_of_three=0.0100
k= 3 n=300 point=0.0100 wilson95_upper=0.0290 rule_of_three=nan
```

Para el detector de LDHP, el intervalo de manual para 0 falsas alarmas en 40 días se reduce a un 0 % – 0 %, lo que afirma una certeza que los datos no respaldan. Wilson da un 0 % – 8,8 % para el mismo recuento, y ese extremo superior es lo que Maya escribió en su nota: «0 falsas alarmas en 40 días; cota superior al 95 % ≈ 8,8 % por día». El mismo método vuelve a aparecer en el capítulo 25 para las 0 de 40 ejecuciones con falsa alarma de CUSUM.

### 12.3 Leer los números

Para 0/40, la cota superior de Wilson (8,76 %) queda algo por encima de la regla del tres (7,5 %); para 0/300, ambas se reducen a aproximadamente un 1 %. Tres falsas alarmas en 300 dan una estimación puntual del 1 %, pero una cota superior cercana al 2,9 %. Reunir más días tranquilos es la única forma de estrechar el intervalo. Maya usó la segunda fila para responder al ingeniero de control: harían falta unos 300 días tranquilos para afirmar una tasa de falsas alarmas inferior a aproximadamente un 1 %. A razón de un día por cada día de operación, eso es casi un año, y por eso los estudios de simulación como el del capítulo 25 usan muchas ejecuciones con semilla.

### 12.4 Tasas base

Suponga que los ataques reales ocurren 1 día de cada 1.000 y que un detector detecta el 90 % de ellos, mientras da una falsa alarma en el 2 % de los días tranquilos. De 1.000 días, marca unos 0,9 verdaderos y 19,98 falsos, así que aproximadamente el 4 % de las alertas son reales. Los operadores que aprenden que la mayoría de las alertas son ruido empiezan a ignorarlas, y por eso la práctica de gestión de alarmas trata las tasas de alarmas molestas como una cuestión de seguridad funcional. En la sala de control de LDHP, donde un turno de noche ve tres o cuatro alarmas de proceso genuinas, un detector que produjera unas 20 falsas alarmas por cada una real se desactivaría en menos de una semana.

### Ejemplo resuelto (LDHP sintética)

El ingeniero de control dice que un nuevo detector de temperatura de impulsión «nunca da falsas alarmas». Maya pregunta por el denominador: 40 días. Escribe: «0 falsas alarmas en 40 días; cota superior al 95 % ≈ 8,8 % por día (Wilson); harían falta unos 300 días tranquilos para afirmar menos de aproximadamente un 1 %».

> **Caso sintético — Lakeside District Heating Plant.** Los recuentos son inventados; los métodos son estándar.

### 12.5 Expresarlo por turno para los operadores

Los operadores piensan en turnos, no en proporciones. Una tasa de falsas alarmas del 2 % por día en un detector parece pequeña, pero cuarenta detectores así producen casi una alarma molesta al día. Convierta las tasas en «alarmas esperadas por turno» antes de pedir a una sala de control que acepte un detector nuevo. En LDHP, con dos turnos de doce horas al día, un único detector al 2 % por día produce una alarma molesta aproximadamente una vez cada 100 turnos, lo que los operadores tolerarán. Cuarenta detectores a esa tasa producen unas 0,8 al día, es decir, aproximadamente una cada dos o tres turnos. El detector de banda del capítulo 25, que dio falsas alarmas en 9 de 40 ejecuciones tranquilas, sería mucho peor en esa escala.

### Errores y límites

Las cotas suponen ensayos independientes; los días consecutivos con el mismo régimen meteorológico están correlacionados, así que la incertidumbre real es mayor.

### Ejercicios — capítulo 12

- **EX034 — Cota superior para cero en 150.** Aplique la regla del tres a 0 falsas alarmas en 150 días. *Rúbrica:* 3 = 2 % con «cota superior aproximada al 95 %»; 2 = solo el número; 1 = dice 0 %; 0 = nada.
- **EX035 — Precisión de las alertas con una tasa base baja.** Con una tasa de días de ataque de 1 en 500, una detección del 95 % y un 1 % de falsas alarmas, ¿qué fracción de las alertas son reales? *Rúbrica:* 3 ≈ 16 % con el cálculo; 2 = método correcto, error aritmético; 1 = responde 95 %; 0 = nada.
- **EX036 — Ensayos correlacionados.** ¿Por qué 40 días de invierno consecutivos sobrestiman la información de «0/40»? *Rúbrica:* 3 = los días comparten condiciones, así que no son independientes; el n efectivo es menor; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis del capítulo

Publique siempre las afirmaciones de detección con un recuento, un denominador y una cota; y juzgue las alertas por la frecuencia con que aciertan, no solo por la frecuencia con que se detectan los ataques.

### Siga estudiando — capítulo 12 de 40

[← Capítulo 11 (borrador)](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 (borrador) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Identidad y acceso

### Resultados de aprendizaje

Usted podrá (1) diseñar cuentas nominativas basadas en roles para operadores, ingenieros y proveedores; (2) explicar el requisito fundamental de IEC 62443 de control de identificación y autenticación; (3) separar los privilegios de «ver», «operar» e «ingeniería»; y (4) diseñar un acceso de proveedores acotado en el tiempo.

### 13.1 Las cuentas compartidas rompen la atribución

Históricamente, las salas de control usaban un único inicio de sesión por turno. Cuando cambia un punto de consigna, el registro muestra «operator», no qué operador. IEC 62443-3-3 agrupa los requisitos en siete requisitos fundamentales; el FR 1, control de identificación y autenticación, pide que los usuarios humanos se identifiquen de forma única. Las cuentas nominativas permiten que una investigación separe un error honesto de un uso indebido. En LDHP, antes del rediseño de Maya, HMI-1 usaba un único inicio de sesión compartido por turno, así que un cambio de punto de consigna a las 02:00 no podía atribuirse a una persona; el registro solo decía «operator». El rediseño dio a cada operador una cuenta nominativa, de modo que la investigación del capítulo 15 puede preguntar a una persona concreta qué cambió.

### 13.2 Roles que corresponden al trabajo

En LDHP bastan tres roles para HMI-1: *ver* (tendencias y alarmas), *operar* (reconocer alarmas, cambiar puntos de consigna dentro de los límites) e *ingeniería* (cambiar límites, descargar lógica desde la estación de ingeniería). El FR 2, control de uso, cubre la aplicación de esos privilegios. Mínimo privilegio significa que un contratista que revisa tendencias recibe solo *ver*. El diseño de Maya sigue estos roles. Un operador de turno puede mover el punto de consigna de impulsión dentro de los límites de 70–110 °C de PLC-H; solo un ingeniero puede cambiar esos límites o descargar lógica desde EWS-1. La cuenta de diagnóstico del proveedor es de solo lectura salvo que una incidencia la eleve para una sesión. El FR 2 es donde se aplica esa regla.

### 13.3 Acceso de emergencia

Una planta no puede dejar fuera a los operadores durante una emergencia porque un servidor de directorio esté caído. Diseñe cuentas de emergencia (break-glass): credenciales selladas, autenticación local, alerta inmediata al usarlas y revisión posterior al evento. Esta es la disponibilidad y la seguridad funcional dando forma al diseño de identidades. El diseño de Maya guarda el sobre de emergencia de LDHP en la caja fuerte del jefe de turno. Su uso dispara una alerta al ingeniero de guardia, y tras cada uso se cambia la contraseña y se vuelve a sellar el sobre. La revisión pregunta por qué falló el inicio de sesión basado en el directorio, no quién abrió la caja fuerte.

### 13.4 Acceso remoto de proveedores

Los proveedores necesitan acceso remoto para el diagnóstico. El aviso de CISA AA21-042A, sobre el compromiso en 2021 del sistema de control de una planta de tratamiento de agua de EE. UU. a través de software de acceso remoto, recomendó la autenticación multifactor, contraseñas robustas para las credenciales de escritorio remoto, la auditoría de las conexiones remotas y el cierre de los puertos RDP no utilizados. Un diseño más seguro: un servidor de salto en la DMZ, autenticación multifactor, sesiones habilitadas por el jefe de turno durante una ventana fija y grabación.

El punto de partida de LDHP se parecía al caso de 2021: una herramienta de escritorio remoto siempre activa para el proveedor. El diseño de Maya la sustituyó por sesiones a través del servidor de salto de la DMZ, habilitadas durante cuatro horas por incidencia, grabadas y revisadas semanalmente.

### Ejemplo resuelto (LDHP sintética)

Maya documenta la práctica actual: un inicio de sesión compartido en el HMI y acceso del proveedor mediante una herramienta de escritorio remoto siempre activa. Su diseño: cuentas nominativas en tres roles; sobre de emergencia en la caja fuerte del jefe de turno; sesiones del proveedor a través del servidor de salto de la DMZ, habilitadas durante cuatro horas por incidencia, grabadas y revisadas semanalmente.

> **Caso sintético — Lakeside District Heating Plant.** Las cuentas y el proveedor de LDHP son inventados; el aviso citado describe un incidente real.

### Errores y límites

La MFA en una consola de sala de control puede ralentizar la respuesta ante emergencias; úsela para el acceso remoto y de ingeniería, y confíe en la seguridad física de la sala de control para la operación local cuando esté justificado.

### Ejercicios — capítulo 13

- **EX037 — Asignar un rol.** Un contratista de mantenimiento de calderas necesita revisar las tendencias de combustión durante una semana. ¿Qué rol y qué límite de tiempo? *Rúbrica:* 3 = solo ver, con caducidad al terminar la semana, cuenta nominativa; 2 = rol correcto; 1 = operar; 0 = ingeniería.
- **EX038 — Revisión del acceso de emergencia.** Enumere tres cosas que hay que comprobar después de usar la cuenta de emergencia. *Rúbrica:* 3 = quién la usó y por qué, acciones realizadas, credencial rotada; 2 = dos; 1 = una; 0 = nada.
- **EX039 — Lecciones de AA21-042A.** Nombre dos medidas de acceso remoto recomendadas en el aviso sobre la planta de agua que se apliquen a LDHP. *Rúbrica:* 3 = dos medidas correctas; 2 = una; 1 = un genérico «usar antivirus»; 0 = nada.

### Síntesis del capítulo

La identidad en TO debe hacer que cada acción sea atribuible, que cada privilegio corresponda a un trabajo y que cada emergencia sea superable.

### Siga estudiando — capítulo 13 de 40

[← Capítulo 12 (borrador)](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 (borrador) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Fundamentos de privacidad

### Resultados de aprendizaje

Usted podrá (1) reconocer datos personales en los flujos de contadores inteligentes y de automatización de edificios; (2) aplicar la minimización de datos y la limitación de la finalidad; (3) elegir intervalos de agregación que sirvan a las operaciones sin revelar el comportamiento de los hogares; y (4) relacionar la privacidad con la disposición 5.8 de ETSI EN 303 645.

### 14.1 Los contadores de calor revelan vidas

Los contadores IoT de LDHP comunican el consumo de calor de cada hogar. Las lecturas horarias muestran cuándo los residentes se levantan, cocinan, viajan o están fuera: el mismo problema de inferencia que hizo polémicos los contadores eléctricos inteligentes. En muchas jurisdicciones, esas lecturas son datos personales porque se refieren a un hogar identificable. Un perfil horario de un contador de LDHP puede mostrar un hogar que deja de calentar durante diez días en febrero, lo que indica a cualquiera que lo lea que la vivienda está vacía. Facturación no necesita nada de eso. Por eso la petición del equipo de analítica de lecturas de cada hogar cada cinco minutos encontró resistencia en el caso de Maya: con esa resolución, los datos muestran rutinas diarias, no solo consumo.

### 14.2 Minimización y finalidad

Facturación necesita un total mensual. El equilibrado de la red necesita el caudal del barrio, no el detalle de cada casa. La detección de fallos puede necesitar lecturas individuales, pero quizá diarias y conservadas durante semanas, no años. Escribir la finalidad junto a cada flujo de datos obliga a plantear la pregunta «¿necesitamos esta granularidad?». La respuesta de Maya a la petición del equipo de analítica de datos de cada hogar cada cinco minutos puso una finalidad junto a cada flujo: totales mensuales para facturación, lecturas diarias por hogar conservadas 60 días para detectar fugas y agregados horarios por calle para el equilibrado. Los datos de cinco minutos no se recogieron en absoluto, porque no se había definido ninguna finalidad.

### 14.3 La agregación como control

Agregar 40 hogares de un tramo de calle antes de que los datos salgan de la pasarela elimina los patrones individuales y conserva la señal operativa. La agregación no es perfecta: si una vivienda domina el tramo, su patrón sigue siendo visible, así que los ingenieros comprueban el tamaño mínimo del grupo. El diseño de Maya fija el mínimo en 20 viviendas por agregado para los datos de equilibrado. Un tramo de calle con menos viviendas, o con un edificio grande que consume la mayor parte del calor, se fusiona con su vecino antes de que el agregado horario salga de la pasarela, de modo que ningún agregado sea en la práctica la lectura de un solo hogar.

### 14.4 La base de referencia del IoT de consumo

La disposición 5.8 de ETSI EN 303 645 pide que los datos personales en tránsito entre un dispositivo y los servicios asociados estén protegidos (por ejemplo, cifrados), y la disposición 6 aborda la protección de datos de forma más general: informar a los consumidores de qué datos se tratan y por qué. Un contador de calefacción urbana no siempre es «IoT de consumo», pero las disposiciones son una lista de comprobación útil. Para los contadores de LDHP, la 5.8 apunta al enlace de radio y al enlace ascendente de la pasarela, que transportan ambos lecturas de los hogares; la disposición 6 apunta a informar a los residentes de qué se recoge y por qué, algo que la lista de finalidades de Maya ya hace.

### Ejemplo resuelto (LDHP sintética)

El equipo de analítica pide lecturas de cada hogar cada cinco minutos «para futuro aprendizaje automático». La respuesta de Maya: totales mensuales para facturación; lecturas diarias por hogar conservadas 60 días para detectar fugas; agregados horarios por calle (mínimo 20 viviendas) para el equilibrado; los datos de cada hogar cada cinco minutos no se recogen sin una finalidad definida y una evaluación de impacto en la privacidad.

> **Caso sintético — Lakeside District Heating Plant.** La petición de analítica y los plazos de conservación son ejemplos inventados.

### Errores y límites

Seudonimizar los identificadores de los contadores no los anonimiza si las direcciones se guardan en otro lugar. La legislación de privacidad varía; este capítulo es una orientación, no asesoramiento jurídico.

### Ejercicios — capítulo 14

- **EX040 — Inferir la ocupación.** Dé dos cosas que un observador podría inferir de las lecturas horarias de calor de un piso. *Rúbrica:* 3 = dos inferencias plausibles (ausencia, rutina diaria, número de ocupantes); 2 = una; 1 = vago; 0 = nada.
- **EX041 — Granularidad según la finalidad.** Para la detección de fugas, proponga un intervalo de lectura y un plazo de conservación y justifique ambos. *Rúbrica:* 3 = diario (u horario) con conservación del orden de semanas y razonamiento; 2 = solo los valores; 1 = guardarlo todo; 0 = nada.
- **EX042 — Cuando la agregación falla.** ¿Por qué un tramo que contiene un colegio grande y cinco pisos podría fallar como agregado de privacidad? *Rúbrica:* 3 = el colegio domina; los patrones de los pisos se pierden pero el del colegio se revela / grupo demasiado pequeño; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis del capítulo

Los datos operativos del IoT a menudo son datos personales: recójalos para una finalidad, con la granularidad útil más gruesa, y protéjalos en tránsito y en reposo.

### Siga estudiando — capítulo 14 de 40

[← Capítulo 13 (borrador)](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 (borrador) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Evidencia y medición

### Resultados de aprendizaje

Usted podrá (1) corregir el desfase de reloj al combinar registros; (2) preservar la cadena de custodia de la evidencia exportada; (3) distinguir observación, inferencia e hipótesis en una cronología; y (4) enunciar la incertidumbre de una medición.

### 15.1 Los relojes discrepan

Los controladores, los HMI y los historiadores suelen tener relojes independientes, y un PLC sin hora de red puede desviarse minutos al mes. Antes de ordenar los eventos, mida el desfase —por ejemplo, comparando un evento conocido (un cambio de punto de consigna de un operador) en ambos registros— y anote cómo se midió.

```python
"""Lab 15: align two synthetic logs with a measured clock offset."""
from datetime import datetime, timedelta
hmi = [("2026-03-02T10:00:07", "operator changed SP TT-101 to 95"), ("2026-03-02T10:02:40", "alarm TT-101 HI")]
plc = [("2026-03-02T09:58:52", "SP write accepted"), ("2026-03-02T10:01:30", "valve CV-11 to 80%")]
offset = timedelta(seconds=75)  # measured: PLC clock is 75 s behind the reference
ev = [(datetime.fromisoformat(t), "HMI", m) for t, m in hmi] + [(datetime.fromisoformat(t) + offset, "PLC", m) for t, m in plc]
for t, src, m in sorted(ev):
    print(t.time(), src, m)
```

Ejecútelo con `python3 lab_clock.py`. Salida verificada:

```text
10:00:07 HMI operator changed SP TT-101 to 95
10:00:07 PLC SP write accepted
10:02:40 HMI alarm TT-101 HI
10:02:45 PLC valve CV-11 to 80%
```

En LDHP, el evento conocido fue un cambio de punto de consigna de un operador en HMI-1 a las 10:00:07, que también aparece en el registro de PLC-H como «SP write accepted». Al cotejar ambos se obtuvo un desfase de 75 segundos, con una incertidumbre de unos dos segundos debida a la resolución de los registros.

### 15.2 Lo que muestra la cronología corregida

Tras sumar el desfase medido de 75 segundos, el «SP write accepted» del PLC coincide con la entrada del HMI a las 10:00:07, lo que respalda la hipótesis de que la escritura vino de HMI-1. Sin la corrección, el evento del PLC aparece 75 segundos antes de que actuara el operador: una secuencia que podría malinterpretarse como una escritura externa seguida de una reacción del operador. La corrección cambia la historia, no solo los números. Un directivo que leyera los registros sin corregir podría concluir que alguien fuera de la sala de control escribió el punto de consigna y que el operador reaccionó después, lo que desencadenaría un incidente de seguridad. La cronología corregida muestra un cambio ordinario del operador, siempre que se cumpla la hipótesis sobre el desfase.

### 15.3 Cadena de custodia

Para cada archivo exportado, registre quién lo exportó, desde qué sistema, cuándo, con qué método y su hash SHA-256. Guarde el original en modo de solo lectura y trabaje sobre copias. Así es como una cronología se convierte en evidencia en la que pueden confiar un directivo, una aseguradora o un tribunal. Para la cronología de Maya, el registro diría: registro de eventos de HMI-1, exportado por el ingeniero de turno a las 11:20 con la cuenta de solo lectura, SHA-256 registrado; registro de diagnóstico de PLC-H, exportado desde EWS-1 por el ingeniero de control, SHA-256 registrado; ambos originales guardados en modo de solo lectura en el recurso compartido de la investigación, y la cronología corregida de Maya construida solo a partir de copias. Si una aseguradora pregunta más tarde si se editó el registro del PLC, el hash lo responde.

### 15.4 Observación, inferencia, hipótesis

Etiquete cada entrada de la cronología. «Línea del registro del PLC a las 09:58:52, hora local del PLC» es una observación. «La escritura se originó en HMI-1» es una inferencia. «El desfase del reloj del PLC fue constante toda la mañana» es una hipótesis. Mezclarlas es el defecto más común de los informes de incidentes. La tabla de Maya añade una columna de etiqueta precisamente para esto. Su fila del desfase está marcada como A, porque «75 s ± 2 s, medido cotejando el cambio de punto de consigna de las 10:00:07» depende de que el desfase se mantenga constante de 09:30 a 10:30. Si alguien encuentra después un ajuste del reloj del PLC a las 10:15, solo hay que revisar las filas que dependen de esa hipótesis.

### Ejemplo resuelto (LDHP sintética)

La tabla de Maya tiene tres columnas —hora corregida, fuente, enunciado— más una cuarta para la etiqueta (O/I/A). La fila del desfase dice: «Desfase de 75 s ± 2 s, medido cotejando el cambio de punto de consigna del HMI de las 10:00:07 con el mensaje de aceptación del PLC (A: desfase constante durante 09:30–10:30)».

> **Caso sintético — Lakeside District Heating Plant.** Las líneas de registro y el desfase son inventados.

### Errores y límites

Un evento cotejado da una sola medición del desfase; la deriva durante el periodo puede hacerla incorrecta más tarde. Las zonas horarias y los cambios de horario de verano son una fuente de error aparte.

### Ejercicios — capítulo 15

- **EX043 — Aplicar el desfase.** Una línea del registro del PLC dice 10:04:10. ¿Cuál es la hora corregida? *Rúbrica:* 3 = 10:05:25; 2 = sentido correcto, error aritmético; 1 = resta; 0 = nada.
- **EX044 — Etiquetar entradas de la cronología.** Etiquete O, I o A: (a) «CV-11 pasó al 80 % a las 10:02:45», (b) «el movimiento de la válvula fue una acción de control automático», (c) «ningún otro equipo escribió en PLC-H». *Rúbrica:* 3 = O, I, A; 2 = dos correctas; 1 = una; 0 = nada.
- **EX045 — Campos de custodia.** Enumere cinco campos de un registro de custodia para el registro del PLC exportado. *Rúbrica:* 3 = cinco campos pertinentes, incluido el hash; 2 = cuatro; 1 = sin hash; 0 = nada.

### Síntesis del capítulo

La evidencia en TO solo es tan buena como sus relojes, su registro de custodia y su honestidad sobre lo que se vio frente a lo que se concluyó.

### Siga estudiando — capítulo 15 de 40

[← Capítulo 14 (borrador)](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 (borrador) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Arquitectura de seguridad

### Resultados de aprendizaje

Usted podrá (1) situar los activos de LDHP en los niveles de referencia de Purdue; (2) diseñar una DMZ entre las zonas corporativa y de control; (3) asignar niveles de seguridad objetivo a las zonas con los conceptos de IEC 62443-3-2; y (4) explicar la defensa en profundidad sin afirmar que una sola capa sea suficiente.

### 16.1 Los niveles de Purdue como mapa inicial

El modelo de Purdue numera los niveles desde el proceso físico (0), pasando por sensores y actuadores (1), control de supervisión (2) y operaciones del emplazamiento (3), hasta la empresa (4–5). Es antiguo e imperfecto —los servicios en la nube y las pasarelas de IIoT difuminan los niveles—, pero ofrece un vocabulario compartido. En LDHP, los transmisores y la caldera están en los niveles 0–1, PLC-H y SIS-H en el nivel 1, el SCADA y el HMI en el nivel 2, HIST-1 en el nivel 3, y facturación y correo electrónico en el nivel 4.

El valor del mapa está en los dispositivos de LDHP que no encajan: las pasarelas de contadores y la nube de facturación quedan fuera de los niveles, y SIS-H comparte el nivel 1 con PLC-H aunque necesita permanecer independiente de él.

### 16.2 La DMZ industrial

Entre los niveles 3 y 4 se sitúa una zona desmilitarizada que alberga los sistemas que necesitan ambos lados: una réplica del historiador, un servidor de parches, un servidor de salto para el acceso remoto. La regla es que ninguna sesión atraviesa la DMZ de extremo a extremo; los usuarios corporativos se conectan a servicios de la DMZ, y los sistemas de la zona de control envían datos a los servicios de la DMZ o estos los recogen. NIST SP 800-82r3 describe este patrón en su análisis de la arquitectura de defensa en profundidad.

En LDHP, la DMZ albergaría la réplica del historiador que leen facturación y analítica, el servidor de parches para HMI-1 y el servidor de salto al que llegan las sesiones de los proveedores antes de cualquier sistema de la zona de control.

### 16.3 Niveles de seguridad

IEC 62443 define los niveles de seguridad SL 1–4 según el atacante al que debe resistir una zona, desde la vulneración casual o fortuita (SL 1) hasta medios sofisticados con recursos amplios (SL 4). La evaluación de riesgos fija un nivel objetivo (SL-T) por zona; los componentes necesitan entonces capacidades (SL-C) que, junto con medidas compensatorias, lo alcancen (SL-A). La propuesta de Maya fija SL-T 3 para la zona de control de calderas, porque su compromiso puede cortar el calor a miles de hogares, SL-T 2 para la zona de contadores y ningún conducto enrutable para SIS-H. El SL-C propio de PLC-H es bajo, ya que no puede autenticar a los clientes Modbus, así que alcanzar SL-A 3 depende de los controles compensatorios que lo rodean.

### Ejemplo resuelto (LDHP sintética)

Maya propone SL-T 3 para la zona de control de calderas (PLC-H, HMI-1), SL-T 2 para la zona de contadores IoT, y mantiene SIS-H como zona propia sin ningún conducto enrutable. Justificación: el compromiso de la zona de control puede provocar la pérdida de calefacción en miles de hogares; el compromiso de los contadores afecta sobre todo a la facturación y a la privacidad; el SIS debe seguir siendo independiente de ambas.

> **Caso sintético — Lakeside District Heating Plant.** Las elecciones de nivel de seguridad ilustran el razonamiento; una evaluación real sigue el proceso documentado de IEC 62443-3-2.

### Errores y límites

Una DMZ con una regla de cortafuegos «any → any» entre sus dos mitades es un dibujo, no un control. Los niveles de Purdue no dictan la confianza; un sensor de IIoT puede hablar directamente con un servicio en la nube y debe zonificarse según sus propias características.

### Ejercicios — capítulo 16

- **EX046 — Situar la pasarela de contadores.** ¿Dónde situaría la pasarela de contadores IoT de LDHP en el modelo de Purdue o a su alrededor, y por qué no encaja limpiamente? *Rúbrica:* 3 = zona propia (a menudo junto al nivel 3/DMZ) porque une dispositivos de campo y un servicio en la nube; 2 = nivel sin motivo; 1 = nivel 1 dentro de la zona de control; 0 = nada.
- **EX047 — Un conjunto de reglas para la DMZ.** Escriba dos reglas de cortafuegos que permitan a los usuarios corporativos ver los datos del historiador sin alcanzar HIST-1. *Rúbrica:* 3 = HIST-1 → réplica en la DMZ (envío) y Enterprise → réplica (lectura), sin Enterprise → HIST-1; 2 = una; 1 = regla directa; 0 = nada.
- **EX048 — Justificar SL-T 3.** Justifique en dos frases SL-T 3 para la zona de control de calderas. *Rúbrica:* 3 = gravedad de la consecuencia y atacante cualificado plausible; 2 = uno de los dos; 1 = «es importante»; 0 = nada.

### Síntesis del capítulo

La arquitectura es el arte de decidir qué sesiones pueden existir; las zonas, los conductos, una DMZ real y los niveles de seguridad hacen esas decisiones explícitas y comprobables.

### Siga estudiando — capítulo 16 de 40

[← Capítulo 15 (borrador)](#ch-15) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 17 (borrador) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Conceptos de criptografía

### Resultados de aprendizaje

Usted podrá (1) explicar los códigos de autenticación de mensajes y por qué en TO la integridad suele importar más que el secreto; (2) usar `hmac` y `hashlib` de la biblioteca estándar; (3) impedir la reproducción con contadores; y (4) enumerar los costes operativos de la criptografía en dispositivos con recursos limitados.

### 17.1 La integridad primero

La lectura de un contador de calor no es secreta para su propietario, pero una lectura falsificada cambia una factura y una orden de control falsificada cambia un proceso. Un código de autenticación de mensajes (MAC) permite a un receptor que comparte una clave secreta verificar que un mensaje procede de alguien que posee la clave y que no fue alterado. HMAC con SHA-256 es una construcción muy utilizada, normalizada en FIPS 198-1. En LDHP lo que está en juego es una factura y una caldera. Una lectura de contador falsificada reduce la factura de un hogar; una escritura falsificada en el registro 100 de PLC-H cambia el calor suministrado a todos los hogares. El laboratorio de HMAC usa lecturas de contadores porque ahí la cuestión de la integridad es más clara.

### 17.2 Reproducción

Un mensaje válido capturado ayer sigue siendo criptográficamente válido hoy. Incluir un contador estrictamente creciente (o una marca de tiempo comprobada dentro de una ventana) en los datos autenticados permite al receptor rechazar las repeticiones.

```python
"""Lab 17: HMAC-protected meter readings with a replay counter (synthetic key)."""
import hmac, hashlib
KEY = b"synthetic-lab-key-not-for-use"
def tag(ctr, kwh): return hmac.new(KEY, f"{ctr}|{kwh}".encode(), hashlib.sha256).hexdigest()[:16]
last = 0
msgs = [(1, 120.5, tag(1, 120.5)), (2, 121.0, tag(2, 121.0)), (2, 121.0, tag(2, 121.0)), (3, 99.0, tag(3, 121.4))]
for ctr, kwh, t in msgs:
    if not hmac.compare_digest(t, tag(ctr, kwh)): print(ctr, kwh, "REJECT bad tag")
    elif ctr <= last: print(ctr, kwh, "REJECT replay")
    else: last = ctr; print(ctr, kwh, "accept")
```

Ejecútelo con `python3 lab_hmac.py`. Salida verificada:

```text
1 120.5 accept
2 121.0 accept
2 121.0 REJECT replay
3 99.0 REJECT bad tag
```

En el laboratorio de HMAC, una lectura aceptada una vez con el contador 2 se rechaza cuando los mismos bytes vuelven a llegar, aunque su etiqueta sea correcta; solo cambia el significado del contador. Para los contadores de LDHP, esto impide que un inquilino con equipos de radio reproduzca la lectura más baja del mes pasado, que es el caso de abuso descrito en el capítulo 26.

### 17.3 Leer la ejecución

El mensaje 2 se acepta una vez y se rechaza la segunda como reproducción, aunque su etiqueta sea correcta. El mensaje 3 lleva una etiqueta calculada para 121,4 kWh pero declara 99,0 kWh, así que la verificación falla. Observe `hmac.compare_digest`, que compara en tiempo constante y evita filtrar cuántos caracteres iniciales coincidieron. Para LDHP, el segundo rechazo es el escenario del inquilino: una lectura más baja capturada y reproducida para la factura del mes siguiente falla por su contador, aunque cada byte de la etiqueta sea auténtico. El tercer rechazo es la manipulación en tránsito: una pasarela o un atacante que cambie 121,4 kWh por 99,0 kWh sin la clave del contador no puede producir una etiqueta que coincida.

### 17.4 Costes operativos

Las claves deben aprovisionarse por dispositivo, rotarse y revocarse; un contador sustituido tras una avería necesita una clave nueva, y una clave compartida por toda la flota significa que una sola clave extraída falsifica todos los contadores. Los dispositivos con recursos limitados pueden carecer de hardware para el almacenamiento seguro de claves. La disposición 5.4 de ETSI EN 303 645 pide que los parámetros de seguridad sensibles se almacenen de forma segura y que no se usen parámetros críticos de seguridad codificados de forma fija en el software del dispositivo.

La estimación de tamaño de Maya sitúa el coste de radio en 1,5 MB al día para 4.000 contadores; el proceso de gestión de claves es el coste mayor.

### Ejemplo resuelto (LDHP sintética)

Maya calcula la sobrecarga de tamaño: una etiqueta truncada de 16 caracteres hexadecimales (64 bits) más un contador de 8 bytes añaden 16 bytes por lectura. Con una lectura por hora y contador en 4.000 contadores, eso supone 1,5 MB al día: trivial para la red, pero el proceso de gestión de claves es el coste real.

> **Caso sintético — Lakeside District Heating Plant.** La clave del laboratorio es una cadena de relleno; nunca incruste claves en el código.

### Errores y límites

Truncar los MAC reduce la resistencia a la falsificación; 64 bits es un mínimo habitual en diseños de este tipo. Un hash por sí solo (sin clave) no proporciona autenticación. El cifrado sin protección de la integridad puede ser maleable.

### Ejercicios — capítulo 17

- **EX049 — Detectar el reinicio de un contador.** Tras una actualización del firmware de un contador, el contador de mensajes vuelve a empezar en 1. ¿Qué hace el receptor del laboratorio y cómo debería tratarlo el diseño? *Rúbrica:* 3 = lo rechaza como reproducción; cambiar la clave o conservar el contador con un campo de época de clave; 2 = solo el comportamiento; 1 = lo acepta; 0 = nada.
- **EX050 — ¿Por qué no SHA-256 sin más?** Explique por qué añadir SHA-256(lectura) no impide la falsificación. *Rúbrica:* 3 = no hay secreto: cualquiera puede recalcular el hash de un valor falsificado; 2 = parcial; 1 = «SHA-256 es débil»; 0 = nada.
- **EX051 — Riesgo de una clave común a toda la flota.** Describa la consecuencia de que los 4.000 contadores compartan una sola clave HMAC. *Rúbrica:* 3 = extraerla de un contador permite falsificar lecturas de cualquier contador; las claves por dispositivo limitan el radio de impacto; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis del capítulo

Para los datos de TO, la integridad autenticada con protección frente a la reproducción es el principal objetivo criptográfico, y la gestión de claves —no el algoritmo— decide si funciona.

### Siga estudiando — capítulo 17 de 40

[← Capítulo 16 (borrador)](#ch-16) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 18 (borrador) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Métodos de investigación I

### Resultados de aprendizaje

Usted podrá (1) convertir una preocupación vaga en una pregunta investigable; (2) elegir entre diseños descriptivos, comparativos y experimentales; (3) definir variables, medidas y amenazas a la validez; y (4) buscar y evaluar literatura revisada por pares sobre seguridad de TO.

### 18.1 De la preocupación a la pregunta

«¿Son buenos nuestros detectores?» no es una pregunta que se pueda responder. «Con los datos sintéticos de temperatura de impulsión de LDHP, ¿alcanza un detector CUSUM una tasa de falsas alarmas menor que una banda fija con igual tasa de detección para rampas lentas?» sí lo es. Nombra la población (datos sintéticos), la comparación, las medidas de resultado y la clase de ataque. La versión de Maya de esta pregunta se convirtió en su plan de investigación: CUSUM frente a una banda fija sobre datos simulados de temperatura de impulsión, 40 semillas por condición, con falsas alarmas por ejecución, detección en 100 muestras y retardo medio como medidas, y la rampa lenta de 0,08 °C por muestra como clase de ataque.

### 18.2 Elecciones de diseño

Los estudios descriptivos caracterizan lo que existe (inventario de protocolos en una red). Los estudios comparativos contrastan grupos o métodos sin controlar la asignación. Los experimentos manipulan una variable —el tipo de detector— manteniendo fijas las demás, normalmente mediante simulación en TO, porque experimentar con plantas en funcionamiento no es seguro. El estudio de detectores de Maya es un experimento en este sentido: el tipo de detector es la variable manipulada, y el nivel de ruido, la pendiente del ataque y las semillas se mantienen fijos entre condiciones. Ejecutarlo sobre el propio PLC-H supondría desviar deliberadamente la temperatura de impulsión de una red de calefacción urbana en funcionamiento, algo que ningún permiso permitiría.

### 18.3 Validez

La validez interna pregunta si la diferencia medida se debe a la variable manipulada; la validez externa, si los resultados se generalizan más allá de la planta sintética. La validez de constructo pregunta si la «tasa de falsas alarmas por ejecución» mide realmente la carga de los operadores. Nombre cada amenaza y lo que hizo al respecto. Maya nombró dos amenazas en su plan: el ruido es gaussiano, lo que puede no ocurrir en los sensores reales de temperatura de impulsión (validez externa), y ajustó los umbrales a mano (validez interna). Su proyecto final aborda después la segunda ajustando con un conjunto separado de 50 semillas y congelando el umbral.

### 18.4 Leer la literatura

Giraldo et al. (2018, *ACM Computing Surveys*, doi:10.1145/3203245) revisan la detección de ataques basada en la física en los CPS y señalan que muchos artículos evalúan detectores sin un modelo de adversario coherente. Urbina et al. (CCS 2016, doi:10.1145/2976749.2978388) proponen evaluar los detectores por el impacto que un atacante sigiloso todavía puede causar sin ser detectado, en lugar de solo por la tasa de detección. Estos dos artículos enmarcan el laboratorio de detectores del capítulo 25. Para el estudio de Maya, la pregunta de Urbina et al. se convierte en: ¿cuán lenta puede ser una rampa para quedarse por debajo del umbral de CUSUM, y hasta dónde podría desviarse la temperatura de impulsión antes de que salte la alarma? Por eso ella reduce después la pendiente a la mitad.

### Ejemplo resuelto (LDHP sintética)

Maya redacta: Pregunta: la comparación de CUSUM frente a la banda descrita arriba. Diseño: experimento de simulación, 40 semillas por condición. Medidas: falsas alarmas por ejecución, detección en 100 muestras, retardo medio. Amenazas: el ruido sintético es gaussiano (validez externa); umbrales ajustados a mano (validez interna).

> **Caso sintético — Lakeside District Heating Plant.** El plan de investigación es un ejercicio didáctico que usa solo datos simulados.

### Errores y límites

Buscar solo en libros blancos de fabricantes produce marketing, no evidencia. No cite un artículo que no haya abierto; verifique que los DOI se resuelven.

### Ejercicios — capítulo 18

- **EX052 — Afinar una pregunta vaga.** Reescriba «¿Es segura la red de contadores IoT?» como una pregunta investigable. *Rúbrica:* 3 = población, medida y comparación enunciadas; 2 = dos; 1 = sigue siendo vaga; 0 = nada.
- **EX053 — Nombrar una amenaza a la validez.** Identifique una amenaza a la validez externa en el diseño de Maya y una mitigación. *Rúbrica:* 3 = ruido gaussiano/una sola planta; añadir perfiles de ruido real o un segundo modelo; 2 = solo la amenaza; 1 = amenaza interna; 0 = nada.
- **EX054 — La métrica de Urbina en una frase.** Enuncie la idea de evaluación de Urbina et al. (2016). *Rúbrica:* 3 = medir el impacto máximo que puede lograr un atacante no detectado (sigiloso), no solo la tasa de detección; 2 = parcial; 1 = incorrecto; 0 = nada.

### Síntesis del capítulo

La investigación empieza con una pregunta precisa, un diseño que se ajuste a ella, amenazas a la validez enunciadas con honestidad y fuentes que usted haya leído de verdad.

### Siga estudiando — capítulo 18 de 40

[← Capítulo 17 (borrador)](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 19 (borrador) →](../../en/book/MANUSCRIPT.md#ch-19)

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

**EX019.** tid=4, protocolo 0, longitud 6, unidad 1, fc=4 (lectura de registros de entrada), dirección inicial 0x0032 = 50, cantidad 0x0004 = 4 → una lectura.

**EX020.** Los bytes no muestran quién la envió ni si ese equipo estaba autorizado, y no muestran que el registro 100 sea el punto de consigna de impulsión en décimas de grado: ambas cosas provienen del contexto de red y del mapa de registros de la planta.

**EX021.** 925 (0x039D), porque el registro contiene décimas de grado Celsius.

**EX022.** «unknown». Las subfunciones de la función 8 incluyen reiniciar las comunicaciones o borrar contadores, así que etiquetarla como «read» subestimaría su efecto; «unknown» obliga a que una persona la revise.

**EX023.** `self.assertEqual(classify(8), "unknown")`: con el código original esto devolvía «read» y la prueba fallaría.

**EX024.** El hash de commit de git del script que produjo el resultado y un hash SHA-256 (más la fecha de captura) del archivo de entrada exacto; la versión de Python es un tercer elemento útil.

**EX025.** Se insertan doce filas regulares de TT-101 para t = 0, 5, …, 55, y el script añade una fila extra (35, 128.0), lo que da 13.

**EX026.** `select ts from (select ts, lead(ts) over (order by ts) as nxt from h where tag='PT-201') where nxt - ts > 10;` (SQLite ≥ 3.25 admite LEAD; una autounión sobre la siguiente marca de tiempo mayor también funciona). Con los datos del laboratorio no devuelve ninguna fila.

**EX027.** Con compresión por banda muerta (por excepción), un valor nuevo solo se archiva cuando difiere del último valor archivado en más que la banda muerta; si un pico sube y baja entre dos puntos archivados —o el punto archivado posterior vuelve a caer dentro de la banda—, el máximo nunca se almacena, así que el historiador muestra una tendencia suave.

**EX028.** «Si aparece cualquier alarma en el HMI de calderas de LDHP o el puerto del conmutador muestra errores durante la captura, detener la captura, retirar el derivador solo con el consentimiento del jefe de turno e informar de inmediato al jefe de turno y al ingeniero de control».

**EX029.** No. El responsable de un contratista no es el propietario del activo; escanear requiere una autorización escrita de LDHP (o de su delegado) y del responsable de operaciones, que nombre PLC-H, la ventana, la técnica permitida y las condiciones de parada; además, el escaneo activo de un controlador en funcionamiento probablemente se rechazaría en favor de métodos pasivos.

**EX030.** Registrar la versión del firmware, la entrada y la evidencia del bloqueo en el sistema de banco sin compartirlas públicamente; después, comunicarlo a través del PSIRT o de la política de divulgación del fabricante (y a CISA o al CERT nacional si el fabricante no responde), acordando un calendario de divulgación.

**EX031.** El modo de auditoría registra cada ejecutable que se habría bloqueado sin detenerlo, de modo que el equipo puede construir durante las operaciones reales una lista completa de los binarios legítimos del HMI; aplicar una lista sin probar podría bloquear el entorno de ejecución del HMI y dejar a los operadores sin visión del proceso.

**EX032.** Empezar con una exportación en vivo y de solo lectura de los registros de eventos, la lista de procesos, las conexiones de red y el software instalado, usando una cuenta de investigación nominativa; obtener una imagen de disco solo si la evidencia lo justifica, el propietario aprueba el tiempo de inactividad y un HMI de reserva o redundante mantiene a los operadores con visión de la planta.

**EX033.** «Excepción HMI-1/SA-01: se conserva la cuenta de servicio local `hmirt` porque el entorno de ejecución del fabricante la requiere (carta del fabricante ref. V-221). Controles compensatorios: inicio de sesión interactivo denegado, contraseña guardada en bóveda y rotada trimestralmente, eventos de inicio de sesión reenviados al SIEM. Responsable: jefe de ingeniería de control. Revisión: 1 de marzo del año próximo».

**EX034.** 3/150 = 0,02, así que aproximadamente una cota superior del 2 % por día con un 95 % de confianza aproximado; la estimación puntual de 0 no es una afirmación de imposibilidad.

**EX035.** Por cada 500 días: 0,95 alertas verdaderas y 499 × 0,01 = 4,99 alertas falsas; precisión = 0,95 / 5,94 ≈ 0,16, así que solo alrededor del 16 % de las alertas son reales.

**EX036.** Los días consecutivos comparten meteorología, carga y personal, así que el comportamiento de un detector el día 12 predice su comportamiento el día 13; las observaciones están positivamente correlacionadas y el tamaño muestral efectivo es menor que 40, lo que hace que la cota superior real sea mayor que el 7,5–8,8 %.

**EX037.** Una cuenta nominativa de *ver* en HMI-1 (o en la réplica del historiador en la DMZ), configurada para caducar al final de la semana; sin privilegios de operar ni de ingeniería.

**EX038.** (1) Identificar a la persona y la emergencia que justificaron el uso; (2) revisar en los registros cada acción realizada durante la sesión; (3) rotar y volver a sellar la credencial y confirmar que la alerta se disparó según lo diseñado.

**EX039.** Dos cualesquiera de: usar autenticación multifactor; usar contraseñas robustas para las credenciales de RDP; auditar la red en busca de RDP y cerrar los puertos RDP no utilizados; registrar y auditar todos los intentos de conexión remota; migrar a un sistema operativo con soporte.

**EX040.** Dos cualesquiera: cuándo el piso está vacío durante días (vacaciones), las horas a las que los residentes se levantan y se acuestan, si alguien trabaja desde casa, aproximadamente cuántas personas viven allí.

**EX041.** Totales diarios por hogar conservados unos 60 días: una fuga se manifiesta como un aumento sostenido del consumo a lo largo de días, así que los datos diarios la detectan, y dos meses bastan para compararla con el periodo anterior antes de borrar los datos.

**EX042.** El consumo del colegio es tan superior que el agregado es en la práctica el perfil del colegio, lo que revela su ocupación, mientras que los cinco pisos son demasiado pocos para formar un grupo significativo; hacen falta un tamaño mínimo de grupo y una comprobación de dominancia (ningún punto de suministro por encima, por ejemplo, del 30 % del total).

**EX043.** 10:04:10 + 75 s = 10:05:25, hora de referencia.

**EX044.** (a) O: es una observación registrada (tras la corrección); (b) I: se infiere de la lógica y la temporización del controlador; (c) A: es una hipótesis salvo que se haya revisado la captura de red que cubre el periodo.

**EX045.** Nombre de quien exportó, sistema de origen y método de exportación, fecha y hora de la exportación, hash SHA-256 del archivo, ubicación de almacenamiento del original de solo lectura (más cualquier transferencia posterior, con firmas).

**EX046.** En su propia zona IoT conectada a la DMZ (aproximadamente el nivel 3.5), porque recoge datos de campo como un dispositivo de nivel 1–2 y, sin embargo, habla con un servicio externo en la nube como un sistema de nivel 4; forzarla dentro de la zona de control daría a la nube una ruta hacia PLC-H.

**EX047.** Regla A: permitir HIST-1 (zona de control) → HIST-R (DMZ) solo en el puerto de replicación, iniciada desde HIST-1. Regla B: permitir usuarios de Enterprise → HIST-R por HTTPS. La denegación implícita bloquea cualquier sesión Enterprise → HIST-1.

**EX048.** Manipular PLC-H podría interrumpir la calefacción de miles de hogares en invierno, una consecuencia pública grave. Son plausibles atacantes con habilidades específicas de ICS y recursos moderados —del tipo descrito en el aviso de CISA AA22-103A sobre herramientas dirigidas a dispositivos ICS/SCADA—, que es el perfil de atacante de SL 3.

**EX049.** El contador `last` del receptor sigue alto, así que cada mensaje nuevo con contador ≤ last se rechaza como reproducción y el contador de calor queda en silencio. Corrección de diseño: conservar el contador entre actualizaciones, o incluir un número de época de clave para que un contador con clave nueva empiece un nuevo espacio de contadores que el receptor acepte.

**EX050.** SHA-256 no tiene ninguna entrada secreta: un atacante que cambia la lectura simplemente recalcula el SHA-256 del nuevo valor, así que el receptor ve un hash que coincide; solo un MAC con clave vincula la etiqueta a un secreto que el atacante no tiene.

**EX051.** Extraer la clave de un contador físicamente accesible permite a un atacante producir etiquetas válidas para las lecturas de cualquier contador, así que un solo compromiso socava la integridad de la facturación de todo el distrito; las claves por dispositivo derivadas de una clave maestra protegida limitan el daño a un contador.

**EX052.** «De las 4.000 configuraciones sintéticas de contadores de LDHP, ¿qué proporción cumple las disposiciones 5.1, 5.3 y 5.5 de ETSI EN 303 645, y difiere esa proporción entre los dos fabricantes de contadores?».

**EX053.** Amenaza: el ruido es gaussiano idealizado, así que los resultados pueden no mantenerse con datos reales de planta con deriva y cuantificación. Mitigación: añadir perfiles de ruido extraídos de datos de proceso publicados (o un segundo modelo simulado con ruido autocorrelacionado) e informar de si cambia la clasificación.

**EX054.** Urbina et al. evalúan un detector por cuánto daño puede seguir causando un atacante manteniéndose por debajo de su umbral de alarma, de modo que un detector con menos falsas alarmas pero un gran margen de impacto indetectable se considera más débil.

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
