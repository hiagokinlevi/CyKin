# Infraestructura crítica y seguridad sectorial: fundamentos, evidencia y práctica

- Idioma: español neutro (`es`); curso de grado, cuatro años; aproximadamente 3.200 horas de estudio planificado (curso 115 de 207 en la [ruta de estudio](../../../../../STUDY_PATH.md)). Edición de referencia: [inglés](../../en/book/MANUSCRIPT.md).
- Estado editorial: **borrador**. Los capítulos 1–40 de 40 tienen texto didáctico escrito; los ejercicios EX001–EX080 (dos por capítulo) tienen sus resultados resueltos correspondientes; catorce laboratorios sin conexión están incluidos con su salida verificada. Siguen pendientes la revisión independiente por especialistas, la nueva verificación de las fuentes, la revisión de accesibilidad, la edición lingüística y la verificación de las 300 páginas A4. La meta del plan de tres ejercicios por capítulo aún no se cumple. La cobertura de capítulos en borrador no es un libro terminado.
- Público: estudiantes de seguridad e informática en sentido amplio que quieren trabajar en los servicios de los que las sociedades no pueden prescindir: salud, energía, agua, transporte, finanzas y servicios públicos. Conocimientos de entrada: matemáticas de la educación secundaria, uso básico del computador y la capacidad de leer y escribir prosa clara. El libro construye probabilidad, programación, redes, datos, identidad y criptografía desde el capítulo 1.
- Relación con los demás libros de esta área: el [libro de ingeniería](../../../../engineering-5-years/critical-sector-security/es/book/MANUSCRIPT.md) enseña a *diseñar, construir y verificar* un sistema seguro frente a unos requisitos; el [libro de maestría](../../../../masters-2-years/critical-sector-security/es/book/MANUSCRIPT.md) enseña a diseñar y defender un estudio empírico con revisión ética; el [libro de doctorado](../../../../doctorate-2-years/critical-sector-security/es/book/MANUSCRIPT.md) exige una contribución original al conocimiento. **Este libro de grado trata de amplitud y de juicio**: comprender cómo funcionan varios sectores críticos y cómo dependen unos de otros, leer la evidencia con espíritu crítico, comparar métodos y controles con supuestos explícitos y participar de forma segura en el trabajo de protección y de respuesta a incidentes de una organización real. Su proyecto final (capítulos 35–40) es un proyecto comparativo guiado por la evidencia, no la construcción de un sistema ni una tesis doctoral.
- Autoría y responsabilidad editorial: [hiagokinlevi](https://github.com/hiagokinlevi). El texto didáctico original del mantenedor se dedica bajo [CC0 1.0](../../../../../LICENSE); las obras citadas conservan sus propios derechos y no se relicencian aquí.
- Límite educativo: este curso es un proyecto educativo independiente. No es un título acreditado y no concede autorización para acceder, escanear, probar o modificar ningún sistema real. Toda organización, sitio, dispositivo, dirección, persona y número de un ejemplo resuelto es **sintético**, salvo que una frase cite explícitamente una fuente pública. Nada de lo que aquí aparece es un procedimiento operativo para un hospital, una empresa de servicios, un banco o un operador reales, y nada constituye asesoramiento jurídico.

[Página del curso](../../README.md) · [Índice de capítulos](../SUBJECTS.md) · [Plan del libro](PLAN.md) · [Skill del curso](../../skill/SKILL.md) · [Estándar del libro](../../../../../BOOK_STANDARD.md) · [Resultados resueltos](#worked-results)

## Cómo usar este borrador

Los cuarenta capítulos siguen los ocho semestres del plan. Los **capítulos 1–18** son los fundamentos que necesita todo graduado en seguridad (razonamiento matemático, informática, programación, redacción, cultura de seguridad, estructuras discretas, redes, datos, ética, sistemas operativos, probabilidad, identidad, privacidad, medición, arquitectura, criptografía y método de investigación), cada uno enseñado mediante un ejemplo de servicio crítico desde su primera página. Los **capítulos 19–32** son el núcleo del campo: qué hace «crítica» a una infraestructura, los casos públicos que dieron forma al campo, los modelos de sistemas de la tecnología operacional, las dependencias entre sectores, los métodos de evaluación de riesgos, los controles, la verificación, el análisis de fallas, las operaciones y la respuesta a incidentes, con dos laboratorios (25, 30). Los **capítulos 33–40** son práctica de investigación, un proyecto comparativo, práctica de campo y la secuencia del proyecto final, que termina con una tesis y una presentación.

Cada capítulo tiene resultados de aprendizaje, secciones didácticas con definiciones, un ejemplo resuelto, una actividad práctica, errores comunes y límites, dos ejercicios y una síntesis. Catorce capítulos incluyen un laboratorio sin conexión escrito para la biblioteca estándar de Python 3; las salidas impresas se obtuvieron ejecutando el código con Python 3.13. Escriba su respuesta antes de abrir los [resultados resueltos](#worked-results).

Mantenga cuatro encabezados en sus notas de estudio para cada caso que analice: **servicio** (de qué dependen las personas y con qué rapidez llega el daño cuando se pierde), **dependencia** (qué necesita el servicio: energía, comunicaciones, personas, proveedores, datos), **evidencia** (qué sabe realmente, de qué fuente y con qué límites) y **decisión** (qué recomendaría, comparado con qué alternativa y con qué supuestos). La falla más común en el nivel de grado no es un dato que falta; es una recomendación segura de sí misma que nunca enuncia sus supuestos ni se compara con nada.

### El condado sintético que se usa en este libro

| Elemento sintético | Función | Límite |
|---|---|---|
| El **condado de Calder** y su **County Resilience Partnership (CRP)** | Una región cuyos operadores comparten planes y ejercicios | Inventado; ningún lugar real |
| **Calder Valley Hospital (CVH)**: 420 camas, servicio de urgencias, imagenología, laboratorio, sistema de gestión del edificio (BMS), generadores de reserva | Operador sanitario | Inventado |
| **Calder Power Networks (CPN)**: distribución eléctrica, Substation North, RTU de alimentadores, sala de control, pasarela de acceso remoto | Operador energético | Inventado; no se nombra ningún producto real |
| **Calder Water (CW)**: planta de tratamiento, bombas, 10 horas de almacenamiento de agua tratada, telemetría | Operador de agua | Inventado |
| **Calder Transit (CT)**: tren ligero con señalización y venta de billetes | Operador de transporte | Inventado |
| **Calder Mutual**: un banco regional con servicios de tarjetas y pagos | Operador financiero | Inventado |
| **County Emergency Dispatch Centre (CEDC)**: atención de llamadas y despacho asistido por computador (CAD) | Servicio público | Inventado |
| Todas las direcciones IP (10.x y 198.51.100.x, del rango de documentación), claves, probabilidades, costos (en libras, £) y salidas de los laboratorios | Datos didácticos | Sintéticos; la clave de demostración del Lab 8 es pública y nunca debe usarse |

### Política de fuentes

Las afirmaciones fácticas sobre leyes, normas, incidentes y estudios publicados se enlazan con fuentes públicas cuando se citan. Este borrador **no** ha recibido una verificación independiente fuente por fuente, por lo que el lector debe volver a comprobar la versión exacta, la fecha y el alcance respaldado antes de basarse en una afirmación. Los resultados clásicos (el teorema de Bayes, la definición de función hash y los principios de Saltzer y Schroeder) se acompañan de referencias clásicas. La discusión sobre Oldsmar enlaza tanto un relato inicial como una revisión posterior, para que la acusación inicial no se confunda con una conclusión establecida. Las normas de pago (incluida IEC 62443) se citan mediante páginas públicas de presentación o de catálogo; el borrador no cita cláusulas no verificadas.

## Contenido

1. [Razonamiento matemático](#ch-01)
2. [Sistemas informáticos](#ch-02)
3. [Programación I](#ch-03)
4. [Redacción académica](#ch-04)
5. [Cultura de seguridad](../../en/book/MANUSCRIPT.md#ch-05)
6. [Estructuras discretas](../../en/book/MANUSCRIPT.md#ch-06)
7. [Redes y protocolos](../../en/book/MANUSCRIPT.md#ch-07)
8. [Programación II](../../en/book/MANUSCRIPT.md#ch-08)
9. [Datos y bases de datos](../../en/book/MANUSCRIPT.md#ch-09)
10. [Ética y práctica autorizada](../../en/book/MANUSCRIPT.md#ch-10)
11. [Sistemas operativos](../../en/book/MANUSCRIPT.md#ch-11)
12. [Probabilidad y estadística](../../en/book/MANUSCRIPT.md#ch-12)
13. [Identidad y acceso](../../en/book/MANUSCRIPT.md#ch-13)
14. [Fundamentos de privacidad](../../en/book/MANUSCRIPT.md#ch-14)
15. [Evidencia y medición](../../en/book/MANUSCRIPT.md#ch-15)
16. [Arquitectura de seguridad](../../en/book/MANUSCRIPT.md#ch-16)
17. [Conceptos de criptografía](../../en/book/MANUSCRIPT.md#ch-17)
18. [Métodos de investigación I](../../en/book/MANUSCRIPT.md#ch-18)
19. [Infraestructura crítica y seguridad sectorial: alcance y teoría](../../en/book/MANUSCRIPT.md#ch-19)
20. [Infraestructura crítica y seguridad sectorial: casos fundacionales](../../en/book/MANUSCRIPT.md#ch-20)
21. [Infraestructura crítica y seguridad sectorial: modelos de sistemas](../../en/book/MANUSCRIPT.md#ch-21)
22. [Infraestructura crítica y seguridad sectorial: datos y dependencias](../../en/book/MANUSCRIPT.md#ch-22)
23. [Infraestructura crítica y seguridad sectorial: métodos I](../../en/book/MANUSCRIPT.md#ch-23)
24. [Infraestructura crítica y seguridad sectorial: controles](../../en/book/MANUSCRIPT.md#ch-24)
25. [Laboratorio I](../../en/book/MANUSCRIPT.md#ch-25)
26. [Infraestructura crítica y seguridad sectorial: métodos II](../../en/book/MANUSCRIPT.md#ch-26)
27. [Infraestructura crítica y seguridad sectorial: verificación](../../en/book/MANUSCRIPT.md#ch-27)
28. [Infraestructura crítica y seguridad sectorial: análisis de fallas](../../en/book/MANUSCRIPT.md#ch-28)
29. [Infraestructura crítica y seguridad sectorial: operaciones](../../en/book/MANUSCRIPT.md#ch-29)
30. [Laboratorio II](../../en/book/MANUSCRIPT.md#ch-30)
31. [Infraestructura crítica y seguridad sectorial: casos avanzados](../../en/book/MANUSCRIPT.md#ch-31)
32. [Infraestructura crítica y seguridad sectorial: interfaces interdisciplinarias](../../en/book/MANUSCRIPT.md#ch-32)
33. [Métodos de investigación II](../../en/book/MANUSCRIPT.md#ch-33)
34. [Proyecto comparativo](../../en/book/MANUSCRIPT.md#ch-34)
35. [Propuesta del proyecto final](../../en/book/MANUSCRIPT.md#ch-35)
36. [Práctica de campo o comunitaria](../../en/book/MANUSCRIPT.md#ch-36)
37. [Seminario de revisión de la evidencia](../../en/book/MANUSCRIPT.md#ch-37)
38. [Implementación del proyecto final](../../en/book/MANUSCRIPT.md#ch-38)
39. [Evaluación del proyecto final](../../en/book/MANUSCRIPT.md#ch-39)
40. [Tesis y presentación](../../en/book/MANUSCRIPT.md#ch-40)

Los [resultados resueltos](#worked-results) contienen EX001–EX080. Un [glosario](#glossary) y las [referencias](#references) cierran el libro.

<a id="ch-01"></a>

## Capítulo 1 — Razonamiento matemático

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) convertir una preocupación vaga («¿y si el centro de despacho pierde su enlace a internet?») en una cantidad con unidades; (2) calcular una pérdida anual esperada y explicar por qué no es lo mismo que el peor evento creíble; (3) estimar órdenes de magnitud y comprobar un cálculo acotándolo; y (4) enunciar los supuestos que hay detrás de un número para que otra persona pueda discrepar de ellos con precisión. El capítulo presenta el condado sintético de Calder, que se usa a lo largo de todo el libro, y prepara el capítulo 6 (estructuras discretas) y el capítulo 12 (probabilidad y estadística).

### 1.1 Por qué la seguridad necesita números, y por qué los números no bastan

La seguridad de los sectores críticos está llena de comparaciones. ¿Debe el Calder Valley Hospital gastar dinero en un segundo enlace de red o en probar sus generadores? ¿Debe Calder Power Networks parchear un controlador de alimentador ahora, durante una parada planificada el mes próximo, o nunca? Son decisiones en condiciones de incertidumbre, y la única manera honesta de compararlas es hacer explícita la incertidumbre. El **razonamiento matemático** no significa aquí matemáticas avanzadas. Significa cuatro hábitos: dar una unidad a cada cantidad; anotar de dónde salió cada número; comprobar un resultado estimándolo de otra manera; y decir qué cambiaría la respuesta.

Una **cantidad** es un número con una unidad: 4 horas, £2.000 por hora, 0,3 eventos por año. La mayoría de los errores en la aritmética del riesgo son errores de unidades: multiplicar una probabilidad por año por un costo por hora, o sumar un porcentaje a un recuento. Escribir las unidades junto a cada término, y simplificarlas a medida que avanza, detecta estos errores antes que nadie.

### 1.2 El valor esperado y sus límites

En un modelo anual de un solo evento, si un evento tiene probabilidad $p$ y cuesta $C$ cuando ocurre, su **pérdida anual esperada** (EAL, por sus siglas en inglés) es $p \times C$. Las pérdidas esperadas de componentes de costo distintos se suman incluso cuando los eventos son dependientes: esta es la linealidad de la esperanza. Aun así, el analista debe evitar contar dos veces la *misma* consecuencia cuando los escenarios se solapan. La independencia es necesaria para algunos cálculos de probabilidad, como multiplicar las probabilidades de dos fallas, pero no para sumar costos esperados. El valor esperado ayuda a comparar el costo anual de un control con la pérdida que podría evitar. También puede ocultar diferencias importantes: una catástrofe de 1 entre 100 y una molestia casi segura pueden tener el mismo producto. Para un hospital, una pérdida de energía de 72 horas no es «lo mismo» que setenta y dos pérdidas de una hora: los pacientes que necesitan ventilación, diálisis o cirugía sufren daño por la duración, no por un promedio. Por eso, cada tabla de valor esperado de este libro va acompañada de un **peor evento creíble**: el resultado más grave que usted cree que podría ocurrir de forma realista, enunciado con su duración.

Las probabilidades que se usan en estas tablas rara vez se miden. Son estimaciones a partir de registros de incidentes, informes sectoriales o juicio experto. Eso es aceptable solo si usted lo dice. Un buen hábito es escribir la fuente entre paréntesis («(estimación, jefe de operaciones del CEDC, 2026)») y probar el cálculo con la mitad y con el doble de la estimación. Si la decisión no cambia, la estimación es suficientemente buena; si cambia, necesita más evidencia. El capítulo 15 vuelve sobre esta idea como **análisis de sensibilidad**.

### 1.3 Órdenes de magnitud y acotación

Antes de calcular con precisión, estime. Un hospital de 420 camas podría perder del orden de miles de libras por hora de interrupción en procedimientos cancelados y ambulancias desviadas, no decenas ni millones. Una estimación que cae tres órdenes de magnitud lejos del cálculo cuidadoso es señal de que se ha deslizado una unidad o una coma decimal. La **acotación** es la habilidad relacionada: si no puede estimar una cantidad, busque números entre los que deba estar. Si un programa de pruebas de generadores cuesta como mínimo £8.000 (tiempo del personal) y como máximo £15.000 (tiempo del personal más combustible y contratista), una decisión que se sostiene en ambos extremos no necesita la cifra exacta.

### 1.4 Ejemplo resuelto: dos propuestas en el condado de Calder (sintético)

**Este caso es sintético.** La **County Resilience Partnership (CRP)** del condado de Calder dispone de dinero para una de dos propuestas.

- **A — segundo enlace a internet para el County Emergency Dispatch Centre (CEDC)**, con un costo de £18.000 al año. Sin él, la CRP estima una probabilidad anual de 0,30 de una caída del enlace de 4 horas y de 0,02 de una caída de 48 horas (un cable cortado en la única ruta), cada una con un costo de £2.000 por hora en personal de respaldo y retrasos.
- **B — un programa de pruebas de generadores para el Calder Valley Hospital**, con un costo de £12.000 al año. Sin él, la estimación es una probabilidad de 0,10 de que el generador no arranque durante 12 horas en un corte de la red y de 0,01 de una falla de 72 horas, cada una con un costo de £5.000 por hora.

Para A, EAL = 0,30 × 4 h × £2.000/h + 0,02 × 48 h × £2.000/h = £2.400 + £1.920 = £4.320 al año. Para B, EAL = 0,10 × 12 × 5.000 + 0,01 × 72 × 5.000 = £6.000 + £3.600 = £9.600. Ninguna opción «se paga sola» en términos esperados (cocientes 0,24 y 0,80), algo habitual en el gasto en resiliencia: compramos protección contra las colas, no contra los promedios. Los peores eventos creíbles (£96.000 y £360.000) hacen de B el caso más sólido, y el daño de B recae sobre pacientes, algo que ninguna cifra en libras expresa del todo. La recomendación es B, con el supuesto explícito de que las estimaciones de probabilidad son correctas dentro de un factor de dos.

### 1.5 Actividad práctica: Lab 1

El laboratorio reproduce la comparación. Cambie una probabilidad cada vez por un factor de dos y observe si cambia la clasificación.

```python
# Lab 1 - expected loss versus worst credible case for two options (synthetic Calder data, offline)
options = {
    "A: second ISP link for dispatch centre": {"cost": 18_000, "scenarios": [(0.30, 4, 2_000), (0.02, 48, 2_000)]},
    "B: backup generator test programme":     {"cost": 12_000, "scenarios": [(0.10, 12, 5_000), (0.01, 72, 5_000)]},
}
# each scenario: (annual probability it occurs without the option, outage hours, loss per hour in GBP)
for name, o in options.items():
    eal = sum(p * h * c for p, h, c in o["scenarios"])
    worst = max(h * c for p, h, c in o["scenarios"])
    print(f"{name}: expected annual loss avoided = {eal:,.0f}; worst single event = {worst:,.0f}; cost = {o['cost']:,}")
    print(f"   ratio avoided/cost = {eal / o['cost']:.2f}")
```

Salida esperada:

```text
A: second ISP link for dispatch centre: expected annual loss avoided = 4,320; worst single event = 96,000; cost = 18,000
   ratio avoided/cost = 0.24
B: backup generator test programme: expected annual loss avoided = 9,600; worst single event = 360,000; cost = 12,000
   ratio avoided/cost = 0.80
```

El laboratorio supone que cada opción elimina por completo sus escenarios. Los controles reales reducen la probabilidad o la duración solo en parte; el ejercicio EX002 le pide modelarlo.

Dos ejecuciones muestran para qué sirve el laboratorio. Reducir a la mitad la probabilidad de 0,10 de B, hasta 0,05, baja su pérdida esperada a £6.600, todavía por encima de los £4.320 de A, de modo que la clasificación se mantiene. Duplicar la probabilidad de 0,02 de A de una caída de 48 horas, hasta 0,04, eleva A a £6.240, todavía por debajo de B. Como ningún cambio individual invierte el orden, la recomendación del programa de generadores es robusta ante un factor de dos en cualquier estimación aislada, que es exactamente lo que afirmaba el ejemplo resuelto.

### 1.6 Errores comunes y límites

- Multiplicar cantidades con unidades incompatibles (una cantidad por año por otra por hora, sin convertir).
- Presentar una probabilidad estimada como si fuera medida.
- Clasificar opciones solo por pérdida esperada cuando el daño a las personas depende de la duración.
- Olvidar que los controles rara vez eliminan un riesgo por completo.
- Sumar probabilidades de eventos que no son mutuamente excluyentes (el capítulo 12 muestra la regla correcta).

Cada error tiene un ejemplo en Calder. El colega de EX001 multiplicó una probabilidad anual por horas y llamó al resultado libras por hora. Escribir «probabilidad de 0,02» sin fuente hace que la conjetura del CEDC parezca una tasa medida. Clasificar A y B solo por pérdida esperada ocultaría que la cola de £360.000 de B son 72 horas sin energía fiable en el hospital. Y el propio supuesto del laboratorio, que cada opción elimina por completo sus escenarios, es el cuarto error, incorporado a propósito en un modelo didáctico.

### Ejercicios — capítulo 1

**EX001 — Disciplina de unidades.** *Objetivo:* encontrar y corregir errores de unidades. *Entradas:* un colega escribe «EAL = 0,02 por año × 48 horas × £2.000 = £1.920 por hora». *Pasos:* (1) simplifique las unidades término a término; (2) indique la unidad correcta del resultado; (3) explique en una frase por qué el error importa al compararlo con un costo anual de £18.000. *Evidencia esperada:* la expresión corregida con unidades. *Rúbrica:* 3 = unidad correcta (£ por año) y una razón clara; 2 = unidad correcta, razón débil; 1 = advierte un error pero lo describe mal; 0 = nada.

**EX002 — Eficacia parcial.** *Objetivo:* modelar un control que solo reduce un riesgo. *Entradas:* Lab 1. *Pasos:* suponga que la opción B reduce a la mitad la probabilidad de cada escenario en lugar de eliminarlo; modifique el laboratorio para calcular la pérdida evitada; luego duplique ambas probabilidades de B y vuelva a calcular. *Evidencia esperada:* dos números y una recomendación de dos frases. *Rúbrica:* 3 = valores correctos (£4.800 y £9.600) y una recomendación que menciona los peores eventos creíbles; 2 = números correctos, argumento débil; 1 = un número; 0 = nada.

### Síntesis del capítulo

Las decisiones de seguridad son comparaciones en condiciones de incertidumbre. Dé unidades a las cantidades, separe la pérdida esperada del peor daño creíble, compruebe los resultados mediante estimación y acotación, y diga qué supuestos cambiarían la decisión. Un número sin fuente ni sensibilidad declaradas es una opinión disfrazada.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Siga estudiando — capítulo 01 de 40

[← Inicio del curso](../../README.md) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 02 →](#ch-02)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Capítulo 2 — Sistemas informáticos

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) describir las capas de un sistema informático (hardware, firmware, sistema operativo, aplicaciones, datos y personas) y decir dónde se toman decisiones de seguridad en cada una; (2) distinguir la tecnología de la información (TI) de la tecnología operacional (TO) y explicar por qué sus prioridades difieren; (3) describir el ciclo de vida de un dispositivo en un servicio crítico, desde la adquisición hasta la eliminación; y (4) explicar por qué el componente más antiguo de un sistema suele determinar su seguridad. Se apoya en el hábito del capítulo 1 de usar cantidades explícitas y prepara el capítulo 3, en el que escribirá código para examinar un inventario de dispositivos.

### 2.1 Capas y confianza

Un computador es una pila. En la base está el **hardware**: procesador, memoria, almacenamiento e interfaces. Encima está el **firmware**, el código de bajo nivel almacenado en el dispositivo que lo arranca y controla el hardware. El **sistema operativo** (capítulo 11) reparte el hardware entre los programas y hace cumplir quién puede hacer qué. Las **aplicaciones** realizan el trabajo que interesa a las personas: la biblioteca de fármacos de una bomba de infusión, un sistema de despacho, un conmutador de pagos. Los **datos** son lo que las aplicaciones crean y consumen. Las **personas** configuran, usan y mantienen todo ello. Cada capa confía en las capas inferiores: una aplicación no puede ser más fiable que el sistema operativo sobre el que se ejecuta, y un sistema operativo no puede detectar un firmware que le miente. Por eso el arranque seguro, el firmware firmado y el soporte del fabricante importan tanto en los servicios críticos (capítulo 17).

### 2.2 TI y TO

La **tecnología de la información** maneja información: correo electrónico, registros, pagos, planificación. La **tecnología operacional** supervisa y controla procesos físicos: válvulas, interruptores, bombas, señales, ventiladores. El NIST describe la TO como sistemas que "interact with the physical environment (or manage devices that interact with the physical environment)", es decir, que interactúan con el entorno físico o gestionan dispositivos que lo hacen ([NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). La distinción importa porque las consecuencias difieren. Cuando falla un sistema de TI, la información no está disponible o es errónea; cuando falla un sistema de TO, el agua puede dejar de fluir, un interruptor puede no abrirse o un tren puede no recibir una señal. Normalmente se espera que los dispositivos de TO funcionen entre 15 y 25 años, pueden no tolerar un reinicio durante la operación y a menudo están certificados en una configuración concreta, de modo que parchearlos requiere la aprobación del fabricante. La atención sanitaria añade una tercera categoría, los **dispositivos médicos**, que son productos regulados cuyo software el hospital no puede cambiar sin más.

### 2.3 El ciclo de vida del dispositivo

La seguridad se decide mucho antes de un ataque. En la **adquisición**, el comprador puede exigir software con soporte, un proceso de divulgación de vulnerabilidades y una lista de materiales de software (SBOM, una lista de los componentes de software; véase [CISA SBOM](https://www.cisa.gov/sbom)). En la **instalación**, se pueden cambiar los valores predeterminados y colocar el dispositivo en la zona de red adecuada. Durante la **operación**, necesita supervisión, parches cuando sea posible y controles compensatorios cuando no. Al **fin del soporte**, el fabricante deja de publicar correcciones; el dispositivo sigue funcionando, y precisamente por eso sigue en servicio. En la **eliminación**, hay que borrar los datos. Una estación de trabajo de imagenología hospitalaria comprada en 2014 con un sistema operativo cuyo soporte terminó en 2020 no es una anomalía fruto del descuido; es la consecuencia normal de un dispositivo médico de 15 años sobre un sistema operativo de 10 años.

### 2.4 Ejemplo resuelto: imagenología del Calder Valley Hospital (sintético)

**Este caso es sintético.** El departamento de imagenología del CVH utiliza la estación de trabajo IMG-01, conectada a un escáner certificado por su fabricante con un sistema operativo concreto que llegó al fin de su soporte en 2020. El fabricante ofrece una actualización solo con un escáner nuevo (£400.000). Las opciones son: (a) sustituirlo ahora; (b) conservarlo y aislarlo, es decir, permitir solo las conexiones que necesita con el archivo de imágenes, eliminar el correo electrónico y la navegación web y supervisar su tráfico; (c) no hacer nada. La opción (c) deja una máquina con vulnerabilidades conocidas sin parchear en una red clínica plana. La opción (a) elimina el riesgo, pero cuesta un presupuesto de capital del que el hospital no dispone este año. La opción (b) es la respuesta habitual: un **control compensatorio** que reduce la exposición hasta la sustitución, con un responsable designado y una fecha de sustitución. El registro de la decisión indica qué riesgo permanece (un archivo malicioso que llegue a través de la conexión con el archivo) y cómo se supervisa.

### 2.5 Actividad práctica

Elija un dispositivo que use a diario (un teléfono, un router doméstico, un portátil). Sin abrirlo ni cambiar nada, averigüe en las páginas públicas del fabricante: su versión de firmware o de sistema operativo, si sigue teniendo soporte y cómo se distribuyen las actualizaciones. Escriba una nota de ciclo de vida de cinco líneas: adquisición, instalación, operación, fin del soporte, eliminación. Haga lo mismo con un dispositivo *imaginario* de un servicio crítico, una bomba de infusión del CVH, y enumere lo que necesitaría preguntar a su fabricante. Para la bomba, pregunte al fabricante por el proceso de actualización de la biblioteca de fármacos, la fecha de fin del soporte de su firmware y quién puede instalar las actualizaciones.

### 2.6 Errores comunes y límites

- Suponer que «todavía funciona» significa «todavía es seguro»: los dispositivos sin soporte acumulan vulnerabilidades sin corregir.
- Tratar la TO como TI: reiniciar un controlador durante la operación, o escanearlo de forma agresiva, puede perturbar el proceso físico.
- Ignorar el firmware: es código, tiene vulnerabilidades y rara vez se inventaría.
- Olvidar a las personas como capa: la mayoría de los sistemas los configura alguien bajo presión de tiempo.

En el CVH los cuatro errores coinciden en IMG-01: todavía funciona, así que siguió en la red clínica; la certificación de su escáner lo asemeja a la TO en sus restricciones de parcheo; nadie inventarió su firmware; y los técnicos de radiología que lo usan eligieron la configuración del escritorio compartido. El límite de este capítulo es que nombra las capas sin medir cuántos dispositivos hay en cada una.

### Ejercicios — capítulo 2

**EX003 — Localizar la decisión.** *Objetivo:* relacionar capas con controles. *Entradas:* cinco controles: actualizaciones de firmware firmadas, cuentas de usuario del sistema operativo, los límites de la biblioteca de fármacos de una aplicación, copias de seguridad de la base de datos, formación del personal. *Pasos:* asigne cada uno a una capa e indique una falla que cada control no aborda. *Evidencia esperada:* una tabla de cinco filas. *Rúbrica:* 3 = capas correctas y una carencia plausible para cada una; 2 = un error; 1 = solo las capas; 0 = nada.

**EX004 — ¿TI o TO?** *Objetivo:* razonar sobre las consecuencias. *Entradas:* el sistema de facturación de CPN, la RTU de alimentador de CPN, el sistema de administración de pacientes del CVH, el BMS del CVH que controla la ventilación de los quirófanos. *Pasos:* clasifique cada uno como TI, TO o dispositivo médico; nombre la peor consecuencia plausible de su falla; diga si probablemente se necesita una ventana de parcheo aprobada por el fabricante. *Evidencia esperada:* la tabla y dos frases sobre el BMS. *Rúbrica:* 3 = clases correctas, consecuencias vinculadas a efectos físicos en la TO; 2 = un desliz menor; 1 = solo las clases; 0 = nada.

### Síntesis del capítulo

Los sistemas informáticos son pilas de confianza, del hardware a las personas. La TO y los dispositivos médicos controlan resultados físicos, viven durante décadas y no siempre pueden parchearse, por lo que la seguridad depende de las condiciones de adquisición, la ubicación y los controles compensatorios. El componente más antiguo y con menos soporte suele definir la exposición real.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Siga estudiando — capítulo 02 de 40

[← Capítulo 01](#ch-01) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 03 →](#ch-03)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Capítulo 3 — Programación I

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) escribir programas breves en Python con variables, condiciones, bucles, funciones, listas y diccionarios; (2) leer texto estructurado (CSV) con la biblioteca estándar; (3) convertir una pregunta sobre un sistema («¿qué dispositivos han superado el fin de su soporte?») en un filtro, un recuento y un informe; y (4) probar un programa con un caso pequeño cuya respuesta ya conoce. Se apoya en el ciclo de vida de los dispositivos del capítulo 2 y prepara el capítulo 8, en el que los programas se vuelven robustos frente a entradas defectuosas.

### 3.1 Por qué programa un estudiante de seguridad

El trabajo de seguridad en los servicios críticos consiste sobre todo en saber qué se tiene y en advertir qué ha cambiado. Ambas cosas exigen procesar datos: inventarios con miles de filas, registros con millones de líneas, avisos publicados a diario. Una hoja de cálculo sirve para cincuenta filas; un programa breve sirve para cincuenta mil y puede volver a ejecutarse mañana. Aquí se usa Python porque su biblioteca estándar lee CSV, JSON, fechas y bases de datos sin instalar nada, y porque el código legible es más fácil de revisar, una propiedad que importa cuando su resultado informa una decisión sobre la seguridad de los pacientes.

### 3.2 Las construcciones básicas

Una **variable** da nombre a un valor (`year = 2026`). Una **condición** elige entre caminos (`if eos < year:`). Un **bucle** repite el trabajo para cada elemento (`for row in rows:`). Una **función** empaqueta un paso con un nombre y unas entradas para poder probarlo por separado. Una **lista** contiene elementos en orden; un **diccionario** asocia claves con valores (`row["os"]`). El módulo `csv` convierte cada línea de un archivo CSV en un diccionario cuyas claves son las del encabezado. La clase `collections.Counter` cuenta cuántas veces aparece cada valor. Con esto se puede responder a la mayoría de las preguntas sobre un inventario.

Dos disciplinas importan desde el principio. Primero, **pruebe con una respuesta conocida**: antes de ejecutar sobre el archivo real, ejecute sobre cinco filas que comprobó a mano. Segundo, **imprima lo que excluyó**, no solo lo que encontró: un filtro que descarta en silencio las filas con la fecha en blanco informará de «ningún dispositivo sin soporte» precisamente para los dispositivos que nadie documentó.

### 3.3 Ejemplo resuelto y Lab 2: clasificación del inventario del CVH (sintético)

**Este caso es sintético.** El equipo de ingeniería clínica del CVH exporta una muestra de ocho filas de su inventario de dispositivos. La pregunta: ¿qué dispositivos ejecutan software que ha superado el fin de su soporte, dónde están y hay algún dispositivo no clínico en la red clínica?

```python
# Lab 2 - triage a synthetic hospital device inventory with the standard library (offline)
import csv, io
from collections import Counter
DATA = """asset,type,os,os_end_of_support,network,clinical
INF-01,infusion pump,RTOS-x 2.1,2030,clinical-vlan,yes
INF-02,infusion pump,RTOS-x 1.4,2021,clinical-vlan,yes
IMG-01,imaging workstation,Windows 7,2020,clinical-vlan,yes
IMG-02,imaging workstation,Windows 10,2025,clinical-vlan,yes
LAB-01,lab analyser,Linux 3.10,2019,lab-vlan,yes
ADM-01,office pc,Windows 11,2031,corporate,no
ADM-02,office pc,Windows 10,2025,clinical-vlan,no
BMS-01,building controller,vendor fw 4,2027,bms-vlan,no
"""
YEAR = 2026
rows = list(csv.DictReader(io.StringIO(DATA)))
unsupported = [r for r in rows if int(r["os_end_of_support"]) < YEAR]
print("assets:", len(rows), "| unsupported:", len(unsupported))
for r in unsupported:
    print(f"  {r['asset']:7} {r['type']:20} {r['os']:12} EoS {r['os_end_of_support']} clinical={r['clinical']}")
print("by network:", dict(Counter(r["network"] for r in unsupported)))
misplaced = [r["asset"] for r in rows if r["clinical"] == "no" and r["network"] == "clinical-vlan"]
print("non-clinical devices on clinical VLAN:", misplaced)
```

Salida esperada:

```text
assets: 8 | unsupported: 5
  INF-02  infusion pump        RTOS-x 1.4   EoS 2021 clinical=yes
  IMG-01  imaging workstation  Windows 7    EoS 2020 clinical=yes
  IMG-02  imaging workstation  Windows 10   EoS 2025 clinical=yes
  LAB-01  lab analyser         Linux 3.10   EoS 2019 clinical=yes
  ADM-02  office pc            Windows 10   EoS 2025 clinical=no
by network: {'clinical-vlan': 4, 'lab-vlan': 1}
non-clinical devices on clinical VLAN: ['ADM-02']
```

Interpretación: cuatro dispositivos clínicos no tienen soporte, lo que es un problema de planificación de sustituciones con controles compensatorios (capítulo 2). ADM-02 es distinto: un PC de oficina sin soporte en la red clínica es el hallazgo más barato de corregir; actualícelo y muévalo. Las filas son datos didácticos: las etiquetas de los dispositivos son inventadas y, aunque algunos nombres de sistemas operativos resulten familiares, trate cada año de fin de soporte como una entrada de muestra y compruebe cualquier producto real con la página de ciclo de vida que publica su fabricante.

### 3.4 Actividad práctica

Amplíe el Lab 2: (1) añada una fila con `os_end_of_support` vacío y observe el error; (2) cambie el programa para que esas filas se notifiquen como «desconocido: necesita responsable» en lugar de provocar un fallo o ser omitidas; (3) escriba un `assert` que compruebe que el recuento de dispositivos sin soporte para las ocho filas originales es 5. El paso (2) es el importante. Una fila notificada como «desconocido: necesita responsable» pone nombre a una carencia; una fila omitida la oculta, y un fallo detiene el informe para todos. El `assert` del paso (3) es una prueba con respuesta conocida: si un cambio posterior en el filtro hace que imprima 4 o 6, la prueba falla antes de que nadie lea un informe erróneo.

### 3.5 Errores comunes y límites

- Comparar números almacenados como texto (`"2025" < "2026"` funciona por casualidad; `"9" < "10"` no).
- Omitir en silencio las filas mal formadas.
- Fijar en el código el año actual, de modo que el informe quede obsoleto; léalo del reloj, pero manténgalo fijo en las pruebas.
- Tratar una exportación del inventario como la verdad: solo es tan buena como la última persona que la actualizó (capítulo 22).

En el Lab 2, el segundo error habría ocultado VEN-01 en EX005; el tercero habría hecho que los dispositivos de 2025 volvieran a parecer con soporte si el año se hubiera quedado en 2025; y el cuarto se aplica a toda la exportación: ADM-02 aparece en la VLAN clínica solo porque alguien registró correctamente su red.

### Ejercicios — capítulo 3

**EX005 — Lo desconocido es un hallazgo.** *Objetivo:* hacer visibles los datos que faltan. *Entradas:* el Lab 2 más una novena fila `VEN-01,ventilator,,,clinical-vlan,yes`. *Pasos:* modifique el programa para que imprima una sección de desconocidos; explique por qué una fecha de soporte desconocida en un ventilador debe escalarse. *Evidencia esperada:* el cambio en el código, la salida y dos frases. *Rúbrica:* 3 = sin fallo, VEN-01 notificado como desconocido, razón de escalamiento vinculada a la consecuencia clínica; 2 = funciona, sin razonamiento; 1 = evita el fallo omitiendo la fila; 0 = nada.

**EX006 — Una función que se puede probar.** *Objetivo:* separar la lógica de los datos. *Entradas:* el Lab 2. *Pasos:* escriba `def is_unsupported(row, year) -> bool`, pruébela con tres filas hechas a mano (con soporte, sin soporte y el año límite igual a `year`) y enuncie su regla para el límite. *Evidencia esperada:* la función, las pruebas y la regla. *Rúbrica:* 3 = función correcta, las tres pruebas, regla del límite enunciada y justificada; 2 = no se discute el límite; 1 = solo la función; 0 = nada.

### Síntesis del capítulo

Los programas breves y legibles convierten los inventarios en decisiones. Filtre, cuente e informe, y notifique siempre lo que no pudo clasificar. Pruebe con casos que conoce, mantenga la lógica en funciones y recuerde que el programa solo es tan veraz como sus datos.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Siga estudiando — capítulo 03 de 40

[← Capítulo 02](#ch-02) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 04 →](#ch-04)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Capítulo 4 — Redacción académica

### Resultados de aprendizaje y conexión

Después de este capítulo usted podrá (1) estructurar un argumento técnico breve como afirmación, evidencia, razonamiento y límites; (2) citar las fuentes de modo que el lector pueda encontrar exactamente aquello en lo que usted se basó; (3) escribir para dos públicos a la vez, un especialista que comprobará su razonamiento y una persona que decide y dispone de cinco minutos; y (4) distinguir su propio análisis de lo que dice una fuente. Se apoya en los supuestos explícitos del capítulo 1 y prepara el capítulo 18 (métodos de investigación) y la tesis final (capítulo 40).

### 4.1 Escribir forma parte del trabajo de seguridad

En los servicios críticos, gran parte del trabajo de seguridad termina en un documento: una evaluación de riesgos, un informe de incidente, una recomendación a un consejo de administración, una presentación ante un regulador. Un análisis correcto mal escrito a menudo se ignora; un análisis bien escrito con un supuesto oculto puede engañar a toda una organización. La redacción académica entrena para ambos problemas. Su núcleo es el **argumento**: una afirmación sostenida por evidencia mediante un razonamiento explícito, con sus límites reconocidos. El modelo de Toulmin nombra estas partes: afirmación, datos (evidencia), garantía (el razonamiento que los conecta), respaldo, calificador y refutación ([Toulmin, *The Uses of Argument*](https://doi.org/10.1017/CBO9780511840005)). No necesita este vocabulario en cada párrafo, pero debe poder señalar cada parte.

### 4.2 Una estructura para dos lectores

Ponga primero la conclusión. Quien decide lee el primer párrafo; el especialista lo lee todo. Una estructura útil para un informe breve es: **resumen** (la recomendación y su razón principal, en tres frases); **contexto** (qué servicio, qué pregunta, qué alcance); **evidencia** (qué examinó y qué encontró, con fuentes); **análisis** (cómo sostiene la evidencia la recomendación y qué alternativas comparó); **límites** (qué no examinó y qué cambiaría su conclusión); **referencias**. Use encabezados que digan algo («Los dispositivos sin soporte se concentran en imagenología») en lugar de etiquetas («Hallazgos»).

### 4.3 Citación y honestidad

Cite una fuente siempre que enuncie un hecho que no estableció usted mismo, y cite el documento concreto (el número y la revisión de la publicación del NIST, el identificador del aviso de la agencia, el DOI del artículo), no «según el NIST». Cite textualmente con moderación y con exactitud; parafrasee con sus propias palabras y cite igualmente. Separe la **información** («El aviso de CISA indica que…») de la **inferencia** («esto sugiere que…») y de la **recomendación** («el CVH debería…»). Nunca cite una fuente que no haya leído; si se basa en un resumen de una norma de pago, cite el resumen. Las herramientas generativas pueden redactar textos fluidos que contienen citas inventadas: cada referencia de su trabajo debe ser una que usted abrió y comprobó.

### 4.4 Ejemplo resuelto: reescritura de un párrafo débil (sintético)

**Débil (borrador sintético de un estudiante):** «Los hospitales son muy vulnerables a los ciberataques, como todo el mundo sabe por WannaCry. El CVH tiene muchos computadores viejos, así que corre un riesgo alto y debería comprar un cortafuegos nuevo». Problemas: una afirmación universal sin sustento («todo el mundo sabe»); un incidente real usado sin fuente ni lección precisa; «muchos» y «alto» sin números; una recomendación que no se deriva de la evidencia (los computadores viejos no se arreglan con un cortafuegos). **Revisado:** «La National Audit Office del Reino Unido constató que el ransomware WannaCry de 2017 perturbó al menos a un tercio de los *trusts* del NHS en Inglaterra, y que las organizaciones afectadas tenían sistemas Windows sin parches o sin soporte ([NAO, 2017](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/)). El inventario de muestra del CVH muestra cuatro de cinco dispositivos clínicos con el soporte vencido (capítulo 3, Lab 2). Recomendamos aislar estos dispositivos para que solo tengan las conexiones que necesitan y fijar fechas de sustitución, en lugar de confiar en un cortafuegos perimetral, porque el caso de la NAO muestra que el daño se propagó dentro de las redes hospitalarias. Esta recomendación supone que la muestra es representativa; se necesita un inventario completo para confirmarla».

### 4.5 Actividad práctica

Tome un artículo de prensa de una página sobre cualquier incidente de infraestructura. Escriba un informe de 250 palabras para la dirección de un hospital: un resumen de tres frases, lo que se sabe (con el artículo y cualquier fuente primaria que cite), lo que es incierto y una pregunta que el CVH debería hacerse. Marque cada frase con R (información), I (inferencia) o C (recomendación). Un buen informe mantiene visiblemente separados los tres tipos de frase. «La empresa de servicios informó de un corte de seis horas (R)» es información; «el corte probablemente comenzó en el sistema de facturación (I)» es una inferencia y debe indicar su fundamento; «el CVH debería comprobar si su propio sistema de facturación puede detener el trabajo clínico (C)» es una recomendación. Cuando el artículo cite una fuente primaria, ábrala y cítela en su lugar.

### 4.6 Errores comunes y límites

- Enterrar la conclusión en la página cuatro.
- Citar un resumen secundario como si fuera la fuente primaria.
- Palabras que ocultan cantidades: «muchos», «significativo», «crítico» sin un número ni una definición.
- Recomendaciones que no se derivan de la evidencia presentada.
- El plagio, incluida la paráfrasis cercana sin cita y el texto generado por IA no declarado.

El párrafo débil del ejemplo resuelto muestra cuatro de ellos a la vez: «todo el mundo sabe» oculta una fuente, «muchos computadores viejos» oculta un recuento, «riesgo alto» oculta una definición y «comprar un cortafuegos nuevo» no se deriva de los dispositivos sin soporte. El quinto error es el que los evaluadores comprueban de forma mecánica: una frase cercana a la redacción del informe de la NAO sin cita es plagio aunque los hechos sean correctos.

### Ejercicios — capítulo 4

**EX007 — Encontrar la garantía.** *Objetivo:* sacar a la luz el razonamiento oculto. *Entradas:* «El sistema de pagos de Calder Mutual no tuvo ninguna caída el año pasado, así que es seguro». *Pasos:* identifique la afirmación, la evidencia y la garantía no enunciada; explique por qué falla la garantía; reescriba la afirmación para que la evidencia la sostenga. *Evidencia esperada:* tres partes etiquetadas y una frase reescrita. *Rúbrica:* 3 = garantía identificada («la ausencia de caídas implica la ausencia de debilidades»), falla explicada, reescritura defendible; 2 = parcial; 1 = solo afirmación y evidencia; 0 = nada.

**EX008 — Primero el resumen.** *Objetivo:* escribir para quien decide. *Entradas:* el ejemplo resuelto del capítulo 1. *Pasos:* escriba un resumen de 120 palabras que recomiende la opción B e incluya la razón principal, el supuesto principal y lo que cambiaría la recomendación. *Evidencia esperada:* el resumen. *Rúbrica:* 3 = recomendación en la primera frase, razón, supuesto y condición de reversión, ≤ 120 palabras; 2 = falta un elemento; 1 = recomendación enterrada; 0 = nada.

### Síntesis del capítulo

La buena redacción de seguridad enuncia una afirmación, muestra la evidencia, hace explícito el razonamiento y admite los límites: primero la conclusión, fuentes exactas y la información separada de la inferencia y de la recomendación. Escriba como si un especialista fuera a comprobar cada frase y quien decide fuera a leer solo las tres primeras.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Siga estudiando — capítulo 04 de 40

[← Capítulo 03](#ch-03) · [Índice de capítulos del curso](../SUBJECTS.md) · [Capítulo 05 →](../../en/book/MANUSCRIPT.md#ch-05)

Continúe con la siguiente lección escrita.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Resultados resueltos y notas de evaluación

Las respuestas son resultados modelo, no las únicas aceptables. Acepte una respuesta distinta que cumpla el mismo nivel de evidencia, de razonamiento y de honestidad sobre los límites. Los números se refieren a los datos sintéticos de este libro.

**EX001.** Unidades: (1/año) × h × (£/h) = £/año. El resultado es £1.920 **por año**, no por hora. Escribir «por hora» haría que el escenario pareciera 8.760 veces mayor de lo que es al compararlo con un costo anual de £18.000, lo que invertiría la decisión.

**EX002.** Si se reducen a la mitad las probabilidades de B, la pérdida evitada es la mitad de £9.600 = **£4.800** al año (cociente 0,40). Si las estimaciones de probabilidad originales se duplicaran y el control siguiera reduciéndolas a la mitad, la pérdida evitada sería la mitad de £19.200 = **£9.600**. Recomendación: B sigue siendo preferible porque su peor evento creíble (72 h sin energía de respaldo en un hospital) es el mayor daño para las personas, y la comparación por valor esperado favorece a B con ambos supuestos; la incertidumbre en las probabilidades no cambia la clasificación.

**EX003.** Actualizaciones de firmware firmadas: capa de firmware (no aborda una actualización maliciosa pero correctamente firmada procedente de un fabricante comprometido). Cuentas de usuario del sistema operativo: sistema operativo (no impiden el error de un usuario autorizado). Límites de la biblioteca de fármacos: aplicación (no detectan un fármaco equivocado elegido dentro de los límites). Copias de seguridad de la base de datos: datos (no ayudan si las copias también se cifran o nunca se restauran). Formación del personal: personas (no detiene siempre un señuelo convincente y dirigido).

**EX004.** Facturación: TI (lo peor: interrupción de los ingresos y de la atención al cliente; parcheo normal). RTU de alimentador: TO (lo peor: pérdida de visibilidad o de control de la distribución; ventana aprobada por el fabricante). Administración de pacientes: TI, pero clínicamente importante (lo peor: atención retrasada por pérdida de la programación y de los registros; parcheo normal con control de cambios clínico). BMS de la ventilación de quirófanos: TO en un entorno sanitario (lo peor: renovaciones de aire inseguras que obligan a cancelar cirugías o crean riesgo de infección; coordinación entre mantenimiento de instalaciones y personal clínico, y ventana aprobada por el fabricante). El BMS muestra que los «sistemas del edificio» son TO cuyas consecuencias son clínicas.

**EX005.** Cambie el filtro para tratar por separado `row["os_end_of_support"] == ""`: `unknown = [r for r in rows if not r["os_end_of_support"].strip()]`, notifíquelos bajo «DESCONOCIDO: necesita responsable» y calcule `unsupported` solo a partir de las filas con fecha. La salida añade `VEN-01 ventilator`. Un ventilador con estado de soporte desconocido es un equipo de soporte vital en la red clínica cuya exposición a parches nadie puede precisar; escálelo a ingeniería clínica para obtener la declaración de soporte del fabricante y revisar su ubicación.

**EX006.** `def is_unsupported(row, year): return int(row["os_end_of_support"]) < year`. Pruebas: fin de soporte 2030 → False; 2020 → True; fin de soporte igual a `year` (2026) → False con esta regla. Regla enunciada: un dispositivo cuyo soporte termina *durante* el año en curso todavía tiene soporte ahora, pero debe señalarse en una lista aparte de «termina este año»; una regla alternativa defendible trata `<=` como sin soporte, para ser conservadora. Cualquiera de las dos es aceptable si se enuncia y se prueba.

**EX007.** Afirmación: «el sistema de pagos es seguro». Evidencia: «ninguna caída el año pasado». Garantía: «la ausencia de caídas implica la ausencia de debilidades explotables», que es falsa, porque las debilidades pueden no haberse explotado, la explotación puede no causar ninguna caída (fraude, robo de datos) o pasar inadvertida. Reescritura sostenida por la evidencia: «El sistema de pagos de Calder Mutual no tuvo ninguna caída registrada el año pasado; esto, por sí solo, no dice nada sobre su exposición a ataques, que requiere una evaluación».

**EX008.** Modelo (≈ 100 palabras): «Recomendamos financiar el programa de pruebas de los generadores del hospital (opción B). Evita una pérdida esperada estimada de £9.600 al año frente a un costo de £12.000, en comparación con £4.320 frente a £18.000 de un segundo enlace para el centro de despacho, y aborda el peor caso más grave: hasta 72 horas sin energía de respaldo en el Calder Valley Hospital. Estas estimaciones suponen que las probabilidades de corte son correctas dentro de un factor de dos; la clasificación se mantiene en todo ese intervalo. Revisaríamos la elección si nueva evidencia mostrara que la única ruta de cable del enlace de despacho corre un riesgo mucho mayor, por ejemplo durante obras viales planificadas».

<a id="glossary"></a>

## Glosario

- **Lista de permitidos (*allowlist*)**: política que permite solo los flujos, programas, valores o usuarios enumerados; todo lo demás se deniega.
- **Ancla**: copia de confianza de la cabeza de una cadena de hashes, guardada fuera del alcance de quien controla el registro.
- **Autonomía (de respaldo)**: cuánto tiempo sigue funcionando un servicio por sí mismo con su energía, almacenamiento o proceso manual de respaldo.
- **Tasa base**: frecuencia de una condición antes de cualquier prueba o alerta; domina el significado de una alerta.
- **Causa común / modo común**: una sola causa que anula varias salvaguardas supuestamente independientes.
- **Control compensatorio**: medida que reduce la exposición cuando el control preferido (por ejemplo, aplicar parches) no es posible.
- **Conducto**: vía de comunicación controlada entre zonas.
- **Análisis centrado en las consecuencias**: análisis de riesgos que parte de los resultados inaceptables y rastrea los caminos que llevan a ellos (por ejemplo, CCE).
- **Restricción (de decisión)**: requisito que excluye opciones con independencia de su puntuación.
- **Función crítica**: función (por ejemplo, «suministrar agua») cuya interrupción dañaría gravemente a la sociedad.
- **DMZ**: zona de red entre los sistemas corporativos y los de control para el intercambio controlado de datos.
- **Pérdida anual esperada (EAL)**: probabilidad por año multiplicada por la pérdida por evento, sumada sobre los escenarios.
- **FMEA**: análisis de modos de falla y sus efectos; análisis ascendente de cómo fallan los componentes y qué sigue a esas fallas.
- **Árbol de fallas**: modelo descendente de un evento no deseado, construido con puertas AND y OR sobre eventos básicos.
- **HMAC**: código de autenticación de mensajes con clave, construido a partir de una función hash.
- **HMI**: interfaz humano-máquina que usan los operadores para ver y controlar un proceso.
- **Kappa (de Cohen)**: grado de acuerdo entre dos codificadores corregido por el azar.
- **Mínimo privilegio**: dar a cada usuario o programa solo el acceso que necesita.
- **TO (tecnología operacional)**: sistemas que supervisan o controlan procesos físicos.
- **Precisión / exhaustividad**: la proporción de alertas que son reales / la proporción de eventos reales que se detectan.
- **Reglas de enfrentamiento (RoE)**: condiciones escritas que autorizan una prueba o un ejercicio: alcance, métodos, ventana, condiciones de parada.
- **SCADA**: supervisión, control y adquisición de datos; supervisión de amplia área de los lazos de control.
- **Análisis de sensibilidad**: comprobar si una decisión cambia cuando cambian las entradas inciertas o las ponderaciones.
- **SIS**: sistema instrumentado de seguridad; protección automática independiente que lleva un proceso a un estado seguro.
- **STPA**: análisis de procesos basado en la teoría de sistemas; encuentra acciones de control inseguras en una estructura de control.
- **Combinación tóxica**: conjunto de funciones que una misma persona no debe ostentar (separación de funciones).
- **Validación / verificación**: cumplir el propósito en el entorno real / cumplir la especificación.
- **Intervalo de Wilson**: intervalo de confianza para una proporción que se comporta bien con muestras pequeñas.
- **Zona**: grupo de activos con requisitos de seguridad similares.

<a id="references"></a>

## Referencias

Las leyes, las normas, las orientaciones y las páginas sobre incidentes cambian. Las versiones y fechas que siguen son las consultadas para este borrador (octubre de 2026); vuelva a verificarlas antes de basarse en ellas. La lista es idéntica a la de la edición en inglés; los títulos de las obras se citan en su idioma original.

**Política, derecho, normas y marcos**

- Cybersecurity and Infrastructure Security Agency. [Critical Infrastructure Sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- Cybersecurity and Infrastructure Security Agency. [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
- Cybersecurity and Infrastructure Security Agency. [ICS Advisories](https://www.cisa.gov/news-events/ics-advisories).
- Cybersecurity and Infrastructure Security Agency. [Coordinated Vulnerability Disclosure (CVD) Program](https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program).
- Cybersecurity and Infrastructure Security Agency. [Secure by Design](https://www.cisa.gov/securebydesign).
- Cybersecurity and Infrastructure Security Agency. [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom).
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Official Journal, 4 May 2016.
- European Union. [Directive (EU) 2022/2555 (NIS2 Directive)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/). Official Journal, 27 December 2022.
- European Union. [Directive (EU) 2022/2557 on the resilience of critical entities (CER Directive)](https://eur-lex.europa.eu/eli/dir/2022/2557/oj). Official Journal, 27 December 2022.
- European Union. [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). Official Journal, 27 December 2022.
- Idaho National Laboratory. [Consequence-driven Cyber-informed Engineering (CCE)](https://inl.gov/national-security/cce/).
- International Electrotechnical Commission. [IEC 62443-3-2:2020 — Security risk assessment for system design (catalogue page)](https://webstore.iec.ch/en/publication/30727).
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- MITRE. [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/).
- Modbus Organization. [Modbus Application Protocol Specification](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf).
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework). February 2024.
- National Institute of Standards and Technology. [NIST Privacy Framework](https://www.nist.gov/privacy-framework).
- National Institute of Standards and Technology. [SP 800-30 Rev. 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final). September 2012.
- National Institute of Standards and Technology. [SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025.
- National Institute of Standards and Technology. [SP 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management](https://csrc.nist.gov/pubs/sp/800/63/b/upd2/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final). September 2023.
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., and McQuaid, R. [SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems: A Systems Security Engineering Approach](https://doi.org/10.6028/NIST.SP.800-160v2r1). NIST, December 2021.
- National Institute of Standards and Technology. [SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final). August 2020.
- National Institute of Standards and Technology. [SP 800-218, Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final). February 2022.
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final); [FIPS 197, Advanced Encryption Standard](https://csrc.nist.gov/pubs/fips/197/final); [FIPS 198-1, The Keyed-Hash Message Authentication Code (HMAC)](https://csrc.nist.gov/pubs/fips/198-1/final).
- National Institute of Standards and Technology. [NIST Releases First 3 Finalized Post-Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). 13 August 2024.
- North American Electric Reliability Corporation. [Critical Infrastructure Protection (CIP) Standards](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).
- Open Source Security Foundation. [SLSA — Supply-chain Levels for Software Artifacts](https://slsa.dev/).
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, February 1997.
- Rescorla, E. [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446). IETF, August 2018.
- Eddy, W. (ed.). [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293). IETF, August 2022.
- U.S. Department of Health and Human Services. [Healthcare and Public Health Cybersecurity Performance Goals](https://hphcyber.hhs.gov/performance-goals.html). January 2024.
- U.S. Environmental Protection Agency. [America's Water Infrastructure Act of 2018: Risk Assessments and Emergency Response Plans](https://www.epa.gov/waterresilience/americas-water-infrastructure-act-2018-risk-assessments-and-emergency-response-plans).

**Ética profesional**

- Association for Computing Machinery. [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics). 2018.

**Incidentes y evidencia sectorial**

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [Compromise of U.S. Water Treatment Facility (AA21-042A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). February 2021.
- Cybersecurity and Infrastructure Security Agency and Federal Bureau of Investigation. [DarkSide Ransomware: Best Practices for Preventing Business Disruption from Ransomware Attacks (AA21-131A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a). May 2021, updated July 2021.
- Cybersecurity and Infrastructure Security Agency. [The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years](https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years). May 2023.
- Cybersecurity and Infrastructure Security Agency. [MAR-17-352-01 HatMan — Safety System Targeted Malware (Update B)](https://www.cisa.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%20-%20Safety%20System%20Targeted%20Malware%20%28Update%20B%29.pdf). 2019.
- E-ISAC and SANS. [Analysis of the Cyber Attack on the Ukrainian Power Grid: Defense Use Case](https://nsarchive.gwu.edu/document/15331-sans-and-electricity-information-sharing-and). March 2016 (archived copy).
- Langner, R. [Stuxnet: Dissecting a Cyberwarfare Weapon](https://doi.org/10.1109/MSP.2011.67). *IEEE Security & Privacy*, 9(3), 49–51, 2011.
- Microsoft. [Helping Our Customers Through the CrowdStrike Outage](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). 20 July 2024.
- National Audit Office. [Investigation: WannaCry Cyber Attack and the NHS](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/). October 2017.
- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems*, 21(6), 11–25, 2001.
- WUSF Public Media. [Former Oldsmar City Manager Says 2021 Water Treatment Plant 'Hack' Was Likely Employee Error](https://www.wusf.org/local-state/2023-04-13/official-hack-oldsmar-city-water-treatment-plant-2021). 13 April 2023.

**Informática, seguridad, seguridad funcional y resiliencia**

- Bruneau, M., Chang, S. E., Eguchi, R. T., et al. [A Framework to Quantitatively Assess and Enhance the Seismic Resilience of Communities](https://doi.org/10.1193/1.1623497). *Earthquake Spectra*, 19(4), 733–752, 2003.
- Codd, E. F. [A Relational Model of Data for Large Shared Data Banks](https://doi.org/10.1145/362384.362685). *Communications of the ACM*, 13(6), 377–387, 1970.
- Diffie, W., and Hellman, M. [New Directions in Cryptography](https://doi.org/10.1109/TIT.1976.1055638). *IEEE Transactions on Information Theory*, 22(6), 644–654, 1976.
- Haimes, Y. Y. [On the Definition of Resilience in Systems](https://doi.org/10.1111/j.1539-6924.2009.01216.x). *Risk Analysis*, 29(4), 498–501, 2009.
- Leveson, N. [A New Accident Model for Engineering Safer Systems](https://doi.org/10.1016/S0925-7535(03)00047-X). *Safety Science*, 42(4), 237–270, 2004.
- Reason, J. [Human Error: Models and Management](https://doi.org/10.1136/bmj.320.7237.768). *BMJ*, 320(7237), 768–770, 2000.
- Rivest, R. L., Shamir, A., and Adleman, L. [A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](https://doi.org/10.1145/359340.359342). *Communications of the ACM*, 21(2), 120–126, 1978.
- Saltzer, J. H., and Schroeder, M. D. [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939). *Proceedings of the IEEE*, 63(9), 1278–1308, 1975.

**Evidencia, investigación y argumentación**

- Arp, D., Quiring, E., Pendlebury, F., et al. [Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/conference/usenixsecurity22/presentation/arp). *USENIX Security Symposium*, 2022.
- Efron, B. [Bootstrap Methods: Another Look at the Jackknife](https://doi.org/10.1214/aos/1176344552). *The Annals of Statistics*, 7(1), 1–26, 1979.
- Kim, S., Choi, K., Choi, H.-S., Lee, B., and Yoon, S. [Towards a Rigorous Evaluation of Time-Series Anomaly Detection](https://ojs.aaai.org/index.php/AAAI/article/view/20680). *AAAI*, 2022.
- Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E. [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285). *PLoS Computational Biology*, 9(10), e1003285, 2013.
- Sargent, R. G. [Verification and Validation of Simulation Models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation*, 7(1), 12–24, 2013.
- Sommer, R., and Paxson, V. [Outside the Closed World: On Using Machine Learning for Network Intrusion Detection](https://doi.org/10.1109/SP.2010.25). *IEEE Symposium on Security and Privacy*, 2010.
- Toulmin, S. E. [The Uses of Argument](https://doi.org/10.1017/CBO9780511840005). Updated edition, Cambridge University Press, 2003 (first published 1958).
- Wilson, E. B. [Probable Inference, the Law of Succession, and Statistical Inference](https://doi.org/10.1080/01621459.1927.10502953). *Journal of the American Statistical Association*, 22(158), 209–212, 1927.
