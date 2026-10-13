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
4. [Programación I](../../en/book/MANUSCRIPT.md#ch-04)
5. [Comunicación en ingeniería](../../en/book/MANUSCRIPT.md#ch-05)
6. [Cálculo II](../../en/book/MANUSCRIPT.md#ch-06)
7. [Probabilidad y estadística](../../en/book/MANUSCRIPT.md#ch-07)
8. [Arquitectura de computadoras](../../en/book/MANUSCRIPT.md#ch-08)
9. [Programación II](../../en/book/MANUSCRIPT.md#ch-09)
10. [Ética y seguridad en ingeniería](../../en/book/MANUSCRIPT.md#ch-10)
11. [Redes y protocolos](../../en/book/MANUSCRIPT.md#ch-11)
12. [Sistemas operativos](../../en/book/MANUSCRIPT.md#ch-12)
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

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](../../en/book/MANUSCRIPT.md#ch-04)

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
