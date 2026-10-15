# Seguridad de TO, IoT y sistemas ciberfísicos: fundamentos de grado y proyecto final

- Idioma: español neutro (`es`); curso de grado, cuatro años; aproximadamente 3.200 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Los capítulos 1–40 de 40 tienen texto didáctico escrito a mano; los ejercicios EX001–EX120 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan la biblioteca estándar de Python 3 y sus salidas se incluyen a partir de ejecuciones reales. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no equivale a un libro terminado.
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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

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

[← Capítulo 17 (borrador)](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 19 (borrador) →](#ch-19)

<a id="ch-19"></a>

## Capítulo 19 — Seguridad de TO, IoT y sistemas ciberfísicos: alcance y teoría

### Resultados de aprendizaje

Usted podrá (1) definir TO, IIoT, IoT de consumo y sistemas ciberfísicos, y dónde se solapan; (2) explicar el lazo de realimentación como el objeto que se protege; (3) identificar las normas centrales de cada ámbito; y (4) describir por qué la ingeniería de seguridad funcional y la de ciberseguridad deben coordinarse.

### 19.1 Definiciones

La tecnología operativa es el hardware y el software que supervisa o controla dispositivos y procesos físicos. NIST SP 800-82r3 amplió su alcance de los «sistemas de control industrial» a la TO en general, incluidas la automatización de edificios y el transporte. Los dispositivos IoT son objetos conectados a la red con capacidad de detección o actuación; NIST IR 8259 enmarca las actividades básicas que los fabricantes deberían realizar para ellos. Un sistema ciberfísico es la combinación de computación, redes y proceso físico en un lazo cerrado.

LDHP contiene los tres: PLC-H y SIS-H son TO, los contadores de calor y las pasarelas son IoT, y el lazo de temperatura de impulsión es un sistema ciberfísico.

### 19.2 El lazo como activo

Lo que protege un defensor de TO no es un computador sino un lazo de realimentación: sensor → controlador → actuador → proceso → sensor. Un atacante puede falsificar la lectura del sensor, cambiar la lógica o los parámetros del controlador, anular el actuador o interrumpir la comunicación que los une. Cada opción corresponde a tácticas de ATT&CK for ICS como *Impair Process Control* e *Inhibit Response Function*. El lazo de LDHP de Maya es TT-101 → PLC-H → válvula de combustible FV-12 → caldera → TT-101. Para cada elemento nombra un ataque y la salvaguarda independiente de él: SIS-H, con su propio transmisor TT-101S, cableado al corte de combustible.

### 19.3 Mapa de normas

IEC 62443 cubre los sistemas de automatización y control industrial para propietarios de activos, integradores y proveedores de productos. NIST SP 800-82r3 es una guía para programas de seguridad de TO. NIST IR 8259 (y 8259A) establece las capacidades básicas de ciberseguridad de los dispositivos IoT para los fabricantes. ETSI EN 303 645 es la base de referencia europea para el IoT de consumo. Se solapan, pero responden a preguntas distintas: quién debe hacer qué, y para qué tipo de sistema. Para LDHP: IEC 62443 para PLC-H y la zona de control, SP 800-82r3 para el programa, IR 8259 y EN 303 645 para los contadores y las pasarelas.

### 19.4 Seguridad funcional y ciberseguridad

La seguridad funcional (IEC 61508, e IEC 61511 para las industrias de proceso) supone fallos aleatorios y sistemáticos; la ciberseguridad supone un adversario. Un sistema instrumentado de seguridad debe mantenerse independiente para que una perturbación del proceso inducida por un ciberataque termine aun así en un estado seguro. Tanto IEC 62443 como IEC 61511 indican a los profesionales que coordinen ambos análisis. En LDHP, SIS-H dispara el corte del suministro de combustible por alta temperatura usando TT-101S, un transmisor separado del TT-101 de PLC-H, y el disparo está cableado. Un ciberataque que lleve a PLC-H a sobrecalentar la caldera sigue encontrándose con un disparo independiente, siempre que nada en la red pueda cambiar el punto de disparo de SIS-H.

### Ejemplo resuelto (LDHP sintética)

Maya traza el lazo de temperatura de impulsión de LDHP: TT-101 → PLC-H → válvula de combustible FV-12 → caldera → TT-101. Enumera un punto de ataque por elemento y la salvaguarda independiente: SIS-H, con su propio transmisor de temperatura TT-101S, cableado al corte de combustible.

> **Caso sintético — Lakeside District Heating Plant.** Las etiquetas del lazo son inventadas.

### Errores y límites

Etiquetas como «TO» e «IoT» son comodidades; un sensor de gestión de edificios conectado por Wi-Fi es ambas cosas. No elija una norma por familiaridad con la marca; elíjala por el rol y el tipo de sistema.

### Ejercicios — capítulo 19

- **EX055 — Cuatro puntos de ataque en un lazo.** Nombre un punto de ataque por cada elemento del lazo de TT-101. *Rúbrica:* 3 = cuatro, uno por elemento; 2 = tres; 1 = dos; 0 = nada.
- **EX056 — Relacionar normas con roles.** ¿Qué documento corresponde a (a) la base de referencia del producto del fabricante de contadores, (b) el propio programa de seguridad de TO de LDHP? *Rúbrica:* 3 = NIST IR 8259 o ETSI EN 303 645 / IEC 62443-4-2; y SP 800-82r3 o IEC 62443-2-1; 2 = uno; 1 = la misma respuesta para ambos; 0 = nada.
- **EX057 — Por qué importa TT-101S.** Explique por qué SIS-H usa su propio transmisor en lugar de leer TT-101 a través de PLC-H. *Rúbrica:* 3 = una ruta TT-101/PLC falsificada o averiada dejaría ciego al SIS; independencia; 2 = parcial; 1 = coste; 0 = nada.

### Síntesis del capítulo

La seguridad de TO, IoT y sistemas ciberfísicos protege lazos de realimentación; la norma adecuada depende de su rol, y la independencia de la seguridad funcional no es negociable.

### Siga estudiando — capítulo 19 de 40

[← Capítulo 18 (borrador)](#ch-18) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 20 (borrador) →](#ch-20)

<a id="ch-20"></a>

## Capítulo 20 — Seguridad de TO, IoT y sistemas ciberfísicos: casos fundamentales

### Resultados de aprendizaje

Usted podrá (1) resumir tres incidentes documentados a partir de fuentes primarias; (2) extraer de cada uno la ruta de ataque y la lección defensiva; (3) distinguir lo que está confirmado públicamente de la especulación; y (4) relacionar cada caso con LDHP.

### 20.1 Red eléctrica de Ucrania, diciembre de 2015

La alerta IR-ALERT-H-16-056-01 del ICS-CERT de EE. UU. informa de que tres empresas regionales ucranianas de distribución de electricidad sufrieron ciberataques coordinados que causaron cortes que afectaron a unos 225.000 clientes. La alerta indica que los actores probablemente usaron credenciales legítimas obtenidas de antemano para el acceso remoto, borraron sistemas con el malware KillDisk, sobrescribieron algunos HMI y corrompieron el firmware de dispositivos de serie a Ethernet en las subestaciones. Se restableció el suministro, pero las empresas siguieron operando con restricciones. Lección: las credenciales robadas y el acceso remoto fueron la ruta, y la recuperación dependió de poder funcionar sin la automatización dañada.

### 20.2 Mirai, 2016

Antonakakis et al. («Understanding the Mirai Botnet», USENIX Security 2017) midieron una botnet que infectó cientos de miles de dispositivos IoT, en gran parte iniciando sesión por Telnet con credenciales de fábrica, y que después lanzó grandes ataques de denegación de servicio. Lección: las contraseñas por defecto universales a escala son un riesgo para la infraestructura, que es exactamente lo que prohíbe la disposición 5.1 de ETSI EN 303 645. El equivalente en LDHP son sus pasarelas de contadores: si se hubieran entregado con una misma contraseña por defecto para toda la flota, un escaneo al estilo de Mirai encontraría cada una de ellas alcanzable desde internet. MTR-B, en el capítulo 30, que no cumple la disposición 5.1, es el modelo de contador en esa situación.

### 20.3 Planta de tratamiento de agua, febrero de 2021

El aviso de CISA AA21-042A describe un acceso no autorizado al sistema SCADA de una planta de tratamiento de agua potable de EE. UU. a través de software de acceso remoto, con un intento de elevar los niveles de hidróxido de sodio. El personal de la planta advirtió el cambio y lo corrigió antes de que saltara la alarma del software SCADA. El aviso señala como debilidades probables un software de escritorio compartido y un sistema operativo al final de su vida útil. Lección: la vigilancia de los operadores importa, y las herramientas de acceso remoto forman parte de la superficie de ataque.

El equivalente en LDHP es su propia herramienta de escritorio remoto del proveedor siempre activa, que Maya sustituyó por sesiones intermediadas de cuatro horas.

### 20.4 Leer los casos con cuidado

Cada fuente documenta algunos hechos y no otros. Escriba lo que dice la fuente, cítela y marque todo lo demás como inferencia. Las versiones divulgativas a menudo añaden una certeza que el informe primario no tiene. La tabla de casos de Maya sigue esta regla. Para la planta de agua de 2021 registra solo lo que afirma AA21-042A —software de acceso remoto, escritorio compartido y un sistema operativo al final de su vida útil— y marca su equivalente en LDHP, la herramienta de escritorio remoto del proveedor siempre activa, como inferencia propia. Para Mirai, el método de infección procede de la medición de Antonakakis et al., no de resúmenes de prensa. Para Ucrania, la lección que extrae, mantener procedimientos documentados de arranque manual de las calderas, está etiquetada como recomendación para LDHP y no como hallazgo de la fuente.

### Ejemplo resuelto (LDHP sintética)

Maya construye una tabla: caso, acceso inicial, efecto, qué lo detuvo, equivalente en LDHP. Para el caso del agua de 2021, el equivalente es la herramienta de escritorio remoto del proveedor siempre activa de LDHP (capítulo 13); para Mirai, las contraseñas por defecto de las pasarelas de contadores; para Ucrania, la necesidad de operar después de que se dañe la automatización: LDHP mantiene procedimientos documentados de arranque manual de las calderas.

> **Caso sintético — Lakeside District Heating Plant.** Solo los equivalentes en LDHP son sintéticos; los tres casos proceden de las fuentes públicas citadas.

### Errores y límites

Las afirmaciones de atribución de las noticias no forman parte de la evidencia de este capítulo. Las lecciones de los casos solo se generalizan cuando las condiciones coinciden.

### Ejercicios — capítulo 20

- **EX058 — Detalles de la fuente primaria.** A partir de la alerta del ICS-CERT de 2016, indique el número aproximado de clientes afectados y una acción de los actores contra los dispositivos de campo. *Rúbrica:* 3 = ~225.000 y firmware de serie a Ethernet corrompido (o KillDisk en los HMI); 2 = uno; 1 = cifra incorrecta; 0 = nada.
- **EX059 — El método de entrada de Mirai.** ¿Qué explotó principalmente Mirai para infectar dispositivos y qué disposición de ETSI lo aborda? *Rúbrica:* 3 = credenciales por defecto por Telnet; disposición 5.1; 2 = uno; 1 = «un día cero»; 0 = nada.
- **EX060 — Hecho frente a inferencia.** Marque como hecho de la fuente o inferencia: (a) «un operador revirtió el cambio de hidróxido de sodio» (b) «el intruso pretendía un envenenamiento masivo». *Rúbrica:* 3 = (a) hecho de AA21-042A, (b) inferencia; 2 = uno; 1 = ambos hechos; 0 = nada.

### Síntesis del capítulo

Lea los incidentes en fuentes primarias, separe los hechos del relato y convierta cada uno en una pregunta concreta sobre su propia planta.

### Siga estudiando — capítulo 20 de 40

[← Capítulo 19 (borrador)](#ch-19) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 21 (borrador) →](#ch-21)

<a id="ch-21"></a>

## Capítulo 21 — Seguridad de TO, IoT y sistemas ciberfísicos: modelos de sistema

### Resultados de aprendizaje

Usted podrá (1) construir un modelo en tiempo discreto de un depósito o de un lazo; (2) explicar el control proporcional y su error en régimen permanente; (3) usar un modelo para predecir con qué rapidez un punto de consigna manipulado cambia el proceso; y (4) enunciar lo que deja fuera un modelo simplificado.

### 21.1 Por qué modelar

Un modelo convierte «el atacante cambia el punto de consigna» en «el nivel alcanza la alarma de rebose en 12 minutos». Los defensores usan ese tiempo para dimensionar la detección y la respuesta: si el proceso da 12 minutos, un detector que tarda 20 es inútil para ese escenario. Para LDHP la pregunta es concreta: si el registro 100 se escribe a 30 °C a las 02:10, ¿cuánto tardan los radiadores del distrito en enfriarse lo suficiente como para que los residentes lo noten, y cuánto hasta que las tuberías de las calles más frías corran peligro? En el ejercicio de mesa del capítulo 29, el operador restableció los 90 °C a las 02:15, cinco minutos después de la alerta. Un modelo le dice si cinco minutos son holgados o están cerca del límite y, por tanto, si la detección tiene que ser la alerta del monitor y no la llamada telefónica de un residente.

### 21.2 Un depósito de compensación con control proporcional

El vaso de expansión de LDHP amortigua el volumen de agua a medida que cambia la temperatura. El laboratorio modela su nivel con un controlador proporcional que fija el caudal de entrada en kp·(punto de consigna − nivel), limitado al rango de 0–5 de la bomba, frente a un caudal de salida constante.

```python
"""Lab 21: discrete-time model of a synthetic buffer tank with a proportional level loop."""
level, sp, kp = 40.0, 60.0, 0.08
for step in range(0, 61):
    inflow = max(0.0, min(5.0, kp * (sp - level) * 10))
    outflow = 2.0
    if step % 10 == 0: print(f"t={step:2} level={level:5.1f}% inflow={inflow:4.2f}")
    level += (inflow - outflow) * 0.5
print("steady-state error ~", round(sp - level, 1), "pct (P-only offset)")
```

Ejecútelo con `python3 lab_tank.py`. Salida verificada:

```text
t= 0 level= 40.0% inflow=5.00
t=10 level= 55.0% inflow=4.00
t=20 level= 57.5% inflow=2.01
t=30 level= 57.5% inflow=2.00
t=40 level= 57.5% inflow=2.00
t=50 level= 57.5% inflow=2.00
t=60 level= 57.5% inflow=2.00
steady-state error ~ 2.5 pct (P-only offset)
```

El laboratorio usa kp = 0,08, multiplicado por 10 en la línea del caudal de entrada para dar una ganancia efectiva de 0,8, un punto de consigna del 60 %, un nivel inicial del 40 % y un caudal de salida fijo de 2,0, así que al principio la bomba funciona en su límite de 5,0. Su salida imprime el nivel cada 10 pasos: 55,0 % en t = 10, y después 57,5 % a partir de t = 20, con un caudal de entrada de 2,01 en t = 20 y de 2,00 a partir de t = 30. Los números son inventados para el vaso de LDHP, pero la forma es general: un lazo proporcional que no llega del todo a su punto de consigna.

### 21.3 Leer el modelo

El nivel sube rápidamente mientras el caudal de entrada está saturado en 5 y después se estabiliza en el 57,5 % en lugar del 60 %. Esa diferencia de 2,5 puntos es el error clásico del control solo proporcional: en equilibrio, el caudal de entrada debe igualar al de salida (2,0), lo que requiere un error distinto de cero (2,0 / 0,8 = 2,5). La acción integral elimina el error; los ingenieros suelen usar control PI o PID. Para la seguridad, este error importa de una forma fácil de pasar por alto: un operador acostumbrado a ver un 57,5 % frente a un punto de consigna del 60 % no notará una pequeña diferencia adicional. Un sesgo del sensor o un cambio modesto del punto de consigna se esconden dentro de una diferencia que todos aceptan ya como normal.

### 21.4 Usar el modelo para la seguridad

Si un atacante mueve el punto de consigna del 60 % al 95 %, el modelo predice cuánto tarda el nivel en superar una alarma de nivel alto en el 85 %. El mismo modelo le dice cómo un sesgo del sensor de +10 puntos haría que el controlador llenara de menos el vaso. Los modelos conectan las acciones cibernéticas con el tiempo del proceso. Para usar el laboratorio de esta forma, cambie en una copia del script el punto de consigna de 60 a 95 en un paso elegido e imprima el primer paso en el que el nivel supera 85; con la bomba limitada a 5,0 frente a un caudal de salida fijo de 2,0, el nivel puede subir como máximo (5,0 − 2,0) × 0,5 = 1,5 puntos por paso. Registre juntas la modificación y la salida. Un sesgo de +10 en el sensor actúa al revés: el controlador ve el nivel 10 puntos más alto de lo que está, así que se estabiliza unos 10 puntos por debajo, y nadie lo ve en HMI-1.

### Ejemplo resuelto (LDHP sintética)

Con la dinámica del laboratorio, con el caudal de entrada saturado en 5 y el de salida en 2, el nivel sube (5 − 2) × 0,5 = 1,5 puntos por paso. Del régimen permanente del 57,5 % a una alarma en el 85 % hay 27,5 puntos, es decir, unos 18–19 pasos. Si un paso representa 20 segundos, los operadores tienen aproximadamente seis minutos.

> **Caso sintético — Lakeside District Heating Plant.** Las ganancias del depósito y la duración del paso son inventadas.

### Errores y límites

Los vasos reales tienen geometría no lineal, dinámica de válvulas y ruido de medición. Un modelo validado en la operación normal puede ser erróneo en los estados extremos que busca un atacante. Nunca derive límites reales de una planta a partir de un modelo de clase.

### Ejercicios — capítulo 21

- **EX061 — Error con una ganancia mayor.** Si kp = 0,16 (ganancia ×10 = 1,6), ¿qué error en régimen permanente predice el modelo? *Rúbrica:* 3 = 2,0 / 1,6 = 1,25 puntos; 2 = método correcto; 1 = dice cero; 0 = nada.
- **EX062 — Tiempo hasta la alarma.** Partiendo del 57,5 % con el caudal de entrada saturado, ¿cuántos pasos hasta que el nivel supere el 70 %? *Rúbrica:* 3 = 9 pasos (57,5 + 1,5 × 9 = 71,0); 2 = 8–9 con razonamiento; 1 = ignora el caudal de salida; 0 = nada.
- **EX063 — Efecto del sesgo del sensor.** Si el sensor de nivel marca 10 puntos de más, ¿dónde se estabiliza el nivel real? *Rúbrica:* 3 = alrededor del 47,5 % (el controlador mantiene el nivel medido en 57,5); 2 = sentido correcto; 1 = 67,5; 0 = nada.

### Síntesis del capítulo

Los modelos de proceso sencillos dan a los defensores un reloj: cuánto tarda un lazo manipulado en causar daño y, por tanto, con qué rapidez deben llegar la detección y la respuesta.

### Siga estudiando — capítulo 21 de 40

[← Capítulo 20 (borrador)](#ch-20) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 22 (borrador) →](#ch-22)

<a id="ch-22"></a>

## Capítulo 22 — Seguridad de TO, IoT y sistemas ciberfísicos: datos y dependencias

### Resultados de aprendizaje

Usted podrá (1) construir un inventario de activos y dependencias; (2) seguir los flujos de datos desde el dispositivo de campo hasta el uso de negocio; (3) encontrar puntos únicos de fallo, incluidas personas y proveedores; y (4) usar una lista de materiales de software para razonar sobre vulnerabilidades heredadas.

### 22.1 Primero, el inventario

No se puede proteger lo que no se ha enumerado. NIST SP 800-82r3 sitúa el inventario de activos al comienzo de un programa de seguridad de TO. Un inventario útil registra no solo fabricante, modelo y firmware, sino también función, zona, responsable, criticidad y qué depende del activo. La lista de dependencias de Maya en este capítulo parte de un inventario así: TT-101, PLC-H con firmware v3.2, FV-12, el conmutador de control SW-2, HMI-1, el servidor de licencias LIC-1, EWS-1 y el contrato de soporte del proveedor. Registrar la v3.2 es lo que permitiría a LDHP responder el mismo día a un aviso sobre el firmware del PLC; registrar LIC-1 como dependencia de HMI-1 es lo que dejó al descubierto un punto único de fallo que ningún diagrama de red mostraba.

### 22.2 Cadenas de dependencia

PLC-H depende de la alimentación de 24 V, de sus módulos de E/S, del conmutador de la red de control, de la estación de ingeniería para los cambios de lógica y del proveedor para el firmware. HMI-1 depende de Windows, del servidor de licencias del entorno de ejecución del HMI y del controlador de dominio para las cuentas nominativas. Una caída del servidor de licencias que deja en blanco los HMI es un incidente de disponibilidad con causa raíz cibernética, aunque no haya ningún atacante.

Maya marcó LIC-1 como el punto único de fallo oculto y preguntó al fabricante del HMI por un periodo de gracia de la licencia, que permitiría a HMI-1 seguir funcionando si LIC-1 estuviera caído durante una noche.

### 22.3 Dependencias de proveedores

El firmware de la pasarela de contadores incorpora una pila TCP/IP de código abierto y una biblioteca TLS. Si se publica una vulnerabilidad en la pila, todas las pasarelas la heredan. Una lista de materiales de software (SBOM) enumera esos componentes para que, cuando aparezca un aviso, la planta pueda responder «¿nos afecta?» en horas y no en semanas. Los avisos de ICS de CISA identifican los productos y versiones afectados, lo que solo sirve si su inventario registra las versiones.

MTR-C, en el capítulo 30, es el caso en que una SBOM no basta: aunque muestre una pila afectada, el dispositivo no puede actualizarse.

### 22.4 Las personas como dependencias

Si solo un ingeniero sabe restaurar la lógica de PLC-H desde la copia de seguridad, esa persona es un punto único de fallo. Documente los procedimientos y forme a más personas. En LDHP el riesgo es mayor de noche en invierno. Si la lógica de PLC-H se corrompiera, por una descarga fallida desde EWS-1 o de forma deliberada, restaurarla requiere el último archivo de programa bueno, la versión de firmware correspondiente (v3.2 en la lista de Maya) y alguien que conozca los pasos de restauración en ese controlador. Si esa persona está de vacaciones en enero, la caldera funciona en control manual local hasta que vuelva. La recomendación de Maya fue un procedimiento de restauración escrito, probado en banco una vez al año por un segundo ingeniero, con el hash del archivo de copia de seguridad registrado junto a cada restauración probada.

### Ejemplo resuelto (LDHP sintética)

Maya redacta la lista de dependencias de la función de temperatura de impulsión: TT-101, PLC-H (firmware v3.2), FV-12, el conmutador de control SW-2, HMI-1, el servidor de licencias LIC-1, la estación de ingeniería EWS-1 y el contrato de soporte del proveedor. Marca LIC-1 como punto único de fallo oculto y recomienda comprobar con el fabricante del HMI el periodo de gracia de la licencia.

> **Caso sintético — Lakeside District Heating Plant.** Las versiones y los nombres son inventados.

### Errores y límites

Un inventario construido solo con escaneo de red omite los dispositivos serie y los repuestos apagados, y el escaneo activo puede perturbar dispositivos frágiles; combine la captura pasiva, las exportaciones de configuración y los recorridos por la planta.

### Ejercicios — capítulo 22

- **EX064 — Campos de un registro de inventario.** Enumere seis campos para una entrada del inventario de activos de TO. *Rúbrica:* 3 = seis, incluidos versión de firmware, zona y criticidad; 2 = cuatro o cinco; 1 = solo fabricante/modelo; 0 = nada.
- **EX065 — Responder a un aviso.** Un aviso de CISA indica como afectadas las versiones 2.0–2.4 de la biblioteca TLS de la pasarela. ¿Qué dos datos del inventario deciden si LDHP está afectada? *Rúbrica:* 3 = versión del firmware de la pasarela y versión del componente en su SBOM; 2 = uno; 1 = solo el nombre del fabricante; 0 = nada.
- **EX066 — Un punto único oculto.** Identifique un punto único de fallo de LDHP que no sea de red y una mitigación. *Rúbrica:* 3 = p. ej., un solo ingeniero, el servidor de licencias, un único repuesto; con mitigación; 2 = solo el punto; 1 = solo un dispositivo de red; 0 = nada.

### Síntesis del capítulo

Los inventarios, las cadenas de dependencia y las SBOM permiten a una planta razonar sobre fallos y avisos antes de que lleguen.

### Siga estudiando — capítulo 22 de 40

[← Capítulo 21 (borrador)](#ch-21) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 23 (borrador) →](#ch-23)

<a id="ch-23"></a>

## Capítulo 23 — Seguridad de TO, IoT y sistemas ciberfísicos: métodos I

### Resultados de aprendizaje

Usted podrá (1) realizar una evaluación de riesgos guiada por las consecuencias para una zona; (2) usar con responsabilidad una matriz de probabilidad y consecuencia; (3) relacionar la evaluación con el flujo de trabajo de IEC 62443-3-2; y (4) registrar el riesgo residual con un responsable.

### 23.1 Empezar por la consecuencia

En TO, la evaluación empieza preguntando qué podría hacer el proceso que resultara inaceptable —pérdida de calefacción en invierno, sobrepresión, escaldaduras— y solo después qué rutas cibernéticas podrían causarlo. Partir de las vulnerabilidades produce largas listas de hallazgos de bajo impacto; partir de la consecuencia centra el esfuerzo en los lazos que importan. En LDHP, los resultados inaceptables son la pérdida de calefacción en 4.000 hogares en invierno y la sobretemperatura en la impulsión. El primero tiene rutas cibernéticas a través del registro 100 y de EWS-1; el segundo también tiene una ruta, pero el disparo independiente de SIS-H limita su consecuencia. Empezar ahí le indica a Maya que examine los conductos de PLC-H antes que las interfaces web de las pasarelas de contadores, aunque las pasarelas producirían más hallazgos en un escaneo.

### 23.2 El flujo de trabajo de 62443-3-2 a grandes rasgos

IEC 62443-3-2 describe identificar el sistema considerado, realizar una evaluación de riesgos inicial de alto nivel, dividirlo en zonas y conductos, realizar una evaluación de riesgos detallada por zona y documentar los requisitos de seguridad y los niveles de seguridad objetivo. No necesita la norma completa para practicar el razonamiento, pero cítela correctamente. Aplicado a LDHP, el sistema considerado es la planta de calderas con sus contadores. La evaluación inicial identifica la pérdida de calefacción como consecuencia dominante. La división produce la zona de control de calderas, la zona de contadores y SIS-H como zona propia. La evaluación detallada por zona produce, respectivamente, el SL-T 3, el SL-T 2 y la ausencia de conductos enrutables de Maya.

### 23.3 Las matrices y sus trampas

Una matriz de 5 × 5 multiplica una puntuación de probabilidad por una de consecuencia. Es una herramienta de comunicación, no aritmética: «3 × 4 = 12» no significa el doble de grave que 6. Los errores de inversión del orden se producen cuando las categorías son amplias. Mantenga siempre el escenario narrado junto a la puntuación. En LDHP, un escenario de toma de control de una pasarela de contadores puntuado 3 × 4 y otro de escritura del punto de consigna en PLC-H puntuado 2 × 5 dan 12 y 10, lo que situaría primero la pasarela. Las narraciones cuentan otra historia: la pasarela afecta a la facturación y la configuración de una calle; la escritura del punto de consigna afecta a la calefacción de todos los hogares. Mantener la narración junto al número es lo que permite a un revisor detectar esa inversión, como hace la clasificación por consecuencias de Maya en el capítulo 26 cuando sitúa la reproducción de un solo inquilino por debajo de la toma de control de la pasarela.

### 23.4 Riesgo residual

Después de los controles queda algo de riesgo. Debe tener un responsable que lo acepte por escrito, una fecha de revisión y las hipótesis en que se basa. Para S-3, la manipulación del punto de consigna, el riesgo residual tras los controles del capítulo 24 tiene dos partes: un empleado interno con acceso de ingeniería y una escritura desde el propio HMI-1, el origen permitido. El proyecto final de Maya demuestra después que la segunda es real: el único fallo que le quedaba a su monitor fue una escritura originada en el HMI. El responsable sería el director de la planta de LDHP, como en el ejemplo resuelto siguiente, que lo acepta por escrito bajo la hipótesis de que las cuentas nominativas hacen atribuibles esas escrituras, con una fecha de revisión seis meses después, o antes si se construye la correlación del monitor con los inicios de sesión de los operadores.

### Ejemplo resuelto (LDHP sintética)

Escenario S-3: malware de la oficina alcanza PLC-H a través de la regla 14 y baja el punto de consigna de impulsión (ATT&CK for ICS T0836). Consecuencia 4 (pérdida de calefacción en todo el distrito durante horas, sin heridos porque SIS-H se ocupa de la sobretemperatura, pero no de la baja temperatura). Probabilidad 3 antes de los controles. Tras eliminar la regla 14 y añadir una lista de permitidos, probabilidad 1. Residual: persiste el empleado interno con acceso de ingeniería; responsable: el director de la planta; revisión en seis meses.

> **Caso sintético — Lakeside District Heating Plant.** Las puntuaciones son ilustrativas.

### Errores y límites

La probabilidad de los ataques dirigidos es un juicio, no una frecuencia; indique quién la juzgó y con qué fundamento. No deje que una puntuación baja oculte una consecuencia catastrófica.

### Ejercicios — capítulo 23

- **EX067 — Primero la consecuencia.** Escriba una consecuencia inaceptable para la zona de contadores IoT y la ruta cibernética que podría causarla. *Rúbrica:* 3 = consecuencia concreta más ruta; 2 = una de las dos; 1 = lista de vulnerabilidades; 0 = nada.
- **EX068 — Interpretar puntuaciones de la matriz.** El escenario A puntúa 2 × 5 = 10 y el B, 5 × 2 = 10. ¿Son igual de urgentes? *Rúbrica:* 3 = no; A tiene una consecuencia catastrófica y necesita otro tratamiento; juzgar por la narración; 2 = solo «no»; 1 = sí; 0 = nada.
- **EX069 — Registro del riesgo residual.** Escriba el enunciado de riesgo residual de S-3 tras los controles. *Rúbrica:* 3 = ruta que persiste, responsable, fecha de revisión, hipótesis; 2 = tres; 1 = «riesgo aceptado»; 0 = nada.

### Síntesis del capítulo

La evaluación guiada por las consecuencias, el uso honesto de las matrices y un riesgo residual con responsable convierten un registro de riesgos de TO en una herramienta de decisión y no en una hoja de cálculo.

### Siga estudiando — capítulo 23 de 40

[← Capítulo 22 (borrador)](#ch-22) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 24 (borrador) →](#ch-24)

<a id="ch-24"></a>

## Capítulo 24 — Seguridad de TO, IoT y sistemas ciberfísicos: controles

### Resultados de aprendizaje

Usted podrá (1) elegir controles preventivos, detectivos y correctivos para un escenario; (2) relacionarlos con los requisitos fundamentales de IEC 62443-3-3; (3) reconocer controles que podrían dañar la disponibilidad o la seguridad funcional; y (4) diseñar controles compensatorios para dispositivos heredados.

### 24.1 Familias de controles

IEC 62443-3-3 agrupa los requisitos de sistema en siete requisitos fundamentales: control de identificación y autenticación (FR 1), control de uso (FR 2), integridad del sistema (FR 3), confidencialidad de los datos (FR 4), flujo de datos restringido (FR 5), respuesta oportuna a los eventos (FR 6) y disponibilidad de los recursos (FR 7). Usarlos como encabezados mantiene equilibrado un plan de controles. La tabla de controles de Maya para S-3 muestra el efecto: cinco controles repartidos entre los FR 1, 3, 5, 6 y 7. Sin los encabezados, un primer borrador tiende a enumerar tres reglas de cortafuegos y nada para la recuperación, que es lo que le concierne al FR 7. Las columnas vacías, aquí FR 2 y FR 4, no son automáticamente carencias, pero cada una necesita una frase que explique por qué no se aplica a este escenario.

### 24.2 Ajustar los controles a S-3

Para el escenario de manipulación del punto de consigna: restringir el flujo de datos con una lista de permitidos en el cortafuegos (FR 5); exigir cuentas nominativas en HMI-1 (FR 1); añadir en la lógica de PLC-H límites de punto de consigna confirmados por el operador (en la práctica, FR 3, y un control de proceso); alertar de las escrituras de punto de consigna desde cualquier equipo distinto de HMI-1 (FR 6); mantener copias de seguridad probadas de la lógica del PLC (FR 7). La tabla de Maya registra completa la fila del límite del punto de consigna: PLC-H rechaza puntos de consigna de impulsión fuera de 70–110 °C salvo que esté activo el modo de ingeniería; FR 3; preventivo; con el modo de fallo de bloquear un cambio legítimo fuera de banda durante la puesta en marcha, mitigado con el modo de ingeniería registrado; responsable, ingeniería de control.

### 24.3 Controles que hacen daño

La prevención activa de intrusiones que descarta escrituras Modbus «sospechosas» puede bloquear una orden de emergencia legítima. El bloqueo de cuentas tras inicios de sesión fallidos puede dejar fuera a un operador durante un incidente. Cada control necesita una pregunta sobre su modo de fallo: si se dispara por error, ¿qué le pasa al proceso? La fila del límite del punto de consigna de Maya plantea esta pregunta y la responde: durante la puesta en marcha se rechazaría un punto de consigna legítimo fuera de 70–110 °C, así que para ese caso existe el modo de ingeniería, con registro. La misma pregunta aplicada a un dispositivo de prevención de intrusiones en línea con PLC-H tiene una respuesta peor: si descarta la escritura de emergencia de un operador durante una avería en una noche fría, el proceso pierde su única vía rápida de recuperación. Por eso LDHP supervisa de forma pasiva y aplica las restricciones con la lista de permitidos del cortafuegos, que bloquea por origen en lugar de adivinar la intención.

### 24.4 Controles heredados y compensatorios

El firmware de PLC-H no puede autenticar a los clientes Modbus. El enfoque compensatorio es rodearlo: limitar los conductos con una lista de permitidos para que solo HMI-1 y HIST-1 puedan alcanzarlo, supervisar el tráfico de forma pasiva y proteger la estación de ingeniería que puede cambiar su lógica. La lista de permitidos del capítulo 27 hace comprobable la primera medida: HMI-1 puede escribir los registros 100–119, HIST-1 solo puede leer y cualquier otro origen queda bloqueado. La supervisión es el sensor pasivo del conmutador de control, y la protección de EWS-1 incluye reenviar sus eventos de carga de controladores de software, que Maya añade tras leer AA22-103A en el capítulo 31. Ninguna de estas medidas cambia PLC-H; juntas deciden quién puede alcanzarlo.

### Ejemplo resuelto (LDHP sintética)

La tabla de Maya tiene las columnas: control, FR, previene/detecta/corrige, modo de fallo, responsable. La fila del límite del punto de consigna dice: «PLC-H rechaza puntos de consigna de impulsión fuera de 70–110 °C salvo que esté activo el modo de ingeniería — FR 3 — previene — modo de fallo: bloquea un cambio legítimo fuera de banda durante la puesta en marcha; mitigado con el modo de ingeniería con registro — responsable: ingeniería de control».

> **Caso sintético — Lakeside District Heating Plant.** Los límites y los responsables son inventados.

### Errores y límites

Los controles enumerados pero no probados no dan ninguna garantía. La relación con los FR muestra la cobertura de las categorías, no que un requisito se cumpla en el nivel de seguridad objetivo.

### Ejercicios — capítulo 24

- **EX070 — Relacionar un control de la zona de contadores.** Dé un control para cada uno de los FR 1, FR 5 y FR 6 en la zona de contadores. *Rúbrica:* 3 = tres controles pertinentes bien relacionados; 2 = dos; 1 = uno; 0 = nada.
- **EX071 — Plantear la pregunta del modo de fallo.** ¿Cuál es el modo de fallo de bloquear las cuentas del HMI tras tres contraseñas erróneas, y qué alternativa es más segura? *Rúbrica:* 3 = operador bloqueado en una emergencia; alerta con retardo o eximir las consolas de la sala de control con seguridad física; 2 = uno; 1 = vago; 0 = nada.
- **EX072 — Compensar un dispositivo que no puede autenticar.** Enumere tres controles compensatorios para una pasarela de contadores que no puede cambiar su contraseña por defecto. *Rúbrica:* 3 = aislar, restringir la interfaz de gestión, supervisar, planificar la sustitución (tres cualesquiera); 2 = dos; 1 = uno; 0 = nada.

### Síntesis del capítulo

Un buen plan de controles de TO cubre los siete requisitos fundamentales, pregunta cómo falla cada control y rodea lo que no se puede corregir.

### Siga estudiando — capítulo 24 de 40

[← Capítulo 23 (borrador)](#ch-23) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 25 (borrador) →](#ch-25)

<a id="ch-25"></a>

## Capítulo 25 — Laboratorio I

### Resultados de aprendizaje

Usted podrá (1) ejecutar un experimento reproducible de detectores con semillas fijas; (2) comparar una banda fija con un detector CUSUM en falsas alarmas, detección y retardo; (3) comunicar resultados con sus denominadores; y (4) relacionar los resultados con la crítica de la evaluación de Urbina et al. (2016).

### 25.1 El experimento

El laboratorio simula la temperatura de impulsión de LDHP a 90 °C con ruido gaussiano (σ = 1 °C). En las ejecuciones con ataque, a partir de la muestra 100 una rampa lenta añade 0,08 °C por muestra: una deriva sigilosa del punto de consigna en el espíritu de ATT&CK for ICS T0836. El detector de banda da la alarma cuando la lectura sale de 90 ± 3,5 °C. CUSUM acumula las desviaciones positivas menos una holgura de 0,5 °C y da la alarma por encima de 12.

```python
"""Lab 25: compare a fixed band and a CUSUM detector on synthetic supply temperature."""
import random
def run(seed, attack):
    rnd = random.Random(seed); s = 0.0; band = cus = None
    for t in range(200):
        x = 90 + rnd.gauss(0, 1.0) + (0.08 * (t - 100) if attack and t >= 100 else 0)
        if band is None and abs(x - 90) > 3.5: band = t
        s = max(0.0, s + (x - 90) - 0.5)
        if cus is None and s > 12: cus = t
    return band, cus
fa_b = sum(run(s, False)[0] is not None for s in range(40)); fa_c = sum(run(s, False)[1] is not None for s in range(40))
det = [run(1000 + s, True) for s in range(40)]
db = [b for b, _ in det if b is not None and b >= 100]; dc = [c for _, c in det if c is not None and c >= 100]
print(f"band : false alarms {fa_b}/40, detections {len(db)}/40, mean delay {sum(b-100 for b in db)/max(1,len(db)):.1f}")
print(f"cusum: false alarms {fa_c}/40, detections {len(dc)}/40, mean delay {sum(c-100 for c in dc)/max(1,len(dc)):.1f}")
```

Ejecútelo con `python3 lab_detect.py`. Salida verificada:

```text
band : false alarms 9/40, detections 37/40, mean delay 28.8
cusum: false alarms 0/40, detections 40/40, mean delay 23.1
```

Con σ = 1 °C, los límites de ±3,5 °C de la banda están a 3,5 desviaciones típicas, así que las falsas alarmas son raras por muestra, pero no por ejecución de 200 muestras.

### 25.2 Interpretar la salida

En 40 ejecuciones tranquilas, la banda dio falsas alarmas en 9 ejecuciones —con σ = 1 °C, una sola muestra más allá de 3,5 σ es rara, pero en 200 muestras por ejecución ocurre—, mientras que CUSUM no dio ninguna. Frente a la rampa, CUSUM detectó las 40 ejecuciones con un retardo medio de 23,1 muestras; la banda detectó 37 de 40 (contando solo las alarmas en la muestra 100 o después) con un retardo medio de 28,8. Como la banda también se dispara con el ruido, algunas de sus «detecciones» son desviaciones afortunadas del ruido.

Las cotas de Wilson concretan la comparación: las 9 ejecuciones con falsa alarma de 40 de la banda dan aproximadamente entre un 12 % y un 38 %.

### 25.3 Comunicar con honestidad

Escriba: «CUSUM 0/40 ejecuciones con falsa alarma (cota superior de Wilson al 95 % ≈ 8,8 %), 40/40 detecciones, retardo medio de 23,1 muestras, semillas 0–39 tranquilas y 1000–1039 con ataque». No escriba «CUSUM es perfecto». Urbina et al. preguntarían además qué rampa podría sostener un atacante por debajo del umbral de CUSUM: una pendiente menor podría evadirlo durante mucho más tiempo. La línea de la banda debe comunicarse de la misma forma: «banda 9/40 ejecuciones con falsa alarma (intervalo de Wilson al 95 % de aproximadamente un 12 % a un 38 %), 37/40 detecciones en la muestra 100 o después, retardo medio de 28,8 muestras». El seguimiento de Maya, que reduce la pendiente a la mitad, a 0,04 °C por muestra, con las mismas semillas, responde a la pregunta de Urbina para un punto de la curva.

### Ejemplo resuelto (LDHP sintética)

Maya reduce la pendiente del ataque a la mitad, a 0,04 °C/muestra, en una copia del script y registra el cambio en el retardo, conservando las semillas. Así convierte un resultado en una curva y muestra el compromiso del atacante entre velocidad y sigilo.

> **Caso sintético — Lakeside District Heating Plant.** Todos los datos son simulados; las semillas hacen reproducible la salida.

### Errores y límites

El ruido gaussiano e independiente es optimista. Los umbrales se fijaron a mano sobre la misma familia de datos con la que se evalúan.

### Ejercicios — capítulo 25

- **EX073 — Leer las ejecuciones con falsa alarma.** Indique el recuento de falsas alarmas del detector de banda y dé una cota superior al 95 % para el de CUSUM. *Rúbrica:* 3 = 9/40 la banda; CUSUM 0/40 con una cota superior de ≈7,5–8,8 %; 2 = uno; 1 = «CUSUM 0 %»; 0 = nada.
- **EX074 — ¿Para qué el término de holgura?** Explique el papel de la holgura de 0,5 °C en CUSUM. *Rúbrica:* 3 = resta el ruido esperado para que la suma tienda a cero en operación normal y solo crezca ante un desplazamiento sostenido; 2 = parcial; 1 = «reduce las alarmas»; 0 = nada.
- **EX075 — Aplicar la crítica del sigilo.** Describa un experimento adicional inspirado en Urbina et al. *Rúbrica:* 3 = barrer la pendiente/el tamaño del ataque para encontrar el mayor impacto no detectado dentro de una ventana de tiempo; 2 = variar el umbral; 1 = solo más semillas; 0 = nada.

### Síntesis del capítulo

Un resultado de laboratorio es un recuento sobre semillas con cotas y un modelo de atacante; cambiar el atacante es el siguiente experimento, no una ocurrencia tardía.

### Siga estudiando — capítulo 25 de 40

[← Capítulo 24 (borrador)](#ch-24) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 26 (borrador) →](#ch-26)

<a id="ch-26"></a>

## Capítulo 26 — Seguridad de TO, IoT y sistemas ciberfísicos: métodos II

### Resultados de aprendizaje

Usted podrá (1) aplicar un modelado de amenazas al estilo STRIDE a un diagrama de flujo de datos del sistema de contadores; (2) traducir las amenazas a técnicas de ATT&CK for ICS cuando proceda; (3) escribir casos de abuso con precondiciones; y (4) priorizar las mitigaciones frente a la clasificación por consecuencias del capítulo 23.

### 26.1 Diagramas de flujo de datos

Dibuje los procesos (círculos), los almacenes de datos (líneas paralelas), las entidades externas (cajas) y los flujos de datos (flechas), y después marque los límites de confianza donde los datos pasan de una zona a otra. El sistema de contadores de LDHP: contadores → pasarela (radio) → pasarela → nube de facturación (TLS) → nube → base de datos de facturación → réplica del historiador (exportación unidireccional para el equilibrado de la red). En LDHP, el enlace de radio de los contadores a la pasarela y el enlace ascendente TLS de la pasarela a la nube de facturación son límites de confianza, y también lo es la exportación unidireccional a la réplica del historiador. Cada límite es donde la tabla STRIDE de Maya hace sus preguntas; un diagrama sin ellos pondría las lecturas de los hogares y los datos de las calderas en la misma zona de confianza.

### 26.2 STRIDE por elemento

Suplantación (*Spoofing*), Manipulación (*Tampering*), Repudio (*Repudiation*), Divulgación de información (*Information disclosure*), Denegación de servicio (*Denial of service*) y Elevación de privilegios (*Elevation of privilege*) dan una lista de preguntas guía. En el enlace de radio contador–pasarela: suplantación (un contador falso), manipulación (lecturas alteradas), divulgación de información (consumo de los hogares). En la pasarela: elevación de privilegios a través de su interfaz web. STRIDE se diseñó para el software, así que añada una pregunta propia de TO: *consecuencia física*, ¿puede esta amenaza cambiar el suministro de calor?

La tabla de Maya produjo 14 amenazas en total. Las tres primeras por consecuencia fueron la toma de control de una pasarela que envía una configuración maliciosa a todos los contadores de su calle, la manipulación de las lecturas en tránsito y el compromiso de una cuenta en la nube que expone el historial de todos los hogares.

### 26.3 Casos de abuso

Un caso de abuso enuncia actor, precondición, acción y resultado. «Un inquilino con equipos de radio y conocimiento del protocolo de los contadores (precondición: no hay autenticación de mensajes en el enlace de radio) reproduce las lecturas más bajas del mes pasado (acción) para que se reduzca la factura (resultado)». Escribir las precondiciones hace evidente la mitigación: autenticar las lecturas y usar contadores, como en el capítulo 17. La reproducción del inquilino ocupa un lugar bajo en la tabla de Maya porque su resultado es una sola factura reducida; aun así, el caso de abuso importa porque el mismo contador ausente permitiría a un atacante con acceso a la pasarela reproducir las lecturas de toda una calle. El laboratorio de HMAC del capítulo 17 muestra la corrección: el mensaje reproducido se rechaza por su contador aunque su etiqueta sea correcta.

### 26.4 Relación con ATT&CK

No todas las amenazas de IoT tienen una técnica de ATT&CK for ICS, y no pasa nada. Cuando la tienen —pasarela alcanzada desde internet (T0883), servicios remotos abusados (T0886)—, registre el identificador para enlazarlo con la inteligencia de amenazas. Para el sistema de contadores de LDHP, T0883 corresponde a una interfaz de gestión de la pasarela alcanzable desde internet, y T0886, al abuso de un servicio remoto usado para gestionar las pasarelas. Las amenazas a nivel de hogar, como la de un inquilino que reproduce la lectura del mes pasado, no tienen técnica de ATT&CK for ICS, porque el marco describe ataques al control industrial y no fraudes de facturación. La tabla de Maya deja esas filas en blanco en la columna de técnica en lugar de forzar una correspondencia pobre, y anota en su lugar la disposición de ETSI EN 303 645 que se aplica.

### Ejemplo resuelto (LDHP sintética)

La tabla de Maya da 14 amenazas. Clasificadas por consecuencia, las tres primeras son: la toma de control de una pasarela que envía una configuración maliciosa a todos los contadores de su calle; la manipulación de las lecturas en tránsito; el compromiso de la cuenta en la nube que expone el historial de todos los hogares. La reproducción por un inquilino queda más abajo: es real, pero se limita a una factura.

> **Caso sintético — Lakeside District Heating Plant.** La lista de amenazas es el resultado de un ejercicio, no la evaluación de un producto real.

### Errores y límites

Un modelo de amenazas solo es tan completo como su diagrama. STRIDE enumera amenazas, no probabilidades. Vuelva a ejecutar el modelo cuando cambie la arquitectura.

### Ejercicios — capítulo 26

- **EX076 — STRIDE en el límite de confianza.** Nombre una amenaza para cada una de S, T y D en el flujo de la pasarela a la nube. *Rúbrica:* 3 = tres amenazas plausibles; 2 = dos; 1 = una; 0 = nada.
- **EX077 — Escribir un caso de abuso.** Escriba un caso de abuso para la interfaz web de la pasarela. *Rúbrica:* 3 = actor, precondición, acción, resultado; 2 = tres; 1 = vago; 0 = nada.
- **EX078 — Situar la reproducción por debajo de la toma de la pasarela.** Justifique la clasificación. *Rúbrica:* 3 = alcance del impacto (una factura frente a una calle entera/la configuración) y consecuencia; 2 = parcial; 1 = solo «menos probable»; 0 = nada.

### Síntesis del capítulo

El modelado de amenazas convierte un diagrama en una lista clasificada de casos de abuso cuyas precondiciones apuntan directamente a las mitigaciones.

### Siga estudiando — capítulo 26 de 40

[← Capítulo 25 (borrador)](#ch-25) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 27 (borrador) →](#ch-27)

<a id="ch-27"></a>

## Capítulo 27 — Seguridad de TO, IoT y sistemas ciberfísicos: verificación

### Resultados de aprendizaje

Usted podrá (1) escribir vectores de prueba para una política de lista de permitidos; (2) incluir casos límite, negativos y de origen desconocido; (3) ejecutar pruebas de conformidad sin conexión antes de cualquier despliegue; y (4) explicar por qué la evidencia de verificación forma parte del ciclo de vida de IEC 62443.

### 27.1 Las políticas necesitan pruebas

Un cortafuegos o una lista de permitidos que entiende el protocolo es código, aunque esté escrito como reglas. Verificar significa mostrar, con evidencia registrada, que la política permite lo que necesitan las operaciones y bloquea lo que debe. IEC 62443-4-1 (ciclo de vida de desarrollo seguro de productos) y las actividades de puesta en marcha del integrador de sistemas esperan ambas pruebas documentadas. La política de LDHP para PLC-H es lo bastante pequeña como para enunciarla en una línea: HMI-1 puede leer con el código de función 3 y escribir los registros 100–119 con el código de función 6, HIST-1 puede leer con los códigos de función 3 y 4, y cualquier otro origen y función queda bloqueado. El laboratorio convierte esa línea en seis vectores con resultados esperados. Una política que nunca se ha ejecutado contra vectores como estos es una conjetura sobre lo que hace el cortafuegos.

### 27.2 Diseñar los vectores

Unos buenos vectores incluyen: cada par permitido (origen, función); cada límite de un rango de registros (primero, último, uno después del último); un origen permitido que usa una función prohibida; un origen desconocido; y una función de escritura que la planta nunca usa (16, escritura múltiple). Los resultados esperados se escriben antes de ejecutar la prueba.

```python
"""Lab 27: conformance test of a Modbus allow-list against a test vector table."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}
WRITE_RANGE = range(100, 120)
def permit(src, fc, reg):
    if (src, fc) not in ALLOW: return "BLOCK"
    if fc == 6 and reg not in WRITE_RANGE: return "BLOCK"
    return "PASS"
vectors = [("HMI-1", 3, 100, "PASS"), ("HMI-1", 6, 119, "PASS"), ("HMI-1", 6, 120, "BLOCK"),
           ("HIST-1", 6, 105, "BLOCK"), ("ENG-WS", 16, 100, "BLOCK"), ("HIST-1", 4, 10, "PASS")]
fails = 0
for src, fc, reg, want in vectors:
    got = permit(src, fc, reg); fails += got != want
    print(f"{src:6} fc={fc:2} reg={reg:3} want={want:5} got={got:5} {'ok' if got == want else 'FAIL'}")
print("failures:", fails, "of", len(vectors))
```

Ejecútelo con `python3 lab_allow.py`. Salida verificada:

```text
HMI-1  fc= 3 reg=100 want=PASS  got=PASS  ok
HMI-1  fc= 6 reg=119 want=PASS  got=PASS  ok
HMI-1  fc= 6 reg=120 want=BLOCK got=BLOCK ok
HIST-1 fc= 6 reg=105 want=BLOCK got=BLOCK ok
ENG-WS fc=16 reg=100 want=BLOCK got=BLOCK ok
HIST-1 fc= 4 reg= 10 want=PASS  got=PASS  ok
failures: 0 of 6
```

En el laboratorio, los seis vectores son: HMI-1 leyendo el registro 100; HMI-1 escribiendo el 119, el último registro permitido; HMI-1 escribiendo el 120, uno después del final; HIST-1 escribiendo el 105; ENG-WS usando la función 16; e HIST-1 leyendo con la función 4.

### 27.3 Leer el resultado

Los seis vectores coinciden. Observe el vector 3: el registro 120 está uno después del final de `range(100, 120)`, así que debe bloquearse: el clásico error de límite por uno. El vector 4 confirma que el historiador no puede escribir ni siquiera dentro del rango escribible. Una ejecución limpia es evidencia solo para estos seis casos; no dice nada del código de función 23 (lectura/escritura múltiple) salvo que usted lo añada. La solicitud de cambio de un colega de Maya muestra cómo se mantienen los vectores: ampliar el rango escribible de HMI-1 para incluir el registro 120, destinado a un nuevo punto de consigna de velocidad de bomba, supuso cambiar a PASS el resultado esperado del vector 3, añadir un vector nuevo (HMI-1, 6, 121, BLOCK) y solo entonces editar `WRITE_RANGE`.

### 27.4 Del laboratorio a la planta

Antes de desplegar una política en el cortafuegos de la zona de control de LDHP, los mismos vectores se reproducen en un entorno de banco con el dispositivo real, primero en modo de supervisión, y el resultado se adjunta a la incidencia de cambio. El modo de supervisión significa que el cortafuegos registra lo que habría bloqueado sin bloquearlo. En LDHP, ese periodo debería cubrir al menos una semana completa, incluida la ejecución del informe semanal y una ventana de mantenimiento, porque un origen legítimo que solo escribe ocasionalmente, como EWS-1 durante un cambio de lógica, aparecería de otro modo por primera vez como una escritura bloqueada en mitad del turno de un operador. La incidencia de cambio lleva entonces los resultados de los vectores en banco, el registro del modo de supervisión y el acuerdo del jefe de turno para aplicar la política.

### Ejemplo resuelto (LDHP sintética)

Un colega propone ampliar el rango escribible de HMI-1 para incluir el registro 120 (un nuevo punto de consigna de velocidad de bomba). Maya cambia primero a PASS el resultado esperado del vector 3, añade el vector (HMI-1, 6, 121, BLOCK), después edita `WRITE_RANGE` a `range(100, 121)` y vuelve a ejecutar. El cambio de las pruebas se revisa junto con el cambio de la política.

> **Caso sintético — Lakeside District Heating Plant.** Los números de registro son inventados.

### Errores y límites

Las pruebas escritas después del código tienden a confirmar lo que hace el código, no lo que necesita la planta. La conformidad sin conexión no demuestra el rendimiento del dispositivo bajo carga.

### Ejercicios — capítulo 27

- **EX079 — Un código de función que falta.** Añada un vector para (HMI-1, 23, 105). ¿Qué debería esperar y qué devuelve el laboratorio? *Rúbrica:* 3 = esperar BLOCK; el laboratorio devuelve BLOCK porque (HMI-1, 23) no está en ALLOW; 2 = uno; 1 = PASS; 0 = nada.
- **EX080 — Límites tras el cambio de rango.** Tras `WRITE_RANGE = range(100, 121)`, enumere los dos vectores de límite que conservaría. *Rúbrica:* 3 = reg 120 PASS y reg 121 BLOCK; 2 = uno; 1 = solo 119; 0 = nada.
- **EX081 — Escribir antes las expectativas.** ¿Por qué escribir los resultados esperados antes de ejecutar? *Rúbrica:* 3 = evita confirmar el comportamiento del código; vincula las pruebas al requisito operativo; 2 = parcial; 1 = «buena práctica»; 0 = nada.

### Síntesis del capítulo

La verificación es una lista escrita de decisiones esperadas, que incluye límites y desconocidos, ejecutada antes del despliegue y conservada como evidencia.

### Siga estudiando — capítulo 27 de 40

[← Capítulo 26 (borrador)](#ch-26) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 28 (borrador) →](#ch-28)

<a id="ch-28"></a>

## Capítulo 28 — Seguridad de TO, IoT y sistemas ciberfísicos: análisis de fallos

### Resultados de aprendizaje

Usted podrá (1) construir un árbol de fallos para la pérdida de la calefacción urbana; (2) combinar puertas AND y OR con probabilidades sencillas; (3) añadir eventos inducidos por ciberataques a un análisis de estilo de seguridad funcional; y (4) usar el análisis de modos de fallo y efectos (AMFE) para una pasarela IoT.

### 28.1 Árboles de fallos

Un árbol de fallos parte de un evento superior no deseado y lo descompone en causas unidas por puertas. Una puerta OR significa que cualquier hijo causa el padre; una puerta AND necesita todos los hijos. Para eventos independientes, P(OR) ≈ suma de las probabilidades cuando son pequeñas, y P(AND) = producto. Para el evento superior de LDHP, el árbol de pérdida de calefacción durante cuatro horas de este capítulo, la puerta OR de la cima significa que basta con una rama cualquiera; la puerta AND bajo la rama (c) significa que el ataque solo tiene éxito si se cumplen sus tres condiciones. Si cada una de esas tres tuviera una probabilidad de 0,1 y fueran realmente independientes, la rama (c) sería 0,001; los párrafos siguientes explican por qué una causa cibernética rompe esa hipótesis.

### 28.2 Añadir eventos cibernéticos

Evento superior: pérdida de calefacción en el distrito durante más de cuatro horas. Hijos de la OR: (a) las dos calderas disparan y no pueden volver a arrancar; (b) las bombas de circulación se detienen; (c) el punto de consigna de impulsión se manipula y no se detecta durante cuatro horas. El evento (c) es a su vez una AND: escritura no autorizada del punto de consigna *y* los operadores no lo advierten *y* el detector falla. Los eventos cibernéticos rompen la hipótesis de independencia: un solo intruso puede causar a la vez varios fallos «independientes», así que trate con cuidado la causa común.

En LDHP, un intruso con acceso a HMI-1 podría escribir el punto de consigna y además silenciar la pantalla de alarmas en la que confían los operadores para advertirlo.

### 28.3 AMFE para la pasarela

El AMFE enumera cada componente, sus modos de fallo, sus efectos, su detección y su gravedad. Los modos de fallo de la pasarela incluyen la pérdida de alimentación (faltan lecturas; se detecta por latido), el firmware corrupto (datos mal formados; se detecta por validación), la manipulación de la configuración (lecturas falsas pero plausibles; difícil de detectar) y la caducidad del certificado (enlace ascendente rechazado; se detecta por supervisión). Para LDHP, la manipulación de la configuración es la fila en la que hay que detenerse: una pasarela configurada para multiplicar cada lectura por 0,9 produce números plausibles que superan las comprobaciones de validación y de latido, y solo aparecería al comparar los totales de las pasarelas con el calor que sale de la planta. Por esta razón la clasificación STRIDE de Maya pone en primer lugar la toma de control de la pasarela. La caducidad del certificado, en cambio, es fácil de detectar y fácil de prevenir con una alerta de renovación, así que ocupa un lugar bajo aunque detenga todas las lecturas.

### Ejemplo resuelto (LDHP sintética)

Probabilidades anuales (ilustrativas): escritura no autorizada 0,05; los operadores no la advierten durante cuatro horas 0,2; el detector falla 0,1. P(c) = 0,05 × 0,2 × 0,1 = 0,001. Las dos calderas no vuelven a arrancar 0,002; bombas 0,003. P(superior) ≈ 0,002 + 0,003 + 0,001 = 0,006 al año. Pero si el intruso también puede suprimir las alarmas del HMI, «los operadores no lo advierten» deja de ser 0,2 y la independencia de la puerta AND se derrumba: P(c) puede acercarse a 0,05 × 1 × 0,1 = 0,005.

> **Caso sintético — Lakeside District Heating Plant.** Todas las probabilidades son inventadas con fines ilustrativos y no deben reutilizarse.

### 28.4 Vista de pajarita

Un diagrama de pajarita sitúa el evento superior en el centro, las amenazas y las barreras preventivas a la izquierda, y las consecuencias con las barreras de mitigación a la derecha. Ayuda a los operadores a ver que SIS-H es una barrera de mitigación para la sobretemperatura, pero no ofrece nada frente a la baja temperatura causada por un punto de consigna rebajado. La contribución de Maya al HAZOP del capítulo 32 señala lo mismo desde el otro lado: el disparo por alta temperatura de SIS-H es la salvaguarda para un punto de consigna manipulado que sobrecalienta la caldera, pero un punto de consigna rebajado a 30 °C, como en el ejercicio de mesa del capítulo 29, causa la pérdida de calefacción sin acercarse nunca a un punto de disparo. Para esa consecuencia, las barreras están a la izquierda de la pajarita: la lista de permitidos del cortafuegos, las cuentas nominativas, los límites de punto de consigna de 70–110 °C de PLC-H y la alerta del monitor.

### Errores y límites

Las probabilidades de los eventos adversarios son juicios; preséntelas como rangos. Los árboles de fallos omiten las interacciones que no se dibujan.

### Ejercicios — capítulo 28

- **EX082 — Calcular una puerta AND cibernética.** Con escritura 0,1, los operadores no lo advierten 0,3 y el detector falla 0,2, calcule P(c). *Rúbrica:* 3 = 0,006; 2 = método correcto; 1 = suma en lugar de multiplicar; 0 = nada.
- **EX083 — Causa común.** Explique cómo una sola intrusión puede romper la independencia de la puerta AND. *Rúbrica:* 3 = el mismo actor suprime las alarmas/ciega al detector, así que los eventos están correlacionados; 2 = parcial; 1 = vago; 0 = nada.
- **EX084 — Una línea de AMFE.** Escriba la fila de AMFE para la caducidad del certificado de la pasarela. *Rúbrica:* 3 = modo, efecto, detección, gravedad, acción; 2 = cuatro; 1 = solo el modo; 0 = nada.

### Síntesis del capítulo

Los árboles de fallos y el AMFE incorporan los eventos cibernéticos a la ingeniería de fiabilidad, siempre que usted cuestione la independencia que a los adversarios se les paga por romper.

### Siga estudiando — capítulo 28 de 40

[← Capítulo 27 (borrador)](#ch-27) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 29 (borrador) →](#ch-29)

<a id="ch-29"></a>

## Capítulo 29 — Seguridad de TO, IoT y sistemas ciberfísicos: operaciones

### Resultados de aprendizaje

Usted podrá (1) diseñar un flujo de trabajo de supervisión de seguridad de TO con los operadores en el circuito; (2) escribir un paso de un manual de respuesta a incidentes que respete la seguridad del proceso; (3) planificar la aplicación de parches dentro de las ventanas de mantenimiento; y (4) dirigir un ejercicio de mesa.

### 29.1 Una supervisión en la que confíen los operadores

La supervisión pasiva de la red en el conmutador de control de LDHP construye una línea base de quién habla con quién. Las alertas —un equipo nuevo que habla Modbus, una escritura desde un origen inesperado, una descarga de firmware— van a un analista de seguridad que llama al jefe de turno antes de que nadie toque la planta. NIST SP 800-82r3 subraya que la respuesta a incidentes en TO debe coordinarse con operaciones, porque las propias acciones de contención pueden causar una perturbación del proceso.

En LDHP, la alerta del ejercicio de mesa de este capítulo, una escritura Modbus en el registro 100 desde 10.20.4.17, en la VLAN de oficina, es exactamente el caso del «origen inesperado».

### 29.2 Pasos del manual

Los buenos pasos de un manual de TO nombran a quien decide y el estado seguro. «Aislar PLC-H de la red» es peligroso si los operadores pierden el HMI. Mejor: «El jefe de turno decide si pasar la caldera a control manual local; solo entonces el analista bloquea el origen sospechoso en el cortafuegos». El ejercicio de mesa de este capítulo siguió este orden: el analista llamó al jefe de turno a las 02:12, el operador restableció el punto de consigna de impulsión de 30 °C a 90 °C a las 02:15 y el jefe de turno aprobó bloquear 10.20.4.17 en el cortafuegos a las 02:18. El bloqueo llegó después de que el proceso estuviera seguro, no antes, y después de que lo decidiera una persona con nombre.

### 29.3 Parches en ventanas

LDHP tiene una ventana de mantenimiento mensual de cuatro horas. Los parches se prueban en un HMI de banco, se clasifican por riesgo (exposición × consecuencia) y se aplican en ese orden hasta llenar la ventana; el resto se aplaza con una incidencia fechada y controles compensatorios. IEC TR 62443-2-3 trata la gestión de parches en entornos IACS. En un mes con una corrección de firmware para PLC-H, una actualización de Windows para HMI-1 y un parche para las pasarelas, la clasificación pone primero a PLC-H solo si la corrección aborda una ruta expuesta; de lo contrario, HMI-1, que alberga las cuentas nominativas de los operadores y está expuesto a EWS-1 y al servidor de salto, puede ir primero. Lo que se aplace recibe una incidencia fechada y los controles compensatorios del capítulo 24.

### 29.4 Ejercicios de mesa

Un ejercicio de mesa ensaya un escenario sobre el papel: a quién se llama, qué se decide, qué información falta. Revela carencias sin poner en riesgo el proceso. El ejercicio de mesa de LDHP partió de una alerta a las 02:10 de una noche de enero: una escritura Modbus en el registro 100 de PLC-H desde 10.20.4.17, en la VLAN de oficina. El analista llamó al jefe de turno a las 02:12, el operador confirmó que el punto de consigna de impulsión había cambiado a 30 °C y restableció 90 °C a las 02:15, y el jefe de turno aprobó bloquear la dirección a las 02:18, tras lo cual comenzó la recogida de evidencia. La carencia que encontró era corriente e importante: nadie tenía el teléfono nocturno del administrador del cortafuegos. Un incidente real habría encontrado la misma carencia con menos tiempo para corregirla.

> **Caso sintético — Lakeside District Heating Plant.** Las horas, las direcciones y la carencia son inventadas.

### Errores y límites

Los manuales se deterioran a medida que cambian el personal y las redes; revíselos después de cada ejercicio. El bloqueo automático en TO debería ser excepcional y acordado de antemano.

### Ejercicios — capítulo 29

- **EX085 — Reescribir un paso peligroso del manual.** Reescriba de forma segura «Apagar de inmediato el servidor SCADA». *Rúbrica:* 3 = quien decide, primero el estado seguro del proceso y después la contención; 2 = parcial; 1 = sin cambios; 0 = nada.
- **EX086 — Llenar una ventana.** Hay parches que necesitan 1,5 h (riesgo 9), 2 h (riesgo 6), 1 h (riesgo 8) y 1 h (riesgo 3) en una ventana de 4 h. ¿Cuáles entran? *Rúbrica:* 3 = riesgo 9, 8 y 3 (3,5 h), con el parche de riesgo 6 aplazado en una incidencia fechada; 2 = conjunto correcto, sin registro del aplazamiento; 1 = se excede de la ventana; 0 = nada.
- **EX087 — Corregir la carencia del ejercicio de mesa.** Proponga una corrección para el número de teléfono que faltaba y cómo probarla. *Rúbrica:* 3 = lista de guardias en el manual más una llamada de prueba en el siguiente ejercicio; 2 = una de las dos; 1 = vago; 0 = nada.

### Síntesis del capítulo

La seguridad de las operaciones de TO mantiene a los operadores al mando del proceso, aplica parches por riesgo dentro de las ventanas y ensaya hasta que las carencias se encuentran sobre el papel y no a las 2 de la madrugada.

### Siga estudiando — capítulo 29 de 40

[← Capítulo 28 (borrador)](#ch-28) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 30 (borrador) →](#ch-30)

<a id="ch-30"></a>

## Capítulo 30 — Laboratorio II

### Resultados de aprendizaje

Usted podrá (1) evaluar una flota IoT sintética frente a disposiciones seleccionadas de ETSI EN 303 645; (2) comunicar las carencias por dispositivo y de toda la flota; (3) relacionar las disposiciones con las actividades de los fabricantes de NIST IR 8259; y (4) priorizar la remediación.

### 30.1 La base de referencia

ETSI EN 303 645 V2.1.1 establece 13 disposiciones de ciberseguridad para el IoT de consumo, más disposiciones de protección de datos. Este laboratorio comprueba cuatro: 5.1 (sin contraseñas por defecto universales), 5.2 (implantar un medio para gestionar los informes de vulnerabilidades), 5.3 (mantener el software actualizado) y 5.5 (comunicar de forma segura). NIST IR 8259 cubre un terreno similar desde el lado del proceso del fabricante, por ejemplo, la planificación de las actualizaciones y la comunicación con los clientes.

```python
"""Lab 30: score a synthetic IoT meter fleet against selected ETSI EN 303 645 provisions."""
fleet = {"MTR-A": {"unique_pw": True, "vuln_policy": True, "update": True, "tls": True},
         "MTR-B": {"unique_pw": False, "vuln_policy": True, "update": True, "tls": True},
         "MTR-C": {"unique_pw": True, "vuln_policy": False, "update": False, "tls": False}}
PROV = {"unique_pw": "5.1 no universal default passwords", "vuln_policy": "5.2 vulnerability disclosure",
        "update": "5.3 software updatable", "tls": "5.5 secure communication"}
for dev, f in fleet.items():
    miss = [PROV[k] for k, v in f.items() if not v]
    print(f"{dev}: {4-len(miss)}/4 met; missing: {miss or 'none'}")
print("fleet-wide gaps:", sorted({k for f in fleet.values() for k, v in f.items() if not v}))
```

Ejecútelo con `python3 lab_fleet.py`. Salida verificada:

```text
MTR-A: 4/4 met; missing: none
MTR-B: 3/4 met; missing: ['5.1 no universal default passwords']
MTR-C: 1/4 met; missing: ['5.2 vulnerability disclosure', '5.3 software updatable', '5.5 secure communication']
fleet-wide gaps: ['tls', 'unique_pw', 'update', 'vuln_policy']
```

Los tres modelos de contador del laboratorio responden a un breve cuestionario sobre esas cuatro disposiciones; el script informa de cuáles cumple cada uno y de lo que le falta a la flota.

### 30.2 Leer el resultado de la flota

MTR-A cumple las cuatro. MTR-B solo incumple la 5.1, lo que se corrige forzando credenciales únicas en la instalación. MTR-C incumple tres disposiciones: no tiene política de divulgación, ni mecanismo de actualización, ni comunicación segura. La lista de carencias de toda la flota contiene las cuatro disposiciones, lo que parece alarmante pero se debe solo a dos modelos; comunique ambas vistas. La vista por dispositivo le dice a Maya qué corregir en cada modelo de contador, mientras que la vista de la flota le dice al director de LDHP qué disposiciones faltan en algún punto del parque. Leer solo la lista de la flota sugeriría cuatro problemas distintos en todos los contadores, cuando MTR-A está limpio y tres de las cuatro carencias recaen solo en MTR-C.

### 30.3 Priorizar

La gravedad depende de la consecuencia y de la facilidad de corrección. La falta de capacidad de actualización de MTR-C es estructural —no se puede parchear—, así que la planificación de su sustitución empieza ya. La contraseña por defecto de MTR-B es el vector clásico de Mirai (capítulo 20) y es urgente, pero barata. La tabla de remediación de Maya sigue ese orden. MTR-B se corrige en dos semanas, en la siguiente visita de lectura de contadores. MTR-C recibe de inmediato controles compensatorios —aislamiento detrás de la pasarela, con TLS terminado allí— y una sustitución programada en 12 meses, porque ningún cambio de configuración puede cumplir la 5.3. MTR-A no necesita nada por ahora, pero se vuelve a comprobar cada vez que cambia su firmware, ya que un resultado favorable describe una sola versión.

### 30.4 Límites de la evaluación por lista de comprobación

«Cumple la 5.3» es en este laboratorio un booleano procedente de un cuestionario. Una evaluación real comprueba la evidencia: ¿verifica firmas el mecanismo de actualización, y se publican realmente actualizaciones? Para los contadores de LDHP, eso significa pedir a cada fabricante evidencia en lugar de respuestas. Para el «cumple la 5.3» de MTR-A, significa un paquete de actualización firmado y la fecha de la última actualización publicada. Para la 5.1, un restablecimiento de fábrica que siga dando una contraseña única. Para la 5.5, la versión de TLS y la gestión de certificados observadas en el banco. Solo las afirmaciones de MTR-A tendrían que comprobarse así en primer lugar, porque sus cuatro «sí» son los que ahora mismo sustentan una decisión de no actuar.

### Ejemplo resuelto (LDHP sintética)

Tabla de remediación de Maya: MTR-B: restablecer contraseñas únicas durante la siguiente visita de lectura de contadores, 2 semanas. MTR-C: aislar detrás de la pasarela con terminación TLS como control compensatorio para la 5.5, solicitar el contacto de divulgación del fabricante, programar la sustitución en 12 meses porque no puede cumplirse la 5.3. MTR-A: ninguna acción; volver a comprobar cuando cambie el firmware.

> **Caso sintético — Lakeside District Heating Plant.** Los modelos de dispositivo y las respuestas son inventados.

### 30.5 Reproducir y ampliar el laboratorio

Cambie el diccionario de un solo dispositivo cada vez y vuelva a ejecutar, registrando la salida junto a la modificación. Si dos estudiantes obtienen resultados distintos con los mismos diccionarios, compare las versiones de Python y el archivo exacto; el script es determinista y nunca debería diferir. Una primera modificación útil es poner a true el `unique_pw` de MTR-B y confirmar que su línea pasa a 4/4, mientras la lista de carencias de la flota pierde `unique_pw` y conserva las tres carencias de MTR-C; una segunda es dar a MTR-C una política de divulgación y comprobar que solo desaparece la 5.2 de su lista de incumplimientos. Si la lista de la flota no cambia como usted predijo, lea la agregación del script antes de fiarse de su modificación.

### Errores y límites

ETSI EN 303 645 se dirige a dispositivos de consumo; los contadores de un distrito pueden estar sujetos a otros regímenes. Las cuatro disposiciones comprobadas son un subconjunto.

### Ejercicios — capítulo 30

- **EX088 — Añadir una disposición.** Añada `"secure_storage"` asignada a la 5.4 con MTR-A True, MTR-B True, MTR-C False. ¿Qué imprime ahora MTR-C? *Rúbrica:* 3 = detecta el 4 fijo en el código (imprime 0/4), lo corrige y obtiene 1/5 con cuatro disposiciones incumplidas; 2 = una de las dos cosas; 1 = dice 1/4; 0 = nada.
- **EX089 — Por qué engañan las carencias de toda la flota.** Explique por qué «carencias de toda la flota: las cuatro» podría engañar a un directivo. *Rúbrica:* 3 = lo causan dos modelos; la vista por dispositivo muestra la mayoría de los problemas en MTR-C; 2 = parcial; 1 = vago; 0 = nada.
- **EX090 — Evidencia para la 5.3.** ¿Qué evidencia pediría a un fabricante para aceptar «software actualizable»? *Rúbrica:* 3 = mecanismo de actualización firmado, historial de actualizaciones publicado/periodo de soporte, prueba de actualización en banco; 2 = dos; 1 = el fabricante dice que sí; 0 = nada.

### Síntesis del capítulo

Las evaluaciones frente a una base de referencia son útiles cuando se comunican por dispositivo y por flota, se respaldan con evidencia y se convierten en un plan de remediación con fechas.

### Siga estudiando — capítulo 30 de 40

[← Capítulo 29 (borrador)](#ch-29) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 31 (borrador) →](#ch-31)

<a id="ch-31"></a>

## Capítulo 31 — Seguridad de TO, IoT y sistemas ciberfísicos: casos avanzados

### Resultados de aprendizaje

Usted podrá (1) analizar un marco modular de ataque a ICS a partir de un aviso de CISA; (2) distinguir la capacidad del uso observado; (3) derivar oportunidades de detección del comportamiento documentado; y (4) comparar un aviso centrado en capacidades con un informe de incidente.

### 31.1 Herramientas dirigidas a dispositivos ICS/SCADA

CISA, junto con agencias asociadas, publicó en abril de 2022 el aviso AA22-103A, que advertía de que actores de amenazas persistentes avanzadas habían desarrollado herramientas a medida capaces de buscar, comprometer y controlar determinados PLC de Schneider Electric, PLC OMRON Sysmac NEX y servidores OPC UA una vez que tenían acceso a la red de TO. El mismo aviso describe una herramienta que explotaba un controlador de software vulnerable de placas base ASRock para comprometer estaciones de ingeniería basadas en Windows. El aviso nombra familias de productos y herramientas, no víctimas, y eso condiciona cómo debe leerlo LDHP.

### 31.2 Capacidad no es incidente

A diferencia de la alerta de Ucrania de 2015, AA22-103A no describe una interrupción en una víctima con nombre. Describe una capacidad. La respuesta adecuada es la preparación: inventariar las familias de productos afectadas, restringir los protocolos de ingeniería a las estaciones de ingeniería, supervisar las conexiones inesperadas y proteger los controladores de software de las estaciones de trabajo. Entre las mitigaciones del aviso figuran aislar las redes de ICS, exigir autenticación multifactor para el acceso remoto y vigilar la presencia de controladores de software inusuales.

La lectura de Maya para LDHP: no se usa ninguna de las familias de productos nombradas, pero el servidor OPC UA de HIST-1 y los controladores de software de EWS-1 son las exposiciones genéricas que describe el aviso.

### 31.3 Del comportamiento a la detección

El comportamiento documentado sugiere detecciones concretas: un equipo nuevo que habla el protocolo de ingeniería de un fabricante de PLC; la carga o descarga de programas fuera de una ventana de cambios (ATT&CK for ICS T0843 *Program Download*); sesiones OPC UA desde equipos distintos de los clientes conocidos; la carga en una estación de trabajo de un controlador de software firmado del que se sabe que es vulnerable. Maya añadió dos de ellas a la supervisión de LDHP: las sesiones OPC UA con HIST-1 desde clientes no aprobados y los eventos de carga de controladores de software en EWS-1, que ahora figuran en la lista de reenvío de registros de la estación. La tercera, la descarga de programas en PLC-H fuera de una ventana de cambios, encaja en el monitor pasivo existente en el conmutador de control, que ya alerta de las descargas de firmware; ampliarlo a las descargas de lógica solo necesita como entrada el calendario de ventanas de cambios.

### 31.4 Comparar tipos de casos

Los informes de incidentes enseñan lo que ocurrió con restricciones reales; los avisos de capacidad enseñan lo que podría ocurrir a continuación. Ambos son necesarios, y ninguno sustituye a su propio inventario. La tabla de casos de Maya del capítulo 20 usaba informes de incidentes: la planta de agua de 2021 y Mirai, cada uno con un equivalente en LDHP. AA22-103A añade una entrada de otro tipo, porque LDHP no usa ninguno de sus productos nombrados. Su respuesta, dos detecciones nuevas para HIST-1 y EWS-1, surgió del inventario y no de la lista de productos del aviso. Una planta que solo hubiera comprobado la lista de productos habría concluido que no había nada que hacer.

### Ejemplo resuelto (LDHP sintética)

LDHP no usa ninguna de las familias de productos nombradas en AA22-103A. Maya no se detiene ahí: señala que el servidor OPC UA de HIST-1 es una exposición genérica, añade a la supervisión «sesiones OPC UA desde clientes no aprobados» y añade «eventos de carga de controladores de software en EWS-1» a la lista de reenvío de registros de la estación de trabajo.

> **Caso sintético — Lakeside District Heating Plant.** La combinación de productos de LDHP es inventada; AA22-103A es un aviso real.

### Errores y límites

Los avisos son instantáneas; compruebe si hay actualizaciones. No descargue ni ejecute las herramientas nombradas en los avisos fuera de un entorno de investigación autorizado y aislado.

### Ejercicios — capítulo 31

- **EX091 — Alcance del aviso.** Nombre las dos familias de fabricantes de PLC y el tipo de servidor enumerados en AA22-103A. *Rúbrica:* 3 = Schneider Electric, OMRON (Sysmac NEX), servidores OPC UA; 2 = dos; 1 = uno; 0 = nada.
- **EX092 — Una detección a partir de T0843.** Escriba una idea de regla de detección basada en el comportamiento de descarga de programas. *Rúbrica:* 3 = alertar de una descarga de programa en un PLC fuera de una ventana de cambios aprobada o desde un equipo que no sea de ingeniería; 2 = parcial; 1 = «supervisar los PLC»; 0 = nada.
- **EX093 — No afectados, pero actuando.** ¿Por qué actuar ante un aviso que nombra productos que usted no tiene? *Rúbrica:* 3 = las técnicas se transfieren (OPC UA, controladores de software de las estaciones, protocolos de ingeniería); el inventario puede estar incompleto; 2 = uno; 1 = «por si acaso»; 0 = nada.

### Síntesis del capítulo

El análisis de casos avanzados significa leer los avisos buscando comportamientos, traducir los comportamientos en detecciones y negarse a concluir «no nos afecta» solo a partir de una lista de productos.

### Siga estudiando — capítulo 31 de 40

[← Capítulo 30 (borrador)](#ch-30) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 32 (borrador) →](#ch-32)

<a id="ch-32"></a>

## Capítulo 32 — Seguridad de TO, IoT y sistemas ciberfísicos: interfaces interdisciplinarias

### Resultados de aprendizaje

Usted podrá (1) explicar cómo se relaciona el trabajo de seguridad con la seguridad de procesos, las operaciones, las compras y el derecho; (2) escribir requisitos de seguridad para una especificación de compra; (3) participar en una revisión conjunta de seguridad funcional y ciberseguridad; y (4) comunicarse con profesionales ajenos a la seguridad usando sus propios términos.

### 32.1 Ingenieros de seguridad funcional

Los equipos de seguridad de procesos realizan estudios de peligros y operabilidad (HAZOP) y determinan los niveles de integridad de seguridad de las funciones instrumentadas de seguridad conforme a IEC 61511. Un ingeniero de ciberseguridad se une para preguntar, para cada peligro, si una causa cibernética podría iniciarlo o desactivar la capa de protección. El resultado es compartido: un registro de peligros que enumera las causas cibernéticas junto a los fallos de los equipos. La contribución de Maya al HAZOP de LDHP es el ejemplo de este capítulo: «punto de consigna manipulado mediante una escritura de red no autorizada», añadido como causa en el nodo de alta temperatura de impulsión, junto al fallo del controlador y a una válvula atascada en posición abierta.

### 32.2 Compras

El momento más barato para corregir la seguridad es antes de la compra. Una especificación puede exigir capacidades de IEC 62443-4-2 en un nivel de seguridad indicado, conformidad con ETSI EN 303 645 para dispositivos de tipo consumo, una SBOM, un proceso de divulgación de vulnerabilidades, un periodo de soporte definido y firmware firmado. Sin estas cláusulas, la planta hereda lo que el fabricante entregue. Para la próxima compra de contadores de LDHP, esas cláusulas habrían descartado MTR-C antes de la entrega: no tiene mecanismo de actualización, ni contacto de divulgación, ni comunicación segura, tres incumplimientos que ahora cuestan una sustitución en 12 meses.

### 32.3 Operaciones y mantenimiento

Los operadores juzgan cualquier cambio por su efecto en su turno. Presente los cambios de seguridad en sus términos: «este cambio en el cortafuegos significa que la pantalla de tendencias del historiador se actualiza cada 10 s en lugar de cada 2 s». Los técnicos de mantenimiento necesitan procedimientos que se ajusten a sus herramientas; exigir un portátil que no llevan consigo fracasa en silencio. En LDHP, el cambio de la lista de permitidos del capítulo 27 se presentaría al equipo de turno así: «HMI-1 sigue escribiendo los mismos puntos de consigna; el historiador ya no puede escribir nada; si se rechaza una escritura legítima, llamen al ingeniero de control, que puede verla en el registro del cortafuegos». Esa frase responde a la pregunta de los operadores, qué cambia esta noche, sin una sola palabra sobre códigos de función.

### 32.4 Derecho y regulación

Según la jurisdicción, la calefacción urbana puede estar regulada como infraestructura crítica con obligaciones de notificación de incidentes. El personal de seguridad debe conocer los plazos de notificación y quién notifica. Este libro ofrece orientación, no asesoramiento jurídico. Para un estudiante de seguridad en LDHP, el paso práctico es averiguar a través del responsable de cumplimiento de la propia planta qué régimen se aplica, qué cuenta como incidente notificable y quién lo notifica. En el ejercicio de mesa del capítulo 29, una escritura del punto de consigna desde la VLAN de oficina que cortó la calefacción durante cinco minutos bien podría alcanzar un umbral de notificación. Saberlo a las 02:18 cambia qué evidencia conserva el analista y a quién llama después el jefe de turno.

### Ejemplo resuelto (LDHP sintética)

En la revisión HAZOP de LDHP de «alta temperatura de impulsión», las causas existentes eran el fallo del controlador y la válvula atascada en posición abierta. Maya añade como causa «punto de consigna manipulado mediante una escritura de red no autorizada», con la salvaguarda existente del disparo por alta temperatura de SIS-H (transmisor independiente, cableado) y una salvaguarda adicional recomendada: los límites de punto de consigna de PLC-H (capítulo 24).

> **Caso sintético — Lakeside District Heating Plant.** El nodo HAZOP y las recomendaciones son inventados.

### Errores y límites

Un ingeniero de ciberseguridad no está cualificado para cambiar las determinaciones de SIL; recomiende y deje que decida el equipo de seguridad funcional. Las cláusulas de compra necesitan verificarse en la entrega.

### Ejercicios — capítulo 32

- **EX094 — Tres cláusulas de compra.** Escriba tres cláusulas de seguridad para la próxima compra de pasarelas de contadores de LDHP. *Rúbrica:* 3 = tres cláusulas específicas y verificables; 2 = dos; 1 = «debe ser seguro»; 0 = nada.
- **EX095 — Una causa cibernética en el HAZOP.** Para el nodo «bajo caudal de circulación», añada una causa cibernética y su salvaguarda. *Rúbrica:* 3 = causa cibernética plausible más salvaguarda independiente; 2 = solo la causa; 1 = fallo de un equipo; 0 = nada.
- **EX096 — Explicar un cambio a los operadores.** Explique en términos de operador la aplicación de la lista de permitidos en HMI-1. *Rúbrica:* 3 = qué ven, qué hacer si algo se bloquea, a quién llamar; 2 = dos; 1 = jerga; 0 = nada.

### Síntesis del capítulo

La seguridad de TO tiene éxito a través de otras disciplinas: revisiones de seguridad funcional, cláusulas de compra, cambios centrados en los operadores y conocimiento de las obligaciones legales.

### Siga estudiando — capítulo 32 de 40

[← Capítulo 31 (borrador)](#ch-31) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 33 (borrador) →](#ch-33)

<a id="ch-33"></a>

## Capítulo 33 — Métodos de investigación II

### Resultados de aprendizaje

Usted podrá (1) diseñar un estudio de simulación replicable con hipótesis prerregistradas; (2) elegir tamaños muestrales para estimar proporciones; (3) comunicar tamaños del efecto e intervalos en lugar de solo la significación; y (4) escribir una sección de amenazas a la validez que un revisor acepte.

### 33.1 Prerregistro

Escribir las hipótesis, las medidas, el análisis y las reglas de parada antes de ejecutar el experimento impide ajustar el análisis al resultado. Para un estudio de detectores: «H1: la proporción de falsas alarmas de CUSUM en 300 ejecuciones tranquilas será menor que la de la banda; medida principal: ejecuciones con alguna falsa alarma; análisis: diferencia de proporciones con intervalo al 95 %». En el proyecto final de Maya, la regla de parada es el número fijo de semillas: 300 ejecuciones tranquilas y 300 con ataque, sin añadir ejecuciones adicionales si el primer resultado parece débil. Fijar la medida, ejecuciones con alguna falsa alarma, también le impide cambiar después a otra medida que resulte favorecer a CUSUM.

### 33.2 Tamaño muestral para una proporción

Para estimar una proporción cercana a p con un margen de error E al 95 %, n ≈ 1,96² p(1−p)/E². Para p = 0,2 y E = 0,05, n ≈ 246. Para afirmar una tasa inferior al 1 % cuando no se observa ninguna, la regla del tres necesita n ≈ 300. Las 300 semillas tranquilas de Maya se derivan de la segunda fórmula: con 0 falsas alarmas en 300 ejecuciones, la cota superior es de aproximadamente un 1 %, que es la afirmación que ella quiere poder hacer. Cuarenta ejecuciones, como en el capítulo 25, solo podrían respaldar alrededor de un 8,8 %. Sus 300 semillas con ataque por pendiente proceden de la primera fórmula, dimensionadas para que una proporción de detección cercana a 0,8 tenga un margen de unos 5 puntos.

### 33.3 Tamaños del efecto

«p < 0,05» dice poco sobre el tamaño. Comunique la diferencia: banda 22,5 % frente a CUSUM 0 % de ejecuciones con falsa alarma, diferencia de 22,5 puntos (con su intervalo calculado). Los lectores pueden entonces decidir si importa en la operación. Con los números del capítulo 25, la banda dio falsas alarmas en 9 de 40 ejecuciones tranquilas y CUSUM en 0 de 40. La diferencia, 22,5 puntos, importa a los operadores porque significa una alarma molesta aproximadamente en una de cada cuatro ejecuciones, frente a ninguna observada. Un valor p solo diría que es improbable que la diferencia se deba al azar, que es el dato menos interesante sobre ella. Un operador que decide si aceptar CUSUM en HMI-1 necesita el tamaño y las cotas de cada lado.

### 33.4 Paquete de replicación

Publique el código, las semillas, los parámetros, la versión de Python y el comando exacto. En este libro, los laboratorios incluyen su salida verificada para que el lector pueda comprobar que una nueva ejecución coincide. El paquete de replicación de Maya para el estudio de detectores contiene `lab_detect.py`, los rangos de semillas (0–39 tranquilas y 1000–1039 con ataque para la ejecución del capítulo 25; 0–299 y 1000–1299 previstas para el proyecto final), los valores de umbral y de holgura, la versión de Python y la línea de comandos. Cualquiera que lo vuelva a ejecutar debería obtener exactamente 9/40 y 0/40 ejecuciones con falsa alarma; un recuento distinto significa que algo del paquete está mal, no que el resultado sea incierto.

### Ejemplo resuelto (LDHP sintética)

El prerregistro del proyecto final de Maya fija: 300 semillas tranquilas y 300 con ataque, tres pendientes de ataque, umbral elegido en un conjunto de ajuste separado de 50 semillas y después congelado. Resultado principal: ejecuciones con alguna falsa alarma, la medida fijada en H1; la detección en 60 muestras es un resultado secundario. También enuncia qué resultado falsaría H1.

> **Caso sintético — Lakeside District Heating Plant.** El plan corresponde a un estudio simulado.

### 33.5 Resultados negativos

Si CUSUM no supera a la banda con el umbral congelado, ese es un hallazgo publicable en una tesis de grado siempre que el método haya sido sólido. Comuníquelo con los mismos intervalos que habría usado para un resultado positivo y discuta qué hipótesis —modelo de ruido, pendiente del ataque o elección del umbral— lo explica con más probabilidad. Ocultar un resultado negativo y volver a ejecutar con nuevos ajustes hasta que algo «funcione» es la práctica que el prerregistro existe para impedir.

El umbral congelado de Maya es lo que hace creíble un resultado así.

### 33.6 El control de versiones como cuaderno de laboratorio

Haga commit del archivo de prerregistro antes de la primera ejecución experimental, y haga commit de los resultados con el comando exacto que los produjo. El historial de commits muestra entonces el orden de las decisiones, que es lo que comprueba un examinador cuando un resultado parece sospechosamente limpio. Para Maya, el primer commit contiene el prerregistro con el diseño de 300 semillas y la regla del umbral congelado; a continuación viene el commit del ajuste, sobre las 50 semillas separadas; después, el commit de evaluación registra el comando y las salidas. Un examinador puede confirmar así que el umbral existía antes de ejecutar cualquier semilla de evaluación.

### Errores y límites

Los estudios de simulación se replican con facilidad, pero pueden no trasladarse a las plantas. Las comparaciones múltiples inflan los falsos descubrimientos; ajústelas o declare de antemano un resultado principal.

### Ejercicios — capítulo 33

- **EX097 — Tamaño muestral para un 10 % ± 3 %.** Calcule n para estimar una proporción cercana a 0,10 con ±0,03 al 95 %. *Rúbrica:* 3 ≈ 385; 2 = método; 1 = usa E = 3; 0 = nada.
- **EX098 — ¿Por qué congelar los umbrales?** Explique por qué el umbral se ajusta con semillas separadas. *Rúbrica:* 3 = evita el sobreajuste a los datos de evaluación; estimación no sesgada; 2 = parcial; 1 = vago; 0 = nada.
- **EX099 — Un resultado falsador.** Enuncie el resultado que falsaría H1. *Rúbrica:* 3 = proporción de falsas alarmas de CUSUM ≥ la de la banda (el intervalo incluye una diferencia cero o queda por debajo); 2 = parcial; 1 = «si CUSUM falla»; 0 = nada.

### Síntesis del capítulo

El rigor en la investigación aplicada de TO procede del prerregistro, de muestras adecuadas, de tamaños del efecto con intervalos y de paquetes de replicación completos.

### Siga estudiando — capítulo 33 de 40

[← Capítulo 32 (borrador)](#ch-32) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 34 (borrador) →](#ch-34)

<a id="ch-34"></a>

## Capítulo 34 — Proyecto comparativo

### Resultados de aprendizaje

Usted podrá (1) comparar dos arquitecturas de acceso remoto de proveedores frente a criterios explícitos; (2) construir una matriz de decisión ponderada y probar su sensibilidad; (3) documentar las hipótesis de cada opción; y (4) hacer una recomendación con su riesgo residual.

### 34.1 Las dos opciones

Opción A: VPN persistente desde el proveedor hasta un servidor de salto en la DMZ de LDHP, con MFA. Opción B: sesiones intermediadas bajo demanda: el jefe de turno habilita una sesión para una incidencia, el proveedor se conecta a través de un intermediario en la nube hasta el servidor de salto, la sesión se graba y termina al cabo de cuatro horas. Ambas evitan las conexiones directas con PLC-H. Estas dos opciones surgieron del punto de partida de LDHP, la herramienta de escritorio remoto del proveedor siempre activa. Ambas cierran esa ruta. La pregunta es cuál encaja en una planta que necesita la ayuda del proveedor por la noche.

### 34.2 Criterios

Exposición (cuánto tiempo existe una ruta), atribución (usuarios nominativos, grabación), encaje operativo (¿puede ayudar un proveedor a las 3 de la madrugada?), coste y dependencia de terceros. Los pesos reflejan las prioridades de LDHP: exposición 0,3, atribución 0,25, encaje operativo 0,25, coste 0,1, dependencia de terceros 0,1. Los pesos se fijaron antes de puntuar, en una reunión con el responsable de operaciones de LDHP, y por eso pueden cuestionarse sin acusar a quien puntúa de haberlos elegido para favorecer a su preferida. La exposición tiene el mayor peso porque tanto el caso del agua de 2021 como la propia herramienta siempre activa de LDHP dependían de cuánto tiempo permanecía abierta una ruta remota. El coste pesa poco porque la diferencia entre ambas opciones es pequeña comparada con el coste de una noche sin calefacción.

### 34.3 Puntuación

Puntuaciones de 1 a 5. A: exposición 2, atribución 3, encaje 5, coste 4, dependencia 4 → 0,6 + 0,75 + 1,25 + 0,4 + 0,4 = 3,40. B: exposición 5, atribución 5, encaje 3, coste 3, dependencia 2 → 1,5 + 1,25 + 0,75 + 0,3 + 0,2 = 4,00. B va por delante. La opción B gana sobre todo en exposición y atribución: una ruta que solo existe durante cuatro horas por incidencia, y una sesión grabada con una cuenta nominativa del proveedor. La opción A gana en encaje operativo, porque una VPN persistente está disponible a las 3 de la madrugada sin que nadie la habilite. La diferencia de 0,60 procede casi por completo de la exposición, donde B puntúa 5 frente al 2 de A, así que la recomendación solo es tan buena como ese par de puntuaciones. Si se juzgara que el intermediario en la nube es una dependencia más débil de lo indicado, la ventaja de B se reduciría, aunque no lo suficiente por sí sola para invertirla.

### 34.4 Sensibilidad

Suba el encaje operativo a 0,45 y baje la exposición a 0,1: A = 0,2 + 0,75 + 2,25 + 0,4 + 0,4 = 4,00; B = 0,5 + 1,25 + 1,35 + 0,3 + 0,2 = 3,60. La clasificación se invierte, así que la recomendación depende de cuánto valore la planta la disponibilidad nocturna del proveedor. Dígalo explícitamente. La inversión se produce porque el encaje operativo es donde A puntúa 5 y B puntúa 3: con un peso de 0,45, esa diferencia vale 0,9, más que la ventaja de B en exposición con el peso reducido de 0,1. La respuesta de Maya no fue elegir la ponderación que prefería, sino reforzar el criterio más débil de B: un procedimiento nocturno en el que el jefe de turno habilita una sesión mediante una llamada telefónica al ingeniero de guardia.

### Ejemplo resuelto (LDHP sintética)

Maya recomienda B con un cambio para abordar su criterio más débil: un procedimiento nocturno documentado en el que el jefe de turno puede habilitar una sesión mediante una llamada telefónica al ingeniero de guardia. Registra el riesgo residual de que el intermediario en la nube sea una dependencia de terceros y solicita su certificación de seguridad.

> **Caso sintético — Lakeside District Heating Plant.** Las puntuaciones son juicios de la estudiante sobre opciones inventadas.

### 34.5 Evidencia para cada puntuación

Adjunte un motivo a cada número. La puntuación de atribución de 5 de B se basa en la grabación de las sesiones y en las cuentas nominativas del proveedor en el intermediario; la puntuación de exposición de 2 de A se basa en que la VPN es alcanzable de forma permanente, incluso cuando no hay trabajo programado. Si un revisor discute una puntuación, la columna de evidencia muestra exactamente qué comprobar, y la prueba de sensibilidad muestra si la discusión podría llegar a cambiar la recomendación.

La puntuación de dependencia de 2 de B se basa en el intermediario en la nube, y por eso Maya solicitó su certificación de seguridad.

### 34.6 Presentar la comparación

Muestre al director de la planta la matriz, el resultado de sensibilidad y un párrafo por opción que describa una llamada de soporte nocturna con cada diseño. Los escenarios concretos son más fáciles de juzgar que los totales ponderados. Para las dos opciones de LDHP, el párrafo nocturno hace la mayor parte del trabajo. Con A, se llama a un ingeniero del proveedor a las 03:00 por una avería de la caldera; se conecta a través de la VPN, que siempre está abierta, y llega al servidor de salto en minutos. Con B, el jefe de turno llama al ingeniero de guardia, que habilita una sesión de cuatro horas para la incidencia; el proveedor se conecta a través del intermediario y la sesión se graba. El director puede ver que B cuesta una llamada y unos minutos por la noche, y que A deja la ruta abierta todas las demás noches del año.

### Errores y límites

Las matrices ponderadas mezclan juicio y aritmética; revele los pesos y realice comprobaciones de sensibilidad. Las puntuaciones sin evidencia son opiniones.

### Ejercicios — capítulo 34

- **EX100 — Recalcular con pesos iguales.** Con un peso de 0,2 para los cinco criterios, puntúe A y B. *Rúbrica:* 3 = A 3,6, B 3,6, empate señalado; 2 = uno correcto; 1 = errores aritméticos; 0 = nada.
- **EX101 — Una hipótesis tras la puntuación de exposición de B.** Nombre una hipótesis en la que se basa dar a B una exposición de 5. *Rúbrica:* 3 = las sesiones terminan de verdad, el intermediario no puede abrir sesiones por sí mismo, se impone la habilitación por el jefe de turno; 2 = vaga pero pertinente; 1 = ninguna pertinente; 0 = nada.
- **EX102 — Cuándo invertir la recomendación.** Enuncie la condición en la que debería elegirse A. *Rúbrica:* 3 = si la disponibilidad del proveedor 24/7 pesa más que la exposición (peso alto del encaje) y el riesgo de A se compensa; 2 = parcial; 1 = «si es más barata»; 0 = nada.

### Síntesis del capítulo

El trabajo comparativo es honesto cuando los criterios, los pesos, la evidencia y la sensibilidad son visibles, y la recomendación indica cuándo cambiaría.

### Siga estudiando — capítulo 34 de 40

[← Capítulo 33 (borrador)](#ch-33) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 35 (borrador) →](#ch-35)

<a id="ch-35"></a>

## Capítulo 35 — Propuesta del proyecto final

### Resultados de aprendizaje

Usted podrá (1) escribir una propuesta de proyecto final con problema, pregunta, alcance, método, ética y calendario; (2) definir entregables que puedan evaluarse; (3) enunciar los límites de seguridad y de autorización; y (4) obtener la aprobación del alcance por parte de su supervisor.

### 35.1 Estructura de la propuesta

Una propuesta de proyecto final para este curso tiene siete partes: planteamiento del problema (un párrafo con una fuente citada), pregunta de investigación o de diseño, alcance y exclusiones, método, límites éticos y de seguridad, entregables con criterios de aceptación, y un calendario con hitos. No supere las cuatro páginas; un supervisor debe poder aprobarla o rechazarla en una sola reunión. La propuesta de Maya cabe en tres páginas: un párrafo de problema que cita ATT&CK for ICS T0836 y CISA AA21-042A, una pregunta sobre con qué exactitud puede clasificar escrituras Modbus un monitor basado en reglas, un alcance sintético y sin conexión, y entregables comprobables.

### 35.2 Un alcance que encaje

Los proyectos finales de grado fracasan más a menudo por el alcance que por la dificultad. «Proteger LDHP» no es un proyecto final. «Diseñar, implementar y evaluar un monitor pasivo de escrituras Modbus para la captura sintética de la zona de control de LDHP, midiendo la precisión y la exhaustividad en seis clases de ataque» sí lo es. La pregunta del proyecto final de Maya se acerca a la segunda: clasificar las escrituras Modbus de una captura sintética de LDHP con reglas del capítulo 27 más una regla de frecuencia, y medir la precisión y la exhaustividad. Es lo bastante acotada como para terminarla en un semestre y aun así responde a algo que les importa a los ingenieros de LDHP: si la supervisión pasiva habría detectado una escritura como la del ejercicio de mesa del capítulo 29. El alcance también dice lo que queda fuera: otros protocolos, las capturas en vivo y cualquier aplicación de bloqueos.

### 35.3 Límite ético y de seguridad

La propuesta debe enunciar: todos los datos son sintéticos o los proporciona un propietario mediante un acuerdo escrito; no se sondeará ningún controlador ni red reales; cualquier herramienta es pasiva y funciona sin conexión; los resultados que revelen una debilidad de un producto real pasan por la divulgación coordinada. Un supervisor firma esta sección. Para el proyecto de Maya, el límite es fácil de enunciar y aun así debe firmarse: las capturas son tráfico sintético de LDHP, el monitor lee archivos y nunca abre un socket de red, y nada se ejecuta contra PLC-H ni contra ningún controlador real. Si su trabajo sugiriera un fallo en un producto de PLC real, iría primero al fabricante.

### 35.4 Criterios de aceptación

Cada entregable necesita una comprobación: «el monitor procesa el conjunto de evaluación de 8 casos e informa de TP/FP/FN/TN con precisión y exhaustividad» es comprobable; «una buena herramienta» no lo es. Los tres criterios de Maya son comprobables de este modo: el monitor procesa el conjunto de 8 casos e informa de una matriz de confusión; informa de la precisión y la exhaustividad con sus denominadores; y detecta cada una de las seis clases de ataque. El tercero es el que su evaluación marca después como cumplido en parte. Un criterio que no puede fallar, como «el monitor es útil», no le da al examinador nada que evaluar ni al estudiante nada que defender.

### Ejemplo resuelto (LDHP sintética)

La propuesta de Maya. Problema: las escrituras no autorizadas de puntos de consigna, como las descritas en ATT&CK for ICS T0836, suelen pasar inadvertidas para los operadores (motivado por CISA AA21-042A, donde el personal lo advirtió solo porque estaba mirando la pantalla). Pregunta: ¿con qué exactitud puede un monitor basado en reglas clasificar las escrituras Modbus de una captura sintética? Alcance: sin conexión, sintético, solo Modbus/TCP. Método: reglas de lista de permitidos del capítulo 27 más una regla de frecuencia; conjunto de evaluación del capítulo 38. Calendario: 12 semanas con hitos en las semanas 3, 7 y 10.

> **Caso sintético — Lakeside District Heating Plant.** El proyecto final usa solo capturas sintéticas.

### Errores y límites

Prometer de más en las métricas de una propuesta («detección del 100 %») prepara el fracaso. Las propuestas deberían prever que un resultado negativo sea aceptable si está bien fundamentado.

### Ejercicios — capítulo 35

- **EX103 — Acotar una idea de proyecto final.** Reescriba «una IA que proteja la calefacción urbana» como una pregunta de proyecto final acotada. *Rúbrica:* 3 = datos, método, medida, límite; 2 = tres; 1 = sigue siendo amplia; 0 = nada.
- **EX104 — El párrafo ético.** Escriba en tres frases el límite ético y de seguridad del proyecto de Maya. *Rúbrica:* 3 = solo datos sintéticos, sin sondeos, vía de divulgación; 2 = dos; 1 = genérico; 0 = nada.
- **EX105 — Un criterio de aceptación.** Escriba un criterio de aceptación para el entregable «informe de evaluación». *Rúbrica:* 3 = contenido y comprobación concretos (matriz de confusión, intervalos, semillas); 2 = parcial; 1 = «informe completo»; 0 = nada.

### Síntesis del capítulo

Una propuesta sólida es pequeña, comprobable y está acotada por una ética explícita, y admite un resultado negativo honesto.

### Siga estudiando — capítulo 35 de 40

[← Capítulo 34 (borrador)](#ch-34) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 36 (borrador) →](#ch-36)

<a id="ch-36"></a>

## Capítulo 36 — Práctica de campo o comunitaria

### Resultados de aprendizaje

Usted podrá (1) planificar una estancia supervisada o un proyecto comunitario con una empresa de servicios, un centro educativo o un municipio; (2) acordar un alcance escrito que excluya las pruebas en vivo; (3) realizar trabajos de concienciación o de inventario que ayuden a un operador pequeño; y (4) reflexionar sobre la práctica con un diario estructurado.

### 36.1 Lo que un estudiante de grado puede ofrecer con seguridad

Las pequeñas empresas de agua, los centros educativos con sistemas de gestión de edificios y las cooperativas comunitarias de calefacción a menudo carecen de personal de seguridad. Un estudiante supervisado puede ayudar con trabajos de bajo riesgo y mucha documentación: una lista de activos a partir de los registros existentes, una revisión de los mecanismos de acceso remoto, una lista de comprobación de higiene de contraseñas, una sesión de concienciación para los operadores. Ninguno de ellos requiere tocar un controlador en funcionamiento.

Cada una de estas tareas usa registros o conversaciones en lugar de acceso a los controladores, así que un error cuesta tiempo, pero no puede detener una bomba ni una caldera. La lista de activos de Maya para la cooperativa de calefacción es un ejemplo: construida a partir de facturas y planos, aun así encontró un router celular no documentado en la sala de calderas.

### 36.2 El acuerdo

El acuerdo de la estancia nombra a la persona responsable de la organización anfitriona, al supervisor, los entregables, las reglas de tratamiento de datos (qué sale del emplazamiento, cómo se almacena y cuándo se borra) y una prohibición explícita de escanear, sondear o cambiar configuraciones. Si la anfitriona pide «un escaneo rápido», el estudiante remite la petición al supervisor. Cuando el gerente de la cooperativa le pidió a Maya que «hiciera un escaneo para ver si nos han hackeado», el acuerdo le dio la respuesta: declinar con cortesía, explicar que escanear está fuera del alcance acordado, ofrecer en su lugar la revisión documental y trasladar la petición a su supervisor.

### 36.3 Trabajar con operadores pequeños

Los consejos deben ajustarse a su presupuesto y su personal. «Desplieguen un SOC» no le sirve de nada a una cooperativa de tres personas; «retiren la herramienta de escritorio remoto siempre activa y usen la función de sesiones bajo demanda del proveedor, habilitada desde el teléfono del gerente» sí es aplicable. Los recursos gratuitos de CISA para pequeños sistemas de agua potable y aguas residuales son un ejemplo de orientación escrita para este público. El ejemplo del acceso remoto también encaja en una cooperativa de tres personas porque no requiere equipos nuevos ni personal de supervisión, solo un cambio en la forma en que se conecta el proveedor. La recomendación de Maya para el router de la sala de calderas sigue el mismo patrón: confirmar para qué sirve, desactivarlo si no se necesita y, en caso contrario, permitir que el proveedor lo use solo a petición.

### 36.4 Diario reflexivo

Después de cada visita, anote: qué hice, qué observé, qué me sorprendió, qué haría de otra manera y cualquier cuestión ética que surgiera. La reflexión convierte la actividad en aprendizaje. La entrada de Maya tras la visita a la sala de calderas podría decir: hice, una lista de activos a partir de facturas y planos; observé, un router celular en la sala de calderas que ninguna factura mencionaba; me sorprendió, el gerente no sabía que existía, aunque era anterior a su época; de otra manera, pedir los documentos de puesta en marcha del fabricante del cuadro eléctrico antes de la visita, no después; cuestión ética, la petición del gerente de «hacer un escaneo», que ella declinó y trasladó a su supervisor. La entrada no nombra ninguna dirección ni credencial, así que puede mostrarse tal cual a un evaluador.

### Ejemplo resuelto (sintético)

La estancia de Maya en una cooperativa ficticia de calefacción de un pueblo produce una lista de activos de dos páginas construida a partir de facturas y de los planos del fabricante del cuadro eléctrico, y descubre un router celular no documentado en la sala de calderas. Su recomendación: confirmar con el fabricante del cuadro para qué sirve, desactivarlo si no se necesita y, en caso contrario, exigir que el proveedor lo habilite solo a petición.

> **Caso sintético — cooperativa ficticia de un pueblo.** La cooperativa y el router son inventados.

### Errores y límites

Un estudiante no es un consultor; el supervisor revisa las recomendaciones antes de entregarlas. El trabajo comunitario no debe crear una dependencia que el estudiante no pueda sostener una vez terminada la estancia.

### Ejercicios — capítulo 36

- **EX106 — Responder a una petición de escaneo.** El gerente de la cooperativa pide a Maya que «haga un escaneo para ver si nos han hackeado». Escriba su respuesta. *Rúbrica:* 3 = declina con cortesía, explica el alcance, ofrece una alternativa segura, remite al supervisor; 2 = tres; 1 = acepta con salvedades; 0 = lo ejecuta.
- **EX107 — Regla de tratamiento de datos.** Escriba una regla de tratamiento de datos para la lista de activos. *Rúbrica:* 3 = dónde se almacena, quién puede acceder, fecha de borrado; 2 = dos; 1 = «guardarla bien»; 0 = nada.
- **EX108 — Una entrada del diario.** Escriba la línea «qué me sorprendió» sobre el router celular. *Rúbrica:* 3 = observación concreta y lección sobre las rutas no documentadas; 2 = solo la observación; 1 = genérico; 0 = nada.

### Síntesis del capítulo

La práctica de campo permite a los estudiantes ayudar a los operadores pequeños con documentación y criterio, dentro de acuerdos escritos que mantienen intactos los sistemas en funcionamiento.

### Siga estudiando — capítulo 36 de 40

[← Capítulo 35 (borrador)](#ch-35) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 37 (borrador) →](#ch-37)

<a id="ch-37"></a>

## Capítulo 37 — Seminario de revisión de evidencia

### Resultados de aprendizaje

Usted podrá (1) revisar críticamente una afirmación publicada sobre seguridad de TO; (2) graduar la calidad de la evidencia, desde la anécdota hasta la medición replicada; (3) comprobar si las conclusiones se derivan de los datos presentados; y (4) dar y recibir una revisión por pares estructurada.

### 37.1 Una escalera de evidencia

De la más débil a la más fuerte: afirmación de marketing de un fabricante; anécdota aislada; informe de caso de una fuente primaria; medición sistemática en un sistema; medición replicada en varios sistemas o por equipos independientes. Un seminario pregunta ante cada afirmación: ¿en qué peldaño está y va la conclusión más allá de él? La revisión de Maya del informe de un compañero aplica la escalera: «CUSUM elimina las falsas alarmas en la calefacción urbana» pretende un resultado replicado, pero la evidencia es una sola medición sistemática con datos sintéticos, 0 de 40 ejecuciones. Ese peldaño respalda «no se observaron falsas alarmas, cota superior de aproximadamente un 8,8 %», no la eliminación, y no dice nada sobre plantas reales.

### 37.2 Leer un artículo de medición

El estudio de Mirai de Antonakakis et al. (USENIX Security 2017) es un buen texto para un seminario: combina varias fuentes de datos —escaneos de un telescopio de red, honeypots, datos de DNS y datos de las víctimas de los ataques— para estimar el tamaño y el comportamiento de la infección. Pregunte: ¿qué ve y qué no ve cada fuente? ¿Cómo se contaron los dispositivos infectados cuando cambian las direcciones IP? ¿Qué conclusiones dependen de una sola fuente? Para el seminario de LDHP, el ejercicio útil es tomar una conclusión, como la proporción de infecciones a través de credenciales de Telnet por defecto, y nombrar la fuente en la que se basa.

### 37.3 Leer una revisión bibliográfica

Giraldo et al. (ACM Computing Surveys, 2018) clasifican los trabajos de detección basada en la física. La fortaleza de una revisión es su amplitud; su riesgo es que comunica lo que afirman los artículos en lugar de volver a probarlo. Úsela para encontrar artículos primarios y debilidades recurrentes, como los modelos de atacante incoherentes. Para el estudio de detectores de Maya, Giraldo et al. remitieron a la evaluación basada en el impacto de Urbina et al., que orientó su decisión de variar la pendiente del ataque en lugar de comunicar una sola tasa de detección. La revisión también le advirtió de que muchos artículos sobre detectores no usan ningún modelo de atacante coherente, y por eso su prerregistro nombra la rampa de 0,08 °C por muestra como su clase de ataque antes de cualquier ejecución.

### 37.4 Revisión por pares estructurada

Formato de la revisión: resumen con sus propias palabras; principales fortalezas; preocupaciones mayores (validez, comparaciones que faltan, conclusiones exageradas); cuestiones menores; una recomendación. Comente el trabajo, no a la persona. La revisión de Maya del informe de CUSUM de su compañero sigue exactamente este orden. Su resumen reformula la afirmación, la fortaleza nombra el script reproducible con semillas, su preocupación mayor es que 0 de 40 ejecuciones sintéticas no pueden respaldar «elimina», y su cuestión menor es el retardo expresado en muestras en lugar de en minutos. La recomendación, revisar la afirmación y añadir la cota de aproximadamente un 8,8 %, le dice al autor qué cambiar. Separar las preocupaciones mayores de las menores muestra qué cambio es imprescindible para que el informe se sostenga.

### Ejemplo resuelto (LDHP sintética)

El informe de un compañero afirma que «CUSUM elimina las falsas alarmas en la calefacción urbana». La revisión de Maya: resumen; fortaleza: script reproducible con semillas; preocupación mayor: 0/40 ejecuciones sintéticas respaldan «no se observaron falsas alarmas, cota superior ≈ 8,8 %», no la eliminación, y no se probó nada con datos reales de planta; menor: la unidad del retardo (muestras) no se convierte a minutos; recomendación: revisar la afirmación y añadir la cota.

> **Caso sintético — Lakeside District Heating Plant.** El informe del compañero es inventado.

### Errores y límites

La revisión por pares comprueba el razonamiento, no la verdad; los revisores también pasan por alto errores. El prestigio de una publicación no es evidencia de que sea correcta.

### Ejercicios — capítulo 37

- **EX109 — Situar afirmaciones en la escalera.** Sitúe en la escalera de evidencia: (a) un folleto de un fabricante que dice «bloquea el 99,9 % de los ataques a ICS», (b) AA21-042A. *Rúbrica:* 3 = (a) afirmación de marketing, (b) informe de caso primario; 2 = uno; 1 = invertidos; 0 = nada.
- **EX110 — Cuestionar una conclusión de una sola fuente.** Identifique una conclusión del estudio de Mirai que sería más débil si se basara solo en datos de honeypots, y por qué. *Rúbrica:* 3 = tamaño de la infección/estimación de la población; los honeypots solo ven los dispositivos que contactan con ellos; 2 = parcial; 1 = vago; 0 = nada.
- **EX111 — Escribir una preocupación mayor.** Escriba la preocupación mayor para un artículo que evalúa un detector en una sola planta simulada con umbrales ajustados a mano. *Rúbrica:* 3 = generalización y sesgo por ajustar con los datos de prueba, con la corrección solicitada; 2 = uno; 1 = comentario de estilo; 0 = nada.

### Síntesis del capítulo

La revisión de la evidencia pregunta cuán fuerte es la evidencia, si la conclusión se ajusta a ella y cómo decirlo de forma constructiva.

### Siga estudiando — capítulo 37 de 40

[← Capítulo 36 (borrador)](#ch-36) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 38 (borrador) →](#ch-38)

<a id="ch-38"></a>

## Capítulo 38 — Implementación del proyecto final

### Resultados de aprendizaje

Usted podrá (1) implementar el artefacto de un proyecto final en incrementos pequeños y probados; (2) mantener un registro de cambios y un registro de decisiones; (3) evaluar el artefacto con un conjunto etiquetado mediante una matriz de confusión; y (4) comunicar la precisión y la exhaustividad con sus denominadores.

### 38.1 Incrementos

Construya primero la versión completa más pequeña: leer un archivo de captura, clasificar cada escritura, imprimir las decisiones. Después añada las reglas una a una, cada una con pruebas (capítulo 8) y vectores de conformidad (capítulo 27). Una herramienta pequeña que funciona en la semana 4 vale más que una ambiciosa que nunca llega a ejecutarse. La versión de la semana 4 de Maya leía una captura sintética, clasificaba cada escritura Modbus frente a la lista de permitidos del capítulo 27 e imprimía una decisión por línea. La regla de frecuencia llegó después, con sus propias pruebas, y la regla de cambio acumulado solo después de que la evaluación mostrara que no se detectaba el ataque de deriva. Cada incremento podía ejecutarse y comprobarse frente a los ocho casos etiquetados antes de empezar el siguiente.

### 38.2 Registros de decisiones

Cuando elija, registre por qué: «Decisión 7: tratar las escrituras durante una ventana de mantenimiento programada como benign-maint solo si el identificador de la incidencia aparece en la lista de la ventana; alternativas consideradas: regla solo horaria (rechazada: los internos podrían sincronizar sus ataques con ella)». Los registros de decisiones permiten a los examinadores seguir el razonamiento. Las decisiones posteriores de Maya siguen el mismo formato. Tras la evaluación, un registro añade una regla de cambio acumulado para el ataque de deriva no detectado, y rechaza la alternativa de un umbral menor por escritura porque marcaba los ajustes ordinarios de los operadores. Otro registra la correlación de las escrituras del HMI con los eventos de inicio de sesión de los operadores, para abordar la escritura del punto de consigna que procedía de HMI-1, un origen permitido.

### 38.3 Evaluación

El laboratorio evalúa la salida de un monitor en ocho casos etiquetados del conjunto sintético de Maya.

```python
"""Lab 38: capstone evaluation - precision/recall with denominators (synthetic results)."""
cases = [("replay", True, True), ("replay", True, True), ("setpoint", True, False), ("setpoint", True, True),
         ("benign-maint", False, True), ("benign", False, False), ("benign", False, False), ("drift", True, False)]
tp = sum(a and d for _, a, d in cases); fp = sum((not a) and d for _, a, d in cases)
fn = sum(a and not d for _, a, d in cases); tn = sum((not a) and not d for _, a, d in cases)
print(f"TP={tp} FP={fp} FN={fn} TN={tn}")
print(f"precision={tp}/{tp+fp}={tp/(tp+fp):.2f} recall={tp}/{tp+fn}={tp/(tp+fn):.2f}")
print("missed classes:", sorted({c for c, a, d in cases if a and not d}))
```

Ejecútelo con `python3 lab_eval.py`. Salida verificada:

```text
TP=3 FP=1 FN=2 TN=2
precision=3/4=0.75 recall=3/5=0.60
missed classes: ['drift', 'setpoint']
```

Los ocho casos incluyen cinco ataques y tres escrituras benignas, entre ellas una escritura de mantenimiento. El laboratorio calcula la precisión y la exhaustividad a partir de las etiquetas del monitor e imprime la matriz de confusión. El conjunto es de juguete: su propósito es mostrar qué clases no detecta el monitor, y un noveno caso podría cambiar todas las tasas. Su valor está en que cada caso tiene una respuesta conocida escrita antes de ejecutar el monitor, así que una discrepancia siempre es un error del monitor o de la etiqueta, y Maya registra cuál.

### 38.4 Leer la matriz de confusión

Tres verdaderos positivos, un falso positivo (una escritura de mantenimiento marcada), dos falsos negativos (un ataque de punto de consigna y el ataque de deriva no detectados), dos verdaderos negativos. Precisión 3/4 = 0,75; exhaustividad 3/5 = 0,60. Ocho casos son demasiado pocos para obtener tasas precisas —un intervalo de Wilson para 3/5 abarca aproximadamente de 0,23 a 0,88—, así que el uso honesto de esta tabla es encontrar clases de fallo, no clasificar herramientas. El único falso positivo es la escritura de mantenimiento, que la decisión 7 trata como benigna solo cuando el identificador de su incidencia aparece en la lista de la ventana. Los dos fallos de detección apuntan a correcciones distintas, una regla de cambio acumulado para el ataque de deriva y la correlación con los inicios de sesión para la escritura desde HMI-1, y por eso Maya examina cada clase por separado en lugar de ajustar un único umbral.

### Ejemplo resuelto (LDHP sintética)

Maya examina los dos fallos de detección. El ataque de deriva usó muchas escrituras pequeñas, cada una dentro del rango permitido: un monitor basado en reglas sin una regla de frecuencia o de tendencia no puede verlo. El ataque de punto de consigna no detectado procedía del propio HMI-1, que está en la lista de permitidos. Ambos llevan a nuevos registros de decisión: añadir una regla de cambio acumulado y correlacionar las escrituras del HMI con los eventos de inicio de sesión de los operadores.

> **Caso sintético — Lakeside District Heating Plant.** Los ocho casos son un conjunto de juguete con fines ilustrativos.

### Errores y límites

Las etiquetas solo son tan buenas como el autor del escenario; un ataque etiquetado como «benigno» corrompe todas las métricas. No ajuste las reglas con los casos de evaluación para después comunicar los mismos números.

### Ejercicios — capítulo 38

- **EX112 — Corregir el falso positivo.** Proponga un cambio que evite marcar la escritura de mantenimiento sin ocultar ataques reales. *Rúbrica:* 3 = exigir que coincidan la incidencia/ventana y la cuenta de ingeniería, y seguir registrándola; 2 = parcial; 1 = ignorar el horario de mantenimiento; 0 = nada.
- **EX113 — Exhaustividad tras una corrección.** Si la regla de cambio acumulado detecta el caso de deriva y nada más cambia, ¿cuál es la nueva exhaustividad? *Rúbrica:* 3 = 4/5 = 0,80; 2 = número correcto sin fracción; 1 = 0,75; 0 = nada.
- **EX114 — Por qué importa el intervalo.** Explique por qué la exhaustividad de 0,60 no puede compararse con el 0,70 de otra herramienta en un conjunto distinto de 10 casos. *Rúbrica:* 3 = muestras diminutas, intervalos amplios que se solapan, distinta combinación de casos; 2 = uno; 1 = «herramientas distintas»; 0 = nada.

### Síntesis del capítulo

Implemente en incrementos probados, registre las decisiones y use los conjuntos de evaluación pequeños para encontrar clases de fallo, no para afirmar tasas.

### Siga estudiando — capítulo 38 de 40

[← Capítulo 37 (borrador)](#ch-37) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 39 (borrador) →](#ch-39)

<a id="ch-39"></a>

## Capítulo 39 — Evaluación del proyecto final

### Resultados de aprendizaje

Usted podrá (1) evaluar un proyecto final frente a su propia propuesta; (2) separar resultados, interpretación y limitaciones; (3) realizar una autoevaluación estructurada con la rúbrica del curso; y (4) planificar el trabajo que necesitaría hacer quien le suceda.

### 39.1 Frente a la propuesta

Vuelva a los criterios de aceptación escritos en el capítulo 35. Para cada uno, registre cumplido, cumplido en parte o no cumplido, con evidencia. Un proyecto final que no cumple un criterio pero explica por qué —por ejemplo, que la clase de deriva no podía detectarse solo con reglas— todavía puede obtener una calificación alta. La tabla de evaluación de Maya muestra en uso los tres resultados posibles. Los criterios 1 y 2 se cumplen, con la matriz de confusión y los denominadores como evidencia, mientras que el criterio 3 se cumple en parte: cinco de seis clases de ataque tras la regla de cambio acumulado, con la escritura interna originada en el HMI todavía sin detectar y el motivo enunciado.

### 39.2 Resultados frente a interpretación

Los resultados son lo que produjo la evaluación: «exhaustividad de 4/5 en el conjunto de ocho casos». La interpretación es lo que usted cree que significa: «la regla de cambio acumulado aborda la manipulación lenta». Las limitaciones acotan la interpretación: «probado solo con datos sintéticos y un único perfil de deriva». Mantener tres encabezados impide que los resultados absorban en silencio las opiniones. En la tesis de Maya, la exhaustividad subió a 4/5 en el conjunto de ocho casos cuando la regla de cambio acumulado detectó el ataque de deriva; la escritura desde HMI-1 sigue sin detectarse. Esa frase es un resultado. «El monitor es adecuado para LDHP» sería una interpretación que la limitación, un único perfil de deriva con datos sintéticos, todavía no respalda.

### 39.3 Rúbrica de autoevaluación

Puntúese de 0 a 3 en: planteamiento del problema, adecuación del método, calidad de la evidencia, seguridad y ética, comunicación. Escriba una frase de evidencia por cada puntuación. Los supervisores usan la misma rúbrica; las diferencias abren una conversación útil. Maya se puntuó con un 2 en calidad de la evidencia, con la frase «ocho casos son un conjunto de juguete», y con un 3 en seguridad y ética, con «solo sin conexión, documentado». Los resultados resueltos explican por qué un 2 y no un 3 es justo: el análisis es reproducible y comunica los denominadores, pero ocho casos sintéticos con un único perfil de deriva no pueden respaldar afirmaciones generales. Una autopuntuación de 3 en ese punto habría sido el primer motivo de desacuerdo con su supervisor.

### 39.4 Plan para quien le suceda

Enumere lo que haría con tres meses más: un segundo modelo de proceso, capturas reales anonimizadas (proporcionadas por un propietario), un estudio de usabilidad con operadores. Ordénelo por su valor para la pregunta. Para Maya, la clasificación pone en primer lugar la escritura originada en el HMI, porque es la clase que su monitor sigue sin detectar: correlacionar las escrituras con los inicios de sesión de los operadores, sobre capturas anonimizadas proporcionadas por un propietario, pondría a prueba el remedio. Un segundo modelo de proceso, como el vaso de expansión del capítulo 21, viene después, ya que un monitor ajustado a un lazo puede no trasladarse a otro. Un estudio de usabilidad con operadores va al final, porque solo importa cuando el monitor ya detecta las clases que importan.

### Ejemplo resuelto (LDHP sintética)

Tabla de evaluación de Maya: criterio 1 (procesa el conjunto de 8 casos, informa de la matriz de confusión): cumplido; criterio 2 (precisión y exhaustividad con denominadores): cumplido; criterio 3 (detecta las seis clases de ataque): cumplido en parte, cinco de seis tras la regla de cambio acumulado, con la escritura interna originada en el HMI todavía sin detectar. Autoevaluación: calidad de la evidencia 2 («ocho casos son un conjunto de juguete»), seguridad 3 («solo sin conexión, documentado»).

> **Caso sintético — Lakeside District Heating Plant.** Las puntuaciones son una ilustración resuelta.

### 39.5 La visión del supervisor

Los supervisores buscan la coherencia entre la pregunta, la evidencia y las afirmaciones. Un comentario frecuente en esta etapa es que la sección de conclusiones repite los resultados en lugar de responder a la pregunta de investigación. Reescriba la conclusión para que su primera frase responda directamente a la pregunta del capítulo 35, la segunda enuncie la limitación más importante y la tercera nombre el siguiente estudio. La primera frase de Maya respondería directamente a la pregunta de su propuesta: con capturas sintéticas de LDHP, el monitor basado en reglas clasificó correctamente cinco de seis clases de ataque.

### Errores y límites

La autoevaluación tiende a puntuar de más la comunicación y de menos la adecuación del método. No redefina los criterios de aceptación a posteriori para que se ajusten a los resultados.

### Ejercicios — capítulo 39

- **EX115 — Clasificar tres frases.** Etiquete como resultado, interpretación o limitación: (a) «precisión 4/5»; (b) «la herramienta está lista para un piloto»; (c) «se probó un perfil de deriva». *Rúbrica:* 3 = R, I, L; 2 = dos; 1 = una; 0 = nada.
- **EX116 — Puntuar la calidad de la evidencia.** Justifique una puntuación de 2 (no de 3) en calidad de la evidencia para el proyecto final de Maya. *Rúbrica:* 3 = reproducible y correcto, pero el pequeño conjunto sintético limita la generalidad; 2 = parcial; 1 = «podría ser mejor»; 0 = nada.
- **EX117 — La tarea principal para quien le suceda.** ¿Qué tarea de continuación refuerza más la pregunta de investigación y por qué? *Rúbrica:* 3 = un modelo de proceso adicional o capturas proporcionadas por un propietario para probar la generalización; 2 = solo la tarea; 1 = pulir la interfaz; 0 = nada.

### Síntesis del capítulo

Evalúe un proyecto final frente a sus propias promesas, mantenga los resultados separados de las opiniones y deje un camino ordenado para quien continúe el trabajo.

### Siga estudiando — capítulo 39 de 40

[← Capítulo 38 (borrador)](#ch-38) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 40 (borrador) →](#ch-40)

<a id="ch-40"></a>

## Capítulo 40 — Tesis y presentación

### Resultados de aprendizaje

Usted podrá (1) estructurar una tesis de grado en seguridad de TO; (2) diseñar diapositivas que muestren evidencia en lugar de decoración; (3) preparar una defensa oral anticipando las preguntas; y (4) publicar un paquete de replicación de forma responsable.

### 40.1 Estructura de la tesis

Introducción (problema, pregunta, contribución); antecedentes (normas y trabajos previos, citados con precisión: NIST SP 800-82r3, las partes pertinentes de IEC 62443, las técnicas de ATT&CK for ICS, los artículos revisados por pares que usted haya leído); método; resultados; discusión, incluidas las limitaciones; conclusión y trabajo futuro; apéndices con el código y la descripción de los datos. Mantenga visible la etiqueta de sintético en el pie de cada figura que use datos de LDHP. Para la tesis de Maya, el capítulo de antecedentes cita ATT&CK for ICS T0836 y CISA AA21-042A para el problema, IEC 62443-3-3 para los controles de zonas y conductos que sustentan su lista de permitidos, y Urbina et al. para evaluar los detectores por el impacto del atacante. Cada figura construida a partir de capturas de LDHP lleva «datos sintéticos» en su pie.

### 40.2 Diapositivas

Un mensaje por diapositiva, enunciado en su título: «La supervisión basada en reglas no detectó la deriva lenta; una regla acumulada la recuperó». Muestre la matriz de confusión, los denominadores y el intervalo. Evite las imágenes de hackers y los iconos de candados; los examinadores los leen como señal de un contenido débil. La diapositiva de resultados de Maya muestra su matriz de ocho casos con los recuentos en cada celda —tres verdaderos positivos, un falso positivo, dos falsos negativos, dos verdaderos negativos— y el intervalo de Wilson para la exhaustividad de 3/5, aproximadamente de 0,23 a 0,88. Su título enuncia el hallazgo en lugar de decir «Resultados». Así, el tribunal puede preguntar por el falso positivo, una escritura de mantenimiento marcada, sin tener que descifrar antes el gráfico.

### 40.3 Anticipar las preguntas

Prepare respuestas para: ¿Por qué datos sintéticos? ¿Cómo fallaría esto en una planta real? ¿Cuál es la carga de falsas alarmas para los operadores por turno? ¿Por qué estas clases de ataque? ¿Qué haría un atacante que conociera sus reglas? Responder «no lo sé, pero así es como lo averiguaría» es aceptable; inventar números no lo es. Para la pregunta sobre las falsas alarmas, Maya puede responder con sus propios datos: un falso positivo en ocho casos es demasiado poco para estimar la carga por turno, y lo dice, junto con el número de horas tranquilas que necesitaría para medirla. Para la pregunta sobre el atacante, sus dos fallos de detección ya responden en parte: muchas escrituras pequeñas dentro del rango permitido, y escrituras desde el propio HMI-1.

### 40.4 Publicación responsable

Publique el código, las semillas y los datos sintéticos bajo una licencia abierta. No publique nada que sea un ataque funcional contra productos reales. Si el trabajo encontró una vulnerabilidad real, la publicación espera a la divulgación coordinada (capítulo 10). El repositorio de la tesis de Maya contendría el código del monitor, las capturas sintéticas de LDHP con su generador y sus semillas, y los ocho casos etiquetados. No contendría nada que envíe escrituras Modbus, porque el monitor solo lee archivos de captura. Si su trabajo hubiera revelado un fallo en el tratamiento del código de función 8 por parte de un PLC real, la descripción en la tesis esperaría a que el fabricante tuviera una corrección.

### Ejemplo resuelto (LDHP sintética)

La defensa de Maya empieza con la contribución en una frase: «Un monitor de escrituras Modbus basado en reglas, con una regla de cambio acumulado, detectó cinco de seis clases de ataque sintéticas en las capturas de LDHP; la clase restante —escrituras desde un HMI legítimo— requiere correlación con la identidad del operador». Su diapositiva final enumera tres limitaciones y el plan de continuación del capítulo 39.

> **Caso sintético — Lakeside District Heating Plant.** La tesis es una ilustración resuelta con datos simulados.

### Errores y límites

Una tesis se juzga más por su razonamiento y su honestidad que por el tamaño del resultado. Los capítulos de revisión bibliográfica largos que resumen sin evaluar añaden páginas, no puntos.

### Ejercicios — capítulo 40

- **EX118 — Un título de diapositiva que lleve la afirmación.** Escriba el título de la diapositiva que muestra el resultado de exhaustividad de 4/5. *Rúbrica:* 3 = afirmación en una frase completa con matiz; 2 = afirmación sin matiz; 1 = «Resultados»; 0 = nada.
- **EX119 — Defenderse frente a un atacante informado.** Redacte una respuesta a «¿qué haría un atacante que conociera sus reglas?». *Rúbrica:* 3 = admite la evasión (p. ej., a través del HMI o por debajo del umbral acumulado), cita el margen de impacto al estilo de Urbina, propone una defensa; 2 = dos; 1 = lo niega; 0 = nada.
- **EX120 — Qué no publicar.** Nombre un elemento que debería excluirse del paquete de replicación público y por qué. *Rúbrica:* 3 = cualquier cosa utilizable contra productos reales o cualquier dato proporcionado por un propietario; motivo; 2 = solo el elemento; 1 = «el código»; 0 = nada.

### Síntesis del capítulo

Una tesis cierra el curso mostrando que usted sabe plantear una pregunta de seguridad de TO, responderla con evidencia honesta y comunicar los límites de la respuesta a quienes deben actuar en consecuencia.

### Siga estudiando — capítulo 40 de 40

[← Capítulo 39 (borrador)](#ch-39) · [Índice de capítulos del curso](../SUBJECTS.md) · [Resultados resueltos ↓](#worked-results) · [Siguiente curso a través del índice de capítulos →](../SUBJECTS.md)

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

**EX055.** Sensor: suplantar o sesgar la señal de TT-101. Controlador: cambiar el punto de consigna o la lógica de PLC-H. Actuador: forzar la apertura de FV-12 mediante una anulación manual o la manipulación de la E/S. Comunicación: interrumpir o retrasar el enlace PLC-H ↔ HMI para que los operadores pierdan la visibilidad.

**EX056.** (a) NIST IR 8259 (con IR 8259A) o ETSI EN 303 645 para el fabricante de contadores; IEC 62443-4-2 si el contador se vende como componente industrial. (b) NIST SP 800-82r3 o IEC 62443-2-1 para el programa de LDHP como propietario del activo.

**EX057.** Si SIS-H leyera la temperatura a través de PLC-H, un atacante que comprometiera PLC-H o falsificara TT-101 también dejaría ciego al disparo. Un transmisor separado, cableado directamente a SIS-H, mantiene la función de seguridad independiente del sistema de control que protege.

**EX058.** Se vieron afectados unos 225.000 clientes; los actores corrompieron el firmware de dispositivos de serie a Ethernet en las subestaciones (el borrado de los HMI con KillDisk también es una respuesta aceptable).

**EX059.** Nombres de usuario y contraseñas de fábrica o débiles, alcanzables por Telnet; la disposición 5.1 de ETSI EN 303 645 (sin contraseñas por defecto universales) lo aborda.

**EX060.** (a) Hecho comunicado en CISA AA21-042A. (b) Inferencia: el aviso informa del intento de cambio, no de la intención del intruso.

**EX061.** En equilibrio, caudal de entrada = caudal de salida = 2,0 = 1,6 × error, así que el error es de 1,25 puntos; el nivel se estabiliza en torno al 58,75 %.

**EX062.** Cada paso saturado añade 1,5 puntos: tras 8 pasos, 69,5 %; tras 9 pasos, 71,0 %; así que 9 pasos.

**EX063.** El controlador lleva el nivel *medido* al 57,5 %; con un sesgo de +10, el nivel real es del 47,5 %: el vaso está por debajo de su llenado mientras el HMI parece normal.

**EX064.** Etiqueta y función del activo, fabricante y modelo, versión de firmware/software, zona y dirección de red (o enlace serie), responsable, nivel de criticidad (más ubicación y dependencias).

**EX065.** La versión de firmware instalada en cada pasarela de LDHP y la versión de la biblioteca TLS que contiene ese firmware según su SBOM (o la declaración del fabricante); si la biblioteca está entre 2.0 y 2.4, las pasarelas están afectadas.

**EX066.** Solo un ingeniero sabe restaurar la lógica de PLC-H desde la copia de seguridad; mitíguelo con un procedimiento de restauración escrito y probado y un segundo ingeniero formado. (El servidor de licencias del HMI o una única tarjeta de E/S de repuesto también son válidos).

**EX067.** Consecuencia: lecturas de consumo falsificadas para una calle entera producen facturas erróneas y ocultan una fuga real durante semanas. Ruta: la contraseña por defecto de la pasarela de contadores permite a un atacante alterar las lecturas antes de que se firmen y se envíen a la nube.

**EX068.** No. A (raro pero catastrófico) puede requerir cambios de diseño, como salvaguardas independientes, aunque sea improbable; B (frecuente pero menor) puede tratarse en la operación. Productos iguales ocultan situaciones muy distintas, así que decida con los escenarios, no con el número.

**EX069.** «Residual de S-3: un empleado interno con credenciales de ingeniería en EWS-1 todavía podría cambiar los puntos de consigna de PLC-H. Supone que las cuentas nominativas y el registro están implantados. Aceptado por el director de la planta; revisión el 1 de abril del año próximo o tras cualquier cambio en el acceso de ingeniería».

**EX070.** FR 1: credenciales únicas por dispositivo y cuentas de administración nominativas en las pasarelas. FR 5: las pasarelas solo pueden abrir TLS saliente hacia la nube de facturación; ninguna sesión entrante desde ella hacia la zona de control. FR 6: alertar cuando cambie la configuración de una pasarela o esta contacte con un destino desconocido.

**EX071.** Un operador que se equivoca al teclear durante una perturbación estresante queda bloqueado justo cuando se necesita el control. Más seguro: retardo progresivo y alerta al jefe de turno, con el bloqueo desactivado en las consolas de la sala de control protegidas físicamente.

**EX072.** Situarla en su propia VLAN con un cortafuegos que permita solo los flujos necesarios; bloquear su interfaz de gestión desde cualquier lugar excepto un servidor de salto; supervisar su tráfico en busca de destinos nuevos; programar su sustitución por un modelo conforme.

**EX073.** Banda: falsas alarmas en 9 de 40 ejecuciones tranquilas. CUSUM: 0 de 40, con una cota superior al 95 % de aproximadamente un 7,5 % (regla del tres) o un 8,8 % (Wilson), así que «no se observaron falsas alarmas», no «nunca».

**EX074.** La holgura (valor de referencia) se resta de cada desviación para que, con el ruido normal, la suma acumulada vuelva una y otra vez a cero; solo un desplazamiento sostenido mayor que la holgura la hace crecer hasta el umbral, lo que suprime las alarmas por ruido de una sola muestra.

**EX075.** Barrer la pendiente de la rampa (p. ej., 0,005–0,08 °C/muestra) y, para cada una, registrar la desviación de temperatura alcanzada antes de que CUSUM dé la alarma; la mayor desviación lograda sin ser detectado en un horizonte fijo es la métrica de impacto del ataque sigiloso que recomiendan Urbina et al.

**EX076.** S: un atacante presenta a la pasarela un punto de conexión falso de la nube (servidor suplantado) si la validación de certificados es débil. T: lecturas alteradas en el trayecto por un proxy comprometido. D: se inunda el enlace ascendente de la pasarela o se inhibe su módem celular para que las lecturas no se entreguen.

**EX077.** Actor: un atacante externo en internet. Precondición: la interfaz web de la pasarela es alcanzable desde internet y sigue usando la contraseña por defecto del fabricante. Acción: inicia sesión y sube un firmware o una configuración modificados. Resultado: los 40 contadores que hay detrás de esa pasarela comunican lecturas falsas y la pasarela puede usarse para pivotar hacia la DMZ.

**EX078.** La reproducción de un inquilino afecta a la factura de un hogar y su valor está acotado, mientras que la toma de control de la pasarela afecta a todos los contadores de su calle y puede proporcionar un punto de apoyo hacia otras zonas; el mayor radio de impacto y el posible efecto operativo la sitúan más arriba.

**EX079.** Se espera BLOCK, y `permit("HMI-1", 23, 105)` devuelve BLOCK porque el par (HMI-1, 23) no está en ALLOW: la política deniega por defecto las funciones no enumeradas.

**EX080.** (HMI-1, 6, 120) → PASS, el nuevo último registro escribible; (HMI-1, 6, 121) → BLOCK, el primer registro fuera del rango.

**EX081.** Si las expectativas salen de ejecutar el código, un fallo se convierte en el resultado esperado. Escribirlas primero a partir del requisito operativo (qué registros necesita realmente HMI-1) permite que la prueba detecte la discrepancia.

**EX082.** 0,1 × 0,3 × 0,2 = 0,006 al año.

**EX083.** Un solo intruso que escribe el punto de consigna también puede suprimir las alarmas del HMI o desactivar el detector, así que «los operadores no lo advierten» y «el detector falla» se vuelven probables dada la escritura; multiplicar entonces las probabilidades marginales subestima P(c).

**EX084.** Componente: pasarela de contadores. Modo: caduca el certificado de cliente TLS. Efecto: la nube rechaza el enlace ascendente; las lecturas se encolan y después se descartan cuando se llena el búfer. Detección: supervisión de la caducidad de certificados con 30 días de antelación y alerta por latido ausente. Gravedad: media (retraso en la facturación, sin efecto sobre el proceso). Acción: renovación automatizada con alerta si falla.

**EX085.** «El analista informa al jefe de turno. El jefe de turno confirma que los operadores pueden mantener la caldera en estado seguro con los paneles locales o el HMI de reserva, y después autoriza desconectar el enlace de red del servidor SCADA (sin apagarlo, para conservar la evidencia)».

**EX086.** Voraz por riesgo: riesgo 9 (1,5 h) y riesgo 8 (1 h) ocupan 2,5 h; el de riesgo 6 necesita 2 h y excedería la ventana hasta 4,5 h, así que se aplaza; el de riesgo 3 (1 h) cabe, total 3,5 h. Aplicar 9, 8 y 3; aplazar el parche de riesgo 6 con una incidencia fechada y controles compensatorios (o dividir el plan de la ventana si la tarea de riesgo 6 puede acortarse).

**EX087.** Añadir a la primera página del manual una lista de guardias con los teléfonos nocturnos del administrador del cortafuegos y del ingeniero de control, e incluir una llamada de prueba real a cada número al inicio del siguiente ejercicio de mesa.

**EX088.** El bucle usa `4-len(miss)`, así que imprimiría `MTR-C: 0/4 met` salvo que se cambie el 4; tras cambiarlo por `len(f)-len(miss)`, MTR-C imprime 1/5 met con 5.2, 5.3, 5.4 y 5.5 incumplidas. Detectar el 4 fijo en el código forma parte de la respuesta.

**EX089.** Todas las disposiciones aparecen como carencias de la flota, pero MTR-A las supera todas y MTR-B solo incumple una; el directivo podría financiar la sustitución de toda la flota cuando el problema real se concentra en MTR-C, más un restablecimiento de contraseñas barato para MTR-B.

**EX090.** Una descripción de cómo se firman criptográficamente las actualizaciones y cómo se verifican en el dispositivo, el historial de actualizaciones publicado por el fabricante y su periodo de soporte declarado, y una demostración en banco de la aplicación de una actualización y del rechazo de una manipulada.

**EX091.** PLC de Schneider Electric, PLC OMRON Sysmac NEX y servidores Open Platform Communications Unified Architecture (OPC UA).

**EX092.** Alertar siempre que la supervisión pasiva vea una operación de descarga de programa (o de cambio de lógica) en PLC-H que no proceda de EWS-1 o que se produzca fuera de una ventana de cambios registrada en el sistema de mantenimiento.

**EX093.** Las técnicas —abusar de OPC UA, de los protocolos de ingeniería y de controladores de software vulnerables de las estaciones de trabajo— se aplican a otros productos, y un inventario que dice «no tenemos ninguno» puede estar incompleto; actuar sobre detecciones genéricas reduce la exposición a la siguiente variante.

**EX094.** (1) El fabricante deberá proporcionar una SBOM para cada versión de firmware en formato SPDX o CycloneDX. (2) La pasarela no deberá tener ninguna contraseña por defecto universal y deberá forzar una credencial única en la puesta en marcha (disposición 5.1 de ETSI EN 303 645). (3) El fabricante deberá publicar una política de divulgación de vulnerabilidades y proporcionar actualizaciones de seguridad durante al menos siete años tras la entrega.

**EX095.** Causa: una escritura no autorizada detiene la bomba de circulación P-2 a través de la interfaz de red de su variador de velocidad. Salvaguarda: un interruptor de bajo caudal cableado que dispara los quemadores de la caldera a través de SIS-H, independiente de la red de los variadores.

**EX096.** «A partir del lunes, HMI-1 solo ejecutará el programa del HMI y las herramientas aprobadas. Si algo que usan normalmente no arranca, aparecerá un mensaje; en la planta no cambia nada. Anoten qué intentaron y llamen al ingeniero de control a la extensión 214; no intenten sortearlo».

**EX097.** n = 1,96² × 0,10 × 0,90 / 0,03² = 3,8416 × 0,09 / 0,0009 ≈ 384,2, es decir, unas 385 ejecuciones.

**EX098.** Elegir el umbral con las mismas ejecuciones usadas para la evaluación lo ajusta al ruido de esas ejecuciones y hace optimistas las estimaciones de falsas alarmas y de detección; ajustarlo con semillas separadas y congelarlo da una estimación honesta del rendimiento con datos no vistos.

**EX099.** H1 queda falsada si, en las 300 ejecuciones tranquilas, la proporción de ejecuciones de CUSUM con alguna falsa alarma no es menor que la de la banda, es decir, si el intervalo al 95 % de (banda − CUSUM) incluye el cero o queda por debajo de él.

**EX100.** A = 0,2 × (2 + 3 + 5 + 4 + 4) = 3,6; B = 0,2 × (5 + 5 + 3 + 3 + 2) = 3,6: un empate exacto, que muestra que son los pesos los que separan las opciones.

**EX101.** Que el intermediario no puede iniciar sesiones sin la aprobación del jefe de turno y que las sesiones terminan automáticamente a las cuatro horas; si falla cualquiera de las dos cosas, B tiene una ruta persistente como A.

**EX102.** Elegir A cuando la planta juzgue la disponibilidad del proveedor las veinticuatro horas más importante que la exposición de la ruta —por ejemplo, si el encaje tiene un peso ≥ 0,45, como en la prueba de sensibilidad—, y solo con controles compensatorios como la grabación de las sesiones y revisiones mensuales de los accesos.

**EX103.** «¿Puede un clasificador de regresión logística entrenado con 20 características sintéticas de la temperatura de impulsión de LDHP distinguir una deriva lenta del punto de consigna de los cambios normales de carga, medido por la exhaustividad con una tasa fija de falsas alarmas del 5 % en ejecuciones simuladas reservadas, sin ningún acceso a una planta real?».

**EX104.** «Todos los datos de este proyecto son sintéticos y los generan los scripts del repositorio; no se contactará con ningún controlador, red ni servicio reales. El monitor solo lee archivos de captura sin conexión. Si el trabajo revela una debilidad en cualquier producto real, se comunicará a través del proceso de divulgación del fabricante y no se publicará hasta que esté coordinado».

**EX105.** «El informe de evaluación contiene la matriz de confusión del conjunto de 8 casos, la precisión y la exhaustividad con numeradores y denominadores, la lista de clases de ataque no detectadas, el hash de commit del script y las semillas, y sus números coinciden con una nueva ejecución de `lab_eval.py`».

**EX106.** «Gracias por confiarme esto. Mi acuerdo de estancia no me permite escanear ni sondear sus sistemas, porque incluso los escaneos sencillos pueden perturbar los controladores antiguos. Lo que sí puedo hacer esta semana es revisar con usted sus mecanismos de acceso remoto y sus registros, y preguntaré a mi supervisor si una empresa cualificada debería hacer una evaluación técnica».

**EX107.** «La lista de activos se almacena solo en la carpeta cifrada del proyecto de la universidad, compartida con el supervisor y el gerente de la cooperativa, y se borra de todos los dispositivos del estudiante el último día de la estancia».

**EX108.** «Me sorprendió que un router celular pudiera estar en la sala de calderas sin aparecer en ningún plano ni factura: significa que el diagrama de red de la cooperativa no es un mapa fiable de cómo pueden alcanzar la caldera desde fuera».

**EX109.** (a) Peldaño inferior: una afirmación de marketing no verificada, sin método ni denominador. (b) Un informe de caso primario de una fuente gubernamental: más fuerte, pero se trata de un solo incidente.

**EX110.** La estimación de cuántos dispositivos se infectaron: los honeypots solo observan los bots que casualmente los escanean o atacan, así que cuentan de menos y están sesgados por dónde se sitúan; los datos del telescopio proporcionan la visión más amplia de la población.

**EX111.** «El detector se ajusta y se evalúa en la misma planta simulada, así que las tasas de falsas alarmas y de detección comunicadas probablemente sean optimistas y puedan no generalizarse. Ajusten los umbrales con semillas separadas, congélenlos y evalúen con al menos un modelo de proceso adicional o un conjunto de datos publicado».

**EX112.** Clasificar una escritura como benign-maint solo cuando procede de EWS-1 con una cuenta nominativa de ingeniero y su hora cae dentro de una ventana de mantenimiento vinculada a una incidencia abierta; seguir registrando la escritura e incluirla en la revisión diaria para que un interno no pueda esconderse tras la ventana.

**EX113.** TP sube a 4 y FN baja a 1, así que la exhaustividad = 4/5 = 0,80; la precisión queda en 4/5 = 0,80 si el falso positivo se mantiene.

**EX114.** Con 5 casos de ataque, 0,60 tiene un intervalo al 95 % de aproximadamente 0,23–0,88, y un conjunto de 10 casos tiene un intervalo igual de amplio y clases de ataque distintas, así que las dos cifras se solapan casi por completo y miden cosas diferentes.

**EX115.** (a) Resultado. (b) Interpretación, y una que va más allá de esta evidencia. (c) Limitación.

**EX116.** El análisis es reproducible, usa las métricas correctas y comunica los denominadores, pero ocho casos sintéticos con un único perfil de deriva no pueden respaldar afirmaciones generales, así que la evidencia es sólida pero estrecha: un 2 y no un 3.

**EX117.** Probar con un segundo modelo de proceso construido de forma independiente (o con capturas anonimizadas proporcionadas por un propietario mediante un acuerdo), porque la principal pregunta abierta es si el conjunto de reglas se generaliza más allá de la planta para la que se diseñó.

**EX118.** «Añadir una regla de cambio acumulado elevó la exhaustividad de 3/5 a 4/5 en el conjunto sintético de ocho casos: un hallazgo sobre clases de fallo, no una estimación de tasas».

**EX119.** «Harían escrituras desde el propio HMI-1 o mantendrían cada cambio por debajo del umbral acumulado, como describen Urbina et al. para los ataques sigilosos. Mi monitor no puede impedirlo; acota cuánto puede moverse el punto de consigna sin que se note, y correlacionar las escrituras con los inicios de sesión de los operadores es la siguiente defensa que probaría».

**EX120.** Cualquier exportación de configuración, captura o mapa de registros proporcionado por un propietario real, aunque esté anonimizado, porque puede revelar su arquitectura; se queda bajo el acuerdo de datos, mientras que el paquete público contiene solo los generadores sintéticos y las semillas.

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
