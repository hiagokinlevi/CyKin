# Infraestructura crítica y seguridad sectorial: ingeniería de sistemas seguros y resilientes

- Idioma: español neutro (`es`); curso de ingeniería, cinco años; aproximadamente 4.000 horas de estudio planificado (curso 138 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **publicado**. Los capítulos 1–50 de 50 tienen texto didáctico escrito; los ejercicios EX001–EX100 (dos por capítulo) tienen sus resultados resueltos correspondientes; diecisiete laboratorios sin conexión están incluidos con su salida verificada. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La meta del plan de tres ejercicios por capítulo aún no se cumple. La cobertura de capítulos en borrador no es un libro terminado.
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
27. [Infraestructura crítica y seguridad sectorial: diseño de controles](#ch-27)
28. [Infraestructura crítica y seguridad sectorial: implementación I](#ch-28)
29. [Infraestructura crítica y seguridad sectorial: medición](#ch-29)
30. [Laboratorio de verificación I](#ch-30)
31. [Infraestructura crítica y seguridad sectorial: implementación II](#ch-31)
32. [Infraestructura crítica y seguridad sectorial: confiabilidad](#ch-32)
33. [Infraestructura crítica y seguridad sectorial: seguridad funcional y resiliencia](#ch-33)
34. [Infraestructura crítica y seguridad sectorial: integración](#ch-34)
35. [Taller de diseño II](#ch-35)
36. [Infraestructura crítica y seguridad sectorial: desempeño y escala](#ch-36)
37. [Infraestructura crítica y seguridad sectorial: operaciones](#ch-37)
38. [Infraestructura crítica y seguridad sectorial: validación](#ch-38)
39. [Infraestructura crítica y seguridad sectorial: mantenibilidad](#ch-39)
40. [Laboratorio de verificación II](#ch-40)
41. [Infraestructura crítica y seguridad sectorial: optimización del sistema](#ch-41)
42. [Infraestructura crítica y seguridad sectorial: investigación aplicada](#ch-42)
43. [Práctica en la industria o en el servicio público](#ch-43)
44. [Proyecto final de ingeniería I](#ch-44)
45. [Revisión independiente del diseño](#ch-45)
46. [Proyecto final de ingeniería II](#ch-46)
47. [Ensayo de falla y recuperación](#ch-47)
48. [Expediente de evidencia](#ch-48)
49. [Tesis de ingeniería](#ch-49)
50. [Defensa final](#ch-50)

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

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 50

[← Página del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 50

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 50

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 50

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](#ch-05)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Siga estudiando — capítulo 05 de 50

[← Capítulo 04](#ch-04) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 06 →](#ch-06)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Siga estudiando — capítulo 06 de 50

[← Capítulo 05](#ch-05) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 07 →](#ch-07)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Siga estudiando — capítulo 07 de 50

[← Capítulo 06](#ch-06) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 08 →](#ch-08)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Siga estudiando — capítulo 08 de 50

[← Capítulo 07](#ch-07) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 09 →](#ch-09)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Siga estudiando — capítulo 09 de 50

[← Capítulo 08](#ch-08) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 10 →](#ch-10)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Siga estudiando — capítulo 10 de 50

[← Capítulo 09](#ch-09) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 11 →](#ch-11)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Siga estudiando — capítulo 11 de 50

[← Capítulo 10](#ch-10) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 12 →](#ch-12)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Siga estudiando — capítulo 12 de 50

[← Capítulo 11](#ch-11) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 13 →](#ch-13)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Siga estudiando — capítulo 13 de 50

[← Capítulo 12](#ch-12) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 14 →](#ch-14)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Siga estudiando — capítulo 14 de 50

[← Capítulo 13](#ch-13) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 15 →](#ch-15)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Siga estudiando — capítulo 15 de 50

[← Capítulo 14](#ch-14) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 16 →](#ch-16)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Siga estudiando — capítulo 16 de 50

[← Capítulo 15](#ch-15) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 17 →](#ch-17)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Siga estudiando — capítulo 17 de 50

[← Capítulo 16](#ch-16) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 18 →](#ch-18)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Siga estudiando — capítulo 18 de 50

[← Capítulo 17](#ch-17) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 19 →](#ch-19)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Siga estudiando — capítulo 19 de 50

[← Capítulo 18](#ch-18) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 20 →](#ch-20)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Siga estudiando — capítulo 20 de 50

[← Capítulo 19](#ch-19) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 21 →](#ch-21)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-21 -->
### Siga estudiando — capítulo 21 de 50

[← Capítulo 20](#ch-20) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 22 →](#ch-22)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-22 -->
### Siga estudiando — capítulo 22 de 50

[← Capítulo 21](#ch-21) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 23 →](#ch-23)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-23 -->
### Siga estudiando — capítulo 23 de 50

[← Capítulo 22](#ch-22) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 24 →](#ch-24)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-24 -->
### Siga estudiando — capítulo 24 de 50

[← Capítulo 23](#ch-23) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 25 →](#ch-25)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-25 -->
### Siga estudiando — capítulo 25 de 50

[← Capítulo 24](#ch-24) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 26 →](#ch-26)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

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

<!-- open-cyber-academy:chapter-navigation:start ch-26 -->
### Siga estudiando — capítulo 26 de 50

[← Capítulo 25](#ch-25) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 27 →](#ch-27)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-27"></a>

## Capítulo 27 — Infraestructura crítica y seguridad sectorial: diseño de controles

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) diseñar controles que aborden escenarios concretos con un desempeño definido; (2) combinar controles preventivos, detectivos y de recuperación en una defensa en profundidad cuyas capas fallen de forma independiente; (3) preferir límites diseñados, basados en la física, para las peores consecuencias; y (4) especificar cada control de modo que pueda verificarse. Aplica los capítulos 15, 23 y 26 y prepara los capítulos 28 y 30.

### 27.1 Del escenario al control

Cada escenario del capítulo 23 recibe controles en tres puntos: **prevenir** el evento de amenaza, **detectarlo** si la prevención falla, y **limitar y recuperarse** de las consecuencias. Ejemplo, órdenes de parada falsificadas a PS3 y PS4: prevenir con órdenes autenticadas (R1); detectar con alarmas ante anomalías en las órdenes y cambios de estado inesperados; limitar con una lógica local de rearranque automático y con el tanque del hospital; recuperarse con procedimientos manuales locales (R4). Cada uno de estos controles debe especificarse y verificarse después, como muestra el resto del capítulo, antes de que el escenario de la parada falsificada pueda darse por cubierto en el expediente.

### 27.2 Primero, los límites diseñados

Para las peores consecuencias, los controles más robustos no dependen en absoluto del software: válvulas de alivio de presión, topes mecánicos, enclavamientos cableados, bombas dosificadoras de productos químicos dimensionadas físicamente para que no puedan sobredosificar con la carrera máxima. La ingeniería informada por lo cibernético (véase la [CCE del INL](https://inl.gov/national-security/cce/)) da importancia a estos controles porque se mantienen aunque se comprometan todos los sistemas digitales. No pueden cubrirlo todo (una válvula de alivio mecánica no puede impedir que se apague una bomba), pero acotan los peores casos.

Para la bomba dosificadora de LRWA, el límite de carrera dimensionado por los ingenieros de proceso es uno de estos controles.

### 27.3 Capas independientes

La defensa en profundidad solo funciona si las capas fallan de forma independiente. Enumere las dependencias de cada capa: si la autenticación, el monitoreo y el registro dependen todos de los servidores SCADA, un solo compromiso anula los tres. Ponga al menos una capa de detección fuera de los sistemas que vigila (monitoreo pasivo de la red, un analizador independiente) y mantenga los materiales de recuperación (copias fuera de línea, procedimientos, claves de repuesto) fuera del alcance de la amenaza de la que hay que recuperarse.

El TMRP aplica esto poniendo la alarma del analizador de cloro en un registrador separado y guardando las copias fuera de línea lejos de los servidores SCADA que restaurarían.

### 27.4 Especificar los controles

Una especificación de control indica: el escenario o escenarios que aborda; su función; su desempeño (detección en menos de X, tasa de rechazo, tiempo de restauración); sus dependencias; su modo de falla (a prueba de fallos o con operación mantenida, y qué significa eso aquí); su responsable; y su método de verificación. Sin desempeño ni verificación, un control es una intención. La especificación de los límites de consigna del ejemplo resuelto que sigue muestra todos los elementos: el escenario, los límites y el límite de escalón, la regla de alarma, las dependencias, la conservación de la última consigna válida como modo de falla y la prueba T3 como verificación. Su responsable es el equipo de ingeniería de control que configura el controlador de dosificación.

### 27.5 Ejemplo resuelto: límites de consigna (sintético)

Escenario: una consigna falsificada o errónea lleva la bomba dosificadora de cloro a sobredosificar. Controles: (1) **diseñado**: carrera de la bomba dosificadora limitada físicamente para que la dosis máxima con el caudal máximo quede por debajo de una concentración dañina (dimensionada por los ingenieros de proceso); (2) **preventivo**: límites y límites de escalón en el controlador (R3), implementados en el controlador y no en la HMI, para que un SCADA comprometido no pueda eludirlos; (3) **detectivo**: alarma de un analizador de cloro independiente (R9) en un registrador separado; (4) **de recuperación**: procedimiento para aislar la línea de dosificación y purgarla. Especificación de (2): rechazar las consignas fuera de 0,5–5,5 mg/L o que cambien más de 0,5 mg/L por orden, rechazar los valores no finitos, registrar cada rechazo, alarmar ante tres rechazos en 10 minutos; a prueba de fallos = conservar la última consigna válida; verificado con la prueba T3, incluidas pruebas basadas en propiedades (Lab 11).

### 27.6 Actividad práctica

Redacte especificaciones completas de dos controles del escenario de parada falsificada de §27.1, con desempeño, dependencias, modo de falla y verificación. Elija un control preventivo, como las órdenes autenticadas, y un control de recuperación, como la operación manual local en PS3 y PS4. Para cada uno, indique el desempeño que debe lograr, de qué depende y qué ocurre cuando falla. La autenticación debe fallar cerrada para las órdenes; la operación manual local debe funcionar sin el SCADA ni la red. Nombre un responsable por su rol y un método de verificación, y después compruebe si los dos controles comparten alguna dependencia que permitiría a un solo evento anular ambos.

### 27.7 Errores comunes y límites

- Controles sin criterios de desempeño.
- Límites impuestos en la HMI y no en el controlador.
- «Capas» que comparten dependencias.
- Ningún límite diseñado para la peor consecuencia cuando es factible.
- Materiales de recuperación al alcance del mismo atacante.

El ejemplo de la dosificación evita cada uno: los límites están en el controlador, la alarma del analizador usa un registrador separado, el límite de carrera está diseñado y cada elemento tiene una meta de desempeño. Los límites también conservan la última consigna válida cuando se rechaza una orden, de modo que el modo de falla queda enunciado, y cada rechazo se registra para la regla de alarma.

### Ejercicios — capítulo 27

**EX053 — Auditoría de dependencias de las capas.** *Objetivo:* comprobar la independencia. *Entradas:* los cuatro controles de §27.5 y su implementación: límites del controlador en el PLC de dosificación; analizador en un registrador separado; registro a través del SCADA. *Pasos:* enumere las dependencias de cada capa; identifique cualquier dependencia compartida; proponga un cambio. *Evidencia esperada:* tabla y cambio. *Rúbrica:* 3 = se encuentra la dependencia compartida (registro y alarma de los rechazos a través del SCADA), se propone un cambio (registro local más un camino de alarma independiente); 2 = sin cambio; 1 = solo la lista; 0 = nada.

**EX054 — Qué significa «a prueba de fallos».** *Objetivo:* definir los modos de falla en su contexto. *Entradas:* la pasarela de telemetría autenticada de PS4. *Pasos:* ante una falla de la pasarela, defina qué significa «a prueba de fallos» para (a) las órdenes, (b) la telemetría, (c) el control local, y justifíquelo. *Evidencia esperada:* tres definiciones. *Rúbrica:* 3 = las órdenes fallan cerradas (se rechazan), la telemetría falla de forma visible (alarma en el SCADA), el control local continúa automáticamente; 2 = una mal definida; 1 = «a prueba de fallos = parar»; 0 = nada.

### Síntesis del capítulo

Diseñe controles por escenario en los puntos de prevención, detección y recuperación. Ponga límites físicos diseñados a las peores consecuencias, imponga los límites donde el atacante no pueda eludirlos, haga independientes las capas y especifique para cada control su desempeño, sus dependencias, su modo de falla, su responsable y su verificación.

<!-- open-cyber-academy:chapter-navigation:start ch-27 -->
### Siga estudiando — capítulo 27 de 50

[← Capítulo 26](#ch-26) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 28 →](#ch-28)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-28"></a>

## Capítulo 28 — Infraestructura crítica y seguridad sectorial: implementación I

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) implementar un control de seguridad como código funcional con pruebas, a partir de su especificación; (2) aplicar prácticas de codificación segura para el manejo de entradas, la criptografía y el manejo de errores; (3) construir un banco de pruebas que ejercite el control sin conexión; y (4) registrar una evidencia de implementación que remita a los requisitos. Implementa las especificaciones del capítulo 27 y prepara el capítulo 29.

### 28.1 De la especificación al código

Parta de la especificación del control (capítulo 27): cada «deberá» se convierte en al menos una prueba, antes del código o a la par que él. Mantenga la implementación pequeña y, cuando sea posible, sin dependencias: la pasarela de este libro usa solo la biblioteca estándar de Python. Estructúrela como recomienda el capítulo 9: un analizador (capítulo 4), un verificador (capítulo 19), un almacén de estado (contadores contra repeticiones) y una interfaz de salida, cada uno probado por separado. La pasarela del TMRP sigue esta estructura, y por eso su error con NaN pudo encontrarse y corregirse solo en el validador.

### 28.2 Codificación segura para los caminos de control

- Valide la entrada antes de usarla: longitud, MAC, contador, forma, rango físico (Labs 3 y 8).
- Compare los secretos en tiempo constante (`hmac.compare_digest`).
- Cargue las claves desde un almacenamiento protegido, nunca desde el código fuente ni desde archivos legibles por todos.
- Trate toda excepción en el camino de verificación como un rechazo; nunca acepte por defecto.
- Acote el uso de recursos: tamaño máximo de mensaje, longitud máxima de cola, límites de frecuencia por origen.
- Registre los rechazos con contexto suficiente para investigar, sin registrar secretos.

Estas reglas salen directamente de los Labs 3, 8 y 11. Cada una tiene una prueba en el conjunto de pruebas de la pasarela.

### 28.3 El banco de pruebas

Un banco de pruebas reproduce sin conexión el entorno del control: RTU simuladas que envían mensajes válidos, malformados, falsificados, repetidos y retrasados; un SCADA simulado que recibe la salida de la pasarela; y un reloj que se puede controlar. El Lab 15 (capítulo 40) es una versión compacta. Los bancos permiten probar modos de falla que sería inseguro o imposible provocar en un sistema en servicio. El banco del TMRP incluye RTU simuladas en PS2 y PS4, un receptor SCADA simulado y un reloj controlable, de modo que los reinicios, los retardos y las repeticiones pueden producirse a demanda. El mismo arnés sostiene después la campaña de inyección de fallas con semilla, y por eso invertir pronto en él ahorra tiempo cuando empieza la verificación del proyecto final.

### 28.4 Evidencia

Registre para cada implementación: las versiones del requisito y de la especificación implementadas; la revisión del código fuente; los resultados de las pruebas con las versiones de las herramientas; las limitaciones conocidas; y la aprobación del revisor. Esto pasa a formar parte del expediente de evidencia (capítulo 48). Para el validador de consignas del TMRP, el registro muestra la versión de la especificación, los *commits* de v1 y v2, los resultados de T3 de cada uno, la limitación conocida de que v1 aceptaba NaN y el revisor que planteó la pregunta sobre NaN. Sin ese registro, el hallazgo posterior del expediente sobre el estado de T3 habría sido imposible de resolver, porque nadie podría haber mostrado qué versión había pasado. Registrar la evidencia mientras se hace el trabajo cuesta minutos; reconstruirla después cuesta días.

### 28.5 Ejemplo resuelto: validador de consignas v1 (sintético)

El equipo del TMRP implementa R3 a partir de la especificación de §27.5. La versión 1 comprueba `new < lo`, `new > hi` y el límite de escalón, y supera las pruebas de ejemplo: en rango, aceptado; por encima y por debajo del rango, rechazado; escalón demasiado grande, rechazado. La revisión de código pregunta: ¿y NaN? En la aritmética IEEE 754, toda comparación de orden con NaN es falsa, así que `nan < lo` y `nan > hi` son ambas falsas y `abs(nan - old) > max_step` es falsa: v1 acepta NaN. La versión 2 rechaza explícitamente los valores no finitos y expresa la región segura en positivo (`lo <= new <= hi`), lo que es falso para NaN. Las pruebas basadas en propiedades del capítulo 30 confirman la diferencia de forma sistemática (Lab 11). Esta es la falla de la prueba T3 del escenario de aprobación del capítulo 10.

### 28.6 Actividad práctica

Implemente una pasarela mínima que combine la salida del analizador del Lab 3 con el sellado del Lab 8, de modo que una lectura Modbus validada se convierta en una trama autenticada. Escriba pruebas para cada camino de rechazo. Mantenga las dos partes separadas tras interfaces claras: el analizador devuelve una lectura validada o un motivo de rechazo, y solo se sella una lectura validada. Pruebe cada camino de rechazo del Lab 3 y confirme que nada llega a la función de sellado. Después compruebe que la trama sellada supera el receptor del Lab 8 y que una copia manipulada se rechaza. Guarde la clave fuera del archivo fuente, incluso en este ejercicio, para que el hábito esté instalado antes de que aparezcan claves reales.

### 28.7 Errores comunes y límites

- Código escrito antes de que la especificación esté clara.
- Comportamiento de aceptar por defecto ante las excepciones.
- Comprobaciones en negativo (`if x > hi: reject`) que pasan por alto NaN; prefiera comprobaciones en positivo de la región segura.
- Claves en el código fuente.
- Evidencia reconstruida a posteriori.

La primera versión del validador de consignas muestra el tercer error, y el expediente del TMRP existe para evitar el último. Su aceptación de NaN venía de las comprobaciones en negativo, y la corrección fue enunciar en positivo la región segura. Las claves del código del banco del TMRP se cargan desde un archivo protegido, nunca se escriben en el código fuente, y toda excepción en el camino de verificación termina en un rechazo que se registra.

### Ejercicios — capítulo 28

**EX055 — NaN y compañía.** *Objetivo:* encontrar aceptaciones inseguras. *Entradas:* `validate_v1` del Lab 11. *Pasos:* evalúe a mano v1 y v2 para `new` = NaN, +∞, −∞, 5.5 y 5.50001 con `old` = 5.2, y explique cada resultado. *Evidencia esperada:* tabla. *Rúbrica:* 3 = entre los valores especiales, v1 acepta solo NaN (∞ se rechaza por `> hi`, −∞ por `< lo`), 5.5 lo aceptan ambas (límite inclusivo), 5.50001 se rechaza; v2 rechaza todos los no finitos; explicaciones correctas; 2 = un error; 1 = sin explicaciones; 0 = nada.

**EX056 — Registro de los rechazos.** *Objetivo:* diseñar registros útiles. *Entradas:* la pasarela. *Pasos:* defina un registro para cada tipo de rechazo (etiqueta, repetición, sin datos recientes, forma, rango) con sus campos, y explique un campo que excluye deliberadamente. *Evidencia esperada:* esquema. *Rúbrica:* 3 = los campos permiten investigar (fuente de tiempo, estación, contador, motivo, ID de la pasarela, hash del mensaje), excluye el material de claves y la carga útil completa cuando es sensible; 2 = falta la fuente de tiempo o la estación; 1 = texto libre; 0 = nada.

### Síntesis del capítulo

Implemente los controles a partir de las especificaciones, con pruebas para cada «deberá». Programe el camino de control de forma defensiva: valide por completo, compare en tiempo constante, proteja las claves, rechace ante cualquier error, acote los recursos y registre de forma útil. Prefiera las comprobaciones en positivo de la región segura. Pruebe en un banco capaz de producir las fallas que no puede provocar en servicio, y registre la evidencia sobre la marcha.

<!-- open-cyber-academy:chapter-navigation:start ch-28 -->
### Siga estudiando — capítulo 28 de 50

[← Capítulo 27](#ch-27) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 29 →](#ch-29)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-29"></a>

## Capítulo 29 — Infraestructura crítica y seguridad sectorial: medición

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) definir métricas de seguridad y resiliencia que respalden decisiones; (2) calcular métricas de detección —precisión, exhaustividad, F1, tasa de falsas alarmas, tiempo de detección— a partir de pruebas etiquetadas; (3) medir la resiliencia como el desempeño del servicio a lo largo del tiempo durante una perturbación; y (4) evitar métricas que recompensen el comportamiento equivocado. Se apoya en los capítulos 7 y 28 y prepara los capítulos 30, 38 y 40.

### 29.1 Qué medir

Una métrica es útil si cambia una decisión. Hay tres familias: **desempeño de los controles** (¿hace el control lo que se especificó?: tasas de rechazo, tiempos de detección); **exposición** (¿cuánta superficie de ataque o vulnerabilidad existe?: conductos sin autenticación, vulnerabilidades alcanzables sin parchear, cuentas compartidas); y **resiliencia del servicio** (¿cómo se degrada y se recupera el servicio?). Use el enfoque objetivo–pregunta–métrica: enuncie el objetivo, la pregunta que mostraría el avance y, solo entonces, la métrica. En el TMRP, la latencia de alarma de R7 mide el desempeño de los controles, el número de conductos sin autenticación mide la exposición y la proporción de la demanda atendida durante el ensayo de recuperación mide la resiliencia.

### 29.2 Métricas de detección

De un conjunto de prueba etiquetado se obtienen verdaderos positivos (TP), falsos positivos (FP), falsos negativos (FN) y verdaderos negativos (TN). **Precisión** = TP/(TP+FP): de las alarmas, cuántas eran reales. **Exhaustividad** (*recall*) = TP/(TP+FN): de los eventos reales, cuántos se encontraron. **F1** es su media armónica. Informe la precisión y la exhaustividad junto con la tasa base del conjunto de prueba; la precisión en un conjunto de prueba con un 50 % de ataques dice poco sobre una operación con un 0,1 % (capítulo 7). El **tiempo de detección** es una distribución; informe la mediana y los peores casos, no solo la media. [Arp et al. (2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) enumeran errores frecuentes al evaluar sistemas de seguridad basados en aprendizaje automático, entre ellos tasas base poco realistas y la contaminación por espionaje de datos (*data snooping*); [Kim et al. (2022)](https://ojs.aaai.org/index.php/AAAI/article/view/20680) muestran cómo la evaluación con ajuste por puntos puede inflar las puntuaciones de detección de anomalías en series temporales.

### 29.3 La resiliencia como desempeño a lo largo del tiempo

Represente el desempeño del servicio $Q(t)$ —para la LRWA, la fracción de la demanda atendida— durante una perturbación. [Bruneau et al. (2003)](https://doi.org/10.1193/1.1623497) propusieron medir la pérdida de resiliencia como el área entre el desempeño pleno y $Q(t)$, desde la perturbación hasta la recuperación. La curva muestra la robustez (cuánto cae el desempeño), la rapidez (con qué velocidad se recupera) y la pérdida total. Los requisitos de ingeniería se proyectan sobre ella: R4 mantiene la caída poco profunda; R6 acorta la recuperación.

El ensayo de recuperación del TMRP ofrece una curva real, ya que el suministro se mantuvo en modo local mientras se restablecía la operación remota.

### 29.4 Métricas que engañan

Contar los ataques bloqueados recompensa a los cortafuegos ruidosos; contar los parches aplicados ignora cuáles importaban; el tiempo medio de detección oculta el único evento detectado al cabo de tres semanas. Cuando una métrica se convierte en objetivo, las personas optimizan la métrica. Prefiera métricas ligadas a las consecuencias y verificadas mediante pruebas. La prueba de aceptación del detector del TMRP los evita al informar de las omisiones y de la detección más lenta, no solo de un promedio. Los dos eventos de reconocimiento no detectados permanecen en el informe, porque son el resultado que cambia cuánto puede confiar la LRWA en el detector.

### 29.5 Ejemplo resuelto: prueba de aceptación de un detector de anomalías (sintético)

La prueba de aceptación del TMRP para un detector de anomalías de red usa 14 eventos etiquetados de una semana de pruebas en el banco (Lab 10): 7 maliciosos (inundaciones de escrituras, códigos de función no autorizados, una nueva conexión de ingeniería) y 7 benignos (mantenimiento, copia de seguridad del firmware, una conmutación por error). Resultados: precisión 0,625, exhaustividad 0,714, F1 0,667; tiempo de detección de los eventos detectados de 2 a 30 minutos, mediana 7. Los dos ataques no detectados fueron ambos reconocimientos lentos y de bajo volumen. La decisión de aceptación: desplegarlo para detectar ataques de alto volumen, no confiar en él para el reconocimiento y dejar constancia de que la tasa base del 50 % del conjunto de prueba hace que la precisión operativa sea mucho menor.

### 29.6 Actividad práctica: Lab 10

```python
# Lab 10 - detection metrics and time-to-detect from a labelled synthetic test week (offline)
# (event_id, truly_malicious, alerted, minutes_from_start_to_alert or None)
EV = [(1,1,1,4),(2,1,1,11),(3,1,0,None),(4,0,1,None),(5,0,0,None),(6,1,1,2),(7,0,1,None),
      (8,0,0,None),(9,1,1,30),(10,0,0,None),(11,0,0,None),(12,1,0,None),(13,0,1,None),(14,1,1,7)]
tp = sum(1 for e in EV if e[1] and e[2]); fp = sum(1 for e in EV if not e[1] and e[2])
fn = sum(1 for e in EV if e[1] and not e[2]); tn = sum(1 for e in EV if not e[1] and not e[2])
prec, rec = tp / (tp + fp), tp / (tp + fn)
print(f"TP={tp} FP={fp} FN={fn} TN={tn} precision={prec:.3f} recall={rec:.3f} F1={2*prec*rec/(prec+rec):.3f}")
ttd = sorted(e[3] for e in EV if e[1] and e[2])
print("time to detect (min):", ttd, "mean", round(sum(ttd)/len(ttd), 1), "median", ttd[len(ttd)//2])
```

Salida esperada:

```text
TP=5 FP=3 FN=2 TN=4 precision=0.625 recall=0.714 F1=0.667
time to detect (min): [2, 4, 7, 11, 30] mean 10.8 median 7
```

Los recuentos coinciden con el ejemplo resuelto: cinco ataques detectados, tres eventos benignos que generaron alarma, dos ataques no detectados y cuatro eventos benignos sin alarma. Los dos ataques no detectados fueron reconocimientos lentos y de bajo volumen, que el detector no ve. Los tiempos de detección muestran por qué importa la mediana: un evento tardó treinta minutos, mientras que la mayoría se encontró en menos de diez. Como la mitad de los eventos de prueba eran maliciosos, la precisión aquí es muy superior a la que la LRWA observaría en operación, como muestra el EX057.

### 29.7 Errores comunes y límites

- Métricas que nadie usa para tomar una decisión.
- Precisión obtenida en conjuntos de prueba equilibrados presentada como si fuera operativa.
- Tiempo medio de detección sin distribución ni omisiones.
- Resiliencia informada solo como tiempo de disponibilidad.
- Métricas que se convierten en objetivos.

La prueba de aceptación del TMRP informa de las omisiones y de la detección más lenta, y su precisión se enuncia junto con la tasa base del cincuenta por ciento del conjunto de prueba, para que nadie la confunda con la precisión operativa. La resiliencia se muestra como la proporción de la demanda atendida a lo largo del tiempo, no como tiempo de disponibilidad. Cada métrica que contiene informa la decisión de despliegue.

### Ejercicios — capítulo 29

**EX057 — Precisión operativa.** *Objetivo:* trasladar las métricas de prueba a la operación. *Entradas:* exhaustividad del Lab 10 de 0,714 y tasa de FP de la prueba de 3/7; tasa base operativa de 1 evento malicioso por cada 1.000 eventos. *Pasos:* calcule la precisión operativa y las falsas alarmas esperadas por cada 1.000 eventos; interprete. *Evidencia esperada:* cifras e interpretación. *Rúbrica:* 3 = cálculo correcto (precisión ≈ 0,0017; ≈ 428 falsas alarmas por cada 1.000 eventos), con la interpretación de que la estimación de FP a partir de 7 eventos benignos es demasiado incierta y de que el detector es inutilizable sin una FPR mucho menor; 2 = cifras correctas; 1 = fórmula errónea; 0 = nada.

**EX058 — Curva de resiliencia.** *Objetivo:* calcular la pérdida de resiliencia. *Entradas:* $Q(t)$ sintética: 100 % hasta t = 0; 60 % de 0 a 4 h; recuperación lineal hasta el 100 % de 4 h a 12 h. *Pasos:* calcule el área de pérdida en %·h; recalcúlela si el modo manual local (R4) mantiene $Q$ en el 85 % de 0 a 4 h. *Evidencia esperada:* dos cifras y una frase. *Rúbrica:* 3 = 160+160 = 320 %·h y 60+60 = 120 %·h con una interpretación clara; 2 = un error; 1 = solo el método; 0 = nada.

### Síntesis del capítulo

Mida lo que cambia las decisiones: el desempeño de los controles, la exposición y la resiliencia del servicio. Informe la precisión y la exhaustividad con las tasas base, y distribuciones del tiempo de detección que incluyan las omisiones. Represente la resiliencia como desempeño a lo largo del tiempo. Desconfíe de las métricas que pueden manipularse o que ocultan el peor caso.

<!-- open-cyber-academy:chapter-navigation:start ch-29 -->
### Siga estudiando — capítulo 29 de 50

[← Capítulo 28](#ch-28) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 30 →](#ch-30)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-30"></a>

## Capítulo 30 — Laboratorio de verificación I

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) planificar y ejecutar una campaña de verificación de controles de seguridad con criterios de aprobación y rechazo definidos; (2) usar pruebas basadas en ejemplos, de límites, negativas y basadas en propiedades; (3) registrar los resultados de modo que otro ingeniero pueda reproducirlos; y (4) tratar con honestidad las pruebas fallidas, incluida la repetición de la prueba tras las correcciones. Verifica la implementación del capítulo 28 y prepara el capítulo 38 (validación) y el capítulo 40 (Laboratorio de verificación II).

### 30.1 La verificación como campaña

La verificación responde a la pregunta: ¿cumple la implementación su especificación? Un plan de campaña enumera, para cada requisito, los casos de prueba, el entorno, las entradas, el procedimiento, el resultado esperado, el criterio de aprobación y quién la ejecuta. Las pruebas se escriben antes de la ejecución y no se modifican para que los resultados aprueben. Los resultados incluyen los detalles del entorno (versiones de software, semillas, configuración) para que la prueba pueda repetirse. El plan de campaña del TMRP enumera las pruebas T1 a T7 frente a R1 a R8, con criterios de aprobación fijados antes de ejecutar ninguna prueba; R9 aún no tiene prueba asignada, lo que el mapa de evidencias pone de manifiesto más adelante. Cada prueba indica su entorno y quién la ejecuta.

### 30.2 Tipos de prueba

- Las **pruebas basadas en ejemplos** comprueban el comportamiento típico.
- Las **pruebas de límites** comprueban los bordes: exactamente en los límites, justo dentro, justo fuera.
- Las **pruebas negativas** comprueban que se rechaza la entrada no válida: malformada, falsificada, repetida, fuera de rango.
- Las **pruebas basadas en propiedades** enuncian una propiedad que debe cumplirse para todas las entradas («nunca se acepta una consigna insegura») y la comprueban sobre muchas entradas generadas, incluidos valores especiales. Encuentran casos que a nadie se le ocurrió escribir.
- Las **pruebas de inyección de fallos** (capítulo 40) perturban el entorno: descartan, retrasan o corrompen mensajes; reinician componentes.

Las pruebas basadas en ejemplos muestran la presencia de un comportamiento correcto en los casos elegidos; las pruebas basadas en propiedades y las de inyección de fallos buscan de forma más amplia la ausencia de comportamiento incorrecto. Ninguna demuestra la corrección para todas las entradas, salvo en dominios finitos pequeños (capítulo 2).

### 30.3 Reproducibilidad

Fije la semilla de todo generador aleatorio e imprímala; registre las versiones de herramientas y bibliotecas; conserve las entradas de prueba; almacene los resultados junto con la revisión del código fuente. Una prueba fallida que no puede reproducirse no puede corregirse ni volver a verificarse. El registro de T3 del TMRP sigue esta regla: indica la semilla, el número de casos generados y la versión de Python, de modo que cualquiera puede volver a ejecutar la prueba basada en propiedades y ver las mismas treinta y una aceptaciones de NaN en v1 y ninguna en v2. Sin la semilla, un revisor solo podría aceptar el resultado por confianza. El mismo registro almacena la revisión del código fuente de cada versión del validador.

### 30.4 Pruebas fallidas

Una prueba fallida es información. Regístrela como fallida, con evidencia; analice la causa raíz; corrija; vuelva a ejecutar la prueba fallida y el conjunto de regresión; registre la nueva prueba. Nunca vuelva a etiquetar un fallo como «no aplicable» porque se acerca el plazo (capítulo 10). Si un fallo se acepta temporalmente, necesita un control compensatorio, un responsable y una fecha. T3 es el modelo: falló en v1, se corrigió en v2, se volvió a probar y se registró. El fallo de v1 nunca se reetiquetó, y el control compensatorio PS4 tenía responsable y fecha.

### 30.5 Ejemplo resuelto: límites de consigna en T3 (sintético)

La prueba T3 verifica R3. Las pruebas basadas en ejemplos sobre v1 (dentro del rango, por encima, por debajo, paso grande) aprueban. La prueba basada en propiedades genera 2.000 casos con la semilla 30, uno de cada diez extraído de valores especiales (NaN, ±∞, límites exactos). v1 acepta 31 valores inseguros, todos NaN. v2 no acepta ninguno. T3 se registra como **fallida en v1**, con la causa raíz «las comparaciones negativas son falsas para NaN», se corrige en v2, se vuelve a probar y queda **aprobada en v2**, con la semilla y la versión de Python registradas.

Ambos resultados permanecen en el registro. El resultado de la nueva prueba se anota después en la matriz de trazabilidad.

### 30.6 Actividad práctica: Lab 11

```python
# Lab 11 - property-based testing of a setpoint validator finds what example tests missed (offline)
import random, math
def validate_v1(new, old, lo=0.5, hi=5.5, max_step=0.5):
    if new < lo: return False
    if new > hi: return False
    if abs(new - old) > max_step: return False
    return True
def validate_v2(new, old, lo=0.5, hi=5.5, max_step=0.5):
    if not (isinstance(new, float) and math.isfinite(new)): return False
    return lo <= new <= hi and abs(new - old) <= max_step
examples = [(3.0, 3.2), (6.0, 5.8), (0.2, 0.6), (4.0, 3.0)]
print("example tests v1:", [validate_v1(n, o) for n, o in examples])
rng = random.Random(30)
specials = [float("nan"), float("inf"), -float("inf"), 5.5, 0.5]
def prop(f, trials=2000):
    fails = []
    for i in range(trials):
        old = rng.uniform(0.5, 5.5)
        new = rng.choice(specials) if i % 10 == 0 else rng.uniform(-1, 7)
        ok = f(new, old)
        safe = math.isfinite(new) and 0.5 <= new <= 5.5 and abs(new - old) <= 0.5
        if ok and not safe: fails.append(new)
    return fails
f1 = prop(validate_v1); f2 = prop(validate_v2)
print("v1 unsafe acceptances:", len(f1), "first:", f1[:1])
print("v2 unsafe acceptances:", len(f2))
```

Salida esperada:

```text
example tests v1: [True, False, False, False]
v1 unsafe acceptances: 31 first: [nan]
v2 unsafe acceptances: 0
```

Las pruebas basadas en ejemplos dan las mismas respuestas para ambos validadores, de modo que no pueden distinguir v1 de v2. Lo que los separa es la ejecución basada en propiedades: v1 acepta treinta y un valores inseguros, todos NaN, mientras que v2 no acepta ninguno. La semilla treinta hace que la ejecución sea repetible. Observe que el generador extrae valores especiales solo una vez de cada diez; sin eso, NaN casi nunca aparecería y el error seguiría oculto por muchos casos aleatorios que se probaran. Registre la semilla junto con el resultado.

### 30.7 Errores comunes y límites

- Pruebas escritas después de ver los resultados.
- Solo pruebas basadas en ejemplos.
- Pruebas aleatorias sin semilla; resultados sin versiones.
- Fallos reetiquetados en lugar de corregidos.
- Afirmar que las pruebas basadas en propiedades demuestran la corrección.

El registro de T3 del TMRP evita cada uno de estos errores. Su propiedad se escribió antes de la ejecución, su generador tiene semilla, el fallo en v1 siguió registrado como fallido y el informe afirma solo que no se encontró ningún valor inseguro entre los casos generados, no que v2 sea correcto para cualquier entrada. La semilla y la versión se almacenan con el resultado.

### Ejercicios — capítulo 30

**EX059 — Cuente los fallos.** *Objetivo:* razonar sobre pruebas generadas. *Entradas:* Lab 11. *Pasos:* (1) explique por qué las 31 aceptaciones inseguras son NaN; (2) estime cuántos casos NaN produjo el generador (uno de cada diez casos es un valor especial, elegido de manera uniforme entre cinco) y compárelo con 31; (3) explique por qué no todo caso NaN es una aceptación insegura en v1, o demuestre que todo NaN se acepta. *Evidencia esperada:* razonamiento y cifras. *Rúbrica:* 3 = ≈ 200 casos especiales × 1/5 ≈ 40 NaN esperados, 31 observados, compatible con la variación aleatoria, y todo NaN es aceptado por v1, de modo que 31 es el número de NaN; 2 = parcial; 1 = sin cifras; 0 = nada.

**EX060 — Plan de verificación para R2.** *Objetivo:* planificar pruebas de rechazo de repeticiones. *Entradas:* R2 y el Lab 8. *Pasos:* redacte un plan de pruebas con al menos seis casos (incluido el reinicio de cada lado, el desbordamiento o el máximo del contador y la entrega fuera de orden), resultados esperados y criterios de aprobación. *Evidencia esperada:* tabla. *Rúbrica:* 3 = los casos cubren el reinicio y el orden, los resultados esperados son coherentes con el diseño del §19.5 y los criterios no son ambiguos; 2 = falta el reinicio; 1 = solo el camino feliz; 0 = nada.

### Síntesis del capítulo

La verificación es una campaña planificada con criterios fijados de antemano. Combine pruebas basadas en ejemplos, de límites, negativas, basadas en propiedades y de inyección de fallos; haga reproducible cada ejecución; y trate los fallos como información que debe corregirse y volver a verificarse, nunca reetiquetarse.

<!-- open-cyber-academy:chapter-navigation:start ch-30 -->
### Siga estudiando — capítulo 30 de 50

[← Capítulo 29](#ch-29) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 31 →](#ch-31)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-31"></a>

## Capítulo 31 — Infraestructura crítica y seguridad sectorial: implementación II

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) desplegar controles en entornos operativos mediante una implantación por etapas con reversión; (2) gestionar claves, configuración y secretos en producción; (3) integrar equipos heredados mediante pasarelas y controles compensatorios; y (4) poner en servicio un control con pruebas de aceptación y traspaso a los operadores. Lleva al terreno la implementación de banco del capítulo 28 y prepara los capítulos 32–34.

### 31.1 Despliegue por etapas

El despliegue en campo sigue etapas, cada una con criterios de entrada y de salida: banco (todas las pruebas aprueban); emplazamiento piloto de baja consecuencia; un emplazamiento de alta consecuencia con supervisión adicional y un plan de reversión; flota. Cada etapa tiene una **reversión** —la capacidad de volver con rapidez al estado anterior conocido como correcto—, probada antes de necesitarla. Programe los cambios fuera de los picos de demanda y con los operadores informados; en el sector del agua, evite cambios durante periodos de alta demanda o cuando el almacenamiento esté bajo.

Las etapas del TMRP son el banco, PS2 como piloto de baja consecuencia, PS4 como primer emplazamiento de alta consecuencia y, después, la flota.

### 31.2 Gestión de claves y secretos en producción

En el banco, las claves son archivos; en producción, son ciclos de vida. Genere las claves en módulos de seguridad de hardware o en elementos seguros de los dispositivos; registre los dispositivos mediante una ceremonia auditable (dos personas, con registro); guarde el inventario de qué clave pertenece a qué dispositivo y su fecha de rotación; rótelas; y revóquelas sin demora cuando un dispositivo se pierda o se dé de baja. Los secretos de las cuentas de servicio van a una bóveda con registro de accesos, no a scripts. Un inventario de claves es, en sí mismo, información sensible.

En el TMRP, las claves se generan en el elemento seguro de la pasarela durante el registro.

### 31.3 Integración de equipos heredados

Los dispositivos heredados que no pueden autenticarse se envuelven: una pasarela colocada físicamente al lado (en el mismo armario) añade autenticación en el lado de la red y habla el protocolo heredado por un enlace corto y protegido físicamente. La pasarela pasa a formar parte de la frontera de seguridad del dispositivo, de modo que necesita su propio bastionado, su propia supervisión y su propio camino de actualización. Los controles compensatorios cubren lo que la pasarela no puede cubrir: alarmas de manipulación del armario, registro local y restricciones sobre qué códigos de función pasan.

En PS2, la pasarela se encuentra en el armario de la RTU, con un enlace serie de 30 cm, y deja pasar solo dos códigos de función.

### 31.4 Puesta en servicio y traspaso

La puesta en servicio verifica el sistema instalado en su entorno real: las pruebas de aceptación en el emplazamiento repiten en el lugar las pruebas clave del banco (la autenticación rechaza tramas falsificadas; se rechaza la repetición; la conmutación a automático local funciona; las alarmas llegan a la sala de control en 60 s). El traspaso entrega a los operadores procedimientos, formación, contactos y las limitaciones conocidas. Mientras los operadores no puedan manejar y recuperar el sistema, el control no está en servicio.

En PS2, la aceptación en el emplazamiento también detectó la deriva del reloj de la pasarela, que se corrigió y se volvió a probar antes del traspaso. Primero se formó a los operadores.

### 31.5 Ejemplo resuelto: piloto en PS2 (sintético)

El emplazamiento piloto del TMRP es PS2: RTU-A heredada, de baja consecuencia. Criterios de entrada: T1, T2, T3 (v2) y T5 aprobadas en el banco; imagen de reversión preparada; operadores informados. La pasarela se instala en el armario de la RTU; el enlace serie mide 30 cm dentro del armario cerrado con llave; la pasarela deja pasar solo los códigos de función 3 (lectura) y 6 (escritura de un único registro) para el rango de registros configurado. Aceptación en el emplazamiento: las tramas falsificadas y repetidas se rechazan y generan alarma; al retirar la antena LTE se pasa a operación automática local y salta una alarma de pérdida de comunicación en 60 s; al reponer la antena se reanuda la telemetría con los contadores en continuidad. Un hallazgo: el reloj de la pasarela derivó 40 s en 48 h porque NTP no era alcanzable a través del nuevo conducto; se corrigió añadiendo una fuente de tiempo interna a la lista de permitidos del conducto. Criterios de salida cumplidos tras la nueva prueba; PS4 es el siguiente.

### 31.6 Actividad práctica

Redacte el plan de etapas para la implantación del TMRP en la flota, con criterios de entrada y salida y reversión para cada etapa, y una nota de traspaso de dos páginas para los operadores sobre la pasarela. Use el piloto de PS2 como modelo de criterios de entrada y salida y, después, extienda el plan a PS4 y a las estaciones restantes. Para cada etapa, indique cómo se realiza la reversión y quién decide aplicarla. En la nota de traspaso, indique a los operadores las alarmas que genera la pasarela, qué significa cada una, cómo pasar a operación manual local y a quién llamar. Enumere con claridad las limitaciones conocidas, como la dependencia de una fuente de tiempo interna aprendida en PS2.

### 31.7 Errores comunes y límites

- Despliegue «de golpe» sin piloto ni reversión.
- Planes de reversión nunca probados.
- Registro de claves hecho por una sola persona y sin constancia.
- Pasarelas tratadas como transparentes en lugar de como dispositivos críticos para la seguridad.
- Puesta en servicio sin operadores; traspaso sin limitaciones conocidas.

El piloto de PS2 del TMRP evitó estos errores: tenía una imagen de reversión, se informó a los operadores antes de la instalación y el hallazgo de la deriva del reloj se trató como una corrección de interfaz y se volvió a probar antes de empezar con PS4. El registro de claves sigue la ceremonia de dos personas con registro descrita arriba, y la pasarela se trató como un dispositivo crítico para la seguridad, con su propio bastionado y su propio camino de actualización.

### Ejercicios — capítulo 31

**EX061 — Criterios de reversión.** *Objetivo:* definir cuándo revertir. *Entradas:* el despliegue en PS4. *Pasos:* defina tres desencadenantes medibles de reversión, quién decide y el tiempo máximo para completar la reversión. *Evidencia esperada:* lista. *Rúbrica:* 3 = desencadenantes medibles (p. ej., pérdida de telemetría > 5 min no explicada por pérdida del enlace, cualquier mensaje aceptado que no supere la auditoría, latencia de alarma > 60 s en alarmas prioritarias), responsable de la decisión designado por su función, tiempo de reversión coherente con la reserva del hospital; 2 = desencadenantes vagos; 1 = sin responsable; 0 = nada.

**EX062 — La pasarela como frontera.** *Objetivo:* proteger un envoltorio para equipos heredados. *Entradas:* la pasarela de PS2. *Pasos:* enumere seis controles que necesita la propia pasarela y el riesgo residual si un atacante obtiene acceso físico al armario. *Evidencia esperada:* lista y enunciado del riesgo residual. *Rúbrica:* 3 = bastionado, actualizaciones firmadas, protección de claves, filtrado de códigos de función, detección de manipulación, registro; riesgo residual honesto (un atacante físico puede eludirla a través del enlace serie); 2 = falta el riesgo residual; 1 = genérico; 0 = nada.

### Síntesis del capítulo

Despliegue por etapas con criterios de entrada y de salida y una reversión probada. Gestione las claves y los secretos como ciclos de vida con ceremonias auditables. Envuelva los dispositivos heredados con pasarelas que se traten a su vez como críticas para la seguridad, junto con controles físicos compensatorios. Un control solo está en servicio tras la aceptación en el emplazamiento y el traspaso a los operadores.

<!-- open-cyber-academy:chapter-navigation:start ch-31 -->
### Siga estudiando — capítulo 31 de 50

[← Capítulo 30](#ch-30) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 32 →](#ch-32)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-32"></a>

## Capítulo 32 — Infraestructura crítica y seguridad sectorial: confiabilidad

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) usar medidas de confiabilidad: tasa de fallos, MTBF, MTTR y disponibilidad; (2) calcular la disponibilidad de sistemas en serie, en paralelo y redundantes reparables con modelos de Markov; (3) mostrar cómo la capacidad de reparación y las causas comunes modifican los beneficios de la redundancia; y (4) vincular la ingeniería de confiabilidad con la seguridad, donde los fallos pueden ser provocados. Se apoya en el capítulo 7 y prepara los capítulos 33 y 41.

### 32.1 Medidas

Para un componente con tasa de fallos constante $\lambda$ (fallos por hora), el tiempo medio entre fallos es $1/\lambda$. Con un tiempo medio de reparación $1/\mu$, la disponibilidad en régimen estacionario es $A = \mu/(\lambda+\mu) = \text{MTBF}/(\text{MTBF}+\text{MTTR})$. Las tasas de fallos constantes se ajustan al periodo de vida útil de la electrónica; los fallos tempranos y por desgaste necesitan otras distribuciones (Weibull). En los componentes en **serie** (todos necesarios), las tasas se suman: $\lambda_s = \sum\lambda_i$. Los componentes en **paralelo** (basta con uno cualquiera) solo fallan cuando fallan todos a la vez.

En PS4, la tasa de fallos de cada bomba, de uno cada dos mil horas, y su tiempo de reparación de 24 horas dan la disponibilidad de una sola bomba que se usa en el Lab 12.

### 32.2 Redundancia reparable

Las fórmulas sencillas para sistemas en paralelo suponen unidades independientes, cada una reparada de forma independiente. Los emplazamientos reales suelen tener una sola cuadrilla de reparación, de modo que, cuando ambas unidades están caídas, una espera. Una cadena de Markov de tiempo continuo modela esta situación: estados 0, 1 y 2 unidades averiadas; transiciones con tasa $2\lambda$ de 0 a 1 y $\lambda$ de 1 a 2, y con tasa $\mu$ de vuelta desde 1 y desde 2 con una sola cuadrilla. Resolver las ecuaciones de equilibrio da las probabilidades en régimen estacionario; la indisponibilidad es la probabilidad del estado 2.

PS4 tiene exactamente esta restricción: dos bombas y una cuadrilla de reparación. El modelo de Markov del Lab 12 recoge la espera.

### 32.3 Fallos provocados

Los modelos de confiabilidad suponen que los fallos llegan al azar. Un adversario elige cuándo. Si un atacante puede inutilizar una bomba a distancia y esperar a que falle la otra, o inutilizar ambas, las cifras de Markov dejan de describir el riesgo. La ingeniería de confiabilidad sigue siendo importante para la seguridad: indica la **línea de base** que el atacante debe superar, la **capacidad de reparación** que determina la velocidad de recuperación y las existencias de repuestos que hacen real la reserva en frío. Los requisitos de seguridad buscan entonces que los fallos provocados exijan compromisos independientes (el condicionamiento del capítulo 23).

### 32.4 Ejemplo resuelto: bombas de servicio y reserva de PS4 (sintético)

Cada bomba de PS4 tiene una tasa de fallos de 1 cada 2.000 h y un tiempo medio de reparación de 24 h con una cuadrilla. El Lab 12 da una disponibilidad de una sola bomba de 0,98814 (unas 104 h de parada al año). El par 1 de 2 con una cuadrilla tiene una disponibilidad de 0,999719: ambas bombas paradas unos 148 minutos al año. La fórmula ingenua $1-(1-A)^2$ da 0,999859, la mitad de la indisponibilidad real, porque ignora que el segundo fallo puede producirse mientras la única cuadrilla está ocupada. Para la cadena de control del grupo de bombeo —bomba, arrancador y RTU en serie, con MTBF de 2.000, 5.000 y 10.000 h—, el MTBF en serie es de 1.250 h: la cadena es menos confiable que su elemento más débil.

### 32.5 Actividad práctica: Lab 12

```python
# Lab 12 - availability of a duplicated pump set with repair (two-state units, one repair crew; offline)
lam, mu = 1 / 2000, 1 / 24     # failures per hour per pump, repairs per hour
A1 = mu / (lam + mu)
# states: 0 = both up, 1 = one down, 2 = both down; one crew repairs one pump at a time
# balance: p1 = (2 lam / mu) p0 ; p2 = (lam / mu) p1
p0 = 1 / (1 + 2 * lam / mu + 2 * (lam / mu) ** 2)
p1 = 2 * lam / mu * p0; p2 = lam / mu * p1
print(f"single pump availability {A1:.6f}  downtime h/yr {8760*(1-A1):.1f}")
print(f"1oo2 availability {1-p2:.8f}  P(both down) {p2:.2e}  downtime min/yr {8760*60*p2:.2f}")
print(f"naive independent 1-(1-A1)^2 = {1-(1-A1)**2:.8f}")
mtbf_series = 1 / (1/2000 + 1/5000 + 1/10000)
print(f"series MTBF pump+starter+RTU: {mtbf_series:.0f} h")
```

Salida esperada:

```text
single pump availability 0.988142  downtime h/yr 103.9
1oo2 availability 0.99971883  P(both down) 2.81e-04  downtime min/yr 147.78
naive independent 1-(1-A1)^2 = 0.99985939
series MTBF pump+starter+RTU: 1250 h
```

Una sola bomba está parada unas 104 horas al año. El par con una cuadrilla está parado a la vez unos 148 minutos al año, aproximadamente el doble de lo que sugiere la fórmula ingenua, porque el segundo fallo puede llegar mientras la cuadrilla aún repara el primero. La cifra en serie muestra la debilidad de la cadena de control: bomba, arrancador y RTU juntos tienen un tiempo medio entre fallos de 1.250 horas, menor que el de cualquiera de ellos por separado. La diferencia la determina la capacidad de reparación, no la calidad de las bombas.

### 32.6 Errores comunes y límites

- Fórmulas de reparación independiente con una sola cuadrilla.
- Tasas de fallos constantes para equipos que envejecen.
- Ignorar las causas comunes (cuadro de arrancadores compartido, alimentación compartida).
- Cifras de confiabilidad presentadas como protección frente a ataques deliberados.
- Cifras de MTBF del fabricante usadas sin conocer sus condiciones de prueba.

En PS4, el primer error reduce a la mitad el tiempo de parada previsto, y el tercero ignora que ambas bombas comparten un cuadro de arrancadores y un alimentador. Las cifras de MTBF del fabricante para la RTU deberían contrastarse con los propios registros de mantenimiento de la LRWA antes de incorporarse al expediente, y ninguna de estas cifras dice nada sobre un atacante que detenga ambas bombas de forma deliberada.

### Ejercicios — capítulo 32

**EX063 — Dos cuadrillas.** *Objetivo:* modelar la capacidad de reparación. *Entradas:* Lab 12. *Pasos:* modifique el modelo de Markov para dos cuadrillas independientes (tasa de reparación $2\mu$ desde el estado 2) y calcule la indisponibilidad; compárela con una cuadrilla y con la fórmula ingenua. *Evidencia esperada:* cifras y conclusión. *Rúbrica:* 3 = el resultado con dos cuadrillas coincide con la fórmula ingenua independiente (explique por qué) y con una cuadrilla es aproximadamente el doble; 2 = cifras correctas, sin explicación; 1 = no se ejecutó; 0 = nada.

**EX064 — Decisión sobre repuestos.** *Objetivo:* vincular la confiabilidad con la logística. *Entradas:* el tiempo de reparación de 24 h supone una bomba de repuesto en almacén; sin repuesto, la reparación tarda 21 días (504 h). *Pasos:* calcule la indisponibilidad 1oo2 con una cuadrilla y un MTTR de 504 h, y recomiende si conviene mantener un repuesto. *Evidencia esperada:* cifra y recomendación. *Rúbrica:* 3 = cálculo correcto (use la fórmula del laboratorio con μ = 1/504) y recomendación ligada a la consecuencia para el hospital; 2 = cifra correcta; 1 = tasa errónea; 0 = nada.

### Síntesis del capítulo

La confiabilidad se mide con tasas de fallos, tiempos de reparación y disponibilidad; las cadenas en serie son más débiles que su eslabón más débil; la redundancia reparable depende de la capacidad de reparación, que las fórmulas sencillas ignoran. Los adversarios provocan fallos según su propio calendario, de modo que la confiabilidad aporta la línea de base y la capacidad de recuperación, mientras que la seguridad debe lograr que los fallos provocados exijan compromisos independientes.

<!-- open-cyber-academy:chapter-navigation:start ch-32 -->
### Siga estudiando — capítulo 32 de 50

[← Capítulo 31](#ch-31) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 33 →](#ch-33)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-33"></a>

## Capítulo 33 — Infraestructura crítica y seguridad sectorial: seguridad funcional y resiliencia

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) aplicar el análisis de procesos basado en la teoría de sistemas (STPA) a una estructura de control, incluidas las causas relacionadas con la seguridad; (2) describir los sistemas instrumentados de seguridad y por qué necesitan independencia; (3) definir y diseñar la resiliencia: anticipar, resistir, recuperarse, adaptarse; y (4) integrar la seguridad funcional, la seguridad y la resiliencia en un único análisis. Se apoya en los capítulos 10, 17, 23 y 32 y prepara los capítulos 34 y 47.

### 33.1 STPA

[Leveson (2004)](https://doi.org/10.1016/S0925-7535(03)00047-X) propuso STAMP, un modelo de accidentes que trata la seguridad funcional como un problema de control: los accidentes surgen cuando no se hacen cumplir las restricciones sobre el comportamiento del sistema. STPA, el método de análisis construido sobre él, procede así: (1) definir las pérdidas y los peligros; (2) modelar la estructura de control: controladores, acciones de control, retroalimentación; (3) identificar las **acciones de control inseguras** (UCA) de cuatro tipos: no proporcionada cuando se necesita, proporcionada cuando es insegura, proporcionada demasiado pronto o demasiado tarde o en el orden equivocado, detenida demasiado pronto o aplicada durante demasiado tiempo; (4) identificar los escenarios de pérdida, es decir, por qué podría producirse cada UCA, incluidas la retroalimentación defectuosa, los modelos de proceso defectuosos y, en seguridad (STPA-Sec), la acción de un adversario. La fortaleza de STPA es que encuentra peligros derivados de interacciones en las que ningún componente ha fallado, que es exactamente la situación de un ataque de datos falsos.

### 33.2 Sistemas instrumentados de seguridad e independencia

Un sistema instrumentado de seguridad (SIS) lleva un proceso a un estado seguro cuando se detecta una condición peligrosa, con independencia del sistema básico de control del proceso. Las normas de seguridad funcional (IEC 61508 y sus derivadas sectoriales) asignan niveles de integridad de seguridad. La independencia implica sensores, lógica y elementos finales separados y, en términos actuales, redes y acceso de ingeniería separados, porque una estación de trabajo de ingeniería comprometida que puede reprogramar tanto la lógica de control como la de seguridad elimina la independencia. TRITON atacó directamente controladores de SIS ([informe HatMan de la CISA](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf)).

### 33.3 Resiliencia

[NIST SP 800-160 Vol. 2 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v2r1) articula la ciberresiliencia en torno a los objetivos de anticipar, resistir, recuperarse y adaptarse, con técnicas como la diversidad, la segmentación, la redundancia, la no persistencia y la respuesta adaptativa. [Haimes (2009)](https://doi.org/10.1111/j.1539-6924.2009.01216.x) sostiene que la resiliencia debe definirse en relación con amenazas y estados del sistema concretos. Diseñar la resiliencia significa: diseñar modos degradados (capítulo 22), mantener capacidad y reservas (almacenamiento, baterías, repuestos), lograr que la recuperación sea rápida y esté ensayada (capítulo 47) y aprender después de los eventos.

En la LRWA, el depósito del hospital, las baterías de los armarios y las 72 horas de operación automática local son reservas; el ensayo de recuperación es práctica.

### 33.4 Ejemplo resuelto: STPA sobre el control de nivel de Hollin Hill (sintético)

Pérdida L1: hospital sin agua; L2: desbordamiento del depósito e inundación. Peligros: H1, nivel por debajo del mínimo mientras continúa la demanda; H2, nivel por encima del rebosadero. Estructura de control: operador del SCADA → controlador PI (velocidad de la bomba de PS3) → bomba → depósito; retroalimentación mediante el transmisor de nivel. UCA: UCA1 «el controlador reduce el caudal de entrada cuando el nivel es bajo» (proporcionada cuando es insegura → H1); UCA2 «el operador no interviene cuando el nivel baja» (no proporcionada → H1); UCA3 «el controlador aumenta el caudal de entrada cuando el nivel es alto» (→ H2). Escenario de UCA1: el modelo de proceso del controlador cree que el nivel es alto porque la retroalimentación de nivel está falsificada (Lab 7). Escenario de UCA2: la pantalla del operador muestra el mismo nivel falsificado. Restricciones: medición de nivel independiente con alarma (EX034); disparo cableado de la bomba por nivel alto para H2; alarma de nivel bajo al operador a partir de la medición independiente. STPA llegó al mismo control que el detector de residuos, pero desde el peligro y no desde el ataque.

### 33.5 Actividad práctica

Amplíe el §33.4 con el lazo de dosificación: pérdidas, peligros, estructura de control, al menos cuatro UCA (una de cada tipo) y un escenario de pérdida para cada una, uno de ellos adversarial. Empiece por pérdidas como el daño a los consumidores por sobredosificación o subdosificación, y por peligros como un cloro residual fuera de sus límites. Dibuje la estructura de control: el operador, el controlador de dosificación, la bomba dosificadora y el analizador que retroalimenta el residual. Use los límites del lado del controlador y la alarma del analizador independiente de los controles de dosificación del TMRP al derivar las restricciones, y haga que su escenario adversarial sea uno en el que la retroalimentación del controlador esté falsificada.

### 33.6 Errores comunes y límites

- Análisis de peligros que ignora a los adversarios, o análisis de seguridad que ignora los peligros.
- «Independencia» del SIS con estación de trabajo de ingeniería o red compartidas.
- Resiliencia definida como «tiempo de disponibilidad».
- STPA reducido a una lista de comprobación sin estructura de control.

El EX066 muestra el segundo error en Fenwick, donde el sistema de parada por fuga de cloro gaseoso comparte la estación de trabajo de ingeniería y el conmutador de red con los controladores del proceso. El análisis de Hollin Hill del TMRP evita el primer error al incluir la retroalimentación de nivel falsificada como escenario de pérdida junto a los fallos aleatorios, y trata la resiliencia como servicio prestado a lo largo del tiempo, no como tiempo de disponibilidad de los servidores.

### Ejercicios — capítulo 33

**EX065 — Tabla de UCA.** *Objetivo:* identificar acciones de control inseguras. *Entradas:* §33.5. *Pasos:* elabore la tabla de UCA con los cuatro tipos y los escenarios. *Evidencia esperada:* tabla. *Rúbrica:* 3 = los cuatro tipos aplicados correctamente, escenarios que incluyen retroalimentación defectuosa y acción de un adversario, restricciones derivadas; 2 = tipos confundidos; 1 = lista de fallos, no de acciones de control; 0 = nada.

**EX066 — Auditoría de independencia.** *Objetivo:* comprobar la independencia del SIS. *Entradas:* el sistema de parada por fuga de cloro gaseoso de Fenwick comparte la estación de trabajo de ingeniería y el conmutador de red con los controladores del proceso. *Pasos:* identifique las violaciones de la independencia y proponga una arquitectura que la restablezca, con los riesgos residuales. *Evidencia esperada:* media página. *Rúbrica:* 3 = se identifican la estación de trabajo y el conmutador compartidos, acceso de ingeniería separado con llave física o estación de trabajo separada, red separada o cableado directo, riesgo residual enunciado; 2 = falta una violación; 1 = genérico; 0 = nada.

### Síntesis del capítulo

STPA trata las pérdidas como fallos de control y encuentra acciones de control inseguras que surgen de las interacciones, incluidas las adversariales. Los sistemas instrumentados de seguridad deben ser independientes en sensores, lógica, redes y acceso de ingeniería. La resiliencia —anticipar, resistir, recuperarse, adaptarse— debe definirse frente a amenazas concretas y diseñarse mediante modos degradados, reservas y una recuperación ensayada.

<!-- open-cyber-academy:chapter-navigation:start ch-33 -->
### Siga estudiando — capítulo 33 de 50

[← Capítulo 32](#ch-32) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 34 →](#ch-34)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-34"></a>

## Capítulo 34 — Infraestructura crítica y seguridad sectorial: integración

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) planificar la integración del sistema de forma incremental, con pruebas de interfaz; (2) integrar los controles de seguridad con las operaciones: alarmas, procedimientos, supervisión y respuesta a incidentes; (3) gestionar las interfaces organizativas con fabricantes, operadores de telecomunicaciones y otras empresas de servicios; y (4) reconocer el comportamiento emergente que aparece solo cuando los componentes se combinan. Sigue a los capítulos 31–33 y prepara el Taller de diseño II (capítulo 35).

### 34.1 Integración incremental

Integre en pequeños incrementos, con pruebas de interfaz en cada paso: pasarela con RTU; pasarela con SCADA; SCADA con la réplica del historiador; sensores de supervisión con el colector de registros. Cada paso usa el documento de control de interfaces (capítulo 16) como especificación de prueba. Cuando una prueba de integración falla, la especificación de la interfaz indica qué lado está mal, o revela que la especificación era ambigua. El orden del TMRP sigue los documentos de control de interfaces: primero pasarela con RTU en PS2, después pasarela con SCADA y, por último, la réplica de la DMZ.

### 34.2 Comportamiento emergente

Combinar componentes correctos puede producir sistemas incorrectos. Ejemplos: una pasarela de autenticación que almacena mensajes durante una pérdida del enlace y luego libera una ráfaga al reconectarse, inundando el sondeador del SCADA; una conmutación por error del par SCADA que reinicia los contadores contra repeticiones; un detector de anomalías que marca como ataque cada retransmisión de la pasarela. Las pruebas de integración deben incluir escenarios de sistema completo —pérdida y recuperación del enlace, conmutación por error, modo de mantenimiento—, no solo la conformidad de las interfaces.

El TMRP se encontró con el primer ejemplo en las pruebas de integración, como describe el ejemplo resuelto más abajo. Cada uno necesita una prueba de escenario.

### 34.3 Integración con las operaciones

Un control no está integrado hasta que las operaciones pueden usarlo: alarmas con significado, prioridad y procedimientos de respuesta claros; paneles que muestren el estado de seguridad junto al estado del proceso; guías de actuación que vinculen las alarmas de seguridad con las decisiones operativas (¿pasar a manual local?, ¿llamar al jefe de turno?); y formación. La práctica de gestión de alarmas —racionalizar las alarmas para que cada una exija una acción del operador— importa porque las avalanchas de alarmas sin sentido ocultan las reales.

En la LRWA, la guía de actuación ante un cambio inesperado de consigna es el medio por el que las alarmas de la pasarela llegan a las decisiones operativas. Cada nueva alarma se racionaliza antes de su puesta en marcha.

### 34.4 Interfaces organizativas

La seguridad de la infraestructura depende de organizaciones que usted no controla: el operador de LTE, el fabricante de las RTU, el integrador, la distribuidora eléctrica y las empresas de servicios vecinas para la ayuda mutua. Haga explícitas las interfaces en contratos y acuerdos: obligaciones de notificación de incidentes y vulnerabilidades, condiciones de acceso, tiempos de respuesta del soporte y ejercicios conjuntos. Un incidente en el operador de telecomunicaciones también es su incidente. Para la LRWA, el operador de LTE es el ejemplo más claro, ya que todo el conducto de campo del TMRP pasa por su red. El contrato debería fijar plazos de notificación y ejercicios conjuntos con condiciones medibles.

### 34.5 Ejemplo resuelto: la ráfaga de reconexión (sintético)

Durante las pruebas de integración, el equipo desconecta la cabecera LTE durante 30 minutos. Al reconectarse, cada una de las 42 pasarelas libera de golpe 180 lecturas almacenadas. El frontal del SCADA, dimensionado para el régimen estacionario, pone en cola la ráfaga; las alarmas prioritarias se retrasan más de dos minutos, lo que incumple R7. El modelo de colas del Lab 13 explica por qué: una utilización superior a 0,9 hace que el retardo se dispare. Corrección: las pasarelas reenvían de inmediato solo el valor más reciente y cualquier alarma, y después completan el histórico a una frecuencia limitada hacia el historiador, no hacia el sondeador del SCADA. La corrección se registra como un cambio de interfaz (revisión del ICD) y una prueba de regresión.

### 34.6 Actividad práctica

Diseñe una prueba de integración que combine la conmutación por error del SCADA con la protección contra repeticiones, indicando el comportamiento esperado, las observaciones y el criterio de aprobación. Describa la secuencia: un servidor SCADA conmuta a su pareja mientras las pasarelas siguen enviando mensajes autenticados. El comportamiento esperado es que el lado receptor siga rechazando las repeticiones tras la conmutación, lo que significa que el último contador aceptado de cada estación debe compartirse o persistirse. Observe si se acepta algún mensaje antiguo y si las alarmas siguen llegando en 60 segundos. El criterio de aprobación es cero repeticiones aceptadas y ninguna interrupción en la entrega de alarmas.

### 34.7 Errores comunes y límites

- Integración «de golpe» al final.
- Solo pruebas de interfaz, sin escenarios de sistema completo.
- Alarmas de seguridad sin procedimientos operativos.
- Contratos que no dicen nada sobre la notificación de incidentes ni la divulgación de vulnerabilidades.
- Tratar los problemas emergentes como el error de un componente en lugar de como un problema de interfaz.

La ráfaga de reconexión muestra el segundo y el último error: cada componente superó sus pruebas de interfaz y, sin embargo, juntos retrasaron las alarmas, y la corrección fue un cambio de interfaz, no un único error. La integración en la LRWA avanza interfaz por interfaz. Cada paso tiene su propia prueba de interfaz.

### Ejercicios — capítulo 34

**EX067 — Aritmética de la ráfaga.** *Objetivo:* cuantificar la ráfaga de reconexión. *Entradas:* 42 pasarelas × 180 lecturas liberadas en 10 s; el frontal del SCADA procesa 50 mensajes/s. *Pasos:* calcule el tiempo necesario para vaciar la ráfaga suponiendo que llega toda a la vez; calcule el tiempo que espera una alarma prioritaria situada al final de la cola; compárelo con R7. *Evidencia esperada:* cifras. *Rúbrica:* 3 = 7.560 mensajes / 50 por s = 151,2 s, incumple los 60 s, explica la cola con prioridad o la corrección del valor más reciente; 2 = aritmética correcta, sin corrección; 1 = aritmética errónea; 0 = nada.

**EX068 — Acuerdo con el operador de telecomunicaciones.** *Objetivo:* especificar una interfaz organizativa. *Entradas:* el contrato con el operador de LTE. *Pasos:* enumere seis cláusulas relevantes para la seguridad con condiciones medibles. *Evidencia esperada:* lista. *Rúbrica:* 3 = plazo de notificación de incidentes, divulgación de vulnerabilidades, notificación de mantenimientos, prioridades de restablecimiento, registro de accesos, ejercicio conjunto, con cifras; 2 = sin cifras; 1 = genérico; 0 = nada.

### Síntesis del capítulo

Integre de forma incremental, con pruebas de interfaz y escenarios de sistema completo, porque el comportamiento emergente solo aparece en combinación. Integre los controles en las operaciones mediante alarmas con sentido, guías de actuación y formación. Haga explícitas y medibles las interfaces organizativas; su seguridad depende de organizaciones que usted no controla.

<!-- open-cyber-academy:chapter-navigation:start ch-34 -->
### Siga estudiando — capítulo 34 de 50

[← Capítulo 33](#ch-33) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 35 →](#ch-35)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-35"></a>

## Capítulo 35 — Taller de diseño II

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) llevar un diseño desde el concepto hasta el diseño de detalle con una justificación cuantitativa; (2) integrar los análisis de confiabilidad, seguridad funcional, seguridad, desempeño y coste en un único argumento; (3) construir un argumento de aseguramiento estructurado que vincule las afirmaciones con la evidencia; y (4) defender las decisiones del diseño de detalle ante una revisión. Integra los capítulos 26–34 y prepara los capítulos 36–40.

### 35.1 Del concepto al diseño de detalle

El Taller I seleccionó un concepto. El Taller II lo detalla: componentes concretos, configuraciones, interfaces, procedimientos y verificación. Vuelven todas las cifras de los capítulos anteriores: tiempos de autonomía (capítulos 1 y 6), dimensionamiento de baterías (capítulo 3), tasas base (capítulo 7), latencia (capítulo 11), árbol de fallos (capítulo 23), métricas de detección (capítulo 29), disponibilidad (capítulo 32) y colas (avance del capítulo 36). Un diseño de detalle es coherente cuando estas cifras concuerdan entre sí y con los requisitos. En el TMRP, el dimensionamiento de las baterías, las 72 horas de operación automática local, la reserva de cuatro horas del hospital y el tiempo de recuperación deben contar la misma historia; el EX069 muestra qué ocurre cuando una de ellas no lo hace.

### 35.2 Argumentos de aseguramiento

Un **caso de aseguramiento** es un argumento estructurado de que un sistema cumple una afirmación, respaldado por evidencia. Tiene una afirmación principal («el TMRP mantiene abastecido al hospital en escenarios creíbles, incluida la falsificación de órdenes remotas»), subafirmaciones (cada requisito se cumple; los riesgos residuales son aceptables), argumentos (por qué las subafirmaciones respaldan la afirmación) y evidencia (resultados de pruebas, análisis, revisiones). El modelo de argumentación de Toulmin —afirmación, datos, garantía, respaldo, cualificador, refutación ([Toulmin, 1958/2003](https://doi.org/10.1017/CBO9780511840005))— es una lente útil: qué evidencia respalda la afirmación, por qué es pertinente y qué la derrotaría. Los **derrotadores** explícitos («salvo que el centro SCADA esté comprometido») mantienen honesto el argumento.

### 35.3 Encargo del Taller II (sintético)

Elabore el diseño de detalle de la fase 1 del TMRP (PS2, PS3, PS4 y Hollin Hill): lista de componentes con sus funciones de seguridad; listas de permitidos de zonas y conductos; procedimiento de gestión de claves; procedimientos de manual local y de conmutación por error; racionalización de las nuevas alarmas de seguridad; plan de verificación; y un caso de aseguramiento para la afirmación principal con al menos cuatro subafirmaciones y derrotadores identificados. El encargo abarca los cuatro activos que más importan para St Brenna's: PS2 como piloto probado, PS3 y Hollin Hill como la vía del depósito y PS4 como alimentación directa. Las estaciones restantes y la planta de Fenwick vienen en fases posteriores, de modo que el caso de aseguramiento de la fase 1 debe decir con claridad que todavía no las cubre.

### 35.4 Ejemplo resuelto: una rama del caso de aseguramiento (sintético)

*Subafirmación C2:* las órdenes remotas falsificadas no pueden causar la pérdida del suministro al hospital. *Argumento:* las órdenes requieren un MAC válido por estación (R1) y un contador reciente (R2); incluso las órdenes aceptadas no pueden llevar el proceso más allá de los límites locales (R3); la pérdida de ambas vías de suministro exige además que falle el depósito del hospital (árbol de fallos). *Evidencia:* T1 y T2 aprobadas (banco y aceptación en el emplazamiento en PS2); T3 aprobada en v2; análisis de condicionamiento del Lab 9; revisión independiente de la gestión de claves. *Derrotadores:* (D1) servidores SCADA comprometidos: las órdenes son auténticas; se mitiga con los límites locales y la aprobación por dos personas de los cambios masivos, con el riesgo residual aceptado por el director de operaciones; (D2) clave de estación extraída de una RTU robada: limitada a una estación, detección mediante la alarma de manipulación, procedimiento de rotación. *Cualificador:* la afirmación se sostiene para los escenarios del registro de riesgos v1.2; no para un ataque físico contra ambas estaciones de bombeo.

### 35.5 Actividad práctica

Redacte el caso de aseguramiento completo para el encargo del Taller II y preséntelo a un panel al que se le haya pedido encontrar derrotadores. Entregue al panel el encargo, su lista de componentes y el caso de aseguramiento, y pídale que encuentre qué derrotaría cada subafirmación. Registre cada derrotador que encuentre, lo hubiera enumerado usted o no, y redacte una respuesta: evidencia que lo aborde, un cambio de diseño o una aceptación explícita con un responsable. Se esperan derrotadores como un centro SCADA comprometido o una clave de RTU robada; la tarea del panel es encontrar los que usted pasó por alto, como el mal uso del modo manual local.

### 35.6 Errores comunes y límites

- Cifras incoherentes entre análisis.
- Casos de aseguramiento con afirmaciones sin evidencia, o con evidencia sin argumento.
- Derrotadores omitidos para que el caso parezca más sólido.
- Diseño de detalle que modifica los requisitos en silencio.

El EX069 es un ejemplo del primer error dentro del propio TMRP: R6 pide ocho horas, pero el ensayo de recuperación midió doce. Un caso que afirmara R6 citando el ensayo sería incoherente, de modo que el caso registra R6 como no cumplido y explica por qué la afirmación sobre el hospital puede seguir sosteniéndose gracias a la operación automática local.

### Ejercicios — capítulo 35

**EX069 — Comprobación de coherencia.** *Objetivo:* encontrar incoherencias entre análisis. *Entradas:* autonomía de las baterías de PS4 de 24 h (R5); reserva del hospital de 4 h; R6, restablecer la operación remota en 8 h; el ensayo del capítulo 47 muestra 12 h. *Pasos:* identifique qué afirmaciones entran en conflicto y qué significa el conflicto para el caso de aseguramiento. *Evidencia esperada:* análisis. *Rúbrica:* 3 = identifica que R6 no se cumple (12 > 8), que el suministro no depende de la operación remota (automático local), de modo que la afirmación sobre el hospital puede seguir sosteniéndose, y que el caso debe registrar R6 como fallido con un plan; 2 = parcial; 1 = no advierte lo de R6; 0 = nada.

**EX070 — Encuentre un derrotador.** *Objetivo:* cuestionar un argumento. *Entradas:* la subafirmación C2 del §35.4. *Pasos:* proponga otros dos derrotadores no enumerados y la evidencia o el cambio de diseño que respondería a cada uno. *Evidencia esperada:* dos derrotadores con sus respuestas. *Rúbrica:* 3 = derrotadores creíbles (p. ej., mal uso del modo manual local por un interno; compromiso del camino de actualización del firmware de la pasarela; fallo en la persistencia del contador) con respuestas específicas; 2 = uno débil; 1 = repite los ya enumerados; 0 = nada.

### Síntesis del capítulo

El diseño de detalle hace que todas las cifras anteriores encajen. Un caso de aseguramiento conecta la afirmación principal con la evidencia mediante argumentos explícitos, con los cualificadores y los derrotadores enunciados abiertamente. La coherencia entre análisis y la honestidad sobre los derrotadores son lo que hace defendible un diseño de detalle.

<!-- open-cyber-academy:chapter-navigation:start ch-35 -->
### Siga estudiando — capítulo 35 de 50

[← Capítulo 34](#ch-34) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 36 →](#ch-36)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-36"></a>

## Capítulo 36 — Infraestructura crítica y seguridad sectorial: desempeño y escala

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) modelar el rendimiento, la latencia y la utilización con la teoría de colas y la ley de Little; (2) estimar el coste en desempeño de los controles de seguridad; (3) dimensionar sistemas para condiciones de pico y degradadas, incluida la carga provocada por ataques; y (4) diseñar para la escala —flotas de miles de dispositivos— en la gestión de claves, la supervisión y las actualizaciones. Se apoya en los capítulos 11, 19 y 34 y prepara el capítulo 41.

### 36.1 Colas por todas partes

Los mensajes esperan en colas en pasarelas, servidores y enlaces. La [ley de Little](https://doi.org/10.1287/opre.9.3.383), $L = \lambda W$, relaciona el número medio en un sistema $L$, la tasa de llegadas $\lambda$ y el tiempo medio en el sistema $W$, en condiciones muy generales. Para el modelo sencillo M/M/1 (llegadas aleatorias, servicio exponencial, un servidor con tasa de servicio $\mu$), la utilización es $\rho = \lambda/\mu$ y $W = 1/(\mu - \lambda)$. El retardo crece sin límite cuando $\rho \to 1$: con una utilización del 80 %, el mensaje medio pasa cinco tiempos de servicio en el sistema; con el 96 %, veinticinco. Dimensione de modo que la utilización de pico se mantenga muy por debajo de 1, habitualmente por debajo de 0,7 en los caminos críticos para la latencia.

### 36.2 El coste de la seguridad

Todo control cuesta algo: bytes (la sobrecarga de 22 bytes del Lab 8), CPU (cálculo de MAC, negociaciones TLS), latencia (decisiones de política, inspección) y tiempo de los operadores (reautenticación, aprobaciones). Mídalos en el banco. Los costes suelen ser pequeños en comparación con los tiempos de ida y vuelta de la red, pero importan en enlaces limitados (radio de bajo ancho de banda), en dispositivos limitados (microcontroladores pequeños) y a escala. En el TMRP, los costes medidos incluyen los veintidós bytes adicionales por trama, el cálculo del MAC de cada mensaje en el verificador del lado del SCADA y el tiempo de los operadores para la aprobación por dos personas de los cambios masivos de consignas. Ninguno es grande, pero el límite de rendimiento del verificador es lo que el ejemplo resuelto debe dimensionar.

### 36.3 Carga de pico, degradada y de ataque

Dimensione para la peor carga creíble: avalanchas de alarmas durante tormentas, ráfagas de reconexión tras cortes (capítulo 34), recuperación del retraso tras una conmutación por error e inundaciones deliberadas. Un atacante que puede enviar tráfico a una pasarela puede llevar la utilización hacia 1 y retrasar las alarmas legítimas; las defensas incluyen límites de frecuencia por origen, colas con prioridad para las alarmas, rechazo temprano del tráfico no autenticado (verifique primero la comprobación barata) y márgenes de capacidad. En el TMRP, la ráfaga de reconexión encontrada en las pruebas de integración es el ejemplo más claro, y la cola con prioridad para las alarmas del verificador es la defensa elegida en el ejemplo resuelto.

### 36.4 Escala

A escala de flota, los procesos manuales fallan. El registro, la rotación y la revocación de claves deben automatizarse, con auditoría; la supervisión debe agregar y priorizar; las actualizaciones deben hacerse por etapas y ser observables; el inventario debe conciliarse de forma continua. Un procedimiento que lleva 30 minutos por dispositivo consume 500 horas de trabajo del personal, unos tres meses de un ingeniero a tiempo completo, para mil dispositivos. La LRWA tiene hoy solo 42 estaciones de campo, pero el mismo diseño puede usarse más adelante para una flota mucho mayor, de modo que el TMRP automatiza desde el principio los registros de alta y rotación de claves, en lugar de depender de una hoja de cálculo mantenida por un único ingeniero.

### 36.5 Ejemplo resuelto: dimensionamiento de la pasarela (sintético)

El verificador del lado del SCADA puede procesar 50 mensajes/s. En régimen estacionario, las 42 estaciones de la LRWA generan unos 20 mensajes/s ($\rho = 0.4$, $W \approx 33$ ms). Durante una tormenta, las alarmas elevan las llegadas a 40/s ($\rho = 0.8$, $W = 100$ ms, unos 4 mensajes en el sistema). A 48/s, $W = 500$ ms y hay de media 24 mensajes en el sistema. El sondeo secuencial de 42 estaciones con 180 ms de ida y vuelta más el tiempo de registros dura 7,8 s por ciclo; seis canales en paralelo lo reducen a 1,3 s. Decisiones: duplicar la capacidad del verificador hasta 100 mensajes/s para tener margen; cola con prioridad para las alarmas; notificación por excepción de las alarmas en lugar de esperar al sondeo.

### 36.6 Actividad práctica: Lab 13

```python
# Lab 13 - is the telemetry gateway fast enough? M/M/1 and a polling cycle (synthetic, offline)
mu = 50.0                                    # messages/s the gateway can verify and forward
for lam in (20.0, 40.0, 45.0, 48.0):
    rho = lam / mu; W = 1 / (mu - lam); L = lam * W
    print(f"lambda={lam:>4} rho={rho:.2f} W={W*1000:6.1f} ms L={L:5.1f} msgs")
stations, regs_per_poll, rtt_ms, per_reg_ms = 42, 3, 180, 2
cycle = stations * (rtt_ms + regs_per_poll * per_reg_ms)
print(f"sequential polling cycle: {cycle/1000:.2f} s; with 6 parallel channels: {cycle/6/1000:.2f} s")
```

Salida esperada:

```text
lambda=20.0 rho=0.40 W=  33.3 ms L=  0.7 msgs
lambda=40.0 rho=0.80 W= 100.0 ms L=  4.0 msgs
lambda=45.0 rho=0.90 W= 200.0 ms L=  9.0 msgs
lambda=48.0 rho=0.96 W= 500.0 ms L= 24.0 msgs
sequential polling cycle: 7.81 s; with 6 parallel channels: 1.30 s
```

Las cuatro primeras líneas muestran cómo el retardo crece con fuerza a medida que las llegadas se acercan a la capacidad del verificador, de cincuenta mensajes por segundo: a veinte mensajes por segundo, el mensaje medio espera aproximadamente un tercio de décima de segundo, mientras que a cuarenta y ocho espera medio segundo y hay dos docenas de mensajes en el sistema. Las líneas de sondeo muestran por qué la LRWA usa seis canales en paralelo: un ciclo secuencial de casi ocho segundos dejaría las alarmas esperando mucho antes de que llegaran al verificador.

### 36.7 Errores comunes y límites

- Dimensionar para la carga media.
- Ignorar que el retardo se dispara cerca de la utilización plena.
- Suponer que los costes de seguridad son despreciables sin medirlos en el dispositivo de destino.
- Procedimientos manuales que no escalan.
- Usar M/M/1 cuando las llegadas llegan en ráfagas o el servicio es determinista; trátelo como una primera aproximación.

El dimensionamiento del TMRP evita los dos primeros errores al dimensionar para la carga de tormenta y mantener el verificador duplicado muy por debajo de la utilización plena, y trata los resultados de colas como una primera aproximación que debe contrastarse con mediciones en el banco.

### Ejercicios — capítulo 36

**EX071 — Duplicar la capacidad.** *Objetivo:* cuantificar el margen. *Entradas:* Lab 13 con $\mu = 100$. *Pasos:* calcule $\rho$, $W$ y $L$ a 20, 40 y 48 mensajes/s; compárelos con $\mu = 50$. *Evidencia esperada:* tabla. *Rúbrica:* 3 = valores correctos (p. ej., a 48/s: ρ = 0,48, W ≈ 19,2 ms, L ≈ 0,92) y conclusión; 2 = un error; 1 = una sola tasa; 0 = nada.

**EX072 — Defensa contra inundaciones.** *Objetivo:* diseñar frente a la carga de ataque. *Entradas:* un atacante en la red LTE puede enviar 1.000 tramas falsificadas/s al verificador. *Pasos:* proponga tres defensas en orden de coste y explique cómo protege cada una la latencia de las alarmas. *Evidencia esperada:* lista. *Rúbrica:* 3 = filtrado a nivel de red por origen o túnel, comprobaciones previas baratas antes del MAC, límites de frecuencia por origen y colas con prioridad, con razonamiento sobre dónde se descarta la carga; 2 = una sola defensa; 1 = solo «añadir capacidad»; 0 = nada.

### Síntesis del capítulo

Las colas gobiernan la latencia; la ley de Little y los modelos de colas sencillos muestran que el retardo se dispara cuando la utilización se acerca a uno. Mida los costes de los controles de seguridad, dimensione para la carga de pico, degradada y de ataque con prioridad para las alarmas, y automatice desde el principio los procesos a escala de flota.

<!-- open-cyber-academy:chapter-navigation:start ch-36 -->
### Siga estudiando — capítulo 36 de 50

[← Capítulo 35](#ch-35) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 37 →](#ch-37)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-37"></a>

## Capítulo 37 — Infraestructura crítica y seguridad sectorial: operaciones

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) diseñar operaciones de seguridad para la TO: supervisión, clasificación, escalado y coordinación con las operaciones del proceso; (2) redactar procedimientos operativos y guías de actuación que los operadores puedan ejecutar bajo presión; (3) gestionar los cambios, los accesos y las vulnerabilidades en las operaciones diarias; y (4) aprender de los incidentes y de los cuasiincidentes sin culpabilizar. Se apoya en los capítulos 18, 29 y 34 y prepara los capítulos 38 y 47.

### 37.1 Operaciones de seguridad en la TO

La supervisión de seguridad de la TO vigila el tráfico de red, los registros y los datos del proceso en busca de indicios de uso indebido. La clasificación en la TO difiere de la de TI: la primera pregunta no es «¿es esto malicioso?», sino «¿está seguro el proceso?». Por eso, las vías de escalado llegan a la sala de control y al jefe de operaciones de turno, además de al personal de seguridad. Muchas empresas de servicios no tienen un equipo de seguridad 24/7; la sala de control sí está atendida 24/7 y debe poder actuar ante las alarmas de seguridad con guías de actuación claras, escalando a especialistas de seguridad de guardia.

### 37.2 Guías de actuación

Una guía de actuación es un procedimiento breve y probado para una situación concreta: desencadenante, acciones de seguridad inmediatas, información que recopilar, decisiones y quién las toma, comunicaciones y vuelta a la normalidad. Escriba para un operador cansado a las 03:00: pasos numerados, puntos de decisión claros, números de teléfono, sin jerga. Pruebe cada guía en ejercicios y actualícela después de cada uso. Las orientaciones sobre gestión de incidentes como [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) ofrecen una estructura general; las guías de TO añaden pasos de seguridad del proceso.

La guía de actuación de la LRWA ante un cambio inesperado de consigna está redactada conforme a este criterio.

### 37.3 Gestión de cambios, accesos y vulnerabilidades

Las operaciones diarias mantienen el sistema en su estado de diseño: gestión de cambios (ningún cambio de configuración sin aprobación y registro); gestión de accesos (altas, cambios de puesto y bajas; sesiones de fabricantes aprobadas para cada uso); gestión de vulnerabilidades (seguir avisos como los [avisos ICS de la CISA](https://www.cisa.gov/news-events/ics-advisories), evaluar su aplicabilidad, planificar la corrección, capítulo 12). La deriva —la acumulación de cambios no documentados— es la forma más común en que un sistema bien diseñado se vuelve inseguro.

En la LRWA, el script olvidado de informes corporativos que apareció en la revisión de flujos es un ejemplo de deriva, y el control de cambios en cada conducto es la forma en que el TMRP impide que esas vías reaparezcan.

### 37.4 Aprender sin culpabilizar

Los incidentes y los cuasiincidentes son evidencia sobre el sistema. [Reason (2000)](https://doi.org/10.1136/bmj.320.7237.768) contrastó el enfoque centrado en la persona (culpar a los individuos) con el enfoque sistémico (defensas, barreras y condiciones latentes), y sostuvo que este último es más eficaz. Las revisiones posteriores a la acción preguntan qué ocurrió, por qué tenía sentido para las personas implicadas en aquel momento, qué defensas funcionaron o fallaron y qué va a cambiar. La culpa reprime la notificación, y los cuasiincidentes no notificados son lecciones perdidas.

En la LRWA, el técnico que conectó un portátil a la red de PS3 en el EX074 recibe este trato: la revisión pregunta por qué el servidor de salto le parecía demasiado lento y qué hizo posible el atajo.

### 37.5 Ejemplo resuelto: guía de actuación «cambio inesperado de consigna» (sintético)

*Desencadenante:* el SCADA muestra un cambio de consigna en cualquier estación que no coincide con una acción del operador en los últimos 5 minutos, o una pasarela registra fallos de MAC repetidos. *Acciones de seguridad inmediatas:* (1) contraste los valores del proceso de la estación con mediciones independientes; (2) si están fuera del rango normal, restablezca localmente la consigna anterior o pase a manual local a través del técnico de turno; (3) no desactive la telemetría remota. *Recopilar:* estación, hora, valores anterior y nuevo, extracto del registro de la pasarela, registro del operador. *Decidir:* el jefe de turno decide si desactiva las escrituras remotas en toda la flota (conmutador de configuración de las pasarelas). *Comunicar:* al responsable de seguridad de guardia en 30 minutos; al enlace con el hospital si PS3 o PS4 están afectadas. *Vuelta a la normalidad:* las escrituras remotas se reactivan solo cuando el responsable de seguridad de guardia está de acuerdo.

### 37.6 Actividad práctica

Ejecute la guía de actuación en un ejercicio de mesa con una secuencia guionizada de inyecciones (primero un único cambio de consigna, luego fallos de MAC en una segunda estación y, por último, una llamada del hospital por presión baja). Registre los tiempos de decisión y las ambigüedades, y revise la guía. Ejecute las inyecciones en orden y anote la hora de cada decisión. Observe en particular si el equipo mantiene en funcionamiento la telemetría remota, como exige la guía, y si el jefe de turno decide desactivar las escrituras remotas en toda la flota antes de que llegue la llamada del hospital. Registre cada punto en el que alguien preguntó qué quería decir la guía. Después del ejercicio de mesa, reescriba esos pasos y programe una segunda ejecución para comprobar las revisiones.

### 37.7 Errores comunes y límites

- Alarmas de seguridad dirigidas a un equipo que no está de servicio cuando saltan.
- Guías de actuación escritas para expertos y nunca probadas.
- Gestión de cambios eludida «temporalmente».
- Revisiones posteriores a la acción que terminan en «error del operador».

El diseño de la guía de la LRWA responde a estos errores: las alarmas de seguridad llegan a la sala de control, que está atendida a todas horas, y se llama al responsable de seguridad de guardia en 30 minutos. La guía se prueba en ejercicios de mesa, y el control de cambios no admite excepciones temporales. Las revisiones posteriores a la acción de la LRWA buscan condiciones latentes, como un servidor de salto lento, en lugar de terminar en un error del operador.

### Ejercicios — capítulo 37

**EX073 — Revisión de la guía de actuación.** *Objetivo:* mejorar una guía de actuación. *Entradas:* §37.5. *Pasos:* identifique tres debilidades (p. ej., umbrales ambiguos, contactos que faltan, un valor por defecto inseguro) y reescriba los pasos afectados. *Evidencia esperada:* pasos revisados. *Rúbrica:* 3 = debilidades sustanciales corregidas con pasos ejecutables; 2 = cambios cosméticos; 1 = solo crítica; 0 = nada.

**EX074 — Revisión de un cuasiincidente.** *Objetivo:* realizar una revisión sin culpabilizar. *Entradas:* un técnico conectó un portátil a la red de control de PS3 para descargar registros, eludiendo el servidor de salto; el portátil no se había analizado. No hubo incidente posterior. *Pasos:* redacte una revisión de una página: qué ocurrió, por qué tenía sentido, qué defensas fallaron y qué cambios del sistema se proponen. *Evidencia esperada:* revisión. *Rúbrica:* 3 = explica la racionalidad local (servidor de salto lento, plazo), identifica las condiciones latentes (sin seguridad de puertos, sin una vía sencilla para los registros) y propone cambios del sistema; 2 = algo de culpa; 1 = «volver a formar al técnico»; 0 = nada.

### Síntesis del capítulo

Las operaciones de seguridad de la TO empiezan por la seguridad del proceso y encauzan el escalado a través de la sala de control. Las guías de actuación deben ser breves, estar probadas y poder ejecutarse bajo presión. La gestión diaria de cambios, accesos y vulnerabilidades mantiene el sistema tal como se diseñó, y el aprendizaje sin culpabilizar a partir de incidentes y cuasiincidentes mejora las defensas.

<!-- open-cyber-academy:chapter-navigation:start ch-37 -->
### Siga estudiando — capítulo 37 de 50

[← Capítulo 36](#ch-36) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 38 →](#ch-38)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-38"></a>

## Capítulo 38 — Infraestructura crítica y seguridad sectorial: validación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) distinguir la validación (el sistema adecuado para la necesidad) de la verificación (el sistema construido conforme a su especificación); (2) validar con las partes interesadas mediante demostraciones, ensayos operativos y ejercicios; (3) usar la trazabilidad para mostrar qué necesidades están respaldadas por evidencia y cuáles no; y (4) informar con honestidad de los resultados de la validación, incluidos los resultados parciales. Se apoya en los capítulos 16, 24 y 30 y prepara los capítulos 40 y 48.

### 38.1 La verificación no es validación

Un sistema puede superar todas las pruebas frente a su especificación y aun así fallar a sus usuarios si la especificación era errónea o incompleta. La validación pregunta si el sistema satisface las necesidades de las partes interesadas en su entorno previsto: ¿pueden los operadores manejar de verdad el modo manual local de noche? ¿Recibe de verdad el hospital agua dentro de su reserva cuando se pierde PS4? La evidencia de validación procede del uso realista: ensayos operativos, demostraciones con las partes interesadas, ejercicios y primeros datos de operación.

Para el TMRP, el ejercicio nocturno del modo manual local es la actividad de validación que responde a la primera pregunta.

### 38.2 La trazabilidad como mapa de evidencia

Trace las necesidades hasta los requisitos, los requisitos hasta las pruebas y las pruebas hasta los resultados. Después, haga tres preguntas: ¿qué requisitos no tienen prueba (afirmaciones no probadas)? ¿Qué pruebas fallaron o no se ejecutaron (afirmaciones no respaldadas)? ¿Qué necesidades dependen solo de requisitos que aún no están verificados (necesidades no validadas)? El laboratorio 14 calcula estas respuestas para el expediente del TMRP. Para el TMRP, las preguntas son concretas. R4 no tiene prueba porque su demostración nunca se programó. R9, la alarma independiente de dosificación, no tiene ninguna prueba: la tabla de requisitos indica una prueba como método de verificación, pero nunca se escribió una prueba para él. La única prueba registrada de R3 es la que falló en v1, y la prueba de R8 no se ha ejecutado. N1 depende de R4, por lo que no puede declararse validada hasta que se realice el ejercicio nocturno. El laboratorio 14 imprime estas lagunas directamente.

### 38.3 Validación con las partes interesadas

Implique a las personas a las que sirve el sistema. Los operadores validan los procedimientos y las pantallas; el personal de mantenimiento valida la reparabilidad y los repuestos; el hospital valida que las disposiciones de suministro satisfacen sus necesidades; los reguladores validan el razonamiento de cumplimiento. Registre sus hallazgos como registraría los hallazgos de una revisión, con respuestas. Para el TMRP, los operadores validan el procedimiento manual local y las nuevas alarmas de seguridad, el personal de mantenimiento comprueba que las pasarelas pueden sustituirse con repuestos, y el hospital confirma que las disposiciones de suministro y su reserva de cuatro horas satisfacen sus necesidades. Sus hallazgos se incorporan al mismo registro de respuestas que los hallazgos de la revisión de diseño.

### 38.4 Informar de resultados parciales

Informe del estado de validación por necesidad: validada, parcialmente validada (con lo que falta) o no validada. No redondee al alza. «N1 parcialmente validada: el ensayo de pérdida de PS4 cumplió la reserva de 4 h; la pérdida combinada de PS4 y del alimentador F1 de la red aún no se ha ensayado». El mapa de evidencia del TMRP lo hace concreto: N1 depende de R4, que aún no se ha demostrado, por lo que N1 se declara no validada hasta que se realice el ejercicio nocturno, aunque la mayoría de sus demás requisitos hayan superado sus pruebas. El estado se actualiza después del ejercicio.

### 38.5 Ejemplo resuelto: mapa de evidencia del TMRP (sintético)

El laboratorio 14 muestra: R4 (operación manual local) no tiene prueba; se planificó como demostración y nunca se programó; R3 tiene una prueba fallida (en v1; la repetición de la prueba en v2 aún no se ha introducido en la matriz); la prueba T6 de R8 no se ha ejecutado. R9 (alarma independiente de dosificación) tampoco tiene prueba: su método de verificación es «Prueba», pero nunca se le asignó un identificador de prueba, de modo que la evidencia de que dispone es una intención de diseño, no un resultado. Verificados: 5 de 9 requisitos (55,6 %). Consecuencia para la validación: N1 (suministro al hospital) depende de R4, por lo que N1 no puede declararse validada; el ejercicio nocturno de operación manual local se programa como actividad de validación. La matriz también pone al descubierto una laguna administrativa (debe registrarse la repetición de T3 en v2), que es exactamente el tipo de incoherencia que encuentran los examinadores y los auditores.

### 38.6 Actividad práctica: laboratorio 14

```python
# Lab 14 - requirements traceability: what is claimed but not shown? (synthetic TMRP dossier, offline)
REQS = ["R1 auth telemetry", "R2 replay reject", "R3 setpoint bounds", "R4 local manual", "R5 24h hold-up",
        "R6 restore 8h", "R7 alarm 60s", "R8 log integrity", "R9 dosing alarm"]
TESTS = {"T1": ["R1"], "T2": ["R1", "R2"], "T3": ["R3"], "T4": ["R5"], "T5": ["R7"], "T6": ["R8"], "T7": ["R6"]}
RESULT = {"T1": "pass", "T2": "pass", "T3": "fail", "T4": "pass", "T5": "pass", "T6": "not run", "T7": "pass"}
ids = [r.split()[0] for r in REQS]
cov = {r: [t for t, rs in TESTS.items() if r in rs] for r in ids}
verified = [r for r in ids if cov[r] and all(RESULT[t] == "pass" for t in cov[r])]
print("untested:", [r for r in ids if not cov[r]])
print("tested but not passing:", [r for r in ids if cov[r] and r not in verified])
print(f"verified {len(verified)}/{len(ids)} = {100*len(verified)/len(ids):.1f}%")
```

Salida esperada:

```text
untested: ['R4', 'R9']
tested but not passing: ['R3', 'R8']
verified 5/9 = 55.6%
```

La salida muestra que R4 y R9 no tienen prueba, que R3 y R8 están probados pero no superan las pruebas, y que cinco de los nueve requisitos están verificados. El estado de R3 está desactualizado más que realmente fallido: la repetición de la prueba en v2 se superó, pero nadie la introdujo en la matriz, que es exactamente la laguna administrativa sobre la que advierte el ejemplo resuelto. El EX075 actualiza el mapa. R9 es la lección más difícil: la alarma de dosificación aparece en el conjunto de requisitos, en la tabla de riesgos y en los controles de dosificación, así que parece cubierta, y sin embargo nunca se le asignó una prueba. Una versión anterior de esta matriz omitía R9 por completo de la lista, lo que elevaba la proporción verificada de cinco de nueve a cinco de ocho sin ninguna evidencia nueva. Una matriz debe enumerar todos los requisitos definidos, porque un requisito que omite no puede declararse como no probado.

### 38.7 Errores comunes y límites

- Llamar «validación» a un conjunto de pruebas superado.
- Partes interesadas consultadas solo al principio.
- Redondear una validación parcial al alza hasta «validada».
- Mapas de evidencia que no se actualizan tras repetir las pruebas.

El propio mapa del TMRP muestra el último error: la repetición de T3 en v2 se superó, pero la matriz nunca se actualizó. Las partes interesadas, como los operadores y el hospital, participan durante todo el proceso, no solo cuando se redactaron los requisitos, y el mapa de evidencia se actualiza cada vez que una repetición de prueba o una demostración produce un resultado, de modo que el estado de validación declarado nunca se adelanta a la evidencia.

### Ejercicios — capítulo 38

**EX075 — Actualizar el mapa.** *Objetivo:* mantener la trazabilidad. *Entradas:* laboratorio 14. *Pasos:* (1) añada T3b (repetición de la prueba en v2) que cubre R3 con resultado «pass» y elimine el vínculo de T3 con R3 por quedar sustituido; (2) añada la demostración T8 que cubre R4 con resultado «pass»; (3) ejecute T6 con resultado «pass»; vuelva a calcular. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = ocho de nueve verificados (88,9 %), R9 sigue figurando como no probado porque no existe una prueba de la alarma de dosificación, con una nota de que verificación ≠ validación; 2 = falta un cambio; 1 = no ejecutado; 0 = nada.

**EX076 — Plan de validación para N1.** *Objetivo:* planificar la validación con las partes interesadas. *Entradas:* N1 «el hospital no debe quedarse sin agua > 4 h». *Pasos:* proponga dos actividades de validación con partes interesadas, condiciones realistas, observaciones y criterios de éxito. *Evidencia esperada:* plan. *Rúbrica:* 3 = actividades realistas (ejercicio nocturno de operación manual local con la plantilla real; aislamiento planificado de PS4 con supervisión del hospital), criterios ligados a la reserva de 4 h, partes interesadas nombradas por su función; 2 = criterios vagos; 1 = pruebas rebautizadas como validación; 0 = nada.

### Síntesis del capítulo

La verificación pregunta si el sistema se construyó bien; la validación pregunta si es el sistema adecuado. Use la trazabilidad como mapa de evidencia para encontrar afirmaciones no probadas, no respaldadas y no validadas, valide con las personas a las que sirve el sistema en condiciones realistas e informe de los resultados parciales como parciales.

<!-- open-cyber-academy:chapter-navigation:start ch-38 -->
### Siga estudiando — capítulo 38 de 50

[← Capítulo 37](#ch-37) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 39 →](#ch-39)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-39"></a>

## Capítulo 39 — Infraestructura crítica y seguridad sectorial: mantenibilidad

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) diseñar para la mantenibilidad a lo largo de ciclos de vida largos: actualizaciones, repuestos, competencias y documentación; (2) gestionar la deuda técnica y la obsolescencia en la TO; (3) planificar la agilidad criptográfica y la transición a la criptografía poscuántica; y (4) planificar de forma segura la retirada de servicio. Se apoya en los capítulos 8, 14 y 31 y prepara los capítulos 41 y 44.

### 39.1 Ciclos de vida largos

Los activos de infraestructura duran décadas; el software y las amenazas cambian en meses. La mantenibilidad significa que el sistema puede mantenerse seguro y funcional durante toda su vida: componentes sustituibles sin rediseño; actualizaciones posibles sin interrupciones largas; documentación al día; competencias disponibles. Entre las decisiones de diseño que perjudican la mantenibilidad están los protocolos propietarios con un único proveedor, el código a medida sin documentar y el hardware sin vía de actualización. Para el TMRP, las RTU que se instalan ahora pueden seguir funcionando en la década de 2040, de modo que el diseño de las pasarelas, el formato de los mensajes y la gestión de claves deben ser mantenibles durante todo ese periodo.

### 39.2 Deuda técnica y obsolescencia

La deuda técnica es el coste futuro de los atajos que se toman ahora: una configuración codificada de forma fija, una prueba omitida, una pasarela construida «temporalmente» para RTU heredadas. Registre los elementos de deuda con su responsable, el coste de corregirlos y el riesgo de dejarlos. La gestión de la obsolescencia sigue las fechas de fin de venta y de fin de soporte de cada componente y planifica la sustitución antes de que termine el soporte, manteniendo repuestos cuando la sustitución es lenta.

Las pasarelas del TMRP para las unidades RTU-A heredadas de PS1 y PS2 se registran como deuda con un horizonte de tres años. Los repuestos se compran antes del fin de venta.

### 39.3 Agilidad criptográfica

Los algoritmos se debilitan y las normas cambian. La agilidad criptográfica es la capacidad de cambiar algoritmos y tamaños de clave sin rediseñar el sistema: identificadores de algoritmo en los formatos de mensaje, vías de actualización del firmware y una gestión de claves capaz de aprovisionar nuevos tipos de clave. El NIST publicó sus primeras normas de criptografía poscuántica (FIPS 203, 204 y 205) en agosto de 2024 ([anuncio del NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)); el equipamiento de infraestructura que se compra ahora puede seguir funcionando cuando sean plausibles adversarios con capacidad cuántica, por lo que los mecanismos de clave pública de los dispositivos de vida larga necesitan una vía de migración. Los MAC simétricos como HMAC-SHA256 se ven mucho menos afectados; es en el intercambio de claves y en las firmas donde la migración importa.

### 39.4 Retirada de servicio segura

Los dispositivos retirados contienen claves, configuraciones y detalles de la red. Pasos de la retirada de servicio: revocar claves y certificados; eliminar cuentas; borrar o destruir el almacenamiento según la política; actualizar el inventario, los modelos y las listas de permitidos; y eliminar las reglas de cortafuegos que daban servicio al dispositivo. Las reglas obsoletas de dispositivos retirados son una vía clásica para los atacantes que colocan un dispositivo nuevo en una dirección antigua. La revisión de mantenibilidad del TMRP constató que no existía un procedimiento de retirada de servicio, así que se redactó uno y se vinculó a la gestión de cambios. Se usará por primera vez cuando se sustituyan la RTU-A heredada de PS2 y su pasarela, como describe el EX078.

### 39.5 Ejemplo resuelto: revisión de mantenibilidad del TMRP (sintético)

La revisión constata: (1) las pasarelas de PS1/PS2 son deuda técnica con un horizonte de tres años, registrada con un plan de sustitución; (2) el formato de mensaje del laboratorio 8 carece de identificador de algoritmo: se modifica para incluir un ID de conjunto de un byte (versión 1 = HMAC-SHA256-128) antes del despliegue en la flota, con un coste de un byte por mensaje; (3) la firma del firmware de la RTU-B usa un esquema de firma clásico: se pide al fabricante, como condición contractual, una hoja de ruta de migración poscuántica; (4) no se mantienen módems LTE de repuesto y el modelo llega al fin de venta el año próximo: se compran repuestos ahora y se planifica la sustitución; (5) falta el procedimiento de retirada de servicio: se redacta y se vincula a la gestión de cambios.

### 39.6 Actividad práctica

Construya un registro de obsolescencia para los componentes del TMRP (RTU, pasarelas, módems, servidores SCADA, sistema operativo, HSM) con fechas supuestas, estado del soporte, repuestos disponibles y plan de sustitución. Incluya todos los componentes que menciona la revisión del TMRP: RTU-A y RTU-B, las pasarelas, los módems LTE, los servidores SCADA y su sistema operativo, y el módulo de seguridad de hardware. Para cada uno, registre las fechas supuestas de fin de venta y de fin de soporte, los repuestos disponibles y el plan de sustitución. Señale cualquier componente cuyo soporte termine antes de su sustitución prevista, como constató la revisión para los módems LTE. Mantenga el registro bajo control de cambios para que siga al día.

### 39.7 Errores comunes y límites

- Diseños que requieren al proveedor original para siempre.
- Deuda técnica que no se registra.
- Formatos de mensaje sin versionado ni identificadores de algoritmo.
- Dispositivos retirados que dejan atrás claves y reglas de cortafuegos.

La revisión del TMRP encontró el tercer error en la trama del laboratorio 8 y lo corrigió con un identificador de conjunto de un byte antes del despliegue en la flota. También registró las pasarelas heredadas como deuda y redactó el procedimiento de retirada de servicio que faltaba. Los módems LTE de repuesto se compran antes del fin de venta del modelo. El nuevo procedimiento revoca las claves y elimina las reglas de cortafuegos obsoletas.

### Ejercicios — capítulo 39

**EX077 — Incorporar agilidad.** *Objetivo:* añadir agilidad criptográfica. *Entradas:* formato de trama del laboratorio 8. *Pasos:* añada un ID de conjunto de un byte y una política del receptor que acepte solo los conjuntos configurados; muestre cómo podría introducirse el conjunto 2 (un MAC diferente) durante un periodo de transición y cómo se retiraría el conjunto 1. *Evidencia esperada:* diseño y un breve esbozo de código. *Rúbrica:* 3 = ID de conjunto autenticado (dentro del MAC), política de conjuntos permitidos por estación, prevención de la degradación, paso de retirada; 2 = ID de conjunto no autenticado; 1 = solo descripción; 0 = nada.

**EX078 — Lista de comprobación de retirada de servicio.** *Objetivo:* retirar un dispositivo de forma segura. *Entradas:* la RTU-A heredada de PS2 y su pasarela, que se sustituyen por una RTU-B. *Pasos:* redacte una lista de comprobación de al menos ocho pasos con la evidencia de cada uno. *Evidencia esperada:* lista de comprobación. *Rúbrica:* 3 = claves revocadas, cuentas eliminadas, almacenamiento borrado, inventario/modelo/lista de permitidos actualizados, reglas de cortafuegos eliminadas, líneas base de supervisión actualizadas, destino de los repuestos, aprobación final; 2 = faltan las reglas o las claves; 1 = genérica; 0 = nada.

### Síntesis del capítulo

Diseñe para décadas: componentes sustituibles, software actualizable, documentación al día, competencias disponibles. Registre la deuda técnica, gestione la obsolescencia antes del fin del soporte, incorpore la agilidad criptográfica en los formatos y en las vías de actualización con un plan de migración poscuántica, y retire los dispositivos de modo que nada (claves, cuentas, reglas) sobreviva al dispositivo.

<!-- open-cyber-academy:chapter-navigation:start ch-39 -->
### Siga estudiando — capítulo 39 de 50

[← Capítulo 38](#ch-38) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 40 →](#ch-40)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-40"></a>

## Capítulo 40 — Laboratorio de verificación II

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) diseñar y ejecutar una campaña de inyección de fallos con semilla contra un control de seguridad; (2) clasificar los resultados y calcular las tasas de detección por clase de fallo; (3) encontrar las lagunas entre lo que detecta un control y lo que necesita un requisito; y (4) informar de una campaña de forma reproducible. Amplía el capítulo 30 a los fallos del entorno y a los ataques y prepara el proyecto final (capítulos 44–47).

### 40.1 Inyección de fallos

La inyección de fallos introduce deliberadamente fallos (mensajes corrompidos, descartados, retrasados, reproducidos o reordenados; reinicios de procesos; saltos de reloj; agotamiento de recursos) para observar cómo se comporta un sistema. Pone a prueba el tratamiento de errores al que las pruebas ordinarias rara vez llegan. Una campaña especifica el modelo de fallos (qué fallos y con qué tasas), el sistema bajo prueba, el oráculo (cuál es el comportamiento correcto ante cada fallo) y las mediciones. Para el TMRP, la campaña sobre el receptor de este capítulo inyecta corrupción, reproducción, retraso y descartes. Cada fallo tiene un oráculo. Los resultados se cuentan por clase.

### 40.2 Oráculos y clasificación

Para cada fallo inyectado, defina el resultado esperado: corrompido → rechazado como corrupto; reproducido → rechazado como reproducción; retrasado más allá de la ventana de frescura → rechazado como obsoleto; descartado → detectado como un hueco (o no, si el diseño no detecta huecos). Clasifique los resultados observados frente a los esperados. Un fallo que produce «ok» cuando debería haberse rechazado es un **fallo silencioso**, la clase más importante que hay que encontrar. Para el receptor del TMRP, la clase de descartes es aquella en la que el oráculo puso al descubierto una laguna: el diseño no tenía un resultado esperado para un mensaje perdido, porque nadie había preguntado qué debía ocurrir.

### 40.3 Semillas, tasas y cobertura

Fije la semilla del generador de fallos, regístrela e informe de los recuentos por clase de fallo. Elija tasas que produzcan suficientes eventos de cada clase para que sean significativos; una campaña de 500 mensajes con un 5 % por clase de fallo da unos 25 eventos de cada una, suficientes para encontrar fallos sistemáticos, pero no para estimar con precisión los raros. Amplíe la campaña para las clases que preocupen especialmente. La campaña del TMRP usa la semilla cuarenta, quinientos mensajes y un cinco por ciento por clase de fallo, de modo que cada clase produce suficientes eventos para mostrar un comportamiento sistemático. El proyecto final amplía la campaña a diez mil mensajes en siete clases de fallo, incluidos el reinicio y la reordenación.

### 40.4 Ejemplo resuelto: campaña sobre el receptor de telemetría (sintético)

El laboratorio 15 envía 500 mensajes con la semilla 40; cada uno tiene un 80 % de probabilidad de no tener fallo y un 5 % de cada uno de los siguientes: corrupción, reproducción de un mensaje válido anterior, un retraso de 120 s (ventana de frescura de 60 s) y descarte. Resultados: todos los mensajes corrompidos se rechazaron como corruptos; todas las reproducciones, como reproducción; todos los mensajes retrasados, como obsoletos; ningún fallo produjo un «ok» silencioso. Pero **los descartes son invisibles para el receptor**: se perdieron 21 mensajes y el receptor no señaló nada. La comprobación de contadores del receptor rechaza los contadores antiguos, pero no alarma ante los huecos. El requisito R7 (alarmas en 60 s) implica que la pérdida de los datos de una estación debe ser visible en sí misma. Cambio de diseño: alarmar cuando no llegue ningún mensaje válido de una estación durante 60 s y registrar los huecos de contador. La campaña se vuelve a ejecutar tras el cambio con la misma semilla.

### 40.5 Actividad práctica: laboratorio 15

```python
# Lab 15 - fault-injection campaign against the telemetry receiver (synthetic, seeded, offline)
import random, hmac, hashlib, struct
KEY = b"k" * 32
def seal(c, lvl, ts):
    b = struct.pack(">QHI", c, lvl, ts); return b + hmac.new(KEY, b, hashlib.sha256).digest()[:16]
def receive(m, state, now, max_age=60):
    b, tag = m[:14], m[14:]
    if len(m) != 30 or not hmac.compare_digest(tag, hmac.new(KEY, b, hashlib.sha256).digest()[:16]): return "corrupt"
    c, lvl, ts = struct.unpack(">QHI", b)
    if c <= state["last"]: return "replay"
    if now - ts > max_age: return "stale"
    state["last"] = c; return "ok"
rng = random.Random(40); state = {"last": 0}; tally = {}; sent = []
for i in range(1, 501):
    now = 10 * i; m = seal(i, 300, now); fault = rng.choices(["none", "corrupt", "replay", "delay", "drop"], [80, 5, 5, 5, 5])[0]
    if fault == "corrupt": m = m[:5] + bytes([m[5] ^ 0x10]) + m[6:]
    if fault == "replay" and sent: m = rng.choice(sent)
    if fault == "drop": tally[("drop", "lost")] = tally.get(("drop", "lost"), 0) + 1; continue
    arrive = now + (120 if fault == "delay" else 1)
    out = receive(m, state, arrive)
    tally[(fault, out)] = tally.get((fault, out), 0) + 1
    if fault == "none": sent.append(m)
for k in sorted(tally): print(k, tally[k])
```

Salida esperada:

```text
('corrupt', 'corrupt') 14
('delay', 'stale') 22
('drop', 'lost') 21
('none', 'ok') 419
('replay', 'replay') 24
```

Todos los mensajes corrompidos, reproducidos y retrasados acabaron en la clase que predecía su oráculo, y ningún fallo produjo una aceptación silenciosa. Los mensajes descartados son el hallazgo: se perdieron veintiuno y el receptor no señaló nada, porque las comprobaciones de contadores solo rechazan mensajes antiguos. Ese resultado dio lugar a la alarma de estación sin datos, que salta cuando no llega ningún mensaje válido de una estación durante sesenta segundos, y al hallazgo de revisión F2. Después, la campaña se vuelve a ejecutar con la misma semilla para confirmar el cambio.

### 40.6 Errores comunes y límites

- Modelos de fallos limitados a lo que esperaba el diseñador.
- Sin oráculo, de modo que los resultados no pueden juzgarse.
- Campañas sin semilla.
- Tratar «no se observaron fallos silenciosos» como una prueba.
- No volver a ejecutar la campaña después de las correcciones.

La primera campaña del TMRP mostró el primer error: los descartes eran silenciosos porque los diseñadores nunca incluyeron la pérdida de datos entre los fallos que su receptor debía advertir. Volver a ejecutarla tras añadir la alarma de estación sin datos es la forma de confirmar la corrección. Su semilla está registrada, así que la nueva ejecución es comparable. La clase de descartes se mantiene ahora en todas las ejecuciones.

### Ejercicios — capítulo 40

**EX079 — Detección de huecos.** *Objetivo:* cerrar la laguna de los descartes. *Entradas:* laboratorio 15. *Pasos:* añada la detección de huecos (un salto de contador mayor que 1 registra `gap`) y vuelva a ejecutar con la misma semilla; informe de cuántos eventos de hueco se registran y de por qué el número puede diferir del número de descartes. *Evidencia esperada:* código y salida. *Rúbrica:* 3 = implementado correctamente; explica que los descartes consecutivos producen un único evento de hueco y que las reproducciones y los mensajes rechazados también afectan a la continuidad de los contadores; 2 = implementado, sin explicación; 1 = no ejecutado; 0 = nada.

**EX080 — Ampliar el modelo de fallos.** *Objetivo:* añadir fallos. *Entradas:* laboratorio 15. *Pasos:* añada dos clases de fallo, la reordenación (intercambiar dos mensajes consecutivos) y el reinicio del receptor (restablecer `state`), defina los oráculos, ejecute e informe de los fallos silenciosos. *Evidencia esperada:* código, oráculos y resultados. *Rúbrica:* 3 = la reordenación hace que el mensaje anterior se rechace como reproducción (aceptable o no, de forma argumentada), el reinicio permite reproducciones (fallo silencioso) salvo que el estado se conserve; 2 = una clase; 1 = sin oráculo; 0 = nada.

### Síntesis del capítulo

La inyección de fallos ejercita el tratamiento de errores que las pruebas ordinarias no alcanzan. Defina de antemano el modelo de fallos y el oráculo, fije la semilla y cuente, clasifique los resultados y busque los fallos silenciosos. El laboratorio 15 muestra el resultado típico: el control rechaza lo que se diseñó para rechazar y es ciego a lo que nadie incluyó en la lista, aquí la pérdida de datos.

<!-- open-cyber-academy:chapter-navigation:start ch-40 -->
### Siga estudiando — capítulo 40 de 50

[← Capítulo 39](#ch-39) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 41 →](#ch-41)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-41"></a>

## Capítulo 41 — Infraestructura crítica y seguridad sectorial: optimización de sistemas

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) formular la inversión en seguridad como un problema de optimización con objetivos y restricciones; (2) resolver problemas pequeños de forma exacta y entender por qué las heurísticas voraces pueden fallar; (3) tratar objetivos múltiples y la incertidumbre con el análisis de Pareto y la sensibilidad; y (4) presentar los resultados de la optimización como apoyo a la decisión, no como decisiones. Se apoya en los capítulos 25, 32 y 36 y prepara el proyecto final.

### 41.1 Formular el problema

Elija un conjunto de controles $S$ que maximice el beneficio $\sum_{c\in S} b_c$ sujeto al coste $\sum_{c\in S} k_c \le B$. Este es el problema de la mochila 0/1. Los beneficios pueden ser la reducción de la pérdida anual esperada, la reducción de las personas-hora sin agua o la reducción de la probabilidad del evento cima. Los problemas reales añaden restricciones (dependencias entre controles, límites de personal, fases) e interacciones (dos controles que abordan el mismo escenario no suman sus beneficios).

Para la fase 1 del TMRP, los beneficios del laboratorio 16 son estimaciones sintéticas de la reducción de la pérdida anual esperada.

### 41.2 Soluciones exactas y heurísticas

Con un puñado de candidatos, enumere todos los subconjuntos ($2^n$). La programación dinámica resuelve los problemas de la mochila de forma exacta en un tiempo proporcional a $n \times B$ para costes enteros. La heurística **voraz** (elegir por la razón beneficio/coste hasta agotar el presupuesto) es rápida e intuitiva, pero puede dejar presupuesto sin usar o pasar por alto combinaciones mejores. Para problemas mayores, los solucionadores de programación entera son lo habitual. El laboratorio 16 muestra el fallo de la heurística voraz con los siete candidatos del TMRP. La heurística voraz dejó presupuesto sin usar y omitió las RTU de repuesto, una laguna que la búsqueda exhaustiva encontró de inmediato.

### 41.3 Objetivos múltiples e incertidumbre

Las inversiones en seguridad ponderan el coste, la reducción del riesgo, la operabilidad y otros bienes. Una solución es **óptima de Pareto** si ninguna otra solución es mejor en un objetivo sin ser peor en otro; presente el conjunto de Pareto en lugar de una única respuesta ponderada. Los beneficios son estimaciones inciertas; compruebe si el conjunto óptimo cambia cuando los beneficios varían dentro de rangos plausibles. Las elecciones robustas (las que son buenas en todos los escenarios) suelen ser preferibles a las elecciones que solo son óptimas con estimaciones puntuales.

Para el TMRP, la comprobación de robustez del EX082 varía cada beneficio un veinte por ciento y constata que tres de las catorce ejecuciones cambian el óptimo, de modo que la última parte de la cartera es un casi empate.

### 41.4 Interacciones

Los beneficios rara vez son aditivos. La telemetría autenticada y la supervisión de red reducen ambas el riesgo de órdenes falsificadas; una vez implantada la autenticación, el beneficio adicional de la supervisión para ese escenario es menor. Modele las interacciones calculando el beneficio a partir del modelo de escenarios (p. ej., el árbol de fallos) para cada conjunto candidato, en lugar de sumar cifras por control. En el laboratorio 16 los beneficios simplemente se suman, lo cual es una simplificación: la telemetría autenticada y el sensor de detección de red reducen ambos el riesgo de órdenes falsificadas, de modo que su valor combinado es menor que la suma. Un modelo mejor vuelve a calcular el beneficio a partir del árbol de fallos para cada conjunto candidato.

### 41.5 Ejemplo resuelto: cartera de la fase 1 del TMRP (sintético)

Siete controles candidatos con costes y beneficios sintéticos, presupuesto de 250 k (laboratorio 16). La heurística voraz por razón elige las copias de seguridad desconectadas, el modo manual local, la telemetría autenticada y el bastionado de la estación de ingeniería: coste 215 k, beneficio 480 k. La búsqueda exhaustiva encuentra un conjunto mejor (telemetría autenticada, modo manual local, copias de seguridad desconectadas y RTU de repuesto) con un coste de 250 k y un beneficio de 530 k. La heurística voraz tomó pronto el bastionado barato de la estación de trabajo y después no pudo costear las RTU de repuesto. El equipo presenta ambos resultados, señala que las estimaciones de beneficio tienen una incertidumbre amplia y muestra que, cuando cada beneficio varía individualmente un ±20 %, la telemetría autenticada y el modo manual local permanecen en todos los óptimos, mientras que tres ejecuciones sustituyen las copias de seguridad desconectadas y las RTU de repuesto por el generador de respaldo (EX082): una comprobación de robustez, no una demostración.

### 41.6 Actividad práctica: laboratorio 16

```python
# Lab 16 - choose controls under a budget: exhaustive search beats greedy here (synthetic, offline)
from itertools import combinations
C = {  # control: (cost k$, expected annual loss reduction k$)
    "auth_telemetry": (120, 260), "backup_gen_PS4": (90, 150), "local_manual_mode": (40, 110),
    "offline_backups": (30, 70), "eng_ws_hardening": (25, 40), "ndr_sensor": (100, 120), "spare_rtus": (60, 90)}
B = 250
best = max((s for r in range(len(C)+1) for s in combinations(C, r) if sum(C[c][0] for c in s) <= B),
           key=lambda s: sum(C[c][1] for c in s))
print("optimal:", sorted(best), "cost", sum(C[c][0] for c in best), "benefit", sum(C[c][1] for c in best))
g, spent = [], 0
for c in sorted(C, key=lambda c: C[c][1] / C[c][0], reverse=True):
    if spent + C[c][0] <= B: g.append(c); spent += C[c][0]
print("greedy :", sorted(g), "cost", spent, "benefit", sum(C[c][1] for c in g))
```

Salida esperada:

```text
optimal: ['auth_telemetry', 'local_manual_mode', 'offline_backups', 'spare_rtus'] cost 250 benefit 530
greedy : ['auth_telemetry', 'eng_ws_hardening', 'local_manual_mode', 'offline_backups'] cost 215 benefit 480
```

El óptimo exhaustivo gasta todo el presupuesto en la telemetría autenticada, el modo manual local, las copias de seguridad desconectadas y las RTU de repuesto. La heurística voraz elige pronto el bastionado de la estación de trabajo por su buena razón, deja demasiado poco dinero para las RTU de repuesto y termina con menos beneficio y algo de presupuesto sin usar. Con siete candidatos, la búsqueda exhaustiva es instantánea, así que no hay motivo para aceptar la respuesta voraz; con cientos de candidatos, un solucionador de programación entera sustituiría a ambas. Registre ambos resultados. Anote el presupuesto sin usar.

### 41.7 Errores comunes y límites

- Sumar los beneficios de controles que interactúan.
- Presentar un único óptimo sin sensibilidad.
- Heurísticas voraces usadas sin compararlas con las soluciones exactas en instancias pequeñas.
- Resultados de la optimización presentados como decisiones en lugar de como insumos para las decisiones.
- Cifras de beneficio sin una base declarada.

La cartera del TMRP evita el tercer error comparando la heurística voraz con la búsqueda exhaustiva, y presenta ambos resultados con la comprobación de robustez al responsable de la decisión. Cada cifra de beneficio se etiqueta como estimación sintética, y el resultado se ofrece como apoyo a la decisión. Las interacciones se señalan.

### Ejercicios — capítulo 41

**EX081 — Barrido de presupuesto.** *Objetivo:* ver cómo cambia el óptimo con el presupuesto. *Entradas:* laboratorio 16. *Pasos:* calcule el conjunto óptimo y el beneficio para presupuestos de 150, 200, 250, 300 y 350 k; represente gráficamente o tabule el beneficio marginal por cada 50 k adicionales. *Evidencia esperada:* tabla. *Rúbrica:* 3 = óptimos correctos (ejecute el código), beneficio marginal decreciente observado e interpretado; 2 = un error; 1 = un solo presupuesto; 0 = nada.

**EX082 — Robustez.** *Objetivo:* comprobar la sensibilidad del óptimo. *Entradas:* laboratorio 16. *Pasos:* para cada control, multiplique su beneficio por 0,8 y por 1,2 (los demás sin cambios), vuelva a calcular el óptimo e informe de cualquier cambio. *Evidencia esperada:* tabla de 14 ejecuciones. *Rúbrica:* 3 = resultados correctos y conclusión sobre la robustez; 2 = parcial; 1 = no ejecutado; 0 = nada.

### Síntesis del capítulo

Formule las decisiones de inversión como una optimización con objetivos y restricciones explícitos, resuelva los problemas pequeños de forma exacta y desconfíe de los atajos voraces, modele las interacciones en lugar de sumar beneficios, presente conjuntos de Pareto y la sensibilidad, y ofrezca el resultado como apoyo estructurado para una decisión humana.

<!-- open-cyber-academy:chapter-navigation:start ch-41 -->
### Siga estudiando — capítulo 41 de 50

[← Capítulo 40](#ch-40) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 42 →](#ch-42)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-42"></a>

## Capítulo 42 — Infraestructura crítica y seguridad sectorial: investigación aplicada

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) plantear una pregunta de ingeniería que necesita evidencia nueva; (2) diseñar un pequeño estudio aplicado (experimento en un banco de pruebas, estudio de simulación o medición de campo) con controles y reproducibilidad; (3) usar de forma responsable los conjuntos de datos y bancos de pruebas públicos; y (4) informar de los resultados con sus límites. Es la contrapartida de ingeniería de los libros de investigación de maestría y de doctorado y prepara el proyecto final y la tesis (capítulos 44–49).

### 42.1 Investigación de ingeniería frente a investigación académica

La investigación aplicada de este curso responde a una pregunta de diseño para un sistema concreto, con evidencia suficiente para una decisión de ingeniería. Difiere del [libro de maestría](../../../../masters-2-years/critical-sector-security/es/book/MANUSCRIPT.md), que enseña a diseñar y defender un estudio empírico con revisión ética, y del [libro de doctorado](../../../../doctorate-2-years/critical-sector-security/es/book/MANUSCRIPT.md), que exige una contribución original al conocimiento validada de forma independiente. Un estudio de ingeniería tiene éxito si cambia o confirma una decisión de diseño con evidencia que un revisor pueda comprobar.

### 42.2 Diseñar un estudio pequeño

Formule la pregunta y la decisión a la que informa; defina la medición (capítulo 29); elija un diseño (comparación de alternativas en un banco de pruebas, un barrido de parámetros en simulación o la medición de un sistema existente); fije el análisis antes de ejecutar; controle los factores de confusión (la misma carga, el mismo hardware, las mismas semillas); repita las ejecuciones para medir la variabilidad; y registre todo para permitir la reproducción ([Sandve et al., 2013](https://doi.org/10.1371/journal.pcbi.1003285)). El estudio del detector del TMRP sigue este patrón, con su regla de análisis fijada antes de cualquier ejecución. Sus semillas quedan registradas.

### 42.3 Conjuntos de datos y bancos de pruebas públicos

Los conjuntos de datos y bancos de pruebas públicos de seguridad industrial permiten experimentar sin tocar infraestructuras reales. El conjunto de datos del banco de pruebas Secure Water Treatment (SWaT) descrito por [Goh et al. (2017)](https://doi.org/10.1007/978-3-319-71368-7_8) y la competición BATADAL sobre redes de distribución de agua de la que informan [Taormina et al. (2018)](https://doi.org/10.1061/(ASCE)WR.1943-5452.0000969) se usan ampliamente. Conozca sus límites: los bancos de pruebas son más pequeños y limpios que las plantas reales, los conjuntos de ataques los eligen los investigadores, y el rendimiento en un banco de referencia no se transfiere automáticamente. Lea sobre los errores de evaluación antes de declarar resultados ([Arp et al., 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/arp); [Sommer y Paxson, 2010](https://doi.org/10.1109/SP.2010.25)).

### 42.4 Ética y autorización

La investigación aplicada sobre sistemas reales requiere la autorización escrita del propietario y, cuando intervienen personas o datos personales, una revisión ética (capítulo 10). Los resultados que revelan debilidades de sistemas concretos van al propietario, no a un congreso. Para el TMRP, el estudio del detector usa simulación y los datos del propio historiador de la LRWA bajo la autoridad del programa. Cualquier hallazgo sobre el producto de un fabricante se comunicaría a ese fabricante en privado antes de escribir nada para un público más amplio, y ninguna estación real se usa como sujeto experimental.

### 42.5 Ejemplo resuelto: ¿merece la pena desplegar el detector acumulativo? (sintético)

Pregunta: ¿debería el TMRP desplegar en Hollin Hill el detector acumulativo de balance de masa del capítulo 17? Decisión a la que informa: desplegarlo, con qué umbral y con qué intervalo de recalibración. Diseño del estudio: barrido de simulación sobre niveles de ruido (0,005–0,02 m), deriva del caudalímetro (0–1 %) y umbrales (0,02–0,08 m), 100 ejecuciones con semilla por celda, midiendo las falsas alarmas al mes y el tiempo de detección de ataques en rampa de 0,01–0,1 m/h. Análisis fijado de antemano: elegir el umbral con menos de una falsa alarma al mes al nivel de ruido medido e informar del tiempo de detección con ese umbral. Validación: comparar el ruido simulado con dos semanas de datos del historiador. Límites: modelo de depósito de mezcla perfecta; un atacante que controle los caudalímetros queda fuera del alcance.

### 42.6 Actividad práctica

Implemente una versión reducida del §42.5 usando el laboratorio 7: tres umbrales × tres niveles de ruido × 20 semillas; informe de las falsas alarmas y de los tiempos de detección de la rampa en una tabla con su variabilidad. Fije su regla de análisis antes de ejecutar: por ejemplo, elija el umbral más bajo sin falsas alarmas en las ejecuciones sin ataque para cada nivel de ruido. Fije la semilla de cada ejecución y registre las semillas. Informe del número de falsas alarmas y del tiempo de detección de la rampa para cada celda con su dispersión entre semillas, no solo la media. Después, declare un límite del estudio reducido, como unos caudalímetros perfectos, y la dirección en la que sesga sus resultados.

### 42.7 Errores comunes y límites

- Estudios que no informan ninguna decisión.
- Análisis elegido después de ver los resultados.
- Ejecuciones únicas presentadas como resultados.
- Rendimiento en un banco de referencia del que se afirma que se transfiere a plantas reales.
- Debilidades de sistemas reales publicadas sin coordinación.

El estudio del detector acumulativo del ejemplo resuelto evita cada uno de ellos: informa una decisión de despliegue, fija de antemano su regla de análisis, usa cien ejecuciones por celda, valida su modelo de ruido frente a dos semanas de datos del historiador de la LRWA y declara que un atacante que controle los caudalímetros queda fuera del alcance.

### Ejercicios — capítulo 42

**EX083 — Protocolo del estudio.** *Objetivo:* redactar un protocolo especificado de antemano. *Entradas:* §42.5. *Pasos:* redacte un protocolo de una página: pregunta, decisión, diseño, mediciones, regla de análisis, validación, límites. *Evidencia esperada:* protocolo. *Rúbrica:* 3 = completo, regla de análisis fijada de antemano, validación frente a datos reales de ruido, límites honestos; 2 = análisis vago; 1 = sin decisión; 0 = nada.

**EX084 — Límites de un conjunto de datos.** *Objetivo:* evaluar la transferencia desde un banco de pruebas. *Entradas:* un fabricante afirma un 99 % de detección en un conjunto de datos público de un banco de pruebas de agua. *Pasos:* enumere cinco preguntas que haría antes de aceptarlo para la LRWA. *Evidencia esperada:* lista. *Rúbrica:* 3 = tasa base y tasa de falsas alarmas en operación, realismo del conjunto de ataques, protocolo de evaluación (ajuste por puntos, fuga de datos), escala/diferencia de la planta, adaptación a los adversarios; 2 = tres buenas preguntas; 1 = genérica; 0 = nada.

### Síntesis del capítulo

La investigación de ingeniería responde a una pregunta de diseño con evidencia comprobable. Especifique el estudio de antemano, controle los factores de confusión, repita las ejecuciones, use los bancos de pruebas públicos dentro de sus límites, obtenga autorización para cualquier cosa real e informe de los resultados con sus fronteras.

<!-- open-cyber-academy:chapter-navigation:start ch-42 -->
### Siga estudiando — capítulo 42 de 50

[← Capítulo 41](#ch-41) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 43 →](#ch-43)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-43"></a>

## Capítulo 43 — Prácticas en la industria o en el servicio público

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) planificar y completar una estancia de prácticas supervisada en un operador, un fabricante, un integrador, un regulador o un organismo público; (2) trabajar dentro de las normas de autorización, confidencialidad y seguridad de la estancia; (3) llevar un diario de práctica reflexiva que vincule el trabajo observado con los métodos del curso; y (4) elaborar un informe de la estancia que sea útil para la entidad de acogida y seguro de compartir. Aplica todo el curso a la práctica real y prepara el proyecto final.

### 43.1 Finalidad de las prácticas

Las prácticas ponen de manifiesto las restricciones que los libros de texto suavizan: los ciclos de contratación, la dotación de personal, los equipos heredados, los plazos regulatorios, los convenios sindicales, los presupuestos y la distancia entre el procedimiento y la práctica. Los ingenieros que han visto una sala de control de noche diseñan de forma distinta a los que no. El caso del TMRP de este libro es sintético; una estancia es donde se ve hasta qué punto las restricciones de una empresa de servicios real difieren de él. Fíjese en cómo se toman realmente las decisiones, en quién es responsable del riesgo operativo y en cuánto tarda un cambio sencillo, porque esas observaciones condicionarán cómo delimita el alcance de su proyecto final.

### 43.2 Acuerdo de la estancia

Antes de empezar, acuerde por escrito: el supervisor de la entidad de acogida y el supervisor académico; el alcance del trabajo; los sistemas a los que puede acceder y cómo; la confidencialidad y el tratamiento de los datos; la formación inicial en seguridad; lo que puede publicar en su informe; y cómo se gestionan los hallazgos incidentales. Usted trabaja bajo la autoridad y las políticas de la entidad de acogida; su curso no le da autoridad para probar ni acceder a nada.

La entidad de acogida del ejemplo resuelto aprobó el texto del informe final antes de que saliera de la organización. Acordar de antemano la norma de publicación evitó cualquier discusión sobre lo que podía incluir el informe.

### 43.3 Diario de práctica reflexiva

Lleve un diario semanal con cuatro entradas: **observación** (lo que vio, sin juzgarlo), **conexión** (con qué método de qué capítulo se relaciona), **diferencia** (en qué se apartó la práctica del método y por qué tenía sentido localmente) y **pregunta** (qué investigaría). La reflexión convierte la experiencia en un criterio transferible. No registre detalles sensibles en el diario; registre patrones. En el ejemplo resuelto que sigue, la observación del estudiante sobre las versiones de firmware sigue exactamente este patrón y no contiene nombres de dispositivos. Las entradas semanales mantienen el hábito.

### 43.4 Trabajo habitual en las estancias

Tareas típicas para un estudiante de ingeniería: actualizar un inventario de activos y conciliarlo con los datos de red (capítulo 22); redactar o revisar una guía de actuación (capítulo 37); apoyar una evaluación de riesgos (capítulo 24); preparar un procedimiento de prueba para una puesta en servicio (capítulo 31); evaluar avisos de seguridad frente al inventario (capítulo 12). Cada una produce un entregable para la entidad de acogida y un artefacto de aprendizaje depurado para el curso. El estudiante del ejemplo resuelto realizó la primera tarea: conciliar un registro de activos con los datos de supervisión. Su entregable para la entidad de acogida fue un cambio en el formulario de órdenes de trabajo.

### 43.5 Ejemplo resuelto: un informe de estancia depurado (sintético)

Un estudiante en prácticas en una distribuidora eléctrica regional (sintética) redacta una sección del informe: «Observación: las versiones de firmware de las RTU de subestación que figuraban en el registro de activos diferían de las observadas mediante supervisión pasiva en el 18 % de una muestra de 60 dispositivos. Conexión: la conciliación de múltiples fuentes de inventario del capítulo 22. Diferencia: el registro se actualiza en las visitas de mantenimiento anuales, mientras que los cambios de firmware se producen durante reparaciones no programadas; el personal de campo no tenía una forma sencilla de notificar los cambios. Recomendación (aceptada por la entidad de acogida): añadir un campo de firmware al formulario de órdenes de trabajo de reparación y una conciliación trimestral con los datos de supervisión». No aparecen nombres de dispositivos, direcciones ni ubicaciones; la entidad de acogida aprobó el texto.

### 43.6 Actividad práctica

Redacte un acuerdo de estancia para una estancia hipotética de cuatro meses en una empresa de servicios de agua, que cubra todos los puntos del §43.2. Use una empresa de agua como la LRWA como modelo mental, pero mantenga el acuerdo lo bastante general como para que una entidad de acogida real pueda firmarlo. Nombre a ambos supervisores por su función, enumere los sistemas que puede ver y cómo, y declare claramente que no puede probar ni explorar nada. Indique cómo se notifican los hallazgos incidentales y quién aprueba su informe antes de que salga de la entidad de acogida. Añada una fecha para la formación inicial en seguridad y los datos que puede llevarse, que normalmente no deberían ser ninguno.

### 43.7 Errores comunes y límites

- Empezar sin un alcance y un acuerdo de tratamiento de datos por escrito.
- Tratar el acceso de la estancia como permiso para explorar.
- Diarios que contienen detalles sensibles.
- Informes que critican a la entidad de acogida sin entender las restricciones locales.

El ejemplo resuelto evita cada uno de ellos: su alcance se acordó, su diario registró patrones en lugar de detalles de dispositivos y su recomendación tuvo en cuenta por qué el registro iba por detrás de las reparaciones. Su crítica del registro se planteó en torno a una laguna del proceso, no en torno al personal de campo, y la entidad de acogida aceptó la recomendación porque encajaba con la forma en que realmente se hacían las reparaciones.

### Ejercicios — capítulo 43

**EX085 — Acuerdo de la estancia.** *Objetivo:* definir los límites de la estancia. *Entradas:* §43.6. *Pasos:* redacte el acuerdo. *Evidencia esperada:* de una a dos páginas. *Rúbrica:* 3 = todos los puntos del §43.2, prohibición explícita de las pruebas fuera del alcance, vía para los hallazgos incidentales, aprobación de la publicación; 2 = falta uno; 1 = genérico; 0 = nada.

**EX086 — Entrada reflexiva.** *Objetivo:* reflexionar de forma útil. *Entradas:* una observación: «los operadores llevaban un cuaderno en papel con los cambios de consigna junto al registro del SCADA». *Pasos:* redacte una entrada del diario en cuatro partes. *Evidencia esperada:* entrada. *Rúbrica:* 3 = observación neutral, vínculo con los capítulos 13/37, racionalidad local (confianza, interrupciones, traspaso de turno), pregunta de investigación; 2 = enjuiciadora; 1 = solo la observación; 0 = nada.

### Síntesis del capítulo

Las prácticas enseñan las restricciones que dan forma a los diseños reales. Trabaje dentro de un acuerdo escrito y bajo la autoridad de la entidad de acogida, registre observaciones, conexiones, diferencias y preguntas sin detalles sensibles, y aporte valor a la entidad de acogida de una forma que sea seguro compartir.

<!-- open-cyber-academy:chapter-navigation:start ch-43 -->
### Siga estudiando — capítulo 43 de 50

[← Capítulo 42](#ch-42) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 44 →](#ch-44)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-44"></a>

## Capítulo 44 — Proyecto final de ingeniería I

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) definir un proyecto final con un patrocinador, un alcance, unos requisitos y unos criterios de aceptación; (2) planificarlo con un calendario, un registro de riesgos y un plan de verificación; (3) preparar un entorno de ingeniería reproducible; y (4) superar una revisión preliminar de diseño. El proyecto final integra el curso en un único sistema construido y verificado y continúa en los capítulos 45–50.

### 44.1 Qué es un proyecto final

Un proyecto final es un proyecto de ingeniería sustancial en el que el estudiante diseña, construye y verifica un sistema que cumple requisitos reales o realistas bajo restricciones. En este curso, el proyecto final debe: responder a una necesidad de seguridad o de resiliencia de una infraestructura crítica; incluir un artefacto que funcione (software, configuración, banco de pruebas o prototipo); incluir análisis (amenazas/fallos, rendimiento, fiabilidad); y verificarse frente a requisitos declarados. El proyecto final continúa el caso del TMRP, salvo que su supervisor apruebe otro caso sintético o autorizado.

El ejemplo resuelto que sigue continúa el TMRP: telemetría autenticada segura ante reinicios para las RTU heredadas de PS1 y PS2.

### 44.2 Delimitación del alcance

Un buen alcance de proyecto final es lo bastante estrecho para terminarlo y lo bastante profundo para exigir ingeniería real. Ejemplos: una pasarela de telemetría autenticada con verificación por inyección de fallos; un detector basado en residuos con un estudio de simulación validado; una herramienta de orquestación de la recuperación con un ensayo de restablecimiento medido; una herramienta de verificación de la segmentación con un modelo de políticas. Redacte un alcance de una página: necesidad, partes interesadas, entregables, elementos fuera del alcance, restricciones y criterios de aceptación.

El alcance del proyecto final del TMRP en el ejemplo resuelto que sigue cabe en una página y deja fuera el hardware real de las RTU y la red del operador de telecomunicaciones.

### 44.3 Planificación

Planifique con una estructura de desglose del trabajo, un calendario con hitos (revisión preliminar de diseño, revisión crítica de diseño, verificación completada, borrador de la tesis, defensa), un registro de riesgos (técnicos, de calendario, de acceso, de competencias) y un plan de verificación que trace los requisitos hasta las pruebas. Lleve un diario semanal y actualice el registro de riesgos cada mes. Para el proyecto final del TMRP, el calendario de doce semanas sitúa la revisión preliminar de diseño en las primeras semanas y la revisión independiente antes de la verificación. Su registro de riesgos incluye la posibilidad de que la seguridad ante reinicios resulte más difícil de lo esperado, que es, como muestra después el resumen de la verificación, lo que ocurrió cuando el receptor aceptó reproducciones tras un reinicio.

### 44.4 Entorno

Prepare el control de versiones, un gestor de incidencias, una compilación reproducible (dependencias fijadas o solo la biblioteca estándar), pruebas automatizadas y un directorio de resultados en el que cada resultado se guarde con el commit, las semillas y el entorno que lo produjeron. Para el proyecto final del TMRP, la pasarela usa solo la biblioteca estándar de Python, de modo que no hay dependencias que fijar, y cada resultado de campaña se guarda con su semilla y su commit. Esa disciplina es la que permite que el expediente posterior indique un hash y una versión para cada resultado.

### 44.5 Ejemplo resuelto: alcance del proyecto final (sintético)

*Título:* Telemetría autenticada segura ante reinicios para RTU heredadas. *Necesidad:* N2/N3 del TMRP. *Entregables:* software de la pasarela (biblioteca estándar de Python), arnés de banco de pruebas, campaña de inyección de fallos, procedimiento de rotación de claves, tesis. *Fuera del alcance:* hardware real de las RTU; red del operador de telecomunicaciones. *Restricciones:* 12 semanas; datos sintéticos. *Aceptación:* R1, R2 (incluidos los reinicios) y R7 verificados en el banco de pruebas; cero fallos silenciosos en una campaña con semilla de 10.000 mensajes en siete clases de fallo; demostración de la rotación de claves sin pérdida de telemetría.

Cada criterio de aceptación corresponde a un requisito o a una demostración, de modo que la revisión crítica de diseño puede comprobarlos uno por uno.

### 44.6 Actividad práctica

Redacte el alcance y el plan de su proyecto final y celebre una revisión preliminar de diseño con su supervisor y un compañero. Base su alcance en la plantilla de una página: necesidad, partes interesadas, entregables, elementos fuera del alcance, restricciones y criterios de aceptación. Después, prepare un plan breve con hitos y un registro de riesgos. En la revisión, pida a su supervisor y a su compañero que cuestionen sobre todo los criterios de aceptación, porque un criterio que no puede probarse causará problemas en la revisión crítica de diseño. Registre sus hallazgos y sus respuestas.

### 44.7 Errores comunes y límites

- Alcances demasiado amplios («proteger la empresa de servicios»).
- Sin criterios de aceptación.
- Verificación planificada al final.
- Entornos no reproducibles.

El borrador de alcance del EX087 muestra los dos primeros errores: proteger las empresas de agua con un sistema de IA no tiene límites ni criterios de aceptación. El alcance del proyecto final del TMRP los evita nombrando una pasarela, tres requisitos y una campaña medida. Su plan de verificación se redactó junto con el alcance, y su entorno usa solo la biblioteca estándar con ejecuciones con semilla, de modo que todo resultado puede reproducirse. Sus hitos tienen fecha.

### Ejercicios — capítulo 44

**EX087 — Crítica de un alcance.** *Objetivo:* acotar un alcance. *Entradas:* borrador de alcance «Construir un sistema de IA para proteger a las empresas de agua frente a los ciberataques». *Pasos:* enumere cuatro problemas y reescriba el alcance en una página. *Evidencia esperada:* crítica y reescritura. *Rúbrica:* 3 = problemas (sin límites, sin requisitos, sin datos, sin aceptación) y una reescritura viable y verificable; 2 = reescritura vaga; 1 = solo la crítica; 0 = nada.

**EX088 — Registro de riesgos.** *Objetivo:* planificar los riesgos del proyecto. *Entradas:* §44.5. *Pasos:* redacte cinco riesgos del proyecto con probabilidad, impacto, mitigación y desencadenante. *Evidencia esperada:* tabla. *Rúbrica:* 3 = riesgos realistas (ampliación descontrolada del alcance, diseño de la seguridad ante reinicios más difícil de lo esperado, fidelidad del banco de pruebas, tiempo, disponibilidad del supervisor) con desencadenantes concretos; 2 = sin desencadenantes; 1 = genérico; 0 = nada.

### Síntesis del capítulo

Un proyecto final es un sistema acotado, construido y verificado. Defina la necesidad, los entregables, las restricciones y los criterios de aceptación; planifique desde el principio los hitos, los riesgos y la verificación; y haga reproducible el entorno para que todo resultado pueda trazarse y volver a ejecutarse.

<!-- open-cyber-academy:chapter-navigation:start ch-44 -->
### Siga estudiando — capítulo 44 de 50

[← Capítulo 43](#ch-43) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 45 →](#ch-45)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-45"></a>

## Capítulo 45 — Revisión independiente del diseño

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) realizar una revisión técnica independiente del diseño de otro equipo con criterios estructurados; (2) redactar hallazgos específicos, respaldados por evidencia y accionables; (3) clasificar los hallazgos por gravedad y recomendar su tratamiento; y (4) recibir una revisión de su propio diseño y responder a ella. Aplica a diseños completos el rigor de tipo Fagan (capítulo 14) y prepara el Proyecto final II.

### 45.1 Independencia y finalidad

Un revisor independiente no ha trabajado en el diseño ni depende jerárquicamente de sus autores. La independencia detecta errores que los autores no pueden ver: supuestos compartidos, puntos ciegos, verificación ilusoria. La finalidad es mejorar el diseño y la decisión sobre él, no anotarse tantos. Para el TMRP, el revisor del expediente del proyecto final es alguien que no trabajó en la pasarela ni depende de sus autores. Esa independencia es la razón por la que el revisor advirtió que el caso de aseguramiento citaba T3 como superada mientras la matriz aún la registraba como fallida, una incoherencia que los autores habían pasado por alto muchas veces al leer.

### 45.2 Criterios de revisión

Revise frente a: los requisitos (completos, verificables, trazados); la arquitectura (guiada por las consecuencias, con el comportamiento ante fallos y ataques analizado); los controles (especificados con su rendimiento, capas independientes); los análisis (supuestos declarados, cifras coherentes); la verificación (el plan cubre los requisitos, los fallos se tratan con honestidad); las operaciones (procedimientos, formación, recuperación); la mantenibilidad; y el caso de aseguramiento (afirmaciones respaldadas, derrotadores declarados). Cada criterio corresponde a un capítulo de este libro: los requisitos al capítulo 21, la arquitectura al capítulo 26, los controles al capítulo 27, la verificación a los capítulos 30 y 40, las operaciones al capítulo 37 y el caso de aseguramiento al capítulo 35. Los revisores del expediente del TMRP usaron esta lista como lista de comprobación.

### 45.3 Redactar hallazgos

Un hallazgo indica: lo que se observó (con una referencia al documento o a la evidencia), por qué importa (consecuencia), el criterio que incumple y una recomendación. Gravedad: **crítico** (la afirmación no puede sostenerse, o hay un riesgo para la seguridad funcional), **mayor** (laguna significativa que exige un cambio antes de la aprobación), **menor** (mejora), **observación** (no se requiere ningún cambio). Evite los hallazgos vagos («la seguridad parece débil») y el diseño por parte del revisor (prescribir su solución favorita cuando varias servirían).

Los hallazgos del TMRP en el ejemplo resuelto que sigue tienen esta forma. F4, sobre la fracción de la batería, es menor porque la afirmación se sostiene si se añade una fuente.

### 45.4 Responder a la revisión

Los autores responden a cada hallazgo: lo aceptan (con un cambio), lo rechazan (con razonamiento y evidencia) o lo aplazan (con responsable y fecha). El revisor comprueba las respuestas y cierra o escala los hallazgos. Los desacuerdos que no pueden resolverse pasan al responsable de la decisión con ambas posturas registradas. Para el TMRP, los autores aceptaron F2 y añadieron la alarma de estación sin datos, y aceptaron F3 declarando R6 como no cumplido y valorando opciones en el ADR-015. Cada respuesta nombraba a un responsable, y el revisor comprobó la nueva ejecución de la campaña antes de cerrar F2.

### 45.5 Ejemplo resuelto: hallazgos sobre el expediente del TMRP (sintético)

- **F1 (crítico):** La subafirmación C2 del caso de aseguramiento cita T3 como superada, pero la matriz de trazabilidad (laboratorio 14) registra T3 como fallida y la repetición de la prueba en v2 no está registrada. *Recomendación:* registrar la evidencia de la repetición de la prueba o rebajar la afirmación.
- **F2 (mayor):** El receptor no alarma ante la falta de datos (los descartes del laboratorio 15 son silenciosos); R7 no puede declararse para los eventos de pérdida de datos. *Recomendación:* añadir la alarma de estación sin datos y volver a ejecutar la campaña.
- **F3 (mayor):** El ensayo de restablecimiento (capítulo 47) muestra 12 h frente a las 8 h de R6; el expediente declara R6 como cumplido. *Recomendación:* declarar R6 como no cumplido y presentar opciones.
- **F4 (menor):** El dimensionamiento de la batería usa una fracción utilizable de 0,6 sin fuente; cite los datos del fabricante de la batería.
- **F5 (observación):** La evaluación ponderada de conceptos (§25.4) es sensible al peso de la operabilidad; la decisión sigue siendo defendible.

### 45.6 Actividad práctica

Intercambie los expedientes del proyecto final con otro estudiante, revíselos frente a los criterios del §45.2 y redacte al menos seis hallazgos con su gravedad. Elija un revisor que no haya ayudado con su diseño. Para cada hallazgo, incluya la observación con su referencia, la consecuencia, el criterio que incumple y una recomendación. Use con honestidad los cuatro niveles de gravedad. Después, intercambien los papeles y responda a los hallazgos sobre su propio expediente con aceptar, rechazar o aplazar, aportando evidencia para cada rechazo. Conserve ambos registros para su expediente. Cíñase a la evidencia.

### 45.7 Errores comunes y límites

- Revisiones realizadas por personas que ayudaron a diseñar.
- Hallazgos vagos o sin evidencia.
- Inflación o deflación de la gravedad.
- Autores que rechazan hallazgos sin evidencia.

La revisión del TMRP evitó estos errores: el revisor era independiente, cada hallazgo citaba un documento, las gravedades se correspondían con las consecuencias, y las respuestas de los autores se respaldaron con evidencia y se comprobaron antes del cierre. F5 se mantuvo como observación, sin inflarla. F1 se calificó como crítico porque la afirmación no podía sostenerse tal como estaba redactada, no porque el error fuera embarazoso, y los autores no rechazaron ningún hallazgo sin evidencia que respaldara el rechazo.

### Ejercicios — capítulo 45

**EX089 — Reescribir hallazgos débiles.** *Objetivo:* redactar hallazgos accionables. *Entradas:* «la gestión de claves no es muy buena»; «las pruebas parecen incompletas»; «yo usaría OPC UA en su lugar». *Pasos:* reescriba cada uno como un hallazgo propiamente dicho o explique por qué debe retirarse. *Evidencia esperada:* tres reescrituras. *Rúbrica:* 3 = observación específica, consecuencia, criterio, recomendación; el tercero retirado o replanteado como una preocupación basada en requisitos; 2 = uno vago; 1 = solo reformulación; 0 = nada.

**EX090 — Responder a F2 y F3.** *Objetivo:* responder a la revisión. *Entradas:* §45.5. *Pasos:* redacte las respuestas de los autores a F2 y F3 con su tratamiento, los cambios, los responsables y las fechas. *Evidencia esperada:* dos respuestas. *Rúbrica:* 3 = F2 aceptado con cambio de diseño y nueva prueba, F3 aceptado con información honesta y opciones (paralelizar la recuperación, imágenes preconstruidas, revisar el requisito con el acuerdo de las partes interesadas); 2 = a la defensiva; 1 = los rechaza; 0 = nada.

### Síntesis del capítulo

La revisión independiente encuentra lo que los autores no pueden ver. Revise frente a criterios explícitos, redacte hallazgos específicos, respaldados por evidencia y accionables con gravedades honestas, y responda a cada hallazgo con aceptar, rechazar o aplazar, de forma registrada y comprobada.

<!-- open-cyber-academy:chapter-navigation:start ch-45 -->
### Siga estudiando — capítulo 45 de 50

[← Capítulo 44](#ch-44) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 46 →](#ch-46)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-46"></a>

## Capítulo 46 — Proyecto final de ingeniería II

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) completar la implementación del artefacto del proyecto final; (2) ejecutar el plan de verificación completo y registrar los resultados; (3) cerrar los hallazgos de la revisión; y (4) superar una revisión crítica de diseño con evidencia. Continúa el capítulo 44 tras la revisión independiente y prepara el ensayo de fallo y recuperación (capítulo 47).

### 46.1 Terminar la construcción

Congele el alcance: a estas alturas, las funciones nuevas amenazan la verificación. Cierre primero los hallazgos de la revisión que exigen cambios de diseño. Mantenga la rama principal superando siempre sus pruebas; etiquete la versión que entra en la verificación final. Para el proyecto final del TMRP, el alcance se congeló tras la revisión independiente. La alarma de estación sin datos de F2 fue el cambio de diseño realizado antes de que la versión etiquetada entrara en la verificación final; cualquier idea posterior pasó a una lista de trabajo futuro. La corrección del reinicio llegó más tarde, como una corrección hallada por la propia verificación, que es el único tipo de cambio permitido tras una congelación. La rama principal se mantuvo en verde.

### 46.2 Ejecutar la verificación

Ejecute el plan de verificación completo contra la versión etiquetada: pruebas unitarias, de integración, basadas en propiedades y de inyección de fallos (capítulos 30 y 40). Registre cada resultado con la versión, la semilla y el entorno. Ante cualquier fallo: registre, analice, corrija, vuelva a ejecutar y registre de nuevo. No sobrescriba los resultados anteriores; el historial es evidencia. Para el proyecto final del TMRP, el fallo del receptor al no rechazar las reproducciones tras un reinicio se registró, se corrigió conservando el último contador de cada estación y se volvió a probar, y se guardaron ambos resultados. La versión etiquetada fue la que se probó. Su semilla quedó registrada.

### 46.3 Revisión crítica de diseño

En la revisión crítica de diseño, el tribunal comprueba: los requisitos cumplidos con evidencia; los hallazgos de la revisión cerrados o con un tratamiento decidido; los riesgos residuales declarados y con responsable; las operaciones y el mantenimiento preparados; y la preparación para el ensayo. Lleve la matriz de trazabilidad, los resultados de la verificación, el registro de hallazgos y el caso de aseguramiento. Para el TMRP, el tribunal vio el resumen de la verificación que sigue. Incluye el fallo tras el reinicio y su corrección, la alarma de estación sin datos añadida tras F2 y la demostración de la rotación de claves. Con F1 a F3 cerrados o con un tratamiento decidido y R6 declarado con honestidad, el tribunal pudo tomar una decisión explícita sobre la preparación para el ensayo en lugar de darla por supuesta.

### 46.4 Ejemplo resuelto: resumen de la verificación del proyecto final (sintético)

| Requisito | Pruebas | Resultado | Notas |
|---|---|---|---|
| R1 | T1, T2, campaña (clase de corrupción) | Superado | 0 fallos silenciosos en 10.000 mensajes |
| R2 | T2, pruebas de reinicio (ambos extremos), campaña (reproducción, reordenación, reinicio) | Superado tras la corrección | El receptor aceptaba inicialmente reproducciones tras un reinicio; se corrigió conservando el último contador de cada estación; se volvió a probar |
| R7 | T5, prueba de la alarma de estación sin datos | Superado tras la corrección | Detección de descartes añadida tras F2 |
| Rotación de claves | Demostración | Superado | Ventana de solapamiento de 10 min con ambas claves aceptadas; después, se revocó la clave antigua |

El fallo tras el reinicio lo encontró el modelo de fallos ampliado del EX080: un rendimiento directo de la inversión en el laboratorio de verificación.

### 46.5 Actividad práctica

Ejecute su plan de verificación completo y elabore la tabla resumen con enlaces a los resultados en bruto. Para cada requisito, indique las pruebas, el resultado y cualquier corrección, como en el resumen del TMRP. Conserve los resultados fallidos con sus fechas y las correcciones que los siguieron, y enlace cada línea con los archivos de resultados en bruto, con sus semillas y versiones. Si una prueba no se ejecutó, dígalo en la tabla en lugar de dejar la casilla en blanco. La tabla debe permitir a un revisor trazar cualquier afirmación hasta un archivo en un solo paso.

### 46.6 Errores comunes y límites

- Añadir funciones durante la verificación.
- Sobrescribir los resultados fallidos con superaciones posteriores.
- Llegar a la revisión crítica de diseño con hallazgos críticos abiertos.

El proyecto final del TMRP evitó estos errores congelando el alcance tras la revisión, manteniendo en el registro el fallo tras el reinicio junto a su superación posterior y cerrando F1 a F3 antes de la revisión crítica de diseño. Los resultados fallidos permanecieron en el registro con las correcciones que los siguieron, de modo que los revisores pudieron ver cómo se había ganado cada superación. No se añadió ninguna función durante la verificación. Los hallazgos abiertos se cerraron primero.

### Ejercicios — capítulo 46

**EX091 — Diseño de la rotación.** *Objetivo:* diseñar una rotación de claves sin pérdidas. *Entradas:* §46.4. *Pasos:* describa paso a paso el protocolo de rotación, incluido cómo sabe el receptor qué clave probar, la ventana de solapamiento, el tratamiento de fallos y la revocación. *Evidencia esperada:* procedimiento. *Rúbrica:* 3 = ID de clave en la cabecera autenticada, el receptor acepta ambas claves durante la ventana, los contadores continúan, reversión si la nueva clave falla, clave antigua revocada y destruida; 2 = sin ID de clave; 1 = «cambiar la clave»; 0 = nada.

**EX092 — Decisión de preparación.** *Objetivo:* juzgar la preparación. *Entradas:* todos los requisitos se superan, salvo un hallazgo menor sobre la documentación y un hallazgo mayor abierto según el cual el umbral de la alarma de estación sin datos (60 s) produce dos falsas alarmas al día durante la congestión de LTE. *Pasos:* recomiende continuar / continuar con condiciones / no continuar para el ensayo, de forma razonada. *Evidencia esperada:* recomendación. *Rúbrica:* 3 = continuar con condiciones (estudio de ajuste del umbral durante el ensayo, operadores informados), razonamiento sobre la consecuencia de las falsas alarmas frente a una pérdida de datos no detectada; 2 = sin condiciones; 1 = sin razonar; 0 = nada.

### Síntesis del capítulo

Congele el alcance, cierre los hallazgos, verifique por completo la versión etiquetada y conserve el historial de fallos como evidencia. Llegue a la revisión crítica de diseño con la trazabilidad, los resultados, los hallazgos y el caso de aseguramiento, y salga de ella con una decisión explícita sobre la preparación.

<!-- open-cyber-academy:chapter-navigation:start ch-46 -->
### Siga estudiando — capítulo 46 de 50

[← Capítulo 45](#ch-45) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 47 →](#ch-47)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-47"></a>

## Capítulo 47 — Ensayo de fallo y recuperación

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) diseñar un ensayo controlado de fallo y recuperación con límites de seguridad; (2) calcular caminos críticos y comparar los tiempos de recuperación planificados y medidos; (3) observar y registrar el desempeño humano y técnico durante el ensayo; y (4) convertir los resultados del ensayo en el estado de los requisitos y en cambios de diseño. Valida los requisitos de recuperación (R6) y prepara el expediente de evidencia (capítulo 48).

### 47.1 Por qué ensayar la recuperación

Una capacidad de recuperación que no se ha ejercitado es una esperanza. Las copias de seguridad que no se han restaurado pueden estar incompletas; los procedimientos que no se han seguido pueden ser erróneos; los tiempos que no se han medido son conjeturas. La [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) trata la planificación de contingencias, incluidas las pruebas, la formación y los ejercicios. El propio ensayo del TMRP mostró por qué: el objetivo de restablecimiento de ocho horas de R6 parecía razonable hasta que se midió el camino crítico. Medirlo era precisamente el objetivo.

### 47.2 Diseñar el ensayo

Defina el escenario (p. ej., servidores SCADA declarados comprometidos a las 02:00), los objetivos (restablecer la operación remota a partir de copias de seguridad desconectadas; mantener el suministro en modo local durante todo el ensayo), los límites de seguridad (ensayo en el entorno de pruebas o en una ventana planificada con la operación local atendida por personal; criterios de interrupción), los observadores y las mediciones (tiempo de cada tarea, desviaciones respecto al procedimiento, decisiones). El ensayo del TMRP usó el escenario de servidores SCADA declarados comprometidos, con el suministro mantenido en modo local durante todo el ensayo. Los observadores registraron el tiempo de cada tarea y cada desviación respecto al procedimiento.

### 47.3 Camino crítico

Las tareas de recuperación tienen duraciones y dependencias. El **camino crítico** es la cadena más larga de tareas dependientes; fija el tiempo mínimo de recuperación. Las tareas que quedan fuera del camino crítico tienen **holgura**. Acortar la recuperación significa acortar las tareas del camino crítico o romper dependencias, no acelerar las tareas con holgura. En el ensayo del TMRP, el recambio de claves de las RTU tenía seis horas de holgura. Acelerarlo no habría cambiado nada. Solo la generación de imágenes, la reconstrucción y la restauración de la configuración determinaron el resultado de doce horas, y por eso todas las opciones para cumplir R6 actúan sobre una de esas tres tareas, como las imágenes en espera preconstruidas o la generación de imágenes en hardware de repuesto.

### 47.4 Ejemplo resuelto: ensayo de recuperación del TMRP (sintético)

El plan del ensayo (laboratorio 17): aislar (1 h); establecer las operaciones manuales (1 h); generar imágenes forenses de los servidores SCADA (3 h); reconstruir el SCADA a partir de soportes desconectados (4 h); restaurar la configuración (2 h); recambiar las claves de las RTU (3 h, en paralelo); verificar las consignas (1 h); reanudar el control remoto (1 h). El camino crítico pasa por la generación de imágenes forenses, la reconstrucción y la restauración de la configuración: el control remoto vuelve a las 12 h, frente a las 8 h de R6. El recambio de claves tiene 6 h de holgura; acelerarlo no consigue nada. Opciones para cumplir las 8 h: imágenes del SCADA en espera preconstruidas (reconstrucción de 4 h → 1 h); generación de imágenes en paralelo con la reconstrucción en hardware de repuesto (quita 3 h del camino); o un acuerdo con las partes interesadas para que R6 sea de 12 h, puesto que el suministro se mantiene en modo local durante todo el proceso. El ensayo midió además que las operaciones manuales se establecieron en 50 minutos, con lo que se cumplió el requisito de 1 h.

### 47.5 Actividad práctica: laboratorio 17

```python
# Lab 17 - recovery critical path versus the restoration target (synthetic TMRP trial plan, offline)
T = {  # task: (hours, prerequisites)
    "isolate": (1, []), "manual_ops": (1, ["isolate"]), "forensic_image": (3, ["isolate"]),
    "rebuild_scada": (4, ["forensic_image"]), "restore_config": (2, ["rebuild_scada"]),
    "rekey_rtus": (3, ["isolate"]), "verify_setpoints": (1, ["restore_config", "rekey_rtus"]),
    "resume_remote": (1, ["verify_setpoints"])}
ef, prev = {}, {}
def finish(t):
    if t not in ef:
        d, ps = T[t]; start = max((finish(p) for p in ps), default=0)
        prev[t] = max(ps, key=finish) if ps else None; ef[t] = start + d
    return ef[t]
end = finish("resume_remote"); path, n = [], "resume_remote"
while n: path.append(n); n = prev[n]
print("restore remote control at", end, "h; critical path:", " -> ".join(reversed(path)))
print("slack of rekey_rtus:", finish("restore_config") - finish("rekey_rtus"), "h; target 8 h met:", end <= 8)
```

Salida esperada:

```text
restore remote control at 12 h; critical path: isolate -> forensic_image -> rebuild_scada -> restore_config -> verify_setpoints -> resume_remote
slack of rekey_rtus: 6 h; target 8 h met: False
```

La salida confirma el ejemplo resuelto: el control remoto vuelve al cabo de doce horas porque la generación de imágenes, la reconstrucción y la restauración de la configuración se ejecutan en serie, y el recambio de claves termina seis horas antes de que se necesite. Cambie el plan como pide el EX093 y observe cómo el camino crítico pasa a otra cadena. El laboratorio no incluye las operaciones manuales en el camino hacia el control remoto, porque se ejecutan en paralelo; el ensayo las midió por separado en cincuenta minutos frente al requisito de una hora. Conserve ambas salidas.

### 47.6 Errores comunes y límites

- Recuperación probada solo sobre el papel.
- Ensayos sin criterios de interrupción ni personal para la seguridad.
- Mejorar tareas que tienen holgura.
- Resultados del ensayo declarados como superados cuando no se cumplió el requisito.
- Conservación forense omitida para ganar tiempo sin una decisión.

El ensayo del TMRP evitó el cuarto error al declarar R6 como no cumplido con doce horas, y mantuvo la generación de imágenes forenses en lugar de omitirla sin una decisión. Los criterios de interrupción y el personal local se fijaron antes de que comenzara el ensayo, y las opciones para cumplir R6 actúan solo sobre las tareas del camino crítico.

### Ejercicios — capítulo 47

**EX093 — Acortar el camino.** *Objetivo:* usar el camino crítico. *Entradas:* laboratorio 17. *Pasos:* (1) haga que `rebuild_scada` dependa solo de `isolate` (hardware de repuesto, imágenes en paralelo) y vuelva a calcular; (2) reduzca además `rebuild_scada` a 1 h (imagen en espera) y vuelva a calcular; informe cada vez del nuevo camino crítico. *Evidencia esperada:* salidas. *Rúbrica:* 3 = resultados correctos (ejecute el código) y la observación de que el camino crítico pasa a otra cadena; 2 = cifras correctas, camino no comentado; 1 = no ejecutado; 0 = nada.

**EX094 — Análisis forense frente a rapidez.** *Objetivo:* tomar una decisión de compromiso documentada. *Entradas:* omitir la generación de imágenes forenses acorta la recuperación. *Pasos:* redacte una nota de decisión para el director de operaciones: opciones, consecuencias para la investigación, aspectos legales/regulatorios y prevención futura, recomendación. *Evidencia esperada:* una página. *Rúbrica:* 3 = generación de imágenes en paralelo en hardware de repuesto como opción preferida, riesgos de perder evidencia explicados, responsable de la decisión; 2 = recomienda omitirla sin consecuencias; 1 = vaga; 0 = nada.

### Síntesis del capítulo

La recuperación debe ensayarse para que se pueda confiar en ella. Diseñe ensayos con límites de seguridad y mediciones, encuentre el camino crítico, mejore solo lo que está en él e informe del estado del requisito que el ensayo muestra realmente; después, cambie el diseño o el requisito con las partes interesadas.

<!-- open-cyber-academy:chapter-navigation:start ch-47 -->
### Siga estudiando — capítulo 47 de 50

[← Capítulo 46](#ch-46) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 48 →](#ch-48)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-48"></a>

## Capítulo 48 — Expediente de evidencia

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) reunir un expediente de evidencia de ingeniería que respalde las afirmaciones del proyecto final; (2) organizar la evidencia por afirmación con su procedencia; (3) proteger la evidencia sensible manteniéndola revisable; y (4) comprobar la coherencia del expediente antes de su entrega. Reúne los capítulos 44–47 y prepara la tesis de ingeniería.

### 48.1 Qué es el expediente

El expediente de evidencia es el conjunto de artefactos que respalda el caso de aseguramiento: los requisitos y la trazabilidad; los documentos de diseño y los registros de decisiones; los análisis (modelos de amenazas, árboles de fallos, rendimiento, fiabilidad); los registros de implementación (revisión del código fuente, SBOM, procedencia de la compilación); los resultados de la verificación y la validación; los hallazgos de la revisión y las respuestas; los informes de los ensayos; los documentos operativos; y el registro de riesgos residuales con sus responsables. Organícelo por afirmación, no por fecha: un revisor debería poder partir de una afirmación y encontrar su evidencia en dos clics.

Para el TMRP, las afirmaciones del expediente son C1 a C4.

### 48.2 Procedencia

Cada elemento de evidencia indica qué es, quién lo produjo, cuándo, a partir de qué versión del sistema y con qué herramientas. Las cifras de la tesis deben poder trazarse hasta un archivo de resultados (compárese con la comprobación de procedencia del libro de maestría, en su capítulo 7). Use hashes de contenido para los archivos de resultados y regístrelos en un índice, como hace con los registros la cadena de hashes del capítulo 13. Para el TMRP, cada entrada del índice del expediente lleva una versión, como la versión publicada de la pasarela o la fecha del ensayo, y los primeros caracteres de su hash.

### 48.3 Sensibilidad

Los expedientes sobre infraestructuras contienen detalles sensibles. Mantenga una versión completa restringida para los revisores autorizados y una versión censurada para públicos más amplios, y registre qué se censuró y por qué. En los trabajos del curso con casos sintéticos la sensibilidad es menor, pero practique la disciplina. Para el TMRP, la versión restringida incluiría las configuraciones de las pasarelas y los procedimientos de gestión de claves, mientras que la versión censurada describe la arquitectura al nivel de zonas y conductos. El registro de censura enumera cada elemento eliminado y el motivo, de modo que un revisor de la versión censurada sabe qué se ha retenido y puede solicitar acceso por la vía adecuada.

### 48.4 Comprobación de coherencia

Antes de la entrega: cada afirmación tiene evidencia; cada cifra de la tesis coincide con su fuente; los estados concuerdan entre documentos (nada de «superada» en uno y «fallida» en otro, como en el hallazgo F1 del capítulo 45); los riesgos residuales tienen responsable; y todos los hallazgos de la revisión están cerrados o tienen un tratamiento decidido. El expediente del TMRP no superó esta comprobación una vez, cuando C2 citaba T3 como superada mientras la matriz aún la mostraba como fallida. La corrección consistió en registrar la repetición de la prueba en v2 como T3b y actualizar todos los documentos que se referían a ella, de modo que el índice muestra ahora el mismo estado en todas partes.

### 48.5 Ejemplo resuelto: extracto del índice del expediente (sintético)

| Afirmación | Evidencia | Versión | Hash (primeros 12) | Estado |
|---|---|---|---|---|
| C1 R1 cumplido | Resultados de T1/T2; campaña de 10k mensajes | gw v1.3.0 | 3f9a1c0b7e22 | Superado |
| C2 las órdenes falsificadas no pueden causar una pérdida de suministro | Condicionamiento del laboratorio 9; T3b; revisión de la gestión de claves | registro de riesgos v1.2 | 8b01d4e6aa90 | Respaldada con los derrotadores D1, D2 |
| C3 R6 restablecimiento ≤ 8 h | Informe del ensayo de recuperación | ensayo 2026-09-14 | c47e2b19f5d3 | **No cumplido (12 h)**; opciones en el ADR-015 |
| C4 R5 batería de 24 h | Análisis de dimensionamiento; prueba de descarga T4 | armario v2 | 51d7a0e8c4f6 | Superado |

(Los hashes son marcadores ilustrativos para el caso sintético).

### 48.6 Actividad práctica

Construya el índice de su expediente con hashes de contenido reales de sus archivos de resultados (`hashlib.sha256`) y ejecute la comprobación de coherencia del §48.4. Use el script del EX095 para calcular los hashes y guarde el índice bajo control de versiones para que su historial forme parte de la evidencia. Después, ejecute la comprobación de coherencia frente al borrador de su tesis. Cada cifra del borrador debe aparecer en un archivo de resultados incluido en el índice, y cada estado debe coincidir. Corrija primero cualquier discrepancia en el documento fuente y, después, vuelva a generar el índice.

### 48.7 Errores comunes y límites

- Expedientes organizados por fecha o por autor en lugar de por afirmación.
- Cifras de la tesis sin archivo fuente.
- Incoherencias de estado entre documentos.
- Censura sin registro.

El índice del TMRP evita el primer error organizando la evidencia por afirmación, y su registro de C3 como no cumplido impide que aparezca el tercero. Un registro de censura acompaña a la versión compartida. Cada cifra de la tesis se traza hasta un archivo de resultados incluido en el índice, y la versión compartida lleva un registro de lo que se censuró y por qué.

### Ejercicios — capítulo 48

**EX095 — Script de índice.** *Objetivo:* automatizar la procedencia. *Entradas:* una carpeta de resultados. *Pasos:* escriba un script con la biblioteca estándar que recorra la carpeta, calcule el SHA-256 de cada archivo y escriba un índice CSV con la ruta, el tamaño, el hash y la hora de modificación; explique por qué la hora de modificación es una evidencia débil. *Evidencia esperada:* script y explicación. *Rúbrica:* 3 = script que funciona, explicación (la mtime se cambia fácilmente; el hash junto con un commit del control de versiones es más sólido); 2 = sin explicación; 1 = no funciona; 0 = nada.

**EX096 — Auditoría de coherencia.** *Objetivo:* detectar incoherencias. *Entradas:* el extracto del §48.5 y una frase del resumen: «Todos los requisitos se verificaron y el sistema restablece la operación remota en menos de 8 horas». *Pasos:* identifique la incoherencia y reescriba la frase. *Evidencia esperada:* reescritura. *Rúbrica:* 3 = identifica la contradicción con C3, reescritura precisa y aún positiva donde está justificado; 2 = reescritura vaga; 1 = no la detecta; 0 = nada.

### Síntesis del capítulo

El expediente es el conjunto de evidencia, organizado por afirmación y con su procedencia trazada, que sustenta el caso de aseguramiento. Mantenga versiones restringida y censurada con un registro de censura, y compruebe la coherencia de cada afirmación, cifra y estado antes de que lo haga cualquier otra persona.

<!-- open-cyber-academy:chapter-navigation:start ch-48 -->
### Siga estudiando — capítulo 48 de 50

[← Capítulo 47](#ch-47) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 49 →](#ch-49)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-49"></a>

## Capítulo 49 — Tesis de ingeniería

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) estructurar una tesis de ingeniería en torno a un problema de diseño, una solución y la evidencia; (2) redactar resultados y limitaciones que no vayan más allá de la evidencia; (3) presentar resultados cuantitativos con su incertidumbre y su procedencia; y (4) preparar una tesis que un examinador pueda verificar. Convierte el expediente en un documento y prepara la defensa.

### 49.1 La tesis de ingeniería

Una tesis de ingeniería sostiene que un sistema diseñado satisface una necesidad bajo restricciones, con el respaldo de la evidencia de verificación y validación. No es una tesis de investigación (de eso se ocupa el [libro de maestría](../../../../masters-2-years/critical-sector-security/es/book/MANUSCRIPT.md)) ni necesita afirmar una contribución original al conocimiento (el [libro de doctorado](../../../../doctorate-2-years/critical-sector-security/es/book/MANUSCRIPT.md)). Su originalidad, si la tiene, reside en el diseño y en la calidad de su evidencia.

Para el TMRP, la tesis sostiene que la pasarela segura ante reinicios cumple R1, R2 y R7 en el banco de pruebas y declara R6 como no cumplido.

### 49.2 Estructura

1. **Introducción:** necesidad, partes interesadas, consecuencia, alcance.
2. **Antecedentes:** contexto del sector, normas pertinentes y diseños previos, con fuentes.
3. **Requisitos:** requisitos derivados, con sus fuentes y métodos de verificación.
4. **Diseño:** alternativas, selección, arquitectura, controles, con registros de decisiones.
5. **Análisis:** análisis de amenazas y fallos, rendimiento, fiabilidad.
6. **Implementación:** qué se construyó, cómo y con qué herramientas.
7. **Verificación y validación:** métodos, resultados, fallos y correcciones.
8. **Discusión:** estado de los requisitos, riesgos residuales, limitaciones, qué haría de otra manera.
9. **Conclusión:** qué se logró y qué queda pendiente.
Apéndices: matriz de trazabilidad, índice del expediente, código de los laboratorios.

La tesis del TMRP sigue esta estructura.

### 49.3 Resultados y limitaciones

Informe con honestidad del estado de los requisitos: cumplido, cumplido tras corrección, no cumplido, no verificado. Para cada limitación, indique a qué afirmaciones afecta y en qué dirección: «el banco de pruebas usa relojes perfectos; la deriva real del reloj aumentaría los rechazos de mensajes obsoletos, por lo que la tasa de falsos obsoletos indicada es una cota inferior». Una limitación sin dirección es decoración. El párrafo de discusión del TMRP en el ejemplo resuelto que sigue ofrece una limitación de este tipo: el banco de pruebas usó una red sintética, de modo que el umbral de sesenta segundos de la alarma de estación sin datos debe reajustarse in situ, donde la congestión de LTE puede aumentar las falsas alarmas. Esa frase nombra la afirmación afectada y la dirección probable.

### 49.4 Escribir bien

Abra cada capítulo con su idea principal. Use figuras con ejes rotulados y unidades, y tablas para los valores exactos. Mantenga las cifras trazables hasta el expediente. Escriba en un lenguaje técnico claro, defina los términos en su primer uso y use un glosario. Para el TMRP, la tabla del estado de los requisitos aparece al principio de la discusión, y cada cifra que contiene se traza hasta una entrada del índice del expediente con su hash. Cada capítulo se abre con su idea principal, y términos como alarma de estación sin datos se definen en su primer uso y en el glosario, de modo que un examinador puede leer cualquier capítulo sin tener que ir a buscar definiciones.

### 49.5 Ejemplo resuelto: párrafo de discusión (sintético)

> La pasarela cumplió R1 y R2 en el banco de pruebas, incluidos los reinicios de cualquiera de los dos extremos, después de modificar el receptor para que conservara su último contador aceptado (sección 7.3). R7 se cumplió para las alarmas prioritarias y, tras el hallazgo de revisión F2, para la pérdida de datos. R6 no se cumplió: el ensayo de recuperación restableció la operación remota en 12 h frente a un requisito de 8 h, porque la generación de imágenes forenses y la reconstrucción están en serie en el camino crítico. El suministro al hospital se mantuvo en modo local durante todo el ensayo, de modo que la consecuencia del incumplimiento es una menor visibilidad y capacidad de intervención, no una pérdida de suministro. En el ADR-015 se valoran dos opciones de diseño que cumplirían las 8 h. Todos los resultados proceden de un banco de pruebas sintético; el rendimiento en campo, en particular la latencia de LTE con congestión, puede diferir, y el umbral de 60 s de la alarma de estación sin datos debe reajustarse in situ.

### 49.6 Actividad práctica

Redacte el capítulo de discusión de su tesis, con una tabla del estado de los requisitos y limitaciones con dirección. Use como modelo el párrafo de discusión del TMRP. Empiece con una tabla que dé el estado de cada requisito como cumplido, cumplido tras corrección, no cumplido o no verificado. Después, redacte un párrafo por cada resultado significativo, incluido cualquier requisito que no haya cumplido, y termine con sus limitaciones, cada una con la afirmación a la que afecta y la dirección del sesgo probable. Compruebe cada cifra frente al índice de su expediente antes de entregar.

### 49.7 Errores comunes y límites

- Tesis organizadas como diarios.
- Estado de los requisitos redondeado al alza.
- Limitaciones sin dirección ni afirmaciones afectadas.
- Cifras que no coinciden con el expediente.

La tesis del TMRP evita cada uno de ellos: está organizada por argumentos, declara R6 como no cumplido, da limitaciones con dirección y toma sus cifras del índice del expediente. Su tabla del estado de los requisitos se comprueba frente al expediente antes de la entrega, de modo que nada se redondea al alza. Sus limitaciones nombran el banco de pruebas sintético y el ensayo de recuperación único, y dicen en qué dirección podría sesgar cada una los resultados.

### Ejercicios — capítulo 49

**EX097 — Limitaciones con dirección.** *Objetivo:* redactar limitaciones útiles. *Entradas:* tres limitaciones: modelo de ruido sintético; banco de pruebas sin LTE real; un solo ensayo de recuperación. *Pasos:* para cada una, indique la afirmación afectada y la dirección del sesgo probable. *Evidencia esperada:* tres frases. *Rúbrica:* 3 = cada una tiene afirmación y dirección (p. ej., un solo ensayo no da ninguna estimación de la variabilidad, por lo que las 12 h podrían ser optimistas o pesimistas; la latencia real de LTE aumentaría los rechazos por obsolescencia y la latencia de las alarmas); 2 = falta una dirección; 1 = solo una lista; 0 = nada.

**EX098 — Resumen.** *Objetivo:* resumir con exactitud. *Entradas:* §49.5. *Pasos:* redacte un resumen estructurado de 150 palabras (necesidad, diseño, métodos, resultados, limitaciones). *Evidencia esperada:* resumen. *Rúbrica:* 3 = exacto, incluido R6 no cumplido, con el límite del banco de pruebas sintético declarado; 2 = una exageración; 1 = vago; 0 = nada.

### Síntesis del capítulo

Una tesis de ingeniería argumenta desde la necesidad hasta el diseño y la evidencia. Estructúrela para un examinador, informe del estado de los requisitos tal como es, dé a cada limitación una afirmación afectada y una dirección, y mantenga cada cifra trazable hasta el expediente.

<!-- open-cyber-academy:chapter-navigation:start ch-49 -->
### Siga estudiando — capítulo 49 de 50

[← Capítulo 48](#ch-48) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 50 →](#ch-50)

Continúe con la siguiente lección escrita.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-50"></a>

## Capítulo 50 — Defensa final

### Resultados de aprendizaje y conexión

Al terminar este capítulo, usted podrá (1) preparar una presentación técnica para la defensa de un proyecto final y una tesis; (2) anticipar las preguntas de los examinadores por familias y preparar respuestas basadas en la evidencia; (3) tratar con honestidad las preguntas que no puede responder; y (4) planificar las correcciones y el traspaso tras la defensa. Cierra el curso.

### 50.1 Qué evalúan los examinadores

Los examinadores comprueban que el candidato entiende la necesidad y las restricciones; tomó decisiones de diseño defendibles; verificó las afirmaciones con competencia; conoce los límites de la evidencia; y sabe razonar sobre cambios («¿y si el requisito fuera de 2 h?»). Leen la tesis con atención e indagan en las incoherencias. En la defensa del TMRP, es probable que los examinadores indaguen en el incumplimiento de R6 y en el riesgo residual aceptado D1. Pueden preguntar qué cambiaría si la reserva del hospital fuera de dos horas en lugar de cuatro, y el candidato debería razonar a partir del árbol de fallos y del modo automático local en lugar de hacer conjeturas.

### 50.2 La presentación

Veinte minutos: necesidad y consecuencia (2 min); requisitos (2); alternativas y selección (3); arquitectura y controles clave (4); resultados de la verificación y la validación con fallos y correcciones (5); estado de los requisitos y riesgos residuales (2); limitaciones y próximos pasos (2). Un mensaje por diapositiva. Muestre la tabla del estado de los requisitos; los examinadores respetan un «no cumplido» dicho con claridad. Para el TMRP, la tabla del estado de los requisitos mostraría R1, R2 y R7 como cumplidos tras correcciones y R6 como no cumplido con doce horas, con las opciones del ADR-015. Esa diapositiva prepara al tribunal para las preguntas del ejemplo resuelto, y declarar el incumplimiento antes de que lo encuentre un examinador genera más confianza que cualquier resultado pulido.

### 50.3 Familias de preguntas

- **Necesidad:** ¿por qué importa esto, a quién y cómo lo sabe?
- **Diseño:** ¿por qué esta alternativa y no aquella; qué le haría cambiar de elección?
- **Análisis:** ¿de dónde sale esta cifra; y si este supuesto es erróneo?
- **Verificación:** ¿cómo sabe que la prueba prueba el requisito; qué se les escapó a sus pruebas?
- **Límites:** ¿qué no puede afirmar; qué revelaría un despliegue en campo?
- **Ética y seguridad funcional:** ¿qué podría salir mal para las personas; quién es responsable del riesgo residual?

Prepare dos respuestas por familia con referencias al expediente.

### 50.4 Respuestas honestas

Cuando no sepa algo: dígalo, diga cómo lo averiguaría y, si puede, razone en voz alta hacia una respuesta, presentándolo como razonamiento. No invente cifras. Cuando un examinador encuentre un error: reconózcalo, evalúe su impacto en las afirmaciones y proponga una corrección. En el ejemplo resuelto, el candidato hace esto cuando se le pregunta por el riesgo residual D1: indica quién lo aceptó, la evidencia que lo acota y la alternativa que lo eliminaría, sin fingir que el riesgo es despreciable. No se inventa ninguna cifra.

### 50.5 Después de la defensa

Las correcciones se enumeran en una tabla: petición del examinador, cambio realizado, ubicación. Entregue el artefacto y el expediente al patrocinador con las limitaciones conocidas y las necesidades de mantenimiento. En los proyectos reales, encauce cualquier hallazgo de seguridad a través de los procesos del propietario. Para el TMRP, el traspaso se hace al director de operaciones de la LRWA con el expediente, el punto abierto sobre R6 y la nota de que el umbral de la alarma de estación sin datos necesita reajustarse in situ. Cualquier hallazgo de seguridad sobre equipos reales seguiría los procesos propios de la LRWA, no la tesis.

### 50.6 Ejemplo resuelto: responder a una pregunta difícil (sintético)

*Examinador:* «Su caso de aseguramiento acepta el riesgo residual D1: un centro SCADA comprometido que emite órdenes auténticas. ¿Por qué es aceptable para el suministro a un hospital?». *Candidato:* «Lo acepta el director de operaciones, no yo, y el caso explica por qué: los límites locales (R3) mantienen cualquier consigna aceptada dentro de límites seguros, de modo que lo peor que puede hacer un centro comprometido en PS4 es detener las bombas, y el árbol de fallos muestra que, para perder el suministro, tendrían que fallar además la vía del depósito y el tanque del hospital. Si los examinadores lo consideran insuficiente, la alternativa del ADR-012 (escrituras de consignas solo locales en PS4) elimina el control remoto en ese emplazamiento con un coste de personal estimado de una salida de guardia al mes. No afirmaría que D1 es despreciable; afirmo que está acotado y tiene responsable».

### 50.7 Actividad práctica

Celebre una defensa simulada con dos compañeros que actúen como examinadores usando las familias de preguntas; registre las preguntas que no pudo responder y prepare las respuestas. Pida a sus examinadores que usen todas las familias de preguntas y que indaguen en al menos una cifra de su tesis. Registre cada pregunta que no pudo responder y, después, trace la respuesta hasta su expediente. Para el TMRP, las preguntas más difíciles se refieren al incumplimiento de R6 y al riesgo residual D1; prepare esas respuestas hasta que pueda darlas de forma breve, nombrando la evidencia y sin afirmar más de lo que respalda el expediente.

### 50.8 Errores comunes y límites

- Presentaciones que ocultan los fallos.
- Respuestas a la defensiva ante los errores encontrados.
- Cifras inventadas bajo presión.
- Ningún plan de correcciones.

El candidato del TMRP evita estos errores mostrando el incumplimiento de R6 en una diapositiva, reconociendo los errores con claridad, negándose a inventar cifras y teniendo preparada una tabla de correcciones para las peticiones de los examinadores. Los fallos, como la reproducción tras el reinicio, se presentan como hallazgos que detectó la verificación, con la corrección y la nueva prueba, que es exactamente lo que los examinadores quieren ver. Una tabla de correcciones está preparada. Toda afirmación se mantiene dentro del expediente.

### Ejercicios — capítulo 50

**EX099 — Banco de preguntas.** *Objetivo:* anticipar el examen. *Entradas:* su tesis o el caso del TMRP. *Pasos:* redacte doce preguntas (dos por familia) y respuestas breves basadas en la evidencia con referencias al expediente. *Evidencia esperada:* banco. *Rúbrica:* 3 = preguntas difíciles y específicas con respuestas honestas que incluyen los límites; 2 = preguntas blandas; 1 = respuestas sin evidencia; 0 = nada.

**EX100 — Tabla de correcciones.** *Objetivo:* planificar las correcciones. *Entradas:* peticiones de los examinadores: (1) informar de la variabilidad del tiempo de recuperación; (2) justificar la fracción utilizable de la batería de 0,6; (3) eliminar la afirmación de que el detector «impide» los ataques. *Pasos:* redacte una tabla de correcciones con el cambio, la ubicación y cómo se respalda cada uno. *Evidencia esperada:* tabla. *Rúbrica:* 3 = (1) reconoce el ensayo único y añade un plan o ejecuciones simuladas repetidas, (2) añade la fuente del fabricante o un análisis de sensibilidad, (3) reformulación a «detecta»; 2 = una débil; 1 = sin ubicaciones; 0 = nada.

### Síntesis del capítulo

La defensa pone a prueba la comprensión, el criterio y la honestidad sobre los límites. Presente con claridad la necesidad, el diseño, la evidencia y el estado; prepárese por familias de preguntas con referencias al expediente; responda lo que sabe, razone de forma transparente sobre lo que no sabe y convierta los hallazgos de los examinadores en una tabla de correcciones precisa y en un traspaso responsable.

<!-- open-cyber-academy:chapter-navigation:start ch-50 -->
### Siga estudiando — capítulo 50 de 50

[← Capítulo 49](#ch-49) · [Índice de capítulos del curso](../SUBJECTS.md) · [Siguiente curso desde el índice de capítulos →](../SUBJECTS.md)

Este es el último capítulo de este curso; el índice enlaza con el siguiente curso del itinerario completo de estudio.
<!-- open-cyber-academy:chapter-navigation:end -->

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

### Capítulo 27

**EX053.** Límite diseñado: ninguna (mecánico). Límites del controlador: PLC de dosificación. Alarma del analizador: registrador separado y sus comunicaciones. Registro y alarma de los rechazos: a través del SCADA, compartido con el sistema que podría estar comprometido. Cambio: registro local no volátil de los rechazos en el PLC y un camino de alarma independiente (del registrador del analizador a la sala de control por una ruta separada).

**EX054.** Las órdenes fallan cerradas: si la pasarela falla, no pasa ninguna orden. La telemetría falla de forma visible: el SCADA genera una alarma de estación sin datos en menos de 60 s. El control local continúa automáticamente dentro de los límites impuestos localmente. Parar la estación convertiría la falla de un componente de seguridad en una falla de suministro.

### Capítulo 28

**EX055.** Con `old` = 5.2: v1: NaN aceptado (todas las comparaciones son falsas); +∞ rechazado (`> hi`); −∞ rechazado (`< lo`); 5,5 aceptado (|5,5 − 5,2| = 0,3 ≤ 0,5, límite inclusivo); 5,50001 rechazado (`> hi`). v2 rechaza NaN y ±∞ mediante `isfinite`, acepta 5,5 y rechaza 5,50001.

**EX056.** Campos: marca de tiempo UTC y fuente de tiempo; ID de la pasarela; ID de la estación; código de motivo (etiqueta, repetición, sin datos recientes, forma, rango); valor del contador (si puede analizarse); último contador aceptado; SHA-256 de la trama recibida; dirección de origen. Excluya el material de claves y la carga útil completa de las órdenes cuando pueda revelar consignas sensibles a quienes leen los registros; el hash de la trama permite correlacionar sin divulgar.

### Capítulo 29

**EX057.** Exhaustividad 5/7 ≈ 0,714; FPR de la prueba 3/7 ≈ 0,429. Por cada 1.000 eventos con uno malicioso: TP esperados ≈ 0,714, FP ≈ 428. Precisión operativa ≈ 0,0017. Interpretación: la estimación de la FPR a partir de 7 eventos benignos es sumamente incierta, pero incluso una mejora de un orden de magnitud deja el detector inutilizable para avisos de guardia; necesita una FPR mucho menor, medida sobre muchos más datos benignos.

**EX058.** Base: 40 % × 4 h = 160 %·h, más el triángulo de recuperación 0,5 × 8 × 40 = 160 → 320 %·h. Con el modo manual local al 85 %: 15 × 4 = 60, más 0,5 × 8 × 15 = 60 → 120 %·h. R4 reduce la pérdida de resiliencia en torno a un 62 % en este caso sintético.

### Capítulo 30

**EX059.** NaN da falso en cualquier comparación, de modo que las comprobaciones negativas de v1 nunca lo rechazan, mientras que ±∞ fallan en `> hi` o en `< lo`. Unos 2.000/10 = 200 casos de valores especiales, una quinta parte NaN → unos 40 esperados; 31 observados (el generador extrajo 31 casos NaN con la semilla 30), dentro de la variación aleatoria (desviación típica binomial ≈ 5,7). Todo caso NaN es una aceptación insegura de v1, así que los 31 fallos son exactamente los casos NaN.

**EX060.** Casos: (1) contadores 1, 2, 3 → todos aceptados; (2) repetición de 2 → rechazado; (3) contador inferior → rechazado; (4) reinicio del receptor y luego repetición de un mensaje antiguo → rechazado (requiere estado persistido o rotación de claves); (5) reinicio del emisor → reanuda en el valor persistido + 1.000, aceptado; contadores antiguos rechazados; (6) entrega fuera de orden (3 antes que 2) → 3 aceptado, 2 rechazado y registrado (comportamiento documentado); (7) contador en el máximo 2⁶⁴ − 1 → se requiere rotación de claves antes del desbordamiento; pruebe que el emisor se niega a desbordar. Criterios de aprobación: resultados exactos de aceptación o rechazo y entradas de registro.

### Capítulo 31

**EX061.** Desencadenantes: falta telemetría de PS4 durante > 5 min con el enlace activo; cualquier trama aceptada que no supere la auditoría posterior; latencia de alarmas prioritarias > 60 s en dos eventos en una hora; cambio inesperado del estado de una bomba. Responsable de la decisión: el jefe de operaciones de turno. Reversión completada en 1 h (muy por debajo de la reserva de 4 h del hospital), con PS4 en automático local durante todo el proceso.

**EX062.** Controles: bastionado del sistema operativo y de los servicios; actualizaciones de firmware firmadas; clave en un elemento seguro; filtrado de códigos de función y de rango de registros; interruptor de manipulación del armario con alarma hacia el SCADA; registro local y reenviado; puertos no usados deshabilitados; cerraduras físicas. Riesgo residual: un atacante con acceso físico al armario abierto puede conectarse al enlace serie heredado y dar órdenes directamente a la RTU; la detección de manipulación reduce el tiempo de permanencia, pero no lo impide.

### Capítulo 32

**EX063.** Con dos cuadrillas, la transición del estado 2 de vuelta al estado 1 tiene tasa 2μ, de modo que $p_2 = p_0 \cdot 2r \cdot r/2 = p_0 r^2$, con $r = \lambda/\mu$. Indisponibilidad ≈ 1,41 × 10⁻⁴, igual a la de la fórmula ingenua independiente, porque la reparación independiente es exactamente lo que esa fórmula supone. Con una cuadrilla: 2,81 × 10⁻⁴, aproximadamente el doble.

**EX064.** Con un MTTR de 504 h y una cuadrilla: indisponibilidad ≈ 0,078 (unos 28 días al año con ambas bombas paradas), frente a 2,8 × 10⁻⁴ con un repuesto. Mantenga una bomba de repuesto: su coste es insignificante frente a semanas de suministro por una sola vía al hospital.

### Capítulo 33

**EX065.** Filas modelo para el lazo de dosificación (pérdidas: agua no apta; daño por sobredosificación): no proporcionada: el controlador no aumenta la dosis cuando sube la demanda (retroalimentación de caudal defectuosa); proporcionada cuando es insegura: el controlador aumenta la dosis cuando el residual ya es alto (lectura del analizador falsificada por un atacante); momento equivocado: el aumento de dosis se aplica después de que el caudal haya bajado (retardo en la retroalimentación); demasiado tiempo: la dosificación continúa después de que el caudal se detiene (señal de caudal bloqueada). Restricciones: supervisión independiente del residual, dosis enclavada con el caudal, límite físico de carrera.

**EX066.** Violaciones: estación de trabajo de ingeniería compartida (un solo compromiso puede reprogramar tanto la lógica de control como la de seguridad) y conmutador compartido (camino de red y fallo común). Arquitectura: estación de trabajo de ingeniería del SIS dedicada y mantenida sin conexión, cambios en el programa del SIS habilitados solo con un interruptor de llave física, SIS en una red separada o cableado directamente a sus sensores y elementos finales, exportación de datos de solo lectura hacia el sistema de control. Riesgo residual: un interno con la llave física, compromiso de la cadena de suministro del firmware del SIS.

### Capítulo 34

**EX067.** 42 × 180 = 7.560 mensajes; a 50 por segundo, 151,2 s para vaciar la cola; una alarma prioritaria situada al final espera unos 151 s, lo que incumple R7 (60 s). Corrección: cola con prioridad para las alarmas y reenvío del valor más reciente, con relleno del histórico a frecuencia limitada hacia el historiador.

**EX068.** Cláusulas: notificación de incidentes a la LRWA en 1 h desde su detección; divulgación en 72 h de las vulnerabilidades que afecten a la red privada; mantenimientos planificados notificados con 10 días hábiles de antelación; prioridad de restablecimiento para los emplazamientos de la LRWA con un objetivo de 4 h; registros de acceso al APN de la LRWA entregados mensualmente; ejercicio conjunto anual.

### Capítulo 35

**EX069.** R6 (8 h) entra en conflicto con el resultado del ensayo (12 h): R6 no se cumple. El suministro al hospital no depende de la operación remota (modo automático local, 72 h), de modo que la afirmación N1 puede seguir sosteniéndose; el caso de aseguramiento debe registrar R6 como fallido, con un plan de corrección o una revisión acordada con las partes interesadas. Las baterías de 24 h y la reserva de 4 h son coherentes.

**EX070.** D3: mal uso del modo manual local en PS4 por un interno; respuesta: regla de dos personas para el modo manual fuera de las horas de mantenimiento, alarma y CCTV en el panel. D4: compromiso del camino de actualización del firmware de la pasarela; respuesta: actualizaciones firmadas con claves en un HSM, implantación por etapas, supervisión del comportamiento de la pasarela. D5: la persistencia del contador falla tras una pérdida de alimentación; respuesta: prueba de reinicio (EX060) y rotación de claves tras un reinicio no limpio.

### Capítulo 36

**EX071.** μ = 100/s: λ = 20 → ρ = 0,20, W = 12,5 ms, L = 0,25; λ = 40 → ρ = 0,40, W ≈ 16,7 ms, L ≈ 0,67; λ = 48 → ρ = 0,48, W ≈ 19,2 ms, L ≈ 0,92. En comparación con μ = 50 (33,3, 100 y 500 ms), duplicar la capacidad elimina la explosión del retardo durante las tormentas.

**EX072.** (1) Filtrado a nivel de red: solo los extremos de los túneles de las pasarelas pueden llegar al verificador, lo que descarta la mayor parte del tráfico falsificado antes de cualquier cálculo. (2) Comprobaciones previas baratas (longitud, ID de estación conocido, contador plausiblemente por delante del último aceptado) antes de calcular el MAC. (3) Límites de frecuencia por origen y una cola de prioridad estricta para las alarmas verificadas, de modo que las inundaciones se descarten en la prioridad más baja. Añadir capacidad por sí solo pierde frente a un atacante que puede escalar el tráfico.

### Capítulo 37

**EX073.** Debilidades: «no coincide con una acción del operador» es ambiguo; defínalo como la ausencia de una orden registrada del operador para esa estación y ese parámetro en los 5 min anteriores; no hay datos de contacto: añada los números del jefe de turno y del responsable de seguridad de guardia; restablecer las consignas a distancia podría usar el camino comprometido: especifique el restablecimiento local por parte del técnico de turno si hay fallos de MAC en la pasarela.

**EX074.** Qué ocurrió: un técnico conectó un portátil a la red de PS3 para descargar registros. Por qué tenía sentido: la ruta por el servidor de salto es lenta y exige un ticket; los registros se necesitaban para una llamada con el fabricante esa misma tarde. Defensas que fallaron: sin seguridad de puertos en el conmutador; sin una vía sencilla y aprobada para los registros; el procedimiento suponía que el servidor de salto siempre estaba disponible. Cambios: ofrecer un colector de registros en la DMZ para que los técnicos no tengan que conectarse; habilitar la seguridad de puertos; proporcionar un conjunto de portátiles de mantenimiento analizados; simplificar el acceso por el servidor de salto para la obtención de registros de solo lectura.

### Capítulo 38

**EX075.** Con T3b superada para R3, T8 superada para R4 y T6 superada para R8: no probados ['R9'], probados pero sin superar [], verificados 8/9 (88,9 %). R9 sigue sin verificar hasta que se escriba y se supere una prueba de la alarma independiente de dosificación (por ejemplo, detener la dosificación en el banco de pruebas y cronometrar la alarma en el registrador independiente frente a 15 min). La verificación está completa para los otros ocho requisitos; la validación de N1 aún necesita las actividades con partes interesadas del EX076.

**EX076.** (1) Ejercicio nocturno: el personal de operaciones pasa PS3 y PS4 a manual local con la plantilla nocturna real; se observan el tiempo y los errores; éxito: operación manual en menos de 1 h y presión de suministro mantenida. (2) Aislamiento planificado de PS4 en un periodo de baja demanda, con el responsable de instalaciones del hospital supervisando el almacenamiento in situ y la presión; éxito: suministro mantenido desde el depósito sin que el almacenamiento baje nunca del nivel que da 4 h de reserva. Partes interesadas: jefe de operaciones, instalaciones del hospital, ingeniería del TMRP.

### Capítulo 39

**EX077.** Trama: ID de conjunto (1 byte) ‖ contador ‖ estación ‖ valor ‖ etiqueta, con el MAC calculado también sobre el ID de conjunto (para que no pueda alterarse). El receptor mantiene los conjuntos permitidos por estación, p. ej., {1} → {1, 2} durante la transición → {2}. Prevención de la degradación: en cuanto una estación ha enviado el conjunto 2, se rechaza el conjunto 1 procedente de ella. Retirada: eliminar el conjunto 1 de todos los conjuntos permitidos una vez que todas las estaciones hayan migrado y revocar las claves del conjunto 1.

**EX078.** Revocar la clave de la estación y eliminarla del HSM; eliminar las cuentas de la pasarela; borrar el almacenamiento de la pasarela y de la RTU (o destruirlo); actualizar el inventario, el modelo del sistema y el expediente; eliminar las entradas de la lista de permitidos y las reglas de cortafuegos de las direcciones antiguas; actualizar las líneas base de supervisión; dar de baja o poner en cuarentena los repuestos; registrar la aprobación final de operaciones y de seguridad.

### Capítulo 40

**EX079.** Con la semilla 40, la detección de huecos registra 67 eventos de hueco que cubren 81 contadores ausentes. Los números difieren de los 21 descartes porque todo mensaje que no se acepta (corrompidos (14), retrasados y obsoletos (22), descartados (21) y las posiciones en las que se reprodujo una trama antigua en lugar de la actual (24)) deja su contador sin usar; 14 + 22 + 21 + 24 = 81. Los contadores ausentes consecutivos producen un único evento de hueco, por lo que hay menos eventos que contadores ausentes.

**EX080.** Con las clases de reordenación y reinicio (5 % cada una, semilla 40): los mensajes reordenados que llegan después de su sucesor se rechazan como reproducciones (17); es aceptable si se documenta, puesto que se descartan datos obsoletos y ya se dispone del valor más reciente, pero debe registrarse. Los reinicios del receptor no producen ningún error visible (26 aceptados con normalidad), y ese es el peligro: tras un restablecimiento, cualquier reproducción que llegue antes del siguiente mensaje fresco se aceptaría. Por azar, la campaña no muestra ningún caso así; una prueba determinista (reinicio y, después, reproducción) lo pone al descubierto: un fallo silencioso salvo que el receptor conserve el estado.

### Capítulo 41

**EX081.** 150 k: telemetría autenticada + copias de seguridad desconectadas → 330; 200 k: + modo manual local → 440 (coste 190); 250 k: + RTU de repuesto → 530; 300 k: telemetría autenticada, generador de respaldo, modo manual local, copias de seguridad desconectadas → 590 (coste 280); 350 k: + RTU de repuesto → 680 (coste 340). Beneficio marginal por cada 50 k adicionales: 110, 90, 60, 90; decreciente a grandes rasgos, pero irregular porque los controles son indivisibles.

**EX082.** De las 14 ejecuciones, tres cambian el óptimo a {telemetría autenticada, generador de respaldo de PS4, modo manual local} (coste 250, beneficio 520 con los valores de referencia): beneficio del generador de respaldo × 1,2, copias de seguridad desconectadas × 0,8 o RTU de repuesto × 0,8. Todas las demás ejecuciones mantienen el conjunto de referencia. Conclusión: la telemetría autenticada y el modo manual local son elecciones robustas; los últimos 90 k del presupuesto son un casi empate entre {copias de seguridad desconectadas + RTU de repuesto} y el generador de respaldo, por lo que esa parte de la decisión debe basarse en mejores estimaciones o en criterios no monetarios.

### Capítulo 42

**EX083.** El protocolo incluye: pregunta (¿ofrece el detector acumulativo con el umbral θ < 1 falsa alarma al mes con el ruido medido, detectando a la vez rampas de 0,05 m/h en menos de 2 h?); decisión (desplegarlo y fijar θ y el intervalo de recalibración); diseño (barrido de simulación, 100 semillas por celda); mediciones; regla de análisis fijada de antemano; validación frente a dos semanas de ruido del historiador; límites (mezcla perfecta, caudalímetros honestos, un único depósito).

**EX084.** ¿Qué tasa de falsas alarmas al día veríamos con nuestra tasa de eventos? ¿Qué ataques había en el conjunto de prueba y quién los eligió? ¿Se evaluó con ajuste por puntos o sin fuga de datos (división entrenamiento/prueba por tiempo)? ¿En qué medida se parece el banco de pruebas a nuestra planta en escala y ruido? ¿Cómo se mantiene el rendimiento frente a un atacante adaptativo que conoce el detector?

### Capítulo 43

**EX085.** Se evalúa con la rúbrica; el acuerdo debe nombrar a los supervisores, el alcance, el método de acceso, la confidencialidad, la formación inicial en seguridad, la aprobación de la publicación, la vía para los hallazgos incidentales y una declaración explícita de que el estudiante no probará ni explorará sistemas fuera de las tareas acordadas.

**EX086.** Observación: los operadores registran los cambios de consigna en un cuaderno en papel además de en el SCADA. Conexión: capítulo 13 (procedencia) y capítulo 37 (operaciones). Diferencia: la práctica duplica el registro electrónico; es localmente racional porque el cuaderno sobrevive a las interrupciones del SCADA, facilita el traspaso de turno y goza de confianza. Pregunta: ¿discrepan alguna vez los dos registros y podría el cuaderno servir como comprobación de integridad independiente?

### Capítulo 44

**EX087.** Problemas: alcance sin límites («empresas de agua»), sin requisitos ni criterios de aceptación, sin fuente de datos, tecnología elegida antes que el problema. Reescritura: p. ej., «Un detector basado en residuos para datos de nivel falsos en un único depósito sintético: requisitos, estudio de simulación con ruido con semilla, criterios de aceptación < 1 falsa alarma/mes y detección de rampas de 0,05 m/h en menos de 2 h, 12 semanas, solo datos sintéticos».

**EX088.** Ampliación descontrolada del alcance (probabilidad media, impacto alto; mitigación: congelar el alcance en la CDR; desencadenante: nuevas peticiones de funciones después de la semana 6); seguridad ante reinicios más difícil de lo previsto (M/A; prototipo exploratorio en la semana 2; desencadenante: diseño no estable en la semana 4); fidelidad insuficiente del banco de pruebas (M/M; revisión con el supervisor; desencadenante: hallazgo de un revisor); tiempo (A/A; semana de margen; desencadenante: retraso de un hito > 1 semana); disponibilidad del supervisor (B/M; revisiones programadas; desencadenante: revisión no celebrada).

### Capítulo 45

**EX089.** (1) «Las claves de las 42 estaciones se generan en el portátil de un ingeniero (procedimiento de gestión de claves §3.2); un compromiso de ese portátil expone a toda la flota; incumple la intención de R1; se recomienda la generación en el HSM o en el elemento seguro de la pasarela». (2) «El comportamiento del receptor tras un reinicio no está cubierto por ninguna prueba (plan de verificación, tabla 4); R2 exige rechazar las reproducciones tras un reinicio; se recomiendan pruebas según el EX060». (3) Retirarlo por ser una preferencia de diseño, o replantearlo: «el diseño no indica por qué el protocolo elegido cumple R1 y R7; añadir la justificación».

**EX090.** F2: aceptado; se añaden la alarma de estación sin datos a los 60 s y el registro de huecos de contador; la campaña se vuelve a ejecutar con la semilla 40; responsable: jefe de la pasarela; fecha: dos semanas. F3: aceptado; el expediente se corrige a «R6 no cumplido (12 h)»; opciones valoradas: generación de imágenes en paralelo en hardware de repuesto (9 h), más una imagen del SCADA en espera (6 h); revisión con las partes interesadas para decidir entre un cambio de diseño y un requisito revisado; responsable: director del TMRP; fecha: próxima reunión del comité de dirección.

### Capítulo 46

**EX091.** Generar la nueva clave en el HSM; distribuirla a la pasarela con el ID de clave k+1; durante 10 minutos, el receptor acepta las tramas etiquetadas con cualquiera de los dos ID de clave (el ID de clave va dentro de la cabecera autenticada); el emisor cambia a k+1 y los contadores continúan; si las tramas con k+1 fallan, se revierte a k; tras la ventana, el receptor rechaza k, y k se destruye en ambos extremos; se registra cada paso.

**EX092.** Continuar con condiciones: iniciar el ensayo con el umbral de 60 s, supervisado por un ingeniero; recopilar datos sobre las falsas alarmas de estación sin datos durante la congestión; ajustar el umbral (p. ej., 90 s para las estaciones no críticas) antes de una fecha declarada; informar a los operadores de que se esperan alarmas de estación sin datos durante la congestión. La consecuencia de no detectar una pérdida real de datos pesa más que dos falsas alarmas al día durante un periodo limitado.

### Capítulo 47

**EX093.** (1) Con la reconstrucción dependiendo solo del aislamiento: control remoto a las 9 h; camino crítico aislar → reconstruir → restaurar la configuración → verificar → reanudar; la generación de imágenes sale del camino. (2) Con una reconstrucción de 1 h a partir de una imagen en espera: 6 h; la cadena de la reconstrucción y la del recambio de claves (aislar → recambiar claves → verificar → reanudar) empatan ahora a 6 h, de modo que el recambio de claves se ha vuelto crítico y nuevas mejoras exigen acortarlo también.

**EX094.** Opciones: (a) omitir la generación de imágenes (la más rápida; se pierde la evidencia; pueden pasar inadvertidas la causa raíz y la persistencia del atacante; posibles consecuencias regulatorias o legales); (b) generar las imágenes primero (la más lenta); (c) generar las imágenes en paralelo usando hardware de repuesto y reconstruir en hardware limpio (casi la más rápida; se conserva la evidencia). Recomendación: (c), con una decisión aprobada de antemano según la cual el director de operaciones solo puede autorizar (a) si el suministro está en riesgo. Responsable: director de operaciones.

### Capítulo 48

**EX095.** Script: recorrer la carpeta con `os.walk`; para cada archivo, leerlo por bloques en `hashlib.sha256`; escribir `path, size, sha256, mtime` con `csv.writer`. La hora de modificación es una evidencia débil porque se cambia fácilmente y no está ligada al contenido; un hash de contenido registrado en el control de versiones (ID de commit y etiqueta firmada) es mucho más sólido.

**EX096.** Incoherencia: C3 muestra R6 como no cumplido (12 h). Reescritura: «Se verificaron todos los requisitos salvo el objetivo de restablecimiento de 8 horas; un ensayo de recuperación restableció la operación remota en 12 horas mientras el suministro continuaba en modo local, y se presentan dos opciones de diseño para cumplir el objetivo».

### Capítulo 49

**EX097.** Modelo de ruido sintético → afecta a las afirmaciones sobre las falsas alarmas y el tiempo de detección del detector; es probable que el ruido real no sea gaussiano y tenga deriva, por lo que probablemente se subestiman las falsas alarmas. Banco de pruebas sin LTE real → afecta a las afirmaciones sobre la latencia y los rechazos por obsolescencia; la latencia y la fluctuación reales aumentarían los rechazos por obsolescencia y la latencia de las alarmas. Un solo ensayo de recuperación → afecta al estado de R6; no hay estimación de la variabilidad, por lo que las 12 h podrían ser optimistas o pesimistas.

**EX098.** Ejemplo: «Necesidad: las RTU heredadas de una empresa de servicios de agua aceptan órdenes no autenticadas a través de LTE, lo que pone en riesgo el suministro a un hospital. Diseño: una pasarela que añade autenticación HMAC por estación con contadores seguros ante reinicios, retorno automático a la operación local y alarmas de estación sin datos. Métodos: verificación en banco de pruebas, campañas de inyección de fallos con semilla y un ensayo de recuperación en sistemas sintéticos. Resultados: se cumplieron los requisitos de autenticación y de reproducción, incluidos los reinicios tras una corrección; las alarmas cumplieron los 60 s; el restablecimiento remoto llevó 12 h frente a un objetivo de 8 h mientras el suministro continuaba en local. Limitaciones: banco de pruebas sintético sin LTE real; un único ensayo de recuperación».

### Capítulo 50

**EX099.** Se evalúa con la rúbrica. Entre las preguntas sólidas: «¿Qué ocurre si falla el HSM?»; «¿Por qué 60 s?»; «¿Qué no incluía su modelo de fallos?»; «¿Quién es responsable de D1?»; «¿Qué cambiaría si la reserva del hospital fuera de 1 h?»; las respuestas citan elementos del expediente y declaran los límites.

**EX100.** (1) Añadir la declaración de que un solo ensayo no da ninguna estimación de la variabilidad; añadir 100 ejecuciones simuladas de recuperación con semilla y rangos de duración de las tareas, e informar de la mediana y del percentil 90; sección 7.4 y apéndice C. (2) Citar la recomendación de profundidad de descarga del fabricante de la batería o añadir una tabla de sensibilidad para 0,5–0,8; sección 5.2. (3) Sustituir «impide» por «detecta» y añadir el contexto del tiempo de detección; resumen y sección 8.1.

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
