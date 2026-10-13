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
13. [Sistemas de datos](../../en/book/MANUSCRIPT.md#ch-13)
14. [Ingeniería de software](../../en/book/MANUSCRIPT.md#ch-14)
15. [Fundamentos de seguridad](../../en/book/MANUSCRIPT.md#ch-15)
16. [Ingeniería de sistemas](../../en/book/MANUSCRIPT.md#ch-16)
17. [Fundamentos de control y realimentación](../../en/book/MANUSCRIPT.md#ch-17)
18. [Arquitectura de seguridad](../../en/book/MANUSCRIPT.md#ch-18)
19. [Identidad y criptografía](../../en/book/MANUSCRIPT.md#ch-19)
20. [Infraestructura crítica y seguridad sectorial: contexto de ingeniería](../../en/book/MANUSCRIPT.md#ch-20)
21. [Infraestructura crítica y seguridad sectorial: requisitos](../../en/book/MANUSCRIPT.md#ch-21)
22. [Infraestructura crítica y seguridad sectorial: modelos de sistema y de datos](../../en/book/MANUSCRIPT.md#ch-22)
23. [Infraestructura crítica y seguridad sectorial: análisis de amenazas y fallas](../../en/book/MANUSCRIPT.md#ch-23)
24. [Infraestructura crítica y seguridad sectorial: métodos I](../../en/book/MANUSCRIPT.md#ch-24)
25. [Taller de diseño I](../../en/book/MANUSCRIPT.md#ch-25)
26. [Infraestructura crítica y seguridad sectorial: alternativas de arquitectura](../../en/book/MANUSCRIPT.md#ch-26)
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

[← Capítulo 11](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 →](../../en/book/MANUSCRIPT.md#ch-13)

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
