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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](../../en/book/MANUSCRIPT.md#ch-07) · [8](../../en/book/MANUSCRIPT.md#ch-08) · [9](../../en/book/MANUSCRIPT.md#ch-09) · [10](../../en/book/MANUSCRIPT.md#ch-10) · [11](../../en/book/MANUSCRIPT.md#ch-11) · [12](../../en/book/MANUSCRIPT.md#ch-12) · [13](../../en/book/MANUSCRIPT.md#ch-13) · [14](../../en/book/MANUSCRIPT.md#ch-14) · [15](../../en/book/MANUSCRIPT.md#ch-15) · [16](../../en/book/MANUSCRIPT.md#ch-16) · [17](../../en/book/MANUSCRIPT.md#ch-17) · [18](../../en/book/MANUSCRIPT.md#ch-18) · [19](../../en/book/MANUSCRIPT.md#ch-19) · [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) · [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) · [31](../../en/book/MANUSCRIPT.md#ch-31) · [32](../../en/book/MANUSCRIPT.md#ch-32) · [33](../../en/book/MANUSCRIPT.md#ch-33) · [34](../../en/book/MANUSCRIPT.md#ch-34) · [35](../../en/book/MANUSCRIPT.md#ch-35) · [36](../../en/book/MANUSCRIPT.md#ch-36) · [37](../../en/book/MANUSCRIPT.md#ch-37) · [38](../../en/book/MANUSCRIPT.md#ch-38) · [39](../../en/book/MANUSCRIPT.md#ch-39) · [40](../../en/book/MANUSCRIPT.md#ch-40) · [41](../../en/book/MANUSCRIPT.md#ch-41) · [42](../../en/book/MANUSCRIPT.md#ch-42) · [43](../../en/book/MANUSCRIPT.md#ch-43) · [44](../../en/book/MANUSCRIPT.md#ch-44) · [45](../../en/book/MANUSCRIPT.md#ch-45) · [46](../../en/book/MANUSCRIPT.md#ch-46) · [47](../../en/book/MANUSCRIPT.md#ch-47) · [48](../../en/book/MANUSCRIPT.md#ch-48) · [49](../../en/book/MANUSCRIPT.md#ch-49) · [50](../../en/book/MANUSCRIPT.md#ch-50) |

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

[← Capítulo 05 (borrador)](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 (borrador) →](../../en/book/MANUSCRIPT.md#ch-07)

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

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; los marcos cambian, así que vuelva a verificarlos. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series overview. <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS. <https://attack.mitre.org/matrices/ics/>
- Modbus Application Protocol V1.1b3. <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
- NIST SP 800-82 Rev. 3. Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
