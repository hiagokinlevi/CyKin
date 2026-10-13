# Seguridad de TO, IoT y sistemas ciberfísicos: ingeniería de sistemas de control seguros

- Idioma: español neutro (`es`); curso de ingeniería, cinco años; aproximadamente 4.000 horas de estudio planificado. Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–50 de 50 tienen texto didáctico escrito; los ejercicios EX001–EX150 tienen sus resultados resueltos correspondientes; los laboratorios sin conexión usan solo la biblioteca estándar de Python 3, con salidas verificadas. Siguen pendientes la revisión independiente y la verificación de 300 páginas A4. La cobertura de capítulos en borrador no equivale a un libro terminado.
- Público: futuros ingenieros que diseñarán, implementarán y verificarán la seguridad de sistemas de control industrial, de TO y ciberfísicos.
- Relación con los libros vecinos: el libro de ingeniería de infraestructura crítica pone el énfasis en los sectores; el libro de maestría de TO, en el diseño de estudios empíricos. **Este libro trata de construir la seguridad de los sistemas de control**.
- Autoría: [hiagokinlevi](https://github.com/hiagokinlevi). Texto original bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus derechos.
- Límite educativo: no es un título acreditado ni una licencia profesional. No concede autorización para acceder a plantas reales. Todas las plantas, personas y números de los ejemplos son **sintéticos**, salvo que una frase cite una fuente pública.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los capítulos 1–19 construyen fundamentos aplicados a la TO desde la primera página. El capítulo 20 establece el contexto de TO. Los capítulos 21–42 forman el núcleo del campo, con talleres de diseño (25, 35) y laboratorios de verificación (30, 40). Los capítulos 43–50 son de práctica y proyecto final. Mantenga las etiquetas: **requisito**, **decisión de diseño**, **evidencia**, **riesgo residual**.

### Caso de diseño sintético

| Elemento | Función | Límite |
|---|---|---|
| **Ashford Batch Plant (ABP)** — reactor R-101, tanques de alimentación T-1/T-2, PLC-A, SIS-B, SCADA, historiador | Sistema en diseño | Inventado |
| **Control Network Hardening Programme (CNHP)** | El programa de ingeniería | Inventado |
| **Lena Okafor** | Ingeniera del CNHP | Inventada |

### Fuentes principales

- NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [presentación de ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); Modbus [Application Protocol V1.1b3](https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf); Giraldo et al. [CSUR 2018](https://doi.org/10.1145/3203245); Urbina et al. [CCS 2016](https://doi.org/10.1145/2976749.2978388).

## Contenido

| Capítulos |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Resultados resueltos](#worked-results) · [Referencias](#references)

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Resultados de aprendizaje

Usted podrá (1) modelar el nivel de un tanque como la integral del caudal neto; (2) usar ese modelo para calcular cuánto tiempo tienen los operadores tras la parada de una bomba; (3) explicar por qué ese tiempo es una magnitud de seguridad, no solo de proceso.

### 1.1 El nivel es caudal acumulado

El tanque de alimentación T-1 de Ashford Batch Plant (ABP) contiene V(t) metros cúbicos. Si la bomba de reposición se detiene en t = 0 y el reactor sigue extrayendo q(t) m³/h, entonces V(t) = V₀ − ∫₀ᵗ q(s) ds. El nivel baja exactamente tan rápido como sale el caudal, y el tiempo hasta alcanzar la autonomía mínima segura V_min es el t* que resuelve ∫₀^t* q(s) ds = V₀ − V_min. Cuando q es constante, esto es (V₀ − V_min)/q; cuando q varía, hay que integrar.

### 1.2 Por qué le importa a un ingeniero de seguridad

Un atacante capaz de detener una bomba o falsear una lectura de nivel cambia esta integral. El tiempo de autonomía es la ventana en la que los operadores o un sistema de seguridad deben darse cuenta y actuar. Si T-1 contiene 12 m³, el mínimo es 2 m³ y el reactor extrae unos 1,8 m³/h, los operadores tienen aproximadamente 5,5 horas. Ese número pasa directamente al requisito de detección: una alarma que salta a las seis horas no detecta nada útil. El cálculo convierte «detectar rápido» en «detectar en menos de 5,5 horas, con margen».

Lena escribe el número en el requisito junto con la forma en que se calculó.

### 1.3 Extracción variable

La extracción de ABP oscila con la receta del lote: q(t) = 1,8 + 0,4 sin(2πt/6). Su integral tiene forma cerrada, y el laboratorio resuelve t* por bisección. La respuesta, 5,53 h, se acerca a la estimación con caudal medio de 5,56 h porque la oscilación se compensa a lo largo de un ciclo completo de seis horas; con una ventana más corta o una receta sesgada, ambas divergirían, y la elección conservadora es el tiempo menor.

```python
# Lab 1 - tank hold-up after feed pump stop (Ashford Batch Plant, synthetic)
import math
V0, VMIN = 12.0, 2.0   # m3 in feed tank T-1
def outflow(t):         # m3/h to reactor; t hours after stop of makeup
    return 1.8 + 0.4*math.sin(2*math.pi*t/6)
def drawn(t):
    return 1.8*t - (0.4*6/(2*math.pi))*(math.cos(2*math.pi*t/6)-1)
lo,hi=0.0,24.0
for _ in range(50):
    mid=(lo+hi)/2
    lo,hi=(mid,hi) if drawn(mid)<V0-VMIN else (lo,mid)
print(f"time to min level: {lo:.2f} h")
print(f"average-rate estimate: {(V0-VMIN)/1.8:.2f} h")
```

Salida esperada:

```text
time to min level: 5.53 h
average-rate estimate: 5.56 h
```

> **Caso sintético — Ashford Batch Plant.** Lena Okafor, ingeniera del Control Network Hardening Programme (CNHP), usó el cálculo de autonomía para argumentar que una alarma de nivel bajo en T-1 debe ser independiente del PLC-A, porque un PLC comprometido podría suprimir tanto el estado de la bomba como la alarma dentro de la ventana de 5,5 horas.

### 1.4 Errores y límites

Los modelos suponen que el sensor de nivel es honesto; el capítulo 29 trata la suplantación de sensores. Mezclar m³/h con minutos es el desliz más común. Elija siempre la raíz conservadora cuando la incertidumbre sea grande. Una lectura de nivel falseada es el caso que este modelo no puede manejar: si el transmisor informa de un tanque lleno mientras T-1 se vacía, la integral es correcta, pero nadie la está mirando. Por eso Lena acompaña el cálculo de autonomía con un interruptor de nivel independiente. Compruebe las unidades en cada paso, escriba el tiempo en horas con la extracción supuesta al lado y repita el cálculo cada vez que la receta cambie la demanda del reactor.

### Ejercicios — capítulo 1

- **EX001 — Extracción constante.** T-2 contiene 9 m³, mínimo 1,5 m³, extracción constante de 1,25 m³/h. ¿Tiempo hasta el mínimo? Rúbrica: 3 = 6,0 h con el desarrollo; 2 = método correcto, error aritmético; 1 = solo la fórmula; 0 = nada.
- **EX002 — Requisito.** Convierta su respuesta de EX001 en un requisito de detección con margen. Rúbrica: 3 = límite de tiempo con margen declarado e independencia del PLC que controla; 2 = solo el límite de tiempo; 1 = un vago «rápido»; 0 = nada.
- **EX003 — Lectura del laboratorio.** ¿Por qué las respuestas por bisección y con caudal medio están tan cerca aquí, y cuándo no lo estarían? Rúbrica: 3 = un ciclo senoidal completo promedia 1,8; una ventana sesgada o corta diverge; 2 = una de las dos mitades; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

El tiempo de autonomía es a la vez una integral y un presupuesto de seguridad: acota cuán tarde puede llegar la detección.

### Siga estudiando — capítulo 01 de 50

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 (borrador) →](#ch-02)

<a id="ch-02"></a>

## Capítulo 2 — Matemáticas discretas

### Resultados de aprendizaje

Usted podrá (1) representar una red de TO como un grafo dirigido; (2) calcular la alcanzabilidad entre niveles de Purdue; (3) demostrar que eliminar una arista no puede añadir un camino.

### 2.1 Grafos de conductos

En el vocabulario de ISA/IEC 62443, las zonas son grupos de activos con requisitos de seguridad comunes y los conductos son los caminos de comunicación permitidos entre ellas. Un grafo dirigido lo modela con exactitud: los nodos son zonas (L4 oficina, L3.5 DMZ, L3 historiador, L2 SCADA, L1 PLC, L1 SIS, L0 E/S) y una arista a→b significa que a puede iniciar tráfico hacia b. La pregunta «¿puede la red de oficina escribir en el sistema de seguridad?» se convierte en «¿es L1-SIS alcanzable desde L4?».

Lena construye el grafo de ABP a partir de la exportación del cortafuegos, no del diagrama de red, porque la exportación es lo que realmente se aplica.

### 2.2 Alcanzabilidad

La búsqueda en profundidad calcula el conjunto de nodos alcanzables desde un nodo inicial en un tiempo proporcional a los nodos más las aristas. La alcanzabilidad es transitiva: si L4→L3, L3→L2 y L2→L1-SIS, entonces L4 alcanza el SIS aunque no haya ninguna regla directa. Las revisiones de cortafuegos que comprueban las reglas una por una pasan por alto justamente esta composición, y por eso los ingenieros calculan el cierre en lugar de leer listas de reglas. Lena ejecuta la búsqueda desde cada zona, no solo desde la oficina, y guarda el resultado como una tabla con la que la siguiente revisión pueda compararse.

### 2.3 Demostración de monotonía

Afirmación: eliminar una arista nunca agranda un conjunto alcanzable. Demostración: cualquier camino del grafo menor usa solo aristas que también existen en el grafo mayor, de modo que todo nodo alcanzable tras la eliminación ya era alcanzable antes. De ahí se sigue la regla práctica: las eliminaciones de reglas pueden aprobarse con rapidez; las adiciones requieren análisis, porque pueden crear nuevos caminos transitivos.

```python
# Lab 23 - reachability count on a synthetic Purdue-layered OT network
# Nodes: L5-ERP, L4-Office, L3.5-DMZ, L3-Hist, L2-SCADA, L1-PLC, L1-SIS, L0-IO
edges_flat=[("L5","L4"),("L4","L3"),("L3","L2"),("L2","L1-PLC"),("L2","L1-SIS"),("L1-PLC","L0"),("L1-SIS","L0"),("L4","L2")]
edges_zoned=[("L5","L4"),("L4","L3.5"),("L3.5","L3"),("L3","L2"),("L2","L1-PLC"),("L1-SIS","L0"),("L1-PLC","L0")]  # SIS not reachable from SCADA
def reach(edges, start):
    g={}; 
    for a,b in edges: g.setdefault(a,[]).append(b)
    seen=set(); stack=[start]
    while stack:
        n=stack.pop()
        if n in seen: continue
        seen.add(n); stack.extend(g.get(n,[]))
    return seen
for name,e in (("flat",edges_flat),("zoned",edges_zoned)):
    r=reach(e,"L4")
    print(f"{name}: L4 reaches {sorted(r)} count={len(r)} writes_to_SIS={'L1-SIS' in r}")
```

Salida esperada:

```text
flat: L4 reaches ['L0', 'L1-PLC', 'L1-SIS', 'L2', 'L3', 'L4'] count=6 writes_to_SIS=True
zoned: L4 reaches ['L0', 'L1-PLC', 'L2', 'L3', 'L3.5', 'L4'] count=6 writes_to_SIS=False
```

> **Caso sintético — Ashford Batch Plant.** La red original de ABP tenía una regla de conveniencia L4→L2 para ver el HMI a distancia. El laboratorio de alcanzabilidad muestra que, en el diseño plano, la zona de oficina alcanza L1-SIS; en el diseño por zonas, con una DMZ y sin conducto SCADA→SIS, no lo alcanza.

### 2.4 Errores y límites

Los grafos modelan el inicio permitido, no el tráfico real ni las vulnerabilidades. Los protocolos bidireccionales y las herramientas de acceso remoto pueden crear aristas inversas ocultas; inventaríelas de forma explícita. Lena añade una herramienta de acceso remoto usada por un proveedor como arista explícita desde fuera de la planta hacia L2, ya que sus sesiones se inician hacia fuera pero transportan órdenes hacia dentro. Sin esa arista, el grafo mostraría la oficina aislada de SCADA mientras una sesión de soporte todavía podría alcanzarlo. Cada una de estas aristas figura con su responsable y el registro que la justifica, y el grafo se reconstruye tras cualquier cambio en las herramientas de acceso remoto o en los contratos con proveedores.

### Ejercicios — capítulo 2

- **EX004 — Cierre.** Aristas: A→B, B→C, C→D, B→E. Enumere todos los nodos alcanzables desde A. Rúbrica: 3 = {A,B,C,D,E}; 2 = falta uno; 1 = solo los directos; 0 = nada.
- **EX005 — Uso de la demostración.** Explique en dos frases por qué añadir L3→L1-SIS requiere más revisión que eliminar L4→L2. Rúbrica: 3 = la adición puede crear nuevos caminos transitivos y la eliminación no (monotonía); 2 = solo intuición; 1 = vago; 0 = incorrecto.
- **EX006 — Laboratorio.** ¿Qué arista concreta del diseño plano da a L4 su camino hasta L1-SIS? Rúbrica: 3 = L2→L1-SIS (con L4→L2 o L4→L3→L2 aguas arriba); 2 = solo nombra L4→L2; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

Las zonas y los conductos son un grafo; la alcanzabilidad, y no la lectura regla por regla, responde quién puede tocar el sistema de seguridad.

### Siga estudiando — capítulo 02 de 50

[← Capítulo 01 (borrador)](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 (borrador) →](#ch-03)

<a id="ch-03"></a>

## Capítulo 3 — Física para la computación

### Resultados de aprendizaje

Usted podrá (1) calcular la temporización de enlaces serie para el sondeo de buses de campo; (2) relacionar la velocidad del proceso físico con los tiempos de ciclo de control necesarios; (3) reconocer que las señales físicas pueden manipularse fuera de la red.

### 3.1 Bits en un cable

Gran parte de la comunicación de planta sigue funcionando sobre RS-485 serie a velocidades como 115.200 bit/s. Con un bit de inicio, ocho bits de datos y un bit de parada, cada byte cuesta diez tiempos de bit. Por tanto, una respuesta Modbus RTU de 40 bytes tarda 40 × 10 / 115.200 ≈ 3,5 ms en el cable, antes del procesamiento en el dispositivo. Sumar todos los sondeos de un ciclo indica si la planificación cabe en el presupuesto de ciclo del controlador.

```python
"""Lab: does a polling schedule fit the PLC scan/communication budget? (synthetic)"""
link_bps = 115200; bits_per_byte = 10           # RS-485 serial, 8N1 + start bit
polls = [("T-1 level", 8), ("T-2 level", 8), ("R-101 block", 40), ("pump status", 8), ("historian sweep", 120)]
overhead = 12                                    # bytes of request+framing per poll (assumed)
total = sum(n + overhead for _, n in polls)
t = total * bits_per_byte / link_bps
print(f"bytes per cycle={total} time per cycle={t*1000:.1f} ms")
for target in (100, 50):
    print(f"cycle budget {target} ms -> {'fits' if t*1000 <= target else 'OVERRUN'}")
```

Salida esperada:

```text
bytes per cycle=244 time per cycle=21.2 ms
cycle budget 100 ms -> fits
cycle budget 50 ms -> fits
```

Lena hace esta suma para la línea troncal hacia el PLC-A antes de aprobar cualquier dispositivo de monitorización en ella, y el resultado es la cifra de 21 ms que luego usa en todo el programa.

### 3.2 Constantes de tiempo del proceso

Un lazo de nivel en un tanque de 12 m³ cambia en minutos; un lazo de presión en un compresor cambia en decenas de milisegundos. La velocidad de control y de detección necesaria se deriva de la física. Una monitorización de seguridad que añade 200 ms de latencia es inofensiva en el tanque y peligrosa en el compresor. Pregunte siempre cuál es la constante de tiempo del proceso antes de insertar dispositivos de inspección en línea. En ABP, los tanques de alimentación y el nivel del reactor son lazos lentos, mientras que un patín de compresor cercano es rápido. Lena enumera los lazos de cada línea troncal con sus constantes de tiempo antes de elegir dónde puede ubicarse un monitor.

### 3.3 Manipulación de la capa física

Los sensores miden física: un lazo de 4–20 mA, la tensión de un termopar, un pulso de un caudalímetro. Un adversario o una falla pueden alterar esas señales sin tocar ningún paquete de red: inyectando corriente, calentando una sonda o haciendo vibrar un medidor. La monitorización de red no puede verlo; las comprobaciones de plausibilidad física (capítulo 29) y las envolventes con evidencia de manipulación sí pueden.

> **Caso sintético — Ashford Batch Plant.** El presupuesto de sondeo de Lena para la línea troncal RS-485 hacia el PLC-A resultó de 21 ms por ciclo, holgadamente dentro del ciclo de 100 ms. Eso dejaba margen para un monitor serie en línea, que ella aprobó solo después de medir en una copia de banco la latencia que añadía.

### 3.4 Errores y límites

Los cálculos de temporización ignoran el tiempo de respuesta de los dispositivos y los reintentos; mida en un banco antes de comprometerse. No pruebe la inyección de señales en lazos en servicio. La copia de banco de Lena de la línea troncal RS-485 hacia el PLC-A es donde se midieron el presupuesto de sondeo y la latencia añadida por el monitor serie, y es el único lugar donde el trabajo del curso toca la temporización serie. Cualquier experimento de inyección de señales, incluso un pequeño sesgo en un lazo de 4–20 mA, corresponde a un banco con un transmisor de repuesto, nunca al lazo en servicio de T-1. Registre los resultados de banco con el equipo utilizado, porque otro transmisor u otro cable pueden cambiar los números.

### 3.5 Ejemplo resuelto: niveles de señal y presupuesto de tiempo (ABP sintética)

El transmisor de nivel de T-1 envía una señal de 4–20 mA por 180 m de par trenzado hasta el PLC-A. Un sesgo de 0,2 mA inyectado en un armario de distribución desplaza la lectura en 0,2/16 = 1,25 % del rango, lo que para el rango calibrado de 9 m³ del transmisor equivale a unos 0,11 m³: lo bastante pequeño para ocultarse dentro del ruido normal. La constante de tiempo del tanque (rango dividido por el caudal de entrada típico, 9/1,25 ≈ 7,2 h) indica a Lena cuánto tiempo puede actuar un sesgo así antes de que el cálculo de autonomía del capítulo 1 se equivoque en todo un margen de seguridad. Por eso especifica un segundo interruptor de nivel independiente en T-1, cableado al SIS-B, y una comparación periódica entre transmisor e interruptor, porque así un ataque a la capa física de un lazo no puede anular ambos en silencio.

### Ejercicios — capítulo 3

- **EX007 — Tiempo en el cable.** ¿Cuánto tarda una trama de 120 bytes a 19.200 bit/s con 10 bits por byte? Rúbrica: 3 = 62,5 ms con el desarrollo; 2 = error; 1 = método; 0 = nada.
- **EX008 — Presupuesto.** Con los 244 bytes por ciclo del laboratorio, ¿cuál es la velocidad en baudios más lenta que todavía cabe en un presupuesto de 50 ms? Rúbrica: 3 = 48.800 bit/s (por tanto, 57.600 estándar) con el desarrollo; 2 = número sin velocidad estándar; 1 = método; 0 = nada.
- **EX009 — Física.** Indique dos manipulaciones de la capa física que un IDS de red no puede detectar y un control compensatorio para cada una. Rúbrica: 3 = dos manipulaciones más controles; 2 = dos sin controles; 1 = una; 0 = nada.

### Síntesis del capítulo

La física fija el presupuesto de tiempo del control y de cualquier dispositivo de seguridad que se coloque en el lazo.

### Siga estudiando — capítulo 03 de 50

[← Capítulo 02 (borrador)](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 (borrador) →](#ch-04)

<a id="ch-04"></a>

## Capítulo 4 — Programación I

### Resultados de aprendizaje

Usted podrá (1) escribir funciones pequeñas y puras que decidan si un mensaje de TO está permitido; (2) representar direcciones industriales con tipos exactos; (3) probar con tráfico decodificado sintético, nunca con tráfico real de planta.

### 4.1 Decisiones como funciones

Una lista de permitidos para Modbus es una función `permit(source, function_code, register) -> (bool, reason)`. Hacerla pura —entradas que llegan, decisión que sale, sin configuración oculta— permite probarla en un portátil con registros sintéticos. La cadena del motivo importa: «register-out-of-range» le dice a un revisor que el HMI intentó escribir fuera del bloque de puntos de consigna, lo cual es una historia distinta de la de una estación desconocida que usa una función de diagnóstico. Lena mantiene las cadenas de motivo cortas y fijas para que los registros puedan contarse por motivo.

### 4.2 Tipos exactos

Guarde los códigos de función como enteros, los rangos de registros como objetos `range` y las identidades de las estaciones como cadenas fijas tomadas de un inventario. Un error frecuente trata la notación 4xxxx de «registro de retención» como una cadena y compara por prefijo, de modo que 400500 parece 40050. Convierta las direcciones una sola vez, al analizarlas, en enteros con desplazamientos documentados. Lena escribe una única función de conversión para las direcciones de registro y la prueba en ambos extremos del rango escribible del HMI, 40001 y 40010, y un paso fuera de cada uno. Los nombres de estación provienen del inventario, de modo que una errata en la lista de permitidos hace fallar una búsqueda en lugar de crear en silencio una estación nueva que no coincide con nada.

### 4.3 Pruebas con tramas decodificadas sintéticas

El laboratorio siguiente nunca abre un socket; comprueba tuplas ya decodificadas. Es deliberado. El código del curso no debe enviar tráfico Modbus a ningún dispositivo. Escriba una prueba por regla, más los registros límite 40001 y 40010.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Salida esperada:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

Las pruebas se agrupan por regla para que un fallo apunte directamente a la cláusula que se rompió. La prueba de escritura del historiador, que detectó la función 16, se conserva como caso permanente. La tabla de pruebas de Lena enumera cada tupla, la decisión esperada y la cadena del motivo, y un revisor puede leerla sin ejecutar nada. Las nuevas estaciones o registros que se añaden a la lista de permitidos llegan con sus propias filas en la misma solicitud de incorporación de cambios (pull request).

### 4.3b Registrar lo que decidió la función

Cada decisión debe registrarse con el origen, el código de función, el registro, la decisión, el motivo y la versión del archivo de la lista de permitidos. Cuando un operador pregunta por qué se bloqueó una escritura del HMI a las 03:12, el registro responde en una línea. Sin el campo de versión, nadie puede saber si el bloqueo vino de la lista de ayer o de la de hoy.

> **Caso sintético — Ashford Batch Plant.** La primera lista de permitidos de Lena dejaba que HIST-1 usara la función 16 (escribir múltiples registros) porque «solo lee». La tabla de pruebas lo detectó: el historiador no tiene por qué escribir, así que se eliminó la función 16 y la prueba ahora espera BLOCK.

### 4.4 Errores y límites

Una lista de permitidos en un monitor es tan buena como su decodificador. Las tramas mal formadas deben contarse y generar alarma, no descartarse en silencio. Los dispositivos reales de aplicación necesitan validación del proveedor antes del despliegue. El monitor de Lena cuenta las tramas mal formadas por minuto y genera una alarma si la cuenta sube, porque una ráfaga repentina puede indicar un dispositivo que falla o un error del decodificador. Tratar esas tramas como permitidas convertiría cada laguna del decodificador en una puerta abierta. El monitor de este curso solo observa; cualquier dispositivo que realmente bloquee tráfico en ABP es un producto de proveedor validado antes en el banco.

### Ejercicios — capítulo 4

- **EX010 — Regla.** Escriba la regla de permiso (en palabras o en código) para «HIST-1 puede leer registros de entrada y de retención, nada más». Rúbrica: 3 = solo fc 3 y 4, todo lo demás BLOCK con motivo; 2 = falta un motivo; 1 = vago; 0 = incluye escrituras.
- **EX011 — Límites.** ¿Qué valores de registro prueban los extremos del rango de escritura del HMI en el laboratorio, y qué se espera para 40011? Rúbrica: 3 = 40001 y 40010 PASS, 40011 BLOCK; 2 = un extremo; 1 = vago; 0 = incorrecto.
- **EX012 — Laboratorio.** ¿Por qué se bloquea ENG-WS fc=8, y por qué es ese el comportamiento predeterminado correcto? Rúbrica: 3 = no hay entrada (ENG-WS, 8); diagnóstico/denegación predeterminada; 2 = la primera mitad; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

Las funciones de permiso puras, tipadas y probadas son la unidad más pequeña y fiable del software de seguridad de TO.

### Siga estudiando — capítulo 04 de 50

[← Capítulo 03 (borrador)](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 (borrador) →](#ch-05)

<a id="ch-05"></a>

## Capítulo 5 — Comunicación en ingeniería

### Resultados de aprendizaje

Usted podrá (1) redactar hallazgos de seguridad de TO sobre los que operadores e ingenieros de seguridad funcional puedan actuar; (2) separar observación, consecuencia y recomendación; (3) evitar el lenguaje alarmista o sin límites.

### 5.1 Tres públicos

Un operador de sala de control necesita saber qué vigilar. Un ingeniero de seguridad de procesos necesita saber si una función de seguridad se ve afectada. Un directivo necesita costes y tiempo de parada. Un mismo hallazgo puede servir a los tres si indica: activo y zona; qué se observó y cómo; la consecuencia plausible en el proceso; el estado de la capa de seguridad; la corrección y la ventana de mantenimiento necesaria. Lena escribe cada hallazgo una sola vez, en ese orden, para que cada lector encuentre rápido su parte. Un hallazgo al que le falte alguna de estas partes vuelve a su autor antes de la revisión.

### 5.2 Consecuencias acotadas

«Un atacante podría hacer volar la planta» no es ni cierto ni útil. Una afirmación acotada dice: «Una estación en L2 puede escribir registros de punto de consigna en el PLC-A sin autenticación. Un cambio del punto de consigna de nivel de T-1 podría sobrellenar el tanque en unos 40 minutos; el disparo independiente por nivel muy alto del SIS-B detendría la bomba de alimentación antes del desbordamiento». Esto nombra el camino, el tiempo y la capa de protección que sigue en pie.

Lena revisa cada afirmación acotada con el ingeniero de seguridad de procesos antes de enviarla, ya que los minutos hasta el desbordamiento y el disparo que se mantiene provienen del análisis de seguridad de procesos, no del equipo de seguridad de la información.

### 5.3 Estructura de un informe breve

Resumen (tres frases); alcance y método; hallazgos ordenados por consecuencia; riesgo residual con las capas de protección nombradas; apéndice con referencias a la evidencia. Los diagramas de zonas valen más que páginas de tablas de reglas. Los informes de Lena para el CNHP caben en dos páginas más el apéndice. El resumen nombra el hallazgo más grave e indica si alguna función de seguridad se ve afectada. Cada hallazgo cita su evidencia por hash e indica la ventana de mantenimiento necesaria para la corrección, de modo que los planificadores puedan programarla. Un diagrama de zonas con el conducto afectado resaltado suele explicar el hallazgo más rápido que el texto.

### 5.3b Palabras que evitar y palabras que usar

Evite «trivial», «catastrófico» y «totalmente comprometido»: ninguna puede comprobarse. Use magnitudes medidas —minutos hasta el desbordamiento, número de zonas alcanzables, capas de protección intactas— y nombre la evidencia. Un ingeniero de seguridad funcional confiará mucho más en un hallazgo que dice «el SIS-B sigue siendo independiente» que en uno que dice «todo está en riesgo».

> **Caso sintético — Ashford Batch Plant.** El primer borrador de un hallazgo de Lena decía que la red SCADA era «totalmente insegura». La versión revisada: «La regla de visualización remota L4→L2 permite que los equipos de oficina alcancen los servidores SCADA (regla FW-12, observada en la exportación de configuración del 3 de marzo). Se recomienda eliminarla y visualizar a través de la réplica del historiador en la DMZ. Tiempo de parada: ninguno».

### 5.4 Errores y límites

Nunca incluya procedimientos de ataque operativos en los informes; remita al almacén de evidencia. No afirme una consecuencia de seguridad funcional sin la revisión del ingeniero de seguridad de procesos. La evidencia, como las exportaciones de configuración, permanece en el almacén sellado, y el informe la cita por hash, de modo que cualquiera con acceso pueda verificarla sin que el informe contenga detalles sensibles. Lena envía cada hallazgo que menciona el SIS-B o un disparo al ingeniero de seguridad de procesos para que lo revise antes de publicarlo, y registra en el informe el nombre del revisor. Una consecuencia que el ingeniero no ha confirmado se escribe como pregunta, no como afirmación.

### Ejercicios — capítulo 5

- **EX013 — Reescritura.** Reescriba «el PLC puede ser hackeado» como una frase de hallazgo acotada para el PLC-A. Rúbrica: 3 = camino, zona, observación, límite de la consecuencia, capa de protección; 2 = falta uno; 1 = sigue siendo vaga; 0 = sin cambios.
- **EX014 — Público.** Para el hallazgo FW-12, escriba una frase para el operador, otra para el ingeniero de seguridad funcional y otra para el directivo. Rúbrica: 3 = tres frases adaptadas; 2 = dos; 1 = una; 0 = nada.
- **EX015 — Riesgo residual.** Tras eliminar FW-12, enuncie con honestidad un riesgo residual. Rúbrica: 3 = camino restante específico (p. ej., estación de ingeniería, acceso remoto del proveedor) y su control; 2 = genérico; 1 = «ninguno»; 0 = nada.

### Síntesis del capítulo

Los buenos hallazgos de TO están acotados, nombran las capas de protección y dan a cada público lo que necesita para decidir.

### Siga estudiando — capítulo 05 de 50

[← Capítulo 04 (borrador)](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 (borrador) →](#ch-06)

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Resultados de aprendizaje

Usted podrá (1) usar series para razonar sobre los reintentos repetidos de las comunicaciones de planta; (2) aplicar un modelo diferencial sencillo a la acumulación de alarmas; (3) decidir cuándo un modelo continuo basta para un debate de mantenimiento.

### 6.1 Reintentos geométricos en un bus de campo

Si cada solicitud Modbus tiene éxito con probabilidad p = 0,9 de forma independiente (sintético, para una línea troncal ruidosa), la probabilidad de tener éxito en k intentos o menos es 1 − (1 − p)^k. Con k = 3, eso es 0,999. Los reintentos aumentan la fiabilidad pero multiplican el tráfico: el número esperado de intentos hasta el éxito es 1/p ≈ 1,11, de modo que un ciclo de 1.000 sondeos espera unas 1.110 tramas. El presupuesto de comunicaciones (capítulo 3) debe contar los reintentos, no solo los sondeos lógicos. Lena incluye los reintentos cuando comprueba la línea troncal RS-485 hacia el PLC-A, ya que un periodo ruidoso puede elevar el tráfico en una décima parte o más.

### 6.2 La acumulación de alarmas como ecuación de tasas

Sea B(t) el número de alarmas abiertas. Las alarmas llegan con tasa a y se reconocen con tasa c cuando hay personal. Entonces B′ ≈ a − c. Si a = 3,3/h (la tasa previa a la racionalización del laboratorio de alarmas) y dos operadores juntos atienden 2,0/h, la acumulación crece. Tras la racionalización a 1,05/h, el mismo personal la absorbe. El modelo es tosco —ignora la prioridad—, pero vuelve cuantitativos el dimensionamiento del personal y la racionalización.

```python
"""Lab: alarm load per operator hour before and after rationalisation (synthetic counts)."""
before = {"T-1 high": 140, "T-2 high": 95, "R-101 temp": 30, "pump trip": 6, "comm loss PLC-A": 210, "door open": 75}
remove = {"comm loss PLC-A": 200, "door open": 70, "T-1 high": 110}   # chattering/duplicate alarms removed
hours = 24 * 7
tb = sum(before.values()); ta = tb - sum(remove.values())
print(f"week alarms before={tb} after={ta}")
print(f"per operator-hour before={tb/hours:.2f} after={ta/hours:.2f}")
top = max(before, key=before.get)
print(f"worst source before: {top} ({before[top]/tb:.0%} of load)")
```

Salida esperada:

```text
week alarms before=556 after=176
per operator-hour before=3.31 after=1.05
worst source before: comm loss PLC-A (38% of load)
```

Lena usa el modelo para defender la racionalización antes de pedir personal. Los números dejaron el caso claro.

### 6.3 Cuándo basta lo continuo

Los debates de mantenimiento suelen necesitar un orden de magnitud: «¿Saturarán a un operador 200 alarmas intermitentes de pérdida de comunicación por semana?». Sí: eso solo ya supone unas 1,2/h. Reserve el análisis exacto para los lazos que afectan a la temporización de seguridad.

> **Caso sintético — Ashford Batch Plant.** El laboratorio de alarmas redujo la carga semanal de 556 a 176 eliminando fuentes intermitentes conocidas. Lena usó B′ para mostrar que un único operador nocturno podría mantener el ritmo tras el cambio, lo que desbloqueó la propuesta del CNHP, estancada en «primero necesitamos más personal».

### 6.4 Errores y límites

La independencia de los reintentos falla cuando la línea troncal está caída de forma sistemática. Los modelos de acumulación ignoran las alarmas críticas para la seguridad que deben interrumpir; trátelas por separado. Cuando la línea troncal hacia el PLC-A está caída, todos los reintentos fallan juntos, de modo que la fórmula geométrica sobrestima mucho la fiabilidad; Lena trata una caída de la línea troncal como un caso aparte con su propia alarma. Del mismo modo, el nivel muy alto en T-1 o un disparo del SIS-B deben llegar al operador de inmediato, sea cual sea la acumulación de alarmas rutinarias. El modelo de tasas sirve para planificar el personal y la racionalización, no para decidir qué alarmas pueden esperar.

### Nota práctica

Mantenga un gráfico semanal de a y c junto al registro de racionalización de alarmas. Cuando a sube tras un cambio de firmware, sabrá que debe buscar una nueva fuente intermitente antes de culpar a los operadores.

### Ejercicios — capítulo 6

- **EX016 — Reintentos.** Con p = 0,85 y 500 sondeos, ¿tramas esperadas? Rúbrica: 3 ≈ 588 con el desarrollo; 2 = error; 1 = fórmula; 0 = nada.
- **EX017 — Acumulación.** B(0)=40, a=1.0/h, c=1.5/h. ¿Horas hasta vaciarla? Rúbrica: 3 = 80 h; 2 = método; 1 = cualitativo; 0 = nada.
- **EX018 — Laboratorio.** ¿Qué fracción de la carga previa al cambio correspondía a «comm loss PLC-A»? Rúbrica: 3 = 38 %; 2 = solo el conteo; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

Las series y las tasas convierten «inténtelo de nuevo» y «contrate a alguien» en números que encajan en una decisión de comunicaciones o de personal.

### Siga estudiando — capítulo 06 de 50

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](#ch-07)

<a id="ch-07"></a>

## Capítulo 7 — Probabilidad y estadística

### Resultados de aprendizaje

Usted podrá (1) informar tasas de detección con intervalos; (2) comparar detectores sin exagerar las conclusiones; (3) rechazar clasificaciones que la muestra no puede sostener.

### 7.1 Tasas e intervalos

Sesenta ensayos sintéticos con 0 falsas alarmas y 60/60 detecciones parecen perfectos, hasta que se recuerda que un intervalo de Wilson al 95 % para 0/60 todavía admite, a largo plazo, una tasa de falsas alarmas de unos pocos puntos porcentuales. Informe el intervalo, no solo el valor puntual. Para 60/60 detecciones, el intervalo de la tasa de omisión también es estrecho, pero no es cero para siempre. Los informes de Lena para el CNHP dan juntos el conteo, el intervalo y la lista de semillas, de modo que el lector puede ver tanto el resultado como cuánto podría moverse con más ensayos.

### 7.2 Comparar detectores

El laboratorio de CUSUM sobre residuos muestra un detector de banda que no detecta los ataques de clase A, mientras que el CUSUM los detecta con un retardo medio de ~25 muestras, ambos con 0/60 falsas alarmas en este conjunto de semillas. Eso es evidencia de que el CUSUM supera a la banda *en estos ataques sintéticos*, no de que el CUSUM sea mejor en general. Prefiera diseños pareados sobre las mismas trazas e indique la clase de ataque.

```python
# Lab 27 - residual CUSUM vs band on batch reactor level (synthetic)
import random
def run(seed, atk, det, k=0.8, h=6.0):
    rng=random.Random(seed); true=est=50.0; s=0.0; alarm=None
    for t in range(500):
        inflow=1.0+rng.gauss(0,0.05)+(0.08 if atk and t>=250 else 0)
        true+=inflow-0.02*true
        lvl=true+rng.gauss(0,0.3); fm=inflow+rng.gauss(0,0.02)
        if atk and t>=250: lvl=50+rng.gauss(0,0.3)
        if atk=="B" and t>=250: fm=1.0+rng.gauss(0,0.02)
        est+=fm-0.02*est
        hit=abs(lvl-50)>2.0 if det=="band" else False
        if det=="cusum":
            s=max(0.0,s+abs(lvl-est)-k); hit=s>h
        if hit and alarm is None: alarm=t
    return alarm
for det in ("band","cusum"):
    fa=sum(run(i,None,det) is not None for i in range(60))
    for atk in ("A","B"):
        hits=[a-250 for a in (run(i,atk,det) for i in range(60)) if a is not None and a>=250]
        print(f"{det} class{atk} FA={fa}/60 det={len(hits)}/60 mean_delay={sum(hits)/len(hits) if hits else float('nan'):.1f}")
```

Salida esperada:

```text
band classA FA=0/60 det=0/60 mean_delay=nan
band classB FA=0/60 det=0/60 mean_delay=nan
cusum classA FA=0/60 det=60/60 mean_delay=24.8
cusum classB FA=0/60 det=0/60 mean_delay=nan
```

El plan piloto de Lena conserva las mismas trazas para ambos detectores y nombra la clase de ataque probada, para que la comparación pueda repetirse más adelante con semillas nuevas.

### 7.3 Tasas base en la sala de control

Si los ataques ciberfísicos genuinos son raros, un detector con una tasa de falsas alarmas de apenas un 1 % dominará la atención del operador. La regla de Bayes se aplica exactamente como en el capítulo 7 de los cursos de seguridad vecinos: la precisión se desploma cuando la tasa base es diminuta. Diseñe para la tasa base de la planta, no para el conjunto equilibrado de un laboratorio.

> **Caso sintético — Ashford Batch Plant.** Un proveedor afirmó «99 % de detección, 0 % de falsas alarmas» a partir de una demostración de 20 ejecuciones. Lena pidió la clase de ataque, la lista de semillas y el intervalo de falsas alarmas; no se aportó ninguno. El piloto usó en su lugar el diseño del laboratorio de CUSUM.

### 7.4 Errores y límites

Los ataques sintéticos no son el adversario. Los intervalos suponen ensayos independientes; las semillas correlacionadas los invalidan. Nunca invente un valor p para una tabla que no ha sometido a prueba. Los informes piloto de Lena indican que los ataques eran sintéticos, enumeran las semillas y explican cómo se generaron. Si dos semillas producen trazas casi idénticas, las cuenta como un solo ensayo, porque tratarlas como independientes haría que el intervalo pareciera más estrecho de lo que la evidencia sostiene. Toda prueba estadística que informa es una que ejecutó de verdad, y conserva sus entradas para que un revisor pueda repetirla.

### Nota práctica

Publique la lista de semillas y los parámetros del detector con cada afirmación de detección en los documentos del CNHP. La reproducibilidad es más barata que discutir sobre una diapositiva seis meses después, y es lo que Urbina et al. y Giraldo et al. exigen de las evaluaciones.

### Ejercicios — capítulo 7

- **EX019 — Intervalo.** Indique qué le permite afirmar, a ~95 %, un resultado de 0/60 falsas alarmas. Rúbrica: 3 = cota superior de ~5–6 % (regla del tres / Wilson), no «cero para siempre»; 2 = solo la cota; 1 = «cero»; 0 = nada.
- **EX020 — Laboratorio.** Para el CUSUM en la clase A, informe las detecciones y el retardo medio. Rúbrica: 3 = 60/60 y ~24,8; 2 = un número; 1 = vago; 0 = incorrecto.
- **EX021 — Rechazo de la clasificación.** La banda y el CUSUM muestran ambos FA=0/60 en la clase B (sin detecciones). Escriba la frase que se niega a declararlos de igual calidad. Rúbrica: 3 = menciona la falta de potencia / la necesidad de la clase A o de un n mayor; 2 = cautela vaga; 1 = los declara iguales; 0 = nada.

### Síntesis del capítulo

Las afirmaciones de detección necesitan intervalos, clase de ataque y honestidad sobre la tasa base, no un único porcentaje.

### Siga estudiando — capítulo 07 de 50

[← Capítulo 06 (borrador)](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 (borrador) →](#ch-08)

<a id="ch-08"></a>

## Capítulo 8 — Arquitectura de computadores

### Resultados de aprendizaje

Usted podrá (1) situar el PLC, el SIS y el SCADA en un mapa de privilegios y dependencias; (2) explicar por qué los sistemas de seguridad funcional necesitan hardware independiente; (3) diseñar una recogida de evidencia que no requiera escribir en el PLC.

### 8.1 Privilegios en la planta

Un PLC ejecuta el lazo básico de regulación. Un SIS implementa las funciones instrumentadas de seguridad y debe poder actuar cuando el PLC se equivoca o está comprometido. El SCADA y los HMI son de supervisión: fijan puntos de consigna y muestran el estado. Una arquitectura que permite al SCADA escribir en la lógica del SIS anula esa independencia, que es exactamente lo que advertía el laboratorio de alcanzabilidad. En ABP, el PLC-A ejecuta los lazos de regulación de T-1, T-2 y R-101, y el SIS-B contiene los disparos. Lena marca estas funciones en su mapa de privilegios.

### 8.2 La independencia es física

La independencia no es una etiqueta de VLAN. Significa controladores separados, sensores propios donde lo exija la especificación de requisitos de seguridad y conductos que no permitan a la red de regulación alterar la lógica de seguridad. Tanto NIST SP 800-82 como ISA/IEC 62443 tratan los sistemas de seguridad funcional como necesitados de una zonificación cuidadosa; las normas de seguridad de procesos (IEC 61511) van más lejos en materia de independencia. La arquitectura de seguridad de la información no debe deshacer lo que pagó la arquitectura de seguridad funcional.

Lena comprueba la independencia siguiendo cables y conductos, no leyendo etiquetas en el plano de red. Los sensores de nivel propios del SIS-B en T-1 son el ejemplo más claro de esa independencia.

### 8.3 Evidencia sin escribir en el PLC

La evaluación autorizada de la TO prefiere los métodos de solo lectura: exportaciones de configuración, datos replicados del historiador, puertos espejo, monitores serie en modo escucha. Escribir un punto de consigna de prueba en un PLC en servicio es un cambio de proceso y necesita la misma autorización que un cambio de ingeniería. Los laboratorios del curso nunca escriben en dispositivos reales.

> **Caso sintético — Ashford Batch Plant.** El SIS-B es un controlador separado con sus propios sensores para el nivel muy alto de T-1. El conjunto de reglas del CNHP prohíbe cualquier conducto desde L2/L3 hacia los puertos de ingeniería del SIS, salvo a través de un conmutador físico con llave bloqueado durante las pruebas programadas.

### 8.4 Errores y límites

Las afirmaciones de «air gap» (aislamiento físico) suelen ocultar USB, portátiles de proveedores y módems celulares. Inventaríe esas vías fuera de banda con el mismo cuidado que las rutas IP. El inventario de Lena para ABP enumera cada puerto USB de los HMI y de las estaciones de ingeniería, cada portátil de proveedor que se conecta para dar soporte y cada módem celular instalado para diagnóstico remoto. Cada uno recibe un responsable y un control, como el bloqueo del puerto o una salida registrada. Una planta descrita como aislada se contrasta con esta lista antes de que alguien repita la afirmación en un informe, porque un solo módem olvidado puede crear un camino que el grafo de zonas nunca muestra.

### Nota práctica

Dibuje el mapa de privilegios en una página: quién puede cambiar puntos de consigna, quién puede cambiar la lógica, quién puede cambiar los puntos de consigna de seguridad y a través de qué puertos físicos. Cuélguelo en la sala de ingeniería. Las discusiones sobre «solo una regla temporal» se acaban antes cuando el mapa está a la vista.

### Ejercicios — capítulo 8

- **EX022 — Mapa.** Nombre tres acciones que requieran privilegio de ingeniería del SIS y tres que un HMI normal pueda realizar. Rúbrica: 3 = seis bien repartidas; 2 = cuatro; 1 = vago; 0 = nada.
- **EX023 — Independencia.** ¿Por qué la separación por VLAN no basta por sí sola para la independencia del SIS? Rúbrica: 3 = un controlador, unos sensores o una vía de gestión compartidos todavía pueden acoplarlos; 2 = una razón; 1 = vago; 0 = afirma que la VLAN basta.
- **EX024 — Evidencia.** Proponga una vía de evidencia de solo lectura para «el HMI puede escribir el registro 40050». Rúbrica: 3 = exportación de configuración o captura de puerto espejo que muestre la capacidad de escritura / el intento, sin escritura en servicio; 2 = parcial; 1 = escritura en servicio; 0 = nada.

### Síntesis del capítulo

Mantenga la lógica de seguridad funcional independiente en hardware y conductos; recoja evidencia sin convertirse en un actuador.

### Siga estudiando — capítulo 08 de 50

[← Capítulo 07 (borrador)](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 (borrador) →](#ch-09)

<a id="ch-09"></a>

## Capítulo 9 — Programación II

### Resultados de aprendizaje

Usted podrá (1) diseñar un esquema para hallazgos de TO que prohíba las recetas de explotación; (2) implementar actualizaciones idempotentes indexadas por activo y debilidad; (3) aplicar pruebas basadas en propiedades a las reglas de zona.

### 9.1 Esquema sin cargas útiles

Guarde título, activo, zona, clase de debilidad, hash de la evidencia, límite de la consecuencia, capas de protección intactas y estado. Rechace los campos llamados payload, shell o exploit. La evidencia vive en un almacén sellado; el ticket guarda el hash. El esquema de Lena rechaza un registro de plano si aparece un campo prohibido, en lugar de eliminarlo en silencio, para que quien lo envió aprenda a no hacerlo. Los límites de la consecuencia y las capas de protección intactas son campos separados, lo que permite al ingeniero de seguridad funcional filtrar los hallazgos que afectan al SIS-B. El hash de la evidencia vincula cada ticket con su prueba sellada sin copiar nada de ella en el sistema de tickets.

### 9.2 Inserciones o actualizaciones idempotentes

Dos escáneres que informan de la misma escritura Modbus abierta en el PLC-A deben convertirse en un solo hallazgo. Huella = (activo, clase de debilidad, registro o camino). Los reintentos y las reimportaciones dejan una sola fila. Lena lo prueba importando dos veces la misma salida de un escáner e importando los informes de dos escáneres sobre el mismo problema; ambos casos deben dejar exactamente un hallazgo. La huella usa el registro o el camino, no la redacción propia del escáner, porque dos herramientas describen la misma debilidad de forma distinta. Cuando las huellas coinciden para problemas realmente distintos, una persona los separa y registra por qué.

### 9.3 Pruebas basadas en propiedades para zonas

Enuncie: «para todo equipo de la zona de oficina y todo registro del SIS, permit es falso». Genere equipos sintéticos y compruébelo. Las pruebas basadas en propiedades detectan el error en el que se añadió una nueva subred de oficina al inventario pero no al lado de denegación de la lista de permitidos.

> **Caso sintético — Ashford Batch Plant.** Tras el hallazgo FW-12, Lena añadió una prueba basada en propiedades: ningún equipo de L4 puede tener un camino de permiso hacia L1-SIS. La integración continua la ejecuta con cada cambio en la exportación del cortafuegos.

La prueba se ejecuta sobre equipos sintéticos tomados del inventario.

### 9.4 Errores y límites

Los esquemas derivan; póngales versión. Los generadores de propiedades que nunca emiten la nueva subred pasan por alto el error que debían detectar; incluya como entradas las diferencias del inventario. Lena alimenta la prueba basada en propiedades con la última diferencia del inventario, de modo que cada subred nueva se prueba en la siguiente ejecución. El esquema tiene un campo de versión, y los registros antiguos se migran con un script registrado en lugar de editarse a mano. Cuando se modifica una prueba, comprueba que siga fallando con el error original, ya que una propiedad que ya no puede fallar no protege nada.

### Nota práctica

Cuando alguien pida un equipo de excepción «solo por esta vez», exija en el esquema un objeto de excepción con duración limitada, fecha de caducidad y responsable. Las excepciones sin caducidad se convierten en conductos permanentes.

### 9.1b Evolución del esquema sin tiempo de parada

Cuando el esquema de hallazgos incorpora un campo obligatorio, despliegue un cambio en dos fases: primero acepte y persista el campo como opcional mientras rellena los registros existentes; después cambie el validador a obligatorio. Las operaciones a medio camino no deben romperse porque un cliente móvil vaya una versión por detrás. Publique la versión del esquema en las respuestas de la API para que los clientes puedan negarse a escribir cuando sean incompatibles. Las importaciones masivas desde escáneres deben pasar por la misma ruta de validación que las creaciones interactivas, incluidas las comprobaciones de campos prohibidos, o las cargas útiles se colarán por la puerta lateral de confianza de la importación.

### Ejercicios — capítulo 9

- **EX025 — Rechazo.** Escriba una regla de validación que rechace los campos con aspecto de carga útil. Rúbrica: 3 = regla + ejemplo que falla; 2 = regla; 1 = idea; 0 = nada.
- **EX026 — Huella.** ¿Por qué se fusionan dos informes sobre el registro 40050 del PLC-A? Rúbrica: 3 = misma huella; 2 = «mismo hallazgo»; 1 = vago; 0 = incorrecto.
- **EX027 — Propiedad.** Enuncie una propiedad tras añadir una zona DMZ. Rúbrica: 3 = p. ej., L4 alcanza L2 solo a través de L3.5; 2 = informal; 1 = incorrecta; 0 = nada.

### Síntesis del capítulo

Los esquemas, la idempotencia y las propiedades mantienen aburridas las herramientas de seguridad de TO, en el buen sentido.

### Siga estudiando — capítulo 09 de 50

[← Capítulo 08 (borrador)](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 (borrador) →](#ch-10)

<a id="ch-10"></a>

## Capítulo 10 — Ética y seguridad en ingeniería

### Resultados de aprendizaje

Usted podrá (1) rechazar el acceso no autorizado a plantas y las solicitudes de doble uso; (2) aplicar condiciones de parada que protejan la seguridad del proceso; (3) documentar el consentimiento para que una revisión pueda reconstruirlo.

### 10.1 La autorización no es entusiasmo

Un jefe de planta que dice «adelante» en un pasillo no es una autorización escrita. El trabajo en TO necesita un alcance firmado que nombre las unidades, los métodos, las ventanas, las condiciones de parada y un contacto de seguridad de procesos capaz de detener la planta. Sin ese documento, el ingeniero se detiene. NIST SP 800-82 e ISA/IEC 62443 presuponen una actividad autorizada y planificada, no una improvisación ingeniosa. Lena guarda una copia del alcance firmado con cada paquete de trabajo y la revisa antes de cada sesión. Si el alcance no cubre un paso previsto, se detiene y pide una modificación en lugar de interpretarlo con generosidad. El número de teléfono del contacto de seguridad de procesos figura en el propio permiso.

### 10.2 Doble uso

Este programa enseña zonificación, monitorización, medición e informes. No enseña desarrollo de exploits contra PLC, pilas de protocolos convertidas en armas ni formas de eludir los sistemas de seguridad funcional. Cuando un colega pide «solo la prueba de concepto contra la marca X», la respuesta es la descripción del hallazgo y el canal de divulgación del proveedor, no un ataque operativo. Las negativas de Lena son corteses y concretas, y señalan lo que puede ofrecer a cambio: un hallazgo con consecuencias acotadas, una referencia al proceso de divulgación del proveedor y un cambio de diseño que elimine la exposición. El registro de cada solicitud y de cada negativa se guarda con las notas del proyecto.

### 10.3 Condiciones de parada que protegen el proceso

Deténgase si: salta una alarma de proceso inesperada; la latencia o el tiempo de ciclo superan el presupuesto; un sistema de seguridad funcional indica una falla; el contacto de seguridad de procesos dice que se pare. Los bloqueos estrictos por software ayudan, pero las personas siempre tienen la última palabra. Nunca desactive una función de seguridad para «hacer que la prueba funcione».

> **Caso sintético — Ashford Batch Plant.** Durante una prueba en banco del monitor serie, el tiempo de ciclo subió por encima de 50 ms. Lena se detuvo, retiró el dispositivo y repitió la prueba en una línea troncal de repuesto antes de reservar ninguna ventana en la planta.

Estas condiciones están impresas en el permiso.

### 10.4 Errores y límites

La ética es una restricción sobre cada capítulo posterior. Los textos legales aquí son orientación, no asesoramiento. Las plantas en servicio nunca son objetivos de los laboratorios del curso. Todos los capítulos posteriores dan por supuesto este límite. El trabajo de Lena en ABP se realiza bajo un alcance firmado, con condiciones de parada nombradas y un contacto de seguridad de procesos; nada en el curso se dirige nunca contra una planta en funcionamiento. Cuando una pregunta toca el derecho, como la protección de datos o los contratos con proveedores, consulta al asesor jurídico del sitio en lugar de basarse en los apuntes del curso, y registra el consejo recibido.

### Nota práctica

Imprima las condiciones de parada en el permiso de trabajo colgado junto al panel. Con ruido y bajo presión de tiempo, la gente recuerda lo que puede ver. Una condición de parada enterrada en la página 12 de un PDF es una condición de parada que se pasará por alto.


### 10.5 Ejemplo resuelto: un permiso que dice que no (ABP sintética)

Un contratista pide ejecutar un escaneo Modbus activo del PLC-A durante un lote «para terminar antes el inventario». La revisión del permiso que hace Lena aplica tres pruebas: si la autorización escrita del propietario es específica para este equipo y esta técnica (no lo es); si existe una condición de parada que un operador pueda activar (no se escribió ninguna); y si hay una alternativa pasiva (una captura por puerto espejo más la exportación del proyecto de ingeniería da el mismo inventario). Rechaza el escaneo activo, registra el motivo y emite un permiso solo para captura pasiva, con el jefe de turno nombrado como la persona que puede detener el trabajo. NIST SP 800-82r3 advierte que el escaneo activo puede perturbar los dispositivos de TO, que es la razón de ingeniería que respalda la razón ética.

### Ejercicios — capítulo 10

- **EX028 — Negativa.** Negativa en dos frases a una solicitud de un exploit operativo contra un PLC para un trabajo evaluado. Rúbrica: 3 = se niega, ofrece una alternativa permitida, menciona la seguridad; 2 = solo se niega; 1 = vago; 0 = proporciona el exploit.
- **EX029 — Parada.** Enumere cuatro condiciones de parada para una ventana en ABP. Rúbrica: 3 = cuatro pertinentes para el proceso; 2 = tres; 1 = una; 0 = nada.
- **EX030 — Campos.** Seis campos que debe contener un permiso de trabajo de TO firmado. Rúbrica: 3 = unidades, métodos, ventana, límites de tasa/impacto, contactos, parada/reanudación; 2 = cuatro; 1 = dos; 0 = nada.

### Síntesis del capítulo

El permiso escrito, las condiciones de parada que anteponen el proceso y el hábito de negarse son ingeniería de seguridad.

### Siga estudiando — capítulo 10 de 50

[← Capítulo 09 (borrador)](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 (borrador) →](#ch-11)

<a id="ch-11"></a>

## Capítulo 11 — Redes y protocolos

### Resultados de aprendizaje

Usted podrá (1) describir lo que un observador autorizado puede aprender de los protocolos de TO sin atacarlos; (2) definir el alcance por códigos de función y registros; (3) tratar los rechazos del protocolo como controles que funcionan.

### 11.1 Puntos de observación

Los monitores serie ven Modbus RTU en el cable; los puertos SPAN ven EtherNet/IP o Modbus TCP; los registros de aplicación ven las acciones del HMI. Una evaluación que solo dispone de capturas de pantalla del HMI no debe afirmar visibilidad del bus de campo. Indique el punto de observación en la sección de método de cada hallazgo. Lena escribe el punto de observación en el campo de método de cada hallazgo, para que los lectores sepan qué podía verse y qué no. En ABP, un monitor serie en la línea troncal RS-485 hacia el PLC-A da visibilidad del bus de campo, mientras que los registros propios del HMI muestran las acciones del operador. Los hallazgos basados solo en una de estas fuentes lo dicen, porque cada una puede pasar por alto lo que la otra ve.

### 11.2 Los puertos no son semántica

El TCP 502 suele significar Modbus TCP, pero el alcance relevante es qué códigos de función y qué rangos de registros puede usar cada estación. Un puerto 502 abierto es una información incompleta sin el estado de la lista de permitidos y las estaciones observadas. La función de permiso del capítulo 4 es la abstracción adecuada. Los hallazgos de Lena sobre puertos abiertos siempre añaden qué estaciones se vieron usando qué códigos de función, para que el lector sepa si el puerto importa. En ABP, la lista de permitidos establece que HMI-1 solo puede escribir los registros 40001 a 40010 y que el historiador solo puede leer. Un escaneo de puertos por sí solo no mostraría nada de eso.

### 11.3 Los rechazos son cobertura

Un cortafuegos que bloquea el tráfico de oficina a SCADA, o un monitor que descarta la función 16 de HIST-1, es evidencia de que un control funcionó frente a esa sonda. Los tableros de cobertura deben contar las comprobaciones planificadas que fueron rechazadas como comprobaciones completadas, no como intentos fallidos de entrar.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Salida esperada:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

> **Caso sintético — Ashford Batch Plant.** El tablero de cobertura del CNHP incluye «HIST-1 no puede escribir» como comprobación planificada. El BLOCK del laboratorio sobre la función 16 es un resultado verde para esa comprobación, no una prueba fallida en rojo.

El tablero de Lena muestra cada comprobación planificada con su resultado esperado.

### 11.4 Errores y límites

Los banners mienten; confirme con evidencia de nivel de aplicación o de tramas decodificadas. Los entornos del curso nunca escanean plantas en servicio. Lena trata el banner de un dispositivo como un indicio y confirma el producto a partir de la exportación del proyecto de ingeniería o de tramas decodificadas antes de registrarlo en el inventario. Los banners pueden quedar desactualizados tras una actualización de firmware o ser deliberadamente genéricos. El paso de confirmación también evita un error común en el que el banner de una pasarela se confunde con el del controlador que hay detrás. En el curso, todas estas comprobaciones se hacen sobre datos capturados o sintéticos, nunca sobre la red de una planta en servicio.

### Nota práctica

Mantenga un inventario de protocolos de una página: línea troncal, velocidad en baudios, estaciones, códigos de función en uso, responsable de la lista de permitidos. Actualícelo cuando un proveedor añada una estación. La mayor parte del tráfico misterioso es un portátil de ingeniería no documentado.

### 11.1b Familias de protocolos en el permiso de trabajo

Los permisos de trabajo deben nombrar de forma explícita las familias de protocolos: Modbus TCP con los códigos de función 3/4/6 sobre los registros 40001-40010 es más claro que «puerto 502». Si los códigos de escritura están prohibidos desde las estaciones de evaluación, dígalo. Si solo se autorizan derivaciones de solo escucha, dígalo. La ambigüedad en este punto se convierte en una discusión durante la ventana, cuando alguien quiere probar una función de diagnóstico solo para ver qué pasa. Cuando el permiso nombra códigos de función, la lista de permitidos del monitor para esa ventana debe nombrar los mismos códigos, para que el permiso y la evidencia puedan compararse línea por línea.

En ABP, el permiso de Lena para la verificación serie indica solo escucha en la línea troncal RS-485 hacia el PLC-A, nombra las escrituras permitidas de HMI-1 y prohíbe los códigos de función de diagnóstico desde el portátil de evaluación. Durante la ventana W-17 se rechazó por exactamente esta razón la solicitud de un proveedor de probar un diagnóstico, que se evaluó más tarde con su propio permiso.

### Ejercicios — capítulo 11

- **EX031 — Punto de observación.** Asocie tres tipos de evidencia con el punto de observación mínimo. Rúbrica: 3 = asociación correcta (p. ej., errores CRC de RTU con serie; FC de Modbus TCP con decodificación IP; atribución de un cambio de punto de consigna con registro del HMI o de la aplicación); 2 = dos; 1 = uno; 0 = nada.
- **EX032 — Alcance.** Reescriba «probar Modbus en el PLC-A» como una línea acotada de una ficha de método. Rúbrica: 3 = códigos, registros, estaciones, solo lectura, ventana; 2 = parcial; 1 = solo el puerto; 0 = nada.
- **EX033 — Laboratorio.** ¿Por qué se bloquea HMI-1 fc=6 reg=40050 mientras que 40003 pasa? Rúbrica: 3 = register-out-of-range frente a dentro de WRITE_REGS; 2 = un lado; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

Acote los protocolos de TO por su semántica (códigos, registros, estaciones); celebre los rechazos que coinciden con el plan.

### Siga estudiando — capítulo 11 de 50

[← Capítulo 10 (borrador)](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 (borrador) →](#ch-12)

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operativos

### Resultados de aprendizaje

Usted podrá (1) bastionar los HMI y las estaciones de ingeniería sin romper el control; (2) recoger evidencia del sistema operativo con mínimo privilegio; (3) planificar la aplicación de parches dentro de las ventanas de mantenimiento.

### 12.1 Las estaciones de trabajo forman parte del sistema de control

Los HMI y las estaciones de ingeniería suelen ejecutar sistemas operativos de propósito general con décadas de software heredado. Tratarlos como simples PC es la forma en que el malware entra en L2. Las líneas base de bastionado (listas de aplicaciones permitidas, eliminación del administrador local, control de USB) deben probarse frente a la matriz de soporte del proveedor del HMI: un cambio de bastionado no soportado que deja en blanco una pantalla durante un lote es un incidente de disponibilidad. En ABP, Lena prueba cada cambio de bastionado en un HMI de banco con la misma versión del proveedor antes de que llegue a la sala de control, y registra qué elementos admite el proveedor.

### 12.2 Mínimo privilegio para los ingenieros

Cuentas nominales, derechos de administrador con duración limitada, elevaciones registradas. Las contraseñas compartidas de ingeniería siguen siendo comunes y siguen siendo un error: destruyen la atribución y perduran después de que los contratistas se marchan. Los hallazgos sobre contraseñas compartidas son hallazgos de configuración, no invitaciones a descifrar hashes. En ABP, la contraseña compartida de ingeniería de eng-WS-1 se sustituye por cuentas nominales, y cada elevación se registra con la persona y el motivo. Los contratistas reciben cuentas que caducan al final de su orden de trabajo. Lena informa de las contraseñas compartidas a partir de la configuración y de la lista de cuentas, nunca probándolas.

### 12.3 Ventanas de parches

Los parches de TO se aplican en ventanas de mantenimiento, no el martes de parches. Encaje los trabajos según su riesgo en las horas disponibles; aplace lo que no quepa en lugar de invadir la producción.

```python
"""Lab: fit patch jobs into plant maintenance windows (synthetic, greedy by risk)."""
windows = [("W1 Sat 02-06", 4.0), ("W2 Sun 02-04", 2.0)]
jobs = [("HMI OS update", 1.5, 8), ("historian DB patch", 2.5, 5), ("PLC-A firmware", 3.0, 9),
        ("eng-WS AV update", 0.5, 3), ("switch firmware", 1.0, 6)]   # name, hours, risk score
left = {w: h for w, h in windows}; plan = {w: [] for w, _ in windows}; deferred = []
for name, h, r in sorted(jobs, key=lambda j: -j[2]):
    for w, _ in windows:
        if left[w] >= h:
            left[w] -= h; plan[w].append(name); break
    else:
        deferred.append(name)
for w, _ in windows:
    print(w, plan[w], f"spare={left[w]:.1f}h")
print("deferred:", deferred)
```

Salida esperada:

```text
W1 Sat 02-06 ['PLC-A firmware', 'switch firmware'] spare=0.0h
W2 Sun 02-04 ['HMI OS update', 'eng-WS AV update'] spare=0.0h
deferred: ['historian DB patch']
```

> **Caso sintético — Ashford Batch Plant.** El laboratorio de parches aplazó el parche de la base de datos del historiador porque W1 y W2 estaban llenas con trabajos de mayor riesgo en el PLC y el HMI. Lena programó una ventana dedicada para el mes siguiente en lugar de meterlo con calzador el domingo por la mañana.

Cada trabajo aplazado conserva su ticket y su fecha. Los aplazamientos se revisan cada mes.

### 12.4 Errores y límites

No desactive el antivirus ni las listas de permitidos para contentar al proveedor sin una excepción escrita y una monitorización compensatoria. Las plantas desconectadas siguen necesitando control de soportes. Cuando el proveedor del HMI pide una excepción, Lena registra qué protección se relaja, en qué equipo, durante cuánto tiempo y qué monitorización la sustituye. La excepción tiene un responsable y una fecha de caducidad. Los equipos desconectados siguen recibiendo soportes a través de una estación de análisis y una transferencia registrada, ya que las memorias USB son la vía habitual de entrada a una red aislada.

### Nota práctica

Cada parche aplazado recibe un ticket con su riesgo residual y una fecha. «Aplazado sin fecha» es la forma en que sobreviven imágenes de sistema operativo de HMI con una década de antigüedad. Revise la lista de aplazados en la misma reunión que planifica la siguiente ventana.

### 12.1b Imágenes y análisis fuera de línea

Las imágenes de disco completo de los HMI tienen un gran impacto: dejan los sistemas fuera de servicio, pueden contener recetas propietarias e invitan a explorar fuera del alcance. Prefiera las lecturas en vivo con mínimo privilegio y las exportaciones de configuración. Si una imagen es realmente necesaria, el permiso de trabajo debe nombrar la cadena de custodia, el cifrado en reposo, quién puede montarla y una fecha límite de destrucción; y los laboratorios del curso siguen sin practicar la obtención de imágenes de equipos reales. Las plantas desconectadas siguen necesitando control de soportes; un aislamiento físico que oculta USB y módems celulares no es un aislamiento físico.

Lena nunca ha necesitado una imagen completa en ABP.

### Ejercicios — capítulo 12

- **EX034 — Cuenta.** Especifique un patrón de mínimo privilegio para el acceso de ingeniería al PLC. Rúbrica: 3 = nominal, de duración limitada, registrado, doble control para la descarga de lógica; 2 = tres de cuatro; 1 = administrador compartido; 0 = nada.
- **EX035 — Laboratorio.** ¿Qué trabajo se aplazó y por qué? Rúbrica: 3 = el parche de la base de datos del historiador; ventanas llenas tras los trabajos de mayor riesgo; 2 = solo el nombre; 1 = vago; 0 = incorrecto.
- **EX036 — Excepción.** Escriba en una línea una excepción de USB para la puesta en marcha de un proveedor, con control compensatorio. Rúbrica: 3 = duración limitada, soportes analizados, equipo monitorizado; 2 = parcial; 1 = USB abierto; 0 = nada.

### Síntesis del capítulo

Bastione y parchee las estaciones de trabajo como si fueran controladores, porque para el malware son la puerta.

### Siga estudiando — capítulo 12 de 50

[← Capítulo 11 (borrador)](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 (borrador) →](#ch-13)

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de datos

### Resultados de aprendizaje

Usted podrá (1) proteger los datos del historiador y de las recetas sin bloquear las operaciones; (2) acotar la evaluación de bases de datos sin extraer lotes propietarios; (3) diseñar conjuntos de datos sintéticos para los laboratorios.

### 13.1 Los historiadores son las joyas de la corona

Los historiadores guardan valores de proceso que revelan ritmos de producción, recetas y a veces datos de calidad. Las escrituras no autorizadas pueden corromper los registros de lote; las lecturas no autorizadas pueden filtrar datos comerciales. Colóquelos en su zona (L3), permita las vías de lectura a través de réplicas controladas y nunca exponga SQL a L4. En ABP, HIST-1 está en L3 y los usuarios de oficina leen de la réplica de la DMZ, nunca del historiador de la zona de control. El acceso de escritura a HIST-1 se limita al servicio de recogida, y cada cambio en los registros de lote queda registrado. Lena comprueba ambas vías en cada revisión de conductos.

### 13.2 Minimizar las extracciones

El trabajo autorizado con bases de datos usa copias sintéticas o enmascaradas. Exportar la genealogía real de los lotes al portátil de un estudiante es un incidente de confidencialidad. El permiso de trabajo debe indicar: ningún volcado completo, listas de columnas permitidas, límites de filas, fecha límite de destrucción. El permiso de trabajo de Lena para el acceso al historiador enumera en lenguaje llano las columnas permitidas y el límite de filas. Las extracciones van a un equipo de análisis aprobado, no a un portátil personal, y su borrado queda registrado. Una solicitud de más datos de los que la pregunta necesita se acota antes de ejecutar cualquier consulta.

### 13.3 Datos de proceso sintéticos

Genere niveles de tanque y puntos de consigna deterministas con semillas fijas para que los laboratorios sean reproducibles. Los laboratorios de CUSUM y de PI lo hacen; nunca copie un historiador de producción en el repositorio del curso.

> **Caso sintético — Ashford Batch Plant.** Operaciones proporcionó a Lena una semana de valores sintéticos de T-1/T-2/R-101 a 1 Hz para los ensayos de detectores: sin números de pedido de clientes ni nombres de operadores.

La semana de valores sintéticos de T-1, T-2 y R-101 de ABP con resolución de un hercio se generó de este modo, y su semilla está registrada junto con el conjunto de datos. Lena vuelve a ejecutar el generador para confirmar que el archivo coincide antes de cada ensayo.

### 13.4 Errores y límites

Un enmascaramiento que deja recetas raras y únicas todavía puede identificar series de producción. Para la enseñanza, prefiera la generación sintética. Una receta que ABP solo produce dos veces al año puede identificar el lote aunque se hayan quitado los nombres. Por eso Lena usa datos sintéticos para la enseñanza y conserva datos reales enmascarados solo para las investigaciones que realmente los necesitan, con el acceso limitado a los investigadores. Las decisiones de enmascaramiento se registran y se revisan con el equipo de calidad. Los casos de lotes raros se enumeran en la solicitud de extracción. El equipo de calidad revisa esos casos antes de la entrega.

### Nota práctica

Dibuje el flujo de datos: del sensor al PLC, al historiador, a la réplica y a los informes de L4. Cada flecha necesita un responsable y un protocolo. Las flechas misteriosas son donde viven la exfiltración y la exposición accidental.

### 13.1b Controles por fila y por columna

Los historiadores y almacenes de datos modernos ofrecen políticas por fila y por columna. Las preguntas de evaluación pasan a ser: ¿ve el rol R la columna C? ¿Se aplica el filtro de filas F? Pruebe con el propio rol. Documente la versión del motor de políticas; «ejecutamos SELECT * con un rol de administrador» demuestra poco sobre la exposición de un analista. Registre cada resultado de rol y columna con la cuenta utilizada y la fecha, para que la siguiente revisión repita exactamente las mismas comprobaciones.

Lena prueba la réplica de ABP con una cuenta de analista antes de cada revisión. Los resultados van a las notas de la revisión.

### 13.5 Ejemplo resuelto: una extracción minimizada del historiador (ABP sintética)

Los ingenieros de calidad piden «todos los datos de R-101 del año pasado». La extracción de Lena contiene solo las cuatro etiquetas que necesita la investigación de la desviación (temperatura del reactor, temperatura de la camisa, velocidad del agitador, posición de la válvula de alimentación) con resolución de un minuto, para los 11 lotes en revisión, con los identificadores de lote sustituidos por códigos de estudio y la columna del nombre del operador eliminada. La extracción es una lectura de la réplica de la DMZ, nunca del historiador de la zona de control, y el texto de la consulta y un hash SHA-256 del archivo de salida van al ticket de la solicitud, para que las mismas filas puedan reproducirse o borrarse más adelante. El resultado son 11 × 4 etiquetas × unos 480 minutos ≈ 21.000 filas, en lugar de decenas de millones.

### Ejercicios — capítulo 13

- **EX037 — Cláusula del permiso.** Redacte una cláusula de tratamiento de datos para una evaluación del historiador. Rúbrica: 3 = solo réplica, lista de columnas permitidas, límite de filas, fecha de destrucción, sin volcados; 2 = tres; 1 = una; 0 = nada.
- **EX038 — Autorización.** ¿Cómo comprobaría si el rol analyst puede escribir anotaciones en el historiador sin técnicas de inyección? Rúbrica: 3 = conectarse como analyst, intentar la escritura, registrar si se concede o se deniega; 2 = idea; 1 = inyección; 0 = nada.
- **EX039 — Sintético.** Tres campos seguros para una tabla sintética de tanques y dos que no deben aparecer. Rúbrica: 3 = p. ej., `tag`, `value`, `timestamp` frente a `operator_name`, `customer_order`; 2 = parcial; 1 = débil; 0 = nada.

### Síntesis del capítulo

Minimice los datos, pruebe los roles, sintetice para enseñar. El historiador no es una vitrina de trofeos.

### Siga estudiando — capítulo 13 de 50

[← Capítulo 12 (borrador)](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 (borrador) →](#ch-14)

<a id="ch-14"></a>

## Capítulo 14 — Ingeniería de software

### Resultados de aprendizaje

Usted podrá (1) poner las herramientas de seguridad de TO bajo control de versiones con revisión; (2) controlar los cambios que amplían conductos; (3) mantener la integración continua solo con datos de prueba sintéticos.

### 14.1 Las herramientas son productos

Los compiladores de listas de permitidos, los comprobadores de alcanzabilidad y las configuraciones de detectores son software. Necesitan repositorios, revisiones, etiquetas y registros de cambios. Un permiso de trabajo que cita la exportación del cortafuegos sin un hash está incompleto. Lena mantiene las herramientas del CNHP en un único repositorio con versiones etiquetadas y un registro de cambios, y cada permiso de trabajo cita la etiqueta y el hash de las exportaciones en que se basa. Cuando un revisor pregunta qué versión del comprobador de alcanzabilidad produjo un resultado, la respuesta es una etiqueta, no un recuerdo.

### 14.2 Controlar las ampliaciones

Las fusiones que añaden un conducto, abren un código de función o eliminan una denegación requieren un segundo revisor y un ticket de autorización vinculado. Los cambios que restringen pueden ser más ligeros. Codifíquelo en CODEOWNERS sobre las rutas de las políticas. Lena asigna como responsables de código a personas de ingeniería de control para los archivos de la lista de permitidos y de conductos, de modo que los cambios que amplían no pueden fusionarse sin ellas. Los cambios que restringen siguen necesitando un revisor. La regla se aplica mediante la configuración de responsables de código en las rutas de las políticas, así que un revisor ocupado no puede saltársela. Un cambio que amplía también necesita un ticket de autorización vinculado que nombre quién aprobó el nuevo camino y por qué.

### 14.3 Datos de prueba de la integración continua

La integración continua ejecuta los laboratorios y las pruebas unitarias con datos sintéticos. Nunca apunte la integración continua a una VPN de planta. Los datos semilla viven en el repositorio; las credenciales de planta viven en una bóveda y nunca en los registros de la integración continua.

> **Caso sintético — Ashford Batch Plant.** Una solicitud de incorporación de cambios añadió una regla temporal de L4 a L2 para la visita de un proveedor. La comprobación de alcanzabilidad de la integración continua falló porque L1-SIS pasaba a ser alcanzable; la solicitud quedó bloqueada hasta que la regla se reescribió a través de la DMZ.

La canalización de Lena carga datos de prueba sintéticos para las zonas y la lista de permitidos de ABP.

### 14.4 Errores y límites

Las etiquetas pueden desviarse de lo que ejecutan los operadores; registre el hash en ejecución en el registro del encargo al inicio de la ventana. El registro del encargo de Lena anota el hash del binario del monitor y de la lista de permitidos que realmente se ejecutan al comienzo de cada ventana. Si difiere de la versión etiquetada, la ventana espera hasta que se explique la diferencia. Esa comprobación encontró un monitor de banco que seguía ejecutando una versión candidata después de una corrección urgente. Los hashes en ejecución van al registro de la ventana. Una discrepancia se trata como una parada, no como un aviso.

### Nota práctica

Los repositorios de políticas usan la misma cultura de doble aprobación que las descargas de lógica al PLC. Si descargar el ladder al PLC-A necesita dos personas, publicar un conducto que alcance el PLC-A también debería necesitarlas.

### 14.1b Trenes de versiones frente a correcciones urgentes

Las mejoras normales viajan en un tren de versiones con los laboratorios I/II. Las correcciones urgentes de seguridad pueden saltarse funcionalidades, pero no la verificación: un paquete mínimo de regresión de fallo cerrado es obligatorio. Etiquete claramente las correcciones urgentes para que una ventana pueda fijar, con conocimiento de causa, la compilación del tren o el SHA de la corrección. Las versiones fijadas figuran en la lista de comprobación de arranque junto al hash del permiso de trabajo; si la versión fijada y el binario en ejecución no coinciden, la ventana no comienza.

Las correcciones urgentes de ABP llevan su propia etiqueta y el resultado del paquete de regresión en la nota de versión, para que el responsable de una ventana pueda ver exactamente qué se verificó.

### 14.5 Ejemplo resuelto: revisar un cambio en permit() (ABP sintética)

Una solicitud de incorporación de cambios amplía el rango escribible del HMI en el PLC-A de 40001–40010 a 40001–40012 para un nuevo punto de consigna del agitador. La lista de revisión de Lena: el identificador del requisito que justifica 40011–40012; nuevos vectores de conformidad para 40012 (pasa) y 40013 (se bloquea); la denegación predeterminada para orígenes desconocidos sin cambios; un incremento de versión y una línea en el registro de cambios; y un segundo revisor de ingeniería de control que confirme el significado de los registros en el proyecto del PLC. La fusión espera a la ejecución en banco de los vectores contra la compilación real del cortafuegos. La disciplina de ingeniería de software aquí no es ceremonia: un error de un carácter en un rango dejaría al HMI escribir un registro que el diseño del proceso nunca previó.

### Ejercicios — capítulo 14

- **EX040 — Fijar.** Escriba la frase de método que fija la lista de permitidos para una ventana. Rúbrica: 3 = nombre, hash/etiqueta, fecha de carga; 2 = nombre + etiqueta; 1 = nombre; 0 = nada.
- **EX041 — Control.** Política de fusión en una frase para los archivos de conductos. Rúbrica: 3 = segundo revisor + AUTH para ampliar; 2 = solo el revisor; 1 = vago; 0 = nada.
- **EX042 — Integración continua.** ¿Por qué la integración continua nunca debe usar credenciales de la VPN de planta? Rúbrica: 3 = automatización no autorizada, filtración de secretos, falta de determinismo; 2 = una razón sólida; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

Trate el software de seguridad de TO como software de producción: versiones, controles de revisión, integración continua sintética.

### Siga estudiando — capítulo 14 de 50

[← Capítulo 13 (borrador)](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 (borrador) →](#ch-15)

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de seguridad

### Resultados de aprendizaje

Usted podrá (1) relacionar la tríada CIA y la seguridad funcional con las preguntas de evaluación de TO; (2) distinguir vulnerabilidad, exposición y riesgo de proceso; (3) rechazar las puntuaciones de seguridad vacías.

### 15.1 CIA más seguridad funcional

Confidencialidad: ¿quién puede leer recetas o tendencias? Integridad: ¿quién puede cambiar puntos de consigna o lógica? Disponibilidad: ¿qué detiene el lote? Seguridad funcional: ¿qué capas de protección siguen siendo independientes? Cada hallazgo debe decir qué propiedades se ven afectadas y si una función de seguridad entra en el alcance. Lena añade a cada hallazgo del CNHP una línea que nombra las propiedades afectadas e indica si el SIS-B entra en el alcance. En ABP, un hallazgo sobre una escritura sin autenticación en el PLC-A afecta a la integridad y, a través del nivel del tanque, posiblemente a la seguridad funcional; un hallazgo sobre la réplica del historiador afecta a la confidencialidad. Nombrar la propiedad indica a los lectores qué equipo debe responder.

### 15.2 Vulnerabilidad, exposición, riesgo

Una escritura Modbus sin autenticación es una vulnerabilidad. En un PLC alcanzable desde L2 es una exposición. El riesgo de proceso añade la probabilidad y la consecuencia para la planta, lo que necesita el modelo del ingeniero de seguridad funcional, no un relato universal basado solo en CVSS. Los tickets guardan por separado los límites de la consecuencia y las capas de protección; la aceptación del riesgo sigue correspondiendo al propietario de la planta. La plantilla de ticket de Lena tiene campos separados para cada uno, de modo que ninguno se pierde. Lena registra la exposición, como la alcanzabilidad desde L2, por separado de la vulnerabilidad, para poder seguir la corrección de cualquiera de las dos. El jefe de planta firma cualquier aceptación de riesgo residual.

### 15.3 Puntuaciones vacías

Un único «riesgo de TO = 42» oculta si se mantiene la independencia del SIS. Prefiera medidas concretas: hallazgos abiertos de alta consecuencia, conductos hacia el SIS, tasa de falsas alarmas del detector con la tasa base de la planta, antigüedad de los parches aplazados. Si muestra una puntuación, muestre el modelo y las entradas.

> **Caso sintético — Ashford Batch Plant.** Lena dejó de poner una puntuación compuesta en las diapositivas del CNHP. La presentación muestra ahora: ¿SIS alcanzable desde L4? No. Críticos abiertos: 1. Alarmas por operador y hora: 1,05. Parches de alto riesgo aplazados: 0.

Cada medida del CNHP tiene una definición y una fuente, para que pueda volver a calcularse.

### 15.4 Errores y límites

Los fundamentos son vocabulario; no son un análisis de peligros completo. Continúe con el análisis de amenazas y fallos para un estudio estructurado. El vocabulario ayuda a describir los hallazgos de forma coherente, pero no sustituye el análisis de peligros del proceso de la planta. Lena vincula los hallazgos del CNHP al análisis de peligros cuando tocan un peligro, y deja los juicios sobre consecuencias al ingeniero de seguridad de procesos. El análisis de amenazas y fallos, más adelante en el programa, aporta el método estructurado. Cada hallazgo se vincula al peligro pertinente. El ingeniero de seguridad funcional revisa esos vínculos.

### Nota práctica

Cuando alguien pida un tablero tipo semáforo, ofrezca tres luces que signifiquen algo: independencia del SIS intacta (sí/no), hallazgos críticos abiertos (conteo), parches aplazados fuera de plazo (conteo). Rechace una cuarta luz llamada «ciber global».

### 15.1b De la propiedad a la prueba

Si un hallazgo afirma un impacto en la integridad, el plan de validación debe incluir una comprobación de integridad (quién puede seguir escribiendo). Si afirma un impacto en la disponibilidad, la validación incluye un canario o una sonda sintética, no un nuevo ataque. Alinee la propiedad, el hallazgo y el método de nueva prueba en un párrafo del ticket. El resultado de la nueva prueba va al mismo ticket que el hallazgo original, con la fecha y la comprobación utilizada, para que el cierre pueda auditarse más tarde.

En ABP, el hallazgo FW-12 afirmaba una exposición de integridad, así que su nueva prueba comprobó, con el mismo método de alcanzabilidad, que la zona de oficina ya no podía alcanzar SCADA.

### Ejercicios — capítulo 15

- **EX043 — Mapa.** Relacione una escritura de punto de consigna sin autenticación en el PLC-A con C/I/A/seguridad funcional, con una frase para cada una. Rúbrica: 3 = las cuatro acotadas; 2 = tres; 1 = una; 0 = nada.
- **EX044 — Términos.** Distinga vulnerabilidad, exposición y riesgo de proceso para esa escritura. Rúbrica: 3 = división clara; 2 = dos claras; 1 = confuso; 0 = nada.
- **EX045 — Rechazo de la puntuación.** Una parte interesada quiere una puntuación de 0 a 100 de «hackeabilidad». Recházela con alternativas. Rúbrica: 3 = se niega + medidas concretas; 2 = solo se niega; 1 = vago; 0 = inventa la puntuación.

### Síntesis del capítulo

Nombre la propiedad, separe la exposición del riesgo de proceso y prefiera medidas que pueda volver a calcular.

### Siga estudiando — capítulo 15 de 50

[← Capítulo 14 (borrador)](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 (borrador) →](#ch-16)

<a id="ch-16"></a>

## Capítulo 16 — Ingeniería de sistemas

### Resultados de aprendizaje

Usted podrá (1) redactar requisitos de seguridad de TO comprobables; (2) trazar un requisito hasta una regla de conducto y un laboratorio; (3) gestionar las interfaces entre el PLC, el SIS, el historiador y los monitores de seguridad.

### 16.1 Requisitos comprobables

«La planta debe ser segura» no es un requisito. «Ningún equipo fuera de L1/L2 deberá iniciar escrituras en los registros de retención del PLC-A; se verifica mediante análisis de alcanzabilidad y pruebas de la lista de permitidos con datos de prueba sintéticos» sí lo es. Cada requisito necesita un identificador, un enunciado con «deberá», un método de verificación y un responsable. Lena asigna a cada requisito del CNHP un identificador como R-12 y un responsable antes de que empiece cualquier trabajo de diseño. Un requisito sin método de verificación se devuelve a su autor. Lena también comprueba que cada uno pueda probarse con datos de prueba sintéticos, porque un requisito que solo puede verificarse escribiendo en un controlador en servicio no puede aceptarse.

### 16.2 Trazabilidad

Matriz: del requisito al elemento de diseño, al caso de prueba y a la evidencia de planta. Cuando un hallazgo muestra un conducto hacia el SIS, se sabe qué requisito y qué prueba fallaron. Sin la matriz, los análisis posteriores se convierten en búsqueda de culpables. Lena mantiene la matriz como un archivo en el repositorio del CNHP, actualizado en la misma solicitud de incorporación de cambios que la política que describe. Cada fila vincula un requisito como R-12 con la lista de aristas por zonas, la prueba de alcanzabilidad y el hash de la última exportación del cortafuegos. Cuando una prueba falla, la matriz muestra qué requisito está en riesgo y quién es su responsable.

### 16.3 Interfaces

El PLC-A publica valores de proceso; el SIS-B consume sensores dedicados; el historiador consume etiquetas del PLC; el monitor serie consume una derivación de solo escucha. Acuerde las listas de etiquetas y las frecuencias de actualización. Un cambio de interfaz es una solicitud de cambio, no una edición silenciosa durante un lote.

> **Caso sintético — Ashford Batch Plant.** El requisito R-12, «SIS no alcanzable desde L4», se traza hasta la lista de aristas por zonas, lab_reach.py y el hash trimestral de la exportación del cortafuegos en el expediente.

Lena mantiene en el repositorio la lista de etiquetas de cada interfaz, con su responsable y su frecuencia de actualización.

### 16.4 Errores y límites

Las matrices de trazabilidad se pudren si no se actualizan en la misma solicitud de incorporación de cambios que la política. Manténgalas junto al código. La integración continua de Lena hace fallar una solicitud de incorporación de cambios que modifica un archivo de política sin tocar la matriz, lo que mantiene ambos sincronizados. Cada fila lleva además la fecha de su última verificación. Las filas que no se han comprobado en un trimestre se señalan en la reunión de revisión, porque un vínculo antiguo suele estar roto. Los responsables confirman cada fila una vez al año.

### Nota práctica

Ponga los identificadores de los requisitos en los nombres de los objetos del cortafuegos y en los comentarios de configuración de los detectores (req=R-12). Poder buscarlos durante un incidente vale más que una diapositiva que alguna vez relacionó requisitos con módulos.

### 16.1b Glosario y retirada

Mantenga un glosario de una página: permiso de trabajo, ConduitSet, lista de permitidos, técnica planificada, evidencia sellada. Las partes interesadas usan mal «cobertura» y «riesgo» constantemente; el glosario es un artefacto de requisitos. La trazabilidad también cubre la retirada: cuando se retira un requisito, márquelo como sustituido con una referencia en lugar de borrar la fila. Los hallazgos históricos siguen citando identificadores antiguos. Los acuerdos de nivel de servicio internos entre servicios importan: el monitor puede necesitar que el almacén de hallazgos acepte un evento en N segundos durante una condición de parada. Escríbalo como requisito con una prueba de carga sintética. Sin él, los avisos de condición de parada llegan después de que la persona ya haya llamado a seguridad de procesos.

### Ejercicios — capítulo 16

- **EX046 — Deberá.** Reescriba «impedir que la oficina toque SCADA» como dos requisitos con «deberá». Rúbrica: 3 = dos enunciados comprobables con método de verificación; 2 = uno bueno; 1 = sigue siendo vago; 0 = nada.
- **EX047 — Traza.** Para R-12, nombre el artefacto y la señal de la prueba que falla. Rúbrica: 3 = aristas por zonas + L1-SIS en reach(L4); 2 = uno; 1 = vago; 0 = nada.
- **EX048 — Interfaz.** Enumere tres campos de un contrato de interfaz de lista de etiquetas. Rúbrica: 3 = nombre de la etiqueta, tipo/unidades de ingeniería, frecuencia de actualización (o equivalente); 2 = dos; 1 = uno; 0 = nada.

### Síntesis del capítulo

Requisitos que se pueden probar, vínculos que se pueden seguir, interfaces con versión.

### Siga estudiando — capítulo 16 de 50

[← Capítulo 15 (borrador)](#ch-15) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 17 (borrador) →](#ch-17)

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de control y realimentación

### Resultados de aprendizaje

Usted podrá (1) ajustar un lazo PI sencillo y ver cómo la acción integral elimina el error estacionario; (2) situar sensores de seguridad en el lazo de control sin desestabilizarlo; (3) evitar las tormentas de alertas que ocultan las alarmas de proceso.

### 17.1 El PI en una página

Un controlador proporcional deja un error estacionario; la acción integral acumula el error y lo elimina. El laboratorio cambia en escalón el punto de consigna de nivel de 50 a 60 y compara solo kp con kp+ki. Los ingenieros de seguridad necesitan esta soltura para no proponer detectores que luchen contra el controlador.

```python
# Lab 17 - discrete PI level control vs. setpoint step (synthetic)
def sim(kp, ki, steps=200, sp=60.0):
    level, integ, err_hist = 50.0, 0.0, []
    for t in range(steps):
        err = sp - level
        integ += err * 0.1
        u = max(0.0, min(3.0, kp*err + ki*integ))   # inflow m3/h capped
        level += (u - 0.02*level)*0.1
        err_hist.append(abs(err))
    return level, sum(err_hist)/len(err_hist), max(err_hist[50:])
for kp,ki in ((0.05,0.0),(0.05,0.01),(0.2,0.01)):
    final, mae, peak = sim(kp,ki)
    print(f"kp={kp} ki={ki} final={final:.2f} mae={mae:.2f} peak_abs_err_after_5s={peak:.2f}")
```

Salida esperada:

```text
kp=0.05 ki=0.0 final=44.61 mae=13.29 peak_abs_err_after_5s=15.38
kp=0.05 ki=0.01 final=57.22 mae=8.34 peak_abs_err_after_5s=10.91
kp=0.2 ki=0.01 final=58.15 mae=4.62 peak_abs_err_after_5s=6.17
```

Lena usa el laboratorio para explicar a sus colegas por qué un detector debe vigilar el error y no el nivel bruto. La salida del laboratorio muestra que el error estacionario se reduce mucho cuando se añade la acción integral (nivel final de unos 57–58 frente a 44,61 sin ella, todavía acercándose a 60 al final de la ejecución), lo que ayuda a los colegas a ver cómo responde un controlador a una perturbación. Un detector que generara alarmas sobre el propio nivel saltaría cada vez que cambiara un punto de consigna.

### 17.2 Sensores en el lazo

La inspección en línea añade latencia. Si la constante de tiempo del proceso es de minutos (nivel de un tanque), unas decenas de milisegundos no importan. Si es de decenas de milisegundos (presión rápida), prefiera derivaciones pasivas. Mida antes de desplegar (capítulo 3). En el banco, Lena compara la latencia añadida por cada dispositivo candidato con la constante de tiempo del lazo en que se colocaría: en la línea troncal de T-1 el margen es de minutos, en el patín del compresor solo de decenas de milisegundos, de modo que un mismo dispositivo puede ser aceptable en el primero e inaceptable en el segundo. La latencia medida en el banco decidió ambas elecciones, no las cifras declaradas por el proveedor. Lena registra los valores medidos con las constantes de tiempo de cada lazo, para poder revisar la decisión si cambia un proceso.

### 17.3 Tormentas de alertas

Si cada alerta cibernética de severidad media envía un aviso a todo el sitio, la gente silencia el buscapersonas y luego se pierde la alarma de proceso que importa. El enrutamiento por severidad y los límites de tasa de las notificaciones son amortiguación, exactamente como en el laboratorio de racionalización de alarmas.

> **Caso sintético — Ashford Batch Plant.** Tras revisar el laboratorio de PI, Lena rechazó un equipo de DPI en línea en el patín del compresor (lazo rápido) y aprobó una derivación serie de solo escucha en la línea troncal lenta del tanque.

El enrutamiento de Lena en ABP solo avisa al jefe de turno ante eventos de severidad alta.

### 17.4 Errores y límites

El PI de manual ignora la fricción estática de las válvulas y el retardo de los sensores. Use los historiadores de planta para el ajuste real; el laboratorio sirve para la intuición. Lena advierte a los revisores que las curvas ordenadas del laboratorio no son lo que muestra el historiador de planta. Los lazos reales de ABP tienen fricción estática en las válvulas y retardo en los transmisores, lo que hace la respuesta más lenta y ruidosa. Cualquier umbral de detector propuesto a partir de resultados de laboratorio se contrasta con una semana de datos del historiador antes de usarse, y el ajuste de los controladores reales sigue en manos de los ingenieros de control. Lena registra las diferencias encontradas.

### Nota práctica

Dibuje el lazo: punto de consigna, error, controlador, actuador, proceso, sensor, y marque dónde se ubica su dispositivo de seguridad. Si no puede marcarlo, no sabe si está midiendo o actuando.

### 17.1b Puntos de ajuste y ubicación de las personas

Escriba el punto de ajuste junto al sensor (tiempo de ciclo ≤ 50 ms). Revise los puntos de ajuste cuando la planta cambie de receta o cuando los avisos falsos superen una tasa acordada. Ponga a las personas donde se requiera juicio sobre la autorización; ponga automatización donde el retraso sea peligroso. Aprobar la ampliación de un conducto es tarea humana. Denegar una escritura fuera de rango es automatización. En ABP, el punto de ajuste del tiempo de ciclo del monitor serie es de 50 ms, y se revisa cuando cambian las recetas. La regla práctica es sencilla: automatización para las decisiones rápidas y bien definidas; personas para los juicios sobre autorización y riesgo.

### Ejercicios — capítulo 17

- **EX049 — Laboratorio.** ¿Qué par (kp, ki) se acerca más a 60 con el menor mae? Rúbrica: 3 = (0.2, 0.01) con cifras; 2 = solo el par; 1 = par incorrecto; 0 = nada.
- **EX050 — Ubicación.** En línea o derivación para un lazo de presión de 20 ms: elija y justifique. Rúbrica: 3 = derivación/pasivo, riesgo de latencia; 2 = elección sin justificación; 1 = en línea a la ligera; 0 = nada.
- **EX051 — Amortiguación.** Una regla de amortiguación para las alertas cibernéticas en la sala de control. Rúbrica: 3 = específica (agrupación, severidad, tasa); 2 = vaga; 1 = nada útil; 0 = nada.

### Síntesis del capítulo

Entienda el lazo antes de insertar seguridad; amortigüe las alertas para que las alarmas de proceso sigan oyéndose.

### Siga estudiando — capítulo 17 de 50

[← Capítulo 16 (borrador)](#ch-16) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 18 (borrador) →](#ch-18)

<a id="ch-18"></a>

## Capítulo 18 — Arquitectura de seguridad

### Resultados de aprendizaje

Usted podrá (1) aplicar la zonificación Purdue/62443 en ABP; (2) definir los límites de confianza para el acceso de ingeniería; (3) elegir cuándo un entorno sintético es el lugar adecuado para probar.

### 18.1 Zonas que coinciden con la seguridad funcional

L0/L1 contienen el proceso y el control básico; L2, la supervisión; L3, las operaciones del sitio; L3.5, la DMZ; L4/L5, la empresa. El SIS se ubica con conductos cuidadosamente controlados. Los diagramas de arquitectura deben coincidir con el grafo de alcanzabilidad, no con un póster comercial de Purdue. Lena contrasta el diagrama de ABP con los resultados de alcanzabilidad de la exportación del cortafuegos en cada revisión. En ABP, los puertos de ingeniería del SIS-B solo son alcanzables a través del camino del conmutador con llave durante las pruebas programadas, y la oficina solo alcanza los datos de SCADA a través de la réplica del historiador en la DMZ. Cuando el diagrama y los resultados de alcanzabilidad no coinciden, ganan los resultados y se corrige el diagrama. Lena marca el diagrama con el hash de la exportación con la que se contrastó.

### 18.2 Acceso de ingeniería

Las estaciones de ingeniería y los portátiles de los proveedores cruzan límites de confianza. Prefiera: servidor de salto en la DMZ, cuentas de duración limitada, sesiones monitorizadas, ninguna VPN permanente desde internet hasta L2. Los USB y los módems celulares también son arquitectura: inventaríelos. En ABP, las sesiones de los proveedores pasan por un servidor de salto en la DMZ con cuentas de duración limitada y sesiones grabadas. El inventario de Lena enumera cada portátil de ingeniería autorizado a conectarse, y cualquier VPN permanente encontrada en una revisión se notifica como hallazgo. El uso de USB en las estaciones de ingeniería se registra y se revisa cada mes.

### 18.3 Entornos sintéticos

Cuando los métodos son ruidosos o la planta es frágil, use un entorno sintético o un gemelo digital que refleje la configuración. Los resultados respaldan entonces afirmaciones sobre la configuración reflejada, no sobre el comportamiento del proceso en servicio. Dígalo en el informe.

```python
# Lab 23 - reachability count on a synthetic Purdue-layered OT network
# Nodes: L5-ERP, L4-Office, L3.5-DMZ, L3-Hist, L2-SCADA, L1-PLC, L1-SIS, L0-IO
edges_flat=[("L5","L4"),("L4","L3"),("L3","L2"),("L2","L1-PLC"),("L2","L1-SIS"),("L1-PLC","L0"),("L1-SIS","L0"),("L4","L2")]
edges_zoned=[("L5","L4"),("L4","L3.5"),("L3.5","L3"),("L3","L2"),("L2","L1-PLC"),("L1-SIS","L0"),("L1-PLC","L0")]  # SIS not reachable from SCADA
def reach(edges, start):
    g={}; 
    for a,b in edges: g.setdefault(a,[]).append(b)
    seen=set(); stack=[start]
    while stack:
        n=stack.pop()
        if n in seen: continue
        seen.add(n); stack.extend(g.get(n,[]))
    return seen
for name,e in (("flat",edges_flat),("zoned",edges_zoned)):
    r=reach(e,"L4")
    print(f"{name}: L4 reaches {sorted(r)} count={len(r)} writes_to_SIS={'L1-SIS' in r}")
```

Salida esperada:

```text
flat: L4 reaches ['L0', 'L1-PLC', 'L1-SIS', 'L2', 'L3', 'L4'] count=6 writes_to_SIS=True
zoned: L4 reaches ['L0', 'L1-PLC', 'L2', 'L3', 'L3.5', 'L4'] count=6 writes_to_SIS=False
```

> **Caso sintético — Ashford Batch Plant.** La arquitectura objetivo del CNHP es el grafo por zonas: L4 visualiza a través de L3.5; la ingeniería del SIS solo mediante el conmutador con llave; ningún conducto de L2 a L1-SIS.

La copia de banco de Lena del cortafuegos y del monitor de ABP es un entorno de este tipo; sus informes indican que los resultados se aplican solo a la configuración reflejada.

### 18.4 Errores y límites

Los diagramas envejecen. Vuelva a validar las zonas frente a la exportación del cortafuegos en servicio en cada ventana. Lena compara el diagrama con la exportación del cortafuegos en servicio al comienzo de cada ventana y registra cualquier diferencia como hallazgo. Un diagrama que no se ha contrastado con la exportación se marca como no verificado, para que nadie se apoye en él por error durante un incidente. La nueva prueba a los seis meses encontró más adelante exactamente este tipo de deriva. La comprobación lleva minutos con el script de alcanzabilidad. Su resultado se archiva con el registro de la ventana.

### Nota práctica

Cuelgue el diagrama de zonas junto al mapa de privilegios del capítulo 8. Cuando un proveedor pida una regla temporal, señale la pared y pregúntele qué arista quiere añadir y qué requisito rompe.

### 18.1b Servidores de salto y tráfico de salida

Los servidores de salto de ingeniería tienen un gran valor: bastiónelos, registre el inicio y el final de las sesiones, prohíba los agentes personales de sincronización de archivos y reconstrúyalos a partir de imágenes de referencia entre ventanas cuando sea posible. Las zonas de evaluación y de ingeniería necesitan listas de salida permitida: solo los CIDR de planta dentro del alcance y el almacén de evidencia. Una salida abierta convierte un portátil comprometido en un punto de pivote que el permiso de trabajo nunca autorizó.



Los diagramas de red de la zona de evaluación van al expediente con la misma disciplina de hash que los archivos de evidencia. Cuando un auditor pregunta cómo llegó el tráfico a L2, se muestra la versión del diagrama que estaba vigente, no un boceto más reciente y limpio.

### Ejercicios — capítulo 18

- **EX052 — Esquema de zonas.** Sitúe el HMI, el PLC-A, el SIS-B, el historiador y un PC de oficina en zonas y nombre dos controles en las flechas. Rúbrica: 3 = zonas claras + dos controles; 2 = solo zonas; 1 = confuso; 0 = nada.
- **EX053 — Límite.** ¿Por qué «enviar por correo un CSV de recetas a mi Gmail» es una violación de límites? Rúbrica: 3 = los datos salen de las zonas controladas/la autorización; 2 = vaguedad sobre privacidad; 1 = vago; 0 = lo da por bueno.
- **EX054 — Afirmación sobre el gemelo.** Frase de limitación para pruebas realizadas solo en un entorno sintético. Rúbrica: 3 = afirma sobre la configuración, no sobre el proceso en servicio; 2 = vaga; 1 = afirma de más; 0 = nada.

### Síntesis del capítulo

Zonas, límites del acceso de ingeniería y límites honestos de lo que un gemelo puede demostrar.

### Siga estudiando — capítulo 18 de 50

[← Capítulo 17 (borrador)](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 19 (borrador) →](#ch-19)

<a id="ch-19"></a>

## Capítulo 19 — Identidad y criptografía

### Resultados de aprendizaje

Usted podrá (1) evaluar la identidad en TO sin atacar la criptografía; (2) usar funciones hash para la integridad de la evidencia; (3) manejar con seguridad las credenciales de ingeniería.

### 19.1 La identidad en la planta

Pregunte: ¿qué cuentas existen en los HMI, los historiadores y los equipos de ingeniería? ¿Cuáles usan contraseñas compartidas? ¿Cuáles se integran con el directorio del sitio? La MFA en los servidores de salto de L4 es habitual; en un HMI heredado puede ser imposible: documente los controles compensatorios (acceso físico, grabación de sesiones). La revisión de identidades de Lena en ABP enumeró cada cuenta de HMI-1, del historiador y de eng-WS-1, con su responsable y si era compartida. La contraseña compartida de ingeniería fue el hallazgo más claro y se sustituyó por cuentas nominales. Donde no se pudo añadir MFA a un HMI heredado, registró los controles compensatorios, como el acceso cerrado a la sala de control y la grabación de sesiones en el servidor de salto, y nombró a quién los comprueba.

### 19.2 Hash de la evidencia

Calcule el hash de las exportaciones de configuración y de los archivos de evidencia (SHA-256); guarde los resúmenes en el ticket. Vuelva a calcularlos más tarde para detectar manipulaciones. Acompañe los hashes con el identificador del actor y la versión del permiso de trabajo. Lena calcula el hash de cada exportación del cortafuegos en el momento de recogerla y guarda el resumen en el ticket con la hora, su cuenta y la versión del permiso de trabajo. Las revisiones posteriores vuelven a calcular el hash del archivo almacenado y lo comparan. Una discrepancia se investiga antes de usar la evidencia, porque una exportación modificada podría indicar una manipulación, una edición descuidada o simplemente el archivo equivocado. El manifiesto nombra el algoritmo utilizado.

### 19.3 Secretos

Las credenciales de ingeniería viven en una bóveda; retiradas de corta duración; rotación al final de la ventana. Nada de secretos en git, en capturas de pantalla ni en el chat. Las cuentas de servicio de los historiadores reciben contraseñas únicas y un uso monitorizado.

> **Caso sintético — Ashford Batch Plant.** Una contraseña compartida de «ingeniero» en eng-WS-1 se sustituyó por cuentas nominales tras la revisión de identidades del CNHP. La retirada de los archivos del proyecto del PLC registra ahora a la persona, no a un mítico usuario compartido.

En ABP, las credenciales de ingeniería del proyecto del PLC-A se retiran de la bóveda para una ventana y se rotan después.

### 19.4 Errores y límites

Los hashes detectan cambios, no si fueron malintencionados o accidentales. Acompáñelos con los registros de acceso. No intente descifrar hashes de contraseñas de planta en este curso. Un hash coincidente solo demuestra que un archivo no ha cambiado desde que se calculó su hash, no que se recogiera legalmente ni que se interpretara correctamente. Lena acompaña las comprobaciones de hash con el registro de acceso del almacén de evidencia, que muestra quién tocó cada archivo y cuándo. Los hallazgos sobre contraseñas se notifican a partir de la configuración y de las listas de cuentas; descifrar hashes queda fuera del programa y fuera de cualquier permiso que ella tenga.

### Nota práctica

Las cuentas de emergencia para situaciones críticas de la planta necesitan doble control para recuperarlas y rotación automática tras su uso. Una contraseña de emergencia sin usar pegada bajo un teclado no es un control.

### 19.1b Certificados y cuentas de emergencia

Para los historiadores y servidores de salto con TLS, registre los certificados presentados bajo autorización. Los certificados caducados o que no coinciden son hallazgos de operaciones. El registro de certificados de Lena enumera, para cada equipo, el sujeto, el emisor, la fecha de caducidad y la fecha de observación, de modo que un certificado a punto de caducar en la réplica del historiador se convierte en un ticket con fecha y no en una interrupción por sorpresa. Prefiera SHA-256 para los manifiestos de evidencia; documente el algoritmo en el manifiesto.



La elección del algoritmo de los manifiestos es un campo de versión, no un cambio silencioso a mitad de ventana. Cuando cambia el algoritmo, los manifiestos existentes conservan su campo de algoritmo original y se vuelven a calcular en un manifiesto nuevo en lugar de editarse.

### Ejercicios — capítulo 19

- **EX055 — Preguntas.** Cinco preguntas de identidad para los equipos de ingeniería de ABP. Rúbrica: 3 = cinco concretas; 2 = tres; 1 = una; 0 = nada.
- **EX056 — Hash.** ¿Qué hace cuando el hash de una exportación sellada del cortafuegos no coincide? Rúbrica: 3 = restaurar/volver a exportar, investigar las escrituras, hallazgo de proceso; 2 = solo el archivo; 1 = vago; 0 = ignorarlo.
- **EX057 — Regla sobre secretos.** Política en una línea para las contraseñas de proyectos de PLC en los tickets. Rúbrica: 3 = nunca en el ticket; referencia a la bóveda; 2 = no compartir; 1 = débil; 0 = permite pegarlas.

### Síntesis del capítulo

Lea la configuración de identidades; calcule el hash de la evidencia; guarde los secretos en una bóveda.

### Siga estudiando — capítulo 19 de 50

[← Capítulo 18 (borrador)](#ch-18) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 20 (borrador) →](#ch-20)

<a id="ch-20"></a>

## Capítulo 20 — Seguridad de TO, IoT y sistemas ciberfísicos: contexto de ingeniería

### Resultados de aprendizaje

Usted podrá (1) situar la ingeniería de seguridad de TO entre SP 800-82, ISA/IEC 62443 y ATT&CK for ICS; (2) definir lo que construye este programa de grado; (3) enunciar el límite de seguridad para todos los capítulos posteriores.

### 20.1 Mapa de la disciplina

NIST SP 800-82 orienta la seguridad de los ICS. ISA/IEC 62443 estructura zonas, conductos y niveles de seguridad. ATT&CK for ICS nombra técnicas adversarias para la planificación y la cobertura, no como puntuación de riesgo residual. Las especificaciones de Modbus definen el protocolo sobre el que se construye la lista de permitidos. Las revisiones académicas (Giraldo et al.; Urbina et al.) advierten contra los detectores evaluados solo con ataques fáciles. Los ingenieros construyen las plataformas y los procesos que hacen operativas esas fuentes bajo las restricciones de la seguridad de procesos.

Lena usa cada fuente para aquello en lo que es buena y cita la revisión exacta.

### 20.2 Qué construimos

El CNHP de Ashford Batch Plant es el ejemplo conductor: zonificación, listas de permitidos, detectores con métricas honestas, ventanas de parches, expedientes de evidencia. Los egresados diseñan, verifican y operan programas de este tipo; no inventan exploits contra PLC. Los resultados del programa son concretos: una red por zonas con alcanzabilidad probada, listas de permitidos aplicadas al tráfico Modbus, detectores con intervalos de falsas alarmas publicados, un calendario de parches con aplazamientos fechados y un expediente que un auditor puede verificar. Cada capítulo posterior añade una parte de ese sistema y muestra cómo Lena la construyó y la comprobó en ABP sin poner en peligro ningún lote.

### 20.3 Límite de seguridad

Nada de cargas útiles de exploits, nada de acceso no autorizado a plantas, nada de datos personales o de lotes propietarios reales en los laboratorios, que solo usan datos locales sintéticos. Las solicitudes de doble uso se rechazan (capítulo 10). Las condiciones de parada de seguridad de procesos siempre prevalecen. Este límite es un requisito en cada revisión de diseño de los capítulos 21-50.

> **Caso sintético — Ashford Batch Plant.** La dirección pidió un equipo rojo que hackeara la planta. Lena reformuló el mandato: un programa autorizado de bastionado que aplica zonas y mide la detección sin poner en peligro los lotes.

Lena contrasta cada diseño con este límite.

### 20.4 Errores y límites

Los marcos evolucionan; vuelva a comprobar las URL y las versiones antes de citarlos en una tesis. Este capítulo orienta; no sustituye la lectura de las fuentes primarias. La lista de fuentes de Lena registra la revisión y la fecha de acceso de cada norma y artículo usados en los documentos del CNHP. Antes de citar un marco en su tesis, comprueba si existe una revisión más reciente y anota cualquier cambio que afecte a su argumento. El capítulo solo da la orientación suficiente para empezar; leer las fuentes primarias forma parte del trabajo.

### Nota práctica

Mantenga en la carpeta del CNHP una lista de una página de «fuentes que realmente usamos», con las fechas de acceso. Los examinadores y los auditores preguntan a qué revisión de 62443 se refería; «la de ISA» no es una respuesta.

### 20.1b Cursos vecinos y entregables

Este libro de ingeniería presupone soltura con el cálculo, la probabilidad y la ingeniería de software de los capítulos anteriores. El libro de TO de licenciatura es más amplio; el de tecnólogo pone el énfasis en los ejercicios de implementación. Los operadores necesitan procedimientos operativos y tickets; los ingenieros necesitan esquemas, pruebas y registros de decisiones de arquitectura (ADR). La evaluación del proyecto final busca ambos. Cada entregable nombra a su lector previsto en la primera página. Los entregables de Lena en ABP incluyen ambos tipos. Sus procedimientos operativos y tickets sirven a los operadores que hacen funcionar la planta cada día, mientras que los esquemas, las pruebas y los registros de decisiones sirven a los ingenieros que mantendrán las herramientas después de ella. Los evaluadores buscan ambos.

### Ejercicios — capítulo 20

- **EX058 — Encaje de marcos.** Empareje cada necesidad con SP 800-82 / 62443 / ATT&CK ICS / especificación Modbus. Rúbrica: 3 = cuatro pares sensatos; 2 = tres; 1 = dos; 0 = nada.
- **EX059 — Mandato.** Reescriba «hackear la planta» como una frase de mandato de ingeniería. Rúbrica: 3 = autorización + bastionado/medición + seguridad funcional; 2 = parcial; 1 = sigue centrada en el ataque; 0 = nada.
- **EX060 — Límite.** Tres elementos concretos fuera del alcance de este programa. Rúbrica: 3 = tres claros; 2 = dos; 1 = uno; 0 = nada.

### Síntesis del capítulo

Los ingenieros hacen posible el bastionado autorizado de la TO; no sustituyen la seguridad de procesos por ingenio.

### Siga estudiando — capítulo 20 de 50

[← Capítulo 19 (borrador)](#ch-19) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 21 (borrador) →](#ch-21)

<a id="ch-21"></a>

## Capítulo 21 — Seguridad de TO, IoT y sistemas ciberfísicos: requisitos

### Resultados de aprendizaje

Usted podrá (1) obtener requisitos de seguridad de procesos, de operaciones y de seguridad de la información; (2) separar los requisitos funcionales, de seguridad funcional y de medición; (3) redactar criterios de aceptación que un probador pueda ejecutar con datos de prueba sintéticos.

### 21.1 Fuentes

Seguridad de procesos quiere capas de protección independientes. Operaciones quiere visualizar sin tiempo de parada. Seguridad de la información quiere conductos con denegación por defecto. Las entrevistas de obtención producen enunciados con «deberá» etiquetados por su fuente. Los conflictos (visualización por conveniencia frente a aislamiento del SIS) se registran, no se disimulan. En ABP, Lena entrevistó por separado al ingeniero de seguridad de procesos, a los jefes de turno, a los ingenieros de control y al equipo de red de TI, y después llevó los conflictos a una reunión conjunta. El conflicto más claro fue la regla de visualización remota FW-12, que operaciones valoraba y seguridad funcional no podía aceptar. Se registró con ambas posturas, y la solución, visualizar a través de la réplica de la DMZ, se convirtió en un requisito con responsable.

### 21.2 Tres familias

Funcional: «El monitor serie deberá decodificar Modbus RTU en la línea troncal A y emitir decisiones de permitir/denegar». Seguridad funcional: «Si el archivo de la lista de permitidos no se carga, el monitor deberá fallar de forma cerrada (descartar todo el tráfico no esencial, o generar una alarma y exigir una acción humana, según el diseño)». Medición: «El CNHP deberá informar de la cobertura de técnicas de ATT&CK for ICS planificada frente a observada, con denominadores». En caso de empate, ganan los requisitos de seguridad funcional.

Lena etiqueta cada requisito del CNHP con su familia, para que las revisiones puedan comprobar que los de seguridad funcional se prueban primero. Los empates se resuelven por escrito.

### 21.3 Criterios de aceptación

Cada requisito tiene un Dado/Cuando/Entonces sobre datos sintéticos. Ejemplo: Dado que se deniega L2 a L1-SIS, Cuando se ejecuta la alcanzabilidad desde L4, Entonces L1-SIS no está en el conjunto alcanzable. Los criterios que requieren una escritura en una planta en servicio se rechazan en la revisión.

> **Caso sintético — Ashford Batch Plant.** El requisito de seguridad funcional S-1, «fallar de forma cerrada si falta la lista de permitidos», no superó su prueba de aceptación cuando una ruta con una errata devolvió PASS. La corrección se publicó antes de cualquier ventana en la planta.

Los criterios se revisan con el responsable del requisito. Cada criterio es una prueba.

### 21.4 Errores y límites

Las partes interesadas inventan requisitos a mitad de ventana; apárquelos en una lista de pendientes con un ticket AUTH; no parchee en caliente los monitores de producción durante un lote. Cuando alguien pide una nueva regla de monitor durante un lote, Lena la registra en la lista de pendientes con un ticket de autorización y la evalúa después de la ventana. Cambiar un monitor de producción a mitad de lote arriesga una interrupción o un error de fallo abierto que nadie ha probado. El elemento pendiente nombra quién lo pidió, por qué y cuándo se revisará, para que la solicitud no se pierda y quien la planteó vea que se atiende.

### Nota práctica

Las pruebas de aceptación llevan el nombre de los identificadores de los requisitos y hacen fallar la integración continua cuando se omiten. Los requisitos Must huérfanos se prueban o se aplazan formalmente con un responsable de la dirección.

### 21.1b MoSCoW bajo seguridad funcional

La priorización Must/Should/Could sigue colocando todos los requisitos de seguridad funcional en Must. Un Could que debilita un Must (la denegación opcional de los códigos de escritura) se reclasifica o se rechaza. Los gestores de producto no ganan por votación al fallo cerrado. Los campos de registro llevan también el identificador del requisito (req=S-1), para que un evento de denegación pueda trazarse hasta el requisito que aplica. En ABP, S-1 y R-12 son ambos elementos Must, y ninguna decisión de producto puede bajarlos de nivel. Una solicitud para hacer opcionales, por conveniencia, las denegaciones de códigos de escritura se rechazó por este motivo, y el rechazo se registra con el requisito que habría debilitado.

### Ejercicios — capítulo 21

- **EX061 — Obtención.** Escriba un requisito funcional y uno de seguridad funcional con «deberá» a partir de «la oficina no debe alcanzar el SIS». Rúbrica: 3 = ambos comprobables; 2 = uno; 1 = vago; 0 = nada.
- **EX062 — Aceptación.** Dado/Cuando/Entonces para el fallo cerrado cuando falta la lista de permitidos. Rúbrica: 3 = completo, con la denegación/alarma esperada; 2 = parcial; 1 = idea; 0 = nada.
- **EX063 — Conflicto.** Visualización de L4 a L2 por conveniencia frente a zonificación: registre el conflicto y la regla elegida. Rúbrica: 3 = conflicto nombrado + regla que antepone la seguridad funcional, vía DMZ; 2 = solo la regla; 1 = elige la conveniencia; 0 = nada.

### Síntesis del capítulo

Los requisitos vienen de las personas, se dividen en familias y se entregan con pruebas de aceptación sobre datos de prueba sintéticos.

### Siga estudiando — capítulo 21 de 50

[← Capítulo 20 (borrador)](#ch-20) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 22 (borrador) →](#ch-22)

<a id="ch-22"></a>

## Capítulo 22 — Seguridad de TO, IoT y sistemas ciberfísicos: modelos de sistemas y de datos

### Resultados de aprendizaje

Usted podrá (1) dibujar un modelo de entidades para activos, zonas, conductos y hallazgos; (2) elegir claves y cardinalidades; (3) mantener el contenido de explotación fuera del modelo.

### 22.1 Entidades

Plant 1—* Unit; Unit 1—* Asset; Zone 1—* Asset; Conduit *—* Zone (origen/destino); Finding *—* EvidenceObject (por hash); TechniqueTag *—* Finding. Los errores de cardinalidad (muchos conjuntos de conductos activos sin un puntero de versión) llevan a los auditores a preguntar qué reglas estaban vigentes. El modelo de Lena da a cada ConduitSet una versión y registra qué versión estaba vigente en cada momento, de modo que un auditor puede ver las reglas que se aplicaban un día determinado. Cada Finding se vincula a su evidencia por hash, y las etiquetas de técnica se vinculan a los hallazgos solo después de la revisión.

### 22.2 Claves

Los identificadores de los hallazgos son UUID. La evidencia se direcciona por contenido mediante SHA-256. ConduitSet tiene (plant_id, version_int). Nunca use el título como clave de los hallazgos: los títulos cambian. El esquema de Lena usa estas claves en todo el CNHP. Un hallazgo sobre FW-12 conservó su identificador cuando se reformuló su título tras la revisión, y su historial siguió intacto. La evidencia indexada por su hash no puede sustituirse en silencio, ya que un archivo distinto tendría una clave distinta. El número de versión de ConduitSet aumenta con cada cambio publicado y nunca reutiliza un valor antiguo.

### 22.3 Atributos prohibidos

Ningún atributo para cargas útiles, shellcode ni ataques paso a paso. EvidenceObject guarda los bytes en un repositorio sellado; el modelo solo guarda el hash, el tipo de medio y la clase de conservación.

> **Caso sintético — Ashford Batch Plant.** Un esquema inicial tenía notas como texto libre; la gente pegaba contraseñas de ingeniería. Lena lo sustituyó por campos estructurados más un hash de evidencia, y un linter rechaza las cadenas con aspecto de contraseña en los títulos.

El linter de Lena aplica la lista. Se ejecuta con cada registro creado o importado, incluidas las importaciones masivas desde escáneres, y rechaza las cadenas con aspecto de contraseña en los títulos. Los registros rechazados devuelven un error que explica qué campo se rechazó.

### 22.4 Errores y límites

Los modelos que imponen cada técnica de ATT&CK for ICS como campo obligatorio generan etiquetas basura. Mantenga las etiquetas de técnica como opcionales y revisadas. En ABP, un analista añade las etiquetas de técnica después de redactar el hallazgo, y una segunda persona las revisa. Un hallazgo sin una técnica adecuada se deja sin etiqueta en lugar de forzarlo a la más cercana. Esto mantiene honestas las cifras de cobertura, porque una etiqueta basura contaría como cobertura observada de una técnica que nadie probó realmente. Las etiquetas se revisan cuando cambia la versión de ATT&CK for ICS.

### Nota práctica

Haga borrados lógicos de los hallazgos con actor y motivo; purgue físicamente solo mediante trabajos de conservación que emitan eventos de auditoría. Un DELETE FROM findings silencioso es un regalo para el repudio.

### 22.1b Límites de los adjuntos y tiempo

Los objetos de evidencia necesitan límites de tamaño y listas de tipos de medio permitidos. Las subidas sin límite se convierten en ataques a la disponibilidad e invitan a volcar datos propietarios en masa. Toda entidad mutable necesita created_at, created_by y, para los cambios de estado, updated_at/updated_by o un evento de solo anexado. En las exportaciones, prefiera UTC con desplazamientos explícitos. Las exportaciones indican su zona horaria una vez en la cabecera del archivo, además de en cada marca de tiempo. A los clientes de la API que emiten DELETE en bucle durante un reintento defectuoso se les revocan las credenciales tras superar un umbral.

### 22.5 Ejemplo resuelto: modelar un hallazgo sin filtrar la planta (ABP sintética)

El modelo de datos de Lena para los hallazgos del CNHP tiene las entidades Asset, Zone, Conduit, Finding y Evidence. Un Finding referencia un Asset por clave, nunca incrusta su dirección IP ni sus credenciales, y guarda la evidencia como un hash más un puntero al almacén de evidencia controlado. La lista de atributos prohibidos (contraseñas, cargas útiles completas de paquetes, valores de recetas) se aplica mediante una comprobación del esquema que rechaza cualquier registro que contenga esos campos. Cuando un hallazgo sobre el puerto Modbus abierto del PLC-A se exporta para la dirección, dice «Asset PLC-A, Conduit L2→L1, ATT&CK for ICS T0869 Standard Application Layer Protocol, severidad alta»: suficiente para actuar, no para atacar.

### Ejercicios — capítulo 22

- **EX064 — Cardinalidad.** ¿Por qué ConduitSet tiene versiones en lugar de editarse en el sitio? Rúbrica: 3 = auditoría de lo que estaba autorizado y cuándo; 2 = versionado vago; 1 = «buena práctica»; 0 = nada.
- **EX065 — Clave.** ¿Por qué direccionar la evidencia por contenido? Rúbrica: 3 = integridad + deduplicación + evidencia de manipulación; 2 = una razón; 1 = vago; 0 = nada.
- **EX066 — Prohibido.** Validación que impida contraseñas en el título. Rúbrica: 3 = heurística/linter + proceso; 2 = uno; 1 = vago; 0 = nada.

### Síntesis del capítulo

Modele activos, zonas, versiones, hallazgos y hashes, no ataques.

### Siga estudiando — capítulo 22 de 50

[← Capítulo 21 (borrador)](#ch-21) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 23 (borrador) →](#ch-23)

<a id="ch-23"></a>

## Capítulo 23 — Seguridad de TO, IoT y sistemas ciberfísicos: análisis de amenazas y fallos

### Resultados de aprendizaje

Usted podrá (1) enumerar los fallos del propio programa de seguridad de TO; (2) aplicar una pasada ligera de STRIDE sobre las herramientas; (3) incorporar los resultados a los requisitos sin construir módulos de explotación.

### 23.1 El programa puede fallar de forma peligrosa

Listas de permitidos que fallan de forma abierta, integración continua de alcanzabilidad omitida, detectores con tormentas silenciosas de falsas alarmas, aplazamientos de parches sin fecha: todo ello amenaza la seguridad de procesos y la honestidad, no solo la confidencialidad de una herramienta. Lena enumera primero estos fallos en el análisis de amenazas del CNHP porque podrían dañar la planta a través de las herramientas destinadas a protegerla. Un monitor que falla de forma abierta dejaría que escrituras no autorizadas llegaran al PLC-A mientras todos creen que están bloqueadas. Una comprobación de alcanzabilidad omitida en la integración continua dejaría fusionar sin que nadie lo viera un nuevo conducto hacia el SIS-B. Cada fallo recibe un requisito y una prueba.

### 23.2 STRIDE sobre las herramientas del CNHP

Suplantación (spoofing): cuenta de ingeniería falsa. Manipulación (tampering): editar la exportación del cortafuegos después del sellado. Repudio: eventos de denegación sin actor. Divulgación de información: réplica del historiador legible por cualquiera. Denegación de servicio: un escáner inunda una línea troncal. Elevación de privilegios: una sola persona puede publicar un conducto hacia el SIS. Cada fila recibe un requisito de mitigación. Lena realiza el análisis sobre cada herramienta del CNHP y registra las filas en la lista de pendientes con sus responsables. En ABP, las filas más graves fueron el monitor que falla de forma abierta y una sola persona que publica un conducto hacia el SIS-B; se convirtieron en el requisito S-1 y en el control de doble aprobación de los cambios de conductos. Cada fila se revisa de nuevo cuando se entrega su mitigación.

### 23.3 Las amenazas a la planta se quedan en el análisis de peligros

Las amenazas al proceso pertenecen al análisis de peligros del proceso de la planta y al HAZOP informado por la ciberseguridad, no a las funciones de una herramienta de estudiante. No construya explotación automatizada para satisfacer una fila de STRIDE.

```python
# Lab 27 - residual CUSUM vs band on batch reactor level (synthetic)
import random
def run(seed, atk, det, k=0.8, h=6.0):
    rng=random.Random(seed); true=est=50.0; s=0.0; alarm=None
    for t in range(500):
        inflow=1.0+rng.gauss(0,0.05)+(0.08 if atk and t>=250 else 0)
        true+=inflow-0.02*true
        lvl=true+rng.gauss(0,0.3); fm=inflow+rng.gauss(0,0.02)
        if atk and t>=250: lvl=50+rng.gauss(0,0.3)
        if atk=="B" and t>=250: fm=1.0+rng.gauss(0,0.02)
        est+=fm-0.02*est
        hit=abs(lvl-50)>2.0 if det=="band" else False
        if det=="cusum":
            s=max(0.0,s+abs(lvl-est)-k); hit=s>h
        if hit and alarm is None: alarm=t
    return alarm
for det in ("band","cusum"):
    fa=sum(run(i,None,det) is not None for i in range(60))
    for atk in ("A","B"):
        hits=[a-250 for a in (run(i,atk,det) for i in range(60)) if a is not None and a>=250]
        print(f"{det} class{atk} FA={fa}/60 det={len(hits)}/60 mean_delay={sum(hits)/len(hits) if hits else float('nan'):.1f}")
```

Salida esperada:

```text
band classA FA=0/60 det=0/60 mean_delay=nan
band classB FA=0/60 det=0/60 mean_delay=nan
cusum classA FA=0/60 det=60/60 mean_delay=24.8
cusum classB FA=0/60 det=0/60 mean_delay=nan
```

> **Caso sintético — Ashford Batch Plant.** La fila de STRIDE «fallo abierto» se convirtió en el requisito de seguridad funcional S-1. La fila «publicación de un conducto por una sola persona» se convirtió en el control de doble aprobación.

Lena traslada las amenazas a la planta al ingeniero de seguridad de procesos para el análisis de peligros. Ella aporta hechos sobre las herramientas y la red, como qué zonas pueden alcanzar el PLC-A, y el ingeniero juzga las consecuencias para el proceso. Nada en las herramientas del CNHP simula un ataque al proceso.

### 23.4 Errores y límites

STRIDE es un estímulo, no una demostración. Vuelva a él cuando añada un nuevo límite de confianza (por ejemplo, un historiador SaaS de un proveedor). Lena repite el análisis cada vez que el CNHP añade un límite de confianza, como una nueva vía de acceso remoto para un proveedor o un cambio en el destino de las alertas. Las filas de revisiones anteriores se conservan, para que el equipo pueda ver qué amenazas se añadieron, qué mitigaciones se construyeron y cuáles siguen abiertas. Una tabla STRIDE nunca demuestra que una herramienta sea segura; eso lo hacen las pruebas y las revisiones.

### Nota práctica

Incluya en el modelo la amenaza «servidor de salto comprometido»: credenciales de corta duración, listas de salida permitida, revocación rápida. Si la respuesta es solo «confiar en el servidor de salto», el análisis está incompleto.

### 23.1b Abuso frente a mal uso y lista de pendientes

Los casos de abuso son acciones intencionadas de un adversario contra las herramientas del CNHP. Los casos de mal uso son operadores honestos que cometen errores peligrosos (pegar un CIDR que incluye a un socio). Diseñe controles para ambos. Las filas de STRIDE se convierten en incidencias vinculadas a requisitos. Las filas de mal uso suelen convertirse en reglas de validación; las de abuso, en controles de acceso. Alimentar la lista de pendientes significa que cada fila de STRIDE tiene un responsable y una fecha límite. En ABP, el caso de mal uso de un ingeniero que pega el CIDR de un socio en el archivo de conductos se convirtió en una regla de validación que rechaza los rangos fuera del plan de direcciones de la planta.

Ambos tipos alimentan la lista de pendientes.

### Ejercicios — capítulo 23

- **EX067 — Fallo abierto.** Una prueba que demuestre el fallo cerrado. Rúbrica: 3 = quitar la política, esperar denegación + alerta; 2 = idea; 1 = vago; 0 = nada.
- **EX068 — STRIDE.** Mitigación del repudio en los eventos de denegación. Rúbrica: 3 = actor autenticado + registro inmutable; 2 = solo registro; 1 = vago; 0 = nada.
- **EX069 — Límite.** ¿Por qué el STRIDE del programa no justifica un módulo de explotación? Rúbrica: 3 = objetivo distinto/límite de seguridad; 2 = parcial; 1 = lo justifica; 0 = nada.

### Síntesis del capítulo

Analice cómo su programa puede dañar la planta o mentir; mitigue eso primero.

### Siga estudiando — capítulo 23 de 50

[← Capítulo 22 (borrador)](#ch-22) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 24 (borrador) →](#ch-24)

<a id="ch-24"></a>

## Capítulo 24 — Seguridad de TO, IoT y sistemas ciberfísicos: métodos I

### Resultados de aprendizaje

Usted podrá (1) encadenar permiso de trabajo, descubrimiento, validación e informe; (2) elegir métodos que se ajusten a la autorización y al riesgo de proceso; (3) definir cuándo está terminado un método sin escribir en un PLC.

### 24.1 Secuencia

Primero, el permiso de trabajo. El descubrimiento enumera activos y conductos mediante métodos acordados. La validación confirma los problemas de configuración con mínimo privilegio. El informe entrega los hallazgos y los hashes de la evidencia. Saltarse el permiso es la forma en que se producen las pruebas no autorizadas. En ABP, cada actividad del CNHP empieza con un permiso de trabajo firmado que nombra las unidades, los métodos, las ventanas y las condiciones de parada. El descubrimiento usa captura pasiva y exportaciones del proyecto de ingeniería; la validación usa revisión de configuración y pruebas en banco. Los hallazgos se notifican con los hashes de la evidencia, y nada pasa al paso siguiente hasta que el anterior ha producido sus artefactos.

### 24.2 Fichas de método

Cada ficha: nombre, propósito, privilegio, ¿ruidoso?, impacto en el proceso, condiciones de parada, artefactos. La revisión de configuración autenticada es una ficha; un exploit de PLC convertido en arma no está en la baraja de este programa. Lena guarda las fichas de método de ABP en el repositorio, junto a la plantilla del permiso de trabajo. Un permiso solo puede enumerar métodos que tengan ficha, y cada ficha indica si el método es ruidoso y qué impacto podría tener en el proceso. Los revisores contrastan las condiciones de parada de la ficha con el permiso, de modo que un método no pueda usarse en condiciones más débiles que las que exige su ficha.

### 24.3 Terminado significa artefactos

Un método está terminado cuando existen el CSV de inventario, los hashes de configuración, los borradores de hallazgos y las actualizaciones de cobertura, no cuando alguien siente que ha acabado.

> **Caso sintético — Ashford Batch Plant.** La ficha de método para la verificación serie de la lista de permitidos exige modo de solo escucha, parada si el tiempo de ciclo llega a 50 ms y, como artefacto, una tabla de decisiones al estilo del laboratorio.

La lista de comprobación de Lena para cada método enumera sus artefactos obligatorios. Para la verificación serie de la lista de permitidos en ABP, eso significa la tabla de decisiones, el hash de la captura, los borradores de hallazgos que haya y el tablero de cobertura actualizado. Un método al que le faltan artefactos se reabre, no se cierra con una nota que promete entregarlos más tarde. Lena revisa la lista al final de cada ventana.

### 24.4 Errores y límites

Copiar la lista de métodos de otra persona sin la autorización correspondiente es 62443 de culto al cargamento. Una lista de métodos copiada de otra planta o de una guía publicada puede suponer autorizaciones, equipos o tolerancias del proceso que ABP no tiene. Lena adapta cada método al permiso propio de ABP, escribe una ficha para él y hace que ingeniería de control la revise antes de usarla. Un método prestado sin esa revisión se trata como no autorizado, por prestigiosa que sea su fuente, y queda fuera del permiso hasta que se revise.

### Nota práctica

Congele los métodos durante una ventana igual que congela los conductos: los métodos nuevos necesitan la vía AUTH, no un «ya que estábamos, también probamos».

### 24.1b Métodos silenciosos frente a ruidosos y dependencias

Los métodos silenciosos (decodificación de solo escucha, exportación de configuración) caben en más ventanas. Los métodos ruidosos necesitan límites de tasa más estrictos y, a menudo, horas de baja actividad. Codifique las dependencias entre métodos en el plan, para que no se programen revisiones contra una lista de activos vacía. El plan de Lena enumera, para cada método, los métodos anteriores cuyos artefactos necesita. Las fichas de método sin un campo «ruidoso» son la causa de que se congestionen las ventanas de los lotes matutinos. Los métodos ruidosos se reservan frente al calendario de lotes con una semana de antelación, fuera de la fase de carga de R-101, y cada reserva nombra la línea troncal y su parada por tiempo de ciclo de 50 ms.

Lena programa primero los métodos silenciosos.

### Nota de campo: congelación de métodos en la práctica

Durante la ventana W-17 de ABP, un proveedor pidió probar una función de diagnóstico adicional a mitad de turno. Lena aparcó la solicitud en la lista de planificación del siguiente encargo y mantuvo congelada la ficha de método. El lote terminó sin tráfico inexplicado, y el diagnóstico se evaluó al mes siguiente con un nuevo permiso de trabajo y sus propias condiciones de parada.

### Ejercicios — capítulo 24

- **EX070 — Ficha.** Escriba una ficha de método para la decodificación Modbus de solo escucha. Rúbrica: 3 = todos los campos rellenados de forma segura; 2 = falta uno; 1 = incluye escrituras/exploits; 0 = nada.
- **EX071 — Secuencia.** ¿Qué tiene de malo el descubrimiento antes de un permiso de trabajo firmado? Rúbrica: 3 = pruebas no autorizadas; 2 = proceso vago; 1 = «orden incorrecto»; 0 = nada.
- **EX072 — Terminado.** Enumere cuatro artefactos que cierran un método de revisión de zonificación. Rúbrica: 3 = cuatro concretos; 2 = dos; 1 = uno; 0 = nada.

### Síntesis del capítulo

Los métodos están autorizados, tienen ficha y están terminados cuando existen los artefactos.

### Siga estudiando — capítulo 24 de 50

[← Capítulo 23 (borrador)](#ch-23) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 25 (borrador) →](#ch-25)

<a id="ch-25"></a>

## Capítulo 25 — Taller de diseño I

### Resultados de aprendizaje

Usted podrá (1) esbozar la canalización de permitir/denegar del monitor serie de ABP; (2) justificar las concesiones en una breve revisión de diseño; (3) producir un registro de decisión de una página.

### 25.1 Problema del taller

Diseño: trama de entrada → decodificar → cargar ConduitSet/lista de permitidos → evaluar permit → emitir evento → reenviar o descartar. Opciones: política incrustada en el código frente a archivo de datos firmado; alertas síncronas frente a asíncronas ante las denegaciones. El equipo de taller de Lena en ABP esboza todo el camino en una página y marca dónde se deniega una trama si falta la política. Las dos elecciones debatidas fueron si la lista de permitidos vive en el código o en un archivo de datos firmado, y si las alertas sobre denegaciones se envían de forma síncrona o se encolan. Cada opción se pone por escrito con sus consecuencias antes de que nadie defienda una.

### 25.2 Concesiones

La política como datos firmados permite publicar actualizaciones sin volver a desplegar el firmware, pero necesita verificación de firma y fallo cerrado ante firmas incorrectas. Las alertas asíncronas escalan, pero pueden desordenarse; para las denegaciones en el camino del SIS, prefiera la alerta síncrona. El equipo de Lena acuerda que una firma incorrecta debe detener todo el tráfico no esencial, exactamente como exige el requisito S-1 cuando falta la política. Las alertas síncronas se reservan para las denegaciones de códigos de escritura y de caminos relacionados con el SIS, donde el retraso importa; las denegaciones rutinarias de lectura se encolan. El equipo registra también qué ocurre si se pierde la clave de firma: el monitor conserva la última lista válida y genera una alarma, y no se acepta ninguna actualización sin firmar.

### 25.3 Registro de decisión

Una página: contexto, opciones, decisión, consecuencias, fecha, responsables. Guárdelo junto al código.

> **Caso sintético — Ashford Batch Plant.** El taller eligió listas de permitidos en JSON firmado, camino síncrono para las denegaciones que afectan a códigos de escritura y procesamiento masivo asíncrono para las lecturas rutinarias. El ADR-004 lo recoge.

El ADR-004 registra en este formato la decisión del taller sobre las listas de permitidos en JSON firmado, con Lena y el responsable de ingeniería de control como responsables. Está en el repositorio junto al código de la política, para que cualquiera que modifique el cargador pueda leer por qué funciona como funciona.

### 25.4 Errores y límites

Los talleres que se saltan los requisitos de seguridad funcional producen diagramas bonitos que fallan de forma abierta. El taller de Lena se niega a revisar un diseño hasta que muestre dónde deniega el tráfico el monitor cuando falta la lista de permitidos o falla su firma. Los diseños que no pueden responder se devuelven antes de cualquier discusión sobre disposición o herramientas. Las tarjetas de restricciones hacen visibles sobre la mesa los requisitos de seguridad funcional desde el primer minuto, para que no se olviden en el entusiasmo por una arquitectura ingeniosa. Los diseños rechazados también se registran.

### Nota práctica

Los facilitadores detienen la sala con: «¿Dónde DENEGAMOS si falta la política?». Si nadie puede responder, la arquitectura no está lista.

### 25.1b Tarjetas de restricciones y galería

Entregue a cada equipo del taller tarjetas de restricciones: residencia de datos, operación con dos ingenieros, fallo cerrado, nada de puntuaciones vacías, independencia del SIS. Los diseños que violan una tarjeta se rechazan antes del debate estético. Los talleres terminan con una galería: los equipos exponen sus borradores de ADR y los demás intentan encontrar un camino de fallo abierto en cinco minutos. Un esbozo de taller debe nombrar por escrito los límites de confianza, los almacenes de datos y el camino de fallo cerrado. Diez minutos de etiquetado valen más que una hora de diseño estético. Los caminos de fallo abierto encontrados en la galería se escriben en el ADR antes de aceptarlo.

### Nota de campo: etiquetar antes de maquetar

Los equipos de taller que dedicaron los primeros veinte minutos a nombrar los puntos de DENEGACIÓN y los límites de confianza produjeron ADR que superaron la revisión. Los equipos que empezaron por las paletas de colores redescubrieron caminos de fallo abierto durante la galería. El CNHP exige ahora un camino de fallo cerrado etiquetado en la fotografía de la pizarra adjunta a cada ADR.

### Ejercicios — capítulo 25

- **EX073 — Opciones.** Dos opciones para entregar la política y un riesgo de cada una. Rúbrica: 3 = dos + riesgos; 2 = opciones; 1 = una; 0 = nada.
- **EX074 — ADR.** Línea de decisión para las alertas síncronas de denegación sobre códigos de escritura. Rúbrica: 3 = decisión clara + por qué; 2 = solo la decisión; 1 = vago; 0 = nada.
- **EX075 — Revisión.** Tres preguntas que debe hacer un revisor. Rúbrica: 3 = fallo cerrado, autenticación de la política, presupuesto de latencia; 2 = dos; 1 = una; 0 = nada.

### Síntesis del capítulo

El trabajo de taller termina en una decisión registrada, no en una impresión.

### Siga estudiando — capítulo 25 de 50

[← Capítulo 24 (borrador)](#ch-24) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 26 (borrador) →](#ch-26)

<a id="ch-26"></a>

## Capítulo 26 — Seguridad de TO, IoT y sistemas ciberfísicos: alternativas de arquitectura

### Resultados de aprendizaje

Usted podrá (1) comparar monitores locales con analítica en la nube para los datos de TO; (2) evaluar frente a las restricciones de residencia de datos y de seguridad de procesos; (3) elegir una alternativa rechazando explícitamente las demás.

### 26.1 Alternativas

A: monitores serie/IP locales con detectores locales. B: recogida local con analítica en el historiador del sitio. C: analítica SaaS en la nube que recibe valores de proceso. Cada una responde a restricciones distintas. Lena describe cada opción para ABP con la misma estructura: adónde van los datos de proceso, quién los opera, cómo falla y cuánto cuesta. La opción C enviaría valores de proceso fuera del sitio, lo que plantea de inmediato cuestiones de residencia de datos y de confidencialidad de las recetas. Las opciones A y B mantienen los datos en el sitio, pero difieren en la rapidez con que pueden aplicar decisiones en el camino de escritura.

### 26.2 Criterios

Independencia de la seguridad de procesos, residencia de datos, comportamiento de fallo cerrado, operabilidad por el equipo del sitio, coste. Dé más peso a la seguridad funcional y a la residencia que a la novedad. Lena acuerda los pesos con el ingeniero de seguridad de procesos y el jefe de planta antes de puntuar. La independencia de la seguridad funcional y la residencia de datos tienen el mayor peso, porque un fallo en ellas no puede deshacerse con correcciones posteriores. Cada opción se puntúa con evidencia, y las opciones que no cumplen un criterio de seguridad funcional se rechazan sean cuales sean sus demás puntuaciones. Los pesos se publican en el análisis para que los revisores puedan cuestionarlos.

### 26.3 Decisión

ABP rechazó C porque las tendencias cercanas a las recetas no deben salir del sitio sin una excepción aprobada por el consejo de administración. Eligió A para la aplicación en el camino de escritura, con B para la investigación de detección a más largo plazo sobre réplicas.

> **Caso sintético — Ashford Batch Plant.** Una demostración de C por parte de un proveedor parecía impecable; la asesoría jurídica y seguridad de procesos bloquearon la subida sin restricciones. El ADR-011 registra el rechazo.

El ADR-011 registra esta decisión. Las razones son breves: la opción A aplica las decisiones localmente en el camino de escritura y pueden operarla los ingenieros del sitio; la opción B añade investigación de detección, pero necesita competencias de las que carece el turno de noche, así que se reserva para el trabajo diurno sobre réplicas. La opción C sigue rechazada hasta que cambien las normas de residencia, que es su desencadenante de revisión registrado.

### 26.4 Errores y límites

Un análisis de alternativas que ignora las cláusulas de datos del permiso de trabajo es teatro. En ABP, las cláusulas de datos del permiso prohíben que los valores de proceso salgan del sitio sin una excepción del consejo de administración, así que la opción C quedó descartada antes de cualquier comparación técnica. Lena registra esa restricción al principio del análisis, para que los lectores vean por qué se rechazó C sin leer la puntuación. Un análisis que hubiera puntuado alto a C ignorando el permiso habría hecho perder el tiempo al consejo y podría haber presionado a alguien para conceder una excepción.

### Nota práctica

Documente las competencias que exige cada alternativa. Una canalización en la nube que nadie en el sitio sabe operar falla de forma abierta en lo social, aunque falle de forma cerrada en lo técnico.

### 26.1b Coste, competencias y desencadenantes de revisión

Incluya el coste anual aproximado y las competencias que exige cada alternativa. Una opción que necesita seis personas a tiempo completo para operar con fallo cerrado no es gratuita. Termine el análisis de alternativas con una decisión, las opciones rechazadas con sus motivos y un desencadenante de revisión (reabrir si cambia la ley de residencia de datos). Los costes de cambio importan: un monolito que ya exporta listas de permitidos firmadas puede crecer hacia servicios; un contrato SaaS con excepciones de residencia es más difícil de deshacer en mitad de un incidente. Prefiera las opciones que conservan una salida de emergencia sin conexión para denegar/permitir.

El ADR-011 indica su desencadenante de revisión.

### Nota de campo: supuestos sobre competencias

La vía analítica de la opción B suponía un ingeniero del sitio que entendiera el orden de los eventos. ABP no tenía a esa persona en el turno de noche. Hasta que la contratación se puso al día, Lena mantuvo la aplicación en el camino de escritura con la opción A y limitó B a la investigación diurna sobre réplicas. Una arquitectura que supone competencias no disponibles falla de forma abierta en lo social.

### Ejercicios — capítulo 26

- **EX076 — Criterio.** Añada un criterio para los datos del SIS y puntúe A/B/C. Rúbrica: 3 = criterio sensato + puntuaciones; 2 = criterio; 1 = vago; 0 = nada.
- **EX077 — Rechazar C.** Frase de rechazo con un motivo de residencia/seguridad funcional. Rúbrica: 3 = clara; 2 = parcial; 1 = solo el coste; 0 = acepta C.
- **EX078 — Alternativa de respaldo.** ¿Cuándo es A, puramente local, el modo de ejecución adecuado? Rúbrica: 3 = caída de la WAN / simulacro de aislamiento; 2 = vago; 1 = siempre; 0 = nunca.

### Síntesis del capítulo

Elija la arquitectura frente a restricciones ponderadas; registre las opciones rechazadas.

### Siga estudiando — capítulo 26 de 50

[← Capítulo 25 (borrador)](#ch-25) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 27 (borrador) →](#ch-27)

<a id="ch-27"></a>

## Capítulo 27 — Seguridad de TO, IoT y sistemas ciberfísicos: diseño de controles

### Resultados de aprendizaje

Usted podrá (1) diseñar controles preventivos, detectivos y correctivos para el CNHP; (2) vincular los controles a los requisitos; (3) evitar controles que exijan competencias de explotación para operarlos.

### 27.1 Tres tipos

Preventivo: lista de permitidos antes de reenviar. Detectivo: alerta ante códigos de escritura denegados. Correctivo: desactivar automáticamente una cuenta de ingeniería comprometida al final de la ventana. Cada uno se asocia a un identificador de requisito. En ABP, la lista de permitidos del monitor serie es preventiva, la alerta cuando HMI-1 intenta escribir fuera de 40001 a 40010 es detectiva y la desactivación de las cuentas temporales de ingeniería al final de cada ventana es correctiva. Lena registra el identificador del requisito junto a cada control, para que un revisor pueda ver qué requisito falla si el control se elimina o se debilita.

### 27.2 Competencia del operador

Los controles deben poder operarlos ingenieros que siguen procedimientos operativos, no solo especialistas en explotación. Un control que necesita shellcode a medida para verificarse es el control equivocado para este programa. Lena redacta una entrada de procedimiento para cada control del CNHP que describe cómo comprobarlo con herramientas ordinarias, como reproducir una trama sintética en el banco y leer el registro de decisiones. Si un control solo puede verificarlo alguien que escriba código de explotación, lo sustituye por otro que los propios ingenieros del sitio puedan comprobar con seguridad durante el trabajo rutinario.

### 27.3 Compensación

Si un PLC heredado no puede aplicar listas de permitidos, añada monitorización detectiva y una aprobación humana más estricta para el acceso de ingeniería. Documente la compensación en el permiso de trabajo.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Salida esperada:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

> **Caso sintético — Ashford Batch Plant.** Las escrituras fuera de 40001-40010 se deniegan: un control preventivo con un evento detectivo cuando alguien lo intenta.

En ABP, la compensación se escribe en el permiso de trabajo con un responsable y una fecha de revisión, para que se compruebe en lugar de darse por supuesta. Para un PLC heredado que no puede aplicar una lista de permitidos, Lena combina la monitorización detectiva en su línea troncal con la aprobación de dos personas para el acceso de ingeniería.

### 27.4 Errores y límites

Las pilas de controles compensatorios sin responsable se convierten en alertas ignoradas. El registro de controles de Lena enumera cada control compensatorio de ABP con su responsable, sus alertas y la fecha de su última prueba. Un control sin responsable recibe uno antes de la siguiente ventana, o se retira del registro y su requisito se marca como no cumplido. Los controles que nadie vigila se cuentan como ausentes, porque sus alertas se ignorarán cuando por fin salten. La asignación de responsables se revisa en cada jornada de salud de los controles.

### Nota práctica

Programe una jornada trimestral de salud de los controles: rompa cada control preventivo en un laboratorio sintético y confirme que saltan los controles detectivos. Los controles no probados son deseos.

### 27.1b Responsables y detección del acceso de emergencia

Cada control tiene un responsable que recibe sus alertas y una fecha de revisión. Registre cuándo un operador usa el acceso de emergencia para saltarse la doble aprobación. Un acceso de emergencia sin detección no es más que un control único oculto. La revisión semanal de los eventos de acceso de emergencia forma parte del diseño de controles, y cada revisión nombra quién lo usó y el motivo alegado. La entrada de cada control en el registro indica también cómo falla: que una lista de permitidos rota bloquee el tráfico o lo deje pasar decide qué alerta detectiva debe saltar primero; en la línea troncal del PLC-A es la alerta de política ausente, que avisa al responsable de la ventana.

### Nota de campo: jornada de salud de los controles

En la jornada de salud de marzo, el equipo borró la lista de permitidos de un monitor de banco y confirmó que la alerta detectiva saltaba en 12 segundos. El camino preventivo denegó las escrituras de inmediato. Un control compensatorio de un PLC heredado no tenía responsable; recibió uno antes de la siguiente ventana.

### Ejercicios — capítulo 27

- **EX079 — Mapa.** Un control preventivo y uno detectivo contra la manipulación de la evidencia. Rúbrica: 3 = ambos; 2 = uno; 1 = vago; 0 = nada.
- **EX080 — Operable.** ¿Por qué «verificar volviendo a explotar» es un mal control? Rúbrica: 3 = doble uso + inestable + competencia equivocada; 2 = una razón; 1 = vago; 0 = lo defiende.
- **EX081 — Laboratorio.** ¿Qué regla bloquea HIST-1 fc=16? Rúbrica: 3 = fc-not-allowed; 2 = denegación vaga; 1 = incorrecta; 0 = nada.

### Síntesis del capítulo

Los controles son preventivos, detectivos o correctivos, tienen responsable y se operan sin exploits.

### Siga estudiando — capítulo 27 de 50

[← Capítulo 26 (borrador)](#ch-26) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 28 (borrador) →](#ch-28)

<a id="ch-28"></a>

## Capítulo 28 — Seguridad de TO, IoT y sistemas ciberfísicos: implementación I

### Resultados de aprendizaje

Usted podrá (1) implementar permit() con códigos de motivo explícitos; (2) añadir pruebas para cada cláusula; (3) registrar sin almacenar secretos.

### 28.1 Forma de la implementación

Función pura: entradas origen, código de función, registro y AllowListVersion, y salida (allow: bool, reason: str). Ninguna E/S de red dentro del predicado. Eso mantiene las pruebas rápidas y libres de contacto con la planta. La función de permiso de Lena en ABP sigue exactamente esta forma: recibe los campos de la trama decodificada y la versión de la lista de permitidos y devuelve una decisión con un motivo. La carga de la lista de permitidos y la escritura de los registros ocurren fuera de la función, de modo que sus pruebas se ejecutan en milisegundos con datos sintéticos y nunca corren el riesgo de tocar la planta.

### 28.2 Pruebas por cláusula

Un archivo de pruebas por cláusula: estación permitida, código de función, rango de registros, política no disponible. Solo datos de prueba sintéticos. Mutación: rompa una cláusula y observe cómo falla la prueba.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Salida esperada:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

Lena mantiene un archivo de pruebas por cláusula para la función de permiso de ABP, con datos de prueba que llevan el nombre del requisito que comprueban. Las pruebas de mutación confirmaron que cada archivo falla cuando se rompe su cláusula: borrar la comprobación del rango de registros, por ejemplo, hizo fallar de inmediato las pruebas fuera de rango. Una cláusula cuyas pruebas sobreviven a una mutación se considera no probada.

### 28.3 Registro

Registre la decisión, el motivo, la versión de la política y el actor. No registre contraseñas ni cargas útiles completas de las tramas que puedan contener datos propietarios de recetas. Oculte lo que haga falta.

> **Caso sintético — Ashford Batch Plant.** La implementación I entregó códigos de motivo que muestra la interfaz de la cronología: los operadores vieron por fin por qué se bloqueó una escritura a las 03:12.

Los registros de Lena muestran qué versión de la política tomó cada decisión. Las cargas útiles de las tramas se dejan fuera porque pueden contener valores de recetas. Lena revisa una muestra de registros después de cada versión para confirmar que no se ha colado nada sensible.

### 28.4 Errores y límites

Los motivos tipados como cadenas libres derivan; use una enumeración compartida con el tablero de cobertura. La implementación de Lena usa una lista compartida de códigos de motivo, como register-out-of-range y policy-unavailable, publicada como documento con versión. El tablero de cobertura y la vista de cronología leen la misma lista, de modo que un código nuevo no puede aparecer en los registros sin entenderse en otros lugares. Los consumidores que ven un código desconocido lo tratan como una denegación y generan una alerta para el responsable de la herramienta. El documento se revisa con cada cambio del predicado.

### Nota práctica

Someta el predicado a fuzzing con estaciones y códigos aleatorios y UTF-8 roto. Debe DENEGAR o fallar de forma cerrada, nunca PERMITIR ante un error de análisis.

### 28.1b Catálogo de motivos y fuzzing

El catálogo enumera, para cada código de motivo, la cláusula que lo emite y la prueba que lo fija: fc-not-allowed, register-out-of-range, policy-unavailable, station-unknown. Las entradas de fuzzing que alguna vez encontraron un error se suman a una lista de regresión que se reproduce en cada versión, incluido el nombre de estación UTF-8 que una vez hizo caer el decodificador. Las listas de comprobación de revisión de código para los cambios del predicado incluyen: cláusula nueva, pruebas nuevas, documentación de los códigos de motivo, caso de fuzzing, fallo cerrado ante errores de análisis. Los revisores que se saltan la lista hacen una revisión social, no una revisión de seguridad.

La lista de comprobación de Lena se adjunta a cada revisión del predicado.

### Nota de campo: hallazgos del fuzzing

Un arnés de fuzzing de cinco minutos lanzó un nombre de estación UTF-8 que antes hacía caer el decodificador en una excepción no capturada, que el llamador trataba como ALLOW. La corrección devolvió DENY parse-error, y el arnés se ejecuta ahora en la integración continua con cada cambio del predicado.


### 28.5 Ejemplo resuelto: una prueba de cláusula que detectó un error real (ABP sintética)

Cada cláusula de la función de permiso tiene su propia prueba: origen permitido, código de función permitido, registro dentro de rango, denegación predeterminada. El arnés de fuzzing de Lena alimenta después 10.000 ternas aleatorias (origen, función, registro) tomadas de un generador con semilla y comprueba que cada PASS cumple todas las cláusulas. En la primera ejecución descubrió que el código de función 23 (lectura/escritura de múltiples registros) pasaba para HMI-1 porque la implementación solo comprobaba la mitad de lectura de la solicitud. La corrección rechaza el 23 salvo que figure explícitamente, una prueba de cláusula lo fija ahora y la nota del incidente registra qué semilla reprodujo el fallo, para que cualquiera pueda volver a ejecutarlo.

### Ejercicios — capítulo 28

- **EX082 — Firma.** Firma de tipos de permit y por qué AllowListVersion es un argumento. Rúbrica: 3 = firma + razón de fijar la versión; 2 = firma; 1 = vago; 0 = nada.
- **EX083 — Mutación.** ¿Qué prueba falla si se ignora el rango de registros? Rúbrica: 3 = 40050 espera BLOCK; 2 = vago; 1 = incorrecto; 0 = nada.
- **EX084 — Ocultación.** Dos campos de registro que deben ocultarse. Rúbrica: 3 = p. ej., contraseñas, cargas útiles completas con datos de recetas; 2 = uno; 1 = vago; 0 = nada.

### Síntesis del capítulo

Predicado puro, pruebas por cláusula, registros seguros.

### Siga estudiando — capítulo 28 de 50

[← Capítulo 27 (borrador)](#ch-27) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 29 (borrador) →](#ch-29)

<a id="ch-29"></a>

## Capítulo 29 — Seguridad de TO, IoT y sistemas ciberfísicos: medición

### Resultados de aprendizaje

Usted podrá (1) definir la cobertura con un denominador; (2) separar las métricas de actividad de las de resultado; (3) evaluar detectores con clase de ataque e intervalos (lecciones de Urbina/Giraldo).

### 29.1 La cobertura necesita un plan

La cobertura de ATT&CK for ICS es lo observado intersecado con lo planificado, dividido entre lo planificado; no lo observado dividido entre todas las técnicas. Sin un plan, la cobertura es vanidad. En ABP, Lena redacta antes de cada evaluación el plan de técnicas que se probarán, y el tablero de cobertura cuenta solo esas. Las técnicas observadas fuera del plan se notifican por separado. La cifra de 31 de 44 técnicas planificadas observadas significa algo porque las 44 se eligieron de antemano y la guía de planificación se publica con el tablero. El plan se fija antes de las pruebas.

### 29.2 Actividad frente a resultado

Actividad: tramas decodificadas, herramientas lanzadas. Resultado: correcciones verificadas, alcanzabilidad del SIS todavía falsa, tasa de falsas alarmas con la tasa base de la planta. Dirija según los resultados. El informe mensual del CNHP de Lena empieza por los resultados: correcciones verificadas mediante nueva prueba, si el SIS-B sigue siendo inalcanzable desde L4 y la tasa de falsas alarmas del detector con la tasa base de ABP. Los conteos de actividad, como las tramas decodificadas, aparecen solo en un apéndice de capacidad. Dirigir según la actividad premiaría ejecutar más herramientas en lugar de resolver más problemas. Los resultados son lo que financia el jefe de planta.

### 29.3 Honestidad de los detectores

Informe los intervalos de falsas alarmas, el retardo de detección y la clase de ataque. Un detector de banda que no detecta ataques sigilosos sobre los residuos no equivale a un CUSUM que sí los detecta; el laboratorio lo hace visible.

```python
# Lab 27 - residual CUSUM vs band on batch reactor level (synthetic)
import random
def run(seed, atk, det, k=0.8, h=6.0):
    rng=random.Random(seed); true=est=50.0; s=0.0; alarm=None
    for t in range(500):
        inflow=1.0+rng.gauss(0,0.05)+(0.08 if atk and t>=250 else 0)
        true+=inflow-0.02*true
        lvl=true+rng.gauss(0,0.3); fm=inflow+rng.gauss(0,0.02)
        if atk and t>=250: lvl=50+rng.gauss(0,0.3)
        if atk=="B" and t>=250: fm=1.0+rng.gauss(0,0.02)
        est+=fm-0.02*est
        hit=abs(lvl-50)>2.0 if det=="band" else False
        if det=="cusum":
            s=max(0.0,s+abs(lvl-est)-k); hit=s>h
        if hit and alarm is None: alarm=t
    return alarm
for det in ("band","cusum"):
    fa=sum(run(i,None,det) is not None for i in range(60))
    for atk in ("A","B"):
        hits=[a-250 for a in (run(i,atk,det) for i in range(60)) if a is not None and a>=250]
        print(f"{det} class{atk} FA={fa}/60 det={len(hits)}/60 mean_delay={sum(hits)/len(hits) if hits else float('nan'):.1f}")
```

Salida esperada:

```text
band classA FA=0/60 det=0/60 mean_delay=nan
band classB FA=0/60 det=0/60 mean_delay=nan
cusum classA FA=0/60 det=60/60 mean_delay=24.8
cusum classB FA=0/60 det=0/60 mean_delay=nan
```

> **Caso sintético — Ashford Batch Plant.** El CNHP informa de la cobertura de técnicas planificadas y de las FA/retardo del detector por clase, no de un único porcentaje de «seguro».

El informe piloto de Lena para ABP enumera los resultados por clase de ataque. Cada clase tiene su propio intervalo de falsas alarmas y su retardo medio, de modo que el lector puede ver que el CUSUM detectó los ataques sigilosos sobre los residuos que el detector de banda pasó por alto.

### 29.4 Errores y límites

Los denominadores tomados de otra planta invalidan la métrica. Los ataques sintéticos no son el adversario. Lena nunca toma prestado un denominador del plan de otro sitio, porque las técnicas, los activos y los procesos de ABP son distintos. Si hace falta una comparación con otra planta, ambos sitios deben usar las mismas reglas de planificación, y el informe lo dice. También indica en cada informe que los ataques sintéticos representan clases elegidas, no el comportamiento de un adversario real, para que los lectores no sobrevaloren las cifras de detección. Ambas advertencias aparecen en todos los informes.

### Nota práctica

Ponga a cada widget del tablero un pie con la fórmula y el identificador de la planta. Un widget sin fórmula es decoración y debe eliminarse en la revisión.

### 29.1b Muestreo y comparaciones entre cohortes

Si muestrea 50 de 500 activos, dígalo y no extrapole los hallazgos como si hubiera visitado los 500. Comparar la cobertura entre ventanas exige las mismas reglas de planificación. Publique la guía de planificación junto al tablero de cobertura para que un 71 % en marzo signifique el mismo tipo de denominador que un 71 % en septiembre. La selección de la muestra se registra con su semilla o su regla, para que los mismos activos puedan volver a visitarse en la nueva prueba. Prefiera las métricas que infravaloran el éxito, como contar una corrección solo después de la nueva prueba.

La guía de planificación de ABP se publica junto al tablero.

### Nota de campo: líneas de metodología en los gráficos

Cuando el CNHP cambió las reglas de planificación en junio, los gráficos de estilo Pulse incorporaron una línea vertical etiquetada methodology_id=2026-06. La dirección dejó de comparar el 80 % de mayo con el 70 % de julio como si tuvieran el mismo denominador. La honestidad en la leyenda del gráfico evitó un relato falso de declive.

### Ejercicios — capítulo 29

- **EX085 — Fórmula.** Escriba la fórmula de la cobertura y explique un mal denominador. Rúbrica: 3 = denominador planificado + ejemplo del mal uso de todas las técnicas de ICS; 2 = fórmula; 1 = vanidad; 0 = nada.
- **EX086 — Laboratorio.** Compare en una frase la banda y el CUSUM en la clase A. Rúbrica: 3 = el CUSUM detecta, la banda no, FA de ambos 0 en la muestra; 2 = parcial; 1 = incorrecto; 0 = nada.
- **EX087 — Infravalorar.** Un diseño que infravalore el éxito. Rúbrica: 3 = exigir nueva prueba antes de cerrar; 2 = parcial; 1 = vago; 0 = nada.

### Síntesis del capítulo

Planifique el denominador; mida los resultados; evalúe los detectores por clase con intervalos.

### Siga estudiando — capítulo 29 de 50

[← Capítulo 28 (borrador)](#ch-28) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 30 (borrador) →](#ch-30)

<a id="ch-30"></a>

## Capítulo 30 — Laboratorio de verificación I

### Resultados de aprendizaje

Usted podrá (1) ejecutar un plan de verificación sobre el monitor y la zonificación de ABP; (2) registrar aprobado/suspenso con hashes de evidencia; (3) detener el laboratorio si falla una prueba de seguridad funcional.

### 30.1 Plan

Pruebas: permitir las lecturas dentro del alcance; denegar los códigos de función indebidos; denegar las escrituras fuera de rango; fallo cerrado si falta la política; la alcanzabilidad del SIS desde L4 es falsa; tiempo de ciclo dentro del presupuesto con la derivación. Cada fila: identificador, preparación, acción, resultado esperado, ruta de la evidencia. En ABP, cada fila del plan nombra el requisito que comprueba, como S-1 para la fila de política ausente y R-12 para la fila de alcanzabilidad. La fila del tiempo de ciclo usa la copia de banco de la línea troncal hacia el PLC-A con la derivación instalada y comprueba que el tiempo se mantiene muy por debajo de la parada de 50 ms. Las filas se escriben antes de ejecutar el laboratorio.

### 30.2 Ejecución

Use solo equipos y bancos sintéticos. Capture la salida estándar y los hashes de configuración. Cualquier fallo de seguridad funcional (fallo abierto o SIS alcanzable) detiene el laboratorio y abre un bloqueante: no se continúa para reunir datos.

```python
# Lab 23 - reachability count on a synthetic Purdue-layered OT network
# Nodes: L5-ERP, L4-Office, L3.5-DMZ, L3-Hist, L2-SCADA, L1-PLC, L1-SIS, L0-IO
edges_flat=[("L5","L4"),("L4","L3"),("L3","L2"),("L2","L1-PLC"),("L2","L1-SIS"),("L1-PLC","L0"),("L1-SIS","L0"),("L4","L2")]
edges_zoned=[("L5","L4"),("L4","L3.5"),("L3.5","L3"),("L3","L2"),("L2","L1-PLC"),("L1-SIS","L0"),("L1-PLC","L0")]  # SIS not reachable from SCADA
def reach(edges, start):
    g={}; 
    for a,b in edges: g.setdefault(a,[]).append(b)
    seen=set(); stack=[start]
    while stack:
        n=stack.pop()
        if n in seen: continue
        seen.add(n); stack.extend(g.get(n,[]))
    return seen
for name,e in (("flat",edges_flat),("zoned",edges_zoned)):
    r=reach(e,"L4")
    print(f"{name}: L4 reaches {sorted(r)} count={len(r)} writes_to_SIS={'L1-SIS' in r}")
```

Salida esperada:

```text
flat: L4 reaches ['L0', 'L1-PLC', 'L1-SIS', 'L2', 'L3', 'L4'] count=6 writes_to_SIS=True
zoned: L4 reaches ['L0', 'L1-PLC', 'L2', 'L3', 'L3.5', 'L4'] count=6 writes_to_SIS=False
```

El laboratorio de Lena en ABP se ejecuta en el entorno de banco con equipos y datos de prueba sintéticos. Cuando la fila de política ausente falló una vez, el laboratorio se detuvo y se abrió un bloqueante contra S-1; no se ejecutaron más filas hasta corregirlo, porque continuar habría producido resultados sobre un monitor que ya se sabía inseguro.

### 30.3 Informe

Informe de laboratorio de una página: versiones del entorno, tabla de resultados, bloqueantes abiertos, aprobación. Adjunte los hashes.

> **Caso sintético — Ashford Batch Plant.** El laboratorio I falló una vez en la fila de política ausente; la publicación de la versión se detuvo hasta corregir S-1.

El informe de Lena para cada ejecución del laboratorio I enumera las versiones de las herramientas, el hash del conjunto de datos de prueba, el resultado de cada fila y los bloqueantes abiertos, y lo firma el ejecutor independiente. Se adjuntan los hashes de los registros y de las exportaciones, para que un revisor pueda confirmar que la evidencia coincide con lo ejecutado. Un informe sin hashes no es evidencia.

### 30.4 Errores y límites

Los laboratorios en bancos compartidos chocan entre sí; reserve el entorno sintético. Lena reserva en el calendario compartido el entorno de banco de ABP para cada ejecución del laboratorio, con la versión en prueba indicada en la reserva. Una vez, dos equipos ejecutaron compilaciones distintas en el mismo banco en horarios solapados, y sus registros se volvieron imposibles de separar. Desde entonces, una ejecución sin reserva no cuenta como evidencia de versión, y el banco se restablece a un estado conocido antes de cada ejecución reservada. Reservar lleva minutos.

### Nota práctica

El laboratorio I lo ejecuta alguien que no implementó el cambio en prueba. El aprobado registrado necesita una lista de comprobación en verde independiente.

### 30.1b Datos de prueba de referencia e inventario

Mantenga un directorio sellado de datos de prueba sintéticos con decisiones esperadas conocidas. Las ejecuciones del laboratorio deben coincidir por hash con el conjunto de datos de prueba antes de contar como evidencia de versión. Fotografíe o exporte el inventario del entorno del laboratorio al informe. «Pasó en mi máquina» sin inventario no es una evidencia transferible. Los cambios en los datos de prueba se revisan como el código: una nueva decisión esperada debe nombrar el requisito del que procede. Los registros de resultados del laboratorio son evidencia; consérvelos con la etiqueta de la versión.

El conjunto de datos de prueba de Lena está sellado y tiene hash.

### Nota de campo: verde independiente

El autor de una corrección urgente se ofreció a ejecutar el laboratorio I para ganar tiempo. El revisor se negó, ejecutó personalmente las filas de seguridad funcional y encontró un camino que seguía dando ALLOW cuando el archivo de política era un directorio en lugar de un archivo. Los ejecutores independientes detectan los supuestos que los autores dejan de ver.


### 30.5 Ejemplo resuelto: leer con honestidad un resultado de laboratorio (ABP sintética)

El laboratorio I reproduce un día grabado de tráfico de ABP más 40 intentos de escritura inyectados a través de la función de permiso y de la lógica de alarmas. Resultados: 40 de 40 escrituras inyectadas bloqueadas; 2 escrituras de ingeniería legítimas bloqueadas porque la estación de ingeniería faltaba en la lista de permitidos durante la puesta en marcha; 0 alarmas suprimidas. Lena informa de los dos bloqueos falsos como un defecto de diseño, no como ruido —en una planta en servicio habrían detenido un cambio de receta programado— y añade un conjunto de vectores para el modo de puesta en marcha. El informe del laboratorio indica lo que no se probó: el rendimiento bajo carga, los enlaces serie y el SIS-B, que queda fuera del alcance por diseño.

### Ejercicios — capítulo 30

- **EX088 — Fila.** Escriba la fila de laboratorio del fallo cerrado. Rúbrica: 3 = fila completa; 2 = parcial; 1 = vago; 0 = nada.
- **EX089 — Parada.** ¿Qué ocurre si el SIS es alcanzable desde L4? Rúbrica: 3 = parada, bloqueante, ningún uso en planta; 2 = solo una nota; 1 = continuar; 0 = nada.
- **EX090 — Evidencia.** Tres hashes que adjuntar. Rúbrica: 3 = política, binario/versión, registro de resultados; 2 = dos; 1 = uno; 0 = nada.

### Síntesis del capítulo

Verifique primero la seguridad funcional; deténgase ante un fallo abierto o una exposición del SIS; calcule el hash de todo.

### Siga estudiando — capítulo 30 de 50

[← Capítulo 29 (borrador)](#ch-29) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 31 (borrador) →](#ch-31)

<a id="ch-31"></a>

## Capítulo 31 — Seguridad de TO, IoT y sistemas ciberfísicos: implementación II

### Resultados de aprendizaje

Usted podrá (1) añadir inserciones o actualizaciones idempotentes de hallazgos; (2) aplicar la validación del esquema en la escritura; (3) versionar las respuestas de la API de las herramientas del CNHP.

### 31.1 Inserción o actualización

PUT /findings/{id} con el cuerpo completo; el mismo id dos veces produce una sola fila. Las huellas de deduplicación proponen identificadores; las personas confirman las fusiones entre causas raíz distintas. En ABP, los identificadores de los hallazgos los genera el cliente al crearlos y se reutilizan en cada reintento, de modo que un fallo de red a mitad de la solicitud no puede crear un duplicado. Las huellas sugieren cuándo dos hallazgos pueden ser el mismo problema, pero una persona confirma cualquier fusión, porque dos hallazgos sobre el PLC-A pueden compartir un registro y tener aun así causas distintas. Las fusiones se registran con sus motivos.

### 31.2 Validar en la escritura

Rechace los campos desconocidos y los nombres prohibidos; fuerce la severidad a través de una enumeración. Los errores de validación devuelven códigos legibles por máquina. El almacén de hallazgos de Lena en ABP rechaza cualquier registro con un campo desconocido o un nombre prohibido, como payload o password, y devuelve un código que indica qué campo falló. La severidad solo acepta los valores acordados. El mismo validador se ejecuta en las creaciones interactivas y en las importaciones masivas, de modo que ninguna vía de entrada goza de más confianza que otra, y una importación de un escáner que envía risk_score se rechaza con el mismo código que el cliente móvil. Los errores se documentan con ejemplos.

### 31.3 Versionado de la API

Prefijo /v1/; dentro de v1, solo cambios aditivos. Los cambios incompatibles requieren /v2/ y una nota de migración.

> **Caso sintético — Ashford Batch Plant.** Un cliente móvil envió risk_score; el validador lo rechazó: las puntuaciones vacías se quedan fuera (capítulo 15).

La API de Lena para ABP se ha mantenido en v1 hasta ahora. Lena publica la regla de cambios aditivos en la documentación de la API, y la integración continua compara cada esquema nuevo con la última versión para detectar campos eliminados o renombrados. Si alguna vez fuera necesario un cambio incompatible, v1 seguiría funcionando junto a v2 durante un periodo anunciado, para que los clientes móviles y las importaciones de escáneres puedan migrar sin fallar en mitad de una ventana.

### 31.4 Errores y límites

Las claves de idempotencia no deben derivarse solo de la hora del reloj. Una clave de idempotencia construida a partir de la hora actual cambia entre reintentos, así que cada reintento parece una solicitud nueva y crea un duplicado. Los clientes de Lena generan la clave una vez por operación lógica, la guardan con la solicitud pendiente y la reutilizan hasta que el servidor confirma el éxito. La regla se documenta con la API y las bibliotecas cliente la aplican, de modo que ningún desarrollador puede reintroducir el atajo basado en la hora. Las revisiones comprueban esta regla de forma explícita.

### Nota práctica

La importación masiva desde escáneres debe pasar la misma validación de esquema que la creación interactiva, incluidas las comprobaciones de campos prohibidos.

### 31.1b Actualizaciones parciales y concurrencia

Un PATCH que permite cambiar la severidad sin referencias a la evidencia invita a rebajas silenciosas. Prefiera un PUT completo del cuerpo validado, o un PATCH restringido que no pueda borrar los hashes de la evidencia ni cambiar el estado a cerrado sin un puntero a una nueva prueba. Use ETags para que dos personas que corrigen no se pisen. Un cambio de estado a cerrado solo se acepta cuando la misma solicitud lleva un puntero a una nueva prueba. Los borrados masivos están prohibidos sin doble control. Documente la semántica de inserción o actualización en OpenAPI para que los clientes móviles no inventen identificadores de reintento.

Las ETags son obligatorias en cada actualización de un hallazgo.

### Nota de campo: incidente de importación masiva

Una vía de importación de escáneres se saltaba las comprobaciones de campos prohibidos porque se consideraba de confianza. El campo de notas de alguien contenía una contraseña. Tras limpiarla y rotarla, la importación masiva se reconectó a través del mismo validador que la creación interactiva. La importación de confianza es la forma en que las cargas útiles entran en los almacenes sellados.



Los clientes que omiten el identificador del hallazgo al crearlo reciben un 400 con un enlace a la documentación de inserción o actualización, para que los reintentos no puedan inventar duplicados por accidente.


### 31.5 Ejemplo resuelto: inserción o actualización idempotente de registros de activos (ABP sintética)

Dos fuentes de inventario informan sobre el PLC-A: la exportación del proyecto de ingeniería y el descubrimiento pasivo en la red. La inserción o actualización de Lena se indexa por (sitio, etiqueta del activo), no por dirección IP, porque la IP cambia cuando se sustituye un controlador. Cada escritura lleva la fuente y una hora de observación; una observación posterior actualiza la versión del firmware solo si su fuente es autoritativa para ese campo (la exportación del proyecto gana para el firmware; el descubrimiento gana para «visto por última vez»). Reproducir dos veces la misma importación no produce ningún cambio: es la prueba que demuestra la idempotencia. Sin estas reglas, una importación masiva sobrescribió una vez el campo de firmware del PLC-A con «unknown» y lo ocultó a una comprobación de avisos de seguridad.

### Ejercicios — capítulo 31

- **EX091 — Inserción o actualización.** ¿Por qué un POST sin id es arriesgado ante los reintentos? Rúbrica: 3 = duplicados al reintentar; 2 = vago; 1 = incorrecto; 0 = nada.
- **EX092 — Rechazo.** Cuerpo JSON que debe recibir un 400. Rúbrica: 3 = contiene payload/password/risk_score; 2 = débil; 1 = cuerpo válido; 0 = nada.
- **EX093 — Versión.** ¿Es seguro en v1 renombrar reason_code a reason? Rúbrica: 3 = no, es incompatible, va a v2; 2 = dubitativo; 1 = sí; 0 = nada.

### Síntesis del capítulo

Escrituras idempotentes, esquema estricto, versiones explícitas.

### Siga estudiando — capítulo 31 de 50

[← Capítulo 30 (borrador)](#ch-30) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 32 (borrador) →](#ch-32)

<a id="ch-32"></a>

## Capítulo 32 — Seguridad de TO, IoT y sistemas ciberfísicos: fiabilidad

### Resultados de aprendizaje

Usted podrá (1) fijar objetivos de disponibilidad para las herramientas de seguridad de TO; (2) usar reintentos con presupuestos que respeten el tiempo de ciclo; (3) degradarse de forma segura cuando falla una dependencia.

### 32.1 Objetivos

Camino de permitir/denegar durante las ventanas: alta disponibilidad. Tableros de cobertura: mejor esfuerzo. Enuncie el objetivo; no insinúe cinco nueves sin un presupuesto. En ABP, el camino de denegación del monitor serie debe funcionar durante toda la ventana, mientras que el tablero de cobertura puede estar caído una hora sin daño. Lena pone por escrito ambos objetivos con el presupuesto que respalda cada uno, para que nadie suponga que el tablero necesita el mismo cuidado que la aplicación de las decisiones, ni que la aplicación puede tolerar las caídas del tablero. Los objetivos se revisan cada año.

### 32.2 Reintentos

Los reintentos ayudan con las subidas inestables de evidencia, pero necesitan un plazo para que se mantenga el presupuesto de la línea troncal. Limite el total de intentos. El cargador de evidencia de Lena en ABP reintenta con retardos crecientes y se rinde tras un número fijo de intentos o un plazo, lo que ocurra primero. Las subidas fallidas quedan en cola en el disco y se notifican, de modo que no se pierde nada. Los reintentos nunca se ejecutan en la línea troncal hacia el PLC-A, donde podrían desplazar el tráfico de control y romper el presupuesto de ciclo. Los límites están escritos en el permiso.

### 32.3 Degradación segura

Si el almacén de hallazgos está caído, siga denegando/permitiendo localmente y encole los borradores en el disco; nunca falle de forma abierta en las comprobaciones de política.

> **Caso sintético — Ashford Batch Plant.** Durante una caída del almacén de hallazgos, la cola del portátil de Lena retuvo los borradores; el monitor serie siguió denegando las escrituras fuera de rango.

Lena prueba este modo degradado en el laboratorio II, en el banco. Durante una caída real del almacén de hallazgos, los borradores se encolaron en el portátil de Lena y el monitor serie siguió denegando las escrituras fuera de rango. Tras cada caída, Lena confirma que todos los borradores encolados llegaron al almacén comparando los conteos con el registro de la cola.

### 32.4 Errores y límites

Los reintentos contra una línea troncal con límite de tasa pueden parecer inundaciones; coordine los presupuestos con el permiso de trabajo. El permiso de trabajo de Lena en ABP indica la tasa máxima de solicitudes de cualquier tráfico de evaluación en cada línea troncal, incluidos los reintentos. Si los reintentos la superaran, la herramienta espera. Antes de una ventana se coordina con el equipo de monitorización del sitio, para que una ráfaga de reintentos no se confunda con un ataque ni desencadene una respuesta a incidentes innecesaria. Las tasas se fijan con los ingenieros de control. Se revisan cada año.

### Nota práctica

Cuando la cola de borradores supere un umbral, deje de iniciar nuevos métodos de descubrimiento y avise al responsable. Los escaneos sin seguimiento mientras no se pueden registrar hallazgos crean riesgo.

### 32.1b Presupuestos de error y comprobaciones de salud

Defina presupuestos de error para el camino de denegación separados de los presupuestos de mejor esfuerzo de la interfaz. Compruebe la salud del almacenamiento de políticas y del receptor de eventos al inicio de la ventana. Empezar una ventana a ciegas y descubrir un receptor roto a mitad de un escaneo es un fallo de operaciones que este capítulo pretende evitar. Una comprobación de salud fallida retrasa el inicio de la ventana; las comprobaciones nunca se acortan para ganar tiempo. Los experimentos de caos se ejecutan solo en entornos sintéticos, nunca durante la ventana firmada de un cliente. Registre los identificadores de los experimentos por separado de los de las ventanas para que las métricas no se mezclen. Publique ambos presupuestos de error, el del camino de denegación y el de la interfaz.

### Nota de campo: contrapresión de la cola

Cuando la cola de borradores llegó a 50 durante una caída del almacén, el descubrimiento de estilo Track se detuvo automáticamente y avisó a Lena. Permitir/denegar siguió funcionando. El umbral de 50 se eligió para que la cola retenga una noche completa de borradores con margen de sobra.


### 32.5 Ejemplo resuelto: degradarse de forma segura cuando falla el recolector (ABP sintética)

El recolector de monitorización del CNHP está en un puerto espejo. Si falla, nada en el proceso debería cambiar: el diseño mantiene el recolector fuera de todo camino de control. Los objetivos de fiabilidad de Lena se refieren a la evidencia, no a la producción: 99,5 % de disponibilidad de captura al mes y alertas ante pérdidas superiores al 0,1 %. Los reintentos hacia el almacén central usan un retroceso exponencial con tope, para que una caída del almacén no inunde el enlace de la DMZ compartido con la réplica del historiador. Cuando la cola se llena, el recolector descarta los paquetes en bruto más antiguos pero conserva los registros resumidos, y genera una alerta de «visibilidad degradada» para que los analistas sepan que la ausencia de alertas significa menos.

### Ejercicios — capítulo 32

- **EX094 — Objetivo.** Frase de disponibilidad para el camino de denegación. Rúbrica: 3 = objetivo por ventana + medida; 2 = «alta» vaga; 1 = broma de los cinco nueves; 0 = nada.
- **EX095 — Degradación.** ¿Qué nunca debe degradarse a ALLOW? Rúbrica: 3 = las decisiones de política/lista de permitidos; 2 = parcial; 1 = la interfaz; 0 = incorrecto.
- **EX096 — Cola.** Regla de contrapresión cuando la cola de borradores es larga. Rúbrica: 3 = detener el nuevo descubrimiento + avisar; 2 = parcial; 1 = ignorar; 0 = nada.

### Síntesis del capítulo

Denegaciones fiables, reintentos con presupuesto, degradación hacia el cierre.

### Siga estudiando — capítulo 32 de 50

[← Capítulo 31 (borrador)](#ch-31) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 33 (borrador) →](#ch-33)

<a id="ch-33"></a>

## Capítulo 33 — Seguridad de TO, IoT y sistemas ciberfísicos: seguridad funcional y resiliencia

### Resultados de aprendizaje

Usted podrá (1) escribir las condiciones de parada como comprobaciones ejecutables; (2) planificar la reversión de cambios de herramientas a mitad de ventana; (3) dirigir un ejercicio de mesa sobre un fallo de la lista de denegados o del tiempo de ciclo.

### 33.1 Paradas ejecutables

Las condiciones de parada son código: canario del tiempo de ciclo, flujo de alarmas de proceso, archivo de interruptor de corte del cliente, entrada de falla del SIS. Las personas también ordenan parar; el software no debe contradecir una parada humana. En ABP, la lógica de parada del monitor serie lee el canario del tiempo de ciclo, el flujo de alarmas de proceso, un archivo de interruptor de corte y la entrada de falla del SIS-B. Cualquiera de ellos detiene de inmediato la actividad de evaluación. Una orden humana de parar siempre gana, y el software no tiene ninguna opción que pueda anularla o retrasarla hasta que termine un trabajo en curso.

### 33.2 Reversión

Fije las versiones; conserve firmado el binario anterior del monitor. Si una compilación nueva evalúa mal las listas de permitidos, revierta en minutos. Lena conserva la compilación firmada anterior del monitor en el banco y en el kit de la ventana, de modo que la reversión es una orden probada, no una recompilación. La reversión se ensayó antes de la primera ventana en planta y se repite tras cada versión importante. Una reversión restaura tanto el binario como la versión de la lista de permitidos que se ejecutaba con él. La reversión restaura el estado anterior en minutos. Ambos están fijados.

### 33.3 Ejercicio de mesa

Recorra un escenario: el tiempo de ciclo supera 50 ms a las 02:40; a quién se llama; qué se dice; cuándo se permite reanudar. Actualice el procedimiento operativo donde el ejercicio se atascó.

> **Caso sintético — Ashford Batch Plant.** El ejercicio de mesa reveló que la ruta del archivo de interruptor de corte no estaba documentada; la versión 1.4 del procedimiento lo corrigió antes de la siguiente ventana.

Los ejercicios de mesa de ABP se realizan cada periodo lectivo con el jefe de turno presente, y cada laguna que revelan se cierra con una nueva versión del procedimiento antes de la siguiente ventana. Cada escenario nombra a quién se llama, qué se le dice y quién puede autorizar la reanudación del trabajo.

### 33.4 Errores y límites

El teatro de la resiliencia es una carpeta que nadie abre. Haga un simulacro por periodo lectivo. Los simulacros de resiliencia de Lena en ABP se hacen una vez por periodo lectivo, usan el procedimiento real e incluyen al menos una parada y una reversión. Cada simulacro produce al menos una modificación del procedimiento o un motivo registrado de por qué no hizo falta ninguna. Una carpeta que no se ha abierto desde la última auditoría se trata como no probada, por completa que parezca en la estantería. Los resultados de los simulacros se archivan con la versión del procedimiento. Las lagunas reciben responsables.

### Nota práctica

Redacte de antemano plantillas de SMS/correo electrónico para la parada, la reanudación y la reversión. Bajo estrés, la gente omite la versión del permiso de trabajo o la hora del siguiente punto de control.

### 33.1b Contactos secundarios y autoridad de reanudación

Las condiciones de parada que avisan a una sola persona fallan cuando esa persona está desconectada. Mantenga contactos primarios y secundarios con un traspaso confirmado. ¿Quién puede reanudar tras una parada? Nombre el rol en el permiso de trabajo. El monitor debería exigir un testigo de reanudación vinculado a ese rol y a AllowListVersion. Tras cada parada real, haga una revisión en caliente de cinco minutos y registre al menos una modificación del procedimiento. Las notas de la revisión en caliente registran el desencadenante, el tiempo hasta la parada y el tiempo hasta la reanudación, para poder comparar los simulacros con las paradas reales.

### Nota de campo: testigo de reanudación

Tras una parada, la reanudación exigió un testigo emitido para el rol del contacto de seguridad de procesos y vinculado a AllowListVersion v1.4.2. Se eliminó de la interfaz un interruptor booleano en el servidor de salto. Reanudar sin autoridad es la forma en que las condiciones de parada se vuelven opcionales.


### 33.5 Ejemplo resuelto: una parada ejecutable durante la puesta en marcha (ABP sintética)

Durante la migración del cortafuegos en el conducto L3–L2, la condición de parada dice: «Si el HMI pierde los valores del PLC-A durante más de 10 segundos, o se produce cualquier disparo del SIS-B, revertir al conjunto de reglas anterior». La reversión es una única orden preparada de antemano y probada dos veces el día anterior, y el jefe de turno tiene la autoridad para ordenarla; el ingeniero no discute. Reanudar exige un testigo escrito del jefe de turno una vez comprendida la causa. Por separado, Lena confirma que el disparo por nivel alto del SIS-B en R-101 está cableado y no se ve afectado por el cambio, en coherencia con la expectativa de IEC 61511 de que la función de seguridad siga siendo independiente.

### Ejercicios — capítulo 33

- **EX097 — Interruptor de corte.** Diseñe un interruptor de corte humano que se respete en ≤30 s. Rúbrica: 3 = mecanismo + sondeo + fallo cerrado; 2 = idea; 1 = vago; 0 = nada.
- **EX098 — Reversión.** Tres condiciones previas para revertir a mitad de ventana. Rúbrica: 3 = binario anterior, política fijada, aviso a seguridad de procesos; 2 = dos; 1 = una; 0 = nada.
- **EX099 — Inyección.** Una inyección para el ejercicio de mesa. Rúbrica: 3 = específica; 2 = vaga; 1 = ninguna; 0 = insegura.

### Síntesis del capítulo

Paradas que se pueden ejecutar, reversiones que se pueden hacer, ejercicios de mesa que actualizan los procedimientos.

### Siga estudiando — capítulo 33 de 50

[← Capítulo 32 (borrador)](#ch-32) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 34 (borrador) →](#ch-34)

<a id="ch-34"></a>

## Capítulo 34 — Seguridad de TO, IoT y sistemas ciberfísicos: integración

### Resultados de aprendizaje

Usted podrá (1) integrar los eventos del monitor en el almacén de hallazgos; (2) definir consumidores idempotentes; (3) probar los contratos con datos de prueba.

### 34.1 Contrato de eventos

Eventos de denegar/permitir: versión del esquema, identificadores, marcas de tiempo UTC, origen, fc, registro, motivo, versión de la política. Los consumidores ignoran los campos desconocidos; los productores solo hacen cambios aditivos. El contrato de eventos de Lena en ABP tiene versión y se publica con datos de prueba para cada código de motivo. Cada evento lleva tanto la hora en que ocurrió como la hora en que se recibió, además de la fuente del reloj. Los productores pueden añadir campos, pero nunca eliminarlos ni renombrarlos dentro de una versión, de modo que los consumidores antiguos siguen funcionando. Los datos de prueba se guardan en el repositorio. Los cambios se revisan.

### 34.2 Consumidores idempotentes

El almacén de hallazgos indexa los eventos procesados por event_id. Reproducir el registro no debe crear hallazgos duplicados. Lena prueba la reproducción en el banco pasando dos veces por el consumidor el registro de eventos de un día completo y comprobando que el número de hallazgos no cambia. La prueba detectó un error en el que los eventos se indexaban por marca de tiempo en lugar de por event_id, lo que duplicó tres tickets durante una tormenta de reproducción antes de que llegara la corrección. Las pruebas de reproducción se ejecutan en la integración continua. Los fallos bloquean la fusión. La prueba se ejecuta cada noche.

### 34.3 Pruebas de contrato

JSON de datos de prueba para cada código de motivo; las pruebas del consumidor comprueban los campos del ticket resultante. Se ejecutan en la integración continua con datos de prueba sintéticos.

> **Caso sintético — Ashford Batch Plant.** Una tormenta de reproducción duplicó tres tickets hasta que llegó la idempotencia por event_id.

Las pruebas de contrato de Lena se ejecutan con cada solicitud de incorporación de cambios y de forma programada. Usan un dato de prueba para cada código de motivo y comprueban los campos del ticket que debería crear el consumidor, como el activo, la técnica y la severidad. Una ejecución programada contra el entorno de preproducción detecta los cambios de los productores aunque no haya ninguna solicitud abierta, de modo que la deriva se encuentra antes de una ventana y no durante ella.

### 34.4 Errores y límites

El desfase de los relojes enturbia las cronologías; prefiera la hora del evento más la hora de recepción. La vista de cronología de Lena en ABP muestra la hora del evento y la hora de recepción una al lado de la otra, para que el lector pueda ver cuándo el reloj de un dispositivo está mal. El laboratorio II inyectó más adelante un desfase de 90 segundos en el PLC-A y descubrió que dos eventos quedaban mal ordenados en el expediente hasta que se aplicó una corrección del desplazamiento. Las fuentes de reloj se registran en cada evento precisamente por esta razón. Lena mantiene los relojes sincronizados cuando es posible. La deriva genera alarma.

### Nota práctica

Los eventos envenenados (marcas de tiempo futuras, versiones de política desconocidas) van a una cola de mensajes fallidos con una alerta: no a los hallazgos ni a /dev/null.

### 34.1b Mensajes fallidos y simulacros de esquema

Cada evento enviado a la cola de mensajes fallidos conserva el error de validación que lo rechazó. Los operadores lo reproducen tras corregir el productor. Practique de extremo a extremo, en un ensayo, la adición de un campo opcional: productor, consumidor, datos de prueba, documentación. Los equipos que solo hacen evolucionar los esquemas en emergencias inventan atajos incompatibles. Una ejecución programada fallida abre un ticket para el equipo productor, no para el consumidor. La antigüedad de los mensajes fallidos es un gráfico de SLO junto a la latencia del camino de denegación.

ABP realiza un simulacro de esquema cada periodo lectivo. Los resultados de los simulacros se registran con las versiones del productor y del consumidor implicadas, como el simulacro que añadió la hora de recepción junto a la hora del evento en los eventos de denegación del PLC-A.

### Nota de campo: cuarentena de eventos envenenados

Un error de un productor emitió eventos con marcas de tiempo de 2099. La cuarentena de mensajes fallidos los atrapó; no se creó ningún hallazgo contra equipos aleatorios. Los descartes invisibles habrían sido peores: al menos la cuarentena avisa a alguien.



Incluya un canario del consumidor que haga fallar el despliegue si los eventos envenenados no se ponen en cuarentena en menos de un minuto en preproducción.



Cada simulacro termina con el nuevo campo visible en un ticket de preproducción para una denegación sintética del PLC-A, y con la duración del simulacro registrada.


### 34.5 Ejemplo resuelto: integrar las alertas con el sistema de mantenimiento (ABP sintética)

Las alertas del CNHP fluyen hacia el sistema de gestión del mantenimiento de ABP para que una alerta de «descarga de programa al PLC-A» pueda asociarse a una orden de trabajo abierta. El contrato de eventos lleva un identificador de evento, la etiqueta del activo, la técnica de ATT&CK for ICS (T0843 Program Download), la hora con la fuente del reloj y el hash de la evidencia. El consumidor es idempotente respecto al identificador de evento, de modo que una alerta reproducida no crea dos órdenes de trabajo. Las pruebas de contrato se ejecutan en la integración continua con datos de prueba de ambas partes; un evento sin el campo de técnica se envía a una cola de mensajes fallidos y se revisa a diario, en lugar de descartarse. Una descarga sin orden de trabajo asociada se escala al jefe de turno en menos de cinco minutos.

### Ejercicios — capítulo 34

- **EX100 — Campo.** ¿Por qué incluir policy_version en cada evento? Rúbrica: 3 = auditar qué reglas se aplicaron; 2 = vago; 1 = incorrecto; 0 = nada.
- **EX101 — Reproducción.** ¿Cómo evita event_id los hallazgos duplicados? Rúbrica: 3 = inserción o actualización / ignorar duplicados; 2 = vago; 1 = incorrecto; 0 = nada.
- **EX102 — Datos de prueba.** Dos datos de prueba necesarios antes de un nuevo código de motivo. Rúbrica: 3 = ejemplo del productor + ticket esperado del consumidor; 2 = uno; 1 = vago; 0 = nada.

### Síntesis del capítulo

Contratos, consumidores idempotentes, pruebas con datos de prueba.

### Siga estudiando — capítulo 34 de 50

[← Capítulo 33 (borrador)](#ch-33) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 35 (borrador) →](#ch-35)

<a id="ch-35"></a>

## Capítulo 35 — Taller de diseño II

### Resultados de aprendizaje

Usted podrá (1) rediseñar la interfaz de cobertura del CNHP según los principios de infravalorar el éxito; (2) defender el diseño en una revisión; (3) redactar textos de interfaz que rechacen las puntuaciones vacías.

### 35.1 Problema

Las partes interesadas quieren un gran porcentaje verde. Diseñe una interfaz que muestre lo planificado, lo observado y lo no visto, y que rechace una puntuación de seguridad única. En ABP, el jefe de planta pidió al principio un único porcentaje que mostrara si el CNHP funcionaba. El equipo de Lena explicó que cualquier cifra única mezclaría las técnicas observadas, la deriva de los conductos y la alcanzabilidad del SIS-B, que necesitan responsables y presupuestos distintos. La pantalla resultante da a cada medida su propia línea con el denominador visible, y las técnicas planificadas pero no vistas se enumeran por identificador para que el jefe pueda preguntar cuáles importan antes de aprobar la siguiente fase.

### 35.2 Textos

«71 % de las técnicas de ICS planificadas observadas: no es una puntuación de riesgo residual». Botón: exportar denominador. Muestre «¿SIS alcanzable?» como un sí/no aparte. El equipo de Lena probó esta redacción con el jefe de planta y dos jefes de turno antes de publicarla. Un jefe de turno leyó un borrador inicial que decía solo «setenta y uno por ciento» y supuso que la planta era segura en un setenta y uno por ciento, que es exactamente la mala lectura que evita la advertencia. El botón de exportar produce la lista de las 44 técnicas planificadas, cada una marcada como observada o no vista, y la línea del SIS-B nunca muestra un porcentaje, porque la alcanzabilidad es verdadera o falsa el día de la comprobación.

### 35.3 Revisión

Los revisores intentan imponer una insignia de riesgo rojo/amarillo/verde; el taller debe mantenerse firme con las reglas del capítulo de medición.

> **Caso sintético — Ashford Batch Plant.** El taller II eliminó la insignia; el tablero enumera por identificador las técnicas planificadas no vistas y, por separado, la alcanzabilidad del SIS.

Los críticos del taller argumentaron que los directivos no leerían una lista. El equipo de Lena respondió con la decisión real del jefe: qué conductos financiar y cerrar a continuación, algo que un color no puede expresar. La insignia eliminada tampoco tenía una regla definida para pasar a amarillo, así que dos revisores ya habían discrepado sobre su color con los mismos datos. Sustituirla por elementos nombrados zanjó esa discusión y dio a cada elemento un responsable.

### 35.4 Errores y límites

Los patrones oscuros («solo para directivos») reintroducen las puntuaciones vacías: rechácelos mediante CODEOWNERS de la interfaz. En ABP, una solicitud posterior pidió una vista resumida solo para directivos con un único indicador de color. El equipo de Lena la rechazó durante la revisión de código, citando la decisión del taller y las reglas de medición, y ofreció en su lugar una exportación de una página con los mismos tres números y sus denominadores. Exigir que un responsable de código apruebe cada cambio en la interfaz del tablero hace que esta discusión la resuelva un revisor nombrado que conoce la historia, en lugar de que la reabra en silencio quien edite la pantalla a continuación.

### Nota práctica

Tarea de investigación con usuarios: explique este número a un jefe de planta sin decir «estamos seguros». Si los usuarios no pueden, el texto ha fallado.

### 35.1b Accesibilidad y veracidad de la exportación

Las métricas que infravaloran el éxito deben seguir siendo legibles: letra grande para la fracción, lenguaje llano para la advertencia, acceso por teclado a la exportación del denominador. Si la interfaz y la exportación CSV no coinciden, la exportación gana para el informe. Construya primero las exportaciones; trate la interfaz como una vista. Las exportaciones narrativas generadas con la misma consulta que la interfaz se pegan en los informes sin la ambigüedad de una captura de pantalla. Ocultar la advertencia en una información emergente reintroduce el problema de la puntuación vacía para quien no pase el cursor por encima.

Lena contrasta cada versión con la exportación.

### Nota de campo: tarea de explicación para el director financiero

En la investigación con usuarios, tres directivos explicaron la fracción de cobertura como «cuán seguros estamos». Tras cambios en los textos que prohibían esa lectura y mostraban por separado la alcanzabilidad del SIS, la misma tarea produjo en cambio explicaciones sobre comprobaciones planificadas y hallazgos abiertos.



Cada exportación lleva en su primera línea la versión de la consulta y la hora en que se ejecutó.


### 35.5 Ejemplo resuelto: la crítica del taller (ABP sintética)

El encargo del taller II: un jefe de planta debe decidir, a partir de una sola pantalla, si aprueba la siguiente fase del CNHP. El equipo de Lena muestra tres números con denominadores —31 de 44 técnicas de ATT&CK for ICS planificadas observadas en las pruebas, 6 de 9 conductos coincidentes con el diseño de zonas, SIS-B alcanzable desde alguna zona enrutada: no— más una lista breve de hallazgos altos abiertos. Los críticos defendían una insignia de riesgo única; el equipo respondió que la decisión del jefe depende de qué conductos siguen abiertos, no de un promedio. El diseño aceptado pone primero la lista de conductos abiertos, porque es el elemento que el jefe puede realmente financiar.

### Ejercicios — capítulo 35

- **EX103 — Texto.** Subtítulo bajo el número de cobertura. Rúbrica: 3 = niega la lectura como riesgo residual; 2 = advertencia débil; 1 = ninguna; 0 = sugiere seguridad.
- **EX104 — Insignia.** Una frase que rechace una insignia RAG. Rúbrica: 3 = clara + alternativa; 2 = solo rechaza; 1 = la acepta; 0 = nada.
- **EX105 — Exportación.** Columnas de la exportación del denominador. Rúbrica: 3 = identificador de la técnica, planificada, observada, notas; 2 = parcial; 1 = solo el %; 0 = nada.

### Síntesis del capítulo

Una interfaz que enseña la métrica, no un semáforo de impresiones.

### Siga estudiando — capítulo 35 de 50

[← Capítulo 34 (borrador)](#ch-34) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 36 (borrador) →](#ch-36)

<a id="ch-36"></a>

## Capítulo 36 — Seguridad de TO, IoT y sistemas ciberfísicos: rendimiento y escala

### Resultados de aprendizaje

Usted podrá (1) dimensionar los monitores dentro de los presupuestos de tiempo de ciclo; (2) aplicar la lógica del cubo de testigos al tráfico de evaluación; (3) medir el impacto en la planta con un canario.

### 36.1 El tiempo de ciclo es de primera categoría

Los objetivos de rendimiento que ignoran el presupuesto de ciclo del PLC son errores. Dimensione las canalizaciones de decodificación para que el tiempo en el cable más el de decodificación se mantenga dentro del presupuesto medido en el capítulo 3.

```python
"""Lab: does a polling schedule fit the PLC scan/communication budget? (synthetic)"""
link_bps = 115200; bits_per_byte = 10           # RS-485 serial, 8N1 + start bit
polls = [("T-1 level", 8), ("T-2 level", 8), ("R-101 block", 40), ("pump status", 8), ("historian sweep", 120)]
overhead = 12                                    # bytes of request+framing per poll (assumed)
total = sum(n + overhead for _, n in polls)
t = total * bits_per_byte / link_bps
print(f"bytes per cycle={total} time per cycle={t*1000:.1f} ms")
for target in (100, 50):
    print(f"cycle budget {target} ms -> {'fits' if t*1000 <= target else 'OVERRUN'}")
```

Salida esperada:

```text
bytes per cycle=244 time per cycle=21.2 ms
cycle budget 100 ms -> fits
cycle budget 50 ms -> fits
```

En ABP, la línea troncal RS-485 hacia el PLC-A funciona con un ciclo de sondeo de 21 ms dentro de un ciclo de control de 100 ms, y la condición de parada salta si el tiempo de ciclo llega a 50 ms. Lena dimensiona el monitor de modo que la derivación, la decodificación y el registro no añadan nada al tiempo en el cable, porque la derivación es pasiva y el decodificador se ejecuta en su propio equipo. Las pruebas de carga en el banco reproducen a doble velocidad un día completo de tráfico capturado para confirmar que el decodificador nunca se queda atrás respecto a la línea troncal.

### 36.2 Tráfico de evaluación

Cuando se autorizan métodos activos, limite su tasa para que no puedan dejar sin recursos al tráfico de control. Prefiera los métodos de solo escucha; cuando deba sondear, comparta un presupuesto global entre los escáneres. Durante las ventanas de evaluación del CNHP en ABP, solo una herramienta activa puede sondear la línea troncal a la vez, y su tasa de solicitudes se escribe en el permiso antes de empezar. El descubrimiento pasivo desde la derivación cubre la mayor parte del inventario, de modo que el sondeo activo se limita a los pocos dispositivos que no hablan por sí mismos. Cada herramienta informa de su tasa al presupuesto compartido, y el responsable de la ventana puede pausar todos los métodos activos con un solo interruptor si sube el tiempo de ciclo.

### 36.3 Canarios

Una solicitud canario sintética o una sonda del tiempo de ciclo cada minuto sigue la salud del sistema; las condiciones de parada saltan al alcanzar el umbral (capítulo 33).

> **Caso sintético — Ashford Batch Plant.** Con ciclos de 21 ms en la línea troncal RS-485, Lena dejó margen por debajo de 50 ms para que un pico de decodificación no activara la parada.

El canario de ABP lee cada minuto un registro de estado inofensivo del PLC-A y anota el tiempo de respuesta junto al tiempo de ciclo de la línea troncal. Si cualquiera de los dos se acerca a su umbral, se avisa al responsable de la ventana antes de llegar a la condición de parada, lo que da tiempo para pausar el trabajo activo con calma en lugar de reaccionar a una parada automática.

### 36.4 Errores y límites

Los escáneres distribuidos necesitan un presupuesto global coordinado o multiplican el límite por N. En ABP, dos escáneres funcionaron una vez desde equipos distintos, cada uno dentro de su propia tasa, y juntos superaron el presupuesto de la línea troncal. Lena trasladó el presupuesto a un único coordinador que concede testigos a cada escáner, de modo que el total se mantiene dentro del permiso sin importar cuántas herramientas estén funcionando. Un escáner que no puede contactar con el coordinador no puede enviar nada, lo que mantiene seguro el fallo en lugar de dejar que cada herramienta vuelva a su propio límite.

### Nota práctica

Publique una nota sobre la economía de los límites de tasa: coste de esperar frente a coste de interrumpir un lote. La mayoría de los argumentos para subir los límites se disuelven cuando se pone por escrito el coste de la interrupción.

### 36.1b Equidad y calentamiento

Cuando varios métodos comparten un presupuesto, un enumerador ruidoso puede dejar sin recursos a una revisión de configuración silenciosa. Pondere o separe los presupuestos por clase de método. Aumente el tráfico de forma gradual al inicio de la ventana y vacíelo antes de la parada definitiva. Vaciar significa ninguna solicitud nueva en los últimos diez minutos, para que las respuestas en curso lleguen antes de la parada. Documente quién puede subir un límite de tasa y qué tipo de ticket AUTH se requiere. Un límite elevado caduca al final de la ventana salvo que se renueve con un ticket nuevo.

Lena aplica ambos presupuestos en el coordinador.

### Nota de campo: calendario de calentamiento

El planificador aumenta ahora los sondeos de evaluación de forma gradual durante cinco minutos al inicio de la ventana. Los arranques instantáneos a plena tasa habían disparado alarmas de vibración no relacionadas en un patín vecino. El calentamiento es una cortesía hacia el proceso y hacia las personas responsables de él.


### 36.5 Ejemplo resuelto: medir la carga de la monitorización en el PLC-A (ABP sintética)

Un sondeador propuesto de la salud de los activos leería 120 registros de retención del PLC-A cada segundo. En el controlador de banco, Lena mide el tiempo de escaneo con y sin el sondeador: 18 ms de base, 23 ms con el sondeo, frente a un temporizador de vigilancia de 50 ms. El aumento es aceptable en el banco, pero aun así limita el sondeador a 120 registros cada 5 segundos en producción, añade un canario en una línea antes del despliegue en toda la planta y genera una alarma si el tiempo de escaneo supera 30 ms. El tráfico de evaluación recibe el mismo trato: toda herramienta de prueba debe declarar su tasa de solicitudes, y el permiso fija un máximo.

### Ejercicios — capítulo 36

- **EX106 — Laboratorio.** Bytes y tiempo por ciclo a 115200: informe de ambos. Rúbrica: 3 = 244 bytes, 21,2 ms; 2 = uno; 1 = incorrecto; 0 = nada.
- **EX107 — Margen.** Si el presupuesto es de 50 ms y el ciclo de 21 ms, ¿qué margen queda y por qué conservarlo? Rúbrica: 3 = ~29 ms para picos/reintentos; 2 = solo el número; 1 = usarlo todo; 0 = nada.
- **EX108 — Global.** ¿Por qué tres sondeadores sin coordinar rompen un permiso de 2 sol./s? Rúbrica: 3 = 3× la tasa; 2 = vago; 1 = lo niega; 0 = nada.

### Síntesis del capítulo

Primero el presupuesto, después la escala, siempre el canario.

### Siga estudiando — capítulo 36 de 50

[← Capítulo 35 (borrador)](#ch-35) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 37 (borrador) →](#ch-37)

<a id="ch-37"></a>

## Capítulo 37 — Seguridad de TO, IoT y sistemas ciberfísicos: operaciones

### Resultados de aprendizaje

Usted podrá (1) redactar el procedimiento operativo de una ventana; (2) hacer el traspaso entre turnos; (3) gestionar el cierre, incluida la desactivación de cuentas y el sellado de la evidencia.

### 37.1 Contenido del procedimiento operativo

Contactos, referencia al permiso de trabajo, versiones de las herramientas, condiciones de parada, árbol de escalado, rutas de la evidencia. Manténgalo lo bastante breve para usarlo bajo estrés. El procedimiento operativo de Lena para ABP cabe en cuatro páginas impresas. Nombra al responsable de la ventana y al ingeniero de control, enlaza el permiso de trabajo y enumera las versiones permitidas de cada herramienta. Las condiciones de parada, incluido el tiempo de ciclo de 50 ms, están en la primera página, seguidas del árbol de escalado y de la ubicación de la carpeta de evidencia. La versión 1.4 del procedimiento añadió la ruta del archivo de interruptor de corte después de que el ejercicio de mesa detectara su ausencia, y cada cambio posterior queda registrado en el historial de versiones.

### 37.2 Traspaso

Registro del turno: hallazgos abiertos, últimos identificadores de evento, aprobaciones pendientes, estado del interruptor de corte, alarmas de proceso durante la ventana. Traspaso verbal más el registro. En ABP, el responsable saliente lee en voz alta el registro del turno al responsable entrante y ambos lo rubrican. El registro enumera los hallazgos abiertos con sus responsables, los últimos identificadores de evento registrados por el monitor, las aprobaciones todavía pendientes, si el interruptor de corte está armado y las alarmas de proceso surgidas durante la ventana. Decir los elementos en voz alta detecta entradas que una persona creía obvias y la otra nunca había visto, como una regla temporal pendiente de eliminar.

### 37.3 Cierre

Desactivar las cuentas temporales, rotar los secretos, sellar la evidencia, exportar las métricas, programar la retrospectiva. Una lista de comprobación vale más que la memoria.

```python
"""Lab: fit patch jobs into plant maintenance windows (synthetic, greedy by risk)."""
windows = [("W1 Sat 02-06", 4.0), ("W2 Sun 02-04", 2.0)]
jobs = [("HMI OS update", 1.5, 8), ("historian DB patch", 2.5, 5), ("PLC-A firmware", 3.0, 9),
        ("eng-WS AV update", 0.5, 3), ("switch firmware", 1.0, 6)]   # name, hours, risk score
left = {w: h for w, h in windows}; plan = {w: [] for w, _ in windows}; deferred = []
for name, h, r in sorted(jobs, key=lambda j: -j[2]):
    for w, _ in windows:
        if left[w] >= h:
            left[w] -= h; plan[w].append(name); break
    else:
        deferred.append(name)
for w, _ in windows:
    print(w, plan[w], f"spare={left[w]:.1f}h")
print("deferred:", deferred)
```

Salida esperada:

```text
W1 Sat 02-06 ['PLC-A firmware', 'switch firmware'] spare=0.0h
W2 Sun 02-04 ['HMI OS update', 'eng-WS AV update'] spare=0.0h
deferred: ['historian DB patch']
```

> **Caso sintético — Ashford Batch Plant.** El cierre detectó que el parche aplazado del historiador seguía sin fecha; se escaló antes de la retrospectiva.

La lista de comprobación de cierre de Lena la ejecutan dos personas y su resultado se guarda con un hash. Un parche del historiador se había aplazado durante la ventana sin fecha, así que la lista lo señaló y el parche recibió un responsable y una fecha antes de que se reuniera la retrospectiva.

### 37.4 Errores y límites

Los procedimientos en wikis a los que nadie puede acceder desde la sala de control fallan; conserve una copia sin conexión. En ABP, la sala de control perdió el acceso de red a la wiki durante una ventana, y el responsable necesitaba de inmediato el árbol de escalado. Desde entonces, el último procedimiento se imprime y se guarda en una carpeta junto a HMI-1, y hay una copia en la estación de ingeniería para su uso sin conexión. Cada copia impresa lleva su número de versión, y la lista de cierre confirma que la copia en papel coincide con la versión vigente, para que no se siga por error un procedimiento antiguo durante un incidente.

### Nota práctica

La guardia de las herramientas del CNHP no es una licencia para ampliar conductos. Los avisos tratan de la seguridad de las herramientas y de la aplicación del permiso; los incidentes de proceso se encaminan por la vía de respuesta a incidentes y de seguridad de procesos de la planta.

### 37.1b Calendario y kits de repuesto

Las ventanas figuran en un calendario compartido con la versión del permiso de trabajo en la descripción. El solapamiento accidental de dos métodos ruidosos en la misma línea troncal es un fallo de operaciones. Los kits de operaciones incluyen imágenes de repuesto del servidor de salto, tarjetas de contacto impresas y copias del permiso sin conexión para cuando el SSO esté caído. El cierre no se marca como terminado hasta que se registren por su nombre los dos firmantes de la lista. El traspaso incluye leer en voz alta al responsable entrante las diez últimas denegaciones del monitor.

Lena revisa el calendario en cada traspaso. Los solapamientos se registran como hallazgos.

### Nota de campo: kit sin conexión

El SSO falló durante una ventana de domingo. La copia sin conexión del procedimiento y las tarjetas de contacto impresas permitieron al equipo detenerse limpiamente y avisar a seguridad de procesos. Desde entonces, el kit se revisa en cada cierre.



Las métricas de operaciones incluyen los avisos por ventana y el tiempo medio hasta el reconocimiento de las paradas; las métricas de vanidad como «equipos tocados» se quedan fuera del tablero de operaciones.


### 37.5 Ejemplo resuelto: un traspaso de turno con contenido de seguridad (ABP sintética)

La hoja de traspaso de ABP gana tres líneas: alertas abiertas del CNHP y quién es su responsable; cualquier sesión remota de proveedor habilitada o programada; y cualquier regla temporal o derivación en vigor con su hora de caducidad. El 14 de marzo, el turno de noche registró una regla temporal del cortafuegos para un diagnóstico del proveedor que caducaba a las 06:00; el turno de día lo comprobó a las 06:15, la encontró todavía presente y la eliminó con el acuerdo del ingeniero. Sin la línea en el traspaso, la regla se habría convertido en un conducto permanente. El cierre de cada orden de trabajo de seguridad exige el puntero a la evidencia y la confirmación de que se revirtieron los cambios temporales.

### Ejercicios — capítulo 37

- **EX109 — Lista de comprobación.** Seis pasos de cierre. Rúbrica: 3 = seis sensatos; 2 = cuatro; 1 = dos; 0 = nada.
- **EX110 — Traspaso.** Tres campos que debe incluir el registro del turno. Rúbrica: 3 = hallazgos/eventos/aprobaciones (o equivalentes); 2 = dos; 1 = uno; 0 = nada.
- **EX111 — Laboratorio.** ¿Qué trabajo se aplazó y qué debe registrar el cierre? Rúbrica: 3 = parche del historiador + riesgo residual + fecha de la siguiente ventana; 2 = solo el nombre; 1 = vago; 0 = incorrecto.

### Síntesis del capítulo

Opere con procedimientos, traspasos y un cierre implacable.

### Siga estudiando — capítulo 37 de 50

[← Capítulo 36 (borrador)](#ch-36) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 38 (borrador) →](#ch-38)

<a id="ch-38"></a>

## Capítulo 38 — Seguridad de TO, IoT y sistemas ciberfísicos: validación

### Resultados de aprendizaje

Usted podrá (1) validar las correcciones con nuevas pruebas; (2) evitar validaciones que reintroduzcan riesgo de proceso; (3) registrar los resultados negativos.

### 38.1 Diseño de la nueva prueba

Mismo punto de observación, mínimo privilegio, mismo estándar de evidencia. Para una corrección de la lista de permitidos: confirme en el banco que la escritura se deniega; no lance escrituras contra el PLC en servicio. Cuando se restringió la lista de permitidos de HIST-1 en ABP, Lena repitió la prueba desde el mismo servidor de salto y la misma cuenta que se usaron para el hallazgo original. Reprodujo una escritura con la función 16 hacia la copia de banco del PLC-A y confirmó que el monitor la denegaba con el código de motivo esperado. La comprobación en servicio fue de solo lectura: comparó la versión desplegada de la lista de permitidos con la versión del banco en lugar de enviar escrituras hacia los equipos de producción.

### 38.2 Resultados negativos

«Sigue abierto» es un resultado de validación válido. Los almacenes de hallazgos deben aceptarlo sin forzar el cierre. En ABP, la nueva prueba sobre las contraseñas de ingeniería compartidas descubrió que seguían en uso en dos estaciones de trabajo, así que el hallazgo siguió abierto con la nueva evidencia adjunta. El almacén de hallazgos de Lena permite que una nueva prueba registre «sigue abierto» con una fecha y un motivo, y el responsable recibe un nuevo plazo. Obligar a que cada nueva prueba cierre un hallazgo animaría a los revisores a dar por terminadas correcciones que solo se han aplicado en parte.

### 38.3 Ningún método nuevo

La validación usa el método que encontró el problema, o una comprobación de solo lectura más débil; no es una oportunidad para probar ataques nuevos.

> **Caso sintético — Ashford Batch Plant.** Nueva prueba de la regla de L4 a L2: la alcanzabilidad ya excluye L1-SIS; ticket cerrado con el hash de la exportación. Un hallazgo aparte sobre las contraseñas de ingeniería compartidas siguió abierto.

El plan de validación de Lena nombra el método original en el ticket antes de que empiece la nueva prueba. Cuando un revisor sugirió probar una nueva herramienta de fuzzing durante la validación, ella lo registró como propuesta para la siguiente evaluación.

### 38.4 Errores y límites

Un entorno distinto (banco frente a planta) significa que validó el banco. En ABP, la corrección de la lista de permitidos de Lena se validó primero en la copia de banco del PLC-A, y el ticket lo decía. Una comprobación aparte de solo lectura confirmó que el monitor de producción ejecutaba la misma versión de la lista de permitidos, y solo entonces el hallazgo se marcó como corregido en producción. Los informes mantienen separados ambos resultados, porque un aprobado en el banco no puede demostrar que la configuración de la planta coincida con la del banco, y algunas diferencias, como las revisiones de firmware, cambiarían el resultado.

### Nota práctica

Las nuevas pruebas automatizadas son comprobaciones de una lista de permitidos con tiempos de espera estrictos. Nunca incluyen relleno de credenciales ni reintentos de explotación.

### 38.1b Evidencia de la validación y arbitraje

Los tickets de validación enlazan con el hallazgo original, el método usado, la marca de tiempo y el hash de la nueva evidencia. Un «a mí me parece bien» sin esos campos no cierra un crítico. Las disputas se escalan a un árbitro nombrado que compara los hashes de la evidencia: no vuelve a atacar. Cuando muchos hallazgos similares comparten una causa raíz, repita la prueba en una muestra más los activos notificados originalmente, y dígalo. Las decisiones del árbitro son definitivas para la ventana y solo pueden recurrirse en la retrospectiva.

Los tickets de Lena llevan los cuatro campos.

### Nota de campo: nueva prueba por muestreo

Veinte HMI compartían una entrada ausente en la lista de permitidos. La validación repitió la prueba en cinco más los dos notificados originalmente, documentó la muestra y dejó el hallazgo abierto hasta que terminó el trabajo en toda la flota. Afirmar que los veinte estaban cerrados tras dos comprobaciones habría sido una mentira de medición.


### 38.5 Ejemplo resuelto: nueva prueba de validación del diseño de zonas (ABP sintética)

Seis meses después del despliegue, Lena vuelve a ejecutar la comprobación de alcanzabilidad del capítulo 2 sobre la exportación del cortafuegos en servicio y la lista de conductos del descubrimiento pasivo. La exportación coincide con el diseño en 8 de 9 conductos; el noveno muestra una regla L4→L3 no documentada añadida durante una actualización del ERP. El informe de validación registra el hallazgo negativo con evidencia, lo asigna al responsable de la red y no introduce ningún método de prueba nuevo a mitad de la validación, para que los resultados sigan siendo comparables con la línea base de la puesta en marcha. La zona del SIS-B sigue siendo inalcanzable en ambos conjuntos de datos, lo que se notifica como confirmado y no como supuesto.

### Ejercicios — capítulo 38

- **EX112 — Nueva prueba.** Pasos para validar con seguridad la eliminación de una regla de L4 a L2. Rúbrica: 3 = exportación + alcanzabilidad, sin camino esperado, evidencia, sin escrituras en servicio; 2 = parcial; 1 = ataque en servicio; 0 = nada.
- **EX113 — Negativo.** ¿Por qué «sigue abierto» debe poder guardarse? Rúbrica: 3 = honestidad/métricas; 2 = vago; 1 = cerrar siempre; 0 = nada.
- **EX114 — Entorno.** Limitación cuando la nueva prueba fue solo en el banco. Rúbrica: 3 = clara; 2 = vaga; 1 = afirma sobre la planta; 0 = nada.

### Síntesis del capítulo

Valide de forma acotada; conserve los negativos; no amplíe los métodos.

### Siga estudiando — capítulo 38 de 50

[← Capítulo 37 (borrador)](#ch-37) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 39 (borrador) →](#ch-39)

<a id="ch-39"></a>

## Capítulo 39 — Seguridad de TO, IoT y sistemas ciberfísicos: mantenibilidad

### Resultados de aprendizaje

Usted podrá (1) presupuestar las actualizaciones de políticas y dependencias; (2) mantener delgados los adaptadores; (3) documentar la responsabilidad, incluida la cobertura durante las vacaciones.

### 39.1 Cambios constantes

Las técnicas de ATT&CK for ICS, los firmwares de los PLC y las matrices de soporte de los HMI de los proveedores cambian. Reserve tiempo de calendario para las actualizaciones; fije las versiones y vigile los avisos de seguridad. En ABP, Lena mantiene una página de dependencias que enumera la versión de ATT&CK for ICS que usa el asignador, las revisiones de firmware del PLC-A y del SIS-B y las versiones admitidas por el proveedor del HMI. Una suscripción a los avisos de los proveedores alimenta una revisión semanal, y cada versión fijada tiene una fecha de revisión. Cuando cambia la lista de técnicas, el plan de cobertura se reconstruye a partir de la nueva versión antes de la siguiente evaluación, para que las 44 técnicas planificadas nunca remitan en silencio a un catálogo desactualizado.

### 39.2 Adaptadores delgados

Aísle los SDK de terceros detrás de interfaces para que las actualizaciones no reescriban el núcleo del almacén de hallazgos. El equipo de Lena lo aprendió del adaptador de alarmas basado en extracción de pantalla, que se rompía con cada actualización del HMI y tocaba código mucho más allá de su propósito. El CNHP coloca ahora cada biblioteca de proveedor detrás de una pequeña interfaz propiedad del equipo, con pruebas de contrato que usan salidas grabadas del proveedor. Cuando un proveedor cambia su biblioteca, solo cambian el adaptador y sus pruebas; la función de permiso, el almacén de hallazgos y el código del expediente quedan intactos, y las notas de versión pueden decir exactamente qué parte se movió.

### 39.3 Responsabilidad

Cada servicio tiene un equipo responsable nombrado y un respaldo. CODEOWNERS impone la revisión. La falta de cobertura durante las vacaciones bloquea la publicación de una versión.

> **Caso sintético — Ashford Batch Plant.** El asignador de ATT&CK for ICS es un adaptador; actualizar la lista de técnicas es una solicitud de incorporación de cambios de datos, no una reescritura.

En ABP, la página de cada servicio del CNHP nombra a un responsable y a un respaldo con nombre y apellido, no con un alias de equipo. Antes de una versión, las páginas se contrastan con el calendario de permisos, y una versión sin cobertura durante la siguiente ventana se retiene hasta que se forme a alguien.

### 39.4 Errores y límites

Las herramientas huérfanas se pudren hasta convertirse en museos de fallo abierto. El adaptador de alarmas basado en extracción de pantalla de ABP es el ejemplo que usa Lena: solo un ingeniero lo entendía, necesitó once correcciones en un año y fallaba en silencio cada vez que cambiaba el HMI. Una herramienta sin responsable deja de recibir parches, y cuando se rompe nadie se da cuenta de si falla de forma cerrada o abierta. La regla de Lena es que una herramienta sin responsable y sin respaldo la adopta una persona nombrada en el plazo de un mes o se retira con una fecha de borrado publicada.

### Nota práctica

Escriba una nota sobre el factor autobús: quién puede publicar versiones, quién entiende permit(), quién puede restaurar el almacén sellado. Si la respuesta es una sola persona, programe formación cruzada antes de la siguiente temporada.

### 39.1b Planes de obsolescencia y borrado

Anuncie con fechas la obsolescencia de las API; mantenga periodos de funcionamiento doble. La mantenibilidad incluye saber retirar una herramienta: exportar los expedientes, revocar las credenciales, archivar el código. Reserve en el calendario un mes anual de actualización de dependencias para que las versiones fijadas por CVE no esperen a una emergencia. Las sesiones de formación cruzada usan los mismos datos de prueba sintéticos que el laboratorio I, de modo que un respaldo practica con las entradas con las que se juzgará la versión; tras una sesión, el respaldo formado ejecutó solo el laboratorio I y la versión retenida salió.

Lena aplica este plan a todas las herramientas del CNHP, incluido el adaptador sustituido. Su retirada se anunció con antelación.

### Nota de campo: bloqueo por vacaciones

Una versión quedó bloqueada porque la única persona que entendía permit() estaba de permiso sin un respaldo formado. La formación cruzada con los datos de prueba del laboratorio I a la semana siguiente levantó el bloqueo. La mantenibilidad consiste sobre todo en que las personas puedan irse de vacaciones.



Los códigos de motivo obsoletos siguen siendo legibles para los consumidores durante una versión completa después de que los productores dejen de emitirlos.



La fecha de borrado se anuncia en la página del servicio con al menos una versión de antelación.


### 39.5 Ejemplo resuelto: eliminar un adaptador frágil (ABP sintética)

El CNHP tenía un adaptador a medida que analizaba la exportación de alarmas del proveedor del HMI mediante extracción de pantalla. Cada actualización del HMI lo rompía, y solo un ingeniero lo entendía. La revisión de mantenibilidad de Lena mide los cambios (11 correcciones en un año), la responsabilidad (una persona) y el radio de impacto (las estadísticas de alarmas de toda la planta). Lo sustituye por la interfaz de alarmas OPC UA admitida por el proveedor, mantiene el adaptador en solo lectura durante una versión como respaldo, publica una fecha de borrado y redacta el procedimiento para que un segundo ingeniero pueda operar la nueva vía. Menos piezas a medida significa menos fallos silenciosos en la evidencia de seguridad.

### Ejercicios — capítulo 39

- **EX115 — Fijar.** ¿Cómo fija el monitor para una ventana y permite aun así los parches de seguridad? Rúbrica: 3 = versión fijada + minilaboratorio I para la corrección urgente; 2 = parcial; 1 = siempre la última; 0 = nada.
- **EX116 — Adaptador.** Un método de una interfaz StoragePort. Rúbrica: 3 = p. ej., put_evidence(hash,bytes); 2 = vago; 1 = llamada concreta a un SDK; 0 = nada.
- **EX117 — Responsable.** Línea de responsabilidad del monitor serie. Rúbrica: 3 = equipo + respaldo + contacto; 2 = equipo; 1 = «el equipo»; 0 = nada.

### Síntesis del capítulo

Las versiones fijadas, los adaptadores y los responsables nombrados mantienen vivas las herramientas de forma segura.

### Siga estudiando — capítulo 39 de 50

[← Capítulo 38 (borrador)](#ch-38) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 40 (borrador) →](#ch-40)

<a id="ch-40"></a>

## Capítulo 40 — Laboratorio de verificación II

### Resultados de aprendizaje

Usted podrá (1) verificar el flujo de extremo a extremo, de la trama al ticket y a la cobertura; (2) inyectar fallos; (3) firmar una versión candidata.

### 40.1 De extremo a extremo

Trama sintética → decisión del monitor → evento → ticket de hallazgo → actualización de la cobertura. Registre los hashes en cada salto. En el laboratorio II de ABP, Lena reproduce una trama sintética en el banco de pruebas y la sigue por cada paso: la decisión de la función de permiso con su código de motivo, la alerta, la orden de trabajo del sistema de mantenimiento, el ticket de hallazgo y la actualización de la cobertura. Se registra un hash en cada salto, de modo que el expediente puede probar que el ticket describe el mismo evento que vio el monitor. Una cadena que no puede rastrearse salto a salto no cuenta como aprobada, aunque el resultado final parezca correcto.

### 40.2 Fallos

Detenga el almacén de hallazgos a mitad del flujo; confirme que el monitor sigue denegando y que los borradores se encolan. Corrompa un archivo de evidencia; confirme la alerta de discrepancia de hash. Proporcione una lista de aristas plana (insegura); confirme que la alcanzabilidad no supera la comprobación del SIS.

```python
# Lab 23 - reachability count on a synthetic Purdue-layered OT network
# Nodes: L5-ERP, L4-Office, L3.5-DMZ, L3-Hist, L2-SCADA, L1-PLC, L1-SIS, L0-IO
edges_flat=[("L5","L4"),("L4","L3"),("L3","L2"),("L2","L1-PLC"),("L2","L1-SIS"),("L1-PLC","L0"),("L1-SIS","L0"),("L4","L2")]
edges_zoned=[("L5","L4"),("L4","L3.5"),("L3.5","L3"),("L3","L2"),("L2","L1-PLC"),("L1-SIS","L0"),("L1-PLC","L0")]  # SIS not reachable from SCADA
def reach(edges, start):
    g={}; 
    for a,b in edges: g.setdefault(a,[]).append(b)
    seen=set(); stack=[start]
    while stack:
        n=stack.pop()
        if n in seen: continue
        seen.add(n); stack.extend(g.get(n,[]))
    return seen
for name,e in (("flat",edges_flat),("zoned",edges_zoned)):
    r=reach(e,"L4")
    print(f"{name}: L4 reaches {sorted(r)} count={len(r)} writes_to_SIS={'L1-SIS' in r}")
```

Salida esperada:

```text
flat: L4 reaches ['L0', 'L1-PLC', 'L1-SIS', 'L2', 'L3', 'L4'] count=6 writes_to_SIS=True
zoned: L4 reaches ['L0', 'L1-PLC', 'L2', 'L3', 'L3.5', 'L4'] count=6 writes_to_SIS=False
```

Los fallos del laboratorio II de Lena incluyen también la pérdida de alimentación del colector, que generó la alerta de visibilidad degradada en 40 segundos, y 90 segundos de desfase de reloj en la copia de banco del PLC-A. Cada fallo se inyecta por separado y luego por pares, porque un fallo inocuo por sí solo puede corromper la evidencia combinado con otro.

### 40.3 Aprobación

Lista de comprobación de la versión candidata firmada por el implementador y el revisor; las filas de seguridad funcional deben estar en verde.

> **Caso sintético — Ashford Batch Plant.** El laboratorio II detectó que, en un reintento, la cobertura se actualizaba antes de crear el ticket; se corrigió el orden con una bandeja de salida.

En ABP, la aprobación del laboratorio II enumera cada fila con su resultado y cada defecto abierto con un responsable, como el orden incorrecto de eventos causado por el desfase de reloj. La corrección del orden de Lena garantiza que el ticket se escriba antes de que se actualice el tablero de cobertura, para que un reintento no pueda contar un hallazgo que nunca se registró.

### 40.4 Errores y límites

Una prueba de extremo a extremo sin inyección de fallos solo demuestra el camino feliz. La primera ejecución de extremo a extremo de Lena en ABP aprobó todas las filas; sin embargo, el laboratorio II con fallos inyectados descubrió que el desfase de reloj desordenaba dos eventos en el expediente y que un reintento actualizaba la cobertura antes de que existiera el ticket. Ninguno de los dos defectos aparecería en una ejecución limpia, porque ambos dependen de fallos de temporización que solo ocurren cuando algo se rompe. Por eso, la aprobación del laboratorio II exige que cada guion de fallos se haya ejecutado y su resultado se haya registrado, y una ejecución sin fallos se informa como prueba de humo.

### Nota práctica

Paquete de datos de prueba maliciosos: hashes erróneos, eventos reordenados, marcas de tiempo futuras, un grafo plano que afirma estar zonificado. Superar solo los datos de prueba favorables es un laboratorio incompleto.

### 40.1b Observabilidad y paridad

El laboratorio II activa temporalmente los registros de depuración, pero sella una copia redactada. Dejar la depuración activada en las compilaciones de la ventana puede filtrar secretos. El entorno de laboratorio replica las versiones de las herramientas de producción y las claves de firma de políticas (claves de prueba). Un laboratorio II inestable es un bloqueo, no un ritual de reintentar hasta ver verde. Un guion de fallos que no puede ejecutarse se registra como fila fallida, no como omitida. Los guiones de inyección de fallos se guardan en la carpeta del laboratorio y se fijan por SHA en el informe. Las diferencias de paridad del entorno explican las sorpresas de verde en el laboratorio y rojo en la ventana.

La aprobación de Lena comprueba las diferencias de paridad.

### Nota de campo: paquete malicioso

El paquete malicioso del laboratorio II incluía un grafo plano etiquetado como zonificado. La comprobación de alcanzabilidad falló de forma cerrada y bloqueó la versión. Los laboratorios que solo prueban el camino feliz publican mentiras.



Selle los registros del laboratorio II con la misma herramienta de manifiesto que usa el expediente, para que los estudiantes practiquen un único flujo de hash.



Las pruebas inestables se ponen en cuarentena y se corrigen; publicar con un fallo cerrado ocasional es publicar con fallo abierto.


### 40.5 Ejemplo resuelto: inyección de fallos de extremo a extremo (ABP sintética)

El laboratorio II ejercita la cadena completa en el banco de pruebas: tráfico reproducido → función de permiso → alerta → orden de trabajo del sistema de mantenimiento → expediente. Fallos inyectados: pérdida de alimentación del colector, desfase de reloj de 90 segundos en el PLC-A, un evento mal formado y una acumulación en la cola de mensajes fallidos. Resultados: la pérdida de alimentación generó «visibilidad degradada» en 40 s; la comprobación de la fuente de tiempo detectó el desfase de reloj, pero este desordenó dos eventos en el expediente hasta que se aplicó la corrección del desfase; el evento mal formado llegó a la cola de mensajes fallidos; la acumulación se despejó en 7 minutos. La aprobación enumera el orden incorrecto como defecto abierto con un responsable.

### Ejercicios — capítulo 40

- **EX118 — Orden.** ¿Por qué crear el ticket antes de que aumente el recuento de cobertura? Rúbrica: 3 = la cobertura debe reflejar hallazgos registrados; 2 = vago; 1 = cualquier orden; 0 = nada.
- **EX119 — Fallo.** Comportamiento esperado del monitor cuando el almacén de hallazgos está caído. Rúbrica: 3 = sigue evaluando/denegando; encola borradores; 2 = parcial; 1 = fallo abierto; 0 = nada.
- **EX120 — Aprobación.** Se requieren dos firmas: ¿de quién? Rúbrica: 3 = implementador + revisor independiente; 2 = una; 1 = solo el responsable jerárquico; 0 = nada.

### Síntesis del capítulo

Extremo a extremo con fallos; seguridad funcional en verde; dos firmas.

### Siga estudiando — capítulo 40 de 50

[← Capítulo 39 (borrador)](#ch-39) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 41 (borrador) →](#ch-41)

<a id="ch-41"></a>

## Capítulo 41 — Seguridad de TO, IoT y sistemas ciberfísicos: optimización del sistema

### Resultados de aprendizaje

Usted podrá (1) perfilar de forma ética las canalizaciones de seguridad de TO; (2) optimizar respetando las restricciones de tiempo de ciclo y de las ROE; (3) rechazar optimizaciones que debiliten la seguridad funcional.

### 41.1 Primero, perfilar

Mida a dónde va el tiempo: decodificación, evaluación del permiso, escritura del evento. Optimice el término dominante. Solo carga sintética. En ABP, Lena perfiló el monitor en el banco de pruebas antes de aprobar cualquier optimización. Reproduciendo un día grabado de tráfico de la línea troncal, midió cuánto tardaban la decodificación, la evaluación del permiso y la escritura del evento, y descubrió que dominaba la escritura del evento. Agrupar las escrituras redujo la latencia total sin cambiar ni una sola regla de permiso. Usa solo carga sintética o reproducida, porque perfilar contra equipos reales añadiría exactamente el riesgo que el monitor existe para reducir, y la copia de banco del PLC-A se comporta de forma suficientemente parecida para el trabajo de temporización.

### 41.2 Preservar las restricciones

Almacenar en caché AllowListVersion es correcto si la invalidación al publicar es correcta. Almacenar en caché decisiones de permiso entre estaciones no lo es: las estaciones difieren. En el CNHP, la lista de permitidos se guarda en caché en memoria con su número de versión, y cada publicación vacía la caché antes de usar la nueva versión, para que no persistan reglas obsoletas. Se rechazó almacenar en caché decisiones individuales, porque el HMI-1 y la estación de ingeniería tienen permitidos registros distintos, y una decisión almacenada para uno sería errónea para el otro. Las pruebas de Lena incluyen una publicación con carga alta para confirmar que la primera decisión después de publicar siempre usa la nueva versión.

### 41.3 Veto de seguridad funcional

Cualquier optimización que omita las comprobaciones de la lista de denegación, acorte los campos de auditoría o falle de forma abierta se rechaza, sea cual sea la mejora de velocidad.

```python
"""Lab: does a polling schedule fit the PLC scan/communication budget? (synthetic)"""
link_bps = 115200; bits_per_byte = 10           # RS-485 serial, 8N1 + start bit
polls = [("T-1 level", 8), ("T-2 level", 8), ("R-101 block", 40), ("pump status", 8), ("historian sweep", 120)]
overhead = 12                                    # bytes of request+framing per poll (assumed)
total = sum(n + overhead for _, n in polls)
t = total * bits_per_byte / link_bps
print(f"bytes per cycle={total} time per cycle={t*1000:.1f} ms")
for target in (100, 50):
    print(f"cycle budget {target} ms -> {'fits' if t*1000 <= target else 'OVERRUN'}")
```

Salida esperada:

```text
bytes per cycle=244 time per cycle=21.2 ms
cycle budget 100 ms -> fits
cycle budget 50 ms -> fits
```

> **Caso sintético — Ashford Batch Plant.** Almacenar en caché en memoria las listas de permitidos firmadas redujo la latencia; la invalidación al publicar mantuvo la seguridad funcional. Se vetó una propuesta para omitir las comprobaciones de registros en los HMI conocidos como fiables.

Lena registra en ABP cada propuesta vetada con su mejora de velocidad esperada y el motivo del rechazo. El registro de decisiones evita que la misma idea se reabra cada trimestre sin nuevos argumentos de seguridad funcional.

### 41.4 Errores y límites

Las pruebas de rendimiento en portátiles no predicen las líneas troncales de planta. En ABP, un decodificador que funcionaba con holgura en el portátil de un desarrollador se quedó atrás cuando Lena lo probó en la copia de banco de la línea troncal RS-485 con la temporización y los tamaños de trama reales. Los portátiles tienen procesadores más rápidos y ninguno de los límites de temporización serie que importan en la planta. Lena solo acepta ahora cifras de rendimiento del banco de pruebas, y cada informe indica el ciclo de sondeo de 21 ms de la línea troncal y la parada de 50 ms junto al resultado medido, para que los lectores puedan juzgar el margen.

### Nota práctica

Las propuestas de optimización requieren un párrafo de seguridad funcional. Las propuestas que no lo tienen se devuelven sin leer.

### 41.1b Descarte de carga y N+1

Ante una sobrecarga, descarte el trabajo de descubrimiento antes que la evaluación de denegaciones. Las actualizaciones de tickets excesivas durante una importación masiva aplastan el almacén de hallazgos: agrupe las escrituras y mida. Mantenga margen dentro del presupuesto de tiempo de ciclo para que una tormenta de reintentos no lo supere. El orden de descarte de carga está escrito en el procedimiento, para que el responsable de la ventana sepa qué trabajo se pausa primero. Las revisiones de Lena aplican cada regla. En ABP, Lena probó la sobrecarga reproduciendo el tráfico al triple de velocidad: el descubrimiento se pausó primero, mientras las decisiones de denegación continuaban a pleno ritmo y quedaban muy por debajo del presupuesto de ciclo.

### Nota de campo: párrafo de seguridad funcional

Una solicitud de incorporación de cambios de optimización que eliminaba los códigos de motivo de los registros de la ruta crítica para ahorrar microsegundos se devolvió sin leer por carecer de párrafo de seguridad funcional. La versión revisada conservó los códigos y encontró la mejora en otra parte. Los párrafos de seguridad funcional no son burocracia; son el mecanismo de veto.



La reproducción de sobrecarga se repite después de cada versión que toca el decodificador.


### 41.5 Ejemplo resuelto: optimización con veto de seguridad funcional (ABP sintética)

Producción pide acortar el lote del R-101 aumentando el caudal de alimentación, y pide al CNHP que relaje el límite de frecuencia de la función de permiso para escrituras de consigna, de una cada 10 s a una por segundo, para adaptarse a la receta más rápida. Lena perfila primero: solo la fase de carga necesita escrituras más rápidas. Propone un límite específico de fase, aplicado solo mientras el estado del lote es «carga», y lo somete al ingeniero de seguridad de procesos, que confirma que los disparos por alta temperatura y alto nivel del SIS-B no se ven afectados. El ingeniero de seguridad funcional tiene derecho de veto sobre cualquier optimización que toque un lazo relevante para la seguridad; esta se aprobó, con una prueba de carga en el banco de pruebas.

### Ejercicios — capítulo 41

- **EX121 — Veto.** Una optimización que debe rechazarse. Rúbrica: 3 = ejemplo que debilita la seguridad funcional; 2 = vago; 1 = la aprueba; 0 = nada.
- **EX122 — Caché.** ¿Cuándo es seguro almacenar decisiones en caché? Rúbrica: 3 = misma versión+estación+fc+registro, TTL corto, invalidar al publicar; 2 = parcial; 1 = siempre; 0 = nada.
- **EX123 — Descarte.** ¿Qué descarta primero ante una sobrecarga? Rúbrica: 3 = descubrimiento/evaluación antes que la evaluación de denegaciones; 2 = parcial; 1 = descartar denegaciones; 0 = nada.

### Síntesis del capítulo

Velocidad dentro de las restricciones; la seguridad funcional tiene derecho de veto.

### Siga estudiando — capítulo 41 de 50

[← Capítulo 40 (borrador)](#ch-40) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 42 (borrador) →](#ch-42)

<a id="ch-42"></a>

## Capítulo 42 — Seguridad de TO, IoT y sistemas ciberfísicos: investigación aplicada

### Resultados de aprendizaje

Usted podrá (1) plantear una pregunta de investigación sobre programas de seguridad de TO; (2) elegir medidas y líneas de base con la higiene propia de la evaluación de detectores; (3) mantener el doble uso fuera de la investigación estudiantil.

### 42.1 Preguntas adecuadas

¿Reduce la doble aprobación los incidentes de ampliación de conductos? ¿Cambia la interpretación de la cobertura por las partes interesadas si se muestran los denominadores? No una nueva evasión contra la marca de PLC X. La investigación aplicada de Lena en ABP siguió este patrón: eligió una pregunta sobre las líneas de base de los detectores, expuesta en el ejemplo resuelto siguiente. La pregunta podía responderse con tráfico grabado y cambiaría directamente cómo configura la planta su monitor. Rechazó la sugerencia de estudiar evasiones contra una marca concreta de PLC, porque eso produciría conocimiento de ataque sin mejorar cómo ABP gestiona sus defensas.

### 42.2 Diseño

Prerregistre las medidas; use datos operativos sintéticos o consentidos; informe intervalos y clases de ataque (Urbina et al.; Giraldo et al.). La replicación vale más que el teatro de la novedad. Lena registró sus medidas, longitudes de línea de base y umbral antes de analizar los 60 días de tráfico grabado de ABP. Su registro de enmiendas contiene el único cambio que hizo después del registro, con su motivo. Los resultados se informan con intervalos para cada longitud de línea de base, para que los lectores vean dónde es débil la evidencia. Prefiere confirmar con cuidado un hallazgo anterior antes que afirmar uno nuevo que nadie pueda reproducir.

### 42.3 Divulgación

Si la investigación descubre accidentalmente un problema real, siga la divulgación responsable, no un blog de clase.

> **Caso sintético — Ashford Batch Plant.** El estudio aplicado de Lena midió cuántos días de línea de base necesita un detector de nuevos conductos antes de que sus falsas alertas bajen de una por semana (§42.5); prerregistrado, sintético+anonimizado.

El plan de investigación de Lena nombraba al equipo de seguridad de producto del proveedor como primer contacto para cualquier fallo encontrado en un producto, y fijaba la publicación solo después de la respuesta del proveedor. La tesis describiría un fallo solo en términos generales. Su supervisor revisó el plan antes de analizar ningún tráfico.

### 42.4 Errores y límites

Los proyectos del curso no son investigación con seres humanos; evite recopilar datos personales de los operadores. La investigación de Lena en ABP usó el tráfico entre dispositivos, no registros de lo que hacía cada operador, por lo que ninguna persona podía identificarse a partir de sus datos. Donde aparecían acciones de operadores en los registros, como los reconocimientos en el HMI-1, eliminó los nombres de usuario antes del análisis. Estudiar a personas como es debido requiere una revisión ética de la que carece un proyecto del curso, así que cualquier pregunta sobre el comportamiento de los operadores se deja para trabajos futuros con las aprobaciones adecuadas, en lugar de responderse con datos recopilados de manera informal.

### Nota práctica

El código de análisis prerregistrado vive en el repositorio con un commit de congelación anterior a la recopilación de datos. Enmendarlo después de mirar los datos requiere una enmienda registrada.

### 42.1b Compartición de datos y resultados negativos

Incluso las métricas operativas sintéticas más anonimizadas requieren un acuerdo escrito con la organización anfitriona para las tesis de los estudiantes. La investigación aplicada publicable incluye resultados negativos. Ocultar los negativos sesga a la siguiente cohorte hacia una confianza vacía. Indique el límite del doble uso en la sección de ética de la tesis con un ejemplo concreto de rechazo. Los resultados negativos reciben la misma calidad de figuras que los positivos en la plantilla de tesis. El acuerdo con la organización anfitriona para los datos de ABP se firmó antes del análisis, y la tesis de Lena informa con figuras completas las longitudes de línea de base que nunca alcanzaron el umbral.

### Nota de campo: registro de enmiendas

Tras mirar los datos piloto, un estudiante quiso cambiar la medida principal. El registro de enmiendas recogió el motivo y conservó la medida original como análisis secundario. El prerregistro sin disciplina de enmiendas es teatro.



El acuerdo nombra quién puede ver los extractos en bruto y cuándo se borran.



Cada entrada de enmienda lleva la fecha, el motivo y el commit que cambió el código de análisis.


### 42.5 Ejemplo resuelto: una pregunta de investigación adecuada para la planta (ABP sintética)

La investigación aplicada de Lena pregunta: con el tráfico grabado de ABP, ¿cuántos días de línea de base se necesitan antes de que las falsas alertas de un detector de nuevos conductos bajen de una por semana? El diseño usa 60 días de tráfico sintético pero realista, líneas de base deslizantes de 3, 7, 14 y 28 días y un umbral prerregistrado. El registro de enmiendas recoge un cambio: una actualización del ERP añadió tráfico el día 33, así que ese día se analiza por separado en lugar de eliminarse en silencio. La planificación de la divulgación forma parte del diseño: si el trabajo revela un fallo de producto, se comunica al PSIRT del proveedor antes de la publicación.

### Ejercicios — capítulo 42

- **EX124 — Pregunta.** Una pregunta de investigación aceptable. Rúbrica: 3 = centrada en el programa/proceso; 2 = dudosa; 1 = centrada en exploits; 0 = nada.
- **EX125 — Medida.** Medida principal para el estudio de doble aprobación. Rúbrica: 3 = p. ej., intentos de ampliación no aprobados por trimestre; 2 = vaga; 1 = «seguridad»; 0 = nada.
- **EX126 — Doble uso.** Rechace un proyecto que pide un nuevo exploit para PLC. Rúbrica: 3 = rechazo + alternativa; 2 = rechazo; 1 = lo acepta; 0 = nada.

### Síntesis del capítulo

Investigue el programa y el proceso; no convierta los hallazgos en armas.

### Siga estudiando — capítulo 42 de 50

[← Capítulo 41 (borrador)](#ch-41) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 43 (borrador) →](#ch-43)

<a id="ch-43"></a>

## Capítulo 43 — Práctica en la industria o en el servicio público

### Resultados de aprendizaje

Usted podrá (1) adaptar la ingeniería CNHP a las restricciones de una organización anfitriona; (2) redactar un informe de prácticas sin detalles de propiedad reservada; (3) traducir entre seguridad de procesos, operaciones e ingeniería.

### 43.1 Estancia

En la industria o el servicio público, las plantillas de permisos de trabajo, la residencia de datos y las compras son distintas. Su trabajo sigue siendo construir herramientas que fallan de forma cerrada y medir con honestidad, no hacer pruebas ingeniosas sin autorización. En su estancia en un fabricante por contrato, Lena encontró formularios de permiso distintos, un proceso de compras distinto y reglas más estrictas que en ABP sobre dónde podían almacenarse los datos. Adaptó sus métodos al proceso de la anfitriona en lugar de importar los formularios de ABP. Lo que no cambió fue el núcleo de su práctica: herramientas que se detienen de forma segura ante la duda, mediciones con sus denominadores y pruebas realizadas solo dentro del alcance que la anfitriona había aprobado por escrito.

### 43.2 Informes depurados

Los entregables del curso usan nombres sintéticos y agregados. Los identificadores reales de la planta permanecen dentro de los sistemas de la anfitriona. El informe de prácticas de Lena describió el riesgo del portátil del proveedor sin nombrar a la anfitriona, sus plantas ni sus dispositivos. Las direcciones y los nombres de host permanecieron dentro de los sistemas de la anfitriona, y las cifras se dieron solo como recuentos o rangos. La revisión de autorización de la anfitriona comprobó el informe antes de que llegara a la universidad, y su supervisora calificó la versión depurada, de modo que nada identificable salió de la organización. Lena conservó los originales en los sistemas de la anfitriona.

### 43.3 Traducción

Seguridad de procesos escucha independencia y SIL. Operaciones escucha ventanas y alarmas. Ingeniería escucha esquemas y pruebas. Los mismos hechos, tres dialectos.

> **Caso sintético — Ashford Batch Plant.** El memorando de prácticas de Lena usó solo cifras sintéticas de ABP; se omitieron los nombres reales de las plantas asociadas.

En su memorando de prácticas, Lena redactó el mismo hallazgo sobre el portátil de tres maneras: para seguridad de procesos, como una amenaza a la independencia de los controladores de línea; para operaciones, como una necesidad de programar actualizaciones; y para ingeniería, como un cambio de configuración. Cada lector recibió la versión que necesitaba.

### 43.4 Errores y límites

«No puedo contarle lo que hice» no es un informe de prácticas: use una reconstrucción sintética acordada con la anfitriona. El informe de prácticas de Lena no podía incluir los detalles reales de la red de la anfitriona, así que acordó con su mentor en la anfitriona una reconstrucción sintética que conservaba la estructura del hallazgo pero sustituía cada detalle identificativo. Su apéndice de restricciones indicaba lo que no se le había permitido examinar. Esto dio a la universidad algo que evaluar sin exponer a la anfitriona, y es la norma para cualquier estancia en la que el propio trabajo no pueda describirse directamente.

### Nota práctica

Si su anfitriona vende escáneres de TO, declárelo y siga rechazando las puntuaciones vacías. Las presentaciones comerciales no son medición.

### 43.1b Autorizaciones y conflictos

Las estancias en el servicio público pueden requerir habilitaciones de seguridad. Los artefactos del curso se mantienen en el nivel de sensibilidad más bajo: reconstrucciones sintéticas. Nunca pegue texto restringido en GitHub. Los informes de prácticas incluyen un apéndice de restricciones que se califica con el mismo peso que el trabajo técnico. Si la anfitriona prohíbe incluso las métricas depuradas, use un escenario de gemelo totalmente sintético y etiquetado como tal. El propio apéndice de Lena siguió esta regla. El acuerdo de Lena con su mentor en la anfitriona se redactó antes de empezar a escribir, y nombraba las cifras que podía usar y las que no.

### Nota de campo: apéndice de restricciones

Una anfitriona del servicio público prohibía el SaaS extranjero y exigía registros preparados para solicitudes de acceso a la información pública (FOIA). El apéndice de restricciones del informe de prácticas explicaba por qué la arquitectura C era imposible y por qué se eligió la A. Los evaluadores calificaron el apéndice con el mismo peso que el código.



El apéndice de restricciones enumera cada restricción junto con el rol de la anfitriona que la impuso.


### 43.5 Ejemplo resuelto: traducir un hallazgo de la estancia (ABP sintética)

En su estancia en un fabricante por contrato, Lena observa que el portátil del proveedor usado para las actualizaciones de los PLC también navega por internet. Su informe depurado omite nombres de host y direcciones, describe el riesgo en términos de planta —«un solo portátil reúne la exposición a internet y la capacidad de descargar lógica en los controladores de línea (ATT&CK for ICS T0843)»— y recomienda un portátil de ingeniería dedicado y actualizado sin conexión. La revisión de autorización de la organización anfitriona aprueba el informe antes de que llegue a su universidad, y el apéndice de restricciones indica lo que no se le permitió examinar.

### Ejercicios — capítulo 43

- **EX127 — Dialecto.** Traduzca «fallar de forma cerrada ante la falta de política» para seguridad de procesos. Rúbrica: 3 = redacción en términos de seguridad/riesgo; 2 = parcial; 1 = avalancha de jerga; 0 = nada.
- **EX128 — Depurar.** Reescriba una frase que filtra un nombre de host real. Rúbrica: 3 = sustituto sintético; 2 = parcial; 1 = sigue filtrando; 0 = nada.
- **EX129 — Restricción.** Dos restricciones del servicio público que cambian la arquitectura. Rúbrica: 3 = p. ej., residencia de datos, compras, FOIA; 2 = una; 1 = vaga; 0 = nada.

### Síntesis del capítulo

La práctica son restricciones reales más artefactos de aprendizaje depurados.

### Siga estudiando — capítulo 43 de 50

[← Capítulo 42 (borrador)](#ch-42) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 44 (borrador) →](#ch-44)

<a id="ch-44"></a>

## Capítulo 44 — Proyecto final de ingeniería I

### Resultados de aprendizaje

Usted podrá (1) proponer un proyecto final que entregue una mejora CNHP medible; (2) definir el alcance y los objetivos excluidos; (3) establecer un plan de verificación vinculado a filas del Laboratorio I.

### 44.1 Propuesta

Problema, usuarios, requisitos (la seguridad primero), esbozo de arquitectura, hitos, plan de verificación en laboratorio y párrafo de ética. Se rechazan los proyectos finales que requieren trabajo de explotación. La propuesta del Proyecto final I de Lena era el compilador de políticas descrito en el ejemplo resuelto siguiente. Sus requisitos ponían la seguridad primero: SIS-B debe seguir siendo inalcanzable desde todas las zonas enrutadas. Sus hitos, su plan de laboratorio y su párrafo de ética se revisaron antes de empezar a programar. El proyecto no necesitó trabajo de explotación, porque su tarea era demostrar que las reglas coinciden con el diseño, no irrumpir en nada de la planta.

### 44.2 Objetivos excluidos

Enumere explícitamente lo que no construirá (módulos de explotación, escaneo de la planta en vivo, oráculos de riesgo basados en aprendizaje automático, puntuaciones vacías). Los objetivos excluidos de Lena quedaron escritos en su propuesta y firmados por su supervisora: ningún despliegue en vivo, ninguna configuración de SIS-B y ningún escaneo activo. Cuando un compañero sugirió añadir un escaneo automático para comprobar las reglas desplegadas, ella señaló la lista congelada y mantuvo las comprobaciones del compilador trabajando sobre exportaciones. Haber escrito pronto los objetivos excluidos le dio una respuesta clara para cada ampliación tentadora durante el trimestre.

### 44.3 Hito 1

Algo demostrable sobre datos sintéticos en la semana 3: p. ej., interruptor de corte respetado en ≤30 s, con una prueba.

> **Caso sintético — Ashford Batch Plant.** Se devolvieron las propuestas de Proyecto final I que mencionaban auto-pwn; avanzó la distribución firmada de listas de permitidos con fallo cerrado.

Otras propuestas de la cohorte de Lena construyeron la distribución firmada de listas de permitidos. El hito 1 de la propia Lena para el compilador cumplió la alcanzabilidad en los nueve conductos de ABP, pero solo produjo vectores de prueba para siete reglas. La demostración se ejecutó íntegramente sobre exportaciones sintéticas, y la carencia se convirtió en el primer punto del hito 2.

### 44.4 Errores y límites

La ampliación descontrolada del alcance es el principal asesino: congele los objetivos excluidos. Durante el proyecto final de Lena, los revisores sugirieron añadir un panel, envíos de reglas al cortafuegos en vivo y soporte para una segunda planta. Cada sugerencia habría llevado semanas y ninguna era necesaria para demostrar que el compilador coincidía con el diseño. Respondió a cada una con los objetivos excluidos congelados y las colocó en una lista de trabajo futuro. Los dos vectores que faltaban del hito 1 se convirtieron en su primera tarea del hito 2, de modo que el tiempo restante se dedicó a terminar lo prometido. Su alcance final coincidió con la propuesta.

### Nota práctica

Las propuestas que no pueden nombrar una fila del Laboratorio I para cada requisito Must vuelven a borrador.

### 44.1b Métricas de éxito y puntos de control

Defina dos métricas que mostrará en la defensa (p. ej., tiempo hasta denegarlo todo, porcentaje de fusiones con tickets AUTH). El Proyecto final I tiene puntos de control obligatorios: propuesta aceptada, demostración del hito 1 y control ético intermedio. Saltarse un punto de control congela la programación hasta recuperarlo. Registro de riesgos del proyecto final: ampliación descontrolada del alcance, retraso de dependencias, falta de disponibilidad de revisores, confusión sobre los límites éticos, cada uno con su alerta temprana y su mitigación. Las demostraciones de hitos que omiten el fallo cerrado reciben cero en ese punto de control.

Las dos métricas de Lena fueron la alcanzabilidad de los conductos y la cobertura de vectores. Ambas aparecen en su defensa.

### Nota de campo: la ética, pronto

Una propuesta que incluía un escaneo de la planta en vivo se rechazó en el punto de control ético antes de escribir una sola línea de código. Vincular los requisitos Must a filas del Laboratorio I en la misma revisión evitó un diseño precioso que no podía demostrar el fallo cerrado.



Un punto de control perdido se recupera con un plan escrito, acordado con el director, antes de reanudar la programación.



Cada métrica se mide con el mismo script en el hito 1 y en la defensa, de modo que las cifras son comparables.


### 44.5 Ejemplo resuelto: hito 1 del proyecto final (ABP sintética)

El proyecto final de Lena construye un compilador verificado de políticas de zonas y conductos: lee un modelo de zonas y emite reglas de cortafuegos más vectores de conformidad. Objetivos excluidos: ningún despliegue en vivo, ninguna configuración de SIS-B, ningún escaneo activo. Métrica de éxito del hito 1: para el modelo de nueve conductos de ABP, el compilador produce reglas cuya alcanzabilidad (comprobada con el código de grafos del capítulo 2) es exactamente igual al diseño, y cada regla tiene al menos un vector de paso y uno de bloqueo. En el punto de control cumplió la alcanzabilidad en 9/9 conductos, pero solo produjo vectores para 7/9 reglas; la carencia es el primer punto del hito 2.

### Ejercicios — capítulo 44

- **EX130 — Objetivo excluido.** Tres objetivos excluidos para un proyecto final de panel de cobertura. Rúbrica: 3 = tres claros; 2 = dos; 1 = uno; 0 = nada.
- **EX131 — Hito.** Hito de la semana 3 con prueba de aceptación. Rúbrica: 3 = demostración + prueba; 2 = solo demostración; 1 = vago; 0 = nada.
- **EX132 — Ética.** Párrafo de ética de cuatro frases. Rúbrica: 3 = autorización, datos sintéticos, doble uso, divulgación; 2 = parcial; 1 = débil; 0 = nada.

### Síntesis del capítulo

Entregue valor de programa relevante para la seguridad; congele pronto los objetivos excluidos.

### Siga estudiando — capítulo 44 de 50

[← Capítulo 43 (borrador)](#ch-43) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 45 (borrador) →](#ch-45)

<a id="ch-45"></a>

## Capítulo 45 — Revisión independiente del diseño

### Resultados de aprendizaje

Usted podrá (1) realizar una revisión capaz de rechazar; (2) usar una lista de comprobación vinculada a los requisitos de seguridad; (3) registrar las opiniones discrepantes.

### 45.1 Derechos de revisión

Los revisores pueden bloquear una fusión por rutas que fallan de forma abierta, pruebas ausentes, regresiones de alcanzabilidad del SIS o puntuaciones vacías en la interfaz. Un LGTM sin la lista de comprobación no es válido. En ABP, los revisores de CNHP tienen autoridad escrita para bloquear una fusión por cualquiera de estos motivos, y el director de planta ha aceptado no anular un bloqueo para cumplir un plazo. Un revisor que aprueba sin completar la lista de comprobación no ha revisado el cambio, y la fusión se revierte hasta que se haga una revisión adecuada. Lena lleva un registro de los bloqueos y sus motivos, que mostró que la mayoría se debían a pruebas ausentes y no a diseños inseguros.

### 45.2 Lista de comprobación

Fallo cerrado; autenticación de la política; el esquema prohíbe cargas útiles; la cobertura tiene denominador; ocultación de secretos; ruta de reversión documentada; prueba de alcanzabilidad del SIS en verde. La lista de comprobación de Lena en ABP tiene una línea por elemento, y cada línea enlaza con el requisito que hace cumplir, como S-1 para el comportamiento de fallo cerrado y R-12 para la alcanzabilidad de SIS-B. El revisor marca una línea solo después de ver la evidencia, como la prueba que falla cuando falta la política. La reversión se comprueba nombrando la versión anterior y el comando para restaurarla, y la prueba de alcanzabilidad debe haberse ejecutado sobre el commit exacto que se fusiona.

### 45.3 Discrepancia

Si un revisor discrepa, registre la discrepancia en el ADR aunque se le desautorice: los incidentes futuros necesitan ese rastro.

> **Caso sintético — Ashford Batch Plant.** Un PR de insignia de cobertura se bloqueó dos veces con esta lista de comprobación; la tercera revisión entregó la interfaz honesta (capítulo 35).

En ABP, la discrepancia de la revisora externa sobre el envío de alertas del colector a la HMI se registró textualmente y, en ese caso, cambió el diseño. Lena guarda en el mismo lugar las discrepancias desautorizadas, porque un incidente posterior puede darles la razón.

### 45.4 Errores y límites

Las revisiones posteriores a la fusión son arqueología, no control. En ABP, un pequeño cambio en el formato de las alertas se fusionó una vez antes de la revisión porque el plazo estaba cerca, y la revisión posterior descubrió que había eliminado el código de motivo del que dependían los operadores. La corrección exigió una segunda publicación durante una ventana. Desde entonces, la cola de fusión de CNHP rechaza cualquier cambio sin una lista de comprobación completada, y una revisión solicitada después de fusionar se registra como fallo de proceso en la retrospectiva en lugar de contarse como revisión.

### Nota práctica

Los revisores ejecutan localmente las pruebas críticas sobre datos de prueba sintéticos antes de la reunión; no se limitan a leer el diff.

### 45.1b Revisores externos y SLO

Una vez por trimestre, invite a un ingeniero ajeno al equipo a revisar un PR crítico para la seguridad. Las revisiones se completan en un número acordado de días hábiles o el cambio caduca en la cola de fusión (no se fusiona automáticamente). Prohíba las fusiones del viernes por la tarde antes de las ventanas, salvo una corrección urgente de seguridad con evidencia del Laboratorio I. Los comentarios de bloqueo deben citar un identificador de requisito o un número de elemento de la lista de comprobación. Las omisiones repetidas de la lista por un mismo revisor desencadenan una conversación de orientación. El calendario forma parte del diseño de los controles.

La revisora externa de ABP procedía de una empresa de abastecimiento de agua.

### Nota de campo: prohibición de fusiones en viernes

Se revirtió una fusión de interfaz, que no era una corrección urgente, hecha un viernes por la tarde antes de una ventana del sábado. La regla del calendario existe porque los revisores cansados pasan por alto las rutas que fallan de forma abierta. Las heroicas fusiones de última hora son una mala señal.



Los hallazgos de la revisora externa se archivan como cualquier otra revisión, con identificadores de requisito.



Una revisión que incumple su SLO se comunica en la retrospectiva con el motivo del retraso.


### 45.5 Ejemplo resuelto: una discrepancia que cambió el diseño (ABP sintética)

En la revisión independiente del diseño, una revisora externa de una empresa de abastecimiento de agua cuestionó el plan de permitir que el colector de monitorización enviara alertas directamente a la HMI. Su argumento: una avalancha de alertas podría distraer a los operadores durante una perturbación, y un colector comprometido obtendría una ruta hacia L2. El elemento de la lista «¿añade algún componente de seguridad un conducto hacia una zona de control?» se había marcado incorrectamente. La discrepancia se registra textualmente, el diseño cambia para que las alertas vayan al SOC y al teléfono del jefe de turno, y se cumple el SLO de revisión (comentarios respondidos en cinco días laborables).

### Ejercicios — capítulo 45

- **EX133 — Bloqueo.** Comentario de bloqueo para un reintento que falla de forma abierta. Rúbrica: 3 = cita el requisito de seguridad + pide la corrección; 2 = bloqueo vago; 1 = detalle menor; 0 = aprueba.
- **EX134 — Lista de comprobación.** Añada un elemento para derivadores serie. Rúbrica: 3 = específico; 2 = vago; 1 = intento mínimo; 0 = nada.
- **EX135 — Discrepancia.** Una frase de discrepancia registrada. Rúbrica: 3 = clara; 2 = con evasivas; 1 = vago; 0 = nada.

### Síntesis del capítulo

Revisiones que pueden decir que no, con una lista de comprobación y memoria.

### Siga estudiando — capítulo 45 de 50

[← Capítulo 44 (borrador)](#ch-44) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 46 (borrador) →](#ch-46)

<a id="ch-46"></a>

## Capítulo 46 — Proyecto final de ingeniería II

### Resultados de aprendizaje

Usted podrá (1) terminar la implementación conforme a la propuesta congelada; (2) ejecutar el Laboratorio de verificación II; (3) entregar la documentación para operadores y la titularidad operativa.

### 46.1 Congelación

La fecha de congelación de funcionalidades es real: después de ella, solo correcciones de seguridad. Las ideas nuevas van a una propuesta de continuación. El proyecto final de Lena se congeló en la v1.0 de su compilador. Tras la congelación, solo corrigió el bloqueo silencioso del cargador de vectores, porque podía ocultar un fallo, y registró cada idea nueva, como el soporte para una segunda planta, en una propuesta de continuación. La fecha de congelación se acordó con su supervisora en la fase de propuesta, así que nadie pudo tratarla como un objetivo flexible cuando las últimas semanas se complicaron.

### 46.2 Verificación

El proyecto final debe superar el Laboratorio II (capítulo 40) sobre datos de prueba sintéticos, con una lista de comprobación firmada. Lena volvió a ejecutar el Laboratorio II para el compilador en una máquina limpia construida a partir de la etiqueta v1.0, usando solo datos de prueba sintéticos. La máquina limpia no tenía artefactos de compilación en caché, de modo que cada resultado procedía del código fuente etiquetado. La lista de comprobación la firmaron Lena y su revisor, y el informe enumeraba cada prueba omitida con su motivo. Lena guardó el registro de compilación de la máquina limpia junto a la etiqueta v1.0, y en él consta tanto la ejecución bloqueada del cargador de vectores como la ejecución satisfactoria.

### 46.3 Documentación

Sección del runbook, ADR, tutorial para operadores con capturas de pantalla de la interfaz sintética, sin datos de la planta. Se requiere la firma de operaciones antes de etiquetar.

```python
"""Lab: alarm load per operator hour before and after rationalisation (synthetic counts)."""
before = {"T-1 high": 140, "T-2 high": 95, "R-101 temp": 30, "pump trip": 6, "comm loss PLC-A": 210, "door open": 75}
remove = {"comm loss PLC-A": 200, "door open": 70, "T-1 high": 110}   # chattering/duplicate alarms removed
hours = 24 * 7
tb = sum(before.values()); ta = tb - sum(remove.values())
print(f"week alarms before={tb} after={ta}")
print(f"per operator-hour before={tb/hours:.2f} after={ta/hours:.2f}")
top = max(before, key=before.get)
print(f"worst source before: {top} ({before[top]/tb:.0%} of load)")
```

Salida esperada:

```text
week alarms before=556 after=176
per operator-hour before=3.31 after=1.05
worst source before: comm loss PLC-A (38% of load)
```

> **Caso sintético — Ashford Batch Plant.** Un equipo del Proyecto final II de la cohorte de Lena entregó la distribución firmada de listas de permitidos; Laboratorio II en verde; runbook actualizado el mismo día.

El proyecto de ese equipo era independiente del proyecto final de Lena, el compilador. Su documentación del compilador la firmó operaciones antes de etiquetar, y su tutorial para operadores usa solo capturas del modelo sintético de nueve conductos. Un ingeniero de operaciones siguió el tutorial una vez sobre la copia de banco del modelo de nueve conductos antes de firmar.

### 46.4 Errores y límites

La magia de una demostración en un portátil, con el fallo cerrado despachado con vaguedades, no aprueba. En la revisión del proyecto final de Lena, la demostración de un compañero mostró una herramienta de políticas funcionando en un portátil, pero no pudo mostrar qué ocurría cuando faltaba el archivo de política. Los examinadores calificaron como no cumplido el requisito de fallo cerrado. La demostración de Lena borró la política en el banco y mostró la denegación con su código de motivo, y después la restauró, porque las afirmaciones sobre el fallo seguro deben demostrarse en situación de fallo, no describirse mientras todo funciona.

### Nota práctica

Prueba silenciosa del runbook: un segundo ingeniero sigue el runbook en frío sobre datos sintéticos mientras el autor guarda silencio. Los puntos donde se atasca se convierten en correcciones de la documentación.

### 46.1b Guion de la demostración y traspaso

La demostración del Proyecto final II sigue un guion sobre datos sintéticos: mostrar el fallo cerrado, mostrar el denominador de la cobertura y mostrar la alcanzabilidad del SIS. La demostración termina restaurando la política y mostrando que el tráfico vuelve a permitirse. Enlace el hash de la grabación de la ejecución silenciosa en el informe del Laboratorio II para la auditoría del director. La revisión del director visiona la grabación de la ejecución silenciosa y registra incidencias de documentación antes de la aprobación. El código de un proyecto final sin un responsable de operaciones en el momento de la fusión está sin terminar. Las incidencias de documentación surgidas de la grabación llevan la marca de tiempo en la que el ingeniero se atascó.

La demostración de Lena siguió este guion al pie de la letra. Su responsable de operaciones firmó en la fusión.

### Nota de campo: atasco en la ejecución silenciosa

La ejecución silenciosa del compañero se atascó por la falta de documentación de la clave de política de prueba. La corrección de la documentación se publicó el mismo día. El Proyecto final II no está terminado hasta que alguien que no escribió el código pueda accionar la ruta de parada solo con el runbook.



El traspaso a operaciones nombra al equipo responsable en README y CODEOWNERS antes de la aprobación del Laboratorio II.



Una demostración que se aparta de su guion se repite desde el principio.


### 46.5 Ejemplo resuelto: congelar y verificar (ABP sintética)

En la congelación del Proyecto final II, Lena etiqueta el compilador como v1.0 y vuelve a ejecutar toda la verificación en una máquina limpia a partir de la etiqueta: 214 pruebas unitarias, 18 conjuntos de vectores de conformidad, la comprobación de equivalencia de alcanzabilidad y la reproducción en el cortafuegos de banco. Una ejecución se bloqueó en silencio porque la API del cortafuegos de banco limitó la tasa del cargador de vectores; la corrección es un tiempo de espera con un mensaje de fallo explícito en lugar de un bucle de reintentos. La documentación incluye el guion de la demostración, la lista de objetivos excluidos y una nota de traspaso que indica qué pruebas requieren hardware de banco, para que un sucesor no confunda las pruebas omitidas con pruebas superadas.

### Ejercicios — capítulo 46

- **EX136 — Congelación.** ¿Qué se permite tras la congelación de funcionalidades? Rúbrica: 3 = solo correcciones de seguridad; 2 = errores; 1 = funcionalidades; 0 = nada.
- **EX137 — Artefactos.** Cinco artefactos de entrega. Rúbrica: 3 = cinco; 2 = tres; 1 = solo código; 0 = nada.
- **EX138 — Operaciones.** ¿Por qué se requiere la firma de operaciones además del Laboratorio II? Rúbrica: 3 = titularidad/preparación del runbook; 2 = vaga; 1 = burocracia; 0 = nada.

### Síntesis del capítulo

Congele, verifique, documente, nombre a operaciones; y después opere.

### Siga estudiando — capítulo 46 de 50

[← Capítulo 45 (borrador)](#ch-45) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 47 (borrador) →](#ch-47)

<a id="ch-47"></a>

## Capítulo 47 — Ensayo de fallo y recuperación

### Resultados de aprendizaje

Usted podrá (1) realizar un ensayo de fallos guionizado; (2) medir el tiempo de recuperación; (3) registrar acciones correctivas.

### 47.1 Guion

Inyecte: archivo de lista de permitidos borrado; almacén de hallazgos detenido; desfase de reloj; reproducción de eventos duplicados; grafo plano en lugar del zonificado. Observe las denegaciones, las colas, las alertas y el fallo de la comprobación de alcanzabilidad. En el ensayo de fallos en banco de ABP, el equipo de Lena borró el archivo de lista de permitidos mientras se reproducía tráfico, después detuvo el almacén de hallazgos, desfasó el reloj de la copia de banco de PLC-A y reprodujo eventos duplicados. Por último, sustituyeron el grafo zonificado por uno plano. Los observadores registraron si se denegaban las escrituras, si los hallazgos se encolaban, si saltaban las alertas y si la comprobación de alcanzabilidad fallaba con el grafo plano. Cada inyección se ejecutó por separado antes de intentar cualquier combinación.

### 47.2 Medidas

Tiempo hasta denegar todas las escrituras tras la pérdida de la política; tiempo hasta la alerta; tiempo hasta la restauración; hallazgos perdidos (deberían ser 0 con la cola); la comprobación de alcanzabilidad del SIS sigue fallando de forma cerrada con un grafo erróneo. En ABP, el ensayo midió 45 segundos hasta denegar todas las escrituras tras borrar la lista de permitidos, frente a un objetivo de 30 segundos. Las alertas saltaron dentro del objetivo y no se perdió ningún hallazgo, porque los borradores se encolaron mientras el almacén de hallazgos estaba caído. La comprobación de alcanzabilidad falló correctamente al sustituir el grafo plano, mostrando SIS-B como alcanzable. Cada medida la registró un observador con un cronómetro y se contrastó con los registros, de modo que las cifras no dependían de la memoria de nadie.

### 47.3 Acciones correctivas

Cada incumplimiento se convierte en un ticket con responsable y fecha límite, no solo en una diapositiva de lecciones aprendidas.

```python
# Lab 27 - residual CUSUM vs band on batch reactor level (synthetic)
import random
def run(seed, atk, det, k=0.8, h=6.0):
    rng=random.Random(seed); true=est=50.0; s=0.0; alarm=None
    for t in range(500):
        inflow=1.0+rng.gauss(0,0.05)+(0.08 if atk and t>=250 else 0)
        true+=inflow-0.02*true
        lvl=true+rng.gauss(0,0.3); fm=inflow+rng.gauss(0,0.02)
        if atk and t>=250: lvl=50+rng.gauss(0,0.3)
        if atk=="B" and t>=250: fm=1.0+rng.gauss(0,0.02)
        est+=fm-0.02*est
        hit=abs(lvl-50)>2.0 if det=="band" else False
        if det=="cusum":
            s=max(0.0,s+abs(lvl-est)-k); hit=s>h
        if hit and alarm is None: alarm=t
    return alarm
for det in ("band","cusum"):
    fa=sum(run(i,None,det) is not None for i in range(60))
    for atk in ("A","B"):
        hits=[a-250 for a in (run(i,atk,det) for i in range(60)) if a is not None and a>=250]
        print(f"{det} class{atk} FA={fa}/60 det={len(hits)}/60 mean_delay={sum(hits)/len(hits) if hits else float('nan'):.1f}")
```

Salida esperada:

```text
band classA FA=0/60 det=0/60 mean_delay=nan
band classB FA=0/60 det=0/60 mean_delay=nan
cusum classA FA=0/60 det=60/60 mean_delay=24.8
cusum classB FA=0/60 det=0/60 mean_delay=nan
```

> **Caso sintético — Ashford Batch Plant.** El ensayo mostró 45 s hasta denegar todas las escrituras; objetivo de 30 s: se acortó el intervalo de sondeo.

En ABP, el tiempo de denegación de 45 segundos se convirtió en un ticket para el responsable del monitor, con fecha límite. La corrección acortó el intervalo de comprobación de la política, y la inyección se repitió hasta cumplir el objetivo dos veces. El ticket se cerró solo después de la segunda ejecución satisfactoria, y la fecha del siguiente ensayo se reservó antes de que los observadores salieran de la sala.

### 47.4 Errores y límites

Los ensayos en ventanas de producción están prohibidos; use entornos sintéticos. Los ensayos de Lena en ABP se ejecutan en el entorno de banco con tráfico sintético, nunca durante una ventana de producción. Borrar la lista de permitidos en el monitor en vivo probaría la misma ruta de código, pero podría interrumpir las escrituras de ingeniería mientras un lote se ejecuta en R-101. La copia de banco de PLC-A y el tráfico reproducido de la línea troncal aportan la evidencia de tiempos necesaria. Las comprobaciones en producción tras una corrección son de solo lectura, como confirmar que la versión desplegada coincide con la probada en el banco.

### Nota práctica

Celebre los tickets registrados: son el resultado. Un ensayo con cero tickets suele haberse saltado las inyecciones difíciles.

### 47.1b Corrección sin culpables y recurrencia

Redacte los tickets correctivos contra componentes y runbooks, no contra personas que siguieron un mal procedimiento. Tras una corrección, repita la inyección que encontró la carencia. Cierre el ticket solo cuando la medida cumpla el SLO dos veces. Los observadores rotan para que nadie quede exento de forma permanente. Los observadores anotan tiempos y desviaciones; no arreglan nada en vivo. Sus tiempos se contrastan con los registros antes de fotografiar el marcador. Las fotos del marcador van al expediente. Los tickets de ABP siguen esta regla. No se culpó a nadie.

### Nota de campo: el olor de cero tickets

Un ensayo que produjo cero tickets se había saltado la inyección del grafo plano. Repetirlo con la inyección difícil generó tres tickets y endureció la barrera de alcanzabilidad del SIS. La inyección del grafo plano es ahora obligatoria en todos los ensayos.



Cada ticket correctivo enlaza el script de inyección y el valor medido que lo desencadenó.



Los observadores rotados reciben información sobre las medidas antes del ensayo, no durante él.


### 47.5 Ejemplo resuelto: ensayo de recuperación en el banco (ABP sintética)

El escenario del ensayo: la lógica de PLC-A se corrompe (simulado cargando un programa erróneo en el controlador de banco) durante un lote. Medidas: tiempo hasta detectar (alerta de cambio de programa, 35 s), tiempo hasta decidir (el jefe de turno elige la retención segura, 4 min), tiempo hasta restaurar la lógica verificada desde la copia de seguridad sin conexión (22 min) y tiempo hasta reanudar (41 min en total). El ensayo revela que el hash de la copia de seguridad nunca se había registrado, así que la verificación dependía de una comparación manual. Las acciones correctivas reciben responsables y fechas: registrar los hashes de las copias de seguridad, añadir un simulacro de restauración al calendario trimestral y hacer seguimiento de la recurrencia.

### Ejercicios — capítulo 47

- **EX139 — Inyección.** Una inyección y el comportamiento seguro esperado. Rúbrica: 3 = ambos; 2 = solo la inyección; 1 = vaga; 0 = insegura.
- **EX140 — Medida.** Medida principal para la inyección de pérdida de la política. Rúbrica: 3 = tiempo hasta denegar las escrituras; 2 = disponibilidad vaga; 1 = intento mínimo; 0 = nada.
- **EX141 — Acción.** Convierta un resultado de 45 s en el título de un ticket correctivo. Rúbrica: 3 = específico; 2 = vago; 1 = intento mínimo; 0 = nada.

### Síntesis del capítulo

Rómpalo a propósito; mida; abra tickets para las carencias.

### Siga estudiando — capítulo 47 de 50

[← Capítulo 46 (borrador)](#ch-46) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 48 (borrador) →](#ch-48)

<a id="ch-48"></a>

## Capítulo 48 — Expediente de evidencia

### Resultados de aprendizaje

Usted podrá (1) reunir un expediente cuyos hashes pueda recalcular un tercero; (2) estructurar clases de conservación; (3) excluir material de doble uso y de propiedad reservada.

### 48.1 Contenido

PDF del permiso de trabajo, JSON de ConduitSet/lista de permitidos, exportaciones de hallazgos, objetos de evidencia, manifiesto de hashes, versiones de las herramientas, informes de laboratorio. El lector puede verificar sin confiar en su portátil. El expediente CNHP de Lena en ABP contiene el permiso de trabajo firmado, el modelo de zonas y la lista de permitidos v1.4.2 como archivos, las exportaciones de hallazgos, los objetos de evidencia, un manifiesto de hashes, las versiones de las herramientas y los informes de laboratorio. Un auditor puede llevar el expediente a una máquina limpia y comprobar cada hash frente al manifiesto, sin necesitar acceso al portátil de Lena ni a su cuenta. La primera página explica cómo hacerlo en pocos pasos.

### 48.2 Conservación

Clases: trabajo de la ventana (90 días), evidencia sellada (años acordados), métricas agregadas (más tiempo). Los trabajos de borrado se prueban. En ABP, los datos de trabajo de cada ventana se conservan 90 días, y la evidencia sellada de los registros de cambios relevantes para la seguridad, siete años, según el calendario de registros del emplazamiento. Las métricas agregadas, como la caída de la tasa de alarmas de 556 a 176 por semana, se conservan más tiempo. Lena prueba cada trimestre el trabajo de borrado sobre una copia del almacén, para que los datos de trabajo caducados se eliminen de verdad en lugar de darse por desaparecidos.

### 48.3 Exclusiones

Ninguna carga útil, ninguna credencial activa, ninguna genealogía de lotes de propiedad reservada. Si no puede compartirse con seguridad con los asesores jurídicos, no tiene cabida.

> **Caso sintético — Ashford Batch Plant.** La v3 del expediente volvió a superar el recálculo de hashes tras un incidente de edición de findings.json; se incluyó una nota de proceso.

Lena comprueba cada archivo frente a la lista de exclusiones antes de sellar; una sola coincidencia detiene la compilación y nombra el archivo infractor, y así se detectó una captura en bruto olvidada en la carpeta de trabajo de la versión dos. Después de que un archivo de hallazgos se editara por error, se recalcularon los hashes de la versión tres y la nota de proceso explica cómo se encontró el error.

### 48.4 Errores y límites

Los expedientes en cuentas personales en la nube incumplen la residencia y la conservación. En ABP, un contratista copió una vez evidencia de una ventana en una carpeta personal en la nube para trabajar desde casa. La carpeta quedaba fuera del calendario de conservación del emplazamiento y fuera de la ubicación de datos aprobada, así que la copia se borró y la evidencia se restauró desde el almacén sellado. El expediente de Lena reside ahora solo en el almacén controlado, y el manifiesto registra su ubicación, de modo que cualquier copia en otro lugar es claramente no oficial y puede identificarse durante una auditoría.

### Nota práctica

Automatice la compilación de los expedientes a partir de etiquetas. Arrastrar archivos a mano es como los hallazgos acaban editados después del sellado.

### 48.1b Lista de comprobación del lector y registro de ocultaciones

Incluya al principio una página sobre cómo verificar este expediente. Al ocultar información, lleve un registro de ocultaciones (qué, por qué, quién) dentro del almacén sellado. Entregue el expediente a alguien ajeno al proyecto para un simulacro de recálculo de hashes. La generación del manifiesto hace fallar la compilación si alguna ruta coincide con una expresión regular de nombres prohibidos. Legibilidad para terceros: si alguien ajeno no encuentra el manifiesto o la versión del permiso de trabajo, el expediente no aprueba. Pruebe una vez por trimestre la restauración desde el expediente en una máquina limpia, como ejercicio calificado.

El expediente de Lena supera esta prueba cada trimestre.

### Nota de campo: expediente automatizado

make dossier ENG=2026-03-abp produce el zip y el manifiesto. Tras la automatización, cesó la clase de incidentes de edición de findings.json posterior al sellado. El camino fácil se convirtió en el camino seguro.



Las ocultaciones las revisa una segunda persona antes de sellar el expediente.



Un simulacro de recálculo de hashes fallido se registra como hallazgo contra la compilación del expediente, no contra el lector.



La etiqueta de compilación se imprime en la primera página del expediente junto al hash del manifiesto.


### 48.5 Ejemplo resuelto: qué entra y qué queda fuera (ABP sintética)

El expediente de evidencia CNHP de Lena incluye el modelo de zonas y su versión, los resultados de conformidad, los informes de laboratorio, la nueva prueba de validación, los hallazgos abiertos con sus responsables y la aceptación del riesgo residual firmada por el director de planta. Excluye las capturas de paquetes en bruto, las contraseñas y los parámetros de receta, que sustituye por hashes y referencias al almacén controlado; el registro de ocultaciones enumera cada exclusión y su motivo. La conservación sigue el calendario de registros del emplazamiento: siete años para los registros de cambios relevantes para la seguridad. La lista de comprobación del lector en la primera página indica a un auditor cómo verificar cualquier hash frente a los originales almacenados.

### Ejercicios — capítulo 48

- **EX142 — Manifiesto.** Esboce un formato de manifiesto de hashes (3 filas). Rúbrica: 3 = ruta + algoritmo + resumen; 2 = solo resúmenes; 1 = vago; 0 = nada.
- **EX143 — Clase.** Clase de conservación para el PDF del permiso de trabajo frente a las notas de borrador. Rúbrica: 3 = sellada frente a trabajo/borrado; 2 = parcial; 1 = lo mismo para siempre; 0 = nada.
- **EX144 — Excluir.** Un estudiante pega una contraseña en un hallazgo: ¿qué hace usted? Rúbrica: 3 = eliminarla, rotarla, hallazgo de proceso; 2 = solo eliminarla; 1 = ignorarlo; 0 = publicarla.

### Síntesis del capítulo

Los expedientes son verificables, están clasificados y son aburridamente seguros.

### Siga estudiando — capítulo 48 de 50

[← Capítulo 47 (borrador)](#ch-47) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 49 (borrador) →](#ch-49)

<a id="ch-49"></a>

## Capítulo 49 — Tesis de ingeniería

### Resultados de aprendizaje

Usted podrá (1) estructurar una tesis en torno a una afirmación sobre el programa; (2) defender las medidas y los límites; (3) citar correctamente SP 800-82, 62443, ATT&CK for ICS y los artículos de evaluación.

### 49.1 Afirmación

Una frase: qué construyó o midió usted y para quién. Ejemplo: la distribución firmada de listas de permitidos con semántica de fallo cerrado reduce las escrituras no autorizadas reenviadas en ensayos sintéticos. La afirmación de la propia Lena trataba de su compilador: para el modelo de nueve conductos de ABP, las reglas generadas coincidieron con la alcanzabilidad del diseño y detectaron tres errores que la revisión manual había pasado por alto. Su frase nombra lo que construyó, con qué modelo de planta se probó y qué mostró, de modo que un examinador pueda contrastar cada parte con la evidencia. La reescribió varias veces hasta que cada cláusula apuntó a un resultado concreto del cuerpo del trabajo.

### 49.2 Cuerpo

Trabajos relacionados, diseño, verificación, resultados con intervalos y clases de ataque, limitaciones, ética. La tesis de Lena sigue este orden. Los trabajos relacionados citan las normas en las que se basan sus métodos, cada una con una nota de uso. El diseño explica cómo el compilador convierte el modelo de zonas de ABP en reglas. La verificación muestra la comprobación de equivalencia y los vectores de conformidad, los resultados informan de los tres errores encontrados, las limitaciones indican que un modelo de zonas defectuoso se compilaría fielmente, y el capítulo de ética explica por qué no se tocó ninguna planta en vivo. Cada parte remite a evidencia.

### 49.3 Citas

Use URL/DOI verificados según la política de fuentes; no invente artículos. Anote las fechas de acceso. Giraldo et al. CSUR 2018 doi 10.1145/3203245; Urbina et al. CCS 2016 doi 10.1145/2976749.2978388.

> **Caso sintético — Ashford Batch Plant.** El borrador de la tesis usó solo datos de ensayos sintéticos y citó correctamente SP 800-82 Rev. 3.

Lena comprobó cada referencia de su tesis frente a su DOI o su URL oficial y registró la fecha de acceso. Cada cita lleva una nota que indica cómo se usó la obra, así que ninguna figura sin haberse leído. Su director revisó las notas.

### 49.4 Errores y límites

Una tesis que evalúa la habilidad de explotación queda fuera del alcance del programa. El trabajo de Lena mide si su compilador produce reglas correctas, no si ella es capaz de irrumpir en una planta. Su capítulo de ética indica que el trabajo usó solo exportaciones sintéticas del modelo de zonas de ABP y el cortafuegos de banco, y da un ejemplo de una petición que rechazó: probar las reglas generadas contra el cortafuegos de una planta en vivo. Los examinadores juzgan la ingeniería y la evidencia, de modo que la habilidad de ataque ni se demuestra ni se evalúa en la defensa.

### Nota práctica

La página de amenazas a la validez se califica. Los examinadores la leen primero. La extensión no es rigor; los límites estructurados sí.

### 49.1b Honestidad en los trabajos relacionados y reproducibilidad

Cite los marcos que realmente usó. Rellenar los trabajos relacionados con artículos no leídos se descubre en la defensa. Entregue lo suficiente para reproducir los ensayos sintéticos: hashes de los datos de prueba, SHA de las herramientas, scripts. «Disponible a petición» no es un apéndice de reproducibilidad. Ponga la frase de la afirmación en negrita en la primera página. Las notas de uso cortan de raíz el relleno de citas en la revisión del director. Dejar en blanco la página de amenazas a la validez suspende la barrera de la tesis, sea cual sea la calidad de la implementación.

La página de amenazas de Lena enumera como primera amenaza la dependencia del compilador de un modelo de zonas correcto, la misma limitación que nombra en su defensa.

### Nota de campo: la afirmación en la primera página

Examinadores y directores comparten el mismo objetivo cuando la frase de la afirmación está en negrita en la primera página. Unos trabajos relacionados escuetos y exactos, con notas de uso, superan a una bibliografía inflada que se derrumba ante la primera pregunta.



El apéndice de Lena permite a un examinador reproducir la comprobación de equivalencia en menos de diez minutos.



Cada entrada de los trabajos relacionados indica si el método citado se usó, se tomó como comparación o solo se comentó.


### 49.5 Ejemplo resuelto: una afirmación de la tesis con su evidencia (ABP sintética)

La afirmación de la tesis de Lena, en la primera página: «Para el modelo de nueve conductos de ABP, un compilador que genera reglas de cortafuegos y vectores de conformidad a partir de un modelo de zonas produjo reglas equivalentes en alcanzabilidad al diseño y detectó tres errores de reglas que la revisión manual había pasado por alto». El cuerpo respalda cada cláusula: la comprobación de equivalencia, los tres errores con sus vectores y los resultados de la revisión manual sobre el mismo conjunto de reglas. Los trabajos relacionados citan IEC 62443-3-2 para el método de zonas y conductos y NIST SP 800-82r3 para las orientaciones de segmentación, e indican con claridad que existen herramientas de verificación formal con las que el trabajo no se comparó.

### Ejercicios — capítulo 49

- **EX145 — Afirmación.** Afirmación de una frase para una tesis sobre la doble aprobación de conductos. Rúbrica: 3 = medible + acotada; 2 = vaga; 1 = afirmación de explotación; 0 = nada.
- **EX146 — Límite.** Un párrafo de limitaciones (3 frases). Rúbrica: 3 = validez externa clara; 2 = parcial; 1 = nada; 0 = afirmación exagerada.
- **EX147 — Cita.** Dé el DOI de Urbina et al. CCS 2016. Rúbrica: 3 = 10.1145/2976749.2978388; 2 = solo el título; 1 = erróneo; 0 = nada.

### Síntesis del capítulo

Una afirmación, límites honestos, citas reales.

### Siga estudiando — capítulo 49 de 50

[← Capítulo 48 (borrador)](#ch-48) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 50 (borrador) →](#ch-50)

<a id="ch-50"></a>

## Capítulo 50 — Defensa final

### Resultados de aprendizaje

Usted podrá (1) presentar la afirmación y la evidencia en 20 minutos; (2) responder preguntas sobre seguridad y medición; (3) indicar qué no volvería a hacer.

### 50.1 Estructura de la exposición

Afirmación; demostración sobre datos sintéticos; resultados de verificación; una lección del ensayo de fallos; límites; preguntas. Ninguna demostración de ataque a una planta en vivo. La defensa de Lena siguió este orden. Enunció su afirmación sobre el compilador, lo mostró con el modelo sintético de nueve conductos de ABP, presentó los resultados de equivalencia y de vectores y después expuso su reflexión sobre un fallo. Cerró con su diapositiva de limitaciones y una frase sobre lo que respalda la evidencia: reglas equivalentes al diseño en nueve de nueve conductos y tres errores que la revisión manual había pasado por alto. Nada en la exposición tocó un sistema en vivo, y cada cifra de sus diapositivas remitía a un artefacto del expediente.

### 50.2 Preguntas probables

¿Prueba del fallo cerrado? ¿Elección del denominador? ¿Límite del doble uso? ¿Independencia del SIS? ¿Qué se rompió en el Laboratorio II? Practique respondiendo con referencias a artefactos. Lena ensayó cada pregunta con su supervisora, respondiendo con una referencia a un artefacto en lugar de con una opinión. Para el comportamiento de fallo cerrado, remitió a los resultados del ensayo; para la independencia del SIS, a la comprobación de alcanzabilidad que muestra SIS-B inalcanzable desde todas las zonas enrutadas. Para el Laboratorio II, describió el defecto de desfase de reloj y su corrección. La pregunta más difícil, qué ocurre si el diseño es erróneo, fue la que más ensayó.

### 50.3 Reflexión

Termine con un error de diseño y su corrección: los examinadores confían en los ingenieros que han visto sus propios fallos.

```python
# Lab 1 - tank hold-up after feed pump stop (Ashford Batch Plant, synthetic)
import math
V0, VMIN = 12.0, 2.0   # m3 in feed tank T-1
def outflow(t):         # m3/h to reactor; t hours after stop of makeup
    return 1.8 + 0.4*math.sin(2*math.pi*t/6)
def drawn(t):
    return 1.8*t - (0.4*6/(2*math.pi))*(math.cos(2*math.pi*t/6)-1)
lo,hi=0.0,24.0
for _ in range(50):
    mid=(lo+hi)/2
    lo,hi=(mid,hi) if drawn(mid)<V0-VMIN else (lo,mid)
print(f"time to min level: {lo:.2f} h")
print(f"average-rate estimate: {(V0-VMIN)/1.8:.2f} h")
```

Salida esperada:

```text
time to min level: 5.53 h
average-rate estimate: 5.56 h
```

> **Caso sintético — Ashford Batch Plant.** La defensa de Lena empezó con el laboratorio de fallo cerrado y la alcanzabilidad del SIS, no con una diapositiva de logotipos. Cuando le pidieron una puntuación de riesgo, se negó y mostró la alcanzabilidad del SIS, los hallazgos críticos abiertos y los denominadores de la cobertura.

La reflexión de Lena fue el bloqueo silencioso durante la nueva ejecución de la congelación: su cargador de vectores había reintentado indefinidamente cuando el cortafuegos de banco le limitó la tasa, de modo que una ejecución fallida parecía una lenta.

### 50.4 Errores y límites

La defensa no es una presentación comercial para un proveedor de escáneres. La defensa de Lena no mencionó nombres de productos ni recomendó herramientas. Cuando un examinador le preguntó qué escáner comercial compraría, explicó que su trabajo producía reglas y evidencia para cualquier cortafuegos y que la elección del producto correspondía al proceso de compras de ABP. Sus diapositivas mostraban resultados y limitaciones, no logotipos, de modo que los examinadores juzgaron su trabajo por su evidencia y no por el marketing de ningún proveedor. Mantuvo esa línea en todo momento.

### Nota práctica

Veinte minutos significan ensayar con un cronómetro. Recortar la diapositiva de límites para ganar tiempo es el recorte equivocado: los examinadores necesitan su honestidad más que un cuarto clic de demostración.

### 50.1b Paquete para los examinadores y seguimiento posterior

Entregue a los examinadores, con un día de antelación, la frase de la afirmación, el resumen del Laboratorio II, la medida del ensayo de fallos y el párrafo de ética. Después de la defensa, programe una revisión de mantenimiento a los noventa días: equipo responsable, versiones fijadas, tickets correctivos. Archive la presentación junto al expediente, con hashes coincidentes. Mantenga una lista de pendientes para las ideas de los examinadores y procésela en una semana. Agradezca a los operadores que ejecutaron los ensayos sintéticos; una defensa sin sus registros es una narración. El último capítulo de la titulación es el primero de la custodia.

Lena envió su paquete con un día de antelación.

### Nota de campo: revisión a los noventa días

Noventa días después de la defensa se revisaron el equipo responsable, las versiones fijadas y los tickets correctivos. Una acción correctiva se había reabierto; se volvió a registrar con un SLO más estricto. La custodia empieza cuando terminan los aplausos.


### 50.5 Ejemplo resuelto: responder la pregunta más difícil de la defensa (ABP sintética)

Un examinador pregunta: «Su compilador demuestra que la alcanzabilidad es igual al diseño. ¿Y si el diseño es erróneo?». La respuesta preparada de Lena: el compilador verifica la implementación frente a la intención, no la intención frente a las amenazas; el propio diseño procedía de la evaluación orientada a las consecuencias y se revisó de forma independiente (capítulo 45); y la nueva prueba de validación (capítulo 38) encontró una deriva real que el compilador habría evitado. Cierra nombrando la limitación —un modelo de zonas defectuoso se compilaría fielmente— y el plan a noventa días para comparar la salida del compilador con el diseño independiente de un segundo equipo.

### Ejercicios — capítulo 50

- **EX148 — Esquema.** Esquema de la exposición en seis puntos. Rúbrica: 3 = afirmación, demostración, verificación, fallo, límites, preguntas; 2 = parcial; 1 = presentación comercial; 0 = nada.
- **EX149 — Respuesta.** De 3 a 4 frases para responder «¿cuál es su puntuación de riesgo?». Rúbrica: 3 = rechaza la puntuación vacía + alternativas; 2 = parcial; 1 = inventa una puntuación; 0 = nada.
- **EX150 — Error.** Un error real (de la historia sintética) y su corrección. Rúbrica: 3 = específico; 2 = vago; 1 = intento mínimo; 0 = nada.

### Síntesis del capítulo

Defienda la ingeniería, las medidas y los rechazos.

### Siga estudiando — capítulo 50 de 50

[← Capítulo 49 (borrador)](#ch-49) · [Índice de capítulos del curso](../SUBJECTS.md) · [Resultados resueltos ↓](#worked-results) · [Siguiente curso a través del índice de capítulos →](../SUBJECTS.md)

<a id="worked-results"></a>

## Resultados resueltos

Respuestas modelo para EX001–EX150. Ashford Batch Plant, Lena Okafor, el CNHP y todos los números son sintéticos. Cualquier respuesta que cumpla la rúbrica obtiene la misma puntuación.

**EX001.** (9 − 1,5) / 1,25 = 7,5 / 1,25 = 6,0 horas.

**EX002.** «Una condición de nivel bajo en T-2 deberá señalizarse al operador mediante alarma en menos de 4 horas desde la pérdida de reposición (6,0 h de autonomía menos 2 h de margen de respuesta), por una vía de alarma independiente del PLC que controla la bomba de reposición».

**EX003.** El término senoidal integra casi a cero a lo largo de un periodo completo de 6 horas, de modo que la extracción media es de 1,8 m³/h y 10/1,8 ≈ 5,56 h. Si la ventana cubriera solo la parte alta del ciclo, o la receta estuviera sesgada hacia una extracción alta, el tiempo real sería más corto que la estimación con caudal medio.

**EX004.** Desde A: B (directo), C y E (vía B), D (vía C). Conjunto alcanzable {A, B, C, D, E}.

**EX005.** Eliminar una arista solo puede reducir los conjuntos alcanzables, así que no puede exponer nada nuevo. Añadir L3→L1-SIS puede crear un camino hacia el sistema de seguridad desde cada zona que ya alcanza L3 —incluidas L4 y L5—, por lo que exige una comprobación completa de alcanzabilidad.

**EX006.** La arista L2→L1-SIS. L4 ya alcanza L2 (directamente vía L4→L2 y vía L3), de modo que ese único conducto de SCADA al SIS completa el camino; el diseño por zonas lo omite.

**EX007.** 120 × 10 = 1.200 bits; 1.200 / 19.200 = 0,0625 s = 62,5 ms.

**EX008.** Velocidad necesaria = 244 × 10 bits / 0,050 s = 48.800 bit/s. La siguiente velocidad estándar igual o superior es 57.600 bit/s; con 38.400 se desbordaría el presupuesto.

**EX009.** (1) Inyección de corriente en un lazo de 4–20 mA → sensor redundante con verificación cruzada. (2) Calentar o enfriar una sonda de temperatura → comprobación de plausibilidad con un modelo físico frente a la potencia del calentador. Las envolventes y los precintos con evidencia de manipulación también son controles aceptables.

**EX010.** permit(src, fc, reg): si src == "HIST-1" y fc in {3, 4} → PASS; si src == "HIST-1" en cualquier otro caso → BLOCK "fc-not-allowed". No figura ningún código de escritura (5, 6, 15, 16).

**EX011.** Pruebe 40001 y 40010 con HMI-1 fc=6; ambos PASS. 40011 queda fuera de range(40001, 40011) y debe dar BLOCK "register-out-of-range".

**EX012.** No hay ninguna tupla (ENG-WS, 8) en ALLOW, así que se bloquea con fc-not-allowed. La función 8 es de diagnóstico; una lista de denegación predeterminada obliga a que las necesidades de la estación de ingeniería se declaren y se aprueben en lugar de suponerse.

**EX013.** «Cualquier equipo en L2 puede enviar solicitudes de escritura Modbus a los registros de retención 40001–40010 del PLC-A sin autenticación (observado en una reproducción en banco, 3 de marzo). Un cambio del punto de consigna de nivel de T-1 podría llevar el nivel hacia el desbordamiento en unos 40 minutos; el disparo por nivel muy alto del SIS-B sigue siendo independiente y detendría la alimentación».

**EX014.** Operador: «Informe de cualquier cambio de punto de consigna en T-1 que usted no haya hecho». Ingeniero de seguridad funcional: «El SIS-B no es alcanzable desde las zonas de oficina; confirme que su prueba de disparo está al día». Directivo: «Eliminar FW-12 no cuesta tiempo de parada y cierra el camino de la oficina a SCADA».

**EX015.** «El acceso remoto del proveedor a la estación de ingeniería en L3 sigue siendo un camino hacia el PLC-A; se controla mediante sesiones de duración limitada a través del servidor de salto de la DMZ con aprobación del operador, y debería auditarse cada mes».

**EX016.** Tramas esperadas = 500 / 0,85 ≈ 588. El presupuesto de comunicaciones y las reglas de intervención (ROE) deben cubrir ~588, no 500.

**EX017.** B′ = 1,0 − 1,5 = −0,5/h, de modo que B(t) = 40 − 0,5t = 0 en t = 80 horas, suponiendo tasas constantes.

**EX018.** 210 / 556 ≈ 0,378, aproximadamente el 38 % de la carga semanal: la peor fuente individual.

**EX019.** Con 0 eventos en 60 ensayos, una cota superior aproximada al 95 % para la tasa es de unos 3/60 = 5 % (regla del tres) o una cota superior de Wilson cercana al 6 %. Puede decir que no se observaron falsas alarmas en esta muestra; no puede afirmar que la tasa sea cero en operación.

**EX020.** CUSUM clase A: det=60/60, mean_delay≈24.8 muestras (después de que el ataque comience en t=250).

**EX021.** «Ninguno de los dos detectores se activó con la clase B en 60 ensayos, así que esta muestra no permite clasificarlos; necesitamos una clase de ataque detectable o un diseño más grande antes de afirmar equivalencia o superioridad».

**EX022.** Ingeniería del SIS: cambiar los puntos de consigna de disparo, modificar la lógica de seguridad, forzar salidas de seguridad durante una prueba. HMI: cambiar puntos de consigna de regulación dentro de los rangos permitidos, reconocer alarmas, ver tendencias. Las listas exactas pueden variar si la división es clara.

**EX023.** El PLC y el SIS todavía pueden compartir sensores, alimentación, estaciones de ingeniería o una red de gestión. Un equipo de ingeniería comprometido puede reprogramar ambos aunque las VLAN de producción estén separadas. La independencia necesita controladores separados y un acceso de ingeniería controlado, no solo etiquetas de VLAN.

**EX024.** Exporte las listas de permitidos del HMI/PLC y las tablas de escaneo que muestran 40050 como escribible; o capture con un puerto espejo o un monitor serie durante una reproducción en banco. No escriba 40050 en la planta en servicio para «demostrarlo».

**EX025.** Al ingerir, si alguna clave coincide con (?i)payload|shell|exploit|password, rechácela con un 400. Ejemplo: `{"title":"x","payload":"..."}`.

**EX026.** Ambos comparten la huella (PLC-A, unauthorized-write, 40050); la inserción o actualización conserva una fila y adjunta los dos hashes de evidencia.

**EX027.** «Todo camino de L4 a L2 incluye L3.5» (o: L4 no tiene ninguna arista hacia L2/L1). La redacción exacta puede variar si es comprobable.

**EX028.** «No puedo proporcionar un exploit operativo ni un procedimiento de ataque contra un PLC real: es de doble uso y queda fuera de este curso. Puedo ayudarle a redactar un hallazgo a partir de evidencia sintética o indicarle el proceso de divulgación coordinada del proveedor».

**EX029.** Alarma de proceso inesperada; tiempo de ciclo o latencia por encima del presupuesto; falla o disparo del SIS; el contacto de seguridad de procesos ordena parar; sondeo de un equipo de la lista de denegados; cambio de punto de consigna sin explicación: cuatro cualesquiera con desencadenantes claros.

**EX030.** Unidades/activos dentro del alcance; métodos permitidos; ventana de fecha y hora; límites de impacto y de tasa; contactos de ingeniería y de seguridad de procesos nombrados; reglas de parada y reanudación. Firmado por alguien con autoridad sobre las unidades.

**EX031.** Ejemplo: el CRC o el entramado serie necesitan un monitor serie en la línea troncal; el código de función de Modbus TCP necesita captura y decodificación IP en el conducto; saber qué operador cambió un punto de consigna necesita un registro de auditoría del HMI o de la aplicación. Se aceptan otras ternas correctas.

**EX032.** Decodificación de solo lectura de Modbus TCP hacia el PLC-A desde HMI-1/HIST-1; solo los códigos de función 3/4/6; registros 40001-40010; ninguna escritura desde la estación de evaluación; ventana sábado 02:00-04:00 con el contacto de seguridad de procesos de guardia.

**EX033.** WRITE_REGS permite HMI-1 fc=6 solo para registros dentro de range(40001, 40011). 40003 está dentro (PASS); 40050 está fuera (BLOCK register-out-of-range).

**EX034.** Cuentas nominales de ingeniería; derechos de administrador mediante la pertenencia temporal y registrada a un grupo, con duración limitada; todas las descargas de lógica registradas; una segunda persona aprueba las descargas al SIS y al PLC de producción fuera de una ventana.

**EX035.** Parche de la base de datos del historiador (2,5 h, riesgo 5) aplazado: W1 se ocupó con el firmware del PLC-A y el del conmutador; W2, con el sistema operativo del HMI y el antivirus de eng-WS; no quedaban horas libres.

**EX036.** USB del proveedor permitido solo en eng-WS-2, 14 de marzo de 09:00 a 12:00, soportes analizados en un quiosco independiente, sesión grabada en video; el puerto se desactiva después.

**EX037.** Use solo la réplica del historiador en la DMZ (L3.5). SELECT limitado a `tag`, `value`, `timestamp`. LIMIT 10000. Sin volcados. Archivos destruidos en un plazo de 24 h, con confirmación en el ticket.

**EX038.** Obtenga credenciales de analista emitidas para la prueba; conéctese; intente un UPDATE/INSERT en una tabla de anotaciones de puntos de consigna; registre el éxito o el permiso denegado. Sin cargas útiles elaboradas.

**EX039.** Seguros: tag_id, value, quality_code, timestamp. Prohibidos: operator_name, customer_order_id, recipe_secret_key.

**EX040.** Lista de permitidos Modbus abp-modbus-v1.4.2 (SHA de git c0ffee1), cargada el 14 de marzo a las 02:05 desde el repositorio de versiones firmadas.

**EX041.** Toda solicitud de incorporación de cambios que amplíe conductos (arista o código añadidos, o denegación eliminada) necesita un ticket AUTH vinculado y un segundo responsable de código; las que restringen necesitan un responsable.

**EX042.** Una integración continua con credenciales de la VPN de planta tocaría sistemas fuera de una ventana autorizada por una persona, podría filtrar secretos en los registros y haría que las compilaciones dependieran de las redes de planta. Los datos de prueba sintéticos mantienen la integración continua segura y repetible.

**EX043.** Confidencialidad: poco impacto directo (escribir puntos de consigna no es leer). Integridad: cambio no autorizado del punto de consigna de nivel de T-1. Disponibilidad: el lote puede abortarse o entrar en enclavamiento. Seguridad funcional: el disparo por nivel muy alto del SIS-B sigue siendo independiente si los conductos se mantienen; dígalo de forma explícita.

**EX044.** Vulnerabilidad: escritura Modbus sin autenticación. Exposición: escribible desde la red de HMI de L2. Riesgo de proceso: el juicio del propietario de la planta sobre la probabilidad y la consecuencia de un desbordamiento dado el SIS-B, aceptado o corregido por él.

**EX045.** No publicamos una única puntuación de «hackeabilidad». Estas son las medidas: alcanzabilidad del SIS (no), críticos abiertos (1), alarmas por operador y hora (1,05), parches de alto riesgo aplazados (0).

**EX046.** «Ningún equipo de L4 deberá tener un conducto permitido hacia los servidores SCADA de L2; se verifica mediante alcanzabilidad en cada exportación del cortafuegos». «Toda visualización de datos de proceso desde L4 deberá usar la réplica del historiador en L3.5; se verifica por la ausencia de reglas directas de L4 a L2 y mediante pruebas de la ACL de la réplica».

**EX047.** Artefacto: lista de aristas por zonas sin L2 a L1-SIS y sin L4 a L2. Señal: lab_reach informa writes_to_SIS=True o L1-SIS en el conjunto alcanzable desde L4.

**EX048.** Nombre/identificador de la etiqueta, tipo de dato y unidades de ingeniería, frecuencia de actualización o de excepción, significado del código de calidad, responsable: tres cualesquiera con un significado claro.

**EX049.** kp=0.2 ki=0.01: final≈58.15, mae≈4.62, el mejor de los tres. El P puro (ki=0) deja un error estacionario mayor (final≈44.61).

**EX050.** Prefiera una derivación pasiva o una réplica de tráfico; la DPI en línea corre el riesgo de añadir una latencia comparable a la escala de tiempo del lazo. Mida primero en una copia de banco.

**EX051.** Aviso inmediato para los eventos cibernéticos relevantes para la seguridad funcional; agrupar los eventos medios en un resumen por turno; suprimir los duplicados con la misma huella durante 24 h.

**EX052.** PC de oficina en L4; historiador en L3; HMI en L2; PLC-A en L1; SIS-B en L1-seguridad. Controles: salto por la DMZ para la visualización desde L4; ninguna arista de L2 al SIS; lista de permitidos en Modbus. Se acepta cualquier esquema coherente con dos controles.

**EX053.** Los datos de recetas salen de la vía controlada de TO/TI hacia una cuenta personal no autorizada, lo que rompe la confidencialidad y la conservación.

**EX054.** Las pruebas usaron un entorno sintético que refleja la configuración de ABP; los resultados respaldan afirmaciones sobre esa configuración bajo el permiso de trabajo, no sobre el comportamiento del proceso en servicio ni sobre los datos de producción.

**EX055.** ¿Cuentas nominales o compartidas? ¿Locales o de directorio? ¿Pertenencia al grupo de administradores? ¿Último cambio de contraseña? ¿Procedimiento de emergencia? ¿Grabación de sesiones en los servidores de salto?

**EX056.** Vuelva a exportar desde el dispositivo o restaure la copia sellada; vuelva a verificar los hashes; compruebe quién escribió después de la hora del sellado; abra un hallazgo de proceso sobre ediciones no controladas.

**EX057.** Los secretos de planta y de ingeniería nunca se pegan en tickets, chat ni git; los tickets guardan solo un identificador de referencia de la bóveda y la marca de tiempo de la última rotación.

**EX058.** Ejemplo: orientación de seguridad de ICS con SP 800-82; zonas/conductos/SL con 62443; vocabulario de técnicas con ATT&CK ICS; detalles de los códigos de función con Modbus Application Protocol.

**EX059.** Diseñar y operar un programa autorizado de bastionado de la red de control que aplique zonas y listas de permitidos, mida la detección con honestidad y nunca ponga en peligro la seguridad de procesos ni exceda el permiso de trabajo firmado.

**EX060.** Exploits operativos contra PLC; escanear plantas en servicio sin permiso de trabajo; exportar la genealogía de lotes propietarios a los laboratorios; desactivar el SIS para facilitar una prueba.

**EX061.** Funcional: «Ninguna exportación del cortafuegos deberá contener un camino de L4 a L1-SIS; se verifica mediante la integración continua de alcanzabilidad». Seguridad funcional: «Si la política no puede cargarse, el punto de aplicación deberá denegar las sesiones nuevas y generar una alarma en menos de 30 s».

**EX062.** Dado que la ruta de la lista de permitidos está configurada pero falta el archivo; Cuando se produce cualquier llamada a permit(); Entonces el resultado es DENY con el motivo policy-unavailable y se dispara una alerta; no se reenvía ninguna trama de escritura.

**EX063.** Conflicto: los operadores quieren visualizar directamente de L4 a L2; seguridad funcional y de la información no quieren ninguna arista de L4 a L2. Regla elegida: visualización solo a través de la réplica del historiador en L3.5; regla directa prohibida; el acceso de emergencia se documenta aparte.

**EX064.** Las ediciones en el sitio borran qué conductos estaban vigentes en el instante t; el versionado permite que un hallazgo apunte al conjunto de reglas que estaba autorizado cuando se hizo la observación.

**EX065.** Volver a calcular el hash detecta los cambios; los archivos idénticos se fusionan; los tickets referencian bytes inmutables.

**EX066.** Rechazar los títulos que coincidan con patrones de asignación de contraseñas o con secretos de alta entropía; los revisores siguen comprobando; solo referencias a la bóveda en los metadatos de la evidencia.

**EX067.** Despliegue con la ruta de la lista de permitidos apuntando a un montaje vacío; llame a permit(); espere DENY policy-unavailable y una alerta; no se reenvía ninguna trama.

**EX068.** Cada evento de denegación guarda el identificador del actor autenticado y la versión de la política; el almacenamiento es de solo anexado; los borrados exigen doble control de emergencia.

**EX069.** El STRIDE del programa protege la integridad de la evaluación y la seguridad de procesos; los módulos de explotación aumentan el daño de doble uso y violan el límite del curso: no son mitigaciones.

**EX070.** Nombre: decodificación Modbus de solo escucha. Propósito: verificar las decisiones de la lista de permitidos. Privilegio: acceso a la derivación, sin inyección. Ruidoso: bajo. Impacto: solo latencia. Parada: tiempo de ciclo >50 ms o alarma de proceso. Artefactos: tabla de decisiones, hash de configuración, registro del tiempo de ciclo.

**EX071.** Las acciones sin un permiso de trabajo firmado no están autorizadas; es un fallo legal, ético y de seguridad de procesos, sea cual sea la intención.

**EX072.** Hash del diagrama de zonas actualizado; informe de alcanzabilidad; hash de la exportación del cortafuegos; borradores de hallazgos o un «ninguno encontrado» explícito con nota de cobertura.

**EX073.** Archivo JSON firmado: riesgo = los operadores olvidan firmar o verificar. Política codificada en el programa: riesgo = nuevos despliegues con cada cambio de la lista de permitidos, deriva entre dispositivos.

**EX074.** Las decisiones de denegación sobre códigos de función de escritura generan una alerta síncrona antes de reenviar, para que las condiciones de parada cumplan el objetivo del sensor; las lecturas permitidas pueden encolarse de forma asíncrona.

**EX075.** ¿Falla de forma cerrada? ¿Quién puede publicar la política? ¿Cuál es la latencia añadida en la línea troncal más lenta?

**EX076.** Criterio: el estado del SIS nunca sale de L1 sin el conmutador con llave. A alta si los monitores son locales; B media si la réplica excluye el SIS; C baja si las subidas incluyen etiquetas de seguridad funcional.

**EX077.** Opción C rechazada: los datos de proceso y los cercanos a las recetas saldrían del límite de residencia del sitio que exigen la política de ABP y la cláusula de datos del permiso de trabajo.

**EX078.** Cuando la WAN del sitio está caída o la vía en la nube queda fuera del permiso: ejecutar solo las listas de permitidos y los detectores locales, con registro manual de los hallazgos.

**EX079.** Preventivo: repositorio sellado de solo anexado con IAM de escritura única. Detectivo: un trabajo programado que vuelve a calcular los hashes y alerta ante una discrepancia.

**EX080.** Exige competencias de doble uso, no es determinista y puede dañar el proceso; prefiera volver a leer la configuración o las pruebas de la lista de permitidos.

**EX081.** (HIST-1, 16) no está en ALLOW, así que BLOCK fc-not-allowed: los historiadores no deben escribir múltiples registros.

**EX082.** permit(source, fc, register, allow_list: AllowListVersion) -> (bool, Reason). AllowListVersion fija, para la auditoría, qué reglas se evaluaron.

**EX083.** La prueba que comprueba BLOCK register-out-of-range para HMI-1 fc=6 reg=40050.

**EX084.** Secretos de autenticación; tramas en bruto que incluyen parámetros propietarios de recetas; identificadores personales de operadores si no son necesarios para la decisión.

**EX085.** cobertura = |observado ∩ planificado| / |planificado|. Usar todas las técnicas de ATT&CK for ICS como denominador hace que la cobertura parezca diminuta o incentiva una planificación basura: planifique las técnicas pertinentes para el encargo.

**EX086.** En la clase A, el CUSUM detecta 60/60 con un retardo de ~25 muestras; la banda detecta 0/60; ambos muestran 0/60 FA en este conjunto de semillas.

**EX087.** El estado sigue abierto hasta que se supera un ticket de nueva prueba; está prohibido el cierre automático por una promesa del proveedor.

**EX088.** ID V-04; preparación: montaje vacío de la lista de permitidos; acción: permit(cualquier escritura); resultado esperado: DENY policy-unavailable + alerta; evidencia: hash del registro.

**EX089.** Detener el laboratorio, abrir un bloqueante, revocar la aprobación de la ventana en planta hasta que se corrija y se supere de nuevo el laboratorio.

**EX090.** Hash del archivo de la lista de permitidos/política, hash de la compilación/versión del monitor, hash del registro de resultados del laboratorio.

**EX091.** Un reintento de red puede crear dos hallazgos con identificadores de servidor distintos; los clientes deberían hacer PUT con identificadores conocidos.

**EX092.** {"title":"x","payload":"..."} o {"password":"..."} o {"risk_score":42}: cualquier campo prohibido o desconocido según la política.

**EX093.** No: renombrar rompe los clientes; mantenga reason_code en v1 o publique /v2/.

**EX094.** Durante las ventanas firmadas, éxito del camino de denegación ≥ 99,5 %, medido con sondas sintéticas cada minuto; las caídas avisan al responsable.

**EX095.** La evaluación del alcance y de la lista de permitidos: debe fallar de forma cerrada y nunca dar ALLOW ante la incertidumbre.

**EX096.** Dejar de iniciar nuevos métodos de descubrimiento; avisar al responsable; mantener en marcha denegar/permitir; vaciar la cola antes de reanudar el descubrimiento.

**EX097.** Depositar el archivo /var/lib/otmon/STOP vía SSH/SSO; el monitor lo sondea cada 10 s; si existe o no puede leerse, deniega las escrituras y genera una alerta.

**EX098.** Binario firmado anterior disponible; AllowListVersion sin cambios o verificada de nuevo; el contacto de seguridad de procesos, avisado de la reversión.

**EX099.** A las 02:40, el tiempo de ciclo en la línea troncal A marca 62 ms durante tres minutos; el responsable está en una zona ruidosa con cobertura de radio irregular.

**EX100.** Para que los revisores sepan qué AllowListVersion autorizó la decisión cuando se disparó el evento.

**EX101.** El consumidor guarda los event_id procesados; los duplicados se ignoran o se insertan/actualizan sin tickets nuevos.

**EX102.** Un JSON de evento de ejemplo para el nuevo motivo y los campos esperados del ticket en el almacén de hallazgos tras consumirlo.

**EX103.** Proporción de las técnicas de ATT&CK for ICS planificadas que se observaron en esta ventana: no es una puntuación de riesgo residual ni de cumplimiento.

**EX104.** No publicamos insignias de riesgo rojo/ámbar/verde; en su lugar, use la alcanzabilidad del SIS, los críticos abiertos y los conteos de SLA/parches aplazados.

**EX105.** technique_id, name, planned (S/N), observed (S/N), first_seen_utc, notes.

**EX106.** bytes per cycle=244; tiempo por ciclo ≈ 21,2 ms a 115200 con 10 bits/byte.

**EX107.** Unos 29 ms de margen absorben los picos de decodificación y los reintentos; gastarlo todo no deja margen para que la condición de parada tenga sentido.

**EX108.** Cada uno puede enviar 2/s → ~6/s en total, el triple del permiso: hace falta un limitador compartido.

**EX109.** Desactivar las cuentas temporales; rotar los secretos de la bóveda; sellar los hashes de la evidencia; exportar las métricas de cobertura/alcanzabilidad del SIS; confirmar que el interruptor de corte está despejado; reservar la retrospectiva; comunicar a seguridad de procesos la hora de finalización.

**EX110.** Identificadores y estado de los hallazgos abiertos; último event_id procesado; solicitudes de aprobación pendientes; estado del interruptor de corte: tres o más cualesquiera.

**EX111.** Parche de la base de datos del historiador aplazado; el cierre debe registrar el riesgo residual y la fecha programada de la siguiente ventana (no aplazado para siempre).

**EX112.** Exportar las reglas actuales del cortafuegos; ejecutar la alcanzabilidad desde L4; esperar que L2/L1-SIS no sean alcanzables indebidamente; guardar los hashes; no enviar tráfico a la planta para demostrarlo.

**EX113.** De lo contrario, las métricas mienten y los tableros se ven verdes mientras el riesgo persiste.

**EX114.** La nueva prueba confirmó solo la configuración del banco/gemelo; el funcionamiento en la planta quedó fuera del alcance de la validación.

**EX115.** Fijar la versión exacta para la ventana; los parches de emergencia necesitan un minilaboratorio de verificación (capítulo 30) antes del cambio.

**EX116.** put_evidence(key: Hash, body: bytes) -> None / get_evidence(key) -> bytes.

**EX117.** Responsable: equipo de plataforma del CNHP (principal: Lena Okafor); respaldo: ingeniero de TO de guardia; contacto: #cnhp-monitors.

**EX118.** De lo contrario, la cobertura declara técnicas observadas sin un registro duradero del hallazgo: la métrica miente ante un fallo parcial.

**EX119.** Sigue permitiendo/denegando según la política local; encola borradores; alerta del crecimiento de la cola; nunca ALLOW ante errores de política.

**EX120.** El implementador del cambio y un segundo ingeniero que no escribió el código.

**EX121.** Omitir las comprobaciones de rango de registros para HMI previamente permitidos, o fallar de forma abierta cuando el servicio de políticas va lento.

**EX122.** La clave de caché incluye la versión de la política, el origen, el fc y el registro; TTL corto; invalidación forzosa al publicar la política.

**EX123.** Descarte el descubrimiento y la analítica de mejor esfuerzo antes que la evaluación de denegaciones: los operadores pueden esperar un escaneo; no pueden esperar una denegación que nunca llega.

**EX124.** ¿Reduce la exigencia de un denominador en los informes de cobertura las afirmaciones exageradas de los directivos sobre el porcentaje de seguridad en las encuestas posteriores a la ventana?

**EX125.** Número de fusiones que amplían conductos sin ticket AUTH por trimestre (o de intentos bloqueados).

**EX126.** Ese proyecto cruza la línea de doble uso del curso; considere estudiar en su lugar las tasas de fallo cerrado o las políticas de nueva prueba.

**EX127.** Si no puede cargarse el archivo de reglas de autorización, el sistema se niega a reenviar el tráfico de escritura y alerta al personal: no continúa en una incertidumbre que podría afectar a una capa de protección.

**EX128.** El host plc-a-prod-03 pasa a ser el host sintético PLC-A del entorno de laboratorio de Ashford.

**EX129.** Residencia de datos; prohibiciones de compra de SaaS extranjero; registro para conservación/FOIA; comités consultivos de cambios: dos cualesquiera, concretos.

**EX130.** Ninguna insignia de riesgo residual; ningún autodescubrimiento ATT&CK en vivo en las redes de la planta; ningún almacenamiento de cargas útiles.

**EX131.** El archivo del interruptor de corte detiene los reenvíos de escritura en 30 s; aceptación: prueba unitaria + V-KS de laboratorio en verde sobre datos sintéticos.

**EX132.** El trabajo usa datos sintéticos bajo los permisos de trabajo del curso. Ningún acceso no autorizado a la planta. Ningún desarrollo de exploits. Los problemas reales encontrados por accidente van a divulgación responsable, no al apéndice del informe.

**EX133.** Bloqueo: ante un tiempo de espera agotado del servicio de políticas, esto reintenta y luego permite (ALLOW), lo que viola el fallo cerrado de S-1. Cámbielo a DENY + alerta antes de fusionar.

**EX134.** Serie: confirma que el modo solo escucha y la condición de parada por tiempo de ciclo se prueban en el Laboratorio I.

**EX135.** Discrepancia: sigo prefiriendo alertas síncronas para todas las denegaciones durante la primera semana de una nueva lista de permitidos; desautorizada en ADR-019.

**EX136.** Correcciones de seguridad o de bloqueantes y correcciones de la documentación; ningún trabajo de funcionalidades.

**EX137.** Código + pruebas, informe del Laboratorio II con hashes, ADR, actualización del runbook, tutorial para operadores, declaración ética: cinco cualesquiera.

**EX138.** Sin un responsable de operaciones y un runbook ejecutable, un Laboratorio II en verde sigue dejando a la planta sin nadie capaz de detener y reanudar de forma segura.

**EX139.** Inyección: borrar el archivo de lista de permitidos. Esperado: denegar (DENY) las escrituras en 30 s, alerta, ningún ALLOW.

**EX140.** Segundos desde la inyección hasta la primera decisión de denegar todas las escrituras (y la alerta disparada).

**EX141.** Acortar el sondeo de política de otmon de 15 s a 5 s: la denegación total en el ensayo fue de 45 s > SLO de 30 s.

**EX142.** work-permit.pdf sha256 18d7…; allow-list.json sha256 01cc…; findings.json sha256 7f5f….

**EX143.** El PDF del permiso de trabajo, a evidencia sellada; las notas de borrador, a trabajo, con borrado a los 90 días o antes.

**EX144.** Eliminarla del almacén, rotar el secreto expuesto, abrir un hallazgo de proceso, volver a sellar el manifiesto y avisar al responsable.

**EX145.** Exigir doble aprobación y un ticket AUTH para las fusiones que amplían conductos redujo a cero los intentos de ampliación no aprobados en 12 semanas de datos sintéticos de CI de ABP.

**EX146.** Los ensayos usaron datos de prueba sintéticos, no tráfico real de la planta. Los resultados pueden no trasladarse a organizaciones sin CODEOWNERS. No medimos la fatiga de los revisores.

**EX147.** https://doi.org/10.1145/2976749.2978388

**EX148.** Afirmación; demostración sintética; resultados del Laboratorio II; lección del ensayo de fallos; límites/ética; preguntas.

**EX149.** No produzco una única puntuación de riesgo residual: no es reproducible. Aquí tiene si el SIS es alcanzable desde L4 (no), los hallazgos críticos abiertos y la cobertura de técnicas planificadas con denominadores; eso es lo que seguimos.

**EX150.** Ejemplo: almacenábamos en caché las decisiones de permiso sin la versión de la política en la clave; una publicación dejó ALLOW obsoletos. Corrección: incluir AllowListVersion en la clave de la caché e invalidarla por completo al publicar.

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; los marcos cambian, así que vuelva a verificarlos. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series overview. <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS. <https://attack.mitre.org/matrices/ics/>
- Modbus Application Protocol V1.1b3. <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
- NIST SP 800-82 Rev. 3. Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
