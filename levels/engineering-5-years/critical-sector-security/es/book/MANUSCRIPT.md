# Infraestructura crítica y seguridad sectorial: ingeniería de sistemas seguros y resilientes

- Idioma: español neutro (`es`); curso de ingeniería, cinco años; aproximadamente 4.000 horas de estudio planificado (curso 138 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–50 de 50 tienen texto didáctico escrito; los ejercicios EX001–EX100 (dos por capítulo) tienen sus resultados resueltos correspondientes; diecisiete laboratorios sin conexión están incluidos con su salida verificada. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La meta del plan de tres ejercicios por capítulo aún no se cumple. La cobertura de capítulos en borrador no es un libro terminado.
- Público: futuros diseñadores de sistemas de seguridad para servicios críticos: agua, electricidad, salud, transporte, finanzas y comunicaciones. Conocimientos de entrada: matemáticas y física de la educación secundaria; el libro construye cálculo, probabilidad, programación, redes e ingeniería de sistemas desde el capítulo 1.
- Relación con los demás libros de esta área: el [libro de maestría](../../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) enseña a diseñar, pilotar y defender un estudio empírico con revisión ética; el [libro de doctorado](../../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) exige una contribución original al conocimiento, validada de forma independiente. **Este libro de ingeniería trata de construir cosas**: derivar requisitos a partir de las consecuencias, elegir arquitecturas, implementar y verificar controles, medir la confiabilidad y el desempeño, ensayar la recuperación y defender con evidencia un sistema diseñado. Su capítulo de investigación (42) existe para resolver decisiones de diseño, no para publicar.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este curso es un proyecto educativo independiente. No es un título de ingeniería acreditado, no otorga licencia profesional y no concede autorización para acceder, escanear, probar o modificar ninguna infraestructura real. Toda organización, sitio, dispositivo, dirección, persona y número de un ejemplo resuelto es **sintético**, salvo que una frase cite explícitamente una fuente pública. Nada de lo que aquí aparece es un procedimiento operativo para una empresa de servicios, un hospital o un operador reales, y nada constituye asesoramiento jurídico.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los cincuenta capítulos siguen los diez semestres del plan. **Los capítulos 1–10** construyen los fundamentos matemáticos, físicos, informáticos y profesionales, cada uno aplicado a un problema de infraestructura desde la primera página. **Los capítulos 11–19** tratan redes, sistemas operativos, datos, ingeniería de software, fundamentos de seguridad, ingeniería de sistemas, control, arquitectura de seguridad, e identidad y criptografía. **El capítulo 20** establece el contexto sectorial. **Los capítulos 21–42** son el núcleo del campo: requisitos, modelos, análisis de amenazas y fallas, métodos, arquitecturas, controles, implementación, medición, confiabilidad, seguridad funcional y resiliencia, integración, desempeño, operaciones, validación, mantenibilidad, optimización e investigación aplicada, con dos talleres de diseño (25, 35) y dos laboratorios de verificación (30, 40). **Los capítulos 43–50** son la práctica y la secuencia del proyecto final: práctica profesional, proyecto final, revisión independiente, ensayo de falla y recuperación, expediente de evidencia, tesis y defensa.

Cada capítulo tiene resultados de aprendizaje, secciones didácticas con definiciones, un ejemplo resuelto, una actividad práctica, errores comunes y límites, dos ejercicios y una síntesis. Diecisiete capítulos incluyen un laboratorio sin conexión escrito para la biblioteca estándar de Python 3; las salidas impresas se obtuvieron ejecutando el código. Escriba su respuesta antes de abrir los [resultados resueltos](#worked-results).

Mantenga cuatro etiquetas en sus notas de ingeniería: **requisito** (lo que debe ser cierto, de forma verificable), **decisión de diseño** (lo que se eligió, por qué y qué la haría cambiar), **evidencia** (prueba, análisis, ensayo o revisión que respalda una afirmación, con su versión) y **riesgo residual** (lo que queda y quién es su responsable). La falla más común en el nivel de ingeniería no es un cálculo equivocado; es una afirmación que ninguna evidencia respalda, o un riesgo residual que nadie asume.

### El caso de diseño sintético usado en este libro

El libro sigue un único programa inventado, desde los primeros principios hasta la defensa final.

| Elemento sintético | Función | Límite |
|---|---|---|
| **Lowmarsh Regional Water Authority (LRWA)**: planta de tratamiento de agua de Fenwick, estaciones de bombeo PS1–PS6, el depósito de servicio de Hollin Hill de 4.000 m³, una sala de control y servidores SCADA, telemetría LTE privada, 42 estaciones de campo | El sistema que se diseña | Empresa de servicios inventada; ningún sitio, red o personal real |
| **Hospital St Brenna's** | Cliente crítico abastecido por Hollin Hill (a través de PS3) y directamente por PS4; unas 4 h de almacenamiento propio | Inventado |
| **Telemetry Modernisation and Resilience Programme (TMRP)** | El programa de diseño; necesidades N1–N4 y requisitos R1–R9 (capítulos 16 y 21) | Inventado |
| Alimentadores de red F1 y F2, el operador LTE, proveedores de RTU (RTU-A heredada, RTU-B nueva) | Dependencias y proveedores | Inventados; no se describe ningún producto real |
| Todas las direcciones (10.x.x.x), claves, probabilidades, costos y salidas de laboratorio | Datos didácticos | Sintéticos; la clave de demostración del Lab 8 es pública y nunca debe usarse |

### Política de fuentes

Toda afirmación factual sobre una ley, una norma, un incidente o un estudio publicado enlaza a una fuente consultada en octubre de 2026. Las leyes y las normas cambian: vuelva a verificar versiones y fechas antes de basarse en ellas. El conocimiento estándar de ingeniería (la ley de Ohm, la ley de Little, la definición de derivada) se enuncia sin cita o con una referencia clásica. Los incidentes se describen solo al nivel de sus fuentes públicas citadas y, cuando un relato inicial fue revisado (Oldsmar), se citan ambos. Las normas de acceso pagado (IEC 62443, IEC 61508) se citan por sus páginas públicas de catálogo o de presentación general; no cite cláusulas que no haya leído.

## Contenido


1. [Cálculo I](#ch-01)
2. [Matemática discreta](#ch-02)
3. [Física para la computación](#ch-03)
4. [Programación I](#ch-04)
5. [Comunicación en ingeniería](#ch-05)
6. [Cálculo II](#ch-06)
7. [Probabilidad y estadística](#ch-07)
8. [Arquitectura de computadoras](#ch-08)
9. [Programación II](#ch-09)
10. [Ética y seguridad en ingeniería](#ch-10)
11. [Redes y protocolos](#ch-11)
12. [Sistemas operativos](#ch-12)
13. [Sistemas de datos](#ch-13)
14. [Ingeniería de software](#ch-14)
15. [Fundamentos de seguridad](#ch-15)
16. [Ingeniería de sistemas](#ch-16)
17. [Fundamentos de control y realimentación](#ch-17)
18. [Arquitectura de seguridad](#ch-18)
19. [Identidad y criptografía](#ch-19)
20. [Infraestructura crítica y seguridad sectorial: contexto de ingeniería](#ch-20)
21. [Infraestructura crítica y seguridad sectorial: requisitos](#ch-21)
22. [Infraestructura crítica y seguridad sectorial: modelos de sistema y de datos](#ch-22)
23. [Infraestructura crítica y seguridad sectorial: análisis de amenazas y fallas](#ch-23)
24. [Infraestructura crítica y seguridad sectorial: métodos I](#ch-24)
25. [Taller de diseño I](#ch-25)
26. [Infraestructura crítica y seguridad sectorial: alternativas de arquitectura](#ch-26)
27. [Infraestructura crítica y seguridad sectorial: diseño de controles](../../en/book/MANUSCRIPT.md#ch-27)
28. [Infraestructura crítica y seguridad sectorial: implementación I](../../en/book/MANUSCRIPT.md#ch-28)
29. [Infraestructura crítica y seguridad sectorial: medición](../../en/book/MANUSCRIPT.md#ch-29)
30. [Laboratorio de verificación I](../../en/book/MANUSCRIPT.md#ch-30)
31. [Infraestructura crítica y seguridad sectorial: implementación II](../../en/book/MANUSCRIPT.md#ch-31)
32. [Infraestructura crítica y seguridad sectorial: confiabilidad](../../en/book/MANUSCRIPT.md#ch-32)
33. [Infraestructura crítica y seguridad sectorial: seguridad funcional y resiliencia](../../en/book/MANUSCRIPT.md#ch-33)
34. [Infraestructura crítica y seguridad sectorial: integración](../../en/book/MANUSCRIPT.md#ch-34)
35. [Taller de diseño II](../../en/book/MANUSCRIPT.md#ch-35)
36. [Infraestructura crítica y seguridad sectorial: desempeño y escala](../../en/book/MANUSCRIPT.md#ch-36)
37. [Infraestructura crítica y seguridad sectorial: operaciones](../../en/book/MANUSCRIPT.md#ch-37)
38. [Infraestructura crítica y seguridad sectorial: validación](../../en/book/MANUSCRIPT.md#ch-38)
39. [Infraestructura crítica y seguridad sectorial: mantenibilidad](../../en/book/MANUSCRIPT.md#ch-39)
40. [Laboratorio de verificación II](../../en/book/MANUSCRIPT.md#ch-40)
41. [Infraestructura crítica y seguridad sectorial: optimización del sistema](../../en/book/MANUSCRIPT.md#ch-41)
42. [Infraestructura crítica y seguridad sectorial: investigación aplicada](../../en/book/MANUSCRIPT.md#ch-42)
43. [Práctica en la industria o en el servicio público](../../en/book/MANUSCRIPT.md#ch-43)
44. [Proyecto final de ingeniería I](../../en/book/MANUSCRIPT.md#ch-44)
45. [Revisión independiente del diseño](../../en/book/MANUSCRIPT.md#ch-45)
46. [Proyecto final de ingeniería II](../../en/book/MANUSCRIPT.md#ch-46)
47. [Ensayo de falla y recuperación](../../en/book/MANUSCRIPT.md#ch-47)
48. [Expediente de evidencia](../../en/book/MANUSCRIPT.md#ch-48)
49. [Tesis de ingeniería](../../en/book/MANUSCRIPT.md#ch-49)
50. [Defensa final](../../en/book/MANUSCRIPT.md#ch-50)

Los [resultados resueltos](#worked-results) contienen EX001–EX100. Un [glosario](#glossary) y las [referencias](#references) cierran el libro.

<a id="ch-01"></a>

## Capítulo 1 — Cálculo I

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) leer una tasa de cambio como la magnitud física que vigila un operador: metros cúbicos por hora que salen de un depósito, megavatios que aumentan en un alimentador; (2) calcular una derivada y una integral definida para las curvas de demanda suaves que se usan en la planificación de infraestructura; (3) resolver problemas del tipo «cuánto falta hasta…» integrando una tasa y hallando el instante en que la cantidad acumulada alcanza un límite; y (4) explicar por qué el atajo de la tasa media puede sobrestimar el tiempo de autonomía. El capítulo inicia el caso de diseño del libro y prepara el capítulo 6, donde el mismo depósito se convierte en una ecuación diferencial con caudal de entrada y control.

### 1.1 Por qué un ingeniero de infraestructura necesita cálculo

Los servicios críticos son existencias y flujos. Un depósito es una existencia de agua tratada; las bombas y los consumidores son flujos. Un banco de baterías es una existencia de energía; la carga es un flujo. El tanque de combustible de un hospital, el empaquetamiento de una línea de gas, una cola de mensajes de telemetría sin procesar: cada uno es una cantidad que cambia a cierta tasa. Las preguntas de seguridad y resiliencia son casi siempre preguntas sobre estas cantidades bajo estrés. *Si las bombas se detienen porque su red de control cayó, ¿cuántas horas de suministro quedan?* *Si un atacante puede mantener abierta una válvula, ¿con qué rapidez sube el nivel?* La respuesta nunca es un único número de una hoja de datos; es la integral de una tasa en el tiempo, comparada con un límite que importa a las personas.

La derivada $dV/dt$ es la tasa instantánea a la que cambia una cantidad $V$. Si $V(t)$ es el volumen de un depósito en metros cúbicos y $t$ está en horas, $dV/dt$ está en m³/h. La integral definida $\int_a^b q(t)\,dt$ de un flujo $q$ es la cantidad total movida entre los instantes $a$ y $b$. El **teorema fundamental del cálculo** une ambas: si $V' = -q$, entonces $V(b) - V(a) = -\int_a^b q(t)\,dt$. Todo cálculo de autonomía de este libro es esa frase aplicada a una existencia real.

### 1.2 Derivadas que usará

Necesita un pequeño conjunto de herramientas: la derivada de un polinomio ($d/dt\, t^n = n t^{n-1}$), de la exponencial ($d/dt\, e^{kt} = k e^{kt}$), del seno y del coseno ($d/dt \sin(\omega t) = \omega\cos(\omega t)$), las reglas del producto y de la cadena, y la idea de punto estacionario, donde $f'(t) = 0$. La demanda diaria de una red de agua se aproxima a menudo con una media más una sinusoide de periodo de 24 horas. Si $d(t) = 150 + 60\sin(2\pi t/24)$ m³/h, entonces $d'(t) = 60\cdot(2\pi/24)\cos(2\pi t/24) \approx 15.7\cos(2\pi t/24)$ m³/h², de modo que la demanda crece más rápido (unos 15,7 m³/h por cada hora) cuando el coseno vale 1. Esa pendiente importa a un controlador de bombas: si las bombas solo pueden aumentar a 10 m³/h², irán por detrás de la demanda en su tramo más empinado.

### 1.3 Integrales y cantidades acumuladas

La antiderivada de la demanda anterior es $D(t) = 150t - \frac{60\cdot 24}{2\pi}\cos(2\pi t/24) + C$. El agua extraída desde el instante 0 hasta $T$ es $D(T) - D(0) = 150T - \frac{1440}{2\pi}(\cos(2\pi T/24) - 1)$. Observe lo que hace la sinusoide: a lo largo de un día completo se cancela, de modo que el total diario es simplemente $150 \times 24 = 3600$ m³; pero a lo largo de parte de un día no se cancela, y el *momento* en que empieza la interrupción cambia cuánto dura la existencia.

Para responder «¿cuándo alcanza el depósito su nivel mínimo seguro?», iguale el volumen extraído al volumen utilizable y despeje $T$. La mayoría de estas ecuaciones no tiene solución en forma cerrada, así que los ingenieros las resuelven numéricamente. La **bisección** divide por la mitad un intervalo que se sabe que contiene la respuesta hasta que es suficientemente pequeño; es lenta, pero no puede fallar si la función es continua y el intervalo inicial encierra la raíz.

### 1.4 Ejemplo resuelto: autonomía de Hollin Hill (sintético)

**Este caso es sintético.** El libro sigue a la inventada **Lowmarsh Regional Water Authority (LRWA)**, que opera la planta de tratamiento de agua de Fenwick, seis estaciones de bombeo (PS1–PS6) y el depósito de servicio de Hollin Hill de 4.000 m³, que abastece, entre otros clientes, al Hospital St Brenna's. LRWA inicia un **Telemetry Modernisation and Resilience Programme (TMRP)**, un programa de modernización y resiliencia de la telemetría; usted forma parte del equipo de ingeniería. Suponga que una falla en la red de telemetría detiene las bombas que alimentan Hollin Hill a las 06:00 (t = 0), cuando el depósito contiene 3.400 m³ (85 %). La política de operación considera el 20 % (800 m³) como el piso por debajo del cual la presión y las reservas contra incendios están en riesgo. La demanda es la $d(t)$ anterior, con t = 0 a las 06:00. El volumen utilizable es de 2.600 m³. Un planificador que divide por la demanda media obtiene 2.600/150 = 17,3 horas. Integrar la curva real da unas **14,6 horas**, porque la interrupción comienza cuando la demanda sube hacia su pico de la mañana y del mediodía. La diferencia de 2,7 horas no es redondeo; es la diferencia entre enviar a tiempo un equipo con un generador y no hacerlo.

### 1.5 Actividad práctica: Lab 1

Ejecute el laboratorio con la biblioteca estándar de Python 3. Halla el tiempo exacto por bisección, compara la integración temporal de Euler explícito con tres tamaños de paso e imprime la estimación por tasa media.

```python
# Lab 1 - how long does Hollin Hill reservoir last after the pumps stop? (synthetic, offline)
import math
V0, VMIN = 3400.0, 800.0          # m3: start at 85% of 4000, alarm floor at 20%
def demand(t):                     # m3/h, t in hours after the pumps stop (t=0 is 06:00)
    return 150.0 + 60.0 * math.sin(2 * math.pi * t / 24)
def drawn(t):                      # exact integral of demand from 0 to t
    return 150.0 * t - (60.0 * 24 / (2 * math.pi)) * (math.cos(2 * math.pi * t / 24) - 1)
lo, hi = 0.0, 48.0
for _ in range(60):                # bisection on drawn(t) = V0 - VMIN
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if drawn(mid) < V0 - VMIN else (lo, mid)
print(f"exact time to 20%: {lo:.2f} h")
for dt in (1.0, 0.1, 0.01):        # forward Euler
    v, t = V0, 0.0
    while v > VMIN:
        v -= demand(t) * dt; t += dt
    print(f"Euler dt={dt:<5} reaches 20% at {t:.2f} h")
print(f"constant-average model (150 m3/h): {(V0 - VMIN) / 150:.2f} h")
print(f"dV/dt at t=6 h: {-demand(6):.1f} m3/h")
```

Salida esperada:

```text
exact time to 20%: 14.62 h
Euler dt=1.0   reaches 20% at 15.00 h
Euler dt=0.1   reaches 20% at 14.70 h
Euler dt=0.01  reaches 20% at 14.63 h
constant-average model (150 m3/h): 17.33 h
dV/dt at t=6 h: -210.0 m3/h
```

Euler con un paso de una hora sobrestima el tiempo en unas 0,4 h; con 0,01 h difiere de la respuesta exacta en solo 0,01 h. La derivada en t = 6 h es −210 m³/h: el vaciado más rápido de la ventana.

Antes de confiar en el laboratorio, compruebe que sus números coinciden con el ejemplo resuelto: el tiempo exacto debe coincidir con la autonomía integrada de Hollin Hill, y la línea de tasa media debe reproducir la estimación más larga del planificador. Si cambia la hora de inicio, mantenga el piso en 800 metros cúbicos para que la comparación siga siendo justa. Un resultado que solo aparece con un tamaño de paso es una propiedad del método, no del depósito.

### 1.6 Errores comunes y límites

- Usar una tasa media para un flujo variable en el tiempo durante menos de un ciclo completo.
- Mezclar unidades (litros por segundo frente a metros cúbicos por hora: 1 L/s = 3,6 m³/h).
- Ignorar que el volumen «utilizable» excluye el almacenamiento muerto y las reservas.
- Confiar en un método numérico sin contrastarlo con un paso más pequeño o con un caso exacto.
- Tratar el modelo de demanda como un hecho. Una sinusoide es una aproximación de planificación; la demanda real tiene efectos del día de la semana, del clima y de los eventos, y la demanda durante una emergencia puede bajar (avisos de ahorro) o subir (personas que almacenan agua).

### Ejercicios — capítulo 1

**EX001 — Pendiente máxima.** *Objetivo:* usar una derivada para comparar la demanda con los límites de los equipos. *Entradas:* $d(t)$ de §1.2; bombas que pueden aumentar como máximo 12 m³/h por hora. *Pasos:* (1) halle $d'(t)$; (2) halle su máximo y la hora del reloj en que ocurre si t = 0 son las 06:00; (3) decida si las bombas pueden seguir la demanda en todo momento. *Evidencia esperada:* la derivación y una conclusión de ingeniería en una frase. *Rúbrica:* 3 = derivada, máximo y hora correctos, y la conclusión relaciona la pendiente con el límite de rampa; 2 = un desliz; 1 = solo la derivada; 0 = nada.

**EX002 — Autonomía con otra hora de inicio.** *Objetivo:* mostrar que la hora de inicio importa. *Entradas:* Lab 1. *Pasos:* cambie la demanda para que la interrupción empiece a las 18:00 (sustituya `sin(2πt/24)` por `sin(2π(t+12)/24)`), vuelva a ejecutar y compare con el resultado de las 06:00 y con la estimación por tasa media. *Evidencia esperada:* tres números y una recomendación de 100 palabras sobre qué valor debe citar un plan de emergencia. *Rúbrica:* 3 = números correctos y una recomendación de planificar con la peor hora de inicio creíble, con la razón; 2 = números correctos, recomendación débil; 1 = no ejecutado; 0 = nada.

### Síntesis del capítulo

La infraestructura está hecha de existencias y flujos. Una derivada es una tasa que se puede comparar con lo que los equipos pueden hacer; una integral es una cantidad que se puede comparar con un límite que protege a las personas. El tiempo de autonomía es una integral resuelta para su límite superior, por lo general numéricamente, y depende de cuándo empieza la perturbación. Contraste los resultados numéricos con una solución exacta o más fina, mantenga explícitas las unidades y nunca deje que un promedio sustituya a una curva cuando la curva es lo que la interrupción va a encontrar.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 50

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Matemática discreta

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) escribir condiciones de enclavamiento y de permiso como expresiones booleanas y comprobarlas de forma exhaustiva con una tabla de verdad; (2) modelar las dependencias de la infraestructura como un grafo dirigido y calcular qué falla cuando falla un nodo; (3) usar conjuntos, relaciones y conteo para acotar en cuántos estados puede estar un sistema de control; y (4) indicar con precisión cuándo una comprobación exhaustiva es factible y cuándo no. El capítulo se apoya en la visión de existencias y flujos del capítulo 1 y prepara el capítulo 4, donde implementará estos modelos en código.

### 2.1 La lógica es el lenguaje de los permisos

Los sistemas de control están llenos de reglas del tipo «la bomba puede funcionar solo si…». Escríbalas como expresiones booleanas. Sea $H$ = nivel por encima del límite alto, $S$ = presión de aspiración baja, $P$ = permiso remoto presente, $M$ = manual local seleccionado. Una regla típica es $\text{RUN} = \neg H \wedge \neg S \wedge (P \vee M)$. Dos reglas son equivalentes si coinciden en todas las entradas; las leyes de De Morgan ($\neg(A\wedge B) = \neg A \vee \neg B$) permiten reescribir condiciones de disparo como permisos. Con cuatro entradas hay $2^4 = 16$ estados, y una tabla de verdad comprueba cada uno. La ingeniería de seguridad añade una pregunta que la seguridad funcional ya se hace: *¿qué entrada puede influir un atacante?* Si $P$ llega por una red, entonces $P \vee M$ significa que un permiso falsificado basta para arrancar la bomba siempre que $H$ y $S$ sean falsos. Eso puede ser aceptable (los disparos físicos siguen actuando) o puede no serlo, si funcionar en ese momento provoca un transitorio de presión.

### 2.2 Los grafos modelan la dependencia

Un **grafo dirigido** $G = (V, E)$ tiene nodos y flechas. Trace una flecha de $a$ a $b$ cuando $a$ necesita $b$ para funcionar. El conjunto de lo afectado cuando $b$ falla es todo lo que puede alcanzar $b$ siguiendo las flechas: sus **ancestros** en esta orientación. La búsqueda en anchura calcula ese conjunto en un tiempo proporcional al número de aristas. [Rinaldi, Peerenboom y Kelly (2001)](https://doi.org/10.1109/37.969131) distinguen interdependencias físicas, cibernéticas, geográficas y lógicas entre infraestructuras; un grafo de dependencias es el modelo más simple que puede contener las cuatro, siempre que se etiquete cada arista con su tipo.

Vocabulario de grafos que usará: **camino**, **ciclo** (un bucle de dependencia; por ejemplo, la red de telemetría necesita la energía de la red eléctrica y la restauración del operador de la red necesita telemetría), **grado de entrada** y **grado de salida**, **vértice de corte** (un nodo cuya eliminación desconecta el grafo) y **componente fuertemente conexa**. Un vértice de corte en un grafo de suministro es un punto único de falla.

### 2.3 Conteo, espacios de estados y sus límites

Un sistema con $n$ entradas binarias tiene $2^n$ estados de entrada; con 30 entradas son más de mil millones. Si se añade memoria interna (temporizadores, enclavamientos con retención), el espacio de estados crece todavía más rápido. La comprobación exhaustiva es excelente para enclavamientos pequeños e imposible para plantas enteras; para estas se usa la estructura (descomposición, invariantes) y el muestreo (capítulo 30). El **principio del palomar** da cotas de seguridad rápidas: un contador de mensajes de 16 bits da la vuelta tras 65.536 mensajes, de modo que, a un mensaje por segundo, se repite en unas 18 horas, y a partir de ahí falla una comprobación contra repetición basada solo en ese contador.

### 2.4 Ejemplo resuelto: dependencias de Lowmarsh (sintético)

Los ingenieros de LRWA enumeran de qué depende el suministro del Hospital St Brenna's: del depósito de Hollin Hill y de la alimentación directa desde PS4; Hollin Hill depende de PS3; cada estación de bombeo necesita energía de la red eléctrica y su RTU; ambas RTU se comunican por una red LTE privada que, a su vez, se alimenta del alimentador F1 de la red. El Lab 2 codifica esto y calcula el conjunto de impacto de cada falla. Perder el alimentador F1 deja fuera de servicio la red LTE además de PS3, de modo que también se pierde la telemetría «redundante» de PS4, que está en el alimentador F2. El diseño de dos alimentadores parecía diverso en el plano eléctrico; el grafo muestra una dependencia común a través de las comunicaciones.

### 2.5 Actividad práctica: Lab 2

```python
# Lab 2 - dependency closure and an interlock truth table (synthetic Lowmarsh assets, offline)
from collections import deque
from itertools import product
DEPENDS = {  # asset: assets it needs in order to work
    "hospital_supply": ["hollin_res", "ps4"],
    "hollin_res": ["ps3"], "ps4": ["grid_f2", "rtu4"], "ps3": ["grid_f1", "rtu3"],
    "rtu3": ["lte"], "rtu4": ["lte"], "lte": ["grid_f1"], "fenwick_wtw": ["grid_f1", "chlorine"],
    "ps3_feed": ["fenwick_wtw"],
}
def impacted(failed):
    users = {}
    for a, ds in DEPENDS.items():
        for d in ds: users.setdefault(d, []).append(a)
    seen, q = {failed}, deque([failed])
    while q:
        n = q.popleft()
        for u in users.get(n, []):
            if u not in seen: seen.add(u); q.append(u)
    return sorted(seen - {failed})
for f in ("grid_f1", "lte", "grid_f2", "chlorine"):
    print(f"{f:9} -> {impacted(f)}")
# Pump P3 may run iff level below high AND suction not low AND (remote permit OR local manual)
rows = [(h, s, p, m, (not h) and (not s) and (p or m)) for h, s, p, m in product([0, 1], repeat=4)]
print("states allowing run:", sum(r[4] for r in rows), "of", len(rows))
```

Salida esperada:

```text
grid_f1   -> ['fenwick_wtw', 'hollin_res', 'hospital_supply', 'lte', 'ps3', 'ps3_feed', 'ps4', 'rtu3', 'rtu4']
lte       -> ['hollin_res', 'hospital_supply', 'ps3', 'ps4', 'rtu3', 'rtu4']
grid_f2   -> ['hospital_supply', 'ps4']
chlorine  -> ['fenwick_wtw', 'ps3_feed']
states allowing run: 3 of 16
```

Solo 3 de los 16 estados de entrada permiten que la bomba funcione: aquellos con $H = S = 0$ y al menos uno de $P, M$.

Lea despacio la lista de impacto del alimentador F1. Contiene la red LTE, ambas RTU y PS4, aunque PS4 se alimenta del alimentador F2, porque la RTU de PS4 llega a la sala de control solo a través de LTE. Esa es la dependencia común oculta que describe el ejemplo resuelto. El resultado de la tabla de verdad es igual de concreto: tres de dieciséis estados permiten que la bomba funcione, y todos ellos exigen que las entradas de nivel alto y de aspiración baja sean falsas, de modo que un permiso remoto falsificado por sí solo nunca puede arrancar la bomba en una condición de disparo.

### 2.6 Errores comunes y límites

- Trazar flechas en direcciones mezcladas («alimenta» frente a «depende de») en un mismo grafo.
- Tratar dos caminos como redundantes sin comprobar los nodos compartidos más abajo.
- Probar un enclavamiento solo con casos «típicos», cuando la tabla es lo bastante pequeña para probarlos todos.
- Olvidar que un grafo modela *si* algo funciona, no *cuán bien*: los modos degradados necesitan pesos o estados (capítulo 22).
- Elegir tamaños de contadores e identificadores sin contar cuánto tardan en dar la vuelta.

En LRWA estos errores tienen consecuencias directas: un grafo que mezcla direcciones de flechas indicaría que perder PS4 perjudica al alimentador F2, y una revisión que se detuviera en el plano eléctrico habría pasado por alto por completo la dependencia LTE compartida.

### Ejercicios — capítulo 2

**EX003 — Reescritura de un enclavamiento.** *Objetivo:* manipular expresiones booleanas y razonar sobre entradas que llegan por la red. *Entradas:* RUN de §2.1. *Pasos:* (1) escriba la condición de disparo $\neg\text{RUN}$ en forma de suma de productos usando las leyes de De Morgan; (2) enumere los estados en los que un permiso remoto falsificado cambia el resultado; (3) proponga un cambio que mantenga la operación remota pero exija una segunda condición independiente. *Evidencia esperada:* expresiones, lista y propuesta. *Rúbrica:* 3 = álgebra correcta, exactamente los estados correctos, propuesta independiente del mismo camino de red; 2 = un desliz; 1 = solo el álgebra; 0 = nada.

**EX004 — Comprobación de diversidad.** *Objetivo:* encontrar dependencias comunes ocultas. *Entradas:* Lab 2. *Pasos:* (1) añada un enlace satelital con respaldo de baterías, `sat`, que solo usa RTU4 y que no depende de la red eléctrica; (2) vuelva a ejecutar e informe el impacto de `grid_f1`; (3) indique si el suministro del hospital sobrevive ahora a la pérdida de F1 y qué sigue sin decirle el grafo. *Evidencia esperada:* diccionario modificado, salida, dos frases. *Rúbrica:* 3 = modelado correcto (que rtu4 dependa de lte *o* de sat obliga a señalar que este grafo simple solo modela dependencias de tipo Y), conclusión honesta sobre ese límite; 2 = salida correcta, límite omitido; 1 = no ejecutado; 0 = nada.

### Síntesis del capítulo

Escriba las reglas como lógica y las dependencias como grafos, y deje que la computadora las compruebe. Los enclavamientos pequeños pueden y deben comprobarse de forma exhaustiva; los sistemas completos no, y el conteo se lo indica. Busque nodos compartidos detrás de caminos aparentemente diversos, etiquete las aristas con su tipo y pregúntese, de cada entrada, cuáles llegan por una red que un adversario podría alcanzar.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 50

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Física para la computación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) usar la ley de Ohm, la potencia y la energía para dimensionar los suministros de respaldo de los equipos de control y de comunicación; (2) explicar la propagación de señales, el ruido y la atenuación lo suficiente para leer un balance de enlace; (3) relacionar el calor, la temperatura y la vida de los componentes con la confiabilidad de los gabinetes de campo; y (4) identificar los canales laterales físicos y los efectos electromagnéticos que importan para la seguridad. Se apoya en los capítulos 1–2 y prepara el capítulo 8 (arquitectura de computadoras) y el capítulo 11 (redes).

### 3.1 Electricidad para el ingeniero de sistemas

La tensión $V$ (voltios) impulsa la corriente $I$ (amperios) a través de la resistencia $R$ (ohmios): $V = IR$. La potencia es $P = VI$ vatios; la energía es la potencia integrada en el tiempo, $E = \int P\,dt$, que suele expresarse en vatios-hora. Una RTU de campo que consume 0,5 A a 24 V usa 12 W; con un módem LTE de 6 W y un pequeño conmutador Ethernet de 8 W, la carga del gabinete es de 26 W. Una batería de 24 V y 40 Ah almacena nominalmente 960 Wh; la energía utilizable es menor porque las baterías no deben descargarse por completo y su capacidad cae con la edad y el frío. Con una fracción utilizable de 0,6 y una eficiencia de conversión del 85 %, el gabinete funciona durante $960 \times 0.6 \times 0.85 / 26 \approx 18.8$ horas. Ese número es un **requisito de seguridad**, no un detalle de mantenimiento: si un corte de energía forma parte de un ataque, una telemetría que muere a las dos horas deja ciego al operador justo cuando más la necesita. El **ataque a la red eléctrica de Ucrania de diciembre de 2015** incluyó la inutilización de los sistemas de alimentación ininterrumpida de los centros de control, según el [caso de uso defensivo de E-ISAC y SANS](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and) y la [alerta de CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01).

### 3.2 Señales, ruido y enlaces

Las señales viajan por el cobre a una fracción significativa de la velocidad de la luz y por la fibra a aproximadamente dos tercios de ella, de modo que 100 km de fibra añaden unos 0,5 ms en un sentido: poco en comparación con los retardos de protocolo y de colas (capítulo 36). Los enlaces de radio pierden potencia con la distancia y los obstáculos; los ingenieros expresan ganancias y pérdidas en decibelios (dB), donde +3 dB es aproximadamente el doble de potencia y +10 dB, diez veces. Un balance de enlace suma la potencia del transmisor y las ganancias de las antenas y resta las pérdidas de trayecto y de cable; lo que queda por encima de la sensibilidad del receptor es el **margen de desvanecimiento**. [Shannon (1948)](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x) demostró que la capacidad de un canal depende del ancho de banda y de la relación señal/ruido, $C = B\log_2(1 + S/N)$. La consecuencia para la seguridad: un inhibidor de señal no necesita romper ninguna criptografía; solo necesita reducir $S/N$ por debajo de lo que el enlace necesita. La disponibilidad de la telemetría por radio es una propiedad física antes que criptográfica.

### 3.3 Calor y vida útil

Los componentes electrónicos fallan antes cuando están calientes. Una regla práctica de ingeniería muy usada, derivada de la relación de Arrhenius, dice que muchos mecanismos de falla duplican aproximadamente su tasa por cada aumento de 10 °C; trátela como una heurística que debe sustituirse por los datos del fabricante. Un gabinete sellado junto a la carretera, bajo el sol del verano, puede estar mucho más caliente que el aire. Implicaciones de diseño: reducir la carga nominal, ventilar o refrigerar, y monitorear la temperatura del gabinete; un aumento repentino también puede indicar una puerta que quedó abierta.

En los gabinetes de LRWA junto a la carretera, el sensor de temperatura debe informar al SCADA junto con la tensión de la batería, para que una tendencia ascendente sea visible antes de que los componentes envejezcan prematuramente.

### 3.4 Física y seguridad

Los efectos físicos filtran información y permiten provocar fallas. El consumo de energía y las emanaciones electromagnéticas pueden revelar claves criptográficas (canales laterales); los fallos inducidos de tensión o de reloj pueden hacer que un procesador se salte instrucciones; las filas de DRAM perturbadas por accesos repetidos pueden invertir bits en sus vecinas, como demostraron [Kim et al. (2014)](https://doi.org/10.1109/ISCA.2014.6853210). En la infraestructura, el acceso físico a los gabinetes de campo suele ser más fácil que el acceso por red, así que estos ataques no son exóticos. Los interruptores antimanipulación, los envolventes sellados y las claves guardadas fuera del dispositivo son los controles físicos.

En LRWA, el gabinete de cada estación de bombeo aloja la RTU y, tras el TMRP, su almacén de claves.

### 3.5 Ejemplo resuelto: autonomía del gabinete de PS4 (sintético)

El requisito R5 del TMRP de LRWA establece que la telemetría de campo debe sobrevivir a un corte de la red eléctrica de 24 horas. El gabinete previsto para PS4 consume 26 W. La energía utilizable necesaria con una eficiencia del 85 % es $26 \times 24 / 0.85 \approx 734$ Wh; con una fracción utilizable de 0,6, la capacidad nominal debe ser de al menos $734/0.6 \approx 1{,}224$ Wh, o unos 51 Ah a 24 V. Los ingenieros redondean hacia arriba a un banco estándar de 65 Ah para tener en cuenta el envejecimiento (la capacidad suele especificarse hasta un fin de vida del 80 %: $65 \times 0.8 = 52$ Ah, que sigue cumpliendo el requisito). Un diseño que cumpliera R5 solo con la batería nueva lo incumpliría en el tercer año.

### 3.6 Actividad práctica

Sin código: construya una hoja de cálculo o un script de diez líneas que calcule la autonomía de la batería a partir de la carga (W), la capacidad nominal (Wh), la fracción utilizable, la eficiencia y el factor de capacidad al fin de vida. Reproduzca §3.5 y, luego, añada un calefactor de gabinete de 15 W que funciona siempre que la temperatura exterior está por debajo de 0 °C, y vuelva a calcular. Use la carga de gabinete de 26 W, la eficiencia del 85 %, la fracción utilizable de 0,6 y el factor de fin de vida del 80 % del ejemplo resuelto, de modo que su primer resultado reproduzca la elección de 65 Ah. Después añada el calefactor y vea cuánto crece el requisito. Escriba la respuesta como una comprobación de requisito, no como un único número: indique si el banco sigue cumpliendo las 24 horas de R5 al fin de vida con tiempo frío y qué cambiaría si no lo hace. Mantenga visibles las unidades en cada columna.

### 3.7 Errores comunes y límites

- Dimensionar con la capacidad nominal de placa de la batería en lugar de la capacidad utilizable al fin de vida y con frío.
- Olvidar que el camino de comunicaciones (estaciones base celulares, repetidores de fibra) tiene su propia dependencia energética, fuera de su control.
- Tratar la protección criptográfica como protección de la disponibilidad.
- Usar reglas prácticas (la duplicación cada 10 °C) como predicciones precisas.

Cada uno de estos errores haría que R5 pareciera cumplido sobre el papel mientras se incumple en la práctica. Dimensionar para una batería nueva es el más común, porque el déficit solo aparece en el tercer año. Olvidar la dependencia energética del operador importa en LRWA porque la red LTE comparte el alimentador F1 con PS3. Tratar el cifrado como protección de la disponibilidad es el malentendido que el EX006 le pide corregir, y una regla práctica usada como predicción da un número de apariencia precisa sin ninguna base real detrás.

### Ejercicios — capítulo 3

**EX005 — Autonomía con calefactor.** *Objetivo:* dimensionar el almacenamiento de energía con una carga condicional. *Entradas:* §3.5–3.6. *Pasos:* calcule la capacidad nominal necesaria al fin de vida si el calefactor de 15 W funciona 10 de las 24 horas. *Evidencia esperada:* cálculo con unidades. *Rúbrica:* 3 = se aplican correctamente la energía y los factores de eficiencia, fracción utilizable y fin de vida; 2 = falta un factor; 1 = unidades erróneas; 0 = nada.

**EX006 — Inhibición de señal frente a cifrado.** *Objetivo:* separar confidencialidad e integridad de disponibilidad. *Entradas:* un comentario de revisión de diseño: «La telemetría LTE está cifrada, así que los ataques por radio están mitigados». *Pasos:* escriba una respuesta de 150 palabras que explique qué mitiga y qué no mitiga el cifrado y proponga dos controles físicos o de arquitectura. *Evidencia esperada:* la respuesta. *Rúbrica:* 3 = razonamiento sobre la inhibición y S/N, controles que abordan la disponibilidad (camino diverso, autonomía local, detección de la pérdida de enlace); 2 = controles genéricos; 1 = se mantiene la idea errónea; 0 = nada.

### Síntesis del capítulo

La energía, la señal y el calor son el punto donde lo cibernético se encuentra con lo físico. Dimensione la energía de respaldo para las condiciones de fin de vida y para la interrupción completa que incluye el modelo de amenazas; trate la disponibilidad por radio como una cuestión de relación señal/ruido, no de criptografía; diseñe los gabinetes pensando en el calor; y recuerde que el acceso físico abre canales laterales y ataques por inducción de fallas que ningún cortafuegos ve.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 50

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Programación I

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) escribir programas pequeños y correctos en Python con funciones, bucles, condicionales, bytes y diccionarios; (2) implementar un algoritmo publicado, el CRC-16 de Modbus RTU, y probarlo contra un vector conocido; (3) analizar entradas binarias no confiables de forma defensiva, rechazando los datos malformados en lugar de repararlos; y (4) explicar por qué el código de análisis sintáctico es crítico para la seguridad en la infraestructura. Convierte en código la lógica del capítulo 2 y prepara el capítulo 9.

### 4.1 Los programas como descripciones precisas

Un programa es una descripción de un cálculo lo bastante precisa para una máquina. El software de infraestructura debe ser preciso en tres cosas que los principiantes confunden: los **tipos** (un byte no es un carácter; un registro entero no es un número de coma flotante), los **límites** (qué ocurre en el primer y el último elemento, en cero, en el máximo) y la **falla** (qué hace el programa con una entrada que no esperaba). En este libro se usa Python porque su biblioteca estándar cubre bytes, hashing y simulación sin instalar nada. Su tipo `bytes` es inmutable y, al indexarlo, devuelve enteros; `int.from_bytes(b, "big")` convierte con un orden de bytes explícito.

### 4.2 Implementar la suma de verificación de un protocolo

Modbus es un protocolo industrial muy longevo; su forma serie (RTU) termina cada trama con una verificación de redundancia cíclica de 16 bits, enviada con el byte bajo primero, tal como la definen las [especificaciones del protocolo de aplicación Modbus y de línea serie publicadas por la Modbus Organization](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf). Un CRC detecta con alta probabilidad la corrupción accidental, como el ruido en una línea serie. **No** es un mecanismo de seguridad: cualquiera puede calcular un CRC válido para una trama falsificada. Aprenda pronto la diferencia: integridad frente a la naturaleza frente a integridad frente a un adversario (capítulo 19).

El CRC estándar de Modbus empieza en 0xFFFF, aplica XOR de cada byte sobre los bits bajos y desplaza a la derecha ocho veces, aplicando XOR con 0xA001 cuando el bit expulsado es 1. Un vector de prueba muy difundido es la petición `01 03 00 00 00 0A` (unidad 1, leer 10 registros de retención desde la dirección 0), cuyos bytes de CRC son `C5 CD`. Probar contra un vector antes de usar su función no es negociable.

### 4.3 Análisis sintáctico defensivo

Un analizador que lee datos de un dispositivo de campo, de una red o de un archivo es la frontera entre el mundo exterior y las suposiciones de su programa. Reglas: compruebe la longitud antes de indexar; compruebe la integridad (CRC) antes de confiar en cualquier campo; compruebe cada campo contra lo que usted pidió (unidad, función, número de bytes); compruebe los valores contra los límites físicos; ante cualquier falla, **rechace e informe**: no adivine. Las listas de debilidades comunes de OWASP y CWE ([CWE Top 25](https://cwe.mitre.org/top25/)) están dominadas por errores de manejo de entradas: lecturas y escrituras fuera de límites, validación de entradas inadecuada, desbordamiento de enteros.

### 4.4 Ejemplo resuelto: lectura del nivel de Hollin Hill (sintético)

La RTU de LRWA en PS3 devuelve dos registros: el nivel del depósito en centímetros y la presión de salida en kPa. El Lab 3 construye la trama de petición y luego analiza cinco respuestas: una correcta, una con un solo bit invertido, una excepción Modbus, un valor fuera del rango físico del tanque (65535 cm, un registro sin inicializar) y una trama truncada. Cada caso erróneo se rechaza con un motivo sobre el que un operador o un analista de registros puede actuar.

Cada motivo de rechazo está redactado para que apunte a una causa: una falla de CRC sugiere ruido en la línea, una excepción apunta al propio estado de la RTU y una falla de rango sugiere una avería o un registro sin inicializar que mantenimiento debe investigar.

### 4.5 Actividad práctica: Lab 3

```python
# Lab 3 - Modbus RTU CRC-16 and a defensive response parser (offline)
def crc16(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return crc
def frame(body: bytes) -> bytes:
    c = crc16(body); return body + bytes([c & 0xFF, c >> 8])   # low byte first
req = frame(bytes.fromhex("01030000000A"))
print("request:", req.hex(" "))
def parse(resp: bytes, unit=1, count=2, lo=0, hi=4000):
    if len(resp) < 5: return "reject: short"
    if crc16(resp[:-2]) != resp[-2] | resp[-1] << 8: return "reject: crc"
    if resp[0] != unit: return "reject: unit"
    if resp[1] & 0x80: return f"reject: exception {resp[2]}"
    if resp[1] != 3 or resp[2] != 2 * count or len(resp) != 5 + 2 * count: return "reject: shape"
    vals = [int.from_bytes(resp[3 + 2*i:5 + 2*i], "big") for i in range(count)]
    if any(not lo <= v <= hi for v in vals): return f"reject: range {vals}"
    return f"ok {vals}"
good = frame(bytes.fromhex("010304") + (3150).to_bytes(2, "big") + (212).to_bytes(2, "big"))
tests = {"good": good, "bitflip": good[:4] + bytes([good[4] ^ 1]) + good[5:],
         "exception": frame(bytes.fromhex("018302")), "outrange": frame(bytes.fromhex("010304FFFF00D4")),
         "truncated": good[:6]}
for k, v in tests.items(): print(f"{k:9} {parse(v)}")
```

Salida esperada:

```text
request: 01 03 00 00 00 0a c5 cd
good      ok [3150, 212]
bitflip   reject: crc
exception reject: exception 2
outrange  reject: range [65535, 212]
truncated reject: crc
```

La trama truncada se rechaza en la comprobación de CRC porque sus dos últimos bytes no son un CRC; un analizador que comprobara primero la forma daría un motivo más claro. Ambos órdenes son seguros; la propiedad importante es que nada se acepta con evidencia parcial.

Observe que la respuesta correcta se decodifica como un nivel de 3.150 cm y una presión de 212 kPa, ambos dentro de los límites físicos configurados en el analizador. El caso fuera de rango muestra por qué reparar es peligroso: recortar 65.535 al máximo de 4.000 cm informaría de un depósito lleno cuando el registro nunca se había escrito. Rechazarlo con el valor bruto en el motivo da al personal de mantenimiento la pista que necesita y da a un investigador evidencia de que el valor no era simplemente ruido en la línea.

### 4.6 Errores comunes y límites

- Errores de orden de bytes (los registros Modbus son *big-endian*; el CRC se transmite con el byte bajo primero).
- Indexar antes de comprobar la longitud; confiar en un campo de longitud dentro del mensaje.
- Tratar un CRC como autenticación.
- «Reparar» una entrada errónea (recortar 65535 a 4000) en lugar de rechazarla, lo que oculta fallas y ataques.
- Escribir pruebas solo para el camino feliz.

Cada punto tiene una prueba correspondiente en el Lab 3 o en el EX008. Un analizador que supera esas pruebas pero nunca se comprobó contra una trama truncada o malformada solo se ha probado para el camino feliz, y la primera línea serie ruidosa de una estación de bombeo mostrará qué hace con una entrada que no esperaba. Escriba primero las pruebas de falla, porque son las que importan cuando algo sale mal en el campo.

### Ejercicios — capítulo 4

**EX007 — CRC a mano y con código.** *Objetivo:* verificar una implementación. *Entradas:* Lab 3. *Pasos:* (1) calcule con la función el CRC de `01 06 00 01 00 03` (escribir un único registro); (2) invierta un bit de los datos y muestre que el CRC cambia; (3) explique en dos frases por qué el CRC no detiene a un atacante en la línea serie. *Evidencia esperada:* valores hexadecimales y explicación. *Rúbrica:* 3 = CRC correcto (verifíquelo con el resultado resuelto), demostración, afirmación de seguridad correcta; 2 = falta uno; 1 = código no ejecutado; 0 = nada.

**EX008 — Endurecimiento del analizador.** *Objetivo:* mejorar el informe de errores sin debilitar las comprobaciones. *Entradas:* `parse()`. *Pasos:* reordene las comprobaciones para que una trama truncada informe «short» o «shape» antes del CRC, añada una comprobación que rechace una respuesta cuyo identificador de unidad sea 0 (difusión) y añada dos casos de prueba. *Evidencia esperada:* diff del código y salidas. *Rúbrica:* 3 = se conservan todos los rechazos originales, comprobaciones nuevas correctas, pruebas incluidas; 2 = se pierde un rechazo; 1 = sin probar; 0 = nada.

### Síntesis del capítulo

Escriba código explícito sobre tipos, límites y fallas. Implemente los algoritmos publicados contra los vectores de prueba publicados. Trate cada analizador como una frontera de seguridad: longitud, integridad, forma y, después, significado físico; y rechace con un motivo en lugar de adivinar. Mantenga separadas en su mente la detección de errores accidentales (CRC) y la integridad frente a adversarios (MAC y firmas).

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 50

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Capítulo 5 — Comunicación en ingeniería

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) escribir un requisito que pueda verificarse; (2) producir una nota de diseño de una página, un registro de decisión y un informe de pruebas que otro ingeniero pueda comprobar; (3) presentar el riesgo y la incertidumbre a operadores, directivos y reguladores sin exagerarlos ni ocultarlos; y (4) tratar adecuadamente en los documentos los detalles sensibles de la infraestructura. Se apoya en los capítulos 1–4, cuyos números ahora tiene que comunicar, y prepara los talleres de diseño (capítulos 25 y 35).

### 5.1 Escribir para decidir

Los documentos de ingeniería existen para que alguien pueda tomar o comprobar una decisión. Empiece por la decisión y su fundamento; ponga las derivaciones después. Una buena nota de diseño responde, en este orden: qué se decide, qué opciones se consideraron, la recomendación, la evidencia y los supuestos en que se basa, qué cambiaría la recomendación y quién debe aprobarla. Los **registros de decisiones de arquitectura** (notas breves, fechadas y numeradas que registran una decisión, su contexto y sus consecuencias) mantienen visibles las razones de un diseño años después, cuando el equipo original ya se ha ido.

### 5.2 Requisitos que pueden verificarse

Un requisito es un enunciado que el sistema debe cumplir, redactado de modo que una prueba, un análisis, una inspección o una demostración puedan mostrar si lo cumple. El [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) recomienda requisitos necesarios, inequívocos, verificables, factibles y trazables. Compare «La telemetría deberá ser segura» (no verificable) con «Cada mensaje de telemetría de una RTU de campo al centro de control deberá llevar un código de autenticación de mensajes sobre su contenido y un contador monótono; el receptor deberá rechazar los mensajes que fallen cualquiera de las dos comprobaciones y generar una alarma en menos de 60 s» (verificable mediante prueba). Use «deberá» para los requisitos, mantenga un requisito por frase y dé a cada uno un identificador.

### 5.3 Números, incertidumbre y figuras

Informe los números con unidades, el método que los produjo y su incertidumbre o sus supuestos: «autonomía de 14,6 h (modelo de demanda integrada, inicio a las 06:00, nivel inicial del 85 %; 17,3 h si se supone la demanda media)». Prefiera tablas para los valores exactos, gráficos de líneas para las series temporales y nunca un gráfico sin ejes rotulados y unidades. Evite la falsa precisión: una autonomía de batería calculada con cargas estimadas es «unas 19 h», no «18,83 h». Haga que las figuras se lean en escala de grises y por personas con deficiencias en la visión del color.

En LRWA, la cifra de autonomía del expediente del TMRP lleva su hora de inicio y su nivel inicial, para que nadie la cite en otro escenario.

### 5.4 Comunicar el riesgo a distintos lectores

Los operadores necesitan saber qué hacer y cuándo; los directivos, la consecuencia, el costo y las opciones; los reguladores, evidencia de cumplimiento y de razonamiento. El mismo hallazgo («las consignas remotas se aceptan sin autenticación») se convierte, para un operador, en «hasta que se corrija, confirme por teléfono con la sala de control cualquier cambio de consigna inesperado»; para un directivo, en «una orden falsificada podría arrancar o detener bombas; costo de la corrección 120 k, tres meses»; para un regulador, en una brecha de control mapeada con un plan fechado. Ninguna de estas versiones puede contradecir a otra.

### 5.5 Información sensible

Los documentos de infraestructura contienen a menudo direcciones de red, modelos de dispositivos, vulnerabilidades y límites de capacidad. Marque los documentos según su sensibilidad, compártalos según la necesidad de saber y elimine detalles de las versiones destinadas a públicos amplios. Los informes públicos y los trabajos de los estudiantes deben describir los sistemas al nivel de la [guía de seguridad de TO del NIST (SP 800-82 Rev. 3)](https://csrc.nist.gov/pubs/sp/800/82/r3/final), es decir, patrones de arquitectura, y no las debilidades concretas de un operador identificado.

En este libro todas las cifras de LRWA son sintéticas, pero practique el hábito de todos modos: marque las notas de diseño para uso interno, mantenga las direcciones de red fuera de las diapositivas y produzca una versión reducida para públicos ajenos al equipo de ingeniería.

### 5.6 Ejemplo resuelto: un registro de decisión del TMRP (sintético)

> **ADR-007 — Autenticar la telemetría de campo en la capa de aplicación.** *Fecha:* 2026-03-04. *Estado:* aceptada. *Contexto:* el tráfico RTU–SCADA atraviesa una red LTE privada operada por un tercero; el cifrado LTE termina en el operador. *Opciones:* (a) confiar en el cifrado del operador; (b) túneles IPsec por RTU; (c) HMAC en la capa de aplicación con contadores. *Decisión:* (c), con (b) donde las RTU lo admitan. *Consecuencias:* +22 bytes por mensaje (Lab 8); se requiere gestión de claves (capítulo 19); las RTU heredadas de PS1 y PS2 necesitan una pasarela. *Revisar si:* cambia el contrato con el operador o el firmware de las RTU incorpora protocolos seguros nativos.

### 5.7 Actividad práctica

Reescriba en forma verificable tres requisitos vagos de un encargo sintético («el sistema deberá ser resiliente», «las alarmas deberán ser oportunas», «los registros deberán estar protegidos»), cada uno con un método de verificación. Para cada reescritura, nombre la evidencia que mostraría que el requisito se cumple: una prueba con un criterio de aprobación, un análisis con supuestos enunciados, una inspección o una demostración. Use el contexto de LRWA cuando ayude. Un sistema resiliente podría convertirse en una autonomía enunciada durante un corte de la red eléctrica, las alarmas oportunas en una meta de latencia para una proporción enunciada de eventos, y los registros protegidos en una protección de integridad con anclas guardadas fuera de la zona de control, como exige más adelante R8. Mantenga cada enunciado en un solo requisito.

### 5.8 Errores comunes y límites

- Enterrar la recomendación; escribir una cronología en lugar de un argumento.
- Requisitos que contienen «y/o», «según corresponda», «fácil de usar», «seguro».
- Números sin unidades, método ni incertidumbre.
- Historias distintas para públicos distintos.
- Compartir en exceso detalles sensibles, o compartir tan poco que los revisores no pueden comprobar el trabajo.

La mayoría de estos errores aparece primero en los conjuntos de requisitos. Un requisito que contiene «seguro» no puede probarse, así que o se abandona discretamente o se da por cumplido sin evidencia. Las historias distintas para públicos distintos son igual de dañinas: si la nota al operador, el resumen al directivo y la declaración al regulador del EX010 discrepan sobre la batería de PS4, quien lea dos de ellas no confiará en ninguna.

### Ejercicios — capítulo 5

**EX009 — Hágalo verificable.** *Objetivo:* escribir requisitos que puedan probarse. *Entradas:* los tres requisitos vagos de §5.7. *Pasos:* reescriba cada uno como uno o más enunciados con «deberá», con un identificador y un método de verificación (prueba, análisis, inspección, demostración). *Evidencia esperada:* tabla. *Rúbrica:* 3 = cada uno medible, único y factible, con un método adecuado; 2 = uno sigue siendo vago; 1 = solo cambio de redacción; 0 = nada.

**EX010 — Tres públicos.** *Objetivo:* comunicar un hallazgo de forma coherente. *Entradas:* «La batería de telemetría de PS4 dura 6 h al fin de vida; el requisito R5 es de 24 h». *Pasos:* escriba una nota de dos frases para el operador, un resumen de 100 palabras con opciones para el directivo y una declaración de brecha dirigida al regulador. *Evidencia esperada:* tres textos. *Rúbrica:* 3 = hechos coherentes, acciones adecuadas a cada público, sin exceso de detalles sensibles; 2 = una incoherencia; 1 = el mismo texto tres veces; 0 = nada.

### Síntesis del capítulo

Escriba para permitir decisiones: primero la recomendación, después la evidencia y los supuestos y, al final, las condiciones de cambio. Haga que cada requisito sea verificable y trazable; informe los números con unidades, métodos e incertidumbre; adapte el mensaje, no los hechos, al lector; y trate los detalles de la infraestructura como información sensible con un público definido.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 50

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Capítulo 6 — Cálculo II

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) escribir una ecuación diferencial ordinaria (EDO) de primer orden para una existencia con caudal de entrada y de salida; (2) resolver analíticamente EDO lineales de primer orden, incluida la aproximación exponencial al equilibrio y su constante de tiempo; (3) resolver EDO numéricamente y controlar el error debido al tamaño del paso; y (4) usar series y sensibilidad (derivadas parciales) para ver qué parámetro importa más para un margen de resiliencia. Amplía el capítulo 1 y prepara el capítulo 17 (control).

### 6.1 Las existencias con realimentación se convierten en ecuaciones diferenciales

El depósito del capítulo 1 tenía un caudal de salida conocido y ningún caudal de entrada. Las existencias reales tienen flujos que dependen de la propia existencia. El agua que sale de un tanque abierto por un orificio depende de la carga hidráulica sobre él; el cloro residual decae a una tasa proporcional a su concentración; la tensión en bornes de una batería cae con su estado de carga. Cuando la tasa depende de la cantidad, se obtiene una ecuación como $dx/dt = f(x, t)$. El caso importante más simple es lineal: $dx/dt = -kx + u$, con una constante $k > 0$ y una entrada $u$.

### 6.2 La solución lineal de primer orden y la constante de tiempo

Con $u$ constante, la solución es $x(t) = x_\infty + (x_0 - x_\infty)e^{-kt}$, donde $x_\infty = u/k$ es el equilibrio. La **constante de tiempo** $\tau = 1/k$ es el tiempo necesario para cerrar alrededor del 63 % de la brecha; tras $3\tau$ se cierra alrededor del 95 %, tras $5\tau$ alrededor del 99 %. Los ingenieros usan $\tau$ para razonar sobre la rapidez con que un sistema responde a un cambio, y sobre la rapidez con que responde a un ataque. Ejemplo: el cloro libre de un tanque de almacenamiento decae con una constante de primer orden; si $k = 0.05$ por hora, $\tau = 20$ h. Si la dosificación se detiene (por una avería o por una orden maliciosa), el residual se reduce a la mitad en $\ln 2/k \approx 13.9$ h. Esa es la ventana en la que un operador debe darse cuenta y actuar antes de que el residual caiga por debajo del mínimo reglamentario.

### 6.3 Solución numérica y error

En la práctica, la mayoría de las EDO son no lineales o están impulsadas por entradas medidas, así que se resuelven numéricamente. El método de Euler explícito, $x_{n+1} = x_n + h f(x_n, t_n)$, tiene un error global proporcional al paso $h$; reducir $h$ a la mitad reduce el error aproximadamente a la mitad. El método de Heun y el método clásico de Runge–Kutta de cuarto orden reducen el error mucho más rápido para el mismo $h$. Haga siempre una **comprobación de convergencia con el tamaño del paso**: si reducir $h$ a la mitad cambia la respuesta que le interesa más que su tolerancia, el paso es demasiado grande. En los sistemas rígidos (con algunos componentes mucho más rápidos que otros), los métodos explícitos pueden volverse inestables salvo que $h$ sea muy pequeño; Euler sobre $dx/dt = -kx$ es inestable para $h > 2/k$.

### 6.4 Sensibilidad: ¿qué supuesto importa?

Un margen de diseño depende de varios parámetros: nivel inicial, demanda, tasa de fugas, capacidad de bombeo. La derivada parcial del margen respecto de cada parámetro, multiplicada por el rango plausible de ese parámetro, muestra qué incertidumbre domina. Para la autonomía $T = V/q$ con demanda constante, $\partial T/\partial V = 1/q$ y $\partial T/\partial q = -V/q^2$; un error del 10 % en la demanda mueve $T$ aproximadamente lo mismo que un error del 10 % en el volumen utilizable, pero en sentido contrario. Las series de Taylor dan la misma intuición en los modelos no lineales: cerca de un punto nominal, $f(x + \Delta) \approx f(x) + f'(x)\Delta$.

### 6.5 Ejemplo resuelto: pérdida de la dosificación de cloro (sintético)

El residual a la salida de Hollin Hill de LRWA se mantiene en 0,8 mg/L; el mínimo de operación sintético es de 0,2 mg/L. Con la dosificación detenida y un decaimiento de primer orden $k = 0.05$ h⁻¹, el residual llega a 0,2 mg/L cuando $0.8e^{-0.05t} = 0.2$, es decir, $t = \ln 4 / 0.05 \approx 27.7$ h. Si el calor eleva $k$ a 0,08 h⁻¹, la ventana se reduce a 17,3 h. El equipo de diseño redacta el requisito R9: *la pérdida de la dosificación deberá generar una alarma en menos de 15 minutos, con independencia de los informes de estado del propio controlador de dosificación*, porque un controlador comprometido podría informar de una operación normal. La EDO se convirtió en un requisito de tiempo de detección con margen.

### 6.6 Actividad práctica

Modifique el Lab 1 para incluir un caudal de entrada constante de 120 m³/h procedente de una única bomba superviviente y una fuga de primer orden de $0.01V$ m³/h. Integre con Euler con tres tamaños de paso y halle analíticamente el nivel de equilibrio haciendo $dV/dt = 0$ con la demanda sustituida por su media. Informe el nivel de equilibrio y compárelo con la capacidad y el piso del depósito. Con una bomba a 120 metros cúbicos por hora frente a una demanda media de 150, la existencia debe seguir bajando salvo que la fuga compense la diferencia, así que compruebe si su respuesta analítica es físicamente posible antes de confiar en ella. Después confirme que las ejecuciones de Euler convergen a medida que el paso se reduce. El sentido del ejercicio es la combinación: una comprobación analítica, un resultado numérico y una prueba de convergencia que coincidan entre sí.

### 6.7 Errores comunes y límites

- Usar un decaimiento exponencial cuando el proceso no es de primer orden.
- Informar una solución numérica sin comprobación del tamaño del paso.
- Ignorar que los parámetros (tasas de decaimiento, demanda) derivan con la temperatura y la estación.
- Analizar la sensibilidad de un parámetro cada vez cuando los parámetros interactúan; para interacciones fuertes, use métodos globales ([Saltelli et al., 2008](https://doi.org/10.1002/9780470725184)).

En el ejemplo del cloro, un equipo que usara todo el año la constante de decaimiento del tiempo fresco creería tener 27,7 horas cuando el verano deja unas 17. La alarma de 15 minutos de R9 se eligió teniendo en cuenta ese rango estacional, y por eso el requisito no depende de la constante exacta.

### Ejercicios — capítulo 6

**EX011 — De la constante de tiempo al requisito.** *Objetivo:* convertir la dinámica en un requisito de tiempo de detección. *Entradas:* §6.5. *Pasos:* (1) calcule la ventana con $k = 0.12$ h⁻¹; (2) si los operadores necesitan 4 h para restablecer la dosificación manualmente, calcule el último momento aceptable para la alarma; (3) redacte el requisito. *Evidencia esperada:* números y requisito. *Rúbrica:* 3 = ventana y margen correctos y un requisito verificable independiente del controlador; 2 = un desliz; 1 = solo números; 0 = nada.

**EX012 — Estabilidad de Euler.** *Objetivo:* ver la inestabilidad numérica. *Entradas:* $dx/dt = -kx$, $k = 0.5$, $x_0 = 1$. *Pasos:* calcule cinco pasos de Euler con $h = 1$, $h = 3$ y $h = 5$ y compárelos con la solución exacta. *Evidencia esperada:* tabla y explicación. *Rúbrica:* 3 = valores correctos y explicación de la inestabilidad para $h > 2/k$; 2 = valores correctos, explicación débil; 1 = un solo tamaño de paso; 0 = nada.

### Síntesis del capítulo

Cuando un flujo depende de la existencia, escriba una EDO. Los sistemas lineales de primer orden se aproximan al equilibrio de forma exponencial con una constante de tiempo $\tau$; ese número se convierte en un requisito de detección y respuesta. Resuelva numéricamente con comprobaciones de convergencia y atención a la estabilidad. Use la sensibilidad para averiguar qué supuesto domina un margen, y diseñe una detección que no dependa del componente bajo sospecha.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 50

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Capítulo 7 — Probabilidad y estadística

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) aplicar la regla de Bayes a las alarmas y explicar el problema de la tasa base; (2) calcular la disponibilidad de caminos redundantes con y sin falla de causa común; (3) modelar eventos raros con la distribución de Poisson; y (4) resumir datos con una incertidumbre honesta, incluido cuándo desconfiar de una muestra pequeña. Se apoya en los capítulos 1–6 y prepara los capítulos 23 (análisis de fallas), 29 (medición) y 32 (confiabilidad).

### 7.1 La probabilidad como modelo de la incertidumbre

Una probabilidad es un número entre 0 y 1 asociado a un evento bajo un modelo. Los ingenieros usan tres lecturas: frecuencia a largo plazo (fallas de bombas por año en una flota), grado de creencia (la estimación de un experto sobre la capacidad de un adversario) y margen de diseño (una meta como una disponibilidad del 99,9 %). Sea explícito sobre cuál quiere decir; mezclarlas es la forma en que los registros de riesgos se vuelven ficción. Las reglas básicas: $P(A \cup B) = P(A) + P(B) - P(A\cap B)$; $P(A \cap B) = P(A)P(B\mid A)$; la independencia significa $P(B\mid A) = P(B)$.

### 7.2 La regla de Bayes y el problema de la tasa base

$P(H\mid E) = P(E\mid H)P(H)/P(E)$. Aplíquela a una alarma de intrusión: suponga que los ataques ocurren en el 0,1 % de las ventanas horarias, que el detector se activa en el 95 % de los ataques (tasa de verdaderos positivos) y en el 1 % de las ventanas benignas (tasa de falsos positivos). La probabilidad de que una alarma signifique un ataque es solo de alrededor del 8,7 %. La mayoría de las alarmas son falsas incluso con un detector «99 % preciso», porque las ventanas benignas superan con mucho a los ataques. Por eso los operadores aprenden a ignorar las alarmas, y por eso el diseño de alarmas debe informar la tasa de alarmas esperada y el **valor predictivo positivo**, no solo la exactitud. [Sommer y Paxson (2010)](https://doi.org/10.1109/SP.2010.25) analizan este y otros obstáculos relacionados para la detección de anomalías en redes operativas.

### 7.3 Redundancia y causa común

Si un camino de comunicaciones está disponible con probabilidad $a$ y los caminos fallan de forma independiente, $n$ caminos dan $1-(1-a)^n$. La independencia es el supuesto que falla en la práctica: los caminos que comparten un alimentador eléctrico, un proveedor, una configuración o una vulnerabilidad explotable fallan juntos. El **modelo del factor beta** asigna una fracción $\beta$ de la indisponibilidad de cada unidad a causas comunes que inutilizan todas las unidades a la vez. Con $a = 0.98$ y $\beta = 0.05$, dos caminos tienen una indisponibilidad ≈ 0,00136 en lugar de 0,0004: la causa común domina. En seguridad, una vulnerabilidad de software idéntica en ambos caminos es una causa común con $\beta$ cercano a 1 frente a un adversario que la conoce.

### 7.4 Eventos raros: el modelo de Poisson

Si los eventos llegan de forma independiente a una tasa media $\lambda$ por año, su número en un año sigue una distribución de Poisson: $P(N=k) = e^{-\lambda}\lambda^k/k!$. Con $\lambda = 0.5$ cortes largos de la red eléctrica por año, $P(N \ge 1) \approx 0.39$. Poisson supone una tasa constante e independencia; las tormentas, las campañas de ataques y el envejecimiento violan ambas cosas, así que trátelo como una primera aproximación. Para LRWA, un corte largo de la red eléctrica de más de cuatro horas es el evento que pone a prueba a la vez R5 y la reserva del hospital. Si los cortes se agrupan en tormentas, la cifra de Poisson subestima la probabilidad de dos cortes en pocos días, así que el equipo del TMRP la contrasta con los registros de cortes de la distribuidora antes de usarla en el árbol de fallas.

### 7.5 Describir los datos con honestidad

Informe un valor central con su dispersión (mediana y rango intercuartílico para datos asimétricos, como la duración de los cortes), el tamaño de la muestra y cómo se recogieron los datos. Un intervalo de confianza describe la incertidumbre de muestreo bajo un modelo; no dice nada del sesgo en lo que se registró. Las muestras pequeñas de eventos raros son especialmente traicioneras: cero fallas en 3 años de operación no significa riesgo cero. La «regla del tres» da una cota superior aproximada al 95 % de $3/n$ para una tasa cuando se observan 0 eventos en $n$ ensayos o unidades de tiempo.

### 7.6 Ejemplo resuelto: ¿debe LRWA avisar al ingeniero de guardia? (sintético)

El TMRP propone un detector de anomalías de red en el centro de control con las tasas de §7.2. Evaluado sobre ventanas horarias, avisaría unas 0,26 veces al día (aproximadamente una vez cada cuatro días) y alrededor del 91 % de los avisos serían falsos. El equipo decide: avisar solo cuando la alarma de red coincida con una anomalía del proceso (cambio de consigna inesperado o desequilibrio de caudales) y enviar las alarmas de red aisladas a una cola de revisión para el siguiente día hábil. La decisión se justifica por la tasa base, y su costo (una respuesta más lenta ante un ataque sigiloso que solo afecte a la red) queda anotado en el registro de riesgos.

### 7.7 Actividad práctica: Lab 4

```python
# Lab 4 - base rates, redundancy and rare events (synthetic numbers, offline)
import math
prior, tpr, fpr = 0.001, 0.95, 0.01
ppv = tpr * prior / (tpr * prior + fpr * (1 - prior))
print(f"P(attack | alarm) = {ppv:.3f}")
alarms_per_day = 24 * (tpr * prior + fpr * (1 - prior))
print(f"expected alarms per day (hourly windows) = {alarms_per_day:.3f}")
a = 0.98
for n in (1, 2, 3): print(f"{n} independent paths at {a}: availability {1 - (1 - a) ** n:.6f}")
beta = 0.05   # beta-factor common-cause share of unavailability
q = 1 - a
print(f"2 paths with beta={beta}: unavailability {(1 - beta) ** 2 * q ** 2 + beta * q:.6f}")
lam = 0.5
print(f"P(>=1 grid outage >4 h per year | lambda={lam}) = {1 - math.exp(-lam):.3f}")
print(f"P(>=2) = {1 - math.exp(-lam) * (1 + lam):.4f}")
```

Salida esperada:

```text
P(attack | alarm) = 0.087
expected alarms per day (hourly windows) = 0.263
1 independent paths at 0.98: availability 0.980000
2 independent paths at 0.98: availability 0.999600
3 independent paths at 0.98: availability 0.999992
2 paths with beta=0.05: unavailability 0.001361
P(>=1 grid outage >4 h per year | lambda=0.5) = 0.393
P(>=2) = 0.0902
```

Las dos primeras líneas repiten el resultado de la tasa base del ejemplo resuelto: menos de una alarma de cada diez sería un ataque real, y el detector avisaría aproximadamente una vez cada cuatro días. Las líneas de redundancia muestran con qué rapidez los caminos independientes mejoran la disponibilidad, y la línea del factor beta muestra cómo una causa común del cinco por ciento anula la mayor parte de esa ganancia. Las líneas de Poisson dan la probabilidad de al menos uno, y de al menos dos, cortes largos de la red eléctrica en un año con la tasa supuesta por LRWA.

### 7.8 Errores comunes y límites

- Informar la exactitud del detector sin la tasa base ni el valor predictivo.
- Multiplicar disponibilidades como si fueran independientes cuando los caminos comparten causas.
- Usar Poisson para eventos agrupados.
- Tratar cero fallas observadas como probabilidad cero.
- Estimaciones puntuales sin tamaño de muestra ni método de recogida.

Cada error tiene un ejemplo en LRWA. Avisar al ingeniero de guardia ante cada alarma de red ignora la tasa base. Tratar los dos caminos LTE como independientes ignora su alimentador compartido. Usar Poisson para los cortes por tormentas oculta la agrupación, y tres años tranquilos en PS4 no prueban que las bombas no puedan fallar juntas.

### Ejercicios — capítulo 7

**EX013 — Sensibilidad a la tasa base.** *Objetivo:* ver cómo el valor predictivo depende de la prevalencia. *Entradas:* Lab 4. *Pasos:* calcule el VPP para probabilidades previas de 0,0001, 0,001 y 0,01 con el mismo detector, y para la previa de 0,001 con una TFP de 0,001. *Evidencia esperada:* cuatro valores y una recomendación sobre qué parámetro mejorar. *Rúbrica:* 3 = valores correctos y la idea de que reducir la TFP es lo que más importa con prevalencia baja; 2 = valores correctos; 1 = un valor; 0 = nada.

**EX014 — Causa común en la telemetría.** *Objetivo:* cuantificar la diversidad. *Entradas:* dos caminos LTE de operadores distintos ($a = 0.98$ cada uno). *Pasos:* calcule la indisponibilidad para $\beta$ = 0, 0,05 y 0,2; nombre dos causas comunes reales que estos caminos podrían seguir compartiendo. *Evidencia esperada:* tres números y dos causas. *Rúbrica:* 3 = números correctos y causas compartidas plausibles (energía del sitio, torre o red de retorno compartidas, mismo firmware del módem); 2 = causas genéricas; 1 = un número; 0 = nada.

### Síntesis del capítulo

La probabilidad es un modelo; diga de qué tipo. La regla de Bayes hace que las tasas base sean decisivas para las alarmas; la redundancia solo funciona en la medida en que las fallas son independientes, y las causas comunes, incluidas las vulnerabilidades compartidas, suelen dominar. Poisson es un punto de partida para los eventos raros. Describa los datos con su dispersión, el tamaño de la muestra y el método de recogida, y nunca trate la ausencia de fallas observadas como prueba de seguridad.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 50

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Capítulo 8 — Arquitectura de computadoras

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) describir cómo interactúan el procesador, la jerarquía de memoria y la E/S, y por qué esto importa para el control en tiempo real; (2) explicar la arquitectura de los controladores lógicos programables (PLC), las RTU y los controladores embebidos; (3) relacionar las características del hardware (niveles de privilegio, protección de memoria, arranque seguro, raíces de confianza en hardware) con las garantías de seguridad; y (4) explicar cómo las optimizaciones de desempeño, como las cachés y la especulación, crean vulnerabilidades. Se apoya en el capítulo 3 y prepara el capítulo 12 (sistemas operativos).

### 8.1 El modelo de máquina

Un procesador busca instrucciones en la memoria, las decodifica y las ejecuta, y lee y escribe datos en registros y en memoria. La memoria es una jerarquía (registros, cachés, memoria principal, almacenamiento), en la que cada nivel es más grande y más lento. Los dispositivos de E/S se conectan mediante buses e interrupciones; una interrupción suspende la ejecución normal para que el procesador atienda a un dispositivo. El **determinismo**, es decir, conocer el tiempo de peor caso de una operación, importa más en control que la velocidad media: una rutina de protección de bombas que suele tardar 1 ms pero en ocasiones tarda 50 ms por una avalancha de fallos de caché o por la recolección de basura puede incumplir su plazo.

### 8.2 PLC, RTU y controladores embebidos

Un PLC ejecuta un **ciclo de barrido**: leer las entradas, ejecutar el programa del usuario, escribir las salidas, realizar las comunicaciones y los diagnósticos, y repetir, a menudo cada 10–100 ms. Su programa se escribe en lenguajes normalizados en IEC 61131-3 (lógica de escalera, diagramas de bloques de funciones, texto estructurado). Una RTU está diseñada para sitios remotos: recoge mediciones, aplica una lógica sencilla y se comunica por enlaces de larga distancia, tolerando una conectividad intermitente. Ambos tienen una vida larga: un equipo instalado hoy puede funcionar entre quince y veinticinco años, de modo que las características de seguridad que elija ahora deben seguir siendo aceptables en la década de 2040. Muchos controladores heredados aceptan cambios de programa de cualquiera que pueda alcanzarlos por la red; Stuxnet explotó el camino desde una estación de ingeniería hasta la lógica del PLC, según el análisis de [Langner (2011)](https://doi.org/10.1109/MSP.2011.67).

### 8.3 Soporte del hardware para la seguridad

- Los **niveles de privilegio** separan el código del núcleo del código de usuario; una falla en el código de usuario no puede sobrescribir directamente el núcleo.
- Las **unidades de protección de memoria** (MPU) y las **unidades de gestión de memoria** (MMU) imponen qué código puede acceder a qué memoria; la MPU es común en microcontroladores que carecen de una MMU completa.
- El marcado de **no ejecución** impide que se ejecuten las regiones de datos.
- El **arranque seguro** verifica una firma criptográfica en cada etapa del firmware antes de ejecutarla, anclada en una raíz de confianza inmutable (código en ROM o claves grabadas en fusibles). Protege contra la modificación persistente del firmware, no contra una imagen correctamente firmada pero vulnerable.
- Los **módulos de plataforma confiable** y los elementos seguros almacenan las claves de modo que el software no pueda extraerlas.

### 8.4 Cuando la velocidad crea filtraciones

Las cachés y la ejecución especulativa hacen rápidos a los procesadores porque adivinan y conservan estado, y ese estado puede filtrarse. [Kocher et al. (2019)](https://doi.org/10.1109/SP.2019.00002) mostraron que la ejecución especulativa puede dirigirse para leer memoria a través de fronteras de protección (Spectre). [Kim et al. (2014)](https://doi.org/10.1109/ISCA.2014.6853210) mostraron que el acceso repetido a la DRAM puede invertir bits en filas adyacentes (Rowhammer). Estos problemas importan sobre todo donde el código no confiable comparte hardware con el código confiable (servidores virtualizados del centro de control, nube compartida) y menos en un PLC de propósito único. La lección de ingeniería: el hardware forma parte de la superficie de ataque, y el aislamiento que depende de hardware compartido debe justificarse.

### 8.5 Ejemplo resuelto: elección de una plataforma de RTU (sintético)

El TMRP compara dos RTU candidatas. *RTU-A:* madura, determinista, sin arranque seguro, actualizaciones de firmware sin firmar, cambios de programa autenticados solo con una contraseña compartida. *RTU-B:* arranque seguro con firmware firmado por el proveedor, autenticación basada en roles para los cambios de programa, almacenamiento de claves en hardware, pero una respuesta de peor caso a las peticiones de comunicación 200 ms más lenta y un producto nuevo con un historial de campo limitado. El equipo puntúa ambas frente a los requisitos: R1 (telemetría autenticada) necesita almacenamiento de claves, lo que favorece a B; R7 (alarma en menos de 60 s) la cumplen ambas, porque 200 ms es despreciable; la mantenibilidad durante 20 años favorece a un proveedor con un ciclo de vida de desarrollo seguro publicado. El registro de decisión selecciona B para los sitios nuevos y una pasarela para los sitios heredados con RTU-A, con un piloto para recoger datos de confiabilidad en campo antes del despliegue en toda la flota.

### 8.6 Actividad práctica

Para una familia de microcontroladores o de PLC de su elección, lea el manual público de seguridad del proveedor (o una hoja de datos) y complete una tabla: separación de privilegios, protección de memoria, arranque seguro, actualizaciones firmadas, almacenamiento de claves, programación autenticada. Marque cada una como «sí / no / configurable / desconocido» con la cita de su fuente. Use solo documentos públicos. Anote el título, la versión y la fecha del documento de cada entrada, porque las características de seguridad cambian entre versiones de firmware. Donde el manual no diga nada, marque la característica como desconocida en lugar de adivinar, y anote la pregunta que haría al proveedor. La tabla es la misma comparación que el equipo del TMRP hizo entre RTU-A y RTU-B, y muestra rápidamente si un producto puede admitir telemetría autenticada y almacenamiento de claves sin una pasarela.

### 8.7 Errores comunes y límites

- Equiparar «rápido» con «determinista».
- Suponer que el arranque seguro impide la explotación de un firmware firmado.
- Ignorar la vida útil de 20 años al elegir las características criptográficas y de actualización.
- Tratar como absoluto el aislamiento por hardware en servidores compartidos.
- Tratar el marketing del proveedor como evidencia; pida documentación y pruebe.

La comparación de RTU muestra estos errores en la práctica. RTU-A es determinista pero no puede proteger claves, así que la velocidad por sí sola no la hace adecuada. El arranque seguro de RTU-B no detiene un cambio de lógica malicioso pero firmado legítimamente, y por eso el acceso de programación basado en roles figura junto a él. Ambas deben poder seguir recibiendo soporte en la década de 2040, y el piloto existe porque las afirmaciones del proveedor no son evidencia de campo.

### Ejercicios — capítulo 8

**EX015 — Presupuesto del ciclo de barrido.** *Objetivo:* razonar sobre el determinismo. *Entradas:* ciclo de barrido de un PLC de 20 ms nominales y 45 ms en el peor caso; un requisito de protección de bomba que exige disparar en menos de 100 ms desde una señal de aspiración baja, filtrada contra rebotes durante dos barridos consecutivos. *Pasos:* calcule la latencia de disparo en el peor caso (muestreo de la entrada justo después de una lectura, dos barridos para confirmar, escritura de la salida). *Evidencia esperada:* cálculo y conclusión. *Rúbrica:* 3 = peor caso correcto, incluido el retardo de muestreo, y juicio frente a los 100 ms; 2 = se omite el retardo de muestreo; 1 = solo el barrido nominal; 0 = nada.

**EX016 — Lo que aporta el arranque seguro.** *Objetivo:* delimitar con precisión un control. *Entradas:* RTU-B de §8.5. *Pasos:* enumere dos ataques que el arranque seguro impide, dos que no impide y el control complementario para cada uno de estos últimos. *Evidencia esperada:* tabla. *Rúbrica:* 3 = alcance exacto (impide el firmware persistente sin firmar; no impide las explotaciones en tiempo de ejecución ni los cambios de lógica maliciosos mediante la programación legítima), controles adecuados; 2 = un error; 1 = genérico; 0 = nada.

### Síntesis del capítulo

La arquitectura determina tanto la temporización como la confianza. El control necesita el desempeño del peor caso, no el medio. Los PLC y las RTU son máquinas longevas basadas en ciclos de barrido cuyas características de seguridad deben seguir siendo adecuadas dentro de décadas. Los mecanismos de hardware (privilegio, protección de memoria, arranque seguro, almacenamiento de claves) dan garantías específicas y limitadas; las características de desempeño pueden filtrar información a través de las fronteras. Indique exactamente contra qué protege cada mecanismo.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 50

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Capítulo 9 — Programación II

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) estructurar un programa en módulos con interfaces e invariantes claros; (2) implementar máquinas de estados sencillas para la lógica de protocolos y de equipos; (3) escribir pruebas unitarias, incluidas pruebas de límites y de fallas, y medir lo que cubren; y (4) tratar de forma deliberada los errores, el tiempo y la concurrencia. Se apoya en el capítulo 4 y prepara el capítulo 14 (ingeniería de software) y el capítulo 30 (verificación).

### 9.1 Módulos, interfaces e invariantes

[Parnas (1972)](https://doi.org/10.1145/361598.361623) sostuvo que un sistema debe descomponerse de modo que cada módulo oculte una decisión de diseño que probablemente cambie. En el software de infraestructura, los cambios probables incluyen el protocolo de campo, el historiador de datos y el esquema de autenticación. Oculte cada uno detrás de una interfaz: un `TelemetrySource` que entrega lecturas validadas, sea cual sea el protocolo. Cada módulo debe enunciar sus **invariantes**, propiedades que siempre son ciertas sobre su estado; por ejemplo, «el último contador aceptado de cada estación nunca disminuye». Escriba los invariantes como aserciones en las pruebas y, cuando sea barato, como comprobaciones en tiempo de ejecución que fallen de forma segura.

### 9.2 Máquinas de estados

Los equipos y los protocolos tienen modos: una bomba está *detenida*, *arrancando*, *en marcha*, *deteniéndose* o *disparada*; una sesión está *sin autenticar*, *autenticada* o *cerrada*. Una máquina de estados finitos enumera los estados, los eventos que provocan transiciones, las guardas de las transiciones y las acciones. Escríbala como una tabla e impleméntela a partir de la tabla, rechazando cualquier evento que no figure para el estado actual. Las transiciones no enumeradas son donde viven tanto los errores como los ataques: una orden «stop» que llega mientras la bomba está *arrancando*, o un «escribir consigna» que llega antes de la autenticación.

El controlador de bombas de LRWA del ejemplo resuelto que sigue está construido exactamente así, de modo que sus pruebas pueden enumerar cada par.

### 9.3 Pruebas

Una prueba unitaria comprueba un comportamiento de una unidad. Los buenos conjuntos de pruebas incluyen: casos típicos; **límites** (mínimo, máximo, justo dentro, justo fuera); entradas no válidas; y pruebas de **regresión** que reproducen errores pasados. La cobertura mide qué sentencias o ramas ejecutaron las pruebas; le dice lo que *no* se probó, no que el código probado sea correcto. El módulo `unittest` de Python, incluido en la biblioteca estándar, basta para este libro. Para el controlador de bombas de LRWA, las pruebas de límites incluyen el tiempo de espera de arranque de 30 segundos exactamente a los 30 segundos y justo después, y las pruebas de regresión reproducen cada error de transición encontrado en la puesta en marcha, de modo que una falla corregida no pueda volver discretamente en una versión posterior.

### 9.4 Errores, tiempo y concurrencia

Decida cómo se trata cada error: rechazado con un motivo, reintentado con un límite o escalado. Nunca silencie excepciones en el código de control o de seguridad. El tiempo es una fuente recurrente de fallas: use relojes monótonos para los intervalos y la hora de reloj sincronizada (con su fuente registrada) para los registros; trate los saltos de reloj. La concurrencia (hilos, tareas asíncronas, varios clientes) crea condiciones de carrera: dos operadores que envían consignas contradictorias, o una comprobación y una acción separadas por una ventana en la que el estado cambia (*time-of-check to time-of-use*). Prefiera un único propietario para cada elemento de estado, con mensajes para cambiarlo.

### 9.5 Ejemplo resuelto: una máquina de estados para una bomba (sintético)

El controlador de bombas de LRWA acepta `start`, `stop`, `trip` y `reset`. La tabla: *detenida* + `start` (guarda: permiso verdadero) → *arrancando*; *arrancando* + `run_confirmed` → *en marcha*; *arrancando* + tiempo de espera de 30 s → *disparada*; *en marcha* + `stop` → *deteniéndose*; cualquier estado + `trip` → *disparada*; *disparada* + `reset` (guarda: operador local) → *detenida*. La guarda de `reset` importa: exigir una acción local tras un disparo significa que un atacante remoto que provoca un disparo no puede volver a arrancar de inmediato la bomba en la misma falla. Las pruebas cubren cada transición enumerada y verifican que todo par no enumerado (por ejemplo, *disparada* + `start`) se rechaza y se registra.

### 9.6 Actividad práctica

Implemente la tabla de §9.5 en unas 40 líneas de Python con un diccionario indexado por `(state, event)`. Escriba casos `unittest` para todas las transiciones enumeradas y un bucle que verifique que cada par `(state, event)` no enumerado genera un error. Cuente los pares no enumerados. Su bucle debe imprimir el número de pares no enumerados y confirmar que cada uno genera un error y escribe una línea de registro. Después añada una prueba que muestre que se rechaza un reinicio remoto tras un disparo, porque la guarda exige un operador local. Esa prueba protege la propiedad que más importa en el ejemplo resuelto: un atacante que dispara una bomba de forma remota no puede volver a arrancarla directamente en la misma falla. Mantenga la tabla y las pruebas en un solo archivo para que un revisor pueda compararlas.

### 9.7 Errores comunes y límites

- Implementar la lógica de estados con indicadores dispersos en lugar de una tabla explícita.
- Ramas por defecto que aceptan eventos desconocidos.
- Usar la hora de reloj para los tiempos de espera.
- Pruebas que solo recorren el camino feliz; equiparar cobertura con corrección.
- Tratamiento silencioso de las excepciones.

Cada error anula una propiedad de la máquina de estados de la bomba. Los indicadores dispersos hacen imposible enumerar todas las transiciones. Una rama por defecto dejaría pasar una orden de arranque mientras la bomba está disparada. Un tiempo de espera basado en la hora de reloj podría saltar antes de tiempo o no saltar nunca tras un salto de reloj, y una excepción silenciada en el camino de reinicio dejaría la bomba en un modo desconocido.

### Ejercicios — capítulo 9

**EX017 — Cuente y pruebe las transiciones no enumeradas.** *Objetivo:* razonar sobre la completitud. *Entradas:* §9.5 (estados: stopped, starting, running, stopping, tripped; eventos: start, stop, trip, reset, run_confirmed, timeout, stop_confirmed; añada *stopping* + `stop_confirmed` → *stopped*). *Pasos:* cuente los pares totales, los enumerados y los no enumerados; dé tres pares no enumerados cuyo rechazo tenga una justificación de seguridad funcional o de seguridad. *Evidencia esperada:* recuentos y justificación. *Rúbrica:* 3 = recuentos correctos y justificaciones con sentido; 2 = error de recuento; 1 = sin justificación; 0 = nada.

**EX018 — Invariante contra repeticiones.** *Objetivo:* expresar y probar un invariante. *Entradas:* el `Receiver` del Lab 8. *Pasos:* escriba el invariante sobre `last`, una prueba unitaria que envíe los contadores 1, 2, 2, 1, 5 y verifique los resultados de aceptación o rechazo y el estado final, e indique un modo de falla del invariante tras reiniciar el receptor. *Evidencia esperada:* código de la prueba y enunciado. *Rúbrica:* 3 = resultados esperados correctos (aceptar, aceptar, rechazar, rechazar, aceptar), problema del reinicio identificado (estado perdido → se aceptan repeticiones salvo que se persista o se roten las claves); 2 = se omite el reinicio; 1 = sin probar; 0 = nada.

### Síntesis del capítulo

Descomponga en torno a las decisiones que probablemente cambien y enuncie invariantes. Haga explícitos los modos como máquinas de estados y rechace todo lo que no esté enumerado. Pruebe los límites y las fallas, lea la cobertura como un mapa de lo no probado, trate los errores de forma deliberada, use el reloj adecuado y dé a cada elemento de estado compartido un único propietario.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Siga estudiando — capítulo 09 de 50

[← Capítulo 08](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Capítulo 10 — Ética y seguridad en ingeniería

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) aplicar los códigos de ética profesional a las decisiones de seguridad en infraestructura; (2) explicar la relación entre seguridad funcional y seguridad, y dónde entran en conflicto; (3) reconocer los límites legales y de autorización de las pruebas y la investigación; y (4) tomar y documentar una decisión ética en condiciones de incertidumbre, incluido cuándo escalar. Se apoya en el capítulo 5 y enmarca todos los capítulos posteriores, en particular los de pruebas (capítulos 30 y 40) y práctica (capítulo 43).

### 10.1 Los deberes de un ingeniero

Los códigos profesionales convergen en una jerarquía: anteponer a todo la seguridad, la salud y el bienestar del público; actuar dentro de la propia competencia; ser honesto y objetivo; evitar los conflictos de intereses; proteger la información confidencial. El [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics) hace de la seguridad pública el primer canon fundamental; el [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) pide a los profesionales de la computación que eviten el daño y que sean honestos sobre las capacidades y los límites de los sistemas. En la infraestructura crítica, el público es concreto: pacientes en diálisis, hogares sin agua, personas que esperan una ambulancia. El deber no se cumple siguiendo instrucciones si el resultado es un daño previsible al público.

### 10.2 Seguridad funcional y seguridad, juntas

La **seguridad funcional** (*safety*) protege a las personas y al ambiente del daño causado por el sistema; la **seguridad** (*security*) protege al sistema del uso indebido deliberado. En la tecnología operativa ambas interactúan. Un control de seguridad puede crear un peligro para la seguridad funcional: un bloqueo automático de cuenta en la consola de un operador durante una emergencia, o un parche que reinicia un controlador durante un proceso en curso. Un mecanismo de seguridad funcional puede ser un objetivo de ataque: el malware TRITON/TRISIS atacó controladores de sistemas instrumentados de seguridad, como describe el [informe de análisis del malware HatMan](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf) de CISA. La buena práctica trata ambas en un único análisis de peligros (capítulo 33) y da a las funciones de seguridad funcional independencia respecto de las redes y los sistemas que protegen.

### 10.3 Autorización y derecho

Probar un sistema que no le pertenece o que no tiene permiso escrito para probar puede ser un delito, sean cuales sean sus intenciones, y en la infraestructura puede poner en peligro a las personas. La autorización debe ser escrita, específica (sistemas, horarios, métodos), otorgada por alguien facultado para darla, e incluir condiciones de detención. La investigación con personas o con datos operativos necesita revisión ética y acuerdos sobre los datos. Las vulnerabilidades que encuentre de forma incidental deben comunicarse al propietario del activo en privado o mediante un programa de divulgación coordinada, como el [programa CVD de CISA](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program). Los laboratorios de este libro son sintéticos precisamente por estas razones.

### 10.4 Decidir en condiciones de incertidumbre

Un procedimiento práctico de decisión ética: (1) enuncie la decisión y a quién afecta; (2) identifique los deberes y los hechos que inciden en ellos; (3) enumere las opciones, incluidas la escalada y la negativa; (4) evalúe las consecuencias para las partes interesadas más vulnerables; (5) elija, documente el razonamiento y los desacuerdos, y fije un punto de revisión. Los ingenieros rara vez enfrentan dilemas limpios; con más frecuencia, el problema es la presión para aprobar algo que aún no se ha demostrado que funcione. «No verificado» es una respuesta honesta y suficiente.

En el ejemplo resuelto que sigue, el ingeniero de verificación del TMRP usa exactamente estos cinco pasos.

### 10.5 Ejemplo resuelto: la aprobación con plazo (sintético)

El plazo de puesta en marcha del TMRP es el viernes. La prueba T3 (límites de consigna) ha fallado: el controlador de PS4 acepta una consigna fuera del rango seguro cuando se envía como valor NaN. El proveedor propone poner en marcha con una nota para corregirlo en la próxima versión. Como ingeniero de verificación, usted aplica el procedimiento: entre las personas afectadas están los pacientes del hospital si PS4 se comporta de forma impredecible; su deber es con la seguridad pública y con un informe honesto; las opciones son (a) firmar, (b) negarse, (c) poner en marcha con un control compensatorio (escrituras remotas de consigna deshabilitadas en la pasarela, operación solo local para PS4) y una corrección con fecha. Usted recomienda (c), registra T3 como fallida, no como dispensada, y exige repetir la prueba antes de habilitar las escrituras remotas. La decisión queda documentada y la firma el gerente de operaciones, responsable del riesgo operativo.

### 10.6 Actividad práctica

Escriba una plantilla de autorización de una página para una prueba de un sistema sintético: alcance, métodos excluidos, ventana temporal, condiciones de detención, contactos, tratamiento de los datos y firma. Complete la plantilla para una prueba de banco de la pasarela de telemetría de LRWA y no para una estación en servicio. Indique quién puede firmarla, enumere los métodos excluidos, como cualquier tráfico dirigido a RTU reales, y dé condiciones de detención que un probador pueda reconocer sin interpretación. Incluya un contacto que pueda detener la prueba en cualquier momento y una regla sobre qué ocurre después con los datos capturados. Una plantilla que permitiera a alguien probar PS4 en un periodo de alta demanda ha fracasado en su propósito.

### 10.7 Errores comunes y límites

- Tratar la ética como una lista de cumplimiento en lugar de razonar sobre el daño.
- El «permiso verbal» para realizar pruebas.
- Controles de seguridad diseñados sin considerar la seguridad funcional en emergencias.
- Aprobar lo que no se ha verificado porque lo exige un calendario.
- Divulgar públicamente debilidades de la infraestructura sin coordinación.

La aprobación con plazo del ejemplo resuelto muestra varios de estos errores a la vez: presión para poner en marcha, un proveedor que ofrece una promesa verbal de corregir más tarde y una prueba fallida que fácilmente podría haberse marcado como dispensada. El ingeniero evitó cada uno registrando la falla y acordando por escrito un control compensatorio.

### Ejercicios — capítulo 10

**EX019 — Conflicto entre seguridad funcional y seguridad.** *Objetivo:* resolver un control que pone en peligro la operación. *Entradas:* propuesta de bloquear las cuentas de la HMI de los operadores tras cinco inicios de sesión fallidos. *Pasos:* analice el peligro, proponga una alternativa que preserve la intención de seguridad e indique cómo la verificaría. *Evidencia esperada:* análisis de media página. *Rúbrica:* 3 = peligro claro (bloqueo durante una emergencia), la alternativa mantiene la rendición de cuentas y resiste los intentos de adivinar (p. ej., limitación de frecuencia con alertas, anulación con presencia física, cuentas por turno con registro), verificación indicada; 2 = alternativa débil; 1 = solo el peligro; 0 = nada.

**EX020 — Hallazgo incidental.** *Objetivo:* actuar dentro de la autorización. *Entradas:* mientras estudia para un trabajo del curso los documentos de compra de una empresa pública de servicios, observa en una captura de pantalla una página de gestión de un controlador de bombas expuesta a internet, con el proveedor y el modelo visibles. *Pasos:* indique qué no debe hacer, qué debe hacer y ante quién, y qué puede decir su trabajo del curso. *Evidencia esperada:* 150 palabras. *Rúbrica:* 3 = ningún acceso ni sondeo, notificación privada al propietario o mediante CVD, trabajo anonimizado; 2 = falta un paso; 1 = sugiere «comprobar si es real»; 0 = nada.

### Síntesis del capítulo

La seguridad pública va primero, comunicada con honestidad. La seguridad funcional y la seguridad deben analizarse juntas, porque cada una puede anular a la otra. Pruebe solo con autorización escrita y específica; comunique en privado los hallazgos incidentales. Decida en condiciones de incertidumbre con un procedimiento documentado, y trate «no verificado» como una respuesta que usted puede, y debe, dar.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Siga estudiando — capítulo 10 de 50

[← Capítulo 09](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Capítulo 11 — Redes y protocolos

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) explicar el modelo de capas y las funciones de Ethernet, IP, TCP, UDP y los protocolos de aplicación; (2) describir los protocolos industriales (Modbus/TCP, DNP3, IEC 60870-5-104, OPC UA) y qué propiedades de seguridad ofrece o no ofrece cada uno; (3) construir un presupuesto de latencia para la telemetría; y (4) expresar la segmentación como zonas y conductos y contrastar con ella los flujos observados. Se apoya en los capítulos 3 y 4 y prepara los capítulos 18 (arquitectura de seguridad) y 26 (alternativas de arquitectura).

### 11.1 Las capas y lo que prometen

Las redes se construyen en capas: física y de enlace (tramas Ethernet en un segmento), de red (paquetes IP encaminados entre segmentos), de transporte (TCP, flujos de bytes fiables y ordenados; UDP, datagramas sin garantía de entrega; TCP se especifica en [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293)) y de aplicación (el protocolo que transporta el significado). Cada capa promete algo limitado. TCP garantiza el orden y la retransmisión, no la autenticidad. IP encamina, pero en muchas redes las direcciones de origen pueden falsificarse. Las propiedades de seguridad deben añadirse de forma deliberada, normalmente con TLS ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)), IPsec o autenticación en la capa de aplicación.

### 11.2 Protocolos industriales

Los protocolos industriales clásicos se diseñaron para redes serie cerradas. **Modbus/TCP** (puerto 502) transporta códigos de función, como leer y escribir registros, sin ninguna autenticación; cualquiera que pueda alcanzar el puerto 502 puede emitir escrituras. **DNP3** se usa ampliamente en agua y electricidad; su extensión Secure Authentication añade autenticación por desafío y respuesta de las órdenes críticas, pero no está desplegada de forma universal. **IEC 60870-5-104** es común en los sistemas eléctricos europeos, con extensiones de seguridad definidas en IEC 62351. **OPC UA** se diseñó con modos de seguridad que ofrecen firma y cifrado, pero deben configurarse: «None» es una política válida. La lección es constante: la capacidad del protocolo no es su despliegue. Compruebe lo que está configurado.

### 11.3 Latencia, fluctuación y sondeo

La telemetría suele obtenerse por sondeo: el maestro SCADA pregunta a cada RTU por turno. La latencia de extremo a extremo, desde un evento físico hasta la pantalla de un operador, es la suma de la actualización del sensor, el barrido de la RTU, el viaje de ida y vuelta por el enlace, la espera de sondeo del maestro, el procesamiento y el refresco de la pantalla. La **fluctuación** (*jitter*) es la variación de la latencia. Escriba un presupuesto, mida cada elemento y compare el total con el requisito; el capítulo 36 añade las colas.

El presupuesto de LRWA en el Lab 5 suma el barrido de la RTU, el viaje de ida y vuelta por LTE, la espera de sondeo y el refresco de pantalla hasta llegar a un segundo frente a un requisito de 1,5 segundos, pero la espera de sondeo es el elemento que más varía, y el EX022 muestra cómo domina el peor caso.

### 11.4 Zonas, conductos y listas de permitidos

La segmentación divide una red en **zonas** con requisitos de seguridad similares y controla los **conductos** entre ellas. Este vocabulario procede de la [serie ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards). Una política de conducto es una **lista de permitidos**: zona de origen, zona de destino, protocolo y puerto concretos, y todo lo demás denegado. Verificar no es leer la configuración del cortafuegos; es contrastar los flujos observados con la política prevista, porque las configuraciones derivan y los caminos no documentados (el módem de acceso remoto de un proveedor, un portátil conectado a dos redes) eluden los cortafuegos.

La revisión de flujos de LRWA que sigue muestra por qué.

### 11.5 Ejemplo resuelto: revisión de flujos de LRWA (sintético)

LRWA define estas zonas: *enterprise* (corporativa), *dmz*, *control* (servidores SCADA), *field* (campo, las RTU) y *eng* (estaciones de ingeniería). Los conductos previstos se enumeran en el Lab 5. Una semana de registros de flujos muestra tres infracciones: un equipo corporativo que habla Modbus directamente con una RTU de campo (un script de informes olvidado que elude la DMZ), una estación de ingeniería que abre SSH directamente hacia una RTU en lugar de pasar por el servidor de salto de la zona de control, y un servidor SCADA que hace consultas DNS a un resolutor público. Cada una es un hallazgo con un responsable: eliminar el script y servir sus datos desde el historiador de la DMZ; encaminar el acceso de ingeniería a través del servidor de salto; apuntar el DNS del SCADA a un resolutor interno o a ninguno.

### 11.6 Actividad práctica: Lab 5

```python
# Lab 5 - check observed flows against a zone-conduit allowlist (synthetic, offline)
RULES = [  # (src_zone, dst_zone, protocol, port)
    ("control", "field", "tcp", 502), ("control", "dmz", "tcp", 443), ("dmz", "enterprise", "tcp", 443),
    ("eng", "control", "tcp", 22), ("field", "control", "udp", 20000)]
ZONE = {"10.1.0.": "control", "10.2.0.": "field", "10.3.0.": "dmz", "10.4.0.": "enterprise", "10.5.0.": "eng"}
def zone(ip): return next((z for p, z in ZONE.items() if ip.startswith(p)), "unknown")
FLOWS = [("10.1.0.5", "10.2.0.31", "tcp", 502), ("10.4.0.77", "10.2.0.31", "tcp", 502),
         ("10.2.0.31", "10.1.0.5", "udp", 20000), ("10.3.0.9", "10.4.0.20", "tcp", 443),
         ("10.5.0.12", "10.2.0.33", "tcp", 22), ("10.1.0.5", "8.8.8.8", "udp", 53),
         ("10.1.0.6", "10.3.0.9", "tcp", 443)]
for s, d, p, port in FLOWS:
    ok = (zone(s), zone(d), p, port) in RULES
    print(f"{s:>10} {zone(s):>10} -> {d:<10} {zone(d):<10} {p}/{port:<5} {'allowed' if ok else 'VIOLATION'}")
budget = {"rtu_scan": 120, "lte_rtt": 180, "scada_poll_wait": 500, "operator_view": 200}
print("end-to-end latency budget ms:", sum(budget.values()), "vs requirement 1500")
```

Salida esperada:

```text
  10.1.0.5    control -> 10.2.0.31  field      tcp/502   allowed
 10.4.0.77 enterprise -> 10.2.0.31  field      tcp/502   VIOLATION
 10.2.0.31      field -> 10.1.0.5   control    udp/20000 allowed
  10.3.0.9        dmz -> 10.4.0.20  enterprise tcp/443   allowed
 10.5.0.12        eng -> 10.2.0.33  field      tcp/22    VIOLATION
  10.1.0.5    control -> 8.8.8.8    unknown    udp/53    VIOLATION
  10.1.0.6    control -> 10.3.0.9   dmz        tcp/443   allowed
end-to-end latency budget ms: 1000 vs requirement 1500
```

Tres de los siete flujos son infracciones, y cada una coincide con un hallazgo del ejemplo resuelto: el script corporativo de informes que habla Modbus con una RTU de campo, la estación de ingeniería que abre SSH directamente hacia una RTU en lugar de hacerlo a través del servidor de salto, y un servidor SCADA que consulta un resolutor DNS público. La línea del presupuesto de latencia muestra un total de un segundo frente al requisito de 1,5 segundos, pero esa cifra usa valores típicos, así que trátela como punto de partida para el análisis del peor caso del EX022 y no como evidencia de que R7 se cumple.

### 11.7 Errores comunes y límites

- Equiparar el cifrado en una capa con la protección de extremo a extremo.
- Suponer que la seguridad opcional de un protocolo industrial está habilitada.
- Verificar la segmentación solo leyendo configuraciones.
- Presupuestos de latencia con promedios en lugar de peores casos.
- Listas de permitidos por equipo en lugar de por función, que se vuelven imposibles de mantener.

La revisión de flujos de LRWA ilustra directamente el tercer error: la configuración del cortafuegos parecía correcta y, sin embargo, una semana de registros de flujos mostró tres infracciones. Leer las configuraciones no habría encontrado ninguna. Las listas de permitidos escritas por equipo también habrían necesitado modificaciones constantes a medida que se añadían RTU.

### Ejercicios — capítulo 11

**EX021 — Amplíe la comprobación de la política.** *Objetivo:* encontrar infracciones por función. *Entradas:* Lab 5. *Pasos:* (1) añada un flujo de `10.2.0.31` a `10.4.0.77` por TCP/445; (2) añada una regla para que la estación de ingeniería pueda llegar a las RTU solo a través de un servidor de salto en la zona de control, y modele los dos saltos; (3) vuelva a ejecutar e informe. *Evidencia esperada:* cambios en el código y salida. *Rúbrica:* 3 = se detecta la nueva infracción, el modelo de dos saltos es correcto, ninguna regla debilita la protección del campo; 2 = un problema; 1 = no ejecutado; 0 = nada.

**EX022 — Latencia frente al requisito.** *Objetivo:* presupuestar la latencia del peor caso. *Entradas:* barrido de la RTU de 120 ms, viaje de ida y vuelta LTE de 180 ms típico / 900 ms en el percentil 99, espera de sondeo de hasta un ciclo completo de 1,3 s (Lab 13), refresco de la vista del operador de 200 ms; requisito: el 95 % de las alarmas en pantalla en menos de 1,5 s y todas en menos de 5 s. *Pasos:* calcule los totales típico y de peor caso; juzgue ambas cláusulas; proponga un cambio de diseño. *Evidencia esperada:* tabla. *Rúbrica:* 3 = sumas correctas, se reconoce que la espera de sondeo domina, se propone un cambio (informe por excepción o alarmas no solicitadas); 2 = una suma errónea; 1 = solo el caso típico; 0 = nada.

### Síntesis del capítulo

Cada capa de red promete algo acotado; la autenticidad hay que añadirla. Los protocolos industriales varían en capacidad de seguridad, y la capacidad no es la configuración. Presupueste la latencia con peores casos. Exprese la segmentación como zonas y conductos con listas de permitidos, y verifíquela con los flujos observados y no con las configuraciones previstas.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Siga estudiando — capítulo 11 de 50

[← Capítulo 10](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Capítulo 12 — Sistemas operativos

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) explicar los procesos, los hilos, la planificación, la gestión de memoria y los sistemas de archivos; (2) distinguir los sistemas operativos de propósito general de los de tiempo real y elegir entre ellos; (3) aplicar los mecanismos de seguridad del sistema operativo (cuentas, permisos, aislamiento, registro, parches) a los servidores del centro de control y a las estaciones de ingeniería; y (4) planificar los parches y el endurecimiento bajo las restricciones de disponibilidad de la tecnología operativa. Se apoya en el capítulo 8 y prepara los capítulos 18 y 39.

### 12.1 Qué hace un sistema operativo

Un sistema operativo reparte el hardware entre los programas y ofrece abstracciones: **procesos** (espacios de direcciones aislados), **hilos** (ejecución concurrente dentro de un proceso), **memoria virtual**, **archivos** y **dispositivos**. El núcleo se ejecuta con privilegios; las aplicaciones solicitan servicios mediante llamadas al sistema. El planificador decide qué hilo se ejecuta; su política determina la latencia. En LRWA, los servidores SCADA y las estaciones de ingeniería ejecutan sistemas operativos de propósito general, mientras que la lógica de protección de las bombas se ejecuta en las RTU y los PLC de cada estación. Saber qué código se ejecuta dónde le indica qué máquinas necesitan garantías de tiempo real y cuáles necesitan endurecimiento, parches y registro del tipo que se describe a continuación.

### 12.2 Sistemas operativos de tiempo real

Un sistema operativo de **tiempo real** garantiza una respuesta acotada: las tareas con plazos se planifican de modo que, si el análisis dice que caben, cumplen sus plazos. La planificación por prioridades fijas con asignación de prioridades monótona en la tasa (*rate-monotonic*) es un enfoque clásico; el análisis de Liu y Layland da una cota de utilización suficiente para tareas periódicas bajo esa política. Los sistemas operativos de propósito general (Windows, Linux de escritorio) optimizan el rendimiento y la equidad; su latencia de peor caso no está acotada sin una configuración especial. Regla: las funciones de protección se ejecutan en controladores de tiempo real; las funciones de supervisión (HMI, historiador) pueden ejecutarse en sistemas de propósito general.

### 12.3 Mecanismos de seguridad del sistema operativo

- **Mínimo privilegio:** los servicios se ejecutan con cuentas dedicadas que tienen solo los derechos necesarios; no hay cuentas de administrador compartidas. [Saltzer y Schroeder (1975)](https://doi.org/10.1109/PROC.1975.9939) formularon el mínimo privilegio, los valores predeterminados a prueba de fallos, la mediación completa y la economía de mecanismo como principios de diseño que siguen vigentes.
- **Control de acceso:** permisos sobre archivos y objetos; control de acceso obligatorio donde esté disponible.
- **Lista de aplicaciones permitidas:** solo se ejecutan los ejecutables aprobados; es práctico en equipos de TO de propósito único cuyo software rara vez cambia.
- **Registro:** autenticación, uso de privilegios, cambios de servicios y creación de procesos, reenviados fuera del equipo.
- **Endurecimiento:** eliminar los servicios no usados, cerrar los puertos no usados, deshabilitar la ejecución automática de medios extraíbles.
- **Parches:** aplicar las actualizaciones de seguridad, probadas y programadas.

### 12.4 Parches bajo restricciones de disponibilidad

Los sistemas de TO a menudo no pueden reiniciarse a voluntad, y los proveedores pueden dar soporte solo a niveles de parche concretos. Por tanto, la aplicación de parches se basa en el riesgo: evalúe la explotabilidad de cada vulnerabilidad en su arquitectura (¿es alcanzable el servicio vulnerable?), su consecuencia y el riesgo para la disponibilidad de aplicarlo; después, aplique el parche, mitigue (bloquee el puerto, deshabilite la función) o acepte con una fecha de revisión. Mantenga un sistema de pruebas que refleje la producción para validar los parches. La [guía de TO del NIST (SP 800-82 Rev. 3)](https://csrc.nist.gov/pubs/sp/800/82/r3/final) analiza estas compensaciones.

### 12.5 Ejemplo resuelto: endurecimiento de los servidores SCADA (sintético)

Los dos servidores SCADA de LRWA ejecutan un sistema operativo de propósito general. La línea base del TMRP: cuentas de servicio dedicadas; los operadores inician sesión con cuentas nominativas; administrador local deshabilitado salvo una cuenta de emergencia (*break-glass*) cuya contraseña está sellada y cuyo uso genera una alarma; lista de aplicaciones permitidas habilitada tras un periodo de aprendizaje de dos semanas en un entorno de pruebas; almacenamiento USB bloqueado; registros reenviados al recolector de la DMZ; una ventana mensual de parches que alterna entre servidores para que uno esté siempre en funcionamiento. El riesgo residual (el proveedor certifica los parches 30 días después de su publicación) se mitiga con reglas de red que exponen al campo y a la DMZ solo los puertos de la aplicación SCADA.

### 12.6 Actividad práctica

En una máquina virtual Linux que le pertenezca, enumere los servicios a la escucha (`ss -tulpn`), las cuentas locales con intérprete de inicio de sesión y los servicios habilitados. Escriba una nota de endurecimiento: qué servicios deshabilitaría en un equipo de historiador de propósito único y por qué. No ejecute esto contra ningún sistema que no le pertenezca. Registre la salida con la fecha y el nombre de la máquina y, para cada servicio que deshabilitaría, anote qué se rompería si usted se equivocara. Un equipo de historiador de LRWA necesitaría su servicio de base de datos y el reenvío de registros, pero rara vez un servidor de correo o un servicio para compartir archivos. Compare su lista con las medidas de endurecimiento del ejemplo de SCADA y explique cualquier diferencia. El ejercicio entrena el hábito de preguntar por qué se ejecuta cada servicio antes de decidir si debería ejecutarse.

### 12.7 Errores comunes y límites

- Ejecutar la lógica de protección en un sistema operativo de propósito general.
- Cuentas compartidas que destruyen la rendición de cuentas.
- Aplicar parches por calendario sin evaluar la explotabilidad, o no aplicarlos nunca porque «la TO es especial».
- Registros guardados solo en el equipo que controla el atacante.
- Lista de aplicaciones permitidas activada en producción sin un periodo de aprendizaje.

El endurecimiento del SCADA de LRWA evita cada uno de estos errores: las cuentas nominativas sustituyen a las compartidas, los registros salen del equipo, la lista de permitidos se activó tras dos semanas de aprendizaje en un entorno de pruebas y la ventana mensual de parches alterna entre los dos servidores. El riesgo residual queda registrado.

### Ejercicios — capítulo 12

**EX023 — Comprobación monótona en la tasa.** *Objetivo:* probar la planificabilidad con la cota de Liu–Layland. *Entradas:* tres tareas periódicas en una RTU: (C=2 ms, T=10 ms), (C=4 ms, T=40 ms), (C=10 ms, T=100 ms). *Pasos:* calcule la utilización; calcule la cota $n(2^{1/n}-1)$ para $n = 3$; concluya. *Evidencia esperada:* números y conclusión. *Rúbrica:* 3 = U = 0,40, cota ≈ 0,780, planificable según la prueba suficiente, con la salvedad de que superar la cota no probaría que no es planificable; 2 = falta la salvedad; 1 = error aritmético; 0 = nada.

**EX024 — Decisión sobre un parche.** *Objetivo:* tomar una decisión de parcheo basada en el riesgo. *Entradas:* una vulnerabilidad de ejecución remota de código en el servicio para compartir archivos del sistema operativo; el servicio está habilitado en el historiador, pero el cortafuegos de la zona de control lo bloquea desde todas las zonas salvo la de ingeniería; faltan 30 días para que el proveedor certifique el parche. *Pasos:* recomiende parchear / mitigar / aceptar, con controles provisionales y una fecha de revisión. *Evidencia esperada:* nota de decisión. *Rúbrica:* 3 = mitigación inmediata (deshabilitar el servicio o restringirlo más), parche tras la certificación, monitoreo, fecha; 2 = sin control provisional; 1 = «parchear de inmediato» ignorando el soporte del proveedor, o «aceptar» sin razonamiento; 0 = nada.

### Síntesis del capítulo

El sistema operativo determina tanto la temporización como la línea base de seguridad. Ponga los plazos en plataformas de tiempo real. Aplique el mínimo privilegio, las listas de aplicaciones permitidas, el endurecimiento y el registro fuera del equipo. Aplique los parches según el riesgo evaluado, con procedimientos probados y controles compensatorios cuando aún no pueda parchear, y mantenga un entorno espejo que lo haga posible.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Siga estudiando — capítulo 12 de 50

[← Capítulo 11](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Capítulo 13 — Sistemas de datos

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) diseñar modelos de datos relacionales y de series temporales para los datos operativos; (2) explicar las transacciones, la consistencia y la replicación; (3) proteger la integridad de los datos con restricciones, procedencia y cadenas de hashes, e indicar exactamente qué detecta cada una; y (4) planificar los flujos de datos entre los sistemas de control y la analítica corporativa sin abrir un camino hacia el control. Se apoya en los capítulos 9 y 11 y prepara los capítulos 22 (modelos de datos) y 29 (medición).

### 13.1 Modelos para los datos operativos

[Codd (1970)](https://doi.org/10.1145/362384.362685) introdujo el modelo relacional: los datos como relaciones (tablas) con claves, manipuladas mediante operaciones de conjuntos. Los registros de activos, las órdenes de trabajo y las cuentas de usuario encajan bien en él. Los datos de proceso (miles de etiquetas muestreadas cada segundo) suelen ir a un **historiador**, un almacén de series temporales optimizado para añadir datos y para consultas por rangos, a menudo con una compresión que descarta los cambios menores que una banda muerta. Sepa qué descarta su historiador: el análisis forense puede necesitar valores que nunca almacenó.

El historiador de LRWA almacena el nivel de Hollin Hill con compresión por banda muerta, así que los cambios menores que la banda muerta nunca se conservan.

### 13.2 Transacciones, consistencia y replicación

Una **transacción** agrupa operaciones de modo que todas ocurran o ninguna (atomicidad), dejando los datos válidos (consistencia), sin verse afectada por transacciones concurrentes (aislamiento) y sobreviviendo a las caídas (durabilidad). La replicación copia los datos para la disponibilidad; cuando las réplicas pueden discrepar, los sistemas eligen entre consistencia y disponibilidad durante una partición de la red. Para la operación: una alarma reconocida por un operador no debe reaparecer como no reconocida tras una conmutación por falla; un cambio de consigna no debe aplicarse dos veces.

En el par SCADA de LRWA, la conmutación por falla es el momento en que se ponen a prueba estas propiedades: las pruebas de integración deben confirmar que las alarmas reconocidas y las consignas aplicadas sobreviven al cambio exactamente una vez.

### 13.3 Integridad: qué detecta cada mecanismo

- Las **restricciones** (tipos, rangos, claves foráneas) rechazan los valores imposibles en la entrada.
- Los campos de **procedencia** (fuente, hora de recogida, transformación) permiten rastrear un número hasta su origen.
- Las **sumas de verificación** detectan la corrupción accidental.
- Las **cadenas de hashes** enlazan cada registro con el anterior, de modo que editar cualquier registro cambia todos los hashes posteriores. Detectan la modificación *si* se dispone de una copia de confianza de un hash posterior (un **ancla**) guardada en un lugar que el atacante no pueda alterar. No detectan el truncamiento del final salvo que el ancla incluya el número de registros, y no prueban que los datos originales fueran verdaderos.
- Las **firmas digitales** o los MAC sobre los registros o las anclas los vinculan a quien posee una clave.

### 13.4 Sacar los datos sin dejar entrar los ataques

Los equipos corporativos quieren datos de control para informes y analítica. El patrón seguro es empujar los datos hacia fuera, desde la zona de control hasta una réplica del historiador en la DMZ, y dejar que los usuarios corporativos consulten la réplica, nunca el historiador de control. Donde la consecuencia de comprometer la zona de control es grave, las pasarelas unidireccionales (diodos de datos) imponen físicamente un flujo solo de salida. La infracción del Lab 5 (un script corporativo que sondea directamente una RTU) es el antipatrón.

En LRWA, la réplica del historiador en la DMZ atiende a los equipos de finanzas y de activos, y el script corporativo olvidado que encontró la revisión de flujos se está retirando en su favor.

### 13.5 Ejemplo resuelto: proteger la cronología del incidente (sintético)

Tras una caída inexplicada del nivel del depósito el 4 de marzo en el registro sintético, LRWA debe preservar el extracto del historiador para la investigación. El Lab 6 encadena con hashes seis lecturas diarias y guarda el hash de cabeza en el ticket del incidente (el ancla). La edición del valor del 4 de marzo se detecta en el índice 3 y en todos los registros posteriores. La eliminación del último registro no se detecta comparando solo las cabezas si el atacante también sustituye la cabeza guardada; por eso el ancla va a un sistema fuera del alcance del atacante, junto con el número de registros.

### 13.6 Actividad práctica: Lab 6

```python
# Lab 6 - a hash-chained historian extract detects edits, not deletions at the tail (offline)
import hashlib, json
recs = [{"t": f"2026-03-0{d} 06:00", "tag": "HOLLIN_LVL", "v": v} for d, v in zip(range(1, 7), [78.1, 77.4, 79.0, 41.2, 76.5, 77.9])]
def chain(rs):
    prev, out = "0" * 64, []
    for r in rs:
        h = hashlib.sha256((prev + json.dumps(r, sort_keys=True)).encode()).hexdigest()
        out.append(h); prev = h
    return out
anchor = chain(recs)
print("head:", anchor[-1][:16])
tampered = [dict(r) for r in recs]; tampered[3]["v"] = 74.0
bad = [i for i, (a, b) in enumerate(zip(anchor, chain(tampered))) if a != b]
print("first mismatch at index:", bad[0], "mismatches:", len(bad))
print("truncated head matches stored index 4:", chain(recs[:5])[-1] == anchor[4])
```

Salida esperada:

```text
head: a8407870e41914c1
first mismatch at index: 3 mismatches: 3
truncated head matches stored index 4: True
```

El hash de cabeza es lo que LRWA guarda en el ticket del incidente. Editar la lectura del 4 de marzo para ocultar la caída cambia el hash en el índice tres y en todos los registros posteriores, de modo que la edición se detecta dondequiera que ocurra. La última línea muestra la debilidad: una cadena construida con los cinco primeros registros coincide con el hash guardado en el índice cuatro, así que un atacante que elimine el registro final y sustituya la cabeza guardada pasaría desapercibido. El EX025 cierra esa brecha añadiendo el número de registros al ancla.

### 13.7 Errores comunes y límites

- Tratar los datos del historiador como completos cuando la compresión o las bandas muertas descartan detalle.
- Cadenas de hashes sin un ancla guardada de forma independiente.
- Creer que los mecanismos de integridad prueban la verdad; prueban la ausencia de modificación desde el anclaje.
- Conexiones de «informes» bidireccionales hacia la zona de control.
- Perder la información de zona horaria y de la fuente del reloj.

La investigación del 4 de marzo depende de evitar cada uno de estos errores, desde los huecos de compresión hasta la falta de zona horaria. Un historiador que descarta los cambios pequeños puede haber eliminado justo los valores que mostrarían con qué rapidez bajó el nivel; un ancla guardada en el servidor del historiador podría reescribirla el mismo administrador; y unas marcas de tiempo sin zona hacen imposible alinear la caída con el registro del operador.

### Ejercicios — capítulo 13

**EX025 — Truncamiento del final.** *Objetivo:* cerrar la brecha del truncamiento. *Entradas:* Lab 6. *Pasos:* (1) muestre que `chain(recs[:5])` coincide con el hash guardado en el índice 4; (2) modifique el ancla para incluir el número de registros y muestre que el truncamiento se detecta; (3) indique dónde debe guardarse el ancla en LRWA y por qué. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = demostración y corrección correctas, ancla guardada fuera del alcance de los administradores del control y del historiador; 2 = corrección incompleta; 1 = no ejecutado; 0 = nada.

**EX026 — Diseño del flujo de datos.** *Objetivo:* diseñar con seguridad el acceso para la analítica. *Entradas:* el equipo de finanzas quiere datos horarios de energía de las bombas; el equipo de activos quiere datos de presión en vivo para un tablero. *Pasos:* describa (en texto) los flujos, las zonas y la dirección; indique qué componente impone la dirección y qué ocurre si se compromete la réplica de la DMZ. *Evidencia esperada:* descripción de los flujos y análisis de consecuencias. *Rúbrica:* 3 = envío hacia la DMZ, nada entrante hacia el control, consecuencia limitada a la confidencialidad e integridad de los datos de la réplica; 2 = la dirección no se impone; 1 = consulta directa al historiador de control; 0 = nada.

### Síntesis del capítulo

Modele los datos operativos de forma deliberada, sepa qué descarta su historiador y use las transacciones y la replicación pensando en la conmutación por falla. Cada mecanismo de integridad detecta algo específico: las restricciones rechazan lo imposible, las cadenas de hashes detectan ediciones respecto de un ancla guardada de forma independiente, las firmas vinculan a quien posee una clave; ninguno prueba la verdad. Mueva los datos hacia fuera, a una DMZ, y nunca deje que los informes se conviertan en un camino hacia el control.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Siga estudiando — capítulo 13 de 50

[← Capítulo 12](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Capítulo 14 — Ingeniería de software

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) aplicar un ciclo de vida de desarrollo seguro al software de infraestructura; (2) gestionar requisitos, revisiones de diseño, revisiones de código e inspecciones; (3) gestionar las dependencias y la cadena de suministro de software con SBOM y procedencia; y (4) planificar versiones y actualizaciones para software embebido y de TO de larga vida. Se apoya en los capítulos 5 y 9 y prepara los capítulos 28, 31 y 39.

### 14.1 Por qué importa el proceso

[Brooks (1987)](https://doi.org/10.1109/MC.1987.1663532) sostuvo que las dificultades esenciales del software (complejidad, conformidad, mutabilidad, invisibilidad) no admiten un único avance decisivo. El proceso no las elimina; hace visibles los errores pronto, cuando corregirlos es barato, y deja evidencia de que el trabajo se hizo. En la infraestructura crítica, la evidencia forma parte del producto: los reguladores, las aseguradoras y los propietarios de los activos la pedirán. Para la pasarela del TMRP, esa evidencia incluye la revisión del modelo de amenazas, los resultados de las pruebas y la compilación firmada, que van todos al expediente.

### 14.2 Un ciclo de vida de desarrollo seguro

El [NIST Secure Software Development Framework (SP 800-218)](https://csrc.nist.gov/pubs/sp/800/218/final) agrupa las prácticas en preparar a la organización, proteger el software, producir software bien protegido y responder a las vulnerabilidades. En concreto: requisitos de seguridad y modelos de amenazas con cada funcionalidad; normas de codificación segura; revisión por pares; análisis estático automatizado y pruebas en la integración continua; sistemas de compilación protegidos; recepción y divulgación de vulnerabilidades; y parches con avisos claros. Los principios [Secure by Design de CISA](https://www.cisa.gov/securebydesign) añaden que los fabricantes deben asumir la responsabilidad de los resultados de seguridad de sus clientes: valores predeterminados seguros, sin contraseñas predeterminadas, lenguajes con seguridad de memoria cuando sea factible.

### 14.3 Revisiones e inspecciones

[Fagan (1976)](https://doi.org/10.1147/sj.153.0182) describió inspecciones formales de diseño y de código con roles y listas de comprobación definidos, e informó de que encontraban defectos antes y con menor costo que las pruebas. La revisión de código moderna es más ligera, pero conserva los principios: una segunda persona competente lee cada cambio, con una lista de comprobación que incluye la validación de entradas, la autenticación, el manejo de errores y el registro. Las métricas de complejidad, como la complejidad ciclomática de McCabe ([McCabe, 1976](https://doi.org/10.1109/TSE.1976.233837)), señalan las funciones difíciles de probar.

En LRWA, cada cambio en el código de la pasarela lo lee un segundo ingeniero con una lista de comprobación.

### 14.4 Dependencias y cadena de suministro

La mayor parte del software se ensambla a partir de componentes de terceros. Una **lista de materiales de software (SBOM)** los enumera para que, cuando se anuncie una vulnerabilidad, pueda saber si le afecta ([recursos sobre SBOM de CISA](https://www.cisa.gov/sbom)). La **procedencia**, evidencia verificable de cómo y a partir de qué se construyó un artefacto, protege contra compilaciones manipuladas; el [marco SLSA](https://slsa.dev/) define niveles de integridad de la compilación, y las [compilaciones reproducibles](https://reproducible-builds.org/) permiten a terceros independientes confirmar que un binario corresponde a su código fuente.

### 14.5 Versiones para sistemas de larga vida

El software de TO puede mantenerse durante veinte años. Planifique: actualizaciones firmadas; reversión; despliegue por etapas (banco de pruebas, un sitio, flota); ventanas de compatibilidad; fechas de fin de soporte publicadas con antelación; y un proceso de actualización que funcione cuando un sitio solo es alcanzable de forma intermitente. Un mecanismo de actualización es en sí mismo una superficie de ataque y debe estar autenticado. Para el TMRP, el plan es concreto: la pasarela pasa del banco a PS2 y luego a PS1, se conserva una imagen de reversión en cada etapa, y las actualizaciones deben llegar a estaciones que solo son alcanzables de forma intermitente por LTE. Como las pasarelas están registradas como deuda técnica con un horizonte de tres años, la fecha de fin de soporte se publica desde el principio.

### 14.6 Ejemplo resuelto: el proyecto de la pasarela de telemetría (sintético)

El TMRP debe construir una pequeña pasarela que añada autenticación HMAC para las RTU heredadas de PS1 y PS2. El plan: los requisitos R1, R2 y R7, trazados hasta las pruebas; un modelo de amenazas revisado por un segundo ingeniero; solo la biblioteca estándar de Python, evitando dependencias de terceros; análisis estático y pruebas unitarias en la integración continua; compilaciones en un ejecutor dedicado, con artefactos firmados y una SBOM (trivialmente corta en este caso); despliegue en un banco, luego en PS2 y luego en PS1; y una imagen de reversión conservada. Cada paso deja un registro en el expediente de evidencia (capítulo 48).

### 14.7 Actividad práctica

Escriba un plan de una página, mapeado al SSDF, para una pequeña herramienta que haya escrito: para cada uno de los cuatro grupos de prácticas, enumere dos prácticas concretas y la evidencia que produce cada una. Elija algo real que haya escrito, como su analizador del Lab 3, para que las prácticas sean concretas. Para cada práctica, nombre la evidencia que deja: un registro de revisión, un informe de pruebas, una compilación firmada o una plantilla de aviso. Si una práctica no dejara ninguna evidencia, cámbiela o admita que es solo una intención. Compare su plan con el plan de la pasarela del TMRP y anote una práctica que añadiría.

### 14.8 Errores comunes y límites

- Documentos de proceso sin las prácticas que describen.
- Revisión de código sin lista de comprobación o sin autoridad para bloquear.
- Dependencias descargadas en tiempo de compilación sin fijar versiones ni procedencia.
- Mecanismos de actualización sin autenticación ni reversión.
- Ninguna fecha de fin de soporte publicada.

El plan de la pasarela del TMRP se redactó para evitar cada uno de estos errores. Usa solo la biblioteca estándar, así que no hay dependencias sin fijar; las revisiones siguen una lista de comprobación; las compilaciones se firman con una SBOM; el despliegue conserva una imagen de reversión; y las pasarelas tienen un horizonte publicado de tres años.

### Ejercicios — capítulo 14

**EX027 — Lista de comprobación de revisión.** *Objetivo:* crear una lista de comprobación de revisión para el código de infraestructura. *Entradas:* el código del Lab 3 y del Lab 8. *Pasos:* escriba una lista de diez puntos y aplíquela a ambos laboratorios, registrando un hallazgo para cada uno. *Evidencia esperada:* lista y dos hallazgos. *Rúbrica:* 3 = lista específica (validación de entradas, comparación en tiempo constante, manejo de claves, caminos de error, registro, límites) y hallazgos reales; 2 = lista genérica; 1 = sin hallazgos; 0 = nada.

**EX028 — Simulacro de respuesta con SBOM.** *Objetivo:* usar una SBOM en la respuesta a una vulnerabilidad. *Entradas:* una SBOM sintética que enumera `libmodbus 3.1.6`, `openssl 3.0.8` y `zlib 1.2.13` para el firmware de RTU-B, y un aviso sobre uno de ellos. *Pasos:* describa los pasos de triaje desde el aviso hasta la decisión, incluido cómo determina la explotabilidad en su despliegue. *Evidencia esperada:* procedimiento. *Rúbrica:* 3 = coincidencia, análisis de alcanzabilidad, contacto con el proveedor, control compensatorio, comunicación; 2 = sin alcanzabilidad; 1 = «actualizar todo»; 0 = nada.

### Síntesis del capítulo

El proceso hace visibles los errores pronto y deja evidencia. Use un marco de desarrollo seguro reconocido, revise con listas de comprobación, mida la complejidad y trate las dependencias y las compilaciones como parte de su superficie de ataque, con SBOM y procedencia. Diseñe las versiones y las actualizaciones para décadas, con autenticación, despliegue por etapas y reversión.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Siga estudiando — capítulo 14 de 50

[← Capítulo 13](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Capítulo 15 — Fundamentos de seguridad

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) definir la confidencialidad, la integridad y la disponibilidad y explicar por qué su prioridad difiere en la infraestructura; (2) describir las amenazas, las vulnerabilidades, el riesgo y los controles, y relacionarlos en una evaluación de riesgos; (3) aplicar los principios de diseño de la literatura de seguridad; y (4) mapear los controles de un sistema a un marco reconocido. Integra los capítulos 1–14 y prepara los capítulos de arquitectura de seguridad e identidad (18–19) y los capítulos sectoriales (del 20 en adelante).

### 15.1 Las propiedades

La **confidencialidad** limita quién puede leer la información; la **integridad** garantiza que la información y los sistemas no se alteren sin autorización; la **disponibilidad** garantiza un acceso oportuno y fiable. En la TI corporativa, la confidencialidad suele ir primero. En la infraestructura, el proceso físico ocupa el primer lugar: la integridad y la disponibilidad del control, después la seguridad funcional y después la confidencialidad, aunque la confidencialidad de los diseños de red y de las credenciales protege a las demás. [Avizienis et al. (2004)](https://doi.org/10.1109/TDSC.2004.2) sitúan la seguridad junto a la confiabilidad, la seguridad funcional y la mantenibilidad como atributos de la confiabilidad en sentido amplio (*dependability*); su taxonomía de fallas, errores y averías se usa en todo este libro.

### 15.2 Amenaza, vulnerabilidad, riesgo

Una **amenaza** es una causa potencial de daño (un actor con capacidad e intención, o un peligro natural); una **vulnerabilidad** es una debilidad que una amenaza puede explotar; el **riesgo** combina la probabilidad y la consecuencia. [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) describe la evaluación de riesgos como la identificación de las fuentes y los eventos de amenaza, las vulnerabilidades, la probabilidad y el impacto. En la infraestructura, empiece por la consecuencia: ¿qué es lo peor que podría ocurrirles al servicio y a las personas? El método [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/) del Idaho National Laboratory empieza así: pregunta qué funciones serían inaceptables si se perdieran o se usaran indebidamente y trabaja hacia atrás hasta lo que necesitaría un adversario.

### 15.3 Controles y principios

Los controles son preventivos, detectivos, correctivos o compensatorios, y técnicos, procedimentales o físicos. Principios de diseño de [Saltzer y Schroeder (1975)](https://doi.org/10.1109/PROC.1975.9939): economía de mecanismo, valores predeterminados a prueba de fallos, mediación completa, diseño abierto, separación de privilegios, mínimo privilegio, mínimo mecanismo común y aceptabilidad psicológica. Añada la **defensa en profundidad** (capas cuyas fallas son independientes) y la **suposición de brecha** (diseñar de modo que el compromiso de una capa se detecte y se contenga). En el diseño del TMRP, el modo manual local con un interruptor de llave físico es un ejemplo de separación de privilegios, y el analizador de cloro independiente es una capa de detección fuera de los sistemas que vigila.

### 15.4 Marcos

Los marcos dan estructura y un vocabulario común. El [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) organiza los resultados en Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar. El catálogo [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) enumera controles; [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) especifica requisitos para los sistemas y componentes de automatización industrial, con niveles de seguridad; el [NCSC Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf) del Reino Unido está basado en resultados para los servicios esenciales. Un marco es una lista de comprobación de resultados, no la evidencia de que un diseño los alcanza.

### 15.5 Ejemplo resuelto: la primera tabla de riesgos del TMRP (sintético)

| Consecuencia | Evento de amenaza | Vulnerabilidad | Control existente | Control propuesto |
|---|---|---|---|---|
| El hospital pierde el suministro > 4 h | Órdenes de parada falsificadas a PS3/PS4 | Modbus sin autenticar sobre LTE | Cifrado del operador | Telemetría autenticada (R1/R2), modo manual local |
| Niveles de cloro inseguros | Consigna de dosificación manipulada | Sin límites de consigna en el controlador | Observación del operador | Límites en el controlador (R3), alarma de un analizador independiente (R9) |
| Pérdida de visibilidad | Caída de la telemetría durante la pérdida de la red eléctrica | Batería del gabinete de 6 h al fin de vida | Ninguno | Batería de 24 h (R5) |
| Recuperación lenta | *Ransomware* en los servidores SCADA | Copias de seguridad en línea, en el mismo dominio | Copias de seguridad nocturnas | Copias fuera de línea, restauración probada (R6) |

Cada fila nombra primero una consecuencia en términos del servicio. La tabla es una hipótesis que se refinará en los capítulos 23 y 27.

### 15.6 Actividad práctica

Mapee cada control propuesto de §15.5 a una función del CSF 2.0 y a una familia de controles de SP 800-53, citando los documentos. Para cada fila de la tabla de riesgos del TMRP, elija la función del CSF que mejor describa el propósito principal del control propuesto, y anote dónde un control sirve a dos. La telemetría autenticada es principalmente protectora, la alarma del analizador independiente es principalmente detectiva y las copias fuera de línea probadas apoyan la recuperación. Cite los documentos del marco con sus versiones. Después escriba una frase por fila explicando lo que el mapeo no le dice, porque un mapeo correcto sigue sin ser evidencia de que el control funciona en LRWA.

### 15.7 Errores comunes y límites

- Copiar las prioridades corporativas en la TO.
- Registros de riesgos que enumeran vulnerabilidades sin consecuencias.
- Capas de «defensa en profundidad» que comparten un único punto de falla.
- Tratar el mapeo a un marco como prueba de seguridad.
- Puntuaciones de probabilidad sin fundamento enunciado.

La primera tabla de riesgos del TMRP evita estos errores nombrando primero cada consecuencia en términos del servicio, de modo que cada vulnerabilidad queda ligada a un daño, y tratando sus probabilidades como hipótesis que se refinarán en capítulos posteriores. Antes de llamar independientes a sus capas, se comprueba si comparten dependencias.

### Ejercicios — capítulo 15

**EX029 — Auditoría de principios.** *Objetivo:* aplicar los principios de diseño. *Entradas:* el Lab 8 y la máquina de estados de la bomba de §9.5. *Pasos:* para cada uno, identifique dos principios de Saltzer–Schroeder aplicados y uno infringido o no abordado, y proponga una corrección. *Evidencia esperada:* tabla. *Rúbrica:* 3 = principios aplicados correctamente, con una carencia creíble (p. ej., la clave escrita en el código del Lab 8 infringe la separación y el mínimo privilegio; HMAC respeta el diseño abierto); 2 = una atribución errónea; 1 = solo nombres; 0 = nada.

**EX030 — Escenario a partir de la consecuencia.** *Objetivo:* empezar por la consecuencia. *Entradas:* el servicio de LRWA. *Pasos:* identifique dos consecuencias inaceptables y, para cada una, las funciones que un adversario necesitaría usar indebidamente y el control de ingeniería más barato que haría la consecuencia físicamente imposible o acotada. *Evidencia esperada:* media página. *Rúbrica:* 3 = consecuencias en términos del servicio, funciones específicas, al menos un límite físico diseñado (p. ej., alivio mecánico de sobrepresión, límite cableado de la bomba de cloro); 2 = todos los controles son digitales; 1 = genérico; 0 = nada.

### Síntesis del capítulo

La seguridad de la infraestructura protege un servicio físico: la integridad y la disponibilidad del control y la seguridad funcional van primero. Empiece por la consecuencia; después, las amenazas y las vulnerabilidades; después, los controles. Aplique principios de diseño duraderos, superponga defensas cuyas fallas sean independientes, suponga la brecha y use los marcos como listas de comprobación estructuradas, no como evidencia.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Siga estudiando — capítulo 15 de 50

[← Capítulo 14](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Capítulo 16 — Ingeniería de sistemas

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) aplicar a un programa de seguridad el ciclo de vida de la ingeniería de sistemas: concepto, requisitos, arquitectura, diseño, integración, verificación, validación, operación y retirada; (2) descomponer las necesidades de las partes interesadas en requisitos de sistema y de subsistema con trazabilidad; (3) gestionar las interfaces y la configuración; y (4) integrar la ingeniería de seguridad en la ingeniería de sistemas en lugar de añadirla a posteriori. Se apoya en los capítulos 5 y 14 y enmarca toda la segunda mitad del libro.

### 16.1 El ciclo de vida y la V

La ingeniería de sistemas gestiona la complejidad pasando de las necesidades a los requisitos, a la arquitectura y a los componentes, y luego subiendo de nuevo a través de la integración y la verificación. El **modelo en V** empareja cada nivel de descomposición de la izquierda con un nivel de verificación de la derecha: las necesidades de las partes interesadas con la validación, los requisitos del sistema con la verificación del sistema, el diseño de subsistemas con las pruebas de integración, los componentes con las pruebas unitarias. El [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) describe este ciclo de vida y sus revisiones técnicas. El desarrollo iterativo no abole la V; recorre V más pequeñas con más frecuencia.

### 16.2 Necesidades, requisitos, trazabilidad

Las necesidades de las partes interesadas son lo que las personas necesitan que el sistema logre, en su propio lenguaje: «el hospital no debe quedarse sin agua más de cuatro horas». Los requisitos del sistema traducen las necesidades en enunciados verificables sobre el sistema (capítulo 5). La **trazabilidad** vincula cada requisito hacia arriba con una necesidad y hacia abajo con los elementos de diseño y la verificación. Un requisito sin padre es un exceso innecesario o una necesidad oculta; una necesidad sin requisito es una brecha; un requisito sin verificación es una afirmación sin respaldo (capítulo 38 y Lab 14).

### 16.3 Interfaces y configuración

La mayoría de las fallas de los sistemas ocurren en las interfaces: entre subsistemas, organizaciones o personas. Un **documento de control de interfaces** especifica los datos, la temporización, los protocolos, la energía, las conexiones físicas y las responsabilidades de cada lado. La **gestión de la configuración** identifica cada elemento (hardware, versiones de firmware, ajustes, documentos), controla los cambios mediante revisión y conserva registros, de modo que se conozca el sistema tal como se construyó. En seguridad, una configuración desconocida es una superficie de ataque desconocida.

Los tres documentos de control de interfaces del TMRP cubren RTU–pasarela, pasarela–SCADA y SCADA–DMZ. Cada uno nombra un responsable a ambos lados.

### 16.4 La seguridad como disciplina de la ingeniería de sistemas

[NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) plantea la ingeniería de seguridad de sistemas como un conjunto de actividades de seguridad integradas en los procesos técnicos de la ingeniería de sistemas: necesidades de protección de las partes interesadas, requisitos de seguridad, diseño arquitectónico para la seguridad, verificación de las afirmaciones de seguridad, y operación y eliminación seguras. Su volumen complementario, [SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1), trata la ciberresiliencia: anticipar condiciones adversas, incluido el ataque, resistirlas, recuperarse de ellas y adaptarse.

El TMRP sigue este enfoque: N2 es una necesidad de protección descompuesta en R1 y R2, y cada uno tiene una verificación planificada.

### 16.5 Ejemplo resuelto: el TMRP como sistema (sintético)

Las necesidades de nivel superior del TMRP: N1, mantener abastecido el hospital (interrupción ≤ 4 h en los escenarios creíbles); N2, detectar y contener el uso indebido del control remoto; N3, recuperar la operación remota en un día hábil; N4, conservar la visibilidad del operador durante los cortes de la red eléctrica. Estas se descomponen en los requisitos R1–R9 presentados hasta ahora (telemetría autenticada, rechazo de repeticiones, límites de consigna, modo manual local, 24 h de autonomía del gabinete, restauración en 8 h, alarmas en menos de 60 s, integridad de los registros, alarma de dosificación independiente). El equipo redacta documentos de control de interfaces para RTU–pasarela, pasarela–SCADA y SCADA–DMZ, y pone bajo control de cambios todas las versiones de firmware y los archivos de configuración de las RTU. Cada requisito tiene ahora una necesidad padre y un método de verificación planificado.

### 16.6 Actividad práctica

Dibuje una matriz de trazabilidad N1–N4 × R1–R9 y marque el padre o los padres de cada requisito. Identifique cualquier necesidad con una cobertura débil. Use una cuadrícula simple con las necesidades como columnas y los requisitos como filas, y marque el padre o los padres de cada requisito. Algunos requisitos sirven a más de una necesidad: R5 apoya la visibilidad durante los cortes de la red eléctrica, y R1 apoya tanto la contención como el suministro al hospital. Cuando termine, cuente los requisitos de cada necesidad. Una necesidad respaldada por un solo requisito merece una segunda mirada, porque una sola prueba fallida la dejaría sin respaldo en el expediente.

### 16.7 Errores comunes y límites

- Requisitos redactados después del diseño para justificarlo.
- Interfaces sin responsable.
- Configuración conocida solo por el ingeniero de puesta en marcha.
- Requisitos de seguridad en un documento aparte, nunca trazados ni verificados.
- Tratar el modelo en V como una excusa de cascada para aplazar las pruebas.

En el TMRP cada uno de estos errores tiene una contramedida: los requisitos se trazan hasta N1–N4, cada interfaz tiene un responsable y el firmware y la configuración de las RTU están bajo control de cambios. La verificación se planifica para cada requisito antes de que empiece el diseño, de modo que la V no se usa como razón para aplazar las pruebas.

### Ejercicios — capítulo 16

**EX031 — Trace y encuentre brechas.** *Objetivo:* construir y analizar una matriz de trazabilidad. *Entradas:* §16.5. *Pasos:* asigne cada uno de R1–R9 a su necesidad o necesidades padre; identifique qué necesidad depende de menos requisitos y proponga un requisito adicional. *Evidencia esperada:* matriz y propuesta. *Rúbrica:* 3 = mapeo defendible, necesidad más débil identificada con un nuevo requisito verificable; 2 = errores de mapeo; 1 = sin propuesta; 0 = nada.

**EX032 — Control de interfaces.** *Objetivo:* especificar una interfaz por completo. *Entradas:* la interfaz pasarela–SCADA. *Pasos:* enumere al menos ocho atributos de la interfaz con valores de ejemplo (elementos de datos, codificación, frecuencia, latencia, autenticación, manejo de errores, fuente de tiempo, responsabilidad, proceso de cambio). *Evidencia esperada:* tabla. *Rúbrica:* 3 = completa y coherente con los Labs 8 y 13; 2 = faltan atributos de seguridad o de responsabilidad; 1 = solo datos; 0 = nada.

### Síntesis del capítulo

La ingeniería de sistemas pasa de las necesidades a sistemas verificados y validados mediante requisitos trazables, interfaces gestionadas y configuración controlada. La seguridad pertenece a esos procesos: las necesidades de protección se convierten en requisitos, los requisitos en arquitectura y diseño, y cada afirmación de seguridad necesita evidencia de verificación.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Siga estudiando — capítulo 16 de 50

[← Capítulo 15](#ch-15) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Capítulo 17 — Fundamentos de control y realimentación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) describir el control en lazo abierto y en lazo cerrado, las consignas, el error y los límites de los actuadores; (2) explicar el control proporcional-integral (PI) y la saturación del integrador (*wind-up*); (3) analizar cómo los datos de sensor falsos, una inyección de datos falsos, llevan a un controlador correcto a un estado inseguro; y (4) diseñar una detección basada en residuos con mediciones físicas independientes e indicar sus puntos ciegos. Se apoya en el capítulo 6 y prepara los capítulos 27 y 33.

### 17.1 Realimentación

Un controlador en **lazo cerrado** mide una variable de proceso, la compara con una consigna y ajusta un actuador para reducir el error. La realimentación hace que los sistemas sean robustos frente a las perturbaciones y los errores de modelo, y hace que confíen por completo en sus sensores. [*Feedback Systems*, de Åström y Murray](https://fbswiki.org/wiki/index.php/Main_Page), disponible gratuitamente en línea, es el texto de referencia de este capítulo. En Hollin Hill, el controlador PI ajusta el caudal de entrada de PS3 para mantener el nivel del depósito en su consigna. Ve el depósito solo a través del transmisor de nivel, de modo que lo que informe ese transmisor es, para el controlador, la verdad. El resto de este capítulo sigue las consecuencias de esa confianza.

### 17.2 Control PI

Un controlador proporcional fija la salida del actuador en $u = K_p e$; deja un error en régimen permanente cuando debe compensarse una perturbación constante. Añadir un término integral, $u = K_p e + K_i\int e\,dt$, elimina el error en régimen permanente porque la integral sigue creciendo hasta que el error es cero. Los actuadores se saturan (una bomba no puede dar más que su caudal máximo) y, mientras están saturados, la integral sigue creciendo (**saturación del integrador**), lo que causa un sobreimpulso cuando el actuador sale de la saturación. El antisaturación (*anti-wind-up*) detiene la integración mientras dura la saturación.

### 17.3 Datos falsos y el controlador confiado

Si un atacante añade un sesgo $b$ a la medición de nivel, el controlador regula el nivel *medido* a la consigna, de modo que el nivel *real* se estabiliza en la consigna menos $b$. El controlador funciona perfectamente; el proceso no. Este es el núcleo de los ataques conscientes del proceso: Stuxnet, según el análisis de [Langner (2011)](https://doi.org/10.1109/MSP.2011.67), manipuló las velocidades de las centrifugadoras mientras reproducía ante los operadores valores de apariencia normal. Las defensas no pueden basarse en el mismo flujo de datos del sensor que controla el atacante.

En Hollin Hill, un transmisor de nivel sesgado bajaría el nivel real mientras la pantalla del operador mostraba la consigna, así que la defensa debe venir de una medición independiente.

### 17.4 Detección basada en residuos

Un **residuo** es la diferencia entre lo que dice una medición y lo que predice un modelo independiente. Para un depósito, el balance de masa predice el cambio de nivel a partir de los caudales de entrada y de salida medidos de forma independiente: $\Delta h = (q_{in} - q_{out})\Delta t / A$. Dos detectores: un **residuo por paso** compara el cambio del nivel medido con el cambio predicho en un paso; un **residuo acumulado** compara el nivel medido con el nivel integrado a partir de los caudales desde la última calibración de confianza. El detector por paso detecta un sesgo abrupto, pero no una deriva lenta; el detector acumulado detecta la deriva, pero acumula el error de los medidores, así que necesita recalibraciones periódicas y un umbral por encima de la deriva normal de los medidores. Un atacante que también controle los caudalímetros anula ambos: la independencia de los caminos de medición es el verdadero control.

### 17.5 Ejemplo resuelto: ataque al nivel de Hollin Hill (sintético)

El Lab 7 simula durante 48 h el control PI de Hollin Hill (superficie en planta de 1.000 m², consigna de 3,0 m, caudal de salida de 300 m³/h, bomba de entrada de 0–600 m³/h). Un sesgo escalón de +1,5 m a las 10 h lleva el nivel real a 1,5 m; ambos detectores alarman a las 10,0 h. Un sesgo de +0,04 m, lo bastante pequeño para parecer un error del sensor, solo lo detecta el detector acumulado. Una rampa lenta de 0,05 m/h elude por completo al detector por paso; el detector acumulado alarma a las 10,6 h, cuando el sesgo es de unos 0,03 m. Sin detección, la rampa deja el nivel real en 1,1 m al cabo de 48 h.

### 17.6 Actividad práctica: Lab 7

```python
# Lab 7 - PI level control under sensor-bias attacks, and two residual detectors (synthetic, offline)
def run(attack=None, hours=48, dt=0.1):
    A = 1000.0                         # m2 reservoir plan area: level h (m), volume A*h (m3)
    h, integ, sp, kp, ki = 3.0, 7.5, 3.0, 400.0, 40.0   # integ preloaded so u = 300 at start
    est = h                            # mass-balance estimate from independently metered flows
    prev_meas, step_t, cum_t, hmin = h, None, None, h
    for k in range(int(hours / dt)):
        t = k * dt
        b = attack(t) if attack else 0.0
        meas = h + b
        err = sp - meas
        u = kp * err + ki * integ
        q_in = min(max(u, 0.0), 600.0)              # pump limits 0..600 m3/h
        if 0.0 < u < 600.0: integ += err * dt         # anti-windup
        q_out = 300.0
        if k > 0 and step_t is None and abs((meas - prev_meas) - (est - est_prev)) > 0.05: step_t = round(t, 1)
        if cum_t is None and abs(meas - est) > 0.03: cum_t = round(t, 1)
        prev_meas, est_prev = meas, est
        h += (q_in - q_out) / A * dt; est += (q_in - q_out) / A * dt
        hmin = min(hmin, h)
    return round(h, 2), round(hmin, 2), step_t, cum_t
print("columns: true final level m, true min level m, step-detector alarm h, cumulative-detector alarm h")
print("no attack        ", run())
print("step bias +1.5 m ", run(lambda t: 1.5 if t >= 10 else 0.0))
print("step bias +0.04 m", run(lambda t: 0.04 if t >= 10 else 0.0))
print("ramp 0.05 m/h    ", run(lambda t: 0.05 * (t - 10) if t >= 10 else 0.0))
```

Salida esperada:

```text
columns: true final level m, true min level m, step-detector alarm h, cumulative-detector alarm h
no attack         (3.0, 3.0, None, None)
step bias +1.5 m  (1.5, 1.4, 10.0, 10.0)
step bias +0.04 m (2.96, 2.95, None, 10.0)
ramp 0.05 m/h     (1.1, 1.1, None, 10.6)
```

Lea las cuatro filas a la luz del ejemplo resuelto. Sin ataque, el nivel se mantiene en tres metros y ningún detector se activa. El sesgo escalón grande lo detectan ambos detectores a la vez, y el nivel real se estabiliza metro y medio por debajo. El escalón pequeño y la rampa lenta son los casos en que los detectores difieren: solo el detector acumulado los ve, y la rampa, si no se hace nada, arrastra el nivel real hasta alrededor de un metro. Recuerde que los caudalímetros del laboratorio son perfectos, de modo que los tiempos de detección reales serían más tardíos.

### 17.7 Errores comunes y límites

- Equiparar «el controlador funcionó» con «el proceso es seguro».
- Una detección que usa el mismo camino de datos que el lazo de control.
- Umbrales fijados sin medir el ruido y la deriva normales.
- Ignorar la saturación del integrador y del actuador en el razonamiento de seguridad funcional.
- Presentar resultados de simulación como comportamiento de la planta; el Lab 7 es un modelo simplificado con caudalímetros perfectos.

Para Hollin Hill, el EX034 muestra claramente el problema de la dependencia: el sensor de nivel y el caudalímetro de entrada están cableados ambos a la RTU3, de modo que comprometer una sola RTU anula los dos lados del residuo.

### Ejercicios — capítulo 17

**EX033 — Compromiso del umbral.** *Objetivo:* ajustar un detector. *Entradas:* Lab 7. *Pasos:* (1) añada ruido gaussiano de desviación típica 0,01 m al nivel medido (semilla 17) y cuente las falsas alarmas del detector acumulado en el caso sin ataque con umbrales de 0,03 y 0,05; (2) informe el tiempo de detección de la rampa con ambos umbrales; (3) recomiende un umbral. *Evidencia esperada:* tabla y recomendación. *Rúbrica:* 3 = experimento implementado correctamente, compromiso explicado, recomendación ligada al tiempo de respuesta; 2 = un solo umbral; 1 = no ejecutado; 0 = nada.

**EX034 — Argumento de independencia.** *Objetivo:* argumentar la independencia de la detección. *Entradas:* la arquitectura de LRWA: el sensor de nivel y el caudalímetro de entrada, ambos cableados a la RTU3; el caudalímetro de salida en PS4, en la RTU4. *Pasos:* identifique qué posiciones del atacante anulan el detector de residuos y proponga un cambio de arquitectura que mejore la independencia. *Evidencia esperada:* media página. *Rúbrica:* 3 = el compromiso de la RTU3 anula tanto el nivel como el caudal de entrada, el cambio propone un camino separado (p. ej., un transmisor de nivel independiente hacia un registrador separado o una comprobación física con indicador de nivel); 2 = parcial; 1 = genérico; 0 = nada.

### Síntesis del capítulo

La realimentación hace que los sistemas sean robustos y crédulos. Un sensor sesgado lleva a un controlador correcto a un estado físico incorrecto. Detecte con residuos construidos a partir de una física independiente, use pruebas por paso y acumuladas para los ataques abruptos y lentos, fije los umbrales a partir del ruido medido y recuerde que la independencia de los caminos de medición, y no la astucia del algoritmo, es lo que derrota a un atacante capaz.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Siga estudiando — capítulo 17 de 50

[← Capítulo 16](#ch-16) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Capítulo 18 — Arquitectura de seguridad

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) describir arquitecturas de referencia para la tecnología operativa, incluidos los modelos por niveles y las DMZ; (2) aplicar los principios de confianza cero donde encajan en la TO y explicar dónde no encajan; (3) diseñar arquitecturas de acceso remoto, registro y monitoreo; y (4) evaluar una arquitectura según las consecuencias, no solo según el número de controles. Se apoya en los capítulos 11, 12 y 15 y prepara los capítulos 26 y 27.

### 18.1 Arquitecturas de TO por niveles

Las arquitecturas de TO suelen describirse por niveles: proceso físico (nivel 0), sensores y actuadores con control básico (1), control de supervisión (2), operaciones del sitio (3), una zona desmilitarizada y la empresa (4–5). El modelo, que desciende de la arquitectura de referencia de Purdue y aparece en la [guía de TO del NIST](https://csrc.nist.gov/pubs/sp/800/82/r3/final), es una herramienta para ubicar activos y conductos, no una ley. Los sistemas modernos difuminan los niveles: sensores conectados a la nube, servicios remotos de los proveedores y dispositivos de campo con enlaces celulares directos.

En LRWA, los servidores SCADA están en la zona de control, las RTU en la zona de campo y la réplica del historiador en la DMZ.

### 18.2 La DMZ y la intermediación de datos

La DMZ de TO se sitúa entre las redes de control y las corporativas. Ningún tráfico directo la atraviesa: los sistemas corporativos hablan con los servicios de la DMZ (réplica del historiador, servidor de parches, pasarela de acceso remoto), que hablan con los sistemas de control. Una prueba útil: si se compromete cualquier equipo corporativo, ¿puede enviar un paquete que llegue a un controlador? Si la respuesta es sí, la DMZ es decorativa. En LRWA, la revisión de flujos aplicó esta prueba y no la superó: un script corporativo de informes llegaba directamente a una RTU de campo. Trasladar esos datos a la réplica del historiador en la DMZ es la forma en que LRWA hace que su DMZ sea real y no decorativa, y la prueba se repite cada vez que se añade un conducto nuevo.

### 18.3 Confianza cero en la TO

La confianza cero, tal como la describe [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final), elimina la confianza implícita basada en la ubicación en la red; cada acceso se autentica, se autoriza y se evalúa por sesión. En la TO, el principio es valioso para el acceso humano y de ingeniería (identidades nominativas, autenticación fuerte, privilegio justo a tiempo, grabación de sesiones) y para los dispositivos nuevos que lo admiten. Encaja mal donde los controladores heredados no pueden autenticarse en absoluto y donde los lazos de control no toleran un punto de decisión de políticas en su camino. La respuesta de ingeniería es aplicar la confianza cero en las fronteras donde se puede (acceso de ingeniería, intermediación de datos, pasarelas) y usar la segmentación y el monitoreo alrededor de lo que no puede autenticarse.

### 18.4 Acceso remoto

El acceso remoto de proveedores y personal es una de las principales vías de entrada a la TO. Diséñelo así: una pasarela de acceso en la DMZ; autenticación multifactor; cuentas nominativas; acceso aprobado por sesión; conexiones a un servidor de salto, nunca directamente a los controladores; grabación de sesiones; y caducidad automática. El [incidente de la planta de tratamiento de agua de Oldsmar](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a) se atribuyó inicialmente a un acceso remoto no autorizado mediante software de escritorio compartido; declaraciones posteriores, recogidas por [WUSF Public Media (2023)](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021), indicaron que probablemente se trató de un error de un empleado. En cualquier caso, el caso ilustra por qué el escritorio compartido sin control en las estaciones de los operadores es una debilidad de arquitectura, y por qué los primeros relatos de un incidente deben tomarse como provisionales.

### 18.5 Arquitectura de monitoreo

El monitoreo de la seguridad de la red en la TO suele ser pasivo: copias del tráfico procedentes de puertos espejo de los conmutadores o de derivadores (*taps*) alimentan sensores que entienden los protocolos industriales y establecen una línea base del comportamiento normal. Los registros de servidores, cortafuegos y pasarelas van a un recolector en la DMZ o en una zona de seguridad dedicada. El monitoreo no debe crear caminos nuevos hacia el control: los sensores reciben solo copias, y las interfaces de gestión están en una red separada.

En LRWA, los derivadores pasivos están en el conmutador de la zona de control y en la cabecera LTE, y sus interfaces de gestión se mantienen fuera de la red monitoreada.

### 18.6 Ejemplo resuelto: la arquitectura objetivo del TMRP (sintético)

El objetivo de LRWA: empresa — cortafuegos — DMZ (réplica del historiador, pasarela de acceso remoto con MFA, preparación de parches, recolector de registros) — cortafuegos — zona de control (par SCADA, servidor de salto de ingeniería) — conducto de campo sobre LTE privada con autenticación en la capa de aplicación (pasarelas para las RTU heredadas) — RTU y paneles de control locales con modo manual. Los derivadores pasivos de monitoreo están en el conmutador de la zona de control y en la cabecera LTE. La arquitectura se evalúa según las consecuencias: las órdenes falsificadas exigen comprometer la clave de una pasarela de campo o los servidores SCADA; el compromiso corporativo da acceso a los datos de la réplica del historiador, pero a ningún camino de paquetes hacia los dispositivos de campo; la pérdida de LTE deja los sitios en modo automático local o manual, con baterías de telemetría de 24 h.

### 18.7 Actividad práctica

Dibuje la arquitectura objetivo en texto o en un diagrama sencillo y anote cada conducto con las entradas de la lista de permitidos del Lab 5. Después aplique la prueba de la DMZ de §18.2. Marque cada conducto con su dirección y su protocolo, y muestre dónde están los derivadores pasivos. Para cada entrada de la lista de permitidos, pregúntese qué zona inicia la conexión y si la prueba de la DMZ sigue superándose si esa zona se compromete. Después añada el camino de ingeniería a través del servidor de salto y compruebe que ninguna regla permite que una estación de ingeniería llegue directamente a una RTU de campo, que fue una de las tres infracciones de flujo de LRWA. Un diagrama que oculta la dirección no puede mostrar si la DMZ funciona realmente.

### 18.8 Errores comunes y límites

- DMZ con reglas directas «temporales».
- Confianza cero declarada para sistemas que no pueden autenticarse.
- Acceso remoto que elude la pasarela (módems de proveedores, herramientas de escritorio compartido).
- Sensores de monitoreo con interfaces de gestión en la red monitoreada.
- Arquitecturas juzgadas por el número de controles y no por las consecuencias que evitan.

En LRWA, el tercer y el primer error son los más probables: un proveedor que quiere acceso rápido a RTU-B para hacer diagnósticos, y una regla directa temporal añadida durante una interrupción. La arquitectura objetivo responde a ambos con la pasarela de acceso de la DMZ y con control de cambios en cada conducto.

### Ejercicios — capítulo 18

**EX035 — Prueba de la DMZ.** *Objetivo:* probar un diseño de DMZ. *Entradas:* una regla propuesta que permite al servidor ERP corporativo escribir el estado de las órdenes de trabajo directamente en la base de datos del SCADA por TCP/1433. *Pasos:* aplique la prueba de la DMZ; proponga un diseño alternativo que satisfaga la necesidad del negocio. *Evidencia esperada:* análisis y diseño. *Rúbrica:* 3 = regla rechazada con su motivo, la alternativa intermedia los datos a través de la DMZ, con el lado de control recogiéndolos o con una exportación unidireccional; 2 = la alternativa sigue siendo entrante; 1 = acepta la regla; 0 = nada.

**EX036 — Arquitectura de acceso remoto.** *Objetivo:* diseñar el acceso del proveedor. *Entradas:* el proveedor de RTU-B necesita acceso trimestral para diagnósticos. *Pasos:* especifique el camino de acceso, la autenticación, la aprobación, el monitoreo y la caducidad; enumere la evidencia que mostraría que el diseño funciona. *Evidencia esperada:* especificación y lista de evidencias. *Rúbrica:* 3 = pasarela, MFA, aprobación por sesión, servidor de salto, grabación, caducidad y evidencia (registros, prueba de que el camino directo está denegado); 2 = sin evidencia; 1 = VPN directa hacia el control; 0 = nada.

### Síntesis del capítulo

Use los modelos por niveles para ubicar activos y conductos, haga real la DMZ sin permitir ningún cruce directo, aplique la confianza cero donde los sistemas puedan autenticarse y la segmentación donde no puedan, haga pasar todo el acceso remoto por una pasarela controlada, monitoree de forma pasiva sin crear caminos y juzgue la arquitectura por las consecuencias que hace difíciles de provocar.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Siga estudiando — capítulo 18 de 50

[← Capítulo 17](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Capítulo 19 — Identidad y criptografía

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) explicar la criptografía simétrica y de clave pública, los hashes y los MAC, y elegir entre ellos; (2) diseñar la autenticación de mensajes con protección contra repeticiones para telemetría con recursos limitados; (3) planificar la gestión de claves (generación, distribución, almacenamiento, rotación, revocación) para una flota de campo; y (4) diseñar la identidad y la autenticación de personas y dispositivos. Se apoya en los capítulos 4, 13 y 18 y prepara los capítulos 27–28.

### 19.1 Primitivas

- Las **funciones de hash** (SHA-256, [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)) transforman los datos en un resumen de tamaño fijo; encontrar colisiones o preimágenes debe ser inviable. Un hash por sí solo no autentica nada.
- El **cifrado simétrico** (AES, [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final)) usa una única clave compartida para la confidencialidad.
- Los **códigos de autenticación de mensajes** (HMAC, [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final); [RFC 2104](https://www.rfc-editor.org/rfc/rfc2104)) permiten a quienes poseen una clave compartida verificar que un mensaje no se ha alterado y que procede de un poseedor de la clave.
- La **criptografía de clave pública**, introducida por [Diffie y Hellman (1976)](https://doi.org/10.1109/TIT.1976.1055638) y llevada a las firmas por [Rivest, Shamir y Adleman (1978)](https://doi.org/10.1145/359340.359342), usa pares de claves: cualquiera puede verificar una firma con la clave pública; solo quien posee la clave privada puede firmar.
- El **cifrado autenticado** (p. ej., AES-GCM) proporciona a la vez confidencialidad e integridad.

Nunca diseñe sus propias primitivas o protocolos cuando haya uno estándar que sirva; TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)) es la opción predeterminada para los enlaces IP que puedan ejecutarlo.

### 19.2 Autenticar la telemetría

Para un enlace con recursos limitados, un diseño habitual es: carga útil más un contador monótono (o una marca de tiempo), un MAC sobre ambos; el receptor comprueba el MAC en tiempo constante y después comprueba que el contador supere el último valor aceptado. El contador derrota la repetición; una marca de tiempo con una ventana de frescura derrota los ataques de retardo, pero necesita relojes sincronizados. Truncar HMAC-SHA256 a 128 bits es habitual para ahorrar ancho de banda, con un margen contra la falsificación reducido en proporción pero todavía muy grande. Persista el último contador o rote las claves al reiniciar; de lo contrario, un reinicio vuelve a abrir la puerta a la repetición (EX018).

### 19.3 Gestión de claves

Las claves son el punto donde la criptografía se encuentra con la operación. Decida: quién genera las claves y dónde (idealmente en hardware, nunca a mano); cómo llegan a los dispositivos (aprovisionamiento en fábrica, inscripción segura); dónde se almacenan (elementos seguros, no archivos de configuración); cómo rotan (de forma programada y tras una sospecha de compromiso); cómo se revocan; y quién puede acceder a ellas. Una clave por cada par de dispositivos limita el radio de impacto: comprometer una RTU no debe permitir a un atacante suplantar a otra. Una única clave para toda la flota es una causa común con $\beta \approx 1$ (capítulo 7).

### 19.4 Identidad de personas y dispositivos

Las personas necesitan cuentas nominativas, autenticación fuerte (multifactor resistente al phishing cuando sea posible; véase [NIST SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final)), roles asignados según las tareas y una baja inmediata cuando se van. Los dispositivos también necesitan identidades (certificados o claves aprovisionadas), para que una pasarela sepa con qué RTU está hablando. Las credenciales compartidas o predeterminadas son la falla de identidad más común en la TO. En el TMRP, los operadores usan cuentas nominativas con autenticación fuerte en los servidores SCADA, y cada RTU tiene su propia clave, de modo que la pasarela sabe qué estación envió cada mensaje.

### 19.5 Ejemplo resuelto: el formato de mensaje del TMRP (sintético)

El ADR-007 eligió HMAC con contadores. La trama del Lab 8 lleva un contador de 8 bytes, un ID de estación de 2 bytes, un nivel de 2 bytes y un HMAC-SHA256 truncado de 16 bytes: 28 bytes, de los cuales 22 son sobrecarga respecto de una carga útil sin autenticar de 6 bytes. Las claves por estación se generan en el elemento seguro de la pasarela durante la inscripción y se almacenan en el almacén de claves de la RTU; el lado SCADA las guarda en un módulo de seguridad de hardware. Las claves rotan anualmente y de inmediato ante una sospecha de compromiso; el contador se persiste en memoria no volátil cada 1.000 incrementos, con un salto hacia delante al reiniciar, de modo que la repetición de mensajes antiguos sigue siendo imposible.

### 19.6 Actividad práctica: Lab 8

```python
# Lab 8 - authenticated telemetry with a counter: tamper and replay are rejected (synthetic key, offline)
import hmac, hashlib, struct
KEY = bytes.fromhex("00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff")  # demo key only
def seal(ctr, station, level_cm):
    body = struct.pack(">QHH", ctr, station, level_cm)
    return body + hmac.new(KEY, body, hashlib.sha256).digest()[:16]
class Receiver:
    def __init__(self): self.last = {}
    def accept(self, msg):
        body, tag = msg[:12], msg[12:]
        if not hmac.compare_digest(tag, hmac.new(KEY, body, hashlib.sha256).digest()[:16]): return "reject: tag"
        ctr, st, lvl = struct.unpack(">QHH", body)
        if ctr <= self.last.get(st, -1): return "reject: replay"
        self.last[st] = ctr; return f"ok st={st} ctr={ctr} level={lvl}cm"
r = Receiver(); m1, m2 = seal(1, 3, 312), seal(2, 3, 309)
forged = m2[:10] + struct.pack(">H", 150) + m2[12:]
for name, m in [("m1", m1), ("m2", m2), ("replay m1", m1), ("forged", forged)]: print(f"{name:10}", r.accept(m))
print("frame bytes:", len(m1), "overhead vs 6-byte payload:", len(m1) - 6)
```

Salida esperada:

```text
m1         ok st=3 ctr=1 level=312cm
m2         ok st=3 ctr=2 level=309cm
replay m1  reject: replay
forged     reject: tag
frame bytes: 28 overhead vs 6-byte payload: 22
```

La clave del laboratorio es un valor de demostración publicado; las claves reales nunca deben aparecer en el código fuente.

Los dos primeros mensajes de la estación tres se aceptan con contadores crecientes. La repetición del primer mensaje se rechaza porque su contador no es mayor que el último valor aceptado, y el mensaje falsificado, con su nivel cambiado de 309 a 150 centímetros, no supera la comprobación de la etiqueta. La última línea confirma el tamaño de trama usado en el ADR-007: veintiocho bytes, veintidós de ellos de sobrecarga. El laboratorio guarda el estado solo en memoria, y por eso el EX018 pregunta qué ocurre tras un reinicio.

### 19.7 Errores comunes y límites

- Usar hashes o CRC como si fueran MAC.
- Comparar etiquetas en un tiempo que no es constante.
- Perder la protección contra repeticiones al reiniciar.
- Claves compartidas por toda la flota; claves en archivos de configuración o en el código fuente.
- Contraseñas predeterminadas y cuentas compartidas.
- Decisiones criptográficas sin un plan para la vida útil del sistema (agilidad criptográfica).

El diseño del TMRP responde a cada punto: las etiquetas se comparan en tiempo constante, los contadores persisten entre reinicios, las claves son por estación y están en hardware seguro, y el formato de mensaje incorpora un identificador de suite para futuros cambios de algoritmo. Cada decisión tiene una prueba.

### Ejercicios — capítulo 19

**EX037 — Persistencia del contador.** *Objetivo:* diseñar una protección contra repeticiones que resista los reinicios. *Entradas:* §19.5 (persistir cada 1.000 incrementos). *Pasos:* explique por qué la RTU debe saltar hacia delante al reiniciar y, como mínimo, cuánto; indique qué debe persistir el receptor. *Evidencia esperada:* explicación. *Rúbrica:* 3 = salto ≥ 1.000 más allá del último valor persistido para que ningún contador se reutilice, el receptor persiste el último aceptado por estación o rota las claves; 2 = solo un lado; 1 = vago; 0 = nada.

**EX038 — Radio de impacto.** *Objetivo:* comparar diseños de claves. *Entradas:* 42 estaciones de campo; opción A, una clave para toda la flota; opción B, una clave por estación. *Pasos:* compare la consecuencia de extraer una clave de una RTU robada, el esfuerzo de rotación tras ese robo y el almacenamiento necesario en el SCADA. *Evidencia esperada:* tabla y recomendación. *Rúbrica:* 3 = A permite al ladrón falsificar cualquier estación y obliga a rotar en toda la flota; B limita la falsificación a una estación con una sola rotación; almacenamiento trivial; recomendación B; 2 = falta una dimensión; 1 = recomendación sin razonamiento; 0 = nada.

### Síntesis del capítulo

Elija primitivas estándar para la propiedad que necesite: hashes para las huellas, MAC o firmas para la autenticidad, cifrado autenticado para la confidencialidad con integridad. Añada frescura para derrotar la repetición y consérvela entre reinicios. La gestión de claves es el verdadero sistema: claves por dispositivo en hardware, rotación y revocación. Dé a las personas y a los dispositivos identidades distintas y con autenticación fuerte.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Siga estudiando — capítulo 19 de 50

[← Capítulo 18](#ch-18) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Capítulo 20 — Infraestructura crítica y seguridad sectorial: contexto de ingeniería

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) describir cómo se define la infraestructura crítica y cómo se organiza en sectores, así como el panorama regulatorio en el que trabajan los ingenieros; (2) caracterizar los sectores por sus procesos físicos, sus unidades de consecuencia y su tecnología; (3) describir las interdependencias entre sectores; y (4) aprender de los incidentes documentados al nivel que sus fuentes públicas permiten. Es el puente entre los fundamentos (capítulos 1–19) y los capítulos del campo (21–50).

### 20.1 Qué hace «crítica» a una infraestructura

Los gobiernos designan como críticos los activos, sistemas y redes cuya incapacidad dañaría gravemente la seguridad, la economía, la salud pública o la seguridad de las personas. Estados Unidos identifica dieciséis [sectores de infraestructura crítica](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors) y, más recientemente, un conjunto de [funciones críticas nacionales](https://www.cisa.gov/national-critical-functions-set) que atraviesan las organizaciones. La [Directiva NIS2 (2022/2555)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/) de la Unión Europea fija obligaciones de ciberseguridad para las entidades esenciales e importantes, y la [Directiva CER (2022/2557)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj) aborda de forma más amplia la resiliencia de las entidades críticas. Las normas sectoriales añaden detalle: las [normas NERC CIP](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx) para los sistemas eléctricos mayoristas de Norteamérica, los [requisitos de evaluación de riesgos de la America's Water Infrastructure Act de 2018](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans) para los sistemas comunitarios de agua de Estados Unidos, [DORA (2022/2554)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) para las finanzas de la UE y los [HHS Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). Todo esto cambia; cite versión y fecha, y vuelva a verificar.

### 20.2 Los sectores como sistemas de ingeniería

Cada sector tiene un proceso físico o de servicio, una **unidad de consecuencia** y una tecnología característica.

| Sector | Proceso | Unidad de consecuencia | Tecnología típica |
|---|---|---|---|
| Agua | Tratar y distribuir agua | Personas sin agua segura × horas | PLC/RTU, SCADA, dosificación, telemetría |
| Electricidad | Generar, transmitir, distribuir | MW o clientes interrumpidos × horas | Relés de protección, EMS/DMS, automatización de subestaciones |
| Salud | Diagnosticar y tratar | Atención retrasada, derivaciones, daño | Historia clínica electrónica, dispositivos médicos, sistemas del edificio |
| Transporte | Mover personas y mercancías | Viajes interrumpidos, incidentes de seguridad | Señalización, control de tráfico, venta de billetes |
| Finanzas | Compensar y liquidar | Transacciones fallidas o retrasadas | Sistemas de pago, infraestructuras de mercado |
| Comunicaciones | Transportar voz y datos | Abonados afectados × horas | Redes troncales, acceso radio, sincronización |

La tabla es una simplificación para orientarse en ingeniería; cada fila es una carrera profesional.

### 20.3 Interdependencia

[Rinaldi, Peerenboom y Kelly (2001)](https://doi.org/10.1109/37.969131) clasifican las interdependencias en físicas, cibernéticas, geográficas y lógicas. El agua necesita electricidad para el bombeo; el restablecimiento eléctrico necesita comunicaciones; los hospitales necesitan agua, energía y comunicaciones; casi todo necesita una hora exacta. La interdependencia convierte las fallas locales en regionales y los proveedores compartidos en causas comunes. La actualización defectuosa de CrowdStrike de julio de 2024, que según la estimación de Microsoft afectó a unos 8,5 millones de dispositivos Windows ([Microsoft, 2024](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)), no fue un ataque, pero perturbó a la vez aerolíneas, hospitales y otros servicios a través de una dependencia de software compartida.

### 20.4 Aprender de los incidentes documentados

Los informes públicos de incidentes son valiosos y parciales. Úselos al nivel de sus fuentes. El [incidente de Colonial Pipeline](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years) de 2021 implicó *ransomware* en la TI de gestión; la empresa detuvo las operaciones del oleoducto como precaución, lo que recuerda que la dependencia de las operaciones respecto de los sistemas de TI (facturación, programación) puede detener el servicio físico sin ningún compromiso de la TO. El [ataque a la red eléctrica ucraniana de 2015](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01) usó acceso remoto para operar interruptores y dañó las capacidades de recuperación. El brote de [WannaCry de 2017](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/) perturbó los servicios del NHS en Inglaterra. Cada uno tiene detalles documentados y preguntas abiertas; cuando los primeros relatos se revisaron, como en Oldsmar, cite ambos.

### 20.5 Ejemplo resuelto: situar a LRWA en su contexto (sintético)

LRWA es una empresa de agua con un hospital entre sus clientes críticos. Su unidad de consecuencia son las personas-hora sin agua segura, ponderadas para los usuarios vulnerables; el almacenamiento propio de St Brenna's da unas cuatro horas de reserva. Sus interdependencias: electricidad (bombeo, tratamiento), comunicaciones (telemetría LTE), suministro químico (cloro) y tiempo (correlación de registros). Se supone que su contexto regulatorio incluye una obligación de evaluación de riesgos y resiliencia similar a la de la AWIA. El alcance del TMRP queda definido por todo esto: el programa no consiste en «proteger el SCADA», sino en «mantener el agua segura llegando a las personas en condiciones adversas creíbles, incluido un ataque».

### 20.6 Actividad práctica

Elija un sector distinto del agua. Solo con fuentes públicas, construya con más detalle su fila de §20.2: tres unidades de consecuencia, tres tecnologías típicas, dos regulaciones clave con versión y fecha, y un incidente documentado con su fuente. Mantenga el perfil al nivel de sus fuentes. Para cada regulación, dé la versión, la fecha en que la consultó y las entidades que abarca. Para el incidente, indique solo lo que dice el informe citado y anote cualquier revisión posterior, como en Oldsmar. Después compare la unidad de consecuencia de su sector con las personas-hora sin agua segura de LRWA, y anote una interdependencia que su sector comparta con el agua, como la electricidad, las comunicaciones o el tiempo.

### 20.7 Errores comunes y límites

- Tratar la «infraestructura crítica» como una categoría tecnológica y no como una categoría de consecuencias.
- Citar regulaciones sin versión ni fecha.
- Repetir relatos de incidentes más allá de lo que las fuentes respaldan.
- Ignorar las dependencias de TI de las operaciones físicas.
- Pensar en un solo sector en un mundo interdependiente.

El propio contexto de LRWA muestra por qué esto importa. Su condición de crítica procede de St Brenna's y de sus demás clientes, no de la tecnología que opera. Sus operaciones dependen de la electricidad, de LTE, del suministro de cloro y de una hora exacta, de modo que analizar el agua de forma aislada pasaría por alto la dependencia oculta del alimentador encontrada antes. Cualquier obligación regulatoria en la que se apoye debe citarse con versión y fecha.

### Ejercicios — capítulo 20

**EX039 — Perfil de un sector.** *Objetivo:* elaborar el perfil de un sector a partir de fuentes públicas. *Entradas:* §20.6. *Pasos:* elabore el perfil con citas. *Evidencia esperada:* una página. *Rúbrica:* 3 = exacto, citado, con unidades de consecuencia medibles y el incidente descrito dentro de sus fuentes; 2 = una afirmación sin citar; 1 = genérico; 0 = nada.

**EX040 — Dependencia compartida.** *Objetivo:* razonar sobre las causas comunes entre sectores. *Entradas:* la caída de CrowdStrike de julio de 2024 tal como la describe Microsoft. *Pasos:* explique en 200 palabras por qué una actualización de software no maliciosa provocó una perturbación intersectorial, qué propiedad de ingeniería revela y una práctica de diseño que limite estos eventos. *Evidencia esperada:* texto. *Rúbrica:* 3 = dependencia compartida o causa común, componente privilegiado con actualización automática, despliegue por etapas o diversidad como práctica, afirmaciones dentro de las fuentes; 2 = práctica genérica; 1 = lo llama ataque; 0 = nada.

### Síntesis del capítulo

La infraestructura crítica se define por las consecuencias. Los sectores difieren en procesos, unidades de consecuencia y tecnología, pero comparten la interdependencia respecto de la energía, las comunicaciones, el tiempo y los proveedores comunes. Trabaje dentro de las regulaciones según versión y fecha, aprenda de los incidentes solo hasta donde llegan sus fuentes y defina cada programa de seguridad por el servicio y las personas que protege.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Siga estudiando — capítulo 20 de 50

[← Capítulo 19](#ch-19) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Capítulo 21 — Infraestructura crítica y seguridad sectorial: requisitos

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) obtener requisitos de seguridad y resiliencia a partir de las consecuencias, las partes interesadas, las regulaciones y la información sobre amenazas; (2) escribir requisitos basados en el desempeño para la operación degradada, la recuperación y la seguridad funcional, no solo para la protección; (3) derivar requisitos de componentes a partir de los requisitos del sistema usando niveles de seguridad; y (4) negociar de forma explícita los conflictos entre requisitos. Aplica al sector los capítulos 5 y 16 y prepara el capítulo 22.

### 21.1 Fuentes de los requisitos

Los requisitos de seguridad de la infraestructura proceden de cinco fuentes, y un buen conjunto se traza hasta todas ellas: **consecuencias** (lo que nunca debe ocurrir y lo que debe restablecerse y con qué rapidez); **partes interesadas** (operadores, clientes como los hospitales, servicios de emergencia, reguladores); **regulaciones y normas** (p. ej., las evaluaciones de riesgos de la AWIA, NERC CIP, las medidas de gestión de riesgos de NIS2); **información sobre amenazas** (capacidades de los adversarios documentadas en fuentes como [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) y los avisos de CISA); y **restricciones** (equipos heredados, presupuesto, personal, certificación de seguridad funcional).

### 21.2 Requisitos para la operación degradada

Un sistema que solo puede estar «seguro» o «comprometido» está mal especificado. Escriba requisitos para los estados intermedios: *Durante la pérdida de la red de telemetría, cada estación de bombeo deberá continuar en control automático local dentro de sus límites configurados durante al menos 72 h.* *Durante una sospecha de compromiso de los servidores SCADA, los operadores deberán poder hacer funcionar PS3 y PS4 en modo manual local con procedimientos y personal documentados en menos de 1 h desde la decisión.* *Tras un incidente, la operación remota deberá restablecerse en menos de 8 h desde la decisión de restaurar, a partir de copias de seguridad fuera de línea verificadas.* Estos son los requisitos que mantienen abastecidas a las personas.

### 21.3 Niveles de seguridad y requisitos de componentes

IEC 62443-3-3 e IEC 62443-4-2 expresan los requisitos de sistema y de componente frente a **niveles de seguridad** (SL 1–4) que reflejan la capacidad del adversario al que hay que resistir, desde la infracción casual o fortuita hasta el ataque sofisticado y con muchos recursos ([presentación general de la serie ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). La evaluación de riesgos para el diseño (IEC 62443-3-2, [página del catálogo](https://webstore.iec.ch/en/publication/30727)) divide el sistema en zonas y conductos y asigna un nivel objetivo a cada uno. Un nivel objetivo se convierte después en requisitos de componente concretos; por ejemplo, la autenticación de todos los usuarios humanos o la protección de la integridad de las comunicaciones. El texto de la norma no es de libre acceso; cite cláusulas solo de un ejemplar obtenido legalmente.

### 21.4 Conflictos y negociación

Los requisitos entran en conflicto: acceso rápido del operador frente a autenticación fuerte; parches frecuentes frente a disponibilidad; registro detallado frente a almacenamiento en sitios remotos; soporte del proveedor frente a aislamiento de la red. No resuelva los conflictos en silencio durante el diseño. Registre cada uno, sus opciones y la decisión con su responsable, que suele ser la persona dueña del riesgo operativo. El primer conflicto registrado del TMRP es entre el modo manual local de R4 y la autenticación de R1, resuelto con un interruptor de llave, una alarma y un registro local. El responsable es operaciones, que asume el riesgo de un acceso manual más lento.

### 21.5 Ejemplo resuelto: el conjunto de requisitos v1.0 del TMRP (sintético)

| ID | Requisito | Fuente | Verificación |
|---|---|---|---|
| R1 | La telemetría y las órdenes entre el campo y el SCADA deberán llevar un MAC sobre el contenido y el contador; las comprobaciones fallidas deberán rechazarse y alarmarse. | Consecuencia (órdenes falsificadas), ADR-007 | Prueba (T1, T2) |
| R2 | Los mensajes repetidos deberán rechazarse, también tras el reinicio de cualquiera de los extremos. | Amenaza (repetición) | Prueba (T2) |
| R3 | Los controladores deberán rechazar las consignas fuera de los límites físicos configurados o que superen el escalón configurado, incluidos los valores no finitos. | Consecuencia (operación insegura) | Prueba (T3) |
| R4 | Cada estación deberá admitir la operación manual local con independencia del SCADA y de la red. | Operación degradada | Demostración |
| R5 | La telemetría de campo deberá funcionar ≥ 24 h con batería a la capacidad de fin de vida. | Parte interesada (visibilidad) | Análisis + prueba (T4) |
| R6 | La operación remota deberá poder restaurarse en menos de 8 h a partir de copias de seguridad fuera de línea. | Recuperación | Ensayo (T7, capítulo 47) |
| R7 | Las alarmas prioritarias deberán llegar a las pantallas de los operadores en menos de 60 s para el 99 % de los eventos. | Operaciones | Prueba (T5) |
| R8 | Los registros de seguridad deberán protegerse en su integridad con anclas fuera de la zona de control. | Investigación | Prueba (T6) |
| R9 | La pérdida de la dosificación de cloro deberá alarmarse en menos de 15 min por un camino independiente del controlador de dosificación. | Consecuencia (agua insegura) | Prueba |

Conflicto registrado: el modo manual local de R4 crea un camino que elude la autenticación de R1. Resolución: el modo manual exige un interruptor de llave físico en el panel, genera una alarma en el SCADA y se registra localmente.

### 21.6 Actividad práctica

Elija un estado degradado aún no cubierto (p. ej., la pérdida del proveedor de cloro durante 7 días) y escriba un requisito, su fuente y su método de verificación. Escriba el requisito con la misma forma que la tabla del TMRP: un identificador, un único enunciado verificable, su fuente y un método de verificación. Una pérdida de siete días del suministro de cloro, por ejemplo, podría llevar a un inventario mínimo de producto químico en el sitio, verificado por inspección, y a un procedimiento con un proveedor alternativo, probado mediante un ejercicio. Compruebe que su requisito no entra en conflicto con uno existente y, si lo hace, registre el conflicto y quién debe decidirlo.

### 21.7 Errores comunes y límites

- Requisitos solo de protección, ninguno de degradación y recuperación.
- Niveles de seguridad asignados sin una evaluación de riesgos documentada.
- Citar cláusulas de normas sin acceso al texto.
- Conflictos resueltos en silencio por quien redacta el diseño.
- Requisitos que no pueden verificarse con los medios del programa.

El conjunto del TMRP evita el primer error incluyendo R4, R5 y R6 para la operación degradada y la recuperación, y evita el cuarto registrando abiertamente el conflicto del modo manual local. Cada requisito del conjunto puede verificarse con el banco, el ensayo o la demostración del propio programa.

### Ejercicios — capítulo 21

**EX041 — Requisitos para estados degradados.** *Objetivo:* especificar el comportamiento bajo estrés. *Entradas:* LRWA, escenario «servidores SCADA cifrados por *ransomware*». *Pasos:* escriba tres requisitos que cubran la continuidad del servicio, la detección y contención, y la restauración, cada uno con su fuente y su verificación. *Evidencia esperada:* tabla. *Rúbrica:* 3 = medibles, cubren las tres fases, verificación realista; 2 = falta una fase; 1 = solo protección; 0 = nada.

**EX042 — Registro de un conflicto.** *Objetivo:* documentar un conflicto. *Entradas:* los operadores quieren que la HMI permanezca con la sesión iniciada todo el turno; un requisito nuevo exige volver a autenticarse tras 15 min de inactividad. *Pasos:* redacte un registro de conflicto con opciones, resolución recomendada y responsable. *Evidencia esperada:* registro. *Rúbrica:* 3 = las opciones incluyen controles compensatorios (control de acceso físico a la sala de control, bloqueo en modo solo visualización con reautenticación rápida para las acciones de control), responsable designado por su rol; 2 = sin responsable; 1 = elige un bando sin opciones; 0 = nada.

### Síntesis del capítulo

Derive los requisitos de las consecuencias, las partes interesadas, las regulaciones, las amenazas y las restricciones. Especifique la operación degradada y la recuperación con tanto cuidado como la protección. Traduzca los niveles de seguridad objetivo en requisitos de componente concretos mediante una evaluación de riesgos documentada, y registre cada conflicto con sus opciones, su decisión y su responsable.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Siga estudiando — capítulo 21 de 50

[← Capítulo 20](#ch-20) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Capítulo 22 — Infraestructura crítica y seguridad sectorial: modelos de sistema y de datos

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) construir un inventario de activos y un modelo del sistema que sirvan para el análisis de seguridad; (2) modelar las dependencias funcionales, los flujos de datos y las fronteras de confianza; (3) representar los estados degradados, no solo «funciona / no funciona»; y (4) mantener el modelo actualizado y protegido como información sensible. Se apoya en los capítulos 2, 13 y 21 y prepara el capítulo 23 (análisis de amenazas y fallas).

### 22.1 Primero, el inventario

No se puede proteger lo que no se conoce. Un inventario de activos de TO registra, para cada dispositivo: identidad, ubicación, función, zona, direcciones de red, versiones de hardware y de firmware, relaciones de comunicación, responsable, criticidad y estado del soporte. Constrúyalo a partir de varias fuentes y concílielas: documentos de diseño, monitoreo pasivo de la red, exportaciones de configuración y recorridos por los sitios. Cada fuente omite cosas: los documentos derivan, el monitoreo pasivo no ve los dispositivos silenciosos y los recorridos no ven los virtuales.

En LRWA, el inventario cubre las 42 estaciones de campo, el par SCADA y las pasarelas, y se construyó con los documentos de diseño, el monitoreo pasivo en el conmutador de control y en la cabecera LTE, y visitas a los sitios.

### 22.2 Tres vistas de un sistema

- **Vista funcional:** lo que hace el sistema (funciones como «mantener el nivel del depósito», «desinfectar», «dar visibilidad al operador») y qué funciones dependen de cuáles (el grafo del Lab 2).
- **Vista física y de red:** dónde están los activos y cómo se conectan: zonas, conductos, enlaces.
- **Vista de flujos de datos:** qué datos se mueven, hacia dónde, en qué dirección, con qué protección y a través de qué **fronteras de confianza**. Los diagramas de flujo de datos con fronteras de confianza son la entrada del modelado de amenazas (capítulo 23).

Mantenga las vistas enlazadas: cada función corresponde a los activos que la implementan; cada flujo corresponde a un conducto.

### 22.3 Estados degradados

Los grafos de «funciona / no funciona» son útiles (capítulo 2), pero insuficientes. Una estación de bombeo puede estar en *automático remoto*, *automático local*, *manual local*, *degradada* (una bomba de dos) o *fuera de servicio*; el depósito puede estar *normal*, *bajo* o *por debajo del piso*. Un **modelo de estados** para cada función crítica, con transiciones causadas por fallas, ataques y acciones de los operadores, permite preguntar: desde la operación normal, ¿qué secuencia de eventos lleva a un estado inaceptable y qué control la interrumpe?

PS4 es el primer candidato evidente en LRWA, porque abastece directamente al hospital.

### 22.4 El modelo como información sensible

Un modelo preciso del sistema es un mapa para un adversario. Guárdelo con control de acceso, versiónelo y publique solo abstracciones. Trate las exportaciones a proveedores y consultores mediante acuerdos. Mantenga un **registro de cambios del modelo** vinculado a la gestión de la configuración (capítulo 16) para que el modelo siga actualizado; un modelo con un año de retraso es un pasivo presentado como activo. El modelo de LRWA, incluidos el grafo de dependencias y las listas de permitidos de las zonas, se guarda con control de acceso y se versiona con cada cambio de configuración.

### 22.5 Ejemplo resuelto: modelo funcional de Hollin Hill (sintético)

La función F1, «abastecer a St Brenna's», se cumple si está disponible el camino A (PS4 directo) o el camino B (depósito de Hollin Hill alimentado por PS3), *y* el tanque propio del hospital cubre el hueco durante la conmutación. El camino A necesita PS4, su energía (alimentador F2 o generador) y su control (basta el automático local). El camino B necesita el depósito por encima del piso y PS3 con energía del alimentador F1. La telemetría no es necesaria para el suministro (el control automático local mantiene las bombas en marcha), pero sí para la *visibilidad* (F3) y la *intervención* remota. Esta idea cambia las prioridades: la propiedad de seguridad más importante para F1 es que nadie pueda ordenar a distancia a las bombas que entren en un estado inseguro, mientras que la pérdida de telemetría es un problema de visibilidad con una reserva de 72 h en automático local (R-local). El árbol de fallas del capítulo 23 formaliza exactamente esta estructura Y/O.

### 22.6 Actividad práctica

Amplíe el Lab 2 para que cada nodo tenga un tipo de dependencia Y u O, e implemente una función de disponibilidad que evalúe si `hospital_supply` funciona dado un conjunto de nodos fallidos. Pruebe con las fallas `{grid_f1}`, `{ps4}` y `{ps4, grid_f1}`. Modele el suministro del hospital como un O de sus dos caminos, con la energía de PS4 como un O del alimentador F2 y el generador. Deje la telemetría fuera de la función de suministro, como argumenta el ejemplo resuelto, pero manténgala en una función de visibilidad separada para que su pérdida siga apareciendo. Después contraste sus tres resultados con el EX043: el suministro debe sobrevivir a la pérdida del alimentador F1 o a la de PS4, y fallar solo cuando se pierden ambos.

### 22.7 Errores comunes y límites

- Inventario a partir de una sola fuente.
- Diagramas sin fronteras de confianza ni dirección de los datos.
- Modelos de «funciona / no funciona» cuando los modos degradados deciden el resultado.
- Modelos que nunca se actualizan o que se comparten libremente.
- Tratar la pérdida de telemetría y el uso indebido del control como la misma consecuencia.

El modelo de Hollin Hill muestra claramente el último error: tratar la pérdida de telemetría como pérdida de suministro enviaría el presupuesto del TMRP a la redundancia de comunicaciones, cuando la propiedad que realmente protege al hospital es que no se pueda ordenar a distancia a las bombas que entren en un estado inseguro.

### Ejercicios — capítulo 22

**EX043 — Evaluación Y/O.** *Objetivo:* implementar y usar un modelo de dependencias mixto. *Entradas:* §22.6. *Pasos:* impleméntelo, ejecute las tres pruebas e informe los resultados. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = semántica correcta; `{grid_f1}` → el suministro sobrevive gracias a PS4 si PS4 funciona en automático local (sin necesidad de LTE); `{ps4}` → sobrevive gracias al depósito; `{ps4, grid_f1}` → falla; 2 = se exige erróneamente la telemetría para el suministro; 1 = no ejecutado; 0 = nada.

**EX044 — Modelo de estados.** *Objetivo:* modelar los estados degradados. *Entradas:* los modos de PS4 de §22.3. *Pasos:* dibuje un modelo de estados con al menos cinco estados y los eventos (falla, ataque, acción del operador) entre ellos; identifique un camino desde *automático remoto* hasta *fuera de servicio* que un atacante remoto podría provocar, y el control que lo rompe. *Evidencia esperada:* tabla de estados y análisis. *Rúbrica:* 3 = estados y eventos coherentes, camino de ataque realista, el control lo rompe (p. ej., el rearme tras un disparo exige una acción local); 2 = solo estados; 1 = solo «funciona / no funciona»; 0 = nada.

### Síntesis del capítulo

Construya el inventario a partir de varias fuentes conciliadas, modele el sistema en vistas funcional, física y de flujos de datos con fronteras de confianza, represente explícitamente los modos degradados y mantenga el modelo actualizado y protegido. Los buenos modelos separan la visibilidad del control y muestran qué propiedad protege realmente el servicio.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Siga estudiando — capítulo 22 de 50

[← Capítulo 21](#ch-21) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Capítulo 23 — Infraestructura crítica y seguridad sectorial: análisis de amenazas y fallas

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) modelar amenazas sobre diagramas de flujo de datos con STRIDE y ATT&CK for ICS; (2) construir árboles de fallas y calcular los conjuntos de corte mínimos y la probabilidad del evento superior; (3) combinar el análisis de fallas y de ataques mediante árboles de ataque, diagramas de pajarita (*bow-tie*) y escenarios guiados por las consecuencias; y (4) enunciar los supuestos y los límites de cada método. Usa los capítulos 7 y 22 y prepara los capítulos 24, 27 y 33.

### 23.1 Modelado de amenazas

El modelado de amenazas pregunta de forma sistemática qué puede salir mal en cada elemento y en cada frontera de confianza de un modelo del sistema. **STRIDE** (suplantación, manipulación, repudio, divulgación de información, denegación de servicio, elevación de privilegios) es un recurso mnemotécnico para las categorías de amenazas que se aplica a cada flujo de datos, proceso y almacén. [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) cataloga las tácticas y técnicas de los adversarios observadas contra sistemas industriales, desde el acceso inicial hasta el impacto (por ejemplo, la manipulación del control o la pérdida de la vista). Use STRIDE para generar amenazas candidatas elemento por elemento y ATT&CK para comprobar su realismo y su exhaustividad frente al comportamiento observado.

### 23.2 Árboles de fallas

Un árbol de fallas descompone un evento superior no deseado en combinaciones de eventos básicos mediante puertas Y y O. Un **conjunto de corte mínimo** es un conjunto mínimo de eventos básicos cuya ocurrencia conjunta provoca el evento superior; la lista de conjuntos de corte mínimos es la lógica de falla del sistema en su forma más simple. Los conjuntos de corte de un solo evento son puntos únicos de falla. Con probabilidades independientes de los eventos básicos, la probabilidad del evento superior se calcula exactamente por enumeración en los árboles pequeños, o de forma aproximada sumando las probabilidades de los conjuntos de corte (la **aproximación de eventos raros**, una cota superior cuando las probabilidades son pequeñas).

### 23.3 Árboles de ataque y diagramas de pajarita

Un árbol de ataque aplica la misma estructura Y/O al objetivo de un adversario; las hojas son acciones del atacante con atributos como el costo, la habilidad o la detectabilidad, en lugar de probabilidades. Asignar probabilidades a los ataques deliberados es cuestionable (los adversarios se adaptan), así que los árboles de ataque suelen usarse para encontrar el camino más barato o menos detectable y colocar después controles en él. Un **diagrama de pajarita** une las causas (izquierda), el evento central y las consecuencias (derecha), y muestra las barreras preventivas antes del evento y las barreras de mitigación después; comunica bien con operadores y directivos.

### 23.4 Combinar fallas y ataques

Los eventos de infraestructura mezclan causas accidentales y deliberadas: un atacante puede esperar a una tormenta, o una falla puede enmascarar una intrusión. Los métodos guiados por las consecuencias, como la [CCE del INL](https://inl.gov/national-security/cce/), parten de la consecuencia inaceptable y preguntan qué combinaciones de fallas y acciones del adversario llegan a ella. Un enfoque práctico: construya el árbol de fallas de la consecuencia; marque qué eventos básicos podría provocar deliberadamente un adversario; vuelva a calcular con esos eventos fijados como «ocurridos» para ver qué queda como protección. Lo que queda es su verdadera defensa frente a un adversario capaz.

### 23.5 Ejemplo resuelto: pérdida del suministro al hospital (sintético)

Evento superior: St Brenna's pierde el suministro durante más de 4 h en un año. Siguiendo el modelo del capítulo 22: el camino A (PS4) se pierde si falla PS4, o si fallan a la vez el alimentador F2 *y* el generador de PS4; el camino B se pierde si el depósito no está disponible, si falla PS3 o si falla el alimentador F1; y el evento exige que se pierdan ambos caminos *y* que el tanque del hospital no logre cubrir el hueco (TANK). El Lab 9 enumera el árbol con probabilidades anuales sintéticas. Hay seis conjuntos de corte mínimos, todos de orden tres o cuatro, porque TANK aparece en todos. El mayor contribuyente es {G1, PS4, TANK}. La probabilidad exacta es de 9,10 × 10⁻⁵ por año; la aproximación de eventos raros da 9,36 × 10⁻⁵.

Ahora, la visión adversarial: si un atacante puede detener a distancia PS3 y PS4 (sin R1), ambos pasan a «ocurridos» y el evento superior se reduce a TANK por sí solo, con probabilidad 0,03. La autenticación de las órdenes remotas lleva el sistema de un problema de dos de tres fallas independientes a un problema de punto único de falla. Esa comparación es el argumento más claro a favor de R1 en todo el expediente.

### 23.6 Actividad práctica: Lab 9

```python
# Lab 9 - fault tree: minimal cut sets and top-event probability (synthetic annual probabilities, offline)
from itertools import product
P = {"G1": 0.10, "G2": 0.08, "GEN": 0.05, "PS4": 0.02, "PS3": 0.02, "RES": 0.01, "TANK": 0.03}
# Top: hospital loses supply > 4 h = (feed A lost AND feed B lost)
# feed A (PS4 direct) lost = PS4 OR (G2 AND GEN);  feed B (reservoir) lost = RES OR PS3 OR G1
# hospital on-site tank TANK failing (empty/contaminated) is needed too: top = A AND B AND TANK
def top(s): A = s["PS4"] or (s["G2"] and s["GEN"]); B = s["RES"] or s["PS3"] or s["G1"]; return A and B and s["TANK"]
names = list(P); exact = 0.0; cuts = []
for bits in product([0, 1], repeat=len(names)):
    s = dict(zip(names, bits)); pr = 1.0
    for n in names: pr *= P[n] if s[n] else 1 - P[n]
    if top(s):
        exact += pr
        on = frozenset(n for n in names if s[n])
        cuts.append(on)
mcs = sorted({c for c in cuts if not any(o < c for o in cuts)}, key=lambda c: (len(c), sorted(c)))
for c in mcs:
    pr = 1.0
    for n in c: pr *= P[n]
    print(sorted(c), f"{pr:.2e}")
rare = sum(eval("*".join(str(P[n]) for n in c)) for c in mcs)
print(f"rare-event approx {rare:.3e}  exact {exact:.3e}")
```

Salida esperada:

```text
['G1', 'PS4', 'TANK'] 6.00e-05
['PS3', 'PS4', 'TANK'] 1.20e-05
['PS4', 'RES', 'TANK'] 6.00e-06
['G1', 'G2', 'GEN', 'TANK'] 1.20e-05
['G2', 'GEN', 'PS3', 'TANK'] 2.40e-06
['G2', 'GEN', 'RES', 'TANK'] 1.20e-06
rare-event approx 9.360e-05  exact 9.101e-05
```

Los seis conjuntos de corte contienen TANK, de modo que el almacenamiento propio del hospital aparece en todos los caminos hacia el evento superior. El mayor contribuyente individual combina el alimentador F1, PS4 y el tanque. Las dos cifras de probabilidad difieren ligeramente porque la aproximación de eventos raros cuenta dos veces los conjuntos de corte que se solapan, y por eso da una pequeña cota superior del valor exacto. La lectura adversarial del ejemplo resuelto se obtiene fijando PS3 y PS4 como falla segura y volviendo a ejecutar, lo que el EX045 le pide hacer a usted.

### 23.7 Errores comunes y límites

- Árboles de fallas con eventos básicos dependientes tratados como independientes (energía común, software común).
- Probabilidades de ataques deliberados presentadas como frecuencias.
- Modelos de amenazas sin fronteras de confianza.
- Listas STRIDE nunca contrastadas con el comportamiento observado de los adversarios.
- Tratar la aproximación de eventos raros como exacta cuando las probabilidades son grandes.

El propio Lab 9 supone independencia, así que una falla de software compartida en las RTU de ambas estaciones haría optimistas sus cifras. Sus probabilidades de falla de PS3 y PS4 son frecuencias de fallas aleatorias, de modo que no dicen nada sobre la probabilidad de que un atacante detenga ambas estaciones; por eso el caso adversarial se trata condicionando y no añadiendo una probabilidad de ataque.

### Ejercicios — capítulo 23

**EX045 — Árbol condicionado al adversario.** *Objetivo:* cuantificar lo que aporta la autenticación. *Entradas:* Lab 9. *Pasos:* (1) fije PS3 y PS4 con probabilidad 1 (el atacante puede detenerlas a distancia) y calcule la probabilidad del evento superior; (2) en su lugar, fije G1 y G2 en 1 (el atacante puede cortar ambos alimentadores) y vuelva a calcular; (3) interprete ambos resultados. *Evidencia esperada:* números e interpretación de 150 palabras. *Rúbrica:* 3 = números correctos (0,03; y con G1=G2=1, superior = P(TANK)·P(PS4 o GEN), calcúlelo), interpretación vinculada a los controles (R1; independencia del generador y tanque); 2 = un número erróneo; 1 = no ejecutado; 0 = nada.

**EX046 — STRIDE sobre un flujo.** *Objetivo:* modelar las amenazas de un flujo de datos. *Entradas:* el flujo pasarela–SCADA (tramas del Lab 8 sobre el conducto LTE). *Pasos:* aplique cada categoría de STRIDE, nombre una técnica de ATT&CK for ICS donde encaje e indique el control existente o propuesto. *Evidencia esperada:* tabla de seis filas. *Rúbrica:* 3 = las seis categorías tienen sentido y los controles corresponden (p. ej., suplantación → MAC; DoS → recurso al automático local); 2 = una categoría vacía; 1 = solo una lista; 0 = nada.

### Síntesis del capítulo

Los modelos de amenazas generan lo que podría salir mal en cada frontera de confianza; ATT&CK los mantiene realistas. Los árboles de fallas y los conjuntos de corte mínimos muestran la lógica de falla y los puntos únicos de falla; los árboles de ataque y los diagramas de pajarita muestran los caminos del adversario y las barreras. Combínelos condicionando a lo que un adversario puede provocar: lo que queda es la defensa que realmente importa.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Siga estudiando — capítulo 23 de 50

[← Capítulo 22](#ch-22) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Capítulo 24 — Infraestructura crítica y seguridad sectorial: métodos I

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) seleccionar métodos de análisis adecuados para una pregunta de diseño: evaluación de riesgos, STPA, simulación, experimento en banco de pruebas, ejercicio de mesa; (2) realizar una evaluación de riesgos estructurada y documentarla de forma reproducible; (3) planificar un estudio de simulación con verificación y validación explícitas; y (4) elegir una evidencia proporcionada a la decisión. Se apoya en los capítulos 15, 21 y 23 y prepara el taller de diseño (capítulo 25).

### 24.1 Ajustar el método a la pregunta

| Pregunta | Método | Evidencia típica |
|---|---|---|
| ¿Qué escenarios importan más? | Evaluación de riesgos (SP 800-30, IEC 62443-3-2) | Tabla de escenarios, justificación |
| ¿Qué acciones de control son inseguras? | STPA ([Leveson, 2004](https://doi.org/10.1016/S0925-7535(03)00047-X)) | Acciones de control inseguras, escenarios de pérdida |
| ¿Cómo responde el proceso? | Simulación (Labs 1, 7) | Modelo, registro de V&V, ejecuciones |
| ¿Funciona el control en la práctica? | Experimento en banco de pruebas | Plan de pruebas, resultados, registros |
| ¿Pueden las personas ejecutar el plan? | Ejercicio de mesa o funcional | Informe posterior a la acción |
| ¿Es sólido el diseño? | Revisión independiente (capítulo 45) | Hallazgos de la revisión y respuestas |

Los proyectos de ingeniería usan varios; un error común es usar un método para responder la pregunta de otro, por ejemplo, un ejercicio de mesa que «muestra» que un tiempo de restauración es alcanzable.

### 24.2 Evaluación de riesgos estructurada

Una evaluación reproducible documenta: alcance y supuestos; versión del modelo del sistema; fuentes de amenaza y sus capacidades supuestas; escenarios (evento de amenaza → vulnerabilidad → consecuencia); controles existentes; escalas de probabilidad y de consecuencia con sus definiciones; calificaciones con su justificación; y controles recomendados. Las escalas deben definirse en los términos de la organización (personas-hora sin agua, no «alto»). Las calificaciones sin justificación son opiniones; con justificación, pueden cuestionarse y mejorarse. Las escalas del TMRP usan personas-hora sin agua en el hospital y en los demás clientes, de modo que las calificaciones significan lo mismo para los operadores y para los directivos.

### 24.3 Simulación con verificación y validación

La **verificación** pregunta si el modelo está implementado correctamente (¿hace el código lo que dice el modelo?); la **validación** pregunta si el modelo representa la realidad lo bastante bien para su propósito. [Sargent (2013)](https://doi.org/10.1057/jos.2012.20) describe técnicas: comparación con resultados analíticos (el Euler del Lab 1 frente a la solución exacta), pruebas en condiciones extremas, comparación con datos históricos, validez aparente ante los operadores y análisis de sensibilidad. Enuncie el uso previsto del modelo; un modelo válido para estimar la autonomía puede no serlo para analizar los transitorios de presión.

Para el TMRP, el modelo de autonomía se valida con una interrupción planificada histórica antes de usarlo en el escenario combinado de pérdida de la red eléctrica y de la telemetría.

### 24.4 Ejercicios con personas

Los ejercicios de mesa recorren con un equipo un escenario para probar los planes, los roles y las decisiones; los ejercicios funcionales realizan algunas acciones de verdad. Diséñelos con objetivos, inyecciones, observadores y un informe posterior a la acción que registre las carencias sin culpar a nadie. Muestran si las personas saben qué hacer y dónde los planes son ambiguos; no miden el desempeño de los equipos. El ejercicio funcional nocturno del TMRP sobre el modo manual local en PS3 y PS4 es el ejemplo: usa la dotación real de la noche, registra el tiempo necesario para establecer la operación manual e informa de las carencias que encuentra, pero no puede mostrar si las bombas o las pasarelas cumplen sus propios requisitos.

### 24.5 Ejemplo resuelto: elegir los métodos del TMRP (sintético)

El TMRP tiene cuatro preguntas abiertas: (1) qué escenarios merecen financiación: evaluación de riesgos con escalas de consecuencia en personas-hora; (2) si los operadores pueden pasar PS3/PS4 a manual local en menos de 1 h: un ejercicio funcional nocturno con la dotación real; (3) si la pasarela rechaza las tramas falsificadas y repetidas: pruebas T1–T2 en banco; (4) si el depósito dura lo suficiente durante una interrupción combinada de la red eléctrica y la telemetría: simulación al estilo del Lab 1, validada con una interrupción planificada histórica. El plan nombra la evidencia de cada método y su límite, para que nadie cite después el ejercicio de mesa como prueba de R6.

### 24.6 Actividad práctica

Realice con dos compañeros un ejercicio de mesa de 45 minutos sobre el escenario «servidores SCADA cifrados a las 02:00», usando el conjunto de requisitos del TMRP. Registre las decisiones, los tiempos y las carencias en un informe posterior a la acción. Asigne los roles antes de empezar: el operador nocturno, el responsable de turno y un facilitador que entrega las inyecciones. Use los requisitos del TMRP como vara de medir, en especial la operación manual local en menos de una hora y la restauración de la operación remota en menos de ocho. Registre cada decisión con su hora y quién la tomó. El informe posterior a la acción debe enumerar lo que el plan no cubría, sin señalar a nadie como causa, y debe indicar que un ejercicio de mesa no puede mostrar si la restauración en ocho horas es alcanzable.

### 24.7 Errores comunes y límites

- Estirar un único método para responder todas las preguntas.
- Escalas de probabilidad y de consecuencia sin definir.
- Simulaciones presentadas sin V&V ni uso previsto.
- Informes de ejercicios que culpan a personas o registran solo los éxitos.
- Evidencia desproporcionada respecto de la decisión (demasiado poca para lo crítico para la seguridad funcional, demasiada para lo trivial).

El plan de métodos del TMRP se protege del primer error nombrando el límite de cada método, de modo que un ejercicio de mesa nunca se cite como prueba de que R6 se cumple. Sus escalas de probabilidad y de consecuencia se definen en personas-hora, y la simulación de autonomía enuncia su uso previsto.

### Ejercicios — capítulo 24

**EX047 — Ajuste del método.** *Objetivo:* seleccionar métodos. *Entradas:* cuatro preguntas: (a) ¿provocarían sobrepresión las consignas falsificadas en PS4? (b) ¿encuentra el detector de anomalías del proveedor las inundaciones de escrituras Modbus? (c) ¿puede el responsable de turno autorizar el modo manual local de noche? (d) ¿cuál es la clasificación anual de riesgos de ocho escenarios? *Pasos:* elija para cada una un método, su evidencia y su principal límite. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (a) simulación o análisis hidráulico más STPA, (b) experimento en banco de pruebas, (c) ejercicio, (d) evaluación de riesgos, con límites honestos; 2 = un desajuste; 1 = un solo método para todo; 0 = nada.

**EX048 — Valide un modelo.** *Objetivo:* planificar la V&V. *Entradas:* el modelo del Lab 1. *Pasos:* proponga tres comprobaciones de verificación y tres de validación, incluida una con datos históricos, e indique el uso previsto del modelo y un uso para el que no es válido. *Evidencia esperada:* lista. *Rúbrica:* 3 = verificación y validación diferenciadas, comparación histórica especificada, uso no válido identificado (p. ej., transitorios de presión, calidad del agua); 2 = se mezclan las dos V; 1 = vago; 0 = nada.

### Síntesis del capítulo

Asigne a cada pregunta un método capaz de responderla y conozca el límite de cada método. Haga reproducibles las evaluaciones de riesgos con escalas definidas y justificación; verifique y valide las simulaciones para un propósito enunciado; use los ejercicios para probar a las personas y los planes, no los equipos; y gradúe la evidencia según la decisión que respalda.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Siga estudiando — capítulo 24 de 50

[← Capítulo 23](#ch-23) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Capítulo 25 — Taller de diseño I

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) conducir un taller de diseño estructurado, desde el encargo hasta un concepto revisado; (2) generar alternativas de concepto y compararlas con criterios ponderados; (3) presentar un concepto con sus supuestos, sus riesgos y su plan de verificación ante un panel de revisión crítico; y (4) responder de forma constructiva a los hallazgos de la revisión. Integra los capítulos 16–24 en el primer artefacto de diseño completo y prepara el capítulo 26.

### 25.1 Qué es un taller

Un taller de diseño es un ejercicio de diseño iterativo y sometido a crítica. Los equipos reciben un encargo, producen conceptos, los presentan a revisores que cuestionan los supuestos, y los revisan. Su valor es la crítica: los diseños mejoran más rápido cuando alguien competente intenta romperlos pronto. En este curso, cada taller produce un **expediente de concepto**: enunciado del problema, extracto de los requisitos, alternativas, evaluación, concepto seleccionado, registro de riesgos, plan de verificación y preguntas abiertas. Para el TMRP, el expediente del Taller I cubre la operación remota de las seis estaciones de bombeo y de la planta de Fenwick.

### 25.2 El encargo

**Encargo del Taller I (sintético):** LRWA debe proteger la operación remota de PS1–PS6 y de la planta de Fenwick. Restricciones: presupuesto de 250 k (Lab 16); PS1 y PS2 tienen unidades RTU-A heredadas que no pueden sustituirse durante tres años; la LTE privada es el único enlace económico; una sala de control con personal 24/7 y un solo operador de noche; el hospital necesita una interrupción ≤ 4 h. Entregables: de dos a cuatro conceptos, evaluación, selección y plan de verificación. La restricción de la dotación nocturna es la que más condiciona los conceptos, porque cualquier diseño que exija que alguien vaya en coche a una estación para cada cambio deja a un único operador sin capacidad de atender seis sitios.

### 25.3 Generar alternativas

Genere conceptos que difieran en principio, no en detalle: (A) LTE cifrada por el operador con solo un cortafuegos central; (B) túneles IPsec desde las RTU nuevas y pasarelas para las heredadas; (C) autenticación en la capa de aplicación con pasarelas y una fuerte autonomía local; (D) ningún control remoto: solo monitoreo, con operadores enviados para cada cambio. Incluir un extremo (D) aclara cuánto vale el control remoto. Los cuatro conceptos difieren en dónde se produce la autenticación y en si existe o no el control remoto. La puntuación de operabilidad muy baja del concepto D en la evaluación muestra por qué vale la pena incluir un extremo.

### 25.4 Evaluación ponderada

Defina los criterios a partir de los requisitos y las restricciones, pondérelos antes de puntuar, puntúe cada concepto con evidencia y compruebe si la clasificación resiste cambios plausibles de los pesos (sensibilidad). Una suma ponderada es una conversación estructurada, no un oráculo.

| Criterio (peso) | A | B | C | D |
|---|---:|---:|---:|---:|
| Impide órdenes falsificadas, R1 (0,30) | 1 | 4 | 4 | 5 |
| Servicio durante la pérdida de la red, R4 (0,20) | 2 | 3 | 5 | 5 |
| Operabilidad con un operador nocturno (0,20) | 5 | 4 | 4 | 1 |
| Costo dentro de 250 k (0,15) | 5 | 2 | 4 | 4 |
| Compatibilidad con lo heredado (0,15) | 5 | 3 | 4 | 5 |
| **Puntuación ponderada** | **3,20** | **3,35** | **4,20** | **4,05** |

D puntúa cerca de C porque es muy seguro, pero su puntuación de operabilidad refleja que un operador nocturno no puede desplazarse a seis sitios; en la práctica, incumple la necesidad del hospital. El desafío del panel al equipo es mostrar que la ventaja de C resiste si la operabilidad pesa 0,10 y R1 pesa 0,40 (EX049).

### 25.5 Presentar y responder a la revisión

Presente: el problema en una frase, las restricciones, las alternativas, la evaluación, la selección, los riesgos y lo que no ha verificado. Los revisores atacarán los supuestos; registre cada hallazgo, responda (aceptar, rechazar con un motivo, aplazar con un responsable) y revise. Un equipo a la defensiva no aprende nada; un equipo que acepta todos los comentarios no tiene diseño. Los hallazgos del panel del EX050 son típicos del TMRP: la pasarela como punto único de falla, el modo manual local que elude la autenticación y la falta del costo de personal para la gestión de claves. Cada uno necesita una respuesta registrada con un responsable. El segundo puede responderse con evidencia que ya existe, porque el interruptor de llave, la alarma y el registro local quedaron registrados cuando se resolvió el conflicto entre R4 y R1.

### 25.6 Actividad práctica

Produzca el expediente de concepto para el encargo del Taller I en no más de ocho páginas y celebre una revisión de 20 minutos con dos compañeros que actúen como panel. Limítese a ocho páginas para que el panel pueda leerlo antes de la revisión. Presente los cuatro conceptos en la tabla ponderada, muestre la comprobación de sensibilidad e indique lo que no se ha verificado. Pida a cada compañero que ataque un supuesto, como la estimación de costos o la puntuación de operabilidad nocturna. Registre sus hallazgos en un registro de respuestas con aceptar, rechazar o aplazar y un responsable, como pide el EX050, y revise el concepto antes de entregar el expediente.

### 25.7 Errores comunes y límites

- Alternativas que son variaciones de una sola idea.
- Pesos elegidos después de puntuar.
- Puntuaciones sin evidencia.
- Sin comprobación de sensibilidad.
- Tratar la revisión como un examen que aprobar y no como información.

El Taller I se protege de estos errores: sus cuatro conceptos difieren en principio, sus pesos se fijaron antes de puntuar y el EX049 comprueba si la ventaja del concepto C resiste otros pesos. El desafío del panel al concepto D, que puntúa bien en seguridad pero incumple la operabilidad nocturna, es el tipo de hallazgo que debe producir una revisión. Cada puntuación cita evidencia.

### Ejercicios — capítulo 25

**EX049 — Sensibilidad a los pesos.** *Objetivo:* probar la solidez de una selección. *Entradas:* la tabla de §25.4. *Pasos:* vuelva a calcular con los pesos (R1 0,40, pérdida de red 0,20, operabilidad 0,10, costo 0,15, heredado 0,15) y con (R1 0,20, pérdida de red 0,20, operabilidad 0,30, costo 0,15, heredado 0,15). *Evidencia esperada:* puntuaciones y conclusión. *Rúbrica:* 3 = aritmética correcta y una conclusión honesta sobre cuándo D supera a C y qué implica; 2 = un error aritmético; 1 = un solo escenario; 0 = nada.

**EX050 — Registro de respuestas a la revisión.** *Objetivo:* responder a la crítica. *Entradas:* tres hallazgos del panel: «la pasarela es un punto único de falla»; «el modo manual local elude la autenticación»; «la estimación de costos ignora el personal para la gestión de claves». *Pasos:* escriba una entrada del registro de respuestas para cada uno (aceptar/rechazar/aplazar, motivo, cambio, responsable). *Evidencia esperada:* registro. *Rúbrica:* 3 = respuestas sustantivas con cambios de diseño cuando procede (p. ej., pasarelas duplicadas o caída a automático local; interruptor de llave y alarma; añadir una línea de costo operativo); 2 = una respuesta despectiva; 1 = acepta todo sin cambios; 0 = nada.

### Síntesis del capítulo

Un taller convierte el conocimiento en un diseño sometido a crítica. Genere alternativas realmente distintas, incluidos los extremos; pondere los criterios antes de puntuar y compruebe la sensibilidad; presente abiertamente los supuestos y las afirmaciones no verificadas; y trate los hallazgos de la revisión como información de diseño, con respuestas registradas.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Siga estudiando — capítulo 25 de 50

[← Capítulo 24](#ch-24) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Capítulo 26 — Infraestructura crítica y seguridad sectorial: alternativas de arquitectura

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) comparar patrones de arquitectura para sistemas críticos: control centralizado frente a distribuido, esquemas de redundancia, diversidad, flujos unidireccionales, autonomía local; (2) analizar el comportamiento de cada patrón ante fallas y ataques; (3) cuantificar las compensaciones con los modelos de disponibilidad, latencia y costo de capítulos anteriores; y (4) documentar las decisiones de arquitectura con sus consecuencias. Desarrolla el concepto seleccionado en el Taller I y prepara el capítulo 27.

### 26.1 Control centralizado y distribuido

El control centralizado (un SCADA que dirige dispositivos de campo sencillos) da a los operadores una vista única y facilita la coordinación, pero concentra tanto la falla como el ataque. El control distribuido (controladores de campo capaces, que funcionan localmente y aceptan objetivos de supervisión) se degrada con suavidad cuando se pierden el centro o la red, a costa de más dispositivos que proteger y configurar. La mayoría de los diseños resilientes son jerárquicos: el control local mantiene de forma autónoma una operación segura; el centro optimiza y coordina.

La elección del TMRP, el C2 jerárquico, mantiene el control automático local en cada estación.

### 26.2 Patrones de redundancia

- **Reserva en caliente:** una segunda unidad en marcha y lista para tomar el relevo automáticamente (pares de servidores SCADA).
- **Reserva en frío:** un repuesto que hay que arrancar o instalar (RTU de repuesto en un estante).
- **N+1:** una unidad más de las necesarias (tres bombas donde dos cubren la demanda).
- **Votación k de n:** se usa en los sistemas de seguridad funcional (sensores 2 de 3) para tolerar una entrada defectuosa o falsificada.

Cada patrón debe juzgarse frente a las causas comunes (capítulo 7): dos servidores idénticos con software idéntico son redundantes frente a una falla de hardware y no frente al malware.

### 26.3 Diversidad

La diversidad (tecnologías, proveedores, caminos o equipos distintos) reduce las causas comunes. Cuesta más, aumenta las competencias necesarias y puede añadir superficie de ataque. Úsela donde una causa común sería inaceptable: un segundo camino de comunicación a través de otro operador y con otra alimentación; un disparo de seguridad cableado independiente del software; un indicador manual que un operador puede leer cuando toda la electrónica es sospechosa. En LRWA, el argumento a favor de la diversidad es más claro en el camino de telemetría, donde un segundo operador con alimentación separada eliminaría la dependencia compartida del alimentador F1, y en Hollin Hill, donde un indicador de nivel manual da a los operadores una lectura fiable cuando toda la electrónica es sospechosa.

### 26.4 Flujos unidireccionales y autonomía local

Las pasarelas unidireccionales imponen físicamente un flujo de datos solo de salida; eliminan toda una clase de ataques entrantes contra el lado protegido, pero también eliminan el control remoto a través de ese camino. La autonomía local (la capacidad de un sitio para funcionar con seguridad sin el centro) es un patrón de resiliencia que además limita la consecuencia de un ataque: un centro comprometido puede perturbar la optimización, pero no debería poder llevar un sitio fuera de sus límites seguros si esos límites se imponen localmente (R3).

La opción C3 del TMRP lleva esto a su extremo para el monitoreo.

### 26.5 Ejemplo resuelto: tres arquitecturas del TMRP comparadas (sintético)

| Propiedad | C1: central + IPsec | C2: jerárquica + autenticación en la capa de aplicación (elección del Taller I) | C3: jerárquica + diodo para el monitoreo, control solo local |
|---|---|---|---|
| Orden remota falsificada | Exige la clave del túnel o comprometer el SCADA | Exige la clave por estación o comprometer el SCADA | Imposible a distancia |
| Centro comprometido | Puede dar órdenes a cualquier sitio dentro de los límites de la RTU | Puede dar órdenes a cualquier sitio dentro de los límites impuestos localmente | No puede dar órdenes |
| Pérdida de la red | Los sitios mantienen el último estado | Los sitios funcionan en automático local 72 h | Los sitios funcionan en automático local |
| Operabilidad | Alta | Alta | Baja de noche (hay que enviar personal) |
| Indisponibilidad de comunicaciones, dos operadores, β = 0,05 | 0,00136 | 0,00136 | n/a para el control |
| Costo | Medio | Medio | Capital bajo, personal alto |

La tabla hace explícito el riesgo residual de C2: un centro SCADA comprometido aún puede emitir órdenes autenticadas dentro de los límites locales. Ese residuo se acepta sobre la base del monitoreo, la aprobación por dos personas de los cambios masivos de consigna y los límites locales que mantienen seguro el proceso.

### 26.6 Actividad práctica

Escriba un ADR que elija entre C2 y C3 específicamente para PS4 (la alimentación del hospital), teniendo en cuenta que las consignas de PS4 cambian rara vez. Parta de la tabla comparativa y de lo que hace especial a PS4: abastece directamente a St Brenna's y sus consignas cambian rara vez. Sopese la seguridad de eliminar las escrituras remotas de consigna frente al costo de enviar a un técnico para cada cambio, sobre todo de noche con un solo operador de guardia. Indique qué le haría revisar la decisión, como un aumento de la frecuencia de los cambios de consigna. La defensa del capítulo 50 se refiere más adelante a un ADR con exactamente esta opción de solo local para PS4.

### 26.7 Errores comunes y límites

- Redundancia sin diversidad, presentada como resiliencia frente al ataque.
- Diversidad en todas partes, que desborda la capacidad de mantenimiento.
- Centralización por comodidad, sin límites seguros locales.
- Ignorar el costo operativo de las arquitecturas que eliminan el control remoto.
- Comparaciones de arquitectura sin números cuando hay números disponibles.

La tabla del TMRP evita el último error poniendo números donde existen, como la indisponibilidad de las comunicaciones con un factor de causa común, y declarando con claridad el costo de personal de C3. También acepta abiertamente el residuo de C2 en lugar de afirmar que su redundancia protege frente al ataque.

### Ejercicios — capítulo 26

**EX051 — Votación frente a la falsificación.** *Objetivo:* analizar la votación 2 de 3. *Entradas:* tres transmisores de nivel en Hollin Hill; selección de la mediana. *Pasos:* explique qué puede y qué no puede hacer un transmisor falsificado; qué puede hacer un atacante que controle la RTU común que lee los tres; y cómo restablecer la independencia. *Evidencia esperada:* media página. *Rúbrica:* 3 = la mediana tolera una entrada falsificada, la RTU común anula la votación, independencia mediante E/S o controladores separados; 2 = se omite la RTU común; 1 = genérico; 0 = nada.

**EX052 — Decisión de arquitectura para PS4.** *Objetivo:* redactar un registro de decisión. *Entradas:* §26.6. *Pasos:* redacte el ADR con contexto, opciones, decisión, consecuencias y condiciones de revisión. *Evidencia esperada:* ADR. *Rúbrica:* 3 = decisión justificada por la criticidad de PS4 y por la rareza de los cambios de consigna (C3, o C2 con escrituras de consigna solo locales, defendida), consecuencias que incluyen el costo operativo, desencadenantes de revisión; 2 = consecuencias débiles; 1 = sin opciones; 0 = nada.

### Síntesis del capítulo

Elija la arquitectura según cómo falla y cómo puede atacarse. El control jerárquico con límites seguros locales combina la operabilidad con la degradación suave. La redundancia protege frente a las fallas independientes, la diversidad frente a las causas comunes; los flujos unidireccionales eliminan los caminos de ataque entrantes junto con el control remoto. Cuantifique donde pueda y documente el riesgo residual que acepta.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Siga estudiando — capítulo 26 de 50

[← Capítulo 25](#ch-25) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 27 →](../../en/book/MANUSCRIPT.md#ch-27)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Cada resultado muestra una respuesta defendible. Los resultados numéricos se obtuvieron ejecutando los laboratorios y los scripts breves descritos, con Python 3 y las semillas indicadas; sus últimos dígitos pueden diferir si cambia el orden de los sorteos aleatorios. En los ejercicios de diseño, la rúbrica del capítulo importa más que coincidir con la redacción que sigue.

### Capítulo 1

**EX001.** $d'(t) = 60\cdot\frac{2\pi}{24}\cos(2\pi t/24) \approx 15.71\cos(2\pi t/24)$ m³/h². Máximo de 15,71 m³/h² en $t = 0$ (06:00) y de nuevo cada 24 h. Como 15,71 > 12, las bombas no pueden seguir la demanda en todo momento: $d'(t) > 12$ cuando $|t| < 2.68$ h, es decir, aproximadamente entre las 03:20 y las 08:40 de cada día. El almacenamiento debe cubrir el déficit durante la rampa de la mañana, que es una de las razones por las que existen los depósitos.

**EX002.** Interrupción a las 06:00: 14,62 h. Interrupción a las 18:00: 18,62 h. Estimación por demanda media: 17,33 h. El plan de emergencia debe citar la peor hora de inicio creíble (≈ 14,6 h, o menos si un nivel inicial más bajo es creíble), porque el plan debe funcionar sea cual sea el momento en que empiece la interrupción; la cifra de demanda media no es ni el peor caso ni el caso típico.

### Capítulo 2

**EX003.** $\neg\text{RUN} = H \vee S \vee (\neg P \wedge \neg M)$. Un permiso falsificado cambia el resultado solo en los estados con $H = 0$, $S = 0$, $M = 0$ (donde RUN sería falso de otro modo): un estado de 16. Una propuesta: exigir para el arranque remoto tanto $P$ como una segunda condición que no recorra el mismo camino de red; por ejemplo, un interruptor de llave local de «remoto habilitado» $K$: $\text{RUN} = \neg H \wedge \neg S \wedge ((P \wedge K) \vee M)$. El personal del sitio acciona el interruptor de llave para la operación remota planificada.

**EX004.** Con RTU4 pasada solo a `sat` (y `sat` sin depender de nada), la pérdida de `grid_f1` afecta a `fenwick_wtw, hollin_res, hospital_supply, lte, ps3, ps3_feed, rtu3`; `ps4` y `rtu4` sobreviven. Pero el grafo del laboratorio sigue marcando `hospital_supply` como afectado, porque sus aristas son dependencias de tipo Y: el suministro «necesita» tanto el depósito como PS4. La lógica real es O (cualquiera de los dos caminos basta), algo que este grafo simple no puede expresar; el capítulo 22 añade tipos Y/O. Un modelado mejor de la tarea (RTU4 necesita LTE *o* satélite) también requiere semántica O. Respuesta honesta: probablemente el hospital sobrevive a la pérdida de F1 gracias a PS4, pero este modelo no puede mostrarlo.

### Capítulo 3

**EX005.** Energía diaria: 26 W × 24 h + 15 W × 10 h = 774 Wh en la carga. Divida por la eficiencia 0,85, la fracción utilizable 0,6 y el factor de fin de vida 0,8: 774 / (0,85 × 0,6 × 0,8) ≈ 1.897 Wh nominales, ≈ 79 Ah a 24 V. Se necesita un banco estándar de 80 Ah o mayor; el banco de 65 Ah de §3.5 ya no cumple R5 en invierno.

**EX006.** Respuesta modelo: «El cifrado LTE protege la confidencialidad y, según la configuración, la integridad del tráfico en el tramo de radio; no hace nada por la disponibilidad. Un inhibidor de señal o una caída del operador reducen la relación señal/ruido por debajo de lo que el enlace necesita, y ninguna clave lo impide. Además, el cifrado termina en el operador, de modo que no autentica nuestras RTU ante nuestro SCADA de extremo a extremo. Para la disponibilidad: (1) diseñar los sitios para que funcionen en modo automático local durante 72 h sin telemetría y alarmar la pérdida de enlace en el SCADA en menos de 60 s; (2) ofrecer un camino diverso (un segundo operador con otras torres y otra alimentación, o satélite) para los sitios más críticos; (3) monitorear la calidad del enlace para distinguir una inhibición de señal de una caída.»

### Capítulo 4

**EX007.** `01 06 00 01 00 03` → bytes de CRC `98 0B` (trama `01 06 00 01 00 03 98 0b`). Cambiar el último byte de datos a `02` da `59 CB`. Un atacante en la línea serie calcula el CRC de una trama falsificada exactamente igual que el maestro legítimo, porque el algoritmo no tiene ningún secreto; el CRC solo detecta la corrupción accidental.

**EX008.** Mueva `len(resp) < 5` y una comprobación de longitud completa (`len(resp) == 5 + 2*count` para respuestas normales, 5 para excepciones) antes del CRC; después, el CRC; después, `if resp[0] == 0: return "reject: broadcast"` y la comprobación de unidad; después, función y número de bytes; y, por último, el rango. Pruebas: trama truncada → "reject: shape"; trama con unidad 0 y CRC válido → "reject: broadcast". Todos los casos originales siguen generando un rechazo. (Las peticiones de difusión no reciben respuesta en Modbus; una respuesta de la unidad 0 está malformada.)

### Capítulo 5

**EX009.** Ejemplo: «R10 — El sistema deberá mantener el suministro de agua tratada a St Brenna's dentro de la presión contractual durante la pérdida de cualquier estación de bombeo individual durante al menos 24 h (análisis + ensayo)». «R7 — Las alarmas prioritarias deberán mostrarse en las pantallas de los operadores en menos de 60 s desde el evento de campo para el 99 % de los eventos, en una medición de 30 días (prueba)». «R8 — Los registros de seguridad deberán reenviarse fuera del equipo en menos de 5 min y protegerse en su integridad con anclas diarias guardadas fuera de la zona de control; la modificación de cualquier registro almacenado deberá poder detectarse (prueba)».

**EX010.** Operador: «La telemetría de PS4 puede quedarse a oscuras tras unas 6 h sin red eléctrica. Si se pierde la telemetría de PS4 durante un corte de energía, envíe al técnico de guardia a leer los manómetros locales al cumplirse las 4 h». Directivo: «La batería de telemetría de PS4 dura unas 6 h al fin de vida frente a un requisito de 24 h (R5). Durante un corte largo perderíamos la visibilidad, no el suministro, en la alimentación del hospital. Opciones: sustituirla por un banco de 80 Ah (≈ costo de una visita al sitio más el equipo, dos semanas) o añadir una toma para un pequeño generador; medida provisional: regla de envío del técnico». Regulador: «Brecha: R5 (24 h de autonomía de la telemetría) no se cumple en PS4 (6 h medidas al fin de vida). Procedimiento compensatorio vigente desde [fecha]; corrección prevista para [fecha]».

### Capítulo 6

**EX011.** Con $k = 0.12$ h⁻¹: ventana = ln 4 / 0,12 ≈ 11,6 h. Con 4 h para el restablecimiento manual, la alarma debe llegar en menos de ≈ 7,6 h; con un margen de seguridad, especifique mucho menos. Requisito: «La pérdida de la dosificación de cloro deberá alarmarse en la sala de control en menos de 30 min, detectada por un analizador y un registrador independientes del controlador de dosificación». Los 30 min dejan un margen amplio incluso con el decaimiento del peor caso en tiempo cálido.

**EX012.** Exacta: 0,6065; 0,3679; 0,2231; 0,1353; 0,0821 en t = 1…5. Euler h = 1: 0,5; 0,25; 0,125; 0,0625; 0,0312 (estable, subestima). h = 3 (factor −0,5): −0,5; 0,25; −0,125; 0,0625; −0,0312: oscila de signo, físicamente sin sentido aunque decae. h = 5 (factor −1,5): −1,5; 2,25; −3,375; 5,06; −7,59: inestable. Euler explícito sobre $x' = -kx$ multiplica por $(1 - kh)$ en cada paso; $|1 - kh| > 1$ cuando $h > 2/k = 4$.

### Capítulo 7

**EX013.** VPP: 0,009 (previa 0,0001), 0,087 (0,001), 0,490 (0,01); con previa 0,001 y TFP 0,001: 0,487. Reducir diez veces la tasa de falsos positivos mejora el valor predictivo aproximadamente tanto como multiplicar por diez la prevalencia; con tasas base bajas, la TFP es el parámetro que vale la pena mejorar.

**EX014.** Indisponibilidad: β = 0 → 0,0004; β = 0,05 → 0,00136; β = 0,2 → 0,00426. Causas compartidas: energía y batería del sitio; mástil de antena o gabinete; mismo modelo de módem y mismo firmware; red de retorno compartida o acuerdos de itinerancia entre operadores; misma plataforma de aprovisionamiento de SIM.

### Capítulo 8

**EX015.** Peor caso: la señal de aspiración baja aparece justo después de una lectura de entradas, así que se ve por primera vez en el barrido siguiente (hasta 45 ms después); la confirmación requiere un segundo barrido consecutivo (45 ms); la salida se escribe al final de ese barrido. Peor caso ≈ 45 + 45 + 45 = 135 ms (más el retardo del módulo de salida), lo que incumple los 100 ms. Corrección: reducir el barrido de peor caso, filtrar los rebotes con un temporizador en una tarea más rápida o usar un disparo cableado.

**EX016.** El arranque seguro impide: (1) la instalación persistente de firmware sin firmar o modificado; (2) arrancar una imagen degradada a una versión anterior, si se aplica la protección contra reversión. No impide: (1) la explotación en tiempo de ejecución de una vulnerabilidad del firmware firmado → parches, validación de entradas, restricción de red; (2) cambios de lógica maliciosos pero legítimos a través de la interfaz de ingeniería → programación autenticada y basada en roles, con detección de cambios y registro.

### Capítulo 9

**EX017.** 5 estados × 7 eventos = 35 pares. Enumerados: stopped+start, starting+run_confirmed, starting+timeout, running+stop, stopping+stop_confirmed, tripped+reset (6), más `trip` desde los 5 estados (5) = 11. No enumerados: 24. Ejemplos con justificación: tripped+start (volver a arrancar en la falla; debe exigir un reinicio local); stopped+run_confirmed (una confirmación espuria o falsificada no debe crear la creencia de que la bomba está «en marcha»); running+reset (el reinicio no debe borrar un disparo inexistente y enmascarar el estado).

**EX018.** Invariante: para cada estación, `last[st]` nunca disminuye y es igual al mayor contador aceptado. Secuencia 1, 2, 2, 1, 5 → aceptar, aceptar, rechazar (repetición), rechazar (repetición), aceptar; estado final `last[3] == 5`. Tras reiniciar el receptor, `last` está vacío, así que los mensajes ya vistos vuelven a aceptarse salvo que el receptor persista `last` o que las claves se roten al reiniciar.

### Capítulo 10

**EX019.** Peligro: un operador bloqueado durante una emergencia no puede actuar; un atacante puede bloquear deliberadamente a los operadores (denegación de servicio). Alternativa: sin bloqueo en las HMI de la sala de control; en su lugar, retardo progresivo tras los fallos, alertas ante fallos repetidos, cuentas nominativas con autenticación fuerte, control de acceso físico a la sala de control y una anulación de emergencia con presencia física y registro. Verifique mediante prueba (los intentos fallidos producen retardos y alertas, nunca bloqueo) y mediante ejercicio (el operador puede iniciar sesión bajo estrés).

**EX020.** No visite, sondee ni intente iniciar sesión en la página, y no comparta la captura de pantalla. Notifique a la empresa de servicios en privado a través de su contacto de seguridad publicado o, si no existe, mediante un programa de divulgación coordinada como el de CISA, indicando solo lo que observó y dónde. El trabajo del curso puede describir el patrón («interfaces de gestión expuestas en documentos de compra») sin nombrar a la empresa, el proveedor, el modelo ni la ubicación.

### Capítulo 11

**EX021.** El nuevo flujo field → enterprise por TCP/445 es una VIOLATION. Modele el servidor de salto: añada la regla ("control", "field", "tcp", 22); entonces eng `10.5.0.12` → servidor de salto `10.1.0.20` por TCP/22 queda permitido; servidor de salto → RTU `10.2.0.33` por TCP/22, permitido; el acceso directo eng → RTU por TCP/22 sigue siendo una VIOLATION. Ninguna regla da a la zona de ingeniería acceso directo al campo.

**EX022.** Típico: 120 + 180 + hasta 1.300 + 200 ≈ 1,8 s si un evento llega justo después de su sondeo (≈ 1,15 s de media con una espera de medio ciclo). Peor caso: 120 + 900 + 1.300 + 200 ≈ 2,5 s. La cláusula del 95 % en menos de 1,5 s está en riesgo porque domina la espera de sondeo; la cláusula de 5 s se cumple. Cambio: informe por excepción (respuestas no solicitadas) para las alarmas, de modo que no esperen al sondeo.

### Capítulo 12

**EX023.** U = 2/10 + 4/40 + 10/100 = 0,40. Cota para n = 3: 3(2^{1/3} − 1) ≈ 0,780. U ≤ cota, así que el conjunto es planificable con prioridades monótonas en la tasa. La prueba es suficiente, no necesaria: un conjunto que supere la cota podría seguir siendo planificable (lo decidiría un análisis exacto del tiempo de respuesta).

**EX024.** Mitigar ahora: deshabilitar el servicio para compartir archivos en el historiador si no se necesita, o restringirlo a un único equipo de ingeniería identificado; monitorear los intentos de conexión; aplicar el parche tras la certificación del proveedor en la siguiente ventana de mantenimiento; fecha de revisión: certificación + 14 días. Aceptar sin hacer nada ignora el camino alcanzable desde la zona de ingeniería.

### Capítulo 13

**EX025.** `chain(recs[:5])[-1] == anchor[4]` → True: un atacante que elimine el último registro y sustituya la cabeza guardada por `anchor[4]` pasa desapercibido. Incluir el recuento, ancla = H(cabeza ‖ n), hace detectable el truncamiento (verificado: el ancla truncada difiere). Guarde el ancla en el sistema de tickets de incidentes y en un archivo de una sola escritura, fuera de la zona de control y fuera de los privilegios de los administradores del historiador.

**EX026.** El historiador de control envía los datos horarios de energía y los valores de presión en vivo a una réplica en la DMZ (solo de salida, impuesto por un cortafuegos o por una pasarela unidireccional); finanzas y el tablero consultan la réplica. Ninguna conexión entrante hacia la zona de control. Si se compromete la réplica, los atacantes pueden leer o falsificar los datos de informes y los tableros (un problema de integridad y confidencialidad de los datos), pero no obtienen ningún camino hacia el control.

### Capítulo 14

**EX027.** Lista de comprobación: longitud de la entrada comprobada antes de indexar; integridad comprobada antes del uso; comparación de secretos en tiempo constante; ningún secreto en el código fuente; los caminos de error rechazan; las excepciones no se silencian; límites en bucles y tamaños; registro de los rechazos sin secretos; orden de bytes explícito; pruebas para cada camino de rechazo. Hallazgos: Lab 3: las tramas truncadas informan «crc» en lugar de la forma (claridad del diagnóstico); Lab 8: clave escrita en el código fuente (aceptable solo como demostración etiquetada).

**EX028.** Haga coincidir el aviso con las entradas y versiones de la SBOM; confirme que la función o característica vulnerable está presente y es alcanzable en la configuración de RTU-B (p. ej., ¿está habilitado el servidor TLS?, ¿se usa el analizador vulnerable de la biblioteca?); pida al proveedor una evaluación y un firmware corregido; aplique controles compensatorios (restringir el conducto, deshabilitar la característica); comunique a operaciones; programe la actualización mediante despliegue por etapas; registre la decisión.

### Capítulo 15

**EX029.** Lab 8: aplica el diseño abierto (la seguridad descansa en la clave, no en el secreto del algoritmo) y la mediación completa (se comprueba cada mensaje); infringe el mínimo privilegio y la separación en cuanto a que la clave de demostración está en el código fuente y se comparte entre estaciones; corrección: claves por estación desde un almacenamiento protegido. Máquina de estados (§9.5): aplica valores predeterminados a prueba de fallos (se rechazan los eventos no enumerados) y separación de privilegios (el reinicio necesita un operador local); no abordado: la economía de mecanismo si se implementa con indicadores dispersos; corrección: implementación dirigida por tabla.

**EX030.** Consecuencia 1: hospital sin agua > 4 h; funciones usadas indebidamente: arranque y parada de bombas en PS3/PS4, posiciones de válvulas; límite diseñado: almacenamiento propio del hospital más una lógica local de rearranque automático que una orden remota no puede deshabilitar. Consecuencia 2: sobredosis de cloro; funciones: consigna de dosificación y velocidad de la bomba; límite diseñado: bomba dosificadora dimensionada físicamente de modo que la carrera máxima con el caudal máximo no pueda superar una concentración dañina, más un disparo cableado por residual alto.

### Capítulo 16

**EX031.** Un mapeo posible: N1 ← R3, R4, R5 (en parte), R9; N2 ← R1, R2, R3, R7, R8; N3 ← R6, R8; N4 ← R5, R7. N3 y N4 empatan con el menor número (dos cada una); la propuesta refuerza N3: «R10 — Se deberán hacer semanalmente copias de seguridad fuera de línea de las configuraciones del SCADA y de los controladores, guardadas fuera de los dominios de control y corporativo, con pruebas de restauración trimestrales».

**EX032.** Elementos de datos (ID de estación, contador, nivel, presión, alarmas); codificación (binaria, *big-endian*, trama de 28 bytes más ID de la suite); frecuencia (1 cada 10 s por estación, más alarmas por excepción); latencia (≤ 1 s en la pasarela); autenticación (HMAC-SHA256-128, clave por estación); manejo de errores (rechazar y registrar; alarma tras 3 rechazos en 10 min; alarma de estación sin datos a los 60 s); fuente de tiempo (NTP interno a través de un conducto permitido; marcas de tiempo en UTC); responsabilidad (pasarela: ingeniería del TMRP; lado SCADA: operaciones); proceso de cambio (revisión del ICD bajo control de configuración con la aprobación de ambos responsables).

### Capítulo 17

**EX033.** Semilla 17, ruido σ = 0,01 m, 48 h: umbral de 0,03 m → 2 episodios de falsa alarma sin ataque (≈ 1 por día), primera alarma de la rampa de 0,05 m/h a las 10,7 h; umbral de 0,05 m → 0 episodios de falsa alarma, primera alarma de la rampa a las 10,9 h. Recomendación: 0,05 m; el retardo de detección de 0,2 h es pequeño frente a horas de autonomía, mientras que las falsas alarmas diarias enseñarían a los operadores a ignorar el detector. Vuelva a comprobarlo con datos de ruido reales.

**EX034.** Comprometer la RTU3 permite a un atacante falsificar tanto el nivel como el caudal de entrada, de modo que puede hacer coherente el balance de masa y el residuo sigue siendo pequeño; comprometer solo la RTU4 falsifica el caudal de salida y es detectable. Mejora: un transmisor de nivel independiente cableado a un registrador separado (otro controlador y otro camino de comunicaciones), o una lectura física periódica del indicador de nivel comparada con el SCADA.

### Capítulo 18

**EX035.** La regla no supera la prueba de la DMZ: un servidor ERP comprometido podría enviar paquetes directamente a la base de datos del SCADA. Alternativa: el ERP escribe el estado de las órdenes de trabajo en un servicio de la DMZ; un proceso de la zona de control recoge las actualizaciones (o las recibe a través de un intermediario con una validación estricta), validando el formato y el contenido; ninguna conexión entrante desde la empresa hacia el control.

**EX036.** Camino: proveedor → pasarela de acceso de la DMZ (MFA, cuentas nominativas del proveedor) → sesión aprobada en cada solicitud por el responsable de turno → servidor de salto en la zona de control → solo la interfaz de diagnóstico de RTU-B; sesión grabada; el acceso caduca al final de la ventana aprobada; la cuenta del proveedor se deshabilita entre sesiones. Evidencia: registros de la pasarela y del servidor de salto, sesiones grabadas, una prueba que muestre que la conexión directa del proveedor a las RTU está bloqueada y una revisión trimestral de las cuentas.

### Capítulo 19

**EX037.** Si la RTU persiste su contador cada 1.000 incrementos y se reinicia, el último valor persistido puede ir hasta 999 por detrás del último valor usado. Para no reutilizar un contador (que el receptor rechazaría, o que podría permitir una repetición tras un reinicio del receptor), la RTU salta hacia delante al menos 1.000 más allá del valor persistido. El receptor debe persistir el último contador aceptado por estación, o ambos lados deben rotar las claves tras el reinicio.

**EX038.** A (clave de flota): una RTU robada permite al ladrón falsificar mensajes de las 42 estaciones; la recuperación exige cambiar las claves de todas las estaciones. B (claves por estación): la falsificación se limita a la estación robada; se revoca y sustituye una sola clave. Almacenar 42 claves en un HSM es trivial para el SCADA. Recomendación: B.

### Capítulo 20

**EX039.** Se evalúa con la rúbrica; por ejemplo, distribución eléctrica: unidades de consecuencia: clientes interrumpidos × horas, MW no suministrados, clientes críticos afectados; tecnologías: relés de protección, sistemas de gestión de la distribución, RTU de subestaciones; regulaciones: normas NERC CIP (cite versión y fecha) y NIS2 (2022/2555) para los operadores de la UE; incidente: Ucrania 2015, descrito a partir de CISA IR-ALERT-H-16-056-01.

**EX040.** Modelo: un único producto de seguridad con acceso privilegiado al núcleo estaba instalado en muchas organizaciones de distintos sectores y se actualizaba automáticamente; una actualización de contenido defectuosa hizo fallar a la vez los equipos Windows, y Microsoft estimó que resultaron afectados unos 8,5 millones de dispositivos. La propiedad es una causa común a través de una dependencia compartida, privilegiada y actualizada automáticamente. Práctica: despliegues por etapas (canario) de las actualizaciones, por parte de los proveedores y, cuando sea posible, controlados por los clientes en los sistemas críticos, más procedimientos de recuperación que no dependan de los equipos afectados. No fue un ataque.

### Capítulo 21

**EX041.** Continuidad del servicio: «Ante la pérdida del SCADA, PS3 y PS4 deberán continuar en control automático local y los operadores deberán poder operarlas localmente en menos de 1 h (ejercicio)». Contención: «Ante una sospecha de compromiso del SCADA, los caminos de órdenes remotas hacia todas las estaciones deberán deshabilitarse desde las pasarelas en menos de 15 min desde la decisión (prueba)». Restauración: «La operación remota deberá restaurarse a partir de copias de seguridad fuera de línea verificadas en menos de 8 h desde la decisión de restaurar (ensayo)».

**EX042.** Conflicto: acceso continuo del operador frente a reautenticación a los 15 min. Opciones: (a) mantener la reautenticación; (b) sin reautenticación; (c) la pantalla de solo visualización sigue activa; las acciones de control exigen una reautenticación rápida (acercar la credencial o PIN) tras 15 min de inactividad, con la sala de control bajo control de acceso físico. Recomendación: (c). Responsable: el gerente de operaciones (dueño del riesgo) junto con el responsable de seguridad.

### Capítulo 22

**EX043.** Con PS4 necesitando solo `grid_f2` en modo automático local (sin LTE para el suministro) y el suministro como O: `{grid_f1}` → el suministro funciona (gracias a PS4); `{ps4}` → funciona (gracias al depósito); `{ps4, grid_f1}` → falla. Un modelo que hace depender el suministro de la telemetría falla erróneamente en el primer caso.

**EX044.** Estados: automático remoto, automático local, manual local, degradada (una bomba), disparada, fuera de servicio. Camino de ataque: órdenes de parada falsificadas y arranques y paradas repetidos (automático remoto → disparada por la protección del arrancador) → si el rearme tras el disparo es remoto, el atacante mantiene la estación disparada → fuera de servicio. Control: el rearme tras el disparo exige una acción local; órdenes autenticadas; limitación de la frecuencia de las órdenes de arranque.

### Capítulo 23

**EX045.** PS3 = PS4 = 1: superior = P(TANK) = 0,03. G1 = G2 = 1: el camino B se pierde; el camino A se pierde si falla PS4 o GEN: 1 − 0,98 × 0,95 = 0,069; superior = 0,03 × 0,069 = 0,00207. Interpretación: la autenticación de las órdenes remotas elimina el camino más barato para el adversario (el evento superior baja de 0,03 a 9,1 × 10⁻⁵); si un adversario puede cortar ambos alimentadores, el generador y el tanque del hospital se convierten en las barreras decisivas: hay que mantenerlos y probarlos.

**EX046.** Suplantación: tramas falsificadas (ATT&CK for ICS: Spoof Reporting Message) → MAC por estación. Manipulación: valores modificados en tránsito → MAC. Repudio: disputas sobre las órdenes → registros firmados o con MAC y anclas. Divulgación de información: telemetría leída en la red del operador → cifrado del operador más cifrado opcional de la carga útil. Denegación de servicio: inhibición de señal o inundación (Denial of Service; Block Reporting Message) → recurso al automático local, alarma de estación sin datos, limitación de frecuencia. Elevación de privilegios: compromiso de la pasarela para emitir órdenes → endurecimiento de la pasarela, filtrado de códigos de función, límites locales.

### Capítulo 24

**EX047.** (a) Simulación hidráulica más STPA del camino de la consigna; límite: fidelidad del modelo para los transitorios. (b) Experimento en banco de pruebas con inundaciones etiquetadas; límite: el tráfico de laboratorio difiere del del sitio. (c) Ejercicio funcional nocturno; límite: una sola ocasión, efecto del observador. (d) Evaluación de riesgos estructurada con escalas definidas; límite: estimaciones, no mediciones.

**EX048.** Verificación: comparar Euler con la integral exacta (Lab 1); pruebas unitarias de `demand` y `drawn`; casos extremos (demanda cero → autonomía infinita; demanda constante → V/q). Validación: comparar la caída de nivel predicha con los datos del historiador de una parada planificada de bombas; validez aparente de la curva de demanda ante los operadores; sensibilidad a la amplitud de la demanda. Uso previsto: estimación de la autonomía para la planificación. No válido para los transitorios de presión, la calidad del agua ni la hidráulica de la red.

### Capítulo 25

**EX049.** Pesos (0,40; 0,20; 0,10; 0,15; 0,15): A 2,80; B 3,35; C 4,20; D 4,45: D supera a C. Pesos (0,20; 0,20; 0,30; 0,15; 0,15): A 3,60; B 3,35; C 4,20; D 3,65. La ventaja de C depende de que la operabilidad tenga un peso real; si quienes deciden valoran la prevención de órdenes falsificadas muy por encima de la operabilidad, D gana sobre el papel, pero en la práctica D incumple de noche la necesidad del hospital, lo que sugiere que la operabilidad se expresa mejor como restricción que como peso.

**EX050.** Pasarela como punto único de falla: aceptar; la falla de la pasarela debe llevar al automático local con alarma; añadir una pasarela de reserva en frío por región. Elusión mediante el modo manual: aceptar; interruptor de llave en el panel, alarma en el SCADA ante el cambio de modo, registro local. Personal para la gestión de claves: aceptar; añadir al caso de negocio 0,2 ETC de costo operativo y el mantenimiento del HSM; responsable: el gerente del TMRP.

### Capítulo 26

**EX051.** La mediana de tres tolera un transmisor falsificado o averiado. Un atacante que controle la RTU que lee los tres puede falsificarlos todos de forma coherente y anular la votación. Restablezca la independencia cableando los transmisores a módulos de E/S o controladores separados, con comunicaciones separadas, de modo que ningún compromiso individual controle dos de las tres entradas.

**EX052.** ADR modelo: contexto: PS4 es la alimentación directa del hospital y sus consignas cambian aproximadamente una vez al mes; opciones: C2 (remoto dentro de límites) o C3/variante de C2 (escrituras de consigna solo locales, monitoreo remoto); decisión: escrituras de consigna solo locales en PS4, manteniendo el arranque y la parada remotos con autenticación; consecuencias: visita mensual al sitio para los cambios de consigna, procedimientos de respuesta local más rápidos, riesgo residual D1 en PS4 reducido al arranque y la parada; revisar si aumenta la frecuencia de los cambios de consigna o cambia la dotación de personal.

<a id="glossary"></a>

## Glosario

- **Lista de permitidos (*allowlist*)**: política que permite solo los flujos, programas o valores enumerados; todo lo demás se deniega.
- **Ancla**: copia de confianza de la cabeza de una cadena de hashes (con el número de registros), guardada fuera del alcance del atacante.
- **Caso de aseguramiento**: argumento estructurado de que un sistema cumple una afirmación, que vincula subafirmaciones con evidencia, con calificadores y refutadores.
- **Disponibilidad**: fracción del tiempo en que un sistema puede cumplir su función; MTBF/(MTBF + MTTR) para una unidad reparable simple.
- **Tasa base**: prevalencia del evento de interés; decisiva para el valor predictivo de una alarma.
- **Factor beta**: fracción de la indisponibilidad de una unidad atribuida a causas comunes que inutilizan a la vez las unidades redundantes.
- **Conducto**: camino de comunicación controlado entre zonas (vocabulario de IEC 62443).
- **Ruta crítica**: la cadena más larga de tareas dependientes; fija el tiempo mínimo de finalización.
- **Refutador**: condición en la que la conclusión de un argumento no se sostendría.
- **DMZ**: zona intermedia a través de la cual se intermedia todo el tráfico entre las redes de control y las corporativas.
- **Inyección de fallas**: introducción deliberada de fallas para probar el manejo de errores.
- **HMAC**: código de autenticación de mensajes con clave construido a partir de una función de hash (FIPS 198-1).
- **Autonomía local**: capacidad de un sitio para seguir operando de forma segura sin el centro ni la red.
- **Conjunto de corte mínimo**: conjunto más pequeño de eventos básicos cuya ocurrencia conjunta provoca el evento superior de un árbol de fallas.
- **PLC / RTU**: controlador lógico programable (control local basado en ciclos de barrido) / unidad terminal remota (adquisición de datos y control remotos a través de enlaces largos).
- **Precisión / exhaustividad**: proporción de alarmas que son reales / proporción de eventos reales que generan alarma.
- **Prueba basada en propiedades**: prueba que comprueba una propiedad enunciada sobre muchas entradas generadas, incluidos valores especiales.
- **Residuo**: diferencia entre una medición y la predicción de un modelo independiente.
- **Riesgo residual**: riesgo que queda después de los controles; debe tener un responsable.
- **Arranque seguro**: verificación de las firmas del firmware desde una raíz de confianza inmutable antes de su ejecución.
- **STPA**: System-Theoretic Process Analysis (análisis de procesos basado en la teoría de sistemas); encuentra acciones de control inseguras y sus escenarios causales.
- **Constante de tiempo**: en los sistemas de primer orden, el tiempo necesario para cerrar alrededor del 63 % de la brecha hasta el equilibrio.
- **Trazabilidad**: vínculos desde las necesidades hasta los requisitos, el diseño, las pruebas y los resultados.
- **Acción de control insegura**: acción de control que, en un contexto determinado, conduce a un peligro.
- **Validación / verificación**: sistema adecuado para la necesidad / sistema construido según su especificación.
- **Zona**: agrupación de activos con requisitos de seguridad comunes.

<a id="references"></a>

## Referencias

Las leyes, las normas, las orientaciones y las páginas sobre incidentes cambian. Las versiones y fechas que siguen son las consultadas para este borrador (octubre de 2026); vuelva a verificarlas antes de basarse en ellas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

**Política, derecho, normas y marcos**

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Cybersecurity and Infrastructure Security Agency. [ICS Advisories](https://www.cisa.gov/news-events/ics-advisories).
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- International Electrotechnical Commission. [IEC 62443-3-2:2020 — Security risk assessment for system design (catalogue page)](https://webstore.iec.ch/en/publication/30727).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- MITRE. [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/).
- Modbus Organization. [Modbus Application Protocol Specification](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf).
- NASA. [NASA Systems Engineering Handbook (SP-2016-6105 Rev. 2)](https://www.nasa.gov/reference/systems-engineering-handbook/).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework). February 2024.
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final). September 2012.
- National Institute of Standards and Technology. [SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final).
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025.
- National Institute of Standards and Technology. [SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final). September 2023.
- National Institute of Standards and Technology. [SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final). November 2022.
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST, December 2021.
- National Institute of Standards and Technology. [SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final). August 2020.
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final). February 2022.
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final); [FIPS 197, Advanced Encryption Standard](https://csrc.nist.gov/pubs/fips/197/final); [FIPS 198-1, The Keyed-Hash Message Authentication Code (HMAC)](https://csrc.nist.gov/pubs/fips/198-1/final).
- National Institute of Standards and Technology. [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). 13 August 2024.
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- Open Source Security Foundation. [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/).
- Reproducible Builds project. [Reproducible Builds](https://reproducible-builds.org/).
- Rescorla, E. [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446). IETF, August 2018.
- Eddy, W. (ed.). [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293). IETF, August 2022.
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, February 1997.
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).

**Ética profesional**

- Association for Computing Machinery. [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics). 2018.
- National Society of Professional Engineers. [NSPE Code of Ethics for Engineers](https://www.nspe.org/resources/ethics/code-ethics).

**Incidentes y evidencia sectorial**

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Cybersecurity and Infrastructure Security Agency. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf). 2019.
- E-ISAC and SANS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). March 2016 (archived copy).
- Langner, R. [Stuxnet: Dissecting a Cyberwarfare Weapon](https://doi.org/10.1109/MSP.2011.67). *IEEE Security & Privacy*, 9(3), 49–51, 2011.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems*, 21(6), 11–25, 2001.
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

**Computación, seguridad y confiabilidad**

- Avizienis, A., Laprie, J.-C., Randell, B., and Landwehr, C. [Basic Concepts and Taxonomy of Dependable and Secure Computing](https://doi.org/10.1109/TDSC.2004.2). *IEEE Transactions on Dependable and Secure Computing*, 1(1), 11–33, 2004.
- Brooks, F. P. [No Silver Bullet: Essence and Accidents of Software Engineering](https://doi.org/10.1109/MC.1987.1663532). *Computer*, 20(4), 10–19, 1987.
- Codd, E. F. [A Relational Model of Data for Large Shared Data Banks](https://doi.org/10.1145/362384.362685). *Communications of the ACM*, 13(6), 377–387, 1970.
- Diffie, W., and Hellman, M. [New Directions in Cryptography](https://doi.org/10.1109/TIT.1976.1055638). *IEEE Transactions on Information Theory*, 22(6), 644–654, 1976.
- Fagan, M. E. [Design and Code Inspections to Reduce Errors in Program Development](https://doi.org/10.1147/sj.153.0182). *IBM Systems Journal*, 15(3), 182–211, 1976.
- Kim, Y., Daly, R., Kim, J., et al. [Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors](https://doi.org/10.1109/ISCA.2014.6853210). *ISCA*, 2014.
- Kocher, P., Horn, J., Fogh, A., et al. [Spectre Attacks: Exploiting Speculative Execution](https://doi.org/10.1109/SP.2019.00002). *IEEE Symposium on Security and Privacy*, 2019.
- Liu, C. L., and Layland, J. W. [Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment](https://doi.org/10.1145/321738.321743). *Journal of the ACM*, 20(1), 46–61, 1973.
- McCabe, T. J. [A Complexity Measure](https://doi.org/10.1109/TSE.1976.233837). *IEEE Transactions on Software Engineering*, SE-2(4), 308–320, 1976.
- Parnas, D. L. [On the Criteria to Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623). *Communications of the ACM*, 15(12), 1053–1058, 1972.
- Rivest, R. L., Shamir, A., and Adleman, L. [A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](https://doi.org/10.1145/359340.359342). *Communications of the ACM*, 21(2), 120–126, 1978.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.
- Shannon, C. E. [A Mathematical Theory of Communication](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). *Bell System Technical Journal*, 27(3), 379–423, 1948.

**Control, seguridad funcional, confiabilidad y resiliencia**

- Åström, K. J., and Murray, R. M. [Feedback Systems: An Introduction for Scientists and Engineers](https://fbswiki.org/wiki/index.php/Main_Page). Princeton University Press; free online edition.
- Bruneau, M., Chang, S. E., Eguchi, R. T., et al. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra*, 19(4), 733–752, 2003.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis*, 29(4), 498–501, 2009.
- Leveson, N. [A New Accident Model for Engineering Safer Systems](https://doi.org/10.1016/S0925-7535(03)00047-X). *Safety Science*, 42(4), 237–270, 2004.
- Little, J. D. C. [A Proof for the Queuing Formula: L = λW](https://doi.org/10.1287/opre.9.3.383). *Operations Research*, 9(3), 383–387, 1961.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320(7237), 768–770, 2000.
- Saltelli, A., Ratto, M., Andres, T., et al. [Global Sensitivity Analysis: The Primer](https://doi.org/10.1002/9780470725184). Wiley, 2008.

**Evaluación, investigación y argumentación**

- Arp, D., Quiring, E., Pendlebury, F., et al. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). *USENIX Security Symposium*, 2022.
- Goh, J., Adepu, S., Junejo, K. N., and Mathur, A. [A Dataset to Support Research in the Design of Secure Water Treatment Systems](https://doi.org/10.1007/978-3-319-71368-7_8). *Critical Information Infrastructures Security (CRITIS 2016)*, LNCS 10242, 88–99, 2017.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *AAAI*, 2022.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology*, 9(10), e1003285, 2013.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation*, 7(1), 12–24, 2013.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). *IEEE Symposium on Security and Privacy*, 2010.
- Taormina, R., Galelli, S., Tippenhauer, N. O., et al. [Battle of the Attack Detection Algorithms: Disclosing Cyber Attacks on Water Distribution Networks](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969). *Journal of Water Resources Planning and Management*, 144(8), 2018.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
