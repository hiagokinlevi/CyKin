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
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](../../en/book/MANUSCRIPT.md#ch-19) · [20](../../en/book/MANUSCRIPT.md#ch-20) · [21](../../en/book/MANUSCRIPT.md#ch-21) · [22](../../en/book/MANUSCRIPT.md#ch-22) · [23](../../en/book/MANUSCRIPT.md#ch-23) · [24](../../en/book/MANUSCRIPT.md#ch-24) · [25](../../en/book/MANUSCRIPT.md#ch-25) · [26](../../en/book/MANUSCRIPT.md#ch-26) · [27](../../en/book/MANUSCRIPT.md#ch-27) · [28](../../en/book/MANUSCRIPT.md#ch-28) · [29](../../en/book/MANUSCRIPT.md#ch-29) · [30](../../en/book/MANUSCRIPT.md#ch-30) · [31](../../en/book/MANUSCRIPT.md#ch-31) · [32](../../en/book/MANUSCRIPT.md#ch-32) · [33](../../en/book/MANUSCRIPT.md#ch-33) · [34](../../en/book/MANUSCRIPT.md#ch-34) · [35](../../en/book/MANUSCRIPT.md#ch-35) · [36](../../en/book/MANUSCRIPT.md#ch-36) · [37](../../en/book/MANUSCRIPT.md#ch-37) · [38](../../en/book/MANUSCRIPT.md#ch-38) · [39](../../en/book/MANUSCRIPT.md#ch-39) · [40](../../en/book/MANUSCRIPT.md#ch-40) · [41](../../en/book/MANUSCRIPT.md#ch-41) · [42](../../en/book/MANUSCRIPT.md#ch-42) · [43](../../en/book/MANUSCRIPT.md#ch-43) · [44](../../en/book/MANUSCRIPT.md#ch-44) · [45](../../en/book/MANUSCRIPT.md#ch-45) · [46](../../en/book/MANUSCRIPT.md#ch-46) · [47](../../en/book/MANUSCRIPT.md#ch-47) · [48](../../en/book/MANUSCRIPT.md#ch-48) · [49](../../en/book/MANUSCRIPT.md#ch-49) · [50](../../en/book/MANUSCRIPT.md#ch-50) |

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
- **EX039 — Sintético.** Tres campos seguros para una tabla sintética de tanques y dos que no deben aparecer. Rúbrica: 3 = p. ej., tag, value, timestamp frente a operator_name, customer_order; 2 = parcial; 1 = débil; 0 = nada.

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

[← Capítulo 17 (borrador)](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 19 (borrador) →](../../en/book/MANUSCRIPT.md#ch-19)

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

**EX037.** Use solo la réplica del historiador en la DMZ (L3.5). SELECT limitado a tag, value, timestamp. LIMIT 10000. Sin volcados. Archivos destruidos en un plazo de 24 h, con confirmación en el ticket.

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

<a id="references"></a>

## Referencias

Enlaces comprobados el 12 de octubre de 2026; los marcos cambian, así que vuelva a verificarlos. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series overview. <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS. <https://attack.mitre.org/matrices/ics/>
- Modbus Application Protocol V1.1b3. <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
- NIST SP 800-82 Rev. 3. Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
